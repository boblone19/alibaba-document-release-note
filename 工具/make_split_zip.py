#!/usr/bin/env python3
"""把 markdown/ 打成多个 ZIP 分卷，每卷压缩后不超过上限（默认 45 MB；GitHub 单文件软限 50 MB）。

为什么分卷：整包 1,247 册共 63.5 MB，越过 GitHub 的 50 MB 提示线，再补版本线会顶到 100 MB 硬限。
分卷比 LFS 轻：不改历史、不需要 git-lfs 配置，clone 出来就能按卷下载。

装箱规则
  * 先按 markdown/ 的顶层目录（= 一个 stack 版本线）分组，实测每组压缩后字节数，
    再 First-Fit-Decreasing 装进各卷 —— 一个版本线绝不跨卷，所以单独下一卷解压就是
    那一版本完整可读的 Markdown；根下的散文件（README、清单）单独成组同样整块放。
  * 每卷都是独立 zip（不是 .z01 切片），可单独 testzip / 解压，不需要"全到齐再拼"。
  * 产出 分卷清单.json：卷名、字节数、sha256、条目数、包含哪些版本线、合并顺序。
  * 某一组本身就超上限时直接报错，绝不腰斩一个版本线。

    python3 工具/make_split_zip.py --plan                  # 只看分组与预估体积
    python3 工具/make_split_zip.py                         # 生成分卷 + 清单，并自动 --verify
    python3 工具/make_split_zip.py --max-mb 40 --prefix ApsaraStack_Markdown
    python3 工具/make_split_zip.py --verify                # 只验（尺寸上限 / sha256 / zip 完整 / 与盘上一致 / 覆盖全）
"""
import argparse
import hashlib
import io
import json
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "markdown")
MANIFEST = "分卷清单.json"


def all_files():
    out = []
    for root, dirs, files in os.walk(SRC):
        dirs.sort()
        for f in sorted(files):
            out.append(os.path.relpath(os.path.join(root, f), SRC).replace(os.sep, "/"))
    return out


def groups_of(paths):
    g = {}
    for p in paths:
        g.setdefault(p.split("/")[0] if "/" in p else "(根文件)", []).append(p)
    return g


def compressed_size(names):
    """实测这一组进 zip 后占多少字节（与整卷同参数，避免靠比例估）。"""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for n in names:
            z.write(os.path.join(SRC, n), n)
    return len(buf.getvalue())


def pack(groups, limit, cache_size, parts=None):
    """装箱：先按上限算最少卷数，再用 LPT（大组先放、每次丢进当前最小的卷）均衡。

    这样每卷体积接近 total/卷数，而不是第一卷塞到贴上限、最后一卷空着 —— 留出增长余量，
    也避免下一卷小得没意义。绝不在中途把一个版本线拆成两半。"""
    order = sorted(groups, key=lambda k: -cache_size[k])
    total = sum(cache_size.values())
    if order and cache_size[order[0]] > limit:
        raise SystemExit(f"分组 {order[0]!r} 压缩后 {cache_size[order[0]]/1048576:.2f} MB 已超上限 "
                         f"{limit/1048576:.2f} MB；要更小只能按文件二次切分，而那样会腰斩版本线")
    n = parts or max(1, -(-int(total) // int(limit)))
    bins = [[0, []] for _ in range(n)]
    for k in order:                       # Largest-Processing-Time：放最小的那个卷
        b = min(bins, key=lambda x: x[0])        # 只取一次：先更新体积再取会挑错卷
        b[0] += cache_size[k]
        b[1].append(k)
    out = [sorted(b[1]) for b in bins if b[1]]
    if max(b[0] for b in bins) > limit:
        raise SystemExit(f"均衡后仍有卷超上限，请把 --max-mb 调小或 --parts 调大")
    return out


def prune_old(prefix):
    n = 0
    for f in os.listdir(ROOT):
        if re.match(rf"^{re.escape(prefix)}_Part\d+Of\d+\.zip$", f) or f == MANIFEST:
            os.remove(os.path.join(ROOT, f))
            n += 1
    return n


def build(prefix, max_mb, plan_only, parts=None):
    paths = all_files()
    grp = groups_of(paths)
    sizes = {k: compressed_size(v) for k, v in grp.items()}
    plan = pack(grp, int(max_mb * 1048576), sizes, parts)
    print(f"markdown/：{len(paths)} 个条目，{len(grp)} 个顶层分组，压缩后合计 {sum(sizes.values())/1048576:.2f} MB")
    for k in sorted(grp, key=lambda x: -sizes[x]):
        print(f"   组 {sizes[k]/1048576:6.2f} MB / {len(grp[k]):>4} 项  {k}")
    print(f"\n装箱（每卷 ≤{max_mb} MB）：{len(plan)} 卷")
    for i, tops in enumerate(plan, 1):
        mb = sum(sizes[t] for t in tops) / 1048576
        print(f"   卷{i}: {mb:5.2f} MB  ← {', '.join(tops)}")
    if plan_only:
        return 0

    prune_old(prefix)
    n = len(plan)
    rec = []
    for i, tops in enumerate(plan, 1):
        name = f"{prefix}_Part{i}Of{n}.zip"
        p = os.path.join(ROOT, name)
        with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            cnt = 0
            for t in tops:
                for f in grp[t]:
                    z.write(os.path.join(SRC, f), f)
                    cnt += 1
        blob = open(p, "rb").read()
        if len(blob) > int(max_mb * 1048576):
            os.remove(p)
            raise SystemExit(f"{name} 实际 {len(blob)/1048576:.2f} MB 超上限，请降 --max-mb")
        rec.append({"file": name, "bytes": len(blob), "MB": round(len(blob) / 1048576, 2),
                    "entries": cnt, "sha256": hashlib.sha256(blob).hexdigest(), "contains": tops})
        print(f"   写出 {name}: {len(blob)/1048576:.2f} MB / {cnt} 条目")
    m = {"policy": "按顶层目录（=stack 版本线）整块装箱，版本线与根级清单文件都不跨卷；"
                   "每卷是独立 zip，可单独下载解压，不需要按顺序拼接",
         "maxFileMB": max_mb, "source": "markdown/", "parts": rec,
         "totalMB": round(sum(r["bytes"] for r in rec) / 1048576, 2),
         "entries": sum(r["entries"] for r in rec),
         "download": [r["file"] for r in rec],
         "verify": "python3 工具/make_split_zip.py --verify",
         "integrity": "逐卷 sha256 见 parts[].sha256；卷内每条与盘上 markdown/ 逐条 md5 比对由 --verify 执行"}
    json.dump(m, open(os.path.join(ROOT, MANIFEST), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"   清单：{MANIFEST}")
    return 0


def verify(max_mb=50.0):
    mp = os.path.join(ROOT, MANIFEST)
    if not os.path.exists(mp):
        raise SystemExit(f"没有 {MANIFEST}，先生成")
    m = json.load(open(mp, encoding="utf-8"))
    bad, seen = [], set()
    for r in m["parts"]:
        p = os.path.join(ROOT, r["file"])
        if not os.path.exists(p):
            bad.append(f"缺卷 {r['file']}")
            continue
        blob = open(p, "rb").read()
        if len(blob) != r["bytes"] or hashlib.sha256(blob).hexdigest() != r["sha256"]:
            bad.append(f"{r['file']} 字节数或 sha256 与清单不符")
        if len(blob) > max_mb * 1048576:
            bad.append(f"{r['file']} {len(blob)/1048576:.2f} MB 超 {max_mb} MB")
        z = zipfile.ZipFile(p)
        if z.testzip() is not None:
            bad.append(f"{r['file']} testzip 失败")
        for i in z.infolist():
            if i.is_dir():
                continue
            fp = os.path.join(SRC, i.filename)
            if not os.path.exists(fp):
                bad.append(f"{r['file']} 含盘上不存在的条目 {i.filename[:48]}")
                continue
            if hashlib.md5(z.open(i).read()).hexdigest() != hashlib.md5(open(fp, "rb").read()).hexdigest():
                bad.append(f"{r['file']}:{i.filename[:44]} 与盘上内容不一致")
            seen.add(i.filename)
    miss = set(all_files()) - seen
    if miss:
        bad.append(f"{len(miss)} 个文件没进任何卷，例：{sorted(miss)[:3]}")
    print(f"核验：{len(m['parts'])} 卷 / {m['totalMB']} MB / {len(seen)} 条目"
          f"{'，全部通过' if not bad else '，发现问题'}")
    for b in bad[:10]:
        print("   !", b[:120])
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-mb", type=float, default=45.0)
    ap.add_argument("--prefix", default="ApsaraStack_Markdown_1247")
    ap.add_argument("--plan", action="store_true", help="只打印分组与装箱预估，不写文件")
    ap.add_argument("--verify", action="store_true", help="只核验已生成的分卷与清单")
    ap.add_argument("--parts", type=int, default=0, help="强制分几卷（默认按上限算最少卷数再均衡）")
    a = ap.parse_args()
    os.chdir(ROOT)
    if a.verify:
        return verify(50.0)
    rc = build(a.prefix, a.max_mb, a.plan, a.parts or None)
    return rc or (0 if a.plan else verify(50.0))


if __name__ == "__main__":
    sys.exit(main())
