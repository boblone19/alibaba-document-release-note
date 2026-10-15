"""Re-list the official catalogues into cache-shaped candidates (no PDF traffic).

  python3 工具/list_docs.py --langs en                 # 无需登录：抽国际站下载页的 .pdf 链接
  APSARA_COOKIE='…' python3 工具/list_docs.py --langs zh --stacks enterprise@v_3_18_6_20260730
  python3 工具/list_docs.py --langs en --out 云端清单.json   # 给 pull_docs.py 当 --manifest

英文页是服务端全量渲染，抓 HTML 里的 .pdf 即可（不登录、不翻页）；中文清单接口需要
"有专有云权益的登录态"（cookie 只从环境读，绝不写盘、绝不打印）。
输出字段与 文档缓存索引.json 对齐，因此 decide() 能直接判 SKIP/FETCH/NEW。
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cache  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
EN_PAGE = "https://www.alibabacloud.com/en/product/apsara-stack/download"
ZH_API = "https://help.aliyun.com/apsara/api"
TYPES = ["Introduction to Instance Families and Instance Types", "Operations and Maintenance Guide",
         "Product Introduction", "User Guide", "Developer Guide", "Operations Guide",
         "Release Notes", "Best Practices", "Glossary", "Whitepaper"]
# 版本目录形如 v3.18.6版本文档 / V3.18.6_2607版本文档 / 3.18.1版本文档
# _2607 一批还多一层 "pdf 3/" 子目录，由 (.*/)? 吸收
DIR_RE = re.compile(r"(?:国际版文档|01_ApsaraStackEnterprise)/([Vv]?[\d.]+(?:[-_]\d+)?)(?:_intl_en|版本文档)?/(.*/)?([^/]+)\.pdf$")


def fetch(url, cookie=None, tries=3):
    for i in range(tries):
        try:
            h = {"User-Agent": UA, "Referer": "https://help.aliyun.com/apsara/integrated.html"}
            if cookie:
                h["Cookie"] = cookie
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=90) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception as ex:
            if i == tries - 1:
                print(f"  取不到 {url[:80]}: {ex!r}"[:160], file=sys.stderr)
                return ""
    return ""


def book_file(cid, name, limit=200):
    """手册文件名（不含扩展名）。只有真被 limit 截断时才追加 id 短哈希后缀：
    同产品同类型的长标题（EDAS / 云安全中心 / Flink 分离版等）若一律截到 120 会撞名互相覆盖。"""
    full = safe(name, limit)
    if len(full) < len(safe(name, 10 ** 6)):
        import hashlib
        full += "~" + hashlib.sha1(str(cid).encode("utf-8")).hexdigest()[:6]
    return full


def safe(s, limit=120):
    s = re.sub(r"\s+", " ", str(s or "").strip())
    s = "".join("_" if c in '\\/:*?"<>|' else c for c in s)
    return re.sub(r"_+", "_", s).strip(" ._")[:limit]


def en_list(version=""):
    html = fetch(EN_PAGE + "?_p_lc=1")
    urls = []
    seen = set()
    for m in re.finditer(r"https?:[^\"'\s<>]*?\.pdf", html):
        u = m.group(0).replace("&amp;", "&")
        if u not in seen:
            seen.add(u)
            urls.append(u)
    out = []
    for u in sorted(seen):
        d = urllib.parse.unquote(u)
        # 路径形如 国际版文档/<版本目录>/<...层级可选...>/<文件名>.pdf
        # 已知两种真实形态：
        #   国际版文档/v3.18.6版本文档/统一云管平台/...20260630.pdf
        #   国际版文档/3816 2607/pdf 3/API 网关/... v3.18.6-2607 ... 20260828.pdf
        # 旧版正则把版本目录写死成 [Vv]?[\d.]+ 且只允许一层，因此 "3816 2607" 这类
        # 被打散改名、并多一层 pdf 3/ 中转目录的路径整批漏掉（239 本全丢），
        # 故改为按路径段解析，版本号只认文件名里的 Vx.y.z(-NNNN)。
        rest = d.split("国际版文档/", 1)[1] if "国际版文档/" in d else \
            (d.split("01_ApsaraStackEnterprise/", 1)[1] if "01_ApsaraStackEnterprise/" in d else "")
        if not rest:
            continue
        head, fn = rest.rsplit("/", 1)
        if not fn.lower().endswith(".pdf"):   # 只收 .pdf 对象（页面里还有 zip/图片等非手册）
            continue
        fn = fn[:-4]                          # 既有缓存行的 label/product 不含 .pdf
        segs = [s for s in head.split("/") if s]
        if not segs:
            continue
        fn = re.sub(r"\s*\.pdf$", "", fn, flags=re.I)
        # 少数官方书名里带字面 "/"（如 "PolarDB for MySQL (Primary/Secondary Edition)"），
        # 会把一个文件名劈成两段"目录"。产品目录不以 "Alibaba Cloud Apsara Stack" 开头，
        # 据此回退出真正的末级目录，并把被劈开的后半段并回文件名。
        cut = next((i for i in range(len(segs) - 1, -1, -1)
                    if not re.match(r"(?i)^Alibaba Cloud Apsara Stack", segs[i])), 0)
        fn = "/".join(segs[cut + 1:] + [fn])
        segs = segs[:cut + 1]
        VRE = r"[Vv](\d+\.\d+\.\d+(?:[ _-]\d{3,6})?)"
        m = re.search(VRE, fn)
        if not m:
            hits = list(re.finditer(VRE, d))          # 文件名不含版本号时退回整条路径
            m = hits[-1] if hits else None
        if m:
            ver = "V" + re.sub(r"[ _-]+", "_", m.group(1))
        else:
            ver = "V" + re.sub(r"\s+", "_", segs[0].strip("Vv版本文档_ "))
        if version and ver.lower().lstrip("v") != version.lower().lstrip("v"):
            continue
        dt = next((t for t in TYPES if t.lower() in fn.lower()), "Other")
        prod = re.sub(r"(?i)^\s*Alibaba Cloud Apsara Stack( Enterprise)?( Apsara Stack)?\s*v?[\d.]+(?:[ _-]\d{3,6})?\s*", "", fn)
        prod = re.sub(r"\s*" + re.escape(dt) + r"\s*\d{8}$", "", prod).strip() or segs[-1]
        cat = segs[-1] or prod
        stamp = (re.search(r"(\d{8})", fn) or [""])[0]
        cid, _ = cache.identity("en", u)
        out.append({"id": cid, "lang": "en", "stack": "apsara-stack-intl", "version": ver,
                    "versionStamp": stamp, "productCode": safe(prod, 40).lower().replace(" ", ""),
                    "product": prod, "category": dt, "docType": dt, "label": fn,
                    "pages": None, "bytes": None, "prodVer": ver,
                    "pdfLocal": False, "pdfCloud": "", "url": u,
                    "localPath": f"10_EN_ApsaraStack_{safe(ver)}/{safe(cat) or '未分组'}/{book_file(cid, fn)}.pdf",
                    "inScope": dt in ("User Guide", "Product Introduction", "Developer Guide")})
    return out


def zh_list(stacks, cookie):
    out = []
    for spec in stacks:
        stack, ver = spec.split("@")
        prods = json.loads(fetch(f"{ZH_API}/products?type={stack}&version={ver}", cookie) or "{}").get("data") or []
        if not prods:
            print(f"  {spec}: 空清单（cookie 无效或该账号无专有云权益）", file=sys.stderr)
        for p in prods:
            ms = json.loads(fetch(f"{ZH_API}/product/mapListByUserId?stackCode={stack}&version={ver}"
                                  f"&productCode={p['code']}", cookie) or "{}").get("data") or []
            for m in ms:
                u = m.get("pdfDownloadUrl") or ""
                if u.startswith("//"):
                    u = "https:" + u
                if not u:
                    continue
                cid, _ = cache.identity("zh", u)
                grp = ("02_AIStack_" if stack.startswith("ai_stack") else "01_专有云企业版_") + ver
                out.append({"id": cid, "lang": "zh", "stack": stack, "version": ver,
                            "versionStamp": m.get("docVer") or "", "productCode": p["code"],
                            "product": p.get("name") or p["code"], "category": p.get("category") or "-",
                            "docType": m.get("title") or "", "label": m.get("code") or "",
                            "pages": None, "bytes": None, "prodVer": "",
                            "pdfLocal": False, "pdfCloud": "", "url": u,
                            "localPath": f"{grp}{p.get('category','')}/{safe(p.get('name') or p['code'])}/"
                                         f"{m.get('sort', 0):02d}_{safe(m.get('title') or '')}_{safe(m.get('code') or '')}.pdf",
                            "inScope": True})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langs", default="en", help="en / zh / en,zh")
    ap.add_argument("--version", default="", help="英文只取某版本，如 V3.18.6")
    ap.add_argument("--stacks", default="enterprise@v_3_18_6_20260730,ai_stack@v_2_17_0_20260828")
    ap.add_argument("--out", default="云端清单.json")
    a = ap.parse_args()
    langs = [x.strip() for x in a.langs.split(",") if x.strip()]
    rows = []
    if "en" in langs:
        rows += en_list(a.version)
    if "zh" in langs:
        rows += zh_list([s.strip() for s in a.stacks.split(",") if s.strip()],
                        os.environ.get("APSARA_COOKIE", ""))
    ids = {r["id"] for r in rows}
    print(f"清单 {len(rows)} 条 / 唯一 id {len(ids)} → {a.out}")
    with open(os.path.join(ROOT, a.out) if not os.path.isabs(a.out) else a.out, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    return len(rows) != len(ids)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
