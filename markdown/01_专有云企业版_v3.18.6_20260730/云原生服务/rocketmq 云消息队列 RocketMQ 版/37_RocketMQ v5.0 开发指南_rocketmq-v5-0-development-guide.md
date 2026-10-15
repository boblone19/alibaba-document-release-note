---
title: "云消息队列 RocketMQ 版 RocketMQ v5.0 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 169
source_pdf: "37_RocketMQ v5.0 开发指南_rocketmq-v5-0-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/rocketmq/zh/rocketmq-v5-0-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云消息队列 RocketMQ 版 RocketMQ v5.0 开发指南

消息队列

## 快速入门

### 开发文档使用说明

本文为您介绍在使用专有云API进行开发工作时，如何查看所需要的产品文档。

**使用流程**

您可以按照以下流程图中步骤，判断自己所需要使用的开发文档。

**前提条件**

通过运维人员或运营管理员已获取专有云的版本。

**操作步骤**

您可以通过阿里云专有云文档中心，获取需要的产品文档。
1. 通过浏览器打开专有云文档中心。
2. 根据专有云的版本，单击**飞天企业版**、**敏捷版****&XStack**或**一体机**页签。
消息队列
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

本文为您介绍调用流程及可以参考的文档资料。

**流程图**

消息队列

| 获取API信息获取AccessKey或STS AccessKey 获取公共Header参数 |  |
|---|---|
| 获取RocketMQ v5.0的Endpoint 获取RocketMQ v5.0的SDK包调用API |  |

准备工正式调

**调用步骤**

1. 获取AccessKey。

**说明**

推荐使用个人AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
3. 获取组织ID与资源集ID。

**说明**

调用API时，通过Header参数组织ID（<x-acs-organizationid>）和资源集ID（<x-acsresourcegroupid>）指定组织和资源集，实现实例资源的隔离查询。 组织ID（<x-acs-organizationid>）不指定则默认获取当前用户所属的组织。 资源集ID（<x-acs-resourcegroupid>）不指定默认为空，如果指定资源集需要同时指定组织ID。
4. 查找API的开发文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，查找开发指南的方式请参见开发文档使用说明。 消息队列
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
消息队列

## 准备工作

### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 消息队列通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。

**说明**

AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。 消息队列
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取公共Header参数

调用API时需要提供多个Header参数。本文为您介绍如何获取这些参数。并对调用后的一些返回值做出解释。

**获取Region ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理**>**地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看**Region****名称**，即为Region ID。

**获取组织ID**

组织ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取组织ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，
调用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源
集ID。接口信息详见《**Apsara Uni-manager****运营控制台开发指南》**中的章节**ListResourceGroup**。 消息队列

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以API网关为例， 获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品** > **中间件** > **消息队列** > **消息队列** **RocketMQ** 版。
3. 在左侧导航栏中，单击**v4.0**右侧的**切换**，然后在弹框中单击**确定**，将环境切换为**v5.0**。
4. 在左侧导航栏中，单击**实例列表**。
5. 在实例列表中查看**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择利用STS方式，调用专有云的产品API。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 使用以下代码，通过角色的 `RAM Role` 获得 `stsAK` 、 `stsSK` 和 `stsToken` 。
消息队列

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
```

`//` 调用来源说明

```
        asClient.setSdkSource("test");
```

`//` 传入`Arn`

```
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
```

`//` 获取到`STS`三元组

```
        String stsAK = credentials.getString("AccessKeyId");
        String stsSK = credentials.getString("AccessKeySecret");
        String stsToken = credentials.getString("SecurityToken");
} public static String AssumeRole(ASClient asClient, String roleArn) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "AssumeRole");
        reqParams.put("Product", "Sts");
        reqParams.put("Version", "2015-04-01");
        reqParams.put("regionId", regionId);
```

`//` 当前登录用户的`ak`

```
        reqParams.put("AccessKeyId", <当前用户的AccessKey ID>);
```

`//` 当前登录用户的`sk`

```
        reqParams.put("AccessKeySecret", <当前用户的AccessKey Secret>);
        reqParams.put("roleSessionName", "StsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
}
```

3. 通过STS可以调用云产品的接口，示例如下。
消息队列

```java
import com.aliyun.credentials.Client; import com.aliyun.credentials.models.Config;
```

`//` 以下示例演示如何使用`STS Token`初始化凭据客户端（不包含如何获取到`STS Token`的过程）。

```java
public class DemoStsTest {
    public static void main(String[] args) {
        Config credentialConfig = new Config();
        credentialConfig.setType("sts");
        credentialConfig.setAccessKeyId("your_AccessKeyId");
        credentialConfig.setAccessKeySecret("your__AccessKeySecret");
```

`//` 请替换为前一步获取到的`STS`三元组中`SecurityToken`

```
        credentialConfig.setSecurityToken("your__SecurityToken");
        Client credentialClient = new Client(credentialConfig);
```

`//` 继续调用`API`，完整参考的`API`文档

```
    }
}
```

消息队列

## 通过POP网关调用专有云API

### 概述

阿里云专有云与公共云一样，可通过POP网关的方式进行API调用。本文为您介绍概述情况。

**背景信息**

通过POP网关调用专有云API，可以实现对管控层资源（如实例、Topic、Group等）的增删改查等操作。平台已封装支持Java语言的SDK，您可以通过在平台中下载该SDK直接调用专有云API。 文档中SDK关于API的示例代码仅供参考，各API的完整使用步骤与参数说明请参见开发者门户SDK示例和 OpenAPI文档。

**环境要求**

支持JDK8~JDK19 Platform支持：Linux、Mac、Windows

**语言**

当前仅支持Java语言。

**发布历史**

**SDK版本**

| 版本号 | 发布时间 | 更新内容 |
|---|---|---|
| 3.18.6 | 2026.5 | 专有云3.18.6对外API的SDK。 |

**API列表**

当前专有云企业版SDK支持的API列表。

| API名称 | 所在版本 |
|---|---|
| ConsoleCreateCloudInfo | 3.18.6 |
| ConsoleCreateCloudRouterTask | 3.18.6 |
| ConsoleGroupCreate | 3.18.6 |
| ConsoleClusterCreate | 3.18.6 |
| ConsoleTopicCreate | 3.18.6 |

消息队列

| ConsoleDeleteCloudInfo | 3.18.6 |
|---|---|
| ConsoleDeleteCloudRouterTask | 3.18.6 |
| ConsoleGroupDelete | 3.18.6 |
| ConsoleTopicDelete | 3.18.6 |
| ConsoleTraceDeleteTraceQueryTask | 3.18.6 |
| ConsoleMessageDownload | 3.18.6 |
| ConsoleMessageDownloadAllInDLQ | 3.18.6 |
| ConsoleMessageDownloadBodyInDLQ | 3.18.6 |
| ConsoleListInPageCloudRouterTask | 3.18.6 |
| ConsoleGroupList | 3.18.6 |
| ConsoleTopicListInPage | 3.18.6 |
| ConsoleTraceListByUserIdInPage | 3.18.6 |
| ConsoleMessagePush | 3.18.6 |
| ConsoleConsumerAccumulate | 3.18.6 |
| ConsoleQueryCloudInfo | 3.18.6 |
| ConsoleQueryItemsCloudRouterTask | 3.18.6 |
| ConsoleQueryCloudRouterTask | 3.18.6 |
| ConsoleQueryStatsCloudRouterTask | 3.18.6 |
| ConsoleClusterGetCapacity | 3.18.6 |

消息队列

| ConsoleClusterList | 3.18.6 |
|---|---|
| ConsoleCommonRegionData | 3.18.6 |
| ConsoleConsumerAccumulate | 3.18.6 |
| ConsoleConsumerGetConnection | 3.18.6 |
| ConsoleConsumerJstackInfo | 3.18.6 |
| ConsoleConsumerProgress | 3.18.6 |
| ConsoleConsumerStatus | 3.18.6 |
| ConsoleConsumerTimespan | 3.18.6 |
| ConsoleGroupListGroupIds | 3.18.6 |
| ConsoleGroupList | 3.18.6 |
| ConsoleGroupSubDetail | 3.18.6 |
| ConsoleInstanceBaseInfo | 3.18.6 |
| ConsoleInstanceList | 3.18.6 |
| ConsoleInstanceStatistics | 3.18.6 |
| ConsoleMessageGetById | 3.18.6 |
| ConsoleMessageGetByIdInDLQ | 3.18.6 |
| ConsoleMessageGetByKey | 3.18.6 |
| ConsoleMessageGetByPagedDLQ | 3.18.6 |
| ConsoleMessageGetByPagedTopic | 3.18.6 |

消息队列

| ConsoleMetaData | 3.18.6 |
|---|---|
| ConsoleTraceGetPubTraceByQueryId | 3.18.6 |
| ConsoleRegionList | 3.18.6 |
| ConsoleTopicGet | 3.18.6 |
| ConsoleTopicList | 3.18.6 |
| ConsoleGroupListTopicsByGroupId | 3.18.6 |
| ConsoleTopicListNames | 3.18.6 |
| ConsoleTopicStatus | 3.18.6 |
| ConsoleTopicSubDetail | 3.18.6 |
| ConsoleTraceQueryByMsgId | 3.18.6 |
| ConsoleTraceQueryByMsgKey | 3.18.6 |
| ConsoleTraceQueryByMsgTopic | 3.18.6 |
| ConsoleTraceGetTraceMapByQueryId | 3.18.6 |
| ConsoleMessageResendByIdInDLQ | 3.18.6 |
| ConsoleConsumerResetOffset | 3.18.6 |
| ConsoleMessageSend | 3.18.6 |
| ConsoleStartCloudRouterTask | 3.18.6 |
| ConsoleStopCloudRouterTask | 3.18.6 |
| ConsoleMessageTrace | 3.18.6 |

消息队列

| ConsoleUpdateCloudInfo | 3.18.6 |
|---|---|
| ConsoleGroupConsumerUpdate | 3.18.6 |
| ConsoleGroupUpdateInfo | 3.18.6 |
| ConsoleInstanceUpdate | 3.18.6 |
| ConsoleTopicUpdate | 3.18.6 |
| ConsoleTopicUpdateInfo | 3.18.6 |

### 调用前置

阿里云专有云与公共云一样，可通过POP网关的方式进行API调用。本文为您介绍调用前需要进行的准备工作。

**背景信息**

为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

**获取云产品的Endpoint**

**通过开发者门户获取**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。
消息队列

**通过飞天基础运维平台获取**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。您也可以自行获取Endpoint，本文为您介绍获取云产品业务域Endpoint的方法。
1. 登录Apsara Uni-manager运维控制台。
2. 顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务注册变量大盘**。
4. 在**服务注册变量大盘**页面，单击**高级筛选**。
5. 在Service Registration文本框中输入 `ons_bizapi_endpoint` ，单击**搜索**。
6. 在 `mq-console` 服务的**Service Registration**列中，单击
图标。
7. 单击 `mq-console` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
ons_bizapi_endpoint值，即 `Endpoint` 。

**获取公共参数**

通过POP网关调用专有云API过程中所使用的参数，如组织ID、资源集ID、RegionID和实例ID，获取方式请

### Java版

本文为您介绍通过POP网关的方式进行API调用时，高级SDK的使用示例。

**安装说明**

**开发者门户获取SDK包**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
消息队列
3. 在**开发者门户**页面，选择**API****集成** > **SDK****示例**。
4. 单击
按钮，选择**中间件** > **消息队列****MQ**，**版本**选择**2018-02-05**。
5. 从**SDK****类型**下拉列表中选择**高级版**，选择Java语言。
6. 下方可看到示例代码，点击**下载完整工程**以获取示例项目及SDK包。

**导入SDK包**

1. 通过以下任一方式创建Maven项目。
方式一：在IDEA中添加一个Maven项目。 消息队列方式二：将已有的项目转换为Maven项目。 i. 右键单击要转换的项目，并选择**Add Framework Support...**。 消息队列 ii. 选择**Maven**，并单击**OK**。
2. 在项目根目录下创建lib目录，通过开发者门户获取SDK包后放入到lib目录下，如下图。
3. 在项目目录下的pom.xml中，添加Java SDK依赖。

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun.apsarastack</groupId>
        <artifactId>aliyun-java-sdk-ons</artifactId>
        <version>3.18.3-0</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/lib/aliyun-java-sdk-ons-3.18.3-
0.jar</systemPath>
    </dependency>
</dependencies>
```

4. 查看IDEA右侧Maven栏。
如图所示，表示已成功导入依赖。 消息队列

**代码示例**

示例展示了如何调用 `QueryInstanceList` API进行查询`MQ`实例列表请求。

```java
import com.aliyun.ons_inner20180205.Client; import com.aliyun.ons_inner20180205.models.QueryInstanceListRequest; import com.aliyun.ons_inner20180205.models.QueryInstanceListResponse; import com.aliyun.tea.TeaException; import com.aliyun.teaopenapi.models.Config; import com.aliyun.teautil.models.ExtendsParameters; import com.aliyun.teautil.models.RuntimeOptions; import java.util.HashMap; import java.util.Map; public class sample {
    public static void main(String[] args) throws Exception {
        // 1.初始化配置对象 com.aliyun.teaopenapi.models.Config
        Config config = new Config()
```

`//` 地域`ID`

```
                .setRegionId("<your-regionId>")
```

`//` 支持通过`Config`在初始化`Client`阶段设置请求的代理，根据实际情况替换下面示例。

```
                .setHttpProxy("http://127.0.0.1:9898");
```

`//` 访问的域名，可以参考开发者门户`API`调试页面获取 `Endpoint`

```
        config.endpoint = "<your Endpoint>";
```

`// 2.`实例化一个客户端，从 `com.aliyun.ons_inner20180205.Client` 类生成对象 `client` 。后

```
续 request、response 从 com.aliyun.ons_inner20180205.models 中获得。
        Client client = new Client(config);
```

`// 3.`运行时参数设置

```
        RuntimeOptions runtime = new RuntimeOptions();
        Map<String, String> headers = new HashMap<>();
```

`//` 组织`id`

```
        headers.put("x-acs-organizationid", "<your-organizationId>");
```

`//` 资源组`id`

```
        headers.put("x-acs-resourcegroupid", "<your-resourcegroupId>");
```

`//` 角色`id`

```
        headers.put("x-acs-roleId", "<your-roleId>");
        runtime.setExtendsParameters(new ExtendsParameters().setHeaders(headers));
```

`//` 支持通过运行时参数（`RuntimeOptions`）配置当前请求的代理，代理配置优先级：`RuntimeOption` 配置配置根据需要选择种即可消息队列配置 `> Client`配置，根据需要选择一种即可。

```
        runtime.setHttpProxy("http://127.0.0.1:9898");
        runtime.ignoreSSL = true;
        runtime.setConnectTimeout(3000);
        runtime.setReadTimeout(30000);
```

`// 4.`设置请求类 `request` 的参数，类的属性设置必要的信息，即 `API` 中必须要提供的信息可以参考具体的`API`文档。

```
        QueryInstanceListRequest request = new QueryInstanceListRequest();
```

`//` 该参数值为假设值，请您根据实际业务情况进行填写

```
        request.setNeedResourceInfo(true);
```

`//` 该参数值为假设值，请您根据实际业务情况进行填写

```
        request.setOnsSessionId("your_value");
```

`//` 该参数值为假设值，请您根据实际业务情况进行填写

```
        request.setOnsRegionId("your_value");
```

`//` 该参数值为假设值，请您根据实际业务情况进行填写

```
        request.setPreventCache(System.currentTimeMillis());
        try{
```

`// 5.`通过 `client` 对象获得对应 `request` 响应 `response` 。

```
            QueryInstanceListResponse response =
client.queryInstanceListWithOptions(request, runtime);
```

`// 6.`调用 `response` 中对应的属性获得返回的参数值，假设您需要获取 `requestId` ：

```
            String requestId = response.body.getRequestId();
```

`//` 打印返回结果仅做示例，请您根据实际业务情况替换

```java
            System.out.println(com.aliyun.teautil.Common.toJSONString(response));
        } catch (TeaException error) {
```

`//` 使用 `catch()` 处理报错。 `//` 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。

```java
            System.out.println(error.message);
        } catch (Exception _error) {
```

`//` 使用 `catch()` 处理报错。

```
            TeaException error = new TeaException(_error.getMessage(), _error);
```

`//` 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。

```java
            System.out.println(error.getMessage());
        }
    }
}
```

**步骤介绍**

1. 初始化配置对象com.aliyun.teaopenapi.models.Config。Config对象存放AccessKeyId、
AccessKeySecret、Endpoint等配置，该配置信息参考获取AccessKey和获取API信息及其EndPoint进行获取。

```
Config config = new Config() .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")) .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
```

`//` 访问的域名

```
config.endpoint = "************";
```

2. 实例化一个客户端，从com.aliyun.ons_inner20180205.Client类生成对象client 。后续request
消息队列 response从com.aliyun.ons_inner20180205.models中获得。

```
Client client = new Client(config);
```

3. 创建对应API的Request 。类的命名规则为API方法名加上Request。例如：

```
QueryInstanceListRequest request = new QueryInstanceListRequest();
```

4. 设置请求类request的参数。通过request类的属性设置必要的信息，即API中必须要提供的信息。
request.SourceRegionId = "your_value"; // 该参数值为假设值，请您根据实际情况进行填写 request.RegionId = "your_value"; // 该参数值为假设值，请您根据实际情况进行填写
5. 通过client对象获得对应request响应response 。

```java
QueryInstanceListResponse response = client.queryInstanceListWithOptions(request, run time); System.out.println(new Gson().toJson(response.Body));
```

6. 调用response中对应的属性获得返回的参数值。假设您需要获取requestId，例如：

```
String requestId = response.Body.requestId;
```

7. 使用catch()处理报错。

```
catch (Exception e) {
    e.printStackTrace();
}
```

消息队列

## API参考

### RocketMQ v5.0_API

#### RocketMQ v5.0 Open API简介

##### 面向用户和场景

Open API是RocketMQ v5.0提供给用户的管控手段，用于实现一系列资源管理和运维功能。同生产用SDK 不同，Open API主要用于管理RocketMQ v5.0相关的资源，例如Topic、Group ID等。 Open API的主要用户： 已经熟悉RocketMQ v5.0控制台的主要功能。 需要实现类似控制台的管控，存在自定义管控功能等需求。

##### 适用场景和局限性

1. Open API由于其实现原理，调用端必须具备访问RocketMQ v5.0控制台域名的能力，否则无法调通。
2. Open API底层基于HTTP协议实现，性能和效率不高，仅适用于管控场景，请勿用于大批量高并发的生产
场景。

##### Open API基本原理

Open API底层通过HTTP接口提供服务，用户调用HTTP客户端，发出HTTP请求到RocketMQ的后端服务去执行。 用户将参数封装到每个请求中，每个请求即对应一个接口，执行的结果放在response中，请求和响应的字符编码都是采用UTF-8编码。 其中，HTTP请求的服务端地址即为控制台的域名地址。

#### RocketMQ v5.0 Open API接入指南

##### 公共参数设置

客户端基于HTTPS方式调用RocketMQ v5.0 Open API，所有API请求都需要传入一部分公共参数，供服务端进行权限校验。 公共参数列表如下：

| 参数名称 | 类型 | 是否必须 | 说明 |
|---|---|---|---|
| accesskey _ | String | 是 | 用户账号AK。 |
| preventCache __ | Long | 是 | 用于CSRF校验，设置为系统当前时间即可，单位毫秒（ms）。 |

消息队列

| regionId _ | String | 是（获取regionId列表接口除外） | 当前Region。 |
|---|---|---|---|
| signature _ | String | 是 | 请求的签名。 |

**_regionId**参数需要填写当前请求操作的Region，专有域和专有云情况下，默认值为mq-private。
**_signature**参数是对HTTPS请求中其他参数字段做排序后得到待签名字符串，然后使用账号的SecretKey
进行签名计算得到。

**签名计算示例**

例如原始请求的HTTPS方法是：

```
https://mq.console.${global:internet-domain}/json/topic/create
```

**说明**

在单region部署的情况下或接入多region部署中的中心region，使用${global:internet-domain}作为访问域名；接入多region部署下的普通region，使用${global:region}.${global:internetdomain}作为访问域名参数列表有（参数包含公共参数和每个接口自定义的参数）：

**Key_2=Value_2&Key_1=Value_1&Key_3=Value_3**

那么原始请求URL是：

```
https://mq.console.${global:internet-domain}/json/topic/create? Key_2=Value_2&Key_1=Value_1&Key_3=Value_3
```

将**Key_2**，**Key_1**，**Key_3**这3对参数的key按字典序排序，然后将对应的value按字符串连接。Key的排序结果为：Key_1、Key_2、Key_3，排序后其对应值的连接结果为Value1Value2Value3。此时待签名字符串就是Value1Value2Value3。 然后使用您的secretKey作为密钥，使用 HmacSHA1方法对上面的待签名字符串做签名，得到签名字符串。Hmac的算法实现，各个语言都有现成的函数库，请自行搜索。 Linux命令行的方式可以参考：

```
echo -n 'Value1Value2Value3' | openssl dgst -hmac '用户的SecretKey' -sha1 -binary | base
```

假设最终得到的结果为：eqweq+adwe23****= 最后，整个HTTPS请求就是（注意通过curl的方式需要将“+”替换成“%2B”，“=”替换成“%3D”，“/”替换成“%2F”，否则自动转义后会报鉴权失败）：

```
https://mq.console.${global:internet-domain}/json/topic/create? Key_2=Value_2&Key_1=Value_1&Key_3=Value_3&_signature= eqweq%2Badwe23****%3D
```

##### 公共返回值解析

消息队列客户端发起HTTP请求到服务端，服务端处理完成后同样以HTTP响应形式返回结果，正常情况下返回结果 HTTP状态码都是200，返回的内容放在Body中，为JSON字符串，需要客户端自己做JSON解析，判断是否调用成功。 JSON格式如下：

```json
 {
    "code": 200,
    "currentPage": 0,
    "data": { },
    "dynamicCode": "",
    "dynamicMessage": "",
    "message": "operation success",
    "pageSize": 0,
    "requestId": "",
    "status": "SUCCESS",
    "success": true,
    "total": 0
}
```

返回值说明： code：状态码，200代表成功，其他都是处理失败。 currentPage：当前请求如果是分页查询的请求，此变量代表结果所处的当前页。 dynamicMessage：错误异常信息字符串。 message：处理结果信息。 pageSize：当前请求如果是分页查询的请求，此变量代表结果所处的当前页大小。 success：是否成功。 data：业务信息返回，String类型，也是JSON，如果当前请求的返回结果中带有业务数据，则此处需要反解JSON内容。 RequestId：每个请求的唯一ID，String类型。

#### RocketMQ v5.0 Open API公共术语

##### 账号安全类

###### AccessKey

访问阿里云产品使用的账号的AccessKeyId，在控制台获得。调用时传入给RocketMQ v5.0后台用于身份验证，调用RocketMQ v5.0 Open API只能操作对应账号下的资源。

###### SecretKey

访问阿里云产品使用的账号的AccessKeySecret，在控制台获得，调用时传入，用于计算访问请求的签名。RocketMQ v5.0后端根据对应账号比对签名实现鉴权。

##### RocketMQ v5.0资源管控类

###### Topic

RocketMQ v5.0产品中消息按照Topic进行分类存储，因此Topic是RocketMQ v5.0中最重要的资源之消息队列

###### Group ID（GID）

一类Producer或Consumer，这类Producer或Consumer通常生产或消费同一类消息，且消息发布或订阅的逻辑一致。 对于子账号创建的消费者Group ID或存量CID，该子账号及其主账号都有使用权限。 对于主账号创建的消费者Group ID或存量CID，仅该主账号有使用权限，其子账号无使用权限。

#### RocketMQ v5.0 Open API错误码列表

RocketMQ v5.0 Open API调用成功时返回给客户端的ResponseCode=200，当出现调用失败时，会返回对应的异常错误码以及描述信息。您可以根据以下异常信息对照表查找对应的解决方法。

| 错误码 | 现象&原因 | 解决方法 |
|---|---|---|
| ONS SYSTEM ERROR _ _ | RocketMQ v5.0后端异常。 | 通过阿里云工单联系RocketMQ v5.0技术人员。 |
| ONS SERVICE UNSUPPORTED _ _ | 当前调用在对应的区域不支持。 | 请找RocketMQ v5.0技术支持确认该接口的开通情况。 |
| ONS INVOKE ERROR _ _ | Open API接口调用失败。 | 联系RocketMQ v5.0技术人员处理。 |
| BIZ FIELD CHECK INVALID _ _ _ | 参数检验失败。 | 请参考API手册检查各个参数传入是否合法。 |
| BIZ TOPIC NOT FOUND _ _ _ | Topic没有找到。 | 请检查Topic输入是否合法，或者是否创建过。 |
| BIZ SUBSCRIPTION NOT FOUND _ _ _ | 目标订阅关系GID找不到。 | 请检查GID是否创建过，或者查询条件错误。 |
| BIZ PUBLISHER EXISTED _ _ | 指定GID已经存在。 | 更换GID的名称重试请求。 |
| BIZ SUBSCRIPTION EXISTED _ _ | 指定GID已经存在。 | 更换GID的名称重试请求。 |
| BIZ CONSUMER NOT ONLINE _ _ _ | 指定GID的客户端不在线。 | 请确保消费端在线，然后重试请求。 |

消息队列

| BIZ NO MESSAGE _ _ | 当前查询条件没有匹配消息。 | 请检查查询条件，并确认查询范围内是否发过消息。 |
|---|---|---|
| BIZ REGION NOT FOUND _ _ _ | 请求的region找不到。 | 确认请求的Region参数是否合法。 |
| BIZ TOPIC EXISTED _ _ | 指定Topic已经存在。 | 更改Topic名称重试请求。 |
| BIZ PRODUCER ID BELONG TO OTHER US _ _ _ _ _ _ ER | 当前GID已经被其他用户占用。 | 更换GID重试请求。 |
| BIZ CONSUMER ID BELONG TO OTHER US _ _ _ _ _ _ ER | 当前GID已经被其他用户占用。 | 更换GID重试请求。 |
| BIZ PUBLISH INFO NOT FOUND _ _ _ _ | 请求的GID没有找到。 | 确认GID是否存在，或者请求条件错误。 |
| EMPOWER EXIST ERROR _ _ | 当前授权关系已经存在。 | 核实请求参数，重试或者先查询。 |
| EMPOWER OWNER CHECK ERROR _ _ _ | 当前用户不是授权Topic的 Owner。 | 确认资源所属关系。 |

#### API详细说明

##### 实例管理

###### ConsoleInstanceList

获取实例列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |

| ocketMQ v5. | 0开发指南 | ·API参考 |  |  | 消息队列 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |
| NeedReso urceInfo | Boole an | Query | 否 | true | 是否需要资源统计信息。即实例下Topic的数量和 Group的数量。 默认值： false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |
| Success | Boolean | true | 是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleInstanceList &OnsRegionId=region123 &PreventCache=xxxxx
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleClusterCreate

创建MQ实例接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-wulan-env***-d01 | 实例所属的地域ID。 |
| InstanceN ame | Strin g | Query | 是 | test instance _ | 待创建的实例名称。 不填写则以实例ID作为实例名称。 |
| ResourceT ype | Strin g | Query | 是 | rmq.1xunit | 资源类型。 |
| Replicas | Strin g | Query | 是 | 4 | 实例副本数。 |
| Remark | Strin g | Query | 否 | This is the remark for test. | 实例的备注信息。 |
| TopicCapa city | Integ er | Query | 否 | 50 | 该实例下允许创建的Topic 数量上限。 |
| MaxSendT ps | Long | Query | 否 | 1000 | 表示系统每秒最多可以处理 1000个发送请求。 |
| MaxRecei veTps | Long | Query | 否 | 1000 | 表示系统每秒最多接收 1000个事务请求 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Independe ntNaming | Boole an | Query | 否 | true | 实例是否有命名空间。取值说明如下： true ：拥有独立命名空间，资源命名确保实例内唯一，跨实例之间可重名。 false ：无独立命名空间，实例内或者跨实例之间，资源命名必须全局唯一。 默认值：true |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 否 | 1000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |
| Code | Integer | 200 | HTTP状态码或接口错误码。 |

**示例**

请求示例消息队列

```
http(s)://[Endpoint]/?Action=ConsoleClusterCreate &InstanceName=test_instance &ResourceType=rmq.1xunit &Replicas=4 &OnsRegionId=region123
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleClusterSpecList

查询集群规格信息接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 实例所属的地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 否 | 100000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 附加信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleClusterSpecList &OnsRegionId=region123
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleClusterStatus

查询RocketMQ v5.0实例Pod状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 否 | 10000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| InstanceId | Strin g | Query | 是 | MQ INST 1****mioMmJ0 _ _ | 待查询实例的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleClusterStatus &OnsRegionId=region123 &InstanceId=MQ_INST_1****mioMmJ0
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleInstanceStatistics

实例统计数据接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| EndTime | Long | Query | 否 | 1706668721 | 查询结束时间。 |
| OnsSessio nId | Strin g | Query | 否 | abc123*** | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |

|  | 消息队列 |  |  | RocketMQ v5.0开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleInstanceStatistics &PreventCache=1000 &InstanceId=MQ_INST_136744485915***_B***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleInstanceUpdate

更新实例信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据而非使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceN ame | Strin g | Query | 否 | test instance _ | 实例名称。 |
| Remark | Strin g | Query | 否 | This is the remark for test. | 备注。 |
| TopicCapa city | Integ er | Query | 否 | 50 | 该实例下允许创建的Topic 数量上限。 |
| MaxSendT ps | Long | Query | 否 | 1000 | 表示系统每秒最多可以处理 1000个发送请求。 |
| MaxRecei veTps | Long | Query | 否 | 1000 | 表示系统每秒最多接收 1000个事务请求 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleInstanceUpdate &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136744485915***_B***
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleInstanceBaseInfo

查询实例详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |

| RocketMQ v5.0开发 | 指南·API参考 |  | 消息队列 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleInstanceBaseInfo &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136744485915***_B***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Topic管理

###### ConsoleTopicDelete

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PreventCa che | Long | Query | 是 | xxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test | Topic名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |
| Success | Boolean | true | 是否成功 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTopicDelete &OnsRegionId=region123 &PreventCache=xxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

消息队列

###### ConsoleTopicListInPage

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 15243******3 _ _ _ BmioMmJ0 | 实例的ID。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |
| PageSize | Integ er | Query | 否 | 10 | 分页大小，每页最多显示的返回结果数量。 取值范围： 10~200。 若您设置的参数值小于10，则系统默认按照参数值为10处理；若您设置的参数值大于200，则系统默认按照参数值为200处理。 |
| Search | Strin g | Query | 否 | test | 搜索关键字。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |

| 消息队列 |  |  | RocketMQ v5.0开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTopicListInPage &OnsRegionId=cn-wulan-env188-d01 &PreventCache=xxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTopicStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |

| ocketMQ v5. | 0开发指南 | ·API参考 |  |  | 消息队列 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-mq topic _ | Topic名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTopicStatus &OnsRegionId=region123 &PreventCache=xxxx
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTopicUpdateInfo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13*****3 Bmio _ _ _ MmJ0 | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-mq topic _ | Topic名称。 |
| Remark | Strin g | Query | 是 | xxxx | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTopicUpdateInfo &OnsRegionId=region123 &PreventCache=xxx &InstanceId=MQ_INST_13*****3_BmioMmJ0 &Remark=xxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTopicUpdate

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |

|  | 消息队列 |  |  |  | Roc | ketMQ v5.0开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13*****BmioM _ _ mJ0 | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| Perm | Integ er | Query | 否 | 6 | 设置该 Topic 的读写模式。 取值说明： 6：同时支持读写。 4：禁写。 2：禁读。 |
| UnitFlag | Boole an | Query | 否 | unitA | 单元隔离开关。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例消息队列

```
http(s)://[Endpoint]/?Action=ConsoleTopicUpdate &OnsRegionId=region123 &PreventCache=xxxxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTopicSubDetail

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存的旧资源。 |
| InstanceId | Strin g | Query | 是 | MQ INST 136*****33 B _ _ _ mioMmJ0 | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

消息队列

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTopicSubDetail &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136*****33_BmioMmJ0
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTopicListNames

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存的旧资源。 |
| InstanceId | Strin g | Query | 否 | MQ INST 1**** BmioMm _ _ _ J0 | 实例的ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTopicListNames &OnsRegionId=region123 &PreventCache=xxxx
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTopicList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 否 | test-topic | Topic名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |

|  | RocketMQ v5.0开发 | 指南·API参考 |  | 消息队列 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
&OnsRegionId=region123 &PreventCache=xxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTopicGet

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |

| 消息队列 |  |  |  | Roc | ketMQ v5.0开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 否 | test-topic | Topic名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
&OnsRegionId=region123 &PreventCache=xxxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

消息队列

###### ConsoleTopicCreate

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| OrderType | Integ er | Query | 否 | 0 | 消息类型。 0：普通消息。 1：分区顺序消息。 4：事务消息。 5：定时/延时消息。 |
| Remark | Strin g | Query | 否 | xxxxx | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTopicCreate &OnsRegionId=region123 &PreventCache=xxxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleGroupListTopicsByGroupId

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |

| ocketMQ v5. | 0开发指南 | ·API参考 |  |  | 消息队列 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleGroupListTopicsByGroupId &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136744485915***_B*** &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Group管理

###### ConsoleGroupListInPage

分页查询订阅组信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |
| PageSize | Integ er | Query | 否 | 10 | 分页大小，每页最多显示的返回结果数量。 取值范围：10~200。 若您设置的参数值小于10， 则系统默认按照参数值为10 处理；若您设置的参数值大于200，则系统默认按照参数值为200处理。 |
| GroupTyp e | Strin g | Query | 否 | 0 | Group类型。 |

|  | RocketMQ v5. | 0开发指南 | ·API参考 |  |  | 消息队列 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Search | Strin g | Query | 否 | test | 搜索关键字。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleGroupListInPage &OnsRegionId=cn-wulan-env188-d01 &PreventCache=xxxx &InstanceId=MQ_INST_1367444859152433_BmioMmJ0
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

消息队列

###### ConsoleGroupUpdateInfo

更新订阅组信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| Remark | Strin g | Query | 是 | This is the remark for test. | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

消息队列

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleGroupUpdateInfo &OnsRegionId=region123 &PreventCache=xxxx &GroupId=GID_test &Remark=This is the remark for test.
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleGroupListGroupIds

获取GroupIds。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleGroupListGroupIds &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136744485915***_B***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

消息队列

###### ConsoleGroupList

查询消费组列表

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 否 | GID test _ | 消息组ID。 |
| GroupTyp e | Strin g | Query | 否 | 0 | Group类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

消息队列

**示例**

请求示例

```
&OnsRegionId=region123 &PreventCache=xxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleGroupDelete

删除消费者组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |

**返回数据**

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleGroupDelete &OnsRegionId=region123 &PreventCache=xxxxx &InstanceId=MQ_INST_136744485915***_B*** &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleGroupCreate

创建消费者组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| GroupTyp e | Strin g | Query | 否 | 0 | Group类型。 |
| Remark | Strin g | Query | 否 | This is the remark for test. | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例消息队列

```
http(s)://[Endpoint]/?Action=ConsoleGroupCreate &OnsRegionId=region123 &PreventCache=xxxx &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Message管理

###### ConsoleMessageGetByPagedDLQ

分页查询死信消息接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 实例所属的地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消费者组ID。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TaskId | Strin g | Query | 否 | ev- c5566dc90a718042e40a cfa07e29e**** | 任务ID。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |
| PageSize | Integ er | Query | 否 | 10 | 分页大小，每页最多显示的返回结果数量。 取值范围：10~200。 若您设置的参数值小于10， 则系统默认按照参数值为10 处理；若您设置的参数值大于200，则系统默认按照参数值为200处理。 |
| BeginTime | Long | Query | 否 | 1570852800000 | 开始时间。 |
| EndTime | Long | Query | 否 | 1703575552000 | 结束时间。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 返回数据总数 |

###### ConsoleMessageResendByIdInDLQ

消息队列死信消息重推接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消费者组ID。 |
| MsgId | Strin g | Query | 是 | 0BC16699165C03B925D B8A404E2D**** | 消息ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | C7F94090-3358- 506A-97DC- 34BC803C**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleMessageDownload

消息队列下载消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据而非使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| MsgId | Strin g | Query | 是 | 0BC16699165C03B925D B8A404E2D**** | 消息ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

消息队列

**示例**

`JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleMessageDownloadAllInDLQ

下载死信队列中的消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据而非使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| MsgId | Strin g | Query | 是 | 1E0578FE110F18B4AAC 235C05F2***** | 消息ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 返回数据总数 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleMessageDownloadAllInDLQ &OnsRegionId=region123 &PreventCache=xxxxx &InstanceId=MQ_INST_136744485915***_B*** &GroupId=GID_test &MsgId=1E0578FE110F18B4AAC235C05F2*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleMessageSend

消息发送。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| Tag | Strin g | Query | 否 | 标签1 | 标签。 |
| Key | Strin g | Query | 否 | TestKey | 消息key |
| Message | Strin g | Query | 是 | xxxx | 消息内容。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例消息队列

```
http(s)://[Endpoint]/?Action=ConsoleMessageSend &OnsRegionId=region123 &PreventCache=xxxx &Message=xxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleMessageTrace

查询消息轨迹。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| MsgId | Strin g | Query | 是 | 0BC16699165C03B925D B8A404E2D**** | 消息ID。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |
| NeedDeliv eryResult | Boole an | Query | 否 | false | 表示需要交付结果，通常用于标识某个流程或任务需要返回最终执行结果给调用方或系统。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleMessageTrace &OnsRegionId=cn-wulan-env188-d01 &PreventCache=xxxx &MsgId=0BC16699165C03B925DB8A404E2D****
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleMessagePush

推送消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| ClientId | Strin g | Query | 是 | c-********************* | 客户端ID。 |
| MsgId | Strin g | Query | 是 | 0BC16699165C03B925D B8A404E2D**** | 消息ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleMessagePush &OnsRegionId=region123 &PreventCache=xxxx &GroupId=GID_test &ClientId=c-********************* &MsgId=0BC16699165C03B925DB8A404E2D****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleMessageGetByPagedTopic

分页查询消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 消息队列

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| TaskId | Strin g | Query | 否 | 123456 | 任务ID。 |
| BeginTime | Long | Query | 是 | 1570852800000 | 开始时间。 |
| EndTime | Long | Query | 是 | 1703575552000 | 结束时间。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 分页查询时，当前页的页码。 |
| PageSize | Integ er | Query | 是 | 10 | 分页大小，每页最多显示的返回结果数量。 取值范围：10~200。 若您设置的参数值小于10， 则系统默认按照参数值为10 处理；若您设置的参数值大于200，则系统默认按照参数值为200处理。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |

| RocketMQ v5.0开发 | 指南·API参考 |  | 消息队列 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleMessageGetByPagedTopic &OnsRegionId=region123 &BeginTime=1570852800000 &EndTime=1703575552000 &PageSize=10
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleMessageGetByKey

根据消息Key查询消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test | Topic名称。 |
| Key | Strin g | Query | 是 | key1 | 消息key值。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例消息队列

```
http(s)://[Endpoint]/?Action=ConsoleMessageGetByKey &OnsRegionId=region123 &PreventCache=xxxx &Key=key1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleMessageGetByIdInDLQ

根据消息ID获取死信队列中的消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| MsgId | Strin g | Query | 是 | 0BC16699165C03B925D B8A404E2D**** | 消息ID。 |

| 消息队列 |  |  |  | Roc | ketMQ v5.0开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleMessageGetByIdInDLQ &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136744485915***_B*** &GroupId=GID_test &MsgId=0BC16699165C03B925DB8A404E2D****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

消息队列

###### ConsoleMessageGetById

查询消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| MsgId | Strin g | Query | 是 | 0BC16699165C03B925D B8A404E2D**** | 消息ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |

| 消息队列 |  |  | RocketMQ v5.0开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleMessageGetById &OnsRegionId=region123 &PreventCache=xxx &InstanceId=MQ_INST_136744485915***_B*** &MsgId=0BC16699165C03B925DB8A404E2D****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleMessageDownloadBodyInDLQ

下载死信队列中的消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存 |

| ocketMQ v5. | 0开发指南 | ·API参考 |  |  | 消息队列 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| MsgId | Strin g | Query | 是 | 0BC16699165C03B925D B8A404E2D**** | 消息ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleMessageDownloadBodyInDLQ &OnsRegionId=region123 &PreventCache=xxxxx &InstanceId=MQ_INST_136744485915***_B*** &GroupId=GID_test &MsgId=0BC16699165C03B925DB8A404E2D****
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Trace管理

###### ConsoleTraceDeleteTraceQueryTask

删除轨迹查询任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| QueryId | Strin g | Query | 是 | 2729675626528836491 57096685**** | 查询ID，即查询的唯一标识。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

###### ConsoleTraceGetPubTraceByQueryId

查询消息发送轨迹接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 实例所属的地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| QueryId | Strin g | Query | 是 | 2729675626528836491 57096685**** | 查询ID，即查询的唯一标识。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 分页查询时，当前页的页码。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

消息队列

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

###### ConsoleTraceQueryByMsgId

查询消息轨迹。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 1******33 Bmi _ _ _ oMmJ0 | 实例的ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| MsgId | Strin g | Query | 是 | 0BC16699165C03B925D B8A404E2D**** | 消息ID。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTraceQueryByMsgId &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_1******33_BmioMmJ0 &MsgId=0BC16699165C03B925DB8A404E2D****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTraceQueryByMsgTopic

消息队列根据主题名称查询消息轨迹。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 1****** BmioM _ _ _ mJ0 | 实例的ID。 |
| Topic | Strin g | Query | 是 | test | topic名称。 |
| BeginTime | Long | Query | 否 | 1570852800000 | 开始时间。 |
| EndTime | Long | Query | 是 | 1703575552000 | 结束时间。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |

| RocketMQ v5.0开发 | 指南·API参考 |  | 消息队列 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTraceQueryByMsgTopic &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_1******_BmioMmJ0 &EndTime=1703575552000
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTraceQueryByMsgKey

根据消息Key查询消息轨迹。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据而非使用本地缓存 |
| InstanceId | Strin g | Query | 是 | MQ INST 136********3 _ _ _ BmioMmJ0 | 实例的ID。 |
| Topic | Strin g | Query | 是 | test | Topic名称。 |
| MsgKey | Strin g | Query | 是 | keyA | 需查询的消息的Message Key。 |
| BeginTime | Long | Query | 否 | 1570852800000 | 开始时间。 |
| EndTime | Long | Query | 是 | 1703575552000 | 结束时间。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例消息队列

```
http(s)://[Endpoint]/?Action=ConsoleTraceQueryByMsgKey &OnsRegionId=region123 &PreventCache=xxxxx &InstanceId=MQ_INST_136********3_BmioMmJ0 &MsgKey=keyA &EndTime=1703575552000
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTraceListByUserIdInPage

查询用户权限内的轨迹信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 1367*****3 B _ _ _ mioMmJ0 | 实例的ID。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | 否 | 10 | 分页大小，每页最多显示的返回结果数量。 取值范围： 10~200。 若您设置的参数值小于10，则系统默认按照参数值为10处理；若您设置的参数值大于200，则系统默认按照参数值为200处理。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTraceListByUserIdInPage &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_1367*****3_BmioMmJ0
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleTraceGetTraceMapByQueryId

根据单一的QueryID获取完整轨迹链路图。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13*****33 Bmi _ _ _ oMmJ0 | 实例的ID。 |
| QueryId | Strin g | Query | 是 | 2729675626528836491 57096685**** | 查询ID，即查询的唯一标识。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleTraceGetTraceMapByQueryId &OnsRegionId=region123 &PreventCache=xxxxx &InstanceId=MQ_INST_13*****33_BmioMmJ0 &QueryId=272967562652883649157096685****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Consumer管理

###### ConsoleConsumerGetConnection

获取在线消费者信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |

| R | ocketMQ v5. | 0开发指南 | ·API参考 |  |  | 消息队列 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 返回码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleConsumerGetConnection &OnsRegionId=region123 &PreventCache=xxxxx &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleConsumerProgress

查看消费者消费进度。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| GroupId | Strin g | Query | 否 | GID test _ | 消息组ID。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| Consumer Id | Strin g | Query | 否 | consumer-123 | 消费者ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |

| RocketMQ v5.0开发 | 指南·API参考 |  | 消息队列 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleConsumerProgress &OnsRegionId=region123 &PreventCache=xxxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleGroupConsumerUpdate

更新订阅组消费者信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |

| 消息队列 |  |  |  | Roc | ketMQ v5.0开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| ReadEnab le | Boole an | Query | 否 | true | 读权限。 |
| UnitFlag | Boole an | Query | 否 | unitA | 单元隔离开关。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 请求返回代码，如为200则请求成功。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleGroupConsumerUpdate &OnsRegionId=region123 &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleConsumerAccumulate

查看消费进度接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消费者组ID。 |
| Detail | Boole an | Query | 否 | true | 明细。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |

| 消息队列 |  |  | RocketMQ v5.0开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleConsumerTimespan

查看消费进度。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| Topic | Strin g | Query | 是 | test-topic | Topic名称。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleConsumerTimespan &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136744485915***_B*** &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleGroupSubDetail

查询消费者订阅的详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | 表示某一特定区域（如华东、华北等）的唯一标识， 用于消息服务中区分不同地理区域的部署和管理。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存副本。 |
| InstanceId | Strin g | Query | 是 | MQ INST 136*******3 B _ _ _ mioMmJ0 | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123*** | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例消息队列

```
http(s)://[Endpoint]/?Action=ConsoleGroupSubDetail &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136*******3_BmioMmJ0 &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleConsumerStatus

查询消费者消费状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| Detail | Boole an | Query | 否 | true | 明细。 |

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NeedJstac k | Boole an | Query | 否 | true | 是否打印 Jstack 信息。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleConsumerStatus &OnsRegionId=region123 &PreventCache=xxxx &InstanceId=MQ_INST_136744485915***_B*** &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式消息队列

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleConsumerResetOffset

重置消费位点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据而非使用本地缓存 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| GroupId | Strin g | Query | 是 | GID test _ | 消息组ID。 |
| Topic | Strin g | Query | 是 | test | Topic名称。 |
| Type | Integ er | Query | 否 | 1 | 类型。 0：从最新位点开始消费， 1：按时间点重置。 |
| ResetTime | Long | Query | 否 | 2022-10-29 01:06:24 | 重置时间，从xxxx时间点开始消费。 |

**返回数据**

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleConsumerResetOffset &OnsRegionId=region123 &PreventCache=xxxxx &InstanceId=MQ_INST_136744485915***_B*** &GroupId=GID_test
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleConsumerJstackInfo

查询消费者堆栈信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 是 | xxxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |
| Consumer Id | Strin g | Query | 否 | consumer-123 | 消费者ID。 |
| GroupId | Strin g | Query | 否 | GID test _ | 消息组ID。 |
| ClientId | Strin g | Query | 是 | GID test@@@test _ | 客户端ID。 |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 5*** B*** _ | 实例的ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

消息队列请求示例

```
http(s)://[Endpoint]/?Action=ConsoleConsumerJstackInfo &OnsRegionId=region123 &PreventCache=xxxx &ClientId=GID_test@@@test
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Cluster管理

###### ConsoleClusterGetCapacity

获取集群容量接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 实例所属的地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 否 | 1000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| ResourceT ype | Strin g | Query | 否 | rmq.1xunit | 资源类型。 |
| Replicas | Strin g | Query | 否 | 4 | 副本数。 |

消息队列

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleClusterList

查询集群列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定资源所在的地理区域。 |
| PreventCa che | Long | Query | 否 | xxx | 启用防止缓存功能，确保每次请求都从服务器获取最新数据，避免使用本地缓存。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |

|  |  |  | RocketMQ v5.0 ·API |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleClusterList &OnsRegionId=region123
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Total":1,
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Region管理

###### ConsoleRegionList

查询区域。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| OnsSessio nId | Strin g | Query | 否 | abc123*** | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
&PreventCache=1000
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

消息队列

###### ConsoleMetaData

查询元数据信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| OnsSessio nId | Strin g | Query | 否 | abc123*** | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |
| RegionId | Strin g | Host | 否 | cn-hangzhou | 实例所属的地域ID，用于指定服务的地理区域。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
&OnsRegionId=region123
```

&公共请求参数正常返回示例消息队列 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleCommonRegionData

查询区域参数接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PreventCa che | Long | Query | 是 | 10000 | 指示客户端和中间代理服务器不要缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| OnsSessio nId | Strin g | Query | 否 | abc123*** | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

消息队列请求示例

```
http(s)://[Endpoint]/?Action=ConsoleCommonRegionData &PreventCache=10000
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Connect管理

###### ConsoleConnectCreate

Connect实例创建接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 否 | 10000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据。 |
| ClusterNa me | Strin g | Query | 是 | testCluster**** | RocketMQ v5.0集群名称。 |
| InstanceId | Strin g | Query | 是 | MQ INST 13674****** B _ _ _ mioMmJ0 | RocketMQ v5.0实例ID。 |

**返回数据**

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | True | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleConnectCreate &OnsRegionId=region123 &ClusterName=testCluster**** &InstanceId=MQ_INST_13674******_BmioMmJ0
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

###### ConsoleConnectList

Connect实例列表查询接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 实例所属的地域ID。 |

|  | 消息队列 |  |  |  | Roc | ketMQ v5.0开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OnsRegio nId | Strin g | Query | 是 | region123 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 否 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConsoleConnectList &OnsRegionId=region123
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"AF9A8B10-C426-530F-A0DD-96320B39****",
 "Message":"success",
 "Data":"{}",
 "Code":200,
 "Success":true
}
```

##### Router Task管理

消息队列

###### ConsoleStopCloudRouterTask

停止云路由器任务的控制台操作

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudRout erTaskId | Strin g | Query | 否 | ONS xxx 23424we _ _ | 任务id |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 请求是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleStartCloudRouterTask

启动云路由器任务的控制台操作

**请求头**

消息队列该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudRout erTaskId | Strin g | Query | 否 | ONS xxx ewwr3423 _ _ | 任务id |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 请求是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleQueryCloudRouterTask

查询云路由器任务的控制台操作

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudRout erTaskId | Strin g | Query | 否 | 任务id | 路由任务id |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleQueryStatsCloudRouterTask

查询云路由器统计信息的任务

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudRout erTaskId | Strin g | Query | 否 | ONS xxxxx qd34322 _ _ | 任务id |
| FromDate | Long | Query | 是 | 1560134212326 | 开始时间。 |
| ToDate | Long | Query | 是 | 1560134212326 | 结束时间。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleQueryItemsCloudRouterTask

消息队列查询云路由器相关配置项的任务

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudId | Strin g | Query | 否 | 1 | 云实例ID。 |
| QueryRegi onId | Strin g | Query | 否 | cn-hangzhou-01 | 查询的路由区域id |
| InstanceId | Strin g | Query | 否 | MQ INST 13674448591 _ _ 52433 **** _ | 实例的ID。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |

| 消息队列 |  |  | RocketMQ v5.0开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleListInPageCloudRouterTask

分页查询云路由器列表的任务

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CurrentPa ge | Integ er | Query | 是 | 1 | 当前页的页码。 |
| PageSize | Integ er | Query | 是 | 10 | 分页大小，每页最多显示的返回结果数量。 取值范围：10~200。 若您设置的参数值小于10， 则系统默认按照参数值为10 处理；若您设置的参数值大于200，则系统默认按照参数值为200处理。 |
| TaskKey | Strin g | Query | 否 | taskKey | taskKey。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

消息队列

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleDeleteCloudRouterTask

删除云路由器的控制台任务

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudRout erTaskId | Strin g | Query | 否 | 111 | 消息路由id |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 请求状态。 |
| Code | Integer | 200 | 返回码 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

###### ConsoleCreateCloudRouterTask

创建云路由器的控制台异步任务

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SrcCloudI d | Strin g | Host | 是 | 1 | 表示源端云平台的唯一标识符，用于区分不同的云服务提供商或云实例。 |
| DesCloudI d | Strin g | Host | 是 | 2 | 目标云平台的唯一标识符， 用于区分不同的云服务提供商或云环境。 |
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |

消息队列

| 参数名称 | 类型 | 位置 |  | 是否必选 | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|
| TaskDesc | Strin g | Query |  | 否 | task-desc |  | 任务描述。 |  |
| TaskKey | Strin g | Query |  | 否 | taskKey |  | taskKey。 |  |
| FilterType | Strin g | Query |  | 否 | Tag |  | 消息过滤类型。 |  |
| FilterRule | Strin g | Query |  | 否 | {"field":"status","operat or":"=","value":"active"} |  | 用于筛选。 |  |
| FilterProp erty | Strin g | Query |  | 否 | Date |  | 用于过滤字段的条件。 |  |
| SrcTopic | Strin g | Query |  | 是 | test |  | 源Topic，即被订阅的 Topic。 如， SrcTopic.1=/x7aW |  |
|  |  |  |  |  |  |  |  | SrcTopic.1=/x7aW |
|  |  |  |  |  |  |  | KW9****/testDataToDat |  |
|  |  |  |  |  |  |  | aHub/user/update |  |
| SrcRegion | Strin g | Query |  | 是 | cn-beijing |  | 实例所在地域。 |  |
| SrcInstanc eId | Strin g | Query |  | 否 | rm-2ze1jdv45i7l6**** |  | 源项目ID。 |  |
| DesTopic | Strin g | Query |  | 是 | des-topic |  | topic名称。 |  |
| DesRegio n | Strin g | Query |  | 是 | SG |  | 地域。 |  |
| DesInstan ceId | Strin g | Query |  | 否 | inst123456 |  | 目标实例的唯一标识符，用于指定操作的具体实例。 |  |
| OffsetFro mType | Strin g | Query |  | 是 | 256 |  | 表示从基准位置偏移500个单位的类型标识。 |  |
| OffsetFro mGroupId | Strin g | Query |  | 否 | 1001 |  | 表示从组ID为1001的元素开始计算偏移量。 |  |
| OffsetFro mTimesta mp | Long | Query |  | 否 | 1630425600000 |  | 表示从该时间戳开始的偏移量，通常用于标记某个时间点的起始位置。 |  |
| ConnectCl usterId | Strin g | Query |  | 是 | cluster-xxx |  | connect集群id |  |

**返回数据**

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 请求状态。 |
| Code | Integer | 200 | 返回码 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |
| Total | Long | 1 | 总数。 |

##### CloudInfo管理

###### ConsoleUpdateCloudInfo

更新控制台中的云服务配置或状态信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudNam e | Strin g | Query | 否 | 212e | 云实例名称。 |
| AddRegio nId | Strin g | Query | 否 | 1001 | 表示新增的区域ID，用于标识新加入的地理区域或服务范围。 |

| R | ocketMQ v5. | 0开发指南 | ·API参考 |  |  | 消息队列 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CloudId | Strin g | Query | 是 | ffe1********6d6d | 云实例ID。 |
| Ak | Strin g | Query | 否 | LTAIpY33******** | AccessKeyId。 |
| Sk | Strin g | Query | 否 | 123456 | SecretKeyId。 |
| MqEndPoi nt | Strin g | Query | 否 | http://nameserverAddr | 表示本地主机上的消息队列服务端点，常用于开发环境中的消息通信。 |
| ConsoleEn dPoint | Strin g | Query | 否 | http://consoleAddr/pop | 控制台服务的终端接入点地址。 |
| Remark | Strin g | Query | 否 | xxxx | 更新后的消费者分组的备注信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 返回码 |
| Message | String | success | 附加信息。 |
| Data | String | {} | 返回数据。 |

###### ConsoleQueryCloudInfo

查询云平台相关信息的控制台操作指令

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

消息队列

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CurrentPa ge | Integ er | Query | 是 | 1 | 当前页的页码。 |
| PageSize | Integ er | Query | 是 | 10 | 分页大小，每页最多显示的返回结果数量。 取值范围：10~200。 若您设置的参数值小于10， 则系统默认按照参数值为10 处理；若您设置的参数值大于200，则系统默认按照参数值为200处理。 |
| CloudInfo Key | Strin g | Query | 否 | 111 | 唯一标识符。 |
| OnsSessio nId | Strin g | Query | 否 | abc123xyz | 表示在消息队列ONS服务中标识一次客户端会话的唯一 ID，用于维护生产者或消费者的连接状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

| R | ocketMQ v5.0开发 | 指南·API参考 |  | 消息队列 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Total | Long | 1 | 总数。 |

###### ConsoleDeleteCloudInfo

删除云平台相关信息的操作指令

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 是 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudId | Strin g | Query | 是 | 1 | 云实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 返回码 |
| Message | String | success | 附加信息。 |
| Data | String | {} | 返回数据。 |

消息队列

###### ConsoleCreateCloudInfo

创建云资源时在控制台中填写的云服务配置信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OnsRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | Ons服务的区域标识符，用于指定消息服务的地域节点。 |
| PreventCa che | Long | Query | 否 | 1000 | 指示客户端和代理服务器不应缓存响应内容，强制每次请求都从服务器获取最新数据 |
| CloudNam e | Strin g | Query | 是 | cloud-test | 云实例名称。 |
| AddRegio nId | Strin g | Query | 是 | cn-hangzhou-01 | 表示新增的区域ID，用于标识新加入的地理区域或服务范围。 |
| Ak | Strin g | Query | 是 | LTAIpY33******** | AccessKeyId。 |
| Sk | Strin g | Query | 是 | 123456 | SecretKeyId。 |
| MqEndPoi nt | Strin g | Query | 是 | http://nameserv | 表示本地主机上的消息队列服务端点，常用于开发环境中的消息通信。 |
| ConsoleEn dPoint | Strin g | Query | 是 | http://consoleAddr/pop | 控制台服务的终端接入点地址。 |
| Remark | Strin g | Query | 是 | xxxx | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

消息队列

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AF9A8B10-C426- 530F-A0DD- 96320B39**** | 请求ID，每个请求的ID都是唯一的，可用于排查和定位问题。 |
| Success | Boolean | true | 执行结果是否成功。 |
| Code | Integer | 200 | 返回码 |
| Message | String | success | 返回信息。 |
| Data | String | {} | 返回数据。 |

消息队列

## SDK参考

### RocketMQ v5.0_SDK

#### 概述

消息队列 RocketMQ v5.0 版（简称RocketMQ v5.0）是分布式系统中重要的组件，主要解决系统解耦、 异步消息、削峰填谷等问题，实现高性能、高可用、可伸缩和最终一致性架构。 本参考规定RocketMQ v5.0应用节点与消息队列服务中心间数据传输服务管理方法，包括服务遵循的规范，以及服务管理相关的公共API。 本参考适用于使用RocketMQ v5.0 Java SDK，基于TCP协议进行消息传输的场景。

#### 消息模型

RocketMQ v5.0支持发布/订阅模型，发布者可以将一条消息发送至消息服务端，多个接收方进行订阅。如下图： 图 1. Pub-Sub模型

#### 传输协议与字符编码

RocketMQ v5.0 SDK底层通过TCP协议提供服务，用户请求和响应的字符编码都是采用UTF-8编码。

**传输层加密**

RocketMQ v5.0实例支持TLS v1.2及以上版本的传输层安全性协议，您可以通过SDK的配置来决定是否使用加密的传输层链接。
**配置方式：**在启动客户端程序时，设置JVM属性来决定是否使用加密的传输层链接。启动命令为**java -**
**Dtls.enable=true**。默认情况下，TLS链接不开启，设置为true将启用加密的传输层链接。

#### 常用类及其方法

消息队列

##### 常量类PropertyKeyConst

该类字段主要包括以下内容。

| 名称 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| AccessKey | String | - | 您在阿里云账号管理控制台中创建的 AccessKey ID，用于身份认证。 |
| SecretKey | String | - | 您在阿里云账号管理控制台中创建的 AccessKey Secret，用于身份认证。 |
| OnsChannel | String | ALIYUN | 用户渠道，阿里云：ALIYUN，聚石塔用户：CLOUD。 |
| NAMESRV ADDR _ | String | - | 设置RocketMQ v5.0 TCP协议接入点。 |
| GROUP ID _ | String | - | 标识一类Producer或Consumer，您在RocketMQ v5.0控制台创建的Group ID。 |
| MessageModel | String | CLUSTERING | 设置Consumer实例的消费模式，集群消费：CLUSTERING，广播消费： BROADCASTING。 |
| ConsumeThreadNums | String | 64 | 消费线程数量。 |
| MaxReconsumeTimes | String | 16 | 设置消息消费失败的最大重试次数。 |
| ConsumeTimeout | String | 15 | 设置每条消息消费的最大超时时间，超过设置时间则被视为消费失败，等下次重新投递再次消费。每个业务需要设置一个合理的值，单位（分钟）。 |
| ConsumeMessageBatc hMaxSize | String | 1 | BatchConsumer每次批量消费的最大消息数量，默认值为1，允许自定义范围为[1, 32]，实际消费数量可能小于该值。 |
| CheckImmunityTimeIn Seconds | String | 30 | 设置事务消息第一次回查的最快时间，单位 （秒）。 |
| shardingKey | String | - | 顺序消息中用来计算不同分区的值。 |

消息队列

| suspendTimeMillis | String | 3000 | 只适用于顺序消息，设置消息消费失败的重试间隔时间，单位（毫秒）。 |
|---|---|---|---|

##### 工厂类ONSFactory

###### createConsumer

语法：static Consumer createConsumer(Properties properties) 描述：创建RocketMQ v5.0普通消息、定时和延时消息、分布式事务消息等消息类型的消费者实例。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| properties | Properties | 详情参考PropertyKeyConst说明。 必填属性：PropertyKeyConst.NAMESRV ADDR、 _ PropertyKeyConst.ConsumerId、 PropertyKeyConst.AccessKey、 PropertyKeyConst.SecretKey。 可选属性：PropertyKeyConst.ConsumeThreadNums、 PropertyKeyConst.ConsumeTimeout。 |

返回值

| 类型 | 描述 |
|---|---|
| Consumer | RocketMQ v5.0普通消息、定时和延时消息、分布式事务消息等消息类型的消费者实例。 |

###### createBatchConsumer

语法：static BatchConsumer createBatchConsumer(Properties properties) 描述：创建RocketMQ v5.0批量消费者实例。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| properties | Properties | 详情参考PropertyKeyConst说明; 必填属性：PropertyKeyConst.NAMESRV ADDR、 _ PropertyKeyConst.GROUP ID、 _ PropertyKeyConst.AccessKey、 PropertyKeyConst.SecretKey； 可选属性：PropertyKeyConst.ConsumeThreadNums、 PropertyKeyConst.ConsumeTimeout、 PropertyKeyConst.ConsumeMessageBatchMaxSize。 |

消息队列返回值：

| 类型 | 描述 |
|---|---|
| BatchConsumer | BatchConsumer |

###### createOrderedConsumer

语法：static OrderConsumer createOrderedConsumer(Properties properties) 描述：创建RocketMQ v5.0顺序消息消费者。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| properties | properties | 详情参考PropertyKeyConst说明； 必填属性：PropertyKeyConst.NAMESRV ADDR、 _ PropertyKeyConst.GROUP ID、PropertyKeyConst.AccessKey、 _ PropertyKeyConst.SecretKey； 可选属性：PropertyKeyConst.ConsumeThreadNums、 PropertyKeyConst.ConsumeTimeout。 |

返回值：

| 类型 | 描述 |
|---|---|
| OrderConsumer | RocketMQ v5.0顺序消息消费者实例 |

###### createOrderProducer

语法：static OrderProducer createOrderProducer(Properties properties) 描述：创建RocketMQ v5.0顺序消息发布者。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| properties | Properties | 详情参考PropertyKeyConst说明; 必填属性：PropertyKeyConst.NAMESRV ADDR、 _ PropertyKeyConst.GROUP ID、 _ PropertyKeyConst.AccessKey、 PropertyKeyConst.SecretKey、 PropertyKeyConst.ShardingKey； 可选属性：PropertyKeyConst.SendMsgTimeoutMillis |

返回值： 消息队列

| 类型 | 描述 |
|---|---|
| OrderProducer | RocketMQ v5.0顺序消息发布者实例 |

###### createProducer

语法：static Producer createProducer(Properties properties) 描述：创建RocketMQ v5.0普通消息、定时和延时消息发布者。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| properties | Properties | 详情参考PropertyKeyConst说明。 必填属性：PropertyKeyConst.NAMESRV ADDR、 _ PropertyKeyConst.GROUP ID、 _ PropertyKeyConst.AccessKey、 PropertyKeyConst.SecretKey。 可选属性：PropertyKeyConst.SendMsgTimeoutMillis。 |

返回值：

| 类型 | 描述 |
|---|---|
| Producer | RocketMQ v5.0普通消息、定时和延时消息发布者实例。 |

###### createTransactionProducer

语法：static TransactionProducer createTransactionProducer(Properties properties, LocalTransactionChecker checker) 描述：创建RocketMQ v5.0分布式事务消息发布者。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| properties | Properties | 详情参考PropertyKeyConst说明; 必填属性：PropertyKeyConst.NAMESRV ADDR、 _ PropertyKeyConst.GROUP ID、 _ PropertyKeyConst.AccessKey、 PropertyKeyConst.SecretKey； 可选属性：PropertyKeyConst.SendMsgTimeoutMillis、 PropertyKeyConst.CheckImmunityTimeInSeconds。 |

消息队列

| checker | LocalTransactionC hecker | 详情参考LocalTransactionChecker说明。 |
|---|---|---|

返回值：

| 类型 | 描述 |
|---|---|
| TransactionProducer | RocketMQ v5.0分布式事务消息发布者实例 |

##### 消息类Message

###### 消息类Message概述

消息类，表示要发送的消息。一条合法的消息，应包含主题(Topic)，消息体以及可选的标签和业务标识。 注意：我们对每条消息的自定义键值对的长度没有限制，但所有的自定义键值对，系统键值对序列化后，所占空间不能超过32767字节。

###### Message默认构造方法

语法：Message() 描述：默认构造函数，创建消息对象。 参数：无

###### Message有参构造方法（一）

语法：public Message(String topic, String tag, String key, byte body) 描述：有参构造函数，创建消息对象。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| topic | String | 消息主题，最长不超过255个字符；由a-z, A-Z, 0-9，以及中划线"-"和下划线" "构成。 _ |
| tag | String | 消息标签，请使用合法标识符，尽量简短且见名知意。 |
| key | String | 业务标识。 |
| body | byte | 消息体，消息体长度默认不超过4 MB（包含消息属性，其中消息属性不超过8 KB），具体请参阅集群部署文档描述。 |

###### Message有参构造方法（二）

语法：public Message(String topic, String tags, byte body) 描述：有参构造函数，创建消息对象。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|

消息队列

| topic | String | 消息主题，最长不超过255个字符；由a-z, A-Z, 0-9，以及中划线"- "和下划线" "构成。 _ |
|---|---|---|
| tags | String | 消息标签，请使用合法标识符，尽量简短且见名知意。 |
| body | byte | 消息体，消息体长度默认不超过4 MB（包含消息属性，其中消息属性不超过8 KB），具体请参阅集群部署文档描述。 |

###### putUserProperties

语法：public void putUserProperties(String key, String value) 描述：添加用户自定义属性键值对; 该键值对在消费消息时可被获取。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| key | String | 自定义属性键。 |
| value | String | 自定义属性值。 |

返回值：无

###### getUserProperties

语法：public String getUserProperties(String key) 描述：获取用户自定义属性的值。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| key | String | 自定义属性键。 |

返回值：

| 类型 | 描述 |
|---|---|
| String | 用户自定义属性值 |

###### getTopic

描述：获取消息的主题。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 消息主题 |

###### setTopic

消息队列描述：设置消息主题。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| topic | String | 消息主题 |

返回值：无

###### getTag

描述：获取消息标签。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 消息标签 |

###### setTag

描述：设置消息标签。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| tag | String | 消息标签 |

返回值：无

###### getKey

描述：获取业务标识。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 业务标识 |

###### setKey

描述：设置业务标签。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|

消息队列

| key | String | 业务标识 |
|---|---|---|

返回值：无

###### getMsgID

描述：获取消息ID。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 消息ID |

###### setMsgID

描述：设置消息ID 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| msgid | String | 消息ID |

返回值：无

###### getReconsumeTimes

描述：消息消费时，获取消息已经被重试消费的次数。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 重试消费次数 |

###### setReconsumeTimes

描述：设置消息重试消费次数。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| value | int | 重试消费次数 |

返回值：无消息队列

###### getBornTimestamp

描述：获取消息的生产时间。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 消息的生产时间 |

###### setBornTimestamp

描述：设置消息的产生时间。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| value | long | 消息生产时间。 |

返回值：无

###### getBornHost

描述：获取产生消息的主机。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 产生消息的主机 |

###### setBornHost

描述：设置生产消息的主机。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| value | long | 生产消息的主机。 |

返回值：无

###### getStartDeliverTime

消息队列描述：获取定时消息开始投递时间。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 定时消息开始投递时间 |

###### setStartDeliverTime

语法：public void setStartDeliverTime(long value) 描述：设置消息的定时投递时间（绝对时间)，最大延迟时间为40天。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| value | long | 定时消息的开始投递时间。 |

返回值：无

###### getShardingKey

描述：获取顺序消息中用来计算不同分区的值。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 顺序消息中用来计算不同分区的值 |

###### setShardingKey

描述：设置顺序消息中用来计算不同分区的值。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| String | long | 顺序消息中用来计算不同分区的值。 |

返回值：无

##### 异常类ONSClientException

###### ONSClientException默认构造方法

语法：public ONSClientException() 描述：默认异常构造函数。 参数：无消息队列

###### ONSClientException有参构造方法（一）

语法：public ONSClientException(String message) 描述：异常接口构造函数。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | String | 需要向外传递的异常信息 |

###### ONSClientException有参构造方法（二）

语法：public ONSClientException(Throwable cause) 描述：异常接口构造函数。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | String | 需要向外传递的异常信息 |

###### ONSClientException有参构造方法（三）

语法：public ONSClientException(String message, Throwable cause) 描述：异常接口构造函数。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | String | 需要向外传递的异常信息 |
| cause | Throwable | 需要向外传递的异常信息 |

##### 发送消息接口

###### 发送消息接口概述

本单元主要详述RocketMQ发送各种类消息的接口规范。不同消息类型与各个接口、参数的对应关系如下图所示。 图 1. 发布消息相关接口参数说明消息队列

###### 发送结果SendResult

###### SendResult默认构造方法

语法：public SendResult() 描述：默认构造函数，创建消息发送结果对象。 参数：无

###### getMessageId

描述：获取被发送消息的消息 ID。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 被发送消息的消息 ID |

###### getTopic

描述：获取被发送消息的消息主题。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| String | 被发送消息的消息主题 |

###### toString

描述：序列化发送结果。 参数：无消息队列返回值：

| 类型 | 描述 |
|---|---|
| String | 发送结果的String表示 |

###### 生产者实例Producer

###### 生产者实例Producer概述

发布者对象，可以通过该对象接口发送普通消息，发送定时/延时消息。 线程安全性: 本接口的实现类都是线程安全的，可以多线并发发送消息。 一个实例可以发送多个主题的消息。 正常情况下，一个实例足够高效完成本模块的发送任务，无需创建多个实例 RocketMQ普通消息支持3种发送方式：可靠同步发送、可靠异步发送、单向（Oneway）发送。

###### send

语法：public SendResult send(Message message) 描述：同步发送消息，只要不抛异常就表示成功；支持普通消息，发送定时/延时消息。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | Message | 要发送的消息对象 |

返回值：

| 类型 | 描述 |
|---|---|
| SendResult | 发送结果，含消息Id，消息主题等 |

###### sendOneway

描述：发送消息，Oneway形式，服务器不应答，无法保证消息是否成功到达服务器；支持普通消息，发送定时/延时消息。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | Message | 要发送的消息对象 |

返回值：无

###### sendAsync

语法：public void sendAsync(Message message, SendCallback sendCallback) 描述：发送消息，异步Callback形式；支持普通消息，发送定时/延时消息。 参数： 消息队列

| 名称 | 类型 | 描述 |
|---|---|---|
| message | Message | 要发送的消息对象 |
| sendCallback | SendCallback | 发送完成要执行的回调函数 |

返回值：无

###### isStarted

描述：检查服务是否已经启动。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果检查服务已经启动返回 true; 其它情况返回 false |

###### isClosed

描述：检查服务是否已经关闭。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果服务已关闭返回 true; 其它情况返回 false |

###### start

描述：启动消息发送 Producer 服务。 参数：无返回：无

###### shutdown

描述：关闭消息发送 Producer 服务。 参数：无返回：无

###### 分布式事务消息生产者实例

**TransactionProducer**

###### send

消息队列语法：SendResult send(Message message, LocalTransactionExecuter executer, Object arg) 描述：该方法用来发送一条事务型消息。事务型消息发送分为三个步骤： 本服务实现类首先发送一条半事务消息到消息服务器; 通过executer执行本地事务; 根据上一步骤执行结果, 决定发送提交或者回滚第一步发送的半事务消息; 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | Message | 要发送的事务型消息 |
| executer | LocalTransactionExecuter | 本地事务执行器，详情请参考 LocalTransactionExecuter类说明 |
| arg | Object | 应用自定义参数，该参数可以传入本地事务执行器 |

返回值：

| 类型 | 描述 |
|---|---|
| SendResult | 返回发送结果，含消息Id, 消息主题等 |

###### isStarted

描述：检查服务是否已经启动。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果检查服务已经启动返回 true; 其它情况返回 false |

###### isClosed

描述：检查服务是否已经关闭。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果服务已关闭返回 true; 其它情况返回 false |

###### start

描述：启动事务消息发送 Producer 服务。 参数：无消息队列返回值：无

###### shutdown

描述：关闭事务消息发送 Producer 服务。 参数：无返回值：无

###### 本地事务执行器LocalTransactionExecuter

语法：TransactionStatus execute(Message msg, Object arg) 描述：执行本地事务，由应用来重写； 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | Message | 要发送的事务型消息 |
| arg | Object | 应用自定义参数，由send方法传入并回调 |

返回值：

| 类型 | 描述 |
|---|---|
| TransactionStatus | 返回事务执行结果，包括提交事务、回滚事务、未知状态 |

###### 分布式事务消息状态TransactionStatus

分布式事务半消息的状态，包括提交事务、回滚事务、未知状态。 枚举：

| 取值 | 描述 |
|---|---|
| CommitTransaction | 提交事务，对应的事务消息将投递给消费者 |
| RollbackTransaction | 回滚事务，对应的事务消息会被删除，不会投递给消费者 |
| Unknow | 未知状态，一般在用户无法确定事务是成功还是失败时使用，对于未知状态的事务，服务端会定期进行事务回查 |

###### 顺序消息生产者实例OrderProducer

###### send

语法：SendResult send(Message message, String shardingKey) 描述：发送顺序消息。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|

消息队列

| message | Message | 要发送的顺序消息对象。 |
|---|---|---|
| shardingKey | String | 顺序消息选择因子，发送方法基于 shardingKey 选择具体的消息队列。 |

返回值：

| 类型 | 描述 |
|---|---|
| SendResult | 发送结果。含消息ID、消息主题等。 |

###### isStarted

描述：检查服务是否已经启动。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果检查服务已经启动返回 true; 其它情况返回 false |

###### isClosed

描述：检查服务是否已经关闭。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果服务已关闭返回 true; 其它情况返回 false |

###### start

描述：启动顺序消息消息发送Producer服务。 参数：无返回：无

###### shutdown

描述：关闭顺序消息发送Producer服务。 参数：无返回：无

##### 订阅消息接口

消息队列

###### 订阅消息接口概述

本节详述RocketMQ订阅各种类消息的接口规范。不同消息类型与各个接口、参数的对应关系如下图所示。

###### 消费者实例Consumer

###### 消费者实例Consumer概述

消息消费者实例，用来订阅消息，支持普通消息、事务消息、定时消息/延时消息。

###### subscribe

语法：public void subscribe(String topic, String subExpression, MessageListener listener) 描述：订阅消息，包括普通消息、事务消息、定时消息/延时消息。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| topic | String | 消息主题 |
| subExpression | String | 订阅过滤表达式字符串，RocketMQ服务器依据此表达式进行过滤，只支持或 (\|\|) 运算； 示例1："tag1 \|\| tag2 \|\| tag3"； 示例2：subExpression 等于 null 或者 * ，则表示全部订阅； |
| listener | MessageListener | 消息回调监听器 |

返回值：无

###### unsubscribe

参数： 消息队列

| 名称 | 类型 | 描述 |
|---|---|---|
| topic | String | 消息主题 |

返回值：无

###### isStarted

描述：检查服务是否已经启动。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果检查服务已经启动返回 true; 其它情况返回 false |

###### isClosed

描述：检查服务是否已经关闭。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果服务已关闭返回 true; 其它情况返回 false |

###### start

参数：无返回值：无

###### shutdown

参数：无返回值：无

###### 消息监听器MessageListener

###### 消费监听器MessageListener概述

线程安全性要求：该接口会被Consumer的多个线程并发调用, 用户需要保证并发安全性消息队列

###### consume

语法：Action consume(Message message, ConsumeContext context) 描述：消费消息接口，由应用来实现；网络抖动等不稳定的情形可能会带来消息重复，对重复消息敏感的业务可对消息做幂等处理。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | Message | 消息对象 |
| context | ConsumeContext | 消费上下文，具体参考 ConsumeContext 说明 |

返回值：

| 类型 | 描述 |
|---|---|
| Action | 消费结果。 消费失败：如果应用抛出异常或者返回Null等价于返回Action.ReconsumeLater； 消费成功：返回 Action.CommitMessage。 |

###### 消息消费结果Action

###### 消息消费结果Action概述

消费消息的返回结果。 枚举：

| 名称 | 类型 | 描述 |
|---|---|---|
| CommitMessage | String | 消费成功，继续消费下一条消息 |
| ReconsumeLater | String | 消费失败，告知服务器稍后再投递这条消息，继续消费其他消息 |

###### valueOf

描述：返回带有指定名称的该类型的枚举常量，字符串必须与用于声明该类型的枚举常量的标识符完全匹配；（不允许有多余的空格字符）。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| name | String | 要返回的枚举常量的名称 |

返回值：

| 类型 | 描述 |
|---|---|

消息队列

| Action | 返回带有指定名称的枚举常量 |
|---|---|

异常：

| 类型 | 描述 |
|---|---|
| IllegalArgumentException | 如果该枚举类型没有带有指定名称的常量 |
| NullPointerException | 如果参数为空值 |

###### values

描述：按照声明该枚举类型常量的顺序, 返回包含这些常量的数组。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| Action[] | 按照声明该枚举类型的常量的顺序返回的包含这些常量的数组 |

###### 消费模式PropertyValueConst

消费模式常量类。 枚举：

| 名称 | 类型 | 描述 |
|---|---|---|
| BROADCASTING | String | 广播消费模式 |
| CLUSTERING | String | 集群消费模式 |

###### 顺序消费者实例OrderConsumer

###### 顺序消费者实例OrderConsumer概述

顺序消息消费者实例，通过改对象的接口可以先进先出的方式进行顺序订阅。

###### subscribe

语法：void subscribe(String topic, String subExpression, MessageOrderListener listener) 描述：订阅顺序消息。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| topic | String | 消息主题 |

消息队列

| subExpression | String | 订阅过滤表达式字符串，RocketMQ服务器依据此表达式进行过滤， 只支持或 (\|\|) 运算； 示例1: "tag1 \|\| tag2 \|\| tag3"； 示例2：subExpression 等于null或者*，则表示全部订阅； |
|---|---|---|
| listener | MessageOrd erListener | 消息回调监听器 |

返回值：无

###### unsubscribe

参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| topic | String | 消息主题 |

返回值：无

###### isStarted

描述：检查服务是否已经启动。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果检查服务已经启动返回 true; 其它情况返回 false |

###### isClosed

描述：检查服务是否已经关闭。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果服务已关闭返回 true; 其它情况返回 false |

###### start

参数：无消息队列返回值：无

###### shutdown

参数：无返回：无

###### 消息监听器MessageOrderListener

###### 消息监听器MessageOrderListener概述

线程安全性要求：该接口会被Consumer的多个线程并发调用, 用户需要保证并发安全性

###### consume

语法：OrderAction consume(Message message, ConsumeOrderContext context) 描述：消费消息接口，由应用来实现；网络抖动等不稳定的情形可能会带来消息重复，对重复消息敏感的业务可对消息做幂等处理。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | Message | 消息对象 |
| context | ConsumeOrderContext | 消费上下文，具体参考 ConsumeOrderContext 说明； |

返回值：

| 类型 | 描述 |
|---|---|
| OrderAction | 消费结果。 消费失败：如果应用抛出异常或者返回Null等价于返回 Action.Suspend； 消费成功：返回Action.Success。 |

###### 顺序消息消费结果OrderAction

###### 顺序消息消费结果OrderAction概述

顺序消息消费消息的返回结果。 枚举：

| 名称 | 类型 | 描述 |
|---|---|---|
| Success | String | 消费成功，继续消费下一条消息 |
| Suspend | String | 消费失败，挂起当前队列 |

消息队列

###### valueOf

语法：public static OrderAction valueOf(String name) 描述：返回带有指定名称的该类型的枚举常量，字符串必须与用于声明该类型的枚举常量的标识符完全匹配；（不允许有多余的空格字符）。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| name | String | 要返回的枚举常量的名称 |

返回值：

| 类型 | 描述 |
|---|---|
| OrderAction | 返回带有指定名称的枚举常量 |

异常：

| 类型 | 描述 |
|---|---|
| IllegalArgumentException | 如果该枚举类型没有带有指定名称的常量 |
| NullPointerException | 如果参数为空值 |

###### values

描述：按照声明该枚举类型常量的顺序, 返回包含这些常量的数组。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| OrderAction[] | 按照声明该枚举类型的常量的顺序返回的包含这些常量的数组 |

###### 批量消费者实例BatchConsumer

###### 批量消费者实例BatchConsumer概述

批量消息消费者，用来通过批量的方式订阅消息。

###### subscribe

语法：void subscribe(String topic, String subExpression, BatchMessageListener listener) 描述：订阅消息，包括普通消息、事务消息、定时消息/延时消息。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| topic | String | 消息主题 |

消息队列

| subExpression | String | 订阅过滤表达式字符串，RocketMQ服务器依据此表达式进行过滤， 只支持或 (\|\|) 运算； 示例1: "tag1 \|\| tag2 \|\| tag3"； 示例2：subExpression等于null或者*，则表示全部订阅； |
|---|---|---|
| listener | BatchMess ageListener | 消息回调监听器 |

返回值：无

###### unsubscribe

参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| topic | String | 消息主题 |

返回值：无

###### isStarted

描述：检查服务是否已经启动。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果检查服务已经启动返回 true; 其它情况返回 false |

###### isClosed

描述：检查服务是否已经关闭。 参数：无返回值：

| 类型 | 描述 |
|---|---|
| boolean | 如果服务已关闭返回 true; 其它情况返回 false |

###### start

参数：无消息队列返回：无

###### shutdown

参数：无返回：无

###### 批量消费消息监听器BatchMessageListener

###### 批量消费消息监听器

**BatchMessageListener概述**

线程安全性要求：该接口会被Consumer的多个线程并发调用, 用户需要保证并发安全性。

###### consume

语法：Action consume(Message message, ConsumeContext context) 描述：批量消费消息接口，由应用来实现需要注意网络抖动等不稳定的情形可能会带来消息重复，对重复消息敏感的业务可对消息做幂等处理。 参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| message | Message | 消息对象 |
| context | ConsumeContext | 消费上下文，具体参考 ConsumeContext 说明 |

返回值：

| 类型 | 描述 |
|---|---|
| Action | 消费结果。 消费失败：如果应用抛出异常或者返回Null等价于返回Action.ReconsumeLater； 消费成功：返回 Action.CommitMessage； |
