---
title: "智能体工厂 OpenTrek Agent Dev部署指南"
product_version: "V2.17.0"
doc_version: "20260902"
pdf_pages: 73
source_pdf: "17_Agent Dev部署指南_opentrek-agent-dev-aistack-deployment-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/ai_stack/v_2_17_0_20260828/opentrek/zh/opentrek-agent-dev-aistack-deployment-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 智能体工厂 OpenTrek Agent Dev部署指南

智能体工厂 OpenTrek

## Agent Dev部署指南

### 部署概述

**说明**

OpenTrek Agent Dev（原百炼专属版）部署前置依赖一个Kubernetes集群，请提前准备好 Kubernetes集群并将制品包全部上传至集群的一个Master节点上。 OpenTrek CoWorker 需单独购买，购买后方可部署；且在部署 CoWorker 前，须先完成 OpenTrek Agent Dev 的部署。本文关于 OpenTrek CoWorker 的内容仅适用于已购买该产品的用户，请根据实际需求阅读。

**交付产品内容**

| 产品名称 | 应用编码 |
|---|---|
| OpenTrek Agent Dev | OpenTrek-Standard |
| OpenTrek CoWorker | OpenTrek-CoWorker |

**Kubernetes命名空间**

部署过程会创建如下kubernetes 命名空间。

| Namespace | 用途 |
|---|---|
| sfm | OpenTrek Agent Dev管控区相关服务 |
| sfm-agent-studio | 智能体相关服务 |
| sfm-agent-xdb | 知识库相关服务 |
| sfm-agent-cluster | 数据加工任务Job |
| monitoring | 天眼监控相关服务 |
| opentrek-coworker | OpenTrek CoWorker相关服务 |

**对外端口开放**

| 功能 | 对外端口 |
|---|---|

智能体工厂 OpenTrek

| Uni-Operator控制台 | 默认端口30007 |
|---|---|
| OpenTrek Agent Dev控制台 | 默认端口30226 |
| OpenTrek Agent Dev租户区OpenAPI | 80 (ingress) |
| 监控大盘 | 80 (ingress) |

#### 文档说明

本文档旨在为 OpenTrek Agent Dev的部署提供标准化的操作指南，确保部署过程的规范性和可重复性。

**发布说明**

| 文档版本 | V3.4.0 |
|---|---|
| 发布日期 | 2026年8月17日 |
| 修订记录 | 1. 可观测方案支持OpenTrek Monitor。 2. 增加以下模块的部署参数。 OpenTrek Agent Dev： Knowledge Wave配置 DKE内置解析服务配置 Knowledge Claw配置可观测配置 CoWorker部署：可观测配置 3. 部署参数精简： OpenTrek Agent Dev：LOGIN INTERCEPTOR、 _ LOGIN PROCESSOR PREFIX、POP DOMAIN _ _ _ CoWorker部署：POP AK、POP SK。 _ _ 4. 增加获取资产包和DKE资产部署。 |

**适用对象**

本文档适用于 OpenTrek Agent Dev的运维工程师和交付工程师。

**内容概述**

本文档包含以下主要内容：

### 1. 部署概述

介绍本文档的发布日期、适用对象、部署方式和部署架构。

### 2. 部署依赖

智能体工厂 OpenTrek 介绍部署OpenTrek Agent Dev前所依赖的中间件、集群、组件等；支持VM/裸金属和企业版ECS两种场景，不同场景下所依赖底座/产品不同，请根据现场实际情况部署。

### 3. 部署前准备

### 4. 部署实施

i. 介绍Agent Dev的完整部署流程。 iii. 介绍CoWorker的完整部署流程。

### 5. 部署验证

i. 验证登录控制台。 ii. 验证管控状态。
6. 附录
提供部署过程中的补充操作指南。

### 7. 常见问题

提供部署过程中常见问题的排查

#### 部署架构

#### 部署架构

**部署阶段顺序表**

| 阶段 | 组件 | 依赖 | 说明 |
|---|---|---|---|
| Stage 1 | 创建AI Stack上的中间件实例。 | 无 | 完成中间件部署、实例创建和配置。 |

智能体工厂 OpenTrek

| Stage 2 | OpenTrek UniOperator | 无 | 部署OpenTrek UniOperator，并导入授权文件。 |
|---|---|---|---|
| Stage 3 | OpenTrek Monitor | Stage 2 | 部署OpenTrek Monitor。 |
| Stage 4 | OpenTrek UniManager | Stage 2 | 部署OpenTrek UniManager。 |
| Stage 5 | OpenTrek Agent Dev | Stage 1～3 | 部署OpenTrek Agent Dev。 |
| Stage 6 | 模型接入 | Stage 4 | 模型部署和接入。 |
| Stage 7 | OpenTrek Coworker | stage 5 | （可选）部署 Coworker。 |

**存储架构**

**NFS**

1. PVC当前是直接挂载到 NFS PV，StroageClass 为 `""` 。
2. PVC 列表
i. `auto-agent-sandbox` ：持久化存储，RWX，trekclaw 管控区服务挂载 ii. `auto-agent-sandbox-shared` ：持久化存储，RWX，trekclaw 沙箱挂载，一个 session 对应一个目录并挂载到一个沙箱，通过 subpath 方式挂载 pvc 用于安全隔离

**网络架构和安全策略**

智能体工厂 OpenTrek

| 编号 | 源端 | 目标端 | 访问内容 | 协议/默认端口 |
|---|---|---|---|---|
| ① | 用户浏览器 | 管控区服务 | 以独立登录的方式访问OpenTrek Agent Dev控制台 | HTTP/30266 |
| ② | 用户浏览器 | oneconsole | 以oneconsole统一登录方式访问 OpenTrek Agent Dev控制台，独立登录方式和统一登录方式只会存在一种 | HTTP/30266 |
| ③ | 用户浏览器 | 对象存储 | 对象存储前端直传 | HTTP/Minio or OSS |
| ④ | 租户区服务 | 外部模型服务 | 模型服务调用 | - |
| ⑤ | 外部模型服务 | 对象存储 | 图像识别和向量化等 | HTTP/Minio or OSS |

### 部署依赖

**安装机器环境要求**

| 检查项 | 要求 |
|---|---|
| 网络 | 请参见网络架构和安全策略。 |
| 端口 |  |
| 额外依赖 | 无。 |

**部署产品依赖**

部署OpenTrek Agent Dev前，您需要完成以下产品的部署： Uni-Operator，具体操作，请参见《Uni-Operator 部署指南》。 Uni-Manager Lite，具体操作，请参见《Uni-Manager Lite 部署指南》。 OpenTrek Monitor，具体操作，请参见《OpenTrek Monitor 部署指南》。

**说明**

CoWorker 需额外购买，购买后方可进行部署，部署 CoWorker 前需先部署 OpenTrek Agent Dev。

**需要客户放通的端口**

智能体工厂 OpenTrek

| 序号 | 源端 IP |  |  |  |  | 目的端 IP |  |  |  |  | 目的端口 （VM 版） |  |  |  | 目的端 IP 查询方式 |  |  |  | 目的端口查询方式 |  |  |  |  | 开通策略的原因 |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 运维/使用方终端网段 |  |  |  |  | K8s worker 节点 IP |  |  |  |  | 30011 |  |  |  | kubectl |  |  |  | NodePort， kubectl |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kubectl |  |  |  | 控制台 Web |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kube | ctl |  | get svc - |  |  |  |  |  | UI 与 API 统一入口 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 0011 |  |  | get nodes - |  |  |  | n |  |  |  |  | （ops- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o wide |  |  | 取 | opentrek- |  |  |  |  | manager |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | INTERNAL-IP |  |  |  | ops ops- |  |  |  |  | Spring Boot |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Boot |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | manager- |  |  |  |  | 内 70 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | service |  |  |  |  |  |  |  |  |  |  |
| 2 | 运维/使用方终端网段 |  |  |  |  | K8s worker 节点 IP |  |  |  |  |  |  |  |  | kubectl |  |  |  | NodePort， kubectl |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kubectl |  |  |  | 可观测数据 OTLP 接收入 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kube | ctl |  | get svc - |  |  |  |  |  | 口（ops- |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | get nodes - |  |  |  | n |  |  |  |  | monitor，容 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 30012 |  |  |  | o wide |  |  | 取 | opentrek- |  |  |  |  | 器内 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 7001），接 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | INTERNAL-IP |  |  |  | ops ops- |  |  |  |  | 收 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | monitor- |  |  |  |  | trace |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | service |  |  |  |  |  |  |  |  |  |  |
| 3 | 运维/使用方终端网段 |  |  |  |  | K8s worker 节点 IP |  |  |  |  |  |  |  |  |  |  |  |  | NodePort， kubectl |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kubectl |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | get svc - |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kubectl |  |  | n |  |  |  |  |  | 制品管理服务 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | get nodes - |  |  |  | open |  | trek- |  |  | （容器内 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 30013 |  |  |  | o wide |  |  | 取 | ops ops- |  |  |  |  | 7001），制 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 品包/技能包 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | INTERNAL-IP |  |  |  | middleware |  |  |  |  | 上传下载 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | - |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | artifact- |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | service |  |  |  |  |  |  |  |  |  |  |
| 4 | 运维/使用方终端网段 |  |  |  |  | K8s worker 节点 IP |  |  |  |  |  |  |  |  |  |  |  |  | NodePort， kubectl |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kubectl |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Prometheus |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 查询 UI 与 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | get svc - |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kubectl | ctl |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | n |  |  |  |  |  | API，同时接 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | n |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | get nodes - |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | open |  | trek- |  |  | 收 OTLP 数 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 3 | 0014 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o wide |  |  | 取 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ops |  |  |  |  | 据 （ /api/v1 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | /api/v1 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | INTERNAL-IP |  |  |  |  |  |  |  |  | （ |  | /api/ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | prometheus |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | etheus |  |  | /otlp |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ） |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | - |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | nodeport |  |  |  |  |  |  |  |  |  |  |
| 5 | K8s 所有节点 |  |  |  |  | K8s worker 节点 IP |  |  |  |  |  |  |  |  | kubectl |  |  |  |  |  |  |  |  | LoongColle ctor 日志采集端点，平台运行日志 gRPC 导出 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kubectl |  |  | NodePort， |  |  |  |  | L |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | get nodes - |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Loon |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 30155 | 0155 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o wide |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

智能体工厂 OpenTrek

### 部署前准备

#### 获取安装包

本章节介绍获取部署时使用的资产包。

#### 获取资产包

本章节介绍获取DKE使用的资产包。

#### 收集安装参数

**组件部署配置**

下表介绍组件部署配置时涉及的参数，包括参数项及含义，并给出了示例值，请按照说明填写参数。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| CLOUD TYPE MODE _ _ | 支持的参数： AiStack：适用于在 AI Stack 一体化平台环境中的部署场景，请选择此项。 Light：用于纯软版的轻量级部署场景，即On VM/裸金属部署和On 企业版ECS部署请选择此项。 PublicCloudVPC：适用于在公有云 VPC网络环境中的部署场景，请选择此项。计算巢直接拉起，不需要用户感知。 | 是 | Light |
| REPLICAS | 非高可用版则填写1。 高可用版则填写2。 说明为保障系统稳定性与业务连续性，建议您填写 2，启用高可用模式。 | 否 | 2 |
| DEPLOY AISTUDIO _ | 若当前 Kubernetes 集群中已部署 AI Studio，请设置为 true。 若尚未部署 AI Studio，请设置为 false。 | 是 | false |

智能体工厂 OpenTrek

| DEPLOY AGENT _ | 默认值为 true，表示将部署智能体网关。 若您的部署场景为 DKE 独立输出模式（即不依赖集成的智能体网关），DKE 独立输出模式不需要智能体网关， 请设置为 false。 | 是 | true |
|---|---|---|---|
| DEPLOY OPS _ | 是否部署运维组件，默认为 false。 | 是 | false |
| RES MODE _ | 资源创建模式，支持的参数： Auto（默认）：系统将自动创建所需资源，适用于大多数标准部署场景。 Manual：需用户预先手动创建并配置相关资源，适用于对资源管理有定制化要求的高级场景。如果需要使用 Manual方式，请联系技术支持。 | 是 | Auto |
| HIS BIZ RAG _ _ | 老知识中心能力是否透出。基于老的百炼专属版本 V2.1.* 做迁移升级到新版本的场景，需要基于迁移方案走定向升级策略,此时需要基于现场老版本情况，按需开启。 固定值。在全新部署场景中此参数无需填写或修改。 | 是 | false |
| HIS BIZ KC _ _ | 老插件中心能力是否透出。基于老的百炼专属版本 V2.1.* 做迁移升级到新版本的场景，需要基于迁移方案走定向升级策略,此时需要基于现场老版本情况，按需开启。 固定值。在全新部署场景中此参数无需填写或修改。 | 是 | false |
| HIS MODEL _ | 老天璇运行态路由转发能力是否透出。基于老的百炼专属版本V2.1.* 做迁移升级到新版本的场景，需要基于迁移方案走定向升级策略,此时需要基于现场老版本情况， 按需开启。 固定值。在全新部署场景中此参数无需填写或修改。 | 是 | false |

智能体工厂 OpenTrek

**访问入口信息**

下表介绍访问入口信息配置时涉及的参数，包括参数项及含义，并给出了示例值，请按照说明填写参数。

**说明**

1. 如果使用域名访问，默认访问OpenTrek Agent DEV管控的流量会经由ingress-controller的80 转
发至下面的服务中。如果使用ip+端口，则访问OpenTrek Agent DEV管控的流量不会经过 ingress-controller，而是直接经过NodePort。
2. on VM/裸金属安装K8s的时候一般要求提供 VIP 来负载均衡到ingress-controller的80端口上，故
DOMAIN填写域名时，需保证域名能解析到这个VIP上。
3. 如果DOMAIN 填写的是 IP，建议填写一个VIP, 且这个VIP能负载到3台k8s的master上。如果没有
VIP或做部署测试验证，IP可以填写master节点的一个IP。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| TENANT INGRES _ S PORT _ | Kubenetes集群的nginx-controller的端口请根据客户实际规划填写。 | 否 | 80 |

智能体工厂 OpenTrek

| DOMAIN | 若启用域名访问 （即 ENABLE WEB DOMAIN=true ），请在 _ _ 此填写实际分配的、可被客户端解析的访问域名。 若使用 IP 加端口方式访问 （即 ENABLE WEB DOMAIN=false ），请在 _ _ 此填写外部浏览器可直接连通的 IP 地址与端口组合。 说明默认端口为30226，如果有冲突可以自行填写，此处填写的端口部署后是NodePort。 请根据实际部署环境的网络策略和访问需求选择相应模式。 | 是 |  | 域名示例： example. com IP:Port示例： 1.2.3.4:30226 |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | example. |  |
|  |  |  |  | com |  |  |
| ENABLE WEB DO _ _ MAIN | 是否启用域名访问，参数含义如下： true：启用基于域名的访问方式，需配合配置有效的访问域名。 false：使用 IP 地址加端口（IP:Port）方式进行访问。 | 否 |  | false |  |  |
| FE ASSETS NOD _ _ EPORT | Open Trek Agent Dev 控制台端口。默认30226， 可自行指定未被占用的且在Kubernetes NodePort 范围内的端口。 | 是 |  | 30226 |  |  |
| HTTP SCHEMA _ | 控制台访问入口协议，可选参数： http：默认使用 HTTP 协议访问OpenTrek Agent Dev控制台。 如无特殊安全要求或未配置 TLS 证书，系统将通过 HTTP 提供前端服务。 https：启用HTTPS加密传输，选择此项前请确保已完成TLS/SSL证书的部署与配置，以保障通信安全。 | 是 |  | http |  |  |

**登录鉴权方式**

下表介绍登录鉴权方式配置时涉及的参数，包括参数项及含义，并给出了示例值，请按照说明填写参数。 智能体工厂 OpenTrek

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| LOGIN TYPE _ | 登录类型，参数填写请参考： 已接入Uni-Manager Lite请填写为 pop。 未接入Uni-Manager Lite请填写 inner。 | 否 | pop |

**镜像仓库信息**

下表介绍镜像仓库配置时涉及的参数，包括参数项及含义，并给出了示例值，请按照说明填写参数。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| ACR CREDENTIAL REQ _ _ UIRED | 是否需要 ACR 凭证。 设置为 true：表示部署过程中需从阿里云容器镜像服务（ACR）拉取私有镜像， 此时必须同时提供有效的 ACR 访问凭证： ACR USERNAME _ ACR PASSWORD _ 设置为 false：表示使用公开镜像或镜像已预加载至集群，无需 ACR 凭证，此时可忽略上述两个字段。 | 是 |  |
| ACR ENDPOINT _ | ACR的服务接入点。 UO：参数获取方式请参见：获取ACR部署参数。 非UO请根据规划填写。 | 是 | registry.k8s.local:5 000 |
| ACR USERNAME _ | ACR 镜像仓库的用户名。 参数获取方式请参见：获取ACR部署参数。 | 否 | admin |
| ACR PASSWORD _ | ACR 镜像仓库的访问凭证。 参数获取方式请参见：获取ACR部署参数。 | 否 | pwd**** |

请执行下述命令，获取ACR_ENDPOINT、ACR_USERNAME、ACR_PASSWORD。 智能体工厂 OpenTrek

```java
kubectl get secret ahm-registry-secret -n ahm-runtime -o jsonpath='{.data.\.dockerconfigjson}' | base64 -d | python3 -c " import sys,json,base64 d=json.load(sys.stdin) for repo,v in d['auths'].items():
    u,p=base64.b64decode(v['auth']).decode().split(':',1)
```

`print(f'`仓库: {repo}\n账户: {u}\n密码`: {p}')` "

**AI Studio计算集群镜像仓库信息**

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| AISTUDIO REGISTRY TY _ _ PE | 环境中部署 AIStudio 时，需要将 OpenTrek 数据加工运行时镜像导入到AI Studio 部署或使用的租户区镜像仓库。 用于支持 DKE 加工任务运行在 AIStudio 资源组中。 没有部署AI Studio 则全配置为空。 若部署了AI Studio 则从 AI Studio 应用参数中复制。去掉参数前缀 AISTUDIO 即为AI Studio中对应 _ 参数名称。 | 否 | CR |
| AISTUDIO REGISTRY E _ _ NDPOINT |  | 否 | 192.168.3.147:844 3 |
| AISTUDIO REGISTRY U _ _ SERNAME |  | 否 | admin |
| AISTUDIO REGISTRY PA _ _ SSWORD |  | 否 | password |
| AISTUDIO REGISTRY IN _ _ STANCE ID _ |  | 否 | cri-private |
| AISTUDIO REGISTRY N _ _ AMESPACE |  | 否 | acr-aipaas |
| AISTUDIO REGISTRY RE _ _ GION ID _ |  | 否 | cn-wulan-env17e- d01 |

智能体工厂 OpenTrek

**对象存储信息**

下表介绍对象存储配置时涉及的参数，包括参数项及含义，并给出了示例值，请根据用户实际填写。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| OBJECT STORAGE TYPE _ _ | 对象存储服务类型： MINIO：若后端对象存储为自建或第三方 MinIO 服务，请填写 MINIO 。 OSS：若使用阿里云企业版底座（如部署在阿里云 ECS 上）并对接阿里云对象存储服务（OSS），请填写 OSS 。 SEAWEEDFS：在AI Stack场景下支持此参数。 EOS AISTACK：在AI Stack场景下支持 _ 此参数。 | 是 | MINIO |
| OBJECT STORAGE END _ _ POINT | 对象存储访问地址： on AI Stack部署时，如需获取此值，可参见对象存储SDS-X。 | 是 | http://1.2.3.4:3000 1 |
| OBJECT STORAGE PUBL _ _ IC ENDPOINT _ |  | 否 | http://1.2.3.4:3000 1 |
| OBJECT STORAGE BUC _ _ KET | bucket名称。 on AI Stack部署时，如需获取此值，可参见对象存储SDS-X。 | 是 | minio-06**** |
| OBJECT STORAGE ACC _ _ ESS KEY ID _ _ | 对象存储访问用的AK。 on AI Stack部署时，如需获取此值，可参见对象存储SDS-X。 | 是 | xxxxxxxx |
| OBJECT STORAGE ACC _ _ ESS KEY SECRET _ _ | 对象存储访问用的SK。 on AI Stack部署时，如需获取此值，可参见对象存储SDS-X。 | 是 | xxxxxxxx |

智能体工厂 OpenTrek

| OSS STS ROLE ARN _ _ _ | 唯一标识的RAM角色，用于给OSS/MINIO STS角色授权。 | 否 | sts.aliyuncs.com |
|---|---|---|---|
| OSS PROTOCOL _ | 可选参数： http https 默认填写 http。 | 否 | http |
| STS OPENAPI ENDPOIN _ _ T | STS OpenAPI服务地址。 在On 企业版ECS部署时，且 OBJECT STORAGE TYPE为OSS时，需要 _ _ 填写此参数。 on 企业版ECS：OSS角色授权配置操作。 on VM/裸金属不需要填写。 | 否 | STS OPENAPI END _ _ POINT |

**管控区PostgresSql**

下表介绍管控区PostgresSql配置时涉及的参数，包括参数项及含义，并给出了示例值，请根据用户实际填写。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| PG HOST _ | 数据库的host地址 | 是 | 192.168.3.148 |
| PG PORT _ | 数据库端口 | 是 | 30005 |
| PG USERNAME _ | 数据库登录用户名 | 是 | postgres |
| PG PASSWORD _ | 数据库登录密码 | 是 | Passw*** |
| PG SSL ENABLE _ _ | 是否启用 SSL | 否 | false |

**缓存数据库**

下表介绍缓存数据库配置时涉及的参数，包括参数项及含义，并给出了示例值，请根据用户实际填写。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|

智能体工厂 OpenTrek

| REDIS REDIS MODE _ _ | redis的运行模式，可能是single（单机模式）或 cluster （集群）模式，请根据实际填写。 | 是 | single |
|---|---|---|---|
| REDIS HOST _ | 请根据 Redis 部署模式（单节点或集群）填写。 Cluster 模式：填写Redis 节点的 IP:Port 。REDIS PORT使用默认值 _ 填充即可。 Single 模式：请填写 Redis 服务器的 IP 地址。 | 是 | 1.2.3.4 |
| REDIS PORT _ | 请根据 Redis 部署模式（单节点或集群）填写。 Cluster 模式：使用默认值填充即可。 Single 模式：请填写 Redis 服务器的端口。 | 是 | 30009 |
| REDIS PASSWORD _ | Redis密码 | 否 | Qzy****34 |
| REDIS SSL ENABLE _ _ | 是否启用SSL | 否 | false |

**向量数据库信息**

下表介绍向量数据库配置时涉及的参数，包括参数项及含义，并给出了示例值，请根据用户实际填写。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| VECTOR DB HOST _ _ | 向量数据库的地址 | 否 | 1.2.3.4 |
| VECTOR DB PORT _ _ | 向量数据库的端口 | 否 | 30007 |
| VECTOR DB USERNA _ _ ME | 向量数据库登录用户名 | 否 | post**** |
| VECTOR DB PASSWO _ _ RD | 向量数据库登录密码 | 否 | Qzyx%**** |

智能体工厂 OpenTrek

| VECTOR DB TYPE _ _ | 指定所使用的 AnalyticDB for PostgreSQL（ADBPG）底层向量计算引擎类型，请根据实际数据库版本填写： pgvector ：若您的 ADBPG 实例基于开源 pgvector 插件提供向量检索能力，请填写此值。 adbpg ：若使用阿里云 AnalyticDB for PostgreSQL 原生向量引擎（即企业版内置优化版本），请填写此值。 milvus：若向量检索由外部 Milvus 向量数据库提供，而非通过 ADBPG 内置引擎实现，请填写此值。注意：选择 milvus 时， 需确保已独立部署并配置好 Milvus 服务， 且系统具备与之通信的网络和权限。 | 否 | pgvector |
|---|---|---|---|

**ElasticSearch信息**

下表介绍ElasticSearch配置时涉及的参数，包括参数项及含义，并给出了示例值，请根据用户实际填写。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| ES HOST _ | ElasticSearch连接的主机地址 | 否 | 1.2.3.4 |
| ES PORT _ | ElasticSearch的端口 | 否 | 30008 |
| ES USERNAME _ | ElasticSearch连接用户名 | 否 | ela**** |
| ES PASSWORD _ | ElasticSearch连接密码 | 否 | Qzyx%**** |
| ES PROTOCOL _ | 可选参数： http https 默认填写 http。 | 否 | http |

**租户区PG数据库配置**

下表介绍租户区PG数据库配置时涉及的参数，包括参数项及含义，并给出了示例值，请根据用户实际填写。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| RELATIONAL DB HOST _ _ | PG数据库连接的主机地址 | 否 | 1.2.3.4 |

智能体工厂 OpenTrek

| RELATIONAL DB PORT _ _ | PG数据库的端口 | 否 | 30005 |
|---|---|---|---|
| RELATIONAL DB USER _ _ NAME | PG数据库连接用户名 | 否 | post**** |
| RELATIONAL DB PASS _ _ WORD | PG数据库连接密码 | 否 | Qzyx%**** |
| RELATIONAL DB SSL _ _ _ ENABLE | 是否启用SSL | 否 | false |

**K8s集群信息**

下表介绍K8s集群配置时涉及的参数，包括参数项及含义，并给出了示例值，请根据用户实际填写。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| CLUSTER INGRESS SL _ _ B IP _ | Kubernetes 集群中 Ingress Controller 所绑定的对外负载均衡（SLB）IP 地址。 | 否 | 1.2.3.4 |
| CLUSTER INGRESS SL _ _ B INTERNAL IP _ _ | Kubernetes 集群中 Ingress Controller 所绑定的对内负载均衡（SLB）IP 地址。 请填写任一master节点所在IP。 | 否 | 1.2.3.4 |
| CLUSTER API SERVER _ _ SLB IP _ _ | Kubernetes API Server 的负载均衡 IP。 请填写任一master节点所在IP。 | 否 | 1.2.3.4 |
| CLUSTER DUBBO SLB _ _ IP _ | Dubbo RPC 服务注册中心的负载均衡 IP。 请填写任一master节点所在IP。 | 否 | 1.2.3.4 |
| API GATEWAY ENDPOI _ _ NT | API Gateway 服务地址。适用于AI Stack、公共云 VPC场景。 on 企业版ECS/VM&裸金属部署：请填写unused。 on AI Stack部署：http://cop-gateway-admin- svc.higress-system.svc.cluster.local 说明 higress-system 是其部署的 namespace， 不同版本可能不同，可通过命令：kubectl get svc -A \| grep cop-gateway 查询 on VPC（PublicCloudVPC）部署：自动配置。 | 否 | unused |

智能体工厂 OpenTrek

| GW INSTANCE ID _ _ | AI Gateway 实例信息。 on 企业版ECS/VM&裸金属部署：请填写default。 on AI Stack部署：请从中间件API网关上获取。 on VPC（PublicCloudVPC）部署：自动配置。 | 否 | default |
|---|---|---|---|

**应用配置**

CoWorker配置。

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| COWORKER PUBLIC KEY _ _ | CoWorker公钥配置。 如果未部署 CoWorker，则使用默认值即可。 获取方式：请务必使用CoWorker 公钥和私钥生成中的步骤生成密钥后，再填写使用，不要使用默认展示值。 | 是 | Dqjk********Tcpi |

**日志配置**

| 参数 | 说明 | 是否必填 | 获取方法 | 示例值 |
|---|---|---|---|---|
| TIANYAN ENABLE _ D | 是否部署天眼。默认填写 false | 否 | 请根据实际部署情况填写。 | false |

**Tracing配置**

|  | 参数 |  |  | 说明 |  |  |  | 是否必填 | 示例值 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | OTEL TRACE ENDPOIN _ _ T |  |  | OTLP HTTP Trace上报入口（完整 URL，包含/v1/traces路径） MONITOR MODE=opentrek monitor _ _ 时使用此地址，默认值指向天眼tempo， 兼容原有天眼链路。 切换到product-aistack-monitor的 |  |  |  |  | http://otel- |  |  |
|  |  |  |  |  |  |  |  |  | collector.aistack- |  |  |
|  |  |  |  |  | istack-monitor的 |  |  | 是 |  |  |  |
|  |  |  |  |  |  |  |  |  | monitor.svc.cluster. |  |  |
|  |  |  |  | otel-collector时填： |  |  |  |  |  |  |  |
|  |  |  |  |  |  | http://otel- |  |  | local:4318 |  |  |
|  |  |  |  | collector.aistack- |  |  |  |  |  |  |  |
|  |  |  |  | monitor.svc.cluster.local:4318/ |  |  |  |  |  |  |  |
|  |  |  |  | v1/traces |  |  |  |  |  |  |  |

**OSS NGINX代理**

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|

智能体工厂 OpenTrek

| DEPLOY OSS NGINX _ _ | 是否部署 OSS 透明代理组件（sfm-oss- nginx） 无该场景需求默认false | 是 | false |
|---|---|---|---|
| OSS NGINX PROXY E _ _ _ NDPOINT | OSS 透明代理后端接入点，例如 oss- cn-hangzhou- internal.aliyuncs.com（仅 DEPLOY OSS NGINX=true 时生效） _ _ | 否 | oss-cn-beijing- internal.aliyuncs.com |
| OSS NGINX METRICS _ _ _ ENABLED | 是否为 oss-nginx 开启 Prometheus 监控（集群已有 Prometheus Operator 时开启，仅 DEPLOY OSS NGINX=true 时生效） _ _ | 否 | false |
| OSS NGINX TLS ENAB _ _ _ LED | 是否为 oss-nginx 开启 TLS/HTTPS（仅 DEPLOY OSS NGINX=true 时生效） _ _ | 否 | false |
| OSS NGINX DOMAIN _ _ | oss-nginx 域名访问基础域名，virtual- hosted 访问形如 .<该域名>，Ingress 使用泛域名 *.<该域名>（仅 DEPLOY OSS NGINX=true 时生效） _ _ | 否 | oss.vm.pipelinevm071 0.com |

**Knowledge Wave配置**

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| AGENT ENABLED _ | 是否开启Agent，只有部署Knowledge Base时才需要设置成true。 | 是 | false |
| GRAPH ENABLED _ | 是否开启图的能力，只有部署 Knowledge Base并且需要图能力时才需要设置成true。 | 是 | false |
| GRAPH EXTENSION N _ _ AME | 图插件名称，只有GRAPH ENABLED为 _ true时才需要，目前两个值：age、 polar age，根据pg里面的实际的图插件 _ 类型填写，一般阿里云的polardb是 polar age。 _ | 否 | age |

智能体工厂 OpenTrek

**DKE内置解析服务配置**

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| DATA MIXER REPLICA _ _ S | 解析服务的副本数。 | 是 | 2 |
| DATA MIXER CPU _ _ | 单个解析Pod的CPU。 | 是 | 4 |
| DATA MIXER MEMORY _ _ | 单个解析Pod的内存。 | 是 | 8 Gi |

**可观测配置**

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| MONITOR MODE _ | 可观测方案，支持的方式： none：不接入可观测。 opentrek monitor：接入OpenTrek _ Monitor（otel-collector）进行可观测。 | 否 | opentrek monitor _ |
| AISTACK MONITOR NA _ _ MESPACE | product-aistack-monitor平台部署所在的K8s命名空间。用于文档/运维定位。 | 否 | aistack-monitor |

**Knowledge Claw配置**

| 参数 | 说明 | 是否必填 | 示例值 |
|---|---|---|---|
| KW DEFAULT USER A _ _ _ PI KEY _ | 知识引擎默认用户 API Key。不需要修改，使用默认值即可。 | 否 | false |
| CLAW AUTH ENABLED _ _ | claw认证开关，不需要修改，使用默认值即可。 | 否 | true |
| CLAW AUTH PASSWO _ _ RD | claw认证密码，不需要修改，使用默认值即可。 | 否 | xxx |

智能体工厂 OpenTrek

| CLAW ENGINE AUTH _ _ _ TOKEN | 调 knowledge-engine 的认证 Token， 不需要修改，使用默认值即可。 | 否 | xxx |
|---|---|---|---|
| DASHSCOPE API KEY _ _ | DashScope 全局 API Key，不需要修改，使用默认值即可。 | 否 | xxx |
| DASHSCOPE ENABLE _ _ ENCRYPTION | DashScope 加密开关，不需要修改，使用默认值即可。 | 否 | false |
| CLAW LLM API KEY _ _ _ | Claw 内部 LLM API Key，不需要修改， 使用默认值即可。 | 否 | xxx |
| CLAW LLM BASE URL _ _ _ | LLM 服务地址，不需要修改，使用默认值即可。 | 否 | xxx |
| CLAW LLM MODEL _ _ | LLM 模型名称，不需要修改，使用默认值即可。 | 否 | qwen3.7-max |
| QUARK SEARCH API K _ _ _ EY | 夸克搜索（IQS）API Key，不需要修改，使用默认值即可。 | 否 | xxx |
| QUARK SEARCH ENDP _ _ OINT | 夸克搜索 Endpoint，不需要修改，使用默认值即可。 | 否 | xxx |
| JUICEFS CACHE STOR _ _ AGE CLASS _ | juiceFS 缓存盘容量（GB），缓存配额取其 80%，不需要修改，使用默认值即可。 | 否 | xxx |
| JUICEFS CACHE PVC S _ _ _ IZE GB _ | 填写pvc storage class。默认空值，使用emptydir存储数据，不需要修改，使用默认值即可。 | 否 | 40 |

智能体工厂 OpenTrek

| 区域 | 参数名称 | 参数说明 | 示例值 |
|---|---|---|---|
| CLOUD TYPE MODE _ _ |  | 支持的参数： AiStack：适用于在 AI Stack 一体化平台环境中的部署场景，请选择此项。 Light：用于纯软版的轻量级部署场景，即On VM/裸金属部署和On 企业版ECS部署请选择此项。 PublicCloudVPC：适用于在公有云 VPC网络环境中的部署场景，请选择此项。计算巢直接拉起，不需要用户感知。 | Light |
| PG数据库配置信息 | PG HOST _ | 请输入PG数据库的Host。 | 1.2.3.4 |
|  | PG PORT _ | 请输入PG数据库的Port。 | 30005 |
|  | PG USERNAME _ | 请输入PG数据库的用户名。 | post**** |
|  | PG PASSWORD _ | 请输入PG数据库用户名对应的密码。 | Pass**** |

智能体工厂 OpenTrek

|  | POP配置信息 | DEV API MODE _ _ | openapi：Opentrek-Agent Dev部署形态为独立登录，未接入Unimanager Lite请填写此参数，此时，POP AK、POP SK、POP ENDPOINTE、 _ _ _ POP REGION可不填或者填写为xxx。 _ pop：Opentrek-Agent Dev部署接入了 Unimanager Lite请填写此参数。 |  |  |  |  |  | pop |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | POP ENDPOINT _ E | 当OpenTrek Agent Dev非飞天企业版时，请填写 pop- service.unimanager.svc.cluster.local 。 |  |  |  |  |  | pop- |  |  |
|  |  |  |  |  |  |  |  |  |  | pop- |  |
|  |  |  |  |  |  |  |  |  | service.unima |  |  |
|  |  |  |  |  |  |  |  |  |  | service.unima |  |
|  |  |  |  |  | ager.svc.cluster.local | ter.local | 。 |  |  |  |  |
|  |  |  |  |  |  |  |  |  | ster.local |  |  |
|  |  | POP REGION _ | 默认为aistack，无需修改。 |  |  |  |  |  | aistack |  |  |
|  | DEV交互配置 | SFM APP KEY _ _ | 请输入在DEV平台申请具有全部空间权限的APPKEY。 详细的申请方式，请参见，《OpenTrek Agent Dev 用户指南》的《APP KEY》章节。 _ |  |  |  |  |  | ql0rEZ6ySXd34 x3wK1NH6fQJq qFT**** |  |  |
|  |  | SFM CONTROL _ _ API ENDPOINT _ | 请输入Opentrek-Agent Dev管控区API调用地址， 已接入了UniManager Lite：请填写任意非空内容即可。 未接入UniManager Lite：请填写OpenTrek Agent Dev控制台的IP:Port。您可以在已部署的OpenTrek Agent Dev的实例详情页面查看Domain的值。 |  |  |  |  |  | xxx |  |  |
|  |  | SFM TENANT A _ _ PI ENDPOINT _ | Opentrek-Agent Dev租户区API调用地址，一般是租户区ingress ip + 80端口。您可以登录OpenTrek Agent Dev控制台，在OpenAPI页面的应用集成类下查看任一接口的调用地址中的IP:Port。 |  |  |  |  |  | http://1.2.3.4:8 0 |  |  |
|  |  | TIANYAN ENAB _ LED | 是否部署天眼。默认填写 false |  |  |  |  |  | false |  |  |
|  |  | MONITOR MOD _ E | 可观测方案，支持的方式： none：不接入可观测。 opentrek monitor：接入OpenTrek _ Monitor（otel-collector）进行可观测。 |  |  |  |  |  | opentrek moni _ tor |  |  |

智能体工厂 OpenTrek

|  |  | AISTACK MONI _ TOR NAMESPA _ CE |  | product-aistack-monitor平台部署所在的K8s命名空间。用于文档/运维定位。 |  |  |  |  |  |  |  | aistack- monitor |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | OTEL TRACE E _ _ NDPOINT |  | OTLP HTTP Trace上报入口（完整URL，包含/v1/traces路径） MONITOR MODE=opentrek monitor时使用此地址， _ _ 默认值指向天眼tempo，兼容原有天眼链路。 切换到product-aistack-monitor的otel-collector时填： http://otel-collector.aistack- |  |  |  |  |  |  |  | http://otel |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | http://otel |  |
|  |  |  |  |  |  |  |  |  |  |  |  | - |  |  |
|  |  |  |  |  |  |  |  |  | 使用此地址， |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | collector.ais |  |  |
|  |  |  |  |  |  |  |  | _ 兼容原有天眼链路。 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | tack- |  |  |
|  |  |  |  |  |  |  | stack-monitor的otel-collector时 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | monitor.svc.c |  |  |
|  |  |  |  |  | 填： | http://otel-collector.aistack- |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | luster.local: |  |  |
|  |  |  |  | monitor.svc.cluster.local:4318/v1/traces |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 4318 |  |  |
|  |  | COWORKER RE _ PLICAS |  | 请输入coworker基础服务副本数量，控制基础服务拉起 Pod的副本数。 |  |  |  |  |  |  |  | 2 |  |  |
|  |  | COWORKER SE _ SSION REPLICA _ S |  | 请输入coworker会话服务副本数量，控制会话服务拉起 Pod的副本数。 |  |  |  |  |  |  |  | 2 |  |  |
|  |  | COWORKER PRI _ VATE KEY _ |  | 请输入与DEV进行非对称加密通信的私钥。 获取方式：请务必使用CoWorker公钥和私钥生成中的步骤生成密钥后，再填写使用，不要使用默认展示值。 |  |  |  |  |  |  |  | MIIE********TRf i |  |  |

#### License申请

本章节介绍如何获取License。 请联系SA（解决方案架构师）获取License。

### 部署实施

本章节及其子章节介绍产品部署及配置的完整操作指导，涵盖依赖产品准备、产品部署和部署后配置全过程。

#### 产品部署

本章节及其子章节系统介绍了在 OpenTrek-UniOperator 平台上部署 OpenTrek Agent Dev和 OpenTrek CoWorker的完整流程，主要包括三部分内容：
1. 产品导入：说明如何将产品制品包通过平台导入功能注册到产品管理中。
2. Agent Dev 部署：指导用户在完成产品导入后，配置基础信息与资源参数，完成 Agent Dev 实例的部
署。
3. CoWorker 部署：指导用户在完成产品导入后，配置基础信息与资源参数，完成 CoWorker 实例的部
署。

##### 导入产品

**使用场景**

智能体工厂 OpenTrek

**使用场景**

当您需要将服务商提供的新产品导入到产品管理时，可使用导入功能。

**前提条件**

在K8s集群部署unioperator，具体步骤请参考《Uni-Operator 部署指南》。 已获取对应的软件包并导入到客户现场。

**操作步骤**

1. 登录AI Stack控制台，在顶部导航栏选择**平台运维**。
2. 在左侧导航栏中，单击**产品列表**。
3. 单击页面左上方的**导入产品**按钮，打开导入对话框。
i. 获取制品目录的绝对路径。 在部署机通过 `cd` 命令进入安装包的目录，然后执行 `pwd` 命令查看绝对路径。 智能体工厂 OpenTrek ii. 填写上个步骤获取的绝对路径，例如： `/data/cicd/package-dir` 可单击**查看填写说明**，查看CICD制品目录说明。 同时兼容支持填写旧版product-*.tar.gz 制品路径，例如： `/data/packages/product-`

```
example.tar.gz
```

iii. 可选：单击**指定解包临时目录**自定义解压路径。 默认使用 `/tmp/product_import` 解包，根目录空间不足时可指向大盘磁盘上的绝对路径，导入完成后自动清理。 智能体工厂 OpenTrek iv. 单击**生成命令**，系统生成导入脚本。 v. 单击**复制命令**并在服务器终端中执行该命令，最终提示success表示导入成功。 vi. 最后单击**完成**。
4. 导入完成后，在**产品列表**页面可以看到新导入的产品，产品列表显示**产品名称**、**产品****Code**、**版本**等信
息。

##### Agent Dev部署

**说明**

密码类信息，最好复制粘贴，避免手敲导致的信息错误。

**前提条件**

智能体工厂 OpenTrek 已完成Agent Dev导入，即Uni-Operator控制台产品列表中已有**百炼专属版****standard**。具体操作，请参见导入产品。

**部署配置**

1. 登录AI Stack控制台，在顶部导航栏选择**平台运维**。
2. 在**产品列表**页面，单击目标产品**操作**列的**部署**。
3. 在**产品部署**页面，进入部署向导。
i. 填写**基础配置**。

| 参数 | 说明 | 校验规则 |
|---|---|---|
| 实例名称 | 产品实例的自定义名称，部署完成后显示在产品实例列表中。 | 长度不超过 64 个字符；必须以英文字母开头；可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |
| 实例描述 | 产品实例的描述信息。 | 长度为 2~256 个字符；不能以 http:// 或 https:// 开头；支持中英文、数字、 全角字符及 - . 半角字符。 _ |
| 版本 | 要部署的产品版本。下拉列表显示格式为"版本号 (修订号)"。 | 必填。 选择目标版本或者一键导入。 |
| 规格 | 产品的规格/功能版本。不同规格对应不同的应用配置项和资源需求。版本选择后可用。 | 必填。 |

智能体工厂 OpenTrek ii. **依赖检查**步骤无需配置。单击**下一步**。 iii. 填写**资源**&**应用配置**信息。 iv. 在右下角单击**开始执行**，相关服务会陆续拉起。
4. 部署完成后，您可以在OpenTrek-UniOperator 平台的**产品实例**列表看到刚部署的产品。
5. 查看部署日志。
智能体工厂 OpenTrek i. 单击目标实例操作列的**查看详情**，进入实例详情页。 ii. 单击界面右侧的**详情**，可以查看部署日志。

##### CoWorker部署

CoWorker支持在K8s环境中通过 OpenTrek-UniOperator 平台完成图形化部署，配置数据库连接、平台集成参数和授权许可证。本文介绍CoWorker部署的完整流程，包括环境检查、配置参数、依赖验证和授权激活等步骤。

**前提条件**

已申请部署时所需的资源。 已申请CoWorker的License。 OpenTrek-UniOperator已是最新版本，如果不是请升级至最新版本。 已部署OpenTrek Agent Dev。 已完成OpenTrek Coworker导入，即Uni-Operator控制台产品列表中已有**OpenTrek**
**CowWorker**。具体操作，请参见导入产品。

**操作步骤**

1. 登录AI Stack控制台，在顶部导航栏选择**平台运维**。
智能体工厂 OpenTrek
2. 在**产品列表**页面，单击目标产品**操作**列的**部署**。
3. 在**产品部署**页面，进入部署向导。
i. 填写**基础配置**。

| 参数 | 说明 | 校验规则 |
|---|---|---|
| 实例名称 | 产品实例的自定义名称，部署完成后显示在产品实例列表中。 | 长度不超过 64 个字符；必须以英文字母开头；可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |
| 实例描述 | 产品实例的描述信息。 | 长度为 2~256 个字符；不能以 http:// 或 https:// 开头；支持中英文、数字、 全角字符及 - . 半角字符。 _ |
| 版本 | 要部署的产品版本。下拉列表显示格式为"版本号 (修订号)"。 | 必填。 选择目标版本或者一键导入。 |
| 规格 | 产品的规格/功能版本。不同规格对应不同的应用配置项和资源需求。版本选择后可用。 | 必填。 |

ii. 在**依赖检查**阶段。 依赖检查步骤无需配置，直接单击**下一步**。 iii. 在**资源**&**应用配置**阶段。 参数配置，请参见CoWorker参数说明。 iv. 配置参数后单击**开始执行**。
4. 在**完成**阶段，等待部署成功。
5. 在 OpenTrek-UniOperator 的许可证管理页面，单击**导入授权**。
6. 选择提前获取的授权资源包并导入。

#### 部署后配置

##### 模型部署和接入

部署完成后，请继续执行以下步骤完成模型接入，配置完成后即可开始创建和使用智能体。

**模型参考清单**

**说明**

OpenTrek Agent Dev 运行需依赖特定模型资源，请预先准备如下类型的模型。请在每种模型类型中至少选择一个。 下方展示的模型仅供参考示例。考虑到模型更新频繁，请您结合具体业务场景，灵活选择最新的同类模型。 智能体工厂 OpenTrek

| 模型类型 | 示例模型 |
|---|---|
| 大语言模型 | qwen3.6-plus |
|  | qwen3.6-max-preview |
|  | qwen3.6-flash |
|  | deepseek-v4-flash |
|  | deepseek-v4-pro |
|  | kimi-k2.6 |
|  | glm-5.1 |
|  | MiniMax-M2.5 |
|  | Qwen3.5-plus |
|  | Qwen3.5-Flash |
|  | Qwen3-Max |
|  | Qwen-Plus |
|  | Qwen-Max |
|  | deepseek-v3.2 |
|  | deepseek-r1 |
| 多模态理解大模型 | qwen3.6-plus |
|  | qwen3.6-flash |
|  | Qwen3.5-plus |
| 7 | > 文档版本：2026090 |

| 智能体工厂 OpenTrek |  |
|---|---|
|  | Qwen3.5-Flash |
|  | Qwen3-VL-Flash |
| 文本向量模型 | text-embedding-v4 |
| 多模态向量模型 | qwen3-vl-embedding |
| 文本精排模型 | qwen3-rerank |
| 多模态精排模型 | qwen3-vl-rerank |

**公共云百炼模型服务接入**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏选择**系统管理** > **内置服务** > **模型接入**。
3. 切换到**三方注册模型**。
4. 单击**接入模型**。接入方式请选择**公共云百炼模型服务接入**。
参数详情请参见《OpenTrek Agent Dev 用户指南》的《模型接入》章节。

**AI Studio模型服务接入**

**通过平台部署模型接入模型**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏选择**系统管理** > **内置服务** > **模型接入**。
默认进入到**平台部署模型**页面。
3. 单击**接入模型**。
可直接通过下拉框快速完成接入，用户只需输入**模型服务名称**。参数详情请参见《OpenTrek Agent Dev 用户指南》的《模型接入》章节。 选择某一个模型类型后，请按下表选择对应模型协议：

| 模型类型 | 模型协议类型 |
|---|---|
| 大语言模型 | OpenAI预测接口 |
| 多模态理解 | OpenAI预测接口 |
| 文本向量化 | OpenAI embedding接口 |
| 多模态向量 | 预测接口 |

智能体工厂 OpenTrek

| 文本精排 | Qwen文本精排接口 |
|---|---|
| 多模态精排 | 预测接口 |

**通过三方注册模型接入模型**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏选择**系统管理** > **内置服务** > **模型接入**。
3. 单击**三方注册模型**。
4. 单击**接入模型**。
可直接通过下拉框快速完成接入，用户只需输入**模型服务名称**。参数详情请参见《OpenTrek Agent Dev 用户指南》的《模型接入》章节。 i. 需要额外配置请求头：key为Authorization，value为Bearer {apiKey} （Bearer后面有一个空格） ii. **选择模型****API_KEY**可到AIStudio页面查询。
5. 选择某一个模型类型后，请按下表选择对应模型协议、服务地址：

| 模型类型 | 模型协议类型 | 服务地址 |
|---|---|---|
| 大语言模型 | OpenAI预测接口 | http://{VPC专有网络输入地址}/v1/chat/completions |
| 多模态理解 | OpenAI预测接口 | http://{VPC专有网络输入地址}/v1/chat/completions |
| 文本向量化 | OpenAI embedding接口 | http://{VPC专有网络输入地址}/v1/embeddings |

智能体工厂 OpenTrek

| 多模态向量 | 预测接口 | http://{VPC专有网络输入地址}/api/predict |
|---|---|---|
| 文本精排 | Qwen文本精排接口 | http://{VPC专有网络输入地址}/v1/rerank |
| 多模态精排 | 预测接口 | http://{VPC专有网络输入地址}/api/predict |

服务地址中的**VPC****专有网络输入地址**可在AIStudio页面上进行查询。

**AIStack模型接入**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏选择**系统管理** > **内置服务** > **模型接入**。
3. 切换到**三方注册模型**。
4. 单击**接入模型**。接入方式请选择**自定义接入**。
参数详情请参见《OpenTrek Agent Dev 用户指南》的《模型接入》章节。 选择某一个模型类型后，请按下表选择对应模型协议、服务地址：

| 模型类型 | 模型协议类型 | 服务地址 |
|---|---|---|
| 大语言模型 | OpenAI预测接口 | 模型实际地址 |
| 多模态理解 | OpenAI预测接口 | 模型实际地址 |
| 文本向量化 | OpenAI embedding接口 | 模型实际地址 |
| 多模态向量 | 公有云百炼接口 | 模型实际地址 |

智能体工厂 OpenTrek

| 文本精排 | OpenAI embedding接口 | 模型实际地址 |
|---|---|---|
| 多模态精排 | AIStack重排接口 | 模型实际地址 |

##### DKE资产部署

**前提条件**

OpenTrek Agent Dev已部署成功。

**说明**

以下流程均以所有包出在文件夹路径为/apsarapangu/ahm/dke_resource为例。 文件夹路径必须为空，不要含其他文件！建议命名为dke_resource。

**操作步骤**

1. 拷贝获取资产包中出盘的资产包到现场管控机器上。
2. 进入资产目录，解压元数据资产包后查看镜像元数据。
# 进入资产目录

```
cd /apsarapangu/ahm/runtime-resources/dke/30bi4l27p24733gbbq6j15itjm
```

# 解压元数据资产包

```
tar -xvf _file/sfm-models-resource/metadata/metadata.tar -C _file/sfm-models-resource /metadata/
```

# 查看镜像元数据（这里是全量`DKE`镜像元数据，会比实际导入的镜像要多）

```
cat _file/sfm-models-resource/metadata/metadata/image_info.json
```

智能体工厂 OpenTrek
# 查看镜像列表（这里是实际导入的镜像）

```
ls -al _docker_image/docker/registry/v2/repositories/dke-apsara
```

3. 上传资产包。
#执行资产自动上传脚

```
cd _file/sfm-models-resource/deploy_script/
```

#解压资产上传脚本，如果已经有`deploy.sh`不需要解压

```
tar -xvf deploy.tar -C . chmod +x deploy.sh ./deploy.sh
```

智能体工厂 OpenTrek
4. 若脚本执行失败，请按以下步骤执行rolling dke-resource-init job。
i. 登录Uni-Operator控制台。 ii. 选择**平台运维** > **产品实例**。 iii. 单击目标OpenTrek Agent Dev实例操作列的**升级**。具体操作，请参见实例升级。

**验证**

**AI Studio融合部署环境**

1. 登录AI Studio控制台。
2. 在左侧导航栏选择**AI** **资产管理** > **镜像库**。
智能体工厂 OpenTrek
3. 搜索**dke**，看到dke相关镜像，则证明导入成功。

**未部署AI Studio的环境**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏选择**数据** > **数据加工**。
3. 切换到**数据加工任务**页面。
4. 单击**新建任务**，模板选择依赖GPU的，例如模板名称中包含“**PDF****深度解析**”的。
5. 配置任务。
在任务详情中选择带GPU的资源组。
6. 运行任务。
7. 验证结果。
在任务运行总览中，正常 pulling data-mixer-operators:3.x.0-nvidia 这类标签的镜像，则导入成功。

##### 模型上架OpenTrek CoWorker

**注意事项**

上架至 CoWorker 的模型须同时满足两项要求： 支持 Function Call 功能上下文Tokens限制大于 128K Tokens。

**操作步骤**

1. 登录OpenTrek Agent Dev控制台。
2. 完成模型部署和接入。

**说明**

接入的时候需要**勾选**下面的选项：

**Function Call**

**支持TrekAgent**

**上下文****Tokens****限制**需要大于128K。
智能体工厂 OpenTrek
3. 在**系统管理** **> CoWorker****上架**中进行模型服务上架。详细操作，请参见《OpenTrek Agent Dev用户
指南》。
4. 配置完成后，在**CoWorker****上架**页可以看到该模型。
5. 登录OpenTrek Coworker控制台。
6. 在左侧导航栏选择**运营管理**。
切换到**模型服务授权**页面，进行模型授权，授权操作完成之后CoWorker就可以选到新上架的模型。

### 部署验证

#### 控制台访问验证

本章节介绍具体的登录方法和验证方式。

**Agent Dev控制台验证**

1. 登录OpenTrek控制台。
2. 首页正常展示Agent Dev卡片。
3. 单击Agent Dev卡片，进入Agent Dev控制台。
4. 可以正常登录并且前端页面显示正常说明已部署成功。
智能体工厂 OpenTrek

**CoWorker控制台验证**

1. 登录OpenTrek控制台。
2. 首页正常展示CoWorker卡片。
3. 单击CoWorker卡片，进入CoWorker控制台。
4. 可以正常访问并查看每个页面。

#### 功能验证

本章节介绍通过K8s命令验证Agent Dev各组件Pod状态的方法，确保管控组件和租户区组件正常运行，帮助用户确认系统功能完整性。

**Agent Dev组件状态验证**

**管控组件状态验证**

执行以下命令查看pod是否都到Running状态

```bash
kubectl get pod -n agentstudio
```

智能体工厂 OpenTrek

**租户区组件状态验证**

执行以下命令查看pod是否都到Running状态

```bash
kubectl get pod -n sfm-agent-studio kubectl get pod -n sfm-agent-xdb kubectl get pod -n sfm-agent-cluster
```

**CoWorker组件状态验证**

登录K8s节点，执行以下命令，查看Pod是否已到Running状态。 智能体工厂 OpenTrek

```bash
kubectl get pod -n opentrek-coworker
```

### 升级与卸载

#### 升级前准备及说明

**从AI Stack V2.16.0及以下版本升级到V2.17.0及以上版本**

1. 实例升级。
2. 基础资源迁移。
i. 数据库PolarDB。 a. 执行命令。

```bash
kubectl exec -it $(kubectl get pods -A --no-headers | grep 'resreg-process' | hea d -1 | awk '{print "-n", $1, $2}') -- bash
```

# 登录元数据库，执行以下`SQL`

```
select * from aihub_polardb where tenant = 'baseline'\G echo 'QUlTdGFja0AxMjM=' | base64 -d
```

智能体工厂 OpenTrek b. 登录OpenTrek Agent Dev控制台，在全局资源管理页面，添加资源。具体操作，请参见 《OpenTrek Agent Dev 用户指南》。 ii. SDS-X对象存储。 智能体工厂 OpenTrek a. 执行命令。

```bash
kubectl exec -it $(kubectl get pods -A --no-headers | grep 'resreg-process' | hea d -1 | awk '{print "-n", $1, $2}') -- bash
```

# 登录元数据库，执行以下`SQL`

```
select * from aihub_oss where tenant = 'baseline'\G echo 'aHU3cXBtdHRqb2Q4OTYwYzNmM3E=' | base64 -d echo 'ZGEybjE3MjkyeXp4cHpwenA5bnNhdnB4ajE2dzBhYmU0NHVqbnNlMw==' | base64 -d
```

b. 登录OpenTrek Agent Dev控制台，在全局资源管理页面，添加资源。具体操作，请参见 《OpenTrek Agent Dev 用户指南》。 智能体工厂 OpenTrek iii. 镜像仓库 ACR。 a. 执行命令。

```bash
kubectl exec -it $(kubectl get pods -A --no-headers | grep 'resreg-process' | hea d -1 | awk '{print "-n", $1, $2}') -- bash
```

# 登录元数据库，执行以下`SQL`

```
select * from aihub_acr where tenant = 'baseline'\G echo 'QUlTdGFja0AxMjM=' | base64 -d
```

b. 登录OpenTrek Agent Dev控制台，在全局资源管理页面，添加资源。具体操作，请参见 《OpenTrek Agent Dev 用户指南》。 iv. 向量数据库。 智能体工厂 OpenTrek a. 执行命令。

```bash
kubectl exec -it $(kubectl get pods -A --no-headers | grep 'resreg-process' | hea d -1 | awk '{print "-n", $1, $2}') -- bash
```

# 登录元数据库，执行以下`SQL`

```
select * from aihub_adbpg where tenant = 'baseline'\G echo 'QUlTdGFja0AxMjM=' | base64 -d
```

b. 登录OpenTrek Agent Dev控制台，在全局资源管理页面，添加资源。具体操作，请参见 《OpenTrek Agent Dev 用户指南》。 智能体工厂 OpenTrek v. 缓存数据库。 a. 执行命令。

```bash
kubectl exec -it $(kubectl get pods -A --no-headers | grep 'resreg-process' | hea d -1 | awk '{print "-n", $1, $2}') -- bash
```

# 登录元数据库，执行以下`SQL`

```
select * from aihub_redis where tenant = 'baseline'\G echo 'cmVkaXM6QUlTdGFja0AxMjM=' | base64 -d
```

b. 登录OpenTrek Agent Dev控制台，在全局资源管理页面，添加资源。具体操作，请参见 《OpenTrek Agent Dev 用户指南》。 vi. 普通集群 ACK。 智能体工厂 OpenTrek a. 执行命令。

```bash
kubectl exec -it $(kubectl get pods -A --no-headers | grep 'resreg-process' | hea d -1 | awk '{print "-n", $1, $2}') -- bash
```

# 登录元数据库，执行以下`SQL`

```
select * from aihub_clusters where tenant = 'baseline' and deleted_at is NULL\G
```

b. 登录OpenTrek Agent Dev控制台，在全局资源管理页面，添加资源。具体操作，请参见 《OpenTrek Agent Dev 用户指南》。 智能体工厂 OpenTrek vii. 检索服务ES。 a. 执行命令。

```bash
kubectl exec -it $(kubectl get pods -A --no-headers | grep 'resreg-process' | hea d -1 | awk '{print "-n", $1, $2}') -- bash
```

# 登录元数据库，执行以下`SQL`

```
select * from aihub_es where tenant = 'baseline'\G
```

b. 登录OpenTrek Agent Dev控制台，在全局资源管理页面，添加资源。具体操作，请参见 《OpenTrek Agent Dev 用户指南》。
3. 终态检查。

#### 实例升级

**说明**

本文以OpenTrek Agent Dev为例介绍实例升级，Coworker的升级流程与之类似。

**操作步骤**

1. 登录AI Stack控制台。
2. 在顶部菜单栏选择**平台运维**。
3. 在左侧导航栏中单击**产品实例**。
智能体工厂 OpenTrek
4. 找到新导入的产品实例，例如：OpenTrek-Standard。
5. 单击操作列**升级**。
6. 选择**升级版本**，单击**下一步**。
7. 依赖检查步骤无需配置，单击**下一步**。
智能体工厂 OpenTrek
8. 填写**实例配置**，单击**开始执行**。
9. 观察升级过程，等待管控区升级完成。

**重要**

若升级过程中有失败项以及报错，优先将详细报错信息提供给技术支持人员。切勿私自点击跳过。
0. 登录OpenTrek Agent Dev控制台。
管控区升级完成后，在渲染变量区域获取DOMAIN信息，进入OpenTrek Agent Dev控制台。输入账号密码后，可登录OpenTrek Agent Dev平台。 智能体工厂 OpenTrek

#### 实例卸载

本文介绍如何在Uni-Operator统一运维平台卸载OpenTrek Agent Dev应用的具体操作步骤。

**说明**

本文以OpenTrek Agent Dev为例介绍实例卸载，Coworker的卸载流程与之类似。

**操作步骤**

1. 登录AI Stack控制台。
2. 在顶部菜单栏选择**平台运维**。
3. 在左侧导航栏中单击**产品实例**。
4. 找到产品code是“OpenTrek-Standard”的实例。
5. 单击操作列**卸载**。
智能体工厂 OpenTrek
6. 单击**确定**。

### 附录

#### on AI Stack

##### 中间件实例

本文介绍AI Stack下中间件实例的部署与配置方法，包括各组件的详细部署步骤、访问方式及使用注意事项。

**ACR**

1. 部署管控区和租户区ACR，具体操作，请参见《容器镜像服ACR 部署指南》。
管控区部署时ACR_NAMESPACE需要填写为sfm。
2. ACR配置：
i. 管控区 ahm-registry（管控侧 ACR）专用于托管应用部署所需的系统镜像，严禁存放任何客户镜像或业务镜像。 该仓库不具备对外服务能力且不符合客户数据的安全合规要求。如需托管客户镜像，请务必使用租户侧 ACR。 ii. 租户区配置。

**说明**

具体操作，请参见《容器镜像服务ACR用户指南》。 a. 访问租户区ACR工作台门户服务。 b. 创建命名空间。 创建时需填写命名空间名称，启用自动创建仓库功能，并选择默认仓库类型。 c. 修改访问凭证。

**PolarDB**

**管控区**

**说明**

中间件服务由 AI PaaS 提供，常见方式是通过 yaml 文件直接创建。 请严格按照规格部署，变更规格可能会引起产品部署资源不足，如需变更，请做好整体资源评估工作。 智能体工厂 OpenTrek
1. 准备yaml文件。yaml示例：

```
apiVersion: polardb.gitlab.alibaba-inc.com/v1 kind: LogicInstance metadata:
  name: pl-sfm-db
  namespace: polardb
  labels:
    app.kubernetes.io/name: aistack-db-operator
    app.kubernetes.io/managed-by: kustomize
spec:
  clusters:
  - clusterType: rw
    cpus: 1
    creator: admin
    dbVersion: pg14
    engineType: pg
    memory: 8
    storageSize: 100
    users:
    - decodePassword: {your_password}
      userName: polar_admin
    visibility: inner
  dbType: polarm
  insName: sfm-db
```

2. 执行 `kubectl apply -f xxxx.yaml` 命令。
3. 等待 PolarDB 命名空间下的 pod 就绪。
4. 此时的访问方式：
i. 地址：ps-sfm-db-0.polardb.svc.cluster.local ii. 端口： kubectl get svc -n polardb |grep sfm-db 自行查看实际端口号。 iii. 用户名：polar_admin iv. 密码：{your_password}
5. 查看刚刚部署的pod，命令示例：

```
#kubectl get pod -n polardb |grep sfm-db
#kubectl exec -it pi-sfm-db-0-pg-0-0 -n polardb -- bash /u01/polardb_pg/bin/psql -h p
```

`s-`

```
sfm-db-0.polardb.svc.cluster.local -p 61301 -U polar_admin -d postgres
```

**租户区**

**说明**

请严格按照规格部署，变更规格可能会引起产品部署资源不足，如需变更，请做好整体资源评估工作。
1. 准备yaml文件，yaml示例：
智能体工厂 OpenTrek

```
apiVersion: polardb.gitlab.alibaba-inc.com/v1 kind: LogicInstance metadata:
  name: pl-sfm-db-employ
  namespace: polardb
  labels:
    app.kubernetes.io/name: aistack-db-operator
    app.kubernetes.io/managed-by: kustomize
spec:
  clusters:
  - clusterType: rw
    cpus: 2
    creator: admin
    dbVersion: pg14
    engineType: pg
    memory: 16
    storageSize: 500
    users:
    - decodePassword: {your_password}
      userName: polar_admin
    visibility: inner
  dbType: polarm
  insName: sfm-db-employ
```

2. 执行 `kubectl apply -f xxxx.yaml` 命令。

**说明**

`xxxx.yaml` 请替换成实际yaml文件名。
3. 等待 PolarDB 命名空间下的 pod 就绪。
4. 此时的访问方式：
i. 地址：ps-sfm-db-0.polardb.svc.cluster.local ii. 端口：kubectl get svc -n polardb |grep sfm-db 自行查看实际端口号 iii. 域名为：ps-sfm-db-employ-0.polardb.svc.cluster.local iv. 端口：见查询出的结果。 v. 用户名：polar_admin vi. 密码：{your_password}
5. 查看刚刚部署的pod。
智能体工厂 OpenTrek

```
#kubectl get pod -n polardb |grep sfm-db
#kubectl exec -it pi-sfm-db-employ-0-pg-0-0 -n polardb -- bash
#/u01/polardb_pg/bin/psql -h ps-sfm-db-employ-0.polardb.svc.cluster.local -p 61305 -U
polar_admin -d postgres
```

**租户区Pgvector**

**说明**

请严格按照规格部署，变更规格可能会引起产品部署资源不足，如需变更，请做好整体资源评估工作。
1. 准备yaml文件，yaml示例：

```
apiVersion: polardb.gitlab.alibaba-inc.com/v1 kind: LogicInstance metadata:
  name: pl-sfm-vector
  namespace: polardb
  labels:
    app.kubernetes.io/name: aistack-db-operator
    app.kubernetes.io/managed-by: kustomize
spec:
  insName: sfm-vector
  dbType: polarpg
  clusters:
    - clusterType: rw
      dbVersion: pg14
      engineType: pg
      visibility: inner
      cpus: 4
      memory: 16
      storageSize: 500
      creator: admin
      users:
        - userName: pgvector
          decodePassword: {your_password}
```

2. 执行 `kubectl apply -f xxxx.yaml` 命令。

**说明**

`xxxx.yaml` 请替换成实际yaml文件名。
3. 等待 PolarDB 命名空间下的 pod 就绪。
4. 此时的访问方式：
i. 地址：ps-sfm-vector-0.polardb.svc.cluster.local ii. 端口：kubectl get svc -n polardb |grep sfm-vector 自行查看实际端口号 iii. 用户名：pgvector iv. 密码：{your_password}
5. 查看刚刚部署的pod。
智能体工厂 OpenTrek

```bash
# kubectl exec -it pi-sfm-0-pg-0-0 -n polardb -- bash
# /u01/polardb_pg/bin/psql -h ps-sfm-vector-0.polardb.svc.cluster.local  -p 61311 -U
pgvector -d postgres
# select version();
```

**Redis（Orca）**

**管控区**

**说明**

请严格按照规格部署，变更规格可能会引起产品部署资源不足，如需变更，请做好整体资源评估工作。
1. 准备yaml文件，yaml示例：

```
apiVersion: polardb.gitlab.alibaba-inc.com/v1 kind: LogicInstance metadata:
  name: pl-sfm-redis
  namespace: polardb
  labels:
    app.kubernetes.io/name: aistack-db-operator
    app.kubernetes.io/managed-by: kustomize
spec:
  insName: sfm-redis
  dbType: polarorca
  clusters:
    - clusterType: rw
      dbVersion: orca
      engineType: orca
      visibility: inner
      cpus: 2
      memory: 4
      storageSize: 30
      creator: admin
      users:
        - userName: redis
          decodePassword: {your_password}
```

2. 执行 `kubectl apply -f xxxx.yaml` 命令。

**说明**

`xxxx.yaml` 请替换成实际yaml文件名。
3. 等待 PolarDB 命名空间下的 pod 就绪。
4. 此时的访问信息是：
i. 地址：ps-sfm-redis-0.polardb.svc.cluster.local ii. 端口：kubectl get svc -n polardb |grep sfm-redis 自行查看实际端口号 iii. 密码：redis:{your_password} （平台仅支持无用户名登录，需要将用户名拼接到密码中使用）需要特别注意。 智能体工厂 OpenTrek

**租户区**

**说明**

请严格按照规格部署，变更规格可能会引起产品部署资源不足，如需变更，请做好整体资源评估工作。
1. 准备yaml文件，yaml示例：

```
apiVersion: polardb.gitlab.alibaba-inc.com/v1 kind: LogicInstance metadata:
  name: pl-sfm-redis-employ
  namespace: polardb
  labels:
    app.kubernetes.io/name: aistack-db-operator
    app.kubernetes.io/managed-by: kustomize
spec:
  insName: sfm-redis-employ
  dbType: polarorca
  clusters:
    - clusterType: rw
      dbVersion: orca
      engineType: orca
      visibility: inner
      cpus: 2
      memory: 4
      storageSize: 30
      creator: admin
      users:
        - userName: redis
          decodePassword: {your_password}
```

2. 执行 `kubectl apply -f xxxx.yaml` 命令。

**说明**

`xxxx.yaml` 请替换成实际yaml文件名。
3. 等待 PolarDB 命名空间下的 pod 就绪。
4. 此时的访问信息是：
i. 地址：ps-sfm-redis-employ-0.polardb.svc.cluster.local ii. 端口：kubectl get svc -n polardb |grep sfm-redis 自行查看实际端口号 iii. 密码：redis:{your_password} （平台仅支持无用户名登录，需要将用户名拼接到密码中使用）需要特别注意。 智能体工厂 OpenTrek

**租户区ElasticSearch**

**说明**

请严格按照规格部署，变更规格可能会引起产品部署资源不足，如需变更，请做好整体资源评估工作。
1. 规格配置要求如下，部署时参数填写需要参考下表。

| 参数项 | 建议值 |
|---|---|
| MASTER CPU LIMIT _ _ | 4 |
| MASTER MEMORY LIMIT _ _ | 16Gi |
| MASTER ES JAVA OPTS _ _ _ | -Xms8g -Xmx8g |
| DATA CPU LIMIT _ _ | 4 |
| DATA MEMORY LIMIT _ _ | 32Gi |
| DATA ES JAVA OPTS _ _ _ | -Xms16g -Xmx16g |
| MASTER PV SIZE _ _ | 100Gi |
| DATA PV SIZE _ _ | 500Gi |

2. 部署ElasticSearch，具体操作，请参见《AI PaaS部署指南》。
记录部署参数ELASTIC_PASSWORD、KIBANA_PASSWORD、EXPORTER_PASSWORD，OpenTrek

##### 对象存储SDS-X

现场运维需要

**前提条件**

已部署SDS-X。 获取到SDS-X的登录用户名和密码，和登录地址。

**资源配置说明**

OpenTrek Agent Dev准备SDS-X相关资源时不需要创建用户。请直接复用部署 AI Studio 时创建的 aipaas-user 用户及其对应的 AK/SK 凭证。

**操作步骤**

1. 登录SDS-X控制台。
智能体工厂 OpenTrek
2. 分别创建如下2个bucket，配置拥有者为aipaas-user。
管控区：sfm-main 租户区：sfm-employee 智能体工厂 OpenTrek
3. 进入SDS-X站点页面，获取访问SDS-X的endpoint信息。endpoint为站点下目标对象路由的访问地址。
智能体工厂 OpenTrek
4. 进入aipaas-user用户页面，获取OpenTrek Agent Dev访问SDS-X的AK/SK信息。
5. 租户区角色 ARN信息：
直接使用aipaas-user用户的即可。
6. 记录下Endpoint、管控区Bucket、AK、SK，部署OpenTrek Agent Dev时，需要在部署页面填写。

#### CoWorker公钥和私钥生成

本章节介绍如何获取COWORKER_PRIVATE_KEY和COWORKER_PUBLIC_KEY。 智能体工厂 OpenTrek
1. 登录任一支持openssl命令的机器。
2. 执行以下命令获取私钥。

```
 openssl genpkey -algorithm RSA -out coworker_private.pem -pkeyopt
rsa_keygen_bits:2048
```

3. 执行以下命令获取公钥。

```
 openssl pkey -in coworker_private.pem -pubout -out coworker_public.pem
```

4. 使用如下命令提取私钥和公钥的字符串。

```
grep -v '^-----' coworker_private.pem | tr -d '\n' grep -v '^-----' coworker_public.pem | tr -d '\n'
```

### 常见问题

#### 部署天眼的常见问题

本章节介绍部署天眼过程中遇到的常见问题及其解决方案，包括PV状态异常、权限问题、日志采集故障和重装失败等情况的处理方法。

**存储**

**PV状态不对，无法bond**

问题描述：若此前已安装过天眼，PV的状态可能处于released状态。 解决方案：此类PV需要手动释放，即对每一个状态为 released 的 PV 执行对应释放命令。

```bash
kubectl patch pv tianyan-local-pv-1 -p '{"spec":{"claimRef": null}}' kubectl patch pv tianyan-local-pv-2 -p '{"spec":{"claimRef": null}}' kubectl patch pv tianyan-local-pv-3 -p '{"spec":{"claimRef": null}}' kubectl patch pv tianyan-local-pv-4 -p '{"spec":{"claimRef": null}}'
```

**PV存储bond成功，但是describe对应pod发现权限问题，无法创建目录**

问题描述：若此前已安装过天眼，产生过对应的应用数据，可能存在PV挂载目录错误的情况，例如prom 的挂载到了之前jaeger的目录下。 解决方案：删除对应PV目录，使用deploy.py脚本重新创建PV。 智能体工厂 OpenTrek
# --pv-node表示部署的节点
# --pv-path表示天眼数据存储的路径
# --storage-class-type 表示存储方式

```
python3 deploy.py \
  --from-secret \
  --deploy-pv \
  --pv-node node-1 \
  --pv-remote \
  --pv-path /data/tianyan/ \
  --package-path /apsarapangu/disk9/e2e/xxxxx \
  --storage-class-type default
python3 deploy.py \
  --from-secret \
  --package-path <path> \
  --storage-class-type alicloud
```

**vector采集不到日志**

问题描述：在某些 Kubernetes 集群环境中，节点上的容器日志目录被配置为指向实际存储路径的符号链接（软链接），导致vector读取不到。 解决方案：请执行以下语句进行修复。 智能体工厂 OpenTrek
# 新增额外的挂载

```json
kubectl patch daemonset tianyan-vector -n monitoring --type='json' -p='[
  {
    "op": "add",
    "path": "/spec/template/spec/volumes/-",
    "value": {
      "name": "containerd-logs",
      "hostPath": {
        "path": "/var/lib/containerd/container_logs",
        "type": "DirectoryOrCreate"
      }
    }
  },
  {
    "op": "add",
    "path": "/spec/template/spec/containers/0/volumeMounts/-",
    "value": {
      "name": "containerd-logs",
      "mountPath": "/var/lib/containerd/container_logs",
      "readOnly": true
    }
  }
```

`]'`

```bash
# rollout
kubectl rollout restart daemonset tianyan-vector -n monitoring
```

**安装天眼失败后重装的处理建议**

**说明**

若您需要重装天眼，请先卸载再重新部署，以避免残留配置项导致冲突。

**清理范围**

| 清理项 | 基础清理 | 完全清理 |  |  |
|---|---|---|---|---|
| Helm Release | 存储类型为alicloud模式时，会卸载 tianyan-* 前缀的所有 helm release。 |  |  |  |
| Namespace | 存储类型为alicloud模式时，会删除部署 namespace（级联删除 Pod/PVC/Secret/Service）。 |  |  |  |
| PV（PersistentVolume） | 存储类型为default模式时，会删除标签为 tianyan- purpose=tianyan-storage 的 PV。 |  |  |  |
|  |  |  | tianyan- |  |
| 临时文件 | 删除 deploy.py 生成的临时文件。 |  |  |  |

|  | purpose=tianyan-storage |
|---|---|

智能体工厂 OpenTrek

| StorageClass | 保留。 | 存储类型为default模式时， 会删除StorageClass。 |
|---|---|---|
| CRD（Custom Resource Definition） | 保留。 | 删除CRD。 |
| 节点标签（Node Labels） | 保留。 | 存储类型为default模式时， 会删除节点标签。 |
| HostPath 磁盘数据 | 保留。 | 存储类型为default模式时， 会删除节点磁盘上 PV 对应的实际数据目录。 |

**操作步骤**

基础清理。
# 交互确认后清理

```
python3 tools/clean_deploy.py
```

# 跳过确认直接执行

```
python3 tools/clean_deploy.py --yes
```

# 仅预览将要执行的命令

```
python3 tools/clean_deploy.py --dry-ru
```

完整清理。 完整清理会还原环境至初始状态。适用于需要从零开始重建的场景。

```
python3 tools/clean_deploy.py \
  --yes \
  --delete-storageclass \
  --delete-crds \
  --clean-node-labels \
  --clean-host-paths \
  --wait
```

**其他**

**vector的pod中deleted 文件堆积占满磁盘**

问题描述：tianyan-vector 通过 hostPath 扫描 /var/log/pods 下的 Pod 日志文件，打开后持有文件句柄。当 kubelet 轮转删除旧日志时，vector 没有及时释放句柄，导致 deleted 文件堆积占满磁盘。 解决方案： 智能体工厂 OpenTrek
# 1. 备份

```bash
kubectl get cm tianyan-vector -n monitoring -o yaml > tianyan-vector-cm-backup.yaml
# 2. 编辑，在 kube_logs 下加 rotate_wait_secs: 300
kubectl edit cm tianyan-vector -n monitoring
```

# 简单示例如下

```
sources:
  kube_logs:
    type: kubernetes_logs
    rotate_wait_secs: 300
```

# 3. 滚动重启生效（改 `ConfigMap` 不会自动触发滚动）

```bash
kubectl -n monitoring rollout restart ds tianyan-vector kubectl -n monitoring rollout status ds tianyan-vector
```

# 4. 验证配置已生效

```bash
POD=$(kubectl -n monitoring get pod -l app.kubernetes.io/name=vector -o jsonpath='{.items[0].metadata.name}') kubectl -n monitoring exec $POD -- cat /etc/vector/vector.yaml | grep rotate_wait_secs
```
