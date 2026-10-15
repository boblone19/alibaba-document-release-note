"""V3.16.2 → V3.18.6 配对差异提取（release note 的证据层）。

  python3 工具/rn3162_pairs.py            # 产出 .scratch/rn3162_pairs.json 并打印统计

与 rn2607_pairs.py 是同一条证据管线（句子级增删、大纲增减/改名、配额表逐行差异、
官方 release notes 段），只换配对两侧：old=V3.16.2（53 册英文基线），new=V3.18.6（287 册）。
V3.16.2 英文集只有 User / Developer / Instance-Families Guide，没有 Product Introduction
与运维卷，因此 V3.18.6 的大多数手册没有可比对象——只对配对成功的部分给 diff，
其余如实列出并标注最接近的历史英文名，不推断、不写"未变化"。
配对仅用严格同名同类型（norm(product)+docType），不做近似匹配。
"""
import collections
import difflib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import release_note as RN  # noqa: E402
import rn2607_pairs as P   # noqa: E402  （句子管线/配对键/大纲差分在此复用）

IDX = os.path.join(ROOT, "文档缓存索引.json")
OUT = os.path.join(ROOT, os.pardir, os.pardir, ".scratch", "rn3162_pairs.json")
OLD_VER, NEW_VER = "V3.16.2", "V3.18.6"
DEP = re.compile(r"(?i)\bdeprecated\b|\breplaced by\b|\bno longer supported\b|"
                 r"\bno longer available\b|\bhas been (removed|retired|discontinued)\b|"
                 r"\bare (retired|discontinued)\b")
DUPNUM = re.compile(r"\s+\(\d+\)$")                        # 上游重名文件加的 " (1)" 尾巴
DOUBLED = re.compile(r"^(.{4,}?) \1(?:\b|$)(.+)$", re.S)   # 产品名整段重复："X X (sub)"


def clean_row(r):
    """门户 label 的两处上游瑕疵：文件重名尾巴 "(1)"、产品名整段重复。只影响名称解析。
    先剥版本前缀（与 prod_key 同一条 PRE 规则），重复段才暴露在串首。"""
    r = dict(r)
    lb = P.PRE.sub("", r.get("label") or "")
    lb = DUPNUM.sub("", lb)
    m = DOUBLED.match(lb)
    if m:
        lb = f"{m.group(1)}{m.group(2)}"
    r["label"] = lb
    return r


def main():
    rows = json.load(open(IDX, encoding="utf-8"))
    old, new = {}, {}
    for r in rows:
        if r["lang"] != "en" or not r.get("markdown"):
            continue
        if r.get("version") == OLD_VER:
            old[P.prod_key(clean_row(r))[:2]] = clean_row(r)
        elif r.get("version") == NEW_VER:
            new[P.prod_key(clean_row(r))[:2]] = clean_row(r)
    pairs = [(k, old[k], new[k]) for k in sorted(set(old) & set(new))]
    print(f"可配对 {len(pairs)} | V3.18.6 无 V3.16.2 基线 {len(new) - len(pairs)} | "
          f"V3.16.2 未随 V3.18.6 复刊 {len(old) - len(pairs)}")

    freq = collections.Counter()
    cache = {}
    for k, ro, rn_ in pairs:
        for side, r in (("o", ro), ("n", rn_)):
            p = RN.parse(os.path.join(ROOT, r["markdown"]))
            s = P.sentences(p)
            cache[(k, side)] = (p, s)
            for h in s:
                freq[h] += 1
    thresh = max(6, int(0.08 * len(pairs)))
    print(f"套话阈值：出现在 ≥{thresh} 本手册的句子按模板处理（配对数 {len(pairs)}）")

    out = []
    for (kp, kt), ro, rn_ in pairs:
        po, so = cache[((kp, kt), "o")]
        pn, sn = cache[((kp, kt), "n")]
        raw_add = [v for h, v in sn.items() if h not in so and freq[h] < thresh]
        raw_del = [v for h, v in so.items() if h not in sn and freq[h] < thresh]
        added_s, gone_s, reworded = P.cancel_reword(raw_add, raw_del)
        rank = lambda xs: sorted(xs, key=lambda x: (0 if P.INFO.search(x[1]) else 1,
                                                    -len(P.NUMUNIT.findall(x[1]))))
        heads_add, heads_gone, renames = P.outline_delta(po, pn)
        lim = RN.limit_diff(po["tables"], pn["tables"])
        rel = RN.release_sections(pn)
        feat = [x for x in added_s if re.search(r"(?i)\b(support|add|new|introduc|allow|enable|now)\b", x[1])]
        rem = [x for x in added_s + gone_s if DEP.search(x[1])]
        quant = [x for x in added_s if re.search(r"\d", x[1])]
        out.append({
            "product": P.prod_key(rn_)[2] or P.prod_key(ro)[2] or kp, "key": [kp, kt], "docType": kt,
            "old": {"pages": ro.get("pages"), "ver": ro.get("versionStamp"), "file": ro["markdown"],
                    "heads": len(po["heads"]), "chars": po["chars"]},
            "new": {"pages": rn_.get("pages"), "ver": rn_.get("versionStamp"), "file": rn_["markdown"],
                    "heads": len(pn["heads"]), "chars": pn["chars"]},
            "newSections": heads_add[:20], "newSectionsTotal": len(heads_add),
            "droppedSections": heads_gone[:12], "droppedSectionsTotal": len(heads_gone),
            "renamedSections": renames[:8],
            "limits": lim,
            "releaseNotesOfficial": rel[:3],
            "sentAdd": [[t, s] for t, s in rank(added_s)[:40]], "sentAddTotal": len(added_s),
            "sentDel": [[t, s] for t, s in rank(gone_s)[:25]], "sentDelTotal": len(gone_s),
            "rawAddTotal": len(raw_add), "rawDelTotal": len(raw_del), "reworded": reworded,
            "bucketFeat": len(feat), "bucketQuant": len(quant), "bucketRem": len(rem),
        })

    # "无基线"册子的近似归类：只对照 V3.16.2（本次的上一代英文集合）的产品名。
    old_names = {}
    for r in rows:
        if r["lang"] == "en" and r.get("version") == OLD_VER:
            old_names.setdefault(P.prod_key(r)[2], OLD_VER)

    def nearest(pname):
        best, bs, bver = "", 0.0, ""
        for o, ver in old_names.items():
            ratio = difflib.SequenceMatcher(None, RN.norm(pname), RN.norm(o)).ratio()
            if ratio > bs:
                best, bs, bver = o, ratio, ver
        return best, round(bs, 3), bver

    paired_keys = {(e["key"][0], e["key"][1]) for e in out}

    def ent(r):
        pn = P.prod_key(r)[2]
        nb, score, nver = nearest(pn)
        dt = r.get("docType")
        if (dt or "").isdigit():                    # 上游个别行的 docType 是日期；产品名里已含 Guide 字样
            dt = "—"
        return {"id": r["id"], "product": pn, "docType": dt,
                "pages": r.get("pages"), "ver": r.get("versionStamp"), "file": r["markdown"],
                "folder": r.get("localPath", "").split("/")[1], "nearestOld": nb,
                "nearScore": score, "nearestOldVersion": nver}

    json.dump({"pairs": out,
               "onlyNew": [ent(r) for k, r in new.items() if k not in paired_keys],
               "onlyOld": [ent(r) for k, r in old.items() if k not in paired_keys],
               "stats": {"pairs": len(out), "onlyNew": len(new) - len(out),
                         "notRefreshed": len(old) - len(out),
                         "oldTotal": len(old), "newTotal": len(new)}},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    withd = sum(1 for e in out if e["sentAddTotal"] or e["sentDelTotal"] or e["newSectionsTotal"] or e["limits"])
    print(f"有实质差异的配对 {withd}/{len(out)}；句子级新增合计 {sum(e['sentAddTotal'] for e in out):,} 条，"
          f"删除合计 {sum(e['sentDelTotal'] for e in out):,} 条，配额差异 {sum(len(e['limits']) for e in out)} 处，"
          f"自带 release notes 段的配对 {sum(1 for e in out if e['releaseNotesOfficial'])} 个")
    print(f"→ {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
