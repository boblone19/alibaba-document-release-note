---
title: "网关 云原生网关 用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 156
source_pdf: "34_云原生网关 用户指南_user-guide-1.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/apigateway/zh/user-guide-1.pdf"
converter: line-classifier (PyMuPDF)
---

# 网关 云原生网关 用户指南

## 产品概述

### 什么是云原生网关

云原生网关是一款集成流量网关、微服务网关和安全网关的统一网关产品，基于开源 Istio 与 Envoy 构建，旨在为 Kubernetes 环境提供统一、高性能、易运维的入口网关解决方案。 作为云原生网关，具备以下核心特性： 三合一架构：实现了流量网关 + 微服务网关 + 安全网关三合一的高集成能力，简化架构、降低链路延迟与运维复杂度。 深度生态集成：原生支持 Dubbo、Nacos、Sentinel 等主流微服务组件，适用于复杂的云原生应用体系。 动态配置与可观测性：通过 Kubernetes CRD 实现声明式配置，支持热更新、实时监控与日志追踪，满足生产级稳定性要求。 高性能与可扩展：以 Envoy 为数据面，具备高并发、低延迟的处理能力，并可通过插件机制灵活扩展功能。

## 快速入门

### 登录云原生网关控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。

**说明**

单击页面右上角的当前语言可以切换其它语言。 授权登录是第三方认证中配置了全局IdP设置才会显示，且“授权登录”名称用户可按需自定义。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 单击**账号登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：

**管理员强制开启MFA后的首次登录**

a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**账号登录**。 c. 输入6位MFA码后单击**认证**。

**您已开启并绑定MFA**

输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《 Apsara Uni-manager运营控制台用户指南》的**管理多因素认** 证章节。
5. 在顶部菜单栏选择**产品** > **中间件** > **应用集成** **> API** **网关**，进入**API Gateway 2.0**控制台。

**说明**

云原生网关与API网关共享同一个控制台入口。

### 路由管理

路由是网关对外暴露访问能力的主要方式，本文主要介绍了如何管理路由。

**创建路由**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**，然后单击**创建路由**。
5. 在**创建路由**面板中，根据页面提示配置相关参数后，单击**确定**。

| 配置项 | 说明 |
|---|---|
| 路由名称 | 自定义创建的路由名称。 重要路由名称必须全局唯一。 |

| 路由路径 | 配置路由匹配的路径和匹配方式，匹配方式支持前缀匹配、精确匹配、正则匹配。 |
|---|---|
| 请求方法 | 匹配的请求方法，若不指定请求方法，路由匹配时将匹配任何请求方法。 |
| 请求Header | 匹配的请求Header，多个Header之间是与关系。 |
| 请求Query | 匹配的请求Query，多个Query之间是与关系。 |
| 后端服务 | 关联的多个后端服务并支持配置后端服务权重。 |
| 域名 | 访问路由使用的域名，支持选择多个域名。 说明域名与基本路径（BasePath）的组合全局唯一， 不可重复。 |

**查看路由详情**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. （可选）在**路由管理**页面，可根据**路由名称**或**服务名称**快速筛选路由。
6. 在路由列表中，单击路由名称，进入**路由详情**页面，可查看**路由详情**、**插件配置**以及**策略配置**信息。
在**路由详情**页签，可查看路由的详细信息，包括**基本信息**、**关联服务**、**关联域名**等。 单击**插件配置**页签，可管理当前路由绑定的插件；单击**添加插件**，可为路由绑定插件，具体操作请参考创建插件。

**说明**

在路由列表页面，单击**操作**列的**插件配置**，也可直接跳转到**插件配置**页签。 单击**策略配置**页签，可进行策略重写、Header修改、超时以及降级等配置，具体请参考策略配置。

**修改路由**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. 在路由列表中，单击目标路由**操作**列的**编辑**。
6. 在**编辑路由**面板，根据实际需求修改路由信息，单击**确定**。

**删除路由**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. 删除路由。
单个删除：在路由列表中，单击目标路由**操作**列的**删除**。 批量删除：在路由列表中，勾选目标路由，单击**批量删除**。
6. 在弹出的**提示**对话框中，单击**确定**。

## 操作指南

### 网关管理

#### 创建网关实例

本文介绍如何创建云原生网关实例。

**前提条件**

已创建K8s集群，具体请参考**《容器服务****ACK** **用户指南》** > **创建****Kubernetes****集群**章节。

**操作步骤**

1. 登录容器服务控制台。
2. 在左侧导航栏，单击**集群**。
3. 在**集群列表**页面，单击目标集群名称或者目标集群右侧**操作**列的**详情**。
4. 在左侧导航栏，单击**运维管理** > **组件管理**。
5. 在**组件管理**页面，找到API Gateway Ingress Controller组件，然后单击组件卡片下方的**安装**。
6. 在弹出的对话框中，可选择是否勾选**Create public network service**，然后单击**确定**。
**Create public network service**：创建公网访问服务。

**说明**

组件卡片显示**已安装**，表明组件安装成功。

#### 查看网关实例详情

本文介绍如何在云原生网关控制台查看云原生网关实例的详细信息。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. （可选）在**网关实例**页面，可根据**实例名称**和**实例****ID**快速筛选目标实例。
4. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
5. 在左侧导航栏，选择**概览**页面，可查看云原生网关实例的**基本信息**、**接入点**和**可观测**信息。
**基本信息**页签：
**网关总览**：展示当前云原生网关实例的**路由总数**、**消费者数**、**服务总数**以及**策略总数**。
**基本信息**：展示当前云原生网关实例的**实例****ID**、**实例名称**、**状态**、**部署架构**、**集群**、**命名空间**、创
**建时间**、**修改时间**、**引擎类型**。
**可观测**：可选择开启或关闭云原生网关实例的**日志服务**和**监控插件**。
**日志服务**：开启后将自动收集实例日志到SLS日志服务。
**监控插件**：开启后将启用Prometheus监控指标收集。
**接入点**页签：展示实例的接入点信息，包括**类型**、**网络类型**、**ServiceName**、**External**
**IPs**、**Ports**以及**ClusterIP**。

#### 修改网关实例

本文介绍如何修改云原生网关实例名称。

**操作步骤**

**说明**

仅支持修改实例名称。
1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标实例**操作**列的
，然后单击**编辑**。
4. 在**编辑实例**页面，修改**实例名称**后，单击**提交**。

#### 释放云原生网关实例

如果您无需再使用云原生网关，可以通过释放实例来关闭云原生网关。

**注意事项**

实例释放后，该实例将会被删除，其数据均被删除，请谨慎操作。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标实例**操作**列的
，然后单击**注销**或**强制注销**。
4. 在弹出的**提示**对话框中，单击**确定**。

#### 停止网关实例

本文介绍了如何停止云原生网关实例。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标实例**操作**列的
，然后单击**停机**。
4. 在弹出的**提示**对话框中，单击**确定**，在实例列表中可以看到**实例状态**变为**停机**。

#### 重启网关实例

本文介绍了如何启动云原生网关实例。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标实例**操作**列的
，然后单击**重启**。
4. 在弹出的**提示**对话框中，单击**确定**，在实例列表中可以看到**实例状态**变为**运行中**。

#### 设置安全组规则

云原生网关和后端服务所在的节点分别处于不同安全组内。您可以通过设置安全组规则为云原生网关授予访问后端服务的权限。

**背景信息**

安全组是一种虚拟防火墙，用于控制安全组内ECS实例和ENI网卡的入流量和出流量，从而提高ECS实例的安全性。安全组具备状态检测和数据包过滤能力，您可以基于安全组的特性和安全组规则的配置在云端划分安全域，详情请参见**《云服务器** **ECS** **用户指南》** > **安全组概述**章节。 因为云原生网关和后端服务所在的节点分别处于不同安全组内，需要您在后端服务的安全组内为云原生网关授予必要的端口范围访问权限。 上图展示了如何通过云原生网关实现不同类型服务的网络安全访问控制和流量分发，连接关系如下： 从左侧的客户端设备（如电脑），通过云原生网关进入内部网络。 云原生网关根据配置将流量分别转发到service-sg1和service-sg2。 service-sg1中的Pod可以处理来自8080/8080端口的请求。 service-sg2中的ECS可以处理来自80/9000端口的请求。

**步骤一：获取网关实例所在节点的网段**

1. 登录容器服务Kubernetes版控制台，在左侧导航栏选择**集群**。
2. 在**集群列表**页面，单击目标集群名称，然后在左侧导航栏，选择**节点管理** > **节点池**，单击节点池名称。
3. 在**节点池**页面，**节点配置**信息中获取**节点虚拟交换机**的ID。
4. 登录专有云网络VPC控制台，在左侧导航栏单击**交换机**。
5. 在**交换机**页面，单击步骤3中获取的虚拟交换机ID。
6. 在**交换机详情**页面的**基本信息**页签，获取IPv4网段对应的值，即虚拟交换机所在的网段。

**步骤二：获取目标服务所在节点的安全组**

云原生网关关联的上游服务，主要包括容器部署和ECS部署。您可以通过以下方式获取安全组ID：

**目标服务部署在容器服务ACK中**

1. 登录容器服务Kubernetes版控制台，在左侧导航栏选择**集群**。
2. 在**集群列表**页面，单击目标集群名称，然后在左侧导航栏，选择**节点管理** > **节点池**，单击节点池名称。
3. 在**节点池**页面的**节点池信息**区域中获取安全组的ID。

**目标服务部署在ECS上**

1. 登录云服务器ECS控制台。
2. 在左侧导航栏，选择**实例与镜像** **> ECS****实例**。
3. 在**ECS****实例**页面，单击目标服务所部署的ECS实例，然后单击**安全组**页签，获取安全组的ID。

**步骤三：添加安全组授权规则**

1. 登录云服务器ECS控制台。
2. 在左侧导航栏，选择**网络与安全** > **安全组**，单击步骤二中获取的目标服务所在节点的安全组ID。
3. 单击**安全组规则**页签，在**入方向**中单击**添加安全组规则**，配置以下参数后，单击**确定**。

| 参数 | 说明 | 示例 |
|---|---|---|
| 端口范围 | 输入安全组授权的端口范围。 | 1/65535 |
| 优先级 | 输入安全组规则的优先级。 | 1 |
| 授权类型 | 选择IPv4地址段访问。 | IPv4地址段访问 |
| 授权对象 | 填写步骤一中获取的网关实例所在节点的网段。 | 172.16.0.2/24 |

**删除安全组授权规则**

1. 登录云服务器ECS控制台。
2. 在左侧导航栏，选择**网络与安全** > **安全组**，单击步骤二中获取的目标服务所在节点的安全组ID。
3. 单击**安全组规则**页签，根据需要选择一种方式删除安全组授权规则。
方式一：单击目标安全组规则**操作**列的**删除**。 方式二：单击目标安全组规则**操作**列的**修改属性**，然后在**修改属性**对话框中删除对应安全组授权的IP范围。

**常见问题**

**问题一：安全组已经授权，为什么服务还是访问不通？**

您可以按照如下步骤自助排查：
1. 首先需要确认您的目标服务所部署的节点是否正确。
有可能存在服务部署在了A节点上，但是给B节点所在的安全组授权。
2. 您的目标节点是否设置了多个安全组。
如果是多个安全组，建议给每个安全组都授权。

**问题二：安全组已经授权，之前网关访问服务是通的，现在突然间不通了，是什么**

**原因？**

您可以按照如下步骤自助排查：
1. 首先确认您的服务本身没有问题。
您可以对同一安全组内的其他节点使用 `curl` 命令检查服务的连通性。
2. 确认您发布的服务对外暴露的端口是否有变更。
例如以前端口为8080，在云原生网关只给8080端口授权了，之后又将端口变更为8081，这时需要重新调整云安全组授权规则端口。为了避免这种情况发生，建议您在配置安全组授权时扩大端口范围，可以将范围选成1/65535。

### 路由管理

路由是网关对外暴露访问能力的主要方式，本文主要介绍了如何管理路由。

**创建路由**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**，然后单击**创建路由**。
5. 在**创建路由**面板中，根据页面提示配置相关参数后，单击**确定**。

| 配置项 | 说明 |
|---|---|
| 路由名称 | 自定义创建的路由名称。 重要路由名称必须全局唯一。 |
| 路由路径 | 配置路由匹配的路径和匹配方式，匹配方式支持前缀匹配、精确匹配、正则匹配。 |

| 请求方法 | 匹配的请求方法，若不指定请求方法，路由匹配时将匹配任何请求方法。 |
|---|---|
| 请求Header | 匹配的请求Header，多个Header之间是与关系。 |
| 请求Query | 匹配的请求Query，多个Query之间是与关系。 |
| 后端服务 | 关联的多个后端服务并支持配置后端服务权重。 |
| 域名 | 访问路由使用的域名，支持选择多个域名。 说明域名与基本路径（BasePath）的组合全局唯一， 不可重复。 |

**查看路由详情**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. （可选）在**路由管理**页面，可根据**路由名称**或**服务名称**快速筛选路由。
6. 在路由列表中，单击路由名称，进入**路由详情**页面，可查看**路由详情**、**插件配置**以及**策略配置**信息。
在**路由详情**页签，可查看路由的详细信息，包括**基本信息**、**关联服务**、**关联域名**等。 单击**插件配置**页签，可管理当前路由绑定的插件；单击**添加插件**，可为路由绑定插件，具体操作请参考创建插件。

**说明**

在路由列表页面，单击**操作**列的**插件配置**，也可直接跳转到**插件配置**页签。 单击**策略配置**页签，可进行策略重写、Header修改、超时以及降级等配置，具体请参考策略配置。

**修改路由**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. 在路由列表中，单击目标路由**操作**列的**编辑**。
6. 在**编辑路由**面板，根据实际需求修改路由信息，单击**确定**。

**删除路由**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. 删除路由。
单个删除：在路由列表中，单击目标路由**操作**列的**删除**。 批量删除：在路由列表中，勾选目标路由，单击**批量删除**。
6. 在弹出的**提示**对话框中，单击**确定**。

### 策略配置

#### 配置重写策略

通过配置重写策略，您可以在将请求转发给目标后端服务之前修改请求的路径和主机域，以满足特定的业务环境和架构要求。重写策略能够精确地控制请求的路径和主机域，并确保将请求正确地路由到适当的服务或端点。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. 在路由列表中，单击路由名称，进入**路由详情**页面。
6. 在**路由详情**页面，单击**策略配置**页签。
7. 在**策略配置**页签，单击**重写**，然后单击**开启**按钮，配置**路径重写**和**Host****重写**，单击**保存**。

**说明**

**路径重写**和**Host****重写**配置说明请参考重写策略。

**重写策略**

重写主要用于修改原始请求的路径（Path）和主机域（Host）。

**路径（Path）重写**

对于路径（Path）重写，云原生网关支持两种重写模式：精确重写和前缀重写。

**精确重写**

精确重写可以完全修改原始请求的Path。

**示例**

原始请求的Path为 `/app/test` ，但转发给后端服务的Path为 `/foo/bar` ，建议配置方式如下： 路由匹配条件：匹配方式为精确匹配，Path为 `/app/test` 。 重写：重写方式为精确重写，Path为 `/foo/bar` 。

|  | 重要精确重写要求路由的匹配方式为精确匹配或正则匹配，前缀匹配不支持精确重写。 |  |
|---|---|---|

**前缀重写**

前缀重写可以修改原始请求的Path前缀。

**示例一**

原始请求的Path为 `/app/test` ，但转发给后端服务的Path为 `/test` ，配置方式建议如下： 路由匹配条件：匹配方式为前缀匹配，Path为 `/app` 。 重写：重写方式为前缀重写，Path为 / 。

**示例二**

原始请求的Path为 `/v1/test` ，但转发给后端服务的Path为 `/v2/test` 。配置方式建议如下： 路由匹配条件：匹配方式为前缀匹配，Path为 `/v1` 。 重写：重写方式为前缀重写，Path为 `/v2` 。

**重要**

前缀重写要求路由的匹配方式为前缀匹配，精确匹配和正则匹配不支持前缀重写。由于路由匹配方式为前缀匹配且可以匹配所有带有指定前缀Path的请求，所以您在配置前缀重写时需要关注是否需要对所有这些请求进行重写，否则建议使用精确重写。

**主机域（Host）重写**

对于主机域（Host）重写，云原生网关支持精确重写。 例如，原始请求的Host为 `test.com` ，但转发给后端服务的Host为 `dev.com` ，在重写策略中将重写主机设置为 `dev.com` 。

#### 配置Header修改策略

在请求转发给目标后端服务或后端服务的响应返回给客户端之前，Header修改策略可以修改原始请求中的 Header。本文介绍云原生网关如何设置请求和响应的Header。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. 在路由列表中，单击路由名称，进入**路由详情**页面。
6. 在**路由详情**页面，单击**策略配置**页签。
7. 在**策略配置**页签，单击**Header** **修改**。
8. 在**Header** **修改**区域，根据实际情况配置相关参数，然后单击**保存**。

| 参数 | 说明 |
|---|---|

| 开启 | 开启：开启Header修改策略后，网关会控制请求和响应的Header。 关闭：关闭Header修改策略后，网关不会控制请求和响应的Header。 |
|---|---|
| 新增请求头 | 单击新增，输入Header名称和值，向请求新增一个 Header。 说明如果新增的Header已存在，那么Header值将会拼接在已有的Header值后面，并通过英文逗号 （,）分隔。 |
| 修改请求头 | 单击新增，输入Header名称和值，修改请求指定的 Header。 说明如果指定的Header不存在，将会按照 Header名称和Header值进行新增操作。 如果指定的Header存在，将会进行覆盖修改操作。 |
| 删除请求头 | 单击新增，输入Header名称，删除请求指定的 Header。 |
| 新增响应头 | 单击新增，输入Header名称和值，向响应新增一个 Header。 说明如果新增的Header已存在，那么Header值将会拼接在已有的Header值后面，并通过英文逗号 （,）分隔。 |
| 修改响应头 | 单击新增，输入Header名称和值，修改响应指定的 Header。 说明如果指定的Header不存在，将会按照 Header名称和Header值进行新增操作。 如果指定的Header存在，将会进行覆盖修改操作。 |
| 删除响应头 | 单击新增，输入Header名称，删除响应指定的 Header。 |

**结果验证**

假设添加一个测试的响应Header，如下图所示，您可以根据实际业务场景进行设置。 执行以下测试请求命令：

```bash
curl -I http://121.196.XX.XX/demo/item/list // 网关入口IP
```

响应结果（返回带有 `test:demo` 的Header值）：

```
HTTP/1.1 200 OK x-content-type-options: nosniff x-xss-protection: 1; mode=block cache-control: no-cache, no-store, max-age=0, must-revalidate pragma: no-cache expires: 0 x-frame-options: DENY content-type: application/json content-length: 86 date: Tue, 30 Nov 2021 03:03:04 GMT x-envoy-upstream-service-time: 4 test: demo server: istio-envoy
```

#### 配置超时策略

云原生网关提供路由级别的超时设置，您可以按需为指定路由配置网关等待请求响应结果的最大时间。如果在指定时间内，网关未收到后端服务的响应结果，网关会向客户端返回一个HTTP状态码为504（Gateway Timeout）的响应结果。本文介绍如何为云原生网关配置路由超时策略。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. 在路由列表中，单击路由名称，进入**路由详情**页面。
6. 在**路由详情**页面，单击**策略配置**页签。
7. 在**策略配置**页签，单击**超时**。
8. 在**超时**区域配置相关参数，然后单击**保存**。

**说明**

超时策略配置完成且开启后，请根据实际业务验证服务超时规则是否生效。

| 参数 | 描述 |
|---|---|
| 开启 | 路由超时策略的启用开关。 开启：网关路由超时策略生效。 关闭：网关路由超时策略失效。 |
| 超时时间 | 为当前路由设置超时时间，单位为秒。 说明当设置为0或者关闭超时策略时，表示网关会一直等待请求的响应结果。 |

#### 配置降级策略

降级是一种容错机制，当后端服务出现异常（如超时、错误响应码等）时，系统会自动切换到预先配置的降级服务，以保证系统的可用性，避免完全中断。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**路由**。
5. 在路由列表中，单击路由名称，进入**路由详情**页面。
6. 在**路由详情**页面，单击**策略配置**页签。
7. 在**策略配置**页签，单击**降级**。
8. 在**降级**区域配置相关参数，然后单击**保存**。

**重要**

降级服务应具备简单、稳定、快速响应的特点。 建议在测试环境验证降级逻辑后再上线生产环境。 降级不应影响核心业务逻辑，仅用于保障可用性。

| 参数 | 描述 |
|---|---|
| 开启 | 路由降级策略的启用开关。 开启：网关路由降级策略生效。 关闭：网关路由降级策略失效。 |
| 需要降级的响应码 | 可选择4xx或5xx。 4xx：客户端错误（如 404、403）。 5xx：服务器错误（如 500、502）。 |
| 降级服务 | 选择备用的服务作为降级目标。 |

### 服务管理

#### 创建服务

您需要将已有的服务添加到网关中，登记为路由备选服务，以便网关获取服务地址。云原生网关支持以固定地址和DNS域名集群两种形式添加服务。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**服务**。
5. 在**服务列表**页面，单击**创建服务**。
6. 在**创建服务**页面，配置以下参数后，单击**提交**。

**说明**

云原生网关不会修改您的请求，当请求转发到后端域名服务时，并不会将Host重写为您配置的域名。

| 配置项 | 说明 |
|---|---|
| 名称 | 自定义服务名称。 |

| 来源类型 | 选择DNS域名或固定地址。 DNS域名：云原生网关支持将DNS解析的结果作为后端服务地址。 固定地址：如果该服务没有服务发现机制，需要手动添加服务的后端节点地址。 |
|---|---|
| 节点 | 当来源类型选择DNS域名，输入域名和端口。 域名：服务的域名配置。 端口：服务的域名访问端口。 当来源类型选择固定地址时，输入主机名/IP和端口主机名/IP：服务的后端节点地址，可以是主机名或者IP。 端口：服务的后端节点地址端口。 |
| 协议类型 | 服务使用协议类型，选择HTTP或者HTTPS。 |
| 开启健康检查 | 若开启健康检查系统会主动发送请求（如TCP链接/HTTP GET），探测服务节点是否存活，直接判断节点是否可用。 |
| 健康检查协议 | HTTP：健康检查通过发送请求模拟浏览器的访问行为来检查服务器应用是否健康。 TCP：健康检查通过发送SYN握手报文来检测服务器端口是否存活。 |
| 健康检查路径 | 用于健康检查页面文件的URI，建议对静态页面进行检查。 说明仅当健康检查协议选择HTTP时显示此参数。 |
| 健康检查域名（可选） | 只能使用字母、数字、“-”、“.”，默认无HOST字段。 说明仅当健康检查协议选择HTTP时显示此参数。 |
| 正常状态码 | 用于判断健康检查正常的HTTP状态码。 说明仅当健康检查协议选择HTTP时显示此参数。 |
| 健康检查响应超时时间 | 每次健康检查响应的最大超时时间，超时视为不健康。 |

| 健康检查间隔时间 | 相邻两次健康检查的时间间隔。 |
|---|---|
| 健康检查健康阈值 | 表示云服务器从失败到成功的连续健康检查成功次数。 |
| 健康检查不健康阈值 | 表示云服务器从成功到失败的连续健康检查失败次数。 |

#### 管理服务

在云原生网关中添加固定地址来源的服务的后端节点地址可能发生变更，网关无法动态获取该服务的后端节点地址。需要通过变更服务手动调整服务的后端节点地址，以便网关获取。本文介绍如何查看、编辑和删除服务。

**查看服务详情**

服务创建成功后，可以查看服务。如果服务较多，还可以通过筛选、搜索来提高查找效率。
1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**服务**。
5. （可选）在**服务列表**页面，可通过**服务名称**的关键字进行快速筛选。
6. 在服务列表中，单击服务名称，进入**服务详情**，可查看**服务详情**、**插件配置**以及**关联路由**信息。
在**服务详情**页签，可查看服务的详细信息，包括**基本信息**、**节点列表**以及**关联路由**等。 在**基本信息**区域，查看服务**名称**、**来源类型**以及**协议类型**。 在**节点列表**区域，查看主**机名****/IP**和**端口**。 单击**插件配置**页签，可管理当前服务绑定的插件；单击**添加插件**，可为服务绑定插件，具体操作请参考创建插件。

**说明**

在服务列表页面，单击**操作**列的**插件配置**，也可直接跳转到**插件配置**页签。 单击**关联路由**页签，查看当前服务关联的路由信息。

**编辑服务**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**服务**。
5. 在服务列表中，单击需要变更的服务**操作**列下的**编辑**。
6. 在**编辑服务**面板，修改服务相关参数，然后单击**提交**。

**说明**

您可以编辑由您自己创建的静态IP服务和DNS服务。其他类型的服务不允许编辑，例如 KUBERNETES服务。

**删除服务**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**服务**。
5. 删除服务。
单个删除：在服务列表中，单击目标服务**操作**列下的**删除**。 批量删除：在服务列表中，勾选目标服务，单击**批量删除**。
6. 在弹出的**提示**对话框中，单击**确定**。

### 消费者管理

#### 创建消费者

云原生网关通过消费者来为路由、API开启认证能力，本文介绍云原生网关控制台如何创建消费者。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**消费者**。
5. 在**消费者**页面，单击**创建消费者**。
6. 在**创建消费者**面板，配置以下参数后，单击**确定**。

| 配置项 | 描述 |
|---|---|
| 名称 | 自定义消费者的名称。实例内唯一。 |
| 说明 | 对消费者进行描述。 |
| 认证方式 | 当前消费者支持的认证方式，目前主要支持API KEY一种认证方式。 |
| Token | 自定义API Key凭证。 默认系统生成：系统为您自动生成API Key凭证。 自定义：自定义API Key凭证及凭证来源。 |

#### 查看消费者详情

本文介绍了如何查看消费者的详细信息。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**消费者**。
5. 在**消费者**页面，单击消费者名称，进入**消费者详情**页面，可查看消费者的**基础配置**和**消费者授权**信息。
在**基础配置**页签，可查看消费者的**基本信息**和**消费者认证**信息。
**基本信息**：可查看**消费者****ID**、**消费者名称**、**消费者说明**和**消费者状态**。
**消费者认证**：可查看**认证方式**、**Token**信息。
单击**消费者授权**页签，可对消费者进行授权管理，具体可参考授权管理。

#### 授权管理

本文介绍如何通过对API消费者进行授权管理，确保只有经过身份验证和权限校验的请求才能访问服务资源。

**授权消费者**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**消费者**。
5. 在**消费者**页面，可通过以下两种方式进入**消费者授权**页签。
方式一：单击目标消费者**操作**列的**授权**。 方式二：单击目标消费者名称，进入**消费者详情**页面，单击**消费者授权**页签。
6. 在**消费者授权**页签，单击**关联路由**，选择**路由**（可多选），然后单击**确定**。

**说明**

若没有可选路由，可参考路由管理创建路由。

**解除授权**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**消费者**。
5. 在**消费者**页面，可通过以下两种方式进入**消费者授权**页签。
方式一：单击目标消费者**操作**列的**授权**。 方式二：单击目标消费者名称，进入**消费者详情**页面，单击**消费者授权**页签。
6. 在路由列表中找到需要解除授权的目标路由，单击**操作**列中的**删除**，然后在弹出的**提示**对话框中单击确
定。

#### 修改消费者

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**消费者**。
5. 在**消费者**页面，单击目标消费者的**操作**列下的**编辑**。
6. 在**编辑消费者**面板中，修改相关参数，然后单击**确定**。

#### 删除消费者

本文介绍如何删除云原生网关消费者。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**消费者**。
5. 删除消费者。
单个删除：在**消费者**页面，单击目标消费者的**操作**列下的**删除**。 批量删除：在**消费者**页面，勾选目标消费者，单击**批量删除**。
6. 在弹出的**提示**对话框中，单击**确定**。

### 插件管理

#### 创建插件

插件配置可以把云原生网关中的各种插件配置到各种领域对象以及领域对象的组合上，比如可以把一条流量控制的插件分别配置到路由上或者服务上，从而使得云原生网关有着更加灵活的插件配置能力。

**背景信息**

在云原生网关中，存在着多种多样的插件。同时，在网关中也存在着以下三种领域对象。 路由服务域名在云原生网关中，对于同一个领域对象以及领域对象的组合，同种类型的插件配置可以在这个领域对象或者领域对象的组合上配置多次，举个例子：对于同一条路由，您可以配置多条限流规则。

**支持的插件类型**

认证 key-auth jwt-auth basic-auth oidc hmac-auth ext-auth opa 安全 cors ip-restriction waf request-block bot-detect 流量 cluster-key-rate-limit key-rate-limit traffic-tag requet-validation 转换 transformer frontend-gray custom-response cache-control

#### 可观测性

geo-ip log-request-response

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 进入创建插件入口。

**说明**

系统提供创建插件的四种入口，以及各自的适用场景，您可以按需选择任意一种创建入口。 主入口创建的插件作用范围为当前实例。 快捷入口创建的插件作用范围为当前服务、路由和域名。
**主入口**：若需要为当前实例创建插件，建议使用此入口。
a. 在左侧导航栏，选择**插件管理**，单击**创建插件**。 b. 在**创建插件**页面，选择对应的插件。
**快捷入口**1：如需为某个路由或包含该路由的领域对象组合创建插件，建议使用此入口。
a. 在左侧导航栏，选择**路由**。 b. 在**路由管理**页面，单击目标路由**操作**列的**插件配置**。 c. 在**插件配置**页签，单击**添加插件**进入**创建插件**页面，选择对应的插件进行创建。
**快捷入口**2：如需为某个服务或包含该服务的领域对象组合创建插件，建议使用该入口。
a. 在左侧导航栏，选择**服务**。 b. 在**服务管理**页面，单击目标服务**操作**列的**插件配置**。 c. 在**插件配置**页签，单击**添加插件**进入**创建插件**页面，选择对应的插件进行创建。
**快捷入口**3：如需为某个域名或包含该域名的领域对象组合创建插件，建议使用该入口。
a. 在左侧导航栏，选择**域名**。 b. 在**域名管理**页面，单击目标域名**操作**列的**插件配置**。 c. 在**插件配置**页签，单击**添加插件**进入**创建插件**页面，选择对应的插件进行创建。
5. 单击目标插卡卡片下方的**创建插件**，根据所选的插件配置相关信息后，单击**确定**。

**说明**

以下操作以创建cors插件为例，其他插件操作步骤类似。

| 参数 | 说明 |
|---|---|
| 作用范围 | 选择全局或局部。 全局：默认将此插件应用到整个实例上。 局部：需要填写此插件绑定的领域对象或者领域对象的组合，需要注意的是不同的插件类型下可选的领域对象不同。如果填写了领域对象的组合，那么这些领域对象之间的关系是与关系：比如这条局部插件同时绑定在路由和消费者上，那么只有携带该消费者 Token并且命中此条路由的请求才会执行该插件。 |
| 绑定类型 | 仅作用范围选择局部时显示。 选择路由、服务或域名。 |

| 绑定路由 | 仅绑定类型为路由时显示。 选择需要为插件绑定的路由，若没有可选择的路由，可参考路由管理创建路由。 |
|---|---|
| 绑定服务 | 仅绑定类型为服务时显示。 选择需要为插件绑定的服务，若没有可选择的服务，可参考创建服务自定义服务。 |
| 绑定域名 | 仅绑定类型为域名时显示。 选择需要为插件绑定的域名，若没有可选择的域名，可参考创建域名关联域名。 |
| cors | 配置cors插件。单击查看文档或参考跨域资源共享查看配置说明。 |

#### 管理插件

本文介绍了如何管理插件。

**查看插件详情**

在插件创建完成后，您可以查看插件的详细信息。
1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**插件管理**。
5. （可选）在**插件管理**页面，可根据**插件****ID**或**插件类型**快速筛选插件。
6. 在插件列表中，单击插件ID，进入**插件配置详情**页面，可查看插件配置的**基本信息**和**插件信息**。
**基本信息**：可查看插件**名称**、**插件类型**、**插件状态**、**作用范围**、**创建时间**以及**更新时间**。
**插件信息**：可查看详细插件信息。

**启用/禁用插件**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**插件管理**。
5. 在插件列表中，单击目标插件**操作**列的**启用**/**禁用**。
6. 在弹出的**提示**对话框中，单击**确定**。

**修改插件**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**插件管理**。
5. 在插件列表中，单击目标插件**操作**列的**编辑**。
6. 在**编辑插件**页面，修改配置信息后，单击**确定**。

**删除插件**

当不再需要插件时，可选择删除插件。
1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**插件管理**。
5. 在插件列表中，单击目标插件**操作**列的**删除**。
6. 在弹出的**提示**对话框中，单击**确定**。

#### 认证

##### Key认证

**功能说明**

`key-auth` 插件实现了基于API Key进行认证鉴权的功能，支持从HTTP请求的URL参数或者请求头解析 API Key，同时验证该API Key是否有权限访问。

**配置字段**

在一个规则里，鉴权配置和认证配置不可同时存在。 对于通过认证鉴权的请求，请求的header会被添加一个 `X-Mse-Consumer` 字段，用以标识调用者的名称。

**认证配置**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| global auth _ | bool | 选填（仅实例级别配置） | - | 只能在实例级别配置，若配置为 true，则全局生效认证机制；若配置为false，则只对做了配置的域名和路由生效认证机制； 若不配置，则仅当没有域名和路由配置时全局生效（兼容老用户使用习惯）。 |
| consumers | array of object | 必填 | - | 配置服务的调用者，用于对请求进行认证。 |

| keys | array of string | 必填 | - | API Key的来源字段名称，可以是 URL 参数或者 HTTP请求头名称。 |
|---|---|---|---|---|
| in query _ | bool | in query 和 _ in header 至少 _ 有一个为true。 | true | 配置true时，网关会尝试从URL 参数中解析API Key。 |
| in header _ | bool | in query 和 _ in header 至少 _ 有一个为true。 | true | 配置true时，网关会尝试从 HTTP请求头中解析API Key。 |

`consumers` 中每一项的配置字段说明如下：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| credential | string | 必填 | - | 配置该consumer 的访问凭证。 |
| name | string | 必填 | - | 配置该consumer 的名称。 |

**鉴权配置（非必需）**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| allow | array of string | 选填(非实例级别配置) | - | 只能在路由或域名等细粒度规则上配置，对于符合匹配条件的请求，配置允许访问的 consumer，从而实现细粒度的权限控制。 |

**配置示例**

**全局配置认证和路由粒度进行鉴权**

以下配置将对网关特定路由或域名开启Key Auth认证和鉴权。credential字段不能重复。 在实例级别做如下插件配置：

```
global_auth: false consumers:
- credential: 2bda943c-ba2b-11ec-ba07-00163e1250b5
 name: consumer1
- credential: c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
 name: consumer2
keys:
- apikey
- x-api-key
```

对route-a和route-b这两个路由做如下配置：

```
allow:
- consumer1
```

对*.example.com和test.com在这两个域名做如下配置:

```
allow:
- consumer2
```

**说明**

此例指定的route-a和route-b即在创建网关路由时填写的路由名称，当匹配到这两个路由时， 将允许name为consumer1的调用者访问，其他调用者不允许访问。 此例指定的*.example.com和test.com用于匹配请求的域名，当发现域名匹配时，将允许 name为consumer2的调用者访问，其他调用者不被允许访问。 根据该配置，下列请求可以允许访问：

**假设以下请求会匹配到route-a这条路由，将API Key设置在url参数中。**

```bash
curl http://xxx.hello.com/test?apikey=2bda943c-ba2b-11ec-ba07-00163e1250b5
```

**将API Key设置在http请求头中。**

```bash
curl http://xxx.hello.com/test -H 'x-api-key: 2bda943c-ba2b-11ec-ba07- 00163e1250b5'
```

认证鉴权通过后，请求的header中会被添加一个 `X-Mse-Consumer` 字段，在此例中其值为 `consumer1` ，用以标识调用方的名称。 下列请求将拒绝访问：

**请求未提供API Key，返回401。**

```bash
curl http://xxx.hello.com/test
```

**请求提供的API Key无权访问，返回401。**

```bash
curl http://xxx.hello.com/test?apikey=926d90ac-ba2e-11ec-ab68-00163e1250b5
```

**根据请求提供的API Key匹配到的调用者无访问权限，返回403。**

# consumer2不在`route-a`的`allow`列表里

```bash
curl http://xxx.hello.com/test?apikey=c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
```

**网关实例级别开启**

以下配置将对网关实例级别开启Basic Auth认证，所有请求均需要经过认证后才能访问。

```
global_auth: true consumers:
- credential: 2bda943c-ba2b-11ec-ba07-00163e1250b5
 name: consumer1
- credential: c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
 name: consumer2
keys:
- apikey
- x-api-key
```

##### JWT 认证

jwt-auth插件实现了基于JWT（JSON Web Tokens）进行认证鉴权的功能，支持从HTTP请求的URL参数、请求头、Cookie字段解析JWT，同时验证该Token是否有权限访问。相较于配置JWT认证鉴权，jwtauth插件额外提供了调用方身份识别的能力，支持对不同调用方配置不同的JWT凭证。本文介绍如何配置 jwt-auth插件。

**配置字段**

**认证配置**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| consumers | array of object | 必填。 | - | 配置服务的调用者，用于对请求进行认证。 |
| global auth _ | array of string | 选填（仅实例级别配置）。 | - | 只能在实例级别配置。 若配置为true，则全局生效认证机制。 若配置为false，则只对做了配置的域名和路由生效认证机制。 若不配置则仅当没有域名和路由配置时全局生效（兼容过往客户的使用习惯）。 |

子项 `consumers` 中的每一项配置字段说明如下。

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|

| name | string | 必填。 | - | 配置该consumer的名称。 |
|---|---|---|---|---|
| jwks | string | 选填。jwks和 remote jwks必填一 _ 个。 | - | JSON Web Key (JWK)指定的 JSON格式字符串，是由验证JWT 中签名的公钥（或对称密钥）组成的JSON Web Key Set。 |
| remote jwks _ | object | 选填。jwks和 remote jwks二选一。 _ | {"uri":" http://1 27.0.0. 1/keys", "servic e":"test. static"," port":"8 0","ttl": 30000," timeout ":3000} | 用于从指定服务的指定URI定时拉取JWKS，和JWKS字段同时配置时，以此字段配置拉取的JWKS 优先。 说明建议remote jwks返回的 _ jwks大小控制在1Mb以内。 |
| issuer | string | 选填。 | - | JWT的签发者，需要和payload 中的iss字段保持一致。 |
| claims | object | 选填。 | - | key/value分别对应payload中的key/value，可以用于校验多个字段是否和payload中一致， 例如配置aud: mobile-site，则要求payload中的aud必须是 mobile-site。 |
| claims to he _ _ aders | array of object | 选填。 | - | 抽取JWT的payload中指定字段，设置到指定的请求头中，然后转发给后端。 |
| from header _ s | array of object | 选填。 | [{"nam e":"Aut horizati on","val ue pref _ ix":"Be arer"}] | 从指定的请求头中抽取JWT。 |
| from params _ | array of string | 选填。 | access _ token | 从指定的URL参数中抽取JWT。 |
| from cookies _ | array of string | 选填。 | - | 从指定的cookie中抽取JWT。 |
| clock skew s _ _ econds | number | 选填。 | 60 | 校验JWT的exp和iat字段时允许的时钟偏移量，单位为秒。 |

| keep token _ | bool | 选填。 | true | 转发给后端时是否保留JWT。 |
|---|---|---|---|---|

**说明**

只有当 `from_headers` ， `from_params` ， `from_cookies` 均未配置时，才会使用默认值。 `from_headers` 中每一项的配置字段说明如下：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| name | string | 必填。 | - | 抽取JWT的请求Header。 |
| value prefix _ | string | 必填。 | - | 对请求Header的value去除此前缀，剩余部分作为JWT。 |

`claims_to_headers` 中每一项的配置字段说明如下：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| claim | string | 必填。 | - | JWT payload中的指定字段，要求必须是字符串或无符号整数类型。 |
| header | string | 必填。 | - | 从payload取出字段的值设置到这个请求头中，转发给后端。 |
| override | bool | 选填。 | true | true时，存在同名请求头会进行覆盖。 false时，追加同名请求头。 |

`remote_jwks` 中每一项的配置字段说明如下：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| uri | string | 必填。 | - | 请求URL。 |

| service | string | 必填。 | - | K8s服务填写示例： foo.default.svc.cluster.loc al。 Nacos服务填写示例： foo.DEFAULT- GROUP.public.nacos。 如果是名为test的DNS服务， 则填写test.dns。 如果是名为test的静态IP服务，则填写test.static。 |
|---|---|---|---|---|
| port | bool | 必填。 | - | 服务端口。 |
| timeout | bool | 选填。 | 3000 | 服务请求超时时间，单位是毫秒。 |
| ttl | bool | 选填。 | 30000 | 缓存时间，单位是毫秒。 |

**鉴权配置（非必需）**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| allow | array of string | 选填（非实例级别配置）。 | - | 只能在路由或域名等细粒度规则上进行配置，对于符合匹配条件的请求， 配置允许访问的 consumer，从而实现细粒度的权限控制。 |

**重要**

在一个规则里，鉴权配置和认证配置不可同时存在。 对于通过认证鉴权的请求，请求的Header会被添加一个 `X-Mse-Consumer` 字段，用以标识调用者的名称。

**配置示例**

**全局配置认证和路由粒度进行鉴权**

以下配置将对网关特定路由或域名开启JWT Auth认证和鉴权。

**说明**

如果一个JWT能匹配多个jwks，则按照配置顺序命中第一个匹配的consumer。

**插件配置**

在实例级别做如下插件配置：

```json
consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k":
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqX pNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD- MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct-- 7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
```

]

```json
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n":
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha LMt2iyiSb9LZJAeJmHf7ecguXS_- 4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz- N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT POGZh_25KXGdF_ZC_MSRw"
        }
```

]

```
    }
```

**路由和域名配置**

在 `route-a` 和 `route-b` 两个路由做如下插件配置：

```
allow:
- consumer1
```

在 `*.example.com` 和 `test.com` 两个域名做如下插件配置：

```
allow:
- consumer2
```

**说明**

此例指定的 `route-a` 和 `route-b` 即在创建网关路由时填写的路由名称，当匹配到这两个路由时，将允许 `name` 为 `consumer1` 的调用者访问，其他调用者不被允许访问。 此例指定的 `*.example.com` 和 `test.com` 用于匹配请求的域名，当发现域名匹配时，将允许 `name` 为 `consumer2` 的调用者访问，其他调用者不被允许访问。

**请求示例**

根据该配置，允许访问以下请求。假设以下请求会匹配到route-a这条路由。 将JWT设置在URL参数中。

```bash
curl 'http://xxx.hello.com/test? access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEy****.eyJp************.-v BSV0bKeDwQcuS6eeSZN9dLTUnSnZVk8eVCXdooCQ4'
```

将JWT设置在HTTP请求头中。

```bash
curl http://xxx.hello.com/test -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEyMyJ9.eyJpc3MiOiJhYmNkIiwic3ViIjoidGVzdC ImlhdCI6MTY2NTY2MDUyNywiZXhwIjoxODY1NjczODE5fQ.vBSV0bKeDwQcuS6eeSZN9dLTUnSnZVk8eVCXdooCQ4'
```

**结果验证**

认证通过后，请求Header会添加 `X-Mse-Consumer` 字段，在此例中其值为 `consumer1` ，用于标识调用方名称。 下列请求将拒绝访问： 请求未提供JWT，返回401。 根据请求提供的JWT匹配到的调用者无访问权限，返回403。

**网关实例级别开启，但特定路由关闭**

在实例级别做如下插件配置：

```json
global_auth: true consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k":
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqX pNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD- MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct-- 7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
```

]

```json
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n":
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha LMt2iyiSb9LZJAeJmHf7ecguXS_- 4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz- N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT POGZh_25KXGdF_ZC_MSRw"
        }
```

]

```
    }
```

在 `route-b` 路由做如下插件配置：

```
_disable_: true
```

此例 `route-b` 即在创建网关路由时填写的路由名称。因为 `_disable_` 设置为 `true` ，当匹配到这个

|  | global auth _ |  |
|---|---|---|
| consumer1 |  |  |

**域名级别开启，但特定路由关闭**

在实例级别做如下插件配置：

```json
consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k":
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqX pNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD- MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct-- 7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
```

]

```json
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n":
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha LMt2iyiSb9LZJAeJmHf7ecguXS_- 4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz- N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT POGZh_25KXGdF_ZC_MSRw"
        }
```

]

```
    }
```

在 `route-b` 路由做如下插件配置：

```
_disable_: true
```

在 `*.example.com` 域名做如下插件配置：

```
allow:
- consumer1
- consumer2
```

此例中 `route-b` 即在创建网关路由时填写的路由名称。因为 `_disable_` 设置为 `true` ，当匹配到这此例中指定的 `*.example.com` 用于匹配请求的域名。当发现域名匹配时，将允许 `name` 为 `consumer1` 或 `consumer2` 的调用者访问，其他调用者不允许访问。 配置规则顺序会依次执行匹配，有任一规则匹配到，就会执行对应配置，不再匹配其他规则。因为这里配置路由匹配优先级高于域名，即对当前配置的域名生效，而对域名下的特定路由关闭。

**相关错误码**

| HTTP状态码 | 出错信息 | 原因说明 |
|---|---|---|
| 401 | Jwt missing | 请求头未提供JWT。 |
| 401 | Jwt expired | JWT已经过期。 |
| 401 | Jwt verification fails | JWT payload校验失败，如iss不匹配。 |
| 403 | Access Denied | 无权限访问当前路由。 |

##### Basic 认证

basic-auth插件实现了基于HTTP Basic Auth标准进行认证鉴权的功能。本文介绍如何配置basic-auth插件。

**插件类型**

认证鉴权。

**配置字段**

**认证配置**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| consumers | array of object | 必填。 | - | 配置服务的调用者，用于对请求进行认证。 |
| global auth _ | array of string | 选填（**仅实例级别配置**）。 | - | 只能在实例级别配置。 若配置为true，则全局生效认证机制。 若配置为false，则只对做了配置的域名和路由生效认证机制。 若不配置则仅当没有域名和路由配置时全局生效（兼容过往客户的使用习惯）。 |

子项 `consumers` 中每一项的配置字段说明如下：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| credential | string | 必填。 | - | 配置该consumer的访问凭证。 |
| name | string | 必填。 | - | 配置该consumer的名称。 |

**鉴权配置（非必需）**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| allow | array of string | 选填（**非实例级别配置**）。 | - | 只能在路由或域名等细粒度规则上配置，对于符合匹配条件的请求，配置允许访问的 consumer，从而实现细粒度的权限控制。 |

**重要**

在一个规则里，鉴权配置和认证配置不可同时存在。 对于通过认证鉴权的请求，请求的Header会被添加一个 `X-Mse-Consumer` 字段，用以标识调用者的名称。

**配置示例**

**全局配置认证和路由粒度进行鉴权**

以下配置将对网关特定路由或域名开启Basic Auth认证和鉴权。

**说明**

凭证信息中的用户名和密码之间使用“:”分隔。 `credential` 字段不能重复。 在实例级别做如下插件配置：

```
global_auth: false consumers:
- credential: 'admin:123456'
  name: consumer1
- credential: 'guest:abc'
  name: consumer2
```

在 `route-a` 和 `route-b` 两个路由做如下插件配置：

```
allow:
- consumer1
```

在 `*.example.com` 和 `test.com` 两个域名做如下插件配置：

```
allow:
- consumer2
```

**说明**

此例指定的 `route-a` 和 `route-b` 即在创建网关路由时填写的路由名称，当匹配到这两个路由时，将允许 `name` 为 `consumer1` 的调用者访问，其他调用者不允许访问。 此例指定的 `*.example.com` 和 `test.com` 用于匹配请求的域名，当发现域名匹配时，将允许 `name` 为 `consumer2` 的调用者访问，其他调用者不被允许访问。 根据该配置，下列请求可以允许访问： 请求指定用户名密码。
# 假设以下请求将会匹配到`route-a`路由
# 使用 `curl` 的 `-u` 参数指定

```bash
curl -u admin:123456 http://xxx.hello.com/test
```

# 或者直接指定 `Authorization` 请求头，用户名密码使用 `base64` 编码

```bash
curl -H 'Authorization: Basic YWRtaW46MTIzNDU2' http://xxx.hello.com/test
```

**说明**

认证鉴权通过后，请求的Header中会被添加一个 `X-Mse-Consumer` 字段，在此例中其值为 `consumer1` ，用以标识调用方的名称。 下列请求将拒绝访问： 请求未提供用户名密码，返回401。

```bash
curl http://xxx.hello.com/test
```

请求提供的用户名密码错误，返回401。

```bash
curl -u admin:abc http://xxx.hello.com/test
```

根据请求的用户名和密码匹配到的调用者无访问权限，返回403。
# consumer2不在`route-a`的`allow`列表里

```bash
curl -u guest:abc http://xxx.hello.com/test
```

**网关实例级别开启**

以下配置将对网关实例级别开启 Basic Auth 认证，所有请求均需要经过认证后才能访问。

```
global_auth: true consumers:
- credential: 'admin:123456'
  name: consumer1
- credential: 'guest:abc'
  name: consumer2
```

**相关错误码**

| HTTP状态码 | 出错信息 | 原因说明 |
|---|---|---|
| 401 | Request denied by Basic Auth check. No Basic Authentication information found. | 请求未提供凭证。 |
| 401 | Request denied by Basic Auth check. Invalid username and/or password. | 请求凭证无效。 |
| 403 | Request denied by Basic Auth check. Unauthorized consumer. | 请求的调用方无访问权限。 |

##### OIDC 认证

oidc插件支持OpenID Connect（OIDC）身份认证。同时，该插件强化了对跨站请求伪造（CSRF）攻击的防御能力，并支持OpenID Connect协议中的注销端点（Logout Endpoint）以及刷新令牌（Refresh Token）机制。在经过Wasm插件进行OIDC验证后的请求将携带 `Authorization` 头部，包含相应的访问令牌（Access Token）。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `350` 。

**配置字段**

| 名称 | 数据类型 | 描述 | 默认值 |
|---|---|---|---|
| cookie name _ | string | the name of the cookie that the oauth proxy _ creates. Should be changed to use a cookie prefix( Host- or __ Secure- ) if -- __ cookie-secure is set. | " oauth2 proxy" _ _ |
| cookie secret _ | string | the seed string for secure cookies (optionally base64 encoded) | - |

|  |  |  | Host- __ |  |  |
|---|---|---|---|---|---|
|  |  | Secure- __ |  |  |  |
|  |  |  |  | ) if |  |
|  | cookie-secure |  |  |  |  |

| cookie domains _ | string\|list | Optional cookie domains to force cookies to (e.g. .yourcompany.c om ). The longest domain matching the request’s host will be used (or the shortest cookie domain if there is no match). | - |
|---|---|---|---|
| cookie path _ | string | an optional cookie path to force cookies to (e.g. /poc/ ) | "/" |
| cookie expire _ | duration | expire timeframe for cookie. If set to 0, cookie becomes a session-cookie which will expire when the browser is closed. | 168h0m0s |
| cookie refresh _ | duration | refresh the cookie after this duration; 0 to disable | - |
| cookie secure _ | bool | set secure (HTTPS only) cookie flag | true |
| cookie httponly _ | bool | set HttpOnly cookie flag | true |
| cookie samesite _ | string | set SameSite cookie attribute ( "lax" , "strict" , "none" , or "" ). | "" |
| cookie csrf per reque _ _ _ st | bool | Enable having different CSRF cookies per request, making it possible to have parallel requests. | false |
| cookie csrf expire _ _ | duration | expire timeframe for CSRF cookie. | 15m |
| client id _ | string | the OAuth Client ID. | - |

| .yourcompany.c |  |
|---|---|

| t | om |
|---|---|

|  |  | "lax" |  |
|---|---|---|---|

|  | client secret _ |  |  | string |  |  | the OAuth Client Secret. |  | - |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | provider |  |  | string |  |  | OAuth provider. |  | oidc |  |
|  | pass authorization he _ _ ader |  |  | bool |  |  | pass OIDC IDToken to upstream via Authorization Bearer header. |  | true |  |
|  | oidc issuer url _ _ |  |  | string |  |  | the OpenID Connect issuer URL, e.g. "https://dev- |  |  |  |
|  |  |  |  |  |  |  |  | "https://dev- | - |  |
|  |  |  |  |  |  |  | o43xb1mz7ya7ach4.us. |  |  |  |
|  |  |  |  |  |  |  | auth0.com" |  |  |  |
|  | oidc verifier request t _ _ _ imeout |  |  | uint32 |  |  | OIDC verifier discovery request timeout. |  | 2000(ms) |  |
|  | scope |  |  | string |  |  | OAuth scope specification. |  | - |  |
|  |  |  |  |  |  |  | the OAuth Redirect URL, e.g. "https://inter |  |  |  |
|  |  |  |  |  |  |  |  | "https://inter |  |  |
|  |  |  |  |  |  |  | nalapp.yourcompany.c |  |  |  |
|  |  |  |  |  |  |  | om/oauth2/callback" |  |  |  |
|  | redirect url _ |  |  |  |  |  |  |  |  |  |
|  |  |  |  | string |  |  |  |  |  |  |
|  | service name _ |  |  | string |  |  | registered name of the OIDC service, e.g. auth.dns , ke ycloak.static |  | - |  |
|  | service port _ |  |  | int64 |  |  | service port of the OIDC service. |  | - |  |
|  | service host _ |  |  | string |  |  | host of the OIDC service when type is static ip. |  | - |  |

|  |  | auth.dns |
|---|---|---|
|  | ycloak.static |  |

| ke | - |
|---|---|

| match type _ | string | match type ( whitelist or bl acklist ). | "whitelist" |
|---|---|---|---|
| match list _ | rule\|list | a list of (match rule domain, _ _ match rule path, and _ _ match rule type). _ _ | - |
| match rule domain _ _ | string | match rule domain, support wildcard pattern such as *.bar.com . | - |
| match rule path _ _ | string | match rule path such as /headers . | - |
| match rule type _ _ | string | match rule type can be exact or pref ix or regex . | - |

|  |  | whitelist |
|---|---|---|
|  | acklist |  |

| bl |  | "whi | telist" |
|---|---|---|---|

|  |  | exact |  |
|---|---|---|---|
|  | ix |  |  |

| pref |  |
|---|---|

**使用方式**

**生成 Cookie 密钥**

```python
python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'
```

参考：Oauth2-proxy Generating a Cookie Secret。

**黑白名单模式**

支持黑白名单模式配置，默认为白名单模式，白名单为空，即所有请求都需要经过验证，匹配域名支持泛域名例如 `*.bar.com` ，匹配规则支持精确匹配 `exact` ，前缀匹配 `prefix` ，正则匹配 `regex` 。

**白名单模式**

```
match_type: 'whitelist' match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/foo'
 match_rule_type: 'prefix'
```

泛域名 `*.bar.com` 下前缀匹配 `/foo` 的请求无需验证。

**黑名单模式**

```
match_type: 'blacklist' match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/headers'
 match_rule_type: 'prefix'
```

只有泛域名 `*.bar.com` 下前缀匹配 `/header` 的请求需要验证。

**注销用户**

注销用户需重定向到 `/oauth2/sign_out` 这个端点。这个端点仅移除oauth2-proxy自己设置的cookie， 也就是说，用户仍然在OIDC Provider处保持登录状态，并且在再次访问应用时可能会自动重新登录。因此还需要使用 `rd` 查询参数将用户重定向到认证提供商的注销页面，即重定向用户到类似如下地址（注意 URL编码）：

```
/oauth2/sign_out?rd=https%3A%2F%2Fmy-oidcprovider.example.com%2Fsign_out_page
```

或者，可以在 `X-Auth-Request-Redirect` 头部中包含重定向URL：

```
GET /oauth2/sign_out HTTP/1.1 X-Auth-Request-Redirect: https://my-oidc-provider.example.com/sign_out_page ...
```

重定向URL中可以包含 `post_logout_redirect_uri` 参数指定OIDC Provider登出后跳转到的页面，例如后端服务的登出页面，不携带该参数则默认跳转到OIDC Provider的登出页面，详情见下方auth0和 keycloak的示例。

**说明**

如果OIDC Provider支持会话管理和发现，那么“sign_out_page”应该是从metadata中获取

```
的 end_session_endpoint
```

**OIDC 服务 HTTPS 协议**

如果 OIDC Provider 为 HTTPS 协议，参考Higress中配置后端服务协议：HTTPS的说明，需要通过使用注解 `higress.io/backend-protocol: "HTTPS"` 配置请求转发至后端服务使用HTTPS协议，参考Auth0 示例中Ingress配置。

**配置示例**

**Auth0 配置示例**

**配置步骤**

**Step 1: 配置Auth0账户**

登录到开发人员Okta网站Developer Auth0 site。 注册测试web应用程序。

**重要**

需填写Allowed Callback URLs、Allowed Logout URLs、Allowed Web Origins等配置项，否则 OIDC Provider会认为用户跳转的重定向 URL 或登出URL无效。

**Step 2: 云原生网关配置服务来源**

在云原生网关服务来源中创建auth0 DNS来源。

**Step 3: OIDC服务HTTPS配置**

```
apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 name: auth0-ingress
 annotations:
 higress.io/destination: auth.dns
 higress.io/backend-protocol: "HTTPS"
 higress.io/ignore-path-case: "false"
spec:
 ingressClassName: higress
 rules:
 - host: foo.bar.com
 http:
 paths:
 - path: /
 pathType: Prefix
 backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
```

**Step 4: Wasm插件配置**

```
redirect_url: 'http://foo.bar.com/oauth2/callback' oidc_issuer_url: 'https://dev-o43xb1mz7ya7ach4.us.auth0.com/' client_id: 'XXXXXXXXXXXXXXXX' client_secret: 'XXXXXXXXXXXXXXXX' scope: 'openid email offline_access' cookie_secret: 'nqav************_8DCfY=' service_name: 'auth.dns' service_port: 443 match_type: 'whitelist' match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/foo'
 match_rule_type: 'prefix'
```

**重要**

必须先配置服务来源，wasm插件在初始化时需要访问配置的服务获取openid-configuration。

**结果测试**

**访问服务页面，未登录的话进行跳转**

**登录成功跳转到服务页面**

headers中可以看到携带了_oauth2_proxy 的cookie用于下次登录访问，Authorization对应IDToken用于后端服务获得用户信息。

**访问登出跳转到登出页面**

```
http://foo.bar.com/oauth2/sign_out?rd=https%3A%2F%2Fdevo43xb1mz7ya7ach4.us.auth0.com%2Foidc%2Flogout
```

**访问登出跳转到登出页面（携带post_logout_redirect_uri参数跳转指定**

**uri）**

```
http://foo.bar.com/oauth2/sign_out?rd=https%3A%2F%2Fdevo43xb1mz7ya7ach4.us.auth0.com%2Foidc%2Flogout%3Fpost_logout_redirect_uri%3Dhttp% A%2F%2Ffoo.bar.com%2Ffoo
```

**重要**

post_logout_redirect_uri跳转的URI需要在OIDC Provider Allowed URLs处配置才可以正常跳转。

**keycloak配置示例**

**配置步骤**

**Step 1: Get started with keycloak on docker**

https://www.keycloak.org/getting-started/getting-started-docker

**重要**

需填写Valid redirect URIs、Valid post logout URIs、Web origins配置项，否则OIDC Provider 会认为用户跳转的重定向URL或登出URL 无效。

**Step 2: 云原生网关配置服务来源**

在云原生网关服务来源中创建Keycloak固定地址服务。

**Step 3: Wasm插件配置**

```
redirect_url: 'http://foo.bar.com/oauth2/callback' oidc_issuer_url: 'http://127.0.0.1:9090/realms/myrealm' client_id: 'XXXXXXXXXXXXXXXX' client_secret: 'XXXXXXXXXXXXXXXX' scope: 'openid email' cookie_secret: 'nqavJrGvRmQxWwGNptLdyUVKcBNZ2b18Guc1n_8DCfY=' service_name: 'keycloak.static' service_port: 80 service_host: '127.0.0.1:9090' match_type: 'blacklist' match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/headers'
 match_rule_type: 'prefix'
```

**结果测试**

**访问服务页面，未登录的话进行跳转**

**登录成功跳转到服务页面**

**访问登出跳转到登出页面**

```
http://foo.bar.com/oauth2/sign_out? rd=http%3A%2F%2F127.0.0.1:9090%2Frealms%2Fmyrealm%2Fprotocol%2Fopenidconnect%2Flogout
```

**访问登出跳转到登出页面（携带post_logout_redirect_uri参数跳转指定**

**URI）**

```
http://foo.bar.com/oauth2/sign_out? rd=http%3A%2F%2F127.0.0.1:9090%2Frealms%2Fmyrealm%2Fprotocol%2Fopenidconnect%2Flogout%3Fpost_logout_redirect_uri%3Dhttp%3A%2F%2Ffoo.bar.com%2Ffoo
```

**OIDC流程**

Upstream 网关 OIDC Provider User 用户当前状态未登录
1. HTTP 请求
2. 生成csrf cookie
存储state值
3. 跳转到登录页
4. 录
5. 携带授权跳转到网关
6. 校验state值
防护csrf攻击
7. 利用授权交换Token
8. 将Tokens存储
到oidc cookie中
9. 在浏览器
设置cookie
10. 校验oidc
11. HTTP请求携带AccessToken
cookie
12. HTTP响应
用户状态已登录，后续请求无需再次登录
1. HTTP 请求
2. 校验oidc
3. HTTP 请求携带Access Token
cookie
4. HTTP响应
用户状态已登录，需要进行令牌刷新
1. HTTP 请求
2. 验证Token
过期时间
3. 用Refresh Token刷新ID
Token和Access Token
4. HTTP请求携带AccessToken
5. HTTP响应
网关 Upstream OIDC Provider User

**OIDC流程解析**

**用户未登录**

1. 模拟用户访问对应服务API。

```bash
curl --url "foo.bar.com/headers"
```

2. 云原生网关重定向到OIDC Provider登录页，同时携带client_id、response_type、scope等OIDC认证
的参数，并设置csrf cookie防御CSRF攻击。

```bash
curl --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/authorize"\
 --url-query "approval_prompt=force" \
 --url-query "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
 --url-query "redirect_uri=http%3A%2F%2Ffoo.bar.com%2Foauth2%2Fcallback" \
 --url-query "response_type=code" \
 --url-query "scope=openid+email+offline_access" \
 --url-query "state=nT06************_hCjskrH_VupPqdcdw%3A%2Ffoo" \
 --header "Set-Cookie:
_oauth2_proxy_csrf=LPruATEDgcdmelr8zScD_ObhsbP4zSzvcgmPlcNDcJpFJ0OvhxP2hFotsUkZnYxd5KsIjzeIXGTOjf8TKcbTHbDItaQoZORXI_0id3qeY0Jt78223DPeJ1xBqa8VO0UiEOUFOR53FGxirJOdKFxaAvxDFb1Ok=|17189624 5|V1QGWyjQ4hMNOQ4Jtf17HeQJdVqHdt5d65uraFduMIU=; Path=/; Expires=Fri, 21 Jun 2024 08:06:20 GMT; HttpOnly"
```

3. 重定向到登录页。
4. 用户输入用户名密码登录完成。
5. 携带授权重定向到云原生网关并携带了state参数用于验证csrf cookie ，授权码用于交换token。

```bash
curl --url "http://foo.bar.com/oauth2/callback" \
 --url-query "state=nT06xdCqn4IqemzBRV5hmO73U_hCjskrH_VupPqdcdw%3A%2Ffoo" \
 --url-query "code=0bdopoS2c2lx95u7iO0OH9kY1TvaEdJHo4lB6CT2_qVFm"
```

6. 校验csrf cookie中加密存储的state值与url参数中的state值必须相同。
7. 利用授权交换id_token 和access_token。

```bash
curl -X POST \
 --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/oauth/token" \
 --data "grant_type=authorization_code" \
 --data "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
 --data
"client_secret=ekqv5XoZuMFtYms1NszEqRx03qct6BPvGeJUeptNG4y09PrY16BKT9IWezTrrhJ " \
 --data "redirect_uri=http%3A%2F%2Ffoo.bar.com%2Foauth2%2Fcallback" \
 --data "code=0bdopoS2c2lx95u7iO0OH9kY1TvaEdJHo4lB6CT2_qVFm" \
```

返回的请求里包含了id_token, access_token，refresh_token用于后续刷新token。

```json
{
 "access_token": "eyJh************..WP_WRVM-
y3fM1sN4.fAQqtKoKZNG9Wj0OhtrMgtsjTJ2J72M2klDRd9SvUKGbiYsZNPmIl_qJUf81D3VIjD59o xrOOJIzXTgsfFVA2x15gjBlNh68N7dyhXu9237Tbplweu1jA25IZDSnjitQ3pbf7xJVIfPnWcrzl6uT8G1EPomFcl6AQprV2FoKFMCGFCgeafuttppKe1a8mpJDj7AFLPs- 344tT9mvCWmI4DuoLFh0PiqMMJBByoijRSxcSdXLPxZng84j8JVF7H6mFa-dj-icP- KLy6yvzEaRKz_uwBzQCzgYK434LIpqw_PRuN3ClEsenwRgIsNdVjvKcoAysfoZhmRy9BQaE0I7qToh BFNX6A.mgGGeeWgugfXcUcsX4T5dQ",
 "refresh_token": "GrZ1f2JvzjAZQzSXmyr1ScWbv8aMFBvzAXHBUSiILcDEG",
 "id_token":
"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imc1Z1ExSF9ZbTY0WUlvVkQwSVpXTCJ9 yJlbWFpbCI6IjE2MDExNTYyNjhAcXEuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJpc3MiOiJ dHRwczovL2Rldi1vNDN4YjFtejd5YTdhY2g0LnVzLmF1dGgwLmNvbS8iLCJhdWQiOiJZYWdGcVJEOX mTklhYWM1QmFtamhzU2F0anJBbnNuWiIsImlhdCI6MTcxOTE5ODYzOCwiZXhwIjoxNzE5MjM0NjM4L JzdWIiOiJhdXRoMHw2NjVkNzFlNzRjMTMxMTc3YmU2NmU2MDciLCJzaWQiOiJjdDJVOF9ZUS16VDdF GkwRTNNeUstejc5ZGlWUWhhVSJ9.gfzXKJ0FeqzYqOUDLQHWcUG19IOLqkpLN09xTmIat0umrlGV5V SumgWH3XJmmwnhdb8AThH3Jf-7kbRJzu4rM- BbGbFTRBTzNHeUajFOFrIgld5VENQ_M_sXHkTp0psWKSr9vF24kmilCfSbvC5lBKjt878ljZ7-x teWuaUYOMUdcJb4DSv0-zjX01sonJxYamTlhji3M4TAW7VwhwqyZt8dBhVSNaRw1wUKj- M1JrBDLyx65sroZtSqVA0udIrqMHEbWYb2de7JjzlqG003HRMzwOm7OXgEd5ZVFqgmBLosgixOU5DJ A26nlqK92Sp6VqDMRvA-3ym8W_m-wJ_A",
 "scope": "openid email offline_access",
 "expires_in": 86400,
 "token_type": "Bearer"
}
```

8. 将获得的id_token, access_token, refresh_token加密存储在cookie _oauth2_proxy中。
9. 重定向到用户访问的后端服务并设置cookie，用于后续用户登录状态的验证，同时清除 cookie
_oauth2_proxy_csrf。

```
"Set-Cookie": [
 "_oauth2_proxy_csrf=; Path=/; Expires=Mon, 24 Jun 2024 02:17:39 GMT;
HttpOnly",
 "_oauth2_proxy=8zM_Pcfpp_gesKFe4SMg08o5Iv0A8WAOQOmG1-vZBbQ56UggYVC0Cu-
gFMEoxJZU5q1O5vqRlVBizlLetgVjRCksGVbttwl8tQ7h5YiyIubbbtvF1T4JzLh3QfzUUrwbB- VznOkh8qLbjAhddocecjBt4rMiDyceKXqMr4eO5TUEMx4vHtJYnTYalMeTYhGXk5MNSyrdZX9NnQnk rCjiOQM13ggwob2nYwhGWaAlgzFSWkgkdtBy2Cl_YMWZ8_gKk9rDX289- JrJyGpr5k9O9RzRhZoY2iE3Mcr8-Q37RTji1Ga22QO- XkAcSaGqY1Qo7jLdmgZTYKC5JvtdLc4rj3vcbveYxU7R3Pt2vEribQjKTh4Sqb0aA03p4cxXyZN4SU BW1NAOm4JLPUhKJy8frqC9_E0nVqPvpvnacaoQs8WkX2zp75xHoMa3SD6KZhQ5JUiPEiNkOaUsyafL ht6lLkNDhgzW3BP2czoe0DCDBLnsot0jH-qQpMZYkaGr- ZnRKI1OPl1vHls3mao5juOAW1VB2A9aughgc8SJ55IFZpMfFMdHdTDdMqPODkItX2PK44GXpHeLxkOqrzp3GHtMInpL5QIQlTuux3erm3CGntlUE7JBtN2T9LEb8XfIFu58X9_vzMun4JQlje2Thi9_taI_z1DSaTtvNNb54wJfSPwYCCl4OsH- BacVmPQhH6TTZ6gP2Qsm5TR2o1U2D9fuVkSM- OPCG9l3tILambIQwC3vofMW6X8SIFSmhJUDvN7NbwxowBiZ6Y7GJRZlAk_GKDkpsdrdIvC67QqczZF hRVnm6qigPO41APCbcO6fgTwyOhbP3RrZZKWSIqWJYhNE3_Sfkf0565H7sC7Hc8XUUjJvP3WnjKS9x7KwzWadsUjV3-Q-VNl-rXTguVNAIirYKqrMNMZGCRcJqcLnUF0V_J2lVmFyVsSlE3t0sDw2xmbkOwDptXFOjQL5Rb4esUMYdCBWFajBfvUtcZE tYhD0kb6VcbjXO3NCVW5qKh_l9C9SRCc7TG1vcRAqUQlRXHacTGWfcWsuQkCJ3Mp_oWaDxs1GRDykQ xAn5sTICovThWEU2C6o75grWaNrkj5NU- 0eHh3ryvxLmGLBOXZV9OQhtKShWmUgywSWMxOHOuZAqdAPULc8KheuGFjXYp- RnCbFYWePJmwzfQw89kSkj1KUZgMYwKEjSz62z2qc9KLczomv76ortQzvo4Hv9kaW6xVuQj5R5Oq6_ MBOqsmUMzcXpxCIOGjcdcZRBc0Fm09Uy9oV1PRqvAE4PGtfyrCaoqILBix8UIww63B07YGwzQ-h AXDysBK- Vca2x7GmGdXsNXXcTgu00bdsjtHZPDBBWGfL3g_rMAXr2vWyvK4CwNjcaPAmrlF3geHPwbIePT0hsk boX1v1bsuhzsai7rGM4r53pnb1ZEoTQDa1B- HyokFgo14XiwME0zE1ifpNzefjpkz1YY2krJlqfCydNwoKaTit4tD2yHlnxAeFF9iIrxzSKErNUFpm La7ge7V33vhEH-6k5oBTLE2Q2BrC6aAkLCcPwU9xv_SzBDQPRY0MEYv3kGF03Swo1crRbGhaifYX9NiHDsmG6r1vAnx0MAOw2Jzuz2x6SSdfBrzlcoWBlrwiZzd9kAKq75n1Uy9uzZ8SRnkBrEZyS BwEbu196VklkRE0jqwC-e3wWNNuviSOfwkVeX- 7QdOoO10yw9VK2sW52lFvIEf4chv_ta7bGfAZOWBjpktG6ZLD81SE6A88zpqG2SysSyNMp9hl-u mG-5sFsjCn_c9E8bDvwkUOUVb9bNqhBDsZgR0BNPawiOZjmyfhzmwmWfzgFzfFSV6BvOwNRi3sCOHTsWcuk9NBQ_YK8CpNkVl3WeIBSDfidimuC_QV9UWKs1GPk35ZRkM4zKtL 2JsBFWKaDy_P80TcOzcMBoP8gIBClXZ-WUqfE8s1yyc4jrqqL1_wJ24ef1O9FktsbyZiDKXw2vnqsT8-g_hCeG-unrT1ZFscf8oNdqczARHX- K4vKH2k3uIqEx1M=|1719199056|2rsgdUIClHNEpxBLlHOVRYup6e4oKensQfljtmn4B80=; P ath=/; Expires=Mon, 01 Jul 2024 03:17:36 GMT; HttpOnly"
```

]
0. 校验是否存在cookie存储了用户的token信息，同时查看是否过期。
1. 使用含有Authorization头部存储用户的access_token访问相应的API。

```bash
curl --url "foo.bar.com/headers"
 --header "Authorization: Bearer
eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtbzQzeGIxbXo3eW 3YWNoNC51cy5hdXRoMC5jb20vIn0..WP_WRVMy3fM1sN4.fAQqtKoKZNG9Wj0OhtrMgtsjTJ2J72M2klDRd9SvUKGbiYsZNPmIl_qJUf81D3VIjD59o xrOOJIzXTgsfFVA2x15gjBlNh68N7dyhXu9237Tbplweu1jA25IZDSnjitQ3pbf7xJVIfPnWcrzl6uT8G1EPomFcl6AQprV2FoKFMCGFCgeafuttppKe1a8mpJDj7AFLPs- 344tT9mvCWmI4DuoLFh0PiqMMJBByoijRSxcSdXLPxZng84j8JVF7H6mFa-dj-icP- KLy6yvzEaRKz_uwBzQCzgYK434LIpqw_PRuN3ClEsenwRgIsNdVjvKcoAysfoZhmRy9BQaE0I7qToh BFNX6A.mgGGeeWgugfXcUcsX4T5dQ"
```

2. 后端服务根据access_token获取用户授权信息并返回对应的HTTP响应。

```json
{
 "email": "******",
 "email_verified": false,
 "iss": "https://dev-o43xb1mz7ya7ach4.us.auth0.com/",
 "aud": "YagFqRD9tfNIaac5BamjhsSatjrAnsnZ",
 "iat": 1719198638,
 "exp": 1719234638,
 "sub": "auth0|665d71e74c131177be66e607",
 "sid": "ct2U8_YQ-zT7E8i0E3MyK-z79diVQhaU"
}
```

**用户令牌刷新**

1. 模拟用户访问对应服务API。

```bash
curl --url "foo.bar.com/headers"
```

2. 验证令牌的过期时间。
3. 如果在cookie中检测到存在refresh_token，则可以访问相应的接口以交换新的id_token 和
access_token。

```bash
curl -X POST \
 --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/oauth/token" \
 --data "grant_type=refresh_token" \
 --data "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
 --data
"client_secret=ekqv5XoZuMFtYms1NszEqRx03qct6BPvGeJUeptNG4y09PrY16BKT9IWezTrrhJ " \
 --data "refresh_token=GrZ1f2JvzjAZQzSXmyr1ScWbv8aMFBvzAXHBUSiILcDEG"
```

4. 携带Authorization的标头对应access_token访问对应API。
5. 后端服务根据access_token获取用户授权信息并返回对应的HTTP响应。

##### HMAC 认证

hmac-auth插件实现了基于HMAC算法为HTTP请求生成不可伪造的签名的功能，并基于签名实现身份认证和鉴权。本文介绍如何配置hmac-auth插件。

**插件类型**

**插件类型**

认证鉴权。

**配置字段**

**认证配置**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| consumers | array of object | 必填 | - | 配置服务的调用者，用于对请求进行认证。 |
| date offset _ | number | 选填 | - | 配置允许的客户端最大时间偏移，单位为秒。根据请求头 Date 解析客户端UTC时间，可用于避免请求重放。未配置时，不做校验。 |
| global auth _ | array of string | 选填（仅实例级别配置） | - | 只能在实例级别配置。 若配置为true，则全局生效认证机制。 若配置为false，则只对做了配置的域名和路由生效认证机制。 若不配置则仅当没有域名和路由配置时全局生效（兼容以往用户使用习惯）。 |

子项 `consumers` 中每一项的配置字段说明如下。

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| key | string | 必填 | - | 配置该consumer的访问凭证。 |
| secret | string | 必填 | - | 配置用于生成签名的secret。 |
| name | string | 必填 | - | 配置该consumer的名称。 |

**鉴权配置（非必需）**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| allow | array of string | 选填（非实例级别配置） | - | 只能在路由或域名等细粒度规则上配置，对于符合匹配条件的请求，配置允许访问的 consumer，从而实现细粒度的权限控制。 |

**重要**

在一个规则里，鉴权配置和认证配置不可同时存在。 对于通过认证鉴权的请求，请求的Header会被添加一个 `X-Mse-Consumer` 字段，用以标识调用者的名称。

**配置示例**

**全局配置认证和路由粒度进行鉴权**

以下配置将对网关特定路由或域名开启 Hmac Auth 认证和鉴权。

**重要**

`key` 字段不能重复。 在实例级别做如下插件配置：

```
global_auth: false consumers:
- key: appKey-example-1
  secret: appSecret-example-1
  name: consumer-1
- key: appKey-example-2
  secret: appSecret-example-2
  name: consumer-2
```

`route-a` 和 `route-b` 两个路由做如下插件配置：

```
allow:
- consumer1
```

在 `*.example.com` 和 `test.com` 两个域名做如下插件配置：

```
allow:
- consumer2
```

**说明**

此例指定的 `route-a` 和 `route-b` 即在创建网关路由时填写的路由名称，当匹配到这两个路由时，将允许 `name` 为 `consumer1` 的调用者访问，其他调用者不允许访问。 此例指定的 `*.example.com` 和 `test.com` 用于匹配请求的域名，当发现域名匹配时，将允许 `name` 为 `consumer2` 的调用者访问，其他调用者不被允许访问。

**网关实例级别开启**

```
global_auth: true consumers:
- key: appKey-example-1
  secret: appSecret-example-1
  name: consumer-1
- key: appKey-example-2
  secret: appSecret-example-2
  name: consumer-2
```

**签名机制说明**

**配置准备**

如上指引，在插件配置中配置生成和验证签名所需的凭证配置。 key: 用于请求头 `x-ca-key` 中设置。 secret: 用于生成请求签名。

**客户端签名生成方式**

**流程简介**

客户端生成签名共分三步处理：
1. 从原始请求中提取关键数据，得到一个用来签名的字符串。
2. 使用加密算法和配置的 `secret` 对关键数据签名串进行加密处理，得到签名。
3. 将签名所相关的所有头加入到原始HTTP请求中，得到最终HTTP请求。

**签名串提取流程**

客户端需要从HTTP请求中提取出关键数据，组合成一个签名串，生成的签名串的格式如下。

```
HTTPMethod Accept Content-MD5 Content-Type Date Headers PathAndParameters
```

以上7个字段构成整个签名串，字段之间使用\n间隔，如果Headers为空，则不需要加\n，其他字段如果为空都需要保留\n。签名大小写敏感。 每个字段的提取规则如下。 HTTPMethod：HTTP的方法，全部大写，比如POST。 Accept：请求中的Accept头的值，可为空。建议显式设置 Accept Header。当 Accept 为空时，部分 HTTP客户端会给Accept设置默认值为 `*/*` ，导致签名校验失败。 Content-MD5：请求中的Content-MD5头的值可为空，只有在请求存在Body且Body为非Form形式时才计算Content-MD5头，下面是Java的Content-MD5值的参考计算方式。

```
String content-MD5 = Base64.encodeBase64(MD5(bodyStream.getbytes("UTF-8")));
```

Content-Type：请求中的Content-Type头的值，可为空。 Date：请求中的Date头的值，当未开启 `date_offset` 配置时，可为空，否则将用于时间偏移校验。 Headers：您可以选取指定的Header参与签名，关于Header的签名串拼接方式有以下规则。 参与签名计算的Header的Key按照字典排序后使用如下方式拼接。

```
HeaderKey1 + ":" + HeaderValue1 + "\n"\+ HeaderKey2 + ":" + HeaderValue2 + "\n"\+ ... HeaderKeyN + ":" + HeaderValueN + "\n"
```

某个Header的Value为空，则使用HeaderKey+":"+"\n"参与签名，需要保留Key和英文冒号。 所有参与签名的Header的Key的集合使用英文逗号分割放到Key为 `X-Ca-Signature-Headers` 的 Header中。 以下Header不参与Header签名计算：X-Ca-Signature、X-Ca-Signature-Headers、Accept、 Content-MD5、Content-Type、Date。 PathAndParameters: 这个字段包含Path、Query和Form中的所有参数，具体组织形式如下。

```
Path + "?" + Key1 + "=" + Value1 + "&" + Key2 + "=" + Value2 + ... "&" + KeyN + "=" + ValueN
```

**说明**

Query和Form参数对的Key按照字典排序后使用上面的方式拼接。 Query和Form参数为空时，则直接使用Path，不需要添加。 Query和Form存在数组参数时（Key相同，Value不同的参数），取第一个Value参与签名计算。

**签名串提取示例**

初始的HTTP请求：

```
POST /http2test/test?param1=test HTTP/1.1 host:api.aliyun.com accept:application/json; charset=utf-8 ca_version:1 content-type:application/x-www-form-urlencoded; charset=utf-8 x-ca-timestamp:1525872629832 date:Wed, 09 May 2018 13:30:29 GMT+00:00 user-agent:ALIYUN-ANDROID-DEMO x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44 content-length:33 username=xiaoming&password=123456789
```

生成的正确签名串：

```
POST application/json; charset=utf-8 application/x-www-form-urlencoded; charset=utf-8 Wed, 09 May 2018 13:30:29 GMT+00:00 x-ca-key:203753385 x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44 x-ca-signature-method:HmacSHA256 x-ca-timestamp:1525872629832 /http2test/test?param1=test&password=123456789&username=xiaoming
```

**签名计算流程**

客户端从HTTP请求中提取出关键数据组装成签名串后，需要对签名串进行加密及编码处理，形成最终的签名。 具体的加密形式如下，其中 `stringToSign` 是提取出来的签名串， `secret` 是插件配置中填写的， `sign` 是最终生成的签名。

```
Mac hmacSha256 = Mac.getInstance("HmacSHA256"); byte[] secretBytes = secret.getBytes("UTF-8"); hmacSha256.init(new SecretKeySpec(secretBytes, 0, secretBytes.length, "HmacSHA256")); byte[] result = hmacSha256.doFinal(stringToSign.getBytes("UTF-8")); String sign = Base64.encodeBase64String(result);
```

将 `stringToSign` 使用UTF-8解码后得到Byte数组，然后使用加密算法对Byte数组进行加密，然后使用 Base64算法进行编码，形成最终的签名。

**添加签名流程**

客户端需要将以下四个Header放在HTTP请求中传输给云原生API网关，进行签名校验。 x-ca-key：取值APP Key。必选。 x-ca-signature-method：签名算法。取值HmacSHA256或者HmacSHA1，可选，默认值为 HmacSHA256。 x-ca-signature-headers：所有签名头的Key的集合。使用英文逗号分隔，可选。 x-ca-signature：签名。必选。 下面是携带签名的整个HTTP请求的示例。

```
POST /http2test/test?param1=test HTTP/1.1 host:api.aliyun.com accept:application/json; charset=utf-8 ca_version:1 content-type:application/x-www-form-urlencoded; charset=utf-8 x-ca-timestamp:1525872629832 date:Wed, 09 May 2018 13:30:29 GMT+00:00 user-agent:ALIYUN-ANDROID-DEMO x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44 x-ca-key:203753385 x-ca-signature-method:HmacSHA256 x-ca-signature-headers:x-ca-timestamp,x-ca-key,x-ca-nonce,x-ca-signature-method x-ca-signature:xfX+bZxY2yl7EB/qdoDy9v/uscw3Nnj1pgoU+Bm6xdM= content-length:33 username=xiaoming&password=123456789
```

**服务端签名验证方式**

**流程简介**

服务器验证客户端签名一共分四步处理。
1. 从接收到的请求中提取关键数据，得到一个用来签名的字符串。
2. 从接收到的请求中读取 `key` ，通过 `key` 查询到对应的 `secret` 。
3. 使用加密算法和 `secret` 对关键数据签名串进行加密处理，得到签名。
4. 从接收到的请求中读取客户端签名，对比服务器端签名和客户端签名的一致性。

**签名排错方法**

网关签名校验失败时，会将服务端的签名串（StringToSign）放到HTTP Response的Header中返回到客户端，Key为：X-Ca-Error-Message，您只需要将本地计算的签名串（StringToSign）与服务端返回的签名串进行对比即可找到问题。 如果服务端与客户端的StringToSign一致，请检查用于签名计算的APP Secret是否正确。 因为HTTP Header中无法表示换行，因此StringToSign中的换行符都被替换成 # ，如下所示。

```
X-Ca-Error-Message: Server StringToSign:`GET#application/json##application/json##X-Ca- Key:200000#X-Ca-Timestamp:1589458000000#/app/v1/config/keys?keys=TEST`
```

**相关错误码**

| HTTP状态码 | 出错信息 | 原因说明 |
|---|---|---|
| 400 | Invalid Signature. | 请求头x-ca-signature签名串，与服务端计算得到签名不一致。 |
| 400 | Invalid Content-MD5. | 请求头content-md5不正确。 |
| 400 | Invalid Date. | 根据请求头date计算时间偏移超过配置的 date offset。 _ |
| 401 | Invalid Key. | 请求头未提供x-ca-key，或者x-ca-key无效。 |
| 401 | Empty Signature. | 请求头未提供x-ca-signature签名串。 |
| 403 | Unauthorized Consumer. | 请求的调用方无访问权限。 |
| 413 | Request Body Too Large. | 请求Body超过限制大小：32MB。 |
| 413 | Payload Too Large. | 请求Body超过全局配置 DownstreamConnectionBufferLimits，请在参数配置页调高此项。 |

**说明**

注意：请谨慎调高 `DownstreamConnectionBufferLimits`。此参数配置调高后，网关内存使用将有显著增加。

##### 外部认证

ext-auth插件实现了向外部授权服务发送鉴权请求，以检查客户端请求是否得到授权的功能。本文介绍如何配置ext-auth插件。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `360` 。

**配置字段**

|  | 名称 |  | 数据类型 | 必填 |  |  |  | 默认值 | 描述 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | http service _ |  | object | 是 |  |  |  | - | 外部授权服务配置。 |  |  |  |
|  | match type _ |  | string | 否 |  |  |  |  | 可选 whitelist 或 blacklist 。 |  |  |  |
|  | match list _ |  | array of MatchRule | 否 |  |  |  |  | 一个包含 ( match rule domain , match rule path _ _ _ _ , match rule type ) 的列表。 _ _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | match rule domain _ _ |  |  |
|  | failure mode _ _ allow |  | bool | 否 |  |  |  | false | 当设置为true时，即使与授权服务的通信失败，或者授权服务返回了HTTP 5xx错误，仍会接受客户端请求。 |  |  |  |
|  | failure mode _ _ |  |  | 否 |  |  |  |  | 当 failure mode allow 和 failure mode _ _ _ allow header add 都设置为true 时，若与授 _ _ _ 权服务的通信失败，或授权服务返回了HTTP 5xx错误，那么请求头中将会添加 x-envoy-auth- failure-mode-allowed: true 。 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | failure mode allow _ _ |  |
|  |  | failure mode _ _ |  |  |  |  |  |  | _ _ allow header add _ _ _ |  | _ _ |  |
|  | allow header ad _ _ |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | false |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | x-envoy-auth- |
|  | d |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | failure-mode-allowed: true |  |  |  |
|  | status on err _ _ or |  | int | 否 |  |  |  | 403 | 当授权服务无法访问或状态码为5xx时，设置返回给客户端的HTTP状态码。默认状态码是 403 。 |  |  |  |

|  |  | http service _ |
|---|---|---|

|  |  | failure mode _ _ | boo |
|---|---|---|---|
|  | allow |  |  |

|  |  | status on err _ _ |  |
|---|---|---|---|
|  | or |  |  |

`http_service` 中每一项的配置字段说明：

| 名称 | 数据类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|

|  | endpoint mode _ |  | string | 否 | envoy | 可选 envoy 或 forward auth _ 。 |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | forward auth _ |  |  |
|  | endpoint |  | object | 是 | - | 发送鉴权请求的 HTTP服务信息。 |  |  |
|  | timeout |  | int | 否 | 1000 | ext-auth 服务连接超时时间， 单位毫秒。 |  |  |
|  | authorization _ request |  | object | 否 | - | 发送鉴权请求配置。 |  |  |
|  |  | authorization _ | object |  |  |  |  |  |
|  | request |  |  |  |  |  |  |  |
|  | authorization _ response |  | object | 否 | - | 处理鉴权响应配置。 |  |  |
|  |  | authorization _ | object |  |  |  |  |  |
|  | response |  |  |  |  |  |  |  |

|  |  | endpoint mode _ |
|---|---|---|

`endpoint` 中每一项的配置字段说明：

|  | 名称 |  | 数据类型 | 必填 |  | 默认值 |  |  |  | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | service name _ |  | string | 是 |  | - |  |  |  | 输入授权服务名称，带服务类型的完整 FQDN 名称， 例如 ext- auth.dns 、 e |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ext- |  |  |  |
|  |  | service name _ |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | auth.dns |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 、 | e |  |
|  |  |  |  |  |  |  |  |  |  | ns.svc.cluster. |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | local |  |  |  |  |
|  | service port _ |  | int | 否 |  | 80 |  |  |  | 输入授权服务的服务端口。 |  |  |  |  |
|  |  | service port _ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | service host _ |  | string | 否 |  | - |  |  |  | 请求授权服务时设置的Host 头，不填时和FQDN 保持一致。 |  |  |  |  |
|  |  | service host _ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | path prefix _ |  | string | endpoint mode _ 为 envoy 时必填。 |  | - |  |  |  | endpoint mode _ 为 envoy 时 ，客户端向授权服务发送请求的请求路径前缀。 |  |  |  |  |

|  |  | endpoint mode _ |
|---|---|---|

| g |  |
|---|---|

|  | request method _ |  | string |  |  | 否 |  |  |  | GET |  |  | endpoint mode _ 为 forward a _ uth 时，客户端向授权服务发送请求的HTTP Method。 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | endpoint mode _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 为 | forward a _ |  |
|  |  | request method _ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | uth |  |  |  |  |
|  | path |  | string |  |  | endpoint mode _ |  |  |  | - |  |  | endpoint mode _ 为 forward a _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | endpoint mode _ |  |  |  |
|  |  |  |  |  |  |  | endpoint mode _ |  |  |  |  |  |  |  |  | _ |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 为 | forward a _ |  |
|  |  |  |  | g |  |  |  | 为 | forward a _ | - |  |  | uth |  |  |  |  |

`authorization_request` 中每一项的配置字段说明：

|  | 名称 |  | 数据类型 | 必填 | 默认值 |  |  |  |  | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | allowed header _ s |  | array of StringMatcher | 否 | - |  |  |  |  | 设置后，匹配项的客户端请求头将添加到授权服务请求中的请求头中。除了用户自定义的头部匹配规则外，授权服务请求中会自动包含 Authorizati on HTTP头 （ endpoint mod _ e 为 forward _ auth 时，会添加 X- Forwarded-* 的请求头）。 |  |  |  |  |
|  |  | allowed header _ |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | Authorizati |  |  |  |
|  | s |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | on |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | HTTP头 |  |  |
|  |  |  |  |  |  |  |  |  |  | （ |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | e |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 为 |  | forward _ |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 时，会添 |  |
|  |  |  |  |  |  |  |  |  |  | 加 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | Forwarded-* |  |  |  |  |
|  | headers to add _ _ |  | map[string]string | 否 | - |  |  |  |  | 设置将包含在授权服务请求中的请求头列表。 重要同名的客户端请求头将被覆盖。 |  |  |  |  |
|  |  | headers to add _ _ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | with request b _ _ ody |  | bool | 否 | false |  |  |  |  | 缓冲客户端请求体，并将其发送至鉴权请求中（HTTP Method为GET、 OPTIONS、HEAD 请求时不生效）。 |  |  |  |  |
|  |  | with request b _ _ | bo |  |  |  |  |  |  |  |  |  |  |  |
|  | ody |  |  |  |  |  |  |  |  |  |  |  |  |  |

|  | max request bo _ _ dy bytes _ |  | int | 否 | 10MB |  |  | 设置在内存中保存客户端请求体的最大尺寸。当客户端请求体达到在此字段中设置的数值时，将会返回HTTP 413状态码，并且不会启动授权过程。 重要此设置会优先于 failure mode allow _ _ 的配置。 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | max request bo _ _ | int |  |  |  |  |  |  |  |  |  |
|  | dy bytes _ |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 重要此设置会优先于 failure |  |  |  |
|  |  |  |  |  |  |  |  |  |  | failure |  |  |
|  |  |  |  |  |  |  |  |  | mode allow _ _ |  |  |  |

`authorization_response` 中每一项的配置字段说明：

|  | 名称 |  | 数据类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
|  | allowed upstre _ am headers _ |  | array of StringMatcher | 否 | - | 匹配项的鉴权请求的响应头将添加到原始的客户端请求头中。请注意，同名的请求头将被覆盖。 |
|  |  | allowed upstre _ | array of |  |  |  |
|  | am headers _ |  |  |  |  |  |
|  | allowed client _ headers _ |  | array of StringMatcher | 否 | - | 如果不设置，在请求被拒绝时，所有的鉴权请求的响应头将添加到客户端的响应头中。当设置后，在请求被拒绝时，匹配项的鉴权请求的响应头将添加到客户端的响应头中。 |
|  |  | allowed client _ | array of |  |  |  |
|  | headers _ |  |  |  |  |  |

`StringMatcher` 类型每一项的配置字段说明，在使用 `array of StringMatcher` 时会按照数组中定义的 StringMatcher 顺序依次进行配置。

| 名称 | 数据类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|
| exact | string | 否， exact , prefix , suff ix , contains , regex 中选填一项。 | - | 精确匹配。 |

|  |  |  | exact |  |  |  |
|---|---|---|---|---|---|---|
|  |  | prefix |  |  |  |  |
|  |  |  |  |  | , |  |
|  |  | ix | , |  |  |  |

| prefix | string | 否， exact , prefix , suff ix , contains , regex 中选填一项。 | - | 前缀匹配。 |
|---|---|---|---|---|
| suffix | string | 否， exact , prefix , suff ix , contains , regex 中选填一项。 | - | 后缀匹配。 |
| contains | string | 否， exact , prefix , suff ix , contains , regex 中选填一项。 | - | 是否包含。 |
| regex | string | 否， exact , prefix , suff ix , contains , regex 中选填一项。 | - | 正则匹配。 |

|  |  |  |  | exact |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | prefix |  |  |  |  |  |
|  |  |  |  |  |  | , |  |
|  |  | ix |  | , |  |  |  |

|  |  |  |  | exact |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | prefix |  |  |  |  |  |
|  |  |  |  |  |  | , |  |
|  |  | ix |  | , |  |  |  |

|  |  |  | exact |  |  |  |
|---|---|---|---|---|---|---|
|  |  | prefix |  |  |  |  |
|  |  |  |  |  | , |  |
|  |  | ix | , |  |  |  |

|  |  |  | exact |  |  |  |
|---|---|---|---|---|---|---|
|  |  | prefix |  |  |  |  |
|  |  |  |  |  | , |  |
|  |  | ix | , |  |  |  |

MatchRule 类型每一项的配置字段说明，在使用 `array of MatchRule` 时会按照数组中定义的 MatchRule 顺序依次进行配置。

|  | 名称 |  | 数据类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
|  | match rule dom _ _ ain |  | string | 否 | - | 匹配规则域名，支持通配符模式，例如 *.bar.com 。 |
|  |  | match rule dom _ _ | str |  |  |  |
|  | ain |  |  |  |  |  |
|  | match rule met _ _ hod |  | []string | 否 | - | 匹配请求方法。 |
|  |  | match rule met _ _ | []s |  |  |  |
|  | hod |  |  |  |  |  |
|  | match rule pat _ _ h |  | string | 否 | - | 匹配请求路径的规则。 |
|  |  | match rule pat _ _ |  |  |  |  |
|  | h |  |  |  |  |  |

|  | match rule typ _ _ | string | 否 | - |  |  | 匹配请求路径的规则类型，可选 exact , p |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  | p |  |
|  | e |  |  |  |  |  | refix |  |  | , | suffi |  |  |
|  |  |  |  |  |  |  | x | , |  |  |  |  |  |
|  |  |  |  |  |  |  |  | regex |  |  |  |  |  |

**两种 endpoint_mode 的区别**

| endpoint mode _ |  |
|---|---|
| 的 | path prefix _ |

|  | forward auth _ |
|---|---|
| path |  |

| Header | 说明 |  |
|---|---|---|
| x-forwarded-proto | 原始请求的scheme，比如 http/https。 |  |
| x-forwarded-method | 原始请求的方法，比如 get/post/delete/patch。 |  |
| x-forwarded-host | 原始请求的host。 |  |
| x-forwarded-uri | 原始请求的path，包含路径参数，比如 /v1/app? test=true 。 |  |

|  | test=true |
|---|---|

**黑白名单模式**

支持黑白名单模式配置，默认为白名单模式，白名单为空，即所有请求都需要经过验证，匹配域名支持泛域名例如 `*.bar.com` ，匹配规则支持 `exact` , `prefix` , `suffix` , `contains` , `regex` 。

**白名单模式**

# 白名单模式配置，符合白名单规则的请求无需验证

```
match_type: 'whitelist' match_list:
```

# 所有以 `api.example.com` 为域名，且路径前缀为 `/public` 的请求无需验证

```
 - match_rule_domain: 'api.example.com'
 match_rule_path: '/public'
 match_rule_type: 'prefix'
```

# 针对图片资源服务器 `images.example.com`，所有 `GET` 请求无需验证

```
 - match_rule_domain: 'images.example.com'
 match_rule_method: ["GET"]
```

# 所有域名下，路径精确匹配 `/health-check` 的 `HEAD` 请求无需验证

```
 - match_rule_method: ["HEAD"]
 match_rule_path: '/health-check'
 match_rule_type: 'exact'
```

**黑名单模式**

# 黑名单模式配置，符合黑名单规则的请求需要验证

```
match_type: 'blacklist' match_list:
```

# 所有以 `admin.example.com` 为域名，且路径前缀为 `/sensitive` 的请求需要验证

```
 - match_rule_domain: 'admin.example.com'
 match_rule_path: '/sensitive'
 match_rule_type: 'prefix'
```

# 所有域名下，路径精确匹配 `/user` 的 `DELETE` 请求需要验证

```
 - match_rule_method: ["DELETE"]
 match_rule_path: '/user'
 match_rule_type: 'exact'
```

# 所有以 `legacy.example.com` 为域名的 `POST` 请求需要验证

```
 - match_rule_domain: 'legacy.example.com'
 match_rule_method: ["POST"]
```

**配置示例**

| 面假设 | ext-auth |  |
|---|---|---|
|  |  | ，命名空间 |

**endpoint_mode为envoy时**

**示例1**

`ext-auth` 插件的配置：

```
http_service:
 endpoint_mode: envoy
 endpoint:
 service_name: ext-auth.backend.svc.cluster.local
 service_port: 8090
 path_prefix: /auth
 timeout: 1000
```

使用如下请求网关，当开启 `ext-auth` 插件后：

```bash
curl -X POST http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf- 00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx"
```

**请求** `ext-auth` **服务成功：**
`ext-auth` 服务将接收到如下的鉴权请求：

```
POST /auth/users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 HTTP/1.1 Host: ext-auth.backend.svc.cluster.local Authorization: xxx Content-Length: 0
```

**请求** `ext-auth` **服务失败：**
当调用 `ext-auth` 服务响应为 5xx 时，客户端将接收到HTTP响应码403和 `ext-auth` 服务返回的全量响应头。 假如 `ext-auth` 服务返回了 `x-auth-version: 1.0` 和 `x-auth-failed: true` 的响应头，会传递给客户端。

```
HTTP/1.1 403 Forbidden x-auth-version: 1.0 x-auth-failed: true date: Tue, 16 Jul 2024 00:19:41 GMT server: istio-envoy content-length: 0
```

当 `ext-auth` 无法访问或状态码为5xx时，将以 `status_on_error` 配置的状态码拒绝客户端请求。

| ext-auth | 服务返回其他HT |
|---|---|

**示例2**

`ext-auth` 插件的配置：

```
http_service:
 authorization_request:
 allowed_headers:
 - exact: x-auth-version
 headers_to_add:
 x-envoy-header: true
 authorization_response:
 allowed_upstream_headers:
 - exact: x-user-id
 - exact: x-auth-version
 endpoint_mode: envoy
 endpoint:
 service_name: ext-auth.backend.svc.cluster.local
 service_host: my-domain.local
 service_port: 8090
 path_prefix: /auth
 timeout: 1000
```

使用如下请求网关，当开启 `ext-auth` 插件后：

```bash
curl -X POST http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf- 00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx"
```

`ext-auth` 服务将接收到如下的鉴权请求：

```
POST /auth/users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 HTTP/1.1 Host: my-domain.local Authorization: xxx X-Auth-Version: 1.0 x-envoy-header: true Content-Length: 0
```

`ext-auth` 服务返回响应头中如果包含 `x-user-id` 和 `x-auth-version` ，网关调用upstream时的请求中会带上这两个请求头。

**endpoint_mode为forward_auth时**

**示例1**

`ext-auth` 插件的配置：

```
http_service:
 endpoint_mode: forward_auth
 endpoint:
 service_name: ext-auth.backend.svc.cluster.local
 service_port: 8090
 path: /auth
 request_method: POST
 timeout: 1000
```

使用如下请求网关，当开启 `ext-auth` 插件后：

```bash
curl -i http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf- 00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx" -H "Host: foo.bar.com"
```

**请求** `ext-auth` **服务成功：**
`ext-auth` 服务将接收到如下的鉴权请求：

```
POST /auth HTTP/1.1 Host: ext-auth.backend.svc.cluster.local Authorization: xxx X-Forwarded-Proto: HTTP X-Forwarded-Host: foo.bar.com X-Forwarded-Uri: /users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 X-Forwarded-Method: GET Content-Length: 0
```

**请求** `ext-auth` **服务失败：**
当调用 `ext-auth` 服务响应为 5xx 时，客户端将接收到HTTP响应码403和 `ext-auth` 服务返回的全量响应头。 假如 `ext-auth` 服务返回了 `x-auth-version: 1.0` 和 `x-auth-failed: true` 的响应头，会传递给客户端。

```
HTTP/1.1 403 Forbidden x-auth-version: 1.0 x-auth-failed: true date: Tue, 16 Jul 2024 00:19:41 GMT server: istio-envoy content-length: 0
```

当 `ext-auth` 无法访问或状态码为5xx时，将以 `status_on_error` 配置的状态码拒绝客户端请求。

| ext-auth | 服务返回其他HT |
|---|---|

**示例2**

`ext-auth` 插件的配置：

```
http_service:
 authorization_request:
 allowed_headers:
 - exact: x-auth-version
 headers_to_add:
 x-envoy-header: true
 authorization_response:
 allowed_upstream_headers:
 - exact: x-user-id
 - exact: x-auth-version
 endpoint_mode: forward_auth
 endpoint:
 service_name: ext-auth.backend.svc.cluster.local
 service_host: my-domain.local
 service_port: 8090
 path: /auth
 request_method: POST
 timeout: 1000
```

使用如下请求网关，当开启 `ext-auth` 插件后：

```bash
curl -i http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf- 00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx" -H "X-Auth-Version: 1.0" -H "Host: foo.bar.com"
```

`ext-auth` 服务将接收到如下的鉴权请求：

```
POST /auth HTTP/1.1 Host: my-domain.local Authorization: xxx X-Forwarded-Proto: HTTP X-Forwarded-Host: foo.bar.com X-Forwarded-Uri: /users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 X-Forwarded-Method: GET X-Auth-Version: 1.0 x-envoy-header: true Content-Length: 0
```

`ext-auth` 服务返回响应头中如果包含 `x-user-id` 和 `x-auth-version` ，网关调用upstream时的请求中会带上这两个请求头。

##### OAuth2 认证

OAuth2插件实现了基于JWT（JSON Web Tokens）进行OAuth2 Access Token签发的能力, 遵循RFC9068规范。本文介绍如何配置OAuth2插件。

**插件类型**

认证鉴权。

**插件配置说明**

**配置字段**

**认证配置**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| consumers | array of object | 必填 | - | 配置服务的调用者，用于对请求进行认证。 |
| issuer | string | 选填 | Higress - Gatewa y | 用于填充JWT中的issuer。 |
| auth path _ | string | 选填 | /oauth2 /token | 指定路径后缀用于签发Token， 路由级配置时，要确保能首先匹配对应的路由。在使用 API 管理时，需要创建相同路径的接口。 |
| global crede _ ntials | bool | 选填 | true | 在通过 consumer 认证的前提下，允许任意路由签发的凭证访问。 |
| auth header _ _ name | string | 选填 | Authori zation | 用于指定从哪个请求头获取 JWT。 |
| token ttl _ | number | 选填 | 7200 | Token从签发后多长时间内有效，单位为秒。 |
| clock skew s _ _ econds | number | 选填 | 60 | 校验JWT的exp和iat字段时允许的时钟偏移量，单位为秒。 |
| keep token _ | bool | 选填 | true | 转发给后端时是否保留JWT。 |

| global auth _ | array of string | 选填（仅实例级别配置） | - | 只能在实例级别配置。 若配置为true，则全局生效认证机制。 若配置为false，则只对做了配置的域名和路由生效认证机制。 若不配置则仅当没有域名和路由配置时全局生效（兼容过往客户的使用习惯）。 |
|---|---|---|---|---|

子项 `consumers` 中每一项的配置字段说明如下。

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| name | string | 必填 | - | 配置该consumer的名称。 |
| client id _ | string | 必填 | - | OAuth2 client id。 |
| client secret _ | string | 必填 | - | OAuth2 client secret。 |

**重要**

对于开启该配置的路由，如果路径后缀和 `auth_path` 匹配，则该路由不会被转发到原目标服务，而是用于生成Token。 如果关闭 `global_credentials` ，请确保启用此插件的路由不是精确匹配路由，此时若存在另一条前缀匹配路由，则可能导致预期外行为。 对于通过认证鉴权的请求，请求的header会被添加一个 `X-Mse-Consumer` 字段，用以标识调用者的名称。

**鉴权配置（非必需）**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| allow | array of string | 选填（非实例级别配置） | - | 只能在路由或域名等细粒度规则上配置，对于符合匹配条件的请求，配置允许访问的 consumer，从而实现细粒度的权限控制。 |

**重要**

在一个规则里，鉴权配置和认证配置不可同时存在。

**配置示例**

**路由粒度配置认证**

在 `route-a` 和 `route-b` 两个路由做如下插件配置：

```
consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

此时虽然使用同一份配置，但 `route-a` 下签发的凭证无法用于访问 `route-b` ，反之亦然。 如果希望同一份配置共享凭证访问权限，可以做如下配置：

```
global_credentials: true consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**全局配置认证和路由粒度进行鉴权**

以下配置将对网关特定路由或域名开启 Jwt Auth 认证和鉴权，注意如果一个JWT能匹配多个 `jwks` ，则按照配置顺序命中第一个匹配的 `consumer` 。 在实例级别做如下插件配置：

```
global_auth: false consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- name: consumer2
  client_id: 87654321-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: hgfedcba-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

在 `route-a` 和 `route-b` 两个路由做如下插件配置：

```
allow:
- consumer1
```

在 `*.example.com` 和 `test.com` 两个域名做如下插件配置：

```
allow:
- consumer2
```

**说明**

此例指定的 `route-a` 和 `route-b` 即在创建网关路由时填写的路由名称，当匹配到这两个路由时，将允许 `name` 为 `consumer1` 的调用者访问，其他调用者不允许访问。 此例指定的 `*.example.com` 和 `test.com` 用于匹配请求的域名，当发现域名匹配时，将允许 `name` 为 `consumer2` 的调用者访问，其他调用者不允许访问。

**网关实例级别开启**

```
global_auth: true consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- name: consumer2
  client_id: 87654321-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: hgfedcba-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**请求示例**

**使用 Client Credential 授权模式**

**获取 AccessToken**

# 通过 `GET` 方法获取（推荐）

```bash
curl 'http://test.com/oauth2/token?grant_type=client_credentials&client_id=12345678-xxx x-xxxx-xxxx-xxxxxxxxxxxx&client_secret=abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
```

# 通过 `POST` 方法获取（需要先匹配到有真实目标服务的路由，否则网关不会读取请求 `Body`）

```bash
curl 'http://test.com/oauth2/token' -H 'content-type: application/x-www-form-urlencoded ' -d 'grant_type=client_credentials&client_id=12345678-xxxx-xxxx-xxxxxxxxxxxxxxxx&client_secret=abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
```

# 获取响应中的 `access_token` 字段即可:

```json
{
  "token_type": "bearer",
  "access_token":
"eyJh************.eyJhdWQiOiJkZWZhdWx0IiwiY2xpZW50X2lkIjoiMTIzNDU2NzgteHh4eC14eHh4LXh4eHg Hh4eHh4eHh4eHh4IiwiZXhwIjoxNjg3OTUxNDYzLCJpYXQiOjE2ODc5NDQyNjMsImlzcyI6IkhpZ3Jlc3MtR2F0ZX eSIsImp0aSI6IjEwOTU5ZDFiLThkNjEtNGRlYy1iZWE3LTk0ODEwMzc1YjYzYyIsInN1YiI6ImNvbnN1bWVyMSJ9. T_rG3DcV9543vBQgneVqoGfIhVeOuUBwLJJ4Wycb0",
  "expires_in": 7200
}
```

**使用 AccessToken 请求**

```bash
curl 'http://test.com' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6ImFwcGxpY2F0aW9uXC9hdCtqd3QifQ.eyJhdWQiOiJkZWZhdWx0IiwiY2xpZW X2lkIjoiMTIzNDU2NzgteHh4eC14eHh4LXh4eHgteHh4eHh4eHh4eHh4IiwiZXhwIjoxNjg3OTUxNDYzLCJpYXQiO 2ODc5NDQyNjMsImlzcyI6IkhpZ3Jlc3MtR2F0ZXdheSIsImp0aSI6IjEwOTU5ZDFiLThkNjEtNGRlYy1iZWE3LTk0 EwMzc1YjYzYyIsInN1YiI6ImNvbnN1bWVyMSJ9.NkT_rG3DcV9543vBQgneVqoGfIhVeOuUBwLJJ4Wycb0'
```

**相关错误码**

| HTTP状态码 | 出错信息 | 原因说明 |
|---|---|---|
| 401 | Invalid Jwt token. | 请求头未提供JWT、JWT格式错误或过期等原因。 |

| 403 | Access Denied. | 无权限访问当前路由。 |
|---|---|---|

##### OPA 策略

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `225` 。

**配置字段**

| 字段 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| policy | string | 必填 | - | opa策略。 |
| timeout | string | 必填 | - | 访问超时时间设置。 |
| serviceSource | string | 必填 | - | k8s、nacos、ip、route。 |
| host | string | 非必填 | - | 服务主机（serviceSource为 ip 必填）。 |
| serviceName | string | 非必填 | - | 服务名称（serviceSource 为 k8s,nacos,ip 必填）。 |
| servicePort | string | 非必填 | - | 服务端口（serviceSource 为 k8s,nacos,ip 必填）。 |
| namespace | string | 非必填 | - | 命名空间（serviceSource为 k8s,nacos 必填）。 |

**配置示例**

```
serviceSource: k8s serviceName: opa servicePort: 8181 namespace: higress-backend policy: example1 timeout: 5s
```

**OPA 服务安装参考**

**启动 OPA 服务**

```java
docker run -d --name opa -p 8181:8181 openpolicyagent/opa:0.35.0 run -s curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
 -H 'Content-Type: text/plain' \
 -d 'package example1
import input.request default allow = false allow {
 # HTTP method must GET
 request.method == "GET"
}'
```

**查询策略**

```bash
curl -X POST '127.0.0.1:8181/v1/data/example1/allow' \
 -H 'Content-Type: application/json' \
 -d '{"input":{"request":{"method":"GET"}}}'
```

#### 安全

##### 跨域资源共享

**功能说明**

`cors` 插件可以为服务端启用CORS（Cross-Origin Resource Sharing，跨域资源共享）的返回http响应头。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| allow origins _ | array of string | 选填 | * | 允许跨域访问的 Origin，格式为 scheme://host:po rt，示例如 http://example .com:8081。当 allow credentials _ 为false时，可以使用*来表示允许所有 Origin通过。 |

| allow origin patt _ _ erns | array of string | 选填 | - | 允许跨域访问的 Origin模式匹配， 用*匹配域名或者端口， 比如 http://.example.c om — 匹配域名， http://.example.c om:[8080,9090] — 匹配域名和指定端口， http://.example.c om:[] — 匹配域名和所有端口。单独* 表示匹配所有域名和端口。 |
|---|---|---|---|---|
| allow methods _ | array of string | 选填 | GET, PUT, POST, DELETE, PATCH, OPTIONS | 允许跨域访问的 Method，比如： GET，POST等。可以使用 * 来表示允许所有 Method。 |
| allow headers _ | array of string | 选填 | DNT,X- CustomHeader,K eep-Alive,User- Agent,X- Requested- With， If-Modified- Since,Cache- Control,Content- Type,Authorizatio n | 允许跨域访问时请求方携带哪些非 CORS规范以外的 Header。可以使用 *来表示允许任意 Header。 |
| expose headers _ | array of string | 选填 | - | 允许跨域访问时响应方携带哪些非 CORS规范以外的 Header。可以使用 *来表示允许任意 Header。 |
| allow credentials _ | bool | 选填 | false | 是否允许跨域访问的请求方携带凭据 （如 Cookie等）。 根据CORS规范，如果设置该选项为 true，在 allow origins不能 _ 使用*， 替换成使用 allow origin patt _ _ erns *。 |

| max age _ | number | 选填 | 86400秒 | 浏览器缓存CORS结果的最大时间，单位为秒。 在这个时间范围内，浏览器会复用上一次的检查结果。 |
|---|---|---|---|---|

**配置示例**

**允许所有跨域访问, 不允许请求方携带凭据。**

```
allow_origins:
 - '*'
allow_methods:
 - '*'
allow_headers:
 - '*'
expose_headers:
 - '*'
allow_credentials: false max_age: 7200
```

**允许所有跨域访问，同时允许请求方携带凭据。**

```
allow_origin_patterns:
 - '*'
allow_methods:
 - '*'
allow_headers:
 - '*'
expose_headers:
 - '*'
allow_credentials: true max_age: 7200
```

**允许特定子域,特定方法，特定请求头跨域访问，同时允许请求方携带凭据。**

```
allow_origin_patterns:
 - http://*.example.com
 - http://*.example.org:[8080,9090]
allow_methods:
 - GET
 - PUT
 - POST
 - DELETE
allow_headers:
 - Token
 - Content-Type
 - Authorization
expose_headers:
 - '*'
allow_credentials: true max_age: 7200
```

**测试**

**测试配置**

```
apiVersion: networking.higress.io/v1 kind: McpBridge metadata:
 name: mcp-cors-httpbin
 namespace: higress-system
spec:
 registries:
 - domain: httpbin.org
 name: httpbin
 port: 80
 type: dns
--apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 annotations:
 higress.io/destination: httpbin.dns
 higress.io/upstream-vhost: "httpbin.org"
 higress.io/backend-protocol: HTTP
 name: ingress-cors-httpbin
 namespace: higress-system
spec:
 ingressClassName: higress
 rules:
 - host: httpbin.example.com
 http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: mcp-cors-httpbin
```

`th` /

```
 path: /
 pathType: Prefix
--apiVersion: extensions.higress.io/v1alpha1 kind: WasmPlugin metadata:
 name: wasm-cors-httpbin
 namespace: higress-system
spec:
 defaultConfigDisable: true
 matchRules:
 - config:
 allow_origins:
 - http://httpbin.example.net
 allow_origin_patterns:
 - http://*.example.com:[*]
 - http://*.example.org:[9090,8080]
 allow_methods:
 - GET
 - POST
 - PATCH
 allow_headers:
 - Content-Type
 - Token
 - Authorization
 expose_headers:
 - X-Custom-Header
 - X-Env-UTM
 allow_credentials: true
 max_age: 3600
 configDisable: false
 ingress:
 - ingress-cors-httpbin
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/cors:1.0.0
 imagePullPolicy: Always
```

**请求测试**

**简单请求**

```bash
curl -v -H "Origin: http://httpbin2.example.org:9090" -H "Host: httpbin.example.com" http://127.0.0.1/anything/get\?foo\=1 < HTTP/1.1 200 OK
> x-cors-version: 1.0.0
> access-control-allow-origin: http://httpbin2.example.org:9090
> access-control-expose-headers: X-Custom-Header,X-Env-UTM
> access-control-allow-credentials: true
```

**预检请求**

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H "Host: httpbin.example.com" -H "Access-Control-Request-Method: POST" -H "Access-Control-Reque st-Headers: Content-Type, Token" http://127.0.0.1/anything/get\?foo\=1 < HTTP/1.1 200 OK < x-cors-version: 1.0.0 < access-control-allow-origin: http://httpbin2.example.org:9090 < access-control-allow-methods: GET,POST,PATCH < access-control-allow-headers: Content-Type,Token,Authorization < access-control-expose-headers: X-Custom-Header,X-Env-UTM < access-control-allow-credentials: true < access-control-max-age: 3600 < date: Tue, 23 May 2023 11:41:28 GMT < server: istio-envoy < content-length: 0
```

<

```
* Connection #0 to host 127.0.0.1 left intact
* Closing connection 0
```

**非法CORS Origin预检请求**

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org" -H "Host: httpbin.example.com" -H "Access-Control-Request-Method: GET" http://127.0.0.1/anything/get\?foo\=1
 HTTP/1.1 403 Forbidden
< content-length: 70 < content-type: text/plain < x-cors-version: 1.0.0 < date: Tue, 23 May 2023 11:27:01 GMT < server: istio-envoy
```

<

```
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

**非法CORS Method预检请求**

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H "Host: httpbin.example.com" -H "Access-Control-Request-Method: DELETE" http://127.0.0.1/anything/get\?foo\=1 < HTTP/1.1 403 Forbidden < content-length: 49 < content-type: text/plain < x-cors-version: 1.0.0 < date: Tue, 23 May 2023 11:28:51 GMT < server: istio-envoy
```

<

```
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

**非法CORS Header预检请求**

```bash
 curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H  "Host:
httpbin.example.com" -H "Access-Control-Request-Method: GET" -H "Access-Control-Request -Headers: TokenView" http://127.0.0.1/anything/get\?foo\=1 < HTTP/1.1 403 Forbidden < content-length: 52 < content-type: text/plain < x-cors-version: 1.0.0 < date: Tue, 23 May 2023 11:31:03 GMT < server: istio-envoy
```

<

```
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

##### IP限制

ip-restriction 插件可以通过将 IP 地址列入白名单或黑名单来限制对服务或路由的访问。支持对单个 IP 地址、多个 IP 地址和类似 10.10.10.0/24 的 CIDR范围的限制。本文介绍如何配置ip-restriction插件。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `210` 。

**配置说明**

| 配置项 | 类型 | 必填 | 默认值 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| ip source type _ _ | string | 否 | origin-source |  | 可选值： 对端socket ip： origin- source 。 通过header获取： header 。 |  |  |
|  |  |  |  |  |  | origin- |  |
|  |  |  |  |  | source |  |  |
| ip header name _ _ | string | 否 | x-forwarded-for |  | 当 ip source ty _ _ pe 为 header 时，指定自定义IP 来源头。 |  |  |
| allow | array | 否 | [] |  | 白名单列表。 |  |  |
| deny | array | 否 | [] |  | 黑名单列表。 |  |  |
| status | int | 否 | 403 |  | 拒绝访问时的 HTTP 状态码。 |  |  |

|  |  | ip source ty _ _ |  |
|---|---|---|---|
| warded-for | pe |  |  |

| message | string | 否 | Your IP address is blocked. | 拒绝访问时的返回信息。 |
|---|---|---|---|---|

```
ip_source_type: origin-source allow:
 - 10.0.0.1
 - 192.168.0.0/16
ip_source_type: header ip_header_name: x-real-iP deny:
 - 10.0.0.1
 - 192.169.X.X/16
```

##### WAF防护

waf插件实现了基于ModSecurity的规则防护引擎，可以根据用户配置的规则屏蔽可疑请求，并支持 OWASP CRS，为站点提供基础的防护功能。本文介绍如何配置waf插件。

**运行属性**

插件执行阶段：授权阶段插件执行优先级： `330` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| useCRS | bool | 选填 | false | 是否开启OWASP CRS，详情可参考coreruleset。 |
| secRules | array of string | 选填 | - | 用户自定义的waf防护规则，语法规则可参考ModSecurity中文手册。 |

**配置示例**

**观察模式**

```
useCRS: true secRules:
 - "SecRuleEngine DetectionOnly"
```

**移除特定规则**

例如开启观察模式后，发现有一个id为10的规则导致误拦截，可以单独移除这条规则。

```
useCRS: true secRules:
 - "SecRuleRemoveById 10"
 - "SecRuleEngine On"
```

**自定义防护规则**

```
useCRS: true secRules:
 - "SecDebugLogLevel 3"
 - "SecRuleEngine On"
 - "SecAction \"id:100,phase:1,pass\""
 - "SecRule REQUEST_URI \"@streq /admin\" \"id:101,phase:1,t:lowercase,deny\""
 - "SecRule REQUEST_BODY \"@rx maliciouspayload\" \"id:102,phase:2,t:lowercase,deny\""
```

根据该配置，以下请求将被禁止访问：

```bash
curl http://example.com/admin curl http://example.com -d "maliciouspayload"
```

##### 请求屏蔽

request-block插件实现了基于URL、请求头等特征屏蔽HTTP请求，可以用于防护部分站点资源不对外部暴露。本文介绍如何配置request-block插件。

**运行属性**

插件执行阶段：鉴权阶段插件执行优先级： `320` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| block urls _ | array of string | 选填， block urls _ , block exact _ urls , block _ _ regexp urls , _ block headers _ , block bodies _ 中至少必填一项。 | - | 配置用于匹配需要屏蔽URL的字符串。 |

| block urls _ |  |  |
|---|---|---|
|  | block _ |  |

|  |  | g |  |
|---|---|---|---|

|  | block headers _ |  |
|---|---|---|
|  | , |  |

| block exact urls _ _ | array of string | 选填， block urls _ , block exact _ urls , block _ _ regexp urls , _ block headers _ , block bodies _ 中至少必填一项。 | - | 配置用于匹配需要精确屏蔽URL的字符串。 |
|---|---|---|---|---|
| block regexp url _ _ s | array of string | 选填， block urls _ , block exact _ urls , block _ _ regexp urls , _ block headers _ , block bodies _ 中至少必填一项。 | - | 配置用于匹配需要屏蔽 URL 的正则表达式。 |
| block headers _ | array of string | 选填， block urls _ , block exact _ urls , block _ _ regexp urls , _ block headers _ , block bodies _ 中至少必填一项。 | - | 配置用于匹配需要屏蔽请求Header的字符串。 |
| block bodies _ | array of string | 选填， block urls _ , block exact _ urls , block _ _ regexp urls , _ block headers _ , block bodies _ 中至少必填一项。 | - | 配置用于匹配需要屏蔽请求Body的字符串。 |

| block urls _ |  |
|---|---|

|  |  | g |  |
|---|---|---|---|

|  | block headers _ |  |
|---|---|---|
|  | , |  |

| block urls _ |  |
|---|---|

|  |  | g |  |
|---|---|---|---|

|  | block headers _ |  |
|---|---|---|
|  | , |  |

| block urls _ |  |
|---|---|

|  | block headers _ |  |
|---|---|---|
|  | , |  |

| block urls _ |  |
|---|---|

|  |  | g |  |
|---|---|---|---|

|  | block headers _ |  |
|---|---|---|
|  | , |  |

| blocked code _ | number | 选填。 | 403 | 配置请求被屏蔽时返回的HTTP状态码。 |
|---|---|---|---|---|
| blocked message _ | string | 选填。 | - | 配置请求被屏蔽时返回的HTTP应答 Body。 |
| case sensitive _ | bool | 选填。 | true | 配置匹配时是否区分大小写，默认区分。 |

**配置示例**

**屏蔽请求url路径**

```
block_urls:
- swagger.html
- foo=bar
case_sensitive: false
```

根据该配置，下列请求将被禁止访问：

```bash
curl http://example.com?foo=Bar curl http://exmaple.com/Swagger.html
```

**屏蔽精确匹配的请求url路径**

```
block_exact_urls:
- /swagger.html?foo=bar
case_sensitive: false
```

根据该配置，下列请求将被禁止访问：

```bash
curl http://exmaple.com/Swagger.html?foo=Bar
```

**屏蔽正则匹配的请求url路径**

```
block_exact_urls:
- .*swagger.*
case_sensitive: false
```

根据该配置，下列请求将被禁止访问：

```bash
curl http://exmaple.com/Swagger.html?foo=Bar
```

**屏蔽请求header**

```
block_headers:
- example-key
- example-value
```

根据该配置，下列请求将被禁止访问：

```bash
curl http://example.com -H 'example-key: 123' curl http://exmaple.com -H 'my-header: example-value'
```

**屏蔽请求body**

```
block_bodies:
- "hello world"
case_sensitive: false
```

根据该配置，下列请求将被禁止访问：

```bash
curl http://example.com -d 'Hello World' curl http://exmaple.com -d 'hello world'
```

**请求Body大小限制**

| 配置了 block bodies 时，仅支 _ 且不存在匹配到的 block urls _ block bodies 时，若请求 Bo _ 413 Payload Too Large 。 | block bodies _ |  | 时，仅支 |
|---|---|---|---|
| 413 Payload Too Large |  |  |  |

##### 机器人拦截

bot-detect插件可以用于识别并阻止互联网爬虫对站点资源的爬取。本文介绍如何配置bot-detect插件。

**运行属性**

插件执行阶段：授权阶段插件执行优先级： `310` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| allow | array of string | 选填 | - | 配置匹配User- Agent请求头的正则表达式，匹配命中时将允许其访问。 |
| deny | array of string | 选填 | - | 配置匹配User- Agent请求头的正则表达式，匹配命中时将屏蔽请求。 |

| blocked code _ | number | 选填 | 403 | 配置请求被屏蔽时返回的HTTP 状态码。 |
|---|---|---|---|---|
| blocked message _ | string | 选填 | - | 配置请求被屏蔽时返回的HTTP 应答 Body。 |

`allow` 和 `deny` 字段可以均不配置，这种情况下将执行默认的爬虫判断逻辑，通过配置 `allow` 字段可以将原本命中默认爬虫判断逻辑的请求放行，通过配置 `deny` 字段可以增加额外的爬虫判断逻辑。 默认的爬虫判断正则表达式集合如下：

```bash
# Bots General matcher 'name/0.0'
 (?:\/[A-Za-z0-9\.]+|) {0,5}([A-Za-z0-9 \-_\!\[\]:]{0,50}(?:[Aa]rchiver|[Ii]ndexer|[Ss]
craper|[Bb]ot|[Ss]pider|[Cc]rawl[a-z]{0,50}))[/ ](\d+)(?:\.(\d+)(?:\.(\d+)|)|)
# Bots General matcher 'name 0.0'
 (?:\/[A-Za-z0-9\.]+|) {0,5}([A-Za-z0-9 \-_\!\[\]:]{0,50}(?:[Aa]rchiver|[Ii]ndexer|[Ss]
craper|[Bb]ot|[Ss]pider|[Cc]rawl[a-z]{0,50})) (\d+)(?:\.(\d+)(?:\.(\d+)|)|)
# Bots containing spider|scrape|bot(but not CUBOT)|Crawl
 ((?:[A-z0-9]{1,50}|[A-z\-]{1,50} ?|)(?: the |)(?:[Ss][Pp][Ii][Dd][Ee][Rr]|[Ss]crape|[C
c][Rr][Aa][Ww][Ll])[A-z0-9]{0,50})(?:(?:[ /]| v)(\d+)(?:\.(\d+)|)(?:\.(\d+)|)|)
# Bots Pattern '/name-0.0'
 /((?:Ant-)?Nutch|[A-z]+[Bb]ot|[A-z]+
[Ss]pider|Axtaris|fetchurl|Isara|ShopSalad|Tailsweep)[ \-](\d+)(?:\.(\d+)(?:\.(\d+))?)?
# Bots Pattern 'name/0.0'
\b(008|Altresium|Argus|BaiduMobaider|BoardReader|DNSGroup|DataparkSearch|EDI|Goodzer|Grub NGRID|Infohelfer|LinkedInBot|LOOQ|Nutch|OgScrper|PathDefender|Peew|PostPost|Steeler|Twitt bot|VSE|WebCrunch|WebZIP|Y!J-BR[A-Z]|YahooSeeker|envolk|sproose|wminer)/(\d+)(?:\.(\d+)
|)(?:\.(\d+)|)
# More bots
 (CSimpleSpider|Cityreview Robot|CrawlDaddy|CrawlFire|Finderbots|Index crawler|Job Robo
ter|KiwiStatus Spider|Lijit Crawler|QuerySeekerSpider|ScollSpider|
```

**配置示例**

**放行原本命中爬虫规则的请求**

```
allow:
- ".*Go-http-client.*"
```

若不作该配置，默认的 Golang 网络库请求会被视做爬虫，被禁止访问。

**增加爬虫判断**

```
deny:
- "spd-tools.*"
```

根据该配置，下列请求将被禁止访问：

```bash
curl http://example.com -H 'User-Agent: spd-tools/1.1' curl http://exmaple.com -H 'User-Agent: spd-tools'
```

#### 流量

##### 基于Key集群限流

cluster-key-rate-limit插件基于Redis实现集群限流，适用于需要跨多个云原生网关实例实现全局一致速率限制的场景。本文介绍如何配置cluster-key-rate-limit插件。

**功能说明**

`cluster-key-rate-limit` 插件基于Redis实现**集群级限流**，适用于需要跨多个云原生网关实例进行**全局**
**一致速率限制**的场景。
支持两种限流模式：
**规则级全局限流**：基于相同的 `rule_name` 和 `global_threshold` 配置，对自定义规则组设置全局
限流阈值。
**Key** **级动态限流**：根据请求中的动态 Key（如 URL 参数、请求头、客户端 IP、Consumer 名称或
Cookie 字段）进行分组限流。

**运行属性**

插件执行阶段：默认阶段插件执行优先级： `20` 。

**配置说明**

| 配置项 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| rule name _ | string | 是 | - | 限流规则名称，根据限流规则名称 + 限流类型 + 限流 key名称 + 限流 key对应的实际值来拼装Redis key。 |
| global threshold _ | Object | 否， global thr _ eshold 或 rul e items 选填一 _ 项。 | - | 对整个自定义规则组进行限流。 |
| rule items _ | array of object | 否， global thr _ eshold 或 rul e items 选填一 _ 项。 | - | 限流规则项数组，按顺序匹配， 命中第一个符合条件的规则项后触发限流，后续规则不再执行。 |

|  |  |  | global thr _ |  |  |
|---|---|---|---|---|---|
|  |  | eshold |  |  |  |
|  |  |  |  | rul |  |

|  |  |  | global thr _ |  |  |
|---|---|---|---|---|---|
| object |  | eshold |  |  |  |
|  |  |  |  | rul |  |

| show limit quota _ _ header _ | bool | 否 | false |  |  | 响应头中是否显示 X- |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | X- |  |
|  |  |  |  |  |  | RateLimit- |  |  |
|  |  |  |  |  |  | Limit |  |  |
| rejected code _ | int | 否 | 429 |  |  | 请求被限流时，返回的HTTP状态码。 |  |  |
| rejected msg _ | string | 否 | Too many requests |  |  | 请求被限流时，返回的响应体。 |  |  |
| redis | object | 是 | - |  |  | Redis相关配置。 |  |  |

|  |  |  | X- |  |
|---|---|---|---|---|
|  |  | RateLimit- |  |  |
|  |  | Remaining |  |  |

`global_threshold` 中每一项的配置字段说明：

| 配置项 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| query per secon _ _ d | int | 否， query per _ _ second 、 quer y per minute _ _ 、 query per ho _ _ ur 、 query pe _ r day 中选填一 _ 项。 | - | 允许每秒请求次数。 |
| query per minut _ _ e | int | 否， query per _ _ second 、 quer y per minute _ _ 、 query per ho _ _ ur 、 query pe _ r day 中选填一 _ 项。 | - | 允许每分钟请求次数。 |

|  |  |  |  |  |  | query per _ _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | second |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 、 | quer |  |  |
|  |  |  |  |  |  |  |  |  |  |  | - |
|  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  | ur |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 、 | query pe _ |  |  |  |  |

|  |  |  |  |  |  | query per _ _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | second |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 、 | quer |  |  |
|  |  |  |  |  |  |  |  |  |  |  | - |
|  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  | ur |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 、 | query pe _ |  |  |  |  |

| query per hour _ _ | int | 否， query per _ _ second 、 quer y per minute _ _ 、 query per ho _ _ ur 、 query pe _ r day 中选填一 _ 项。 | - | 允许每小时请求次数。 |
|---|---|---|---|---|
| query per day _ _ | int | 否， query per _ _ second 、 quer y per minute _ _ 、 query per ho _ _ ur 、 query pe _ r day 中选填一 _ 项。 | - | 允许每天请求次数。 |

|  |  |  |  |  |  | query per _ _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | second |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 、 | quer |  |  |
|  |  |  |  |  |  |  |  |  |  |  | - |
|  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  | ur |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 、 | query pe _ |  |  |  |  |

|  |  |  |  |  |  | query per _ _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | second |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 、 | quer |  |  |
|  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  | ur |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 、 | query pe _ |  |  |  |  |

`rule_items` 中每一项的配置字段说明：

| 配置项 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| limit by header _ _ | string | 否， limit by * _ _ 中选填一项。 | - | 配置获取限流键值的来源HTTP 请求头名称。 |
| limit by param _ _ | string | 否， limit by * _ _ 中选填一项。 | - | 配置获取限流键值的来源URL参数名称。 |
| limit by consume _ _ r | string | 否， limit by * _ _ 中选填一项。 | - | 根据 consumer 名称进行限流，无需添加实际值。 |
| limit by cookie _ _ | string | 否， limit by * _ _ 中选填一项。 | - | 配置获取限流键值的来源Cookie中 key的名称。 |
| limit by per hea _ _ _ der | string | 否， limit by * _ _ 中选填一项。 | - | 按规则匹配特定 HTTP 请求头，并对每个请求头分别计算限流，配置获取限流键值的来源 HTTP 请求头名称， 配置 limit keys _ 时支持正则表达式或 * 。 |

| limit by per para _ _ _ m | string | 否， limit by * _ _ 中选填一项。 |  | - |  |  | 按规则匹配特定 URL 参数，并对每个参数分别计算限流，配置获取限流键值的来源 URL 参数名称，配置 limit keys _ 时支持正则表达式或 * 。 |  |  |
|---|---|---|---|---|---|---|---|---|---|
| limit by per cons _ _ _ umer | string | 否， limit by * _ _ 中选填一项。 |  | - |  |  | 按规则匹配特定 consumer，并对每个 consumer 分别计算限流，根据 consumer 名称进行限流，无需添加实际值，配置 limit keys _ 时支持正则表达式或 * 。 |  |  |
| limit by per cook _ _ _ ie | string | 否， limit by * _ _ 中选填一项。 |  | - |  |  | 按规则匹配特定 Cookie，并对每个 Cookie 分别计算限流，配置获取限流键值的来源 Cookie 中 key的名称，配置 limit keys _ 时支持正则表达式或 * 。 |  |  |
| limit by per ip _ _ _ | string | 否， limit by * _ _ 中选填一项。 |  | - |  |  | 按规则匹配特定 IP，并对每个 IP 分别计算限流，配置获取限流键值的来源IP参数名称，从请求头获取 from- header- 对应的 header名，示例： from- |  |  |
|  |  |  |  |  |  |  |  | from- |  |
|  |  |  |  |  |  |  | header-x- |  |  |
|  |  |  |  |  |  |  | forwarded- |  |  |
|  |  |  |  |  |  |  | for |  |  |
| limit keys _ | array of object | 是 |  | - |  |  | 配置匹配键值后的限流次数。 |  |  |

|  |  | from- |
|---|---|---|
|  | header- |  |

|  |  | from- |  |
|---|---|---|---|
|  | remote-addr |  |  |

`limit_keys` 中每一项的配置字段说明：

| 配置项 | 类型 | 必填 | 默认值 |  |  |  |  |  | 说明 |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| key | string | 是 | - |  |  |  |  |  | 匹配的键值， limit by p _ _ er header 、 l _ |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | limit by p _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | er header _ |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 、 | l |  |  |
|  |  |  |  |  |  |  |  |  | am |  | 、 | limit by _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | cookie _ |  |  |  |  |  |  |  |
| query per secon _ _ d | int | 否， query per _ _ second 、 quer y per minute _ _ 、 query per ho _ _ ur 、 query pe _ r day 中选填一 _ 项。 | - |  |  |  |  |  | 允许每秒请求次数。 |  |  |  |  |  |  |  |
| query per minut _ _ e | int | 否， query per _ _ second 、 quer y per minute _ _ 、 query per ho _ _ ur 、 query pe _ r day 中选填一 _ 项。 | - |  |  |  |  |  | 允许每分钟请求次数。 |  |  |  |  |  |  |  |
| query per hour _ _ | int | 否， query per _ _ second 、 quer y per minute _ _ 、 query per ho _ _ ur 、 query pe _ r day 中选填一 _ 项。 | - |  |  |  |  |  | 允许每小时请求次数。 |  |  |  |  |  |  |  |

| regexp:^d. |  |
|---|---|

|  | * |
|---|---|

|  |  | limit by _ |  |
|---|---|---|---|
|  | per ip _ _ |  |  |

|  |  |  |  |  |  | query per _ _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | second |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 、 | quer |  |  |
|  |  |  |  |  |  |  |  |  |  |  | - |
|  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  | ur |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 、 | query pe _ |  |  |  |  |

|  |  |  |  |  |  | query per _ _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | second |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 、 | quer |  |  |
|  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  | ur |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 、 | query pe _ |  |  |  |  |

|  |  |  |  |  |  | query per _ _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | second |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 、 | quer |  |  |
|  |  |  |  |  |  |  |  |  |  |  | - |
|  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  | ur |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 、 | query pe _ |  |  |  |  |

| query per day _ _ | int | 否， query per _ _ second 、 quer y per minute _ _ 、 query per ho _ _ ur 、 query pe _ r day 中选填一 _ 项。 | - | 允许每天请求次数。 |
|---|---|---|---|---|

|  |  |  |  |  |  | query per _ _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | second |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 、 | quer |  |  |
|  |  |  |  |  |  |  |  |  |  |  | - |
|  |  |  |  | 、 |  |  |  |  |  |  |  |
|  |  |  |  | ur |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 、 | query pe _ |  |  |  |  |

`redis` 中每一项的配置字段说明：

| 配置项 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| service name _ | string | 必填 | - | Redis 服务名称， 带服务类型的完整 FQDN 名称，例如 my-redis.dns、 redis.my- ns.svc.cluster.loc al。 |
| service port _ | int | 否 | 服务类型为固定地址（static service）默认值为 80，其他为6379。 | 输入Redis服务的服务端口。 |
| username | string | 否 | - | Redis用户名。 |
| password | string | 否 | - | Redis密码。 |
| timeout | int | 否 | 1000 | Redis连接超时时间，单位毫秒。 |
| database | int | 否 | 0 | 使用的数据库ID， 例如配置为1，对应 SELECT 1 。 |

**配置示例**

**自定义规则组全局限流**

```
rule_name: routeA-global-limit-rule global_threshold:
```

`query_per_minute: 1000 #` 自定义规则组限`1000`次请求/分钟

```
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**识别请求参数 apikey，进行区别限流**

```
rule_name: routeA-request-param-limit-rule rule_items:
 - limit_by_param: apikey
 limit_keys:
 - key: 9a342114-ba8a-11ec-b1bf-00163e1250b5
 query_per_minute: 10
 - key: a6a6d7f2-ba8a-11ec-bec2-00163e1250b5
 query_per_hour: 100
 - limit_by_per_param: apikey
 limit_keys:
```

# 正则匹配a开头的`apikey`，每个匹配项独立限`10`次/秒

```
 - key: "regexp:^a.*"
 query_per_second: 10
```

# 正则匹配b开头的`apikey`，每个匹配项独立限`100`次/分钟

```
 - key: "regexp:^b.*"
 query_per_minute: 100
```

# 兜底规则：通配所有`apikey`，每个独立限`1000`次/小时

```
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**识别请求头 x-ca-key，进行区别限流**

```
rule_name: routeA-request-header-limit-rule rule_items:
 - limit_by_header: x-ca-key
 limit_keys:
 - key: 102234
 query_per_minute: 10
 - key: 308239
 query_per_hour: 10
 - limit_by_per_header: x-ca-key
 limit_keys:
```

# 正则匹配a开头的`apikey`，每个匹配项独立限`10`次/秒

```
 - key: "regexp:^a.*"
 query_per_second: 10
```

# 正则匹配b开头的`apikey`，每个匹配项独立限`100`次/分钟

```
 - key: "regexp:^b.*"
 query_per_minute: 100
```

# 兜底规则：通配所有`apikey`，每个独立限`1000`次/小时

```
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**根据请求头x-forwarded-for获取对端IP，进行区别限流**

```
rule_name: routeA-client-ip-limit-rule rule_items:
 - limit_by_per_ip: from-header-x-forwarded-for # 基于x-forwarded-for头的IP限流
 limit_keys:
```

# 精确`IP`：`1.1.X.X`，限`10`次/天

```
 - key: 1.1.X.X
 query_per_day: 10
```

# IP段`1.1.1.0/24`：每个`IP`独立限`100`次/天

```
 - key: 1.1.1.0/24
 query_per_day: 100
```

# 兜底规则：所有`IP`，每个独立限`1000`次/天

```
 - key: 0.0.0.0/0
 query_per_day: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**识别consumer，进行区别限流**

```
rule_name: routeA-consumer-limit-rule rule_items:
 - limit_by_consumer: ''
 limit_keys:
 - key: consumer1
 query_per_second: 10
 - key: consumer2
 query_per_hour: 100
 - limit_by_per_consumer: ''
 limit_keys:
```

# 正则匹配a开头的`consumer`，每个匹配项独立限`10`次/秒

```
 - key: "regexp:^a.*"
 query_per_second: 10
```

# 正则匹配b开头的`consumer`，每个匹配项独立限`100`次/分钟

```
 - key: "regexp:^b.*"
 query_per_minute: 100
```

# 兜底规则：通配所有`apikey`，每个独立限`1000`次/小时

```
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**识别Cookie中的键值对，进行区别限流**

```
rule_name: routeA-cookie-limit-rule rule_items:
 - limit_by_cookie: key1 # 基于Cookie键key1限流
 limit_keys:
```

# 固定值`value1`：限`10`次/分钟

```
 - key: value1
 query_per_minute: 10
```

# 固定值`value2`：限`100`次/小时

```
 - key: value2
 query_per_hour: 100
```

  - `- limit_by_per_cookie: key1 #` 基于`Cookie`键`key1`的每个值独立限流

```
 limit_keys:
```

# 正则匹配a开头的`value`，每个独立限`10`次/秒

```
 - key: "regexp:^a.*"
 query_per_second: 10
```

# 正则匹配b开头的`value`，每个独立限`100`次/分钟

```
 - key: "regexp:^b.*"
 query_per_minute: 100
```

# 兜底规则：所有`value`，每个独立限`1000`次/小时

```
 - key: "*"
 query_per_hour: 1000
rejected_code: 200 rejected_msg: '{"code":-1,"msg":"Too many requests"}' redis:
 service_name: redis.static
show_limit_quota_header: true
```

##### 基于Key限流

key-rate-limit插件实现了基于特定键值实现限流的能力，键值来源可以是URL参数、HTTP请求头。本文介绍如何配置key-rate-limit插件。

**运行属性**

插件执行阶段：默认阶段插件执行优先级： `10` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| limit by header _ _ | string | 选填， limit by h _ _ eader , limit _ by param 中选 _ 填一项。 | - | 配置获取限流键值的来源HTTP请求头名称。 |

|  |  |  | limit by h _ _ |  |
|---|---|---|---|---|
|  |  | eader |  |  |

| limit by param _ _ | string | 选填， limit by h _ _ eader , limit _ by param 中选 _ 填一项。 | - | 配置获取限流键值的来源URL参数名称。 |
|---|---|---|---|---|
| limit keys _ | array of object | 必填。 | - | 配置匹配键值后的限流次数。 |

|  |  |  | limit by h _ _ |  |  |
|---|---|---|---|---|---|
|  |  |  |  | limit _ |  |
|  |  | by param _ |  |  |  |

`limit_keys` 中每一项的配置字段说明：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| key | string | 必填。 | - | 匹配的键值。 |
| query per secon _ _ d | number | 选填， query per _ _ second , query per minute , _ _ query per hour _ _ , query per d _ _ ay 中选填一项。 | - | 允许每秒请求次数。 |
| query per minut _ _ e | number | 选填， query per _ _ second , query per minute , _ _ query per hour _ _ , query per d _ _ ay 中选填一项。 | - | 允许每分钟请求次数。 |
| query per hour _ _ | number | 选填， query per _ _ second , query per minute , _ _ query per hour _ _ , query per d _ _ ay 中选填一项。 | - | 允许每小时请求次数。 |
| query per day _ _ | number | 选填， query per _ _ second , query per minute , _ _ query per hour _ _ , query per d _ _ ay 中选填一项。 | - | 允许每天请求次数。 |

|  |  |  | query per _ _ |  |
|---|---|---|---|---|
|  |  | second |  |  |

|  |  | query per hour _ _ |
|---|---|---|
|  |  | ay |

|  |  |  | query per _ _ |  |
|---|---|---|---|---|
|  |  | second |  |  |

|  |  | query per hour _ _ |
|---|---|---|
|  |  | ay |

|  |  |  | query per _ _ |  |
|---|---|---|---|---|
|  |  | second |  |  |

|  |  | query per hour _ _ |
|---|---|---|
|  |  | ay |

|  |  |  | query per _ _ |  |
|---|---|---|---|---|
|  |  | second |  |  |

|  |  | query per hour _ _ |
|---|---|---|
|  |  | ay |

**配置示例**

**识别请求参数 apikey，进行区别限流**

```
limit_by_param: apikey limit_keys:
- key: 9a342114-ba8a-11ec-b1bf-00163e1250b5
 query_per_second: 10
- key: a6a6d7f2-ba8a-11ec-bec2-00163e1250b5
 query_per_minute: 100
```

**识别请求头 x-ca-key，进行区别限流**

```
limit_by_header: x-ca-key limit_keys:
- key: 102234
 query_per_second: 10
- key: 308239
 query_per_hour: 10
```

##### 流量染色

traffic-tag插件允许根据权重或特定请求内容通过添加特定请求头的方式对请求流量进行染色。它支持复杂的逻辑来确定如何根据用户定义的标准染色流量。本文介绍如何配置traffic-tag插件。

**运行属性**

插件执行阶段：默认阶段插件执行优先级： `400` 。

**配置字段**

此部分提供了配置字段的详细描述。

|  | 字段名称 |  | 类型 | 默认值 | 是否必填 | 描述 |
|---|---|---|---|---|---|---|
|  | conditionGroup s |  | array of object | - | 否 | 定义基于内容的标记条件组，详细结构见条件组配置。 |
|  |  | conditionGroup |  |  |  |  |
|  | s |  |  |  |  |  |
|  | weightGroups |  | array of object | - | 否 | 定义基于权重的标记条件组，详细结构见权重组配置。 |
|  | defaultTagKey |  | string | - | 否 | 默认的标记键名， 当未匹配到任何条件时使用。当且仅当同时配置了defaultTagVal 时生效。 |

|  |  | weightGroups |
|---|---|---|

|  |  | defaultTagKey |
|---|---|---|

| defaultTagVal | string | - | 否 | 默认的标记值，当未匹配到任何条件时使用。当且仅当同时配置了defaultTagKe y时生效。 |
|---|---|---|---|---|

|  |  | defaultTagVal |
|---|---|---|

**条件组配置**

`conditionGroups` 中每一项的配置字段说明如下：

| 字段名称 | 类型 | 默认值 | 是否必填 | 描述 |
|---|---|---|---|---|
| headerName | string | - | 是 | 要添加或修改的 HTTP 头名称。 |
| headerValue | string | - | 是 | HTTP 头的值。 |
| logic | string | - | 是 | 条件组中的逻辑关系，支持 and 、 or ，必须为小写字母。 |
| conditions | array of object | - | 是 | 描述具体的标记条件，详细结构参见下方的 conditions 配置字段说明。 |

`conditions` 中每一项的配置字段说明如下：

|  | 字段名称 |  | 类型 | 默认值 | 是否必填 | 描述 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | conditionType |  | string | - | 是 | 条件类型，支持 header 、 parameter 、 c ookie 。 |  |  |  |
|  |  | conditionType |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | c |  |  |
|  | key |  | string | - | 是 | 条件的关键字。 |  |  |  |

|  | parameter |
|---|---|
|  | ookie |

| operator | string | - | 是 |  |  |  | 操作符，支持 equal 、 n ot equal 、 pr _ |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  | n |  |
|  |  |  |  |  |  |  | efix |  | 、 |  | in | 、 |  |
|  |  |  |  |  |  |  | gex |  |  | percent |  |  |  |
|  |  |  |  |  |  |  | age |  |  |  |  |  |  |
| value | array of string | - | 是 |  |  |  | 条件的值，仅当操作符为 in 和 not in 时支持配置 _ 多个值。 |  |  |  |  |  |  |

|  |  | in |
|---|---|---|
|  | in _ |  |

| not |  |
|---|---|

**说明**

当operator为regex时，使用的正则表达式引擎是RE2。详情请参阅RE2 官方文档。

**权重组配置**

`weightGroups` 中每一项的配置字段说明如下：

| 字段名称 | 类型 | 默认值 | 是否必填 | 描述 |
|---|---|---|---|---|
| headerName | string | - | 是 | 要添加或修改的 HTTP头名称。 |
| headerValue | string | - | 是 | HTTP头的值。 |
| weight | integer | - | 是 | 流量权重百分比。 |

**操作符说明**

| 操作符 | 描述 |
|---|---|
| equal | 精确匹配，值需要完全相等。 |
| not equal _ | 不等匹配，值不相等时满足条件。 |
| prefix | 前缀匹配，指定值是实际值的前缀时满足条件。 |
| in | 包含匹配，实际值需要在指定的列表中。 |

| not in _ | 排除匹配，实际值不在指定的列表中时满足条件。 |  |  |
|---|---|---|---|
| regex | 正则表达式匹配，按照正则表达式规则匹配。 |  |  |
| percentage | 百分比匹配，原理： hash(get(key)) % 100 < value 成立时满足条件。 |  |  |
|  |  | hash(get(key)) % 100 < |  |

|  | value |
|---|---|

**重要**

关于percentage和weight的区别：在使用percentage进行条件匹配时，将判断每个请求是否满足特定百分比条件；而weight则是静态随机分配整体流量的比例。

**配置示例**

**例1: 基于内容的匹配**

| 请求头 role 的值是 user 、 viewer 被添加请求头 x-mse-tag: gray 。由于配 defaultTagVal ，当未匹配到任何条件时 | role |  | 的值是 | user | 、 | viewer |
|---|---|---|---|---|---|---|
| defaultTagVal |  |  |  |  |  |  |

| 数了 | foo=bar |  | 的请求 |
|---|---|---|---|
| base |  |  |  |
|  |  | 。 |  |

```
defaultTagKey: x-mse-tag defaultTagVal: base conditionGroups:
 - headerName: x-mse-tag
 headerValue: gray
 logic: and
 conditions:
 - conditionType: header
 key: role
 operator: in
 value:
 - user
 - viewer
 - editor
 - conditionType: parameter
 key: foo
 operator: equal
 value:
 - bar
```

**例子2: 基于权重的匹配**

按照下列配置，请求将有30%几率被添加请求头 `x-mse-tag: gray` ，30%几率被添加请求头 `x-mse-` `tag: blue` ，40%几率不添加请求头。
# 权重总和为`100`，下例中未配置的`40`权重将不添加`header`

```
weightGroups:
 - headerName: x-mse-tag
 headerValue: gray
 weight: 30
 - headerName: x-mse-tag
 headerValue: blue
 weight: 30
```

##### 请求校验

request-validation插件用于提前验证向上游服务转发的请求。该插件使用 `JSON Schema` 机制进行数据验证，可以验证请求的body及header数据。本文介绍如何配置request-validation插件。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `220` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| header schema _ | object | 选填 | - | 配置用于验证请求 header的JSON Schema。 |
| body schema _ | object | 选填 | - | 配置用于验证请求 body的JSON Schema。 |
| rejected code _ | number | 选填 | 403 | 配置请求被拒绝时返回的HTTP状态码。 |
| rejected msg _ | string | 选填 | - | 配置请求被拒绝时返回的HTTP应答 Body。 |
| enable swagger _ | bool | 选填 | false | 配置是否开启 swagger文档验证。 |
| enable oas3 _ | bool | 选填 | false | 配置是否开启OAS3 文档验证。 |

**重要**

校验规则对header和body是一样的。

**配置示例**

**枚举（Enum）验证**

```
body_schema:
 type: object
 required:
 - enum_payload
 properties:
 enum_payload:
 type: string
 enum:
 - "enum_string_1"
 - "enum_string_2"
 default: "enum_string_1"
```

**布尔（Boolean）验证**

```
body_schema:
 type: object
 required:
 - boolean_payload
 properties:
 boolean_payload:
 type: boolean
 default: true
```

**数字范围（Number or Integer）验证**

```
body_schema:
 type: object
 required:
 - integer_payload
 properties:
 integer_payload:
 type: integer
 minimum: 1
 maximum: 10
```

**字符串长度（String）验证**

```
body_schema:
 type: object
 required:
 - string_payload
 properties:
 string_payload:
 type: string
 minLength: 1
 maxLength: 10
```

**正则表达式（Regex）验证**

```
body_schema:
 type: object
 required:
 - regex_payload
 properties:
 regex_payload:
 type: string
 minLength: 1
 maxLength: 10
 pattern: "^[a-zA-Z0-9_]+$"
```

**数组（Array）验证**

```
body_schema:
 type: object
 required:
 - array_payload
 properties:
 array_payload:
 type: array
 minItems: 1
 items:
 type: integer
 minimum: 1
 maximum: 10
 uniqueItems: true
 default: [1, 2, 3]
```

**多字段组合（Combined）验证**

```
body_schema:
 type: object
 required:
 - boolean_payload
 - array_payload
 - regex_payload
 properties:
 boolean_payload:
 type: boolean
 array_payload:
 type: array
 minItems: 1
 items:
 type: integer
 minimum: 1
 maximum: 10
 uniqueItems: true
 default: [1, 2, 3]
 regex_payload:
 type: string
 minLength: 1
 maxLength: 10
 pattern: "^[a-zA-Z0-9_]+$"
```

**自定义拒绝信息**

```
body_schema:
 type: object
 required:
 - boolean_payload
 properties:
 boolean_payload:
 type: boolean
rejected_code: 403
```

`rejected_msg: "`请求被拒绝"

#### 转换

##### 请求/响应转换

transformer插件可以对请求/响应头、请求查询参数、请求/响应体参数进行转换，支持的转换操作类型包括删除、重命名、更新、添加、追加、映射、去重。本文介绍如何配置transformer插件。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `410` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|

| reqRules | string | 选填，reqRules和 respRules至少填一个。 | - | 请求转换器配置， 指定转换操作类型以及请求头、请求查询参数、请求体的转换规则。 |
|---|---|---|---|---|
| respRules | string | 选填，reqRules和 respRules至少填一个。 | - | 响应转换器配置， 指定转换操作类型以及响应头、响应体的转换规则。 |

`reqRules` 和 `respRules` 中每一项的配置字段说明如下：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| operate | string | 必填，可选值为 remove , r ename , repla ce , add , a ppend , map , dedupe 。 | - | 指定转换操作类型，支持的操作类型有删除 （remove）、重命名（rename）、更新（replace）、添加（add）、追加 （append）、映射 （map）、去重 （dedupe），当存在多项不同类型的转换规则时，按照上述操作类型顺序依次执行。 |
| mapSource | string | 选填，可选值为 headers , querys , body 。 | - | 仅在operate 为 map 时有效。 指定映射来源，若不填该字段，则默认映射来源为自身。 |
| headers | array of object | 选填。 | - | 指定请求/响应头转换规则。 |
| querys | array of object | 选填。 | - | 指定请求查询参数转换规则。 |

|  |  | ename |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | , |  |  |  |  |
|  |  | ce |  | , |  |  |  | , | a |  |
|  |  |  |  |  |  |  | map |  |  |  |
|  |  |  |  |  |  | , |  |  |  |  |

|  | headers |
|---|---|
| querys |  |

|  | - |
|---|---|

| body | array of object | 选填。 |  |  |  |  | 指定请求/响应体参数转换规则，请求体转换允许 content-type 为 application /json , appli |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | /json |  |  |  |  |  |
|  |  |  |  |  |  |  |  | , | appli |  |  |  |
|  |  |  |  | - |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | form- |  |  |  |  |  |
|  |  |  |  |  |  |  | urlencoded |  |  | , |  |  |

|  | data |
|---|---|

|  | /json |
|---|---|

`headers` , `querys` , `body` 中每一项的配置字段说明如下：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| key | string | 选填。 | - | 在operate 为 remove 时使用，用法详见转换操作类型。 |
| oldKey | string | 选填。 | - | 在operate 为 rename 时使用，用法详见转换操作类型。 |
| newKey | string | 选填。 | - | 在operate 为 rename 时使用，用法详见转换操作类型。 |
| key | string | 选填。 | - | 在operate 为 replace 时使用，用法详见转换操作类型。 |
| newValue | string | 选填。 | - | 在operate 为 replace 时使用，用法详见转换操作类型。 |
| key | string | 选填。 | - | 在operate 为 add 时使用， 用法详见转换操作类型。 |

| value | string |  |  | 选填。 |  |  |  |  |  |  |  | - |  |  |  | 在operate 为 add 时使用， 用法详见转换操作类型。 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| key | string |  |  | 选填。 |  |  |  |  |  |  |  | - |  |  |  | 在operate 为 append 时使用，用法详见转换操作类型。 |  |  |
| appendValue | string |  |  | 选填。 |  |  |  |  |  |  |  | - |  |  |  | 在operate 为 append 时使用，用法详见转换操作类型。 |  |  |
| fromKey | string |  |  | 选填。 |  |  |  |  |  |  |  | - |  |  |  | 在operate 为 map 时使用， 用法详见转换操作类型。 |  |  |
| toKey | string |  |  | 选填。 |  |  |  |  |  |  |  | - |  |  |  | 在operate 为 map 时使用， 用法详见转换操作类型。 |  |  |
| key | string |  |  | 选填。 |  |  |  |  |  |  |  | - |  |  |  | 在operate 为 dedupe 时使用，用法详见转换操作类型。 |  |  |
| strategy | string |  |  | 选填。 |  |  |  |  |  |  |  | - |  |  |  | 在operate 为 dedupe 时使用，用法详见转换操作类型。 |  |  |
| value type _ | string |  |  | 选填，可选值为 object , b oolean , numb er , string 。 |  |  |  |  |  |  |  |  |  |  |  | 当 content- |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | content- |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | type: |  |  |
|  |  |  |  |  | object |  |  |  |  | b |  |  |  |  |  |  |  |  |
|  |  |  |  | oolean |  |  |  |  |  |  |  |  |  |  |  | application/jso |  |  |
|  |  |  |  |  |  |  |  | , |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | n |  | numb |  |  |  |  | ng |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | n |  |  |
|  |  |  |  | er |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| host pattern _ | string |  |  | 选填。 |  |  |  |  |  |  |  | - |  |  |  | 指定请求主机名匹配规则，当转换操作类型为 replace , add , append 时有效。 |  |  |

|  |  | add |
|---|---|---|

| path pattern _ | string | 选填。 | - | 指定请求路径匹配规则，当转换操作类型为 replace , add , append 时有效。 |
|---|---|---|---|---|

|  |  | add |  |
|---|---|---|---|

注意： `request transformer` 支持以下转换对象：请求头部、请求查询参数、请求体（application/json, application/x-www-form-urlencoded, multipart/form-data）。 `response transformer` 支持以下转换对象：响应头部、响应体（application/json）。 插件支持双向转换能力，即单个插件能够完成对请求和响应都做转换。 转换操作类型的执行顺序，为配置文件中编写的顺序，如：remove → rename → replace → add → append → map → dedupe或者dedupe → map → append → add → replace → rename → remove等。

| ， | value |  |  | 也不区 |
|---|---|---|---|---|
| key |  |  |  |  |
|  |  | , |  |  |

`value_type` 仅对content-type为application/json的请求/响应体有效。

| 对 | replace | , | add |  |
|---|---|---|---|---|
|  |  |  |  | 生效 |

而 `path_pattern` 失效。

**转换操作类型**

| 操作类型 | key 字段含义 | value 字段含义 | 描述 |
|---|---|---|---|
| 删除 remove | 目标key | 无需设置 | 若存在指定的 key ， 则删除；否则无操作。 |
| 重命名 rename | 目标oldKey | 新的key名称 | 若存在指定的 oldKey:value ， 则将其键名重命名为 newKey ，得到 newKey:value ； 否则无操作。 |
| 更新 replace | 目标key | 新的value值 | 若存在指定的 key:value ，则将其 value 更新为 newValue ，得到 key:newValue ； 否则无操作。 |

| 添加 add | 添加的key | 添加的value |  | 若不存在指定的 key:value ，则添加；否则无操作。 |  |  |
|---|---|---|---|---|---|---|
| 追加 append | 目标key | 追加的value值 |  | 若存在指定的 key:value ，则追加 appendValue 得到 key:[value..., appendValue] ；否则相当于执行 add 操作，得到 key:appendValue 。 |  |  |
|  |  |  |  |  | key:[value..., |  |
|  |  |  |  | appendValue] |  |  |
| 映射 map | 映射来源 fromKey | 映射目标toKey |  | 若存在指定的 fromKey:fromValu e ，则将其值 fromValue 映射给 toKey 的值，得到 toKey:fromValue ，同时保留 fromKey:fromValu e 。 说明若 toKey 已存在， 则其值会被覆盖；否则无操作。 |  |  |

| fromKey:fromValu |  |
|---|---|

|  | e |
|---|---|

| fromKey:fromValu |  |
|---|---|

|  | e |
|---|---|

| 去重 dedupe | 目标key | 指定去重策略 strategy |  | strategy 可选值为： RETAIN UNIQUE : _ 按顺序保留所有唯一值，如 k1: |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | k1: |  |
|  |  |  |  | [v1,v2,v3,v3,v2,v1 |  |  |  |
|  |  |  |  | ] |  |  |  |
|  |  |  |  |  | k1: |  |  |
|  |  |  |  | 到 |  |  |  |

|  | k1: |  |
|---|---|---|
| [v1,v2,v3] |  |  |

|  | k1: |  |
|---|---|---|
| [v1,v2,v3] |  |  |

|  | [v1] |
|---|---|

**配置示例**

**实现基于Body参数路由**

配置示例：

```
reqRules:
- operate: map
 headers:
 - fromKey: userId
 toKey: x-user-id
 mapSource: body
```

此规则将请求body中的 `userId` 解析出后，设置到请求Header `x-user-id` 中，这样即可基于云原生网关请求Header匹配路由的能力，实现基于Body参数的路由。 此配置同时支持 `application/json` 和 `application/x-www-form-urlencoded` 两种类型的请求 Body。 举例来说：

**对于application/json类型的body**

```bash
curl localhost -d '{"userId":12, "userName":"johnlanni"}' -H 'contenttype:application/json'
```

将从json中提取出 `userId` 字段的值，设置到 `x-user-id` 中，后端服务收到的请求头将增加: `x-usr-`

```
id: 12 。
```

因为在插件新增这个Header后，网关将重新计算路由，所以可以实现网关路由配置根据这个请求头来匹配路由到特定的目标服务。

**对于application/x-www-form-urlencoded类型的body**

```bash
curl localhost -d 'userId=12&userName=johnlanni'
```

| k1=v1&k2=v2 | 这样的表单格式 |
|---|---|
| 请求头将增加: |  |

因为在插件新增这个Header后，网关将重新计算路由，所以可以实现网关路由配置根据这个请求头来匹配路由到特定的目标服务。

**json path 支持**

可以根据GJSON Path 语法，从复杂的 json 中提取出字段。 比较常用的操作举例，对于以下 json:

```json
{
 "name": {"first": "Tom", "last": "Anderson"},
 "age":37,
 "children": ["Sara","Alex","Jack"],
 "fav.movie": "Deer Hunter",
 "friends": [
 {"first": "Dale", "last": "Murphy", "age": 44, "nets": ["ig", "fb", "tw"]},
 {"first": "Roger", "last": "Craig", "age": 68, "nets": ["fb", "tw"]},
 {"first": "Jane", "last": "Murphy", "age": 47, "nets": ["ig", "tw"]}
```

]

```
}
```

可以实现这样的提取:

```
name.last "Anderson" name.first "Tom" age 37 children ["Sara","Alex","Jack"] children.0 "Sara" children.1 "Alex" friends.1 {"first": "Roger", "last": "Craig", "age": 68} friends.1.first "Roger"
```

现在如果想从上面这个 json 格式的 body 中提取出 friends 中第二项的 first 字段，来设置到 Header `x-first-name` 中，同时抽取 last 字段，来设置到 Header `x-last-name` 中，则可以使用这份插件配置:

```
reqRules:
- operate: map
 headers:
 - fromKey: friends.1.first
 toKey: x-first-name
 - fromKey: friends.1.last
 toKey: x-last-name
 mapSource: body
```

**Request Transformer**

**转换请求头部**

```
reqRules:
- operate: remove
 headers:
 - key: X-remove
- operate: rename
 headers:
 - oldKey: X-not-renamed
 newKey: X-renamed
- operate: replace
 headers:
 - key: X-replace
 newValue: replaced
- operate: add
 headers:
 - key: X-add-append
 value: host-$1
 host_pattern: ^(.*)\.com$
- operate: append
 headers:
 - key: X-add-append
 appendValue: path-$1
 path_pattern: ^.*?\/(\w+)[\?]{0,1}.*$
- operate: map
 headers:
 - fromKey: X-add-append
 toKey: X-map
- operate: dedupe
 headers:
 - key: X-dedupe-first
 strategy: RETAIN_FIRST
 - key: X-dedupe-last
 strategy: RETAIN_LAST
 - key: X-dedupe-unique
 strategy: RETAIN_UNIQUE
```

发送请求：

```bash
$ curl -v console.higress.io/get -H 'host: foo.bar.com' \ -H 'X-remove: exist' -H 'X-not-renamed:test' -H 'X-replace:not-replaced' \ -H 'X-dedupe-first:1' -H 'X-dedupe-first:2' -H 'X-dedupe-first:3' \ -H 'X-dedupe-last:a' -H 'X-dedupe-last:b' -H 'X-dedupe-last:c' \ -H 'X-dedupe-unique:1' -H 'X-dedupe-unique:2' -H 'X-dedupe-unique:3' \ -H 'X-dedupe-unique:3' -H 'X-dedupe-unique:2' -H 'X-dedupe-unique:1'
```

# httpbin 响应结果

```json
{
 "args": {},
 "headers": {
 ...
 "X-Add-Append": "host-foo.bar,path-get",
 ...
 "X-Dedupe-First": "1",
 "X-Dedupe-Last": "c",
 "X-Dedupe-Unique": "1,2,3",
 ...
 "X-Map": "host-foo.bar,path-get",
 "X-Renamed": "test",
 "X-Replace": "replaced"
 },
 ...
}
```

**转换请求查询参数**

```
reqRules:
- operate: remove
 querys:
 - key: k1
- operate: rename
 querys:
 - oldKey: k2
 newKey: k2-new
- operate: replace
 querys:
 - key: k2-new
 newValue: v2-new
- operate: add
 querys:
 - key: k3
 value: v31-$1
 path_pattern: ^.*?\/(\w+)[\?]{0,1}.*$
- operate: append
 querys:
 - key: k3
 appendValue: v32
- operate: map
 querys:
 - fromKey: k3
 toKey: k4
- operate: dedupe
 querys:
 - key: k4
 strategy: RETAIN_FIRST
```

发送请求：

```bash
$ curl -v "console.higress.io/get?k1=v11&k1=v12&k2=v2"
```

# httpbin 响应结果

```json
{
 "args": {
 "k2-new": "v2-new",
 "k3": [
 "v31-get",
 "v32"
```

`],`

```json
 "k4": "v31-get"
 },
 ...
 "url": "http://foo.bar.com/get?k2-new=v2-new&k3=v31-get&k3=v32&k4=v31-get"
}
```

**转换请求体**

```
reqRules:
- operate: remove
 body:
 - key: a1
- operate: rename
 body:
 - oldKey: a2
 newKey: a2-new
- operate: replace
 body:
 - key: a3
 newValue: t3-new
 value_type: string
- operate: add
 body:
 - key: a1-new
 value: t1-new
 value_type: string
- operate: append
 body:
 - key: a1-new
 appendValue: t1-$1-append
 value_type: string
 host_pattern: ^(.*)\.com$
- operate: map
 body:
 - fromKey: a1-new
 toKey: a4
- operate: dedupe
 body:
 - key: a4
 strategy: RETAIN_FIRST
```

发送请求：

**Content-Type: application/json**

```bash
$ curl -v -x POST console.higress.io/post -H 'host: foo.bar.com' \ -H 'Content-Type: application/json' -d '{"a1":"t1","a2":"t2","a3":"t3"}'
```

# httpbin 响应结果

```json
{
 ...
 "headers": {
 ...
 "Content-Type": "application/json",
 ...
 },
 "json": {
 "a1-new": [
 "t1-new",
 "t1-foo.bar-append"
```

`],`

```json
 "a2-new": "t2",
 "a3": "t3-new",
 "a4": "t1-new"
 },
 ...
}
```

**Content-Type: application/x-www-form-urlencoded**

```bash
$ curl -v -X POST console.higress.io/post -H 'host: foo.bar.com' \ -d 'a1=t1&a2=t2&a3=t3'
```

# httpbin 响应结果

```json
{
 ...
 "form": {
 "a1-new": [
 "t1-new",
 "t1-foo.bar-append"
```

`],`

```json
 "a2-new": "t2",
 "a3": "t3-new",
 "a4": "t1-new"
 },
 "headers": {
 ...
 "Content-Type": "application/x-www-form-urlencoded",
 ...
 },
 ...
}
```

**Content-Type: multipart/form-data**

```bash
$ curl -v -X POST console.higress.io/post -H 'host: foo.bar.com' \ -F a1=t1 -F a2=t2 -F a3=t3
```

# httpbin 响应结果

```json
{
 ...
 "form": {
 "a1-new": [
 "t1-new",
 "t1-foo.bar-append"
```

`],`

```json
 "a2-new": "t2",
 "a3": "t3-new",
 "a4": "t1-new"
 },
 "headers": {
 ...
 "Content-Type": "multipart/form-data; boundary=------------------------
1118b3fab5afbc4e",
 ...
 },
 ...
}
```

**Response Transformer**

与 Request Transformer 类似，在此仅说明转换 JSON 形式的请求/响应体时的注意事项。

**key 嵌套 .**

1. 通常情况下，指定的 key 中含有 . 表示嵌套含义，如下：

```bash
respRules:
- operate: add
 body:
 - key: foo.bar
 value: value
$ curl -v console.higress.io/get
```

# httpbin 响应结果

```json
{
 ...
 "foo": {
 "bar": "value"
 },
 ...
}
```

2. 当使用 \. 对 key 中的 . 进行转义后，表示非嵌套含义，如下：

**说明**

当使用双引号括住字符串时使用\\.进行转义。

```bash
respRules:
- operate: add
 body:
 - key: foo\.bar
 value: value
$ curl -v console.higress.io/get
```

# httpbin 响应结果

```
{
 ...
 "foo.bar": "value",
 ...
}
```

**访问数组元素 .index**

可以通过数组下标 `array.index 访问数组元素，下标从 0 开始：

```json
{
 "users": [
 {
 "123": { "name": "zhangsan", "age": 18 }
 },
 {
 "456": { "name": "lisi", "age": 19 }
 }
```

]

```
}
```

1. 移除 `user` 第一个元素：

```
reqRules:
- operate: remove
 body:
 - key: users.0
```

```bash
$ curl -v -X POST console.higress.io/post \ -H 'Content-Type: application/json' \ -d '{"users":[{"123":{"name":"zhangsan"}},{"456":{"name":"lisi"}}]}'
```

# httpbin 响应结果

```json
{
 ...
 "json": {
 "users": [
 {
 "456": {
 "name": "lisi"
 }
 }
```

]

```
 },
 ...
}
```

2. 将 `users` 第一个元素的 key 为 `123` 重命名为 `msg` :

```bash
reqRules:
- operate: rename
 body:
 - oldKey: users.0.123
 newKey: users.0.first
$ curl -v -X POST console.higress.io/post \ -H 'Content-Type: application/json' \ -d '{"users":[{"123":{"name":"zhangsan"}},{"456":{"name":"lisi"}}]}'
```

# httpbin 响应结果

```json
{
 ...
 "json": {
 "users": [
 {
 "msg": {
 "name": "zhangsan"
 }
 },
 {
 "456": {
 "name": "lisi"
 }
 }
```

]

```
 },
 ...
}
```

**遍历数组元素 .#**

可以使用 `array.#` 对数组进行遍历操作：

**说明**

该操作目前只能用在replace上，请勿在其他转换中尝试该操作，以免造成无法预知的结果。

```json
{
 "users": [
 {
 "name": "zhangsan",
 "age": 18
 },
 {
 "name": "lisi",
 "age": 19
 }
```

]

```bash
} reqRules:
- operate: replace
 body:
 - key: users.#.age
 newValue: 20
$ curl -v -X POST console.higress.io/post \ -H 'Content-Type: application/json' \ -d '{"users":[{"name":"zhangsan","age":18},{"name":"lisi","age":19}]}'
```

# httpbin 响应结果

```json
{
 ...
 "json": {
 "users": [
 {
 "age": "20",
 "name": "zhangsan"
 },
 {
 "age": "20",
 "name": "lisi"
 }
```

]

```
 },
 ...
}
```

##### 前端灰度

frontend-gray插件实现了前端用户灰度的功能。此插件不仅可以用于业务A/B实验，同时还能够通过可灰度、可监控和可回滚策略，确保系统发布和运维的稳定性。本文介绍如何配置frontend-gray插件。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `450` 。

**配置字段**

|  | 名称 |  | 数据类型 | 填写要求 |  |  | 默认值 |  |  |  |  | 描述 |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | grayKey |  | string | 非必填 |  |  | - |  |  |  |  | 用户ID的唯一标识，可以来自 Cookie或者 Header中，比如 userid ，如果没有填写则使用 rules[].gray TagKey 和 rule |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | rules[].gray |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | TagKey |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 和 | rule |  |
|  |  |  |  |  |  |  |  |  |  |  |  | e |  |  |  |  |  |
|  | graySubKey |  | string | 非必填 |  |  |  |  |  |  |  | 用户身份信息可能以JSON形式透出， 比如： userInfo: |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | userInfo: |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | { |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | userCode:"001" |  |  |  |  |  |
|  |  |  |  |  |  |  | - |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | } |  |  |  |  |  |
|  | rules |  | array of object | 必填 |  |  | - |  |  |  |  | 用户定义不同的灰度规则，适配不同的灰度场景。 |  |  |  |  |  |
|  | rewrite |  | object | 必填 |  |  | - |  |  |  |  | 重写配置，一般用于OSS/CDN前端部署的重写配置。 |  |  |  |  |  |
|  | baseDeployment |  | object | 非必填 |  |  | - |  |  |  |  | 配置Base基线规则的配置。 |  |  |  |  |  |
|  |  | baseDeployment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | grayDeployment s |  | array of object | 非必填 |  |  | - |  |  |  |  | 配置Gray灰度的生效规则，以及生效版本。 |  |  |  |  |  |
|  |  | grayDeployment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | s |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

`rules` 字段配置说明：

|  | 名称 |  | 数据类型 | 填写要求 | 默认值 |  | 描述 |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | name |  | string | 必填 | - |  | 规则名称唯一标识， 和 deploy.gray[ ].name 进行关联生效。 |  |  |
|  |  |  |  |  |  |  |  | deploy.gray[ |  |
|  |  |  |  |  |  |  | ].name |  |  |
|  | grayKeyValue |  | array of string | 非必填 | - |  | 用户ID白名单列表。 |  |  |
|  |  | grayKeyValue |  |  |  |  |  |  |  |
|  | grayTagKey |  | string | 非必填 | - |  | 用户分类打标的标签key值，来自 Cookie。 |  |  |
|  | grayTagValue |  | array of string | 非必填 | - |  | 用户分类打标的标签value值，来自 Cookie。 |  |  |
|  |  | grayTagValue |  |  |  |  |  |  |  |

`rewrite` 字段配置说明：

| indexRouting |  |  |  | 首页重写和 | fileRouting |  |  |
|---|---|---|---|---|---|---|---|
| 如到被 | /app1 | : |  |  |  |  |  |
|  | baseDeployment.version |  |  |  |  | 或者 |  |

| {version} |  | 作为保留字段，在执 |
|---|---|---|
| 者 |  |  |

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| host | string | 非必填 | - | Host地址，如果是 OSS则设置为VPC 内网访问地址。 |
| notFoundUri | string | 非必填 | - | 404页面配置。 |

|  | indexRouting | map of string to string | 非必填 |  | - |  | 用于定义首页重写路由规则。每个键 （Key）表示首页的路由路径，值 （Value）则指向重定向的目标文件。 例如，键为 /app1 对应的值为 /mfe/app1/{ |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | /mfe/app1/{ |  |
|  |  |  |  |  |  |  | version}/index. |  |  |
|  |  |  |  |  |  |  | html |  |  |
|  |  |  |  |  |  |  |  | /mfe/app1/0 |  |
|  |  |  |  |  |  |  | .0.1/index.html |  |  |
|  |  |  |  |  |  |  | 。 |  |  |
|  | fileRouting | map of string to string | 非必填 |  | - |  | 用于定义资源文件重写路由规则。每个键 （Key）表示资源访问路径，值 （Value）则指向重定向的目标文件。 例如，键为 /app1/ 对应的值为 /mfe/app1/{ version} 。生效 version 为 0.0.1 ，访问路径为 /app1/js/a. js ，则重定向到 /mfe/app1/0 .0.1/js/a.js 。 |  |  |

| /mfe/app1/{ |  |
|---|---|

|  |  | /app1/js/a. |  |  |
|---|---|---|---|---|
|  | js |  |  |  |
|  |  |  | ，则重定向 |  |
|  | 到 |  |  |  |
|  | .0.1/js/a.js |  |  |  |

`baseDeployment` 字段配置说明：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| version | string | 必填 | - | Base版本的版本号，作为兜底的版本。 |

`grayDeployments` 字段配置说明：

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|

|  | version | string | 必填 | - |  | Gray版本的版本号，如果命中灰度规则，则使用此版本。如果是非CDN 部署，在header中添加 x- higress-tag 。 |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | x- |  |
|  |  |  |  |  |  | higress-tag |  |  |
|  | backendVersion | string | 必填 | - |  | 后端灰度版本，会在 XHR/Fetch 请求的header头中添加 x-mse- tag 到后端。 |  |  |
|  | name | string | 必填 | - |  | 规则名称和 rules[].name 关联。 |  |  |
|  | enabled | boolean | 必填 | - |  | 是否启动当前灰度规则。 |  |  |

|  | tag |
|---|---|

**配置示例**

**基础配置**

```
grayKey: userid rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

cookie中的用户唯一标识为 `userid` ，当前灰度规则配置了 `beta-user` 的规则。 当满足下面调试的时候，会使用 `version: gray` 版本： cookie中 `userid` 等于 `00000002` 或者 `00000003` 。 cookie中 `level` 等于 `level3` 或者 `level5` 的用户。 否则使用 `version: base` 版本。

**用户信息存在JSON中**

```
grayKey: appInfo graySubKey: userId rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

| okie存在 | appInfo |  |
|---|---|---|
| beta-user |  |  |
|  |  | 的规则 |

cookie中 `userid` 等于 `00000002` 或者 `00000003` 。 cookie中 `level` 等于 `level3` 或者 `level5` 的用户。 否则使用 `version: base` 版本。

**rewrite重写配置**

**说明**

一般用于CDN部署场景。

```
grayKey: userid rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
rewrite:
 host: frontend-gray.oss-cn-shanghai-internal.aliyuncs.com
 notFoundUri: /mfe/app1/dev/404.html
 indexRouting:
 /app1: '/mfe/app1/{version}/index.html'
 /: '/mfe/app1/{version}/index.html',
 fileRouting:
 /: '/mfe/app1/{version}'
 /app1/: '/mfe/app1/{version}'
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

`{version}` 会在运行过程中动态替换为真正的版本。

**indexRouting：首页路由配置**

访问 `/app1` , `/app123` , `/app1/index.html` , `/app1/xxx` , `/xxxx` 都会路由到‘/mfe/app1/{version}/index.html’。

**fileRouting：文件路由配置**

下面文件映射均生效：

```
 /js/a.js  =>  /mfe/app1/v1.0.0/js/a.js
 /js/template/a.js  =>  /mfe/app1/v1.0.0/js/template/a.js
 /app1/js/a.js  =>  /mfe/app1/v1.0.0/js/a.js
 /app1/js/template/a.js  =>  /mfe/app1/v1.0.0/js/template/a.js
```

##### 自定义应答

custom-response插件支持配置自定义的响应，包括自定义HTTP应答状态码、HTTP应答头，以及HTTP应答Body。可以用于Mock响应，也可以用于判断特定状态码后给出自定义应答，例如在触发网关限流策略时实现自定义响应。本文介绍如何配置custom-response插件。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `910` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| status code _ | number | 选填 | 200 | 自定义HTTP应答状态码。 |
| headers | array of string | 选填 | - | 自定义HTTP应答头，key和value 用 = 分隔。 |
| body | string | 选填 | - | 自定义HTTP应答 Body。 |
| enable on status _ _ | array of number | 选填 | - | 匹配原始状态码， 生成自定义响应， 不填写时，不判断原始状态码。 |

**配置示例**

**Mock 应答场景**

```json
status_code: 200 headers:
- Content-Type=application/json
- Hello=World
body: "{\"hello\":\"world\"}" HTTP/1.1 200 OK Content-Type: application/json Hello: World Content-Length: 17 {"hello":"world"}
```

**触发限流时自定义响应**

```
enable_on_status:
- 429
status_code: 302 headers:
- Location=https://example.com
```

```
HTTP/1.1 302 Found Location: https://example.com
```

从而实现基于浏览器 302 重定向机制，将限流后的用户引导到其他页面，比如可以是一个 CDN 上的静态页面。 如果希望触发限流时，正常返回其他应答，参考 Mock 应答场景配置相应的字段即可。

##### DeGraphQL

de-graphql插件通过将URIs映射到GraphQL查询，从而可以将GraphQL上游转换为传统服务进行访问。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `430` 。

**参数配置**

| 参数 | 描述 | 默认 |
|---|---|---|
| gql | Graphql查询。 | 不能为空 |
| endpoint | Graphql查询端点。 | /graphql |
| timeout | 查询连接超时，单位毫秒。 | 5000 |
| domain | 服务域名，当服务来源是DNS配置。 | - |

**插件使用**

测试配置

```
apiVersion: networking.higress.io/v1 kind: McpBridge metadata:
 name: default
 namespace: higress-system
spec:
 registries:
 - domain: api.github.com
 name: github
 port: 443
 type: dns
--apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 annotations:
 higress.io/destination: github.dns
```

```
gess.o/dest ato:gtub.ds
 higress.io/upstream-vhost: "api.github.com"
 higress.io/backend-protocol: HTTPS
 name: github-api
 namespace: higress-system
spec:
 ingressClassName: higress
 rules:
 - http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
 path: /api
 pathType: Prefix
--apiVersion: extensions.higress.io/v1alpha1 kind: WasmPlugin metadata:
 namespace: higress-system
spec:
 matchRules:
 - ingress:
 - github-api
 config:
 timeout: 5000
 endpoint: /graphql
 domain: api.github.com
 gql: |
 query ($owner:String! $name:String!){
 repository(owner:$owner, name:$name) {
 name
 forkCount
 description
 }
 }
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/de-graphql:1.0.0
```

测试结果

```json
curl "http://localhost/api?owner=alibaba&name=higress" -H "Authorization: Bearer some-t oken" {
 "data": {
 "repository": {
 "description": "Next-generation Cloud Native Gateway",
 "forkCount": 149,
 "name": "higress"
 }
 }
}
```

**GraphQL介绍**

**GraphQL 端点**

REST API 有多个端点，GraphQL API 只有一个端点。

```
https://api.github.com/graphql
```

**与 GraphQL 通信**

由于GraphQL操作由多行JSON组成，因此可以使用curl或其他任何支持HTTP的库。在REST中，HTTP谓词确定执行的操作；而在GraphQL中，执行查询时需要提供JSON请求体，因此使用的HTTP谓词为POST。 唯一的例外是内省查询，它是一种简单的GET请求，针对终结点进行查询。

**GraphQL POST 请求参数**

标准的GraphQL POST请求情况如下： 添加HTTP请求头：Content-Type: application/json。 使用JSON格式的请求体。 JSON请求体包含三个字段： query：查询文档，必填。 variables：变量，选填。 operationName：操作名称，选填，查询文档有多个操作时必填。

```json
{
 "query": "{viewer{name}}",
 "operationName": "",
 "variables": {
 "name": "value"
 }
}
```

**GraphQL 基本参数类型**

基本参数类型包含： String、Int、Float、Boolean。 [类型]代表数组，例如：[Int]代表整型数组。 GraphQL基本参数传递： 小括号内定义形参，注意：参数需要定义类型。 !（叹号）代表参数不能为空。

```
query ($owner : String!, $name : String!) {
 repository(owner: $owner, name: $name) {
 name
 forkCount
 description
 }
}
```

**GitHub GraphQL 测试**

使用curl命令查询GraphQL，用有效JSON请求体发出POST请求。有效请求体必须包含一个名为query的字符串。

```json
curl https://api.github.com/graphql -X POST \ -H "Authorization: bearer <PAT>" \ -d "{\"query\": \"query { viewer { login }}\"}" {
 "data": {
 "viewer": {
 "login": "2456868764"
 }
 }
} curl 'https://api.github.com/graphql' -X POST \ -H 'Authorization: bearer <PAT>' \ -d '{"query":"query ($owner: String!, $name: String!) {\n repository(owner: $owner, na me: $name) {\n name\n forkCount\n description\n }\n}\n","variables": {"owner":"2456868764","name":"higress"}}' {
 "data": {
 "repository": {
 "name": "higress",
 "forkCount": 149,
 "description": "Next-generation Cloud Native Gateway | 下一代云原生网关"
 }
 }
}
```

**参考文档**

https://github.com/graphql/graphql-spec https://docs.github.com/zh/graphql/guides/forming-calls-with-graphql https://github.com/altair-graphql/altair

##### 浏览器缓存控制

cache-control插件实现了基于 URL 文件后缀来为请求的响应头部添加 `Expires` 和 `Cache-` `Control` 头部的功能，从而方便浏览器对特定后缀的文件进行缓存，例如 `jpg` 、 `png` 等图片文件。 本文介绍如何配置cache-control插件。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `420` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| suffix | string | 选填，表示匹配的文件后缀名，例如 jpg 、 png 等。 如果需要匹配多种后缀，需要用 \| 进行分割，例如 png\|jpg 。 如果不填写，表示匹配所有后缀。 | - | 配置用于匹配的请求文件后缀。 |
| expires | string | 必填，表示缓存的最长时间。 当填入的字符串为数字时，单位为秒，例如需要缓存1 小时，需填写 3600。 另外，还可以填写 epoch或 max，与 nginx中语义相同。 | - | 配置缓存的最大时间。 |

**配置示例**

1. 缓存后缀为 `jpg` , `png` , `jpeg` 的文件，缓存时间为一小时。

```
suffix: jpg|png|jpeg expires: 3600
```

根据该配置，下列请求在访问时，将会在响应头中添加 `Expires` 和 `Cache-Control` 字段，且过期时间为 1 小时后。

```bash
curl http://example.com/test.png curl http://exmaple.com/test.jpg
```

2. 缓存所有文件，且缓存至最大时间 “Thu, 31 Dec 2037 23:55:55 GMT” 。

```
expires: max
```

#### 可观测性

##### IP地理位置

geo-ip插件实现了通过用户ip查询出地理位置信息，然后通过请求属性和新添加的请求头把地理位置信息传递给后续插件的功能。本文介绍如何配置geo-ip插件。

**运行属性**

插件执行阶段：认证阶段插件执行优先级： `440` 。

**配置字段**

| 名称 | 数据类型 | 填写要求 | 默认值 | 描述 |
|---|---|---|---|---|
| ip protocol _ | string | 否 | ipv4 | 可选值： ipv4：只对ipv4用户请求查找地理位置信息，传递给后续插件。而ipv6用户的请求会跳过该插件，继续由后续插件处理。 ipv6：（后续版本实现此能力）只对ipv6用户查找地理位置信息，传递给后续插件。而ipv4用户的请求会跳过该插件，继续由后续插件处理。 说明当前处理方式依旧是跳过插件，请求由后续插件处理。 |
| ip source type _ _ | string | 否 | origin-source | 可选值： 对端socket ip： origin- source 。 通过header获取： header 。 |
| ip header nam _ _ e | string | 否 | x-forwarded-for | 当 ip source type 为 _ _ header 时，指定自定义 IP来源头。 |

|  |  | origin- |
|---|---|---|
| e | source |  |

**配置示例**

```
ip_protocol: ipv4 ip_source_type: header ip_header_name: X-Real-Ip
```

**property 的使用方式**

在geo-ip插件里调用proxywasm.SetProperty() 分别把country、city、province、isp设置进请求属性里，以便后续插件可以调用。proxywasm.GetProperty()获取该请求的用户ip对应的地理信息。

**基于geo-ip插件的能力，扩展AI提示词装饰器插件携带用户地理位置信息**

如果需要在LLM的请求前后加入用户地理位置信息，请确保同时开启geo-ip插件和AI提示词装饰器插件。并且在相同的请求处理阶段里，geo-ip插件的优先级必须高于AI提示词装饰器插件。首先geo-ip插件会根据用户ip计算出用户的地理位置信息，然后通过请求属性传递给后续插件。比如在默认阶段里，geo-ip插件的 priority配置1000，ai-prompt-decorator插件的priority配置500。 geo-ip插件配置示例：

```
ipProtocal: "ipv4"
```

AI提示词插件的配置示例如下：

```
prepend:
- role: system
```

`content: "`提问用户当前的地理位置信息是，国家：${geo-country}，省份：${geo-province}, 城市：${g

```
eo-city}" append:
- role: user
```

`content: "`每次回答完问题，尝试进行反问" 使用以上配置发起请求：

```json
curl http://localhost/test \ -H "content-type: application/json" \ -H "x-forwarded-for: 87.254.XXX.XXX,4.5.X.X" \ -d '{
 "model": "gpt-3.5-turbo",
 "messages": [
 {
 "role": "user",
```

`"content": "`今天天气怎么样？"

```
 }
```

]

```
}'
```

经过插件处理后，实际请求为：

```json
curl http://localhost/test \ -H "content-type: application/json" \ -H "x-forwarded-for: 87.254.XXX.XXX,4.5.X.X" \ -d '{
 "model": "gpt-3.5-turbo",
 "messages": [
 {
 "role": "system",
```

`"content": "`提问用户当前的地理位置信息是，国家：中国，省份：北京, 城市：北京"

```json
 },
 {
 "role": "user",
```

`"content": "`今天天气怎么样？"

```json
 },
 {
 "role": "user",
```

`"content": "`每次回答完问题，尝试进行反问"

```
 }
```

]

```
}'
```

##### Log请求响应记录

本文介绍如何配置log-request-response插件。 此插件用于在 Higress 的访问日志中添加以下信息： HTTP 请求头（添加为 %FILTER_STATE(wasm.log-request-headers:PLAIN)% ）。 POST、PUT、PATCH 请求的请求体内容（添加为 %FILTER_STATE(wasm.log-request-

```
body:PLAIN)% ）。
```

响应头（添加为 %FILTER_STATE(wasm.log-response-headers:PLAIN)% ）。 响应体内容（添加为 %FILTER_STATE(wasm.log-response-body:PLAIN)% ）。

**配置参数**

在 Higress 控制台配置该插件时，使用以下结构化的 YAML 配置：
# 请求相关配置`request:#` 请求头配置`headers:#` 是否记录请求头（默认：`false`）`enabled: true#` 请求体配
置`body:#` 是否记录请求体内容（默认：`false`）`enabled: true#` 最大记录长度限制，单位字节（默认：`10KB`）m `axSize: 10240#` 需要记录请求体的内容类型（默认包含常见的内容类型）`contentTypes:-`

```
application/json
      - application/xml
      - application/x-www-form-urlencoded
      - text/plain
```

# 响应相关配置`response:#` 响应头配置`headers:#` 是否记录响应头（默认：`false`）`enabled: true#` 响应体
配置`body:#` 是否记录响应体内容（默认：`false`）`enabled: true#` 最大记录长度限制，单位字节（默认： `10KB`）`maxSize: 10240#` 需要记录响应体的内容类型（默认包含常见的内容类型）`contentTypes:- applicati`

```
on/json
      - application/xml
      - text/plain
      - text/html
```

**工作原理**

请求处理时，插件会根据配置决定是否记录请求头和请求体。 只有当请求方法为 POST、PUT 或 PATCH，且内容类型在配置的 `request.body.contentTypes` 列表中时，才会记录请求体。 响应处理时，插件会根据配置决定是否记录响应头和响应体。 只有当响应的内容类型在配置的 `response.body.contentTypes` 列表中时，才会记录响应体。 所有记录的内容都会被限制在配置的 `maxSize` 指定的大小内。 插件对请求体和响应体都使用流式处理方式，不会阻止或修改原始内容传递。 记录的内容会被存储在 Envoy 的 Filter State 中，可以通过访问日志配置获取。

**访问日志配置**

要在 Higress 访问日志中显示插件添加的 Filter State 数据，需要修改 Higress 的访问日志配置。编辑 ConfigMap：

```bash
kubectl edit cm -n higress-system higress-config
```

在 `envoyAccessLogService.config.accessLog` 下的 `format` 字段中添加以下内容：

```json
{"request_headers": "%FILTER_STATE(wasm.log-request-headers:PLAIN)%","request_body": "% FILTER_STATE(wasm.log-request-body:PLAIN)%","response_headers": "%FILTER_STATE(wasm.log-response-headers:PLAIN)%","response_body": "%FILTER_STATE(wasm.log-response-body:PLAIN)%"}
```

完整的访问日志配置可能如下所示（添加至现有配置中）：

```json
mesh:accessLogFile: "/dev/stdout"accessLogFormat: |
    {
      "authority": "%REQ(:AUTHORITY)%",
      "bytes_received": "%BYTES_RECEIVED%",
      "bytes_sent": "%BYTES_SENT%",
      "downstream_local_address": "%DOWNSTREAM_LOCAL_ADDRESS%",
      "downstream_remote_address": "%DOWNSTREAM_REMOTE_ADDRESS%",
      "duration": "%DURATION%",
      "method": "%REQ(:METHOD)%",
      "path": "%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%",
      "protocol": "%PROTOCOL%",
      "request_id": "%REQ(X-REQUEST-ID)%",
      "requested_server_name": "%REQUESTED_SERVER_NAME%",
      "response_code": "%RESPONSE_CODE%",
      "response_flags": "%RESPONSE_FLAGS%",
      "route_name": "%ROUTE_NAME%",
      "start_time": "%START_TIME%",
      "trace_id": "%REQ(X-B3-TRACEID)%",
      "upstream_cluster": "%UPSTREAM_CLUSTER%",
      "upstream_host": "%UPSTREAM_HOST%",
      "upstream_local_address": "%UPSTREAM_LOCAL_ADDRESS%",
      "upstream_service_time": "%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%",
      "upstream_transport_failure_reason": "%UPSTREAM_TRANSPORT_FAILURE_REASON%",
      "user_agent": "%REQ(USER-AGENT)%",
      "x_forwarded_for": "%REQ(X-FORWARDED-FOR)%",
      "request_headers": "%FILTER_STATE(wasm.log-request-headers:PLAIN)%",
      "request_body": "%FILTER_STATE(wasm.log-request-body:PLAIN)%",
      "response_headers": "%FILTER_STATE(wasm.log-response-headers:PLAIN)%",
      "response_body": "%FILTER_STATE(wasm.log-response-body:PLAIN)%"
    }
```

**日志输出示例**

配置完成后，Higress 的访问日志中将包含这些额外字段（具体取决于您所启用的配置选项）：

```json
{"authority": "example.com","method": "POST","path": "/api/users","response_code": 200, "request_headers": " {\"host\":\"example.com\",\"path\":\"/api/users\",\"method\":\"POST\",\"content-type\": \"application/json\"}","request_body": "{\"name\":\"测试用户 \",\"email\":\"test@example.com\"}","response_headers": "{\"contenttype\":\"application/json\",\"status\":\"200\"}","response_body": " {\"id\":123,\"status\":\"success\"}"}
```

**注意事项**

所有日志记录选项默认都是关闭的（false），需要明确启用才会记录相应内容。 对于大型请求体或响应体，可以通过 `request.body.maxSize` 和 `response.body.maxSize` 参数限制记录的长度，以避免日志过大。 插件使用流式处理方式处理请求体和响应体，不会对原始内容产生任何影响。 只有指定内容类型的 POST、PUT、PATCH 请求才会记录请求体内容。 只有指定内容类型的响应才会记录响应体内容。 请确保合理配置该插件，避免记录敏感信息到日志中。

### 证书管理

#### 创建证书

通过使用证书管理功能，我们可以将证书上传至云原生网关，在上传成功后，当用户通过HTTPS方式访问网关时，网关会根据用户请求的域名将对应的证书返回给用户，从而完成TLS握手。

#### 创建证书

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**证书**。
5. 在**证书管理**页面，单击**创建证书**，配置参数信息后，单击**确定**。

| 参数 | 说明 |
|---|---|
| 证书名称 | 自定义名称，支持最大长度15个字符。 |
| 证书类型 | 仅支持服务器证书。 |
| 证书文件 | 可以直接在文本框中输入证书文件内容，或者单击上传证书从文件中读取内容。 |
| 证书密钥 | 可以直接在文本框中输入证书密钥内容，或者单击上传密钥从文件中读取内容。 |

#### 管理证书

证书管理功能还提供更新、删除、查看证书详情信息等功能，方便用户管理证书的完整生命周期。

**查看证书详情**

在上传证书成功后，可查看证书的详细信息。
1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**证书**。
5. 在**证书管理**页面，单击目标证书名称，可查看证书的详细信息：
**基本信息**：可查看**证书****ID**、**序列号**、**证书名称**、**算法**、**证书类型**、**私钥长度**、**签发时间**和**到期时间**。
**签发者信息**：可查看**签发者名称**和**签发者部门**信息。

**更新证书**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**证书**。
5. 在**证书管理**页面，单击目标证书**操作**列的**更新**。
6. 在**更新证书**面板填入更新后的证书信息，单击**确定**。

**删除证书**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**证书**。
5. 在**证书管理**页面，单击目标证书**操作**列的**删除**。
6. 在弹出的**提示**对话框中，单击**确定**。

**请求网关**

在上传证书后，分别使用证书对应的域名和错误的域名来访问网关。结果如下： 可以看出，只有通过正确的域名访问网关，才能从网关获取对应的证书，从而实现成功的握手。

### 域名管理

#### 创建域名

云原生网关提供多域名管理能力，便于您管理不同域名下的协议、证书及路由配置。

**前提条件**

完成相关域名的备案。

**说明**

中国地域独立域名需要在阿里云备案或者在阿里云备案接入，海外地域不需要域名备案。

**操作步骤**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**域名**。
5. 单击**关联域名**，在**关联域名**面板中配置相关参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| 域名 | 输入完整域名（例如： hello.com ）。在这个域名下，您可以独立管理该域名的协议及证书，路由配置可以通过域名实现相互隔离。 |
| 协议 | 选择HTTP协议或HTTPS协议。不同协议支持的端口号如下： HTTP：支持80端口。 HTTPS：支持443端口。 |
| 服务器证书 | 说明仅协议选择HTTPS时显示此参数。 选择证书管理服务创建的SSL证书。 |
| 开启双向认证 | 选择打开或关闭双向认证。 |
| CA证书 | 说明仅开启双向认证时显示此参数。 选择CA证书。若无可选的CA证书，可参考证书管理新建CA证书。 |

| 添加请求头字段以获取客户端证书持有者（Subject） 信息 | 说明仅开启双向认证时显示此参数。 可选择勾选或取消勾选此参数。若勾选此参数，系统会根据CA证书自动填写自定义请求头。 |
|---|---|
| 添加请求头字段以获取客户端证书颁发者（Issuer）信息 | 说明仅开启双向认证时显示此参数。 可选择勾选或取消勾选此参数。若勾选此参数，系统会根据CA证书自动填写自定义请求头。 |

**结果验证**

当前域名的路径下已配置可访问的路由。 如果您的域名公网解析已生效，可以直接通过浏览器访问验证。 如果您的域名还未配置DNS解析，可以通过以下方式进行验证。例如域名配置为 `hello.com` ，将下面 URL中的{公网IP}替换为您的实际公网IP。 验证HTTP

```bash
curl http://hello.com --resolve "hello.com:80:{公网IP}"
```

验证HTTPS

```bash
curl -v -k https://hello.com --resolve "hello.com:443:{公网IP}" --cacert my-cert.pem
```

#### 管理域名

创建域名后，您可以对其执行编辑、删除以及查看详情等操作。

**查看域名详情**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**域名**。
5. 在**域名管理**列表页面，单击目标域名，进入**域名详情**页面，可查看域名的**基本信息**、**插件配置**以及**关联路**
由信息。
**基本信息**：可查看**域名**和**协议**。
单击**插件配置**页签，可管理当前域名绑定的插件；单击**添加插件**，可为域名绑定插件，具体操作请参考创建插件。

**说明**

在域名列表页面，单击**操作**列的**插件配置**，也可直接跳转到**插件配置**页签。 单击**关联路由**页签，查看当前域名关联的路由信息，单击路由/服务名称可快速跳转至相应的路由/服务详情页面。

**修改域名**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**域名**。
5. 在**域名管理**列表页面，单击目标域名**操作**列的**编辑**。
6. 在**修改域名**面板中可以修改协议及证书，然后单击**确定**。

**删除域名**

1. 登录云原生网关控制台。
2. 在左侧导航栏，单击**云原生网关** > **实例列表**。
3. 在**网关实例**页面，单击目标网关实例ID或**操作**列的**详情**。
4. 在左侧导航栏，选择**域名**。
5. 在**域名管理**列表页面，单击目标域名**操作**列的**删除**。
6. 在弹出的**提示**框中，单击**确定**。

### 观测分析

#### 查看网关监控指标

云原生网关对接监控服务实现了对网关核心运行指标的全方位可观测能力，本文介绍在开启监控服务后如何

**前提条件**

已在云原生网关实例的**概览**页面启用**监控插件**功能。

**操作步骤**

1. 在顶部菜单栏，选择**产品** > **中间件** > **云原生可观测** **> Prometheus****监控** **2.0**，进入Prometheus监
控2.0控制台。
2. 在左侧导航栏，单击**接入管理**，右侧显示**已接入环境**，搜索网关所在环境名称。
3. 搜索得到相应环境，单击环境名称进入**详情**页面。
4. 在**详情**页选择单击**自监控** **> Targets**，可以在右侧列表找到**higress-gateway-metrics**。
5. 展开**higress-gateway-metrics**，单击Endpoint进入详情页面。
弹出详情页展示了所有指标。

### Nginx Ingress 迁移

Nginx Ingress 迁移是云原生网关平台提供的一站式自动化迁移工具，旨在帮助用户将现有 Kubernetes 集群中基于 Nginx Ingress Controller 的流量入口规则（Ingress 资源），平滑、安全地迁移到新一代高性能网关，即Higress 网关。本文介绍如何创建Nginx Ingress迁移任务。

**创建迁移任务**

1. 登录云原生网关控制台。
2. 在左侧导航栏，选择**云原生网关** **> Nginx Ingress****迁移**。
3. 在**Nginx Ingress** **迁移**页面，单击**创建迁移任务**。
4. 在**迁移范围确认**步骤中，配置以下参数后，单击**创建并开始评估**。

| 参数 | 说明 |
|---|---|
| 任务名称 | 输入迁移任务名称。 |
| K8s 集群 | 选择包含待迁移 Nginx Ingress 资源的 Kubernetes 集群。 |
| IngressClass | 指定要迁移的 Ingress 资源所属的 IngressClass。 |
| Namespace | 指定要迁移的 Ingress 资源所在的 Kubernetes 命名空间说明不选择则表示范围为全部 Namespace。 |

5. 在**兼容性评估**步骤中，单击**开始评估**。待评估成功后，单击**下一步：配置迁移规则**。

**说明**

若评估失败，您可以单击**重新评估**。 评估结果主要分为两类：
**不存在阻塞性问题**：可以继续执行迁移。包括以下三类：
完全兼容：Higress 原生支持，可直接使用。 部分兼容：处理策略是“带着风险迁移”，即不会被认为是阻塞性问题。它们的行为是：注解原样保留到 Higress Ingress 中，APIGateway 能识别的部分正常生效，不支持的部分（如 AJP 协议、ewma 算法）会静默失效。用户需要根据评估报告中的 `solution` 和 `risk` 字段自行判断是否可接受。
**存在阻塞性问题**：需先解决后才能继续迁移流程。阻塞性问题（BlockingIssue）包
括以下两类： 不兼容（INCOMPATIBLE）：在兼容性数据库中明确标记为 Higress 不支持。 未知注解（UNKNOWN）：注解在兼容性数据库中找不到对应记录，无法判断兼容性，需要人工评估。
6. 在**迁移规则配置**步骤中，配置以下参数后，单击**执行迁移**。

| 参数 | 说明 |
|---|---|
| 迁移模式 | 同集群迁移：指将 Ingress 在同一个 Kubernetes 集群内从一个命名空间迁移到另一个命名空间。 跨集群迁移：指将 Ingress 资源从一个 Kubernetes 集群迁移到另一个集群。 警告跨集群迁移时，请确认目标集群能够访问到所有后端服务，否则迁移后路由将无法正常工作。 |
| 目标实例 | 请指定接收迁移资源的网关实例。 |
| 迁移范围 | 选择本次迁移的Ingress资源范围。 说明不兼容和无需迁移的注解会在迁移时自动移除，可等价替换和部分兼容的注解会保留。 |

| 执行模式 | 增量迁移（跳过已迁移）：只迁移尚未成功迁移过的资源，如果某个 Ingress 已经在前一次迁移中成功转移，则本次不再重复操作。 全量覆盖（重新生成）：无论Ingress资源此前是否迁移过，系统都将执行全量重建；目标端的同名资源会被自动替换。 |
|---|---|

7. 在**流量切换**步骤中，请根据页面展示的流量切换信息，将域名解析或负载均衡器的后端从 Nginx Ingress
Controller 的 SLB 切换到 Higress 网关的 SLB。确认流量切换完成后，单击**完成迁移**。

**更多操作**

在**Nginx Ingress** **迁移**页面，您可以通过任务名称快速查询迁移任务，列表展示了迁移任务的**任务名** 称、**源集群****ID/****名称**、**目标实例****ID/****名称**、**目标集群****ID/****名称**、**创建时间**以及**任务状态**。 单击任务名称，可跳转到当前执行步骤。
