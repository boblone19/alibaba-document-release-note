---
title: "实时计算（流计算） Flink存算分离版 用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260730"
pdf_pages: 129
source_pdf: "19_Flink存算分离版 用户指南_empty-manual.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sc/zh/empty-manual.pdf"
converter: line-classifier (PyMuPDF)
---

# 实时计算（流计算） Flink存算分离版 用户指南

实时计算（流计算） 时计算

## 什么是实时计算

阿里云实时计算（Alibaba Cloud Realtime Compute）是一套基于Apache Flink构建的一站式、高性能实时大数据处理平台，广泛适用于流式数据处理、离线数据处理等多种场景。

**产品特点**

强大的实时处理能力阿里云实时计算集成诸多全链路功能，方便您进行全链路实时计算开发，包括： 强大的流计算引擎。 阿里云实时计算提供Flink SQL，支持各类错误场景的自动恢复，保证故障情况下数据处理的准确性。 支持多种内置函数，包括：字符串函数、日期函数、聚合函数。 精确的计算资源控制，高度保证用户作业的隔离性。 关键性能指标为开源Flink的3到4倍。数据计算延迟优化到亚秒级甚至秒级。单个作业吞吐量可做到百万（记录/秒）级别。单集群规模为数千台。 深度整合各类云数据存储。 托管的实时计算服务不同于开源或者自建的流式处理服务，阿里云实时计算是完全托管的流计算引擎。阿里云可针对流数据运行查询，无需预置或管理任何基础设施。在阿里云实时计算，您可以享受一键启用的流式数据服务能力。 阿里云实时计算天然集成数据存储、数据开发、数据运维、监控报警等功能，方便您以较小成本试用和迁移流式计算。同时，实时计算提供完全租户隔离的托管运行服务。从最上层工作空间，到最底层执行机器，提供高度有效的隔离和全面防护，让您放心使用实时计算。 低廉的人力和集群成本大量优化的SQL执行引擎，提供比原生Flink作业更高效且更廉价的计算作业。在开发成本和运行成本方面，阿里云实时计算均要远低于开源流式框架。 实时计算（流计算）

## 准备工作

### 登录实时计算开发控制台

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
1. 单击左侧导航栏**Workspace****管理**，进入**Workspace****列表**页面。
2. 在目标Workspace中找到目标Namespace，单击**操作**列下的**控制台**，跳转至实时计算开发控制台。

### 进入概览页

实时计算Flink版管理控制台上的概览页面展示了当前工作空间中的项目空间数量信息。

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，单击**Flink****（存算分离版）** > **概览**。
3. 在**实例概览**区域，查看当前工作空间下的项目空间数量信息。

### 创建Workspace

本文介绍如何创建Flink工作空间（Workspace）。

**前提条件**

已创建目标组织、目标资源集，为目标用户开放相应的权限。

**重要**

请先进行管理控制台授权，配置用户工作空间访问权限。用户应至少具备创建和查看实时计算Flink工作空间的权限。

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 在左侧导航栏，选择**Flink****（存算分离版）** **> Workspace** **管理**。
3. 在**Workspace** **列表**页面，单击**创建** **Workspace**。
4. 在**创建** **Flink Workspace**页面，填写配置信息。

| 参数 |  | 说明 |
|---|---|---|
| 区域 | 组织 | 选择目标组织，需要与已创建的用户身份处于同一组织。 |
|  | 资源集 | 选择目标资源集。 |
|  | 地域 | 选择地域。 |

实时计算（流计算）

| 基本信息 | 名称 | Flink Workspace的名称，可自定义。但需要满足以下要求： 允许小写字母、数字、- 或 . 且开头结尾为小写字母、数字。 在同一个地域内，名称不可重复。 |
|---|---|---|
|  | 处理器架构类型 | 根据界面提示按需选择。 |
|  | 用户名 | 默认显示当前登录的用户名。 |

5. 确认并提交配置信息。
如果服务管理中已创建云资源为**实时计算** **Flink**版的服务：确认以上配置参数无误后，单击**确认订单**。 如果服务管理中未创建云资源为**实时计算** **Flink**版的服务：确认以上配置参数无误后，单击**提交**。 关于服务管理的更多信息，请参见《**Apsara Uni-manager****运营控制台****用户指南》**中的**《服务管**
**理》**章节。
提交后，在**Workspace** **列表**页面可以看到新建的Workspace，待状态由**配置中**变为**可用**时，则说明创建成功了。如果需要删除已创建的Workspace，单击操作列的**删除**即可。

### 创建Namespace

本文介绍如何在实时计算Flink版管理控制台中创建和管理Namespace，包括权限配置、操作步骤和常见问题解决方案。

**前提条件**

已创建目标组织、目标资源集，为目标用户开放相应的权限。

**重要**

请先进行管理控制台授权，配置用户项目空间访问权限。用户应至少具备创建和查看实时计算Flink工作空间、项目空间的权限。

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 创建Namespace。
i. 在左侧导航栏，单击**Flink****（存算分离版）** **> Workspace****管理**。 实时计算（流计算） iii. （可选）选择服务目录。

**说明**

Flink（存算分离版）支持接入服务目录，实现运营管控。上架后可配置页面参数，并支持询价与流程审批。 创建服务目录后，您在创建Flink Namespace时可看到**计费方式**信息，当前仅支持**按量计** 费。 未创建服务目录的用户可忽略当前步骤。 a. 已创建服务目录，可在跳转到的页面中选择对应的服务目录。

**说明**

如果仅创建一个服务目录，将默认选择对应服务目录，自动进入**创建****Flink**
**Namespace****页面**。
b. 选择目标服务目录后，单击**开通服务**后可进入**创建****Flink Namespace**页面。 iv. 在**创建****Flink Namespace**页面，填写**区域**和**基本信息**。

**区域**

| 参数 | 说明 |
|---|---|
| 组织 | 选择目标组织，需要与已创建的用户身份处于同一组织。 |
| 资源集 | 选择目标资源集。 |
| 地域 | 选择地域。 |

实时计算（流计算）

**基本信息**

| 参数 | 说明 |
|---|---|
| Workspace | 您选择的Workspace，无法进行修改。 |
| Namespace名称 | Flink Namespace的名称，可自定义。但需要满足以下要求： 允许小写字母、数字、- 或 . 且开头结尾为小写字母、数字。 在同一个地域内，名称不可重复。 长度不超过40。 |
| CPU芯片类型 | 选择芯片类型。 |
| 部署模式 | 选择部署模式： 单可用区实例。 同城容灾实例。 |
| 可用区 | 选择可用区。 |
| CU信息 | 按需填写，但数量不能超过Workspace剩余的可分配的CU数量。 |
| 用户名 | 选择当前组织下有权限的用户名，指定该Namespace归属的用户。 |

3. 单击**提交**。
4. 创建成功后刷新，在对应的Workspace下可查看到新建的Namespace信息。

**相关操作**

跳转至实时计算开发控制台单击目标Namespace名称**操作**列下的**控制台**，即可跳转至实时计算开发控制台。 修改CU数量

**说明**

若已创建服务目录，在调整配额组的CU数量时，可实施运营管控。 单击目标Namespace名称**操作**列下的修改CU数量，可调整CU大小，并单击**确认订单**。

**重要**

减小CU大小可能导致Flink重启后无法恢复，请检查Namespace已使用的CU情况，谨慎操作。 单击目标Namespace名称**操作**列下的**配置外部存储****IP**，可添加IP地址或网段，IP地址为存储域名对应的实时计算（流计算） 删除Namespace 如果需要删除已创建的Namespace，单击**操作**列下的**删除**。 查询目标Namespace信息在**Workspace** **列表**下的搜索框中，可按关键词搜索目标Workspace，在Workspace列表中查看目标 Namespace信息。

**附录：创建服务目录**

1. 单击上方工具栏中的**运营** > **服务运营**。
2. 找到左侧导航栏中的**服务目录** > **服务管理**。
3. 单击**创建服务**，进入**创建服务**页面。
4. 在**创建服务**时，选择目标**产品**和关联资源。
5. 按界面提示配置其它参数（**服务名称**、**授权类型**等）。

**说明**

更多参数详细信息，可以参考阿里云专有云官网文档**统一云管平台****用户指南** > **运营中心** > **服务运** 营 > **服务目录**章节。
6. **提交**并完成服务目录创建后，您可基于该目录创建Namespace，并管理**修改****CU****数量**。

## 常见问题

问题描述：为什么我的账号已经授予了Namespace的访问权限，列表中却没有目标Namespace? 问题原因：针对该问题，可能存在两种情况： 您的账号没有加入到Namespace所属的资源集。 问题描述：为什么我的账号进入Flink Workspace 列表后，有些操作按钮没有显示，或者有显示但是有些按钮是灰色的？ 问题原因： 您的资源管理角色没有授权创建、删除工作空间或项目空间的权限，请联系管理员配置对应空间访问权实时计算（流计算） 您在**控制台**置灰的项目空间中没有被分配业务角色，无法访问实时计算开发控制台，请联系资源owner 问题描述：为什么我的账号在创建，修改，删除等操作提交后，报错没有权限修改项目空间？ 问题原因：如图所示，账号当前的角色没有被授权进行如上操作。请联系管理员配置项目空间访问权限， 实时计算（流计算）

## 快速入门

### Flink SQL作业快速入门

Flink支持通过SQL代码编辑和运行作业。本文带您快速体验Flink SQL作业的创建和上线运行等操作。

**操作流程**

1. 步骤一：创建SQL作业并编写业务代码
在**数据开发** **> ETL**页面，创建一个SQL类型的流作业，并编写DDL和DML代码。
2. 步骤二：启动作业，查看Flink计算结果
在作业运维页面，启动作业并查看作业运行状态。

**步骤一：创建SQL作业并编写业务代码**

1. 创建SQL作业。
ii. 在左侧导航栏单击**数据开发** **> ETL**，默认选择**作业草稿**页签。 iii. 单击后，单击**新建流作业**。 iv. 在**新建作业草稿**对话框中填写**文件名称**，选择**引擎版本**。 v. 单击**创建**。
2. 将以下作业代码拷贝到作业文本编辑区。
创建一个产生随机数据的datagen源表，将datagen源表中的name字段的数据插入blackhole结果表， 代码示例如下所示。 实时计算（流计算）

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

3. 单击**深度检查**，进行语法检查。
4. 深度检查通过后，单击**部署**。
5. 单击**确定**。

**步骤二：启动作业，查看Flink计算结果**

1. 在左侧导航栏单击**运维中心** > **作业运维**，展开**作业运维**页面。
2. 单击目标作业名称**操作**列中的**启动**。
3. 选择**无状态启动**，单击**启动**，详情请参见作业启动。
作业从当前状态变为**运行中**，则代表作业运行正常。
4. 查看Flink计算结果。
i. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。 ii. 在**作业日志** > **运行日志** > **运行****Task Managers**页签下，单击**Path, ID**。

**说明**

在**运行日志**页签，单击**作业**右侧的下拉框选择运行作业。默认选择正在运行作业。 实时计算（流计算） iii. 选择**日志**页签，查看Flink计算结果。

### Flink JAR作业快速入门

Flink支持JAR流作业和批作业的创建、部署与启动。本文带您快速体验Flink JAR作业的操作流程。

**操作流程**

步骤一：开发JAR包。 步骤二：上传测试JAR包和数据文件。 步骤三：部署JAR作业，并配置作业信息。 步骤四：启动作业后，查看Flink计算结果。

**步骤一：开发JAR包**

实时计算开发平台不提供JAR包的开发环境，您需要在本地完成开发、编译、打包。详情请参见JAR作业开发。

**步骤二：上传测试JAR包和数据文件**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**文件管理**。
3. 单击**上传资源**，上传要部署的JAR包和数据文件。
您可以直接下载测试文件以供后续步骤使用。 单击FlinkQuickStart-1.0-SNAPSHOT.jar，下载测试JAR包。 单击Shakespeare，下载输入数据文件Shakespeare。 实时计算（流计算）

**步骤三：部署JAR作业，并配置作业信息**

**流作业**

1. 在左侧导航栏单击**运维中心** > **作业运维**，展开**作业运维**页面。
2. 单击**部署作业**，选择**JAR****作业**。
3. 在**部署****JAR****作业**对话框，填写部署信息。

| 参数 | 说明 | 示例 |
|---|---|---|
| 部署模式 | 请选择部署为流模式。 | 流模式 |
| 部署名称 | 填写对应的JAR作业名称。 | flink-streaming-test-jar |
| 引擎版本 | 当前作业使用的Flink引擎版本。 建议使用带有推荐标签的版本，这些版本具有更高的可靠性和性能表现。 | vvr-11.5.0-flink-1.20 |
| JAR URI | 下拉框选择资源管理中的文件，或单击右侧图标选择文件，上传JAR包。 | - |
| Entry Point Class | 程序的入口类。如果您的JAR包未指定主类， 请在此处输入您的Entry Point Class类的标准路径。 说明因为本文提供的测试JAR包中既包含了流作业代码，又包含批作业代码。所以，此处需要指定为流作业的程序入口。 | org.example.WordCountStreaming |
| Entry Point Main Arguments | 填写输入数据文件的OSS路径。您可以在文件管理中查看并复制路径。 说明本文输入数据文件和测试JAR包存放路径一致。 | --input oss://flink-fullymanaged-< 工作空间 ID>/artifacts/namespaces/<项目空间名称>/Shakespeare |

更多配置参数详情请参见作业部署。
4. 单击**部署**。

**批作业**

1. 在左侧导航栏单击**运维中心** > **作业运维**，展开**作业运维**页面。
2. 单击**部署作业**，选择**JAR****作业**。
3. 在**部署****JAR****作业**对话框，填写部署信息。
实时计算（流计算）

| 参数 | 说明 | 示例 |
|---|---|---|
| 部署模式 | 请选择部署为批模式。 | 批模式 |
| 部署名称 | 填写对应的JAR作业名称。 说明作业名称在当前项目中必须保持唯一。 | flink-batch-test-jar |
| 引擎版本 | 当前作业使用的Flink引擎版本。 建议使用带有推荐标签的版本，这些版本具有更高的可靠性和性能表现。 | vvr-11.5.0-flink-1.20 |
| JAR URI | 下拉框选择资源管理中的文件，或单击右侧图标选择文件，上传JAR包。 | - |
| Entry Point Class | 程序的入口类。如果您的JAR包未指定主类，请在此处输入您的Entry Point Class类的标准路径。 说明因为本文提供的测试JAR包中既包含了流作业代码，又包含批作业代码。所以，此处需要指定为批作业的程序入口。 | org.example.WordCountBatch |
| Entry Point Main Arguments | 填写输入数据文件的OSS路径。您可以在文件管理中查看并复制路径。 说明本文输入数据文件、输出文件和测试JAR 包存放路径一致。 | --input oss://flink-fullymanaged- <工作空间 ID>/artifacts/namespaces/<项目空间名称>/Shakespeare --output oss://flink- fullymanaged-<工作空间 ID>/artifacts/namespaces/<项目空间名称>/batch-quickstart-test- output.txt |

更多配置参数详情请参见作业部署。
4. 单击**部署**。

**步骤四：启动作业后，查看Flink计算结果**

**流作业**

1. 部署成功后，系统默认跳转到该作业的**作业运维**页面。单击目标作业名称**操作**列中的**启动**。
2. 选择**无状态启动**，单击**启动**，详情请参见作业启动。
3. 作业状态变为**运行中**后，查看Flink计算结果。
i. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。 实时计算（流计算） ii. 在**作业日志** > **运行日志** > **运行****Task Managers**页签下，单击**Path, ID**。

**说明**

在**运行日志**页签，单击**作业**右侧的下拉框选择运行作业。默认选择正在运行作业。 iii. 单击**日志列表**，在**.out**尾缀的日志文件中，搜索shakespeare查看Flink计算结果。

**批作业**

1. 部署成功后，系统默认跳转到该作业的**作业运维**页面。单击目标作业名称**操作**列中的**启动**。
2. 在**作业启动**对话框中单击**启动**。
3. 作业状态变为**运行中**后，查看Flink计算结果。
i. 在左侧导航栏中，单击**文件管理**。 实时计算（流计算） ii. 单击batch-quickstart-test-output.txt文件**操作**列的**下载**，在本地进行查看。

### Flink Python作业快速入门

Flink支持部署与启动Python流作业和批作业。本文带您快速体验部署并启动Flink Python作业的操作流程。

**使用限制**

Flink存算分离版的ARM架构仅VVR 8.x及以上版本支持创建Python作业。

**操作流程**

步骤一：准备Python代码文件。 步骤二：上传测试Python文件和数据文件。 步骤三：部署Python作业，并配置作业信息。 步骤四：启动作业后，查看Flink计算结果。

**步骤一：准备Python代码文件**

实时计算开发平台不提供Python的开发环境，您需要在本地完成作业开发。详情请参见Python作业开发。

**步骤二：上传测试Python文件和数据文件**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**文件管理**。
3. 单击**上传资源**，上传要部署的Python文件和数据文件。
您可以直接下载测试文件以供后续步骤使用。 流模式测试Python文件：单击word_count_streaming.py下载。 批模式测试Python文件：单击word_count_batch.py下载。 输入数据文件Shakespeare：单击Shakespeare下载。 实时计算（流计算）

**步骤三：部署Python作业，并配置作业信息**

**流作业**

1. 在左侧导航栏单击**运维中心** > **作业运维**，展开**作业运维**页面。
2. 单击**部署作业**，选择**Python****作业**。
3. 在**部署****Python****作业**对话框，填写部署信息。

| 参数 | 说明 | 示例 |
|---|---|---|
| 部署模式 | 请选择部署为流模式。 | 流模式 |
| 部署名称 | 填写对应的Python作业名称。 | flink-streaming-test-python |
| 引擎版本 | 当前作业使用的Flink引擎版本。 建议使用带有推荐标签的版本，这些版本具有更高的可靠性和性能表现。 | vvr-11.5.0-flink-1.20 |
| Python文件地址 | 下拉框选择资源管理中的文件，或单击右侧图标选择文件，上传Python文件。 | - |
| Entry Module | 程序的入口类。 如果Python作业文件为.py文件，则该项不需要填写。 如果Python作业文件为.zip文件，则需要在此处输入您的Entry Module，例如 word count。 _ | 无需填写 |
| Entry Point Main Arguments | 填写输入数据文件的OSS路径。您可以在文件管理中查看并复制路径。 说明本示例中输入数据文件和测试Python文件存放路径一致。 | --input oss://flink-fullymanaged-< 工作空间 ID>/artifacts/namespaces/<项目空间名称>/Shakespeare |

更多配置参数详情请参见作业部署。
4. 单击**部署**。

**批作业**

1. 在左侧导航栏单击**运维中心** > **作业运维**，展开**作业运维**页面。
2. 单击**部署作业**，选择**Python****作业**。
3. 在**部署****Python****作业**对话框，填写部署信息。
4. 实时计算（流计算）

| 参数 | 说明 | 示例 |
|---|---|---|
| 部署模式 | 请选择部署为批模式。 | 批模式 |
| 部署名称 | 填写对应的Python作业名称。 | flink-batch-test-python |
| 引擎版本 | 当前作业使用的Flink引擎版本。 建议使用带有推荐标签的版本，这些版本具有更高的可靠性和性能表现。 | vvr-11.5.0-flink-1.20 |
| Python文件地址 | 下拉框选择资源管理中的文件，或单击右侧图标选择文件，上传Python文件。 | - |
| Entry Module | 程序的入口类。 如果Python作业文件为.py文件，则该项不需要填写。 如果Python作业文件为.zip文件，则需要在此处输入您的Entry Module，例如 word count。 _ | 无需填写 |
| Entry Point Main Arguments | 填写输入数据文件的OSS路径。您可以在文件管理中查看并复制路径。 说明本示例中输入数据文件、输出文件和测试Python文件存放路径一致。 | --input oss://flink-fullymanaged-< 工作空间 ID>/artifacts/namespaces/<项目空间名称>/Shakespeare --output oss://flink-fullymanaged-< 工作空间 ID>/artifacts/namespaces/<项目空间名称>/python-batch-quickstart- test-output |

更多配置参数详情请参见作业部署。
5. 单击**部署**。

**步骤四：启动作业后，查看Flink计算结果**

**流作业**

1. 部署成功后，系统默认跳转到该作业的**作业运维**页面。单击目标作业名称**操作**列中的**启动**。
2. 选择**无状态启动**，单击**启动**，详情请参见作业启动。
作业状态变为**运行中**或**已完成**，则代表作业运行正常。如果您部署本文档Python测试文件，作业最终运行状态是**已完成**状态。
3. 作业状态变为**运行中**后，查看Flink计算结果。

**重要**

如果您部署的是本文Python测试文件，流作业变为**已完成**状态时会删除作业结果，故流作业状态为**运行中**才能看到计算结果。 实时计算（流计算） i. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。 ii. 在**作业日志** > **运行日志** > **运行****Task Managers**页签下，单击**Path, ID**。

**说明**

在**运行日志**页签，单击**作业**右侧的下拉框选择运行作业。默认选择正在运行作业。 iii. 单击**日志列表**，在**.out**尾缀的日志文件中，搜索shakespeare查看Flink计算结果。

**批作业**

1. 部署成功后，系统默认跳转到该作业的**作业运维**页面。单击目标作业名称**操作**列中的**启动**。
2. 在**作业启动**对话框中单击**启动**。
3. 作业状态变为**已完成**后，查看Flink计算结果。
在左侧导航栏中，单击**文件管理**。 单击python-batch-quickstart-test-output/yyyy-MM-dd/prefix-****.ext文件**操作**列的**下载**，在本地进行查看。 实时计算（流计算） 实时计算（流计算）

## 数据开发

数据开发提供ETL和数据摄入能力。您可以在ETL中开发SQL、JAR和Python作业，也可以在数据摄入中使用YAML配置Flink CDC任务。

### Flink CDC数据摄入

#### MySQL数据同步写入Paimon

实时计算Flink版支持通过YAML作业配置Flink CDC任务，实现从源端同步到目标端的数据摄入工作。本文介绍如何构建一个Flink CDC数据摄入作业将MySQL库中的数据同步到Paimon中。

**背景信息**

基于Flink CDC开发YAML作业能有效实现将数据从源端同步到目标端的数据摄入工作。通过YAML配置的方式可以轻松定义复杂的ETL流程，并自动转化为Flink运算逻辑。相对于CDAS和CTAS，数据摄入还支持 ETL处理、Where条件过滤、列裁剪和计算列能力，极大地简化了数据集成过程，有效提升了数据集成的效率和可靠性。 实时计算Flink版支持通过YAML配置方式将MySQL数据源的数据同步至Paimon湖仓，可以按照以下步骤进行：
1. 步骤一：准备测试数据并配置白名单。
2. 步骤二：开发Flink CDC数据摄入作业。
3. 步骤三：启动Flink CDC数据摄入作业。
4. 步骤四：通过数据查询查看同步结果。

**前提条件**

上下游存储： 已创建RDS MySQL实例，详情请参见《云数据库RDS 用户指南（RDS MySQL）》中**快速入门** > 创
**建实例**。
已在OSS中创建Bucket和Paimon目录，详情请参见《对象存储用户指南》中**存储空间** > **创建存储空** 间以及**对象（文件）** > **新建目录**。

**步骤一：准备测试数据并配置白名单**

1. 创建账号和数据库。
为目标实例创建具有数据库读写权限的普通账号和数据库，详情请参见《云数据库RDS 用户指南（RDS MySQL）》中**快速入门** > **初始化设置**。
2. 通过DMS登录RDS数据库。
详情请参见《云数据库RDS 用户指南（RDS MySQL）》中**数据库连接** > **通过****DMS****登录****RDS****数据库**。
3. 创建源表并插入数据。
在已登录的SQL窗口输入如下命令生成测试RDS MySQL数据，单击**执行**。 实时计算（流计算）

```
CREATE TABLE flink_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10)
); INSERT INTO flink_user (name,age,gender) VALUES
  ('zhangsan',18,'M'),
  ('lisi',19,'F'),
  ('wangwu',20,'M');
```

4. 登录实时计算Flink版管理控制台。
5. 在**Workspace****列表**页面，单击目标NameSpace**操作**列下的**配置外部存储****IP**。
6. 单击**+IP****地址**，输入IP信息后单击**确认**。
i. 获取RDS MySQL实例对应的IP地址。

**说明**

可登录OPS机器执行 `ping` 命令查看Endpoint对应的IP地址。 ii. 将IP地址加入当前Flink工作空间的网络访问白名单中，详情请参见配置外部存储IP。
1. 登录实时计算开发控制台。
2. 在左侧导航栏选择**数据开发** > **数据摄入**。
3. 单击
后，单击**新建数据摄入草稿**。
4. 填写**文件名称**，选择**引擎版本**后，单击**创建**。
5. 输入YAML任务。
定义该任务为RDS MySQL的数据库中所有表作为源端，基于OSS的Paimon作为目标端，将源表同步至 `flink` 库。代码示例如下。 实时计算（流计算）

```bash
source:
  type: mysql
  # name: Database A to Data warehouse             #自行命名非必填
  hostname: rm-1b3r****.mysql.rds.intra.env35.shuguang.com
  port: 3306
  username: ${secret_values.mysqlusername}
  password: ${secret_values.mysqlpassword}
  tables: flink.\.*
  # scan.binlog.newly-added-table.enabled: true    # 支持动态增加表
sink:
  type: paimon
  name: Paimon Sink
  catalog.properties.metastore: filesystem
  catalog.properties.warehouse: oss://paimon-test/test/
  catalog.properties.fs.oss.endpoint: oss-cn-****.inter.env35.shuguang.com
  catalog.properties.fs.oss.region: cn-wulan-env35****
  catalog.properties.fs.oss.accessKeyId: ****
  catalog.properties.fs.oss.accessKeySecret: ****
  catalog.properties.fs.oss.signer.version: 1
```

1. 在**数据摄入**页面，单击**深度检查**。
2. 单击**部署**，在弹出的对话框中，单击**确定**。
3. 在**运维中心** > **作业运维**页面，单击目标YAML作业**操作**中的**启动**。
4. 选择启动状态，单击**无状态启动**或**有状态启动**，单击**启动**。
5. 等待作业状态为运行中后，查看OSS对应Bucket的目录下后缀为 `.db` 的目录和表目录。

**步骤四：通过数据查询查看同步结果**

1. 在左侧导航栏单击**数据开发** **> ETL**，默认选择**作业草稿**页签。
2. 单击
后，单击**新建流作业**。
3. 输入SQL语句读取Paimon数据查看同步结果。示例代码如下。
实时计算（流计算）

```
CREATE CATALOG paimon_catalog WITH (
  'type' = 'paimon',
  'metastore' = 'filesystem',
  'warehouse' = 'oss://paimon-test/test/',
  'fs.oss.endpoint' = 'oss-cn-wulan-env35-****.inter.env35.shuguang.com',
  'fs.oss.accessKeyId' = '****',
  'fs.oss.accessKeySecret' = '****',
  'fs.oss.signer.version' = '1'
); USE CATALOG paimon_catalog; SELECT * FROM flink.flink_user;
```

4. 单击页面右上角**运行**，输出结果如下所示。

### 作业开发

ETL提供SQL、JAR和Python作业的开发与调试能力，并支持通过模板中心快速创建作业。

#### 模板中心

##### 数据同步模板

Flink CDC支持数据的实时同步和表结构变更的自动同步。您可以使用数据同步模板帮您快速生成数据同步的Flink SQL作业代码。本文为您介绍如何使用多库多表同步或者分库分表合并模板实现数据同步。

**背景信息**

实时计算Flink版支持多库多表同步和分库分表合并两种数据同步方式，二者的区别请参见下表。

| 同步方式 | 详情 |
|---|---|
| 多库多表同步 | 如果您需要将一个或多个数据库中的一张或多张业务数据表实时复制到另一个数据库时，则可以使用多库多表同步模板。Flink CDC可以自动同步整库的全量和增量数据，同时还能实时将每张源表的表结构变更（加列等）实时同步到对应的目标表中。多库多表同步模板会将您的参数翻译成CDAS语句。 |
| 分库分表合并 | 当同一份业务数据分散在不同的数据库或者业务表时，我们往往需要用到分库分表合并的能力， 将表结构相似的分库分表的数据同步到一张目标表中。Flink CDC可以自动同步源中所有分库分表的全量和增量数据（包括新增的符合正则表达式的新表），同时还能实时将每张源表的表结构变更（加列等）实时同步到对应的目标表中。分库分表合并同步模板会将您的参数翻译成CTAS 语句。 |

**使用限制**

实时计算（流计算） 目前仅支持从MySQL到Hologres的数据同步。

**注意事项**

在同步MySQL到Hologres的数据时，会同步表结构变更，同步时需要注意以下几点： 无需您手动在Hologres上创建表。 Flink会自动在Hologres上创建表，但如果Hologres已经存在对应的表，Flink会根据您创建计划中选择的目标库和表信息来映射。 Hologres不支持更改列的类型。 如果当前字段的类型和Hologres下游表中对应的字段类型不同，则会写入失败，您需重修改列类型并重新同步。

**操作步骤**

**配置MySQL和Hologres存储IP**

1. 登录MySQL和Hologres实例，获取实例域名信息。
2. 登录OPS机器，执行 `ping` 命令获取MySQL和Hologres域名对应的IP。
3. 配置MySQL和Hologres存储IP，请参见配置外部存储IP。

**创建MySQL Catalog、Hologres Catalog**

1. 登录实时计算开发控制台。
2. 在左侧导航栏单击**数据管理**，展开**Catalog****列表**页面，单击**创建****Catalog**。
3. 在**创建****Catalog**对话框中选择**MySQL**，点击**下一步**配置Catalog信息。
实时计算（流计算）

| 参数 | 说明 |
|---|---|
| catalog name | 自定义catalog名称。 |
| hostname | MySQL数据库服务器的IP地址或主机名。 |
| port | 连接到服务器的端口，默认是3306。 |
| default-database | 默认数据库名称。 |
| username | 连接MySQL数据库服务器时使用的用户名。 |
| password | 连接MySQL数据库服务器时使用的密码。 |

4. 同上步骤，选择**Hologres**，点击**下一步**配置Catalog信息。

| 参数 | 说明 |
|---|---|
| catalog name | 自定义catalog名称。 |
| endpoint | Hologres的连接地址，<host>:<port>。 |

实时计算（流计算）

| username | 与dbname相匹配的用户名，为Hologres所在组织的 AccessKey ID。 |
|---|---|
| password | 与dbname相匹配的密码，为Hologres所在组织的 AccessKey Secret。 |
| dbname | 您访问Hologres的默认数据库名称。 |

**数据同步**

1. 在左侧导航栏单击**数据开发** **> ETL**，默认选择**作业草稿**页签。
2. 单击
，选择**从模板新建**。
3. 在**数据同步模板**页签单击**MySQL**到**Hologres****数据同步**模板名称，单击**下一步**。
4. 配置数据同步信息。
实时计算（流计算） i. 配置源和目标，填写**MySQL****配置项**，单击**下一步**。

| 类别 | 配置项 | 详情 |
|---|---|---|
| 源 | MySQL Catalog | 您可以直接选择已创建好的MySQL Catalog。如果您没有提前创建源MySQL Catalog，则请单击创建Catalog进行创建。 |
|  | MySQL server-id | 每个MySQL数据库客户端的唯一ID。取值范围为 5400~6400。该参数也支持ID范围的格式，例如5400- 5408。推荐在开启增量读取模式多并发读取数据时，设置该参数为ID范围，因为这样可以使得每个并发使用不同的ID。 重要不要和其他访问数据库的作业或者服务使用同一个 Server ID。 |
| 目标 | Hologres Catalog | 您可以直接选择已创建好的目标Hologres Catalog。如果您没有提前创建好目标Hologres Catalog，则请单击创建 Catalog进行创建。 |

ii. 创建计划。 实时计算（流计算） 多库多表同步 a. 在**多库多表同步**页签下，选中目标的源库和表名称。 b. 单击**保存计划**，单击**下一步**。 c. 查看系统根据您选择的目标库和表生成对应的SQL代码，单击**确认**。 您可以根据需要修改**文件名称**、**存储位置**或**引擎版本**等信息。 分库分表合并 a. 在**分库分表合并**页签下，选中目标的源库和表名称，或者直接输入您创建的目标库和表名称。

**说明**

推荐您使用正则表达式填写源库和源表信息。 b. 单击**保存计划**，单击**下一步**。 在一个作业中，可以同时创建多个多库多表同步和分库分表合并的计划。 c. 查看系统根据您选择的目标库和表生成对应的SQL代码，单击**确认**。 您可以根据需要修改**文件名称**、**存储位置**或**引擎版本**等信息。
5. 单击**创建**。
实时计算（流计算） 作业创建后，就会进入SQL作业开发页面。后面的操作和正常的作业开发完全相同，参数配置详情和后续

##### 代码模板

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

实时计算（流计算）

|  |  | 累积窗口聚合 | 如果您需要提早看到窗口的计算结果，例如每分钟看到最新的窗口结果，则可以使用累积窗口。 说明累积窗口聚合不支持CDC，使用CDC后语法校验会报错 org.apache.flink.table.api.TableException: Not |  |  |  |
|---|---|---|---|---|---|---|
|  | 聚合分析 |  |  |  |  |  |
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
1. 登录实时计算开发控制台。
实时计算（流计算）
2. 在左侧导航栏单击**数据开发** **> ETL**，默认选择**作业草稿**页签。
3. 单击
，选择**从模板新建**。
4. 在**SQL****基础模板**页签单击**创建表**模板名称，单击**下一步**。
5. 根据需要，修改**文件名称**、**存储位置**等。
6. 单击**创建**。
单击**创建**后，就会进入SQL开发页面。后面的操作和正常的作业开发完全相同，参数配置详情和后续操作

#### SQL作业开发

本文介绍Flink SQL流作业开发的操作步骤，包括创建作业和编辑代码、检查语义、调试及部署。

**操作步骤**

实时计算（流计算）

**操作步骤**

1. 新建SQL流作业。
ii. 在左侧导航栏单击**数据开发** **> ETL**，默认选择**作业草稿**页签。 iii. 单击后，单击**新建流作业**。 iv. 在**新建作业草稿**对话框中填写**文件名称**，选择**引擎版本**。 v. 单击**创建**。
2. 编写DDL和DML代码。

**说明**

依托于元数据管理能力，您能够在不同的作业中重复利用创建的表结构。在使用Flink开发控制台编辑SQL作业时，只需要输入部分字符，系统即可自动补全字段和表名称。 代码示例如下。 `--`创建源表`datagen_source`。

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

3. 在**ETL**页面右侧页签，查看或者填写配置信息。

| 页签名称 | 配置说明 |
|---|---|

实时计算（流计算）

| 更多配置 | 引擎版本：建议您使用推荐版本或稳定版本，引擎版本标记含义详情如下： 推荐版本（Recommend）：当前最新大版本下的最新小版本。 EOS版本（Eos）：超过产品服务期限的版本。 附加依赖文件：作业中需要使用到的附加依赖，例如临时函数等。 Kerberos 认证：你可以开启Kerberos认证开关，当开启Kerberos认证时，还需配置Kerberos 集群和Principal参数。 |
|---|---|
| 代码结构 | 数据流向图：您可以通过数据流向图快速查看出数据的流向。 树状结构图：您可以通过树状结构图快速查看出数据的来源。 |
| 版本信息 | 您可以在此处查看作业版本信息。 |

4. 单击**深度检查**。
检查作业的SQL语义和作业使用的表的元数据信息。
5. **可选：**单击**调试**。
您可以使用作业调试功能模拟作业运行、检查输出结果，验证SELECT或INSERT业务逻辑的正确性，提升开发效率，降低数据质量风险。详情请参见作业调试。
6. 单击**部署**。
完成作业开发和深度检查后，即可部署作业，将数据发布至生产环境。
7. 在**部署新版本**中，填写备注信息，按需选择是否**提交到****Session****集群**后，单击**确定**。

#### JAR作业开发

Flink JAR提供了更灵活的编程模型和API，可以自定义各种数据转换、操作和算子，适用于复杂的业务逻辑和数据处理需求。本文为您介绍Flink JAR作业的开发方法和调试方法。

**使用限制**

受部署环境、网络环境等因素的影响，开发DataStream作业，需要注意以下限制： 仅支持JAR形式的作业提交和运行，支持一个主JAR包和多个附加依赖JAR包。 不支持在Main函数中读取本地配置。 x86的工作空间仅支持JDK 8，ARM的工作空间支持JDK 8和JDK 11版本。 支持开源Scala V2.12版本。

**注意事项**

Flink产品开发界面上配置的参数优先级均低于作业代码中的优先级。为了保证作业的正常运行，建议优先在开发界面配置Checkpoint相关参数，请勿在作业代码中配置Checkpoint相关参数。 如果Datastream作业访问的上下游存储提供了白名单机制，则您需要进行白名单配置。 为了避免JAR包依赖冲突，您需要注意以下几点： 作业开发页面选择的Flink版本，请在Pom文件中使用相同版本的Apache Flink依赖库。 实时计算（流计算） Flink相关依赖，scope请使用provided，即在依赖中添加 `<scope>provided</scope>` 。Flink相关依赖主要包括 `org.apache.flink` 组下以 `flink-` 开头的，非Connector的依赖。例如flinkstreaming-java、flink-streaming-java_2.11和flink-java，flink-runtime等。

**说明**

建议您在作业开发时先进行依赖配置，以避免Flink依赖冲突问题。 其他第三方依赖请采用Shade方式打包，Shade打包详情请参见Apache Maven Shade Plugin。 Flink源代码中只有明确标注了@Public或者@PublicEvolving的才是公开供用户调用的方法，阿里云实时计算Flink版只对这些方法的兼容性做出产品保证。 如果是Flink服务内置的Connector支持的DataStream API，建议使用其内置的依赖。

### 作业开发

**说明**

JAR作业需要您在线下完成开发，再在Flink开发控制台上部署并运行。

**开发参考**

Apache Flink简介，以及它的体系架构、应用程序和特性功能等，请参见Apache Flink介绍。 Apache Flink V1.17业务代码开发，请参见Flink DataStream API开发指南和Flink Table API & SQL 开发指南。 Apache Flink的编码、Java语言、Scala语言、组件和格式等指南，请参见代码风格和质量指南。 Apache Flink作业的源代码项目配置，请参见Project Configuration和Datastream开发打包问题。 Flink DataStream Connector依赖，请参见Connector依赖。 Apache Flink编码过程中遇到的问题及解决方法，请参见常见问题。

**业务代码编写**

1. 将外部数据源集成到Flink数据流程序。
`Watermark` 是Flink一种基于时间语义的计算策略，往往伴随着时间戳一起使用，所以本示例不使用水印策略。详情请参考水印策略。 `//` 将外部数据源集成到`flink`数据流程序 `// WatermarkStrategy.noWatermarks()` 指没有使用水印策略

```
        DataStreamSource<String> stream = env.fromSource(kafkaSource,
WatermarkStrategy.noWatermarks(), "kafka Source");
```

2. 算子转换处理。
示例中将 `DataStream<String>` 转换成 `DataStream<Student>` ，更多复杂的算子转化和处理方式请参考Flink算子。 实时计算（流计算） `//` 转换数据结构为`student`的算子

```java
          DataStream<student> source = stream
                .map(new MapFunction<String, student>() {
                    @Override
                    public student map(String s) throws Exception {
```

`//` 数据由逗号分隔

```
                        String[] data = s.split(",");
                        return new student(Integer.parseInt(data[0]), data[1], Integer
.parseInt(data[2]));
                    }
```

}).filter(student -> student.score >=60); // 筛选出分数大于`60`分的数据

**作业打包**

通过maven-shade-plugin插件打包。

**重要**

如果选择作为附加依赖文件引入使用连接器，打包作业时，确认连接器相关依赖的作用域为 `provided` 。 如果选择连接器作为依赖一起打包，作用域默认（compile）即可。 maven-shade-plugin插件依赖参考

```xml
<build>
        <plugins>
```

<!-- Java 编译器`-->`

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>${target.java.version}</source>
                    <target>${target.java.version}</target>
                </configuration>
            </plugin>
```

<!-- 我们使用`maven-shade-plugin`创建一个包含所有必须依赖的`fat jar -->` <!-- 修改`<mainClass>`的值.如果您的程序入口点发生了改变 `-->`

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
```

<!-- 去掉一些不必要的依赖性 `-->`

```xml
                        <configuration>
                            <artifactSet>
                                <excludes>
                                    <exclude>org.apache.flink:force-shading</exclude>
```

实时计算（流计算）

```xml
                                    <exclude>com.google.code.findbugs:jsr305</exclude>
                                    <exclude>org.slf4j:*</exclude>
                                    <exclude>org.apache.logging.log4j:*</exclude>
                                </excludes>
                            </artifactSet>
                            <filters>
                                <filter>
```

<!-- 不要复制`META-INF`文件夹中的签名。否则，这可能会在使用`JAR` 文件时导致安全异常 `-->`

```xml
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                            <transformers>
                                <transformer
implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.aliyun.FlinkDemo</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
```

**作业测试及部署**

由于实时计算Flink版默认不具备访问公网的能力，您的代码可能无法在本地进行直接测试。建议您分开进行单元测试。 JAR作业部署请参见作业部署。

**说明**

部署时，如果选择方式一使用连接器打包的作业，切记需要上传添加连接器相关的JAR包。 如果需要读取配置文件，也需要在附加依赖文件中上传添加。

**完整示例代码**

本示例代码中，将Kafka数据源的数据进行处理后写入MySQL。此示例仅供参考，更多的代码风格和质量指南请参见代码风格和质量指南。

**说明**

示例中未包含CheckPoint、TTL、重启策略等运行参数的配置。上述配置可在部署作业完成后，通过部
**署详情**页进行自定义配置。鉴于代码中设置配置项的优先级较高，建议在部署作业后进行自定义配置，
以便于后续的修改和应用。 实时计算（流计算）

**FlinkDemo.java**

```java
package com.aliyun; import org.apache.flink.api.common.eventtime.WatermarkStrategy; import org.apache.flink.api.common.functions.MapFunction; import org.apache.flink.connector.jdbc.JdbcConnectionOptions; import org.apache.flink.connector.jdbc.JdbcExecutionOptions; import org.apache.flink.connector.jdbc.JdbcSink; import org.apache.flink.connector.jdbc.JdbcStatementBuilder; import org.apache.flink.connector.kafka.source.KafkaSource; import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer; import org.apache.flink.connector.kafka.source.reader.deserializer.KafkaRecordDeserializationSch a; import org.apache.flink.kafka.shaded.org.apache.kafka.common.serialization.StringDeserializer; import org.apache.flink.streaming.api.datastream.DataStream; import org.apache.flink.streaming.api.datastream.DataStreamSource; import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment; import java.io.FileInputStream; import java.io.IOException; import java.io.InputStream; import java.sql.PreparedStatement; import java.sql.SQLException; import java.util.HashMap; import java.util.Map; import java.util.Properties; public class FlinkDemo {
```

`//` 定义数据结构

```
    public static class Student {
        public int id;
        public String name;
        public int score;
        public Student(int id, String name, int score) {
            this.id = id;
            this.name = name;
            this.score = score;
        }
    }
    public static void main(String[] args) throws Exception {
```

`//` 创建`Flink`执行环境

```
        final StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment();
        Properties properties = new Properties();
        Map<String,String> configMap = new HashMap<>();
        try (InputStream input = new
FileInputStream("/flink/usrlib/config.properties")) {
```

加载属性文件实时计算（流计算） `//` 加载属性文件

```
            properties.load(input);
```

`//` 获取属性值

```
configMap.put("bootstrapServers",properties.getProperty("bootstrapServers")) ;
            configMap.put("inputTopic",properties.getProperty("inputTopic"));
            configMap.put("groupId",properties.getProperty("groupId"));
            configMap.put("url",properties.getProperty("database.url")) ;
            configMap.put("username",properties.getProperty("database.username"));
            configMap.put("password",properties.getProperty("database.password"));
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        // Build Kafka source
        KafkaSource<String> kafkaSource = KafkaSource.<String>builder()
                        .setBootstrapServers(configMap.get("bootstrapServers"))
                        .setTopics(configMap.get("inputTopic"))
                        .setStartingOffsets(OffsetsInitializer.latest())
                        .setGroupId(configMap.get("groupId"))
.setDeserializer(KafkaRecordDeserializationSchema.valueOnly(StringDeserializer.class))
                        .build();
```

`//` 将外部数据源集成到`flink`数据流程序 `// WatermarkStrategy.noWatermarks()` 指没有使用水印策略

```
        DataStreamSource<String> stream = env.fromSource(kafkaSource,
WatermarkStrategy.noWatermarks(), "kafka Source");
```

`//` 筛选出分数大于`60`分的数据

```java
        DataStream<Student> source = stream
                .map(new MapFunction<String, Student>() {
                    @Override
                    public Student map(String s) throws Exception {
                        String[] data = s.split(",");
                        return new Student(Integer.parseInt(data[0]), data[1], Integer.p
arseInt(data[2]));
                    }
                }).filter(Student -> Student.score >=60);
        source.addSink(JdbcSink.sink("INSERT IGNORE INTO student (id, username, score)
VALUES (?, ?, ?)",
                new JdbcStatementBuilder<Student>() {
                    public void accept(PreparedStatement ps, Student data) {
                        try {
                            ps.setInt(1, data.id);
                            ps.setString(2, data.name);
                            ps.setInt(3, data.score);
                        } catch (SQLException e) {
                            throw new RuntimeException(e);
                        }
                    }
                },
                new JdbcExecutionOptions.Builder()
```

`(5)``//`每次批量写入的记录数

```
ithBthSi
```

实时计算（流计算） `.withBatchSize(5) //` 每次批量写入的记录数 `.withBatchIntervalMs(2000) //` 重试时的最大延迟时间（毫秒）

```
                        .build(),
                new JdbcConnectionOptions.JdbcConnectionOptionsBuilder()
                        .withUrl(configMap.get("url"))
                        .withDriverName("com.mysql.cj.jdbc.Driver")
                        .withUsername(configMap.get("username"))
                        .withPassword(configMap.get("password"))
                        .build()
        )).name("Sink MySQL");
        env.execute("Flink Demo");
    }
}
```

**pom.xml**

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v
4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.aliyun</groupId>
    <artifactId>FlinkDemo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <name>FlinkDemo</name>
    <packaging>jar</packaging>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <flink.version>1.17.1</flink.version>
        <vvr.version>1.17-vvr-8.0.4-1</vvr.version>
        <target.java.version>1.8</target.java.version>
        <maven.compiler.source>${target.java.version}</maven.compiler.source>
        <maven.compiler.target>${target.java.version}</maven.compiler.target>
        <log4j.version>2.14.1</log4j.version>
    </properties>
    <dependencies>
        <!-- Apache Flink 依赖项 -->
```

<!-- 之所以提供这些依赖项，是因为它们不应该打包到`JAR`文件中。 `-->`

```xml
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-java</artifactId>
            <version>${flink.version}</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java</artifactId>
            <version>${flink.version}</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
```

实时计算（流计算）

```xml
            <artifactId>flink-clients</artifactId>
            <version>${flink.version}</version>
            <scope>provided</scope>
        </dependency>
```

<!-- 在这里添加连接器依赖项。它们必须在默认作用域`(compile)`中。 `-->`

```xml
        <dependency>
            <groupId>com.alibaba.ververica</groupId>
            <artifactId>ververica-connector-kafka</artifactId>
            <version>${vvr.version}</version>
        </dependency>
        <dependency>
            <groupId>com.alibaba.ververica</groupId>
            <artifactId>ververica-connector-mysql</artifactId>
            <version>${vvr.version}</version>
        </dependency>
```

<!-- 添加日志框架，以便在运行时生成控制台输出 `-->` <!-- 默认情况下，这些依赖项从应用程序`JAR`中排除 `-->`

```xml
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-slf4j-impl</artifactId>
            <version>${log4j.version}</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
            <version>${log4j.version}</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>${log4j.version}</version>
            <scope>runtime</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
```

<!-- Java 编译器`-->`

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>${target.java.version}</source>
                    <target>${target.java.version}</target>
                </configuration>
            </plugin>
```

<!-- 我们使用`maven-shade-plugin`创建一个包含所有必须依赖的 `fat jar -->` 实时计算（流计算） <!-- 修改`<mainClass>`的值.如果您的程序入口点发生了改变 `-->`

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
```

<!-- 去掉一些不必要的依赖性 `-->`

```xml
                        <configuration>
                            <artifactSet>
                                <excludes>
                                    <exclude>org.apache.flink:force-shading</exclude>
                                    <exclude>com.google.code.findbugs:jsr305</exclude>
                                    <exclude>org.slf4j:*</exclude>
                                    <exclude>org.apache.logging.log4j:*</exclude>
                                </excludes>
                            </artifactSet>
                            <filters>
                                <filter>
```

<!-- 不要复制`META-INF`文件夹中的签名。否则，这可能会在使用`JAR` 文件时导致安全异常 `-->`

```xml
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                            <transformers>
                                <transformer
implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.aliyun.FlinkDemo</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Python作业开发

本文为您介绍Flink Python API作业开发的背景信息、使用限制、开发方法、调试方法和连接器使用等。 实时计算（流计算）

**背景信息**

Flink Python作业需要您在本地完成开发工作，Python作业开发完成后，再在Flink开发控制台上部署并启 Flink工作空间已安装下列软件包。

| 软件包 | 版本 |
|---|---|
| apache-beam | 2.23.0 |
| avro-python3 | 1.9.1 |
| certifi | 2020.12.5 |
| cloudpickle | 1.2.2 |
| crcmod | 1.7 |
| cython | 0.29.16 |
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

实时计算（流计算）

| numpy | 1.19.5 |
|---|---|
| oauth2client | 3.0.0 |
| pandas | 0.25.3 |
| pbr | 5.5.1 |
| pip | 20.1.1 |
| protobuf | 3.15.3 |
| py4j | 0.10.8.1 |
| pyarrow | 0.17.1 |
| pyasn1-modules | 0.2.8 |
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

实时计算（流计算）

| typing-extensions | 3.7.4.3 |
|---|---|
| urllib3 | 1.26.3 |
| wheel | 0.36.2 |

**使用限制**

由于Flink受部署环境、网络环境等因素的影响，所以开发Python作业，需要注意以下限制： Arm环境VVR 8.0.7以上支持Python作业。 Flink工作空间已预装了Python 3.7.9，且Python环境中已预装了Pandas、NumPy、PyArrow等常用的Python库。因此需要您在Python 3.7版本开发代码。 x86的工作空间仅支持JDK 8，arm的工作空间支持JDK 8和JDK 11版本。 仅支持开源Scala V2.11版本，如果Python作业中依赖第三方JAR包，请确保使用Scala V2.11对应的 JAR包依赖。

### 作业开发

您可以参见以下文档在本地完成Flink业务代码开发： Apache Flink V1.17业务代码开发，请参见Flink Python API开发指南。 Apache Flink编码过程中遇到的问题及解决方法，请参见常见问题。

#### 作业调试

您可以在Python自定义函数的代码实现中，通过logging的方式，输出日志信息，方便后期问题定位，示例如下。

```python
@udf(result_type=DataTypes.BIGINT()) def add(i, j):
  logging.info("hello world")
  return i + j
```

日志输出后，您可以在TaskManager的日志文件中查看。 您可以在Flink Python作业中使用自定义的Python虚拟环境、第三方Python包、JAR包和数据文件等，详

##### 使用Python依赖

您可以在Flink Python作业中使用自定义的Python虚拟环境、第三方Python包、JAR包和数据文件等，本文为您介绍如何在Python作业中使用这些依赖。

**背景信息**

使用自定义的Python虚拟环境使用第三方Python包使用JAR包实时计算（流计算） 使用数据文件

**使用自定义的Python虚拟环境**

当前仅支持Python 3.7的Python虚拟环境，下文为您介绍如何准备Python 3.7的虚拟环境。
1. 准备Python 3.7的虚拟环境。
i. 在本地准备**build.sh**脚本，其内容如下。

```bash
#!/bin/bash
set -e -x yum install -y zip wget cd /root/ bash /build/setup-pyflink-virtual-env.sh mv venv.zip /build/
```

ii. 在本地准备**setup-pyflink-virtual-env.sh**脚本，其内容如下。

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
2. 在Python作业中使用**Python 3.7**虚拟环境。
实时计算（流计算） ii. 在左侧导航栏，单击**文件管理**，上传**venv.zip**文件。

**说明**

实时计算Flink开发控制台上可以上传文件大小的限制为200 MB，而Python虚拟环境的大小通常会超过该限制，因此，您需要通过OSS管理控制台上传文件。详情请参见**《对象存储****用户指南》**
> **对象（文件）** > **上传文件**。
iii. 在**运维中心** > **作业运维**页面单击**部署作业**，在配置项**Python Archives**中选择**venv.zip**文件。 iv. 单击右侧的**高级配置**，在**更多****Flink****配置**项，添加配置信息。

```
python.executable: venv.zip/venv/bin/python
```

v. 单击**保存**。

**使用第三方Python包**

下面将从以下两个场景为您介绍如何使用第三方Python包： 使用可直接Import的第三方Python包如果您的第三方Python包是Zip Safe的，即不需要安装即可直接在Python作业中使用。操作步骤如下： i. 下载可直接Import的第三方Python包。 a. 在浏览器上打开PyPI页面。 b. 在搜索框中输入目标第三方Python包名称，例如**apache-flink 1.12.2**。 c. 在搜索结果中，单击目标结果名称。 d. 在左侧导航栏，单击Download files。 e. 单击文件名中包含**cp37-cp37m-manylinux1**的包名称进行下载。 iii. 在左侧导航栏，单击**文件管理**，上传第三方Python包。 iv. 在**运维中心** > **作业运维**页面单击**部署作业**，在配置项**Python Libraries**中选择所上传的第三方 Python包。 v. 单击**保存**。 使用需要编译的第三方Python包如果您的第三方Python包是**tar.gz**格式的压缩包，或从其他地方下载的源码包，且压缩包的根目录下存在**setup.py**文件，则这种类型的第三方Python包通常需要先编译才能被使用。您需要先在与Flink兼容的环境下编译第三方Python包，然后才可在Python作业中调用第三方Python包。 推荐使用**quay.io/pypa/manylinux2014_x86_64**镜像容器中的**Python 3.7**来编译第三方Python 包，使用该容器编译生成的包兼容绝大多数Linux环境，关于该镜像容器的更多信息请参见manylinux。

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

该命令执行完后，会生成一个名字为**deps.zip**的文件，该文件为编译之后的第三方Python包。 您也可以修改**requirements.txt**，安装其他所需的第三方Python包。此外，**requirements.txt**文件中可以指定多个Python依赖。 ii. 在Python作业中使用第三方Python包**deps.zip**。 b. 在左侧导航栏，单击**文件管理**，上传**deps.zip**。

**说明**

实时计算Flink产品限制可上传的最大文件大小为200 MB，而Python虚拟环境的大小通常会超过该限制，需要通过OSS管理控制台进行文件上传。详情请参见**《对象存储****用户指南》** > **对象**
**（文件）** > **上传文件**。
c. 在**运维中心** > **作业运维**页面单击**部署作业**，在配置项**Python Libraries**中选择**deps.zip**。 d. 单击**保存**。

**使用JAR包**

如果您的Flink Python作业中使用了Java类，例如作业中使用了Connector或者Java自定义函数时，可以通过如下方式来指定Connector或者Java自定义函数的JAR包。
1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**文件管理**，上传需要使用的JAR包。
3. 在**运维中心** > **作业运维**页面单击**部署作业**，在配置项**附加依赖文件**中选择需要使用的JAR包。
4. 单击已部署的作业名称，在**部署详情**页签**运行参数配置**区域，单击**编辑**，在**其他配置**中，添加相关配置。
假如需要依赖多个JAR包，且名字分别为**jar1.jar**和**jar2.jar**，配置内容如下。

```
pipeline.classpaths: 'file:///flink/usrlib/jar1.jar;file:///flink/usrlib/jar2.jar'
```

5. 单击**保存**。

**使用连接器**

实时计算（流计算）
1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**文件管理**。
3. 单击**上传资源**，选择您要上传的目标连接器的Python包。
您可以上传您自己开发的连接器，也可以上传Flink提供的连接器。Flink提供的连接器官方Python包的下载地址，请参见Connector列表。
4. 在**作业运维**页面，单击**部署作业**，**附加依赖文件**项选择目标连接器的Python包。
5. 单击已部署的作业名称，在**部署详情**页签**运行参数配置**区域，单击**编辑**，在**其他配置**中，添加相关配置。
如果您的作业需要依赖多个连接器Python包，例如依赖的2个包的名字分别为connector-1.jar和 connector-2.jar，则配置信息如下。

```
pipeline.classpaths: 'file:///flink/usrlib/connector- 1.jar;file:///flink/usrlib/connector-2.jar'
```

**使用数据文件**

下面将从两个场景为您介绍如何使用数据文件： 通过Python Archives选项方式如果您的数据文件的数量比较多时，您可以将数据文件打包成一个ZIP包，然后通过如下方式在Python作业中使用。操作步骤如下： ii. 在左侧导航栏，单击**文件管理**，上传需要数据文件ZIP包。 iii. 在目标作业开发页面的**Python Archives**项，选择需要使用的数据文件ZIP包。 iv. 在Python自定义函数中，可以通过如下方式访问数据文件。假如数据文件所在压缩包名称为**mydata.zip**。

```python
def map():
    with open("mydata.zip/mydata/data.txt") as f:
    ...
```

通过附加依赖文件选项如果您的数据文件数量比较少时，可以通过如下方式在Python作业中使用。操作步骤如下： ii. 在左侧导航栏，单击**文件管理**，上传需要的数据文件ZIP包。 iii. 在目标作业开发页面的**附加依赖文件**项，选择需要的数据文件。 iv. 在Python自定义函数中，可以通过如下方式访问数据文件。假如数据文件名称为**data.txt**。

```python
def map():
    with open("/flink/usrlib/data.txt") as f:
    ...
```

#### 作业调试

您可以使用作业调试功能模拟作业运行、检查输出结果，验证SELECT或INSERT业务逻辑的正确性，提升开发效率，降低数据质量风险。本文介绍作业调试操作方法。

**使用限制**

仅SQL作业支持单击调试进行作业调试。 Flink默认读取最多1000条数据后会自动暂停。 实时计算（流计算） Session集群不支持显示数据曲线、监控告警功能和开启自动调优功能。

**操作步骤**

1. 编写SQL作业代码。详情请参见SQL作业开发。
2. 登录实时计算开发控制台。
3. 在**数据开发** **> ETL**页面，单击**调试**。
4. **选择调试集群**后，单击**下一步**。
如果没有已创建的Session集群，您可以创建并启动一个，操作详情请参见配置Session集群。
5. 配置调试数据。
如果您使用线上数据，直接单击**确认**即可。 如果您需要使用调试数据，需要先单击**下载调试数据模板**后，填写调试数据后，上传调试数据。 其中该页面涉及的功能解释如下。

| 配置项 | 说明 |
|---|---|
| 下载调试数据模板 | 为了便于编辑，您可以直接下载调试数据模板，模板已适配源表的数据结构。 |
| 上传调试数据 | 如果您需要使用本地调试数据进行调试，您可以先下载调试数据模板，本地编辑好数据后上传，并选中使用调试数据。 调试数据文件存在以下限制： 上传文件仅支持CSV格式。 CSV格式的文件必须含有表头，例如 id(INT)。 调试数据CSV文件最大支持1 MB或1千条记录。 |
| 数据预览 | 上传好调试数据后，单击源表名称左侧的图标，可以预览数据和下载调试数据。 |
| 调试代码预览 | 调试功能会自动改变源表和结果表的DDL代码，但不会改变作业中的实际代码。您可以在下方预览代码详情。 |

实时计算（流计算）
6. 确定好调试数据后，单击**确定**。
单击**确定**后，SQL编辑器下方会显示调试结果。 实时计算（流计算）

## 运维中心

运维中心提供作业运维、Session管理和配置管理功能，方便您部署、启动、停止、调优作业，管理 Session集群以及配置作业默认参数。

### 作业运维

作业运维页面提供部署、启动、停止、删除作业以及查看作业详情、运行事件、检查点、日志和自动调优等功能，方便您管理作业的全生命周期。

#### 作业部署

作业开发完成后，您需要将作业部署上线，才能启动并运行作业。本文为您介绍如何部署SQL作业、JAR作业和Python作业。

**操作步骤**

**部署SQL作业**

1. 登录实时计算开发控制台。
2. 在**SQL****开发**页面，进行SQL作业开发，详情请参见SQL作业开发。
3. SQL作业开发完毕后，单击**部署**。
4. 填写配置信息如下。

| 参数 | 说明 |
|---|---|
| 备注 | 可选，填写备注信息。 |
| 提交到Session集群 | 不推荐在生产环境使用。 如果您选中了提交到Session集群后，需要在下面的下拉列表中，选择目标Session集群。Session集群创建步骤详情请参见配置Session集群。 |
| 跳过部署前的深度检查 | 选中后，在部署前就跳过深度检查。 |

5. 单击**确定**。

**部署JAR作业**

1. 登录实时计算开发控制台。
2. 在**运维中心** > **作业运维**页面，单击**部署作业**，选择**JAR****作业**。
3. 填写配置信息如下。

| 参数 | 说明 |
|---|---|
| 部署模式 | 请选择部署为流模式或批模式。 |

实时计算（流计算）

| 部署名称 | 填写对应的JAR作业名称。 |
|---|---|
| 引擎版本 | 建议您使用推荐版本或稳定版本，版本标记含义详情如下： 推荐版本：当前最新大版本下的最新小版本。 稳定版本：还在产品服务期内的大版本下最新的小版本，已修复历史版本缺陷。 普通版本：还在产品服务期内的其他小版本。 EOS版本：超过产品服务期限的版本。 |
| JAR URI | 请选择一个文件或者手动上传新文件，您可以拖拽文件到此区域或者单击右侧图标选择文件上传。 说明如果您的作业是Python API类型，则需要填写PyFlink的官方JAR包。官方JAR包的下载地址请参见PyFlink V1.11和PyFlink V1.12。 |
| Entry Point Class | 程序的入口类。如果您的JAR包未指定主类，请在此处输入您的Entry Point Class类的标准路径。 说明如果您的作业是Python API类型，Entry Point Class应该填写为 org.apache.flink.client.python.PythonDriver。 |
| Entry Point Main Arguments | 您可以在此处传入参数，在主方法里面调用该参数。 说明参数信息长度不要大于1024，且不建议用来传复杂参数，复杂参数指包括了换行、空格或者其他特殊字符的参数。如果您需要传入复杂参数，请使用附加依赖文件来传输。 如果您的作业是Python API类型，需要首先上传您的Python作业文件。Python 作业文件上传之后，默认会被上传到作业运行节点的/flink/usrlib/目录下。 假如您的Python作业文件名为word count.py，则该参数需要填写为 -py _ /flink/usrlib/word count.py 。 _ Python作业文件的路径需要填写为完整路径，/flink/usrlib/不能省略，且不能更改。 |

| -py |  |
|---|---|

实时计算（流计算）

| 附加依赖文件 | （推荐）选择您已上传的目标附加依赖文件。 您需要提前通过Flink全托管开发控制台左侧资源管理或部署作业的附件依赖文件右侧的上传附件依赖文件。上传的附件依赖文件会固定被保存在 oss://ossBucketName/artifacts/namespaces/namespaceName/<file> 目录。 填写目标附加依赖文件的OSS路径。 您需要提前将附加依赖文件上传至当前实例对应的OSS Bucket，上传附加依赖文件的OSS Bucket必须为您开通Flink全托管时选择的OSS Bucket。 填写目标附加依赖文件的URL，目前仅支持以文件名结尾的URL，例如 http://xxxxxx/<file>。 您需要提前将附加依赖文件上传至公开可访问的HTTP服务。 说明以上三种方式上传的附件依赖文件，也会被下载到目标机器，在作业运行时，加载到JM和TM所在Pod的/flink/usrlib目录下。 如果作业勾选了提交到Session集群，则该作业不支持配置附加依赖文件路径。 |
|---|---|
| 备注 | 可选，填写备注信息。 |
| 更多设置 | 开启Kerberos按钮，打开该开关后，您需要配置以下信息： Kerberos集群：单击左侧下拉列表选择您已创建的Kerberos集群。 principal：Kerberos principal又称为主体，主体可以是用户或服务，用于在Kerberos加密系统中标记一个唯一的身份。 |

4. 单击**部署**。

**部署Python作业**

1. 登录实时计算开发控制台。
2. 在**作业运维**页面，单击**部署作业**，选择**Python****作业**。
3. 填写配置信息如下。

| 参数 | 说明 |
|---|---|
| 部署模式 | 部署为流模式或批模式。 |
| 部署名称 | 填写对应的Python作业名称。 |
| 引擎版本 | 建议您使用推荐版本或稳定版本，版本标记含义详情如下： 推荐版本：当前最新大版本下的最新小版本。 EOS版本：超过产品服务期限的版本。 |

实时计算（流计算）

| Python文件地址 | 请选择Python作业文件。Python文件可以为.py文件或者.zip文件。 |
|---|---|
| Entry Module | 程序的入口类。如果Python作业文件为.py文件，则该项不需要填写；如果Python作业文件为.zip文件，则需要在此处输入您的Entry Module，例如example.word count。 _ |
| Entry Point Main Arguments | 作业参数。 |
| Python Libraries | 第三方Python包。第三方Python包会被添加到Python worker进程的PYTHONPATH中，从而在Python自定义函数中可以直接访问。 详情请参见使用Python依赖。 |
| Python Archives | 存档文件，目前仅支持ZIP格式的文件，例如 .zip、.jar、.whl和.egg等。详情请参见使用 Python依赖。 存档文件会被解压到Python worker进程的工作目录下。如果存档文件所在的压缩包名称为 mydata.zip，则在Python自定义函数中可以编写以下代码来访问mydata.zip存档文件。 def map(): with open("mydata.zip/mydata/data.txt") as f: ... |
| 附加依赖文件 | 选择您的Python作业文件，以及所依赖的数据文件等。Python依赖详情，请参见使用Python 依赖。上传的依赖文件默认会被下载到作业运行节点的/flink/usrlib/目录下。 说明 Session集群不支持设置附加依赖文件，仅Per-Job集群支持设置附加依赖文件。 |
| 部署目标 | 在下拉列表中，选择目标集群。 说明可选择Session集群或Per-Job集群，未部署到Session集群的作业默认选择Per-Job集群。 |
| 备注 | 可选，填写备注信息。 |
| 更多设置 | 打开该开关后，您需要配置以下信息： Kerberos集群：单击左侧下拉列表选择您已创建的Kerberos集群。 principal：Kerberos principal又称为主体，主体可以是用户或服务，用于在Kerberos 加密系统中标记一个唯一的身份。 |

4. 单击**部署**。

**相关文档**

实时计算（流计算） 部署完成后，您需要在**运维中心** > **作业运维**页面，启动该作业。启动步骤详情请参见作业启动。

#### 作业启动

完成作业开发和部署后，您需要在作业运维页面启动作业至运行阶段。此外，作业在停止后需要恢复、更新了非动态生效的参数配置需要生效时，也需要启动作业。本文为您介绍如何启动作业。

**使用限制**

仅流作业支持填写启动选项。 仅日志服务SLS和消息队列Kafka支持在界面上设置源表开始时间。 作业启动界面指定的读取数据时间优先级高于作业DDL代码里设置的startTime。即如果您在作业DDL和作业启动界面都指定了读取数据时间，则作业启动界面指定的读取数据时间生效。

**说明**

不是所有的Connector都支持startTime，详情请参见各Connector WITH参数是否包含 startTime。 只有全新启动作业并指定了startTime，startTime才生效。如果基于Checkpoint或 Savepoint启动作业，即使指定了startTime，startTime也不会生效。

**注意事项**

在启动作业时，如果您选择从最新状态或指定状态启动作业时，系统会进行State兼容性检测。

**操作步骤**

1. 登录实时计算开发控制台。
2. 在**运维中心** > **作业运维**页面的下拉列表中，选择**流作业**或**批作业**。
3. 在目标作业名称右侧，单击**操作**列下的**启动**。
4. （可选）流作业需要填写启动选项信息。
**无状态启动**：当您是新上线作业或者无法复用State时，需要选择无状态启动。此外，您需要根据业务
情况决定是否打开自动调优。

| 策略 | 说明 |
|---|---|

实时计算（流计算）

| 指定源表开始时间 | 选中指定源表开始时间并指定具体的时间信息。 作业启动界面指定的读取数据时间优先级高于作业DDL代码里设置的startTime。 说明 0.11版本以下的Kafka不保证获得支持，因为连接器所使用的Kafka客户端版本可能存在不兼容的问题，所以建议升级Kafka版本。 不是所有连接器都支持配置startTime参数，详情请参见各连接器WITH 参数是否包含startTime。 只有全新启动作业并指定了startTime，startTime才生效。如果基于系统检查点或作业快照启动作业，指定了startTime不会生效。 |
|---|---|
| 配置自动调优 | 打开该开关后，您需要选择调优模式： 智能调优：系统将在资源使用率比较低时，自动降低资源配置，在资源使用率提高到一定阈值时，再自动提高资源配置。 定时调优：选择定时调优后，您需要在下拉列表中选择定时计划。一个计划中可以包含多组资源和时间点的对应关系。您可以根据各时间段的资源使用情况，配置对应的资源。 详情请参见配置自动调优。 |

**有状态启动**：您可以根据业务情况选择具体的策略，以及决定是否打开自动调优。

| 策略 | 说明 |
|---|---|
| 从最新状态恢复 | 从快照或者系统检查点的最新状态进行恢复。如果您选择从最新状态启动作业时，系统会进行State兼容性检测。 |
| 从指定状态恢复 | 选择指定的快照。 |
| 从其他作业恢复 | 选择从其他作业恢复后，您需要指定目标作业及对应的快照，来进行作业恢复。 支持作业间快照的共享，但需要满足作业间的状态的兼容性。 |
| 允许忽略部分算子状态 （AllowNonRestored State） 说明不支持SQL作业。 | 默认情况下，Flink系统会尝试将整个快照与正在提交的作业匹配。作业的修改引起算子状态的变化，会出现任务不能恢复的情况。此时您可以打开此开关，Flink 系统将跳过无法匹配的状态，让作业先正常启动起来。允许忽略部分算子状态详情请参见Allow None-Restored State。 |

实时计算（流计算）

| 配置自动调优 | 打开该开关后，您需要选择调优模式： 智能调优：系统将在资源使用率比较低时，自动降低资源配置，在资源使用率提高到一定阈值时，再自动提高资源配置。 定时调优：选择定时调优后，您需要在下拉列表中选择定时计划。一个计划中可以包含多组资源和时间点的对应关系。您可以根据各时间段的资源使用情况，配置对应的资源。 详情请参见配置自动调优。 |
|---|---|

5. 单击**启动**。
在**运维中心** > **作业运维**页面，查看作业运行状态。

#### 作业停止

更改了SQL逻辑或作业版本、增删WITH参数或增加作业参数后，需要经过作业停止和启动的步骤，才能使变更生效。本文为您介绍如何停止状态为RUNNING的作业。

**注意事项**

作业停止后再启动时，您可以选择全新启动（无状态），同时您也可以指定读取数据的时间；或者从所选 Savepoint恢复作业。详情请参见作业启动。

**说明**

如果您修改了SQL等逻辑导致State不兼容，则只能从无状态启动作业。

**操作步骤**

1. 登录实时计算开发控制台。
2. 在**运维中心** > **作业运维**页面的下拉列表中，选择**流作业**或**批作业**。
3. 单击目标作业**操作**列下的**停止**。
4. 单击**确定。**
更多设置中的选项说明如下： 实时计算（流计算）
**停止前创建一次快照**：如果您需要在停止前创建一次快照，则需要先单击**更多设置**，然后选中**停止前创**
**建一次快照**。选中**停止前创建一次快照**，作业会先进行快照创建，然后进入停止流程。如果您未选中停
**止前创建一次快照**，则作业会直接进入停止流程。
**输出窗口数（****Drain**）：该选项用于永久性终止作业。
如果您希望稍后再重新启动作业，请不要选中该选项。因为恢复作业时，可能会出现错误的结果。

#### 作业调优

作业调优提供自动调优能力，支持智能调优和定时调优两种模式，帮助您根据作业运行情况自动调整资源配置。

##### 配置自动调优

Flink作业支持智能调优和定时调优两种自动调优模式。本文介绍如何配置智能调优和定时调优，以及配置过程中的注意事项。

**背景信息**

通常，您需要花费大量的时间进行作业调优。例如，新上线一个作业时，需要考虑如何配置该作业的资源、 并发个数、Task Manager个数及大小等。此外，作业运行过程中，还需要考虑如何调整作业资源，使作业处于最高资源利用率；作业出现反压或延时增大的情况时，需要考虑如何调整作业配置等。实时计算Flink版提供了自动调优功能，其优势在于： 帮您更合理地调整作业并发度和资源配置； 全局优化您的作业，解决作业吞吐量不足、全链路存在反压和资源浪费等各种性能调优问题。 您可以根据以下信息，选择合适的调优模式。

| 调优模式 | 适用场景 | 相关文档 |
|---|---|---|
| 智能调优 | 某作业使用资源30 CU，上线平稳运行一段时间后，发现在 Source无延迟、无反压的情况下，作业的CPU和内存使用率有时会很低。 此时如果您不想人工调节资源，需要系统自动完成资源调节，可以使用智能调优模式。系统将在资源使用率比较低时，自动降低资源配置，在资源使用率提高到一定阈值时，再自动提高资源配置。 | 开启智能调优功能，请参见开启并配置智能调优。 |
| 定时调优 | 定时调优计划描述了资源和时间点的对应关系，一个定时调优计划中可以包含多组资源和时间点的关系。 在使用定时调优计划时，您需要明确知道各个时间段的资源使用情况，根据业务时间区间特征，设置对应的资源。 例如，某业务全天早09：00~19：00是业务高峰，19：00到第二天09：00是业务低峰。此时您可以使用定时调优功能，在高峰时间段使用30 CU，在业务低峰时使用10 CU。 | 配置定时调优策略，请参见配置并应用定时调优计划。 |

**使用限制**

最多创建20个资源计划。 在开启unaligned checkpoint时，不支持调整并发。 智能调优不支持Session集群部署的作业。 实时计算（流计算） 调优模式之间互斥，需要先停止正在应用的模式，才可以应用另一种。 定时调优和智能调优模式互斥，如果您应用了任何一种调优模式，则无法应用另一种。如果您需要应用另一种调优模式，则需要先停止正在应用的调优模式。 定时调优中的定时计划互斥，如果您应用了某个定时计划，则无法应用其他定时调优计划。如果您需要应用其他定时调优计划，则需要先停止正在应用的定时调优计划。

**注意事项**

任何模式的调优使作业重启时，会导致作业短暂停止消费数据。

**说明**

VVR 8.0.1及以上版本，Flink系统会先尝试使用动态参数更新重启作业，再尝试使用作业整体重启。 动态参数更新下业务中断时间较之作业整体重启缩短30%-98%，具体依赖于作业状态和逻辑，目前如果您使用了DataStream作业或SQL自定义的连接器，请确认作业代码中未配置作业并发度，否则智能调优和定时调优将无法调整作业资源，即自动调优配置无法生效。 智能调优无法解决流作业所有的性能瓶颈。 流作业性能问题是由上下游共同决定的，如果是Flink出现了瓶颈，可以通过Flink资源调优解决。但调优策略对作业的处理模式是基于一定的假设的。例如，流量平滑变化、不能有数据倾斜、每个算子的吞吐能力能够随并发度的升高而线性拓展。当业务逻辑严重偏离以上假设时，作业可能会存在异常。例如： 无法触发修改并发度的操作、作业不能达到正常状态和作业持续重启等。 自定义标量函数UDF、自定义聚合函数UDAF或自定义表值函数UDTF性能问题。 智能调优无法识别外部系统的问题。如果出现外部系统问题，您需要自行解决。 外部系统故障或访问变慢时，会导致作业并发度增大，加重外部系统的压力，导致外部系统雪崩。常见的外部系统问题如下： 数据总线DataHub分区不足或消息队列RocketMQ吞吐量不足。 Sink性能问题。 云数据库RDS死锁。 在进行资源调整时，系统会进行资源对比并确定资源调整方式。 如果要应用的资源计划和现在线上配置是CPU或Memory的变更，作业就会使用停止->启动的方式进行资源调整，可能会出现业务中断、数据回追延迟和资源不足导致启动失败等问题。如果仅是并发度的变

**开启并配置智能调优**

**调优策略**

| 策略 | 适用场景 | 作用及优势 |
|---|---|---|
| （推荐） 自适应策略 | 适用于资源需求波动较大、对延迟高度敏感、多任务并发、存在数据倾斜或负载不均以及长时间运行的场景。 | 应用该策略后，系统会根据实时作业资源和指标信息动态修改资源配置，更加关注当前作业的延时和资源使用情况，并根据相关指标的变化更快速地优化资源适配。 这样做可以使系统更加敏锐地响应作业需求，提高资源配置的效率和适应性。 |

实时计算（流计算）

| 平稳策略 | 适用于资源需求相对稳定、启停成本较高且对稳定性要求较高的周期性任务、定时任务以及长时间运行的场景。 | 通过应用该策略，系统会寻找适合整个运行周期的固定资源或定时计划，并根据整个周期作业的运行情况来调整作业资源，从而减少启停行为对作业的影响。这样做可以使作业的运行趋于稳定，减少不必要的变动和波动，最终达到收敛状态。 说明只有找到更适合整个周期的资源配置，才会动态调整，否则不会修改已有资源。在达到平稳状态后，会输出资源调整方案， 您可以保存并应用，详情请参见保存资源调整计划。 重新启停作业，或者进行hot-update会破坏平稳状态，会进行重新调优。 |
|---|---|---|

**操作步骤**

1. 进入智能调优开启和配置页面。
ii. 在左侧导航栏选择**运维中心** > **作业运维**，单击目标作业名称，默认展开作业详情页面。 iii. 在**自动调优**页签，单击**智能调优模式**。
2. 打开**自动调优**开关。
开启后，在自动调优页签页面顶部会显示**智能调优应用中**。如果您需要关闭已开启的智能调优，则可以单击**关闭智能调优**或者关闭**自动调优**右侧的开关。
3. 单击**调优配置**右侧的**编辑**后，选择调优策略并修改智能调优相关参数。

**（推荐）自适应策略**

| 参数 | 说明 |
|---|---|
| 最大CPU限制 | 作业自动调整资源可以扩容的最大CPU上限，默认值为64 Core。 |
| 最大内存限制 | 作业自动调整资源可以扩容的最大内存上限，默认值为256 GiB。 |
| 最大并发度 | 自动调优可以设置的最大并发度，默认值为1024。 说明对于消息队列类产品（例如Kafka，MQ，SLS等），自动调优并发的调整会受到分区数的影响，无法超过该上限。即如果您设置的并发度最大值超过其分区数，系统将自动调整并发度为分区数。 |
| 最小并发度 | 自动调优可以设置的最小并发度，默认值为1。 |

实时计算（流计算）

| 扩容策略 | 满足以下任何一个条件即可触发扩容。如果某些参数不适用于当前业务场景，可以通过单击右侧的禁用按钮将其关闭。 作业的延时是否超过某个阈值，并且该状态需要持续一定时间。 作业单个算子的平均Busy是否超过某个阈值，并且该状态需要持续一定时间。 作业单个TaskManager（TM）的内存使用率是否超过某个阈值。 作业是否发生OutOfMemory（OOM）异常。 作业TaskManager（TM）或JobManager（JM）的每秒垃圾回收（GC）耗时占比是否超过某个阈值，并且该状态需要持续一定时间。 说明您可以根据历史运行数据或默认值设置阈值。如果参考数据不可用，可以开始时先设定一个相对宽松的阈值，观察一段时间后再进行调整。阈值的单位为百分比，取值范围为0% ~ 100%。 持续时间用于过滤瞬时波动，避免因短暂异常而频繁触发扩容。合理设置持续时间有助于提高扩容的准确性。时间单位可以根据需求进行选择。 是否发生OOM异常，无需填写具体值，只需启用或禁用。 |
|---|---|
| 缩容策略 | 满足以下任何一个条件即可触发缩容。如果某些参数不适用于当前业务场景，可以通过单击右侧的禁用按钮将其关闭。阈值单位为百分比，您可以根据需要选择时间单位。 单个算子的平均Busy是否小于某个阈值（单位为百分比），并且该状态需要持续一定时间。 单个TaskManager（TM）的内存使用率是否小于某个阈值。 |
| 高级参数配置 | 某些规则尚处于测试阶段，暂时无法全面提供。如有相关需求，欢迎联系我们以获取支持。 |

**平稳策略**

| 参数 | 说明 |
|---|---|
| 调整间隔时间 （分钟） | 作业调优重启生效一次之后，下一次再进行调优的时间间隔。默认值是10分钟。 |
| 最大CPU限制 | 作业自动调整资源可以扩容的最大CPU上限，默认值为16 Core。 |
| 最大内存限制 | 作业自动调整资源可以扩容的最大内存上限，默认值为64 GiB。 |
| 最大可接受延迟 | 可以容忍的最大延迟阈值。默认值为1分钟。 |

实时计算（流计算）

| 更多参数配置 | 可以配置的参数如下： mem.scale-down.interval ：调低内存时的最小触发时间间隔。 默认值为4小时。4小时内，检测到内存使用率低于设定的阈值，系统将会调整内存分配，或建议减少内存分配以优化资源利用率。 parallelism.scale.max ：并发度向上调整时，最大并发限制。 默认值为-1，表示最大并发没有限制。 说明对于消息队列类产品（例如Kafka，MQ，SLS等），自动调优并发的调整会受到分区数的影响，无法超过该上限。即如果您设置的并发度最大值超过其分区数，系统将自动调整并发度为分区数。 parallelism.scale.min ：并发度向下调整时，最小并发限制。 默认值为1，表示最小并发为1。 delay-detector.scale-up.threshold ：可以容忍的最大延迟阈值。基于消费数据源头的延迟，来衡量作业处理吞吐的能力。 默认值为1分钟。当数据处理能力不足导致延迟超过1分钟，将通过Scale Up方式来提高作业的吞吐能力，Scale Up方式包括增加并发或者拆分Chain，或建议Scale Up。 slot-usage-detector.scale-up.threshold ：设定处理节点（不含 Source）的计算/IO资源使用率阈值。当节点处理数据的时间占比持续高于此值，系统将增加并发度。默认值为 0.8。 slot-usage-detector.scale-down.threshold ：设定处理节点（不含 Source）的计算/IO资源使用率阈值。当节点处理数据的时间占比持续低于此值，系统将减少并发度。默认值为 0.2。 slot-usage-detector.scale-up.sample-interval ：系统采样处理节点使用率的时间跨度。系统计算该时间段内的平均使用率，并与上述两个阈值比较，决定是否进行 scale-up 或scale-down。默认值为 3 分钟。 resources.memory-scale-up.max ：调整单个Task Manager和Job Manager的内存时，能调整到的最大值。 默认值为16 GiB。TM和JM进行智能调优或调大并发时，内存的上限为16 GiB。 |
|---|---|

4. 单击**保存**。

**保存资源调整计划**

**平稳策略**在作业的运行趋于稳定后，系统会自动生成固定资源或定时计划方案供您选择，您可以手动查看、
分析、保存或应用资源调整方案。推荐方案详情如下。

| 推荐方案 | 使用说明 | 备注 |
|---|---|---|
| 固定资源 | 输出单个不含时间维度的资源配置。 在自动调优页面单击查看详情后，选中固定资源，单击保存后单击确定。 | 单击确定后，作业部署上的资源配置将被预估的资源配置代替，在作业下次启动时被应用。 |

实时计算（流计算）

| 定时计划 | 输出时间段和每个时间段的资源配置。 您可以将系统生成的定时计划保存后继续应用，具体操作请参见保存定时计划并应用。 | 智能调优中应用该定时计划后，调优模式将从智能调优自动更换为定时调优，达到平稳后将不会再调整资源。 |
|---|---|---|

**配置并应用定时调优计划**

**操作步骤**

**新建定时计划并应用**

1. 进入开启并配置定时调优页面。
ii. 在左侧导航栏选择**运维中心** > **作业运维**，单击目标作业名称，默认展开作业详情页面。 iii. 在**自动调优**页签，单击**定时调优模式**。
2. 单击**新建定时计划**。
3. 在**资源配置**区域，填写资源配置信息。
**触发周期**：您可以选择单次触发、每天、每周和每月。当选择每周和每月时，您还需要指定对应的生效
日期范围。
**生效时间**：选择具体的生效时间。
**运行参数**：参数配置详情请参见运行参数配置。
4. （可选）单击**新增资源配置时段**后，配置生效时间和资源配置。
您可以在同一个定时计划中，配置多个时间段的资源调优计划。

**重要**

同一定时计划中，**新增资源配置时段**的触发时间必须和已有资源配置的触发时间之间的间隔大于半小时，否则无法保存新的资源配置。
5. 单击**确定**，保存定时计划。
6. 单击目标资源定时计划名称右侧**操作**列下的**应用**。

**保存定时计划并应用**

**平稳策略**在作业的运行趋于稳定后，系统会自动生成定时计划方案供您查看、分析、保存并应用。
1. 进入自动调优页面。
ii. 在左侧导航栏选择**运维中心** > **作业运维**，单击目标作业名称，默认展开作业详情页面。 iii. 单击**自动调优**页签。
2. 单击**查看详情**后，**推荐方案**选中**定时计划**。
3. 配置定时计划。

| 动作 | 说明 | 备注 |
|---|---|---|

实时计算（流计算）

| 1、设置最大变更次数。 | 指定定时计划最多出现的变更次数。 | 下限为2次，上限为5次。 |
|---|---|---|
| 2、单击合并时间段。 | 根据您设定的最大变更次数进行合并。 | 合并时，根据具体情况考虑是否提前扩容或缩减资源，以满足相应的策略要求。 |

4. 查看与修改合并后的资源配置。配置详情请参见配置作业资源。
5. 单击页面左下角的**保存**。
6. 填写**定时计划名称**，或勾选**应用本计划**，单击**确定**。
智能调优中应用该定时计划后，调优模式将从智能调优自动更换为定时调优，达到平稳后将不会再调整资源。

**配置示例**

全天09：00~19：00是业务高峰，在高峰时间段使用30 CU。19：00到第二天09：00是业务低峰，在业务低峰时使用10 CU。该场景的调优策略配置结果如下图所示。

##### 配置作业资源

您可以在作业启动前配置作业资源或者作业上线后修改作业资源，支持基础模式（粗粒度）和专家模式（细

**背景信息**

实时计算Flink版支持基础模式（粗粒度）和专家模式（细粒度）两种资源配置模式。

| 资源模式 | 说明 |
|---|---|

实时计算（流计算）

| 基础模式 | 基础模式是一种静态资源分配方式，您只需要给定每个TM启动所需要的总资源（CPU和 JVM总内存），系统会根据每个TaskManager Slot数（即flink conf taskmanager.numberOfTaskSlots）均匀分配所有资源。对于大多数简单作业，粗粒度即可满足要求。 详情请参见配置作业资源。 |
|---|---|
| 专家模式 | 专家模式是一种动态资源分配方式，您可以配置每个Slot共享组（Slot Sharing Group，SSG）所需要的资源，Flink会计算出每个Slot需要的资源规格大小，动态地从可用资源池中申请完全匹配的TM和Slot。对于复杂作业，粗粒度可能导致资源利用率低，因此需要细粒度资源对每个算子进行精细资源控制，从而提高资源使用率，满足作业吞吐的要求。 详情请参见配置作业资源。 |

关于TM、JM、Task或Slot等概念，详情请参见Apache Flink Architecture。

**使用限制**

仅SQL作业支持配置专家模式。

**注意事项**

资源配置后，需重启作业才能生效。

**操作步骤**

1. 进入**作业运维**页面。
ii. 在左侧导航栏选择**运维中心** > **作业运维**，单击目标作业名称，默认展开作业详情页面。
2. 在**部署详情**页签，单击**资源配置**区域右侧的**编辑**。
3. 修改作业资源信息。

**基础模式（粗粒度）配置项说明**

| 配置项 | 说明 |
|---|---|
| 并发度 | 作业全局并发数。 |
| JobManager CPU | 根据Flink最佳实践，单个JM内存资源需要至少配置为0.5 Core和2 GiB，才能保证作业稳定运行。建议您配置为1 Core和4 GiB。最大值为16 Core。 |
| JobManager Memory | 单位为GiB，最小值为2 GiB，最大值为64 GiB。 |
| TaskManager CPU | 根据Flink最佳实践，单个TM内存资源需要至少配置为0.5 Core和2 GiB， 才能保证作业稳定运行。建议您配置为1 Core和4 GiB。最大值为16 Core。 |
| TaskManager Memory | 单位为GiB，最小值为2 GiB，最大值为64 GiB。 |

实时计算（流计算）

| 每个TaskManager Slot数 | 请填写TM的Slot数。 |
|---|---|

您可以根据以下公式进行推算：
**作业所配置的****CU**数 = **MAX**（**JM**和**TM**的**CPU****总和****, JM**和**TM****的内存总和****/4****）。**

**实际TM数（设置的TM的CPU或内存小于等于其默认最大值）= 设置的并发度/设置的每个**

**TaskManager Slot数。**

**实际****TM****数（设置的****TM**的**CPU****或内存大于其默认最大值）****= MAX**（⌈**TM**总**CPU**数**/16 Core**⌉，⌈**TM**
**总内存数****/64 GiB**⌉）。
TM总CPU数=设置的并发度/设置的每个TaskManager Slot数×设置的单个TM CPU。 TM总内存数=设置的并发度/设置的每个TaskManager Slot数×设置的单个TM的内存。 TM的CPU默认最大值为16 Core。 TM的内存默认最大值为64 GiB。
**实际每个****TM****上可分配的****slot**数 = ⌈**设置的并发数**/**实际****TM**数⌉。

**说明**

计算比值需分别向上取整。 您也可以在作业**部署详情**页签**运行参数配置**区域的**其他配置**中设置numberOfTaskSlots参数，和界面配置**每个****TaskManager Slot**数作用相同，但优先级更高。

**专家模式（细粒度）配置项说明**

**说明**

仅SQL作业支持配置专家模式。 在部署作业后，若对SQL或者资源配置进行了修改，需要重新生成资源计划图，以确保作业能够正常启动。

**配置基础资源**

| 配置项 | 说明 |
|---|---|
| JobManager CPU | 根据Flink最佳实践，单个JM内存资源需要至少配置为0.25 Core和1 GiB，才能保证作业稳定运行，最大值16 Core。 |
| JobManager Memory | 单位为GiB，例如，4 GiB。最小值为1 GiB，最大值64 GiB。 |
| 每个TaskManager Slot数 | 无。 |

**配置Slot资源**

实时计算（流计算） i. 在**专家模式**下，单击**立刻获取**，获取资源计划图。 ii. 单击**SLOT**框上的图标。 iii. **修改****SLOT**配置信息。 此处设置的并发数为该Slot共享组内所有算子的统一并发数。设置完成后，系统将自动进行以下操作： 系统会根据作业的计算逻辑按需自动生成Statebackend、Python和Operator所需的内存，无需您手动进行配置

**说明**

建议在有明确异常或者需求时，再调整Heap Memory和Off-Heap Memory的大小，例如作业出现OOM或严重GC等。因为在作业正常运行时，调整Heap Memory和Off-Heap Memory的大小，不会明显改变作业的吞吐量。 iv. 单击**确定**。

**配置算子并发数与Chain策略**

实时计算（流计算） i. 修改VERTEX并发数。 单击目标VERTEX上的图标，批量设置对应VERTEX下的算子并发数。 ii. 单击目标VERTEX框上的展开VERTEX。 实时计算（流计算） iii. 单击算子的图标，配置算子资源。 参数说明如下：

| 参数 | 说明 |
|---|---|
| 并发数 | 对应算子的并发数。 |
| Chaining策略 | Chain是指多个算子被连接在一起形成的逻辑计算链。它能够提高作业的执行效率和性能，减少数据在算子之间的传输和序列化开销。不过有时可能需要将Chain断开，以便更好地控制作业的执行流程和性能。支持配置策略如下： ALWAYS（默认值）：算子始终可以和上下游算子Chain一起。 HEAD：当前算子作为Chain的头节点，只和上游算子断开Chain，下游节点仍和当前算子Chain在一起。 NEVER：当前算子不会与上下游算子进行Chain。 |

**说明**

建议Source节点并发度和分区数成比例，即并发度数能整除分区数。例如Kafka有16个分区，则并发度建议设置为16、8或4，这样可以避免数据倾斜。同时Source节点的并发度不宜设置太小，避免一个Source需要读取太多数据，导致出现入口瓶颈，影响作业吞吐。 建议按需配置除Source外的其他节点的并发度。流量大的节点，并发设置大一些；流量小的节点，并发设置小一些。 iv. 单击**确定**。
4. 单击**保存**。
5. 重启作业。
作业资源配置后，需重启作业才能生效。

**相关文档**

实时计算（流计算） 如果不想手动调节资源，可以使用自动调优，系统会自动完成资源调节，详情请参见配置自动调优。

#### 参数动态更新

动态更新Flink作业参数可以实现更快的参数配置生效，减少作业启停对业务的中断时间，方便进行TM动态

**背景信息**

传统的Flink参数更新方式需要重新启动作业，可能会出现业务中断、数据回追延迟和资源占用高峰等问题， 导致作业停止时间变长，影响业务连续性。 动态更新参数功能通过REST请求发送至运行中的作业，它允许作业复用现有的JobManager和 TaskManager容器，以原地重启、甚至不重启的方式来进行更新，从而降低重启的代价。配合资源预申请、State lazy加载等能力，进一步提升更新后的作业启动速度，将参数更新带来的断流时间从分钟级降到秒级。以一个典型的Source -> Map -> Sink作业为例，在动态扩缩容操作中，通过动态参数更新可以显著减少断流时间。断流时间对比情况如下图所示。

**说明**

您可以通过动态更新并发度来实现动态扩缩容TM，实际TM个数推算详情请参见配置作业资源。

**使用限制**

仅实时计算引擎VVR-11.5.0-flink-1.20版本支持动态更新参数。 专家模式（细粒度）不支持动态更新并发度。

**注意事项**

动态更新为实验性功能，在动态更新参数时，业务并不是完全不中断。相比传统的参数修改模式，动态更新能够显著缩短中断时间，但中断的具体时长受到作业拓扑和状态大小等因素的影响，通常在5秒至1分钟之间。 仅作业处于运行状态时，才能动态更新参数并让其生效。 在动态更新并发度时，由于节点的并发度在某些场景下有特殊要求（例如：Global算子的并发度必须为 1，不能更改；用户显式设置Kafka Source的并发度，以避免其超过其分区数），因此，实时计算Flink 版会跳过已被设置并发度的节点，仅修改未指定并发度的节点。如果您希望节点的并发度可以被动态更新，建议不要通过DataStream#setParallelism方法或Source/Sink的并发度配置参数等方式指定算子的并发度。 仅**并发度**、**系统检查点间隔**、**系统检查点超时时间**以及**两次系统检查点最短间隔**参数支持动态更新。参数值修改后，才会出现**动态更新**按钮，单击按钮后生效。如果您同时修改了无法动态更新的参数，需要重新启动作业才能使这些参数生效。

**操作步骤**

实时计算（流计算）
1. 进入**作业运维**页面。
ii. 在左侧导航栏选择**运维中心** > **作业运维**，单击目标作业名称，默认展开作业详情页面。
2. 在**部署详情**页签，单击**资源配置**或**运行参数配置**区域右侧的**编辑**。
3. 修改可以提示“动态更新”的参数取值后，单击**保存**。

**重要**

仅**并发度**、**系统检查点间隔**、**系统检查点超时时间**以及**两次系统检查点最短间隔**参数支持动态更新。 参数值修改后，才会出现**动态更新**按钮，单击按钮后生效。如果您同时修改了无法动态更新的参数， 需要重新启动作业才能使这些参数生效。
4. 单击页面右上角的**动态更新**。
5. 在弹出的对话框中查看提示信息后，单击**确定**。
单击**确定**后，您会看到正在更新的标识。

**相关文档**

不支持动态更新的参数，您可以在**部署详情**页签配置后重启作业，详情请参见作业默认配置和作业启动。 自动调优功能可以帮助您更合理地调整作业并发度和资源配置，解决相关性能调优问题，详情请参见配置自动调优。

### 配置Session集群

您可以使用Session集群模式部署或调试作业，提高作业JM（Job Manager）资源利用率和作业启动速度。 本文介绍实时计算Flink中Session集群的使用建议及创建方法。

**重要**

因Session集群JobManager共用，JobManager异常将导致该集群所有作业异常，请勿在生产环境中使用Session集群。 实时计算（流计算）

**背景信息**

实时计算Flink支持Per-Job集群和Session集群两种集群模式。两种集群模式有以下区别： Per-Job集群（默认）：作业之间资源隔离，每个作业都需要一个独立的JM，小任务JM的资源利用率较低。因此，适用于占用资源比较大或持续稳定运行的作业。 Session集群：多个作业可以复用相同的JM，可以提高JM资源利用率。因此适用于占用资源比较小或任务启停比较频繁的作业，可以有效节约资源开销。

**说明**

Session集群暂不支持开启自动调优功能。 无论您是否使用Session集群，在创建Session集群时会消耗集群资源，其中消耗的资源和您创建集群时选择的资源配置有关。

**使用限制**

Session集群有以下限制： 暂停Session集群后，不支持修改Flink计算引擎版本。 暂停Session集群后，不支持对TM个数或资源进行缩容。 不支持显示数据曲线。 不支持监控告警功能。 实时计算Flink（存算分离）不支持容灾使用。

**注意事项**

请勿将Session集群用于正式生产环境，Session集群可以作为开发测试环境。使用Session集群调试作业，可以提高作业JM（Job Manager）资源利用率。在正式环境中使用Session集群，JM的复用机制会对作业间的稳定性产生负面影响，详情如下： JobManager单点故障会对集群内的所有作业造成影响。 TaskManager单点故障会对在其上有task运行的相关作业造成影响。 同一个TaskManager内部，不同Task之间如果没有进程隔离，则存在相互影响的潜在风险。 如果Session集群为默认配置，则有以下建议： 对于单并发的小作业，建议整个集群的作业总数不超过100个。 对于复杂作业，建议单作业最大并发数不超过512，64个并发的中等规模作业单集群不多于32个。否则可能会出现心跳超时等问题影响集群稳定性。此时，您需要增大心跳间隔和心跳超时时间。 如果您需要同时运行更多的任务，则需要增加Session集群的资源配置。 不建议使用开启了SQL Preview的Session集群运行作业。因为如果产品后续发布新版本，则需要停止 Session集群后，手动适配Flink计算引擎，否则本地调试会报错。

**创建Session集群**

1. 进入**Session****管理**页面。
ii. 在左侧导航栏，单击**运维中心** **> Session****管理**。
2. 单击**创建****Session****集群**，填写配置信息。
实时计算（流计算） 参数解释如下表所示。

| 模块 | 配置项 | 说明 |
|---|---|---|
| 基础配置 | 名称 | 集群名称。 |
|  | 部署目标 | 在下拉列表中，选择目标集群。 说明可选择Session集群或Per-Job集群，未部署到Session集群的作业默认选择Per-Job集群。 |
|  | 状态 | 设置当前集群的期望运行状态： STOPPED：当集群配置完成后保持停止状态，同样会停止所有在运行中的作业。 RUNNING：当集群配置完成后保持运行状态。 |
|  | 标签名 | 您可以在标签选项中添加作业标签，便于在总览页面快速定位作业。 |
|  | 标签值 | 无。 |
|  | 引擎版本 | 当前作业使用的Flink的引擎版本。建议您使用推荐版本或稳定版本，引擎版本标记含义详情如下： 推荐：当前最新大版本下的最新小版本。 EOS：超过产品服务期限的版本。 |

|  | 时计算（流计 |  |  |
|---|---|---|---|
|  | 配置 |  |  |
|  |  | Flink重启策略配置 | 该参数取值如下： Failure Rate：基于失败率重启。选择该选项后，您还需要填写检测失败率的时间间隔，时间间隔内的最大失败次数和每次重启时间间隔。 Fixed Delay：固定间隔重启。选择该选项后，您还需要填写尝试重启的次数和每次重启时间间隔。 No Restarts：作业task失败不会重启。 说明如果您没有配置该参数，则按Apache Flink默认的重启策略，即当有Task 失败时，如果没有开启Checkpoint，JobManager进程不会重启。如果开启了Checkpoint，则JobManager进程会重启。 |
|  |  |  | 在此设置其他Flink配置。例如 taskmanager.numberOfTaskSlots: 1 。 |
|  | 其他配置 |  | 1 |
|  | 资源配置 | Task Managers 数量 | 默认与并行度一致。 |
|  |  | JobManager CPU Cores | 默认值为1。 |
|  |  | JobManager Memory | 推荐值：4 GiB，最小值：1 GiB。单位GiB，例如：1 GiB或1.5 GiB。 JobManager推荐配置包含JobManager资源以及心跳相关参数。具体内容如下： 由于JobManager上承载TaskManager心跳、作业Task序列化和资源调度等功能。因此建议JobManager资源不小于默认配置，请根据集群负载情况进行处理。 为了集群稳定，避免JobManager主线程繁忙导致心跳超时。因此建议心跳间隔（heartbeat.interval）不小于10秒，同时心跳超时 （heartbeat.timeout）不小于50秒。请根据TaskManager个数与作业量上涨情况而上调。 |
|  |  | TaskManager CPU Cores | 默认值为2。 |

实时计算（流计算）

|  | TaskManager Memory | 推荐值：8 GiB，最小值：1 GiB。单位GiB，例如：1 GiB或1.5 GiB。 TaskManager推荐配置包含单个TaskManager的Slot个数 （taskmanager.numberOfTaskSlots）及TaskManager资源大小。具体内容如下： 对于单并发小作业，建议单Slot的CPU内存比为1:4，使用的资源不小于1核2 GiB。 对复杂作业，建议单Slot使用资源不小于1核4 GiB。在默认资源配置下，每个TaskManager可以配置2个Slot。 TaskManager资源不宜过小，也不宜过大，推荐使用默认资源配置并将Slot 数目设为2。 说明如果单个TaskManager资源过小，则可能影响其上作业的稳定性，并且由于其Slot数目不多，无法有效平摊TaskManager的开销，降低了资源的利用效率。 如果单个TaskManager资源过大，则TaskManager上运行的作业数会很多，一旦TaskManager发生单点故障，影响面会很大。 |
|---|---|---|
|  | 根日志等级 | 日志级别从低到高的顺序如下： TRACE：比DEBUG更细粒度的信息。 DEBUG：系统运行状态的信息。 INFO：重要或者您感兴趣的信息。 WARN：系统可能出现潜在错误的信息。 ERROR：系统出现错误和异常的信息。 |
| 日志配置 |  |  |
|  | 类日志名称 | 填写日志名称。 |
|  | 类日志等级 | 填写日志级别。 |
|  | 日志模板 | 日志模板，可以选择系统模板，也可以选择自定义模板。 |

4. 单击**创建****Session****集群**。
Session集群创建完成后，您需要单击**启动**。启动后，您就可以在创建作业的部署目标中选择此集群。

### 作业默认配置

本文介绍如何管理流作业和批作业的默认配置信息，包括运行参数、Flink重启策略、日志配置等，您可以按需进行修改。
1. 登录实时计算开发控制台。

| 在左侧导航栏，单击 | 运维中心 |
|---|---|

| 配置管理 | 。 |
|---|---|

3. 在**作业默认配置**下，单击**流作业**。
实时计算（流计算）
4. 进行参数修改。

| 参数 |  | 说明 |
|---|---|---|
| 运行参数配置 | 系统检查点间隔 | 定时执行 Checkpoint 的时间间隔，如果不填写，将会使用作业引擎版本的默认值，默认值为180秒。 |
|  | 两次系统检查点之间的最短时间间隔 | 两次系统检查点之间的最短时间间隔，如果 Checkpoint 最大并行度是1，那么这个配置确保两个 Checkpoint 之间有一个最短时间间隔，如果不填写，将会使用作业引擎版本的默认值。默认值为180秒。 |
|  | 系统检查点超时时间 | 默认值： - 。系统检查点超时时间，默认值为10min，到达默认值后系统检查点将生成失败。 |
|  | State数据过期时间 | 设定的 Flink 状态生存时间，状态服务每经过设置的时间就会清理当前存储的状态。默认值为36小时。 |
|  | Flink重启策略配置 | 支持以下三种策略： Failure Rate：基于失败率重启。选择该选项后，您还需要填写检测 Failure Rate 的时间间隔、时间间隔内的最大失败次数和每次重启时间间隔。 Fixed Delay：固定间隔重启。选择该选项后，您还需要填写尝试重启的次数和每次重启时间间隔。 No Restarts：作业任务失败后不会重启。 |
|  | 尝试重启的次数 | Flink 在宣告作业失败之前重试执行的次数。 如果通过检查点激活，则使用 Integer.MAX VALUE。默认值为2147483647。 _ |
| 文档版本：202607 | 30 8 |  |

实时计算（流计算）

|  | 每次重启时间间隔 | 延迟重试意味着在执行失败后，重新执行不会立即开始，而只会在一定的延迟后开始。默认值为10秒。 |
|---|---|---|
| 其他配置 | / | 可以在此设置其他 Flink 配置。 例如： taskmanager.numberOfTaskSlots: 1 。 |
| 日志配置 | 根日志等级 | 日志级别从低到高顺序如下： TRACE：比DEBUG更细粒度的信息。 DEBUG：系统运行状态的信息。 INFO：重要或者您感兴趣的信息。 WARN：系统可能出现潜在错误的信息。 ERROR：系统出现错误和异常的信息。 |
|  | 类日志等级 | 填写类日志名称和日志等级。 |
|  | 日志模板 | 支持系统模板和用户定义模板，默认值为系统模板default。 |

5. 单击**保存更改**。
在未保存前，单击**放弃更改**，将舍弃未保存的修改。
1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**配置管理**。
3. 在**作业默认配置**下，单击**批作业**。
4. 进行参数修改。
实时计算（流计算）

| 参数 |  | 说明 |
|---|---|---|
| 运行参数配置 | Flink重启策略配置 | 支持以下三种策略： Failure Rate：基于失败率重启。选择该选项后，您还需要填写检测 Failure Rate 的时间间隔、时间间隔内的最大失败次数和每次重启时间间隔。 Fixed Delay：固定间隔重启。选择该选项后，您还需要填写尝试重启的次数和每次重启时间间隔。 No Restarts：作业任务失败后不会重启。 |
|  | 尝试重启的次数 | Flink 在宣告作业失败之前重试执行的次数。 如果通过检查点激活，则使用 Integer.MAX VALUE。默认值为 _ 2147483647。 |
|  | 每次重启时间间隔 | 延迟重试意味着在执行失败后，重新执行不会立即开始，而只会在一定的延迟后开始。默认值为10秒。 |
| 其他配置 | / | 可以在此设置其他 Flink 配置。 例如： taskmanager.numberOfTaskSlots: 1 。 |

实时计算（流计算）

| 日志配置 | 根日志等级 | 日志级别从低到高顺序如下： i. TRACE：比DEBUG更细粒度的信息。 ii. DEBUG：系统运行状态的信息。 iii. INFO：重要或者您感兴趣的信息。 iv. WARN：系统可能出现潜在错误的信息。 v. ERROR：系统出现错误和异常的信息。 |
|---|---|---|
|  | 类日志等级 | 填写类日志名称和日志等级。 |
|  | 日志模板 | 日志模板，可以选择系统模板，也可以选择用户配置。 |

5. 单击**保存更改**。
在未保存前，单击**放弃更改**，将舍弃未保存的修改。

### 作业日志

#### 查看启动和运行日志

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
实时计算（流计算） ii. 在左侧导航栏选择**运维中心** > **作业运维**，单击目标作业名称，默认展开作业详情页面。
2. 在**作业日志**页签，单击左侧的**启动日志**，即可查看启动日志。

**查看运行日志**

**在作业日志页面查看运行日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开作业详情页面。
2. 在**作业日志**页面的**运行日志**页签，单击**作业**右侧的下拉框，选择正在运行作业。
3. 查看Job Manager和Task Managers日志。
查看Job Manager日志在**Job Manager**页签，单击**日志**。 查看Task Managers日志实时计算（流计算） a. 在**运行****Task Managers**页签，单击**Path, ID**。 b. 单击**日志**。

**在Flink UI页面查看运行日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开作业详情页面。
2. 在**状态总览**页签的**操作**行，单击**Flink UI**，默认进入**Apache Flink Dashboard**的**Overview**页面。

**说明**

作业状态为**运行中**才出现**Flink UI**入口。
3. 在左侧导航栏，单击**Task Managers**或**Job Manager**。
单击**Task Managers** 后，单击目标**Path, ID**，在**logs**页签查看作业Task Manager日志。 单击**Job Manager**后，在**Logs**页签，查看作业Job Manager日志。

#### 查看运行异常日志

在作业启动或者运行异常时，您可以查看运行异常日志进行问题排查。本文为您介绍如何查看Job Manager 异常、失效Task Managers日志和慢Checkpoint对应的Task Managers日志。

**背景信息**

| 类型 | 详情 |
|---|---|
| Job Manager异常 | 如果作业出现Failover，导致作业运行失败，则需要查看Job Manager异常。 说明如果Job Manager都没启动起来，不属于Job Manager异常，需要在启动日志中去查看。 |

实时计算（流计算）

| 失效Task Managers日志 | 运行状态为正常的作业，不会有失败TM。但是对于风险等级较高的作业，可能有失败的TM， 但TM又被拉起了，这时可以查看失败的TM归档日志去定位可能的原因。 说明只有开启了日志归档才能查看失效Task Managers日志，并且只能查看日志归档中配置的保留天数之内的失效Task Managers日志。 |
|---|---|
| 慢Checkpoint对应的Task Managers 日志 | 作业运行过程中，如果某个Checkpoint运行耗时较长，您需要查看其具体的原因，则可以查看其关联的TM的日志。 |

**前提条件**

作业实例为运行状态。

**注意事项**

支持日志分页，每页显示1 MB，大概会显示8000~9000行日志，基本可以帮您排查错误。如果在第一页还未定位到问题，请注意切换页码查看日志。

**查看Job Manager异常**

1. 进入**作业运维**页面。
ii. 在左侧导航栏单击**运维中心** > **作业运维**，展开**作业运维**页面。
2. 在**作业日志**页签，选择左侧的**异常信息**页签后，查看Job Manager异常信息。

**说明**

在**异常历史**中，您可以查看近7天内产生的异常信息，并过滤异常类型后查看历史异常。

**查看失效Task Managers日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开作业详情页面。
2. 在**作业日志**页签，选择**运行日志**后，选择正在运行的作业实例。
3. 单击**失效****Task Managers**页签，查看失效Task Managers日志。

**定位慢Checkpoint并查看对应Task Managers的日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开作业详情页面。
2. 查看慢Checkpoint日志信息。
i. 在**作业日志**页签，单击**Checkpoints**页签，单击**Checkpoints****历史**。 实时计算（流计算） ii. 查看**End to End Duration**列值，确认慢Checkpoint对应的ID。 iii. 单击慢Checkpoint对应的ID左侧的 ，确认慢Checkpoint对应的Operators节点。 iv. 单击Operators节点左侧的 ，展开查看每个Task的情况。 v. 单击慢Checkpoint对应的Task节点对应的**ID**。 实时计算（流计算） vi. 在跳转的页面**运行****Task Managers**页签，查看慢Checkpoint日志信息。

#### 查看历史作业实例日志

当Flink UI无法打开或需分析历史作业运行问题时，您可以查看历史作业实例日志定位问题。本文介绍如何

**背景信息**

如果出现以下情况，则您需要查看历史作业实例的日志： 您需要查看、搜索和分析历史作业实例的运行日志（系统默认保留最近5 MB大小的运行日志）。 您需要查看Job Manager日志定位问题。

**前提条件**

在**作业日志**页签查看历史作业实例日志，需要您在日志配置中已打开日志归档功能。默认已开启日志归档功能，归档日志有效期7天。

**注意事项**

当日志文件达到指定大小时，系统将默认自动归档日志，并定期清理超过归档有效期的日志文件。作业停止后，未清理的归档日志将被保留下来，不会自动进行清理。若作业被删除，则相应的日志也将随之删除。 日志配置中默认会保留2个文件，每个文件大小为5 MB，不建议您修改该值。 实时计算（流计算）

**说明**

图片上的文件个数不包括正在写的文件，即如果这里配置为1，则最多会保存2个文件，一个保存在内存中，一个保存在您的本地磁盘中。

**在作业日志界面查看**

1. 进入作业运维页面。
ii. 在左侧导航栏选择**运维中心** > **作业运维**，单击目标作业名称，默认展开作业详情页面。
2. 在**作业日志**页签，单击左侧**运行日志**。
3. 单击**作业**右侧的下拉框，选择历史运行作业。
4. 查看Job Manager和Task Managers日志。
在**Job Manager**或**Task Managers**页签，分别单击对应的日志名称，进行查看。

#### 修改运行作业日志级别

当INFO级别的日志无法满足您定位问题的需求时，您可以修改打印日志的级别为DEBUG。本文介绍如何动态修改日志级别及使用限制和注意事项。

**背景信息**

系统支持的日志级别从低到高的顺序与下面表格内容中的前后顺序一致。

| 级别 | 详情 |
|---|---|
| DEBUG | 系统运行状态的信息。 |
| INFO | 重要或者您感兴趣的信息。 |

**使用限制**

只支持设置为INFO或DEBUG，不支持设置为其他级别，以避免级别设置太高导致在日志中定位不到原因的问题。 实时计算（流计算） 支持修改整个JM的日志级别。 支持修改单个TM日志级别，不能一次性修改所有TM日志级别。如果需要修改所有TM日志级别，则需要您进行单独配置。

**注意事项**

日志级别修改为DEBUG后，会打印DEBUG、INFO、WARN、ERROR级别的日志。 日志级别修改为INFO后，只会打印INFO、WARN、ERROR级别的日志。 修改日志级别后，只会影响新输出的日志，之前已输出的日志不会受到影响。 DEBUG日志的开启会对作业性能造成少许影响。如果您没有定位问题的必要，建议将日志级别设置为 INFO。

**操作步骤**

1. 进入作业运维页面。
ii. 在左侧导航栏选择**运维中心** > **作业运维**，单击目标作业名称，默认展开作业详情页面。
2. 在**作业日志**页签，单击左侧**运行日志**，选择正在运行的作业实例。
3. 修改Job Manager或Task Managers日志级别。

**修改Job Manager日志级别**

a. 在**Job Manager**页签，单击**日志**。 b. 单击**编辑**。 c. 单击**确定**。 d. 在下拉框中选择目标日志级别。 e. 单击**确定**。

**修改Task Managers日志级别**

a. 在**运行****Task Managers**页签，单击**Path, ID**。 实时计算（流计算） b. 单击**日志**。 c. 单击**编辑**。 d. 单击**确定**。 e. 在下拉框中选择目标日志级别。 f. 修改日志级别后，单击**确定**。

#### 查看Flink审计事件

**背景信息**

云盾安全审计可以帮助您监控并记录阿里云账号的活动，您可以将这些行为事件下载或保存到日志服务 SLS，然后进行行为分析、安全分析、资源变更行为追踪和行为合规性审计等操作。

**操作步骤**

1. 登录飞天基础运维控制台。
i. 打开浏览器。 ii. 登录Apsara Uni-manager运维控制台。 在地址栏中，输入Apsara Uni-manager运维控制台的访问地址后按回车键，输入正确的用户名和密码后，单击**登录**。

**说明**

登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。
2. 在顶部菜单栏，鼠标悬浮至**安全管理**，选择**安全审计** > **云盾安全审计**，系统默认进入**安全审计**页面。
3. 在**安全审计**页面，单击**原始日志**页签。
4. 选择**审计类型**为**云产品**，**审计对象**为**vvp****操作日志**（或者**flink****存算分离版操作日志**），设置**起始时间**后
单击**查询**。 实时计算（流计算）

## 常见问题

问题描述：为什么进入审计页面后，原始日志中没有数据？ 问题原因：存在以下两种可能情况： 用户在查询的时间段内未曾操作vvp平台。 用户确实进行了vvp平台的操作，此时需要对日志上报的成功与否进行排查。请联系阿里云技术支持获取排查方案。 问题描述：为什么进入审计页面后，有原始日志，但是没有审计数据？ 问题原因：存在以下两种可能情况： 在审计查询的时间段内，用户未进行高危操作。 用户确实进行了高危操作，但云盾单日日志审计已达到上限，此时需要联系云盾相关同事以调高单日审计上限。 实时计算（流计算）

## 数据管理

数据管理提供Catalog列表功能，支持创建、查看和删除Hologres、MySQL、Apache Paimon等 Catalog，方便您在作业开发中直接引用元数据。

### 管理自定义函数（UDF）

在SQL作业中使用自定义函数，需要先注册自定义函数（UDF）。本文为您介绍如何注册、更新和删除自定义函数。

**注意事项**

为了避免JAR包依赖冲突，您需要注意以下几点： Flink镜像的版本请与Pom依赖中的Flink版本保持一致。 请不要上传Runtime层的JAR包，即在依赖中添加 `<scope>provided</scope>` 。 其他第三方依赖请采用Shade方式打包，Shade打包详情参见Apache Maven Shade Plugin。

**注册自定义函数**

如果您的SQL需要使用自定义函数，您需要先注册您的自定义函数，才能在SQL中使用。
1. 登录实时计算开发控制台。
2. 在左侧导航栏上，单击**SQL** **开发**。
3. 在**函数**页签，首次注册直接点击**注册****UDF**，也可点击右上角
图标。
4. 上传自定义函数JAR文件，单击**确认**。
实时计算（流计算） 您可以通过以下任何一种方式上传自定义函数JAR文件：
**上传文件**：单击**选择文件**项右侧的**选择文件**后，选择您的目标自定义函数Artifact文件。如果有依赖文
件，单击**依赖文件**项右侧的**选择文件**，选择您的目标自定义函数Artifact所依赖的文件。
**外部****URL**：输入外部URL地址。
Flink开发控制台会解析您自定义函数JAR文件中是否使用了Flink UDF、UDAF和UDTF接口的类，并自动提取类名，填充到Function Name字段中。 对于Java类型的自定义函数，其依赖可以打包到自定义函数JAR包中，也可以通过依赖文件项进行上传；对于Python类型的自定义函数，推荐通过单独上传依赖文件方式上传依赖。 在自定义函数Artifact文件或者其依赖文件比较大时，推荐通过外部URL的方式进行上传。需要注意的是，如果外部URL是OSS Bucket地址，其依赖文件必须位于 `sql-`

```
artifacts/namespaces/{namespace} 目录下。
```

**说明**

Bucket目录至少需要公共读权限，URL路径只支持HTTP协议，且不可带编码字符。
5. 在**管理** **Functions**弹框中，确认函数信息，单击**创建** **Function**。
注册成功后，弹框会显示当前**已注册的** **Function**的信息。此时，您可以按需移除不需要的函数。 实时计算（流计算） 移除后，界面显示如下。确认函数信息无误后，关掉弹框。
6. 在SQL编辑器页面左侧的**函数**列表中，您可以看到所有注册成功的自定义函数。
如果您需要对已注册的自定义函数JAR文件进行函数添加或者移除，您可以按照以下步骤管理自定义函数 JAR文件。
1. 在**函数**页签中，鼠标悬停在目标自定义函数名称上，单击
图标。
2. 添加或者移除目标函数。
实时计算（流计算）

**更新自定义函数**

如果您的自定义函数JAR文件中，新增了自定义函数或已注册了自定义函数的代码变更，您可以按照以下步骤更新自定义函数JAR文件。
1. 在**函数**页签中，鼠标悬停在目标自定义函数名称上，单击
图标。
2. 管理自定义函数。
您可以通过以下任何一种方式上传自定义函数JAR文件：
**上传文件**：单击**选择文件**项右侧的**选择文件**后，选择您的目标自定义函数Artifact文件。如果有依赖文
件，单击**依赖文件**项右侧的**选择文件**，选择您的目标自定义函数 Artifact所依赖的文件。
**外部****URL**：输入外部URL地址。

**重要**

您上传的新自定义函数JAR文件中，必须包含当前已经注册自定义函数的所有类，不能出现某个已注册自定义函数的类消失的情况。 只有重启作业或提交新作业时，才会使用新自定义函数JAR文件中的代码。如果引用该自定义函数JAR的作业正在运行，则依然会使用旧自定义函数JAR文件。
3. 单击**修改**。

**删除自定义函数**

如果您的自定义函数JAR文件不再使用，您可以按照以下步骤删除自定义函数。
1. 在左侧导航栏上，单击**SQL** **开发**。
2. 在**函数**页签中，鼠标悬停在目标自定义函数名称上，单击
图标。

**说明**

在删除自定义函数JAR文件前，请确定其注册的自定义函数没有被作业或SQL文件引用。 实时计算（流计算）
3. 选中**删除关联的文件**。
如果您要删除该自定义函数JAR文件，则需要删除该自定义函数JAR中所有注册的自定义函数，避免有脏数据残留。
4. 单击**确定**。

### 管理Paimon Catalog

配置Paimon Catalog后，您可以通过实时计算Flink版直接访问阿里云对象存储OSS中的Paimon表。本文为您介绍如何在实时计算开发控制台创建、查看与删除Paimon Catalog，以及管理Paimon数据库和 Paimon表。

**创建Paimon Filesystem Catalog**

1. 进入数据管理页面。
ii. 在左侧导航栏，单击**数据管理**，默认展开**Catalog****列表**页面。
2. 单击**创建****Catalog**，选择**Apache Paimon**，单击**下一步**。
3. 填写参数配置信息。

| 配置项 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| catalog name | Paimon Catalog名称。 | 是 | 请填写为自定义的英文名。 |
| metastore | 数据存储类型。 | 是 | 参数取值选择为Filesystem。 |
| warehouse | OSS服务中所指定的数仓目录。 | 是 | 格式为oss://<bucket>/<object>。其中： bucket：表示您创建的OSS Bucket名称。 object：表示您存放数据的路径。 |
| fs.oss.endpoint | OSS服务的连接地址。 | 是 | 例如oss-cn-hangzhou.aliyuncs.com。 |
| fs.oss.accessKeyI d | 访问OSS服务所需的 Access Key ID。 | 是 | 无 |
| fs.oss.accessKeyS ecret | 访问OSS服务所需的 Access Key Secret。 | 是 |  |
| fs.oss.signer.versi on | OSS签名版本。 | 否 | 无 |

4. 单击**确定**。

**管理Paimon数据库**

在SQL开发文本编辑区域输入如下命令，选中代码后单击**运行**。 实时计算（流计算）

**创建数据库**

创建Paimon Catalog后，Catalog中会自动创建名为 `default` 的数据库。 `--my-catalog`需要替换为您创建的`Paimon Catalog`名称。

```
USE CATALOG `my-catalog`;
```

`--my_db`需要替换为自定义的`database`英文名称。

```
CREATE DATABASE `my_db`;
```

**删除数据库**

**重要**

无法删除DLF、MaxCompute和Sync类型Catalog下的default数据库，允许删除Filesystem类型 Catalog下的default数据库。 `--my-catalog`需要替换为您创建的`Paimon Catalog`名称。

```
USE CATALOG `my-catalog`;
```

`--my_db`需要替换为您想要删除的数据库名称。 DROP DATABASE `my_db`; --只需要删除内部没有任何表的数据库。 DROP DATABASE `my_db` CASCADE; --删除数据库且同时删除数据库下的所有表。

**查看或删除Paimon Catalog**

在**数据管理**页面，查看或删除Paimon Catalog。 查看：在**Catalog****列表**页面，查看**Catalog****名称**和**类型**。如果您需要查看Catalog下的数据库和表，请单击**查看**。 删除：在**Catalog****列表**页面，单击目标Catalog名称对应**操作**列的**删除**。 您也可以在SQL开发文本编辑区域输入 DROP CATALOG <catalog name>; ，选中代码后单击**运行**。

**说明**

删除Paimon Catalog只会删除Flink项目空间数据管理中的记录，不会影响Paimon表的数据文件。 删除Catalog后，只需要重新执行创建Paimon Catalog，即可重新使用Catalog中的Paimon表。

### 管理Hologres Catalog

配置Hologres Catalog后，您可以在Flink全托管控制台直接读取Hologres元数据，不用再手动注册 Hologres表，可以提高作业开发的效率且保证数据的正确性。本文为您介绍如何在Flink全托管模式下配置、查看及删除Hologres Catalog。

**背景信息**

Catalog提供了元数据信息，例如数据库、表、分区、视图以及数据库或其他外部系统中存储的函数和信息。详情请参见Catalogs。 创建Hologres Catalog 查看Hologres Catalog 使用Hologres Catalog 删除Hologres Catalog 实时计算（流计算）

**使用限制**

仅Flink 1.13及以上版本支持配置Hologres Catalog。 不支持修改Catalog DDL。

**创建Hologres Catalog**

**UI方式**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**数据管理**，默认展开**Catalog****列表**页面。
3. 单击**创建****Catalog**，选择**Hologres**，单击**下一步**。
4. 填写参数配置信息。

| 参数 | 说明 | 是否必填 |
|---|---|---|
| catalogname | 自定义Hologres Catalog名称。 仅支持小写字母a-z和数字0-9，不含大写字母、中划线（-）、下划线（ ）等特殊字符。 _ | 是 |
| endpoint | Hologres的连接地址，<host>:<port>。 | 是 |
| username | 与dbname相匹配的用户名，为Hologres所在组织的AccessKey ID。 | 是 |
| password | 与dbname相匹配的密码，为Hologres所在组织的 AccessKey Secret。 | 是 |
| dbname | Hologres的数据库名称。 在目标Hologres实例中应完成数据库的创建，否则创建Catalog会报错。 | 是 |

5. 单击**确定**。
6. 单击
图标，刷新查看新建的Hologres Catalog。

**SQL方式**

1. 新建SQL流作业。
ii. 在左侧导航栏单击**数据开发** **> ETL**，默认选择**作业草稿**页签。 实时计算（流计算） iii. 单击后，单击**新建流作业**。 iv. 在**新建作业草稿**对话框中填写**文件名称**，选择**引擎版本**。 v. 单击**创建**。
2. 在文本编辑区域，输入配置Hologres Catalog的命令。

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
| <catalogname> | 自定义Hologres Catalog名称。仅支持小写字母a~z 和数字0~9，不含大写字母、短划线（-）、下划线 （ ）等特殊字符。 _ | 是 |
| type | 类型，固定值为hologres。 | 是 |
| endpoint | Hologres的连接地址，<host>:<port>。 | 是 |
| username | 与dbname相匹配的用户名，为Hologres所在组织的 AccessKey ID。 | 是 |
| password | 与dbname相匹配的密码，为Hologres所在组织的 AccessKey Secret。 | 是 |
| dbname | 您访问Hologres的默认数据库名称。 | 是 |

3. 单击**部署**。
执行完会提示Query has been executed。如果您需要删除Hologres Catalog，详情请参见删除 Hologres Catalog。 实时计算（流计算）
4. 在左侧单击**元数据**页签，单击
图标，刷新查看新建的Hologres Catalog。

**查看Hologres Catalog**

Hologres Catalog配置成功后，您可以通过以下步骤查看Hologres元数据。
1. 在左侧导航栏，单击**数据管理**，默认展开**Catalog****列表**页面。
2. 在顶部菜单栏下拉框中，切换到目标Hologres Catalog名称，本文以holo为例。
3. 查看不同Hologres Catalog下的数据库、表和函数信息。

**说明**

如果Schema为public时，则表名称前面就省略了Schema的前缀，即直接显示tableName。

**使用Hologres Catalog**

**创建Hologres表**

**UI方式**

1. 进入数据管理页面。
实时计算（流计算） ii. 在左侧导航栏，单击**数据管理**，默认展开**Catalog****列表**页面。
2. 进入目标数据库。
i. 单击目标Catalog名称对应**操作**列的**查看**。 ii. 单击目标数据库名称对应**操作**列的**查看**。
3. 创建Hologres表。
i. 单击**创建表**。 ii. 在**使用内置连接器连接**页签，选择实时数仓Hologres连接器，单击**下一步**。 iii. 填写建表语句并配置相关参数信息。代码示例如下。

```
CREATE TABLE `${catalog_name}`.`${db_name}`.`${table_name}` (
 ...
) WITH (
 'connector' = 'hologres'
);
```

iv. 单击**确定**。

**SQL方式**

使用 `USE CATALOG HoloName` 命令直接引用Hologres数据服务。

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

在已注册的Hologres数据服务下创建表时，WITH参数中connector为必填参数，且取值为 hologres。可省略endpoint等其他参数。 目前不支持直接在Hologres表中添加或修改WITH参数，可以通过SQL hints的方式在INSERT 语句中添加或修改WITH参数。

**从Hologres表中读取数据**

```
INSERT INTO ${other_sink_table} SELECT ... FROM `${catalog_name}`.`${db_name}`.`${schema_name.table_name}`
```

实时计算（流计算）

**写入结果数据至Hologres表**

```
INSERT INTO `${catalog_name}`.`${db_name}`.`${schema_name.table_name}` SELECT ... FROM ${other_source_table}
```

**说明**

如果Schema为public时，在填写**${schema_name.table_name}**时，可以省略模式名称的前缀，直接填写tableName，即${table_name}。

**删除Hologres Catalog**

1. 新建SQL流作业。
ii. 在左侧导航栏单击**数据开发** **> ETL**，默认选择**作业草稿**页签。 iii. 单击后，单击**新建流作业**。 iv. 在**新建作业草稿**对话框中填写**文件名称**，选择**引擎版本**。 v. 单击**创建**。
2. 在文本编辑区域，输入以下命令。

```
DROP CATALOG ${catalog_name}
```

其中，catalog_name为您要删除的在Flink全托管开发控制台上显示的Hologres Catalog名称。

**说明**

删除Hologres Catalog不会影响已运行的作业，但对未上线或者需要暂停恢复的作业均会产生影响，请您谨慎操作。
3. 单击**部署**。
4. 在左侧，单击**元数据**页签。
5. 单击
图标，刷新查看新建的Hologres Catalog是否已被删除。 实时计算（流计算） 实时计算（流计算） 义连接器

## 管理自定义连接器

本文为您介绍如何管理Flink自定义连接器，包括创建、更新和删除。

**背景信息**

在使用Flink SQL开发作业时，需要使用SQL 连接器连接您的源表、结果表和维表。Flink支持云上常用的多种类型的连接器，但相对于目前大数据常用的技术栈而言，仍然只是较少的一部分，为了支持您可以使用更多类型的连接器，我们支持您自定义连接器后上传使用。在使用过程中，您需要注意以下事项： 您需要根据社区定义的连接器标准开发您自定义的连接器，才能被Flink正确识别并使用，因此您需要明确的Connector Meta文件和申明Factory类。自定义Connector开发详情请参见User-defined Sources & Sinks。 同种类型的连接器仅可以上传一次。 为了避免JAR包依赖冲突，您需要注意以下几点： Flink镜像和Pom依赖的Flink版本请保持一致。 请不要上传Runtime层的JAR包，即在依赖中添加 `<scope>provided</scope>` 。 其他第三方依赖请采用Shade方式打包，Shade打包详情参见Apache Maven Shade Plugin。

**创建自定义连接器**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**连接器**。
3. 在**连接器**页面，单击**自定义连接器**页签。
4. 单击**创建自定义连接器**，在**创建自定义连接器**对话框，进行以下操作。
i. **上传****JAR**包选择待上传的JAR文件（本文以lindorm-connector-1.0-SNAPSHOT.jar为例），并单击**下一步**。 ii. **查看连接器** 在**创建自定义连接器**界面，按需配置相关信息。 实时计算（流计算） 义连接器

| 参数 | 说明 |
|---|---|
| Connector | 连接器的名称。 |
| Lookup | 能否作为lookup表，按需设置即可。 |
| Formats | 左键单击下拉框，选择支持的Format。 |
| Properties | 按需设置连接器的属性。 |

5. 单击**完成**。

**更新自定义连接器**

1. 在自定义连接器列表中，找到目标连接器，单击右侧的**编辑**。
实时计算（流计算） 义连接器
2. 可按需重新上传JAR包，也可以直接选择**跳过**，修改已有连接器的属性。
3. 单击**完成**。

**删除自定义连接器**

如果您的自定义Connectors不再使用，您可以按照以下步骤删除自定义Connectors。
1. 在自定义连接器列表中，找到目标连接器，单击右侧的**删除**。
2. 在删除连接器对话框中，单击**确定**。
实时计算（流计算）

## 文件管理

Flink支持通过资源上传功能存放作业运行时需要的文件或者运行过程中产生的数据文件（例如作业系统检查点、作业快照、日志和JAR包等）。本文为您介绍资源的上传、下载、删除及路径复制等资源管理的相关操作。

**操作步骤**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**文件管理**。
3. 进行资源管理操作。

|  | 操作 | 说明 |  |
|---|---|---|---|
|  | 上传资源 | 单击上传资源后选择本地文件上传资源，或者直接将待上传文件拖拽到资源列表区域。 上传后，文件路径格式为 oss://flink-fullymanaged-<工作空间 ID>/artifacts/namespaces/<项目空间名称>/<文件名> 。 |  |
|  |  |  | oss://flink-fullymanaged-<工作空间 |
|  |  | ID>/artifacts/namespaces/<项目空间名称>/<文件名> |  |
|  | 下载资源 | 单击操作列的下载，可以将文件下载到本地进行查看。 |  |
|  | 删除资源 | 单击操作列的删除，可以将上传的文件直接删除。 |  |
|  | 复制路径 | 鼠标悬停在目标资源名称处，右侧出现复制图标，单击图标进行复制。 |  |

实时计算（流计算）

## 安全服务

安全服务包括访问安全、变量管理和权限管理功能。您可以在访问安全中配置Hive Kerberos，使用变量管理进行密钥托管，通过权限管理配置角色和成员信息，确保数据与操作安全。

### 访问安全

Kerberos 是一种网络身份认证协议，用于保障通信安全。若您的 Flink 作业需要访问启用了 Kerberos 认证的外部服务（如 HBase、Kafka 等），请先在 Flink 全托管控制台上注册对应的 Kerberos 集群，然后在作业中配置该 Kerberos 集群信息，即可实现安全访问，防止未授权操作。

**功能介绍**

本功能解决了 Flink 存算分离版访问外部 Kerberos 认证服务（如自建 Kafka、HBase 等）时的身份认证问题。您可在 Flink 全托管控制台预先注册 Kerberos 集群信息（包括 krb5.conf、Principal 及 Keytab 文件），并在作业配置中引用该集群。Flink 运行时将基于此完成身份认证，确保作业在整个运行期间具备有效访问权限，认证凭据由平台统一管理，无需在代码中硬编码，满足企业级安全与合规要求。

**使用限制**

仅 VVR 11.5.0 引擎支持 Kerberos 认证。 云消息队列 Kafka 版不支持 Kerberos 认证，Flink 作业仅可访问自建 Kafka 集群（需已启用 Kerberos）。 Flink 作业仅可访问自建 HBase 集群（需已启用 Kerberos）。

## 准备工作

获取 Kerberos 客户端的配置文件 `krb5.conf` 。

**说明**

该文件通常位于 KDC 服务器的 `/etc/krb5.conf` 路径下，请根据实际路径获取。 联系 Kerberos 管理员获取 Flink 客户端 Principal（ Principal 和 Keytab 文件）。

|  | 说明 Principal名称通常格式为 flink@YOUR-REALM.COM ， flink 是自定义的用户名， YOUR- REALM.COM 是集群的 Kerberos Realm，注意大写。 |  |  |
|---|---|---|---|
|  |  | YOUR- |  |
|  | REALM.COM |  |  |

**在作业中开启Kerberos认证**

1. 创建 Kerberos。
ii. 在左侧导航栏单击**安全服务** > **访问安全**。 实时计算（流计算） iii. 单击**新增** **Kerberos**。配置相关参数：

| 参数 | 说明 |
|---|---|
| Kerberos 集群名称 | 集群名称，在当前 Namespace 下 Kerberos 集群名称唯一，且添加完成后不可修改。 |
| Kerberos Krb5.conf | 上传准备工作已获取的 Kerberos 客户端的配置文件 krb5.conf 。 |
| Kerberos 用户信息 | 填写准备工作已获取的 Flink 客户端 Principal（Principal和 Keytab文件）。 |

iv. 单击**确定**。
2. 在左侧导航栏单击**数据开发** **> ETL**。
3. 在作业草稿中单击
，选择**新建流作业**，在弹出的对话框中，设置**引擎版本**为 `vvr-11.5.0-flink-` `1.2.0` 。
4. 单击**创建**。
5. 配置完作业相关配置后，单击右侧更多配置，设置如下参数开启Kerberos认证。

| 参数 | 说明 |
|---|---|
| 附加依赖文件 | 上传准备工作已获取 krb5.conf 文件和Keytab文件。 |
| Kerberos 认证 | 开启Kerberos 认证开关。 |
| Kerberos 集群 | 开启Kerberos 认证开关后需要配置，下拉选择创建Kerberos集群步骤创建的集群名称和配置的 Principal。 |
| Principal |  |

**后续步骤**

作业配置完成后，按需进行深度检查、调试和部署，详情请参见作业开发。

### 变量管理

使用变量可以避免明文AccessKey、密码等信息带来的安全风险，通过复用可以避免重复编写相同的代码或值，易于配置管理。Flink存算分离版支持在JAR或Python作业密钥托管场景中使用。本文介绍如何创建变量并使用变量。

**新增变量**

1. 登录实时计算开发控制台。
实时计算（流计算）
2. 单击左侧导航栏的**安全服务** > **变量管理**，单击**新增变量**。

| 参数 | 说明 |
|---|---|
| 类型（明文/密文） | 创建后不支持修改类型。 明文：在变量管理页面可以直接查看变量值。 密文：无法查看变量值。 |
| 变量名 | 变量名需在同一个项目空间下保持唯一，创建后不支持修改。 说明请避免使用关键字作为变量名。 |
| 变量值 | 变量值对字母大小写敏感，填写时请注意字母大小写。创建后支持修改变量值。 说明不支持为一个变量名配置多个值。 |

3. 单击**确定**。
如果需要删除已创建的密钥，单击**操作**列的**删除**。

**使用变量**

Flink存算分离版支持JAR和Python的密钥托管，支持JAR和Python作业中Main函数入参使用变量。 增加变量后，您可以通过 ${secret_values.变量名} 格式使用，使用时仅需将其中的变量名进行修改，其他部分保留不变，具体变量使用示例如下。

**JAR作业密钥托管**

1. 登录实时计算开发控制台。
2. 单击左侧导航栏的**运维中心** > **作业运维**，单击**部署作业** **> JAR****作业**。
3. 在**Entry Point Main Arguments**参数位置输入入参变量名，使用格式为 `--`代码中的变量名
${secret_values.变量管理中的变量名} 。示例如下。 实时计算（流计算）
4. 其他部署参数配置详情请参见作业部署。
5. 单击**部署**。

**Python作业密钥托管**

1. 登录实时计算开发控制台。
2. 单击左侧导航栏的**运维中心** > **作业运维**，单击**部署作业** **> Python****作业**。
3. 在**Entry Point Main Arguments**参数位置输入入参变量名，使用格式为 `--`代码中的变量名
${secret_values.变量管理中的变量名} 。示例如下。 实时计算（流计算）
4. 其他部署参数配置详情请参见作业部署。
5. 单击**部署**。

### 权限管理

权限管理提供成员管理和角色管理功能，您可以在成员管理中添加、编辑和删除项目空间成员，在角色管理中查看和维护角色权限。

#### 授权须知

本文介绍授权操作前需要了解的关键信息，说明权限分类以及权限与控制台功能的关系与区别。 随着产品演进和现场计量的需求，Flink项目空间（Namespace）资源的管理由大数据管家（ABM）迁移至Apsara Uni-manager运营控制台，可以更贴合用户在Apsara Uni-manager运营控制台上创建资源的行为。 Flink权限分为资源管理和业务角色两部分：

| 权限分类 | 说明 |
|---|---|
| 资源管理 | 适用于实时计算Flink版管理控制台。 授予对工作空间、项目空间资源的管理能力，包括创建、修改、删除以及查询四类权限。拥有该权限的账号可以在实时计算Flink版管理控制台上管理工作空间及项目空间资源。 |
| 业务角色 | 适用于实时计算开发控制台。 针对目标项目空间内作业的权限，系统内置角色包括owner、editor和view（只读）三类权限。 在实际业务的操作中，已授权业务角色的用户可以通过实时计算Flink版管理控制台登录实时计算开发控制台，进行作业开发、运维管理以及人员管理等操作。 |

#### 管理控制台授权

用户创建及管理工作空间、项目空间资源需要配置对应空间的访问权限。本文介绍在实时计算Flink版管理控制台上创建目标用户并配置工作空间及项目空间访问权限的操作。

**操作步骤**

1. 创建目标组织。
详细操作，请参见《统一云管平台用户指南》中**企业中心** > **资源管理** > **组织管理** > **创建组织**。
2. 创建目标资源集（创建一个组织，系统会默认为该组织创建一个资源集，可按需创建）。
详细操作，请参见《统一云管平台用户指南》中**企业中心** > **资源管理** > **资源集管理** > **创建资源集**。
3. 创建目标用户。
详细操作，请参见《统一云管平台用户指南》中**企业中心** > **人员管理** > **用户管理** > **创建用户**，根据角色权限范围添加对应的角色。 实时计算（流计算）

**说明**

推荐选择资源集管理员或组织管理员预置角色。该预置角色开放了对工作空间与项目空间创建、修改、删除与查看的权限。 选择资源使用人预置角色，用户可查看、修改工作空间以及项目空间。 查看角色权限或自定义角色，请参见《统一云管平台用户指南》中**企业中心** > **权限管理** > **角色授** 权。
4. 添加目标用户至目标资源集中。
详细操作，请参见《统一云管平台用户指南》中**企业中心** > **资源管理** > **资源集管理** > **管理资源集成** 员，将目标用户添加至对应的资源集中。
5. 授权目标用户其他角色（可选）。
详细操作，请参见《统一云管平台用户指南》中**企业中心** > **人员管理** > **用户管理** > **用户角色授权**，修改或添加目标用户对工作空间及项目空间资源的管理权限。

**后续操作**

切换owner角色在开发控制台授权，为目标用户分配业务角色后，可通过实时计算Flink版管理控制台访问实时计算开发控制台。

#### 开发控制台授权

当多个用户需要共同使用Flink中的某项目空间，并对作业开发、运维等操作进行权限区分时，可以通过角色管理和成员管理在开发控制台完成精细化授权。本文介绍授权场景、角色类型、自定义角色以及为成员绑定角色的操作方法。

**授权场景**

场景一：无法访问当前项目空间。 说明您当前无该目空间权限。请联系该项目空间具有owner角色的成员或拥有成员管理权限的用户，按照为您分配View及以上角色。授权完成后，请重新进入或刷新页面即可访问。 场景二：无法使用某个具体的功能或操作。 说明当前账号无对应操作权限。请联系具有owner角色的成员或拥有角色管理权限用户，根据您的操作需求重新修改自定义角色的权限，以保证您能够执行相关操作。

**角色类型**

角色是多种权限策略的集合。实时计算开发控制台中的角色分为系统角色和自定义角色两种类型，具体差异如下表所示。

| 角色类型 | 角色说明 | 注意事项 |
|---|---|---|
| 系统角色 | Flink系统内置角色，具有owner、editor、 viewer三种系统角色。不同系统角色支持的权限差异请参见细粒度权限列表。 | 不支持修改系统角色的权限以及删除系统角色。 |
| 自定义角色 | 当系统角色无法满足更细粒度的授权需求时， 您可以创建自定义角色。支持在viewer或 editor角色权限基础上快速扩展和添加所需权限。 | 自定义权限需包含并高于viewer角色的权限。 仅owner角色或具有角色管理权限的用户可以创建、编辑、删除自定义角色。 单个项目空间最多支持创建10个自定义角色。 |

实时计算（流计算）

**授权操作**

**步骤一：（可选）创建自定义角色**

根据实际需求创建自定义角色权限。如需直接使用系统默认角色，可跳过此步骤。
1. 登录实时计算开发控制台。

**说明**

使用具有owner角色的成员或具有角色管理权限的成员账号登录。
2. 单击左侧导航栏的**安全服务** > **权限管理**，单击**角色管理**页签。
3. 单击**添加角色**，填写相关信息。

| 参数 | 说明 |
|---|---|
| 角色名称 | 自定义角色名称。字母开头，仅支持数字、字母和短横线（-），不超过64个字符。 |
| 角色备注 | 描述角色，用于角色的信息补充或说明，帮助管理员或其他成员理解角色的用途、权限范围等。不超过256个字符。 |
| 角色权限 | 为了确保权限的完整性，部分权限点包含其他必要的依赖权限点，系统将自动为您默认勾选，具体权限依赖请参见细粒度权限列表。 |

4. 单击**确定**，即可查看、编辑和删除已添加的自定义角色。
**查看权限：**查看该角色具有哪些权限。
**查看成员：**查看该角色都绑定了哪些成员。
**编辑权限：**具有编辑角色权限的成员可以根据需要添加或移除权限。
**删除**：删除前考虑安全风险您需要将该角色下所有绑定的成员删除或更改为其他角色。该角色无绑定成
员后，具有删除角色权限的成员才可以删除该自定义角色。

**步骤二：为成员绑定目标角色**

为成员绑定目标角色，即授权，确保其拥有必要的权限。
1. 登录实时计算开发控制台。

**说明**

使用具有owner角色的成员或具有角色管理权限的成员账号登录。 owner角色可以为同组织下的子账号授予业务的访问权限（editor或view）。不支持跨一级组织用户授权，即使授权成功，该用户登录后，列表也不展示相关内容。 实时计算（流计算）
2. 在页面顶部，选择目标项目空间名称。
3. 单击左侧导航栏的**安全服务** > **权限管理**，单击**成员管理**页签。
4. 单击**添加成员**，添加成员并为成员选择**角色**。
参数说明：
**成员信息**：您可以在Apsara Uni-manager运营控制台系统界面右上角，单击当前登录用户的头像，
查看**UID**信息。

**重要**

已添加的成员不允许重复添加。
**角色**：支持选择系统角色和自定义角色。您可以通过将鼠标悬停在目标角色上方的方式查看角色描述。
5. 单击**确定**。

**细粒度权限列表**

| 一级权限 | 二级权限 | owner | editor | viewer |
|---|---|---|---|---|
| ETL/数据摄入 | 开发SQL/YAML作业草稿（创建、编辑） | √ | √ |  |
|  | 调试SQL作业草稿 | √ | √ |  |
|  | 删除SQL/YAML作业草稿 | √ | √ |  |
|  | 部署SQL/YAML作业草稿 | √ | √ |  |
|  | 深度检查 SQL/YAML作业草稿 | √ | √ |  |
| > 文档版本：2026073 | 0 11 |  |  |  |

实时计算（流计算）

|  | 查看SQL/YAML作业草稿列表 | √ | √ | √ |
|---|---|---|---|---|
|  | 部署JAR、 PYTHON作业 | √ | √ |  |
| 作业运维 |  |  |  |  |
|  | 删除运维部署作业 | √ | √ |  |
|  | 查看运维部署作业列表 | √ | √ | √ |
|  | 更新运维部署作业配置 | √ | √ |  |
|  | 启动/停止作业实例 | √ | √ |  |
| 数据管理 | 创建物化表 | √ | √ |  |
|  | 删除物化表 | √ | √ |  |
|  | 查看物化表 | √ | √ | √ |
|  | 编辑物化表 | √ | √ |  |
| 文件管理 | 删除资源 | √ | √ |  |
|  | 下载资源 | √ | √ |  |
|  | 查看资源列表 | √ | √ | √ |
|  | 上传资源 | √ | √ |  |
| Session管理 | 创建Session集群 | √ | √ |  |
|  | 删除Session集群 | √ | √ |  |
|  | 查看Session集群 | √ | √ | √ |
|  | 更新Session集群配置 | √ | √ |  |
| 20 | > 文档版本：2026073 |  |  |  |

实时计算（流计算）

|  | 启动/停止Session 集群 | √ | √ |  |
|---|---|---|---|---|
| 安全中心 | 创建角色 | √ |  |  |
|  | 创建变量 | √ | √ |  |
|  | 创建成员 | √ |  |  |
|  | 删除角色 | √ |  |  |
|  | 删除变量 | √ | √ |  |
|  | 删除成员 | √ |  |  |
|  | 查看角色列表 | √ | √ | √ |
|  | 查看变量列表 | √ | √ | √ |
|  | 查看成员列表 | √ | √ | √ |
|  | 编辑角色 | √ |  |  |
|  | 编辑成员 | √ |  |  |
| 配置管理 | 查看作业模板 | √ | √ | √ |
|  | 编辑作业模板 | √ | √ |  |

### 配置外部存储IP

默认情况下，所有作业的出向流量被禁止，您需要添加IP白名单来允许访问。本文介绍如何配置外部存储 IP，以开放作业的出向流量。

**背景信息**

为了解决计算逃逸安全漏洞问题，平台采用了开启NetworkPolicy功能。该功能默认禁止所有作业的出向流 NetworkPolicy功能的默认规则如下： 默认禁止所有出向的访问。 允许同NameSpace内的Pod间互相访问。 实时计算（流计算） 允许访问Ververica NameSpace下的HDFS。 允许访问APIServer。 允许访问CoreDNS。 允许访问CMS地址，用于指标数据上报。

**注意事项**

低版本升级到3.18.1及以上版本或者3.18.1及以上版本全新部署场景下，所有NameSpace默认开启

**使用限制**

创建完Namespace后可以在Namespace列表页面看到**配置外部存储****IP**按钮。该按钮的权限同**修改****CU**
**数量**按钮，即都要Namespace的编辑权限才能看到，否则按钮不可见。
添加的白名单IP或网段不得与黑名单网段存在交集，否则将提示错误。

**操作步骤**

1. 登录实时计算Flink版管理控制台。
2. 在**Workspace****列表**页面，单击目标NameSpace**操作**列下的**配置外部存储****IP**。
3. 单击**+IP****地址**，输入IP信息后单击**确认**。
IP地址为存储域名对应的VIP，支持添加单个IP或者Classless Inter-Domain Routing（CIDR）格式的网段，例如： `192.168.0.1` 、 `192.168.0.1/24` 。 如果格式错误会对应报错：
4. 单击**确认**。
实时计算（流计算）

## 作业迁移

本文介绍如何将Flink企业版项目空间的作业迁移到Flink存算分离版项目空间中。

**前提条件**

请确认您登录的企业版账号下已开通存算迁移版Flink集群，并创建了对应的工作空间和项目空间。 当前账号已具备迁移权限。若无迁移权限，需由项目空间所在组织在配置页面为该账号添加 AliyunStreamTransferRole策略。

**注意事项**

项目空间中的资源无需手动迁移。只需创建迁移任务并选择相关作业，单击了**开始迁移**，系统便会自动将该项目空间下的所有资源迁移到目标项目空间，建议您迁移到同一个项目空间的作业时使用同一个迁移任务。 迁移作业前务必使用**停止前创建一次快照**的方式来停止作业。否则，Flink系统在检测到有正在运行的作业时，会提示您选择取消迁移任务或是强制迁移。 不支持迁移Session集群，Session集群上运行的作业如果要迁移会被迁移成Per-Job类型的作业。 同一个任务可以多次运行，已经成功的迁移资源不会再进行迁移。

**操作步骤**

1. 登录Flink企业版实时计算开发控制台。
2. 在**系统管理** > **作业迁移**页面，单击**创建迁移任务**。
3. 填写迁移任务信息后，单击**确认**。

| 配置项 | 说明 |
|---|---|

实时计算（流计算）

| 迁移任务名称 | 自定义迁移任务名称。 |
|---|---|
| 目标工作空间 | 选择Flink存算分离版的工作空间。 |
| 目标项目空间 | 选择Flink存算分离版的项目空间。 |

4. 单击**操作**列的**添加**/**查看迁移**资源。
5. 选择迁移的作业。
i. 在**作业资源**页签，分别单击**流作业管理**或**批作业管理**。 ii. 选择迁移的作业和作业快照，单击向右的箭头，单击**确认**。 您可以仅选择迁移作业，或者同时选择迁移作业及其某个状态快照。单击左侧的 ，即可看到作业相关的快照信息。 iii. 在右侧选择作业状态资源后，单击**确认**。
6. 单击**开始迁移**。
迁移完成后，根据资源迁移状态和错误信息判断是否需要重新调整迁移资源后再次进行迁移，迁移完成的您就可以在Flink存算分离的目标项目空间中查看迁移过来的任务。 实时计算（流计算）

## Flink MCP Server

Flink基于MCP协议，支持通过飞天助理-托管模式调用API获取空间、作业等信息，也可通过自行部署MCP Server方式实现查询，助力用户打造自然语言驱动的数据查询Agent，实现从提问到可视化的智能数据处理全流程。本文介绍使用飞天助理托管模式和自行部署MCP Server的操作方式。

**支持MCP模式**

飞天助理-托管模式飞天助理托管模式开箱即用，无需用户配置，可以直接通过大模型访问。 自行部署MCP Server 用户可以在应用、智能体或AI中自行部署。

**飞天助理-托管模式**

**说明**

使用飞天助理-托管模式前，请先参考**统一云管平台** > **飞天助理****用户指南**文档开启飞天助手。
1. 登录实时计算Flink版管理控制台。
2. 查看系统预设的MCP列表。
i. 在左侧导航栏单击**AI****专栏** **> AI****原生接口****MCP****服务**。 ii. 在**MCP****列表** **> Flink****管控****MCP**单击图标，进入**MCP****详情**页面。 实时计算（流计算） iii. 单击**工具**，查看系统预设的MCP列表。当前系统预设工具如下：

| 工具名称 | 调用接口 | 说明 |
|---|---|---|
| 引擎版本列表查询 | ListFlinkVersions | 列出指定Namespace中支持的Flink引擎版本号，有助于用户选择合适的引擎来创建与运行作业。 |
| 工作空间列表查询 | DescribeWorkspacesFlin kOnOss | 查询当前用户的工作空间列表，有助于用户管理 WorkSpace，优化资源管理。 |
| 工作空间下属命名空间列表查询 | ListNamespacesByWork spaceIdFlinkOnOss | 查询指定工作空间下的NameSpace列表，有助于用户管理NameSpace，优化资源分配与管理。 |
| 用户全量命名空间列表查询 | DescribeNamespacesFli nkOnOss | 查询指定用户下的全量NameSpace列表，有助于用户管理NameSpace，优化资源分配与管理。 |
| 作业列表查询 | ListJobs | 查询指定NameSpace名称，获取作业列表，有助于用户作业管理，优化作业资源与执行计划。 |
| 作业部署列表查询 | ListDeployments | 查询指定NameSpace名称，获取已部署作业的列表信息，有助于用户作业管理，优化作业资源与执行计划。 |
| 用户资源查询 | ListArtifacts | 列出指定命名空间和工作区中的用户资源，有助于用户作业管理，优化作业资源管理。 |

3. 使用飞天助理调用预设工具。
i. 在页面顶部单击工具栏中的图标，进入**飞天助理**页。 ii. 在对话框底部单击图标，打开**MCP**开关，单击图标进入**选择** **MCP**页面。 iii. 选择已有的Flink MCP。 iv. 单击**确定**，返回对话框，使用自然语言描述查询内容，例如“查询当前用户的工作空间列表”。 v. 单击右侧的图标发送并执行指令信息。 vi. 等待任务执行结束，您可查看返回的结果信息。

**自行部署MCP Server**

1. 下载MCP服务包。
2. 部署在ECS、容器或云外服务器。
实时计算（流计算）
3. 集成至应用或智能体：将MCP作为后端服务嵌入AI应用、智能体（Agent）或RPA流程中。
4. 通过RESTful API调用MCP功能。
实时计算（流计算）

## 常见问题

本文介绍在Flink存算分离版使用过程中遇到的常见问题及解决方案，主要包括创建Namespace、查看 Flink审计事件的FAQ。 问题描述：为什么我的账号已经授予了Namespace的访问权限，列表中却没有目标Namespace? 问题原因：针对该问题，可能存在两种情况： 您的账号没有加入到Namespace所属的资源集。 问题描述：为什么我的账号进入Flink Workspace 列表后，有些操作按钮没有显示，或者有显示但是有些按钮是灰色的？ 问题原因： 您的资源管理角色没有授权创建、删除工作空间或项目空间的权限，请联系管理员配置对应空间访问权您在**控制台**置灰的项目空间中没有被分配业务角色，无法访问实时计算开发控制台，请联系资源owner 问题描述：为什么我的账号在创建，修改，删除等操作提交后，报错没有权限修改项目空间？ 实时计算（流计算） 问题原因：如图所示，账号当前的角色没有被授权进行如上操作。请联系管理员配置项目空间访问权限， 问题描述：为什么进入审计页面后，原始日志中没有数据？ 问题原因：存在以下两种可能情况： 用户在查询的时间段内未曾操作vvp平台。 用户确实进行了vvp平台的操作，此时需要对日志上报的成功与否进行排查。请联系阿里云技术支持获取排查方案。 问题描述：为什么进入审计页面后，有原始日志，但是没有审计数据？ 问题原因：存在以下两种可能情况： 在审计查询的时间段内，用户未进行高危操作。 用户确实进行了高危操作，但云盾单日日志审计已达到上限，此时需要联系云盾相关同事以调高单日审计上限。
