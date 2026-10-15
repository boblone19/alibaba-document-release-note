"""Shared cache helper — the single source of truth for "已下载 + 已转换".

  id        稳定身份：中文 = 手册 URL；英文 = 去掉 8 位发布日期的 URL
  key/stamp 版本戳：英文取文件名日期，中文取册内「文档版本」日期
  markdown / markdownSha256  该册是否已转成 Markdown 及其内容指纹

标签语义（pull_docs.py 与转换脚本都按它动作）：
  SKIP     同 id 同 stamp 且已有 markdown  → 不下载、不转换
  FETCH    同 id 但 stamp 更新（官方发了新版）→ 只下这一本
  CONVERT  已登记但还没 markdown           → 只转，不重复下载
  NEW      没见过的 id（新手册/新产品）      → 下载后转换
缓存文件同时以 .json（程序读）与 .csv（人看）两份保存，并同步到 OSS，
所以沙箱重置后仍能据此判定，不会重新下载已转过 MD 的同一份 PDF。
"""
import csv
import hashlib
import json
import os
import re
import urllib.parse

FIELDS = ["id", "lang", "stack", "version", "versionStamp", "productCode", "product", "category",
          "docType", "label", "pages", "bytes", "prodVer", "pdfLocal", "pdfCloud", "markdown",
          "markdownKB", "markdownSha256", "url", "localPath", "mdCloudKey", "inScope"]
JSON_NAME = "文档缓存索引.json"
CSV_NAME = "文档缓存索引.csv"


def _date_in(name):
    m = re.search(r"(\d{8})", name.rsplit("/", 1)[-1])
    return m.group(1) if m else ""


def identity(lang, url):
    """Return (id, versionStamp) for a manual URL."""
    path = urllib.parse.unquote(urllib.parse.urlsplit(url or "").path)
    stamp = _date_in(path)
    ident = f"{lang}:" + (re.sub(r"\d{8}(?=\.pdf$)", "", path) if lang == "en" else path)
    return ident, stamp


def load(dest):
    p = os.path.join(dest, JSON_NAME)
    if not os.path.exists(p):
        return {}
    return {r["id"]: r for r in json.load(open(p, encoding="utf-8"))}


def save(dest, rows):
    rows = sorted(rows, key=lambda r: (r.get("lang", ""), str(r.get("productCode")), str(r.get("docType"))))
    json.dump(rows, open(os.path.join(dest, JSON_NAME), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open(os.path.join(dest, CSV_NAME), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        [w.writerow(r) for r in rows]
    return rows


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def decide(cached, cands):
    """Tag each candidate: (label, row-with-cache-backref)."""
    out = []
    for c in cands:
        cid = c.get("id") or ""
        stamp = c.get("versionStamp") or ""
        old = cached.get(cid)
        if old and str(old.get("versionStamp")) == stamp:
            if old.get("markdown"):
                out.append(("SKIP", {**c, "cached": old}))
            else:
                out.append(("CONVERT" if c.get("inScope", True) else "SCOPE", {**c, "cached": old}))
        elif old:
            out.append(("FETCH", {**c, "cached": old, "cachedStamp": old.get("versionStamp")}))
        else:
            out.append(("NEW", c))
    return out


def mark_converted(dest, md_rel, pdf_url, lang, pages=None):
    """Attach markdown path + content hash to the cache row for a converted manual."""
    rows = json.load(open(os.path.join(dest, JSON_NAME), encoding="utf-8"))
    cid, stamp = identity(lang, pdf_url)
    hit = [r for r in rows if r["id"] == cid]
    if not hit:
        raise KeyError(f"缓存无此 id，请先登记再标记：{cid}")
    r = hit[0]
    r["markdown"] = md_rel
    r["markdownKB"] = os.path.getsize(os.path.join(dest, md_rel)) // 1024
    r["markdownSha256"] = sha256(os.path.join(dest, md_rel))
    if stamp:
        r["versionStamp"] = stamp
    if pages:
        r["pages"] = pages
    save(dest, rows)
    return r
