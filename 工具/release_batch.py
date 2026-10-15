"""按发布版本批量接入新文档：下载 → 转 Markdown → 校验 → 写回缓存索引 → 删 PDF。

  python3 工具/release_batch.py --manifest ../../.scratch/en_all.json --version V3.18.6_2607 --limit 3
  python3 工具/release_batch.py --manifest ../../.scratch/en_all.json --version V3.18.6_2607
  加 --no-delete 保留 PDF（默认转完即删，交付树只留 Markdown）。

只做一件事：把 list_docs.py 产出的候选落成交付树里的 Markdown + 缓存索引行。
并发：下载 8 线程（IO），转换 6 进程（CPU，PyMuPDF 释放 GIL，实测比线程快 ~2.5x）。
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from functools import partial

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cache  # noqa: E402
import pdf2md  # noqa: E402

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
SCRATCH = os.path.join(ROOT, os.pardir, os.pardir, ".scratch")


def quoted(url):
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((p.scheme, p.netloc, urllib.parse.quote(p.path, safe='/%'), p.query, p.fragment))


def get_size(url):
    """Range 探体积：0 流量拿到真实总字节（key 含空格/中文，必须先 quote）。"""
    req = urllib.request.Request(quoted(url), headers={"User-Agent": UA, "Range": "bytes=0-0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        cr = r.headers.get("Content-Range") or ""
        return int(cr.rsplit("/", 1)[-1]) if "/" in cr else -1


def pdf_path(row, pdf_dir):
    """暂存 PDF 的路径 = localPath 的形态（产品子目录 / 含日期文件名.pdf）"""
    rel = (row.get("localPath") or f"en/{safe(row['label'])}.pdf").split("/", 1)[-1]
    return os.path.join(pdf_dir, rel)


def download(row, pdf_dir=None):
    dest = pdf_path(row, pdf_dir)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        req = urllib.request.Request(quoted(row["url"]), headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=600) as h:
            data = h.read()
    except Exception as ex:
        return row, f"下载失败 {ex!r}"[:160]
    if data[:5] != b"%PDF-":
        return row, "响应不是 PDF"
    open(dest, "wb").write(data)
    row["_pdf"], row["_bytes"] = dest, len(data)
    return row, None


def safe(name, limit=120):
    return re.sub(r'[\\/:*?"<>|\x00-\x1f]+', "_", name).strip(" ._")[:limit]


def convert_one(row, md_dir=None):
    out = pdf_path(row, md_dir)[:-4] + ".md"      # 与 PDF 同名，仅扩展名不同
    os.makedirs(os.path.dirname(out), exist_ok=True)
    nchars, err = None, None
    try:
        nchars, err = pdf2md.convert(row["_pdf"], out, url=row["url"], title=row["label"],
                                    prodver=row.get("version", ""), docver=row.get("versionStamp", ""))
    except Exception as ex:
        err = f"转换异常 {ex!r}"[:160]
    if err:
        return row, err
    if not os.path.exists(out) or os.path.getsize(out) < 800:
        return row, "Markdown 过小或为空"
    body = open(out, encoding="utf-8").read()
    # 只拦真正的图片嵌入。正文里的 (?![0-9]) 这类 Grok/正则片段包含 "![",
    # 早先用 "![" in body 会把 CDS 用户指南整本误判为含图丢弃（踩过）。
    if re.search(r"!\[[^\]]*\]\((?:data:|[^)]*\.(?:png|jpe?g|gif|webp|bmp))", body):
        return row, "含图片嵌入（应为纯文本）"
    import pymupdf
    with pymupdf.open(row["_pdf"]) as d:
        row["_pages"] = d.page_count
    row["_md"], row["_mdrel"], row["_sha"], row["_chars"] = out, os.path.relpath(out, ROOT), cache.sha256(out), nchars
    return row, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--md-prefix", default="10_EN_ApsaraStack_")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dl-workers", type=int, default=8)
    ap.add_argument("--cv-workers", type=int, default=6)
    ap.add_argument("--no-delete", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="只探体积不下载")
    a = ap.parse_args()

    rows_all = json.load(open(a.manifest, encoding="utf-8"))
    rows = [r for r in rows_all if r.get("version") == a.version]
    if a.limit:
        rows = rows[: a.limit]
    cached = cache.load(ROOT)                      # dict：id -> 行
    done_before = [r for r in rows if r["id"] in cached
                   and cached[r["id"]].get("markdownSha256")
                   and os.path.exists(os.path.join(ROOT, cached[r["id"]]["markdown"]))]
    rows = [r for r in rows if r not in done_before]
    print(f"版本 {a.version}：清单 {len(rows_all)} 条 → 本版本 {len(rows) + len(done_before)} 本，"
          f"已登记跳过 {len(done_before)} 本，待处理 {len(rows)} 本")

    pdf_dir = os.path.join(SCRATCH, "pdf_" + safe(a.version))
    md_dir = os.path.join(ROOT, "markdown", a.md_prefix + safe(a.version))
    os.makedirs(pdf_dir, exist_ok=True)
    os.makedirs(md_dir, exist_ok=True)

    if a.dry_run:
        with cf.ThreadPoolExecutor(a.dl_workers) as ex:
            sizes = list(ex.map(get_size, [r["url"] for r in rows]))
        bad = sum(1 for s in sizes if s < 0)
        print(f"探体积：成功 {len(sizes) - bad} / 失败 {bad} → {sum(s for s in sizes if s > 0)/1048576:.0f} MB")
        return 0

    print(f"[1/4] 下载 → {os.path.relpath(pdf_dir, ROOT)}")
    errs, done, downloaded = [], 0, []
    with cf.ThreadPoolExecutor(a.dl_workers) as ex:
        for row, err in ex.map(partial(download, pdf_dir=pdf_dir), rows):
            done += 1
            if err:
                errs.append(("download", row["label"][:50], err))
            elif row.get("_pdf"):
                downloaded.append(row)          # 跨线程也要显式收集，不依赖共享可变对象
            if done % 20 == 0:
                print(f"      … {done}/{len(rows)}")
    got = downloaded
    print(f"      完成 {len(got)} 本，失败 {len(errs)}")

    print(f"[2/4] 转换 → markdown/{os.path.basename(md_dir)}（每本成功即登记并删 PDF）")
    ok, errs_before = [], len(errs)
    cached = cache.load(ROOT)          # dict：id -> 行

    def book(r):
        row = {k: v for k, v in r.items() if not k.startswith("_")}
        row.update({"key": f"{r['id']}@{r['versionStamp']}", "manualCode": r["versionStamp"],
                    "pages": r.get("_pages"), "bytes": r.get("_bytes"), "prodVer": "",
                    "markdown": r["_mdrel"], "markdownSha256": r["_sha"], "mdChars": r.get("_chars"),
                    "pdfLocal": bool(a.no_delete), "pdfCloud": "",
                    "category": r.get("category") or r.get("docType")})
        row.setdefault("productCode", "")
        cached[r["id"]] = {**cached.get(r["id"], {}), **row}

    n = 0
    # 逐本落账：中断也不丢已完成部分（上一版全批结束才写索引，进程被杀就白跑）
    with cf.ProcessPoolExecutor(a.cv_workers) as ex:
        futs = [ex.submit(convert_one, r, md_dir) for r in got]
        for f in cf.as_completed(futs):
            row, err = f.result()
            n += 1
            if err:
                errs.append(("convert", row["label"][:50], err))
                continue
            ok.append(row)
            book(row)
            if not a.no_delete:
                try:
                    os.remove(row["_pdf"])       # 交付树只留 Markdown
                except OSError:
                    pass
            if n % 20 == 0:
                cache.save(ROOT, list(cached.values()))
                print(f"      … {n}/{len(got)} 已登记 {len(ok)}")
    cache.save(ROOT, list(cached.values()))
    print(f"[3/4] 缓存索引已更新：本次新增/刷新 {len(ok)} 本，转换失败 {len(errs) - errs_before} 本")
    print(f"      索引现共 {len(cached)} 条")

    if not a.no_delete:
        import shutil
        shutil.rmtree(pdf_dir, ignore_errors=True)
        print(f"[4/4] 已删除 PDF 暂存目录（交付树只留 Markdown）")
    else:
        print(f"[4/4] 保留 PDF 于 {os.path.relpath(pdf_dir, ROOT)}")

    by = {}
    for kind, label, msg in errs:
        by.setdefault(kind, []).append((label, msg))
    for k, v in by.items():
        print(f"  {k} 失败 {len(v)}：")
        for label, msg in v[:8]:
            print(f"     {label} → {msg}")
    json.dump([r["label"] for _, r in enumerate(ok)], open(os.path.join(
        SCRATCH, f"batch_{safe(a.version)}.json"), "w"), ensure_ascii=False)
    return 1 if by.get("convert") or by.get("download") else 0


if __name__ == "__main__":
    sys.exit(main())
