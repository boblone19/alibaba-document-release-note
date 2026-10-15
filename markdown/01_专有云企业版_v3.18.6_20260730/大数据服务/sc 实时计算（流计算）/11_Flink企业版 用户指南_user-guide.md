---
title: "实时计算（流计算） Flink企业版 用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 107
source_pdf: "11_Flink企业版 用户指南_user-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sc/zh/user-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 实时计算（流计算） Flink企业版 用户指南

实时计算（流计算） 算

## 什么是实时计算

阿里云实时计算（Alibaba Cloud Realtime Compute）是一套基于Apache Flink构建的一站式、高性能实时大数据处理平台，广泛适用于流式数据处理、离线数据处理等多种场景。

**产品特点**

强大的实时处理能力阿里云实时计算集成诸多全链路功能，方便您进行全链路实时计算开发，包括： 强大的流计算引擎。 阿里云实时计算提供Flink SQL，支持各类错误场景的自动恢复，保证故障情况下数据处理的准确性。 支持多种内置函数，包括：字符串函数、日期函数、聚合函数。 精确的计算资源控制，高度保证用户作业的隔离性。 关键性能指标为开源Flink的3到4倍。数据计算延迟优化到亚秒级甚至秒级。单个作业吞吐量可做到百万（记录/秒）级别。单集群规模为数千台。 深度整合各类云数据存储。 托管的实时计算服务不同于开源或者自建的流式处理服务，阿里云实时计算是完全托管的流计算引擎。阿里云可针对流数据运行查询，无需预置或管理任何基础设施。在阿里云实时计算，您可以享受一键启用的流式数据服务能力。 阿里云实时计算天然集成数据存储、数据开发、数据运维、监控报警等功能，方便您以较小成本试用和迁移流式计算。同时，实时计算提供完全租户隔离的托管运行服务。从最上层工作空间，到最底层执行机器，提供高度有效的隔离和全面防护，让您放心使用实时计算。 低廉的人力和集群成本大量优化的SQL执行引擎，提供比原生Flink作业更高效且更廉价的计算作业。在开发成本和运行成本方面，阿里云实时计算均要远低于开源流式框架。 实时计算（流计算）

## 准备工作

### 登录实时计算开发平台

您可以在实时计算Flink版管理控制台管理工作空间与项目空间，在实时计算开发控制台进行作业开发与运维管理相关操作。本文为您介绍如何登录实时计算Flink版管理控制台、实时计算开发控制台。

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**登录实时计算Flink版管理控制台**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
实时计算（流计算）

**说明**

单击页面右上角的当前语言可以切换其它语言。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 勾选**我已阅读并同意产品服务协议、隐私协议、用户协议**。

**说明**

登录页展示的链接文字为文档标题，单击链接文字，可查看协议的详细内容。
**产品服务协议**、**隐私协议**和**用户协议**仅在已发布时才会显示。如果三种类型协议都没有发布，
则不需要执行该操作。
4. 单击**账号登录**/**授权登录**。

**说明**

“授权登录”仅第三方认证的全局IdP设置启用时才会显示，且该显示名称可自定义，默认显示名称为“授权登录”。
5. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：

**说明**

公网场景下，登录入口默认强制开启多因素认证。

**开启MFA后的首次登录**

a. 输入账号密码登录后，展示绑定虚拟MFA设备页面。 b. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定虚拟MFA设备。 c. 登录成功，进入控制台。

**已开启并绑定MFA**

输入6位MFA码后单击**认证**。
6. 在顶部导航栏，鼠标悬浮至**产品**，选择**大数据计算** > **实时计算** **Flink**版。
7. 在右下角悬浮菜单处，单击
图标，可按需展开或者收起悬浮菜单。 ：定价。单击后，跳转至**价格计算器**页面。 实时计算（流计算） ：购物车。单击后，跳转至**配置报价器**页面。 ：飞天助理。单击后，可打开飞天助理对话窗口，通过自然语言提问，快速获取帮助。

**登录实时计算开发控制台**

1. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
2. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。

### 配置项目空间访问权限

**背景信息**

随着产品演进和现场计量的需求，Flink项目空间（Namespace）资源的管理由大数据管家（ABM）迁移至Apsara Uni-manager运营控制台，可以更贴合用户在Apsara Uni-manager运营控制台上创建资源的行为。 Flink权限分为以下两部分，分别面向实时计算Flink版管理控制台与实时计算开发控制台：

| 权限分类 | 说明 |
|---|---|
| 资源管理 | 针对项目空间资源管理的权限，包括创建、修改、删除以及工作空间查询四类权限，拥有该权限的账号可以在实时计算Flink版管理控制台上管理项目空间资源。 |
| 业务角色 | 针对具体项目空间内作业的权限，包括owner、editor和view（只读）三类权限。主要体现在实际业务的操作上面，授权业务角色的用户可以通过实时计算Flink版管理控制台登录实时计算开发控制台，进行作业开发与运维管理操作。 |

本文介绍资源管理角色授权。如需配置业务角色权限，开放实时计算开发控制台操作的相关权限，请参见成员管理。

**操作步骤**

1. 创建目标组织。
详细操作，请参见**统一云管平台****用户指南** > **企业中心** > **资源管理** > **组织管理** > **创建组织**。
2. 创建目标资源集（创建一个组织，系统会默认为该组织创建一个资源集，可按需创建）。
详细操作，请参见**统一云管平台****用户指南** > **企业中心** > **资源管理** > **资源集管理** > **创建资源集**。
3. 创建目标用户。
详细操作，请参见**Apsara Uni-manager****运营控制台****用户指南** > **企业中心** > **人员管理** > **用户管理**
> **创建用户**，根据角色权限范围添加对应的角色。

**说明**

推荐选择资源集管理员或组织管理员预置角色。该预置角色开放了对工作空间与项目空间创建、修改、删除与查看的权限。 选择资源使用人预置角色，用户可查看、修改工作空间以及项目空间。 查看角色权限或自定义角色，请参见**统一运管****用户指南** > **企业中心** > **权限管理** > **角色授权**。 实时计算（流计算）
4. 添加目标用户至目标资源集中。
详细操作，请参见**统一运管****用户指南** > **企业中心** > **资源管理** > **资源集管理** > **管理资源集成员**，将目标用户添加至对应的资源集中。
5. 授权目标用户其他角色（可选）。
详细操作，请参见**统一运管****用户指南** > **企业中心** > **人员管理** > **用户管理** > **用户角色授权**，修改或添加目标用户对项目空间资源的管理权限。

**后续操作**

切换owner角色进入成员管理页面，为目标用户分配业务角色，通过实时计算Flink版管理控制台访问实时计算开发控制台。

### 进入概览页

本文介绍控制台概览页展示的详细信息。

**概览页介绍**

登录实时计算Flink版管理控制台，系统默认进入**Flink (****企业版****) >** **概览**页。概览页展示的信息说明如下。

| 区域 | 说明 |
|---|---|
| 实例概览 | 在实例总览区域可查看本组织下已创建的namespace个数（总数）和数据更新时间。 |
| 告警统计 | 在告警统计区域，可查看告警总数，以及P1紧急、P2警告和P3提示级别的告警汇总情况。 |
| 告警趋势 | 在告警趋势区域，可查看近7天、近15天或者近30天内的告警趋势。 |

### 创建NameSpace

本文介绍如何创建Flink NameSpace资源。

**前提条件**

已创建目标组织、目标资源集，为目标用户开放相应的权限。

**重要**

请先配置项目空间访问权限，用户应至少具备创建和查看实时计算Flink项目空间的权限。

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 创建Namespace。
i. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。 实时计算（流计算） iii. 在**创建****Flink Namespace**页面，填写**区域**和**基本信息**。

| 类别 | 参数 | 说明 |
|---|---|---|
| 计费配置 | 计费方式 | 计费方式是指云服务根据用户使用其服务的情况来收取费用的方法，目前支持按量计费。 说明该配置参数只有创建了服务管理功能，才会显示。更多创建服务管理详情可参见《统一云管平台用户指南》中的运营中心 > 服务运营 > 服务目录 > 服务管理章节。 |
| 区域 | 组织/资源集 | 选择目标组织和资源集。 |
|  | 地域 | 选择地域。 |
| 基本信息 | 名称 | Flink Namespace的名称，可自定义。但需要满足以下要求： 允许小写字母、数字、- 或 . 且开头结尾为小写字母、数字。 在同一个地域内，名称不可重复。 长度不超过40。 |
|  | 保障资源（CU） | 按需填写，但数量不能超过剩余的可分配的CU数量。 |
|  | CPU | CPU类型，不可修改。 |
|  | 用户名 | 选择当前组织下有权限的用户名，指定该Namespace归属的用户。 |

3. （可选）查看配置概览信息。
在右侧的**配置概览**面板中，您可以执行以下操作： 实时计算（流计算） 查看参数配置情况
**配置概览**会实时校验必填项，未填写时相应条目将呈现红色警告状态。
管理配额您可单击**管理**按钮，进入配额管理页面为实例设置配额上限。更多设置详情可参见**《统一云管平台**用
**户指南》**中的**运营中心** > **配额管理**章节。
快速定位单击目标参数右侧的条目，即可快速跳转到目标参数的配置项。
4. 确认并提交配置信息。
如果服务管理中已创建云资源为**实时计算** **Flink**版的服务：确认以上配置参数无误后，单击**确认订单**。 如果服务管理中未创建云资源为**实时计算** **Flink**版的服务：确认以上配置参数无误后，单击**提交**。 关于服务管理的更多信息，请参见《**Apsara Uni-manager****运营控制台****用户指南》**中的**《服务管**
**理》**章节。
5. 在**操作成功**弹框中，单击**确定**。
创建成功后，刷新**NameSpace** **列表**，即可看到新建的Namespace信息。

**相关操作**

跳转至实时计算开发平台单击目标Namespace名称**操作**列下的**控制台**，即可跳转至实时计算开发控制台。 修改CU数量单击目标Namespace名称**操作**列下的**修改****CU****数量**，可调整CU大小。

**重要**

减小CU大小可能导致Flink重启后无法恢复, 请检查NameSpace已使用的CU情况，谨慎操作。 单击目标Namespace名称**操作**列下的**配置外部存储****IP**，可添加IP地址或网段，IP地址为存储域名对应的删除NameSpace 如果需要删除已创建的NameSpace，单击**操作**列下的**删除**。 实时计算（流计算） 查询目标Namespace信息在**NameSpace** **列表**下的搜索框中，可按关键词搜索目标Namespace。 配置标签将鼠标悬浮至**标签**列，单击按钮，即可配置项目空间的标签。配置完成后，您可以通过标签快速筛选项目空间。 如果存在需要同时绑定或者解绑多个实例标签的场景，可通过**批量绑定标签**功能和**批量解绑标签**功能实现。 自定义列表项单击图标，可按需重置Namespace展示的列信息。

**常见问题**

问题描述：为什么我的账号已经授予了NameSpace的访问权限，列表中却没有目标NameSpace? 问题原因：针对该问题，可能存在两种情况： 您的账号没有加入到NameSpace所属的资源集。 问题描述：为什么我的账号进入Flink NameSpace管理页面后，有些操作按钮没有显示，或者有显示但是是灰色的？ 问题原因：您的账号当前的角色没有赋予相关操作权限，请检查您的角色在产品应用中的授权情况。 如果您的资源管理角色没有授权创建、删除工作空间或项目空间的权限，请联系管理员配置项目空间访问权限。 如果您没有被分配业务角色，无法访问实时计算开发控制台，请联系资源owner分配业务角色，详情见成员管理。 问题描述：为什么我的账号在创建，修改，删除等操作提交后，报如下这个错误？ 问题原因：如图所示，账号当前的角色没有被授权进行这个操作。请检查你的角色在流计算这个应用的授权。 实时计算（流计算）

## 快速入门

### Flink SQL作业快速入门

Flink支持通过SQL代码编辑和运行作业。本文带您快速体验Flink SQL作业的创建和上线运行等操作。

**操作流程**

步骤一：创建SQL作业并编写业务代码在作业开发页面，创建一个SQL类型的流作业，并编写DDL和DML代码。 步骤二：启动作业，查看Flink计算结果在作业运维页面，启动作业并查看作业运行状态。

**步骤一：创建SQL作业并编写业务代码**

1. 创建SQL作业。
i. 登录实时计算Flink版管理控制台。 ii. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。

| 在 |  |
|---|---|
|  | 。 |

iv. 在左侧导航栏，单击**作业开发**。 v. 单击**新建**。 vi. 在**新建文件**对话框，填写作业配置信息。

| 作业参数 | 说明 | 示例 |
|---|---|---|
| 文件名称 | 作业的名称。 说明作业名称在当前项目中必须保持唯一。 | flink-test |
| 文件类型 | 流作业和批作业均支持以下文件类型： SQL JAR PYTHON | 流作业/SQL |
| 部署目标 | 选择作业需要部署的集群名称。Flink支持Per-Job集群和Session 集群两种集群模式。两种集群模式的区别说明，请参见配置 Session集群。 | vvp-workload |
| 存储位置 | 指定该作业的代码文件所属的文件夹。默认存放在作业开发目录。 您还可以在现有文件夹右侧，单击图标，新建子文件夹。 | 作业开发 |

实时计算（流计算） vii. 单击**确认**。
2. 将以下作业代码拷贝到作业文本编辑区。
创建一个产生随机数据的datagen源表，将datagen源表中的name字段中的数据插入blackhole结果表，代码示例如下所示。

```
CREATE TEMPORARY TABLE datagen_source(
  randstr VARCHAR
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE print_table(
  randstr  VARCHAR
) WITH (
  'connector' = 'print',
  'logger' = 'true'
); INSERT INTO print_table SELECT SUBSTRING(randstr,0,8) from datagen_source;
```

3. 单击**验证**，进行语法检查。
4. 检查通过后，单击**上线**。
5. 按需填写上线备注信息，单击**确认**。

**步骤二：启动作业，查看Flink计算结果**

1. 在左侧导航栏，单击**作业运维**。
2. 单击目标作业名称**操作**列中的**启动**。
i. 进行资源设置。
**资源模式**默认为**基础模式**，按需设置**并发度**和**Flink****配置**信息，单击**下一步**。
实时计算（流计算） ii. 进行基础设置。 设置**启动策略**和**更多设置**，单击**启动**。
3. 单击启动后，您可以看到作业从当前状态到期望状态的变化过程及最终结果。直到状态变为**运行中**，则代
表作业运行正常。
4. 查看Flink计算结果。
i. 在**作业运维**页面，单击目标作业名称，默认进入**作业总览**页签。 ii. 在**当前实例**区域，单击**Flink UI**，默认进入**Apache Flink Dashboard**的**Overview**页面。 iii. 在左侧导航栏，单击**Task Manager**。 iv. 单击目标**Path, ID**，选择**Logs**页签。搜索关键字 `Sink` ，查看Flink计算结果。

### Flink JAR作业快速入门

Flink支持通过JAR代码编辑和运行作业。本文带您快速体验Flink JAR流作业和批作业的创建和上线运行等操作。 实时计算（流计算）

**操作流程**

步骤一：准备JAR包步骤二：上传测试JAR包和数据文件步骤三：部署JAR作业，并配置作业信息步骤四：启动作业后，查看Flink计算结果

**步骤一：准备JAR包**

实时计算开发平台不提供JAR包的开发环境，您需要在本地完成开发、编译、打包。详情请参见JAR作业开发。

**步骤二：上传测试JAR包和数据文件**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏，单击**资源上传**。
5. 单击**上传资源**，上传要部署的JAR包和数据文件。
您可以直接下载测试文件以供后续步骤使用。 单击FlinkQuickStart-1.0-SNAPSHOT.jar，下载测试JAR包。 单击Shakespeare，下载输入数据文件Shakespeare。

**步骤三：部署JAR作业，并配置作业信息**

**部署JAR流作业，并配置作业信息**

1. 创建JAR流作业。
i. 在左侧导航栏，单击**作业开发**。 ii. 单击**新建**。 实时计算（流计算） iii. 在**新建文件**对话框，填写作业配置信息。

| 作业参数 | 说明 | 示例 |
|---|---|---|
| 文件名称 | 作业的名称。 说明作业名称在当前项目中必须保持唯一。 | flink-streaming-test-jar |
| 文件类型 | 流作业和批作业均支持以下文件类型： SQL JAR PYTHON | 流作业/JAR |
| 部署目标 | 选择作业需要部署的集群名称。Flink支持Per-Job集群和 Session集群两种集群模式。两种集群模式的区别说明，请参见配置Session集群。 | vvp-workload |
| 存储位置 | 指定该作业的代码文件所属的文件夹。默认存放在作业开发目录。 您还可以在现有文件夹右侧，单击图标，新建子文件夹。 | 作业开发 |

iv. 单击**确认**。
2. 在**作业开发**页面，填写基本配置信息。

| 参数 | 说明 | 示例 |
|---|---|---|
| 部署目标 | 您可以修改创建作业时已选择的部署目标。 | vvp-workload |
| JAR URI | 单击下拉框选择资源上传中的文件，或者单击右侧图标选择文件，上传JAR包。 | hdfs:///vvp/data/artifact s/namespaces/flink- test- default/FlinkQuickStart- 1.0-SNAPSHOT.jar |
| Entry Point Class | 程序的入口类。如果您的JAR包未指定主类，请在此处输入您的Entry Point Class类的标准路径。 说明因为本文提供的测试JAR包中既包含了流作业代码，又包含批作业代码。所以，此处需要指定为流作业的程序入口。 | org.example.WordCoun tStreaming |

实时计算（流计算）

| Entry Point Main Arguments | 填写输入数据文件的hdfs路径。您可以在资源管理中查看并复制路径。 说明本文输入数据文件和测试JAR包存放路径一致。 | --input hdfs:///vvp/data/artifact s/namespaces/flink- test- default/Shakespeare |
|---|---|---|
| 附加依赖文件 | 填写目标附加依赖文件的OSS路径或者URL。 | 无需填写 |

3. 单击**上线**。
4. 按需填写上线备注信息，单击**确认**。

**部署JAR批作业，并配置作业信息**

1. 创建JAR批作业。
i. 在左侧导航栏，单击**作业开发**。 ii. 单击**新建**。 iii. 在**新建文件**对话框，填写作业配置信息。

| 作业参数 | 说明 | 示例 |
|---|---|---|
| 文件名称 | 作业的名称。 说明作业名称在当前项目中必须保持唯一。 | flink-batch-test-jar |
| 文件类型 | 流作业和批作业均支持以下文件类型： SQL JAR PYTHON | 批作业/JAR |
| 部署目标 | 选择作业需要部署的集群名称。Flink支持Per-Job集群和 Session集群两种集群模式。两种集群模式的区别说明，请参见配置Session集群。 | vvp-workload |
| 存储位置 | 指定该作业的代码文件所属的文件夹。默认存放在作业开发目录。 您还可以在现有文件夹右侧，单击图标，新建子文件夹。 | 作业开发 |

iv. 单击**确认**。
2. 在作业开发页面，填写基本配置信息。
实时计算（流计算）

| 参数 | 说明 | 示例 |
|---|---|---|
| 部署目标 | 您可以修改创建作业时已选择的部署目标。 | vvp-workload |
| JAR URI | 下拉框选择资源管理中的文件，或单击右侧图标选择文件，上传JAR包。 | hdfs:///vvp/data/artifacts/namespaces /flink-test-default/FlinkQuickStart-1.0- SNAPSHOT.jar |
| Entry Point Class | 程序的入口类。如果您的JAR包未指定主类，请在此处输入您的Entrypoint Class类的标准路径。 说明因为本文提供的测试JAR包中既包含了流作业代码，又包含批作业代码。所以，此处需要指定为批作业的程序入口。 | org.example.WordCountBatch |
| Entry Point Main Arguments | 填写输入数据文件和结果数据输出文件路径。 说明本示例中输入数据文件、输出文件和测试JAR包存放路径一致。 | --input hdfs:///vvp/data/artifacts/namespaces /flink-test-default/Shakespeare --output hdfs:///vvp/data/artifacts/namespaces /flink-test-default/batch-quickstart- test-output.txt |
| 附加依赖文件 | 填写目标附加依赖文件的OSS路径或者 URL。 | 无需填写 |

3. 单击**上线**。
4. 按需填写上线备注信息，单击**确认**。

**步骤四：启动作业后，查看Flink计算结果**

1. 在左侧导航栏，单击**作业运维**。

**说明**

系统默认展示的作业为**流作业**，本操作以**流作业**为例。如果您需要启动批作业，则需要在**作业运维**页面，将作业类型切换为**批作业**，才可以看到您上线的批作业。批作业的启动，请根据控制台界面提示进行操作。
2. 单击目标作业名称**操作**列中的**启动**。
实时计算（流计算） i. 进行资源设置。
**资源模式**默认为**基础模式**，按需设置CPU Cores、Memory、并发度和Flink配置信息，单击**下一步**。
ii. 进行基础设置。 设置**启动策略**和**更多设置**，单击**启动**。
3. 单击启动后，您可以看到作业从当前状态到期望状态的变化过程及最终结果。直到状态变为**运行中**，则代
表作业运行正常。
4. 查看Flink计算结果。
流作业示例的计算结果： a. 在**作业运维**页面，单击目标作业名称，默认进入**作业总览**页签。 b. 在**当前实例**区域，单击**Flink UI**，默认进入**Apache Flink Dashboard**的**Overview**页面。 c. 在左侧导航栏，单击**Task Manager**。 实时计算（流计算） d. 单击目标**Path, ID**，选择**Log List**页签，在 `.out` 尾缀的日志文件中查看Flink计算结果。 批作业示例的计算结果： a. 在左侧导航栏中，单击**资源上传**。 b. 单击batch-quickstart-test-output.txt文件**操作**列**下载**，在本地进行查看。

### Flink Python作业快速入门

Flink支持通过Python代码编辑和运行作业。本文带您快速体验Flink Python流作业和批作业的创建和上线运行等操作。

**使用限制**

Flink企业版的ARM架构不支持创建Python作业。

**操作流程**

实时计算（流计算） 步骤一：准备Python代码文件步骤二：上传测试Python文件和数据文件步骤三：创建PYTHON作业，并配置作业信息步骤四：启动作业后，查看Flink计算结果

**步骤一：准备Python代码文件**

实时计算开发平台不提供Python的开发环境，您需要在本地完成作业开发。详情请参见Python作业开发。

**步骤二：上传测试Python文件和数据文件**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏，单击**资源管理**。
5. 单击**上传资源**，上传要部署的Python文件和数据文件。
您可以直接下载测试文件以供后续步骤使用。 流模式测试Python文件：单击word_count_streaming.py下载。 批模式测试Python文件：单击word_count_batch.py下载。 输入数据文件Shakespeare：单击Shakespeare下载。

**步骤三：创建PYTHON作业，并配置作业信息**

**创建PYTHON流作业，并配置作业信息**

1. 创建PYTHON流作业。
i. 在左侧导航栏，单击**作业开发**。 ii. 单击**新建**。 实时计算（流计算） iii. 在**新建文件**对话框，填写作业配置信息。

| 作业参数 | 说明 | 示例 |
|---|---|---|
| 文件名称 | 作业的名称。 说明作业名称在当前项目中必须保持唯一。 | flink-streaming-test- python |
| 文件类型 | 流作业和批作业均支持以下文件类型： SQL JAR PYTHON | 流作业/PYTHON |
| 部署目标 | 选择作业需要部署的集群。 重要 Python作业仅支持Per-Job集群。 | vvp-workload |
| 存储位置 | 指定该作业的代码文件所属的文件夹。默认存放在作业开发目录。 您还可以在现有文件夹右侧，单击图标，新建子文件夹。 | 作业开发 |

iv. 单击**确认**。
2. 在作业开发页面，填写基本配置信息。

| 参数 | 说明 | 示例 |
|---|---|---|
| 部署目标 | 您可以修改创建作业时已选择的部署目标。 | vvp-workload |
| Python 文件地址 | 单击下拉框选择资源上传中的文件，或者单击右侧图标选择文件，上传Python文件。 | hdfs:///vvp/data/artifacts/namespaces /<Your NameSpace>/word count str _ _ _ eaming.py |
| Entry Module | 程序的入口类。 如果Python作业文件为.py文件，则该项不需要填写。 如果Python作业文件为.zip文件，则需要在此处输入您的Entry Module，例如 word count。 _ | 无需填写 |

实时计算（流计算）

| Entry Point Main Arguments | 填写输入数据文件的OSS路径。 说明本示例中输入数据文件、输出文件和测试PYTHON包存放路径一致。 | --input hdfs:///vvp/data/artifacts/namespaces /<Your NameSpace>/Shakespeare _ --output hdfs:///vvp/data/artifacts/namespaces /<Your NameSpace>/ _ |
|---|---|---|
| Python Libraries | 第三方Python包。第三方Python包会被添加到Python worker进程的PYTHONPATH 中，从而在Python自定义函数中可以直接访问。如何使用第三方Python包，详情请参见使用第三方Python包。 | 无需填写 |
| Python Archives | 存档文件，目前仅支持ZIP格式的文件，例如 .zip、.jar、.whl和.egg等。 存档文件会被解压到Python worker进程的工作目录下。假如，存档文件所在的压缩包名称为mydata.zip，则在Python自定义函数中可以编写以下代码来访问mydata.zip存档文件。 def map(): with open("mydata.zip/mydata/data.t xt") as f: ... 请参见使用自定义的Python虚拟环境和使用数据文件，了解更多关于Python Archives的信息。 | 无需填写 |
| 附加依赖文件 | 填写目标附加依赖文件的OSS路径或者 URL。 | 无需填写 |

3. 单击**上线**。
4. 按需填写上线备注信息，单击**确认**。

**创建PYTHON批作业，并配置作业信息**

1. 创建PYTHON批作业。
i. 在左侧导航栏，单击**作业开发**。 ii. 单击**新建**。 实时计算（流计算） iii. 在**新建文件**对话框，填写作业配置信息。

| 作业参数 | 说明 | 示例 |
|---|---|---|
| 文件名称 | 作业的名称。 说明作业名称在当前项目中必须保持唯一。 | flink-batch-test- python |
| 文件类型 | 流作业和批作业均支持以下文件类型： SQL JAR PYTHON | 批作业/PYTHON |
| 部署目标 | 选择作业需要部署的集群名称。Flink支持Per-Job集群和 Session集群两种集群模式。两种集群模式的区别说明，请参见配置Session集群。 | vvp-workload |
| 存储位置 | 指定该作业的代码文件所属的文件夹。默认存放在作业开发目录。 您还可以在现有文件夹右侧，单击图标，新建子文件夹。 | 作业开发 |

iv. 单击**确认**。
2. 在作业开发页面，填写基本配置信息。

| 参数 | 说明 | 示例 |
|---|---|---|
| 部署目标 | 您可以修改创建作业时已选择的部署目标。 | vvp-workload |
| Python 文件地址 | 下拉框选择资源管理中的文件，或单击右侧图标选择文件，上传Python文件。 | hdfs:///vvp/data/artifacts/namespaces /<Your NameSpace>/word count bat _ _ _ ch.py |
| Entry Module | 程序的入口类。 如果Python作业文件为.py文件，则该项不需要填写。 如果Python作业文件为.zip文件，则需要在此处输入您的Entry Module，例如 word count。 _ | 无需填写 |

实时计算（流计算）

| Entry Point Main Arguments | 填写输入数据文件和结果数据输出文件路径。 说明本示例中输入数据文件、输出文件和测试PYTHON包存放路径一致。 | --input hdfs:///vvp/data/artifacts/namespaces /<Your NameSpace>/Shakespeare _ --output hdfs:///vvp/data/artifacts/namespaces /<Your NameSpace>/ _ |
|---|---|---|
| Python Libraries | 第三方Python包。第三方Python包会被添加到Python worker进程的PYTHONPATH 中，从而在Python自定义函数中可以直接访问。如何使用第三方Python包，详情请参见使用第三方Python包。 | 无需填写 |
| Python Archives | 存档文件，目前仅支持ZIP格式的文件，例如 .zip、.jar、.whl和.egg等。 存档文件会被解压到Python worker进程的工作目录下。假如，存档文件所在的压缩包名称为mydata.zip，则在Python自定义函数中可以编写以下代码来访问mydata.zip存档文件。 def map(): with open("mydata.zip/mydata/data.t xt") as f: ... 请参见使用自定义的Python虚拟环境和使用数据文件，了解更多关于Python Archives的信息。 | 无需填写 |
| 附加依赖文件 | 填写目标附加依赖文件的OSS路径或者 URL。 | 无需填写 |

3. 单击**上线**。
4. 按需填写上线备注信息，单击**确认**。

**步骤四：启动作业后，查看Flink计算结果**

1. 在左侧导航栏，单击**作业运维**。

**说明**

系统默认展示的作业为**流作业**，本操作以**流作业**为例。如果您需要启动批作业，则需要在**作业运维**页面，将作业类型切换为**批作业**，才可以看到您上线的批作业。批作业的启动，请根据控制台界面提示进行操作。
2. 单击目标作业名称**操作**列中的**启动**。
实时计算（流计算） i. 进行资源设置。
**资源模式**默认为**基础模式**，按需设置CPU Cores、Memory、并发度和Flink配置信息，单击**下一步**。
ii. 进行基础设置。 设置**启动策略**和**更多设置**，单击**启动**。
3. 单击启动后，您可以看到作业从当前状态到期望状态的变化过程及最终结果。直到状态变为**运行中**，则代
表作业运行正常。
4. 查看Flink计算结果。
流作业示例的计算结果： 在左侧导航栏中，单击**资源上传**。下载结果文件查看。本示例中结果文件为2025-05-30--15/prefixdb40****-47ff-4cba-acbc-18febf89****-0.ext。 实时计算（流计算） 批作业示例的计算结果： 在左侧导航栏中，单击**资源上传**。下载结果文件查看。本示例中结果文件为2025-05-30--11_prefix- 5209****-8287-4948-8a80-9912e097****-0.ext。 实时计算（流计算）

## 作业开发

### 模板中心

#### 代码模板

Flink提供了丰富的代码模板，每种代码模板都为您提供了具体的使用场景、代码示例和使用指导。您可以通过代码模板快速地了解Flink产品功能和相关语法，实现自己的业务逻辑。本文为您介绍代码模板的使用场景和操作步骤。

**注意事项**

如果该模板中不包含INSERT INTO语句，则不支持部署该作业。

**支持的模板**

Flink全托管支持的模板和其使用场景详情如下表所示，具体请以控制台为准。

| 模板类别 | 模板名称 | 使用场景 |
|---|---|---|
| 基础模板 | 创建表 | 如果您需要创建表并保存在Catalog中，则可以使用DDL创建表。对表的操作和数据库类似。 |
|  | 创建临时表 | 如果您只需要在当前会话或SQL脚本中使用某些表，则可以使用临时表。 |
|  | 创建临时视图 | 如果您需要在Flink SQL开发过程中，重用代码，组织长查询或者SQL脚本来简化开发，则可以使用临时视图。 |
|  | INSERT INTO | 如果您需要将查询结果写入到外部存储系统中的表，从而提供给下游应用程序，则可以使用INSERT INTO语法。 |
|  | STATEMENT SET | 如果您需要将查询的结果输出到下游的两到多个外部系统中，则可以使用STATEMENT SET语法。 |
|  | Watermark | 如果您希望Flink可以正确处理乱序数据，则需要使用Watermark。您可以在建表DDL中创建一个Watermark，即在一个已有字段上定义一个 Watermark生成表达式，标记这个字段为时间属性字段。详情请参见Event Time and Watermarks。 |
|  | GROUP BY | 如果您需要实时对数据进行聚合分析，则可以使用GROUP BY语句。 |
|  | 滚动窗口聚合 | 如果您需要对时间序列数据进行分组，并对每个分组内的数据进行聚合分析，则可以使用滚动窗口。 |
|  | 滑动窗口聚合 | 如果您需要每间隔一段时间更新一个窗口内的数据，则可以使用滑动窗口。 |

|  | link企业版用户指南 |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | 聚合分析 |  |  |  |  |  |
|  |  | 累积窗口聚合 | 如果您需要提早看到窗口的计算结果，例如每分钟看到最新的窗口结果，则可以使用累积窗口。 说明累积窗口聚合不支持CDC，使用CDC后语法校验会报错 org.apache.flink.table.api.TableException: Not |  |  |  |
|  |  |  |  | 说明累积窗口聚合不支持CDC，使用CDC后语法校验会报错 org.apache.flink.table.api.TableException: Not |  |  |
|  |  |  |  |  | org.apache.flink.table.api.TableException: Not |  |
|  |  |  |  | supported window type: CUMULATE(max size=[xxx _ |  |  |
|  |  |  |  | ms], step=[xxx min]) |  |  |
|  |  | 会话窗口聚合 | 如果您需要实时统计用户在一个活跃会话期间的数据，则可以使用会话窗口。 |  |  |  |
|  |  | Over窗口聚合 | 如果您需要对一个窗口内的每个元素进行统计分析，则需要使用OVER窗口。 |  |  |  |
|  |  | 级联窗口聚合 | 如果您需要同时对同一个流的数据进行不同时间维度（例如1min、 5min、30min、1h）的聚合，则可以使用级联窗口。 |  |  |  |
|  | 去重模板 | 去重 | 如果您需要去除数据流中的重复数据，则可以使用去重语法。 |  |  |  |
|  | Top-N模板 | Top-N | 如果您需要根据业务要求计算出当前排名前几位或者后几位的数据，则可以使用Top-N语法。 |  |  |  |
|  |  | 窗口Top-N | 如果您需要在某个时间范围内计算出目前排名前几位或者后几位的数据，则可以使用窗口Top-N语法。 |  |  |  |
|  | CEP模板 | 模式检测（CEP） | 在数据流情景中，如果您需要搜索一组事件模式，则可以使用 MATCH RECOGNIZE语法。 _ |  |  |  |
|  | Join模板 | Regular Join | 如果您需要关联查询其他流表的数据进行计算，则可以使用Regular Join语法。 |  |  |  |
|  |  | Interval Join | 如果您需要关联某张表在指定时间范围内的数据，则可以使用Interval Join语法。 |  |  |  |
|  |  | 时态表Join | 如果您需要流表中的每条数据都关联其他表中对应时间版本数据，则可以使用时态表Join。 |  |  |  |
|  |  | 维表Join | 如果您需要关联静态维表上的数据，则可以使用维表Join。 |  |  |  |

**操作步骤**

本文以**创建表**模板为您介绍如何使用代码模板。
1. 登录实时计算Flink版管理控制台。
实时计算（流计算）
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏上，单击**模板中心**。
5. 在**代码模板**页签，单击选中目标模板后，在左下角单击**下一步**。
6. 按需修改**文件名称**、**部署目标**、**存储位置**和SQL代码。
7. 单击**确认**。
实时计算（流计算） 单击**确认**后，就会进入SQL开发页面。后面的操作和正常的作业开发完全相同，参数配置详情和后续操作

#### 数据同步模板

Flink CDC支持数据的实时同步和表结构变更的自动同步。您可以使用数据同步模板帮您快速生成数据同步的Flink SQL作业代码。本文为您介绍如何使用多库多表同步或者分库分表合并模板实现数据同步。

**背景信息**

实时计算Flink版支持多库多表同步和分库分表合并两种数据同步方式，二者的区别请参见下表。

| 同步方式 | 详情 |
|---|---|
| 多库多表同步 | 如果您需要将一个或多个数据库中的一张或多张业务数据表实时复制到另一个数据库时，则可以使用多库多表同步模板。Flink CDC可以自动同步整库的全量和增量数据，同时还能实时将每张源表的表结构变更（加列等）实时同步到对应的目标表中。多库多表同步模板会将您的参数翻译成CDAS语句。 |
| 分库分表合并 | 当同一份业务数据分散在不同的数据库或者业务表时，我们往往需要用到分库分表合并的能力， 将表结构相似的分库分表的数据同步到一张目标表中。Flink CDC可以自动同步源中所有分库分表的全量和增量数据（包括新增的符合正则表达式的新表），同时还能实时将每张源表的表结构变更（加列等）实时同步到对应的目标表中。分库分表合并同步模板会将您的参数翻译成CTAS 语句。 |

**使用限制**

目前仅支持从MySQL到Hologres的数据同步。

**注意事项**

在同步MySQL到Hologres的数据时，会同步表结构变更，同步时需要注意以下几点： 无需您手动在Hologres上创建表。 Flink会自动在Hologres上创建表，但如果Hologres已经存在对应的表，Flink会根据您创建计划中选择的目标库和表信息来映射。 Hologres不支持更改列的类型。 如果当前字段的类型和Hologres下游表中对应的字段类型不同，则会写入失败，您需重修改列类型并重新同步。

**操作步骤**

**配置MySQL和Hologres存储IP**

1. 登录MySQL和Hologres实例，获取实例域名信息。
2. 登录OPS机器，执行 `ping` 命令获取MySQL和Hologre域名对应的IP。
3. 配置MySQL和Hologres存储IP，请参见配置外部存储IP。

**创建MySQL Catalog和Hologres Catalog**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏上，单击**作业开发**，单击**Schemas**，单击+图标后，单击**创建****Catalog**。
实时计算（流计算）
5. 选择MySQL并配置Catalog信息，单击**确认**。

| 参数 | 说明 |
|---|---|
| catalog name | 自定义catalog名称。 |
| hostname | MySQL数据库服务器的IP地址或主机名。 |
| port | 连接到服务器的端口，默认是3306。 |
| default-database | 默认数据库名称。 |
| username | 连接MySQL数据库服务器时使用的用户名。 |
| password | 连接MySQL数据库服务器时使用的密码。 |

6. 同上步骤，选择Hologres并配置Catalog信息，单击**确认**。
实时计算（流计算）

| 参数 | 说明 |
|---|---|
| catalog name | 自定义catalog名称。 |
| endpoint | Hologres的Endpoint地址。 |
| username | 用户名为企业AccessKey ID。 |
| password | 密码为企业AccessKey Secret。 |
| dbname | Hologres的数据库名称。 |

**数据同步**

1. 在左侧导航栏上，单击**模板中心**。
2. 在**数据同步**页签，单击**MySQL**到**Hologres****数据同步**模板名称，左下角单击**下一步**。
3. 配置数据同步信息。
实时计算（流计算） i. 配置源/**目标选择**，并填写**MySQL****配置项**，单击**下一步**。

| 类别 | 配置项 | 详情 |
|---|---|---|
| 源 | MySQL Catalog | 您可以直接选择已创建好的MySQL Catalog。如果您没有提前创建好源MySQL Catalog，则请单击创建Catalog进行创建。 |
|  | MySQL server-id | 每个MySQL数据库客户端的唯一ID。取值范围为 5400~6400。该参数也支持ID范围的格式，例如5400- 5408。推荐在开启增量读取模式多并发读取数据时，设置该参数为ID范围，因为这样可以使得每个并发使用不同的ID。 重要不要和其他访问数据库的作业或者服务使用同一个 Server ID。 |
| 目标 | Hologres Catalog | 您可以直接选择已创建好的目标Hologres Catalog。如果您没有提前创建好目标Hologres Catalog，则请单击创建 Catalog进行创建。 |

ii. 创建计划。 实时计算（流计算） 多库多表同步 a. 在**多库多表同步**页签下，选中目标的源库和表名称。 b. 单击**保存计划**，单击**下一步**。 c. 查看系统根据您选择的目标库和表生成对应的SQL代码，单击**确认**。 您可以根据需要修改**文件名称**、**部署目标**和**存储位置**信息。 分库分表合并实时计算（流计算） a. 在**分库分表合并**页签下，选中目标的源库和表名称，或者直接输入您创建的目标库和表名称。

**说明**

推荐您使用正则表达式填写源库和源表信息。 b. 单击**保存计划**，单击**下一步**。 在一个作业中，可以同时创建多个多库多表同步和分库分表合并的计划。 c. 查看系统根据您选择的目标库和表生成对应的SQL代码，单击**确认**。 您可以根据需要修改**文件名称**、**部署目标**和**存储位置**信息。 作业创建后，就会进入作业开发页面。后面的操作和正常的作业开发完全相同，参数配置详情和后续操作

### SQL作业开发

**使用限制**

实时计算（流计算） 实时计算Flink版仅支持开源Flink V1.11、Flink V1.12、Flink V1.13、Flink V1.15、Flink V1.17版本。

## 作业开发

为了方便您编写和管理Flink SQL作业，提高作业开发效率，Flink全托管产品为您提供Flink SQL的全套功
1. 登录Flink开发控制台，新建作业。
i. 登录实时计算Flink版管理控制台。 ii. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。

| 在 |  |
|---|---|
|  | 。 |

iv. 在左侧导航栏，单击**作业开发**。 v. 单击**新建**。 实时计算（流计算） vi. 在**新建文件**对话框，填写作业配置信息。

| 作业参数 | 说明 |
|---|---|
| 文件名称 | 作业的名称。 说明作业名称在当前项目中必须保持唯一。 |
| 文件类型 | 流作业和批作业均支持以下文件类型： SQL JAR PYTHON 说明 VVP 2.4.1且VVR 3.0.1及以上版本支持批作业。 |
| 部署目标 | 选择作业需要部署的集群，支持以下两种集群模式： Per-Job集群（默认）：适用于占用资源比较大或持续稳定运行的作业。因为作业之间资源隔离，每个作业都需要一个独立的JM，小任务JM的资源利用率较低。 Session集群：适用于占用资源比较小或任务启停比较频繁的作业。因为多个作业可以复用相同的JM，可以提高JM资源利用率。 说明如果您需要开启SQL Preview功能，必须选择Session集群，且已将其设置为SQL Previews集群，详情请参见作业调试和配置Session集群。 |
| 存储位置 | 指定该作业的代码文件所属的文件夹。 您还可以在现有文件夹右侧，单击图标，新建子文件夹。 |

vii. 单击**确认**。
2. 在作业开发页面，编写DDL和DML代码。
示例代码如下。 实时计算（流计算） `--`创建源表`datagen_source`。

```
CREATE TEMPORARY TABLE datagen_source(
  name VARCHAR
) WITH (
  'connector' = 'datagen'
);
```

`--`创建结果表`blackhole_sink`。

```
CREATE TEMPORARY TABLE blackhole_sink(
  name  VARCHAR
) WITH (
  'connector' = 'blackhole'
);
```

`--`将源表数据插入到结果表。

```
INSERT INTO blackhole_sink SELECT
  name
from datagen_source;
```

3. 在作业开发页面右侧，单击**高级配置**，填写配置信息。
参数解释如下表所示。

| 类别 | 配置项 | 说明 |
|---|---|---|
| 基础配置 | 部署目标 | 您可以修改创建作业时已选择的部署目标。 |
|  | 附加依赖文件 | 如果您需要添加更多依赖文件，请选择或者输入任意合法的文件地址。 说明 Session集群不支持设置附加依赖文件，仅Per-Job集群支持设置附加依赖文件。 |
| 常规配置 | 引擎版本 | 当前作业使用的Flink的引擎版本。 |
|  | 编辑标签 | 您可以为作业设置标签。后续可以通过搜索的方式，快速找到目标作业。 |
|  | Checkpoint间隔 | 定时执行Checkpoint的时间间隔。如果不填写，将会关闭 Checkpoint。 |
|  | 两次Checkpoint之间的最短时间间隔 | 两次Checkpoint之间的最短时间间隔，如果Checkpoint最大并行度是1，则该配置确保两个Checkpoint之间有一个最短时间间隔。 |

| Flink配置 |  |  |
|---|---|---|
|  | 开启Unaligned Checkpoint | 开启Unaligned Checkpoint会大大降低反压情况下 Checkpoint的总执行时间。但是也会导致增大单次 Checkpoint的大小。 |
|  | Flink重启策略配置 | 当有Task失败时，如果没有开启Checkpoint，JobManager 进程不会重启。如果开启了Checkpoint，则JobManager进程会重启。该参数取值如下： Failure Rate：基于失败率重启。 Fixed Delay：固定间隔重启。 No Restarts（默认值）：不会重启。 |
|  | 更多Flink配置 | 在此设置其他Flink配置。例如 taskmanager.numberOfTaskSlots: 1 。 |
| 日志配置 | Root Log Level | 日志级别从低到高顺序如下： TRACE：比DEBUG更细粒度的信息。 DEBUG：系统运行状态的信息。 INFO：重要或者您感兴趣的信息。 WARN：系统可能出现潜在错误的信息。 ERROR：系统出现错误和异常的信息。 |
|  | Logger name | 填写日志名称。 |
|  | Logger level | 填写日志名称和日志级别。 |
|  | Logging Profile | 日志模板，可以选择系统模板，也可以选择用户配置。 |

4. （可选）在作业开发页面右侧，单击**代码结构**，查看数据来源和流向。
**数据流向图**：您可以通过数据流向图快速查看数据的流向。
**树状结构图**：您可以通过树状结构图快速查看数据的来源。
5. （可选）在作业开发页面右侧，单击**版本信息**，查看历史版本信息。
您还可以在此区域，对比、回滚、锁定和删除目标版本。
6. 单击**保存**。
7. 单击**验证**。
8. 单击**上线**。
完成作业开发和语法检查后，即可上线作业，将数据发布至生产环境。
9. 按需填写上线备注信息，单击**确认**。

### JAR作业开发

Flink JAR提供了更灵活的编程模型和API，可以自定义各种数据转换、操作和算子，适用于复杂的业务逻辑和数据处理需求。本文为您介绍Flink JAR作业的开发方法和调试方法。 实时计算（流计算）

**使用限制**

由于Flink受部署环境、网络环境等因素的影响，所以开发Flink DataStream或Table API作业，需要注意以下限制： 仅支持开源Flink V1.10、Flink V1.11和Flink V1.12版本。 仅支持JAR形式的作业提交和运行。 支持一个主JAR包和多个附加依赖JAR包。 不支持在Main函数中读取本地配置。 产品运行环境使用的是JDK 1.8，作业开发也需要使用JDK 1.8。 仅支持开源Scala V2.11版本。

**注意事项**

为了避免JAR包依赖冲突，您需要注意以下几点： Flink镜像和Pom依赖Flink版本请保持一致。 请不要上传Runtime层的JAR包，即在依赖中添加 `<scope>provided</scope>` 。 其他第三方依赖请采用Shade方式打包，Shade打包详情请参见Apache Maven Shade Plugin。

## 作业开发

您需要在线下完成作业开发后，再在Flink开发控制台上提交作业到集群上运行。您在编写Flink业务代码时，可以参见以下文档： Apache Flink简介，以及它的体系架构、应用程序和特性功能等，请参见Apache Flink介绍。 Flink Datastream和TableAPI Connector依赖，请参见Connector依赖。 Connector的使用方法，请参见Connector使用。 Apache Flink V1.10业务代码开发，请参见Flink DataStream API开发指南和Flink Table API & SQL 开发指南。 Apache Flink的编码、Java语言、Scala语言、组件和格式等指南，请参见代码风格和质量指南。 Apache Flink编码过程中遇到的问题及解决方法，请参见常见问题。

**Connector使用**

Maven中央库中已经放置了VVR Connector，以供您在作业开发时直接使用。您可以使用以下任意一种方式来使用Connector： 直接将Connector作为项目依赖打进作业JAR包。 需要在作业的Maven POM文件中添加您需要的Connector作为项目依赖，示例如下。

```xml
<dependencies>
    <dependency>
        <groupId>com.alibaba.ververica</groupId>
        <artifactId>${connector.type}</artifactId>
        <version>${connector.version}</version>
    </dependency>
</dependencies>
```

每个Connector版本对应的Connector类型可能不同，建议您使用最新版本。Connector版本、 实时计算（流计算）

**重要**

您需要在SNAPSHOT仓库（oss.sonatype.org）查找带SNAPSHOT的Connector版本，在Maven 中央库（search.maven.org ）上会查找不到。 上传Connector JAR包到Flink开发控制台后，填写配置信息。 i. 登录实时计算Flink版管理控制台。 ii. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。

| 在 | N |
|---|---|
| 台 | 。 |

iv. 在左侧导航栏，单击**资源上传**。 v. 单击**上传资源**，选择您要上传的目标Connector的JAR包。 您可以上传您自己开发的Connector，也可以上传Flink提供的Connector。Flink提供的Connector官方JAR包的下载地址，请参见Connector列表。 vi. 在左侧导航栏，单击**作业开发**。 vii. 在目标作业开发页面的基础配置中的**附加依赖文件**项中，选择目标Connector的JAR包。 viii. 在右侧的**高级配置** **> Flink** **配置** > **更多** **Flink** **配置**项中，添加配置。 假如您的作业需要依赖多个Connector JAR包，且名字分别为connector-1.jar和connector-2.jar， 则配置信息如下。

```
pipeline.classpaths: 'file:///flink/usrlib/connector- 1.jar;file:///flink/usrlib/connector-2.jar'
```

### Python作业开发

本文为您介绍Python API作业开发的背景信息、使用限制、开发方法、调试方法和Connector使用等。

**背景信息**

Flink集群已安装下列软件包。

| 软件包 | 版本 |
|---|---|
| apache-beam | 2.23.0 |
| avro-python3 | 1.9.1 |
| certifi | 2020.12.5 |
| chardet | 4.0.0 |
| cloudpickle | 1.2.2 |
| crcmod | 1.7 |

实时计算（流计算）

| cython | 0.29.16 |
|---|---|
| dill | 0.3.1.1 |
| docopt | 0.6.2 |
| fastavro | 0.23.6 |
| future | 0.18.2 |
| grpcio | 1.29.0 |
| hdfs | 2.6.0 |
| httplib2 | 0.17.4 |
| idna | 2.10 |
| jsonpickle | 1.2 |
| mock | 2.0.0 |
| numpy | 1.19.5 |
| oauth2client | 3.0.0 |
| pandas | 0.25.3 |
| pbr | 5.5.1 |
| pip | 20.1.1 |
| protobuf | 3.15.3 |
| py4j | 0.10.8.1 |
| pyarrow | 0.17.1 |

实时计算（流计算）

| pyasn1-modules | 0.2.8 |
|---|---|
| pyasn1 | 0.4.8 |
| pydot | 1.4.2 |
| pymongo | 3.11.3 |
| pyparsing | 2.4.7 |
| python-dateutil | 2.8.0 |
| pytz | 2021.1 |
| requests | 2.25.1 |
| rsa | 4.7.2 |
| setuptools | 47.1.0 |
| six | 1.15.0 |
| typing-extensions | 3.7.4.3 |
| urllib3 | 1.26.3 |
| wheel | 0.36.2 |

**使用限制**

由于实时计算Flink产品受部署环境、网络环境等因素的影响，所以开发Python作业，需要注意以下限制： 支持开源Flink V1.13及以上版本。 实时计算Flink集群已预装了Python 3.7.9，且Python环境中已预装了Pandas、NumPy、PyArrow等常用的Python库。因此需要您在Python 3.7版本开发代码。 实时计算Flink运行环境使用的是JDK1.8，如果Python作业中依赖第三方JAR包，请确保JAR包兼容 JDK1.8。 仅支持开源Scala V2.11版本，如果Python作业中依赖第三方JAR包，请确保使用Scala V2.11对应的 JAR包依赖。

## 作业开发

实时计算（流计算） 您需要在线下完成Python API作业开发后，再在实时计算Flink开发控制台上提交作业到集群上运行。您可以参见以下文档开发实时计算Flink产品业务代码： Apache Flink V1.12业务代码开发，请参见Flink Python API开发指南。 Apache Flink编码过程中遇到的问题及解决方法，请参见常见问题。

### 作业调试

您可以在Python自定义函数的代码实现中，通过logging的方式，输出日志信息，方便后期问题定位，示例如下。

```python
@udf(result_type=DataTypes.BIGINT()) def add(i, j):
  logging.info("hello world")
  return i + j
```

日志输出后，您可以在TaskManager的日志文件查看。

**Connector使用**

Connector使用方法如下：
1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏，单击**资源上传**。
5. 单击**上传资源**，选择您要上传的目标Connector的JAR包。
您可以上传您自己开发的Connector，也可以上传实时计算Flink产品提供的Connector。实时计算Flink 产品提供的Connector官方JAR包的下载地址，请参见Connector列表。
6. 在左侧导航栏，单击**作业开发**。
7. 在目标作业开发页面的基础配置中的**附加依赖文件**项中，选择目标Connector的JAR包。
8. 在右侧的**高级配置** **> Flink** **配置** > **更多** **Flink** **配置**项中，添加配置。
假如您的作业需要依赖多个Connector JAR包，且名字分别为connector-1.jar和connector-2.jar，则配置信息如下。

```
pipeline.classpaths: 'file:///flink/usrlib/connector- 1.jar;file:///flink/usrlib/connector-2.jar'
```

### 使用Python依赖

您可以在Flink Python作业中使用自定义的Python虚拟环境、第三方Python包、JAR包和数据文件等，本文为您介绍如何在Python作业中使用这些依赖。

**背景信息**

使用自定义的Python虚拟环境使用第三方Python包使用JAR包使用数据文件

**使用自定义的Python虚拟环境**

实时计算（流计算） 当前仅支持Python 3.7的Python虚拟环境，下文为您介绍如何准备Python 3.7的虚拟环境。
1. 准备Python 3.7的虚拟环境。
i. 在本地准备bulid.sh脚本，其内容如下。

```bash
#!/bin/bash
set -e -x yum install -y zip wget cd /root/ bash /build/setup-pyflink-virtual-env.sh mv venv.zip /build/
```

ii. 在本地准备 `setup-pyflink-virtual-env.sh` 脚本，其内容如下。

```
set -e
```

# 下载`Python 3.7 miniconda.sh`脚本。

```
wget "https://repo.continuum.io/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh" -O "miniconda.sh"
```

# 为`Python 3.7 miniconda.sh`脚本添加执行权限。

```
chmod +x miniconda.sh
```

# 创建`Python`的虚拟环境。

```
./miniconda.sh -b -p venv
```

# 激活`Conda Python`虚拟环境。

```
source venv/bin/activate ""
```

# 安装`PyFlink`依赖。

```bash
# update the PyFlink version if needed
pip install "apache-flink==1.12.1"
```

# 关闭`Conda Python`虚拟环境。

```
conda deactivate
```

# 删除缓存的包。

```
rm -rf venv/pkgs
```

# 将准备好的`Conda Python`虚拟环境打包。

```
zip -r venv.zip venv
```

iii. 在CMD命令行，执行如下命令。

```bash
docker run -it --rm -v $PWD:/build -w /build quay.io/pypa/manylinux2014_x86_64 ./b uild.sh
```

执行完该命令后，会生成一个名字为**venv.zip**的文件，即为**Python 3.7**的虚拟环境。 您也可以修改上述脚本，在虚拟环境中安装所需的第三方Python包。
2. 在Python作业中使用Python 3.7虚拟环境。
i. 登录实时计算开发控制台。 实时计算（流计算） ii. 在左侧导航栏，单击**资源上传**，上传venv.zip文件。

**说明**

实时计算Flink开发控制台上可以上传文件大小的限制为200 MB，而Python虚拟环境的大小通常会超过该限制，因此，您需要通过OSS管理控制台上传文件。 iii. 在目标作业开发页面的**Python Archives**项，选择venv.zip文件。 iv. 单击右侧的**高级配置**，在**更多****Flink****配置**项，添加配置信息。

```
python.executable: venv.zip/venv/bin/python
```

v. 单击**保存**。

**使用第三方Python包**

下面将从以下两个场景为您介绍如何使用第三方Python包： 使用可直接Import的第三方Python包如果您的第三方Python包是Zip Safe的，即不需要安装即可直接在Python作业中使用。操作步骤如下： i. 下载可直接Import的第三方Python包。 a. 在浏览器上打开PyPI页面。 b. 在搜索框中输入目标第三方Python包名称，例如**apache-flink 1.12.2**。 c. 在搜索结果中，单击目标结果名称。 d. 在左侧导航栏，单击Download files。 e. 单击文件名中包含**cp37-cp37m-manylinux1**的包名称进行下载。 ii. 登录实时计算开发控制台。 iii. 在左侧导航栏，单击**资源上传**，上传第三方Python包。 iv. 在目标作业开发页面的**Python Libraries**项，选择所上传的第三方Python包。 v. 单击**保存**。 使用需要编译的第三方Python包如果您的第三方Python包是**tar.gz**格式的压缩包，或从其他地方下载的源码包，且压缩包的根目录下存在**setup.py**文件，则这种类型的第三方Python包通常需要先编译才能被使用。您需要先在与Flink兼容的环境下编译第三方Python包，然后才可在Python作业中调用第三方Python包。 推荐使用**quay.io/pypa/manylinux2014_x86_64**镜像容器中的**Python 3.7**来编译第三方Python 包，使用该容器编译生成的包兼容绝大多数Linux环境，关于该镜像容器的更多信息请参见manylinux。

**说明**

**Python 3.7**的安装路径为 **/opt/python/cp37-cp37m/bin/python3**。
下面以**opencv-python-headless**第三方Python包为例，介绍一下如何编译和使用该第三方Python 包。 i. 编译第三方Python包。 实时计算（流计算） a. 在本地准备**build.sh**脚本，其内容如下。

```bash
#!/bin/bash
set -e -x yum install -y zip PYBIN=/opt/python/cp37-cp37m/bin "${PYBIN}/pip" install --target __pypackages__ -r requirements.txt --no-deps cd __pypackages__ && zip -r deps.zip . && mv deps.zip ../ && cd .. rm -rf __pypackages__
```

b. 在本地准备**requirements.txt**文件，其内容如下。

```
opencv-python-headless
```

c. 在CMD命令行，执行如下命令。

```bash
docker run -it --rm -v $PWD:/build -w /build quay.io/pypa/manylinux2014_x86_64 / bin/bash build.sh
```

该命令执行完后，会生成一个名字为**deps.zip**的文件，该文件为编译之后的第三方Python包。 您也可以修改**requirements.txt**，安装其他所需的第三方Python包。此外，**requirements.txt**文件中可以指定多个Python依赖。 ii. 在Python作业中使用第三方Python包**deps.zip**。 a. 登录实时计算开发控制台。 b. 在左侧导航栏，单击**资源上传**，上传**deps.zip**。

**说明**

实时计算Flink产品限制可上传的最大文件大小为200 MB，而Python虚拟环境的大小通常会超过该限制，需要通过OSS管理控制台进行文件上传。 c. 在目标作业开发页面的**Python Libraries**项，选择**deps.zip**。 d. 单击**保存**。

**使用JAR包**

如果您的Flink Python作业中使用了Java类，例如作业中使用了Connector或者Java自定义函数时，可以通过如下方式来指定Connector或者Java自定义函数的JAR包。
1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**资源上传**，上传需要使用的JAR包。
3. 在目标作业开发页面的**附加依赖文件**项，选择需要使用的JAR包
4. 单击右侧的**高级配置**，在**更多****Flink****配置**项，添加配置信息。
假如需要依赖多个JAR包，且名字分别为**jar1.jar**和**jar2.jar**，配置内容如下。

```
pipeline.classpaths: 'file:///flink/usrlib/jar1.jar;file:///flink/usrlib/jar2.jar'
```

5. 单击**保存**。

**使用数据文件**

下面将从两个场景为您介绍如何使用数据文件： 实时计算（流计算） 通过Python Archives选项方式如果您的数据文件的数量比较多时，您可以将数据文件打包成一个ZIP包，然后通过如下方式在Python作业中使用。操作步骤如下： i. 登录实时计算开发控制台。 ii. 在左侧导航栏，单击**资源上传**，上传需要数据文件ZIP包。 iii. 在目标作业开发页面的**Python Archives**项，选择需要使用的数据文件ZIP包。 iv. 在Python自定义函数中，可以通过如下方式访问数据文件。假如数据文件所在压缩包名称为**mydata.zip**。

```python
def map():
    with open("mydata.zip/mydata/data.txt") as f:
    ...
```

通过附加依赖文件选项如果您的数据文件数量比较少时，可以通过如下方式在Python作业中使用。操作步骤如下： i. 登录实时计算开发控制台。 ii. 在左侧导航栏，单击**资源上传**，上传需要的数据文件ZIP包。 iii. 在目标作业开发页面的**附加依赖文件**项，选择需要的数据文件。 iv. 在Python自定义函数中，可以通过如下方式访问数据文件。假如数据文件名称为**data.txt**。

```python
def map():
    with open("/flink/usrlib/data.txt") as f:
    ...
```

### 作业调试

您可以使用作业调试功能模拟作业运行、检查输出结果，验证SELECT或INSERT业务逻辑的正确性，提升开发效率，降低数据质量风险。本文为您介绍如何进行作业调试。

**背景信息**

您可以在Flink开发控制台使用作业调试功能本地验证作业逻辑的正确性，而不会将数据实际写入您生产的下游中（无论您使用什么样的结果表）。使用调试功能时，您可以使用上游的线上数据或指定调试数据。调试可以包含多个SELECT或INSERT的复杂作业。此外，查询语句支持UPSERT，即可以执行 `count(*)` 等包含更新操作的语句。

**前提条件**

作业调试功能需要使用Session集群，已创建Session集群。详情请参见配置Session集群。

**使用限制**

仅SQL类型的作业支持作业调试。 CTAS和CDAS语法不支持调试。 Flink默认读取最多1000条数据后会自动暂停。 Session集群调试不支持无限期运行，每次调试最长仅持续三分钟，以确保集群生命周期的可控性与稳定性。

**操作步骤**

1. 进入作业开发页面，新建SQL作业。
i. 登录实时计算Flink版管理控制台。 实时计算（流计算） ii. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。

| 在 | N |
|---|---|
| 台 | 。 |

iv. 在左侧导航栏，单击**作业开发**。 v. 单击**新建**。 vi. 填写作业信息，单击**确认**。

| 作业参数 | 说明 | 示例 |
|---|---|---|
| 文件名称 | 作业的名称。 说明作业名称在当前项目中必须保持唯一。 | test sql _ |
| 文件类型 | 仅SQL类型的作业支持作业调试。 | 流作业/SQL |
| 部署目标 | 选择已创建的Session集群。 | vvp-workload |
| 存储位置 | 指定该作业的代码文件所属的文件夹。默认存放在作业开发目录。 您还可以在现有文件夹右侧，单击图标，新建子文件夹。 | 作业开发 |

2. 分别注册源表和结果表。
分别编写源表和结果表SQL代码后，单击**执行**。注册成功的表会出现在**Schemas**页签中的**Tables**列表中，您可以单击表名，查看表的字段和数据类型信息。 以注册datagen源表、blackhole结果表和blackhole_cnt结果表为例，示例代码如下： datagen源表

```
CREATE TABLE `vvp`.`default`.`datagen` (
  `id`   VARCHAR(2147483647),
  `name` VARCHAR(2147483647)
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '5'
);
```

blackhole结果表

```
CREATE TABLE `vvp`.`default`.`blackhole` (
  `id` VARCHAR(2147483647),
  `name` VARCHAR(2147483647)
) WITH (
  'connector' = 'blackhole'
);
```

blackhole_cnt结果表实时计算（流计算）

```
CREATE TABLE `vvp`.`default`.`blackhole_cnt` (
  `cnt` BIGINT
) WITH (
  'connector' = 'blackhole'
);
```

3. 编写调试DML语句。
以从datagen中读取数据后，一个直接写入blackhole中，另一个取总数后写入blackhole_cnt中为例， 代码如下。

```
BEGIN STATEMENT SET; insert into `blackhole`
  select *
    from `datagen`;
insert into `blackhole_cnt`
  select count(*)
    from `datagen`;
END;
```

4. 单击**验证**。
在SQL编辑页面下方，您可以看到SQL语法校验结果。
5. 单击**执行**。
6. 配置调试数据。
如果您使用线上数据，直接单击**执行**即可。如果您需要使用调试数据，需要先上传调试数据。 参数解释如下表所示。

| 配置项 | 说明 |
|---|---|

实时计算（流计算）

| 下载调试数据模板 | 为了便于编辑，您可以直接下载调试数据模板，模板已适配源表的数据结构。 |
|---|---|
| 上传调试数据 | 如果您需要使用本地调试数据进行调试，您可以先下载好调试数据模板，在本地编辑好数据后上传，并选中使用调试数据。 调试数据文件存在以下限制： 上传文件仅支持CSV格式。 CSV格式的文件必须含有表头，例如 id(INT)。 调试数据CSV文件最大支持1 MB或1千条记录。 |
| 预览数据 | 上传好调试数据后，单击源表名称左侧的图标，可以预览数据和下载调试数据。 |
| 执行代码预览 | 调试功能会自动改变源表和结果表的DDL代码，但不会改变作业中的实际代码。您可以在下方预览代码详情。 |

7. 确定好调试数据后，单击**执行**。
单击**执行**后，会在SQL编辑器下方显示调试结果。

**说明**

Flink默认读取最多1000条数据后会自动暂停。

### 作业上线

本文为您介绍如何提交JAR类型的作业至集群运行。

**上传JAR包**

JAR类型的作业运行前，需要您按照以下步骤将JAR包上传到Flink开发控制台。
1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏，单击**资源上传**。
5. 单击**上传资源**，选择您要上传的JAR包。

**创建作业**

1. 登录Flink开发控制台，新建作业。
实时计算（流计算） i. 在左侧导航栏，单击**作业开发**。 ii. 单击**新建**。 iii. 在**新建文件**对话框，填写作业配置信息。

| 作业参数 | 说明 |
|---|---|
| 文件名称 | 作业的名称。 说明作业名称在当前项目中必须保持唯一。 |
| 文件类型 | 流作业和批作业均支持以下文件类型，此处需要选择JAR类型的作业。 SQL JAR PYTHON 说明 VVP 2.4.1且VVR 3.0.1及以上版本支持批功能。 文件类型请选择为JAR。 |
| 部署目标 | 选择作业需要部署的集群，支持以下两种集群模式： Per-Job集群（默认）：适用于占用资源比较大或持续稳定运行的作业。因为作业之间资源隔离，每个作业都需要一个独立的JM，小任务 JM的资源利用率较低。 Session集群：适用于占用资源比较小或任务启停比较频繁的作业。 因为多个作业可以复用相同的JM，可以提高JM资源利用率。 说明如果您需要开启SQL Preview功能，必须选择Session集群，且已将其设置为SQL Previews集群，详情请参见作业调试和配置 Session集群。 |
| 存储位置 | 指定该作业的代码文件所属的文件夹。 您还可以在现有文件夹右侧，单击图标，新建子文件夹。 |

iv. 单击**确认**。
2. 在作业开发页面，填写基本配置信息。

| 参数 | 说明 |
|---|---|
| 部署目标 | 您可以修改创建作业时已选择的部署目标。 |

实时计算（流计算）

| JAR URI | 请选择一个文件或者手动上传新文件，您可以拖拽文件到此区域或者单击右侧图标选择文件上传。 |
|---|---|
| Entry Point Class | 程序的入口类。 说明如果您的JAR包未指定主类，请在此处输入您的Entrypoint Class类的标准路径。 |
| Entry Point Main Arguments | 您可以在此处传入参数，在主方法里面去调用该参数。 |
| 附加依赖文件 | （推荐）选择您已上传的目标附加依赖文件。 您需要提前通过Flink开发控制台左侧资源上传或作业开发页面附件依赖文件右侧的上传附件依赖文件。上传的附件依赖文件会固定被保存在oss://ossBucketName/artifacts/namespaces/namespace Name/* 目录。 填写目标附加依赖文件的OSS路径。 您需要提前将附加依赖文件上传至当前实例对应的OSS Bucket， 上传附加依赖文件的OSS Bucket必须为您开通Flink时选择的OSS Bucket。 填写目标附加依赖文件的URL，目前仅支持以文件名结尾的URL， 例如http://xxxxxx/file。 您需要提前将附加依赖文件上传至公开可访问的HTTP服务。 说明以上三种方式上传的附加依赖文件，在作业运行时，最终都会被加载到JM和TM所在Pod的/flink/usrlib目录下。 Session模式的作业不支持配置附加依赖文件路径。 |

3. 在作业开发页面右侧，单击**高级配置**，根据业务需要填写配置信息。

| 类别 | 配置项 | 说明 |
|---|---|---|
| 常规配置 | 引擎版本 | 当前作业使用的Flink的引擎版本。 |
|  | 编辑标签 | 您可以为作业设置标签。后续可以通过搜索的方式，快速找到目标作业。 |
|  | Checkpoint间隔 | 定时执行Checkpoint的时间间隔。如果不填写，将会关闭 Checkpoint。 |

| k企业版用户指南·作业开发 | 实时计算（流计算） |  |
|---|---|---|
| Flink配置 |  |  |
|  | 两次Checkpoint之间的最短时间间隔 | 两次Checkpoint之间的最短时间间隔，如果 Checkpoint最大并行度是1，则该配置确保两个 Checkpoint之间有一个最短时间间隔。 |
|  | 开启Unaligned Checkpoint | 开启Unaligned Checkpoint会大大降低反压情况下 Checkpoint的总执行时间。但是也会导致增大单次 Checkpoint的大小。 |
|  | Flink重启策略配置 | 当有Task失败时，如果没有开启 Checkpoint，JobManager进程不会重启。如果开启了Checkpoint，则JobManager进程会重启。该参数取值如下： Failure Rate：基于失败率（您填写时间间隔内的最大失败次数）重启。 Fixed Delay：固定间隔重启。 No Restarts：默认值，不会重启。 |
|  | 更多Flink配置 | 在此设置其他Flink配置。例如 taskmanager.numberOfTaskSlots: 1 。 |
| 日志配置 | Root Log Level | TRACE、DEBUG、INFO、WARN和ERROR。 |
|  | Logger name | 填写日志名称。 |
|  | Logger level | 填写日志名称和日志级别。 |
|  | Logging Profile | 日志模板，可以选择系统模板，也可以选择用户配置。 |

4. 在作业开发页面右上角，单击**上线**。
5. 按需填写上线备注信息，单击**确认**。

### 变量配置

本文介绍如何通过变量配置功能对密钥进行脱敏处理。

**注意事项**

3.16.2 SP10及以上版本支持SQL作业密钥脱敏功能。

**新增变量**

为密钥定义一个关联的变量名。
1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在**变量配置**页面，单击**新增变量**。
实时计算（流计算）

| 参数 | 说明 |
|---|---|
| 变量名 | 同一个项目空间下保持唯一，创建后不支持修改。 |
| 变量值 | 填写密钥，大小写敏感，填写时请注意字母大小写。 |

**使用变量**

通过引用变量实现对显式定义密钥的隐蔽处理，以达到密钥的脱敏效果。在SQL作业中通过 ${secret_values.变量名} 格式引用变量。在使用时，只需将密钥替换为变量名，其余部分保持不变。 示例如下：

```
CREATE TEMPORARY TABLE datagen_table (strname VARCHAR)
 with (
    'connector' = 'datagen', 'rows-per-second' = '10'
); CREATE TEMPORARY table datahub_table (strname VARCHAR) with (
    'connector' = 'datahub',
    'endpoint' = 'https://datahub.cn-***.com',
    'project' = 'cms',
    'topic' = 'source',
    'accessId' = '${secret_values.datahub_access_key}',      -- 使用变量名替换原accessId
    'accessKey' = '${secret_values.datahub_access_secret}'   -- 使用变量名替换原accessKey
); INSERT INTO datahub_table select * from datagen_table;
```

实时计算（流计算）

## 数据连接

### 管理自定义Connectors

本文为您介绍如何管理Flink自定义Connectors，包括创建、更新和删除。

**背景信息**

在使用Flink SQL开发作业时，需要使用SQL Connectors连接您的源表、结果表和维表。Flink支持云上常用的多种类型的Connectors，但相对于目前大数据常用的技术栈而言，仍然只是较少的一部分，为了支持您可以使用更多类型的Connectors，我们支持您自定义Connectors后上传使用。在使用过程中，您需要注意以下事项： 您需要根据社区定义的Connectors标准开发您自定义的Connectors，才能正确的被Flink识别并使用， 因此您需要明确的Connector Meta文件和申明Factory类。自定义Connector开发详情请参见Userdefined Sources & Sinks。 同种类型的Connectors仅可以上传一次。 为了避免JAR包依赖冲突，您需要注意以下几点： Flink镜像和Pom依赖的Flink版本请保持一致。 请不要上传Runtime层的JAR包，即在依赖中添加 `<scope>provided</scope>` 。 其他第三方依赖请采用Shade方式打包，Shade打包详情参见Apache Maven Shade Plugin。

**创建自定义Connectors**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏，单击**作业开发**。
5. 在**Connectors**页签，单击
图标。
6. 上传自定义Connectors JAR文件。
实时计算（流计算） 您可以通过以下任何一种方式上传自定义Connectors JAR文件：
**上传文件**：单击**选择文件**后，选择您的目标Connectors JAR文件。本文以此方式为例。
**外部****URL**：输入外部URL地址。
7. 上传完成后，单击**继续**。
系统会对您上传的自定义Connectors内容进行解析。如果解析成功，您可以继续下一步。如果解析失败，请确认您上传的自定义Connectors代码是否符合Flink社区标准。
8. 查看上传的Connector信息，可以按需修改配置信息。
实时计算（流计算）

| 参数 | 说明 |
|---|---|
| Connector | 目标Connectors JAR文件名称，系统会自动生成。 |
| Lookup | 能否作为Lookup表，按需开启。 |
| Formats | 选择支持的Format，单击输入框，选择目标Format。 |
| Properties | 按需修改属性。 |

9. 单击**完成**。
创建完成的自定义Connectors会出现在Connectors列表中。 实时计算（流计算）

**更新自定义Connectors**

1. 在**Connectors**页签，鼠标悬停在目标自定义Connectors名称上，单击
图标。
2. 上传自定义Connectors JAR文件。
您可以通过以下任何一种方式上传自定义Connectors JAR文件：
**上传文件**：单击**选择文件**后，选择您的目标Connectors JAR文件。本文以此方式为例。
**外部****URL**：输入外部URL地址。
3. 上传完成后，单击**继续**。
系统会对您上传的自定义Connectors内容进行解析。如果解析成功，您可以继续下一步。如果解析失败，请确认您上传的自定义Connectors代码是否符合Flink社区标准。
4. 单击**完成**。
创建完成的自定义Connectors会出现在Connectors列表中。 实时计算（流计算）

**删除自定义Connectors**

如果您的自定义Connectors不再使用，您可以按照以下步骤删除自定义Connectors。
1. 在**Connectors**页签，鼠标悬停在目标自定义Connectors名称上，单击
图标。
2. 单击**确认**。
实时计算（流计算）

## 运维管理

### 作业管理

#### 作业启动

完成作业开发和上线后，您需要在作业运维页面启动作业至运行阶段。此外，作业在暂停或者停止后需要恢复时，需要启动作业。本文为您介绍如何启动作业以及作业启动后的状态变化及状态含义。

**背景信息**

作业启动的场景如下： 上线后启动：您可以选择全新启动（无状态），并可以指定读取数据的时间。 停止后启动：停止作业时，系统会自动清除作业相关的Checkpoint信息。作业停止后启动时，您可以选择全新启动（无状态），同时您也可以指定读取数据的时间；或者从所选Savepoint开始恢复作业。

**使用限制**

仅Flink1.13及以上版本的界面上支持设置启动位点。作业启动界面指定的读取数据时间优先级高于作业 DDL代码里设置的**startTime**。即如果您在作业DDL和作业启动界面都指定了读取数据时间，则作业启动界面指定的读取数据时间生效。

#### 作业启动

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏，单击**作业运维**。
5. 单击目标作业名称**操作**列中的**启动**。
6. 在**作业启动配置**对话框，进行资源配置和Flink参数配置后，单击**下一步**。
7. 选择**启动策略**后，单击**启动**。
实时计算（流计算）
8. 查看作业状态变化。
单击**启动**后，您可以看到作业从当前状态到期望状态的变化过程及最终结果。 作业的运行状态及含义如下表所示。 期望状态

| 状态 | 说明 |
|---|---|
| RUNNING | 期望作业正常运行。 |
| SUSPENDED | 期望作业暂停运行。 |
| CANCELLED | 期望作业停止运行。 |

当前状态

| 状态 | 说明 |
|---|---|
| RUNNING | 作业正常运行。 |
| CANCELLED | 作业停止运行。 |
| SUSPENDED | 作业暂停运行。 |
| FINISHED | 作业运行完成。 |
| TRANSITIONING | 作业处于向期望状态的过渡阶段。 |

实时计算（流计算）

| FAILED | 作业向期望状态转换失败，需要手动处理。 |
|---|---|
| ClusterUnreachable | VVP无法访问JM（JobManager），获取不到Job的状态。 |

#### 作业停止

更改了SQL逻辑或作业版本、增删WITH参数或增加作业参数后，需要经过作业停止和启动的步骤，才能使变更生效。本文为您介绍如何停止状态为RUNNING的作业。

**注意事项**

作业停止后再启动时，您可以选择全新启动（无状态），同时您也可以指定读取数据的时间；或者从所选 Savepoint恢复作业。详情请参见作业启动。

**说明**

如果您修改了SQL等逻辑导致State不兼容，则只能从无状态启动作业。

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏上，单击**作业运维**。
5. 单击目标作业**操作**列下的**停止**。
6. 单击**确认**。
更多设置中的选项说明如下：
**停止前创建一次快照**：如果您需要在停止前创建一次快照，则需要先单击**更多设置**，然后选中**停止前创**
**建一次快照**。选中**停止前创建一次快照**，作业会先进行快照创建，然后进入停止流程。如果您未选中停
**止前创建一次快照**，则作业会直接进入停止流程。
**输出窗口数（****Drain**）：该选项用于永久性终止作业，具体原理请参见Drain。

**重要**

如果您希望稍后再重新启动作业，请不要选中该选项。因为恢复作业时，可能会出现错误的结果。 实时计算（流计算）

### 元数据管理

#### 管理自定义函数（UDF）

在SQL作业中使用自定义函数，需要先注册自定义函数（UDF）。本文为您介绍如何注册、更新和删除自定义函数。

**注意事项**

为了避免JAR包依赖冲突，您需要注意以下几点： Flink镜像的版本请与Pom依赖中的Flink版本保持一致。 请不要上传Runtime层的JAR包，即在依赖中添加 `<scope>provided</scope>` 。 其他第三方依赖请采用Shade方式打包，Shade打包详情参见Apache Maven Shade Plugin。

**注册自定义函数**

如果您的SQL需要使用自定义函数，您需要先注册您的自定义函数，才能在SQL中使用。
1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏上，单击**作业开发**。
5. 在**UDFs**页签，首次注册直接点击**注册****UDF**，也可点击右上角
图标。
6. 上传自定义函数JAR文件，单击**确认**。
实时计算（流计算） 您可以通过以下任何一种方式上传自定义函数JAR文件：
**上传文件**：单击**选择文件**项右侧的**选择文件**后，选择您的目标自定义函数Artifact文件。如果有依赖文
件，单击**依赖文件**项右侧的**选择文件**，选择您的目标自定义函数Artifact所依赖的文件。
**外部****URL**：输入外部URL地址。
Flink开发控制台会解析您自定义函数JAR文件中是否使用了Flink UDF、UDAF和UDTF接口的类，并自动提取类名，填充到Function Name字段中。 对于Java类型的自定义函数，其依赖可以打包到自定义函数JAR包中，也可以通过依赖文件项进行上传；对于Python类型的自定义函数，推荐通过单独上传依赖文件方式上传依赖。 在自定义函数Artifact文件或者其依赖文件比较大时，推荐通过外部URL的方式进行上传。需要注意的是，如果外部URL是OSS Bucket地址，其依赖文件必须位于sqlartifacts/namespaces/{namespace}目录下。

**说明**

Bucket目录至少需要公共读权限，URL路径只支持HTTP协议，且不可带编码字符。
7. 在**管理** **Functions**弹框中，确认函数信息，单击**创建** **Function**。
注册成功后，弹框会显示当前**已注册的** **Function**的信息。此时，您可以按需移除不需要的函数。 实时计算（流计算） 移除后，界面显示如下。确认函数信息无误后，关掉弹框。
8. 在SQL编辑器页面左侧的**UDFs**列表中，您可以看到所有注册成功的自定义函数。
实时计算（流计算） 如果您需要对已注册的自定义函数JAR文件进行函数添加或者移除，您可以按照以下步骤管理自定义函数 JAR文件。
1. 在**UDFs**页签中，鼠标悬停在目标自定义函数名称上，单击
图标。
2. 添加或者移除目标函数。

**更新自定义函数**

如果您的自定义函数JAR文件中，新增了自定义函数或已注册了自定义函数的代码变更，您可以按照以下步骤更新自定义函数JAR文件。
1. 在**UDFs**页签中，鼠标悬停在目标自定义函数名称上，单击
图标。
2. 管理自定义函数。
您可以通过以下任何一种方式上传自定义函数JAR文件： 实时计算（流计算）
**上传文件**：单击**选择文件**项右侧的**选择文件**后，选择您的目标自定义函数Artifact文件。如果有依赖文
件，单击**依赖文件**项右侧的**选择文件**，选择您的目标自定义函数 Artifact所依赖的文件。
**外部****URL**：输入外部URL地址。

**重要**

您上传的新自定义函数JAR文件中，必须包含当前已经注册自定义函数的所有类，不能出现某个已注册自定义函数的类消失的情况。 只有重启作业或提交新作业时，才会使用新自定义函数JAR文件中的代码。如果引用该自定义函数JAR的作业正在运行，则依然会使用旧自定义函数JAR文件。
3. 单击**修改**。

**删除自定义函数**

如果您的自定义函数JAR文件不再使用，您可以按照以下步骤删除自定义函数。
1. 在左侧导航栏上，单击**作业开发**。
2. 在**UDFs**页签中，鼠标悬停在目标自定义函数名称上，单击
图标。

**说明**

在删除自定义函数JAR文件前，请确定其注册的自定义函数没有被作业或SQL文件引用。
3. 选中**Drop****以上所有****Functions****并且删除关联的****JAR** 。
如果您要删除该自定义函数JAR文件，则需要删除该自定义函数JAR中所有注册的自定义函数，避免有脏数据残留。
4. 单击**确认**。

#### 管理Hologres Catalog

配置Hologres Catalog后，您就可以在Flink全托管控制台直接读取Hologres元数据，不用再手动注册 Hologres表，可以提高作业开发的效率且保证数据的正确性。本文为您介绍如何在Flink全托管模式下配置、查看及删除Hologres Catalog。

**背景信息**

Catalog提供了元数据信息，例如数据库、表、分区、视图以及数据库或其他外部系统中存储的函数和信息。详情请参见Catalogs。 配置Hologres Catalog 查看Hologres Catalog 使用Hologres Catalog 删除Hologres Catalog

**使用限制**

Flink 1.13及以上版本支持配置Hologres Catalog。 不支持修改Catalog DDL。

**配置Hologres Catalog**

实时计算（流计算）

**UI方式（推荐）**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**作业开发**。
3. 在**Schemas**页签，单击
图标。
4. 单击**创建** **Catalog**，在弹框中选择**Hologres**。
5. 填写参数配置信息。

| 参数 | 说明 | 是否必填 |
|---|---|---|
| catalogname | 自定义Hologres Catalog名称。 仅支持小写字母a-z和数字0-9，不含大写字母、中划线（-）、下划线（ ）等特殊字符。 _ | 是 |
| endpoint | Hologres的连接地址，<host>:<port>。 | 是 |
| username | 与dbname相匹配的用户名，为Hologres所在组织的AccessKey ID。 | 是 |
| password | 与dbname相匹配的密码，为Hologres所在组织的 AccessKey Secret。 | 是 |
| dbname | Hologres的数据库名称。 在目标Hologres实例中已完成数据库的创建，否则创建Catalog会报错。 | 是 |

6. 单击**确认**。
实时计算（流计算）
7. 单击
图标，在**Schemas**页签下再单击图标，查看新建的Hologres Catalog。本文以holocatalog 为例。

**SQL命令**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**作业开发**。
3. 单击**新建**，填写文件配置信息，**文件类型**选择为**流作业****/SQL**。
4. 在文本编辑区域，输入配置Hologres Catalog的命令。

```
CREATE CATALOG <catalogname> WITH (
  'type' = 'hologres',
  'endpoint' = '<endpoint>',
  'username' = '<AccessKey>',
  'password' = '<AccessSecret>',
  'dbname' = '<dbname>'
);
```

| 参数 | 说明 | 是否必填 |
|---|---|---|
| <catalogname> | 自定义Hologres Catalog名称。 仅支持小写字母a-z和数字0-9，不含大写字母、中划线 （-）、下划线（ ）等特殊字符。 _ | 是 |
| type | 类型，固定值为hologres。 | 是 |
| endpoint | Hologres的连接地址，格式为： <host>:<port> 。 | 是 |

实时计算（流计算）

| username | 与dbname相匹配的用户名，为Hologres所在组织的 AccessKey ID。 | 是 |
|---|---|---|
| password | 与dbname相匹配的密码，为Hologres所在组织的 AccessKey Secret。 | 是 |
| dbname | Hologres的数据库名称。 在目标Hologres实例中已完成数据库的创建，否则创建 Catalog会报错。 | 是 |

5. 单击**执行**。
执行完会提示 `Query has been executed` 。如果您需要删除Hologres Catalog，详情请参见删除 Hologres Catalog。
6. 在左侧单击**Schemas**页签，并单击
图标。
7. 单击
图标，查看新建的Hologres Catalog。本文以holocatalog为例。

**查看Hologres Catalog**

Hologres Catalog配置成功后，您可以通过以下步骤查看Hologres元数据。
1. 在左侧导航栏，单击**作业开发**。
2. 单击**Schemas**页签。
3. 单击
图标，选择目标Hologres Catalog名称。
4. 查看Hologres Catalog下的数据库、表和函数信息。

**说明**

如果Schema为public时，则表名称前面就省略了Schema的前缀，即直接显示tableName。 实时计算（流计算）

**使用Hologres Catalog**

创建Hologres表。 使用 `USE CATALOG HoloName` 命令直接引用Hologres数据服务。

```
USE CATALOG ${catalog_name}; CREATE TABLE `${db_name}`.`${schema_name.table_name}`(
  ...
 ) WITH (
   'connector' = 'hologres'
 );
```

USE语法详情请参见USE语句。 DDL语句中直接引用Hologres数据服务信息。

```
CREATE TABLE `${catalog_name}`.`${db_name}`.`${schema_name.table_name}` (
  ...
) WITH (
  'connector' = 'hologres'
);
```

**说明**

在已注册的Hologres数据服务下创建表时，WITH参数中connector为必填参数，且取值为hologres。可省略endpoint等其他参数。 目前不支持直接在Hologres表中添加或修改WITH参数，可以通过SQL hints的方式在 INSERT语句中添加或修改WITH参数。 从Hologres表中读取数据。

```
INSERT INTO ${other_sink_table} SELECT ... FROM `${catalog_name}`.`${db_name}`.`${schema_name.table_name}`
```

写入结果数据至Hologres表。

```
INSERT INTO `${catalog_name}`.`${db_name}`.`${schema_name.table_name}` SELECT ... FROM ${other_source_table}
```

**说明**

如果Schema为public时，在填写**${schema_name.table_name}**时，可以省略模式名称的前缀，直接填写tableName，即${table_name}。

**删除Hologres Catalog**

**UI方式（推荐）**

1. 在左侧导航栏，单击**作业开发**。
2. 在**Schemas**页签下单击
图标，找到目标Catalog。 实时计算（流计算）
3. 单击右侧的
图标，确认删除信息后，单击**删除**。

**SQL方式**

1. 在左侧导航栏，单击**作业开发**。
2. 单击**新建**，填写文件配置信息，**文件类型**选择为**流作业****/SQL**。
3. 在文本编辑区域，输入以下命令。

```
DROP CATALOG ${catalog_name}
```

其中，catalog_name为您要删除的在Flink全托管开发控制台上显示的Hologres Catalog名称。

**说明**

删除Hologres Catalog不会影响已运行的作业，但对未上线或者作业需要暂停恢复的作业，均产生影响，请您谨慎操作。
4. 单击**执行**。
5. 在左侧单击**Schemas**页签，再单击
图标。
6. 查看新建的Hologres Catalog，确认已被删除。

#### 管理MySQL Catalog

创建MySQL Catalog后，您可以在Flink控制台直接访问Catalog下MySQL实例中的表，并在Flink SQL作

**背景信息**

MySQL Catalog具有以下功能特点： 直接访问MySQL实例中的表，无需通过DDL语句手动注册MySQL表，提升开发效率和正确性。 MySQL Catalog提供的表可以直接作为Flink SQL作业中的MySQL CDC源表、MySQL结果表和MySQL 维表。 实时计算（流计算） 支持RDS MySQL、PolarDB MySQL或自建MySQL。 支持直接访问分库分表逻辑表。 支持配合CDAS和CTAS语法完成基于MySQL数据源的整库同步、分库分表合并同步、表结构变更同步。

**前提条件**

已创建MySQL实例，并获取了实例的相关基本信息。 网络互通配置要求：需确保MySQL实例侧和Flink控制台侧两端均已正确配置白名单。 MySQL实例侧：通过**设置白名单**功能添加Flink SQL作业所在的IP网段至白名单。 Flink控制台侧：通过**配置外部存储** **IP** 功能添加MySQL实例的VIP地址至白名单。

**使用限制**

创建后不支持修改Catalog配置信息。如需修改，请删除后重新创建。 仅支持查询已有数据库和表，不支持通过Flink创建数据库和表。 作为源表时仅支持流读、不支持批读。

**说明**

MySQL Catalog提供的表作为MySQL CDC源表时，需要在RDS MySQL、PolarDB MySQL或者自建MySQL上开启Binlog等配置。 无法识别建表语句中使用PolarDB特有语法的表。

| PARTITION BY KEY(`idempotent id`) PARTITIONS 16, UNIQUE KEY `uk order id` _ _ _ |  |
|---|---|

创建Catalog后不支持使用视图作为Flink的表。 MySQL仅支持5.7和8.0.x版本。

**配置MySQL Catalog**

**UI方式（推荐）**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**作业开发**。
3. 在**Schemas**页签，单击
图标。 实时计算（流计算）
4. 单击**创建** **Catalog**，在弹框中选择**MySQL**。
5. 填写参数配置信息。

| 参数 | 说明 | 是否必填 |
|---|---|---|
| catalogname | 自定义MySQL Catalog名称，需满足以下要求： 仅由小写字母、数字和- 、.符号组成，不能以符号结尾。 | 是 |
| hostname | MySQL数据库的IP地址或者主机名。 | 是 |
| port | MySQL数据库服务的端口号，默认值为3306。 | 是 |
| default-database | 默认的MySQL数据库名称。 | 是 |
| username | 连接MySQL数据库服务器时使用的用户名。 | 是 |
| password | 连接MySQL数据库服务器时使用的密码。 | 是 |

6. 单击**确认**。
7. 在**Schemas**页签下单击
图标，再单击图标，查看新建的MySQL Catalog。本文以mysqlcatalog 为例。 实时计算（流计算）

**SQL命令**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**作业开发**。
3. 单击**新建**，填写文件配置信息，**文件类型**选择为**流作业****/SQL**。
4. 在文本编辑区域，输入配置MySQL Catalog的命令。

```
CREATE CATALOG YourCatalogName WITH(
  'type' = 'mysql',
  'hostname' = 'rm-bp1gcn0q0j0******.mysql.rds.aliyuncs.com',
  'port' = '3306',
  'username' = 'usertest',
  'password' = '${secret_values.mysqlpw}',
  'default-database' = 'flinktest',
  'catalog.table.metadata-columns'='table_name'
);
```

| 参数 | 说明 | 是否必填 |
|---|---|---|
| YourCatalogNam e | 自定义MySQL Catalog名称。 | 是 |
| type | 类型，固定值为mysql。 | 是 |
| hostname | MySQL数据库的IP地址或者Hostname。 | 是 |
| port | MySQL数据库服务的端口号，默认值为3306。 | 否 |
| username | MySQL数据库服务的用户名。 | 是 |

实时计算（流计算）

| password | MySQL数据库服务的密码。 | 是 |
|---|---|---|
| default-database | 默认的MySQL数据库名称。 | 是 |

5. 单击**执行**。执行完会提示 `Query has been executed` 。
6. 在左侧单击**Schemas**页签，并单击
图标。
7. 单击
图标，查看新建的MySQL Catalog。本文以mysqlcatalog为例。

**查看和删除MySQL Catalog**

**UI方式（推荐）**

1. 在左侧导航栏，单击**作业开发**。
2. 在**Schemas**页签下单击
图标，找到目标Catalog。 实时计算（流计算）
3. 单击右侧的
图标，确认删除信息后，单击**删除**。

**SQL方式**

1. 在左侧导航栏，单击**作业开发**。
2. 单击**新建**，填写文件配置信息，**文件类型**选择为**流作业****/SQL**。
3. 在文本编辑区域，输入以下命令。
`--`查看`Catalog`下表在`Flink`中对应的`Schema`信息，暂不支持展示字段`comment`信息。

```
DESCRIBE `<catalogname>`.`<dbname>`.`<tablename>`;
```

`--`删除`Catalog`

```
DROP CATALOG `<catalogname>`;
```

**重要**

删除操作仅删除创建的Catalog，不会在相应服务中删除这些表。删除Catalog后使用该 Catalog下表的已运行作业不受影响，但重新部署或启动时会报错（无法找到该表），请您谨慎操作。
4. 单击**执行**。
5. 在左侧单击**Schemas**页签，再单击
图标。
6. 单击
图标，查看新建的MySQL Catalog，确认已被删除。 实时计算（流计算）

**使用MySQL Catalog**

**从MySQL源表中读取数据**

```
INSERT INTO `<othersinktable>` SELECT ... FROM `<mysqlcatalog>`.`<dbname>`.`<tablename>` /*+ OPTIONS('server-id' = '6000-6008') * /;
```

MySQL Catalog作为MySQL CDC源表时，建议使用Table Hints来为作业指定不同的 server-id。如果源表需要多并发读取，server-id还需要配置成范围格式，范围中的server-id个数需要大于等于并发度。

**读取MySQL分库分表逻辑表**

MySQL Catalog支持使用正则表达式，将库名和表名作为逻辑表名，来读取分库分表的数据。 例如，有一个分库分表的MySQL数据库，包括user01、user02和user99等多个表，分散在db01~db10 等数据库中，且所有表的Schema都相互兼容，则可以通过如下正则表达式的库名表名访问到所有user的分库分表。

```
SELECT ... FROM `db.*`.`user.*` /*+ OPTIONS('server-id'='6000-6018') */;
```

分库分表的逻辑表会返回额外的_db_name (STRING) 和_table_name (STRING)两个系统字段，且这两个字段与原分表的主键会作为逻辑表的新联合主键以保证主键的唯一性。如果user01~user99的主键均为 id，则user逻辑表的联合主键为（_db_name, _table_name, id）。 MySQL Catalog支持结合正则表达式匹配所要同步的多张表，实现分库分表合并同步。

**使用CTAS和CDAS实时同步MySQL数据变更和结构变更**

**说明**

|  | CREATE TABLE ... AS TABLE ... statement requires target catalog ... implements |
|---|---|
| org.apache.flink.table.catalog.CatalogTableProvider interface. |  |

CTAS支持单表同步、表结构变更同步、分库分表合并同步、自定义计算列同步，支持新增CTAS语句加入数据同步作业。 实时计算（流计算） CDAS支持整库级别的表结构和数据的实时同步，以及表结构变更的同步。 `--` 单表同步，实时同步表级别的表结构变更和数据变更。

```
CREATE TABLE IF NOT EXISTS `<targetcatalog>`.`<targetdbname>`.`<targettablename>` WITH (...) AS TABLE `<mysqlcatalog>`.`<dbname>`.`<tablename>` /*+ OPTIONS('server-id'='6000-6018') */;
```

`--` 整库同步，实时同步整库级别的表结构变更和数据变更。

```
CREATE DATABASE `<targetcatalog>`.`<targetdbname>` WITH (...) AS DATABASE `<mysqlcatalog>`.`<dbname>` INCLUDING ALL TABLES /*+ OPTIONS('server-id'='6000-6018') */;
```

**从MySQL维表中读取数据**

```
INSERT INTO `<othersinktable>` SELECT ... FROM `<othersourcetable>` AS e JOIN `<mysqlcatalog>`.`<dbname>`.`<tablename>` FOR SYSTEM_TIME AS OF e.proctime AS w ON e.id = w.id;
```

**写入数据至MySQL表**

```
INSERT INTO `<mysqlcatalog>`.`<dbname>`.`<tablename>` SELECT ... FROM `<othersourcetable>`
```

#### 配置Hive Metastore

**背景信息**

您可以将Hive Metastore配置文件和Hadoop依赖存放至对象存储OSS控制台指定目录后，再在Flink开发控制台上配置Hive Metastore功能。配置成功后，您就可以在Flink开发控制台上直接使用DML创建业务逻辑，获取Hive中表的元数据信息，无需再使用DDL语句声明相应的表信息。Hive Metastore可以作为 Stream作业和Batch作业的源表或结果表。

**注意事项**

使用Hive Metastore功能需要注意以下几点： 支持自建Hive Metastore。 VVP 2.3.0及以上版本支持Hive Metastore。 VVP 2.3.0版本仅支持Hive Metastore 2.3.6版本；VVP 2.3.0以上版本支持Hive Metastore 2.2.0~2.3.7。 Hive Metastore不支持Kerberos鉴权。 一个Flink实例仅支持一个Hive Metastore，多项目无法设置多Hive Metastore。 Hive Metastore只读，即您不能通过Flink开发控制台在Hive中创建物理表。
1. 连通Hadoop集群和Flink的VPC。
实时计算（流计算） 您可以使用云解析PrivateZone产品连通Hadoop集群和Flink的VPC。网络连通后，Flink就可以使用 Hadoop集群的配置文件访问Hadoop集群。
2. 在OSS控制台新建文件夹，并将Hive配置文件和Hadoop依赖放置目标路径。
i. 登录OSS控制台。 ii. 在左侧导航栏，单击**Bucket****列表**。 iv. 单击**文件管理**页签，新建文件夹，用于存放Hive配置文件和Hadoop依赖。 Hive配置文件路径：oss://${bucket}/artifacts/namespaces/${ns}/${hms}/hive-conf-dir/ Hadoop依赖路径：oss://${bucket}/artifacts/namespaces/${ns}/${hms}/hadoop-confdir/ 其中：
**${bucket}**：您Flink实例使用的Bucket名称。
**${ns}**：您要使用Hive Metastore功能的Flink项目名称。
**${hms}**：您在Flink上显示的Hive Metastore名称。
v. 将您的Hive配置文件（hive-site.xml）放置到**hive-conf-dir**目录下。 在上传hive-site.xml文件前，请您先检查下配置文件中**hive.metastore.uris**参数配置是否符合下列要求。

```xml
<property>
    <name>hive.metastore.uris</name>
    <value>thrift://xx.yy.zz.mm:9083</value>
    <description>Thrift URI for the remote metastore. Used by metastore client to c
onnect to remote metastore.</description>
 </property>
```

其中 `xx.yy.zz.mm` 为Hive的内网IP或者公网IP，如果您将**hive.metastore.uris**填写为 hostname，则VVP远程访问Hive时，**hive.metastore.uris**参数值会被解析失败并报

```
错 UnknownHostException 。
```

vi. 将您的以下配置文件放置到**hadoop-conf-dir**目录下。 hive-site.xml core-site.xml hdfs-site.xml mapred-site.xml 其他文件，例如Hive作业使用的压缩包。
3. 在Flink开发控制台上配置Hive Metastore服务。
i. 登录实时计算开发控制台。 ii. 在左侧导航栏，单击**作业开发**。 iii. 在页面左上角，单击**新建**。 iv. 填写文件名称、文件类型选择SQL，选择部署目标和存储位置。 实时计算（流计算） v. 在作业开发页面文本编辑区域，输入创建Hive Metastore的命令。

```
CREATE CATALOG ${HMS-Name} WITH (
    'type' = 'hive',
    'default-database' = 'default',
    'hive-version' = '<hive-version>',
    'hive-conf-dir' = '<hive-conf-dir>'
    'hadoop-conf-dir' = '<hadoop-conf-dir>'
);
```

其中：
**${HMS-Name}**：Hive Metastore名称。
**type**：Connector类型，固定值为hive。
**default-database**：默认数据库名称。
**hive-version**：Hive Metastore版本号。

**说明**

Hive Metastore版本兼容为**2.2.0~2.3.7**，其中：
**2.0.0~2.2.0**：**hive-version**需要指定为**2.2.0**
**2.3.0~2.3.7**：**hive-version**需要指定为**2.3.6**。
**hive-conf-dir**：存放Hive配置文件的目录。
**hadoop-conf-dir**：存放Hadoop依赖的目录。
vi. 单击**运行**。 Hive Metastore服务配置完成后，您就可以在作业中引用Hive Metastore表信息，作为结果表和维表，无需声明表的DDL。Hive Metastore表名称格式为**${hive-catlog-name}.${hive-db-**
**name}.${hive-table-name}**。
此外，如果您想停用Hive Metastore服务，详情请参见删除Hive Metasore服务。

**查看Hive元数据**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**作业开发**。
3. 在**Schemas**页签的顶部菜单栏下拉框中，切换到目标Hive Metastore。
实时计算（流计算）
4. 在**Tables**列查看不同数据库下的表和字段信息。

**删除Hive Metasore服务**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**作业开发**。
3. 在**作业开发**页面文本编辑区域，输入以下命令。

```
 Drop CATALOG ${HMS-Name}
```

其中， ${HMS-Name} 为您要删除的在Flink开发控制台上显示的Hive Metastore名称。

**重要**

删除Hive Metastore服务不会影响已运行的作业，但对未上线或者作业需要暂停恢复的作业，均产生影响，请您谨慎操作。
4. 单击**运行**。

### 配置Session集群

您可以使用Session集群模式部署或调试作业，提高作业JM（Job Manager）资源利用率和作业启动速度。 本文介绍实时计算Flink中Session集群的使用建议及创建方法。

**重要**

Session集群仅适用于测试，请勿生产环境使用，且不支持容灾。

**背景信息**

实时计算Flink支持Per-Job集群和Session集群两种集群模式。两种集群模式有以下区别： Per-Job集群（默认）：作业之间资源隔离，每个作业都需要一个独立的JM，小任务JM的资源利用率较低。因此，适用于占用资源比较大或持续稳定运行的作业。 实时计算（流计算） Session集群：多个作业可以复用相同的JM，可以提高JM资源利用率。因此适用于占用资源比较小或任务启停比较频繁的作业，可以有效节约资源开销。

**说明**

每个项目空间可以配置多个Session集群，但只能选择一个Session集群开启SQL Preview 。该配置项的详细说明请参见本文参数解释中的**设置为****SQL Previews****集群**。 Session集群暂不支持开启自动调优功能。 无论您是否使用Session集群，在创建Session集群时会消耗集群资源，其中消耗的资源和您创建集群时选择的资源配置有关。 VVR 3.0.4及以下版本的每个Session集群运行后，都会额外消耗0.5 CU的资源。

**使用限制**

Session集群有以下限制： 暂停Session集群后，不支持修改Flink计算引擎版本。 暂停Session集群后，不支持对TM个数或资源进行缩容。 不支持显示数据曲线。 不支持监控告警功能。

**注意事项**

JobManager单点故障会对集群内的所有作业造成影响。 TaskManager单点故障会对在其上有task运行的相关作业造成影响。 同一个TaskManager内部，不同Task之间如果没有进程隔离，则存在相互影响的潜在风险。 如果Session集群为默认配置，则有以下建议： 对于单并发的小作业，建议整个集群的作业总数不超过100个。 对于复杂作业，建议单作业最大并发数不超过512，64个并发的中等规模作业单集群不多于32个。否则可能会出现心跳超时等问题影响集群稳定性。此时，您需要增大心跳间隔和心跳超时时间。 如果您需要同时运行更多的任务，则需要增加Session集群的资源配置。 不建议使用开启了SQL Preview的Session集群运行作业。因为如果产品后续发布新版本，则需要停止 Session集群后，手动适配Flink计算引擎，否则本地调试会报错。

**创建Session集群**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏上，单击**Session****集群**。
5. 单击**创建****Session****集群**，填写配置信息。
实时计算（流计算） 参数解释如下表所示。

| 模块 | 配置项 | 说明 |
|---|---|---|
| 基础配置 | 名称 | 集群名称。 |
|  | 状态 | 设置当前集群的期望运行状态： STOPPED：当集群配置完成后保持停止状态，同样会停止所有在运行中的作业。 RUNNING：当集群配置完成后保持运行状态。 |
|  | 设置为SQL Previews集群 | 将此Session集群设置为SQL Preview查询的资源集群。 说明每个项目空间只能有一个Session集群开启SQL Preview，开启此设置将取消之前为SQL Preview设置的Session集群。 |
|  | 标签名 | 您可以在标签选项中添加作业标签，便于在总览页面快速定位作业。 |
|  | 标签值 | 无。 |

实时计算（流计算）

| 配置 | 引擎版本 | 当前作业使用的Flink的引擎版本。 说明 Python API作业需要选择vvr-2.1.4-flink 1.11及以上版本。 |
|---|---|---|
|  | Flink重启策略配置 | 该参数取值如下： No Restarts：不重启。 Fixed Delay：固定延迟。选择该选项后，您还需要填写尝试重启的次数和每次重启时间间隔。 Failure Rate：故障率。选择该选项后，您还需要填写检测故障率的时间间隔，时间间隔内的最大失败次数和每次重启时间间隔。 说明如果您没有配置该参数，则按Apache Flink默认的重启策略，即当有Task失败时，如果没有开启 Checkpoint，JobManager进程不会重启。如果开启了 Checkpoint，则JobManager进程会重启。 |
|  | 其他配置 | 在此设置其他Flink配置。例如 taskmanager.numberOfTaskSlots: 1 。 |
|  | Task Managers 数量 | 默认与并行度一致。 |
|  | JobManager CPU Cores | 默认值为1。 |
|  | JobManager Memory | 推荐值：2 GiB，最小值：1 GiB。单位GiB，例如：1 GiB或 1.5 GiB。 JobManager推荐配置包含JobManager资源以及心跳相关参数。具体内容如下： 由于JobManager上承载TaskManager心跳、作业Task序列化和资源调度等功能。因此建议JobManager资源不小于默认配置，请根据集群负载情况进行处理。 为了集群稳定，避免JobManager主线程繁忙导致心跳超时。因此建议心跳间隔（heartbeat.interval）不小于10 秒，同时心跳超时（heartbeat.timeout）不小于50秒。 请根据TaskManager个数与作业量上涨情况而上调。 |
|  | TaskManager CPU Cores | 默认值为2。 |

实时计算（流计算）

| 资源配置 |  |  |
|---|---|---|
|  | TaskManager Memory | 推荐值：8 GiB，最小值：1 GiB。单位GiB，例如：1 GiB或 1.5 GiB。 TaskManager推荐配置包含单个TaskManager的Slot个数 （taskmanager.numberOfTaskSlots）及TaskManager 资源大小。具体内容如下： 对于单并发小作业，建议单Slot的CPU内存比为1:4，使用的资源不小于1核2 Gi。 对复杂作业，建议单Slot使用资源不小于1核4 Gi。在默认资源配置下，每个TaskManager可以配置2个Slot。 TaskManager资源不宜过小，也不宜过大，推荐默认资源配置并将Slot数目设为2。 说明如果单个TaskManager资源过小，则可能影响其上作业的稳定性，并且由于其Slot数目不多，无法有效平摊TaskManager的开销，降低了资源的利用效率。 如果单个TaskManager资源过大，则 TaskManager上运行的作业数会很多，一旦 TaskManager发生单点故障，影响面会很大。 |
| 日志配置 | Root Log Level | TRACE、DEBUG、INFO、WARN和ERROR。 |
|  | Logger name | 填写日志名称。 |
|  | Logger level | 填写日志级别。 |
|  | Logging Profile | 日志模板，可以选择系统模板，也可以选择用户配置。 |

4. 单击**创建****Session****集群**。
Session集群创建完成后，您需要单击**启动**。启动后，您就可以在创建作业的部署目标中选择此集群。

### 创建作业模板

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏，单击**作业模板**。
5. 在**作业模板**页面，单击**流作业模板**或者**批作业模板**页签，填写作业模板信息。
实时计算（流计算）

| 类别 | 配置项 | 说明 |
|---|---|---|
| Flink配置 | Checkpoint间隔 | 定时执行Checkpoint的时间间隔。如果不填写，将会关闭 Checkpoint。 |
|  | 两次Checkpoint之间的最短时间间隔 | 两次Checkpoint之间的最短时间间隔，如果Checkpoint最大并行度是1，则该配置确保两个Checkpoint之间有一个最短时间间隔。 |
|  | 开启Unaligned Checkpoint | 开启Unaligned Checkpoint会大大降低反压情况下 Checkpoint的总执行时间。但是也会导致增大单次 Checkpoint的大小。 |
|  | Flink重启策略配置 | Flink Default是默认重启策略。当有Task失败时，如果没有开启Checkpoint，JobManager进程不会重启。如果开启了 Checkpoint，则JobManager进程会重启。该参数取值如下： No Restarts：作业任务失败后，不会重启。 Fixed Delay：固定间隔重启。 Failure Rate：基于失败率重启。 |
| 其他配置 | 配置 | 在此设置其他Flink配置。例如： taskmanager.numberOfTaskSlots: 1 。 |
| 日志配置 | Root Log Level | TRACE、DEBUG、INFO、WARN和ERROR。 |
|  | Logger name | 填写日志名称。 |
|  | Logger level | 填写日志级别。 |
|  | Logging Profile | 日志模板，可以选择系统模板，也可以选择用户配置。 |

6. 单击**保存更改**。

### 配置外部存储IP

默认情况下，所有作业的出向流量被禁止，您需要添加IP白名单来允许访问。本文介绍如何配置外部存储 IP，以开放作业的出向流量。

**背景**

为了解决计算逃逸安全漏洞问题，平台采用了开启NetworkPolicy功能。该功能默认禁止所有作业的出向流 NetworkPolicy功能的默认规则如下： 默认禁止所有出向的访问。 允许同NameSpace内的Pod间互相访问。 实时计算（流计算） 允许访问Ververica NameSpace下的HDFS。 允许访问APIServer。 允许访问CoreDNS。 允许访问CMS地址，用于指标数据上报。

**注意事项**

低版本升级到3.18.1及以上版本或者3.18.1及以上版本全新部署场景下，所有NameSpace默认开启

**使用限制**

创建完NameSpace后可以在NameSpace列表页面看到**配置外部存储****IP**按钮。该按钮的权限同**修改****CU**
**数量**按钮，即都要NameSpace的编辑权限才能看到，否则按钮不可见。.
添加的白名单IP或网段不得与黑名单网段存在交集，否则将提示错误。

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**NameSpace****管理**页面，单击目标NameSpace**操作**列下的**配置外部存储****IP**。
4. 单击**+IP****地址**，输入IP信息。
IP地址为存储域名对应的VIP，支持添加单个IP或者Classless Inter-Domain Routing（CIDR）格式的网段，例如： `192.168.0.1` 、 `192.168.0.1/24` 。 如果格式错误会对应报错：
5. 单击**确认**。

**示例**

实时计算（流计算） 在未配置外部存储IP场景下，新建DataHub结果表作业，并启动，作业运行时报错网络连接异常。 实时计算（流计算）

### 资源管理

Flink支持通过资源上传功能存放作业运行时需要的文件或者运行过程中产生的数据文件（例如作业系统检查点、作业快照、日志和JAR包等）。本文为您介绍资源的上传、下载、删除及路径复制等资源管理的相关操作。

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏，选择**应用** > **资源上传**。
5. 进行资源管理操作。

| 操作 | 说明 |  |
|---|---|---|
| 上传资源 | 单击上传资源后选择本地文件上传资源，或者直接将待上传文件拖拽到资源列表区域。 上传后，文件路径格式为 hdfs:///vvp/data/artifacts/namespaces/<Your NameSpace>/<文件名 _ > 。 |  |
|  |  | hdfs:///vvp/data/artifacts/namespaces/<Your NameSpace>/<文件名 _ |
|  | > |  |
| 下载资源 | 单击操作列的下载，可以将文件下载到本地进行查看。 |  |
| 删除资源 | 单击操作列的删除，可以将上传的文件直接删除。 |  |
| 复制路径 | 鼠标悬停在目标资源名称处，右侧出现复制图标，单击图标进行复制。 |  |

### 成员管理

本文为您介绍如何在Flink开发控制台上进行成员角色管理，该功能可以有效管理用户权限、确保数据安全。

**绑定成员角色**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。
3. 在**Namespace** **列表**下找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。
4. 在左侧导航栏上，选择**系统管理** > **成员管理**。
5. 在**成员管理**页面，单击**添加角色绑定**。
实时计算（流计算）
6. 在**添加成员**弹框中，按需选择**角色**信息，并填写**成员信息**。

**角色**

不同角色功能差异如下。

| 功能 | owner | editor | viewer |
|---|---|---|---|
| 查看作业列表 | Y | Y | Y |
| 启停作业 | Y | Y | N |
| 更改作业配置 | Y | Y | N |
| 上传JAR | Y | Y | N |
| 编写SQL | Y | Y | N |
| 注册UDF | Y | Y | N |
| 注册元数据 | Y | Y | N |
| 查看作业模板 | Y | Y | Y |
| 增删改作业模板 | Y | Y | N |
| 管理成员 | Y | N | N |

**成员信息**：您可以在Apsara Uni-manager运营控制台系统界面右上角，单击当前登录用户的头像，
查看**UID**信息。成员信息一旦绑定，不可修改。
7. 单击**确认**。
实时计算（流计算）

**编辑成员角色**

1. 在**成员管理**页面的列表下，找到目标角色。
2. 单击**操作**列下的**编辑**，修改成员角色信息。
3. 单击**确认**。

**删除成员角色**

1. 在**成员管理**页面的列表下，找到目标角色。
2. 单击**操作**列下的**删除**。
3. 确认删除信息后，单击**确认**。

### 作业迁移

本文为您介绍如何将企业版的Flink项目空间的作业迁移到存算分离版的Flink项目空间。

**前提条件**

请确认您登录的企业版账号下已开通存算迁移版Flink集群，并创建了对应的工作空间和项目空间。 当前账号已具备迁移权限。若无迁移权限，需由项目空间所在组织在配置页面为该账号添加 AliyunStreamTransferRole策略。

**注意事项**

项目空间中的资源无需手动迁移。只需创建迁移任务并选择相关作业，单击了**开始迁移**，系统便会自动将该项目空间下的所有资源迁移到目标项目空间，建议您迁移到同一个项目空间的作业时使用同一个迁移任务。 迁移作业前务必使用**停止前创建一次快照**的方式来停止作业。否则，Flink系统在检测到有正在运行的作业时，会提示您是取消迁移任务还是强制迁移。 不支持迁移Session集群，Session集群上运行的作业如果要迁移会被迁移成per-job类型的作业。 同一个任务可以多次运行，已经成功的迁移资源不会再进行迁移。

**操作步骤**

1. 登录实时计算开发控制台，进入作业迁移页面。
i. 登录实时计算Flink版管理控制台。 ii. 在左侧导航栏，选择**Flink****（企业版）** **> NamesPace****管理**。

| 在 | N |
|---|---|
| 台 | 。 |

iv. 在左侧导航栏，单击**作业迁移**。
2. 在**作业迁移**页面，单击**创建迁移任务**。
实时计算（流计算）
3. 填写迁移任务信息后，单击**确认**。

| 配置项 | 说明 |
|---|---|
| 迁移任务名称 | 自定义迁移任务名称。 |
| 目标工作空间 | 选择目标存算分离版的Flink工作空间。 |
| 目标项目空间 | 选择目标存算分离版的Flink项目空间。 |

4. 在迁移任务列表中，单击目标迁移任务**操作**列的**添加**/**查看迁移**资源。
5. 选择迁移的作业。
i. 在**作业资源**页签，按需选择**流作业管理**或**批作业管理**。 实时计算（流计算） ii. 选择迁移的作业和作业快照，单击向右的箭头，单击**确认**。 您可以仅选择迁移作业，或者同时选择迁移作业及其某个状态快照。单击左侧的 ，即可看到作业相关的快照信息。 iii. 在右侧选择作业状态资源后，单击**确认**。
6. 在**作业迁移**页面，找到目标迁移任务，单击**开始迁移**。
迁移完成后，根据资源迁移状态和错误信息判断是否需要重新调整迁移资源后再次进行迁移。迁移状态显示为**成功**的，您就可以在目标的Flink存算分离项目空间查看迁移过来的任务。 实时计算（流计算）

## 作业日志

### 查看启动和运行日志

在作业为运行状态时，您可以查看其启动日志和运行日志。本文为您介绍如何查看启动日志和运行日志。

**背景信息**

| 类型 | 详情 |
|---|---|
| 启动日志 | Flink作业启动之后的日志，即从Flink环境被初始化一直到Job Manager被启动起来的中间日志。 说明启动日志中不包含调度日志，需要在运行事件中去查看相应的日志信息。例如资源不足、交换机IP不足都属于调度方面的问题。 |
| 运行日志 | Flink的Job Manager和Task Managers的日志可以在作业日志页面查看，也可以在Flink UI界面查看。 |

**前提条件**

作业为运行状态。

**注意事项**

支持日志分页，每页显示1 MB，大概会显示8000~9000行日志，基本可以帮您排查错误。如果在第一页还未定位到问题，请注意切换日志查看页码。

**查看启动日志**

1. 进入**作业运维**页面。
ii. 在左侧导航栏，单击**作业运维**。 iii. 在**作业运维**页面，单击目标作业名称，默认展开**作业总览**页面。
2. 在**作业探查**页签，单击左侧的**启动日志**，即可查看启动日志。

**查看运行日志**

**在作业日志页面查看运行日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开**作业总览**页面。
2. 在**作业探查**页面的**运行日志**页签，单击**作业实例**右侧的下拉框，选择正在运行作业。
实时计算（流计算）
3. 查看Job Manager和Task Managers日志。
查看Job Manager日志在**Job Manager**页签下，单击**日志**。 查看Task Managers日志 a. 在**运行****Task Managers**页签下，单击**Path, ID**。 b. 单击**日志**。

**在Flink UI页面查看运行日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开**作业总览**页面。
实时计算（流计算）
2. 在**状态总览**页签下的**操作**行，单击**Flink UI**，默认进入**Apache Flink Dashboard**的**Overview**页
面。

**说明**

作业状态为**运行中**才出现**Flink UI**入口。
3. 在左侧导航栏，单击**Task Managers**或**Job Manager**。
单击**Task Managers** 后，单击目标**Path, ID**，在**logs**页签查看作业Task Manager日志。 单击**Job Manager**后，在**Logs**页签，查看作业Job Manager日志。

### 查看运行异常日志

在作业启动或者运行异常时，您可以查看运行异常日志进行问题排查。本文为您介绍如何查看Job Manager 异常、失效Task Managers日志和慢Checkpoint对应的Task Managers日志。

**背景信息**

| 类型 | 详情 |
|---|---|
| Job Manager异常 | 如果作业出现Failover，导致作业运行失败，则需要查看Job Manager异常。 说明如果Job Manager都没启动起来，不属于Job Manager异常，需要在启动日志中去查看。 |
| 失效Task Managers日志 | 运行状态为正常的作业，不会有失败TM。但是对于风险等级较高的，可能有失败的TM，但 TM又被拉起了，这时可以查看失败的TM归档日志去定位可能的原因。 说明只有开启了日志归档才能查看失效Task Managers日志，并且只能查看日志归档中配置的保留天数之内的失效Task Managers日志。 |
| 慢Checkpoint对应的Task Managers 日志 | 作业运行过程中，如果某个Checkpoint运行耗时较长，您需要查看其具体的原因，则可以查看其关联的TM的日志。 |

**前提条件**

作业实例为运行状态。

**注意事项**

支持日志分页，每页显示1 MB，大概会显示8000~9000行日志，基本可以帮您排查错误。如果在第一页还未定位到问题，请注意切换页码查看日志。

**查看Job Manager异常**

1. 进入**作业运维**页面。
实时计算（流计算） ii. 在左侧导航栏，单击**作业运维**。 iii. 在**作业运维**页面，单击目标作业名称，默认展开**作业总览**页面。
2. 在**作业探查**页签，选择左侧的**异常信息**页签后，查看Job Manager异常信息。

**说明**

在**异常历史**中，您可以查看近7天内产生的异常信息，并过滤异常类型后查看历史异常。

**查看失效Task Managers日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开**作业总览**页面。
2. 在**作业探查**页签，选择**运行日志**后，选择正在运行的作业实例。
3. 单击**失效****Task Managers**页签，查看失效Task Managers日志。

**定位慢Checkpoint并查看对应Task Managers的日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开**作业总览**页面。
2. 查看慢Checkpoint日志信息。
i. 在**作业探查**页签，单击 **Flink Checkpoints**页签，单击**Flink****Checkpoints****历史**。 ii. 查看**End to End Duration**列下的值，确认慢Checkpoint对应的ID。 iii. 单击慢Checkpoint对应的ID左侧的 ，确认慢Checkpoint对应的Operators节点。 iv. 单击Operators节点左侧的 ，展开查看每个SubTasks的情况。 实时计算（流计算） v. 单击慢Checkpoint对应的SubTasks节点对应的**ID**。 vi. 在跳转页面的**运行** **Task Managers >** **日志**页签下，查看慢Checkpoint日志信息。

### 查看Flink审计事件

**背景信息**

云盾安全审计可以帮助您监控并记录阿里云账号的活动，您可以将这些行为事件下载或保存到日志服务 SLS，然后进行行为分析、安全分析、资源变更行为追踪和行为合规性审计等操作。

**操作步骤**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏，鼠标悬浮至**安全管理**，选择**安全审计** > **云盾安全审计**，系统默认进入**安全审计**页面。
3. 在**安全审计**页面，单击**原始日志**页签。
4. 选择**审计类型**为**云产品**，**审计对象**为**vvp****操作日志**，设置**起始时间**后单击**查询**。

**FAQ**

Q：为什么进入审计页面后，原始日志中没有数据？ A：存在以下两种可能情况： 实时计算（流计算） 用户在查询的时间段内未曾操作vvp平台。 用户确实进行了vvp平台的操作，此时需要对日志上报的成功与否进行排查。请联系阿里云技术支持获取排查方案。 Q：为什么进入审计页面后，有原始日志，但是没有审计数据？ A：存在以下两种可能情况： 在审计查询的时间段内，用户未进行高危操作。 用户确实进行了高危操作，但云盾单日日志审计已达到上限，此时需要联系云盾相关同事以调高单日审计上限。

### 修改运行作业日志级别

当INFO级别的日志无法满足您定位问题的需求时，您可以修改打印日志的级别为DEBUG。本文介绍如何动态修改日志级别及使用限制和注意事项。

**背景信息**

系统支持的日志级别从低到高的顺序与下面表格内容中的前后顺序一致。

| 级别 | 详情 |
|---|---|
| DEBUG | 系统运行状态的信息。 |
| INFO | 重要或者您感兴趣的信息。 |

**使用限制**

只支持设置为INFO或DEBUG，不支持设置为其他级别，以避免级别设置太高导致在日志中定位不到原因的问题。 支持修改整个JM的日志级别。 支持修改单个TM日志级别，不能一次性修改所有TM日志级别。如果需要修改所有TM日志级别，则需要您进行单独配置。

**注意事项**

日志级别修改为DEBUG后，会打印DEBUG、INFO、WARN、ERROR级别的日志。 日志级别修改为INFO后，只会打印INFO、WARN、ERROR级别的日志。 修改日志级别后，只会影响新输出的日志，之前已输出的日志不会受到影响。 DEBUG日志的开启会对作业性能造成少许影响。如果您没有定位问题的必要，建议将日志级别设置为 INFO。

**操作步骤**

1. 进入作业运维页面。
ii. 在左侧导航栏，单击**作业运维**。 iii. 在**作业运维**页面，单击目标作业名称，默认展开**作业总览**页面。
2. 在**作业探查**页签，单击左侧**运行日志**，选择正在运行的作业实例。
3. 修改Job Manager或Task Managers日志级别。
实时计算（流计算）

**修改Job Manager日志级别**

a. 在**Job Manager**页签，单击**日志**。 b. 单击**日志级别**右侧的**编辑**。 c. 单击**确定**。 d. 在下拉框中选择目标日志级别。 e. 单击**确认**。

**修改Task Managers日志级别**

a. 在**运行****Task Managers**页签，单击**Path, ID**。 b. 单击**日志**页签。 c. 单击**日志级别**右侧的**编辑**。 d. 单击**确定**。 e. 在下拉框中选择目标日志级别。 f. 修改日志级别后，单击**确认**。 实时计算（流计算） ver

## Flink MCP Server

Flink基于MCP协议，支持通过飞天助理-托管模式调用API获取空间、作业等信息，也可通过自行部署MCP Server方式实现查询，助力用户打造自然语言驱动的数据查询Agent，实现从提问到可视化的智能数据处理全流程。本文介绍使用飞天助理托管模式和自行部署MCP Server的操作方式。

**支持MCP模式**

飞天助理-托管模式飞天助理托管模式开箱即用，无需用户配置，可以直接通过大模型访问。 自行部署MCP Server 用户可以在应用、智能体或AI中自行部署。

**飞天助理-托管模式**

**说明**

使用飞天助理-托管模式前，请先参考**统一云管平台** > **飞天助理****用户指南**文档开启飞天助手。
1. 登录实时计算Flink版管理控制台。
2. 查看系统预设的MCP列表。
在左侧导航栏选择**AI****专栏** **> AI****原生接口****MCP****服务**，查看系统预设的MCP列表。当前系统预设工具如下：

| 工具名称 | 调用接口 | 说明 |
|---|---|---|
| 引擎版本列表查询 | ListFlinkVersions | 列出指定Namespace中支持的Flink引擎版本号，有助于用户选择合适的引擎来创建与运行作业。 |
| 工作空间列表查询 | DescribeWorkspacesFlin kOnOss | 查询当前用户的工作空间列表，有助于用户管理 WorkSpace，优化资源管理。 |
| 工作空间下属命名空间列表查询 | ListNamespacesByWorks paceIdFlinkOnOss | 查询指定工作空间下的NameSpace列表，有助于用户管理NameSpace，优化资源分配与管理。 |
| 用户全量命名空间列表查询 | DescribeNamespacesFlin kOnOss | 查询指定用户下的全量NameSpace列表，有助于用户管理NameSpace，优化资源分配与管理。 |
| 作业列表查询 | ListJobs | 查询指定NameSpace名称，获取作业列表，有助于用户作业管理，优化作业资源与执行计划。 |
| 作业部署列表查询 | ListDeployments | 查询指定NameSpace名称，获取已部署作业的列表信息，有助于用户作业管理，优化作业资源与执行计划。 |

实时计算（流计算） ver

| 用户资源查询 | ListArtifacts | 列出指定命名空间和工作区中的用户资源，有助于用户作业管理，优化作业资源管理。 |
|---|---|---|

3. 使用飞天助理调用预设工具。
i. 在页面顶部单击工具栏中的图标，进入**飞天助理**页。 ii. 在对话框底部单击图标，打开**MCP**开关，单击图标进入**选择** **MCP**页面。 iii. 选择已有的Flink MCP。 iv. 单击**确定**，返回对话框，使用自然语言描述查询内容，例如“查询当前用户的工作空间列表”。 v. 单击右侧的图标发送并执行指令信息。 vi. 等待任务执行结束，您可查看返回的结果信息。

**自行部署MCP Server**

1. 下载MCP服务包。
2. 部署在ECS、容器或云外服务器。
3. 集成至应用或智能体：将MCP作为后端服务嵌入AI应用、智能体（Agent）或RPA流程中。
4. 通过RESTful API调用MCP功能。
