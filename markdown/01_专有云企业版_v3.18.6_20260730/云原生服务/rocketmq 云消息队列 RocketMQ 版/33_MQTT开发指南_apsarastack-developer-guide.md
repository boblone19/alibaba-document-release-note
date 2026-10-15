---
title: "云消息队列 RocketMQ 版 MQTT开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 36
source_pdf: "33_MQTT开发指南_apsarastack-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/rocketmq/zh/apsarastack-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云消息队列 RocketMQ 版 MQTT开发指南

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
| 获取MQTT的Endpoint 获取MQTT的SDK包调用API |  |

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
您需要查看目标云产品的开发指南，了解API的功能与使用方式，查找开发指南的方式请参见开发文档使用说明。
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
2. 单击顶部菜单栏**产品**，选择**开发者工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，
调用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发者工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源
集ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节ListResourceGroup。 消息队列

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以API网关为例， 获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品** > **中间件** > **消息队列** > **微消息队列** **MQTT** 版。
3. 在左侧导航栏中，单击**实例详情**。
4. 在实例列表中查看**实例****ID**。

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

`/**`以下示例演示如何使用`STS Token`初始化凭据客户端（不包含如何获取到`STS Token`的过程）。`*/`

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

### Java版本

**环境要求**

支持 JDK8~JDK19，平台支持：Linux、Mac、Windows。

**安装说明代码**

从开发者门户获取SDK包后可使用以下 Mavan 依赖配置进行管理：

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

**安装说明文档**

**开发者门户获取 SDK**

1.登录 ASCM 的开发者门户，单击 SDK 示例。 2.SDK 类型下拉选择高级版，选择 Java 语言。 3.下方可看到示例代码，点击下载完整工程以获取示例项目及 SDK 包。 消息队列

**导入 SDK 包**

1.通过以下任一方式创建 Maven 项目。 方式一：在 IDEA 中添加一个 Maven 项目。 方式二：将已有的项目转换为 Maven 项目。 右键单击要转换的项目，并选择**Add Framework Support** ...。 选择 Maven，并单击 OK。 2.在项目根目录下创建 lib 包，将 Java SDK 包放入到 lib 目录下，如下图。 3.在项目目录下的 pom.xml 中，添加 Java SDK 依赖，代码请参考上文中《安装说明代码》部分。 4.查看 IDEA 右侧 Maven 栏，如图所示，表示已成功导入依赖。 消息队列

**代码示例**

请参考示例，将某个 API 录入，注意保证代码通过，隐私信息泄露。

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
        headers.put("x-acs-organizationid", "<your-organizationid>");
```

`//` 资源组`id`

```
        headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>");
```

`//` 角色`id`

```
        headers.put("x-acs-roleId", "<your-roleId>");
        runtime.setExtendsParameters(new ExtendsParameters().setHeaders(headers));
```

`//` 支持通过运行时参数（`RuntimeOptions`）配置当前请求的代理，代理配置优先级：`RuntimeOption` 配置 `> Client`配置，根据需要选择一种即可。

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

`//` 该参数值为假设值，请您根据实际业务情况进行填写消息队列

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

**步骤示例**

1. 初始化配置对象 com.aliyun.teaopenapi.models.Config 。 Config 对象存放 AccessKeyId、
AccessKeySecret 、Endpoint 等配置，Endpoint 可以在ASCM的开发者门户查询。

```
Config config = new Config() .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")) .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
```

`//` 访问的域名

```
config.endpoint = "ecs-cn-hangzhou.aliyuncs.com";
```

2. 实例化一个客户端，从 com.aliyun.ecs20140526.Client 类生成对象 client 。后续 request、
response 从 com.aliyun.ons_inner20180205.models 口中获得。

```
Client client = new Client(config);
```

3. 创建对应 API 的 Request 。类的命名规则为 API 方法名加上 Request 。例如：

```
QueryInstanceListRequest request = new QueryInstanceListRequest();
```

4. 设置请求类 request 的参数。通过 request 类的属性设置必要的信息，即 API 中必须要提供的信息。
消息队列 request.SourceRegionId = "your_value"; // 该参数值为假设值，请您根据实际情况进行填写 request.RegionId = "your_value"; // 该参数值为假设值，请您根据实际情况进行填写
5. 通过 client 对象获得对应 request 响应 response 。

```java
ModifySecurityGroupRuleResponse response = client.modifySecurityGroupRule(request); System.out.println(new Gson().toJson(response.Body));
```

6. 调用 response 中对应的属性获得返回的参数值。假设您需要获取 requestId ：

```
String requestId = response.Body.requestId;
```

7. 使用 catch() 处理报错。

```
catch (Exception e) {
    e.printStackTrace();
}
```

### SDK概览

**概览**

文档中 SDK 关于 API 的示例代码仅供参考，各 API 的完整使用步骤与参数说明请参见开发者门户 SDK 示例和 OpenAPI 文档。

**SDK版本**

| 语言 | 版本号 | 发布时间 | 更新内容 |
|---|---|---|---|
| Java | 3.18.3-0 | 2024/11 | 全新发布专有云 3.18.3-0 对外 API 的 SDK。 |

**API列表**

当前 SDK 支持的 API 列表。

| API名称 | 所在版本 |
|---|---|
| BindMqttInstance | v3.18.6 |
| BindSystemTags | v3.18.6 |
| ChangeMqttInstanceSpec | v3.18.6 |
| CheckFortestConsumerId | v3.18.6 |
| CheckFortestInstance | v3.18.6 |
| CheckFortestRamAction | v3.18.6 |
| CheckFortestTopic | v3.18.6 |
| CreateCloudInfo | v3.18.6 |
| CreateCloudRouterTask | v3.18.6 |

|  | 消息队列 | MQTT 开发指南·通过POP网关调用专有云AP | I |
|---|---|---|---|

| API名称 | 所在版本 |
|---|---|
| CreateDeploymentMqConnector | v3.18.6 |
| CreateGroup | v3.18.6 |
| CreateInstance | v3.18.6 |
| CreateMqttGroupId | v3.18.6 |
| CreateMqttInstance | v3.18.6 |
| CreateMqttInstanceStoreResource | v3.18.6 |
| CreateTopic | v3.18.6 |
| CreateUnitResetTask | v3.18.6 |
| CreateVpcTunnelInstanceSingleTunnel | v3.18.6 |
| DeleteCloudInfo | v3.18.6 |
| DeleteCloudRouterTask | v3.18.6 |
| DeleteDeploymentMqConnector | v3.18.6 |
| DeleteGroup | v3.18.6 |
| DeleteInstance | v3.18.6 |
| DeleteMqttGroupId | v3.18.6 |
| DeleteMqttInstance | v3.18.6 |
| DeleteMqttInstanceStoreResource | v3.18.6 |
| DeleteTopic | v3.18.6 |
| DeleteTraceQueryTask | v3.18.6 |
| DeleteVpcTunnelInstanceSingleTunnel | v3.18.6 |
| DeployDeploymentMqConnector | v3.18.6 |
| DownloadMessage | v3.18.6 |
| DownloadMessageAllInDLQ | v3.18.6 |
| DownloadMessageBodyInDLQ | v3.18.6 |
| PageQueryCloudRouterTask | v3.18.6 |
| PageQueryGroupList | v3.18.6 |
| PageQueryMqttGroupId | v3.18.6 |
| PageQueryMqttInstanceList | v3.18.6 |

| MQTT 开发指南·通过POP网关调用专 | 消息队列 |
|---|---|

| API名称 | 所在版本 |
|---|---|
| PageQueryMqttInstanceStoreResource | v3.18.6 |
| PageQueryTopicList | v3.18.6 |
| PageQueryTraceListByUserId | v3.18.6 |
| PauseMqConnector | v3.18.6 |
| PushMessage | v3.18.6 |
| QueryAllConsumerAccumulation | v3.18.6 |
| QueryCloudInfo | v3.18.6 |
| QueryCloudInfoNoPage | v3.18.6 |
| QueryCloudRouterItems | v3.18.6 |
| QueryCloudRouterTask | v3.18.6 |
| QueryCloudRouterTaskStats | v3.18.6 |
| QueryClusterCapacity | v3.18.6 |
| QueryClusterList | v3.18.6 |
| QueryCommonGenRedirectUrl | v3.18.6 |
| QueryCommonRegionData | v3.18.6 |
| QueryConsumerAccumulate | v3.18.6 |
| QueryConsumerConnection | v3.18.6 |
| QueryConsumerJstackInfo | v3.18.6 |
| QueryConsumerProgress | v3.18.6 |
| QueryConsumerStatus | v3.18.6 |
| QueryConsumerTimespan | v3.18.6 |
| QueryEmpowerList | v3.18.6 |
| QueryGroupEmpowerList | v3.18.6 |
| QueryGroupIdList | v3.18.6 |
| QueryGroupList | v3.18.6 |
| QueryGroupSubDetail | v3.18.6 |
| QueryInstanceBaseInfo | v3.18.6 |
| QueryInstanceList | v3.18.6 |

| 消息队列 | MQTT 开发指南·通过POP网关调用专 |
|---|---|

| API名称 | 所在版本 |
|---|---|
| QueryInstanceStatistics | v3.18.6 |
| QueryMessageById | v3.18.6 |
| QueryMessageByIdInDLQ | v3.18.6 |
| QueryMessageByKey | v3.18.6 |
| QueryMessageByPagedDLQ | v3.18.6 |
| QueryMessageByPagedTopic | v3.18.6 |
| QueryMetaData | v3.18.6 |
| QueryMqConnectorDeploymentList | v3.18.6 |
| QueryMqConnectorInfoList | v3.18.6 |
| QueryMqConnectorMetricsDetailList | v3.18.6 |
| QueryMqConnectorSysResourceName | v3.18.6 |
| QueryMqttClientSetByGroupId | v3.18.6 |
| QueryMqttClientSetByTopic | v3.18.6 |
| QueryMqttConnectionSum | v3.18.6 |
| QueryMqttDeviceRunningInfo | v3.18.6 |
| QueryMqttGroupIdList | v3.18.6 |
| QueryMqttInstanceBaseInfo | v3.18.6 |
| QueryMqttInstanceList | v3.18.6 |
| QueryMqttInstanceReport | v3.18.6 |
| QueryMqttInstanceStoreInstanceList | v3.18.6 |
| QueryMqttInstanceStoreResourceNameList | v3.18.6 |
| QueryMqttMsgByPubInfo | v3.18.6 |
| QueryMqttMsgTransTask | v3.18.6 |
| QueryMqttTraceByTraceId | v3.18.6 |
| QueryPubTraceByQueryId | v3.18.6 |
| QueryRegionConsoleUrlList | v3.18.6 |
| QueryRegionList | v3.18.6 |
| QueryRouterInstanceList | v3.18.6 |

| MQTT 开发指南·通过POP网关调用专 | 消息队列 |
|---|---|

| API名称 | 所在版本 |
|---|---|
| QueryRouterTopicList | v3.18.6 |
| QuerySubscriptionList | v3.18.6 |
| QuerySystemTagList | v3.18.6 |
| QueryTopic | v3.18.6 |
| QueryTopicList | v3.18.6 |
| QueryTopicListByGroupId | v3.18.6 |
| QueryTopicNameList | v3.18.6 |
| QueryTopicStatus | v3.18.6 |
| QueryTopicSubDetail | v3.18.6 |
| QueryTraceByMsgId | v3.18.6 |
| QueryTraceByMsgKey | v3.18.6 |
| QueryTraceByMsgTopic | v3.18.6 |
| QueryTraceMapByQueryId | v3.18.6 |
| QueryTrendFlowLimit | v3.18.6 |
| QueryTrendGroupOutputTps | v3.18.6 |
| QueryTrendTopicInputTps | v3.18.6 |
| QueryUnitLatestConsumerTime | v3.18.6 |
| QueryUnitResetTask | v3.18.6 |
| QueryVpcTunnelInstanceSingleTunnelList | v3.18.6 |
| QueryVpcTunnelTunnelSwitch | v3.18.6 |
| ResendMessageByIdInDLQ | v3.18.6 |
| ResetConsumerOffset | v3.18.6 |
| ResumeMqConnector | v3.18.6 |
| SearchRouterTask | v3.18.6 |
| SearchSubscription | v3.18.6 |
| SendMessage | v3.18.6 |
| SendMqtt | v3.18.6 |
| StartCloudRouterTask | v3.18.6 |

| 消息队列 | MQTT 开发指南·通过POP网关调用专 |
|---|---|

| API名称 | 所在版本 |
|---|---|
| StopCloudRouterTask | v3.18.6 |
| TraceMessage | v3.18.6 |
| UnbindSystemTags | v3.18.6 |
| UpdateCloudInfo | v3.18.6 |
| UpdateCloudRouterTask | v3.18.6 |
| UpdateConsumerReadableByTopicAndGroup | v3.18.6 |
| UpdateGroupConsumer | v3.18.6 |
| UpdateGroupInfo | v3.18.6 |
| UpdateInstance | v3.18.6 |
| UpdateMqConnectorDeployment | v3.18.6 |
| UpdateMqttInstance | v3.18.6 |
| UpdateTopic | v3.18.6 |
| UpdateTopicInfo | v3.18.6 |

**可用性说明**

在之前版本曾提供过的 API 中，有部分已不推荐使用，有部分已废弃不支持。本文主要阐述不推荐使用和已不支持的 API 情况。 对于不推荐使用的 API，并且仍会在 API 参考中阐述该接口的调用方法，IDE 中会带有过时标记。一般情况下，不推荐使用的 API 将不再在后续专有云版本中继续提供支持。 对于已不支持的 API，大部分均不存在替代接口，且不会在 API 参考中阐述该接口的调用方法；少部分已不支持的 API 有功能相似的替代 API 提供使用。

| API名称 | 可用性 | 替代API |
|---|---|---|
| CreateEmpower | 3.18.3-0起，不推荐使用 | N/A |
| CreateEmpowerBySub | 3.18.3-0起，不推荐使用 | N/A |
| CreateGroupEmpowerBySub | 3.18.3-0起，不推荐使用 | N/A |
| DeleteEmpower | 3.18.3-0起，不推荐使用 | N/A |
| DeleteGroupEmpower | 3.18.3-0起，不推荐使用 | N/A |

IDEA 会带上过时标记方便开发人员注意到过时 API，新用户不应该再使用这些接口。 消息队列消息队列

## API参考

### MQTT_API

#### MQTT Open API简介

##### 面向用户和场景

Open API是微消息队列MQTT版提供给用户的管控手段，用于实现一系列资源管理和运维功能。同生产用 SDK不同，Open API主要用于管理微消息队列MQTT版相关的资源，如Group ID。

##### 适用场景和局限性

Open API由于其实现原理，调用端必须具备访问微消息队列MQTT版控制台域名的能力，否则无法调通。 Open API底层基于HTTP协议实现，性能和效率不高，仅适用于管控场景，请勿用于大批量高并发的生产场景。

##### Open API基本原理

Open API底层通过HTTP接口提供服务，您调用HTTP客户端，发出HTTP请求到微消息队列MQTT版的后端服务去执行。 您将参数封装到每个请求中，每个请求即对应一个接口，执行的结果放在response中，请求和响应的字符编码都是采用UTF-8编码。 其中，HTTP请求的服务端地址即为控制台的域名地址。

#### MQTT Open API接入指南

##### 公共参数设置

客户端基于HTTPS方式调用MQTT Open API，所有API请求都需要传入一部分公共参数，供服务端进行权限校验。 公共参数列表如下：

| 参数名称 | 类型 | 是否必须 | 说明 |
|---|---|---|---|
| accesskey _ | String | 是 | 用户账号AK |
| preventCache __ | Long | 是 | 用于CSRF校验，设置为系统当前时间即可，单位毫秒（ms） |
| regionId _ | String | 是（获取regionId列表接口除外） | 当前Region |
| mqttInstanceId _ | String | 是 | 当前API 操作的实例 Id |
| signature _ | String | 是 | 请求的签名 |

**_regionId**参数需要填写当前请求操作的Region，专有域和专有云情况下，默认值为mq-private。
消息队列
**_signature**参数是对HTTPS请求中其他参数字段做排序后得到待签名字符串，然后使用账号的SecretKey
进行签名计算得到。

**签名计算示例**

例如原始请求的HTTP方法是：

```
https://mq.console.${global:internet-domain}/json/topic/create
```

在单region部署的情况下或接入多region部署中的中心region，使

**说明**

用 ${global:internet-domain} 作为访问域名；接入多region部署下的普通region，使

```
用 ${global:region}.${global:internet-domain} 作为访问域名
```

参数列表有（参数包含公共参数和每个接口自定义的参数）：

**Key_2=Value_2&Key_1=Value_1&Key_3=Value_3**

那么原始请求URL是：

```
https://mq.console.${global:internet-domain}/json/topic/create? Key_2=Value_2&Key_1=Value_1&Key_3=Value_3
```

将**Key_2**，**Key_1**，**Key_3**这3对参数的key按字典序排序，然后将对应的value按字符串连接。Key的排序结果为：Key_1、Key_2、Key_3，排序后其对应值的连接结果为Value1Value2Value3。此时待签名字符串就是Value1Value2Value3。 然后使用您的secretKey作为秘钥，使用 HmacSHA1方法对上面的待签名字符串做签名，得到签名字符串。Hmac的算法实现，各个语言都有现成的函数库，请自行搜索。 Linux命令行的方式可以参考：

```
echo -n 'Value1Value2Value3' | openssl dgst -hmac '用户的SecretKey' -sha1 -binary | base
```

假设最终得到的结果为：eqweq+adwe23****= 最后，整个HTTPS请求就是（注意通过curl的方式需要将“+”替换成“%2B”，“=”替换成“%3D”，“/”替换成“%2F”，否则自动转义后会报鉴权失败）：

```
https://mq.console.${global:internet-domain}/json/topic/create? Key_2=Value_2&Key_1=Value_1&Key_3=Value_3&_signature= eqweq%2Badwe23****%3D
```

##### 公共返回值解析

客户端发起HTTP请求到服务端，服务端处理完成后同样以HTTP响应形式返回结果，正常情况下返回结果 HTTP状态码都是200，返回的内容放在Body中，为JSON字符串，需要客户端自己做JSON解析，判断是否调用成功。 JSON格式如下： 消息队列

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
"total": 0 }
```

返回值说明： code：状态码，200代表成功，其他都是处理失败。 currentPage：当前请求如果是分页查询的请求，此变量代表结果所处的当前页。 dynamicMessage：错误异常信息字符串。 message：处理结果信息。 pageSize：当前请求如果是分页查询的请求，此变量代表结果所处的当前页大小。 success：是否成功。 data：业务信息返回，String类型，也是JSON，如果当前请求的返回结果中带有业务数据，则此处需要反解JSON内容。 RequestId：每个请求的唯一ID，String类型。

#### MQTT Open API公共术语

##### 账号安全类

###### AccessKey

访问阿里云产品使用的账号的AccessKey，由阿里云官网获得。调用时传入给微消息队列MQTT版后台用于身份验证，调用微消息队列MQTT版的Open API只能操作对应账号下的资源。

###### SecretKey

访问阿里云产品使用的账号的AK秘钥，由阿里云官网获得，调用时传入，用于计算访问请求的签名。微消息队列MQTT版后端根据对应账号比对签名实现鉴权。

##### MQTT资源管控类

###### Group ID（GID）

用于指定一组逻辑功能完全一致的节点共用的组名，代表一类相同功能的设备。Group ID需要创建后方可使用。

#### MQTT API错误码列表

消息队列如果成功调用微消息队列MQTT版的API，则会返回给客户端ResponseCode=200；如果调用失败，会返回对应的异常错误码以及描述信息。您可以根据以下异常信息对照表查找对应的解决方法。 表 1. 错误码列表

| 错误码 | 现象或原因 | 解决方法 |
|---|---|---|
| ONS SYSTEM ERROR _ _ | 微消息队列MQTT版后端异常 | 请联系技术支持人员处理。 |
| ONS SERVICE UNSUPPORTED _ _ | 当前调用在对应的地域不支持 | 请联系技术支持人员确认该接口的开通情况。 |
| ONS INVOKE ERROR _ _ | Open API接口调用失败 | 请联系技术支持人员处理。 |
| BIZ FIELD CHECK INVALID _ _ _ | 参数检验失败 | 请参考API手册检查各个参数传入是否合法。 |
| BIZ TOPIC NOT FOUND _ _ _ | Topic没有找到 | 请检查Topic输入是否合法，或者是否创建过。 |
| BIZ SUBSCRIPTION NOT FOUN _ _ _ D | 目标订阅关系GID找不到 | 请检查GID是否创建过，或者查询条件错误。 |
| BIZ PUBLISHER EXISTED _ _ | 指定GID已经存在 | 更换GID的名称重试请求。 |
| BIZ SUBSCRIPTION EXISTED _ _ | 指定GID已经存在 | 更换GID的名称重试请求。 |
| BIZ CONSUMER NOT ONLINE _ _ _ | 指定GID的客户端不在线 | 请确保消费端在线，然后重试请求。 |
| BIZ NO MESSAGE _ _ | 当前查询条件没有匹配消息 | 请检查查询条件，并确认查询范围内是否发过消息。 |
| BIZ REGION NOT FOUND _ _ _ | 请求的Region找不到 | 确认请求的Region参数是否合法。 |
| BIZ TOPIC EXISTED _ _ | 指定Topic已经存在 | 更改Topic名称重试请求。 |
| BIZ PUBLISH INFO NOT FOUND _ _ _ _ | 请求的GID没有找到 | 确认GID是否存在，或者请求条件错误。 |
| EMPOWER EXIST ERROR _ _ | 当前授权关系已经存在 | 核实请求参数，重试或者先查询。 |
| EMPOWER OWNER CHECK ERR _ _ _ OR | 当前用户不是授权Topic的Owner | 确认资源所属关系。 |

#### API详细说明

##### Group管理接口

###### 创建Group ID（/json/mqtt/createGroupId）

**使用场景**

新业务上线时，在创建Topic资源后，如需使用微消息队列MQTT版客户端收发消息，首先需要创建GID。

**请求参数列表**

消息队列

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| groupId | String | 是 | 需要创建的微消息队列MQTT版客户端分组ID。 |

**返回结果示例**

```json
{
    "requestId":"",
    "code":200,
    "status":"SUCCESS",
    "message":"operation success",
    "data":null,
    "success":true,
    "helpUrl":null,
    "dynamicCode":"",
    "dynamicMessage":"",
    "total":0,
    "pageSize":0,
    "currentPage":0
}
```

###### 删除Group ID（/json/mqtt/deleteGroupId）

**使用场景**

新应用迭代过程中，如果部分GID不再使用，可以删除GID。

**请求参数列表**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| groupId | String | 是 | 需要删除的GID |

**返回结果参考**

消息队列

```json
{
    "requestId":"",
    "code":200,
    "status":"SUCCESS",
    "message":"operation success",
    "data":null,
    "success":true,
    "helpUrl":null,
    "dynamicCode":"",
    "dynamicMessage":"",
    "total":0,
    "pageSize":0,
    "currentPage":0
}
```

###### 查询Group ID列表（/json/mqtt/listGroupId）

**描述**

一般用于管理您所有的GID的场景。您可先获取GID列表，然后查询单个GID的相关数据。

**请求参数列表**

**返回结果示例**

```json
{
    "requestId":"",
    "code":200,
    "status":"SUCCESS",
    "message":"operation success.",
    "data":[
        {
            "id":56222,
            "channelId":0,
            "regionId":"cn-qingdao-publictest",
            "regionName":"\u516C\u7F51",
            "owner":"138015630679****",
            "parent":null,
            "applier":"138015630679****",
            "groupId":"GID_BBBB",
            "topic":null,
            "status":0,
            "appkey":null,
            "relation":null,
            "createTime":1566013570000,
            "updateTime":1566013570000,
            "pageStart":0,
            "pageSize":20,
            "aoneId":"",
            "namespaceId":"mqtt-cn-45919cr0002",
```

消息队列

```json
            "independentNaming":true,"aoneUrl":null,
            "relationName":"",
            "channelName":"ALIYUN",
            "statusName":"\u670D\u52A1\u4E2D"},
        {
            "id":56221,
            "channelId":0,
            "regionId":"cn-qingdao-publictest",
            "regionName":"\u516C\u7F51",
            "owner":"1380156306793859",
            "parent":null,
            "applier":"1380156306793859",
            "groupId":"GID_AAAA",
            "topic":null,
            "status":0,
            "appkey":null,
            "relation":null,
            "createTime":1566013563000,
            "updateTime":1566013563000,
            "pageStart":0,
            "pageSize":20,
            "aoneId":"",
            "namespaceId":"mqtt-cn-45919cr0002",
            "independentNaming":true,
            "aoneUrl":null,
            "relationName":"",
            "channelName":"ALIYUN",
            "statusName":"\u670D\u52A1\u4E2D"
        }],
    "success":true,
    "helpUrl":null,
    "dynamicCode":"",
    "dynamicMessage":"",
    "total":2,
    "pageSize":20,
    "currentPage":1
}
```

##### 设备管控接口

###### 查询设备在线信息

**（/json/mqtt/getDeviceRunningInfo）**

查询单一设备在线信息的接口，调用该接口可以查询指定的微消息队列MQTT版客户端的状态信息。

**使用场景**

查询单个微消息队列MQTT版客户端的订阅关系和在线状态。

**请求参数列表**

消息队列

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| clientId | String | 是 | 需要查询的微消息队列MQTT版客户端的ID |

**返回结果示例**

```json
{
    "requestId":"",
    "code":200,
    "status":"SUCCESS",
    "message":"operation success.",
    "data":
{"online":true,"clientId":"GID_HK_qd_test@@@11.193.**.**_R_V2","clientChannel":"/11.193.*
**:46179","lastTouch":0,"brokerName":"ons-mqtt-cs011193243214.nu20","subScriptonData":[
{"firstTopic":"mqtt_new_hk_qd_test","secondTopic":"/ons-mqttcs01119324****_nu20/QOS1_V2/","qos":1}, {"firstTopic":"mqtt_new_hk_qd_test","secondTopic":"/ons-mqttcs01119324****_nu20/QOS2_V2/","qos":2}, {"firstTopic":"mqtt_new_hk_qd_test","secondTopic":"/ons-mqttcs01119324****_nu20/QOS0_V2/","qos":0}, {"firstTopic":"mqtt_new_hk_qd_test","secondTopic":"/ons-mqttcs01119324****_nu20/","qos":1}],
    "extInfo":{"KEY_CLEANSESSION":"true"}},
    "success":true,
    "helpUrl":null,
    "dynamicCode":"",
    "dynamicMessage":"",
    "total":0,
    "pageSize":0,
    "currentPage":0
}
```

###### 查询历史在线统计

**（/json/mqtt/getMqttConnectionSum）**

查询某个分组历史在线终端数据的接口，调用该接口可以查询指定GroupId的历史在线客户端在线数量信息。

**使用场景**

统计历史上某个设备分组下在线终端数。

**请求参数列表**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| groupId | String | 是 | 需要查询的分组ID |
| beginTime | Long | 是 | 查询的起始毫秒时间戳，不得早于一周前 |

消息队列

| endTime | Long | 是 | 查询的截止毫秒时间戳，不得晚于当前时间 |
|---|---|---|---|

**返回结果示例**

```json
{
    "requestId":"",
    "code":200,
    "status":"SUCCESS",
    "message":"operation success.",
    "data":
{"title":"\u5BA2\u6237\u7AEF\u8FDE\u63A5\u6570","xUnit":"\u65F6\u95F4","yUnit":"\u6570\u9 F","sumStat":0.0,"records":[{"x":1566010800000,"y":4.0},{"x":1566010860000,"y":4.0},{"x ":1566010920000,"y":4.0},{"x":1566010980000,"y":4.0},{"x":1566011040000,"y":4.0},{"x":1 566011100000,"y":4.0},{"x":1566011160000,"y":4.0},{"x":1566011220000,"y":4.0},{"x":1566 011280000,"y":4.0},{"x":1566011340000,"y":4.0},{"x":1566011400000,"y":4.0}, {"x":1566011460000,"y":4.0},{"x":1566011520000,"y":4.0},{"x":1566011580000,"y":4.0},{"x ":1566011640000,"y":4.0},{"x":1566011700000,"y":4.0},{"x":1566011760000,"y":4.0},{"x":1 566011820000,"y":4.0},{"x":1566011880000,"y":4.0},{"x":1566011940000,"y":4.0},{"x":1566 012000000,"y":4.0},{"x":1566012060000,"y":4.0},{"x":1566012120000,"y":4.0}, {"x":1566012180000,"y":4.0},{"x":1566012240000,"y":4.0},{"x":1566012300000,"y":4.0},{"x ":1566012360000,"y":4.0},{"x":1566012420000,"y":4.0},{"x":1566012480000,"y":4.0},{"x":1 566012540000,"y":4.0},{"x":1566012600000,"y":4.0},{"x":1566012660000,"y":4.0},{"x":1566 012720000,"y":4.0},{"x":1566012780000,"y":4.0},{"x":1566012840000,"y":4.0}, {"x":1566012900000,"y":4.0},{"x":1566012960000,"y":4.0},{"x":1566013020000,"y":4.0},{"x ":1566013080000,"y":4.0},{"x":1566013140000,"y":4.0},{"x":1566013200000,"y":4.0},{"x":1 566013260000,"y":4.0},{"x":1566013320000,"y":4.0},{"x":1566013380000,"y":4.0},{"x":1566 013440000,"y":4.0},{"x":1566013500000,"y":4.0},{"x":1566013560000,"y":5.0}, {"x":1566013620000,"y":4.0},{"x":1566013680000,"y":4.0},{"x":1566013740000,"y":4.0},{"x ":1566013800000,"y":4.0},{"x":1566013860000,"y":4.0},{"x":1566013920000,"y":4.0},{"x":1 566013980000,"y":5.0},{"x":1566014040000,"y":4.0},{"x":1566014100000,"y":4.0},{"x":1566 014160000,"y":4.0},{"x":1566014220000,"y":4.0},{"x":1566014280000,"y":4.0}, {"x":1566014340000,"y":4.0},{"x":1566014400000,"y":5.0},{"x":1566014460000,"y":4.0}]},
    "success":true,
    "helpUrl":null,
    "dynamicCode":"",
    "dynamicMessage":"",
    "total":0,
    "pageSize":0,
    "currentPage":0
}
```

###### 根据Topic查询在线设备的数量

**（/json/mqtt/getClientSetByTopic）**

根据微消息队列MQTT的Topic统计订阅该Topic的在线设备的数量。

**使用场景**

getClientSetByTopic接口一般用于业务分析。业务上订阅某个特定Topic的设备一般是参与某个特殊活动的设备，可以根据Topic查询参与该活动的设备数量。 消息队列由于OpenAPI面向的场景是用户自定义管控开发，服务端会对过快的调用进行限流，因此不要在业务的主流程中使用本接口。如需判断设备是否在线，请使用设备上下线通知功能。

**返回结果示例**

```json
{
    "requestId":"",
    "code":200,
    "status":"SUCCESS",
    "message":"operation success.",
    "data":{"clientIdSet":[],"onlineCount":0,"persistCount":0},
    "success":true,
    "helpUrl":null,
    "dynamicCode":"",
    "dynamicMessage":"",
    "total":0,
    "pageSize":0,
    "currentPage":0
}
```

##### 资源报表接口

###### 消息收发统计

**（/json/mqtt/getMqttMsgTransTask）**

查询指定Topic的历史收发量的曲线信息。

**使用场景**

统计历史上特定Topic的消息收发量。

**请求参数列表**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| topic | String | 是 | 需要查询的一级Topic。 |
| secondTopic | String | 否 | 查询的子Topic，如果没有则不填。 |
| beginTime | Long | 是 | 查询的起始毫秒时间戳，不得早于一周前。 |
| endTime | Long | 是 | 查询的截止毫秒时间戳，不得晚于当前时间。 |
| qos | Integer | 否 | 查询的消息QoS，如果不填则查询所有。 |
| msgType | String | 否 | 设置P2P或者SUB分别查询点对点消息或者普通发布订阅的消息，如果不填则查询所有。 |
| queryType | String | 是 | 设置PUB或者SUB，分别代表查询发送和接收。 |
| consoleType | String | 是 | 设置TPS或者SUM，代表查询消息TPS或者是消息总量。 |

消息队列

**返回结果示例**

```json
{
    "requestId":"",
    "code":200,
    "status":"SUCCESS",
    "message":"operation success.",
    "data":
{"title":"\u6D88\u606F\u6D88\u8D39\u6570\u91CF","xUnit":"\u65F6\u95F4","yUnit":"\u6761"," mStat":0.0,"records":[{"x":1566014820000,"y":288.0},{"x":1566014760000,"y":288.0},{"x": 1566014700000,"y":288.0},{"x":1566014640000,"y":288.0},{"x":1566014580000,"y":288.0},{" x":1566014520000,"y":288.0},{"x":1566014460000,"y":288.0}, {"x":1566014400000,"y":288.0},{"x":1566014340000,"y":288.0}, {"x":1566014280000,"y":288.0},{"x":1566014220000,"y":288.0}, {"x":1566014160000,"y":288.0},{"x":1566014100000,"y":288.0}, {"x":1566014040000,"y":288.0},{"x":1566013980000,"y":288.0}, {"x":1566013920000,"y":288.0},{"x":1566013860000,"y":288.0}, {"x":1566013800000,"y":288.0},{"x":1566013740000,"y":288.0}, {"x":1566013680000,"y":288.0},{"x":1566013620000,"y":288.0}, {"x":1566013560000,"y":288.0},{"x":1566013500000,"y":288.0}, {"x":1566013440000,"y":288.0},{"x":1566013380000,"y":288.0}, {"x":1566013320000,"y":288.0},{"x":1566013260000,"y":288.0}, {"x":1566013200000,"y":288.0},{"x":1566013140000,"y":288.0}, {"x":1566013080000,"y":288.0},{"x":1566013020000,"y":288.0}, {"x":1566012960000,"y":288.0},{"x":1566012900000,"y":288.0}, {"x":1566012840000,"y":288.0},{"x":1566012780000,"y":288.0}, {"x":1566012720000,"y":288.0},{"x":1566012660000,"y":288.0}, {"x":1566012600000,"y":288.0},{"x":1566012540000,"y":288.0}, {"x":1566012480000,"y":288.0},{"x":1566012420000,"y":288.0}, {"x":1566012360000,"y":288.0},{"x":1566012300000,"y":288.0}, {"x":1566012240000,"y":288.0},{"x":1566012180000,"y":288.0}, {"x":1566012120000,"y":288.0},{"x":1566012060000,"y":288.0}]},
    "success":true,
    "helpUrl":null,
    "dynamicCode":"",
    "dynamicMessage":"",
    "total":0,
    "pageSize":0,
    "currentPage":0
}
```
