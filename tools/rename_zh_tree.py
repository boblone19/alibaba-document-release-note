#!/usr/bin/env python3
"""把中文两棵树（01_ApsaraStack-Enterprise / 02_AIStack）改成与英文树一致的命名。

规则（与 10_EN_* 完全同一条）：

    markdown/<NN>_ZH_<Suite>_<Version>/<Product>/<Product> <DocType> <YYYYMMDD>.md

- 树名：去掉日期尾巴、补语言位，版本统一 vX.Y.Z
      01_ApsaraStack-Enterprise_v3.18.6_20260730 -> 01_ZH_ApsaraStack_v3.18.6
      02_AIStack_v2.17.0_20260828_OpenTrek      -> 02_ZH_AIStack_v2.17.0
- 取消服务域层（ai/ database/ ...）：英文树本来就没有这一层，46 个 code 跨域唯一，0 撞名。
- 产品目录用官方英文名；一个 code 里含多个子产品时按子产品拆目录
  （polardb 下 MySQL 集群版/主备版、PostgreSQL 主备版/共享存储版、集分一体版；
   opentrek 下 AI Studio / AI Gateway / Agent Dev ...），否则文件名会丢产品身份。
- 文件名 = 目录名 + 手册类型 + 8 位日期；完全同名才加 " (2)"。
- 中文书名（label）留在索引里做检索，不再进路径。

    python tools/rename_zh_tree.py            # 试跑：出迁移表、撞名与路径长度检查
    python tools/rename_zh_tree.py --apply    # 真搬 + 改索引 + 剪空目录
"""
import argparse
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cache  # noqa: E402

MD = os.path.join(ROOT, "markdown")
MANIFEST = os.path.join(MD, "conversion_manifest_zh.json")

TREES = {
    "01_ApsaraStack-Enterprise_v3.18.6_20260730": "01_ZH_ApsaraStack_v3.18.6",
    "02_AIStack_v2.17.0_20260828_OpenTrek": "02_ZH_AIStack_v2.17.0",
}

# code 级默认目录：书名里没有子产品前缀时用它
DEFAULT_DIR = {
    "acr": "Container Registry",
    "aegis": "Server Guard",
    "alinux": "Alibaba Cloud Linux",
    "apds": "Cloud Migration Hub",
    "apigateway": "API Gateway",
    "apsara_stack_dns": "Apsara Stack DNS",
    "apsara_stack_platform": "Apsara Uni-manager",
    "apsarabase": "Apsara Stack Platform",
    "asdelivery": "Apsara Stack Delivery",
    "asr": "Apsara Stack Resilience",
    "cas": "Certificate Management Service",
    "cbs": "Database Backup",
    "cgw": "Cloud gateway",
    "csk": "Container Service for Kubernetes",
    "dbaudit": "Database Audit",
    "dide": "DataWorks",
    "dms": "Data Management",
    "dts": "Data Transmission Service",
    "ecs": "Elastic Compute Service",
    "ess": "Auto Scaling",
    "expressconnect": "Express Connect",
    "hcs_hgw": "Cloud Defined Storage",
    "hdm": "Database Autonomy Service",
    "hologram": "Hologres",
    "hsm": "Hardware Security Module",
    "kms": "Key Management Service",
    "kvstore": "Tair(Redis OSS-compatible)",
    "mongodb": "ApsaraDB for MongoDB",
    "nas": "File Storage NAS",
    "ntr": "TransitRouter",
    "odps": "MaxCompute",
    "oos": "Operation Orchestration Service",
    "opentrek": "OpenTrek",
    "oss": "Object Storage Service",
    "polardb": "ApsaraDB for POLARDB",
    "quickbi": "Quick BI",
    "rds": "ApsaraDB for RDS",
    "rocketmq": "Message Queue RocketMQ",
    "ros": "Resource Orchestration Service",
    "sas": "Cloud Security Management Center",
    "sc": "Realtime Compute",
    "slb": "Server Load Balancer",
    "sls": "Log Service",
    "vpc": "Virtual Private Cloud",
    "vpn": "VPN Gateway",
    "yundun": "Cloud Security",
}

# 书名里的子产品前缀 -> 官方英文产品名（键是去掉类型词后的中文字头）
PRODUCT = {
    # security
    "安骑士": "Server Guard",
    "容器安全": "Container Security",
    "云安全管理中心": "Cloud Security Management Center",
    "漏洞扫描": "Vulnerability Scan",
    "安全编排自动化响应": "Security Orchestration Automation and Response",
    "安全响应自动化编排": "Security Orchestration Automation and Response",
    "数据库安全审计": "Database Security Audit",
    "数据静态脱敏与水印": "Static Data Masking and Watermarking",
    "数据库审计与风险控制": "Database Audit and Risk Control",
    "云盾": "Cloud Security",
    "加密服务（租户侧）": "Encryption Service (Tenant Side)",
    "加密服务管控（租户侧）": "Encryption Service Management (Tenant Side)",
    "密码服务": "Cryptographic Service",
    "密钥管理服务": "Key Management Service",
    "数字证书管理服务（租户侧）": "Certificate Management Service (Tenant Side)",
    # compute / cloud-native
    "分布式云容器平台ACK One": "ACK One",
    "容器计算服务ACS": "Container Compute Service (ACS)",
    "实例规格族&实例规格": "Instance Families and Specifications",
    "远程证明服务": "Remote Attestation Service",
    "统一云管平台": "Apsara Uni-manager",
    "飞天助理": "Apsara Copilot",
    "云原生网关": "Cloud-native Gateway",
    "API网关（旧）": "API Gateway (Legacy)",
    "API网关": "",                       # 就是 code 级产品名，落回 DEFAULT_DIR
    "专有云": "",                        # 套件名，不单独建目录
    "数据中心": "",                      # “数据中心机房要求”归到平台目录下
    # network
    "域名解析DNS（云内）": ("Apsara Stack DNS", "Intra-cloud"),
    "域名解析DNS（跨云）": ("Apsara Stack DNS", "Cross-cloud"),
    "应用型负载均衡ALB": "Application Load Balancer (ALB)",
    "ALB": "Application Load Balancer (ALB)",
    # database
    "PolarDB MySQL集群版": "PolarDB MySQL Cluster Edition",
    "PolarDB MySQL主备版": "PolarDB MySQL Primary_Standby Edition",
    "PolarDB PostgreSQL主备版": "PolarDB PostgreSQL Primary_Standby Edition",
    "PolarDB PostgreSQL集群共享存储版": "PolarDB PostgreSQL Shared-Storage Cluster Edition",
    "PolarDB集分一体版": "PolarDB Integrated Edition",
    # storage
    "CPFS": "CPFS",
    "APFS": "APFS",
    "EFS-NAS": "EFS-NAS",
    # big-data
    "Flink企业版": "Flink Enterprise Edition",
    "Flink存算分离版": "Flink Compute-Storage Separation Edition",
    # messaging
    "RocketMQ v5.0": "RocketMQ v5.0",
    "MQTT v5.0": "MQTT v5.0",
    "RocketMQ": "RocketMQ",
    "MQTT": "MQTT",
    # opentrek
    "AgentRuntime": "AgentRuntime",
    "AI网关": "AI Gateway",
    "AI Studio（标准版）": "AI Studio (Standard Edition)",
    "AI Studio": "AI Studio",
    "OpenTrek-Ops": "OpenTrek-Ops",
    "HiMarket": "HiMarket",
    "Agent Dev": "Agent Dev",
    "OpenTrek-UniOperator": "OpenTrek UniOperator",
    "Blink": "Blink",
    # delivery / platform
    "JOK": "JOK",
    "ASI": "ASI",
    "钟馗": "Zhongkui",
    "专有云平台企业版": "Apsara Stack Enterprise",
    "专有云平台企业版安全": ("Apsara Stack Platform", "Enterprise Edition Security"),
    "高可用": ("Apsara Stack Platform", "High Availability"),
    "多Region": ("Apsara Stack Platform", "Multi-Region"),
    "数据中心机房": "IDC Facility",
    "专有云术语表": "Apsara Stack Glossary",
    # disaster recovery
    "灾备管理平台": "Disaster Recovery Management Platform",
    "同城容灾管理平台ASR": "ASR (Local Disaster Recovery)",
    "同城容灾ASR": "ASR (Local Disaster Recovery)",
    "异地容灾管理平台ASR-DR": "ASR-DR (Remote Disaster Recovery)",
    "备份管理平台ASR-BR": "ASR-BR (Backup and Recovery)",
    "云平台备份": "Cloud Platform Backup",
}

# 手册类型：中文后缀 -> 英文（按长度降序匹配，避免 "管理员指南" 抢 "安全管理员指南"）
TYPES = {
    "安全管理员指南": "Security Administrator Guide",
    "实例规格族&实例规格简介": "Instance Families and Specifications",
    "License指南": "License Guide",
    "运维指南": "Operations and Maintenance Guide",
    "开发指南": "Developer Guide",
    "用户指南": "User Guide",
    "部署指南": "Deployment Guide",
    "使用指南": "User Guide",
    "管理员指南": "Administrator Guide",
    "技术白皮书": "Technical Whitepaper",
    "产品简介": "Product Introduction",
    "产品概述": "Product Overview",
    "版本说明书": "Release Notes",
    "系统配置": "System Configuration Guide",
    "术语表": "Glossary",
    "白皮书": "Whitepaper",
    "机房要求": "IDC Requirements",
}
TYPE_KEYS = sorted(TYPES, key=len, reverse=True)

# 书名尾部的括号限定词 -> 英文写法
QUAL = {"ascm": "ASCM", "RDS MySQL": "RDS MySQL", "RDS PostgreSQL": "RDS PostgreSQL", "PolarDB": "PolarDB"}
QUAL_RE = re.compile(r"[（(]([^（）()]*)[)）]\s*$")


def split_label(label):
    """'云安全管理中心用户指南（ascm）' -> ('Cloud Security Management Center', 'User Guide', 'ASCM')"""
    lab = label.strip()
    qual = ""
    m = QUAL_RE.search(lab)
    if m:
        qual = QUAL.get(m.group(1).strip(), m.group(1).strip())
        lab = lab[:m.start()].strip()
    typ = None
    for k in TYPE_KEYS:
        if lab.endswith(k):
            typ, lab = TYPES[k], lab[:-len(k)].strip()
            break
    if typ is None:
        return None, None, qual
    head = lab.strip(" -")
    return (head or None), typ, qual


def build_plan():
    man = json.load(open(MANIFEST, encoding="utf-8"))
    idx = {(r.get("markdown") or "").replace("\\", "/"): r
           for r in cache.load(ROOT).values() if r.get("lang") == "zh"}
    plan, unmapped = [], []
    for x in man:
        old = x["mdPath"].replace("\\", "/")
        parts = old.split("/")
        if len(parts) != 5:
            unmapped.append((old, "层级不是 树/域/code/文件"))
            continue
        tree, code = parts[1], parts[3]
        if tree not in TREES or code not in DEFAULT_DIR:
            unmapped.append((old, f"未登记的树或 code：{tree} / {code}"))
            continue
        r = idx.get(old) or {}
        head, typ, qual = split_label(r.get("label") or "")
        if typ is None:
            unmapped.append((old, f"认不出手册类型：{r.get('label')}"))
            continue
        prod = PRODUCT.get(head, None) if head else ""
        if prod is None:
            unmapped.append((old, f"认不出子产品：{head!r}"))
            continue
        if isinstance(prod, tuple):        # (目录, 文件名限定词)
            prod, q2 = prod
            qual = qual or q2
        if not prod:                       # 空串 = 用 code 级产品名
            prod = DEFAULT_DIR[code]
        name = f"{prod} {typ}" + (f" ({qual})" if qual else "") + f" {x['docVer']}.md"
        new = f"{TREES[tree]}/{prod}/{name}"
        bad = set('<>:"/\\|?*') & set(new.replace("/", ""))
        if bad:
            unmapped.append((old, f"名字里有非法字符 {sorted(bad)}：{prod}"))
            continue
        plan.append({"old": old, "new": new, "label": r.get("label"), "code": code})
    return plan, unmapped


def dedupe(plan):
    """完全同名才加 (2)(3)……；顺序按旧路径，保证可复现"""
    seen = {}
    for it in sorted(plan, key=lambda x: x["old"]):
        base = it["new"][:-3]
        n = seen.get(base.lower(), 0) + 1
        seen[base.lower()] = n
        if n > 1:
            it["new"] = f"{base} ({n}).md"
    return plan


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    os.chdir(ROOT)
    plan, unmapped = build_plan()
    print(f"待迁移 {len(plan)} 本；映射不出来的 {len(unmapped)} 项")
    for o, why in unmapped[:20]:
        print("   未映射：", why, "|", o)
    plan = dedupe(plan)

    dirs = {}
    for it in plan:
        dirs.setdefault(it["new"].split("/")[0], set()).add(it["new"].split("/")[1])
    for t in sorted(dirs):
        print(f"  {t}: {len(dirs[t])} 个产品目录, "
              f"{sum(1 for i in plan if i['new'].startswith(t + '/'))} 本")

    suf = [i for i in plan if re.search(r" \(\d+\)\.md$", i["new"])]
    ln = [len("markdown/" + i["new"]) for i in plan]
    fn = [len(os.path.basename(i["new"])) for i in plan]
    print(f"加尾号 {len(suf)} 本 | 文件名 均 {sum(fn)/len(fn):.0f} 最长 {max(fn)}"
          f" | 全路径 最长 {max(ln)} | >260 {sum(1 for x in ln if x > 260)}")

    old_missing = [i["old"] for i in plan if not os.path.exists(os.path.join(ROOT, i["old"]))]
    if old_missing:
        print(f"\n磁盘上找不到的旧文件 {len(old_missing)} 条，样例：")
        for m in old_missing[:5]:
            print("   ", m)
    tgt = {}
    for i in plan:
        tgt.setdefault(i["new"].lower(), []).append(i["old"])
    clash = {k: v for k, v in tgt.items() if len(v) > 1}
    if clash:
        print("目标撞名（应为 0）：", list(clash.items())[:3])

    print("\n样例：")
    for i in plan[:8]:
        print("  ", i["old"].split("/", 1)[1])
        print("   ->", i["new"])
    if not a.apply:
        print("\n（试跑，未改动。加 --apply 才搬）")
        return 0
    return apply(plan)


def apply(plan):
    moved = 0
    for it in plan:
        so = os.path.join(MD, it["old"].split("/", 1)[1])
        sn = os.path.join(MD, it["new"])
        if not os.path.exists(so):
            continue
        os.makedirs(os.path.dirname(sn), exist_ok=True)
        shutil.move(so, sn)
        moved += 1
    mp = {i["old"]: i["new"] for i in plan}
    print(f"搬完 {moved} 本；开始同步索引")

    # 1) doc_cache_index（markdown 字段；mdCloudKey 指向 OSS 已发布包，不动）
    rows = cache.load(ROOT)
    hit = 0
    for r in rows.values():
        v = (r.get("markdown") or "").replace("\\", "/")
        if v in mp:
            r["markdown"] = "markdown/" + mp[v]
            hit += 1
    cache.save(ROOT, list(rows.values()))
    print(f"   doc_cache_index 改 {hit} 条")

    # 2) conversion_manifest_zh（mdPath）
    man = json.load(open(MANIFEST, encoding="utf-8"))
    n = 0
    for x in man:
        v = (x.get("mdPath") or "").replace("\\", "/")
        if v in mp:
            x["mdPath"] = "markdown/" + mp[v]
            n += 1
    json.dump(man, open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"   conversion_manifest_zh 改 {n} 条")

    # 3) download_ledger（manuals[].markdown / group；cacheIndex 快照）
    led = json.load(open("download_ledger.json", encoding="utf-8"))
    n = 0
    for m in led.get("manuals", []):
        v = (m.get("markdown") or "").replace("\\", "/")
        if v in mp:
            m["markdown"] = "markdown/" + mp[v]
            m["group"] = mp[v].split("/")[0]
            n += 1
    for e in led.get("cacheIndex", {}).get("entries_detail", []):
        v = (e.get("markdown") or "").replace("\\", "/")
        if v in mp:
            e["markdown"] = "markdown/" + mp[v]
    json.dump(led, open("download_ledger.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"   download_ledger 改 {n} 条")

    # 4) doc_details / doc_index.csv 的 group 字段（PDF 路径保留原始来源，不动）
    det = json.load(open("doc_details.json", encoding="utf-8"))
    n = 0
    for r in det:
        if r.get("group") in TREES:
            r["group"] = TREES[r["group"]]
            n += 1
    json.dump(det, open("doc_details.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"   doc_details 改 {n} 条")
    if os.path.exists("doc_index.csv"):
        t = open("doc_index.csv", encoding="utf-8").read()
        for old, new in TREES.items():
            t = t.replace(old, new)
        open("doc_index.csv", "w", encoding="utf-8").write(t)
        print("   doc_index.csv 改 group 列")

    empties = []
    for root, ds, _fs in os.walk(MD, topdown=False):
        for d in ds:
            p = os.path.join(root, d)
            if not os.listdir(p):
                empties.append(p)
    print(f"\n空目录 {len(empties)} 个（用 host_safe_delete 清理）：")
    for p in empties:
        print("   ", os.path.relpath(p, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())