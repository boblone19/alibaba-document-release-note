"""Decide and fetch: never re-download a PDF whose Markdown is already in the cache.

  python3 工具/pull_docs.py --plan                     只打印决策
  python3 工具/pull_docs.py --fetch --limit 5          只下需要的那几本（按 url 直取单本）
  python3 工具/pull_docs.py --fetch --langs zh         中文侧同理

候选来源：--manifest（list_docs.py 输出）或缓存自身（核对既有登记）。
标签见 工具/cache.py：SKIP=同 id 同版本戳且已转，直接跳过下载与转换；
FETCH=官方发了新版；CONVERT=有 PDF 但缺 Markdown；NEW=没登记过。
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cache  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"


def candidates(path, langs):
    rows = json.load(open(path, encoding="utf-8")) if path else \
        json.load(open(os.path.join(ROOT, cache.JSON_NAME), encoding="utf-8"))
    out = []
    for r in rows:
        if langs and r.get("lang") not in langs:
            continue
        url = r.get("url") or r.get("sourceUrl") or ""
        cid, stamp = cache.identity(r["lang"], url)
        out.append({**r, "id": r.get("id") or cid, "versionStamp": r.get("versionStamp") or stamp, "url": url})
    return out


def need_pdf(c):
    """需要重新下载的条件：本地无实体 PDF，且云端也没有登记过可取回的包。
    （有 pdfCloud 记录时优先从云端包/已转 Markdown 里拿，不重新下官方 PDF。）"""
    lp = c.get("localPath")
    if lp and os.path.exists(os.path.join(ROOT, lp)):
        return False
    return not c.get("pdfCloud")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="")
    ap.add_argument("--langs", default="")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--into-tree", action="store_true", help="按缓存登记的 localPath 写入交付树")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--to", default="/tmp/pulltest",
                    help="临时落地目录；加 --into-tree 则按缓存路径写回交付树")
    a = ap.parse_args()
    langs = [x.strip() for x in a.langs.split(",") if x.strip()]
    cands = candidates(a.manifest, langs)
    decided = cache.decide(cache.load(ROOT), cands)
    tally = Counter(lab for lab, _ in decided)
    print(f"候选 {len(cands)} → {dict(tally)}")
    pdf_needed = [(lab, c) for lab, c in decided if lab in ("NEW", "FETCH")
                  or (lab == "CONVERT" and need_pdf(c))]
    print(f"其中需要下载 PDF 的: {len(pdf_needed)} 本 "
          f"（SKIP {tally.get('SKIP', 0)} 条一次都不会下载）")
    for lab, c in pdf_needed[:6]:
        print(f"   {lab:<8} {str(c.get('product'))[:24]:<26} {str(c.get('docType'))[:22]:<24} "
              f"stamp={c.get('versionStamp')} 缓存={c.get('cachedStamp', '—')}")
    if not a.fetch:
        return 0
    todo = pdf_needed[: a.limit or len(pdf_needed)]
    ok = bad = 0
    for lab, c in todo:
        url = c["url"]
        name = urllib.parse.unquote(url).rsplit("/", 1)[-1]
        p = os.path.join(ROOT, c["localPath"]) if (a.into_tree and c.get("localPath")) else \
            os.path.join(a.to, c.get("lang", "?"), name)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=240) as h:
                data = h.read()
        except Exception as ex:
            print("   下载失败:", name[:40], repr(ex)[:70])
            bad += 1
            continue
        if data[:5] != b"%PDF-":
            print("   非 PDF:", name[:40])
            bad += 1
            continue
        open(p, "wb").write(data)
        if c.get("bytes") and int(c["bytes"]) != len(data):
            print(f"   字节与登记不符({len(data)} vs {c['bytes']}) 但已存:", name[:36])
        ok += 1
        print(f"   已下 {ok}: {name[:56]} {len(data)/1024:.0f} KB")
    print(f"下载完成 {ok} 本，失败 {bad} 本 → {a.to}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
