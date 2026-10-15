"""Fetch + convert the extra English corpus needed for the 3.18.6 vs 3.16.2 release note.

Groups:
  A) V3.18.6 English manuals outside the earlier 4-class scope (cache rows without markdown) — 68
  B) V3.16.2 English manuals, re-listed live via list_docs (no cache entries yet) — ~53

Per manual: download PDF → convert to text-only Markdown at markdown/<same tree> → delete the PDF
→ record id/versionStamp/bytes/pages/markdown/sha256 in 文档缓存索引.json+csv so the next run
SKIPs it. Cache is flushed every 10 manuals; interrupted runs resume from the cache.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cache      # noqa: E402
import list_docs  # noqa: E402
import pdf2md     # noqa: E402

ROOT = os.path.dirname(HERE)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
V162 = "V3.16.2"
os.chdir(ROOT)


def safe(s, limit=120):
    s = re.sub(r"\s+", " ", str(s or "").strip())
    s = "".join("_" if c in '\\/:*?"<>|' else c for c in s)
    return re.sub(r"_+", "_", s).strip(" ._")[:limit]


def build(rows):
    by_id = {r["id"]: r for r in rows}
    todo = []
    for r in rows:                                     # A: 3.18.6 补类
        if r["lang"] == "en" and r["version"] == "V3.18.6" and not r.get("markdown"):
            todo.append((r, False))
    for c in list_docs.en_list(V162):                 # B: 3.16.2
        if c["id"] in by_id:
            continue
        fn = urllib.parse.unquote(c["url"]).rsplit("/", 1)[-1]
        row = {k: "" for k in cache.FIELDS}
        row.update({"id": c["id"], "key": c["id"] + "@" + c["versionStamp"], "lang": "en",
                    "stack": "apsara-stack-intl", "version": V162, "versionStamp": c["versionStamp"],
                    "productCode": c["productCode"], "product": c["product"], "category": c["docType"],
                    "docType": c["docType"], "label": fn[:-4], "pages": None, "bytes": None,
                    "prodVer": V162, "pdfLocal": False, "pdfCloud": "", "markdown": "",
                    "markdownKB": 0, "markdownSha256": "", "url": c["url"],
                    "localPath": f"10_EN_{V162}/{safe(c['docType'], 40)}/{safe(c['product'])}/{fn}",
                    "mdCloudKey": "", "inScope": True, "addedFor": "release note A/B 补料"})
        rows.append(row)
        todo.append((row, True))
    return rows, todo


def one(job):
    row, _new = job
    rel, url = row["localPath"], row["url"]
    p = os.path.join(ROOT, rel)
    try:
        data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}),
                                      timeout=600).read()
    except Exception as ex:
        return ("DLFAIL", rel, repr(ex)[:70])
    if data[:5] != b"%PDF-":
        return ("MAGIC", rel, "")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "wb").write(data)
    md = os.path.join("markdown", rel[:-4] + ".md")
    out = os.path.join(ROOT, md)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    title = f"{row['product']} {row['docType']}".strip()
    n, err = pdf2md.convert(p, out, url=url, title=title,
                            prodver=row.get("prodVer") or row.get("version", ""),
                            docver=row.get("versionStamp", ""))
    os.remove(p)                                       # 不留 PDF
    if not n:
        return ("MDFAIL", rel, (err or "")[:70])
    pages = None
    head = open(out, encoding="utf-8").read(4000)
    mm = re.search(r"^pdf_pages:\s*(\d+)", head, re.M)
    if mm:
        pages = int(mm.group(1))
    row.update({"bytes": len(data), "pdfLocal": False, "markdown": md,
                "markdownKB": os.path.getsize(out) // 1024, "pages": pages,
                "markdownSha256": cache.sha256(out), "mdCloudKey": "本地待打包"})
    return ("OK", rel, f"{len(data)/1048576:.1f}MB→{row['markdownKB']}KB/{pages or '?'}p")


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    rows = json.load(open("文档缓存索引.json", encoding="utf-8"))
    rows, todo = build(rows)
    print(f"待处理 {len(todo)} 本（A 补类 + B {V162}）｜进程 {workers}", flush=True)
    t0, stat, done = time.time(), {}, 0
    with ThreadPoolExecutor(workers) as ex:
        for i, res in enumerate(ex.map(one, todo), 1):
            stat[res[0]] = stat.get(res[0], 0) + 1
            done = i
            if res[0] != "OK" or i % 12 == 0:
                print(f"  [{i}/{len(todo)}] {res[0]:<7} {os.path.basename(res[1])[:40]:<42} {res[2]}"
                      f"  {(time.time()-t0)/60:5.1f}min", flush=True)
            if i % 10 == 0:
                cache.save(ROOT, rows)                 # 断点可续
    cache.save(ROOT, rows)
    ok = stat.get("OK", 0)
    print(f"\n完成 {ok}/{len(todo)} 统计 {stat}｜用时 {(time.time()-t0)/60:.1f} min")
    print(f"缓存 {len(rows)} 条，其中已转 Markdown {sum(1 for x in rows if x['markdown'])}；"
          f"本地 PDF 残留 {sum(1 for x in rows if x['pdfLocal'])}")
    return 0 if ok == len(todo) else 1


if __name__ == "__main__":
    sys.exit(main())
