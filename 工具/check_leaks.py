#!/usr/bin/env python3
"""提交前自查：个人邮箱与云端凭证不允许进版本库。

用法
    check_leaks.py --cached   只看本次暂存的新增行（pre-commit 钩子用）
    check_leaks.py            扫全部已跟踪文件

规则（宁可放过，也不误伤官方文档正文）
1. 官方文档树 `markdown/`、`英文译文_机翻/` 整体豁免：里面是阿里云文档自带正文（示例账号、示例 AccessKeyId），
   脱敏它等于改官方原文，且这类示例到处都有，逐条判会淹掉真信号。
   （v1 版按邮箱形状全仓通搜，一次提交误报 200+ 条，就是踩在这个点上。）
2. 已知个人身份：邮箱小写后取 sha256 比对 BLOCKLIST → 命中即 BLOCK（不落明文，本文件可以公开）。
   命中范围**包括官方文档树**，官方文档里不会出现我们的地址，真出现就该拦。
3. 自研文件（README / 台账 / 索引 / 工具 等）出现任何邮箱形态 → BLOCK，白名单示例域除外。
4. 自研文件出现 AccessKeyId 形状的串（LTAI + 16 位以上）或预签名查询参数 → BLOCK；输出统一打码。

退出码 0 = 干净，1 = 命中（钩子据此拒绝提交）。
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXEMPT_PREFIXES = ("markdown/", "英文译文_机翻/")

# 个人身份：sha256(邮箱小写全文)。新增地址用
#   python3 -c "import hashlib;print(hashlib.sha256(b'地址').hexdigest())"
BLOCKLIST = {
    "261e06da04ed4bb5cbb52ca18316bcaaa58e0606c661d6307d5a3b6463237640",  # 工作邮箱
    "e9c3e4370aa296d3f8d9fdb6b80b2f92bb85ef329e3d61de3232f3372b84122e",  # 钉钉邮箱
}

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SAFE_DOMAINS = {
    "example.com", "example1.com", "example2.com", "example.co", "example.org",
    "test.com", "163.com", "123.com", "122.com", "qq.com", "gmail.com", "mail.com",
    "w3.org", "openssh.com", "istio.io", "code.aliyun.com", "aliyun-inc.com",
    "alibaba-inc.com", "aliyun.com", "aliyuncs.com", "odps.aliyuncs.com",
    "users.noreply.github.com",
}
# AccessKeyId / 预签名参数形状。本文件自己不能出现这些字面量，否则自查会咬到自己，
# 所以下面用字符串拼接构造。
AK = re.compile("LTAI[0-9A-Za-z]{16,}|OSS" "AccessKeyI" "d=" + "|Sign" "ature%3D" + "|x" "-oss-sig" "nature")


def git(*args):
    return subprocess.run(["git", "-c", "core.quotepath=off", *args],
                          cwd=ROOT, capture_output=True, text=True).stdout


def staged_rows():
    """[(路径, 新增行)]，首提交（无 HEAD）时与空树比对。"""
    head = git("rev-parse", "--verify", "-q", "HEAD").strip() or \
        git("hash-object", "-t", "tree", "/dev/null").strip()
    out = git("diff", "--cached", "-U0", "--no-color", head)
    rows, path = [], None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            path = line[6:].strip()
        elif line.startswith("+") and not line.startswith("+++") and path:
            rows.append((path, line[1:]))
    return rows


def tracked_rows():
    rows = []
    for rel in git("ls-files", "-z").split("\0"):
        if not rel:
            continue
        try:
            for text in (ROOT / rel).read_text(encoding="utf-8").splitlines():
                rows.append((rel, text))
        except (UnicodeDecodeError, OSError):
            continue
    return rows


def scan(rows):
    hits, authored = [], 0
    for rel, text in rows:
        exempt = rel.startswith(EXEMPT_PREFIXES)
        if not exempt:
            authored += len(text.split())
        for e in EMAIL.findall(text):
            known = hashlib.sha256(e.lower().encode()).hexdigest() in BLOCKLIST
            if known or (not exempt and e.rsplit("@", 1)[-1].lower() not in SAFE_DOMAINS):
                shown = e.split("@", 1)[0][:1] + "***@" + e.rsplit("@", 1)[-1]
                hits.append(f"BLOCK {rel} {'已登记个人邮箱' if known else '自研文件里的邮箱'} {shown}")
        if not exempt and AK.search(text):
            hits.append(f"BLOCK {rel} AccessKeyId/预签名串（原文已打码，不外泄）")
    return sorted(set(hits)), authored


def main():
    rows = staged_rows() if "--cached" in sys.argv else tracked_rows()
    hits, authored = scan(rows)
    for h in hits:
        print(h, file=sys.stderr)
    if hits:
        print("→ 处理：个人身份改成 REDACTED:<sha8>（见 下载台账.json 写法）；确属误报再临时绕过并在提交说明里写清。",
              file=sys.stderr)
        return 1
    print(f"clean（自研内容约 {authored//1000}k 词已扫，官方文档树按前缀豁免，个人身份仍全树比对）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
