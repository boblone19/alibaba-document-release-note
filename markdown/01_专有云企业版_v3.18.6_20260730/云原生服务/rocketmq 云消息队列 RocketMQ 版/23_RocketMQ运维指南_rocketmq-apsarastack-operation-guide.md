---
title: "云消息队列 RocketMQ 版 RocketMQ运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 54
source_pdf: "23_RocketMQ运维指南_rocketmq-apsarastack-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/rocketmq/zh/rocketmq-apsarastack-operation-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云消息队列 RocketMQ 版 RocketMQ运维指南

消息队列

## 运维概述

本文介绍消息队列RocketMQ版（简称RocketMQ）的产品架构和运维架构。

### 系统架构

本节内容旨在帮助您在运维过程中了解RocketMQ的系统架构和其中包含的各组件。 RocketMQ主要由RocketMQ服务发现节点、RocketMQ数据节点、RocketMQ鉴权节点、RocketMQ配置中心、Tlog、RocketMQ高可用节点等系统模块组成。 图 1. RocketMQ系统架构图各模块和组件的介绍如下：

**RocketMQ服务发现节点**

RocketMQ服务发现节点由Name Server和Cai组成。 Cai主要用于Name Server和Diamond的地址发现。调用方通过Cai获得地址，并在本地缓存地址列表。 Name Server主要负责消息队列服务的注册与查找，是实现消息队列服务弹性部署和线性扩展的核心。 RocketMQ Broker会把消息队列服务注册到Name Server并把Broker的状态同步到Name Server中。生产者与消费者通过Name Server来查找到具体的Broker。在已启动的生产者与消费者在建立与Name Server的连接后，会缓存Broker与消息队列的信息，并周期性地从Name Server更新缓存信息。 消息队列服务器（RocketMQ Broker）是消息队列的核心处理模块，由多个服务节点组成服务集群，支持集群化、多副本部署，主备复制实现高可用。它提供高可用、稳定高效、可线性扩容的消息服务能力。 RocketMQ Broker管理Topic信息、发布订阅的连接，并把相关Topic注册到Name Server上，由Name Server提供服务发现与路由服务。RocketMQ Broker负责消息的收发以及消息的存储。 Console用于为消息队列提供用户访问的外部界面服务，所有消息队列操作都可以通过RocketMQ Consoler实现。使用者优先考虑在Console上执行RocketMQ的操作。

**RocketMQ OpenAPI**

消息队列为方便用户接入、自主运维，RocketMQ OpenAPI通过HTTP/HTTPS接口的形式提供一整套API服务，用户可以

**RocketMQ 鉴权节点**

RocketMQ鉴权节点（DAuth）为消息队列提供统一登录服务以及安全访问控制。包括资源的权限控制、跨账号与子账号访问控制、资源授权等功能。

**RocketMQ 配置中心**

RocketMQ配置中心（Diamond）主要负责存储消息队列的配置信息，如VIP转换规则、资源权限信息等数据。

**Tlog**

Tlog收集消息队列的资源报表数据及其他关键日志。 用于高可用控制，提供RocketMQ Broker的主备切换功能。它通过与ZooKeeper组件交互来管理RocketMQ Broker集群状态，确保RocketMQ Broker节点主备状态的一致性。

**RocketMQ Housekeeping**

定时检查RocketMQ服务核心链路的健康状态，覆盖核心业务、内核参数、应用配置、应用监控指标和控制台等等，如果发现异常及时发出告警，确保RocketMQ集群高可用。

### 运维架构

在您了解了RocketMQ的产品架构后，通过本文档希望帮忙您了解RocketMQ的运维架构。 RocketMQ的运维主要是借助命令行完成。

| 运维大类 | 描述 | 运维工具 |
|---|---|---|
| 例行维护 | 包括巡检和监控。 | 命令行：对RocketMQ的容器、组件进行人工巡检。 |
| 停机维护 | 检查、确认容器、组件状态。 停止、启动容器、组件。 | 命令行、运维控制台。 |

### 产品更新说明

本文介绍消息队列RocketMQ版（简称RocketMQ）从V3.8.0到V3.18.3的产品更新说明，帮助您更快地上手更新后的版本。

**资源隔离优化（实例化支持）**

RocketMQ开放实例化功能，解决多租之间的隔离问题，每个用户可以购买多个实例，每个实例之间逻辑隔离。 为兼容老用户的既有资源，RocketMQ实例的命名空间分为两种： 默认实例（兼容老用户的既有资源） 无独立命名空间，实例内或者跨实例之间，资源命名必须全局唯一。 对RocketMQ老用户来说，既有资源将自动生成一个默认的无独立命名空间实例；无既有资源，则可选择创建不带命名空间的实例，最多创建1个。 消息队列接入点配置（可在控制台**实例详情**页面中获取）。 `//` 推荐配置

```
properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxxx");
```

`//` 兼容配置（不推荐继续使用, 建议逐渐升级为推荐配置）

```
properties.put(PropertyKeyConst.ONSAddr, "xxxx");
```

新建实例有独立命名空间，资源命名确保实例内唯一，跨实例之间可重名。 接入点配置（可在控制台**实例详情**页面中获取）。 `//` 推荐配置

```
properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxx");
```

ons-client客户端必须升级到最新版本： JAVA：1.8.7.1.Final C/C++：v2.0.0 .NET：1.1.3

**资源申请流程优化**

原RocketMQ的资源包括3个部分：消息主题（Topic）、生产者（Producer ID）、消费者（Consumer ID），三者之间都是多对多的对应关系，三者之间的关系复杂而难以理解；对于中、大型企业客户来说，每创建一个Topic，都要关联或者更新Producer ID和Consumer ID，流程过于复杂。 因此，为进一步优化用户体验，降低新用户的接入门槛，对资源申请的接入流程进行简化。 资源申请方面，主要包括以下部分： Topic管理（保持不变） Topic资源申请，一级消息类型，通过Topic对消息进行分类。 Group管理取消原Producer ID的申请，与原Consumer ID统一为Group ID，即对应控制台上，取消原生产者管理， 与原消费者管理统一为Group管理。 取消原申请Producer ID或Consumer ID时需要指定Topic的关联约束，只需申请Group ID即可在代码中直接配置与Topic的关联使用。 兼容性相关问题原申请的Producer ID列表将不再显示，不影响当前业务的正常使用。 原申请的以“CID-”或者“CID_”打头的Consumer ID仍可以正常使用，代码中既可在**PropertyKeyConst.ConsumerId**中设置，亦可在**PropertyKeyConst.GROUP_ID**中设置。 示例代码

**说明**

建议您将ons-client客户端升级为最新版本： JAVA：1.8.7.1.Final C/C++：v2.0.0 .NET：1.1.3 原来已经在使用的Producer ID或者Consumer ID保持兼容，不影响当前在线业务的正常使用， 但建议逐步替换为新的推荐配置方式。 消息队列推荐方式：将Producer ID、Consumer ID的概念融合成Group ID。

```
// 设置PropertyKeyConst.GROUP_ID，原PropertyKeyConst.ProducerId和 PropertyKeyConst.ConsumerId会被@Deprecated properties.put(PropertyKeyConst.GROUP_ID, "原CID-XXX或GID-XXX");
```

兼容方式：Producer ID用来标识生产者，Consumer ID用来标识消费者。 `//` 创建`Producer`时需要配置`PropertyKeyConst.ProducerId`。

```
properties.put(PropertyKeyConst.ProducerId, "原PID-XXX或GID-XXX");
```

`//` 创建`Consumer`时需要配置`PropertyKeyConst.ConsumerId`。

```
properties.put(PropertyKeyConst.ConsumerId, "原CID-XXX或GID-XXX");
```

消息队列

## RocketMQ运维控制台操作指南

### 登录消息队列运维·RocketMQ控制台

**前提条件**

已从部署人员或管理员处获取Apsara Uni-manager运维控制台的访问地址、用户名和密码。 Apsara Uni-manager运维控制台访问地址格式为region-id.ops.console.intranet-domain-id。 推荐使用Chrome浏览器。

**操作步骤**

1. 打开浏览器。
2. 在地址栏中，输入Apsara Uni-manager运维控制台的访问地址，按回车键。

**说明**

您可以单击右上角的当前语言切换其它语言。当前支持简体中文、英文、繁体中文三种语言切换。
3. 输入正确的用户名及密码。

**说明**

登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。 若连续输入密码错误三次，系统将启动图片验证码登录功能；若连续输入错误五次，账户将被锁定，请联系管理员进行激活。 首次登录Apsara Uni-manager运维控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。 消息队列为提高安全性，密码必须满足以下要求： 必须包含英文大小写字母。 必须包含阿拉伯数字（0~9）。 必须包含特殊符号，包括感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等。 密码长度为10~20个字符。
4. 单击**账号登录**。
5. 在顶部菜单栏，选择**产品运维** > **中间件运维** > **消息队列运维****·RocketMQ**。

### 概览

本文介绍消息队列RocketMQ的核心功能与关键指标，帮助用户快速掌握RocketMQ实例的运行状态与健康情况。

**操作步骤**

1. 登录消息队列运维·RocketMQ控制台。
2. 系统默认进入**概览**页面，展示RocketMQ的指标概览、磁盘使用率与流入/流出TPS排名靠前的Broker信息，
以及实时告警统计和最近5条告警记录。

| 区域 | 描述 |
|---|---|
| 指标概览 | 集群总数：当前环境下的RocketMQ集群数量。 Broker总数：所有集群中在线的Broker的总数。单击Broker总数或下方的数字，可跳转至Broker管理页面查看Broker的详细信息。 Topic总数：系统中创建的Topic数量。 Group总数：消费组的数量。 实例总数：部署的RocketMQ实例数量。 |
| 磁盘使用率 TOP Broker | 展示了磁盘使用率最高的几个Broker，包括每个Broker的名称和对应的IP地址及端口号，以及具体的磁盘使用率百分比。 |
| 流入TPS TOP Broker | 展示消息流入速率最高的前四个Broker，单位为条/秒。 |
| 流出TPS TOP Broker | 展示消息流出速率最高的前四个Broker，单位为条/秒。 |
| 告警统计 | 展示不同严重程度（P1严重、P2重要、P3一般、P4警告）的告警总数。 |
| 最近5条告警记录 | 展示最近发生的5条告警记录，包括告警项、严重程度和告警时间。单击查看更多跳转至告警列表页面，可以查看完整的告警信息，包括未关闭的实时告警和已关闭历史告警。 |

### Broker管理

本文介绍如何查看、管理Broker。 消息队列

**背景信息**

在RocketMQ中，Broker管理是确保消息系统高效、稳定运行的重要组成部分。Broker作为RocketMQ的核心组件之一，负责实际的消息存储、转发和查询等操作。

**查看Broker信息**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**Broker** **管理**。
3. 在**Broker****管理**页面，选择**集群名称**。
4. （可选）您可通过Broker名称快速搜索Broker。
5. 在Broker列表中，查看Broker的基本信息。

| 参数 | 描述 |
|---|---|
| Broker名称 | Broker组的唯一标识名称。 |
| 主/备 | 表示该Broker实例在其所属集群中的角色，是主节点还是备节点。 |
| 主机IP | 单个Broker在网络中的地址，由IP地址和端口号组成。 |
| 状态 | 当前Broker的状态。 readonly：表示该Broker处于只读模式。 online：表示该Broker在线并正常工作。 offline：表示该Broker离线，可能由于故障或其他原因无法提供服务。 |
| HA状态 | 当前Broker实例的工作状态。 SYNC STATE：表示该Broker处于同步状态。 _ ONLY MASTER：表示该Broker是唯一的主节点， _ 没有对应的备节点。 ASYNC STATE：表示该Broker处于异步状态，即数 _ 据正在从主节点同步到备节点。 HAIF STATE：表示该Broker处于半同步状态。 _ |
| 流入TPS | 每秒流入的消息数量。单击流量，弹出业务生产流量分析 Top10对话框，查看当前生产者发送消息最多的前10个 Topic，包括Topic、TPS以及Timestamp信息。 |
| 流出TPS | 每秒流出的消息数量。单击流量，弹出业务消费流量分析 Top10对话框，查看当前消费量最高的前10个Topic及其对应的Consumer Group，包括Topic、Group、TPS以及Timestamp信息。 |

6. 在**Broker****管理**页面，单击Broker名称或**操作**列的**查看**，可查看Broker的详细信息。
在**基本信息**页签，查看Broker的**基础信息**和**关键指标**。
**基础信息**：查看Broker的主备节点信息。
消息队列
**关键指标**：查看Broker的**发送****tps**、**拉取****tps**、**磁盘占用率**、**磁盘空间**、**保存时长**等信息，同时分析一段
时间内的**in/out tps**、**PageCache**、**CPU**、**内存**、**磁盘****IO**和**网络****IO**的趋势图。支持按**15****分钟**、1小时、6**小时**或自定义时间进行切换。 在**配置信息**页签，可查看配置项的键、值以及**描述**信息。单击**操作**列的**修改**，可修改**配置值**。 在**VPC****管理**页签，查看Broker集群的VPC网络信息，包括**VPC ID/****名称**、**交换机****ID**、**地域**、集群、**broker VIP**和**nameserver VIP**。 在**状态修复**页签，可修复状态异常的Broker，具体请参考修复Broker。

**禁写Broker**

在RocketMQ中，对Broker执行禁写操作通常是为了避免在维护、故障排查或紧急情况下继续向Broker写入新消息，从而防止数据不一致或其他潜在问题的发生。

**说明**

仅**状态**为**online**的Broker节点支持禁写。
1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**Broker** **管理**。
3. 在**Broker****管理**页面，单击**操作**列的**禁写**。
4. 在弹出的对话框中，单击**确定**。

**恢复Broker**

若需要继续向Broker写入新消息，可解除Broker的禁写。

**说明**

仅状态为**readonly**的Broker节点支持禁写。
1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**Broker** **管理**。
3. 在**Broker****管理**页面，单击**操作**列的**解除禁写**。
4. 在弹出的对话框中，单击**确定**。

**下线/上线Broker**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**Broker** **管理**。
3. 在**Broker****管理**页面，单击**操作**列的**下线**/**上线**。
4. 在弹出的对话框中，单击**确定**。

**重启Broker**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**Broker** **管理**。
3. 在**Broker****管理**页面，单击**操作**列的**重启**。
4. 在弹出的对话框中，单击**确定**。

**修复Broker**

当Broker状态机异常时，您可以通过状态修复功能修复Broker。 消息队列

**说明**

异常类型包括： 主备脑裂主备长期处于 async_stete 状态主备长期处于 half_sync 状态
1. 在**当前修复状态**模块，您可以查看Broker状态机的当前状态以及修复流程。
2. 在**Broker** **列表**模块，单击**操作**列或列表上方显示的可执行的操作，并完成相关操作。
3. 重复步骤2直至完成修复流程。

**说明**

在**状态修复拓扑图**模块，可实时查看Broker 生命周期状态机。

### NameServer管理

本文介绍如何查看NameServer节点的信息。 消息队列

**背景信息**

RocketMQ运维控制台中的NameServer管理模块主要用于管理和监控RocketMQ集群中的NameServer节点。NameServer在RocketMQ中扮演着非常重要的角色，它主要负责服务发现和路由信息管理，是消息生产者、消费者与Broker之间通信的枢纽。

**操作步骤**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**NameServer** **管理**。
3. 在**NameServer** **管理**页面，查看NameServer节点的**IP****地址**、**端口**、**状态**以及**连接数**等信息。

| 参数 | 说明 |
|---|---|
| IP地址 | NameServer节点在网络中的标识符，用于客户端（生产者、消费者）与NameServer进行通信。每个 NameServer都有一个独立的IP地址。 |
| 端口 | 客户端与NameServer通信时使用的网络端口号。 |
| 状态 | NameServer节点的运行状况。 |
| 连接数 | 当前与NameServer建立连接的客户端数量，包括生产者、消费者和Broker。 |

4. 单击**操作**列的**详情**，在弹出的**详情**对话框中，查看NameServer节点的Key、value信息。

### 元数据管理

在元数据管理页面，您可以查看和管理与RocketMQ集群相关联的VPC网络配置信息，进行产品元数据的查看与修改、设置IP白名单以及管理实例和云产品账号。

**操作步骤**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**元数据管理**。
3. 在**元数据管理**可进行以下操作：
在**VPC****管理**页签，可查看RocketMQ实例绑定的VPC信息，包括**VPC ID**和**VPC****名称**。单击**查看****broker**， 可查看该VPC下的Broker列表，包括**Broker****地址**、**Broker VIP**、**Nameserver VIP**、**实例****ID**、集群以及**交换机****ID**。 单击**配置管理**页签，您可以查看配置项及其描述信息，并对配置项进行修改。 修改配置值：单击**操作**列的**修改**，设置**集群**和**配置值**，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| 集群 | 下拉选择要修改的集群。 |
| 配置值 | 开启：启用写入认证。 关闭：禁用写入认证。 |

消息队列

**重要**

修改操作将统一更新集群内所有Broker的相关配置项的配置值，请谨慎执行。 单击**TaoKeeper** **节点管理**页签，在左侧结构树中选中节点，右侧将展示该节点的详细数据；在Broker主备重建时，您可以通过单击**删除节点**来移除元数据。

**重要**

删除节点会对RocketMQ产品正常运行产生影响，请谨慎操作。 单击**IP** **白名单**页签，可设置RocketMQ的IP访问白名单。

**说明**

仅允许白名单范围内的客户端进行更新、获取Broker配置以及更新namesrv配置的操作。 系统默认生成的IP白名单不支持修改和删除。 若未手动配置白名单，系统将默认关闭访问控制。 查找IP白名单：在**IP** **白名单**页签，输入IP地址，单击**确认**，系统将展示搜索结果的列表。 新增IP白名单：在**IP** **白名单**页签，单击**新增**，输入具体IP地址或者CIDR地址段，然后单击**确定**。 修改IP白名单：在IP 白名单列表中，单击目标IP操作列的**编辑**，在弹出的对话框中修改IP地址后单击确定。 删除IP白名单：在IP 白名单列表中，单击目标IP操作列的**删除**，在弹出的对话框中单击**确定**。 单击**实例管理**页签：您可以查看云产品通过基线申请的AK、SK调用SDK创建的实例，包括**实例****ID/**名称、**集群****ID**、**云产品名称**以及**状态**等信息。 a. （可选）选择**集群名称**，输入**云产品名称**，可快速筛选实例。 b. 单击**操作**列的**查看**，跳转至**实例管理详情**页面，展示实例的**基础信息**、**Topic****管理**和**Group****管理**等信息。
**基础信息**：展示**实例****ID/****名称**、**实例名称**、**集群****ID**、**云产品名称**以及**状态**等信息。
**Topic****管理**：展示**Topic**、**类型**和**描述**等信息。
**Group****管理**：展示**Grup ID**、**类型**和**描述**等信息。
单击**云产品账号管理**页签：您可以查看并编辑用于访问云产品的账号信息。 查看云产品账号：在**产品**框中输入云产品名称，可快速筛选云产品的账号信息，包括**账号名称****/ID**、**云产** 品以及**状态**。 编辑云产品账号：单击目标账号**操作**列的**编辑**，在**编辑账号**对话框，修改账号所关联的**云产品**和**状态**后， 单击**确定**。

**说明**

**账号名称****/ID**不支持修改。

### Copilot

#### 热升级

本文介绍如何创建热升级任务。 消息队列

**背景信息**

RocketMQ热升级指的是在不中断服务的情况下对RocketMQ进行版本更新或配置调整，以减少系统停机时间并维持业务的连续性。

**前提条件**

当前系统存在升级审批任务。

**操作步骤**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，选择**Copilot >** **热升级**。
3. 在**热升级**页面，单击**创建热升级任务**。
4. 在弹出的对话框中，单击**确定**，生成热升级任务列表。您可以单击**集群名称**右侧的下拉框，选择集群，快速筛
选Broker节点。

| 参数 | 说明 |
|---|---|
| Broker 名称 | Broker组的唯一标识名称。 |
| Broker 地址 | 单个Broker在网络中的地址，由IP地址和端口号组成。 |
| 主备 | 表示该Broker实例在其所属集群中的角色，是主节点还是备节点。 |
| HA状态 | 当前Broker实例的工作状态。 SYNC STATE：表示该Broker处于同步状态。 _ ONLY MASTER：表示该Broker是唯一的主节点， _ 没有对应的备节点。 ASYNC STATE：表示该Broker处于异步状态，即数 _ 据正在从主节点同步到备节点。 HAIF STATE：表示该Broker处于半同步状态。 _ |
| 更新时间 | HA状态最后一次更新或检查的时间。 |
| 升级状态 | 当前Broker的升级状态。 |
| 是否禁写 | 是否禁止向该Broker写入消息。 是：表示当前禁止向该Broker写入消息。 否：表示允许向该Broker写入消息。 |
| 流入TPS | 每秒流入的消息数量。单击流量，弹出业务生产流量分析 Top10对话框，查看当前生产者发送消息最多的前10个 Topic，包括Topic、TPS以及Timestamp信息。 |

消息队列

| 流出TPS | 每秒流出的消息数量。单击流量，弹出业务消费流量分析 Top10对话框，查看当前消费量最高的前10个Topic及其对应的Consumer Group，包括Topic、Group、TPS以及Timestamp信息。 |
|---|---|

5. 确认需要升级的Broker集群相应的Broker的**HA****状态**为**SYNC_STATE**。

**说明**

本文仅以一组操作为例，其他组的操作步骤参照步骤6至步骤9。
6. 禁写操作组的节点。
在**热升级**页面，依次单击一组主备节点**操作**列的**禁写**，然后单击**确定**。
7. 升级主备节点。
i. 待主备节点**升级状态**为**可升级**后，单击主节点**操作**列的**升级**，然后单击**确定**。 ii. 待主节点**升级状态**为**升级完成**后，单击备节点**操作**列的**升级**，然后单击**确定**。
8. 恢复操作组的节点。
待主备节点**升级状态**均为**升级完成**且**HA****状态**为**SYNC_STATE**后，依次单击主备节点**操作**列的**解除禁写**，然后单击**确定**。

#### 容灾搭建

本文介绍如何搭建单集群容灾以及扩容容灾集群。

**背景信息**

在交付阶段结束后，提升消息队列容灾搭建的效率，以降低对线上业务的影响。容灾关系的搭建属于运维阶段， 由运维人员进行排期并执行相关变更。

**前提条件**

检查集群状态为正常。 主备机房的升级及扩容应遵循标准流程。 此时，主机房已正常启动，而备机房则处于阻塞状态。通过broker_location，可以查看到主备节点的信息，主机房已成功分配broker_name。

**注意事项**

容灾搭建不支持包含全局顺序消息Topic的集群。 请检查主备机房所有RocketMQ的Broker所在物理机的机型信息。 确保一组主备使用相同的机型和磁盘容量。 选择备机房节点进行主备搭建时，确保选择的备机房节点和主机房的节点机型一致。 如果从备机房中无法选择到和主机房相同的机型，请谨慎搭建或提工单联系规划人员评估机型风险。

**单集群容灾搭建**

**说明**

任务完成或者未完成状态都支持结束任务，单击**结束容灾任务**会清空任务信息表。
1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，选择**Copilot >** **容灾搭建**。
消息队列
3. 在**容灾搭建**页面，单击**创建容灾搭建任务**。
4. 在弹出的对话框中，选择**集群**和**主机房**，然后单击**确定**。此操作将触发任务创建，系统会检查是否存在未完成
的搭建任务。如果不存在，则同步现有集群信息到新任务中，扩容的主机房Broker会显示在列表末尾，待上线，同时会缓存集群内某个主Broker的元数据。

| 参数 | 说明 |
|---|---|
| Broker 名称 | Broker组的唯一标识名称。 |
| Broker 地址 | 单个Broker在网络中的地址，由IP地址和端口号组成。 |
| 主备 | 表示该Broker实例在其所属集群中的角色，是主节点还是备节点。 |
| 状态 | 当前Broker实例的工作状态。 SYNC STATE：表示该Broker处于同步状态。 _ ONLY MASTER：表示该Broker是唯一的主节点， _ 没有对应的备节点。 ASYNC STATE：表示该Broker处于异步状态，即数 _ 据正在从主节点同步到备节点。 HAIF STATE：表示该Broker处于半同步状态。 _ |
| 流入TPS | 每秒流入的消息数量。单击流量，弹出业务生产流量分析 Top10对话框，查看当前生产者发送消息最多的前10个 Topic，包括Topic、TPS以及Timestamp信息。 |
| 流出TPS | 每秒流出的消息数量。单击流量，弹出业务消费流量分析 Top10对话框，查看当前消费量最高的前10个Topic及其对应的Consumer Group，包括Topic、Group、TPS以及Timestamp信息。 |
| 是否禁写 | 是否禁止向该Broker写入消息。 是：表示当前禁止向该Broker写入消息。 否：表示允许向该Broker写入消息。 |
| idc room | 所属机房或数据中心名称。 |

**说明**

本文仅以一组操作为例，其他组的操作步骤参照步骤5至步骤10。
5. 禁写操作组的节点。
在**容灾搭建**页面，依次单击主备节点**操作**列的**禁写**，然后单击**确定**。此操作将禁用所对应节点的写入功能，观察流量下降为0。
6. 下线备节点。
消息队列 i. 当流量降为0后，单击备节点操作列的**下线**，然后单击**确定**，将下线该节点，并删除对应的BrokerName， 清理store目录下 `broker.conf` 、 `/config/topics.json` 和 `/config/subscriptionGroup.json` 之外的其余文件。

**说明**

下线备节点后，主节点状态变为**ONLY_MASTER**。
7. 为操作组的主节点新增备节点。

**说明**

下线备节点后，主机房操作组的主节点**操作**列会显示**新增备节点**按钮。 单击**新增备节点**，选择备节点并单击**确定**，将挂载备机房的备节点一，并将缓存的元数据同步至该Broker， 设置该Broker为禁读禁写状态，同时会在broker_name插入备节点一。
8. 将操作组原备节点提升为主节点（上线）。

**说明**

下线备节点后，主机房操作组已下线的备节点**操作**列会显示**上线**按钮。 在挂载备机房备节点一之后，单击**上线**，然后单击**确定**，会设置该Broker为新主节点，将缓存的元数据同步至该Broker，并设置该Broker为禁读禁写状态，申请BrokerName并插入数据库，最后重启容器。
9. 为操作组的新主节点新增备节点。

**说明**

操作组原备节点升为主节点后，**操作**列会显示**新增备节点**按钮。 单击**新增备节点**，选择备节点并单击**确定**，将挂载备机房的备节点二，并将缓存的元数据同步至该Broker， 设置该Broker为禁读禁写状态，同时会在broker_name插入备节点二。
0. 解除禁写。
依次单击主备节点**操作**列的**解除禁写**，然后单击**确定**，解禁当前节点的写入，观察流量上升。

**容灾集群扩容**

**说明**

任务完成或者未完成状态都支持结束任务，单击**结束容灾任务**会清空任务信息表。
1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，选择**Copilot >** **容灾搭建**。
3. 在**容灾搭建**页面，单击**创建容灾搭建任务**。
4. 在弹出的对话框中，选择**集群**和**主机房**，然后单击**确定**。此操作将触发任务创建，系统会检查是否存在未完成
的搭建任务。如果不存在，则同步现有集群信息到新任务中，扩容的主机房Broker会显示在列表末尾，待上线，同时会缓存集群内某个主Broker的元数据。
5. 上线主机房新扩容的Broker。
存在新扩容的Broker时，主机房操作组的已下线备Broker或者新Broker会显示**上线**按钮，单击**上线**，然后单击**确定**，会设置该Broker为新主节点，将缓存的元数据同步至该Broker，并设置该Broker为禁读禁写状态， 申请BrokerName并插入数据库，最后重启容器。
6. 为操作组的新主节点新增备节点。
消息队列

**说明**

操作组原备节点升为主节点后，**操作**列会显示**新增备节点**按钮。 单击**新增备节点**，选择备节点并单击**确定**，将挂载备机房的备节点二，并将缓存的元数据文件同步至该 Broker，设置该Broker为禁读禁写状态，同时会在broker_name插入备节点二。

#### 容灾解除

本文介绍如何解除容灾关系。

**背景信息**

解除集群中Broker的容灾关系，使容灾集群缩容为单机房集群，也可以进行集群迁移或 XC 轮转。

**前提条件**

检查集群状态为正常。 主备机房的升级及扩容应遵循标准流程。 确保主节点部署在主机房。

**适用范围**

容灾机房转换成单机房。 集群跨机房迁移。 XC 轮转。

**操作步骤**

**说明**

以下操作以一组Broker为例，其他组的操作步骤亦相同。
1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，选择**Copilot >** **容灾解除**。
3. 在**容灾关系解除**页面，选择**集群名称**。
4. 列表展示Broker的基本信息。

| 参数 | 描述 |
|---|---|
| Broker名称 | Broker组的唯一标识名称。 |
| 主/备 | 表示该Broker实例在其所属集群中的角色，是主节点还是备节点。 |
| 主机IP | 单个Broker在网络中的地址，由IP地址和端口号组成。 |

消息队列

| 状态 | 当前Broker的状态。 readonly：表示该Broker处于只读模式。 online：表示该Broker在线并正常工作。 offline：表示该Broker离线，可能由于故障或其他原因无法提供服务。 |
|---|---|
| HA状态 | 当前Broker实例的工作状态。 SYNC STATE：表示该Broker处于同步状态。 _ ONLY MASTER：表示该Broker是唯一的主节点， _ 没有对应的备节点。 ASYNC STATE：表示该Broker处于异步状态，即数 _ 据正在从主节点同步到备节点。 HAIF STATE：表示该Broker处于半同步状态。 _ |
| 流入TPS | 每秒流入的消息数量。单击流量，弹出业务生产流量分析 Top10对话框，查看当前生产者发送消息最多的前10个 Topic，包括Topic、TPS以及Timestamp信息。 |
| 流出TPS | 每秒流出的消息数量。单击流量，弹出业务消费流量分析 Top10对话框，查看当前消费量最高的前10个Topic及其对应的Consumer Group，包括Topic、Group、TPS以及Timestamp信息。 |

5. 禁写操作组主备节点。
在**容灾关系解除**页面，依次单击主备节点**操作**列的**禁写**，然后单击**确定**。此操作将禁用所对应节点的写入功能，观察流量下降为0。
6. 单击操作组备节点**操作**列的**解除容灾关系**，然后单击**确定**。此操作将停止该Broker，并从broker_name表中
移除该节点。
7. 解除容灾关系后，将支持清理元数据。单击操作组备节点**操作**列的**清理数据**，将删

```
除 /home/admin/store/broker.conf 、
 /home/admin/store/config/topics.json 和 /home/admin/store/config/subscriptionGroup.json 之
```

外的其他文件。

#### 容量分析

系统支持在指定时间范围内查看某个集群的性能指标，包括集群级别资源水位概览以及历史资源使用趋势等。

**背景信息**

容量分析旨在为用户提供一个直观、全面的可视化平台，用于评估和监控 RocketMQ 集群的当前负载情况及容量使用趋势，从而支持科学决策与主动运维。

**操作步骤**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，选择**Copilot >** **容量分析**。
3. 在**容量分析**页面，选择**集群名称**，设置**时间范围**，勾选Broker规格。
4. 页面展示TPS趋势和保存时间趋势图。
消息队列

**说明**

将鼠标悬停在图表上，可查看当前时间的详细数值。
**TPS****趋势图**：展示当前集群流入消息速率、流出消息速率以及总吞吐量趋势图。图中的虚线橙色标线表示该
Broker规格的理论最大TPS规格上限。
**保存时间趋势**：展示消息在Broker上实际保留的时间长度趋势图。默认消息保存时长为72小时。

#### 集群巡检

您可以利用**集群巡检**功能进行智能化巡检，并生成相应的巡检报告。

**创建巡检任务**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，选择**Copilot >** **集群巡检**。
3. 在**集群巡检**页面，单击**创建巡检任务**。
4. 在**创建巡检任务**面板，配置以下参数后，单击**确定**。

| 参数 | 说明 |
|---|---|
| 巡检任务类型 | 一次巡检：立即执行一次巡检任务。 定时巡检：按周期自动执行巡检任务。 |

消息队列

| 定时巡检时间 | 仅当选择定时巡检时显示此参数。 您可以输入cron表达式或单击使用工具生成来设置具体执行时间点。 |
|---|---|
| 集群 | 选择要巡检的目标集群。 说明如未选择特定集群，则系统将自动对所有集群进行巡检，并对结果进行汇总。 |
| 巡检设置 | 选择巡检项，巡检项说明见下表。 |

巡检项说明表：

| 巡检项 | 巡检规则 |
|---|---|
| Broker基本信息 | 检查集群Broker流量、磁盘水位、ZK状态等基本信息。 说明系统默认勾选，不可取消。 |
| Broker权限检查 | 检查每个Broker是否处于可读可写状态。 |
| Broker鉴权状态检查 | 检查每个Broker是否开启鉴权配置 |
| 消息保留时间检查 | 检查集群消息保留时间是否大于等于72小时。 |
| Nameserver注册状态检查 | 检查每个Broker的注册状态。 |
| NameServer连接数检查 | 检查NameServer连接数及状态。 |
| NameServer CPU Steal时间检查 | 检查NameServer节点的CPU Steal时间。 |

**开启巡检任务**

巡检任务创建完成后，默认为**待运行**状态，您可单击**开启巡检**执行一次巡检任务。
1. 在巡检任务列表中，单击目标任务**操作**列的**开启巡检**。
2. 在弹出的对话框中，单击**确定**。

**关闭巡检任务**

当巡检任务长时间处于运行状态时，您可以选择关闭巡检任务。一旦关闭巡检，系统将停止执行该巡检任务。
1. 在巡检任务列表中，单击目标任务**操作**列的**关闭巡检**。
2. 在弹出的对话框中，单击**确定**。
消息队列

**查看巡检结果**

1. 在巡检任务列表中，您可以查看巡检任务的**任务****ID**、**集群**、**巡检类型**、**巡检项**、**任务状态**、**最新巡检时间**、创
**建时间**以及**定时巡检时间**。

**说明**

单击**巡检项**列的信息，将弹出**巡检项**对话框，您可以查看当前巡检任务对应的**巡检项**和**巡检规则**。
2. 单击目标任务**操作**列的**查看巡检结果**。
3. 在**巡检任务**对话框中，可以查看任务**ID**、**巡检状态**、**巡检耗时**、**创建时间**、以及**过期时间**。
4. 单击**操作**列的**查看巡检报告**。
5. 在**巡检结果**面板中，可以查看集群巡检的详细报告，您可以单击**下载报告**，生成并导出当前集群的完整巡检报
告。

**说明**

报告格式支持以下三种： Markdown HTML PDF

**修改巡检任务**

1. 在巡检任务列表中，单击目标任务**操作**列的**编辑**。
2. 在**编辑巡检任务**对话框中，您可以重新选择**集群**和**巡检设置**，然后单击**确定**。

**删除巡检任务**

若您不再需要某项巡检任务，可以将其删除。
1. 在巡检任务列表中，单击目标任务**操作**列的**删除**。
2. 在弹出的对话框中，单击**确定**。

**修改巡检规则参数**

1. 在**集群巡检**页面，单击**巡检配置**。
2. 在**规则参数**页签，展示当前已设置的规则参数，包括**ID**、**巡检项**、**参数名称**、**参数值**、**操作符**、**单位**、**告警级**
别以及**状态**。
3. 在规则参数列表中，单击**操作**列的**编辑**。
4. 在**编辑规则参数**对话框中，修改以下参数后，单击**确定**。

| 参数 | 说明 |
|---|---|
| 参数值 | 设定触发告警的数值阈值。 |

消息队列

| 操作符 | 定义比较逻辑，判断实际采集值是否满足条件。可选值： > >= < <= == != |
|---|---|
| 单位 | 标注参数值的计量单位。 |
| 告警开关 | 控制该规则是否启用。 开启 ：系统会实时监测并按此规则触发告警。 关闭：即使条件满足也不会告警，常用于临时屏蔽或调试。 |
| 告警级别 | 说明仅当告警开关开启时显示此参数。 定义告警的严重程度，可选值： P1 P2 P3 P4 |
| 描述 | 输入该规则的描述信息。 |

例如：配置一个合理的磁盘使用率告警规则，可以设置以下取值： 参数值：83 操作符：> 单位：% 告警开关：开启告警级别：P2 描述：磁盘使用率超过83%时触发告警，请及时清理空间或扩容。 配置完成后，系统将在磁盘使用率达到 84%、85%... 时持续发送 P2 级别告警，直到降至 83% 以下。

**修改巡检项权重**

在集群巡检系统中为各个巡检项分配“权重分数”，主要用于计算整体健康度。
1. 在**集群巡检**页面，单击**巡检配置**。
2. 单击**巡检项权重**页签，展示**巡检项名称**、**巡检项编码**以及**权重分数**。
3. 在巡检项列表中，单击**操作**列的**编辑**。
4. 在**编辑权重**对话框中，设置**权重分数**，然后单击**确定**。
消息队列

**说明**

分数越高表示权重越大，各项分数之和无需等于100。

#### Topic迁移

**Topic** **迁移**用于将指定 Topic 的数据从源集群平滑、安全地迁移到目标集群。该功能广泛应用于集群扩容、地
域迁移、架构升级、灾备切换等场景，确保业务在数据迁移过程中无感知、零中断。

**新建迁移任务**

**说明**

仅支持迁移普通消息类型的 Topic。
1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，选择**Copilot > Topic****迁移**。
3. 在**Topic** **迁移**页面，单击**新建迁移任务**。
4. 在**新建迁移任务**对话框中，配置以下参数后，单击**确定**。

| 参数 | 说明 |
|---|---|
| 源集群 | 选择当前存放待迁移 Topic 的原始集群。 |
| 实例 | 选择待迁移 Topic 所属的 RocketMQ 实例。 |
| Topic | 要迁移的消息主题名称。 |
| 目标集群 | 选择接收迁移数据的目的地集群。 |
| 等待天数 | 迁移完成后，系统保留源端数据的天数，用于回滚或校验。 |

5. 创建完成后，默认进入**迁移任务详情**页面。在**迁移任务详情**页面，执行以下步骤。

**说明**

在迁移过程中可以**取消迁移**任务。 在**步骤日志**模块，单击步骤右侧的**查看详情**，可查看相应操作任务的详细信息。 若迁移步骤失败，可**单击**重试重启任务。 i. 前置检查 a. 单击**开始检查**，进行前置检查操作。 消息队列 iii. 禁写源集群Topic a. 单击**禁写源集群** **Topic**。 b. 待禁写源集群Topic后，单击**下一步：监控消费**。 iv. 监控消费

**说明**

自动刷新间隔为 30 秒。全部消费者组堆积为 0 后，可进入下一步执行禁读源集群 Topic。 a. 待完成等待期后，系统自动进行监控消费，您可单击**跳过消费检查和等待期**，立即进行监控消费。 b. 待完成监控消费后，单击**下一步：禁读源集群** **Topic**。 v. 禁读源集群 Topic a. 单击**禁读源集群** **Topic**。 b. 待禁读源集群Topic后，单击**下一步：清理** **Topic**。 vi. 清理 Topic a. 单击**删除源集群** **Topic**，在弹出的对话框中单击**确定**。 b. 待源集群Topic删除后，操作完成。

**查看迁移任务详情**

1. （可选）在**Topic****迁移**页面，您可以通过**Topic**、**状态**、**集群**和**实例****ID**快速筛选迁移任务。
2. 在迁移任务列表中，可查看迁移任务的**任务** **ID**、**实例** **ID**、**Topic**、**源集群**、**目标集群**、**当前步骤**、**状态**和创

**建时间。**

3. 单击迁移任务**操作**列的**查看详情**，进入**迁移任务详情**页面，展示迁移任务的**任务信息**、**任务结果**和**步骤日志**。

**说明**

在**步骤日志**模块，单击步骤右侧的**查看详情**，可查看相应操作任务的详细信息。

**删除迁移任务**

**说明**

迁移任务执行过程中不支持删除。
1. 在迁移任务列表中，单击迁移任务**操作**列的**删除**。
2. 认真阅读对话框中的提示信息后，单击**确定**。

**重要**

删除任务将永久移除任务记录及步骤日志，请谨慎操作。

**取消迁移任务**

消息队列

**说明**

**失败**和**已完成**的迁移任务中不支持取消。
1. 在迁移任务列表中，单击迁移任务**操作**列的**取消**。
2. 在弹出的对话框中，输入取消原因，单击**确定**。

**重要**

取消将回滚已执行的步骤（恢复源集群权限、删除目标集群 Topic），可能导致已发往目标集群未消费的消息丢失，请谨慎操作。

**重试迁移任务**

**说明**

仅执行**失败**的迁移任务支持重试。
1. 在迁移任务列表中，单击迁移任务**操作**列的**重试**。
2. 认真阅读对话框中的提示信息后，单击**确定**。

**说明**

重试任务将从失败的步骤恢复执行。

### 操作审计

本文介绍如何查看所有对RocketMQ 4.x集群执行的操作日志。

**操作步骤**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**操作审计**。
3. （可选）您可以通过选择**操作类型**，输入**操作人**以及设置**操作时间**快速筛选操作日志。
4. 在操作日志列表中，可以获取**ID**、**操作人****ID/****名称**、**部门****ID**、**操作类型**、**操作时间**、**操作项**以及**操作参数**。
消息队列

## 高危操作

### 运维操作的危险级别定义

所有运维操作按业务场景和操作的危险程度被分为三级：G1、G2、G3。 各级别定义如下： G1：L1/L2可以根据文档完成操作，不需要做变更申请，该操作按文档执行完全安全，该操作不会对业务产生影响。 G2：L1/L2驻场人员可以根据文档指引，需要做变更申请，向产品侧咨询确认方可执行操作。该操作不会对业务产生影响。 G3：L1/L2驻场人员可以根据文档指引，需要做变更申请，向产品侧以及客户侧咨询确认方可执行操作（提工单）。该操作有可能对业务产生影响。

### 高危操作和文件

本节将列出您在运维时需格外注意的高危运维操作和不能随意清理的高危文件。

## 高危操作

高危操作即上文提到的**G3**级别的运维操作，进行该类操作时请按照相应的指导进行。

**高危文件**

高危文件是指不能被随意清理的文件，需要您在处理文件时注意以下事项： 从文件产生到现在都没有动态增长的文件原则上不能清理。如需要清理（如一些陈旧的包，升级时遗留下来不再使用的版本），需要与产品，客户进行确认。 配置文件不能清理。所有conf目录下的内容都是受保护的。 应用程序包目录下的文件不能清理。 当前正在使用的日志文件不能清理。例如日志文件有mw.log和mw-2018-07-22.log，这种场景下，当前生效的文件mw.log不能被清理。 对于RocketMQ Broker的高危文件，RocketMQ Broker会自主管理这些文件，不能主动清理。 表 1. 高危文件

| 文件名称 | 用途 | 说明 |
|---|---|---|

消息队列

| /home/admin/store/commitlog/* | 消息存储文件，用于存放生产者提交的消息，属于数据文件。 | 每个文件的大小由 /home/admin/rmq/conf /broker.conf中的配置项mapedFileSizeCommitLog 决定，默认值为1G。 删除旧数据的执行时间由/home/admin/rmq/ conf/broker.conf中的配置项deleteWhen决定，默认值为每天早上4:00。 空间使用率到多大时开始清理旧数据， 由home/admin/rmq/conf/broke r.conf中的配置项 diskMaxUsedSpaceRatio决定，默认值为 75%。 当磁盘满时是否强制删除旧文件， 由home/admin/rmq/conf/broke r.conf中的配置项 leanFileForciblyEnable决定。 |
|---|---|---|
| /home/admin/store/config/consu merOffset.json | 消费位点存储文件。 | RocketMQ Broker会自主管理该文件，不能主动清理。 |
| /home/admin/store/config/delayO ffset.json | 重试消息队列的消费位点。 | RocketMQ Broker会自主管理该文件，不能主动清理。 |
| /home/admin/store/config/subscri ptionGroup.json | 订阅组配置。 | RocketMQ Broker会自主管理该文件，不能主动清理。 |
| /home/admin/store/config/topics.j son | topic配置。 | RocketMQ Broker会自主管理该文件，不能主动清理。 |

消息队列

## 运维准备

本文介绍运维时需要的登录入口、账号、权限和工具。 表 1. 运维准备说明

| 名称 | 作用 | 说明 |
|---|---|---|
| SSH远程登录工具 （如MobaXterm或PuTTY） | 登录组件所在的机器。 | 登录使用的账号需要具有相应的操作权限。但不建议直接使用root或 admin账号。 |
| 账号 | 用于登录控制台或具体机器。 | 控制台的登录账号和密码请向 RocketMQ技术支持人员获取。 登录RocketMQ机器组件所在机器使用的账号需要具有相应的操作权限。但不建议直接使用root或 admin账号。 |

消息队列

## 例行维护

组件巡检监控是指对RocketMQ各系统组件的状态进行监测，包括Cai、Name Server、Broker、 Controller、Console和Housekeeping。 服务巡检监控是指对RocketMQ的核心链路进行运行时巡检和监控，覆盖核心业务、内核参数、应用配置、应用指标（Metrics）和控制台等。

### 组件巡检监控

巡检：周期性地拨测URL或端口等来判断RocketMQ的组件运行是否正常。目前支持的巡检方式有：HTTP、 TCP、PING和JDBC。 监控：通过TLog从客户机搜集日志并按一定方式汇聚出关键指标，以此来衡量系统运行状况，包括容器监控和其他自定义指标的监控。

#### 人工巡检

人工巡检使用的命令为Linux系统通用的命令，具体参数需要根据实际环境设置。

##### Name Server的巡检

1. 登录Name Server容器。
2. Name Server运行时是一个Java进程，通过PS命令查看进程状态是否正常运行： ps aux|grep -i

| NamesrvStartup |  |  |
|---|---|---|
| 3. 通过 | ss -s | 命 |

##### RocketMQ Console的巡检

RocketMQ Console 是一个部署在Tomcat内部的Web系统，因此巡检需考虑如下几方面：
1. 登录RocketMQ Console容器。
2. 检查Tomcat进程是否存在，7001端口是否开通： netstat -an |grep 7001 。
3. 检查Nginx进程是否存在，80端口是否能够正常转发到7001。
4. 检查/home/admin/logs/ons-api/*.log中是否存在明显的异常。
5. 检查/home/admin/ons-api/logs 中是否需要清理无用的日志文件。
6. 检查/home/admin对应磁盘是否有足够的容量。

##### RocketMQ Controller的巡检

1. 登录RocketMQ Controller容器。
2. RocketMQ Controller运行时是一个Java进程，通过PS命令查看进程状态是否正常运行： ps aux|grep -i

| FailoverStartUp |  | 。 |  |
|---|---|---|---|
|  | grep 'take the leadership of role' |  |  |
|  |  |  | 可以确认两台Controller中哪一台正在负责 |

消息队列
4. 检查 `/home/admin/logs/rocketmqlogs/*.log` 中是否存在明显的异常。

##### RocketMQ Broker的巡检

1. 登录RocketMQ Broker容器。
2. 执行命令 ps aux|grep brokerStartup ，查看进程信息。
3. 执行命令 `ss -s` ，检查连接数，如果连接数大于规格半数以上，请联系售后工程师处理。
4. 查看RocketMQ Broker相关的日志，路径为/home/admin/logs/rocketmqlogs/。
5. 检查磁盘容量： `df -h` ，确保磁盘使用率小于80%。
6. 检查/home/admin/store路径下的配置是否存在：
/home/admin/store/config/consumerOffset.json：消费位点存储文件。 /home/admin/store/config/delayOffset.json：定时消息消费位点。 /home/admin/store/config/subscriptionGroup.json：订阅组配置。 /home/admin/store/config/topics.json：Topic配置。 /home/admin/store/consumequeue：消费索引文件存储文件，以Topic维度进行存储。 /home/admin/store/index：key查询索引文件。
7. 发消息之后，查看消息存储文件commitlog：
i. 查看/home/admin/store/commitlog目录下是否有文件产生。 ii. 在目录du –sh /home/admin/store/commitlog/* 下查看文件是否有新的数据写入。 iii. 检查当前服务器的收发情况，执行 `sh /home/admin/rmq/bin/mqadmin clusterlist` 命令，查看集群内各节点的收发情况。

##### Address Server（Cai）的巡检

1. 登录Address Server（Cai）容器。
AddressServer是一个Nginx进程模块，默认开启HTTP端口是8080。
2. 执行命令 `curl -v 'http://localhost:8080/rocketmq/nsaddr4broker-internal'` ，检查地址服务器上
Name Server的配置信息。返回状态码为200，同时返回/home/admin/cai/htdocs/rocketmq/nsaddr4broker-internal配置中的内容表明正常。

##### Diamond Server的巡检

1. 登录Diamond Server容器。
2. 磁盘空间检查，避免磁盘满导致Diamond服务异常： df –lh 。
3. 确保系统内存，CPU在正常范围： `top` 。
4. 确保地址服务器正常连接，且不能延迟太大（内网10 ms以下）： `ping jmenv.tbsite.net -c 3` 。
5. 确保每个Diamond Server彼此能相互连接，网络延迟不能太大，执行一下脚本，循环ping所有的Diamond
Server。
6. 确保Diamond服务压力在可控范围内，单机QPS极限4000左右，建议单机QPS不超过500，load少于CPU核
数，CPU不超过20%： `tsar --nginx --load --cpu -l -i3` 。

##### Dauth的巡检

Dauth 是一个部署在Tomcat内部的Web系统，因此巡检考虑以下几方面：
1. 登录Dauth容器。
消息队列
2. 检查Tomcat进程是否存在，8080端口是否已开通。
3. 检查Nginx进程是否存在，80端口是否能够正常转发到8080。
4. 检查/home/admin/dauth/logs/*.log中是否存在明显的异常。
5. 检查/home/admin/dauth/logs中是否存在需要清理的无用日志文件。
6. 执行curl 'localhost:8080'|grep Unsupported命令，若返回结果中有“Unsupported”字段，说明服务正
常。
7. 检查/home/admin对应磁盘是否有足够的容量。
8. Dauth也是Diamond的客户端，因此需要巡检以下方面：
/home/admin/logs/diamond-client/diamond-client.log中是否有明显异常。

```
执行如下 curl 'http://jmenv.tbsite.net:8080/diamond-server/diamond-unit-spas' 命令，返回
```

diamond spas单元的服务器列表，ping每台机器，确保延迟在10 ms以下。

##### TLog Console的巡检

登录TLog Console容器。 检查Tomcat进程： ps aux|grep tomcat 。 检查磁盘容量： `df -h` 。 检查访问是否正常： `curl -v 'http://localhost'` 。

### 服务巡检监控

RocketMQ的服务巡检是通过Housekeeping组件执行。 Housekeeping会周期性地巡检RocketMQ的各个监控项（注意：当前的监控项都是固定配置的，不支持变更），并把告警信息输出到Housekeeping容器中的位置/home/admin/logs/aliware-mqhkagent/warning.log。

### 日志

日志是RocketMQ运维的重要方式之一，主要用于监控及故障处理。所以需要对日志进行例行的维护。 RocketMQ的日志主要包括基础监控日志、服务监控日志、容器监控日志和JVM监控日志。详细信息请参考《日志参考》。 消息队列

## 运维命令

后端运维命令是提供给有经验的运维工程师使用的，请优先选择使用控制台执行相关的命令。

### 概述

消息队列提供一个后台运维工具，帮助您进行日常运维。此运维工具在目录/home/admin/rmq/bin下，文件名是sh mqadmin 。 运维的命令需要登录到mq-namesrv或mq-broker的容器上执行，步骤如下：
1. 执行以下命令登录容器。

```bash
docker exec -it <namesrv或broker的容器id> /bin/bash
```

2. 执行以下命令进入运行目录。

```
cd /home/admin/rmq/bin
```

**命令语法示例**

在mq-broker中使用cd命令跳转到rmq/bin目录后通过此工具执行相关指令，例如： 展示所有支持的指令： `./mqadmin` 展示指令clusterList的帮助文档（用法及参数）： `./mqadmin help clusterList` 运行指令clusterList，展示cluster列表及详细信息： `./mqadmin clusterList -m` 指令clusterList的用法描述为： `mqadmin clusterList [-h] [-i <arg>] [-m] [-n <arg>]` ，其中的参数用法如下： `-h` 、 `-i` 、 `-m` 和 `-n` 是参数短标识，有相应标识表示指定了相应选项和参数。 用法描述中用方括号括起的参数标识表示可选参数，可以不指定。 用法描述中用尖括号括起的arg表示此参数如果指定则需要一个具体的参数值，例如 `./mqadmin`

```
clusterList -i 3 -m 。
```

**资源命名**

从V3.8.1版本开始，针对有命名空间和无命名空间的实例所包含的资源命名有所变更。具体说明如下： Topic命名有命名空间的实例：instanceid%topic。 无命名空间的实例：topic。 Group ID命名有命名空间的实例：instanceid%gid。 无命名空间的实例：gid。

### 查看所有运维命令

表 1. mqadmin

| 参数名称 | 说明 |
|---|---|

消息队列

| updateTopic | 创建Topic。 |
|---|---|
| deleteTopic | 删除Topic。 |
| topicList | 查看Topic列表信息。 |
| topicCLusterList | 查看Topic所属集群。 |
| topicRoute | 查看Topic路由信息。 |
| updateTopicPerm | 更新Topic读写权限。 |
| topicStatus | 查看Topic统计信息。 |
| brokerStatus | 查看Broker状态。 |
| wipeWritePerm | 清除特定Broker权限。 |
| updateBrokerConfig | 更新Broker配置。 |
| producerConnection | 查看Producer连接状态。 |
| consumerConnection | 查看Consumer的连接状态。 |
| brokerConsumerStats | 查看Broker所有GID消费状态。 |
| updateSubGroup | 创建（修订）订阅组。 |
| deleteSumGroup | 删除订阅组。 |
| consumerProgress | 查看订阅组消费状态。 |
| consumerStatus | 获取Consumer消费进度。 |
| queryMsgById | 根据消息ID查询消息。 |
| queryMsgByKey | 根据消息Key查询消息。 |
| queryMsgByOffset | 根据消息Offset查询消息。 |

消息队列

| printMsg | 查看Topic指定时间的消息。 |
|---|---|
| clusterList | 查看集群信息。 |
| resetOffsetByTime | 重置位点。 |

### 创建Topic

表 1. updateTopic

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -b | 如果-c为空，则必填 | Broker 地址，表示Topic 建在该Broker。 |
| -c | 如果-b为空，则必填 | Cluster 名称，表示Topic 建在该集群（集群可通过clusterList 查询）。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |
| -p | 否 | 指定新Topic 的权限限制（W\|R\|WR）。 |
| -r | 否 | 可读队列数（默认为8）。 |
| -w | 否 | 可写队列数（默认为8）。 |
| -t | 是 | Topic 名称。 |

### 删除Topic

本命令为高危操作，请谨慎执行。 表 1. deleteTopic

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -c | 是 | Cluster名称，表示删除某集群下的某个Topic （集群可通过clusterList 查询）。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |
| -p | 是 | Topic名称。 |

消息队列

### 查看Topic列表信息

表 1. topicList

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |

### 查看Topic所属集群

表 1. topicClusterList

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -n | 是 | Name Server地址，例如：192.168.0.1:9876。 |
| -t | 是 | Topic名称。 |

### 查看Topic路由信息

表 1. topicRoute

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -t | 是 | Topic名称。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |

### 更新Topic读写权限

本命令为高危操作，请谨慎执行。 表 1. updateTopicPerm

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -b | 如果-c为空，则必填 | Broker地址。 |
| -c | 如果-b为空，则必填 | Cluster名称。 |
| -p | 是 | 权限：2：只写；4：只读；6：读写。 |
| -t | 是 | Topic名称。 |
| -n | 是 | Name Server服务地址列表，格式为ip:port;ip:port。 |

消息队列

### 查看Topic统计信息

表 1. topicStatus

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -t | 是 | Topic名称。 |

### 查看Broker状态

表 1. brokerStatus

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -b | 如果-c为空，则必填 | Broker地址，例如：11.164.190.48:10911。 |
| -c | 如果-b为空，则必填 | Cluster名称。 |
| -n | 是 | Name Server地址，例如：192.168.0.1:9876。 |

### 清除特定Broker权限

本命令为高危操作，请谨慎执行。 表 1. wipeWritePerm

| 是否必填 | 说明 |
|---|---|
| 是 | Broker名称。 |

### 更新Broker配置

**updateBrokerConfig**

更新Broker配置的命令为 `updateBrokerConfig` ，命令参数如下表所示。 本命令为高危操作，请谨慎执行。

**重要**

表 1. 命令参数

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -b | 如果-c为空，则必填， 且-b和-c只能同时填写一个。 | Broker的IP地址。格式为<BrokerIP:Port>，端口号固定为10911。 |

消息队列

| -c | 如果-b为空，则必填， 且-b和-c只能同时填写一个。 | Broker所在的集群名称。集群可通过 clusterList 查询。 |
|---|---|---|
| -k | 是 | Broker配置项名称。具体配置项及说明，请参见下文Broker配置项说明。 |
| -v | 是 | Broker配置项的值。具体配置项及说明，请参见下文Broker配置项说明。 |
| -n | 是说明如果该命令在Broker 所在容器中执行， 该参数可以不用填写，系统会自动查询Name Server 服务地址。 | Name Server服务地址列表，格式为<ip:port;ip:port>。 |

**Broker配置项说明**

`updateBrokerConfig` 命令中，Broker的配置项**-k**和**-v**的取值说明如下。

| Broker配置项名称（-k） | Broker配置项取值（-v） | 说明 |
|---|---|---|
| runtimeWriteMessageEncrypt Enable | 运行时加密开关。控制RocketMQ运行时写消息是否开启KMS加密。 该配置项取值如下： true：开启加密开关。 false：关闭加密开关。 默认值：true。 | 建议在Broker主备节点上保持开关状态一致，避免因准备节点切换造成开关状态和预期不一致。 例如，主节点开启，备节点关闭，主备节点切换后，主节点开关变成关闭了，和预期要求不一致。 |
| enableSendFlowlimit | 实例限流开关。控制RocketMQ是否会对实例的消息发送TPS进行限流。 消息发送TPS若超过规格上限值，RocketMQ服务端会直接拒绝生产者发送的消息。 该配置项取值如下： true：开启实例限流开关。 false：关闭实例限流开关。 默认值：false。 | 实例消息发送TPS的上限值可在控制台实例详情页面查看。 实例限流开关打开后，还需要打开前端功能开关，具体操作，请参见实例限流运维操作。 |

**使用示例**

示例中的<BrokerIP:10911>、<ClusterName>请替换为您实际的Broker的IP地址和集群名

**重要**

称。 关闭某个Broker的加密开关：

| -b <BrokerIP:10911> |  |  |
|---|---|---|
| -k runtimeWriteMessageEncryptEnable |  |  |
| -v false |  |  |

消息队列

```
sh /home/admin/rmq/bin/mqadmin updateBrokerConfig -b <BrokerIP:10911> -k runtimeWriteMessageEncryptEnable -v false
```

关闭某个集群所有Broker的加密开关：

| -c <ClusterName> |  |
|---|---|
| -a all |  |
| -k runtimeWriteMessageEncryptEnable |  |
| -v false |  |

```
sh /home/admin/rmq/bin/mqadmin updateBrokerConfig -c <ClusterName> -a all -k runtimeWrite MessageEncryptEnable -v false
```

若不支持使用 `-a` 命令，则需要使用 `-b` 命令手动替换所有Broker的IP地址，依次将集群

**说明**

下所有准备节点开关都统一修改。如果仅使用 `-c` 命令，仅修改主节点的开关，会造成主备节点切换后开关状态和预期不符。 开启某个Broker的实例限流开关：

| -b <BrokerIP:10911> |  |  |
|---|---|---|
| -k enableSendFlowlimit |  |  |
| -v true |  |  |

```
sh /home/admin/rmq/bin/mqadmin updateBrokerConfig -b <BrokerIP:10911> -k enableSendFlowlimit -v true
```

### 查看Producer连接状态

表 1. producerConnection

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -g | 是 | 发送者GID，该参数根据实例是否有命名空间而异： 有命名空间：instanceid%gid 无命名空间：gid |
| -t | 是 | Topic名。 |

### 查询Consumer的网络连接

表 1. consumerConnection

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -g | 是 | 订阅组的Group ID。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |

### 查看Broker所有GID消费状态

表 1. brokerConsumeStats 消息队列

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -b | 是 | Broker地址，例如：11.164.190.48:10911。 |
| -t | 否 | 超时时间，单位毫秒，默认50000毫秒。 |

### 创建（修订）订阅组

表 1. updateSubGroup

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -b | 如果-c为空，则必填 | Broker地址，表示Topic建在该Broker。 |
| -c | 如果-b为空，则必填 | Cluster名称，表示Topic建在该集群（集群可通过clusterList 查询）。 |
| -g | 是 | 订阅组名。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |
| -d | 否 | 是否容许广播方式消费。 |
| -m | 否 | 是否容许从队列的最小位置开始消费，默认会设置为false。 |
| -q | 否 | 消费失败的消息放到一个重试队列，每个订阅组配置几个重试队列。 |
| -r | 否 | 重试消费最大次数，超过则投递到死信队列，不再投递。 |
| -s | 否 | 消费功能是否开启。 |

### 删除订阅组

本命令为高危操作，请谨慎执行。表 1. deleteSubGroup

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -b | 如果-c为空，则必填 | Broker地址，表示Topic建在该Broker。 |
| -c | 如果-b为空，则必填 | Cluster名称，表示Topic建在该集群（集群可通过clusterList 查询）。 |
| -g | 是 | 订阅组名。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |

### 查看订阅组消费状态

表 1. consumerProgress

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -g | 是 | 订阅组的Group ID。该参数根据实例是否有命名空间而异： 有命名空间：instanceid%gid 无命名空间：gid |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |

消息队列

### 获取Consumer消费进度

表 1. consumerStatus

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -g | 是 | 订阅组名。 |
| -i | 否 | Consumer客户端IP地址。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |
| -s | 否 | 打印堆栈信息。 |

### 根据消息ID查询消息

表 1. queryMsgById

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -i | 是 | 消息ID。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |

### 根据消息Key查询消息

表 1. queryMsgByKey

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -k | 是 | 消息设置的key内容。 |
| -t | 是 | Topic名称。 |
| -n | 是 | Name Server服务地址列表，格式ip:port;ip:port。 |

### 根据消息offset查询消息

表 1. queryMsgByOffset

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -o | 是 | 消息位点。 |

消息队列

| -i | 是 | 队列id。 |
|---|---|---|
| -b | 是 | Broker地址，表示Topic建在该Broker。 |
| -t | 是 | Topic名称。 |

### 查看Topic指定时间的消息

表 1. printMsg

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -b | 是 | 开始时间。 格式为：yyyy-MM-dd#HH:mm:ss:SSS。 |
| -e | 是 | 结束时间。 格式为：yyyy-MM-dd#HH:mm:ss:SSS。 |
| -d | 否 | 是否打印消息体。 |
| -s | 否 | 消息标签，默认：*，格式：TagA \|\| TagB。 |
| -c | 否 | 编码格式，例如：UTF-8,GBK。 |
| -t | 是 | Topic名。 |

### 查看集群消息

表 1. clusterList

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| -m | 是 | 打印集群的统计信息。 |
| -i | 否 | 循环打印间隔时间，单位为秒。 |
| -n | 是 | Name Server服务地址列表，格式为ip:port;ip:port。 |

### 重置消费位点

此命令可能会导致消息被重复消费或被跳过不消费。 表 1. resetOffsetByTime

| 参数名称 | 是否必填 | 说明 |
|---|---|---|

消息队列

| -g | 是 | 消费者GID。该参数根据实例是否有命名空间而异： 有命名空间：instanceid%gid 无命名空间：gid |
|---|---|---|
| -s | 是 | 时刻：yyyy-MM-dd#HH:mm:ss:SS。 |
| -t | 是 | Topic名。 |

消息队列

## 运维操作

### 实例限流运维操作

RocketMQ实例限流功能默认关闭，系统不会对消息发送TPS进行限制。若您需要对消息发送TPS进行限制，可通过本操作开启实例限流功能。

**背景信息**

实例限流功能开启后，若消息发送TPS超过规格限制，RocketMQ会拒绝接收超过上限的消息。

**前提条件**

RocketMQ所属集群已增量部署限流组件**MQFlowLimit**。 MQFlowLimit中的tokenserver服务容器和Broker的容器完成时钟同步，否则会影响限流准确性。

**注意事项**

本操作为高危操作，可能对业务产生影响。操作前需要做变更申请，向产品侧以及客户侧咨询确认方可执行。 增量部署限流组件后需要回滚RocketMQ集群，Console组件会重启，Broker并不会重启。 限流组件部署后，存量实例默认不限流，只有新建实例和更新了Broker配置的存量实例会限流。您可以登录 onsflowlimit数据库中的flow_limit表查看哪些实例存在限流。

**步骤一：开启限流开关**

1. 登录消息队列运维·RocketMQ控制台。
2. 在左侧导航栏，单击**Broker** **管理**。
3. 在**Broker****管理**页面，单击Broker名称或**操作**列的**查看**。
4. 在**Broker****详情**页面，单击**配置信息**页签。
5. 在**配置名**搜索框中，输入**enableSendFlowlimit**。
6. 单击**enableSendFlowlimit**配置项右侧的**修改**。
7. 在**修改配置**对话框中，开启**配置值**，然后单击**确定**。

**重要**

请依次开启所有集群下的每个Broker的限流开关。

**步骤二：打开实例限流报表**

1. 登录UiConsole控制台。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏，选择**平台运维** **> UniConsole****管控研发平台**。
2. 在**产品列表**页面的搜索框输入**mq**，然后单击**搜索**。
3. 在搜索结果中找到**rocketmq**，在其**操作**列单击**开关列表**。
`privateCloud.trafficLimit`并单击**搜索**。
4. 在**rocketmq** **开关列表**页面中的搜索框输入
5. 在搜索结果中找到**privateCloud.trafficLimit**，打开其**当前值**列的开关。
消息队列

## 容量评估

### Name Server组件

**连接数指标**

**当前水位统计：**

进入mq-namesrv容器执行 `ss -s` 。

**基准和警戒水位：**

当连接数超过规格的一半时，请联系运维工程师处理。

### Broker组件

**连接数指标**

**当前水位统计：**

进入mq-broker容器执行 `ss -s` 。

**基准和警戒水位：**

当连接数超过规格的一半时，请联系运维工程师处理。 消息队列

## 日志参考

在运维过程中，您可以通过日志了解RocketMQ各组件的状态或定位故障。本文将罗列出RocketMQ组件的所有日志的路径，并提供相关说明。 您也可以使用专有云运维平台**日志中心**的**日志查询**功能对RocketMQ产品的部分日志进行查询和分析，详情请参见《**Apsara Uni-manager****运维控制台****用户指南》** > **《平台运维》** > **《日志中心》** > **《日志查询》**。 表 1. RocketMQ组件日志

| 组件 | 文件 | 说明 |
|---|---|---|
|  | /home/admin/logs/rocketmqlogs/ broker.log | 关键字：Register broker to name server 通过 register 信息确认 broker 的注册：Register broker to name server {ip} OK，标识该 broker 已在 namesrv 上注册，即 clusterlist 可查到该 broker。 |
|  | /home/admin/logs/rocketmqlogs/ remoting.log | 根据 Client 端 IP 判断网络何时断开； RocketMQ有很多调用 remoting 工程，该日志使用较少。 |
|  | /home/admin/logs/rocketmqlogs/f ailover controller.log _ | 主备切换，关注状态机切换的时间点。 |
|  | /home/admin/logs/rocketmqlogs/f ilter.log | 控制结果的过滤； RocketMQ 现采用类似 tag 表达式的方式配置过滤条件。 |
|  | /home/admin/logs/rocketmqlogs/l ock.log | 关键字：tryLockBatch consumer 分配 queue 的绑定关系：一个 queue 最多只分配给一个 consumer 实例； 下线后会有 unlockBatch 日志。 |

消息队列

|  | /home/admin/logs/rocketmqlogs/t ime.log | 定时消息，定时消息在 server 端先存入 DB，DB 通过轮询服务检查快要到发送时间的消息，再通过 broker 发送； 关键字： Scan add infly 当发生定时消息未投递或投递时间不准时，可通过关键字查看：Scan add infly: msgID。表示消息从 DB 中捞出，放入 broker 投递的时间点； 通过查询 msgID 在 time.log 中捞出的时间点，结合轨迹，可说明流程何处发生了阻塞，卡顿，何处慢了。 |
|---|---|---|
|  | /home/admin/logs/rocketmqlogs/t ransaction.log | 事务消息，半事务消息，同样会通过 server 先存入 DB； 部分消息为事务半决状态，未commit 的半事务会通过 DB 扫描定时向 producer 询问事务确认。 |
|  | /home/admin/logs/rocketmqlogs/ stats.log | 记录当前的 broker tps。用于查阅历史的 tps 问题。资源报表，也是由这里的日志汇总得到。 关键字： BROKER PUT NUMS 每分钟写消息 _ _ TPS 流量监控； BROKER GET NUMS 每分钟读消息 _ _ TPS 流量监控； 可用于某个时间点发送消息失败/写消息失败的排查； 结合 TLOG 使用，看报表。 |
| mq-broker |  |  |
|  | /home/admin/logs/rocketmqlogs/ store.log | TPS 的宏观统计； 关键字：PAGECACHERT totalput —— 写入量； putmessagedistributetime —— 快速落盘消息数量，按耗时分类（10 ms以内正常）； 可用于 TPS 低问题的排查，常用于压测的时候关注延迟问题。 （commitLog 串行写入，在这里体现明显） |

消息队列

|  | /home/admin/logs/rocketmqlogs/ dup.log | 主备切换，主备相关信息； broker row SYNC MASTER 状态 _ 状态机状态： 1. orignal-state： NULL STATE _ 2. singal-master-state： ONLY MASTER _ 3. async-sync-state： ASYNC STATE _ 4. semi-sync-state：HALF SYNC _ 5. sync-state：SYNC STATE _ 服务启动后的状态机及转换过程： 服务启动时为orignal-state初始状态， 当主机启动后，置为ONLY MASTER _ 状态； 启动备机并开始将消息以异步状态同步至备机，主机继续写请求； 当消息同步的位点差异在100条消息以内时，hold 主机的写请求， (HALF SYNC)备机继续异步复制； _ 直至全部写完，即转化为同步复制状态（SYNC STATE）； _ CONTROLLER决定谁是主机谁是备机。 专有云99.99%基本是主备同步部署； 关键字：DuplicationStatus voteDupoffset标识位点，若一直在增长，表示消费正常位移。 |
|---|---|---|
|  | /home/admin/logs/rocketmqlogs/ dup-stats.log | 性能监控：任务数，备机写延迟，本地写延迟。 |
|  | /home/admin/logs/rocketmqlogs/ dup-study.log | 主备机异步复制状态。 |
|  | /home/admin/logs/rocketmqlogs/ broker default.log _ | WATERMARK数据，排查意义不大。 |
|  | /home/admin/logs/rocketmqlogs/ rocketmq.log | 排查意义不大。 |

消息队列

|  | /home/admin/logs/spas/spas sdk. _ log | 鉴权信息，权限，validate。 authorized。 根据AK获取阿里云用户的UID在DB里确认创建的 topic 匹配。确认是否授权。 权限规则：控制台用的哪个账号创建 TOPIC client 端口就要用哪个账号的 Access-Key Security-Key。 |
|---|---|---|
| mq-namesrv | /home/admin/logs/spas/spas sdk. _ log | 鉴权信息，权限，validate。 authorized。 根据AK获取阿里云用户的 UID 在DB 里确认创建的 topic 匹配。确认是否授权。 权限规则：控制台用的哪个账号创建 TOPIC client 端口就要用哪个账号的 Access-Key Security-Key。 |
|  | /home/admin/logs/rocketmqlogs/ namesrv.log | 无。 |
| mq-console | /home/admin/logs/spas/spas sdk. _ log | 鉴权信息，权限，validate。 authorized。 根据AK获取阿里云用户的 UID 在 DB 里确认创建的 topic 匹配。确认是否授权。 权限规则：控制台用的哪个账号创建 TOPIC client 端口就要用哪个账号的 Access-Key Security-Key。 |
|  | /home/admin/rmq/ons- api/register.log | 用户查询； Topic增删改查； GID增删改查。 |
|  | /home/admin/rmq/ons- api/rest.log | 展现控制台操作的异常。 |
| Mq-cai | /home/admin/cai/logs/error.log | 地址服务器运行错误日志。 |
|  | /home/admin/cai/logs/access.log | 地址服务器访问日志。 |
| Mq-controller | /home/admin/logs/rocketmqlogs/f ailover controller.log _ | RocketMQ broker主备切换日志，有日志就需要观察和分析是否正常。 |
| Mq-housekeeping | /home/admin/logs/aliware-mq- hkagent/warning.log | RocketMQ自带巡检工具，保存检查结果，所有日志都需要进行观察并分析其是否正常。 |

消息队列
