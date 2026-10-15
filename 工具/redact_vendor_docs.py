#!/usr/bin/env python3
"""厂商文档（markdown/、英文译文_机翻/、根目录 Release Note）脱敏。

2026-10-15 起，厂商文档不再是"原文不动的豁免树"：阿里云文档里混入的真实内部账号
（工号/实名邮箱）、AccessKeyId、AccessKeySecret 实值也要脱敏后才入库。
本脚本可重复执行（新同步一批厂商文档后跑一遍再提交）。

处理规则
1. 邮箱：本地段 → 首字符 + `***`，域名保留。下列形状不改：
   - example.com 族示例域（官方文档通用占位邮箱，无身份信息）
   - Kerberos 主体（域名全大写，如 HADOOP.COM 里的 user@REALM，不是邮箱）
   - user@IP 形状（root@IP 这类 SSH/主机写法，域名只含数字、点、x/X）
   - openssh.com 证书算法名（ssh-rsa-cert-v01@openssh.com）
   - 本地段 `git`（git@code.aliyun.com 克隆地址）
   - 本地段本来就是纯 x/X 占位（xxx@aliyun.com）
   - JSON 路径误报（域名里有纯数字段，如 messages.@reverse 这种）
   - 数据库 账号@实例地址（rm-*/pc-*/gp-* 开头或 .rds 结尾的域名）
2. AccessKeyId：LTAI + 16 位以上 → 前缀保留，其余打 `*`。
3. AccessKeySecret：实值（≥20 位）或行内打了尾码的残值（以 `**` 结尾的串）→ 整段打 `*`；
   `yourAccessKeySecret` 这类占位词、纯描述文字不动。

刻意不处理（判定为厂商公开示例值，非凭证）：示例密码（Test123456 等）、
预签名 URL 里的 Signature 运算结果、样例手机号、文档截图（图片无法改写）。

用法
    redact_vendor_docs.py            # 默认扫 markdown/、英文译文_机翻/、两份 Release Note
    redact_vendor_docs.py 路径...    # 指定文件或目录（目录递归 *.md）
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
AK = re.compile(r"LTAI[0-9A-Za-z]{16,}")
AKSECRET = re.compile(
    r"(?i)(access[\s_]?key[\s_]?secret|secretaccesskey)([|:=\"'\s]{1,10})([A-Za-z0-9+/=]{20,})"
)
# 表格行里厂商自己打了尾码的残值：| AccessKeySecret | String | wyLTSmsy**** 这种
AKSECRET_ROW = re.compile(r"(?i)access[\s_]?key[\s_]?secret")
PARTIAL_SECRET = re.compile(r"[A-Za-z0-9+/=]{8,}(?:[ \t][A-Za-z0-9+/=]+)*\*{2,}")

EXAMPLE_DOMAINS = {"example.com", "example1.com", "example2.com", "example.co", "example.org"}


def email_skipped(addr: str) -> bool:
    local, _, domain = addr.rpartition("@")
    d = domain.lower()
    if d in EXAMPLE_DOMAINS:
        return True
    if d == "openssh.com":                                   # ssh 证书算法名
        return True
    if local.lower() == "git":                               # git clone 地址
        return True
    if local and all(c in "xX*" for c in local):             # 本地段已是占位符
        return True
    if re.fullmatch(r"[0-9xX.]+", domain):                   # user@IP / 已打码 IP
        return True
    if any(c.isalpha() for c in domain) and domain == domain.upper():  # Kerberos realm
        return True
    if any(len(l) == 1 and l.isdigit() for l in d.split(".")):  # JSON 路径误报（如 messages.@reverse）
        return True
    if d.endswith(".rds"):                                   # DMS 库账号@库名
        return True
    if any(l.startswith(("rm-", "pc-", "gp-")) for l in d.split(".")):  # 实例地址
        return True
    return False


def redact(text: str):
    count = 0

    def sub_email(m):
        nonlocal count
        addr = m.group(0)
        if email_skipped(addr):
            return addr
        count += 1
        local, _, domain = addr.rpartition("@")
        return local[0] + "***@" + domain

    def sub_ak(m):
        nonlocal count
        count += 1
        return "LTAI" + "*" * (len(m.group(0)) - 4)

    def sub_secret(m):
        nonlocal count
        val = m.group(3)
        if val.lower().startswith("your"):                   # yourAccessKeySecret 占位词
            return m.group(0)
        count += 1
        return m.group(1) + m.group(2) + "*" * len(val)

    text = EMAIL.sub(sub_email, text)
    text = AK.sub(sub_ak, text)
    text = AKSECRET.sub(sub_secret, text)

    lines = text.split("\n")
    for i, line in enumerate(lines):
        if AKSECRET_ROW.search(line):
            def sub_partial(m):
                nonlocal count
                count += 1
                return "*" * len(m.group(0))
            lines[i] = PARTIAL_SECRET.sub(sub_partial, line)
    text = "\n".join(lines)
    return text, count


def main():
    paths = sys.argv[1:] or [
        "markdown", "英文译文_机翻",
        "ApsaraStack-3.18.6-Release-Note-EN.md",
        "ApsaraStack-V3.18.6_2607-Release-Note-EN.md",
    ]
    files = []
    for p in paths:
        pp = Path(p)
        if pp.is_dir():
            files += sorted(pp.rglob("*.md"))
        else:
            files.append(pp)
    changed, total, bad = 0, 0, 0
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            bad += 1
            continue
        new, n = redact(text)
        if n:
            f.write_text(new, encoding="utf-8")
            changed += 1
            total += n
            print(f"{n:4d}  {f.relative_to(ROOT) if f.is_relative_to(ROOT) else f}")
    print(f"== {changed} 个文件改动，{total} 处脱敏，{bad} 个非 UTF-8 跳过")


if __name__ == "__main__":
    main()
