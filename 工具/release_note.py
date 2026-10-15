"""Build an English 3.18.6 release note for Apsara Stack from the converted Markdown corpus.

Evidence rules (no invented claims):
  * manuals are paired per product/docType; product names are matched exactly after
    normalization, then by high string similarity (renames are reported as such)
  * from each manual: front-matter version stamps, heading outline, "release notes"-like
    sections (verbatim bullets), and limit/quota tables (numeric rows compared cell by cell)
  * every statement in the note cites product + manual file + section
  * anything without a 3.16.2 counterpart is listed under "not comparable", never summarized
    as "unchanged"
"""
import csv
import difflib
import json
import os
import re
import sys
from collections import defaultdict

ROOT = "/workspace/b845c37e-09f5-4e58-9113-3e8ea10d12f0/work/output/apsara-stack-docs"
os.chdir(ROOT)
FM = re.compile(r"^(title|product_version|doc_version|pdf_pages|source_pdf|source_url|converter): \"?([^\"\n]*)\"?$")
HEAD = re.compile(r"^(#{1,6})\s+(.*)$")
RN_HEAD = re.compile(r"(?i)\b(release\s*notes?|change\s*log|what'?s\s*new|version\s*(notes?|updates?|changes?)|"
                     r"new\s+features?|feature\s*(notes?|changes?)|修订|变更|新增特性)")
LIMIT_HEAD = re.compile(r"(?i)\b(limit|quota|maximum|constraint|限制|配额|规格上限)\w*")
API_TABLE = re.compile(r"(?i)\b(type|parameter|required|field|api name|response)\b")
NUM = re.compile(r"-?\d[\d,\.]*\s*(%|GiB|MiB|TiB|KB|MB|GB|TB|vCPU|characters?|seconds?|minutes?|hours?|days?|QPS|TPS|RPS)?", re.I)


def parse(path):
    """front matter + heading outline + section bodies + tables of one manual."""
    txt = open(path, encoding="utf-8").read()
    fm, body = {}, txt
    if txt.startswith("---"):
        end = txt.find("\n---", 3)
        for line in txt[3:end].split("\n"):
            m = FM.match(line.strip())
            if m:
                fm[m.group(1)] = m.group(2).strip()
        body = txt[end + 4:]
    heads, tables, secs = [], [], []
    cur, buf = None, []
    lines, i, fence = body.split("\n"), 0, False
    while i < len(lines):
        l = lines[i]
        if l.lstrip().startswith("```"):
            fence = not fence
            if cur is not None:
                buf.append(l)
            i += 1
            continue
        if fence:                                   # code inside a fence is never a heading
            if cur is not None:
                buf.append(l)
            i += 1
            continue
        if l.startswith("|") and i + 1 < len(lines) and lines[i + 1].startswith("|---"):
            rows, j = [], i
            while j < len(lines) and lines[j].startswith("|"):
                rows.append([c.strip() for c in lines[j].strip("|").split("|")])
                j += 1
            tables.append({"at": cur, "rows": rows})
            i = j
            continue
        m = HEAD.match(l)
        if m:
            if cur is not None:
                secs.append((cur, list(buf)))
            cur = m.group(2).strip()
            heads.append((len(m.group(1)), cur))
            buf = []
        elif cur is not None:
            buf.append(l)
        i += 1
    if cur is not None:
        secs.append((cur, list(buf)))
    return {"fm": fm, "heads": heads, "tables": tables, "secs": secs, "chars": len(body)}


def norm(s):
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", (s or "").lower())


def rows_key(r):
    return norm(r[0]) if r and r[0] else ""


def limit_diff(t16, t18):
    """Numeric/quota rows present only in 3.18.6, or with changed values."""
    out = []
    def usable(tabs):
        d = {}
        for t in tabs:
            at = (t["at"] or "").lower()
            hdr = " | ".join(t["rows"][0]).lower() if t["rows"] else ""
            if not LIMIT_HEAD.search(at):        # 标题须是限制/配额语义
                continue
            if API_TABLE.search(hdr):             # API 字段/参数表（含 Type/Parameter/Required/Field）不是配额表
                continue
            for row in t["rows"][1:]:
                k = rows_key(row)
                if len(k) >= 3:
                    d[(at, k)] = " | ".join(row)
        return d
    a, b = usable(t16), usable(t18)
    for k, v in b.items():
        if k not in a:
            if NUM.findall(v):                   # 新增配额项须含数值
                out.append(("new", k[0], v))
            continue
        if (NUM.findall(a[k]) or []) != (NUM.findall(v) or []):
            out.append(("changed", k[0], f"{a[k]}  →  {v}"))
    return out[:8]


def release_sections(p):
    """Sections the manual itself labels as release notes / what's new / change log."""
    got = []
    for cur, buf in p["secs"]:
        if cur and RN_HEAD.search(cur):
            body = re.sub(r"\bnts\b", " ", " ".join(x.strip() for x in buf if x.strip()))[:600]
            if body:
                got.append((cur, body))
    return got[:6]


def domain_lookup():
    """英文产品名 → 服务域：经中英对照表拿中文 code，再用中文缓存的 category。"""
    code_of, cat_of = {}, {}
    try:
        for r in csv.DictReader(open("中英对照手册映射.csv", encoding="utf-8-sig")):
            code_of[norm(r.get("英文产品名(国际版)") or "")] = (r.get("产品code") or "").strip()
    except Exception:
        pass
    rows = json.load(open("文档缓存索引.json", encoding="utf-8"))
    for r in rows:
        if r["lang"] == "zh":
            cat_of[(r.get("productCode") or "").lower()] = r.get("category") or "-"
    def dom(prod):
        c = code_of.get(norm(prod), "")
        return cat_of.get(c) or "-"
    return dom


def main():
    rows = json.load(open("文档缓存索引.json", encoding="utf-8"))
    dom = domain_lookup()
    md = [r for r in rows if r.get("markdown") and os.path.exists(r["markdown"])]
    byver = defaultdict(dict)
    for r in md:
        byver[r["version"]].setdefault((norm(r["product"]), r.get("docType") or r.get("category")), []).append(r)
    flat = {v: {k: x[0] for k, x in d.items()} for v, d in byver.items()}
    v18, v16 = flat.get("V3.18.6", {}), flat.get("V3.16.2", {})
    pairs, renamed, only18 = [], [], []
    used16 = set()
    for k, r18 in v18.items():
        pn, dt = k
        if k in v16:
            pairs.append((r18, v16[k], "exact"))
            used16.add(k)
            continue
        cand = [x for x in v16 if x[1] == dt and difflib.SequenceMatcher(None, pn, x[0]).ratio() > 0.86]
        if cand:
            pairs.append((r18, v16[cand[0]], f"rename≈{v16[cand[0]]['product']}"))
            used16.add(cand[0])
        else:
            only18.append(r18)
    print(f"配对 {len(pairs)} 组（精确 + 近似改名）｜3.18.6 独有 {len(only18)} 本｜可对比的 3.16.2 已用 {len(used16)}/{len(v16)}")

    ev = []
    e18_title = ""
    for r18, r16, how in sorted(pairs, key=lambda x: (x[0]["category"], x[0]["product"])):
        p18, p16 = parse(r18["markdown"]), parse(r16["markdown"])
        e18_title = (p18["heads"][0][1] if p18["heads"] else "") + ".md"
        h18 = {norm(t) for _l, t in p18["heads"]}
        h16 = {norm(t) for _l, t in p16["heads"]}
        skip = {norm(e18_title), norm(str(r18.get("product"))), norm(str(r18.get("docType") or ""))}
        newh = [t for _l, t in p18["heads"]
                if norm(t) and norm(t) not in h16 and len(norm(t)) > 4
                and norm(t) not in skip and not re.search(r"\d{8}", t)
                and not re.search(r"(?i)\b(table of contents|preface|conventions|legal disclaimer)\b", t)
                and not re.search(r"(?i)\b(the|of|about|and|to|in|for|a|an|with|by|as)\W*$", t.strip())
                and not re.search(r"[=;{}<>]|https?://|\.(com|md|pdf)$", t)
                and 5 <= len(t) <= 88 and not t.rstrip().endswith(("-", "–", "—"))
                and not re.match(r"(?i)^alibaba cloud apsara stack", t)]
        new_total = len(newh)
        seen_h, newh2 = set(), []
        for t in newh:
            k = norm(t)
            if k not in seen_h:
                seen_h.add(k)
                newh2.append(t)
        newh = newh2[:10]
        goneh = [t for _l, t in p16["heads"]
                 if norm(t) and norm(t) not in h18 and 5 <= len(t) <= 88
                 and not re.search(r"\d{8}|[=;{}<>]", t)
                 and norm(t) != norm(str(r16.get("product")))
                 and not re.match(r"(?i)^alibaba cloud apsara stack", t)
                 and not t.rstrip().endswith(("-", "–", "—"))]
        gone_total = len(goneh)
        seen_g, goneh2 = set(), []
        for t in goneh:
            k = norm(t)
            if k not in seen_g:
                seen_g.add(k)
                goneh2.append(t)
        goneh = goneh2[:6]
        ev.append({"cat": dom(r18["product"]) if dom(r18["product"]) != "-" else (r18.get("category") or "-"),
                   "rawCat": r18.get("category"), "docType": r18.get("docType") or r18.get("category"),
                   "product": r18["product"], "matched": how,
                   "18": {"file": r18["markdown"], "ver": r18.get("versionStamp"),
                          "pages": r18.get("pages"), "chars": p18["chars"], "heads": len(p18["heads"])},
                   "16": {"file": r16["markdown"], "ver": r16.get("versionStamp"),
                          "pages": r16.get("pages"), "chars": p16["chars"], "heads": len(p16["heads"])},
                   "new_sections": newh, "new_sections_total": new_total,
                   "dropped_sections": goneh, "dropped_sections_total": gone_total,
                   "release_notes_18": release_sections(p18), "release_notes_16": release_sections(p16),
                   "limits": limit_diff(p16["tables"], p18["tables"])})
    json.dump({"pairs": ev, "only18": [{"product": x["product"], "docType": x.get("docType"),
                                       "file": x["markdown"], "pages": x.get("pages"), "cat": x["category"]}
                                      for x in only18],
               "counts": {"pairs": len(pairs), "only18": len(only18), "v16_total": len(v16)}},
              open("/tmp/release_note_evidence.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tot_new = sum(len(x["new_sections"]) for x in ev)
    tot_lim = sum(len(x["limits"]) for x in ev)
    tot_bn = sum(1 for x in ev if x["release_notes_18"])
    print(f"证据汇总：新增小节 {tot_new} ｜限制/配额差异 {tot_lim} ｜含官方 Release notes 段的手册 {tot_bn}")
    print("写出 /tmp/release_note_evidence.json")


if __name__ == "__main__":
    main()
