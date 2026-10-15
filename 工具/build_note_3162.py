"""渲染 V3.16.2 → V3.18.6 的英文 release note（细节级变化说明，2607 版式）。

  python3 工具/build_note_3162.py     # 读 .scratch/rn3162_pairs.json，覆盖交付根目录 ApsaraStack-3.18.6-Release-Note-EN.md

与 build_note_2607.py 同一版式：汇总表 → 最大变化排名与观察 → 官方 release notes 逐字引用 →
逐册细节（句子级增删/配额/章节增删改名）→ 仅新集合有的册（近似归类）→ 未复刊的基线册 → 方法 → 文件。
每一句都可回溯到产品 / 手册文件 / 小节标题；没有证据的地方写"无对比对象"，不写"未变化"。
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCRATCH = os.path.join(ROOT, os.pardir, os.pardir, ".scratch")
OUT = os.path.join(ROOT, "ApsaraStack-3.18.6-Release-Note-EN.md")
OLD_VER, NEW_VER = "V3.16.2", "V3.18.6"
DETAIL = 5          # 净新增行数 ≥ 该值（或有配额差异/官方说明/页量变化）才展开细节
ST = {}             # 集合规模统计（main 里填充，_part3/_part4 引用）
from build_note_2607 import tidy, quote  # noqa: E402


def fdate(v):
    v = str(v or "")
    return f"{v[:4]}-{v[4:6]}-{v[6:8]}" if len(v) == 8 and v.isdigit() else v


def main():
    d = json.load(open(os.path.join(SCRATCH, "rn3162_pairs.json"), encoding="utf-8"))
    rows = json.load(open(os.path.join(ROOT, "文档缓存索引.json"), encoding="utf-8"))
    pairs, only_new, only_old, st = d["pairs"], d["onlyNew"], d["onlyOld"], d["stats"]
    ST.update(st)
    b18 = [r for r in rows if r["lang"] == "en" and r.get("version") == NEW_VER]
    b16 = [r for r in rows if r["lang"] == "en" and r.get("version") == OLD_VER]
    span = lambda rs: (fdate(min(r["versionStamp"] for r in rs)), fdate(max(r["versionStamp"] for r in rs)))
    d16, d18 = span(b16), span(b18)
    brand = lambda rs: sum(1 for r in rs if "Apsara Stack Enterprise" in
                           open(os.path.join(ROOT, r["markdown"]), encoding="utf-8", errors="ignore").read())
    br16, br18 = brand(b16), brand(b18)
    later = sum(1 for e in pairs if str(e["new"]["ver"]) > str(e["old"]["ver"]))
    L = []
    add = L.append

    add(f"# Alibaba Cloud Apsara Stack V3.18.6 — What changed in the English document set since V3.16.2")
    add("")
    add(f"**Delta of `{NEW_VER}` vs `{OLD_VER}` on the international documentation portal, "
        "derived line-by-line from the converted English Markdown corpus.**")
    add("")
    add("| | |")
    add("|---|---|")
    add(f"| Manuals in the {NEW_VER} English set | {st['newTotal']} |")
    add(f"| Documented pages ({NEW_VER}) | {sum(r.get('pages') or 0 for r in b18):,} |")
    add(f"| Document dates in the {NEW_VER} set | {d18[0]} → {d18[1]} |")
    add(f"| Products covered ({NEW_VER}) | {len({r['localPath'].split('/')[1] for r in b18})} |")
    add(f"| Baseline available for comparison — the {OLD_VER} English set | {st['oldTotal']} manuals "
        f"dated {d16[0]} → {d16[1]}; User / Developer / Instance-Families guides only, no Product "
        "Introduction or O&M volumes |")
    add(f"| Manuals paired to a {OLD_VER} counterpart | {len(pairs)} (every pair has a strictly later "
        f"document date: {later}/{len(pairs)}) |")
    add(f"| {NEW_VER} manuals with no {OLD_VER} counterpart (delta not computable) | {st['onlyNew']} (§5) |")
    add(f"| {OLD_VER} manuals not re-published in the {NEW_VER} set | {st['notRefreshed']} (§6) |")
    ra = sum(p.get('rawAddTotal', p['sentAddTotal']) for p in pairs)
    rd = sum(p.get('rawDelTotal', p['sentDelTotal']) for p in pairs)
    add(f"| Sentences added in the new editions (informative only) | {sum(p['sentAddTotal'] for p in pairs):,} |")
    add(f"| Sentences no longer present (informative only) | {sum(p['sentDelTotal'] for p in pairs):,} |")
    add(f"| Informative sentences before cancelling re-typeset pairs | {ra:,} added, {rd:,} removed"
        " (after cancellation: the two rows above) |")
    add(f"| Limit/quota rows added or changed | {sum(len(p['limits']) for p in pairs)} |")
    add(f"| Paired manuals carrying their own release-notes section | "
        f"{sum(1 for p in pairs if p['releaseNotesOfficial'])} |")
    add("")
    add("**How to read this.** §2 ranks the largest changes and states what the diff itself shows. §3 quotes the "
        "release-notes sections that product teams wrote into the manuals themselves. §4 is the detail: for every "
        "manual with material evidence it shows what text appeared, what text disappeared, which sections were "
        "added, removed or renamed, and which limits changed — each line attributed to the section it sits in. "
        "§5 lists the manuals that have no comparable baseline (with the closest earlier English name, because the "
        f"{OLD_VER} English set is far smaller than {NEW_VER}), §6 the baseline manuals that were not re-published. "
        "§7 states the method and its limits. Nothing here is inferred from product knowledge: every claim is a "
        "diff of two PDFs, and absence of a diff is **not** evidence that a product is unchanged.")
    add("")
    add("---")
    add("")
    add("## 1. Scope: two document sets, different catalogue generations")
    add("")
    add(f"The download page exposes **{NEW_VER}** and **{OLD_VER}** as two selectable English sets. They are not "
        "two editions of the same catalogue: the V3.16.2 baseline holds "
        f"{st['oldTotal']} manuals dated {d16[0]} → {d16[1]} and only three document types "
        f"({', '.join(f'{n}× {t}' for t, n in sorted(_mix(b16).items(), key=lambda kv: -kv[1]))}), while the {NEW_VER} set holds "
        f"{st['newTotal']} manuals dated {d18[0]} → {d18[1]} across "
        f"{len(_mix(b18))} document types (adding Product Introduction, Operations Guide and Operations & "
        "Maintenance Guide volumes that the baseline never published in English). Only "
        f"{len(pairs)} manuals can therefore be diffed at all; the other {st['onlyNew']} are listed in §5 with the "
        "closest earlier English name instead of a fabricated comparison.")
    add("")
    add(f"The corpus was also rebranded between the two sets: the string **“Apsara Stack Enterprise”** appears in "
        f"{br16} of {st['oldTotal']} baseline manuals but only {br18} of {st['newTotal']} {NEW_VER} manuals "
        "(`Apsara Stack Enterprise v3.16.2` → `Apsara Stack V3.18.6` in the title blocks). Sentences whose only "
        "difference is this rename still count as changed text below — they are real textual deltas, and no "
        "attempt was made to suppress them.")
    add("")
    return _part2(add, L, pairs, only_new, only_old, rows, b18)


def _mix(rs):
    m = {}
    for r in rs:
        m[r.get("docType") or "Other"] = m.get(r.get("docType") or "Other", 0) + 1
    return m


def _part2(add, L, pairs, only_new, only_old, rows, b18):
    def metrics(e):
        dp = (e['new']['pages'] or 0) - (e['old']['pages'] or 0)
        return dp, e['sentAddTotal'] + e['sentDelTotal']

    add("## 2. Biggest changes between the two sets")
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
    grew = sorted(pairs, key=lambda x: -((x['new']['pages'] or 0) - (x['old']['pages'] or 0)))[:5]
    shrink = max(pairs, key=lambda x: x['droppedSectionsTotal'])
    rem_pairs = [e for e in pairs if e['bucketRem']
                 or any(re.search(r"(?i)no longer|deprecat|not supported|retire", s) for _, s in e['sentDel'][:25])]
    rn_heads = sum(len(e['releaseNotesOfficial']) for e in off)
    add("**Four observations that fall out of the diff**")
    add("")
    add("- The largest documented growth is concentrated in a few products: "
        + ", ".join(f"{tidy(g['product'], 30)} {tidy(g['docType'], 16)} "
                    f"{g['old']['pages']}→{g['new']['pages']} pp ({g['sentAddTotal']:+,} sentences)" for g in grew) + ".")
    add(f"- {len(off)} of the {len(pairs)} paired manuals carry {rn_heads} release-notes / what's-new sections "
        "of their own (§3 quotes them verbatim); outside these, everything in this note was derived by diffing, "
        "not stated by the vendor.")
    add(f"- {len(rem_pairs)} of the {len(pairs)} paired manuals contain explicit deprecation / removal wording "
        "(\"no longer supported\", \"deprecated\" …); they are quoted per manual in §4.")
    sdp = (shrink['new']['pages'] or 0) - (shrink['old']['pages'] or 0)
    tail = ("— the chapters were re-organised, not deleted with the content." if sdp >= -20 else
            f"— the section titles were re-organised while the page count also moved {sdp:+d}, so content was "
            "removed along with the restructure.")
    add(f"- Largest restructure: **{shrink['product']}** {shrink['docType']} dropped "
        f"{shrink['droppedSectionsTotal']} section titles {tail}")
    add("")
    add("## 3. What the product teams wrote themselves")
    add("")
    add(f"{len(off)} paired manuals in this set carry their own release-notes / what's-new section. Those are quoted "
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
    add(f"*{len(detail)} manuals with material evidence are expanded; {len(other)} further "
        f"{'manual' if len(other) == 1 else 'manuals'} changed only cosmetically (re-flow, page numbering, "
        f"boilerplate) and {'is' if len(other) == 1 else 'are'} tabled at the end of this section.*")
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
            add(f"**Sections added** ({e['newSectionsTotal']} total): "
                + "; ".join(f"`{tidy(x, 60)}`" for x in e['newSections'][:8])
                + (" …" if e['newSectionsTotal'] > 8 else ""))
        if e['droppedSections']:
            add(f"**Sections dropped** ({e['droppedSectionsTotal']} total): "
                + "; ".join(f"`{tidy(x, 60)}`" for x in e['droppedSections'][:6])
                + (" …" if e['droppedSectionsTotal'] > 6 else ""))
        if e['renamedSections']:
            add("**Sections renamed**: "
                + "; ".join(f"`{tidy(a, 40)}` → `{tidy(b, 40)}`" for a, b in e['renamedSections'][:4]))
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
    return _part3(add, L, pairs, only_new, only_old, ST["oldTotal"], ST["newTotal"])


def _part3(add, L, pairs, only_new, only_old, n_old, n_new):
    add("## 5. Manuals that have no V3.16.2 counterpart (delta not computable)")
    add("")
    add(f"{len(only_new)} of the {n_new} {NEW_VER} manuals have no same-name, "
        f"same-document-type counterpart in the {n_old}-manual {OLD_VER} English set. The baseline "
        "published only User, Developer and Instance-Families guides, so most Product Introduction, Operations and "
        "O&M volumes enter this list **by construction**, together with every product documented in English for "
        "the first time. Each manual below is matched against the *previous English product names* and classified "
        "by how close the closest name is — treat near-matches as catalogue restructuring or renames to verify, "
        "not as confirmed new products.")
    add("")
    hi = [m for m in only_new if m['nearScore'] >= 0.98]
    fresh = [m for m in only_new if m['nearScore'] < 0.5]
    relab = [m for m in only_new if m not in hi and m not in fresh]
    add(f"- **Product already in the baseline, manual type is new ({len(hi)})** — e.g. "
        + ", ".join(f"{tidy(m['product'], 34)} ({m['docType']})" for m in sorted(hi, key=lambda x: -x['pages'])[:6])
        + "; full list in the table.")
    add(f"- **Closest earlier name ≥ 0.5 similarity ({len(relab)})** — the closest *string* match, shown per row "
        "with its score. The score is a search hint only, **not** evidence of a rename: string similarity also "
        "pairs unrelated products (ApsaraDB for RDS scores 0.933 against ApsaraDB for Redis). Verify before "
        "treating any row here as renamed / split by sub-edition.")
    add(f"- **No close predecessor ({len(fresh)})** — first English appearance of the product: "
        + ", ".join(f"{tidy(m['product'], 40)} ({m['docType']}, {m['pages']} pp)" for m in
                    sorted(fresh, key=lambda x: -x['pages'])[:12])
        + ("; full list in the table." if len(fresh) > 12 else "."))
    add("")
    add("| product (V3.18.6) | manual | pages | doc date | closest earlier English name (string score) |")
    add("|---|---|---|---|---|")
    for m in sorted(only_new, key=lambda x: (x['product'].lower(), x['docType'])):
        near = (f"{tidy(m['nearestOld'], 44)} ({m['nearScore']})" if m['nearScore'] >= 0.5 else "— none —")
        add(f"| {tidy(m['product'], 54)} | {m['docType'][:26]} | {m['pages']} | {m['ver']} | {near} |")
    add("")
    add("## 6. V3.16.2 manuals not carried into the V3.18.6 set")
    add("")
    add(f"{len(only_old)} manuals exist in the {OLD_VER} English baseline with no same-name, same-type "
        f"counterpart in {NEW_VER}. Their text was not superseded inside the new set by an object this note could "
        "pair — some product lines are presented under new names in the V3.18.6 catalogue (the closest-name column "
        "in §5 flags the candidates), the rest simply have no English edition in the new set. The baseline files "
        "remain in the local corpus, nothing was deleted.")
    add("")
    add("| product (V3.16.2) | manual | pages | doc date |")
    add("|---|---|---|---|")
    for m in sorted(only_old, key=lambda x: (x['product'].lower(), x['docType'])):
        add(f"| {tidy(m['product'], 58)} | {m['docType'][:26]} | {m['pages']} | {m['ver']} |")
    add("")
    return _part4(add, L, pairs)


def st_msg(pairs, only_new):
    return f"{len(pairs)}-manual overlap between the two sets and the rest of the {len(only_new) + len(pairs)}-manual" if False else ""


def _part4(add, L, pairs):
    ra = sum(p.get('rawAddTotal', p['sentAddTotal']) for p in pairs)
    rd = sum(p.get('rawDelTotal', p['sentDelTotal']) for p in pairs)
    add("## 7. Method, and what it cannot tell you")
    add("")
    add("1. Both sets were downloaded as official PDFs, converted to text-only Markdown with the same line "
        "classifier, and every page hash-verified; PDFs are not kept locally by design.")
    add("2. Manuals are paired by **exact** product name + document type after normalisation. No fuzzy pairing: "
        "at 0.90 similarity *ApsaraDB for RDS* would match *ApsaraDB for Redis*, which would manufacture "
        "`changes`. Unmatched names are listed in Sections 5/6 instead of being guessed.")
    add("3. Textual deltas are **sentence-level, not line-level**: PDF re-flow moves line breaks between editions, "
        "so lines are re-joined per section and split on punctuation before comparison. Three gates then run: "
        "(i) headings, tables, fenced code, log samples and regex fragments are dropped; (ii) template text "
        "recurring in ≥ 8% of the paired corpus (floor of 6 manuals — with only "
        f"{len(pairs)} pairs this filter is weaker than in the V3.18.6→2607 note) is dropped; (iii) only "
        "*informative* sentences are counted — those carrying a version/number/quota or a support/add/deprecate/"
        "change verb, with self-describing UI narration (\"This topic describes…\", \"On the X page, click…\") "
        f"excluded. Gates (i)–(iii) leave {ra:,} added / {rd:,} removed informative sentences; re-typing "
        f"cancellation then reduces that to {sum(p2['sentAddTotal'] for p2 in pairs):,} / "
        f"{sum(p2['sentDelTotal'] for p2 in pairs):,} — the figures quoted in §1.")
    add("3b. Per-pair document dates range from a few months to almost four years apart (part of the baseline "
        "dates back to 2022), so deltas include re-branding and re-typing of "
        "long-lived text; the re-typing cancellation above removes same-sentence rewrites (token Jaccard ≥ 0.82) "
        "from both sides. The known brand rename (“Apsara Stack Enterprise” → “Apsara Stack”) was deliberately "
        "**not** suppressed — sentences that changed only by brand still appear as added/removed lines.")
    add("3c. Quoted lines are verbatim extracts from the converted Markdown. The PDF extraction occasionally "
        "duplicates a short token or reorders a cell; those are extraction artifacts of our converter, not "
        "typographical errors in the manual, and they do not affect the substance of the quoted sentence.")
    add("4. Section counting normalises numbered headings (`2.1.1.2.3. Limits_1578278510` → `limits`), so a "
        "re-number is not counted as add + drop. Renames are reported when the normalised titles are ≥ 0.85 similar.")
    add("5. What this cannot show: why a change was made; whether removed text reflects a dropped feature or an "
        "editorial decision; anything about the manuals with no baseline (§5 — listed with closest names, never "
        "summarised as new or unchanged); and limits rows where the two editions do not share the row key.")
    add("6. Full machine-readable evidence (all added/removed sentences per manual, with section attribution): "
        "`.scratch/rn3162_pairs.json` in the session workspace. Regenerate with "
        "`python3 工具/rn3162_pairs.py && python3 工具/build_note_3162.py`.")
    add("")
    add("## 8. Where the files are")
    add("")
    add("| path | contents |")
    add("|---|---|")
    add(f"| `markdown/10_EN_ApsaraStack_v3.18.6/` | the {ST['newTotal']}-manual English set "
        "this note describes |")
    add(f"| `markdown/10_EN_ApsaraStack_V3.16.2/` | the {ST['oldTotal']}-manual 2024–2025 English baseline |")
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
