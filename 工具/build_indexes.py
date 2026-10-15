"""Rebuild the human-facing indexes from 文档缓存索引.json (single source of truth).

Outputs refreshed counts for: markdown/README.md (per-manual link list), 全量文档清单.html
(filterable overview), and keeps inScope truthful (a manual that now has Markdown is in scope).
Run after any fetch/convert batch.
"""
import html as H
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cache  # noqa: E402

ROOT = os.path.dirname(HERE)
os.chdir(ROOT)
ZHL = {"zh": "中文", "en": "English"}

rows = json.load(open("文档缓存索引.json", encoding="utf-8"))
fixed = 0
for r in rows:
    if r.get("markdown") and not r.get("inScope"):
        r["inScope"] = True           # 已转换 = 在口径内，别让下次误判为范围外
        fixed += 1
cache.save(ROOT, rows)

have = [r for r in rows if r.get("markdown") and os.path.exists(r["markdown"])]
missing = [r for r in rows if r.get("markdown") and not os.path.exists(r["markdown"])]
byver = {}
for r in have:
    byver[(r["lang"], r["version"])] = byver.get((r["lang"], r["version"]), 0) + 1

L = ["# 阿里专有云 Apsara Stack · Markdown 文档索引", "",
     f"共 **{len(have)} 份纯文本 Markdown**（无插图；部首字形/页脚/正文空格均已归一）。"
     f"生成：{time.strftime('%Y-%m-%d %H:%M %Z')}。"
     + (f" 索引登记但文件缺失 {len(missing)} 条。" if missing else ""),
     "", "| 语言 | 版本 | 份数 |", "|---|---|---|"]
for (lg, v), n in sorted(byver.items()):
    L.append(f"| {ZHL[lg]} | {v} | {n} |")
L += ["", "| 语言 | 服务域/类型 | 产品 | 手册 | 源页数 | 版本戳 | Markdown |", "|---|---|---|---|---|---|---|"]
for r in sorted(have, key=lambda x: (x["lang"], str(x["product"]).lower(), str(x.get("docType")))):
    grp = r["category"] if r["lang"] == "zh" else (r.get("docType") or "")
    lab = (r.get("label") or r.get("docType") or "")[:48].replace("|", "\\|")
    link = r["markdown"]
    wrap = f"<{link}>" if re.search(r"[()]", link) else link
    L.append(f"| {ZHL[r['lang']]} | {grp} | {r['product']} | {lab} | {r.get('pages') or ''} | "
             f"{r.get('versionStamp') or ''} | [{os.path.basename(link)[:34]}]({wrap}) |")
open("markdown/README.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

tr = []
for r in have:
    q = H.escape(" ".join([ZHL[r["lang"]], str(r["product"]), str(r.get("label")), str(r.get("docType")),
                           str(r["version"])]).lower())
    where = "本地(已删, 云端可取)" if not r.get("pdfLocal") else "本地"
    tr.append(f'<tr data-q="{q}" data-l="{ZHL[r["lang"]]}"><td>{ZHL[r["lang"]]}</td>'
              f'<td>{H.escape(str(r["product"]))}</td>'
              f'<td>{H.escape(str(r["category"] if r["lang"] == "zh" else (r.get("docType") or "")))}</td>'
              f'<td>{H.escape(str(r.get("label") or "")[:70])}</td><td class=n>{r.get("pages") or ""}</td>'
              f'<td>{H.escape(str(r.get("versionStamp") or ""))}</td><td class=no>{where}</td>'
              f'<td><a href="{H.escape(r["markdown"])}">{os.path.basename(r["markdown"])[:32]}</a></td></tr>')
mb = sum(os.path.getsize(r["markdown"]) for r in have) / 1048576
stat = "".join(f'<div><b>{n}</b><span>{ZHL[l]} {v}</span></div>' for (l, v), n in sorted(byver.items()))
page = f"""<!DOCTYPE html><html lang=zh-CN><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>专有云文档交付总览（Markdown）</title>
<style>*{{box-sizing:border-box}}body{{margin:0;font:14px/1.6 -apple-system,"Segoe UI","PingFang SC",sans-serif;background:#f6f7f8;color:#17191c}}
.wrap{{max-width:1380px;margin:0 auto;padding:22px}}h1{{font-size:22px;margin:0 0 6px}}.sub{{color:#66707a;font-size:13px;margin:0 0 14px}}
.stat{{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:14px}}.stat div{{background:#fff;border:1px solid #e3e6ea;border-radius:6px;padding:9px 14px}}
.stat b{{display:block;font-size:18px}}.stat span{{color:#66707a;font-size:12px}}
.bar{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px}}input,select{{padding:8px 10px;border:1px solid #e3e6ea;border-radius:5px;font:inherit;background:#fff}}
input{{flex:1;min-width:250px}}.card{{background:#fff;border:1px solid #e3e6ea;border-radius:7px;overflow:auto;max-height:80vh}}
table{{border-collapse:collapse;width:100%;font-size:13px}}th{{position:sticky;top:0;background:#fbfbfc;text-align:left;padding:9px;border-bottom:1px solid #e3e6ea;white-space:nowrap;z-index:2}}
td{{padding:8px 9px;border-bottom:1px solid #eef0f2}}tr:hover td{{background:#fcf7f4}}.n{{text-align:right}}
a{{color:#c8500f}}.no{{color:#8a939b}}#cnt{{margin-left:auto;color:#66707a;font-size:12px}}
footer{{color:#66707a;font-size:12px;margin-top:14px;line-height:1.8}}</style></head><body><div class=wrap>
<h1>阿里专有云（Apsara Stack）交付总览 · 仅 Markdown</h1>
<p class=sub>中文 v3.18.6-SP2607（册内文档版本 20260729–20260818）· English V3.18.6 与 V3.16.2（用于 release note 对比）· AI Stack V2.17.0。
全部为<b>纯文本无插图</b>；PDF 不保留在本地（云端 <code>apsara-docs/zips*</code> 与逐册 url 可取）。</p>
<div class=stat><div><b>{len(have)}</b><span>Markdown 总份数</span></div>{stat}
<div><b>{mb:.0f} MB</b><span>合计体积</span></div><div><b>{sum(1 for r in rows if r.get('pdfLocal'))}</b><span>PDF 本地在位</span></div></div>
<div class=bar><input id=q placeholder="搜索 产品 / 手册 / 类型 / 版本，如 ECS、用户指南、V3.16.2">
<select id=fl><option value="">全部语言</option><option>中文</option><option>English</option></select>
<span id=cnt></span></div>
<div class=card><table><thead><tr><th>语言</th><th>产品</th><th>服务域/类型</th><th>手册</th><th class=n>源页数</th>
<th>版本戳</th><th>PDF</th><th>Markdown</th></tr></thead><tbody id=tb>{''.join(tr)}</tbody></table></div>
<footer>判重：读 <code>文档缓存索引.csv</code> 的 <code>id@versionStamp</code> + <code>markdownSha256</code>，已转 Markdown 的册子不再下载。
Release note：<code>ApsaraStack-3.18.6-Release-Note-EN.md</code>（工具 <code>工具/release_note.py</code> → <code>工具/build_note.py</code>）。</footer></div>
<script>const q=document.getElementById('q'),fl=document.getElementById('fl'),cnt=document.getElementById('cnt'),
rs=[...document.querySelectorAll('#tb tr')];
function f(){{const s=q.value.trim().toLowerCase(),a=fl.value;let k=0;
rs.forEach(r=>{{const ok=(!s||r.dataset.q.includes(s))&&(!a||r.dataset.l===a);r.hidden=!ok;k+=ok?1:0}});
cnt.textContent=k+' / '+rs.length;}} q.oninput=f;fl.onchange=f;f();</script></body></html>"""
open("全量文档清单.html", "w", encoding="utf-8").write(page)
bad_link = [l for l in re.findall(r'<a href="([^"]+\.md)"', page) if not os.path.exists(H.unescape(l))]
print(f"inScope 修正 {fixed} 条 | 索引 {len(have)} 份（缺失登记 {len(missing)}）| {mb:.0f} MB")
print("各语言/版本:", byver)
print("HTML 链接失效:", len(bad_link))
