---
title: "云服务器 ECS 实例规格族&实例规格简介"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 51
source_pdf: "13_实例规格族&实例规格简介_instance-family-and-instance-types.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/ecs/zh/instance-family-and-instance-types.pdf"
converter: line-classifier (PyMuPDF)
---

# 云服务器 ECS 实例规格族&实例规格简介

云服务器ECS 实例规格

## 实例规格族&实例规格

根据业务场景和使用场景，阿里云将ECS实例分为多个实例规格族，如共享型、独享型、弹性裸金属、本地 HDD盘、本地SSD盘、异构计算型、超级计算集群等，每个规格族是一个或多个具有相似属性的实例规格的组合。

**实例规格族类型**

实例规格族类型及应用场景如下表所示：

| 实例规格族 | 应用场景 |
|---|---|
| 共享型 | 适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序、开发环境、构建服务器、代码存储库、微服务、测试和暂存环境、轻量级数据库、轻量级企业应用、综合应用服务等。 |
| 独享型 | 适合对虚拟机性能要求较高的业务场景，如高网络包收发场景、Web前端服务器、数据分析、 批量计算、视频编码、高性能科学和工程应用等。 |
| 弹性裸金属 | 提供强劲的计算、存储以及网络配置，满足对资源独享、安全隔离、性能有较高要求的业务场景，如容器、数据库、企业核心业务、大数据计算等。 |
| 本地HDD盘 | 适用于有大数据计算与存储分析需求的业务场景，如海量数据存储和离线计算，满足以 Hadoop为代表的分布式计算业务对实例存储性能、存储容量和内网带宽的多方面要求。 |
| 本地SSD盘 | 用于满足I/O密集型应用对块存储的低时延和高I/O性能需求，如NoSQL非关系型数据库 （Cassandra、MongoDB等）、MPP数据仓库和分布式文件系统、ElasticSearch等搜索场景等。 |
| 异构计算型 | 搭配各类加速器，如NVIDIA T4、NVIDIA V100、FPGA等，适用于AI推理、计算机视觉、语音识别/合成、机器翻译、推荐系统、实时渲染、深度学习、科学计算等业务场景。 |
| 超级计算集群 | 在弹性裸金属实例的基础上，搭配高速InfiniBand（IB）网络，提供具有极致计算性能和并行效率的计算集群服务，适合搭建高性能计算、人工智能/机器学习、科学/工程计算、数据分析、音视频处理等应用。 |
| 突发型 | vCPU持续提供基准性能，可突然提速，但受到CPU积分的限制，适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序。 |
| 网络增强型 | 针对网络密集型应用场景专门优化，各项网络指标得到提升，远高于同代通用实例规格，满足垂直场景需求。特别适用于需要网络性能高于通用实例的场景。 |
| 存储增强型 | 相比于同代系实例，在云盘带宽、云盘IOPS等EBS相关能力上进行了优化，更适用于存储密集型应用场景。 |
| 可信计算型 | 可信计算型实例通过使用UEFI安全固件、虚拟可信平台模块（vTPM/vTCM）、远程证明服务，实现实例启动度量和完整性校验，从而保障实例的安全可信。 |

云服务器ECS 实例规格

**实例规格**

同一个实例规格族里，根据vCPU和内存的配置不同，分为多个不同的实例规格。ECS实例规格定义了实例的具体属性：vCPU数量、内存大小、网络能力（如VPC带宽、PPS大小、弹性网卡数量、每个弹性网卡支持的IP数量等）与存储能力（云盘带宽峰值、云盘IOPS峰值、云盘数量等），同一个实例规格族中，实例的网络性能、存储性能与计算规格对应（规格越高网络性能越强）。 ECS实例规格命名规范如下图所示： ECS实例规格命名规则说明如下： 产品名称：以ecs.开头，表示ECS产品。 规格族：如s6-k，s代表共享型实例，6代表阿里云六代机型，k代表KVM虚拟化；如g6x-k10，g代表是独享型实例，6代表是阿里云六代机型，x代表是高密机型（整机128逻辑核），k10代表是KVM机型搭配 10 GB网络。 资源配比：如c1m2，代表计算内存比为1:2，如2 vCPU 4 GiB、4 vCPU 8 GiB等。 规格大小：large代表2 vCPU，xlarge代表4 vCPU，2xlarge代表8 vCPU，3xlarge代表12 vCPU。 在下列的Intel规格族、Hygon规格族、Kunpeng规格族和Feiteng规格族章节中，表格各列的含义如下： 规格族：实例规格族名字。 处理器：规格族支持和建议使用的处理器型号，如Intel V6代表Intel Cascade Lake处理器。 虚拟化：使用的虚拟化技术，分为KVM、一代神龙架构、二代神龙架构、三代神龙架构。 物理机线程数：宿主机超线程（X86架构）或逻辑核（ARM架构）的数量（用vCPU表示）。在相同的网络环境下，如果物理机的vCPU数量不一样，那么单vCPU能获得的网络能力是有差异的，最新非共享规格族会尽量区分开来，以提供更好的QoS。不限代表不区分物理机vCPU的数量。 网络：宿主机的网络配置。相同的物理机，在不同的网络配置下，单vCPU能获得的网络能力是有差异的，最新非共享规格族会尽量区分开来，以提供更好的QoS。10 G代表是2*10 Gbps网络条件下用的规格族，25 G代表是2*25 Gbps网络条件下用的规格族，不限代表不区分网络配置。 规格族描述：描述了此规格族下的实例规格的一些特性，如规格大小、计算内存比、配置了什么样的加速卡和磁盘等等。

**资源分配**

不同类型的ECS实例在资源分配上有所不同，具体说明如下： 所有的KVM机型，需要为虚拟化预留部分CPU与内存资源，如预留8 vCPU 32 GiB、10 vCPU 40 GiB或 10 vCPU 48 GiB，以承载网络虚拟化、存储虚拟化和管控方面的任务。 所有的神龙架构机型，无需在服务器侧预留CPU与内存资源。神龙架构采用软硬一体设计，可以将网络虚拟化、存储虚拟化以及系统管控全部卸载到专用芯片系统，除了实现资源零开销，还可以避免底层资源争抢而导致的虚拟机性能波动。 云服务器ECS 实例规格宿主机的内存资源、本地盘资源都是不可超分的。 在生产共享型实例和突发型实例时，宿主机的CPU资源是可以超分的，建议您控制超分比不要超过4。在生产其他类型实例时，宿主机的CPU资源都是不可超分的。

**自定义规格限制**

部分规格类型在使用中有所限制，以下类型暂不支持自定义规格： CPU Credit规格 NUMA ON规格裸金属规格 vGPU规格 SCC规格云服务器ECS

## Intel规格族

### 共享型

共享型实例适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序、开发环境、构建服务器、代码存储库、微服务、测试和暂存环境、轻量级数据库、轻量级企业应用、综合应用服务等。本文介绍了共享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.s9-k | Intel V9 | KVM | 96 vCPU、128 vCPU、192 vCPU、256 vCPU | 10 G、 25 G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.s8-k | Intel V8 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.s6-k | Intel V6 | KVM | 64 vCPU、72 vCPU、80 vCPU、96 vCPU、104 vCPU | 10 G、 25 G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.s6-m | Intel V6 | 二代神龙架构 | 64 vCPU、96 vCPU、104 vCPU | 10 G、 25 G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.s7-k | Intel V7 | KVM | 64 vCPU、80 vCPU、96 vCPU、104 vCPU、128 vCPU、144 vCPU、152 vCPU、192 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS

| ecs.anysha re | Intel | KVM | 40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU、104 vCPU、128 vCPU | 10 G、 25 G | 支持通过Apsara Uni- manager运维控制台创建、修改和删除自定义实例规格自定义的实例规格均为共享型，仅支持Intel处理器 |
|---|---|---|---|---|---|
| ecs.xn4 | Intel V4/V5/V6 | KVM | 32 vCPU、40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 仅支持ecs.xn4.small，1 vCPU 1 GiB |
| ecs.n4 | Intel V4/V5/V6 | KVM | 32 vCPU、40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：1、 2、4、8、16、32 计算内存比：1:2 |
| ecs.mn4 | Intel V4/V5/V6 | KVM | 32 vCPU、40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：1、 2、4、8、16、32 计算内存比：1:4 |
| ecs.e4 | Intel V4/V5/V6 | KVM | 32 vCPU、40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：1、 2、4、8、16 计算内存比：1:8 |

云服务器ECS

| ecs.xn4v2 | Intel V4/V5/V6 | KVM | 40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | ecs.xn4.small，1 vCPU 1 GiB 支持IPv6地址 |
|---|---|---|---|---|---|
| ecs.n4v2 | Intel V4/V5/V6 | KVM | 40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU） ：1、 2、4、8、16、32 计算内存比：1:2 支持IPv6地址 |
| ecs.mn4v2 | Intel V4/V5/V6 | KVM | 40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：1、 2、4、8、16、32 计算内存比：1:4 支持IPv6地址 |
| ecs.e4v2 | Intel V4/V5/V6 | KVM | 40 vCPU、48 vCPU、64 vCPU、56 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：1、 2、4、8、16 计算内存比：1:8 支持IPv6地址 |

### 独享型

独享型实例适合对虚拟机性能要求较高的业务场景，如高网络包收发场景、Web前端服务器、数据分析、批量计算、视频编码、高性能科学和工程应用等。本文介绍了独享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.g9m- k10 | Intel V9 | KVM | 96 vCPU | 10 G | 支持ENI Trunking 规格大小（vCPU）： 2、 4、8、12、16、24、32、 40、48、56、64、72、 80、86 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS

| ecs.g9m- k25 | Intel V9 | KVM | 96 vCPU | 25 G | 支持ENI Trunking 规格大小（vCPU）： 2、 4、8、12、16、24、32、 40、48、56、64、72、 80、86 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g9x- k10 | Intel V9 | KVM | 128 vCPU | 10 G | 支持ENI Trunking 规格大小（vCPU）： 2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g9x- k25 | Intel V9 | KVM | 128 vCPU | 25 G | 支持ENI Trunking 规格大小（vCPU）： 2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g9v- k10 | Intel V9 | KVM | 192 vCPU | 10 G | 支持ENI Trunking 规格大小（vCPU）： 2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、128、 160、178 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g9v- k25 | Intel V9 | KVM | 192 vCPU | 25 G | 支持ENI Trunking 规格大小（vCPU）： 2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、128、 160、178 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS

| ecs.g9h- k10 | Intel V9 | KVM | 256 vCPU | 10 G | 支持ENI Trunking 规格大小（vCPU）： 2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、128、 160、192、224、242 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g9h- k25 | Intel V9 | KVM | 256 vCPU | 25 G | 支持ENI Trunking 规格大小（vCPU）： 2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、128、 160、192、224、242 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8x- k25 | Intel V8 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8x- k10 | Intel V8 | KVM | 128 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8s- k10 | Intel V8 | KVM | 64 vCPU | 10 G | 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8s- k25 | Intel V8 | KVM | 64 vCPU | 25 G | 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8m- k10 | Intel V8 | KVM | 96 vCPU | 10 G | 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8m- k25 | Intel V8 | KVM | 96 vCPU | 25 G | 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7x- x25 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 规格大小（vCPU）：2、4、 8、12、16、24、32、48、 64、128 |

云服务器ECS

| ecs.g7s- k10 | Intel V7 | KVM | 64 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、54 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g7s- k25 | Intel V7 | KVM | 64 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、54 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7m- k10 | Intel V7 | KVM | 96 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、86 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7m- k25 | Intel V7 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、86 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7x- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7x- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7v- k10 | Intel V7 | KVM | 192 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS

| ecs.g7v- k25 | Intel V7 | KVM | 192 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g6s- m10 | Intel V6 | 二代神龙架构 | 64 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6s- m25 | Intel V6 | 二代神龙架构 | 64 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6m- m10 | Intel V6 | 二代神龙架构 | 96 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6m- m25 | Intel V6 | 二代神龙架构 | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88、96 计算内存比 1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6s- k10 | Intel V6 | KVM | 64 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6s- k25 | Intel V6 | KVM | 64 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS

| ecs.g6m- k10 | Intel V6 | KVM | 96 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g6m- k25 | Intel V6 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64、72、 80、88 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.c6 | Intel V6 | 二代神龙架构 | 104 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 52、64、104 计算内存比 1:2 |
| ecs.g6 | Intel V6 | 二代神龙架构 | 104 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 52、64、104 计算内存比：1:4 |
| ecs.r6 | Intel V6 | 二代神龙架构 | 104 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 52、64、104 计算内存比：1:8 |
| ecs.re6 | Intel V6 | 二代神龙架构 | 208 vCPU | 10 G、 25 G | 整机配置3 TB内存，计算内存比约为1:15 |
| ecs.sn1 | Intel V5/V6 | KVM | 48 vCPU、64 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、 4、8、16、32、56 计算内存比：1:2 |
| ecs.sn2 | Intel V5/V6 | KVM | 48 vCPU、64 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、 4、8、16、32、56 计算内存比：1:4 |
| ecs.se1 | Intel V5/V6 | KVM | 40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、 4、8、16、32、56 计算内存比：1:8 |

云服务器ECS

| ecs.sn1ne | Intel V5/V6 | KVM | 40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 88 计算内存比：1:2 支持IPv6地址 |
|---|---|---|---|---|---|
| ecs.sn2ne | Intel V5/V6 | KVM | 40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 56、88 计算内存比：1:4 支持IPv6地址 |
| ecs.se1ne | Intel V5/V6 | KVM | 40 vCPU、48 vCPU、56 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 56、88 计算内存比：1:8 支持IPv6地址 |
| ecs.c5 | Intel V5 | 二代神龙架构 | 104 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 64、86、88 计算内存比：1:2 |
| ecs.g5 | Intel V5 | 二代神龙架构 | 104 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 64、86、88 计算内存比：1:4 |
| ecs.r5 | Intel V5 | 二代神龙架构 | 104 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 64、86、88 计算内存比：1:8 |

### 弹性裸金属

弹性裸金属可提供强劲的计算、存储以及网络配置，满足对资源独享、安全隔离、性能有较高要求的业务场景，如容器、数据库、企业核心业务、大数据计算等。本文介绍了弹性裸金属实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|

云服务器ECS

| ecs.ebmg7 s-se-x25- c1m8 | Intel V7 | 三代神龙架构 | 64 vCPU | 25 G | ecs.ebmg7s-se-x25- c1m8.16xlarge，64 vCPU 512 GiB 支持共享块存储，NUMA ON 配置 |
|---|---|---|---|---|---|
| ecs.ebmg7 m-se-x25- c1m8 | Intel V7 | 三代神龙架构 | 96 vCPU | 25 G | ecs.ebmg7m-se-x25- c1m8.24xlarge，96 vCPU 768 GiB 支持共享块存储，NUMA ON 配置 |
| ecs.ebmg7 x-se-x25- c1m8 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | ecs.ebmg7x-se-x25- c1m8.32xlarge，128 vCPU 1024 GiB 支持共享块存储，NUMA ON 配置 |
| ecs.ebmg7 s-se- numaoff- x25-c1m8 | Intel V7 | 三代神龙架构 | 64 vCPU | 25 G | ecs.ebmg7s-se-numaoff- x25-c1m8.16xlarge，64 vCPU 512 GiB 支持共享块存储，NUMA OFF 配置 |
| ecs.ebmg7 m-se- numaoff- x25-c1m8 | Intel V7 | 三代神龙架构 | 96 vCPU | 25 G | ecs.ebmg7m-se-numaoff- x25-c1m8.24xlarge，96 vCPU 768 GiB 支持共享块存储，NUMA OFF 配置 |
| ecs.ebmg7 x-se- numaoff- x25-c1m8 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | ecs.ebmg7x-se-numaoff- x25-c1m8.32xlarge，128 vCPU 1024 GiB 支持共享块存储，NUMA OFF 配置 |
| ecs.ebmg7 s-x25-c1m8 | Intel V7 | 三代神龙架构 | 64 vCPU | 25 G | ecs.ebmg7s-x25- c1m8.16xlarge，64 vCPU 512 GiB，NUMA ON 配置计算内存比：1:8 |
| ecs.ebmg7 m-x25- c1m8 | Intel V7 | 三代神龙架构 | 96 vCPU | 25 G | ecs.ebmg7m-x25- c1m8.24xlarge，96 vCPU 768 GiB，NUMA ON 配置 |

云服务器ECS

| ecs.ebmg7 x-x25-c1m8 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | ecs.ebmg7x-x25- c1m8.32xlarge，128 vCPU 1024 GiB，NUMA ON 配置计算内存比：1:8 |
|---|---|---|---|---|---|
| ecs.ebmg7 x-1nvme- x25-c1m8 | Intel V7 | 三代神龙架构 | 128vCPU | 25G | ecs.ebmg7x-1nvme-x25- c1m8.32xlarge，128vCPU 1024GiB |
| ecs.ebmg7 x-12nvme- x25-c1m8 | Intel V7 | 三代神龙架构 | 128vCPU | 25G | ecs.ebmg7x-1nvme-x25- c1m8.32xlarge，128vCPU 1024GiB |
| ecs.ebmg6 s-m10- c1m4 | Intel V6 | 二代神龙架构 | 64 vCPU | 10 G | ecs.ebmg6s-m10- c1m4.16xlarge，64 vCPU 256 GiB |
| ecs.ebmg6 s-m25- c1m4 | Intel V6 | 二代神龙架构 | 64 vCPU | 25 G | ecs.ebmg6s-m25- c1m4.16xlarge，64 vCPU 256 GiB |
| ecs.ebmg6 s-m10- c1m24 | Intel V6 | 二代神龙架构 | 64 vCPU | 10 G | ecs.ebmg6s-m10- c1m24.16xlarge，64 vCPU 1536 GiB |
| ecs.ebmg6 s-m25- c1m24 | Intel V6 | 二代神龙架构 | 64 vCPU | 25 G | ecs.ebmg6s-m25- c1m24.16xlarge，64 vCPU 1536 GiB |
| ecs.ebmg6 m-m10- c1m4 | Intel V6 | 二代神龙架构 | 96 vCPU | 10 G | ecs.ebmg6m-m10- c1m4.24xlarge，96 vCPU 384 GiB |
| ecs.ebmg6 m-m25- c1m4 | Intel V6 | 二代神龙架构 | 96 vCPU | 10 G | ecs.ebmg6m-m25- c1m4.24xlarge，96 vCPU 384 GiB |
| ecs.ebmre6 -3t | Intel V6 | 二代神龙架构 | 208 vCPU | 25 G | ecs.ebmre6- 3t.52xlarge，208 vCPU 3072 GiB |
| ecs.ebmc6 | Intel V6 | 二代神龙架构 | 104 vCPU | 25 G | ecs.ebmc6.26xlarge，104 vCPU 192 GiB |

云服务器ECS

| ecs.ebmg6 | Intel V6 | 二代神龙架构 | 104 vCPU | 25 G | ecs.ebmg6.26xlarge，104 vCPU 384 GiB |
|---|---|---|---|---|---|
| ecs.ebmr6 | Intel V6 | 二代神龙架构 | 104 vCPU | 25 G | ecs.ebmr6.26xlarge，104 vCPU 768 GiB |
| ecs.ebmre6 p | Intel V6 | 二代神龙架构 | 104 vCPU | 25 G | 搭配1536 GiB Intel傲腾持久内存（AEP） |
| ecs.ebmg5 | Intel V5 | 一代神龙架构 | 96 vCPU | 10 G | ecs.ebmg5.24xlarge，96 vCPU 384 GiB |
| ecs.ebmg5 s | Intel V5 | 二代神龙架构 | 96 vCPU | 25 G | ecs.ebmg5s.24xlarge，96 vCPU 384 GiB |

### 异构计算型&异构裸金属

异构计算型&异构裸金属实例可搭配各类加速器，如NVIDIA T4、NVIDIA V100、寒武纪 MLU 370 S4、 Hygon DCU Z100、FPGA等，适用于AI推理、计算机视觉、语音识别/合成、机器翻译、推荐系统、实时渲染、深度学习、科学计算等业务场景。本文介绍了异构计算型&异构裸金属实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.gn8ix- k25 | Intel V8 | KVM | 128 vCPU | 25 G | 搭配8块NVIDIA L20 |
| ecs.gp7vv- k25 | Intel V8 | KVM | 192 vCPU | 25 G | 搭配16块ZW810E 支持ENI Trunking |
| ecs.gn7fm- k10 | Intel V7 | KVM | 96 vCPU | 10 G | 搭配4块NVIDIA A16 |
| ecs.gn7fm- k25 | Intel V7 | KVM | 96 vCPU | 25 G | 搭配4块NVIDIA A16 |
| ecs.gn7km- k10 | Intel V7 | KVM | 96 vCPU | 10 G | 搭配4块NVIDIA A2 |
| ecs.gn7km- k25 | Intel V7 | KVM | 96 vCPU | 25 G | 搭配4块NVIDIA A2 |

云服务器ECS

| ecs.gn7kx- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 搭配8块NVIDIA A2 |
|---|---|---|---|---|---|
| ecs.gn7kx- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 搭配8块NVIDIA A2 |
| ecs.gn7im- k10 | Intel V7 | KVM | 96 vCPU | 10 G | 搭配2块NVIDIA A10 |
| ecs.gn7im- k25 | Intel V7 | KVM | 96 vCPU | 25 G | 搭配2块NVIDIA A10 |
| ecs.gn7fx- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 搭配8块NVIDIA A16 |
| ecs.gn7fx- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 搭配8块NVIDIA A16 |
| ecs.gh6vm- k10 | Intel V7 | KVM | 96 vCPU | 10 G | 搭配2块Hygon DCU Z100 |
| ecs.gh6vm- k25 | Intel V7 | KVM | 96 vCPU | 25 G | 搭配2块Hygon DCU Z100 |
| ecs.gh6vx- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 搭配8块Hygon DCU Z100 |
| ecs.gh6vx- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 搭配8块Hygon DCU Z100 |
| ecs.gc6im- k10 | Intel V7 | KVM | 96 vCPU | 10 G | 搭配2块寒武纪 MLU 370 S4 |
| ecs.gc6im- k25 | Intel V7 | KVM | 96 vCPU | 25 G | 搭配2块寒武纪 MLU 370 S4 |
| ecs.gc6ix- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 搭配8块寒武纪 MLU 370 S4 |
| ecs.gc6ix- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 搭配8块寒武纪 MLU 370 S4 |
| ecs.gc6em- k10 | Intel V7 | KVM | 96 vCPU | 10 G | 搭配2块寒武纪 MLU 370 X8 |

云服务器ECS

| ecs.gc6em- k25 | Intel V7 | KVM | 96 vCPU | 25 G | 搭配2块寒武纪 MLU 370 X8 |
|---|---|---|---|---|---|
| ecs.gc6ex- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 搭配8块寒武纪 MLU 370 X8 |
| ecs.gc6ex- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 搭配8块寒武纪 MLU 370 X8 |
| ecs.gn7ix- x25 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 搭配4块NVIDIA A10 |
| ecs.ebmgn 7ix-x25- c1m8 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 搭配4块NVIDIA A10 |
| ecs.vgn7hx -k10 | Intel V7 | KVM | 128 vCPU | 10 G | 搭配4块NVIDIA A40，支持分片后虚拟化的虚拟GPU，支持 NVIDIA A40的1/2 |
| ecs.vgn7hx -k25 | Intel V7 | KVM | 128 vCPU | 25 G | 搭配4块NVIDIA A40，支持分片后虚拟化的虚拟GPU，支持 NVIDIA A40的1/2 |
| ecs.vgn7ix- x25 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 搭配4块NVIDIA A10，支持分片后虚拟化的虚拟GPU，支持 NVIDIA A10的1/2、1/3、 1/4、1/6 |
| ecs.vgn6ix- k25-slice2 | Intel V7 | KVM | 128 vCPU | 25 G | 支持分片虚拟化后的虚拟 GPU 支持NVIDIA Tesla T4的 1/2 |
| ecs.vgn6ix- k10-slice2 | Intel V7 | KVM | 128 vCPU | 10 G | 支持分片虚拟化后的虚拟 GPU 支持NVIDIA Tesla T4的 1/2 |
| ecs.vgn6im -k25-slice4 | Intel V7 | KVM | 96 vCPU | 25 G | 支持分片虚拟化后的虚拟 GPU 支持NVIDIA Tesla T4的 1/4 |

云服务器ECS

| ecs.vgn6im -k10-slice4 | Intel V7 | KVM | 96 vCPU | 10 G | 支持分片虚拟化后的虚拟 GPU 支持NVIDIA Tesla T4的 1/4 |
|---|---|---|---|---|---|
| ecs.gn7ix- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 搭配4块或8块NVIDIA A10 |
| ecs.gn7ix- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 搭配4块NVIDIA A10 |
| ecs.gn6ix- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 搭配4块NVIDIA Tesla T4 |
| ecs.gn6ix- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 搭配4块NVIDIA Tesla T4 |
| ecs.gn6i | Intel V5/V6 | KVM | 48 vCPU、64 vCPU、80 vCPU、96 vCPU | 10 G、 25 G | 搭配1~8块NVIDIA T4 计算内存比约为1:4 |
| ecs.gn6v | Intel V5/V6 | KVM | 96 vCPU | 10 G、 25 G | 搭配1~8块NVIDIA V100 计算内存比约为1:4 |
| ecs.vgn6i | Intel V5/V6 | 二代神龙架构 | 96 vCPU、 104 vCPU | 10 G、 25 G | 支持分片虚拟化后的虚拟 GPU 支持NVIDIA Tesla T4的 1/4和1/2 |
| ecs.ebmgn 6i | Intel V5/V6 | 二代神龙架构 | 96 vCPU、 104 vCPU | 10 G、 25 G | 搭配4块NVIDIA T4 弹性裸金属 |
| ecs.ebmgn 6i-2 | Intel V5/V6 | 二代神龙架构 | 96 vCPU、 104 vCPU | 10 G、 25 G | 搭配2块NVIDIA T4 弹性裸金属 |
| ecs.ebmgn 6i-8 | Intel V5/V6 | 二代神龙架构 | 96 vCPU | 10 G、 25 G | 搭配8块NVIDIA T4 弹性裸金属 |
| ecs.ebmgn 6e-2 | Intel V6 | 二代神龙架构 | 104 vCPU | 10 G、 25 G | 搭配2块NVIDIA V100 弹性裸金属 |

云服务器ECS

| ecs.gn3 | Intel V4 | KVM | 56 vCPU | 10 G、 25 G | 搭配1~2块NVIDIA K2 |
|---|---|---|---|---|---|
| ecs.gn4 | Intel V4 | KVM | 56 vCPU | 10 G、 25 G | 搭配1~2块NVIDIA M40 |
| ecs.gn5 | Intel V4 | KVM | 64 vCPU | 10 G、 25 G | 搭配1~8块NVIDIA P100 |
| ecs.gn5e | Intel V5 | KVM | 96 vCPU | 10 G、 25 G | 搭配1~8块NVIDIA P4 计算内存比为1:6 |
| ecs.gn5i | Intel V4 | KVM | 56 vCPU、64 vCPU | 10 G、 25 G | 搭配1~2块NVIDIA P4 计算内存比为1:4 |
| ecs.gn5t | Intel V4 | KVM | 64 vCPU | 10 G、 25 G | 搭配2~8块NVIDIA 1080Ti 计算内存比约为1:4 |

### 超级计算集群

超级计算集群实例在弹性裸金属实例的基础上，搭配高速InfiniBand（IB）网络，提供具有极致计算性能和并行效率的计算集群服务，适合搭建高性能计算、人工智能/机器学习、科学/工程计算、数据分析、音视频

**说明**

SCC超级计算集群专用于HPC场景，需要关闭HT，但规格大小依然是按照开启HT计算的，因此在操作系统（GuestOS）内查询的CPU核数为规格定义核数的一半。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.sccg7- ib | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 搭配InfiniBand高性能网络 |
| ecs.sccc7- ib | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 搭配InfiniBand高性能网络 |
| ecs.sccr7-ib | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 搭配InfiniBand高性能网络 |
| ecs.sccg7x- roce-x25- c1m2 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 支持RoCE网卡 |

云服务器ECS

| ecs.sccg7x- roce-x25- c1m4 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 支持RoCE网卡 |
|---|---|---|---|---|---|
| ecs.sccg7x- roce-x25- c1m8 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 支持RoCE网卡 |
| ecs.sccgn6 e | Intel V6 | 二代神龙架构 | 104 vCPU | 10 G、 25 G | 搭配8块NVIDIA V100和100 Gbps InfiniBand高性能网络 |
| ecs.sccgn6 p | Intel V5/V6 | 二代神龙架构 | 96 vCPU | 10 G、 25 G | 搭配8块NVIDIA V100和100 Gbps InfiniBand高性能网络 |
| ecs.scch5 | Intel V5 | 二代神龙架构 | 64 vCPU | 10 G、 25 G | 高主频处理器，基频3.1 GHz，全核睿频3.5 GHz |
| ecs.sccg5ib | Intel V5 | 一代神龙架构 | 96 vCPU | 10 G | 搭配100 Gbps InfiniBand高性能网络 |

### 本地HDD盘

本地HDD盘实例适用于有大数据计算与存储分析需求的业务场景，如海量数据存储和离线计算，满足以 Hadoop为代表的分布式计算业务对实例存储性能、存储容量和内网带宽的多方面要求。本文介绍了本地 HDD盘实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.d7s- 12x8t-k25 | Intel V7 | KVM | 64 vCPU | 25 G | 整机配置12块8 TB SATA HDD |
| ecs.d7x- 12x12t-k25 | Intel V7 | KVM | 128 vCPU | 25 G | 整机配置12块12TB SATA HDD |
| ecs.d7x- 12x12t-k10 | Intel V7 | KVM | 128 vCPU | 10 G | 整机配置12块12TB SATA HDD |
| ecs.d7s- 12x8t-k10 | Intel V7 | KVM | 64 vCPU | 10 G | 整机配置12块8TB SATA HDD |
| ecs.d7s- 10x16t-k25 | Intel V7 | KVM | 64 vCPU | 25 G | 整机配置10块16TB SATA HDD |

云服务器ECS

| ecs.d7s- 10x16t-k10 | Intel V7 | KVM | 64 vCPU | 10 G | 整机配置10块16TB SATA HDD |
|---|---|---|---|---|---|
| ecs.d7m- 12x8t-k25 | Intel V7 | KVM | 96 vCPU | 25 G | 整机配置12块8TB SATA HDD |
| ecs.d7m- 12x8t-k10 | Intel V7 | KVM | 96 vCPU | 10 G | 整机配置12块8TB SATA HDD |
| ecs.d7s- k10-8t | Intel V7 | KVM | 64 vCPU | 10 G | 整机配置12块8 TB SATA HDD |
| ecs.d7s- k25-8t | Intel V7 | KVM | 64 vCPU | 25 G | 整机配置12块8 TB SATA HDD |
| ecs.d7m- k10-8t | Intel V7 | KVM | 96 vCPU | 10 G | 整机配置12块8 TB SATA HDD |
| ecs.d7m- k25-8t | Intel V7 | KVM | 96 vCPU | 25 G | 整机配置12块8 TB SATA HDD |
| ecs.d7x- k10-12t | Intel V7 | KVM | 128 vCPU | 10 G | 整机配置12块12 TB SATA HDD |
| ecs.d7x- k25-12t | Intel V7 | KVM | 128 vCPU | 25 G | 整机配置12块12 TB SATA HDD |
| ecs.d6m- 24x2t-k10 | Intel V6 | KVM | 80 vCPU | 10 G | 整机配置24块2 TB SATA HDD |
| ecs.d5m- 24x1t-k10 | Intel V5 | KVM | 80 vCPU | 10 G | 整机配置24块1 TB SATA HDD |
| ecs.d4s- 16x1t-k10 | Intel V4 | KVM | 56 vCPU | 10 G | 整机配置16块1 TB SATA HDD |
| ecs.d2-zyy | Intel V5/V6 | KVM | 40 vCPU、48 vCPU、64 vCPU、80 vCPU、96 vCPU、104 vCPU | 10 G、 25 G | 整机配置12块8 TB SATA HDD |

### 突发型

云服务器ECS 突发型实例的vCPU可持续提供基准性能，可突然提速，但受到CPU积分的限制，适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序。本文介绍了突发型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.t5 | Intel V5/V6 | KVM | 40 vCPU、48 vCPU、64 vCPU、80 vCPU、96 vCPU、104 vCPU | 10 G、 25 G | vCPU持续提供基准性能，可突然提速，但受到CPU积分的限制。 |

### 网络增强型

网络增强型实例，针对网络密集型应用场景专门优化，各项网络指标得到提升，远高于同代通用实例规格， 满足垂直场景需求。特别适用于需要网络性能高于通用实例的场景。本文介绍了网络增强型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.ne9x- k25 | Intel V9 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、16、32、64、72 计算内存比：1:2、1:4、 1:6、1:8 |
| ecs.ne9m- k25 | Intel V9 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、16、32、64、72 计算内存比：1:2、1:4、 1:6、1:8 |
| ecs.ne8m- k25 | Intel V8 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、16、32、64、72 计算内存比：1:2、1:4、 1:6、1:8 |
| ecs.ne7x- k10 | Intel V7 | KVM | 128 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、16、32、64、 72、96、104 计算内存比：1:2、1:4、 1:6、1:8 |
| ecs.ne7m- k25 | Intel V7 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：8、 12、16、24、32、40、 48、56、64、72 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS

| ecs.ne7m- k10 | Intel V7 | KVM | 96 vCPU | 10 G | 规格大小（vCPU）：8、 12、16、24、32、40、 48、56、64、72 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|

### 存储增强型

存储增强型实例在云盘带宽、云盘IOPS等EBS相关能力上进行了优化，更适用于存储密集型应用场景。本文

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.g7x-se- k25 | Intel V7 | KVM | 128 vCPU | 25 G | 支持共享块存储 |
| ecs.g7x-se- x25 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 支持共享块存储 |
| ecs.g7x-se- x25 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 规格大小（vCPU）： 2、4、 8、12、16、24、32、48、 64、128 |
| ecs.ebmg7 s-se- numaoff- x25-c1m8 | Intel V7 | 三代神龙架构 | 64 vCPU | 25 G | 计算内存比：1:8 支持共享块存储，支持 NUMA OFF配置 |
| ecs.g7s-se- x25 | Intel V7 | 三代神龙架构 | 64 vCPU | 25 G | 计算内存比：1:8 |
| ecs.ebmg7 x-se- numaoff- x25-c1m8 | Intel V7 | 三代神龙架构 | 128 vCPU | 25 G | 计算内存比：1:8 支持共享块存储，支持 NUMA OFF配置 |

### 可信计算型

可信计算型实例通过使用UEFI安全固件、虚拟可信平台模块（vTPM/vTCM）、远程证明服务，实现实例启动度量和完整性校验，从而保障实例的安全可信。本文介绍了可信计算型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|

云服务器ECS

| ecs.g7x- vtpm-k25 | Intel V7 | KVM | 128vCPU | 25G | 支持ENI Trunking 计算内存比：1:1、 1:2、1:3、1:4、1:6、 1:8 |
|---|---|---|---|---|---|

### 本地SSD盘

本地SSD型实例属于高I/O型本地盘存储实例，适用于对存储I/O性能有极高要求，同时具备应用层高可用架构的业务场景，例如NoSQL非关系型数据库、MPP数据仓库、分布式文件系统等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.i7m- 12x4t-k25 | Intel V7 | KVM | 96 vCPU | 25 G | 整机配置12块3840 GB的NVMe SSD |
| ecs.i7m- 4x4t-k25 | Intel V7 | KVM | 96 vCPU | 25 G | 整机配置4块3840 GB的NVMe SSD |
| ecs.i7x- 12x4t-k25 | Intel V7 | KVM | 128 vCPU | 25 G | 整机配置12块3840 GB的NVMe SSD |
| ecs.i7x- 12x4t-k10 | Intel V7 | KVM | 128 vCPU | 10 G | 整机配置12块3840 GB的NVMe SSD |
| ecs.i6m- k25-4x4t | Intel V6 | KVM | 96 vCPU | 25 G | 整机配置4块3840 GB的NVMe SSD |
| ecs.i6m- k10-4x4t | Intel V6 | KVM | 96 vCPU | 10 G | 整机配置4块3840 GB的NVMe SSD |

云服务器ECS

## 倚天规格族

### 共享型

共享型实例适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序、开发环境、构建服务器、代码存储库、微服务、测试和暂存环境、轻量级数据库、轻量级企业应用、综合应用服务等。本文介绍了共享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.s8-yt-k | Yitian 710 | KVM | 128vCPU | 10G、 25G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.s8- numaon-yt- k | Yitian 710 | KVM | 128vCPU | 10G、 25G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 支持NUMA ON |

### 独享型

独享型实例适合对虚拟机性能要求较高的业务场景，如高网络包收发场景、Web前端服务器、数据分析、批量计算、视频编码、高性能科学和工程应用等。本文介绍了独享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.g8x-yt- k10 | Yitian 710 | KVM | 128vCPU | 10G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8x-yt- k25 | Yitian 710 | KVM | 128vCPU | 25G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 支持NUMA ON |

云服务器ECS

| ecs.g8x- numaon-yt- k10 | Yitian 710 | KVM | 128vCPU | 10G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64、 80、96 计算内存比：1:4 支持NUMA ON |
|---|---|---|---|---|---|
| ecs.g8x- numaon-yt- k25 | Yitian 710 | KVM | 128vCPU | 25G | 规格大小（vCPU）： 2、 4、8、12、16、24、 32、40、48、56、64、 80、96 计算内存比：1:4 支持NUMA ON |

云服务器ECS

## Hygon规格族

### 共享型

共享型实例适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序、开发环境、构建服务器、代码存储库、微服务、测试和暂存环境、轻量级数据库、轻量级企业应用、综合应用服务等。本文介绍了共享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.s8 -hg-k | Hygon 4号 | KVM | 256 vCPU | 25 G | 计算内存比：1:1、1:2、1:3、1:4、1:6、1:8 规格大小（vCPU）：2、4、8、12、16、24、 32、40、48、56、64 |
| ecs.s8 - numa on-hg- k | Hygon 4号 | KVM | 256 vCPU | 10 G、 25 G | 支持NUMA ON配置计算内存比：1:1、1:2、1:3、1:4、1:6、1:8 规格大小（vCPU）：2、4、8、12、16、24、 32、40、48、56、64 |
| ecs.s7 - numa on-hg- k | Hygon 3号 | KVM | 128 vCPU | 10 G、 25 G | 支持NUMA ON配置计算内存比：1:1、1:2、1:3、1:4、1:6、1:8 规格大小（vCPU）：2、4、8、12、16、24、 32、40、48、56、64 |
| ecs.s7 -hg-k | Hygon 3号 | KVM | 128 vCPU | 10 G、 25 G | 计算内存比：1:1、1:2、1:3、1:4、1:6、1:8 规格大小（vCPU）：2、4、8、12、16、24、 32、40、48、56、64 |
| ecs.s6 -hg-k | Hygon 2号 | KVM | 64 vCPU、 128 vCPU | 10 G、 25 G | 计算内存比：1:1、1:2、1:3、1:4、1:6、1:8 规格大小（vCPU）：2、4、8、12、16、24、 32、40、48、56、64 |
| ecs.gh g-s | Hygon 1号 | 神龙二代 | 128 vCPU | 10 G、 25 G | 计算内存比：1:4 规格大小（vCPU）：2、4、8、12、16、32、 64、96、128 |

### 独享型

独享型实例适合对虚拟机性能要求较高的业务场景，如高网络包收发场景、Web前端服务器、数据分析、批量计算、视频编码、高性能科学和工程应用等。本文介绍了独享型实例规格族的具体属性、规格大小、虚拟化技术等。 云服务器ECS

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.g8h- vtpm- 2numa-hg- k10 | Hygon 4号 | KVM | 256 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128、192 计算内存比：1:2、1:3、 1:4、1:6、1:8 支持vTPM特性 |
| ecs.g8h- vtpm- 2numa-hg- k25 | Hygon 4号 | KVM | 256 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128、192 计算内存比：1:2、1:3、 1:4、1:6、1:8 支持vTPM特性 |
| ecs.g8m- 2numa-hg- k10 | Hygon 4号 | KVM | 96 vCPU | 10 G | 支持NUMA ON配置支持ENI Trunking 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、64 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g8m- 2numa-hg- k25 | Hygon 4号 | KVM | 96 vCPU | 25 G | 支持NUMA ON配置支持ENI Trunking 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、64 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g8x- 2numa-hg- k10 | Hygon 4号 | KVM | 128 vCPU | 10 G | 支持NUMA ON配置支持ENI Trunking 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96 计算内存比：1:2、1:3、 1:4、1:6、1:8 |

云服务器ECS

| ecs.g8x- 2numa-hg- k25 | Hygon 4号 | KVM | 128 vCPU | 25 G | 支持NUMA ON配置支持ENI Trunking 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g8v- 2numa-hg- k10 | Hygon 4号 | KVM | 192 vCPU | 10 G | 支持NUMA ON配置支持ENI Trunking 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g8v- 2numa-hg- k25 | Hygon 4号 | KVM | 192 vCPU | 25 G | 支持NUMA ON配置支持ENI Trunking 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g8h- 2numa-hg- k10 | Hygon 4号 | KVM | 256 vCPU | 10 G | 支持ENI Trunking 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128、192 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g8h- 2numa-hg- k25 | Hygon 4号 | KVM | 256 vCPU | 25 G | 支持ENI Trunking 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128、192 计算内存比：1:2、1:3、 1:4、1:6、1:8 |

云服务器ECS

| ecs.g8h- hg-k25 | Hygon 4号 | KVM | 256 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、128、 160、192、224、242 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g7m- hg-k10 | Hygon 3号 | KVM | 96 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、86 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g7m- hg-k25 | Hygon 3号 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、86 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g7x- numaoff- hg-x25 | Hygon 3号 | 三代神龙架构 | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、48、64、96、128 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7x- numaon- hg-x25 | Hygon 3号 | 三代神龙架构 | 128 vCPU | 25 G | 支持NUMA ON配置规格大小（vCPU）：2、 4、8、12、16、24、 32、68、128 计算内存比：1:8 |
| ecs.g7x- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7x- numaon- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、48、64 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g7x- numaon- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、48、64 计算内存比：1:2、1:3、 1:4、1:6、1:8 |

云服务器ECS

| ecs.g7x- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、104、 112、118 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g7s- numaon- hg-k25 | Hygon 3号 | KVM | 64 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g7s- numaon- hg-k10 | Hygon 3号 | KVM | 64 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、32 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g7s- hg-k25 | Hygon 3号 | KVM | 64 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、54 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g7s- hg-k10 | Hygon 3号 | KVM | 64 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、54 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6s- hg-k10 | Hygon 2号 | KVM | 64 vCPU | 10G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6s- hg-k25 | Hygon 2号 | KVM | 64 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6x- hg-k10 | Hygon 2号 | KVM | 128 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、104、 112、120 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS

| ecs.g6x- hg-k25 | Hygon 2号 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、104、 112、120 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.ghg | Hygon 1 号/2号 | 神龙二代 | 128 vCPU | 10 G、 25 G | 计算内存比：1:4 |

### 异构计算型

Hygon异构计算型实例可搭配各类加速器，如Hygon 1号、Hygon 3号等，适用于AI推理、计算机视觉、 语音识别/合成、机器翻译、推荐系统、实时渲染、深度学习、科学计算等业务场景。本文介绍了异构计算型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.gh8vv- 2numa-hg- k10 | Hygon 4号 | KVM | 192 vCPU | 10 G | 搭配8块Hygon DCU BW150 |
| ecs.gh8vv- 2numa-hg- k25 | Hygon 4号 | KVM | 192 vCPU | 25 G | 搭配8块Hygon DCU BW150 |
| ecs.gn7kx- hg-k10 | Hygon 2号 | KVM | 128 vCPU | 10 G | 搭配2块NVIDIA A2 |
| ecs.gn7kx- hg-k25 | Hygon 2号 | KVM | 128 vCPU | 25 G | 搭配2块NVIDIA A2 |
| ecs.gb7eh- 2numa-hg- k10 | Hygon 4号 | KVM | 256 vCPU | 10 G | 搭配8块昆仑芯P800 |
| ecs.gb7eh- 2numa-hg- k25 | Hygon 4号 | KVM | 256 vCPU | 25 G | 搭配8块昆仑芯P800 |
| ecs.gp7vh- 2numa-hg- k25 | Hygon 4号 | KVM | 256 vCPU | 25 G | 搭配16块ZW810E |

云服务器ECS

| ecs.gp7vv- 2numa-hg- k25 | Hygon 4号 | KVM | 192 vCPU | 25 G | 搭配16块ZW810E |
|---|---|---|---|---|---|
| ecs.gp7vv- 2numa-hg- k10 | Hygon 4号 | KVM | 192 vCPU | 10 G | 搭配16块ZW810E |
| ecs.gn6ix- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配4块NVIDIA T4 |
| ecs.gn6ix- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配4块NVIDIA T4 |
| ecs.gh7vh- 2numa-hg- k25 | Hygon 4号 | KVM | 256 vCPU | 25 G | 搭配8块Hygon DCU K100 AI |
| ecs.gh7vh- 2numa-hg- k10 | Hygon 4号 | KVM | 256 vCPU | 10 G | 搭配8块Hygon DCU K100 AI |
| ecs.gn7ix- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配4块NVIDIA A10 |
| ecs.gn7ix- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配4块NVIDIA A10 |
| ecs.gh7ex- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配8块Hygon DCU K100 |
| ecs.gh7ex- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配8块Hygon DCU K100 |
| ecs.gc6ex- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配2块寒武纪 MLU 370 X8 或8块寒武纪 MLU 370 X8 |
| ecs.gc6ex- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配2块寒武纪 MLU 370 X8 或8块寒武纪 MLU 370 X8 |
| ecs.ge7ix- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配8块燧原 I20 |
| ecs.ge7ix- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配8块燧原 I20 |

云服务器ECS

| ecs.ge7vx- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配8块燧原 T20 |
|---|---|---|---|---|---|
| ecs.ge7vx- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配8块燧原 T20 |
| ecs.gt6ex- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配8块ILUVATAR BI-V150 |
| ecs.gt6ex- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配8块ILUVATAR BI-V150 |
| ecs.gh7vx- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配8块海光DCUK100-AI |
| ecs.gh7vx- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配8块海光DCUK100-AI |
| ecs.gh6vx- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 搭配2块或8块海光DCUZ100L |
| ecs.gh6vx- hg-k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 搭配2块或8块海光DCUZ100L |
| ecs.gn6hv | Hygon 1号 | KVM | 128 vCPU | 10 G、 25 G | 搭配1~2块NVIDIA V100 计算内存比约为1:4 |

### 本地HDD盘

本地HDD盘实例适用于有大数据计算与存储分析需求的业务场景，如海量数据存储和离线计算，满足以 Hadoop为代表的分布式计算业务对实例存储性能、存储容量和内网带宽的多方面要求。本文介绍了本地 HDD盘实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.dhg | Hygon 1 号/2号 | KVM | 64 vCPU、 128 vCPU | 10 G、 25 G | 整机配置12块8 TB SATA HDD |

### 本地SSD盘

本地SSD盘用于满足I/O密集型应用对块存储的低时延和高I/O性能需求，如NoSQL非关系型数据库 （Cassandra、MongoDB等）、MPP数据仓库和分布式文件系统、ElasticSearch等搜索场景等。本文介云服务器ECS

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.i7x- 4x4t-hg- k10 | Hygon 3号 | KVM | 128 vCPU | 10 G | 整机配置4块3840GB的NVMe SSD |
| ecs.i7x- 4x4t-hg- k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 整机配置4块3840GB的NVMe SSD |

### 超级计算集群

超级计算集群实例在弹性裸金属实例的基础上，搭配高速InfiniBand（IB）网络，提供具有极致计算性能和并行效率的计算集群服务，适合搭建高性能计算、人工智能/机器学习、科学/工程计算、数据分析、音视频

**说明**

SCC超级计算集群专用于HPC场景，需要关闭HT，但规格大小依然是按照开启HT计算的，因此在操作系统（GuestOS）内查询的CPU核数为规格定义核数的一半。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.sccg7x- roce-hg- x25-c1m4 | Hygon 3号 | 三代神龙架构 | 128 vCPU | 25 G | 支持RoCE网卡 |

### 网络增强型

网络增强型实例，针对网络密集型应用场景专门优化，各项网络指标得到提升，远高于同代通用实例规格， 满足垂直场景需求。特别适用于需要网络性能高于通用实例的场景。本文介绍了网络增强型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.ne8x- hg-k25 | Hygon 4号 | KVM | 128 vCPU | 25 G | 支持ENI Trunking 规格大小（vCPU）：2、 4、8、16、32、64、72 计算内存比：1:2、1:4、 1:6、1:8 |
| ecs.ne8m- hg-k25 | Hygon 4号 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、16、32、64、72 计算内存比：1:2、1:4、 1:6、1:8 |

云服务器ECS

| ecs.ne7x- hg-k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、16、32、64、 72、96、104 计算内存比：1:2、1:4、 1:6、1:8 |
|---|---|---|---|---|---|

### 存储增强型

存储增强型实例在云盘带宽、云盘IOPS等EBS相关能力上进行了优化，更适用于存储密集型应用场景。本文

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.g8h- se-2numa- hg-k25 | Hygon 4号 | KVM | 256 vCPU | 25 G | 支持共享块存储 |
| ecs.g8x-se- 2numa-hg- k25 | Hygon 4号 | KVM | 128 vCPU | 25 G | 支持共享块存储 |
| ecs.g7x-se- numaoff- hg-x25 | Hygon 3号 | 三代神龙架构 | 128 vCPU | 25 G | 支持共享块存储规格大小（vCPU）：16、 32、128 计算内存比：1:8 |
| ecs.g7x-se- 2numa-hg- k25 | Hygon 3号 | KVM | 128 vCPU | 25 G | 支持共享块存储 |

云服务器ECS 族

## Kunpeng规格族

### 共享型

共享型实例适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序、开发环境、构建服务器、代码存储库、微服务、测试和暂存环境、轻量级数据库、轻量级企业应用、综合应用服务等。本文介绍了共享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.s8- numaon-kp- k | Kunpeng92 0 | KVM | 128 vCPU、 160 vCPU、 256 vCPU | 10 G、 25 G | 支持NUMA ON配置规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.s5-kp-k | Kunpeng92 0 | KVM | 64 vCPU、96 vCPU、128 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、32、 40、48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.gkp-s | Kunpeng92 0 | KVM | / | 10 G、 25 G | 计算内存比：1:4 |

### 独享型

独享型实例适合对虚拟机性能要求较高的业务场景，如高网络包收发场景、Web前端服务器、数据分析、批量计算、视频编码、高性能科学和工程应用等。本文介绍了独享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.g8v- 2numa-kp- k25 | Kunpeng920 | KVM | 192 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128 计算内存比：1:2、1:3、 1:4、1:6、1:8 |

云服务器ECS 族

| ecs.g8v- 2numa-kp- k10 | Kunpeng920 | KVM | 192 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g8h- 2numa-kp- k25 | Kunpeng920 | KVM | 256 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128、192 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8h- 2numa-kp- k10 | Kunpeng920 | KVM | 256 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128、192 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g8x- 2numa-kp- k25 | Kunpeng920 | KVM | 128vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g8x- 2numa-kp- k10 | Kunpeng920 | KVM | 128vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
| ecs.g5h- kp-k10 | Kunpeng920 | KVM | 256 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS 族

| ecs.g5h- kp-k25 | Kunpeng920 | KVM | 256 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g5s- kp-k10 | Kunpeng920 | KVM | 64 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g5s- kp-k25 | Kunpeng920 | KVM | 64 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g5m- kp-k10 | Kunpeng920 | KVM | 96 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g5m- kp-k25 | Kunpeng920 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g5x- kp-k10 | Kunpeng920 | KVM | 128 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、 104、112、120 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g5x- kp-k25 | Kunpeng920 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、 104、112、120 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS 族

| ecs.g5m- kp-m10 | Kunpeng920 | 二代神龙架构 | 96 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g5m- kp-m25 | Kunpeng920 | 二代神龙架构 | 96 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.gkp | Kunpeng920 | KVM | 96 vCPU | 10 G、 25 G | 计算内存比：1:4 |
| ecs.gkp-m | Kunpeng920 | 二代神龙架构 | / | 10 G、 25 G | 计算内存比：1:4 |

### 异构计算型

Kunpeng异构计算型实例可搭配各类加速器，如Atlas 300I、Atlas 710、Ascend 910等，适用于AI推理、计算机视觉、语音识别/合成、机器翻译、推荐系统、实时渲染、深度学习、科学计算等业务场景。本文

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.gs6im- kp-k10 | Kunpeng 920 | KVM | 96 vCPU | 10 G | 搭配6块或4块或2块 HUAWEI DaVinci Atlas300 I Pro |
| ecs.gs6im- kp-k25 | Kunpeng 920 | KVM | 96 vCPU | 25 G | 搭配6块或4块或2块 HUAWEI DaVinci Atlas300 I Pro |
| gs6vv-b4- kp-k25 | Kunpeng 920 | KVM | 192 vCPU | 25 G | 搭配8块 HUAWEI DaVinci Ascend9 10B4 HAM |
| ecs.gs6vv- kp-k25 | Kunpeng 920 | KVM | 192 vCPU | 25 G | 搭配8块 HUAWEI DaVinci Ascend9 10B3 HAM |

云服务器ECS 族

| ecs.gs6vv- kp-k10 | Kunpeng 920 | KVM | 192 vCPU | 10 G | 搭配8块 HUAWEI DaVinci Ascend9 10B3 HAM |
|---|---|---|---|---|---|
| ecs.gs6sm- kp-k25 | Kunpeng 920 | KVM | 96 vCPU | 25 G | 搭配4块 HUAWEI DaVinci Atlas300 I DUO |
| ecs.gs6sm- kp-k10 | Kunpeng 920 | KVM | 96 vCPU | 10 G | 搭配4块 HUAWEI DaVinci Atlas300 I DUO |

### 本地HDD盘

本地HDD盘实例适用于有大数据计算与存储分析需求的业务场景，如海量数据存储和离线计算，满足以 Hadoop为代表的分布式计算业务对实例存储性能、存储容量和内网带宽的多方面要求。本文介绍了本地 HDD盘实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.dkp | Kunpeng920 | KVM | 64 vCPU、96 vCPU | 10 G、 25 G | 整机配置12块8 TB SATA HDD |

### 网络增强型

网络增强型实例，针对网络密集型应用场景专门优化，各项网络指标得到提升，远高于同代通用实例规格， 满足垂直场景需求。特别适用于需要网络性能高于通用实例的场景。本文介绍了网络增强型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.ne8x-kp-k25 | Kunpen g 920- 5250Z | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、4、 8、16、32、64、72 计算内存比：1:2、1:4、1:6、 1:8 |
| ecs.ne8m-kp-k25 | Kunpen g 920- 5230Z | KVM | 192 vCPU | 25 G | 规格大小（vCPU）：2、4、 8、16、32、64、72 计算内存比：1:2、1:4、1:6、 1:8 |

云服务器ECS 族

| ecs.ne5x-kp-k25 | Kunpen g 920 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、4、 8、16、32、64、72 计算内存比：1:2、1:4、1:6、 1:8 |
|---|---|---|---|---|---|
| ecs.ne5m-kp-k25 | Kunpen g 920 | KVM | 96 vCPU | 25 G | 规格大小（vCPU）：8、12、 16、24、32、40、48、56、 64、72 计算内存比：1:1、1:2、1:3、 1:4、1:6、1:8 |
| ecs.ne5m-kp-k10 | Kunpen g 920 | KVM | 96 vCPU | 10 G | 规格大小（vCPU）：8、12、 16、24、32、40、48、56、 64、72 计算内存比：1:1、1:2、1:3、 1:4、1:6、1:8 |

云服务器ECS 族

## Feiteng规格族

### 共享型

共享型实例适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序、开发环境、构建服务器、代码存储库、微服务、测试和暂存环境、轻量级数据库、轻量级企业应用、综合应用服务等。本文介绍了共享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.s7- 2numa-ft-k | FT-5000C-E | KVM | 160 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、4、 8、12、16、24、32、40、 48、56、64 计算内存比 1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.s5-ft-k | FT-2000+ | KVM | 64 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、4、 8、12、16、24、32、40、 48、56、64 计算内存比 1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.s6-ft-k | FT-S2500 | KVM | 128 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、4、 8、12、16、24、32、40、 48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

### 独享型

独享型实例适合对虚拟机性能要求较高的业务场景，如高网络包收发场景、Web前端服务器、数据分析、批量计算、视频编码、高性能科学和工程应用等。本文介绍了独享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.g7x- 2numa-ft- k10 | FT-5000C-E | KVM | 160 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128 计算内存比：1:2、1:3、 1:4、1:6、1:8 |

云服务器ECS 族

| ecs.g7x- 2numa-ft- k25 | FT-5000C-E | KVM | 160 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 96、128 计算内存比：1:2、1:3、 1:4、1:6、1:8 |
|---|---|---|---|---|---|
| ecs.g7x- 8numa-ft- k10 | FT-5000C | KVM | 128 vCPU | 10 G | 支持ENI Trunking 计算内存比：1:4、2:7、 4:15、8:30、16:60、 24:90、32:120、 48:180、64:240、 96:360 |
| ecs.g6x- numaon-ft- k10 | FT-S2500 | KVM | 128 vCPU | 10 G | 支持NUMA ON 配置 |
| ecs.g6x- numaon-ft- k25 | FT-S2500 | KVM | 128 vCPU | 25 G | 支持NUMA ON 配置 |
| ecs.g5s-ft- k10 | FT-2000+ | KVM | 64 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g5s-ft- k25 | FT-2000+ | KVM | 64 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6x-ft- k10 | FT-S2500 | KVM | 128 vCPU | 10 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、104、 112、120 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
| ecs.g6x-ft- k25 | FT-S2500 | KVM | 128 vCPU | 25 G | 规格大小（vCPU）：2、 4、8、12、16、24、 32、40、48、56、64、 72、80、88、96、104、 112、120 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

云服务器ECS 族

| ecs.gft | FT-2000+ | KVM | 64 vCPU | 10 G、 25 G | 计算内存比：1:4 |
|---|---|---|---|---|---|

云服务器ECS

## 兆芯规格族

### 共享型

共享型实例适合对虚拟机性能要求不高的业务场景，如中小型网站和Web应用程序、开发环境、构建服务器、代码存储库、微服务、测试和暂存环境、轻量级数据库、轻量级企业应用、综合应用服务等。本文介绍了共享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.s7-zx-k | 兆芯KH- 40000/32 | KVM | 64 vCPU | 10 G、 25 G | 规格大小（vCPU）：2、4、 8、12、16、24、32、40、 48、56、64 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |

### 独享型

独享型实例适合对虚拟机性能要求较高的业务场景，如高网络包收发场景、Web前端服务器、数据分析、批量计算、视频编码、高性能科学和工程应用等。本文介绍了独享型实例规格族的具体属性、规格大小、虚拟化技术等。

| 规格族 | 处理器 | 虚拟化 | 物理机线程数 | 网络 | 规格族描述 |
|---|---|---|---|---|---|
| ecs.g7s-zx- k10 | 兆芯KH- 40000/32 | KVM | 64 vCPU | 10 G | 支持ENI Trunking 规格大小（vCPU）：2、4、 8、12、16、24、32、40、 48、54 计算内存比：1:1、1:2、 1:3、1:4、1:6、1:8 |
