#!/usr/bin/env python3
"""把中文树的目录与文件名改成英文（ASCII）命名。

现状：markdown/01_专有云企业版_v3.18.6_20260730/<服务域中文>/<code 产品中文名>/NN_<中文手册名>_<手册code>.md
目标：markdown/01_ApsaraStack-Enterprise_v3.18.6_20260730/<domain-en>/<code>/NN_<手册code>.md

素材本来就够，不需要猜：站点接口给的 productCode / 手册 code 都是 ASCII，
中文只是被抄进了目录名与文件名（序号 sort 保留，防撞名）。

    python3 工具/rename_cn_dirs.py             # 试跑：出迁移表与冲突检查，不动文件
    python3 工具/rename_cn_dirs.py --apply     # 真搬 + 改索引 + 改全仓引用

云端对象键（下载台账.json 的 mdCloudKey / pdfCloud）不动 —— 那指向 OSS 上已发布的
中文路径包，改了就对不上。本地路径与云端路径的这层差异已在台账 localState.dirNaming 写明。
英文树的上一次同类改造见 工具/rename_en_dirs.py。
"""
import argparse
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cache  # noqa: E402

MD = os.path.join(ROOT, "markdown")

# 服务域：站点接口只给中文名，这里是一张固定的英译表（12 项，全是站点上的域）
DOMAIN_EN = {
    "专有云云平台": "platform",
    "云原生服务": "cloud-native",
    "交付服务": "delivery",
    "人工智能": "ai",
    "大数据服务": "big-data",
    "存储服务": "storage",
    "安全服务": "security",
    "应用服务": "application",
    "数据库服务": "database",
    "统一运营平台": "unified-operations",
    "网络服务": "network",
    "计算服务": "compute",
}
VER_EN = {"01_专有云企业版_": "01_ApsaraStack-Enterprise_"}
# markdown/ 下的辅助文件与目录也一并英文化
FLATTEN = {
    "_预览样书": "_preview-samples",
    "转换清单.json": "conversion_manifest.json",
    "转换清单.csv": "conversion_manifest.csv",
    "中文转换清单.json": "conversion_manifest_zh.json",
}
SAMPLE_EN = {  # 预览样书页（3 份 HTML）
    "DG-容器服务.html": "DG-container-service.html",
    "PI-WAF简介.html": "PI-waf-introduction.html",
    "UG-容器镜像.html": "UG-container-registry.html",
}
CJK = re.compile(r"[\u4e00-\u9fff]")


def prod_dir_code(name):
    """'rocketmq 云消息队列 RocketMQ 版' -> 'rocketmq'（接口给的 ASCII code）"""
    return name.split(" ")[0].strip() or name


def file_code(base):
    """'19_RocketMQ产品简介_apsarastack-product-introduction.md' -> ('19', 'apsarastack-product-introduction')"""
    m = re.match(r"^(\d+)_.+_([A-Za-z0-9][A-Za-z0-9._+-]*)\.md$", base)
    return (m.group(1), m.group(2)) if m else (None, None)


def target_rel(rel):
    """markdown 内的相对路径 -> 英文路径；映射不出来就返回 None（宁可不动，也不臆造名字）"""
    parts = rel.split("/")
    if rel.startswith("10_EN_") or parts[0] == "README.md":
        return None
    if parts[0] in FLATTEN and len(parts) == 1:
        return FLATTEN[parts[0]]
    if parts[0] == "_预览样书":
        return os.path.join("_preview-samples", SAMPLE_EN.get(parts[1], parts[1])) if len(parts) > 1 else "_preview-samples"
    if len(parts) < 4:
        return None
    ver, dom, prod, fn = parts[0], parts[1], parts[2], parts[-1]
    vpre, vrest = re.match(r"^(\d+_.+?_)(.*)$", ver).groups() if re.match(r"^(\d+_.+?_)(.*)$", ver) else (ver, "")
    nv = VER_EN.get(vpre, "" if CJK.search(vpre) else vpre) + vrest
    if nv is None or CJK.search(vpre) and not VER_EN.get(vpre):
        nv = ver
    nd = DOMAIN_EN.get(dom)
    if not nd:
        return None
    seq, code = file_code(fn)
    if not code:
        return None
    return "/".join([nv, nd, prod_dir_code(prod), f"{seq}_{code}.md"] + parts[4:])


def build_plan():
    plan, unmapped = [], []
    for root, _ds, fs in os.walk(MD):
        for f in sorted(fs):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, MD).replace(os.sep, "/")
            top = rel.split("/")[0]
            want = target_rel(rel) if (f.endswith(".md") or top in FLATTEN or top == "_预览样书") else None
            if want is None:
                if CJK.search(rel):
                    unmapped.append(rel)
                continue
            if want != rel:
                plan.append((rel, want))
    return plan, unmapped          # 目录不进气泡：文件按新路径落地后，空目录统一剪掉


REF_FILES = ["README.md", "下载台账.json", "下载台账.md", "中英对照手册映射.csv", "文档索引.csv",
             "文档明细.json", "全量文档清单.html", "钉钉索引_文档包.md", "00_产品清单_全量待选.md",
             "markdown/转换清单.json", "markdown/转换清单.csv", "markdown/中文转换清单.json",
             "markdown/README.md", "markdown/_预览样书/DG-容器服务.html",
             "markdown/_预览样书/PI-WAF简介.html", "markdown/_预览样书/UG-容器镜像.html"]


def rewrite_refs(plan, apply_it):
    """全仓文本替换旧路径。云端键（mdCloudKey/pdfCloud）指向 OSS 已发布路径，不能跟改。"""
    pairs = []
    for old, new in plan:
        pairs.append(("markdown/" + old, "markdown/" + new))
        pairs.append((old, new))
    pairs.sort(key=lambda x: -len(x[0]))
    hits = {}
    for f in REF_FILES:
        p = os.path.join(ROOT, f)
        if not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        orig = t
        if f == "下载台账.json":
            rows = json.loads(t)

            def walk(o):
                n = 0
                if isinstance(o, dict):
                    for k, v in list(o.items()):
                        if k in ("mdCloudKey", "pdfCloud"):
                            continue
                        if isinstance(v, str):
                            for a, b in pairs:
                                if a in v:
                                    o[k] = v = v.replace(a, b)
                                    n += 1
                        else:
                            n += walk(v)
                elif isinstance(o, list):
                    for v in o:
                        n += walk(v)
                return n
            if walk(rows):
                t = json.dumps(rows, ensure_ascii=False, indent=1)
        else:
            for a, b in pairs:
                if a and a != b and a in t:
                    t = t.replace(a, b)
        if t != orig:
            hits[f] = sum(1 for a, _ in pairs if a in orig)
            if apply_it:
                open(p, "w", encoding="utf-8").write(t)
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    os.chdir(ROOT)
    plan, unmapped = build_plan()
    md = [(o, n) for o, n in plan if o.endswith(".md")]
    print(f"待迁移 {len(md)} 本（+ 辅助文件 {len(plan)-len(md)} 项）；映射不出英文名的 {len(unmapped)} 项")
    for u in unmapped[:8]:
        print("   未映射：", u)
    seen, bad = set(), []
    for _o, n in md:
        if n in seen:
            bad.append(n)
        seen.add(n)
    if bad:
        print("目标撞名，拒绝执行：", bad[:5])
        return 1
    for o, n in md[:6]:
        print(f"   {o[:66]:68} → {n[-52:]}")
    if not a.apply:
        print("（试跑，未改动。加 --apply 才搬）")
        return 0

    for old, new in plan:
        so, sn = os.path.join(MD, old), os.path.join(MD, new)
        if not os.path.exists(so) or so == sn:
            continue
        os.makedirs(os.path.dirname(sn), exist_ok=True)
        shutil.move(so, sn)
    rows = cache.load(ROOT)
    mp = {o: n for o, n in plan}
    for _rid, r in rows.items():
        for k in ("markdown", "localPath"):
            v = (r.get(k) or "").replace(os.sep, "/")
            pre = "markdown/" if v.startswith("markdown/") else ""
            if v[len(pre):] in mp:
                r[k] = pre + mp[v[len(pre):]]
    cache.save(ROOT, list(rows.values()))
    for root, ds, _fs in sorted(os.walk(MD), key=lambda x: -len(x[0])):
        for d in ds:
            dd = os.path.join(root, d)
            if not os.listdir(dd):
                os.rmdir(dd)
    hits = rewrite_refs(plan, True)
    left = [os.path.relpath(os.path.join(r, f), MD) for r, _d, fs in os.walk(MD) for f in fs if CJK.search(
        os.path.relpath(os.path.join(r, f), MD))]
    left += [os.path.relpath(os.path.join(r, d), MD) for r, ds, _f in os.walk(MD) for d in ds if CJK.search(d)]
    print(f"搬完；改引用的文件：{', '.join(f'{k}({v})' for k, v in hits.items()) or '无'}")
    print(f"复查：markdown/ 下路径仍含中文的条目 {len(left)}")
    for x in left[:8]:
        print("   残留：", x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
