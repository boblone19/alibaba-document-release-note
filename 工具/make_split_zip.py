#!/usr/bin/env python3
"""打包 markdown/：中文树一个整包 + 其余按体积上限分卷，所有产物文件名一律英文（ASCII）。

规则
  1. 中文树（顶层目录 `01_…` / `02_…`）单独打成 **一个** zip，不参与装箱；
     超过 --max-mb 就直接报错，而不是偷偷拆成两卷。
  2. 其余顶层分组（英文各 stack 版本线、markdown/ 根级清单、_preview-samples）
     按原逻辑装箱：卷数 = ceil(总量/上限)，再用 LPT 均衡，一个版本线绝不跨卷，
     所以单独下一卷解压就是那一版本完整可读的 Markdown。
  3. 每卷都是独立 zip（不是 .z01 切片），可单独下载解压，无需按顺序拼接。
  4. 产出 `ApsaraStack_Markdown_split_manifest.json`：每卷文件名/字节/sha256/条目数/
     包含哪些顶层目录/是中文整包还是分卷，以及下载顺序。
  5. 必须排在 redact_vendor_docs.py 与 build_indexes.py 之后跑 —— 先打包再重建清单，
     卷里就是旧文件（--verify 正是用来抓这种漂移的）。

    python3 工具/make_split_zip.py --plan           # 只看分组与装箱预估，不写文件
    python3 工具/make_split_zip.py                  # 生成 + 自动核验
    python3 工具/make_split_zip.py --max-mb 40      # 上限降到 40 MB（卷数自动增加）
    python3 工具/make_split_zip.py --verify         # 只核验已有产物
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
MANIFEST = "ApsaraStack_Markdown_split_manifest.json"
ZH_TOP = ("01_", "02_")          # 中文树：专有云企业版 + AIStack
OLD_ARTIFACTS = (MANIFEST, "分卷清单.json")


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
    """实测这组进 zip 后占多少字节（与整卷同参数，不靠比例估）。"""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for n in names:
            z.write(os.path.join(SRC, n), n)
    return len(buf.getvalue())


def bin_pack(groups, limit, size, parts=None):
    """卷数取 ceil(总量/上限) 的最少值，再 LPT：最大的组先放，每次进当前最小的卷。"""
    order = sorted(groups, key=lambda k: -size[k])
    if not order:
        raise SystemExit("待打包内容为空")
    if size[order[0]] > limit:
        raise SystemExit(f"分组 {order[0]!r} 压缩后 {size[order[0]]/1048576:.2f} MB 已超上限 "
                         f"{limit/1048576:.2f} MB；按文件二次切会腰斩版本线，请人工决定切法")
    n = parts or max(1, -(-sum(size.values()) // limit))
    bins = [[0, []] for _ in range(n)]
    for k in order:
        b = min(bins, key=lambda x: x[0])          # 只求一次；先改体积再求会挑错卷
        b[0] += size[k]
        b[1].append(k)
    if max(b[0] for b in bins) > limit:
        raise SystemExit("均衡后仍有卷超上限，请调小 --max-mb 或调大 --parts")
    return [sorted(b[1]) for b in bins if b[1]]


def books(names):
    return sum(1 for f in names if f.endswith(".md") and os.path.basename(f) != "README.md")


def clean_old(prefix):
    n = 0
    for f in os.listdir(ROOT):
        if (f in OLD_ARTIFACTS or re.match(r"^ApsaraStack_Markdown.*\.zip$", f)
                or re.match(r"^markdown_全量.*\.zip$", f)):   # 清掉历史命名（含带册数前缀的旧写法）
            os.remove(os.path.join(ROOT, f))
            n += 1
    return n


def write_zip(name, tops, grp, max_bytes, rec, kind):
    path = os.path.join(ROOT, name)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        cnt = 0
        for t in tops:
            for f in grp[t]:
                z.write(os.path.join(SRC, f), f)
                cnt += 1
    blob = open(path, "rb").read()
    if len(blob) > max_bytes:
        os.remove(path)
        raise SystemExit(f"{name} 实际 {len(blob)/1048576:.2f} MB 超上限，请降 --max-mb")
    rec.append({"file": name, "kind": kind, "bytes": len(blob),
                "MB": round(len(blob) / 1048576, 2), "entries": cnt,
                "books": books([f for t in tops for f in grp[t]]),
                "sha256": hashlib.sha256(blob).hexdigest(), "contains": tops})
    print(f"   写出 {name}: {len(blob)/1048576:.2f} MB / {cnt} 条目 / {tops}")


def build(prefix, max_mb, parts, plan_only):
    paths = all_files()
    grp = groups_of(paths)
    size = {k: compressed_size(v) for k, v in grp.items()}
    zh = {k: v for k, v in grp.items() if k.startswith(ZH_TOP)}
    rest = {k: v for k, v in grp.items() if not k.startswith(ZH_TOP)}
    limit = int(max_mb * 1048576)
    if not zh:
        raise SystemExit(f"没认出中文树（顶层目录应形如 {ZH_TOP}…），拒绝按新规则打包")
    if sum(size[k] for k in zh) > limit:
        raise SystemExit(f"中文树整包压缩后 {sum(size[k] for k in zh)/1048576:.2f} MB 超上限 "
                         f"{max_mb} MB；新规则要求中文只出一个 zip，请先压缩率或改规则")
    plan = bin_pack(rest, limit, {k: size[k] for k in rest}, parts)
    zbooks = books([f for k in zh for f in grp[k]])
    print(f"markdown/：{len(paths)} 个条目，{len(grp)} 组，压缩后合计 {sum(size.values())/1048576:.2f} MB")
    for k in sorted(grp, key=lambda x: -size[x]):
        tag = "中文树→整包" if k in zh else "参与分卷"
        print(f"   {size[k]/1048576:6.2f} MB / {len(grp[k]):>4} 项  {k:<44} [{tag}]")
    print(f"\n中文：{zbooks} 本 → 1 个整包；其余 → {len(plan)} 卷（每卷 ≤{max_mb} MB）")
    for i, tops in enumerate(plan, 1):
        print(f"   卷{i}: {sum(size[t] for t in tops)/1048576:5.2f} MB  ← {', '.join(tops)}")
    if plan_only:
        return 0

    rm = clean_old(prefix)
    rec = []
    write_zip(f"{prefix}_zh_{zbooks}books.zip", sorted(zh), grp, limit, rec, "chinese_single")
    n = len(plan)
    for i, tops in enumerate(plan, 1):
        write_zip(f"{prefix}_part{i}of{n}.zip", tops, rest, limit, rec, "other_volume")
    m = {"policy": "中文树（01_/02_ 顶层目录）单独一个整包；其余（英文各 stack 版本线、markdown/ 根级"
                   "清单与 _preview-samples）按 --max-mb 装箱分卷。版本线绝不跨卷；每卷独立 zip，"
                   "无需拼接；所有产物文件名一律英文 ASCII。构建顺序必须是 脱敏 → build_indexes → 本工具",
         "maxFileMB": max_mb, "source": "markdown/", "removedOld": rm,
         "chinesePackage": next(r["file"] for r in rec if r["kind"] == "chinese_single"),
         "chineseBooks": zbooks,
         "volumes": [r["file"] for r in rec if r["kind"] == "other_volume"],
         "parts": rec, "totalMB": round(sum(r["bytes"] for r in rec) / 1048576, 2),
         "entries": sum(r["entries"] for r in rec),
         "books": sum(r["books"] for r in rec),
         "downloadOrder": [r["file"] for r in rec],
         "verify": "python3 工具/make_split_zip.py --verify"}
    json.dump(m, open(os.path.join(ROOT, MANIFEST), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"   清单：{MANIFEST}（共 {m['totalMB']} MB / {m['books']} 册）")
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
            bad.append(f"缺文件 {r['file']}")
            continue
        if not r["file"].isascii():
            bad.append(f"{r['file']} 文件名含非 ASCII")
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
            if not i.filename.isascii():
                bad.append(f"{r['file']} 卷内路径含非 ASCII：{i.filename[:40]}")
            fp = os.path.join(SRC, i.filename)
            if not os.path.exists(fp):
                bad.append(f"{r['file']} 含盘上没有的条目 {i.filename[:48]}")
                continue
            if hashlib.md5(z.open(i).read()).hexdigest() != hashlib.md5(open(fp, "rb").read()).hexdigest():
                bad.append(f"{r['file']}:{i.filename[:40]} 与盘上内容不一致")
            seen.add(i.filename)
    zh = [r for r in m["parts"] if r["kind"] == "chinese_single"]
    if len(zh) != 1:
        bad.append("中文整包应恰好 1 个")
    else:
        want = {f for f in all_files() if f.split("/")[0].startswith(ZH_TOP)}
        got = {i.filename for i in zipfile.ZipFile(os.path.join(ROOT, zh[0]["file"])).infolist()
               if not i.is_dir()}
        if want != got:
            bad.append(f"中文整包内容不平：应 {len(want)} 条目，实 {len(got)}，差 {sorted(want ^ got)[:3]}")
    miss = set(all_files()) - seen
    if miss:
        bad.append(f"{len(miss)} 个文件没进任何包，例：{sorted(miss)[:3]}")
    print(f"核验：{len(m['parts'])} 个包 / {m['totalMB']} MB / {len(seen)} 条目（中文 {m['chineseBooks']} 册成单包）"
          f"{'，全部通过' if not bad else '，发现问题'}")
    for b in bad[:10]:
        print("   !", b[:130])
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-mb", type=float, default=45.0, help="单包压缩后上限 MB（GitHub 软限 50）")
    ap.add_argument("--prefix", default="ApsaraStack_Markdown", help="产物文件名前缀（必须 ASCII）")
    ap.add_argument("--parts", type=int, default=0, help="强制其余部分分几卷；默认按上限算最少卷数")
    ap.add_argument("--plan", action="store_true", help="只打印分组与装箱预估，不写文件")
    ap.add_argument("--verify", action="store_true", help="只核验已生成的包与清单")
    a = ap.parse_args()
    os.chdir(ROOT)
    if not a.prefix.isascii():
        raise SystemExit("--prefix 必须是 ASCII")
    if a.verify:
        return verify(50.0)
    rc = build(a.prefix, a.max_mb, a.parts or None, a.plan)
    return rc or (0 if a.plan else verify(50.0))


if __name__ == "__main__":
    sys.exit(main())
