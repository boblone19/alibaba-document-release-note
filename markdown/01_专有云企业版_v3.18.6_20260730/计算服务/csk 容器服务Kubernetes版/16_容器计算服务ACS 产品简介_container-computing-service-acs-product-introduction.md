---
title: "容器服务Kubernetes版 容器计算服务ACS 产品简介"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 15
source_pdf: "16_容器计算服务ACS 产品简介_container-computing-service-acs-product-introduction.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/csk/zh/container-computing-service-acs-product-introduction.pdf"
converter: line-classifier (PyMuPDF)
---

# 容器服务Kubernetes版 容器计算服务ACS 产品简介

容器服务Kubernetes版 CS

## 什么是容器计算服务 ACS

容器计算服务 ACS是面向专有云环境的Serverless容器算力服务，用于以Pod为算力单元提供GPU容器计算资源，无需管理节点即可运行容器化工作负载。

**背景与挑战**

随着企业数字化转型深入推进，越来越多的组织在专有云环境中部署容器化应用和AI工作负载。传统容器服务要求用户预先规划节点容量、管理虚拟机生命周期、处理操作系统升级和集群组件维护，运维复杂度高。 在AI Agent场景中，应用对安全隔离和弹性速度提出了更高要求——Agent运行时需要执行不可信代码，需要严格的安全沙箱隔离；模型动态控制工具执行会产生大规模秒级弹性并发，传统节点级扩容方式难以满足。同时，GPU算力在多租户环境下的规格化切分和按需分配也缺乏有效手段。

**产品概述**

容器计算服务 ACS是基于Kubernetes的Serverless容器计算服务，面向专有云环境提供GPU容器算力。 ACS以Pod作为算力交付单元，用户无需进行容量规划和节点运维，直接提交Pod即可获得容器算力资源。 产品支持GPU型和高性能网络GPU型等实例类型，GPU Pod最小支持1卡GPU。ACS默认采用安全沙箱技术实现Pod级别的强隔离，每个Pod运行在独立内核中，不存在资源争抢。弹性方面，ACS支持秒级Pod级弹性伸缩，适配突发流量和AI推理等场景。产品兼容标准Kubernetes API，支持kubectl连接和YAML部署， 同时兼容E2B等AI Agent生态协议，为Agent应用提供安全沙箱运行环境。

**核心功能列表**

**Serverless****容器算力**：以Pod为算力交付单元，无需节点运维和容量规划，支持GPU型实例类型，按量
秒级计费。
**安全沙箱隔离**：基于轻量级安全沙箱技术，每个Pod运行在独立内核中，实现计算、网络、存储多维度的
强隔离。
**秒级弹性伸缩**：支持Pod维度的秒级弹性伸缩，集成HPA和AHPA预测伸缩策略，适配突发流量场景。
**GPU****容器算力**：支持多种GPU卡型，面向AI训练推理和异构计算场景，提供灵活的vCPU/内存/GPU配
比。
**Kubernetes****生态兼容**：兼容标准Kubernetes API，支持kubectl、YAML部署，集成Prometheus监
控和SLS日志采集。 容器服务Kubernetes版

## 产品详情

容器计算服务 ACS基于Serverless架构提供容器算力服务，按照“集群创建→算力声明→调度交付→运行管理”的工作流程交付容器资源。本文主要介绍容器计算服务 ACS的工作原理、核心功能与技术特性。

**工作原理**

ACS采用控制面全托管的Serverless Kubernetes架构，将传统Kubernetes中用户需要自行管理的节点层抽象为平台侧的算力资源池。用户通过kubectl命令行或控制台创建ACS集群后，直接以Pod为单位提交工作负载，系统自动匹配底层计算资源完成调度交付，整个过程无需用户介入节点规划和管理。 在**集群**层面，ACS提供全托管的Kubernetes控制面，包括API Server、etcd、调度器等核心组件均由平台侧运维管理。ACS仅发布Kubernetes社区双数版本号，每个Minor版本提供两年的维保周期。集群创建时，用户选择Region和可用区，系统自动完成控制面部署和算力资源池初始化。 在**算力交付**层面，ACS将底层计算资源抽象为标准化的容器算力规格。GPU Pod支持多种GPU卡型，最小支持1卡GPU，vCPU从2核起，内存从2 GiB起。用户通过标准Kubernetes YAML声明工作负载类型、实例类型和资源规格，ACS的调度系统根据资源申请自动匹配底层算力资源，完成Pod的调度和启动。 在**安全隔离**层面，ACS默认采用安全沙箱技术，每个Pod运行在独立的内核承载环境中，与其他Pod不存在资源争抢，实现虚机级别的安全隔离。Pod在调度时尽可能分布在不同的物理机上，进一步保障高可用性。安全沙箱同时支持Pause/Resume状态保持能力，可在1至30秒内完成休眠和唤醒操作。 在**应用管理**层面，ACS支持Deployment、StatefulSet、Job、CronJob等标准Kubernetes工作负载类型，提供HPA和AHPA预测伸缩策略。存储方面基于CSI对接云盘、OSS和NAS文件存储。网络方面集成 Terway容器网络，Pod使用独立IP地址，支持LoadBalancer Service、ClusterIP Service和EIP挂载。 在**运维**层面，ACS默认集成Prometheus监控、SLS日志采集和事件报警，提供集群巡检、故障诊断及 API Server审计功能。计费方面以Pod实例为单位按量付费，按秒计费按小时出账，集群管理不收取费用。

**核心能力**

**Serverless Kubernetes架构**

提供全托管的Kubernetes控制面，用户无需管理底层节点与集群组件。Pod直接作为算力单元提交，系统自动匹配底层资源，实现“Pod即实例”的交付模式。支持标准Kubernetes API，可通过kubectl和 kubeconfig连接管理集群，兼容现有的Kubernetes工具链和工作流。

**多类型容器算力**

支持GPU型和高性能网络GPU型等实例类型。GPU型面向AI推理和异构计算场景；高性能网络GPU型提供高带宽RDMA网络互联，适用于GPU分布式训练。每种实例类型提供灵活的vCPU/内存/GPU配比，支持细粒度资源规格。

**安全沙箱隔离**

基于轻量级安全沙箱技术，每个Pod实例通过独立内核承载实现强隔离，实例间互不影响。支持计算隔离、 网络隔离（Terway NetworkPolicy）、存储隔离和鉴权隔离（Kubernetes RBAC）。安全沙箱同时支持状态保持能力，包括休眠、唤醒、Checkpoint和Commit操作，适用于Agent沙箱等需要状态持久化的场景。

**秒级弹性伸缩**

支持Pod维度的秒级弹性伸缩，无需等待节点扩容。集成HPA水平自动伸缩和AHPA预测伸缩策略，支持基于KEDA的事件驱动弹性伸缩。Pod与算力1:1对应，工作负载缩容时自动释放对应算力并停止计费，无需用户干预。

**GPU异构计算**

容器服务Kubernetes版支持多种GPU卡型，覆盖大模型训练、推理和通用AI任务。通过Kubernetes标签指定GPU实例类型，使用标准YAML部署。支持多GPU卡配置和NVLink/P2P通信，提供GPU Pod容量预留功能保障工作负载容量确定性。集成Prometheus监控GPU Pod指标，支持GPU Pod调度失败等问题诊断。

**管理工具**

ACS提供控制台和命令行两种管理方式。 控制台支持集群创建与管理、工作负载部署与监控、弹性策略配置和资源用量查看。 命令行支持通过kubectl连接集群，使用标准Kubernetes命令管理资源。 运维侧提供ACS管控集群和super集群的管理能力，包括组件管理、版本升级、资源监控、日志管理和操作记录等功能。 容器服务Kubernetes版

## 产品价值

容器计算服务 ACS通过Serverless架构简化专有云容器算力的交付与运维，为用户提供免规划、免运维、 高弹性的容器运行环境。本文主要介绍容器计算服务 ACS的核心产品价值。

**免节点运维**

控制面全托管，用户无需管理节点、规划容量或维护集群组件。Pod直接提交即可获得算力，节点运维由平台侧负责，降低运维复杂度。

**安全沙箱隔离**

每个Pod运行在独立内核中，实现虚机级别的安全隔离。适用于Agent代码执行、多租户共享算力等需要强隔离的场景，防止代码逃逸和数据泄露。

**秒级弹性伸缩**

Pod维度秒级弹性扩容，无需等待节点创建。支持HPA、AHPA预测伸缩和KEDA事件驱动弹性，适配突发流量和AI推理等弹性场景。

**细粒度资源规格**

GPU Pod最小支持1卡。按量秒级计费，资源规格与业务负载匹配，减少资源浪费。

**GPU算力按需供给**

支持多种GPU卡型，覆盖AI训练、推理和异构计算场景。提供GPU Pod容量预留和多卡通信支持，满足从单卡推理到分布式训练的不同需求。

**Kubernetes生态兼容**

兼容标准Kubernetes API，支持kubectl、YAML部署和主流K8s工具链。集成Prometheus监控、SLS日志采集和故障诊断能力。

**成本优化**

集群管理免费，仅对Pod资源按量计费。Pod与工作负载1:1对应，缩容时自动释放算力停止计费，避免节点闲置成本。 容器服务Kubernetes版

## 功能特性

容器计算服务 ACS覆盖Serverless Kubernetes架构、容器算力定义、集群管理、应用管理、运维安全和 GPU调度等功能模块。具体功能及详细说明如下： 具体功能及详细说明如下：

**Serverless Kubernetes架构**

| 功能点 | 详细说明 |
|---|---|
| 托管控制面 | 提供全托管的Kubernetes控制面，用户无需管理底层节点与集群。 |
| 算力交付 | Pod直接作为算力单元提交，系统自动匹配底层资源，实现“Pod即实例”，无需节点运维。 |
| 原生Kubernetes兼容 | 支持标准Kubernetes API，可通过kubectl和 kubeconfig连接管理集群。 |

**算力类型与资源模型**

| 功能点 | 详细说明 |
|---|---|
| 实例类型 | 支持GPU型（gpu）、高性能网络GPU型（gpu-hpn） 等Pod实例类型。 |
| 算力质量 | 每种实例类型提供default（稳定保障）算力质量。 |

**GPU卡型与规格**

| 功能点 | 详细说明 |
|---|---|
| 支持多种GPU卡型 | 包括 APG1.5等主流GPU卡 ，覆盖大模型训练/推理、通用AI任务等场景，覆盖大模型训练/推理、通用AI任务等场景。 |
| 灵活资源配置 | GPU Pod最小支持1卡；vCPU从2核起，内存从2 GiB 起，存储30~6144 GiB；部分规格内存支持1 GiB步长调整。 |

**资源管理**

| 功能点 | 详细说明 |
|---|---|

容器服务Kubernetes版

| 按需弹性 | 秒级弹性伸缩，Pod维度vCPU/内存/GPU资源使用量进行计量计费。 |
|---|---|

**集群管理**

| 功能点 | 详细说明 |
|---|---|
| 集群创建 | 通过YAML或控制台一键创建，无需运维节点。 |
| 授权管理 | 支持阿里云RAM授权与Kubernetes RBAC双重权限控制。 |
| 调度管理 | 兼容原生Kubernetes调度能力，支持异构资源与弹性资源的精细化调度。 |
| K8s版本 | 支持Kubernetes社区双数版本，每个Minor版本提供两年维保周期。 支持K8s 1.32版本集群。 |

**应用管理**

| 功能点 | 详细说明 |
|---|---|
| 工作负载支持 | 支持无状态（Deployment）、有状态 （StatefulSet）、任务（Job）、定时任务（CronJob） 等工作负载。 |
| 弹性伸缩策略 | 支持手动伸缩、HPA及AHPA预测伸缩。 |
| 存储集成 | 基于CSI对接阿里云存储。 |
| 网络集成 | 集成Terway容器网络、VPC与SLB，Pod使用独立IP地址，支持LoadBalancer Service和ClusterIP Service，提供高性能容器网络。 |

**运维与安全**

| 功能点 | 详细说明 |
|---|---|
| 故障诊断 | 提供集群巡检、故障诊断及API Server审计功能。 |

**GPU调度与部署**

容器服务Kubernetes版

| 功能点 | 详细说明 |
|---|---|
| Kubernetes原生兼容 | 通过 alibabacloud.com/compute-class: gpu 或 gpu-hpn 标签指定GPU实例类型，使用标准 YAML部署。 |

|  |  | alibabacloud.com/compute-class: |
|---|---|---|
| 生兼容 | gpu |  |

**可观测与运维**

| 功能点 | 详细说明 |
|---|---|
| 监控与日志 | 集成Prometheus监控GPU Pod指标，通过SLS采集 GPU应用日志。 |
| 故障诊断 | 提供Pod级一键诊断，支持GPU Pod调度失败 （Pending）等问题排查。 |

容器服务Kubernetes版

## 应用场景

容器计算服务 ACS适用于专有云环境中的容器化应用部署、AI工作负载运行和弹性业务场景。本文主要介绍容器计算服务 ACS的应用场景。

**GPU AI训练与推理**

面向AI训练和推理场景，ACS提供GPU型和高性能网络GPU型Pod实例，支持多种GPU卡型和多卡 NVLink/P2P通信。通过GPU Pod容量预留功能保障关键工作负载的算力确定性，支持GPU分布式训练和大规模推理任务。 场景特点： 支持多种GPU卡型，覆盖训练和推理不同需求。 高性能网络GPU型提供RDMA网络互联，适用于分布式训练场景。 GPU Pod容量预留保障关键任务算力确定性。

**突发弹性业务**

为应对突发流量场景（如在线业务、金融交易），ACS提供秒级Pod弹性扩容能力，无需等待节点创建。可作为ACK集群的临时弹性资源池，通过虚拟节点实现跨产品统一调度，在突发场景下快速补充算力资源。 场景特点： Pod维度秒级弹性扩容，无需节点扩缩容等待。 支持HPA和AHPA预测伸缩策略，自动适配流量波动。 缩容时自动释放算力并停止计费，按需使用。

**多租户混部与集中运维**

在集团云或行业运营云中，ACS支持多业务负载混部调度，通过Kubernetes资源隔离策略保障多租户安全。集中化运维模式降低租户自运维成本，负载混合部署提升物理资源利用率。 场景特点： 支持GPU混合任务的统一调度与隔离。 基于Namespace和RBAC实现多租户权限隔离。 控制面全托管，租户侧获得免运维体验。

**离线批处理任务**

面向成本敏感、具有容错能力的离线计算任务。在资源库存不足时实例会被抢占和驱逐，驱逐前提供事件通知，适用于大数据计算、日志处理等无状态离线工作负载。 场景特点： 支持Job和CronJob工作负载类型。 缩容时自动释放资源，按实际使用时长计费。 容器服务Kubernetes版

## 使用限制

容器计算服务 ACS对部分功能和使用范围进行了约束，请在使用前了解以下限制项。 具体的限制项和限制值请参见下表。

| 限制项 | 限制值 | 说明 |
|---|---|---|
| 不支持DaemonSet | 不支持 | ACS为Serverless架构，无节点概念，不支持DaemonSet工作负载。 |
| 不支持HostPath | 不支持 | 用户无法访问宿主机文件系统。 |
| 不支持HostNetwork | 不支持 | Pod无法使用宿主机网络命名空间。 |
| 不支持Privileged容器 | 不支持 | Pod无法以特权模式运行，安全沙箱环境下不支持特权容器。 |
| 不支持NodePort Service | 不支持 | ACS使用Terway网络模式，不支持 NodePort类型的Service。 |
| 不支持Session Affinity | 不支持 | Service不支持基于Session的亲和性配置。 |
| CPU Pod最大规格 | 64 vCPU / 512 GiB | CPU Pod的最大资源规格上限。 |
| GPU Pod最大GPU卡数 | 8卡 | 单个GPU Pod最多支持8张GPU卡。 |
| K8s版本策略 | 社区双数版本 | ACS仅发布Minor版本号为双数的 K8s版本，每个版本提供两年维保周期。 |

容器服务Kubernetes版

## 基本概念

本文主要对容器计算服务 ACS涉及的专有名词及术语进行定义和解析，方便您更好地理解相关概念并使用容器计算服务 ACS。 面向专有云环境的Serverless容器计算服务，以Pod为算力交付单元，提供GPU容器算力，用户无需管理底层节点即可运行容器化工作负载。

**Serverless Kubernetes**

一种Kubernetes服务模式，控制面由平台全托管，用户直接提交Pod获得算力，无需管理Worker节点。容器计算服务 ACS即为Serverless Kubernetes的实现，提供标准化的K8s使用体验。

**Pod**

Kubernetes中最小的可部署计算单元，包含一个或多个容器。在ACS中，Pod同时作为算力交付单元，用户通过声明Pod的资源规格来获得对应的容器算力。

**安全沙箱**

基于轻量级虚拟化技术实现的容器隔离机制，每个Pod运行在独立内核中，与其他Pod不存在资源争抢，实现虚机级别的安全隔离，防止代码逃逸。

**算力质量**

定义Pod实例资源保障等级和稳定性特性的分类机制。ACS提供default（稳定保障）算力质量类型。

**实例类型**

ACS Pod的计算类型分类，包括通用型、GPU型和高性能网络GPU型等。不同实例类型对应不同的底层硬件资源和适用场景。

**vCPU**

虚拟CPU，是容器算力中CPU资源的计量单位。ACS Pod的vCPU规格支持0.25核起步，步长0.5核， 用户可按需声明CPU资源请求。

**GPU Pod**

配置了GPU资源的ACS Pod实例，用于AI训练、推理等异构计算场景。GPU Pod通过Kubernetes标签指定GPU实例类型，支持单卡和多卡配置。

**HPA**

Horizontal Pod Autoscaler的缩写，即Pod水平自动伸缩。根据CPU/内存等指标自动调整Pod副本数量，实现工作负载的自动弹性伸缩。

**AHPA**

Advanced Horizontal Pod Autoscaler的缩写，即高级预测弹性伸缩。基于历史数据和预测模型提前扩容，减少弹性滞后，适配可预测的流量波动场景。

**KEDA**

Kubernetes Event-Driven Autoscaling的缩写，基于Kafka、RabbitMQ、MySQL等事件源的度量指标触发工作负载弹性伸缩，适用于事件驱动的离线任务场景。

**Terway**

ACS默认集成的容器网络插件，为每个Pod分配独立的Pod IP地址，占用交换机vSwitch的一个弹性网卡，支持Pod间直接互联互通。

**CSI**

容器服务Kubernetes版 Container Storage Interface的缩写，是Kubernetes标准存储接口规范。ACS基于CSI对接云盘、 OSS和NAS等持久化存储类型。

**E2B**

一种面向AI Agent的沙箱生态协议，定义了Agent沙箱的创建、连接、执行和回收等标准接口。ACS提供与E2B兼容的接入方式，降低Agent应用迁移成本。

**Checkpoint**

对运行中Pod的内存和状态进行快照的操作，生成的快照可用于后续的克隆或恢复。在Agent沙箱场景中，Checkpoint用于保存Agent执行上下文。

**Pod容量预留**

按指定Pod规格预先预留算力资源数量的机制，保障工作负载的容量确定性。GPU场景下支持Pod级别和Node级别两种容量预留方式。

**RDMA**

Remote Direct Memory Access的缩写，即远程直接内存访问。高性能网络GPU型实例提供RDMA 网络互联能力，适用于GPU分布式训练等需要高带宽低延迟通信的场景。

**NVLink**

NVIDIA开发的高速GPU互联技术，支持多张GPU之间的高带宽直接通信。ACS部分GPU卡型支持 NVLink，用于提升分布式训练效率。

**SLS**

阿里云日志服务（Simple Log Service），ACS默认集成SLS进行日志采集，支持容器标准输出和业务日志的收集、查询和分析。
