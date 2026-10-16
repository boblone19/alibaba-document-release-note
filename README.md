# 阿里专有云（Apsara Stack）产品文档包 —— 索引清单

> **当前状态（2026-10-15：英文 V3.16.2 已补齐至站点全量 61 册）**
> - Markdown 共 **909 份 / 210.8 MB / 源 138,780 页**，本地**不含任何 PDF**：
>   中文 296（42,368 页）·
>   英文 V3.18.6 287（42,932 页）·
>   英文 V3.16.2 61 全量（14,968 页，10-15 补入 8 册）·
>   英文 V3.18.6_2607 265（38,512 页）
> - 站点核对（2026-10-15，alibabacloud.com 英文下载页实测）：V3.16.2 实际可下载 **61** 册——站点筛选器显示的 63 里有 2 条是错挂在该版本下的他版本书目（Terraform User Guide 实为 V3.18.3、V3.12.0 Apsara Big Data Manager User Guide）；V3.18.6 实际 287、V3.18.6_2607 实际 265，均与本地**完全一致，无缺失**
> - 整包：`markdown_全量_909册.zip`（**2026-10-16 重打包**，42.0 MB / 916 条目，testzip 通过）
>   —— 上一版是 10-15 14:17 打的，**早于 16:17 的英文重转提交 `e5a964c`**，所以包里 613 本英文仍是缺目录、丢标题编号的旧稿；本次已逐本核对：613/613 含 `## Table of Contents` 与 `toc+numbered-headings` 标记，中文 296 册内容不变（md5 全等）
>   —— 条目文件名补上 zip UTF-8 标记（原包全部条目未置位，Windows/部分解压工具下中文目录名显示为乱码）；可随时由 `markdown/` 重生成
>   —— **10-16 又修了一轮转换器的标题判定**：`pdf2md` 原来要求标题字号 ≥13.5pt，但很多英文手册的三~六级标题只排 9.8/10.9pt，`junk()` 还会把这类小字号书签同名行当目录残留**整行删掉**；另有 API 手册把编号与标题排成两行（`1.5.2.` 独占一行）而认不出。现在：能与 PDF 书签编号对上的行一律按编号层级升为标题，编号独占一行时用书签标题合并补全
>   —— 分两轮重转（第一轮 65 本小字号深层标题、第二轮 55 本两行式编号），共 120 本重跑、**净 65 本内容变化**（重跑结果与已修好的相同则不变）；英文 613 本现计 **48,504** 个带编号标题，ToC 编号在正文未命中从千余条降到 **10 条**（0.021%）；无一册正文体量缩小 >3%，抽样核对无标题丢失/误升
> - 云端 OSS 副本**落后且无凭证可更新**（AK 已禁用、预签名链接 2026-09-20 过期）
> - 复查新版：`python3 工具/list_docs.py --langs en --out ../../.scratch/en_all.json` → 再 `python3 工具/release_batch.py --manifest ... --version V3.16.2`（已登记的本会自动跳过）
> - 交付物 ``ApsaraStack-V3.18.6_2607-Release-Note-EN.md`（149 KB / 1,535 行）= **最新一版**，基线 V3.18.6 → V3.18.6_2607，162 对逐册细节差异 + 43 处配额变化 + 13 本产品自写 release notes 原文；尚未投递邮件
> - 旧版 `ApsaraStack-3.18.6-Release-Note-EN.md`（V3.16.2 → V3.18.6 口径）保留作为历史，**已发送到本人工作邮箱（地址已脱敏）**：sendStatus success，messageId `DzzzzzzNqZv`

> 英文 PDF ↔ Markdown 的对应关系统一以 `文档缓存索引.csv` 为准（`pdfCloud` = PDF 所在云端包，`localPath` = 登记路径，`markdown` = 已转出的 md）。

两套内容分开看：**中文 296 册 / 英文 613 册 Markdown**。PDF 不在本地保留：中文原件在云端 `apsara-docs/zips/`（13 包），英文在 `apsara-docs/zips_en/`（8 包，本地 markdown 对应的只是其中 4 包范围）。

- 企业版：stack 版本 **v3.18.6（20260730）**，册内实际标注 `产品版本 v3.18.6-SP2607`，`文档版本 202607xx–202608xx`（各册独立更新）
- AI Stack：stack 版本 **v2.17.0（20260828）**，册内标注 `V2.17.0`，OpenTrek 的 Agent Dev 与 AI Studio 标准版
- 来源：阿里云专有云帮助中心（help.aliyun.com/apsara）官方 PDF 直链；全部校验 `%PDF` 头、长度与页数，0 失败


## 目录结构

```
apsara-stack-docs/
├── 01_专有云企业版_v3.18.6_20260730/<服务域>/<产品code 产品名>/<序号>_<手册名>_<手册code>.pdf
├── 02_AIStack_v2.17.0_20260828_OpenTrek/人工智能/...
├── README.md · index.csv · manifest.json · 00_产品清单_全量待选.md
```

机器可读：`文档索引.csv`（Excel 直开，含原始链接/页数/版本）、`文档明细.json`。

---

## 01_专有云企业版_v3.18.6_20260730

290 本 · 46 个产品 · 1514 MB · 41,406 页


### 专有云云平台

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 全栈云平台 `apsarabase` | [专有云平台企业版安全白皮书](<01_专有云企业版_v3.18.6_20260730/专有云云平台/apsarabase 全栈云平台/02_专有云平台企业版安全白皮书_private-cloud-platform-enterprise-edition-security-white-paper.pdf>) | 53 | 3.5 MB | 20260729 |
| 全栈云平台 `apsarabase` | [高可用白皮书](<01_专有云企业版_v3.18.6_20260730/专有云云平台/apsarabase 全栈云平台/03_高可用白皮书_a3f70c8.pdf>) | 42 | 2.9 MB | 20260729 |
| 全栈云平台 `apsarabase` | [多Region技术白皮书](<01_专有云企业版_v3.18.6_20260730/专有云云平台/apsarabase 全栈云平台/04_多Region技术白皮书_a2c6b57.pdf>) | 32 | 2.3 MB | 20260729 |
| 全栈云平台 `apsarabase` | [License指南](<01_专有云企业版_v3.18.6_20260730/专有云云平台/apsarabase 全栈云平台/05_License指南_license-guide.pdf>) | 73 | 0.7 MB | 20260729 |
| 全栈云平台 `apsarabase` | [数据中心机房要求](<01_专有云企业版_v3.18.6_20260730/专有云云平台/apsarabase 全栈云平台/07_数据中心机房要求_idc.pdf>) | 12 | 0.3 MB | 20260729 |
| 全栈云平台 `apsarabase` | [专有云术语表](<01_专有云企业版_v3.18.6_20260730/专有云云平台/apsarabase 全栈云平台/08_专有云术语表_apsara-stack-glossary.pdf>) | 83 | 1.0 MB | 20260729 |


### 云原生服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| API 网关 `apigateway` | [API网关 产品简介](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/13_API网关 产品简介_apigateway2.pdf>) | 13 | 0.9 MB | 20260729 |
| API 网关 `apigateway` | [API网关 用户指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/15_API网关 用户指南_csb-2-0-user-guide.pdf>) | 173 | 12.5 MB | 20260729 |
| API 网关 `apigateway` | [API网关 开发指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/18_API网关 开发指南_ai-gateway-development-guide.pdf>) | 333 | 3.1 MB | 20260729 |
| API 网关 `apigateway` | [API网关 运维指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/21_API网关 运维指南_api-gateway-operation-guide.pdf>) | 11 | 1.3 MB | 20260729 |
| API 网关 `apigateway` | [API网关（旧）产品简介](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/22_API网关（旧）产品简介_product-introduction.pdf>) | 9 | 0.3 MB | 20260729 |
| API 网关 `apigateway` | [API网关（旧）用户指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/25_API网关（旧）用户指南_user-guide-ascm.pdf>) | 88 | 5.1 MB | 20260729 |
| API 网关 `apigateway` | [API网关（旧）开发指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/26_API网关（旧）开发指南_apsara-developer-guide.pdf>) | 174 | 2.4 MB | 20260729 |
| API 网关 `apigateway` | [API网关（旧）运维指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/27_API网关（旧）运维指南_apsara-operation-guide.pdf>) | 12 | 0.5 MB | 20260729 |
| API 网关 `apigateway` | [云原生网关 产品简介](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/33_云原生网关 产品简介_product-introduction-2.pdf>) | 11 | 0.3 MB | 20260729 |
| API 网关 `apigateway` | [云原生网关 用户指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/apigateway API 网关/34_云原生网关 用户指南_user-guide-1.pdf>) | 156 | 6.2 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [RocketMQ产品简介](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/19_RocketMQ产品简介_apsarastack-product-introduction.pdf>) | 23 | 2.4 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [RocketMQ用户指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/21_RocketMQ用户指南_rocketmq-apsarastack-user-guide.pdf>) | 312 | 6.5 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [RocketMQ开发指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/22_RocketMQ开发指南_rocketmq-apsarastack-developer-guide.pdf>) | 343 | 5.2 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [RocketMQ运维指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/23_RocketMQ运维指南_rocketmq-apsarastack-operation-guide.pdf>) | 54 | 1.2 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [MQTT产品简介](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/28_MQTT产品简介_apsaratack-product-introduction.pdf>) | 16 | 0.3 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [MQTT用户指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/32_MQTT用户指南_apsarastack-user-guide.pdf>) | 35 | 0.8 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [MQTT开发指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/33_MQTT开发指南_apsarastack-developer-guide.pdf>) | 36 | 2.2 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [MQTT运维指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/34_MQTT运维指南_apsarastack-operation-guide.pdf>) | 38 | 2.3 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [RocketMQ v5.0 产品简介](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/35_RocketMQ v5.0 产品简介_rocketmq-v5-0-product-brief.pdf>) | 20 | 2.4 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [RocketMQ v5.0 用户指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/36_RocketMQ v5.0 用户指南_rocketmq-v5-0-user-guide.pdf>) | 150 | 4.0 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [RocketMQ v5.0 开发指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/37_RocketMQ v5.0 开发指南_rocketmq-v5-0-development-guide.pdf>) | 169 | 3.9 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [MQTT v5.0 产品简介](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/38_MQTT v5.0 产品简介_mqtt-v5-0-product-brief.pdf>) | 16 | 0.3 MB | 20260729 |
| 云消息队列 RocketMQ 版 `rocketmq` | [MQTT v5.0 用户指南](<01_专有云企业版_v3.18.6_20260730/云原生服务/rocketmq 云消息队列 RocketMQ 版/39_MQTT v5.0 用户指南_mqtt-v5-0-user-guide.pdf>) | 47 | 1.0 MB | 20260729 |


### 交付服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 专有云部署服务 `asdelivery` | [部署指南](<01_专有云企业版_v3.18.6_20260730/交付服务/asdelivery 专有云部署服务/01_部署指南_same.pdf>) | 569 | 105.7 MB | 20260729 |
| 专有云部署服务 `asdelivery` | [JOK版本说明书](<01_专有云企业版_v3.18.6_20260730/交付服务/asdelivery 专有云部署服务/02_JOK版本说明书_jok-version-instruction.pdf>) | 5 | 0.2 MB | 20260729 |
| 专有云部署服务 `asdelivery` | [JOK部署指南](<01_专有云企业版_v3.18.6_20260730/交付服务/asdelivery 专有云部署服务/03_JOK部署指南_jok-deployment-guide.pdf>) | 12 | 3.1 MB | 20260729 |
| 专有云部署服务 `asdelivery` | [JOK使用指南](<01_专有云企业版_v3.18.6_20260730/交付服务/asdelivery 专有云部署服务/04_JOK使用指南_jok-use-guide.pdf>) | 21 | 8.8 MB | 20260729 |
| 专有云部署服务 `asdelivery` | [ASI使用指南](<01_专有云企业版_v3.18.6_20260730/交付服务/asdelivery 专有云部署服务/05_ASI使用指南_delivery-services.pdf>) | 49 | 4.6 MB | 20260729 |
| 专有云部署服务 `asdelivery` | [ASI部署指南](<01_专有云企业版_v3.18.6_20260730/交付服务/asdelivery 专有云部署服务/06_ASI部署指南_empty-manual.pdf>) | 8 | 1.6 MB | 20260729 |
| 专有云部署服务 `asdelivery` | [钟馗使用指南](<01_专有云企业版_v3.18.6_20260730/交付服务/asdelivery 专有云部署服务/07_钟馗使用指南_zhong-kui-use-guide.pdf>) | 14 | 3.3 MB | 20260729 |
| 专有云部署服务 `asdelivery` | [钟馗版本说明书](<01_专有云企业版_v3.18.6_20260730/交付服务/asdelivery 专有云部署服务/08_钟馗版本说明书_zhong-kui-version-instruction.pdf>) | 6 | 0.2 MB | 20260729 |


### 人工智能

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 智能体工厂 OpenTrek `opentrek` | [AgentRuntime产品简介](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/02_AgentRuntime产品简介_agent-runtime-apsarastack-product-introduction.pdf>) | 13 | 0.3 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [AgentRuntime用户指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/03_AgentRuntime用户指南_agent-runtime-apsarastack-user-guide.pdf>) | 57 | 1.8 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [AI网关 产品简介](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/04_AI网关 产品简介_product-introduction-1.pdf>) | 19 | 2.3 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [AI网关 用户指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/05_AI网关 用户指南_user-guide.pdf>) | 329 | 10.5 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [AI Studio 产品简介](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/08_AI Studio 产品简介_product-introduction-2.pdf>) | 12 | 0.3 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [AI Studio 用户指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/10_AI Studio 用户指南_aistudio-enterprise-user-guide.pdf>) | 254 | 24.5 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [AI Studio 开发指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/11_AI Studio 开发指南_ai-studio-development-guide-2.pdf>) | 931 | 6.9 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [AI Studio 运维指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/12_AI Studio 运维指南_operation-and-maintenance-guide-1.pdf>) | 97 | 24.4 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [OpenTrek-Ops产品简介](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/25_OpenTrek-Ops产品简介_aop-agentops-product-brief.pdf>) | 12 | 0.3 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [OpenTrek-Ops用户指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/28_OpenTrek-Ops用户指南_aop-agentops-user-guide.pdf>) | 62 | 3.6 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [HiMarket产品简介](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/31_HiMarket产品简介_himarket-product-introduction-1.pdf>) | 15 | 0.3 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [HiMarket用户指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/32_HiMarket用户指南_himarket-user-guide-1.pdf>) | 88 | 2.5 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [HiMarket开发指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/33_HiMarket开发指南_himarket-development-guide-1.pdf>) | 670 | 5.5 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [Agent Dev产品简介](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/34_Agent Dev产品简介_op-agent-dev-enterprise-product-introduction.pdf>) | 27 | 0.8 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [Agent Dev用户指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/36_Agent Dev用户指南_op-agent-dev-enterprise-user-guide.pdf>) | 103 | 1.8 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [Agent Dev开发指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/37_Agent Dev开发指南_op-agent-dev-enterprise-developer-guide.pdf>) | 258 | 3.7 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [Agent Dev运维指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/38_Agent Dev运维指南_op-agent-dev-enterprise-operation-guide.pdf>) | 82 | 50.5 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [AI网关 开发指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/42_AI网关 开发指南_ai-gateway-development-guide-1.pdf>) | 413 | 4.1 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [OpenTrek-UniOperator 产品简介](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/43_OpenTrek-UniOperator 产品简介_unified-operation-and-maintenance-platform-lightweight-edition-product-brief-v0-1-0.pdf>) | 11 | 0.3 MB | 20260729 |
| 智能体工厂 OpenTrek `opentrek` | [OpenTrek-UniOperator 用户指南](<01_专有云企业版_v3.18.6_20260730/人工智能/opentrek 智能体工厂 OpenTrek/45_OpenTrek-UniOperator 用户指南_unified-operations-platform-lightweight-edition-user-guide-v0-1-0.pdf>) | 42 | 2.4 MB | 20260729 |


### 大数据服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| DataWorks `dide` | [产品简介](<01_专有云企业版_v3.18.6_20260730/大数据服务/dide DataWorks/01_产品简介_enterprise-ascm-product-introduction-new.pdf>) | 35 | 1.4 MB | 20260729 |
| DataWorks `dide` | [用户指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/dide DataWorks/05_用户指南_enterprise-ascm-user-guide.pdf>) | 1516 | 50.9 MB | 20260729 |
| DataWorks `dide` | [开发指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/dide DataWorks/06_开发指南_enterprise-ascm-developer-guide.pdf>) | 884 | 5.7 MB | 20260729 |
| DataWorks `dide` | [运维指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/dide DataWorks/07_运维指南_enterprise-ascm-operation-guide.pdf>) | 123 | 10.3 MB | 20260729 |
| 实时数仓 Hologres `hologram` | [产品简介](<01_专有云企业版_v3.18.6_20260730/大数据服务/hologram 实时数仓 Hologres/01_产品简介_apsarastack-product-introduction.pdf>) | 9 | 0.3 MB | 20260729 |
| 实时数仓 Hologres `hologram` | [用户指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/hologram 实时数仓 Hologres/06_用户指南_enterprise-ascm-user-guide.pdf>) | 312 | 15.1 MB | 20260831 |
| 实时数仓 Hologres `hologram` | [开发指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/hologram 实时数仓 Hologres/07_开发指南_development-manual.pdf>) | 262 | 7.6 MB | 20260729 |
| 实时数仓 Hologres `hologram` | [运维指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/hologram 实时数仓 Hologres/08_运维指南_apsarastack-operation-guide.pdf>) | 100 | 7.0 MB | 20260729 |
| 大数据计算服务 `odps` | [产品简介](<01_专有云企业版_v3.18.6_20260730/大数据服务/odps 大数据计算服务/01_产品简介_enterprise-product-introduction.pdf>) | 24 | 0.9 MB | 20260729 |
| 大数据计算服务 `odps` | [用户指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/odps 大数据计算服务/06_用户指南_enterprise-ascm-user-guide.pdf>) | 395 | 11.8 MB | 20260729 |
| 大数据计算服务 `odps` | [开发指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/odps 大数据计算服务/07_开发指南_enterprise-ascm-developer-guide.pdf>) | 511 | 8.0 MB | 20260729 |
| 大数据计算服务 `odps` | [运维指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/odps 大数据计算服务/10_运维指南_enterprise-operation-guide.pdf>) | 143 | 7.6 MB | 20260729 |
| Quick BI `quickbi` | [产品简介](<01_专有云企业版_v3.18.6_20260730/大数据服务/quickbi Quick BI/01_产品简介_apsarastack-product-introduction.pdf>) | 7 | 0.3 MB | 20260729 |
| Quick BI `quickbi` | [用户指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/quickbi Quick BI/05_用户指南_apsarastack-user-guide.pdf>) | 351 | 18.8 MB | 20260729 |
| Quick BI `quickbi` | [开发指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/quickbi Quick BI/06_开发指南_development-guide.pdf>) | 220 | 1.6 MB | 20260729 |
| Quick BI `quickbi` | [运维指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/quickbi Quick BI/07_运维指南_apsarastack-operation-guide.pdf>) | 29 | 1.7 MB | 20260729 |
| 实时计算（流计算） `sc` | [ 产品简介（Blink）](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/01_产品简介（Blink）_enterprise-ase-paas-product-introduction.pdf>) | 10 | 0.3 MB | 20260729 |
| 实时计算（流计算） `sc` | [用户指南（Blink）](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/04_用户指南（Blink）_enterprise-user-guide.pdf>) | 58 | 2.9 MB | 20260729 |
| 实时计算（流计算） `sc` | [开发指南（Blink）](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/05_开发指南（Blink）_enterprise-developer-guide.pdf>) | 246 | 5.0 MB | 20260729 |
| 实时计算（流计算） `sc` | [运维指南（Blink）](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/06_运维指南（Blink）_enterprise-operation-guide.pdf>) | 47 | 3.0 MB | 20260729 |
| 实时计算（流计算） `sc` | [Flink企业版 产品简介](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/08_Flink企业版 产品简介_product-introduction.pdf>) | 9 | 0.3 MB | 20260729 |
| 实时计算（流计算） `sc` | [Flink企业版 用户指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/11_Flink企业版 用户指南_user-guide.pdf>) | 107 | 9.3 MB | 20260729 |
| 实时计算（流计算） `sc` | [Flink企业版 开发指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/12_Flink企业版 开发指南_development-guide.pdf>) | 532 | 4.7 MB | 20260729 |
| 实时计算（流计算） `sc` | [Flink企业版 运维指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/13_Flink企业版 运维指南_o-m-guide.pdf>) | 55 | 4.4 MB | 20260729 |
| 实时计算（流计算） `sc` | [Flink存算分离版 产品简介](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/16_Flink存算分离版 产品简介_product-introduction-1.pdf>) | 10 | 0.3 MB | 20260729 |
| 实时计算（流计算） `sc` | [Flink存算分离版 用户指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/19_Flink存算分离版 用户指南_empty-manual.pdf>) | 129 | 16.8 MB | 20260730 |
| 实时计算（流计算） `sc` | [Flink存算分离版 开发指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/20_Flink存算分离版 开发指南_development-guide-flink-storage-and-computing-separated-version.pdf>) | 746 | 5.9 MB | 20260730 |
| 实时计算（流计算） `sc` | [Flink存算分离版 运维指南](<01_专有云企业版_v3.18.6_20260730/大数据服务/sc 实时计算（流计算）/21_Flink存算分离版 运维指南_operation-and-maintenance-guide.pdf>) | 50 | 4.8 MB | 20260729 |


### 存储服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 混合云存储CDS `hcs_hgw` | [产品简介](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/01_产品简介_product-introduction.pdf>) | 37 | 0.7 MB | 20260730 |
| 混合云存储CDS `hcs_hgw` | [用户指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/05_用户指南_test.pdf>) | 939 | 31.0 MB | 20260813 |
| 混合云存储CDS `hcs_hgw` | [开发指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/08_开发指南_development-guide.pdf>) | 1675 | 22.0 MB | 20260813 |
| 混合云存储CDS `hcs_hgw` | [运维指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/09_运维指南_o-m-guide-1.pdf>) | 327 | 4.3 MB | 20260730 |
| 混合云存储CDS `hcs_hgw` | [CPFS产品简介](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/43_CPFS产品简介_cpfs-product-introduction.pdf>) | 9 | 0.2 MB | 20260729 |
| 混合云存储CDS `hcs_hgw` | [CPFS用户指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/45_CPFS用户指南_user-guide1.pdf>) | 13 | 1.1 MB | 20260729 |
| 混合云存储CDS `hcs_hgw` | [CPFS开发指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/46_CPFS开发指南_cpfs-development-guide.pdf>) | 38 | 1.0 MB | 20260729 |
| 混合云存储CDS `hcs_hgw` | [CPFS运维指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/47_CPFS运维指南_cpfs-operation-and-maintenance-guide.pdf>) | 19 | 2.0 MB | 20260729 |
| 混合云存储CDS `hcs_hgw` | [APFS产品简介](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/52_APFS产品简介_product-introduction-3.pdf>) | 10 | 0.5 MB | 20260729 |
| 混合云存储CDS `hcs_hgw` | [APFS用户指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/54_APFS用户指南_user-guide-2.pdf>) | 18 | 0.5 MB | 20260729 |
| 混合云存储CDS `hcs_hgw` | [APFS开发指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/55_APFS开发指南_development-guide-4.pdf>) | 53 | 1.2 MB | 20260729 |
| 混合云存储CDS `hcs_hgw` | [APFS运维指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/56_APFS运维指南_operation-and-maintenance-guide-1.pdf>) | 16 | 2.7 MB | 20260729 |
| 混合云存储CDS `hcs_hgw` | [EFS-NAS产品简介](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/61_EFS-NAS产品简介_efs-nas-product-introduction.pdf>) | 11 | 0.3 MB | 20260730 |
| 混合云存储CDS `hcs_hgw` | [EFS-NAS用户指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/63_EFS-NAS用户指南_efs-nas-user-guide.pdf>) | 43 | 1.5 MB | 20260730 |
| 混合云存储CDS `hcs_hgw` | [EFS-NAS开发指南](<01_专有云企业版_v3.18.6_20260730/存储服务/hcs_hgw 混合云存储CDS/64_EFS-NAS开发指南_efs-nas-development-guide.pdf>) | 91 | 1.8 MB | 20260729 |
| 文件存储NAS `nas` | [产品简介](<01_专有云企业版_v3.18.6_20260730/存储服务/nas 文件存储NAS/03_产品简介_enterprise-product-introduction.pdf>) | 8 | 0.3 MB | 20260729 |
| 文件存储NAS `nas` | [用户指南](<01_专有云企业版_v3.18.6_20260730/存储服务/nas 文件存储NAS/06_用户指南_enterprise-ascm-user-guide.pdf>) | 61 | 3.9 MB | 20260729 |
| 文件存储NAS `nas` | [开发指南](<01_专有云企业版_v3.18.6_20260730/存储服务/nas 文件存储NAS/07_开发指南_enterprise-developer-guide.pdf>) | 120 | 2.0 MB | 20260729 |
| 文件存储NAS `nas` | [运维指南](<01_专有云企业版_v3.18.6_20260730/存储服务/nas 文件存储NAS/08_运维指南_enterprise-operation-guide.pdf>) | 34 | 1.8 MB | 20260729 |
| 对象存储 `oss` | [产品简介](<01_专有云企业版_v3.18.6_20260730/存储服务/oss 对象存储/01_产品简介_ascm-enterprise-product-introduction.pdf>) | 13 | 0.3 MB | 20260729 |
| 对象存储 `oss` | [用户指南](<01_专有云企业版_v3.18.6_20260730/存储服务/oss 对象存储/05_用户指南_ascm-enterprise-user-guide.pdf>) | 79 | 1.2 MB | 20260729 |
| 对象存储 `oss` | [开发指南](<01_专有云企业版_v3.18.6_20260730/存储服务/oss 对象存储/06_开发指南_ascm-enterprise-developer-guide.pdf>) | 588 | 4.9 MB | 20260813 |
| 对象存储 `oss` | [运维指南](<01_专有云企业版_v3.18.6_20260730/存储服务/oss 对象存储/07_运维指南_ascm-enterprise-operation-guide.pdf>) | 93 | 2.1 MB | 20260729 |


### 安全服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 云安全中心（安骑士） `aegis` | [安骑士产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/aegis 云安全中心（安骑士）/21_安骑士产品简介_product-introduction.pdf>) | 40 | 0.6 MB | 20260729 |
| 云安全中心（安骑士） `aegis` | [安骑士用户指南（ascm）](<01_专有云企业版_v3.18.6_20260730/安全服务/aegis 云安全中心（安骑士）/23_安骑士用户指南（ascm）_server-guard-user-guide.pdf>) | 269 | 5.2 MB | 20260729 |
| 云安全中心（安骑士） `aegis` | [安骑士开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/aegis 云安全中心（安骑士）/24_安骑士开发指南_server-guard-development-guide.pdf>) | 251 | 2.4 MB | 20260729 |
| 云安全中心（安骑士） `aegis` | [安骑士运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/aegis 云安全中心（安骑士）/25_安骑士运维指南_server-guard-operation-and-maintenance-guide.pdf>) | 106 | 7.7 MB | 20260729 |
| 云安全中心（安骑士） `aegis` | [容器安全产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/aegis 云安全中心（安骑士）/32_容器安全产品简介_introduction-to-container-safety-products.pdf>) | 25 | 0.6 MB | 20260729 |
| 云安全中心（安骑士） `aegis` | [容器安全用户指南](<01_专有云企业版_v3.18.6_20260730/安全服务/aegis 云安全中心（安骑士）/34_容器安全用户指南_container-security-user-guide.pdf>) | 58 | 1.6 MB | 20260729 |
| 云安全中心（安骑士） `aegis` | [容器安全开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/aegis 云安全中心（安骑士）/35_容器安全开发指南_container-security-development-guide.pdf>) | 180 | 1.8 MB | 20260729 |
| 云安全中心（安骑士） `aegis` | [容器安全运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/aegis 云安全中心（安骑士）/36_容器安全运维指南_container-security-operation-and-maintenance-guide.pdf>) | 45 | 0.7 MB | 20260729 |
| SSL证书（CA证书服务、数据安全） `cas` | [数字证书管理服务（租户侧）产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/cas SSL证书（CA证书服务、数据安全）/01_数字证书管理服务（租户侧）产品简介_product-introduction-1.pdf>) | 8 | 0.3 MB | 20260729 |
| SSL证书（CA证书服务、数据安全） `cas` | [数字证书管理服务（租户侧）用户指南](<01_专有云企业版_v3.18.6_20260730/安全服务/cas SSL证书（CA证书服务、数据安全）/03_数字证书管理服务（租户侧）用户指南_user-guide.pdf>) | 17 | 0.7 MB | 20260729 |
| SSL证书（CA证书服务、数据安全） `cas` | [数字证书管理服务（租户侧）运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/cas SSL证书（CA证书服务、数据安全）/04_数字证书管理服务（租户侧）运维指南_operation-and-maintenance-guide.pdf>) | 15 | 7.0 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据库安全审计产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/30_数据库安全审计产品简介_product-introduction-1.pdf>) | 12 | 0.3 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据库安全审计用户指南](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/32_数据库安全审计用户指南_database-guide-user-guide.pdf>) | 115 | 24.3 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据库安全审计开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/33_数据库安全审计开发指南_database-audit-development-guide.pdf>) | 100 | 1.9 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据库安全审计运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/34_数据库安全审计运维指南_database-audit-operations-guide.pdf>) | 27 | 2.5 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据静态脱敏与水印产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/40_数据静态脱敏与水印产品简介_introduction-of-data-sorting-and-desensitization-products.pdf>) | 14 | 0.3 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据静态脱敏与水印用户指南](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/42_数据静态脱敏与水印用户指南_data-sorting-and-desensitization-system-user-guide.pdf>) | 134 | 21.6 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据静态脱敏与水印运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/43_数据静态脱敏与水印运维指南_data-sorting-and-desensitization-system-operation-and-maintenance-guide.pdf>) | 20 | 2.6 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据库审计与风险控制产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/49_数据库审计与风险控制产品简介_product-introduction.pdf>) | 17 | 0.4 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据库审计与风险控制用户指南](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/51_数据库审计与风险控制用户指南_user-guide.pdf>) | 113 | 12.2 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据库审计与风险控制开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/52_数据库审计与风险控制开发指南_database-audit-and-risk-control-system-development-guide.pdf>) | 222 | 2.5 MB | 20260729 |
| 数据库审计 `dbaudit` | [数据库审计与风险控制运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/dbaudit 数据库审计/53_数据库审计与风险控制运维指南_operation-and-maintenance-guide.pdf>) | 45 | 2.8 MB | 20260729 |
| 加密服务 `hsm` | [加密服务（租户侧）产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/hsm 加密服务/01_加密服务（租户侧）产品简介_product-introduction-encryption-service-control-tenant-side.pdf>) | 9 | 0.4 MB | 20260729 |
| 加密服务 `hsm` | [加密服务管控（租户侧）用户指南](<01_专有云企业版_v3.18.6_20260730/安全服务/hsm 加密服务/05_加密服务管控（租户侧）用户指南_cryptographic-service-user-guide.pdf>) | 18 | 1.1 MB | 20260729 |
| 加密服务 `hsm` | [加密服务管控（租户侧）开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/hsm 加密服务/06_加密服务管控（租户侧）开发指南_developer-guide.pdf>) | 112 | 1.8 MB | 20260729 |
| 加密服务 `hsm` | [加密服务管控（租户侧）运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/hsm 加密服务/07_加密服务管控（租户侧）运维指南_encryption-service-operation-and-maintenance-guide.pdf>) | 36 | 3.8 MB | 20260729 |
| 密钥管理服务 `kms` | [密码服务产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/kms 密钥管理服务/01_密码服务产品简介_password-service-product-brief.pdf>) | 12 | 0.3 MB | 20260729 |
| 密钥管理服务 `kms` | [密码服务用户指南](<01_专有云企业版_v3.18.6_20260730/安全服务/kms 密钥管理服务/03_密码服务用户指南_password-service-user-guide.pdf>) | 19 | 0.7 MB | 20260729 |
| 密钥管理服务 `kms` | [密码服务运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/kms 密钥管理服务/04_密码服务运维指南_password-service-operation-and-maintenance-guide.pdf>) | 8 | 0.7 MB | 20260729 |
| 密钥管理服务 `kms` | [密钥管理服务产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/kms 密钥管理服务/08_密钥管理服务产品简介_enterprise-ascm-product-introduction.pdf>) | 9 | 0.2 MB | 20260729 |
| 密钥管理服务 `kms` | [密钥管理服务用户指南](<01_专有云企业版_v3.18.6_20260730/安全服务/kms 密钥管理服务/10_密钥管理服务用户指南_enterprise-ascm-user-guide.pdf>) | 49 | 1.4 MB | 20260729 |
| 密钥管理服务 `kms` | [密钥管理服务开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/kms 密钥管理服务/11_密钥管理服务开发指南_enterprise-ascm-developer-guide.pdf>) | 127 | 2.2 MB | 20260729 |
| 密钥管理服务 `kms` | [密钥管理服务运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/kms 密钥管理服务/12_密钥管理服务运维指南_enterprise-ascm-operation-guide.pdf>) | 24 | 1.4 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [云安全管理中心产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/33_云安全管理中心产品简介_cloud-security-management-center-product-introduction.pdf>) | 23 | 0.3 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [云安全管理中心用户指南（ascm）](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/35_云安全管理中心用户指南（ascm）_cloud-security-management-center-user-guide.pdf>) | 62 | 4.6 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [云安全管理中心开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/36_云安全管理中心开发指南_developer-guide.pdf>) | 262 | 2.9 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [云安全管理中心运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/37_云安全管理中心运维指南_cloud-security-management-center-operation-and-maintenance-guide.pdf>) | 13 | 1.3 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [漏洞扫描产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/43_漏洞扫描产品简介_product-introduction.pdf>) | 11 | 0.3 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [漏洞扫描用户指南（ascm）](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/44_漏洞扫描用户指南（ascm）_vulnerability-scan-user-guide.pdf>) | 51 | 3.0 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [漏洞扫描开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/45_漏洞扫描开发指南_empty-manual-1.pdf>) | 215 | 2.5 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [漏洞扫描运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/46_漏洞扫描运维指南_vulnerability-scanning-operations-guide.pdf>) | 17 | 1.1 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [安全响应自动化编排产品简介](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/52_安全响应自动化编排产品简介_security-response-automation-orchestration-product-brief.pdf>) | 13 | 0.3 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [安全编排自动化响应用户指南（ascm）](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/54_安全编排自动化响应用户指南（ascm）_secure-automatic-orchestration-response-user-guide.pdf>) | 45 | 1.5 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [安全编排自动化响应开发指南](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/55_安全编排自动化响应开发指南_security-orchestration-automation-response-development-guide.pdf>) | 76 | 1.9 MB | 20260729 |
| 云安全中心（态势感知） `sas` | [安全编排自动化响应运维指南](<01_专有云企业版_v3.18.6_20260730/安全服务/sas 云安全中心（态势感知）/56_安全编排自动化响应运维指南_security-automatic-orchestration-response-operation-and-maintenance-guide.pdf>) | 10 | 1.8 MB | 20260729 |
| 云盾 `yundun` | [安全管理员指南](<01_专有云企业版_v3.18.6_20260730/安全服务/yundun 云盾/01_安全管理员指南_enterprise-security-admin-guide.pdf>) | 105 | 5.2 MB | 20260729 |
| 云盾 `yundun` | [云盾系统配置](<01_专有云企业版_v3.18.6_20260730/安全服务/yundun 云盾/02_云盾系统配置_apsara-stack-security-system-configuration.pdf>) | 22 | 0.8 MB | 20260729 |


### 应用服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 日志服务 `sls` | [产品简介](<01_专有云企业版_v3.18.6_20260730/应用服务/sls 日志服务/03_产品简介_enterprise-ascm-product-introduction.pdf>) | 12 | 0.6 MB | 20260729 |
| 日志服务 `sls` | [用户指南](<01_专有云企业版_v3.18.6_20260730/应用服务/sls 日志服务/06_用户指南_enterprise-ascm-user-guide.pdf>) | 707 | 20.9 MB | 20260813 |
| 日志服务 `sls` | [开发指南](<01_专有云企业版_v3.18.6_20260730/应用服务/sls 日志服务/07_开发指南_enterprise-ascm-developer-guide.pdf>) | 407 | 4.2 MB | 20260813 |
| 日志服务 `sls` | [运维指南](<01_专有云企业版_v3.18.6_20260730/应用服务/sls 日志服务/08_运维指南_enterprise-ascm-operation-guide.pdf>) | 23 | 0.7 MB | 20260729 |


### 数据库服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 数据库备份DBS `cbs` | [产品简介](<01_专有云企业版_v3.18.6_20260730/数据库服务/cbs 数据库备份DBS/01_产品简介_enterprise-product-introduction.pdf>) | 17 | 0.3 MB | 20260729 |
| 数据库备份DBS `cbs` | [用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/cbs 数据库备份DBS/05_用户指南_enterprise-user-guide.pdf>) | 48 | 1.2 MB | 20260729 |
| 数据库备份DBS `cbs` | [开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/cbs 数据库备份DBS/06_开发指南_enterprise-developer-guide.pdf>) | 96 | 0.9 MB | 20260729 |
| 数据库备份DBS `cbs` | [运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/cbs 数据库备份DBS/07_运维指南_o-m-manual.pdf>) | 13 | 1.1 MB | 20260729 |
| 数据管理DMS `dms` | [产品简介](<01_专有云企业版_v3.18.6_20260730/数据库服务/dms 数据管理DMS/01_产品简介_enterprise-ascm-product-introduction-enterprise.pdf>) | 15 | 0.3 MB | 20260729 |
| 数据管理DMS `dms` | [用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/dms 数据管理DMS/06_用户指南_enterprise-ascm-user-guide-enterprise.pdf>) | 198 | 5.7 MB | 20260729 |
| 数据管理DMS `dms` | [开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/dms 数据管理DMS/10_开发指南_enterprise-ascm-developer-guide.pdf>) | 399 | 3.7 MB | 20260729 |
| 数据传输服务DTS `dts` | [产品简介](<01_专有云企业版_v3.18.6_20260730/数据库服务/dts 数据传输服务DTS/01_产品简介_enterprise-ascm-product-introduction.pdf>) | 17 | 0.3 MB | 20260729 |
| 数据传输服务DTS `dts` | [用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/dts 数据传输服务DTS/05_用户指南_enterprise-ascm-user-guide.pdf>) | 520 | 5.2 MB | 20260729 |
| 数据传输服务DTS `dts` | [开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/dts 数据传输服务DTS/06_开发指南_enterprise-ascm-developer-guide.pdf>) | 493 | 4.7 MB | 20260729 |
| 数据传输服务DTS `dts` | [运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/dts 数据传输服务DTS/07_运维指南_enterprise-ascm-operation-guide.pdf>) | 34 | 1.8 MB | 20260729 |
| 数据库自治服务 `hdm` | [产品简介](<01_专有云企业版_v3.18.6_20260730/数据库服务/hdm 数据库自治服务/01_产品简介_enterprise-product-introduction.pdf>) | 14 | 0.3 MB | 20260729 |
| 数据库自治服务 `hdm` | [用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/hdm 数据库自治服务/04_用户指南_enterprise-user-guide.pdf>) | 45 | 3.5 MB | 20260729 |
| 数据库自治服务 `hdm` | [开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/hdm 数据库自治服务/05_开发指南_development-guide.pdf>) | 58 | 1.0 MB | 20260729 |
| 数据库自治服务 `hdm` | [运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/hdm 数据库自治服务/06_运维指南_enterprise-operation-guide.pdf>) | 13 | 0.7 MB | 20260729 |
| 云数据库 Tair（兼容 Redis） `kvstore` | [产品简介](<01_专有云企业版_v3.18.6_20260730/数据库服务/kvstore 云数据库 Tair（兼容 Redis）/14_产品简介_enterprise-product-introduction.pdf>) | 13 | 0.3 MB | 20260729 |
| 云数据库 Tair（兼容 Redis） `kvstore` | [用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/kvstore 云数据库 Tair（兼容 Redis）/16_用户指南_enterprise-user-guide.pdf>) | 159 | 2.6 MB | 20260729 |
| 云数据库 Tair（兼容 Redis） `kvstore` | [开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/kvstore 云数据库 Tair（兼容 Redis）/17_开发指南_enterprise-developer-guide.pdf>) | 104 | 1.9 MB | 20260729 |
| 云数据库 Tair（兼容 Redis） `kvstore` | [运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/kvstore 云数据库 Tair（兼容 Redis）/18_运维指南_enterprise-operation-guide.pdf>) | 295 | 16.7 MB | 20260729 |
| 云数据库MongoDB版 `mongodb` | [产品简介](<01_专有云企业版_v3.18.6_20260730/数据库服务/mongodb 云数据库MongoDB版/01_产品简介_enterprise-ascm-product-introduction.pdf>) | 13 | 0.3 MB | 20260729 |
| 云数据库MongoDB版 `mongodb` | [用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/mongodb 云数据库MongoDB版/05_用户指南_enterprise-ascm-user-guide.pdf>) | 139 | 3.8 MB | 20260729 |
| 云数据库MongoDB版 `mongodb` | [开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/mongodb 云数据库MongoDB版/06_开发指南_enterprise-ascm-developer-guide.pdf>) | 205 | 2.7 MB | 20260729 |
| 云数据库MongoDB版 `mongodb` | [运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/mongodb 云数据库MongoDB版/07_运维指南_enterprise-ascm-operation-guide.pdf>) | 284 | 15.3 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [产品简介](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/64_产品简介_product-introduction-3.pdf>) | 37 | 0.6 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB MySQL集群版 用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/67_PolarDB MySQL集群版 用户指南_user-guide.pdf>) | 242 | 10.1 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB MySQL集群版 开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/68_PolarDB MySQL集群版 开发指南_development-guide.pdf>) | 333 | 3.4 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB MySQL集群版 运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/69_PolarDB MySQL集群版 运维指南_operation-and-maintenance-guide.pdf>) | 279 | 15.5 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB MySQL主备版 用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/70_PolarDB MySQL主备版 用户指南_user-guide-2.pdf>) | 155 | 7.9 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB MySQL主备版 开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/71_PolarDB MySQL主备版 开发指南_development-guide-polardb-mysql-local-disk-version.pdf>) | 146 | 1.9 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB MySQL主备版 运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/72_PolarDB MySQL主备版 运维指南_operation-and-maintenance-guide-2.pdf>) | 292 | 15.7 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB PostgreSQL主备版 用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/76_PolarDB PostgreSQL主备版 用户指南_user-guide-polardb-postgresql-local-disk-version.pdf>) | 202 | 8.8 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB PostgreSQL主备版 开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/77_PolarDB PostgreSQL主备版 开发指南_development-guide-polardb-postgresql-local-disk-version.pdf>) | 148 | 1.9 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB PostgreSQL主备版 运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/78_PolarDB PostgreSQL主备版 运维指南_operation-guide-polardb-postgresql-local-disk-edition.pdf>) | 306 | 16.0 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB PostgreSQL集群共享存储版 用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/81_PolarDB PostgreSQL集群共享存储版 用户指南_user-guide-1.pdf>) | 163 | 7.8 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB PostgreSQL集群共享存储版 开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/82_PolarDB PostgreSQL集群共享存储版 开发指南_development-guide-1.pdf>) | 1175 | 13.0 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB PostgreSQL集群共享存储版 运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/83_PolarDB PostgreSQL集群共享存储版 运维指南_operation-and-maintenance-guide-1.pdf>) | 277 | 15.4 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB集分一体版 用户指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/86_PolarDB集分一体版 用户指南_user-guide-4.pdf>) | 194 | 7.9 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB集分一体版 开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/87_PolarDB集分一体版 开发指南_development-guide-2.pdf>) | 193 | 2.4 MB | 20260729 |
| 云原生关系型数据库 PolarDB `polardb` | [PolarDB集分一体版 运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/polardb 云原生关系型数据库 PolarDB/88_PolarDB集分一体版 运维指南_o-m-guide.pdf>) | 277 | 15.2 MB | 20260729 |
| 云数据库RDS `rds` | [产品简介](<01_专有云企业版_v3.18.6_20260730/数据库服务/rds 云数据库RDS/03_产品简介_enterprise-ascm-product-introduction.pdf>) | 34 | 0.8 MB | 20260729 |
| 云数据库RDS `rds` | [用户指南（RDS MySQL）](<01_专有云企业版_v3.18.6_20260730/数据库服务/rds 云数据库RDS/12_用户指南（RDS MySQL）_enterprise-user-guide-mysql.pdf>) | 146 | 4.6 MB | 20260729 |
| 云数据库RDS `rds` | [用户指南（RDS PostgreSQL）](<01_专有云企业版_v3.18.6_20260730/数据库服务/rds 云数据库RDS/13_用户指南（RDS PostgreSQL）_enterprise-user-guide-pg.pdf>) | 147 | 3.4 MB | 20260729 |
| 云数据库RDS `rds` | [用户指南（PolarDB）](<01_专有云企业版_v3.18.6_20260730/数据库服务/rds 云数据库RDS/14_用户指南（PolarDB）_enterprise-user-guide-polardb.pdf>) | 160 | 4.5 MB | 20260729 |
| 云数据库RDS `rds` | [开发指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/rds 云数据库RDS/15_开发指南_enterprise-ascm-developer-guide.pdf>) | 351 | 3.3 MB | 20260729 |
| 云数据库RDS `rds` | [运维指南](<01_专有云企业版_v3.18.6_20260730/数据库服务/rds 云数据库RDS/16_运维指南_enterprise-ascm-operation-guide.pdf>) | 305 | 15.9 MB | 20260729 |


### 统一运营平台

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 云迁移中心 `apds` | [产品简介](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apds 云迁移中心/01_产品简介_product-introduction.pdf>) | 10 | 0.3 MB | 20260729 |
| 云迁移中心 `apds` | [用户指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apds 云迁移中心/05_用户指南_user-guide.pdf>) | 144 | 53.1 MB | 20260729 |
| 云迁移中心 `apds` | [运维指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apds 云迁移中心/07_运维指南_operation-and-maintenance-guide.pdf>) | 49 | 3.1 MB | 20260729 |
| 统一云管平台 `apsara_stack_platform` | [统一云管平台 产品简介](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apsara_stack_platform 统一云管平台/22_统一云管平台 产品简介_apsara-uni-manager-product-introduction.pdf>) | 17 | 0.3 MB | 20260729 |
| 统一云管平台 `apsara_stack_platform` | [统一云管平台 用户指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apsara_stack_platform 统一云管平台/24_统一云管平台 用户指南_enterprise-user-guide.pdf>) | 1219 | 90.1 MB | 20260729 |
| 统一云管平台 `apsara_stack_platform` | [统一云管平台 开发指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apsara_stack_platform 统一云管平台/25_统一云管平台 开发指南_enterprise-developer-guide.pdf>) | 603 | 11.6 MB | 20260729 |
| 统一云管平台 `apsara_stack_platform` | [统一云管平台 运维指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apsara_stack_platform 统一云管平台/26_统一云管平台 运维指南_apsara-uni-manager-o-m-guide.pdf>) | 73 | 6.0 MB | 20260729 |
| 统一云管平台 `apsara_stack_platform` | [飞天助理 产品简介](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apsara_stack_platform 统一云管平台/39_飞天助理 产品简介_feitian-assistant-product-introduction.pdf>) | 8 | 0.6 MB | 20260729 |
| 统一云管平台 `apsara_stack_platform` | [飞天助理 用户指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apsara_stack_platform 统一云管平台/40_飞天助理 用户指南_feitian-assistant-user-guide.pdf>) | 72 | 7.4 MB | 20260729 |
| 统一云管平台 `apsara_stack_platform` | [飞天助理 开发指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/apsara_stack_platform 统一云管平台/41_飞天助理 开发指南_flying-assistant-development-guide.pdf>) | 53 | 1.2 MB | 20260729 |
| 灾备管理平台 `asr` | [灾备管理平台 产品简介](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/01_灾备管理平台 产品简介_product-introduction-of-disaster-recovery-management-platform-1.pdf>) | 24 | 1.1 MB | 20260729 |
| 灾备管理平台 `asr` | [同城容灾管理平台ASR 用户指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/03_同城容灾管理平台ASR 用户指南_asr-user-guide.pdf>) | 109 | 12.7 MB | 20260729 |
| 灾备管理平台 `asr` | [同城容灾ASR开发指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/04_同城容灾ASR开发指南_guide-to-the-development-of-disaster-recovery-in-the-same.pdf>) | 111 | 2.3 MB | 20260729 |
| 灾备管理平台 `asr` | [同城容灾管理平台ASR 运维指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/05_同城容灾管理平台ASR 运维指南_local-disaster-recovery-o-m-guide.pdf>) | 92 | 11.1 MB | 20260729 |
| 灾备管理平台 `asr` | [异地容灾管理平台ASR-DR 用户指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/13_异地容灾管理平台ASR-DR 用户指南_asrdr-user-guide.pdf>) | 201 | 12.7 MB | 20260729 |
| 灾备管理平台 `asr` | [异地容灾管理平台ASR-DR开发指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/14_异地容灾管理平台ASR-DR开发指南_development-guide-1.pdf>) | 183 | 1.7 MB | 20260729 |
| 灾备管理平台 `asr` | [异地容灾管理平台ASR-DR 运维指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/15_异地容灾管理平台ASR-DR 运维指南_asrdr-operation-guide.pdf>) | 125 | 11.7 MB | 20260729 |
| 灾备管理平台 `asr` | [备份管理平台ASR-BR用户指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/21_备份管理平台ASR-BR用户指南_user-guide.pdf>) | 279 | 15.8 MB | 20260729 |
| 灾备管理平台 `asr` | [备份管理平台ASR-BR开发指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/22_备份管理平台ASR-BR开发指南_development-guide.pdf>) | 362 | 3.7 MB | 20260729 |
| 灾备管理平台 `asr` | [备份管理平台ASR-BR运维指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/23_备份管理平台ASR-BR运维指南_empty-manual.pdf>) | 147 | 17.0 MB | 20260729 |
| 灾备管理平台 `asr` | [云平台备份用户指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/27_云平台备份用户指南_cloud-platform-backup-user-guide.pdf>) | 13 | 0.4 MB | 20260729 |
| 灾备管理平台 `asr` | [云平台备份运维指南](<01_专有云企业版_v3.18.6_20260730/统一运营平台/asr 灾备管理平台/28_云平台备份运维指南_cloud-platform-backup-operations-guide.pdf>) | 12 | 1.7 MB | 20260729 |


### 网络服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 专有云DNS `apsara_stack_dns` | [产品简介](<01_专有云企业版_v3.18.6_20260730/网络服务/apsara_stack_dns 专有云DNS/01_产品简介_enterprise-product-introduction.pdf>) | 13 | 0.3 MB | 20260729 |
| 专有云DNS `apsara_stack_dns` | [域名解析DNS（云内）用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/apsara_stack_dns 专有云DNS/04_域名解析DNS（云内）用户指南_enterprise-user-guide.pdf>) | 57 | 0.9 MB | 20260729 |
| 专有云DNS `apsara_stack_dns` | [域名解析DNS（跨云）用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/apsara_stack_dns 专有云DNS/05_域名解析DNS（跨云）用户指南_domain-name-resolution-dns-cross-cloud-user-guide.pdf>) | 16 | 0.4 MB | 20260729 |
| 专有云DNS `apsara_stack_dns` | [开发指南](<01_专有云企业版_v3.18.6_20260730/网络服务/apsara_stack_dns 专有云DNS/09_开发指南_enterprise-developer-guide.pdf>) | 222 | 3.1 MB | 20260729 |
| 专有云DNS `apsara_stack_dns` | [运维指南](<01_专有云企业版_v3.18.6_20260730/网络服务/apsara_stack_dns 专有云DNS/11_运维指南_enterprise-operation-guide.pdf>) | 20 | 1.7 MB | 20260729 |
| 云接入网关 `cgw` | [产品简介](<01_专有云企业版_v3.18.6_20260730/网络服务/cgw 云接入网关/01_产品简介_introduction.pdf>) | 16 | 0.6 MB | 20260729 |
| 云接入网关 `cgw` | [用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/cgw 云接入网关/05_用户指南_userguide.pdf>) | 38 | 2.7 MB | 20260729 |
| 云接入网关 `cgw` | [开发指南](<01_专有云企业版_v3.18.6_20260730/网络服务/cgw 云接入网关/06_开发指南_development-guide.pdf>) | 67 | 1.2 MB | 20260729 |
| 云接入网关 `cgw` | [运维指南](<01_专有云企业版_v3.18.6_20260730/网络服务/cgw 云接入网关/07_运维指南_o-m-guide.pdf>) | 152 | 14.0 MB | 20260729 |
| 高速通道 `expressconnect` | [产品简介](<01_专有云企业版_v3.18.6_20260730/网络服务/expressconnect 高速通道/01_产品简介_product-introduction.pdf>) | 8 | 0.3 MB | 20260729 |
| 高速通道 `expressconnect` | [用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/expressconnect 高速通道/05_用户指南_enterprise-user-guide.pdf>) | 47 | 0.7 MB | 20260729 |
| 高速通道 `expressconnect` | [开发指南](<01_专有云企业版_v3.18.6_20260730/网络服务/expressconnect 高速通道/06_开发指南_enterprise-developer-guide.pdf>) | 116 | 2.2 MB | 20260729 |
| 高速通道 `expressconnect` | [运维指南](<01_专有云企业版_v3.18.6_20260730/网络服务/expressconnect 高速通道/08_运维指南_operation-and-maintenance-guide.pdf>) | 76 | 5.8 MB | 20260729 |
| 转发路由器 `ntr` | [产品简介](<01_专有云企业版_v3.18.6_20260730/网络服务/ntr 转发路由器/01_产品简介_empty-manual.pdf>) | 8 | 0.2 MB | 20260729 |
| 转发路由器 `ntr` | [用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/ntr 转发路由器/03_用户指南_user-guide-1.pdf>) | 50 | 2.1 MB | 20260729 |
| 转发路由器 `ntr` | [开发指南](<01_专有云企业版_v3.18.6_20260730/网络服务/ntr 转发路由器/04_开发指南_development-guide.pdf>) | 137 | 1.7 MB | 20260729 |
| 转发路由器 `ntr` | [运维指南](<01_专有云企业版_v3.18.6_20260730/网络服务/ntr 转发路由器/05_运维指南_operation-and-maintenance-guide.pdf>) | 11 | 0.9 MB | 20260729 |
| 负载均衡 `slb` | [产品简介](<01_专有云企业版_v3.18.6_20260730/网络服务/slb 负载均衡/01_产品简介_enterprise-product-introduction.pdf>) | 17 | 0.3 MB | 20260729 |
| 负载均衡 `slb` | [用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/slb 负载均衡/05_用户指南_enterprise-user-guide-1.pdf>) | 104 | 2.2 MB | 20260729 |
| 负载均衡 `slb` | [开发指南](<01_专有云企业版_v3.18.6_20260730/网络服务/slb 负载均衡/06_开发指南_enterprise-developer-guide.pdf>) | 206 | 3.3 MB | 20260729 |
| 负载均衡 `slb` | [运维指南](<01_专有云企业版_v3.18.6_20260730/网络服务/slb 负载均衡/07_运维指南_operation-and-maintenance-guide.pdf>) | 37 | 2.7 MB | 20260729 |
| 负载均衡 `slb` | [ALB产品简介](<01_专有云企业版_v3.18.6_20260730/网络服务/slb 负载均衡/08_ALB产品简介_alb-product-brief.pdf>) | 18 | 0.3 MB | 20260729 |
| 负载均衡 `slb` | [应用型负载均衡ALB用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/slb 负载均衡/10_应用型负载均衡ALB用户指南_alb-user-guide.pdf>) | 117 | 2.0 MB | 20260729 |
| 专有网络VPC `vpc` | [产品简介](<01_专有云企业版_v3.18.6_20260730/网络服务/vpc 专有网络VPC/01_产品简介_enterprise-product-introduction.pdf>) | 14 | 0.3 MB | 20260729 |
| 专有网络VPC `vpc` | [用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/vpc 专有网络VPC/05_用户指南_enterprise-user-guide.pdf>) | 135 | 1.9 MB | 20260729 |
| 专有网络VPC `vpc` | [开发指南](<01_专有云企业版_v3.18.6_20260730/网络服务/vpc 专有网络VPC/06_开发指南_enterprise-developer-guide.pdf>) | 258 | 4.2 MB | 20260729 |
| 专有网络VPC `vpc` | [运维指南](<01_专有云企业版_v3.18.6_20260730/网络服务/vpc 专有网络VPC/09_运维指南_operation-and-maintenance-guide.pdf>) | 187 | 19.4 MB | 20260729 |
| VPN网关 `vpn` | [产品简介](<01_专有云企业版_v3.18.6_20260730/网络服务/vpn VPN网关/01_产品简介_product-introduction-manual-refactoring.pdf>) | 7 | 0.2 MB | 20260729 |
| VPN网关 `vpn` | [用户指南](<01_专有云企业版_v3.18.6_20260730/网络服务/vpn VPN网关/04_用户指南_enterprise-user-guide.pdf>) | 49 | 0.8 MB | 20260729 |
| VPN网关 `vpn` | [开发指南](<01_专有云企业版_v3.18.6_20260730/网络服务/vpn VPN网关/05_开发指南_enterprise-developer-guide.pdf>) | 103 | 2.1 MB | 20260729 |
| VPN网关 `vpn` | [运维指南](<01_专有云企业版_v3.18.6_20260730/网络服务/vpn VPN网关/06_运维指南_operation-and-maintenance-guide.pdf>) | 8 | 0.5 MB | 20260729 |


### 计算服务

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 容器镜像服务 `acr` | [产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/acr 容器镜像服务/01_产品简介_enterprise-product-introduction.pdf>) | 9 | 0.3 MB | 20260729 |
| 容器镜像服务 `acr` | [用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/acr 容器镜像服务/05_用户指南_enterprise-user-guide.pdf>) | 109 | 1.7 MB | 20260729 |
| 容器镜像服务 `acr` | [开发指南](<01_专有云企业版_v3.18.6_20260730/计算服务/acr 容器镜像服务/06_开发指南_enterprise-development-guide.pdf>) | 134 | 1.9 MB | 20260729 |
| 容器镜像服务 `acr` | [运维指南](<01_专有云企业版_v3.18.6_20260730/计算服务/acr 容器镜像服务/07_运维指南_enterprise-operation-guide.pdf>) | 8 | 1.1 MB | 20260729 |
| Alibaba Cloud Linux `alinux` | [产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/alinux Alibaba Cloud Linux/01_产品简介_product-introduction.pdf>) | 36 | 0.6 MB | 20260729 |
| Alibaba Cloud Linux `alinux` | [用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/alinux Alibaba Cloud Linux/03_用户指南_user-guide.pdf>) | 228 | 8.6 MB | 20260729 |
| Alibaba Cloud Linux `alinux` | [运维指南](<01_专有云企业版_v3.18.6_20260730/计算服务/alinux Alibaba Cloud Linux/04_运维指南_operation-and-maintenance-guide.pdf>) | 98 | 16.8 MB | 20260729 |
| Alibaba Cloud Linux `alinux` | [远程证明服务用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/alinux Alibaba Cloud Linux/07_远程证明服务用户指南_remote-certification-service-user-guide.pdf>) | 32 | 2.6 MB | 20260729 |
| 容器服务Kubernetes版 `csk` | [产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/csk 容器服务Kubernetes版/01_产品简介_enterprise-ascm-product-introduction.pdf>) | 19 | 0.4 MB | 20260729 |
| 容器服务Kubernetes版 `csk` | [用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/csk 容器服务Kubernetes版/05_用户指南_enterprise-ascm-user-guide.pdf>) | 561 | 19.0 MB | 20260831 |
| 容器服务Kubernetes版 `csk` | [开发指南](<01_专有云企业版_v3.18.6_20260730/计算服务/csk 容器服务Kubernetes版/06_开发指南_enterprise-ascm-developer-guide.pdf>) | 171 | 2.3 MB | 20260729 |
| 容器服务Kubernetes版 `csk` | [运维指南](<01_专有云企业版_v3.18.6_20260730/计算服务/csk 容器服务Kubernetes版/07_运维指南_enterprise-ascm-operation-guide.pdf>) | 24 | 0.8 MB | 20260729 |
| 容器服务Kubernetes版 `csk` | [分布式云容器平台ACK One 产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/csk 容器服务Kubernetes版/14_分布式云容器平台ACK One 产品简介_ackoneproduct-introduction.pdf>) | 12 | 0.3 MB | 20260729 |
| 容器服务Kubernetes版 `csk` | [分布式云容器平台ACK One 用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/csk 容器服务Kubernetes版/15_分布式云容器平台ACK One 用户指南_ackoneuser-guide.pdf>) | 19 | 0.5 MB | 20260729 |
| 容器服务Kubernetes版 `csk` | [容器计算服务ACS 产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/csk 容器服务Kubernetes版/16_容器计算服务ACS 产品简介_container-computing-service-acs-product-introduction.pdf>) | 15 | 0.3 MB | 20260729 |
| 容器服务Kubernetes版 `csk` | [容器计算服务ACS 用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/csk 容器服务Kubernetes版/17_容器计算服务ACS 用户指南_container-computing-service-acs-user-guide.pdf>) | 141 | 1.3 MB | 20260729 |
| 云服务器 ECS `ecs` | [产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/ecs 云服务器 ECS/01_产品简介_product-introduction.pdf>) | 24 | 0.4 MB | 20260729 |
| 云服务器 ECS `ecs` | [用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ecs 云服务器 ECS/02_用户指南_enterprise-user-guide.pdf>) | 440 | 13.6 MB | 20260818 |
| 云服务器 ECS `ecs` | [开发指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ecs 云服务器 ECS/06_开发指南_enterprise-developer-guide.pdf>) | 717 | 5.8 MB | 20260729 |
| 云服务器 ECS `ecs` | [运维指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ecs 云服务器 ECS/07_运维指南_enterprise-operation-guide.pdf>) | 167 | 5.8 MB | 20260803 |
| 云服务器 ECS `ecs` | [实例规格族&实例规格简介](<01_专有云企业版_v3.18.6_20260730/计算服务/ecs 云服务器 ECS/13_实例规格族&实例规格简介_instance-family-and-instance-types.pdf>) | 51 | 0.7 MB | 20260729 |
| 弹性伸缩 `ess` | [产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/ess 弹性伸缩/01_产品简介_enterprise-ascm-product-introduction.pdf>) | 8 | 0.3 MB | 20260729 |
| 弹性伸缩 `ess` | [用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ess 弹性伸缩/05_用户指南_enterprise-ascm-user-guide.pdf>) | 63 | 1.2 MB | 20260729 |
| 弹性伸缩 `ess` | [开发指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ess 弹性伸缩/06_开发指南_enterprise-ascm-developer-guide.pdf>) | 339 | 3.2 MB | 20260729 |
| 弹性伸缩 `ess` | [运维指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ess 弹性伸缩/07_运维指南_enterprise-ascm-operation-guide.pdf>) | 8 | 0.3 MB | 20260729 |
| 运维编排 `oos` | [产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/oos 运维编排/02_产品简介_product-introduction.pdf>) | 8 | 0.3 MB | 20260729 |
| 运维编排 `oos` | [用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/oos 运维编排/06_用户指南_user-guide.pdf>) | 56 | 2.9 MB | 20260729 |
| 运维编排 `oos` | [开发指南](<01_专有云企业版_v3.18.6_20260730/计算服务/oos 运维编排/07_开发指南_development-guide.pdf>) | 73 | 1.8 MB | 20260729 |
| 运维编排 `oos` | [运维指南](<01_专有云企业版_v3.18.6_20260730/计算服务/oos 运维编排/08_运维指南_o-m-guide.pdf>) | 29 | 6.6 MB | 20260729 |
| 资源编排 `ros` | [产品简介](<01_专有云企业版_v3.18.6_20260730/计算服务/ros 资源编排/01_产品简介_empty-manual.pdf>) | 6 | 0.2 MB | 20260729 |
| 资源编排 `ros` | [用户指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ros 资源编排/05_用户指南_enterprise-ascm-user-guide.pdf>) | 412 | 3.0 MB | 20260729 |
| 资源编排 `ros` | [开发指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ros 资源编排/06_开发指南_enterprise-ascm-developer-guide.pdf>) | 151 | 2.2 MB | 20260729 |
| 资源编排 `ros` | [运维指南](<01_专有云企业版_v3.18.6_20260730/计算服务/ros 资源编排/07_运维指南_enterprise-ascm-operation-guide.pdf>) | 6 | 0.3 MB | 20260729 |

---

## 02_AIStack_v2.17.0_20260828_OpenTrek

6 本 · 1 个产品 · 44 MB · 962 页


### 人工智能

| 产品 | 手册 | 页数 | 大小 | 文档版本 |
|---|---|---|---|---|
| 智能体工厂 OpenTrek `opentrek` | [Agent Dev产品简介](<02_AIStack_v2.17.0_20260828_OpenTrek/人工智能/opentrek 智能体工厂 OpenTrek/01_Agent Dev产品简介_opentrek-agent-dev-aistack-product-introduction.pdf>) | 52 | 0.6 MB | 20260902 |
| 智能体工厂 OpenTrek `opentrek` | [Agent Dev用户指南](<02_AIStack_v2.17.0_20260828_OpenTrek/人工智能/opentrek 智能体工厂 OpenTrek/03_Agent Dev用户指南_agent-dev-user-guide.pdf>) | 171 | 12.2 MB | 20260902 |
| 智能体工厂 OpenTrek `opentrek` | [Agent Dev开发指南](<02_AIStack_v2.17.0_20260828_OpenTrek/人工智能/opentrek 智能体工厂 OpenTrek/05_Agent Dev开发指南_opentrek-agengt-dev-aistack-development-guide.pdf>) | 475 | 3.4 MB | 20260902 |
| 智能体工厂 OpenTrek `opentrek` | [Agent Dev部署指南](<02_AIStack_v2.17.0_20260828_OpenTrek/人工智能/opentrek 智能体工厂 OpenTrek/17_Agent Dev部署指南_opentrek-agent-dev-aistack-deployment-guide.pdf>) | 73 | 16.2 MB | 20260902 |
| 智能体工厂 OpenTrek `opentrek` | [AI Studio（标准版）产品简介](<02_AIStack_v2.17.0_20260828_OpenTrek/人工智能/opentrek 智能体工厂 OpenTrek/19_AI Studio（标准版）产品简介_aistudio-std-product-overview-aistack.pdf>) | 8 | 0.3 MB | 20260902 |
| 智能体工厂 OpenTrek `opentrek` | [AI Studio（标准版）用户指南](<02_AIStack_v2.17.0_20260828_OpenTrek/人工智能/opentrek 智能体工厂 OpenTrek/21_AI Studio（标准版）用户指南_aistudio-std-user-guide-aistack.pdf>) | 183 | 10.8 MB | 20260902 |

---

## 本次未纳入（按你的指示排除）

监控与运维平台全域 8 个产品（aso / asm / tongque / cms / arms / prometheus / xtrace / tianji），以及 EDAS、全局事务服务、Kafka版、多活容灾MSHA、CSB、AHAS、无影、Dataphin、DataV、DataQ、机器学习、大数据管家、DataHub、Elasticsearch、表格存储、应用身份服务、云盾云防火墙、堡垒机、NDR、WAF、敏感数据保护、DDoS、内容安全、AnalyticDB、Lindorm、EHPC、裸机管理BMS、GPU云服务器。

横向运维文档与公告（告警参考 / 常见问题 / 运维控制台操作指南 / 版本说明书 / 生命周期与安全公告，约 0.53 GiB）未纳入，随时可追加。

---

## 英文（国际版）文档包

`10_EN_ApsaraStack_v3.18.6/` —— **287 本 PDF / 89 个英文产品 / 42,932 页 / 1.14 GiB**，来源为国际站下载页，与中文包是两套独立出版物（不是翻译对齐），单独目录存放、单独索引。

| 文档类型 | 本数 |
|---|---|
| User Guide | 79 |
| Product Introduction | 72 |
| Operations and Maintenance Guide | 67 |
| Developer Guide | 65 |
| ? | 2 |
| Operations Guide | 1 |
| Introduction to Instance Families and Instance Types | 1 |

- 可与中文册配对的（同产品同类型）：**160 / 287**；其余为中文侧未选或国际版专属产品（12 个英文独有产品）
- 子目录名用官方英文产品名，保留官方原文件名（含发布日期）
- 索引：`10_EN_ApsaraStack_v3.18.6/文档索引_EN.csv`、`README_EN.md`
- 中英互查：根目录 `中英对照手册映射.csv`
- 打包：`_zips_en/ENv3.18.6_<文档类型>_<n>本_<MB>MB.zip`（按类型 5 个包）



## AI / OpenTrek 便利包

`_zips_en/ENv3.18.6_AI-OpenTrek_17本_62MB.zip` —— 把散在按类型包里的 17 本 AI 手册（OpenTrek Dev / Ops / AI Studio / AI Gateway / AgentRuntime + Apsara AIOps / Copilot）合并成一个 zip，内容与按类型包重叠，不是新下载。

---

## 下次怎么只取新版（不重复下载同一份）

判重**不靠本地文件**（本地已不存 PDF），靠 `文档缓存索引.csv` 的 583 条记录：每条含
`id`（产品+手册类型，中文再加 manualCode）、`versionStamp`（版本戳）、`url`、`bytes`、`pages`、
`markdownSha256`、`pdfCloud`（该册 PDF 现存于云端哪个包）。

流程（清单抓取是秒级，不碰 PDF）：

1. **重新列清单**
   - 英文：`curl -s https://www.alibabacloud.com/en/product/apsara-stack/download` → 正则抽 `.pdf`，
     文件名尾 8 位日期即版本戳；新版 stack 出现时（如 V3.19.x）整组按新 `stackVersion` 处理
   - 中文：先 `curl -s https://help.aliyun.com/apsara/integrated.html` 取 `data-stack-code` 与
     `<option value="v_...">` 判断是否有更新的企业版版本；再用
     `/apsara/api/products?type=<stack>&version=<v>` 与
     `/apsara/api/product/mapListByUserId?stackCode=&version=&productCode=`（**需有专有云权益的登录态**）
     取每册 `pdfDownloadUrl` 与 `docVer`
2. **做差集**：`key = id@versionStamp`
   - 索引里没有该 `id` → 新产品/新手册：**下载**
   - `id` 相同但 `versionStamp` 更新 → 版本升级：**下载新版**，并把旧 markdown 标记待替换
   - `id` 与 `versionStamp` 都相同 → **跳过**（这就是你要的去重；不再重复拉同一份）
   - 想更严格时再比 `bytes`（或对应包内 CRC64），防同名不同内容
3. **转换**：只转新/变的那几本；已有 markdown 用 `markdownSha256` 比对，避免白跑
4. **收尾**：更新 `文档缓存索引.csv` 与 `下载台账.json.cacheIndex.entries_detail`、`全量文档清单.html`；
   如只要文字结果，转完即删 PDF（就保持现在这种"0 个 PDF"状态）

现成索引位置（OSS 同名对象；预签名链接含 AccessKeyId，**不入库**，只留在本地 `下载链接.md` 另行分发）：
`apsara-docs/文档缓存索引.csv`、`apsara-docs/下载台账.json`、`apsara-docs/README.md`

## 防重复下载机制（中英同一套 · 2026-09-14T03:54:39+08:00 落地并验证）

**主表**：`文档缓存索引.json`（程序读）+ `文档缓存索引.csv`（人看），583 条，**以本地这份为准**（OSS 上的 `apsara-docs/文档缓存索引.csv` 是补 `pdfCloud/localPath/inScope/markdownSha256` 之前的旧版，按你的决定不再补推）。

| 字段 | 作用 |
|---|---|
| `id` | 稳定身份。中文 = 手册 URL；英文 = **去掉 8 位发布日期**的 URL（所以官方换日期后 id 不变） |
| `versionStamp` | 版本戳。英文 = 文件名发布日期；中文 = 册内「文档版本」日期 |
| `markdown` / `markdownSha256` | 是否已转 Markdown + 内容指纹 → **有值即视为已处理，永不再下该 PDF** |
| `pdfLocal` / `localPath` | PDF 是否在本地、登记路径 |
| `pdfCloud` | 该 PDF 所属云端包（`apsara-docs/zips*/…zip`），要原件按此取回 |
| `mdCloudKey` | 该 Markdown 在云端整包内的条目 |
| `inScope` | 是否在你指定的转换口径内（英文 4 类，故 71 条 False） |

**决策代码**：`工具/cache.py:decide()` + `工具/pull_docs.py`（`--fetch` 只补 NEED，`--into-tree` 写回登记路径）。
**取清单**：`工具/list_docs.py`（英文免登录抓下载页；中文需 `APSARA_COOKIE`）。

| 标签 | 条件 | 动作 |
|---|---|---|
| SKIP | 同 id 同 stamp 且已有 markdown | 不下载、不转换 |
| FETCH | 同 id 但 stamp 更新（新版） | 只下这一本 |
| CONVERT | 已登记、口径内、缺 markdown | 只转换 |
| NEW | 未登记 | 下载 + 转换 |
| SCOPE | 口径外（英文 O&M 等 68 本） | 不动作（避免当缺失反复补） |

实测（`python3 工具/pull_docs.py`）：候选 583 → SKIP 515 / SCOPE 68 → **需下载 0**。
用**重新抓取的线上清单**核对（`list_docs.py --langs en` → 287 条 V3.18.6）：SKIP 219 / SCOPE 68 / **需下载 0**。
反向用例：改 stamp → FETCH；伪造新 id → NEW；清空 markdown → CONVERT；`--fetch --limit 1` 实际只落 1 个文件且 `%PDF` 头正确（测试件已删）。

> 结论：**删掉本地 PDF 不会触发重下**。判定只看 `id + versionStamp + 是否已有 markdown 指纹`，
> 与 PDF 是否在本地无关；需要原件时走 `pdfCloud` 指向的云端包或 `url` 单取。
