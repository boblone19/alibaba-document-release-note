#!/usr/bin/env python3
"""把英文树的文件名从"官方书名"改成"产品名 + 手册类型 + 日期"。

背景：markdown/10_EN_ApsaraStack_<版本>/<产品目录>/<官方书名>.md 的文件名前缀
"Alibaba Cloud Apsara Stack [Enterprise] [版本]" 里的版本信息，父目录 10_EN_ApsaraStack_<版本>
已经有了，白占 30~45 个字符；产品路径又和产品目录名重复一遍。Windows 单路径上限 260 字符，
951 本里有 175 本的完整路径超限，去掉这段前缀后降到 77 本（剩下的由产品目录名决定，
那是目录改名的事，见 tools/rename_en_dirs.py）。

    python3 tools/rename_en_files.py                 # 试跑：出迁移表 + 冲突检查，不动文件
    python3 tools/rename_en_files.py --apply          # 真改名 + 改索引/清单/全仓引用
    python3 tools/rename_en_files.py --apply --limit 5   # 试点 5 本

只动 markdown/10_EN_* 下的**文件名**：目录结构、正文、云端键（mdCloudKey / pdfCloud）一律不动；
索引里的 label / title 仍是官方书名，原书身份不丢。
"""
import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cache  # noqa: E402

EN_PREFIX = "10_EN_ApsaraStack_"
MD_ROOT = os.path.join(ROOT, "markdown")

# 手册类型（长的一定排在前面，从文件名尾部往回匹配）
TYPES = ["Introduction to Instance Families and Instance Types",
         "Operations and Maintenance Operations Guide",
         "Operations and Maintenance Guide", "Security Administrator Guide",
         "Product Introduction", "Operations and Maintenance", "Developer Guide",
         "User Guide", "Operations Guide", "Administrator Guide", "Migration Guide",
         "Deployment Guide", "API Reference", "Release Notes", "Best Practices",
         "Glossary", "Whitepaper", "Overview", "Introduction"]

# 文件名里"版本目录已经有了"的那段前缀，只在产品名与父目录对不上时才用
STACK_PREFIX = re.compile(
    r"^(?:Alibaba\s+Cloud\s+)?Apsara\s+Stack(?:\s+Enterprise)?(?:\s+apsara\s+base)?"
    r"(?:\s+[vV]?\d+(?:\.\d+)*(?:-\w+)?)?\s+")

REWRITE = ["README.md", "markdown/README.md", "doc_cache_index.json", "doc_cache_index.csv",
           "download_ledger.json", "download_ledger.md", "all_docs_overview.html",
           "cn_en_manual_map.csv", "doc_index.csv", "doc_details.json",
           "ApsaraStack-3.18.6-Release-Note-EN.md", "ApsaraStack-V3.18.6_2607-Release-Note-EN.md",
           "00_product_catalog_candidates.md", "dingtalk_docpack_index.md",
           "markdown/conversion_manifest.csv", "markdown/conversion_manifest.json",
           "markdown/conversion_manifest_zh.json", "ApsaraStack_Markdown_split_manifest.json"]


def en_md_files():
    out = []
    for d in sorted(os.listdir(MD_ROOT)):
        if not d.startswith(EN_PREFIX):
            continue
        for root, _ds, fs in os.walk(os.path.join(MD_ROOT, d)):
            for f in fs:
                if f.endswith(".md"):
                    out.append(os.path.join(root, f))
    return out


def split_stem(stem):
    """'Alibaba Cloud Apsara Stack V3.18.6 API Gateway User Guide 20260828'
        -> ('Alibaba Cloud Apsara Stack V3.18.6 API Gateway', 'User Guide', '20260828', None)"""
    m = re.search(r"(\d{8})(?:\s*\((\d+)\))?$", stem)
    if not m:
        return None
    date, dup = m.group(1), m.group(2)
    body = stem[: m.start()].rstrip()
    dt = ""
    for t in TYPES:
        if body.lower().endswith(" " + t.lower()):
            dt = t
            break
    prod = body[: len(body) - len(dt)].strip() if dt else body
    return prod, dt, date, dup


def new_name(stem, parent):
    """算出该文件的新文件名；识别不出前缀就返回 None（不动它）。"""
    parts = split_stem(stem)
    if not parts:
        return None
    prod, dt, date, dup = parts
    if parent and dt and parent.lower().endswith(" " + dt.lower()):
        product, dt = parent, ""               # 目录名自带手册类型（如 Apsara Stack Security
    elif parent and prod.endswith(parent):     # Security Administrator Guide），不再重复一遍
        product = parent                      # 产品路径就是父目录名 → 只砍掉前面的版本前缀
    else:
        m = STACK_PREFIX.match(prod)
        product = prod[m.end():].strip() if m else prod
    if not product:
        return None
    s = product + ((" " + dt) if dt else "") + " " + date
    if dup:
        s += f" ({dup})"
    return s + ".md"


def build_plan(limit=0):
    """返回 [(旧绝对路径, 新绝对路径)]。"""
    plan = []
    for p in en_md_files():
        stem = os.path.basename(p)[:-3]
        parent = os.path.basename(os.path.dirname(p))
        nn = new_name(stem, parent)
        if not nn or nn == stem + ".md":
            continue
        plan.append((p, os.path.join(os.path.dirname(p), nn)))
        if limit and len(plan) >= limit:
            break
    return plan


def check_collisions(plan):
    seen, bad = {}, []
    for _o, n in plan:
        k = n.lower()
        if k in seen:
            bad.append((seen[k], n))
        seen[k] = n
    return bad


def rewrite_refs(plan, apply_it):
    """全仓文本里把旧文件名换成新文件名（长的先换，避免前缀吃掉后缀）。"""
    pairs = sorted(((os.path.basename(o), os.path.basename(n)) for o, n in plan),
                   key=lambda x: -len(x[0]))
    targets = list(REWRITE) + sorted(glob.glob(os.path.join(MD_ROOT, "_preview-samples", "*.html")))
    hits = {}
    for f in targets:
        p = os.path.join(ROOT, f)
        if not os.path.exists(p):
            continue
        try:
            t = open(p, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        orig = t
        for old, new in pairs:
            t = t.replace(old, new)
        if t != orig:
            hits[f] = sum(1 for o, _ in pairs if o in orig)
            if apply_it:
                open(p, "w", encoding="utf-8").write(t)
    return hits


def update_index(plan, apply_it):
    """索引里 markdown 字段换成新路径；label / localPath / 云端键保持官方原样。"""
    by_old = {os.path.basename(o): os.path.basename(n) for o, n in plan}
    rows = json.load(open(os.path.join(ROOT, cache.JSON_NAME), encoding="utf-8"))
    n = 0
    for r in rows:
        md = (r.get("markdown") or "").replace("\\", "/")
        if not md:
            continue
        base = md.rsplit("/", 1)[-1]
        if base in by_old:
            r["markdown"] = md[: md.rfind("/") + 1] + by_old[base]
            n += 1
    if apply_it and n:
        cache.save(ROOT, rows)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="只改前 N 本（试点用）")
    a = ap.parse_args()

    plan = build_plan(a.limit)
    bad = check_collisions(plan)
    if not plan:
        print("没有可改的文件（文件名已经不含版本前缀了？）")
        return 0
    old_len = sum(len(os.path.basename(o)) for o, _ in plan)
    new_len = sum(len(os.path.basename(n)) for _, n in plan)
    print(f"待改名 {len(plan)} 本 | 文件名平均 {old_len/len(plan):.0f} → {new_len/len(plan):.0f} 字符")
    over = sum(1 for o, n in plan if len(o) > 260)
    over2 = sum(1 for o, n in plan if len(n) > 260)
    print(f"完整路径 >260 字符：{over} → {over2}")
    for o, n in plan[:6]:
        print(f"   {os.path.basename(o)[:74]}\n     -> {os.path.basename(n)}")
    if bad:
        print(f"目标撞名 {len(bad)} 处，拒绝执行：")
        for x, y in bad[:10]:
            print(f"   {x}\n   {y}")
        return 1
    if not a.apply:
        print("（试跑，未改动。加 --apply 才改）")
        return 0

    moved = 0
    for o, n in plan:
        if os.path.exists(n):
            print(f"   目标已存在，跳过：{n}")
            continue
        os.replace(o, n)
        moved += 1
    n_idx = update_index(plan, True)
    hits = rewrite_refs(plan, True)
    print(f"改名 {moved} 本 | 索引改路径 {n_idx} 条")
    print("改了引用的文件：" + (", ".join(f"{k}({v})" for k, v in hits.items()) or "无"))
    left = [p for p in en_md_files()
            if os.path.basename(p).startswith("Alibaba Cloud Apsara Stack ")
            and not os.path.basename(os.path.dirname(p)).startswith("Alibaba Cloud Apsara Stack")]
    print(f"复查：文件名仍带套件前缀、且父目录不是同名产品的 {len(left)} 本")
    for p in left[:5]:
        print("   ", os.path.relpath(p, ROOT))
    miss = [r["markdown"] for r in json.load(open(os.path.join(ROOT, cache.JSON_NAME), encoding="utf-8"))
            if r.get("markdown") and not os.path.exists(os.path.join(ROOT, r["markdown"]))]
    print(f"索引里登记但文件不存在的：{len(miss)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
