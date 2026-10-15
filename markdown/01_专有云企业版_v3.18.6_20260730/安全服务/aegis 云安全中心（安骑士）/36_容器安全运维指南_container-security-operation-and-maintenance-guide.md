---
title: "云安全中心（安骑士） 容器安全运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 45
source_pdf: "36_容器安全运维指南_container-security-operation-and-maintenance-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/aegis/zh/container-security-operation-and-maintenance-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云安全中心（安骑士） 容器安全运维指南

## 运维文档

### 总体介绍

容器安全是面向不可变基础设施的云原生容器安全统一管理运营平台，以自动化的模式，解决容器持续集成、交付、部署以及运行时的安全问题。 容器安全底层复用安骑士云上资产管理、配置核查、主动防御、安全加固和安全可视化等能力，基于云原生架构优势，可有效发现和阻止容器逃逸，病毒传播、黑客攻击、勒索加密、漏洞利用等风险事件，保护云内云外的容器运行节点、容器、镜像等工作负载安全性，同时满足监管合规要求。 镜像安全扫描功能支持对镜像中存在的高、中危系统漏洞、应用漏洞、恶意样本、配置风险和敏感数据进行检测，并提供漏洞修复方案，为您提供一站式镜像安全风险管理能力。 容器防火墙是容器安全为容器环境提供的防火墙服务。当黑客利用漏洞或恶意镜像入侵容器集群时，容器防火墙会对异常行为进行告警或拦截。

#### 部署架构

#### 部署架构

**V3.18.1版本及之前的版本**

YundunConsole YundunBaseService AegislmageAnalyzer 横向基础能力 Dipper 计算引擎 Aegisbiz AegisSuspicious SasFileserver

**SasCluster**

核心能力 AegisContainerNetwork SasContainerService AegisVirusScan MiniRDS

**服**

**务**

AegisVulnerability AegisHealthCheck AegisDetect

**端**

OSS 检测/防御能力 SLS YaraSlave AegisMaster AegisCloudavbd MetaQ/Diamond Aegiserver Aegisupdate AegisPrivateCloudEngine AegisCloudavira Tair/SchedulerX 客户端管理检测引擎

**中间件**

**BasicThinCluster**

AliYunDun AliYunDunUpdate sas-jenkins-plugin sas-image-scanner

**客**

**户**

ECS或云外主机（ACK或自建K8s节点） ECS或云外主机（Jenkins节点）

**端**

**V3.18.2版本 -- V3.18.6(2512通用)版本**

YundunConsole YundunBaseService 横向基础能力 AegisPrivateCloudEegine Dipper 检测引擎计算引擎

**yundun-basic**

MiniRDS Aegisbiz AegisContainerNetwork SasContainerDefense SasContainerService OSS 核心能力 SLS AegisHealthCheck AegisVirusScan AegisImageAnalyzer AegisSuspicious MetaQ/Diamond

**服**

**务**

AegisVulnerability AegisDetect BanffAegisWeb AegisMatcher

**端**

检测/防御能力 Tair/SchedulerX

**中间件**

AegisMaster Aegiserver Aegisupdate 客户端管理

**yundun-**

**css(ageis)**

**Paas共享Node池**

AliYunDun AliYunDunUpdate sas-jenkins-plugin sas-image-scanner

**客**

**户**

ECS或云外主机（ACK或自建K8s节点） ECS或云外主机（Jenkins节点）

**端**

**V3.19版本 -- V3.18.6(2512limit)版本**

YundunConsole YundunBaseService 横向基础能力 AegisPrivateCloudEegine Dipper 检测引擎计算引擎

**yundun-basic**

MiniRDS Aegisbiz AegisContainerNetwork SasContainerDefense SasContainerService OSS 核心能力 SLS AegisHealthCheck AegisVirusScan AegisImageAnalyzer AegisSuspicious MetaQ/Diamond

**服**

**务**

AegisVulnerability BanffAegisWeb AegisMatcher

**端**

检测/防御能力 Tair/SchedulerX

**中间件**

AegisMaster Aegiserver Aegisupdate 客户端管理

**yundun-**

**css(ageis)**

**Paas共享Node池**

AliYunDun AliYunDunUpdate sas-jenkins-plugin sas-image-scanner

**客**

**户**

ECS或云外主机（ACK或自建K8s节点） ECS或云外主机（Jenkins节点）

**端**

**V3.18.6(2512limit)之后版本**

YundunConsole YundunBaseService 横向基础能力 AegisPrivateCloudEegine Dipper 检测引擎计算引擎

**yundun-basic**

MiniRDS Aegisbiz AegisContainerNetwork SasContainerDefense SasContainerService OSS 核心能力 SLS AegisHealthCheck AegisVirusScan AegisImageAnalyzer AegisSuspicious MetaQ/Diamond

**服**

**务**

AegisVulnerability BanffAegisWeb AegisMatcher

**端**

检测/防御能力 Tair/SchedulerX

**中间件**

AegisMaster Aegiserver Aegisupdate 客户端管理

**yundun-**

**css(ageis)**

**Paas共享Node池**

AliYunDun AliYunDunUpdate sas-jenkins-plugin sas-image-scanner deamonset-

**客**

docker

**户**

ECS或云外主机（ACK或自建K8s节点） ECS或云外主机（Jenkins节点）

**端**

容器安全，复用安骑士检测能力，包括服务端、客户端两大模块。 服务端：负责将云内、云外的容器集群和镜像资产纳入到容器安全管理范围，并提供检测、防御等核心能力。 客户端：负责实时上报容器集群运行状态，以及容器运行节点运行状态，提供运行检测、网络阻断防护能力。

**服务端**

服务端主要分成以下几个模块： 横向基础能力：云盾通用能力，提供控制台和OpenAPI。 核心能力：包括资产管理、安全告警、文件采集等。 检测防御：包括漏洞、基线、文件、网络、进程的检测防御能力。 检测引擎：包括商业病毒检测引擎、阿里自研病毒检测引擎、大数据计算引擎。 客户端管理：负责管理客户端连接、容器集群状态更新、配置规则下发等。 服务端每个应用的具体职责：

| 模块 | 职责 |
|---|---|
| YundunConsole | 控制台，为安全管理员提供了统一的管理界面。 |

| YundunBaseService | API网关，将主机安全能力开放给第三方开发者。 |
|---|---|
| AegisSuspicious | 入侵告警事件、应用白名单。 |
| Aegisbiz | 管理云内、云外的容器集群和镜像的资产。 |
| SasFileserver | 文件采集。 |
| AegisContainerNetwork（AegisMet aData） | 网络可视化、容器防火墙。 |
| SasContainerService（NewSas） | 镜像插件扫描服务。 |
| SasContainerDefence（NewSas） | 容器主动防御服务。 |
| AegisHealthCheck | 主机基线检查。 |
| AegisVirusScan | 文件检测。 |
| AegisDetect | 旧版文件检测，当前仅保留文件白名单管理，其他流程全部迁移到 AegisVirusScan。 |
| AegisDefence | 防篡改。 |
| AegisVulnerability | 漏洞检测。 |
| AegisPrivateCloudEngine | GLE引擎是阿里自研病毒检测引擎。 |
| AegisMaster | 客户端配置、插件管理。 |
| Aegiserver | 客户端连接管理、配置下发、消息转发等。 |
| Aegisupdate | 客户单升级、规则/脚本/补丁等文件拉取。 |
| YaraSlave | Yara二进制检测引擎，商业病毒检测引擎。 |
| AegisCloudavira | 小红伞二进制引擎，商业病毒检测引擎。 |
| AegisCloudavbd | BD二进制检测引擎，商业病毒检测引擎。 |

| AegisImageAnalyzer | 镜像扫描。 |
|---|---|
| Dipper | 大数据计算引擎，入侵检测。 |

**客户端**

客户端包括以下模块。

| 名称 | 说明 |
|---|---|
| SasJenkinsPlugin | 镜像扫描Jenkins插件，负责拉起SasImageScanner容器。 |
| SasImageScanner | 负责运行镜像扫描功能的容器进程。 |
| AliYunDun | 核心进程，用于与云安全中心服务器建立连接。 |
| AliYunDunUpdate | 核心进程，用于定期检测云安全中心Agent是否需要升级。 |
| AliNet | 容器防护墙进程。 |

**说明**

客户端支持的操作系统 AliNet支持操作系统

#### 核心模块

##### 资产管理

通过容器安全资产中心，可以全盘展示纳入管理的容器集群、镜像等资产的安全防护状态。

**支持的资产类型**

云内资产：ACK（容器服务kubernetes）、ACR（容器镜像服务） 云外资产：自建kubernetes，quay镜像仓库，harbor镜像仓库，Jenkins构建镜像

**核心流程**

**资产同步**

通过openapi获取ACK、ACR数据。 自建k8s接入： V3.18.6-2512-limit版本及之前版本，通过方向访问获取自建k8s、自建镜像仓数据。 V3.18.6-2512-limit之后版本，通过镜像托管集群方式，将自建集群master节点执行yaml，通过客户端上报的方式获取集群信息。 容器集群资产结合客户端上报的容器变更消息，实时更新容器状态。

**V3.18.6-2512-limit版本及之前版本核心流程**

| 1. 通过webhook通知镜 | 像资产变更 |
|---|---|

云外资产同步
1. 通过反向访问同步资产
云内资产同步自建K8S api 自建镜像仓资产变更 api

**Aegisbiz**

3. 广播容器资产变更信息
1. 调用OpenAPI同步ACK

**服**

2. 转发容器变更信息

**务**

**端**

监听容器变更 ACK管控

**Aegiserver**

消息并转发 ACK管控其他应用
1. 客户端上报容器变更信息
AliYunDun AliYunDun

**客**

**户**

**端**

ACR节点自建K8S 集群节点接口访问 metaq通知

**V3.18.6-2512-limit之后版本核心流程**

| 1. 通过webhook通知镜 | 像资产变更 |
|---|---|

云外资产同步

| 1. | 配置镜像托管集群接入 |
|---|---|

云内资产同步镜像托管集群接入信息资产变更

**Aegisbiz**

| 1. 调用OpenAPI同步ACK | 资产 |
|---|---|

**服**

3. 广播容器资产变更信息
2. 转发容器变更信息

**务**

**端**

监听容器变更 ACK管控

**Aegiserver**

消息并转发 ACK管控其他应用
2. 在master节点执
1. 客户端上报容器变更信息
AliYunDun AliYunDun

**客**

**户**

**端**

ACR节点自建K8S 集群节点接口访问 metaq通知

**云外资产接入流程**

通过反向访问，容器安全服务端可以从管控区访问用户VPC网络请求镜像仓库api、k8s apiServer。 用户IDC场景通过并网方式，也可能将云外资产纳入容器安全管理。 镜像仓库api 镜像仓库api K8S apiServer 并网 ECS ECS ECS 用户VPC 用户VPC

|  | 反向访问 |
|---|---|
|  | 通过反向访问下载镜像 |
| 获取manifest 下载layer AegisImage |  |

通过反向访问获取K8S集群和镜像资产信息管控区

**容器网络拓扑核心流程**

容器的网络日志会被打标成in和out流量，结合网络链路日志，经过dipper处理，容器间东西流量、公网和容器间的南北流量会被保留，并在拓扑图中呈现。 东西向流量：in和out日志时间间隔在特定范围，且两份日志的五元组（源ip、源端口、目标ip、目标端口）完全匹配。 南北向流量：in和out日志时间间隔在特定范围，且源ip或者目标ip有其一可追溯到公网ip 匹配时间间隔范围：精准匹配是60秒，service mode是10秒。 消费匹配后的网络日志获取容器资产信息

**服**

拼装拓扑图

**务**

**端**

AegisContainerNetwork Aegisbiz sls 匹配后的网络日志配对网络日志

| 匹配后 | 的网络日志 |
|---|---|

Dipper 上报in和out网络日志配对网络日志配对网络日志

**客**

网络通信

**户**

**端**

云外主机 ECS

##### 容器防火墙

容器防火墙是容器安全为容器环境提供的防火墙服务，是容器安全运行时防护的核心功能。结合容器网络可视化，配置合理的隔离规则，当黑客利用漏洞或恶意镜像入侵容器集群时，容器防火墙会对异常行为进行告警或拦截，可以将风险控制在小范围内，避免整个容器环境被入侵。

**网络对象说明**

相较于主机，容器、pod的生存周期是短暂的且会在不同节点间漂移，无法依赖固定的ip、port来配置规则，因此防火墙的隔离规则需要定义额外的网络对象。 用户的隔离规则是要配置在IP,DNS或者容器的pod，namespace，镜像，标签。IP、DNS，容器实例启动时需要实时的匹配对应的镜像、标签间的隔离规则。

| 对象类型 | 属性名 | 说明 | 备注 |
|---|---|---|---|
| 容器 | 命名空间 | 集群所内定义的命名空间 | 标签：kubernetes.io/metadata.name: <命名空间> |
|  | 应用名称 | 各个应用内定义的标签 （app） | 本质为自定义标签app: <应用名称>，ack默认会打上app:标。，自建k8s需要自行定义标签，否则在定义网络对象时会选择不到对应的应用 |
|  | 镜像 | 镜像名 |  |
| 4 | > 文档版本：2026072 |  |  |

|  | 标签 | 自定义标签 |  |
|---|---|---|---|
| IP | IP | 多个ip或者CIDR网段请用英文逗号隔开，最多支持50个IP或者网段 |  |
| DNS域名 | DNS域名 | 配置的域名通过DNS解析为IP（最多500个）， 并对这些IP实施访问控制。 |  |

**核心流程**

AliYunDun AliYunDun 容器启动容器启动事件和容事件和容器元数据器元数据通知通知业务业务 Container A Container B 内核过滤下发源容下发容器下发目的下发容器发起器实例信拦截规则容器实例拦截规则 tcp、 后最终息 syn、外信息 syn报文联请求 AliSecNetFilter AliSecNetFilter 携带有源携带有源容器信息容器信息的syn报的文 payload Network
1. 配置防火墙规则：容器防火墙下发配置和拦截功能完全依赖alinet插件，开启容器防火墙功能前会对
alinet插件状态进行校验，如未安装，或者alinet插件心跳异常将无法开启容器防火墙功能。
2. 下发防火墙规则：aliNet插件会记录当前节点容器状态和元数据，并接受记录服务端下发的防火墙规则。
3. 网络流量放行、告警、拦截：aliNet中子插件aliSecNetFilter会根据记录的容器元数据和防火墙规则，对
命中的规则的流量进行放行、告警、拦截。

##### 镜像扫描

镜像安全扫描功能支持对镜像中存在的高中危系统漏洞、应用漏洞、恶意样本、配置风险进行检测。

**支持扫描镜像类型**

云内镜像类型：defaultACR，企业版ACR 云外镜像类型：quay，harbor，jenkins构建的镜像

**支持扫描风险内容**

**漏洞：**系统漏洞（cve），应用漏洞（sca）

**基线：**

身份鉴别确保不存在重复的用户名或UID 确保不存在相同密码Hash的账户确保系统不存在空密码账户确保使用强密码哈希算法确保root是唯一UID为0的帐户确保不存在重复用户组或GID 未授权访问 CouchDB未授权访问配置风险 ES未授权访问配置风险 Postgresql未授权访问配置风险 Jenkins未授权访问配置风险 Hadoop未授权访问配置风险弱口令 tomcat弱口令配置 redis弱口令配置 rsync弱口令配置 svn弱口令配置服务配置确保未安装openssh服务
**恶意样本：**webshell、二进制文件（木马、勒索病毒、挖矿病毒、后门程序等）

**扫描流程**

**周期任务镜像扫描**

通过镜像扫描设置，可以在指定周期内对指定的镜像仓库镜像扫描。

| 生成周期任务 1. 下发扫描任务更新扫描进度更新镜像安全信息 Aegisbiz 获取manifest 2. 查询镜各阶段上报镜像扫描进度下载镜像layer 3. 下载镜像layer 漏洞规则 6. 查询镜像安全信息 4. 并发执行groovy解析脚本上报漏洞信息 5. 软件包列获表取软件包列表进行基线扫描获取文件列表 groovy解析脚本执行 AegisVulnerability AegisImageAnalyzer 5. 触发文件检测记录基线检查结果 5. 上报基线检查结果 AegisHealthCheck 判断文件是否就绪记录告警信息推送引擎镜像cve、sca漏洞 AegisSuspicious AaegisVirusScan | 像manifest 镜像仓库 5. 文件上传至oss OSS 检测引擎 |
|---|---|

|  | 2. 查询镜 | 2. 查询镜 | 像manifes |
|---|---|---|---|
| . 下载 | 镜像layer |  |  |

|  | 各阶段上报镜像扫描进 |  |  | 度 |  |  |
|---|---|---|---|---|---|---|
| 漏洞规则询镜像安全信息上报漏洞信息 AegisVulnerability |  |  |  |  |  |  |
|  |  |  |  |  |  | 列获表取软件包列表 |
|  |  |  | 5. | 软件 | 包 | 列获表 |

|  |  | 漏洞规则全信息 |
|---|---|---|
| 6. 查 | 询镜像安 | 全信息 |

| 镜像cve、sca漏 | 洞 |
|---|---|

**webhook镜像扫描**

acr镜像、自建镜像仓可以通过webhook的方式上报镜像变更，同时会创建单次周期的镜像扫描任务，并立即执行任务进行镜像扫描。

**Jenkins插件镜像扫描**

OpenApi请求 Http请求 SasImagerPlugin
1. 下载SasImageScanner镜像
JenKins

| 2. 加载SasImageScanner | 镜像 |
|---|---|

3. 启动镜像扫描容器
保存镜像到本地解压镜像tar 更新扫描任务状态
4. 镜像预处理
5. 下载groovy脚本

| 获取g | roovy检测脚本 |
|---|---|

文件上传至oss 获取软件包列表进行基线扫描获取文件列表
6. 并发执行groovy解析脚本
客户端临时上传oss url SasImageScanner容器服务端查询groovy脚本获取临时上传url 更新扫描进度 Aegisbiz OSS
7. 上报脚本筛选结果
分发镜像筛选结果 SasContainerService
8. 上报文件筛选列表
8. 上报软件包筛选列表
8. 上报基线检查结果
生命周期任务漏洞规则判断文件是否就绪记录基线检查结果更新扫描进度上报漏洞信息推送引擎 AegisHealthCheck 更新镜像安全信息 Aegisbiz AegisVulnerability AegisVirusScan
9. 查询镜像安全信息
引擎检测结果记录告警信息镜像cve、sca漏洞 AegisSuspicious 检测引擎

##### 集群防御

**容器文件防御**

该功能属于容器防护的基础服务，要求集群已接入容器安全、操作系统及内核版本在支持范围内。用户可通过创建文件防御规则，指定需防护的路径、包含/排除的文件类型、执行动作（告警或拦截）以及白名单进程等配置，实现精细化的文件级防护。容器文件防御流程图如下： 容器防篡改架构规则管理目录管理规则应用管理进程白名单管理告警管理 POP 弹内 VPC sas-container-defense aegis-suspicious 规则下发/插件安装告警上报弹内 aegis-master aegis-server 规则下发/插件安装告警上报 aegis-client

**容器主动防御**

该功能从镜像自身安全、运行时安全、运行环境安全多维度主动检测容器启动或运行时存在的安全风险。通过配置相应规则，您可以拦截风险镜像运行、停止不可信进程和阻断容器逃逸行为，提升整体容器运行环境的安全水位。本文介绍如何配置风险镜像阻断、非镜像程序防御和容器防逃逸规则。

| 规则类型 | 规则说明 | 备注 |
|---|---|---|
| 风险镜像阻断 | 创建风险镜像阻断规则后，在指定集群内使用镜像创建资源时，容器安全会对镜像进行安全校验，对命中风险镜像阻断规则的镜像执行拦截、告警或放行动作，确保集群内启动的镜像符合您的安全要求。 | 仅支持容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）的部分集群类型。 |

| 非镜像程序防御 | 创建非镜像程序防御规则后，容器安全可检测并拦截镜像外的程序启动，主动防御恶意软件的入侵， 帮助您防御已知或未知的攻击模式。 | 容器中安骑士客户端进程AliYunDun ≥ aegis 12 13，AliHips ≥ 00 43。 _ _ _ 对于白名单规则中容器镜像，还需确保对应容器镜像名称的长度不超过287个字符。 容器中运行程序的完整路径长度不超过 1023个字符。 容器集群的命名空间长度不超过287个字符。 |
|---|---|---|
| 容器防逃逸 | 容器防逃逸功能可以从进程、文件、系统调用等多种维度检测高风险行为，在容器与宿主机之间建立防护屏障，有效阻断逃逸行为保障容器运行时安全。该功能可拦截攻击者利用容器漏洞逃逸到宿主服务器上的攻击，有助于提升服务器系统的安全性。 | 集群所在服务器已接入到容器安全。 |

**风险镜像阻断流程图**

|  |  | yundun-css- main 则下发规则镜像扫描结果查询规则有风险匹配到规则 |
|---|---|---|
| 镜 | 匹配到规则像执行行为(拦截/告警/放行) |  |

ACK 创建pod SASMaliciouslm

| 规 | 则下发 |
|---|---|

age策略镜像的校验根据集群id获取规则策略管理组件 (gatewatkeeper) 告警/放行拦截是否创建pod 创建pod 产生告警结束 suspicious

**非镜像程序防御流程图**

**容器防逃逸流程图**

部署危险容器
6. 危险容器部署
客户端 aegis-suspicious Alihips
5. 规则推送

|  | aegis-server 上报 |
|---|---|
| 7. 告警记录 | 上报 |

Aliyundun
8. T_MSG_PLUGIN_EV

| 3. T MSG CLIE | NT)R | ULE PUSH |
|---|---|---|

1. T_MSG_PLUGIN_HEARTS
aegis-server 2.组装需要下发的规则

**容器签名**

容器签名可实现对容器镜像的可信签名，确保只允许部署您认可的容器镜像，防止未经签名授权的镜像启动，从根本上帮助您提升资产的安全性。 该功能基于非对称加密算法（需使用KMS创建密钥类型为 RSA_2048、用途为 SIGN/VERIFY 的密钥）， 通过在容器安全配置**证明者**和**安全策略**，将签名验证能力与ACK集群集成。当启用策略后，只有携带有效签名的镜像才能在指定命名空间中部署，未签名或验签失败的镜像将被拦截。流程图如下： 容器启动的签名验容器证在ack集群安全给集群的命名空间进行证明者加签证明者安全策略查询证明者 ack集群
1. 查询ack集群
2. 查看集群插件是否安装
容器加签注意事项：
1. 创建的ack集群需要安装组件kritis-validation-hook
2. 检查ack加签的密钥与云安全中心的证明者使用同一个密钥
查询kms密钥接口，用户生成证明者查询云安全中心的安全策略进行镜像加签
3. 检查下发的策略和下发到ack的namespace是否正确
kms acr 需要开启企业版的acr，只有企业菜单用户主密钥创建类型： 选择企业版acr的镜像创建容器版的acr具备镜像加签功能 RSA_2048 秘钥用途：SIGN/VERIFY的密钥

### 高可靠性

**服务端高可用**

**说明**

设计原则：无状态应用容器安全服务端全部是无状态应用，通过VIP+Dubbo实现负载均衡保证服务可用性。 服务端本身是无状态的，部署在至少两台物理机上，只要有一台物理机正常运行即可保证可用性。 数据存储在MiniRDS、SLS、OSS、Tair、Diamond、MetaQ等中间件或云服务上，存储高可用性由中间件或云服务保证。 对外提供HTTPS协议的OpenAPI，通过DNS+VIP实现负载均衡，以保证可用性。 服务内部调用依赖Dubbo框架，由Dubbo的软负载保证可用性。

| 三方应用用户安骑士客户端 VIP 云解析 DNS |  |
|---|---|
| Aegisbiz Aegisbiz SasContainerService SasContainerService Dubbo SasContainerNetwork SasContainerNetwork AegislmageAnalyzer AegislmageAnalyzer ...... ...... 物理机物理机 |  |
| MiniRDS OSS Tair MetaQ 云存储中间件底座资源 |  |

|  | VIP |  |
|---|---|---|

### 容灾备份

**同城容灾**

**说明**

设计原则：业务双活。 容器安全同城容灾架构遵循双活原则，数据由云存储或中间件自身保证容灾。

| 流量入口流量入口主备主备网 VIP VIP 网络络 SasContainerService Aegisbiz SasContainerService Aegisbiz 双活安安骑骑士 AegisimageAnalyzer ...... AegisimageAnalyzer ...... 士 MiniRDS MiniRDS 主备云 OSS OSS 云存存储储 OSS OSS Tair MetaQ Tair MetaQ 双活中中间间件 Diamond Dubbo Diamond Dubbo 件主机房备机房 |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| 网 VIP 络 SasContainerService Aegisbiz 安骑士 AegisimageAnalyzer ...... MiniRDS 云 OSS 存储 OSS Tair MetaQ 中间件 Diamond Dubbo 主机房 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 主备 |  |  |  |
|  | 网 VIP 络 |  |  |  |  | 主备 | VIP 网络 |  |  |
|  | SasContainerService Aegisbiz 安骑士 AegisimageAnalyzer ...... |  |  |  |  | 双活 | SasContainerService Aegisbiz 安骑 AegisimageAnalyzer ...... 士 |  |  |
|  |  |  |  |  |  | 主备 | MiniRDS OSS 云存储 OSS |  |  |
|  | Tair MetaQ 中间件 Diamond Dubbo |  |  |  |  | 双活 | Tair MetaQ 中间 Diamond Dubbo 件 |  |  |

|  | VIP |  |
|---|---|---|

|  | VIP |  |
|---|---|---|

各组件同城容灾实现方案介绍：

| 组件 | 方案 |
|---|---|
| 容器安全 | 双活部署，依赖中间件及云存储保证数据一致。 |

| DNS | 通过Anycast VIP实现主备机房流量隔离。 |
|---|---|
| VIP | 通过BGP路由实现主备切换。 |
| MiniRDS | 主从库binlog复制。 |
| SLS | 基于OSS备份实现数据同步。 |
| OSS | 主备机房数据同步。 |
| 中间件 | 双活部署，依赖MiniRDS保证数据一致。 |

**异地灾备**

**说明**

设计原则：Region间相互独立。 容器安全多Region架构遵循独立原则，单元Region对中心Region无任何依赖，数据及服务保证完全隔离。

### 监控告警

**系统监控指标**

容器安全系统监控均已接入TianjiMon。

**重要**

注意：3.17.1之前版本还未开启告警。 各应用具体监控指标如下：

**aegisbiz应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisbiz cpu container host _ _ _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisbiz cpu container serv _ _ _ errole | CPU使用率（服务角色） |  |  |  |
| aegisbiz cpu container clust _ _ _ er | CPU使用率（集群） |  |  |  |

| aegisbiz memo container ho _ _ _ st | 内存（单机） | 内存使用率最大值和平均值 | util avg > _ 90 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
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
| aegisbiz ntp container clust _ _ _ er | NTP（集群） |  |  |  |
| aegisbiz process count cont _ _ _ ainer host _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisbiz process count cont _ _ _ ainer cluster _ | 进程数（服务角色） |  |  |  |
| aegisbiz process count cont _ _ _ ainer host _ | 进程数（集群） |  |  |  |

| aegisbiz nginx container ho _ _ _ st | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
|---|---|---|---|---|
| aegisbiz nginx container ser _ _ _ verrole | nginx QPS（服务角色） |  |  |  |
| aegisbiz nginx container clu _ _ _ ster | nginx QPS（集群） |  |  |  |
| aegisbiz health container ho _ _ _ st | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisbiz health container se _ _ _ rverrole | 健康检查（服务角色） |  |  |  |
| aegisbiz health container cl _ _ _ uster | 健康检查（集群） |  |  |  |

**aegis-metadata应用**

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
| aegismetadata nginx contai _ _ ner cluster _ | nginx QPS（集群） |  |  |  |

| aegismetadata health contai _ _ ner host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegismetadata health contai _ _ ner serverrole _ | 健康检查（服务角色） |  |  |  |
| aegismetadata health contai _ _ ner cluster _ | 健康检查（集群） |  |  |  |

**aegisContainerNetWork应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 |
|---|---|---|---|
| tjmon aegismetadata memo conta _ _ _ iner host _ | 内存（单机） | CPU使用率 | util avg > _ 90 |
| tjmon aegismetadata load contain _ _ _ er host _ | 负载（单机） | CPU 负载最大值和平均值 （load1，load5，load 15） | load1 avg > _ 2 |
| tjmon aegismetadata process cou _ _ _ nt container host _ _ | 进程数（单机） | 进程数的最大值 | process nu _ mber max> _ 100 |
| tjmon aegismetadata health conta _ _ _ iner host _ | 健康检查（单机） | 应用使用启动是否正常 | health>0 |
| tjmon aegismetadata exception al _ _ _ arm | 异常告警（单机） | 错误告警上报 | level=="ER ROR" |
| tjmon aegiscontainer oom host _ _ _ | 内存溢出告警（单机） | 内存溢出告警 | oom status _ _ sum>0 |

**aegis-image-analyzer应用**

| 监控指标（TianjiMon指标名称） | 监控名称 | 监控描述 | 告警阈值 | 告警描述 |
|---|---|---|---|---|
| aegisimageanalyzer cpu con _ _ tainer host _ | CPU使用率（单机） | CPU使用率 | util avg > _ 95 | 连续次数： 3次沉默时长： 300s |
| aegisimageanalyzer cpu con _ _ tainer serverrole _ | CPU使用率（服务角色） |  |  |  |
| 0 |  |  | > 文档版 | 本：2026072 |

|  |  |  | 容器安全运维 | 指南·运维文档 |
|---|---|---|---|---|
|  |  |  |  | 探测间隔： 60s |
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
| aegisimageanalyzer ntp con _ _ tainer serverrole _ | NTP（服务角色） |  |  |  |
| aegisimageanalyzer ntp con _ _ tainer cluster _ | NTP（集群） |  |  |  |

| aegisimageanalyzer process _ count container host _ _ _ | 进程数（单机） | 进程数的最大值和平均值 | process n _ umber m _ ax > 100 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
|---|---|---|---|---|
| aegisimageanalyzer process _ count container cluster _ _ _ | 进程数（服务角色） |  |  |  |
| aegisimageanalyzer process _ count container host _ _ _ | 进程数（集群） |  |  |  |
| aegisimageanalyzer nginx c _ _ ontainer host _ | nginx QPS（单机） | nginx请求的QPS | 暂无 | 暂无 |
| aegisimageanalyzer nginx c _ _ ontainer serverrole _ | nginx QPS（服务角色） |  |  |  |
| aegisimageanalyzer nginx c _ _ ontainer cluster _ | nginx QPS（集群） |  |  |  |
| aegisimageanalyzer health c _ _ ontainer host _ | 健康检查（单机） | 应用使用启动是否正常 | health > 0 | 连续次数： 3次沉默时长： 300s 探测间隔： 60s |
| aegisimageanalyzer health c _ _ ontainer serverrole _ | 健康检查（服务角色） |  |  |  |
| aegisimageanalyzer health c _ _ ontainer cluster _ | 健康检查（集群） |  |  |  |

**说明**

复用安骑士应用的系统监控，详见《安骑士运维指南》。

**业务监控指标**

容器安全系统监控基于TianjiMon实现，监控指标如下：

| 模块 | 名称 | 描述 |
|---|---|---|
| 容器资产 | 节点数量 | 容器集群节点各维度数量统计 |
|  | 应用（app）数量 | 容器集群应用各维度数量统计 |
|  | 容器组（pod）数量 | 容器集群容器组各维度数量统计 |
| 2 | > 文档版本：2026072 |  |

|  | 容器数量 | 容器集群容器各维度数量统计 |
|---|---|---|
|  | 镜像数量 | 镜像各维度数量统计 |
| 镜像扫描 | 镜像扫描任务数 | 创建的镜像扫描任务数量 |
|  | 镜像扫描层数 | 被扫描的镜像层数量 |
|  | 镜像扫描结果数 | 镜像扫描结果的数量监控 |
|  | 镜像预分析耗时 | 镜像扫描预分析各维度耗时 |
|  | 镜像分析耗时 | 镜像扫描分析各维度耗时 |
|  | 镜像分析（manifests）耗时 | 镜像扫描分析（manifests）各维度耗时 |
| CICD | Jenkins规则拉取次数 | Jenkins扫描镜像时拉取groovy规则次数 |
|  | Jenkins规则拉取耗时 | Jenkins扫描镜像时拉取groovy规则耗时 |
|  | Jenkins扫描结果上报次数 | Jenkins扫描镜像后上报结果次数 |
|  | Jenkins扫描结果上报耗时 | Jenkins扫描镜像后上报结果耗时 |
| 容器防火墙 | 容器网络日志消费数 | 容器网络可视化dipper日志消费的消息数 |
|  | 容器网络日志处理耗时 | 容器网络可视化dipper日志消费的耗时 |
|  | 容器防火墙拦截数 | 容器防火墙告警、拦截数量 |
| 容器运行时防护 | 容器Linux漏洞数量 | 容器Linux漏洞数量 |
|  | 容器应用漏洞数量 | 容器应用漏洞数量 |
|  | 容器告警事件数量 | 容器告警事件数量 |

### 容量规划

容器安全基于可用区内NC的CPU Core的数量计算出规格。每增加12000容器core，BasicThinCluster需增加2台物理机（NC和ECS的比例按照1:6，500台NC对应3000台ECS，每个ecs平均规格为4core）。 安骑士最大规格只能支持到192000core，如超过上限需联系研发介入。

**资源规格定义**

| 安骑士规格 | BasicThinCluster | SasCluster | 计算公式（整朵云的机器预期cpu核数量） |
|---|---|---|---|
| small | 2 | 2 | 集群容器core number总和 < 12000 |
| standard | 2~4 | 2~4 | 集群容器core number总和 < 24000 |
| large | 4~8 | 4~8 | 集群容器core number总和 < 48000 |
| xlarge | 8~16 | 8~16 | 集群容器core number总和 < 96000 |
| 2xlarge | 16~32 | 16~32 | 集群容器core number总和 < 192000 |

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
|---|---|---|---|---|---|
| baseline | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |
| newsas | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
| aegismat cher | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| aegisdefe nce | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| magpiebr idgedb | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| yunduna pi | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| yundunlu ban | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| datasync | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |

**Oss/Sls-inner资源容量规划**

| 规格 | 集群容器core number总和 | OSS容量(GB) | sls-Inner盘古磁盘总用（GB） |
|---|---|---|---|
|  | 计算公式： | 2GB/单台机器 | 0.1GB/单台机器 |
| small | 12000 | 7000 | 350 |
| standar d | 24000 | 14000 | 700 |
| large | 48000 | 28000 | 1400 |
| xlarge | 96000 | 56000 | 2800 |

| 2xlarge | 192000 | 112000 | 5600 |
|---|---|---|---|

**Tair资源容量规划**

| 规格 | 集群容器 core num ber总和 | tair 各namespace所需分配配额（MB） |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | nam espa ce | 92 | 381 | 499 | 663 | 106 | 690 | 478 | 692 | 总计 (MB) |
| small | 1200 0 | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| stan dard | 2400 0 | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| large | 4800 0 | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| xlarg e | 9600 0 | 1024 | 1024 | 1024 | 512 | 512 | 512 | 512 | 512 | 5632 |
| 2xlar ge | 1920 00 | 联系研发确认 |  |  |  |  |  |  |  |  |

**MetaQ资源容量规划**

| 规格 | 集群容器 core numbe r总和 | metaq容量规划 (单位:万条) |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  | 进程消息 | 网络消息 | 文件消息 | 进程写文件消息 | 插件心跳消息 | 其他 | 总计 (单位:万条) |
|  | 计算公式： （消息数/小时/ 机器） | 240 | 20 | 5 | 15 | 60 | 140 | 0.058 |
| small | 12000 | 84 | 7 | 1.75 | 5.25 | 21 | 49 | 203 |

| standa rd | 24000 | 168 | 14 | 3.5 | 10.5 | 42 | 98 | 406 |
|---|---|---|---|---|---|---|---|---|
| large | 48000 | 336 | 28 | 7 | 21 | 84 | 196 | 812 |
| xlarge | 96000 | 672 | 56 | 14 | 42 | 168 | 392 | 1624 |
| 2xlarg e | 192000 | 1344 | 112 | 28 | 84 | 336 | 784 | 3248 |

### XC支持

**企业版与自主可控能力差异**

企业版与自主可控能力差异主要是平台差异导致： x86企业版与x86海光能力100%一致。 arm飞腾、arm鲲鹏与企业版能力差异在30%以内，未来有计划对齐。 sw申威与x86企业版能力差异50%以内，未来暂无计划对齐。

**容器安全能力差异**

| 功能 | x86 | ar m | sw | 描述 |
|---|---|---|---|---|
| 总览 | 100 % | 100 % | 100 % | 展示需要重点关注的资产、漏洞、异常、配置缺陷、事件等信息总览。 |
| 容器资产 | 100 % | 100 % | 100 % | 提供服务器安全状态相关信息。例如，服务器的防护状态、分组、专有网络 VPC等统计信息，以及统计区分所有服务器、存在风险的服务器、未受保护的服务器、未启动的服务器和新增服务器的资产数量。 单击目标服务器名称可查看详细信息，包括漏洞信息、安全告警处理、基线检查、资产指纹调查等。 |
| 镜像扫描 &CICD | 100 % | 90 % | 80 % | 漏洞检测：支持检测包括Linux、应用漏洞，提供具体漏洞详情，提供一键扫描功能。 基线检测：自动检测服务器上的系统、账号、数据库、弱密码、合规性配置中存在的风险点，并提供加固建议。 恶意样本检测：提供病毒查杀和网站后门查杀功能，检测出主流木马病毒、 勒索软件、挖矿病毒、DDoS木马后自动隔离查杀。 重要能力差异： 部分自主可控操作系统不在支持范围，需通过规则包适配。 arm不支持AV/BD检测引擎，仅支持GLE。sw均不支持。 |

| 容器防火墙 | 100 % | 0% | 0% | 容器防火墙是容器安全为容器环境提供的防火墙服务。当黑客利用漏洞或恶意镜像入侵容器集群时，容器防火墙会对异常行为进行告警或拦截。 重要能力差异：arm、sw均不支持AliNet，无法对异常行为进行告警或拦截。 |
|---|---|---|---|---|
| 容器运行时防护 | 100 % | 80 % | 50 % | 集中展示受影响集群节点的告警信息，包括存在告警服务器的数量、待处理告警总数、需要紧急处理的告警等，其中告警类型覆盖进程异常行为、网站后门、异常登录、恶意进程（云查杀）、敏感文件篡改、异常网络连接、持久化后门、web应用威胁检测等多种入侵告警类型。 重要能力差异：arm不支持AV/BD检测引擎，仅支持GLE。sw均不支持。 |
| 日志检索 | 100 % | 100 % | 100 % | 提供登录流水、暴力破解、进程快照、网络连接、端口监听快照、账号快照、进程启动的日志查询。 |

**当前各模块适配情况**

| 模块 | x86（企业版、海光） | arm（飞腾、鲲鹏） | sw（申威） |
|---|---|---|---|
| 客户端 | 100% | 50%（不支持AliNet） | 50%（不支持AliNet） |
| 服务端 | 100% | 100% | 100% |
| 前端 | 100% | 100% | 100% |
| 计算引擎 | 100% | 100% | 100% |
| 检测引擎 | 100% | 50%（不支持AV、BD引擎） | 0%（所有检测引擎都不支持） |

**一云多芯支持情况**

一云多芯的主要包括异构同城容灾（主备机房的机房级硬件异构）以及异构多Region（中心/单元机房级硬件异构）2大横向场景。 容器安全对一云多芯的支持情况如下：

| 场景 | 支持情况 |
|---|---|

| 异构同城容灾（x86+arm） 主备机房的机房级硬件异构 | 支持 （部分能力在arm机房不生效，如主动防御、自保护） |
|---|---|
| 异构多Region（x86+arm） 中心/单元机房级硬件异构 | 支持 |

### 热升级

容器安全默认支持热升级，无需额外运维操作。

### AliNet (06_21) Linux Driver OS

**/ Kernel List**

**支持的系统版本**

| linux大版本 | linux小版本 |
|---|---|
| CentOS6 | 6.5, 6.6, 6.7, 6.8, 6.9, 6.10 |
| CentOS7 | 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9 |
| CentOS8 | 8 |
| Ubuntu14 | 14.04 |
| Ubuntu16 | 16.04 |
| Ubuntu18 | 18.04 |
| Ubuntu20 | 20.04 |
| AliYunLinux | 2.1903, 17.01, 3 |
| ANOLIS | 7.9,8.4 |

**kernel 版本**

| Linux系统 | kernel版本 | 备注 |
|---|---|---|

| CentOS | 2.6.32 3.10.0 4.18.0 4.19.104 5.4.8 5.4.42 | 3.10.0-123开头的特殊匹配 4.18.0开头的，完全匹配 （ 4.18.0-147.5.1.el8 1.x86 64 _ _ 4.18.0-193.14.2.el8 2.x86 64 _ _ 4.18.0-193.28.1.el8 2.x86 64 _ _ 4.18.0-240.15.1.el8 3.x86 64 _ _ 4.18.0-240.22.1.el8 3.x86 64 _ _ 4.18.0-305.3.1.el8.x86 64 _ 4.18.0-305.10.2.el8 4.x86 64 _ _ 4.18.0-305.19.1.el8 4.x86 64 _ _ 4.18.0-348.2.1.el8 5.x86 64 _ _ 4.18.0-348.7.1.el8 5.x86 64 _ _ 4.18.0-358.el8.x86 64 _ 4.18.0-365.el8.x86 64 _ 4.19.104-300.el7.x86 64 _ 5.4.8-1.el7.elrepo.x86 64 _ 5.4.42-200.el7.x86 64） _ |
|---|---|---|
|  | 3.13.0-32-generic 3.13.0-86-generic 4.4.0-62-generic 4.4.0-63-generic 4.4.0-93-generic 4.4.0-96-generic 4.4.0-104-generic 4.4.0-117-generic 4.4.0-124-generic 4.4.0-142-generic 4.4.0-146-generic 4.4.0-151-generic 4.4.0-170-generic 4.4.0-174-generic 4.4.0-179-generic 4.4.0-184-generic 4.4.0-185-generic 4.4.0-210-generic 4.15.0-13-generic 4.15.0-23-generic 4.15.0-42-generic 4.15.0-45-generic | 需要kernel整个版本字符串匹配， 如"3.13.0-32-generic" |

| Ubuntu | 4.15.0-52-generic 4.15.0-54-generic 4.15.0-72-generic 4.15.0-96-generic 4.15.0-106-generic 4.15.0-109-generic 4.15.0-111-generic 4.15.0-118-generic 4.15.0-124-generic 4.15.0-128-generic 4.15.0-144-generic 4.15.0-147-generic 4.15.0-158-generic |  |
|---|---|---|
|  | 4.15.0-166-generic 4.15.0-169-generic 4.15.0-170-generic 4.15.0-1047-gcp 5.3.0-40-generic 5.4.0-31-generic 5.4.0-42-generic 5.4.0-47-generic 5.4.0-58-generic 5.4.0-73-generic 5.4.0-77-generic 5.4.0-86-generic 5.4.0-91-generic 5.4.0-92-generic 5.4.0-94-generic 5.4.0-100-generic 5.4.0-102-generic 5.4.0-106-generic |  |

| AliYunLinux | 3.10.0-1160.al7.1.x86 64 _ 4.4.95-1.al7.x86 64 _ 4.4.95-3.al7.x86 64 _ 4.19.24-7.al7.x86 64 _ 4.19.24-7.14.al7.x86 64 _ 4.19.81-17.al7.x86 64 _ 4.19.81-17.2.al7.x86 64 _ 4.19.91-19.1.al7.x86 64 _ 4.19.91-21.2.al7.x86 64 _ 4.19.91-21.al7.x86 64 _ 4.19.91-22.2.al7.x86 64 _ 4.19.91-22.al7.x86 64 _ 4.19.91-23.al7.x86 64 _ 4.19.91-24.1.al7.x86 64 _ 4.19.91-25.1.al7.x86 64 _ 4.19.91-25.3.al7.x86 64 _ 4.19.91-25.6.al7.x86 64 _ 4.19.91-25.7.al7.x86 64 _ 5.10.23-5.al8.x86 64 _ 5.10.60-9.al8.x86 64 _ 5.10.84-10.2.al8.x86 64 _ 5.10.84-10.3.al8.x86 64 _ | 需要kernel整个版本字符串匹配 |
|---|---|---|
| Anolis | 3.10.0-1160.an7.x86 64 _ 3.10.0-1062.an7.x86 64 _ 3.10.0- 1160.59.1.0.1.an7.x86 64 _ 4.19.91-25.2.an7.x86 64 _ 4.19.91-25.7.an7.x86 64 _ 4.18.0-348.2.1.an8 4.x86 64 _ _ 4.18.0-348.12.2.an8.x86 64 _ |  |
