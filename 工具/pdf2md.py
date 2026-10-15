"""PDF -> text-only Markdown for Apsara Stack manuals (rebuilt, PyMuPDF line classifier).

Design (all of these were learned the hard way on this corpus — don't regress):
  * normalize glyphs FIRST: Kangxi radicals U+2F00-U+2FD5 via NFKC, CJK Radicals Supplement
    (⻄⺠⻘⻁…) via explicit table, else filters below miss them and 页脚/部首 leak into output
  * code  = lines whose Courier-family chars are >=85% of the line  → fenced block, language guess
  * table = page.find_tables(); tables and text lines are merged into ONE stream sorted by y,
            otherwise whole-page tables jump ahead of the section they belong to
  * heading = numbering depth ("1.2.3" → ###) with font size >= 13.5pt, or a PDF-outline title;
              the number is KEPT in the output ("### 1.2.3 Title"), it is the manual's own编号
  * TOC     = a `## Table of Contents` rebuilt from the PDF outline is emitted right after the H1;
              when the PDF has no outline, fall back to the headings collected during conversion
  * junk    = running headers ("X·Y"), 文档版本/Document Version footers, bare page numbers/romans,
              cover + legal + conventions + TOC pages (front matter cut at the first bookmark page)
  * prose   = hard-wrapped lines re-joined; no space between two Han characters (CJK glue)
  * no images are extracted (per requirement: text only)
"""
import os
import re
import unicodedata as _ud

CODE_F = ("courier", "consolas", "monaco", "menlo", "mono")
HEAD_MIN_PT = 13.5
HEAD_NUM = re.compile(r"^\s*(\d+(?:\.\d+)*)(?:[.)](?!\d))?[ \t]*(?=[A-Za-z\u4e00-\u9fff])")
BULLET = re.compile(r"^\s*[•·●○‣◦\-\u2013]\s+")
NUMITEM = re.compile(r"^\s*\(?(\d{1,2})[.)]\s+")
CSIMPL = {"SEE": "见", "HORN": "角", "SPEECH": "讠", "SHELL": "贝", "CART": "车", "WALK": "辶",
          "GOLD": "钅", "LONG": "长", "GATE": "门", "TANNED LEATHER": "革", "LEAF": "页",
          "WIND": "风", "FLY": "飞", "EAT": "饣", "HORSE": "马", "FISH": "鱼", "BIRD": "鸟",
          "SALT": "卤", "WHEAT": "麦", "YELLOW": "黄", "FROG": "黾", "EVEN": "齐", "TOOTH": "齿",
          "DRAGON": "龙", "TURTLE": "龟", "SILK": "纟", "TIGER": "虎", "WEST": "西", "BLUE": "青",
          "MOTHER": "母"}
EXPL = {"\u2ec4": "西", "\u2ea0": "民", "\u2ed8": "青", "\u2ec1": "虎", "\u2edd": "食", "\u2ec2": "己",
        "\u2ee9": "黄", "\u2ee8": "麦", "\u2eda": "页", "\u2ec5": "见", "\u2ed3": "长", "\u2edb": "风",
        "\u2ee2": "马", "\u2ee5": "鱼", "\u2ee6": "鸟", "\u2ef3": "龟", "\u2ef0": "龙", "\u2eec": "齐",
        "\u2eee": "齿", "\u2ea6": "丨", "\u2eb0": "纟", "\u2ec6": "角", "\u2ec8": "讠", "\u2ec9": "贝",
        "\u2ecb": "车", "\u2ecc": "辶", "\u2ed0": "钅", "\u2ed4": "门", "\u2ed9": "革", "\u2ee0": "饣",
        "\u2ee7": "卤", "\u2eea": "黾", "\u2e9f": "母"}
_TBL = dict(EXPL)
for _cp in range(0x2E80, 0x2F00):
    _c = chr(_cp)
    if _c in _TBL:
        continue
    try:
        _nm = _ud.name(_c)
    except ValueError:
        continue
    m = re.search(r"(?:C-)?SIMPLIFIED (.+)$", _nm)
    if m and m.group(1) in CSIMPL:
        _TBL[_c] = CSIMPL[m.group(1)]
RAD = re.compile(r"[\u2e80-\u2fdf]")
CJK = "\u4e00-\u9fff\u3400-\u4dbf"
CJKSP = re.compile(rf"(?<=[{CJK}]) (?=[{CJK}])")
PAGEJUNK = re.compile(r"^\s*>?\s*(?:Document Version|文档版本|产品版本|文件版本)\s*[:：].*$"
                      r"|^\s*[-–—]?\s*\d{1,4}\s*[-–—]?$|^\s*[IVXLC]{1,7}\s*$")
BOILER = re.compile(r"considered confidential|reminds you to carefully read|shall not be excerpted|"
                    r"total acceptance|保密信息|事先书面许可", re.I)
FRONT = re.compile(r"^\**\s*(Legal disclaimer|Document conventions|Table of Contents|目录|前言|警告"
                   r"|Warning|Caution)\s*\**$", re.I)
LANGS = [(r"^\s*(?:import|package|public class|private |protected |@Override|System\.out|throws )", "java"),
         (r"^\s*[{\[]\s*[\"']|^\s*[\"']\w+[\"']\s*:", "json"),
         (r"^\s*<\?xml|^\s*<[a-zA-Z][\w:-]*>", "xml"),
         (r"^\s*(?:def |elif |print\(|from \w+ import |sudo )", "python"),
         (r"^\s*(?:\$ |# |curl |kubectl |docker |systemctl |yum |apt )", "bash")]


def normalize(text):
    """Kangxi/radical glyphs → real Han chars."""
    def rep(m):
        c = m.group(0)
        if c in _TBL:
            return _TBL[c]
        if 0x2F00 <= ord(c) <= 0x2FD5:
            nf = _ud.normalize("NFKC", c)
            if nf != c and len(nf) == 1:
                return nf
        return c
    return RAD.sub(rep, text)


def _is_code(spans):
    tot = mono = 0
    for s in spans:
        t = (s.get("text") or "").strip()
        tot += len(t)
        if any(k in (s["font"] or "").lower() for k in CODE_F):
            mono += len(t)
    return tot >= 3 and mono / tot >= 0.85


def _bold(spans):
    return bool(spans) and all((s.get("flags", 0) & 16) or "bold" in (s["font"] or "").lower() for s in spans)


def _lang(body):
    for pat, lg in LANGS:
        if re.search(pat, body, re.M):
            return lg
    return ""


def _cell(c):
    s = normalize(re.sub(r"\s+", " ", str(c or "")).replace("|", "\\|").strip())
    prev = None
    while prev != s:
        prev, s = s, CJKSP.sub("", s)
    return s


def _table_md(tab):
    try:
        rows = [r for r in tab.extract() if r and any(str(c or "").strip() for c in r)]
    except Exception:
        return ""
    if not rows:
        return ""
    w = max(len(r) for r in rows)
    out = []
    for i, r in enumerate(rows):
        cells = [(_cell(c) or " ") for c in (list(r) + [None] * (w - len(r)))][:w]
        out.append("| " + " | ".join(cells) + " |")
        if i == 0:
            out.append("|" + "---|" * w)
    return "\n".join(out)


def _inline(spans):
    buf = []
    for s in spans:
        t = s.get("text") or ""
        core = t.strip()
        if not core:
            buf.append(t)
            continue
        pre, post = t[:len(t) - len(t.lstrip())], t[len(t.rstrip()):]
        low = (s["font"] or "").lower()
        bold = (s.get("flags", 0) & 16) or "bold" in low
        if any(k in low for k in CODE_F) and len(core) <= 90 and \
                re.fullmatch(r"[A-Za-z0-9_./:\-\[\](){}'\"@#+*&<>=, ]+", core):
            buf.append(f"{pre}`{core}`{post}")
        elif bold and len(core) <= 90 and "*" not in core and "`" not in core:
            buf.append(f"{pre}**{core}**{post}")
        else:
            buf.append(t)
    return re.sub(r"[ \t]{2,}", " ", "".join(buf)).strip()


def _para_join(md):
    lines, buf, out = md.split("\n"), [], []

    def flush():
        if not buf:
            return
        t = buf[0]
        for nxt in buf[1:]:
            if t.endswith("-") and nxt[:1].isascii() and nxt[:1].islower():
                t = t[:-1] + nxt
            elif re.search(rf"[{CJK}]$", t) and re.match(rf"[{CJK}]", nxt):
                t = t + nxt
            else:
                t = t + " " + nxt
        out.append(re.sub(r"\s{2,}", " ", t).strip())
        buf.clear()

    for l in lines:
        st = l.strip()
        if not st:
            flush()
            out.append("")
        elif st.startswith(("#", "|", "```", "- ", "* ", "> ", "**")) or re.match(r"^\d{1,2}[.)]\s", st) \
                or BULLET.match(st) or (len(l) - len(l.lstrip())) > 0:
            flush()
            out.append(l.rstrip())
        else:
            buf.append(st)
    flush()
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


class Manual:
    def __init__(self, path):
        import pymupdf
        self.pymupdf, self.path = pymupdf, path
        self.pdf = pymupdf.open(path)
        self.toc = [(l, normalize(t), pg) for l, t, pg in (self.pdf.get_toc() or [])]
        self.toc_lvl = {}
        self.toc_by_num = {}         # 编号 → 书签全标题：页面上被折行的标题用书签补全
        for lvl, t, _pg in self.toc:
            k = re.sub(r"\s+", " ", re.sub(HEAD_NUM, "", t).replace("·", " ")).strip().lower()
            if re.search(r"[A-Za-z\u4e00-\u9fff]{3}", k):
                self.toc_lvl.setdefault(k, lvl)
            m2 = HEAD_NUM.match(t)
            if m2:
                num, full = m2.group(1), re.sub(r"\s+", " ", t[m2.end():]).strip()
                if num not in self.toc_by_num or len(full) > len(self.toc_by_num[num]):
                    self.toc_by_num[num] = full
        self.start = max(0, min((p for _l, _t, p in self.toc if p > 1), default=1) - 1)
        self.out, self.code = [], []
        self.collected = []          # (level, text) of emitted headings，无书签时的目录兜底
        self.unreadable = set(p for _l, t, p in self.toc if re.fullmatch(r"[\d.\s?？·_—-]*", t or " "))

    def blank(self):
        if self.out and self.out[-1] != "":
            self.out.append("")

    def toc_markdown(self):
        """目录：直接取 PDF 书签（标题自带编号），层级缩进。无书签返回空串。"""
        if not self.toc:
            return ""
        lines, seen = [], set()
        for lvl, t, _pg in self.toc:
            title = re.sub(r"\s+", " ", t.replace("·", " ")).strip().strip("-").strip()
            if not re.search(r"[A-Za-z\u4e00-\u9fff]{3}", title):
                continue                       # 纯点线/纯数字的坏书签
            m = HEAD_NUM.match(title)
            if m:
                title = (m.group(1) + " " + re.sub(r"\s+", " ", title[m.end():]).strip()).strip()
            title = title.replace("|", "\\|")
            k = (lvl, title.lower())
            if k in seen:
                continue
            seen.add(k)
            lines.append("  " * min(5, max(0, lvl - 1)) + "- " + title)
        return "\n".join(lines)

    def fallback_toc(self):
        """PDF 无书签时，用转换过程中收集到的带编号标题拼一个目录。"""
        lines, seen = [], set()
        for lvl, title in self.collected:
            k = (lvl, title.lower())
            if k in seen:
                continue
            seen.add(k)
            lines.append("  " * min(5, max(0, lvl - 2)) + "- " + title.replace("|", "\\|"))
        return "\n".join(lines)

    def flush(self):
        if not self.code:
            return
        body = "\n".join(self.code).strip("\n")
        self.code = []
        if body:
            self.blank()
            self.out += [f"```{_lang(body)}", body, "```", ""]

    def junk(self, txt, raw, flagged, size=99.0):
        if PAGEJUNK.match(raw.strip()) or BOILER.search(txt):
            return True
        # 小字号的章名/编号行：页眉碎片或目录页残留（真标题 >= 13.5pt，不会被误杀）
        if size < 12.5:
            k = re.sub(r"\s+", " ", re.sub(HEAD_NUM, "", txt)).strip().lower()
            if k and len(k) <= 60 and k in self.toc_lvl:
                return True
        if flagged or FRONT.match(txt):
            return False
        if "·" in txt and not raw.strip().startswith(("·", "•")):
            return True
        # 页眉的正确判据：跨页重复出现（真页眉每页都有，正文断行不会）
        key = re.sub(r"\s+", " ", txt).strip().lower()
        if len(key) <= 60 and self.frequent.get(key, 0) >= self.freq_min:
            return True
        return False

    def scan_frequency(self):
        """Pass 1: count on how many distinct pages each normalized line appears."""
        seen = {}
        for pno in range(self.start, self.pdf.page_count):
            d = self.pdf[pno].get_text("dict", sort=True)
            for blk in d.get("blocks", []):
                if blk.get("type") != 0:
                    continue
                for ln in blk.get("lines", []):
                    spans = [sp for sp in ln.get("spans", []) if (sp.get("text") or "").strip()]
                    if not spans:
                        continue
                    t = normalize("".join(sp["text"] for sp in spans)).strip()
                    if t:
                        k = re.sub(r"\s+", " ", t).lower()
                        s2 = seen.setdefault(k, set())
                        s2.add(pno)
        self.frequent = {k: len(v) for k, v in seen.items()}
        n = max(1, self.pdf.page_count - self.start)
        self.freq_min = max(4, int(n * 0.35))

    @property
    def base(self):
        return re.sub(r"^Alibaba Cloud Apsara Stack V[\d.]+\s*", "", os.path.basename(self.path)[:-4])

    def run(self, title=""):
        pymupdf = self.pymupdf
        self.scan_frequency()
        for pno in range(self.start, self.pdf.page_count):
            page = self.pdf[pno]
            items, rects = [], []
            try:
                tabs = page.find_tables()
            except Exception:
                tabs = None
            for t in (tabs.tables if tabs else []):
                if t.row_count and t.col_count:
                    r = pymupdf.Rect(t.bbox)
                    rects.append(r)
                    md = _table_md(t)
                    if md:
                        items.append((round(r.y0, 1), len(items), "T", md))
            d = page.get_text("dict", sort=True)
            bi = 0
            for blk in d.get("blocks", []):
                bi += 1
                if blk.get("type") != 0:
                    continue
                for li, ln in enumerate(blk.get("lines", [])):
                    spans = [sp for sp in ln.get("spans", []) if (sp.get("text") or "").strip()]
                    if not spans:
                        continue
                    box = pymupdf.Rect(ln["bbox"])
                    midx, midy = (box.x0 + box.x1) / 2, (box.y0 + box.y1) / 2
                    if any(r.contains((midx, midy)) for r in rects):
                        continue        # 只把行中心真正落在表格框内的行当作表格内容，避免吃掉贴边正文
                    raw = normalize("".join(sp["text"] for sp in spans))
                    if raw.strip():
                        items.append((round(box.y0, 1), bi * 10000 + li, "L", (raw, spans, box.x0)))
            for _y, _o, kind, payload in sorted(items, key=lambda x: (x[0], x[1])):
                if kind == "T":
                    self.flush()
                    self.blank()
                    self.out += [payload, ""]
                    continue
                raw, spans, x0 = payload
                txt = raw.strip()
                size = max(round(sp.get("size", 0) or 0, 1) for sp in spans)
                flagged = size >= HEAD_MIN_PT or bool(HEAD_NUM.match(raw))
                if self.junk(txt, raw, flagged, size):
                    continue
                if _is_code(spans):
                    self.code.append(raw.rstrip())
                    continue
                self.flush()
                m = HEAD_NUM.match(raw)
                if m and size >= HEAD_MIN_PT and len(txt) < 170:
                    lvl = min(6, m.group(1).count(".") + 2)
                    title = re.sub(r"\s+", " ", raw[m.end():]).strip()
                    full = self.toc_by_num.get(m.group(1))
                    if full and full.lower().startswith(title.lower().rstrip()) and len(full) > len(title):
                        title = full          # 页面标题折行被截断 → 用书签全标题补全
                    text = f"{m.group(1)} {title}".strip()
                    self.blank()
                    self.out.append("#" * lvl + " " + text)
                    self.out.append("")
                    self.collected.append((lvl, text))
                    continue
                key = re.sub(r"\s+", " ", txt).strip().lower()
                if size >= HEAD_MIN_PT and key in self.toc_lvl and len(txt) < 130:
                    lvl = min(6, 1 + self.toc_lvl[key])
                    title = re.sub(r"\s+", " ", txt)
                    self.blank()
                    self.out.append("#" * lvl + " " + title)
                    self.out.append("")
                    self.collected.append((lvl, title))
                    continue
                if BULLET.match(raw):
                    self.out.append("  " * max(0, int((x0 - 40) // 20)) + "- "
                                    + re.sub(BULLET, "", _inline(spans)).strip())
                    continue
                ni = NUMITEM.match(raw)
                if ni and len(txt) < 400:
                    self.out.append(f"{ni.group(1)}. " + _inline(spans)[ni.end():].strip())
                    continue
                if _bold(spans) and len(txt) < 120:
                    self.blank()
                    self.out += [f"**{re.sub(r'[*`]', '', txt).strip()}**", ""]
                    continue
                self.out.append(_inline(spans))
            self.flush()
        md = normalize(_para_join("\n".join(self.out)))
        prev = None
        while prev != md:
            prev = md
            md = CJKSP.sub("", md)
        return md

def convert(pdf, outpath, url="", title="", prodver="", docver=""):
    m = Manual(pdf)
    body = m.run()
    pages = m.pdf.page_count
    if len(body) < 400 and pages > 4:
        return None, "输出过短（疑似图片型/扫描版 PDF）"
    toc = m.toc_markdown() or m.fallback_toc()
    name = re.sub(r"\s+", " ", (title or m.base)).strip()
    os.makedirs(os.path.dirname(outpath) or ".", exist_ok=True)
    head = (f'---\ntitle: "{name}"\n'
            + (f'product_version: "{prodver}"\n' if prodver else '')
            + (f'doc_version: "{docver}"\n' if docver else '')
            + f'pdf_pages: {pages}\n'
            + (f'source_pdf: "{os.path.basename(pdf)}"\n')
            + (f'source_url: "{url}"\n' if url else "")
            + 'converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)\n---\n\n')
    open(outpath, "w", encoding="utf-8").write(
        head + f"# {name}\n\n"
        + (("## Table of Contents\n\n" + toc + "\n\n") if toc else "")
        + body.strip() + "\n")
    return len(body), None   # 正文体量，供缓存登记


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--url", default="")
    ap.add_argument("--title", default="")
    ap.add_argument("--prodver", default="")
    ap.add_argument("--docver", default="")
    a = ap.parse_args()
    n, e = convert(a.pdf, a.out, url=a.url, title=a.title, prodver=a.prodver, docver=a.docver)
    print(f"wrote {a.out} ({(n or 0)//1024} KB)" if n else f"skip: {e}")
