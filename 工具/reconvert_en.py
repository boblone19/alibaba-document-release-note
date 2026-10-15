"""用升级版 pdf2md 重转全部英文 Markdown：补回目录（Table of Contents）与标题编号。

背景：旧转换把封面/目录页连同正文一起裁掉，且标题编号（"1.1."）被剥掉，
导致 md 里既没有目录也没有编号。升级后的 pdf2md 会
  * 保留标题编号（### 1.1 What is API Gateway）；
  * 正文最前面输出由 PDF 书签重建的 ## Table of Contents；
  * 用书签全标题补全页面上被折行截断的标题。

  python3 工具/reconvert_en.py --plan            只统计
  python3 工具/reconvert_en.py --limit 3         先试 3 本
  python3 工具/reconvert_en.py                   全量重转（断点续跑：已带新标记的跳过）

流程：按缓存索引取 lang=en 且已登记 markdown 的行 → 从 source_url 重下 PDF
（暂存 .scratch/pdf_reconvert_en/）→ 原地覆盖同名 md（title/版本号沿用旧 front matter）
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
SCRATCH = os.path.join(ROOT, os.pardir, os.pardir, ".scratch", "pdf_reconvert_en")
NEW_TAG = "toc+numbered-headings"


def quoted(url):
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((p.scheme, p.netloc, urllib.parse.quote(p.path, safe='/%'), p.query, p.fragment))


def front_matter(md_path):
    """沿用旧 md 的 title/版本号/源 URL，保证文件元数据不漂移。"""
    head = open(md_path, encoding="utf-8").read(3000)

    def g(k):
        m = re.search(rf'^{k}: "(.*)"\s*$', head, re.M)
        return m.group(1) if m else ""
    return g("title"), g("product_version"), g("doc_version"), g("source_url")


def already_done(md_path):
    try:
        return NEW_TAG in open(md_path, encoding="utf-8").read(3000)
    except OSError:
        return False


def worker(row):
    md_path = os.path.join(ROOT, row["markdown"])
    title, prodver, docver, src_url = front_matter(md_path)
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
                                      prodver=prodver, docver=docver)
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
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()

    cached = cache.load(ROOT)
    rows = [r for r in cached.values() if r.get("lang") == "en" and r.get("markdown")
            and os.path.exists(os.path.join(ROOT, r["markdown"]))]
    todo = rows if a.force else [r for r in rows if not already_done(os.path.join(ROOT, r["markdown"]))]
    if a.limit:
        todo = todo[: a.limit]
    print(f"英文 {len(rows)} 本，待重转 {len(todo)} 本 → {SCRATCH}")
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
