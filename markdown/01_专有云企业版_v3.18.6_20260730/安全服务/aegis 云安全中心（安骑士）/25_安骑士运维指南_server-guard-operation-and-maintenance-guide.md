---
title: "云安全中心（安骑士） 安骑士运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 106
source_pdf: "25_安骑士运维指南_server-guard-operation-and-maintenance-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/aegis/zh/server-guard-operation-and-maintenance-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云安全中心（安骑士） 安骑士运维指南

## 安骑士运维手册

### 产品介绍

安骑士（主机安全+态势感知）是一款集持续监测、深度防御、全面分析、快速响应能力于一体的云上安全管理平台。 安骑士基于云原生架构优势，提供云上资产管理、配置核查、主动防御、安全加固、云产品配置评估和安全可视化等能力，可有效发现和阻止病毒传播、黑客攻击、勒索加密、漏洞利用等风险事件，实现一体化、自动化的安全运营闭环，保护云内云外的主机、容器、虚拟机等工作负载安全性，同时满足监管合规要求。 安骑士在服务器系统内核层面通过Agent插件实现云上文件和进程行为的全局监控和实时分析，对海量病毒样本持久化攻击方式的自动化分析，有效绕过顽固木马和恶意程序的反查杀能力；还可以基于程序行为分析，挖掘出黑名单未能辨识的恶意威胁，实现主动拦截；其云端病毒库实时更新，集成了国内外主流杀毒引擎、阿里云自研沙箱和机器学习引擎等前沿技术，可以避免因病毒库更新不及时而造成的损失。 防护策略和数据源自于多年的积累，是阿里云上多达百万级的用户，每天面临多达几十万次的各种攻击。 阿里云安全团队充分利用了这些安全攻防的数据积累，每天对公共云上10多TB的安全数据进行分析，形成恶意IP库、恶意行为库、恶意样本库、安全漏洞库等基础安全能力，并及时应用到态势感知的各个防护模块中，提升防护能力，为用户带来更好的安全保障。

**V3.16.2版本产品架构**

**V3.18.3版本产品架构**

**(新版)V3.18.3版本产品架构**

### 部署架构

安骑士是典型的C/S架构，包括服务端和客户端。服务端负责资产、检测、防御等核心能力，客户端负责实时监测主机状态、执行检测脚本、实时防御等。

**V3.18.1及之前的版本**

**V3.18.2-- V3.18.6(2512通用)版本**

**V3.19版本 -- V3.18.6(2512limit)版本**

**服务端**

服务端主要分成以下几个模块： 基础能力：云盾通用能力，提供控制台和OpenAPI。 客户端管理：负责管理客户端连接、配置、规则、补丁包等。 核心能力：包括资产、告警、日志、文件采集、安全报告等。 检测防御：包括漏洞、基线、文件、网络、进程的检测防御能力。 检测引擎：包括商业病毒检测引擎、阿里自研病毒检测引擎、大数据计算引擎。 服务端每个应用的具体职责：

| 模块 | 职责 |
|---|---|
| YundunConsole | 安骑士控制台，为安全管理员提供了统一的管理界面。 |
| YundunBaseService | 安骑士API网关，将主机安全能力开放给三方开发者。 |
| Aegiserver | 客户端连接管理、配置下发、消息转发等。 |
| Aegisupdate | 客户单升级、规则/脚本/补丁等文件拉取。 |

| AegisMaster | 客户端配置、插件管理。 |
|---|---|
| AegisSuspicious | 入侵告警事件、应用白名单。 |
| AegisAssets | 资产指纹、日志归档 |
| Aegisbiz | 负责API转发到各个模块 |
| NewSas | 安全报告。 |
| SasFileserver | 文件采集。 |
| AegisHealthCheck | 主机基线检查。 |
| AegisVirusScan | 文件检测。 |
| AegisDetect | 旧版文件检测，当前仅保留文件白名单管理，其他流程全部迁移到 AegisVirusScan。 |
| AegisDefence | 防篡改。 |
| AegisVulnerability | 漏洞检测。 |
| BaselineCheck | 云产品配置检查。 |
| AegisMatcher | 云查杀。 |
| BanffAegisWeb | 命令下发通道。 |
| AegisPrivateCloudEngine | GLE引擎，阿里自研病毒检测引擎。 |
| YaraSlave | Yara二进制检测引擎，商业病毒检测引擎。 |
| AegisCloudavira | 小红伞二进制引擎，商业病毒检测引擎。 |
| AegisCloudavbd | BD二进制检测引擎，商业病毒检测引擎。 |
| Dipper | 大数据计算引擎，入侵检测。 |

**客户端**

客户端包括以下模块，每个模块对应一个主机进程。

| 名称 | 说明 |
|---|---|
| AliYunDun | 核心进程，用于与云安全中心服务器建立连接。 |
| AliYunDunUpdate | 核心进程，用于定期检测云安全中心Agent是否需要升级。 |
| AliWebGuard | 网页防篡改进程。 |
| AliYunDunMonitor | 云安全中心的守护进程。 |
| AliSecGuard | 客户端自保护进程。 |
| AliHips | 病毒木马防护进程。 |

**说明**

参考文档：客户端支持的操作系统

### 服务端模块功能与组件依赖关系

**模块功能**

**服务端组件与依赖关系**

### 核心模块

**资产同步**

通过资产中心的总览页面全面了解云安全中心已防护的资产的安全状态和统计信息。 资产数据来源包括：**ECS****、平台物理机、云外主机、****BMS/BMCP****机器**

**ECS资产同步**

通过OpenAPI同步ECS资产，OpenAPI返回的是全量ECS列表。

**平台物理机**

通过Tianji Api获取全量的物理机列表，再通过平台侧物理机的客户端上报的机器信息进行对比完善。

**云外主机**

将连接到Aegiserver的云外主机作为资产，此外云外主机还需通过安装码识别到租户归属关系。

**BMS/BMCP**

BMS/BMCP资产的接入和ECS资产接入流程上基本一致，但不同的地方在于，BMS/BMCP接口返回的信息缺乏uuid，需要由aegis-update生成。

**主机资产刷新入口与逻辑**

**主机指纹**

资产指纹周期性采集服务器的账号、端口、进程、中间件、软件、计划任务、启动项等数据。 采集方式： 周期性自动采集采集单个或多个资产最新指纹数据周期采集取决于页面上的周期扫描配置，关闭后则无法采集，其中如果需要使用**云外暴露检查**功能，则必须开启**中间件**采集。 周期性自动采集时间：不是在同一时间点采集全部资产的指纹数据，如：扫描周期为一天，则实际会把采集任务打散到这一天的各个时间段。

**云外暴露检查**

云外暴露检查功能依赖于资产指纹的调查中采集的中间件信息。 云外暴露检查支持自动分析您的ECS服务器在互联网上的暴露情况，可视化呈现ECS与互联网的通信链路， 并集中展示您暴露在公网的ECS的漏洞信息，帮助您快速定位您资产在互联网上的异常暴露情况并提供相应漏洞的修复建议。 统计数据说明：

| 统计项名称 | 说明 |
|---|---|
| 暴露资产/公网IP数 | 暴露在互联网上的服务器总数量和IP地址总数量。 |
| 网关资产 | 暴露在互联网上的网关资产（负载均衡、NAT网关）总数量。单击相应数值打开网关资产面板，可查看网关资产的列表。在网关资产面板，单击网关资产名称可跳转至对应资产详情页面。 |
| 暴露端口 | 暴露在互联网上的端口总数量。单击相应数值打开暴露端口面板，可查看暴露端口的列表。 在暴露端口面板，单击暴露端口名称查看存在该暴露端口的资产列表。 |
| 暴露组件 | 暴露在互联网上的您服务器的系统组件（例如OpenSSL、OpenSSH）总数量。单击相应数值打开暴露组件面板，可查看暴露组件的列表。在暴露组件面板，单击暴露组件名称查看存在该暴露组件的资产列表。 |

| 可被利用漏洞 | 暴露在互联网上可被黑客利用的漏洞总数量及高危、中危、低危漏洞数量。单击表示高危、 中危、低危漏洞数量的数字可跳转至漏洞修复页面。不同类型的漏洞使用不同颜色表示： 高危：红色。此类漏洞会对您的资产安全较大的威胁，建议您重点关注并及时修复。 中危：橙色。此类漏洞对您的资产会产生一定的危害，建议您及时修复。 低危：灰色。此类漏洞对您的资产安全危害较小，您可以延后修复。 |
|---|---|

**漏洞管理**

安骑士支持对常见漏洞类型进行检测和修复，包括Linux漏洞、Windows漏洞、CMS漏洞、应用漏洞、应急漏洞。

**Linux漏洞检测流程**

1、客户端段上报心跳时根据扫描周期定时下发扫描。 2、客户端上报软件包信息后，根据oval规则匹配漏洞，补充漏洞详情，经历漏洞白名单，漏洞运营过滤后入库。

**Linux漏洞修复流程**

1. 手动修复会生成修复任务，定时执行下发
2. 系统内核内漏洞不支持修复

**Windows漏洞检测流程**

1. 每48小时会在大心跳上报时下发漏洞检测命令。
2. 客户端接收命令后，从aegisupdate中更新检测脚本及规则后执行检测，将执行结果上报。
3. 服务端接收后，会根据漏洞详情获取漏洞名称，经漏洞运营，漏洞白名单后入库。

**Windows漏洞修复流程**

1. 点击修复会生成修复任务，通过定时任务下发修复命令。
2. 当修复失败后，会定时检测修复结果，当修复失败时，默认会失败重试修复2次。
3. aegisUpdate服务启动时从windowsPath服务的OSS中获取系统补丁包文件，客户端从aegisUpdate容
器中下载补丁并修复。

**CMS漏洞检测流程**

**CMS漏洞修复流程**

**CMS漏洞入库逻辑**

**应用漏洞检测流程**

1. 每48小时会在大心跳上报时下发漏洞检测命令。
2. 客户端从aegisUpdate中拉取脚本并执行。
3. 客户端分片上报运行时软件包信息。
4. 软件包信息上报完成后，统一进行规则匹配（自定义规则），并修改历史漏洞状态。

**病毒查杀**

勒索病毒、挖矿程序等持久化、顽固型病毒已经成为网络安全最大的威胁。病毒防御功能针对此类病毒提供扫描、告警、深度查杀的能力，可有效预防此类病毒入侵您的服务器。 病毒防御功能针对勒索病毒、挖矿程序等顽固性病毒，对安骑士所有服务器提供深度扫描服务。安骑士支持立即扫描和周期性扫描病毒。

**文件检测防御**

**二进制文件检测防御**

**功能介绍**

该功能适用于防范上传至OSS或存在于服务器中的恶意二进制程序，广泛应用于服务器安全、文件存储环境风险治理等场景

**业务流程图**

**恶意脚本检测防御**

**功能介绍**

功能主要用于识别服务器中是否存在由攻击者植入的恶意脚本，以防止进一步的攻击利用，如挖矿、添加后门、创建系统账户等行为。

**业务流程图**

**webshell检测防御**

**功能介绍**

该功能可检测包括WebShell在内的23类病毒类型，如勒索病毒（RansomWare）、挖矿程序 （Miner）、高危程序（Trojan）、恶意脚本（MalScript）、DDoS木马、Rootkit等。当检测到 WebShell等风险文件时，系统会提供事件说明及处置建议，便于用户及时处理。

**业务流程图**

**恶意文件检测SDK**

**功能介绍**

当您需要检测存储在某个Bucket内的数据是否存在WebShell文件、勒索病毒、木马等恶意文件的风险时， 您可以通过OSS的恶意文件检测功能识别风险数据。如果检测到恶意文件，您可以根据事件说明中的处置建议及时处理该文件。

**业务流程图**

**核心文件监控**

**功能介绍**

核心文件监控功能可以实时监控服务器上核心文件的访问情况，对文件的访问、修改、删除、重命名等操作进行实时监控和告警，可监控核心文件是否被盗取或篡改。本文介绍如何实现对服务器核心文件访问的监控。

**业务流程图**

**进程检测防御**

**网络检测防御**

**暴力破解**

安骑士支持配置自定义暴力破解防御规则。配置防暴力破解规则后，登录服务器时，在某个时间范围内登录服务器的失败次数超过限定次数将被禁止登录一段时间。防暴力破解功能，可有效防止您服务器账号的密码被暴力破解。

**说明**

1. 客户端上报原始主机登录日志
2. aegisAssets消费原始主机登录日志消息
3. 主机登录日志归档至OSS,满足等保要求（185天）
4. 主机登录日志接入sls-inner，提供日志检索能力
5. 大数据引擎消费主机登录日志
6. 客户在控制台设置暴力破解相关规则
7. 大数据引擎定去获取客户设置的暴力破解规则（每小时获取一次）
8. 大数据引擎根据规则，消费主机登录日志后，产出暴力破解数据结果（只发送未加白的告警数据）
9. suspicious服务消费告警数据后，发送主机暴力破解数据至攻击分析模块（告警已加白直接发送，告
警未加白，消费入库后再发送攻击分析）
10. v3.15版本后暴力破解以新版暴力破解结果为准，旧版暴力破解只是作为日志溯源信息参考

**防暴力破解**

暴力破解（Brute Force Attack）是一种密码攻击技术，攻击者尝试通过枚举所有可能的组合，直到找到正确的密码或密钥。防暴力破解功能，以帮助您保护主机免受暴力破解攻击。 防暴力破解功能：新建防暴力破解策略可以启用防暴力破解功能。创建防暴力破解策略后，如果某个IP地址在指定时间范围内登录服务器的失败次数超过限定次数将触发防暴力策略生效，该策略生效后会自动生成IP 拦截规则（即**系统规则**子页签下的拦截IP），在一段时间内禁止该IP登录服务器。自动生成的IP拦截规则在生成时为已启用状态，生效时长为防暴力破解策略的禁止登录时长。 系统规则：防暴力破解策略被触发后自动生成的IP拦截规则自定义规则：生效资产和过期时间执行IP拦截任务

**基线检查**

基线检查功能针对服务器操作系统、数据库、软件和容器的配置进行安全检测，并提供检测结果说明和加固建议。 基线指操作系统、数据库及中间件的安全实践及合规检查的配置红线，包括弱口令、账号权限、身份鉴别、 密码策略、访问控制、安全审计和入侵防范等安全配置检查。云安全中心的安全基线支持弱口令、未授权访问、历史漏洞和配置红线的立体巡检，合规基线支持等保合规和CIS标准。安全基线与合规基线均已覆盖常用的30多个系统版本和10多个数据库及中间件，可以满足企业多种合规需求。

**攻击分析**

攻击分析对资产受到的攻击行为进行分析，并展示攻击相关的数据。 攻击分析的数据来源： 安骑士：主机层攻击数据，主要包括暴力破解数据，客户端上报登录日志给Aegiserver，Dipper分析登录日志产出暴力破解数据，Aegisbiz消费暴力破解数据，按资产、类型、小时维度归类后存储到 MiniRDS。

| code | 类型名称 | 来源 | 支持版本 |
|---|---|---|---|
| 2 | SSH暴力破解 | cfw | 3.16 |
| 1 | RDP暴力破解 | cfw | 3.16 |
| 4 | FTP暴力破解 | cfw | 3.16 |

WAF：应用层攻击数据，Aegisbiz消费暴力破解数据，按资产、类型、小时维度归类后存储到 MiniRDS。

| code | 类型名称 | 来源 | 支持版本 |
|---|---|---|---|
| sqli | SQL注入 | waf | 3.16 |
| code exec _ | 代码执行 | waf | 3.16 |

| codei | 代码执行 | waf | 3.16 |
|---|---|---|---|
| xss | XSS攻击 | waf | 3.16 |
| lfi | 本地文件包含 | waf | 3.16 |
| rfi | 远程文件包含 | waf | 3.16 |
| webshell | 脚本木马 | waf | 3.16 |
| upload | 上传漏洞 | waf | 3.16 |
| path | 路径遍历 | waf | 3.16 |
| bypass | 越权访问 | waf | 3.16 |
| csrf | CSRF | waf | 3.16 |
| crlf | CRLF | waf | 3.16 |
| 21 | 扫描攻击 | waf | 3.16 |
| 6 | 反序列化攻击 | waf | 3.16 |
| 14 | 信息泄露攻击 | waf | 3.16 |
| 213 | 反弹shell攻击 | waf | 3.16 |
| 211 | 蠕虫病毒请求 | waf | 3.16 |
| 5 | 木马后门请求 | waf | 3.16 |
| 104 | DoS攻击 | waf | 3.16 |
| 0 | SQL注入攻击 | waf | 3.16 |
| 101 | XSS跨站脚本攻击 | waf | 3.16 |

| 102 | CSRF跨站请求伪造攻击 | waf | 3.16 |
|---|---|---|---|
| 103 | SSRF服务器端请求伪造攻击 | waf | 3.16 |
| 7 | 代码执行攻击 | waf | 3.16 |
| 8 | 代码注入攻击 | waf | 3.16 |
| 109 | 命令注入攻击 | waf | 3.16 |
| 10 | 远程文件包含 | waf | 3.16 |
| 11 | 脚本木马 | waf | 3.16 |
| 17 | XML实体注入攻击 | waf | 3.16 |
| 20 | 路径穿越攻击 | waf | 3.16 |
| 61 | 超时攻击 | waf | 3.16 |
| 112 | 重定向攻击 | waf | 3.16 |
| 113 | 权限不当 | waf | 3.16 |
| 15 | 未授权访问 | waf | 3.16 |
| 16 | 不安全的配置 | waf | 3.16 |
| 18 | XPath注入攻击 | waf | 3.16 |
| 19 | LDAP注入攻击 | waf | 3.16 |
| 31 | 越权访问攻击 | waf | 3.16 |
| 24 | 文件修改攻击 | waf | 3.16 |
| 25 | 文件读取攻击 | waf | 3.16 |

| 26 | 文件删除攻击 | waf | 3.16 |
|---|---|---|---|
| 27 | 逻辑错误 | waf | 3.16 |
| 28 | CRLF注入攻击 | waf | 3.16 |
| 29 | 模板注入攻击 | waf | 3.16 |
| 30 | 点击劫持 | waf | 3.16 |
| 31 | 缓冲器溢出攻击 | waf | 3.16 |
| 32 | 整数溢出攻击 | waf | 3.16 |
| 33 | 格式化字符串 | waf | 3.16 |
| 34 | 条件竞争 | waf | 3.16 |
| other | 其他 | waf | 3.16 |

NDR：网络层攻击数据，Aegisbiz消费暴力破解数据，按资产、类型、小时维度归类后存储到 MiniRDS。

| code | 类型名称 | 来源 | 支持版本 |
|---|---|---|---|
| 203 | 暴力破解 | ips | 3.16 |
| 209 | Web攻击 | ips | 3.16 |
| 212 | 挖矿行为 | ips | 3.16 |
| 201 | 异常连接攻击 | ips | 3.16 |

**应用白名单**

应用白名单功能支持将需要重点防御的服务器加入到白名单中，通过检测白名单中指定的应用程序区分可信、可疑和恶意程序，防止未经白名单授权的程序运行。 应用白名单功能主要包括采集、告警、拦截三个流程，其中拦截模式只针对特定局点开启。 采集流程：客户端上报进程BinInfo或快照日志，aegis-suspicious消费后通过引擎、内置白库、自定义白库三类检测后，确定是否是白名单进程并入库。 告警流程：客户端上报进程BinInfo或快照日志，aegis-suspicious通过采集的白名单进程判断是否是可信进程，如果是不可信进程，则生成告警。 拦截流程：如果开启了拦截模式，aegis-suspicious会通知aegis-matcher更新云查杀库，云查杀模块会通过客户端HIPS进程阻断主机上的进程启动，同时还会主动下发kill进程命令用于阻断已启动的进程。

**网页防篡改**

网页防篡改实时监控网站目录并通过备份恢复被篡改的文件或目录，保障重要系统的网站信息不被恶意篡改，防止出现挂马、黑链、非法植入等入侵。

**云产品检查**

云平台配置检查功能，可帮助您检查您云产品的安全配置是否存在安全隐患，主要可检查的云产品涉及 （oss,sls,rds，ecs，MongoDb,redis等）
1. 用户可设置扫描周期或立即扫描触发云产品检查
2. 当开始扫描时，先从aegisbi获取ak信息
3. 通过groovy脚本中使用网关代理调用各个云产品的openapi，获取检查结果

**高危命令审计**

用户可通过该功能对主机侧进程等数据自定义命令特征，从而获取到存在高危命令的运行记录及告警事件。

**恶意行为防御**

恶意行为防御是安骑士提供的一项主机防护功能，用于识别、阻止和应对各类恶意活动，保护云主机免受攻击。 该功能包含两类规则：
**系统防御规则**：由安骑士预置，分为**网络防御**和**进程防御**。
网络防御可自动拦截基础网络攻击，并在“安全告警 > 网络防御告警”中查看相关事件。 进程防御会触发“精准防御”类告警，用于检测如勒索病毒、挖矿木马、后门程序等恶意行为。
**自定义防御规则**：用户可根据业务需求自定义规则，对特定行为（如命令行、进程Hash、文件读写、注册
表操作等）进行放行或拦截，有效减少误报自定义规则的优先级高于系统防御规则

### 高可靠性

**服务端高可用**

**说明**

服务端整体设计原则：无状态应用安骑士服务端全部是无状态应用，通过VIP+Dubbo实现负载均衡保证服务可用性。

**V3.18.1及之前的版本**

服务端本身是无状态的，部署在至少两台物理机上，只要有一台物理机正常运行即可保证可用性。 数据存储在在MiniRDS、SLS、OSS、Tair、Diamond、MetaQ等中间件或云服务上，存储高可用性由中间件或云服务保证。 对外提供HTTPS协议的OpenAPI，通过DNS+VIP实现负载均衡保证可用性。 服务内部调用依赖Dubbo框架，由Dubbo的软负载保证可用性。

**V3.18.2及之后的版本**

服务端本身是无状态的，Paas部署时相同pod至少拓扑分散在两个Node上，只要有一个pod正常运行即可保证可用性，其他高可用特性同早期版本相同。

**客户端高可用**

客户端高可用是为了保证客户端进程不会被操作系统或恶意程序kill，导致主机脱离安全管理。 客户端高可用有两个措施保证： 1、AliYunDun和AliYunDunUpdate互为守护进程，当其中一个被kill后，另一个进程会实时拉起对方。 2、当启用自保护（AliSecGuard）时，AliSecGuard会在驱动层保证客户端无法被Killed。

### 容灾备份

**同城容灾**

**说明**

设计原则：业务双活安骑士同城容灾架构遵循双活原则，数据由云存储或中间件自身保证容灾。 各组件同城容灾实现方案介绍：

| 组件 | 方案 |
|---|---|
| 安骑士 | 双活部署，依赖中间件及云存储保证数据一致。 |

| DNS | 通过Anycast VIP实现主备机房流量隔离。 |
|---|---|
| VIP | 通过BGP路由实现主备切换。 |
| MiniRDS | 主从库binlog复制。 |
| SLS-inner | V3.16.2版本sls-inner支持同城容灾。 |
| OSS | 主备机房数据同步。 |
| 中间件 | 双活部署，依赖MiniRDS保证数据一致。 |

**异地灾备**

**说明**

设计原则：Region间相互独立安骑士多Region架构遵循独立原则，单元Region对中心Region无任何依赖，数据及服务保证完全隔离。

### 监控告警

**系统监控指标**

安骑士系统监控均已接入TianjiMon。

**重要**

注意：3.17.1之前版本还未开启告警。 各应用具体监控指标如下：

**aegis-virus-scan应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisvirusscan cpu containe _ _ r host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisvirusscan cpu containe _ _ r serverrole _ | CPU使用率（服务角色） |  |  |  |
| aegisvirusscan cpu containe _ _ r cluster _ | CPU使用率（集群） |  |  |  |

| aegisvirusscan memo contai _ _ ner host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegisvirusscan memo contai _ _ ner serverrole _ | 内存（服务角色） |  |  |  |
| aegisvirusscan memo contai _ _ ner cluster _ | 内存（集群） |  |  |  |
| aegisvirusscan load contain _ _ er host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisvirusscan load contain _ _ er serverrole _ | 负载（服务角色） |  |  |  |
| aegisvirusscan load contain _ _ er cluster _ | 负载（集群） |  |  |  |
| aegisvirusscan tcp conns co _ _ _ ntainer host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegisvirusscan tcp conns co _ _ _ ntainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegisvirusscan tcp conns co _ _ _ ntainer cluster _ | tcp连接数（集群） |  |  |  |
| aegisvirusscan ntp container _ _ host _ | NTP（单机） | NTP | 暂无 | 暂无 |
| aegisvirusscan ntp container _ _ serverrole _ | NTP（服务角色） |  |  |  |
| aegisvirusscan ntp container _ _ cluster _ | NTP（集群） |  |  |  |
| aegisvirusscan process coun _ _ t container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisvirusscan process coun _ _ t container cluster _ _ | 进程数（服务角色） |  |  |  |
| aegisvirusscan process coun _ _ t container host _ _ | 进程数（集群） |  |  |  |

| aegisvirusscan nginx contai _ _ ner host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
|---|---|---|---|---|
| aegisvirusscan nginx contai _ _ ner serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegisvirusscan nginx contai _ _ ner cluster _ | nginx QPS（集群） |  |  |  |
| aegisvirusscan health contai _ _ ner host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisvirusscan health contai _ _ ner serverrole _ | 健康检查（服务角色） |  |  |  |
| aegisvirusscan health contai _ _ ner cluster _ | 健康检查（集群） |  |  |  |

**mordor应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| mordor cpu container host _ _ _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| mordor cpu container serve _ _ _ rrole | CPU使用率（服务角色） |  |  |  |
| mordor cpu container cluste _ _ _ r | CPU使用率（集群） |  |  |  |
| mordor memo container ho _ _ _ st | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| mordor memo container ser _ _ _ verrole | 内存（服务角色） |  |  |  |
| mordor memo container clu _ _ _ ster | 内存（集群） |  |  |  |

| mordor load container host _ _ _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| mordor load container serve _ _ _ rrole | 负载（服务角色） |  |  |  |
| mordor load container clust _ _ _ er | 负载（集群） |  |  |  |
| mordor tcp conns container _ _ _ host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| mordor tcp conns container _ _ _ serverrole _ | tcp连接数（服务角色） |  |  |  |
| mordor tcp conns container _ _ _ cluster _ | tcp连接数（集群） |  |  |  |
| mordor ntp container host _ _ _ | NTP（单机） | NTP | 暂无 | 暂无 |
| mordor ntp container server _ _ _ role | NTP（服务角色） |  |  |  |
| mordor ntp container cluste _ _ _ r | NTP（集群） |  |  |  |
| mordor process count conta _ _ _ iner host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| mordor process count conta _ _ _ iner cluster _ | 进程数（服务角色） |  |  |  |
| mordor process count conta _ _ _ iner host _ | 进程数（集群） |  |  |  |
| mordor nginx container host _ _ _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| mordor nginx container serv _ _ _ errole | nginx QPS（服务角色） |  |  |  |
| mordor nginx container clus _ _ _ ter | nginx QPS（集群） |  |  |  |

| mordor health container hos _ _ _ t | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| mordor health container ser _ _ _ verrole | 健康检查（服务角色） |  |  |  |
| mordor health container clu _ _ _ ster | 健康检查（集群） |  |  |  |

**defender应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| defender cpu container host _ _ _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| defender cpu container serv _ _ _ errole | CPU使用率（服务角色） |  |  |  |
| defender cpu container clus _ _ _ ter | CPU使用率（集群） |  |  |  |
| defender memo container h _ _ _ ost | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| defender memo container s _ _ _ erverrole | 内存（服务角色） |  |  |  |
| defender memo container cl _ _ _ uster | 内存（集群） |  |  |  |
| defender load container hos _ _ _ t | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| defender load container ser _ _ _ verrole | 负载（服务角色） |  |  |  |
| defender load container clu _ _ _ ster | 负载（集群） |  |  |  |
| defender tcp conns contain _ _ _ er host _ | tcp连接数（单机） |  |  |  |

| 安骑士运维指南·安骑士运维手册 |  |  |  |  |
|---|---|---|---|---|
|  |  | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| defender tcp conns contain _ _ _ er serverrole _ | tcp连接数（服务角色） |  |  |  |
| defender tcp conns contain _ _ _ er cluster _ | tcp连接数（集群） |  |  |  |
| defender ntp container host _ _ _ | NTP（单机） | NTP | 暂无 | 暂无 |
| defender ntp container serv _ _ _ errole | NTP（服务角色） |  |  |  |
| defender ntp container clust _ _ _ er | NTP（集群） |  |  |  |
| defender process count con _ _ _ tainer host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| defender process count con _ _ _ tainer cluster _ | 进程数（服务角色） |  |  |  |
| defender process count con _ _ _ tainer host _ | 进程数（集群） |  |  |  |
| defender nginx container ho _ _ _ st | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| defender nginx container se _ _ _ rverrole | nginx QPS（服务角色） |  |  |  |
| defender nginx container cl _ _ _ uster | nginx QPS（集群） |  |  |  |
| defender health container h _ _ _ ost | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| defender health container s _ _ _ erverrole | 健康检查（服务角色） |  |  |  |
| defender health container cl _ _ _ uster | 健康检查（集群） |  |  |  |

**banffaegisweb应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| banffaegisweb cpu containe _ _ r host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| banffaegisweb cpu containe _ _ r serverrole _ | CPU使用率（服务角色） |  |  |  |
| banffaegisweb cpu containe _ _ r cluster _ | CPU使用率（集群） |  |  |  |
| banffaegisweb memo contai _ _ ner host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| banffaegisweb memo contai _ _ ner serverrole _ | 内存（服务角色） |  |  |  |
| banffaegisweb memo contai _ _ ner cluster _ | 内存（集群） |  |  |  |
| banffaegisweb load containe _ _ r host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g >1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| banffaegisweb load containe _ _ r serverrole _ | 负载（服务角色） |  |  |  |
| banffaegisweb load containe _ _ r cluster _ | 负载（集群） |  |  |  |
| banffaegisweb tcp conns co _ _ _ ntainer host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| banffaegisweb tcp conns co _ _ _ ntainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| banffaegisweb tcp conns co _ _ _ ntainer cluster _ | tcp连接数（集群） |  |  |  |
| banffaegisweb ntp container _ _ host _ | NTP（单机） | NTP | 暂无 | 暂无 |
| banffaegisweb ntp container _ _ serverrole _ | NTP（服务角色） |  |  |  |
| > 文档版本：20260729 |  |  |  | 5 |

| banffaegisweb ntp container _ _ cluster _ | NTP（集群） |  |  |  |
|---|---|---|---|---|
| banffaegisweb process coun _ _ t container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| banffaegisweb process coun _ _ t container cluster _ _ | 进程数（服务角色） |  |  |  |
| banffaegisweb process coun _ _ t container host _ _ | 进程数（集群） |  |  |  |
| banffaegisweb nginx contain _ _ er host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| banffaegisweb nginx contain _ _ er serverrole _ | nginx QPS（服务角色） |  |  |  |
| banffaegisweb nginx contain _ _ er cluster _ | nginx QPS（集群） |  |  |  |
| banffaegisweb health contai _ _ ner host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| banffaegisweb health contai _ _ ner serverrole _ | 健康检查（服务角色） |  |  |  |
| banffaegisweb health contai _ _ ner cluster _ | 健康检查（集群） |  |  |  |

**aegisvulnerability应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisvulnerability cpu contai _ _ ner host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisvulnerability cpu contai _ _ ner serverrole _ | CPU使用率（服务角色） |  |  |  |
| aegisvulnerability cpu contai _ _ ner cluster _ | CPU使用率（集群） |  |  |  |

| aegisvulnerability memo co _ _ ntainer host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegisvulnerability memo co _ _ ntainer serverrole _ | 内存（服务角色） |  |  |  |
| aegisvulnerability memo co _ _ ntainer cluster _ | 内存（集群） |  |  |  |
| aegisvulnerability load conta _ _ iner host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisvulnerability load conta _ _ iner serverrole _ | 负载（服务角色） |  |  |  |
| aegisvulnerability load conta _ _ iner cluster _ | 负载（集群） |  |  |  |
| aegisvulnerability tcp conns _ _ container host _ _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegisvulnerability tcp conns _ _ container serverrole _ _ | tcp连接数（服务角色） |  |  |  |
| aegisvulnerability tcp conns _ _ container cluster _ _ | tcp连接数（集群） |  |  |  |
| aegisvulnerability ntp contai _ _ ner host _ | NTP（单机） | NTP | 暂无 | 暂无 |
| aegisvulnerability ntp contai _ _ ner serverrole _ | NTP（服务角色） |  |  |  |
| aegisvulnerability ntp contai _ _ ner cluster _ | NTP（集群） |  |  |  |
| aegisvulnerability process c _ _ ount container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisvulnerability process c _ _ ount container cluster _ _ | 进程数（服务角色） |  |  |  |
| aegisvulnerability process c _ _ ount container host _ _ | 进程数（集群） |  |  |  |

| aegisvulnerability nginx con _ _ tainer host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
|---|---|---|---|---|
| aegisvulnerability nginx con _ _ tainer serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegisvulnerability nginx con _ _ tainer cluster _ | nginx QPS（集群） |  |  |  |
| aegisvulnerability health co _ _ ntainer host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisvulnerability health co _ _ ntainer serverrole _ | 健康检查（服务角色） |  |  |  |
| aegisvulnerability health co _ _ ntainer cluster _ | 健康检查（集群） |  |  |  |

**aegisupdate应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisupdate cpu container _ _ _ host | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisupdate cpu container s _ _ _ erverrole | CPU使用率（服务角色） |  |  |  |
| aegisupdate cpu container c _ _ _ luster | CPU使用率（集群） |  |  |  |
| aegisupdate memo containe _ _ r host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisupdate memo containe _ _ r serverrole _ | 内存（服务角色） |  |  |  |
| aegisupdate memo containe _ _ r cluster _ | 内存（集群） |  |  |  |

| aegisupdate load container _ _ _ host | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegisupdate load container _ _ _ serverrole | 负载（服务角色） |  |  |  |
| aegisupdate load container _ _ _ cluster | 负载（集群） |  |  |  |
| aegisupdate tcp conns cont _ _ _ ainer host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegisupdate tcp conns cont _ _ _ ainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegisupdate tcp conns cont _ _ _ ainer cluster _ | tcp连接数（集群） |  |  |  |
| aegisupdate ntp container h _ _ _ ost | NTP（单机） | NTP | 暂无 | 暂无 |
| aegisupdate ntp container s _ _ _ erverrole | NTP（服务角色） |  |  |  |
| aegisupdate ntp container c _ _ _ luster | NTP（集群） |  |  |  |
| aegisupdate process count _ _ _ container host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisupdate process count _ _ _ container cluster _ | 进程数（服务角色） |  |  |  |
| aegisupdate process count _ _ _ container host _ | 进程数（集群） |  |  |  |
| aegisupdate nginx container _ _ host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegisupdate nginx container _ _ serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegisupdate nginx container _ _ cluster _ | nginx QPS（集群） |  |  |  |

| aegisupdate health containe _ _ r host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegisupdate health containe _ _ r serverrole _ | 健康检查（服务角色） |  |  |  |
| aegisupdate health containe _ _ r cluster _ | 健康检查（集群） |  |  |  |

**aegissuspicious应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegissuspicious cpu contain _ _ er host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegissuspicious cpu contain _ _ er serverrole _ | CPU使用率（服务角色） |  |  |  |
| aegissuspicious cpu contain _ _ er cluster _ | CPU使用率（集群） |  |  |  |
| aegissuspicious memo conta _ _ iner host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegissuspicious memo conta _ _ iner serverrole _ | 内存（服务角色） |  |  |  |
| aegissuspicious memo conta _ _ iner cluster _ | 内存（集群） |  |  |  |
| aegissuspicious load contain _ _ er host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g >1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegissuspicious load contain _ _ er serverrole _ | 负载（服务角色） |  |  |  |
| aegissuspicious load contain _ _ er cluster _ | 负载（集群） |  |  |  |
| aegissuspicious tcp conns c _ _ _ ontainer host _ | tcp连接数（单机） |  |  |  |

|  |  | 安 | 骑士运维指南· | 安骑士运维手册 |
|---|---|---|---|---|
|  |  | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegissuspicious tcp conns c _ _ _ ontainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegissuspicious tcp conns c _ _ _ ontainer cluster _ | tcp连接数（集群） |  |  |  |
| aegissuspicious ntp containe _ _ r host _ | NTP（单机） | NTP | 暂无 | 暂无 |
| aegissuspicious ntp containe _ _ r serverrole _ | NTP（服务角色） |  |  |  |
| aegissuspicious ntp containe _ _ r cluster _ | NTP（集群） |  |  |  |
| aegissuspicious process cou _ _ nt container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegissuspicious process cou _ _ nt container cluster _ _ | 进程数（服务角色） |  |  |  |
| aegissuspicious process cou _ _ nt container host _ _ | 进程数（集群） |  |  |  |
| aegissuspicious nginx contai _ _ ner host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegissuspicious nginx contai _ _ ner serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegissuspicious nginx contai _ _ ner cluster _ | nginx QPS（集群） |  |  |  |
| aegissuspicious health conta _ _ iner host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegissuspicious health conta _ _ iner serverrole _ | 健康检查（服务角色） |  |  |  |
| aegissuspicious health conta _ _ iner cluster _ | 健康检查（集群） |  |  |  |

**aegismaster应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegismaster cpu container _ _ _ host | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismaster cpu container s _ _ _ erverrole | CPU使用率（服务角色） |  |  |  |
| aegismaster cpu container c _ _ _ luster | CPU使用率（集群） |  |  |  |
| aegismaster memo containe _ _ r host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismaster memo containe _ _ r serverrole _ | 内存（服务角色） |  |  |  |
| aegismaster memo containe _ _ r cluster _ | 内存（集群） |  |  |  |
| aegismaster load container _ _ _ host | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismaster load container _ _ _ serverrole | 负载（服务角色） |  |  |  |
| aegismaster load container _ _ _ cluster | 负载（集群） |  |  |  |
| aegismaster tcp conns cont _ _ _ ainer host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegismaster tcp conns cont _ _ _ ainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegismaster tcp conns cont _ _ _ ainer cluster _ | tcp连接数（集群） |  |  |  |
| aegismaster ntp container h _ _ _ ost | NTP（单机） | NTP | 暂无 | 暂无 |
| aegismaster ntp container s _ _ _ erverrole | NTP（服务角色） |  |  |  |
| 4 |  |  | > 文档版 | 本：2026072 |

|  |  | 安 | 骑士运维指南· | 安骑士运维手册 |
|---|---|---|---|---|
| aegismaster ntp container c _ _ _ luster | NTP（集群） |  |  |  |
| aegismaster process count _ _ _ container host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismaster process count _ _ _ container cluster _ | 进程数（服务角色） |  |  |  |
| aegismaster process count _ _ _ container host _ | 进程数（集群） |  |  |  |
| aegismaster nginx container _ _ host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegismaster nginx container _ _ serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegismaster nginx container _ _ cluster _ | nginx QPS（集群） |  |  |  |
| aegismaster health containe _ _ r host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismaster health containe _ _ r serverrole _ | 健康检查（服务角色） |  |  |  |
| aegismaster health containe _ _ r cluster _ | 健康检查（集群） |  |  |  |

**aegishealthcheck应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegishealthcheck cpu contai _ _ ner host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegishealthcheck cpu contai _ _ ner serverrole _ | CPU使用率（服务角色） |  |  |  |
| aegishealthcheck cpu contai _ _ ner cluster _ | CPU使用率（集群） |  |  |  |

| aegishealthcheck memo con _ _ tainer host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegishealthcheck memo con _ _ tainer serverrole _ | 内存（服务角色） |  |  |  |
| aegishealthcheck memo con _ _ tainer cluster _ | 内存（集群） |  |  |  |
| aegishealthcheck load conta _ _ iner host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegishealthcheck load conta _ _ iner serverrole _ | 负载（服务角色） |  |  |  |
| aegishealthcheck load conta _ _ iner cluster _ | 负载（集群） |  |  |  |
| aegishealthcheck tcp conns _ _ _ container host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegishealthcheck tcp conns _ _ _ container serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegishealthcheck tcp conns _ _ _ container cluster _ | tcp连接数（集群） |  |  |  |
| aegishealthcheck ntp contai _ _ ner host _ | NTP（单机） | NTP | 暂无 | 暂无 |
| aegishealthcheck ntp contai _ _ ner serverrole _ | NTP（服务角色） |  |  |  |
| aegishealthcheck ntp contai _ _ ner cluster _ | NTP（集群） |  |  |  |
| aegishealthcheck process co _ _ unt container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegishealthcheck process co _ _ unt container cluster _ _ | 进程数（服务角色） |  |  |  |
| aegishealthcheck process co _ _ unt container host _ _ | 进程数（集群） |  |  |  |

| aegishealthcheck nginx cont _ _ ainer host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
|---|---|---|---|---|
| aegishealthcheck nginx cont _ _ ainer serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegishealthcheck nginx cont _ _ ainer cluster _ | nginx QPS（集群） |  |  |  |
| aegishealthcheck health con _ _ tainer host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegishealthcheck health con _ _ tainer serverrole _ | 健康检查（服务角色） |  |  |  |
| aegishealthcheck health con _ _ tainer cluster _ | 健康检查（集群） |  |  |  |

**aegiserver应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegiserver cpu container ho _ _ _ st | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegiserver cpu container se _ _ _ rverrole | CPU使用率（服务角色） |  |  |  |
| aegiserver cpu container clu _ _ _ ster | CPU使用率（集群） |  |  |  |
| aegiserver memo container _ _ _ host | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegiserver memo container _ _ _ serverrole | 内存（服务角色） |  |  |  |
| aegiserver memo container _ _ _ cluster | 内存（集群） |  |  |  |

| aegiserver load container h _ _ _ ost | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 4 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegiserver load container se _ _ _ rverrole | 负载（服务角色） |  |  |  |
| aegiserver load container cl _ _ _ uster | 负载（集群） |  |  |  |
| aegiserver tcp conns contai _ _ _ ner host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegiserver tcp conns contai _ _ _ ner serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegiserver tcp conns contai _ _ _ ner cluster _ | tcp连接数（集群） |  |  |  |
| aegiserver ntp container ho _ _ _ st | NTP（单机） | NTP | 暂无 | 暂无 |
| aegiserver ntp container ser _ _ _ verrole | NTP（服务角色） |  |  |  |
| aegiserver ntp container clu _ _ _ ster | NTP（集群） |  |  |  |
| aegiserver process count co _ _ _ ntainer host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegiserver process count co _ _ _ ntainer cluster _ | 进程数（服务角色） |  |  |  |
| aegiserver process count co _ _ _ ntainer host _ | 进程数（集群） |  |  |  |
| aegiserver nginx container _ _ _ host | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegiserver nginx container _ _ _ serverrole | nginx QPS（服务角色） |  |  |  |
| aegiserver nginx container _ _ _ cluster | nginx QPS（集群） |  |  |  |

| aegiserver health container _ _ _ host | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegiserver health container _ _ _ serverrole | 健康检查（服务角色） |  |  |  |
| aegiserver health container _ _ _ cluster | 健康检查（集群） |  |  |  |

**aegisdetect应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisdetect cpu container h _ _ _ ost | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisdetect cpu container s _ _ _ erverrole | CPU使用率（服务角色） |  |  |  |
| aegisdetect cpu container cl _ _ _ uster | CPU使用率（集群） |  |  |  |
| aegisdetect memo container _ _ host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisdetect memo container _ _ serverrole _ | 内存（服务角色） |  |  |  |
| aegisdetect memo container _ _ cluster _ | 内存（集群） |  |  |  |
| aegisdetect load container _ _ _ host | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisdetect load container s _ _ _ erverrole | 负载（服务角色） |  |  |  |
| aegisdetect load container c _ _ _ luster | 负载（集群） |  |  |  |
| aegisdetect tcp conns conta _ _ _ iner host _ | tcp连接数（单机） |  |  |  |

| 安骑士运维指南·安骑士运维手册 |  |  |  |  |
|---|---|---|---|---|
|  |  | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegisdetect tcp conns conta _ _ _ iner serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegisdetect tcp conns conta _ _ _ iner cluster _ | tcp连接数（集群） |  |  |  |
| aegisdetect ntp container h _ _ _ ost | NTP（单机） | NTP | 暂无 | 暂无 |
| aegisdetect ntp container s _ _ _ erverrole | NTP（服务角色） |  |  |  |
| aegisdetect ntp container cl _ _ _ uster | NTP（集群） |  |  |  |
| aegisdetect process count c _ _ _ ontainer host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisdetect process count c _ _ _ ontainer cluster _ | 进程数（服务角色） |  |  |  |
| aegisdetect process count c _ _ _ ontainer host _ | 进程数（集群） |  |  |  |
| aegisdetect nginx container _ _ host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegisdetect nginx container _ _ serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegisdetect nginx container _ _ cluster _ | nginx QPS（集群） |  |  |  |
| aegisdetect health container _ _ host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisdetect health container _ _ serverrole _ | 健康检查（服务角色） |  |  |  |
| aegisdetect health container _ _ cluster _ | 健康检查（集群） |  |  |  |

**aegisbiz应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisbiz cpu container host _ _ _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisbiz cpu container serv _ _ _ errole | CPU使用率（服务角色） |  |  |  |
| aegisbiz cpu container clust _ _ _ er | CPU使用率（集群） |  |  |  |
| aegisbiz memo container ho _ _ _ st | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisbiz memo container se _ _ _ rverrole | 内存（服务角色） |  |  |  |
| aegisbiz memo container cl _ _ _ uster | 内存（集群） |  |  |  |
| aegisbiz load container host _ _ _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisbiz load container serv _ _ _ errole | 负载（服务角色） |  |  |  |
| aegisbiz load container clus _ _ _ ter | 负载（集群） |  |  |  |
| aegisbiz tcp conns containe _ _ _ r host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegisbiz tcp conns containe _ _ _ r serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegisbiz tcp conns containe _ _ _ r cluster _ | tcp连接数（集群） |  |  |  |
| aegisbiz ntp container host _ _ _ | NTP（单机） | NTP | 暂无 | 暂无 |
| aegisbiz ntp container serve _ _ _ rrole | NTP（服务角色） |  |  |  |
| > 文档版本：20260729 |  |  |  | 7 |

| aegisbiz ntp container clust _ _ _ er | NTP（集群） |  |  |  |
|---|---|---|---|---|
| aegisbiz process count cont _ _ _ ainer host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisbiz process count cont _ _ _ ainer cluster _ | 进程数（服务角色） |  |  |  |
| aegisbiz process count cont _ _ _ ainer host _ | 进程数（集群） |  |  |  |
| aegisbiz nginx container ho _ _ _ st | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegisbiz nginx container ser _ _ _ verrole | nginx QPS（服务角色） |  |  |  |
| aegisbiz nginx container clu _ _ _ ster | nginx QPS（集群） |  |  |  |
| aegisbiz health container ho _ _ _ st | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisbiz health container se _ _ _ rverrole | 健康检查（服务角色） |  |  |  |
| aegisbiz health container cl _ _ _ uster | 健康检查（集群） |  |  |  |

**aegisassets应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisassets cpu container h _ _ _ ost | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisassets cpu container s _ _ _ erverrole | CPU使用率（服务角色） |  |  |  |
| aegisassets cpu container cl _ _ _ uster | CPU使用率（集群） |  |  |  |

| aegisassets memo container _ _ host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegisassets memo container _ _ serverrole _ | 内存（服务角色） |  |  |  |
| aegisassets memo container _ _ cluster _ | 内存（集群） |  |  |  |
| aegisassets load container _ _ _ host | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 3 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisassets load container s _ _ _ erverrole | 负载（服务角色） |  |  |  |
| aegisassets load container c _ _ _ luster | 负载（集群） |  |  |  |
| aegisassets tcp conns conta _ _ _ iner host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegisassets tcp conns conta _ _ _ iner serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegisassets tcp conns conta _ _ _ iner cluster _ | tcp连接数（集群） |  |  |  |
| aegisassets ntp container h _ _ _ ost | NTP（单机） | NTP | 暂无 | 暂无 |
| aegisassets ntp container s _ _ _ erverrole | NTP（服务角色） |  |  |  |
| aegisassets ntp container cl _ _ _ uster | NTP（集群） |  |  |  |
| aegisassets process count c _ _ _ ontainer host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisassets process count c _ _ _ ontainer cluster _ | 进程数（服务角色） |  |  |  |
| aegisassets process count c _ _ _ ontainer host _ | 进程数（集群） |  |  |  |

| aegisassets nginx container _ _ host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
|---|---|---|---|---|
| aegisassets nginx container _ _ serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegisassets nginx container _ _ cluster _ | nginx QPS（集群） |  |  |  |
| aegisassets health container _ _ host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisassets health container _ _ serverrole _ | 健康检查（服务角色） |  |  |  |
| aegisassets health container _ _ cluster _ | 健康检查（集群） |  |  |  |

**aegisdefence应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisdefence cpu container _ _ _ host | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisdefence cpu container _ _ _ serverrole | CPU使用率（服务角色） |  |  |  |
| aegisdefence cpu container _ _ _ cluster | CPU使用率（集群） |  |  |  |
| aegisdefence memo contain _ _ er host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisdefence memo contain _ _ er serverrole _ | 内存（服务角色） |  |  |  |
| aegisdefence memo contain _ _ er cluster _ | 内存（集群） |  |  |  |

| aegisdefence load container _ _ host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegisdefence load container _ _ serverrole _ | 负载（服务角色） |  |  |  |
| aegisdefence load container _ _ cluster _ | 负载（集群） |  |  |  |
| aegisdefence tcp conns con _ _ _ tainer host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegisdefence tcp conns con _ _ _ tainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegisdefence tcp conns con _ _ _ tainer cluster _ | tcp连接数（集群） |  |  |  |
| aegisdefence ntp container _ _ _ host | NTP（单机） | NTP | 暂无 | 暂无 |
| aegisdefence ntp container _ _ _ serverrole | NTP（服务角色） |  |  |  |
| aegisdefence ntp container _ _ _ cluster | NTP（集群） |  |  |  |
| aegisdefence process count _ _ container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisdefence process count _ _ container cluster _ _ | 进程数（服务角色） |  |  |  |
| aegisdefence process count _ _ container host _ _ | 进程数（集群） |  |  |  |
| aegisdefence nginx containe _ _ r host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegisdefence nginx containe _ _ r serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegisdefence nginx containe _ _ r cluster _ | nginx QPS（集群） |  |  |  |

| aegisdefence health contain _ _ er host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegisdefence health contain _ _ er serverrole _ | 健康检查（服务角色） |  |  |  |
| aegisdefence health contain _ _ er cluster _ | 健康检查（集群） |  |  |  |

**aegismatcher应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegismatcher cpu container _ _ host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismatcher cpu container _ _ serverrole _ | CPU使用率（服务角色） |  |  |  |
| aegismatcher cpu container _ _ cluster _ | CPU使用率（集群） |  |  |  |
| aegismatcher memo contain _ _ er host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismatcher memo contain _ _ er serverrole _ | 内存（服务角色） |  |  |  |
| aegismatcher memo contain _ _ er cluster _ | 内存（集群） |  |  |  |
| aegismatcher load container _ _ host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismatcher load container _ _ serverrole _ | 负载（服务角色） |  |  |  |
| aegismatcher load container _ _ cluster _ | 负载（集群） |  |  |  |
| aegismatcher tcp conns con _ _ _ tainer host _ | tcp连接数（单机） |  |  |  |

|  |  | 安 | 骑士运维指南· | 安骑士运维手册 |
|---|---|---|---|---|
|  |  | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegismatcher tcp conns con _ _ _ tainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegismatcher tcp conns con _ _ _ tainer cluster _ | tcp连接数（集群） |  |  |  |
| aegismatcher ntp container _ _ _ host | NTP（单机） | NTP | 暂无 | 暂无 |
| aegismatcher ntp container _ _ _ serverrole | NTP（服务角色） |  |  |  |
| aegismatcher ntp container _ _ _ cluster | NTP（集群） |  |  |  |
| aegismatcher process count _ _ container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismatcher process count _ _ container cluster _ _ | 进程数（服务角色） |  |  |  |
| aegismatcher process count _ _ container host _ _ | 进程数（集群） |  |  |  |
| aegismatcher nginx contain _ _ er host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegismatcher nginx contain _ _ er serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegismatcher nginx contain _ _ er cluster _ | nginx QPS（集群） |  |  |  |
| aegismatcher health contain _ _ er host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismatcher health contain _ _ er serverrole _ | 健康检查（服务角色） |  |  |  |
| aegismatcher health contain _ _ er cluster _ | 健康检查（集群） |  |  |  |

**newsas应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| newsas cpu container host _ _ _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| newsas cpu container serve _ _ _ rrole | CPU使用率（服务角色） |  |  |  |
| newsas cpu container cluste _ _ _ r | CPU使用率（集群） |  |  |  |
| newsas memo container ho _ _ _ st | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| newsas memo container ser _ _ _ verrole | 内存（服务角色） |  |  |  |
| newsas memo container clu _ _ _ ster | 内存（集群） |  |  |  |
| newsas load container host _ _ _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| newsas load container serv _ _ _ errole | 负载（服务角色） |  |  |  |
| newsas load container clust _ _ _ er | 负载（集群） |  |  |  |
| newsas tcp conns container _ _ _ host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| newsas tcp conns container _ _ _ serverrole _ | tcp连接数（服务角色） |  |  |  |
| newsas tcp conns container _ _ _ cluster _ | tcp连接数（集群） |  |  |  |
| newsas ntp container host _ _ _ | NTP（单机） | NTP | 暂无 | 暂无 |
| newsas ntp container server _ _ _ role | NTP（服务角色） |  |  |  |
| 8 |  |  | > 文档版 | 本：2026072 |

|  |  | 安 | 骑士运维指南· | 安骑士运维手册 |
|---|---|---|---|---|
| newsas ntp container cluste _ _ _ r | NTP（集群） |  |  |  |
| newsas process count conta _ _ _ iner host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| newsas process count conta _ _ _ iner cluster _ | 进程数（服务角色） |  |  |  |
| newsas process count conta _ _ _ iner host _ | 进程数（集群） |  |  |  |
| newsas nginx container hos _ _ _ t | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| newsas nginx container ser _ _ _ verrole | nginx QPS（服务角色） |  |  |  |
| newsas nginx container clus _ _ _ ter | nginx QPS（集群） |  |  |  |
| newsas health container ho _ _ _ st | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| newsas health container ser _ _ _ verrole | 健康检查（服务角色） |  |  |  |
| newsas health container clu _ _ _ ster | 健康检查（集群） |  |  |  |

**sasfileserver应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| sasfileserver cpu container _ _ _ host | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| sasfileserver cpu container _ _ _ serverrole | CPU使用率（服务角色） |  |  |  |
| sasfileserver cpu container _ _ _ cluster | CPU使用率（集群） |  |  |  |

| sasfileserver memo contain _ _ er host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| sasfileserver memo contain _ _ er serverrole _ | 内存（服务角色） |  |  |  |
| sasfileserver memo contain _ _ er cluster _ | 内存（集群） |  |  |  |
| sasfileserver load container _ _ _ host | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| sasfileserver load container _ _ _ serverrole | 负载（服务角色） |  |  |  |
| sasfileserver load container _ _ _ cluster | 负载（集群） |  |  |  |
| sasfileserver tcp conns cont _ _ _ ainer host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| sasfileserver tcp conns cont _ _ _ ainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| sasfileserver tcp conns cont _ _ _ ainer cluster _ | tcp连接数（集群） |  |  |  |
| sasfileserver ntp container _ _ _ host | NTP（单机） | NTP | 暂无 | 暂无 |
| sasfileserver ntp container s _ _ _ erverrole | NTP（服务角色） |  |  |  |
| sasfileserver ntp container c _ _ _ luster | NTP（集群） |  |  |  |
| sasfileserver process count _ _ _ container host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| sasfileserver process count _ _ _ container cluster _ | 进程数（服务角色） |  |  |  |
| sasfileserver process count _ _ _ container host _ | 进程数（集群） |  |  |  |

| sasfileserver nginx containe _ _ r host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
|---|---|---|---|---|
| sasfileserver nginx containe _ _ r serverrole _ | nginx QPS（服务角色） |  |  |  |
| sasfileserver nginx containe _ _ r cluster _ | nginx QPS（集群） |  |  |  |
| sasfileserver health containe _ _ r host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| sasfileserver health containe _ _ r serverrole _ | 健康检查（服务角色） |  |  |  |
| sasfileserver health containe _ _ r cluster _ | 健康检查（集群） |  |  |  |

**aegismetadata应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegismetadata cpu containe _ _ r host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismetadata cpu containe _ _ r serverrole _ | CPU使用率（服务角色） |  |  |  |
| aegismetadata cpu containe _ _ r cluster _ | CPU使用率（集群） |  |  |  |
| aegismetadata memo contai _ _ ner host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismetadata memo contai _ _ ner serverrole _ | 内存（服务角色） |  |  |  |
| aegismetadata memo contai _ _ ner cluster _ | 内存（集群） |  |  |  |

| aegismetadata load contain _ _ er host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegismetadata load contain _ _ er serverrole _ | 负载（服务角色） |  |  |  |
| aegismetadata load contain _ _ er cluster _ | 负载（集群） |  |  |  |
| aegismetadata tcp conns co _ _ _ ntainer host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegismetadata tcp conns co _ _ _ ntainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| aegismetadata tcp conns co _ _ _ ntainer cluster _ | tcp连接数（集群） |  |  |  |
| aegismetadata ntp containe _ _ r host _ | NTP（单机） | NTP | 暂无 | 暂无 |
| aegismetadata ntp containe _ _ r serverrole _ | NTP（服务角色） |  |  |  |
| aegismetadata ntp containe _ _ r cluster _ | NTP（集群） |  |  |  |
| aegismetadata process coun _ _ t container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismetadata process coun _ _ t container cluster _ _ | 进程数（服务角色） |  |  |  |
| aegismetadata process coun _ _ t container host _ _ | 进程数（集群） |  |  |  |
| aegismetadata nginx contai _ _ ner host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegismetadata nginx contai _ _ ner serverrole _ | nginx QPS（服务角色） |  |  |  |
| 2 |  |  | > 文档版 | 本：2026072 |

|  |  | 安 | 骑士运维指南· | 安骑士运维手册 |
|---|---|---|---|---|
| aegismetadata nginx contai _ _ ner cluster _ | nginx QPS（集群） |  |  |  |
| aegismetadata health contai _ _ ner host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegismetadata health contai _ _ ner serverrole _ | 健康检查（服务角色） |  |  |  |
| aegismetadata health contai _ _ ner cluster _ | 健康检查（集群） |  |  |  |

**baselinecheck应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| baselinecheck cpu container _ _ host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| baselinecheck cpu container _ _ serverrole _ | CPU使用率（服务角色） |  |  |  |
| baselinecheck cpu container _ _ cluster _ | CPU使用率（集群） |  |  |  |
| baselinecheck memo contai _ _ ner host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| baselinecheck memo contai _ _ ner serverrole _ | 内存（服务角色） |  |  |  |
| baselinecheck memo contai _ _ ner cluster _ | 内存（集群） |  |  |  |
| baselinecheck load containe _ _ r host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| baselinecheck load containe _ _ r serverrole _ | 负载（服务角色） |  |  |  |
| baselinecheck load containe _ _ r cluster _ | 负载（集群） |  |  |  |

| baselinecheck tcp conns co _ _ _ ntainer host _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
|---|---|---|---|---|
| baselinecheck tcp conns co _ _ _ ntainer serverrole _ | tcp连接数（服务角色） |  |  |  |
| baselinecheck tcp conns co _ _ _ ntainer cluster _ | tcp连接数（集群） |  |  |  |
| baselinecheck ntp container _ _ host _ | NTP（单机） | NTP | 暂无 | 暂无 |
| baselinecheck ntp container _ _ serverrole _ | NTP（服务角色） |  |  |  |
| baselinecheck ntp container _ _ cluster _ | NTP（集群） |  |  |  |
| baselinecheck process count _ _ container host _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| baselinecheck process count _ _ container cluster _ _ | 进程数（服务角色） |  |  |  |
| baselinecheck process count _ _ container host _ _ | 进程数（集群） |  |  |  |
| baselinecheck nginx contain _ _ er host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| baselinecheck nginx contain _ _ er serverrole _ | nginx QPS（服务角色） |  |  |  |
| baselinecheck nginx contain _ _ er cluster _ | nginx QPS（集群） |  |  |  |
| baselinecheck health contai _ _ ner host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| baselinecheck health contai _ _ ner serverrole _ | 健康检查（服务角色） |  |  |  |
| 4 |  |  | > 文档版 | 本：2026072 |

| baselinecheck health contai _ _ ner cluster _ | 健康检查（集群） |  |  |  |
|---|---|---|---|---|

**aegisimageanalyzer应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisimageanalyzer cpu con _ _ tainer host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisimageanalyzer cpu con _ _ tainer serverrole _ | CPU使用率（服务角色） |  |  |  |
| aegisimageanalyzer cpu con _ _ tainer cluster _ | CPU使用率（集群） |  |  |  |
| aegisimageanalyzer memo c _ _ ontainer host _ | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisimageanalyzer memo c _ _ ontainer serverrole _ | 内存（服务角色） |  |  |  |
| aegisimageanalyzer memo c _ _ ontainer cluster _ | 内存（集群） |  |  |  |
| aegisimageanalyzer load co _ _ ntainer host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 av _ g > 1 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisimageanalyzer load co _ _ ntainer serverrole _ | 负载（服务角色） |  |  |  |
| aegisimageanalyzer load co _ _ ntainer cluster _ | 负载（集群） |  |  |  |
| aegisimageanalyzer tcp con _ _ ns container host _ _ | tcp连接数（单机） | tcp连接的最大值和平均值 | 暂无 | 暂无 |
| aegisimageanalyzer tcp con _ _ ns container serverrole _ _ | tcp连接数（服务角色） |  |  |  |
| aegisimageanalyzer tcp con _ _ ns container cluster _ _ | tcp连接数（集群） |  |  |  |

| aegisimageanalyzer ntp con _ _ tainer host _ | NTP（单机） | NTP | 暂无 | 暂无 |
|---|---|---|---|---|
| aegisimageanalyzer ntp con _ _ tainer serverrole _ | NTP（服务角色） |  |  |  |
| aegisimageanalyzer ntp con _ _ tainer cluster _ | NTP（集群） |  |  |  |
| aegisimageanalyzer process _ count container host _ _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisimageanalyzer process _ count container cluster _ _ _ | 进程数（服务角色） |  |  |  |
| aegisimageanalyzer process _ count container host _ _ _ | 进程数（集群） |  |  |  |
| aegisimageanalyzer nginx c _ _ ontainer host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegisimageanalyzer nginx c _ _ ontainer serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegisimageanalyzer nginx c _ _ ontainer cluster _ | nginx QPS（集群） |  |  |  |
| aegisimageanalyzer health c _ _ ontainer host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisimageanalyzer health c _ _ ontainer serverrole _ | 健康检查（服务角色） |  |  |  |
| aegisimageanalyzer health c _ _ ontainer cluster _ | 健康检查（集群） |  |  |  |

### 容量规划

安骑士基于可用区内的NC数量ExpectedNcCountOfLocalZone（当前机房的机器预期数量）计算出规格。 每增加500台NC，BasicThinCluster和SasCluster都需增加2台物理机（NC和ECS的比例按照1:6，500 台NC对应3000台ECS）。

|  | 重要安骑士最大规格只能支持到8000台NC，如超过上限需联系安骑士研发介入。 |  |
|---|---|---|

**V3.16.2~V3.18.1版本容量规划（on Tianji）**

**资源规格定义**

| 安骑士规格 | BasicThinCluster | SasCluster | 计算公式（整朵云的机器预期数量） |
|---|---|---|---|
| small | 2 | 2 | ExpectedNcCountOfLocalZone < 500 |
| standard | 2~4 | 2~4 | ExpectedNcCountOfLocalZone < 1000 |
| large | 4~8 | 4~8 | ExpectedNcCountOfLocalZone < 2000 |
| xlarge | 8~16 | 8~16 | ExpectedNcCountOfLocalZone < 4000 |
| 2xlarge | 16~32 | 16~32 | ExpectedNcCountOfLocalZone < 8000 |

**MiniRDS资源规格定义**

x86数据库规格

| 容量规格 | small |  | standard |  | large |  | xlarge |  | 2xlarge |  |
|---|---|---|---|---|---|---|---|---|---|---|
| 数据库实例名称 | 数据库规格 | 磁盘 (单位:G) | 数据库规格 | 磁盘 (单位:G) | 数据库规格 | 磁盘 (单位:G) | 数据库规格 | 磁盘 (单位:G) | 数据库规格 | 磁盘 (单位:G) |
| aegis erver | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 |
| healt hche ck | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| defe nder | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.xl arge | 200 |

| aegis vul | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
|---|---|---|---|---|---|---|---|---|---|---|
| mord or | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.xl arge | 200 |
| aegis biz | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 |
| aegis asset s | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| aegis dete ct | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 |
| aegis mast er | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| suspi cious | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| banff web | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 |
| aegis virus scan | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| sasfil eserv er | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 |

| aegis meta data | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 |
|---|---|---|---|---|---|---|---|---|---|---|
| basel ine | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 |
| news as | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 |
| aegis matc her | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.xl arge | 200 |
| aegis defe nce | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.xl arge | 200 |
| mag piebr idge db | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.la rge | - | rds.m ys2.la rge | - |
| yund unap i | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.la rge | - | rds.m ys2.la rge | - |
| yund unlu ban | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.la rge | - | rds.m ys2.la rge | - |
| data sync | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.la rge | - | rds.m ys2.la rge | - |

arm/sw数据库规格

| 数据库实例名称 | small | standard | large | xlarge | 2xlarge |
|---|---|---|---|---|---|

| aegiserve r | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |
|---|---|---|---|---|---|
| healthch eck | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| defender | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| aegisvul | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| mordor | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| aegisbiz | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |
| aegisasse ts | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| aegisdete ct | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
| aegismas ter | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| suspiciou s | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| banffweb | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
| aegisviru sscan | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| sasfileser ver | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
| aegismet adata | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |

| baseline | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |
|---|---|---|---|---|---|
| newsas | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
| aegismat cher | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| aegisdefe nce | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| magpiebr idgedb | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| yunduna pi | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| yundunlu ban | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| datasync | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |

**Oss 、Sls-inner资源容量规划**

| 规格 | OSS容量(GB) | sls-Inner盘古磁盘总用 （GB） | sls-Inner盘古磁盘总用（GB） |
|---|---|---|---|
|  | 2GB/单台机器 | 0.1GB/单台机器 | 0.1GB/单台机器 |
| small | 7000 | 350 | 350 |
| standar d | 14000 | 700 | 700 |
| large | 28000 | 1400 | 1400 |
| xlarge | 56000 | 2800 | 2800 |
| 2xlarge | 112000 | 5600 | 5600 |

**Tair资源容量规划**

| 规格 | tair 各namespace所需分配配额（MB） |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | 92 | 381 | 499 | 66 3 | 106 | 690 | 478 | 692 | 总计 (MB) | 总计 (MB) |
| smal l | 512 | 512 | 512 | 25 6 | 256 | 256 | 256 | 256 | 2816 | 2816 |
| stan dard | 512 | 512 | 512 | 25 6 | 256 | 256 | 256 | 256 | 2816 | 2816 |
| large | 512 | 512 | 512 | 25 6 | 256 | 256 | 256 | 256 | 2816 | 2816 |
| xlarg e | 1024 | 102 4 | 102 4 | 51 2 | 512 | 512 | 512 | 512 | 5632 | 5632 |
| 2xlar ge | 联系研发确认 |  |  |  |  |  |  |  |  |  |

**MetaQ资源容量规划**

| 规格 | metaq容量规划 (单位:万条) |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  | 进程消息 | 网络消息 | 文件消息 | 进程写文件消息 | 插件心跳消息 | 其他 | 总计 (单位:万条) |
|  | 240 | 20 | 5 | 15 | 60 | 140 | 0.058 |
| small | 84 | 7 | 1.75 | 5.25 | 21 | 49 | 203 |
| standar d | 168 | 14 | 3.5 | 10.5 | 42 | 98 | 406 |
| large | 336 | 28 | 7 | 21 | 84 | 196 | 812 |
| xlarge | 672 | 56 | 14 | 42 | 168 | 392 | 1624 |
| 2xlarge | 1344 | 112 | 28 | 84 | 336 | 784 | 3248 |

**V3.18.2及之后版本容量规划（on PaaS）**

**资源规格定义**

| 安骑士规格 | 计算公式（整朵云的机器预期数量） | 备注 |
|---|---|---|
| small | ExpectedNcCountOfLocalZone < 500 |  |
| standard | ExpectedNcCountOfLocalZone < 1000 |  |
| standard plus 1 _ _ | ExpectedNcCountOfLocalZone < 1500 | 3.18.3之后版本支持 |
| large | ExpectedNcCountOfLocalZone < 2000 |  |
| large plus 1 _ _ | ExpectedNcCountOfLocalZone < 3000 | 3.18.3之后版本支持 |
| xlarge | ExpectedNcCountOfLocalZone < 4000 |  |
| xlarge plus 1 _ _ | ExpectedNcCountOfLocalZone < 5000 | 3.18.3之后版本支持 |
| xlarge plus 2 _ _ | ExpectedNcCountOfLocalZone < 6000 | 3.18.3之后版本支持 |
| xlarge plus 3 _ _ | ExpectedNcCountOfLocalZone < 7000 | 3.18.3之后版本支持 |
| 2xlarge | ExpectedNcCountOfLocalZone < 8000 |  |

**安骑士（On PaaS）部署规格定义**

服务容量规划.xlsx

**MiniRDS 规格定义**

安骑士数据库容量规划.xlsx

**Oss 、Sls-inner资源容量规划**

| 规格 | OSS容量(GB) | sls-Inner盘古磁盘总用（GB） |
|---|---|---|
|  | 2GB/单台机器 | 0.1GB/单台机器 |
| small | 7000 | 350 |
| standard | 14000 | 700 |

| standard plus 1 _ _ | 21000 | 1050 |
|---|---|---|
| large | 28000 | 1400 |
| large plus 1 _ _ | 42000 | 2100 |
| xlarge | 56000 | 2800 |
| xlarge plus 1 _ _ | 70000 | 3500 |
| xlarge plus 2 _ _ | 84000 | 4200 |
| xlarge plus 3 _ _ | 98000 | 4900 |
| 2xlarge | 112000 | 5600 |

**Tair资源容量规划**

| 规格 | tair 各namespace所需分配配额（MB） |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | 92 | 381 | 499 | 663 | 106 | 690 | 478 | 692 | 总计 (MB) |
| small | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| stand ard | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| stand ard pl _ us 1 _ | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| large | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| large _ plus _ 1 | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| xlarge | 1024 | 1024 | 1024 | 512 | 512 | 512 | 512 | 512 | 5632 |

| xlarge plus _ _ 1 | 1024 | 1024 | 1024 | 512 | 512 | 512 | 512 | 512 | 5632 |
|---|---|---|---|---|---|---|---|---|---|
| xlarge plus _ _ 2 | 1024 | 1024 | 1024 | 512 | 512 | 512 | 512 | 512 | 5632 |
| xlarge plus _ _ 3 | 1024 | 1024 | 1024 | 512 | 512 | 512 | 512 | 512 | 5632 |
| 2xlar ge | 联系研发确认 |  |  |  |  |  |  |  |  |

**MetaQ资源容量规划**

| 规格 | metaq容量规划 (单位:万条) |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | 进程消息 | 网络消息 | 文件消息 | 进程写文件消息 | 插件心跳消息 | 其他 |
|  | 240 | 20 | 5 | 15 | 60 | 140 |
| small | 84 | 7 | 1.75 | 5.25 | 21 | 49 |
| standard | 168 | 14 | 3.5 | 10.5 | 42 | 98 |
| standard _ plus 1 _ | 252 | 21 | 5.25 | 15.75 | 63 | 147 |
| large | 336 | 28 | 7 | 21 | 84 | 196 |
| large plus _ 1 _ | 504 | 42 | 10.5 | 31.5 | 126 | 294 |
| xlarge | 672 | 56 | 14 | 42 | 168 | 392 |
| xlarge plu _ s 1 _ | 840 | 70 | 17.5 | 52.5 | 210 | 490 |

| xlarge plu _ s 2 _ | 1008 | 84 | 21 | 63 | 252 | 588 |
|---|---|---|---|---|---|---|
| xlarge plu _ s 3 _ | 1176 | 98 | 24.5 | 73.5 | 294 | 686 |
| 2xlarge | 1344 | 112 | 28 | 84 | 336 | 784 |

### XC支持

**企业版与自主可控能力差异**

企业版与自主可控能力差异主要是平台差异导致： x86企业版与x86海光能力100%一致。 arm飞腾、arm鲲鹏与企业版能力差异在30%以内，未来有计划对齐。 sw申威与x86企业版能力差异50%以内，未来暂无计划对齐。

**主机安全能力差异**

| 功能 | x86 | arm | sw | 描述 |
|---|---|---|---|---|
| 总览 | 100 % | 100 % | 100 % | 展示需要重点关注的资产、漏洞、异常、配置缺陷、事件等信息总览。 |
| 主机资产 | 100 % | 100 % | 100 % | 提供服务器安全状态相关信息。例如，服务器的防护状态、分组、专有网络 VPC等统计信息，以及统计区分所有服务器、存在风险的服务器、未受保护的服务器、未启动的服务器和新增服务器的资产数量。 单击目标服务器名称可查看详细信息，包括漏洞信息、安全告警处理、基线检查、资产指纹调查等。 |
| 主机指纹 | 100 % | 100 % | 100 % | 周期性采集服务器的账号、端口、进程、中间件、软件、计划任务、启动项等数据。 端口：清点主机端口监听信息，包括监听端口、网络协议、对应的进程、IP地址最新采集时间等信息。 软件：清点主机软件安装的资产信息，包括具体软件资产名称、软件版本、软件安装目录、最新采集时间等信息。 进程：清点主机进程信息，包括进程名、进程路径、启动参数、启动时间、运行用户、运行权限、pid、父进程、最新采集时间等信息。 账户：清点主机账户信息，包括账户名、登录权限、root权限、用户组、到期时间、上次登录时间、最新采集时间等信息。 计划任务：清点主机的计划任务，包括任务路径、执行命令、任务周期、账户名称，最新采集时间等信息。 |

| 漏洞管理 | 100 % | 100 % | 100 % | 支持检测包括Linux、Windows、Web-CMS、应用漏洞以及应急漏洞五种漏洞类型，针对检测出来的漏洞提供修复方案、验证等操作，提供具体漏洞详情，提供一键扫描功能。 重要部分自主可控操作系统不在支持范围内，需通过规则包适配。 |
|---|---|---|---|---|
| 基线检测 | 100 % | 100 % | 100 % | 自动检测服务器上的系统、账号、数据库、弱密码、合规性配置中存在的风险点，并提供加固建议，支持的资产类型包括常见数据库、系统、中间件等。 重要部分自主可控操作系统不在支持范围，需通过规则包适配。 |
| 云外暴露检查 | 100 % | 100 % | 100 % | 云外暴露检查支持自动分析您的ECS服务器在互联网上的暴露情况，可视化呈现ECS与互联网的通信链路，并集中展示您暴露在公网的ECS的漏洞信息，帮助您快速定位资产在互联网上的异常暴露情况并提供相应漏洞的修复建议。 |
| 病毒防御 | 100 % | 60% | 60 % | 提供病毒查杀和网站后门查杀功能，检测出主流木马病毒、勒索软件、挖矿病毒、DDoS木马后自动隔离查杀。 重要能力差异：arm、sw不支持主动防御、诱捕勒索功能。 |
| 防篡改 | 100 % | 60% | 60 % | 网页防篡改实时监控网站目录并通过备份恢复被篡改的文件或目录，保障重要系统的网站信息不被恶意篡改，防止出现挂马、黑链、非法植入等入侵。 防篡改支持驱动版和rsync版，驱动版支持全部功能，rsync版不支持进程白名单、告警模式、NFS 路径防御，能力是驱动版的60%左右。具体内容，请参见能力差异说明。 重要能力差异：x86支持驱动版和rsync版本，arm/sw仅支持rsync。 |
| 入侵事件告警 | 100 % | 80% | 50 % | 集中展示受影响主机资产的告警信息，包括存在告警服务器的数量、待处理告警总数、需要紧急处理的告警等，其中告警类型覆盖进程异常行为、网站后门、异常登录、恶意进程（云查杀）、敏感文件篡改、异常网络连接、持久化后门、Web应用威胁检测等多种入侵告警类型。 重要能力差异：arm不支持AV/BD检测引擎，仅支持GLE。sw均不支持。 |
| 日志检索 | 100 % | 100 % | 100 % | 提供登录流水、暴力破解、进程快照、网络连接、端口监听快照、账号快照、 进程启动的日志查询 |

| 客户端安装 | 100 % | 100 % | 100 % | 支持查看离线的服务器，选择重新安装，提供安装教程，可选择指定服务器卸载安骑士插件。 |
|---|---|---|---|---|
| 防护模式 | 100 % | 50% | 0% | 提供业务优先和防护优先两种模式，供不同的业务场景使用。 重要能力差异：arm版本不支持自保护功能，sw版本不支持防护模式设置。 |

**态势感知能力差异**

| 功能 | x86 | ar m | sw | 描述 |
|---|---|---|---|---|
| 总览 | 100 % | 100 % | 100 % | 提供整体安全威胁概览信息，包括总体安全评分、防护资产状态、待处理风险告警、已处理风险等态势信息。 |
| 安全大屏 | 100 % | 100 % | 100 % | 提供基于态势感知的大屏展示，将安全攻防数据转化并呈现到安全大屏上， 展示包括资产、漏洞、基线、攻击来源、攻击分布等网络安全态势信息。 |
| 安全告警 | 100 % | 80 % | 50 % | 提供如下类型告警：进程异常行为，网站后门，异常登录，敏感文件篡改， 恶意进程（云查杀），异常网络连接，Web应用威胁检测，按照紧急，可疑，提醒三种程度告警，展示受影响资产和最新告警时间。 重要能力差异：arm检测引擎不支持AV/BD，仅支持GLE。sw均不支持。 |
| 攻击分析 | 100 % | 100 % | 100 % | 展示最近7天、30天攻击趋势和攻击类型分布。 包括SSH暴力破解、RDP暴力破解、SQL Server暴力破解、MySQL暴力破解、FTP暴力破解、远程文件包含、路径遍历、越权访问、CSRF、 SQL注入，XSS攻击，反弹shell，代码执行等攻击行为。 提供展示包括攻击时间，攻击来源，被攻击资产，攻击次数，风险等级，攻击类型等具体信息。 |
| 云产品检查 | 100 % | 100 % | 100 % | 从网络访问控制、数据安全两个维度提供云产品安全配置检查，涉及的云产品检查项包括RDS白名单，MongoDB白名单，Redis白名单，OSS Bucket权限设置，RDS数据库安全策略，ECS自动快照，ECS安全组策略等，并根据检查结果定义低、中、高风险等级，支持手工启动检查以及周期性自动检查，并对检查结果进行验证或者加白操作。 |
| 应用白名单 | 100 % | 90 % | 0% | 通过采集将需要重点防御的服务器加入到白名单中，通过检测白名单中指定的应用程序区分可信、可疑和恶意程序，防止未经白名单授权的程序运行。 重要能力差异：arm不支持拦截模式。sw均不支持。 |

| 资产中心 | 100 % | 100 % | 100 % | 提供服务器安全状态相关信息，例如服务器的防护状态、分组、专有网络 VPC等统计信息，统计区分所有服务器、存在风险的服务器、未受保护的服务器、未启动的服务器和新增服务器的资产数量。 提供云产品安全状态相关信息，支持负载均衡、NAT网关。 |
|---|---|---|---|---|
| 安全报告 | 100 % | 80 % | 80 % | 提供报表查询功能，可根据报表名称检索历史报表，可按日，周，月自定义报表任务，发送到指定邮箱。 报表内容可选：安全评分、资产风险分布、安全告警趋势、主动防御趋势、 防篡改趋势、漏洞趋势、基线问题趋势、攻击数量趋势。 重要能力差异：arm/sw不支持报告导出。 |

**当前各模块适配情况**

| 模块 | x86（企业版、海光） | arm（飞腾、鲲鹏） | sw（申威） |
|---|---|---|---|
| 客户端 | 100% | 50% （不支持AliHips、AliSecGuard、 AliNet） | 50% （不支持AliHips、AliSecGuard、 AliNet） |
| 服务端 | 100% | 99% （不支持报告导出） | 80% （不支持报告导出，版本落后于x86 和arm） |
| 前端 | 100% | 100% | 100% |
| 计算引擎 | 100% | 100% | 100% |
| 检测引擎 | 100% | 50% （不支持AV、BD引擎） | 0% （所有检测引擎都不支持） |

**一云多芯支持情况**

一云多芯的主要包括异构同城容灾（主备机房的机房级硬件异构）以及异构多Region（中心/单元机房级硬件异构）2大横向场景。 安骑士对一云多芯的支持情况如下：

| 场景 | 支持情况 |
|---|---|
| 异构同城容灾（x86+arm） 主备机房的机房级硬件异构 | 支持 （部分能力在arm机房不生效，如主动防御、自保护） |

| 异构多Region（x86+arm） 中心/单元机房级硬件异构 | 支持 |
|---|---|

### 热升级

安骑士默认支持热升级，无需额外运维操作。

## 安骑士运维操作

### 登录飞天基础运维平台

**前提条件**

已从部署人员或管理员处获取Apsara Uni-manager运维控制台的访问地址、用户名和密码。 Apsara Uni-manager运维控制台访问地址格式为 `region-id.ops.console.intranet-domain-`

```
id.com 。
```

推荐使用Chrome浏览器。

**操作步骤**

1. 打开浏览器。
2. 在地址栏中，输入Apsara Uni-manager运维控制台的访问地址 `region-id.aso.intranet-domain-`
`id.com` ，按回车键。

**说明**

您可以单击右上角的当前语言切换其它语言。当前支持简体中文、英文、繁体中文三种语言切换。
3. 输入正确的用户名及密码。

**说明**

登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。 若连续输入密码错误三次，系统将启动图片验证码登录功能；若连续输入错误五次，账户将被锁定，请联系管理员进行激活。 首次登录Apsara Uni-manager运维控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。 为提高安全性，密码必须满足以下要求： 必须包含英文大小写字母。 必须包含阿拉伯数字（0~9）。 必须包含特殊符号，包括感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等。 密码长度为10~20个字符。
4. 单击**账号登录**。
5. 在Apsara Uni-manager运维控制台的顶部菜单栏，选择**平台运维** > **飞天基础运维平台**。

### 客户端状态检查

检查安骑士客户端以下状态信息，确定安骑士客户端正常运行。

**客户端日志**

客户端日志存放在进程文件所在目录层级data目录下， 如/usr/local/aegis/aegis_client/aegis_xx_xx/data。 客户端日志按照日期存储：data.1-data.7

**客户端在线状态**

执行以下命令，查看客户端在线状态。

```
 ps -aux | grep AliYunDun
```

**网络连接状态**

执行以下命令，查看客户端是否与服务器端正常建立TCP连接。

```
 netstat -tunpe |grep AliYunDun
```

**客户端UUID**

打开客户端日志文件data.x，查看 `Currentuid Ret` 后续字符串，即为当前的UUID。

**客户端进程**

客户端共有两个常运行进程（选择了自动病毒阻断时，会启

```
动 AliHips ）： AliYunDun 、 AliYunDunUpdate 。
```

正常工作时上述两个进程都正常运行。

|  | AliYunDunUpdate |  |
|---|---|---|
| Alibaba Security Aegis Detect Service |  |  |

**说明**

### 检查服务器端（Aegiserver）状态

**背景信息**

参考以下操作步骤，进行安骑士服务器端运行状态检查：

**操作步骤**

1. 执行 `ssh` 宿主机`IP` 命令，登录安骑士服务器端（Aegiserver）所在的宿主机。
2. 执行以下命令，查找安骑士服务器所对应的imageId。

```bash
 docker ps -a |grep aegiserver
```

系统显示如下信息：

```
b9e59994df41 reg.docker.alibabainc.com/aqs/aegiserverlite@sha256:f9d292f54c58646b672a8533a0d78fba534d26d376a194034e884 70d9aa0b3 "/bin/bash /startApp." 2 hours ago Up 2 hours 80/tcp, 7001/tcp, 8005/tcp, 8 009/tcp yundun-aegis.Aegiserverlite__.aegiserverlite.1484712802
```

3. 执行以下命令，进入Docker内部。

```bash
 docker exec -it [imageId] /bin/bash
```

4. 执行以下命令，查看相关Java进程是否正常运行。

```
 ps aux |grep aegiserver
```

正常情况下，系统显示如下信息：

```
root 153 0.6 25.8 2983812 1084588 ? Sl 12:13 1:01 /opt/taobao/java/bin/java -Djava.ut il.logging.config.file=/home/admin/aegiserverlite/.default/conf/logging.properties -D java.util.logging.manager=org.apache.juli.ClassLoaderLogManager -server -Xms2g -Xmx2g -XX:PermSize=96m -XX:MaxPermSize=384m -Xmn1g -XX:+UseConcMarkSweepGC - XX:+UseCMSCompactAtFullCollection -XX:CMSMaxAbortablePrecleanTime=5000 -XX:+CMSClassU nloadingEnabled -XX:+UseCMSInitiatingOccupancyOnly - XX:CMSInitiatingOccupancyFraction=80 -XX:+HeapDumpOnOutOfMemoryError - XX:HeapDumpPath=/home/admin/logs/java.hprof -verbose:gc - Xloggc:/home/admin/logs/gc.log -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Djava.awt. headless=true -Dsun.net.client.defaultConnectTimeout=10000 - Dsun.net.client.defaultReadTimeout=30000 -XX:+DisableExplicitGC -Dfile.encoding=UTF-8 -Ddruid.filters=mergeStat -Ddruid.useGloalDataSourceStat=true - Dproject.name=aegiserverlite -Dcatalina.vendor=alibaba - Djava.security.egd=file:/dev/./urandom -Dlog4j.defaultInitOverride=true -Dorg.apache. tomcat.util.http.ServerCookie.ALLOW_EQUALS_IN_VALUE=true - Dorg.apache.tomcat.util.http.ServerCookie.ALLOW_HTTP_SEPARATORS_IN_V0=true -Djava.end orsed.dirs=/opt/taobao/tomcat/endorsed -classpath /opt/taobao/tomcat/bin/bootstrap.jar:/opt/taobao/tomcat/bin/tomcat-juli.jar -Dcatalin a.logs=/home/admin/aegiserverlite/.default/logs - Dcatalina.base=/home/admin/aegiserverlite/.default -Dcatalina.home=/opt/taobao/tomcat -Djava.io.tmpdir=/home/admin/aegiserverlite/.default/temp org.apache.catalina.startup.Bootstrap - Djboss.server.home.dir=/home/admin/aegiserverlite/.default - Djboss.server.home.url=file:/home/admin/aegiserverlite/.default start
```

5. 执行以下命令，进行健康检查。

```bash
 curl 127.0.0.1:7001/checkpreload.htm
```

如果返回success，表示服务正常。
6. 查看日志。
**协议日志**：/home/admin/aegiserver/logs/AEGIS_MESSAGE.log，查看与客户端上下行协议日志。
**运行日志**：/home/admin/aegiserver/logs/aegis-default.log，查看运行过程中异常的堆栈信息。
**离线日志**：/home/admin/aegiserver/logs/AEGIS_OFFLINE_MESSAGE.log，查看客户端超时掉线
日志。

### 检查更新服务（Aegisupdate）状态

**背景信息**

参考以下操作步骤，进行安骑士更新服务状态检查：

**操作步骤**

1. 执行 `ssh` 宿主机`IP` 命令，登录安骑士服务器端所在的宿主机。
2. 执行以下命令，查找安骑士服务器所对应的imageId。

```bash
 docker ps -a |grep aegiserver
```

3. 执行以下命令，进入Docker内部。

```bash
 docker exec -it [imageId] /bin/bash
```

4. 执行以下命令，查看相关Java进程是否正常运行。

```
 ps aux |grep aegisupdate
```

5. 执行以下命令，进行健康检查。

```bash
 curl 127.0.0.1:7001/checkpreload.htm
```

如果返回success，表示服务正常。

### 检查Defender模块状态

**背景信息**

参考以下操作步骤，进行安骑士Defender模块状态检查：

**操作步骤**

1. 执行 `ssh` 宿主机`IP` 命令，登录安骑士Defender模块所在的宿主机。
2. 执行以下命令，查找安骑士Defender模块对应的imageId。

```bash
 docker ps -a |grep defender
```

3. 执行以下命令，进入Docker内部。

```bash
 docker exec -it [imageId] /bin/bash
```

4. 执行以下命令，查看相关Java进程是否正常运行。

```
 ps aux |grep defender
```

5. 执行如下命令，进行健康检查。

```bash
 curl 127.0.0.1:7001/checkpreload.htm
```

如果返回success，表示服务正常运行。

### 重启安骑士服务

**背景信息**

在安骑士模块出现故障时，可参考以下操作步骤，尝试重启相关服务。

**操作步骤**

1. 执行 `ssh` 宿主机`IP` 命令，登录到安骑士功能模块所在的宿主机。
2. 执行以下命令，查找安骑士功能模块所对应的imageId。
docker ps -a |grep 应用名称
3. 执行以下命令，进入Docker内部。

```bash
 docker exec -it [imageId] /bin/bash
```

4. 重启安骑士相关服务。
重启安骑士客户端服务： Windows系统主机：进入服务管理器，找到服务Alibaba Security Aegis Detect Service，重启该服务。 Linux系统主机，可以使用以下两种方法： 执行 `service aegis restart` 命令，重启服务。 以root权限执行 `killall` `AliYunDun` 命令关闭当前进程后，重新启动/usr/local/aegis/aegis_client/aegis_xx_xx/AliYunDun进程。 a. 执行以下命令，查看相关Java进程的进程id。

|  | ps aux \|grep |
|---|---|
| aegiserver |  |

b. 执行以下命令，关闭当前进程。 `kill -9` 进程 c. 执行以下命令，重启进程。

|  | sudo -u admin |
|---|---|
| /home/admin/aegiserever/bin/jbossctl |  |

d. 执行以下命令，检查进程是否重启成功。

|  | curl |  |
|---|---|---|
| 127.0.0.1:7001/checkpreload.htm |  |  |

重启安骑士更新服务（Aegisupdate）： a. 执行如下命令，查找java的进程id。

|  | ps aux \|grep |  |
|---|---|---|
| aegisupdate |  |  |

b. 执行如下命令，关闭当前进程。 `kill -9` 进程 c. 执行如下命令，重启进程。

|  | sudo -u admin |
|---|---|
| /home/admin/aegisupdate/bin/jbossctl |  |

d. 执行如下命令，查看进程是否重启成功。

|  | curl |  |
|---|---|---|
| 127.0.0.1:7001/checkpreload.htm |  |  |

重启安骑士Defender服务： a. 执行以下命令，查找相关Java进程的进程id。

|  | ps aux \|grep |  |
|---|---|---|
| secure-service |  |  |

b. 执行以下命令，关闭当前进程。 `kill -9` 进程 c. 执行以下命令，重启进程。

|  | sudo -u admin |
|---|---|
| /home/admin/secure-service/bin/jbossctl |  |

d. 执行以下命令，查看进程是否重启成功。

|  | curl |  |
|---|---|---|
| 127.0.0.1:7001/checkpreload.htm |  |  |
