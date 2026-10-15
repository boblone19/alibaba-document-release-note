"""V3.18.6 → V3.18.6_2607 配对差异提取（release note 的证据层）。

  python3 工具/rn2607_pairs.py            # 产出 .scratch/rn2607_pairs.json 并打印统计

只提取**可核对的事实**，不做任何推断：
  * 页量/字符量、文档版本、标题大纲的增减与改名（difflib 相似度 ≥0.8 视为改名）
  * 配额/限制表逐行差异（复用 release_note.limit_diff）
  * 新册里产品团队自己写的 release notes / what's new 段（逐字）
  * **正文句子级增删**：同一配对内 new-only / old-only 句子，再按跨手册语频
    过滤模板套话（出现于 ≥8% 手册的句子丢掉了，法律通告、"This topic describes"
    之类不充当"变化"）
配对仅用严格同名同类型（norm(product)+docType），不做近似匹配——
上一版按 0.90 相似度会把 RDS 配到 Redis（假变化），宁可留空。
"""
import collections
import difflib
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import release_note as RN  # noqa: E402

IDX = os.path.join(ROOT, "文档缓存索引.json")
OUT = os.path.join(ROOT, os.pardir, os.pardir, ".scratch", "rn2607_pairs.json")
PRE = re.compile(r"(?i)^\s*Alibaba Cloud Apsara Stack( Enterprise)?( Apsara Stack)?\s*v?[\d.]+(?:[ _-]\d{3,6})?\s*")
CODE = re.compile(r"^\s{0,3}(#{1,6}\s|\||```|!\[|<)")
MINLEN, MAXLEN = 26, 400
STOP = set("""a an the and or but if then than that this these those for from to of in on at by with without
you your yours we our they them their it its is are was were be been being have has had do does did will would
shall should can could may might must not no nor all any both each few more most other some such only own same
so as too very just also now here there when where which who whom what why how about above after before between
during into out over under again further once because while should must don t s re ve ll d o""".split())
PLURAL = re.compile(r"([^aeiou])s$")
INFO = re.compile(r"(?i)\b(support|supporths|add|adds|new|news|introduc|allow|enabl|deprecat|no longer|not supported|"
                  r"remov|retir|chang|updat|migrat|limit|quota|maxim|minimum|default|version|instance type|API)\b")
# 残渣行：日志样例、Grok/正则片段、CLI 输出表、纯符号行——不是"文档变化"
NOISE = (re.compile(r"\d{2}:\d{2}:\d{2}[,.]\d{3}"),                 # 时间戳日志
         re.compile(r"\b[A-Z]{3,6}\s+\w+(?::\d+)?\s+[-:]"),        # INFO/DEBUG 类日志行
         re.compile(r"\(\?[:<=!]|\[[:^=]|[\\||].{3,}[\\|]]"),     # 正则片段
         re.compile(r"^[\W_]*$"),
         re.compile(r"\b(?:ERROR|WARN|TRACE|DEBUG)\b\s+\w+"))


PUNCT_OK = set(" ,.-:") | {chr(39), chr(34), "(", ")", "/"}


BOILER = re.compile(r"(?i)^\s*(this topic (describes|explains|shows|introduces|covers)|these topics|"
                    r"the following (table|section|list|example|figure|columns?)|for more info|"
                    r"as shown in|in the navigation pane|on the .{0,40} ?page[,，]|"
                    r"you can click|click (ok|confirm|create)\b|this section|the table below|"
                    r"steps? to? (follow|be)|example\s*[:：])")


def informative(s):
    """只保留承载信息的句子：版本/数字/支持-弃用-限制语义/参数名等，滤掉界面导引与自述式套话。"""
    if BOILER.match(s):
        return False
    return bool(INFO.search(s)) or bool(re.search(r"\b\d+\.\d+(\.\d+)?\b", s))


OKCHARS = re.compile(r"^[A-Z][A-Za-z0-9 ,;:'\"()\.\-/&%*+=_\[\]<>\?]*$")


def wellformed(s):
    """PDF 转换在 bullet/表格边界会留下断词残渣（如 "sage Queue ... M Q?"）。
    只保留结构完整的句子，否则 note 里会出现看不出所以然的片段。"""
    if not OKCHARS.match(s):
        return False
    w = s.split()
    if len(w) < 8:
        return False
    if sum(1 for x in w if len(x) <= 2) / len(w) > 0.18:      # 单元音词/断词碎片过多
        return False
    if not s.endswith((".", "?", ":", "!", ")")):
        return False
    return len(re.findall(r"[a-z]{4,}", s)) >= 6


def is_noise(s):
    """True for log samples, regex fragments, CLI dumps and symbol soup — those are
    converter artifacts or code snippets, not documentation changes."""
    if len(re.sub(r"[^A-Za-z0-9]", "", s)) < 12:
        return True
    odd = sum(1 for c in s if not c.isalnum() and c not in PUNCT_OK)
    if odd / max(1, len(s)) > 0.18:
        return True
    return any(r.search(s) for r in NOISE)


NUMUNIT = re.compile(r"\b\d[\d,.]*\s*(%|GiB|MiB|TiB|KB|MB|GB|TB|vCPU|characters?|bytes?|seconds?|minutes?|hours?|days?|QPS|TPS|RPS|Mbps|Gbps)?\b")


def toks(s):
    w = [x for x in re.findall(r"[a-z0-9]+", s.lower()) if len(x) > 3 or x.isdigit()]
    return {PLURAL.sub(r"\1", x) for x in w if x not in STOP}


def cancel_reword(added, removed):
    """把"同一句话被改写/拆分/换排版"的行从增删两侧各摘掉，避免把排版当成产品变化。
    判据：显著词集合 Jaccard ≥ 0.82（用倒排索引限制候选，避免 O(n²)）。"""
    inv = collections.defaultdict(list)
    rtok = [toks(s) for _, s in removed]
    for i, ts in enumerate(rtok):
        for t in ts:
            inv[t].append(i)
    used, net_add, net_del, reworded = set(), [], [], 0
    rset = [None] * len(removed)
    for i, ts in enumerate(rtok):
        rset[i] = ts
    for item in added:
        ts = toks(item[1])
        if not ts:
            net_add.append(item)
            continue
        posts = sorted((inv.get(t, []) for t in ts), key=len)[:3]
        cand = {i for p in posts for i in p}
        best, bi = 0.0, None
        for i in cand:
            if i in used or not rset[i]:
                continue
            inter = len(ts & rset[i])
            j = inter / max(1, len(ts | rset[i]))
            if j > best:
                best, bi = j, i
        if best >= 0.82 and bi is not None:
            used.add(bi)
            reworded += 1
        else:
            net_add.append(item)
    for i, item in enumerate(removed):
        if i not in used:
            net_del.append(item)
    return net_add, net_del, reworded


def prod_key(r):
    fn = PRE.sub("", r["label"])
    dt = r.get("docType") or "Other"
    prod = re.sub(r"\s*" + re.escape(dt) + r"\s*\d{8}$", "", fn).strip()
    prod = re.sub(r"\s*\d{8}$", "", prod).strip()
    return RN.norm(prod), dt, prod


def sentences(p):
    """手册正文里的"句子"（按行，去掉标题/表格/代码块/图片行）。返回 {hash: 原文}。"""
    out = {}
    for title, buf in p["secs"]:
        prose, fenced = [], False
        for x in buf:                                   # 跳过代码块内部：SQL/日志/正则不是"文档变化"
            t = x.strip()
            if t.startswith("```"):
                fenced = not fenced
                continue
            if fenced or not t or CODE.match(t) or t.startswith("---"):
                continue
            prose.append(t)
        para = " ".join(prose)
        for s in re.split(r"(?<=[.?!:])\s{1,3}|\n", para):      # 段落内按句切，不受 PDF 换行影响
            s = s.strip()
            if not s or s.startswith("---"):
                continue
            s = re.sub(r"^[-*>]\s*", "", s)
            s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
            s = re.sub(r"\[(.+?)\]\([^)]*\)", r"\1", s)
            s = re.sub(r"`([^`]*)`", r"\1", s)
            s = re.sub(r"\s+", " ", s).strip()
            if not (MINLEN <= len(s) <= MAXLEN) or len(re.findall(r"[A-Za-z]{3,}", s)) < 4:
                continue
            if is_noise(s) or not wellformed(s):
                continue
            if not informative(s):
                continue                  # 只有信息型句子才算"变化"
            h = hashlib.sha1(RN.norm(s).encode()).hexdigest()
            out.setdefault(h, (title or "", s))
    return out


NUM_PREFIX = re.compile(r"^(?:\d+(?:[.:]\d+)*[.)]?\s+|[一二三四五六七八九十]+、\s*)")


RUNHEAD = re.compile(r"(?i)^\s*(alibaba cloud apsarastack|alibaba cloud apsara stack|apsara stack"
                     r"|.*\bv\d\.\d+\.\d+.*|.*版本文档.*|manual names?\b)")


def hnorm(t):
    """标题比较用归一：去章节编号、去尾部随机数字、丢停用词、复数还原。"""
    t = re.sub(r"_\d{6,}", "", t or "")
    t = NUM_PREFIX.sub("", t)
    t = re.sub(r"\[\d+\]", "", t)
    ws = [w for w in re.findall(r"[a-z0-9]+", t.lower()) if w not in STOP and not w.isdigit()]
    return " ".join(PLURAL.sub(r"\1", w) for w in ws)


def outline_delta(o, n):
    """标题大纲：新增 / 移除 / 改名（同名视为未变，按 norm 比较）。"""
    oh, nh = {}, {}
    for lv, t in o["heads"]:
        if lv == 1 or RUNHEAD.match(t or "") or not hnorm(t):
            continue                                  # 册名/页眉不算章节
        oh.setdefault(hnorm(t), t)
    for lv, t in n["heads"]:
        if lv == 1 or RUNHEAD.match(t or "") or not hnorm(t):
            continue
        nh.setdefault(hnorm(t), t)
    added = [v for k, v in nh.items() if k not in oh]
    gone = [v for k, v in oh.items() if k not in nh]
    renames = []
    for a in list(added):
        cand = difflib.get_close_matches(hnorm(a), [hnorm(g) for g in gone], n=1, cutoff=0.85)
        if cand:
            g = [x for x in gone if hnorm(x) == cand[0]][0]
            renames.append((g, a))
            gone.remove(g)
            added.remove(a)
    return added, gone, renames


def main():
    rows = json.load(open(IDX, encoding="utf-8"))
    # 目录名口径：老行的 localPath 是历史遗留（英文产品名），与新册的中文目录不在同一空间。
    # 判断"整产品全新"必须用门户清单里的目录名，两边同域才可比。
    man = json.load(open(os.path.join(ROOT, os.pardir, os.pardir, ".scratch", "en_all.json"), encoding="utf-8"))
    folder_by_id = {r["id"]: r["localPath"].split("/")[1] for r in man}
    old_folders = {v for k, v in folder_by_id.items()
                   if any(k == r["id"] and r.get("version") == "V3.18.6" for r in rows)}
    old = {}
    for r in rows:
        if r["lang"] == "en" and r.get("version") == "V3.18.6":
            old[prod_key(r)[:2]] = r
    new = {}
    for r in rows:
        if r["lang"] == "en" and r.get("version") == "V3.18.6_2607":
            new[prod_key(r)[:2]] = r
    pairs = [(k, old[k], new[k]) for k in sorted(set(old) & set(new))]
    print(f"可配对 {len(pairs)} | _2607 独有 {len(new) - len(pairs)} | 老册未随 _2607 刷新 {len(old) - len(pairs)}")

    # 跨手册语频：用于剔除模板句
    freq = collections.Counter()
    cache = {}
    for k, ro, rn_ in pairs:
        for side, r in (("o", ro), ("n", rn_)):
            p = RN.parse(os.path.join(ROOT, r["markdown"]))
            s = sentences(p)
            cache[(k, side)] = (p, s)
            for h in s:
                freq[h] += 1
    thresh = max(6, int(0.08 * len(pairs) * 2 / 2))
    print(f"套话阈值：出现在 ≥{thresh} 本手册的句子按模板处理（配对数 {len(pairs)}）")

    out = []
    for (kp, kt), ro, rn_ in pairs:
        po, so = cache[((kp, kt), "o")]
        pn, sn = cache[((kp, kt), "n")]
        raw_add = [v for h, v in sn.items() if h not in so and freq[h] < thresh]
        raw_del = [v for h, v in so.items() if h not in sn and freq[h] < thresh]
        # 先取消"同句被改写/重排"的行，剩下的才是真正新增/消失的内容
        added_s, gone_s, reworded = cancel_reword(raw_add, raw_del)
        rank = lambda xs: sorted(xs, key=lambda x: (0 if INFO.search(x[1]) else 1, -len(NUMUNIT.findall(x[1]))))
        heads_add, heads_gone, renames = outline_delta(po, pn)
        lim = RN.limit_diff(po["tables"], pn["tables"])
        rel = RN.release_sections(pn)
        feat = [x for x in added_s if re.search(r"(?i)\b(support|add|new|introduc|allow|enable|now)\b", x[1])]
        DEP = re.compile(r"(?i)\bdeprecated\b|\breplaced by\b|\bno longer supported\b|"
                         r"\bno longer available\b|\bhas been (removed|retired|discontinued)\b|"
                         r"\bare (retired|discontinued)\b")   # 只认明确的弃用/下线措辞
        rem = [x for x in added_s + gone_s if DEP.search(x[1])]
        quant = [x for x in added_s if re.search(r"\d", x[1])]
        out.append({
            "product": ro["product"] or kp, "key": [kp, kt], "docType": kt,
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
    paired_keys = {(e["key"][0], e["key"][1]) for e in out}
    old_names = {}
    for r in rows:
        if r["lang"] == "en" and r.get("version") in ("V3.18.6", "V3.16.2"):
            old_names.setdefault(prod_key(r)[2], r["version"])

    def nearest(pname):
        """老集合里最接近的产品名：只有同名配不上时才用近似度说明"可能是改名/分版本"，
        不当作新产品宣布（新发布整套改了目录名，按目录名判定会把改名误报成新产品）。"""
        best, bs = "", 0.0
        for o, ver in old_names.items():
            ratio = difflib.SequenceMatcher(None, RN.norm(pname), RN.norm(o)).ratio()
            if ratio > bs:
                best, bs, bver = o, ratio, ver
        return best, round(bs, 3), bver if best else ""

    def ent(r):
        pn = prod_key(r)[2]
        nb, score, nver = (nearest(pn) if r.get("version") == "V3.18.6_2607" else ("", 0.0, ""))
        return {"id": r["id"], "product": pn, "docType": r.get("docType"),
                "pages": r.get("pages"), "ver": r.get("versionStamp"), "file": r["markdown"],
                "folder": folder_by_id.get(r["id"], ""), "nearestOld": nb,
                "nearScore": score, "nearestOldVersion": nver}
    json.dump({"pairs": out,
               "onlyNew": [ent(r) for k, r in new.items() if k not in paired_keys],
               "onlyOld": [ent(r) for k, r in old.items() if k not in paired_keys],
               "oldFolders": sorted(old_folders),
               "stats": {"pairs": len(out), "onlyNew": len(new) - len(out), "notRefreshed": len(old) - len(out)}},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    withd = sum(1 for e in out if e["sentAddTotal"] or e["sentDelTotal"] or e["newSectionsTotal"] or e["limits"])
    print(f"有实质差异的配对 {withd}/{len(out)}；句子级新增合计 {sum(e['sentAddTotal'] for e in out):,} 条，"
          f"删除合计 {sum(e['sentDelTotal'] for e in out):,} 条，配额差异 {sum(len(e['limits']) for e in out)} 处")
    print(f"→ {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
