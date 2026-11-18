#!/usr/bin/env python3
"""把英文树的目录名从"抄 OSS 中文目录"改成"英文产品名"。

背景：markdown/10_EN_ApsaraStack_<版本>/<目录>/<书名>.md 的中间那层来自 OSS 对象路径，
阿里云自己中英混着（v3.18.6 是英文产品名，V3.18.6_2607 与老版本是中文，V3.16.2 是文档类型），
还混着 20230221 / v3.12.0 这类垃圾段。改成统一用 list_docs 从书名解析出的英文 product，
product 在 951 条清单里零中文。

    python3 工具/rename_en_dirs.py            # 试跑：只报迁移表与冲突，不动文件
    python3 工具/rename_en_dirs.py --apply     # 真搬 + 改索引 + 改全仓引用
    python3 工具/rename_en_dirs.py --manifest ../../.scratch/en_all.json --apply
        # 顺手把清单里待下载书的 localPath 也换成英文目录（新一轮下载直接落对路径）

只动 markdown/10_EN_* ；中文树（01_/02_）按既定约定保留中文目录。
文件末名不变（本来就是官方英文书名），所以整棵树只是换目录，不重转。
"""
import argparse
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # 仓库根（apsara-stack-docs/）
sys.path.insert(0, HERE)
import cache  # noqa: E402

EN_PREFIX = "10_EN_ApsaraStack_"
MD_ROOT = os.path.join(ROOT, "markdown")


def safe(s, limit=120):
    s = cache.fold_ascii(s)                      # NBSP / 全角括号先折 ASCII，再判语言
    s = re.sub(r"\s+", " ", str(s or "").strip())
    s = "".join("_" if c in '\\/:*?"<>|' else c for c in s)
    return re.sub(r"_+", "_", s).strip(" ._")[:limit]


def cjk(s):
    return bool(re.search(r"[\u4e00-\u9fff]", s or ""))


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


def build_plan(rows):
    """返回 [(旧相对路径, 新相对路径)]：中间层换成英文 product，末名保留。"""
    by_md = {}
    for r in rows:
        if r.get("lang") == "en" and r.get("markdown"):
            by_md[r["markdown"].replace("\\", "/")] = r
    plan = []
    for p in en_md_files():
        rel = "markdown/" + os.path.relpath(p, MD_ROOT).replace(os.sep, "/")
        parts = rel.split("/")                      # markdown/10_EN_x/<dir>/<file>.md
        if len(parts) != 4:
            print(f"  跳过（层数不是 3）：{rel}")
            continue
        row = by_md.get(rel)
        if row is None:
            print(f"  跳过（索引里没这行，不敢猜目录名）：{rel}")
            continue
        prod = safe(row.get("product") or "", 120)
        if not prod or cjk(prod):
            print(f"  跳过（product 非纯英文）：{prod!r} ← {rel}")
            continue
        want = "/".join([parts[0], parts[1], prod, parts[3]])
        if want != rel:
            plan.append((rel, want))
    return plan


def check_collisions(plan):
    seen, bad = {}, []
    for _old, new in plan:
        if new in seen:
            bad.append(new)
        seen[new] = 1
    return bad


REWRITE = ["README.md", "markdown/README.md", "下载台账.json", "下载台账.md", "下载链接.md",
           "文档索引.csv", "文档明细.json", "全量文档清单.html", "中英对照手册映射.csv",
           "markdown/转换清单.json", "markdown/转换清单.csv",
           "ApsaraStack-3.18.6-Release-Note-EN.md", "ApsaraStack-V3.18.6_2607-Release-Note-EN.md",
           "00_产品清单_全量待选.md", "钉钉索引_文档包.md"]


def rewrite_refs(plan, apply_it):
    """全仓文本里把旧路径换成新路径；两种写法都替换（带 markdown/ 前缀与不带）。"""
    pairs = []
    for old, new in plan:
        pairs.append((old, new))                                  # markdown/10_EN_x/…
        pairs.append((old.split("/", 1)[1], new.split("/", 1)[1]))  # 10_EN_x/…
    hits = {}
    for f in REWRITE:
        p = os.path.join(ROOT, f)
        if not os.path.exists(p):
            continue
        try:
            t = open(p, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        orig = t
        for old, new in pairs:
            if old != new and old in t:
                for sep in ("", "%20"):                             # URL 里空格有两种写法
                    if sep:
                        t = t.replace(old.replace(" ", sep), new.replace(" ", sep))
                    else:
                        t = t.replace(old, new)
        if t != orig:
            n = sum(1 for o, _ in pairs if o in orig)
            hits[f] = n
            if apply_it:
                open(p, "w", encoding="utf-8").write(t)
    return hits


def patch_manifest(path, rows):
    """清单（list_docs 产物）里的 localPath 同步换英文目录，新下的书直接落对位置。"""
    if not path or not os.path.exists(path):
        return 0
    by_url = {r["url"]: safe(r.get("product") or "", 120) for r in rows if r.get("lang") == "en"}
    s = json.load(open(path, encoding="utf-8"))
    s = s if isinstance(s, list) else list(s.values())
    n = 0
    for r in s:
        lp = r.get("localPath") or ""
        prod = by_url.get(r.get("url"))
        parts = lp.split("/")
        if prod and len(parts) == 3 and parts[1] != prod:
            r["localPath"] = "/".join([parts[0], prod, parts[2]])
            n += 1
    json.dump(s, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--manifest", default="")
    a = ap.parse_args()

    rows = cache.load(ROOT)
    rowlist = list(rows.values())
    plan = build_plan(rowlist)
    bad = check_collisions(plan)
    per = {}
    for old, new in plan:
        per[("/".join(old.split("/")[:2]), "/".join(new.split("/")[:2]))] = 0
    print(f"待迁移 {len(plan)} 本，涉及 {len({(o.split('/')[1]) for o, _ in plan})} 个旧目录 → "
          f"{len({n.split('/')[2] for _, n in plan})} 个英文产品目录")
    nonascii = sum(1 for _o, n in plan if cjk(n.split("/")[2]))
    print(f"迁移后新路径里仍含中文的：{nonascii}")
    if bad:
        print(f"目标冲突 {len(bad)} 处，拒绝执行：\n  " + "\n  ".join(sorted(set(bad))[:10]))
        return 1
    if not a.apply:
        for o, n in plan[:8]:
            print(f"   {o[8:][:62]:64} → {n.split('/')[2][:36]}")
        print("（试跑，未改动。加 --apply 才搬）")
        return 0

    moved = 0
    for old, new in plan:
        so, sn = os.path.join(ROOT, old), os.path.join(ROOT, new)
        os.makedirs(os.path.dirname(sn), exist_ok=True)
        if os.path.exists(so):
            shutil.move(so, sn)
            moved += 1
    # 索引里逐条改路径：md 换目录，PDF 的 localPath 跟着同一层走（末名不变，只换扩展名）
    by_old = {o: n for o, n in plan}
    for _rid, r in rows.items():
        m = (r.get("markdown") or "").replace("\\", "/")
        if m not in by_old:
            continue
        new_md = by_old[m]
        r["markdown"] = new_md
        lp = (r.get("localPath") or "").replace("\\", "/")
        if lp:
            r["localPath"] = "/".join(new_md.split("/")[1:-1] + [os.path.basename(lp)])
    cache.save(ROOT, list(rows.values()))
    hits = rewrite_refs(plan, True)
    nman = patch_manifest(a.manifest, rowlist)
    empt = [os.path.join(MD_ROOT, d, x) for d in os.listdir(MD_ROOT) if d.startswith(EN_PREFIX)
            for x in os.listdir(os.path.join(MD_ROOT, d))
            if os.path.isdir(os.path.join(MD_ROOT, d, x)) and not os.listdir(os.path.join(MD_ROOT, d, x))]
    for e in sorted(empt, key=len, reverse=True):
        for root, ds, fs in os.walk(e, topdown=False):
            if not os.listdir(root):
                os.rmdir(root)
    print(f"搬了 {moved}/{len(plan)} 本；索引已改；清掉空目录 {len(empt)} 个")
    print("改了引用的文件：", ", ".join(f"{k}({v})" for k, v in hits.items()) or "无")
    if a.manifest:
        print(f"清单 localPath 换英文目录：{nman} 条")
    still = [p for p in en_md_files() if cjk(os.path.relpath(p, MD_ROOT).split(os.sep)[1])]
    print(f"复查：英文树里路径中间层仍含中文的书 {len(still)} 本")
    return 0


if __name__ == "__main__":
    sys.exit(main())
