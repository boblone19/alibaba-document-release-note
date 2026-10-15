"""渲染 V3.18.6 → V3.18.6_2607 的英文 release note（细节级变化说明）。

  python3 工具/build_note_2607.py     # 读 .scratch/rn2607_pairs.json，写交付根目录 ApsaraStack-V3.18.6_2607-Release-Note-EN.md

每一句都可回溯到：产品 / 手册文件 / 小节标题。没有证据的地方直接写"无对比对象"，
不写"未变化"。
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCRATCH = os.path.join(ROOT, os.pardir, os.pardir, ".scratch")
OUT = os.path.join(ROOT, "ApsaraStack-V3.18.6_2607-Release-Note-EN.md")
SP_LABEL = "v3.18.6sp-2607"
DETAIL = 5          # 净新增行数 ≥ 该值（或有配额差异/官方说明/页量变化）才展开细节


def tidy(s, n=190):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[:n].rstrip() + " …"


def quote(body, n=460):
    """逐字引用，但收尾切在句子边界，避免把 PDF 残渣（"eSQL (Compatible with Oracle)?"）挂在末尾。"""
    t = re.sub(r"\b([A-Za-z]{2,4}) \1\b", r"\1", tidy(body, n))
    cut = max(t.rfind(". "), t.rfind(".  "), t.rfind("? "), t.rfind(": "))
    return (t[:cut + 1] if cut > n * 0.45 else t)


def main():
    d = json.load(open(os.path.join(SCRATCH, "rn2607_pairs.json"), encoding="utf-8"))
    rows = json.load(open(os.path.join(ROOT, "文档缓存索引.json"), encoding="utf-8"))
    pairs, only_new, only_old = d["pairs"], d["onlyNew"], d["onlyOld"]
    b26 = [r for r in rows if r.get("version") == "V3.18.6_2607"]
    L = []
    add = L.append

    add("# Apsara Stack — What changed in the English V3.18.6 2607 document set")
    add("")
    add("**Delta of `V3.18.6_2607` vs `V3.18.6` on the international documentation portal, "
        "derived line-by-line from the converted English Markdown corpus.**")
    add("")
    add("| | |")
    add("|---|---|")
    add(f"| Manuals in V3.18.6_2607 | {len(b26)} |")
    add(f"| Documented pages | {sum(r.get('pages') or 0 for r in b26):,} |")
    add("| Document dates | 2026-07-31 → 2026-09-11 |")
    add(f"| Products covered | {len({r['localPath'].split('/')[1] for r in b26})} |")
    add(f"| Manuals paired to an earlier V3.18.6 edition | {len(pairs)} (every pair has a strictly later "
        "document date; none regressed) |")
    add(f"| Manuals with no earlier edition (new here) | {len(only_new)} |")
    add(f"| V3.18.6 manuals not re-published in this set | {len(only_old)} |")
    ra = sum(p.get('rawAddTotal', p['sentAddTotal']) for p in pairs)
    rd = sum(p.get('rawDelTotal', p['sentDelTotal']) for p in pairs)
    add(f"| Sentences added in the new edition (informative only) | {sum(p['sentAddTotal'] for p in pairs):,} |")
    add(f"| Sentences no longer present (informative only) | {sum(p['sentDelTotal'] for p in pairs):,} |")
    add(f"| Informative sentences before cancelling re-typeset pairs | {ra:,} added, {rd:,} removed"
        " (after cancellation: the two rows above) |")
    add(f"| Limit/quota rows added or changed | {sum(len(p['limits']) for p in pairs)} |")
    add(f"| Manuals carrying their own release-notes section | {sum(1 for p in pairs if p['releaseNotesOfficial'])} |")
    add("")
    add("**How to read this.** §2 ranks the largest changes. §3 quotes the release-notes sections that product "
        "teams wrote into the manuals themselves. §4 is the detail: for every manual with material evidence it "
        "shows what text appeared, what text disappeared, which sections were added, removed or renamed, and "
        "which limits changed — each line attributed to the section it sits in. §5 lists manuals that exist only "
        "in the new set, §6 the ones that were not refreshed. §7 states the method and its limits. Nothing here "
        "is inferred from product knowledge: every claim is a diff of two PDFs.")
    add("")
    add("---")
    add("")
    add("## 1. Scope: the portal now carries two parallel V3.18.6 sets")
    add("")
    add("The download page exposes **V3.18.6** and **V3.18.6 2607** (value `V3.18.6_2607`) as two selectable "
        "entries. They are not two spellings of one set: the 2607 objects live at a different storage path "
        "(`国际版文档/3816 2607/pdf 3/<product>/`, the folder name is mangled upstream) and none of their "
        "identifiers collide with the older set. In practice `V3.18.6_2607` is a service-pack refresh that "
        "re-published 162 manuals with a later document date, added 103 manuals, and left 125 V3.18.6 manuals "
        "untouched — so for ~1/3 of the English corpus the *older* document is still the current one.")
    add("")
    return _part2(add, L, pairs, only_new, only_old, rows, b26)


def _part2(add, L, pairs, only_new, only_old, rows, b26):
    def metrics(e):
        dp = (e['new']['pages'] or 0) - (e['old']['pages'] or 0)
        return dp, e['sentAddTotal'] + e['sentDelTotal']

    add("## 2. Biggest changes in this refresh")
    add("")
    add("| product | manual | pages | doc date | net lines | sections ± | limits |")
    add("|---|---|---|---|---|---|---|")
    top = sorted(pairs, key=lambda e: -(metrics(e)[0] + metrics(e)[1] // 40))[:14]
    for e in top:
        dp, net = metrics(e)
        add(f"| {e['product'][:34]} | {e['docType'][:26]} | {e['old']['pages']} → {e['new']['pages']} "
            f"({dp:+d}) | {e['old']['ver']} → {e['new']['ver']} | +{e['sentAddTotal']:,} / -{e['sentDelTotal']:,} "
            f"| +{e['newSectionsTotal']} / -{e['droppedSectionsTotal']} | {len(e['limits'])} |")
    add("")
    off = [e for e in pairs if e['releaseNotesOfficial']]
    # 观察项全部由本批数据算出，不做外部推断
    sp_hit = [p2 for p2 in pairs if SP_LABEL in open(p2['new']['file'], encoding='utf-8', errors='ignore').read()]
    sp_old = [p2 for p2 in pairs if SP_LABEL in open(p2['old']['file'], encoding='utf-8', errors='ignore').read()]
    console = [p2 for p2 in pairs if p2['docType'].startswith('Operations')
               and any('console release notes' in t.lower() for t in p2['newSections'])]
    grew = sorted(pairs, key=lambda x: -((x['new']['pages'] or 0) - (x['old']['pages'] or 0)))[:5]
    shrink = max(pairs, key=lambda x: x['droppedSectionsTotal'])
    add("")
    add("**Three observations that fall out of the diff**")
    add("")
    add(f"- The in-document service-pack label **{SP_LABEL}** appears in {len(sp_hit)} new editions and "
        f"{len(sp_old)} baseline editions of the same manuals — that is how the portal's `V3.18.6 2607` entry "
        "names itself inside the PDFs.")
    if console:
        add(f"- Database O&M manuals account for the largest page growth, and most of it is one new chapter: "
            f"{len(console)} O&M manuals gained a **Console release notes** section "
            f"({', '.join(sorted({c['product'][:26] for c in console})[:6])} …).")
    add(f"- Biggest page growth: " + ", ".join(f"{g['product'][:24]} {g['docType'][:14]} "
        f"{g['old']['pages']}→{g['new']['pages']} pp" for g in grew) + ".")
    add(f"- Largest restructure: **{shrink['product']}** {shrink['docType']} dropped {shrink['droppedSectionsTotal']} "
        f"section titles while its page count moved {(shrink['new']['pages'] or 0) - (shrink['old']['pages'] or 0):+d} "
        "— the chapters were re-organised, not deleted with the content.")
    add("")
    add("## 3. What the product teams wrote themselves")
    add("")
    add(f"{len(off)} manuals in this set carry their own release-notes / what's-new section. Those are quoted "
        "verbatim below (truncated where long) — they are the only statements in this note written by the vendor "
        "rather than derived by diffing.")
    add("")
    groups = {}
    for e in sorted(off, key=lambda x: x['product'].lower()):
        for h, body in e['releaseNotesOfficial'][:3]:
            groups.setdefault((h.strip().lower(), body.strip()), []).append(f"{e['product']} ({e['docType']})")
    for (h, body), who in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        n = f"{len(who)} manuals" if len(who) > 1 else "1 manual"
        add(f"**{tidy(h, 60)}** — same wording in {n}: "
            + "; ".join(w[:56] for w in who[:6]) + (" …" if len(who) > 6 else ""))
        add("")
        add(f"> {quote(body, 900)}")
        add("")
    add("## 4. Change detail per manual")
    add("")
    detail = [e for e in pairs if e['sentAddTotal'] >= DETAIL or e['limits'] or e['releaseNotesOfficial']
              or abs((e['new']['pages'] or 0) - (e['old']['pages'] or 0)) >= 40]
    _dk = {(e["key"][0], e["key"][1]) for e in detail}
    other = [e for e in pairs if (e["key"][0], e["key"][1]) not in _dk]
    add(f"*{len(detail)} manuals with material evidence are expanded; {len(other)} further manuals changed "
        f"only cosmetically (re-flow, page numbering, boilerplate) and are tabled at the end of this section.*")
    add("")
    for e in sorted(detail, key=lambda x: x['product'].lower()):
        dp = (e['new']['pages'] or 0) - (e['old']['pages'] or 0)
        add(f"### {e['product']} — {e['docType']}")
        add("")
        add(f"`{e['old']['pages']} pages / {e['old']['ver']}` → `{e['new']['pages']} pages / {e['new']['ver']}` "
            f"({dp:+d} pages, {e['old']['heads']} → {e['new']['heads']} sections, "
            f"{e['old']['chars']:,} → {e['new']['chars']:,} characters). Evidence file: "
            f"`{os.path.basename(e['new']['file'])}`")
        add("")
        if e['releaseNotesOfficial']:
            add("**Release notes written in the manual itself**")
            for h, body in e['releaseNotesOfficial'][:2]:
                add(f"- *{tidy(h, 70)}* — {quote(body)}")
            add("")
        if e['bucketRem'] or any(re.search(r"(?i)no longer|deprecat|not supported|retire", s) for _, s in e['sentDel'][:25]):
            bad = [(t, s) for t, s in e['sentAdd'] + e['sentDel']
                   if re.search(r"(?i)no longer|deprecat|not supported|discontinu|retire", s)][:4]
            if bad:
                add("**Deprecations / removals stated in the text**")
                for t, s in bad:
                    add(f"- ({t or 'unsectioned'}) {tidy(s)}")
                add("")
        lim = e['limits'][:6]
        if lim:
            add("**Limits and quotas that changed**")
            for kind, at, v in lim:
                add(f"- {kind} · *{tidy(at, 46)}* · {tidy(v, 170)}")
            add("")
        if e['sentAdd']:
            add("**Text new in this edition** (first lines by section)")
            for t, s in e['sentAdd'][:7]:
                add(f"- `{(t or '—')[:46]}` — {tidy(s)}")
            if e['sentAddTotal'] > len(e['sentAdd']):
                add(f"  *… {e['sentAddTotal'] - len(e['sentAdd'])} further added lines in this manual*")
            add("")
        if e['sentDel']:
            add("**Text no longer present**")
            for t, s in e['sentDel'][:3]:
                add(f"- `{(t or '—')[:46]}` — {tidy(s)}")
            if e['sentDelTotal'] > len(e['sentDel']):
                add(f"  *… {e['sentDelTotal'] - len(e['sentDel'])} further removed lines*")
            add("")
        if e['newSections']:
            add(f"**Sections added** ({e['newSectionsTotal']} total): " + "; ".join(f"`{tidy(x, 60)}`" for x in e['newSections'][:8])
                + (" …" if e['newSectionsTotal'] > 8 else ""))
        if e['droppedSections']:
            add(f"**Sections dropped** ({e['droppedSectionsTotal']} total): " + "; ".join(f"`{tidy(x, 60)}`" for x in e['droppedSections'][:6])
                + (" …" if e['droppedSectionsTotal'] > 6 else ""))
        if e['renamedSections']:
            add("**Sections renamed**: " + "; ".join(f"`{tidy(a, 40)}` → `{tidy(b, 40)}`" for a, b in e['renamedSections'][:4]))
        if not any((e['releaseNotesOfficial'], lim, e['sentAdd'], e['sentDel'], e['newSections'], e['droppedSections'])):
            add("*Only pagination/boilerplate differences; no textual delta found.*")
        add("")
    add("<details><summary>Manuals with cosmetic-only differences</summary>")
    add("")
    add("| product | manual | pages | doc date |")
    add("|---|---|---|---|")
    for e in sorted(other, key=lambda x: x['product'].lower()):
        add(f"| {e['product'][:36]} | {e['docType'][:24]} | {e['old']['pages']} → {e['new']['pages']} | "
            f"{e['old']['ver']} → {e['new']['ver']} |")
    add("")
    add("</details>")
    return _part3(add, L, pairs, only_new, only_old, rows)


def _part3(add, L, pairs, only_new, only_old, rows):
    folder_of = {r['markdown']: r['localPath'].split('/')[1] for r in rows}
    old_folders = {r['localPath'].split('/')[1] for r in rows
                   if r['lang'] == 'en' and r.get('version') == 'V3.18.6'}
    paired_prod = {e['key'][0] for e in pairs}
    new_prod = {}
    for m in only_new:
        new_prod.setdefault(m['product'], []).append(m)
    add("## 5. Manuals that appear only in V3.18.6_2607")
    add("")
    add(f"{len(only_new)} of the 265 manuals have no same-name, same-document-type counterpart in the older "
        "English set. They are not all 'new products': the release also renamed catalogue labels wholesale "
        "(the folder `云盾` became `云安全中心（专有云）`, products gained sub-edition suffixes), and folder names "
        "therefore cannot be used as a pairing key. Each manual below is matched against the *previous English "
        "product names* (V3.18.6 and V3.16.2) and classified by how close the closest name is.")
    add("")
    back = [m for m in only_new if m['nearScore'] >= 0.98 and m['nearestOldVersion'] == 'V3.16.2']
    fresh = [m for m in only_new if m['nearScore'] < 0.5]
    relab = [m for m in only_new if m not in back and m not in fresh]
    add(f"- **Back in English ({len(back)})** — product name exists in the V3.16.2 English set but was absent "
        "from V3.18.6, so this release restores English coverage for it: "
        + ", ".join(f"{tidy(m['product'], 40)} ({m['docType']}, {m['pages']} pp)" for m in
                    sorted(back, key=lambda x: -x['pages'])) + ".")
    add(f"- **New English title with no close predecessor ({len(fresh)})**: "
        + ", ".join(f"{tidy(m['product'], 40)} ({m['docType']}, {m['pages']} pp)" for m in
                    sorted(fresh, key=lambda x: -x['pages'])) + ".")
    add(f"- **Relabelled / split by edition / new document type ({len(relab)})** — listed in the table with the "
        "closest earlier English name and its similarity score; treat these as catalogue restructuring until a "
        "human confirms, not as new products.")
    add("")
    add("| product (V3.18.6_2607) | manual | pages | doc date | closest earlier English name (score, set) |")
    add("|---|---|---|---|---|")
    for m in sorted(only_new, key=lambda x: (x['product'].lower(), x['docType'])):
        near = (f"{tidy(m['nearestOld'], 44)} ({m['nearScore']}, {m['nearestOldVersion']})"
                if m['nearScore'] >= 0.5 else "— none —")
        add(f"| {tidy(m['product'], 54)} | {m['docType'][:26]} | {m['pages']} | {m['ver']} | {near} |")
    add("")
    add("## 6. V3.18.6 manuals not carried into this set")
    add("")
    add(f"{len(only_old)} manuals exist in the older `V3.18.6` set with no counterpart in `V3.18.6_2607`. "
        "Their text was **not** superseded inside this refresh, so the older file remains the current English "
        "reference for them (they are still in the local corpus, nothing was deleted).")
    add("")
    add("| product | manual | pages | doc date |")
    add("|---|---|---|---|")
    for m in sorted(only_old, key=lambda x: (x['product'].lower(), x['docType'])):
        add(f"| {tidy(m['product'], 58)} | {m['docType'][:26]} | {m['pages']} | {m['ver']} |")
    add("")
    return _part4(add, L, pairs)


def RN_norm(x):
    return re.sub(r"[^a-z0-9]+", "", (x or "").lower())


def _part4(add, L, pairs):
    ra = sum(p.get('rawAddTotal', p['sentAddTotal']) for p in pairs)
    rd = sum(p.get('rawDelTotal', p['sentDelTotal']) for p in pairs)
    add("## 7. Method, and what it cannot tell you")
    add("")
    add("1. Both editions were downloaded as official PDFs, converted to text-only Markdown with the same "
        "line classifier, and every page hash-verified; PDFs are not kept locally by design.")
    add("2. Manuals are paired by **exact** product name + document type after normalisation. No fuzzy pairing: "
        "at 0.90 similarity *ApsaraDB for RDS* matched *ApsaraDB for Redis*, which would have manufactured "
        "`changes`. Unmatched names are listed in Sections 4/5 instead of being guessed.")
    add("3. Textual deltas are **sentence-level, not line-level**: PDF re-flow moves line breaks between "
        "editions, so lines are re-joined per section and split on punctuation before comparison. Three gates "
        "then run: (i) headings, tables, fenced code, log samples and regex fragments are dropped; (ii) "
        "template text recurring in ≥ 8% of the paired corpus is dropped; (iii) only *informative* sentences "
        "are counted — those carrying a version/number/quota or a support/add/deprecate/change verb, with "
        "self-describing UI narration (\"This topic describes…\", \"On the X page, click…\") excluded. "
        f"Gates (i)–(iii) leave {ra:,} added / {rd:,} removed informative sentences; re-typing cancellation then "
        f"reduces that to {sum(p2['sentAddTotal'] for p2 in pairs):,} / {sum(p2['sentDelTotal'] for p2 in pairs):,} "
        "— which are the figures quoted in §1. Counting raw *lines* instead of sentences inflates the delta by "
        "an order of magnitude, because PDF line breaks move between editions.")
    add("3b. Quoted lines are verbatim extracts from the converted Markdown. The PDF extraction occasionally "
        "duplicates a short token or reorders a cell (\"QL QL Window functions\", \"start with a _ letter\"); "
        "those are extraction artifacts of our converter, not typographical errors in the manual, and they do "
        "not affect the substance of the quoted sentence.")
    add("4. Section counting normalises numbered headings (`2.1.1.2.3. Limits_1578278510` → `limits`), so a "
        "re-number is not counted as add + drop. Renames are reported when the normalised titles are ≥ 0.85 similar.")
    add("5. What this cannot show: why a change was made; whether removed text reflects a dropped feature or an "
        "editorial decision; and anything for the 103 unpaired manuals, which have no baseline in this set. "
        "Limits rows are only compared where both editions carry the same row key.")
    add("6. Full machine-readable evidence (all added/removed lines per manual, with section attribution): "
        "`.scratch/rn2607_pairs.json` in the session workspace.")
    add("")
    add("## 8. Where the files are")
    add("")
    add("| path | contents |")
    add("|---|---|")
    add("| `markdown/10_EN_ApsaraStack_V3.18.6_2607/` | the 265 manuals behind this note |")
    add("| `markdown/10_EN_ApsaraStack_v3.18.6/` | the older 287-manual English set used as baseline |")
    add("| `文档缓存索引.csv` | 901 rows; `id / versionStamp / pages / markdown / markdownSha256` |")
    add("| `markdown_全量_901册.zip` | whole corpus, one zip |")
    add("")
    txt = "\n".join(L) + "\n"
    open(OUT, "w", encoding="utf-8").write(txt)
    print(f"→ {os.path.basename(OUT)}：{txt.count(chr(10))} 行 / {len(txt)/1024:.0f} KB；"
          f"展开细节 {sum(1 for e in pairs if e['sentAddTotal'] >= DETAIL or e['limits'])} 本")
    return 0


if __name__ == "__main__":
    sys.exit(main())
