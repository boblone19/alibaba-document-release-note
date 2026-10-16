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
NUM_ONLY = re.compile(r"^(\d+(?:\.\d+)+)\.?\s*$")   # 编号独占一行（标题在下一行），至少两级编号避免误判列表项
# 注意/警告框：厂商 PDF 里 note 总是一个独立文本块、标签在块首行，必须带冒号（"Note that…" 是普通散文）
# 注意框在 PDF 里是独立文本块，但 _para_join 会把它并进上一句 → 在拼好的段落里按句子边界切开。
# 只认厂商 DITA 提示框的实际写法（首字母大写）：全大写的 "WARNING:" 多数是示例日志输出，不是提示框。
NOTE_INLINE = re.compile(r"(?:^|(?<=[.!?;])\s+)((?:Important\s+)?Note|Notice|Important|Warning|Caution|Danger)\s*[:：]\s+")
# 提示框的物理特征：厂商 PDF 把 note 整块排成同一个灰色（实测各手册均为 0x73777a），
# 标签行单独成行且只有 "Note" / "Note:"（图标说明会重复一行）。
NOTE_WORD = re.compile(r"^\**\s*(Note|NOTICE|Notice|IMPORTANT|Important|WARNING|Warning|CAUTION|Caution|DANGER|Danger|说明|注意|警告|重要|禁止)\s*[:：]?\s*\**\s*$")
# 标签与正文同一行的情况。容忍 _inline 已经给标签加上的粗体星号，避免输出两个 "Note:"。
NOTE_LEAD = re.compile(r"^\**\s*((?:Important\s+)?Note|NOTICE|Notice|IMPORTANT|Important|WARNING|Warning"
                       r"|CAUTION|Caution|DANGER|Danger|说明|注意|警告|重要|禁止)\s*\**\s*[:：]\s*\**\s*(.*)$", re.S)


def _rgb(c):
    return ((c >> 16) & 255, (c >> 8) & 255, c & 255) if isinstance(c, int) else (0, 0, 0)


def _near(c1, c2, tol=0x26):
    """两个颜色是否足够接近（同一手册里 note 灰可能是 0x73777a 或 0x777777）。"""
    return c1 is not None and c2 is not None and all(abs(a - b) <= tol for a, b in zip(_rgb(c1), _rgb(c2)))


def _grey_ratio(spans, col):
    """该行有多大比例的字符是提示框灰。链接是蓝色，所以不能要求整行同色。"""
    tot = grey = 0
    for s in spans:
        n = len((s.get("text") or "").strip())
        tot += n
        if _near(s.get("color"), col):
            grey += n
    return tot and grey / tot


def note_blocks(md):
    """把 "… sentence. Note: follow-up" 里的提示块改成 Markdown 引用块 `> **Note:** follow-up`。

    只动普通段落行：代码块内、表格行（放不进引用块）、标题、列表项、缩进行一律跳过。
    """
    out, fence = [], False
    for line in md.split("\n"):
        st = line.strip()
        if st.startswith("```"):
            fence = not fence
            out.append(line)
            continue
        if (fence or not st or st.startswith(("#", "|", ">", "`")) or BULLET.match(st)
                or NUMITEM.match(st) or line[:1].isspace()):
            out.append(line)
            continue
        frag, pieces = st, []
        while True:
            m = NOTE_INLINE.search(frag)
            if not m:
                pieces.append(("text", frag.strip()))
                break
            lab = re.sub(r"\s+", " ", m.group(1)).strip().title()
            body = frag[m.end():].strip()
            if len(body) < 8:                         # 只有标签没有正文 → 整行原样
                pieces.append(("text", frag.strip()))
                break
            pieces.append(("text", frag[:m.start()].strip()))
            pieces.append(("note", f"> **{lab}:** {body}"))
            frag = ""
            break
        head = [p[1] for p in pieces if p[0] == "text" and p[1]]
        note = [p[1] for p in pieces if p[0] == "note"]
        if not note:
            out.append(line)
            continue
        for h in head:
            out += [h, ""]
        out += note
    return "\n".join(out)
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
        self.seen_nums = set()           # 已当作标题输出的书签编号，重复出现即页眉/目录残留
        self.drop_next = ""              # 编号行合并成标题后，下一次出现的同名标题行不再输出
        self.note_col = None             # 提示框文字用的灰色（由标签行反推，None=这本书不按灰色识别）
        self.pend = None                 # 标签自成一格时，挂起来等紧跟着的正文块

    def num_head(self, raw):
        """行首编号能与 PDF 书签对上 → 真标题，字号再小也算（有的手册二级以下标题只排 9.8pt）。

        返回 (num, level, title) 或 None。必须整行文字与书签标题吻合（允许折行截断），
        避免把 "1. Create a bucket" 这类步骤行误升为第 1 章。
        """
        m = HEAD_NUM.match(raw)
        if not m:
            return None
        num = m.group(1)
        book = self.toc_by_num.get(num)
        if not book:
            return None
        bkey = re.sub(r"\s+", " ", book).strip().lower()
        key = re.sub(r"\s+", " ", normalize(raw[m.end():])).strip().rstrip(".· )\t ").lower()
        if not key:
            return None
        hit = key == bkey or (bkey.startswith(key) and len(key) >= max(8, int(0.6 * len(bkey))))
        return (num, min(6, num.count(".") + 2), re.sub(r"\s+", " ", book).strip()) if hit else None

    def blank(self):
        if self.out and self.out[-1] != "":
            self.out.append("")

    def note_kind(self, bdata):
        """给一个文本块定性：
          ("label", 标签, y1)   —— 整块只有 "Note:" 这类标签（图标说明，正文在下一块）
          ("note", 标签或空, [(k, 文本)], y1)  —— 提示框正文（可能自带行首标签）
          (None,)               —— 普通内容
        判据：整块灰（标签色），或首行是 Note/Warning… 标签且标签带颜色。
        """
        col, none = self.note_col, (None,)
        if not bdata:
            return none
        raw0, sp0, box0 = bdata[0]
        first, html0 = raw0.strip(), _inline(sp0).strip()
        if _is_code(sp0) or HEAD_NUM.match(first) or re.sub(r"\s+", " ", first).lower() in self.toc_lvl:
            return none
        grey = bool(col) and sum(_grey_ratio(sp, col) for _r, sp, _b in bdata) >= 0.7 * len(bdata)
        only = all(NOTE_WORD.match(r.strip()) for r, _s, _b in bdata)
        ml = NOTE_LEAD.match(html0)
        own = (ml.group(1)[0].upper() + ml.group(1)[1:].lower()) if ml else ""
        labelled = NOTE_WORD.match(first)
        if labelled and own == "" and not ml:
            own = labelled.group(1)[0].upper() + labelled.group(1)[1:].lower()
        lab_col = self.line_label(sp0)
        if only and (grey or labelled):
            return ("label", own, max(b.y1 for _r, _s, b in bdata))
        lines = None
        if grey:
            lines = self.note_lines(bdata, bool(own))
        elif labelled and len(bdata) > 1 and not _is_code(bdata[1][1]):
            lines = self.note_lines(bdata, False)       # 标签独立成行 + 下面缩进的正文（无颜色线索）
        elif ml and lab_col and not _near(lab_col[1], self.body_col) and ml.group(2).strip():
            lines = self.note_lines(bdata, True)        # 标签有色、正文黑色（另一些手册的排法）
        if lines is None:
            return none
        return none if not lines else ("note", own, lines)

    def note_lines(self, bdata, drop_lead):
        """把提示框块里的行格式化成 (k, 文本, y0, y1)；k：p 正文 / b 项目符号 / n 编号项。"""
        out = []
        for i, (raw, spans, box) in enumerate(bdata):
            txt, html = raw.strip(), _inline(spans).strip()
            m = NOTE_WORD.match(txt)
            if m and not out:                           # 纯标签行（图标说明会重复一次）
                continue
            if drop_lead and i == 0:
                ml = NOTE_LEAD.match(html)
                if ml:
                    html = ml.group(2).strip()
                    if not html:
                        continue
            ni = NUMITEM.match(txt)
            if BULLET.match(txt):
                out.append(("b", re.sub(BULLET, "", html).strip(), box.y0, box.y1))
            elif ni:
                out.append(("n", f"{ni.group(1)}. " + html[ni.end():].strip(), box.y0, box.y1))
            else:
                out.append(("p", html, box.y0, box.y1))
        return out

    def close_quote(self):
        """提示框结束后必须补空行，否则后面的段落会被 Markdown 当成引用块的续行吃掉。"""
        if self.out and self.out[-1].startswith("> "):
            self.out.append("")

    def emit_note(self, lab, lines):
        """提示框 → Markdown 引用块。lines 为 (kind, text)，kind：p 正文 / b 项目符号 / n 编号项。

        同一个提示框常被排成好几块（标签一块、正文一块、列表一块），靠纵向间距判断是否续写。
        """
        parts, buf = [], []

        def cut():
            if buf:
                parts.append(("p", " ".join(buf)))
                buf.clear()

        for kind, text, _y0, _y1 in lines:
            if kind != "p":
                cut()
                parts.append((kind, text))
            elif buf and re.search(rf"[{CJK}]$", buf[-1]) and re.match(rf"[{CJK}]", text):
                buf[-1] += text
            else:
                buf.append(text)
        cut()
        if not parts:
            return
        cont = bool(lab) is False and bool(self.out) and self.out[-1].startswith("> ")
        if cont:
            pass                        # 无标签的灰块紧跟在引用块后 = 同一个提示框的后续段/列表
        else:
            self.blank()
        out, labelled = [], False
        if lab and parts[0][0] != "p":
            out.append(f"> **{lab}:**")
            labelled = True
        for kind, text in parts:
            head = "> "
            if lab and not labelled and kind == "p":
                head += f"**{lab}:** "
                labelled = True
            out.append(head + ("- " + text if kind == "b" else text))
        self.out += out

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
        # 小字号的章名/编号行：页眉碎片或目录页残留（能与书签编号对上的真标题不在此列）
        if size < 12.5:
            k = re.sub(r"\s+", " ", re.sub(HEAD_NUM, "", txt)).strip().lower()
            if k and len(k) <= 60 and k in self.toc_lvl and not self.num_head(raw):
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
        """Pass 1: count on how many distinct pages each normalized line appears.
        顺带反推提示框的标签色：行首是 Note/Warning/… 的那些行，取标签所在 span 的颜色。"""
        seen, colcnt, labcol = {}, {}, {}
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
                    for sp in spans:
                        colcnt[sp.get("color")] = colcnt.get(sp.get("color"), 0) + len(sp["text"])
                    if t:
                        k = re.sub(r"\s+", " ", t).lower()
                        seen.setdefault(k, set()).add(pno)
                        lab = self.line_label(spans)
                        if lab:
                            c = lab[1]
                            labcol[c] = labcol.get(c, 0) + 1
        self.frequent = {k: len(v) for k, v in seen.items()}
        n = max(1, self.pdf.page_count - self.start)
        self.freq_min = max(4, int(n * 0.35))
        self.body_col = body = max(colcnt, key=colcnt.get) if colcnt else None
        hits = sorted(labcol, key=lambda c: -labcol[c])
        self.note_col = next((c for c in hits if labcol[c] >= 2 and c != body and c not in (0, None)), None)

    @staticmethod
    def line_label(spans):
        """行首若是提示框标签就返回 (标签, 该 span 的颜色)。允许两种排法：
        标签独占一行（"Warning"），或标签与正文同行（"Note: 正文…"）；后者要求标签自己是粗体，
        免得把 "Warning: 100" 这类日志输出误判成提示框。"""
        import itertools
        acc = ""
        for sp in spans:
            txt = (sp.get("text") or "").strip()
            if not txt:
                continue
            head = (acc + " " + txt).strip() if acc else txt
            m = NOTE_WORD.match(head) or NOTE_LEAD.match(head)
            if m:
                bold = (sp.get("flags", 0) & 16) or "bold" in (sp.get("font") or "").lower()
                lab = m.group(1) if m.re is NOTE_WORD else m.group(1)
                if NOTE_LEAD.match(head) and not bold and not acc:
                    return None
                return (lab[0].upper() + lab[1:].lower(), sp.get("color"))
            acc = head
            if len(acc) > 40:
                break
        return None

    @property
    def base(self):
        return re.sub(r"^Alibaba Cloud Apsara Stack V[\d.]+\s*", "", os.path.basename(self.path)[:-4])

    def run(self, title=""):
        pymupdf = self.pymupdf
        self.scan_frequency()
        for pno in range(self.start, self.pdf.page_count):
            page = self.pdf[pno]
            self.drop_next = ""           # 只在同一页内合并
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
            blocks = []
            for blk in d.get("blocks", []):
                if blk.get("type") != 0:
                    continue
                bdata = []
                for ln in blk.get("lines", []):
                    spans = [sp for sp in ln.get("spans", []) if (sp.get("text") or "").strip()]
                    if not spans:
                        continue
                    box = pymupdf.Rect(ln["bbox"])
                    midx, midy = (box.x0 + box.x1) / 2, (box.y0 + box.y1) / 2
                    if any(r.contains((midx, midy)) for r in rects):
                        continue        # 只把行中心真正落在表格框内的行当作表格内容，避免吃掉贴边正文
                    raw = normalize("".join(sp["text"] for sp in spans))
                    if raw.strip():
                        bdata.append((raw, spans, box))
                if bdata:
                    blocks.append((round(min(b.y0 for _r, _s, b in bdata), 1), len(blocks),
                                   self.note_kind(bdata), bdata))
            def plain(sq, bd):
                for li, (raw, spans, box) in enumerate(bd):
                    items.append((round(box.y0, 1), sq * 10000 + li, "L", (raw, spans, box.x0)))

            i2, nbl = 0, len(blocks)
            while i2 < nbl:
                y0, seq, kind, bdata = blocks[i2]
                if kind[0] == "label":                  # 标签自成一格，往下看紧跟的正文格
                    labs, j, bottom = [(kind[1], kind[2])], i2 + 1, kind[2]
                    while j < nbl and blocks[j][2][0] == "label" and blocks[j][0] - bottom <= 26:
                        labs.append((blocks[j][2][1], blocks[j][2][2]))
                        bottom = blocks[j][2][2]
                        j += 1
                    lab = next((l for l, _y in labs if l), "")
                    nk = blocks[j][2] if j < nbl else None
                    if nk and nk[0] == "note" and not nk[1] and blocks[j][0] - bottom <= 26:
                        items.append((blocks[j][0], blocks[j][1], "N", (lab, nk[2])))
                    else:                               # 没配上正文：标签行退回普通文本，绝不吞字
                        for k in range(i2, j):
                            plain(blocks[k][1], blocks[k][3])
                    i2 = j + 1
                    continue
                if kind[0] == "note":
                    items.append((y0, seq, "N", (kind[1], kind[2])))
                    i2 += 1
                    continue
                plain(seq, bdata)
                i2 += 1
            for _y, _o, kind, payload in sorted(items, key=lambda x: (x[0], x[1])):
                if kind == "N":
                    self.flush()
                    self.emit_note(*payload)
                    continue
                self.close_quote()
                if kind == "T":
                    self.flush()
                    self.blank()
                    self.out += [payload, ""]
                    continue
                raw, spans, x0 = payload
                txt = raw.strip()
                if self.drop_next and re.sub(r"\s+", " ", normalize(txt)).strip().lower().rstrip(".·") == self.drop_next:
                    self.drop_next = ""      # 编号行已用书签补全成标题，标题文字行不再重复输出
                    continue
                one = NUM_ONLY.match(txt)
                if one and one.group(1) in self.toc_by_num:
                    # 编号与标题分两行排版（API 手册常见 "1.5.2." 独占一行）：合并且只输出一次
                    self.flush()
                    self.blank()
                    num = one.group(1)
                    text = f"{num} {self.toc_by_num[num]}"
                    lvl = min(6, num.count(".") + 2)
                    self.out.append("#" * lvl + " " + text)
                    self.out.append("")
                    self.collected.append((lvl, text))
                    self.seen_nums.add(num)
                    self.drop_next = re.sub(r"\s+", " ", self.toc_by_num[num]).strip().lower()
                    continue
                size = max(round(sp.get("size", 0) or 0, 1) for sp in spans)
                flagged = size >= HEAD_MIN_PT or bool(HEAD_NUM.match(raw))
                if self.junk(txt, raw, flagged, size):
                    continue
                if _is_code(spans):
                    self.code.append(raw.rstrip())
                    continue
                self.flush()
                m = HEAD_NUM.match(raw)
                nh = self.num_head(raw) if m else None
                if nh and size < HEAD_MIN_PT:            # 小字号真标题：同一编号只认第一次出现
                    if nh[0] in self.seen_nums:
                        continue
                    self.seen_nums.add(nh[0])
                if m and (size >= HEAD_MIN_PT or nh) and len(txt) < 170:
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
        md = note_blocks(normalize(_para_join("\n".join(self.out))))
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
            + 'converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)\n---\n\n')
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
