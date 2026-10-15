---
title: "全栈云平台 多Region技术白皮书"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 32
source_pdf: "04_多Region技术白皮书_a2c6b57.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/apsarabase/zh/a2c6b57.pdf"
converter: line-classifier (PyMuPDF)
---

# 全栈云平台 多Region技术白皮书

## 多Region概述

### 背景

专有云的地域（Region）指的是根据地理位置，把某个地区的基础设施服务的集合称为一个地域。地域可以按照多种维度进行划分，通常按照数据中心所在的城市进行划分，也可以按照合规要求进行划分。 专有云的各个地域是相互独立的。专有云云服务通过地域可以为客户提供在地理位置上靠近用户的基础设施来部署各种应用，用户可以选择不同地域存储数据，以满足各种法规遵循方面的客户需求。 专有云多Region设计的因素主要有以下几种： 可用性提供故障转移能力，以抵御区域系统故障，从而使部分或全部系统能够有效地将服务应用迁移至备用区域。此外，还能够确保灰度部署和发布升级过程中的业务连续性。 低延迟在某些访问分布广泛的场景中，应用程序的访问模式及常规使用模式往往难以在单一地域内实现，因此必须确保不会产生较大的网络跳跃开销。 合规性地域合规性要求数据和服务必须在特定地区内遵循相关法规的规定。 一云多芯用于异构芯片资源池统一管理调度，按照芯片类型建设Region，既保持隔离性又具备统一管理能力。 容量扩展用于单个区域容量不足（上限1万台）的扩容场景，旨在继续保持统一的云管理体验。 网络隔离用于DMZ区和内网区间的隔离，既在VPC并网方案基础上增加了一层安全保障，又支持批量并网保障了使用体验。 跨域计算用于有大数据任务跨Region联合计算需求的场景（数据全局共享无冗余，数据不移动，算力全局统一调度）。 全局统管支持统一运营、统一运维、统一监控、统一计量、统一开发等全局统管能力。 异构硬件 Region之间是逻辑耦合，物理隔离，单元支持部署与中心及其它Region不同的硬件（网络、服务器、芯片等），例如：部署为纯海光芯片Region以支持信创，部署RDMA网络以支持AI算力。

### 多Region的基本原则

专有云地域（Region）的设计旨在满足客户在多个地域部署云系统的需求。在云平台架构设计中，区域可分为中心Region和单元Region。 专有云多Region具有以下特点： 统一监管：云平台提供统一的管控、运维和监控服务。 一致性：与阿里云公共云的架构保持一致。 兼容性：向前兼容单Region的部署形态，向后支持多Region的扩展部署。 可用性：故障域隔离确保在中心Region出现故障时，不会影响云平台中已申请的云实例资源的正常使用。同时，当单元Region发生问题时，也不会对其他Region的使用造成影响。

### 多Region的设计概述

专有云产品的多Region设计需要考虑自身的特点，来决定多Region的部署形态。 仅部署在中心Region，暴露服务给单元Region，比如云平台底座组件Ram-master。 管控服务中心的部署应实施服务节点区域化。例如，在多Region 1.0架构下，ECS产品的业务逻辑层部署于中心，而ECS后端控制系统的各项服务则进行区域化部署。 完全Region化部署，例如RDS和Tablestore产品。 云产品的配置数据同步仅支持从中心Region向单元Region的同步，不支持单元Region向中心Region的同步，产品可以根据飞天基础运维平台从中心Region同步至单元Region的配置，进行反方向向中心的注册。 多Region的设计考虑向前兼容的问题。支持已部署局点兼容性升级。 不支持多Region的产品仅能够部署在中心Region，功能局限于中心Region内使用。 专有云产品架构层次分布以及多Region化的整体框架如下图所示。其中橘色代表中心化部署，蓝色代表 Region化部署。有部分产品的管控是中心化部署，服务是Region化部署的，具体参见中心Region跟单元 Region之间数据交互。 自专有云V3.18版本起，对部分平台基础服务及管控中心化部署的云产品实施了单元化下沉。此举使用户在访问单元实例时能够通过单元管控进行访问，从而提升用户访问速度，并增强故障场景下多Region的可用性。以下为V3.18版本实施单元化下沉的产品列表：

| 类别 | 产品 |
|---|---|

| 计算服务 | 云服务器ECS管控服务 |
|---|---|
| 弹性服务 | 弹性伸缩ESS管控服务、资源编排ROS管控服务、运维编排ACS管控服务 |
| 网络服务 | 负载均衡SLB管控服务、专有网络VPC管控服务 |
| 中间件云产品 | 企业级分布式应用服务EDAS管控服务 |
| 安全 | 密钥管理服务KMS（自v3.18.2开始支持） |
| 云管 | 运营控制台ASCM、运维控制台ASO |
| 底座组件 | OAM、Rule OMS（自v3.18.6开始支持） |
| 大数据 | MaxCompute、DataWorks、Abm |

在新部署V3.18及其单元化下沉后的场景中，SLB、ECS、VPC、EDAS、ESS、ACS、ROS这七款产品的管控服务与Worker服务均采用单元化部署。用户仅需通过这七款产品的单元管控来创建和查询资源， 从而有效利用单元的资源。 在从旧版本升级至V3.18版本的过程中，SLB、ECS、VPC、EDAS、ESS、ACS、ROS这七款产品的管控服务依然采取中心化部署，仅Worker服务实现单元化。单元所需的资源需通过这七款产品的中心管控进行创建和查询。 自v3.18.2版本起，KMS（密钥管理服务）实现了单元化部署。 在全新的部署场景中，如果某个Region内部署了KMS，则该Region支持数据加密；反之，则不支持数据加密。 在存量多Region的升级场景中，如果中心Region部署了KMS，则可以在单元部署临时KMS功能的情况下，单元Region继续使用中心Region的KMS服务，直到KMS以Region粒度完成单元化改造，以确保升级的兼容性。 自v3.18.6版本开始，大数据新增单元化部署形态。 MaxCompute 支持在单元部署管控+计算的混合集群 HybridOdpsCluster。 DataWorks 支持在单元部署为和中心相同的组件。 Abm、Hologres、Datahub 这三个产品的部署形态不发生变化，但需要通过一个集群变量 UseOdpsEngineCrossRegion 来选择是否与单元 MaxCompute、Dataworks管控联动（默认为 True，不联动），这三个产品需要在出朱雀规划时，将集群变量调整为 False。

### 多Region的整体架构图

多Region架构侧重云管控层面的统一，由一个中心进行统一管理、统一运维、统一计量等。 专有云多Region的整体架构如下图所示。 管控服务Apsara Uni-manager运营控制台在每个Region都会部署一套，中心Region的 Apsara Uni-manager运营控制台能够管控全部Region的资源，单元Region的Apsara Unimanager运营控制台只能管理本Region内的资源。 DataWorks的一级和二级调度网关服务部署在单元Region，以解决在多Region场景下的任务调度响应问题。其他组件中心化部署。 MaxCompute的管控集群中心化部署，服务节点单元化部署。 基础服务的读写服务部署在中心，单元Region的基础服务只提供读服务，相关的元数据库 （比如账号系统的元数据等）的同步通过DTS实现。单元Region只需要部署服务节点，由中心Region统一管控运维。

### 多Region架构的优势

多Region架构的优势主要体现在高可用性和可扩展性上。当一个Region发生故障时，其他Region内已经运行的服务实例大部分可以持续地提供服务，从而保证业务连续性。 故障域隔离可提供更高的可用性和业务连续性。在Region级别的故障情况下，受影响的业务仅限于本 Region内部，不会对其他Region的业务产生影响。当中心Region发生故障时，中心管控的服务将会中断，但单元Region已创建的资源实例将不受任何影响。单元Region可以通过降级方式恢复单元管控服务的正常使用。此外，在一些灰度发布、升级等场景中，将确保业务的连续性。 提供强大的可扩展性。可以通过新建单元Region的方式，轻松地提升服务能力。

### 多Region的适用场景

多Region架构提供了统一的能力，但并非扩容的万能解决方案。是否部署多Region应依据您具体的业务形态进行评估，具体分析如下： 存在对真实的统一管控、统一运维和统一监控的需求，物理和逻辑上均需设立一个中心节点。运维主体与运营主体均为该中心的核心。 由于许多产品的元数据存储在中心Region内，因此必须确保单元Region内的业务对存储在中心Region 内的元数据不敏感。 需要明确您的业务在各个Region间的调用需求，建议业务部署形态与产品的多Region部署形态保持一致，以避免产生过多的跨Region调用。

### 中心Region跟单元Region的区别

中心Region不仅承载类似单元Region的业务，还提供中心管控和中心运维等服务。 Apsara Uni-manager运营控制台的登录状态信息、Access Key、Account及RAM等服务的写入操作仅会在中心Region进行。当中心Region发生故障时，将会对新建Access Key、Account、RAM以及统一运维等功能产生影响。然而，通过在单元Region执行故障降级操作，用户的登录、利用Apsara Uni-manager 运营控制台访问资源、新建ECS实例及新建域名等操作将不受影响。单元Region内现有服务将保持正常运行（MaxCompute除外），用户仍可通过单元Region的Endpoint访问该Region的资源。

### 中心Region跟单元Region之间数据

**交互**

介绍各组件的部署方案以及中心Region和单元Region之间的数据交互。 多Region架构实现了云管控层面的统一。通过一个中心进行统一管理、统一运维及统一计量，部分产品的管控和运维采用中心化部署。除了中心Region内的相关产品调用中心Region的管控服务外，部分单元 Region内的数据也会回流至中心Region进行统一的处理。 底座基础服务中的DNS-api部署于中心Region。涉及域名申请、更新及删除操作时，均需调用中心的 DNS-api服务。更新后的数据将由中心Region同步至单元Region。 云平台账号体系（包括RAM、Access Key、Dauth）、位置服务（Location）、Rc-service服务、账号鉴权系统（OAM）、规则系统（RULE）以及CMDB等组件，虽然在单元Region中均有部署，但单元 Region的服务仅提供只读功能。所有新建及其他服务均调用中心Region的写服务，并通过DTS同步至单元Region。云平台账号体系（AAS）已实现完全单元化，单元的读写操作均可在单元Region内进行，AAS会将写请求路由至中心Region。AAS写入SSO Tair缓存，正常情况下通过中心Tair实现单点登录。当单元与中心断网时，运维操作将降级为写入单元Tair，以确保不影响用户登录。 基础中间件服务的JMENV服务部署于中心Region，负责记录各个Region内的VIPServer、Diamond、 MQ的IP地址及端口号。单元Region内的服务将调用中心Region的JMENV，以获取本Region的服务节点信息。同时，单元Region也将部署JMENV服务，正常情况下该服务不对外提供。当单元Region与中心 Region断开网络连接时，通过修改域名对应的VIP，单元Region内的服务将调用本Region的JMENV，以获取相关服务节点信息，从而有效规避JMENV中心化部署所带来的弊端。 大数据跨域计算形态，大数据服务MaxCompute及大数据开发环境DataWorks部署于中心Region，作为用户的统一入口。MaxCompute的管控节点位于中心Region，所有元数据均存储在中心的OTS-inner 上，包括表结构、实例及任务元数据等。单元Region则部署计算集群。 大数据单元化形态，大数据服务MaxCompute及大数据开发环境DataWorks以单元化方式部署，各 Region之间相互独立。MaxCompute的管控节点与计算节点部署在相同Region，元数据存储在本 Region的OTS-inner上，包括表结构、实例及任务元数据等。暂不支持部署多计算集群。 Apsara Uni-manager运维控制台的控制台部署于中心Region和单元Region，中心Region的数据通过 DTS进行同步至单元Region。用户可以通过中心控制台或单元控制台分别访问中心或单元的云产品和服务。此外，中心的Apsara Uni-manager运维控制台还可以对各个Region内的云产品和服务进行运维管理。云监控实现了单元化部署，各个单元Region的监控数据将汇聚至本单元的云监控上。 管控平台Apsara Uni-manager运营控制台部署于中心Region和单元Region，中心Region的数据通过 DTS同步至单元Region。用户可以通过中心控制台或单元控制台分别访问中心或单元的云产品和服务。 此外，中心运营控制台亦可访问各个Region产品的相关管控域名等信息，从而实现管控通信。 在部署阶段，单元Region将从中心Region同步一些配置信息（主要是中心管控部署的产品）。另外，单元Region还会向中心Region注册一些单元内部的信息，以实现统一的管控与运维。 支持全局anytunnel_vip段的使用，Dauth-server将为单元Region的相关组件提供服务能力。

### 多Region产品支持列表

本文介绍专有云多Region支持的产品。 专有云企业版多Region支持的产品列表如下表所示。

| 类别 | 产品 |
|---|---|
| 云平台基础运维 | 飞天基础运维平台、Apsara Uni-manager运营控制台、Apsara Uni-manager运维控制台、云监控CMS、PaaS底座、ASD、混合云应用中心AHM、 Prometheus、PaaS管控平台ASAPaaS |
| 计算服务 | 云服务器ECS、飞天智能运维平台（cgw-bms）、服务器迁移中心SMC、弹性高性能计算EHPC、一站迁云服务中心APDS、运维编排OOS、无影云桌面 |
| 弹性服务 | 容器服务Kubernetes、弹性伸缩ESS、资源编排ROS、容器镜像服务ACR |
| 应用服务 | 日志服务SLS |
| 存储服务 | 对象存储OSS、表格存储Tablestore、文件存储NAS、表格存储OTS |
| 云数据库 | RDS for MySQL、RDS for PostgreSQL、PolarDB-O、RDS for SQLServer、 Proxy、Redis、MongoDB、云原生数据仓库AnalyticDB PostgreSQL版、云原生分布式数据库PolarDB-X 1.0、云原生分布式数据库PolarDB-X 2.0、DMS企业版、数据传输服务DTS、时序时空数据库TSDB、云原生数据仓库AnalyticDB MySQL版2.0、云原生数据仓库AnalyticDB MySQL版3.0、云原生数据仓库 AnalyticDB PostgreSQL版、图数据库GDB、Oceanbase、GPDB、数据库和应用迁移ADAM、云数据库HBase版、数据库自治服务DAS、数据库备份DBS、云数据库OceanBase |
| 网络服务 | 负载均衡SLB、专有网络VPC、Qitian、VPN网关 |
| 底座中间件 | Middleware-jmenv、Middleware-metaq3、Middleware-diamond、 Middleware-vipserver、Middleware-schedulerx、Middleware-dubbo、 Middleware-tair、Middleware-zookeeper |
| 中间件云产品 | MQ（调用taokeeper）、DNCS、中间件运维管控系统、DAuth、云服务总线 CSB、企业级分布式应用服务EDAS、GTS、ARMS、分布式任务调度平台 ScheduleX 2.0、API网关、CSB-COP、应用高可用服务AHAS、多活容灾 MSHA、消息队列Kafka版 |
| 大数据 | 大数据管家、DataQ、Hologres、关系网络分析、E-MapReduce、Quick BI、 Dataphin、大数据计算MaxCompute、DataWorks、实时计算、Datahub、机器学习（传统PAI/EAS/深度学习）、DataV数据可视化、Elasticsearch |

| 基础服务 | OPS（DNS、YUM、NTP）、OTS-inner 、DMS、POP、Rule、Tag、Https- proxy、OAM、Baseservice-AAS、Baseservice-UMMAK、RAM-master、 RAM-slave、RAM-STS、Baseservice-Location、Baseservice-rc、OMS、 FTP、LicenseManager、Skyline、Permissions-boundary |
|---|---|
| 安全服务 | 云盾高级版、密钥管理服务KMS、云盾-堡垒机（bastionhost）、云盾-网络检测与响应（beaver）、云盾-云防火墙（cfw）、云安全中心（安骑士）（aegis）、 云安全中心（态势感知）（sas）、Web应用防火墙（waf）、云盾基础版 （yundun）、加密服务（hsm）、敏感数据保护（sddp）、数据库审计 （dbaudit）、应用身份服务（idaas） |
| 域名解析服务 | 域名解析DNS |
| 容灾服务 | 同城容灾管理平台ASR、异地容灾管理平台ASR-DR、备份管理平台ASR-BR、混合云备份服务HBR |

架构

## 产品多Region架构

### IDC基础组件

专有云的基础组件主要包含了DNS、YUM服务、NTP服务。 图 1. 基础组件部署方案 DNS服务：提供统一域名注册解析服务。 YUM服务：提供了YUM源的下载服务。 NTP：提供了统一的时钟服务。 基础组件在每个Region内均会单独部署一套，其中DNS（解析服务）、NTP和YUM服务通过Anycast方式进行对外路由（全局Anycast VIP）。在正常情况下，每个Region的访问请求流量将被引导至本Region内的DNS、NTP和YUM服务器，具体路由将由BGP路由长度决定。 当任一Region内的服务发生故障时，该Region的访问请求流量将自动根据路由切换至另一Region的服务器，以提供更高的基础组件服务可靠性。在多Region场景下，OPS-DNS的注册服务仅部署于中心 Region。所有注册请求均需调用中心Region的DNS-Master服务进行域名注册，随后将更新的数据通过 DNS Bind同步协议实时同步至各个Region的解析服务（DNS-Slave）。此流程确保在多Region场景中， 应用能够通过一套DNS系统完成注册服务。因此，中心Region与单元Region内的域名必须能够相互区分。 此外，云平台OPS组件提供了租户级访问能力，因此各类型VPC网络的ECS可以通过VPC direct_anytunnel访问OPS服务（需注意YUM服务为特殊情况）。在技术实现上，云平台用户对此过程是透明的。

### 产品多Region部署方案

#### 概述

介绍产品的部署形态。 产品多Region的部署形态主要分为三大类，包括： 完全实现单元化部署，各个Region之间不存在关联。 保留了中心化管理的部署方式，服务节点需在各个Region内部署，由中心管理节点进行统一管控。 单元化部署的情况下，单元内部的服务仅提供只读功能，写入服务需通过中心进行调用，随后再同步回单元内部。 架构

#### Tianji和PaaS底座

Tianji是一套自动化数据中心管理系统，管理数据中心的硬件生命周期与各类静态资源，为各种云产品应用及服务提供通用的版本管理、部署、热升级方案。

**Tianji底座**

为了使基于Tianji的服务在大规模分布式环境中实现自动化运维，提高运维效率并增强系统可用性，每个 Region需部署一套Tianji服务。由于中心Region的服务变量需要被单元Region所感知，因此在单元 Region的bootstrap阶段，Tianji将同步中心Region的服务变量，以便供单元Region上的产品或服务进行引用。 Tianji的多Region方案通过新增一个CenterRegionSync服务实现，该服务将被部署到每一个单元 Region上。CenterRegionSync负责获取中心Region的服务变量，并将其同步到本Region内部。 Tianji运维平台的监控服务及其依赖的产品（OTS-inner和SLS-inner）在每个Region内独立部署，各 Region的运维监控数据仅会上报至本Region内的Tianji运维平台。 除了Tianji形态接入外，企业版引入了PaaS底座，部分底座服务及产品已迁移至PaaS平台，依赖PaaS平台进行规划和部署等操作。 中心Region需要将其变量同步到单元Region，该处理动作为单元Region从中心Region进行拉取。涉及到以下两个层面的变量同步： PaaS底座单元Region跟中心Region PaaS底座的变量同步。 PaaS底座跟本Region内的Tianji变量同步。

#### 平台基础中间件组件

平台基础中间件包括：Java应用地址服务（JMENV）、Diamond（配置管理系统）、Metaq和软件负载均衡系统（VIPServer）。 JMENV服务部署在中心Region，为各Region内的Diamond（配置管理系统）、Metaq和软件负载均衡系统（VIPServer）提供服务地址查询功能。JMENV会根据源IP信息所属的Region，返回该Region内相应的Diamond（配置管理系统）、Metaq和软件负载均衡系统（VIPServer）的服务地址。 如果单元Region所依赖的中间件服务已经完成部署，并且已经从JMENV获取了相关的服务地址（客户端缓存），那么即使与中心Region断网，在不重启的情况下，也不会影响正常使用。 JMENV也部署在单元Region中，通常情况下不对外提供服务。当单元Region与中心Region断网时，可以通过切换域名对应的VIP来指向单元JMENV服务，即便在重启的情况下，也不会影响正常使用。 Metaq、Diamond（配置管理系统）、软件负载均衡系统（VIPServer）、Tair、分布式任务调度系统 （SchedulerX）、分布式服务框架（Dubbo）、Zookeeper、中间件Redis、云服务总线（CSB）、分布式命名和配置服务（DNCS）、中间件账号服务（Dauth）均在每个Region独立部署。其中，中心 Region内的Dauth服务提供写入功能，而单元Region内的Dauth服务仅提供只读功能及鉴权服务。中心 Region与单元Region之间的数据通过DTS进行同步。

#### 平台基础服务

平台基础服务主要包括账号认证服务（AAS、UMM/AK、RAM-master、RAM-slave、RAM-STS、 OAM）、产品集群位置服务（Rc-Location）、标签服务（Tag）、规则服务（Rule）、网关服务 （POP）、元数据库备份服务（FTP）以及LicenseManager服务。

**账号认证服务**

架构账号认证服务在每个Region部署一套，但仅中心Region的账号认证服务提供写入功能，单元Region仅提供读取功能。因此，在产品运行期间，对于AK、RAM-slave、RAM-STS和Location的读取服务，必须依赖于所在Region的服务。否则，在多Region形态下，中心Region与单元Region之间的专线故障、 网络抖动或中心Region故障，可能会导致产品在单元Region内的功能不可用。 在多Region场景下，需对账号服务的元数据库初始化过程进行改造。中心Region的初始化流程保持不变；在单元Region初始化时，需要从中心Region的元数据库中同步相关数据。具体流程依赖于中心 Region内部署的DTS服务，创建相应的元数据库实例同步任务，通过四元组 （IP+Port+User+Password）将对应的元数据同步至单元Region的账号服务元数据库，涵盖全量与增量的处理。 账号认证服务所依赖的数据是通过中心Region的DTS服务同步至单元Region内的。在单元Region部署账号服务时，数据库的初始化过程是通过调用中心的DTS服务，与中心数据库进行全量或增量同步。 当单元Region与中心Region的网络连接中断后，查询功能仍然可以正常运行，但无法执行新建操作。

**规则服务**

规则服务（Rule）用于存储一些定义的规则，例如ECS的密码规则等。其部署方式为每个Region各自部署一套规则服务，但仅中心Region的规则服务提供写入功能，而单元Region仅提供读取功能。单元 Region的数据依赖于中心Region的DTS服务同步至单元Region。 规则服务（Rule）故障时，不会影响产品对外提供服务。当单元Region与中心Region的网络连接中断后，单元Region无法向中心Region的规则服务写入数据，但仍然可以读取本单元Region的规则服务数据。

**Tag、POP**

标签服务Tag和网关服务POP均采用完全单元化部署。当单元Region与中心Region的连接中断时，POP和 Tag仍能够正常运行。

**FTP**

元数据库备份服务FTP为每个区域内的miniRDS提供独立的备份服务。

**License Manager**

License Manager提供如下功能： 提供现场云产品的授权数量与合同中规定的授权数量进行比对的能力。 提供某些产品的授权类开关信息的能力。 对某些按套售卖的产品，若产品中包含授权规格，则需对规格的实际使用状况进行交互，以实现对规格上限的控制。 License Manager采用多Region完全单元化部署。

#### 管理与计量产品

介绍Apsara Uni-manager运营控制台和计量服务OMS的多Region部署方案。 Apsara Uni-manager运营控制台将在中心Region和单元Region各自部署服务，既提供中心Region内的统一管理能力，也支持单元Region的管理能力。中心Region的管控平台能够管理所有Region的资源，而单元Region的管控平台仅能管理本Region的资源。在中心Region的管控平台出现单产品服务宕机的情况下， 单元Region的管控平台仍可对外提供服务。然而，一旦单元Region与中心Region断开连接，单元Region 内的管控平台将无法登录。 阿里云开放计量服务（OMS）部署于中心Region，各个Region内的计量数据通过POP或REST API统一推送至中心Region内的OMS服务。当单元Region与中心Region的连接中断时，断网Region将无法推送计量数据。 CMS云监控服务负责收集存储租户ECS、RDS、SLB和OSS的监控数据，提供租户侧实例的监控能力，完全单元化部署，每个Region内的监控数据汇总到本Region的CMS。 架构

#### 网络产品

网络产品包括负载均衡产品SLB、私有虚拟网络VPC以及SLB/VPC运维管控系统。 SLB-yaochi、VPC-yaochi和ECS-yaochi均采用单元化部署（包括inner-api、open-api等服务）。在此架构中，中心yaochi仅负责处理中心Region的资源，而单元yaochi则处理单元Region的资源。当单元 Region与中心Region的连接中断后，单元Region的业务逻辑层仍可正常运行，能够获取单元实例，且已有实例同样不受影响。

#### 数据库产品

本文介绍数据库的多Region部署方案。 以下产品均为Region化部署，数据库账户认证依赖Region内的业务基础服务。当单元Region跟中心 Region连接中断后，已创建的数据库实例可以正常工作，且断网Region内新建数据库实例，RDS运维管控系统登录，在断网Region执行降级运维动作后可操作。 RDS PostgreSQL RDS SQL Server RDS MySQL PolarDB 云数据库Redis版云数据库MongoDB版云原生数据仓库AnalyticDB PostgreSQL版云原生数据仓库AnalyticDB MySQL版2.0 云原生数据仓库AnalyticDB MySQL版3.0 云数据库TSDB 图数据库GDB 云数据库OceanBase版 RDS运维管控系统

**DMS**

数据库管理系统DMS专有云的多Region架构跟阿里云公共云类似，服务单元化部署，实例信息存储在中心 Region的元数据内，给中心Region以及单元Region提供统一的数据管理服务。当单元Region跟中心 Region的连接中断后，会导致断网Region的DMS控制台无法登录。

**DTS**

数据传输服务DTS，DTS的管控服务部署在中心Region， DTS的读写服务在每个Region都支持部署。

**PolarDB-X**

云原生分布式数据库PolarDB-X作为分布式关系型数据库服务在多Region场景完全单元化部署。

**OceanBase**

架构 OceanBase的默认多Region部署形态如下图所示。

#### 弹性计算产品

介绍ECS、容器服务、资源编排、弹性伸缩、飞天智能运维平台（Cgw-bms）、服务器迁移中心SMC的多 Region部署方案。

**ECS**

ECS的业务逻辑层管控服务、ECS运维管控系统以及ECS后端控制系统均采用Region化部署。中心与单元各自负责管理本单元的资源及运维服务。 当中心Region发生故障时，自定义镜像和云盘快照因无法创建OSS Bucket而变得不可用，而ECS的其他运营和运维能力则不受影响。 ECS的多Region部署示意图如下图所示。 架构

**容器服务**

在中心Region和单元Region均部署容器服务的管控服务，中心Region与单元Region的功能相同。容器服务负责在中心Region管理中心的K8s集群，并在单元Region管理单元的K8s集群。

**资源编排ROS**

在中心Region和单元Region部署Ros-server以及Ros-notify，各单元业务仅调用本单元的ROS。 ROS的部署架构如下图所示。 架构

**弹性伸缩ESS**

在中心Region和单元Region中分别部署ESS管控集群，各单元的业务仅调用其本单元的ESS。 飞天智能运维平台飞天智能运维平台基于阿里云的基础设施管理实践，在阿里云数据中心隔离区域为用户提供与公共云一致的专有基础设施即服务体验。该平台支持多Region场景下的完全单元化部署。 服务器迁移中心SMC 服务器迁移中心（SMC）能够方便快捷地将其他任意平台的服务器系统迁移至阿里云，包括IDC 服务器、虚拟机、云主机等几乎所有服务器平台。 在多Region场景下，SMC部署于中心Region，通过中心Region的管理向各个Region下发迁移任务。

#### 存储产品

介绍对象存储OSS、表格存储Tablestore、文件存储NAS和日志服务SLS的多Region部署方案。

**对象存储OSS**

对象存储OSS在中心Region部署一个全局OCM，以确保命名的唯一性（OSS bucket要求全局唯一命名）。各个Region独立部署存储服务及区域化的OCM。因此，OSS bucket的创建依赖于中心的全局 OCM，而查询服务则依赖于本Region内的OCM服务。当普通Region与中心Region的连接中断后，将无法创建新的bucket，但已创建的bucket服务不会受到影响。

**表格存储Tablestore**

架构表格存储Tablestore采用Region化独立部署，各个Region内都可以独立创建Tablestore实例，当单元 Region跟中心Region连接中断后，服务不受影响。

**文件存储NAS**

中心Region和单元Region均部署了管控集群和标准集群（或性能集群）。NAS系统实现了完全的单元化， 当单元与中心断网时，已有实例的运行、实例的创建以及使用均不受影响。

**日志服务SLS**

日志服务的多Region架构在设计时充分考虑了和公共云架构的一致性、兼容性和用户体验。 中心Region部署管控模块SCMG，用于Project的唯一性校验，以及向各个Region的SLS服务集群同步账号信息。 各Region部署独立的SLS服务集群，用于日志的存储、查询和分析。

#### 大数据产品

介绍大数据的多Region部署方案。 中心化部署，采用该部署形态的产品包括： Quick BI 各个Region独立部署，采用该部署形态的产品包括： 数据总线Datahub 大数据管家ABM Dataphin 实时计算全文搜索引擎Elasticsearch 大数据计算MaxCompute（单元化形态） 大数据开发平台DataWorks（单元化形态） 交互式分析Hologres 架构

**说明**

Hologres依赖DataWorks，因此当单元Region跟中心Region连接中断后，大数据跨域计算形态，该Region内已创建的Hologres实例资源无法使用；大数据单元化形态，Hologres不受影响关系网络分析各Region独立部署的场景中，当单元Region跟中心Region连接中断后，已有的服务不受影响，但是无法登录控制台。 Portal组件部署在中心Region，服务节点部署在单元Region，采用该部署形态的产品包括： API网关 DataQ 机器学习PAI的Portal组件、EAS、深度学习控制集群中心化部署，计算集群每个Region独立部署，采用该部署形态的产品包括： 大数据计算MaxCompute（跨域计算形态）。当单元Region与中心Region的连接中断后，断网 Region的计算节点将脱离管理，同时相应的计算任务出现异常。 大数据开发平台DataWorks（跨域计算形态），DataWorks会统一管理各Region的MaxCompute的 Projects。当单元Region跟中心Region连接中断后，中心Region无法向断网的单元Region下发任务。

#### 中间件产品

企业级分布式应用服务EDAS：各Region部署管控服务和服务节点。EDAS依赖的中间件运维管控系统和 DAuth（中间件认证服务，中心Region的DAuth服务提供写能力，单元Region的DAuth只提供鉴权能力） 部署在中心，依赖的DNCS和数据收集系统（Tlog）部署在各个单元Region。当单元Region与中心Region 连接中断后，断网Region已经存在的基于EDAS部署的应用无影响，并且断网的单元可以获取本单元 Region的实例。 消息中间件MQ、中间件缓存Redis（EDAS和CSB依赖）、Taokeeper、云服务总线CSB、全局事务服务 GTS、ScheduleX和应用实时监控服务ARMS均为Region化部署，各Region完全独立，即使单元Region 与中心Region连接中断，各断网Region内可以正常提供服务（CSB新建服务受影响）。

#### 安全产品

介绍安全产品的多Region部署方案。 安骑士Aegis采用区域化部署，各Region内的ECS上的安骑士代理将连接至本Region的安骑士服务端。 当单元Region与中心Region的连接中断时，单元Region内主机的安全防护仍可正常运行。 云盾高级版及密钥管理服务KMS均为区域化部署，断网情况下不受影响。

#### 基础运维产品

基础运维包含了云监控、 Apsara Uni-manager运维控制台、ASD（Apsara Stack Doctor）和运维编排 OOS。 云监控采用单元化部署方式，每个单元Region将部署相应的数据收集代理服务，以将相关监控数据上报至本Region内的云监控服务。 架构 Apsara Uni-manager运维控制台实现了单元化部署。在中心Region，Apsara Uni-manager运维控制台能够管理所有Region的资源；而单元Region的Apsara Uni-manager运维控制台则仅限于管理本 Region的资源。 ASD已实现完全区域化部署。 运维编排OOS采用中心化部署。

#### 租户侧域名解析服务

介绍专有云DNS的多Region部署方案。 专有云DNS是运行于阿里云专有云环境中的一套租户侧DNS产品，旨在为专有云环境提供域名解析服务。 租户侧DNS通过配置域名与IP地址的对应规则和策略，可以将来自客户端的域名访问请求重定向至云平台内的云资源、云平台内或企业内网的业务系统，以及互联网服务提供商的服务资源等。 专有云DNS通过Anycast技术提供解析服务，解析服务实现单元化部署，而管控服务则部署于中心 Region。 用

## Region级高可用

多Region架构提供更高的可用性和故障域隔离，Region级的故障不会影响其他Region的服务。 可用性和Region级故障影响范围如下表所示。

| 业务影响 | 中心Region故障 | 单元Region故障 |
|---|---|---|
| 运营工具（Apsara Uni-manager 运营控制台） | 降级后单元可登录、可运营 | 除故障单元Region，其他均可用 |
| 运维工具（Apsara Uni-manager 运维控制台） | 降级后单元可登录、可运维 | 除故障单元Region，其他均可用 |
| 新建Access Key和Account | 不可用 | 除故障单元Region，其他均可用 |
| 产品管控单元化部署 | 单元可用 | 除故障单元Region，其他均可用 |
| 产品管控中心化部署 | 不可用 | 除故障单元Region，其他均可用 |
| Open-API运维 | 单元可用 | 除故障单元Region，其他均可用 |
| Open-API | 单元可用 | 除故障单元Region，其他均可用 |

**中心Region故障**

中心Region除了提供类似单元Region服务外，还承载中心化产品管控、运维等服务。部分云产品管控服务部署在中心Region，Access Key和Account等写服务仅在中心提供，因此当中心Region故障后，会影响用户的登录、影响用户使用中心化产品管控管理资源、影响新建Access Key和Account、影响单元Region 内的大数据（跨域计算形态）计算任务的运行等。基础IAAS、数据库、中间件、安全、大数据（单元化形态）等云产品已经下沉到Region内部，所以不会影响单元Region内对已有资源实例的调用，用户可以通过单元Region的Endpoint去访问Region内的资源（例如：rds.cn-example.aliyuncs.com ），不影响单元 Region内的已有服务；在多Region 2.0架构下，单元故障降级后，单元Region的绝大部分云产品管控可恢复使用（具体限制详见云产品管控恢复限制详情）。 图 1. 中心Region故障场景用备注：升级到v3.18.2且为多region2.0架构，单元故障降级后，云产品管控恢复限制详情如下表：

| 功能类别 | 单元故障降级后，受影响功能 |
|---|---|
|  | ECS-IMAGE：上传自定义镜像失败。 ROS：创建ram、accesskey、oss不可用。 ACS：创建K8s集群不可用。 ACR：跨云镜像复制功能不可用。 EBS：新增块实例创建快照失败，存量块实例首次创建快照失败。自动快照策略设置的云盘，无法自动创建快照。 OSS/CDS：创建 bucket失败。 SLS/CDS：创建 Project 失败。 SLB：七层日志设置时，创建Project 不可用。 DMS：不可用。 RDS：通过DMS登录数据库不可用。 Edas：账号、命名空间、HSF服务分组、K8s 应用无法创建，未登录EDAS控制台的组织断网之后无法登录。 CSB：实例部署不可用。 MQ、MQTT：无法创建实例、topic和订阅组gid。 Tlog：需要登录跳转一次，后面在断网的时候，才能正常登录。 Prometheus：新建一级组织，需要登录一次控制台触发授权，后续断网才能正常使用。 ASCM： 概览页中，资源使用率排序不可用； 无法创建、删除RAM子账号； 无法为RAM子账号开启、关闭控制台登录； 无法修改RAM子账户登录配置； 无法修改RAM子账户密码； |

用

| 运营控制台 | 无法创建、修改、删除RAM用户AK； 无法创建、更新、删除RAM Role； 无法为RAM Role绑定Policy； 无法为RAM User绑定、解绑RAM Policy； 无法创建、删除RAM Policy、RAM Group； 无法从RAM Group上添加、移除RAM User； 无法从RAM Group绑定、解绑Policy； 无法创建、删除PolicyVersion； 无法为用户绑定、解绑MFA设备； 无法创建、删除MFA设备； 无法创建云账户； 无法更新云账户密码； 无法删除云账号的指定AccessKey； 无法更新AccessKey状态； |
|---|---|
|  | ASR：不可用。 ASR-DR：不能新增数据库类的同步实体。 ASR-BR： 存量租户使用过ASR-BR： 未使用过存储类相关功能，则存储类相关功能无法使用。 未使用过OSS备份的清单功能，则OSS备份无法使用清单备份。 未使用过ADB备份，ADB备份恢复无法使用。 大数据（MaxCompute）备份和恢复无法使用。 存量租户未使用过ASR-BR： 控制台无法使用产品。 |
| 运维控制台 | ASO： 用户、权限等无法创建。 AK轮转不可用。 单元无法开启和关闭国密功能。 check region listbucket 告警缺失。（赤骥） _ _ Tianji底座：导终态失败，无法增量部署和升级。 PaaS底座：无法增量部署产品，无法Rolling已有集群。 |

**单元Region故障**

单元Region故障时，不会影响用户的登录，不会影响用户使用Apsara Uni-manager运营控制台管理资源，不影响新建Access Key和Account，不影响运维服务。中心Region跟其他单元Region的已有服务和新建服务都不受影响。 图 2. 单元Region故障场景用架构

## 多Region网络架构

在多Region场景下，各个Region的物理网络通过ISW实现互联，经典网络之间实现互通，IP地址互不冲突。 多Region的网络架构如下图所示。 两个Region的ISW之间通过专线分别连接。 两个Region的ISW、DSW、LSW、CSW使用不同的BGP AS号。 两个Region的ISW之间配置EBGP，不加路由限制。 单元Region和中心Region平台管控侧的流量带宽需超过1Gbps，延迟必须控制在80毫秒以内。 中心Region跟单元Region之间的流量主要包含以下几种流量： 基础服务的同步任务流量以及OPS-DNS的注册服务流量。 管控在中心Region，服务节点在单元Region导致的任务下发流量。 服务节点向中心汇报的流量，比如MaxCompute计算节点向中心MaxCompute的管理节点汇报计算状态。 跨Region的VPC高速通道流量与具体的业务形态有关。 Apsara Uni-manager运营控制台、OMS、云监控等中心化部署的业务，需要从单元Region收集信息。 跨Region的RDS（依赖于DTS）、OSS数据复制流量，根据用户实际使用情况决定。

## 使用限制

### 多Region的部署限制

介绍多Region场景的部署限制。 多Region的部署形式为先在中心Region进行部署，随后再部署单元Region。在部署单元Region之前， 必须提前完成经典网络的并网互通。 请确保中心Region的DNS、NTP和YUM采用Anycast架构。多Region部署对OPS组件（DNS、NTP和 YUM）的Anycast架构有强烈依赖。如果中心Region不是全新部署，而是从V3.6.0之前的版本升级而来，则在部署单元Region之前，需提前将中心Region的DNS、NTP和YUM改造为Anycast架构。 中心Region必须部署DTS产品，因为单元Region内基础服务等资源的元数据（RAM、Access Key、 Location、RC和DAuth）依赖于中心Region部署的DTS服务进行同步。此外，在单元Region相关产品部署完成后，建议提前检测同步任务的正常运行情况。在多Region的日常运维工作中，需要定期检查 DTS同步任务的状态，并关注相关的任务告警信息。 企业版V3.12.0版本之前，单元Region规划后，需要先对中心Region内的JMENV的配置进行变更，补齐单元Region的IP访问网段以及单元Region内的Diamond、 Configserver、 MQ和VIPServer的地址。 任何一个Region如果涉及容器段、物理机网段的扩容，都需要更新JMENV的配置，详细请参见JMENV变更文档（标准KB文档或对应版本**《部署指南》**中**《多****Region**的**jmenv****初始化配置》**章节）。企业版 V3.12.0及后续版本优化了JMENV的自动化配置，无需进行此操作。 多Region的经典网络和BGP AS号必须统一规划。不同Region之间互不相同，以便经典网络互通。 不支持多个云实例合并成一个多Region的场景，主要原因如下： 多个云实例账号体系彼此独立，暂不支持合并为统一的账号体系。不同产品之间存在依赖关系，在部署过程中会将账号耦合到配置中。此外，各云内的元数据库包含大量自增主键，无法通过数据修正来实现统一。平台内的一些内部运维域名是固定的，例如YUM和DNS等，无法进行合并。在多个云实例形态下，产品域名均为中心化申请，修正难度较大且无法保证业务的连续性。 单元Region需要从中心Region同步配置，多个云实例不支持配置同步。 多个云实例的元数据无法同步，多Region部署场景中部分产品管控是中心化部署，元数据库保存在中心Region。 产品级限制，例如OSS要求全局Bucket名字唯一。 无法确保合并过程以及热升级过程中的配置有效。 多个云实例IP独立规划无法保证多Region统一规划要求，包括DNS、NTP、YUM的Anycast IP。 不支持多Region拆分成多个独立的云实例。 单元Region的部署与扩容将对中心Region的管理产生一定的负载，因此在部署时需予以关注。如果规划的单元Region数量较多，例如超过10个，建议中心Region采用大规模部署形式。 产品部署形态上，部分产品在单元Region部署时需要依赖中心Region的部署，例如管控需要部署在中心 Region等。 单元region无法升级为中心region：由于单元region在服务部署、配置等方面与中心region存在差异， 因此无法通过运维等手段将其升级为中心region。

### MaxCompute的使用限制

本文介绍MaxCompute多Region部署时需要满足的要求。 MaxCompute多Region部署时需要满足如下要求： MaxCompute控制集群应与基础服务DNS和Tablestore部署在同一机房，并确保网络延迟在5毫秒以内，因为MaxCompute控制集群对网络延迟具有较高的敏感性。 集群之间的网络能够实现互通，且集群内部及集群间各机器的时钟保持一致。 在多Region场景下，需确保中心Region与计算Region之间的同步升级。此处的同步升级指的是在 MaxCompute的升级过程中，使用MaxCompute内置工具进行更新。 在多Region场景下，计算Region与中心Region的操作系统必须保持一致。若存在不一致，可能导致兼容性问题，需进行扫描以确认。 在升级场景以及正常运行MaxCompute任务时，中心Region与计算Region之间的带宽要求为50 MB/s，网络延迟应控制在80毫秒以内。 管控集群部署于中心Region，若单元Region与中心Region断网，将导致单元Region内的计算集群失去管理，进而引发单元Region内的计算任务异常。

### 多Region高可用说明

本文介绍如何提升多Region架构下中心Region和单元Region的可用性。 在多Region架构下，账号体系、域名服务、部分产品的管控服务以及Apsara Uni-manager控制台均依赖于中心Region的服务可用性。若中心Region发生故障，会对专有云的管理与运维产生影响，例如无法新建实例。为缓解此类影响，可以通过运维手段对单元Region进行降级，从而恢复90%以上的运营和运维能力。然而，已有的MaxCompute实例服务将受到影响，并且无法通过降级进行恢复。若您对业务连续性有极高的要求，建议在中心Region实施同城容灾架构，以进一步提升中心Region可用性。 如果单元Region需要确保业务连续性，则可以采用同城容灾架构，以提升单元Region的可用性。

### Region级别资源隔离

多Region设计的本质是为了解决统一性的问题。然而，在实际客户的应用场景中，资源隔离的需求依然存在。例如，各个Region的资源并不一定需要完全开放给其他Region，并且在多Region环境下，账号也具有 Region属性。为了实现Region级资源隔离，专有云的多Region设计可以通过在Apsara Uni-manager运营控制台上修改组织与Region的映射关系来完成。

### Region间按需放通

多区域之间的网络默认全面放通。出于安全考虑，您也可以选择按需放通。

**Region间放通策略概述**

阿里云专有云网络架构整体分为经典网络与VPC网络。云平台侧网络（underlay网络）采用经典网络， 云平台的管控与服务依赖之间通过RPC（远程过程调用）和HTTP方式进行调用。租户侧网络（overlay网络）则采用VPC网络。经典网络与VPC网络属于不同层面的网络，两者之间默认是隔离的。 多Region通过云平台实现统一管理，云平台内的资源默认支持共享与互通，例如MaxCompute的跨 Region协同计算能力及OSS的跨Region复制能力等。为了提供统一视角，多Region之间的网络设计要求平台侧的网络默认全量放通，即经典网络全量放通，以支持多Region的统一管控、运维及监控能力。 部分客户现场由于安全管控的需求，需要将多Region之间的默认全量放通调整为按需放通，以降低安全风险。建议按需放通采取基于IP网段和端口范围的方式，不建议执行精确放通。如有精确放通的需求，请联系驻场运维工程师。

**按需放通的风险**

阿里云专有云作为原生云架构，其服务化程度非常细致，导致内部应用与组件数量众多，调用链路也非常复杂。因此，梳理相应的IP+端口放通策略，使得运维工作量显著增加。 产品应用与组件的IP由朱雀进行规划，而VIP则通过飞天基础运维平台动态申请。这部分的放通依赖于环境的真实资源状况。 交付部署阶段配置按需放通策略后，涉及如下场景的运维时，还需要更新配置按需放通策略： 单元Region新增部署的产品。 重新部署产品和集群。 单元Region内的产品集群的扩容和缩容。 客户业务层面的互通需求，例如OSS跨域复制、RDS实例同步等。 理论上，所有涉及Region间互访的运维变更操作均需梳理相应的IP及端口并进行放通。这项运维工作量极为庞大。在严重情况下，可能会引发故障，因此在前期必须明确放通需求。 云

## 多Region与多云

本文介绍多Region和多云的概念，以及多Region和多云在各业务场景的优劣对比。 多Region的架构是在确保“统一”的前提下，实现各单元Region部分自治的能力。多云环境是完全独立的云系统，各云系统之间没有任何联系（除非业务侧按需打通）。因此，需要根据客户的业务需求选择合适的架构。 如果客户拥有一个强中心的管控组织，需要对所有Region内的资源进行统一的管控和运维，或者采用行业公共云的形态（服务售卖方式），建议选择多Region架构。 如果客户的云服务使用方与运维主体为不同组织，且组织之间的关系相对松散，安全等级存在不一致，并且对可用性和隔离性有较高要求，建议选择多云架构。 下表是多Region和多云在各业务场景的优劣对比。

| 业务场景 | 多Region | 多云 | 优选方案 |
|---|---|---|---|
| 中央统一管理 | 支持统一账号和授权、统一云管理、 跨区域网络VPC并网简单。 | 可开发，做账号体系映射和多云统一管理，云实例越多越复杂。 | 多Region |
| 区域自治管理 | 具备一定程度的区域自治能力，租户和运维方面均从账号和资源授权的维度对Region进行绑定。 | 支持 | 多云。多 Region也可支持，业界友商也有实现。 |
| 数据中心间异地灾备 | 由于多Region有中心Region， 因此要求中心Region做同城容灾，Region间做异地灾备，最小机房数为3。 多Region存在中心Region，当中心Region故障，单元Region 功能降级。多Region架构本质不提供容灾。 | 异地两个机房时，推荐用跨云灾备，保持主备云的平台独立性和业务灾备。 当需要有灾备能力的机房数量多时，不推荐，跨云数据流动受权限账号影响变得复杂。 | 根据实际场景选择： 异地机房多时，优选多 Region（中心同城容灾 +跨Region 灾备）。 异地两机房时，选择异地跨云灾备。 |
| MaxCompute 跨域计算调度 | 支持 | 不支持 | 多Region |
| RDS或OSS跨域复制 | 支持 | 需要手动打通，包括并网，同步任务配置等。 | 多Region |

云

| 云实例部署和运维 | 支持统一运维和Region化运维能力。扩建、下线、搬迁和升级比多云复杂： 扩建：必须要求中心Region先建，再扩建新机房，不支持把已有云实例合并。 下线和搬迁：多Region间有联系，需要技术手段操作。 升级：多Region场景升级稍微复杂，但基本可以实现按Region维度升级。 | 跨云访问实现复杂，运维工作量较大。扩建、下线、搬迁和升级相对简单： 扩建：独立机房建设，理论上多机房间不需要版本一致（有跨云功能依赖的除外，如灾备）。 下线和搬迁：单实体，机房间依赖低。 升级：单实体升级，机房间依赖低。 | 多云 |
|---|---|---|---|
| 机房间网络安全隔离 | 机房间管理流量和业务流量多，存在如下限制： 对于存在不同安全等级或区域， 需要实现网络强隔离的场景，因网络不通，无法进行建设。 在需要实现网络受限访问及防火墙白名单通行的场景中，安全管理成本较高。 | 机房间管理流量和业务流量少，不同机房间流量互访按客户业务需求，跨云网络流量可控性好于多Region。 | 多云 |
| 成本对比 | 包含如下费用： 管控一套。 云产品各机房按需采购，部分产品中心化部署，在中心Region共用。 硬件每个机房一套。 | 包含如下费用： 管控多套。 云产品各机房按需采购。 硬件每个机房一套。 | 多Region成本略优于多云。 |
