---
title: "大数据计算服务 用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 395
source_pdf: "06_用户指南_enterprise-ascm-user-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/odps/zh/enterprise-ascm-user-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 大数据计算服务 用户指南

## 什么是大数据计算服务

大数据计算服务（MaxCompute）是阿里巴巴自主研发的海量数据处理平台，主要提供数据上传和下载通道，提供SQL及MapReduce等多种计算分析服务，同时还 MaxCompute主要服务于批量结构化数据的存储和计算，可以提供海量数据仓库的解决方案以及针对大数据的分析建模服务。 随着社会数据收集手段的不断丰富及完善，越来越多的行业数据被积累下来。数据规模已经增长到了传统软件行业无法承载的海量数据（百GB、TB、乃至PB）级别。 在分析海量数据场景下，由于单台服务器的处理能力限制，数据分析者通常采用分布式计算模式。但分布式的计算模型对数据分析人员的能力要求较高，且不易维护。 使用分布式模型，数据分析人员不仅需要了解业务需求，同时还需要熟悉底层计算模型。 MaxCompute的目的是为您提供一种便捷的分析处理海量数据的手段。您可以不必关心分布式计算细节，从而达到分析大数据的目的。MaxCompute已经在阿里巴巴内部得到大规模的应用，例如：大型互联网企业的数据仓库和BI分析、网站的日志分析、电子商务网站的交易分析、用户特征和兴趣挖掘等。 MaxCompute具体支持如下相关功能： 数据通道： Tunnel：提供高并发的离线数据上传和下载服务。您可以使用Tunnel服务向MaxCompute批量上传数据，或者将数据从MaxCompute下载到本地。目前，Tunnel仅提供Java编程接口供您使用。 计算及分析任务： SQL：MaxCompute只能以表的形式存储数据，并且对外提供了SQL查询功能。您可以将MaxCompute作为传统的数据库软件操作，但其却能处理TB、PB级别的海量数据。同时MaxCompute的SQL语法符合ANSI99规范，兼容TPCDS全部query，也兼容Hive生态，但与Oracle、MySQL有一定差别。此外，MaxCompute SQL引擎的优化方向是面向高吞吐、性价比和稳定产出，批处理场景不保证高QPS查询任务的毫秒级返回。MaxCompute SQL的优点体现在学习成本低，您不需要了解分布式概念，只要具备数据库操作经验就可以快速熟悉MaxCompute SQL的使用。 MapReduce：MapReduce最早是由Google提出的分布式数据处理模型，随后受到了业内的广泛关注，并被大量应用到各种商业场景中。在本文档中，会对 MapReduce模型做简要介绍，以便于您快速熟悉、了解该模型。使用MapReduce需要对分布式概念有基本了解，并有对应的编程经验。MapReduce为您提供 Java编程接口。 访问并处理非结构化数据（融合计算场景）：MaxCompute团队依托MaxCompute系统架构，引入非结构化数据处理框架，解决了MaxCompute SQL面对 MaxCompute表外的各种用户数据时（例如OSS上的数据）需要先通过各种工具导入MaxCompute表才能进行计算，无法直接处理的问题。 内部数据源：OSS、TableStore、AnalyticDB、RDS、HDFS（内部）、TDDL。 外部数据源：HDFS（开源）、MongoDB、HBase。 访问并处理非结构化数据（内部）：通过支持读写Volume，建立了MaxCompute对非结构化数据的存储和处理能力，解决了非结构化数据只能存储在外部存储系统的问题。 Spark on MaxCompute：Spark on MaxCompute是阿里云开发的大数据分析引擎，为阿里内部用户、政企客户提供大数据处理能力。详情请参见Spark on MaxCompute。 ElasticSearch on MaxCompute：ElasticSearch on MaxCompute是阿里云开发的企业级海量数据检索系统，用于海量数据的全文检索，为政企客户提供近实时搜索性能的海量数据检索服务。详情请参见ElasticSearch on MaxCompute。 SDK：提供给开发者的工具包。 安全解决方案：MaxCompute提供了功能强大的安全服务，为您的数据安全提供保护。

## 使用须知

在使用MaxCompute产品前，您可以根据实际需求，选择性地阅读相应章节。本章节针对不同的阅读对象，给出不同的阅读建议。

**如果您是一个初学者**

如果您是一个初学者，建议您从如下章节开始读起： 什么是大数据计算服务：MaxCompute产品的总体介绍以及包含的主要功能。通过阅读该章节，您会对MaxCompute有一个总体的认识。 快速入门：通过实例一步一步指引您如何下载及配置客户端、如何创建表、如何授权、如何导入导出数据、如何运行SQL任务、如何运行UDF、如何运行基本概念及常用命令：MaxCompute基本概念、MaxCompute常用命令介绍。您可以进一步熟悉如何操作MaxCompute。 常用工具：在分析数据之前，您可能需要掌握MaxCompute常用工具的下载、配置以及使用方法。

**如果您是一个数据分析师**

如果您是一个数据分析师，您可能需要熟读如下章节。 MaxCompute SQL：您可以查询并分析存储在MaxCompute上的大规模数据，包含的主要功能如下： 支持DDL语句：您可以通过Create、Drop和Alter操作对表和分区进行管理。 支持DML语句： 您可以通过Select语句选择表中的某几条记录，通过Where语句查看满足条件的记录，实现过滤功能。 您可以通过等值连接Join实现两张表的关联。 您可以通过对某些列Group By，实现聚合操作。 您可以通过Insert overwrite/into把结果记录插入到另一张表中。 您可以通过Select Transform功能来简化对脚本代码的引用。 你可以通过内置函数和自定义函数（UDF）来实现一系列的计算。 您可以通过UDT在SQL中直接引用第三方语言的类或者对象，获取其数据内容或者调用其方法。 您可以通过UDJ来实现灵活的跨表、多表自定义操作，同时减少不得不通过MR等方式对分布式系统底层细节的操作。 支持收集表的统计信息和设置表生命周期。 支持正则表达式。

**如果您是一个有开发经验的用户**

如果您是一个有开发经验的用户，并且对分布式概念有一定程度的了解，同时，由于某些数据分析无法使用SQL来实现，此时建议您学习MaxCompute更高级的功能模块： MaxCompute MapReduce：MaxCompute提供的Java MapReduce编程模型。您可以使用MapReduce提供的接口（Java API）编写MapReduce程序，用于处理MaxCompute中的数据。 Eclipse开发插件：方便您使用MapReduce、UDF的Java SDK进行开发工作。 Java SDK：提供给开发者的工具包。 MaxCompute Tunnel：您可以使用Tunnel服务向MaxCompute批量上传离线数据，或者从MaxCompute下载离线数据。

**如果您是项目Owner或者管理员**

如果您是一个项目空间的Owner或者管理员，您需要熟读如下章节。 创建项目：项目（Project）是MaxCompute的基本组织单元，是进行多用户隔离和访问控制的主要边界。 用户授权及权限查看：授予用户对MaxCompute中的Object（或称之为客体，例如：表、任务、资源等）某种操作权限，包括：读、写、查看等权限。 安全解决方案：您可以通过阅读该章节，了解如何给用户授权、如何进行跨项目空间的资源共享、如何设置项目空间的数据保护功能、如何进行Policy授权等安全操作。

## 准备工作

### 登录Apsara Uni-manager运营控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。

**说明**

单击右上角的当前语言可以切换其它语言。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Uni-manager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。
请向运营管理员获取登录控制台的用户名和密码。

**说明**

**首次登录**

首次Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。

**忘记密码**

用户忘记登录密码时，单击忘记密码，输入账户名（当前账号的用户名）、邮箱（当前用户创建时所录入的邮箱）和验证码后，重置密码的链接将发至邮箱，进入链接后用户可输入新密码。
3. 单击**账号登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：

**管理员强制开启MFA后的首次登录**

a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**账号登录**。 c. 输入6位MFA码后单击**认证**。

**您已开启并绑定MFA**

输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《**Apsara Uni-manager****运营控制台用户指南》**中的**《管理多因素认证》**章节。

### 进入概览页

本章节为您介绍控制台概览页展示的详细信息。

**操作步骤**

1. 使用管理员身份登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **大数据计算** > **云原生大数据计算服务** **MaxCompute** ，进入**概览**页面。
3. 在**概览**页面，您可以查看以下信息。

| 区域 | 说明 |
|---|---|
| 实例总览 | 在实例总览区域可查看本组织下已创建的Project数和配额组数。 单击Project数，可前往Project管理页面查看Project的详细信息，并创建Project。详情请参见创建项目。 单击配额组数，可前往配额组管理页面查看配额组的详细信息，并创建配额组。详情请参见创建配额组。 |
| 配额统计 | 在配额统计区域可查看资源使用率（%）以及资源分配情况，资源分配情况包括：资源CU数量、已分配、已使用、存储、组织已分配、项目已分配。 重要配额统计信息仅在CU资源超卖开关关闭状态下可见。 |
| 组织排名TOP10 | 在组织排名TOP10区域可查看资源使用趋势。 您可查看本组织及下级组织中，磁盘使用率最高的前10个组织。 可查看近7天、近15天，或近30天内的资源使用趋势图，了解资源的使用变化趋势。 |

### 准备任务云账号

本章节为您介绍如何创建任务云账号。

**操作步骤**

1. 使用管理员身份登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **大数据计算** > **云原生大数据计算服务** **MaxCompute** ，进入**概览**页面。
3. 在左侧导航栏单击**任务云账号**，在页面单击**创建云账号**。
4. 在弹出的对话框中，填写好相关的账号信息后，单击**提交**，完成任务云账号的创建。

| 参数 | 描述 |
|---|---|
| 名称 | 任务云账号的名称。 |
| 组织 | 选择该任务云账号所要归属的组织。 |
| 描述 | 对该任务的云账号描述，可以不填写。 |

**（可选）其他相关操作**

查询云账号信息您可以在**云账号名称**后的搜索框中输入关键词，对目标云账号进行模糊查询。 修改云账号信息如果您需要对已创建的云账号信息进行修改，可单击目标云账号右侧**操作**列下的**修改**，修改云账号的**名称**、**描述**信息。 设置云账号的界面展示信息您可以单击右上角的图标，设置是否展示**云账号****PK**、**云账号****ID**，当前系统默认展示**云账号名称**。

### 创建项目

本章节为您介绍如何创建MaxCompute项目。

**进入MaxCompute项目创建页面**

1. 使用管理员身份登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **大数据计算** > **云原生大数据计算服务** **MaxCompute** ，进入**概览**页面。
3. 单击左侧导航栏中的**Project****管理**，进入**Project****管理**页面。
4. 您可单击**创建****Project**，进入**创建****MaxCompute****项目**配置页面。

**创建MaxCompute项目**

在**创建****MaxCompute****项目**配置页面，请参考以下步骤完成相关参数配置。

**（可选）选择服务目录**

**说明**

MaxCompute项目支持接入服务目录，实现运营管控。上架后可配置页面参数，并支持询价与流程审批。 创建服务目录后，您在**创建****MaxCompute****项目**时可看到**计费方式**信息，当前仅支持**按量计费**。 未创建服务目录的用户可忽略当前步骤。
1. 已创建服务目录，可在跳转到的页面中选择对应的服务目录。
2. 单击**确定**后可进入**创建****MaxCompute****项目**页面。

**区域信息配置**

配置**区域**信息时，容灾项目与非容灾项目的参数略有不同，请根据实际需求选择对应的配置方式。

**非容灾项目配置方式**

| 参数 | 描述 |
|---|---|
| 组织/资源集 | 创建项目时需要选择的组织和相关资源集，必填。 |
| 地域 | 选择地域，必填。 说明若MaxCompute在单元Region是以单元化方式部署的，则此处选中单元化Region时，其他地域为不可选（置灰）状态。 |
| 芯片架构 | 您的芯片架构信息。 |

| 同城容灾 | 配置非容灾项目，无需打开同城容灾开关。 |
|---|---|
| 集群 | 创建项目时，您可根据需要选择创建单集群Project。 重要单集群Project不支持容灾功能。 集群支持别名修改。详细操作：进入飞天基础运维控制台 > 资源管理 > 产品集群运维页面，在产品列表中搜索目标集群，在目标集群下单击别名右侧的编辑图标，即可进行修改。修改后的别名，会同步至Apsara Uni- manager运营控制台上MaxCompute项目空间下。 |

**容灾项目配置方式**

为确保系统高可用性、资源一致性及硬件兼容性，创建具备同城容灾能力的Project时，须遵循以下约束规则。您可在了解完相关约束规则后，进行相关配置。

**约束规则**

**主备集群芯片架构兼容性约束**

容灾主备集群的底层计算芯片必须满足严格的架构兼容矩阵，以保障故障切换时的指令集一致性与运行时稳定性。

| 芯片架构 | 架构说明 | 是否允许交叉使用 |
|---|---|---|
| 主备集群均基于x86指令集架构 | 且芯片厂商为Intel与海光（Hygon）的任意组合。 | 允许 |
| 跨指令集架构配对 | 主集群与备集群分别采用 x86 与 ARM 架构（如Intel vs鲲鹏/飞腾），因指令集不兼容，禁止建立容灾关系。 | 禁止 |
| ARM架构内部异构配对 | 即使同属ARM生态，华为鲲鹏（Kunpeng）与飞腾（Phytium）芯片因微架构差异、固件生态隔离及性能特性不一致，也不允许交叉配对。 | 禁止 |

**同城容灾角色与切换策略限制**

**默认行为**：在同城容灾模式下，主备集群角色固定，不支持自动或手动切换（即备集群不可升主）。
**业务影响说明**：备集群仅作为冷备或温备实例存在，不具备升主能力。若需恢复服务，须重建Project。

**参数配置**

| 参数 | 描述 |
|---|---|
| 组织/资源集 | 创建项目时需要选择的组织和相关资源集，必填。 |
| 地域 | 选择地域，必填。 说明若MaxCompute在单元Region是以单元化方式部署的，则此处选中单元化Region时，其他地域为不可选（置灰）状态。 |
| 芯片架构 | 您的芯片架构信息。 |
| 同城容灾 | 打开同城容灾开关，您可创建容灾Project。 重要您可以单击同城容灾下方的智能容灾指引，查看更详细的同城容灾项目创建说明。 |
| 容灾集群 | 开启同城容灾后，创建项目时可按需选择创建多集群Project。 重要当您需要创建容灾Project时，除了选择默认的计算集群外，还需要选择对端机房的计算集群作为灾备计算集群。此外，在容灾Project创建后，默认主备集群之间不会进行数据同步，您需要登录大数据管家开启数据同步功能。详细操作请参见大数据管家 > 用户指南 > ABM > 业务运维 > 创建及配置MaxCompute同城容灾项目章节。 |

**资源信息配置**

| 参数 | 描述 |
|---|---|

| 配额组 | 可以选择集群中对应的配额组。 说明创建容灾Project时，配额组默认状态不可选。 |
|---|---|
| 申请逻辑存储空间（GB） | 该部分为项目要申请的逻辑存储空间大小，不能超过逻辑存储总量。 说明创建容灾Project时，备集群的申请逻辑存储空间跟随主集群申请值变更。 配额来源：备集群的CU配额完全继承自主集群的申请值，二者严格保持一致。 用户操作限制： 用户不可独立申请、修改或释放备集群的CU配额。 控制台中备集群CU字段为只读状态，仅用于信息同步展示。 |

**安全增强开关配置**

| 参数 | 描述 |
|---|---|
| 联合计算增强包 | 默认关闭，选择开启后，支持联合计算的相关功能。 |
| 是否加密 | 选择是否进行加密，默认值为否。 |
| 加密方式 | 默认不显示，在是否加密中选择是时显示，可供选择的加密算法为AESCTR、AES256、RC4和SM4。 |
| 加密Key | 默认不显示，在是否加密中选择是时显示，默认为项目自建。 |

**基本信息配置**

| 参数 | 描述 |
|---|---|
| Project名称 | 即当前正在创建的项目的名称。 |
| 任务云账号 | 任务云账号的名称。如果没有，创建流程及详细的配置信息请参见准备任务云账号。 |

完成上述参数配置后，请单击**确认订单**以完成MaxCompute项目的创建。

**说明**

若未开启**服务目录**，按钮显示为**提交**。

**查看MaxCompute项目**

在**Project****管理**页面，即可查看所有Project的**配额组名称**、**配置逻辑存储空间**、**Endpoint**及**容灾状态**等信息。单击目标MaxCompute项目名称，进入**项目详情**页， 可查看**实例明细**和**操作日志**。 实例明细选择**实例明细**页签，可查看项目的加密设置、VPC设置等信息。 操作日志选择**操作日志**页签，可通过柱状图查看该项目近一周的API调用数量，也可在日志列表中查看或筛选该项目的日志信息，单击目标日志操作列的**操作详情**，可查看该日志的基本信息及API调用详情。

**管理MaxCompute项目**

**管理配置逻辑存储空间**

1. 单击目标MaxCompute项目名称，进入**项目详情**页。
2. 在**实例明细** > **区域设置**区域，单击目标实例**操作**栏中的**编辑**。
3. 可基于已创建的服务目录，对配置逻辑存储空间操作进行运营管控。

**定义项目标签**

在**Project****管理**页面，您可以根据业务需求定义各类标签，对已创建的Project添加标签，便于分类、检索和查找。
1. 鼠标悬浮至目标Project的**标签**列，即可看到标签编辑图标
。
2. 单击标签编辑图标
，在**编辑标签**对话框中添加或者选择已有的**标签键**和**标签值**。

**说明**

标签键必须唯一。 创建标签时，最多可同时创建20个标签。 如果需要对标签进行统一管理，更多信息请参见**统一云管平台****用户指南** > **运营中心** > **资源运营** > **标签管理**章节的相关内容。
3. 单击**确定**，确认标签编辑成功后，单击**关闭**。
4. 在**Project****管理**页面，即可看到已添加的标签。
待添加标签完成后，您可以使用**标签筛选**功能，选择**标签键**或者**标签值**，筛选目标Project。

**删除项目**

未绑定DataWorks工作空间您可在**Project****管理**页面单击目标MaxCompute项目**操作**列的**删除**，在弹出的**删除****MaxCompute****项目**对话框中阅读项目删除风险，并勾选确认信息后，单击确定。 已绑定DataWorks工作空间： 您可在**Project****管理**页面单击目标MaxCompute项目**操作**列的**解绑并删除****DataWorks****空间**，然后根据页面提示前往DataWorks平台解绑并删除DataWorks工作空间，最后在MaxCompute的**Project****管理**页面删除目标项目。

**重要**

执行项目删除操作后，您可在7天内联系管理员进行恢复，如果到期前没有恢复，项目会正式删除，项目内的数据、UDF、资源、权限配置等均不可恢复。

**恢复项目**

您可在**Project****管理**页面，单击目标MaxCompute项目**操作**列的**恢复**，根据弹框提示联系系统管理员，由项目管理员在项目被标记为**删除**状态后的7天内完成恢复操作。

**说明**

如果到期前没有恢复，项目会正式删除，项目内的数据、UDF、资源、权限配置等均不可恢复。

**附录：创建服务目录**

1. 单击上方工具栏中的**运营** > **服务运营**。
2. 找到左侧导航栏中的**服务目录** > **服务管理**。
3. 单击**创建服务**，进入**创建服务**页面。
4. 在**创建服务**时，选择目标**产品**（**云原生大数据计算服务** **MaxCompute** ）和关联资源（**项目**）。
5. 按界面提示配置其它参数（**服务名称**、**授权类型**等）。

**说明**

更多参数详细信息，可以参考阿里云专有云官网文档**统一云管平台****用户指南** > **运营中心** > **服务运营** > **服务目录**章节。
6. **提交**并完成服务目录创建后，您可基于该目录创建MaxCompute项目，并管理**配置逻辑存储空间**的修改。

### 创建配额组

本文介绍MaxCompute配额组的全生命周期管理，包括创建、查询、修改、共享及CU超卖等操作，方便您高效分配、灵活调整并优化计算资源使用。

**进入配额组创建页面**

1. 使用管理员身份登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **大数据计算** > **云原生大数据计算服务** **MaxCompute** ，进入**概览**页面。
3. 在左侧导航栏单击**配额组管理**，进入**配额组管理**页面。
4. 您可单击**创建配额组**，进入**创建配额组**配置页面。
1. （可选）选择服务目录。

**说明**

MaxCompute项目支持接入服务目录，实现运营管控。上架后可配置页面参数，并支持询价与流程审批。 未创建服务目录的用户可忽略当前步骤。 i. 已创建服务目录，可在跳转到的页面中选择对应的服务目录。
2. 在跳转到的页面中，填写好相关的项目信息。

**区域信息**

| 参数 | 描述 |
|---|---|
| 组织/资源集 | 创建时配额组需要选择的组织和资源集。 |
| 地域 | 配额组所在集群部署的地域。 说明若MaxCompute在单元Region是以单元化方式部署的，您可选择目标单元地域，创建单元地域的配额组。 |
| 集群 | 创建配额组时对应的集群信息。 |

**基本配置信息**

| 参数 | 描述 |
|---|---|
| 配额组名称 | 即当前正在创建的配额组的名称。 |
| 共享范围 | 配额组可以共享的范围，包括本资源集、本组织及下级组织和本组织三个范围。 |
| cu数量 | 选择分配给当前配额组的资源数量，必须大于0。 说明可用数量受集群资源限制，如果集群配额组数量剩余 0 ，请重新选择配额组数量充足的集群。 |

3. （可选）查看配置概览信息。
在右侧的**配置概览**面板中，您可以执行以下操作： 查看参数配置情况
**配置概览**会实时校验必填项，未填写时相应条目将呈现红色警告状态。
管理配额您可单击**管理**按钮，进入配额管理页面为实例设置配额上限。更多设置详情可参见**《统一云管平台****用户指南》**中的**运营中心** > **配额管理**章节。

**说明**

设置配额时，需结合当前配额组CU数量的实际使用情况，防止因配额设置过低，影响配额组的创建。 快速定位单击目标参数右侧的条目，即可快速跳转到目标参数的配置项。
4. 单击**确认订单**按钮，完成配额组的创建。

**说明**

若未开启**服务目录**，按钮显示为**提交**。

**管理配额组**

**查询配额组信息**

您可以通过在**配额组名称**或者**集群名称**后的搜索框中输入关键词，进行相关信息筛选。

**说明**

若MaxCompute在单元Region是以单元化方式部署的，您可单击**地域**后的下拉框，切换单元Region查看对应的配额组信息。

**CU资源超卖**

您可以根据实际情况（例如CU资源售卖较多，但实际使用率不高）决定是否开启CU资源超卖开关。默认为关闭状态。 如果CU资源超卖开关开启，则**配额组管理**页面的配额组列表中将展示为**上限****CU**，此时不支持修改CU数量。 如果CU资源超卖开关关闭，则**配额组管理**页面的配额组列表会展示为**保障****CU**，此时支持修改CU数量。 具体操作：
1. 依次进入**专有云运维平台** > **平台运维** > **管控服务运维** **> UniConsole****管控研发平台**。
2. 在**产品列表**下搜索**odps**。
3. 单击操作列下的**开关列表**，找到**ODPS****超卖展示开关**。
4. 单击右侧**修改开关状态**。在**查看功能开关初始状态**弹框中，按需设置，单击**确定**。

**修改CU数量**

如果您需要对已创建的配额组进行修改，可单击目标配额组右侧**操作**列下的**修改****CU****数量**。

**说明**

若已创建服务目录，在调整配额组的CU数量时，可实施运营管控。

**共享配额组**

如果您需要将配额组共享给其他组织对象使用，可单击目标配额组右侧**操作**列下的**共享设置**，在**共享设置**对话框中选择**共享范围**为**本资源集共享**、**本组织及下级组织共** 享或**本组织共享**，并单击**确定**。

**删除配额组**

如果您需要对已创建的配额组进行删除，可单击目标配额组右侧**操作**列下的**删除**。

**设置配额组界面展示信息**

您可以单击右上角的图标，设置是否展示**配额组**的地域、集群名称、组织、资源集等相关信息，当前系统默认展示**配额组名称**。

**附录：创建服务目录**

1. 单击上方工具栏中的**运营** > **服务运营**。
2. 找到左侧导航栏中的**服务目录** > **服务管理**。
3. 单击**创建服务**，进入**创建服务**页面。
4. 在**创建服务**时，选择目标**产品**（**云原生大数据计算服务** **MaxCompute** ）和关联资源（**配额组**）。
5. 按界面提示配置其它参数（**服务名称**、**授权类型**等）。

**说明**

更多参数详细信息，可以参考阿里云专有云官网文档**统一云管平台****用户指南** > **运营中心** > **服务运营** > **服务目录** > **服务管理**章节。
6. **提交**并完成服务目录创建后，您可基于该目录创建MaxCompute项目，并管理**配额组****CU**的修改。

## 快速入门

### 概述

本文为您介绍MaxCompute的使用流程，旨在引导您一站式完成MaxCompute的基础使用。 MaxCompute的使用流程如下。

| 配置客户端添加用户用户授权角色创建及授权创建表导入导出数据运行SQL 运行使用UDF |  |
|---|---|
| 运行 | 使用UDF |

必选配置可选配置
1. 配置客户端（Console）。
您可以通过MaxCompute客户端访问MaxCompute的项目空间并使用各项功能。因此您需要下载并配置客户端。
2. 添加用户。
任意非项目空间Owner的用户必须被加入MaxCompute项目空间中，并被授予对应的权限，才能在MaxCompute中的对应项目空间中进行操作。
3. 用户授权。
在添加用户后，需要给用户授权。只有用户获得权限后，才能执行相关操作。 当项目空间下有大量用户存在时，用户授权操作会非常繁琐。此时，项目空间管理员可以对拥有相同权限的用户进行分类，每类用户有相同的权限，称之为角色。给角色授权后，该角色下的所有用户即拥有相同的权限。
5. 创建表。
用户加入项目空间并被授予权限之后，即可开始操作MaxCompute。此时，通常会先进行相关的表操作。
6. 导入导出数据。
您可以通过MaxCompute Tunnel提供的SDK自行编写Java程序，完成MaxCompute的数据导入导出操作。
7. 运行SQL。
仅介绍运行SQL的常用语句时的使用限制，具体的SQL使用及运行请参见MaxCompute SQL。
8. 您还可以进行下列的任意可选操作。
（可选）使用UDF。 下载MaxCompute客户端后，可以尝试使用UDF。MaxCompute的UDF包括：UDF、UDAF、UDTF三种函数。

### 配置客户端（Console）

您可通过MaxCompute客户端连接项目空间并使用各项功能；本文将指导您完成客户端的下载、环境准备、配置（包括 AccessKey、项目名称和服务地址）及启动运行。

**前提条件**

| 由于客户端是使用Java开发的，因此要确保本地安装有JRE 1.8。同时，您需要提前准备好云账号并获取 | AccessKey ID | 和 | AccessKey Secret | 。 |
|---|---|---|---|---|
| 说明您在开始配置客户端前，请确认已创建项目空间，且获取其 AccessKey ID 和 AccessKey Secret 。 |  |  |  |  |

**操作步骤**

1. 下载客户端压缩包到本地。
2. 将下载好的客户端压缩包解压到一个文件夹中，在该文件夹中可以看到如下4个文件夹。

```
bin/ conf/ lib/ plugins/
```

| 编辑conf文件夹中的 | odps_config.ini | 文件，配置如下相关信息。 |
|---|---|---|
| project_name=my_project access_id=******************* access_key=********************* end_point= <MaxCompute服务地址> |  |  |

| 参数 | 说明 |
|---|---|
| access_id | 用户的云账号信息。其中， access_id 对应 AccessKey ID ， access_key 对应 AccessKey Secret ，需要获取所属组织的AccessKey ID和AccessKey Secret（登录Apsara Uni-manager运营控制台，在企业 > 资源管理 > 组织管理 > 管理 Accesskey获取）。 |
| access_key |  |
| project_name | 指定您想进入的项目空间。一旦配置此项，每次登录客户端，将会默认进入到该项目空间。如果不配置，登录客户端后，必须使用 use <project_name>; 命令进入项目空间。 |
| end_point | 需要配置成MaxCompute提供给用户的服务地址。针对不同的用户，服务地址也不同。 重要在安全方案允许的情况下，必须保证odpscmd和MaxCompute的endpoint网络是互通的。 _ |

4. 修改好配置文件后，运行bin目录下的odps文件（在Linux系统下运行odpscmd文件，在Windows下运行odpscmd.bat文件），此时就可以开始运行SQL语句及相
关命令行了，示例如下。

```
CREATE TABLE tbl1(id bigint); INSERT OVERWRITE TABLE tbl1 SELECT COUNT(*) FROM tbl1; SELECT 'welcome to MaxCompute!' FROM tbl1;
```

**说明**

更多SQL语句的详细信息请参见《**MaxCompute****开发指南》**的**MaxCompute SQL**章节。

|  | help; |  |
|---|---|---|
| quit; |  | q; |

### 添加删除用户

任意非项目空间Owner用户必须被加入MaxCompute项目中，并被授予对应的权限，才能在MaxCompute中的对应项目中进行操作。本文介绍项目Owner如何将其他用户加入对应的项目或者从对应的项目中删除。

## 使用须知

如果您是项目Owner，建议您仔细阅读本章节；如果您是普通用户，建议您向项目Owner提出申请，加入对应的项目空间后再阅读后续章节。 查询当前用户是否为项目Owner的步骤如下：
1. 在客户端执行 whoami; 命令查询当前用户。

| 使用如下命令查询当前用户的权限，返回结果为 | Project Owner | 表示当前用户账号为项目Owner： |
|---|---|---|
| SHOW grants FOR <username>; |  |  |

`username` 为步骤1的查询结果。

**查询当前项目下的账号**

如果您不确定要添加或删除的用户账号是否已经存在于当前项目中，可以通过如下命令来查看。

```
LIST users;
```

**添加用户**

命令格式。

```
ADD USER ALIYUN$<userid>;
```

参数说明。 使用示例。

| 将云账号ID为 | ascm-dw-1**********28 | 的账号加入当前项目： |
|---|---|---|
| ADD USER ALIYUN$ascm-dw-1**********28; |  |  |

**说明**

添加用户成功后，被添加的用户不能立刻在MaxCompute中对应的项目空间进行操作，需要项目空间Owner对用户授予一定权限，该用户才能在所拥有的权限范围内进行操作。

**删除用户**

命令格式。

```
REMOVE USER ALIYUN$<userid>;
```

参数说明。 `userid` 为您任务云账号的云账号ID，您可以使用 list users; 命令，获取当前项目中已添加的云账号ID。 使用示例。

| 将云账号ID为 | ascm-dw-1**********28 | 的账号从当前项目删除： |
|---|---|---|
| REMOVE USER ALIYUN$ascm-dw-1**********28; |  |  |

在删除用户前，请确保该用户的所有权限已经被取消。

**说明**

如果用户被删除，但该用户的权限未被取消，则该用户的权限仍然保留，当该用户再次被加入对应项目空间时，原有权限将被恢复。 更多信息添加、删除用户操作可参见项目空间的用户管理。

### 用户授权及权限查看

**4.4.1. 概述**

添加用户后，需为其授权，用户只有获得相应权限后才能执行相关操作。

**相关说明**

所谓授权，即授予用户对MaxCompute中Object（或称之为客体，例如：表、任务、资源等）的某种操作权限（包括读、写、查看等）。

**重要**

下面各章节主要针对项目空间的管理员用户。如果您只是MaxCompute的普通用户，请确认已经获取足够权限。 MaxCompute的授权分为以下两种不同的授权策略： 如需了解某个用户具备哪些权限，具体操作请参见查看权限。

#### 4.4.2. ACL授权

本文介绍ACL授权的命令语法及使用示例，方便您通过GRANT命令为用户或角色精准分配操作权限。

**适用范围**

ACL授权中，MaxCompute的客体包括：Project、Table、Function、Resource、Instance和Task。

**授权命令**

```
GRANT actions ON object TO subject REVOKE actions ON object FROM subject actions ::= action_item1, action_item2, ... object ::= project project_name | TABLE schema_name |
           instance inst_name | FUNCTION func_name |
           resource res_name
subject ::= USER full_username | role role_name
```

**授权示例**

项目管理员可以为组织云账号（RAM主账号）、任务云账号（RAM主账号）或本组织的子账号（RAM子账号）授权。

**说明**

添加其他组织的子账号需要先把其他组织云账号加入项目，再由其组织云账号添加。 场景一：假设 `ali***@aliyun.com` 是项目 `test_project_a` 的新成员，项目管理员可执行以下命令，授予用户提交作业、创建数据表及查看项目已有对象的权限。 `--`打开项目。

```
USE test_project_a;
```

`--`添加用户。

```
ADD USER aliyun$ali***@aliyun.com;
```

`--`创建角色`worker`。

```
CREATE role worker;
```

`--`将角色`worker`指派给用户。

```
GRANT worker TO aliyun$ali***@aliyun.com;
```

`--`授权方式一：为角色`worker`授予项目`test_project_a`中创建实例、创建资源、创建函数、创建表以及查看项目所有对象类型的权限。

```
GRANT CreateInstance, CreateResource, CreateFunction, CreateTable, List ON PROJECT test_project_a TO ROLE worker;
```

`--`授权方式二：为角色`worker`授予实例的所有权限。

```
GRANT ALL ON instance instance_name TO Role worker;
```

场景二：假设Allen是从属于 `ali***@aliyun.com` 的RAM子账号。项目管理员可执行以下命令为该组织云账号下的子账号（RAM USER）授权。 `--`添加`RAM`子账号。

```
ADD USER ram$ali***@aliyun.com:Allen;
```

`--`创建角色`worker`。

```
CREATE role worker;
```

`--`将角色`worker`指派给用户。

```
GRANT worker TO ram$ali***@aliyun.com:Allen;
```

#### 4.4.3. Policy授权

本文介绍MaxCompute Policy授权的命令及策略编写方法，通过示例说明如何使用权限策略实现细粒度权限控制，如限制Tunnel操作并授权SQL只读访问。

**使用方式**

Policy授权是一种基于主体的授权，Policy授权的详细信息请参见Policy权限策略。

**授权命令**

```
GET POLICY;
```

`--` 读取项目空间的`Policy`。

```
PUT POLICY <policyFile>;
```

`--` 设置（覆盖）项目空间的`Policy`。

```
GET POLICY ON ROLE <roleName>;
```

`--` 读取项目空间中某个角色的`Policy`。

```
PUT POLICY <policyFile> ON ROLE <roleName>;
```

`--` 设置（覆盖）项目空间中某个角色的`Policy`。

**授权策略**

```json
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "odps:*"
```

`],`

```json
      "Resource": "acs:odps:*:projects/$user_project_name/tables/*",
      "Condition": {
        "StringEquals": {
          "odps:TaskType": [
            "DT"
```

]

```json
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "odps:List",
        "odps:Read",
        "odps:Describe",
        "odps:Select"
```

`],`

```json
      "Resource": [
        "acs:odps:*:projects/$user_project_name/tables/a",
        "acs:odps:*:projects/$user_project_name"
```

`],`

```json
      "Condition": {
        "StringEquals": {
          "odps:TaskType": [
            "SQL"
```

]

```
        }
      }
    }
```

]

```
}
```

**说明**

上述代码的目的是禁用 $user_project_name 的Tunnel功能，并且仅授予您对此Project及该项目中表a的List、Read、Describe及Select权限。

#### 4.4.4. 查看权限

MaxCompute支持使用命令查看用户的权限，方便您快速了解用户所拥有的操作权限，便于进行权限管理。

**查看命令**

如果想查看某个用户的权限，可以执行如下命令。

```
SHOW grants FOR $user_name;
```

**说明**

关于查看权限的详细介绍请参见权限查看。

### 创建角色及授权

当项目空间中用户数量较多时，逐个授权将非常繁琐。为此，项目管理员可将具有相同权限需求的用户归类为角色，通过为角色统一授权，其下所有用户自动继承相应权限。本文介绍如何创建角色并为其分配权限。

**用户与角色的关联规则**

多个用户可以同时存在于一个角色下，一个用户也可以隶属于多个角色。

**创建角色**

**命令格式**

```
CREATE role <roleName>;
```

**使用示例**

```
CREATE role player;
```

**将角色授予用户**

**命令格式**

```
GRANT <roleName> TO <full_username>;
```

**使用示例**

```
GRANT player TO bo***@aliyun.com;
```

**删除角色**

**命令格式**

```
DROP role <roleName>;
```

**使用示例**

```
DROP role player;
```

**说明**

删除弃用的角色前，请确认所有该角色下的用户都已经被移出该角色。

**角色授权**

角色授权与用户授权类似，对角色进行授权的操作请参见用户授权及权限查看。更多有关角色授权的介绍请参见角色管理。

### 创建及删除表

#### 4.6.1. 创建表

本文介绍MaxCompute中创建表的语法与常用示例，包括创建普通表、分区表、带生命周期的表，以及通过 `LIKE` 或 `AS SELECT` 方式复制表结构或数据，方便您快速构建符合业务需求的数据表，提升建表效率与开发体验。

**命令格式**

```
CREATE TABLE [IF NOT EXISTS] table_name [(col_name data_type [comment col_comment], ...)] [comment table_comment] [PARTITIONED BY (col_name data_type [comment col_comment], ...)] [lifecycle days] [AS select_statement]
```

`--` 或者。

```
CREATE TABLE [IF NOT EXISTS] table_name LIKE existing_table_name;
```

**使用示例**

`--` 创建非分区表。

```
CREATE TABLE test1 (key string);
```

`--` 创建分区表。

```
CREATE TABLE test2 (key bigint) PARTITIONED BY (pt string, ds string);
```

`--` 创建带有生命周期的表。

```
CREATE TABLE test3 (key boolean) PARTITIONED BY (pt string, ds string) lifecycle 100;
```

`--` 除生命周期属性外，`test4`的其他属性（字段类型、分区类型等）均与`test3`完全一致。

```
CREATE TABLE test4 LIKE test3;
```

`--` 创建`test5`，但分区、生命周期信息不会被拷贝到目标表中。且仅会将`test2`的数据复制到`test5`中。

```
CREATE TABLE test5 AS SELECT * FROM test2;
```

**表的分区与生命周期管理**

MaxCompute的表支持分区、生命周期。 创建表的详细介绍请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > DDL****语句** > **表操作** > **创建表**章节。 修改分区请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > DDL****语句** > **列及分区操作**的**添加分区**或**删除分区**章节。 修改生命周期请参见**MaxCompute SQL > DDL****语句** > **表操作** > **修改表的生命周期属性**章节。

#### 4.6.2. 获取表信息

本文介绍如何使用 `DESC` 命令查看MaxCompute表的结构信息，包括字段、分区及生命周期等元数据，帮助您快速了解表的基本定义。

**命令格式**

```
DESC <table_name>;
```

**使用示例**

`--`获取`test3`信息。

```
DESC test3;
```

`--`获取`test4`信息。

```
DESC test4;
```

#### 4.6.3. 删除表

本文介绍如何使用 `DROP TABLE` 命令删除MaxCompute表，并提供基本操作示例。

**命令格式**

```
DROP TABLE [IF EXISTS] table_name;
```

**使用示例**

```
DROP TABLE test2;
```

**说明**

更多介绍请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > DDL****语句** > **表操作** > **删除表**章节。

### 导入导出数据

MaxCompute支持通过Tunnel SDK自行编写Java程序，方便您灵活、高效地实现数据的导入与导出。

**相关操作**

### 运行SQL

**4.8.1. 概述**

本文介绍了MaxCompute SQL使用中的关键注意事项，方便您避免语法迁移错误并合理预期查询性能。

**注意事项**

MaxCompute SQL使用中的具体注意事项如下：

**说明**

具体的SQL使用及运行请参见《**MaxCompute****开发指南》**的**MaxCompute SQL**章节。 MaxCompute SQL语法与Oracle、MySQL有一定差别，无法将其他数据库中的SQL语句直接迁移到MaxCompute中。 在使用方式上，MaxCompute SQL无法满足实时查询需求，查询计算时间在分钟或秒级别，无法在毫秒级别返回结果。

#### 4.8.2. Select语句

本文介绍了MaxCompute中SELECT语句的使用限制，方便您正确编写符合语法规范的SQL语句，避免因SQL解析顺序或列引用方式不当而引发错误。

**使用限制**

Group by语句的Key可以是输入表的列名，也可以是由输入表的列构成的表达式，不可以是Select语句的输出列。

```
SELECT substr(col2, 2) FROM tbl GROUP BY substr(col2, 2);
```

`--` 可以，`Group by`的`Key`可以是输入表的列构成的表达式。

```
SELECT col2 FROM tbl GROUP BY substr(col2, 2); SELECT substr(col2, 2) AS c FROM tbl GROUP BY c;
```

**说明**

通常在SQL解析中，Group by的操作先于Select操作，因此Group by只能接受输入表的列或表达式为Key。 Order by/Sort by/Distribute by的Key必须是Select语句的输出列，即列的别名。

```
SELECT col2 AS c FROM tbl ORDER BY col2 limit 100; SELECT col2 FROM tbl ORDER BY col2 limit 100;
```

**说明**

通常在SQL解析中，Order by/Sort by/Distribute by的操作位于Select操作之后，因此只能接受Select语句的输出列为Key。 `Order by` 不和 `Distribute by` 、 `Sort by` 同时使用， `Group by` 也不和 `Distribute by` 、 `Sort by` 同时使用。 更多Select语句详情请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > DML****语句** **> SELECT****语句**章节。

#### 4.8.3. Insert语句

本文介绍了MaxCompute中INSERT语句的使用限制，方便您正确处理静态与动态分区插入操作，避免因分区列在SELECT列表中的错误使用而导致任务失败。

**使用限制**

向某个分区插入数据时，分区列不可以在SELECT列表中出现。

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2026',region='china') SELECT shop_name, customer_id, total_price, sale_ date, region FROM sale_detail;
```

`--` 返回失败，`sale_date, region`为分区列，不可以出现在静态分区的`INSERT`语句中。 向动态分区插入数据时，动态分区列必须在SELECT列表中。

```
INSERT OVERWRITE TABLE sale_detail_dypart PARTITION (sale_date='2026', region) SELECT shop_name,customer_id,total_price FROM sale_detai l;
```

`--` 返回失败，向动态分区插入数据时，动态分区列必须在`SELECT`列表中。 更多Insert语句详情请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > DML****语句** **> INSERT****语句**章节。

#### 4.8.4. Join语句

本文介绍了MaxCompute中JOIN语句的使用限制，包括支持的连接类型及并发JOIN操作的约束，帮助您合理设计查询逻辑，确保SQL语句符合平台规范。

**使用限制**

MaxCompute SQL支持的Join操作类型包括：{LEFT OUTER|RIGHT OUTER|FULL OUTER|INNER|NATURAL} JOIN以及隐式连接。 MaxCompute SQL目前最多支持128个并发Join操作。 更多Join语句详情请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > DML****语句** **> SELECT****语句** **> JOIN**章节。

**4.8.5. 其他**

本文为您介绍MaxCompute SQL的其他使用限制，帮助您合理规划作业结构，防止因超出并发上限（如UNION或INSERT操作超过系统支持的最大数量）导致任务提交失败或执行异常。

**使用限制**

MaxCompute SQL目前最多支持256个并发Union操作。 MaxCompute SQL目前最多支持256个并发Insert overwrite|into操作。

### 编写并使用UDF

**4.9.1. 概述**

本文介绍MaxCompute UDF（包括UDF、UDAF和UDTF）的编写、注册与使用方法，方便您快速开发和部署自定义函数，扩展SQL处理能力。

**UDF介绍**

MaxCompute UDF：包括UDF、UDAF和UDTF三种函数。 创建方法：如果您想编写UDF程序，可以通过添加资源的方式将UDF代码上传到项目空间中，使用注册函数语句创建UDF。 代码示例：

#### 4.9.2. UDF示例

本文介绍MaxCompute UDF的完整开发流程（包括编写、打包、添加资源、注册函数及调用），并提供参考示例，方便您快速上手开发和使用自定义函数，扩展SQL 处理能力。

**操作步骤**

1. 编写代码。
您需要按照MaxCompute UDF框架的规定，实现函数功能，并进行编译。

```java
package org.alidata.odps.udf.examples; import com.aliyun.odps.udf.UDF; public final class Lower extends UDF {
    public String evaluate(String s) {
        if (s == null) {
            return null;
        }
        return s.toLowerCase();
    }
}
```

将上述JAR包命名为my_lower.jar。
2. 添加资源。
在运行UDF之前，必须指定引用的UDF代码。您的代码需要通过资源的形式添加到MaxCompute中。Java UDF必须被打成JAR包，以JAR资源的方式添加到 MaxCompute中。UDF框架会自动加载JAR包，运行您自定义的UDF。 添加JAR资源的示例命令如下。

```
ADD jar my_lower.jar;
```

**说明**

如果存在同名的资源，请重新命名JAR包，并注意修改下面示例命令中相关JAR包的名字；也可以直接使用-f选项覆盖原有的JAR资源。
3. 注册UDF函数。
您的JAR包被上传后，由于MaxCompute中并没有关于这个UDF的任何信息，因此需要在MaxCompute中注册一个唯一的函数名，并指定该函数名与JAR资源及对应资源中函数的对应关系。 注册UDF函数的示例命令如下。

```
CREATE FUNCTION test_lower AS org.alidata.odps.udf.examples.Lower USING my_lower.jar;
```

在SQL中使用此函数的示例如下。

```
SELECT test_lower('A') FROM my_test_table;
```

#### 4.9.3. UDAF示例

本文提供了一个UDAF开发示例，供您参考并用于相关函数的开发。

**示例代码**

UDAF的注册方式与UDF基本相同，使用方式与内建函数中的聚合函数相同。具体示例代码如下。

```java
package org.alidata.odps.udf.examples; import com.aliyun.odps.io.LongWritable; import com.aliyun.odps.io.Text; import com.aliyun.odps.io.Writable; import com.aliyun.odps.udf.Aggregator; import com.aliyun.odps.udf.UDFException; /**
 * project: example_project
 * table: wc_in2
 * partitions: p2=1,p1=2
 * columns: colc,colb,cola
```

`*/`

```java
public class UDAFExample extends Aggregator {
  @Override
  public void iterate(Writable arg0, Writable[] arg1) throws UDFException {
    LongWritable result = (LongWritable) arg0;
    for (Writable item : arg1) {
      Text txt = (Text) item;
      result.set(result.get() + txt.getLength());
    }
  }
  @Override
  public void merge(Writable arg0, Writable arg1) throws UDFException {
    LongWritable result = (LongWritable) arg0;
    LongWritable partial = (LongWritable) arg1;
    result.set(result.get() + partial.get());
  }
  @Override
  public Writable newBuffer() {
    return new LongWritable(0L);
  }
  @Override
  public Writable terminate(Writable arg0) throws UDFException {
    return arg0;
  }
}
```

#### 4.9.4. UDTF示例

本文提供了一个UDTF开发示例，供您参考并用于相关函数的开发。

**示例代码**

UDTF的注册方式与UDF基本相同，使用方式也与UDF相同。具体示例代码如下。

```java
package org.alidata.odps.udtf.examples; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.UDTFCollector; import com.aliyun.odps.udf.annotation.Resolve; import com.aliyun.odps.udf.UDFException; @Resolve({"string,bigint->string,bigint"}) public class MyUDTF extends UDTF{
    @Override
    public void process(Object[] args) throws UDFException {
        String a = (String) args[0];
        long b = (long) args[1];
        for (String t: a.split("\\s+")) {
            forward(t, b);
        }
    }
}
```

### 编写并运行MapReduce

**前提条件**

已安装JDK1.8版本。

**操作步骤**

**步骤一：准备数据环境**

1. 创建输入输出表。
建表语句示例如下。

```
CREATE TABLE wc_in (key string, value string); CREATE TABLE wc_out (key string, cnt bigint);
```

**说明**

创建表的语句请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > DDL****语句** > **表操作** > **创建表**章节。
2. 在表wc_in中插入数据。
您可以通过以下两种方式插入数据： 使用Tunnel命令上传数据。 需要插入的数据如下所示，请在本地创建kv.txt文件保存数据，假设kv.txt文件本地存放路径为D:\。

```
238,val_238 186,val_86 186,val_86
```

执行如下命令，上传数据。

```
Tunnel upload D:\kv.txt wc_in;
```

执行如下SQL语句直接插入数据。

```
INSERT INTO TABLE wc_in VALUES ('238','val_238'),('186','val_86'),('186','val_86');
```

1. 编写MaxCompute程序并编译。
MaxCompute为您提供了便捷的Eclipse开发插件，方便您快速开发MapReduce程序，并提供了本地调试MapReduce的功能。 您需要先在Eclipse中创建一个MaxCompute工程，而后在此工程中编写MapReduce程序。本地调试通过后，将编译好的程序（JAR包）上传至MaxCompute。
2. 添加JAR包到Project资源。
假设当前JAR包名为**word-count-1.0.jar**，示例如下。

```
ADD jar word-count-1.0.jar;
```

**步骤三：运行Jar包并查看结果**

1. 在MaxCompute客户端运行JAR命令。

```
jar -resources word-count-1.0.jar -classpath /home/resources/word-count-1.0.jar com.taobao.jingfan.wordcount wc_in wc_out;
```

**说明**

如果在Java程序中使用了任何资源，请务必将此资源加入**-resources**参数。
2. 在MaxCompute客户端查看结果。

```
SELECT * FROM wc_out;
```

## 基本概念及常用命令

### 基本概念

本文将为您介绍MaxCompute的基本概念，帮助您快速了解其核心要点。

**项目空间（Project）**

项目空间（Project）是MaxCompute的基本组织单元，它类似于传统数据库的Database或Schema的概念，是进行多用户隔离和访问控制的主要边界。一个用户可以同时拥有多个项目空间的权限。通过安全授权，可以在一个项目空间中访问另一个项目空间中的对象，例如：表（Table）、资源（Resource）、函数 （Function）和实例（Instance）。

| 您可以通过 | USE project | 命令进入一个项目空间，示例如下。 |
|---|---|---|
| -- 进入一个名为al_project的项目空间。 USE al_project; |  |  |

**说明**

运行上述命令后，您会进入一个名为 `al_project` 的项目空间，从而可以操作该项目空间下的对象，而不需要关心操作对象所在的项目空间。

**表**

表是MaxCompute的数据存储单元。它在逻辑上也是由行和列组成的二维结构，每行代表一条记录，每列表示相同数据类型的一个字段，一条记录可以包含一个或多个列，各个列的名称和类型构成这张表的Schema。 在MaxCompute中，所有的数据都被存储在表中，表中的列可以是MaxCompute支持的任意一种数据类型。MaxCompute中的各种不同类型计算任务的操作对象 （输入、输出）都是表。您可以创建表、删除表以及向表中导入数据。 为了提高处理效率，可以在创建表时指定表的分区（Partition），即指定表内的某些字段作为分区列。在大多数情况下，您可以将分区类比为文件系统下的目录。 MaxCompute将分区列的每个值作为一个分区（目录）。您可以指定多级分区，即将表的多个字段作为表的分区，分区之间类似多级目录的关系。在使用数据时如果指定了需要访问的分区名称，则只会读取相应的分区，避免全表扫描，提高处理效率。

#### 数据类型

MaxCompute表中的列必须是下列描述的任意一种类型，MaxCompute支持的基本数据类型的描述及取值范围，如下表所示。

**基本数据类型**

| 类型 | 是否为MaxCompute2.0新增类型 | 常量定义 | 描述 | 取值范围 |
|---|---|---|---|---|
| TINYINT | 是 | 1Y,-127Y | 8位有符号整型。 | -128~127 |
| SMALLINT | 是 | 32767S,-100S | 16位有符号整型。 | -32768~32767 |
| INT | 是 | 1000,-15645787 | 32位有符号整型。 | -231~231-1 |
| BIGINT | 否 | 100000000000L,-1L | 64位有符号整型。 | -263+1~263-1 |
| STRING | 否 | "abc",'bcd',"alibaba",'inc' | 字符串，支持UTF-8编码。其他编码的字符行为未定义。 | 单个STRING列最长允许8MB |
| FLOAT | 是 | 无 | 32位二进制浮点型。 | 不涉及 |
| BOOLEAN | 否 | True,False | 布尔型。 | True或False |
| DOUBLE | 否 | 3.1415926 1E+7 | 64位二进制浮点型。 | -1.010308~1.010308 |
| DATETIME | 否 | Datetime '2017-11-11 00:00:00' | 日期时间类型。使用东八区时间作为系统标准时间。 | 0001-01-01 00:00:00.000~9999-12-31 23:59:59.999 |
| DECIMAL | 否 | 3.5BD,99999999999.9999999B D | 10进制精确数字类型。 | 整型部分：-1036+1~1036-1 小数部分：精确到10-18 |
| VARCHAR | 是 | 无 | 变长字符类型，n为长度。 | 1~65535 |
| CHAR | 是 | 无 | 固定长度字符类型，n为长度。长度不足时会填充空格，但空格不参与比较。 | 1~255 |
| BINARY | 是 | 无 | 二进制数据类型。 | 单个BINARY列最长允许8MB |

| TIMESTAMP | 是 | Timestamp '2017-11-11 00:00:00.123456789' | 与时区无关的时间戳类型。 | 0001-01-01 00:00:00.000000000~999 9-12-31 23:59:59.999999999 |
|---|---|---|---|---|

**开启新增数据类型设置**

需要注意，如果您需要使用MaxCompute 2.0的新增数据类型，使用前，请先完成以下Session级别或Project级别使用开关设置。
**Session****级别**： set odps.sql.type.system.odps2=true;
**Project****级别**： setproject odps.sql.type.system.odps2=true;
否则可能产生如下报错： `xxxx type is not enabled in current mode` 。同时，上述的各种数据类型均可为NULL。

**说明**

上面的两个设置仅支持字母小写。

**新增数据类型注意事项**

新增数据类型相关的使用注意事项如下。 进行 set odps.sql.type.system.odps2=true; （Session级别）设置，即打开新增数据类型使用开关后，会带来的主要影响如下： 关键字 `INT` 语义的变化。打开新增数据类型使用开关后SQL中的 `INT` 关键字是指32位整型。

| Select 1 + a; |  |
|---|---|
|  | BIGINT |

打开新增数据类型使用开关后，整型常量会优先被解释为 `INT` 类型，1就是32位整型的1。 整型常量被解释为 `INT` 类型后，会导致后续一些操作调用到的函数原型不一致；同时，落盘（即写入磁盘）后生成的新增数据类型表会导致周边工具以及后续作业的行为改变。 隐式类型转换规则变化。

| STRING->DATETIME |  |
|---|---|
| 情况可以通过 | CAST |

隐式类型转换影响最大的地方是函数调用和 `INSERT` ，未开启新增数据类型使用开关时能执行通过的SQL，在开启后执行会报错。 部分以新增数据类型作为参数和返回值的操作以及内置函数，在未打开新增数据类型使用开关时会被直接忽略，而打开新数据类型使用开关后则可以使用。其中： 一些内置函数必须打开新增数据类型使用开关才能使用，例如返回INT类型的函数（接受INT作为参数的内置函数，基本都有BIGINT的重载），

```
如 YEAR 、 QUARTER 、 MONTH 、 DAY 、 HOUR 、 MINUTE 、 SECOND 、 MILLISECOND 、 NANOSECOND 、 DAYOFMONTH 和 WEEKOFYEAR 等。
```

这些函数实际上可以用内置函数中日期函数里的DATEPART来实现。 UDF的Resolve不一致。 `BIGINT` 关键字的解析不一样。 分区列的类型支持不同：

| 只有 | STRING |  | 一种。 |
|---|---|---|---|
| STRING |  | 、 VARCHAR |  |

未打开新增数据类型使用开关时，存在一种特殊的处理：Insert操作中的分区字段，要当作STRING类型来处理。 集合操作中最后的 `Limit` 语句行为变更。 例如以下语句：

```
SELECT * FROM t1 UNION ALL SELECT * FROM t2 limit 10;
```

未打开新增数据类型使用开关前：

```
SELECT * FROM t1 UNION ALL SELECT * FROM ( SELECT * FROM t2 limit 10) t2;
```

打开新增数据类型使用开关后：

```
SELECT * FROM (SELECT * FROM t1 UNION ALL SELECT * FROM t2 ) limit 10;
```

具有相同行为的操作，除了交集、并集和补集、Intersect以及Except等集合操作，还有Order by、Distribute by、Sort by和Cluster by这几个操作。 IN表达式的类型解析不同。 例如 `a in (1, 2, 3)` ： 未打开新增数据类型使用开关时，要求IN后面的括号里的所有值，其类型必须一致。 打开新增数据类型使用开关后，要求IN后面的括号里的所有值，其支持的隐式类型转换一致。 对于INT类型常量，如果超过INT类型取值范围，会转换为BIGINT类型；如果超过BIGINT类型取值范围，会转换为DOUBLE类型。MaxCompute在未设定 `odps.sql.type.system.odps2` 为True的情况下，保留此转换，但会报告一个警告，提示INT类型被当作BIGINT类型处理了。如果您的脚本有此种情况，建议全部改写为BIGINT类型，避免混淆。 VARCHAR类型常量可通过STRING类型常量的隐式转换表示。 STRING类型常量支持连接，例如 `'abc''xyz'` 会解析为 `'abcxyz'` ，不同部分可以写在不同行上。 目前查询显示的时间值不包含毫秒。而通过Tunnel命令中的 `-dfp` 参数来指定时间格式，是可以指定到毫秒显示的。 MaxCompute支持的复杂数据类型的定义及构造方法，如下表所示。

| 类型 | 定义方法 | 构造方法 |
|---|---|---|
| ARRAY | array< int >; array< struct< a:int, b:string >> | array(1, 2, 3); array(array(1, 2); array(3, 4)) |
| MAP | map< string, string >; map< smallint, array< string>> | map("k1", "v1","k2", "v2"); map(1S, array('a', 'b'), 2S, array('x', 'y')) |
| STRUCT | struct< x:int, y:int>; struct< field1:bigint, field2:array< int>, field3:map< int, int>> | namedstruct('x', 1, 'y', 2); _ namedstruct('field1', 100L, 'field2', array(1, 2), 'field3', map(1, 100, _ 2, 200) |
| JSON | JSON | JSON '123' |

**开启新数据类型开关**

如果通过Execute_sql方式调用，可以执行 o.execute_sql('set odps.sql.type.system.odps2=true;query_sql',hints=

```json
{"odps.sql.submit.mode":"script"}) 进行设置。
```

如果通过DataFrame调用，例如Persist、Execute、To_pandas等立即执行方法，可以通过Hints参数设置。下图中设置方法仅针对单个作业生效。 如果通过DataFrame调用，且需要全局生效，需要使用Option参数进行设置 `options.sql.use_odps2_extension=True` 。

**资源**

**资源概念**

资源（Resource）是MaxCompute的特有概念。您如果想使用MaxCompute的自定义函数（UDF）或MapReduce功能需要依赖资源来完成： MaxCompute SQL UDF：您在编写UDF后，需要将编译好的JAR包作为资源上传到MaxCompute。运行UDF时，MaxCompute会自动下载这个JAR包，获取您的代码，从而运行UDF，无需您干预。上传JAR包的过程就是在MaxCompute上创建资源的过程，这个JAR包是MaxCompute资源的一种。 MaxCompute MapReduce：您在编写MapReduce程序后，将编译好的JAR包作为资源上传到MaxCompute。运行MapReduce作业时，MapReduce框架会自

**说明**

MaxCompute的自定义函数（UDF）或MapReduce对资源的读取有一定的限制，详情请参见应用限制。 您也可以将文本文件以及MaxCompute中的表作为不同类型的资源上传到MaxCompute。您可以在UDF及MapReduce的运行过程中读取、使用这些资源，MaxCompute提供了读取、使用资源的接口。详细示例请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > UDF > Java UDF >**
**UDTF > UDTF****使用示例**章节。

**资源类型**

MaxCompute资源的类型包括： FILE类型。 TABLE类型：MaxCompute中的表。 JAR类型：编译好的Java JAR包。 ARCHIVE类型：通过资源名称中的后缀识别压缩类型，支持的压缩文件类型包括ZIP、TGZ、TAR和JAR。 PY类型：Python脚本，供Python UDF使用。

**说明**

有关资源的操作介绍请参见资源操作。 MaxCompute为您提供了SQL计算功能，您可以在MaxCompute SQL中使用系统的内建函数完成一定的计算和计数功能。当内建函数无法满足要求时，您可以使用 MaxCompute提供的Java编程接口开发自定义函数（User Defined Function，以下简称UDF）。自定义函数（UDF）又可以进一步分为标量值函数（UDF）、自定义聚合函数（UDAF）和自定义表值函数（UDTF）三种。 您在开发完成UDF代码后，需要将代码编译成JAR包，并将此JAR包以JAR资源的形式上传到MaxCompute，最后在MaxCompute中注册此UDF。在使用UDF时，只需要在SQL中指明UDF的函数名及输入参数即可，使用方式与MaxCompute提供的内建函数相同。

**说明**

有关UDF的操作介绍请参见函数操作。

**任务**

任务（Task）是MaxCompute的基本计算单元。SQL及MapReduce功能都是通过任务（Task）完成的。对于您提交的大多数任务，特别是计算型任务（例如SQL DML语句、MapReduce等），MaxCompute会对其进行解析，得出任务的执行计划。 执行计划是由具有依赖关系的多个执行阶段（Stage）构成的。目前，执行计划逻辑上可以被看做一个有向图，图中的点是执行阶段，各个执行阶段的依赖关系是图的边。MaxCompute会依照图（执行计划）中的依赖关系执行各个阶段。在同一个执行阶段内，会有多个进程，也称之为Worker，共同完成该执行阶段的计算工作。同一个执行阶段的不同Worker只是处理的数据不同，执行逻辑完全相同。 计算型任务在执行时，会被实例化，您可以操作这个实例（Instance）的信息，例如：获取实例状态（Status Instance）、终止实例运行（Kill Instance）等。 另一方面，部分MaxCompute任务并不是计算型的任务（例如SQL DDL语句），这些任务本质上仅需要读取、修改MaxCompute中的元数据信息。因此，这些任务无法被解析出执行计划。

**重要**

在MaxCompute中，并不是所有的请求都会被转化为任务（Task），例如项目空间（Project）、资源（Resource）、自定义函数（UDF）及实例（Instance） 的操作就不需要通过MaxCompute的任务来完成。

#### 任务实例

在MaxCompute中，部分任务（Task）在执行时会被实例化，以MaxCompute实例（后续章节简称实例或Instance）的形式存在。实例会经历运行（Running）及结束（Terminated）两个阶段。运行阶段的状态为Running（运行中），而结束阶段的状态将会是Success（成功）、Failed（失败）或Canceled（被取消）。您可以根据运行任务时MaxCompute给出的实例ID查询、改变任务的状态，示例如下。

```
status <instance_id>;
```

`--` 查看某实例的状态。

```
kill <instance_id>;
```

`--` 停止某实例，将其状态设置为`Canceled`。

**资源配额**

资源配额（Quota）分为存储和计算两种。对于存储资源，在MaxCompute中可以设置一个Project中允许使用的存储上限，在接近上限到一定程度时会触发告警。对于计算资源的限制，有内存和CPU两方面，即在Project中同时运行的进程所占用的内存和CPU资源不可以超过指定的上限。

**ACID语义**

此处主要介绍MaxCompute在作业并发情况下ACID的语义。

**相关术语**

操作：指在MaxCompute上提交的单个作业。 数据对象：指持有实际数据的对象，例如非分区表、分区表。 INTO类作业：INSERT INTO、DYNAMIC INSERT INTO等。 OVERWRITE类作业：INSERT OVERWRITE、DYNAMIC INSERT OVERWRITE等。 Tunnel数据上传：可归结为INTO类或OVERWRITE类作业。

**ACID语义描述**

原子性（Atomicity）：一个操作要么全部完成，要么全部不完成，不会结束在中间某个环节。 一致性（Consistency）：从操作开始至结束的期间，数据对象的完整性没有被破坏。 隔离性（Isolation）：操作独立于其它并发操作完成。 持久性（Durability）：操作处理结束后，对数据的修改将永久有效，即使出现系统故障，该修改也不会丢失。

**MaxCompute的ACID具体说明**

| 特性 | 说明 |
|---|---|
| 原子性（Atomicity） | 任何时候MaxCompute会保证在冲突时只有一个作业成功，其他冲突作业失败。 对于单个表/分区的CREATE/OVERWRITE/DROP操作，保证其原子性。 跨表操作时不支持原子性（例如MULTI-INSERT）。 在极端情况下，以下操作可能不保证原子性： DYNAMIC INSERT OVERWRITE多于一万个分区，不支持原子性。 INTO类操作：这类操作的失败的原因是事务回滚时数据清理失败，但不会造成原始数据丢失。 |
| 一致性（Consistency） | OVERWRITE类作业可保证一致性。 INTO类作业在冲突失败后可能存在失败作业的数据残留。 |
| 隔离性（Isolation） | 非INTO类操作保证读已提交。 INTO类操作存在读未提交的场景。 |
| 持久性（Durability） | MaxCompute保证数据的持久性。 |

### 常用命令

**5.2.1. 概述**

MaxCompute提供了对项目空间、表、资源及实例等对象的一系列操作，您可以通过客户端命令及SDK来操作这些对象。 为了帮助您快速了解MaxCompute，下面的章节将详细介绍如何通过客户端使用这些命令。

**说明**

对于SDK的更多介绍请参见《**MaxCompute****开发指南》**的**Java SDK**章节。

#### 5.2.2. 项目空间操作

**创建及删除项目空间**

MaxCompute没有提供创建及删除项目空间的命令，您可以通过Apsara Uni-manager控制台完成项目空间的创建和删除。 创建项目空间的具体操作请参见创建项目。 如果您需要删除项目空间，在Apsara Uni-manager运营控制台上，进入**大数据计算** **MaxCompute**产品后，单击**Project****管理**，在**Project****管理**页面中找到对应项目空间的**操作**列，单击**删除**即可。

**进入项目空间**

**命令格式**

```
USE <project_name>;
```

**用途**

进入指定项目空间。进入该空间后可以直接操作该项目空间下的所有对象。

**说明**

项目空间不存在或当前用户不在此项目空间中时，会返回异常并退出。

**使用示例**

| 访问名称为 | my_project | 的项目。 |
|---|---|---|
| USE my_project; |  |  |

**说明**

上述示例是在客户端中运行此命令时的示例。 且 `my_project` 为您拥有访问权限的项目。 所有的MaxCompute命令关键字、项目空间名、表名和列名均对大小写不敏感。

| 假设查看 | my_project | 项目空间下的表test src，可运行如下命令： _ |
|---|---|---|
| SELECT * FROM test_src; |  |  |

MaxCompute会自动搜索项目空间 `my_project` 下的表。如果存在此表，返回表中的数据，如果不存在此表，则返回异常并退出。 如果在my_project下想要访问另一项目空间 `my_project2` 下的表 `test_src` ，则需要指定项目空间名，如下所示。

```
SELECT * FROM my_project2.test_src;
```

此时返回 `my_project2` 项目空间下的数据结果，而不是my_project下的test_src表数据。

**查询项目空间**

**命令格式**

```
LIST projects;
```

**用途**

查看MaxCompute中的所有Project。

**回收项目空间垃圾**

查看空间垃圾的命令格式如下。

```
SHOW recyclebin;
```

用途：列出本Project中的对象明细。

**说明**

只有Project Owner有权限执行此命令。 清空回收站中所有项目的命令格式如下。

```
purge ALL;
```

用途：清空本Project下回收站中所有对象，释放存储空间。

**说明**

只有Project Owner有权限执行此命令。 回收某张表的命令格式如下。

```
purge TABLE tblname;
```

用途：清空指定表名对象在回收站中的记录，释放存储空间。

**说明**

当指定名称的表存在时，仅Project Owner或对该表具有写权限的用户可执行此命令。 当表已被删除时，只有Project Owner有权限执行此命令。

#### 5.2.3. 表操作

本文介绍MaxCompute项目空间的常用管理操作，包括创建与删除项目、切换项目、查看项目列表以及回收站管理，帮助您高效管理项目资源。

**Create Table**

**命令格式**

```
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name [(col_name data_type [DEFAULT value] [COMMENT col_comment], ...)] [COMMENT table_comment] [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)] [LIFECYCLE days]; CREATE TABLE [IF NOT EXISTS] table_name [AS select_statement | LIKE existing_table_name];
```

**用途**

创建一张MaxCompute表。

**使用示例**

如果没有同名表存在，创建一张分区表sale_detail。

```
CREATE TABLE IF NOT EXISTS sale_detail (
    shop_name     STRING,
    customer_id   STRING,
    total_price   DOUBLE
```

)

```
PARTITIONED BY (
    sale_date STRING,
    region    STRING
);
```

**说明**

表名与列名均对大小写不敏感。 表名和列名中不能有特殊字符，只能使用英文的a~z、A~Z及数字和下划线（_），且以字母开头，名称的长度不超过128字节，否则报错。 注释内容是长度不超过1024字节的有效字符串，否则报错。 对于该命令更详细的介绍请参见《**MaxCompute****开发指南》**的**MaxCompute SQL > DDL****语句** > **表操作** > **创建表**章节。

**ChangeOwner**

**命令格式**

```
ALTER TABLE table_name CHANGEOWNER TO new_owner;
```

**用途**

修改表的所有者（表Owner）。

**使用示例**

| 示例如下，将表 | test1 | 的所有者修改为 | ALIYUN$xxx@aliyun.com | 。 |
|---|---|---|---|---|
| ALTER TABLE test1 CHANGEOWNER to 'ALIYUN$xxx@aliyun.com'; |  |  |  |  |

**Drop Table**

**命令格式**

```
DROP TABLE [IF EXISTS] table_name;
```

参数说明如下。 `table_name` ：要删除的表名。

**用途**

删除一张表。

**说明**

如果不指定IF EXISTS选项而表不存在，则返回异常；如果指定IF EXISTS选项，无论表是否存在，均返回成功。

**使用示例**

```
DROP TABLE sale_detail;
```

`--` 如果表存在，返回删除成功。

```
DROP TABLE IF EXISTS sale_detail;
```

`--` 无论是否存在`sale_detail`表，均返回删除成功。

**查看表信息**

**命令格式**

```
DESC <table_name>;
```

`--` 查看表或视图信息。

```
DESC extended <table_name>;
```

`--` 查看外部表信息。 参数说明如下。 `table_name` ：第一条命令中是表名或视图名称。第二条命令中是外部表名称。

**用途**

返回指定表的信息，包括Owner（表的拥有人）、Project（表所属的项目空间）、CreateTime（创建时间）、LastDDLTime（最后一次DDL操作时间）、 LastModifiedTime（表中的数据最后一次被改动的时间）、InternalTable（表示被描述的对象是表，总是显示YES）、Size（表数据所占存储容量的大小，单位 Byte）、Native Columns（非分区列的信息，包括列名、类型和备注）、Partition Columns（分区列信息，包括分区名、类型和备注）以及Extended Info（外部表StorageHandler 、Location等信息）。

**使用示例**

执行如下命令，查看一张分区表。

```
DESC sale_detail;
```

返回结果如下。

```
+------------------------------------------------------------------------------------+
| Owner: ALIYUN$odpsu***@aliyun.com | Project: test_project                          |
| TableComment:                                                                      |
+------------------------------------------------------------------------------------+
| CreateTime:               2014-01-01 17:32:13                                      |
| LastDDLTime:              2014-01-01 17:57:38                                      |
| LastModifiedTime:         1970-01-01 08:00:00                                      |
+------------------------------------------------------------------------------------+
| InternalTable: YES      | Size: 0                                                  |
+------------------------------------------------------------------------------------+
| Native Columns:                                                                    |
+------------------------------------------------------------------------------------+
| Field           | Type       | Comment                                             |
+------------------------------------------------------------------------------------+
| shop_name       | string     |                                                     |
| customer_id     | string     |                                                     |
| total_price     | double     |                                                     |
+------------------------------------------------------------------------------------+
| Partition Columns:                                                                 |
+------------------------------------------------------------------------------------+
| sale_date       | string     |                                                     |
| region          | string     |                                                     |
+------------------------------------------------------------------------------------+
```

**说明**

如果是不带分区的表，将不会显示 `Partition Columns` 相关信息。 如果描述的是一个视图（View），将不显示 `InternalTable` 选项，而是显示 `VirtualView` 选项，其值总是为 `YES` 。与此类似， `Size` 选项将会被 `ViewText` 选项替代，表示 `View` 的定义，例如 `SELECT * FROM src` 。关于视图的介绍请参见《**MaxCompute****开发指南》**的**MaxCompute**
**SQL > DDL****语句** > **视图操作** > **创建视图**章节。

**查看分区信息**

**命令格式**

```
DESC table_name PARTITION(pt_spec);
```

**用途**

查看某个分区表具体的分区信息。

**使用示例**

执行如下命令，查看分区信息。

```
DESC meta.m_security_users PARTITION (ds='20151010');
```

返回结果如下。

```
+------------------------------------------------------------------------------------+
| PartitionSize: 2109112                                                             |
+------------------------------------------------------------------------------------+
| CreateTime:               2015-10-10 08:48:48                                      |
| LastDDLTime:              2015-10-10 08:48:48                                      |
| LastModifiedTime:         2015-10-11 01:33:35                                      |
+------------------------------------------------------------------------------------+
```

`OK`

**Show Tables和Show Tables like**

**命令格式**

```
SHOW TABLES; SHOW TABLES LIKE 'chart';
```

**用途**

| SHOW TABLES | ：列出当前项目 |
|---|---|
| SHOW TABLES LIKE 'chart' |  |

**使用示例**

执行如下命令，列出当前项目空间下所有的表。

```
SHOW TABLES;
```

执行如下命令，列出当前项目空间下表名与**ods_brand**匹配上的表。

```
SHOW tables LIKE 'ods_brand*';
```

返回结果如下。

```
ALIYUN$odps_u***@aliyun.com:ods_brand ......
```

**说明**

`odps_u***@aliyun.com` 是用户名，表示该表的创建者。 `ods_brand` 是表名称。

**Show Partitions**

**命令格式**

```
SHOW PARTITIONS <table_name>;
```

参数说明如下。 `table_name` ：指定查询的表名称，表不存在或为非分区表时报错。

**用途**

列出一张表的所有分区。

**使用示例**

执行如下命令，列出表的所有分区。

```
SHOW PARTITIONS table_name;
```

返回结果如下。

```
partition_col1=col1_value1/partition_col2=col2_value1 partition_col1=col1_value2/partition_col2=col2_value2
```

**说明**

`partition_col1` 和 `partition_col2` 表示该表的分区列。 `col1_value1` 、 `col2_value1` 、 `col1_value2` 、 `col2_value2` 表示分区列对应的值。

#### 5.2.4. 实例操作

本文介绍MaxCompute实例管理常用命令，包括查看、监控、终止及查询作业状态与日志，方便您高效跟踪、诊断和管理已提交的作业。

**Show Instances/Show P**

**命令格式**

```
SHOW INSTANCES [FROM startdate TO enddate] [number]; SHOW P [FROM startdate TO enddate] [number]; SHOW INSTANCES [-all]; SHOW P [-all]; SHOW P -p <project name>;
```

参数说明：

| 参数 | 说明 |
|---|---|
| startdate | 返回从起始时间startdate到结束时间enddate的实例信息。需满足如下格式：yyyy-mm-dd，精度到天。可选参数，如果不指定，返回您在三天内提交的实例。 |
| enddate |  |
| number | 指定返回实例的数量。依照时间排序，返回距离当前时间最近的number个实例信息。如果不指定number，返回满足要求的所有实例信息。 |
| -all | 返回当前项目下所有执行过的实例，默认最大返回50条。需要注意，执行该命令需要有项目空间的List权限。如果需要返回更多条记录，请使用-limit number参数，例如 show p -all -limit 100 表示返回当前项目下100条执行过的实例记录。 |
| project name | 项目名称，您使用的账号必须已经是项目成员。 |

**用途**

返回由当前用户创建的实例信息。 输出项包括：StartTime（时间精确到秒）、RunTime（s）、Status（实例状态）、InstanceID和实例对应的SQL。

**使用示例**

执行如下命令，返回由当前用户创建的实例信息。

```
SHOW p;
```

返回结果如下。

```
+---------------------+---------+---------+-------------------------+----------------------------+-----------------------+
|      StartTime      | RunTime | Status  |        InstanceID       |             Owner          |          Query        |
+---------------------+---------+---------+-------------------------+----------------------------+-----------------------+
| 2026-01-20 10:51:54 |   0s    | Success | 20260120025154***99u031 | ALIYUN$ascm-org-176***9748 | SELECT * FROM emp_tb; |
| 2026-01-20 13:48:50 |   0s    | Success | 20260120054850***5z2gce | ALIYUN$ascm-org-176***9748 | SHOW recyclebin;      |
| 2026-01-20 13:49:16 |   0s    | Success | 20260120054916***5z2gce | ALIYUN$ascm-org-176***9748 | purge ALL;            |
+---------------------+---------+---------+-------------------------+----------------------------+-----------------------+
```

Instance有如下6种状态： Running：正在运行。 Success：成功结束。 Waiting：等待中。 Failed：作业失败，但是尚未改写目标表数据。 Suspended：挂起。 Cancelled：被中止。

**Status Instance**

**命令格式**

```
STATUS instance_id;
```

参数说明： `instance_id` ，实例的唯一标识符，指定查询哪个实例状态。

**用途**

返回指定实例的状态，状态包括Success、Failed、 Running和Cancelled。

**说明**

如果此实例并非当前用户创建，返回异常。

**使用示例**

执行如下命令，查看ID为20151225123xxx的实例状态。

```
STATUS 20151225123xxx;
```

返回结果如下。

```
Success
```

**Top Instance**

**命令格式**

```
TOP INSTANCE; TOP INSTANCE -all;
```

**说明**

执行此命令，您需要是项目Owner或管理员角色。

**用途**

`TOP INSTANCE` ：返回当前项目中当前账号所提交的正在执行的作业信息，包括InstanceID、Owner、Type、StartTime、Progress、Status、Priority、 RuntimeUsage（CPU/MEM）、TotalUsage（CPU/MEM）和QueueingInfo（POS/LEN）等。 `TOP INSTANCE -all` ：返回当前项目下所有正在执行的作业，默认最大返回50条。如果需要返回更多条记录，请使用 `-limit number` 参数。

**Kill Instance**

**命令格式**

```
kill <instance_id>;
```

参数说明： `instance_id` ，实例的唯一标识符。必须是状态为Running的实例的ID，否则报错。

**用途**

停止指定的实例，此实例的状态必须为Running。需要注意，这是一个异常的过程，在系统接受此请求并返回后，并不意味着分布式的作业已经停止，而是只代表系统已接收到请求，因此还需要使用 `status` 命令查看此Instance的状态后才可以确定。

**使用示例**

停止ID为20251225123xxx的实例。

```
kill 20251225123xxx;
```

**Desc Instance**

**命令格式**

```
DESC INSTANCE <instance_id>;
```

参数说明： `instance_id` ，实例的唯一标识符。

**用途**

根据具体的实例ID获得作业信息，包括具体的SQL、Owner、StartTime、EndTime和Status等信息。

**使用示例**

执行如下命令，查询ID为20250715xxx的实例对应的作业信息。

```
DESC INSTANCE 20250715xxx;
```

返回结果如下。

```
ID 20250715xxx Owner ALIYUN$XXXXXX@alibaba-inc.com StartTime 2015-07-15 18:34:41 EndTime 2015-07-15 18:34:42 Status Terminated console_select_query_task_1436956481295 Success Query select * from mj_test;
```

其中 `Status` 为作业的状态； `console_select_query_task_1436956481295` 为作业中命令执行的状态。

**Wait Instance**

**命令格式**

```
WAIT instance_id;
```

参数说明： `instance_id` ，实例的唯一标识符。

**用途**

根据具体的实例ID获得任务运行日志信息，包含Logview链接。再通过查看Logview获得任务的详细日志。

**说明**

超过3天的Instance对应Logview可以获取，但会因为过期被清除而无法打开。

**使用示例**

执行如下命令，查看实例ID为20250925161122379gxxxxxx的任务运行日志信息。

```
WAIT 20250925161122379gxxxxxx;
```

返回结果如下。

```
ID = 20250925161122379g3xxxxxx Log view: http://logview.odps.aliyun.com/logview/?h=http://service.odps.aliyun.com/api&p=alian&i=202509251611223xxxxxxdqp&token=XXXXXXvbiI6IjEifQ== Job Queueing... Summary: resource cost: cpu 0.05 Core * Min, memory 0.05 GB * Min inputs:
        alian.bank_data: 41187 (588232 bytes)
outputs:
        alian.result_table: 8 (640 bytes)
Job run time: 2.000 Job run mode: service job Job run engine: execution engine M1:
        instance count: 1
        run time: 1.000
        instance time:
                min: 1.000, max: 1.000, avg: 1.000
        input records:
                TableScan_REL5213301: 41187  (min: 41187, max: 41187, avg: 41187
```

)

```
        output records:
                StreamLineWrite_REL5213305: 8  (min: 8, max: 8, avg: 8)
R2_1:
        instance count: 1
        run time: 2.000
        instance time:
                min: 2.000, max: 2.000, avg: 2.000
        input records:
                StreamLineRead_REL5213306: 8  (min: 8, max: 8, avg: 8)
        output records:
                TableSink_REL5213309: 8  (min: 8, max: 8, avg: 8)
```

#### 5.2.5. 资源操作

本文介绍MaxCompute资源操作常用命令，包括添加、删除、查看和下载资源，方便您高效管理作业依赖资源。

**添加资源**

**命令格式**

```
ADD file <local_file> [AS alias] [comment 'cmt'][-f]; ADD archive <local_file> [AS alias] [comment 'cmt'][-f]; ADD TABLE <table_name> [PARTITION (spec)] [AS alias] [comment 'cmt'][-f]; ADD jar <local_file.jar> [comment 'cmt'][-f]; ADD py <local_file.py> [comment 'cmt'][-f];
```

参数说明：

| 参数 |  | 说明 |
|---|---|---|
| file/archive/table/jar/py |  | 表示资源类型。 |
|  | file/archive/table/jar/py |  |
| local_file |  | 表示本地文件所在路径。并以此文件名作为该资源名，资源名是资源的唯一标识。 |
| table_name |  | 表示MaxCompute中的表名。 |

| [partition (spec)] | 当添加的资源为分区表时，MaxCompute仅支持将某个分区作为资源，不支持将整张分区表作为资源。 |
|---|---|
| alias | 指定资源名，不添加该参数时默认文件名为资源名。JAR及PY类型资源不支持此功能。 |
| [comment 'cmt'] | 给资源添加注释。 |
| [-f] | 当存在同名的资源时，此操作会覆盖原有资源。若不指定此选项，存在同名资源时，操作将失败。 |

**用途**

添加资源至MaxCompute中。

**使用示例**

执行如下命令，添加一个别名为sale.res的表资源到MaxCompute。

```
ADD TABLE sale_detail PARTITION (ds='20250602') AS sale.res comment 'sale detail on 202506 02' -f;
```

返回结果如下。

```
OK: Resource 'sale.res' have been updated.
```

**说明**

每个资源文件的大小不能超过 `500 MB` ，单个SQL和MapReduce任务所引用的资源总大小不能超过 `2048 MB` 。

**删除资源**

**命令格式**

```
DROP RESOURCE <resource_name>;
```

参数说明如下。 `resource_name` ：要删除资源的名称。

**用途**

删除已经存在的资源。

**使用示例**

执行如下命令，删除已经存在的资源。

```
DROP RESOURCE getaddr.jar;
```

返回结果如下。

```
Confirm to "DROP RESOURCE getaddr.jar" (yes/no)? y
```

`--` 需要输入y进行确认。 `OK`

**查看资源列表**

**命令格式**

```
LIST RESOURCES;
```

**用途**

查看当前项目空间下所有的资源。

**使用示例**

执行如下命令，查看当前项目空间下所有的资源。

```
LIST RESOURCES;
```

返回结果如下。

```
Resource Name Comment Last Modified Time Type 1234.txt 2025-02-27 07:07:56 file mapred.jar 2025-02-27 07:07:57 jar
```

**下载资源**

**命令格式**

```
GET RESOURCE <resource_name> <path>;
```

参数说明如下：

| resource_name |  |
|---|---|
| path | ：资源保存 |

**用途**

下载MaxCompute中的资源到本地。资源类型必须为FILE、JAR、ARCHIVE和PY，不支持TABLE类型。

**使用示例**

执行如下命令，下载MaxCompute中的资源到本地。

```
GET RESOURCE odps-udf-examples.jar d:\;
```

返回结果如下。 `OK`

#### 5.2.6. 函数操作

本文介绍MaxCompute函数操作常用命令，包括注册、删除和查看自定义函数。方便您高效管理自定义函数。

**注册函数**

**命令格式**

```
CREATE FUNCTION <function_name> AS <package_to_class> USING <resource_list>;
```

参数说明如下。

| 参数 | 说明 |
|---|---|
| function_name | UDF函数名。这个名字就是SQL中引用该函数所使用的名字。 |
| package_to_class | 如果是Java UDF，这个名字就是从顶层包名一直到实现UDF类名的 fully qualified class name 。如果是Python UDF，这个名字就是 Python脚本名.类名。这个名字必须用半角引号（''）引起来。 |
| resource_list | UDF所用到的资源列表，其中必须包括UDF代码所在的资源，且资源已经上传至MaxCompute。如果用户在代码中通过distributed cache接口读取资源文件，这个列表中还需要包括UDF所读取的资源文件列表。资源列表由多个资源名组成，资源名之间由半角逗号（,）分隔。资源列表必须用半角引号（''）引起来。如果需要指定资源所在的Project，写法为 <project_name>/resources/<resource_name> 。 |

**使用示例**

| 假设Java UDF类 | org.alidata.odps.udf.examples.Lower | 在my lower.jar中，创建函数 _ | my_lower | 。 |
|---|---|---|---|---|
| CREATE FUNCTION test_lower AS 'org.alidata.odps.udf.examples.Lower' USING 'my_lower.jar'; |  |  |  |  |

假设Python UDF MyLower在项目空间**test_project**的脚本pyudf_test.py中，创建函数**my_lower**。

```
CREATE FUNCTION my_lower AS 'pyudf_test.MyLower' USING 'pyudf_test.py';
```

假设Java UDF类**com.aliyun.odps.examples.udf.UDTFResource**是在udtfexample1.jar中，同时该函数还依赖File资源**file_resource.txt**、Table资源**table_resource1**以及Archive资源**test_archive.zip**，创建函数**test_udtf**。

```
CREATE FUNCTION test_udtf AS 'com.aliyun.odps.examples.udf.UDTFResource' USING 'udtfexample1.jar, file_resource.txt, table_resource1,test_archive.zip';
```

**说明**

与资源文件一样，同名函数只能注册一次。 通常您的自建函数无法覆盖系统内建函数，只有项目空间的Owner才有权利覆盖内建函数。如果您使用了覆盖内建函数的自定义函数，在SQL执行结束后，会在Summary中打印出warning信息。

**注销函数**

**命令格式**

```
DROP FUNCTION <function_name>;
```

参数说明如下。 `function_name` ：已存在的函数名称。

**使用示例**

```
DROP FUNCTION test_lower;
```

**查看函数清单**

**命令格式**

`--`查看当前项目空间中的所有自定义函数。

```
LIST FUNCTIONS;
```

`--`查看指定项目空间下的所有自定义函数。

```
LIST FUNCTIONS -p project_name;
```

#### 5.2.7. 时区配置操作

本文介绍如何使用Set命令配置MaxCompute Project的时区。

**时区配置的方式**

MaxCompute Project时区默认是中国的东八区，DATETIME、TIMESTAMP和DATE类型字段以及相关时间内置函数都是按东八区进行计算。您可以通过以下两种方式进行时区的配置： Session级别：执行 SET odps.sql.timezone=<timezoneid>; 语句，需要与计算语句一起提交。 示例如下。 执行如下命令，设置时区为Asia/Tokyo。

```
SET odps.sql.timezone=Asia/Tokyo;
```

执行如下命令，查询当前时区下的当前时间。

```
SELECT getdate();
```

返回结果如下。

```
+------------+
| _c0        |
+------------+
| 2018-10-30 23:49:50 |
+------------+
```

| Project级别：执行 | setProject odps.sql.timezone=<timezoneid>; | 语句，此命令需要项目Owner执行。 |
|---|---|---|
| 重要 Project的时区一旦被设置，相关的时间计算会取设置后的时区，原有的任务数据将会受到影响。所以，请您谨慎考虑是否有必要设置时区。如果必要，建议只对新增的Project进行设置，不建议对已有数据的Project进行设置。 |  |  |

**使用限制及注意事项**

时区配置支持的范围：SQL内置日期函数、UDF、UDT、UDJ以及Select Transform都支持获取Project Timezone属性来配置时区。 时区支持的格式为Asia/Shanghai这类的格式（存在夏令时跳变），不支持GMT+9格式。 当SDK时区与Project时区不同时，DATETIME转换STRING的操作需设置GMT时区。 时区配置后，通过DataWorks执行相关SQL时，日期显示某些时间段会存在时间差异，例如1900~1928年的日期时间差异为5分52秒，1900年之前的日期时间差异为9秒。 为了保证MaxCompute在多个时区DATETIME类型数据的正确性，MaxCompute服务、Java SDK以及配套的Console会进行版本更新（ `-oversea` 后缀的Java SDK和Console版本），更新后可能影响MaxCompute中已经存储的早于1928年的DATETIME类型数据的显示。 对于非中国东八区的区域，建议用户同步更新Java SDK和Console版本，以保证SQL计算结果及Tunnel传输1900-01-01之后范围的数据的准确性和一致性。对于早于1900-01-01的DATETIME数据，SQL的计算显示结果和Tunnel传输数据仍然可能存在343秒的差异。对于新版本SDK和Console之前已经上传的早于1928- 01-01的DATETIME数据，在新版本中日期时间会减少352秒。 如果继续使用不带有 `-oversea` 后缀的SDK和Console，SQL计算结果和Tunnel传输数据将存在差异。早于1900-01-01的数据差异为9秒，1900-01-01~1928- 01-01的数据差异为352秒。

**说明**

Java SDK和Console版本更新配置时区不影响DataWorks的时区配置，因此时区会存在差异，需要您对DataWorks中定时任务调度的影响进行计算评估。 通过JDBC连接的第三方客户端需要在客户端设置时区，保证与服务端时区设置的一致性。 Spark支持时区功能： 对于提交到MaxCompute计算集群的任务形式，可以自动获取Project的时区。 对于通过 `yarn-client` 模式启动（例如Spark-shell、Spark-sql以及Pyspark等）的设置，用户需要手动配置Driver的启动参数（Spark-defaults.conf）， 增加 `spark.driver.extraJavaOptions -Duser.timezone=America/Los_Angeles` ， `timezone` 的值为将要使用的时区。

#### 5.2.8. Tunnel操作

本文介绍Tunnel的核心命令： `upload` 、 `download` 、 `resume` 、 `show` 、 `purge` 和 `help` ，用于支持数据的上传、下载、续传、状态查询、历史清理及使用帮助。

**Tunnel命令使用说明**

**命令格式**

| 您可以通过 | tunnel help; | 子命令获取帮助信息，返回结果如下。 |
|---|---|---|
| Usage: tunnel <subcommand> [options] [args] Type 'tunnel help <subcommand>' for help on a specific subcommand. Available subcommands: upload (u) download (d) resume (r) show (s) purge (p) help (h) tunnel is a command for uploading data to / downloading data from ODPS. |  |  |

**参数说明**

| 命令 | 说明 |
|---|---|
| upload | 上传数据到MaxCompute的表中。支持文件或目录（指一级目录）的上传，每次上传只支持数据上传到一张表或表的一个分区。分区表一定要指定上传的分区，多级分区一定要指定到末级分区。 tunnel upload log.txt test_project.test_table/p1="b1",p2="b2"; -- 将log.txt中的数据上传至项目空间test_project的表test_table（二级分区表）中的p1="b1",p2="b2"分区。 tunnel upload log.txt test_table --scan=true; -- 将log.txt中的数据上传至表test_table中。scan参数表示需要扫描log.txt中的数据是否符合test_table的定义，如果不符合报错，并停止上传数据。 |
| download | 从MaxCompute的表中下载数据。只支持下载到单个文件，每次下载只支持下载一张表或一个分区的数据到一个文件。分区表一定要指定下载的分区，多级分区一定要指定到末级分区。 tunnel download test_project.test_table/p1="b1",p2="b2" test_table.txt; -- 将test_project.test_table表（二级分区表）中的数据下载到test_table.txt文件中。 |
| resume | 因为网络或Tunnel服务的原因出错，支持续传文件或目录。如果上传数据失败，通过resume命令进行断点续传，仅支持上传数据的续传。每次上传、下载数据被称为一个Session。在resume后指定Session ID完成续传。 tunnel resume; |
| show | 显示历史任务信息。 tunnel show history -n 5; -- 显示前5次上传或下载数据的详细命令。 tunnel show log; -- 显示最后一次上传或下载数据的日志。 |
| purge | 清理Session目录，默认清理3天内的日志。 tunnel purge 5; -- 清理前5天的日志。 |
| help | 输出Tunnel帮助信息。 |

**命令用途**

将本地文件的数据以追加模式导入到MaxCompute的表中。

**命令格式**

您可以通过 tunnel help upload; 子命令获取帮助信息，返回结果如下。

```
usage: tunnel upload [options] <path> <[project.]table[/partition]>
              upload data from local file
 -acp,-auto-create-partition <ARG>   auto create target partition if not
                                     exists, default false
 -bs,-block-size <ARG>               block size in MiB, default 100
 -c,-charset <ARG>                   specify file charset, default ignore.
                                     set ignore to download raw data
 -cf,-csv-format <ARG>               use csv format (true|false), default
                                     false. When uploading in csv format,
                                     file splitting not supported.
 -cp,-compress <ARG>                 compress, default true
 -dbr,-discard-bad-records <ARG>     specify discard bad records
                                     action(true|false), default false
 -dfp,-date-format-pattern <ARG>     specify date format pattern, default
                                     yyyy-MM-dd HH:mm:ss
 -fd,-field-delimiter <ARG>          specify field delimiter, support
                                     unicode, eg \u0001. default ","
 -h,-header <ARG>                    if local file should have table
                                     header, default false
 -mbr,-max-bad-records <ARG>         max bad records, default 1000
 -ni,-null-indicator <ARG>           specify null indicator string,
                                     default ""(empty string)
 -ow,-overwrite <true | false>       overwrite specified table or
                                     partition, default: false
 -rd,-record-delimiter <ARG>         specify record delimiter, support
                                     unicode, eg \u0001. default "\n"
 -s,-scan <ARG>                      specify scan file
                                     action(true|false|only), default true
 -sd,-session-dir <ARG>              set session dir, default
                                     /apsara/odps/odps/odps_tools/clt/plug
                                     ins/dship
 -ss,-strict-schema <ARG>            specify strict schema mode. If false,
                                     extra data will be abandoned and
                                     insufficient field will be filled
                                     with null. Default true
 -t,-threads <ARG>                   number of threads, default 1
 -te,-tunnel_endpoint <ARG>          tunnel endpoint
 -time,-time <ARG>                   keep track of upload/download elapsed
                                     time or not. Default false
 -tz,-time-zone <ARG>                time zone, default local timezone:
                                     Asia/Shanghai
Example:
    tunnel upload log.txt test_project.test_table/p1="b1",p2="b2"
```

**参数说明**

| 参数 |  | 说明 |
|---|---|---|
| path |  | 上传数据文件的路径以及名称。 |
| [project.]table[/partiti |  | 目标表表名。如果是分区表，需要指定至最末级分区。如果不是当前空间的表，需要指定表所在的空间名。 |
|  | [project.]table[/partiti |  |
| on] |  |  |
| -acp |  | 如果指定分区不存在，自动创建目标分区。默认值为False。 |
| -bs |  | 指定每次上传至Tunnel的数据块大小。默认值为100 MiB（1 MiB＝1024×1024 Byte）。 |
| -c |  | 指定本地数据文件编码。默认为UTF-8，不设定时，默认下载源数据。 |
| -cf |  | 指定是否为CSV文件，默认值为False。 |
| -cp |  | 指定是否在本地压缩后再上传，减少网络流量，默认值为True。 |
| -dbr |  | 指定是否忽略脏数据（多列、少列或列数据类型不匹配等情况）。值为True时，忽略全部不符合表定义的数据。值为False，如果遇到脏数据，则给出错误提示信息，目标表内的原始数据不会被污染。默认值为False。 |
| -dfp |  | 指定DATETIME类型数据格式。默认为yyyy-MM-dd HH:mm:ss。如果您想指定时间格式到毫秒级别，可以使用 tunnel upload -dfp 'yyyy-MM-dd HH:mm:ss.SSS' 。 |
| -fd |  | 指定本地数据文件的列分割符，默认为半角逗号（,）。 |

|  | 'yyyy-MM-dd HH:mm:ss.SSS' |
|---|---|

| -h | 指定数据文件是否包括表头。如果为True，则会跳过表头从第二行开始上传数据。默认值为False。 |
|---|---|
| -mbr | 指定可容忍的脏数据量。超过此数据量时，终止上传。默认值为1000条。 |
| -ni | 指定NULL数据标志符，默认值为空字符串。 |
| -ow | 指定上传数据是否覆盖表或分区。默认值为False，上传数据为累加方式。 |
| -rd | 本地数据文件的行分割符，Linux默认为 \n ，Windows默认为 \r\n 。 |
| -s | 指定是否扫描本地数据文件，默认值为True。值为True时，先扫描数据，如果数据格式正确，再导入数据。值为False，不扫描数据，直接进行数据导入。值为Only时，仅扫描本地数据，扫描结束后不继续导入数据。 |
| -sd | 指定Session目录所在的路径，默认为 D:/console/plugins/dship/lib/.. （plugins/dship/lib所在具体路径）。 |
| -ss | 指定严格架构模式。默认值为True。如果为False，多余的数据将被丢弃，不足的字段将填充NULL。 |
| -t | 指定线程的数量。默认值为1。 |
| -te | 指定Tunnel的Endpoint。 |
| -time | 指定是否跟踪上传所用时间。默认值为False。 |
| -tz | 指定时区。默认为本地时区，例如Asia/Shanghai。 |

**使用示例**

1. 执行如下命令创建分区表sale_detail。

```
CREATE TABLE IF NOT EXISTS sale_detail(
    shop_name STRING,
    customer_id STRING,
     total_price DOUBLE)
PARTITIONED BY (sale_date STRING,region STRING);
```

2. 执行如下命令，为分区表sale_detail添加分区。

```
ALTER TABLE sale_detail ADD PARTITION (sale_date='201705', region='hangzhou');
```

3. 准备需要上传的数据文件data.txt，内容如下所示，保存路径为d:\data.txt。

```
shop9,97,100 shop10,10,200 shop11,11
```

**说明**

这份文件的第三行数据与sale_detail的表定义不符。sale_detail定义了三列，但数据只有两列。
4. 执行如下命令，上传数据文件data.txt至分区表sale_detail。

```
tunnel u d:\data.txt sale_detail/sale_date=201705,region=hangzhou -s false;
```

由于data.txt中存在脏数据，数据导入失败，并返回Session ID及错误提示信息。

```
Upload session: 20150610xxxxxxxxxxx70a002ec60c Start upload:d:\data.txt Total bytes:41 Split input to 1 blocks 2017-06-10 16:39:22 upload block: '1' ERROR: column mismatch -,expected 3 columns, 2 columns found, please check data or delimiter
```

5. 执行如下命令，进行数据验证。

```
SELECT * FROM sale_detail WHERE sale_date='201312';
```

由于存在脏数据，数据导入失败，因此表中无数据。

```
ID = 20150610xxxxxxxxxxxvc61z5 +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+ +-----------+-------------+-------------+-----------+--------+
```

6. 使用show命令查询失败上传的Session ID。

```
tunnel show history;
```

返回结果如下。

```
20150610xxxxxxxxxxx70a002ec60c failed 'u --config-file /D:/console/conf/odps_config.ini --project odpstest_ay52c_ay52 --endpoint http ://service.cn-shanghai.maxcompute.aliyun.com/api --id UlxxxxxxxxxxxrI1 --key 2m4r3WvTxxxxxxxxxx0InVke7UkvR d:\data.txt sale_detail/sale_date=201312,region=hangzhou -s false'
```

7. 修改示例数据data.txt文件为如下内容，使之符合sale_detail的表结构。

```
shopx,x_id,100 shopy,y_id,200
```

8. 执行resume命令修复上传数据。其中，20150610xxxxxxxxxxx70a002ec60c为上传失败的Session ID。

```
tunnel resume 20150610xxxxxxxxxxx70a002ec60c --force;
```

返回结果如下。

```
start resume 20150610xxxxxxxxxxx70a002ec60c Upload session: 20150610xxxxxxxxxxx70a002ec60c Start upload:d:\data.txt Resume 1 blocks 2015-06-10 16:46:42 upload block: '1' 2015-06-10 16:46:42 upload block complete, blockid=1 upload complete, average speed is 0 KB/s
```

`OK`
9. 执行如下命令，进行数据验证。

```
SELECT * FROM sale_detail WHERE sale_date='201312';
```

返回结果如下，说明上传成功。

```
 ID = 20150610xxxxxxxxxxxa741z5
 +-----------+-------------+-------------+-----------+--------+
 | shop_name | customer_id | total_price | sale_date | region |
 +-----------+-------------+-------------+-----------+--------+
 | shopx     | x_id        | 100.0       | 201312    | hangzhou|
 | shopy     | y_id        | 200.0       | 201312    | hangzhou|
 +-----------+-------------+-------------+-----------+--------+
```

**命令用途**

将MaxCompute表数据或指定Instance的执行结果下载至本地。

**命令格式**

您可以通过 tunnel help download; 子命令获取帮助信息，返回结果如下。

```
Usage: tunnel download [options] <[project.]table[/partition]> <path>
              download data to local file
 -c,-charset <ARG>                 specify file charset, default ignore.
                                   set ignore to download raw data
 -cf,-csv-format <ARG>             use csv format (true|false), default
                                   false. When uploading in csv format,
                                   file splitting not supported.
 -ci,-columns-index <ARG>          specify the columns index(starts from
                                   0) to download, use comma to split each
                                   index
 -cn,-columns-name <ARG>           specify the columns name to download,
                                   use comma to split each name
 -cp,-compress <ARG>               compress, default true
 -dfp,-date-format-pattern <ARG>   specify date format pattern, default
                                   yyyy-MM-dd HH:mm:ss
 -e,-exponential <ARG>             When download double values, use
                                   exponential express if necessary.
                                   Otherwise at most 20 digits will be
                                   reserved. Default false
 -fd,-field-delimiter <ARG>        specify field delimiter, support
                                   unicode, eg \u0001. default ","
 -h,-header <ARG>                  if local file should have table header,
                                   default false
    -limit <ARG>                   specify the number of records to
 -ni,-null-indicator <ARG>         specify null indicator string, default
                                   ""(empty string)
 -rd,-record-delimiter <ARG>       specify record delimiter, support
                                   unicode, eg \u0001. default "\r\n"
 -sd,-session-dir <ARG>            set session dir, default
                                   D:\software\odpscmd_public\plugins\dship
 -t,-threads <ARG>                 number of threads, default 1
 -te,-tunnel_endpoint <ARG>        tunnel endpoint
 -time,-time <ARG>                 keep track of upload/download elapsed
                                   time or not. Default false
 -tz,-time-zone <ARG>              time zone, default local timezone:
                                   Asia/Shanghai
usage: tunnel download [options] instance://<[project/]instance_id> <path>
              download instance result to local file
 -c,-charset <ARG>                 specify file charset, default ignore.
                                   set ignore to download raw data
 -cf,-csv-format <ARG>             use csv format (true|false), default
                                   false. When uploading in csv format,
                                   file splitting not supported.
 -ci,-columns-index <ARG>          specify the columns index(starts from
                                   0) to download, use comma to split each
                                   index
 -cn,-columns-name <ARG>           specify the columns name to download,
                                   use comma to split each name
 -cp,-compress <ARG>               compress, default true
 -dfp,-date-format-pattern <ARG>   specify date format pattern, default
                                   yyyy-MM-dd HH:mm:ss
 -e,-exponential <ARG>             When download double values, use
                                   exponential express if necessary.
                                   Otherwise at most 20 digits will be
                                   reserved. Default false
 -fd,-field-delimiter <ARG>        specify field delimiter, support
                                   unicode, eg \u0001. default ","
 -h,-header <ARG>                  if local file should have table header,
                                   default false
    -limit <ARG>                   specify the number of records to
 -ni,-null-indicator <ARG>         specify null indicator string, default
                                   ""(empty string)
 -rd,-record-delimiter <ARG>       specify record delimiter, support
                                   unicode, eg \u0001. default "\r\n"
 -sd,-session-dir <ARG>            set session dir, default
                                   D:\software\odpscmd_public\plugins\dshi
 -t,-threads <ARG>                 number of threads, default 1
 -te,-tunnel_endpoint <ARG>        tunnel endpoint
 -time,-time <ARG>                 keep track of upload/download elapsed
                                   time or not. Default false
 -tz,-time-zone <ARG>              time zone, default local timezone:
                                   Asia/Shanghai
Example:
    tunnel download test_project.test_table/p1="b1",p2="b2" log.txt //下载指定表数据
    tunnel download instance://test_project/test_instance log.txt   //下载指定Instance的执行结果
```

**参数说明**

| 参数 |  | 说明 |
|---|---|---|
| path |  | 下载的数据文件保存的本地路径。 |
| [project.]table[/partitio |  | 需要下载的表名称。如果是分区表，需要指定至最末级分区。如果不是当前空间的表，需要指定表所在的空间名。 |
|  | [project.]table[/partitio |  |
| n] |  |  |
| [project/]instance_id |  | Instance ID。下载指定Instance的执行结果时指定此参数。 |
| -fd |  | 指定本地数据文件的列分割符，默认为半角逗号（,）。 |
| -rd |  | 指定本地数据文件的行分割符，默认为\r\n。 |
| -dfp |  | 指定DATETIME类型数据格式，默认为yyyy-MM-dd HH:mm:ss。 |
| -ni |  | 指定NULL数据标志符，默认值为空字符串。 |
| -c |  | 指定本地数据文件编码，默认为UTF-8。 |
| -cf |  | 指定是否为CSV文件，默认值为False。 |
| -ci |  | 指定列索引（从0开始）下载，使用半角逗号（,）分隔。 |
| -cp |  | 指定要下载的列名称，使用半角逗号（,）分隔每个名称。 |
| -e |  | 指定下载DOUBLE类型值时，如果需要，使用指数函数表示，否则最多保留20位。默认值为False。 |
| -h |  | 指定数据文件是否包括表头。默认值为False。如果为True，则会跳过表头从第二行开始下载数据。 说明 -h=true和threads>1（多线程）不能一起使用。 |
| -limit |  | 指定要下载的文件数量。 |
| -tz |  | 指定时区。默认为本地时区，例如Asia/Shanghai。 |
| -time |  | 指定是否跟踪上传所用时间。默认值为False。 |
| -te |  | 指定Tunnel的Endpoint。 |
| -t |  | 指定线程的数量。默认值为1。 |
| -sd |  | 指定Session目录所在的路径，默认为 D:/console/plugins/dship/lib/.. （plugins/dship/lib所在具体路径）。 |

**使用示例**

1. 执行如下命令，查询表sale_detail。

```
SELECT * FROM sale_detail;
```

返回结果如下。

```
ID = 20170724071705393ge3csfb8 ... ...
```

2. 执行如下命令，下载执行结果到本地文件。

```
tunnel download instance://20170724071705393ge3csfb8 result;
```

返回结果如下，说明下载成功。

```
2017-07-24 15:18:47 - new session: 2017072415184785b6516400090ca8 total lines: 8 2017-07-24 15:18:47 - file [0]: [0, 8), result downloading 8 records into 1 file 2017-07-24 15:18:47 - file [0] start 2017-07-24 15:18:48 - file [0] OK. total: 44 bytes download OK
```

在MaxCompute客户端中打开**use_instance_tunnel**选项后，执行的SELECT查询会默认使用InstanceTunnel来下载结果，从而避免在MaxCompute平台获取 SQL查询结果时所遇到的获取数据超时和获取数据量受限的问题。打开该配置有以下两种方法： 在客户端中的**odps_config.ini**文件里已经默认打开此选项，并且**instance_tunnel_max_record**被默认设置成了10000。

```bash
# the max records when download sql results by instance tunnel
```

**说明**

**instance_tunnel_max_record**用来设置通过InstanceTunnel下载SQL查询结果的条数。如果不设置该项，则下载条数不受限制。

| 将 | set console.sql.result.instancetunnel | 设置为True来开启此功能。 |
|---|---|---|
| SET console.sql.result.instancetunnel=true; |  |  |

**Resume**

**命令用途**

修复执行历史记录，仅对上传数据有效。

**命令格式**

| 您可以通过 | tunnel help resume; | 子命令获取帮助信息，返回结果如下。 |
|---|---|---|
| Usage: tunnel resume [session_id] [--force] resume an upload session -f,-force force resume Example: tunnel resume |  |  |

**参数说明**

session_id：上传失败的Session ID。必选参数。 -f：指定是否强制修复执行历史记录。默认忽略。

**使用示例**

执行如下命令修复上传数据Session。20170610xxxxxxxxxxx70a002ec60c为上传失败的Session ID。

```
tunnel resume 20170610xxxxxxxxxxx70a002ec60c -force;
```

返回结果如下。

```
start resume 201706101639224880870a002ec60c Upload session: 201706101639224880870a002ec60c Start upload:d:\data.txt Resume 1 blocks 2017-06-10 16:46:42 upload block: '1' 2017-06-10 16:46:42 upload block complete, blockid=1 upload complete, average > speed is 0 KB/s
```

`OK`

**Show**

**命令用途**

显示历史记录。

**命令格式**

| 您可以通过 | tunnel help show; | 子命令获取帮助信息，返回结果如下。 |
|---|---|---|
| Usage: tunnel show history [options] show session information -n,-number <ARG> lines Example: tunnel show history -n 5 tunnel show log |  |  |

**参数说明**

`-n` 为指定显示行数。

**Purge**

**命令用途**

清除Session目录。

**命令格式**

您可以通过 tunnel help purge; 子命令获取帮助信息，返回结果如下。

```
usage: tunnel purge [n]
              force session history to be purged.([n] days before, default
              3 days)
Example:
    tunnel purge 5
```

**参数说明**

n ，清除历史日志的天数。默认为3天。

#### 5.2.9. 其他操作

本文为您介绍其他操作的常用命令。

**Alias命令**

**命令用途**

Alias功能主要为了满足在不修改代码的前提下，在MaxCompute的MR或自定义函数（UDF）代码中，通过某个固定的资源名读取不同资源（数据）的需求。为资源创建别名。

**命令格式**

```
ALIAS <alias>=<real>;
```

**参数说明**

**alias**：命名后的资源别名。
**real**：资源的原名。

**使用示例**

```
ADD TABLE src_part PARTITION (ds='20171208') AS res_20171208; ADD TABLE src_part PARTITION (ds='20171209') AS res_20171209;
```

`--` 新增资源`res_20171208`和`res_20171209`。

```
ALIAS resName=res_20171208; jar -resources resName -libjars work.jar -classpath ./work.jar com.company.MainClass args ...;
```

`--` 命名资源`res_20171208`的别名为`resName`，并调用它。

```
ALIAS resName=res_20171209; jar -resources resName -libjars work.jar -classpath ./work.jar com.company.MainClass args ...;
```

`--` 命名资源`res_20171209`的别名为`resName`，并调用它。

**说明**

上面的资源别名**resName**在两个作业里引用到不同的资源表，代码可以不做修改也能读取到不同的数据。

**Set**

**命令用途**

您可以使用Set命令设置MaxCompute或您自定义的系统变量，以影响MaxCompute的行为。

**命令格式**

```
SET <KEY>=<VALUE>
```

```
SET odps.stage.mapper.mem=
```

`--` 设置每个`Map Worker`的内存大小，单位是`MB`，默认值`1024 MB`。

```
SET odps.stage.reducer.mem=
```

`--` 设置每个`Reduce Worker`的内存大小，单位是`MB`，默认值`1024 MB`。

```
SET odps.stage.joiner.mem=
```

`--` 设置每个`Join Worker`的内存大小，单位是`MB`，默认值`1024 MB`。

```
SET odps.stage.mem=
```

`--` 设置`MaxCompute`指定任务下所有`Worker`的内存大小。优先级低于以上三个设置，单位`MB`，无默认值。

```
SET odps.stage.mapper.split.size=
```

`--` 修改每个`Map Worker`的输入数据量，即输入文件的分片大小，从而间接控制每个`Map`阶段下`Worker`的数量，单位`MB`，默认值`256 MB`。

```
SET odps.stage.reducer.num=
```

`--` 修改每个`Reduce Worker`数量，无默认值。

```
SET odps.stage.joiner.num=
```

`--` 修改每个`Join Worker`数量，无默认值。

```
SET odps.stage.num=
```

`--` 修改`MaxCompute`指定任务的所有阶段的`Worker`的并发度，优先级低于以上三个设置，无默认值。

```
SET odps.mapred.map.memory=
```

`--` 设置每个`Map Worker`的内存大小，单位是`MB`，默认值`1024 MB`。

```
SET odps.mapred.reduce.memory=
```

`--` 设置每个`Reduce Worker`的内存大小，单位是`MB`，默认值`1024 MB`。

```
SET odps.mapred.map.split.size=
```

`--` 修改每个`Map Worker`的输入数据量，即输入文件的分片大小，从而间接控制每个`Map`阶段下`Worker`的数量，单位`MB`，默认值`256 MB`。

```
SET odps.mapred.reduce.tasks=
```

`--` 修改每个`Reduce`阶段`Worker`数量，无默认值。

**参数说明**

**KEY**：需要修改的属性名称。
**VALUE**：属性值。

**使用示例**

调整MaxCompute写表过程中为单个复杂类型的列预先申请缓存大小，以便提高写入性能。

```
SET odps.sql.executionengine.coldata.deep.buffer.size.max=1048576;
```

调整每个Mapper读取数据的大小为256 MB。

```
SET odps.stage.mapper.split.size=256;
```

**SetProject**

**命令用途**

您可以使用SetProject命令设置Project属性，当不指定**<KEY>=<VALUE>**时，显示当前Project属性配置。

**命令格式**

```
setproject ["<KEY>=<VALUE>"];
```

**参数说明**

Project属性的详细说明如下。

| 属性名称 | 设置权限 | 属性描述 | 取值范围 |
|---|---|---|---|
| odps.table.drop.ignorenonexisten t | 所有用户 | 当删除不存在的表时，是否报错，True时不报错。 | True或False |
| odps.instance.priority.autoadjust | ProjectOwner | 是否自动调整任务优先级，让小任务优先。 | True或False |
| odps.instance.priority.level | ProjectOwner | 调整Project内任务的优先级。 | 1~3 说明 1的优先级最高。 |
| odps.security.ip.whitelist | ProjectOwner | 指定访问Project的IP白名单。 | IP列表，英文逗号（,）分隔 |
| odps.table.lifecycle | ProjectOwner | optional：创建表时，lifecycle子句为可选，如果您不设置生命周期，则此表永久有效。 mandatory：lifecycle子句为必选。 inherit：如果您不指定生命周期，该表的生命周期为odps.table.lifecycle.value的值。 | optional、mandatory或inherit |

| odps.table.lifecycle.value | ProjectOwner | 默认的生命周期值。 | 1~37231 说明默认值为37231。 |
|---|---|---|---|
| odps.instance.remain.days | ProjectOwner | Instance信息保留时间。 | 3~30 |
| odps.task.sql.outerjoin.ppd | ProjectOwner | 在full outer join中过滤条件是否下推。 | True或False |
| odps.function.strictmode | ProjectOwner | 内置函数遇到脏数据时，返回 NULL（False），或者报错（True）。 | True或False |
| odps.task.sql.write.str2null | ProjectOwner | 是否将空字符串视为NULL（True）。 | True或False |

**导出Project Meta**

**命令用途**

导出Project的Meta到本地。Meta以odpscmd接受的语句表示，利用该Meta文件可以重建一个Project。

**命令格式**

```
export <projectname> <local_path>;
```

**Show Flags**

**命令用途**

显示SET设置的参数。

**说明**

该命令仅对Project级别生效。

**命令格式**

```
SHOW flags;
```

**计量预估（Cost SQL命令）**

**命令用途**

预估出一条SQL的计量信息，包含输入数据的大小、UDF个数以及SQL的复杂等级。

**命令格式**

```
cost sql <SQL Sentence>;
```

**使用示例**

执行如下命令，预估一条SQL的计量信息。

```
cost sql SELECT DISTINCT project_name, user_name FROM meta.m_security_users distribute BY project_name sort BY project_name;
```

返回结果如下。

```
ID = 20190715113033121xxxxxxx Input:65727592 Bytes UDF:0 Complexity:1.0
```

## 数据通道Tunnel

### 概述

本文介绍如何在MaxCompute中进行数据上传和下载，包括DataHub和Tunnel通道的使用方法、工具选择、网络配置指导及使用限制。

**通道介绍**

MaxCompute提供了两种数据上传下载的通道： DataHub实时数据通道：包含的工具有OGG插件、Flume插件、Logstash插件和Fluentd插件。 Tunnel批量数据通道：包含的工具有MaxCompute客户端、DataWorks、DTS、Sqoop、Kettle插件以及MMA迁移工具。 DataHub和Tunnel各自提供了SDK，而基于这些SDK衍生的数据上传下载的工具，方便您在各种场景下的数据上传或下载需求。 基于上述丰富的数据上传下载的工具，可以满足大部分常见的数据上云场景。

**数据通道服务连接**

DataHub和Tunnel在不同网络环境场景下，所使用的Endpoint会有所区别。您在不同网络环境下，需要选择不同的服务地址（Endpoint）来连接服务，否则将无法向服务发起请求。

**使用限制**

Tunnel Upload命令上传限制： Tunnel命令不支持上传下载ARRAY、MAP和STRUCT类型的数据。 上传没有速度限制，上传速度的瓶颈取决于网络带宽以及服务器性能。 重传Retry有次数的限制，当重传次数超过限制，就会继续上传下一个Block。上传完成后，可以通过**select count(*) from table_name**语句，检查数据是否有丢失。 一个项目下Tunnel支持并发的连接数默认上限为2000个。 每个Tunnel的Session在服务端的生命周期为24小时，创建后24小时内均可使用，也可以跨进程或跨线程共享使用，但是必须保证同一个Block ID没有重复使用。 当遇到并发写入时，MaxCompute会根据ACID进行并发写的保障。 DataHub上传数据限制： 每个字段的大小不能超过这个字段本身的限制。

**说明**

STRING的长度不能超过 `8MB` 。 上传的过程中，会将多条数据打包成一个Package来进行上传。 Block ID的取值范围是[0,20000)，单个Block上传的数据限制为 `100GB` 。 Session的超时时间为24小时。大批量数据传送时长超过24小时，需要自行拆分成多个Session。 RecordWriter对应的HTTP Request超时时间为 `120s` 。如果 `120s` 内HTTP连接上没有数据流过，Service端会主动关闭连接。

### 工具介绍

本文介绍MaxCompute平台支持的数据上传和下载工具（其中大部分工具已经在GitHub上公开源代码，以开源社区的方式进行维护），帮助用户根据实际应用场景选择合适的工具进行数据传输。

**阿里云产品**

| 产品 | 描述 |
|---|---|
| DataWorks数据集成（Tunnel通道系列） | DataWorks数据集成（即数据同步），是一个稳定高效、弹性伸缩的数据同步平台，致力于为阿里云上各类异构数据存储系统提供离线全量和实时增量的数据同步、集成及交换服务。关于DataWorks数据集成详情，请参见DataWorks数据集成。 其中数据同步任务支持的数据源类型包括：MaxCompute、RDS（MySQL、SQL Server及PostgreSQL）、Oracle、 FTP、ADS（AnalyticDB）、OSS、Memcache和DRDS。 |
| MaxCompute客户端（Tunnel通道系列） | 客户端基于批量数据通道的SDK，实现了内置的Tunnel命令，可以对数据进行上传和下载。关于MaxCompute Tunnel详情，请参见概述。 |
| DTS（Tunnel通道系列） | 数据传输（Data Transmission）服务DTS是阿里云提供的一种支持RDBMS（关系型数据库）、NoSQL及OLAP等多种数据源之间数据交互的数据服务。它提供了数据迁移、实时数据订阅及数据实时同步等多种数据传输功能。关于DTS数据传输详情，请参见数据传输服务DTS。 DTS可以支持RDS MySQL实例的数据实时同步到MaxCompute表中，暂不支持其他数据源类型。 |

**开源产品**

各产品对应的项目已经开源，您可进入aliyun-maxcompute-data-collectors进行查看。

| 产品 | 描述 |
|---|---|
| Sqoop（Tunnel通道系列） | Sqoop基于社区Sqoop 1.4.6版本开发，增强了对MaxCompute的支持，可以将数据从MySQL等关系数据库导入或导出到 MaxCompute表中，也可以从HDFS或Hive导入数据到MaxCompute表中。 |

| Kettle（Tunnel通道系列） | Kettle是一款开源的ETL工具，纯Java实现，可以在Windows、Unix和Linux上运行。提供图形化的操作界面，可以通过拖拽控件的方式，方便地定义数据传输的拓扑 。 |
|---|---|
| Flume（DataHub通道系列） | Apache Flume是一个分布式的、可靠的、可用的系统，可高效地从不同的数据源中收集、聚合和移动海量日志数据到集中式数据存储系统，支持多种Source和Sink插件。 Apache Flume的DataHub Sink插件可以将日志数据实时上传到DataHub，并归档到MaxCompute表中。 |
| Fluentd（DataHub通道系列） | Fluentd是一个开源的软件，用来收集各种源头日志（包括Application Log、Sys Log及Access Log），允许用户选择插件对日志数据进行过滤，并存储到不同的数据处理端（包括MySQL、Oracle、MongoDB、Hadoop、Treasure Data 等）。 Fluentd的DataHub插件可以将日志数据实时上传到DataHub，并归档到MaxCompute表中。 |
| Logstash（DataHub通道系列） | Logstash是一款开源日志收集处理框架，logstash-output-datahub插件实现了将数据导入DataHub的功能。通过简单的配置即可完成数据的采集和传输，结合MaxCompute和StreamCompute可以轻松构建流式数据从采集到分析的一站式解决方案。 Logstash的DataHub插件可以将日志数据实时上传到DataHub，并归档到MaxCompute表中。 |
| OGG（DataHub通道系列） | OGG的DataHub插件可以支持将Oracle数据库的数据实时地以增量方式同步到DataHub中，并最终归档到MaxCompute 表中。 |
| MMA迁移工具 | MMA利用Meta Carrier连接用户的Hive Metastore服务，抓取用户的Hive Metadata，并利用这些数据生成用于创建 MaxCompute表和分区的DDL语句以及用于迁移数据的Hive UDTF SQL。 |

**说明**

关于上述开源工具的介绍详情，请参见wiki。

### 数据上云的工具选择

MaxCompute平台提供多种工具选择，帮助用户进行Hadoop数据迁移、数据库数据同步和日志采集。本文介绍如何在这些场景中选择合适的数据传输工具。

**Hadoop数据迁移**

您可以使用MMA、Sqoop和DataWorks进行Hadoop数据迁移： 使用DataWorks进行Hadoop数据迁移，需要结合DataX工具。 Sqoop执行时，会在原有的Hadoop集群上执行MapReduce作业，可以分布式地将数据传输到MaxCompute上。 MMA利用Meta Carrier连接您的Hive Metastore服务，抓取Hive Metadata，并利用这些数据生成用于创建MaxCompute表和分区的DDL语句以及用于迁移数据的Hive UDTF SQL。

**数据库数据同步**

数据库的数据同步到MaxCompute需要根据数据库的类型和同步策略来选择相应的工具： 离线批量的数据库数据同步时，您可以选择DataWorks，其支持的数据库种类丰富，包括MySQL、SQL Server及PostgreSQL等。 Oracle数据库数据实时同步时，您可以选择OGG插件。 RDS数据库数据实时同步时，您可以选择DTS同步。

**日志采集**

日志采集时，您可以选用Flume、Fluentd及Logstash等工具。

### Tunnel SDK介绍

**6.4.1. 概述**

MaxCompute支持通过Tunnel SDK进行数据上传和下载。本文介绍如何使用主要接口进行会话管理，包括创建上传和下载会话以及自动路由配置等。

**接口说明**

不同版本的SDK在使用上有差别，准确信息以SDK Java Doc为准。

| 主要接口 | 描述 |
|---|---|
| TableTunnel | 访问MaxCompute Tunnel服务的入口类。 |
| TableTunnel.UploadSession | 表示一个向MaxCompute表中上传数据的会话。 |
| TableTunnel.DownloadSession | 表示一个向MaxCompute表中下载数据的会话。 |
| InstanceTunnel | 访问MaxCompute Tunnel服务的入口类。 |
| InstanceTunnel.DownloadSession | 表示一个向MaxCompute Instance中下载数据的会话。但只能用于下载以SELECT关键字开头的用于获取数据的SQL Instance。 |

**说明**

如果您使用Maven，可以从Maven库中搜索odps-sdk-core来获取不同版本的Java SDK，相关配置信息如下所示。

```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>odps-sdk-core</artifactId>
    <version>0.36.2</version>
</dependency>
```

对于Tunnel Endpoint，支持根据MaxCompute Endpoint自动路由，您无需进行配置。

#### 6.4.2. TableTunnel

TableTunnel接口支持在MaxCompute中上传和下载表数据。通过创建UploadSession和DownloadSession对象，用户可以高效管理数据传输过程，了解接口实现

#### 使用说明

TableTunnel是访问MaxCompute Tunnel服务的入口类，仅支持表数据（非视图）的上传和下载。

**接口定义**

```
public DownloadSession createDownloadSession(String projectName, String tableName); public DownloadSession createDownloadSession(String projectName, String tableName, PartitionSpec partitionSpec); public UploadSession createUploadSession(String projectName, String tableName); public UploadSession createUploadSession(String projectName, String tableName, PartitionSpec partitionSpec); public DownloadSession getDownloadSession(String projectName, String tableName, PartitionSpec partitionSpec, String id); public DownloadSession getDownloadSession(String projectName, String tableName, String id); public UploadSession getUploadSession(String projectName, String tableName, PartitionSpec partitionSpec, String id); public UploadSession getUploadSession(String projectName, String tableName, String id); public void setEndpoint(String endpoint); }
```

**接口说明**

TableTunnel提供创建UploadSession对象和DownloadSession对象的方法。数据的上传和下载分别由**TableTunnel.UploadSession**和**TableTunnel.DownloadSession**这两个Session实现。

**说明**

对一张表或分区上传下载的过程，称为一个Session。Session由一个或多个访问Tunnel RESTful API的HTTP Request组成。 同一Session中，使用同一Block ID多次打开RecordWriter的行为会导致数据覆盖，最后一个调用**close()**的RecordWriter所上传的数据会被保留。该特性可用于Block的上传失败重传。

**接口实现流程**

1. **RecordWriter.write()**将数据上传到临时目录的文件。
2. **RecordWriter.close()**将相应的文件从临时目录移到数据目录。
3. **session.commit()**将相应数据目录下的所有文件移到相应表所在目录，并更新表Meta，即数据进表。使数据对其它MaxCompute任务（例如SQL及

**接口限制**

Block ID的取值范围是[0,20000)，单个Block上传的数据限制为 `100 GB` 。 Session用Session ID来标识。Session的超时时间为24小时。如果大批量数据传送时长超过24小时，需要自行拆分成多个Session。

| RecordWriter对应的HTTP Request超时为 | 120s | 。如果 | 120s | 内HTTP连接上没有数据流过，Service端会主动关闭连接。 |
|---|---|---|---|---|
| 说明 HTTP本身还有8 KB的缓存，因此并不是每次调用RecordWriter.write()都能保证HTTP连接上有数据流过。TunnelRecordWriter.flush()可以将缓存内数据强制刷出。 |  |  |  |  |

对于日志类写入MaxCompute的场景，无法预测数据的到达时间会造成RecordWriter超时。因此： 不建议对每条数据打开一个RecordWriter。因为每个RecordWriter对应一个文件，此操作会造成小文件过多，严重影响MaxCompute后续使用性能。 建议用户代码Cache至少 `64 MB` 的数据后，再使用一个RecordWriter进行一次性批量写入。 RecordReader的超时时间为 `300s` 。

#### 6.4.3. InstanceTunnel

MaxCompute支持通过InstanceTunnel接口访问Tunnel服务，下载SQL Instance执行结果。本文介绍InstanceTunnel接口的使用方法及约束条件，包括创建和获取下载会话的方法及权限要求。

#### 使用说明

InstanceTunnel是访问MaxCompute Tunnel服务的入口类，您可以通过InstanceTunnel下载SELECT语句的SQL Instance的执行结果。

**接口定义**

**接口定义**：

```
    public DownloadSession createDownloadSession(String projectName, String instanceID);
    public DownloadSession createDownloadSession(String projectName, String instanceID, boolean limitEnabled);
    public DownloadSession getDownloadSession(String projectName, String id);
}
```

**参数说明**：
**projectName**：项目空间名称。
**instanceID**：用来标识Instance的ID。
虽然InstanceTunnel提供了非常方便的获取Instance执行结果的方式，但是为了保护您的数据安全，此功能也受到了权限约束。 使用InstanceTunnel下载数据时，如果数据条数不超过10000，则只要对该Instance有Read权限的用户即可以使用。此行为与使用Restful API获取查询数据的行为一致。 使用InstanceTunnel下载数据时，如果数据条数超过10000，则需要对Instance上的SQL查询语句中涉及到的所有源表进行权限检查，您需要具有这些表的Read 权限才可以使用。

#### 6.4.4. UploadSession

UploadSession接口支持数据分块上传及自动重试机制，帮助用户管理数据上传至MaxCompute表。本文介绍接口定义、生命周期、请求方式及数据提交的 overwrite模式。

**接口定义**

```
    UploadSession(Configuration conf, String projectName, String tableName, String partitionSpec) throws TunnelException;
    UploadSession(Configuration conf, String projectName, String tableName, String partitionSpec, String uploadId) throws
TunnelException;
    public void commit(Long[] blocks);
    public Long[] getBlockList();
    public String getId();
    public TableSchema getSchema();
    public UploadSession.Status getStatus();
    public Record newRecord();
    public RecordWriter openRecordWriter(long blockId);
    public RecordWriter openRecordWriter(long blockId, boolean compress);
    public RecordWriter openBufferedWriter();
    public RecordWriter openBufferedWriter(boolean compress);
}
```

**重要**

同一个Upload中Session的Block ID不能重复。即对于同一个UploadSession，用一个Block ID打开RecordWriter，写入一批数据，调用**close**接口， 最后再调用**commit**接口完成上传后。此时，不可以重新再用该Block ID打开另一个RecordWriter写入数据。 每一个Block的大小上限为 `100 GB` ，建议每个Block写入大于 `64 MB` 的数据，否则会严重影响计算性能。 每个Session在服务端的生命周期为24小时。 上传数据时，Writer每写入 `8 KB` 数据就会触发一次网络动作，如果 `120s` 内没有网络动作，服务端将主动关闭连接，此时Writer将不可用，需重新打开一个新的Writer写入。 建议使用**openBufferedWriter**接口上传数据，该接口对您屏蔽了Block ID的细节，并且内部带有数据缓存区，会自动进行失败重试。 UploadSession在Commit阶段增加了 `overwrite` 开关，支持以 `overwrite` 模式提交数据。以 `overwrite` 模式提交数据，会以本次Commit的数据覆盖掉表或分区内现有数据。

**重要**

多个Session并发以**overwrite**模式提交数据会有未定义行为产生，从而导致数据正确性风险。因此，使用 `overwrite` 模式上传数据需要您自己控制并发Commit。

**接口说明**

**生命周期**：从Upload实例被创建开始，一直到程序结束。
**创建****Upload****实例**：您可以通过调用构造方法和TableTunnel两种方式进行创建。
请求方式：同步。 Server端会为该Upload创建一个Session，生成唯一Upload ID标识该Upload，客户端可以通过 `getId` 获取该Upload ID。
**上传数据**：
请求方式：同步。 调用**openRecordWriter**接口，生成RecordWriter实例，其中参数Block ID用于标识此次上传的数据，也描述了数据在整个表中的位置，取值范围为 [0,20000)。当数据上传失败，可以根据Block ID重新上传。
**查看上传**：
请求方式：同步。 调用 `getStatus` 可以获取当前Upload状态。 调用 `getBlockList` 可以获取成功上传的Block ID List，可以和上传的Block ID List对比，对失败的Block ID重新上传。
**结束上传**：
请求方式：同步。 调用**Commit**（**Long[] blocks**）方法，参数**blocks**列表表示已经成功上传的Block列表，Server端会对该列表进行验证。 该功能是为加强对数据正确性的校验，如果提供的Block列表与Server端存在的Block列表不一致，则会报错。 Commit失败可以进行重试。
**状态说明**：
UNKNOWN：Server端刚创建一个Session时设置的初始值。 NORMAL：创建Upload对象成功。 CLOSING：当调用**Complete**方法（结束上传）时，服务端会先把状态置为CLOSING。 CLOSED：上传结束后（即把数据移动到结果表所在目录）。 EXPIRED：上传超时。 CRITICAL：服务出错。

#### 6.4.5. DownloadSession

本文介绍了 `DownloadSession` 接口的功能与使用方法，用于下载MaxCompute表数据。

**接口定义**

```
    DownloadSession(Configuration conf, String projectName, String tableName, String partitionSpec) throws TunnelException
    DownloadSession(Configuration conf, String projectName, String tableName, String partitionSpec, String downloadId) throws TunnelExcep
tion
    public String getId()
    public long getRecordCount()
    public TableSchema getSchema()
    public RecordReader openRecordReader(long start, long count)
    public RecordReader openRecordReader(long start, long count, boolean compress)
}
```

**接口说明**

**生命周期**：从Download实例被创建开始，一直到程序结束。
**创建****Download****实例**：您可以通过调用构造方法和TableTunnel两种方式进行创建。
请求方式：同步。 Server端会为该Download创建一个Session，生成唯一Download ID标识该Download，客户端可以通过 `getId` 获取该Download ID。 该操作开销较大，Server端会对数据文件创建索引，当文件数很多时，该时间会比较长。 同时Server端会返回总Record数，可以根据总Record数启动多个并发同时下载。
**下载数据**：
请求方式：异步。 调用**openRecordReader**接口，生成RecordReader实例，其中参数**start**标识本次下载的Record的起始位置，从0开始，取值范围大于等于0；count标识本次下载的记录数，取值范围大于0。
**查看下载**：
请求方式：同步。 调用 `getStatus` 可以获取当前Download状态。
**状态说明**：
UNKNOWN：Server端刚创建一个Session时设置的初始值。 NORMAL：创建Download对象成功。 CLOSED：下载结束后。 EXPIRED：下载超时。

#### 6.4.6. TunnelBufferedWriter

本文介绍TunnelBufferedWriter接口的功能和使用方法，简化数据上传过程。通过调整缓冲区大小和设置重试策略，优化上传性能并减少连接超时风险。

#### 使用说明

此接口用于上传数据。 由于服务端对Block管理及连接超时等限制，正常的上传过程会变得复杂，为了简化上传过程，SDK提供了更高级的一种RecordWriter——TunnelBufferedWriter。

**接口定义**

```java
public class TunnelBufferedWriter implements RecordWriter {
    public TunnelBufferedWriter(TableTunnel.UploadSession session, CompressOption option) throws IOException;
    public long getTotalBytes();
    public void setBufferSize(long bufferSize);
    public void setRetryStrategy(RetryStrategy strategy);
    public void write(Record r) throws IOException;
    public void close() throws IOException;
}
```

**接口说明**

**生命周期**：从创建RecordWriter到数据上传结束。
**创建****TunnelBufferedWriter****实例**：通过调用UploadSession的**openBufferedWriter**接口创建。
**数据上传**：调用**Write**接口，数据会先写入本地缓存区，缓存区满后会批量提交到服务端，这样可以避免连接超时。此外，如果数据上传失败，则会自动进行重试。
**结束上传**：调用**close**接口，最后再调用UploadSession的**commit**接口，即可完成上传。
**缓冲区控制**：可以通过**setBufferSize**接口修改缓冲区占内存的字节数（Byte），建议设置大于等于 `64 MB` ，避免服务端产生过多小文件，影响性能。最小可以
设置为 `1 MB` ，最大 `1000 MB` ，通常无需设置，维持默认值 `64 MB` 即可。
**重试策略设置**：您可以选择三种重试回避策略，指数回避（EXPONENTIAL_BACKOFF）、线性时间回避（LINEAR_BACKOFF）、常数时间回避

| 避 | 4s | 、 | _ 8s | 、 | 16s | 、 | 32s | 、 | 64s | 和 | 128s | （默认设置为2的指数倍递增序列，从4开始）。 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RetryStrategy retry = new RetryStrategy(6,4,RetryStrategy.BackoffStrategy.EXPONENTIAL_BACKOFF); writer = (TunnelBufferedWriter) uploadSession.openBufferedWriter(); writer.setRetryStrategy(retry); |  |  |  |  |  |  |  |  |  |  |  |  |

**说明**

通常情况下不建议调整上述回避设置。

### Tunnel SDK示例

#### 6.5.1. 简单上传示例

如果您希望使用Tunnel SDK进行数据上传操作，本文提供详细的Java代码示例。本文介绍了如何通过初始化账户信息、创建上传会话、准备数据并写入等步骤完成数据上传。

**代码示例**

```java
import java.io.IOException; import java.util.Date; import com.aliyun.odps.Column; import com.aliyun.odps.Odps; import com.aliyun.odps.PartitionSpec; import com.aliyun.odps.TableSchema; import com.aliyun.odps.account.Account; import com.aliyun.odps.account.AliyunAccount; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.RecordWriter; import com.aliyun.odps.tunnel.TableTunnel; import com.aliyun.odps.tunnel.TableTunnel.UploadSession; import com.aliyun.odps.tunnel.TunnelException; public class UploadSample {
    private static String accessId = "<your access id>";
    private static String accessKey = "<your access Key>";
    private static String tunnelUrl = "<your tunnel endpoint>";
    private static String odpsUrl = "<your odps endpoint>";
    private static String project = "<your project>";
    private static String table = "<your table name>";
    private static String partition = "<your partition spec>";
    public static void main(String[] args) {
        Account account = new AliyunAccount(accessId, accessKey);
        Odps odps = new Odps(account);
        odps.setEndpoint(odpsUrl);
        odps.setDefaultProject(project);
        try {
            TableTunnel tunnel = new TableTunnel(odps);
            tunnel.setEndpoint(tunnelUrl);
            PartitionSpec partitionSpec = new PartitionSpec(partition);
            UploadSession uploadSession = tunnel.createUploadSession(project, table, partitionSpec);
            System.out.println("Session Status is : " + uploadSession.getStatus().toString());
            TableSchema schema = uploadSession.getSchema();
```

`//` 准备数据后打开 `Writer` 开始写入数据，准备数据后写入一个 `Block`。 `//` 单个 `Block` 内写入数据过少会产生大量小文件严重影响计算性能， `//` 强烈建议每次写入 `64 MB` 以上数据 `(100 GB` 以内数据均可写入同一 `Block)`。 `//` 可通过数据的平均大小与记录数量大致计算总量即 `64 MB <` 平均记录大小*记录数 `< 100 GB`。

```
            RecordWriter recordWriter = uploadSession.openRecordWriter(0);
            Record record = uploadSession.newRecord();
            for (int i = 0; i < schema.getColumns().size(); i++) {
                Column column = schema.getColumn(i);
                switch (column.getType()) {
                    case BIGINT:
                        record.setBigint(i, 1L);
                        break;
                    case BOOLEAN:
                        record.setBoolean(i, true);
                        break;
                    case DATETIME:
                        record.setDatetime(i, new Date());
                        break;
                    case DOUBLE:
                        record.setDouble(i, 0.0);
                        break;
                    case STRING:
                        record.setString(i, "sample");
                        break;
                    default:
                        throw new RuntimeException("Unknown column type: " + column.getType());
                }
            }
            for (int i = 0; i < 10; i++) {
```

`// Write` 数据至服务端，每写入 `8 KB` 数据会进行一次网络传输。 `//` 如果 `120s` 没有网络传输服务端将会关闭连接，届时该 `Writer` 将不可用，需要重新写入。

```java
                recordWriter.write(record);
            }
            recordWriter.close();
            uploadSession.commit(new Long[]{0L});
            System.out.println("upload success!");
        } catch (TunnelException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### 6.5.2. 简单下载示例

本文通过Java代码示例展示使用Tunnel SDK下载数据的过程，包括设置账户信息、创建下载会话、读取记录并处理数据，帮助您快速实现从MaxCompute表中下载数据的功能。

**代码示例**

```java
import java.io.IOException; import java.util.Date; import com.aliyun.odps.Column; import com.aliyun.odps.Odps; import com.aliyun.odps.PartitionSpec; import com.aliyun.odps.TableSchema; import com.aliyun.odps.account.Account; import com.aliyun.odps.account.AliyunAccount; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.RecordReader; import com.aliyun.odps.tunnel.TableTunnel; import com.aliyun.odps.tunnel.TableTunnel.DownloadSession; import com.aliyun.odps.tunnel.TunnelException; public class DownloadSample {
    private static String accessId = "<your access id>";
    private static String accessKey = "<your access Key>";
    private static String tunnelUrl = "<your tunnel endpoint>";
    private static String odpsUrl = "<your odps endpoint>";
    private static String project = "<your project>";
    private static String table = "<your table name>";
    private static String partition = "<your partition spec>";
    public static void main(String[] args) {
        Account account = new AliyunAccount(accessId, accessKey);
```

```
ccoutaccout
```

`ew` `yu`

```java
ccout(accessd,accessey);
        Odps odps = new Odps(account);
        odps.setEndpoint(odpsUrl);
        odps.setDefaultProject(project);
        TableTunnel tunnel = new TableTunnel(odps);
        tunnel.setEndpoint(tunnelUrl);
        PartitionSpec partitionSpec = new PartitionSpec(partition);
        try {
            DownloadSession downloadSession = tunnel.createDownloadSession(project, table, partitionSpec);
            System.out.println("Session Status is : " + downloadSession.getStatus().toString());
            long count = downloadSession.getRecordCount();
            System.out.println("RecordCount is: " + count);
            RecordReader recordReader = downloadSession.openRecordReader(0, count);
            Record record;
            while ((record = recordReader.read()) != null) {
                consumeRecord(record, downloadSession.getSchema());
            }
            recordReader.close();
        } catch (TunnelException e) {
            e.printStackTrace();
        } catch (IOException e1) {
            e1.printStackTrace();
        }
    }
    private static void consumeRecord(Record record, TableSchema schema) {
        for (int i = 0; i < schema.getColumns().size(); i++) {
            Column column = schema.getColumn(i);
            String colValue = null;
            switch (column.getType()) {
                case BIGINT: {
                    Long v = record.getBigint(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                case BOOLEAN: {
                    Boolean v = record.getBoolean(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                case DATETIME: {
                    Date v = record.getDatetime(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                case DOUBLE: {
                    Double v = record.getDouble(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                case STRING: {
                    String v = record.getString(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                default:
                    throw new RuntimeException("Unknown column type: " + column.getType());
            }
            System.out.print(colValue == null ? "null" : colValue);
            if (i != schema.getColumns().size()) {
                System.out.print("\t");
            }
        }
        System.out.println();
    }
}
```

#### 6.5.3. 多线程上传示例

本文提供Tunnel SDK的多线程上传示例，展示如何通过多线程提高数据上传效率。使用 `ExecutorService` 创建线程池管理任务，并通过 `UploadThread` 实例和 `RecordWriter` 完成数据上传。本文介绍了如何通过多线程提高数据上传效率。

**代码示例**

```java
import java.io.IOException;
```

|  | import java.util.ArrayList; import java.util.Date; import java.util.concurrent.Callable; import java.util.concurrent.ExecutorService; import java.util.concurrent.Executors; import com.aliyun.odps.Column; import com.aliyun.odps.Odps; import com.aliyun.odps.PartitionSpec; import com.aliyun.odps.TableSchema; import com.aliyun.odps.account.Account; import com.aliyun.odps.account.AliyunAccount; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.RecordWriter; import com.aliyun.odps.tunnel.TableTunnel; import com.aliyun.odps.tunnel.TableTunnel.UploadSession; import com.aliyun.odps.tunnel.TunnelException; class UploadThread implements Callable<Boolean> { private long id; private RecordWriter recordWriter; private Record record; private TableSchema tableSchema; public UploadThread(long id, RecordWriter recordWriter, Record record, TableSchema tableSchema) { this.id = id; this.recordWriter = recordWriter; this.record = record; this.tableSchema = tableSchema; } @Override public Boolean call() { for (int i = 0; i < tableSchema.getColumns().size(); i++) { Column column = tableSchema.getColumn(i); switch (column.getType()) { case BIGINT: record.setBigint(i, 1L); break; case BOOLEAN: record.setBoolean(i, true); break; case DATETIME: record.setDatetime(i, new Date()); break; case DOUBLE: record.setDouble(i, 0.0); break; case STRING: record.setString(i, "sample"); break; default: throw new RuntimeException("Unknown column type: " + column.getType()); } } try { for (int i = 0; i < 10; i++) { // Write 数据至服务端，每写入 8 KB 数据会进行一次网络传输。 // 如果 120s 没有网络传输服务端将会关闭连接，届时该 Writer 将不可用，需要重新写入。 recordWriter.write(record); } recordWriter.close(); } catch (IOException e) { e.printStackTrace(); return false; } return true; } } public class UploadThreadSample { private static String accessId = "<your access id>"; private static String accessKey = "<your access Key>"; private static String tunnelUrl = "<your tunnel endpoint>"; private static String odpsUrl = "<your odps endpoint>"; private static String project = "<your project>"; private static String table = "<your table name>"; private static String partition = "<your partition spec>"; private static int threadNum = 10; public static void main(String[] args) { |  |
|---|---|---|

```java
    public static void main(String[] args) {
        Account account = new AliyunAccount(accessId, accessKey);
        Odps odps = new Odps(account);
        odps.setEndpoint(odpsUrl);
        odps.setDefaultProject(project);
        try {
            TableTunnel tunnel = new TableTunnel(odps);
            tunnel.setEndpoint(tunnelUrl);
            PartitionSpec partitionSpec = new PartitionSpec(partition);
            UploadSession uploadSession = tunnel.createUploadSession(project, table, partitionSpec);
            System.out.println("Session Status is : " + uploadSession.getStatus().toString());
            ExecutorService pool = Executors.newFixedThreadPool(threadNum);
            ArrayList<Callable<Boolean>> callers = new ArrayList<>();
```

`//` 准备数据后打开 `Writer` 开始多线程写入数据，准备数据后写入。 `//` 单个 `Block` 内写入数据过少会产生大量小文件严重影响计算性能， `//` 强烈建议每次写入 `64 MB` 以上数据 `(100 GB` 以内数据均可写入同一 `Block)`。 `//` 可通过数据的平均大小与记录数量大致计算总量即 `64 MB <` 平均记录大小*记录数 `< 100 GB`。

```java
            for (int i = 0; i < threadNum; i++) {
                RecordWriter recordWriter = uploadSession.openRecordWriter(i);
                Record record = uploadSession.newRecord();
                callers.add(new UploadThread(i, recordWriter, record, uploadSession.getSchema()));
            }
            pool.invokeAll(callers);
            pool.shutdown();
            Long[] blockList = new Long[threadNum];
            for (int i = 0; i < threadNum; i++) {
                blockList[i] = Long.valueOf(i);
            }
            uploadSession.commit(blockList);
            System.out.println("upload success!");
        } catch (TunnelException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

#### 6.5.4. 多线程下载示例

本文提供了使用Tunnel SDK进行多线程下载的Java示例代码。通过 `Callable` 接口和 `ExecutorService` 创建多线程环境，并使用 `TableTunnel` 和 `DownloadSession` 从ODPS表中下载数据，帮助您实现高效的数据读取和处理。

**代码示例**

```java
import java.io.IOException; import java.util.ArrayList; import java.util.Date; import java.util.List; import java.util.concurrent.Callable; import java.util.concurrent.ExecutionException; import java.util.concurrent.ExecutorService; import java.util.concurrent.Executors; import java.util.concurrent.Future; import com.aliyun.odps.Column; import com.aliyun.odps.Odps; import com.aliyun.odps.PartitionSpec; import com.aliyun.odps.TableSchema; import com.aliyun.odps.account.Account; import com.aliyun.odps.account.AliyunAccount; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.RecordReader; import com.aliyun.odps.tunnel.TableTunnel; import com.aliyun.odps.tunnel.TableTunnel.DownloadSession; import com.aliyun.odps.tunnel.TunnelException; class DownloadThread implements Callable<Long> {
    private long id;
    private RecordReader recordReader;
    private TableSchema tableSchema;
```

```java
    public DownloadThread(int id, RecordReader recordReader, TableSchema tableSchema) {
        this.id = id;
        this.recordReader = recordReader;
        this.tableSchema = tableSchema;
    }
    @Override
    public Long call() {
        Long recordNum = 0L;
        try {
            Record record;
            while ((record = recordReader.read()) != null) {
                recordNum++;
                System.out.print("Thread " + id + "\t");
                consumeRecord(record, tableSchema);
            }
            recordReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return recordNum;
    }
    private static void consumeRecord(Record record, TableSchema schema) {
        for (int i = 0; i < schema.getColumns().size(); i++) {
            Column column = schema.getColumn(i);
            String colValue = null;
            switch (column.getType()) {
                case BIGINT: {
                    Long v = record.getBigint(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                case BOOLEAN: {
                    Boolean v = record.getBoolean(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                case DATETIME: {
                    Date v = record.getDatetime(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                case DOUBLE: {
                    Double v = record.getDouble(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                case STRING: {
                    String v = record.getString(i);
                    colValue = v == null ? null : v.toString();
                    break;
                }
                default:
                    throw new RuntimeException("Unknown column type: " + column.getType());
            }
            System.out.print(colValue == null ? "null" : colValue);
            if (i != schema.getColumns().size()) {
                System.out.print("\t");
            }
        }
        System.out.println();
    }
} public class DownloadThreadSample {
    private static String accessId = "<your access id>";
    private static String accessKey = "<your access Key>";
    private static String tunnelUrl = "<your tunnel endpoint>";
    private static String odpsUrl = "<your odps endpoint>";
    private static String project = "<your project>";
    private static String table = "<your table name>";
    private static String partition = "<your partition spec>";
    private static int threadNum = 10;
    public static void main(String[] args) {
        Account account = new AliyunAccount(accessId, accessKey);
        Odps odps = new Odps(account);
        odps.setEndpoint(odpsUrl);
```

d f l j

```
(
```

j )

```java
        odps.setDefaultProject(project);
        TableTunnel tunnel = new TableTunnel(odps);
        tunnel.setEndpoint(tunnelUrl);
        PartitionSpec partitionSpec = new PartitionSpec(partition);
        DownloadSession downloadSession;
        try {
            downloadSession = tunnel.createDownloadSession(project, table, partitionSpec);
            System.out.println("Session Status is : " + downloadSession.getStatus().toString());
            long count = downloadSession.getRecordCount();
            System.out.println("RecordCount is: " + count);
            ExecutorService pool = Executors.newFixedThreadPool(threadNum);
            ArrayList<Callable<Long>> callers = new ArrayList<>();
            long start = 0;
            long step = count / threadNum;
            for (int i = 0; i < threadNum - 1; i++) {
                RecordReader recordReader = downloadSession.openRecordReader(step * i, step);
                callers.add(new DownloadThread(i, recordReader, downloadSession.getSchema()));
            }
            RecordReader recordReader = downloadSession.openRecordReader(
                    step * (threadNum - 1), count + ((threadNum - 1) * step));
            callers.add(new DownloadThread(threadNum - 1, recordReader, downloadSession.getSchema()));
            Long downloadNum = 0L;
            List<Future<Long>> recordNum = pool.invokeAll(callers);
            for (Future<Long> num : recordNum) {
                downloadNum += num.get();
            }
            System.out.println("Record Count is: " + downloadNum);
            pool.shutdown();
        } catch (TunnelException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
    }
}
```

#### 6.5.5. BufferedWriter上传示例

本文介绍如何使用Tunnel SDK的BufferedWriter进行数据上传，包括初始化MaxCompute和Tunnel、创建上传会话、写入数据并提交上传。

**代码示例**

`//` 初始化 `MaxCompute` 和 `Tunnel` 的代码。

```
RecordWriter writer = null; TableTunnel.UploadSession uploadSession = tunnel.createUploadSession(projectName, tableName); try {
    int i = 0;
    writer = uploadSession.openBufferedWriter();
    Record product = uploadSession.newRecord();
    for (String item : items) {
        product.setString("name", item);
        product.setBigint("id", i);
```

`//` 调用 `Write` 接口写入数据。

```
        writer.write(product);
        i++;
    }
} finally {
    if (writer != null) {
        writer.close();
    }
} uploadSession.commit();
```

#### 6.5.6. BufferedWriter多线程上传示例

本文提供使用Tunnel SDK进行多线程上传的示例，通过 `UploadThread` 类和 `BufferedWriter` 实现数据写入与提交。本文介绍了如何通过多线程提高数据上传效率。

**代码示例**

```java
class UploadThread extends Thread {
  private UploadSession session;
  private static int RECORD_COUNT = 1200;
    this.session = session;
  }
  @Override
  public void run() {
    RecordWriter writer = up.openBufferedWriter();
    Record r = up.newRecord();
    for (int i = 0; i < RECORD_COUNT; i++) {
      r.setBigint(0, i);
      writer.write(r);
    }
    writer.close();
  }
}; public class Example {
  public static void main(String[] args) {
```

`//` 初始化`MaxCompute`和`Tunnel`的代码。

```
   TableTunnel.UploadSession uploadSession = tunnel.createUploadSession(projectName, tableName);
   UploadThread t1 = new UploadThread(up);
   UploadThread t2 = new UploadThread(up);
   t1.start();
   t2.start();
   t1.join();
   t2.join();
   uploadSession.commit();
}
```

#### 6.5.7. 复杂数据类型上传下载示例

本文提供使用Tunnel SDK上传下载复杂数据类型的示例，演示如何通过RecordWriter和RecordReader处理数组、映射和结构体数据。本文介绍Tunnel SDK的复杂数据类型上传下载示例。

**上传复杂类型数据**

```
RecordWriter recordWriter = uploadSession.openRecordWriter(0); ArrayRecord record = (ArrayRecord) uploadSession.newRecord();
```

`//`准备数据。

```
List arrayData = Arrays.asList(1, 2, 3); Map<String, Long> mapData = new HashMap<String, Long>(); mapData.put("a", 1L); mapData.put("c", 2L); List<Object> structData = new ArrayList<Object>(); structData.add("Lily"); structData.add(18);
```

`//`将数据传入`Record`。

```
record.setArray(0, arrayData); record.setMap(1, mapData); record.setStruct(2, new SimpleStruct((StructTypeInfo) schema.getColumn(2).getTypeInfo(), structData));
```

`//`写入`Record`。

```
recordWriter.write(record);
```

**下载复杂类型数据**

```
RecordReader recordReader = downloadSession.openRecordReader(0, 1);
```

`//`读取`Record`。

```
ArrayRecord record1 = (ArrayRecord)recordReader.read();
```

`//`获取`ARRAY`数据。

```
List field0 = record1.getArray(0); List<Long> longField0 = record1.getArray(Long.class, 0);
```

`//`获取`NAP`数据。

```
Map field1 = record1.getMap(1); Map<String, Long> typedField1 = record1.getMap(String.class, Long.class, 1);
```

`//`获取`STRUCT`数据。

```
Struct field2 = record1.getStruct(2);
```

**上传下载运行实例**

```java
import java.io.IOException; import java.util.ArrayList; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; import com.aliyun.odps.Odps; import com.aliyun.odps.PartitionSpec; import com.aliyun.odps.TableSchema; import com.aliyun.odps.account.Account; import com.aliyun.odps.account.AliyunAccount; import com.aliyun.odps.data.ArrayRecord; import com.aliyun.odps.data.RecordReader; import com.aliyun.odps.data.RecordWriter; import com.aliyun.odps.data.SimpleStruct; import com.aliyun.odps.data.Struct; import com.aliyun.odps.tunnel.TableTunnel; import com.aliyun.odps.tunnel.TableTunnel.UploadSession; import com.aliyun.odps.tunnel.TableTunnel.DownloadSession; import com.aliyun.odps.tunnel.TunnelException; import com.aliyun.odps.type.StructTypeInfo; public class TunnelComplexTypeSample {
```

`//` 阿里云账号`AccessKey`拥有所有`API`的访问权限，风险很高。强烈建议您创建并使用`RAM`用户进行`API`访问或日常运维，请登录`RAM`控制台创建`RAM`用户 `//` 此处以把`AccessKey` 和 `AccessKeySecret` 保存在环境变量为例说明。您也可以根据业务需要，保存到配置文件里 `//` 强烈建议不要把 `AccessKey` 和 `AccessKeySecret` 保存到代码里，会存在密钥泄漏风险

```java
  private static String accessId = "<your access id>";
  private static String accessKey = "<your access Key>";
  private static String odpsUrl = "<your odps endpoint>";
  private static String project = "<your project>";
  private static String table = "<your table name>";
```

`//`一个分区表里的分区，例如"pt=\'1\',ds=\'2\'"。 `//`如果该表不是一个分区表，则不需要以下语句。

```java
  private static String partition = "<your partition spec>";
  public static void main(String[] args) {
    Account account = new AliyunAccount(accessId, accessKey);
    Odps odps = new Odps(account);
    odps.setEndpoint(odpsUrl);
    odps.setDefaultProject(project);
    try {
      TableTunnel tunnel = new TableTunnel(odps);
      PartitionSpec partitionSpec = new PartitionSpec(partition);
      //---------- 上传数据 ---------------
```

`//`为表创建上传会话。

```
      //表Schema为{"col0": ARRAY<BIGINT>, "col1": MAP<STRING, BIGINT>, "col2": STRUCT<name:STRING,age:BIGINT>}。
      UploadSession uploadSession = tunnel.createUploadSession(project, table, partitionSpec);
```

`//`获取表`Schema`。

```
      TableSchema schema = uploadSession.getSchema();
```

`//`开启`Record Writer`。

```
      RecordWriter recordWriter = uploadSession.openRecordWriter(0);
```

```
      ArrayRecord record = (ArrayRecord) uploadSession.newRecord();
```

`//`准备数据。

```
      List arrayData = Arrays.asList(1, 2, 3);
      Map<String, Long> mapData = new HashMap<String, Long>();
      mapData.put("a", 1L);
      mapData.put("c", 2L);
      List<Object> structData = new ArrayList<Object>();
      structData.add("Lily");
      structData.add(18);
```

`//`将数据传入`Record`。

```
      record.setArray(0, arrayData);
      record.setMap(1, mapData);
      record.setStruct(2, new SimpleStruct((StructTypeInfo) schema.getColumn(2).getTypeInfo(), structData));
```

`//`写入`Record`。

```
      recordWriter.write(record);
```

`//`关闭`Writer`。

```java
      recordWriter.close();
      uploadSession.commit(new Long[]{0L});
      System.out.println("upload success!");
      //---------- 下载数据 ---------------
```

`//`为表创建下载会话。

```
      //表Schema为{"col0": ARRAY<BIGINT>, "col1": MAP<STRING, BIGINT>, "col2": STRUCT<name:STRING, age:BIGINT>}。
      DownloadSession downloadSession = tunnel.createDownloadSession(project, table, partitionSpec);
      schema = downloadSession.getSchema();
```

`//`开启`Record Reader,` 示例为读取一个`Record`。

```
      RecordReader recordReader = downloadSession.openRecordReader(0, 1);
```

`//`读取`Record`。

```
      ArrayRecord record1 = (ArrayRecord)recordReader.read();
```

`//`获取`ARRAY`数据。

```
      List field0 = record1.getArray(0);
      List<Long> longField0 = record1.getArray(Long.class, 0);
```

`//`获取`MAP`数据。

```
      Map field1 = record1.getMap(1);
      Map<String, Long> typedField1 = record1.getMap(String.class, Long.class, 1);
```

`//`获取`STRUCT`数据。

```java
      Struct field2 = record1.getStruct(2);
      System.out.println("download success!");
    } catch (TunnelException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

### 附录

#### 6.6.1. Tunnel上传下载常见问题

MaxCompute Tunnel支持数据上传和下载，提供Block ID管理、Session生命周期、超时处理等功能。本文介绍Tunnel上传下载时的常见问题。

**MaxCompute Tunnel是什么？**

Tunnel是MaxCompute的数据通道，您可以通过Tunnel向MaxCompute中上传或下载数据。Tunnel仅支持表（不包括视图View）数据的上传下载。

**Block ID是否可以重复？**

同一个UploadSession里的Block ID不能重复。即对于同一个UploadSession，用一个Block ID打开RecordWriter，写入一批数据，调用**close**接口，最后再调用**commit**接口完成上传后，不可以重新再用该Block ID打开另一个RecordWriter写入数据。Block ID的取值范围是[0,20000)。

**Block大小是否存在限制？**

每个Block的大小上限为 `100 GB` ，建议每个Block写入大于 `64 MB` 的数据。每一个Block对应一个文件，小于 `64 MB` 的文件统称为小文件，小文件过多会影响使用性能。

**Session是否可以共享使用，存在生命周期吗？**

每个Session在服务端的生命周期为24小时，创建后24小时内均可使用，也可以跨进程或跨线程共享使用，但是必须保证同一个Block ID没有重复使用。分布式上传可以按照如下步骤进行：
1. 创建Session。
2. 数据量估算。
3. 分配Block（例如线程1使用0~100，线程2使用100~200）。
4. 准备数据。
5. 上传数据。
6. Commit所有写入成功的Block。

**遇到Write/Read超时或IOException怎么处理？**

上传数据时：Writer每写入 `8 KB` 数据会触发一次网络动作，如果 `120s` 内没有网络动作，服务端将主动关闭连接。此时Writer将不可用，需要重新打开一个新的 Writer写入。 下载数据时：Reader也有类似机制，如果长时间没有网络IO，会被断开连接。建议Read过程连续进行，中间不穿插其他系统的接口。

**MaxCompute Tunnel支持哪些语言的SDK？**

MaxCompute Tunnel支持Java版的SDK。

**MaxCompute Tunnel是否支持多个客户端同时上传同一张表？**

支持。

**MaxCompute Tunnel适合批量上传还是流式上传？**

MaxCompute Tunnel适用于批量上传，不适合流式上传。

**MaxCompute Tunnel上传数据时一定要先存在分区吗？**

是的，Tunnel不会自动创建分区。

**Dship与MaxCompute Tunnel的关系？**

Dship是一个工具，通过MaxCompute Tunnel进行数据的上传下载。

**Tunnel Upload数据的行为是追加还是覆盖？**

追加的模式。

**Tunnel路由功能是怎么回事？**

路由功能指的是Tunnel SDK通过设置MaxCompute获取Tunnel Endpoint的功能。因此，SDK可以只设置MaxCompute的Endpoint即可正常工作。

**用MaxCompute Tunnel上传数据时，每个Block的数据量大小多大比较合适？**

需要综合考虑网络情况、实时性要求、数据如何使用以及集群小文件等因素。通常情况下，如果数据量较大，是持续上传的模式，可以在 `64 MB` ~ `256 MB` 之间； 如果是每天上传一次的批量模式，可以设置到 `1 GB` 左右。

**使用MaxCompute Tunnel 下载，总是提示Timeout是什么问题？**

通常是Endpoint错误，需要检查Endpoint配置，简单的判断方法是通过Telnet等方法检测网络连通性。

**通过MaxCompute Tunnel下载，报出如下错误的原因是什么？**

```
You have NO privilege ‘odps:Select‘ on {acs:odps:*:projects/XXX/tables/XXX}. project ‘XXX‘ is protected
```

导致上述报错的原因是该Project开启了数据保护功能，您的操作是从一个项目的数据导向另一个项目，此操作需要该Project的Owner进行授权。

**通过MaxCompute Tunnel上传，报出如下错误的原因是什么？**

```
ErrorCode=FlowExceeded, ErrorMessage=Your flow quota is exceeded.**
```

导致上述报错的原因是Tunnel对请求的并发数进行了控制，默认上传和下载的并发Quota为2000，任何相关的请求发出到结束过程中均会占用一个Quota单位。如果出现类似错误，有如下几种建议的解决方案： Sleep一下再重试。 将Project的Tunnel并发Quota调大，此操作需要联系管理员评估流量压力。 将问题报告给Project owner，调查谁占用了大量并发Quota并进行控制。

#### 6.6.2. Tunnel常见错误码

本文提供Tunnel常见错误码说明及处理建议，帮助您识别和解决上传下载问题。本文介绍Tunnel常见的错误码。

**常见错误码列表**

Tunnel常见的错误码如下所示。

| ErrorCode | 错误原因 | 处理建议 |
|---|---|---|
| NoSuchPartition | 分区不存在。 | Tunnel不会创建分区，需要您自行创建分区后再进行上传下载操作。 |
| InvalidProjectTable | 项目名称或表名称不合法。 | 重新命名合法的项目名称或表名称。 |
| NoSuchProject | 项目不存在。 | 检查项目名称是否输入正确。 |
| NoSuchTable | 表不存在。 | 检查表名称是否输入正确。 |
| StatusConflict | Session过期或已经Commit过。 | 重新创建Session上传。 |
| MalformedDataStream | 数据格式错误。 | 通常是网络断开或Schema与Table不一致导致的，根据实际情况解决问题即可。 |
| InvalidPartitionSpec | 分区信息不合法。 | 请检查分区信息，正确值示例类似如下所示：pt='1',ct='2017' |
| InvalidRowRange | 指定行数不合法，通常是超出了数据最大Size或者为0。 | 检查相关参数。 |

| Unauthorized | 账号信息错误。 | 通常是AccessKey ID或AccessKey Secret有误，或本地机器时间与服务端时间差距15分钟以上。 |
|---|---|---|
| DataStoreError | 存储错误。 | 建议联系管理员。 |
| NoPermission | 权限不足，通常原因是无相关权限或者设置了IP白名单。 | 检查权限是否正确。 |
| MissingPartitionSpec | 缺失分区信息，分区表操作必须携带分区信息。 | 补充分区信息。 |
| TableModified | 表数据在上传下载期间被其他任务改动。 | 重新创建Session重试。 |
| FlowExceeded | 超出并发Quota限制。 | 建议检查控制并发量，如果确实需要增加并发，请联系Project Owner或管理员评估流量压力。 |
| InvalidResourceSpec | 通常为Project、Table及Partition信息与Session不一致。 | 建议检查相关信息并重试。 |
| MethodNotAllowed | 方法不支持，通常是尝试导出View。 | 不支持View导出。 |
| InvalidColumnSpec | 列信息错误。 | 通常是指定列下载时列名错误。 |
| DataVersionConflict | 服务正在进行跨集群复制。 | 请稍等后重试。 |
| InternalServerError | 内部错误。 | 建议重试或联系管理员。 |

## 多引擎支持

### MapReduce

**7.1.1. 概述**

**MaxCompute MapReduce**：MaxCompute的原生接口，执行速度快、开发快捷、不暴露文件系统。
**MaxCompute****扩展****MapReduce**（**MR2**）：对MaxCompute MapReduce的扩展，支持更复杂的作业调度逻辑。MapReduce的实现方式与MaxCompute原
生接口一致。

**说明**

以上两个版本在基本概念、作业提交、输入与输出及资源使用等方面基本一致，仅各版本的Java SDK有所不同。

### 7.1.1.1. MapReduce

MaxCompute支持两种MapReduce编程接口。本文介绍MaxCompute的MapReduce接口功能，描述了处理流程和应用场景，适用于复杂数据处理任务。

**应用场景**

搜索：网页爬取、倒排索引及PageRank。 Web访问日志分析： 分析和挖掘用户在Web上的访问、购物行为特征，实现个性化推荐。 分析用户访问行为。 文本统计分析： 热门小说的字数统计（WordCount）和词频TFIDF分析。 学术论文及专利文献的引用分析和统计。 维基百科数据分析。 海量数据挖掘：非结构化数据、时空数据和图像数据挖掘。 机器学习：监督学习、无监督学习和分类算法（例如决策树及SVM）。 自然语言处理： 基于大数据的训练和预测。 基于语料库构建单词同现矩阵，频繁项集数据挖掘及重复文档检测等。 广告推荐：用户点击（CTR）和购买行为（CVR）预测。

**操作原理**

MapReduce处理数据过程主要分成Map和Reduce两个阶段。首先执行Map阶段，再执行Reduce阶段。Map和Reduce的处理逻辑由用户自定义实现，但要符合
1. 在正式执行Map前，需要将输入数据进行**分片**。即将输入数据切分为大小相等的数据块，每一块作为单个Map Worker的输入被处理，以便多个Map Worker能够并
行工作。
2. 分片完毕后，多个Map Worker即可以开始同时工作。每个Map Worker在读入各自的数据后，进行计算处理，最终输出给Reduce。

**说明**

Map Worker在输出数据时，需要为每一条输出数据指定一个Key。这个Key值决定了这条数据将会被发送给哪一个Reduce Worker。Key值和Reduce Worker是多对一的关系，具有相同Key的数据会被发送给同一个Reduce Worker，单个Reduce Worker有可能会接收到多个Key值的数据。
3. 在进入Reduce阶段之前，MapReduce框架会对数据按照Key值排序，使得具有相同Key的数据彼此相邻。如果您指定了**合并操作（****Combiner**），框架会调用
Combiner，将具有相同Key的数据进行聚合。

**说明**

Combiner的逻辑可以由您自定义实现。与经典的MapReduce框架协议不同，在MaxCompute中，Combiner的输入、输出参数必须与Reduce保持一致。这部分的处理通常也叫做**洗牌（****Shuffle**）。
4. 进入Reduce阶段，相同的Key的数据会到达同一个Reduce Worker。同一个Reduce Worker会接收来自多个Map Worker的数据。每个Reduce Worker会对
Key相同的数据进行Reduce操作。最后，一个Key的多条数据经过Reduce的作用后，将变成一个值。
5. 输出结果数据。

**操作示例**

下面将以WordCount为例，为您介绍MaxCompute MapReduce各个阶段的概念。 假设存在一个文本 `a.txt` ，文本内每行是一个数字，您要统计每个数字出现的次数。文本内的数字称为Word，数字出现的次数称为Count。如果MaxCompute
1. 对文本 `a.txt` 进行分片，将每片内的数据作为单个Map Worker的输入。
2. Map处理输入，每获取一个数字，将数字的Count设置为1，并将**<Word,Count>**对输出，此时以Word作为输出数据的Key。
3. 在Shuffle阶段前期，首先对每个Map Worker的输出，按照Key值，即Word值排序。排序后进行Combine操作，即将Key值（Word值）相同的Count累加，构成
一个新的**<Word,Count>**对。此过程被称为合并排序。
4. 在Shuffle阶段后期，数据被发送到Reduce端。Reduce Worker收到数据后依赖Key值再次对数据排序。
5. Reduce阶段，每个Reduce Worker对数据进行处理时，采用与Combiner相同的逻辑，将Key值（Word值）相同的Count累加，得到输出结果。

**说明**

由于MaxCompute的所有数据都被存放在表中，因此MaxCompute MapReduce的输入、输出只能是表，不允许您自定义输出格式，不提供类似文件系统的接口。

##### 7.1.1.2. 扩展MapReduce

MaxCompute支持扩展MapReduce（MR2），通过减少冗余磁盘IO和优化调度模型，提高数据处理效率。本文介绍了MR2模型的独特性和优势。

**特性说明**

传统的MapReduce模型要求每一轮MapReduce操作之后，数据必须落地到分布式文件系统上（例如HDFS或MaxCompute表）。MapReduce模型通常由多个 MapReduce作业组成，每个作业执行完成后都需要将数据写入磁盘。然而后续的Map任务很可能只需要读取一遍这些数据，为之后的Shuffle阶段做准备，这种情况就产生了冗余的磁盘I/O操作。 MaxCompute的计算调度逻辑可以支持更复杂的编程模型，针对上述情况，可以在Reduce后面直接执行下一次的Reduce操作，而不需要中间插入一个Map操作。 因此，MaxCompute提供了扩展的MapReduce模型，即可以支持Map后连接任意多个Reduce操作，例如Map-Reduce-Reduce。 MaxCompute支持的扩展MapReduce（MR2）改变了底层的调度和IO模型，可避免作业时冗余的IO操作。 Hadoop Chain Mapper/Reducer也支持类似的串行化Map或Reduce操作，但和MaxCompute的扩展MapReduce（MR2）模型有本质的区别。 Chain Mapper/Reducer基于传统的MapReduce模型，仅可以在原有的Mapper或Reducer后增加一个或多个Mapper操作（不允许增加Reducer）。这样的优点是，您可以复用之前的Mapper业务逻辑，把一个Map或Reduce拆成多个Mapper阶段，同时本质上并没有改变底层的调度和I/O模型。

#### 7.1.2. 应用限制

本文详细介绍了MapReduce服务在实例内存、任务并发度、资源引用、输入输出规模、数据类型支持及超时重试等方面的具体使用限制与默认配置参数。

**使用限制**

Instance内存占用的取值范围是[256 MB,12 GB]。单个Map Instance或Reduce Instance占用框架Memory默认为 `2048 MB` ，占用JVM的Heap Memory默认为 `1024 MB` 。 单个任务引用的资源数量不超过256个，分区表按照一个单位计算；单个任务的输入路数不能超过1024个，单个任务的输出路数不能超过256个；单个任务中自定义Counter的数量不能超过64个；单个任务引用的资源总计字节数大小不超过 `2 GB` 。 单个Job的Map Instance个数由框架根据Split Size计算得出，如果没有输入表，可以通过**odps.stage.mapper.num**直接设置，范围[1,100000]。 单个Job默认Reduce Instance个数为Map Instance个数的1/4，您可以设置Reduce Instance个数，范围是[0,2000]。可能出现如下的情况：Reduce处理的数据量会比Map大很多倍，导致Reduce阶段比较慢，而Reduce只能最多起2000个。 单个Reduce Instance或Map Instance失败重试次数为3，一些不可重试的异常会直接导致作业失败。 本地运行模式下，默认Map Instance个数为2，不能超过100；默认Reduce Instance个数为1，不能超过100；默认一路输入下载记录数100，不能超过10000。 单个Map Instance或Reduce Instance重复读一个资源次数限制小于等于64次。 框架会参考设置的Split Size值来划分Map，决定Map的个数。 MaxCompute表STRING列内容长度不允许超过 `8 MB` 。 Map或者Reduce Worker在无数据读写且没有通过 `context.progress()` 主动发送心跳的情况下，超时时间默认值是 `600s` 。 MapReduce任务引用表资源时，支持的数据类型为BIGINT、DOUBLE、STRING、DATETIME及BOOLEAN类型。如果表字段有其他数据类型，则会报错。

#### 7.1.3. 功能介绍

##### 7.1.3.1. 运行命令

本文介绍如何使用MaxCompute客户端的JAR命令运行MapReduce作业，通过设置运行模式、命令格式、参数配置及示例帮助高效执行数据处理任务。

#### 使用说明

**命令格式**

**命令格式**

```
Usage: jar [<GENERIC_OPTIONS>] <MAIN_CLASS> [ARGS] -conf <configuration_file> Specify an application configuration file -classpath <local_file_list> classpaths used to run mainClass -D <name>=<value> Property value pair, which will be used to run mainClass -local Run job in local mode -resources <resource_name_list> file/table resources used in mapper or reducer, seperate by comma
```

**参数说明**

| 参数 | 说明 |
|---|---|
| -conf <configuration file> | 指定JobConf配置文件。 |
| -classpath <localfilelist> _ _ | 本地执行时的classpath，主要用于指定Main函数所在的JAR包的本地路径（包含相对路径和绝对路径）。 |
| -D <propname>=<propvalue> _ _ | 本地执行时，<mainClass>的Java属性，可以定义多个。 |
| -local | 以本地模式执行MapReduce作业，主要用于程序调试。 |
| -resources <resourcenamelist> _ _ | MapReduce作业运行时使用的资源声明。通常情况下，resourcenamelist中需要指定Map/Reduce函数所在 _ _ 的资源名称。 说明如果您在Map/Reduce函数中读取了其他MaxCompute资源，这些资源名称也需要被添加到resourcenamelist中，资源之间使用逗号分隔。跨项目空间使用资源时，需要在前面加 _ _ 上 PROJECT_NAME/resources/ ，例如- resources otherproject/resources/resfile 。 |

您可以通过**-conf**选项指定JobConf配置文件。该文件可以影响SDK中JobConf的设置。下面给出一个JobConf配置文件的示例。

```xml
<configuration> <property> <name>import.filename</name> <value>resource.txt</value> </property> </configuration>
```

**使用示例**

在上述示例中，通过JobConf配置文件定义一个名为import.filename的变量，该变量的值为resource.txt。您可以在MapReduce程序中通过JobConf接口获取该变

```
jar -resources mapreduce-examples.jar -classpath mapreduce-examples.jar org.alidata.odps.mr.examples.WordCount wc_in wc_out add file data/src.txt jar -resources src.txt,mapreduce-examples.jar -classpath mapreduce-examples.jar org.alidata.odps.mr.examples.WordCount wc_in wc_out add file data/a.txt add table wc_in as test_table add jar work.jar jar -conf odps-mapred.xml -resources a.txt,test_table,work.jar -classpath work.jar:otherlib.jar -D import.filename=resource.txt org.alidata.odps.mr.examples.WordCount args
```

### 7.1.3.2. 基本概念

###### 7.1.3.2.1. Map/Reduce

本文介绍MapReduce的执行流程，涵盖Map/Reduce的调用规律及Setup/Cleanup的使用规范，以确保Worker任务的初始化和清理工作有序进行。

#### 使用说明

Map和Reduce分别支持对应的Map/Reduce方法、Setup方法及Cleanup方法。Setup方法在Map/Reduce方法之前调用，每个Worker调用且仅调用一次。 Cleanup方法在Map/Reduce方法之后调用，每个Worker调用且仅调用一次。

**说明**

详细使用示例请参见示例程序。

**7.1.3.2.2. 排序**

#### 使用说明

支持使用Map输出的Key Record中的特定几列作为排序（Sort）依据，但不支持自定义比较器。同时，您可以从这些排序列中选取部分列作为Group列，不过也不支持自定义Group比较器。Sort列主要用于数据的基本排序，而Group列则用于实现更精细的数据分组或二次排序。

**说明**

**7.1.3.2.3. 哈希**

#### 使用说明

支持设置哈希（partition）列及用户自定义哈希函数（partitioner）。哈希列的使用优先级高于自定义哈希函数。哈希函数用于将Map端的输出数据按照哈希逻辑分配到不同的Reduce Worker上。

**7.1.3.2.4. 归并**

#### 使用说明

归并（Combiner）函数将Shuffle阶段相邻的Record进行归并。您可以根据不同的业务逻辑选择是否使用归并函数。 归并函数是MapReduce计算框架的一种优化，通常情况下，Combiner的逻辑与Reduce相同。当Map输出数据后，框架会在Map端对相同Key值的数据进行本地的归并操作。

**说明**

详细使用示例请参见示例程序。

##### 7.1.3.3. 作业提交

MaxCompute支持通过JAR命令来运行和提交MapReduce作业。本文将详细介绍命令格式、参数说明以及示例应用。

**命令格式**

MaxCompute客户端提供JAR命令用于运行MapReduce作业，命令格式如下。

```
jar [<GENERIC_OPTIONS>] <MAIN_CLASS> [ARGS];
        -conf <configuration_file>         Specify an application configuration file
        -resources <resource_name_list>    file\table resources used in mapper or reducer, seperate by comma
        -classpath <local_file_list>       classpaths used to run mainClass
        -D <name>=<value>                  Property value pair, which will be used to run mainClass
        -l                                 Run job in local mode
```

**参数说明**

**-conf <configuration file>**：指定JobConf配置文件。该配置文件可以影响SDK中JobConf的设置。

```xml
<configuration>
  <property>
    <name>import.filename</name>
    <value>resource.txt</value>
  </property>
</configuration>
```

在上述示例中，通过JobConf配置文件定义一个名为import.filename的变量，该变量的值为resource.txt。您可以在MapReduce程序中通过JobConf接口获取该变量的值。通过SDK中JobConf接口您可以达到相同的目的，详情请参见资源使用示例。 示例如下。

```
add jar data\mapreduce-examples.jar;
    jar -resources mapreduce-examples.jar -classpath data\mapreduce-examples.jar
        org.alidata.odps.mr.examples.WordCount wc_in wc_out;
    add file data\src.txt;
    add jar data\mapreduce-examples.jar;
    jar -resources src.txt,mapreduce-examples.jar -classpath data\mapreduce-examples.jar
        org.alidata.odps.mr.examples.WordCount wc_in wc_out;
    add file data\a.txt;
    add table wc_in as test_table;
    add jar data\work.jar;
    jar -conf odps-mapred.xml -resources a.txt,test_table,work.jar
        -classpath data\work.jar:otherlib.jar
        -D import.filename=resource.txt org.alidata.odps.mr.examples.WordCount args;
```

**-resources <resource_name_list>**：MapReduce作业运行时使用的资源声明。通常情况下，resource_name_list中需要指定Map/Reduce函数所在的资
源名称。

**说明**

如果用户在Map/Reduce函数中读取了其他MaxCompute资源，则这些资源名称也需要被添加到resource_name_list中。资源之间使用半角逗号（,）分隔。 使用跨项目空间使用资源时，需要在前面加上 `PROJECT/resources/` ，例如 `-resources otherproject/resources/resfile` 。
**-classpath <local_file_list>**：本地执行时的**classpath**，主要用于指定Main函数所在的JAR包的本地路径（包含相对路径和绝对路径）。包名之间使用系统
默认的文件分割符进行分割。通常情况下，Windows系统中使用分号（;），Linux系统中使用半角逗号（,）。如果您在云端服务器运行MapReduce任务，则使用半角逗号（,）进行分隔。

**说明**

通常，您可能更习惯于将Main函数与Map/Reduce函数编写在一个包中。因此，在执行相关程序时，-resources及-classpath的参数中都出现了mapreduceexamples.jar。但二者意义不同，-resources引用的是Map/Reduce函数，运行于分布式环境中；而-classpath引用的是Main函数，运行于本地，指定的JAR 包路径也是本地文件路径。
**-D <name>=<value>**：本地执行时，**<mainClass>**的Java属性，可以定义多个。

**命令示例**

```
jar -conf \home\admin\myconf -resources a.txt,example.jar -classpath ..\lib\example.jar:.\other_lib.jar -D java.library.path=.\native;
```

##### 7.1.3.4. 输入与输出

本文详细说明了MaxCompute MapReduce在输入和输出方面的特性和限制，包括支持的数据类型、多表输入的支持、以及多路输出的实现方式。这些特性使得用户能够灵活地处理和存储数据，满足不同的业务需求。

#### 使用说明

MaxCompute MapReduce的输入与输出，支持MaxCompute内置类型的BIGINT、DOUBLE、STRING、DATETIME、BOOLEAN类型，不支持您自定义类型。 接受多表输入，且输入表的Schema可以不同。在Map函数中，您可以获取当前Record对应的Table信息。 输入可以为空，不支持视图（View）作为输入。 Reduce接受多路输出，可以输出到不同表或同一张表的不同分区。不同输出的Schema可以不同。不同输出将通过Label进行区分，默认输出不必加Label，但目前不接受没有输出的情况。

**说明**

##### 7.1.3.5. 资源使用

本文详细介绍了如何在MaxCompute MapReduce任务中使用资源。通过将资源加载到内存中，您可以方便地在Map或Reduce阶段访问这些资源，从而实现更复杂的数据处理逻辑。

#### 使用说明

允许您在Map/Reduce中读取MaxCompute资源。Map/Reduce的任意Worker都会将资源加载到内存中，以供您的代码使用。

**说明**

##### 7.1.3.6. 本地运行

MaxCompute MapReduce支持本地调试功能，本文详细介绍了MaxCompute MapReduce在本地和分布式环境中运行的差异，并提供了详细的本地运行示例。

**各阶段介绍**

本地运行前：通过在JAR命令中设置 `-local` 参数，在本地模拟MapReduce的运行过程，从而进行本地调试。 本地运行时：客户端会从MaxCompute中下载本地调试所需要的输入表的元信息和数据、所需要的资源以及输出表的元信息，并将这些信息保存到一个名为warehouse的本地目录中。 本地运行结束后：程序运行结束后，会将计算结果输出到warehouse目录内的一个文件中。如果本地的warehouse目录下已经下载了输入表及被引用的资源，在下一次运行时，会直接引用warehouse下的数据及文件，无需重复下载。

**本地运行和分布式环境运行差异**

在本地运行过程中，仍然会启动多个Map及Reduce进程处理数据，但这些进程不是并发运行，而是依次串行运行。此外这个模拟运行过程与真正的分布式运行有如下差别：
**输入表行数限制**：最多只支持下载100行数据。
**资源的使用**：在分布式环境中，MaxCompute会限制引用资源的大小。但在本地运行环境中，不会有资源大小的限制。
**安全限制**：MaxCompute MapReduce及UDF程序在分布式环境中运行时受到Java沙箱的限制。但在本地运行时，没有此限制。

**本地运行示例**

本地运行的示例如下。

```
    odps:my_project> jar -l com.aliyun.odps.mapred.example.WordCount wc_in wc_out
    Summary:
    counters: 10
                combine_input_groups=2
                combine_output_records=2
                map_input_bytes=4
                map_input_records=1
                map_output_records=2
                map_output_[wc_out]_bytes=0
                map_output_[wc_out]_records=0
                reduce_input_groups=2
                reduce_output_[wc_out]_bytes=8
                reduce_output_[wc_out]_records=2
```

`OK`

**说明**

如果您是第一次运行本地调试命令，命令成功运行后，会在当前路径下看到一个名为warehouse的目录。warehouse的目录结构如下所示。

```xml
<warehouse>
```

|____my_project（项目空间目录）

```
          |____ <__tables__>
```

| |__wc_in（表数据目录）

```
          |       |      |____ data（文件）
          |       |      |
          |       |      |____ <__schema__>（文件）
```

| |__wc_out（表数据目录）

```
          |               |____ data（文件）
          |               |
          |               |____ <__schema__>（文件）
```

|

```
          |____ <__resources__>
```

|
|___table_resource_name（表资源）

```
                  |         |____<__ref__>
```

|
|___ file_resource_name（文件资源）
my_project的同级目录表示项目空间。wc_in及wc_out表示数据表，您在JAR命令中读写的表文件数据会被下载到这一级的目录下。 Schema文件中的内容表示表的元信息，其文件格式定义如下。

```
  project=local_project_name
  table=local_table_name
  columns=col1_name:col1_type,col2_name:col2_type
```

`partitions=p1:STRING,p2:BIGINT --`本示例中不需要此字。

**说明**

其中，列名与列类型使用英文冒号分隔，列与列之间使用半角逗号（,）分隔。Schema文件的最前面需要声明Project名字及Table名字， 即**projectname.tablename**，并通过半角逗号（,）与列的定义做分隔即**project_name.table_name,col1_name:col1_type,col2_name:col2_type,……**。 tables目录中data文件表示表的数据。列的数量及数据必须与Schema文件的定义相符，不能多列或少列，列之间使用半角逗号（,）分隔。 wc_in的Schema文件内容示例如下。

```
my_project.wc_in,key:STRING,value:STRING
```

对应的data文件内容示例如下。

```
0,2
```

客户端会从MaxCompute中下载表的元信息及部分数据内容并保存到上述两个文件中。如果再次运行这个示例，将直接使用wc_in目录下的数据，不会再次下载。

**说明**

仅在MapReduce的本地运行模式下支持从MaxCompute中下载数据的功能。 wc_out的Schema文件内容示例如下。

```
my_project.wc_out,key:STRING,cnt:BIGINT
```

对应的data文件内容示例如下。

```
0,1 2,1
```

客户端会从MaxCompute中下载表的元信息，并保存到Schema文件中。而本地运行后，生成的结果数据，则保存到data文件中。

**说明**

您也可以自行编辑_schema_及data文件，而后将这两个文件放置在对应的表目录下。 在本地运行时，客户端检测到表目录已经存在，则不会从MaxCompute中下载这个表的信息。本地的表目录可以是MaxCompute中不存在的表。

#### 7.1.4. SDK介绍

##### 7.1.4.1. 核心接口概述

本文介绍了MaxCompute MapReduce的核心接口（如MapperBase、ReducerBase、JobConf等）及其功能，并提供了通过Maven引入odps-sdk-mapred SDK 如果您使用Maven，可以从Maven库获取。

```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>odps-sdk-mapred</artifactId>
    <version>0.36.2-public</version>
</dependency>
```

**接口说明**

| 主要接口 | 描述 |
|---|---|
| MapperBase | 用户自定义的Map函数需要继承自此类。处理输入表的记录对象，加工处理成键值对集合输出到Reduce阶段，或者不经过Reduce阶段直接输出结果记录到结果表。不经过Reduce阶段而直接输出计算结果的作业，也可称之为Map-Only作业。 |
| ReducerBase | 用户自定义的Reduce函数需要继承自此类。对与一个键（Key）关联的一组数值集（Values）进行归约计算。 |
| TaskContext | 是MapperBase及ReducerBase多个成员函数的输入参数之一，含有任务运行的上下文信息。 |
| JobClient | 用于提交和管理作业，提交方式包括阻塞（同步）方式及非阻塞（异步）方式。 |
| RunningJob | 作业运行时对象，用于跟踪运行中的MapReduce作业实例。 |
| JobConf | 描述一个MapReduce任务的配置，通常在主程序（Main函数）中定义JobConf对象，然后通过JobClient提交作业给MaxCompute服务。 |

##### 7.1.4.2. 具体接口描述

###### 7.1.4.2.1. MapperBase

**主要函数接口**

| 主要接口 | 描述 |
|---|---|
| void cleanup(TaskContext context) | 在Map阶段结束时，Map方法之后调用。 |
| void map(long key, Record record, TaskContext context) | Map方法，处理输入表的记录。 |
| void setup(TaskContext context) | 在Map阶段开始时，Map方法之前调用。 |

###### 7.1.4.2.2. ReducerBase

**主要函数接口**

| 主要接口 | 描述 |
|---|---|
| void cleanup(TaskContext context) | 在Reduce阶段结束时，Reduce方法之后调用。 |
| void reduce(Record key, Iterator<Record> values, TaskContext context) | Reduce方法，处理输入表的记录。 |

| void setup(TaskContext context) | 在Reduce阶段开始时，Reduce方法之前调用。 |
|---|---|

###### 7.1.4.2.3. TaskContext

**主要函数接口**

| 主要接口 | 描述 |
|---|---|
| TableInfo[] getOutputTableInfo() | 获取输出的表信息。 |
| Record createOutputRecord() | 创建默认输出表的记录对象。 |
| Record createOutputRecord(String label) | 创建给定Label输出表的记录对象。 |
| Record createMapOutputKeyRecord() | 创建Map输出Key的记录对象。 |
| Record createMapOutputValueRecord() | 创建Map输出Value的记录对象。 |
| void write(Record record) | 写记录到默认输出，用于Reduce端写出数据，可以在Reduce端多次调用。 |
| void write(Record record, String label) | 写记录到给定标签输出，用于Reduce端写出数据 ，可以在Reduce端多次调用。 |
| void write(Record key, Record value) | 写记录到中间结果，用于Map端写出数据，可以在Map端多次调用。 |
| BufferedInputStream readResourceFileAsStream(String resourceName) | 读取文件类型资源。 |
| Iterator<Record> readResourceTable(String resourceName) | 读取表类型资源。 |
| Counter getCounter(Enum<?> name) | 获取给定名称的Counter对象。 |
| Counter getCounter(String group, String name) | 获取给定组名和名称的Counter对象。 |
| void progress() | 向MapReduce框架报告心跳信息。如果用户方法处理时间很长，且中间没有调用框架，可以调用这个方法避免Task超时，框架默认600s超时。 |

**说明**

TaskContext接口中提供了Progress功能，但此功能是为防止Worker长时间运行未结束，被框架误认为超时而被强制停止的情况出现。这个接口更类似于向框架发送心跳信息，并不是用来汇报Worker进度。 MaxCompute MapReduce默认Worker超时时间为10分钟（系统默认配置，不受用户控制），如果超过10分钟，Worker仍然没有向框架发送心跳（调用Progress接口），框架会强制停止该Worker，MapReduce任务失败退出。因此，建议您在Mapper/Reducer函数中，定期调用Progress接口，防止框架认为Worker超时，误杀任务。

###### 7.1.4.2.4. JobConf

**主要函数接口**

| 主要接口 | 描述 |
|---|---|
| void setResources(String resourceNames) | 声明本作业使用的资源。只有声明的资源才能在运行Mapper/Reducer时通过 TaskContext对象读取。 |
| void setMapOutputKeySchema(Column[] schema) | 设置Mapper输出到Reducer的Key属性。 |
| void setMapOutputValueSchema(Column[] schema) | 设置Mapper输出到Reducer的Value属性。 |
| void setOutputKeySortColumns(String[] cols) | 设置Mapper输出到Reducer的Key排序列。 |
| void setOutputGroupingColumns(String[] cols) | 设置Key分组列。 |

| void setMapperClass(Class<? extends Mapper> theClass) | 设置作业的Mapper函数。 |
|---|---|
| void setPartitionColumns(String[] cols) | 设置作业指定的分区列，默认是Mapper输出Key的所有列。 |
| void setReducerClass(Class<? extends Reducer> theClass) | 设置作业的Reducer。 |
| void setCombinerClass(Class<? extends Reducer> theClass) | 设置作业的Combiner。在Map端运行，作用类似于单个Map对本地的相同Key值做 Reduce。 |
| void setSplitSize(long size) | 设置输入分片大小，单位MB，默认值为256 MB。 |
| void setNumReduceTasks(int n) | 设置Reducer任务数，默认为Mapper任务数的1/4。 |
| void setMemoryForMapTask(int mem) | 设置Mapper任务中单个Worker的内存大小，单位MB，默认值为2048 MB。 |
| void setMemoryForReduceTask(int mem) | 设置Reducer任务中单个Worker的内存大小，单位MB，默认值为2048 MB。 |
| void setOutputSchema(Column[] schema, String label) | 设置指定Label的输出属性。多路输出时，每一路输出对应一个Label。 |

**说明**

通常情况下，GroupingColumns包含在KeySortColumns中，KeySortColumns和PartitionColumns需包含在Key中。 在Map端，Mapper输出的Record会根据设置的PartitionColumns计算哈希值，决定分配到哪个Reducer，会根据KeySortColumns对Record进行排序。 在Reduce端，输入Records，再按照KeySortColumns排序后，会根据GroupingColumns指定的列对输入的Records进行分组，即会顺序遍历输入的 Records，把GroupingColumns所指定列相同的Records作为一次Reduce函数调用的输入。

###### 7.1.4.2.5. JobClient

**主要函数接口**

| 主要接口 | 描述 |
|---|---|
| static RunningJob runJob(JobConf job) | 阻塞（同步）方式提交MapReduce作业后立即返回。 |
| static RunningJob submitJob(JobConf job) | 非阻塞（异步）方式提交MapReduce作业后立即返回。 |

###### 7.1.4.2.6. RunningJob

**主要函数接口**

| 主要接口 | 描述 |
|---|---|
| String getInstanceID() | 获取作业运行实例ID，用于查看运行日志和作业管理。 |
| boolean isComplete() | 查询作业是否结束。 |
| boolean isSuccessful() | 查询作业实例是否运行成功。 |
| void waitForCompletion() | 等待直至作业实例结束。通常用于异步方式提交的作业。 |
| JobStatus getJobStatus() | 查询作业实例运行状态。 |
| void killJob() | 结束此作业。 |
| Counters getCounters() | 获取Conter信息。 |

###### 7.1.4.2.7. InputUtils

**主要函数接口**

| 主要接口 | 描述 |
|---|---|
| static void addTable(TableInfo table, JobConf conf) | 添加表Table到任务输入，可以被调用多次，新加入的表以Append方式添加到输入队列中。 |
| static void setTables(TableInfo [] tables, JobConf conf) | 添加多张表到任务输入中。 |

###### 7.1.4.2.8. OutputUtils

**主要函数接口**

| 主要接口 | 描述 |
|---|---|
| static void addTable(TableInfo table, JobConf conf) | 添加表Table到任务输出，可以被调用多次，新加入的表以Append方式添加到输出队列中。 |
| static void setTables(TableInfo[] tables, JobConf conf) | 添加多张表到任务输出中。 |

###### 7.1.4.2.9. Pipeline

**主要接口**

Pipeline是MR2的主体类。可以通过Pipeline.builder构建一个Pipeline。Pipeline的主要接口如下。

```
public Builder addMapper(Class<? extends Mapper> mapper); public Builder addMapper(Class<? extends Mapper> mapper,Column[] keySchema, Column[] valueSchema, String[] sortCols,SortOrder[] order, St ring[] partCols,Class<? extends Partitioner> theClass, String[] groupCols); public Builder addReducer(Class<? extends Reducer> reducer); public Builder addReducer(Class<? extends Reducer> reducer,Column[] keySchema, Column[] valueSchema, String[] sortCols,SortOrder[] order, String[] partCols,Class<? extends Partitioner> theClass, String[] groupCols); public Builder setOutputKeySchema(Column[] keySchema); public Builder setOutputValueSchema(Column[] valueSchema); public Builder setOutputKeySortColumns(String[] sortCols); public Builder setOutputKeySortOrder(SortOrder[] order); public Builder setPartitionColumns(String[] partCols); public Builder setPartitionerClass(Class<? extends Partitioner> theClass); public Builder setOutputGroupingColumns(String[] cols);
```

**示例代码**

```
    Job job = new Job();
     .addMapper(TokenizerMapper.class)
     .setOutputKeySchema(
         new Column[] { new Column("word", OdpsType.STRING) })
     .setOutputValueSchema(
         new Column[] { new Column("count", OdpsType.BIGINT) })
     .addReducer(SumReducer.class)
     .setOutputKeySchema(
         new Column[] { new Column("count", OdpsType.BIGINT) })
     .setOutputValueSchema(
         new Column[] { new Column("word", OdpsType.STRING),
         new Column("count", OdpsType.BIGINT) })
     .addReducer(IdentityReducer.class).createPipeline();
    job.setPipeline(pipeline);
    job.addInput(...);
    job.addOutput(...);
    job.submit();
```

如上所示，您可以在Main函数中构建一个Map之后，连续接两个Reduce的MapReduce任务。如果您比较熟悉MapReduce的基础功能，即可轻松使用MR2。

**说明**

##### 7.1.4.3. 兼容版本SDK概述

本文为您介绍MaxCompute兼容版本MapReduce与Hadoop MapReduce的兼容情况。 MaxCompute兼容版本的MapReduce与Hadoop MapReduce兼容性的详细列表，如下表所示。

| 类型 | 接口 | 是否兼容 |
|---|---|---|
| Mapper | void map(KEYIN key, VALUEIN value, org.apache.hadoop.mapreduce.Mapper.Context context) | 是 |
|  | void run(org.apache.hadoop.mapreduce.Mapper.Context context) | 是 |
|  | void setup(org.apache.hadoop.mapreduce.Mapper.Cont ext context) | 是 |
| Reducer | void cleanup(org.apache.hadoop.mapreduce.Reducer.C ontext context) | 是 |
|  | void reduce(KEYIN key, VALUEIN value, org.apache.hadoop.mapreduce.Reducer.Context context) | 是 |
|  | void run(org.apache.hadoop.mapreduce.Reducer.Contex t context) | 是 |
|  | void setup(org.apache.hadoop.mapreduce.Reducer.Cont ext context) | 是 |
| Partitioner | int getPartition(KEY key, VALUE value, int numPartitions) | 是 |
| MapContext（继承TaskInputOutputContext） | InputSplit getInputSplit() | 否，报异常 |
| ReduceContext | nextKey() | 是 |
|  | getValues() | 是 |
| TaskInputOutputContext | getCurrentKey() | 是 |
|  | getCurrentValue() | 是 |
|  | getOutputCommitter() | 否，报异常 |
|  | nextKeyValue() | 是 |
|  | write(KEYOUT key, VALUEOUT value) | 是 |
|  | getCounter(Enum<?> counterName) | 是 |
|  | getCounter(String groupName, String counterName) | 是 |
|  | setStatus(String msg) | 空实现 |

| 用户指南·多引擎支持 |  |  |
|---|---|---|
| TaskAttemptContext |  |  |
|  | getStatus() | 空实现 |
|  | getTaskAttemptID() | 否，报异常 |
|  | getProgress() | 否，报异常 |
|  | progress() | 是 |
|  | addArchiveToClassPath(Path archive) | 否 |
|  | addCacheArchive(URI uri) | 否 |
|  | addCacheFile(URI uri) | 否 |
|  | addFileToClassPath(Path file) | 否 |
|  | cleanupProgress() | 否 |
|  | createSymlink() | 否，报异常 |
|  | failTask(TaskAttemptID taskId) | 否 |
|  | getCompletionPollInterval(Configuration conf) | 空实现 |
|  | getCounters() | 是 |
|  | getFinishTime() | 是 |
|  | getHistoryUrl() | 是 |
|  | getInstance() | 是 |
|  | getInstance(Cluster ignored) | 是 |
|  | getInstance(Cluster ignored, Configuration conf) | 是 |
|  | getInstance(Configuration conf) | 是 |
|  | getInstance(Configuration conf, String jobName) | 空实现 |
|  | getInstance(JobStatus status, Configuration conf) | 否，报异常 |
|  | getJobFile() | 否，报异常 |
|  | getJobName() | 空实现 |
|  | getJobState() | 否，报异常 |
|  | getPriority() | 否，报异常 |
|  | getProgressPollInterval(Configuration conf) | 空实现 |
|  | getReservationId() | 否，报异常 |
|  | getSchedulingInfo() | 否，报异常 |
|  | getStartTime() | 是 |
|  | getStatus() | 否，报异常 |

| Job |  |  |
|---|---|---|
|  | getTaskCompletionEvents(int startFrom) | 否，报异常 |
|  | getTaskCompletionEvents(int startFrom, int numEvents) | 否，报异常 |
|  | getTaskDiagnostics(TaskAttemptID taskid) | 否，报异常 |
|  | getTaskOutputFilter(Configuration conf) | 否，报异常 |
|  | getTaskReports(TaskType type) | 否，报异常 |
|  | getTrackingURL() | 是 |
|  | isComplete() | 是 |
|  | isRetired() | 否，报异常 |
|  | isSuccessful() | 是 |
|  | isUber() | 空实现 |
|  | killJob() | 是 |
|  | killTask(TaskAttemptID taskId) | 否 |
|  | mapProgress() | 是 |
|  | monitorAndPrintJob() | 是 |
|  | reduceProgress() | 是 |
|  | setCacheArchives(URI[] archives) | 否，报异常 |
|  | setCacheFiles(URI[] files) | 否，报异常 |
|  | setCancelDelegationTokenUponJobCompletion(bool ean value) | 否，报异常 |
|  | setCombinerClass(Class<? extends Reducer> cls) | 是 |
|  | setCombinerKeyGroupingComparatorClass(Class<? extends RawComparator> cls) | 是 |
|  | setGroupingComparatorClass(Class<? extends RawComparator> cls) | 是 |
|  | setInputFormatClass(Class<? extends InputFormat> cls) | 空实现 |
|  | setJar(String jar) | 是 |
|  | setJarByClass(Class<?> cls) | 是 |
|  | setJobName(String name) | 空实现 |
|  | setJobSetupCleanupNeeded(boolean needed) | 空实现 |
|  | setMapOutputKeyClass(Class<?> theClass) | 是 |
|  | setMapOutputValueClass(Class<?> theClass) | 是 |

|  | setMapperClass(Class<? extends Mapper> cls) | 是 |
|---|---|---|
|  | setMapSpeculativeExecution(boolean speculativeExecution) | 空实现 |
|  | setMaxMapAttempts(int n) | 空实现 |
|  | setMaxReduceAttempts(int n) | 空实现 |
|  | setNumReduceTasks(int tasks) | 是 |
|  | setOutputFormatClass(Class<? extends OutputFormat> cls) | 否，报异常 |
|  | setOutputKeyClass(Class<?> theClass) | 是 |
|  | setOutputValueClass(Class<?> theClass) | 是 |
|  | setPartitionerClass(Class<? extends Partitioner> cls) | 是 |
|  | setPriority(JobPriority priority) | 否，报异常 |
|  | setProfileEnabled(boolean newValue) | 空实现 |
|  | setProfileParams(String value) | 空实现 |
|  | setProfileTaskRange(boolean isMap, String newValue) | 空实现 |
|  | setReducerClass(Class<? extends Reducer> cls) | 是 |
|  | setReduceSpeculativeExecution(boolean speculativeExecution) | 空实现 |
|  | setReservationId(ReservationId reservationId) | 否，报异常 |
|  | setSortComparatorClass(Class<? extends RawComparator> cls) | 否，报异常 |
|  | setSpeculativeExecution(boolean speculativeExecution) | 是 |
|  | setTaskOutputFilter(Configuration conf, org.apache.hadoop.mapreduce.Job.TaskStatusFilter newValue) | 否，报异常 |
|  | setupProgress() | 否，报异常 |
|  | setUser(String user) | 空实现 |
|  | setWorkingDirectory(Path dir) | 空实现 |
|  | submit() | 是 |
|  | toString() | 否，报异常 |
|  | waitForCompletion(boolean verbose) | 是 |
|  | mapreduce.map.java.opts | 空实现 |
|  | mapreduce.reduce.java.opts | 空实现 |

| 大数据计算服务 | 用户指南·多引擎支持 |  |
|---|---|---|
| Task Execution & Environment |  |  |
|  | mapreduce.map.memory.mb | 空实现 |
|  | mapreduce.reduce.memory.mb | 空实现 |
|  | mapreduce.task.io.sort.mb | 空实现 |
|  | mapreduce.map.sort.spill.percent | 空实现 |
|  | mapreduce.task.io.soft.factor | 空实现 |
|  | mapreduce.reduce.merge.inmem.thresholds | 空实现 |
|  | mapreduce.reduce.shuffle.merge.percent | 空实现 |
|  | mapreduce.reduce.shuffle.input.buffer.percent | 空实现 |
|  | mapreduce.reduce.input.buffer.percent | 空实现 |
|  | mapreduce.job.id | 空实现 |
|  | mapreduce.job.jar | 空实现 |
|  | mapreduce.job.local.dir | 空实现 |
|  | mapreduce.task.id | 空实现 |
|  | mapreduce.task.attempt.id | 空实现 |
|  | mapreduce.task.is.map | 空实现 |
|  | mapreduce.task.partition | 空实现 |
|  | mapreduce.map.input.file | 空实现 |
|  | mapreduce.map.input.start | 空实现 |
|  | mapreduce.map.input.length | 空实现 |
|  | mapreduce.task.output.dir | 空实现 |
|  | cancelDelegationToken(Token <DelegationTokenIdentifier> token) | 否，报异常 |
|  | close() | 空实现 |
|  | displayTasks(JobID jobId, String type, String state) | 否，报异常 |
|  | getAllJobs() | 否，报异常 |
|  | getCleanupTaskReports(JobID jobId) | 否，报异常 |
|  | getClusterStatus() | 否，报异常 |
|  | getClusterStatus(boolean detailed) | 否，报异常 |
|  | getDefaultMaps() | 否，报异常 |
|  | getDefaultReduces() | 否，报异常 |

|  | getDelegationToken(Text renewer) | 否，报异常 |
|---|---|---|
|  | getFs() | 否，报异常 |
|  | getJob(JobID jobid) | 否，报异常 |
|  | getJob(String jobid) | 否，报异常 |
| JobClient |  |  |
|  | getJobsFromQueue(String queueName) | 否，报异常 |
|  | getMapTaskReports(JobID jobId) | 否，报异常 |
|  | getMapTaskReports(String jobId) | 否，报异常 |
|  | getQueueAclsForCurrentUser() | 否，报异常 |
|  | getQueueInfo(String queueName) | 否，报异常 |
|  | getQueues() | 否，报异常 |
|  | getReduceTaskReports(JobID jobId) | 否，报异常 |
|  | getReduceTaskReports(String jobId) | 否，报异常 |
|  | getSetupTaskReports(JobID jobId) | 否，报异常 |
|  | getStagingAreaDir() | 否，报异常 |
|  | getSystemDir() | 否，报异常 |
|  | getTaskOutputFilter() | 否，报异常 |
|  | getTaskOutputFilter(JobConf job) | 否，报异常 |
|  | init(JobConf conf) | 否，报异常 |
|  | isJobDirValid(Path jobDirPath, FileSystem fs) | 否，报异常 |
|  | jobsToComplete() | 否，报异常 |
|  | monitorAndPrintJob(JobConf conf, RunningJob job) | 否，报异常 |
|  | renewDelegationToken(Token<DelegationTokenIde ntifier> token) | 否，报异常 |
|  | run(String[] argv) | 否，报异常 |
|  | runJob(JobConf job) | 是 |
|  | setTaskOutputFilter(JobClient.TaskStatusFilter newValue) | 否，报异常 |
|  | setTaskOutputFilter(JobConf job, JobClient.TaskStatusFilter newValue) | 否，报异常 |
|  | submitJob(JobConf job) | 是 |
|  | submitJob(String jobFile) | 否，报异常 |
|  | deleteLocalFiles() | 否，报异常 |

| 大数据计算服务 | 用户指南·多引擎支持 |  |
|---|---|---|
| JobConf |  |  |
|  | deleteLocalFiles(String subdir) | 否，报异常 |
|  | normalizeMemoryConfigValue(long val) | 空实现 |
|  | setCombinerClass(Class<? extends Reducer> theClass) | 是 |
|  | setCompressMapOutput(boolean compress) | 空实现 |
|  | setInputFormat(Class<? extends InputFormat> theClass) | 否，报异常 |
|  | setJar(String jar) | 否，报异常 |
|  | setJarByClass(Class cls) | 否，报异常 |
|  | setJobEndNotificationURI(String uri) | 否，报异常 |
|  | setJobName(String name) | 空实现 |
|  | setJobPriority(JobPriority prio) | 否，报异常 |
|  | setKeepFailedTaskFiles(boolean keep) | 否，报异常 |
|  | setKeepTaskFilesPattern(String pattern) | 否，报异常 |
|  | setKeyFieldComparatorOptions(String keySpec) | 否，报异常 |
|  | setKeyFieldPartitionerOptions(String keySpec) | 否，报异常 |
|  | setMapDebugScript(String mDbgScript) | 空实现 |
|  | setMapOutputCompressorClass(Class<? extends CompressionCodec> codecClass) | 空实现 |
|  | setMapOutputKeyClass(Class<?> theClass) | 是 |
|  | setMapOutputValueClass(Class<?> theClass) | 是 |
|  | setMapperClass(Class<? extends Mapper> theClass) | 是 |
|  | setMapRunnerClass(Class<? extends MapRunnable> theClass) | 否，报异常 |
|  | setMapSpeculativeExecution(boolean speculativeExecution) | 空实现 |
|  | setMaxMapAttempts(int n) | 空实现 |
|  | setMaxMapTaskFailuresPercent(int percent) | 空实现 |
|  | setMaxPhysicalMemoryForTask(long mem) | 空实现 |
|  | setMaxReduceAttempts(int n) | 空实现 |
|  | setMaxReduceTaskFailuresPercent(int percent) | 空实现 |
|  | setMaxTaskFailuresPerTracker(int noFailures) | 空实现 |
|  | setMaxVirtualMemoryForTask(long vmem) | 空实现 |

|  | setMemoryForMapTask(long mem) | 是 |
|---|---|---|
|  | setMemoryForReduceTask(long mem) | 是 |
|  | setNumMapTasks(int n) | 是 |
|  | setNumReduceTasks(int n) | 是 |
|  | setNumTasksToExecutePerJvm(int numTasks) | 空实现 |
|  | setOutputCommitter(Class<? extends OutputCommitter> theClass) | 否，报异常 |
|  | setOutputFormat(Class<? extends OutputFormat> theClass) | 空实现 |
|  | setOutputKeyClass(Class<?> theClass) | 是 |
|  | setOutputKeyComparatorClass(Class<? extends RawComparator> theClass) | 否，报异常 |
|  | setOutputValueClass(Class<?> theClass) | 是 |
|  | setOutputValueGroupingComparator(Class<? extends RawComparator> theClass) | 否，报异常 |
|  | setPartitionerClass(Class<? extends Partitioner> theClass) | 是 |
|  | setProfileEnabled(boolean newValue) | 空实现 |
|  | setProfileParams(String value) | 空实现 |
|  | setProfileTaskRange(boolean isMap, String newValue) | 空实现 |
|  | setQueueName(String queueName) | 否，报异常 |
|  | setReduceDebugScript(String rDbgScript) | 空实现 |
|  | setReducerClass(Class<? extends Reducer> theClass) | 是 |
|  | setReduceSpeculativeExecution(boolean speculativeExecution) | 空实现 |
|  | setSessionId(String sessionId) | 空实现 |
|  | setSpeculativeExecution(boolean speculativeExecution) | 否，报异常 |
|  | setUseNewMapper(boolean flag) | 是 |
|  | setUseNewReducer(boolean flag) | 是 |
|  | setUser(String user) | 空实现 |
|  | setWorkingDirectory(Path dir) | 空实现 |
| FileInputFormat | 不涉及 | 否，报异常 |
| TextInputFormat | 不涉及 | 是 |

| InputSplit | mapred.min.split.size | 否，报异常 |
|---|---|---|
| FileSplit | map.input.file | 否，报异常 |
| RecordWriter | 不涉及 | 否，报异常 |
| RecordReader | 不涉及 | 否，报异常 |
| OutputFormat | 不涉及 | 否，报异常 |
| OutputCommitter | abortJob(JobContext jobContext, int status) | 否，报异常 |
|  | abortJob(JobContext context, JobStatus.State runState) | 否，报异常 |
|  | abortTask(TaskAttemptContext taskContext) | 否，报异常 |
|  | abortTask(TaskAttemptContext taskContext) | 否，报异常 |
|  | cleanupJob(JobContext jobContext) | 否，报异常 |
|  | cleanupJob(JobContext context) | 否，报异常 |
|  | commitJob(JobContext jobContext) | 否，报异常 |
|  | commitJob(JobContext context) | 否，报异常 |
|  | commitTask(TaskAttemptContext taskContext) | 否，报异常 |
|  | needsTaskCommit(TaskAttemptContext taskContext) | 否，报异常 |
|  | needsTaskCommit(TaskAttemptContext taskContext) | 否，报异常 |
|  | setupJob(JobContext jobContext) | 否，报异常 |
|  | setupJob(JobContext jobContext) | 否，报异常 |
|  | setupTask(TaskAttemptContext taskContext) | 否，报异常 |
|  | setupTask(TaskAttemptContext taskContext) | 否，报异常 |
| Counter | getDisplayName() | 是 |
|  | getName() | 是 |
|  | getValue() | 是 |
|  | increment(long incr) | 是 |
|  | setValue(long value) | 是 |
|  | setDisplayName(String displayName) | 是 |
|  | CACHEARCHIVES _ | 否，报异常 |
|  | CACHEARCHIVESSIZES _ _ | 否，报异常 |
|  | CACHEARCHIVESTIMESTAMPS _ _ | 否，报异常 |

| 用户指南·多引擎支持 | 大数据计算服务 |  |
|---|---|---|
| DistributedCache |  |  |
|  | CACHEFILES _ | 否，报异常 |
|  | CACHEFILESSIZES _ _ | 否，报异常 |
|  | CACHEFILESTIMESTAMPS _ _ | 否，报异常 |
|  | CACHELOCALARCHIVES _ | 否，报异常 |
|  | CACHELOCALFILES _ | 否，报异常 |
|  | CACHESYMLINK _ | 否，报异常 |
|  | addArchiveToClassPath(Path archive, Configuration conf) | 否，报异常 |
|  | addArchiveToClassPath(Path archive, Configuration conf, FileSystem fs) | 否，报异常 |
|  | addCacheArchive(URI uri, Configuration conf) | 否，报异常 |
|  | addCacheFile(URI uri, Configuration conf) | 否，报异常 |
|  | addFileToClassPath(Path file, Configuration conf) | 否，报异常 |
|  | addFileToClassPath(Path file, Configuration conf, FileSystem fs) | 否，报异常 |
|  | addLocalArchives(Configuration conf, String str) | 否，报异常 |
|  | addLocalFiles(Configuration conf, String str) | 否，报异常 |
|  | checkURIs(URI[] uriFiles, URI[] uriArchives) | 否，报异常 |
|  | createAllSymlink(Configuration conf, File jobCacheDir, File workDir) | 否，报异常 |
|  | createSymlink(Configuration conf) | 否，报异常 |
|  | getArchiveClassPaths(Configuration conf) | 否，报异常 |
|  | getArchiveTimestamps(Configuration conf) | 否，报异常 |
|  | getCacheArchives(Configuration conf) | 否，报异常 |
|  | getCacheFiles(Configuration conf) | 否，报异常 |
|  | getFileClassPaths(Configuration conf) | 否，报异常 |
|  | getFileStatus(Configuration conf, URI cache) | 否，报异常 |
|  | getFileTimestamps(Configuration conf) | 否，报异常 |
|  | getLocalCacheArchives(Configuration conf) | 否，报异常 |
|  | getLocalCacheFiles(Configuration conf) | 否，报异常 |
|  | getSymlink(Configuration conf) | 否，报异常 |
|  | getTimestamp(Configuration conf, URI cache) | 否，报异常 |

|  | setArchiveTimestamps(Configuration conf, String timestamps) | 否，报异常 |
|---|---|---|
|  | setCacheArchives(URI[] archives, Configuration conf) | 否，报异常 |
|  | setCacheFiles(URI[] files, Configuration conf) | 否，报异常 |
|  | setFileTimestamps(Configuration conf, String timestamps) | 否，报异常 |
|  | setLocalArchives(Configuration conf, String str) | 否，报异常 |
|  | setLocalFiles(Configuration conf, String str) | 否，报异常 |
| IsolationRunner | 不涉及 | 否，报异常 |
| Profiling | 不涉及 | 空实现 |
| Debugging | 不涉及 | 空实现 |
| Data Compression | 不涉及 | 是 |
| Skipping Bad Records | 不涉及 | 否，报异常 |
| Job Authorization | mapred.acls.enabled | 否，报异常 |
|  | mapreduce.job.acl-view-job | 否，报异常 |
|  | mapreduce.job.acl-modify-job | 否，报异常 |
|  | mapreduce.cluster.administrators | 否，报异常 |
|  | mapred.queue.queue-name.acl-administer-jobs | 否，报异常 |
| MultipleInputs | 不涉及 | 否，报异常 |
| MultipleOutputs | 不涉及 | 是 |
| org.apache.hadoop.mapreduce.lib.db | 不涉及 | 否，报异常 |
| org.apache.hadoop.mapreduce.security | 不涉及 | 否，报异常 |
| org.apache.hadoop.mapreduce.lib.jobcontrol | 不涉及 | 否，报异常 |
| org.apache.hadoop.mapreduce.lib.chain | 不涉及 | 否，报异常 |

#### 7.1.5. 数据类型

本文为您提供了MaxCompute MapReduce支持的数据类型清单及SQL与Java类型的完整映射对照，方便您在编写代码时快速进行类型转换，避免类型不匹配错误。

**数据类型对照关系**

MapReduce支持的数据类型有：BIGINT、DOUBLE、STRING、DATETIME、BOOLEAN、DECIMAL类型。MaxCompute数据类型与Java类型的对应关系如下。

| MaxCompute SQL Type | Java Type |
|---|---|
| BIGINT | LONG |
| DOUBLE | DOUBLE |
| DECIMAL | BIGDECIMAL |

| BOOLEAN | BOOLEAN |
|---|---|
| STRING | STRING |
| DATETIME | DATE |

#### 7.1.6. 示例程序

##### 7.1.6.1. WordCount示例

本文为您提供MaxCompute MapReduce的经典WordCount示例。该示例完整展示了如何编写Mapper、Combiner和Reducer类，并演示了如何通过JobConf配置输入输出表及中间结果的Schema，帮助您快速掌握MaxCompute MapReduce程序的开发流程。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Iterator; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.ReducerBase; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; public class WordCount {
    public static class TokenizerMapper extends MapperBase {
        private Record word;
        private Record one;
        @Override
            public void setup(TaskContext context) throws IOException {
            word = context.createMapOutputKeyRecord();
            one = context.createMapOutputValueRecord();
            one.set(new Object[] { 1L });
            System.out.println("TaskID:" + context.getTaskID().toString());
        }
        @Override
            public void map(long recordNum, Record record, TaskContext context)
            throws IOException {
            for (int i = 0; i < record.getColumnCount(); i++) {
                word.set(new Object[] { record.get(i).toString() });
                context.write(word, one);
            }
        }
    }
    /**
       * A combiner class that combines map output by sum them.
       **/
    public static class SumCombiner extends ReducerBase {
        private Record count;
        @Override
            public void setup(TaskContext context) throws IOException {
            count = context.createMapOutputValueRecord();
        }
```

`//Combiner`实现的接口和`Reducer`一样，是可以立即在`Mapper`本地执行的一个`Reduce`，作用是减少`Mapper`的输出量。

```java
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
            throws IOException {
            long c = 0;
            while (values.hasNext()) {
                Record val = values.next();
                c += (Long) val.get(0);
            }
            count.set(0, c);
            context.write(key, count);
        }
    }
    /**
       * A reducer class that just emits the sum of the input values.
       **/
    public static class SumReducer extends ReducerBase {
        private Record result = null;
        @Override
            public void setup(TaskContext context) throws IOException {
            result = context.createOutputRecord();
        }
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
```

p `y,` ,

```java
            throws IOException {
            long count = 0;
            while (values.hasNext()) {
                Record val = values.next();
                count += (Long) val.get(0);
            }
            result.set(0, key.get(0));
            result.set(1, count);
            context.write(result);
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: WordCount <in_table> <out_table>");
            System.exit(2);
        }
        JobConf job = new JobConf();
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(SumCombiner.class);
        job.setReducerClass(SumReducer.class);
```

`//`设置`Mapper`中间结果的`key`和`value`的`Schema, Mapper`的中间结果输出也是`Record`的形式。

```
        job.setMapOutputKeySchema(SchemaUtils.fromString("word:string"));
        job.setMapOutputValueSchema(SchemaUtils.fromString("count:bigint"));
```

`//`设置输入和输出的表信息。

```
        InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), job);
        OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
        JobClient.runJob(job);
    }
}
```

##### 7.1.6.2. MapOnly示例

MaxCompute支持MapOnly作业，可在Map阶段直接将<Key, Value>数据写入目标表，无需经过Reduce阶段。本文将通过示例介绍如何在MaxCompute中实现 MapOnly作业。

#### 使用说明

对于MapOnly的作业，Map直接将<Key,Value>信息输出到MaxCompute的表中。您只需要指定输出表即可，不再需要指定Map输出的Key/Value元信息。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import com.aliyun.odps.data.Record; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.SchemaUtils; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.data.TableInfo; public class MapOnly {
    public static class MapperClass extends MapperBase {
        @Override
            public void setup(TaskContext context) throws IOException {
            boolean is = context.getJobConf().getBoolean("option.mapper.setup", false);
```

`//Main`函数在`jobconf`里设置了`option.mapper.setup`为`true`，才会执行下面的逻辑。

```java
            if (is) {
                Record result = context.createOutputRecord();
                result.set(0, "setup");
                result.set(1, 1L);
                context.write(result);
            }
        }
        @Override
            public void map(long key, Record record, TaskContext context) throws IOException {
            boolean is = context.getJobConf().getBoolean("option.mapper.map", false);
```

`//Main`函数在`jobconf`里设置了`option.mapper.map`为`true`，才会执行下面的逻辑。

```java
            if (is) {
                Record result = context.createOutputRecord();
                result.set(0, record.get(0));
                result.set(1, 1L);
                context.write(result);
            }
        }
        @Override
            public void cleanup(TaskContext context) throws IOException {
            boolean is = context.getJobConf().getBoolean("option.mapper.cleanup", false);
```

`//Main`函数在`jobconf`里设置了`option.mapper.cleanup`为`true`，才会执行下面的逻辑。

```
            if (is) {
                Record result = context.createOutputRecord();
                result.set(0, "cleanup");
                result.set(1, 1L);
                context.write(result);
            }
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 2 && args.length != 3) {
            System.err.println("Usage: OnlyMapper <in_table> <out_table> [setup|map|cleanup]");
            System.exit(2);
        }
        JobConf job = new JobConf();
        job.setMapperClass(MapperClass.class);
```

`//`对于`MapOnly`的作业，必须显式设置`reducer`的个数为0。

```
        job.setNumReduceTasks(0);
```

`//`设置输入输出的表信息。

```
        InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), job);
        OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
        if (args.length == 3) {
            String options = new String(args[2]);
```

`//jobconf`中可以设置自定义的`<key,value>`值，在`mapper`中通过`context`的`getJobConf`可以获取到相关的设置。

```
            if (options.contains("setup")) {
                job.setBoolean("option.mapper.setup", true);
            }
            if (options.contains("map")) {
                job.setBoolean("option.mapper.map", true);
            }
            if (options.contains("cleanup")) {
                job.setBoolean("option.mapper.cleanup", true);
            }
        }
        JobClient.runJob(job);
    }
}
```

##### 7.1.6.3. 多路输入输出示例

本文提供在MaxCompute中使用MapReduce实现多路输入与输出的代码示例，通过分词、聚合和分区等操作，完成复杂的数据处理任务。

#### 使用说明

MaxCompute支持多表的输入及输出。但在多表输入中，多张表的列数量及列类型必须相同，多表输出中列数量及列类型则可以不同。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Iterator; import java.util.LinkedHashMap; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.ReducerBase; import com.aliyun.odps.mapred.TaskContext; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; /**
     * Multi input & output example.
     **/
public class MultipleInOut {
    public static class TokenizerMapper extends MapperBase {
        Record word;
        Record one;
        @Override
            public void setup(TaskContext context) throws IOException {
            word = context.createMapOutputKeyRecord();
            one = context.createMapOutputValueRecord();
            one.set(new Object[] { 1L });
        }
        @Override
            public void map(long recordNum, Record record, TaskContext context)
            throws IOException {
            for (int i = 0; i < record.getColumnCount(); i++) {
                word.set(new Object[] { record.get(i).toString() });
                context.write(word, one);
            }
        }
    }
    public static class SumReducer extends ReducerBase {
        private Record result;
        private Record result1;
        private Record result2;
        @Override
            public void setup(TaskContext context) throws IOException {
```

`//`对于不同的输出需要创建不同的`Record`，通过`Label`来区分。

```java
            result = context.createOutputRecord();
            result1 = context.createOutputRecord("out1");
            result2 = context.createOutputRecord("out2");
        }
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
            throws IOException {
            long count = 0;
            while (values.hasNext()) {
                Record val = values.next();
                count += (Long) val.get(0);
            }
            long mod = count % 3;
            if (mod == 0) {
                result.set(0, key.get(0));
                result.set(1, count);
```

`//`不指定`Label`，默认`(default)`输出。

```java
                context.write(result);
            } else if (mod == 1) {
                result1.set(0, key.get(0));
                result1.set(1, count);
                context.write(result1, "out1");
            } else {
                result2.set(0, key.get(0));
                result2.set(1, count);
                context.write(result2, "out2");
            }
        }
        @Override
            public void cleanup(TaskContext context) throws IOException {
            Record result = context.createOutputRecord();
            result.set(0, "default");
            result.set(1, 1L);
            context.write(result);
            Record result1 = context.createOutputRecord("out1");
            result1.set(0, "out1");
            result1.set(1, 1L);
            context.write(result1, "out1");
Recordreslt2 contetcreateOtptRecord("ot2")
```

```
            Record result2 = context.createOutputRecord("out2");
            result2.set(0, "out2");
            result2.set(1, 1L);
            context.write(result2, "out2");
        }
    }
```

`//`将分区字符串如`"ds=1/pt=2"`转为`Map`的形式。

```
    public static LinkedHashMap<String, String> convertPartSpecToMap(
        String partSpec) {
        LinkedHashMap<String, String> map = new LinkedHashMap<String, String>();
        if (partSpec != null && !partSpec.trim().isEmpty()) {
            String[] parts = partSpec.split("/");
            for (String part : parts) {
                String[] ss = part.split("=");
                if (ss.length != 2) {
                    throw new RuntimeException("ODPS-0730001: error part spec format: "
                                               + partSpec);
                }
                map.put(ss[0], ss[1]);
            }
        }
        return map;
    }
    public static void main(String[] args) throws Exception {
        String[] inputs = null;
        String[] outputs = null;
        if (args.length == 2) {
            inputs = args[0].split(",");
            outputs = args[1].split(",");
        } else {
            System.err.println("MultipleInOut in... out...");
            System.exit(1);
        }
        JobConf job = new JobConf();
        job.setMapperClass(TokenizerMapper.class);
        job.setReducerClass(SumReducer.class);
        job.setMapOutputKeySchema(SchemaUtils.fromString("word:string"));
        job.setMapOutputValueSchema(SchemaUtils.fromString("count:bigint"));
```

`//`解析用户的输入表字符串。

```
        for (String in : inputs) {
            String[] ss = in.split("\\|");
            if (ss.length == 1) {
                InputUtils.addTable(TableInfo.builder().tableName(ss[0]).build(), job);
            } else if (ss.length == 2) {
                LinkedHashMap<String, String> map = convertPartSpecToMap(ss[1]);
                InputUtils.addTable(TableInfo.builder().tableName(ss[0]).partSpec(map).build(), job);
            } else {
                System.err.println("Style of input: " + in + " is not right");
                System.exit(1);
            }
        }
```

`//`解析用户的输出表字符串。

```
        for (String out : outputs) {
            String[] ss = out.split("\\|");
            if (ss.length == 1) {
                OutputUtils.addTable(TableInfo.builder().tableName(ss[0]).build(), job);
            } else if (ss.length == 2) {
                LinkedHashMap<String, String> map = convertPartSpecToMap(ss[1]);
                OutputUtils.addTable(TableInfo.builder().tableName(ss[0]).partSpec(map).build(), job);
            } else if (ss.length == 3) {
                if (ss[1].isEmpty()) {
                    LinkedHashMap<String, String> map = convertPartSpecToMap(ss[2]);
                    OutputUtils.addTable(TableInfo.builder().tableName(ss[0]).partSpec(map).build(), job);
                } else {
                    LinkedHashMap<String, String> map = convertPartSpecToMap(ss[1]);
                    OutputUtils.addTable(TableInfo.builder().tableName(ss[0]).partSpec(map)
                                         .label(ss[2]).build(), job);
                }
            } else {
                System.err.println("Style of output: " + out + " is not right");
                System.exit(1);
            }
        }
        JobClient.runJob(job);
    }
}
```

##### 7.1.6.4. 多任务示例

本文提供MapReduce多任务的示例代码，通过定义Mapper类并结合JobConf配置任务参数，展示如何在MapReduce框架中依次执行多个作业，并实现作业状态的监控与管理。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Iterator; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.RunningJob; import com.aliyun.odps.mapred.TaskContext; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; /**
     * MultiJobs
```

*

```
     * Running multiple job
```

*

```java
     **/
public class MultiJobs {
    public static class InitMapper extends MapperBase {
        @Override
            public void setup(TaskContext context) throws IOException {
            Record record = context.createOutputRecord();
            long v = context.getJobConf().getLong("multijobs.value", 2);
            record.set(0, v);
            context.write(record);
        }
    }
    public static class DecreaseMapper extends MapperBase {
        @Override
            public void cleanup(TaskContext context) throws IOException {
            long expect = context.getJobConf().getLong("multijobs.expect.value", -1);
            long v = -1;
            int count = 0;
```

`//`读取资源表里面的数据，这个表是上一个`job`的输出表。

```
            Iterator<Record> iter = context.readResourceTable("multijobs_res_table");
            while (iter.hasNext()) {
                Record r = iter.next();
                v = (Long) r.get(0);
                if (expect != v) {
                    throw new IOException("expect: " + expect + ", but: " + v);
                }
                count++;
            }
            if (count != 1) {
                throw new IOException("res_table should have 1 record, but: " + count);
            }
            Record record = context.createOutputRecord();
            v--;
            record.set(0, v);
            context.write(record);
```

`//`设置`counter`，`counter`在作业成功结束后，可以在`main`函数中获取到。

```
            context.getCounter("multijobs", "value").setValue(v);
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            System.err.println("Usage: TestMultiJobs <table>");
            System.exit(1);
        }
        String tbl = args[0];
        long iterCount = 2;
        System.err.println("Start to run init job.");
        JobConf initJob = new JobConf();
        initJob.setLong("multijobs.value", iterCount);
        initJob.setMapperClass(InitMapper.class);
        InputUtils.addTable(TableInfo.builder().tableName("mr_empty").build(), initJob);
        OutputUtils.addTable(TableInfo.builder().tableName(tbl).build(), initJob);
        initJob.setMapOutputKeySchema(SchemaUtils.fromString("key:string"));
        initJob.setMapOutputValueSchema(SchemaUtils.fromString("value:string"));
```

`//maponly`作业需要显式设置`reducer`的数目为0。

```
        initJob.setNumReduceTasks(0);
        JobClient.runJob(initJob);
        while (true) {
            System.err.println("Start to run iter job, count: " + iterCount);
            JobConf decJob = new JobConf();
            decJob.setLong("multijobs.expect.value", iterCount);
            decJob.setMapperClass(DecreaseMapper.class);
            InputUtils.addTable(TableInfo.builder().tableName("mr_empty").build(), decJob);
OtptUtilsaddTable(TableInfobilder()tableName(tbl)bild() decJob)
```

```
            OutputUtils.addTable(TableInfo.builder().tableName(tbl).build(), decJob);
```

`//maponly`作业需要显式设置`reducer`的数目为0。

```
            decJob.setNumReduceTasks(0);
            RunningJob rJob = JobClient.runJob(decJob);
            iterCount--;
```

`//`如果迭代次数已经达到，则退出循环。

```
            if (rJob.getCounters().findCounter("multijobs", "value").getValue() == 0) {
                break;
            }
        }
        if (iterCount != 0) {
            throw new IOException("Job failed.");
        }
    }
}
```

##### 7.1.6.5. 二次排序示例

本文提供代码示例，介绍如何在MaxCompute中通过自定义MapReduce实现输入数据的二次排序与分组。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Iterator; import com.aliyun.odps.data.Record; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.ReducerBase; import com.aliyun.odps.mapred.TaskContext; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.SchemaUtils; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.data.TableInfo; /**
```

*

```
     * This is an example ODPS Map/Reduce application. It reads the input table that
     * must contain two integers per record. The output is sorted by the first and
     * second number and grouped on the first number.
```

*

```java
     **/
public class SecondarySort {
    /**
       * Read two integers from each line and generate a key, value pair as ((left,
       * right), right).
       **/
    public static class MapClass extends MapperBase {
        private Record key;
        private Record value;
        @Override
            public void setup(TaskContext context) throws IOException {
            key = context.createMapOutputKeyRecord();
            value = context.createMapOutputValueRecord();
        }
        @Override
            public void map(long recordNum, Record record, TaskContext context)
            throws IOException {
            long left = 0;
            long right = 0;
            if (record.getColumnCount() > 0) {
                left = (Long) record.get(0);
                if (record.getColumnCount() > 1) {
                    right = (Long) record.get(1);
                }
                key.set(new Object[] { (Long) left, (Long) right });
                value.set(new Object[] { (Long) right });
                context.write(key, value);
            }
        }
    }
    /**
       * A reducer class that just emits the sum of the input values.
       **/
    public static class ReduceClass extends ReducerBase {
        private Record result = null;
        @Override
            public void setup(TaskContext context) throws IOException {
            result = context.createOutputRecord();
        }
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
            throws IOException {
```

```
            result.set(0, key.get(0));
            while (values.hasNext()) {
                Record value = values.next();
                result.set(1, value.get(0));
                context.write(result);
            }
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: secondarysrot <in> <out>");
            System.exit(2);
        }
        JobConf job = new JobConf();
        job.setMapperClass(MapClass.class);
        job.setReducerClass(ReduceClass.class);
```

`//`将多列设置为`Key`。

```
        //compare first and second parts of the pair
        job.setOutputKeySortColumns(new String[] { "i1", "i2" });
        //partition based on the first part of the pair
        job.setPartitionColumns(new String[] { "i1" });
        //grouping comparator based on the first part of the pair
        job.setOutputGroupingColumns(new String[] { "i1" });
        //the map output is LongPair, Long
        job.setMapOutputKeySchema(SchemaUtils.fromString("i1:bigint,i2:bigint"));
        job.setMapOutputValueSchema(SchemaUtils.fromString("i2x:bigint"));
        InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), job);
        OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
        JobClient.runJob(job);
        System.exit(0);
    }
}
```

##### 7.1.6.6. 资源使用示例

本文通过定义UploadMapper类并配置JobConf，提供了一个使用MapReduce将文本文件导入MaxCompute表的完整示例，展示了如何在作业中加载和使用资源。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.BufferedInputStream; import java.io.FileNotFoundException; import java.io.IOException; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.TaskContext; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; /**
     * Upload
```

*

```
     * Import data from text file into table
```

*

```java
     **/
public class Upload {
    public static class UploadMapper extends MapperBase {
        @Override
            public void setup(TaskContext context) throws IOException {
            Record record = context.createOutputRecord();
            StringBuilder importdata = new StringBuilder();
            BufferedInputStream bufferedInput = null;
            try {
                byte[] buffer = new byte[1024];
                int bytesRead = 0;
                String filename = context.getJobConf().get("import.filename");
                bufferedInput = context.readResourceFileAsStream(filename);
                while ((bytesRead = bufferedInput.read(buffer)) != -1) {
                    String chunk = new String(buffer, 0, bytesRead);
                    importdata.append(chunk);
                }
                String lines[] = importdata.toString().split("\n");
                for (int i = 0; i < lines.length; i++) {
                    String[] ss = lines[i].split(",");
                    record.set(0, Long.parseLong(ss[0].trim()));
                    record.set(1, ss[1].trim());
                    context.write(record);
                }
            } catch (FileNotFoundException ex) {
                throw new IOException(ex);
            } catch (IOException ex) {
                throw new IOException(ex);
            } finally {
            }
        }
        @Override
            public void map(long recordNum, Record record, TaskContext context)
            throws IOException {
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: Upload <import_txt> <out_table>");
            System.exit(2);
        }
        JobConf job = new JobConf();
        job.setMapperClass(UploadMapper.class);
        job.set("import.filename", args[0]);
```

`//maponly`作业需要显式设置`reducer`的数目为0。

```
        job.setNumReduceTasks(0);
        job.setMapOutputKeySchema(SchemaUtils.fromString("key:bigint"));
        job.setMapOutputValueSchema(SchemaUtils.fromString("value:string"));
        InputUtils.addTable(TableInfo.builder().tableName("mr_empty").build(), job);
        OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
        JobClient.runJob(job);
    }
}
```

**说明**

##### 7.1.6.7. 使用Counter示例

本文通过完整代码示例，展示如何在MaxCompute的MapReduce作业中使用自定义Counter。通过在Mapper和Reducer阶段分别定义和更新计数器，并在作业完成后读取其值，实现对任务执行情况的细粒度监控与统计。

**代码示例**

您可以在Map/Reduce的Setup、Map/Reduce及Cleanup接口中获取任意自定义Counter，并进行操作。代码示例如下。

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Iterator; import com.aliyun.odps.counter.Counter; import com.aliyun.odps.counter.Counters; import com.aliyun.odps.data.Record; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.ReducerBase; import com.aliyun.odps.mapred.RunningJob; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.SchemaUtils; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.data.TableInfo; /**
```

*

```
     * User Defined Counters
```

*

```java
     **/
public class UserDefinedCounters {
    enum MyCounter {
        TOTAL_TASKS, MAP_TASKS, REDUCE_TASKS
    }
    public static class TokenizerMapper extends MapperBase {
        private Record word;
        private Record one;
        @Override
            public void setup(TaskContext context) throws IOException {
            super.setup(context);
            Counter map_tasks = context.getCounter(MyCounter.MAP_TASKS);
            Counter total_tasks = context.getCounter(MyCounter.TOTAL_TASKS);
            map_tasks.increment(1);
            total_tasks.increment(1);
            word = context.createMapOutputKeyRecord();
            one = context.createMapOutputValueRecord();
            one.set(new Object[] { 1L });
        }
        @Override
            public void map(long recordNum, Record record, TaskContext context)
            throws IOException {
            for (int i = 0; i < record.getColumnCount(); i++) {
                word.set(new Object[] { record.get(i).toString() });
                context.write(word, one);
            }
        }
    }
    public static class SumReducer extends ReducerBase {
        private Record result = null;
        @Override
            public void setup(TaskContext context) throws IOException {
            result = context.createOutputRecord();
            Counter reduce_tasks = context.getCounter(MyCounter.REDUCE_TASKS);
            Counter total_tasks = context.getCounter(MyCounter.TOTAL_TASKS);
            reduce_tasks.increment(1);
            total_tasks.increment(1);
        }
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
            throws IOException {
            long count = 0;
            while (values.hasNext()) {
                Record val = values.next();
                count += (Long) val.get(0);
            }
            result.set(0, key.get(0));
            result.set(1, count);
            context.write(result);
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err
                .println("Usage: TestUserDefinedCounters <in_table> <out_table>");
System.exit(2);
```

```
            System.exit(2);
        }
        JobConf job = new JobConf();
        job.setMapperClass(TokenizerMapper.class);
        job.setReducerClass(SumReducer.class);
        job.setMapOutputKeySchema(SchemaUtils.fromString("word:string"));
        job.setMapOutputValueSchema(SchemaUtils.fromString("count:bigint"));
        InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), job);
        OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
        RunningJob rJob = JobClient.runJob(job);
```

`//`在作业成功结束后，可以获取到`Job`里面的自定义`Counter`的值。

```
        Counters counters = rJob.getCounters();
        long m = counters.findCounter(MyCounter.MAP_TASKS).getValue();
        long r = counters.findCounter(MyCounter.REDUCE_TASKS).getValue();
        long total = counters.findCounter(MyCounter.TOTAL_TASKS).getValue();
        System.exit(0);
    }
}
```

##### 7.1.6.8. Grep示例

本文提供一个MaxCompute MapReduce的Grep示例，演示如何利用正则表达式从输入表中提取匹配项，统计其出现频次，并按频次降序排序输出结果。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Iterator; import java.util.regex.Matcher; import java.util.regex.Pattern; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.Mapper; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.ReducerBase; import com.aliyun.odps.mapred.RunningJob; import com.aliyun.odps.mapred.TaskContext; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; /**
```

*

```
     * Extracts matching regexs from input files and counts them.
```

*

```java
     **/
public class Grep {
    /**
       * RegexMapper
       **/
        private Pattern pattern;
        private int group;
        private Record word;
        private Record one;
        @Override
            public void setup(TaskContext context) throws IOException {
            JobConf job = (JobConf) context.getJobConf();
            pattern = Pattern.compile(job.get("mapred.mapper.regex"));
            group = job.getInt("mapred.mapper.regex.group", 0);
            word = context.createMapOutputKeyRecord();
            one = context.createMapOutputValueRecord();
            one.set(new Object[] { 1L });
        }
        @Override
            public void map(long recordNum, Record record, TaskContext context) throws IOException {
            for (int i = 0; i < record.getColumnCount(); ++i) {
                String text = record.get(i).toString();
                Matcher matcher = pattern.matcher(text);
                while (matcher.find()) {
                    word.set(new Object[] { matcher.group(group) });
                    context.write(word, one);
                }
            }
        }
    }
    /**
       * LongSumReducer
       **/
    public class LongSumReducer extends ReducerBase {
        private Record result = null;
        @Override
```

```java
            public void setup(TaskContext context) throws IOException {
            result = context.createOutputRecord();
        }
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context) throws IOException {
            long count = 0;
            while (values.hasNext()) {
                Record val = values.next();
                count += (Long) val.get(0);
            }
            result.set(0, key.get(0));
            result.set(1, count);
            context.write(result);
        }
    }
    /**
       * A {@link Mapper} that swaps keys and values.
       **/
    public class InverseMapper extends MapperBase {
        private Record word;
        private Record count;
        @Override
            public void setup(TaskContext context) throws IOException {
            word = context.createMapOutputValueRecord();
            count = context.createMapOutputKeyRecord();
        }
        /**
         * The inverse function. Input keys and values are swapped.
         **/
        @Override
            public void map(long recordNum, Record record, TaskContext context) throws IOException {
            word.set(new Object[] { record.get(0).toString() });
            count.set(new Object[] { (Long) record.get(1) });
            context.write(count, word);
        }
    }
    /**
       * IdentityReducer
       **/
    public class IdentityReducer extends ReducerBase {
        private Record result = null;
        @Override
            public void setup(TaskContext context) throws IOException {
            result = context.createOutputRecord();
        }
        /** Writes all keys and values directly to output. **/
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context) throws IOException {
            result.set(0, key.get(0));
            while (values.hasNext()) {
                Record val = values.next();
                result.set(1, val.get(0));
                context.write(result);
            }
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length < 4) {
            System.err.println("Grep <inDir> <tmpDir> <outDir> <regex> [<group>]");
            System.exit(2);
        }
        JobConf grepJob = new JobConf();
        grepJob.setMapperClass(RegexMapper.class);
        grepJob.setReducerClass(LongSumReducer.class);
        grepJob.setMapOutputKeySchema(SchemaUtils.fromString("word:string"));
        grepJob.setMapOutputValueSchema(SchemaUtils.fromString("count:bigint"));
        InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), grepJob);
        OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), grepJob);
```

`//`设置`grepJob`的`grep`的正则表达式。

```
        grepJob.set("mapred.mapper.regex", args[3]);
        if (args.length == 5) {
            grepJob.set("mapred.mapper.regex.group", args[4]);
        }
        @SuppressWarnings("unused")
            RunningJob rjGrep = JobClient.runJob(grepJob);
```

`//grepJob`的输出作为`sortJob`的输入。

```
        JobConf sortJob = new JobConf();
        sortJob.setMapperClass(InverseMapper.class);
        sortJob.setReducerClass(IdentityReducer.class);
        sortJob.setMapOutputKeySchema(SchemaUtils.fromString("count:bigint"));
        sortJob.setMapOutputValueSchema(SchemaUtils.fromString("word:string"));
        InputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), sortJob);
        OutputUtils.addTable(TableInfo.builder().tableName(args[2]).build(), sortJob);
sortJob.setNumReduceTasks(1);//writeasinglefile
```

```
        sortJob.setNumReduceTasks(1); // write a single file
        sortJob.setOutputKeySortColumns(new String[] { "count" });
        @SuppressWarnings("unused")
            RunningJob rjSort = JobClient.runJob(sortJob);
    }
}
```

##### 7.1.6.9. Join示例

MaxCompute的MapReduce框架自身不提供内置的Join操作，但您可通过自定义Map/Reduce函数实现表连接。本文提供一个Reduce-side Join示例，演示如何将两张表按键关联，并输出连接结果。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.ArrayList; import java.util.Iterator; import java.util.List; import org.apache.commons.logging.Log; import org.apache.commons.logging.LogFactory; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.ReducerBase; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; /**
     * Join, mr_Join_src1/mr_Join_src2(key bigint, value string), mr_Join_out(key
     * bigint, value1 string, value2 string)
```

* `*/`

```java
public class Join {
    public static final Log LOG = LogFactory.getLog(Join.class);
    public static class JoinMapper extends MapperBase {
        private Record mapkey;
        private Record mapvalue;
        private long tag;
        @Override
            public void setup(TaskContext context) throws IOException {
            mapkey = context.createMapOutputKeyRecord();
            mapvalue = context.createMapOutputValueRecord();
            tag = context.getInputTableInfo().getLabel().equals("left") ? 0 : 1;
        }
        @Override
            public void map(long key, Record record, TaskContext context)
            throws IOException {
            mapkey.set(0, record.get(0));
            mapkey.set(1, tag);
            for (int i = 1; i < record.getColumnCount(); i++) {
                mapvalue.set(i - 1, record.get(i));
            }
            context.write(mapkey, mapvalue);
        }
    }
    public static class JoinReducer extends ReducerBase {
        private Record result = null;
        @Override
            public void setup(TaskContext context) throws IOException {
            result = context.createOutputRecord();
        }
```

`//reduce`函数每次的输入会是`key`相同的所有`record`。

```java
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
            throws IOException {
            long k = key.getBigint(0);
            List<Object[]> leftValues = new ArrayList<Object[]>();
```

`//`由于设置了`outputKeySortColumn`是`key + tag`组合，这样可以保证`reduce`函数的输入`record`中，`left`表的`record`数据在前面。

```
            while (values.hasNext()) {
                Record value = values.next();
                long tag = (Long) key.get(1);
```

`//`左表的数据会先缓存到内存中。

```
                if (tag == 0) {
                    leftValues.add(value.toArray().clone());
                } else {
```

`//`右表的数据会与所有左表的数据进行`join`输出，此时左表的数据已经全部在内存里了。 `//`这个实现只是一个功能展示，性能较低，不建议用于实际生产。

```
                    for (Object[] leftValue : leftValues) {
                        int index = 0;
                        result.set(index++, k);
```

f

```
(i
```

i i lf l l h i

```
){
```

```
                        for (int i = 0; i < leftValue.length; i++) {
                            result.set(index++, leftValue[i]);
                        }
                        for (int i = 0; i < value.getColumnCount(); i++) {
                            result.set(index++, value.get(i));
                        }
                        context.write(result);
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length != 3) {
            System.err.println("Usage: Join <input table1> <input table2> <out>");
            System.exit(2);
        }
        JobConf job = new JobConf();
        job.setMapperClass(JoinMapper.class);
        job.setReducerClass(JoinReducer.class);
        job.setMapOutputKeySchema(SchemaUtils.fromString("key:bigint,tag:bigint"));
        job.setMapOutputValueSchema(SchemaUtils.fromString("value:string"));
        job.setPartitionColumns(new String[]{"key"});
        job.setOutputKeySortColumns(new String[]{"key", "tag"});
        job.setOutputGroupingColumns(new String[]{"key"});
        job.setNumReduceTasks(1);
        InputUtils.addTable(TableInfo.builder().tableName(args[0]).label("left").build(), job);
        InputUtils.addTable(TableInfo.builder().tableName(args[1]).label("right").build(), job);
        OutputUtils.addTable(TableInfo.builder().tableName(args[2]).build(), job);
        JobClient.runJob(job);
    }
}
```

##### 7.1.6.10. Sleep示例

本文介绍了一个MapReduce的Sleep示例，展示如何通过设置JobConf参数实现任务延迟执行。示例包括Mapper类的实现与任务配置，适用于无输入数据的 MapOnly任务。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.conf.JobConf; public class Sleep {
  private static final String SLEEP_SECS = "sleep.secs";
  public static class MapperClass extends MapperBase {
```

`//`由于没有输入数据，`map`函数不会被执行，相关逻辑只能写在`setup`中。

```java
    @Override
    public void setup(TaskContext context) throws IOException {
      try {
        Thread.sleep(context.getJobConf().getInt(SLEEP_SECS, 1) * 1000);
      } catch (InterruptedException e) {
        throw new RuntimeException(e);
      }
    }
  }
  public static void main(String[] args) throws Exception {
    if (args.length != 1) {
      System.err.println("Usage: Sleep <sleep_secs>");
      System.exit(-1);
    }
    JobConf job = new JobConf();
    job.setMapperClass(MapperClass.class);
```

`//`这个实例也是一个`MapOnly`的，所以需要设置`reducer`个数为0。

```
    job.setNumReduceTasks(0);
```

`//`由于没有输入表，`mapper`的个数需要由用户明确进行指定。

```
    job.setNumMapTasks(1);
    job.set(SLEEP_SECS, args[0]);
    JobClient.runJob(job);
  }
}
```

##### 7.1.6.11. Unique示例

本文提供一个MaxCompute MapReduce的去重（Unique）示例，通过自定义Mapper和Reducer实现数据去重，支持按键（key）、值（value）或键值对 （key+value）三种模式。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Iterator; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.ReducerBase; import com.aliyun.odps.mapred.TaskContext; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; /**
     * Unique Remove duplicate words
```

*

```java
     **/
public class Unique {
    public static class OutputSchemaMapper extends MapperBase {
        private Record key;
        private Record value;
        @Override
            public void setup(TaskContext context) throws IOException {
            key = context.createMapOutputKeyRecord();
            value = context.createMapOutputValueRecord();
        }
        @Override
            public void map(long recordNum, Record record, TaskContext context)
            throws IOException {
            long left = 0;
            long right = 0;
            if (record.getColumnCount() > 0) {
                left = (Long) record.get(0);
                if (record.getColumnCount() > 1) {
                    right = (Long) record.get(1);
                }
                key.set(new Object[] { (Long) left, (Long) right });
                value.set(new Object[] { (Long) left, (Long) right });
                context.write(key, value);
            }
        }
    }
    public static class OutputSchemaReducer extends ReducerBase {
        private Record result = null;
        @Override
            public void setup(TaskContext context) throws IOException {
            result = context.createOutputRecord();
        }
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
            throws IOException {
            result.set(0, key.get(0));
            while (values.hasNext()) {
                Record value = values.next();
                result.set(1, value.get(1));
            }
            context.write(result);
        }
    }
    public static void main(String[] args) throws Exception {
        if (args.length > 3 || args.length < 2) {
            System.err.println("Usage: unique <in> <out> [key|value|all]");
            System.exit(2);
        }
        String ops = "all";
        if (args.length == 3) {
            ops = args[2];
        }
```

`// Reduce`的输入分组是由`setOutputGroupingColumns`的设置来决定的，这个参数如果不设置，默认就是`MapOutputKeySchema`。

```
        // Key Unique
        if (ops.equals("key")) {
            JobConf job = new JobConf();
            job.setMapperClass(OutputSchemaMapper.class);
            job.setReducerClass(OutputSchemaReducer.class);
            job.setMapOutputKeySchema(SchemaUtils.fromString("key:bigint,value:bigint"));
            job.setMapOutputValueSchema(SchemaUtils.fromString("key:bigint,value:bigint"));
            job.setPartitionColumns(new String[] { "key" });
            job.setOutputKeySortColumns(new String[] { "key", "value" });
            job.setOutputGroupingColumns(new String[] { "key" });
            job.set("tablename2", args[1]);
            job.setNumReduceTasks(1);
            job.setInt("table.counter", 0);
            InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), job);
OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(),job);
```

```
            OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
            JobClient.runJob(job);
        }
        // Key&Value Unique
        if (ops.equals("all")) {
            JobConf job = new JobConf();
            job.setMapperClass(OutputSchemaMapper.class);
            job.setReducerClass(OutputSchemaReducer.class);
            job.setMapOutputKeySchema(SchemaUtils.fromString("key:bigint,value:bigint"));
            job.setMapOutputValueSchema(SchemaUtils.fromString("key:bigint,value:bigint"));
            job.setPartitionColumns(new String[] { "key" });
            job.setOutputKeySortColumns(new String[] { "key", "value" });
            job.setOutputGroupingColumns(new String[] { "key", "value" });
            job.set("tablename2", args[1]);
            job.setNumReduceTasks(1);
            job.setInt("table.counter", 0);
            InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), job);
            OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
            JobClient.runJob(job);
        }
        // Value Unique
        if (ops.equals("value")) {
            JobConf job = new JobConf();
            job.setMapperClass(OutputSchemaMapper.class);
            job.setReducerClass(OutputSchemaReducer.class);
            job.setMapOutputKeySchema(SchemaUtils.fromString("key:bigint,value:bigint"));
            job.setMapOutputValueSchema(SchemaUtils.fromString("key:bigint,value:bigint"));
            job.setPartitionColumns(new String[] { "value" });
            job.setOutputKeySortColumns(new String[] { "value" });
            job.setOutputGroupingColumns(new String[] { "value" });
            job.set("tablename2", args[1]);
            job.setNumReduceTasks(1);
            job.setInt("table.counter", 0);
            InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), job);
            OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
            JobClient.runJob(job);
        }
    }
}
```

##### 7.1.6.12. Sort示例

本文提供MaxCompute MapReduce的排序（Sort）示例，演示如何通过定义IdentityMapper和IdentityReducer、配置JobConf、指定输入输出表并提交作业，实现对小规模数据的分片与全局有序输出。

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Date; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.TaskContext; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.example.Identity.IdentityReducer; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; /**
     * This is the trivial map/reduce program that does absolutely nothing other
     * than use the framework to fragment and sort the input values.
```

*

```java
     **/
public class Sort {
 static int printUsage() {
  System.out.println("sort <input> <output>");
  return -1;
 }
 /**
       * Implements the identity function, mapping record's first two columns to
       * outputs.
       **/
 public static class IdentityMapper extends MapperBase {
  private Record key;
  private Record value;
  @Override
   public void setup(TaskContext context) throws IOException {
   key = context.createMapOutputKeyRecord();
   value = context.createMapOutputValueRecord();
  }
  @Override
   public void map(long recordNum, Record record, TaskContext context)
   throws IOException {
   key.set(new Object[] { (Long) record.get(0) });
   value.set(new Object[] { (Long) record.get(1) });
   context.write(key, value);
  }
 }
 /**
       * The main driver for sort program. Invoke this method to submit the
       * map/reduce job.
```

*

```
       * @throws IOException
       *           When there is communication problems with the job tracker.
       **/
 public static void main(String[] args) throws Exception {
  JobConf jobConf = new JobConf();
  jobConf.setMapperClass(IdentityMapper.class);
  jobConf.setReducerClass(IdentityReducer.class);
```

`//`为了全局有序，这里设置了`reducer`的个数为1，所有的数据都会集中到一个`reducer`上面。 `//`只能用于小数据量，大数据量需要考虑其他的方式，比如`TeraSort`。

```java
  jobConf.setNumReduceTasks(1);
  jobConf.setMapOutputKeySchema(SchemaUtils.fromString("key:bigint"));
  jobConf.setMapOutputValueSchema(SchemaUtils.fromString("value:bigint"));
  InputUtils.addTable(TableInfo.builder().tableName(args[0]).build(), jobConf);
  OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), jobConf);
  Date startTime = new Date();
  System.out.println("Job started: " + startTime);
  JobClient.runJob(jobConf);
  Date end_time = new Date();
  System.out.println("Job ended: " + end_time);
  System.out.println("The job took " + (end_time.getTime() - startTime.getTime()) / 1000 + " seconds.");
 }
}
```

##### 7.1.6.13. 分区表输入示例

本文提供使用MaxCompute MapReduce与 SDK读取分区表的代码示例，展示如何配置MapReduce作业并指定输入分区。

**代码示例**

示例一：

```
public static void main(String[] args) throws Exception {
    JobConf job = new JobConf();
    ...
        LinkedHashMap<String, String> input = new LinkedHashMap<String, String>();
    input.put("pt", "123456");
    InputUtils.addTable(TableInfo.builder().tableName("input_table").partSpec(input).build(), job);
    LinkedHashMap<String, String> output = new LinkedHashMap<String, String>();
    output.put("ds", "654321");
    OutputUtils.addTable(TableInfo.builder().tableName("output_table").partSpec(output).build(), job);
    JobClient.runJob(job);
}
```

示例二

```java
package com.aliyun.odps.mapred.open.example; ...
    public static void main(String[] args) throws Exception {
    if (args.length != 2) {
        System.err.println("Usage: WordCount <in_table> <out_table>");
        System.exit(2);
    }
    JobConf job = new JobConf();
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(SumCombiner.class);
    job.setReducerClass(SumReducer.class);
    job.setMapOutputKeySchema(SchemaUtils.fromString("word:string"));
    job.setMapOutputValueSchema(SchemaUtils.fromString("count:bigint"));
    Account account = new AliyunAccount("my_access_id", "my_access_key");
    Odps odps = new Odps(account);
    odps.setEndpoint("odps_endpoint_url");
    odps.setDefaultProject("my_project");
    Table table = odps.tables().get(tblname);
    TableInfoBuilder builder = TableInfo.builder().tableName(tblname);
    for (Partition p : table.getPartitions()) {
        if (applicable(p)) {
            LinkedHashMap<String, String> partSpec = new LinkedHashMap<String, String>();
            for (String key : p.getPartitionSpec().keys()) {
                partSpec.put(key, p.getPartitionSpec().get(key));
            }
            InputUtils.addTable(builder.partSpec(partSpec).build(), job);
        }
    }
    OutputUtils.addTable(TableInfo.builder().tableName(args[1]).build(), job);
    JobClient.runJob(job);
}
```

**说明**

上述示例是使用MaxCompute SDK和MapReduce SDK组合实现MapReduce任务读取范围分区的示例。 此段代码不能编译执行，仅给出了Main函数的示例。 示例中Applicable函数是用户逻辑，用于决定该分区是否可以作为MapReduce作业的输入。

##### 7.1.6.14. Pipeline示例

本文提供MaxCompute MapReduce Pipeline示例，通过TokenizerMapper、SumReducer和IdentityReducer构建多阶段作业，实现词频统计，并展示如何在

**代码示例**

```java
package com.aliyun.odps.mapred.open.example; import java.io.IOException; import java.util.Iterator; import com.aliyun.odps.Column; import com.aliyun.odps.OdpsException; import com.aliyun.odps.OdpsType; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.mapred.Job; import com.aliyun.odps.mapred.MapperBase; import com.aliyun.odps.mapred.ReducerBase; import com.aliyun.odps.pipeline.Pipeline;
    public static class TokenizerMapper extends MapperBase {
        Record word;
        Record one;
        @Override
            public void setup(TaskContext context) throws IOException {
            word = context.createMapOutputKeyRecord();
            one = context.createMapOutputValueRecord();
            one.setBigint(0, 1L);
        }
        @Override
```

```java
            public void map(long recordNum, Record record, TaskContext context)
            throws IOException {
            for (int i = 0; i < record.getColumnCount(); i++) {
                String[] words = record.get(i).toString().split("\\s+");
                for (String w : words) {
                    word.setString(0, w);
                    context.write(word, one);
                }
            }
        }
    }
    public static class SumReducer extends ReducerBase {
        private Record value;
        @Override
            public void setup(TaskContext context) throws IOException {
            value = context.createOutputValueRecord();
        }
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
            throws IOException {
            long count = 0;
            while (values.hasNext()) {
                Record val = values.next();
                count += (Long) val.get(0);
            }
            value.set(0, count);
            context.write(key, value);
        }
    }
    public static class IdentityReducer extends ReducerBase {
        private Record result;
        @Override
            public void setup(TaskContext context) throws IOException {
            result = context.createOutputRecord();
        }
        @Override
            public void reduce(Record key, Iterator<Record> values, TaskContext context)
            throws IOException {
            while (values.hasNext()) {
                result.set(0, key.get(0));
                result.set(1, values.next().get(0));
                context.write(result);
            }
        }
    }
    public static void main(String[] args) throws OdpsException {
        if (args.length != 2) {
            System.err.println("Usage: WordCountPipeline <in_table> <out_table>");
            System.exit(2);
        }
        Job job = new Job();
        /***
```

* 构造`Pipeline`的过程中，如果不指定`Mapper`的`OutputKeySortColumns`、`PartitionColumns`、`OutputGroupingColumns`，框架会默认使用其`OutputKey`作为此
三者的默认配置。

```
         ***/
            .addMapper(TokenizerMapper.class)
            .setOutputKeySchema(
            new Column[] { new Column("word", OdpsType.STRING) })
            .setOutputValueSchema(
            new Column[] { new Column("count", OdpsType.BIGINT) })
            .setOutputKeySortColumns(new String[] { "word" })
            .setPartitionColumns(new String[] { "word" })
            .setOutputGroupingColumns(new String[] { "word" })
            .addReducer(SumReducer.class)
            .setOutputKeySchema(
            new Column[] { new Column("word", OdpsType.STRING) })
            .setOutputValueSchema(
            new Column[] { new Column("count", OdpsType.BIGINT)})
            .addReducer(IdentityReducer.class).createPipeline();
```

`//`将`pipeline`的设置到`jobconf`中，如果需要设置`combiner`，是通过`jobconf`来设置。

```
        job.setPipeline(pipeline);
```

`//`设置输入输出表。

```
        job.addInput(TableInfo.builder().tableName(args[0]).build());
        job.addOutput(TableInfo.builder().tableName(args[1]).build());
```

`//`作业提交并等待结束。

```
        job.submit();
        job.waitForCompletion();
        System.exit(job.isSuccessful() == true ? 0 : 1);
    }
}
```

r

## MaxCompute MCP Server

MaxCompute基于MCP协议，支持通过飞天助理-托管模式调用API获取项目实例信息，也可通过自行部署MCP Server方式与AI Studio、百炼Agent、Dify、Cherry Studio等平台集成实现ODPS SQL查询，助力用户打造自然语言驱动的数据查询Agent，实现从提问到可视化的智能数据处理全流程。

**支持MCP模式**

飞天助理-托管模式飞天助理托管模式开箱即用，无需用户配置，可以直接通过大模型访问。 自行部署MCP Server 用户可以在应用、智能体或AI中自行部署。

**飞天助理-托管模式**

**说明**

使用飞天助理-托管模式前，请先参考**统一云管平台** > **飞天助理****用户指南**文档开启飞天助手。
1. 使用管理员身份登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **大数据计算** > **云原生大数据计算服务** **MaxCompute** ，进入**概览**页面。
3. 查看系统预设的MCP列表。
在左侧导航栏单击**AI****专栏** **> AI****原生接口****-MCP****服务**，查看系统预设的MCP列表。当前系统预设工具如下：

| 工具名称 | 调用接口 | 说明 |
|---|---|---|
| 实例列表查询 | ListCalcEnginesForAscm | 列出本用户下的Project实例列表，方便用户查看和管理名下Project实例。 |
| 实例详情查询 | GetCalEngineForAscm | 列出指定Project实例的名称、组织、地域、Endpoint、容灾等详情信息，方便用户查询 Project实例配置详情，有助于管理与运维实例。 |

4. 使用飞天助理调用预设工具。
i. 在页面顶部单击工具栏中的图标，进入**飞天助理**页。 ii. 在对话框底部单击图标，打开**MCP**开关，单击图标进入**选择** **MCP**页面。 iii. 选择已有的MaxCompute MCP（**云原生大数据计算服务****MaxCompute** ）。 iv. 单击**确定**，返回对话框，使用自然语言描述查询内容，例如“查询当前用户下的Project实例列表”。 v. 单击右侧的图标发送并执行指令信息。 vi. 等待任务执行结束，您可查看返回的结果信息。

**自行部署MCP Server**

1. 下载MCP服务包。
2. 部署在ECS、容器或云外服务器。
3. 集成至应用或智能体：将MCP作为后端服务嵌入AI应用、智能体（Agent）或RPA流程中。
4. 通过RESTful API调用MCP功能（如需通过MCP只读Project实例下的表数据，您可对用户进行相应授权操作，详情请参见ACL授权）。

## PyODPS

### PyODPS概述

PyODPS是MaxCompute的Python版本的SDK。提供简单方便的Python编程接口，以便您使用Python编写MaxCompute作业、查询MaxCompute表和视图，以及管理MaxCompute资源。PyODPS提供了与ODPS命令行工具类似的功能，例如上传和下载文件、创建表、运行ODPS SQL查询等，同时提供了一些高级功能，如提交MapReduce任务、使用ODPS UDF等。本文为您介绍PyODPS的应用场景、支持的工具，及使用过程中需要关注的注意事项等。

#### 功能介绍

DataFrame Sequence及执行：PyODPS的Sequence及执行操作。

**支持的工具**

**重要**

无论您通过何种工具使用PyODPS，建议您尽量避免将全量数据下载到本地直接运行PyODPS任务，容易占用大量内存造成OOM，建议您将任务提交到 MaxCompute进行分布式运行，对比介绍请参见下文的注意事项：请勿下载全量数据到本地并运行PyODPS。 本地环境：您可以在本地环境安装并使用PyODPS，操作指导可参见通过本地环境使用PyODPS。 DataWorks：DataWorks的PyODPS节点已安装好了PyODPS，您可以直接在DataWorks的PyODPS节点上开发PyODPS任务并周期性运行，操作指导请参见通 PAI Notebooks：PAI的Python环境也可安装运行PyODPS，其中PAI的内置镜像均已安装好了PyODPS可直接使用，如PAI-Designer的自定义python组件，在PAI Notebooks中使用PyODPS的方式与通用的使用方式基本一致，可参考基本操作概述、DataFrame概述。 PyODPS作为一个SDK，本身运行于各种客户端，包括PC、DataWorks（数据开发的PyODPS节点）或PAI Notebooks的运行环境。 需要注意的是，PyODPS提供了多种方便拉取数据到本地的操作，如tunnel下载操作、execute操作、to_pandas操作等，因此，很多初始使用PyODPS的用户会试图把数据拉取到本地，处理完成后再上传到 MaxCompute上，很多时候这种方式是十分低效的，拉取数据到本地彻底丧失了MaxCompute的大规模并行能力的优势。

| 数据处理方式 | 描述 | 场景示例 |
|---|---|---|
| 拉取到本地处理（不推荐， 易OOM） | 例如DataWorks中的PyODPS节点，内置了PyODPS包以及必要的Python 环境，是一个资源非常受限的客户端运行容器，并不使用MaxCompute计算资源，有较强的内存限制。 | PyODPS提供了 to_pandas 接口，可以直接将MaxCompute数据转化成Pandas DataFrame数据结构，但这个接口只应该被用于获取小规模数据做本地开发调试使用，而不是用来大规模处理数据，因为使用这个接口会触发下载行为，将位于MaxCompute中的海量数据下载到本地，如果后续操作的都是本地的DataFrame，则丧失了MaxCompute 的大规模并行计算能力，且数据量稍大时，单机内存就很容易产生OOM。 |
| 提交到MaxCompute分布式执行（推荐） | 推荐您合理利用PyODPS提供的分布式DataFrame功能，将主要的计算提交到MaxCompute分布式执行而不是在PyODPS客户端节点下载处理，这是正确使用PyODPS的关键。 | 推荐使用PyODPS DataFrame接口来完成数据处理。常见的需求，比如需要对每一行数据处理然后写回表，或者一行数据要拆成多行，都可以通过 PyODPS DataFrame中的 map 或者 apply 实现，有些甚至只需要一行代码，足够高效与简洁，案例可参见使用自定义函数及Python第三方库。 使用这些接口最终都会翻译成SQL到MaxCompute计算集群做分布式计算，并且本地几乎没有任何的内存消耗，相比于单机有很大的性能提升。 |

以下以一个分词的示例为例，为您对比两种方式的代码区别。 示例场景用户需要通过分析每天产生的日志字符串来提取一些信息，有一个只有一列的表，类型是string，通过jieba分词可以将中文语句分词，然后再找到想要的关键词存储到信息表里。 低效处理代码demo

```java
import jieba t = o.get_table('word_split') out = [] with t.open_reader() as reader:
    for r in reader:
        words = list(jieba.cut(r[0]))
```

#
# 处理逻辑，产生出 `processed_data`
#

```
        out.append(processed_data)
out_t = o.get_table('words') with out_t.open_writer() as writer:
    writer.write(out)
```

单机处理数据的思维，一行一行读出数据，然后一行一行处理数据，然后再一行一行写入目标表。整个流程中，下载上传数据消耗了大量的时间，并且在执行脚本的机器上需要很大的内存处理所有的数据，特别对于使用DataWorks节点的用户，很容易因为超过默认分配的内存值，导致OOM运行报错。 高效处理代码demo

```
from odps.df import output out_table = o.get_table('words') df = o.get_table('word_split').to_df()
```

# 假定需要返回的字段及类型如下

```java
out_names = ["word", "count"] out_types = ["string", "int"] @output(out_names, out_types) def handle(row):
    import jieba
    words = list(jieba.cut(row[0]))
```

#
# 处理逻辑，产生出 `processed_data`
#

```
    yield processed_data
df.apply(handle, axis=1).persist(out_table.name)
```

利用apply实现分布式执行： 复杂逻辑都放在handle这个函数里，这个函数会被自动序列化到服务端作为UDF使用，在服务端调用执行，且因为handle服务端实际执行时也是对每一行进行处理的，所以逻辑上是没有区别的。不同的是，这样写的程序在提交到MaxCompute端执行时，有多台机器同时处理数据，可以节约很多时间。 调用persist接口会将产生的数据直接写到另一张MaxCompute表中，所有的数据产生与消费都在 MaxCompute集群完成，也节约了本地的网络与内存。 在这个例子中也使用到了三方包，MaxCompute是支持自定义函数中使用三方包的（示例中的 `jieba` ），所以无需担心代码改动带来的成本，您可以几乎不需要改动主要逻辑就可以享受到MaxCompute的大规模计算能力。

**使用限制**

MaxCompute SQL限制项汇总。 由于沙箱的限制，部分Pandas计算后端执行本地调试通过的程序，无法在MaxCompute上调试通过。

### PyODPS快速入门

PyODPS可在DataWorks等数据开发平台中作为数据开发节点调用。这些平台提供了PyODPS运行环境和调度执行的能力，无需您手动创建ODPS入口对象。PyODPS 支持类似Pandas的快速、灵活和富有表现力的数据结构。您可以通过PyODPS提供的DataFrame API使用Pandas的数据结果处理功能。本文以DataWorks平台为

**操作步骤**

1. 登录DataWorks控制台。
2. 新建PyODPS 3节点。

**说明**

PyODPS节点获取本地处理的数据量不能超过50 MB，节点运行时占用的内存不能超过1 GB，否则节点任务会被系统终止。因此请避免在PyODPS任务中写入数据量较大的Python处理代码。 在DataWorks上编写代码并进行调试效率较低，为提升运行效率，建议本地安装IDEA进行代码开发。 i. 新建业务流程。 进入**数据开发**页面，右键单击**业务流程**，选择**新建业务流程**。 右键单击新建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 3**，输入节点**名称**，单击**确认**。
3. 编辑PyODPS节点。
i. 编写程序代码。 在PyODPS节点的编辑框中输入测试代码。以下是一个完整的使用PyODPS接口执行表操作的示例，更多关于表操作以及SQL操作的方法请参见表和SQL。

```python
from odps import ODPS
```

#以直接指定字段名以及字段类型的方式创建非分区表`my_new_table`。
#DataWorks的`PyODPS`节点中默认包含一个全局变量`odps`或者o，即为`ODPS`入口。您不需要手动定义`ODPS`入口，直接使用即可。更多信息，请参见通过`DataWorks`使用`PyODPS`。

```
table = o.create_table('my_new_table', 'num bigint, id string', if_not_exists=True)
```

#向非分区表`my_new_table`中插入数据。

```
records = [[111, 'aaa'],
          [222, 'bbb'],
          [333, 'ccc'],
```

`[444, '`中文`']]`

```
o.write_table(table, records)
```

#读取非分区表`my_new_table`中的数据。

```python
for record in o.read_table(table):
    print(record[0],record[1])
result = o.execute_sql('select * from my_new_table;',hints={'odps.sql.allow.fullscan': 'true'})
```

#读取`SQL`执行结果。

```python
with result.open_reader() as reader:
    for record in reader:
        print(record[0],record[1])
```

#删除表以清除资源。

```
table.drop()
```

ii. 运行代码。 完成编辑后，单击图标。运行结束后，您可以在下方的**运行日志**中看到运行结果。输出如下日志代表执行成功。

### 通过DataWorks使用PyODPS

PyODPS为MaxCompute的Python版SDK，支持在DataWorks中开发运行PyODPS任务。本文为您介绍在DataWorks上使用PyODPS的使用限制、主要流程和部分简单应用示例。

**使用限制**

**使用方式限制**

如果您发现有**Got killed**报错，即表明内存使用超限，进程被中止。请避免在PyODPS节点中直接下载数据并在DataWorks中处理数据，建议将数据处理任务提交到MaxCompute进行分布式执行处理，两种方式的对比详情请参见注意事项：请勿下载全量数据到本地并运行PyODPS。

**包支持限制**

DataWorks的PyODPS节点缺少**matplotlib**等包，如下功能可能受限： DataFrame自定义函数需要提交到MaxCompute执行。由于Python沙箱限制，第三方库只支持所有的纯粹Python库以及Numpy，因此不能直接使用 Pandas。 DataWorks中执行的非自定义函数代码可以使用平台预装的Numpy和Pandas。不支持其他带有二进制代码的三方包。 DataWorks的PyODPS节点不支持Python的**atexit**包，请使用**try-finally**结构实现相关功能。

**读取数据记录数限制**

DataWorks的PyODPS节点中，**options.tunnel.use_instance_tunnel**默认设置为False，即默认情况下，最多读取一万条数据记录。如果需要读取更多数据记录，需全局开启**instance tunnel**，即需要手动将**options.tunnel.use_instance_tunnel**设置为True。

**版本限制**

DataWorks从企业版V3.14开始支持Python 3节点。

**平台限制**

**主要流程**

1. 创建PyODPS节点。
您可以进入DataWorks的**数据开发**页面创建PyODPS节点。PyODPS节点分为PyODPS 2和PyODPS 3两种：
2. 开发PyODPS任务代码。
创建完成后，您可参考下文内容进行简单示例的操作学习，了解PyODPS的主要能力维度。 ODPS入口执行SQL 获取调度参数设置运行参数hints
3. 进行调度配置，完成后保存、提交、发布节点，后续即可周期性运行任务。

**ODPS入口**

| DataWorks的PyODPS节点中，将会包含一个全局变量 | odps | 或者 | o | ，即为ODPS入口。您不需要手动定义ODPS入口。命令示例如下。 |
|---|---|---|---|---|
| #查看表pyodps_iris是否存在 print(o.exist_table('pyodps_iris')) |  |  |  |  |

返回 `True` ，表示表存在。

**执行SQL**

**通用能力**

在PyODPS节点中运行SQL命令：例如使用**execute_sql()/run_sql()**来执行SQL命令，当前主要支持运行DDL、DML类型的SQL命令。

**说明**

可以执行的SQL语句并非都可以通过入口对象的 `execute_sql()` 和 `run_sql()` 方法执行。在调用非DDL或非DML语句时，请使用其他方法。例如，调用 GRANT或REVOKE语句时，请使用 `run_security_query` 方法；调用API命令时，请使用 `run_xflow` 或 `execute_xflow` 方法。 在PyODPS节点中读取SQL运行结果：例如使用**open_reader()**来读取SQL命令运行结果。

**注意事项：数据记录数量限制**

DataWorks上默认没有开启**instance tunnel**，即**instance.open_reader**默认使用Result接口（存在 `limit` 限制，最多读取一万条数据记录）。如果您需要全局关闭 `limit` 限制

| 您可以通过下列语句在全局范围内打开Instance Tunnel并关闭 | limit | 限制。 |
|---|---|---|
| options.tunnel.use_instance_tunnel = True options.tunnel.limit_instance_tunnel = False # 关闭limit限制，读取全部数据。 with instance.open_reader() as reader: # 通过Instance Tunnel可读取全部数据。 # 您可以通过reader.count获取记录数。 |  |  |

仅本次运行关闭 `limit` 限制您也可以通过在**open_reader**上添加 `tunnel=True` ，实现仅对本次**open_reader**开启**instance tunnel**。同时，您还可以添加 `limit=False` ，实现仅对本次关闭 `limit` 限制。

**重要**

```
with instance.open_reader(tunnel=True, limit=False) as reader:
```

# 本次`open_reader`使用`Instance Tunnel`接口，且能读取全部数据。
执行

| 在DataWorks的环境里，DataFrame的执行需要显式调用立即执行的方法（如 | execute | 、 | persist | 等）。示例代码如下。 |
|---|---|---|---|---|
| # 调用立即执行的方法，处理每条Record，打印出表pyodps_iris中iris.sepalwidth小于3的所有数据。 from odps.df import DataFrame iris = DataFrame(o.get_table('pyodps_iris')) for record in iris[iris.sepalwidth < 3].execute(): print(record) |  |  |  |  |

打印详细信息在DataWorks上默认打开 `options.verbose` 选项，即默认情况下，DataWorks的PyODPS节点运行过程会打印Logview等详细过程。您可以手动设置此选项， 指定运行过程是否会打印Logview等详细过程。

**获取调度参数**

使用DataWorks的PyODPS节点开发任务代码时，您也可以使用调度参数，例如，需要通过调度参数获取任务运行的业务日期等场景。PyODPS节点与DataWorks中的SQL节点在调度参数的定义参数操作方面一致，但是在代码中的引用方式不同。 SQL节点会在代码中直接使用**${param_name}**这样的字符串。 为了避免影响代码，PyODPS节点在执行代码前，在全局变量中增加了一个名为 `args` 的dict，代码中使用**args[param_name]**的方式获取调度参数取值，而非在代码中替换**${param_name}**。 例如，在节点的**调度配置** > **参数**中设置了调度参数 ds=${yyyymmdd} ，则可以通过以下方式在代码中获取该参数。

| 获取参数 | ds | 的取值。 |
|---|---|---|
| print('ds=' + args['ds']) #返回ds的时间，如ds=20161116 |  |  |

| 获取名为 | ds=${yyyymmdd} | 的分区的表数据。 |
|---|---|---|
| o.get_table('table_name').get_partition('ds=' + args['ds']) #获取ds分区下表table_name的数据 |  |  |

**设置运行参数hints**

| 运行任务时如果需要设置运行时参数，可以通过设置 | hints | 参数来实现，参数类型是dict。 |
|---|---|---|
| o.execute_sql('select * from pyodps_iris', hints={'odps.sql.mapper.split.size': 16}) |  |  |

您也可以对全局设置sql.setting，设置后后续每次运行时都会添加相关的运行时参数。

```python
from odps import options options.sql.settings = {'odps.sql.mapper.split.size': 16}
```

`o.execute_sql('select * from pyodps_iris') #`会根据全局配置添加`hints`

**使用三方包**

DataWorks节点预装了以下三方包，版本列表如下：

| 包名 | Python 2节点版本 | Python 3节点版本 |
|---|---|---|
| requests | 2.11.1 | 2.26.0 |
| numpy | 1.16.6 | 1.18.1 |
| pandas | 0.24.2 | 1.0.5 |
| scipy | 0.19.0 | 1.3.0 |
| scikitlearn _ | 0.18.1 | 0.22.1 |
| pyarrow | 0.16.0 | 2.0.0 |
| lz4 | 2.1.4 | 3.1.10 |
| zstandard | 0.14.1 | 0.17.0 |

如果您需要使用上面列表中不存在的包，DataWorks节点提供了 `load_resource_package` 方法，支持从MaxCompute资源下载三方包。使用 `pyodps-pack` 打包后，可以直接使用 `load_resource_package` 方法加载三方包，之后就可以导入包中的内容。关于 `pyodps-pack` 的使用方法请参见PyODPS制作第三方

**说明**

如果为Python 2节点打包，请在打包时为 `pyodps-pack` 增加 `--dwpy27` 参数。 示例：
1. 使用以下命令打包ipaddress。
2. 上传并提交 `ipaddress-bundle.tar.gz` 为资源后，可以在PyODPS 3节点中按照下面的方法使用ipaddress包。

```java
load_resource_package("ipaddress-bundle.tar.gz") import ipaddress
```

DataWorks限制下载的包总大小为100 MB。如果您需要跳过预装包的打包，可以在打包时使用 `pyodps-pack` 提供的 `--exclude` 参数。例如：下面打包方法排除了DataWork环境中存在的numpy包和pandas包。

```
pyodps-pack -o bundle.tar.gz --exclude numpy --exclude pandas <your_package>
```

**使用其他账号**

某些场景下您可能希望使用其他账号（而非平台提供的账号）访问MaxCompute。此时，可以使用ODPS入口对象的 `as_account` 方法创建一个使用新账号的入口对

| 象，该对象与系统默认提供的 | o | 实例彼此独立。 |
|---|---|---|
| 重要 as_account 方法从PyODPS 0.11.3版本开始支持。如果您的DataWorks未部署该版本，则无法使用 as_account 方法。 |  |  |

**主要流程**

1. 为其他用户授权项目相关权限，详情请参见附录：为其他用户授权。

| 在PyODPS节点中使用 | as_account | 方法切换账号，创建新的入口对象。 |
|---|---|---|
| import os # 确保 ALIBABA_CLOUD_ACCESS_KEY_ID 环境变量设置为 Access Key ID， # ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为 Access Key Secret， # 不建议直接使用 Access Key ID / Access Key Secret 字符串 new_odps = o.as_account( os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET') ) |  |  |

3. 检查账号切换结果。
查询当前用户信息：在要执行的代码中增加以下语句，如果运行结果中打印出的用户信息为您所传入的其他用户的UID，则表示您是使用其他账号访问的 MaxCompute。

```python
print(od.get_project().current_user)
```

**使用示例**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 创建ODPS SQL节点完成授权。详情请参见附录：为其他用户授权。
3. 创建PyODPS节点完成切换用户操作，代码示例如下。

```java
from odps import ODPS import os import sys reload(sys)
```

#修改系统默认编码。

```
sys.setdefaultencoding('utf8')
```

# 确保 `ALIBABA_CLOUD_ACCESS_KEY_ID` 环境变量设置为用户 `Access Key ID`，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 `Access Key Secret`，
# 不建议直接使用 `Access Key ID / Access Key Secret` 字符串

```
os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'] = '<accesskey id>' os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'] = '<accesskey secret>' od = o.as_account(os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
         os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
```

)
#使用条件方式输出。

```
with od.execute_sql('select * from pyodps_iris WHERE sepallength > 5 ').open_reader() as reader4:
    print reader4.raw
    for record in reader4:
        print record["sepallength"],record["sepalwidth"],record["petallength"],record["petalwidth"],record["name"]
```

#输出当前用户的`UID`

```python
print(od.get_project().current_user)
```

4. 运行并查看结果。

```
"sepallength","sepalwidth","petallength","petalwidth","name" 5.4,3.9,1.7,0.4,"Iris-setosa" 5.4,3.7,1.5,0.2,"Iris-setosa" 5.8,4.0,1.2,0.2,"Iris-setosa" 5.7,4.4,1.5,0.4,"Iris-setosa" 5.4,3.9,1.3,0.4,"Iris-setosa" 5.1,3.5,1.4,0.3,"Iris-setosa" 5.7,3.8,1.7,0.3,"Iris-setosa" 5.1,3.8,1.5,0.3,"Iris-setosa" 5.4,3.4,1.7,0.2,"Iris-setosa" 5.1,3.7,1.5,0.4,"Iris-setosa" 5.1,3.3,1.7,0.5,"Iris-setosa" 5.2,3.5,1.5,0.2,"Iris-setosa" 5.2,3.4,1.4,0.2,"Iris-setosa" 5.4,3.4,1.5,0.4,"Iris-setosa" 5.2,4.1,1.5,0.1,"Iris-setosa" 5.5,4.2,1.4,0.2,"Iris-setosa" 5.5,3.5,1.3,0.2,"Iris-setosa" 5.1,3.4,1.5,0.2,"Iris-setosa" 5.1,3.8,1.9,0.4,"Iris-setosa" 5.1,3.8,1.6,0.2,"Iris-setosa" 5.3,3.7,1.5,0.2,"Iris-setosa" 7.0,3.2,4.7,1.4,"Iris-versicolor" 6.4,3.2,4.5,1.5,"Iris-versicolor" 6.9,3.1,4.9,1.5,"Iris-versicolor" 5.5,2.3,4.0,1.3,"Iris-versicolor" 6.5,2.8,4.6,1.5,"Iris-versicolor" 5.7,2.8,4.5,1.3,"Iris-versicolor" 6.3,3.3,4.7,1.6,"Iris-versicolor" 6.6,2.9,4.6,1.3,"Iris-versicolor" 5.2,2.7,3.9,1.4,"Iris-versicolor" 5.9,3.0,4.2,1.5,"Iris-versicolor" 6.0,2.2,4.0,1.0,"Iris-versicolor" 6.1,2.9,4.7,1.4,"Iris-versicolor" 5.6,2.9,3.6,1.3,"Iris-versicolor" 6.7,3.1,4.4,1.4,"Iris-versicolor" 5.6,3.0,4.5,1.5,"Iris-versicolor" 5.8,2.7,4.1,1.0,"Iris-versicolor" 6.2,2.2,4.5,1.5,"Iris-versicolor" 5.6,2.5,3.9,1.1,"Iris-versicolor" 5.9,3.2,4.8,1.8,"Iris-versicolor" 6.1,2.8,4.0,1.3,"Iris-versicolor" 6.3,2.5,4.9,1.5,"Iris-versicolor" 6.1,2.8,4.7,1.2,"Iris-versicolor" 6.4,2.9,4.3,1.3,"Iris-versicolor" 6.6,3.0,4.4,1.4,"Iris-versicolor" 6.8,2.8,4.8,1.4,"Iris-versicolor" 6.7,3.0,5.0,1.7,"Iris-versicolor" 6.0,2.9,4.5,1.5,"Iris-versicolor" 5.7,2.6,3.5,1.0,"Iris-versicolor" 5.5,2.4,3.8,1.1,"Iris-versicolor" 5.5,2.4,3.7,1.0,"Iris-versicolor" 5.8,2.7,3.9,1.2,"Iris-versicolor" 6.0,2.7,5.1,1.6,"Iris-versicolor" 5.4,3.0,4.5,1.5,"Iris-versicolor" 60344516"Irisversicolor"
```

```
6.0,3.4,4.5,1.6,"Iris-versicolor" 6.7,3.1,4.7,1.5,"Iris-versicolor" 6.3,2.3,4.4,1.3,"Iris-versicolor" 5.6,3.0,4.1,1.3,"Iris-versicolor" 5.5,2.5,4.0,1.3,"Iris-versicolor" 5.5,2.6,4.4,1.2,"Iris-versicolor" 6.1,3.0,4.6,1.4,"Iris-versicolor" 5.8,2.6,4.0,1.2,"Iris-versicolor" 5.6,2.7,4.2,1.3,"Iris-versicolor" 5.7,3.0,4.2,1.2,"Iris-versicolor" 5.7,2.9,4.2,1.3,"Iris-versicolor" 6.2,2.9,4.3,1.3,"Iris-versicolor" 5.1,2.5,3.0,1.1,"Iris-versicolor" 5.7,2.8,4.1,1.3,"Iris-versicolor" 6.3,3.3,6.0,2.5,"Iris-virginica" 5.8,2.7,5.1,1.9,"Iris-virginica" 7.1,3.0,5.9,2.1,"Iris-virginica" 6.3,2.9,5.6,1.8,"Iris-virginica" 6.5,3.0,5.8,2.2,"Iris-virginica" 7.6,3.0,6.6,2.1,"Iris-virginica" 7.3,2.9,6.3,1.8,"Iris-virginica" 6.7,2.5,5.8,1.8,"Iris-virginica" 7.2,3.6,6.1,2.5,"Iris-virginica" 6.5,3.2,5.1,2.0,"Iris-virginica" 6.4,2.7,5.3,1.9,"Iris-virginica" 6.8,3.0,5.5,2.1,"Iris-virginica" 5.7,2.5,5.0,2.0,"Iris-virginica" 5.8,2.8,5.1,2.4,"Iris-virginica" 6.4,3.2,5.3,2.3,"Iris-virginica" 6.5,3.0,5.5,1.8,"Iris-virginica" 7.7,3.8,6.7,2.2,"Iris-virginica" 7.7,2.6,6.9,2.3,"Iris-virginica" 6.0,2.2,5.0,1.5,"Iris-virginica" 6.9,3.2,5.7,2.3,"Iris-virginica" 5.6,2.8,4.9,2.0,"Iris-virginica" 7.7,2.8,6.7,2.0,"Iris-virginica" 6.3,2.7,4.9,1.8,"Iris-virginica" 6.7,3.3,5.7,2.1,"Iris-virginica" 7.2,3.2,6.0,1.8,"Iris-virginica" 6.2,2.8,4.8,1.8,"Iris-virginica" 6.1,3.0,4.9,1.8,"Iris-virginica" 6.4,2.8,5.6,2.1,"Iris-virginica" 7.2,3.0,5.8,1.6,"Iris-virginica" 7.4,2.8,6.1,1.9,"Iris-virginica" 7.9,3.8,6.4,2.0,"Iris-virginica" 6.4,2.8,5.6,2.2,"Iris-virginica" 6.3,2.8,5.1,1.5,"Iris-virginica" 6.1,2.6,5.6,1.4,"Iris-virginica" 7.7,3.0,6.1,2.3,"Iris-virginica" 6.3,3.4,5.6,2.4,"Iris-virginica" 6.4,3.1,5.5,1.8,"Iris-virginica" 6.0,3.0,4.8,1.8,"Iris-virginica" 6.9,3.1,5.4,2.1,"Iris-virginica" 6.7,3.1,5.6,2.4,"Iris-virginica" 6.9,3.1,5.1,2.3,"Iris-virginica" 5.8,2.7,5.1,1.9,"Iris-virginica" 6.8,3.2,5.9,2.3,"Iris-virginica" 6.7,3.3,5.7,2.5,"Iris-virginica" 6.7,3.0,5.2,2.3,"Iris-virginica" 6.3,2.5,5.0,1.9,"Iris-virginica" 6.5,3.0,5.2,2.0,"Iris-virginica" 6.2,3.4,5.4,2.3,"Iris-virginica" 5.9,3.0,5.1,1.8,"Iris-virginica" 5.4 3.9 1.7 0.4 Iris-setosa 5.4 3.7 1.5 0.2 Iris-setosa 5.8 4.0 1.2 0.2 Iris-setosa 5.7 4.4 1.5 0.4 Iris-setosa 5.4 3.9 1.3 0.4 Iris-setosa 5.1 3.5 1.4 0.3 Iris-setosa 5.7 3.8 1.7 0.3 Iris-setosa 5.1 3.8 1.5 0.3 Iris-setosa 5.4 3.4 1.7 0.2 Iris-setosa 5.1 3.7 1.5 0.4 Iris-setosa 5.1 3.3 1.7 0.5 Iris-setosa 5.2 3.5 1.5 0.2 Iris-setosa 5.2 3.4 1.4 0.2 Iris-setosa 5.4 3.4 1.5 0.4 Iris-setosa 5.2 4.1 1.5 0.1 Iris-setosa 5.5 4.2 1.4 0.2 Iris-setosa 5.5 3.5 1.3 0.2 Iris-setosa 5.1 3.4 1.5 0.2 Iris-setosa 5.1 3.8 1.9 0.4 Iris-setosa 5.1 3.8 1.6 0.2 Iris-setosa 5.3 3.7 1.5 0.2 Iris-setosa
```

```
7.0 3.2 4.7 1.4 Iris-versicolor 6.4 3.2 4.5 1.5 Iris-versicolor 6.9 3.1 4.9 1.5 Iris-versicolor 5.5 2.3 4.0 1.3 Iris-versicolor 6.5 2.8 4.6 1.5 Iris-versicolor 5.7 2.8 4.5 1.3 Iris-versicolor 6.3 3.3 4.7 1.6 Iris-versicolor 6.6 2.9 4.6 1.3 Iris-versicolor 5.2 2.7 3.9 1.4 Iris-versicolor 5.9 3.0 4.2 1.5 Iris-versicolor 6.0 2.2 4.0 1.0 Iris-versicolor 6.1 2.9 4.7 1.4 Iris-versicolor 5.6 2.9 3.6 1.3 Iris-versicolor 6.7 3.1 4.4 1.4 Iris-versicolor 5.6 3.0 4.5 1.5 Iris-versicolor 5.8 2.7 4.1 1.0 Iris-versicolor 6.2 2.2 4.5 1.5 Iris-versicolor 5.6 2.5 3.9 1.1 Iris-versicolor 5.9 3.2 4.8 1.8 Iris-versicolor 6.1 2.8 4.0 1.3 Iris-versicolor 6.3 2.5 4.9 1.5 Iris-versicolor 6.1 2.8 4.7 1.2 Iris-versicolor 6.4 2.9 4.3 1.3 Iris-versicolor 6.6 3.0 4.4 1.4 Iris-versicolor 6.8 2.8 4.8 1.4 Iris-versicolor 6.7 3.0 5.0 1.7 Iris-versicolor 6.0 2.9 4.5 1.5 Iris-versicolor 5.7 2.6 3.5 1.0 Iris-versicolor 5.5 2.4 3.8 1.1 Iris-versicolor 5.5 2.4 3.7 1.0 Iris-versicolor 5.8 2.7 3.9 1.2 Iris-versicolor 6.0 2.7 5.1 1.6 Iris-versicolor 5.4 3.0 4.5 1.5 Iris-versicolor 6.0 3.4 4.5 1.6 Iris-versicolor 6.7 3.1 4.7 1.5 Iris-versicolor 6.3 2.3 4.4 1.3 Iris-versicolor 5.6 3.0 4.1 1.3 Iris-versicolor 5.5 2.5 4.0 1.3 Iris-versicolor 5.5 2.6 4.4 1.2 Iris-versicolor 6.1 3.0 4.6 1.4 Iris-versicolor 5.8 2.6 4.0 1.2 Iris-versicolor 5.6 2.7 4.2 1.3 Iris-versicolor 5.7 3.0 4.2 1.2 Iris-versicolor 5.7 2.9 4.2 1.3 Iris-versicolor 6.2 2.9 4.3 1.3 Iris-versicolor 5.1 2.5 3.0 1.1 Iris-versicolor 5.7 2.8 4.1 1.3 Iris-versicolor 6.3 3.3 6.0 2.5 Iris-virginica 5.8 2.7 5.1 1.9 Iris-virginica 7.1 3.0 5.9 2.1 Iris-virginica 6.3 2.9 5.6 1.8 Iris-virginica 6.5 3.0 5.8 2.2 Iris-virginica 7.6 3.0 6.6 2.1 Iris-virginica 7.3 2.9 6.3 1.8 Iris-virginica 6.7 2.5 5.8 1.8 Iris-virginica 7.2 3.6 6.1 2.5 Iris-virginica 6.5 3.2 5.1 2.0 Iris-virginica 6.4 2.7 5.3 1.9 Iris-virginica 6.8 3.0 5.5 2.1 Iris-virginica 5.7 2.5 5.0 2.0 Iris-virginica 5.8 2.8 5.1 2.4 Iris-virginica 6.4 3.2 5.3 2.3 Iris-virginica 6.5 3.0 5.5 1.8 Iris-virginica 7.7 3.8 6.7 2.2 Iris-virginica 7.7 2.6 6.9 2.3 Iris-virginica 6.0 2.2 5.0 1.5 Iris-virginica 6.9 3.2 5.7 2.3 Iris-virginica 5.6 2.8 4.9 2.0 Iris-virginica 7.7 2.8 6.7 2.0 Iris-virginica 6.3 2.7 4.9 1.8 Iris-virginica 6.7 3.3 5.7 2.1 Iris-virginica 7.2 3.2 6.0 1.8 Iris-virginica 6.2 2.8 4.8 1.8 Iris-virginica 6.1 3.0 4.9 1.8 Iris-virginica 6.4 2.8 5.6 2.1 Iris-virginica 7.2 3.0 5.8 1.6 Iris-virginica 7.4 2.8 6.1 1.9 Iris-virginica 7.9 3.8 6.4 2.0 Iris-virginica 6.4 2.8 5.6 2.2 Iris-virginica 6.3 2.8 5.1 1.5 Iris-virginica 6.1 2.6 5.6 1.4 Iris-virginica 7.7 3.0 6.1 2.3 Iris-virginica 6.3 3.4 5.6 2.4 Iris-virginica 64315518
```

i i ii

```xml
6.4 3.1 5.5 1.8 Iris-virginica 6.0 3.0 4.8 1.8 Iris-virginica 6.9 3.1 5.4 2.1 Iris-virginica 6.7 3.1 5.6 2.4 Iris-virginica 6.9 3.1 5.1 2.3 Iris-virginica 5.8 2.7 5.1 1.9 Iris-virginica 6.8 3.2 5.9 2.3 Iris-virginica 6.7 3.3 5.7 2.5 Iris-virginica 6.7 3.0 5.2 2.3 Iris-virginica 6.3 2.5 5.0 1.9 Iris-virginica 6.5 3.0 5.2 2.0 Iris-virginica 6.2 3.4 5.4 2.3 Iris-virginica 5.9 3.0 5.1 1.8 Iris-virginica <User 139xxxxxxxxxxxxx>
```

**问题诊断**

如果您的代码在执行过程中无响应且没有任何输出，您可以在代码头部增加以下注释，DataWorks每隔30秒将输出所有线程的堆栈：

```bash
# -*- dump_traceback: true -*-
```

**说明**

您可以直接使用Python代码查询当前的PyODPS版本，也可以在任意一个PyODPS任务的运行日志中查看。
# 输入如下代码

```java
import odps; print(odps.__version__)
```

# 返回结果示例

```
0.11.2.3
```

**附录：为其他用户授权**

在使用DataWorks时，如果您想要其他指定用户（非子用户）访问本账号下的项目、表等，需要在DataWorks中新建ODPS SQL节点并运行以下授权命令，其他权限详情请参见用户与权限。 `--`添加其他阿里云账号用户（项目级别）

```
ADD USER ALIYUN$<account_name>;
```

`--`授予项目的`CreateInstance`权限

```
GRANT CreateInstance ON project <project_name> TO USER ALIYUN$<account_name>;
```

`--`授予表的`desc`、`select`权限

```
GRANT DESCRIBE, SELECT ON TABLE <table_name> TO USER ALIYUN$<account_name>;
```

`--`查看授权结果

```
SHOW grants FOR ALIYUN$<account_name>;
```

授权结果示例：

**附录：示例数据**

您可参考PyODPS条件查询文档中的步骤1：创建表并导入数据在DataWorks中建好表pyodps_iris并写入数据，文档中的操作示例即以此表作为示例数据，为您演示基本操作。

### 通过本地环境使用PyODPS

#### 9.4.1. 安装PyODPS

PyODPS是MaxCompute的Python版本的SDK，提供对MaxCompute对象的基本操作及DataFrame框架，帮助您在MaxCompute上使用Python进行数据分析，支持在DataWorks或本地环境上使用。本文为您介绍在本地环境中安装使用PyODPS。

**前提条件**

安装PyODPS环境前，您可先查看下Python的版本，建议Python版本为3.6及以上版本，不建议使用2.7及以下版本。

**安装步骤**

1. 执行如下命令安装PyODPS。
2. 执行如下命令检查安装是否成功。若无返回值和报错信息表示安装成功。

```
python -c "from odps import ODPS"
```

3. 如果您使用的Python不是系统默认的Python版本，安装完PIP后，您可以执行如下命令进行Python版本切换。

```
/home/tops/bin/python3.7 -m pip install setuptools>=3.0
```

#/home/tops/bin/python3.7为安装的`python`路径

**后续步骤**

1. 建议您安装以下工具，提升Tunnel上传的速度：**greenlet 0.4.10**或以上版本。
2. 初始化ODPS入口。

```java
import os from odps import ODPS
```

# 确保 `ALIBABA_CLOUD_ACCESS_KEY_ID`环境变量设置为用户`Access Key ID`，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET环境变量设置为用户`Access Key Secret`，

```
o = ODPS(
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    project='your-default-project',
    endpoint='your-end-point',
```

) 其中： ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET：需将该环境变量设置为您的阿里云账号的AccessKey ID和 AccessKey Secret。

**说明**

不建议直接使用AccessKey ID和 AccessKey Secret字符串。 your-default-project和your-end-point：需替换为您设置的默认项目名称与Endpoint信息。 完成上述配置后，您就可以在本地环境中使用PyODPS，例如对于ODPS对象的基本操作 `list` 、 `get` 、 `exist` 、 `create` 、 `delete` 等，更多PyODPS的

**说明**

如无特殊说明，文档中的o对象即为ODPS对象。

#### 9.4.2. 在本地环境上使用PyODPS

PyODPS是阿里云开发的Python SDK，用于在本地环境上使用MaxCompute服务。本文将介绍如何在本地环境上使用PyODPS进行表操作、数据加载和运行SQL查询。

**前提条件**

1. 本地已安装python环境，且已安装PyODPS包，参考：安装PyODPS。
2. 准备数据集**pyodps_iris**。您可参考使用示例下载数据集、创建**pyodps_iris**表并写入数据，文档中的操作示例即以此表作为示例数据，为您演示基本操作。

**主要流程**

1. 打开Python编辑器，并创建一个Python文件。
2. 开发PyODPS任务代码。
创建完成后，您可参考下文内容进行简单示例的操作学习，了解PyODPS的主要能力维度。 创建ODPS入口执行SQL 设置运行参数hints
3. 本地运行python文件。

**创建ODPS入口**

您需要手动定义ODPS入口，代码示例如下。

```java
import os from odps import ODPS
```

# 确保 `ALIBABA_CLOUD_ACCESS_KEY_ID` 环境变量设置为用户 `Access Key ID`，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 `Access Key Secret`，

```
o = ODPS(
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    project='your-default-project',
    endpoint='your-end-point',
```

)

**执行SQL**

您可以在PyODPS节点中使用传统模式或加速查询模式（MCQA）执行SQL命令，当前主要支持运行DDL、DML类型的SQL命令。与传统模式相比，加速查询模式 （MCQA）会将作业的运行结果写入临时缓存中。当您后续执行相同的查询作业时，MaxCompute会优先返回缓存中的结果，加快执行速度，您可根据需要选择相应的模式执行。

**说明**

可以执行的SQL语句并非都可以通过入口对象的 `execute_sql()` 和 `run_sql()` 等方法执行。在调用非DDL或非DML语句时，请使用其他方法。例如，调用创建表语句时，请使用 `create_table` 方法；调用API命令时，请使用 `run_xflow` 或 `execute_xflow` 方法。 使用传统模式执行SQL命令。 您可以使用**execute_sql()/run_sql()**来执行SQL命令，示例如下：

| 使用 | create_table | 方法创建一个新的表。 |
|---|---|---|
| o.create_table('my_t', 'num bigint, id string', if_not_exists=True) |  |  |

| 使用 | execute_sql | 方法执行SQL查询。 |
|---|---|---|
| result = o.execute_sql('SELECT * FROM pyodps_iris LIMIT 3') with result.open_reader() as reader: for record in reader: print(record) |  |  |

使用加速查询模式（MCQA）执行SQL命令。 MCQA是MaxCompute提供的查询加速功能，支持使用独立资源池对中小规模数据进行加速。PyODPS从V0.11.4.1版本开始支持以下列方式通过MCQA执行 SQL。
**execute_sql_interactive()**：通过MCQA执行SQL并返回MCQA Instance。如果MCQA无法执行相应的SQL，会自动回退到传统模式。此时，函数返回的
Instance为回退后的Instance。

```
o.execute_sql_interactive('SELECT * FROM dual')
```

| 如果不希望回退，可以指定参数 fallback=False 。也可以指定为回退策略（或回退策略的组合，使用逗号分隔的字符串）。可用的策略名如下，默认策略为 unsupported,upgrading,noresource,timeout 。 |  |
|---|---|
| 回退策略 | 描述 |
| generic | 指定时，表示发生未知错误时回退到传统模式。 |
| noresource | 指定时，表示发生资源不足问题时回退到传统模式。 |
| upgrading | 指定时，表示升级期间回退到传统模式。 |
| timeout | 指定时，表示执行超时时回退到传统模式。 |
| unsupported | 指定时，表示遇到MCQA不支持的场景时回退到传统模式。 |

例如，下述代码表示通过MCQA执行SQL，如果遇到不支持MCQA的场景或资源不足问题，回退到传统模式。

```
 o.execute_sql_interactive('SELECT * FROM dual', fallback="noresource,unsupported")
```

您可以使用**open_reader()**来读取SQL命令运行结果。具体操作请参见读取SQL执行结果。 执行

| DataFrame的执行需要显式调用立即执行的方法（如 | execute | 、 | persist | 等）。示例代码如下。 |
|---|---|---|---|---|
| # 调用立即执行的方法，处理每条Record，打印出表pyodps_iris中iris.sepalwidth小于3的所有数据。 from odps.df import DataFrame iris = DataFrame(o.get_table('pyodps_iris')) for record in iris[iris.sepalwidth < 3].execute(): print(record) |  |  |  |  |

打印详细信息

| 默认情况下，本地环境的PyODPS节点运行过程不会打印Logview等详细过程。您可以手动设置 | options.verbose | 选项，开启打印Logview等详细过程。 |
|---|---|---|
| from odps import options options.verbose = True |  |  |

**设置运行参数hints**

| 运行任务时如果需要设置运行时参数，可以通过设置 | hints | 参数来实现，参数类型是dict。 |
|---|---|---|
| o.execute_sql('SELECT * FROM pyodps_iris', hints={'odps.sql.mapper.split.size': 16}) |  |  |

您也可以对全局设置sql.setting，设置后后续每次运行时都会添加相关的运行时参数。

```python
from odps import options options.sql.settings = {'odps.sql.mapper.split.size': 16}
```

# 会根据全局配置添加`hints`

**完整示例**

1. 本地创建 `test-pyodps-local.py` 文件。
2. 写入示例代码。

```java
import os from odps import ODPS
```

# 确保 `ALIBABA_CLOUD_ACCESS_KEY_ID` 环境变量设置为用户 `Access Key ID`，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 `Access Key Secret`，

```
o = ODPS(
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    project='your-default-project',
    endpoint='your-end-point',
```

)
# 以直接指定字段名以及字段类型的方式创建非分区表`my_new_table`。

```
table = o.create_table('my_new_table', 'num bigint, id string', if_not_exists=True)
```

# 向非分区表`my_new_table`中插入数据。

```
records = [[111, 'aaa'],
           [222, 'bbb'],
           [333, 'ccc'],
```

`[444, '`中文`']]`

```
o.write_table(table, records)
```

# 读取非分区表`my_new_table`中的数据。

```python
for record in o.read_table(table):
    print(record[0], record[1])
result = o.execute_sql('SELECT * FROM pyodps_iris LIMIT 3;', hints={'odps.sql.allow.fullscan': 'true'})
```

# 删除表以清除资源。

```
table.drop()
```

# 读取`SQL`执行结果。

```python
with result.open_reader() as reader:
    for record in reader:
        print(record[0], record[1])
```

3. 运行python代码。
运行结果：

```
111 aaa 222 bbb 333 ccc
```

`444` 中文

```
4.9 3.0 4.7 3.2 4.6 3.1
```

### 基本操作

#### 9.5.1. 基本操作概述

PyODPS提供了针对ODPS对象的基本操作接口，让您能够以符合Python编程习惯的方式高效操作MaxCompute。

**基本操作说明**

#### 项目空间

#### 任务实例

表

#### SQL

资源函数基本操作命令中涉及到的方法详细说明请参见Definitions。

#### 9.5.2. 项目空间

**前提条件：准备运行环境**

PyODPS支持在DataWorks的PyODPS节点或本地PC环境中运行，运行前您需先选择运行工具并准备好运行环境。 使用DataWorks：创建好PyODPS 2节点或PyODPS 3节点，详情请参见通过DataWorks使用PyODPS。

**获取项目空间**

| 使用MaxCompute入口对象的 | get_project() | 方法获取项目空间。 |
|---|---|---|
| project = o.get_project('project_name') # 指定项目名称时，获取特定项目。 project = o.get_project() # 不指定项目名称时，获取当前项目。 |  |  |

该方法需要提供**project_name**即项目空间名称。指定项目空间名称时，则获取特定项目；如果不指定项目空间名称，则获取当前项目空间名称。

**验证项目空间是否存在**

| 使用 | o.exist_project() | 方法，检验某个项目空间是否存在。 |
|---|---|---|
| print(o.exist_project('doc_test')) |  |  |

返回 `True` 则表示项目空间doc_test存在。

**9.5.3. 表**

本文提供PyODPS对MaxCompute表的全生命周期操作指南，涵盖Schema定义、表创建与删除、数据读写（含Tunnel通道）、分区管理及DataFrame转换等核心功能，方便您高效地在Python环境中完成MaxCompute数据的开发、维护与分析任务。

**背景信息**

| 操作 | 说明 |
|---|---|
| 基本操作 | 列出项目空间下的所有表、判断表是否存在、获取表等基本操作。 |
| 创建表的Schema | 使用PyODPS创建表的Schema。 |
| 创建表 | 使用PyODPS创建表。 |
| 同步表更新 | 使用PyODPS同步表更新。 |
| 写入表数据 | 使用PyODPS向表中写入数据。 |

| 向表中插入一行记录 | 使用PyODPS向表中插入一行记录。 |
|---|---|
| 获取表数据 | 使用PyODPS获取表中数据。 |
| 删除表 | 使用PyODPS删除表。 |
| 转换表为DataFrame | 使用PyODPS转换表为DataFrame。 |
| 表分区 | 使用PyODPS判断是否为分区表、遍历表全部分区、判断分区是否存在、创建分区等。 |
| 数据上传下载通道 | 使用PyODPS操作Tunnel向MaxCompute中上传或者下载数据。 |

**前提条件：准备运行环境**

PyODPS支持在DataWorks的PyODPS节点或本地PC环境中运行，运行前您需先选择运行工具并准备好运行环境。 使用DataWorks：创建好PyODPS 2节点或PyODPS 3节点，详情请参见通过DataWorks使用PyODPS。

### 基本操作

**当前项目内的表操作**

列出项目空间下的所有表：

| o.list_tables() | 方法可以列出项目空间下的所有表。 |
|---|---|
| # 列出项目空间下的所有表。 for table in o.list_tables(): print(table) |  |

判断表是否存在：

| o.exist_table() | 方法可以判断表是否存在。 |
|---|---|
| print(o.exist_table('pyodps_iris')) # 返回True表示表pyodps_iris存在。 |  |

获取表： 入口对象的 `o.get_table()` 方法可以获取表。 获取表的schema信息。 返回值示例如下。

```
odps.Schema {
  sepallength           double      # 片长度(cm)
  sepalwidth            double      # 片宽度(cm)
  petallength           double      # 瓣长度(cm)
  petalwidth            double      # 瓣宽度(cm)
  name                  string      # 种类
}
```

获取表列信息。 `print(t.schema.columns) #` 获取表`pyodps_iris`的`schema`中的列信息返回值示例如下。

```xml
[<column sepallength, type double>,
 <column sepalwidth, type double>,
 <column petallength, type double>,
 <column petalwidth, type double>,
 <column name, type string>]
```

获取表的某个列信息。

```python
print(t.schema['sepallength']) # 获取表pyodps_iris的sepallength列信息
```

返回值示例如下。

```xml
<column sepallength, type double>
```

获取表的某个列的备注信息。

```python
print(t.schema['sepallength'].comment) # 获取表pyodps_iris的sepallength列的备注信息
```

返回示例如下。 片长度`(cm)` 获取表的生命周期。 返回值示例如下。 `-1` 获取表的创建时间。 获取表是否是虚拟视图。 `print(t.is_virtual_view) #` 获取表`pyodps_iris`是否是虚拟视图，返回`False`，表示不是。 与上述示例类似，您也可以通过 `t.size` 、 `t.comment` 来获取表的大小、表备注等信息。

**跨项目的表操作**

| 您可以通过 | project | 参数，跨项目获取表。 |
|---|---|---|
| t = o.get_table('table_name', project='other_project') |  |  |

其中other_project为所跨的项目，table_name为跨项目获取的表名称。

**创建表的Schema**

初始化方法有如下两种： 通过表的列以及可选的分区进行初始化。

```
from odps.models import Schema, Column, Partition columns = [
    Column(name='num', type='bigint', comment='the column'),
    Column(name='num2', type='double', comment='the column2'),
```

]

```
partitions = [Partition(name='pt', type='string', comment='the partition')] schema = Schema(columns=columns, partitions=partitions)
```

初始化后，您可获取字段信息、分区信息等。 获取所有字段信息。

```python
print(schema.columns)
```

返回示例如下。

```xml
[<column num, type bigint>,
 <column num2, type double>,
 <partition pt, type string>]
```

获取分区字段。

```python
print(schema.partitions)
```

返回示例如下。

```
[<partition pt, type string>]
```

获取非分区字段名称。

```python
print(schema.names)
```

返回示例如下。

```json
['num', 'num2']
```

获取非分区字段类型。

```python
print(schema.types)
```

返回示例如下。

```
[bigint, double]
```

使用 `Schema.from_lists()` 方法。该方法更容易调用，但无法直接设置列和分区的注释。

```python
from odps.models import Schema schema = Schema.from_lists(['num', 'num2'], ['bigint', 'double'], ['pt'], ['string']) print(schema.columns)
```

返回值示例如下。

```xml
[<column num, type bigint>,
 <column num2, type double>,
 <partition pt, type string>]
```

#### 创建表

您可以使用 `o.create_table()` 方法创建表，使用方式有两种：使用表Schema方式、使用字段名和字段类型方式。同时创建表时表字段的数据类型有一定的限制条件，详情如下。

**使用表Schema创建表**

使用表Schema创建表时，您需要先创建表的Schema，然后通过Schema创建表。
# 创建表的`schema`

```
from odps.models import Schema schema = Schema.from_lists(['num', 'num2'], ['bigint', 'double'], ['pt'], ['string'])
```

# 通过`schema`创建表

```
table = o.create_table('my_new_table', schema)
```

# 只有不存在表时，才创建表。

```
table = o.create_table('my_new_table', schema, if_not_exists=True)
```

# 设置生命周期。

```
table = o.create_table('my_new_table', schema, lifecycle=7)
```

表创建完成后，您可以通过 `print(o.exist_table('my_new_table'))` 验证表是否创建成功，返回 `True` 表示表创建成功。

**使用字段名及字段类型创建表**

# 创建分区表`my_new_table`，可传入（表字段列表，分区字段列表）。

```
table = o.create_table('my_new_table', ('num bigint, num2 double', 'pt string'), if_not_exists=True)
```

# 创建非分区表`my_new_table02`。

```
table = o.create_table('my_new_table02', 'num bigint, num2 double', if_not_exists=True)
```

表创建完成后，您可以通过 `print(o.exist_table('my_new_table'))` 验证表是否创建成功，返回 `True` 表示表创建成功。

**使用字段名及字段类型创建表：新数据类型**

| 您需要创建TINYINT和STRUCT等新数据类型字段的表，可以打开 | options.sql.use_odps2_extension = True | 开关，示例如下。 |
|---|---|---|
| from odps import options options.sql.use_odps2_extension = True table = o.create_table('my_new_table', 'cat smallint, content struct<title:varchar(100), body:string>') |  |  |

**同步表更新**

| 当一个表被其他程序更新，例如改变了Schema，可以调用 | reload() | 方法同步表的更新。 |
|---|---|---|
| # 表schema变更 from odps.models import Schema schema = Schema.from_lists(['num', 'num2'], ['bigint', 'double'], ['pt'], ['string']) # 通过reload()同步表更新 table = o.create_table('my_new_table', schema) table.reload() |  |  |

**写入表数据**

| 使用入口对象的 | write_table() | 方法写入数据。 |
|---|---|---|
| 重要对于分区表，如果分区不存在，可以使用create partition参数指定创建分区。 _ |  |  |

```
records = [[111, 1.0], # 此处可以是list。
          [222, 2.0],
          [333, 3.0],
          [444, 4.0]]
o.write_table('my_new_table', records, partition='pt=test', create_partition=True) # 创建pt=test分区并写入数据
```

**说明**

每次调用 `write_table()` 方法，MaxCompute都会在服务端生成一个文件。该操作耗时较长，同时文件过多会降低后续的查询效率。因此，建议您在使用此方法时，一次性写入多组数据，或者传入一个生成器对象。 调用 `write_table()` 方法向表中写入数据时会追加到原有数据中。PyODPS不提供覆盖数据的选项，如果需要覆盖数据，请手动清除原有数据。对于非分区表，需要调用 `table.truncate()` 方法；对于分区表，需要删除分区后再建立新的分区。

| 对表对象调用 | open_writer() | 方法写入数据。 |
|---|---|---|
| t = o.get_table('my_new_table') with t.open_writer(partition='pt=test02', create_partition=True) as writer: # 创建pt=test02分区并写入数据 records = [[1, 1.0], # 此处可以是List。 [2, 2.0], [3, 3.0], [4, 4.0]] writer.write(records) # 这里Records可以是可迭代对象。 |  |  |

如果是多级分区表，写入示例如下。

```
t = o.get_table('test_table') with t.open_writer(partition='pt1=test1,pt2=test2') as writer: # 多级分区写法。
    records = [t.new_record([111, 'aaa', True]),   # 也可以是Record对象。
               t.new_record([222, 'bbb', False]),
               t.new_record([333, 'ccc', True]),
               t.new_record([444, '中文', False])]
    writer.write(records)
```

使用多进程并行写数据。 每个进程写数据时共享同一个Session_ID，但是有不同的Block_ID。每个Block对应服务端的一个文件。主进程执行Commit，完成数据上传。

```java
import random from multiprocessing import Pool def write_records(tunnel, table, session_id, block_id):
```

# 对使用指定的`ID`创建`Session`。

```
    local_session = tunnel.create_upload_session(table.name, upload_id=session_id)
```

# 创建`Writer`时指定`Block_ID`。

```
    with local_session.open_record_writer(block_id) as writer:
        for i in range(5):
```

# 生成数据并写入对应`Block`。

```
            record = table.new_record([random.randint(1, 100), random.random()])
            writer.write(record)
if __name__ == '__main__':
    N_WORKERS = 3
    table = o.create_table('my_new_table', 'num bigint, num2 double', if_not_exists=True)
    upload_session = tunnel.create_upload_session(table.name)
```

# 每个进程使用同一个`Session_ID`。

```
    pool = Pool(processes=N_WORKERS)
    futures = []
    block_ids = []
    for i in range(N_WORKERS):
        futures.append(pool.apply_async(write_records, (tunnel, table, session_id, i)))
        block_ids.append(i)
    [f.get() for f in futures]
```

# 最后执行`Commit`，并指定所有`Block`。

**向表中插入一行记录**

Record表示表的一行记录，对表对象调用 `new_record()` 方法即可创建一个新的Record。

```
t = o.get_table('test_table1')
```

`r = t.new_record(['val0', 'val1', 'val2', 'val3']) #` 值的个数必须等于表`Schema`的字段数。 `r2 = t.new_record() #` 可以不传入值。 `r2[0] = 'val0' #` 通过偏移设置值。 `r2['field1'] = 'val1' #` 通过字段名设置值。 `r2.field1 = 'val1' #` 通过属性设置值。 `print(r2[0]) #` 取第0个位置的值。 `print(r2['field1']) #` 通过字段取值。 `print(r2.field1) #` 通过属性取值。 `print(r2[0: 3]) #` 切片操作。 `print(r2[0, 2, 3]) #` 取多个位置的值。 `print(r2['field1', 'field2']) #` 通过多个字段取值。

**获取表数据**

获取表数据的方法有多种，常用方法如下：

| 使用入口对象的 | read_table() | 方法。 |
|---|---|---|
| # 处理一条记录。 for record in o.read_table('my_new_table', partition='pt=test'): print(record) |  |  |

| 如果您仅需要查看每个表最开始的小于1万条数据，可以对表对象调用 | head() | 方法。 |
|---|---|---|
| t = o.get_table('my_new_table') # 处理每个Record对象。 for record in t.head(3): print(record) |  |  |

调用 `open_reader()` 方法读取数据。 使用 `with` 表达式的写法如下。

```
t = o.get_table('my_new_table') with t.open_reader(partition='pt=test') as reader:
    count = reader.count
```

`for record in reader[5:10]: #` 可以执行多次，直到将`Count`数量的`Record`读完，此处可以改造成并行操作。 `print(record) #` 处理一条记录，例如打印记录本身

| 不使用 | with | 表达式的写法如下。 |
|---|---|---|
| t = o.get_table('my_new_table') reader = t.open_reader(partition='pt=test') count = reader.count for record in reader[5:10]: # 可以执行多次，直到将Count数量的Record读完，此处可以改造成并行操作。 print(record) # 处理一条记录，例如打印记录本身 |  |  |

#### 删除表

| 使用 | delete_table() | 方法删除已经存在的表。 |
|---|---|---|
| o.delete_table('my_table_name', if_exists=True) # 只有表存在时，才删除表。 t = o.get_table('my_new_table') t.drop() # Table对象存在时，直接调用Drop方法删除。 |  |  |

| PyODPS提供了DataFrame框架，支持以更方便的方式查询和操作MaxCompute数据。使用 | to_df() | 方法，即可转化为DataFrame对象。 |
|---|---|---|
| table = o.get_table('my_table_name') df = table.to_df() |  |  |

**表分区**

判断是否为分区表。

```python
table = o.get_table('my_new_table') if table.schema.partitions:
    print('Table %s is partitioned.' % table.name)
```

遍历表全部分区。

```
table = o.get_table('my_new_table') for partition in table.partitions: # 遍历所有分区
```

`print(partition.name) #` 具体的遍历步骤，这里是打印分区名

```
for partition in table.iterate_partitions(spec='pt=test'): # 遍历pt=test分区下的二级分区
```

`print(partition.name) #` 具体的遍历步骤，这里是打印分区名

```
for partition in table.iterate_partitions(spec='dt>20230119'): # 遍历dt>20230119分区下的二级分区
```

`print(partition.name) #` 具体的遍历步骤，这里是打印分区名

**重要**

PyODPS自0.11.3版本开始，支持为 `iterate_partitions` 指定逻辑表达式，如上述示例中的 `dt>20230119` 。 判断分区是否存在。

```
table = o.get_table('my_new_table') table.exist_partition('pt=test,sub=2015')
```

获取分区。

```python
table = o.get_table('my_new_table') partition = table.get_partition('pt=test') print(partition.creation_time) partition.size
```

创建分区。

```
t = o.get_table('my_new_table')
```

`t.create_partition('pt=test', if_not_exists=True) #` 指定`if_not_exists`参数，分区不存在时才创建分区。 删除分区。

```
t = o.get_table('my_new_table')
```

`t.delete_partition('pt=test', if_exists=True) #` 指定`if_exists`参数，分区存在时才删除分区。 `partition.drop() #` 分区对象存在时，直接对分区对象调用`Drop`方法删除。

**数据上传下载通道**

Tunnel是MaxCompute的数据通道，用户可以通过Tunnel向MaxCompute中上传或者下载数据。 上传数据示例

```
table = o.get_table('my_table') upload_session = tunnel.create_upload_session(table.name, partition_spec='pt=test') with upload_session.open_record_writer(0) as writer:
    record = table.new_record()
    record[0] = 'test1'
    record[1] = 'id1'
    writer.write(record)
    record = table.new_record(['test2', 'id2'])
    writer.write(record)
```

# 需要在`with`代码块外 `commit`，否则数据未写入即`commit`，会导致报错
下载数据示例

```
download_session = tunnel.create_download_session('my_table', partition_spec='pt=test')
```

# 处理每条记录。

```
with download_session.open_record_reader(0, download_session.count) as reader:
    for record in reader:
```

`print(record) #` 具体的遍历步骤，这里是打印记录对象

**说明**

不推荐直接使用Tunnel接口，推荐您直接使用表对象的写和读接口。 如果您安装了CPython，在安装PyODPS时会编译C代码，加速Tunnel的上传和下载。

#### 9.5.4. SQL

PyODPS支持对MaxCompute SQL的基本操作，本文为您介绍如何在PyODPS中使用SQL。

**背景信息**

| 方法名称 | 方法说明 |
|---|---|
| executesql()/runsql() _ _ | 执行SQL语句。 |
| openreader() _ | 读取SQL执行结果。 |

**说明**

在MaxCompute客户端中可以执行的SQL语句并非都可以通过入口对象的 `execute_sql()` 和 `run_sql()` 方法执行。在调用非DDL或非DML语句时，请使用其他方法。例如，调用GRANT或REVOKE语句时，请使用 `run_security_query` 方法；调用API命令时，请使用 `run_xflow` 或 `execute_xflow` 方法。 在Python UDF编写过程中，如果某个UDF引用的资源是动态变化的，您可以在**execute_sql()**中设置**alias**给旧的资源一个别名作为新的资源，无需重新删除或创建新的UDF。详情请参见设置alias。

**执行SQL语句**

参数说明
**statement**：需要执行的SQL语句。
**hints**：设置运行时参数，参数类型是DICT。
返回值说明执行 `execute_sql()` 和 `run_sql()` 后的返回值是任务实例。详情请参见任务实例。 使用示例示例1 执行SQL语句。 `o.execute_sql('select * from table_name') #`同步的方式执行，会阻塞直到`SQL`语句执行完成。

```python
instance = o.run_sql('select * from table_name') #异步的方式执行。 print(instance.get_logview_address()) # 获取Logview地址。
```

`instance.wait_for_success() #` 阻塞直到完成。 示例2 执行SQL语句时，运行参数。

```
o.execute_sql('select * from pyodps_iris', hints={'odps.stage.mapper.split.size': 16})
```

| 您也可以通过如下示例，设置 | sql.settings | ，对运行的参数进行全局配置，则在每次运行语句时都会执行对应参数。 |
|---|---|---|
| from odps import options options.sql.settings = {'odps.stage.mapper.split.size': 16} o.execute_sql('select * from pyodps_iris') # 会根据全局配置添加hints。 |  |  |

**读取SQL执行结果**

您可以通过 `open_reader` 操作读取SQL执行结果。有以下两种情况：

| 读取表数据，返回结构化数据，通过 | for | 语句遍历即可。 |
|---|---|---|
| with o.execute_sql('select * from table_name').open_reader() as reader: for record in reader: # 处理每一个record。 print(record) |  |  |

| 执行 | desc | 等命令，返回非结构化数据，需要通过 | reader.raw | 获取执行结果。 |
|---|---|---|---|---|
| with o.execute_sql('desc table_name').open_reader() as reader: print(reader.raw) |  |  |  |  |

在调用 `open_reader()` 时，PyODPS会默认调用旧的Result接口，可能会出现获取数据超时或获取数据受限等问题。您可以按照如下方法指定PyODPS调用

```
在脚本中设置 options.tunnel.use_instance_tunnel =True 。
```

按照如下示例，设置 `open_reader(tunnel=True)` 。从PyODPS v0.7.7.1开始，您可以通过 `open_reader()` 方法读取全量数据。

```python
with o.execute_sql('select * from table_name').open_reader(tunnel=True) as reader:
    for record in reader:
        print(record)
```

**说明**

如果您使用了较低版本的MaxCompute服务，或者调用Instance Tunnel出现了问题，PyODPS会给出警告并自动降级到旧的Result接口，您可根据警告信息判断导致降级的原因。 如果您使用的MaxCompute只能支持旧Result接口，并且需要读取所有的数据，您可将SQL结果写入另一张表后用读表接口读取（可能受到Project安全设置的限制）。 PyODPS默认不限制从Instance读取的数据规模，但Project Owner可能在MaxCompute Project上增加保护设置，以限制对Instance结果的读取，此时只能使用受限读取模式读取数据，在此模式下可读取的行数受到Project配置限制，通常为10000行。如果PyODPS检测到读取Instance数据被限制， 且 `options.tunnel.limit_instance_tunnel` 未设置，会自动启用受限读取模式。 如果您的Project被保护，想要手动启用受限读取模式，可以为 `open_reader()` 方法增加 `limit=True` 参数，例如 `open_reader(limit=True)` 。或者设在部分环境中（例如DataWorks）， `options.tunnel.limit_instance_tunnel` 可能默认被置为True，此时，如果想要读取所有数据，需要

| tunnel=True | 和 | limit=False | 参数，例如 | open_reader(tunnel=True, limit=False) |
|---|---|---|---|---|

**重要**

如果Project本身被保护， `tunnel=True` 和 `limit=False` 选项**不能**解除保护，此时应联系Project Owner开放相应的读权限。

**设置alias**

如果某个UDF引用的资源是动态变化的，您可以通过设置**alias**给旧的资源一个别名作为新的资源，无需重新删除或创建新的UDF。

```python
from odps.models import Schema myfunc = '''\ from odps.udf import annotate from odps.distcache import get_cache_file @annotate('bigint->bigint') class Example(object):
    def __init__(self):
        self.n = int(get_cache_file('test_alias_res1').read())
    def evaluate(self, arg):
        return arg + self.n
''' res1 = o.create_resource('test_alias_res1', 'file', file_obj='1') o.create_resource('test_alias.py', 'py', file_obj=myfunc) o.create_function('test_alias_func',
                  class_type='test_alias.Example',
                  resources=['test_alias.py', 'test_alias_res1'])
table = o.create_table(
    'test_table',
    schema=Schema.from_lists(['size'], ['bigint']),
    if_not_exists=True
```

)

```
data = [[1, ], ]
```

# 写入一行数据，只包含一个值1。

```python
o.write_table(table, 0, [table.new_record(it) for it in data]) with o.execute_sql(
    'select test_alias_func(size) from test_table').open_reader() as reader:
    print(reader[0][0])
res2 = o.create_resource('test_alias_res2', 'file', file_obj='2')
```

# 把内容为1的资源别名设置成内容为2的资源。您不需要修改`UDF`或资源。

```python
with o.execute_sql(
    'select test_alias_func(size) from test_table',
    aliases={'test_alias_res1': 'test_alias_res2'}).open_reader() as reader:
    print(reader[0][0])
```

在少数情形下，提交SQL时需要同时提交**biz_id**，否则执行会报错。此时，您可以通过设置全局**options**里的**biz_id**解决此类报错。

```python
from odps import options options.biz_id = 'my_biz_id'
```

#### 9.5.5. 任务实例

Task是MaxCompute的基本计算单元，例如SQL Task。本文为您介绍PyODPS中任务实例的基本操作。

### 基本操作

Task在执行时会被实例化，以MaxCompute实例（下文简称为实例或Instance）的形式存在。实例常见的操作如下： `list_instances()` ：获取项目空间下的所有的Instance。 `exist_instance()` ：判断某实例是否存在。 `get_instance()` ：获取实例。 `stop_instance()` ：停止实例。仅支持对运行中的实例进行停止实例操作，否则会报错。

**说明**

通过Instance对象调用 `stop` 方法也可以用于停止Instance，如 `o.get_instance('instance id').stop` 。

**示例**

获取Instancede的ID

```python
for instance in o.list_instances():
    print(instance.id)
```

判断Instance是否存在

```python
print(o.exist_instance('my_instance_id'))
```

**获取Logview地址**

| 对于SQL等任务，通过Instance对象调用 | get_logview_address | 方法即可获取Logview地址。 |
|---|---|---|
| # 从已有的instance对象获取Logview地址。 instance = o.run_sql('desc pyodps_iris') print(instance.get_logview_address()) # 从instance id获取Logview地址。 instance = o.get_instance('my_instance_id') print(instance.get_logview_address()) |  |  |

对于机器学习PAI类型任务，需要先枚举其子任务，再获取子任务的Logview。

```python
instance = o.run_xflow('AppendID', 'algo_public', {'inputTableName': 'input_table', 'outputTableName': 'output_table'}) for sub_inst_name, sub_inst in o.get_xflow_sub_instances(instance).items():
    print('%s: %s' % (sub_inst_name, sub_inst.get_logview_address()))
```

**任务实例状态**

一个Instance的状态可以是 `Running` 、 `Suspended` 或者 `Terminated` 。关于任务实例状态的方法有以下几种：

| status | ：获取实 |
|---|---|
| is_terminated |  |
| is_successful |  |

代码示例如下。 获取Instance状态。

```python
instance = o.get_instance('my_instance_id') print(instance.status) print(instance.status.value)
```

返回值示例：

```
Status.TERMINATED Terminated
```

判断当前示例是否已经执行完毕。

```python
instance = o.get_instance('my_instance_id') from odps.models import Instance print(instance.status == Instance.Status.TERMINATED)
```

| 返回值为 | True | 表示已执行完毕。 |
|---|---|---|
| 说明调用 wait_for_completion 方法会阻塞直到Instance执行完成。 wait_for_success 方法同样会阻塞，但如果最终任务执行失败，会抛出相关异常。 |  |  |

**子任务操作**

一个Instance在运行时，可能包含一个或者多个子任务，这些子任务称为Task（注意：这里的Task不同于MaxCompute的计算单元）。关于Task的方法有以下几种：

| get_task_names | ：通过此方法获取所有的Task任务。该方法返回一个所有子任务的名称列表。 |
|---|---|
| instance = o.get_instance('my_instance_id') instance.get_task_names() |  |

返回值示例：

```json
['jdbc_sql_task']
```

`get_task_result` ：指定Task名称，获取该Task的执行结果。该方法是以字典的形式返回每个Task的执行结果。代码示例如下： 获取子任务名称。

```python
instance = o.execute_sql('select * from pyodps_iris limit 1') print(instance.get_task_names())
```

返回值示例：

```json
['AnonymousSQLTask']
```

获取子任务运行结果。

```python
print(instance.get_task_result('AnonymousSQLTask'))
```

返回值示例：

```
"sepallength","sepalwidth","petallength","petalwidth","name" 4.9,3.0,1.4,0.2,"Iris-setosa"
```

获取子任务结果。

```python
print(instance.get_task_results())
```

返回值示例：

```
OrderedDict([('AnonymousSQLTask','"sepallength","sepalwidth","petallength","petalwidth","name"\n4.9,3.0,1.4,0.2,"Iris-setosa"\n')])
```

| get_task_progress | ：该方法获取在任务实例运行时Task当前的运行进度。 |
|---|---|
| instance = o.get_instance('20160519101349613gzbzufck2') while not instance.is_terminated(): for task_name in instance.get_task_names(): print(instance.id, instance.get_task_progress(task_name).get_stage_progress_formatted_string()) time.sleep(10) |  |

返回值示例：

```
20160519101349613gzbzufck2 2016-05-19 18:14:03 M1_Stg1_job0:0/1/1[100%]
```

**9.5.6. 资源**

PyODPS支持高效的数据资源管理，包括资源（文件和表）的创建、读取、修改和删除。本文介绍了PyODPS中资源的常见操作，帮助您高效管理数据资源。

### 基本操作

| list_resources() exist_resource() |  |
|---|---|
| delete_resource() |  |
| create_resource() |  |
| open_resource() | ： |

**文件资源**

文件资源包括基础的File类型，以及Py、Jar、Archive类型。 创建文件资源

| 创建文件资源可以通过给定资源名、文件类型和一个file-like的对象（或字符串对象）调用 | create_resource() | 来创建。 |
|---|---|---|
| # 使用file-like的对象创建文件资源，注意压缩包等文件需要用二进制模式读取 resource = o.create_resource('test_file_resource', 'file', file_obj=open('/to/path/file', 'rb')) # 使用字符串创建文件资源 resource = o.create_resource('test_py_resource', 'py', file_obj='import this') |  |  |

读取和修改文件资源打开一个资源有如下两种方法： 对文件资源调用 `open` 方法。 在ODPS入口调用 `open_resource()` 方法。

| 打开后的对象是file-like的对象。类似于Python内置的 | open() | 方法，文件资源也支持打开的模式，示例如下。 |
|---|---|---|
| with resource.open('r') as fp: # 以读模式打开资源。 content = fp.read() # 读取全部的内容。 fp.seek(0) # 回到资源开头。 lines = fp.readlines() # 读成多行。 fp.write('Hello World') # 报错，读模式下无法写资源。 with o.open_resource('test_file_resource', mode='r+') as fp: # 读写模式打开资源。 fp.read() fp.tell() # 定位当前位置。 fp.seek(10) fp.truncate() # 截断后面的内容。 fp.writelines(['Hello\n', 'World\n']) # 写入多行。 fp.write('Hello World') fp.flush() # 手动调用会将更新提交到ODPS。 |  |  |

所有支持的打开类型包括： r ：读模式，只能打开不能写。 w ：写模式，只能写入而不能读文件，注意用写模式打开，文件内容会先被清空。 a ：追加模式，只能写入内容到文件末尾。 `r+` ：读写模式，可以任意读写内容。 `w+` ：类似于 `r+` ，但会先清空文件内容。 `a+` ：类似于 `r+` ，但写入时只能写入文件末尾。 同时，PyODPS中文件资源支持以二进制模式打开，例如一些压缩文件需要以这种模式打开。 `rb` ：指以二进制读模式打开文件。 `r+b` ：指以二进制读写模式打开。

**表资源**

创建表资源

```
o.create_resource('test_table_resource', 'table', table_name='my_table', partition='pt=test')
```

更新表资源

```
table_resource = o.get_resource('test_table_resource') table_resource.update(partition='pt=test2', project_name='my_project2')
```

获取表及分区

```python
table_resource = o.get_resource('test_table_resource') table = table_resource.table print(table.name) partition = table_resource.partition print(partition.spec)
```

读写内容

```python
table_resource = o.get_resource('test_table_resource') with table_resource.open_writer() as writer:
    writer.write([0, 'aaaa'])
    writer.write([1, 'bbbbb'])
with table_resource.open_reader() as reader:
    for rec in reader:
        print(rec)
```

**9.5.7. 函数**

PyODPS支持灵活管理MaxCompute SQL中的自定义函数。本文提供在MaxCompute中管理自定义函数的操作指南，介绍获取、判断、创建、删除和更新函数的方法。

### 基本操作

`list_functions()` ：获取项目空间下的所有函数。 `exist_function()` ：用于判断是否存在某个函数。 `get_function()` ：用于获取函数对象。 `create_function()` ：创建函数。 `delete_function()` ：删除函数。

**创建函数**

| 使用入口对象的 | create_function() | 方法即可创建函数。举例如下。 |
|---|---|---|
| # 引用当前project中的资源。 resource = o.get_resource('my_udf.py') function = o.create_function('test_function', class_type='my_udf.Test', resources=[resource]) # 引用其他project中的资源。 resource2 = o.get_resource('my_udf.py', project='another_project') function2 = o.create_function('test_function2', class_type='my_udf.Test', resources=[resource2]) |  |  |

**删除函数**

| 使用入口对象的 | delete_function() | 方法即可删除函数，也可以使用函数对象调用 | drop | 方法删除函数。举例如下。 |
|---|---|---|---|---|
| o.delete_function('test_function') function.drop() # Function对象存在时直接调用drop方法。 |  |  |  |  |

**更新函数**

| 对函数调用 | update | 方法即可更新函数。举例如下。 |
|---|---|---|
| function = o.get_function('test_function') new_resource = o.get_resource('my_udf2.py') function.class_type = 'my_udf2.Test' function.resources = [new_resource, ] function.update() # 更新函数。 |  |  |

#### 9.5.8. XFlow和模型

XFlow实现了MaxCompute对算法包的封装，您可以使用PyODPS可以执行XFlow。

**调用命令**

您可以同步调用或异步调用下面的PAI命令。

```
PAI -name AlgoName -project algo_public -Dparam1=param_value1 -Dparam2=param_value2 ...
```

同步调用

```
inst = o.execute_xflow('AlgoName', 'algo_public', parameters={'param1': 'param_value1', 'param2': 'param_value2', ...})
```

异步调用

```
inst = o.run_xflow('AlgoName', 'algo_public', parameters={'param1': 'param_value1', 'param2': 'param_value2', ...})
```

参数不应包含命令两端的引号，也不应该包含末尾的分号。

**获取LogView**

这两个方法都会返回一个Instance对象。由于XFlow的一个Instance包含若干个子Instance，您需要使用下面的方法来获得每个Instance的LogView。

```python
for sub_inst_name, sub_inst in o.get_xflow_sub_instances(inst).items():
    print('%s: %s' % (sub_inst_name, sub_inst.get_logview_address()))
```

#### 使用说明

| get_xflow_sub_instances |  |
|---|---|
| 用 | iter_xflow_sub_instances |
| # 此处建议使用异步调用。 inst = o.run_xflow('AlgoName', 'algo_public', parameters={'param1': 'param_value1', 'param2': 'param_value2', ...}) for sub_inst_name, sub_inst in o.iter_xflow_sub_instances(inst): # 此处将进行异步等待。 print('%s: %s' % (sub_inst_name, sub_inst.get_logview_address())) |  |

| 在调用 | run_xflow | 或者 | execute_xflow | 时，也可以指定运行参数，指定的方法与SQL类似。 |
|---|---|---|---|---|
| parameters = {'param1': 'param_value1', 'param2': 'param_value2', ...} o.execute_xflow('AlgoName', 'algo_public', parameters=parameters, hints={'odps.xxx.yyy': 10}) |  |  |  |  |

| 使用 | options.ml.xflow_settings | 可以配置全局设置。 |
|---|---|---|
| from odps import options options.ml.xflow_settings = {'odps.xxx.yyy': 10} parameters = {'param1': 'param_value1', 'param2': 'param_value2', ...} o.execute_xflow('AlgoName', 'algo_public', parameters=parameters) |  |  |

**XFlow模型**

在线模型是ODPS提供的模型在线部署能力。

**部署离线模型上线**

```
model = o.create_online_model('online_model_name', 'offline_model_name')
```

| 含有自定义Pipeline的在线模型可自行构造 | ModelPredictor | 对象，示例如下。 |
|---|---|---|
| from odps.models.ml import ModelPredictor, ModelProcessor, BuiltinProcessor, PmmlProcessor, PmmlRunMode predictor = ModelPredictor(target_name='label') predictor.pipeline.append(BuiltinProcessor(offline_model_name='sample_offlinemodel', offline_model_project='online_test')) predictor.pipeline.append(PmmlProcessor(pmml='data_preprocess.xml', resources='online_test/resources/data_preprocess.xml', run_mode=PmmlRunMode.Converter)) predictor.pipeline.append(CustomProcessor(class_name='SampleProcessor', lib='libsample_processor.so', resources='online_test/resources/sample_processor.tar.gz')) model = o.create_online_model('online_model_name', predictor) |  |  |

其中， `BuiltinProcessor` 、 `PmmlProcessor` 和 `CustomProcessor` 分别指ODPS OfflineModel形成的Pipeline节点、PMML模型文件形成的Pipeline节点和用

**在线模型操作**

与其它ODPS对象类似，创建后，可列举、获取和删除在线模型。

```
 models = o.list_online_models(prefix='prefix')
 model = o.get_online_model('online_model_name')
 o.delete_online_model('online_model_name')
```

可使用模型名和数据进行在线预测，输入数据可以是Record，也可以是字典或数组和Schema的组合。

```
data = [[4, 3, 2, 1], [1, 2, 3, 4]] result = o.predict_online_model('online_model_name', data, schema=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
```

也可为模型设置ABTest。参数中的 `modelx` 可以是在线模型名，也可以是 `get_online_model` 获得的模型对象本身，而 `percentagex` 表示 `modelx` 在 ABTest中所占的百分比，范围为0至100。

```
result = o.config_online_model_ab_test('online_model_name', model1, percentage1, model2, percentage2)
```

| 修改模型参数可以通过修改 | OnlineModel | 对象的属性，再调用 | update | 方法实现，如下所示。 |
|---|---|---|---|---|
| model = o.get_online_model('online_model_name') model.cpu = 200 model.update() |  |  |  |  |

与其它对象不同的是，在线模型的创建和删除较为耗时。PyODPS默认 `create_online_model` 和 `delete_online_model` 以及 `OnlineModel` 的 `update` 方法

| 在整个操作完成后才返回。用户可以通过 | async | 选项控制是否要在模型创建请求提交后立即返回，然后自己控制等待。例如，下列语句 |
|---|---|---|
| model = o.create_online_model('online_model_name', 'offline_model_name') |  |  |

等价于

```
model = o.create_online_model('online_model_name', 'offline_model_name', async=True) model.wait_for_service()
```

而下列语句

```
o.delete_online_model('online_model_name')
```

等价于

```
o.delete_online_model('* online_model_name *', async=True)
 model.wait_for_deletion()
```

#### 9.5.9. 集成SQLAlchemy

PyODPS集成了SQLAlchemy，可以使用SQLAlchemy查询MaxCompute数据。本文为您介绍如何创建连接，并调用SQLAlchemy接口。

**创建连接**

创建连接语法格式如下。

```java
import os from sqlalchemy import create_engine
```

# 确保 `ALIBABA_CLOUD_ACCESS_KEY_ID` 环境变量设置为用户 `Access Key ID`，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 `Access Key Secret`，
# 不建议直接使用 `Access Key ID / Access Key Secret` 字符串

```
conn_string = 'odps://%s:%s@<project>/?endpoint=<endpoint>' % (
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
```

)

```
engine = create_engine(conn_string) conn = engine.connect()
```

**ALIBABA_CLOUD_ACCESS_KEY_ID**：具备访问目标MaxCompute项目权限的AccessKey ID，建议设为环境变量。
**ALIBABA_CLOUD_ACCESS_KEY_SECRET**：AccessKey ID对应的AccessKey Secret，建议设为环境变量。
**project**：目标MaxCompute项目的名称。
**endpoint**：目标MaxCompute项目所属地域的Endpoint。

| 对于已有的ODPS对象o，调用 | o.to_global() | 设为全局账号后，在连接串中就不需要指定上述参数。命令示例如下。 |
|---|---|---|
| from sqlalchemy import create_engine o.to_global() # set ODPS object as global one engine = create_engine('odps://') |  |  |

**调用SQLAlchemy接口**

创建连接之后，就可以正常调用SQLAlchemy接口。建表、写入数据、查询示例如下。 建表

```python
from sqlalchemy import Table, Column, Integer, String, MetaData metadata = MetaData() users = Table('users', metadata,
    Column('id', Integer),
    Column('name', String),
    Column('fullname', String),
```

)

```
metadata.create_all(engine)
```

写入数据

```
ins = users.insert().values(id=1, name='jack', fullname='Jack Jones') conn.execute(ins)
```

查询数据

```python
from sqlalchemy.sql import select s = select([users]) result = conn.execute(s) for row in result:
    print(row)
```

返回值

```
(1, 'jack', 'Jack Jones')
```

### DataFrame

#### 9.6.1. DataFrame概述

本文介绍PyODPS DataFrame API的核心功能与使用方法，包括对象创建、数据清洗、聚合分析及调试技巧，方便您使用类Pandas的接口在MaxCompute上进行数据分析，并支持在本地环境中进行模拟计算。

#### 使用说明

快速入门：为您介绍如何创建和操作DataFrame对象，以及使用Dataframe完成基本的数据处理。 Sequence：为您介绍Sequence。Sequence Expr代表二维数据集中的一列。SequenceExpr只可以从一个Collection中获取，不支持手动创建 Collection：为您介绍Collection。CollectionExpr中包含针对二维数据集的列操作、筛选、变换等大量操作。 MapReduce API：为您介绍DataFrame下MapReduce API的使用。 聚合操作：为您介绍DataFrame支持的聚合操作以及如何实现分组聚合、编写自定义聚合。 排序、去重、采样、数据变换：为您介绍DataFrame对象执行排序、去重、采样、数据变换操作。 数据合并：向您介绍DataFrame支持的数据表的JOIN操作、UNION操作等数据合并操作。 调试指南：由于PyODPS DataFrame本身会对整个操作执行优化，为了更直观地反映整个过程，您可以使用可视化的方式显示整个表达式的计算过程。本文为您介

#### 9.6.2. DataFrame快速入门

本文为您介绍如何创建和操作DataFrame对象，以及使用DataFrame完成基本的数据处理。

**数据准备**

本文将以movielens 100K进行举例，下载ml-100k.zip到本地。其中u.user是用户相关的数据，u.item是电影相关的数据，u.data是评分有关的数据。
1. 创建表：

| pyodps_ml_100k_users | （用户相关的数据）。 |
|---|---|
| CREATE TABLE if NOT EXISTS pyodps_ml_100k_users ( user_id BIGINT COMMENT '用户id', age BIGINT COMMENT '年龄', sex STRING COMMENT '性别', occupation STRING COMMENT '职业', zip_code STRING COMMENT '邮编' ); |  |

```
(
    movie_id            BIGINT COMMENT '电影 ID'
    ,title              STRING COMMENT '电影标题'
    ,release_date       STRING COMMENT '上映日期'
    ,video_release_date STRING COMMENT '视频发布日期'
    ,IMDb_URL           STRING COMMENT 'IMDb 链接'
    ,unknown            TINYINT COMMENT '未知'
    ,Action             TINYINT COMMENT '动作'
    ,Adventure          TINYINT COMMENT '冒险'
    ,Animation          TINYINT COMMENT '动画'
    ,Children           TINYINT COMMENT '儿童'
    ,Comedy             TINYINT COMMENT '喜剧'
    ,Crime              TINYINT COMMENT '犯罪'
    ,Documentary        TINYINT COMMENT '纪录片'
    ,Drama              TINYINT COMMENT '戏剧'
    ,Fantasy            TINYINT COMMENT '奇幻'
    ,FilmNoir           TINYINT COMMENT '黑色电影'
    ,Horror             TINYINT COMMENT '恐怖'
    ,Musical            TINYINT COMMENT '音乐'
    ,Mystery            TINYINT COMMENT '悬疑'
    ,Romance            TINYINT COMMENT '浪漫'
    ,SciFi              TINYINT COMMENT '科幻'
    ,Thriller           TINYINT COMMENT '惊悚'
    ,War                TINYINT COMMENT '战争'
    ,Western            TINYINT COMMENT '西部'
);
```

| pyodps_ml_100k_ratings | （评分有关的数据）。 |
|---|---|
| CREATE TABLE IF NOT EXISTS pyodps_ml_100k_ratings ( user_id BIGINT COMMENT '用户id' ,movie_id BIGINT COMMENT '电影id' ,rating BIGINT COMMENT '得分' ,timestamp BIGINT COMMENT '时间戳' ) |  |

2. 基于Tunnel Upload将本地数据文件内容导入MaxCompute的表中。更多Tunnel操作，请参见Tunnel操作。

```
Tunnel upload -fd | path_to_file/u.user pyodps_ml_100k_users; Tunnel upload -fd | path_to_file/u.item pyodps_ml_100k_movies; Tunnel upload -fd | path_to_file/u.data pyodps_ml_100k_ratings;
```

现在已经有了三张表，分别是 `pyodps_ml_100k_movies` （电影相关的数据）、 `pyodps_ml_100k_users` （用户相关的数据）、 `pyodps_ml_100k_ratings` （评分有关的数据）。以下示例使用IPython运行。

**说明**

确保已经安装了Python。IPython是基于Python的，所以需要先安装Python环境。接着通过pip install IPython安装IPython。安装完成后，可以通过执行 IPython命令来启动IPython的交互式环境，开始编写和执行Python代码。
1. 创建ODPS对象。

```java
import os from odps import ODPS
```

# 确保 `ALIBABA_CLOUD_ACCESS_KEY_ID` 环境变量设置为用户 `Access Key ID`，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 `Access Key Secret`，
# 不建议直接使用 `Access Key ID / Access Key Secret` 字符串

```
o = ODPS(
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    project='your-default-project',
    endpoint='your-end-point',
```

)
2. 通过传入Table对象创建一个DataFrame对象。

```
users = DataFrame(o.get_table('pyodps_ml_100k_users'))
```

| 您可以通过 | dtypes | 属性查看这个DataFrame的字段及字段类型。 |
|---|---|---|
| print(users.dtypes) |  |  |

返回值

```
odps.Schema {
  user_id             int64
  age                 int64
  sex                 string
  occupation          string
  zip_code            string
}
```

| 通过 | head | 方法，您可以取前N条数据并进行快速预览。 |
|---|---|---|
| print(users.head(10)) |  |  |

返回值

```
   user_id  age  sex     occupation  zip_code
0 1 24 M technician 85711 1 2 53 F other 94043 2 3 23 M writer 32067 3 4 24 M technician 43537 4 5 33 F other 15213 5 6 42 M executive 98101 6 7 57 M administrator 91344 7 8 36 M administrator 05201 8 9 29 M student 01002 9 10 53 M lawyer 90703
```

5. 如果您不需要看到所有字段，则可以进行如下操作：
从中筛选出一部分字段。

```python
print(users[['user_id', 'age']].head(5))
```

返回值

```
   user_id  age
0 1 24 1 2 53 2 3 23 3 4 24 4 5 33
```

只做排除个别字段操作。

```python
print(users.exclude('zip_code', 'age').head(5))
```

返回值

```
   user_id  sex  occupation
0 1 M technician 1 2 F other 2 3 M writer 3 4 M technician 4 5 F other
```

| 排除掉一些字段，通过计算得到一些新的列。例如将 | sex | 为 | M | 的置为True，否则为False，并取名为 | sex_bool | 。 |
|---|---|---|---|---|---|---|
| print(users.select(users.exclude('zip_code', 'sex'), sex_bool=users.sex == 'M').head(5)) |  |  |  |  |  |  |

返回值

```
   user_id  age  occupation  sex_bool
0 1 24 technician True 1 2 53 other False 2 3 23 writer True 3 4 24 technician True 4 5 33 other False
```

6. 查看男用户和女用户的个数。

```python
print(users.groupby(users.sex).agg(count=users.count()))
```

返回值

```
   sex  count
0 F 273 1 M 670
```

7. 将用户按职业划分，从高到低进行排序，查看人数最多的前10职业。

```python
df = users.groupby('occupation').agg(count=users['occupation'].count()) print(df.sort(df['count'], ascending=False)[:10])
```

返回值

```
      occupation  count
0 student 196 1 other 105 2 educator 95 3 administrator 79 4 engineer 67 5 programmer 66 6 librarian 51 7 writer 45 8 executive 32 9 scientist 31
```

| 或者通过 | value_counts | 方法快速实现。该方法返回的行数受到 | options.df.odps.sort.limit | 的限制，详情请参见配置选项。 |
|---|---|---|---|---|
| print(users.occupation.value_counts()[:10]) |  |  |  |  |

返回值

```
      occupation  count
0 student 196 1 other 105 2 educator 95 3 administrator 79 4 engineer 67 5 programmer 66 6 librarian 51 7 writer 45 8 executive 32 9 scientist 31
```

8. 通过更直观的图查看这份数据。在IPython中可以启用内嵌图表。

```
%matplotlib inline
```

9. 将年龄分为30组，查看年龄分布的直方图。

```
users.age.hist(bins=30, title="Distribution of users' ages", xlabel='age', ylabel='count of users')
```

显示的图表为

| 此时，只需要使用 | join | 将这三张表联合起来，然后保存为一张新的表pyodps ml 100k lens。 _ _ _ |
|---|---|---|
| movies = DataFrame(o.get_table('pyodps_ml_100k_movies')) ratings = DataFrame(o.get_table('pyodps_ml_100k_ratings')) o.delete_table('pyodps_ml_100k_lens', if_exists=True) lens = movies.join(ratings).join(users).persist('pyodps_ml_100k_lens') print(lens.dtypes) |  |  |

返回值

```
odps.Schema {
  movie_id                            int64
  title                               string
  release_date                        string
  video_release_date                  string
  imdb_url                            string
  user_id                             int64
  rating                              int64
  unix_timestamp                      int64
  age                                 int64
  sex                                 string
  occupation                          string
  zip_code                            string
}
```

1. 将年龄（0到80岁）分成8个年龄段。

```
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79'] cut_lens = lens[lens, lens.age.cut(list(range(0, 81, 10)), right=False, labels=labels).rename('年龄分组')]
```

2. 取分组和年龄唯一的前10条查看。

```python
print(cut_lens['年龄分组', 'age'].distinct()[:10])
```

返回值年龄分组 `age`

```
0 0-9 7 1 10-19 10 2 10-19 11 3 10-19 13 4 10-19 14 5 10-19 15 6 10-19 16 7 10-19 17 8 10-19 18 9 10-19 19
```

3. 最后，查看在各个年龄分组下，用户的评分总数和评分均值。

```python
print(cut_lens.groupby('年龄分组').agg(cut_lens.rating.count().rename('评分总数'), cut_lens.rating.mean().rename('评分均值')))
```

返回值年龄分组评分均值评分总数

```
0 0-9 3.767442 43 1 10-19 3.486126 8181 2 20-29 3.467333 39535 3 30-39 3.554444 25696 4 40-49 3.591772 15021 5 50-59 3.635800 8704 6 60-69 3.648875 2623 7 70-79 3.649746 197
```

请您首先下载鸢尾花数据集保存到本地作为示例数据。本文使用DataWorks PyODPS节点功能。
1. 创建测试数据表。
使用DataWorks表管理功能新建表： i. 打开相应的业务流程，右键单击**MaxCompute**，选择**新建表**。在**新建表**对话框中，选择**路径**，输入**名称**，单击**新建**，进入表的编辑页面。 ii. 选择编辑页面左上角DDL 。 iii. 输入建表语句如下，完成后提交表。

```
    sepallength double COMMENT '片长度(cm)',
    sepalwidth double COMMENT '片宽度(cm)',
    petallength double COMMENT '瓣长度(cm)',
    petalwidth double COMMENT '瓣宽度(cm)',
    name string COMMENT '种类'
);
```

2. 上传测试数据。
i. 在新建表上单击右键，选择**导入数据**，单击**下一步**，上传您刚下载的数据集。 ii. 单击**按位置匹配**后导入数据。
3. 打开相应的**业务流程**，右键单击**MaxCompute**，选择**新建节点，**选择**PyODPS 3**，新建一个PyODPS节点，用于存放和运行代码。
4. 输入代码后，单击运行
，运行后可在下方**运行日志**处查看结果。代码详情如下。

```python
iris = DataFrame(o.get_table('pyodps_iris')) #从ODPS表创建DataFrame对象iris。 print(iris.head(10))
```

`print(iris.sepallength.head(5)) #`打印`iris`部分内容。

```python
print(iris.apply(lambda row: row.sepallength + row.sepalwidth, axis=1, reduce=True, types='float').rename('sepaladd').head(3))
```

#指定函数的输出名称和类型。

```python
@output(['iris_add', 'iris_sub'], ['float', 'float']) def handle(row):
```

#使用`yield`关键字可返回多行结果。

```
    yield row.sepallength - row.sepalwidth,row.sepallength + row.sepalwidth
    yield row.petallength - row.petalwidth,row.petallength + row.petalwidth
```

#打印前5行结果，`axis=1`表示列的轴沿着水平的方向。

```python
print(iris.apply(handle,axis=1).head(5))
```

运行结果：

```bash
# print(iris.head(10))
   sepallength  sepalwidth  petallength  petalwidth         name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa 3 5.0 3.6 1.4 0.2 Iris-setosa 4 5.4 3.9 1.7 0.4 Iris-setosa 5 4.6 3.4 1.4 0.3 Iris-setosa 6 5.0 3.4 1.5 0.2 Iris-setosa 7 4.4 2.9 1.4 0.2 Iris-setosa 8 4.9 3.1 1.5 0.1 Iris-setosa 9 5.4 3.7 1.5 0.2 Iris-setosa
# print(iris.sepallength.head(5))
   sepallength
0 4.9 1 4.7 2 4.6 3 5.0 4 5.4
# print(iris.apply(lambda row: row.sepallength + row.sepalwidth, axis=1, reduce=True, types='float').rename('sepaladd').head(3))
   sepaladd
0 7.9 1 7.9 2 7.7
# print(iris.apply(handle,axis=1).head(5))
   iris_add  iris_sub
0 1.9 7.9 1 1.2 1.6 2 1.5 7.9 3 1.1 1.5 4 1.5 7.7
```

#### 9.6.3. 创建DataFrame

**前提条件**

操作下述代码示例前，您需要先准备好示例表**pyodps_iris**，详细操作请参见Dataframe数据处理。

**背景信息**

在使用DataFrame时，您需要了解 `Collection` （ `DataFrame` ）、 `Sequence` 和 `Scalar` 三类对象的操作。三类对象分别表示表结构（或者二维结构）、列 （一维结构）和标量。 您使用Pandas数据创建的对象包含实际数据，但通过MaxCompute表创建的对象并不包含实际数据，仅包含对数据的操作。MaxCompute完成数据存储和计算。 您唯一需要直接创建的Collection对象是DataFrame。DataFrame用于引用MaxCompute表、MaxCompute分区、Pandas DataFrame或Sqlalchemy Table（数据库表）数据源。这几种数据源的操作相同，您可以不更改数据处理代码，仅修改输入和输出指向，便可以将本地运行的小数据量测试代码迁移到

| 从MaxCompute表创建DataFrame，您需要将Table对象传入DataFrame方法，或者使用表的 | to_df | 方法。代码示例如下： |
|---|---|---|
| from odps.df import DataFrame # 传入Table对象。 iris = DataFrame(o.get_table('pyodps_iris')) # 使用表的to_df方法。 iris2 = o.get_table('pyodps_iris').to_df() |  |  |

| 从MaxCompute分区创建DataFrame，您需要将分区对象传入DataFrame方法，或者使用分区的 | to_df | 方法。代码示例如下： |
|---|---|---|
| from odps.df import DataFrame # 从传入Table对象。 pt_df = DataFrame(o.get_table('partitioned_table').get_partition('pt=20171111')) # 使用分区的to_df方法。 pt_df2 = o.get_table('partitioned_table').get_partition('pt=20171111').to_df() |  |  |

从Pandas DataFrame创建DataFrame，您需要将Pandas DataFrame对象传入DataFrame方法。

**代码示例**

```java
import pandas as pd import numpy as np df = DataFrame(pd.DataFrame(np.arange(9).reshape(3, 3), columns=list('abc')))
```

**注意事项**

PyODPS DataFrame会尝试对NUMPY OBJECT或STRING类型进行推断。如果一整列都为空，则会报错。为避免报错，您可以设置 `unknown_as_string` 值为**True**，将这些列指定为STRING类型。 您可以通过 `as_type` 参数，强制转换类型。如果类型为基本类型，会在创建PyODPS DataFrame时强制转换类型。如果Pandas DataFrame中包含LIST或 DICT列，系统不会推断该列的类型，必须手动使用 `as_type` 指定类型。 `as_type` 参数类型必须是DICT。

**示例：**

| 示例1：指定 | null_col2 | 列类型为 | float | 。 |
|---|---|---|---|---|
| df2 = DataFrame(df, unknown_as_string=True, as_type={'null_col2': 'float'}) print(df2.dtypes) |  |  |  |  |

返回结果：

```
odps.Schema {
  sepallength           float64
  sepalwidth            float64
  petallength           float64
  petalwidth            float64
  name                  string
```

`null_col1 string #` 无法识别，通过`unknown_as_string`设置成`STRING`类型。 `null_col2 float64 #` 强制转换成`FLOAT`类型。

```
}
```

| 示例2：指定 | list_col | 列类型为 | list<int64> | 。 |
|---|---|---|---|---|
| df4 = DataFrame(df3, as_type={'list_col': 'list<int64>'}) print(df4.dtypes) |  |  |  |  |

返回结果：

```
odps.Schema {
  id        int64
```

`list_col list<int64> #` 无法识别且无法自动转换，通过`as_type`设置。

```
}
```

**说明**

从Sqlalchemy Table创建DataFrame，您需要将Sqlalchemy Table对象传入DataFrame方法，Sqlalchemy创建连接及相关参数说明请参见创建连接。代码示例如下：

```java
import sqlalchemy
```

# 确保 `ALIBABA_CLOUD_ACCESS_KEY_ID` 环境变量设置为用户 `Access Key ID`，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 `Access Key Secret`，
# 不建议直接使用 `Access Key ID / Access Key Secret` 字符串

```
conn_string = 'odps://%s:%s@<project>/?endpoint=<endpoint>' % (
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
```

)

```
engine = sqlalchemy.create_engine(conn_string) metadata = sqlalchemy.MetaData(bind=engine) # 需要绑定到Engine。 table = sqlalchemy.Table('pyodps_iris', metadata, extend_existing=True, autoload=True)
```

#### 9.6.4. Sequence

SequenceExpr代表二维数据集中的一列。SequenceExpr只可以从一个Collection中获取，不支持手动创建SequenceExpr。

**前提条件**

您需要提前完成以下步骤，用于操作本文中的示例： 创建DataFrame，详情请参见从MaxCompute表创建DataFrame。

**获取列**

| 您可以使用 | collection.column_name | 取出一列，代码示例如下。 |
|---|---|---|
| print(iris.sepallength.head(5)) |  |  |

返回结果：

```
   sepallength
0 4.9 1 4.7 2 4.6 3 5.0 4 5.4
```

| 当列名存储在一个字符串变量中，可以使用 | df[column_name] | 实现取出一列，代码示例如下。 |
|---|---|---|
| print(iris['sepallength'].head(5)) |  |  |

返回结果

```
   sepallength
0 4.9 1 4.7 2 4.6 3 5.0 4 5.4
```

**列类型**

DataFrame拥有自己的类型系统，进行表初始化时，MaxCompute的类型会被转换成对应的DataFrame类型，以便支持更多类型的计算后端。目前，DataFrame的执行后端支持MaxCompute SQL、Pandas和数据库（MySQL和Postgres）。

| MaxCompute类型 | DataFrame类型 |
|---|---|
| BIGINT | INT64 |
| DOUBLE | FLOAT64 |
| STRING | STRING |
| DATETIME | DATETIME |
| BOOLEAN | BOOLEAN |
| DECIMAL | DECIMAL |
| ARRAY<VALUETYPE> _ | LIST<VALUETYPE> _ |
| MAP<KEYTYPE,VALUETYPE> _ _ | DICT<KEYTYPE,VALUETYPE> _ _ |
| 当 options.sql.use_odps2_extension=True 时，还支持以下数据类型。 |  |
| TINYINT | INT8 |
| SMALLINT | INT16 |
| INT | INT32 |
| FLOAT | FLOAT32 |

数据类型说明如下： LIST和DICT必须填写其包含值的类型，否则会报错。 目前DataFrame暂不支持MaxCompute 2.0中新增的TIMESTAMP及STRUCT类型。

| 在Sequence中可以通过 | sequence.dtype | 获取数据类型，代码示例如下。 |
|---|---|---|
| print(iris.sepallength.dtype) |  |  |

返回结果：

```
FLOAT64
```

如果要修改一列的类型，可以使用 `astype` 方法。该方法输入一个类型，并返回类型转换后的Sequence，代码示例如下。

```python
print(iris.sepallength.astype('int').head(5))
```

返回结果：

```
   sepallength
0 4 1 4 2 4 3 5 4 5
```

**列名**

在DataFrame的计算过程中，每个Sequence必须要有列名。通常，DataFrame会为每个Sequence起一个名字，代码示例如下。

```python
print(iris.groupby('name').sepalwidth.max().head(5))
```

返回结果：

```
   sepalwidth_max
0 4.4 1 3.4 2 3.8
```

**说明**

上述示例中， `sepalwidth` 取最大值后被命名为 `sepalwidth_max` 。除部分操作外（例如，给指定Sequence加上一个Scalar时，结果会自动被命名为这个

| Sequence提供 | rename | 方法对一列进行重命名，代码示例如下。 |
|---|---|---|
| print(iris.sepalwidth.rename('sepal_width').head(5)) |  |  |

返回结果：

```
   sepal_width
0 3.0 1 3.2 2 3.1 3 3.6 4 3.9
```

**简单的列变换**

您可以对一个Sequence进行运算，返回一个新的Sequence，这种操作类似于对简单的Python变量进行运算。Sequence支持对数值列进行四则运算，而对字符串则仅支持字符串的相加操作。代码示例如下：

```python
print((iris.sepallength + 5).head(5))
```

返回结果：

```
   sepallength
0 9.9 1 9.7 2 9.6 3 10.0 4 10.4
```

两列共同参与运算时，PyODPS无法确定最终显示的列名，需要您手动指定，代码示例如下。

```
   sum_sepal
0 7.9 1 7.9 2 7.7 3 8.6 4 9.3
```

**说明**

更多列变换说明，请参见列运算。

#### 9.6.5. Collection

DataFrame中所有二维数据集上的操作都属于CollectionExpr，可视为一张MaxCompute表或一张电子表单，DataFrame对象也是CollectionExpr的特例。

**前提条件**

您需要提前完成以下步骤，用于操作本文中的示例： 创建DataFrame，详情请参见从MaxCompute表创建DataFrame。

**获取类型**

`dtypes` 可以用来获取CollectionExpr中所有列的类型， `dtypes` 返回的是Schema类型，代码示例如下。

| print(iris.dtypes) |  |  |
|---|---|---|

返回结果：

```
odps.Schema {
  sepallength           float64
  sepalwidth            float64
  petallength           float64
  petalwidth            float64
  name                  string
}
```

**列选择和增删**

**列选择**

| 如果您需要从一个CollectionExpr中选取部分列，产生新的数据集，可以使用 | expr[columns] | 语法，代码示例如下。 |
|---|---|---|
| print(iris['name', 'sepallength'].head(5)) |  |  |

返回结果：

```
          name  sepallength
0 Iris-setosa 4.9 1 Iris-setosa 4.7 2 Iris-setosa 4.6 3 Iris-setosa 5.0 4 Iris-setosa 5.4
```

**说明**

如果只需要选取一列，需要在Columns后加上逗号或者显示标记为列表，例如 `iris[iris.sepallength,]` 或 `iris[[iris.sepallength]]` ，否则返回的将是

**列删除**

| 如果您需要在新的数据集中排除已有数据集的某些列，可使用 | exclude | 方法，代码示例如下。 |
|---|---|---|
| print(iris.exclude('sepallength', 'petallength')[:5].head(5)) |  |  |

返回结果：

```
   sepalwidth  petalwidth         name
0 3.0 0.2 Iris-setosa 1 3.2 0.2 Iris-setosa 2 3.1 0.2 Iris-setosa 3 3.6 0.2 Iris-setosa 4 3.9 0.4 Iris-setosa
```

PyODPS 0.7.2版（及以上版本）支持另一种写法，即在数据集上直接排除相应的列。代码示例如下。

```python
del iris['sepallength'] del iris['petallength'] print(iris[:5].head(5))
```

返回结果：

```
   sepalwidth  petalwidth         name
0 3.0 0.2 Iris-setosa 1 3.2 0.2 Iris-setosa 2 3.1 0.2 Iris-setosa 3 3.6 0.2 Iris-setosa 4 3.9 0.4 Iris-setosa
```

**列增加**

如果您需要在已有Collection中添加某一列变换的结果，可以使用 `expr[expr,new_sequence]` 语法，新增的列会作为新Collection的一部分。 示例：将 `iris` 中的 `sepalwidth` 列加一后重命名为 `sepalwidthplus1` 并追加到数据集末尾，形成新的数据集。代码如下：

```python
print(iris[iris, (iris.sepalwidth + 1).rename('sepalwidthplus1')].head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name  \
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa 3 5.0 3.6 1.4 0.2 Iris-setosa 4 5.4 3.9 1.7 0.4 Iris-setosa
   sepalwidthplus1
0 4.0 1 4.2 2 4.1 3 4.6 4 4.9
```

使用 `expr[expr,new_sequence]` 语法需要注意，变换后的列名与原列名可能相同。如果需要与原Collection合并，请将该列重命名。PyODPS 0.7.2版（及以上版本）支持直接在当前数据集中追加，代码示例如下。

```python
iris['sepalwidthplus1'] = iris.sepalwidth + 1 print(iris.head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name  \
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa 3 5.0 3.6 1.4 0.2 Iris-setosa 4 5.4 3.9 1.7 0.4 Iris-setosa
   sepalwidthplus1
0 4.0 1 4.2 2 4.1 3 4.6 4 4.9
```

**同时增删列**

| 您可以先将原列通过 | exclude | 方法进行排除，再将变换后的新列并入，而不必担心重名。代码示例如下。 |
|---|---|---|
| print(iris[iris.exclude('sepalwidth'), iris.sepalwidth * 2].head(5)) |  |  |

返回结果：

```
   sepallength  petallength  petalwidth         name  sepalwidth
0 4.9 1.4 0.2 Iris-setosa 6.0 1 4.7 1.3 0.2 Iris-setosa 6.4 2 4.6 1.5 0.2 Iris-setosa 6.2 3 5.0 1.4 0.2 Iris-setosa 7.2 4 5.4 1.7 0.4 Iris-setosa 7.8
```

PyODPS 0.7.2版（及以上版本）支持直接在当前数据集上覆盖的操作。代码示例如下。

```python
iris['sepalwidth'] = iris.sepalwidth * 2 print(iris.head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 4.9 6.0 1.4 0.2 Iris-setosa 1 4.7 6.4 1.3 0.2 Iris-setosa 2 4.6 6.2 1.5 0.2 Iris-setosa 3 5.0 7.2 1.4 0.2 Iris-setosa 4 5.4 7.8 1.7 0.4 Iris-setosa
```

以创建新Collection的方式实现增删列的另一种方法是调用 `select` ，将需要选择的列作为参数输入。如果您需要重命名，可以使用 `keyword` 参数输入，并将新的列名作为参数名。代码示例如下。

```python
print(iris.select('name', sepalwidthminus1=iris.sepalwidth - 1).head(5))
```

返回结果：

```
          name  sepalwidthminus1
0 Iris-setosa 2.0 1 Iris-setosa 2.2 2 Iris-setosa 2.1 3 Iris-setosa 2.6 4 Iris-setosa 2.9
```

您也可以传入一个Lambda表达式，它接收的参数为上一步的运算结果。在执行时，PyODPS会检查这些Lambda表达式，传入上一步生成的Collection并将其替换为正确的列。代码示例如下。

```python
print(iris['name', 'petallength'][[lambda x: x.name]].head(5))
```

返回结果：

```python
          name
0 Iris-setosa 1 Iris-setosa 2 Iris-setosa 3 Iris-setosa 4 Iris-setosa iris[iris.sepallength > 5.0, 'sepalwidth'] = iris.sepalwidth * 2 print(iris.head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa 3 5.0 3.6 1.4 0.2 Iris-setosa 4 5.4 7.8 1.7 0.4 Iris-setosa
```

**引入常数和随机数**

**引入常数**

| DataFrame支持在Collection中追加一列常数。追加常数需要使用Scalar | Scalar | ，引入时需要手动指定列名。代码示例如下。 |
|---|---|---|
| from odps.df import Scalar print(iris[iris, Scalar(1).rename('id')][:5].head(5)) |  |  |

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name  id
0 4.9 3.0 1.4 0.2 Iris-setosa 1 1 4.7 3.2 1.3 0.2 Iris-setosa 1 2 4.6 3.1 1.5 0.2 Iris-setosa 1 3 5.0 3.6 1.4 0.2 Iris-setosa 1 4 5.4 3.9 1.7 0.4 Iris-setosa 1
```

| 如果需要指定一个空值列，您可以使用NullScalar | NullScalar | ，但需要提供字段类型。代码示例如下。 |
|---|---|---|
| from odps.df import NullScalar print(iris[iris, NullScalar('float').rename('fid')][:5].head(5)) |  |  |

返回结果：

```python
   sepallength  sepalwidth  petallength  petalwidth         name   fid
0 4.9 3.0 1.4 0.2 Iris-setosa None 1 4.7 3.2 1.3 0.2 Iris-setosa None 2 4.6 3.1 1.5 0.2 Iris-setosa None 3 5.0 3.6 1.4 0.2 Iris-setosa None 4 5.4 3.9 1.7 0.4 Iris-setosa None iris['id'] = 1 print(iris.head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name  id
0 4.9 3.0 1.4 0.2 Iris-setosa 1 1 4.7 3.2 1.3 0.2 Iris-setosa 1 2 4.6 3.1 1.5 0.2 Iris-setosa 1 3 5.0 3.6 1.4 0.2 Iris-setosa 1 4 5.4 3.9 1.7 0.4 Iris-setosa 1
```

需要注意的是，这种写法无法自动识别空值的类型，所以在增加空值列时，仍然要使用如下代码。

```python
iris['null_col'] = NullScalar('float') print(iris.head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name null_col
0 4.9 3.0 1.4 0.2 Iris-setosa None 1 4.7 3.2 1.3 0.2 Iris-setosa None 2 4.6 3.1 1.5 0.2 Iris-setosa None 3 5.0 3.6 1.4 0.2 Iris-setosa None 4 5.4 3.9 1.7 0.4 Iris-setosa None
```

**引入随机数**

DataFrame也支持在Collection中增加一列随机数列，该列类型为FLOAT，范围为0~1，每行数值均不同。追加随机数列需要使用RandomScalar `RandomScalar` ，参数为随机数种子，可省略。代码示例如下。

```
from odps.df import RandomScalar iris[iris, RandomScalar().rename('rand_val')][:5]
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name  rand_val
0 4.9 3.0 1.4 0.2 Iris-setosa 0.000471 1 4.7 3.2 1.3 0.2 Iris-setosa 0.799520 2 4.6 3.1 1.5 0.2 Iris-setosa 0.834609 3 5.0 3.6 1.4 0.2 Iris-setosa 0.106921 4 5.4 3.9 1.7 0.4 Iris-setosa 0.763442
```

**过滤数据**

Collection提供了数据过滤的功能。支持使用与（&）、或（|）、非（~）、 `filter` 、Lambda表达式，及其他多种查询方式对数据进行过滤。

| 示例1：查询 | sepallength | 大于5的数据。 |
|---|---|---|
| print(iris[iris.sepallength > 5].head(5)) |  |  |

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 5.4 3.9 1.7 0.4 Iris-setosa 1 5.4 3.7 1.5 0.2 Iris-setosa 2 5.8 4.0 1.2 0.2 Iris-setosa 3 5.7 4.4 1.5 0.4 Iris-setosa 4 5.4 3.9 1.3 0.4 Iris-setosa
```

示例2：与（&）条件。

```python
print(iris[(iris.sepallength < 5) & (iris['petallength'] > 1.5)].head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 4.8 3.4 1.6 0.2 Iris-setosa 1 4.8 3.4 1.9 0.2 Iris-setosa 2 4.7 3.2 1.6 0.2 Iris-setosa 3 4.8 3.1 1.6 0.2 Iris-setosa 4 4.9 2.4 3.3 1.0 Iris-versicolor
```

示例3：或（|）条件。

```python
print(iris[(iris.sepalwidth < 2.5) | (iris.sepalwidth > 4)].head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 5.7 4.4 1.5 0.4 Iris-setosa 1 5.2 4.1 1.5 0.1 Iris-setosa 2 5.5 4.2 1.4 0.2 Iris-setosa 3 4.5 2.3 1.3 0.3 Iris-setosa 4 5.5 2.3 4.0 1.3 Iris-versicolor
```

**说明**

与和或条件必须使用 & 和 | ，不能使用 `and` 和 `or` 。 示例4：非（~）条件。

```python
print(iris[~(iris.sepalwidth > 3)].head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.4 2.9 1.4 0.2 Iris-setosa 2 4.8 3.0 1.4 0.1 Iris-setosa 3 4.3 3.0 1.1 0.1 Iris-setosa 4 5.0 3.0 1.6 0.2 Iris-setosa
```

| 示例5：显式调用 | filter | 方法，提供多个与条件。 |
|---|---|---|
| print(iris.filter(iris.sepalwidth > 3.5, iris.sepalwidth < 4).head(5)) |  |  |

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 5.0 3.6 1.4 0.2 Iris-setosa 1 5.4 3.9 1.7 0.4 Iris-setosa 2 5.4 3.7 1.5 0.2 Iris-setosa 3 5.4 3.9 1.3 0.4 Iris-setosa 4 5.7 3.8 1.7 0.3 Iris-setosa
```

示例6：对于连续的操作，使用Lambda表达式。

```python
print(iris[iris.sepalwidth > 3.8]['name', lambda x: x.sepallength + 1].head(5))
```

返回结果：

```
          name  sepallength
0 Iris-setosa 6.4 1 Iris-setosa 6.8 2 Iris-setosa 6.7 3 Iris-setosa 6.4 4 Iris-setosa 6.2
```

示例7：对于Collection，如果它包含一个列是BOOLEAN类型，则可以直接使用该列作为过滤条件。
# 查询`Schema`

```python
print(df.dtypes)
```

# 返回结果

```
odps.Schema {
  a boolean
  b int64
}
```

# a列为`boolean`类型，执行过滤操作

```python
print(df[df.a])
```

# 返回结果

```
      a  b
0 True 1 1 True 3
```

因此，对Collection取单个Sequence的操作时，只有BOOLEAN列是合法的，即可以对Collection进行以下过滤操作。 `df[df.a, ] #` 取列操作。 `df[[df.a]] #` 取列操作。 `df.select(df.a) #` 显式取列。 `df[df.a] # a`列是`boolean`列，执行过滤操作。 `df.a #` 取单列。 `df['a'] #` 取单列。 示例8：使用Pandas中的 `query` 方法，通过查询语句做数据的筛选，在表达式中直接使用列名（如 `sepallength` ）进行操作。在查询语句中， & 和 `and` 都表示与操作， | 和 `or` 都表示或操作。

```python
print(iris.query("(sepallength < 5) and (petallength > 1.5)").head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 4.8 3.4 1.6 0.2 Iris-setosa 1 4.8 3.4 1.9 0.2 Iris-setosa 2 4.7 3.2 1.6 0.2 Iris-setosa 3 4.8 3.1 1.6 0.2 Iris-setosa 4 4.9 2.4 3.3 1.0 Iris-versicolor
```

| 当表达式中需要使用到本地变量时，需要在该变量前加一个 | @ | 前缀。 |
|---|---|---|
| var = 4 print(iris.query("(sepalwidth < 2.5) \| (sepalwidth > @var)").head(5)) |  |  |

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 5.7 4.4 1.5 0.4 Iris-setosa 1 5.2 4.1 1.5 0.1 Iris-setosa 2 5.5 4.2 1.4 0.2 Iris-setosa 3 4.5 2.3 1.3 0.3 Iris-setosa 4 5.5 2.3 4.0 1.3 Iris-versicolor
```

| 目前 query 支持的语法，如下表所示。 |  |
|---|---|
| 语法 | 说明 |
| name | 没有 @ 前缀的都当作列名处理，有前缀的会获取本地变量。 |
| operator | 支持部分运算符： + 、 - 、 * 、 / 、 // 、 % 、 ** 、 == 、 != 、 < 、 <= 、 > 、 >= 、 in 、 not in 。 |
| bool | 与或非操作，其中 & 和 and 表示与， \| 和 or 表示或。 |
| attribute | 取对象属性。 |

|  | - |
|---|---|
| not in |  |

| index,slice,subscript | 切片操作。 |
|---|---|

**并列多行输出**

对于LIST及MAP类型的列， `explode` 方法会将该列转换为多行输出。您也可以使用 `apply` 方法实现多行输出。为了进行聚合等操作，常常需要将这些输出和原表中的列合并。此时可以使用DataFrame提供的并列多行输出功能，写法为将多行输出函数生成的集合与原集合中的列名一起映射。并列多行输出的示例如下。 查询示例数据：

```python
print(df)
```

返回结果：

```
   id         a             b
0 1 [a1, b1] [a2, b2, c2] 1 2 [c1] [d2, e2]
```

示例1：

```python
print(df[df.id, df.a.explode(), df.b])
```

返回结果：

```
   id   a             b
0 1 a1 [a2, b2, c2] 1 1 b1 [a2, b2, c2] 2 2 c1 [d2, e2]
```

示例2：

```python
print(df[df.id, df.a.explode(), df.b.explode()])
```

返回结果：

```
   id   a   b
0 1 a1 a2 1 1 a1 b2 2 1 a1 c2 3 1 b1 a2 4 1 b1 b2 5 1 b1 c2 6 2 c1 d2 7 2 c1 e2
```

如果多行输出方法对某个输入不产生任何输出，默认输入行将不在最终结果中出现。如果需要在结果中出现该行，可以设置 `keep_nulls=True` 。此时，与该行并列的值将输出为空值。示例如下。 查询示例数据：

```python
print(df)
```

返回结果：

```
   id         a
0 1 [a1, b1] 1 2 []
```

示例1：

```python
print(df[df.id, df.a.explode()])
```

返回结果：

```
   id   a
0 1 a1 1 1 b1
```

示例2：

```python
print(df[df.id, df.a.explode(keep_nulls=True)])
```

返回结果：

```
   id     a
0 1 a1 1 1 b1 2 2 None
```

使用 `explode` 方法实现并列多行输出的示例，请参见集合类型相关操作。

**限制条数**

输出前三条数据。

```python
print(iris[:3].execute())
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa
```

| 目前对于MaxCompute SQL，后端切片不支持 | start | 和 | step | 方法，但支持 | limit | 方法。 |
|---|---|---|---|---|---|---|
| print(iris.limit(3).execute()) |  |  |  |  |  |  |

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa
```

**说明**

**9.6.6. 执行**

**前提条件**

您需要提前完成以下步骤，用于操作本文中的示例： 创建DataFrame，详情请参见从MaxCompute表创建DataFrame。

**延迟执行**

DataFrame上的所有操作并不会立即执行，只有当显式调用 `execute` 方法，或者调用立即执行的方法时（内部调用的也是 `execute` ），才会执行这些操作。立即执行的方法如下表所示。

| 方法 | 说明 | 返回值 |
|---|---|---|
| persist | 将执行结果保存到MaxCompute表。 | PyODPS DataFrame |
| execute | 执行并返回全部结果。 | ResultFrame |
| head | 查看开头N行数据，这个方法会执行所有结果，并取开头N行数据。 | ResultFrame |
| tail | 查看结尾N行数据，这个方法会执行所有结果，并取结尾N行数据。 | ResultFrame |
| topandas _ | 转换为Pandas DataFrame或者Series，wrap参数为True的时候，返回 PyODPS DataFrame对象。 | wrap为True时，返回PyODPS DataFrame。 wrap为False时，返回Pandas DataFrame。False为默认值。 |
| plot，hist，boxplot | 与画图有关。 | 不涉及 |

**说明**

在交互式环境下，PyODPS DataFrame会在打印或者 `repr` 的时候，调用 `execute` 方法，您无需手动调用 `execute` 。

**示例**

# 非交互环境执行，需手动调用`execute`方法

```python
print(iris[iris.sepallength < 5][:5].execute())
```

# 交互环境执行，自动调用`execute`方法

```python
print(iris[iris.sepallength < 5][:5])
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa 3 4.6 3.4 1.4 0.3 Iris-setosa 4 4.4 2.9 1.4 0.2 Iris-setosa
```

在交互环境中，如果您需要关闭自动调用执行，请进行手动设置，设置方式如下。

```python
from odps import options options.interactive = False print(iris[iris.sepallength < 5][:5])
```

返回结果：

```
  odps.Table
    name: hudi_mc_0612.`iris3`
    schema:
      sepallength           : double      # 片长度(cm)
      sepalwidth            : double      # 片宽度(cm)
      petallength           : double      # 瓣长度(cm)
      petalwidth            : double      # 瓣宽度(cm)
      name                  : string      # 种类
    predicate:
        sepallength = Column[sequence(float64)] 'sepallength' from collection ref_0
        Scalar[int8]
  stop:
    Scalar[int8]
```

关闭自动调用执行后，打印 `repr` 对象，会显示整个抽象语法树。如果需要执行，则必须手动调用 `execute` 方法。

**读取执行结果**

| execute | 或 | head | 函数输出的结果为 | ResultFrame | 类型，可从中读取结果。 |
|---|---|---|---|---|---|
| 说明 ResultFrame是结果集合，不能参与后续计算。 |  |  |  |  |  |

ResultFrame可以迭代取出每条记录。示例如下：

```python
result = iris.head(3) for r in result:
    print(list(r))
```

返回结果：

```
[4.9, 3.0, 1.4, 0.2, 'Iris-setosa'] [4.7, 3.2, 1.3, 0.2, 'Iris-setosa'] [4.6, 3.1, 1.5, 0.2, 'Iris-setosa']
```

ResultFrame也支持在安装有Pandas的前提下转换为Pandas DataFrame，或使用Pandas后端的PyODPS DataFrame。

```
pd_df = iris.head(3).to_pandas() wrapped_df = iris.head(3).to_pandas(wrap=True)
```

**保存执行结果为MaxCompute表**

| 对于Collection，您可以调用 | persist | 方法，用于返回一个新的DataFrame对象，参数为表名。 |
|---|---|---|
| iris2 = iris[iris.sepalwidth < 2.5].persist('pyodps_iris') print(iris2.head(5)) |  |  |

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 4.5 2.3 1.3 0.3 Iris-setosa 1 5.5 2.3 4.0 1.3 Iris-versicolor 2 4.9 2.4 3.3 1.0 Iris-versicolor 3 5.0 2.0 3.5 1.0 Iris-versicolor 4 6.0 2.2 4.0 1.0 Iris-versicolor
```

| persist | 可以传入 | partitions | 参数，用于创建一个分区表。它的分区是 | partitions | 所指定的字段。 |
|---|---|---|---|---|---|
| iris3 = iris[iris.sepalwidth < 2.5].persist('pyodps_iris_test', partitions=['name']) print(iris3.data) |  |  |  |  |  |

返回结果：

```
odps.Table
  schema:
    sepallength           : double
    sepalwidth            : double
    petallength           : double
    petalwidth            : double
  partitions:
    name                  : string
```

| 区， | persist | 可以 |
|---|---|---|
| drop_partition |  |  |

| 入 | partition | 参数 |
|---|---|---|
| create_partition |  |  |

存在）该分区。

```python
print(iris[iris.sepalwidth < 2.5].persist('pyodps_iris_partition', partition='ds=test', drop_partition=True, create_partition=True).head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth             name    ds
0 4.5 2.3 1.3 0.3 Iris-setosa test 1 5.5 2.3 4.0 1.3 Iris-versicolor test 2 4.9 2.4 3.3 1.0 Iris-versicolor test 3 5.0 2.0 3.5 1.0 Iris-versicolor test 4 6.0 2.2 4.0 1.0 Iris-versicolor test
```

写入表时，您还可以指定表的生命周期。例如下列语句将表的生命周期指定为10天。

```python
print(iris[iris.sepalwidth < 2.5].persist('pyodps_iris', lifecycle=10).head(5))
```

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 4.5 2.3 1.3 0.3 Iris-setosa 1 5.5 2.3 4.0 1.3 Iris-versicolor 2 4.9 2.4 3.3 1.0 Iris-versicolor 3 5.0 2.0 3.5 1.0 Iris-versicolor 4 6.0 2.2 4.0 1.0 Iris-versicolor
```

| 如果数据源中没有ODPS对象，例如数据源仅为Pandas，在 | persist | 时需要手动指定ODPS入口对象，或者将需要的入口对象标明为全局对象。 |
|---|---|---|
| # 假设入口对象为o。 # 指定入口对象。 df.persist('table_name', odps=o) # 或者可将入口对象标记为全局。 o.to_global() df.persist('table_name') |  |  |

您可以使用 `to_pandas` 方法，如果 `wrap` 参数为True，将返回PyODPS DataFrame对象。

```python
print(type(iris[iris.sepalwidth < 2.5].to_pandas()))
```

返回结果：

| 示例2： | wrap | 参数为True，返回PyODPS DataFrame对象。 |
|---|---|---|
| print(type(iris[iris.sepalwidth < 2.5].to_pandas(wrap=True))) |  |  |

返回结果：

**说明**

PyODPS可以执行 `open_reader` 方法，通过 `reader.to_pandas()` 转成Pandas DataFrame。详情请参见表。

**立即运行设置运行参数**

对于立即执行的方法，例如 `execute` 、 `persist` 、 `to_pandas` 等，您可以通过以下方法设置它们运行时的参数（仅对ODPS SQL后端有效）： 设置全局参数。详情请参见SQL。

| 在这些立即执行的方法上，使用 | hints | 参数，可以确保这些参数只作用于当前的计算过程。 |
|---|---|---|
| print(iris[iris.sepallength < 5].to_pandas(hints={'odps.sql.mapper.split.size': 16})) |  |  |

返回结果：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 4.5 2.3 1.3 0.3 Iris-setosa 1 4.9 2.4 3.3 1.0 Iris-versicolor
```

**运行时显示详细信息**

如果您需要查看运行时Instance的Logview，则应该修改全局配置。代码示例如下。

```python
from odps import options options.verbose = True print(iris[iris.sepallength < 5].exclude('sepallength')[:5].execute())
```

返回结果：

```
Sql compiled: SELECT t1.`sepalwidth`, t1.`petallength`, t1.`petalwidth`, t1.`name` WHERE t1.`sepallength` < 5 LIMIT 5 Instance ID:
  Log view:http://logview
   sepalwidth  petallength  petalwidth             name
0 2.3 1.3 0.3 Iris-setosa 1 2.4 3.3 1.0 Iris-versicolor
```

您可以指定自己的日志记录函数。代码示例如下。

```python
my_logs = [] def my_logger(x):
    my_logs.append(x)
options.verbose_log = my_logger print(iris[iris.sepallength < 5].exclude('sepallength')[:5].execute()) print(my_logs)
```

返回结果：

```json
   sepalwidth  petallength  petalwidth             name
0 2.3 1.3 0.3 Iris-setosa 1 2.4 3.3 1.0 Iris-versicolor ['Sql compiled:', 'CREATE TABLE tmp_pyodps_24332bdb_4fd0_4d0d_aed4_38a443618268 LIFECYCLE 1 AS \nSELECT t1.`sepalwidth`, t1.`petallengt h`, t1.`petalwidth`, t1.`name` \nFROM odps_test_sqltask_finance.`pyodps_iris` t1 \nWHERE t1.`sepallength` < 5 \nLIMIT 5', 'Instance ID: 20230815034706122gbymevg*****', ' Log view:]
```

DataFrame的计算过程中，部分Collection被多次使用。如果您需要查看中间过程的执行结果，可以使用 `cache` 标记某个需要被优先计算的Collection。示例如下。

**说明**

`cache` 会延迟执行，调用 `cache` 不会触发立即计算。

```python
cached = iris[iris.sepalwidth < 3.5]['sepallength', 'name'].cache() df = cached.head(3) print(df)
```

# 返回结果

```
   sepallength             name
0 4.5 Iris-setosa 1 5.5 Iris-versicolor 2 4.9 Iris-versicolor
```

# 由于`cached`已经被计算，所以能立刻取到计算结果。

```python
print(cached.head(3))
```

#返回结果

```
   sepallength             name
0 4.5 Iris-setosa 1 5.5 Iris-versicolor 2 4.9 Iris-versicolor
```

**异步和并行执行**

**异步执行**

DataFrame支持异步操作，对于立即执行的方法，包括 `execute` 、 `persist` 、 `head` 、 `tail` 、 `to_pandas` （其他方法不支持），传入 `async` 参数，即可以将这个操作异步执行， `timeout` 参数指定超时时间，异步返回的是Future对象。

```python
future = iris[iris.sepalwidth < 10].head(10, async_=True) print(future.result())
```

# 返回结果

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 4.5 2.3 1.3 0.3 Iris-setosa 1 5.5 2.3 4.0 1.3 Iris-versicolor 2 4.9 2.4 3.3 1.0 Iris-versicolor 3 5.0 2.0 3.5 1.0 Iris-versicolor 4 6.0 2.2 4.0 1.0 Iris-versicolor 5 6.2 2.2 4.5 1.5 Iris-versicolor 6 5.5 2.4 3.8 1.1 Iris-versicolor 7 5.5 2.4 3.7 1.0 Iris-versicolor 8 6.3 2.3 4.4 1.3 Iris-versicolor 9 5.0 2.3 3.3 1.0 Iris-versicolor
```

**并行执行**

您可以使用新的 `Delay API` ，将立即执行的操作，包括 `execute` 、 `persist` 、 `head` 、 `tail` 、 `to_pandas` （其他方法不支持），变成延迟操作，并返回Future对象。当触发delay执行时，会去寻找依赖，按照给定的并发度执行，并支持异步执行。

```
from odps.df import Delay
```

`delay = Delay() #` 创建`Delay`对象。 `df = iris[iris.sepal_width < 5].cache() #` 有一个共同的依赖。 `future1 = df.sepal_width.sum().execute(delay=delay) #` 立即返回`future`对象，此时并没有执行。

```
future2 = df.sepal_width.mean().execute(delay=delay) future3 = df.sepal_length.max().execute(delay=delay)
```

`delay.execute(n_parallel=3) #` 并发度是3，此时才真正执行。

```python
|==========================================|   1 /  1  (100.00%)        21s
print(future1.result())
```

# 返回结果

```python
25.0 print(future2.result())
```

# 返回结果

```
2.272727272727273
```

| future3 |  | 。 |
|---|---|---|
| 可以用 | timeout |  |

#### 9.6.7. 列运算

本文介绍DataFrame API中的列运算功能，包括数值、逻辑、字符串、时间、集合操作及MaxCompute函数调用，实现复杂数据分析。

#### 列运算

```
lens = DataFrame(o.get_table('pyodps_ml_100k_lens'))
```

为一个Sequence加上一个常量或执行sin函数时，这些操作将作用于Sequence中的每个元素。

**NULL相关（isnull，notnull，fillna）**

DataFrame API提供了几个和NULL相关的内置函数，例如 `isnull` 用于判断某字段是否为NULL， `notnull` 用于判断某字段是否为非NULL， `fillna` 用于将 NULL填充为您指定的值。

```
>>> iris.sepallength.isnull().head(5)
   sepallength
0 False 1 False 2 False 3 False 4 False
```

**逻辑判断（ifelse，switch）**

| ifelse | 作用于BOOLEAN类型的字段，当条件成立时，返回第0个参数，否则返回第1个参数。 |
|---|---|
| >>> (iris.sepallength > 5).ifelse('gt5', 'lte5').rename('cmp5').head(5) cmp5 0 gt5 1 lte5 2 lte5 3 lte5 4 lte5 |  |

`switch` 用于多条件判断的情况。

```
>>> iris.sepallength.switch(4.9, 'eq4.9', 5.0, 'eq5.0', default='noeq').rename('equalness').head(5)
   equalness
0 noeq 1 eq4.9 2 noeq 3 noeq 4 eq5.0 >>> from odps.df import switch >>> switch(iris.sepallength == 4.9, 'eq4.9', iris.sepallength == 5.0, 'eq5.0', default='noeq').rename('equalness').head(5)
   equalness
0 noeq 1 eq4.9 2 noeq 3 noeq 4 eq5.0 >>> iris[iris.sepallength > 5, 'cmp5'] = 'gt5' >>> iris[iris.sepallength <= 5, 'cmp5'] = 'lte5' >>> iris.head(5)
   cmp5
0 gt5 1 lte5 2 lte5 3 lte5 4 lte5
```

**数学运算**

对于数字类型的字段，支持加法（+）、减法（-）、乘法（*）和除法（/）等操作，也支持log、sin等数学计算。

```
>>> (iris.sepallength * 10).log().head(5)
   sepallength
0 3.931826 1 3.891820 2 3.850148 3 3.828641 4 3.912023 >>> fields = [iris.sepallength, >>> (iris.sepallength / 2).rename('sepallength除以2'), >>> (iris.sepallength ** 2).rename('sepallength的平方')] >>> iris[fields].head(5)
   sepallength  sepallength除以2  sepallength的平方
0 5.1 2.55 26.01 1 4.9 2.45 24.01 2 4.7 2.35 22.09 3 4.6 2.30 21.16 4 5.0 2.50 25.00
```

算术运算支持如下操作。

| 算术操作 | 说明 |
|---|---|
| abs | 绝对值 |
| sqrt | 平方根 |
| sin | 无 |
| sinh | 无 |
| cos | 无 |
| cosh | 无 |
| tan | 无 |
| tanh | 无 |
| arccos | 无 |

| arccosh | 无 |
|---|---|
| arcsin | 无 |
| arcsinh | 无 |
| arctan | 无 |
| arctanh | 无 |
| exp | 指数函数 |
| expm1 | 指数减1 |
| log | 传入参数表示底是几。 |
| log2 | 无 |
| log10 | 无 |
| log1p | log(1+x) |
| radians | 给定角度计算弧度。 |
| degrees | 给定弧度计算角度。 |
| ceil | 不小于输入值的最小整数。 |
| floor | 向下取整，返回比输入值小的整数值。 |
| trunc | 将输入值截取到指定小数点位置。 |

```
>>> (iris.sepallength < 5).head(5)
   sepallength
0 False 1 True 2 True 3 True 4 False
```

| 虽然DataFrame API不支持连续操作，例如 | 3 <= iris.sepallength <= 5 | ，但是 | between | 函数可以用于判断 | iris.sepallength | 是否在某个区间。 |
|---|---|---|---|---|---|---|
| >>> (iris.sepallength.between(3, 5)).head(5) sepallength 0 False 1 True 2 True 3 True 4 True |  |  |  |  |  |  |

| 默认情况下， | between | 包含两边的区间，如果计算开区间，则需要设置 | inclusive=False | 。 |
|---|---|---|---|---|
| >>> (iris.sepallength.between(3, 5, inclusive=False)).head(5) sepallength 0 False 1 True 2 True 3 True 4 False |  |  |  |  |

**STRING相关操作**

DataFrame API提供了一系列针对STRING类型的Sequence或者Scalar的操作。

```
>>> fields = [ >>> iris.name.upper().rename('upper_name'), >>> iris.name.extract('Iris(.*)', group=1) >>> ] >>> iris[fields].head(5)
    upper_name     name
0 IRIS-SETOSA -setosa 1 IRIS-SETOSA -setosa 2 IRIS-SETOSA -setosa 3 IRIS-SETOSA -setosa 4 IRIS-SETOSA -setosa
```

STRING的相关操作如下。

| STRING操作 | 说明 |
|---|---|
| capitalize | 无 |
| contains | 包含某个字符串，如果 regex 参数为True，则是包含某个正则表达式，默认为True。 |
| count | 指定字符串出现的次数。 |
| endswith | 以某个字符串结尾。 |
| startswith | 以某个字符串开头。 |
| extract | 抽取出某个正则表达式，如果group不指定，则返回满足整个pattern的子串；否则，返回第几个group。 |
| find | 返回第一次出现的子串位置，若不存在则返回-1。 |
| rfind | 从右查找返回子串第一次出现的位置，不存在则返回-1。 |
| replace | 将某个pattern的子串全部替换成另一个子串，n参数若指定，则替换n次。 |
| get | 返回某个位置上的字符串。 |
| len | 返回字符串的长度。 |
| ljust | 若未达到指定的 width 的长度，则在右侧填充 fillchar 指定的字符串（默认空格）。 |
| rjust | 若未达到指定的 width 的长度，则在左侧填充 fillchar 指定的字符串（默认空格）。 |
| lower | 变为全部小写。 |
| upper | 变为全部大写。 |
| lstrip | 在左侧删除空格（包括空行符）。 |
| rstrip | 在右侧删除空格（包括空行符）。 |
| strip | 在左右两侧删除空格（包括空行符）。 |
| split | 将字符串按分隔符拆分为若干个字符串（返回list<string>类型）。 |
| pad | 在指定的位置（left，right或者both）用指定填充字符（用 fillchar 指定，默认空格）来对齐。 |
| repeat | 重复指定n次。 |
| slice | 切片操作。 |
| swapcase | 对调大小写。 |

| title | 同 str.title 。 |
|---|---|
| zfill | 长度没达到指定 width ，则左侧填充0。 |
| isalnum | 同 str.isalnum 。 |
| isalpha | 同 str.isalpha 。 |
| isdigit | 是否都是数字，同 str.isdigit 。 |
| isspace | 是否都是空格，同 str.isspace 。 |
| islower | 是否都是小写，同 str.islower 。 |
| isupper | 是否都是大写，同 str.isupper 。 |
| istitle | 同 str.istitle 。 |
| isnumeric | 同 str.isnumeric 。 |
| isdecimal | 同 str.isdecimal 。 |
| todict | 将字符串按分隔符拆分为一个Dict，传入的两个参数分别为项目分隔符和Key-Value分隔符（返回dict<string,string>类型）。 |
| strptime | 格式化时间，时间格式和Python标准库相同，详情请参见Python 时间格式化。 格式化时间，时间格式和Python标准库相同，详情请参见Python 时间格式化。 |

**时间相关操作**

对于DATETIME类型Sequence或者Scalar，可以调用时间相关的内置函数。

```
>>> df = lens[[lens.unix_timestamp.astype('datetime').rename('dt')]] >>> df[df.dt, >>> df.dt.year.rename('year'), >>> df.dt.month.rename('month'), >>> df.dt.day.rename('day'), >>> df.dt.hour.rename('hour')].head(5)
                    dt  year  month  day  hour
0 1998-04-08 11:02:00 1998 4 8 11 1 1998-04-08 10:57:55 1998 4 8 10 2 1998-04-08 10:45:26 1998 4 8 10 3 1998-04-08 10:25:52 1998 4 8 10 4 1998-04-08 10:44:19 1998 4 8 10
```

与时间相关的属性如下。

| 时间相关属性 | 说明 |
|---|---|
| year | 无 |
| month | 无 |
| day | 无 |
| hour | 无 |
| minute | 无 |
| second | 无 |
| weekofyear | 返回日期位于那一年的第几周。周一作为一周的第一天。 |

| weekday | 返回日期当前周的第几天。 |
|---|---|
| dayofweek | 返回日期当前周的第几天。 |
| strftime | 格式化时间，时间格式和Python标准库相同，详情请参见Python 时间格式化。 格式化时间，时间格式和Python标准库相同，详情请参见Python 时间格式化。 |

PyODPS也支持时间的加减操作，例如可以通过以下方法得到前3天的日期。两个日期列相减得到相差的毫秒数。

```
>>> df
                           a                          b
0 2016-12-06 16:43:12.460001 2016-12-06 17:43:12.460018 1 2016-12-06 16:43:12.460012 2016-12-06 17:43:12.460021 2 2016-12-06 16:43:12.460015 2016-12-06 17:43:12.460022 >>> from odps.df import day >>> df.a - day(3)
```

a

```
0 2016-12-03 16:43:12.460001 1 2016-12-03 16:43:12.460012 2 2016-12-03 16:43:12.460015 >>> (df.b - df.a).dtype int64 >>> (df.b - df.a).rename('a')
```

a

```
0 3600000 1 3600000 2 3600000
```

支持的时间类型如下表所示。

| 属性 | 说明 |
|---|---|
| year | 无 |
| month | 无 |
| day | 无 |
| hour | 无 |
| minute | 无 |
| second | 无 |
| millisecond | 无 |

**集合类型相关操作**

PyODPS支持的集合类型有List和Dict。这两个类型都可以使用下标获取集合中的某个项目。 `len` 方法用于获得集合的大小。

| explode | 方法 |
|---|---|
| enumerate |  |

示例如下。

```
>>> df
   id         a                            b
0 1 [a1, b1] {'a2': 0, 'b2': 1, 'c2': 2} 1 2 [c1] {'d2': 3, 'e2': 4} >>> df[df.id, df.a[0], df.b['b2']]
   id   a    b
0 1 a1 1 1 2 c1 NaN >>> df[df.id, df.a.len(), df.b.len()]
   id  a  b
0 1 2 3 1 2 1 2 >>> df.a.explode()
```

a

```
0 a1 1 b1 2 c1 >>> df.a.explode(pos=True)
   a_pos   a
0 0 a1 1 1 b1 2 0 c1
```

`>>> #` 指定列名。

```
>>> df.a.explode(['pos', 'value'], pos=True)
   pos value
0 0 a1 1 1 b1 2 0 c1 >>> df.b.explode()
  b_key  b_value
0 a2 0 1 b2 1 2 c2 2 3 d2 3 4 e2 4
```

`>>> #` 指定列名。

```
>>> df.b.explode(['key', 'value'])
  key  value
0 a2 0 1 b2 1 2 c2 2 3 d2 3 4 e2 4
```

| explode | 也可以和并列多行输出结合，以将原有列和 | explode | 的结果相结合，示例如下。 |
|---|---|---|---|
| >>> df[df.id, df.a.explode()] id a 0 1 a1 1 1 b1 2 2 c1 >>> df[df.id, df.a.explode(), df.b.explode()] id a b_key b_value 0 1 a1 a2 0 1 1 a1 b2 1 2 1 a1 c2 2 3 1 b1 a2 0 4 1 b1 b2 1 5 1 b1 c2 2 6 2 c1 d2 3 7 2 c1 e2 4 |  |  |  |

| 除了下标 len 和 explode 两个共有方法以外，List还支持下列方法。 |  |
|---|---|
| List操作 | 说明 |
| contains(v) | 列表是否包含某个元素。 |
| sort | 返回排序后的列表（返回值为List）。 |

Dict还支持下列方法。

| dict操作 | 说明 |
|---|---|
| keys | 获取Dict keys（返回值为List）。 |

| values | 获取Dict values（返回值为List）。 |
|---|---|

**其它元素操作（isin，notin，cut）**

| isin | 用于判断Sequence里的元素是否在某个集合元素里， | notin | 反之。 |
|---|---|---|---|
| >>> iris.sepallength.isin([4.9, 5.1]).rename('sepallength').head(5) sepallength 0 True 1 True 2 False 3 False 4 False |  |  |  |

| cut | 提供离散化的操作，可以将Sequence的数据拆成几个区段。 |
|---|---|
| >>> iris.sepallength.cut(list(range(6)), labels=['0-1', '1-2', '2-3', '3-4', '4-5']).rename('sepallength_cut').head(5) sepallength_cut 0 None 1 4-5 2 4-5 3 4-5 4 4-5 |  |

| include_under | 和 | include_over | 可以分别包括向下和向上的区间。 |
|---|---|---|---|
| >>> labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-'] >>> iris.sepallength.cut(list(range(6)), labels=labels, include_over=True).rename('sepallength_cut').head(5) sepallength_cut 0 5- 1 4-5 2 4-5 3 4-5 4 4-5 |  |  |  |

**调用MaxCompute内建或者已定义函数**

| 如果您需要调用MaxCompute上的内建或者已定义函数来生成列，您可以使用 | func | 接口，该接口默认函数返回值为STRING，可以用 | rtype | 参数指定返回值。 |
|---|---|---|---|---|
| >>> from odps.df import func >>> >>> iris[iris.name, func.rand(rtype='float').rename('rand')][:4] >>> iris[iris.name, func.rand(10, rtype='float').rename('rand')][:4] >>> # 调用ODPS上定义的UDF，列名无法确定时需要手动指定。 >>> iris[iris.name, func.your_udf(iris.sepalwidth, iris.sepallength, rtype='float').rename('new_col')] >>> # 从其它Project调用UDF，也可通过name参数指定列名。 >>> iris[iris.name, func.your_udf(iris.sepalwidth, iris.sepallength, rtype='float', project='udf_project', name='new_col')] |  |  |  |  |

**说明**

Pandas后端不支持执行带有 `func` 的表达式。

#### 9.6.8. 聚合操作

本文为您介绍DataFrame支持的聚合操作，以及如何实现分组聚合和编写自定义聚合。DataFrame提供对列进行HyperLogLog计数的接口。

**常用聚合操作**

| 使用 | describe | 函数，查看DataFrame里数字列的数量、最大值、最小值、平均值以及标准差。 |
|---|---|---|
| print(iris.describe()) |  |  |

返回结果如下。

```
    type  sepal_length  sepal_width  petal_length  petal_width
0 count 150.000000 150.000000 150.000000 150.000000 1 mean 5.843333 3.054000 3.758667 1.198667 2 std 0.828066 0.433594 1.764420 0.763161 3 min 4.300000 2.000000 1.000000 0.100000 4 max 7.900000 4.400000 6.900000 2.500000
```

使用单列执行聚合操作。

```
iris.sepallength.max()
```

返回结果如下。

```
7.9
```

| 如果在消除重复后的列上进行聚合，可以先调用 | unique | 函数，再调用相应的聚合函数。 |
|---|---|---|
| iris.name.unique().cat(sep=',') |  |  |

返回结果如下。

```
u'Iris-setosa,Iris-versicolor,Iris-virginica' iris.exclude('category').mean()
```

返回结果如下。

```
   sepal_length  sepal_width  petal_length  petal_width
1 5.843333 3.054000 3.758667 1.198667
```

| 使用 | count | 函数获取DataFrame的总行数。 |
|---|---|---|
| iris.count() |  |  |

返回结果如下。

**说明**

如果需要打印对应数据到日志中，请执行 `print(iris.count().execute())` 。

| 聚合操作 | 说明 |
|---|---|
| count（或size） | 数量。 |
| unique | 不重复值数量。 |
| min | 最小值。 |
| max | 最大值。 |
| sum | 求和。 |
| mean | 均值。 |
| median | 中位数。 |
| quantile(p) | p分位数，仅在整数值下可取得准确值。 |
| var | 方差。 |
| std | 标准差。 |
| moment | n阶中心矩（或n阶矩）。 |
| skew | 样本偏度（无偏估计）。 |
| kurtosis | 样本峰度（无偏估计）。 |
| cat | 按sep做字符串连接操作。 |
| tolist | 组合为LIST。 |

**说明**

不同于Pandas，对于列上的聚合操作，无论是在MaxCompute还是Pandas后端，PyODPS DataFrame都会忽略空值。这一逻辑与SQL类似。

**分组聚合**

DataFrame提供了 `groupby` 函数执行分组操作，分组后通过调用 `agg` 或者 `aggregate` 方法，执行聚合操作。最终的结果列中会包含分组的列和聚合的列。

```
iris.groupby('name').agg(iris.sepallength.max(), smin=iris.sepallength.min())
```

返回结果如下。

```
              name  sepallength_max  smin
0 Iris-setosa 5.8 4.3 1 Iris-versicolor 7.0 4.9 2 Iris-virginica 7.9 4.9
```

|  | value_counts |
|---|---|
| groupby |  |

```
iris.groupby('name').agg(count=iris.name.count()).sort('count', ascending=False).head(5)
```

返回结果如下。

```
              name  count
0 Iris-virginica 50 1 Iris-versicolor 50 2 Iris-setosa 50
```

| 使用 | value_counts | 函数实现。 |
|---|---|---|
| iris['name'].value_counts().head(5) |  |  |

返回结果如下。

```
              name  count
0 Iris-virginica 50 1 Iris-versicolor 50 2 Iris-setosa 50
```

对于聚合后的单列操作，您也可以直接取出列名。但此时只能使用聚合函数。

```
iris.groupby('name').petallength.sum()
```

返回结果如下。

```
   petallength_sum
0 73.2 1 213.0 2 277.6 iris.groupby('name').agg(iris.petallength.notnull().sum())
```

返回结果如下。

```
              name  petallength_sum
0 Iris-setosa 50 1 Iris-versicolor 50 2 Iris-virginica 50
```

分组时也支持对常量进行分组，但是需要使用Scalar初始化。

```
from odps.df import Scalar iris.groupby(Scalar(1)).petallength.sum()
```

返回结果如下。

```
   petallength_sum
0 563.8
```

**编写自定义聚合**

| 字段使用 | agg |
|---|---|
| buffer() |  |
| __call__(buffer, *val) |  |
| merge(buffer, pbuffer) |  |
| getvalue(buffer) |  |

计算平均值的示例如下。

```python
class Agg(object):
    def buffer(self):
        return [0.0, 0]
    def __call__(self, buffer, val):
        buffer[0] += val
        buffer[1] += 1
    def merge(self, buffer, pbuffer):
        buffer[0] += pbuffer[0]
        buffer[1] += pbuffer[1]
    def getvalue(self, buffer):
        if buffer[1] == 0:
            return 0.0
        return buffer[0] / buffer[1]
iris.sepalwidth.agg(Agg)
```

返回结果如下。

```
3.0540000000000007
```

编写自定义聚合还需要关注如下内容： 如果最终类型和输入类型发生了变化，则需要指定类型。

```
iris.sepalwidth.agg(Agg, 'float')
```

自定义聚合也可以用在分组聚合中。

```
iris.groupby('name').sepalwidth.agg(Agg)
```

返回结果如下。

```
   petallength_aggregation
0 3.418 1 2.770 2 2.974
```

| 对多列可以使用 | agg | 方法调用自定义聚合。 |
|---|---|---|
| class Agg(object): def buffer(self): return [0.0, 0.0] def __call__(self, buffer, val1, val2): buffer[0] += val1 buffer[1] += val2 def merge(self, buffer, pbuffer): buffer[0] += pbuffer[0] buffer[1] += pbuffer[1] def getvalue(self, buffer): if buffer[1] == 0: return 0.0 return buffer[0] / buffer[1] |  |  |

```
from odps.df import agg to_agg = agg([iris.sepalwidth, iris.sepallength], Agg, rtype='float') # 对两列调用自定义聚合。 iris.groupby('name').agg(val=to_agg)
```

返回结果如下。

```
              name       val
0 Iris-setosa 0.682781 1 Iris-versicolor 0.466644 2 Iris-virginica 0.451427
```

如果您需要调用MaxCompute上已经存在的UDAF，指定函数名即可。

```
iris.groupby('name').agg(iris.sepalwidth.agg('your_func')) # 对单列聚合。 to_agg = agg([iris.sepalwidth, iris.sepallength], 'your_func', rtype='float') iris.groupby('name').agg(to_agg.rename('val')) # 对多列聚合。
```

**说明**

目前，因受限于Python UDF，自定义聚合无法支持将LIST或DICT类型作为初始输入或最终输出结果。

**HyperLogLog计数**

DataFrame提供了对列进行HyperLogLog计数的接口 `hll_count` ，这个接口是近似个数的估计接口。当数据量很大时，它可以较快地估计去重后的数据量。 使用该接口计算海量用户UV时，可以快速得出估计值。

**说明**

以下示例使用了Pandas包，您可以在本地环境中运行以下示例，如果在DataWorks环境中运行，您需要先通过三方包的方式导入Pandas包。

```java
import pandas as pd import numpy as np df = DataFrame(pd.DataFrame({'a': np.random.randint(100000, size=100000)})) df.a.hll_count()
```

返回结果如下。

```
63270 df.a.nunique()
```

返回结果如下。

```
63250
```

**说明**

`splitter` 参数会对每个字段进行分隔，再计算去重后的数据量。

#### 9.6.9. 排序、去重、采样、数据变换

本文提供了对DataFrame对象进行排序、去重、采样、数据变换、数据缩放和空值处理的方法，助您高效分析数据。本文介绍了相关操作。

**前提条件**

您需要提前完成以下步骤，用于操作本文中的示例：

**排序**

| 调用 | sort | 或者 | sort_values | 方法进行排序。 |
|---|---|---|---|---|
| >>> iris.sort('sepalwidth').head(5) # 结果如下： sepallength sepalwidth petallength petalwidth name 0 5.0 2.0 3.5 1.0 Iris-versicolor 1 6.2 2.2 4.5 1.5 Iris-versicolor 2 6.0 2.2 5.0 1.5 Iris-virginica 3 6.0 2.2 4.0 1.0 Iris-versicolor 4 5.5 2.3 4.0 1.3 Iris-versicolor |  |  |  |  |

| 设置参数 | ascending=False; | 进行降序排列。 |
|---|---|---|
| >>> iris.sort('sepalwidth', ascending=False).head(5) # 结果如下： sepallength sepalwidth petallength petalwidth name 0 5.7 4.4 1.5 0.4 Iris-setosa 1 5.5 4.2 1.4 0.2 Iris-setosa 2 5.2 4.1 1.5 0.1 Iris-setosa 3 5.8 4.0 1.2 0.2 Iris-setosa 4 5.4 3.9 1.3 0.4 Iris-setosa |  |  |

设置 - 实现降序排列。

```
>>> iris.sort(-iris.sepalwidth).head(5)
```

# 结果如下：

```
   sepallength  sepalwidth  petallength  petalwidth         name
0 5.7 4.4 1.5 0.4 Iris-setosa 1 5.5 4.2 1.4 0.2 Iris-setosa 2 5.2 4.1 1.5 0.1 Iris-setosa 3 5.8 4.0 1.2 0.2 Iris-setosa 4 5.4 3.9 1.3 0.4 Iris-setosa
```

实现多字段排序。

```
>>> iris.sort(['sepalwidth', 'petallength']).head(5)
```

# 结果如下：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 5.0 2.0 3.5 1.0 Iris-versicolor 1 6.0 2.2 4.0 1.0 Iris-versicolor 2 6.2 2.2 4.5 1.5 Iris-versicolor 3 6.0 2.2 5.0 1.5 Iris-virginica 4 4.5 2.3 1.3 0.3 Iris-setosa
```

| 多字段排序时，如果是升序降序不同， | ascending | 参数可以用于传入一个列表，长度必须等同于排序的字段，它们的值都是BOOLEAN类型。 |
|---|---|---|
| >>> iris.sort(['sepalwidth', 'petallength'], ascending=[True, False]).head(5) # 结果如下： sepallength sepalwidth petallength petalwidth name 0 5.0 2.0 3.5 1.0 Iris-versicolor 1 6.0 2.2 5.0 1.5 Iris-virginica 2 6.2 2.2 4.5 1.5 Iris-versicolor 3 6.0 2.2 4.0 1.0 Iris-versicolor 4 6.3 2.3 4.4 1.3 Iris-versicolor |  |  |

下面的代码可以实现同样的效果。

```
>>> iris.sort(['sepalwidth', -iris.petallength]).head(5)
```

# 结果如下：

```
   sepallength  sepalwidth  petallength  petalwidth             name
0 5.0 2.0 3.5 1.0 Iris-versicolor 1 6.0 2.2 5.0 1.5 Iris-virginica 2 6.2 2.2 4.5 1.5 Iris-versicolor 3 6.0 2.2 4.0 1.0 Iris-versicolor 4 6.3 2.3 4.4 1.3 Iris-versicolor
```

**说明**

由于ODPS要求排序必须指定个数，所以在ODPS后端执行时，会通过 `options.df.odps.sort.limit` 指定排序个数，这个值默认是10000。如果需要排序尽量多的数据，可以把这个值设到较大的值。但是，这样可能会导致OOM。

**去重**

| 可以通过以下三种方式调用 | distinct | 方法，对Collection进行去重操作。 |
|---|---|---|
| >>> iris[['name']].distinct() # 结果如下： name 0 Iris-setosa 1 Iris-versicolor 2 Iris-virginica |  |  |

```
>>> iris.distinct('name')
```

# 结果如下：

```
              name
0 Iris-setosa 1 Iris-versicolor 2 Iris-virginica >>> iris.distinct('name', 'sepallength').head(3)
```

# 结果如下：

```
          name  sepallength
0 Iris-setosa 4.3 1 Iris-setosa 4.4 2 Iris-setosa 4.5
```

您可以调用 `unique` 对Sequence进行去重操作，但是调用 `unique` 的Sequence不能用在列选择中。

```
>>> iris.name.unique()
```

# 结果如下：

```
              name
0 Iris-setosa 1 Iris-versicolor 2 Iris-virginica
```

错误示例如下。

```
>>> iris[iris.name, iris.name.unique()]
```

**采样**

| 要对一个Collection的数据采样，可以调用 | sample | 方法。PyODPS支持以下四种采样方式： |
|---|---|---|
| 说明除了按份数采样外，其余方法如果要在ODPS DataFrame上执行，需要Project支持XFlow，否则，这些方法只能在Pandas DataFrame后端上执行。 |  |  |

按份数采样

| 在这种采样方式下，数据被分为 | parts | 份，可选择选取的份数序号。 |
|---|---|---|
| >>> iris.sample(parts=10) # 分成10份，默认取第0份。 >>> iris.sample(parts=10, i=0) # 手动指定取第0份。 >>> iris.sample(parts=10, i=[2, 5]) # 分成10份，取第2和第5份。 >>> iris.sample(parts=10, columns=['name', 'sepalwidth']) # 根据name和sepalwidth的值做采样。 |  |  |

按权重列采样

| 在这种采样方式下，您可以指定权重列和数据条数、采样比例。指定 | replace | 参数为True可启用放回采样。 |
|---|---|---|
| >>> iris.sample(n=100, weights='sepal_length') >>> iris.sample(n=100, weights='sepal_width', replace=True) |  |  |

分层采样

| 在这种采样方式下，您可以指定用于分层的标签列，同时为需要采样的每个标签指定采样比例（ | frac | 参数）或条数 （ | n | 参数）。暂不支持放回采样。 |
|---|---|---|---|---|
| >>> iris.sample(strata='category', n={'Iris Setosa': 10, 'Iris Versicolour': 10}) >>> iris.sample(strata='category', frac={'Iris Setosa': 0.5, 'Iris Versicolour': 0.4}) |  |  |  |  |

**数据缩放**

DataFrame支持通过最大、最小值或平均值、标准差对数据进行缩放。示例数据如下。

```
    name  id  fid
0 name1 4 5.3 1 name2 2 3.5 2 name2 3 1.5 3 name1 4 4.2 4 name1 3 2.2 5 name1 3 4.1
```

| 使用 | min_max_scale | 方法进行归一化。 |
|---|---|---|
| df.min_max_scale(columns=['fid']) # 结果如下： name id fid 0 name1 4 1.000000 1 name2 2 0.526316 2 name2 3 0.000000 3 name1 4 0.710526 4 name1 3 0.184211 5 name1 3 0.684211 |  |  |

| min_max_scale | 还支持使用 | feature_range | 参数指定输出值的范围。例如，需要使输出值在 (-1, 1) 范围内，示例如下。 |
|---|---|---|---|
| df.min_max_scale(columns=['fid'], feature_range=(-1, 1)) # 结果如下： name id fid 0 name1 4 1.000000 1 name2 2 0.052632 2 name2 3 -1.000000 3 name1 4 0.421053 4 name1 3 -0.631579 5 name1 3 0.368421 |  |  |  |

如果需要保留原始值，可以使用 `preserve` 参数。此时，缩放后的数据将会以新增列的形式追加到数据中，列名默认为原列名追加_scaled后缀，该后缀可使用 `suffix` 参数更改。

```
df.min_max_scale(columns=['fid'], preserve=True)
```

# 结果如下：

```
    name  id  fid  fid_scaled
0 name1 4 5.3 1.000000 1 name2 2 3.5 0.526316 2 name2 3 1.5 0.000000 3 name1 4 4.2 0.710526 4 name1 3 2.2 0.184211 5 name1 3 4.1 0.684211
```

| min_max_scale | 也支持使用 | group | 参数指定一个或多个分组列，在分组列中分别取最值进行缩放。 |
|---|---|---|---|
| df.min_max_scale(columns=['fid'], group=['name']) # 结果如下： name id fid 0 name1 4 1.000000 1 name1 4 0.645161 2 name1 3 0.000000 3 name1 3 0.612903 4 name2 2 1.000000 5 name2 3 0.000000 |  |  |  |

结果显示， `name1` 和 `name2` 两组均按组中的最值进行了缩放。 使用 `std_scale` 方法可以依照标准正态分布对数据进行调整。 `std_scale` 同样支持 `preserve` 参数保留原始列以及使用 `group` 进行分组。

```
df.std_scale(columns=['fid'])
```

# 结果如下：

```
    name  id       fid
0 name1 4 1.436467 1 name2 2 0.026118 2 name2 3 -1.540938 3 name1 4 0.574587 4 name1 3 -0.992468 5 name1 3 0.496234
```

**空值处理**

```
id name f1 f2 f3 f4 0 0 name1 1.0 NaN 3.0 4.0 1 1 name1 2.0 NaN NaN 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN
```

| 使用 | dropna | ，删除 | subset | 中包含空值的行。 |
|---|---|---|---|---|
| df.dropna(subset=['f1', 'f2', 'f3', 'f4']) # 结果如下： id name f1 f2 f3 f4 0 5 name1 1.0 2.0 3.0 4.0 |  |  |  |  |

| 如果行中包含非空值则不删除，可以使用 | how=’all’ | 。 |
|---|---|---|
| df.dropna(how='all', subset=['f1', 'f2', 'f3', 'f4']) # 结果如下： id name f1 f2 f3 f4 0 0 name1 1.0 NaN 3.0 4.0 1 1 name1 2.0 NaN NaN 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 |  |  |

| 使用 | thresh | 参数指定行中至少要有多少个非空值。 |
|---|---|---|
| df.dropna(thresh=3, subset=['f1', 'f2', 'f3', 'f4']) # 结果如下： id name f1 f2 f3 f4 0 0 name1 1.0 NaN 3.0 4.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 |  |  |

调用 `fillna` 方法，使用常数或已有的列来填充未知值。 使用常数填充未知值。

```
df.fillna(100, subset=['f1', 'f2', 'f3', 'f4'])
```

# 结果如下：

```
   id   name     f1     f2     f3     f4
0 0 name1 1.0 100.0 3.0 4.0 1 1 name1 2.0 100.0 100.0 1.0 2 2 name1 3.0 4.0 1.0 100.0 3 3 name1 100.0 1.0 2.0 3.0 4 4 name1 1.0 100.0 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 100.0 100.0 100.0 100.0
```

使用一个已有的列填充未知值。

```
df.fillna(df.f2, subset=['f1', 'f2', 'f3', 'f4'])
```

# 结果如下：

```
   id   name   f1   f2   f3   f4
0 0 name1 1.0 NaN 3.0 4.0 1 1 name1 2.0 NaN NaN 1.0 2 2 name1 3.0 4.0 1.0 4.0 3 3 name1 1.0 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN
```

| DataFrame提供了向前、向后填充的功能。您可以按照表格中的取值范围为 method 参数进行赋值。 |  |
|---|---|
| 取值 | 含义 |
| bfill、backfill | 向前填充。 |
| ffill、pad | 向后填充。 |

示例

```
df.fillna(method='bfill', subset=['f1', 'f2', 'f3', 'f4'])
```

# 结果如下：

```
   id   name   f1   f2   f3   f4
0 0 name1 1.0 3.0 3.0 4.0 1 1 name1 2.0 1.0 1.0 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 1.0 1.0 2.0 3.0 4 4 name1 1.0 3.0 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN df.fillna(method='ffill', subset=['f1', 'f2', 'f3', 'f4'])
```

# 结果如下：

```
   id   name   f1   f2   f3   f4
0 0 name1 1.0 1.0 3.0 4.0 1 1 name1 2.0 2.0 2.0 1.0 2 2 name1 3.0 4.0 1.0 1.0 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 1.0 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN
```

您也可以使用 `ffill` 、 `bfill` 函数简化代码。 `ffill` 等价于 fillna(method=’ffill’) ； `bfill` 等价于 fillna(method=’bfill’) 。

#### 9.6.10. 使用自定义函数及Python第三方库

本文介绍如何在PyODPS DataFrame中使用自定义函数（Map/Apply/Aggregate）及引用第三方Python库，涵盖闭包变量处理、资源读取、UDF/UDTF调用以及含二进制依赖包的上传与配置方法，方便您突破内置函数限制，实现复杂的数据清洗、转换与分析逻辑。 DataFrame函数支持对Sequence使用 `map` ，它会对它的每个元素调用自定义函数。

```
>>> iris.sepallength.map(lambda x: x + 1).head(5)
```

# 结果如下：

```
   sepallength
0 6.1 1 5.9 2 5.7 3 5.6 4 6.0
```

**说明**

目前，自定义函数无法支持将List/Dict类型作为输入或输出。

| 如果 | map | 前后，Sequence的类型发生了变化，则需要显式指定 | map | 后的类型。 |
|---|---|---|---|---|
| >>> iris.sepallength.map(lambda x: 't'+str(x), 'string').head(5) # 结果如下： sepallength 0 t5.1 1 t4.9 2 t4.7 3 t4.6 4 t5.0 |  |  |  |  |

如果在函数中包含闭包，则函数外闭包变量值的变化会引起函数内该变量值的变化。

```
>>> dfs = [] >>> for i in range(10): >>> dfs.append(iris.sepallength.map(lambda x: x + i))
```

| 结果为 | dfs | 中每个 | SequenceExpr | 均为 | iris.sepallength+9 | 。为解决此问题，可以将函数作为另一函数的返回值，或者使用 | partial | 。两个示例如下。 |
|---|---|---|---|---|---|---|---|---|
| >>> dfs = [] >>> def get_mapper(i): >>> return lambda x: x + i >>> for i in range(10): >>> dfs.append(iris.sepallength.map(get_mapper(i))) |  |  |  |  |  |  |  |  |

```
>>> import functools >>> dfs = [] >>> for i in range(10): >>> dfs.append(iris.sepallength.map(functools.partial(lambda v, x: x + v, i)))
```

`map` 也支持使用现有的UDF函数，传入的参数是str类型（函数名）或者Function对象，详情请参见函数。 `map` 传入Python函数的实现使用了MaxCompute Python UDF。因此，如果您所在的Project不支持Python UDF，则 `map` 函数无法使用。除此以外，所有 Python UDF的限制在此都适用。 目前，默认可使用的第三方库（包含C）只有numpy，第三方库使用详情请参见使用第三方Python库。 除了调用自定义函数，DataFrame还提供了很多内置函数，这些函数中部分使用了 `map` 函数来实现。因此，如果您所在Project未开通Python UDF，则无法使用这些函数（注意：阿里云公共服务暂不提供对Python UDF的支持）。

**说明**

由于字节码定义的差异，Python 3下使用新语言特性（例如 `yield from` ）时，代码在使用Python 2.7的MaxCompute Worker上执行时会发生错误。因此， 建议您在Python 3下使用MapReduce API编写生产作业前，先确认相关代码是否能正常执行。 示例程序：使用计数器

```python
from odps.udf import get_execution_context def h(x):
    ctx = get_execution_context()
    counters = ctx.get_counters()
    counters.get_counter('df', 'add_one').increment(1)
    return x + 1
df.field.map(h)
```

Logview的JSONSummary中即可找到计数器值。 如果您需要对一行数据使用自定义函数，可以使用 `apply` 方法。参数 `axis` 的值必须设为1，表示对行进行操作。 `apply` 的自定义函数接收一个参数，参数为上 `reduce` 为True时，表示返回结果为Sequence，否则返回结果为Collection。 `names` 和 `types` 参数分别指定返回的Sequence或Collection的字段名和类型。如果未指定类型，则会默认为STRING类型。

```
>>> iris.apply(lambda row: row.sepallength + row.sepalwidth, axis=1, reduce=True, types='float').rename('sepaladd').head(3)
```

# 结果如下：

```
   sepaladd
0 8.6 1 7.9 2 7.9
```

| 在 | apply | 的自定义函数中， | reduce | 为False时，您可以使用 | yield | 关键字返回多行结果。 |
|---|---|---|---|---|---|---|
| >>> iris.count() # 结果如下： 150 >>> >>> def handle(row): >>> yield row.sepallength - row.sepalwidth, row.sepallength + row.sepalwidth >>> yield row.petallength - row.petalwidth, row.petallength + row.petalwidth >>> >>> iris.apply(handle, axis=1, names=['iris_add', 'iris_sub'], types=['float', 'float']).count() # 结果如下： 300 |  |  |  |  |  |  |

您也可以在函数中注释返回的字段和类型，无需在函数调用时再指定它们。

```
>>> from odps.df import output >>> >>> @output(['iris_add', 'iris_sub'], ['float', 'float']) >>> def handle(row): >>> yield row.sepallength - row.sepalwidth, row.sepallength + row.sepalwidth >>> yield row.petallength - row.petalwidth, row.petallength + row.petalwidth >>> >>> iris.apply(handle, axis=1).count()
```

# 结果如下：

| 您也可以使用 | map-only | 的 | map_reduce | ，该操作与 | axis=1 | 的 | apply | 操作是等价的。 |
|---|---|---|---|---|---|---|---|---|
| >>> iris.map_reduce(mapper=handle).count() # 结果如下： 300 |  |  |  |  |  |  |  |  |

如果您想调用MaxCompute上已经存在的UDTF，函数指定为函数名即可。

```
>>> iris['name', 'sepallength'].apply('your_func', axis=1, names=['name2', 'sepallength2'], types=['string', 'float'])
```

| 使用 | apply | 对行操作，且 | reduce | 为False时，您可以使用并列多行输出与已有的行结合，用于后续聚合等操作。 |
|---|---|---|---|---|
| >>> from odps.df import output >>> >>> @output(['iris_add', 'iris_sub'], ['float', 'float']) >>> def handle(row): >>> yield row.sepallength - row.sepalwidth, row.sepallength + row.sepalwidth >>> yield row.petallength - row.petalwidth, row.petallength + row.petalwidth >>> >>> iris[iris.category, iris.apply(handle, axis=1)] |  |  |  |  |

**对所有列调用自定义聚合**

| 调用 | apply | 方法，当不指定 | axis | ，或者 | axis | 值为0时，您可以通过传入一个自定义聚合类对所有Sequence进行聚合操作。 |
|---|---|---|---|---|---|---|
| class Agg(object): def buffer(self): return [0.0, 0] def __call__(self, buffer, val): buffer[0] += val buffer[1] += 1 def merge(self, buffer, pbuffer): buffer[0] += pbuffer[0] buffer[1] += pbuffer[1] def getvalue(self, buffer): if buffer[1] == 0: return 0.0 return buffer[0] / buffer[1] |  |  |  |  |  |  |

```
>>> iris.exclude('name').apply(Agg)
```

# 结果如下：

```
   sepallength_aggregation  sepalwidth_aggregation  petallength_aggregation  petalwidth_aggregation
0 5.843333 3.054 3.758667 1.198667
```

**说明**

目前，自定义函数无法支持将LIST/DICT类型作为初始输入或最终输出结果。

**引用资源**

自定义函数也能读取MaxCompute上的资源（表资源或文件资源），或者引用一个Collection作为资源。此时，自定义函数需要写成函数闭包或Callable的类。两个示例如下。

```
>>> file_resource = o.create_resource('pyodps_iris_file', 'file', file_obj='Iris-setosa') >>> >>> iris_names_collection = iris.distinct('name')[:2]
```

# 结果如下：

```
       sepallength
0 Iris-setosa 1 Iris-versicolor
```

`>>> def myfunc(resources): # resources`按调用顺序传入。

```
>>> names = set()
```

`>>> fileobj = resources[0] #` 文件资源是一个`file-like`的`object`。

```
>>> for l in fileobj: >>> names.add(l) >>> for r in collection:
```

`>>> names.add(r.name) #` 这里可以通过字段名或者偏移来取。

```
>>> def h(x): >>> if x in names: >>> return True >>> else: >>> return False >>> return h >>> >>> df = iris.distinct('name') >>> df = df[df.name, >>> df.name.map(myfunc, resources=[file_resource, iris_names_collection], rtype='boolean').rename('isin')] >>> >>> df
```

# 结果如下：

```
              name   isin
0 Iris-setosa True 1 Iris-versicolor True 2 Iris-virginica False
```

**说明**

分区表资源在读取时不包含分区字段。 当 `axis` 值为1，即在行上操作时，您需要写一个函数闭包或者Callable的类。而对于列上的聚合操作，您只需在 `__init__` 函数里读取资源即可。

```
>>> words_df
                     sentence
0 Hello World 1 Hello Python 2 Life is short I use Python >>> >>> import pandas as pd >>> stop_words = DataFrame(pd.DataFrame({'stops': ['is', 'a', 'I']})) >>> >>> @output(['sentence'], ['string']) >>> def filter_stops(resources): >>> stop_words = set([r[0] for r in resources[0]]) >>> def h(row): >>> return ' '.join(w for w in row[0].split() if w not in stop_words), >>> return h >>> >>> words_df.apply(filter_stops, axis=1, resources=[stop_words])
```

# 结果如下：

```
                sentence
0 Hello World 1 Hello Python 2 Life short use Python
```

**说明**

这里的 `stop_words` 存放于本地，但在真正执行时会被上传到MaxCompute作为资源引用。

**使用第三方Python库**

您可以把第三方Python包作为资源上传到MaxCompute，支持的格式有whl、egg、zip以及tar.gz。在全局或者在立即执行的方法时，指定需要使用的包文件，即可以在自定义函数中使用第三方库。第三方库的依赖库，也必须指定，否则依然会导致导入错误。 您可以通过PyODPS的资源上传接口create_resource()来完成资源的上传。 下面以python-dateutil包进行举例： i. 使用 `pip download` 命令，下载包以及其依赖到某个路径。下载后会出现两个包：six-1.10.0-py2.py3-none-any.whl和python_dateutil-2.5.3-py2.py3none-any.whl（注意：这里需要下载支持Linux环境的包）。

```bash
$ pip download python-dateutil -d /to/path/
```

ii. 分别把两个文件上传到MaxCompute资源。 `>>> #` 这里要确保资源名的后缀是正确的文件类型。

```
>>> odps.create_resource('six.whl', 'file', file_obj=open('six-1.10.0-py2.py3-none-any.whl', 'rb')) >>> odps.create_resource('python_dateutil.whl', 'file', file_obj=open('python_dateutil-2.5.3-py2.py3-none-any.whl', 'rb')) >>> df
```

# 结果如下：

```
               datestr
0 2016-08-26 14:03:29 1 2015-08-26 14:03:29
```

iv. 全局配置使用到的三方库如下。

```
>>> from odps import options >>> >>> def get_year(t): >>> from dateutil.parser import parse >>> return parse(t).strftime('%Y') >>> >>> options.df.libraries = ['six.whl', 'python_dateutil.whl'] >>> df.datestr.map(get_year)
```

# 结果如下：

```
   datestr
0 2016 1 2015
```

或者通过运行方法的 `libraries` 参数指定使用到的第三方库。

```
>>> def get_year(t): >>> from dateutil.parser import parse >>> return parse(t).strftime('%Y') >>> >>> df.datestr.map(get_year).execute(libraries=['six.whl', 'python_dateutil.whl'])
```

# 结果如下：

```
   datestr
0 2016 1 2015
```

PyODPS默认支持执行仅包含Python且不含文件操作的第三方库。在较新版本的MaxCompute服务下，PyODPS也支持执行带有二进制代码或带有文件操作的 Python库。这些库的后缀必须是cp27-cp27m-manylinux1_x86_64，以 `archive` 方式上传，whl后缀的包需要重命名为zip。同时，作业需要开启 `odps.isolation.session.enable` 选项，或者在Project级别开启 `isolation` 。以下示例为您展示如何上传并使用 `scipy` 中的特殊函数。 `>>> #` 对于含有二进制代码的包，必须使用`archive`方式上传资源，`whl`后缀需要改为`zip`。

```
>>> odps.create_resource('scipy.zip', 'archive', file_obj=open('scipy-0.19.0-cp27-cp27m-manylinux1_x86_64.whl', 'rb')) >>>
```

`>>> #` 如果`Project`开启了`isolation`，下面的选项不是必需的。

```
>>> options.sql.settings = { 'odps.isolation.session.enable': True } >>> >>> def psi(value):
```

`>>> #` 建议在函数内部`import`第三方库，以防止不同操作系统下二进制包结构差异造成执行错误。

```
>>> from scipy.special import psi >>> return float(psi(value)) >>> >>> df.float_col.map(psi).execute(libraries=['scipy.zip'])
```

对于只提供源码的二进制包，可以在Linux Shell中打包成Wheel再上传，Mac和Windows中生成的Wheel包无法在MaxCompute中使用。

```
python setup.py bdist_wheel
```

您也可以通过MaxCompute Console上传资源。 i. 现在主流的Python包都提供了whl包，提供了各平台包含二进制文件的包，因此找到可以在MaxCompute上运行的包是第一步。 ii. 其次，要想在MaxCompute上运行，需要包含所有的依赖包，这个是比较繁琐的。各个包的依赖情况如下表所示。

| 包名 | 依赖 |
|---|---|
| pandas | numpy、python-dateutil、pytz、six |
| scipy | numpy |
| scikit-learn | numpy、scipy |

**说明**

其中numpy已包含，您只需上传python-dateutil、pytz、pandas、scipy、sklearn、six包，pandas、scipy和scikit-learn即可使用。 iii. 您可进入python-dateutils找到python-dateutil-2.6.0.zip进行下载。 iv. 重命名为python-dateutil.zip，通过MaxCompute Console上传资源。

```
add archive python-dateutil.zip;
```

**说明**

pytz和six的上传方式同上，分别找到pytz-2017.2.zip和six-1.11.0.tar.gz进行下载和上传资源操作。 v. 对于Pandas这种包含c的包，需要找到名字中包含cp27-cp27m-manylinux1_x86_64的whl包，这样才能在MaxCompute上正确执行。因此，您需要找到pandas-0.20.2-cp27-cp27m-manylinux1_x86_64.whl进行下载，然后把后缀改成zip，在MaxCompute Console中执行 add archive pandas.zip; 进行上传。scipy和scikit-learn包的操作同上。 所有包需要下载的资源如下表所示。

| 包名 | 文件名 | 上传资源名 |
|---|---|---|
| python-dateutil | python-dateutil-2.6.0.zip | python-dateutil.zip |
| pytz | pytz-2017.2.zip | pytz.zip |

| six | six-1.11.0.tar.gz | six.tar.gz |
|---|---|---|
| pandas | pandas-0.20.2-cp27-cp27m-manylinux1x8664.zip _ _ | pandas.zip |
| scipy | scipy-0.19.0-cp27-cp27m-manylinux1x8664.zip _ _ | scipy.zip |
| scikit-learn | scikitlearn-0.18.1-cp27-cp27m-manylinux1x8664.zip _ _ _ | sklearn.zip |

**指定第三方Python库**

在全局指定使用的库。

```
>>> from odps import options >>> options.df.libraries = ['six.whl', 'python_dateutil.whl']
```

在立即执行的方法中，局部指定使用的库。

```
>>> df.apply(my_func, axis=1).to_pandas(libraries=['six.whl', 'python_dateutil.whl'])
```

#### 9.6.11. 使用自定义函数

DataFrame函数支持对Sequence使用map，它会对它的每个元素调用自定义函数。

```
iris.sepallength.map(lambda x: x + 1).head(5)
```

# 结果如下：

```
   sepallength
0 6.1 1 5.9 2 5.7 3 5.6 4 6.0
```

**说明**

目前，受限于Python UDF，自定义函数无法支持将list/dict类型作为输入或输出。

```
iris.sepallength.map(lambda x: 't'+str(x), 'string').head(5)
```

# 结果如下：

```
   sepallength
0 t5.1 1 t4.9 2 t4.7 3 t4.6 4 t5.0
```

如果在函数中包含闭包，需要注意的是，函数外闭包变量值的变化会引起函数内该变量值的变化。例如，

```
dfs = [] for i in range(10):
    dfs.append(df.sepallength.map(lambda x: x + i))
```

| 结果为dfs中每个SequenceExpr均为 | df.sepal_length + 9 | 。为解决此问题，可以将函数作为另一函数的返回值，或者使用partial，如 |
|---|---|---|
| dfs = [] def get_mapper(i): return lambda x: x + i for i in range(10): dfs.append(df.sepallength.map(get_mapper(i))) |  |  |

或

```java
import functools dfs = [] for i in range(10):
    dfs.append(df.sepallength.map(functools.partial(lambda v, x: x + v, i)))
```

map也支持使用现有的UDF函数，传入的参数是str类型（函数名）或者Function对象。 map传入Python函数的实现使用了ODPS Python UDF，但是，如果用户所在的Project不支持Python UDF，则map函数无法使用。除此以外，所有Python UDF的限制在此都适用。 目前，第三方库（包含C）只能使用 `numpy` ，第三方库使用参考使用第三方Python库。 除了调用自定义函数，DataFrame还提供了很多内置函数，这些函数中部分使用了map函数来实现，但是，如果用户所在Project未开通Python UDF，则这些函数也就无法使用。

**说明**

从2018年10月16日开始，MaxCompute公共云环境下的Python UDF使用权限全面开放。 由于字节码定义的差异，Python 3下使用新语言特性（例如 `yield from` ）时，代码在使用Python 2.7的ODPS Worker上执行时会发生错误。因而建议在 Python 3下使用MapReduce API编写生产作业前，先确认相关代码是否能正常执行。

**引用资源**

自定义函数也能读取ODPS上的资源（表资源或文件资源），或者引用一个collection作为资源。此时，自定义函数需要写成函数闭包或callable的类。

```
file_resource = o.create_resource('pyodps_iris_file', 'file', file_obj='Iris-setosa') iris_names_collection = iris.distinct('name')[:2]
```

# 结果如下：

```
       sepallength
0 Iris-setosa 1 Iris-versicolor
```

`def myfunc(resources): # resources`按调用顺序传入

```
    names = set()
```

`fileobj = resources[0] #` 文件资源是一个`file-like`的`object`

```
    for l in fileobj:
        names.add(l)
    for r in collection:
```

`names.add(r.name) #` 这里可以通过字段名或者偏移来取

```python
    def h(x):
        if x in names:
            return True
        else:
            return False
    return h
df = iris.distinct('name') df = df[df.name, df.name.map(myfunc, resources=[file_resource, iris_names_collection], rtype='boolean').rename('isin')]
```

`df`
# 结果如下：

```
              name   isin
0 Iris-setosa True 1 Iris-versicolor True 2 Iris-virginica False
```

**说明**

分区表资源在读取时不包含分区字段。

**使用第三方Python库**

`df`

```
               datestr
0 2016-08-26 14:03:29 1 2015-08-26 14:03:29
```

全局配置使用到的三方库：

```python
from odps import options def get_year(t):
    from dateutil.parser import parse
    return parse(t).strftime('%Y')
options.df.libraries = ['six.whl', 'python_dateutil.whl'] df.datestr.map(get_year)
```

# 结果如下：

```
   datestr
0 2016 1 2015
```

| 或者，通过立即运行方法的 | libraries | 参数指定： |
|---|---|---|
| def get_year(t): from dateutil.parser import parse return parse(t).strftime('%Y') df.datestr.map(get_year).execute(libraries=['six.whl', 'python_dateutil.whl']) # 结果如下： datestr 0 2016 1 2015 |  |  |

PyODPS默认支持执行纯Python且不含文件操作的第三方库。在较新版本的MaxCompute服务下，PyODPS也支持执行带有二进制代码或带有文件操作的Python

| 启 | odps.isolation.session.enable | _ _ 选项，或者在Project级别开启Isolation。下面的例子展示了如何上传并使用scipy中的特殊函数： |
|---|---|---|
| # 对于含有二进制代码的包，必须使用Archive方式上传资源，whl后缀需要改为zip odps.create_resource('scipy.zip', 'archive', file_obj=open('scipy-0.19.0-cp27-cp27m-manylinux1_x86_64.whl', 'rb')) # 如果Project开启了Isolation，下面的选项不是必需的 options.sql.settings = { 'odps.isolation.session.enable': True } def psi(value): # 建议在函数内部import第三方库，以防止不同操作系统下二进制包结构差异造成执行错误 from scipy.special import psi return float(psi(value)) df.float_col.map(psi).execute(libraries=['scipy.zip']) |  |  |

对于只提供源码的二进制包，可以在Linux Shell中打包成Wheel再上传，Mac和Windows中生成的Wheel包无法在 MaxCompute中使用：

```
python setup.py bdist_wheel
```

**使用计数器**

```python
from odps.udf import get_execution_context def h(x):
    ctx = get_execution_context()
    counters = ctx.get_counters()
    counters.get_counter('df', 'add_one').increment(1)
    return x + 1
df.field.map(h)
```

logview的JSONSummary中即可找到计数器值。

**调用ODPS内建或者已定义函数**

要想调用ODPS上的内建或者已定义函数，来生成列，我们可以使用func接口，该接口默认函数返回值为String，可以用rtype参数指定返回值。

```
from odps.df import func iris[iris.name, func.rand(rtype='float').rename('rand')][:4] iris[iris.name, func.rand(10, rtype='float').rename('rand')][:4]
```

# 调用`ODPS`上定义的`UDF`，列名无法确定时需要手动指定

```
iris[iris.name, func.your_udf(iris.sepalwidth, iris.sepallength, rtype='float').rename('new_col')]
```

# 从其他`Project`调用`UDF`，也可通过`name`参数指定列名

```
iris[iris.name, func.your_udf(iris.sepalwidth, iris.sepallength, rtype='float', project='udf_project',name='new_col')]
```

**说明**

在使用Pandas后端时，不支持执行带有func的表达式。

#### 9.6.12. PyODPS DataFrame自定义函数中使用第三方包

本文向您介绍如何在PyODPS DataFrame自定义函数中上传和使用pandas、scipy和scikit-learn第三方包。

#### 使用说明

PyODPS DataFrame提供了类似pandas的接口来操作MaxCompute数据，同时也支持在本地使用pandas和使用数据库来执行。 PyODPS DataFrame不仅支持类似pandas的map和apply方法，也提供了MapReduce API来扩展pandas语法以适应大数据环境。 PyODPS的自定义函数是序列化到MaxCompute上执行，MaxCompute的Python环境仅包含numpy第三方包。现在，MaxCompute可以实现在自定义函数中使用pandas、scipy或scikit-learn等包含c代码的库。

**说明**

**上传第三方包**

**说明**

您只需上传一次第三方包，当MaxCompute资源有了这些包，可直接跳过此步。 现在主流的Python包都提供了whl包，提供了各平台包含二进制文件的包，因此找到可以在MaxCompute上运行的包是第一步。 其次，要想在MaxCompute上运行，需要包含所有的依赖包，这个是比较繁琐的。各个包的依赖情况如下表所示。

| 包名 | 依赖 |
|---|---|
| pandas | numpy，python-dateutil，pytz，six |
| scipy | numpy |
| scikit-learn | numpy，scipy |

**说明**

其中numpy已包含，您只需上传python-dateutil、pytz、pandas、scipy、sklearn、six包，pandas、scipy和scikit-learn即可使用。 您可进入python-dateutils找到python-dateutil-2.6.0.zip进行下载。 重命名为python-dateutil.zip，通过MaxCompute Console上传资源。

```
add archive python-dateutil.zip;
```

**说明**

pytz和six的上传方式同上，分别找到pytz-2017.2.zip和six-1.11.0.tar.gz进行下载和上传资源操作。 对于pandas这种包含c的包，需要找到名字中包含cp27-cp27m-manylinux1_x86_64的whl包，这样才能在MaxCompute上正确执行。因此，您需要找到pandas- 0.20.2-cp27-cp27m-manylinux1_x86_64.whl进行下载，然后把后缀改成zip，在MaxCompute Console中执行 add archive pandas.zip; 进行上传。 其他包的操作同上，需下载资源如下表所示。

| 包名 | 文件名 | 上传资源名 |
|---|---|---|
| python-dateutil | python-dateutil-2.6.0.zip | python-dateutil.zip |
| pytz | pytz-2017.2.zip | pytz.zip |
| six | six-1.11.0.tar.gz | six.tar.gz |
| pandas | pandas-0.20.2-cp27-cp27m-manylinux1x8664.zip _ _ | pandas.zip |
| scipy | scipy-0.19.0-cp27-cp27m-manylinux1x8664.zip _ _ | scipy.zip |
| scikit-learn | scikitlearn-0.18.1-cp27-cp27m-manylinux1x8664.zip _ _ _ | sklearn.zip |

**说明**

**编写代码验证**

1. 写一个简单的函数，里面用到所有的库，最好是在函数中import这些第三方库。

```java
def test(x):
    from sklearn import datasets, svm
    from scipy import misc
    import numpy as np
    iris = datasets.load_iris()
    assert iris.data.shape == (150, 4)
    assert np.array_equal(np.unique(iris.target),  [0, 1, 2])
    clf = svm.LinearSVC()
    clf.fit(iris.data, iris.target)
    pred = clf.predict([[5.0, 3.6, 1.3, 0.25]])
    assert pred[0] == 0
    assert misc.face().shape is not None
    return x
```

**说明**

上述代码只是示例，目标是用到上文所说的所有的包。
2. 写完函数后，写一个简单的map。

**说明**

运行时要确保打开isolation，如果在project级别没有打开，也可在运行时打开一个可以设置全局的选项。

```python
from odps import options options.sql.settings = {'odps.isolation.session.enable': True}
```

您也可以在execute方法上指定本次执行打开isolation。 同样，您可以在全局通过options.df.libraries指定用到的包，也可以在execute时指定。这里需要指定所有的包，包括依赖。
3. 调用定义的函数。

```
hints = {
    'odps.isolation.session.enable': True
} libraries = ['python-dateutil.zip', 'pytz.zip', 'six.tar.gz', 'pandas.zip', 'scipy.zip', 'sklearn.zip'] print iris[:1].sepal_length.map(test).execute(hints=hints, libraries=libraries)
```

**总结**

对于要用到的第三方库及其依赖，如果已经上传，可以直接编写代码，并指定用到的libraries即可。否则，需要按照上述操作上传第三方库。 相关代码请参见aliyun-odps-python-sdk。

#### 9.6.13. MapReduce API

本文介绍PyODPS DataFrame的MapReduce API及高级数据处理功能，涵盖自定义Map/Reduce/Combiner逻辑、资源与第三方库引用、数据重排 （Reshuffle）、布隆过滤（Bloom Filter）、透视表（Pivot Table）以及Key-Value字符串转换等操作，方便您处理复杂的分布式计算场景、优化大规模Join性能并灵活进行数据清洗与聚合分析。

#### 使用说明

PyODPS DataFrame支持MapReduce API，您可以分别编写 `map` 和 `reduce` 函数（ `map_reduce` 可以只有 `mapper` 或者 `reducer` 过程）。

**使用示例**

```
>>> #encoding=utf-8 >>> from odps import ODPS >>> from odps import options >>> options.verbose = True >>> o = ODPS('your-access-id', 'your-secret-access-key',project='DMP_UC_dev', endpoint='http://service-corp.odps.aliyun-inc.com/api') >>> def mapper(row): >>> for word in row[0].split(): >>> yield word.lower(), 1 >>> >>> def reducer(keys):
```

`>>> #` 这里使用`list`而不是`cnt=0`，否则h内的`cnt`会被认为是局部变量，其中的赋值无法输出。

```
>>> cnt = [0]
```

`>>> def h(row, done): # done`表示这个`key`已经迭代结束。

```
>>> cnt[0] += row[1] >>> if done: >>> yield keys[0], cnt[0] >>> return h
```

`>>> # zx_word_count`表只有一列，为`STRING`类型。

```
>>> word_count = DataFrame(o.get_table('zx_word_count')) >>> table = word_count.map_reduce(mapper, reducer, group=['word', ],
                        mapper_output_names=['word', 'cnt'],
                        mapper_output_types=['string', 'int'],
                        reducer_output_names=['word', 'cnt'],
                        reducer_output_types=['string', 'int'])
```

# 结果如下：

```
         word  cnt
0 are 1 1 day 1 2 doing? 1 3 everybody 1 4 first 1 5 hello 2 6 how 1 7 is 1 8 so 1 9 the 1 10 this 1 11 world 1 12 you 1
```

| group |  | 参 |
|---|---|---|
| 些 | keys |  |

| 为了方便，此处写成了函数闭包的方式，您也可以写成 | Callable | 的类。 |
|---|---|---|
| class reducer(object): def __init__(self, keys): self.cnt = 0 def __call__(self, row, done): # done表示这个key已经迭代结束。 self.cnt += row.cnt if done: yield row.word, self.cnt |  |  |

使用 `output` 进行注释会让代码更简单。

```
>>> from odps.df import output >>> >>> @output(['word', 'cnt'], ['string', 'int']) >>> def mapper(row): >>> for word in row[0].split(): >>> yield word.lower(), 1 >>> >>> @output(['word', 'cnt'], ['string', 'int']) >>> def reducer(keys):
```

`>>> #` 此处使用`list`而不是`cnt=0`，否则h内的`cnt`会被认为是局部变量，其中的赋值无法输出。

```
>>> cnt = [0]
```

`>>> def h(row, done): # done`表示这个`key`已经迭代结束。

```
>>> cnt[0] += row.cnt >>> if done: >>> yield keys.word, cnt[0] >>> return h >>> >>> word_count = DataFrame(o.get_table('zx_word_count')) >>> table = word_count.map_reduce(mapper, reducer, group='word')
```

# 结果如下：

```
         word  cnt
0 are 1 1 day 1 2 doing? 1 3 everybody 1 4 first 1 5 hello 2 6 how 1 7 is 1 8 so 1 9 the 1 10 this 1 11 world 1 12 you 1
```

**指定COMBINER**

| combiner |  | 表示 |
|---|---|---|
| 且， | combiner |  |

| combiner | 在 | mapper |
|---|---|---|

```
>>> words_df.map_reduce(mapper, reducer, combiner=reducer, group='word')
```

**引用资源**

在MapReduce API里，您可以分别指定 `mapper` 和 `reducer` 所要引用的资源。 以下示例为对 `mapper` 里的单词做停词过滤，在 `reducer` 里对白名单的单词数量加5。

```
>>> white_list_file = o.create_resource('pyodps_white_list_words', 'file', file_obj='Python\nWorld') >>> >>> @output(['word', 'cnt'], ['string', 'int']) >>> def mapper(resources): >>> stop_words = set(r[0].strip() for r in resources[0]) >>> def h(row): >>> for word in row[0].split(): >>> if word not in stop_words: >>> yield word, 1 >>> return h >>> >>> @output(['word', 'cnt'], ['string', 'int']) >>> def reducer(resources): >>> d = dict() >>> d['white_list'] = set(word.strip() for word in resources[0]) >>> d['cnt'] = 0 >>> def inner(keys): >>> d['cnt'] = 0 >>> def h(row, done): >>> d['cnt'] += row.cnt >>> if done: >>> if row.word in d['white_list']: >>> d['cnt'] += 5 >>> yield keys.word, d['cnt'] >>> return h >>> return inner >>> >>> words_df.map_reduce(mapper, reducer, group='word', >>> mapper_resources=[stop_words], reducer_resources=[white_list_file])
```

# 结果如下：

```
     word  cnt
0 hello 2 1 life 1 2 python 7 3 world 6 4 short 1 5 use 1
```

**使用第三方Python库**

使用方法类似在MAP中使用第三方Python库。 在全局指定使用的库。

```
>>> from odps import options >>> options.df.libraries = ['six.whl', 'python_dateutil.whl']
```

在立即执行的方法中，局部指定使用的库。

```
>>> df.map_reduce(mapper=my_mapper, reducer=my_reducer, group='key').execute(libraries=['six.whl', 'python_dateutil.whl'])
```

**说明**

由于字节码定义的差异，Python 3下使用新语言特性（例如 `yield from` ）时，代码在使用Python 2.7的ODPS Worker上执行时会发生错误。因此，建议您在Python 3下使用MapReduce API编写生产作业前，先确认相关代码是否能正常执行。

**重排数据**

| 当数据在集群上分布不均匀时，您可以调用 | reshuffle | 接口对数据重排。 |
|---|---|---|
| >>> df1 = df.reshuffle() |  |  |

默认会按随机数做哈希来分布，但您也可以按指定列做分布，并且可以指定重排后的排序顺序。

```
>>> df1.reshuffle('name', sort='id', ascending=False)
```

**布隆过滤器**

| bloom_filter |  | 接口进行 |
|---|---|---|
| 个列计算的 | sequence1 |  |

分数据并不会参与 `join` 运算）时的大规模 `join` 场景很有用。例如，在 `join` 用户的浏览数据和交易数据时，用户的浏览数据量远大于交易数据量，可以利用交易数据先对浏览数据进行布隆过滤，然后再 `join` 可以很好地提升性能。

```
>>> df1 = DataFrame(pd.DataFrame({'a': ['name1', 'name2', 'name3', 'name1'], 'b': [1, 2, 3, 4]})) >>> df1
```

# 结果如下：

```
       a  b
0 name1 1 1 name2 2 2 name3 3 3 name1 4 >>> df2 = DataFrame(pd.DataFrame({'a': ['name1']})) >>> df2
```

a

```
0 name1
```

`>>> df1.bloom_filter('a', df2.a) #` 这里第0个参数可以是个计算表达式如`: df1.a + '1'`。
# 结果如下：

```
       a  b
0 name1 1 1 name1 4
```

示例说明： 由于数据量很小， `df1` 中的 a 为 `name2` 和 `name3` 的行都被正确过滤掉了，当数据量很大的时候，可能无法过滤全部数据。 之前提 `join` 场景中，少量数据不能被过滤的情况并不会影响数据的正确性，但可以较大地提升 `join` 的性能。 您可以传入 `capacity` 和 `error_rate` 来设置数据的量以及错误率，默认值是 `3000` 和 `0.01` 。

**说明**

要注意，调大 `capacity` 或者减小 `error_rate` 会增加内存的使用，所以应当根据实际情况选择一个合理的值。

**透视表（PIVOT_TABLE）**

```
>>> df
     A    B      C  D  E
0 foo one small 1 3 1 foo one large 2 4 2 foo one large 2 5 3 foo two small 3 6 4 foo two small 3 4 5 bar one large 4 5 6 bar one small 5 3 7 bar two small 6 2 8 bar two large 7 1
```

| 使用透视表功能时， | rows | 参数为必选参数，表示按一个或者多个字段做取平均值的操作。 |
|---|---|---|
| >>> df['A', 'D', 'E'].pivot_table(rows='A') # 结果如下： A D_mean E_mean 0 bar 5.5 2.75 1 foo 2.2 4.40 |  |  |

| rows | 可以提供多个字段，表示按多个字段做聚合。 |
|---|---|
| >>> df.pivot_table(rows=['A', 'B', 'C']) # 结果如下： A B C D_mean E_mean 0 bar one large 4.0 5.0 1 bar one small 5.0 3.0 2 bar two large 7.0 1.0 3 bar two small 6.0 2.0 4 foo one large 2.0 4.5 5 foo one small 1.0 3.0 6 foo two small 3.0 5.0 |  |

| 指定 | values | 显示指定要计算的列。 |
|---|---|---|
| >>> df.pivot_table(rows=['A', 'B'], values='D') # 结果如下： A B D_mean 0 bar one 4.500000 1 bar two 6.500000 2 foo one 1.666667 3 foo two 3.000000 |  |  |

| 计算值列时，默认会计算平均值。通过 | aggfunc | 指定一个或者多个聚合函数。 |
|---|---|---|
| >>> df.pivot_table(rows=['A', 'B'], values=['D'], aggfunc=['mean', 'count', 'sum']) # 结果如下： A B D_mean D_count D_sum 0 bar one 4.500000 2 9 1 bar two 6.500000 2 13 2 foo one 1.666667 3 5 3 foo two 3.000000 2 6 |  |  |

```
>>> df.pivot_table(rows=['A', 'B'], values='D', columns='C')
```

# 结果如下：

```
     A    B  large_D_mean  small_D_mean
0 bar one 4.0 5.0 1 bar two 7.0 6.0 2 foo one 2.0 1.0 3 foo two NaN 3.0
```

| 使用 | fill_value | 填充空值。 |
|---|---|---|
| >>> df.pivot_table(rows=['A', 'B'], values='D', columns='C', fill_value=0) # 结果如下： A B large_D_mean small_D_mean 0 bar one 4 5 1 bar two 7 6 2 foo one 2 1 3 foo two 0 3 |  |  |

**KEY-VALUE字符串转换**

DataFrame提供了将Key-Value对展开为列，以及将普通列转换为Key-Value列的功能。DataFrame创建及其对象操作请参见创建DataFrame。 将Key-Value对展开为列，示例数据如下。

```
>>> df
```

# 结果如下：

```
    name               kv
0 name1 k1=1,k2=3,k5=10 1 name1 k1=7.1,k7=8.2 2 name2 k2=1.2,k3=1.5 3 name2 k9=1.1,k2=1
```

| 通过 | extract_kv | 方法将Key-Value字段展开。 |
|---|---|---|
| >>> df.extract_kv(columns=['kv'], kv_delim='=', item_delim=',') # 结果如下： name kv_k1 kv_k2 kv_k3 kv_k5 kv_k7 kv_k9 0 name1 1.0 3.0 NaN 10.0 NaN NaN 1 name1 7.0 NaN NaN NaN 8.2 NaN 2 name2 NaN 1.2 1.5 NaN NaN NaN 3 name2 NaN 1.0 NaN NaN NaN 1.1 |  |  |

| kv_delim | 和 | item_delim |
|---|---|---|

```
>>> df.extract_kv(columns=['kv'], kv_delim='=', fill_value=0)
```

# 结果如下：

```
   name   kv_k1  kv_k2  kv_k3  kv_k5  kv_k7  kv_k9
0 name1 1.0 3.0 0.0 10.0 0.0 0.0 1 name1 7.0 0.0 0.0 0.0 8.2 0.0 2 name2 0.0 1.2 1.5 0.0 0.0 0.0 3 name2 0.0 1.0 0.0 0.0 0.0 1.1
```

将多列数据转换为一个Key-Value列，示例数据如下。

```
>>> df
```

# 结果如下：

```
   name    k1   k2   k3    k5   k7   k9
0 name1 1.0 3.0 NaN 10.0 NaN NaN 1 name1 7.0 NaN NaN NaN 8.2 NaN 2 name2 NaN 1.2 1.5 NaN NaN NaN 3 name2 NaN 1.0 NaN NaN NaN 1.1
```

通过 `to_kv` 方法转换为Key-Value表示的格式。

```
>>> df.to_kv(columns=['k1', 'k2', 'k3', 'k5', 'k7', 'k9'], kv_delim='=')
```

# 结果如下：

```
    name               kv
0 name1 k1=1,k2=3,k5=10 1 name1 k1=7.1,k7=8.2 2 name2 k2=1.2,k3=1.5 3 name2 k9=1.1,k2=1
```

#### 9.6.14. 数据合并

本文向您介绍DataFrame支持的数据表的JOIN操作、UNION操作等数据合并操作。

**前提条件**

您需要提前导入以下示例表数据，用于操作本文中的示例，其中示例源数据下载请参见数据准备，使用到的两个示例表结构如下。

```
>>> movies = DataFrame(o.get_table('pyodps_ml_100k_movies')) >>> ratings = DataFrame(o.get_table('pyodps_ml_100k_ratings')) >>> movies.dtypes odps.Schema {
  movie_id                            int64
  title                               string
  release_date                        string
  video_release_date                  string
  _url                            string
} >>> ratings.dtypes odps.Schema {
  user_id                     int64
  movie_id                    int64
  rating                      int64
  unix_timestamp              int64
}
```

**JOIN操作**

| 如果不指定 | join | 的条件，则DataFrame API会寻找名字相同的列，并作为 | join | 的条件。 |
|---|---|---|---|---|
| >>> movies.join(ratings).head(3) # 结果如下： movie_id title release_date video_release_date url user_id rating unix_tim stamp 0 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 49 3 888068877 1 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 621 5 881444887 2 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 291 3 874833936 |  |  |  |  |

| 显式指定 | join | 的条件。在 | join | 时，如果 | on | 条件在两表中所选取的字段名称相同，则只会保留其中一个表的此字段。 |
|---|---|---|---|---|---|---|
| >>> movies.join(ratings, on='movie_id').head(3) # 结果如下： movie_id title release_date video_release_date url user_id rating unix_ti estamp 0 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 49 3 888068877 1 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 621 5 881444887 2 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 291 3 874833936 |  |  |  |  |  |  |

| 在执行其他类型的 | join | 操作时，例如 | left_join | ，两表中相同名称的字段会被重命名。 |
|---|---|---|---|---|
| >>> movies.left_join(ratings, on='movie_id').head(3) # 结果如下： movie_id_x title release_date video_release_date url user_id movie_id_y ra ing unix_timestamp 0 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 49 3 3 888068877 1 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 621 3 5 881444887 2 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 291 3 3 874833936 |  |  |  |  |

示例中， `movie_id` 被重命名为 `movie_id_x` 、 `movie_id_y` ，这与 `suffixes` 参数有关，该参数的默认值为 `('_x','_y')` 。当遇到重名的列时，重名的列会被重命名为指定的后缀名。

```
>>> ratings2 = ratings[ratings.exclude('movie_id'), ratings.movie_id.rename('movie_id2')] >>> ratings2.dtypes odps.Schema {
  user_id                     int64
  rating                      int64
  unix_timestamp              int64
  movie_id2                   int64
} >>> movies.join(ratings2, on=[('movie_id', 'movie_id2')]).head(3)
```

# 结果如下：

```
   movie_id              title  release_date  video_release_date                                           url  user_id  rating  unix_tim
stamp movie_id2 0 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 49 3 888068877 3 1 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 621 5 881444887 3 2 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 291 3 874833936 3
```

| 也可以在 | on | 中直接写等于表达式。 |
|---|---|---|
| >>> movies.join(ratings2, on=[movies.movie_id == ratings2.movie_id2]).head(3) # 结果如下： movie_id title release_date video_release_date url user_id rating unix_tim stamp movie_id2 0 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 49 3 888068877 3 1 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 621 5 881444887 3 2 3 Four Rooms (1995) 01-Jan-1995 http://example.aliyundoc.com/M/title-exact?Four%20Rooms%... 291 3 874833936 3 |  |  |

| 在 | self-join | 时，可以调用 | view | 方法分别提取字段。 |
|---|---|---|---|---|
| >>> movies2 = movies.view() >>> movies.join(movies2, movies.movie_id == movies2.movie_id)[movies, movies2.movie_id.rename('movie_id2')].head(3) # 结果如下： movie_id title_x release_date_x video_release_date_x \ 0 2 GoldenEye (1995) 01-Jan-1995 True 1 3 Four Rooms (1995) 01-Jan-1995 True 2 4 Get Shorty (1995) 01-Jan-1995 True url_x movie_id2 0 http://example.aliyundoc.com/M/title-exact?GoldenEye%20(... 2 1 http://example.aliyundoc.comtitle-exact?Four%20Rooms%... 3 2 http://example.aliyundoc.com/M/title-exact?Get%20Shorty%... 4 |  |  |  |  |

| 持 | join | ， |
|---|---|---|
| suffixes |  |  |

| left_join |  |  |
|---|---|---|
| 元 | tuple | 进行 |

| 如果需要在外连接中避免对位次相等的列取重复列，可以指定 | merge_columns | 选项。该选项会自动选择两列中的非空值作为新列的值。 |
|---|---|---|
| >>> movies.left_join(ratings, on='movie_id', merge_columns=True) |  |  |

| mapjoin |  | 设为Tr |
|---|---|---|
| ction进行 | join |  |

**UNION操作**

| 如果两张表的字段和类型都一致（字段的顺序可以不同），则可以使用 | union | 或者 | concat | 将它们合并成一张表。 |
|---|---|---|---|---|
| >>> mov1 = movies[movies.movie_id < 3]['movie_id', 'title'] >>> mov2 = movies[(movies.movie_id > 3) & (movies.movie_id < 6)]['title', 'movie_id'] >>> mov1.union(mov2) # 结果如下： movie_id title 0 1 Toy Story (1995) 1 2 GoldenEye (1995) 2 4 Get Shorty (1995) 3 5 Copycat (1995) |  |  |  |  |

您也可以对分别来自ODPS和Pandas的Collection进行 `union` 操作，或者对分别来自ODPS和数据库的Collection进行 `union` 操作，相关的计算会在ODPS上执行。

#### 9.6.15. 窗口函数

本文介绍 PyODPS DataFrame API 中窗口函数的使用方法，涵盖分组排序、累积计算（如累加、均值、排名）、行间偏移（lag/lead）及自定义窗口范围等核心功能，方便您在无需编写复杂 SQL 的情况下，高效实现行级分析与统计需求。

**命令示例**

```
grouped = iris.groupby('name') grouped.mutate(grouped.sepallength.cumsum(), grouped.sort('sepallength').row_number()).head(10)
```

# 结果如下：

```
          name  sepallength_sum  row_number
0 Iris-setosa 250.3 1 1 Iris-setosa 250.3 2 2 Iris-setosa 250.3 3 3 Iris-setosa 250.3 4 4 Iris-setosa 250.3 5 5 Iris-setosa 250.3 6 6 Iris-setosa 250.3 7 7 Iris-setosa 250.3 8 8 Iris-setosa 250.3 9 9 Iris-setosa 250.3 10
```

窗口函数可以用在列选择中。

```
iris['name', 'sepallength', iris.groupby('name').sort('sepallength').sepallength.cumcount()].head(5)
```

# 结果如下：

```
          name  sepallength  sepallength_count
0 Iris-setosa 4.3 1 1 Iris-setosa 4.4 2 2 Iris-setosa 4.4 3 3 Iris-setosa 4.4 4 4 Iris-setosa 4.5 5
```

窗口函数按标量聚合时，与分组聚合的处理方式一致。

```
from odps.df import Scalar iris.groupby(Scalar(1)).sort('sepallength').sepallength.cumcount()
```

**支持的函数列表**

| 窗口函数 | 说明 |
|---|---|
| cumsum | 计算累积和。 |
| cummean | 计算累积均值。 |
| cummedian | 计算累积中位数。 |
| cumstd | 计算累积标准差。 |
| cummax | 计算累积最大值。 |
| cummin | 计算累积最小值。 |
| cumcount | 计算累积和。 |
| lag | 按偏移量取当前行之前第几行的值。如果当前行号为rn，则取行号为rn-offset的值。 |
| lead | 按偏移量取当前行之后第几行的值。如果当前行号为rn则取行号为rn+offset的值。 |
| rank | 计算排名。 |
| denserank _ | 计算连续排名。 |
| percentrank _ | 计算一组数据中某行的相对排名。 |
| rownumber _ | 计算行号，从1开始。 |
| qcut | 将分组数据按顺序切分成n片，并返回当前切片值。如果切片不均匀，默认增加第一个切片的分布。 |

| nthvalue _ | 返回分组中的第n个值。 |
|---|---|
| cumedist _ | 计算分组中值小于等于当前值的行数占分组总行数的比例。 |

**参数说明**

各个窗口函数支持的参数说明如下。

| rank | row_number |
|---|---|
| 参数名 | 说明 |
| sort | 排序关键字，默认为空。 |
| ascending | 排序时，是否依照升序排序，默认值为True。 |

| lag 和 lead 除了支持 rank 所支持的参数，还支持下列参数。 |  |
|---|---|
| 参数名 | 说明 |
| offset | 取数据的行距离当前行的行数。 |
| default | 当offset指定的行不存在时的返回值。 |

| cumsum | 、 | cummax | 、 | cummin | 、 | cummean |  | 、 | cummedian | 、 | cumcount | 和 | cumstd | 除了支持 | rank | 所支持的参数外，还支持下列参数。 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 参数名 |  |  |  |  |  |  | 说明 |  |  |  |  |  |  |  |  |  |
| unique |  |  |  |  |  |  | 是否排除重复值，默认False。 |  |  |  |  |  |  |  |  |  |
| preceding |  |  |  |  |  |  | 窗口范围起点。 |  |  |  |  |  |  |  |  |  |
| following |  |  |  |  |  |  | 窗口范围终点。 |  |  |  |  |  |  |  |  |  |

**9.6.16. 绘图**

#### 使用说明

如果您需要使用绘图功能，请先安装Pandas和Matplotlib。 您可以在Jupyter中运行以下示例代码，并使用 `pip install matplotlib` 命令安装Matplotlib。

**绘图**

单线图

```xml
>>> %matplotlib inline >>> iris.sepalwidth.plot() <matplotlib.axes._subplots.AxesSubplot at 0x10c2b3510>
```

多线图

```xml
>>> iris.plot() <matplotlib.axes._subplots.AxesSubplot at 0x10db7e690>
```

竖向柱状图

```xml
>>> iris.groupby('name').sum().plot(kind='bar', x='name', stacked=True, rot=30) <matplotlib.axes._subplots.AxesSubplot at 0x10c5f2090>
```

直方图

```xml
>>> iris.hist(sharex=True) array([[<matplotlib.axes._subplots.AxesSubplot object at 0x10e013f90>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x10e2d1c10>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x10e353f10>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x10e3c4410>]], dtype=object)
```

**参数说明**

| 参数 kind 表示绘图的类型，支持的绘图类型如下表所示。详细的参数说明请参见pandas.DataFrame.plot。 |  |
|---|---|
| kind | 说明 |
| line | 线图。 |
| bar | 竖向柱状图。 |
| barh | 横向柱状图。 |
| hist | 直方图。 |
| box | Box图。 |
| kde | 核密度估计。 |
| density | 和Kde相同。 |
| area | Area图。 |

| pie | 饼图。 |
|---|---|
| scatter | 散点图。 |
| hexbin | Hexbin图。 |

| 除上表所示参数外， plot 函数还增加了以下几种参数，方便进行绘图。 |  |
|---|---|
| 参数 | 说明 |
| xlabel | X轴名。 |
| ylabel | Y轴名。 |
| xlabelsize | X轴名大小。 |
| ylabelsize | Y轴名大小。 |
| labelsize | 轴名大小。 |
| title | 标题。 |
| titlesize | 标题大小。 |
| annotate | 是否标记值。 |

#### 9.6.17. 调试指南

由于PyODPS DataFrame本身会对整个操作执行优化，为了更直观地反映整个过程，您可以使用可视化的方式显示整个表达式的计算过程。 可视化需要依赖graphviz软件和graphvizPython包。

```
>>> df = iris.groupby('name').agg(id=iris.sepalwidth.sum()) >>> df = df[df.name, df.id + 3] >>> df.visualize()
```

| 由上图可见，这个计算过程中，PyODPS DataFrame将 | groupby | 和列筛选做了操作合并。 |
|---|---|---|
| >>> df = iris.groupby('name').agg(id=iris.sepalwidth.sum()).cache() >>> df2 = df[df.name, df.id + 3] >>> df2.visualize() |  |  |

此时，由于执行了Cache操作，整个执行计划将会分成两步执行。

**ODPS SQL后端查看编译结果**

| 您可以直接调用 | compile | 方法查看ODPS SQL后端编译到SQL的结果。 |
|---|---|---|
| >>> df = iris.groupby('name').agg(sepalwidth=iris.sepalwidth.max()) >>> df.compile() Stage 1: SQL compiled: SELECT t1.`name`, MAX(t1.`sepalwidth`) AS `sepalwidth` FROM test_pyodps_dev.`pyodps_iris` t1 GROUP BY t1.`name` |  |  |

**使用Pandas计算后端执行本地调试**

对于来自ODPS表的DataFrame，部分操作不会编译到ODPS SQL执行，而会使用Tunnel下载表数据。这个下载的过程很快，且无需等待ODPS SQL任务的调度。利用这个特性，您可以快速下载小部分ODPS数据到本地，使用Pandas计算后端进行代码编写和调试。这些操作包括： 非分区表：对其进行选取全部或有限条数据、列筛选的操作（不包括列的各种计算），以及计算其数量。 不选取分区或筛选前几个分区字段的分区表：对其选取全部或有限条数据、列筛选的操作，以及计算其数量。

| 例如 | iris | 这个DataFrame来自非分区表，以下操作会使用Tunnel进行下载。 |
|---|---|---|
| >>> iris.count() >>> iris['name', 'sepalwidth'][:10] |  |  |

| 例如有个DataFrame来自分区表（有三个分区字段，即 | ds | 、 | hh | 、 | mm | ），以下操作会使用Tunnel下载。 |
|---|---|---|---|---|---|---|
| >>> df[:10] >>> df[df.ds == '20160808']['f0', 'f1'] >>> df[(df.ds == '20160808') & (df.hh == 3)][:10] >>> df[(df.ds == '20160808') & (df.hh == 3) & (df.mm == 15)] |  |  |  |  |  |  |

因此您可以使用 `to_pandas` 方法将部分数据下载到本地进行调试。

```
>>> DEBUG = True >>> if DEBUG: >>> df = iris[:100].to_pandas(wrap=True) >>> else: >>> df = iris
```

最后把 `DEBUG` 设置为False，便可以在ODPS上执行完整的计算。

**说明**

由于沙箱的限制，本地调试通过的程序不一定能在ODPS上也跑通。

### 配置选项

本文介绍PyODPS的全局配置选项体系，涵盖通用连接参数（如Endpoint、超时重试）、Tunnel数据传输策略、DataFrame执行优化（如谓词下推、列剪裁、排序限制）及机器学习任务设置，方便您根据运行环境灵活调整行为，以优化任务性能、控制资源消耗并确保数据处理的准确性。

```python
from odps import options
```

# 设置所有输出表的生命周期（`lifecycle`选项）。

```
options.lifecycle = 30
```

# 使用`Tunnel`下载`string`类型时使用`bytes`（`tunnel.string_as_binary`选项）。

```
options.tunnel.string_as_binary = True
```

# 用`ODPS`执行`PyODPS DataFrame`时，可以参照下面`dataframe`相关配置，在`sort`时将`limit`设置为一个比较大的值。

```
options.df.odps.sort.limit = 100000000
```

**通用配置**

| 选项 | 说明 | 默认值 |
|---|---|---|
| endpoint _ | ODPS Endpoint。 | None |
| defaultproject _ | 默认Project。 | None |
| logviewhost _ _ | LogView主机名。 | None |
| logviewhours _ _ | LogView保持时间，单位：小时（h）。 | 24 |
| localtimezone _ | 使用的时区。True表示本地时间，False表示UTC，也可用 pytz 的时区。 | None |
| lifecycle | 所有表生命周期。 | None |
| templifecycle _ | 临时表生命周期。 | 1 |
| bizid _ | 用户ID。 | None |
| verbose | 是否打印日志。 | False |
| verboselog _ | 日志接收器。 | None |
| chunksize _ | 写入缓冲区大小，单位：Byte。 | 1496 |
| retrytimes _ | 请求重试次数。 | 4 |
| poolconnections _ | 缓存在连接池的连接数。 | 10 |
| poolmaxsize _ | 连接池最大容量。 | 10 |
| connecttimeout _ | 连接超时，单位：秒（s）。 | 5 |
| readtimeout _ | 读取超时，单位：秒（s）。 | 120 |
| apiproxy _ | API代理服务器。 | None |
| dataproxy _ | 数据代理服务器。 | None |
| completionsize _ | 对象补全列举条数限制。 | 10 |
| notebookreprwidget _ _ | 使用交互式图表。 | True |
| sql.settings | ODPS SQL运行全局hints。 | None |
| sql.useodps2extension _ _ | 启用MaxCompute 2.0语言扩展。 | False |

**数据上传下载配置**

| 选项 | 说明 | 默认值 |
|---|---|---|
| tunnel.endpoint | Tunnel的Endpoint。 | None |

| tunnel.useinstancetunnel _ _ | 使用Instance Tunnel获取执行结果。 | True |
|---|---|---|
| tunnel.limitinstancetunnel _ _ | 是否限制Instance Tunnel获取结果的条数。 | None |
| tunnel.stringasbinary _ _ | 在STRING类型中使用Bytes而非Unicode。 | False |

| 选项 | 说明 | 默认值 |
|---|---|---|
| interactive | 是否在交互式环境。 | 根据检测值。 |
| df.analyze | 是否启用非ODPS内置函数。 | True |
| df.optimize | 是否开启DataFrame全部优化。 | True |
| df.optimizes.pp | 是否开启DataFrame谓词下推优化。 | True |
| df.optimizes.cp | 是否开启DataFrame列剪裁优化。 | True |
| df.optimizes.tunnel | 是否开启DataFrame使用Tunnel优化执行。 | True |
| df.quote | ODPS SQL后端是否用 `` 来标记字段和表名。 | True |
| df.libraries | DataFrame运行使用的第三方库（资源名）。 | None |
| df.supersedelibraries _ | 使用自行上传的Numpy替换服务中的版本。 | False |
| df.odps.sort.limit | DataFrame有排序操作时，默认添加的Limit条数。 | 10000 |

**机器学习配置**

| 选项 | 说明 | 默认值 |
|---|---|---|
| ml.xflowsettings _ | Xflow执行配置。 | None |
| ml.xflowproject _ | 默认Xflow工程名。 | algopublic _ |
| ml.usemodeltransfer _ _ | 是否使用ModelTransfer获取模型PMML。 | False |
| ml.modelvolume _ | 在使用ModelTransfer时使用的Volume名称。 | pyodpsvolume _ |

### PyODPS制作第三方包

| pyodps-pack |  | 命令行 |
|---|---|---|
| 一个后缀为 | .tar.gz |  |

**环境准备**

pyodps-pack命令需要在操作系统命令行（Windows CMD或者macOS/Linux Shell）中执行，DataWorks和odpscmd中不能调用。

**Docker模式**

您需要安装Docker以顺利使用Docker模式运行 `pyodps-pack` ， `pyodps-pack` 会自动调用已安装的Docker，您无需手动在Docker中运行 `pyodps-pack` 。 Linux环境：可以参考Docker官方文档安装Docker。 macOS或Windows环境： 个人开发者：可以使用Docker Desktop。 未购买过授权的企业用户：推荐使用开源的Rancher Desktop。

**说明**

我们没有在包括 `minikube` 在内的其他Docker环境中测试 `pyodps-pack` ，不保证在这些环境中的可用性。 对于Windows用户，可能您的Docker服务需要依赖Windows系统的Server服务才能启动，而Server服务由于安全问题在很多企业被禁止启动。在遇到问题时，请改用Linux打包或者设法启用Server服务。Rancher Desktop在Windows 10下可能无法使用 `containerd` 作为容器引擎，可以尝试改用 `dockerd` ，配置详情请参考Container Engine。 对于专有云环境，如果您的MaxCompute或DataWorks基于Arm64机型部署，您需要额外增加 `--arch aarch64` 参数指定打包需要的架构。通常Docker Desktop 或Rancher Desktop已经安装了跨平台打包所需的 `binfmt` 相关组件，您也可以使用以下命令安装相关的虚拟环境。

```bash
docker run --privileged --rm tonistiigi/binfmt --install arm64
```

**说明**

上述命令要求Linux Kernel版本高于4.8，具体请参考binfmt。

**无Docker模式**

**说明**

建议您在打包时，尽量使用Docker模式。非Docker模式仅用于Docker不可用的场景，且生成的包有可能不可用。 如果您安装Docker遇到困难，可以尝试使用非Docker模式。使用方式为新增一个 `--without-docker` 参数。该模式需要在您的Python环境中已经安装pip。如果使用该模式出现错误，请改用Docker模式。Windows用户需要安装Git Bash以使用该模式，Git Bash包含在Git for Windows中。

**打包操作**

| 您可以使用 | pyodps-pack | 命令在本地PyODPS环境中执行打包操作，其中包括打包所有依赖、打包自定义代码、打包Git Repo中的代码及打包二进制依赖。 |
|---|---|---|
| 说明请勿在Docker环境中执行 pyodps-pack 命令。 |  |  |

**使用限制**

MaxCompute建议除非不得已，新项目请尽量使用Python 3。我们不保证下面打包步骤对Python 2的可用性。 旧项目请尽量迁移至Python 3以减少后续维护的难度。 在Linux中使用下列命令时，请使用 `sudo` 调用 `pyodps-pack` 以保证Docker正常运行。

**打包所有依赖**

安装完PyODPS后，您可以在本地PyODPS环境中使用以下命令为Python 3打包pandas及所有pandas的依赖项： 使用Docker模式打包： 使用非Docker模式打包： 打包时指定所需版本：

| 经过一系列的打包步骤，工具会显示包中的所有依赖版本，具体如下。并在当前目录中生成一个 | packages.tar.gz | 文件，其中包括下面列出的所有依赖项目。 |
|---|---|---|
| Package Version --------------- ------- numpy 1.21.6 pandas 1.2.5 python-dateutil 2.8.2 pytz 2022.6 six 1.16.0 |  |  |

如果您希望为Python 2.7打包，请确定包的后续使用环境为MaxCompute还是DataWorks，辨别方法请参考PyODPS DataFrame的代码运行环境。 在MaxCompute中使用Python 2.7包的打包命令： 在DataWorks中使用Python 2.7包的打包命令：

**打包自定义代码**

| pyodps-pack |  | 支持打包使 |
|---|---|---|
| 以基于 | pyproject.toml |  |

```
test_package_root ├── test_package │ ├── __init__.py │ ├── mod1.py │ └── subpackage │ ├── __init__.py │ └── mod2.py └── pyproject.toml
```

| 其中 | pyproject.toml | 内容可能为： |
|---|---|---|
| [project] name = "test_package" description = "pyodps-pack example package" version = "0.1.0" dependencies = [ "pandas>=1.0.5" ] |  |  |

| 完成包的开发后，使用以下命令可以将此包和所有依赖打包进 | packages.tar.gz | 文件中（ | path_to_package | 为 | test_package_root | 的上级路径）： |
|---|---|---|---|---|---|---|
| pyodps-pack /<path_to_package>/test_package_root |  |  |  |  |  |  |

**打包Git Repo中的代码**

| pyodps-pack | 支持打包远程Git代码仓库（例如GitHub）中的代码。以PyODPS本身为例，可以使用以下命令执行打包： |
|---|---|
| pyodps-pack git+https://github.com/aliyun/aliyun-odps-python-sdk.git |  |

如果想要打包某个分支或者Tag，可以使用：

```
pyodps-pack git+https://github.com/aliyun/aliyun-odps-python-sdk.git@v0.11.2.2
```

| cython | ），可以使用 | --install-requires |
|---|---|---|

```
    --install-requires cython \
    git+https://github.com/aliyun/aliyun-odps-python-sdk.git@v0.11.2.2
```

| 也可以创建一个 | install-requires.txt | 文件并依照 | requirements.txt | 格式编写如下： |
|---|---|---|---|---|
| cython>0.29 |  |  |  |  |

打包命令可以写成：

```
    --install-requires-file install-requires.txt \
    git+https://github.com/aliyun/aliyun-odps-python-sdk.git@v0.11.2.2
```

**更复杂的例子：二进制依赖**

一部分包包含额外的二进制依赖，例如需要编译或安装的外部动态链接库。 `pyodps-pack` 提供了 `--run-before` 参数用以指定打包前需要执行的步骤，该步骤中可以安装所需的二进制依赖。下面以地理信息库GDAL为例为您介绍如何打包。
1. 确定打包时需要安装的二进制依赖。

| CMake打包。据此，编写二进制包安装文件并保存为 | install-gdal.sh | ： |
|---|---|---|
| #!/bin/bash set -e cd /tmp curl -o proj-6.3.2.tar.gz https://download.osgeo.org/proj/proj-6.3.2.tar.gz tar xzf proj-6.3.2.tar.gz cd proj-6.3.2 mkdir build && cd build cmake .. cmake --build . cmake --build . --target install cd /tmp curl -o gdal-3.6.0.tar.gz http://download.osgeo.org/gdal/3.6.0/gdal-3.6.0.tar.gz tar xzf gdal-3.6.0.tar.gz cd gdal-3.6.0 mkdir build && cd build cmake .. cmake --build . cmake --build . --target install |  |  |

| 使用 | pyodps-pack | 进行打包，命令如下： |
|---|---|---|
| pyodps-pack --install-requires oldest-supported-numpy --run-before install-gdal.sh gdal==3.6.0 |  |  |

**命令详情**

| 下面列出 pyodps-pack 命令的可用参数，可用于控制打包过程： 参数名称描述 -r ， --requirement <file> 根据给定的依赖文件打包。该选项可被指定多次。 -o ， --output <file> 指定打包生成目标文件名，默认为 packages.tar.gz 。 --install-requires <item> 指定打包时所需的PyPI依赖，可指定多个，一般用于命令行中。这些依赖不一定会包含在最终的包中。 --install-requires-file <file> 指定打包时所需的PyPI依赖定义文件，可指定多个。这些依赖不一定会包含在最终的包中。 --run-before <script-file> 指定打包前需要执行的Bash脚本，通常可用于安装二进制依赖。 -x ， --exclude <dependency> 指定打包时需要从最终包删除的PyPI依赖。该选项可被指定多次。 --no-deps 指定打包时不包含指定项目的依赖项。 指定打包时所需的PyPI URL。如果缺省，会使用 pip config list 命令返回的 global.index- -i ， --index-url <index-url> url 值，该值通常配置在 pip.conf 配置文件中。 --trusted-host <host> 指定打包时需要忽略证书问题的HTTPS域名。 -l ， --legacy-image 指定后，将使用CentOS 5镜像进行打包，这使得包可以被用在旧版专有云等环境中。 --mcpy27 指定后，将为MaxCompute内的Python 2.7制作三方包。如果启用，将默认 --legacy-image 选项开启。 --dwpy27 指定后将为DataWorks内的Python 2.7制作三方包。如果启用。将默认 --legacy-image 选项开启。 --prefer-binary 指定后，将倾向于选择PyPI中包含二进制编译的旧版，而不是仅有源码包的新版。 指定目标包面向的硬件架构，目前仅支持x86 _64和AArch64（或ARM64），默认为x86 _64。如果您不在专有云 --arch <architecture> 使用MaxCompute或DataWorks，则不需要指定该参数。 指定目标包面向的Python版本，可使用3.6或者36表示Python 3.6。如果您不在专有云使用MaxCompute或 --python-version <version> DataWorks，则不需要指定该参数。 指定在执行Docker命令时需要额外附加的参数。如有多个参数需用引号包裹，例如 --docker-args"--ip --docker-args <args> 192.168.1.10" 。 --without-docker 使用无Docker模式运行 pyodps-pack 。当依赖中存在二进制依赖，可能报错或导致包不可用。 --without-merge 下载或生成Wheel包后不生成 .tar.gz 包，而是保留 .whl 文件。 --debug 指定后，将输出命令运行的详细信息，用于排查问题。 |  |  |  |
|---|---|---|---|
| 参数名称 | 描述 |  |  |
| -r ， --requirement <file> | 根据给定的依赖文件打包。该选项可被指定多次。 |  |  |
| -o ， --output <file> | 指定打包生成目标文件名，默认为 packages.tar.gz 。 |  |  |
| --install-requires <item> | 指定打包时所需的PyPI依赖，可指定多个，一般用于命令行中。这些依赖不一定会包含在最终的包中。 |  |  |
| --install-requires-file <file> | 指定打包时所需的PyPI依赖定义文件，可指定多个。这些依赖不一定会包含在最终的包中。 |  |  |
| --run-before <script-file> | 指定打包前需要执行的Bash脚本，通常可用于安装二进制依赖。 |  |  |
| -x ， --exclude <dependency> | 指定打包时需要从最终包删除的PyPI依赖。该选项可被指定多次。 |  |  |
| --no-deps | 指定打包时不包含指定项目的依赖项。 |  |  |
| -i ， --index-url <index-url> | 指定打包时所需的PyPI URL。如果缺省，会使用 pip config list 命令返回的 global.index- url 值，该值通常配置在 pip.conf 配置文件中。 |  |  |
| --trusted-host <host> | 指定打包时需要忽略证书问题的HTTPS域名。 |  |  |
| -l ， --legacy-image | 指定后，将使用CentOS 5镜像进行打包，这使得包可以被用在旧版专有云等环境中。 |  |  |
| --mcpy27 | 指定后，将为MaxCompute内的Python 2.7制作三方包。如果启用，将默认 --legacy-image 选项开启。 |  |  |
| --dwpy27 | 指定后将为DataWorks内的Python 2.7制作三方包。如果启用。将默认 --legacy-image 选项开启。 |  |  |
| --prefer-binary | 指定后，将倾向于选择PyPI中包含二进制编译的旧版，而不是仅有源码包的新版。 |  |  |
| --arch <architecture> | 指定目标包面向的硬件架构，目前仅支持x8664和AArch64（或ARM64），默认为x8664。如果您不在专有云 _ _ 使用MaxCompute或DataWorks，则不需要指定该参数。 |  |  |
| --python-version <version> | 指定目标包面向的Python版本，可使用3.6或者36表示Python 3.6。如果您不在专有云使用MaxCompute或 DataWorks，则不需要指定该参数。 |  |  |
| --docker-args <args> | 指定在执行Docker命令时需要额外附加的参数。如有多个参数需用引号包裹，例如 --docker-args"--ip 192.168.1.10" 。 |  |  |
|  |  | --docker-args"--ip |  |
| --without-docker | 使用无Docker模式运行 pyodps-pack 。当依赖中存在二进制依赖，可能报错或导致包不可用。 |  |  |
| --without-merge | 下载或生成Wheel包后不生成 .tar.gz 包，而是保留 .whl 文件。 |  |  |
| --debug | 指定后，将输出命令运行的详细信息，用于排查问题。 |  |  |

|  | url |
|---|---|

|  | 192.168.1.10" |
|---|---|

### 场景实践

#### 9.9.1. PyODPS DataFrame的代码运行环境

使用PyODPS DataFrame编写数据应用时，同一个脚本文件中的代码会在不同位置执行，可能导致一些无法预期的问题，本文为您介绍当出现相关问题时，如何确定代码的执行环境，以及提供部分场景下的解决方案。

**概述**

PyODPS是一个Python包而非Python Implementation，其运行环境均为未经修改的Python，因而并不会出现与正常Python解释器不一致的行为。即您所编写的每一条语句都与标准Python语句行为相同，例如自动变成分布式代码等。 代码示例

```java
from odps import ODPS, options import numpy as np o = ODPS(...) coeffs = [0.1, 0.2, 0.4] def handle(v):
    import numpy as np
    return float(np.cosh(v)) * sum(coeffs)
options.df.supersede_libraries = True val = df.sepal_length.map(handle).sum().execute(libraries=['numpy.zip', 'other.zip']) print(np.sinh(val))
```

代码执行系统下图是上述代码执行时可能涉及的系统。代码本身执行的系统都位于MaxCompute外部，为了方便表述，下文统称为**本地**。 代码分析引用第三方包在本地执行的代码包括handle函数之外的部分（注意handle传入map时仅传入了函数本身而并未执行）。因而，这些代码在执行时，行为与普通Python code的执行行为类似，导入第三方包时，引用的是本地的包。上述代码中， `libraries=['numpy.zip', 'other.zip']` 中引用的 `other.zip` 因为并没有在本地安装，如果代码中有诸如 `import other` 的语句，则会导致执行报错。即便 `other.zip` 已被上传至MaxCompute资源也是如此，因为本地不存在 `other.zip` 包。理论上，本地代码如果不涉及PyODPS包，则与PyODPS无关，执行报错时您需要自行排查。 handle函数 handle函数传入map方法时，如果使用的后端是MaxCompute后端，会经历以下几个阶段： a. 会先被cloudpickle模块提取闭包和字节码。 b. PyODPS DataFrame使用闭包和字节码生成一个Python UDF，提交至MaxCompute。 c. 作业以SQL的形式在MaxCompute执行时，会调用已生成的Python UDF，其中的字节码和闭包内容会被unpickle（反序列化），然后在MaxCompute Executor执行。 总结 handle函数体中的代码都不会在本地执行，而是在MaxCompute Executor中执行。 handle函数体中无法引用本地安装的包，只有在MaxCompute Executor中存在的包才有效。 上传的第三方包必须能够在MaxCompute Executor的Python版本（目前为Python 2.7，UCS2）中调用。 handle函数体中修改引用的外部变量（例如上述代码中的 `coeffs` ）不会导致本地的coeffs值被修改。 如果在handle函数体中引用在handle外import的包可能会报错，因为在不同环境中，包的结构可能不同，而cloudpickle会将本地包的引用代入 MaxCompute Executor，导致报错，因而建议import在handle函数体中进行。 由于使用cloudpickle，如果在handle函数体中调用了其他文件的代码，该文件所在的包必须存在于MaxCompute Executor中。如果您不想使用第三方包的形式解决该问题，请将所有引用的个人代码放在同一个文件中。 上述handle函数的解释对于自定义聚合、apply和map_reduce中调用的自定义方法/Agg类均适用。如果使用的后端是Pandas后端，则所有代码都会在本地运行，因而本地也需要安装相关的包。但鉴于Pandas后端调试完毕后通常会转移到MaxCompute运行，建议在本地安装包的同时，参照MaxCompute后端的惯例进行开发。 个人电脑/自有服务器：在本地使用第三方包或其他文件中的代码时，在相应的Python版本上安装即可。 Notebook：在本地代码中使用第三方包或其他文件中的代码请咨询平台提供方。

| DataWorks：DataWorks不支持在本地安装第三方包，但可以进行调用。对于其他文件中的代码，可以通过读取文件+ | exec | 命令的方式在本地进行使用。 |
|---|---|---|
| 重要 DataStudio中的目录结构并非文件系统中真实存在的目录结构，直接import或打开DataStudio中显示的文件路径会导致执行失败。 在DataWorks中上传资源后，需要点击提交确保资源被正确上传到ODPS。 如果需要使用自己的Numpy版本，在上传正确的wheel包的同时，需要配置 odps.df.supersede_libraries = True ，同时确保您上传的Numpy包名作为libraries的第一个参数。 |  |  |

**引用其他MaxCompute表中的数据**

个人电脑/自有服务器：在本地访问MaxCompute表，如果Endpoint可以连接，使用PyODPS/DataFrame访问。 Notebook/DataWorks：在本地代码中访问MaxCompute表，如果Endpoint可以连接，使用PyODPS/DataFrame访问。连接Endpoint时出现问题请咨询平台提供方。 map/apply/map_reduce/自定义聚合：访问其他MaxCompute表，MaxCompute Executor中通常不支持访问Endpoint/Tunnel Endpoint，也没有PyODPS包可用，因而不能直接使用ODPS入口对象或者PyODPS DataFrame，也不能从自定义函数外部传入这些对象。如果表的数据量不大，建议将DataFrame作为资源传入，详情请参见引用资源。如果数据量较大，建议改写为表JOIN。

#### 9.9.2. PyODPS使用第三方包

本文介绍如何在PyODPS中使用第三方Python包，涵盖通过 `pyodps-pack` 打包依赖、上传资源以及在UDF或DataFrame任务中调用的核心步骤，方便您扩展 MaxCompute 的计算能力以支持复杂的数据分析需求。

**前提条件**

已开通MaxCompute产品。 已开通DataWorks产品。

**上传三方包**

使用三方包前，请确保您生成的包已被上传至MaxCompute Archive资源。上传方式如下：

| 使用代码上传资源。您需要将 | packages.tar.gz | 替换成目标包所在的路径和文件名： |
|---|---|---|
| import os from odps import ODPS # 确保 ALIBABA_CLOUD_ACCESS_KEY_ID 环境变量设置为用户 Access Key ID， # ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 Access Key Secret， # 不建议直接使用 Access Key ID / Access Key Secret 字符串 o = ODPS( os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), project='<your-default-project>', endpoint='<your-end-point>', ) o.create_resource("test_packed.tar.gz", "archive", fileobj=open("packages.tar.gz", "rb")) |  |  |

使用DataWorks上传资源。具体操作请参见DataWorks文档。

**在Python UDF中使用三方包**

您需要对UDF进行修改以使用上传的三方包。具体如下：
1. 在UDF类的 `_init_` 方法中添加对三方包的引用。
2. 在UDF代码（例如evaluate或process方法）中调用三方包。

**具体示例**

下面以实现scipy中的psi函数为例，为您介绍如何在Python UDF中使用三方包。
1. 使用以下命令打包scipy。

| 编写以下代码，并将其保存为 | test_psi_udf.py | 。 |
|---|---|---|
| import sys from odps.udf import annotate @annotate("double->double") class MyPsi(object): def __init__(self): # 将路径增加到引用路径 sys.path.insert(0, "work/scipy-bundle.tar.gz/packages") def evaluate(self, arg0): # 将 import 语句保持在 evaluate 函数内部 from scipy.special import psi return float(psi(arg0)) |  |  |

**说明**

代码解释： `__init__` 函数中将 `work/scipy-bundle.tar.gz/packages` 添加至 `sys.path` ，因为MaxCompute会将所有UDF引用的Archive资源以资源名称为目录解压至 `work` 目录下，而 `packages` 则是 `pyodps-pack` 生成包的子目录。而将对scipy的import放在evaluate函数体内部的原因是三方包仅在执行时可用，当UDF在MaxCompute服务端被解析时，解析环境不包含三方包，函数体外的三方包import会导致报错。

| test_psi_udf.py |  | 上传为M |
|---|---|---|
| 建UDF名为 | test_psi_udf |  |

| scipy-bundle.tar.gz |  | 上传为 |
|---|---|---|
| 类名为 | test_psi_udf.MyPsi |  |

```java
import os from odps import ODPS
```

# 确保 `ALIBABA_CLOUD_ACCESS_KEY_ID` 环境变量设置为用户 `Access Key ID`，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 `Access Key Secret`，
# 不建议直接使用 `Access Key ID / Access Key Secret` 字符串

```
o = ODPS(
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    project='<your-default-project>',
    endpoint='<your-end-point>',
```

)

```
bundle_res = o.create_resource(
    "scipy-bundle.tar.gz", "archive", fileobj=open("scipy-bundle.tar.gz", "rb")
```

)

```
udf_res = o.create_resource(
    "test_psi_udf.py", "py", fileobj=open("test_psi_udf.py", "rb")
```

)

```
o.create_function(
    "test_psi_udf", class_type="test_psi_udf.MyPsi", resources=[bundle_res, udf_res]
```

)

```
add archive scipy-bundle.tar.gz; add py test_psi_udf.py; create function test_psi_udf as test_psi_udf.MyPsi using test_psi_udf.py,scipy-bundle.tar.gz;
```

5. 完成以上操作后，即可使用UDF执行SQL。

```
set odps.pypy.enabled=false; set odps.isolation.session.enable=true; select test_psi_udf(sepal_length) from iris;
```

PyODPS DataFrame支持在execute或persist时使用 `libraries` 参数使用上面的第三方库。下面以map方法为例，apply或map_reduce方法的过程类似。
1. 使用以下命令打包scipy。

| 假定表名为 | test_float_col | ，内容只包含一列FLOAT值： |
|---|---|---|
| col1 0 3.75 1 2.51 |  |  |

| 计算 | psi(col1) | 的值，代码如下： |
|---|---|---|
| import os from odps import ODPS, options def psi(v): from scipy.special import psi return float(psi(v)) # 如果 Project 开启了 Isolation，下面的选项不是必需的 options.sql.settings = {"odps.isolation.session.enable": True} # 确保 ALIBABA_CLOUD_ACCESS_KEY_ID 环境变量设置为用户 Access Key ID， # ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 Access Key Secret， # 不建议直接使用 Access Key ID / Access Key Secret 字符串 o = ODPS( os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), project='<your-default-project>', endpoint='<your-end-point>', ) df = o.get_table("test_float_col").to_df() # 直接执行并取得结果 df.col1.map(psi).execute(libraries=["scipy-bundle.tar.gz"]) # 保存到另一张表 df.col1.map(psi).persist("result_table", libraries=["scipy-bundle.tar.gz"]) |  |  |

3. （可选）如果希望在整个执行过程中使用相同的三方包，可以设置全局选项：

```python
from odps import options options.df.libraries = ["scipy-bundle.tar.gz"]
```

**在DataWorks中使用三方包**

DataWorks PyODPS节点预置了若干三方包，同时提供了 `load_resource_package` 方法用以引用其他的包，具体使用方式请参见使用三方包。

**手动上传和使用三方包**

**说明**

以下内容仅作为维护旧项目或者旧环境的参考，新项目建议直接使用 `pyodps-pack` 打包。 部分旧项目可能采用了之前的方式使用三方包，即手动上传所有依赖的Wheel包并在代码中引用，或者使用了不支持二进制包的旧版MaxCompute环境，本节内容为该场景准备。下面以在map中使用python_dateutil为例为您介绍使用三方包的步骤。
1. 在Linux Bash中使用 `pip download` 命令，下载包及其依赖到某个路径。下载后会出现两个包，即 `six-1.10.0-py2.py3-none-`

```
any.whl 和 python_dateutil-2.5.3-py2.py3-none-any.whl 。 pip download python-dateutil -d /to/path/
```

**说明**

您需要下载支持Linux环境的包，建议直接在Linux下调用该命令。
2. 将上述已下载的两个包分别上传至ODPS资源。
方式一：通过代码上传。
# 这里要确保资源名的后缀是正确的文件类型

```
odps.create_resource('six.whl', 'file', file_obj=open('six-1.10.0-py2.py3-none-any.whl', 'rb')) odps.create_resource('python_dateutil.whl', 'file', file_obj=open('python_dateutil-2.5.3-py2.py3-none-any.whl', 'rb'))
```

方式二：通过DataWorks界面上传。 您可以参考DataWorks文档完成目标资源的上传与提交。
3. 使用三方包。

```
>>> df
               datestr
0 2016-08-26 14:03:29 1 2015-08-26 14:03:29
```

全局配置使用到的三方库如下：

```
>>> from odps import options >>> >>> def get_year(t): >>> from dateutil.parser import parse >>> return parse(t).strftime('%Y') >>> >>> options.df.libraries = ['six.whl', 'python_dateutil.whl'] >>> df.datestr.map(get_year)
   datestr
0 2016 1 2015
```

| 通过立即运行方法的 | libraries | 参数指定： |
|---|---|---|
| >>> def get_year(t): >>> from dateutil.parser import parse >>> return parse(t).strftime('%Y') >>> >>> df.datestr.map(get_year).execute(libraries=['six.whl', 'python_dateutil.whl']) datestr 0 2016 1 2015 |  |  |

PyODPS默认支持执行纯Python且不含文件操作的第三方库。在较新版本的MaxCompute服务下，PyODPS也支持执行带有二进制代码或带有文件操作的Python 库。这些库名必须拥有一定的后缀，可根据下表判断：

| 平台 | Python版本 | 可用的后缀 |
|---|---|---|
| RHEL 5 x8664 _ | Python 2.7 | cp27-cp27m-manylinux1x8664 _ _ |
| RHEL 5 x8664 _ | Python 3.7 | cp37-cp37m-manylinux1x8664 _ _ |
| RHEL 7 x8664 _ | Python 2.7 | cp27-cp27m-manylinux1x8664 _ _ cp27-cp27m-manylinux2010x8664 _ _ cp27-cp27m-manylinux2014x8664 _ _ |
| RHEL 7 x8664 _ | Python 3.7 | cp37-cp37m-manylinux1x8664 _ _ cp37-cp37m-manylinux2010x8664 _ _ cp37-cp37m-manylinux2014x8664 _ _ |

| RHEL 7 Arm64 | Python 3.7 | cp37-cp37m-manylinux2014aarch64 _ |
|---|---|---|

所有的Wheel包都需要以Archive格式上传，whl后缀的包需要重命名为zip后缀。同时，作业需要开启 `odps.isolation.session.enable` 选项，或者在Project级别开启Isolation。以下示例展示了如何上传并使用scipy中的特殊函数：
# 对于含有二进制代码的包，必须使用`Archive`方式上传资源，`whl`后缀需要改为`zip`

```
odps.create_resource('scipy.zip', 'archive', file_obj=open('scipy-0.19.0-cp27-cp27m-manylinux1_x86_64.whl', 'rb'))
```

# 如果`Project`开启了`Isolation`，下面的选项不是必需的

```python
options.sql.settings = { 'odps.isolation.session.enable': True } def psi(value):
```

# 建议在函数内部`import`第三方库，以防止不同操作系统下二进制包结构差异造成执行错误

```
    from scipy.special import psi
    return float(psi(value))
df.float_col.map(psi).execute(libraries=['scipy.zip'])
```

对于只提供源码的二进制包，可以在Linux Shell中打包成Wheel再上传，Mac和Windows中生成的Wheel包无法在MaxCompute中使用，Linux Shell中打包命令如下：

```
python setup.py bdist_wheel
```

#### 9.9.3. PyODPS条件查询

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 ii. 创建表**pyodps_iris**并上传数据集iris.csv。操作方法请参见DataWorks中的建表并上传数据文档。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 登录DataWorks控制台。
3. 在数据开发页面，右键单击已经创建的**业务流程**，选择**新建节点** **> MaxCompute > PyODPS 2**。
4. 在**新建节点**对话框，输入节点**名称**，并单击**确认**。
5. 在PyODPS节点输入示例代码。

```java
import sys reload(sys)
```

#修改系统默认编码。

```
sys.setdefaultencoding('utf8')
```

#方法一：使用条件方式输出。

```
with o.execute_sql('select * from pyodps_iris WHERE sepallength > 5 ').open_reader() as reader4:
    print reader4.raw
    for record in reader4:
        print record["sepallength"],record["sepalwidth"],record["petallength"],record["petalwidth"],record["name"]
print iris[iris.sepallength > 5].head(5)
```

#方法三：使用`query`的方式输出。

```
print iris.query("(sepallength < 5) and (petallength > 1.5)").head(5)
```

6. 单击
。
7. 在**运行日志**中查看结果。

```
"sepallength","sepalwidth","petallength","petalwidth","name" 5.1,3.5,1.4,0.2,"Iris-setosa" 5.4,3.9,1.7,0.4,"Iris-setosa" 5.4,3.7,1.5,0.2,"Iris-setosa" 5.8,4.0,1.2,0.2,"Iris-setosa" 5.7,4.4,1.5,0.4,"Iris-setosa" 5.4,3.9,1.3,0.4,"Iris-setosa" 5.1,3.5,1.4,0.3,"Iris-setosa" 5.7,3.8,1.7,0.3,"Iris-setosa" 5.1,3.8,1.5,0.3,"Iris-setosa" 5.4,3.4,1.7,0.2,"Iris-setosa" 5.1,3.7,1.5,0.4,"Iris-setosa" 5.1,3.3,1.7,0.5,"Iris-setosa" 5.2,3.5,1.5,0.2,"Iris-setosa" 5.2,3.4,1.4,0.2,"Iris-setosa" 5.4,3.4,1.5,0.4,"Iris-setosa" 5.2,4.1,1.5,0.1,"Iris-setosa" 5.5,4.2,1.4,0.2,"Iris-setosa" 5.5,3.5,1.3,0.2,"Iris-setosa" 5.1,3.4,1.5,0.2,"Iris-setosa" 5.1,3.8,1.9,0.4,"Iris-setosa" 5.1,3.8,1.6,0.2,"Iris-setosa" 5.3,3.7,1.5,0.2,"Iris-setosa" 7.0,3.2,4.7,1.4,"Iris-versicolor" 6.4,3.2,4.5,1.5,"Iris-versicolor" 6.9,3.1,4.9,1.5,"Iris-versicolor" 5.5,2.3,4.0,1.3,"Iris-versicolor" 6.5,2.8,4.6,1.5,"Iris-versicolor" 5.7,2.8,4.5,1.3,"Iris-versicolor" 6.3,3.3,4.7,1.6,"Iris-versicolor" 6.6,2.9,4.6,1.3,"Iris-versicolor" 5.2,2.7,3.9,1.4,"Iris-versicolor" 5.9,3.0,4.2,1.5,"Iris-versicolor" 6.0,2.2,4.0,1.0,"Iris-versicolor" 6.1,2.9,4.7,1.4,"Iris-versicolor" 5.6,2.9,3.6,1.3,"Iris-versicolor" 6.7,3.1,4.4,1.4,"Iris-versicolor" 5.6,3.0,4.5,1.5,"Iris-versicolor" 5.8,2.7,4.1,1.0,"Iris-versicolor" 6.2,2.2,4.5,1.5,"Iris-versicolor" 5.6,2.5,3.9,1.1,"Iris-versicolor" 5.9,3.2,4.8,1.8,"Iris-versicolor" 6.1,2.8,4.0,1.3,"Iris-versicolor" 6.3,2.5,4.9,1.5,"Iris-versicolor" 6.1,2.8,4.7,1.2,"Iris-versicolor" 6.4,2.9,4.3,1.3,"Iris-versicolor" 6.6,3.0,4.4,1.4,"Iris-versicolor" 6.8,2.8,4.8,1.4,"Iris-versicolor" 6.7,3.0,5.0,1.7,"Iris-versicolor" 6.0,2.9,4.5,1.5,"Iris-versicolor" 5.7,2.6,3.5,1.0,"Iris-versicolor" 5.5,2.4,3.8,1.1,"Iris-versicolor" 5.5,2.4,3.7,1.0,"Iris-versicolor" 5.8,2.7,3.9,1.2,"Iris-versicolor" 6.0,2.7,5.1,1.6,"Iris-versicolor" 5.4,3.0,4.5,1.5,"Iris-versicolor" 6.0,3.4,4.5,1.6,"Iris-versicolor" 6.7,3.1,4.7,1.5,"Iris-versicolor" 6.3,2.3,4.4,1.3,"Iris-versicolor" 5.6,3.0,4.1,1.3,"Iris-versicolor" 5.5,2.5,4.0,1.3,"Iris-versicolor" 5.5,2.6,4.4,1.2,"Iris-versicolor" 6.1,3.0,4.6,1.4,"Iris-versicolor" 5.8,2.6,4.0,1.2,"Iris-versicolor" 5.6,2.7,4.2,1.3,"Iris-versicolor" 5.7,3.0,4.2,1.2,"Iris-versicolor"
```

```
5.7,3.0,.,.,
```

s

```
escoo 5.7,2.9,4.2,1.3,"Iris-versicolor" 6.2,2.9,4.3,1.3,"Iris-versicolor" 5.1,2.5,3.0,1.1,"Iris-versicolor" 5.7,2.8,4.1,1.3,"Iris-versicolor" 6.3,3.3,6.0,2.5,"Iris-virginica" 5.8,2.7,5.1,1.9,"Iris-virginica" 7.1,3.0,5.9,2.1,"Iris-virginica" 6.3,2.9,5.6,1.8,"Iris-virginica" 6.5,3.0,5.8,2.2,"Iris-virginica" 7.6,3.0,6.6,2.1,"Iris-virginica" 7.3,2.9,6.3,1.8,"Iris-virginica" 6.7,2.5,5.8,1.8,"Iris-virginica" 7.2,3.6,6.1,2.5,"Iris-virginica" 6.5,3.2,5.1,2.0,"Iris-virginica" 6.4,2.7,5.3,1.9,"Iris-virginica" 6.8,3.0,5.5,2.1,"Iris-virginica" 5.7,2.5,5.0,2.0,"Iris-virginica" 5.8,2.8,5.1,2.4,"Iris-virginica" 6.4,3.2,5.3,2.3,"Iris-virginica" 6.5,3.0,5.5,1.8,"Iris-virginica" 7.7,3.8,6.7,2.2,"Iris-virginica" 7.7,2.6,6.9,2.3,"Iris-virginica" 6.0,2.2,5.0,1.5,"Iris-virginica" 6.9,3.2,5.7,2.3,"Iris-virginica" 5.6,2.8,4.9,2.0,"Iris-virginica" 7.7,2.8,6.7,2.0,"Iris-virginica" 6.3,2.7,4.9,1.8,"Iris-virginica" 6.7,3.3,5.7,2.1,"Iris-virginica" 7.2,3.2,6.0,1.8,"Iris-virginica" 6.2,2.8,4.8,1.8,"Iris-virginica" 6.1,3.0,4.9,1.8,"Iris-virginica" 6.4,2.8,5.6,2.1,"Iris-virginica" 7.2,3.0,5.8,1.6,"Iris-virginica" 7.4,2.8,6.1,1.9,"Iris-virginica" 7.9,3.8,6.4,2.0,"Iris-virginica" 6.4,2.8,5.6,2.2,"Iris-virginica" 6.3,2.8,5.1,1.5,"Iris-virginica" 6.1,2.6,5.6,1.4,"Iris-virginica" 7.7,3.0,6.1,2.3,"Iris-virginica" 6.3,3.4,5.6,2.4,"Iris-virginica" 6.4,3.1,5.5,1.8,"Iris-virginica" 6.0,3.0,4.8,1.8,"Iris-virginica" 6.9,3.1,5.4,2.1,"Iris-virginica" 6.7,3.1,5.6,2.4,"Iris-virginica" 6.9,3.1,5.1,2.3,"Iris-virginica" 5.8,2.7,5.1,1.9,"Iris-virginica" 6.8,3.2,5.9,2.3,"Iris-virginica" 6.7,3.3,5.7,2.5,"Iris-virginica" 6.7,3.0,5.2,2.3,"Iris-virginica" 6.3,2.5,5.0,1.9,"Iris-virginica" 6.5,3.0,5.2,2.0,"Iris-virginica" 6.2,3.4,5.4,2.3,"Iris-virginica" 5.9,3.0,5.1,1.8,"Iris-virginica" 5.1 3.5 1.4 0.2 Iris-setosa 5.4 3.9 1.7 0.4 Iris-setosa 5.4 3.7 1.5 0.2 Iris-setosa 5.8 4.0 1.2 0.2 Iris-setosa 5.7 4.4 1.5 0.4 Iris-setosa 5.4 3.9 1.3 0.4 Iris-setosa 5.1 3.5 1.4 0.3 Iris-setosa 5.7 3.8 1.7 0.3 Iris-setosa 5.1 3.8 1.5 0.3 Iris-setosa 5.4 3.4 1.7 0.2 Iris-setosa 5.1 3.7 1.5 0.4 Iris-setosa 5.1 3.3 1.7 0.5 Iris-setosa 5.2 3.5 1.5 0.2 Iris-setosa 5.2 3.4 1.4 0.2 Iris-setosa 5.4 3.4 1.5 0.4 Iris-setosa 5.2 4.1 1.5 0.1 Iris-setosa 5.5 4.2 1.4 0.2 Iris-setosa 5.5 3.5 1.3 0.2 Iris-setosa 5.1 3.4 1.5 0.2 Iris-setosa 5.1 3.8 1.9 0.4 Iris-setosa 5.1 3.8 1.6 0.2 Iris-setosa 5.3 3.7 1.5 0.2 Iris-setosa 7.0 3.2 4.7 1.4 Iris-versicolor 6.4 3.2 4.5 1.5 Iris-versicolor 6.9 3.1 4.9 1.5 Iris-versicolor 5.5 2.3 4.0 1.3 Iris-versicolor 6.5 2.8 4.6 1.5 Iris-versicolor 5.7 2.8 4.5 1.3 Iris-versicolor 6.3 3.3 4.7 1.6 Iris-versicolor 6.6 2.9 4.6 1.3 Iris-versicolor
```

```
5.2 2.7 3.9 1.4 Iris-versicolor 5.9 3.0 4.2 1.5 Iris-versicolor 6.0 2.2 4.0 1.0 Iris-versicolor 6.1 2.9 4.7 1.4 Iris-versicolor 5.6 2.9 3.6 1.3 Iris-versicolor 6.7 3.1 4.4 1.4 Iris-versicolor 5.6 3.0 4.5 1.5 Iris-versicolor 5.8 2.7 4.1 1.0 Iris-versicolor 6.2 2.2 4.5 1.5 Iris-versicolor 5.6 2.5 3.9 1.1 Iris-versicolor 5.9 3.2 4.8 1.8 Iris-versicolor 6.1 2.8 4.0 1.3 Iris-versicolor 6.3 2.5 4.9 1.5 Iris-versicolor 6.1 2.8 4.7 1.2 Iris-versicolor 6.4 2.9 4.3 1.3 Iris-versicolor 6.6 3.0 4.4 1.4 Iris-versicolor 6.8 2.8 4.8 1.4 Iris-versicolor 6.7 3.0 5.0 1.7 Iris-versicolor 6.0 2.9 4.5 1.5 Iris-versicolor 5.7 2.6 3.5 1.0 Iris-versicolor 5.5 2.4 3.8 1.1 Iris-versicolor 5.5 2.4 3.7 1.0 Iris-versicolor 5.8 2.7 3.9 1.2 Iris-versicolor 6.0 2.7 5.1 1.6 Iris-versicolor 5.4 3.0 4.5 1.5 Iris-versicolor 6.0 3.4 4.5 1.6 Iris-versicolor 6.7 3.1 4.7 1.5 Iris-versicolor 6.3 2.3 4.4 1.3 Iris-versicolor 5.6 3.0 4.1 1.3 Iris-versicolor 5.5 2.5 4.0 1.3 Iris-versicolor 5.5 2.6 4.4 1.2 Iris-versicolor 6.1 3.0 4.6 1.4 Iris-versicolor 5.8 2.6 4.0 1.2 Iris-versicolor 5.6 2.7 4.2 1.3 Iris-versicolor 5.7 3.0 4.2 1.2 Iris-versicolor 5.7 2.9 4.2 1.3 Iris-versicolor 6.2 2.9 4.3 1.3 Iris-versicolor 5.1 2.5 3.0 1.1 Iris-versicolor 5.7 2.8 4.1 1.3 Iris-versicolor 6.3 3.3 6.0 2.5 Iris-virginica 5.8 2.7 5.1 1.9 Iris-virginica 7.1 3.0 5.9 2.1 Iris-virginica 6.3 2.9 5.6 1.8 Iris-virginica 6.5 3.0 5.8 2.2 Iris-virginica 7.6 3.0 6.6 2.1 Iris-virginica 7.3 2.9 6.3 1.8 Iris-virginica 6.7 2.5 5.8 1.8 Iris-virginica 7.2 3.6 6.1 2.5 Iris-virginica 6.5 3.2 5.1 2.0 Iris-virginica 6.4 2.7 5.3 1.9 Iris-virginica 6.8 3.0 5.5 2.1 Iris-virginica 5.7 2.5 5.0 2.0 Iris-virginica 5.8 2.8 5.1 2.4 Iris-virginica 6.4 3.2 5.3 2.3 Iris-virginica 6.5 3.0 5.5 1.8 Iris-virginica 7.7 3.8 6.7 2.2 Iris-virginica 7.7 2.6 6.9 2.3 Iris-virginica 6.0 2.2 5.0 1.5 Iris-virginica 6.9 3.2 5.7 2.3 Iris-virginica 5.6 2.8 4.9 2.0 Iris-virginica 7.7 2.8 6.7 2.0 Iris-virginica 6.3 2.7 4.9 1.8 Iris-virginica 6.7 3.3 5.7 2.1 Iris-virginica 7.2 3.2 6.0 1.8 Iris-virginica 6.2 2.8 4.8 1.8 Iris-virginica 6.1 3.0 4.9 1.8 Iris-virginica 6.4 2.8 5.6 2.1 Iris-virginica 7.2 3.0 5.8 1.6 Iris-virginica 7.4 2.8 6.1 1.9 Iris-virginica 7.9 3.8 6.4 2.0 Iris-virginica 6.4 2.8 5.6 2.2 Iris-virginica 6.3 2.8 5.1 1.5 Iris-virginica 6.1 2.6 5.6 1.4 Iris-virginica 7.7 3.0 6.1 2.3 Iris-virginica 6.3 3.4 5.6 2.4 Iris-virginica 6.4 3.1 5.5 1.8 Iris-virginica 6.0 3.0 4.8 1.8 Iris-virginica 6.9 3.1 5.4 2.1 Iris-virginica 6.7 3.1 5.6 2.4 Iris-virginica 6.9 3.1 5.1 2.3 Iris-virginica 5.8 2.7 5.1 1.9 Iris-virginica 6.8 3.2 5.9 2.3 Iris-virginica 6.7 3.3 5.7 2.5 Iris-virginica 67305223Iris-virginica
```

```
6.7 3.0 5.2 2.3 Irisvirginica 6.3 2.5 5.0 1.9 Iris-virginica 6.5 3.0 5.2 2.0 Iris-virginica 6.2 3.4 5.4 2.3 Iris-virginica 5.9 3.0 5.1 1.8 Iris-virginica Sql compiled: SELECT * WHERE t1.`sepallength` > 5 Instance ID: 2019xxxx
  Log view: http://logview.odps.aliyun.com/logview/?h=http://service.cn.maxcompute.aliyun.com/api&p=xxxx&i=2019xxxx&token=xxxx
   sepallength  sepalwidth  petallength  petalwidth         name
0 5.1 3.5 1.4 0.2 Iris-setosa 1 5.4 3.9 1.7 0.4 Iris-setosa 2 5.4 3.7 1.5 0.2 Iris-setosa 3 5.8 4.0 1.2 0.2 Iris-setosa 4 5.7 4.4 1.5 0.4 Iris-setosa Sql compiled: SELECT * WHERE (t1.`sepallength` < 5) AND (t1.`petallength` > 1.5) Instance ID: 2019xxxx
  Log view: http://logview.odps.aliyun.com/logview/?h=http://service.cn.maxcompute.aliyun.com/api&p=xxxx&i=2019xxxx&token=xxxx
   sepallength  sepalwidth  petallength  petalwidth             name
0 4.8 3.4 1.6 0.2 Iris-setosa 1 4.8 3.4 1.9 0.2 Iris-setosa 2 4.7 3.2 1.6 0.2 Iris-setosa 3 4.8 3.1 1.6 0.2 Iris-setosa 4 4.9 2.4 3.3 1.0 Iris-versicolor
```

#### 9.9.4. PyODPS参数传递

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 准备测试数据。
i. 创建表并上传数据。操作方法请参见DataWorks文档中的建表并上传数据。 表结构以及源数据信息如下。 分区表user_detail建表语句如下。

```
CREATE TABLE IF NOT EXISTS user_detail ( userid BIGINT comment '用户id', job STRING comment '工作类型', education STRING comment '教育程度'
```

`) comment '`用户信息表'

```
partitioned BY (dt STRING comment '日期',region STRING comment '地区');
```

源数据表user_detail_ods建表语句如下。

```
CREATE TABLE IF NOT EXISTS user_detail_ods (
  userid    BIGINT comment '用户id',
  job       STRING comment '工作类型',
  education STRING comment '教育程度',
  dt STRING comment '日期',
  region STRING comment '地区'
);
```

测试数据保存为user_detail.txt文件。将此文件上传至表user_detail_ods中。 `0001,`互联网,本科`,20190715,beijing`

```
0002,教育,大专,20190716,beijing 0003,金融,硕士,20190715,shandong
```

`0004,`互联网,硕士`,20190715,beijing` ii. 右键单击业务流程，选择**新建节点** **> MaxCompute > ODPS SQL**。 iii. 输入节点**名称**，并单击**确认**。 iv. 在ODPS SQL节点中输入如下代码。

```
INSERT OVERWRITE TABLE user_detail PARTITION(dt,region) SELECT userid,job,education,dt,region FROM user_detail_ods;
```

v. 单击 ，将数据插入到分区表user_detail中。
2. 使用PyODPS传递参数。
i. 登录DataWorks控制台。 ii. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。 iii. 输入节点**名称**，单击**确认**。

```java
import sys reload(sys) print('dt=' + args['dt'])
```

#修改系统默认编码。

```
sys.setdefaultencoding('utf8')
```

#获取表。

```
t = o.get_table('user_detail')
```

#接受传入的分区参数。

```
with t.open_reader(partition='dt=' + args['dt'] + ',region=beijing') as reader1:
    count = reader1.count
```

`print("`查询分区表数据：`")`

```
for record in reader1:
    print record[0],record[1],record[2]
```

v. 单击**高级运行（带参数运行）**。 vi. 在**参数**对话框填写配置参数，单击**运行**。 配置参数**dt**：设置为**dt=20190715**。 vii. 在**运行日志**中查看运行结果。

#### 9.9.5. PyODPS读取分区表数据

**前提条件**

您需要完成以下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 准备测试数据。
i. 创建表并上传数据。操作方法请参见DataWorks文档中的建表并上传数据。 表结构以及源数据信息如下。 分区表user_detail建表语句如下。

```
CREATE TABLE IF NOT EXISTS user_detail ( userid BIGINT comment '用户id', job STRING comment '工作类型', education STRING comment '教育程度'
```

`) comment '`用户信息表'

```
partitioned BY (dt STRING comment '日期',region STRING comment '地区');
```

源数据表user_detail_ods建表语句如下。

```
CREATE TABLE IF NOT EXISTS user_detail_ods (
  userid    BIGINT comment '用户id',
  job       STRING comment '工作类型',
  education STRING comment '教育程度',
  dt STRING comment '日期',
  region STRING comment '地区'
);
```

测试数据保存为user_detail.txt文件。将此文件上传至表user_detail_ods中。 `0001,`互联网,本科`,20190715,beijing`

```
0002,教育,大专,20190716,beijing 0003,金融,硕士,20190715,shandong
```

`0004,`互联网,硕士`,20190715,beijing` ii. 右键单击业务流程，选择**新建节点** **> MaxCompute > ODPS SQL**。 iii. 输入节点**名称**，并单击**确认**。 iv. 在ODPS SQL节点中输入如下代码。

```
INSERT OVERWRITE TABLE user_detail PARTITION(dt,region) SELECT userid,job,education,dt,region FROM user_detail_ods;
```

v. 单击 ，将数据插入到分区表user_detail中。
2. 使用PyODPS读取分区表数据。
i. 登录DataWorks控制台。 ii. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。 iii. 输入节点**名称**，并单击**确认**。

```java
import sys from odps import ODPS reload(sys) print('dt=' + args['dt'])
```

#修改系统默认编码。

```
sys.setdefaultencoding('utf8')
```

#个人信息凭证。

```
t = o.get_table('user_detail')
```

#获取分区表。

```
print t.exist_partition('dt=20190715,region=beijing')
```

#查看所有分区。

```
for partition in t.partitions:
    print partition.name
```

#您可以通过以下三种方式查询分区表数据。
#第一种方式如下。

```
with t.open_reader(partition='dt=20190715,region=beijing') as reader1:
    count = reader1.count
```

`print("`第一种方式查询分区表数据：`")`

```
for record in reader1:
    print record[0],record[1],record[2]
```

#第二种方式如下。
`print("`第二种方式查询分区表数据：`")`

```
reader2 = t.open_reader(partition='dt=20190715,region=beijing') for record in reader2:
    print record["userid"],record["job"],record["education"]
```

#第三种方式如下。
`print("`第三种方式查询分表数据：`")`

```
for record in o.read_table('user_detail', partition='dt=20190715,region=beijing'):
    print record["userid"],record["job"],record["education"]
```

v. 单击**高级运行（带参数运行）**。 vi. 在**参数**对话框填写配置参数，单击**运行**。 配置参数**dt**：设置为**dt=20190715**。 vii. 在**运行日志**中查看运行结果。

#### 9.9.6. PyODPS查看一级分区

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 准备测试数据。
i. 创建表并上传数据。操作方法请参见DataWorks文档中的建表并上传数据。 表结构以及源数据信息如下。 分区表user_detail建表语句如下。

```
CREATE TABLE IF NOT EXISTS user_detail ( userid BIGINT comment '用户id', job STRING comment '工作类型', education STRING comment '教育程度'
```

`) comment '`用户信息表'

```
partitioned BY (dt STRING comment '日期',region STRING comment '地区');
```

源数据表user_detail_ods建表语句如下。

```
CREATE TABLE IF NOT EXISTS user_detail_ods (
  userid    BIGINT comment '用户id',
  job       STRING comment '工作类型',
  education STRING comment '教育程度',
  dt STRING comment '日期',
  region STRING comment '地区'
);
```

测试数据保存为user_detail.txt文件。将此文件上传至表user_detail_ods中。 `0001,`互联网,本科`,20190715,beijing`

```
0002,教育,大专,20190716,beijing 0003,金融,硕士,20190715,shandong
```

`0004,`互联网,硕士`,20190715,beijing` ii. 右键单击业务流程，选择**新建节点** **> MaxCompute > ODPS SQL**。 iii. 输入节点**名称**，并单击**确认**。 iv. 在ODPS SQL节点中输入如下代码。

```
INSERT OVERWRITE TABLE user_detail PARTITION(dt,region) SELECT userid,job,education,dt,region FROM user_detail_ods;
```

v. 单击 ，将数据插入到分区表user_detail中。
2. 使用PyODPS查看一级分区。
i. 登录DataWorks控制台。 ii. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。 iii. 输入节点**名称**，并单击**确认**。

```java
import sys reload(sys)
```

#修改系统默认编码。

```
sys.setdefaultencoding('utf8')
```

#异步方式读取一级分区。

```
instance = o.run_sql('select * from user_detail WHERE dt=\'20190715\'') instance.wait_for_success() for record in instance.open_reader():
    print record["userid"],record["job"],record["education"]
```

#同步方式读取一级分区。

```
with o.execute_sql('select * from user_detail WHERE dt=\'20190715\'').open_reader() as reader4:
    print reader4.raw
    for record in reader4:
        print record["userid"],record["job"],record["education"]
pt_df = DataFrame(o.get_table('user_detail').get_partition('dt=20190715')) print pt_df.head(10)
```

v. 单击按钮。 vi. 在**运行日志**中查看运行结果。

#### 9.9.7. PyODPS的Sequence及执行操作

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 ii. 创建表**pyodps_iris**并上传数据集iris.csv。操作方法请参见DataWorks中的建表并上传数据文档。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 登录DataWorks控制台。
3. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。
4. 输入节点**名称**，并单击**确认**。
5. 进入**PyODPS**节点编辑框，输入示例代码。示例代码如下。
#获取列。

```
print iris.sepallength.head(5) print iris['sepallength'].head(5)
```

#查看列的类型。

```
print iris.sepallength.dtype
```

#修改列的类型。

```
iris.sepallength.astype('int')
```

#计算。

```
print iris.groupby('name').sepallength.max().head(5) print iris.sepallength.max()
```

#重命名列。

```
print iris.sepalwidth.rename('speal_width').head(5)
```

#简单的列变化。

```
print (iris.sepallength + iris.sepalwidth).rename('sum_sepal').head(5)
```

6. 单击
图标。
7. 在**运行日志**中查看结果。
结果如下：

```
Try to fetch data from tunnel
   sepallength
0 4.9 1 4.7 2 4.6 3 5.0 4 5.4 Try to fetch data from tunnel
   sepallength
0 4.9 1 4.7 2 4.6 3 5.0 4 5.4 FLOAT64 Sql compiled: CREATE TABLE tmp_pyodps_ed78e3ba_f13c_4a49_812d_2790d57c25dd LIFECYCLE 1 AS SELECT MAX(t1.`sepallength`) AS `sepallength_max` GROUP BY t1.`name`
   sepallength_max
0 5.8 1 7.0 2 7.9
  odps.Table
    schema:
      sepallength           : double      # 片长度(cm)
      sepalwidth            : double      # 片宽度(cm)
      petallength           : double      # 瓣长度(cm)
      petalwidth            : double      # 瓣宽度(cm)
      name                  : string      # 种类
max = Max[float64]
  sepallength = Column[sequence(float64)] 'sepallength' from collection ref_0
Try to fetch data from tunnel
   speal_width
0 3.0 1 3.2 2 3.1 3 3.6 4 3.9 Sql compiled: CREATE TABLE tmp_pyodps_28120275_8d0f_4683_8318_302fa21459ac LIFECYCLE 1 AS SELECT t1.`sepallength` + t1.`sepalwidth` AS `sum_sepal`
   sum_sepal
0 7.9 1 7.9 2 7.7 3 8.6 4 9.3 2019-08-13 10:48:13 INFO ================================================================= 2019-08-13 10:48:13 INFO Exit code of the Shell command 0 2019-08-13 10:48:13 INFO --- Invocation of Shell command completed --- 2019-08-13 10:48:13 INFO Shell run successfully!
```

8. 按照如上方法，新建并运行Pyodps节点PyExecute。
PyExecute节点示例代码如下。

```python
from odps import options
```

#查看运行时的`instance`的`logview`。

```python
options.verbose = True iris[iris.sepallength < 5].exclude('sepallength')[:5].execute() my_logs = [] def my_loggers(x):
    my_logs.append(x)
options.verbose_log = my_loggers iris[iris.sepallength < 5].exclude('sepallength')[:5].execute() print(my_logs) cached = iris[iris.sepalwidth < 3.5].cache() print cached.head(3)
```

#异步和并行执行。

```
from odps.df import Delay
```

`delay = Delay() #`创建`Delay`对象。 `df = iris[iris.sepalwidth < 5].cache() #`有一个共同的依赖。 `future1 = df.sepalwidth.sum().execute(delay=delay) #`立即返回`future`对象，此时并没有执行。

```
future2 = df.sepalwidth.mean().execute(delay=delay) future3 = df.sepalwidth.max().execute(delay=delay) delay.execute(n_parallel=3) print future1.result() print future2.result() print future3.result()
```

运行结果如下：

```json
Sql compiled: CREATE TABLE tmp_pyodps_4a204590_0510_4e9c_823b_5b837a437840 LIFECYCLE 1 AS SELECT t1.`sepalwidth`, t1.`petallength`, t1.`petalwidth`, t1.`name` WHERE t1.`sepallength` < 5 LIMIT 5 Instance ID: 20190813025233386g04djssa
  Log view: http://logview.odps.aliyun.com/logview/XXX
['Sql compiled:', 'CREATE TABLE tmp_pyodps_03b92c55_8442_4e61_8978_656495487b8a LIFECYCLE 1 AS \nSELECT t1.`sepalwidth`, t1.`petallengt h`, t1.`petalwidth`, t1.`name` \nFROM data_service_fr.`pyodps_iris` t1 \nWHERE t1.`sepallength` < 5 \nLIMIT 5', 'Instance ID: 20190813025236282gcsna5pr2', u' Log view: http://logview.odps.aliyun.com/logview/?h=http://service.odps.aliyun.com/api&XXX
   sepallength  sepalwidth  petallength  petalwidth         name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa 454.6 3.05100671141 4.4 2019-08-13 10:52:48 INFO ================================================================= 2019-08-13 10:52:48 INFO Exit code of the Shell command 0 2019-08-13 10:52:48 INFO --- Invocation of Shell command completed --- 2019-08-13 10:52:48 INFO Shell run successfully! 2019-08-13 10:52:48 INFO Current task status: FINISH
```

#### 9.9.8. PyODPS的聚合操作

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 ii. 创建表**pyodps_iris**并上传数据集iris.csv。操作方法请参见DataWorks中的建表并上传数据文档。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 登录DataWorks控制台。
3. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。
4. 输入节点**名称**，并单击**确认**。
5. 在PyODPS节点中输入聚合操作代码。
示例代码如下。

```java
from odps.df import Delay from odps.df import Scalar from odps.df import agg import numpy as np import pandas as pd
```

#describe函数，查看`DataFrame`里数字列的数量、最大值、最小值、平均值以及标准差。

```
print iris.describe().execute()
```

#单列聚合操作。

```
print iris.sepallength.max().execute()
```

#消除重复列的聚合。

```
print iris.name.unique().cat(sep=',').execute()
```

#统计总行数。

```
print iris.count().execute()
```

#分组聚合。

```
print iris.groupby('name').agg(iris.sepallength.max(),smin=iris.sepallength.min()).head() print iris.groupby('name').agg(count=iris.name.count()).sort('count', ascending=False).head(5) print iris.groupby('name').petallength.sum().head() print iris.groupby('name').agg(iris.petallength.notnull().sum()).head() print iris.groupby(Scalar(1)).petallength.sum().head()
```

#自定义聚合，对应单列。

```python
class Agg(object):
    def buffer(self):
        return [0.0, 0]
    def __call__(self, buffer, val):
        buffer[0] += val
        buffer[1] += 1
    def merge(self, buffer, pbuffer):
        buffer[0] += pbuffer[0]
        buffer[1] += pbuffer[1]
    def getvalue(self, buffer):
        if buffer[1] == 0:
            return 0.0
        return buffer[0] / buffer[1]
print iris.sepalwidth.agg(Agg).execute()
```

#自定义聚合，对应双列。

```python
class Agg2(object):
    def buffer(self):
        return [0.0, 0.0]
    def __call__(self, buffer, val1, val2):
        buffer[0] += val1
        buffer[1] += val2
    def merge(self, buffer, pbuffer):
        buffer[0] += pbuffer[0]
        buffer[1] += pbuffer[1]
    def getvalue(self, buffer):
        if buffer[1] == 0:
            return 0.0
        return buffer[0] - buffer[1]
to_agg = agg([iris.sepalwidth, iris.sepallength], Agg2, rtype='float') # 对两列调用自定义聚合。 print iris.groupby('name').agg(val=to_agg).execute()
```

#HyperLogLog计数。

```
df5 = DataFrame(pd.DataFrame({'a': np.random.randint(100000, size=100000)})) print df5.a.hll_count().execute()
```

6. 单击运行。
7. 在**运行日志**中查看结果。
运行结果如下。

```
Sql compiled: CREATE TABLE tmp_pyodps_28b83337_87f9_4b11_a084_f1896758d53b LIFECYCLE 1 AS SELECT pyodps_udf_1567394092_9467b7ba_3121_4105_81dc_431e8e68be39(t3.`sepallength_count`, t3.`sepallength_mean`, t3.`sepallength_std`, t3.`sepallength_min`, t3.`sepallength_quantile_25`, t3.`sepallength_quantile_50`, t3.`sepallength_quantile_75`, t3.`sepallength_max`, t 3.`sepalwidth_count`, t3.`sepalwidth_mean`, t3.`sepalwidth_std`, t3.`sepalwidth_min`, t3.`sepalwidth_quantile_25`, t3.`sepalwidth_quantile_50`, t3.`sepalwidth_quantile_75`, t3.`sepalwidth_max`, t3.`petallength_count`, t3.`petallength_mean`, t3.`petal length_std`, t3.`petallength_min`, t3.`petallength_quantile_25`, t3.`petallength_quantile_50`, t3.`petallength_quantile_75`, t3.`petall ength_max`, t3.`petalwidth_count`, t3.`petalwidth_mean`, t3.`petalwidth_std`, t3.`petalwidth_min`, t3.`petalwidth_quantile_25`, t3.`pet alwidth_quantile_50`, t3.`petalwidth_quantile_75`, t3.`petalwidth_max`) AS (`type`, `sepallength`, `sepalwidth`, `petallength`, `petalw idth`) FROM (
  SELECT COUNT(t2.`sepallength`) AS `sepallength_count`, AVG(t2.`sepallength`) AS `sepallength_mean`, STDDEV_SAMP(t2.`sepallength`) AS
`sepallength_std`, MIN(t2.`sepallength`) AS `sepallength_min`, PERCENTILE(t2.`sepallength`, 0.25) AS `sepallength_quantile_25`, PERCENT ILE(t2.`sepallength`, 0.5) AS `sepallength_quantile_50`, PERCENTILE(t2.`sepallength`, 0.75) AS `sepallength_quantile_75`, MAX(t2.`sepal length`) AS `sepallength_max`, COUNT(t2.`sepalwidth`) AS `sepalwidth_count`, AVG(t2.`sepalwidth`) AS `sepalwidth_mean`, STDDEV_SAMP(t2.`sepalwidth`) AS `sepalwidth_std`, MIN(t2.`sepalwidth`) AS `sepalwidth_min`, PERCENTILE(t2.`sepalwidth`, 0.25) AS `sepal width_quantile_25`, PERCENTILE(t2.`sepalwidth`, 0.5) AS `sepalwidth_quantile_50`, PERCENTILE(t2.`sepalwidth`, 0.75) AS `sepalwidth_quantile_75`, MAX(t2.`sepalwidth`) AS `sepalwidth_max`, COUNT(t2.`petallength`) AS `petallength_count`, AVG(t2.`petallength`) AS`petallength_mean`, STDDEV_SAMP(t2.`petallength`) AS `petallength_std`, MIN(t2.`petallength`) AS `petallength_m in`, PERCENTILE(t2.`petallength`, 0.25) AS `petallength_quantile_25`, PERCENTILE(t2.`petallength`, 0.5) AS `petallength_quantile_50`, P ERCENTILE(t2.`petallength`, 0.75) AS `petallength_quantile_75`, MAX(t2.`petallength`) AS `petallength_max`, COUNT(t2.`petalwidth`) AS ` petalwidth_count`, AVG(t2.`petalwidth`) AS `petalwidth_mean`, STDDEV_SAMP(t2.`petalwidth`) AS `petalwidth_std`, MIN(t2.`petalwidth`) AS `petalwidth_min`, PERCENTILE(t2.`petalwidth`, 0.25) AS `petalwidth_quantile_25`, PERCENTILE(t2.`petalwidth`, 0.5) AS `petalwidth_quantile_50`, PERCENTILE(t2.`petalwidth`, 0.75) AS `petalwidth_quantile_75`, MAX(t2.`petalwidth`) AS `petalwidth_max`
  FROM (
    SELECT t1.`sepallength`, t1.`sepalwidth`, t1.`petallength`, t1.`petalwidth`
  ) t2
) t3
          type  sepallength  sepalwidth  petallength  petalwidth
0 count 149.000000 149.000000 149.000000 149.000000 1 mean 5.848322 3.051007 3.774497 1.205369 2 std 0.828594 0.433499 1.759651 0.761292 3 min 4.300000 2.000000 1.000000 0.100000 4 quantile_25 5.000000 2.000000 1.000000 0.000000 5 quantile_50 5.000000 3.000000 4.000000 1.000000 6 quantile_75 6.000000 3.000000 5.000000 1.000000 7 max 7.900000 4.400000 6.900000 2.500000 Sql compiled: SELECT MAX(t2.`sepallength`) AS `sepallength_max` FROM (
  SELECT t1.`sepallength`
) t2 7.9 Sql compiled: SELECT WM_CONCAT(DISTINCT ',', t2.`name`) AS `name_cat` FROM (
  SELECT t1.`name`
) t2 Iris-setosa,Iris-versicolor,Iris-virginica Sql compiled: CREATE TABLE tmppyodps4b00d67182b14cd88af4f11dbdac4570 LIFECYCLE 1 AS
```

```
p_py
```

p_ _ _ _ _

```
SELECT t1.`name`, MAX(t1.`sepallength`) AS `sepallength_max`, MIN(t1.`sepallength`) AS `smin` GROUP BY t1.`name`
              name  sepallength_max  smin
0 Iris-setosa 5.8 4.3 1 Iris-versicolor 7.0 4.9 2 Iris-virginica 7.9 4.9 Sql compiled: CREATE TABLE tmp_pyodps_276c901f_7cf0_48ee_aaae_0d3092822b34 LIFECYCLE 1 AS SELECT t1.`name`, COUNT(t1.`name`) AS `count` GROUP BY t1.`name` ORDER BY count DESC LIMIT 10000
              name  count
0 Iris-versicolor 50 1 Iris-virginica 50 2 Iris-setosa 49 Sql compiled: CREATE TABLE tmp_pyodps_440d12ec_8496_4b87_b33f_b9624941e5bd LIFECYCLE 1 AS SELECT SUM(t1.`petallength`) AS `petallength_sum` GROUP BY t1.`name` Instance ID: 20190902031604255go6c472m
   petallength_sum
0 71.8 1 213.0 2 277.6 Sql compiled: CREATE TABLE tmp_pyodps_61e62f5f_7b4f_4971_8c39_dcaccba37764 LIFECYCLE 1 AS SELECT t1.`name`, SUM(IF(t1.`petallength` IS NOT NULL, 1, 0)) AS `petallength_sum` GROUP BY t1.`name` Instance ID: 20190902031607441ghzyr392
              name  petallength_sum
0 Iris-setosa 49 1 Iris-versicolor 50 2 Iris-virginica 50 Sql compiled: CREATE TABLE tmp_pyodps_daeffd50_88fe_4b4d_9db9_57810cfe71c3 LIFECYCLE 1 AS SELECT SUM(t1.`petallength`) AS `petallength_sum` GROUP BY 1
   petallength_sum
0 562.4 Sql compiled: SELECT pyodps_udf_1567394173_ef78183a_a4f5_4372_91dd_18d6ecc6f651(t2.`sepalwidth`) AS `sepalwidth_aggregation` FROM (
  SELECT t1.`sepalwidth`
) t2 Sql compiled: CREATE TABLE tmp_pyodps_e312f110_64e7_465e_adae_fd053f125a90 LIFECYCLE 1 AS SELECT t1.`name`, pyodps_udf_1567394220_49231d7a_faeb_4f2f_9de5_36c4aefaa29b(t1.`sepalwidth`, t1.`sepallength`) AS `val` GROUP BY t1.`name`
              name    val
0 Iris-setosa -77.8 1 Iris-versicolor -158.3 2 Iris-virginica -180.7 63021
```

#### 9.9.9. PyODPS的列运算

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 ii. 创建表**pyodps_iris**并上传数据集iris.csv。操作方法请参见DataWorks中的建表并上传数据文档。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 登录DataWorks控制台。
3. 在数据开发页面，右键单击已经创建的**业务流程**，选择**新建节点** **> MaxCompute > PyODPS 2**。
4. 在**新建节点**对话框，输入节点**名称**，并单击**确认**。
5. 在PyODPS节点输入示例代码。
示例代码如下。

```java
import numpy as np import pandas as pd
```

#判断是否为`null`。

```
print iris.sepallength.isnull().head(5)
```

#逻辑判断。

```
print (iris.sepallength > 5).ifelse('gt5','lte5').rename('cmp5').head(5)
```

#多条件判断。

```
print iris.sepallength.switch(4.9,'eq4.9',5.0,'eq5.0',default='noeq').rename('equalness').head(5) from odps.df import switch print switch(iris.sepallength == 4.9,'eq4.9',iris.sepallength == 5.0,'eq5.0',default='noeq').rename('equalness').head(5)
```

#修该数据集某一列的一部分值。

```
iris[iris.sepallength > 5,'cmp5'] = 'gt5' iris[iris.sepallength <=5,'cmp5'] = 'lte5' print iris.head(5)
```

#数学计算。

```
print (iris.sepallength * 10).log().head(5) fields = [iris.sepallength,(iris.sepallength /2).rename('sepallength/2'),(iris.sepallength ** 2).rename('sepallength的平方')] print iris[fields].head(5) print (iris.sepallength < 5).head(5)
```

#集合类型相关操作。

```
data = {'id': [1,2], 'a': [['a1','b1'],['c1']], 'b': [{'a2': 0, 'b2': 1, 'c2': 2},{'d2': 3, 'e2': 4}]} print df df1 = DataFrame(df, unknown_as_string=True, as_type={'a': 'list<string>','b' : 'dict<string,int64>'}) print df1.dtypes print df1.head() print df1[df1.id,df1.a[0],df1.b.len()].head() print df1.a.explode().head() print df1.a.explode(pos=True).head() print df1.b.explode().head() print df1.b.explode(['key','value']).head()
```

#explode与其他并列多行输出。

```
print df1[df1.id,df1.a.explode()].head()
#isin,notin,cut。
print iris.sepallength.isin([4.9,5.1]).rename('sepallength').head() print iris.sepallength.cut(range(6),labels=['0-1','1-2','2-3','3-4','4-5']).rename('sepallength_cut').head(5)
```

#include_under和`include_over`可以分别包括向下和向上的区间。

```
labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-'] iris.sepallength.cut(range(6), labels=labels, include_over=True).rename('sepallength_cut').head(5)
```

6. 单击运行。
7. 在**运行日志**中查看结果。
运行结果如下：

```
Sql compiled:
```

```
CREATE TABLE tmp_pyodps_32e39a9a_8ae6_4815_b465_4b9dfa3bf1b9 LIFECYCLE 1 AS SELECT t1.`sepallength` IS NULL AS `sepallength`
  sepallength
0 False 1 False 2 False 3 False 4 False Sql compiled: CREATE TABLE tmp_pyodps_d684aded_8ad8_4119_8558_1fddd774dd3f LIFECYCLE 1 AS SELECT IF(t1.`sepallength` > 5, 'gt5', 'lte5') AS `cmp5`
   cmp5
0 lte5 1 lte5 2 lte5 3 lte5 4 gt5 Sql compiled: CREATE TABLE tmp_pyodps_cfc5bdb9_6d3e_4711_8acc_913b29b96c9a LIFECYCLE 1 AS SELECT CASE t1.`sepallength` WHEN 4.9 THEN 'eq4.9' WHEN 5.0 THEN 'eq5.0' ELSE 'noeq' END AS `equalness`
  equalness
0 eq4.9 1 noeq 2 noeq 3 eq5.0 4 noeq Sql compiled: CREATE TABLE tmp_pyodps_d1fd70b4_2ad8_4dc9_838e_f566f7f5841e LIFECYCLE 1 AS SELECT CASE WHEN t1.`sepallength` == 4.9 THEN 'eq4.9' WHEN t1.`sepallength` == 5.0 THEN 'eq5.0' ELSE 'noeq' END AS `equalness`
  equalness
0 eq4.9 1 noeq 2 noeq 3 eq5.0 4 noeq Sql compiled: CREATE TABLE tmp_pyodps_d9e5d64e_1f21_4ffb_993f_70d3f36b6553 LIFECYCLE 1 AS SELECT t1.`sepallength`, t1.`sepalwidth`, t1.`petallength`, t1.`petalwidth`, t1.`name`, IF(t1.`sepallength` <= 5, 'lte5', IF(t1.`sepall ength` > 5, 'gt5', CAST(NULL AS STRING))) AS `cmp5`
   sepallength  sepalwidth  petallength  petalwidth         name  cmp5
0 4.9 3.0 1.4 0.2 Iris-setosa lte5 1 4.7 3.2 1.3 0.2 Iris-setosa lte5 2 4.6 3.1 1.5 0.2 Iris-setosa lte5 3 5.0 3.6 1.4 0.2 Iris-setosa lte5 4 5.4 3.9 1.7 0.4 Iris-setosa gt5 Sql compiled: CREATE TABLE tmp_pyodps_4bfb0aa0_7ec5_4f35_9480_d36baf2b8079 LIFECYCLE 1 AS SELECT LN(t1.`sepallength` * 10) AS `sepallength` FROM DQC_0221_dev.`tmp_pyodps_d9e5d64e_1f21_4ffb_993f_70d3f36b6553` t1
   sepallength
0 3.891820 1 3.850148 2 3.828641 3 3.912023 4 3.988984 Sql compiled: CREATE TABLE tmp_pyodps_deb6fa45_fbb1_41d2_8174_76d35eebea9c LIFECYCLE 1 AS SELECT t1.`sepallength`, t1.`sepallength` / 2 AS `sepallength/2`, POW(t1.`sepallength`, 2) AS `sepallength的平方` FROM DQC_0221_dev.`tmp_pyodps_d9e5d64e_1f21_4ffb_993f_70d3f36b6553` t1
   sepallength  sepallength/2  sepallength的平方
0 4.9 2.45 24.01 1 4.7 2.35 22.09 2 4.6 2.30 21.16 3 5.0 2.50 25.00 4 5.4 2.70 29.16 Sql compiled: CREATE TABLE tmp_pyodps_fa326546_c5e8_466f_915d_e783b7dcacdf LIFECYCLE 1 AS SELECT t1.`sepallength` < 5 AS `sepallength` FROM DQC_0221_dev.`tmp_pyodps_d9e5d64e_1f21_4ffb_993f_70d3f36b6553` t1
```

`ll` `th`

```
  sepallength
0 True 1 True 2 True 3 False 4 False
          a                               b  id
0 [a1, b1] {u'c2': 2, u'a2': 0, u'b2': 1} 1 1 [c1] {u'd2': 3, u'e2': 4} 2 odps.Schema {
  a   list<string>
  b   dict<string,int64>
  id  int64
}
          a                               b  id
0 [a1, b1] {u'c2': 2, u'a2': 0, u'b2': 1} 1 1 [c1] {u'd2': 3, u'e2': 4} 2
   id   a  b
0 1 a1 3 1 2 c1 2
```

a

```
0 a1 1 b1 2 c1
   a_pos   a
0 0 a1 1 1 b1 2 0 c1
  b_key  b_value
0 c2 2 1 a2 0 2 b2 1 3 d2 3 4 e2 4
  key  value
0 c2 2 1 a2 0 2 b2 1 3 d2 3 4 e2 4
   id   a
0 1 a1 1 1 b1 2 2 c1 Sql compiled: CREATE TABLE tmp_pyodps_fb28d9b9_fa45_4712_a564_dd751641286e LIFECYCLE 1 AS SELECT t1.`sepallength` IN (4.9, 5.1) AS `sepallength` FROM DQC_0221_dev.`tmp_pyodps_d9e5d64e_1f21_4ffb_993f_70d3f36b6553` t1
   sepallength
0 True 1 False 2 False 3 False 4 False 5 False 6 False 7 False 8 True 9 False 10 False 11 False 12 False 13 False 14 False 15 False 16 True 17 False 18 True 19 False 20 True 21 False 22 True 23 False 24 False 25 False 26 False 27 False 28 False 29 False 30 False 31 False 32 False
```

```
33 True 34 False 35 False 36 True 37 False 38 True 39 False 40 False 41 False 42 False 43 True 44 False 45 True 46 False 47 False 48 False 49 False 50 False 51 False 52 False 53 False 54 False 55 False 56 True 57 False 58 False 59 False Sql compiled: CREATE TABLE tmp_pyodps_1f85e8e1_a9f0_473f_ac0e_d526fdd80dc4 LIFECYCLE 1 AS SELECT CASE WHEN (0 < t1.`sepallength`) AND (t1.`sepallength` <= 1) THEN '0-1' WHEN (1 < t1.`sepallength`) AND (t1.`sepallength` <= 2) THEN '1-2' WHEN (2 < t1.`sepallength`) AND (t1.`sepallength` <= 3) THEN '2-3' WHEN (3 < t1.`sepallength`) AND (t1.`sepallength` <= 4) THEN '3-4' WHEN (4 < t1.`sepallength`) AND (t1.`sepallength` <= 5) THEN '4-5' END AS `sepallength_cut` FROM DQC_0221_dev.`tmp_pyodps_d9e5d64e_1f21_4ffb_993f_70d3f36b6553` t1
  sepallength_cut
0 4-5 1 4-5 2 4-5 3 4-5 4 None Sql compiled: CREATE TABLE tmp_pyodps_080a677e_904b_4edc_a961_160f8c664d7f LIFECYCLE 1 AS SELECT CASE WHEN (0 < t1.`sepallength`) AND (t1.`sepallength` <= 1) THEN '0-1' WHEN (1 < t1.`sepallength`) AND (t1.`sepallength` <= 2) THEN '1-2' WHEN (2 < t1.`sepallength`) AND (t1.`sepallength` <= 3) THEN '2-3' WHEN (3 < t1.`sepallength`) AND (t1.`sepallength` <= 4) THEN '3-4' WHEN (4 < t1.`sepallength`) AND (t1.`sepallength` <= 5) THEN '4-5' WHEN 5 < t1.`sepallength` THEN '5-' END AS `sepallength_cut` FROM DQC_0221_dev.`tmp_pyodps_d9e5d64e_1f21_4ffb_993f_70d3f36b6553` t1
```

#### 9.9.10. PyODPS的排序

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 ii. 创建表**pyodps_iris**并上传数据集iris.csv。操作方法请参见DataWorks中的建表并上传数据文档。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 登录DataWorks控制台。
3. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。
4. 输入节点**名称**，单击**确认**。
5. 在PyODPS节点输入如下代码实现数据排序。
#排序

```
print iris.sort('sepalwidth').head(5)
```

#降序排列两种方式
#设置参数ascending=False;进行降序排列

```
print iris.sort('sepalwidth',ascending=False).head(5)
```

#设置-实现降序排列

```
print iris.sort(-iris.sepalwidth).head(5)
```

#多字段排序

```
print iris.sort(['sepalwidth','petallength']).head(5)
```

#多字段排序时，如果是升序降序不同，`ascending`参数可以用于传入一个列表，长度必须等同于排序的字段，它们的值都是`BOOLEAN`类型

```
print iris.sort(['sepalwidth','petallength'],ascending=[True,False]).head(5) print iris.sort(['sepalwidth',-iris.petallength]).head(5)
```

6. 单击运行。
7. 在**运行日志**中查看运行结果。
完整的运行结果如下：

```
Sql compiled: CREATE TABLE tmp_pyodps_d1b06785_dc18_4288_ad34_de860de1be08 LIFECYCLE 1 AS SELECT * ORDER BY sepalwidth LIMIT 10000 Instance ID: 20191010061554817gwml0lim
   sepallength  sepalwidth  petallength  petalwidth             name
0 5.0 2.0 3.5 1.0 Iris-versicolor 1 6.0 2.2 5.0 1.5 Iris-virginica 2 6.2 2.2 4.5 1.5 Iris-versicolor 3 6.0 2.2 4.0 1.0 Iris-versicolor 4 5.5 2.3 4.0 1.3 Iris-versicolor Sql compiled: CREATE TABLE tmp_pyodps_3cb90bb2_fb95_43fb_ae84_f2b5a27d72dc LIFECYCLE 1 AS SELECT * ORDER BY sepalwidth DESC LIMIT 10000 Instance ID: 20191010061601287gs086792
   sepallength  sepalwidth  petallength  petalwidth         name
0 5.7 4.4 1.5 0.4 Iris-setosa 1 5.5 4.2 1.4 0.2 Iris-setosa 2 5.2 4.1 1.5 0.1 Iris-setosa 3 5.8 4.0 1.2 0.2 Iris-setosa
```

```
4 5.4 3.9 1.3 0.4 Iris-setosa Sql compiled: CREATE TABLE tmp_pyodps_97b080bb_e014_48e8_a310_4b45fcd6a2ed LIFECYCLE 1 AS SELECT * ORDER BY sepalwidth DESC LIMIT 10000 Instance ID: 20191010061606927g6emz192
   sepallength  sepalwidth  petallength  petalwidth         name
0 5.7 4.4 1.5 0.4 Iris-setosa 1 5.5 4.2 1.4 0.2 Iris-setosa 2 5.2 4.1 1.5 0.1 Iris-setosa 3 5.8 4.0 1.2 0.2 Iris-setosa 4 5.4 3.9 1.3 0.4 Iris-setosa Sql compiled: CREATE TABLE tmp_pyodps_6fe37b6e_6705_4052_b733_211eb9bd16ac LIFECYCLE 1 AS SELECT * ORDER BY sepalwidth, petallength LIMIT 10000 Instance ID: 20191010061611714gn586792
   sepallength  sepalwidth  petallength  petalwidth             name
0 5.0 2.0 3.5 1.0 Iris-versicolor 1 6.0 2.2 4.0 1.0 Iris-versicolor 2 6.2 2.2 4.5 1.5 Iris-versicolor 3 6.0 2.2 5.0 1.5 Iris-virginica 4 4.5 2.3 1.3 0.3 Iris-setosa Sql compiled: CREATE TABLE tmp_pyodps_a52c805c_94a1_4a75_a6af_4fc9ed06ae68 LIFECYCLE 1 AS SELECT * ORDER BY sepalwidth, petallength DESC LIMIT 10000 Instance ID: 20191010061616553gw3m9592
   sepallength  sepalwidth  petallength  petalwidth             name
0 5.0 2.0 3.5 1.0 Iris-versicolor 1 6.0 2.2 5.0 1.5 Iris-virginica 2 6.2 2.2 4.5 1.5 Iris-versicolor 3 6.0 2.2 4.0 1.0 Iris-versicolor 4 6.3 2.3 4.4 1.3 Iris-versicolor Sql compiled: CREATE TABLE tmp_pyodps_aac5538e_9b40_4078_b3c6_852b99c663c1 LIFECYCLE 1 AS SELECT * ORDER BY sepalwidth, petallength DESC LIMIT 10000 Instance ID: 20191010061621329gvmkc292
   sepallength  sepalwidth  petallength  petalwidth             name
0 5.0 2.0 3.5 1.0 Iris-versicolor 1 6.0 2.2 5.0 1.5 Iris-virginica 2 6.2 2.2 4.5 1.5 Iris-versicolor 3 6.0 2.2 4.0 1.0 Iris-versicolor 4 6.3 2.3 4.4 1.3 Iris-versicolor
```

#### 9.9.11. PyODPS的去重

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 ii. 创建表**pyodps_iris**并上传数据集iris.csv。操作方法请参见DataWorks中的建表并上传数据文档。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 登录DataWorks控制台。
3. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。
4. 输入节点**名称**，单击**确认**。
5. 在PyODPS节点输入代码实现数据去重。
示例代码如下。

```
print iris[['name']].distinct() print iris.distinct('name') print iris.distinct('name','sepallength').head(3)
```

#您可以调用`unique`对`Sequence`进行去重操作，但是调用`unique`的`Sequence`不能用在列选择中

```
print iris.name.unique()
```

6. 单击运行。
7. 在**运行日志**中查看运行结果。
完整的运行结果如下：

```
Sql compiled: CREATE TABLE tmp_pyodps_ed85ebd5_d678_44dd_9ece_bff1822376f6 LIFECYCLE 1 AS SELECT DISTINCT t1.`name` Instance ID: 2019101006391142g2cp5692
              name
0 Iris-setosa 1 Iris-versicolor 2 Iris-virginica Sql compiled: CREATE TABLE tmp_pyodps_8ce6128f_9c6f_45af_b9de_c73ce9d5ba51 LIFECYCLE 1 AS SELECT DISTINCT t1.`name` Instance ID: 20191010063915987gmuws592
              name
0 Iris-setosa 1 Iris-versicolor 2 Iris-virginica Sql compiled: CREATE TABLE tmp_pyodps_a3dc338e_0fea_4d5f_847c_79fb19ec1c72 LIFECYCLE 1 AS SELECT DISTINCT t1.`name`, t1.`sepallength` Instance ID: 2019101006392210gj056292
          name  sepallength
0 Iris-setosa 4.3 1 Iris-setosa 4.4 2 Iris-setosa 4.5 Sql compiled: CREATE TABLE tmp_pyodps_bc0917bb_f10c_426b_9b75_47e94478382a LIFECYCLE 1 AS SELECT t2.`name` FROM (
  SELECT DISTINCT t1.`name`
) t2 Instance ID: 20191010063927189g9fsz192
              name
0 Iris-setosa 1 Iris-versicolor 2 Iris-virginica
```

#### 9.9.12. PyODPS的采样

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 ii. 创建表**pyodps_iris**并上传数据集iris.csv。操作方法请参见DataWorks中的建表并上传数据文档。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 登录DataWorks控制台。
3. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。
4. 输入节点**名称**，单击**确认**。
5. 在PyODPS节点输入采样代码。
示例代码如下。
#采样
#按份数采样
`print iris.sample(parts=10).head(5) #`分为`10`，分默认取第0份

```
print iris.sample(parts=10,i=0).head(5) #手动指定取第0份
```

`print iris.sample(parts=10,i=[2,5]).head(5) #`分成`10`份，取第2和第5份

```
print iris.sample(parts=10,columns=['name','sepalwidth']).head(5) #根据name和sepalwidth的值做采样
```

#按比例、条数采样

```
print iris.sample(n=100).head() #选取100条数据 print iris.sample(frac=0.3).head() #采样30%的数据
```

#按权重列采样

```
print iris.sample(n=100,weights='sepallength').head() print iris.sample(n=100,weights='sepalwidth',replace=True).head()
```

#分层采样

```
print iris.sample(strata='name',n={'Iris-setosa' : 10,'Iris-versicolor' : 10}).head() print iris.sample(strata='name',frac={'Iris-setosa': 0.5,'Iris-versicolor': 0.4}).head()
```

6. 单击运行。
7. 在**运行日志**中查看运行结果。
完整的运行结果如下。

```
  odps.Table
    schema:
      sepallength           : double      # 片长度(cm)
      sepalwidth            : double      # 片宽度(cm)
      petallength           : double      # 瓣长度(cm)
      petalwidth            : double      # 瓣宽度(cm)
      name                  : string      # 种类
  _input:
  _parts:
    Scalar[int8]
  _i:
  _replace:
    Scalar[boolean]
      False
  odps.Table
    schema:
      sepallength           : double      # 片长度(cm)
      sepalwidth            : double      # 片宽度(cm)
      petallength           : double      # 瓣长度(cm)
      petalwidth            : double      # 瓣宽度(cm)
      name                  : string      # 种类
  _input:
```

```
  _parts:
    Scalar[int8]
  _i:
  _replace:
    Scalar[boolean]
      False
  odps.Table
    schema:
      sepallength           : double      # 片长度(cm)
      sepalwidth            : double      # 片宽度(cm)
      petallength           : double      # 瓣长度(cm)
      petalwidth            : double      # 瓣宽度(cm)
      name                  : string      # 种类
  _input:
  _parts:
    Scalar[int8]
  _i:
  _replace:
    Scalar[boolean]
      False
  odps.Table
    schema:
      sepallength           : double      # 片长度(cm)
      sepalwidth            : double      # 片宽度(cm)
      petallength           : double      # 瓣长度(cm)
      petalwidth            : double      # 瓣宽度(cm)
      name                  : string      # 种类
  _input:
  _parts:
    Scalar[int8]
  _i:
  _sampled_fields:
    name = Column[sequence(string)] 'name' from collection ref_0
    sepalwidth = Column[sequence(float64)] 'sepalwidth' from collection ref_0
  _replace:
    Scalar[boolean]
      False
Executing RandomSample... Command: PAI -name RandomSample -project algo_public -Dreplace="false" -Dlifecycle="1" - DoutputTableName="tmp_pyodps_1570690014_69f3d75d_9537_4c9c_87ea_a5f6ad8d2e07" -DsampleSize="100" - DinputTableName="WB_BestPractice_dev.pyodps_iris"; Instance ID: 20191010064654985g6co9592 Sub Instance: create_output (20191010064700688g5cbn62m_71ee0561_bcc4_4147_b849_f74688353fb6) Sub Instance: without_replacement (20191010064703694g9cbn62m_93a8a15b_ffd1_4afe_8928_19f28455a15c) Try to fetch data from tunnel
    sepallength  sepalwidth  petallength  petalwidth            name
0 5.1 3.5 1.4 0.2 Iris-setosa 1 4.9 3.0 1.4 0.2 Iris-setosa 2 4.7 3.2 1.3 0.2 Iris-setosa 3 4.6 3.1 1.5 0.2 Iris-setosa 4 5.0 3.6 1.4 0.2 Iris-setosa 5 4.6 3.4 1.4 0.3 Iris-setosa 6 4.4 2.9 1.4 0.2 Iris-setosa 7 4.9 3.1 1.5 0.1 Iris-setosa 8 4.8 3.4 1.6 0.2 Iris-setosa 9 4.8 3.0 1.4 0.1 Iris-setosa 10 4.3 3.0 1.1 0.1 Iris-setosa 11 5.1 3.5 1.4 0.3 Iris-setosa 12 5.7 3.8 1.7 0.3 Iris-setosa 13 5.1 3.8 1.5 0.3 Iris-setosa 14 5.1 3.7 1.5 0.4 Iris-setosa 15 4.6 3.6 1.0 0.2 Iris-setosa 16 5.1 3.3 1.7 0.5 Iris-setosa 17 4.8 3.4 1.9 0.2 Iris-setosa 18 5.0 3.4 1.6 0.4 Iris-setosa 19 5.2 3.5 1.5 0.2 Iris-setosa 20 5.2 3.4 1.4 0.2 Iris-setosa 21 4.8 3.1 1.6 0.2 Iris-setosa 22 5.2 4.1 1.5 0.1 Iris-setosa 5.5 4.2 1.4 0.2 Iris-setosa
```

```
23 5.5 4.2 1.4 0.2 Irissetosa 24 4.9 3.1 1.5 0.1 Iris-setosa 25 5.0 3.2 1.2 0.2 Iris-setosa 26 4.4 3.0 1.3 0.2 Iris-setosa 27 5.1 3.4 1.5 0.2 Iris-setosa 28 5.0 3.5 1.3 0.3 Iris-setosa 29 4.5 2.3 1.3 0.3 Iris-setosa .. ... ... ... ... ... 70 7.1 3.0 5.9 2.1 Iris-virginica 71 7.6 3.0 6.6 2.1 Iris-virginica 72 7.3 2.9 6.3 1.8 Iris-virginica 73 7.2 3.6 6.1 2.5 Iris-virginica 74 6.5 3.2 5.1 2.0 Iris-virginica 75 6.8 3.0 5.5 2.1 Iris-virginica 76 5.8 2.8 5.1 2.4 Iris-virginica 77 7.7 3.8 6.7 2.2 Iris-virginica 78 7.7 2.6 6.9 2.3 Iris-virginica 79 7.7 2.8 6.7 2.0 Iris-virginica 80 6.3 2.7 4.9 1.8 Iris-virginica 81 6.7 3.3 5.7 2.1 Iris-virginica 82 6.2 2.8 4.8 1.8 Iris-virginica 83 6.1 3.0 4.9 1.8 Iris-virginica 84 6.4 2.8 5.6 2.1 Iris-virginica 85 7.2 3.0 5.8 1.6 Iris-virginica 86 7.4 2.8 6.1 1.9 Iris-virginica 87 7.9 3.8 6.4 2.0 Iris-virginica 88 6.3 2.8 5.1 1.5 Iris-virginica 89 6.3 3.4 5.6 2.4 Iris-virginica 90 6.4 3.1 5.5 1.8 Iris-virginica 91 6.0 3.0 4.8 1.8 Iris-virginica 92 6.9 3.1 5.4 2.1 Iris-virginica 93 6.9 3.1 5.1 2.3 Iris-virginica 94 5.8 2.7 5.1 1.9 Iris-virginica 95 6.8 3.2 5.9 2.3 Iris-virginica 96 6.7 3.3 5.7 2.5 Iris-virginica 97 6.3 2.5 5.0 1.9 Iris-virginica 98 6.2 3.4 5.4 2.3 Iris-virginica 99 5.9 3.0 5.1 1.8 Iris-virginica [100 rows x 5 columns] Executing RandomSample... Command: PAI -name RandomSample -project algo_public -Dreplace="false" -DsampleRatio="0.3" - DoutputTableName="tmp_pyodps_1570690039_e1867332_72ea_4656_928d_3bd6e31d87c7" -Dlifecycle="1" - DinputTableName="WB_BestPractice_dev.pyodps_iris"; Instance ID: 20191010064720117gmpms38 Sub Instance: create_output (20191010064725740grcbn62m_b338a671_6047_4360_8792_41d2e748e41f) Sub Instance: without_replacement (20191010064728747gtcbn62m_6c9914da_d5c3_4336_b076_163edb1bf48a) Try to fetch data from tunnel
    sepallength  sepalwidth  petallength  petalwidth             name
0 5.1 3.5 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 4.6 3.1 1.5 0.2 Iris-setosa 3 4.8 3.4 1.6 0.2 Iris-setosa 4 5.7 4.4 1.5 0.4 Iris-setosa 5 5.1 3.5 1.4 0.3 Iris-setosa 6 5.0 3.4 1.6 0.4 Iris-setosa 7 5.2 3.4 1.4 0.2 Iris-setosa 8 4.9 3.1 1.5 0.1 Iris-setosa 9 5.5 3.5 1.3 0.2 Iris-setosa 10 4.4 3.2 1.3 0.2 Iris-setosa 11 5.0 3.3 1.4 0.2 Iris-setosa 12 5.7 2.8 4.5 1.3 Iris-versicolor 13 5.2 2.7 3.9 1.4 Iris-versicolor 14 5.0 2.0 3.5 1.0 Iris-versicolor 15 5.6 2.9 3.6 1.3 Iris-versicolor 16 5.8 2.7 4.1 1.0 Iris-versicolor 17 6.1 2.8 4.0 1.3 Iris-versicolor 18 6.6 3.0 4.4 1.4 Iris-versicolor 19 6.8 2.8 4.8 1.4 Iris-versicolor 20 6.0 2.9 4.5 1.5 Iris-versicolor 21 5.4 3.0 4.5 1.5 Iris-versicolor 22 5.7 2.9 4.2 1.3 Iris-versicolor 23 5.7 2.8 4.1 1.3 Iris-versicolor 24 6.3 2.9 5.6 1.8 Iris-virginica 25 4.9 2.5 4.5 1.7 Iris-virginica 26 6.7 2.5 5.8 1.8 Iris-virginica 27 6.4 2.7 5.3 1.9 Iris-virginica 28 6.8 3.0 5.5 2.1 Iris-virginica 29 5.7 2.5 5.0 2.0 Iris-virginica 30 5.8 2.8 5.1 2.4 Iris-virginica 31 6.5 3.0 5.5 1.8 Iris-virginica 32 6.0 2.2 5.0 1.5 Iris-virginica
```

```
33 6.3 2.7 4.9 1.8 Iris-virginica 34 7.2 3.2 6.0 1.8 Iris-virginica 35 6.2 2.8 4.8 1.8 Iris-virginica 36 6.1 3.0 4.9 1.8 Iris-virginica 37 6.4 2.8 5.6 2.1 Iris-virginica 38 7.2 3.0 5.8 1.6 Iris-virginica 39 6.3 2.8 5.1 1.5 Iris-virginica 40 6.4 3.1 5.5 1.8 Iris-virginica 41 6.0 3.0 4.8 1.8 Iris-virginica 42 6.8 3.2 5.9 2.3 Iris-virginica 43 6.3 2.5 5.0 1.9 Iris-virginica 44 6.2 3.4 5.4 2.3 Iris-virginica Executing WeightedSample... Command: PAI -name WeightedSample -project algo_public -DinputTableName="WB_BestPractice_dev.pyodps_iris" -DsampleSize="100" - DprobCol="sepallength" -Dreplace="false" -DoutputTableName="tmp_pyodps_1570690063_6a62857e_8f85_4ea7_99ef_08aa259546d4" -Dlifecycle="1" ; Instance ID: 20191010064743533gnpms38 Sub Instance: create_output (20191010064748787gkdbn62m_8d47bfb7_e470_4cce_8b69_28811f190083) Sub Instance: without_replacement (20191010064751793gmdbn62m_230a1d26_5c2e_440e_a31d_fe9e63c6f906) Try to fetch data from tunnel
    sepallength  sepalwidth  petallength  petalwidth             name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 5.0 3.6 1.4 0.2 Iris-setosa 3 5.4 3.9 1.7 0.4 Iris-setosa 4 5.0 3.4 1.5 0.2 Iris-setosa 5 4.4 2.9 1.4 0.2 Iris-setosa 6 4.8 3.4 1.6 0.2 Iris-setosa 7 4.8 3.0 1.4 0.1 Iris-setosa 8 5.4 3.9 1.3 0.4 Iris-setosa 9 5.1 3.5 1.4 0.3 Iris-setosa 10 5.7 3.8 1.7 0.3 Iris-setosa 11 4.6 3.6 1.0 0.2 Iris-setosa 12 5.0 3.4 1.6 0.4 Iris-setosa 13 5.2 3.5 1.5 0.2 Iris-setosa 14 5.2 3.4 1.4 0.2 Iris-setosa 15 4.7 3.2 1.6 0.2 Iris-setosa 16 4.8 3.1 1.6 0.2 Iris-setosa 17 5.5 4.2 1.4 0.2 Iris-setosa 18 4.9 3.1 1.5 0.1 Iris-setosa 19 5.0 3.2 1.2 0.2 Iris-setosa 20 5.5 3.5 1.3 0.2 Iris-setosa 21 4.9 3.1 1.5 0.1 Iris-setosa 22 5.1 3.4 1.5 0.2 Iris-setosa 23 4.5 2.3 1.3 0.3 Iris-setosa 24 4.8 3.0 1.4 0.3 Iris-setosa 25 5.1 3.8 1.6 0.2 Iris-setosa 26 4.6 3.2 1.4 0.2 Iris-setosa 27 5.3 3.7 1.5 0.2 Iris-setosa 28 5.0 3.3 1.4 0.2 Iris-setosa 29 7.0 3.2 4.7 1.4 Iris-versicolor .. ... ... ... ... ... 70 7.2 3.6 6.1 2.5 Iris-virginica 71 6.4 2.7 5.3 1.9 Iris-virginica 72 5.7 2.5 5.0 2.0 Iris-virginica 73 5.8 2.8 5.1 2.4 Iris-virginica 74 6.4 3.2 5.3 2.3 Iris-virginica 75 7.7 3.8 6.7 2.2 Iris-virginica 76 6.9 3.2 5.7 2.3 Iris-virginica 77 5.6 2.8 4.9 2.0 Iris-virginica 78 7.7 2.8 6.7 2.0 Iris-virginica 79 6.3 2.7 4.9 1.8 Iris-virginica 80 6.7 3.3 5.7 2.1 Iris-virginica 81 7.2 3.2 6.0 1.8 Iris-virginica 82 6.2 2.8 4.8 1.8 Iris-virginica 83 6.1 3.0 4.9 1.8 Iris-virginica 84 7.2 3.0 5.8 1.6 Iris-virginica 85 7.9 3.8 6.4 2.0 Iris-virginica 86 6.4 2.8 5.6 2.2 Iris-virginica 87 6.3 2.8 5.1 1.5 Iris-virginica 88 6.1 2.6 5.6 1.4 Iris-virginica 89 6.3 3.4 5.6 2.4 Iris-virginica 90 6.4 3.1 5.5 1.8 Iris-virginica 91 6.0 3.0 4.8 1.8 Iris-virginica 92 6.9 3.1 5.1 2.3 Iris-virginica 93 5.8 2.7 5.1 1.9 Iris-virginica 94 6.8 3.2 5.9 2.3 Iris-virginica 95 6.7 3.3 5.7 2.5 Iris-virginica 96 6.7 3.0 5.2 2.3 Iris-virginica Iris-virginica
```

```
97 6.5 3.0 5.2 2.0 Iris-virginica 98 6.2 3.4 5.4 2.3 Iris-virginica 99 5.9 3.0 5.1 1.8 Iris-virginica [100 rows x 5 columns] Executing WeightedSample... Command: PAI -name WeightedSample -project algo_public -DinputTableName="WB_BestPractice_dev.pyodps_iris" -DsampleSize="100" - DprobCol="sepalwidth" -Dreplace="true" -DoutputTableName="tmp_pyodps_1570690082_f55e899c_3cb4_4eeb_ade4_b8cb79e018dc" -Dlifecycle="1"; Instance ID: 2019101006480392g9ers38 Sub Instance: create_output (20191010064808827g9ebn62m_fb70c859_913a_4830_9248_8c8eaf134f1d) Sub Instance: with_replacement (20191010064811833gdebn62m_07544cc2_1d7d_4fa5_972d_196eb6b9f537)
    sepallength  sepalwidth  petallength  petalwidth             name
0 5.1 3.5 1.4 0.2 Iris-setosa 1 4.6 3.4 1.4 0.3 Iris-setosa 2 5.0 3.4 1.5 0.2 Iris-setosa 3 5.0 3.4 1.5 0.2 Iris-setosa 4 4.4 2.9 1.4 0.2 Iris-setosa 5 4.8 3.4 1.6 0.2 Iris-setosa 6 5.8 4.0 1.2 0.2 Iris-setosa 7 5.8 4.0 1.2 0.2 Iris-setosa 8 5.1 3.5 1.4 0.3 Iris-setosa 9 5.1 3.5 1.4 0.3 Iris-setosa 10 5.1 3.5 1.4 0.3 Iris-setosa 11 5.1 3.7 1.5 0.4 Iris-setosa 12 4.6 3.6 1.0 0.2 Iris-setosa 13 4.8 3.4 1.9 0.2 Iris-setosa 14 5.0 3.0 1.6 0.2 Iris-setosa 15 5.0 3.4 1.6 0.4 Iris-setosa 16 5.2 3.4 1.4 0.2 Iris-setosa 17 4.8 3.1 1.6 0.2 Iris-setosa 18 4.8 3.1 1.6 0.2 Iris-setosa 19 5.4 3.4 1.5 0.4 Iris-setosa 20 5.4 3.4 1.5 0.4 Iris-setosa 21 5.4 3.4 1.5 0.4 Iris-setosa 22 5.2 4.1 1.5 0.1 Iris-setosa 23 5.2 4.1 1.5 0.1 Iris-setosa 24 5.5 4.2 1.4 0.2 Iris-setosa 25 5.0 3.2 1.2 0.2 Iris-setosa 26 4.9 3.1 1.5 0.1 Iris-setosa 27 4.4 3.0 1.3 0.2 Iris-setosa 28 5.1 3.4 1.5 0.2 Iris-setosa 29 5.0 3.5 1.3 0.3 Iris-setosa .. ... ... ... ... ... 70 5.6 2.7 4.2 1.3 Iris-versicolor 71 5.7 2.9 4.2 1.3 Iris-versicolor 72 6.3 3.3 6.0 2.5 Iris-virginica 73 7.1 3.0 5.9 2.1 Iris-virginica 74 6.3 2.9 5.6 1.8 Iris-virginica 75 7.3 2.9 6.3 1.8 Iris-virginica 76 7.2 3.6 6.1 2.5 Iris-virginica 77 6.4 2.7 5.3 1.9 Iris-virginica 78 6.8 3.0 5.5 2.1 Iris-virginica 79 6.8 3.0 5.5 2.1 Iris-virginica 80 5.8 2.8 5.1 2.4 Iris-virginica 81 6.2 2.8 4.8 1.8 Iris-virginica 82 6.2 2.8 4.8 1.8 Iris-virginica 83 6.1 3.0 4.9 1.8 Iris-virginica 84 6.4 2.8 5.6 2.1 Iris-virginica 85 7.2 3.0 5.8 1.6 Iris-virginica 86 7.4 2.8 6.1 1.9 Iris-virginica 87 7.4 2.8 6.1 1.9 Iris-virginica 88 7.4 2.8 6.1 1.9 Iris-virginica 89 6.4 3.1 5.5 1.8 Iris-virginica 90 6.0 3.0 4.8 1.8 Iris-virginica 91 6.9 3.1 5.4 2.1 Iris-virginica 92 6.7 3.1 5.6 2.4 Iris-virginica 93 6.7 3.1 5.6 2.4 Iris-virginica 94 6.7 3.1 5.6 2.4 Iris-virginica 95 6.9 3.1 5.1 2.3 Iris-virginica 96 6.9 3.1 5.1 2.3 Iris-virginica 97 6.7 3.0 5.2 2.3 Iris-virginica 98 6.5 3.0 5.2 2.0 Iris-virginica 99 5.9 3.0 5.1 1.8 Iris-virginica [100 rows x 5 columns] Executing StratifiedSample... Command: PAI -name StratifiedSample -project algo_public -Dlifecycle="1" - DoutputTableName="tmp_pyodps_1570690104_6cc52795_2a86_4634_a905_740b3a426d3f" -DsampleSize="Iris-setosa:10,Iris-versicolor:10" -Dstrata ColName="name" -DinputTableName="WB_BestPractice_dev.pyodps_iris"; Instance ID: 20191010064824633gaco9592 Sub Instance: create_output (20191010064829870g4fbn62m_dfa297c5_23b5_43f5_bb17_83ba8d263630)
```

```
Sub Instance: stratified_sampling (20191010064831874g7fbn62m_fc9eddb7_42f1_49fe_8206_891ef451fb76) Try to fetch data from tunnel
    sepallength  sepalwidth  petallength  petalwidth             name
0 5.4 3.9 1.7 0.4 Iris-setosa 1 4.3 3.0 1.1 0.1 Iris-setosa 2 5.4 3.9 1.3 0.4 Iris-setosa 3 5.1 3.3 1.7 0.5 Iris-setosa 4 4.7 3.2 1.6 0.2 Iris-setosa 5 4.5 2.3 1.3 0.3 Iris-setosa 6 5.0 3.5 1.6 0.6 Iris-setosa 7 5.1 3.8 1.9 0.4 Iris-setosa 8 4.8 3.0 1.4 0.3 Iris-setosa 9 5.0 3.3 1.4 0.2 Iris-setosa 10 7.0 3.2 4.7 1.4 Iris-versicolor 11 5.5 2.3 4.0 1.3 Iris-versicolor 12 6.5 2.8 4.6 1.5 Iris-versicolor 13 5.6 3.0 4.5 1.5 Iris-versicolor 14 5.7 2.6 3.5 1.0 Iris-versicolor 15 5.5 2.4 3.7 1.0 Iris-versicolor 16 5.0 2.3 3.3 1.0 Iris-versicolor 17 5.6 2.7 4.2 1.3 Iris-versicolor 18 5.7 3.0 4.2 1.2 Iris-versicolor 19 5.1 2.5 3.0 1.1 Iris-versicolor Executing StratifiedSample... Command: PAI -name StratifiedSample -project algo_public -DsampleRatio="Iris-setosa:0.5,Iris-versicolor:0.4" - DoutputTableName="tmp_pyodps_1570690128_a68477cd_19e5_4fe0_bb39_4712f76dd967" -Dlifecycle="1" -DstrataColName="name" - DinputTableName="WB_BestPractice_dev.pyodps_iris"; Instance ID: 20191010064848733gbers38 Sub Instance: create_output (20191010064853918gwfbn62m_4eb22c22_7051_4372_8d13_05c5a417aa87) Sub Instance: stratified_sampling (20191010064855924g0gbn62m_b4242ac7_bd5a_47a8_a1f2_3367a6a101a7) Try to fetch data from tunnel
    sepallength  sepalwidth  petallength  petalwidth             name
0 4.9 3.0 1.4 0.2 Iris-setosa 1 4.7 3.2 1.3 0.2 Iris-setosa 2 5.0 3.6 1.4 0.2 Iris-setosa 3 5.4 3.9 1.7 0.4 Iris-setosa 4 5.0 3.4 1.5 0.2 Iris-setosa 5 5.4 3.7 1.5 0.2 Iris-setosa 6 4.8 3.4 1.6 0.2 Iris-setosa 7 4.8 3.0 1.4 0.1 Iris-setosa 8 5.8 4.0 1.2 0.2 Iris-setosa 9 5.4 3.4 1.7 0.2 Iris-setosa 10 5.1 3.7 1.5 0.4 Iris-setosa 11 4.8 3.4 1.9 0.2 Iris-setosa 12 5.0 3.0 1.6 0.2 Iris-setosa 13 5.0 3.4 1.6 0.4 Iris-setosa 14 5.2 3.5 1.5 0.2 Iris-setosa 15 5.2 3.4 1.4 0.2 Iris-setosa 16 4.7 3.2 1.6 0.2 Iris-setosa 17 5.2 4.1 1.5 0.1 Iris-setosa 18 5.0 3.2 1.2 0.2 Iris-setosa 19 5.1 3.4 1.5 0.2 Iris-setosa 20 4.5 2.3 1.3 0.3 Iris-setosa 21 5.0 3.5 1.6 0.6 Iris-setosa 22 5.1 3.8 1.9 0.4 Iris-setosa 23 5.1 3.8 1.6 0.2 Iris-setosa 24 5.3 3.7 1.5 0.2 Iris-setosa 25 7.0 3.2 4.7 1.4 Iris-versicolor 26 6.4 3.2 4.5 1.5 Iris-versicolor 27 6.9 3.1 4.9 1.5 Iris-versicolor 28 6.5 2.8 4.6 1.5 Iris-versicolor 29 5.7 2.8 4.5 1.3 Iris-versicolor 30 6.6 2.9 4.6 1.3 Iris-versicolor 31 5.6 2.9 3.6 1.3 Iris-versicolor 32 5.6 3.0 4.5 1.5 Iris-versicolor 33 5.6 2.5 3.9 1.1 Iris-versicolor 34 6.1 2.8 4.7 1.2 Iris-versicolor 35 6.8 2.8 4.8 1.4 Iris-versicolor 36 5.5 2.4 3.8 1.1 Iris-versicolor 37 5.5 2.4 3.7 1.0 Iris-versicolor 38 6.0 2.7 5.1 1.6 Iris-versicolor 39 5.6 3.0 4.1 1.3 Iris-versicolor 40 5.5 2.6 4.4 1.2 Iris-versicolor 41 6.1 3.0 4.6 1.4 Iris-versicolor 42 5.7 3.0 4.2 1.2 Iris-versicolor 43 5.7 2.9 4.2 1.3 Iris-versicolor 44 6.2 2.9 4.3 1.3 Iris-versicolor
```

#### 9.9.13. PyODPS的数据缩放

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 创建表并导入数据。
i. 下载鸢尾花数据集iris.data，重命名为iris.csv。 ii. 创建表**pyodps_iris**并上传数据集iris.csv。操作方法请参见DataWorks中的建表并上传数据文档。 建表语句如下。

```
( sepallength DOUBLE comment '片长度(cm)', sepalwidth DOUBLE comment '片宽度(cm)', petallength DOUBLE comment '瓣长度(cm)', petalwidth DOUBLE comment '瓣宽度(cm)', name STRING comment '种类' );
```

2. 登录DataWorks控制台。
3. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。
4. 输入节点**名称**，单击**确认**。
5. 在PyODPS 2节点中输入数据缩放代码。
示例代码如下：
#数据缩放
#使用`min_max_scale`方法进行归一化

```
print df.min_max_scale(columns=['fid']).head()
```

#min_max_scale还支持使用`feature_range`参数指定输出值的范围。例如，需要使输出值在`(-1,1)`范围内

```
print df.min_max_scale(columns=['fid'],feature_range=(-1,1)).head()
```

#如果需要保留原始值，可以使用`preserve`参数。此时，缩放后的数据将会以新增列的形式追加到数据中，列名默认为原列名追加`_scaled`后缀，该后缀可使用`suffix`参数更改

```
print df.min_max_scale(columns=['fid'],preserve=True).head()
```

#使用`group`分组

```
print df.min_max_scale(columns=['fid'],group=['name']).head()
```

#min_max_scale也支持使用`group`参数指定一个或多个分组列，在分组列中分别取最值进行缩放

```
print df.std_scale(columns=['fid']).head()
```

6. 单击运行。
7. 在**运行日志**中查看运行结果。
完整的运行结果如下：

```
Sql compiled: CREATE TABLE tmp_pyodps_59cb5533_6dc3_4b64_9312_b2da29d70cee LIFECYCLE 1 AS SELECT /*+mapjoin(t5)*/ t2.`name`, t2.`id`, (IF((t5.`fid_max_1570691133` - t5.`fid_min_1570691133`) == 0, 0, (t2.`fid` - t5.`fid_min_15 70691133`) / (t5.`fid_max_1570691133` - t5.`fid_min_1570691133`)) * 1) + 0 AS `fid` FROM (
  SELECT t1.`name`, t1.`id`, t1.`fid`, 1 AS `idx_col_1570691133`
  FROM WB_BestPractice_dev.`pytable` t1
) t2 INNER JOIN
  (
    SELECT 1 AS `idx_col_1570691133`, MIN(t4.`fid`) AS `fid_min_1570691133`, MAX(t4.`fid`) AS `fid_max_1570691133`
    FROM (
      SELECT t3.`fid`
      FROM WB_BestPractice_dev.`pytable` t3
    ) t4
  ) t5
ON t2.`idx_col_1570691133` == t5.`idx_col_1570691133` Instance ID: 2019101007053495gl8by72m
    name  id       fid
0 name1 4 1.000000 1 name2 2 0.526316 2 name2 3 0.000000 3 name1 4 0.710526 4 name1 3 0.184211 5 name1 3 0.684211 Sql compiled: CREATE TABLE tmp_pyodps_88a24967_3bdc_41ce_85d7_4bbd23e4ce01 LIFECYCLE 1 AS SELECT /*+mapjoin(t5)*/ t2.`name`, t2.`id`, (IF((t5.`fid_max_1570691139` - t5.`fid_min_1570691139`) == 0, 0, (t2.`fid` - t5.`fid_min_15 70691139`) / (t5.`fid_max_1570691139` - t5.`fid_min_1570691139`)) * 2) + -1 AS `fid` FROM (
  SELECT t1.`name`, t1.`id`, t1.`fid`, 1 AS `idx_col_1570691139`
  FROM WB_BestPractice_dev.`pytable` t1
) t2 INNER JOIN
  (
    SELECT 1 AS `idx_col_1570691139`, MIN(t4.`fid`) AS `fid_min_1570691139`, MAX(t4.`fid`) AS `fid_max_1570691139`
    FROM (
      SELECT t3.`fid`
      FROM WB_BestPractice_dev.`pytable` t3
    ) t4
  ) t5
ON t2.`idx_col_1570691139` == t5.`idx_col_1570691139` Instance ID: 20191010070539772gjo56292
    name  id       fid
0 name1 4 1.000000 1 name2 2 0.052632 2 name2 3 -1.000000 3 name1 4 0.421053 4 name1 3 -0.631579 5 name1 3 0.368421 Sqlcompiled:
```

`Sq`

```
cop ed: CREATE TABLE tmp_pyodps_439117fc_9ef7_4086_899d_a5bf77d653e5 LIFECYCLE 1 AS SELECT /*+mapjoin(t5)*/ t2.`name`, t2.`id`, t2.`fid`, (IF((t5.`fid_max_1570691146` - t5.`fid_min_1570691146`) == 0, 0, (t2.`fid` - t5.` fid_min_1570691146`) / (t5.`fid_max_1570691146` - t5.`fid_min_1570691146`)) * 1) + 0 AS `fid_scaled` FROM (
  SELECT t1.`name`, t1.`id`, t1.`fid`, 1 AS `idx_col_1570691146`
  FROM WB_BestPractice_dev.`pytable` t1
) t2 INNER JOIN
  (
    SELECT 1 AS `idx_col_1570691146`, MIN(t4.`fid`) AS `fid_min_1570691146`, MAX(t4.`fid`) AS `fid_max_1570691146`
    FROM (
      SELECT t3.`fid`
      FROM WB_BestPractice_dev.`pytable` t3
    ) t4
  ) t5
ON t2.`idx_col_1570691146` == t5.`idx_col_1570691146` Instance ID: 20191010070546769g0c14f72
    name  id  fid  fid_scaled
0 name1 4 5.3 1.000000 1 name2 2 3.5 0.526316 2 name2 3 1.5 0.000000 3 name1 4 4.2 0.710526 4 name1 3 2.2 0.184211 5 name1 3 4.1 0.684211 Sql compiled: CREATE TABLE tmp_pyodps_d3839b4b_1087_4d52_91f5_52763b72f272 LIFECYCLE 1 AS SELECT /*+mapjoin(t3)*/ t1.`name`, t1.`id`, (IF((t3.`fid_max_1570691151` - t3.`fid_min_1570691151`) == 0, 0, (t1.`fid` - t3.`fid_min_15 70691151`) / (t3.`fid_max_1570691151` - t3.`fid_min_1570691151`)) * 1) + 0 AS `fid` FROM WB_BestPractice_dev.`pytable` t1 INNER JOIN
  (
    SELECT t2.`name`, MAX(t2.`fid`) AS `fid_max_1570691151`, MIN(t2.`fid`) AS `fid_min_1570691151`
    FROM WB_BestPractice_dev.`pytable` t2
    GROUP BY t2.`name`
  ) t3
ON t1.`name` == t3.`name` Instance ID: 20191010070551756gtf14f72
    name  id       fid
0 name1 4 1.000000 1 name2 2 1.000000 2 name2 3 0.000000 3 name1 4 0.645161 4 name1 3 0.000000 5 name1 3 0.612903 Sql compiled: CREATE TABLE tmp_pyodps_1ea6e5b4_129f_4d1e_a6a7_410e08d77ae6 LIFECYCLE 1 AS SELECT /*+mapjoin(t5)*/ t2.`name`, t2.`id`, IF(t5.`fid_std_1570691157` == 0, 0, (t2.`fid` - t5.`fid_mean_1570691157`) / t5.`fid_std_157 0691157`) AS `fid` FROM (
  SELECT t1.`name`, t1.`id`, t1.`fid`, 1 AS `idx_col_1570691157`
  FROM WB_BestPractice_dev.`pytable` t1
) t2 INNER JOIN
  (
    SELECT 1 AS `idx_col_1570691157`, AVG(t4.`fid`) AS `fid_mean_1570691157`, STDDEV(t4.`fid`) AS `fid_std_1570691157`
    FROM (
      SELECT t3.`fid`
      FROM WB_BestPractice_dev.`pytable` t3
    ) t4
  ) t5
ON t2.`idx_col_1570691157` == t5.`idx_col_1570691157` Instance ID: 20191010070557788gdl14f72
    name  id       fid
0 name1 4 1.436467 1 name2 2 0.026118 2 name2 3 -1.540938 3 name1 4 0.574587 4 name1 3 -0.992468 5 name1 3 0.496234
```

#### 9.9.14. PyODPS的空值处理

**前提条件**

请提前完成如下操作： 已开通MaxCompute。 已开通DataWorks。 在DataWorks上完成业务流程创建，本例使用DataWorks简单模式。

**操作步骤**

1. 准备测试数据。
i. 登录DataWorks控制台。 ii. 创建表并上传数据。操作方法请参见DataWorks文档中的建表并上传数据。 表pytable2的建表语句如下。

```
CREATE TABLE `pytable2` (
  `id` string,
  `name` string,
  `f1` double,
  `f2` double,
  `f3` double,
  `f4` double
) ;
```

示例数据文件pytable2.txt的内容如下。

```
0, name1, 1.0, NaN, 3.0, 4.0 1, name1, 2.0, NaN, NaN, 1.0 2, name1, 3.0, 4.0, 1.0, NaN 3, name1, NaN, 1.0, 2.0, 3.0 4, name1, 1.0, NaN, 3.0, 4.0 5, name1, 1.0, 2.0, 3.0, 4.0 6, name1, NaN, NaN, NaN, NaN
```

2. 在**数据开发**页面，右键单击已经创建的业务流程，选择**新建节点** **> MaxCompute > PyODPS 2**。
3. 输入节点**名称**，单击**确认**。
4. 在PyODPS 2节点中输入空值处理代码。
示例代码如下：
#dropna方法，删除包含空值的行。

```
print df2.dropna(subset=['f1','f2','f3','f4']).head()
```

#包含非空值则不删除，可以使用`how='all'`。

```
print df2.dropna(how='all', subset=['f1','f2','f3','f4']).head() print df2.dropna(thresh=3, subset=['f1', 'f2', 'f3', 'f4']).head()
```

#fillna方法，使用常数或已有的列填充未知值。

```
print df2.fillna(100, subset=['f1','f2','f3','f4']).head()
```

#使用一个已有的列填充未知值。

```
print df2.fillna(df2.f2, subset=['f1','f2','f3','f4']).head()
```

#向前填充。

```
print df2.fillna(method='bfill', subset=['f1', 'f2', 'f3', 'f4']).head()
```

#向后填充。

```
print df2.fillna(method='ffill', subset=['f1', 'f2', 'f3', 'f4']).head()
```

5. 单击运行。
6. 在**运行日志**中查看运行结果。
完整的运行结果如下：

```
Sql compiled: CREATE TABLE tmp_pyodps_d0c7d8c2_be38_4d48_b0eb_e89bae5bde01 LIFECYCLE 1 AS SELECT * FROM WB_BestPractice_dev.`pytable2` t1 WHERE (((IF(t1.`f1` IS NOT NULL, 1, 0) + IF(t1.`f2` IS NOT NULL, 1, 0)) + IF(t1.`f3` IS NOT NULL, 1, 0)) + IF(t1.`f4` IS NOT NULL, 1, 0 )) >= 4 Instance ID: 20191010071154980g2hic292
  id   name   f1   f2   f3   f4
0 0 name1 1.0 NaN 3.0 4.0 1 1 name1 2.0 NaN NaN 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN Sql compiled: CREATE TABLE tmp_pyodps_49b46768_f589_48f6_be8a_b7139f31f6f2 LIFECYCLE 1 AS SELECT * FROM WB_BestPractice_dev.`pytable2` t1 WHERE (((IF(t1.`f1` IS NOT NULL, 1, 0) + IF(t1.`f2` IS NOT NULL, 1, 0)) + IF(t1.`f3` IS NOT NULL, 1, 0)) + IF(t1.`f4` IS NOT NULL, 1, 0 )) >= 1 Instance ID: 20191010071159759g0dk9592
  id   name   f1   f2   f3   f4
0 0 name1 1.0 NaN 3.0 4.0 1 1 name1 2.0 NaN NaN 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN Sql compiled: CREATE TABLE tmp_pyodps_7f941800_1539_415b_9257_283ebeb893a6 LIFECYCLE 1 AS SELECT * FROM WB_BestPractice_dev.`pytable2` t1 WHERE (((IF(t1.`f1` IS NOT NULL, 1, 0) + IF(t1.`f2` IS NOT NULL, 1, 0)) + IF(t1.`f3` IS NOT NULL, 1, 0)) + IF(t1.`f4` IS NOT NULL, 1, 0 )) >= 3 Instance ID: 20191010071204544giyswx7 0 0 name1 1.0 NaN 3.0 4.0 1 1 name1 2.0 NaN NaN 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN Sql compiled: CREATE TABLE tmp_pyodps_16d6ea6d_5195_4e4c_8346_644a395852f7 LIFECYCLE 1 AS SELECT t1.`id`, t1.`name`, IF(t1.`f1` IS NULL, 100, t1.`f1`) AS `f1`, IF(t1.`f2` IS NULL, 100, t1.`f2`) AS `f2`, IF(t1.`f3` IS NULL, 10 t1`f3`)AS`f3` IF(t1`f4`ISNULL t1`f4`)AS`f4`
```

```
0, t1.f3) AS f3, IF(t1.f4 IS NULL, 100, t1.f4) AS f4 FROM WB_BestPractice_dev.`pytable2` t1 Instance ID: 20191010071209190gyl56292
  id   name   f1   f2   f3   f4
0 0 name1 1.0 NaN 3.0 4.0 1 1 name1 2.0 NaN NaN 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN Sql compiled: CREATE TABLE tmp_pyodps_40755ebd_2d2a_482e_b360_3f3da0d5422c LIFECYCLE 1 AS SELECT t1.`id`, t1.`name`, IF(t1.`f1` IS NULL, t1.`f2`, t1.`f1`) AS `f1`, IF(t1.`f2` IS NULL, t1.`f2`, t1.`f2`) AS `f2`, IF(t1.`f3` IS NULL, t1.`f2`, t1.`f3`) AS `f3`, IF(t1.`f4` IS NULL, t1.`f2`, t1.`f4`) AS `f4` FROM WB_BestPractice_dev.`pytable2` t1 Instance ID: 20191010071213970gbp66792
  id   name   f1   f2   f3   f4
0 0 name1 1.0 NaN 3.0 4.0 1 1 name1 2.0 NaN NaN 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 NaN 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN Sql compiled: CREATE TABLE tmp_pyodps_d39fcce1_d8a9_4cc2_8aff_2ed1e9c6bb1b LIFECYCLE 1 AS SELECT pyodps_udf_1570691538_d9441c59_c666_4a5d_8154_67d8bc8c24ad(t1.`id`, t1.`name`, t1.`f1`, t1.`f2`, t1.`f3`, t1.`f4`) AS (`id`, `name`, `f1`, `f2`, `f3`, `f4`) FROM WB_BestPractice_dev.`pytable2` t1 Instance ID: 20191010071219627goqv9292
  id   name   f1   f2   f3   f4
0 0 name1 1.0 3.0 3.0 4.0 1 1 name1 2.0 1.0 1.0 1.0 2 2 name1 3.0 4.0 1.0 NaN 3 3 name1 1.0 1.0 2.0 3.0 4 4 name1 1.0 3.0 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN Sql compiled: CREATE TABLE tmp_pyodps_3f190cf0_f9fb_4e06_a942_ab31c0241cd3 LIFECYCLE 1 AS SELECT pyodps_udf_1570691566_0330848b_82d3_411c_88e1_cbbcc6adb9c1(t1.`id`, t1.`name`, t1.`f1`, t1.`f2`, t1.`f3`, t1.`f4`) AS (`id`, `name`, `f1`, `f2`, `f3`, `f4`) FROM WB_BestPractice_dev.`pytable2` t1 Instance ID: 20191010071247729gt776792
  id   name   f1   f2   f3   f4
0 0 name1 1.0 1.0 3.0 4.0 1 1 name1 2.0 2.0 2.0 1.0 2 2 name1 3.0 4.0 1.0 1.0 3 3 name1 NaN 1.0 2.0 3.0 4 4 name1 1.0 1.0 3.0 4.0 5 5 name1 1.0 2.0 3.0 4.0 6 6 name1 NaN NaN NaN NaN
```

### PyODPS常见问题

| 问题类别 | 常见问题 |
|---|---|
| 安装PyODPS | 安装PyODPS时，提示Warning: XXX not installed，如何解决？ 安装PyODPS时，提示Project Not Found，如何解决？ 安装PyODPS时，报错Syntax Error，如何解决？ 在Mac上安装PyODPS时，报错Permission Denied，如何解决？ 在Mac上安装PyODPS时，报错Operation Not Permitted，如何解决？ |
| 导入模块 | 执行from odps import ODPS时，报错No Module Named ODPS，如何解决？ 执行from odps import ODPS时，报错Cannot Import Name ODPS，如何解决？ 执行from odps import ODPS时，报错Cannot Import Module odps，如何解决？ 在Ipython或Jupyter下使用PyODPS时，报错ImportError，如何解决？ |

| 使用PyODPS | o.gettable('tablename').size中size字段的含义是什么？ _ 如何设置Tunnel Endpoint？ PyODPS如何使用包含cPython的第三方包？ PyODPS中的DataFrame最多可以处理多少数据，对表的大小有限制吗？ 在DataFrame中如何使用maxpt？ _ 使用PyODPS向表写入数据的两种方式openwriter()和writetable()有什么区别？ _ _ 为什么DataWorks PyODPS节点上查出的数据量要少于本地运行的结果？ DataFrame如何获得Count实际数值？ 使用PyODPS时，报错sourceIP is not in the white list，如何解决？ 使用from odps import options options.sql.settings设置MaxCompute运行环境不成功，如何解决？ 调用DataFrame的head方法时，报错IndexError:listindexoutofrange，是什么原因？ 上传Pandas DataFrame至MaxCompute时，报错ODPSError，如何解决？ 通过DataFrame写表时，报错lifecycle is not specified in mandatory mode，如何解决？ 使用PyODPS写数据时，提示Perhaps the datastream from server is crushed，如何解决？ 使用PyODPS读数据时，报错Project is protected，如何解决？ PyODPS脚本任务不定时出现连接失败，报错ConnectionError: timed out try catch exception，如何解决？ 使用PyODPS运行getsqltaskcost函数时，报错is not defined，如何解决？ _ _ _ 使用PyODPS打印日志时，中文自动转化为编码显示，如何显示成原始中文？ 设置options.tunnel.useinstancetunnel = False，为什么字段在MaxCompute中定义为DATETIME类型，使用 _ _ SELECT语句得到的数据为STRING类型？ 如何利用Python语言特性来实现丰富的功能？ 如何使用Pandas计算后端进行本地Debug？ 如何避免嵌套循环执行慢的情况？ 什么情况下可以下载PyODPS数据到本地处理？ 通过openreader最多只能取到1万条记录，如何获取多于1万条的记录？ _ 为什么尽量使用内建算子，而不是自定义函数？ 为什么通过DataFrame().schema.partitions获得分区表的分区值为空？ 如何使用PyODPS DataFrame执行笛卡尔积？ 如何使用PyODPS下载全量数据？ 使用PyODPS统计表中某个字段的空值率时，是用executesql还是DataFrame？ _ PyODPS数据类型如何设置？ 使用PyODPS时遇到ValueError，如何解决？ |
|---|---|

产生此问题的原因为组件缺失，请根据报错信息中提示的XXX信息，明确缺失的组件名称，使用 `pip` 命令安装此组件。 产生此问题的原因为： Endpoint配置错误，需要修改为目标Project的Endpoint。 MaxCompute入口对象参数位置填写错误。请检查此项确保其填写正确。 由于Python版本过低导致报错。不支持Python2.5及以下版本，建议使用PyODPS支持的主流版本，例如Python2.7.6+、Python3.3+以及Python2.6。

**在Mac上安装PyODPS时，报错Operation Not Permitted，如何解决？**

此报错是由系统完整性保护导致。您需要重启设备，并在重启中按⌘+R键，此后在终端中运行如下命令可以解决此问题。

```
csrutil disable reboot
```

更多信息，请参见Operation Not Permitted when on root - El Capitan (rootless disabled)。

**执行from odps import ODPS时，报错No Module Named ODPS，如何解决？**

此报错说明无法加载ODPS Package。无法加载的原因有如下几种： 原因一：安装了多个Python版本。 解决措施：Search Path（通常是当前目录）中包含 `odps.py` 或 `init.py` 文件且名为odps的文件夹。解决方法如下： 如果是文件夹重名，请修改文件夹名称。 如果是曾经安装过一个名为odps的Python包，请使用 `sudo pip uninstall odps` 进行删除。 原因二：同时安装了Python2和Python3版本。 解决措施：确保设备只安装了Python2或Python3版本。

**执行from odps import ODPS时，报错Cannot Import Name ODPS，如何解决？**

请检查当前工作路径下是否存在名为**odps.py**的文件。若存在，请改名后再执行导入操作。

**执行from odps import ODPS时，报错Cannot Import Module odps，如何解决？**

此报错通常是由于PyODPS遇到了依赖问题。您可以单击申请链接添加PyODPS技术支持钉钉群，联系钉群管理员定位解决。

**在Ipython或Jupyter下使用PyODPS时，报错ImportError，如何解决？**

| 部增加 | from odps import errors |  |
|---|---|---|
| from odps import errors |  | 也报错 |

**o.gettable('table_name').size中size字段的含义是什么？**

SIZE字段表示表的物理存储大小。

**如何设置Tunnel Endpoint？**

您可以通过 `options.tunnel.endpoint` 设置，请参见aliyun-odps-python-sdk。 建议您打包成WHEEL格式后使用，请参见如何制作可以在MaxCompute上使用的crcmod。 PyODPS对表的大小没有限制。本地Pandas创建DataFrame的大小受限于本地内存的大小。

| 使用 | odps.df.func | 模块来调用MaxCompute内建函数。 |
|---|---|---|
| from odps.df import func df = o.get_table('your_table').to_df() df[df.ds == func.max_pt('your_project.your_table')] # ds是分区字段。 |  |  |

**使用PyODPS向表写入数据的两种方式open_writer()和write_table()有什么区别？**

每次调用 `write_table()` ，MaxCompute都会在服务端生成一个文件。这一操作需要较大的时间开销，同时过多的文件会降低后续的查询效率，还可能造成服务端内存不足。因此，建议在使用 `write_table()` 方法时，一次性写入多组数据或者传入一个Generator对象。使用 `write_table()` 方法示例请参见写入表数据。 `open_writer()` 默认写入到Block中。

| unnel，即 | instance.open_reader |  |
|---|---|---|
| reader.count |  | 获取记录数。如果您 |

`False` 关闭Limit限制。
1. 安装PyODPS后，在Python环境下执行如下命令创建MaxCompute表来初始化DataFrame。
2. 在DataFrame上执行Count获取DataFrame的总行数。

```
iris.count()
```

3. 由于DataFrame上的操作并不会立即执行，只有当用户显式调用Execute方法或者立即执行的方法时，才会真正执行。此时为了防止Count方法延迟执行，可输入
如下命令。

```
df.count().execute()
```

获取DataFrame实际数量的相关方法请参见聚合操作。详细的PyODPS方法延迟操作，请参见执行。

**使用PyODPS时，报错sourceIP is not in the white list，如何解决？**

PyODPS访问的MaxCompute项目存在白名单保护，请联系项目所有者将设备添加至IP白名单。

**使用from odps import options options.sql.settings设置MaxCompute运行环境不成功，如何解决？**

问题现象使用PyODPS运行SQL，在申请MaxCompute实例前，通过如下代码设置MaxCompute运行环境。

```python
from odps import options options.sql.settings = {'odps.sql.mapper.split.size': 32}
```

运行任务后只启动了6个Mapper，设置未生效。在客户端执行 `set odps.stage.mapper.split.size=32` ，一分钟运行完毕。 产生原因客户端和PyODPS里设置的参数不一致。客户端的参数是 `odps.stage.mapper.split.size` ，而PyODPS里的参数是 `odps.sql.mapper.split.size` 。 解决措施修改参数为 `odps.stage.mapper.split.size` 。

**调用DataFrame的head方法时，报错IndexError:listindexoutofrange，是什么原因？**

由于 `list[index]` 没有元素或 `list[index]` 超出范围。

**上传Pandas DataFrame至MaxCompute时，报错ODPSError，如何解决？**

问题现象

```
ODPSError: ODPS entrance should be provided.
```

产生原因报错原因为没有找到全局的MaxCompute对象入口。 解决措施使用Room机制 %enter 时，会配置全局入口。

| ompute对象入口调用 | to_global | 方法。 |
|---|---|---|
| DataFrame(pd_df).persist('your_table', odps=odps) |  |  |

**通过DataFrame写表时，报错lifecycle is not specified in mandatory mode，如何解决？**

问题现象

```
table lifecycle is not specified in mandatory mode
```

产生原因未给表设置生命周期。 解决措施 Project要求对每张表设置生命周期，因此只需要在每次执行时设置如下信息即可。

```python
from odps import options
```

`options.lifecycle = 7 #` 此处设置`lifecycle`的值。`lifecycle`取值为整数，单位为天。

**使用PyODPS写数据时，提示Perhaps the datastream from server is crushed，如何解决？**

该报错是由脏数据导致，请您检查数据列数是否和目标表一致。 Project上的安全策略禁止读取表中的数据，如果想使用全部数据，可以使用以下方法： 联系Project Owner增加例外规则。 使用DataWorks或其他脱敏工具先对数据进行脱敏，导出到非保护Project，再进行读取。 如果只想查看部分数据，可使用如下方法：

| o.execute_sql('select * from <table_name>').open_reader() |  |
|---|---|
| DataFrame，o.get_table('<table_name>').to_df() | 。 |

**PyODPS脚本任务不定时出现连接失败，报错ConnectionError: timed out try catch exception，如何解决？**

产生此报错的可能原因如下： 您可以在代码头部加上如下代码，增加超时时间隔。

```
workaround from odps import options options.connect_timeout=30
```

捕获异常，进行重试。 由于沙箱限制，会造成部分机器禁止网络访问。建议您使用独享调度资源组执行任务，解决此问题。

**使用PyODPS运行get_sql_task_cost函数时，报错is not defined，如何解决？**

问题现象

```
NameError: name 'get_task_cost' is not defined.
```

解决措施函数名称有误。 解决措施使用execute_sql_cost替代get_sql_task_cost。 您可以使用类似 `print ("`我叫 %s" % ('abc')) 的输入方式解决。目前仅Python 2涉及此类问题。

**设置options.tunnel.use_instance_tunnel = False，为什么字段在MaxCompute中定义为DATETIME类型，使用**

在调用Open_Reader时，PyODPS会默认调用旧的Result接口。此时从服务端得到的数据是CSV格式的，所以DATETIME都是STRING类型。 打开Instance Tunnel，即设置 `options.tunnel.use_instance_tunnel = True` ，PyODPS会默认调用Instance Tunnel，即可解决此问题。

**如何利用Python语言特性来实现丰富的功能？**

编写Python函数。 计算两点之间的距离有多种计算方法，例如欧氏距离、曼哈顿距离等，您可以定义一系列函数，在计算时根据具体情况调用相应的函数即可。

```python
def euclidean_distance(from_x, from_y, to_x, to_y):
    return ((from_x - to_x) ** 2 + (from_y - to_y) ** 2).sqrt()
def manhattan_distance(center_x, center_y, x, y):
   return (from_x - to_x).abs() + (from_y - to_y).abs()
```

调用如下。

```
In [42]: df
     from_x    from_y      to_x      to_y
0 0.393094 0.427736 0.463035 0.105007 1 0.629571 0.364047 0.972390 0.081533 2 0.460626 0.530383 0.443177 0.706774 3 0.647776 0.192169 0.244621 0.447979 4 0.846044 0.153819 0.873813 0.257627 5 0.702269 0.363977 0.440960 0.639756 6 0.596976 0.978124 0.669283 0.936233 7 0.376831 0.461660 0.707208 0.216863 8 0.632239 0.519418 0.881574 0.972641 9 0.071466 0.294414 0.012949 0.368514 In [43]: euclidean_distance(df.from_x, df.from_y, df.to_x, df.to_y).rename('distance')
   distance
0 0.330221 1 0.444229 2 0.177253 3 0.477465 4 0.107458 5 0.379916 6 0.083565 7 0.411187 8 0.517280 9 0.094420 In [44]: manhattan_distance(df.from_x, df.from_y, df.to_x, df.to_y).rename('distance')
   distance
0 0.392670 1 0.625334 2 0.193841 3 0.658966 4 0.131577 5 0.537088 6 0.114198 7 0.575175 8 0.702558 9 0.132617
```

利用Python语言的条件和循环语句。 如果用户要计算的表保存在数据库，需要根据配置来对表的字段进行处理，然后对所有表进行UNION或者JOIN操作。这时如果用SQL实现是相当复杂的，但是用例如，您有30张表需要合成一张表，此时如果使用SQL，则需要对30张表执行UNION ALL操作。如果使用PyODPS，如下代码就可以完成。

```
table_names = ['table1', ..., 'tableN'] dfs = [o.get_table(tn).to_df() for tn in table_names] reduce(lambda x, y: x.union(y), dfs)
```

## reduce语句等价于如下代码。

```
df = dfs[0] for other_df in dfs[1:]:
    df = df.union(other_df)
```

**如何使用Pandas计算后端进行本地Debug？**

您可以通过如下两种方式来进行本地Debug。这两种方式除了初始化方法不同，后续代码完全一致： 通过Pandas DataFrame创建的PyODPS DataFrame可以使用Pandas执行本地计算。 使用MaxCompute表创建的DataFrame可以在MaxCompute上执行。 示例代码如下。

```
df = o.get_table('movielens_ratings').to_df() DEBUG = True if DEBUG:
    df = df[:100].to_pandas(wrap=True)
```

当所有后续代码都编写完成，本地的测试速度非常快。当测试结束后，您可以把Debug值改为False，这样后续就能在MaxCompute上执行全量的计算。

**如何避免嵌套循环执行慢的情况？**

建议您通过Dict数据结构记录下循环的执行结果，最后在循环外统一导入到Dataframe对象中。如果您将Dataframe对象代码 `df=XXX` 放置在外层循环中，会导致数据量很小的情况下进行本地数据处理。 如果需要对单行数据应用一个Python函数，或者执行一行变多行的操作，这时使用PyODPS DataFrame就可以轻松完成，并且可以完全发挥MaxCompute的并行计算能力。 例如有一份JSON串数据，需要把JSON串按Key-Value对展开成一行，代码如下所示。

```
In [12]: df
               json
0 {"a": 1, "b": 2} 1 {"c": 4, "b": 3} In [14]: from odps.df import output In [16]: @output(['k', 'v'], ['string', 'int'])
    ...: def h(row):
    ...:     import json
    ...:     for k, v in json.loads(row.json).items():
    ...:         yield k, v
    ...:
In [21]: df.apply(h, axis=1)
   k  v
0 a 1 1 b 2 2 c 4 3 b 3
```

**通过open_reader最多只能取到1万条记录，如何获取多于1万条的记录？**

使用 `create table as select ...` 将SQL的结果保存成表，再使用 `table.open_reader` 读取。

**为什么尽量使用内建算子，而不是自定义函数？**

对于百万行的数据，当一行应用了自定义函数后，执行时间从7秒延长到了27秒。如果有更大的数据集、更复杂的操作，时间的差距可能会更大。

**为什么通过DataFrame().schema.partitions获得分区表的分区值为空？**

这是因为DataFrame不区分分区字段和普通字段，所以获取分区表的分区字段作为普通字段处理。您可以通过如下方式过滤掉分区字段。

```
df = o.get_table().to_df() df[df.ds == '']
```

建议您参照表来设置分区或读取分区信息。 PyODPS默认不限制从Instance读取的数据规模。但是对于受保护的MaxCompute项目，通过Tunnel下载数据将受限。此时，如果未设置 `options.tunnel.limit_instance_tunnel` ，则数据量限制会被自动打开，可下载的数据条数受到MaxCompute配置限制，通常该限制为10000条。如果您需要迭代获取全部数据，则需要关闭 `limit` 限制。您可以通过下列语句在全局范围内打开 `Instance Tunnel` 并关闭 `limit` 限制。 `options.tunnel.limit_instance_tunnel = False #` 关闭`limit`限制，读取全部数据。

```
with instance.open_reader() as reader:
```

**使用PyODPS统计表中某个字段的空值率时，是用execute_sql还是DataFrame？**

| execute_sql | 方式打开新数据类 |
|---|---|

如果通过Dataframe打开新数据类型，例如persist、execute、to_pandas等方法，可通过hints参数设置。图示设置方法仅针对单个作业生效。

```
users.persist('copy_test',hints={'odps.sql.type.system.odps2':'true'})
```

如果通过Dataframe调用，且需要全局生效，需要使用Option参数 `options.sql.use_odps2_extension = True` 。 您可以通过以下两种方式进行解决： 升级SDK版本至V0.8.4或以上版本。 SQL中添加如下语句：

```
fromodps.typesimportDecimal Decimal._max_precision=38
```

### PyODPS API概述

#### 使用说明

ODPS详解（Definitions）

## Java沙箱限制

本文为您介绍MaxCompute MapReduce及UDF程序在分布式环境中运行时受到的Java沙箱限制。

**使用限制**

**说明**

不允许直接访问本地文件，只能通过MaxCompute MapReduce提供的接口间接访问。 不允许直接访问分布式文件系统，只能通过MaxCompute MapReduce访问到表的记录。 不允许JNI调用限制。 不允许创建Java线程，不允许运行子进程执行Linux命令。 不允许访问网络，包括获取本地IP地址等都会被禁止。 Java反射限制，**suppressAccessChecks**权限被禁止，无法SetAccessible某Private的属性或方法，以达到读取Private属性或调用Private方法的目的。 即在代码中直接使用上面的这些方法会报**access denied**异常。

## MaxCompute功能增强包

### 联合计算增强包

#### 11.1.1. 联合计算增强包概述

联合计算增强包包括基于MaxCompute的外部表功能访问OSS、OTS、RDS等表或数据的能力，以及基于联合计算平台提供Spark on MaxCompute等计算能力，允许使用开源技术方案处理MaxCompute数仓中的数据。本文为您介绍联合计算增强包相关内容。 与早期Spark相比在性能、稳定性、版本、管理能力，以及OSS、Hadoop融合兼容性方面都有大幅度提升，此外还提供了更简单易用的外部表模式，可以直接访问数据湖中的数据。 MaxCompute Spark是MaxCompute提供的兼容开源Spark的计算服务。在统一的计算资源和数据集权限体系之上提供Spark计算框架，支持您以熟悉的开发使用方式提交运行Spark作业，满足更丰富的数据处理分析需求。基于Spark能力，可以将数据湖OSS中的数据处理到数仓中，打通湖仓数据通道。随着对Spark on MaxCompute的性能逐步优化，基于MaxCompute的大规模存储计算能力，增强能力已经具备优于开源Spark的性能和管理能力，并已支持2.3.0和2.4.5版本。 随着大数据业务的不断扩展，新的数据使用场景在不断产生，MaxCompute原来主要面对内部特殊格式数据的强大计算能力，正逐步开放给不同的外部数据。 MaxCompute提供了外部表来解决上述问题。外部表的功能旨在提供除MaxCompute内部表以外其他数据的处理能力。通过一条简单的DDL语句，即可在 MaxCompute上创建一张外部表，建立MaxCompute表与外部数据源的关联，提供各种数据的接入和输出能力。创建好的外部表可以像普通的MaxCompute表一样使用（大部分场景），充分利用MaxCompute SQL的强大计算功能。同时外部表提供内置访问外部数据源的Extractor，也支持用户自定义Extractor访问外部非结构化数据，还可以用Hive serde handler处理各种开源数据格式，具备充分的灵活性和开放性。MaxCompute外部表包括OSS、OTS、HBase、RDS、 Hologres等JDBC方式的外部数据源。

#### 11.1.2. Spark On MaxCompute使用VolumeFs

本文提供了Spark on MaxCompute使用VolumeFs的完整指南，包括前置条件确认、HDFS客户端环境配置、核心参数设置、Volume创建与文件操作命令，以及结合Spark MLlib进行模型存储与加载的代码案例，方便您快速搭建基于VolumeFs的大数据存储与分析流程，实现高效的数据持久化与管理。

**前提条件**

Spark On MaxCompute使用MaxCompute需要Project支持VolumeFs，所以在使用之前请联系运维管理员确认Project是否支持VolumeFs。

**配置VolumeFs-HDFS客户端**

1. 下载：客户端。
2. 下载VolumeFs相关库：lib.tar.gz。

| 下载并解压客户端后，使用如下命令设置 | HADOOP_HOME | 环境变量。 |
|---|---|---|
| # 添加以下代码到.bashrc \ .bash_profile export HADOOP_HOME=/path/to/hadoop-2.7.1/ |  |  |

| 编辑 | $HADOOP_HOME/etc/hadoop/hadoop-env.sh | 。 |
|---|---|---|
| # 执行相关命令 mkdir -p $HADOOP_HOME/share/hadoop/odps # 解压VolumeFs相关库到上面路径 tar xf /path/to/lib.tar.gz -C $HADOOP_HOME/share/hadoop/odps # 添加以下代码到 $HADOOP_HOME/etc/hadoop/hadoop-env.sh # Odps Support export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$HADOOP_HOME/share/hadoop/odps/lib/* |  |  |

| 配置 | $HADOOP_HOME/etc/hadoop/core-site.xml | 。 |
|---|---|---|
| 重要所有TBD的部分都需要填写。 |  |  |

```xml
<?xml version="1.0" encoding="UTF-8"?> <?xml-stylesheet type="text/xsl" href="configuration.xsl"?> <!--
      Licensed under the Apache License, Version 2.0 (the "License");
      you may not use this file except in compliance with the License.
      You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
      See the License for the specific language governing permissions and
      limitations under the License. See accompanying LICENSE file.
--> <!-- Put site-specific property overrides in this file. --> <configuration>
    <property>
        <name>fs.odps.impl</name>
        <value>com.aliyun.odps.fs.VolumeFileSystem</value>
    </property>
    <property>
        <name>fs.AbstractFileSystem.odps.impl</name>
        <value>com.aliyun.odps.fs.VolumeFs</value>
    </property>
    <property>
        <name>io.file.buffer.size</name>
        <value>512000</value>
    </property>
    <property>
        <name>volume.internal</name>
        <value>false</value>
    </property>
    <property>
        <name>pangu.access.check</name>
        <value>false</value>
    </property>
    <property>
        <name>odps.access.id</name>
        <value>TBD</value>
    </property>
    <property>
        <name>odps.access.key</name>
        <value>TBD</value>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>odps://<projectName>/</value>
    </property>
    <property>
        <name>odps.service.endpoint</name>
        <value>TBD</value>
    </property>
</configuration>
```

**VolumeFs-HDFS客户端演示**

客户端配置完毕，可以直接使用 `bin/hdfs dfs` 命令创建一个Volume，Volume必须在对应的Project下面， `volume1` 为Volume名称， `volume1` 目录为： `bin/hdfs dfs -mkdir odps://cupid_5kn/volume1` ，相关命令如下： `//` 创建`volume`下的一个文件夹

```
bin/hdfs dfs -mkdir odps://cupid_5kn/volume1/test_dir
```

`//` 上传文件

```
bin/hdfs dfs -put ~/abcd odps://cupid_5kn/volume1/test_dir/
```

`//` 查看文件

```
bin/hdfs dfs -cat odps://cupid_5kn/volume1/test_dir/abcd
```

## Spark Mllib使用`VolumeFs`案例以`KMeans`案例作为参考```java

```
## https://github.com/aliyun/aliyun-cupid-sdk/blob/master/examples/spark-
examples/src/main/scala/com/aliyun/odps/spark/examples/mllib/KmeansModelSaveToVolume.scala /**
  * Licensed to the Apache Software Foundation (ASF) under one
  * or more contributor license agreements.  See the NOTICE file
  * distributed with this work for additional information
  * regarding copyright ownership.  The ASF licenses this file
  * to you under the Apache License, Version 2.0 (the
  * "License"); you may not use this file except in compliance
  * with the License.  You may obtain a copy of the License at
  * <p>
  * http://www.apache.org/licenses/LICENSE-2.0
  * <p>
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
```

`*/`

```java
package com.aliyun.odps.spark.examples.mllib import org.apache.spark.mllib.clustering.KMeans._ import org.apache.spark.mllib.clustering.{KMeans, KMeansModel} import org.apache.spark.mllib.linalg.Vectors /**
  * KmeansModelSaveToVolume Volume
  * 1. build aliyun-cupid-sdk please set modelVolumeDir with real volume path
  * 2. properly set spark.defaults.conf must have [spark.hadoop.odps.cupid.volume.paths=odps://projectName/volumeName/]
  * 3. bin/spark-submit --master yarn-cluster --class com.aliyun.odps.spark.examples.mllib.KmeansModelSaveToVolume
  * /path/to/aliyun-cupid-sdk/examples/spark-examples/target/spark-examples_2.11-1.0.0-SNAPSHOT-shaded.jar
```

`*/`

```python
object KmeansModelSaveToVolume {
  val projectName = "projectName"
  val volumeName = "volumeName"
  val modelVolumeDir = s"odps://$projectName/$volumeName/mllib_dir/"
  def main(args: Array[String]) {
    //1. train and save the model
    val spark = SparkSession
      .builder()
      .appName("KmeansModelSaveToVolume")
      .getOrCreate()
    val sc = spark.sparkContext
    val points = Seq(
      Vectors.dense(0.0, 0.0),
      Vectors.dense(0.0, 0.1),
      Vectors.dense(0.1, 0.0),
      Vectors.dense(9.0, 0.0),
      Vectors.dense(9.0, 0.2),
      Vectors.dense(9.2, 0.0)
```

)

```
    val rdd = sc.parallelize(points, 3)
    val initMode = K_MEANS_PARALLEL
    val model = KMeans.train(rdd, k = 2, maxIterations = 2, runs = 1, initMode)
    val predictResult1 = rdd.map(feature => "cluster id: " + model.predict(feature) + " feature:" +
feature.toArray.mkString(",")).collect
    println("modelVolumeDir=" + modelVolumeDir)
    model.save(sc, modelVolumeDir)
    //2. predict from the oss model
    val modelLoadOss = KMeansModel.load(sc, modelVolumeDir)
    val predictResult2 = rdd.map(feature => "cluster id: " + modelLoadOss.predict(feature) + " feature:" +
feature.toArray.mkString(",")).collect
    assert(predictResult1.size == predictResult2.size)
    predictResult2.foreach(result2 => assert(predictResult1.contains(result2)))
  }
}
```

#### 11.1.3. Spark on Maxcompute

**11.1.3.1. 概述**

Spark on MaxCompute提供原生Spark体验及组件，支持MaxCompute数据源存取、多租户安全和资源共享。本文介绍Spark on MaxCompute的核心功能。

**核心功能**

Spark on MaxCompute是阿里云开发的基于MaxCompute平台无缝运行使用Spark的方案，其很大程度上丰富了MaxCompute产品的功能体系。 Spark on MaxCompute为您提供原生Spark的使用体验以及Spark原生的组件及API； 提供存取MaxCompute数据源的能力； 提供多租户场景更好的安全能力； 提供管控平台，让Spark作业与MaxCompute作业共享资源、存储及用户体系，保证高性能和低成本。 Spark配合MaxCompute产品能够构建更加完善高效的数据处理解决方案，同时社区Spark的应用可以无缝运行在Spark on MaxCompute之上。 Spark on MaxCompute在DataWorks上有独立的数据开发节点，支持在DataWorks上进行相应的数据开发操作。

##### 11.1.3.2. 项目资源

本文介绍使用Spark on MaxCompute所需的项目资源，包括发布包与插件，用于完成环境配置并运行示例程序。

#### 使用说明

1. 使用Spark on MaxCompute时，您可能需要关注或下载如下的项目资源。
Spark on MaxCompute发布包：请下载最新的Spark on MaxCompute发布包。 Spark on MaxCompute插件：本项目已开源，插件链接地址为Aliyun Cupid SDK。
2. 准备好上述的项目资源后，还需要完成环境设置才可以运行GitHub项目中的相关Demo。

##### 11.1.3.3. 环境设置

###### 11.1.3.3.1. 解压Spark on MaxCompute发布包

本文介绍Spark on MaxCompute发布包解压后的文件与目录结构，便于后续使用。

**结构说明**

对下载好的Spark on MaxCompute发布包进行解压，解压后的文件夹结构如下。 .

```
|-- R
|-- RELEASE
|-- __spark_libs__.zip
|-- bin
|-- conf
|-- cupid
|-- derby.log
|-- examples
|-- jars
|-- logs
|-- metastore_db
|-- sbin
|-- yarn
```

###### 11.1.3.3.2. 设置环境变量

##### 环境设置

根据您的实际情况，设置所需的环境变量。主要是**JAVA_HOME**和**SPARK_HOME**的设置。

**JAVA_HOME设置**

```
export JAVA_HOME=/path/to/jdk export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar export PATH=$JAVA_HOME/bin:$PATH
```

**SPARK_HOME设置**

```
export SPARK_HOME=/path/to/spark_extracted_package export PATH=$SPARK_HOME/bin:$PATH export PATH=/home/admin/R/bin/:$PATH
```

对于PySpark用户，选择安装Python 2.7，并设置Path。

```
export PATH=/path/to/python/bin/:$PATH
```

###### 11.1.3.3.3. 设置spark-defaults.conf

本文介绍如何配置Spark on MaxCompute所需的 `spark-defaults.conf` 文件。

#### 使用说明

在$SPARK_HOME/conf路径下存在 `spark-defaults.conf` 文件，需要在该文件中设置MaxCompute的账号信息后，才可以提交Spark任务到MaxCompute。

**配置说明**

默认配置内容如下，将空白部分根据实际的账号信息填写即可。

```bash
# OdpsAccount Info Setting
spark.hadoop.odps.project.name= spark.hadoop.odps.access.id= spark.hadoop.odps.access.key= spark.hadoop.odps.end.point=
#spark.hadoop.odps.moye.trackurl.host=
#spark.hadoop.odps.cupid.webproxy.endpoint=
spark.driver.extraJavaOptions -Dscala.repl.reader=com.aliyun.odps.spark_repl.OdpsInteractiveReader -Dscala.usejavacp=true
# odps.cupid.spark.r.archive=/path/to/R-PreCompile-Package.zip
# Cupid Longtime Job
# spark.hadoop.odps.cupid.engine.running.type=longtime
# spark.hadoop.odps.cupid.job.capability.duration.hours=8640
# spark.hadoop.odps.moye.trackurl.dutation=8640
# spark.hadoop.odps.cupid.disk.driver.enable=false
spark.hadoop.odps.cupid.bearer.token.enable=false spark.hadoop.odps.exec.dynamic.partition.mode=nonstrict
```

##### 11.1.3.4. Spark on MaxCompute快速入门

本文为您介绍Spark on MaxCompute的使用流程，旨在引导您一站式完成Spark on MaxCompute的基础使用。

**操作步骤**

1. 获取并解压Spark on MaxCompute发布包。
2. 设置环境变量。

```
export SPARK_HOME=/path/to/spark-2.1.0-private-cloud-v3.1.0 export JAVA_HOME=/path/to/java/
```

3. 设置**spark-defaults.conf**。

```
cp $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf
```

编辑**$SPARK_HOME/conf/spark-defaults.conf**，将空白部分填写即可。

```bash
# OdpsAccount Info Setting
spark.hadoop.odps.project.name= spark.hadoop.odps.access.id= spark.hadoop.odps.access.key= spark.hadoop.odps.end.point=
#spark.hadoop.odps.moye.trackurl.host=
#spark.hadoop.odps.cupid.webproxy.endpoint=
spark.driver.extraJavaOptions -Dscala.repl.reader=com.aliyun.odps.spark_repl.OdpsInteractiveReader -Dscala.usejavacp=true
# odps.cupid.spark.r.archive=/path/to/R-PreCompile-Package.zip
# Cupid Longtime Job
# spark.hadoop.odps.cupid.engine.running.type=longtime
# spark.hadoop.odps.cupid.job.capability.duration.hours=8640
# spark.hadoop.odps.moye.trackurl.dutation=8640
# spark.hadoop.odps.cupid.disk.driver.enable=false
spark.hadoop.odps.cupid.bearer.token.enable=false spark.hadoop.odps.exec.dynamic.partition.mode=nonstrict
```

4. 准备**spark-example**。

```
git clone https://github.com/aliyun/aliyun-cupid-sdk.git cd aliyun-cupid-sdk mvn -T 1C clean install -DskipTests
```

5. 运行SparkPi。

```
cd $SPARK_HOME bin/spark-submit --master yarn-cluster --class com.aliyun.odps.spark.examples.SparkPi /path/to/aliyun-cupid-sdk/examples/spark-examples /target/spark-examples_2.11-1.0.0-SNAPSHOT-shaded.jar
```

成功标准：看到以下输出即代表运行成功，可能会有其他日志一并输出。

```
18/02/09 15:52:28 INFO Client: Application report for application_1518162700322_1635034099 (state: FINISHED) 18/02/09 15:52:28 INFO Client:
     client token: N/A
     diagnostics: N/A
     ApplicationMaster host: ***
     ApplicationMaster RPC port: ***
     queue: queue
     start time: 1518162732343
     final status: SUCCEEDED
     tracking URL: http://***:80/proxyview/jobview/?
h=http://***:80/api&p=odps_smoke_test&i=20180209075148695gbkp8e01&t=spark&id=application_1518162700322_1635034099&metaname=2018020907514869 p8e01&token=YkhjNXJWZ0dvdzVScXVFQWpCQWMra1RSZHVFPSxPRFBTX09CTzoxMzY1OTM3MTUwNzcyMjEzLDE1MTg0MjE5MzUseyJTdGF0ZW1lbnQiOlt7IkFjdGlvbiI6WyJvZHB lYWQiXSwiRWZmZWN0IjoiQWxsb3ciLCJSZXNvdXJjZSI6WyJhY3M6b2RwczoqOnByb2plY3RzL29kcHNfc21va2VfdGVzdC9pbnN0YW5jZXMvMjAxODAyMDkwNzUxNDg2OTVnYmtwOG JdfV0sIlZlcnNpb24iOiIxIn0=
     user: user
18/02/09 15:52:28 INFO ShutdownHookManager: Shutdown hook called 18/02/09 15:52:28 INFO ShutdownHookManager: Deleting directory /tmp/spark-d77416ad-79a8-49f7-931d-0533663b5d85
```

##### 11.1.3.5. 示例Demo

本文为您提供Spark on MaxCompute的示例demo，旨在让您更好地了解Spark on MaxCompute的使用。

**操作步骤**

1. 修改配置文件。
将Spark压缩包解压，进入配置文件目录conf，修改配置文件**spark-defaults.conf**，修改如下配置。

```
spark.hadoop.odps.project.name=xxxx spark.hadoop.odps.access.id=xxxx spark.hadoop.odps.access.key=xxxx spark.hadoop.odps.end.point=http://service.xxxx.xxxx.xxxxx.qd-inc.com:80/api spark.hadoop.odps.cupid.distributedcache.mincopy=3 spark.hadoop.odps.cupid.distributedcache.maxcopy=3 spark.hadoop.odps.cupid.proxy.domain.name=jobview.xxxx.xxxx.xxxx.com spark.hadoop.odps.cupid.history.server.address=10.xx.xx.xx:18080
```

**说明**

前四个配置项，可以通过/cloud/app/odps-service-console/CupidFrontendServer#/cupid_web_proxy/current/conf.local/路径下的**web_component.conf**文件获取。 spark.hadoop.odps.cupid.proxy.domain.name：odps_jobview_server_dns的域名，需要去掉前面的sparkui。 spark.hadoop.odps.cupid.history.server.address：AG机器的IP地址，需要加上端口号18080。
2. 启动程序。
进入Spark解压目录，执行如下命令。

```
bin/spark-submit --class com.aliyun.odps.spark.examples.WordCount --master yarn-cluster examples/spark-examples-2.0.0-SNAPSHOT-shaded.jar
```

3. 查看链接。
logview页面。 Sparkui界面。 Spark History界面。

##### 11.1.3.6. 常用场景案例演示

###### 11.1.3.6.1. WordCount案例

本文为您提供使用Spark on MaxCompute运行WordCount的参考示例。

#### 使用说明

如果您希望运行相关的案例演示Demo，需要下载GitHub项目并对项目进行编译后，才能够运行相关Demo。

```
git clone https://github.com/aliyun/aliyun-cupid-sdk.git
```

`--` 下载`GitHub`项目。

```
cd aliyun-cupid-sdk mvn -T 1C clean install -DskipTests
```

`--` 编译`GitHub`项目。 执行完上述步骤后，会产生相应的JAR包，这些JAR包可以在本章节及以下各章节的案例演示Demo中使用。

**示例代码**

```java
package com.aliyun.odps.spark.examples object WordCount {
  def main(args: Array[String]) {
    val spark = SparkSession
      .builder()
      .appName("WordCount")
      .getOrCreate()
    val sc = spark.sparkContext
    try {
      sc.parallelize(1 to 100, 10).map(word => (word, 1)).reduceByKey(_ + _, 10).take(100).foreach(println)
    } finally {
      sc.stop()
    }
  }
}
```

**提交命令**

提交作业的运行命令如下。

```
bin/spark-submit \ --master yarn-cluster \ --class com.aliyun.odps.spark.examples.WordCount \ /path/to/aliyun-cupid-sdk/examples/spark-examples/target/spark-examples_2.11-1.0.0-SNAPSHOT-shaded.jar
```

###### 11.1.3.6.2. 访问OSS案例

**示例代码**

```java
package com.aliyun.odps.spark.examples.oss object SparkUnstructuredDataCompute {
  def main(args: Array[String]) {
    val spark = SparkSession
      .builder()
      .appName("SparkUnstructuredDataCompute")
      .config("spark.hadoop.fs.oss.accessKeyId", "***")
      .config("spark.hadoop.fs.oss.accessKeySecret", "***")
      .config("spark.hadoop.fs.oss.endpoint", "oss-cn-hangzhou-zmf.aliyuncs.com")
      .getOrCreate()
    val sc = spark.sparkContext
    try {
      val pathIn = "oss://bucket/inputdata/"
      val inputData = sc.textFile(pathIn, 5)
      val cnt = inputData.count
      println(s"count: $cnt")
    } finally {
      sc.stop()
    }
  }
}
```

**提交命令**

提交作业的运行命令如下。

```
./bin/spark-submit --jars cupid/hadoop-aliyun-package-3.0.0-alpha2-odps-jar-with-dependencies.jar --class com.aliyun.odps.spark.examples.oss.SparkUnstructuredDataCompute /path/to/aliyun-cupid-sdk/examples/spark-examples/target/spark-examples_2.11-1.0.0-SNAPSHOT-shaded.jar
```

###### 11.1.3.6.3. MaxCompute Table ReadWrite案例

本文为您提供使用Spark on MaxCompute读写MaxCompute Table，并转化为Spark RDD的参考示例。

**示例代码**

**重要**

案例Demo中的Project和Table必须存在，或更改为对应的Project和Table。

```java
package com.aliyun.odps.spark.examples import com.aliyun.odps.data.Record import com.aliyun.odps.{PartitionSpec, TableSchema} import org.apache.spark.odps.OdpsOps import scala.util.Random object OdpsTableReadWrite {
  def main(args: Array[String]) {
    val spark = SparkSession
      .builder()
      .appName("OdpsTableReadWrite")
      .getOrCreate()
    val sc = spark.sparkContext
    val projectName = sc.getConf.get("odps.project.name")
    try {
      val odpsOps = new OdpsOps(sc)
      // read from normal table via rdd api
      val rdd_0 = odpsOps.readTable(
        projectName,
        "cupid_wordcount",
        (r: Record, schema: TableSchema) => (r.getString(0), r.getString(1))
```

)

```
      //read from single partition column table via rdd api
valrdd1=odpsOps.readTable(
```

```
      val rdd_1  odpsOps.readTable(
        projectName,
        "dftest_single_parted",
        Array("pt=20160101"),
        (r: Record, schema: TableSchema) => (r.getString(0), r.getString(1), r.getString("pt"))
```

)

```
      // read from multi partition column table via rdd api
      val rdd_2 = odpsOps.readTable(
        projectName,
        "dftest_parted",
        Array("pt=20160101,hour=12"),
        (r: Record, schema: TableSchema) => (r.getString(0), r.getString(1), r.getString("pt"), r.getString(3))
```

)

```
      // read with multi partitionSpec definition via rdd api
      val rdd_3 = odpsOps.readTable(
        projectName,
        "cupid_partition_table1",
        Array("pt1=part1,pt2=part1", "pt1=part1,pt2=part2", "pt1=part2,pt2=part3"),
        (r: Record, schema: TableSchema) => (r.getString(0), r.getString(1), r.getString("pt1"), r.getString("pt2"))
```

)

```
      // save rdd into normal table
      val transfer_0 = (v: Tuple2[String, String], record: Record, schema: TableSchema) => {
        record.set("id", v._1)
        record.set(1, v._2)
      }
      odpsOps.saveToTable(projectName, "cupid_wordcount_empty", rdd_0, transfer_0, true)
      // save rdd into partition table with single partition spec
      val transfer_1 = (v: Tuple2[String, String], record: Record, schema: TableSchema) => {
        record.set("id", v._1)
        record.set("value", v._2)
      }
      odpsOps.saveToTable(projectName, "cupid_partition_table1", "pt1=test,pt2=dev", rdd_0, transfer_1, true)
      // dynamic save rdd into partition table with multiple partition spec
      val transfer_2 = (v: Tuple2[String, String], record: Record, part: PartitionSpec, schema: TableSchema) => {
        record.set("id", v._1)
        record.set("value", v._2)
        val pt1_value = if (new Random().nextInt(10) % 2 == 0) "even" else "odd"
        val pt2_value = if (new Random().nextInt(10) % 2 == 0) "even" else "odd"
        part.set("pt1", pt1_value)
        part.set("pt2", pt2_value)
      }
      odpsOps.saveToTableForMultiPartition(projectName, "cupid_partition_table1", rdd_0, transfer_2, true)
    } catch {
      case ex: Exception => {
        throw ex
      }
    } finally {
      sc.stop
    }
  }
}
```

**提交命令**

提交作业的运行命令如下。

```
bin/spark-submit \ --master yarn-cluster \ --class com.aliyun.odps.spark.examples.OdpsTableReadWrite \ /path/to/aliyun-cupid-sdk/examples/spark-examples/target/spark-examples_2.11-1.0.0-SNAPSHOT-shaded.jar
```

**调整并发**

MaxCompute Table读取并发度可以通过如下两个方法进行调整。 调整**spark.hadoop.odps.input.split.size**，该值越大，Map Task越少，默认为256 MB。 通过**OdpsOps.readTable**中的**numPartition**进行设置，该值可直接决定Map Task个数，模式按照**spark.hadoop.odps.input.split.size**进行计算。

###### 11.1.3.6.4. MaxCompute Table Spark-SQL案例

本文为您提供使用Spark on MaxCompute中的SQLContext读写MaxCompute Table的参考示例。

**示例代码**

**重要**

案例Demo中的Project和Table必须存在，或更改为对应的Project和Table。
**Spark-defaults.conf**里必须设置spark.sql.catalogImplementation = odps。

```java
package com.aliyun.odps.spark.examples object OdpsTableReadWriteViaSQL {
  def main(args: Array[String]) {
    // please make sure spark.sql.catalogImplementation=odps in spark-defaults.conf
    // to enable odps catalog
    val spark = SparkSession
      .builder()
      .appName("OdpsTableReadWriteViaSQL")
      .getOrCreate()
    val projectName = spark.sparkContext.getConf.get("odps.project.name")
    val tableName = "cupid_wordcount"
    val df = spark.table(tableName)
    println(s"df.count: ${df.count()}")
    // Just do some query
    spark.sql(s"select * from $tableName limit 10").show(10, 200)
    spark.sql(s"select id, count(id) from $tableName group by id").show(10, 200)
    // any table exists under project could be use
    // productRevenue
      """
        |SELECT product,
        |       category,
        |       revenue
        |FROM
        |  (SELECT product,
        |          category,
        |          revenue,
        |          dense_rank() OVER (PARTITION BY category
        |                             ORDER BY revenue DESC) AS rank
        |   FROM productRevenue) tmp
        |WHERE rank <= 2
      """.stripMargin).show(10, 200)
    spark.stop()
  }
}
```

**提交命令**

提交作业的运行命令如下。

```
bin/spark-submit \ --master yarn-cluster \ --class com.aliyun.odps.spark.examples.OdpsTableReadWrite \ /path/to/aliyun-cupid-sdk/examples/spark-examples/target/spark-examples_2.11-1.0.0-SNAPSHOT-shaded.jar
```

###### 11.1.3.6.5. MaxCompute Table PySpark案例

本文提供Spark on MaxCompute中使用PySpark读写MaxCompute Table的代码示例。

**示例代码**

```python
from odps.odps_sdk import OdpsOps from pyspark import SparkContext, SparkConf if __name__ == '__main__':
    conf = SparkConf().setAppName("odps_pyspark")
    sc = SparkContext(conf=conf)
    sql_context = SQLContext(sc)
    project_name = "cupid_testa1"
    in_table_name = "cupid_wordcount"
    out_table_name = "cupid_wordcount_py"
    normal_df = OdpsOps.read_odps_table(sql_context, project_name, in_table_name)
    for i in normal_df.sample(False, 0.01).collect():
        print i
    print "Read normal odps table finished"
    OdpsOps.write_odps_table(sql_context, normal_df.sample(False, 0.001), project_name, out_table_name)
    print "Write normal odps table finished"
```

**提交命令**

提交作业的运行命令如下。

```
spark-submit \ --master yarn-cluster \ --jars /path/to/aliyun-cupid-sdk/external/cupid-datasource/target/cupid-datasource_2.11-1.0.0-SNAPSHOT.jar \ --py-files /path/to/aliyun-cupid-sdk/examples/spark-examples/src/main/python/odps.zip \ /path/to/aliyun-cupid-sdk/examples/spark-examples/src/main/python/odps_table_rw.py
```

###### 11.1.3.6.6. Mllib案例

**示例代码**

**说明**

Mllib的Model建议使用OSS进行读写。

```java
package com.aliyun.odps.spark.examples.mllib import org.apache.spark.mllib.clustering.KMeans._ import org.apache.spark.mllib.clustering.{KMeans, KMeansModel} import org.apache.spark.mllib.linalg.Vectors object KmeansModelSaveToOss {
  val modelOssDir = "oss://bucket/kmeans-model"
  def main(args: Array[String]) {
    //1. train and save the model
    val spark = SparkSession
      .builder()
      .appName("KmeansModelSaveToOss")
      .config("spark.hadoop.fs.oss.accessKeyId", "***")
      .config("spark.hadoop.fs.oss.accessKeySecret", "***")
      .config("spark.hadoop.fs.oss.endpoint", "***")
      .getOrCreate()
    val sc = spark.sparkContext
    val points = Seq(
      Vectors.dense(0.0, 0.0),
      Vectors.dense(0.0, 0.1),
      Vectors.dense(0.1, 0.0),
      Vectors.dense(9.0, 0.0),
      Vectors.dense(9.0, 0.2),
      Vectors.dense(9.2, 0.0)
```

)

```
    val rdd = sc.parallelize(points, 3)
    val initMode = K_MEANS_PARALLEL
    val model = KMeans.train(rdd, k = 2, maxIterations = 2, runs = 1, initMode)
    val predictResult1 = rdd.map(feature => "cluster id: " + model.predict(feature) + " feature:" +
feature.toArray.mkString(",")).collect
    println("modelOssDir=" + modelOssDir)
    model.save(sc, modelOssDir)
    //2. predict from the oss model
    val modelLoadOss = KMeansModel.load(sc, modelOssDir)
    val predictResult2 = rdd.map(feature => "cluster id: " + modelLoadOss.predict(feature) + " feature:" +
feature.toArray.mkString(",")).collect
    assert(predictResult1.size == predictResult2.size)
    predictResult2.foreach(result2 => assert(predictResult1.contains(result2)))
  }
}
```

**提交命令**

提交作业的运行命令如下。

```
./bin/spark-submit --jars cupid/hadoop-aliyun-package-3.0.0-alpha2-odps-jar-with-dependencies.jar --class com.aliyun.odps.spark.examples.mllib.KmeansModelSaveToOss /path/to/aliyun-cupid-sdk/examples/spark-examples/target/spark-examples_2.11-1.0.0-SNAPSHOT-shaded.jar
```

###### 11.1.3.6.7. Spark Streaming-NetworkWordCount案例

本文提供在Spark on MaxCompute环境下运行Spark Streaming-NetworkWordCount的参考示例。

#### 使用说明

支持原生Spark Streaming，以NetworkWordCount为例，首先需要在本地安装Netcat，并执行以下命令。

```bash
$ nc -lk 9999
```

此时，控制台的输入将成为Spark Streaming的输入。

**示例代码**

```java
package com.aliyun.odps.spark.examples.streaming import org.apache.spark.SparkConf import org.apache.spark.examples.streaming.StreamingExamples import org.apache.spark.storage.StorageLevel import org.apache.spark.streaming.{Seconds, StreamingContext} object NetworkWordCount {
  def main(args: Array[String]) {
    if (args.length < 2) {
      System.err.println("Usage: NetworkWordCount <hostname> <port>")
      System.exit(1)
    }
    StreamingExamples.setStreamingLogLevels()
    // Create the context with a 1 second batch size
    val sparkConf = new SparkConf().setAppName("NetworkWordCount")
    val ssc = new StreamingContext(sparkConf, Seconds(1))
    // Create a socket stream on target ip:port and count the
    // words in input stream of \n delimited text (eg. generated by 'nc')
    // Note that no duplication in storage level only for running locally.
    // Replication necessary in distributed scenario for fault tolerance.
    val lines = ssc.socketTextStream(args(0), args(1).toInt, StorageLevel.MEMORY_AND_DISK_SER)
    val words = lines.flatMap(_.split(" "))
    val wordCounts = words.map(x => (x, 1)).reduceByKey(_ + _)
    wordCounts.print()
    ssc.start()
    ssc.awaitTermination()
  }
}
```

**提交命令**

提交作业的运行命令如下。

```
bin/spark-submit \ --master local[4] \ --class com.aliyun.odps.spark.examples.streaming.NetworkWordCount \ /path/to/aliyun-cupid-sdk/examples/spark-examples/target/spark-examples_2.11-1.0.0-SNAPSHOT-shaded.jar localhost 9999
```

##### 11.1.3.7. Maven依赖

本文介绍在Spark on MaxCompute环境中开发所需的Maven依赖配置。您可以参考本文指导，在 `pom.xml` 中正确添加相关依赖。

**Spark核心依赖配置**

| 上述GitHub项目可作为QuickStart开发模板。若需自定义开发，请参照以下配置修改您的 | pom.xml | 文件。 |
|---|---|---|
| 说明 Spark的模块的版本使用社区2.3.0的版本即可，并且保证scope是provided。 |  |  |

```xml
<dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>spark-core_2.11</artifactId>
    <version>2.3.0</version>
    <scope>provided</scope>
</dependency>
```

**MaxCompute (Cupid) 插件依赖引入**

MaxCompute插件已经发布到Maven仓库，需添加以下依赖。

```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>cupid-core_2.11</artifactId>
    <version>1.0.0</version>
    <scope>provided</scope>
</dependency> <dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>cupid-client_2.11</artifactId>
    <version>1.0.0</version>
</dependency> <dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>cupid-datasource_2.11</artifactId>
    <version>1.0.0</version>
</dependency>
```

**Maven组件功能详解**

Maven仓库的文件列表如下所示： Cupid平台Core代码：包括Cupid Task提交接口封装，以及父子进程读写表相关接口。

```xml
<dependency>
        <groupId>com.aliyun.odps</groupId>
        <artifactId>cupid-core_2.11</artifactId>
        <version>1.0.0</version>
</dependency>
```

Datasource：封装了Spark相关的MaxCompute Table读写的用户接口。

```xml
<dependency>
        <groupId>com.aliyun.odps</groupId>
        <artifactId>cupid-datasource_2.11</artifactId>
        <version>1.0.0</version>
</dependency>
```

Client：封装了Cupid Client模式的用户SDK。

```xml
<dependency>
        <groupId>com.aliyun.odps</groupId>
        <artifactId>cupid-client_2.11</artifactId>
        <version>1.0.0</version>
</dependency>
```

##### 11.1.3.8. 特殊说明

###### 11.1.3.8.1. 运行模式

本文详细介绍了Spark on MaxCompute支持的三种核心运行模式（Local模式、Cluster模式和DataWorks执行模式），旨在帮助您根据不同的开发阶段和业务场景选择最合适的执行方式

**Local模式**

Local模式主要是为方便您调试应用代码。在Local模式下，Spark on MaxCompute的使用方式与社区相同，同时添加了用Tunnel读写MaxCompute表的功能。您可以在IDE和命令行中使用该模式。 需要注意，使用该模式时，需要添加配置 `spark.master=local[N]` ，其中N表示执行该模式所需的CPU资源。 Local模式下读写表是通过读写Tunnel完成的，需要在**Spark-defaults.conf**中增加Tunnel配置项。

**说明**

请根据MaxCompute项目所在的Region及网络环境填写对应的Endpoint地址。 命令行执行该模式的方式如下。

```
1.bin/spark-submit --master local[4] \ --class com.aliyun.odps.spark.examples.SparkPi \ ${path to aliyun-cupid-sdk}/spark/spark-2.x/spark-examples/target/spark-examples_2.11-version-shaded.jar
```

**Cluster模式**

在Cluster模式中，您需要指定自定义程序入口Main。Main结束（Success or Fail）时，对应的Spark作业就会结束。使用场景适合于离线作业，可以与阿里云 DataWorks产品结合进行作业调度。 命令行提交方式如下。

```
1.bin/spark-submit --master yarn-cluster \ -class SparkPi \ ${ProjectRoot}/spark/spark-2.x/spark-examples/target/spark-examples_2.11-version-shaded.jar
```

**DataWorks执行模式**

您可以在DataWorks中运行Spark on MaxComput离线作业（Cluster模式），以方便与其它类型执行节点集成和调度。 运行步骤如下所示。
1. 您需要在DataWorks的业务流程中上传并提交（单击**提交**按钮）资源。
具体操作步骤详情请参见《**DataWorks****用户指南》**的**数据开发** > **节点开发** **> MaxCompute >** **创建和引用资源**章节。
2. 在创建的业务流程中，从**数据开发**组件中选择**ODPS Spark**节点。
具体操作步骤详情请参见《**DataWorks****用户指南》**的**数据开发** > **节点开发** **> MaxCompute > ODPS Spark****节点**章节。
3. 双击拖拽到工作流的Spark节点，对Spark作业进行任务定义。
选择Spark的版本和任务使用的开发语言，并指定任务所使用的资源文件。这里的资源文件是步骤一中在业务流程中预先上传并发布的资源文件。 您还可以指定提交作业时的配置项，例如Executor的数量及内存大小等。

| 同时还需设置Spark on MaxCompute服务的Endpoint配置项 | spark.hadoop.odps.cupid.webproxy.endpoint | 。 |
|---|---|---|
| 说明取值填写项目所在Region的Endpoint，例如http://service.cn.maxcompute.aliyun-inc.com/api。 |  |  |

4. 手动执行Spark节点，可以查看该任务的执行日志，从打印出来的日志中可以获取该任务的Logview和Jobview的URL，便于进一步查看与诊断。
5. Spark作业定义完成后，即可在业务流程中对不同类型服务进行编排和统一调度执行。

###### 11.1.3.8.2. Streaming任务

本文为您介绍运行Spark Streaming需要进行的配置。

**配置说明**

MaxCompute支持Spark Streaming，为了支持长任务运行，需要在**spark-defaults.conf**中添加如下的特殊配置。

```
spark.hadoop.odps.cupid.engine.running.type=longtime
```

# 配置成`Longtime`才不会被回收。

```
spark.hadoop.odps.cupid.job.capability.duration.hours=25920
```

# 配置时间长度。

```
spark.yarn.maxAppAttempts=10
```

# 配置`FailOver`最大重试次数。

```
spark.streaming.receiver.writeAheadLog.enable=true
```

# 是否启用`WriteAheadLog`模式，能够保证数据不丢失，但是效率会降低。

###### 11.1.3.8.3. 作业诊断

本文介绍Spark on MaxCompute的作业诊断机制。作业提交后，开发者可通过分析运行日志确认执行状态。MaxCompute内置了Logview工具与Spark Web UI， 为您提供全方位的作业监控与故障排查支持。

**提交任务**

通过Spark-Submit方式（DataWorks执行Spark任务时也会产生相应日志）提交作业，示例如下。

```
cd $SPARK_HOME bin/spark-submit --master yarn-cluster --class SparkPi /tmp/spark-2.x-demo/target/AliSpark-2.x-quickstart-1.0-SNAPSHOT-shaded.jar
```

**输出Logview**

作业提交成功后，MaxCompute会创建一个Instance，在日志中会打印Instance的Logview。

```
19/01/05 20:36:47 INFO YarnClientImplUtil: logview url: http://logview.odps.aliyun.com/logview/? h=http://service.cn.maxcompute.aliyun.com/api&p=qn_beijing&i=xxx&token=xxx
```

`--` 成功标准`: <`看到以下输出，可能会有其他日志一并输出>

```
19/01/05 20:37:34 INFO Client:
   client token: N/A
   diagnostics: N/A
   ApplicationMaster host: 11.220.xxx.xxx
   ApplicationMaster RPC port: 30002
   queue: queue
   start time: 1546691807945
   final status: SUCCEEDED
   tracking URL: http://jobview.odps.aliyun.com/proxyview/jobview/?h=http://service.cn.maxcompute.aliyun-
inc.com/api&p=project_name&i=xxx&t=spark&id=application_xxx&metaname=xxx&token=xxx
```

1. 通过日志输出的Logview，在浏览器中可以查看CUPID类型的任务执行的基本信息。
2. 单击**TaskName**下名为**master-0**的任务条，在下方的**FuxiInstance**栏中，通过**All**过滤。
3. 单击TempRoot的**StdOut**，可以查看SparkPi的输出结果。

**使用Web-UI诊断作业**

日志中打印出上述的TrackingURL，表示您的作业已经提交到MaxCompute集群。这个TrackingURL非常关键，它既是SparkWebUI，也是HistoryServer的URL。
1. 在浏览器中打开这个URL，可以追踪Spark作业的运行情况。
2. 单击Driver对应的**StdOut**即可以查看Spark作业的输出内容。

##### 11.1.3.9. Spark接口支持

###### 11.1.3.9.1. Spark Shell

**启动程序**

执行如下命令，启动应用。

```
$cd $SPARK_HOME
```

# 进入`spark`目录。
# 选择运行模式并启动应用。

**应用示例**

```
sc.parallelize(0 to 100, 2).collect sql("show tables").show sql("select * from spark_user_data").show(200,100)
```

###### 11.1.3.9.2. Spark R

**启动程序**

执行如下命令，启动应用。

```
$mkdir -p /home/admin/R && unzip ./R/R.zip -d /home/admin/R/
```

# 创建一个目录R并解压该目录下的`R.zip`。

```
$export PATH=/home/admin/R/bin/:$PATH
```

# 选择运行模式并启动应用。

**应用示例**

`df`

```
head(select(df, df$eruptions)) head(select(df, "eruptions")) head(filter(df, df$waiting < 50)) results <- sql("FROM spark_user_data SELECT *") head(results)
```

###### 11.1.3.9.3. Spark SQL

**启动程序**

执行如下命令，启动应用。

```
$cd $SPARK_HOME
```

# 进入`spark`目录。
# 选择运行模式并启动应用。

**应用示例**

```
SHOW tables; SELECT * FROM spark_user_data limit 3;; quit;
```

###### 11.1.3.9.4. Spark JDBC

**启动程序**

执行如下命令，启动应用。

```
$sbin/stop-thriftserver.sh
```

# 停止线程。

```
$sbin/start-thriftserver.sh
```

# 重启线程。

```
$bin/beeline
```

# 启动应用。

**应用示例**

```
!connect jdbc:hive2://localhost:10000/odps_smoke_test show tables; select * from mr_input limit 3; !quit
```

##### 11.1.3.10. Spark动态资源伸缩

本文介绍如何在Spark on MaxCompute中启用动态资源伸缩功能，以优化资源分配并提高作业效率。此功能需Spark 2.4.5（即企业版v3.13.0）及以上版本支持。

**背景**

Spark通过大量的配置项提供了丰富的语义。其中，大部分配置使用默认值就可以正常完成工作，而有些配置则必须手动配置才能正常运行，其中最难配置的是**spark.executor.instances**。 如果配置过小，会造成运行过慢，导致运行失败（OOM或磁盘爆掉等）；如果配置过大，会造成资源浪费。 而且，即使通过对数据和逻辑的充分理解，推算出的最优值也不可靠。因为对于复杂作业，不同Stage所需Executor数目经常有较大差别，导致作业执行过程对资源需求是变化的，固定的配置依然难以避免资源浪费；即便是简单作业，当遇到长尾时其他Executor也不得不占用资源Idle。

**解决方案**

此时，最好的解决方式是按需分配，多退少补。而社区通过动态资源伸缩（Dynamic Resource Allocation, DRA）解决了这个问题。Cupid团队则开发了 CupidService，支持了原生DRA，实现原理如下图所示。

**说明**

社区原生DRA详细信息请参见Spark帮助文档和Spark配置文档。

**开启DRA**

**说明**

仅Spark2.4.5及以上版本，odps0.34.0及以上版本支持。 开启DRA无需修改代码，只需增加以下配置。

```
spark.dynamicAllocation.shuffleTracking.enabled = true //必选，默认为false。 spark.dynamicAllocation.shuffleTracking.timeout = XXXs //必选，默认Long.MaxValue MILLISECONDS。 spark.hadoop.odps.cupid.disk.driver.enable=true //必选，依赖项。 spark.dynamicAllocation.enabled=true // 必选，Spark端开关。 spark.dynamicAllocation.maxExecutors=128 // 可选，最大Executor数。 spark.dynamicAllocation.minExecutors=1 // 可选，最小Executor数。 spark.dynamicAllocation.initialExecutors=1 // 可选，初始Executor数。
```

`spark.dynamicAllocation.executorIdleTimeout=60s //` 可选，缩容等待时间。 开启了DRA后，**spark.executor.instances**成为可选项，此时如果配置该项则等价于 `spark.dynamicAllocation.initialExecutors` 。

##### 11.1.3.11. Spark on MaxCompute常见问题

本文提供了Spark on MaxCompute在代码迁移、网络访问、权限配置及运行时故障排查等方面的常见问题与解决方案，方便您快速定位并解决作业运行中的各类阻碍，保障任务高效稳定执行。 通常分为以下三种情况： 作业无需访问MaxCompute表和OSS。此时您的JAR包可以直接运行。但是需要注意，对于Spark或Hadoop的依赖必须设成Provided。 作业需要访问MaxCompute表。此时配置相关依赖后重新打包即可。 作业需要访问OSS。此时配置相关依赖后重新打包即可。

**如何通过Spark访问VPC环境内服务**

对于VPC内的服务访问，Spark默认暂不支持访问，如有需求可以通过工单与MaxCompute团队联系获取帮助。

**Spark-defaults.conf提供的ID和Key错误**

报错信息如下。

```
Stack: com.aliyun.odps.OdpsException: ODPS-0410042: Invalid signature value - User signature dose not match
```

需要检查**spark-defaults.conf**提供的ID和Key与在Apsara Uni-manager控制台获取的AccessKey ID和Access Key Secret是否一致。

**提示权限不足**

报错信息如下。

```
Stack: com.aliyun.odps.OdpsException: ODPS-0420095: Access Denied - Authorization Failed [4019], You have NO privilege 'odps:CreateResource' on {acs:odps:*:projects/*}
```

需要Project Owner授权Resource的Read和Create权限。

**项目未支持Spark任务运行**

报错信息如下。

```
Exception in thread "main" org.apache.hadoop.yarn.exceptions.YarnException: com.aliyun.odps.OdpsException: ODPS-0420095: Access Denied - The task is not in release range: CUPID
```

首先需要确认项目所在的Region中，是否已经提供了Spark on MaxCompute服务。同时，检查**Spark-defaults.conf**配置信息是否与产品文档中的要求一致。如果Region已经支持，且**Spark-defaults.conf**配置信息正确，请通过工单进行咨询。

**运行时报错**

报错信息如下。

```
No space left on device
```

由于Spark使用网盘进行本地存储（Shuffle数据和BlockManager溢出的数据均存储在网盘上），因此需要先检查网盘的大小设置。网盘的大小通过参数 `spark.hadoop.odps.cupid.disk.driver.device_size` 控制，默认20 GB，最大100 GB。如果调整到100 GB仍然报此错误，则需要分析具体原因。 最常见的原因为数据倾斜，在Shuffle或者Cache过程中数据集中分布在了某些Block。此时可以通过缩小单个Executor的并发（spark.executor.cores）或是增加 Executor的数量（spark.executor.instances）来解决问题。

#### 11.1.4. OSS数据源

**11.1.4.1. 前言**

#### 功能介绍

MaxCompute作为阿里云大数据平台的核心计算组件，拥有强大的计算能力，能够调度大量的节点进行并行计算，同时对分布式计算中的Failover及重试等均有一套行之有效的处理管理机制。而MaxCompute SQL能在简明的语义上实现各种数据处理逻辑，在阿里内外更是广为应用，在其上实现与各种数据源的互通，对于打通整个阿里云的数据生态具有重要意义。 下面通过简单的示例，演示如何在MaxCompute上访问并处理OSS数据。

##### 11.1.4.2. 使用内置Extractor读取OSS数据

**11.1.4.2.1. 概述**

本文为您介绍如何使用MaxCompute内置的Extractor读取OSS数据。

#### 使用说明

使用MaxCompute内置的Extractor，可以非常方便的读取按照约定格式存储的OSS数据。您只需要创建一个外部表，就能以这张表作为源表进行查询操作。 假设有一份CSV数据保存在OSS上，**endpoint**为oss-cn-shanghai-internal.aliyuncs.com，**bucket**为oss-odps-test，数据文件放在/demo/SampleData/CSV/AmbulanceData/vehicle.csv中。使用内置Extractor读取OSS数据的相关操作示例如下面各章节所示。

###### 11.1.4.2.2. 创建外部表

```
CREATE EXTERNAL TABLE IF NOT EXISTS ambulance_data_csv_external ( vehicleId INT, recordId INT, patientId INT, calls INT, locationLatitute DOUBLE, locationLongtitue DOUBLE, recordTime STRING, direction STRING
```

)

```
STORED BY 'com.aliyun.odps.CsvStorageHandler' WITH SERDEPROPERTIES (
 'odps.properties.rolearn'='acs:ram::xxxxx:role/aliyunodpsdefaultrole'
```

)

```
LOCATION 'oss://oss-cn-shanghai-internal.aliyuncs.com/oss-odps-test/Demo/';
```

**说明**

STORED BY：指定内置的StorageHandler。**com.aliyun.odps.CsvStorageHandler**是内置的处理CSV格式文件的StorageHandler，定义了如何读或写CSV文件。您只需要指定该参数，相关逻辑已经由系统实现。 WITH SERDEPROPERTIES：指定外部表相关参数。其中**odps.properties.rolearn**指定RAM中AliyunODPSDefaultRole的ARN信息。当关联OSS权限使用STS模式授权时，您需要指定此参数。 LOCATION：指定需要读取数据的OSS目录，系统会默认读取该目录下所有的文件。 外部表只是在系统中记录了与OSS目录的关联，当删除这张表时，对应的LOCATION数据不会被删除。

**查看表结构**

您可以执行如下命令，查看创建好的外部表结构信息。

```
DESC EXTENDED <table_name>;
```

返回结果包含和内部表一样的基础信息、外部表的StorageHandler和LOCATION等信息。

###### 11.1.4.2.3. 查询外部表

#### 使用说明

外部表创建成功后，您可以像使用普通表一样使用这个外部表。

**示例数据**

假设/demo/SampleData/CSV/AmbulanceData/vehicle.csv的数据如下。

```
1,1,51,1,46.81006,-92.08174,9/14/2017 0:00,S 1,2,13,1,46.81006,-92.08174,9/14/2017 0:00,NE 1,3,48,1,46.81006,-92.08174,9/14/2017 0:00,NE 1,4,30,1,46.81006,-92.08174,9/14/2017 0:00,W 1,5,47,1,46.81006,-92.08174,9/14/2017 0:00,S 1,6,9,1,46.81006,-92.08174,9/14/2017 0:00,S 1,7,53,1,46.81006,-92.08174,9/14/2017 0:00,N 1,8,63,1,46.81006,-92.08174,9/14/2017 0:00,SW 1,9,4,1,46.81006,-92.08174,9/14/2017 0:00,NE 1,10,31,1,46.81006,-92.08174,9/14/2017 0:00,N
```

**示例代码**

执行如下命令，提交一个作业，调用内置CSV Extractor，从OSS读取数据进行处理。

```
SELECT recordId, patientId, direction; FROM ambulance_data_csv_external; WHERE patientId > 25;
```

**说明**

外部表只能通过MaxCompute SQL操作，MaxCompute MapReduce无法操作外部表。 如果需要底层通过HTTPS获取数据，可以在SQL前添加Flag set odps.sql.unstructured.data.oss.use.https=true; 后，一起提交执行来实现。

**查看结果**

输出结果如下。

```
+------------+------------+-----------+
| recordId | patientId | direction |
+------------+------------+-----------+
| 1 | 51 | S |
| 3 | 48 | NE |
| 4 | 30 | W |
| 5 | 47 | S |
| 7 | 53 | N |
| 8 | 63 | SW |
| 10 | 31 | N |
+------------+------------+-----------+
```

**说明**

系统内置提供了**CsvStorageHandler**、**TsvStorageHandler**以及**TextStorageHandler**。

###### 11.1.4.2.4. MSCK REPAIR TABLE

本文为您介绍MaxCompute的MSCK REPAIR TABLE语法，并提供参考示例。

**命令说明**

MaxCompute的MSCK REPAIR TABLE语法支持自动补全添加外表分区，语法格式如下。

```
MSCK [REPAIR] TABLE external_table_name [ADD PARTITIONS];
```

**语法说明**

将数据导入OSS时，OSS文件路径需要符合格式oss://xxx/table-location/ptname1=ptvalue1/ptname2=ptvalue2/xxx。 建立外部表时，需要指定分区的结构。 执行 MSCK [REPAIR] TABLE external_table_name [ADD PARTITIONS]; 时，SQL会自动解析OSS的目录结构，自动识别分区，并为外部表添加分区信息。

**操作示例**

1. 上传数据至OSS，OSS文件路径如下。
2. 执行如下命令创建外部表orc_pt_v0，外部表中需要指定分区pt的结构。

```
CREATE EXTERNAL TABLE orc_pt_v0 ( name STRING
```

)

```
PARTITIONED BY (pt bigint) STORED BY 'com.aliyun.odps.CsvStorageHandler' WITH SERDEPROPERTIES ( 'odps.properties.rolearn'='acs:ram::xxxxx:role/aliyunodpsdefaultrole'
```

)

```
LOCATION 'oss://xxx/odps-ext-reg-perf/orc-pt-v0/';
```

3. 执行如下命令自动补全外部表orc_pt_v0的分区。

```
MSCK REPAIR TABLE orc_pt_v0 ADD PARTITIONS;
```

`--`该场景中，`MSCK`语法等价于执行如下三条语句。

```
ALTER TABLE orc_pt_v0 ADD PARTITION (pt=1); ALTER TABLE orc_pt_v0 ADD PARTITION (pt=10); ALTER TABLE orc_pt_v0 ADD PARTITION (pt=100);
```

###### 11.1.4.2.5. 读取GZIP格式压缩的CSV或TSV数据

#### 使用说明

MaxCompute只支持通过内置Extractor读取OSS上以GZIP格式压缩的CSV或TSV数据。与读取非压缩文件相比，主要区别是SERDEPROPERTIES指定的属性。

**说明**

如果OSS上的数据文件为归档文件，需要先解冻文件。

**示例说明**

```
CREATE EXTERNAL TABLE IF NOT EXISTS ambulance_data_csv_external ( vehicleId BIGINT, recordId BIGINT, patientId BIGINT, calls BIGINT, locationLatitute DOUBLE, locationLongtitue DOUBLE, recordTime STRING, direction STRING
```

)

```
STORED BY 'com.aliyun.odps.CsvStorageHandler' WITH SERDEPROPERTIES (
 'odps.properties.rolearn'='acs:ram::xxxxx:role/aliyunodpsdefaultrole'
 [,'odps.text.option.gzip.input.enabled'='true']
 [,'name3'='value3']
```

)

```
LOCATION 'oss://oss-cn-hangzhou-zmf.aliyuncs.com/oss-odps-test/Demo/SampleData/CSV/AmbulanceData/';
```

SERDEPROPERTIES支持的属性项如下。

| 属性名 | 属性值 | 默认值 | 说明 |
|---|---|---|---|
| odps.text.option.gzip.input.enabled | True False | False | 打开或关闭读压缩。 |
| odps.text.option.gzip.output.enabled | True False | False | 打开或关闭写压缩。 |
| odps.text.option.header.lines.count | 非负整数 | 0 | 跳过文本文件前N行。 |
| odps.text.option.null.indicator | 字符串 | 空字符串 | 指定文本中的哪种字符串会被解析为SQL中的NULL。例如 \N 指代NULL，则 a,\N,b 会解析为 a,NULL,b 。 |

| odps.text.option.ignore.empty.lines | True False | True | 指定是否忽略空行。 |
|---|---|---|---|
| odps.text.option.encoding | UTF-8 UTF-16 US-ASCII GBK | UTF-8 | 指定文本的字符编码。 |
| odps.text.option.delimiter | 单个字符 | 英文逗号（,） | 指定文本的列分隔符。 |
| odps.text.option.use.quote | True False | False | 当CSV某个字段中包含换行（CRLF）、双引号（需要在 " 前再加 " 转义）或英文逗号（分隔符）时，整个字段必须用双引号（" "）括起来作为列分隔符。该参数指定是否识别CSV的列分隔符 " 。 |

**说明**

将**odps.text.option.gzip.input.enabled**和**odps.text.option.gzip.output.enabled**属性设置为True。

##### 11.1.4.3. 使用自定义Extractor读取OSS数据

**11.1.4.3.1. 概述**

本文为您介绍如何使用自定义的Extractor读取OSS数据。

#### 使用说明

**适用场景**：当OSS中的数据格式比较复杂，内置的Extractor无法满足需求时，需要自定义Extractor来读取OSS文件中的数据。
**业务示例：**假设有一份TEXT数据文件保存在OSS上，记录之间的列通过|分割。数据文件放
在/demo/SampleData/CustomTxt/AmbulanceData/vehicle.csv中。使用自定义Extractor读取OSS数据的相关操作示例如下面各章节所示。

###### 11.1.4.3.2. 定义StorageHandler

本文为您介绍如何在使用自定义Extractor的场景下定义StorageHandler，并提供参考示例。

**示例说明**

此时您可以提供自己的数据解析逻辑。而StorageHandler就是作为这些自定义逻辑的统一入口，用来指定您自己实现的Extractor和Outputer的类型。这个入口通常只是提供一个非常简单的定义，例如可以实现如下示例中的**SpeicalTextStorageHandler**。

```java
package com.aliyun.odps.udf.example.text; public class SpeicalTextStorageHandler extends OdpsStorageHandler { @Override public Class<? extends Extractor> getExtractorClass() { return TextExtractor.class; } @Override public Class<? extends Outputer> getOutputerClass() { return TextOutputer.class; } }
```

**说明**

需要注意，对于上述的这种数据格式（用|分割的文本数据），MaxCompute内置的**TextStorageHandler**是可以处理的。此处只是作为一个简单的示例，用来介绍使用SDK定制自定义StorageHandler（尤其是Extractor）来处理特殊数据的方法。

###### 11.1.4.3.3. 定义Extractor

本文介绍如何在使用自定义Extractor的场景下定义Extractor，并提供参考示例。

**示例说明**

下面示例中的**TextExtractor**可以将分隔符作为参数传输进来，可以处理所有类似格式的文本文件。

```java
/**
* Text extractor that extract schematized records from formatted plain-
text(csv, tsv etc.)
**/
public class TextExtractor extends Extractor { private InputStreamSet inputs; private String columnDelimiter; private DataAttributes attributes; private BufferedReader currentReader; private boolean firstRead = true; public TextExtractor() { // default to ",", this can be overwritten if a specific delimiter is provided (via DataAttributes) this.columnDelimiter = ","; } // no particular usage for execution context in this example @Override public void setup(ExecutionContext ctx, InputStreamSet inputs, DataAttributes attributes) { this.inputs = inputs;
```

`-- inputs`是一个`InputStreamSet`，每次调用`next()`返回一个`InputStream`，这个`InputStream`可以读取一个`OSS`文件的所有内容。

```
this.attributes = attributes; // check if "delimiter" attribute is supplied via SQL query String columnDelimiter = this.attributes.getValueByKey("delimiter");
```

`-- delimiter`通过`DDL`语句传输参数。

```java
if ( columnDelimiter != null) { this.columnDelimiter = columnDelimiter; } // note: more properties can be inited from attributes if needed } @Override public Record extract() throws IOException { String line = readNextLine(); if (line == null) { return null;
```

`--` 返回`null`表示这个表中已经没有记录可读了。

```
} return textLineToRecord(line);
```

`-- textLineToRecord`将一行数据按照`delimiter`分割为多个列。完整实现请参见完整的`TextExtractor`实现。 `-- extactor()`调用返回一条`Record`，代表从`OSS`数据中抽取出的一条`Record`。

```java
} @Override public void close(){ // no-op } }
```

###### 11.1.4.3.4. 编译打包

**示例说明**

类似于普通Java UDF的使用方式，您可以将Java代码实现编译及打包，并通过如下命令上传到MaxCompute。

```
add jar odps-udf-example.jar;
```

###### 11.1.4.3.5. 创建外部表

**示例说明**

在代码JAR包上传完成后，与使用内置Extractor类似，您同样需要执行如下命令，建立一个外部表。不同的是，此时在指定外部表访问数据的时候，需要使用自定义的 StorageHandler。

```
CREATE EXTERNAL TABLE IF NOT EXISTS ambulance_data_txt_external ( vehicleId int, recordId int, patientId int, calls int, locationLatitute double, locationLongtitue double, recordTime string, direction string
```

)

```
STORED BY 'com.aliyun.odps.udf.example.text.SpeicalTextStorageHandler' WITH SERDEPROPERTIES('delimiter'='|')
```

`-- SERDEPROPERITES`可以指定参数，这些参数会通过`DataAttributes`传递到`Extractor`代码中。

```
LOCATION 'oss://<*your-id*>:<*your-secret-key*>@oss-cn-shanghai-internal.aliyuncs.com/oss-odpstest/Demo/SampleData/CustomTxt/AmbulanceData/' USING 'odps-udf-example.jar';
```

`--` 同时需要指定类定义所在的`JAR`包。

###### 11.1.4.3.6. 查询外部表

**示例数据**

假设/demo/SampleData/CustomTxt/AmbulanceData/vehicle.csv的数据如下。

```
1|1|51|1|46.81006|-92.08174|9/14/2017 0:00|S 1|2|13|1|46.81006|-92.08174|9/14/2017 0:00|NE 1|3|48|1|46.81006|-92.08174|9/14/2017 0:00|NE 1|4|30|1|46.81006|-92.08174|9/14/2017 0:00|W 1|5|47|1|46.81006|-92.08174|9/14/2017 0:00|S 1|6|9|1|46.81006|-92.08174|9/14/2017 0:00|S 1|7|53|1|46.81006|-92.08174|9/14/2017 0:00|N 1|8|63|1|46.81006|-92.08174|9/14/2017 0:00|SW 1|9|4|1|46.81006|-92.08174|9/14/2017 0:00|NE 1|10|31|1|46.81006|-92.08174|9/14/2017 0:00|N
```

**示例命令**

执行如下命令，提交一个作业，调用自定义的Extractor，从OSS读取数据进行处理。

```
SELECT recordId, patientId, direction; FROM ambulance_data_txt_external; WHERE patientId > 25;
```

**查看结果**

输出结果如下。

```
+------------+------------+-----------+
| recordId   | patientId  | direction |
+------------+------------+-----------+
|      1     |     51     |     S     |
|      3     |     48     |     NE    |
|      4     |     30     |     W     |
|      5     |     47     |     S     |
|      7     |     53     |     N     |
|      8     |     63     |     SW    |
|      10    |     31     |     N     |
+------------+------------+-----------+
```

##### 11.1.4.4. 使用自定义Extractor读取外部非结构化数据

本文为您介绍如何使用自定义Extractor读取外部非结构化数据，并提供参考示例。

**使用示例**

在前面的章节中，介绍了利用内置及自定义Extractor处理OSS上CSV等文本数据的方法。本文将以WAV格式音频文件为例，详解如何通过自定义Extractor访问与处理OSS上的非文本数据。
1. 自定义**SpeechSentenceSnrExtractor**主体逻辑。您在Setup接口中读取参数，进行初始化，并且导入语音处理模型（通过Resource引入）。

```java
public SpeechSentenceSnrExtractor(){ this.utteranceLabels = new HashMap<String, UtteranceLabel>(); } @Override public void setup(ExecutionContext ctx, InputStreamSet inputs, DataAttributes attributes){ this.inputs = inputs; this.attributes = attributes; this.mlfFileName = this.attributes.getValueByKey(MLF_FILE_ATTRIBUTE_KEY); String sampleRateInKHzStr = this.attributes.getValueByKey(SPEECH_SAMPLE_RATE_KEY); this.sampleRateInKHz = Double.parseDouble(sampleRateInKHzStr); try { // read the speech model file from resource and load the model into memory BufferedInputStream inputStream = ctx.readResourceFileAsStream(mlfFileName); loadMlfLabelsFromResource(inputStream); inputStream.close(); } catch (IOException e) { throw new RuntimeException("reading model from mlf failed with exception " + e.getMessage()); } } @Override public Record extract() throws IOException { SourceInputStream inputStream = inputs.next(); if (inputStream == null){ return null; } // process one wav file to extract one output record [snr, id] String fileName = inputStream.getFileName(); fileName = fileName.substring(fileName.lastIndexOf('/') + 1); logger.info("Processing wav file " + fileName); // infer id from speech file name String id = fileName.substring(0, fileName.lastIndexOf('.')); // read speech file into memory buffer long fileSize = inputStream.getFileSize(); byte[] buffer = new byte[(int)fileSize]; int readSize = inputStream.readToEnd(buffer); inputStream.close(); // compute the avg sentence snr from speech file double snr = computeSnr(id, buffer, readSize); // construct output record [snr, id] Column[] outputColumns = this.attributes.getRecordColumns(); ArrayRecord record = new ArrayRecord(outputColumns); record.setDouble(0, snr); record.setString(1, id); return record; } private void loadMlfLabelsFromResource(BufferedInputStream fileInputStream) throws IOException { // loading MLF label from resource, skipped here } // compute the snr of the speech sentence, assuming the input buffer contains the entire content of a wav file private double computeSnr(String id, byte[] buffer, int validBufferLen){ // computing the snr value for the wav file (supplied as byte buffer array), skipped here }
```

**说明**

**extract()**接口中，实现了对语音文件的具体读取和处理逻辑，对读取的数据根据语音模型进行信噪比的计算，并且将结果填充成**[snr,id]**格式的Record。
2. 执行如下命令，创建外部表。

```
CREATE EXTERNAL TABLE IF NOT EXISTS speech_sentence_snr_external ( sentence_snr double, id string
```

)

```
STORED BY 'com.aliyun.odps.udf.example.speech.SpeechStorageHandler' WITH SERDEPROPERTIES ( 'mlfFileName'='sm_random_5_utterance.text.label' , 'speechSampleRateInKHz' = '16'
```

)

```
LOCATION 'oss://<*your-id*>:<*your-secret-key*>@oss-cn-shanghai-internal.aliyuncs.com/oss-odps-test/dev/SpeechSentenceTest/' USING 'odps-udf-example.jar,sm_random_5_utterance.text.label';
```

3. 执行如下命令，从OSS读取数据进行处理。

```
SELECT sentence_snr, id FROM speech_sentence_snr_external WHERE sentence_snr > 10.0;
```

4. 处理完成，输出如下结果。

```
--------------------------------------------------------------
| sentence_snr | id |
--------------------------------------------------------------
| 34.4703      | J310209090013_H02_K03_042 |
--------------------------------------------------------------
| 31.3905      | tsh148_seg_2_3013_3_6_48_80bd359827e24dd7_0 |
--------------------------------------------------------------
| 35.4774      | tsh148_seg_3013_1_31_11_9d7c87aef9f3e559_0 |
+--------------+----------------------------------------------
| 16.0462      | tsh148_seg_3013_2_29_49_f4cb0990a6b4060c_0 |
--------------------------------------------------------------
| 14.5568 | tsh_148_3013_5_13_47_3d5008d792408f81_0 |
--------------------------------------------------------------
```

**说明**

通过自定义Extractor，您在SQL语句上即可分布式地处理多个OSS上的语音数据文件。同样的，使用类似的方法，您可以方便的利用MaxCompute的大规模计算能力，完成对图像或视频等各种类型非结构化数据的处理。

##### 11.1.4.5. 数据的分区

**11.1.4.5.1. 概述**

本文为您介绍外部表的分区功能。

#### 使用说明

在前面的章节中了解到外部表是通过 `LOCATION` 指向OSS目录。默认情况下，MaxCompute会读取该目录及其子目录下的所有文件。然而，面对不断累积的海量数据，这种全目录扫描方式往往会造成巨大的I/O浪费和时间损耗。为解决这一痛点，通常采用以下两种方法。
**减少访问数据量**：您自己负责对数据存放地址做好规划，同时考虑使用多个外部表来描述不同部分的数据，让每个外部表的LOCATION指向数据的一个子集。
**数据分区**：外部表与内部表一样，支持分区表的功能，您可以利用分区功能对数据做系统化的管理。
下面章节通过简单的示例，演示如何使用外部表的分区功能。

###### 11.1.4.5.2. 分区数据在OSS上的标准组织方式和路径格式

本文介绍OSS上分区数据的标准组织规范与路径格式，提供从目录规划、外部表定义、分区注册到SQL查询的完整示例，帮助您通过分区机制精准访问数据，避免全量扫描带来的I/O浪费。

#### 使用说明

与MaxCompute内部表不同，对于存放在外部存储上（如OSS）上面的数据，MaxCompute没有数据的管理权，因此您如果需要在系统中使用分区表功能，在OSS上的数据文件的存放路径需要符合一定的格式，路径格式如下所示。

```
partitionKey1=value1\partitionKey2=value2\...
```

**示例说明**

1. 假设您每天的LOG文件存放在OSS上面，并希望能在通过MaxCompute处理的时候，能够按照粒度为天来访问一部分数据。假设这些LOG文件是CSV的格式（复杂
自定义格式用法也类似），此时可以使用如下的分区外部表来定义数据。

```
CREATE EXTERNAL TABLE log_table_external ( click STRING, ip STRING, url STRING
```

)

```
PARTITIONED BY ( year STRING, month STRING, day STRING
```

)

```
STORED BY 'com.aliyun.odps.CsvStorageHandler' LOCATION 'oss://<ak_id>:<ak_key>@oss-cn-shanghai-internal.aliyuncs.com/oss-odps-test/log_data/';
```

**说明**

与前面章节中的外部表示例不同，在上述的三层分区示例中，在定义外部表的时候，通过**PARTITIONED BY**的语法，指定该外部表为分区表，分区的Key分别是Year、Month和Day。
2. 为了让类似上述的分区能够生效，在OSS上面存储数据的时候需要遵循前面提到的路径格式。一个有效的路径存储Layout的示例如下。

```
osscmd ls oss://oss-odps-test/log_data/ 2017-09-14 08:03:35 128MB Standard oss://oss-odpstest/log_data/year=2017/month=06/day=01/logfile 2017-09-14 08:04:12 127MB Standard oss://oss-odpstest/log_data/year=2017/month=06/day=01/logfile.1 2017-09-14 08:05:02 118MB Standard oss://oss-odpstest/log_data/year=2017/month=06/day=02/logfile 2017-09-14 08:06:45 123MB Standard oss://oss-odpstest/log_data/year=2017/month=07/day=10/logfile 2017-09-14 08:07:11 115MB Standard oss://oss-odpstest/log_data/year=2017/month=08/day=08/logfile ...
```

**说明**

如果您准备了离线数据，即通过工具自行将离线数据上传到OSS存储服务上，此时数据路径格式是由您决定的。如果想要外部表的分区表功能正常工作，推荐您上传数据的时候遵循如上路径格式。
3. 在如上的前提下，通过**ALTER TABLE ADD PARTITION**语句，将分区信息引入MaxCompute。对应的DDL语句示例如下。

```
ALTER TABLE log_table_external ADD PARTITION (year = '2017', month = '06', day = '01'); ALTER TABLE log_table_external ADD PARTITION (year = '2017', month = '06', day = '02'); ALTER TABLE log_table_external ADD PARTITION (year = '2017', month = '07', day = '10'); ALTER TABLE log_table_external ADD PARTITION (year = '2017', month = '08', day = '08'); ...
```

4. 在数据准备好并且**PARTITION**信息引入系统之后，可以通过SQL语句对OSS上的外部表数据的分区进行操作，示例如下。
假设您只想分析2017年6月1号当天，有多少不同的IP出现在LOG里面，可以通过如下命令实现。

```
SELECT count(distinct(ip)) FROM log_table_external WHERE year = '2017' AND month = '06' AND day = '01';
```

**说明**

此时，对于**log_table_external**这个外部表对应的目录，将只访问log_data/year=2016/month=06/day=01子目录下的文件（logfile和logfile.1）， 而不会对整个log_data/目录作全量数据扫描，避免了大量无用的IO操作。 同样，假设您只希望对2017年下半年的数据做分析，则可以通过如下命令实现。

```
SELECT count(distinct(ip)) FROM log_table_external WHERE year = '2017' AND month > '06';
```

**说明**

此时，只访问OSS上面存储的下半年的LOG。

###### 11.1.4.5.3. 分区数据在OSS上的自定义路径

#### 使用说明

如果您有事先保存在OSS上面的历史数据，但是该数据没有按照partitionKey1=value1\partitionKey2=value2\...的路径格式存放，此时同样可以通过 MaxCompute的分区方式进行访问计算，MaxCompute同样提供了通过自定义路径来引入**PARTITION**的方法。

**示例说明**

1. 假设您的数据路径上只有简单的分区值，而无分区Key信息，此时数据的路径存储Layout的示例如下。

```
osscmd ls oss://oss-odps-test/log_data_customized/ 2017-09-14 08:03:35 128MB Standard oss://oss-odpstest/log_data_customized/2017/06/01/logfile 2017-09-14 08:04:12 127MB Standard oss://oss-odpstest/log_data_customized/2017/06/01/logfile.1 2017-09-14 08:05:02 118MB Standard oss://oss-odpstest/log_data_customized/2017/06/02/logfile 2017-09-14 08:06:45 123MB Standard oss://oss-odpstest/log_data_customized/2017/07/10/logfile 2017-09-14 08:07:11 115MB Standard oss://oss-odpstest/log_data_customized/2017/08/08/logfile ...
```

2. 此时要绑定不同的子目录到不同的分区上，可以通过类似如下自定义分区路径的命令实现。

```
ALTER TABLE log_table_external ADD PARTITION (year = '2017', month = '06', day = '01') LOCATION 'oss://<ak_id>:<ak_key>@oss-cn-shanghai-internal.aliyuncs.com/oss-odps-test/log_data_customized/2017/06/01/';
```

**说明**

在**ADD PARTITION**的时候增加了LOCATION信息，从而实现自定义分区数据路径后，即使数据存放不符合推荐的partitionKey1=value1\partitionKey2=value2\...格式，也能正确的实现对子目录数据的分区访问。

###### 11.1.4.5.4. 完全自定义的非分区数据子集访问

#### 使用说明

一些特殊情况下，您可能会有访问某个OSS路径上的任意文件子集的需求，而这个文件子集中的文件在路径格式上没有明显的规律性。在这方面MaxCompute非结构化数据处理框架也提供了相应的支持，此处不再展开做详细介绍。 如果您对于相关高阶的特殊用法，有相关的具体需求，可以联系MaxCompute技术团队获取相关支持。

##### 11.1.4.6. OSS数据的输出

###### 11.1.4.6.1. 创建外部表

**示例说明**

与读取OSS数据类似，对OSS数据进行写操作，同样是先通过**CREATE EXTERNAL TABLE**语句创建出一个外部表，再通过标准MaxCompute SQL的**INSERT**
**INTO**或**OVERWRITE**等语句实现的。此处可以使用MaxCompute内置的**TsvStorageHandler**为例进行操作说明。

```
DROP TABLE IF EXISTS tpch_lineitem_tsv_external; CREATE EXTERNAL TABLE IF NOT EXISTS tpch_lineitem_tsv_external ( orderkey BIGINT, suppkey BIGINT, discount DOUBLE, tax DOUBLE, shipdate STRING, linestatus STRING, shipmode STRING, comment STRING
```

)

```
STORED BY 'com.aliyun.odps.TsvStorageHandler' LOCATION 'oss://<AK_id>:<AK_secret>@oss-cn-hangzhou-zmf.aliyuncs.com/oss-odps-test/tsv_output_folder/';
```

**说明**

上述的DDL语句建立了一个外部表**tpch_lineitem_tsv_external**，并将两个维度的外部数据信息关联到这个外部表上。 数据存储介质：LOCATION将一个OSS上的地址关联到外部表上，对这个外部表进行的读写操作都会反映到这个OSS地址上。 数据存储格式：StorageHandler用来表明对数据的读写操作方式，此处使用了MaxCompute内置的**com.aliyun.odps.TsvStorageHandler**，您可以使用这个由系统自带的实现来读取和写出TSV文件。同时您也可以通过MaxCompute的SDK来自定义StorageHandler。

###### 11.1.4.6.2. 通过对外部表的INSERT操作实现TSV文本文件的写出

本文介绍如何通过对外部表的INSERT操作实现TSV文本文件的写出，并提供参考示例。

#### 使用说明

将OSS数据通过外部表关联后，可以通过对外部表执行标准的**INSERT OVERWRITE**或**INSERT INTO**操作进行OSS文件的写出。具体输出数据的来源有 MaxCompute的内部表和通过外部表引入MaxCompute计算体系的外部数据两种。

**说明**

MaxCompute的内部表：可以通过对外部表的**INSERT**操作实现MaxCompute内部表数据到外部存储介质的写出。 通过外部表引入MaxCompute计算体系的外部数据：通过外部表将外部数据引入MaxCompute进行计算，然后再存储到不同的外部存储地址，或是不同的外部存储介质（例如将TableStore数据经由MaxCompute导出到OSS）。

**示例说明**

此处假设您已经有一个名为**tpch_lineitem**的MaxCompute内部表，并需要将其中的一部分数据以TSV格式导出到OSS上。可以在完成上述的创建外部表操作之后， 使用类似如下的**INSERT OVERWRITE**操作进行实现。

```
INSERT OVERWRITE TABLE tpch_lineitem_tsv_external SELECT l_orderkey, l_suppkey, l_discount, l_tax, l_shipdate, l_linestatus, l_shipmode, l_comment FROM tpch_lineitem WHERE l_discount = 0.07 and l_tax = 0.01;
```

上述操作是从内部的**tpch_lineitem**表中，在符合**l_discount = 0.07**并**l_tax = 0.01**的行中选出8个列（对应**tpch_lineitem_tsv_external**这个外部表的 Schema）按照TSV的格式写到OSS上。在上述操作成功完成后，可以看到在OSS上产生的对应TSV数据文件。

**重要**

从MaxCompute向OSS上输出数据时，存在特有的文件结构。 通过MaxCompute对一个OSS地址，使用**INSERT INTO**或**OVERWRITE**外部表做写出操作时，所有的数据将在指定的LOCATION下的.odps文件夹产生。 .odps文件夹中的.meta文件是MaxCompute额外写出的宏数据文件，用于记录当前文件夹中有效的数据。正常情况下，如果**INSERT**操作成功，可以认为当前文件夹的所有数据均是有效数据。只有在存在作业失败的情况下需要对这个宏数据进行解析。 对于中途失败或者被结束进程的作业，针对**INSERT OVERWRITE**操作，再次完成一次成功操作即可避免对.meta文件这个宏数据的解析。 对于高级用户，如果一定需要解析.meta文件，可以联系MaxCompute技术团队获取相关支持。 对于MaxCompute内置的TSV和CSV处理来说，产生的文件数目与对应SQL Stage的并发度是相同的。如果需要控制产生文件的数目，可以配合MaxCompute的各种灵活语义和配置来实现。例如在上述示例中，如果需要强制产生一个TSV文件，可以在**INSERT OVERWRITE**操作的最后加上一个**DISTRIBUTE BY**
**l_discount**，即可在最后插入仅有一个Reducer的Reduce Stage，实现只输出一个TSV文件。

###### 11.1.4.6.3. 通过对外部表的INSERT操作实现非结构化文件的写出

#### 使用说明

同样对于数据的输出，MaxCompute还提供了Outputer接口，允许您的数据通过OutputStream写成自由的非结构化数据文件。此处不再展开做详细介绍。 如果您有相关的具体需求，可以联系MaxCompute技术团队获取相关支持。

###### 11.1.4.6.4. 以MaxCompute为计算介质，实现不同存储介质之间的数据转移

本文介绍如何以MaxCompute为计算介质，实现不同存储介质之间的数据转移，并提供参考示例。

#### 使用说明

外部表作为一个MaxCompute与外部存储介质的接入点，提供了对多种外部数据的读取和写出的功能。依赖于接入点，我们可以实现各种各样的数据计算和存储链路，例如： 读取外部表A关联的OSS数据，在MaxCompute上做复杂计算处理，并输出到外部表B关联的OSS地址。 读取外部表A关联的TableStore数据，在MaxCompute上做复杂计算处理，并输出到外部表B关联的OSS地址。

**说明**

上述示例与数据源为MaxCompute内部表的场景，唯一的区别在于SELECT的来源变成外部表，而不是MaxCompute内置表。

**示例说明**

以MaxCompute为中心的计算平台，实现数据从OSS输入，再输出到OSS（例如另一个LOCATION或不同的OSS账号）的整个流程，如下图所示。 从上图可以看出，从数据的流动和处理逻辑上理解，您可以把非结构化处理框架理解成在MaxCompute计算平台两端有机耦合的数据导入（Ingres）以及导出（Egress），相关步骤如下。
1. 外部的（OSS）数据经过非结构化框架转换，会使用Java用户容易理解的InputStream类提供给自定义代码接口。您自实现Extract逻辑只需要负责对输
入的InputStream做读取、解析、转化以及计算，最终返回MaxCompute计算平台通用的Record格式。
2. 返回的Record可以自由的参与MaxCompute的SQL逻辑运算，这一部分计算是基于MaxCompute内置的强大结构化SQL运算引擎，并可能产生新的
Record。
3. 运算过后的Record再传递给您自定义的Output逻辑，您可以进行进一步的计算转换，并最终将Record里面需要输出的信息通过系统提供的
OutputStream输出，由系统负责写到OSS。

**说明**

上述的所有步骤都是可以由您根据需要进行自由选择与拼接的。

##### 11.1.4.7. OSS的STS模式授权

#### 使用说明

创建外部表时LOCATION访问OSS的账号支持传入明文****************和**Access Key Secret**，但是这样做有泄露账号的风险。在某些场景下，这种风险是不可容忍的，因此MaxCompute提供了更为安全的方式来访问OSS。

**授权方式**

MaxCompute结合了阿里云的访问控制服务（RAM）和令牌服务（STS）来解决账号的安全问题。您可以通过以下两种方式授予权限： 当MaxCompute和OSS的Owner是同一个账号时，可以直接在RAM控制台进行一键授权操作。 自定义授权。 i. 首先需要在RAM中授权MaxCompute访问OSS的权限。 创建角色，角色名例如**AliyunODPSDefaultRole**或**AliyunODPSRoleForOtherUser**，并将策略内容设置如下。 `--`当`MaxCompute`和`OSS`的`Owner`是同一个账号

```json
{ "Statement": [ {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
   "Service": [
     "odps.aliyuncs.com"
```

]

```
 }
}
```

`],`

```json
"Version": "1" }
```

`--`当`MaxCompute`和`OSS`的`Owner`不是同一个账号

```json
{ "Statement": [ {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
   "Service": [
     "MaxCompute的Owner云账号i***@odps.aliyuncs.com"
```

]

```
 }
}
```

`],`

```json
"Version": "1" }
```

ii. 授予角色访问OSS必要的权限**AliyunODPSRolePolicy**，如下所示。

```json
{ "Version": "1", "Statement": [ {
 "Action": [
   "oss:ListBuckets",
   "oss:GetObject",
   "oss:ListObjects",
   "oss:PutObject",
   "oss:DeleteObject",
   "oss:AbortMultipartUpload",
   "oss:ListParts"
```

`],`

```json
 "Resource": "*",
 "Effect": "Allow"
}
```

]

```
}
```

`--` 可自定义其他权限

**说明**

授权完成后，查看角色详情获取Role的RAM信息，后续创建OSS外部表时需指定这个RAM信息。

#### 11.1.5. TableStore数据源

**11.1.5.1. 前言**

#### 使用说明

MaxCompute作为阿里云大数据平台的核心计算组件，承担了集团内外大部分的分布式计算需求。而MaxCompute SQL作为分布式数据处理的主要入口，为快速方便处理或存储EB级别的离线数据提供了强有力的支持。随着大数据业务的不断扩展，新的数据使用场景在不断产生，在这样的背景下，MaxCompute计算框架也在不断的演化，原来主要面对内部特殊格式数据的强大计算能力，也正在一步步的开放给不同的外部数据。在这里我们将详细介绍如何将来自TableStore的数据纳入 MaxCompute上的计算生态，实现多种数据源之间的无缝连接。 对于在线服务等应用场景，NoSQL KV Store（BigTable或HBase）相比传统数据库，具有Schema灵活、易扩展及实时性强等优点。阿里云TableStore是在飞天操作系统之上实现的大规模的NoSQL数据存储服务，提供海量KV数据的存储和实时访问。在阿里内部各BU以及外部阿里云生态圈中具有广泛的应用，尤其是 TableStore在行级别上的实时更新和可覆盖性写入等特性，相对于MaxCompute内置表Append-Only批量操作，提供了一个很好的补充。但是TableStore作为一个偏存储的服务，对于存储在其上的海量数据，在大规模批量并行处理的计算能力上有所欠缺。基于这样的背景，MaxCompute打通了和TableStore的数据互通，支持下面章节通过简单的示例，演示如何在MaxCompute上访问并处理TableStore数据。

**说明**

此处将假设您对于TableStore已经有了一定的了解。如果您对于TableStore不熟悉或者对于整个KV Table的概念比较陌生，可以先自行了解一些TableStore的基本概念（例如主键、分区键、属性列等）。

##### 11.1.5.2. MaxCompute对TableStore数据进行读取和计算

###### 11.1.5.2.1. 创建外部表

#### 使用说明

MaxCompute通过外部表的方式对接TableStore的数据，您通过 `Create External Table` 命令，把对TableStore表数据的描述引入到MaxCompute的Meta系统内部后，即可以如同使用一个普通表一样实现对TableStore数据的处理。

**示例说明**

```
DROP TABLE IF EXISTS ots_table_external; CREATE EXTERNAL TABLE IF NOT EXISTS ots_table_external ( odps_orderkey bigint, odps_orderdate string, odps_custkey bigint, odps_orderstatus string, odps_totalprice double
```

)

```
STORED BY 'com.aliyun.odps.TableStoreStorageHandler' WITH SERDEPROPERTIES ( 'tablestore.columns.mapping'=':o_orderkey, :o_orderdate, o_custkey,o_orderstatus,o_totalprice', 'tablestore.table.name'='ots_tpch_orders'
```

)

```
LOCATION 'tablestore://<*your AK id*>:<*your AK secret key*>@odps-ots-dev.cn-hangzhou.ots.aliyuncs.com';
```

| 参数 | 说明 |
|---|---|
| com.aliyun.odps.TableStoreStorageHandler | 是MaxCompute内置的处理TableStore数据的StorageHandler，定义了MaxCompute和TableStore的交互，相关逻辑由MaxCompute实现。 |
| SERDEPROPERITES | 可以理解成提供参数选项的接口，在使用TableStoreStorageHandler时，有两个必须指定的选项，分别是下方的 tablestore.columns.mapping和tablestore.table.name。 |
| tablestore.columns.mapping | 必选项，用来描述需要通过MaxCompute来访问的TableStore表的列，包括主键和属性列。其中以“:”开头的用来表示 TableStore主键，例如本示例中的 :o_orderkey 和 :o_orderdate 。其他的均为属性列。TableStore支持的主键数最少为1个，最多为4个，主键类型为bigint或string，其中第一个主键为分区键。在指定映射的时候，用户必须提供指定TableStore表的所有主键，对于属性列无特殊要求，可以只提供需要通过MaxCompute来访问的属性列。 |
| tablestore.table.name | 必选项，用来描述需要通过MaxCompute来访问的TableStore表的表名。如果指定的TableStore表名错误（不存在），则会报错，MaxCompute不会主动创建TableStore表。 |
| LOCATION | 用来指定TableStore的具体信息，包括Instance名字和Endpoint等。 |

**说明**

上述示例将一个TableStore表映射到了MaxCompute的一个外部表上。在此基础上，后续对TableStore数据的操作可以直接通过外部表进行。

###### 11.1.5.2.2. 通过外部表访问TableStore数据进行计算

本文介绍如何利用外部表访问TableStore数据并进行计算。

#### 使用说明

创建外部表成功后，TableStore的数据被引入到了MaxCompute的生态中。此时，您便可以通过正常的MaxCompute SQL语法来访问TableStore数据。

**示例说明**

```
SELECT odps_orderkey, odps_orderdate, SUM(odps_totalprice) AS totalprice FROM ots_table_external WHERE odps_orderkey > 5000 AND odps_orderdate >20170725 AND odps_orderdate <20170910 GROUP BY odps_orderkey, odps_orderdate HAVING totalprice> 2000;
```

**说明**

在本示例中，直接使用的是您所熟悉的MaxCompute SQL语法，访问TableStore的所有细节由MaxCompute内部处理。 如果您需要对一份数据做多次计算，相较于每次从TableStore远程读数据，更高效的做法是一次性把需要的数据导入到MaxCompute内部，成为一个 MaxCompute（内部）表。具体示例如下。

```
CREATE TABLE internal_orders AS SELECT odps_orderkey, odps_orderdate, odps_custkey, odps_totalprice FROM ots_table_external WHERE odps_orderkey > 5000 ;
```

**说明**

此时，**internal_orders**即为一个您熟悉的MaxCompute表，并且拥有所有MaxCompute内部表的特性，包括高效的压缩列存储数据格式以及完整的Meta等。 同时因为存储在MaxCompute内部，访问速度比访问外部的TableStore更快，尤其适用于需要进行多次计算的热点数据。

##### 11.1.5.3. 数据从MaxCompute写出到TableStore

#### 使用说明

打通MaxCompute和TableStore的数据生态，除了将TableStore作为批量数据处理的数据来源以外，另一个重要的场景是将MaxCompute的数据处理结果输出到

| SQL的 | INSERT OVERWRITE | 命令来实现。 |
|---|---|---|
| 说明由于MaxCompute不会主动创建外部的TableStore表，因此对TableStore表进行数据输出之前，必须保证该表已经在TableStore上创建过（否则将报错）。 |  |  |

**示例说明**

假设您已经创建了上一章节示例中的**ots_table_external**这个外部表来打通MaxCompute与TableStore数据表**ots_tpch_orders**的链路，并且在MaxCompute 内部存储有一个名为**internal_orders**的数据。此时，您希望对**internal_orders**中的数据进行一定处理后写回到TableStore上，可以通过对外部表做 `INSERT`

| OVERWITE TABLE |  | 操作进行实现，命令示例如下。 |
|---|---|---|
|  | INSERT OVERWRITE TABLE ots_table_external SELECT odps_orderkey, odps_orderdate, odps_custkey, CONCAT(odps_custkey,'SHIPPED'), CEIL(odps_totalprice) FROM internal_orders; |  |

**说明**

对于TableStore这种KV数据的NoSQL存储介质，从MaxCompute的输出将只影响相对应主键所在的行，并且在这些TabeleStore行上面，同样只会更新在 `INSERT OVERWRITE` 外部表时，MaxCompute默认按照200条记录批量（Batch）写入。为了避免一个Batch的总请求大小可能会超出TableStore的限制（4 MB），当前版本支持BatchSize自适应。

#### 11.1.6. AnalyticDB数据源

**11.1.6.1. 前言**

本文介绍如何在MaxCompute中通过创建外表访问并处理AnalyticDB数据源，方便您在AnalyticDB数据更新或加工后，高效实现与MaxCompute数据的联合计算与同步。

#### 使用说明

AnalyticDB系统有更新数据或者加工数据的需求，加工后的数据和MaxCompute中数据做联合计算时，需要将AnalyticDB的数据同步回MaxCompute，此时就需要下面章节通过简单的示例，演示如何在MaxCompute上访问并处理AnalyticDB的数据。

##### 11.1.6.2. 向AnalyticDB中写入数据

###### 11.1.6.2.1. 创建外部表

本文为您介绍如何针对AnalyticDB数据源创建外部表，并提供参考示例，方便您快速建立MaxCompute与AnalyticDB之间的数据连接，实现跨源数据的联合查询与分析。

**示例说明**

**说明**

执行前，请将 `location` 中的 `host` 、 `port` 、 `databasename` 、 ${user} 、 ${password} 和 ${tablename} 替换为您实际的AnalyticDB连接信息。

```
SET odps.sql.hive.compatible=true; DROP TABLE IF EXISTS ads_table_external; CREATE EXTERNAL TABLE IF NOT EXISTS ads_table_external (
  c_int int,
  c_tinyint tinyint,
  c_boolean boolean,
  c_smallint smallint,
  c_biging bigint,
  c_double double,
  c_float float,
  --c_time datetime,
  c_date date,
  c_timestamp datetime,
  c_string string
```

)

```
STORED BY 'com.aliyun.odps.jdbc.JdbcStorageHandler' location 'jdbc:mysql://host:port/databasename?useSSL=false&user=${user}&password=${password}&table=${tablename}';
```

###### 11.1.6.2.2. 写入及查询数据

本文介绍如何利用外部表对AnalyticDB数据进行写入与查询。

**操作说明**

外部表创建成功后，您可以像使用普通表一样使用这个外部表。您可以使用**INSERT OVERWRITE|INTO**语句及**SELECT**语句进行数据写入及查询数据是否写入成功的操作。 具体的语句使用请参见： 《**MaxCompute****开发指南》**的**MaxCompute SQL > DML****语句** **> INSERT****语句** > **更新表中的数据**章节。 《**MaxCompute****开发指南》**的**MaxCompute SQL > DML****语句** **> SELECT****语句** **> SELECT****操作**章节。

##### 11.1.6.3. 从AnalyticDB中读取数据

本文为您介绍如何从AnalyticDB中读取数据，并提供参考示例，方便您快速验证外部表连接并获取源端数据。

**操作示例**

您可以执行以下命令完成外部表的创建与数据读取：

**说明**

执行前，请将 `location` 中的 `host` 、 `port` 、 `databasename` 、 ${user} 、 ${password} 和 ${tablename} 替换为您实际的AnalyticDB连接信息。

```
SET odps.sql.hive.compatible=true; DROP TABLE IF EXISTS ads_read_external; CREATE EXTERNAL TABLE IF NOT EXISTS ads_read_external (
  c_int int,
  c_tinyint tinyint,
  c_boolean boolean,
  c_smallint smallint,
  c_biging bigint,
  c_double double,
  c_float float,
  --c_time datetime,
  c_date date,
  c_timestamp datetime,
  c_string string
```

)

```
STORED BY 'com.aliyun.odps.jdbc.JdbcStorageHandler' location 'jdbc:mysql://host:port/databasename?useSSL=false&user=${user}&password=${password}&table=${tablename}' SELECT * FROM ads_read_external;
```

`--` 查找及读取数据。

#### 11.1.7. RDS数据源

**11.1.7.1. 前言**

本文介绍如何在MaxCompute中通过创建外表访问并处理RDS数据源，方便您在RDS数据更新或加工后，高效实现与MaxCompute数据的联合计算与同步。

#### 使用说明

RDS系统有更新数据或者加工数据的需求，加工后的数据和MaxCompute中数据做联合计算时，需要将RDS的数据同步回MaxCompute，此时就需要支持通过创建下面章节通过简单的示例，演示如何在MaxCompute上访问并处理RDS数据。

**说明**

需要注意，创建外表时，RDS产品中可以没有对应的表；但是对外表进行 `SELECT` 、 `INSERT` 操作的时候，必须要在RDS产品中将对应的表创建好。

##### 11.1.7.2. 向RDS中写入数据

###### 11.1.7.2.1. 创建外部表

```
SET odps.sql.hive.compatible=true; DROP TABLE IF EXISTS rds_table_external; CREATE EXTERNAL TABLE if NOT EXISTS rds_table_external(
   id bigint,
   name string,
   age tinyint
```

)

```
 STORED BY 'com.aliyun.odps.jdbc.JdbcStorageHandler'
 location 'jdbc:mysql://host:port/databasename?useSSL=false&user=${user}&password=${password}&table=${tablename}'
```

###### 11.1.7.2.2. 写入及查询数据

本文介绍如何利用外部表对RDS数据进行写入与查询。

**操作说明**

外部表创建成功后，您可以像使用普通表一样使用这个外部表。您可以使用**INSERT OVERWRITE|INTO**语句及**SELECT**语句进行数据写入及查询数据是否写入成功的操作。 具体的语句使用请参见： 《**MaxCompute****开发指南》**的**MaxCompute SQL > DML****语句** **> INSERT****语句** > **更新表中的数据**章节。 《**MaxCompute****开发指南》**的**MaxCompute SQL > DML****语句** **> SELECT****语句** **> SELECT****操作**章节。

##### 11.1.7.3. 从RDS中读取数据

本文介绍如何从RDS中读取数据，并提供参考示例，方便您快速验证外部表连接并获取源端数据。

**操作示例**

您可以执行以下命令完成外部表的创建与数据读取：

**说明**

执行前，请将 `location` 中的 `host` 、 `port` 、 `databasename` 、 ${user} 、 ${password} 和 ${tablename} 替换为您实际的RDS连接信息。

```
SET odps.sql.hive.compatible=true; DROP TABLE IF EXISTS rds_read_external; CREATE EXTERNAL TABLE IF NOT EXISTS rds_read_external (
  id int,
  name string,
  age int
```

)

```
STORED BY 'com.aliyun.odps.jdbc.JdbcStorageHandler' location 'jdbc:mysql://host:port/databasename?useSSL=false&user=${user}&password=${password}&table=${tablename}';
```

`--` 查找及读取数据。

```
SELECT * FROM rds_read_external;
```

#### 11.1.8. MaxCompute非结构化数据处理（内部）

**11.1.8.1. 前言**

本文介绍如何通过创建Volume外部表，在MaxCompute内部直接读写和处理存储于Volume中的非结构化数据，无需将数据导出至外部系统。

#### 使用说明

目前MaxCompute内部存在这样的非结构化数据处理的问题：数据通过Volume存储在MaxCompute内部，输出的非结构化数据不想导出到外部系统，而是希望可以直接在MaxCompute内部进行处理。 针对上述问题，由于MaxCompute非结构化数据框架是通过External Table的概念来提供MaxCompute与各种数据的联通。因此，与访问并处理OSS非结构化数据的方法类似，MaxCompute通过外部表支持读写Volume，打通了MaxCompute系统内部存储的非结构化处理，从而解决了上述问题。 下面的各章节分别为您介绍如何创建Volume External Table和访问Volume External Table。

##### 11.1.8.2. 创建Volume External Table

###### 11.1.8.2.1. 建表语法

本文介绍创建Volume外部表的建表语法及相关参数说明。

**命令说明**

首先要通过Create External Table语句创建出一个外部表，语法格式如下。

```
DROP TABLE [IF EXISTS] <external_table_name>; CREATE EXTERNAL TABLE [IF NOT EXISTS] <external_table_name> (<column schemas>) [PARTITIONED BY (PARTITION COLUMN schemas)] STORED BY '<StorageHandler>' [WITH SERDEPROPERTIES (
  'name'='value'
```

`)]`

```
LOCATION 'volume://...' [USING '<Resourcename>'] ;
```

**参数说明**

**STORED BY**

目前支持2个内置StorageHandler，即 `com.aliyun.odps.CsvStorageHandler` 和 `com.aliyun.odps.TsvStorageHandler` 。分别支持读写CSV（数据文件列分隔符为英文逗号，行分隔符为 \n ）和TSV（数据文件列分隔符为 \t ，行分隔符为 \n ）格式数据。如果无法使用内置StorageHandler，也支持使用自定义 StorageHandler。

**WITH SERDEPROPERTIES**

当使用自定义StorageHandler时需要指定的属性，可以是Delimiter等的属性。

**LOCATION**

Volume外表的Location格式，具体格式及相关示例如下。 格式如下：

```
volume://[project_name]/volume_name/partition_value
```

示例如下。

```
volume://test_project/volume_data/20190102
```

其中**project_name**部分可以省去。当**project_name**省去的时候，执行DML SQL时使用当前Project获取Volume。例如上面的示例中，如果当前Project为 MyProject，则可以使用的Location格式示例如下。

```
volume:///volume_data/20190102
```

**重要**

目前外表Location非分区表只能指向Volume分区，不支持指向Volume本身。 分区表的表Location需要指向Volume本身。 由于目前Volume路径中无法包含=字符，所以创建分区时默认的标准分区路径ds=2017071无法在Volume上支持，需要自定义分区路径。自定义的分区路径名可以是任意Volume支持的路径名，例如路径为20190102，和Volume路径拼起来的就是volume://test_project/volume_data/20190102。

**USING**

使用自定义StorageHandler，需要先将自定义StorageHandler导出为JAR包，然后以JAR资源方式添加到MaxCompute。因此，在此处需要指定所使用的 StorageHandler资源。

###### 11.1.8.2.2. 使用内置StorageHandler建表

本文介绍如何使用内置StorageHandler创建Volume外部表，并提供非分区表与分区表的建表示例，方便您快速掌握建表方法。

**建表示例**

使用内置StorageHandler建表时，可以分为创建非分区表和创建分区表，对应示例如下。

**创建非分区表**

```
DROP TABLE IF EXISTS volume_ext; CREATE EXTERNAL TABLE volume_ext ( key string, value string
```

)

```
STORED BY 'com.aliyun.odps.CsvStorageHandler'--内置的StorageHandler LOCATION 'volume://test_project/volume_data/20190102' ;
```

**创建分区表**

```
DROP TABLE IF EXISTS volume_ext_pt; CREATE EXTERNAL TABLE volume_ext_pt ( key string, value string
```

)

```
PARTITIONED BY (ds string) STORED BY 'com.aliyun.odps.CsvStorageHandler'--内置的StorageHandler LOCATION 'volume://test_project/volume_data'; ALTER TABLE volume_ext_pt DROP IF EXISTS PARTITION (ds="20190102"); ALTER TABLE volume_ext_pt ADD PARTITION (ds="20190102") LOCATION "volume://test_project/volume_data/20190102";
```

###### 11.1.8.2.3. 使用自定义StorageHandler建表

本文介绍如何通过自定义Java StorageHandler创建Volume外部表，涵盖从开发打包、资源注册到建表配置的完整流程，方便您灵活处理特定格式的非结构化数据。

#### 使用说明

当内置的StorageHandler无法满足需求时，MaxCompute还支持通过Java自定义StorageHandler，指定Volume外表的一些属性，从而通过外表对Volume数据进行处理。

**建表示例**

假设数据为TXT类型，列分隔符为|，通过自定义StorageHandler进行的建表操作如下。
1. 通过MaxCompute Studio或者MaxCompute Eclipse开发插件，自定义各个Java类。
2. 输出JAR包，此示例假设输出的包名为**odps-volume-example.jar**。
3. 执行如下命令，将JAR包添加为MaxCompute的资源（Resource）。

```
add jar odps-volume-example.jar -f;
```

4. 执行如下命令，创建External Table。

```
DROP TABLE IF EXISTS volume_ext; CREATE EXTERNAL TABLE volume_ext ( key string, value string
```

)

```
STORED BY 'com.aliyun.odps.udf.example.text.TextStorageHandler' WITH SERDEPROPERTIES (
   'delimiter'='|'
```

)

```
LOCATION 'volume://myproject/volume_data/20190102' USING 'odps-volume-example.jar';
```

**说明**

表创建成功后，即可通过该外部表对Volume数据进行操作。

##### 11.1.8.3. 访问Volume External Table

本文介绍如何访问Volume外部表。

**示例说明**

与访问MaxCompute内部方式一样，示例如下。

```
SELECT key,value FROM volume_ext_pt WHERE ds="20190102";
```

### 安全增强包

#### 11.2.1. Label权限控制

MaxCompute支持在项目级别为用户设置访问许可等级标签，为表或表的列设置敏感等级标签（Label），用户仅可以访问MaxCompute项目中敏感等级小于等于自身访问许可等级的表或列数据。本文为您介绍Label授权操作并提供示例供参考。

**背景信息**

Label权限控制即LabelSecurity，是项目级别的一种强制访问控制策略。创建MaxCompute项目后，LabelSecurity默认为关闭状态。项目所有者（Project Owner）可以在MaxCompute项目的Project级别，执行 SET LabelSecurity=true|false; 命令，开启或关闭LabelSecurity。 如果开启了LabelSecurity，项目所有者（Project Owner）需要定义明确的表或表的列敏感等级、用户访问许可等级划分标准，并分别为表或表的列、用户或角色设置敏感等级标签、访问许可等级标签。当用户访问设置了敏感等级的数据时，除必须拥有目标表的SELECT权限外，仅能访问敏感等级小于等于自身访问许可等级的表或列数据。 LabelSecurity对敏感数据的支持能力如下： 最小支持粒度为列级别，即对表的列设置敏感等级。 支持对表的任何列设置敏感等级标签。一张表可以由不同敏感等级的列构成。 支持对视图设置敏感等级标签。视图的敏感等级标签和视图对应的源表的敏感等级标签是独立的。 LabelSecurity支持的操作如下。

| 操作 | 说明 | 操作人 | 授权操作入口 |
|---|---|---|---|
| 为表或列数据设置敏感等级标签 | 为表或表的列设置敏感等级标签。 | 项目所有者（Project Owner） 具备Admin角色的用户 | MaxCompute客户端 |
| 为用户或角色设置访问许可等级标签 | 为用户或角色设置可以访问的敏感等级数据标签。 |  |  |
| Label显式授权 | 为低访问许可等级用户或角色授予访问高敏感等级数据的权限。 |  |  |
| 撤销Label显式授权 | 撤销为用户或角色授予的访问高敏感等级数据的权限。 |  |  |
| 清理过期权限 | 删除过期权限信息。 |  |  |

**LabelSecurity默认权限控制策略**

在对表或列数据、用户或角色设置标签之后，基于标签的默认权限控制策略如下： No-ReadUp：不允许用户访问敏感等级大于用户访问许可等级的数据。如果实际业务涉及此场景，需要执行显式授权操作。更多显式授权操作信息，请参见Label显式授权。 Trusted-User：允许用户写不高于用户访问许可等级的数据。新创建的表或视图默认为0级（不保密）。新添加用户默认为0级。

**前提条件**

被授权人的账号或角色名称，且账号或角色已添加至MaxCompute项目。 您可以通过MaxCompute客户端执行 LIST USERS; 或 LIST ROLES; 命令获取账号或角色信息。 授权对象表或列的名称。 您可以通过MaxCompute客户端执行 SHOW TABLES; 命令获取表或视图名称、列名称。

**使用限制**

不支持对分区列设置敏感数据等级标签。

**注意事项**

使用LabelSecurity的注意事项如下： 在一些传统的强制访问控制系统中，为了防止数据在项目内部被任意分发，通常还支持更多复杂的安全策略。例如，不允许用户写敏感等级不高于用户访问许可等级的数据（No-WriteDown）。但在MaxCompute中，考虑到数据敏感等级的管理成本，默认安全策略并不支持No-WriteDown。如果项目有类似需求，您可以通过 SET ObjectCreatorHasGrantPermission=false; 命令，修改项目安全配置，以达到控制目的。 为避免数据在不同项目之间流动，您可以通过 SET ProjectProtection=true; 命令，将项目设置为受保护状态（ProjectProtection）。设置之后，只允许用户在项目内访问数据，有效防止数据流出到项目之外。更多项目数据保护信息，参见数据保护机制。 如果删除了对象，MaxCompute会自动撤销与该对象关联的所有Label授权信息。 当一个用户被移除后，与该用户有关的授权仍然会被保留。一旦该用户以后被再次添加到该项目时，该用户的历史授权访问权限将被重新激活。

**为表或列数据设置敏感等级标签**

由Project Owner或具备Admin角色的用户为表或表的列设置敏感等级标签。 命令格式

```
SET Label <number> TO TABLE <table_name>[(<column_list>)];
```

注意事项如果只是对表设置了敏感等级标签，未对列设置敏感等级标签，则表的所有列的敏感等级都相同且等于对表设置的标签。例如对表设置的敏感等级为2，未设置列的敏感等级，则表的所有列的敏感等级都为2。 对列设置的标签会覆盖对表设置的标签（与等级高低无关），对表设置的标签不会覆盖对列设置的标签。例如最初为表设置的敏感等级为2，然后对表的某一列 col1设置敏感等级为3，此时表的敏感等级为2，表中col1的敏感等级为3，其他列的敏感等级为2。 如果您需要修改对表或列已设置的敏感等级标签，重新执行该命令设置新的等级标签即可。 参数说明

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| number | 是 | 指定敏感等级。取值范围为0~9。数值越大，安全级别越高。 |
| tablename _ | 是 | 指定目标表或视图的名称。 您可以通过执行 SHOW TABLES; 命令获取表或视图名称。 |
| columnlist _ | 否 | 指定列名。可以指定多个列名，列名之间用英文逗号（,）分隔。 |

**为用户或角色设置访问许可等级标签**

由Project Owner或具备Admin角色的用户为其他用户或角色设置访问许可等级标签。 命令格式

```
SET Label <number> TO {USER|ROLE} <name>;
```

注意事项为用户设置访问许可等级标签后，用户只能访问敏感级别小于等于访问许可等级标签的数据。例如指定用户的敏感等级为3，则用户只能访问敏感等级为0~3的表数据或列数据。 如果您需要修改对用户或角色已设置的敏感等级标签，重新执行该命令设置新的访问许可等级标签即可。 参数说明

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| number | 是 | 指定用户或角色可访问的最高数据敏感等级。取值范围为0~9，与数据敏感等级标签相对应。 |
| name | 是 | 指定用户或角色的名称。 您可以通过MaxCompute客户端执行 LIST USERS; 或 LIST ROLES; 命令获取用户账号或角色名称。 |

**Label显式授权**

由Project Owner或具备Admin角色的用户为低级别用户授予访问高敏感等级数据的权限。 命令格式

```
GRANT Label <number> ON TABLE <table_name> [(<column_list>)] TO {USER|ROLE} <name> [WITH exp <days>];
```

注意事项显式授予用户的表的列Label权限，会覆盖显式授予用户的表的Label权限。 参数说明

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| number | 是 | 指定用户或角色可访问的最高数据敏感等级。 取值范围为0~9，与数据敏感等级标签相对应。 |
| tablename _ | 是 | 指定目标表或视图的名称。 您可以通过MaxCompute客户端执行 SHOW TABLES; 命令获取表或视图名称。 |
| columnlist _ | 否 | 当需要授予目标表或视图中指定列的访问权限时，需要配置该参数。单次授权可以指定多个列名，列名之间用英文逗号（,）分隔。 |
| name | 是 | 指定用户或角色的名称。 您可以通过MaxCompute客户端执行 LIST USERS; 或 LIST ROLES; 命令获取用户账号或角色名称。 |
| days | 否 | 指定权限过期时间，单位为天。取值范围为：0~263-1。不指定该参数时，默认过期时间为180天。 |

**撤销Label显式授权**

由Project Owner或具备Admin角色的用户撤销Label显式授权。 命令格式

```
REVOKE Label ON TABLE <table_name> [(<column_list>)] FROM {USER|ROLE} <name>;
```

注意事项撤销显式授予用户的表的Label权限，会同时撤销显式授予用户的表列的Label权限。 撤销显式Label授权信息，不会影响为用户设置的访问许可等级标签。例如用户的访问许可等级为2，为用户显式授予访问某张表敏感等级不超过3的数据，撤销授权后，用户仍然可以访问表中敏感等级小于等于2的数据。 参数说明

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| tablename _ | 是 | 指定目标表或视图的名称。 您可以通过MaxCompute客户端执行 SHOW TABLES; 命令获取表或视图名称。 |
| columnlist _ | 否 | 当需要撤销目标表或视图中指定列的敏感数据访问权限时，需要配置该参数。可以指定多个列名，列名之间用英文逗号（,）分隔。 |

| name | 是 | 指定用户或角色的名称。 您可以通过MaxCompute客户端执行 LIST USERS; 或 LIST ROLES; 命令获取用户账号或角色名称。 |
|---|---|---|

**清理过期权限**

当Label显式授权信息过期后，需要由Project Owner或具备Admin角色的用户执行如下命令清理过期权限信息。

```
clear expired grants;
```

假设项目test_project_a中存在一张表sale_detail，shop_name、customer_id和total_price为表的列。Bob***@aliyun.com是test_project_a的项目所有者。 Allen为隶属于Bob的RAM用户，已被添加至项目test_project_a中。 示例一：为表sale_detail或表的列设置敏感等级标签，命令示例如下。 `--Bob`进入项目`test_project_a`。

```
USE test_project_a;
```

`--`设置表`sale_detail`的`Label`为1级。此时表中所有列的敏感等级为1级。

```
SET Label 1 TO TABLE sale_detail;
```

`--`设置`sale_detail`的`shop_name`和`customer_id`两列的`Label`为2级。此时其他列的`Label`仍为1。

```
SET Label 2 TO TABLE sale_detail(shop_name, customer_id);
```

`--`修改表`sale_detail`的`Label`为3级。需要注意的是：此时`shop_name`和`customer_id`两列的`Label`仍为2级，其他列的`Label`修改为3。

```
SET Label 3 TO TABLE sale_detail;
```

`--`修改表`sale_detail`的`shop_name`和`customer_id`两列的`Label`为4级。此时其他列的`Label`仍为3。

```
SET Label 4 TO TABLE sale_detail(shop_name, customer_id);
```

`--`查看表的`Label`信息。

```
DESCRIBE sale_detail;
```

`--`返回结果如下。

```
+------------------------------------------------------------------------------------+
| Owner: ALIYUN$****@test.aliyun.com | Project: ****                                 |
| TableComment:                                                                      |
+------------------------------------------------------------------------------------+
| CreateTime:               2021-12-13 11:27:04                                      |
| LastDDLTime:              2021-12-13 11:27:04                                      |
| LastModifiedTime:         2021-12-13 11:27:26                                      |
+------------------------------------------------------------------------------------+
| TableLabel:               3                                                        |  --表的敏感等级为3。
| MaxLabel:                 L4                                                       |
+------------------------------------------------------------------------------------+
| InternalTable: YES      | Size: 784                                                |
+------------------------------------------------------------------------------------+
| Native Columns:                                                                    |
+------------------------------------------------------------------------------------+
| Field           | Type       | Label | Comment                                     |
+------------------------------------------------------------------------------------+
| shop_name       | string     | 4     |                                             |  --列的敏感等级为4。
| customer_id     | string     | 4     |                                             |  --列的敏感等级为4。
| total_price     | double     | 3     |                                             |  --列的敏感等级为3。
+------------------------------------------------------------------------------------+
| Partition Columns:                                                                 |
+------------------------------------------------------------------------------------+
| sale_date       | string     |                                                     |
| region          | string     |                                                     |
+------------------------------------------------------------------------------------+
```

示例二：为项目test_project_a中的用户Kate***@aliyun.com及RAM用户RAM$Bob***@aliyun.com:Allen，设置访问许可等级标签，命令示例如下。 `--Bob`进入项目`test_project_a`。

```
USE test_project_a;
```

`--`设置`Kate`的访问许可等级标签为3级，则`Kate`能访问敏感等级为0~3级的数据。

```
SET Label 3 TO USER ALIYUN$Kate***@aliyun.com;
```

`--`设置`RAM`用户`Allen`的访问许可等级标签为1级，则`Allen`能访问敏感等级为0~1级的数据。

```
SET Label 1 TO USER RAM$Bob***@aliyun.com:Allen;
```

`--`查看`Allen`的访问许可等级信息。

```
SHOW label grants FOR RAM$Bob***@aliyun.com:Allen;
```

`--`返回结果如下。

```
User Label: 1 (granted label list is empty)
```

示例三：为Allen显式授予访问高敏感级数据的权限，命令示例如下。 `--Bob`进入项目`test_project_a`。

```
USE test_project_a;
```

`--`显式授权`Allen`访问`sale_detail`表中敏感度不超过3级的数据，授权有效期为4天。

```
GRANT Label 3 ON TABLE sale_detail TO USER RAM$Bob***@aliyun.com:Allen WITH exp 4;
```

`--`查看`Allen`的显式授权结果。

```
SHOW label grants ON TABLE sale_detail FOR USER RAM$Bob***@aliyun.com:Allen;
```

`--`返回结果如下。

```
User Label: 1 +-------------+--------------+--------------------------+
| Column      | GrantedLabel | Expires                  |
+-------------+--------------+--------------------------+
| total_price | 3            | 2021-12-31T19:56:18+0800 |
+-------------+--------------+--------------------------+
```

`--`显式授权`Allen`访问`sale_detail`表的`shop_name`、`customer_id`和`total_price`列中敏感度不超过3级的数据，授权有效期为`10`天。

```
GRANT Label 4 ON TABLE sale_detail(shop_name, customer_id, total_price) TO USER RAM$Bob***@aliyun.com:Allen WITH exp 10;
```

`--`查看`Allen`的显式授权结果。

```
SHOW label grants ON TABLE sale_detail FOR USER RAM$Bob***@aliyun.com:Allen;
```

`--`返回结果如下。

```
User Label: 1 +-------------+--------------+--------------------------+
| Column      | GrantedLabel | Expires                  |
+-------------+--------------+--------------------------+
| customer_id | 4            | 2022-01-06T19:58:00+0800 |
+-------------+--------------+--------------------------+
| shop_name   | 4            | 2022-01-06T19:58:00+0800 |
+-------------+--------------+--------------------------+
| total_price | 4            | 2022-01-06T19:58:00+0800 |
+-------------+--------------+--------------------------+
```

示例四：撤销为Allen授予的访问高敏感级数据权限，命令示例如下。 `--`撤销`Allen`访问`sale_detail`表的`shop_name`、`customer_id`和`total_price`列中敏感度不超过3级的数据权限。

```
REVOKE Label ON TABLE sale_detail(shop_name, customer_id, total_price) FROM USER RAM$Bob***@aliyun.com:Allen;
```

`--`查看`Allen`的撤销授权结果。

```
SHOW label grants ON TABLE sale_detail FOR USER RAM$Bob***@aliyun.com:Allen;
```

`--`返回结果如下。

```
User Label: 1 +-------------+--------------+--------------------------+
| Column      | GrantedLabel | Expires                  |
+-------------+--------------+--------------------------+
| total_price | 3            | 2021-12-31T19:56:18+0800 |
+-------------+--------------+--------------------------+
```

`--`撤销`Allen`访问`sale_detail`表中敏感数据的权限。

```
REVOKE Label ON TABLE sale_detail FROM USER RAM$Bob***@aliyun.com:Allen;
```

`--`查看`Allen`的撤销授权结果。

```
SHOW label grants ON TABLE sale_detail FOR USER RAM$Bob***@aliyun.com:Allen;
```

`--`返回结果如下。

```
User Label: 1
```

#### 11.2.2. MaxCompute权限系统增强功能

安全增强包是MaxCompute基于权限模型2.0，对安全和权限体系的进一步增强，可以让您获得更严格更精细的管理能力，也因为安全规则的限制，对普通开发流程提升了管理复杂度，请根据安全需求和业务场景需求综合评估使用。本文为您介绍MaxCompute安全增强包新增支持的权限新功能。

**支持表列级别权限控制**

命令格式 `--`授予用户表的列权限

```
GRANT <privileges> ON TABLE <tablename>[(column_list)] TO USER <username>;
```

`--`撤销授予用户表的列权限

```
REVOKE <privileges> ON TABLE <tablename>[(column_list)] FROM USER <username>;
```

参数说明

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| privileges | 是 | 指定被授予的操作权限名称。单次授权可以指定多个操作。 当有多个操作时，多个操作名称之间使用英文逗号（,）分隔。 |
| tablename | 是 | 指定目标表或视图的名称。 您可以通过MaxCompute客户端执行 SHOW TABLES; 命令获取表名称。 |
| columnlist _ | 否 | 当需要授予目标表或视图中指定列的访问权限时，需要配置该参数。单次授权可以指定多个列名，列名之间用英文逗号（,）分隔。 |

| username | 是 | 指定用户或角色的名称。 您可以通过MaxCompute客户端执行 LIST USERS; 或 LIST ROLES; 命令获取用户账号或角色名称。 |
|---|---|---|

Policy通过condition可以从更多维度进行访问控制，例如时间段、来源IP、作业类型。但是ACL只能通过人、资源、操作三个维度进行控制。权限系统2.0为ACL授权增加了添加condition的功能，语法格式如下。

```
GRANT [privileges] ON <objectType> <objectName> TO [role|user] <name> privilegeproperties("conditions" = "acs:SourceIp in ('10.10.11.1/24','10.10.10.1/24') and acs:CurrentTime <= '2020-11-11T23:59:59Z'", "expires"="30");
```

| ACS保留条件关键字 | 类型 | 说明 |
|---|---|---|
| acs:CurrentTime | Date and time | Web Server接收到请求的时间，以ISO 8601格式表示，如2012-11-11T23:59:59Z。 |
| acs:SecureTransport | Boolean | 发送请求是否使用了安全信道，如HTTPS。 |
| acs:SourceIp | IP address | 发送请求时的客户端IP地址。 |
| acs:UserAgent | String | 发送请求时的客户端UserAgent。 |
| acs:Referer | String | 发送请求时的HTTP referer。 |

比较符的映射关系如下所示。

| 类型 | 比较符 | 映射关系 |
|---|---|---|
| String | StringEquals | = |
|  | StringNotEquals | <> |
|  | StringLike | like |
|  | StringNotLike | not like |
| Numeric | NumericEquals | = |
|  | NumericLessThan | < |
|  | NumericLessThanEquals | <= |
|  | NumericGreaterThan | > |
|  | NumericGreaterThanEquals | >= |
| Date and time | DateEquals | = |
|  | DateNotEquals | <> |
|  | DateLessThan | < |
|  | DateLessThanEquals | <= |
|  | DateGreaterThan | > |
|  | DateGreaterThanEquals | >= |
| Boolean | Bool直接写 true\|false | true\|false |

| IP address | IpAddress | in (...) |
|---|---|---|
|  | NotIpAddress | not in (...) |

**expires**：权限过期时间，以天为单位。 `"expires"="30"` 表示30天后过期。

**Policy支持GRANT方式授权**

#### 使用说明

`privilegeproperties` 中的 `{"policy" = "true"}` 部分表示当前授权作用到Policy上， {"allow"="[true|false]"} 部分表示本次授权的形式是白名单还是黑名单（对应Allow或者Deny）。 Revoke不支持condition，并且 `allow` 、 `objectname` 和 `rolename` 都能对应才能执行成功。 命令格式

```
GRANT <privileges> ON <objectType> <objectName> TO role <rolename> privilegeproperties("policy" = "true", "allow"="[true|false]", "con ditions"= "acs:SourceIp in ('10.10.10.10','10.10.10.10/4') and 'odps:InstanceId'='aaaaaa'"); REVOKE <privileges> ON <objectType> <objectName> FROM role <rolename> privilegeproperties ("policy" = "true", "allow"=" [true|false]");
```

参数说明

| 参数名称 |  | 是否必填 | 说明 |
|---|---|---|---|
| privileges |  | 是 | 指定被授予的操作权限名称。单次授权可以指定多个操作。 当有多个操作时，多个操作名称之间使用英文逗号（,）分隔。 |
| objecttype _ |  | 是 | 指定被授予的对象类型，即客体。单次授权只能指定一个客体。 |
| objectname _ |  | 是 | 指定被授予的对象的名称。 |
| rolename |  | 是 | 指定被授权的角色名称。单次授权只能指定一个角色。 您可以通过MaxCompute客户端执行 LIST ROLES; 命令获取角色名称。 |
| privilegeproperties | policy | 是 | 固定取值为true。表示使用Policy权限控制方案。 |
|  | allow | 白名单授权必填 | 指定白名单授权机制。取值范围如下： true：表示允许对指定对象执行指定操作。 false：表示不允许对指定对象执行指定操作，即黑名单。 |
|  | conditions | 否 | 从请求消息来源及访问方式等维度进行权限控制。详细参数取值请参见ACL授权支持condition及过期时间。 |

为了方便对通过Tunnel下载Table、Volume Partition的行为进行管控，权限模型新定义Download权限。通过Tunnel进行下载需要Download权限才可以下载Table 或Volume Partition。 使用限制开启Download权限控制需要具有Project Owner或者Super_Administrator角色权限的账号执行以下命令。 `--`开启`download`权限管控

```
setproject odps.security.enabledownloadprivilege=true;
```

`--`关闭`download`权限管控

```
setproject odps.security.enabledownloadprivilege=false;
```

只支持对Table、Volume资源进行Download鉴权。 命令格式

```
GRANT download ON <objectType> <objectName> TO [role|user] <name>;
```

参数说明

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| objecttype _ | 是 | 指定被授予的对象类型，即客体。单次授权只能指定一个客体。 |
| objectname _ | 是 | 指定被授予的对象的名称。 |

| name | 是 | 指定被授权的角色名称。单次授权只能指定一个角色。 您可以通过MaxCompute客户端执行 LIST ROLES; 命令获取角色名称。 |
|---|---|---|

**Package支持细粒度授权**

Package资源支持细粒度授权

```
GRANT <privileges> ON <objectType> <objectName> TO [USER/ROLE] <principalName> PRIVILEGEPROPERTIES ("refobject" = "true", "refproject "="<objectProject>", "package"="<projectName>.<packagname>"); GRANT <privileges> ON TABLE <tablename>[(column_list)] TO [USER/ROLE] <principalName> PRIVILEGEPROPERTIES ("refobject" = "true", "ref project"="<objectProject>", "package"="<projectName>.<packagname>"); SHOW GRANTS ON <objectType> <objectName> PRIVILEGEPROPERTIES ("refobject" = "true", "refproject"="<objectProject>", "package"="<pack agname>"); REVOKE <privileges> ON <objectType> <objectName> FROM [USER/ROLE] <principalName> PRIVILEGEPROPERTIES ("refobject" = "true", "refproj ect"="<objectProject>", "package"="<projectName>.<packagname>"); REVOKE <privileges> ON TABLE <tablename>[(column_list)] FROM [USER/ROLE] <principalName> PRIVILEGEPROPERTIES ("refobject" = "true", " refproject"="<objectProject>", "package"="<projectName>.<packagname>");
```

Package资源支持lable授权 Package资源lable授权

```
GRANT label <label> ON TABLE <objectName(columns,columns)> TO [USER/ROLE] <principalName>[WITH exp <hours>] PRIVILEGEPROPERTIES ("ref object" = "true", "refproject"="<objectProject>", "package"="<projectName>.<packagname>");
```

查看Package内资源Label授权

```xml
SHOW LABEL GRANTS ON <objectType> <objectName> PRIVILEGEPROPERTIES ("refobject" = "true", "refproject"="<objectProject>", "package"=" <projectName>.<packagname>");
```

撤销Package内资源Label授权

```
REVOKE label <label> ON TABLE <objectName(columns,columns)> FROM [USER/ROLE] <principalName> PRIVILEGEPROPERTIES ("refobject" = " true", "refproject"="<objectProject>", "package"="<projectName>.<packagname>");
```

参数说明

| 参数名称 |  | 是否必填 | 说明 |
|---|---|---|---|
| privileges |  | 是 | 指定被授予的操作权限名称。单次授权可以指定多个操作。 当有多个操作时，多个操作名称之间使用英文逗号（,）分隔。 |
| objecttype |  | 是 | 指定被授予的对象类型，即客体。单次授权只能指定一个客体。 |
| objectname |  | 是 | 指定被授予的对象的名称。 |
| principalName |  | 是 | 指定被授权的角色名称。单次授权只能指定一个角色。 您可以通过MaxCompute客户端执行 LIST ROLES; 命令获取角色名称。 |
| privilegeproperties | refobject | 是 | 固定取值为true。表示对安装的资源进行细粒度授权。 |
|  | Refproject | 是 | 资源所在的Project。 |
|  | projectName.packagna me | 否 | 明确指定只授予某个package的权限。如果未指定，系统会自动匹配一个。 |

**查询接口**

查询项目空间内用户的权限查询项目空间内资源的权限命令示例：

```
SHOW grants FOR ALIYUN$o***@aliyun.com;
```

返回结果客户端输出结果：

```
[roles] ##ALIYUN$o***@aliyun.com拥有的角色
```

`r1`

```
Authorization Type: ACL ##ALIYUN$o***@aliyun.com拥有的acl权限 [user/ALIYUN$o***@aliyun.com] A projects/new_priv_prj_1: All A projects/new_priv_prj_1/tables/test_1: All Authorization Type: Policy ##ALIYUN$o***@aliyun.com拥有的policy的权限 [role/r1]
```

`AC projects/new_priv_prj_1/tables/test2: Select ##`这里`AC`中的A表示`Allow`，如果出现D表示`Deny`，C表示本次授权带有`condition`

```
Authorization Type: ObjectCreator ##ALIYUN$o***@aliyun.com创建的表
```

`AG projects/new_priv_prj_1/tables/user_t: All ##`这里`AG`中的A表示`Allow`，G表示还有`grant`的权限 SDK输出的Json格式：

```json
{
    "ACL": {"user/ALIYUN$o***@aliyun.com": [{
                "Action": ["All"],
                "Effect": "",
                "Resource": ["acs:odps:*:projects/new_priv_prj_1/tables/test_1"]},
            {
                "Action": ["All"],
                "Effect": "",
                "Resource": ["projects/new_priv_prj_1"]}]},
    "POLICY": {"role/r1": [{
                "Action": ["odps:Select"],
                "Condition": {"IpAddress": {"acs:SourceIp": ["10.10.10.10",
                            "10.10.10.10/4"]}},
                "Effect": "Allow",
                "Resource": ["acs:odps:*:projects/new_priv_prj_1/tables/test2"]}]},
    "SuperPrivs": []
}
```

查询项目空间内共享资源的权限命令示例

```
SHOW grants FOR ALIYUN$o***@aliyun.com PRIVILEGEPROPERTIES ("refobject" = "true");
```

返回结果客户端输出结果

```
[roles] ##ALIYUN$o***@aliyun.com拥有的角色
```

`r1`

```
Authorization Type: InstalledObjecACL ##ALIYUN$o***@aliyun.com拥有的共享资源的权限 [pkg1_prj1_1] A projects/new_priv_prj_2/tables/prj2_tb1: Select
```

SDK输出的Json格式

```json
{
  "SharedObjectACL": {
    "pkg1_prj1_1": [
      {
        "Action": [
          "Select"
```

`],`

```json
        "Effect": "",
        "Resource": [
          "acs:odps:*:projects/new_priv_prj_2/tables/prj2_tb1"
```

]

```
      }
```

]

```
  }
}
```

查询项目空间内表的授权情况命令示例

```
SHOW grants ON TABLE test_1;
```

返回结果客户端输出结果 `Authorization Type: Implicit ##`用户身份是`projectOwner`或者是表`test_1`创建者的权限授予

```
AG project_owner/ALIYUN$o***@aliyun.com: All AG object_creator/ALIYUN$o***@aliyun.com: All
```

`Authorization Type: ACL ##test_1`通过`acl`授予给了哪些用户

```
A user/ALIYUN$o***@aliyun.com: All
```

SDK输出的Json格式

```json
{
  "ACL": {
    "": [
      {
        "Action": [
          "All"
```

`],`

```json
        "Effect": "",
        "Principal": [
          "user/ALIYUN$o***@aliyun.com"
```

]

```
      }
```

]

```
  }
}
```

查询通过Role Policy授予的情况命令示例

```
SHOW grants ON TABLE test2 PRIVILEGEPROPERTIES ("policy" = "true");
```

返回结果客户端输出结果

```
Authorization Type: Implicit AG project_owner/: All Authorization Type: Policy ##test_1在哪些role policy中有权限。 [role/r1]
```

SDK输出的Json格式

```json
{
  "POLICY": {
    "role/r1": [
      {
        "Action": [
          "odps:Select"
```

`],`

```json
        "Condition": {
          "IpAddress": {
            "acs:SourceIp": [
              "10.10.10.10",
              "10.10.10.10/4"
```

]

```json
          }
        },
        "Effect": "Allow",
        "Resource": [
          "acs:odps:*:projects/new_priv_prj_1/tables/test2"
```

]

```
      }
```

]

```
  }
}
```

查询Role授予给了哪些用户命令示例

```
SHOW principals r1;
```

返回结果客户端输出结果

```
ALIYUN$o***@aliyun.com
```

SDK输出的Json格式

```json
["ALIYUN$o***@aliyun.com"]
```

命令示例

```
SHOW grants ON TABLE prj2_tb1 PRIVILEGEPROPERTIES ("refobject" = "true", "refproject"="new_priv_prj_2");
```

返回结果客户端输出结果

```
Authorization Type: Implicit AG project_owner/: All Authorization Type: InstalledObjecACL [pkg1_prj1_1] A user/ALIYUN$o***@aliyun.com: Select
```

SDK输出的Json格式

```json
{
  "SharedObjectACL": {
    "pkg1_prj1_1": [
      {
        "Action": [
          "Select"
```

`],`

```json
        "Effect": "",
        "Principal": [
          "user/ALIYUN$o***@aliyun.com"
```

]

```
      }
```

]

```
  }
}
```

**SDK编程示例**

```java
public class OdpsSdk {
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Account account = new AliyunAccount("<accessId>", "<accessKey>");
        Odps odps = new Odps(account);
        String odpsUrl = "<url>";
        odps.setEndpoint(odpsUrl);
        odps.setDefaultProject("<project>");
         try {
            String out = odps.projects().get("<project>").getSecurityManager().runQuery("show grants for ALIYUN$o***@aliyun.com;", t
```

rue); //true表示输出`json`格式

```java
            System.out.print("out: " + out + "\n"); //success if return {}
        } catch (OdpsException e) {
```

`//`异常处理

```
        }
    }
}
```

#### 11.2.3. 存储加密

存储加密采用TDE（透明数据加密）技术，在数据写入Pangu集群时进行加密保护，而在业务层与MaxCompute交互时，数据处于未加密状态。主要对绕过 MaxCompute和云的安全认证与权限管理功能，直接拷贝Pangu集群上的静态数据造成数据泄露的场景进行防护。存储加密功能依赖于密钥管理服务（KMS）。您可通过本文了解数据加密机制和相关操作。

**数据加密机制**

MaxCompute通过KMS托管密钥，实现数据加密或解密功能。数据加密机制如下： MaxCompute以项目为单位，通过KMS加密或解密存储在MaxCompute的数据。 KMS生成和管理您的主密钥CMK（Customer Master Key），并保障密钥的安全性。 MaxCompute支持的加密算法为AES256、AESCTR、RC4和国密算法SM4。 MaxCompute支持通过默认密钥（DataWorks Default Key）和自带密钥（BYOK）加密或解密数据。 创建MaxCompute项目空间时，您可以选择密钥为Default Key，MaxCompute会在KMS上自动创建一个密钥作为CMK。 MaxCompute支持用户通过自带密钥（BYOK）加密或解密数据。即开通KMS，通过KMS创建用户特定的密钥，即自带密钥（BYOK），通过自带密钥（BYOK） 创建MaxCompute项目空间时，选择该密钥作为CMK进行加密或解密数据。 MaxCompute的数据加密为TDE透明加密，用户通过AK和身份认证方式登录MaxCompute，无感使用，进行全功能存储、计算等操作。可以防止未经认证的用户访问存储在Pangu和磁盘上的数据。 MaxCompute在盘古文件访问级别调用密钥，确保引擎每次对数据的操作都经过密钥加解密以提供保护，同时对KMS的访问并发进行了优化，通过缓存减少对KMS 和POP的压力。

**开启存储加密**

对于新的MaxCompute项目，您可通过创建项目时，配置安全增强开关信息中的加密选项开启存储加密，详情请参见创建项目。 对于已创建的MaxCompute项目，您可对存量数据进行重写，完成数据加密转换。详情请参见存量转加密方案。

**存量转加密方案**

存量项目开通加密后，您可以按需通过提交force merge task对存量数据进行重写，实现数据加密转换。操作如下：
1. 获取表及分区信息。
您可以通过Information Schema获取存量数据信息，其中Information Schema为准实时信息。

```
SELECT table_name, table_type, is_partitioned, is_archived FROM Information_Schema.tables;
```

`--`获取分区信息

```
SELECT table_schema, table_name, partition_name, is_archived FROM Information_Schema.PARTITIONS;
```

2. 执行加密转换。
您可对存量的普通表、分区表及Archive表数据进行重写，实现数据加密转换。代码如下：

**普通表重写**

```
SET odps.merge.restructure.action=hardlink; SET odps.merge.force.rewrite=true; SET odps.merge.maintain.order.flag=true; SET odps.sql.type.system.odps2=true; ALTER TABLE sql_encrypt_table MERGE SMALLFILES;
```

**分区表按照分区重写**

```
SET odps.merge.restructure.action=hardlink; SET odps.merge.force.rewrite=true; SET odps.merge.maintain.order.flag=true; SET odps.sql.type.system.odps2=true; ALTER TABLE partsrc PARTITION (pt='1') MERGE SMALLFILES;
```

**Archive表**

对于Archive表，需要增加以下参数：

```
SET odps.merge.force.archive.flag=true; SET odps.merge.archive.flag=true; SET odps.merge.restructure.action=hardlink; SET odps.merge.force.rewrite=true; SET odps.merge.maintain.order.flag=true; SET odps.sql.type.system.odps2=true; SET odps.merge.force.archive.flag=true; SET odps.merge.archive.flag=true; ALTER TABLE partsrc PARTITION (pt='1') MERGE SMALLFILES;
```

**影响**

对于merge重写操作的同时，存在其他任务数据写并发的场景，会保障写入动作生效，避免数据一致性问题，merge重写操作会报错。用户可以重新提交merge任务进行重写。 针对并发读场景，一般无影响，极端情况可能出现正在读取的任务，由于底层数据被重写且旧数据被回收，导致找不到数据的报错问题，用户可以重新提交数据读取任务。 重写加密数据后，部分数据可能会由于merge操作，导致存储占用发生变化，如果文件碎片较多，存储占用的变化可能更为显著。通常情况下，存储空间不会增加， 任何由于merge操作导致的文件大小变化对用户而言都是无感知的。 由于merge操作有文件大小的阈值限制，所以如果原本的文件非常大，经过merge处理后可能会被拆分成多个较小的文件。

**其他可选参数**

通过merge task可以进行文件合并重写，实现加密数据转换。使用方式如下：

```
ALTER TABLE tablename [PARTITION] MERGE SMALLFILES;
```

其他可选参数如下所示：

| 参数设置 | 描述 |
|---|---|

| SET odps.job.workers.limit = 1000 | 可用于限制作业内instance并发，控制资源使用。 |
|---|---|
| SET odps.merge.cross.paths=true\|false | 设置是否跨路径合并。 对于表中有多个分区的情况，合并过程会将多个分区生成独立的MergeAction进行合并，所以如果 odps.merge.cross.paths 设置为true，并不会改变路径个数，只是分别去合并每个路径下的小文件而已。 |
| SET odps.merge.maxmerged.filesize.threshold = 256 | 设置合并输出文件的大小。 如果输出文件大于该阈值，则创建新的输出文件，单位为MB。若不进行设置，则系统会采用全局变量 odps_g_max_merged_filesize_threshold 的默认值，默认值为256；若进行自定义设置， 则该值必须大于等于256。 |
| SET odps.merge.max.filenumber.per.instance = 10000 | 设置Fuxi Job的单个Instance允许合并的小文件个数，可以间接控制合并并行的Fuxi实例个数。 若不进行设置，则系统会采用全局变量 odps_g_merge_files_per_instance 的默认值，默认值为100；在一个Merge任务中，需要的Fuxi实例个数至少为该目录下面的总文件数除以该限制值。 |

### 智能元数据增强包

#### 11.3.1. 元数据支撑能力

元数据是描述数据的数据，元数据又分为技术元数据、业务元数据。本文为您介绍MaxCompute元数据相关内容。

**背景信息**

技术元数据为大数据平台为实现数据存储、计算、管理目的，使用的技术方案和组件产生的元数据，是面向技术实现细节的配置和说明。业务元数据是大数据平台描述数据意义、处理逻辑、价值目的的元数据，是用户访问大数据平台、数据仓库、数据处理时了解业务意义的基础。 MaxCompute记录了大数据平台中的技术元数据和业务元数据，因为MaxCompute是自主研发的大数据平台，且在阿里巴巴集团内部和大量项目中广泛使用，逐渐积累了比开源体系更详细的元数据。MaxCompute的元数据都存储在名为meta的Project中（元仓），包括例如项目、项目存储、表、列、udf、resource、项目安全配置、用户、角色、ACL、Policy、Package、Label等元数据和任务日志、Fuxi日志、Tunnel日志等原始基础信息。 用户和上层应用系统可以基于元仓数据做治理优化、安全审计、数据分析、容量评估等多种业务应用，例如： 开放给运维系统做水位监测，任务情况查询，小文件处理，以及表、任务、资源统计。 用于数据血缘管理，帮助用户数据建模，例如DataWorks的数据地图、数据服务等功能使用了智能元数据增强包的数据。 元仓保留所有用户执行任务记录，通过导出元仓数据，支持用户审计系统进行安全审计。 资源治理和容量评估，通过任务的数量、运行时间和资源消耗信息，配合大数据管家Quota分配情况，进行合理的资源划分和扩容估算。 作业优化，通过任务的运行和资源消耗信息，反馈给业务方进行业务上的优化。 MaxCompute元仓中的日志不包含业务层的信息，例如业务侧客户端类型和任务标识、业务层网络代理、业务用户信息等，MaxCompute只记录提

**说明**

交到大数据平台的网络最后一跳的IP信息、最终通过认证登录的账号信息。 Meta项目的说明请参见ODPS元仓说明。

#### 11.3.2. Information Schema

##### 11.3.2.1. Information Schema概述

本文介绍了MaxCompute元数据服务Information Schema的基本概念、操作使用及限制，方便您高效管理和监控项目元数据。

#### 使用说明

MaxCompute的Information Schema提供了项目元数据及使用历史数据等信息。在ANSI SQL-92的Information Schema基础上，添加了面向MaxCompute服务特有的字段及视图。MaxCompute提供了名称为Information Schema的公共项目，通过访问该公共项目提供的只读视图，可以查询到用户项目的元数据信息及使用历史信息。

**使用限制**

Information Schema提供的是当前项目的元数据视图，不支持跨项目的元数据访问。如果需要对多个项目的元数据进行统一查询、分析，需要分别获取各个项目中的元数据并整合在一起进行跨项目元数据分析。 专有云的元数据更新会有一定的延迟，根据资源和调度配置至少为 `T+1` 。 元数据及作业历史数据保存在Information Schema空间下，默认生命周期参见元数据视图列表，根据项目配置存储时长会有改变，如果需要对历史数据进行快照备使用Information Schema需要禁止SQL1.0回退，命令为 setodps.sql.planner.mode=lot; 。SQL编写如果有错，一些旧版本不禁止SQL1.0模式的话会回退为 1.0模式重新尝试，造成真实错误被掩盖和日志记录问题。 专有云Information Schema还在灰度发布中，部分字段因为引擎或框架原因，可能没有办法上报数据或数据不完整，产品在按照规划节奏修复或补齐，但因为有的问题原因涉及底层技术演进，完成时间暂不能保证完全满足项目中的需求。此外专有云从企业版3.12（不含）之前的版本升级上来的项目，不保证可以安装、使用专有云Information Schema灰度发布完成后，对于新创建的MaxCompute项目，MaxCompute默认提供Information Schema相关的元数据视图，您无需手工安

**说明**

默认行为是插件目录所有插件都会被安装，执行产出是要通过 `odps_config.ini plugins` 配置。 对于存量MaxCompute项目，在您开始使用Information Schema服务前，需要以项目所有者（Project Owner）或具备Super_Administrato管理角色的RAM用户身份安装Information Schema权限包，获得访问项目元数据的权限。安装方式如下：
1. 授权Package的项目操作。
Information Schema项目的有权限的角色或用户可以通过执行下面语句授权目标项目安装：

```
USE information_schema; allow project * TO install package systables;
```

2. 安装Package的项目操作。

```
install package Information_Schema.systables;
```

Package安装成功后，当前操作所在项目即获得了通过Information Schema查询本项目相关元数据的权限。
3. 查看Information Schema所提供的视图列表。

```
DESCRIBE package Information_Schema.systables;
```

查询结果如下图。

**查询元数据视图**

查询元数据视图时，需要在视图名称前指定项目Information Schema，即**Information Schema.view_name**。 例如，您登录访问的当前项目为myproject1，在myproject1中，执行如下命令查询当前myproject1中所有表的元数据信息。

```
odps@myproject1>SELECT * FROM Information_Schema.tables;
```

Information Schema同时也包含了作业历史视图，可以查询到当前项目内的作业历史信息。使用时可添加日期分区进行过滤，请参见如下命令。

```
odps@myproject1>SELECT * FROM Information_Schema.tasks_history WHERE ds='yyyymmdd' limit 100;
```

**访问授权**

Information Schema的视图包含了项目级别的所有用户数据，默认项目所有者可以查看。如果项目内其他用户或角色需要查看，需要进行授权。 授权语法如下。

```
GRANT <actions> ON package Information_Schema.systables TO USER <user_name>; GRANT <actions> ON package Information_Schema.systables TO role <role_name>;
```

参数说明如下。
**actions**：待授予的操作权限，取值为Read。
**user_name**：已添加至项目中的阿里云账号或RAM用户。
**role_name**：已添加至项目中的角色。
授权示例如下。

```
GRANT read ON package Information_Schema.systables TO USER RAM$Bob***@aliyun.com:user01;
```

##### 11.3.2.2. 元数据视图列表

MaxCompute的Information_Schema包含项目空间内关键对象的元数据信息，同时提供了作业运行、数据上传及数据下载的历史行为数据。

**说明**

元数据视图的查询方法请参见查询元数据视图。

#### 功能介绍

借助Information_Schema使用信息视图，您可以对作业的运行情况，例如资源消耗、运行时长、数据处理量等指标进行分析，用于优化作业或规划资源容量。 不同视图存在不同的时效性或系统默认的保留周期，超过保留周期的数据将无法访问。您可以手工从Information_Schema周期性导出数据到本地表中，备份更长周期的历史数据。

**说明**

导出数据时，建议显性地选择视图的字段名称，尽量避免使用 `insert into select * from information_schema.***` 的方式导出数据，防止新增字段后导致备份失败。

| 分类 | 视图 | 时效性/保留周期 | 延迟说明 |
|---|---|---|---|
| 元数据信息 | TABLES | 准实时视图 | 与在线数据存在一定延迟，延迟时间为3小时左右。 |
|  | PARTITIONS | 准实时视图 |  |
|  | COLUMNS | 准实时视图 |  |
|  | UDFS | 准实时视图 |  |
|  | RESOURCES | 准实时视图 |  |
|  | UDFRESOURCES _ | 准实时视图 |  |
|  | USERS | 准实时视图 |  |
|  | ROLES | 准实时视图 |  |
|  | USERROLES _ | 准实时视图 |  |
|  | PACKAGEOBJECTS _ | 准实时视图 |  |
|  | INSTALLEDPACKAGES _ | 准实时视图 |  |
|  | SCHEMAPRIVILEGES _ | 准实时视图 |  |
|  | TABLEPRIVILEGES _ | 准实时视图 |  |

|  | COLUMNPRIVILEGES _ | 准实时视图 |  |
|---|---|---|---|
|  | UDFPRIVILEGES _ | 准实时视图 |  |
|  | RESOURCEPRIVILEGES _ | 准实时视图 |  |
|  | TABLELABELS _ | 准实时视图 |  |
|  | COLUMNLABELS _ | 准实时视图 |  |
|  | TABLELABELGRANTS _ _ | 准实时视图 |  |
|  | COLUMNLABELGRANTS _ _ | 准实时视图 |  |
| 使用信息 | TASKSHISTORY _ | 准实时视图，分区表，保留最近14天明细 | 与在线数据存在一定延迟，延迟时间为15 分钟左右。 |
|  | TUNNELSHISTORY _ | 准实时视图，分区表，保留最近14天明细 |  |

项目空间下的表信息。

| 字段 | 类型 | 值 |
|---|---|---|
| tablecatalog _ | STRING | 固定值 odps 。 |
| tableschema _ | STRING | 项目空间名称。 |
| tablename _ | STRING | 表名。 |
| tabletype _ | STRING | 表类型。取值范围： MANAGEDTABLE _ VIRTUALVIEW _ EXTERNALTABLE _ |
| ispartitioned _ | BOOLEAN | 是否是分区表。 |
| ownerid _ | STRING | 表所有者的ID。 |
| ownername _ | STRING | 可选。表所有者的云账号名称。 |
| createtime _ | DATETIME | 表的创建时间。 |
| lastmodifiedtime _ _ | DATETIME | 表的最后更新时间 |
| datalength _ | BIGINT | 如果表为非分区表，值为表的数据量大小。如果表为分区表，系统不会计算表的数据量大小，值为NULL。 PARTITIONS视图中包含分区表各个分区的数据量大小。单位：字节（Byte）。 |
| tablecomment _ | STRING | 表的注释。 |
| lifecycle _ | BIGINT | 可选。生命周期。 |
| isarchived _ | BOOLEAN | 预留字段，无意义。 |
| tableexstoretype _ _ | STRING | 预留字段，无意义。 |
| clustertype _ | STRING | MaxCompute表的分桶（Clustering）类型。取值为 HASH或RANGE。 |

| numberbuckets _ | BIGINT | 可选字段，Cluster表的Bucket数目，0表示作业执行时动态决定。 |
|---|---|---|
| vieworiginaltext _ _ | STRING | VIRTUALVIEW类型表的view text。 _ |

**PARTITIONS**

项目空间下的表分区信息。

| 字段 | 类型 | 值 |
|---|---|---|
| tablecatalog _ | STRING | 固定值 odps 。 |
| tableschema _ | STRING | 项目名称。 |
| tablename _ | STRING | 表名。 |
| partitionname _ | STRING | 分区名。例如 ds='20190130' 。 |
| createtime _ | DATETIME | 分区的创建时间。 |
| lastmodifiedtime _ _ | DATETIME | 表的最后更新时间。 |
| datalength _ | BIGINT | 分区的数据量大小。单位：字节（Byte）。 |
| isarchived _ | BOOLEAN | 预留字段，无意义。 |
| isexstore _ | BOOLEAN | 预留字段，无意义。 |
| clustertype _ | STRING | 可选字段。MaxCompute表的分桶（Clustering）类型。 取值为HASH或RANGE。 |
| numberbuckets _ | BIGINT | 可选字段，Cluster表的Bucket数目。0表示作业执行时动态决定。 |

**COLUMNS**

描述项目空间下的表字段信息。

| 字段 | 类型 | 值 |
|---|---|---|
| tablecatalog _ | STRING | 固定值 odps 。 |
| tableschema _ | STRING | 项目名称。 |
| tablename _ | STRING | 表名。 |
| columnname _ | STRING | 列名。 |
| ordinalposition _ | BIGINT | 列序号。 |
| columndefault _ | STRING | 字段默认值。 |
| isnullable _ | BOOLEAN | 可选字段。始终为YES。 |
| datatype _ | STRING | 数据类型。 |
| columncomment _ | STRING | 列注释。 |
| ispartitionkey _ _ | BOOLEAN | 是否是分区键。 |

**UDFS**

项目空间下的UDF信息。

| 字段 | 类型 | 值 |
|---|---|---|
| udfcatalog _ | STRING | 固定值 odps 。 |
| udfschema _ | STRING | 项目名称。 |
| udfname _ | STRING | UDF名称。 |
| ownerid _ | STRING | UDF拥有者的ID。 |
| ownername _ | STRING | 可选字段，UDF拥有者的云账号名称。 |
| createtime _ | DATETIME | UDF的创建时间。 |
| lastmodifiedtime _ _ | DATETIME | UDF的最后修改时间。 |

**RESOURCES**

项目空间下的资源信息。

| 字段 | 类型 | 值 |
|---|---|---|
| resourcecatalog _ | STRING | 固定值 odps 。 |
| resourceschema _ | STRING | 项目的名称。 |
| resourcename _ | STRING | 资源名。 |
| resourcetype _ | STRING | 资源类型。取值为Py或Jar。 |
| ownerid _ | STRING | 资源所有者的ID。 |
| ownername _ | STRING | 可选字段，资源所有者的云账号名称。 |
| createtime _ | DATETIME | 资源的创建时间。 |
| lastmodifiedtime _ _ | DATETIME | 资源的最后修改时间。 |
| size | BIGINT | 资源占用的存储空间。 |
| comment | STRING | 资源的注释。 |
| istempresource _ _ | BOOLEAN | 是否是临时资源。 |

**UDF_RESOURCES**

项目空间下UDF的资源依赖。

| 字段 | 类型 | 值 |
|---|---|---|
| udfcatalog _ | STRING | 固定值 odps 。 |
| udfschema _ | STRING | 项目名称。 |
| udfname _ | STRING | UDF名称。 |
| resourceschema _ | STRING | 资源所在的项目。 |
| resourcename _ | STRING | 资源名。 |

**USERS**

项目空间下的用户列表。

| 字段 | 类型 | 值 |
|---|---|---|
| usercatalog _ | STRING | 取值为ALIYUN或RAM。 |
| userschema _ | STRING | 项目名称。 |
| username _ | STRING | 可选字段，用户名。 |
| userid _ | STRING | 用户ID。 |
| userlabel _ | STRING | 用户标签。 |

**ROLES**

项目空间下的角色列表。

| 字段 | 类型 | 值 |
|---|---|---|
| rolecatalog _ | STRING | 固定值 odps 。 |
| roleschema _ | STRING | 项目名称。 |
| rolename _ | STRING | 角色名。 |
| rolelabel _ | STRING | 角色标签。 |
| comment | STRING | 角色的注释。 |

**USER_ROLES**

项目空间下用户拥有的角色信息。

| 字段 | 类型 | 值 |
|---|---|---|
| userrolecatalog _ _ | STRING | 固定值 odps 。 |
| userroleschema _ _ | STRING | 项目名称。 |
| rolename _ | STRING | 角色名。 |
| username _ | STRING | 用户名。 |
| userid _ | STRING | 用户的ID。 |

**PACKAGE_OBJECTS**

项目空间下Package中的对象信息。

| 字段 | 类型 | 值 |
|---|---|---|
| packagecatalog _ | STRING | 固定值 odps 。 |
| packageschema _ | STRING | 项目名称。 |
| packagename _ | STRING | Package名称。 |
| objecttype _ | STRING | Package内成员的类型。 |
| objectname _ | STRING | Package内成员的名字。 |
| columnname _ | STRING | 表的列名。 |

| allowedprivileges _ | VECTOR<STRING> | 共享的权限。 |
|---|---|---|
| allowedlabel _ | STRING | 共享的标签。 |

**INSTALLED_PACKAGES**

项目空间下已安装的Package信息。

| 字段 | 类型 | 值 |
|---|---|---|
| installedpackagecatalog _ _ | STRING | 固定值 odps 。 |
| installedpackageschema _ _ | STRING | 项目名称。 |
| packageproject _ | STRING | 创建Package的项目空间名称。 |
| packagename _ | STRING | Package名称。 |
| installedtime _ | DATETIME | 安装时间（预留字段）。 |
| allowedlabel _ | STRING | 共享的标签。 |

**SCHEMA_PRIVILEGES**

项目空间下SCHEMA的权限信息。

| 字段 | 类型 | 值 |
|---|---|---|
| usercatalog _ | STRING | 固定值 odps 。 |
| userschema _ | STRING | 项目名称。 |
| grantee | STRING | 用户名。 |
| userid _ | STRING | 账户ID。 |
| grantor | STRING | 授权者账号，当前值为NULL。 |
| privilegetype _ | STRING | 权限类型。 |

**TABLE_PRIVILEGES**

项目空间下表的权限信息。

| 字段 | 类型 | 值 |
|---|---|---|
| tablecatalog _ | STRING | 固定值 odps 。 |
| tableschema _ | STRING | 表所在的项目名称。 |
| tablename _ | STRING | 表名。 |
| grantee | STRING | 用户名。 |
| userid _ | STRING | 账户ID。 |
| grantor | STRING | 授权者账号，当前值为NULL。 |
| privilegetype _ | STRING | 权限类型。 |
| userschema _ | STRING | 用户所在的项目名称。 |

**COLUMN_PRIVILEGES**

项目空间下表字段级的权限信息。

| 字段 | 类型 | 值 |
|---|---|---|
| tablecatalog _ | STRING | 固定值 odps 。 |
| tableschema _ | STRING | 表所在的项目名称。 |
| tablename _ | STRING | 表名。 |
| columnname _ | STRING | 列名。 |
| grantee | STRING | 用户名。 |
| userid _ | STRING | 账户ID。 |
| grantor | STRING | 可选字段。目前为NULL。 |
| privilegetype _ | STRING | 权限类型。 |
| userschema _ | STRING | 用户所在的项目名称。 |

**UDF_PRIVILEGES**

项目空间下UDF的权限信息。

| 字段 | 类型 | 值 |
|---|---|---|
| udfcatalog _ | STRING | 固定值 odps 。 |
| udfschema _ | STRING | 项目名称。 |
| udfname _ | STRING | UDF名称。 |
| userschema _ | STRING | 用户所在的项目名称。 |
| grantee | STRING | 用户名。 |
| userid _ | STRING | 账户ID。 |
| grantor | STRING | 授权者账号，当前值为NULL。 |
| privilegetype _ | STRING | 权限类型。 |

**RESOURCE_PRIVILEGES**

项目空间下资源的权限信息。

| 字段 | 类型 | 值 |
|---|---|---|
| resourcecatalog _ | STRING | 固定值 odps 。 |
| resourceschema _ | STRING | 项目名称。 |
| resourcename _ | STRING | 资源名称。 |
| userschema _ | STRING | 用户所在项目空间。 |
| grantee | STRING | 用户名。 |
| userid _ | STRING | 账户ID。 |

| grantor | STRING | 授权者账号，当前值为NULL。 |
|---|---|---|
| privilegetype _ | STRING | 权限类型。 |

**TABLE_LABELS**

项目空间下表的LABEL信息。

| 字段 | 类型 | 值 |
|---|---|---|
| tablecatalog _ | STRING | 固定值 odps 。 |
| tableschema _ | STRING | 项目名称。 |
| tablename _ | STRING | 表名。 |
| labeltype _ | STRING | 标签类型（始终为NULL）。 |
| labellevel _ | STRING | 标签等级。 |

**COLUMN_LABELS**

项目空间下表字段级的LABEL信息。

| 字段 | 类型 | 值 |
|---|---|---|
| tablecatalog _ | STRING | 固定值 odps 。 |
| tableschema _ | STRING | 项目名称。 |
| tablename _ | STRING | 表名。 |
| columnname _ | STRING | 字段名。 |
| labeltype _ | STRING | 标签类型（始终为NULL）。 |
| labellevel _ | STRING | 标签等级。 |

**TABLE_LABEL_GRANTS**

项目空间下表的LABEL授权信息。

| 字段 | 类型 | 值 |
|---|---|---|
| tablelabelgrantcatalog _ _ _ | STRING | 固定值 odps 。 |
| tablelabelgrantschema _ _ _ | STRING | 用户所在的项目名称。 |
| user | STRING | 用户名称。 |
| userid _ | STRING | 用户的ID。 |
| tableschema _ | STRING | 表所在的项目名称。 |
| tablename _ | STRING | 表名。 |
| grantor | STRING | 授权者账号，当前值为NULL。 |
| labellevel _ | STRING | 授予的标签等级。 |
| expired | DATETIME | 过期时间。 |

**COLUMN_LABEL_GRANTS**

项目空间下表字段的LABEL授权信息。

| 字段 | 类型 | 值 |
|---|---|---|
| columnlabelgrantcatalog _ _ _ | STRING | 固定值 odps 。 |
| columnlabelgrantschema _ _ _ | STRING | 用户所在项目名称。 |
| user | STRING | 用户名称。 |
| userid _ | STRING | 用户的ID。 |
| tableschema _ | STRING | 表所在的项目名称。 |
| tablename _ | STRING | 表名。 |
| columnname _ | STRING | 字段名。 |
| grantor | STRING | 授权者账号，当前值为NULL。 |
| labellevel _ | STRING | 授予的标签等级。 |
| expired | DATETIME | 过期时间。 |

**TASKS**

作业实时快照，用于实时监控作业。

| 字段 | 类型 | 值 |
|---|---|---|
| projectname _ | STRING | 项目名称。 |
| taskname _ | STRING | 作业名称。 |
| tasktype _ | STRING | 作业类型。 作业类型取值如下： SQL：SQL作业 CUPID：Spark作业 SQLCost：SQL预估作业 SQLRT：查询加速SQL作业 LOT：MapReduce作业 PS：PAI的Parameter Server AlgoTask：机器学习作业 |
| instid _ | STRING | 实例ID。 |
| status | STRING | 数据采集瞬间的运行状态，取值为Running或Waiting。 |
| ownerid _ | STRING | 作业提交人云账号ID。 |
| ownername _ | STRING | 作业提交人云账号名称。 |
| starttime _ | DATETIME | 作业启动时间。 |
| priority | BIGINT | 作业优先级，仅支持采用包年包月资源的作业。 |
| signature | STRING | 作业签名。 |
| queuename _ | STRING | 计算队列名称。 |
| cpuusage _ | BIGINT | 当前CPU用量，值为core×100。 |

| memusage _ | BIGINT | 当前内存用量，单位为MB。 |
|---|---|---|
| gpuusage _ | BIGINT | 当前GPU用量，值为卡×100。 |
| totalcpuusage _ _ | BIGINT | 累计CPU用量，值为core×100×s。 |
| totalmemusage _ _ | BIGINT | 累计内存用量，值为MB×s。 |
| totalgpuusage _ _ | BIGINT | 累计GPU用量，值为卡×100×s。 |
| cpuminratio _ _ | BIGINT | 作业当前CPU用量占用队列保障水位比例，仅支持采用包年包月资源的作业。 |
| memminratio _ _ | BIGINT | 作业当前内存用量占用队列保障水位比例，仅支持采用包年包月资源的作业。 |
| gpuminratio _ _ | BIGINT | 作业当前GPU用量占用队列保障水位比例，仅支持采用包年包月资源的作业。 |
| cpumaxratio _ _ | BIGINT | 作业当前CPU用量占用队列最高弹性水位比例，仅支持采用包年包月资源的作业。 |
| memmaxratio _ _ | BIGINT | 作业当前内存用量占用队列最高弹性水位比例，仅支持采用包年包月资源的作业。 |
| gpumaxratio _ _ | BIGINT | 作业当前GPU用量占用队列最高弹性水位比例，仅支持采用包年包月资源的作业。 |
| settings | STRING | DataWorks等上层自定义调度设置。 |
| additionalinfo _ | STRING | 附加信息，保留字段。 |

**TASKS_HISTORY**

MaxCompute项目内已完成的作业历史，保留近14天数据。

| 字段 | 类型 | 值 |
|---|---|---|
| taskcatalog _ | STRING | 固定值 odps 。 |
| taskschema _ | STRING | 项目名称。 |
| taskname _ | STRING | 作业名称。 |
| tasktype _ | STRING | 作业类型。 作业类型取值如下： SQL：SQL作业 CUPID：Spark作业 SQLCost：SQL预估作业 SQLRT：查询加速SQL作业 LOT：MapReduce作业 PS：PAI的Parameter Server AlgoTask：机器学习作业 |
| instid _ | STRING | 实例ID。 |
| status | STRING | 数据采集瞬间的运行状态（非实时状态）。 |
| ownerid _ | STRING | 账户ID。 |
| ownername _ | STRING | 云账户名称。 |
| result | STRING | 仅在SQL作业出错时有值，提供报错信息。 |

| starttime _ | DATETIME | 作业启动时间。 |
|---|---|---|
| endtime _ | DATETIME | 作业结束时间（当天未结束为NULL）。 |
| inputrecords _ | BIGINT | 作业读取的records数目。 |
| outputrecords _ | BIGINT | 作业输出的records数目。 |
| inputbytes _ | BIGINT | 实际扫描的数据量，与Logview相同。 |
| outputbytes _ | BIGINT | 输出字节数。 |
| inputtables _ | STRING | [project.table1, project.table2]格式的作业输入表。 |
| outputtables _ | STRING | [project.table1, project.table2]格式的作业输出表。 |
| operationtext _ | STRING | 查询语句的sourcexml（sourcexml超过256 KB时置为 _ _ NULL）。 |
| signature | STRING | 可选字段。作业签名。 |
| complexity | DOUBLE | 可选字段，作业复杂度。仅SQL作业有此字段。 |
| costcpu _ | DOUBLE | 作业CPU消耗（100表示1 core×s。例如：10 core运行 5s，costcpu为10×100×5=5000）。 _ |
| costmem _ | DOUBLE | 作业内存消耗（MB×s）。 |
| settings | STRING | 上层调度或用户传入的信息，以JSON格式存储。包含字段：USERAGENT、BIZID、SKYNETID和 _ SKYNETNODENAME。 _ |
| ds | STRING | 数据采集日期。例如20190101。 |

**TUNNELS_HISTORY**

数据通道批量上传下载的历史数据，保留近14天数据。

| 字段 | 类型 |  | 值 |  |
|---|---|---|---|---|
| tunnelcatalog _ | STRING |  | 固定值 odps 。 |  |
| tunnelschema _ | STRING |  | 项目名称。 |  |
| sessionid _ | STRING |  | 会话ID，格式为 TIMESTAMP（YYYYMMDDHHmmss，14 |  |
|  |  |  |  | TIMESTAMP（YYYYMMDDHHmmss，14 |
|  |  |  | 字符）+ ip（8字符）+ numHex（8字符） |  |
| operatetype _ | STRING |  | 操作类型。取值范围： UPLOADLOG DOWNLOADLOG DOWNLOADINSTANCELOG |  |
| tunneltype _ | STRING |  | 通道类型。取值为TUNNEL LOG或TUNNEL INSTANCE LOG。 |  |
| requestid _ | STRING |  | 请求ID。 |  |
| objecttype _ | STRING |  | 操作对象类型。取值为TABLE或INSTANCE。 |  |
| objectname _ | STRING |  | 表名称或实例ID。 |  |

| partitionspec _ | STRING | 分区信息。例如 time=20130222，loc=beijing 。 |
|---|---|---|
| datasize _ | BIGINT | 数据的字节数，单位：字节（Byte）。 |
| blockid _ | BIGINT | Tunnel上传的Block编号。当操作类型是UPLOADLOG时有效，否则为空。 |
| offset | BIGINT | 下载的起始偏移位置，表示从第几条记录开始（起始是 0）。 |
| length | BIGINT | 即recordcount，本次下载或上传的记录数（下载的记录 _ 数为用户指定的length值）。 |
| ownerid _ | STRING | 云账户ID。 |
| ownername _ | STRING | 云账户名称。 |
| starttime _ | DATETIME | 请求开始时间。 |
| endtime _ | DATETIME | 请求结束时间。 |
| clientip _ | STRING | 发起Tunnel请求的客户端IP地址。 |
| useragent _ | STRING | User Agent，发起Tunnel请求的客户端的相关信息。例如Java版本、操作系统。 |
| columns | STRING | Tunnel下载数据时指定列的集合。 |
| ds | STRING | 数据采集日期。例如20190101。 |

##### 11.3.2.3. Information Schema常见问题

**通过数据源数据增量同步后，如何查看某一条数据具体被同步到MaxCompute中的时间？**

不支持查看某一条数据具体被同步到MaxCompute中的时间。可以看表元数据的LastModifiedTime时间。详情请参见Information Schema概述。

**information_schema.tables中没有查到MaxCompute项目下所有的表，应该如何解决？**

MaxCompute元数据更新会有一定的延迟，至少3个小时。您需要确认建表时间，等待3个小时后重新查看。

### 智能存储增强包

#### 11.4.1. 归档模式支持

MaxCompute新增支持纠删码，可以在很小的性能损耗情况下，大大减少存储成本，适合冷数据归档。本文为您介绍如何在MaxCompute中使用基于纠删码的归档模式。

**背景信息**

纠删码和多副本策略是存储领域常见的两种数据冗余技术。 纠删码（erasure coding，EC）技术主要是将数据分割成片段，经过纠删码算法将原始的数据进行编码获得冗余，并将数据和冗余存储在不一样的位置，以达到容错的目的。其基本思想是将n块原始的数据元素经过计算，获得m块冗余元素（校验块），MaxCompute底层Pangu采用8块原始的数据元素。对于这 `n+m` 块的元素，当其中任意的m块元素出错（包括原始数据和冗余数据）时，都可以经过对应的重构算法恢复出原来的n块数据。生成校验的过程被称为编码（encoding），恢复丢失数据块的过程被称为解码（decoding）。 多副本策略即将数据存储多个副本（通常是三副本），当某个副本丢失时，能够经其余副本复制回来。三副本允许坏的副本数： `2/3` ；纠删码允许坏的副本数： `3/11` 。三副本的冗余度： `3/1` ；纠删码的冗余度： `(3+8)/8` 。 纠删码优点：基于纠删码的方法与多副本方法相比具备冗余度低、磁盘利用率高等优势。额外负担：只要有一个坏块就得通过网络读出n倍的数据并重新计算的计算负荷，以及读取数据造成的数倍的网络负载。坏块原因包括磁盘、存储服务、读取故障等各种原因。读取数据越多，可能出现坏块并重新计算的概率越大，因此对EC数据频繁的读写会造成额外的性能损耗。 按照内部测试经验值统计，对采用了EC模式存储的Archive表读取，CPU负载损耗为5%~20%，假定集群中90%的表是Archive表，又假定读数据占集群计算所有消耗的10%，所以开启EC后，集群负载整体的额外消耗，约占任务总消耗的2%。如果只是历史数据低频查询，IO不紧张的情况下EC对性能几乎没有影响。功能上可以按分区粒度灵活配置存储策略，可选择三副本（3倍冗余）或EC纠删码（1.375倍冗余）存储方式，两种模式可同时使用于同一集群，请按需配置。

**注意事项**

归档对业务的影响主要有以下几个方面： Pangu Raid文件相对普通文件读性能有一定程度损失，所以应该尽量减少业务直接读Raid文件，降低归档对业务的影响。 归档消耗一定的计算资源，可以用于归档的资源有限。所以生命周期较短的数据不应该归档。 数据丢失后恢复时间较长，恢复代价较大，特别是数据块丢失由校验块恢复过程中不可读。因此在做EC归档时请仔细评估。 EC模式下，至少需要12台服务器。

**归档使用方法**

通过命令方式将基于三副本的表迁移到EC模式上或者将表的属性改为EC模式。 MaxCompute默认采用3副本策略，可以通过归档（Archive）的方式将数据转化为EC模式降低数据存储成本。MaxCompute归档表的压缩算法采用了压缩率更高的 Bzip2算法，存储空间可以节省70%以上。MaxCompute提供了两种数据归档方式： 存量数据归档。 使用以下命令将表、分区存量数据转化为归档模式。

```
ALTER TABLE <table_name> [PARTITION (pt_spec)] ARCHIVE;
```

示例如下： `--`归档`ds`为`20170101`的数据

```
ALTER TABLE my_log PARTITION(ds='20170101') archive;
```

新增数据直接归档。

| 使用以下命令将表打标为 | archive | ，对应表新增数据自动保存为归档模式。 |
|---|---|---|
| ALTER TABLE <table_name> SET TBLPROPERTIES("storagestrategy"="archive"); |  |  |

**合并小文件**

在Reduce计算过程或实时Tunnel数据采集过程中，会产生大量小文件，小文件过多会带来以下问题： 小文件越多，单个Instance可以处理的文件数有限制，所以需要Instance资源也越多。因此造成的资源浪费会影响整体的执行性能。 过多的小文件给文件系统带来压力，并且影响磁盘空间的利用率。 目前提供两种可供选择的小文件合并的方法，ALTER合并模式和SQL合并模式： ALTER合并模式通过Console命令行进行合并，命令格式如下。

```
ALTER TABLE tablename [PARTITION] MERGE SMALLFILES;
```

SQL合并模式是在执行SQL结束之后，通过设置控制参数 odps.task.merge.enabled=true; ，进行是否需要小文件合并的判断，如果需要小文件合并，则另外启动Fuxi Job进行小文件合并。

#### 11.4.2. 备份恢复

在数据开发过程中，避免不了会出现误操作删除数据后需要恢复，或使用 `insert into` 、 `insert overwrite` 语法执行后发现数据有问题需要恢复到历史版本的情况。本文为您介绍如何在MaxCompute上实现数据备份恢复。

**开启备份恢复功能**

**前提条件**

| 您可以执行命令 | DESC project <projectname>; |  |
|---|---|---|
| setproject odps.changelogs.ttl=0; |  | 关闭cha |

**开启备份恢复功能**

关闭changelog功能后，MaxCompute数据备份恢复功能默认开启，可恢复周期为1天。Project Owner或拥有Super_Administrator角色的RAM账号可以通过如下命令修改可恢复周期天数。

```
setproject odps.timemachine.retention.days=days;
```

**days**为数据备份天数，即备份数据版本的保留天数。在此期间您可以将当前版本恢复成任意备份中的数据版本。取值范围为0~7，0代表关闭此功能。

**备份恢复功能相关命令**

开启备份恢复功能后，您可以查看表或分区的备份版本信息，也支持将表或分区恢复至某个数据版本，具体操作及命令如下： 查看命令

| 命令 | 说明 |
|---|---|
| SHOW history FOR tables; | 查看当前表和备份中的表。 说明执行该命令需要具备Project的List权限。 |
| SHOW history FOR TABLE table_name; | 查看指定表的备份信息。 说明如果表还存在，则需要具备表的ShowHistory权限；如果表不存在，则需要具备 Project的List权限。 |

| SHOW history FOR TABLE table_name ('id'='xxxx'); | 查看已删除表的备份信息。 |
|---|---|
| SHOW history FOR TABLE table_name PARTITION(pt='xxx'); | 查看指定分区的备份信息。 |
| SHOW history FOR TABLE table_name PARTITION('id'='xxxx'); | 查看已删除分区的备份信息。 |

恢复表命令

| 命令 | 说明 |
|---|---|
| restore TABLE table_name ('id'='xxxxx'); | 恢复已经删除的表。 |
| restore TABLE table_name TO LSN 'xxxx'; | 恢复表到指定版本。 |
| restore TABLE table_name TO LSN 'xxxx' AS new_table_name; | 恢复表到指定版本且生成新的表。 |

**说明**

如果表还存在，则需要具备表的Update权限；如果表不存在，则需要具备Project的CreateTable权限。 恢复分区命令

| 命令 | 说明 |
|---|---|
| restore TABLE table_name PARTITION('id'='xxxx'); | 恢复删除的分区，支持同时恢复多个分区。 |
| restore TABLE table_name PARTITION(pt='xxxx')[ PARTITION(pt='xxxx') ] TO LSN 'xxxx'; | 恢复分区到指定版本，支持同时恢复多个分区。 |
| restore TABLE table_name PARTITION(pt='xxx')[ PARTITION(pt='xxx') ] TO LSN 'xxxx' AS new_table_name; | 恢复分区到指定版本且生成新的表，支持同时恢复多个分区。 |

| 说明恢复分区命令中，只能指定一个LSN版本。当一次性执行恢复多分区操作时，会分别把每个分区恢复为指定LSN或往前第一个点对应的版本。例如pt1的LSN版本分别为100、102、104、106，pt2的LSN版本分别为101、103、104、105，执行 restore table table_name PARTITION(pt='1') PARTITION(pt='2') to LSN '102'; 命令，则最终pt1恢复为102版本，pt2恢复为101版本。 |  |  |
|---|---|---|
|  | restore table table_name PARTITION(pt='1') |  |

**使用示例**

假设已存在如下三张表： orders：非分区表 orders_delta：非分区表 orders_pt：分区表

**示例1：非分区表删除后恢复**

1. 删除非分区表orders，命令示例如下。

```
DROP TABLE orders; Confirm to "drop table orders" (yes/no)? yes
```

`OK`
2. 查看orders表的备份信息，获取id，命令示例如下。

```
SHOW history FOR tables;
```

3. 查看已删除表orders的备份信息，命令示例如下。

```
SHOW history FOR TABLE orders ('id'='25899d487db04852a7f4331491f8****');
```

4. 恢复已经删除的表orders，命令示例如下。

```
restore TABLE orders ('id'='25899d487db04852a7f4331491f8****');
```

**示例2：非分区表数据更新后恢复**

1. 更新非分区表orders的数据，命令示例如下。
`--`更新表数据，也可以是`insert overwrite`操作。

```
INSERT INTO orders SELECT * FROM orders_delta;
```

`OK` `--`或者执行如下操作。

```
TRUNCATE TABLE orders;
```

`OK`
2. 查看非分区表orders的备份信息，获取LSN，命令示例如下。

```
SHOW history FOR TABLE orders;
```

3. 恢复非分区表orders的数据，命令示例如下。
`--`从最新版本恢复到`truncate`之前版本且生成新表。

```
restore TABLE orders TO LSN 'lsn_no' AS orders_restore;
```

**说明**

执行前，请将参数 `lsn_no` 替换为步骤2中获取的实际LSN值。

**示例3：分区删除后恢复**

1. 删除分区表orders_pt的分区，命令示例如下。

```
ALTER TABLE orders_pt DROP IF EXISTS PARTITION(pt='1998-08-02');
```

2. 查看表分区表orders_pt的备份信息，获取分区id，命令示例如下。

```
SHOW history FOR TABLE orders_pt;
```

3. 恢复删除的分区，命令示例如下。

```
restore TABLE orders_pt PARTITION('id'='88ba032fb9524a75b1daddb3e29b****');
```

**示例4：分区数据更新后恢复**

1. 更新分区表orders_pt的数据，命令示例如下。

```
INSERT INTO orders_pt PARTITION(pt='1999-01-01') SELECT * FROM orders;
```

`OK`

```
INSERT OVERWRITE orders_pt PARTITION(pt='1999-01-02') SELECT * FROM orders;
```

`OK`
2. 查看表或分区备份信息，获取LSN，命令示例如下。
`--`查看表备份信息，包含所有分区。

```
SHOW history FOR TABLE orders_pt;
```

`--`查看单个分区备份信息。

```
SHOW history FOR TABLE orders_pt PARTITION(pt='1999-01-01'); SHOW history FOR TABLE orders_pt PARTITION(pt='1999-01-02');
```

3. 恢复分区数据，命令示例如下。
`--`恢复分区到指定版本。

```
restore TABLE orders_pt PARTITION(pt='1999-01-01') PARTITION(pt='1999-01-02') TO LSN '0000000000000026';
```

`--`恢复分区到指定版本并生成新的表。

```
restore TABLE orders_pt PARTITION(pt='1999-01-01') PARTITION(pt='1999-01-02') TO LSN '0000000000000026' AS orders_pt_restore;
```

**示例5：分区表删除后恢复**

1. 删除分区表orders_pt，命令示例如下。

```
DROP TABLE orders_pt;
```

2. 查看分区表orders_pt的备份信息，获取orders_pt表的id，命令示例如下。

```
SHOW history FOR tables;
```

3. 恢复分区表orders_pt，命令示例如下。

```
restore TABLE orders_pt('id'='a26c91705f53483493474d7f28c1****');
```

#### 11.4.3. VolumeFS（Volume2）

MaxCompute是基于大数据技术、提供数据仓库使用方式的大数据平台，为了满足客户希望数据仓库同样可以存储非结构化数据、开放文件系统的需求，MaxCompute提供了VolumeFS（Volume2）的分布式文件系统存储服务能力，用户可以在当前用户的权限和管理体系下，使用数仓提供的文件系统，进行数据读写，并对接引擎进行数据应用。本文为您介绍如何在MaxCompute上使用VolumeFS。

**前期准备**

请联系系统管理员开通VolumeFS功能。 需要项目将**允许****volume File**和**ALLOWED_VOLUME2**参数值选择为 `true` 。 单击客户端，下载VolumeFS客户端。 单击VolumeFs相关库，下载VolumeFs相关库。

**配置VolumeFs-HDFS客户端**

| 下载并解压客户端后，需要使用如下命令配置 | HADOOP_HOME | 环境变量： |
|---|---|---|
| # 添加以下代码到 .bashrc \ .bash_profile export HADOOP_HOME=/path/to/hadoop-2.7.1/ |  |  |

**说明**

请以您客户端实际路径替换上述代码中的路径，后面路径都将以**HADOOP_HOME**环境变量指代。
2. 编辑 $HADOOP_HOME/etc/hadoop/hadoop-env.sh 文件。
i. 创建相关目录。

```
mkdir -p $HADOOP_HOME/share/hadoop/odps
```

ii. 解压VolumeFs相关库到创建的目录。

```
tar xf /path/to/lib.tar.gz -C $HADOOP_HOME/share/hadoop/odps
```

| 添加以下代码到 | $HADOOP_HOME/etc/hadoop/hadoop-env.sh | 文件中。 |
|---|---|---|
| export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$HADOOP_HOME/share/hadoop/odps/lib/* |  |  |

| $HADOOP_HOME/etc/hadoop/core-site.xml |  |  |
|---|---|---|
| TBD | 部分以及默认项目空间 | projectName |

```xml
<configuration>
    <property>
        <name>fs.odps.impl</name>
        <value>com.aliyun.odps.fs.VolumeFileSystem</value>
    </property>
    <property>
        <name>fs.AbstractFileSystem.odps.impl</name>
        <value>com.aliyun.odps.fs.VolumeFs</value>
    </property>
    <property>
        <name>io.file.buffer.size</name>
        <value>512000</value>
    </property>
    <property>
        <name>volume.internal</name>
        <value>false</value>
    </property>
    <property>
        <name>pangu.access.check</name>
        <value>false</value>
    </property>
    <property>
        <name>odps.access.id</name>
        <value>TBD</value>
    </property>
    <property>
        <name>odps.access.key</name>
        <value>TBD</value>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>odps://<projectName>/</value>
    </property>
    <property>
        <name>odps.service.endpoint</name>
        <value>TBD</value>
    </property>
</configuration>
```

| $HADOOP_HOME/bin/hdfs dfs -help |  |  | 命令测试。 |
|---|---|---|---|
| VA HOME未设置，在 _ | .bashrc | 中添加 | export JAVA_HOME=/usr/ali/java |

如果返回如下内容，说明此时客户端已配置完毕： 可以运行如下命令： `//` 创建一个`volume`，`volume`必须在对应的`project`下面，`volume1`为`volume`名称

```
bin/hdfs dfs -mkdir odps://odps_smoke_test/volume25/
```

`//` 创建`volume`下的一个文件夹

```
bin/hdfs dfs -mkdir odps://odps_smoke_test/volume25/test/
```

`//` 上传文件

```
bin/hdfs dfs -put ~/abcd odps://odps_smoke_test/volume25/test/
```

`//` 查看文件

```
bin/hdfs dfs -cat odps://odps_smoke_test/volume25/test/abcd
```

**基于Volume2使用Parquet+Snappy压缩示例**

```
SET odps.ext.parquet.native=false; CREATE EXTERNAL TABLE liantong_v1(
  service_type string COMMENT'xx',
  billing_cycle string COMMENT'xx'
```

)

```
stored AS parquet location "odps://odps_smoke_test/volume25/test/" tblproperties (
  'mcfed.parquet.compression'='SNAPPY'
);
```

`location` 为Volume2文件路径。

**关联Textfile并使用SNAPPY压缩方式数据示例**

1. 查询外部数据：

```
bin/hdfs dfs -ls odps://project1/mid_dwd_d_prd_cb_user_product/part_id=1/day_id=28
```

2. 创建外部表：

```
CREATE EXTERNAL TABLE mid_dwd_d_prd_cb_user_product( month_id string,
  user_id string,
  prov_id string,
  product_id string,
  product_id_b string,
  brand_code string,
  uni_brand_code string,
  net_type_code string,
  prod_id string
```

)

```
partitioned by (part_id string, day_id string) row format serde 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' WITH SERDEPROPERTIES ( 'separatorChar'='\u0001'
```

)

```
stored AS textfile location "odps://project1/mid_dwd_d_prd_cb_user_product/";
```

3. 手动添加分区并进行查询：

```
ALTER TABLE mid_dwd_d_prd_cb_user_product ADD PARTITION(part_id='1',day_id='28'); SELECT * FROM mid_dwd_d_prd_cb_user_product WHERE part_id='1' AND day_id='28' limit 5;
```

**关联Textfile数据建表示例**

1. 上传Textfile数据文件至Volume2文件夹中。
#创建一个新`Volume2`目录

```
$./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest
```

#创建`Volume2`目录下的文件夹

```
$./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest/test_textfile
```

#上传`Textfile`数据文件

```
$./bin/hdfs dfs -put /home/admin/zx/json.txt odps://odps_smoke_test/zxtest/test_textfile/
```

#查看上传情况

```
$./bin/hdfs dfs -ls odps://odps_smoke_test/zxtest/test_textfile/
```

2. 创建外部表关联Textfile数据。

```
CREATE EXTERNAL TABLE test_textfile(
  `id` bigint,
  `type` bigint
```

)

```
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe' stored AS textfile location "odps://odps_smoke_test/zxtest/test_textfile/";
```

3. 查询外部表。

```
SELECT * FROM test_textfile;
```

4. 删除外部表。

```
DROP TABLE test_textfile;
```

5. 查看是否影响外部Textfile存储。

```
$./bin/hdfs dfs -ls odps://odps_smoke_test/zxtest/test_textfile/
```

Textfile数据文件依旧存在，所以删除外部表不会影响外部存储，且不会受生命周期的影响。

**关联CSV数据建表示例**

1. 上传CSV数据文件至Volume2文件夹中。
#创建`Volume2`目录下的文件夹

```
$./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest/test_csv
```

#上传`CSV`数据文件

```
$./bin/hdfs dfs -put /home/admin/zx/testcsv.csv odps://odps_smoke_test/zxtest/test_csv
```

2. 创建外部表关联CSV数据。

```
CREATE EXTERNAL TABLE zxtest_csv(
  `s1` string,
  `s2` string
```

)

```
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ('separatorChar'=',') stored AS textfile location "odps://odps_smoke_test/zxtest/test_csv/";
```

3. 查询外部表。

```
SELECT * FROM zxtest_csv;
```

**关联分区数据建表示例**

1. 创建分区数据存放目录，并上传测试数据。

**说明**

标准分区数据文件路径格式： `odps://<project_name>/<`目录名称>/<partitionKey1=value1>/<partition_Key2=value2>…/ 。

```
$./bin/hdfs dfs -mkdirodps://odps_smoke_test/zxtest/test_partition/year=2022 $./bin/hdfs dfs -put /home/admin/zx/testcsv.csvodps://odps_smoke_test/zxtest/test_partition/year=2022 $./bin/hdfs dfs -cat odps://odps_smoke_test/zxtest/test_partition/year=2022/testcsv.csv
```

2. 创建带有分区的外部表关联Volume2数据。

```
CREATE EXTERNAL TABLE zxtest_csv_partition(
  `s1` string,
  `s2` string
```

)

```
partitioned BY (year string) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ('separatorChar'=',') stored AS textfile location "odps://odps_smoke_test/zxtest/test_partition";
```

3. 手动添加分区。

```
ALTER TABLE zxtest_csv_partition ADD PARTITION (year='2022');
```

4. 查询分区数据。

```
SELECT * FROM zxtest_csv_partition WHERE year='2022';
```

5. 手动创建带分区内部表，从外部表及对应外部存储中访问数据并插入到内部表。

**说明**

可以利用 show create table <table_name>; 命令获取外部表DDL语句，方便构造内部表DDL语句。请不要使用 `create table like` 命令复制外部表结构，会出现报错。 `--`创建内部表

```
CREATE TABLE zxtest_csv_partition3 (s1 string,
 s2 string)
 partitioned BY (year string);
```

`--`手动创建分区

```
ALTER TABLE zxtest_csv_partition3 ADD PARTITION (year='2022');
```

`--`查询外表并将外部存储插入到内表分区中

```
INSERT OVERWRITE TABLE zxtest_csv_partition3 PARTITION (year='2022') SELECT s1,s2 FROM zxtest_csv_partition WHERE year='2022';
```

**关联以gzip压缩格式存储的Textfile数据文件示例**

1. 创建Volume数据存放目录，并将gzip压缩格式的Textfile上传。

```
./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest/test_textfile_gz ./bin/hdfs dfs -put /home/admin/zx/json.gz odps://odps_smoke_test/zxtest/test_textfile_gz
```

2. 创建外部表关联Textfile的gzip压缩格式数据。

```
CREATE EXTERNAL TABLE test_textfile_gz(
  `id` bigint,
  `type` bigint
```

)

```
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe' WITH serdeproperties ('odps.text.option.gzip.input.enabled'='true') stored AS textfile location "odps://odps_smoke_test/zxtest/test_textfile_gz/";
```

3. 查询外部表。

```
SELECT * FROM test_textfile_gz;
```

**关联以bzip2压缩格式存储的Textfile数据文件示例**

1. 创建Volume数据存放目录，并将bzip2压缩格式Textfile文件上传。

```
$./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest/test_textfile_bz2 $./bin/hdfs dfs -put /home/admin/zx/json.bz2 odps://odps_smoke_test/zxtest/test_textfile_bz2/
```

2. 创建外表关联textfile的bzip2压缩格式数据。

```
CREATE EXTERNAL TABLE test_textfile_bz(
  `id` bigint,
  `type` bigint
```

)

```
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe' WITH serdeproperties ('odps.text.option.bzip2.input.enabled'='true') stored AS textfile location "odps://odps_smoke_test/zxtest/test_textfile_bz2/";
```

3. 查询外部表。

```
SELECT * FROM test_textfile_bz;
```

**关联以gzip压缩格式存储的CSV数据文件示例**

1. 创建Volume数据存放目录，并将gzip压缩格式的CSV上传。

```
$./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest/test_csv_gz $./bin/hdfs dfs -put /home/admin/zx/testcsv.gz odps://odps_smoke_test/zxtest/test_csv_gz/
```

2. 创建外部表关联Textfile的gzip压缩格式数据。

```
CREATE EXTERNAL TABLE zxtest_csv_gz(
  `s1` string,
  `s2` string
```

)

```
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ('separatorChar'=',','odps.text.option.gzip.input.enabled'='true') stored AS textfile location "odps://odps_smoke_test/zxtest/test_csv_gz/";
```

3. 查询外部表。

```
SELECT * FROM zxtest_csv_gz;
```

**关联以bzip2压缩格式存储的CSV数据文件示例**

1. 创建Volume数据存放目录，并将bzip2压缩格式的CSV上传。

```
$./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest/test_csv_bz2 $./bin/hdfs dfs -put /home/admin/zx/testcsv.bz2 odps://odps_smoke_test/zxtest/test_csv_bz2/
```

2. 创建外部表关联Textfile的gzip压缩格式数据。

```
CREATE EXTERNAL TABLE zxtest_csv_bz2(
  `s1` string,
  `s2` string
```

)

```
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ('separatorChar'=',','odps.text.option.bzip2.input.enabled'='true') stored AS textfile location "odps://odps_smoke_test/zxtest/test_csv_bz2/";
```

3. 查询外部表。

```
SELECT * FROM zxtest_csv_bz2;
```

**关联Orcfile数据文件**

**非分区外部表关联Orcfile**

1. 创建Volume数据存放目录，并上传Orcfile数据文件。

```
$./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest/ld/ $./bin/hdfs dfs -put /home/admin/zx/000000_0 odps://odps_smoke_test/zxtest/ld
```

2. 创建外部表关联Textfile的gzip压缩格式数据。

```
CREATE EXTERNAL TABLE IF NOT EXISTS ld2( id_card BIGINT, tran_time STRING, name STRING, cash BIGINT
```

)

```
STORED AS ORC LOCATION 'odps://odps_smoke_test/zxtest/ld/';
```

3. 查询外部表。

```
SELECT * FROM ld2;
```

**分区外部表关联Orcfile**

1. 创建Volume数据存放目录，并上传Orcfile数据文件。

**说明**

请不要在分区存放路径名中用类似 `2020-09-21` 这样带有 - 的名称，会影响数据访问。

```
$./bin/hdfs dfs -mkdir odps://odps_smoke_test/zxtest/test_orc_pt/year=2022 $./bin/hdfs dfs -put /home/admin/zx/000000_0 odps://odps_smoke_test/zxtest/test_orc_pt/year=2022
```

2. 创建外部表关联Textfile的gzip压缩格式数据，并进行查询。

```
CREATE EXTERNAL TABLE account_orc( id_card int, tran_time string, name string, cash int
```

)

```
PARTITIONED BY ( year string) ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.orc.OrcSerde' stored AS orc location "odps://odps_smoke_test/zxtest/test_orc_pt"; ALTER TABLE account_orc ADD PARTITION(year='2022');
```

3. 查询外部表。

```
SELECT * FROM account_orc WHERE year='2022';
```

**同目录下多类型数据访问支持度**

同目录下支持同时访问不同数据类型及压缩类型数据，需要保证列的数量及类型与外部存储结构对应。

**VolumeFS中文件上传性能测试**

源文件为30列552 MB大小的CSV文件，分别压缩为gzip和bzip2格式进行上传测试。压缩后，gzip压缩文件为216 MB，bzip2压缩文件为169 MB。 原CSV文件直接上传：

```
./bin/hdfs dfs -put /home/admin/zx/test30.csv odps://odps_smoke_test/zxtest/testput/csv
```

上传时间为15s，平均上传速度约36.8MB/s。 gzip压缩文件上传：

```
./bin/hdfs dfs -put /home/admin/zx/test30.gz odps://odps_smoke_test/zxtest/testput/gz
```

上传时间为8s，平均上传速度约为27MB/s。 bzip2压缩文件上传：

```
./bin/hdfs dfs -put /home/admin/zx/test30.csv.bz2 odps://odps_smoke_test/zxtest/testput/bzip2
```

上传时间为9s，平均上传速度约为18.8MB/s。

**VolumeFs外部表分区数据插入到内部表分区中性能测试**

SQLTask Version如下图所示：

**测试1：2列1.9GB数据测试**

| 创建带分区外部表，Volume数据存放目录为 | odps://odps_smoke_test/zxtest/2t_csv | 。 |
|---|---|---|
| CREATE EXTERNAL TABLE zxtest_2t_csv( `s1` string, `s2` string ) partitioned BY (year string) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ('separatorChar'=',') stored AS textfile location "odps://odps_smoke_test/zxtest/2t_csv"; |  |  |

2. 新增分区，与目录对应。

```
ALTER TABLE zxtest_2t_csv ADD PARTITION (year='2022');
```

3. 创建带分区内部表。

```
CREATE TABLE zxtest_2t_csv_nei( s1 string, s2 string
```

)

```
partitioned BY (year string); ALTER TABLE zxtest_2t_csv_nei ADD PARTITION (year='2022'); --关闭service mode SET odps.service.mode=off;
```

4. 将外部表数据插入到内部表。

```
INSERT OVERWRITE TABLE zxtest_2t_csv_nei PARTITION (year='2022') SELECT s1,s2 FROM zxtest_2t_csv WHERE year='2022';
```

5. 测试结果。
通过LogView查看数据写入情况如下图所示：

**测试2：30列2.1GB数据测试**

| 创建带分区外部表，Volume数据存放目录为 | odps://odps_smoke_test/zxtest/testpartition30c | 。 |
|---|---|---|
| CREATE EXTERNAL TABLE zxtest_csv_30c( c1 string, c2 string, c3 string, c4 string, c5 string, c6 string, c7 string, c8 string, c9 string, c10 string, c11 string, c12 string, c13 string, c14 string, c15 string, c16 string, c17 string, c18 string, c19 string, c20 string, c21 string, c22 string, c23 string, c24 string, c25 string, c26 string, c27 string, c28 string, c29 string, c30 string ) partitioned BY (month string) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ('separatorChar'=',') stored AS textfile location "odps://odps_smoke_test/zxtest/testpartition30c"; |  |  |

2. 新增分区，与目录对应。

```
ALTER TABLE zxtest_csv_30c ADD PARTITION (month='4');
```

3. 创建带分区内部表。
#创建`Maxcompute`内表

```
CREATE TABLE zxtest_csv_30c_input( c1 string, c2 string, c3 string, c4 string, c5 string, c6 string, c7 string, c8 string, c9 string, c10 string, c11 string, c12 string, c13 string, c14 string, c15 string, c16 string, c17 string, c18 string, c19 string, c20 string, c21 string, c22 string, c23 string, c24 string, c25 string, c26 string, c27 string, c28 string, c29 string, c30 string )partitioned BY (month string); ALTER TABLE zxtest_csv_30c_input ADD PARTITION (month='4'); --关闭service mode SET odps.service.mode=off;
```

4. 将外部表数据插入到内部表。

```
INSERT OVERWRITE TABLE zxtest_csv_30c_input PARTITION (month='4') SELECT c1 ,c2 ,c3 ,c4 ,c5 ,c6 ,c7 ,c8 ,c9,c10,c11 ,c12 ,c13 ,c14 ,c15 ,c16 ,c17 ,c18 ,c19 ,c20 ,c21 ,c22 ,c23 ,c24 ,c25,c26 ,c27 ,c28 ,c29 ,c30 FROM zxtest_csv_30c WHERE month='4';
```

5. 查看测试结果。
通过LogView查看数据写入情况如下图所示：

### 离线加速增强包

**11.5.1. 概述**

本文为您介绍MaxCompute的短查询离线加速增强包（MaxCompute Query Acceleration，简称MCQA），方便您了解该增强包的系统架构、关键特性、应用场景和使用限制。

**功能**

MaxCompute的MCQA可以对中、小数据量查询作业进行加速优化，将执行时间为分钟级的查询作业缩减至秒级，同时完全兼容原MaxCompute的查询功能。 MCQA支持将主流BI工具或SQL客户端连接至MaxCompute项目，开展即席查询（Ad Hoc）或商业智能（BI）分析。 MCQA使用独立的资源池，不占用配额组，可以自动识别查询作业，缓解排队压力，优化使用体验。

**关键特性**

MCQA功能的关键特性如下： 低延时采用高效、低延时的资源调度策略，并且使用单独的资源池。 自动识别支持自动识别查询作业大小，优先快速返回查询结果或通过批处理返回结果，为分析不同规模或复杂度的查询作业提供保障。 语法兼容 SQL语法与原MaxCompute SQL语法完全一致。 支持选择查询方式支持客户端选择MCQA或批处理方式执行查询作业，您也可以强制指定使用MCQA适应对时延敏感的场景。

**应用场景**

MCQA的应用场景如下。

| 场景 | 说明 | 场景特点 |
|---|---|---|
| 即席查询（Ad Hoc） | 您可以通过MCQA优化中小规模数据集（百GB规模内）的查询性能，直接对MaxCompute表开展低时延的查询操作，以便快速完成数据开发及数据分析。 | 您可以根据实际需求，灵活选择查询条件，快速获取查询结果并调整查询逻辑。对查询时延的要求在几十秒内。使用者通常为掌握SQL技能的数据开发或数据分析师，希望使用熟悉的客户端工具开展查询分析。 |
| 商业智能（BI） | 利用MaxCompute搭建企业级数据仓库时，ETL会将数据加工处理为面向业务可消费的聚合数据。借助MCQA的低延时、弹性并发、数据缓存等特性，结合MaxCompute表分区、分桶等优化设计，可以低成本满足多并发、快速响应的报告生成、统计分析及固定报表分析需求。 | 查询的数据对象通常为聚合后的结果数据，适用于数据量较小、多维查询、固定查询、高频查询场景。查询延时要求高， 秒级返回（例如大部分查询不超过5秒，不同查询作业由于数据规模和查询复杂度不同，查询时间有较大差异）。 |
| 海量数据明细查询分析 | MCQA可以自动识别查询作业特征，既能快速响应，处理小规模作业，同时还可以自动匹配大规模作业资源需求，满足分析人员分析不同规模和复杂度的查询作业的需求。 | 需要探索的历史数据量大、真正需要的有效数据量不大、查询延时要求适中。使用者通常为业务分析人员，往往需要从明细数据中探寻业务规律，发现业务机会，验证业务假设。 |

**使用限制**

仅支持SELECT语句，不支持用户自定义UDF。如果您提交了MCQA不支持的语句或功能，MaxCompute客户端会自动回退到普通离线模式执行，其它工具暂不支持回退到普通离线模式执行。 MCQA功能的详细使用限制如下。

| 限制项 | 说明 |
|---|---|
| 查询 | 单次执行的MCQA作业如果超过1000个，系统会将MCQA作业默认回退为普通查询作业。 您通过客户端提交的MCQA作业默认30s超时，通过DataWorks临时查询提交的MCQA作业默认20s超时，超时后MCQA作业将默认回退为普通查询作业。 仅存储格式为ALIORC的表的数据才可能被缓存至内存中进行加速。 不支持查询外部表。 |
| 查询并发 | 单个MaxCompute项目的MCQA作业最大并发数为120。 |

#### 11.5.2. 使用说明

MCQA（MaxCompute Query Acceleration）是MaxCompute内建的功能，使用原生的MaxCompute SQL语言，并且支持所有的MaxCompute内建函数以及权限系统。本文为您介绍如何使用MCQA增强包。

**背景信息**

MCQA支持的接入方式如下： DataWorks临时查询或数据开发：默认无缝接入，使用说明请参见DataWorks临时查询或数据开发。 JDBC：无缝接入，使用说明请参见JDBC。 SDK：需要配置Pom依赖，使用说明请参见基于Java SDK启用MCQA功能。
1. 下载最新版客户端。
2. 将下载好的客户端压缩包解压到一个文件夹中，在该文件夹中可以看到如下4个文件夹。

```
bin/ conf/ lib/ plugins/
```

3. 配置客户端，详情请参见配置客户端（Console）。
4. 编辑conf文件夹中的**odps_config.ini**文件，在配置文件最后一行增加如下命令行。

```
enable_interactive_mode=true
```

5. 运行bin目录下的**odps**文件（在Linux系统下运行odpscmd文件，在Windows下运行odpscmd.bat文件）。出现如下信息，表示运行成功。
6. 执行查询作业验证MCQA功能已开启。
执行查询作业后，客户端界面返回结果如果包含如下信息表明MCQA功能已开启。

**DataWorks临时查询或数据开发**

DataWorks的**临时查询**及**手动业务流程**模块默认开启MCQA功能，您无需手动开启。如果您需要关闭MCQA功能，请联系MaxCompute技术支持处理。 在**临时查询**模块执行查询作业，如果返回结果包含如下信息表明MCQA功能已开启。 在**手动业务流程**模块执行查询作业，返回结果包含如下信息表明MCQA功能已开启。

**JDBC**

JDBC使用场景如下： 使用JDBC连接MaxCompute。如果您需要在该场景下开启MCQA功能，需要修改相关配置，详情请参见配置JDBC启用MCQA功能。 使用JDBC连接Tableau，对MaxCompute中的数据进行可视化分析。如果您需要在该场景下开启MCQA功能，需要修改相关配置，详情请参见基于JDBC配置 Tableau启用MCQA功能。 使用JDBC连接SQL Workbench/J，使用SQL Workbench/J对MaxCompute中的数据执行SQL语句。如果您需要在该场景下开启MCQA功能，需要修改相关配置， 详情请参见基于JDBC配置SQLWorkBench启用MCQA功能。

**配置JDBC启用MCQA功能**

使用JDBC连接MaxCompute时，您可以通过执行如下操作开启MCQA功能。
1. 下载支持MCQA功能的JDBC JAR包或可编译的源代码。
2. 通过Maven方式配置Pom依赖。

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-jdbc</artifactId>
  <version>3.2.0</version>
  <classifier>jar-with-dependencies</classifier>
</dependency>
```

**说明**

版本需要为3.2.0及以上版本。
3. 基于源代码创建Java程序，适配实际信息。详情请参见ODPS JDBC。
需要适配的信息如下。

```
String accessId = "your_access_id"; String accessKey = "your_access_key"; String conn = "jdbc:odps:http://service.odps.aliyun.com/api?project=<your_project_name>&accessId&accessKey&charset=UTF- 8&interactiveMode=true"; Statement stmt = conn.createStatement();
```

`--your_access_id`、`your_access_key`为您的云账号信息，`your_project_name`为需要使用`MCQA`功能的项目名称。

```
Connection conn = DriverManager.getConnection(conn, accessId, accessKey); Statement stmt = conn.createStatement(); String tableName = "testOdpsDriverTable"; stmt.execute("drop table if exists " + tableName); stmt.execute("create table " + tableName + " (key int, value string)");
```

在JDBC中启用MCQA功能的方式与常规方式完全一致，只需要在连接串（ `String conn` ）或代码中（二选一即可）配置如下信息：

| String conn |  | ）：增加 | interactiveMode=true |  |
|---|---|---|---|---|
| 加 | interactiveMode=true |  |  | 语句。 |

4. **可选：**您可以在连接串中配置如下参数，完善处理逻辑。

| enableOdpsLogger |  |
|---|---|
| fallbackForUnknownError |  |
| fallbackForResourceNotEnough |  |
| fallbackForUpgrading |  |
| fallbackForRunningTimeout |  |
| fallbackForUnsupportedFeature |  |
| fallbackForAll | ：默认为False， |

**基于JDBC配置Tableau启用MCQA功能**

**服务器**增加 `interactiveMode=true` 属性，用于开启MCQA功能。建议您同步增加 `enableOdpsLogger=true` 属性，用于打印日志。
完整的**服务器**配置示例如下。

```
http://service.cn-beijing.maxcompute.aliyun.com/api?project=****_beijing&interactiveMode=true&enableOdpsLogger=true
```

如果只对项目空间中的部分表进行Tableau操作，您可以在**服务器**参数中增加 `table_list=table_name1,table_name2` 属性选择需要的表，表之间用半角逗号（,） 分隔。如果表过多，会导致Tableau打开缓慢，强烈建议使用此方式只载入需要的表。示例如下。

```
http://service.cn-beijing.maxcompute.aliyun.com/api? project=****_beijing&interactiveMode=true&enableOdpsLogger=true&table_list=orders,customers
```

对于有大量分区的表不建议把所有分区的数据都设置成数据源，可以筛选需要的分区，或通过自定义SQL获取需要的数据。

**基于JDBC配置SQLWorkBench启用MCQA功能**

完成JDBC驱动配置后，在Profile配置界面修改已填写的JDBC URL，支持SQLWorkBench使用MCQA功能。

```
需要配置的URL格式为 jdbc:odps:<MaxCompute_endpoint>?project=<MaxCompute_project_name>&accessId=<AccessKey ID>&accessKey=<AccessKey
```

`Secret>&charset=UTF-8&interactiveMode=true` ，参数说明如下：
**maxcompute_endpoint**：MaxCompute服务的Endpoint。
**maxcompute_project_name**：MaxCompute项目空间名称。
**AccessKey ID**：有访问指定项目空间权限的AccessKey ID。
********************：AccessKey ID对应的AccessKey Secret。
**charset=UTF-8**：字符集编码格式。
**interactiveMode**：MCQA功能开关，true表示开启MCQA功能。

**基于Java SDK启用MCQA功能**

您需要通过Maven配置Pom依赖，配置示例如下。

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-core</artifactId>
  <version>0.36.2-public</version>
</dependency>
```

创建Java程序，命令示例如下。

```java
import com.aliyun.odps.Odps; import com.aliyun.odps.OdpsException; import com.aliyun.odps.OdpsType; import com.aliyun.odps.account.Account; import com.aliyun.odps.account.AliyunAccount; import com.aliyun.odps.data.Record; import com.aliyun.odps.data.ResultSet; import com.aliyun.odps.sqa.*; import java.io.IOException; import java.util.*; public class SQLExecutorExample {
    public static void SimpleExample() {
```

`//` 设置账号和项目信息。

```
        Account account = new AliyunAccount("your_access_id", "your_access_key");
        Odps odps = new Odps(account);
        odps.setDefaultProject("your_project_name");
        odps.setEndpoint("http://service.odps.aliyun.com/api");
```

`//` 准备构建`SQLExecutor`。

```
        SQLExecutorBuilder builder = SQLExecutorBuilder.builder();
        SQLExecutor sqlExecutor = null;
        try {
            // run in offline mode or run in interactive mode
            if (false) {
```

`//` 创建一个默认执行离线`SQL`的`Executor`。

```
                sqlExecutor = builder.odps(odps).executeMode(ExecuteMode.OFFLINE).build();
            } else {
```

`//` 创建一个默认执行查询加速`SQL`的`Executor`。

```
                sqlExecutor = builder.odps(odps).executeMode(ExecuteMode.INTERACTIVE).build();
            }
```

`//` 如果需要的话可以传入查询的特殊设置。

```
            Map<String, String> queryHint = new HashMap<>();
            queryHint.put("odps.sql.mapper.split.size", "128");
```

`//` 提交一个查询作业，支持传入`Hint`。

```
            sqlExecutor.run("select count(1) from test_table;", queryHint);
```

`//` 列举一些支持的常用获取信息的接口。

```java
            // UUID
            System.out.println("ExecutorId:" + sqlExecutor.getId());
```

`//` 当前查询作业的`logview`。

```java
            System.out.println("Logview:" + sqlExecutor.getLogView());
```

`//` 当前查询作业的`Instance`对象（`Interactive`模式多个查询作业可能为同一个`Instance`）。

```java
            System.out.println("InstanceId:" + sqlExecutor.getInstance().getId());
```

`//` 当前查询作业的阶段进度（`Console`的进度条）

```java
            System.out.println("QueryStageProgress:" + sqlExecutor.getProgress());
```

`//` 当前查询作业的执行状态变化日志，例如回退信息。

```java
            System.out.println("QueryExecutionLog:" + sqlExecutor.getExecutionLog());
```

`//` 提供两种获取结果的接口。

```
            if(false) {
```

`//` 直接获取全部查询作业结果，同步接口，可能会占用本线程直到查询成功或失败。

```
                List<Record> records = sqlExecutor.getResult();
                printRecords(records);
            } else {
```

`//` 获取查询结果的迭代器`ResultSet`，同步接口，可能会占用本线程直到查询成功或失败。

```
                ResultSet resultSet = sqlExecutor.getResultSet();
                while (resultSet.hasNext()) {
                    printRecord(resultSet.next());
                }
            }
            // run another query
            sqlExecutor.run("select * from test_table;", new HashMap<>());
            if(false) {
```

`//` 直接获取全部查询结果，同步接口，可能会占用本线程直到查询成功或失败。 `//`直接获取全部查询结果同步接口可能会占用本线程直到查询成功或失败

```
                List<Record> records = sqlExecutor.getResult();
                printRecords(records);
            } else {
```

`//` 获取查询结果的迭代器`ResultSet`，同步接口，可能会占用本线程直到查询成功或失败。

```
                ResultSet resultSet = sqlExecutor.getResultSet();
                while (resultSet.hasNext()) {
                    printRecord(resultSet.next());
                }
            }
        } catch (OdpsException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (sqlExecutor != null) {
```

`//` 关闭`Executor`释放相关资源。

```
                sqlExecutor.close();
            }
        }
    }
    // SQLExecutor can be reused by pool mode
    public static void ExampleWithPool() {
```

`//` 设置账号和项目信息。

```
        Account account = new AliyunAccount("your_access_id", "your_access_key");
        Odps odps = new Odps(account);
        odps.setDefaultProject("your_project_name");
        odps.setEndpoint("http://service.odps.aliyun.com/api");
```

`//` 通过连接池方式执行查询。

```
        SQLExecutorPool sqlExecutorPool = null;
        SQLExecutor sqlExecutor = null;
        try {
```

`//` 准备连接池，设置连接池大小和默认执行模式。

```
            SQLExecutorPoolBuilder builder = SQLExecutorPoolBuilder.builder();
            builder.odps(odps)
                    .initPoolSize(1) // init pool executor number
                    .maxPoolSize(5)  // max executors in pool
                    .executeMode(ExecuteMode.INTERACTIVE); // run in interactive mode
            sqlExecutorPool = builder.build();
```

`//` 从连接池中获取一个`Executor`，如果不够将会在`Max`限制内新增`Executor`。

```
            sqlExecutor = sqlExecutorPool.getExecutor();
```

`// Executor`具体用法和上一示例一致。

```java
            sqlExecutor.run("select count(1) from test_table;", new HashMap<>());
            System.out.println("InstanceId:" + sqlExecutor.getId());
            System.out.println("Logview:" + sqlExecutor.getLogView());
            List<Record> records = sqlExecutor.getResult();
            printRecords(records);
        } catch (OdpsException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            sqlExecutor.close();
        }
        sqlExecutorPool.close();
    }
    private static void printRecord(Record record) {
        for (int k = 0; k < record.getColumnCount(); k++) {
            if (k != 0) {
                System.out.print("\t");
            }
            if (record.getColumns()[k].getType().equals(OdpsType.STRING)) {
                System.out.print(record.getString(k));
            } else if (record.getColumns()[k].getType().equals(OdpsType.BIGINT)) {
                System.out.print(record.getBigint(k));
            } else {
                System.out.print(record.get(k));
            }
        }
    }
    private static void printRecords(List<Record> records) {
        for (Record record : records) {
            printRecord(record);
            System.out.println();
        }
```

```
    }
    public static void main(String args[]) {
        SimpleExample();
        ExampleWithPool();
    }
}
```

### MaxCompute多地域部署

#### 11.6.1. MaxCompute多地域部署概述

MaxCompute 支持多地域部署，本文将介绍控制集群与计算集群的部署方式。

**部署方式**

控制集群：中心化部署，主要是进行资源的配置，计算任务的管理。 计算集群：每个地域独立部署，主要实现项目创建及计算任务下发。

#### 11.6.2. 多地域部署的特点

本文介绍MaxCompute多地域部署的特点。从v3.18.6版本开始，在原有跨域计算形态基础上，新增支持单元化形态。

**特点介绍**

**跨域计算形态**

同一个MaxCompute服务实例可以管理异地不同的集群。 集群间数据交互在MaxCompute服务内部进行，集群间数据复制与同步按照配置管理。 元数据统一存放，对不同机房间网络等基础设施条件要求较高。 账号系统统一，跨地域部署运行时可以全局管理账号，统一添加用户和分配账号权限大数据应用开发系统，如DataWorks统一接入。 运维、部署及升级的相关支持上与单集群方式不同，对现场运维能力要求较高。

**单元化形态**

MaxCompute服务实例仅管理本地域的集群。 集群间数据交互在MaxCompute服务外部进行，集群间数据复制与同步通过Tunnel实现。 元数据单元化存放，对不同机房间网络等基础设施条件要求较低。 账号系统统一。 大数据应用开发系统，如DataWorks单元化接入。

**使用限制**

跨域计算形态，需要改造目前MaxCompute集群为多集群模式，才能进行多地域部署。

**说明**

部署条件： 网络带宽需要满足地域间数据同步要求和链路冗余。 中心地域控制集群对于基础服务，例如DNS或者TableStore的延迟比较高，需要在同一个机房内，网络延迟在5ms以内。 中心地域控制集群与其他Region计算集群间，要求网络延迟在20ms以内。 两地集群间及集群内机器间，要求时钟一致。 网络带宽需要满足集群间数据复制要求。 需要一套DNS服务。 需要集群将机器网络打通，两地集群的网络条件基本一致（千兆/万兆）。 单元化形态，不支持与跨域计算形态下的计算集群在同地域部署，无其它限制。

#### 11.6.3. 多地域部署的使用说明

本文介绍MaxCompute多地域部署的核心原理与应用场景，方便您快速掌握跨集群数据同步技巧及高可用架构设计方法。

#### 使用说明

MaxCompute计算任务在服务内部依据数据分布在某一个集群进行，集群间数据交互依据配置及数据分布，使用跨集群复制或者直读的方式。 不同的集群间可以依据配置进行数据复制和同步，数据复制和同步的粒度为表及分区级别。 需要从业务层规划MaxCompute项目空间和集群的关系，一个Project可以选择多个集群，也可以选择一个集群。

**说明**

选择多个集群的可以进行数据在不同集群间复制同步。 如某种业务在一个Project中，无法进行跨集群计算，可以配置分布数据在不同的集群，然后把计算任务按照数据分布切分。

**说明**

集群间数据复制及管理需要管理策略和维护。 异地机房集群间带宽需满足数据复制的要求，或者满足在数据只读条件下的带宽要求。 因为双机房间的带宽是共享的，MaxCompute跨集群复制或者只读，在数据量较大的情况时会占满带宽，影响其他数据传输。 因为主地域机房含有元数据和账号系统等信息，所以主机房集群故障时影响整个服务使用。 第二计算集群机房故障时，影响到该集群上有数据的项目空间，以及影响整体服务运维。

**说明**

数据独立在主地域机房的Project计算不受影响。 通常的使用场景为数据依据业务特点进行切分和复制配置，计算依据数据在不同的集群进行，然后应用组合不同的MaxCompute任务的结果。

#### 11.6.4. 多地域部署应用示例

##### 11.6.4.1. 多集群间表数据同步

**前提条件**

在AdminConsole中创建Project时，已勾选对应的两个集群，并设置其中一个集群为默认集群，示例如下。

**说明**

本示例中，Project为**multiregion**，**AT-MDU-TEST**和**AT-5KN**为勾选的两个集群，**AT-MDU-TEST**为默认集群。 AdminConsole的专有云地址是**http://{odps_ag}:9090**，即odps ag的9090端口。 操作入口为**ODPS****配置** **> Project****管理** > **创建****Project**。 为已创建的Project设置跨集群复制，示例操作如下。 i. 选择**ODPS****配置** > **多集群复制全局配置**，进入**多集群复制全局配置**页面。 ii. 在**infoBetweenClusters**区域的**Add Item**处，设置**key**为**AT-5KN#AT-MDU-TEST**，设置**availableBandwith**和**totalBandwith**为**2000**后，单击**add**。 iii. 单击**ODPS****配置** **> Project****管理**，找到**multiregion**后单击**多集群复制配置**按钮。 iv. 在打开的对话框中，做类似如下的配置。 v. 配置完成后，按顺序分别单击**保存**及**启动复制**，完成操作。

**操作步骤**

1. 在默认集群**AT-MDU-TEST**的ag上，在Console同级目录下构造一个上传Tunnel的数据文件，例如 `echo "testtest" > uploaddata` 。
2. 进入Console命令行，分别执行如下命令，创建表并向表中插入数据。

```
USE multiregion; CREATE TABLE t1 (s string); tunnel upload uploaddata t1;
```

3. 执行如下命令，查看表中是否插入数据成功。

```
SELECT * FROM t1;
```

4. 在集群**AT-MDU-TEST**、**AT-5KN**的ag机器上查看该表的飞天分布式文件系统目录，执行如下命令，验证该目录下是否有数据。

```
pu ls product/aliyun/odps/multiregion/data/t1
```

5. 如果两个集群均有数据，则表示多集群间表数据同步操作成功。

##### 11.6.4.2. 查询主备集群的数据同步状态

**前提条件**

在AdminConsole中创建Project时，已勾选对应的两个集群，并设置其中一个集群为默认集群，示例如下。

**说明**

本示例中，Project为**multiregion**，**AT-MDU-TEST**和**AT-5KN**为勾选的两个集群，**AT-MDU-TEST**为默认集群。 AdminConsole的专有云地址是**http://{odps_ag}:9090**，即odps ag的9090端口。 操作入口为**ODPS****配置** **> Project****管理** > **创建****Project**。 为已创建的Project设置跨集群复制，示例操作如下。 i. 选择**ODPS****配置** > **多集群复制全局配置**，进入**多集群复制全局配置**页面。 ii. 在**infoBetweenClusters**区域的**Add Item**处，设置**key**为**AT-5KN#AT-MDU-TEST**，设置**availableBandwith**和**totalBandwith**为**2000**后，单击**add**。 iii. 单击**ODPS****配置** **> Project****管理**，找到multiregion后单击**多集群复制配置**按钮。 iv. 在打开的对话框中，做类似如下的配置。 v. 配置完成后，按顺序分别单击**保存**及**启动复制**，完成操作。

**操作步骤**

示例操作如下。
1. 编写Bodychecksync配置文件，用于发送Admintask。

```xml
<Instance>
  <Job>
    <Comment>
    </Comment>
    <Priority>1</Priority>
    <Tasks>
      <Admin>
      <Name>task_1</Name>
      <Comment>test</Comment>
      <Config>
        <Property>
          <Name>PROJECT</Name>
          <Value>multiregion</Value>
        </Property>
        <Property>
          <Name>CLUSTER</Name>
          <Value>AT-MDU-TEST</Value>
        </Property>
      </Config>
      <Command>GET_UNREPLICATED_OBJECTS</Command>
      </Admin>
    </Tasks>
    <DAG>
      <Comment/>
    </DAG>
  </Job>
</Instance>
```

2. 编写Header。

```
content-type: application/xml
```

3. 执行如下命令，发送Admintask。

```
CLTrelease/bin/odpscmd -e "http post /projects/admin_task_project/instances -header=header -content=bodychecksync;"
```

4. 执行如下命令，查看Instance执行结果。

```
CLTrelease/bin/odpscmd --project=admin_task_project -e "wait 20180711050550317gnege3ms2;"
```

5. 复制步骤4中生成的LogView地址，并在浏览器中打开。
6. 在打开的页面中，单击**Job Details**，此时显示出的内容即为主备集群的数据同步状态。

##### 11.6.4.3. 跨域直读

本文为您介绍多地域部署应用中的跨域直读，并提供参考示例。

#### 使用说明

跨域直读有两种操作方式，分别为不配置跨集群访问的操作方式及配置跨集群访问的操作方式。

**说明**

使用不配置跨集群访问的操作方式时，如果数据量较大，会造成数据读取时间较长。

**不配置跨集群访问**

1. 在AdminConsole中分别创建两个Project，第一个Project为**testmdu**，第二个Project为**testcross5kn**。

**说明**

本示例中，Project testmdu勾选**AT-MDU-TEST**和**AT-5KN**两个计算集群，默认集群为**AT-MDU-TEST**；Project testcross5kn只勾**AT-5KN**集群，默认集群为**AT-5KN**。 AdminConsole的专有云地址是**http://{odps_ag}:9090**，即odps ag的9090端口。 操作入口为**ODPS****配置** **> Project****管理** > **创建****Project**。
2. 分别为Project testmdu和Project testcross5kn创建表。

```
CREATE TABLE testrep(s string); CREATE TABLE tablecross5kn (s string);
```

3. 分别为表testrep和tablecross5kn构造一定数据。
4. 执行如下命令，直接在testcross5kn读取testmdu上的表数据。

```
USE testcross5kn; SELECT * FROM testmdu.testrep;
```

**说明**

如果能读取到数据，证明操作成功，即完成跨域直读。

**配置跨集群访问**

1. 在AdminConsole中分别创建两个Project，第一个Project为**testmdu**，第二个Project为**testcross5kn**。

**说明**

本示例中，Project testmdu勾选**AT-MDU-TEST**和**AT-5KN**两个计算集群，默认集群为**AT-MDU-TEST**；Project testcross5kn只勾**AT-5KN**集群，默认集群为**AT-5KN**。 AdminConsole的专有云地址是**http://{odps_ag}:9090**，即odps ag的9090端口。 操作入口为**ODPS****配置** **> Project****管理** > **创建****Project**。
2. 分别为Project testmdu和Project testcross5kn创建表。

```
CREATE TABLE testrep(s string); CREATE TABLE tablecross5kn (s string);
```

3. 分别为表testrep和tablecross5kn构造一定数据。
4. 为Project testmdu配置跨集群复制。

**说明**

操作入口为**ODPS****配置** **> Project****管理**，单击testmdu后的**多集群复制配置**按钮。
5. 执行如下命令，直接在testcross5kn读取testmdu上的表数据。

```
USE testcross5kn; SELECT * FROM testmdu.testrep;
```

**说明**

如果能读取到数据，证明操作成功，即完成跨域直读。

##### 11.6.4.4. 跨域Join

**操作示例**

1. 在AdminConsole中分别创建两个Project，第一个Project为**crosssregion**，第二个Project为**crossregion02**。

**说明**

本示例中，Project crosssregion勾选**AT-MDU-TEST**和**AT-70N**两个计算集群，默认集群为**AT-MDU-TEST**；Project crossregion02只勾选**AT-**
**70N**集群，默认集群为**AT-70N**。
AdminConsole的专有云地址是**http://{odps_ag}:9090**，即odps ag的9090端口。 操作入口为**ODPS****配置** **> Project****管理** > **创建****Project**。
2. 为Project crosssregion配置跨集群复制。

**说明**

操作入口为**ODPS****配置** **> Project****管理**，单击crosssregion后的**多集群复制配置**按钮。
3. 在crosssregion上创建表business。

```
CREATE TABLE business(bid bigint,name string,phone string,address string,region string);
```

4. 为表business构造一定数据。
5. 执行如下命令，向business表中导入数据。

```
tunnel upload business business;
```

6. 在crossregion02上创建表product。

```
CREATE TABLE IF NOT EXISTS product(pid bigint,name string,type string,color string,bid bigint);
```

7. 为表product构造一定数据。
8. 执行如下命令，向product表中导入数据。

```
tunnel upload product product;
```

9. 在Console中执行如下命令，获取上述两张表中的一个特定数据。

```
SELECT pro.pid,pro.name,pro.type,pro.color,bus.name,bus.phone FROM crossregion02.product pro JOIN crosssregion.business bus ON pro.bid= bus.bid WHERE bus.region='上海';
```

**说明**

## 安全解决方案

### 目标用户

### 目标用户

安全解决方案主要面向MaxCompute项目空间所有者（Owner）、管理员以及对MaxCompute多租户数据安全体系感兴趣的用户。其中，MaxCompute多租户数据安全体系主要包括如下内容： 用户认证。 项目空间的用户与授权管理。

### 快速入门

本文介绍MaxCompute安全解决方案的简单操作流程，旨在引导您完成MaxCompute的相关安全操作。

**添加用户并授权**

场景描述： `Jack` 是项目空间 `prj1` 的管理员，一个新加入的项目组成员Alice（已拥有云账号：alice***@aliyun.com）申请加入项目空间 `prj1` ，并申请查看 Table列表、提交作业以及创建表的权限。

```
USE prj1;
```

`--` 添加用户。

```
ADD USER aliyun$alice***@aliyun.com;
```

`--` 使用`grant`语句对用户授权。

```
GRANT List, CreateTable, CreateInstance ON project prj1 TO USER aliyun$alice***@aliyun.com;
```

**说明**

需要由项目空间管理员进行上述操作。 场景描述：Jack是项目空间prj1的管理员，有三个新加入的项目组成员：Alice、Bob和Charlie，他们的角色是数据审查员。他们要申请查看Table列表、提交作业以及读取表userprofile的权限。 针对这个场景的授权，项目空间管理员可以使用基于对象的ACL授权机制来完成。具体操作如下。

```
USE prj1; ADD USER aliyun$alice***@aliyun.com;
```

`--` 添加用户。

```
ADD USER aliyun$bob***@aliyun.com; ADD USER aliyun$charlie***@aliyun.com; CREATE role tableviewer;
```

`--` 创建角色。

```
GRANT List, CreateInstance ON project prj1 TO role tableviewer;
```

`--` 对角色赋权。

```
GRANT DESCRIBE, SELECT ON TABLE userprofile TO role tableviewer; GRANT tableviewer TO aliyun$alice***@aliyun.com;
```

`--` 对用户赋予角色`tableviewer`。

```
GRANT tableviewer TO aliyun$bob***@aliyun.com; GRANT tableviewer TO aliyun$charlie***@aliyun.com;
```

**资源打包分享**

场景描述：Jack是项目空间prj1的管理员。John是项目空间prj2的管理员。由于业务需要，Jack希望将其项目空间prj1中的某些资源（例如datamining.jar及 sampletable表）分享给John的项目空间prj2。如果项目空间prj2的用户Bob需要访问这些资源，那么prj2管理员可以通过ACL或Policy自主授权，无需Jack参与。
1. 项目空间prj1的管理员Jack在项目空间prj1中创建资源包（Package）。

```
USE prj1;
```

`--` 创建一个`Package`。

```
CREATE package datamining;
```

`--` 添加资源到`Package`。

```
ADD resource datamining.jar TO package datamining;
```

`--` 添加`Table`到`Package`。

```
ADD TABLE sampletable TO package datamining;
```

`--` 将`Package`分享给项目空间`prj2`。

```
allow project prj2 TO install package datamining;
```

2. 项目空间prj2管理员John在项目空间prj2中安装Package。

```
USE prj2;
```

`--` 安装一个`Package`。

```
install package prj1.datamining;
```

`--` 查看`Package`中的资源列表。

```
DESCRIBE package prj1.datamining;
```

3. John对Package进行自主授权。

```
USE prj2;
```

`--` 通过`ACL`机制，授权`Bob`使用`Package`。

```
GRANT Read ON package prj1.datamining TO USER aliyun$bob***@aliyun.com;
```

**说明**

场景描述：Jack是项目空间prj1的管理员。该项目空间有很多敏感数据，例如用户身份号码和购物记录。而且还有很多具有自主知识产权的数据挖掘算法。Jack希望能将项目空间中的这些敏感数据和算法保护好，项目中用户只能在项目空间中访问，数据只能在项目空间内流动，不允许流出到项目空间之外。

```
USE prj1; SET ProjectProtection=true;
```

一旦项目空间开启数据保护机制后，无法将项目空间中的数据转移到项目空间之外，所有的数据只能在项目空间内部流动。但是在某些情况下，可能由于业务需要，用户Alice需要将某些数据表导出到项目空间之外，并且也经过空间管理员的审核通过。针对这类情况，MaxCompute提供了两种机制来支持受保护项目空间的数据流出。 方法1：设置ExceptionPolicy。详情请参见开启数据保护后的数据流出方法。
1. 创建Policy文件。例如创建一个/tmp/exception_policy.txt，它只允许Alice使用SQL任务将表t1从项目空间prj1导出。Policy文件内容如下。

```json
{
 "Version": "1",
 "Statement": [{
  "Effect":"Allow",
  "Principal":"ALIYUN$alice***@aliyun.com",
  "Action":["odps:Describe","odps:Select"],
  "Resource":"acs:odps:*:projects/prj1/tables/t1",
  "Condition":{
   "StringEquals": { "odps:TaskType":"SQL"}
      }
   }]
}
```

2. 设置ExceptionPolicy。

```
USE prj1; SET ProjectProtection=true WITH exception /tmp/exception_policy.txt;
```

**说明**

设置ExceptionPolicy时，应确保导出人（Principal）对数据资源（Resource）不具有更新（Update）或重建同名对象（Drop + CreateTable）权限，以防止TOC2TOU（time-of-check to time-of-use）数据泄露。 方法2：设置TrustedProject。将prj2设置为prj1的可信项目空间，设置后将允许prj1中的所有数据流出到prj2。详情请参见开启数据保护后的数据流出方法。

```
USE prj1; ADD trustedproject prj2;
```

**说明**

MaxCompute规定：资源分享拥有更高的优先级。即在一个受保护的项目空间中，如果一个对象是通过Package机制分享给其他项目空间，那么跨项目空间访问该对象时将不受ProjectProtection规则的限制。

### 用户认证

**认证说明**

用户认证（Authentication）的主要功能是检查请求（Request）发送者的真实身份。通常包括如下两个方面： 正确验证消息发送方的真实身份。 正确验证接收到的消息在途中是否被篡改。

### 项目空间的用户及授权管理

**12.4.1. 概述**

本文为您介绍项目空间的用户管理、角色管理以及授权操作。

#### 使用说明

项目空间（Project）是MaxCompute实现多租户体系的基础，是您管理数据和计算的基本单位。当您申请创建一个项目空间之后，您就是这个空间的所有者 （Owner）。也就是说，这个项目空间内的所有对象（例如：表、实例、资源、UDF等）都属于您。除了Owner之外，任何人都无权访问此项目空间内的对象，除非有Owner的授权许可。 假设用户Alice是项目空间test_project的Owner，如果有其他人需要申请访问项目空间test_project的资源，并且这个申请人属于Alice的项目团队。那么可以采用本章节介绍的方法来进行用户管理以及授权操作。如果申请人不属于Alice的项目团队，建议使用跨项目空间的资源分享功能，详情请参见跨项目空间的资源分享。

#### 12.4.2. 用户管理

本文介绍项目空间的用户管理流程，包括用户的添加、移除及权限清理策略。

**添加用户**

当项目空间的Owner Alice决定对另一个用户授权时，Alice需要先将该用户添加到自己的项目空间中。只有添加到项目空间中的用户才能够被授权。 `--` 在项目空间中添加用户。

```
ADD USER <full_username>;
```

**移除用户**

当一个用户离开此项目团队时，Alice需要将该用户从项目空间中移除。用户一旦从项目空间中被移除，该用户将不再拥有任何访问项目空间资源的权限。 `--` 在项目空间中移除用户。

```
remove USER <full_username>
```

**说明**

移除一个用户之前，如果该用户已被赋予某些角色，则需要先撤销该用户的所有角色。关于角色的介绍请参见角色管理。 用户被移除后，其关联的ACL授权与项目空间级Policy将予以保留，仅角色级（Role）Policy失效。若该用户后面重新加入项目，其原有的ACL访问权限将自动恢复。

| purge privs from user <username>; |  |
|---|---|
|  | Principal still exist in the project |

#### 12.4.3. 角色管理

本文介绍项目空间的角色管理流程，包括角色的添加、移除及权限清理策略。

#### 使用说明

角色（Role）是一组访问权限的集合。当需要对一组用户赋予相同的权限时，可以使用角色来授权。基于角色的授权可以简化授权流程，降低授权管理成本。当需要对用户授权时，应当优先考虑是否应该使用角色来完成。 每一个项目空间在创建时，会自动创建一个Admin的角色，并且为该角色授予了固定的权限：能访问项目空间内的所有对象、能进行用户与角色管理以及能对用户或角色进行授权。与项目空间Owner相比，Admin角色不能将Admin权限指派给用户，不能设定项目空间的安全配置，不能修改项目空间的鉴权模型。Admin角色所对应的权限不能被修改。

**角色管理相关命令**

`--` 创建角色。

```
CREATE role <rolename>;
```

`--` 删除角色。

```
DROP role <rolename>;
```

`--` 给用户指派某种角色。

```
GRANT <rolename> TO <username>;
```

`--` 撤销角色指派。

```
REVOKE <rolename> FROM <username>;
```

**说明**

删除一个角色时，MaxCompute会检查该角色内是否还存在其他用户。如果存在，则删除该角色失败。只有在该角色的所有用户都被撤销时，删除角色才会成功。

#### 12.4.4. ACL授权操作

MaxCompute项目空间支持ACL授权操作，通过识别主体、客体和操作三要素来有效管理用户权限。本文介绍授权命令的格式及使用场景。

**授权要素**

授权操作通常涉及到三个要素：主体（Subject）、客体（Object）和操作（Action）。在MaxCompute中，主体是指用户，客体是指项目空间中的各种类型对象， 操作则与特定对象类型有关，不同类型的对象支持的操作也不尽相同。

**授权操作说明**

MaxCompute项目空间支持如下的对象类型及操作。 表1.对象类型及操作

| 客体（Object） | 操作（Action） | 说明 |
|---|---|---|
| Project | Read | 查看项目空间自身（不包括项目空间的任何对象）的信息，如CreateTime等。 |
| Project | Write | 更新项目空间自身（不包括项目空间的任何对象）的信息，如Comments。 |
| Project | List | 查看项目空间所有类型的对象列表。 |
| Project | CreateTable | 在项目空间中创建Table。 |
| Project | CreateInstance | 在项目空间中创建Instance。 |
| Project | CreateFunction | 在项目空间中创建Function。 |
| Project | CreateResource | 在项目空间中创建Resource。 |
| Project | CreateJob | 在项目空间中创建Job。 |
| Project | CreateVolume | 在项目空间中创建Volume。 |
| Project | All | 具备上述Project客体的全部操作权限。 |
| Table | Describe | 读取Table的元信息。 |
| Table | Select | 读取Table的数据。 |
| Table | Alter | 修改Table的元信息，添加删除分区。 |
| Table | Update | 覆盖或添加Table的数据。 |
| Table | Drop | 删除Table。 |
| Table | All | 具备上述Table客体的全部操作权限。 |
| Function | Read | 读取及执行权限。 |
| Function | Write | 更新。 |
| Function | Delete | 删除。 |
| Function | All | 具备上述Function客体的全部操作权限。 |
| Resource,Instance,Jo b,Volume | Read | 读取。 |
| Resource,Instance,Jo b,Volume | Write | 更新。 |
| Resource,Instance,Jo b,Volume | Delete | 删除。 |
| Resource,Instance,Jo b,Volume | All | 具备上述Resource,Instance,Job,Volume客体的全部操作权限。 |

**说明**

上述权限描述中，Project类型对象的CreateTable权限操作和Table类型对象的Select、Alter、Update以及Drop权限操作均需要与Project对象的 CreateInstance权限操作配合使用，单独使用上述几种权限而没有指派CreateInstance权限是无法完成对应操作的。

**授权命令**

**使用场景**：在添加用户或创建角色之后，需要对用户或角色进行授权。MaxCompute ACL授权是一种基于对象的授权，通过授权的权限数据（即访问控制列
表，Access Control List）被看作是该对象的一种子资源，只有当对象已经存在时，才能进行授权操作。当对象被删除时，通过授权的权限数据会被自动删除。
**授权方式**：MaxCompute ACL支持的授权方法是采用类似SQL92定义的GRANT/REVOKE命令进行授权。通过对应的授权命令来完成对已存在的项目空间对象的授
权或撤销授权。

**命令格式**

```
GRANT actions ON object TO subject REVOKE actions ON object FROM subject actions ::= action_item1, action_item2, ... object ::= project project_name | TABLE schema_name | instance inst_name | FUNCTION func_name | resource res_name subject ::= USER full_username | role role_name
```

**说明**

MaxCompute ACL的授权命令并不支持[WITH GRANT OPTION]授权参数。即当用户A授权用户B访问某个对象时，用户B无法将权限进一步授权给用户C。因此，所有的授权操作都必须由具有如下三种身份之一的用户完成： 项目空间Owner。 项目空间中拥有Admin角色的用户。 项目空间中对象的创建者。

**操作示例**

项目管理员可以为组织云账号（RAM主账号）、任务云账号（RAM主账号）或本组织的子账号（RAM子账号）授权。

**说明**

添加其他组织的子账号需要先把其他组织云账号加入项目，再由其组织云账号添加。 场景一：假设 `ali***@aliyun.com` 是项目 `test_project_a` 的新成员，项目管理员可执行以下命令，授予用户提交作业、创建数据表及查看项目已有对象的权限。 `--`打开项目。

```
USE test_project_a;
```

`--`添加用户。

```
ADD USER aliyun$ali***@aliyun.com;
```

`--`创建角色`worker`。

```
CREATE role worker;
```

`--`将角色`worker`指派给用户。

```
GRANT worker TO aliyun$ali***@aliyun.com;
```

`--`授权方式一：为角色`worker`授予项目`test_project_a`中创建实例、创建资源、创建函数、创建表以及查看项目所有对象类型的权限。

```
GRANT CreateInstance, CreateResource, CreateFunction, CreateTable, List ON PROJECT test_project_a TO ROLE worker;
```

`--`授权方式二：为角色`worker`授予实例的所有权限。

```
GRANT ALL ON instance instance_name TO Role worker;
```

| 场景二：假设Allen是从属于 | ali***@aliyun.com | 的RAM子账号。项目管理员可执行以下命令为该组织云账号下的子账号（RAM USER）授权。 |
|---|---|---|
| --添加RAM子账号。 ADD USER ram$ali***@aliyun.com:Allen; --创建角色worker。 CREATE role worker; --将角色worker指派给用户。 GRANT worker TO ram$ali***@aliyun.com:Allen; |  |  |

#### 12.4.5. 权限查看

MaxCompute支持从多种维度查看权限，本文介绍如何查看指定用户、指定角色的权限以及查看指定对象的授权列表。

**查看指定用户的权限**

`--` 查看当前用户自己的访问权限。

```
SHOW grants;
```

`--` 查看指定用户的访问权限，仅`Project Owner`和`Admin`可以操作。

```
SHOW grants FOR <username>;
```

**查看指定角色的权限**

`--` 查看指定角色的访问权限角色指派。

```
DESCRIBE role <rolename>;
```

**查看指定对象的授权列表**

`--` 查看指定对象上的用户和角色授权列表。

```
SHOW acl FOR <objectName> [ON type <objectType>]
```

**说明**

当省略[on type <objectType>]时，默认的Type为Table。

**展现权限**

在展现用户权限或角色权限时，MaxCompute使用了如下的标记字符，它们的含义如下： A：表示Allow，即允许访问。 D：表示Deny，即拒绝访问。 C：表示with Condition，即为带条件的授权，只出现在Policy授权体系中，详细信息请参见条件块结构。 G：表示With Grant Option，即可以对Object进行授权。 展现权限的示例如下。

```
odps@test_project> SHOW grants FOR aliyun$odpstest1***@aliyun.com; [roles] dev Authorization Type: ACL [role/dev] A projects/test_project/tables/t1: Select [user/odpstest1***@aliyun.com] A projects/test_project: CreateTable | CreateInstance | CreateFunction | List A projects/test_project/tables/t1: Describe | Select Authorization Type: Policy [role/dev] AC projects/test_project/tables/test_*: Describe DC projects/test_project/tables/alifinance_*: Select [user/odpstest1***@aliyun.com] A projects/test_project: Create* | List AC projects/test_project/tables/alipay_*: Describe | Select Authorization Type: ObjectCreator AG projects/test_project/tables/t6: All AG projects/test_project/tables/t7: All
```

#### 12.4.6. Download权限控制

MaxCompute支持通过Download权限控制方案，对角色或用户使用Tunnel下载表和实例的行为进行管控，提升项目数据安全性，避免出现数据泄露情况。本文介绍 MaxCompute支持的Download授权命令，并提供授权示例供您参考。

**背景信息**

在MaxCompute项目中，您可以通过MaxCompute Tunner下载表和实例，但由于下载操作存在数据泄露安全风险，需要对该操作权限进行限制。 创建MaxCompute项目后，Download权限控制功能开关默认为关闭状态，表示不使用Download权限控制功能，即项目中的所有用户或角色对所有表或实例都有 Download权限。项目所有者（Project owner）或具备Super_Administrator角色的用户可以在MaxCompute项目的Project级别，执行 `setproject` odps.security.enabledownloadprivilege=true|false; 命令，开启或关闭Download权限控制功能。

| 场景 | 说明 |
|---|---|
| 为用户授权 | 为单个用户授予允许下载指定表数据或实例的权限。 |
| 基于角色为用户授权 | 为单个角色，授予允许下载指定表数据或实例的权限，然后将角色绑定至多个用户，用户即可具备角色的权限。 |

**前提条件**

被授权人的账号或角色名称，且账号或角色已添加至MaxCompute项目。 授权对象类型及对象名称。 您可以通过执行 SHOW tables; 、 LIST resources; 、 LIST functions; 或 SHOW instances; 命令获取表或视图名称及实例名称。

**使用限制**

只支持对已存在的对象、被授权人进行授权。 只支持将具体对象的Download权限授予用户，不支持通过通配符为用户授权。如果需要使用通配符，可以通过角色进行授权。

**注意事项**

如果删除了对象，MaxCompute会自动撤销与该对象关联的所有Download授权信息。 当一个用户被移除后，与该用户有关的授权仍然会被保留。一旦该用户以后被再次添加到该项目时，该用户的历史授权访问权限将被重新激活。

**命令格式**

Download授权

```
GRANT Download ON <object_type> <object_name> TO <subject_type> <subject_name>;
```

撤销Download授权

```
REVOKE Download ON <object_type> <object_name> FROM <subject_type> <subject_name>;
```

参数说明如下。

| 参数名称 | 是否必填 | 说明 |
|---|---|---|
| objecttype _ | 是 | 指定被授予的对象类型，即客体。单次授权只能指定一个客体。 支持的客体取值如下： Table：表。 Instance：实例。 |
| objectname _ | 是 | 指定被授予的对象的名称。获取方式如下： 表名称：您可以执行 SHOW tables; 命令获取表或视图名称。 实例名称：您可以执行 SHOW instances; 命令获取实例ID。 为角色授权时，授权对象支持以通配符星号（*）来表达。例如， table taobao* 表示所有以 taobao 开头的表。 |
| subjecttype _ | 是 | 指定被授权人的类型。 USER：阿里云账号或RAM用户。 ROLE：角色。 |
| subjectname _ | 是 | 指定被授权的用户账号或角色名称。单次授权只能指定一个用户或角色。 您可以执行 LIST users; 或 LIST roles; 命令获取用户账号或角色名称。 |

假设username***@example.com是test_project_a的项目所有者，Allen、Tom、Alice是隶属于username***@example.com的RAM用户。test_project_a项目开启了Download权限控制功能。以MaxCompute客户端操作为例，授权示例如下：

**示例一：为用户授予Download权限**

将用户Allen添加至test_project_a项目，并授予下载sale_detail表数据权限。命令示例如下。 `--Bob`进入项目`test_project_a`。

```
USE test_project_a;
```

`--`将用户`Allen`添加为项目成员。

```
ADD USER RAM$username***@example.com:Allen;
```

`--`支持用户`Allen`下载项目`test_project_a`中表`sale_detail`的数据。

```
GRANT Download ON TABLE sale_detail TO USER RAM$username***@example.com:Allen;
```

`--`查看用户`Allen`的授权结果。

```
SHOW grants FOR RAM$username***@example.com:Allen;
```

`--`授权结果如下。表明用户`Allen`已经具备`Download`权限。

```
Authorization Type: ACL [user/RAM$username***@example.com:Allen] A projects/test_project_a/tables/sale_detail: Download
```

**示例二：为用户撤销Download授权**

基于示例一，撤销对用户Allen的授权。 `--Bob`进入项目`test_project_a`。

```
USE test_project_a;
```

`--`撤销用户`Allen`授权。

```
REVOKE Download ON TABLE sale_detail FROM USER RAM$username***@example.com:Allen;
```

`--`查看用户`Allen`的撤销授权结果。权限列表无`Download`信息。

```
SHOW grants FOR RAM$username***@example.com:Allen;
```

**示例三：基于角色为多个用户授予Download权限**

为Alice、Tom授予在项目test_project_a中下载以tb_开头的表数据权限。命令示例如下。 `--Bob`进入项目`test_project_a`。

```
USE test_project_a;
```

`--`将用户`Alice`、`Tom`添加为项目成员。

```
ADD USER RAM$username***@example.com:Alice; ADD USER RAM$username***@example.com:Tom;
```

`--`创建角色`Worker`。

```
CREATE role Worker;
```

`--`为用户绑定角色`Worker`。

```
GRANT Worker TO RAM$username***@example.com:Alice; GRANT Worker TO RAM$username***@example.com:Tom;
```

`--`支持角色`Worker`下载项目`test_project_a`中以`tb_`开头的表数据。

```
GRANT Download ON TABLE tb_* TO ROLE Worker;
```

`--`查看用户`Alice`的授权结果。

```
DESCRIBE role Worker;
```

`--`授权结果如下。A表示允许执行`Download`操作。

```
Authorization Type: Policy [role/worker] A projects/test_project_a/tables/tb_*: Download
```

**示例四：为多个用户撤销基于角色授予的Download权限**

基于示例三，撤销对用户Alice、Tom的授权。 `--Bob`进入项目`test_project_a`。

```
USE test_project_a;
```

`--`收回用户`Alice`、`Tom`绑定的角色`Worker`。

```
REVOKE Worker FROM RAM$username***@example.com:Alice; REVOKE Worker FROM RAM$username***@example.com:Tom;
```

`--`查看用户`Alice`的撤销授权结果。权限列表无`Download`信息。

```
SHOW grants FOR RAM$username***@example.com:Alice;
```

### 跨项目空间的资源分享

**12.5.1. 概述**

本文介绍跨项目空间资源分享机制，重点讲解如何通过Package进行资源授权与管理，实现跨项目空间的安全数据共享。

#### 使用说明

假设您是项目空间的Owner或管理员（Admin角色），有人需要申请访问您的项目空间资源。 如果申请人属于您的项目团队，此时建议您使用项目空间的用户与授权管理功能，详情请参见项目空间的用户及授权管理。 如果申请人并不属于您的项目团队，此时您可以使用基于Package的跨项目空间资源分享功能。 Package是一种跨项目空间共享数据及资源的机制，主要用于解决跨项目空间的用户授权问题。对于如下场景出现的问题，如果不使用Package，将无法有效的解决。 假设，Alifinance项目空间的成员若要访问Alipay项目空间的数据，此时需要Alipay项目空间管理员先将Alifinance项目空间中的用户添加到Alipay项目空间中，然后再分别对这些新加入的用户进行普通授权。但实际上，Alipay项目空间管理员出于安全因素的考虑，并不希望对Alifinance项目空间中的每个用户都进行授权管理，此时就需要有一种机制能够使Alifinance项目空间管理员能对许可的对象进行自主授权控制。 使用Package之后，Alipay项目空间管理员可以对Alifinance需要使用的对象进行打包授权（也就是创建一个Package），然后许可Alifinance项目空间可以安装这个Package。在Alifinance项目空间管理员安装Package之后，就可以自行管理Package是否需要进一步授权给自己项目空间下的用户。 Package的使用涉及到两个主体：Package创建者和Package使用者。Package创建者项目空间是资源提供方，它将需要分享的资源及其访问权限进行打包，然后许可Package使用方来安装使用。Package使用者项目空间是资源使用方，它在安装资源提供方发布的Package之后，便可以直接跨项目空间访问资源。 下面将分别介绍Package创建者和Package使用者所涉及的相关操作。

#### 12.5.2. Package使用方法

##### 12.5.2.1. Package创建者相关操作

本文提供Package创建者操作指南，涵盖创建、删除、资源管理及权限配置全流程，方便您掌握许可授予与撤销的核心方法，并快速查看Package详细信息以实现高效的数据共享管理。

**创建Package**

```
CREATE package <pkgname>;
```

**删除Package**

```
DELETE package <pkgname>;
```

**将需要分享的资源添加到Package**

```
ADD project_object TO package package_name [WITH privileges <privileges>] remove project_object FROM package package_name project_object ::= TABLE table_name | instance inst_name | FUNCTION func_name | resource res_name privileges ::= action_item1, action_item2, ...
```

**说明**

目前支持的对象类型不包括Project类型，也就是不允许通过Package在其他Project中创建对象。 添加到Package中的不仅仅是对象本身，还包括相应的操作权限。当没有通过[with privileges privileges]来指定操作权限时，默认为只读权限，即 Read/Describe/Select。**对象及其权限**被看作一个整体，Package内的资源可以添加和删除，一旦添加和删除后原先授予的权限也会被回收掉。

**许可其他项目空间使用Package**

```
allow project <prjname> TO install package <pkgname> [USING label <number>];
```

**撤销其他项目空间使用Package的许可**

```
disallow project <prjname> TO install package <pkgname>;
```

**查看已创建和已安装的Package列表**

```
SHOW packages;
```

**查看Package详细信息**

```
DESCRIBE package <pkgname>;
```

##### 12.5.2.2. Package使用者相关操作

本文详解MaxCompute Package的全生命周期管理（安装、卸载、查看及权限配置），方便您基于ACL或Policy机制灵活设置Read权限，从而实现安全、可控的跨项目数据共享。

#### 使用说明

被安装的Package是一种独立的MaxCompute对象类型。如果要访问Package里的资源（即其他项目空间分享给您的资源），您必须拥有对该Package的Read权限。如果请求者没有Read权限，则需要向Project Owner或Admin申请。Project Owner或Admin可以通过ACL授权或Policy授权机制来完成。 例如，如下的ACL授权允许云账号用户odps_test***@aliyun.com访问Package里的资源。

```
USE prj2 security install package prj1.testpkg GRANT read ON package prj1.testpackage TO USER aliyun$odps_test***@aliyun.com
```

如下的Policy授权允许项目空间prj2中的任何用户都可以访问Package里的资源。

```
USE prj2 install package prj1.testpkg put policy /tmp/policy.txt
```

/tmp/policy.txt内容如下。

```json
{
  "Version": "1",
  "Statement": [{
    "Effect":"Allow",
    "Principal":"*",
    "Action":"odps:Read",
    "Resource":"acs:odps:*:projects/prj2/packages/prj1.testpkg"
   }]
}
```

**安装Package**

```
install package <pkgname>;
```

**说明**

安装Package时，要求PkgName的格式为：<projectName>.<packageName>。

**卸载Package**

```
uninstall package <pkgname>;
```

**说明**

卸载Package时，要求PkgName的格式为：<projectName>.<packageName>。

**查看Package**

`--` 查看已创建和已安装的`Package`列表。

```
SHOW packages;
```

`--` 查看`Package`详细信息。

```
DESCRIBE package <pkgname>;
```

### 项目空间的数据保护

#### 12.6.1. 数据保护概述

#### 使用说明

在现实中，有一些公司（例如金融机构）对数据安全非常敏感，通常不允许员工将工作带回家，而只允许在公司内部进行操作，而且公司的所有电脑上的USB存储接口也都是禁用的。这样做的目的是禁止员工将敏感数据泄露出去。 因此，作为MaxCompute项目空间管理员，如果项目空间中的数据非常敏感，绝对不允许流出到其他项目空间中去，希望MaxCompute能将所有可能导致数据流出的操作禁止掉，则需要进行如下的相关设置及操作。

#### 12.6.2. 数据保护机制

#### 使用说明

MaxCompute提供的项目空间保护机制可以将所有可能导致数据流出的操作禁止掉。您只需要在其项目空间中完成如下配置，即可开启数据保护机制。

```
SET security.ProjectProtection=true;
```

`--` 设置`ProjectProtection`规则：数据只能流入，不能流出，外表不受限。 `--` 或者

```
SET security.ProjectProtection=true; SET project IDENTIFY_EXTERNAL_TABLE_WRITE_AS_DATALEAK=true;
```

`--` 在`ProjectProtection`为`true`的前提下，设置`Project`数据不能通过外部表方式流出，即不能通过外部表写入外部存储源。 设置ProjectProtection后，您的项目空间中的数据流向就会得到控制，即数据只能流入，不能流出。 默认情况下，ProjectProtection不会被设置，取值为False。同时在多个项目空间中拥有访问权限的用户，可以自由地使用任意支持跨项目空间的数据访问操作来转移项目空间的数据。如果对项目空间中的数据高度敏感，则需要管理员自行设置ProjectProtection保护机制。

#### 12.6.3. 开启数据保护后的数据流出方法

本文为您介绍MaxCompute项目空间开启数据保护后，可以使用的数据流出方法。

#### 使用说明

在您的项目空间被设置了ProjectProtection之后，您可能很快就会遇到这样的需求：Alice向您提出申请，其需要将某张表的数据导出您的项目空间。而且经过您的审查之后，这张表的确没有泄露您关心的敏感数据。为了不影响Alice的正常业务需要，MaxCompute为您提供了在ProjectProtection被设置之后的两种数据导出途径。

**设置ExceptionPolicy**

Project Owner在设置ProjectProtection时可以附带一个Exception策略，命令如下。

```
SET ProjectProtection=true WITH exception <policyFile>;
```

**说明**

上述这种Policy不同于Policy授权（尽管它与Policy授权语法完全一样），它只是对项目空间保护机制的例外情况的一种描述，即所有符合Policy中所描述的访问都可以打破ProjectProtection规则。

**ExceptionPolicy示例**

假设，允许云账号Alice***@aliyun.com可以通过SQL任务对表alipay.table_test执行Select操作时，将数据流出到alipay项目空间之外。

```json
{ "Version": "1", "Statement": [{
    "Effect":"Allow",
    "Principal":"ALIYUN$Alice***@aliyun.com",
    "Action":["odps:Select"],
    "Resource":"acs:odps:*:projects/alipay/tables/table_test",
    "Condition":{
      "StringEquals": {
          "odps:TaskType":["DT", "SQL"]
      }
    }
  }]
}
```

**说明**

ExceptionPolicy并不是一种普通的授权。如果云账号Alice并没有对表alipay.table_test的Select操作权限，即使设置了上述ExceptionPolicy，Alice仍然是无法导出数据。ProjectProtection是一种数据流向的控制，而不是访问控制。只有在您能访问数据的前提下，控制数据流向才是有意义的。 TOC2TOU（time-of-check to time-of-use）数据泄露问题（又称Race Condition问题）。问题描述如下： i. [TOC阶段]用户A向Project Owner申请将t1导出，Project Owner对t1的数据敏感程度进行评估，PASS后通过ExceptionPolicy授权A可以导出t1。 ii. 恶意用户修改了t1的内容，将敏感数据写入到t1。 iii. [TOU阶段]用户A将t1的内容导出。此时导出的t1已经不是Project Owner审查的那个t1了。 防止TOC2TOU问题的建议：对于申请导出的表，Project Owner需要确保没有任何其他用户（含Admin）能对该表进行更新（Update）操作或重建同名表操作（Drop + CreateTable）。对于TOC2TOU问题描述中的场景，建议Project Owner在第一步中以Project Owner身份创建t1的一个Snapshot， 设置ExceptionPolicy时使用这个Snapshot，并且不要授予Admin角色给任何用户。

**设置TrustedProject**

如果当前项目空间处于受保护状态，如果将数据流出的目标空间设置为当前空间的TrustedProject，那么向目标项目空间的数据流向将不会被视为触犯 ProjectProtection规则。如果多个项目空间之间互相设置为TrustedProject，那么这些项目空间就形成了一个TrustedProject Group，数据可以在这个Project Group内流动，但禁止流出到Project Group之外。 管理TrustedProject的命令如下。 `--` 查看当前`Project`中的所有`TrustedProjects`。

```
LIST trustedprojects;
```

`--` 在当前`Project`中添加一个`TrustedProject`。

```
ADD trustedproject <projectname>;
```

`--` 在当前`Project`中移除一个`TrustedProject`。

```
REMOVE trustedproject <projectname>;
```

#### 12.6.4. 资源分享与数据保护

#### 使用说明

在MaxCompute中，基于Package的资源分享机制与项目空间的数据保护机制是正交的两种安全机制，但在功能上却是相互制约的。 MaxCompute规定：资源分享优先于数据保护。即如果一个数据对象是通过资源分享方式授予其他项目空间的用户访问，那么该数据对象将不受ProjectProtection规则的限制。

**配置说明**

如果要防止数据从项目空间的流出，在设置ProjectProtection=True之后，还需检查如下配置： 确保没有添加TrustedProject，如果有设置，则需要评估可能的风险。 确保没有设置ExceptionPolicy，如果有设置，则需要评估可能的风险，尤其要考虑TOC2TOU数据泄露风险。 确保没有使用Package数据分享，如果有设置，则需要确保Package中没有敏感数据。

### 项目空间的安全配置

MaxCompute项目空间支持灵活的安全配置，以满足不同租户的数据安全需求。本文介绍如何配置项目空间的安全性。

#### 使用说明

MaxCompute是一个支持多租户的数据处理平台，不同的租户对数据安全需求不尽相同。为了满足不同租户对数据安全的灵活需求，MaxCompute支持项目空间级别的安全配置，Project Owner可以定制适合自己的外部账号支持和鉴权模型。

**配置说明**

MaxCompute支持了多种正交的授权机制，例如ACL授权、Policy授权以及隐式授权（例如对象创建者自动被赋予访问对象的权限）。但是并非所有用户都需要使用这些安全机制。您可以根据自己的业务安全需求或使用习惯，合理设置本项目空间的鉴权模型。

```
SHOW SecurityConfiguration; SET security.CheckPermissionUsingACL=true/false; SET security.CheckPermissionUsingPolicy=true/false;
```

`--` 允许/禁止对象创建者默认拥有访问权限，默认为`true`。

```
SET security.ObjectCreatorHasAccessPermission=true/false;
```

`--` 允许/禁止对象创建者默认拥有授权权限，默认为`true`。

```
SET security.ObjectCreatorHasGrantPermission=true/false;
```

`--` 开启/关闭`LabelSecurity`安全策略。

```
SET security.LabelSecurity=true/false; SET security.ProjectProtection=true/false;
```

### Policy权限策略

#### 12.8.1. Policy概况

MaxCompute支持通过自定义访问策略语言进行授权管理，适用于复杂授权场景和条件限制。本文介绍Policy授权机制的使用方法，包括基于主体的授权、Policy类型、操作命令及修改流程。

#### 使用说明

Policy授权是一种基于主体的授权。通过Policy授权的权限数据（即访问策略）被看作是授权主体的一种子资源。只有当主体（用户或角色）存在时，才能进行 Policy授权操作。当主体被删除时，通过Policy授权的权限数据会被自动删除。Policy授权使用MaxCompute自定义的一种访问策略语言来进行授权，允许或禁止主体对项目空间对象的访问权限。 Policy授权是一种新的授权机制，它主要解决ACL授权机制无法解决的一些复杂授权场景，例如： 单次操作对一组对象进行授权，例如所有的函数或所有以**taobao**开头的表。 带限制条件的授权，例如只会在指定的时段内授权才会生效、当请求者从指定的IP地址发起请求时授权才会生效或者只允许用户使用SQL（而不允许其它类型的 Task）来访问某张表。 每种Policy只支持一个Policy文件。由于Put Policy操作会覆盖已有的Policy，当您需要修改Policy时，应按如下顺序分步操作：
1. 进行Get Policy操作。
2. 合并现有与待更新的Statements，生成完整的新版Policy。
3. 进行Put Policy操作。
`--` 读取项目空间的`Policy`。

```
GET POLICY;
```

`--` 设置（覆盖）项目空间的`Policy`。

```
PUT POLICY <policyFile>;
```

`--` 读取项目空间中某个角色的`Policy`。

```
GET POLICY ON ROLE <roleName>;
```

`--` 设置（覆盖）项目空间中某个角色的`Policy`。

```
PUT POLICY <policyFile> ON ROLE <roleName>;
```

**说明**

MaxCompute目前支持的Policy类型有**Project Policy**和**Role Policy**，暂不支持**User Policy**。**Project Policy**对Project中的所有用户有效，而**Role**
**Policy**只对已赋予角色的用户有效。在Policy格式上，**Project Policy**必须指定Principal（用户），而**Role Policy**则不能指定Principal（因为用户与角色的
指派关系已经存在）。

**说明**

场景说明：授权用户alice***@aliyun.com只能在**2019-11-11 23:59:59**这个时间点之前，只能从**10.32.180.0~23**这个IP段提交请求，只允许在项目空间 test_project中执行CreateInstance、CreateTable和List操作，禁止删除test_project下的任何表。

```json
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "ALIYUN$alice***@aliyun.com",
      "Action": [
        "odps:CreateTable",
        "odps:CreateInstance",
        "odps:List"
```

`],`

```json
      "Resource": "acs:odps:*:projects/test_project",
      "Condition": {
        "DateLessThan": {
          "acs:CurrentTime": "2019-11-11T23:59:59Z"
        },
        "IpAddress": {
          "acs:SourceIp": "10.32.180.0/23"
        }
      }
    },
    {
      "Effect": "Deny",
      "Principal": "ALIYUN$alice***@aliyun.com",
      "Action": "odps:Drop",
      "Resource": "acs:odps:*:projects/test_project/tables/*"
    }
```

]

```
}
```

#### 12.8.2. Policy基本术语

本文介绍Policy中的基本术语，包括权限、访问策略及其相关元素，如主体、操作、资源、访问限制和效力。

**权限**

权限（Permission）是访问控制的一个基本概念，它表示允许或拒绝一个请求者（Requester）对资源（Resource）执行某种操作（Action）。用语句 （Statement）来表示单个权限的形式化描述，而用策略（Policy）来表示语句的集合。

**访问策略**

访问策略（Access Policy）主要包括如下的访问控制元素：主体（Principal）、操作（Action）、资源（Resource）、访问限制（Access Restriction）和效力 （Effect）。下面分别对这几个基本实体进行简要描述。

**主体（Principal）**

主体（Principal）是指访问策略中的权限被指派的对象。例如，访问策略允许张三在2019年12月31日之前对资源SampleBucket执行CreateObject操作中的主体是张三。

**操作（Action）**

操作（Action）是指主体对资源的访问方法。例如，访问策略允许张三在2019年12月31日之前对资源SampleBucket执行CreateObject操作中的操作是 CreateObject。

**资源（Resource）**

资源（Resource）是指主体请求访问的对象。例如，访问策略允许张三在2019年12月31日之前对资源SampleBucket执行CreateObject操作中的资源是 SampleBucket。

**访问限制（Access Restriction）**

访问限制（Access Restriction）是指权限生效的限制条件。例如，访问策略允许张三在2019年12月31日之前对资源SampleBucket执行CreateObject操作中的限制条件是在2019年12月31日之前。

**效力（Effect）**

授权效力包括两个方面：允许操作（Allow）和拒绝操作（Deny）。通常，Deny有更高的效力，在权限检查时会优先使用。

**重要**

拒绝操作和撤销授权是完全独立的两个概念，撤销授权通常包括撤销对Allow和Deny这两种不同效力的授权。例如传统数据库通常支持Revoke和Revoke Deny 两种操作。

#### 12.8.3. 访问策略语言结构

##### 12.8.3.1. 访问策略语言结构概述

**访问策略结构说明**

下图描述了访问策略的基本结构，一个策略（Policy）由如下部分组成： 可选的策略头部元素。 一条或多条语句（Statement）。

**说明**

策略头部元素是可选的，它主要包括策略的版本信息。策略的主体是语句的集合。

**Policy结构图**

**Condition1**

**Block1**

**Condition2**

Condition Block

**Block**

**Condition3**

**Block2**

**策略头**

策略头

**Effect**

Effect

##### 12.8.3.2. 授权语句（Statement）结构

本文介绍Policy授权访问策略中的授权语句结构，包括Effect、Principal、Action、Resource和Condition Block等条目，帮助用户更有效地管理权限。

**授权语句结构**

一条授权语句（Statement）包括如下条目信息：

| 条目 | 说明 |
|---|---|
| Effect | 指明该条语句的权限类型，取值必须为 Allow 或 Deny 。 |
| Principal | 如果Policy在授权时是与用户或角色绑定，那么就不允许再指定Principal，例如MaxCompute的Role Policy。如果Policy在授权时是与项目空间或项目空间内的对象绑定，那么必须指定Principal，例如MaxCompute的Project Policy。 |
| Action | 表示授权操作，可以是一个或多个操作名，可支持通配符号 * 和 ? 。例如， Action = * 表示所有的操作。 |
| Resource | 表示授权对象，可以是一个或多个对象名，可支持通配符号 * 和 ? 。例如， Resource = * 表示所有的对象。 |
| Condition Block | 条件块是该条授权语句所述权限得以生效的条件。 |

##### 12.8.3.3. 条件块结构

本文介绍Policy授权语句中的条件块结构及其满足性判断原则，帮助您理解条件子句的组成和判断逻辑。

#### 使用说明

条件块由一个或多个条件子句构成，一个条件子句由条件操作类型、条件关键字和条件值组成。条件操作类型和条件关键字在下面的章节中会有详细描述。 条件块的满足性判断原则如下所示： 一个条件关键字可以指定一个或多个值，在条件检查时，如果条件关键字的值与指定值中的某一个相等，即可判定条件满足。 同一种条件操作类型的条件子句下的多个条件关键字同时满足的情况下，才能判定该条件子句满足。 条件块下的所有条件子句同时满足的情况下，才能判定该条件块满足。

##### 12.8.3.4. 条件操作类型

本文介绍Policy条件子句中字符串、数字、日期、布尔和IP地址类型的条件操作，帮助您理解各类型支持的方法。

**条件操作支持的方法**

| 条件操作类型 | 支持的方法 |
|---|---|
| STRING | StringEquals StringNotEquals StringEqualsIgnoreCase StringNotEqualsIgnoreCase StringLike StringNotLike |
| Numeric | NumericEquals NumericNotEquals NumericLessThan NumericLessThanEquals NumericGreaterThan NumericGreaterThanEquals |
| Date and Time | DateEquals DateNotEquals DateLessThan DateLessThanEquals DateGreaterThan DateGreaterThanEquals |
| BOOLEAN | Bool |
| IP Address | IpAddress NotIpAddress |

##### 12.8.3.5. 条件关键字

本文介绍MaxCompute支持的开放云服务ACS保留条件关键字，方便您在Policy条件子句中正确使用这些关键字。 MaxCompute支持开放云服务ACS（Aliyun Cloud Service）保留了如下条件关键字。

| ACS保留条件关键字 | 类型 | 说明 |
|---|---|---|
| acs:CurrentTime | Date and Time | Web Server接收到请求的时间。以ISO 8601格式表示，例如 2019-11-11T23:59:59Z 。 |
| acs:SecureTransport | BOOLEAN | 发送请求是否使用了安全信道，例如HTTPS。 |
| acs:SourceIp | IP Address | 发送请求时的客户端IP地址。 |
| acs:UserAgent | STRING | 发送请求时的客户端UserAgent。 |
| acs:Referer | STRING | 发送请求时的HTTP Referer。 |

**说明**

**acs:SourceIp**是指HTTP Connection的Remote_ip，而不是HTTP Header中的x-forwarded- for所指的IP List中的IP。
例如，如果 `10.230.205.105` 是一个局域网IP，**acs:SourceIp**则为该网络的网关出口IP。如果该网络出口使用了代理服务器，则**acs:SourceIp**为该代理服务器IP；如果有多级代理服务器，则为最后一级代理服务器IP。如果代理服务器设置的代理规则不同，则对**acs:SourceIp**的值也有影响。

#### 12.8.4. 访问策略语言规范

##### 12.8.4.1. Principal命名规范

本文介绍Policy授权访问策略语言中Principal的命名规范，涵盖支持的身份类型和表示方法。

**Principal命名说明**

Principal是指请求发送者的身份。目前仅支持阿里云账号、域账号和淘宝账号的身份表示。对于云账号，可以支持ID或DisplayName的表示。具体示例如下：

```json
"Principal": "43274" "Principal": "ALIYUN$bob***@aliyun.com" "Principal": ["ALIYUN$bob***@aliyun.com","ALIYUN$jack***@aliyun.com", "TAOBAO$alice"]
```

##### 12.8.4.2. Resource命名规范

本文介绍Policy授权访问策略语言中MaxCompute资源的命名规范，包括命名格式 `acs:<service-name>:<namespace>:<relative-id>` 及其参数说明，方便您管理和访问资源。

**命名格式**

目前使用如下格式来命名MaxCompute所提供的资源。

```
acs:<service-name>:<namespace>:<relative-id>
```

**参数说明**

| 参数 | 说明 |
|---|---|
| acs | 保留的Resource头部。 |
| service-name | 云开放服务名称，如MaxCompute、OSS或Table Store等。 |
| namespace | 命名空间，用于资源隔离。如果以云账号ID来做资源隔离，则可以取值为云账号ID。如果不支持该项，可以使用通配符*来代替。 |
| relative-id | 与Service相关的资源描述部分，其语义由具体Service指定。该部分的格式描述支持类似于文件路径的树状结构。以 MaxCompute为例，relative-id的格式如下。 projects/<project_name>/<object_type>/<object_name> |

**Resource命名说明**

| Resource命名实例 | 说明 |
|---|---|
| * | 项目空间中的所有对象。 |

| projects/prj1/tables/t1 | 项目空间prj1中的t1表。 |
|---|---|
| projects/prj1/instances/* | 项目空间prj1中的所有的Instances。 |
| projects/prj1/tables/* | 项目空间prj1中的所有表。 |
| projects/prj1/tables/taobao* | 项目空间prj1中的所有以taobao开头的表。 |

##### 12.8.4.3. Action命名规范

本文详解MaxCompute Policy策略中Action的命名规范，涵盖服务与操作接口的格式要求及实例说明。

**命名格式**

```xml
<service-name>:<action-name>
```

**参数说明**

**service-name**：开放服务名称，例如MaxCompute、OSS或Table Store等。
**action-name**：Service相关的操作接口名称。

**Action命名说明**

| Action命名实例 | 说明 |
|---|---|
| * | 所有操作。 |
| odps:* | MaxCompute的所有操作。 |
| odps:CreateTable | MaxCompute的CreateTable操作。 |
| odps:Create* | MaxCompute的所有以Create开头的操作。 |

##### 12.8.4.4. Condition Keys命名规范

**开放云服务ACS**

```
acs:<condition-key>
```

参数说明： `condition-key` ，ACS保留了5种条件关键字，所有的开放服务可以共用。 5种条件关键字分别是：

```
 acs:CurrentTime
 acs:SecureTransport
 acs:SourceIp
 acs:UserAgent
 acs:Referer
```

**其他服务**

```xml
<service-name>:<condition-key>
```

##### 12.8.4.5. 访问策略样例

Policy权限访问策略支持灵活的用户权限管理。通过定义JSON格式的策略示例，用户可控制操作权限、资源范围及条件限制。本文介绍Policy权限访问策略的参考示例。

**Policy Sample示例**

```json
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "ALIYUN$alice***@aliyun.com",
      "Action": [
        "odps:CreateTable",
        "odps:CreateInstance",
        "odps:List"
```

`],`

```json
      "Resource": "acs:odps:*:projects/prj1",
      "Condition": {
        "DateLessThan": {
          "acs:CurrentTime": "2019-11-11T23:59:59Z"
        },
        "IpAddress": {
          "acs:SourceIp": "10.32.180.0/23"
        }
      }
    },
    {
      "Effect": "Deny",
      "Principal": "ALIYUN$alice***@aliyun.com",
      "Action": "odps:Drop",
      "Resource": "acs:odps:*:projects/prj1/tables/*"
    }
```

]

```
}
```

**说明**

授权用户 `alice***@aliyun.com` 只能在 `2019-11-11T23:59:59Z` 这个时间点之前，只能从 `10.32.180.0/23` 这个IP段提交请求，只允许在项目空间 `prj1` 中执行 `CreateInstance` 、 `CreateTable` 和 `List` 操作，禁止删除 `prj1` 下的任何Table。

#### 12.8.5. Policy与ACL的区别

本文为您详解MaxCompute中Policy授权与ACL授权的核心区别，助您根据业务场景选择最合适的权限管理策略。 授权或撤销授权时，要求Grantee（例如User或Role）和Object（例如Table）必须已经存在。这点与Oracle授权特性相似，可以避免删除并重建同名对象所带来的安全风险。 删除一个对象时，自动撤销与该对象关联的所有授权。 仅支持Allow（白名单）授权，不支持Deny（黑名单）授权。 使用经典的Grant/Revoke授权命令进行授权。命令简单，使用时不易出错。不支持带限制条件的授权。 适用于简单的授权需求：授权不带限制条件，不需要Deny，并只需要对已存在对象进行授权。 授权或撤销授权时，不关心Grantee或Object存在与否。授权对象可以支持以通配符 * 来表达，例如 `projects/tbproj/tables/taobao*` ，它表示项目空间 tbproj中所有以taobao开头的表。这点与MySQL授权特性相似，它允许对不存在的对象授权，授权者应考虑到删除并重建同名对象所带来的安全风险。 同时支持Allow（白名单）和Deny（黑名单）授权。当Allow和Deny授权同时存在时，遵循Deny优先原则。 支持带限制条件的授权。授权者可以对Allow或Deny授权施加条件限制（目前支持20种条件操作）。例如，允许请求者的IP为指定的IP地址范围，同时访问时间必须在指定时间之前。 适用于相对复杂的授权需求：带授权限制条件，有Deny授权需求，希望支持对未来的对象授权。

#### 12.8.6. 应用限制

**应用限制说明**

| 名称 | 说明 | 限制数 |
|---|---|---|
| ACCESS_POLICY_SIZE_LIMIT | AccessPolicy的文本长度限制。 | 32 KB |
| USER_NUMBER_LIMIT_IN_ONE_PROJECT | 项目空间允许添加的最大用户数量。 | 1000 |
| ROLE_NUMBER_LIMIT_IN_ONE_PROJECT | 项目空间允许创建的最大角色数量。 | 500 |

| ROLE_NAME_LENGTH_LIMIT | 角色命名的字符长度。 | 64 Byte |
|---|---|---|
| SECURITY_COMMENT_SIZE_LIMIT | 注释的字符长度。 | 1 KB |
| PACKAGE_NAME_LENGTH_LIMIT | Package命名的字符长度。 | 128 Byte |
| ALLOW_PROJECT_NUMBER_LIMIT_IN_ONE_PACKAGE | 一个Package允许被多少Project安装。 | 1024 |
| RESOURCE_NUMBER_LIMIT_IN_ONE_PACKAGE | 一个Package允许包含的最大资源数量。 | 256 |
| PACKAGE_NUMBER_LIMIT_IN_ONE_PROJECT | 一个Project允许创建的Package数量。 | 512 |
| INSTALLED_PACKAGE_NUMBER_LIMIT_IN_ONE_PROJECT | 一个Project允许安装的Package数量。 | 64 |

### 安全相关语句汇总

### 12.9.1. 项目空间的安全配置

**鉴权配置**

| 语句 | 说明 |
|---|---|
| SHOW SecurityConfiguration; | 查看项目空间的安全配置。 |
| SET CheckPermissionUsingACL=true/false; | 激活或冻结ACL授权机制。 |
| SET CheckPermissionUsingPolicy=true/false; | 激活或冻结Policy授权机制。 |
| SET ObjectCreatorHasAccessPermission=true/false; | 允许或禁止对象创建者默认拥有访问权限。 |
| SET ObjectCreatorHasGrantPermission=true/false; | 允许或禁止对象创建者默认拥有ACL授权权限。 |

**数据保护**

| 语句 | 说明 |
|---|---|
| SET ProjectProtection=false; | 关闭数据保护机制。 |
| SET ProjectProtection=true [WITH exception <policy>]; | 开启数据保护机制。 |
| LIST TrustedProjects; | 查看可信项目空间列表。 |
| ADD TrustedProject <projectName>; | 添加可信项目空间。 |
| REMOVE TrustedProject <projectName>; | 移除可信项目空间。 |

#### 12.9.2. 项目空间的权限管理

#### 用户管理

| 语句 | 说明 |
|---|---|
| LIST users; | 查看所有已添加的用户。 |
| ADD USER <username>; | 添加一个用户。 |
| REMOVE USER <username>; | 移除一个用户。 |

#### 角色管理

| 语句 | 说明 |
|---|---|
| LIST roles; | 查看所有已创建的角色。 |
| CREATE role <rolename>; | 创建一个角色。 |
| DROP role <rolename>; | 删除一个角色。 |
| GRANT <rolelist> TO <username>; | 对用户指派一个或多个角色。 |
| REVOKE <rolelist> FROM <username>; | 撤销对用户的角色指派。 |

| 语句 | 说明 |
|---|---|
| GRANT <privList> ON <objType> <objName> TO USER <username>; | 对用户授权。 |
| GRANT <privList> ON <objType> <objName> TO role <rolename>; | 对角色授权。 |
| REVOKE <privList> ON <objType> <objName> FROM USER <username>; | 撤销对用户的授权。 |
| REVOKE <privList> ON <objType> <objName> FROM role <rolename>; | 撤销对角色的授权。 |

| 语句 | 说明 |
|---|---|
| GET policy; | 查看项目空间级别的Policy设置。 |
| PUT policy <policyFile>; | 设置项目空间级别的Policy。 |
| GET policy ON role <roleName>; | 查看某个角色的Policy设置。 |

| PUT policy <policyFile> ON role <roleName>; | 设置某个角色的Policy。 |
|---|---|

**权限审查**

| 语句 | 说明 |
|---|---|
| whoami; | 查看当前用户信息。 |
| SHOW grants [FOR <username>] [ON type <objectType>]; | 查看用户权限和角色。 |
| SHOW acl FOR <objectName> [ON type <objectType>]; | 查看具体对象的授权信息。 |
| DESCRIBE role <roleName>; | 查看角色的授权信息和角色指派。 |

#### 12.9.3. 基于Package的资源分享

本文介绍基于Package的资源分享中的相关语句，您可通过以下语句进行资源的分享与查看。

**分享资源**

| 语句 | 说明 |
|---|---|
| CREATE package <pkgName>; | 创建一个Package。 |
| DELETE package <pkgName>; | 删除一个Package。 |
| ADD <objType> <objName> TO package <pkgName> [WITH privileges privs]; | 向Package中添加需要分享的资源。 |
| REMOVE <objType> <objName> FROM package <pkgName>; | 从Package中移除无需分享的资源。 |
| allow project <prjName> TO install package <pkgName> [USING label <num>]; | 允许某个项目空间使用安装Package。 |
| disallow project <prjName> TO install package <pkgName>; | 禁止某个项目空间使用安装Package。 |

**使用资源**

| 语句 | 说明 |
|---|---|
| install package <pkgName>; | 安装Package。 |
| uninstall package <pkgName>; | 卸载Package。 |

**查看Package**

| 语句 | 说明 |
|---|---|

| SHOW packages; | 列出所有创建和安装的Package。 |
|---|---|
| DESCRIBE package <pkgName>; | 查看Package的详细信息。 |

## 常用工具

### MaxCompute客户端

## 13.1.1. 使用须知

#### 使用说明

请您不要依赖MaxCompute客户端的输出格式来做任何的解析工作。客户端的输出格式不承诺向前兼容，不同版本间的客户端命令格式及行为有差异。 MaxCompute客户端是一个Java程序，需要JRE环境才能运行，请下载并安装JRE1.8 版本。 您在开始配置客户端前，请确认已使用云账号创建项目空间，且已获取其****************和********************。

#### 13.1.2. 安装客户端

本文将指导您完成MaxCompute客户端的安装与运行，内容包括：下载解压、认证配置及启动验证。

**操作步骤**

1. 下载客户端压缩包到本地。
2. 将下载好的客户端压缩包解压到一个文件夹中，在该文件夹中可以看到如下4个文件夹。

```
bin/ conf/ lib/ plugins/
```

3. 编辑conf文件夹中的**odps_config.ini**文件，配置如下相关信息。
**配置模板**：

```
project_name=my_project access_id=******************* access_key=********************* end_point= <MaxCompute服务地址>
```

**参数说明**：
**access_id**和**access_key**是用户的云账号信息。其中，**access_id**对应****************，**access_key**对应********************。
**Project_name=my_project**的作用是指定您想进入的项目空间。一旦配置此项，每次登录客户端，将会默认进入到该项目空间。如果不配置，登录客户端
后，必须使用 `USE project_name` 命令进入项目空间。
**end_point**需要配置成MaxCompute提供给用户的服务地址。针对不同的用户，服务地址也不同。

**重要**

在安全方案允许的情况下，必须保证odpscmd和MaxCompute的end_point网络是互通的。
4. 修改好配置文件后，运行bin目录下的**odps**文件（在Linux 系统下运行./bin/odpscmd，在Windows下运行./bin/odpscmd.bat），此时就可以开始运行SQL语句
了，示例如下。

```
CREATE TABLE tbl1(id bigint); INSERT OVERWRITE TABLE tbl1 SELECT count(*) FROM tbl1; SELECT 'welcome to MaxCompute!' FROM tbl1;
```

#### 13.1.3. 配置及参数说明

**获取帮助**

显示客户端的帮助信息，命令格式如下。

```
odps@ >./bin/odpscmd -h;
```

**说明**

您也可以在交互模式下键入 h; 或 help; （不区分大小写）。

**启动参数**

在启动时，您可以指定一系列参数，命令格式如下。

```
Usage: odpscmd [OPTION]... where options include:
    --help (-h)for help
    --project= use project
    --endpoint= set endpoint
    -u  -p  user name and password
    -k  will skip begining queries and start from specified position
    -r  set retry times
    -f <"file_path;"> execute command in file
    -e <"command;[command;]..."> execute command, include sql command
    -C will display job counters
```

以**-f**参数为例，示例如下：
1. 准备本地脚本文件script.txt，假设在D盘，文件内容如下。

```
DROP TABLE if EXISTS test_table_mj; CREATE TABLE test_table_mj (id string, name string); DROP TABLE test_table_mj;
```

2. 运行如下命令。

```
odpscmd\bin>odpscmd -f d:/script.txt;
```

3. 显示执行结果。

```
ID = 20170528122432906gux77io3 Log view: http://webconsole.odps.aliyun-inc.com:8080/logview/?h=http://service-corp.odps.aliyun- inc.com/api&podps_public_dev&i2017052 8122432906 gux77io3&tokenRnlrSzJoL242YW43dFFIc1dmb1ZWZzFxQ1RFPSxPRFBTX09CTzoxMDcwMDI1NjI3ODA1 NjI5LDE0MzM0MjA2NzMseyJTdGF0ZW1lbnQiOlt7IkFjdGlvbiI6WyJvZHBzOlJlYWQiXSwiRWZmZWN0IjoiQWxsb3ciLCJSZXNvdXJjZSI6WyJhY3M6b2RwczoqOnB yb2plY3 RzL29kcHNfcHVibGljX2Rld i9pbnN0YW5jZXMvMjAxNTA1MjgxMjI0MzI5MDZndXg3N2lvMyJdfV0sIlZlcnNpb24iOiIxIn0=
```

`OK`

```
ID = 20170528122439318gcmkk6u1 Log view: http://webconsole.odps.aliyun-inc.com:8080/logview/?h=http://service-corp.odps.aliyun- inc.com/api&podps_public_dev&i2017052 8122439318 gcmkk6u1&tokendSt0RXdlV0M5YjZET2I1MnJuUFkzWDN1aWpzPSxPRFBTX09CTzoxMDcwMDI1NjI3ODA1NjI5LDE0MzM0MjA2ODAseyJTdGF0ZW1lbnQiOlt7IkFjdGlvbiI6WyJ zOlJlYWQiXSwiRWZmZWN0IjoiQWxsb3ciLCJSZXNvdXJjZSI6WyJhY3M6b2RwczoqOnB yb2plY3RzL29kcHNfcHVibGljX2Rld i9pbnN0YW5jZXMvMjAxNTA1MjgxMjI0MzkzMThnY21razZ1MSJdfV0sIlZlcnNpb24iOiIxIn0=
```

`OK`

```
ID = 20170528122440389g98cmlmf Log view: http://webconsole.odps.aliyun-inc.com:8080/logview/?h=http://service-corp.odps.aliyun- inc.com/api&podps_public_dev&i2017052 8122440389 g98cmlmf&tokenNWlwL0EvQThxUXhzcTRERDc5NFg0b2IxZ3QwPSxPRFBTX09CTzoxMDcwMDI1NjI3OD A1NjI5LDE0MzM0MjA2ODAseyJTdGF0ZW1lbnQiOlt7IkFjdGlvbiI6WyJvZHBzOlJlYWQiXSwiRWZmZWN0IjoiQWxsb3ciLCJSZXNvdXJjZSI6WyJhY3M6b2RwczoqOnB yb2pl Y3RzL29kcHNfcHVibGljX2Rld i9pbnN0YW5jZXMvMjAxNTA1MjgxMjI0NDAzODlnOThjbWxtZiJdfV0sIlZlcnNpb24iOiIxIn0=
```

`OK`

**交互模式**

直接运行客户端将进入到交互模式，命令格式如下。

```
[admin: ~]$odpscmd Aliyun ODPS Command Line Tool Version 1.0 @Copyright 2012 Alibaba Cloud Computing Co., Ltd. All rights reserved. XXX@ XXX> insert overwrite table dual select * from dual;
```

**说明**

上面的第一个XXX会显示MaxCompute的标识符，第二个XXX会显示您当前所在的项目空间。在光标位置输入命令（以分号作为语句结束标志），回车即可运行。

**输出信息**

提交SQL语句后的返回值有两种输出格式：HumanReadable格式（默认）和MachineReadable格式。如果您运行odpscmd时加了**-M**参数，则以CSV格式输出。

**说明**

**续跑**

在用**-e**或**-f**模式运行时，如果有多个语句，并且想从中间某个语句开始运行，可以指定参数**-k**，表示忽略前面的语句，从指定位置的语句开始运行。当指定参数小于等于0时，从第一条语句开始执行。每个以分号分隔的语句被视为一个有效语句，在运行时会打印出当前运行成功或者失败的是第几个语句。 例如文件/tmp/dual.sql中有如下三条SQL语句。

```
DROP TABLE dual; CREATE TABLE dual (dummy string); INSERT overwrite TABLE dual SELECT count(*) FROM dual;
```

想忽略前面两条语句，需要执行如下命令。

```
odpscmd -k 3 -f dual.sql
```

**获取当前登录用户**

获取当前登录用户云账号及使用的**end_point**配置，命令格式如下。

```
whoami
```

示例如下。

```
odps@ hiveut>whoami; Name: odpst***@aliyun.com ID: 109014***36588 End_Point: <MaxCompute服务地址> Project: lijunsecuritytest
```

**退出**

命令格式如下。

```
odps@ > quit;
```

或者

```
q;
```

**设置作业优先级**

命令格式如下。

```
Admin@ > ./bin/odpscmd --instance-priority=<PRIORITY>;
```

配置文件：odps_config.ini

| instance_priority=<PRIORITY> |  |
|---|---|
| 重要 <PRIORITY>：表示提交的MaxCompute（ODPS）作业实例的调度优先级。 在配置文件中配置后，对在CLT中提交的所有Instance有效。 您如果没有设置 PRIORITY ，优先级默认值为9。 |  |

**DryRun模式**

DryRun是指提交一个有效的SQL语句时，MaxCompute只分析其语法正确性，生成相应的执行计划，但是并不提交分布式作业即返回。命令格式如下。

```
./bin/odpscmd -y
```

**SQL可靠性**

在客户端中执行Insert或者Create Table AS等SQL语句时。如果作业执行过程中出现了异常，客户端会尽可能根据已知的信息将数据和元数据都自动恢复到执行SQL QUERY之前的状态，包括： Insert Overwrite在QUERY执行过程中覆盖的数据，会从临时备份目录中恢复到原目录。 Insert Into在QUERY执行过程中产生的新增数据，会全部删除。 QUERY执行过程中创建的表，或动态生成的原来不存在的分区信息，全部删除。 如果MaxCompute无法完成恢复过程，则会输出一个特定的出错码，告诉您不要再进行尝试，否则可能导致部分数据无法恢复。报错信息如下。

```
ODPS- 0110999: Critical! Internal error happened in commit operation and rollback failed, possible breach of atomicity
```

### Eclipse开发插件

#### 13.2.1. 安装Eclipse开发插件

**背景信息**

为了方便您使用MapReduce及UDF的Java SDK进行开发工作，MaxCompute提供了Eclipse开发插件。该插件能够模拟MapReduce及UDF的运行过程，为您提供本地调试手段，并提供简单的模板生成功能，工具的下载地址为Eclipse。

**说明**

与MapReduce提供的本地运行模式不同，Eclipse插件不能够与MaxCompute同步数据。您使用的数据需要手动拷贝到Eclipse插件的warehouse目录下。

**操作步骤**

1. 将Eclipse软件包解压。解压后将看到如下的JAR内容。
odps-eclipse-plugin-bundle-0.16.0.jar
2. 将插件放置在Eclipse安装目录的plugins子目录下。
3. 打开Eclipse，单击右上角的打开**透视图（****Open Perspective**）图标，页面如下图所示。
4. 在弹出的如下对话框中选择**ODPS**后单击**Open**。
5. 此时在右上角会出现
图标，表示插件生效，如下图所示。

#### 13.2.2. 创建工程

**操作步骤**

1. 您可选择以下方式中的任一方式创建工程。

**方式一**

在Eclipse左上角选择**File > New > ODPS Project**创建工程，如下图所示。

**方式二**

i. 在Eclipse中直接单击左上角的图标，如下图所示。 ii. 在弹出的对话框中，选择**ODPS Project**，如下图所示。
2. 创建ODPS工程后会出现如下图所示对话框。输入Project name（示例中使用odps作为工程名），选择MaxCompute客户端路径，单击**Finish**并确认。

**说明**

客户端需要提前安装。
3. 创建好工程后，在左侧的包资源管理器（Package Explorer）中可以看到如下图所示的目录结构。

#### 13.2.3. MapReduce运行示例

##### 13.2.3.1. 快速运行WordCount示例

本文为您提供在Eclipse开发插件中快速运行MapReduce的WordCount示例。

**操作步骤**

1. 选择MaxCompute项目中的WordCount示例，如下图所示。
2. 右键单击**WordCount.java**，依次选择**Run As > ODPS Mapreduce|Graph**，如下图所示。
3. 在弹出的对话框中，选择**example_project**，单击**Finish**，如下图所示。
4. 运行成功后，会出现结果提示，如下图所示。

##### 13.2.3.2. 运行自定义MapReduce程序

**操作步骤**

1. 在Eclipse中右键选择**src**目录，然后选择**New > Mapper**。
2. 选择Mapper后出现如下的对话框。输入Mapper类的名字，单击**Finish**。
3. 在左侧包资源管理器（Package Explorer）中，**src**目录下生成文件UserMapper.java。该文件的内容即是一个Mapper类的模板。将模板中Package名称默认配
置为odps，编写模板内容如下。

```java
package odps; import java.io.IOException; import com.aliyun.odps.counter.Counter; import com.aliyun.odps.data.Record; import com.aliyun.odps.mapred.MapperBase;
    Record word; Record one; Counter gCnt;
    @Override
    public void setup(TaskContext context) throws IOException {
        word = context.createMapOutputKeyRecord(); one = context.createMapOutputValueRecord(); one.set(new Object[] { 1L });
        gCnt = context.getCounter("MyCounters", "global_counts");
    }
    @Override
    public void map(long recordNum, Record record, TaskContext context) throws IOException {
        for (int i = 0; i < record.getColumnCount(); i++) {
            String[] words = record.get(i).toString().split("\\s+");
            for (String w : words) {
                word.set(new Object[] { w });
                Counter cnt = context.getCounter("MyCounters", "map_outputs"); cnt.increment(1);
                gCnt.increment(1); context.write(word, one);
            }
        }
    }
    @Override
    public void cleanup(TaskContext context) throws IOException {
    }
}
```

4. 在Eclipse中右键选择**src**目录，然后选择**New > Reducer**。
5. 在弹出的对话框中输入Reduce类的名字，单击**Finish**。
图2.Reducer

**说明**

本示例使用UserReducer。
6. 在左侧包资源管理器（Package Explorer）中，**src**目录下生成文件UserReducer.java。该文件的内容即是一个Reduce类的模板，将模板中Package名称默认配
置为odps，编写模板内容如下。

```java
package odps; import java.io.IOException; import java.util.Iterator; import com.aliyun.odps.counter.Counter; import com.aliyun.odps.data.Record; import com.aliyun.odps.mapred.ReducerBase; public class UserReducer extends ReducerBase {
    private Record result; Counter gCnt;
    @Override
    public void setup(TaskContext context) throws IOException {
        result = context.createOutputRecord();
        gCnt = context.getCounter("MyCounters", "global_counts");
    }
    @Override
    public void reduce(Record key, Iterator<Record> values, TaskContext context) throws IOException {
        long count = 0;
        while (values.hasNext()) {
            Record val = values.next(); count += (Long) val.get(0);
        }
        result.set(0, key.get(0)); result.set(1, count);
        Counter cnt = context.getCounter("MyCounters", "reduce_outputs"); cnt.increment(1);
        gCnt.increment(1);
        context.write(result);
    }
    @Override
    public void cleanup(TaskContext context) throws IOException {
    }
}
```

7. 在Eclipse中右键选择**src**目录，然后选择**New > MapReduce Driver**。
8. 选择MapReduce Driver后出现如下的对话框。输入Driver Name、Mapper及Reducer类，单击**Finish**。
9. 在左侧包资源管理器（Package Explorer）中，src目录下生成文件UserDriver.java。该文件的内容是一个MapReduce Driver的模板。将模板中Package名称默
认配置为odps，编写模板内容如下。

```java
package odps; import com.aliyun.odps.OdpsException; import com.aliyun.odps.data.TableInfo; import com.aliyun.odps.examples.mr.WordCount.SumCombiner; import com.aliyun.odps.examples.mr.WordCount.SumReducer; import com.aliyun.odps.examples.mr.WordCount.TokenizerMapper; import com.aliyun.odps.mapred.JobClient; import com.aliyun.odps.mapred.RunningJob; import com.aliyun.odps.mapred.conf.JobConf; import com.aliyun.odps.mapred.utils.InputUtils; import com.aliyun.odps.mapred.utils.OutputUtils; import com.aliyun.odps.mapred.utils.SchemaUtils; public class UserDriver {
    public static void main(String[] args) throws OdpsException {
        JobConf job = new JobConf();
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(SumCombiner.class);
        job.setReducerClass(SumReducer.class);
        job.setMapOutputKeySchema(SchemaUtils.fromString("word:string"));
        job.setMapOutputValueSchema(SchemaUtils.fromString("count:bigint"));
        InputUtils.addTable(TableInfo.builder().tableName("wc_in1").cols(new String[] { "col2", "col3" }).build(), job);
        InputUtils.addTable(TableInfo.builder().tableName("wc_in2").partSpec("p1=2/p2=1").build(), job);
        OutputUtils.addTable(TableInfo.builder().tableName("wc_out").build(), job);
        RunningJob rj = JobClient.runJob(job); rj.waitForCompletion();
    }
}
```

0. 运行MapReduce程序，选中UserDriver.java，右键选择**Run As > ODPS MapReduce|Graph**。出现如下图所示对话框。
1. 选择ODPS Project为**example_project**，单击**Finish**开始本地运行MapReduce程序，有如下图所示的输出信息，说明本地运行成功。
图5.Console
2. 运行的输出结果在warehouse目录下，刷新MaxCompute工程即可显示，如下图所示。
图6.输出结果

**说明**

**wc_out**是输出目录，**R_000000**是结果文件。通过本地调试，确定输出结果正确后，可以通过Eclipse导出（Export）功能将MapReduce打包，供后续分布
式环境使用。
3. 导出步骤如下所示。
i. 选择**src**目录，单击**Export**，如下图所示。 图7.导出文件步骤1 ii. 选择导出模式为 `JAR file` ，如下图所示。 图8.导出文件步骤2 iii. 仅需要导出**src**目录下的Package（com.aliyun.odps.mapred.open.example），JAR文件名称指定为mr-examples.jar，如下图所示。 图9.导出文件步骤3

**说明**

在本示例中，将程序包命名为**mr-examples.jar**，实际操作时可根据您的实际需求而定。 iv. 确认后，单击**Finish**进行导出。
4. 如果您想在本地模拟新建Project，可以在warehouse下面，创建一个新的子目录（与example_project平级的目录），目录层次结构如下图所示。
Schema文件示例如下。

```
project=project_name table=table_name columns=col1:BIGINT,col2:DOUBLE,col3:BOOLEAN,col4:DATETIME,col5:STRING
```

`--` 非分区表

```
project=project_name table=table_name columns=col1:BIGINT,col2:DOUBLE,col3:BOOLEAN,col4:DATETIME,col5:STRING partitions=col1:BIGINT,col2:DOUBLE,col3:BOOLEAN,col4:DATETIME,col5:STRING
```

`--` 分区表 `--` 注：当前支持5种数据格式：`BIGINT`、`DOUBLE`、`BOOLEAN`、`DATETIME`和`STRING`，对应到`Java`中的数据类型为`LONG`、`DOUBLE`、`BOOLEAN`、`Java.Util.Date`和

```
Java.Lang.STRING。
```

Data文件示例如下。

```
1,1.1,true,2015-06-04 11:22:42 896,hello world \N,\N,\N,\N,\N
```

`--` 注：时间格式精确到毫秒级别，所有类型用\N表示`NULL`。

**说明**

本地模式运行MapReduce程序，默认情况下先到Warehouse下查找相应的数据表或资源，如果表或资源不存在会到服务器上下载相应的数据存入warehouse目录下，再以本地模式运行。

#### 13.2.4. UDF开发运行示例

##### 13.2.4.1. Local Debug UDF程序

###### 13.2.4.1.1. 菜单栏运行

**操作步骤**

1. 从菜单栏选择**Run As > Run Configurations**，弹出如下图所示的对话框。
图 1. Run Configurations
2. 您可以新建一个**Run Configuration**，并选择运行的UDF类及类型、选择ODPS Project以及填写输入表信息，如下图所示。
图 2. Run Configurations 2

**说明**

上述配置中，Table表示UDF的输入表，Partitions表示读取某个分区下的数据，分区由逗号分隔，Columns表示列，将依次作为UDF函数的参数被传入，列名由逗号分隔。
3. 单击**Run**，运行结果将显示在控制台中，如下图所示。
图 3. Console

###### 13.2.4.1.2. 右键单击快速运行

**操作步骤**

1. 选中一个Java文件（例如：UDFExample.java）并单击鼠标右键，选择**Run As > ODPS UDF|UDAF|UDTF**，如下图所示。
2. 在弹出的对话框中，配置相关参数，配置信息如下图所示。

**说明**

上述配置中，Table表示UDF的输入表，Partitions表示读取某个分区下的数据，分区由逗号分隔，Columns表示列，将依次作为UDF 函数的参数被传入，列名由逗号分隔。
3. 单击**Finish**，运行UDF，获得输出结果。

##### 13.2.4.2. 运行自定义UDF程序

**操作步骤**

1. 右键单击一个工程并选择**New > UDF**（或者在菜单栏选择**File > New > UDF**）。填写UDF类名后单击**Finish**。在对应的**src**目录下生成与UDF类名同名的
Java文件，并编辑该Java文件，文件内容如下。

```java
package odps; import com.aliyun.odps.udf.UDF; public class UserUDF extends UDF { /**
* project: example_project
* table: wc_in1
* columns: col1,col2
```

* `*/`

```
public String evaluate(String a, String b) { return "ss2s:" + a + "," + b; } }
```

2. 右键选择该Java文件（如UserUDF.java），选择**Run As > ODPS UDF|UDTF|UDAF**，如下图所示。
图 1. 运行用户自定义UDF程序步骤1
3. 在弹出的对话框中，配置如下图所示的信息。
图 2. 运行用户自定义UDF程序步骤3-1
4. 单击**Finish**，获得输出结果。

```
ss2s:A1,A2 ss2s:A1,A2 ss2s:A1,A2 ss2s:A1,A2
```

**说明**

本示例中仅给出UDF的运行示例，UDTF的运行方式与UDF基本相同，不作特殊说明。

### Logview工具

#### 13.3.1. 使用Logview查看Job运行信息

本文介绍如何使用Logview工具查看Job运行信息，您可了解Job的执行状态、进度详情、运行结果及异常原因。

#### 使用说明

Logview是查看以及Debug已提交的MaxCompute Job的工具。通过Logview可看到一个Job的如下内容： 任务的运行状态。 任务的运行结果。 任务的细节和每个步骤的进度。

**说明**

Job提交到MaxCompute后，会生成一个以 `http://logview.odps.aliyun.com/logview` 开头的URL地址。您可以直接在浏览器上打开Logview链接，查看Job的信息。

**说明**

每个Job的Logview页面的有效期为一周。

**Logview功能组件**

下面将结合具体的Logview Web UI界面，为您介绍每个组件的含义。 Logview的首页分成上下两部分： Instance信息。 Task信息。

**Instance信息**

在Logview页面中，上半部分是您提交的SQL任务对应的MaxCompute Instance信息，包含URL链接、项目、InstanceID、提交人、开始时间、结束时间和状态 （Status）等。 Instance信息部分，您可以单击**Status**查看当前队列的Status详细信息，包含三种状态：
**Waiting**：说明当前作业正在MaxCompute中处理，并没有提交到分布式调度系统（Fuxi）中运行。
**Waiting List : n**：说明作业已提交至分布式调度系统（Fuxi）排队等待运行，当前在队列中处于第n位。
**Running**：作业在分布式调度系统（Fuxi）中运行。

**说明**

处于Terminated状态的Instance由于作业已处理完成，因此不存在队列信息。 单击Status查看队列详细信息：
**Sub Status**：表示当前子状态信息。
**WaitPos**：表示排队位置，如果是0表示正在运行，如果为-表示尚未到Fuxi。
**QueueLength**：表示Fuxi中总的队列长度。
**Total Priority**：表示作业运行时经过系统判断后授予的优先级。
**SubStatus History**：单击后，可以查看作业执行的详细历史状态，包含状态码、状态描述、开始时间、持续时间等（某些版本暂时无历史信息）。

**Task信息**

在Logview页面中，下半部分为该Instance对应的Task信息，包括任务名称、类型、状态、运行结果（Result）、详细信息（Detail）、开始时间、结束时间、总运行时间（Latency）和进度。其中，Latency指的是运行总共消耗的时间，与其他页面的Latency含义类似。
**Result**：在Job运行结束后，可以看到运行结果。例如一条SELECT SQL的结果，示例如下图所示。
**Detail**：一个Job在运行中和结束后，均可以单击**Detail**来查看任务运行的具体情况。
在MaxCompute Task详细信息对话框中，您可以查看以下信息： 一个MaxCompute Task可以由一个或多个Fuxi Job组成。例如，如果您提交的SQL任务较为复杂，MaxCompute将自动向分布式调度系统（Fuxi）提交多个 Fuxi Job。 每个Fuxi Job可以由一个或多个Fuxi Task组成。例如，简单的MapReduce任务通常会产生两个Fuxi Task，即Map Task（M1）和Reduce Task（R2）。而一个比较复杂的SQL任务也可能产生多个Fuxi Task。 查看所产生的Fuxi Task的任务名称。任务名称通常由字母和数字组成，其中字母表示任务类型（例如，M代表Map Task），数字标识任务编号以及依赖关系（例如，R5_4表示该Reduce Task需要J4任务执行结束后才会开始执行；J4_1_2_3则表示该Join Task需要M1、M2和M3这三个任务都执行完成后才会开始执行）。 I/O Records表示该Fuxi Task的输入和输出的记录数。 单击Fuxi Task最右侧的查看列中的按钮或双击该Fuxi Task，您可以查看该Fuxi Task对应的Instance信息。

**说明**

每个Fuxi Task由一个或多个Fuxi Instance组成。当Fuxi Task的输入数据量持续增大时，MaxCompute将自动为该Task启动更多的节点来处理数据，每个节点即对应一个Fuxi Instance。 在页面下方的Fuxi Instance信息部分，Logview将处于不同阶段的Instance进行分组展示。例如，您可以选择Failed组，查看运行出错的节点。同时，您可以单击 StdOut和StdErr列中的按钮查看标准输出信息和标准错误信息。

**说明**

您在所提交的MaxCompute任务中编写的打印信息也将在标准输出信息和标准错误信息中展示。

**使用Logview排查问题**

当有任务出错时，您可以在Logview页面的Result中看到错误的提示信息，也可以在Detail页面中通过Fuxi Instance的Stderr，查看具体某个Instance出错的信息。 例如数据倾斜，运行缓慢有时是由于在某个Fuxi Task中，有个别Instance形成了长尾。长尾的现象由同一个Task内任务分配不均导致。这时可以在任务运行完后，在 Summay标签页中看运行结果。在每个Task中都可以看到类似如下输出。

```
output records: R2_1_Stg1: 199998999 (min: 22552459, max: 177446540, avg: 99999499)
```

此处如果Min和Max值相差较大，不在一个数量级，说明在这一阶段出现了数据倾斜。例如，在执行字段Join时，某个字段中有一个值出现的比例很高，则在这一字段上执行Join就会出现数据倾斜。

#### 13.3.2. 使用Logview 2.0查看Job运行信息

Logview 2.0支持交互式DAG图、作业回放及结果导出，提升作业监控和调试效率。本文介绍Logview 2.0的主要功能和使用方法。

**概述**

Logview 2.0在Logview基础上，进行了全新的页面设计，优化了加载速度，并新增了如下功能： 支持以交互式DAG图展示作业处理逻辑架构，您还可以查看相应的Operation层级。 支持回放作业运行过程。

**入口**

您使用MaxCompute客户端（odpscmd）提交作业后，系统会自动生成一个以 `https://logview.aliyun.com/logview` 开头的URL地址。在搜索引擎中打开，即可进入Logview 2.0界面。 Logview 2.0界面如下。

| 序号 | 区域 |
|---|---|
| ① | 标题与功能区。 |
| ② | Basic Info。 |
| ③ | 作业详情。 |

**标题和功能区**

标题与功能区包含您提交MaxCompute作业时生成的唯一作业ID及您自定义的作业名称（通过SDK方式提交的作业包含作业名称信息）。您还可以执行如下操作。

| 图标 | 功能 |
|---|---|
|  | 打开本地保存的作业详情文件Logviewdetail.txt。 _ |
|  | 返回Logview旧版界面。 |
|  | 将作业详情文件保存至本地设备。 |

**Basic Info**

Basic Info区域展示的作业基本信息如下。

| 参数名 | 描述 |
|---|---|
| MaxCompute Service | 作业使用的MaxCompute服务的Endpoint。 |
| Project | 作业所属的MaxCompute项目名称。 |
| Cloud account | 提交作业的阿里云账号信息。 |
| Type | 作业的类型。例如SQL、SQLRT、LOT、XLib、CUPID、AlgoTask和Graph。 |

| Status | 作业的状态。状态取值如下： Success：作业执行成功。 Failed：作业执行失败。 Canceled：作业执行取消。 Waiting：作业正在MaxCompute中处理，并没有提交至Fuxi中运行。 Running：作业正在Fuxi中处理。 Terminated：作业已执行结束。 |
|---|---|
| Start Time | 作业提交时间。 |
| End Time | 作业执行结束时间。 |
| Latency | 作业执行消耗的时长。 |
| Progress | 作业执行进度。 |
| Priority | 作业优先级。 |
| Queue | 作业在资源配额组内的排队位置。 |

**作业详情**

您可以通过作业详情区域全方位了解作业，作业详情区域包含如下功能区：

**Job Details**

作业执行图
**Job Detail**页签的上半部分为作业执行图。执行图以可视化方式展示三个维度的子任务依赖关系：Fuxi Job层、Fuxi Task层和Operation层，同时提供一系列辅
助工具，为排查问题提供帮助。界面构成如下。

| 序号 | 描述 |
|---|---|
| ① | 面包屑导航，用于切换Fuxi Job。JOB:SQL000job0为Fuxi Job名称。 _ _ _ _ _ _ |
| ② | 排查问题辅助工具。包含Progress Chart、Input Heat Chart、Output Heat Chart、TaskTime Heart Chart和InstanceTime Heart Chart。 |
| ③ | 您可以在此区域刷新作业执行状态（ ）、全屏或缩放显示作业执行图（ ）、获取MaxCompute Studio文档（ ）和切换至任务上一层级（ ）。 |
| ④ | 缩放辅助工具。 |
| ⑤ | Fuxi Task。一个MaxCompute作业由一个或多个Fuxi Job组成。每个Fuxi Job由一个或多个Fuxi Task组成。每个Fuxi Task由一个或者多个Fuxi Instance组成，当用户的输入数据量变大时，MaxCompute会在每个Task启动更多的节点来处理数据，每个节点就是一个Fuxi Instance。例如，简单的MapReduce通常会产生两个Fuxi Task，一个是Map一个是Reduce，两个Fuxi Task的名称分别为M1和R2，当SQL比较复杂时，可能会产生多个Fuxi Task。 您可以在执行界面上看到每个Fuxi Task的名称。例如M1，表示一个Map Task；R439的3、9表示它依赖M3、C93执行结束才能 _ _ _ 开始执行。同理，M2491016表示M2要依赖R439、C93、R10116、C161四个Task执行结束后才能开始执行。R/W表示 _ _ _ _ _ _ _ _ _ _ Task读取和写的行数。 单击某个Task或在Task上单击右键可以查看Task对应的Operator算子依赖关系及全部Operator算子图。 Logview 2.0增加了表依赖关系，您可以快速查看输入和输出表。 |
| ⑥ | Fuxi Task回放。单击即可开始播放，再次单击则暂停。您也可以手动拖动进度条。进度条左边为开始时间，中间为播放时间，右边为结束时间。 |
| ⑦ | 鹰眼。 |

**说明**

不支持回放Running状态的Fuxi Task。 AlgoTask类型的作业（例如PAI机器学习），由于只有一个Fuxi Task，故不提供作业执行图。 非SQL类型作业，仅能展示Fuxi Job和Fuxi Task层，不支持展示Operation层。 如果只有一个Fuxi Job，作业执行图默认展示Fuxi Task层依赖关系；否则，默认展示Fuxi Job层依赖关系。 作业运行情况
**Job Detail**页签的下半部分为作业运行详细信息。界面构成如下。

| 序号 | 描述 |
|---|---|
| ① | Fuxi Job页签，您可以在此切换Fuxi Job。 |
| ② | Fuxi Job对应的Fuxi Task详情。在某个Fuxi Job下，单击任一Fuxi Task，在下方会展开该Fuxi Task对应的Fuxi Instance信息。默认展开第一个Fuxi Job的第一个Fuxi Task的Fuxi Instance信息。 |
| ③ | Logview为不同阶段的Instance进行了分组。您可以单击Failed快速查看出错的节点。 |
| ④ | StdOut和StdErr。您可以查看输出和错误信息，您自己打印的信息也可以在这里查看，同时提供下载功能。 |
| ⑤ | Debug。调测并排除错误。 |

**Result**

Result页签用于展示作业运行结果，如果作业执行失败，系统默认会打开该页签展示失败原因。系统会根据MaxCompute设置的返回格式，显示为表格或纯文本， 您可以通过MaxCompute客户端配置**odps.sql.select.output.format**参数设置显示格式，如果取值为**HumanReadable**表示纯文本，否则默认是CSV格式。 表格您可以通过该界面执行如下操作： 选中某一行可以导出该行数据。 选中标题栏可以导出当前界面的数据。 在标题栏单击 ，选择**Select All Data**或**Deselect All**可以全选或取消全选全量数据。 单击**export**即可导出CSV格式的数据。CSV仅为文件后缀，您可以使用文本编辑器或Sublime Text工具打开。 纯文本

**SourceXML**

您提交至MaxCompute的作业的SourceXML信息。

**SQL Script**

您提交至MaxCompute的作业的SQL脚本信息。

**Summary**

您提交至MaxCompute的作业运行概要信息。

**Json Summary**

以JSON格式显示的作业运行概要信息。

**History**

如果Fuxi Instance重新执行就会产生History信息。

**Substatus History**

您可以查看作业执行的详细历史状态，包含状态码、状态描述、开始时间、持续时间和结束时间。 题

## MaxCompute常见使用问题

本文为您介绍MaxCompute使用中的常见问题及相关解决方案。

**SQL执行缓慢时，如何排查MaxCompute资源使用情况**

使用admin用户登录到**ODPS AG**所在的机器上执行以下相关命令，具体排查步骤如下：
1. 执行如下命令，查看MaxCompute集群各个机器的剩余资源，并按升序排列。

```
r tfrl|sed 's/,//g'|sort -t "|" -k2 -n
```

2. 执行如下命令，查看机器资源明细以及集群总资源。

```
r ttrl|sed 's/,//g'
```

3. 根据以上信息统计出剩余资源在集群总资源中的占比，结合机器资源明细，即可了解此时MaxCompute资源使用情况。

**集群剩余资源充足，但是有个别Project提交的作业执行缓慢，如何处理**

此时可能是当前Project所在的Quota组资源用满，需要确认并考虑加大Quota组资源，具体步骤如下：
1. 使用admin用户登录到**ODPS AG**所在机器上执行如下命令，查看资源组使用情况。

```
r quota
```

2. 当确认MaxCompute Quota组资源用满后，可以通过大数据管家进行配额信息的相关修改。

**Quota组设置**

1. 使用admin用户登录到**ODPS AG**所在机器上执行如下命令，创建或修改Quota。

```
sh /apsara/deploy/rpc_wrapper/rpc.sh setquota -i $QUOTAID -a $QUOTANAME -t fair -s$max_cpu_quota $max_mem_quota -m $min_cpu_quota $min_ mem_quota
```

**说明**

当**$QUOTAID**存在时则为修改，不存在时则为新创建。
2. 登录大数据管家进行相关设置。

**如何简单的使用元仓**

1. 使用admin用户登录到**ODPS AG**所在的机器上。
2. 分别执行如下命令。

```
/apsara/odps_tools/clt/bin/odpscmd USE meta;
```

3. 执行如下命令，查看元仓全部的表。

```
SHOW tables;
```

4. 执行如下命令，获取相关表的描述信息。

```
DESC <table>;
```

**智能元仓使用（Package+View）**

智能元仓采用的是**Package+View**元仓增强包的方式，您（使用方，即被授权Project的Project Owner）在完成该增强包的安装后，即可进行智能元仓的使用。详

**安装**

**Package+View**包是元仓基础上面的增强包，所以是依赖于元仓的。因此，在system metadata warehouse目录下面执行 `odpscmd --`

| config=odps_config.ini -f init.sql |  | 命令即可完成安装。 |
|---|---|---|
|  | 说明如果出现需要重装的情况，可以把init.sql中第一行的create package注释掉后，再次执行上面的命令即可。 odps config.ini：是元仓执行的账户配置（即元仓Project Owner）。 _ |  |

**授权**

允许某个Project（如p1）安装扩展包。

```
odpscmd --config=odps_config.ini -e "allow project p1 to install package systables;"
```

允许所有Project安装扩展包。

```
odpscmd --config=odps_config.ini -e "allow project * to install package systables;"
```

**使用方操作**

被授权Project的Project Owner在Odpscmd中执行安装命令。

```
install package meta.systables;
```

安装完成后，查看Package中的View说明。 题

```
DESC package meta.systables;
```

**说明**

完成上述操作，您可以开始进行智能元仓的使用。

**视图**

查看视图的定义，请执行以下命令：

```
DESC viewname
```

| 视图名称 | 内容信息 |
|---|---|
| allowedpackageinstallers _ _ | Project所属的Package授权安装的Project信息 |
| columnlabelgrants _ _ | 列Label授权信息 |
| columnlabels _ | 表的列Label信息 |
| columns | 表的Schema信息 |
| installedpackages _ | Project安装的Package信息 |
| objectprivileges _ | Table/UDF/Resource的授权信息 |
| packageresources _ | Package中含有的对象信息 |
| partitions | 分区表的分区信息 |
| policies | Policy定义的用户或角色权限信息 |
| resources | 资源信息 |
| roles | 角色信息 |
| tablelabelgrants _ _ | 表级别Label授权信息 |
| tablelabels _ | 表的Label信息 |
| tables | 表或视图信息 |
| tasks | 作业执行记录 |
| tunnels | 数据上传下载记录 |
| udfresources _ | UDF中使用的Resource信息 |
| udfs | UDF信息 |
| userroles _ | 用户或角色关联信息 |
| users | 用户信息 |

##### 特殊说明

元仓包默认只允许查询过去180天的数据。 如果您在某一天没有运行作业，那么这一天的元仓不会有您的数据。 建议您在进行查询时，指定查询范围，避免全盘扫描过去180天的所有数据。 前一天的数据何时可见依赖于凌晨元仓的产出时间，当前设置为产出即可见。 新创建Project当天的元数据不提供，这样做主要是为了避免获取到重名Project之前的数据。

**如何开通Java沙箱权限**

1. 登录adminconsole，选择**ODPS****配置** **> Project****管理**，选择要开通沙箱访问的Project后，双击打开Project属性框。
2. 在**ODPS Sandbox****设置**区域下的**Sandbox Java Permissions**中填入要使用的方法或类。
题

**说明**

需要注意格式，下方仅是示例，实际应用时请根据实际值设置，一行一个，分号分隔。

```
permission java.lang.RuntimePermission "readSystemProperty"; permission java.lang.RuntimePermission "modifyThreadGroup"; permission jav a.security.AllPermission;
```

3. 单击**完成修改**，完成开通步骤。

**磁盘空间用满时，如何处理**

通常进行清理脚本操作。由于通常都是**ODPS AG**根目录或者**/apsara**飞天目录的磁盘空间用满，因此具体操作时，在上述两个路径的操作会比较多。

**如何把MaxCompute机器加入黑名单**

1. 在**Apsara AG**上面使用admin用户执行如下命令，打开Fuxi黑名单功能开关。

```
r sgf fuximaster"{\"fuxi_Enable_BadNodeManager\":false}"
```

2. 执行如下命令，查看Fuxi黑名单。

```
/apsara/deploy/rpc_wrapper/rpc.shblacklist cluster get
```

3. 执行如下命令，添加Tubo（Fuxi）黑名单。

```
/apsara/deploy/rpc_wrapper/rpc.shblacklist cluster add $hostname
```

4. 执行如下命令，再次查看Fuxi黑名单，确认添加成功。

```
/apsara/deploy/rpc_wrapper/rpc.shblacklist cluster get
```

**如何将MaxCompute数据导出**

通常有两种方式，一种是使用Tunnel命令进行导出，另一种是使用大数据开发套件，配置同步任务把MaxCompute数据导出到其他目的端。

**如何查看MaxCompute的版本**

执行如下命令获取MaxCompute的版本。

```
cat /apsara/odps_info/version|grep odps cat /apsara/version
```

**如何进行MaxCompute服务重启**

1. 将MaxCompute常驻服务的配置写入文件中保存起来，启动的时候需要用到这些配置文件。

```
ssh odpsAG cd /home/admin/
```

# 将常驻服务配置保存到文件里面，如果操作时下面某些服务没有，可以忽略，按照实际情况操作。
# 命令`r al`可以查看常驻服务。

```
r plan Odps/CGServiceControllerx > CGServiceControllerx r plan sys/sqlonline-OTS >sqlonline-OTS r plan Odps/MessagerServicex >MessagerServicex r plan Odps/OdpsServicex >OdpsServicex r plan Odps/HiveServerx >HiveServerx r plan Odps/XStreamServicex >XStreamServicex r plan Odps/QuotaServicex > QuotaServicex r plan Odps/ReplicationServicex >ReplicationServicex
```

2. 关闭MaxCompute服务。

```
r sstop Odps/CGServiceControllerx r sstop sys/sqlonline-OTS r sstop Odps/MessagerServicex r sstop Odps/OdpsServicex r sstop Odps/HiveServerx r sstop Odps/XStreamServicex r sstop Odps/QuotaServicex r sstop Odps/ReplicationServicex
```

3. 启动MaxCompute服务。

```
ssh odpsAG cd /home/admin/ r start CGServiceControllerx r start sqlonline-OTS r start MessagerServicex.txt r start OdpsServicex.txt r start HiveServerx.txt r start XStreamServicex.txt r start QuotaServicex.txt r start ReplicationServicex.txt
```

**如何进行MaxCompute上下电**

题
1. 将MaxCompute常驻服务的配置写入文件中保存起来，启动的时候需要用到这些配置文件。

```
ssh odpsAG cd /home/admin/
```

# 将常驻服务配置保存到文件里面，如果操作时下面某些服务没有，可以忽略，按照实际情况操作。
# 命令`r al`可以查看常驻服务。

```
r plan Odps/CGServiceControllerx > CGServiceControllerx r plan sys/sqlonline-OTS >sqlonline-OTS r plan Odps/MessagerServicex >MessagerServicex r plan Odps/OdpsServicex >OdpsServicex r plan Odps/HiveServerx >HiveServerx r plan Odps/XStreamServicex >XStreamServicex r plan Odps/QuotaServicex > QuotaServicex r plan Odps/ReplicationServicex >ReplicationServicex
```

2. 关闭MaxCompute服务。

```
r sstop Odps/CGServiceControllerx r sstop sys/sqlonline-OTS r sstop Odps/MessagerServicex r sstop Odps/OdpsServicex r sstop Odps/HiveServerx r sstop Odps/XStreamServicex r sstop Odps/QuotaServicex r sstop Odps/ReplicationServicex
```

3. 关闭飞天操作系统。

```
/home/admin/dayu/bin/allapsara stop
```

4. 计算节点优雅关机。

```
Shutdown
```

5. 计算节点开机。
6. 启动飞天操作系统。

```
/home/admin/dayu/bin/allapsara start
```

7. 启动MaxCompute服务。

```
ssh odpsAG cd /home/admin/ r start CGServiceControllerx r start sqlonline-OTS r start MessagerServicex.txt r start OdpsServicex.txt r start HiveServerx.txt r start XStreamServicex.txt r start QuotaServicex.txt r start ReplicationServicex.txt
```

**机器Load高如何处理**

1. 登录Load高的主机执行 `top` 命令，查看是否是Task进程占用资源。
2. 如果确认是Task进程占用资源，此时通常情况下是用户任务在占用资源运行，只能等待任务完成或者与用户沟通，让用户Kill掉任务。
