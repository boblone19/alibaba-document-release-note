#!/usr/bin/env python3
"""把交付树里残留的非 ASCII 路径字符折成 ASCII（NBSP、全角括号一类）。

阿里云官方英文书名里混着 U+00A0（不换行空格）和 U+FF08/U+FF09（全角括号）。这些不是"中文命名"，
是同形异码的排版字符：肉眼看着正常、按 ASCII 校验就失败，路径拼接与 URL 引用也容易出错。
所以：无损折叠（不改词义、不改词），改完刷索引、改全仓引用、再让人读清单重生成。

    python3 tools/ascii_paths.py            # 试跑：打印将改名的条目与冲突检查
    python3 tools/ascii_paths.py --apply    # 真改 + 刷索引 + 改引用

只碰 markdown/ 下的**路径**，不动正文（正文里的 NBSP/全角括号是厂商原文，另有
redact/normalize 规则管着）。汉字路径不在本tools范围，那是 rename_en_dirs.py /
rename_cn_dirs.py 的活。
"""
import argparse
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cache  # noqa: E402
import rename_cn_dirs as RC  # noqa: E402

MD = os.path.join(ROOT, "markdown")


def fold(s):
    """段级折叠：先折叠排版字符，再压掉多余空格；汉字原样留给 rename_* tools。"""
    out = cache.fold_ascii(s)
    out = re.sub(r" {2,}", " ", out.replace("\t", " ")).strip()
    return out or s


def plan():
    pairs = []
    for root, _dirs, files in os.walk(MD):
        for f in sorted(files):
            rel = os.path.relpath(os.path.join(root, f), MD).replace(os.sep, "/")
            new = "/".join(fold(seg) for seg in rel.split("/"))
            if new != rel:
                pairs.append((rel, new))
    return pairs


def conflicts(pairs):
    seen, bad = {}, []
    for _o, n in pairs:
        if n in seen:
            bad.append(n)
        seen[n] = 1
    # 目标如果已被别的现存文件占着，也是冲突
    for _o, n in pairs:
        if os.path.exists(os.path.join(MD, n)) and n not in [o for o, _ in pairs]:
            bad.append(n + " (已存在)")
    return sorted(set(bad))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    os.chdir(ROOT)
    pairs = plan()
    print(f"待折叠 {len(pairs)} 个文件路径")
    for o, n in pairs[:12]:
        print(f"   {o[:62]:64} → {n[-46:]}")
    bad = conflicts(pairs)
    if bad:
        print("目标冲突，拒绝执行：", bad[:5])
        return 1
    if not a.apply:
        print("（试跑，未改动。加 --apply 生效）")
        return 0

    moved = 0
    for old, new in pairs:
        so, sn = os.path.join(MD, old), os.path.join(MD, new)
        os.makedirs(os.path.dirname(sn), exist_ok=True)
        shutil.move(so, sn)
        moved += 1
    rows = cache.load(ROOT)
    mp = {o: n for o, n in pairs}
    upd = 0
    for _rid, r in rows.items():
        for k in ("markdown", "localPath"):
            v = (r.get(k) or "").replace(os.sep, "/")
            pre = "markdown/" if v.startswith("markdown/") else ""
            tail = v[len(pre):]
            if tail in mp:
                r[k] = pre + mp[tail]
                upd += 1
        if r.get("lang") == "en" and r.get("product"):
            r["product"] = fold(r["product"])
    cache.save(ROOT, list(rows.values()))
    hits = RC.rewrite_refs(pairs, True)           # 云端键 mdCloudKey/pdfCloud 内部会跳过
    # 空目录（折叠后旧名残留的）自下而上剪掉
    for root, dirs, _f in sorted(os.walk(MD), key=lambda x: -len(x[0])):
        for d in dirs:
            dd = os.path.join(root, d)
            if not os.listdir(dd):
                os.rmdir(dd)
    def offender(name):
        return any(ord(c) > 0x7F for c in name) and not re.search(r"[\u4e00-\u9fff]", name)
    left = [os.path.relpath(os.path.join(r, n), MD) for r, ds, fs in os.walk(MD) for n in ds + fs
            if offender(n)]
    print(f"搬了 {moved} 个文件；索引改了 {upd} 处；引用命中 {hits or '无'}")
    print(f"复查：仍含非 ASCII（非汉字）的路径段 {len(left)}", left[:4])
    print("复查：非 ASCII 且非汉字的路径段应为 0；汉字路径归 rename_cn_dirs / rename_en_dirs 管")
    return 0


if __name__ == "__main__":
    sys.exit(main())
