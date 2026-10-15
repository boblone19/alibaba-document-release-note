"""Render the English 3.18.6 release note from /tmp/release_note_evidence.json.

Every bullet comes from a recorded evidence field (official release-notes section text,
a heading present in 3.18.6 but not in the 3.16.2 counterpart, or a limit/quota row that
differs), with the source manual cited. Coverage and non-comparability are stated explicitly.
"""
import json
import os
import time
from collections import defaultdict

ROOT = "/workspace/b845c37e-09f5-4e58-9113-3e8ea10d12f0/work/output/apsara-stack-docs"
os.chdir(ROOT)
EV = json.load(open("/tmp/release_note_evidence.json", encoding="utf-8"))
OUT_MD = "ApsaraStack-3.18.6-Release-Note-EN.md"
CAT_ORDER = ["专有云云平台", "统一运营平台", "统一云管平台", "计算服务", "存储服务", "网络服务", "数据库服务",
             "大数据服务", "云原生服务", "安全服务", "应用服务", "监控与运维", "人工智能", "交付服务", "其他", "-"]
CAT_EN = {"专有云云平台": "Platform & Foundations", "统一运营平台": "Unified Management (Apsara Uni-manager)",
          "统一云管平台": "Unified Management (Apsara Uni-manager)", "计算服务": "Computing",
          "存储服务": "Storage", "网络服务": "Networking", "数据库服务": "Databases",
          "大数据服务": "Big Data & Analytics", "云原生服务": "Cloud Native & Middleware",
          "安全服务": "Security", "应用服务": "Application Services", "监控与运维": "Observability & O&M",
          "人工智能": "AI / LLM Platform", "交付服务": "Delivery & Deployment", "其他": "Other", "-": "Uncategorised"}
DOCT_SHORT = {"User Guide": "User Guide", "Developer Guide": "Developer Guide",
              "Product Introduction": "Product Introduction",
              "Operations and Maintenance Guide": "O&M Guide", "Operations Guide": "Operations Guide",
              "Introduction to Instance Families and Instance Types": "Instance Families Guide"}


def cite(p):
    return f"`{os.path.basename(p)}`"


def main():
    pairs = EV["pairs"]
    only18 = EV["only18"]
    byc = defaultdict(list)
    for e in pairs:
        byc[e["cat"] or "-"].append(e)
    cats = [c for c in CAT_ORDER if c in byc] + sorted(set(byc) - set(CAT_ORDER))

    L = []
    add = L.append
    add("# Alibaba Cloud Apsara Stack V3.18.6 — Release Note (English corpus)")
    add("")
    add(f"_Compiled {time.strftime('%Y-%m-%d %H:%M UTC+8')} from the official English documentation set "
        f"(Apsara Stack V3.18.6) compared against the V3.16.2 English set._")
    add("")
    add("## 1. What this document is")
    add("")
    add("Alibaba Cloud does not publish a cross-version change matrix. This note is therefore an")
    add("**evidence-based diff** built only from the two English manual sets, and each item states which")
    add("manual it came from. Three kinds of evidence are used:")
    add("")
    add("1. **Release-notes sections written by the product team** — quoted where present in V3.18.6.")
    add("2. **Document structure deltas** — section titles appearing in the V3.18.6 manual that are not")
    add("   found (by name) in its V3.16.2 counterpart. These mark *newly documented or re-titled*")
    add("   material — a rename cannot be told apart from a new section by title alone, so treat them")
    add("   as pointers to verify, not as confirmed feature additions.")
    add("3. **Limits / quota deltas** — rows in a limits table whose value differs from V3.16.2.")
    add("")
    c = EV["counts"]
    add("Nothing in this note is inferred from marketing pages, release blogs or my own assumptions.")
    add("")
    add("## 2. Coverage")
    add("")
    add("| item | count |")
    add("|---|---|")
    add(f"| V3.18.6 English manuals in the compared corpus | {sum(1 for r in json.load(open('文档缓存索引.json', encoding='utf-8')) if r['lang']=='en' and r['version']=='V3.18.6' and r['markdown'])} |")
    add(f"| V3.16.2 English manuals available for comparison | {c['v16_total']} |")
    add(f"| Product × manual-type pairs successfully aligned | {c['pairs']} |")
    add(f"| V3.18.6 manuals with **no** V3.16.2 counterpart (delta not computable) | {c['only18']} |")
    add(f"| Pairs with at least one observed delta | {sum(1 for e in pairs if e['new_sections'] or e['limits'] or e['release_notes_18'])} |")
    add("")
    add("> The V3.16.2 English set (53 manuals, 30 products, User/Developer Guides only) is far smaller,")
    add("> contains **no** Product Introduction or O&M volumes, so a")
    add("> large part of V3.18.6 cannot be diffed. Those manuals are listed in §4 as *not comparable* —")
    add("> absence of a diff is **not** evidence that the product is unchanged.")
    add("")
    add("## 3. Highlights, ranked by measurable document growth")
    add("")
    add("Ranking is objective: growth in documented pages/sections between the two English manual")
    add("versions, plus whether the manual carries its own release-notes section. It is a proxy for")
    add("documentation change, **not** a judgement of customer impact.")
    add("")
    add("| rank | product | manual | Δ pages | Δ sections | new/absent section titles | official release notes | limits deltas |")
    add("|---|---|---|---|---|---|---|---|")
    def metrics(e):
        a, b = e["18"], e["16"]
        dp = (a["pages"] or 0) - (b["pages"] or 0)
        ds = (a["heads"] or 0) - (b["heads"] or 0)
        return dp, ds
    rk = sorted(pairs, key=lambda e: (-(metrics(e)[0]), -len(e["new_sections"])))
    for i, e in enumerate(rk[:15], 1):
        dp, ds = metrics(e)
        add(f"| {i} | {e['product']} | {DOCT_SHORT.get(e.get('docType') or '', e.get('docType') or '')} | "
            f"{dp:+d} ({e['16']['pages'] or '?'} → {e['18']['pages'] or '?'}) | {ds:+d} | {e.get('new_sections_total', len(e['new_sections']))} | "
            f"{'yes' if e['release_notes_18'] else '—'} | {len(e['limits'])} |")
    add("")
    add(f"Full detail for all {len(pairs)} comparable pairs follows. Only "
        f"{sum(1 for e in pairs if e['release_notes_18'])} of them contain a release-notes section written by the "
        f"product team; {sum(1 for e in pairs if e['limits'])} show limits/quota deltas.")
    add("")
    add("## 3. Changes observed, by service domain")
    add("")
    for cat in cats:
        items = byc[cat]
        with_delta = [e for e in items if e["new_sections"] or e["limits"] or e["release_notes_18"]]
        add(f"### {CAT_EN.get(cat, cat)}")
        add("")
        if not with_delta:
            add(f"_{len(items)} compared manual pair(s), no structural or limits delta detected._")
            add("")
            continue
        for e in sorted(with_delta, key=lambda x: str(x["product"]).lower()):
            dt = DOCT_SHORT.get(e.get("docType") or "", e.get("docType") or "")
            add(f"#### {e['product']}" + (f" — {dt}" if dt else ""))
            add("")
            v18, v16 = e["18"], e["16"]
            add(f"- Compared: V3.18.6 ({v18['pages'] or '?'} pp, doc version {v18['ver']}, "
                f"{v18['heads']} sections) vs V3.16.2 ({v16['pages'] or '?'} pp, doc version {v16['ver']}, "
                f"{v16['heads']} sections)" + (f" — matched by name similarity {e['matched'][9:]}" if e["matched"].startswith("rename") else ""))
            if e["release_notes_18"]:
                add("- **Stated by the manual itself:**")
                for head, body in e["release_notes_18"]:
                    add(f"  - *{head}*: {body[:400].replace(chr(10), ' ')}")
            if e["new_sections"]:
                add("- **Section titles absent from the V3.16.2 counterpart** (new or re-titled — verify before quoting):")
                for t in e["new_sections"]:
                    add(f"  - {t}")
                tot = e.get("new_sections_total", len(e["new_sections"]))
                if tot > len(e["new_sections"]):
                    add(f"  _showing {len(e['new_sections'])} of {tot} titles; the rest are in the evidence file_")
            if e["limits"]:
                add("- **Limits / quota rows that differ** (wording changes can also appear here):")
                for kind, where, txt in e["limits"][:8]:
                    add(f"  - [{kind}] {' in ' + where if where else ''}: {txt[:220]}")
            if e["dropped_sections"]:
                add("- **Sections no longer present in V3.18.6:** " + "; ".join(e["dropped_sections"][:6]))
            add(f"- Source: {cite(v18['file'])} ↔ {cite(v16['file'])}")
            add("")
    add("## 4. Manuals without a V3.16.2 counterpart (delta not computable)")
    add("")
    add("| service domain | product | manual | pages |")
    add("|---|---|---|---|")
    for x in sorted(only18, key=lambda y: (str(y["cat"]), str(y["product"]))):
        add(f"| {CAT_EN.get(x['cat'], x['cat'])} | {x['product']} | {DOCT_SHORT.get(x['docType'], x['docType'])} "
            f"| {x['pages'] or ''} |")
    add("")
    add("## 5. Method, limits of this note, and reproducibility")
    add("")
    add("- Corpus: text-only Markdown converted from the official English PDFs on the international "
        "Apsara Stack documentation page; each file's front matter keeps `product_version`, "
        "`doc_version`, `pdf_pages` and the source URL, so any statement here is traceable to a PDF.")
    add("- Pairing: exact match on (normalised product name, manual type), then fuzzy match "
        "(similarity > 0.86) for renamed products — those rows are labelled.")
    add("- Not covered: features documented only in Chinese manuals, and any manual that has no "
        "V3.16.2 English counterpart (§4). Version numbering in the EN corpus is `V3.16.2` vs "
        "`V3.18.6`; the Chinese corpus names the same line `v3.18.6-SP26xx`, which is a service-pack "
        "granularity this note does not attempt.")
    add("- Regenerate: `python3 工具/release_note.py` then `python3 工具/build_note.py`.")
    add("")
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"{OUT_MD}: {os.path.getsize(OUT_MD)/1024:.0f} KB | 段落 {len(L)} 行 | "
          f"含 delta 的产品条目 {sum(1 for e in pairs if e['new_sections'] or e['limits'] or e['release_notes_18'])}")


if __name__ == "__main__":
    main()
