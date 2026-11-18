"""用最新版 pdf2md 重转已转出的 Markdown：补回目录、标题编号、提示框引用块。

原名只转英文；现加 --lang 支持中文（文件名沿用来避免 README 里链接失效）。
英文树的演进（同一提交线）：
  * toc+numbered-headings：保留标题编号、补由书签重建的 ## Table of Contents
  * note-quotes：Note/Important/Warning 提示框输出成 Markdown 引用块

  python3 tools/reconvert_en.py --plan                 英文：只统计
  python3 tools/reconvert_en.py --lang zh --plan       中文：只统计
  python3 tools/reconvert_en.py --lang zh --limit 5    中文先试 5 本
  python3 tools/reconvert_en.py                        英文全量（断点续跑：已带最新标记的跳过）

流程：取缓存索引该语言、已有 markdown 的行 → 按 source_url/url 重下 PDF
（暂存 .scratch/pdf_reconvert_<lang>/）→ 原地覆盖同名 md（title/版本号/原始 PDF 文件名
沿用旧 front matter，中文册的 "21_手册名_code.pdf" 命名不会变成临时名）
→ 更新缓存索引（sha/KB/字符数）→ 删 PDF。转完即删，交付树只留 Markdown。
"""
import argparse
import concurrent.futures as cf
import os
import re
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cache  # noqa: E402
import pdf2md  # noqa: E402

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
SCRATCH_BASE = os.path.join(ROOT, os.pardir, os.pardir, ".scratch", "pdf_reconvert")
SCRATCH = SCRATCH_BASE + "/en"          # main() 里按 --lang 重设（fork 出来的 worker 继承）
NEW_TAG = "toc+numbered-headings+note-quotes+edge-junk"
LANG = ["en"]                                # main() 按 --lang 设置；worker 靠它定目录标题行


def quoted(url):
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((p.scheme, p.netloc, urllib.parse.quote(p.path, safe='/%'), p.query, p.fragment))


def front_matter(md_path):
    """沿用旧 md 的 title/版本号/源 URL/原 PDF 文件名，保证文件元数据不漂移。"""
    head = open(md_path, encoding="utf-8").read(3000)

    def g(k):
        m = re.search(rf'^{k}: "(.*)"\s*$', head, re.M)
        return m.group(1) if m else ""
    return (g("title"), g("product_version"), g("doc_version"), g("source_url"), g("source_pdf"))


def already_done(md_path):
    try:
        return NEW_TAG in open(md_path, encoding="utf-8").read(3000)
    except OSError:
        return False


def worker(row):
    md_path = os.path.join(ROOT, row["markdown"])
    title, prodver, docver, src_url, src_pdf = front_matter(md_path)
    url = src_url or row.get("url") or ""
    import hashlib
    real = re.sub(r'[\\/:*?"<>|]+', "_", urllib.parse.unquote(url).rsplit("/", 1)[-1])[:100]
    pdf = os.path.join(SCRATCH, hashlib.md5(url.encode()).hexdigest()[:16] + "_" + real)
    data, err = None, ""
    for _attempt in (1, 2, 3):
        try:
            req = urllib.request.Request(quoted(url), headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=600) as h:
                data = h.read()
            if data[:5] == b"%PDF-":
                break
            data, err = None, "响应不是 PDF"
        except Exception as ex:
            data, err = None, repr(ex)
    if data is None:
        return row, f"下载失败 {err}"[:160]
    open(pdf, "wb").write(data)
    try:
        nchars, cerr = pdf2md.convert(pdf, md_path, url=url, title=title or row.get("label", ""),
                                      prodver=prodver, docver=docver, src_pdf=src_pdf,
                                      lang=LANG[0])
        if not cerr:
            import pymupdf
            with pymupdf.open(pdf) as d:
                row["_pages"] = d.page_count
    except Exception as ex:
        return row, f"转换异常 {ex!r}"[:160]
    finally:
        try:
            os.remove(pdf)
        except OSError:
            pass
    if cerr:
        return row, cerr[:160]
    row["_sha"], row["_chars"], row["_kb"] = cache.sha256(md_path), nchars, os.path.getsize(md_path) // 1024
    return row, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true", help="连已带新标记的也重转")
    ap.add_argument("--only", help="只重转该 JSON 清单里列出的 md（元素含 \"md\" = 仓库相对路径），隐含 --force")
    ap.add_argument("--lang", default="en", choices=["en", "zh"], help="重转哪种语言（默认英文）")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()

    global SCRATCH
    SCRATCH = os.path.join(SCRATCH_BASE, a.lang)
    LANG[0] = a.lang
    cached = cache.load(ROOT)
    rows = [r for r in cached.values() if r.get("lang") == a.lang and r.get("markdown")
            and os.path.exists(os.path.join(ROOT, r["markdown"]))]
    todo = rows if (a.force or a.only) else [r for r in rows if not already_done(os.path.join(ROOT, r["markdown"]))]
    if a.only:
        import json
        want = {x["md"].replace("\\", "/") for x in json.load(open(a.only, encoding="utf-8"))}
        have = {r["markdown"].replace("\\", "/") for r in todo}
        todo = [r for r in todo if r["markdown"].replace("\\", "/") in want]
        print(f"清单 {len(want)} 条，索引命中 {len(todo)} 条，未登记 {len(want - have)} 条")
    if a.limit:
        todo = todo[: a.limit]
    print(f"{a.lang} 共 {len(rows)} 本已转出，待重转 {len(todo)} 本 → {SCRATCH}")
    if a.plan or not todo:
        return 0
    os.makedirs(SCRATCH, exist_ok=True)

    ok, errs = [], []
    with cf.ProcessPoolExecutor(a.workers) as ex:
        for n, (row, err) in enumerate(ex.map(worker, todo), 1):
            if err:
                errs.append((row["label"][:56], err))
                continue
            ok.append(row)
            upd = {"pages": row["_pages"], "markdownSha256": row["_sha"], "mdChars": row["_chars"],
                   "markdownKB": row["_kb"], "pdfLocal": False}
            cached[row["id"]] = {**row, **upd}
            if n % 20 == 0:
                cache.save(ROOT, list(cached.values()))
                print(f"  … {n}/{len(todo)}  完成 {len(ok)}  失败 {len(errs)}")
    cache.save(ROOT, list(cached.values()))
    print(f"重转完成 {len(ok)} 本，失败 {len(errs)} 本；缓存索引现共 {len(cached)} 条")
    for label, msg in errs[:15]:
        print(f"  失败 {label} → {msg}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
