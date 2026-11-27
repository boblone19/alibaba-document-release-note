"""把 _2607 / V3.16.2 的产品目录改成 v3.18.6 的产品名口径（扁平、去重复拼接）。

    python tools/rename_en_dirs_by_ref.py            # 试跑
    python tools/rename_en_dirs_by_ref.py --apply     # 真搬 + 改索引/清单/引用
"""
import argparse
import collections
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cache  # noqa: E402

MD = os.path.join(ROOT, "markdown")
REF = "10_EN_ApsaraStack_v3.18.6"
TREES = ["10_EN_ApsaraStack_V3.18.6_2607", "10_EN_ApsaraStack_V3.16.2"]

CONTAINERS = ["Alibaba Cloud Security-", "Alibaba Cloud ", "Cloud Defined Storage ",
              "Database Audit ", "Bastionhost ", "Server Load Balancer ",
              "Apsara Uni-manager ", "Enterprise Distributed Application Service (EDAS) ",
              "Container Service for Kubernetes ", "Apsara Stack Operation ",
              "Application Operation Platform ", "AnalyticDB for MySQL "]

# 参考词表给不出正确答案的个例
OVERRIDE = {
    "Alibaba Cloud Security-Web Application Firewall (WAF) Web Application Firewall-Instance":
        "Web Application Firewall (WAF) -Instance",
    "Machine Learning Platform for AI Bare Metal Computing Platform":
        "Machine Learning Platform for AI Bare Metal Computing Platform",
}


def canon_vocab():
    ref = os.path.join(MD, REF)
    return {d.lower(): d for d in sorted(os.listdir(ref)) if os.path.isdir(os.path.join(ref, d))}


def dedupe(s):
    t = s.split(" ")
    for k in range(len(t) // 2, 0, -1):
        if t[:k] == t[k:2 * k]:
            return " ".join(t[k:])
    return s


def clean(prod, canon):
    s = prod.strip()
    if s in OVERRIDE:
        return OVERRIDE[s]
    if s.lower() in canon:
        return canon[s.lower()]
    for p in CONTAINERS:
        if s.startswith(p):
            rest = s[len(p):].strip()
            if rest.lower() in canon:
                return canon[rest.lower()]
    d = dedupe(s)
    if d.lower() in canon:
        return canon[d.lower()]
    if d != s:
        return d
    for p in ("Alibaba Cloud Security-", "Alibaba Cloud "):
        if s.startswith(p):
            return s[len(p):].strip()
    return s


def md_dirs(tree):
    out = set()
    base = os.path.join(MD, tree)
    for r, _ds, fs in os.walk(base):
        if any(f.endswith(".md") for f in fs):
            out.add(os.path.relpath(r, base).replace(os.sep, "/"))
    return sorted(out)


def build_plan(canon):
    """{tree: {old_rel_dir: new_top_dir}} + [(old_abs, new_abs)]"""
    mapping, moves = {}, []
    for tree in TREES:
        base = os.path.join(MD, tree)
        m = {}
        for d in md_dirs(tree):
            leaf = d.split("/")[-1]
            m[d] = clean(leaf, canon)
        # 目录名本身就是文件名的怪目录：取书名里的产品名
        for d in list(m):
            if " Guide " in d.split("/")[-1] and any(ch.isdigit() for ch in d.split("/")[-1][-6:]):
                m[d] = "Object Storage Service"
        mapping[tree] = m
        for d, newdir in m.items():
            src = os.path.join(base, d.replace("/", os.sep))
            for f in sorted(os.listdir(src)):
                if not f.endswith(".md"):
                    continue
                stem = f[:-3]
                oldleaf = d.split("/")[-1]
                stem2 = (newdir + stem[len(oldleaf):]) if stem.startswith(oldleaf) else stem
                dst = os.path.join(base, newdir, stem2 + ".md")
                if os.path.normcase(dst) != os.path.normcase(os.path.join(src, f)):
                    moves.append((os.path.join(src, f), dst, tree, d, newdir))
    return mapping, moves


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    canon = canon_vocab()
    mapping, moves = build_plan(canon)

    for tree in TREES:
        m = mapping[tree]
        chg = {k: v for k, v in m.items() if k != v}
        tg = collections.defaultdict(list)
        for k, v in chg.items():
            tg[v.lower()].append(k)
        merge = {k: v for k, v in tg.items() if len(v) > 1}
        print(f"\n{tree}: {len(m)} 个目录 -> {len(set(m.values()))} 个产品目录；改名 {len(chg)} 个")
        for k, v in sorted(merge.items()):
            print(f"   合并到 [{v[0]}]：{len(k and tg[k])} 个来源 -> {chg and [x for x in tg[k]]}")

    # 落盘后是否撞名（同一目标目录内同名文件）
    dsts = collections.Counter(os.path.normcase(d) for _s, d, *_ in moves)
    dup = [d for d, n in dsts.items() if n > 1]
    print(f"\n文件级目标撞名: {len(dup)}")
    for d in dup[:5]:
        print("   ", d)

    print(f"待移动文件: {len(moves)}")
    for s, d, *_ in moves[:6]:
        print("  ", os.path.relpath(s, MD), "->", os.path.relpath(d, MD))
    if not a.apply:
        print("\n（试跑，未改动。加 --apply 才搬）")
        return 0

    # 1) 建目录 + 搬文件
    for s, d, *_ in moves:
        os.makedirs(os.path.dirname(d), exist_ok=True)
        if os.path.exists(d) and os.path.normcase(d) != os.path.normcase(s):
            print("   目标已存在，跳过:", os.path.relpath(d, MD))
            continue
        os.replace(s, d)
    print(f"搬移完成 {len(moves)} 个文件")

    # 2) 索引：markdown / localPath 换目录前缀
    rows = json.load(open(os.path.join(ROOT, cache.JSON_NAME), encoding="utf-8"))
    n = 0
    for tree, m in mapping.items():
        for old, new in m.items():
            if old == new:
                continue
            o = f"markdown/{tree}/{old}/"
            nw = f"markdown/{tree}/{new}/"
            for r in rows:
                for k in ("markdown", "localPath"):
                    v = (r.get(k) or "").replace("\\", "/")
                    if v.startswith(o):
                        r[k] = nw + v[len(o):]
                        n += 1
    cache.save(ROOT, rows)
    print(f"索引改路径 {n} 处")

    # 3) 清单（conversion_manifest）同步
    for name in ("markdown/conversion_manifest.json",):
        p = os.path.join(ROOT, name)
        if not os.path.exists(p):
            continue
        data = json.load(open(p, encoding="utf-8"))
        c = 0
        for r in data:
            for k in ("md", "mdLink"):
                v = (r.get(k) or "").replace("\\", "/")
                for tree, m in mapping.items():
                    for old, new in m.items():
                        if old == new:
                            continue
                        o = f"markdown/{tree}/{old}/" if k == "md" else f"{tree}/{old}/"
                        if v.startswith(o):
                            r[k] = (f"markdown/{tree}/{new}/" if k == "md" else f"{tree}/{new}/") + v[len(o):]
                            c += 1
        json.dump(data, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{name} 改路径 {c} 处")
    return 0


if __name__ == "__main__":
    sys.exit(main())