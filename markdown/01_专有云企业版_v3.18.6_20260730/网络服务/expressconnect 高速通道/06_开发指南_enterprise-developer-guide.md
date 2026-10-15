---
title: "高速通道 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 116
source_pdf: "06_开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/expressconnect/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 高速通道 开发指南

高速通道

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
高速通道
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。 高速通道
2. 获取RegionID。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。

**说明**

调用API时，请在Header参数中增加组织ID `<x-acs-organizationid>` 和资源集ID `<x-acs-resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参见开发文档使用说明。
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
高速通道

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

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参见获取STS AccessKey。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号 AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全

**警告**

性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni- manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方法可参见《Apsara Uni- manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

高速通道

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。

**说明**

AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取公共Header参数

调用专有云API时需要提供多个Header参数。本文为您介绍这些参数的含义及其获取方式，并对调用后的一些返回值做出解释。

**Header参数描述**

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 环境RegionID。具体操作，请参见获取Region ID。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID。具体操作，请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID。具体操作，请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID。具体操作，请参见获取实例ID。 |

**获取Region ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理**>**地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看Region ID。

**获取组织ID**

组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。

**获取资源集ID**

资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以高速通道为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**网络**>**高速通道**。
3. 在左侧导航栏中，单击**独享物理专线**。
4. 在**独享物理专线**列表中查看**实例****ID/****名称**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。 高速通道

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用云产品API时，三元组缺一不可。更多STS内容请参见什么是STS。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com>，请替换为实际的STS Endpoint。 高速通道

| public static void main(String[] args) { // 创建DefaultAcsClient实例并初始化。 // 请替换为您实际的地域ID、AccessKey ID、AccessKey Secret DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>"); HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true); clientConfig.setProtocolType(ProtocolType.HTTPS); profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); String assumeRole = callAssumeRole(client); if (StringUtils.isEmpty(assumeRole)) return; JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole); JSONObject credentials = assumeRoleJson.getJSONObject("Credentials"); // 获取到STS三元组 String stsAK = credentials.getString("AccessKeyId"); String stsSK = credentials.getString("AccessKeySecret"); String stsToken = credentials.getString("SecurityToken"); } private static String callAssumeRole(IAcsClient client) { CommonRequest request = new CommonRequest(); // "sts.aliyuns.com" 请替换为实际的STS Endpoint，一般格式为sts-vpc.${global:region}.${global:internet-domain} request.setSysDomain("sts.aliyuns.com"); request.setSysProduct("Sts"); request.setSysAction("AssumeRole"); request.setSysVersion("2015-04-01"); request.setSysMethod(MethodType.POST); request.setHttpContentType(FormatType.FORM); // 业务参数，设置本次调用Session的别名，"<yourRoleSessionName>"请您替换为实际值 request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>"); // 扮演的Role角色ARN，"<yourRoleArn>"请替换为上一步获取到的实际Ram Role ARN request.putQueryParameter("RoleArn", "<yourRoleArn>"); try { CommonResponse response = client.getCommonResponse(request); return response.getData(); } catch (ServerException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } catch (ClientException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } return null; } |  |  |
|---|---|---|
| 通过STS AccessKey三元组调用云产品的接口，下列代码以高速通道的 | DescribePhysicalConnections | 接口为示例。 |
| 说明以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>，请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 |  |  |

高速通道

```
public static void main(String[] args) {
```

`// "<yourRegionID>"`请替换为您实际的地域`ID` `// "<yourStsAccessKeyID>", "<yourStsAccessKeySecret>"`请替换为前一步获取到的`STS`三元组中`AccessKeyID`、`AccessKeySecret`

```
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccesskey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("vpc.aliyuns.com");
    request.setSysProduct("vpc");
    request.setSysAction("DescribePhysicalConnections");
    request.setSysVersion("2016-04-28");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//"<yourRegionID>"` 请替换为您实际的地域`ID`

```
    request.putHeaderParameter("x-acs-regionid", "<yourRegionID>");
```

`// "<yourStsToken>"` 请替换为您前一步获取到的`STS`三元组中`SecurityToken`

```
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
```

`//` 非必填,请替换为您实际的资源集`ID`

```
    // request.putHeaderParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填,请替换为您实际的组织`ID`

```java
    request.putHeaderParameter("x-acs-organizationid", "<yourOrganizationID>");
    try {
        CommonResponse response = client.getCommonResponse(request);
        System.out.println(response.getData());
    } catch (ServerException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    } catch (ClientException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    }
}
```

### 获取高速通道的SDK包

通过POP网关调用专有云API时，需使用相应云产品的SDK。本文为您介绍如何获取阿里云开发工具包（SDK）。

**背景介绍**

实现高速通道功能需要您同时安装VPC SDK（高速通道使用VPC SDK实现功能）和阿里云核心库。以Java SDK为例，您需要下载 `aliyun-java-sdk-vpc` 以及 `aliyun-`

```
java-sdk-core 。
```

VPC SDK封装了2016-04-28版本API，以访问密钥（AccessKey）识别调用者身份，提供自动签名等功能，方便您通过API创建和管理资源。阿里云开发工具包（SDK） 包括代码以及示例，您可以自行选择语言来创建云应用。 SDK核心库推荐您使用阿里云官网的SDK核心库，该内容适用于所有云产品，也同样适用于专有云产品。

**操作指导**

目前SDK的语言支持：Java、Python、Go，您可以前往阿里云开发工具包（SDK）中进行选择。

**说明**

推荐使用 Java、Python、Go三种语言的SDK包，使用其他语言的SDK包可能发生不兼容情况。 高速通道

## Java SDK调用

安装阿里云Java SDK后，您可以编写代码使用阿里云Java SDK访问阿里云POP网关，调用Apsara Uni-manager运营控制台的API接口。

**前提条件**

已获取AccessKey或STS Accesskey，获取方式请参见获取AccessKey或STS AccessKey。 已获取Apsara Uni-manager运营控制台的Endpoint，获取方式请参见获取Apsara Uni-manager运营控制台的Endpoint。 已安装1.8及以上版本的JDK。 在项目目录下的pom.xml文件中，添加阿里云Java SDK核心库。

```xml
<!-- https://mvnrepository.com/artifact/com.aliyun/aliyun-java-sdk-core --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.30</version>
</dependency>
```

**说明**

SDK包更新频繁，建议您前往阿里云开发工具包（SDK）获取最新版本依赖。 使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。Java SDK支持通过AccessKey或STS AccessKey进行身份验证。

**重要**

确保包含AccessKey或STS AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKey Secret`。

```
    "<yourSecurityToken>"
```

`//`在使用`STS AccessKey`进行身份验证时，`<yourSecurityToken>`请替换为您实际的`SecurityToken`。 `//`在使用`AccessKey`进行身份验证时，`<yourSecurityToken>`为`null`。

```
);
```

**说明**

以上代码示例中 `<yourRegionID>` 、 `<yourAccessKeyID>` 、 `<yourAccessKeySecret>` 、 `<yourSecurityToken>` 均为可变参数，需要替换为其实际值，尖括号 （<>）在最终代码中不保留。

**创建并配置请求连接**

可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。 `//` 获取`HttpClientConfig`对象。

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

`//` 设置是否忽略证书。`true`：忽略；`false`：不忽略。

```
clientConfig.setIgnoreSSLCerts(true);
```

`//` （可选）设置创建连接超时时间，单位毫秒（`ms`）。

```
clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);
```

`//` （可选）设置读取超时时间，单位毫秒（`ms`）。

```
clientConfig.setReadTimeoutMillis(<readTimeout>);
```

`/**` （可选）请根据实际情况判断是否设置代理，设置方法如下。若需要设置代理，请替换为您实际的代理`IP+`端口。

```
clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

`*/`

```
profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile);
```

**说明**

以上代码示例中 `<connectionTimeout>` 、 `<readTimeout>` 、 `<http://192.168.XX.XX:33XX>` 均为可变参数，需要您结合自身服务替换为其实际值，尖括号 （<>）在最终代码中不保留。

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。 高速通道 `//` 创建`API`请求并设置参数。

```
CommonRequest request = new CommonRequest();
```

`// Apsara Uni-manager`运营控制台接口信息参数。

```
request.setSysProduct("ascm"); request.setSysVersion("2019-05-10"); request.setSysUriPattern("<yourCallUriPattern>");
```

`// Apsara Uni-manager`运营控制台的`Endpoint`地址。

```
request.setSysDomain("<ascmEndpoint>");
```

`//` 设置请求方式。

```
request.setSysMethod(MethodType.POST);
```

`//` 设置`Headers`。 `//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>");
```

`//` 接口业务参数设置。

```
...
```

`//` 设置`Content-Type`。

```
request.setHttpContentType(FormatType.JSON);
```

**说明**

以上代码示例中 `<yourCallUriPattern>` 、 `<ascmEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**设置阿里云核心库SDK参数**

在使用阿里云核心库SDK发起API请求时，可以设置四种类型的参数：Path、Query、Body、Header。在调用具体API时，请根据开发文档中标注的参数位置对应设置。

| 参数类型 | 描述 | 代码示例 |
|---|---|---|
| Path | Path参数用于对请求Request中设置的UriPattern 进行变量替换。 例如：URI "/clusters/[ClusterId]" 中的 [ClusterId] 可以通过设置Path参数 "ClusterId=cluster1" 进行替换。 最终发起HTTP请求的URI则为 "/clusters/clusterId01" 。 | CommonRequest request = new CommonRequest(); request.setSysUriPattern("/clusters/[ClusterId]"); request.putPathParameter("ClusterId", "clusterId01"); |
| Query | Query参数用于对请求Request中的URL参数进行设置（一般用于GET请求）。 例如：“http://aliyun.com/api/? ClusterId=clusterId01&ClusterName=cluster Name01”。 | CommonRequest request = new CommonRequest(); request.putQueryParameter("ClusterId", "clusterId01"); request.putQueryParameter("ClusterName", "clusterName01"); |
| Body | Body参数用于对请求Request中的HTTP Content 进行设置（一般用于POST/PUT请求）。 目前支持两种格式： application/json application/x-www-form-urlencoded 说明在设置Body参数时，需要同时设置HTTP Content-Type。 | key-value形式设置Body参数，并设置HttpContentType。 CommonRequest request = new CommonRequest(); request.putBodyParameter("ClusterId", "clusterId01"); request.putBodyParameter("ClusterName", "clusterName01"); // 若Content-Type设置为application/x-www-form-urlencoded，请求到服务器的 Content数据格式为"ClusterId=clusterId01&ClusterName=clusterName01"的字符串。 request.setHttpContentType(FormatType.FORM); // 或，若Content-Type设置为application/json，请求到服务器的Content数据格式为" {\"ClusterId\":\"clusterId01\",\"ClusterName\":\"clusterName01\"}"的JSON 串。 request.setHttpContentType(FormatType.JSON); 自行构造HTTP Content并直接设置HttpContent。 CommonRequest request = new CommonRequest(); //设置application/json格式的HTTP Content。 String body = "{\"ClusterId\": \"clusterId01\", \"ClusterName\": \"clusterName01\"}"; request.setHttpContent(body.getBytes(), "utf-8", FormatType.JSON); //设置application/x-www-form-urlencoded格式的HTTP Content。 String body = "ClusterId=clusterId01&ClusterName=clusterName01"; request.setHttpContent(body.getBytes(), "utf-8", FormatType.FORM); |
| Header | Header参数用于对请求Request中的HTTP Header进行设置。 | CommonRequest request = new CommonRequest(); request.putHeadParameter("x-acs-organizationid", "3"); request.putHeadParameter("x-acs-resourcegroupid", "2"); |

**发起调用并处理应答**

可参考以下代码发起请求并处理返回结果。 高速通道

```
try {
```

`//` 发起请求，并获取返回。

```java
    CommonResponse response = client.getCommonResponse(request);
    System.out.println(response.getData());
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    System.out.println("ErrCode:" + e.getErrCode());
    System.out.println("ErrMsg:" + e.getErrMsg());
    System.out.println("RequestId:" + e.getRequestId());
}
```

#### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Java SDK返回的错误进行处理，只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try {
    AcsResponse response = client.getAcsResponse(request);
```

`//` 处理`Response`。

```
    // ...
}catch (ServerException e){
```

`//` 这里可以添加您自己的错误处理逻辑。 `//` 例如，打印具体的错误信息。

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`//` 如果遇上棘手问题，可联系阿里云技术支持，并提供`RequestID`。

```java
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
```

`//` 这里可以添加您自己的错误处理逻辑。 `//` 例如，打印具体的错误信息。

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
}
```

**完整调用示例**

以下代码为通过Apsara Uni-manager运营控制台的 `GetOrganizationList` 接口获取组织列表的调用示例。 高速通道

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Demo {
    /**
```

* 本文提供的`API`调用样例仅供参考，更多详细`API`调用方法可参照开发文档中的“快速入门”。
`*/`

```
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID`。 `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKeySecret`。

```
                null);
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
```

请根据实际情况判断是否需要设置`HTTP`代理，设置方法如下。请替换为您实际代理`IP+`端口。

```
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`*/` `//` 设置连接超时，单位：`ms`。

```
        // clientConfig.setConnectionTimeoutMillis(1000L);
```

`//` 设置读取超时，单位：`ms`。

```
        // clientConfig.setReadTimeoutMillis(10000L);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`// Apsara Uni-manager`运营控制台接口信息参数。

```
        request.setSysProduct("ascm");
        request.setSysVersion("2019-05-10");
        request.setSysUriPattern("/ascm/auth/organization/queryList");
```

`// Apsara Uni-manager`运营控制台的`Endpoint`地址。

```
        request.setSysDomain("<ascmEndpoint>");
```

`//` 设置请求方式。

```
        request.setSysMethod(MethodType.POST);
```

`//` 设置`Headers`。 `//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
        request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>");
```

`//` 调用专有云`API`时，一般需要提供多个公共`Header`参数，包括：`x-acs-regionid`、`x-acs-organizationid`、`x-acs-resourcegroupid`、`x-acs-instanceid`。详情可参 `//` 接口业务参数设置。

```
        request.putBodyParameter("id","1");
        request.setHttpContentType(FormatType.JSON);
        try {
```

`//` 发起请求，并获取返回。

```java
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
        }
    }
}
```

**说明**

以上代码示例

```
中 <yourRegionID> 、 <yourAccessKeyID> 、 <yourAccessKeySecret> 、 <http://192.168.XX.XX:33XX> 、 <ascmEndpoint> 、 <yourCallerSdkSource> 均
```

为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

### 快速开始

本节介绍如何获取VPC Java SDK并开始调用。高速通道使用VPC SDK实现功能。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参见获取AccessKey。 获取高速通道的Endpoint，具体操作，请参见获取高速通道的Endpoint。 阿里云专有云Java SDK需要1.8及以上的JDK。 高速通道

**安装阿里云专有云 Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中加入Maven命令。 要使用VPC的开发工具包，必须安装SDK核心库以及VPC产品的SDK。其中，SDK核心库推荐使用4.5.17及以上版本，SDK的版本为3.2.0。

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-vpc</artifactId>
            <version>3.2.0</version>
        </dependency>
</dependencies>
```

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Product>，请替换为您实际的产品名称。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <readTimeout>，请您根据实际情况设置读取超时时间，单位为毫秒。 <connectionTimeout>，请您根据实际情况设置连接超时时间，单位为毫秒。 <maxRequestsPerHost>，请您根据实际情况设置每个主机的最大请求数。 <maxRequests>，请您根据实际情况设置最大请求数。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。 高速通道

```java
import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.vpc.model.v20160428.*; import com.google.gson.Gson; public class Main {
     public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret` `//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值

```
        profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
```

`//` 设置请求配置

```
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);// 忽略证书
```

clientConfig.setReadTimeoutMillis(<readTimeout>);// 读取超时时间（可选）,单位为毫秒（`ms`） clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// 连接超时时间（可选）,单位为毫秒（`ms`） clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// 设置每个主机的最大请求数（可选） clientConfig.setMaxRequests(<maxRequests>);// 设置最大请求数（可选） clientConfig.setProtocolType(ProtocolType.HTTP); // 设置请求协议,默认`HTTP`（可选） `/*` 设置代理(可选`),`替换为代理`IP+Port`

```
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

或

```
        clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```
        DescribePhysicalConnectionsRequest request = new DescribePhysicalConnectionsRequest();
```

`//` 业务参数

```
        request.setPageSize(10);
        request.setPageNumber(1);
```

`//` 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用

```
        request.putHeaderParameter("x-acs-organizationid", "1");
        request.putHeaderParameter("x-acs-resourcegroupid", "11");
```

`//` 发起请求并处理应答或异常

```java
        DescribePhysicalConnectionsResponse response;
       try {
            DescribePhysicalConnectionsResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
        }
     }
 }
```

### 使用手册

#### 3.2.1. 安装Java SDK

本文介绍如何安装及调用VPC Java SDK。高速通道使用VPC SDK实现功能。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包（SDK）的方式安装专有云Java SDK。 要使用VPC的开发工具包，必须安装阿里云Java SDK核心库以及VPC的Java SDK。SDK核心库推荐使用4.5.17及以上版本，Java SDK的版本为3.2.0。 以使用VPC的Java SDK为例，您需要安装阿里云Java SDK核心库和VPC Java SDK，并在pom.xml文件中添加以下依赖即可。准确的SDK版本号，请参见阿里云开发工具包 （SDK）。

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-vpc</artifactId>
            <version>3.2.0</version>
        </dependency>
</dependencies>
```

#### 3.2.2. 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。 高速通道目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 3.2.3. 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <readTimeout>，请您根据自身服务的能力，配置读取超时时间，单位为毫秒（ms）。 <connectionTimeout>，请您根据自身服务的能力，配置连接超时时间，单位为毫秒（ms）。 <maxRequestsPerHost>，请您根据自身服务的能力，配置每台服务器的最大请求数，数据类型为INT。 <maxRequests>，请您根据自身服务的能力，配置最大请求数，数据类型为INT。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。 `//` 获取`HttpClientConfig`对象

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

`//` 设置是否忽略证书

```
clientConfig.setIgnoreSSLCerts(true);
```

`// (`可选)设置读取超时时间，单位毫秒（`ms`）

```
clientConfig.setReadTimeoutMillis(<readTimeout>);
```

`// (`可选)设置创建连接超时时间，单位毫秒（`ms`）

```
clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);
```

`// (`可选)设置每个主机的最大请求数，数据类型为`INT`

```
clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);
```

`// (`可选)设置最大请求数，数据类型为`INT`

```
clientConfig.setMaxRequests(<maxRequests>);
```

`// (`可选)设置协议类型

```
clientConfig.setProtocolType(ProtocolType.HTTP);
```

`/**` （可选）请根据实际情况判断是否设置代理，设置方法如下：

```
clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

或

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

请替换为您实际的代理`IP+`端口 `*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### 3.2.4. 发起调用

本文介绍如何使用VPC Java SDK发起请求。高速通道使用VPC SDK实现功能。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例如DescribePhysicalConnections。 在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。

```
DescribePhysicalConnectionsRequest request = new DescribePhysicalConnectionsRequest();
```

`//` 业务参数

```
request.setPageSize(10); request.setPageNumber(1);
```

`//` 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用

```
request.putHeaderParameter("x-acs-organizationid", "1"); request.putHeaderParameter("x-acs-resourcegroupid", "");
```

3. 发起调用并处理应答。
高速通道

| DescribePhysicalConnectionsResponse response; try { DescribePhysicalConnectionsResponse response = client.getAcsResponse(request); System.out.println(new Gson().toJson(response)); } catch (ServerException e) { e.printStackTrace(); } catch (ClientException e) { e.printStackTrace(); } |  |  |  |  |
|---|---|---|---|---|
| 正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 |  | response.getXXX() |  | 来获得应答中的字段。 |
| instanceStatus := response.getStatus() |  |  |  |  |
| 如果出现了异常，或您需要原始HTTP应答的情况下，您可以通过以使用 | doAction() |  | 来获取原始应答。 |  |
| HttpResponse response = client.doAction(request); |  |  |  |  |

#### 3.2.5. 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息，包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try {
    FooResponse response = client.getAcsResponse(request);
```

`//` 处理`Response`

```
    // ...
}catch (ServerException e){
```

`//` 这里可以添加您自己的错误处理逻辑 `//` 例如，打印具体的错误信息

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`//` 如果遇上棘手问题，可以提交工单，并将`RequestId`提供给我们

```java
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
```

`//` 这里可以添加您自己的错误处理逻辑 `//` 例如，打印具体的错误信息

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
}
```

#### 3.2.6. 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式 （CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。 例如DescribePhysicalConnections接口，在发起CommonRequest请求时，需要使用 `request.setSysAction("DescribePhysicalConnections")` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为高速通道的 `DescribePhysicalConnections` 接口获取实例状态列表的调用示例（高速通道属于RPC的调用风格)。 高速通道

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionUD>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

```
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
```

请根据实际情况判断是否需要设置`HTTP`代理设置方法如下：

```
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

请替换为实际代理`IP+`端口 `*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```
        CommonRequest request = new CommonRequest();
```

`//` 替换为真实的产品域名

```
        request.setSysDomain("vpc.aliyuncs.com");
        request.setSysProduct("Vpc");
        request.setSysVersion("2016-04-28");
        request.setSysAction("DescribePhysicalConnections");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
```

request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// 非必填，请替换为您实际的资源集`ID`

```
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// 必填，请替换为您实际的组织ID
```

request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// 非必填(企业版`V3.15.0`及之前历史版本需要`),`请替换为您实际的地域`ID` // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修改、删除、查询单实例详情时需要）,请替换为您实际的实例`ID`

```
        /**
```

当使用`STS AccessKey`调用接口时需要在参数中加上`SecurityToken`字段调用方法如下：

```
        request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
```

请替换为实际的`Token` `*/`

```java
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClientException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
```

高速通道

## Python SDK调用

安装阿里云Python SDK，您就可以编写代码使用阿里云Python SDK访问专有云POP网关，调用Apsara Uni-manager运营控制台的API接口。

**前提条件**

已获取AccessKey或STS AccessKey，获取方式请参见获取AccessKey或STS AccessKey。 已获取Apsara Uni-manager运营控制台的Endpoint，获取方式请参见获取Apsara Uni-manager运营控制台的Endpoint。 阿里云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装阿里云Python SDK。

**说明**

推荐使用python3.x。 Python 3.x执行：
#安装阿里云`SDK`核心库。

```
pip3 install aliyun-python-sdk-core-v3
```

Python 2.x执行：
#安装阿里云`SDK`核心库。

```
pip install aliyun-python-sdk-core
```

**导入依赖包**

执行以下代码，导入Python SDK的依赖包。

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential
```

Python SDK支持通过AccessKey或STS AccessKey进行身份验证。

**重要**

确保包含AccessKey或STS AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
credentials = StsTokenCredential(
```

`'<yourAccessKeyID>', #` 请替换为您实际的`AccessKey ID`。 `'<yourAccessKeySecret>', #` 请替换为您实际的`AccessKey Secret`。

```
    '<yourSecurityToken>'
```

#使用`STS AccessKey`进行身份验证时，`<yourSecurityToken>`请替换为您实际的`SecurityToken`。
#使用`AccessKey`进行身份验证时，`<yourSecurityToken>`为`None`。
)

**说明**

以上代码示例中 `<yourAccessKeyID>` 、 `<yourAccessKeySecret>` 、 `<yourSecurityToken>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**创建并配置请求连接**

可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

```
client = AcsClient(region_id='<your-region-id>',
                   credential=credentials,
```

# （可选）设置创建连接超时时间，单位毫秒（`ms`）。

```
                   connect_timeout=<connectionTimeout>,
```

# （可选）设置读取超时时间，单位毫秒（`ms`）。

```
                   read_timeout=<readTimeout>,
```

# （可选）请根据实际情况判断是否设置代理，设置方法如下：

```bash
                   # proxy={
                   #     "http":"<http://192.168.XX.XX:33XX>",
                   #     "https":"<http://192.168.XX.XX:33XX>"
                   # }
```

)

**说明**

以上代码示例中 `<connectionTimeout>` 、 `<readTimeout>` 、 `<http://192.168.XX.XX:33XX>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。 高速通道
# 创建`API`请求并设置参数。

```
request = CommonRequest()
```

# 产品接口信息参数。

```
request.set_product("ascm") request.set_version('2019-05-10') request.set_uri_pattern("<yourCallUriPattern>")
```

# Apsara Uni-manager运营控制台的`Endpoint`地址。

```
request.set_domain('<ascmEndpoint>')
```

# 设置请求方式。

```
request.set_method('POST')
```

# 设置请求协议类型：`HTTP/HTTPS`。

```
request.set_protocol_type('https')
```

# 设置`Headers`。
# 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
request.add_header("x-acs-caller-sdk-source", "<yourCallerSdkSource>")
```

# 接口业务参数设置。

```
...
```

# 设置`Content-Type`。

```
request.set_content_type('application/json')
```

**说明**

以上代码示例中 `<yourCallUriPattern>` 、 `<ascmEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要您结合自身服务替换为其实际值，尖括号（<>）在最终代码中不保留。

**设置阿里云核心库SDK参数**

在使用阿里云核心库SDK发起API请求时，可以设置四种类型的参数：Path、Query、Body、Header。在调用具体API时，请根据开发文档中标注的参数位置对应设置。

| 参数类型 | 描述 | 示例 |
|---|---|---|
| Path | Path参数用于对请求Request中设置的UriPattern 进行变量替换。 例如：URI "/clusters/[ClusterId]" 中的 [ClusterId] 可以通过设置Path参数 "ClusterId=cluster1" 进行替换。 最终发起HTTP请求的URI则为 "/clusters/clusterId01" 。 | request = CommonRequest() request.set_uri_pattern("/clusters/[ClusterId]") request.add_path_param("ClusterId", "clusterId01") |
| Query | Query参数用于对请求Request中的URL参数进行设置（一般用于GET请求）。 例如：“http://aliyun.com/api/? ClusterId=clusterId01&ClusterName=cluster Name01”。 | request = CommonRequest() request.add_query_param("ClusterId", "clusterId01"); request.add_query_param("ClusterName", ""); |
| Body | Body参数用于对请求Request中的HTTP Content 进行设置（一般用于POST/PUT请求）。 目前支持两种格式： application/json application/x-www-form-urlencoded 说明在设置Body参数时，需要同时设置HTTP Content-Type。 | key-value形式设置Body参数，并设置HttpContentType。 request = CommonRequest() request.add_body_params("ClusterId", "clusterId01"); request.add_body_params("ClusterName", "clusterName01"); // 若Content-Type设置为application/x-www-form-urlencoded，请求数据格式为"ClusterId=clusterId01&ClusterName=clusterName01"的字符串。 request.set_content_type("application/x-www-form-urlencoded"); // 或，若Content-Type设置为application/json，请求数据格式为" {\"ClusterId\":\"clusterId01\",\"ClusterName\":\"clusterName01\"}"的JSON串。 request.set_content_type("application/json"); 自行构造请求HTTP Content并设置。 request = CommonRequest() //设置application/json格式的HTTP Content。 body = '''{"ClusterId": "clusterId01", "ClusterName": "clusterName01"}'''; request.set_content(body.encode("utf-8")); request.set_content_type("application/json"); //设置application/x-www-form-urlencoded格式的HTTP Content。 body = '''ClusterId=clusterId01&ClusterName=clusterName01'''; request.set_content(body.encode("utf-8")); request.set_content_type("application/x-www-form-urlencoded"); |
| Header | Header参数用于对请求Request中的HTTP Header进行设置。 | request = CommonRequest() request.add_header("x-acs-organizationid", "3") request.add_header("x-acs-resourcegroupid", "2") |

**发起调用并处理返回**

# 发起请求，并获取返回。

```python
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

高速通道

#### 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理，只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access keey is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
```

# 这里可以添加您自己的错误处理逻辑。
# 例如，打印具体的错误信息。

```
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

**完整调用示例**

| 以下代码为通过ASCM的 | GetOrganizationList | 接口获取组织列表的调用示例。 |
|---|---|---|
| # coding=utf-8 # 导入依赖包。 from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential # 本文提供的API调用样例仅供参考，更多详细API调用方法可参照开发文档中的“快速入门”。 credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials) # 创建API请求并设置参数。 request = CommonRequest() # Apsara Uni-manager运营控制台的接口信息参数。 request.set_product("ascm") request.set_version('2019-05-10') request.set_uri_pattern("/ascm/auth/organization/queryList") # Apsara Uni-manager运营控制台的Endpoint地址。 request.set_domain('<ascmEndpoint>') # 设置请求方式。 request.set_method('POST') # 设置请求协议类型。 request.set_protocol_type('http') # 设置Headers # 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。 request.add_header("x-acs-caller-sdk-source", "<yourCallerSdkSource>") # 调用专有云API时，一般需要提供多个公共Header参数，包括：x-acs-regionid、x-acs-organizationid、x-acs-resourcegroupid、x-acs-instanceid。详情可参照开发指南中的“获取公共Header参数"。 # 接口业务参数设置。 request.add_body_params("id", "1") request.set_content_type('application/json') # 发起请求，并获取返回。 response = client.do_action_with_exception(request) # python2: print(response) print(str(response, encoding='utf-8')) |  |  |

**说明**

以上代码示例中 `<yourRegionID>` 、 `<yourAccessKeyID>` 、 `<yourAccessKeySecret>` 、 `<ascmEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

### 快速开始

本节介绍如何获取VPC Python SDK并开始调用。高速通道使用VPC SDK实现功能。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参见获取AccessKey。 获取高速通道的Endpoint。具体操作，请参见获取高速通道的Endpoint。
1. 安装SDK核心库。
如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

高速通道如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

2. 安装SDK。
以下以安装VPC的SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装云服务器VPC的SDK：

```
pip install aliyun-python-sdk-vpc
```

如果您使用的是Python 3.x，执行以下命令，安装云服务器VPC的SDK：

```
pip3 install aliyun-python-sdk-vpc
```

**使用Python SDK**

以下示例以NAT网关为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

**说明**

涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <vpc.aliyuns.com>，请替换为您实际的产品访问地址。

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkvpc.request.v20160428 import DescribeNatGatewaysRequest
# global config
```

`region_id = '<yourRegionID>' #` 请替换为您实际的地域`ID` `access_key = '<yourAccessKeyID>' #` 请替换为您实际的的`AccessKey ID`

```bash
acces_secret = '<yourAccessKeySecret>' # 请替换为您实际的AccessKey Secret
# product config
```

`product_name = 'Vpc' #` 填写产品名称 `endpoint = '<vpc.aliyuns.com>' #` 产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeNatGatewaysRequest.DescribeNatGatewaysRequest()
```

`request.set_accept_format('json') #` 设置返回数据格式

```bash
# get response
response = clt.do_action_with_exception(request)
```

`print response #` 如果您使用的`Python 3.x`，此处请输入`print (response)`

### 使用手册

#### 4.2.1. 安装Python SDK

本文档介绍如何安装及调用VPC Python SDK。高速通道使用VPC SDK实现功能。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。

**说明**

使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用VPC的Python SDK，您需要安装阿里云Python SDK核心库和VPC的 Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

安装云产品的SDK，以下以安装VPC的SDK为例。 如果您使用的是Python 2.x，执行以下命令，安装VPC的SDK：

```
pip install aliyun-python-sdk-vpc
```

如果您使用的是Python 3.x，执行以下命令，安装VPC的SDK：

```
pip3 install aliyun-python-sdk-vpc
```

#### 4.2.2. 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 高速通道

**重要**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 4.2.3. 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。

**说明**

产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。 运行 `python -c "import ssl"` 检查Python环境是否支持OpenSSL。运行后，如果没有出现 `ImportError: No module named ssl` 的错误信息，说明已经支持 OpenSSL。 若没有OpenSSL，运行以下命令安装： `pip install pyopenssl # Python 2`使用此命令。

**说明**

若本地环境为Python 3，则运行 `pip3 install pyopenssl` 命令。

**设置单个请求的HTTP/HTTPS协议**

参考以下代码示例为一个接口设置HTTPS调用：

```java
import DescribeInstancesRequest request = DescribeInstancesRequest() request.set_protocol_type("https")
```

# 取值：`"https"` 或 `"http"`

**设置全局默认协议**

参考以下代码示例设置全局默认协议：

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
```

# 创建请求并调用 `client.do_action_with_exception()` 来发送请求

#### 4.2.4. 发起调用

本节介绍如何使用VPC Python SDK发起请求。高速通道使用VPC SDK实现功能。

**操作步骤**

1. 导入VPC的SDK。

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkvpc.request.v20160428 import DescribePhysicalConnectionsRequest
```

2. 新建一个AcsClient。

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. 创建Request对象。

```
request = DescribePhysicalConnectionsRequest.DescribePhysicalConnectionsRequest() request.set_accept_format('json')
```

4. 发起调用并处理返回。

```
response = clt.do_action_with_exception(request)
```

`print response #` 如果您使用的`Python 3.x`，此处为`print (response)`

#### 4.2.5. 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。 高速通道

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
```

# 这里可以添加您自己的错误处理逻辑
# 例如，打印具体的错误信息

```
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

#### 4.2.6. 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式 （CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 RPC风格的API： 您需要获取**Action**参数，使用 `request.set_action_name('Action')` 的方式来指定API名称。 例如DescribePhysicalConnections接口，在发起CommonRequest请求时，需要使用 `request.set_action_name('DescribePhysicalConnections')` 来指定API名称。

**示例：调用RPC风格的API**

| 以下代码为高速通道的 | DescribePhysicalConnections | 接口，获取实例状态列表的调用示例。 |
|---|---|---|
| 说明以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <vpc.aliyuncs.com>，请替换为您实际的产品访问地址。 |  |  |

高速通道

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Vpc') request.set_action_name('DescribePhysicalConnections') request.set_version('2016-04-28')
```

`request.set_domain('<vpc.aliyuncs.com>') #`产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# or:
# request = = CommonRequest(product='Vpc', action_name='DescribePhysicalConnections',version='2016-04-28',domain='vpc.aliyuncs.com')
######
```

# 设置请求协议类型,支持`https`或`http,`默认为`http`
# 设置`https`方法如下：

```bash
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
```

# 当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段
# 调用方法如下：

```bash
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
```

# 请替换为您实际的`SecurityToken`

```
######
```

# 非必填，请替换为您实际的资源集`ID`

```
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
```

# 必填，请替换为您实际的组织`ID`

```
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
```

# 非必填（企业版`V3.15.0`及之前历史版本需要），请替换为您实际的地域`ID`

```
request.add_header("x-acs-regionid", "<yourRegionID>")
```

# 非必填（修改、删除、查询单实例详情时需要），请替换为您实际的实例`ID`

```python
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

高速通道

## Go SDK调用

安装阿里云Go SDK后，您可以编写代码使用阿里云Go SDK访问阿里云POP网关，调用Apsara Uni-manager运营控制台的API接口。

**前提条件**

已获取AccessKey或STS AccessKey，获取方式请参见获取AccessKey或STS AccessKey。 已获取Apsara Uni-manager运营控制台的Endpoint，获取方式请参见获取Apsara Uni-manager运营控制台的Endpoint。 阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令下载安装Go SDK核心库。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

若出现网络报错，可尝试使用以下两种方式下载。 使用官方提供的下载方式。

```
GOPROXY=https://goproxy.cn,direct go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

使用代理服务器下载。

```
go env -W GOPROXY='https://goproxy.cn,direct'
```

Go SDK支持通过AccessKey或STS AccessKey进行身份验证。

**重要**

确保包含AccessKey或STS AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
credential := credentials.NewStsTokenCredential(
```

`"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKey Secret`。

```
    "<yourStsToken>",
```

`//` 在使用`STS AccessKey`进行身份验证时，`<yourStsToken>`需替换为您实际的`Security Token`。 `//` 在使用`AccessKey`进行身份验证时，`<yourStsToken>`为`""`。 )

**说明**

以上代码示例中 `<yourAccessKeyID>` 、 `<yourAccessKeySecret>` 、 `<yourSecurityToken>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**创建并配置请求连接**

可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

```
client, err := sdk.NewClientWithOptions("<your-region-id>", sdk.NewConfig(), credential) if err != nil {
    panic(err)
}
```

`//` 设置是否忽略证书。`true`：忽略；`false`：不忽略。

```
client.SetHTTPSInsecure(true)
```

`//`（可选）设置创建连接超时时间，单位纳秒。计算公式为：X秒`*time.Second=X*1000000000`纳秒

```
client.SetConnectTimeout(1 * time.Second)
```

`//` （可选）设置读取超时时间，单位纳秒。计算公式为：X秒`*time.Second=X*1000000000`纳秒

```
client.SetReadTimeout(10 * time.Second)
```

`/**` （可选）请根据实际情况判断是否设置代理，设置方法如下。请替换为您实际的代理`IP+`端口。

```
client.SetHttpProxy("<http://192.168.XX.XX:33XX>") client.SetHttpsProxy("<https://192.168.XX.XX:33XX>")
```

`*/`

**说明**

以上代码示例中 `<connectionTimeout>` 、 `<readTimeout>` 、 `<http://192.168.XX.XX:33XX>` 均为可变参数，需要您结合自身服务替换为其实际值，尖括号 （<>）在最终代码中不保留。

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。 高速通道 `//` 创建`API`请求并设置参数。

```
request := requests.NewCommonRequest()
```

`// Apsara Uni-manager`运营控制台接口信息参数。

```
request.Product ="ascm" request.Version = "2019-05-10"
```

`//`被调用接口的`Restful`路径，例如`GetOrganizationList`接口的`Restful`路径为：`/ascm/auth/organization/queryList`。其它接口请查看对应接口文档。

```
request.PathPattern = "<yourCallUriPattern>"
```

`// Apsara Uni-manager`运营控制台的`Endpoint`地址

```
request.Domain = "<ascmEndpoint>"
```

`//` 设置请求方式。

```
request.Method = "POST"
```

`//` 设置协议类型，`https`或`http`。

```
request.Scheme = "https"
```

`//` 设置`Headers`。 `//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
request.Headers["x-acs-caller-sdk-source"] = "<yourCallerSdkSource>"
```

`//` 接口业务参数设置。

```
...
```

`//` 设置`Content-Type`。

```
request.SetContentType("application/json")
```

**说明**

以上代码示例中 `<yourCallUriPattern>` 、 `<ascmEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要您结合自身服务替换为其实际值，尖括号（<>）在最终代码中不保留。

**设置阿里云核心库SDK参数**

在使用阿里云核心库SDK发起API请求时，可以设置四种类型的参数：Path、Query、Body、Header。在调用具体API时，请根据开发文档中标注的参数位置对应设置。

| 参数类型 | 描述 | 示例 |
|---|---|---|
| Path | Path参数用于对请求Request中设置的UriPattern 进行变量替换。 例如：URI "/clusters/[ClusterId]" 中的 [ClusterId] 可以通过设置Path参数 "ClusterId=cluster1" 进行替换。 最终发起HTTP请求的URI则为 "/clusters/clusterId01" 。 | request := requests.NewCommonRequest() request.PathPattern = "/clusters/[ClusterId]" request.PathParams["ClusterId"] = "clusterId01" |
| Query | Query参数用于对请求Request中的URL参数进行设置（一般用于GET请求）。 例如：“http://aliyun.com/api/? ClusterId=clusterId01&ClusterName=cluster Name01”。 | request := requests.NewCommonRequest() request.QueryParams["ClusterId"] = "clusterId01" request.QueryParams["ClusterName"] = "clusterName01" |
| Body | Body参数用于对请求Request中的HTTP Content 进行设置（一般用于POST/PUT请求）。 目前支持两种格式： application/json application/x-www-form-urlencoded 说明在设置Body参数时，需要同时设置HTTP Content-Type。 | 自行构造HTTP Content并直接设置HttpContent。 request := requests.NewCommonRequest() //设置application/json格式的HTTP Content。 body := `{"ClusterId":"clusterId01","ClusterName":"clusterName01"}` request.Content = []byte(body) request.SetContentType(requests.Json) //设置application/x-www-form-urlencoded格式的HTTP Content。 body := `ClusterId=clusterId01&ClusterName=clusterName01` request.Content = []byte(body) request.SetContentType(requests.Form) |
| Header | Header参数用于对请求Request中的HTTP Header进行设置。 | request := requests.NewCommonRequest() request.Headers["x-acs-organizationid"] = "3" request.Headers["x-acs-resourcegroupid"] = "2" |

**发起调用并处理返回**

可参考以下代码发起请求并处理返回结果。 高速通道

```
response, err := client.ProcessCommonRequest(request) if err != nil {
   panic(err)
} fmt.Print(response.GetHttpContentString())
```

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即sdk.errors包下的ClientError和ServerError。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个ClientError，您可以通过以下代码来判断并获取ClientError中的错误信息。

**重要**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法可参考以下代码。

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包。

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := client.ProcessCommonRequest(request) if clientError, ok := err.(*errors.ClientError); ok{
```

`//` 获取错误码。

```
    clientError.ErrorCode()
```

`//` 获取错误描述。

```
    clientError.Message()
```

`//` 获取原始错误（可能为`nil`）。

```
    clientError.OriginError()
}
```

**ServerError**

当服务端返回错误的应答时，SDK会将该应答封装成ServerError返回。在这种情况下，您依然可以从Response中获得原始的HTTP应答，，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息。

**重要**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法可参考以下代码。

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包。

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := client.ProcessCommonRequest(request) if serverError, ok := err.(*errors.ServerError); ok{
```

`//` 获取错误码。

```
    serverError.ErrorCode()
```

`//` 获取错误描述。

```
    serverError.Message()
```

`//` 获取原始`HTTP`应答。

```
    response.GetOriginHttpResponse()
}
```

**完整调用示例**

以下代码为通过ASCM的 `GetOrganizationList` 接口获取组织列表的调用示例。 高速通道

```java
package main import (
 "fmt"
 "time"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```
func main() {
 credential := credentials.NewStsTokenCredential(
```

`"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKey Secret`。 `"<yourStsToken>", //` 请替换为您实际的`Security Token`（非`STS`调用时为`""`）。 )

```
 client, err := sdk.NewClientWithOptions("<yourRegionID>", sdk.NewConfig(), credential)
 if err != nil {
  panic(err)
 }
```

`//` 设置是否忽略证书。

```
 client.SetHTTPSInsecure(true)
```

`//` （可选）设置创建连接超时时间。

```
 client.SetConnectTimeout(1 * time.Second)
```

`//` （可选）设置读取超时时间。

```
 client.SetReadTimeout(10 * time.Second)
```

`/**` （可选）请根据实际情况判断是否设置代理，设置方法如下。请替换为您实际的代理`IP+`端口。

```
 client.SetHttpProxy("<http://192.168.XX.XX:33XX>")
 client.SetHttpsProxy("<https://192.168.XX.XX:33XX>")
```

`*/`

```
 request := requests.NewCommonRequest()
 request.Product = "ascm"
 request.Version = "2019-05-10"
```

`//`被调用接口的`Restful`路径，例如`GetOrganizationList`接口的`Restful`路径为：`/ascm/auth/organization/queryList`。其它接口请查看对应接口文档。

```
 request.PathPattern = "/ascm/auth/organization/queryList"
 request.Domain = "<ascmEndpoint>"
 request.Method = "POST"
 request.Scheme = "https" // https | http
 request.Headers["Content-Type"] = "application/json"
 request.Headers["x-acs-caller-sdk-source"] = "<yourCallerSdkSource>"
 request.SetContentType("application/json")
 body := `{"id": "1"}`
 request.Content = []byte(body)
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  if clientError, ok := err.(*errors.ClientError); ok {
```

`//` 获取错误码。

```
   fmt.Println(clientError.ErrorCode())
```

`//` 获取错误描述。

```
   fmt.Println(clientError.Message())
```

`//` 获取原始错误（可能为`nil`）。

```
   fmt.Println(clientError.OriginError())
   return
  } else if serverError, ok := err.(*errors.ServerError); ok {
```

`//` 获取错误码。

```
   fmt.Println(serverError.ErrorCode())
```

`//` 获取错误描述。

```
   fmt.Println(serverError.Message())
```

`//` 获取原始`HTTP`应答。

```
   fmt.Println(response.GetOriginHttpResponse())
   return
  } else {
   fmt.Println(err.Error())
   return
  }
 }
 fmt.Print(response.GetHttpContentString())
}
```

**说明**

以上代码示例

```
中 <yourRegionID> 、 <yourAccessKeyID> 、 <yourAccessKeySecret> 、 <http://192.168.XX.XX:33XX> 、 <ascmEndpoint> 、 <yourCallerSdkSource> 均
```

为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问。本操作介绍如何获取阿里云VPC Go SDK并开始调用。高速通道使用VPC SDK实现功能。

**环境准备**

使用Go SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参见获取AccessKey。 高速通道获取高速通道关的Endpoint。具体操作，请参见获取高速通道的Endpoint。

**安装阿里云Go SDK核心包**

阿里云Go SDK支持Go 1.10.x及更高版本，您可以通过执行以下命令安装Go SDK核心包。您可以在阿里云Go SDK源码库查看已安装的核心包是否为最新版本。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**使用Go SDK**

以下这个代码示例展示了调用阿里云Go SDK的3个主要步骤：
1. 初始化Client实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

**说明**

涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您实际的Endpoint。

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

)

```
func main() {
```

`//` 创建`vpcClient`实例

```
    vpcClient, err := vpc.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
    if err != nil {
```

`//` 异常处理

```
        panic(err)
    }
```

`//` 创建`API`请求并设置参数

```
    request := vpc.CreatDescribePhysicalConnectionsRequest()
```

`//` 设置当前产品的`Endpoint`

```
    request.Domain = "<Endpoint>"
    // 等价于 request.PageSize = "10"
    request.PageSize = requests.NewInteger(10)
```

`//` 发起请求并处理异常

```
    response, err := vpcClient.DescribePhysicalConnections(request)
    if err != nil {
```

`//` 异常处理

```
        panic(err)
    }
    fmt.Println(response)
}
```

4. （可选）切换HTTP/HTTPS协议。

```
request.Scheme = "HTTPS"
```

### 使用手册

#### 5.2.1. 安装Go SDK核心包

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 5.2.2. 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的阿里云账号的信息安全。

**重要**

以下代码以高速通道为例，展示初始化vpcClient实例。 `//` 初始化`vpcClient`实例

```
vpcClient, err := vpc.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

高速通道

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 5.2.3. 发起调用

本文介绍如何使用阿里云VPC Go SDK发起调用。高速通道使用VPC SDK实现功能。 以下步骤以高速通道为例，展示使用VPC Go SDK发起调用。
1. 导入VPC SDK。

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/vpc
```

2. 新建一个VPC Client，该client中包含VPC的所有API。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 `vpcClient,err := <vpc>.NewClientWithAccessKey( //`请替换为您实际的产品名称 `"<yourRegionID>", //` 请替换为您实际的`RegionID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>") //` 请替换为您实际的`AccessKeySecret` `vpcClient.Domain = "vpc.aliyuns.com" //`设置请求域名地址，当前为示例值，请求根据实际请求地址替换。
3. 使用 `xxx.CreateXXXRequest` 方法创建一个请求。
该方法的命名规范为 ${service}.Create${apiName}Request ，其中：
**${service}**为产品名称(小写)。例如vpc。
**${apiName}**为API名称，例如DescribePhysicalConnections。

```
request := vpc.CreateDescribePhysicalConnectionsRequest() request.InstanceId = ""
```

4. 发起调用。

```
response, err := vpcClient.DescribePhysicalConnections(request)
```

#### 5.2.4. 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。

```
response,err := vpcClient.DescribePhysicalConnections(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

|  | ClientError |
|---|---|
| ClientError |  |

**重要**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法请参考：

```java
package main import (
```

`"github.com/aliyun/alibaba-cloud-sdk-go/services/vpc" //vpc`请替换为您实际的产品名称

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := vpcClient.DescribePhysicalConnections(request) if clientError, ok := err.(*errors.ClientError); ok{
```

`//` 获取错误码

```
    clientError.ErrorCode()
```

`//` 获取错误描述

```
    clientError.Message()
```

`//` 获取原始错误(可能为`nil)`

```
    clientError.OriginError()
}
```

**ServerError**

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从Response中获得原始的HTTP应答。 以下以高速通道为例，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息： 高速通道

**重要**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法请参考：

```java
package main import (
```

`"github.com/aliyun/alibaba-cloud-sdk-go/services/vpc" //vpc`请替换为您实际的产品名称

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := vpcClient.DescribePhysicalConnections(request) if serverError, ok := err.(*errors.ServerError); ok{
```

`//` 获取错误码

```
    serverError.ErrorCode()
```

`//` 获取错误描述

```
    serverError.Message()
```

`//` 获取原始`http`应答

```
    response.GetOriginHttpResponse()
}
```

#### 5.2.5. 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式 （CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**示例：调用RPC风格的API**

| 以下代码为云产品高速通道的 | DescribePhysicalConnections | 接口，获取实例状态列表的调用示例（高速通道属于RPC的调用风格）： |
|---|---|---|
| 说明以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <vpc.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 |  |  |

高速通道

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey(
```

`"<yourRegionID>", //`请替换为您实际的地域`ID` `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID` `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`

```
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Method = "POST"
```

`request.Domain = "<vpc.aliyuncs.com>" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "Vpc"
    request.Version = "2016-04-28"
```

`//` 因为是`RPC`接口，因此需指定`APIName(Action)`

```
    request.ApiName = "DescribePhysicalConnections"
```

`//` 业务参数

```
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*` 当使用`STS AccessKey`调用`RPC`接口时，需要在参数中加上`SecurityToken`字段调用方式如下：

```
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
```

请替换为您实际的`SecurityToken` `*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // 非必填，调用来源说明
```

`request.Headers["x-acs-regionid"] = "<yourRegionID>" //` 非必填（企业版`V3.15.0`及之前历史版本需要），请替换为您实际的地域`ID` `request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" //` 非必填，请替换为您实际的资源集`ID` `request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" //` 非必填，请替换为您实际的组织`ID` `// request.Headers["x-acs-instanceid"] = "<yourInstanceID>" //` 非必填（修改、删除、查看单实例详情时需要），请替换为您实际的实例`ID`

```
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

高速通道

## API参考

### API概览

本文介绍高速通道提供的接口。

| API | 描述 |
|---|---|
| 物理专线 |  |
| CreatePhysicalConnection | 申请物理专线接入。 |
| DescribeAccessPoints | 查询指定地域中的物理专线接入点。用ConnectRouterInterface接口由发起端路由器接口向接收端发起连接。 |
| CancelPhysicalConnection | 取消物理专线接入。 |
| DescribePhysicalConnections | 查询指定地域内的物理专线。 |
| ModifyPhysicalConnectionAttribute | 修改物理专线的配置。 |
| TerminatePhysicalConnection | 终止物理专线接入。 |
| EnablePhysicalConnection | 开通处于Confirmed状态的物理专线。 |
| DeletePhysicalConnection | 删除物理专线。 |
| CreatePhysicalConnectionOccupancyOrder | 创建资源占用费订单。 |
| ApplyPhysicalConnectionLOA | 申请LOA。 |
| CreatePhysicalConnectionSetupOrder | 创建端口初装费订单。 |
| CompletePhysicalConnectionLOA | 完成施工完竣。 |
| DescribePhysicalConnectionLOA | 查询物理专线LOA信息。 |
| 边界路由器 |  |
| CreateVirtualBorderRouter | 创建边界路由器VBR（Virtual Border Router）实例。 |
| DeleteVirtualBorderRouter | 删除VBR实例。 |
| ModifyVirtualBorderRouterAttribute | 修改VBR实例的配置。 |
| DescribeVirtualBorderRouters | 查询已创建的VBR实例。 |
| DescribeVirtualBorderRoutersForPhysicalConnection | 查询指定物理专线下的VBR实例，包括物理专线所有者的VBR实例和其他账号的VBR实例。 |
| TerminateVirtualBorderRouter | 终止VBR实例。 |
| RecoverVirtualBorderRouter | 恢复被终止的VBR实例。 |
| AssociatePhysicalConnectionToVirtualBorderRouter | 将VBR实例关联至物理专线。 |
| UnassociatePhysicalConnectionFromVirtualBorderRou ter | 解绑VBR实例和物理专线。 |
| BGP |  |
| CreateBgpGroup | 为指定的VBR实例创建一个BGP组。 |
| DescribeBgpGroups | 查询指定地域下的BGP组。 |
| ModifyBgpGroupAttribute | 修改BGP组的配置。 |
| DeleteBgpGroup | 删除指定的BGP组。 |
| CreateBgpPeer | 向指定的BGP组中添加BGP邻居。 |
| DescribeBgpPeers | 查询指定地域下的BGP邻居。 |
| ModifyBgpPeerAttribute | 修改BGP邻居的属性。 |
| DeleteBgpPeer | 删除指定的BGP邻居。 |
| AddBgpNetwork | 宣告BGP网段。 |
| DescribeBgpNetworks | 查询已宣告的BGP网络。 |
| DeleteBgpNetwork | 删除已宣告的BGP网络。 |
| 路由器接口 |  |
| CreateRouterInterface | 创建路由器接口。 |
| ConnectRouterInterface | 由发起端路由器接口向接收端发起连接。 |
| DeactivateRouterInterface | 冻结路由器接口。 |
| ModifyRouterInterfaceSpec | 修改路由器接口的规格。 |
| DeleteRouterInterface | 删除路由器接口。 |

高速通道

| DescribeRouterInterfaces | 查询指定地域内的路由器接口。 |
|---|---|
| ActivateRouterInterface | 激活处于Inactive状态的路由器接口。 |
| ModifyRouterInterfaceAttribute | 修改路由器接口的配置。 |

### 调用API

#### 6.2.1. 请求结构

高速通道接口调用是向高速通道API的服务端地址发送HTTP GET请求。您需要按照接口描述在请求中加入相应请求参数，调用后系统会返回处理结果。请求及返回结果都使用UTF-8字符集进行编码。 高速通道的API是RPC风格，您可以通过发送HTTP GET请求调用高速通道API。 其请求结构如下：

```
http://Endpoint/?Action=xx&Parameters
```

其中：

| Endpoint：高速通道API 的服务接入地址为 | vpc.example.com | 。 |
|---|---|---|
| 说明 example.com 是项目自定义的访问域名。关于如何获取Endpoint，请参见获取高速通道的Endpoint。 |  |  |

**Action**：要执行的操作，如使用CreateRouterInterface创建路由器接口。
**Version**：要使用的API版本，专有网络的API版本是2016-04-28。
**Parameters**：请求参数，每个参数之间用and（&）分隔。
请求参数由公共请求参数和API自定义参数组成。公共参数中包含API版本号、身份验证等信息，更多信息，请参见公共参数。

**说明**

为了便于用户查看，本文档中的示例都做了格式化处理。

```
https://vpc.example.com/?Action=CreateRouterInterface &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 6.2.2. API授权

为了确保您的账号安全，建议您使用子账号的身份凭证调用API。如果您使用RAM账号调用高速通道API，您需要为该RAM账号创建、附加相应的授权策略。

#### 6.2.3. API签名

高速通道服务会对每个API请求进行身份验证，无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。 高速通道通过使用AccessKey ID和AccessKey Secret进行对称加密的方法来验证请求的发送者身份。AccessKey是为阿里云账号和RAM用户发布的一种身份凭证(类似于用户的登录密码)，其中AccessKey ID 用于标识访问者的身份，AccessKey Secret是用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密。关于如何创建 RPC API需按如下格式在请求中增加签名（Signature）：

| https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf |  |  |  |
|---|---|---|---|
| 以CreateRouterInterface为例，假设AccessKey ID是 | testid | ， AccessKey Secret是 | testsecret |
| http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 |  |  |  |

完成以下步骤计算签名：
1. 使用请求参数创建待签名字符串：

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpcs&Format%3DXML&SignatureMethod%3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f- 4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. 计算待签名的HMAC的值。
在AccessKey Secret后添加一个and（&）作为计算HMAC值的key。本示例中的key为 `testsecret&` 。 高速通道

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. 将签名加到请求参数中：

```
http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### RAM鉴权

在使用RAM账号调用高速通道API前，需要主账号通过创建授权策略对RAM账号进行授权。在授权策略中，使用资源描述符（Alibaba Cloud Resource Name, ARN）指定授权资源。

**可授权的资源类型**

下表列举了高速通道中可授权的资源及其描述方式：

| 资源类型 | 授权策略中的资源描述方法 |
|---|---|
| 专有网络（VPC） | acs:vpc:$regionid:$accountid:vpc/$vpcid |
|  | acs:vpc:$regionid:$accountid:vpc/* |
|  | acs:vpc:*:$accountid:vpc/* |
| 路由器（VRouter） | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
|  | acs:vpc:$regionid:$accountid:vrouter/* |
|  | acs:vpc:*:$accountid:vrouter/* |
| 交换机（VSwitch） | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
|  | acs:vpc:$regionid:$accountid:vswitch/* |
|  | acs:vpc:*:$accountid:vswitch/* |
| 路由表（Route Table） | acs:vpc:$regionid:$accountid:routetable/$routetableid |
|  | acs:vpc:$regionid:$accountid:routetable/* |
|  | acs:vpc:*:$accountid:routetable/* |
| 弹性公网IP（EIP） | acs:vpc:$regionid:$accountid:eip/$allocationid |
|  | acs:vpc:$regionid:$accountid:eip/* |
|  | acs:vpc:*:$accountid:eip/* |
| NAT网关（NAT Gateway） | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
|  | acs:vpc:$regionid:$accountid:natgateway/* |
|  | acs:vpc*:$accountid:vpc/* |
| NAT网关带宽包（NAT Gateway Bandwidth Package） | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/* |
|  | aacs:vpc:*:$accountid:vpc/* |
| 端口转发表（Forward Table） | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
|  | acs:vpc:$regionid:$accountid:forwardtable/* |
|  | acs:vpc:*:$accountid:vpc/* |
| SNAT表（SNAT Table） | acs:vpc:$regionid:$accountid:snattable/$snattableid |
|  | acs:vpc:$regionid:$accountid:snattable/* |
|  | acs:vpc:*:$accountid:vpc/* |
| 通用资源 | acs:vpc:$regionid:$accountid:* |
|  | acs:vpc:*:$accountid:* |

其中 $regionid/accoutid/vrouterid 为具体的资源ID， * 代表对应的所有资源。

**可授权的接口**

高速通道下表列举了可授权的API及其描述方式：

| API | 资源描述 |
|---|---|
| vpc:CreateVpc | acs:vpc:$regionid:$accountid:vpc/* |
| vpc:DeleteVpc | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DescribeVpcs | vpc:$regionid:$accountid:vpc/* |
| vpc:ModifyVpcAttribute | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DescribeVRouters | acs:vpc:$regionid:$accountid:vrouter/* |
|  | 指定要查询的VRouterId： "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |
|  | 未指定要查询的VRouterId： "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/*" |
| vpc:ModifyVRouterAttribute | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
| vpc:CreateVSwitch | acs:vpc:$regionid:$accountid:vswitch/* |
|  | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DeleteVSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
| vpc:DescribeVSwitches | acs:vpc:$regionid:$accountid:vswitch/* |
|  | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |
| vpc:ModifyVSwitchAttribute | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
| vpc:CreateRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |
| vpc:DeleteRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |
| vpc:DescribeRouteTables | acs:vpc:$regionid:$accountid:routetable/* |
|  | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vrouterid" |
| vpc:AllocateEipAddress | acs:vpc:$regionid:$accountid:eip/* |
| vpc:AssociateEipAddres | acs:vpc:$regionid:$accountid:eip/* |
|  | 绑定ECS实例 acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |
| vpc:DescribeEipAddresses | acs:vpc:$regionid:$accountid:eip/* |
| vpc:UnassociateEipAddress | 绑定ECS实例 acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |
| vpc:ReleaseEipAddress | acs:vpc:$regionid:$accountid:eip/$allocationid |
| vpc:DescribeEipMonitorData | acs:vpc:$regionid:$accountid:eip/$allocationid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| vpc:CreateNatGateway | acs:vpc:$regionid:$accountid:natgateway/* |
| vpc:DescribeNatGateways | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
|  | acs:vpc:$regionid:$accountid:natgateway/* |
| vpc:ModifyNatGatewaySpec | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
| vpc:ModifyNatGatewayAttribute | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| vpc:DeleteNatGateway | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| vpc:CreateBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/* |
| vpc:DescribeBandwidthPackages | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/* |
| vpc:ModifyBandwidthPackageSpec | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |

高速通道

| vpc:ModifyBandwidthPackageAttribute | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
|---|---|
| vpc:AddBandwidthPackageIps | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:RemoveBandwidthPackageIps | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:DeleteBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:CreateForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
| vpc:DeleteForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
| vpc:ModifyForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
| vpc:DescribeForwardTableEntries | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
| vpc:CreateSnatEntry | acs:vpc:$regionid:$accountid:snattable/* |
| vpc:ModifySnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |
| vpc:DescribeSnatTableEntries | acs:vpc:$regionid:$accountid:snattable/$snattableid |
| vpc:DeleteSnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |

### 公共参数

本文介绍高速通道API调用过程中需要使用的公共参数。

**公共请求参数**

公共请求参数是每个接口都需要使用到的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回消息的格式。取值： JSON (默认值) \| XML |
| Version | String | 是 | API版本号，使用 YYYY-MM-DD 日期格式。取值： 2016-04-28 |
| AccessKeyId | String | 是 | 访问服务使用的密钥ID。 |
| Signature | String | 是 | 签名结果串。 |
| SignatureMethod | String | 是 | 签名方式，取值： HMAC-SHA1 |
| Timestamp | String | 是 | 请求的时间戳，为日期格式。使用UTC时间按照 ISO8601标准，格式为 YYYY-MM-DDThh:mm:ssZ 。 例如，北京时间2013年1月10日20点0分0秒，表示为2013-01-10T12:00:00Z。 |
| SignatureVersion | String | 是 | 签名算法版本，取值： 1.0 |
| SignatureNonce | String | 是 | 唯一随机数，用于防止网络重放攻击。 在不同请求间要使用不同的随机数值。 |

示例

```
http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

**公共返回参数**

API返回结果采用统一格式，返回2xx HTTP状态码代表调用成功；返回4xx或5xx HTTP状态码代表调用失败。调用成功返回的数据格式有XML和JSON两种，可以在发送请求时指定返回的数据格式，默认为XML格式。 每次接口调用，无论成功与否，系统都会返回一个唯一识别码**RequestId**。 XML格式高速通道

```xml
<?xml version="1.0" encoding="utf-8"?>
```

<!—结果的根结点`-->` <接口名称`+Response>` <!—返回请求标签`-->`

```xml
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
```

<!—返回结果数据`-->` `</`接口名称`+Response>` JSON格式

```json
{
      "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
```

`/*`返回结果数据`*/`

```
  }
```

### 物理专线

#### 6.5.1. CreatePhysicalConnection

**使用说明**

申请完成后，物理专线的状态为**Initial**，请联系运营商进行施工。 调用该接口时，请注意： 申请物理专线时，处于**Enabled**状态之外的物理专线不得超过5条。 若账号下存在欠费状态的物理专线，则不能再申请物理专线。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreatePhysicalConnection | 要执行的操作。 取值：CreatePhysicalConnection。 |
| AccessPointId | String | 是 | ap-cn-beijing-**** | 物理专线所在的接入点ID。 |
| ClientToken | String | 是 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| LineOperator | String | 是 | CT | 提供接入物理线路的运营商。 CT：中国电信。 CU：中国联通。 CM：中国移动。 CO：中国其他。 Equinix：Equinix。 Other：境外其他。 |
| PeerLocation | String | 是 | XX街道 | 本地数据中心的地理位置。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| Type | String | 否 | VPC | 物理专线的类型。默认值：VPC。 |
| bandwidth | Integer | 否 | 10 | 带宽包的带宽。单位：Mbps。取值范围：5～5000。 |
| PortType | String | 否 | 1000Base-T | 物理专线接入端口类型。 100Base-T：百兆电口。 1000Base-T：千兆电口。 1000Base-LX：千兆单模光口（10千米）。 10GBase-T：万兆电口。 10GBase-LR：万兆单模光口（10千米）。 |
| RedundantPhysicalConnectio nId | String | 否 | pc-119mfjzm7****** | 冗余物理专线的实例ID。该专线的状态必须为Allocated、Confirmed或Enabled。 |
| Description | String | 否 | 物理专线的描述信息 | 物理专线的描述信息。 长度为2～256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |

高速通道

| Name | String | 否 | test | 物理专线的名称。 长度为2～128个字符，必须以字母或中文开头，可包含数字、下划线 （_）和短划线（-），但不能以 http:// 或 https:// 开头。 |
|---|---|---|---|---|
| CircuitCode | String | 否 | longtel001 | 运营商为物理专线提供的电路编码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PhysicalConnectionId | String | pc-bp12mw****** | 物理专线实例ID。 |
| RequestId | String | 8A6A5EC5-6F6C-4906-9689- 56ACE58A13E0 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreatePhysicalConnection &AccessPointId=ap-cn-beijing-**** &ClientToken=123e4567-e89b-12d3-a456-426655440000 &LineOperator=CT &PeerLocation=XX街道 &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreatePhysicalConnectionResponse> <RequestId>8A6A5EC5-6F6C-4906-9689-56ACE58A13E0</RequestId> <PhysicalConnectionId>pc-bp12mw******</PhysicalConnectionId> </CreatePhysicalConnectionResponse> |  |

| JSON | 格式 |
|---|---|
| { "CreatePhysicalConnectionResponse": { "RequestId": "8A6A5EC5-6F6C-4906-9689-56ACE58A13E0", "PhysicalConnectionId": "pc-bp12mw******" } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAccessPointId.NotEnabled | Invalid access point status. | 接入点状态不可用。 |
| 400 | InvalidType.Malformd | The Type provided was invalid. | 参数Type的值不合法。 |
| 400 | InvalidPeerLocation.Malformd | The PeerLocation provided was invalid. | 参数PeerLocation的值不合法。 |
| 400 | InvalidLineOperator.Malformd | The LineOperator provided was invalid. | 参数LineOperator的值不合法。 |
| 400 | InvalidPortType.Malformd | The PortType provided was invalid. | 该端口类型不合法。 |
| 400 | InvalidDescription.Malformed | The specifid ?Description? is not valid. | 指定的资源描述格式不合法。长度为2～256个字符，不能以http://和https://开头。 |
| 400 | InvalidRedundantPhysicalConnect ionId.NotFound | The RedundantPhysicalConnectionId does not found. | 冗余物理专线不存在。 |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | 该名称格式不合法。 |
| 400 | QuotaExceeded.pConnPerAP | Physical connection count per ap quota exceed. | 超过接入点的物理专线配额。 |
| 400 | InvalidBandwidth | invalid physical connection banwidth. | 物理专线的带宽不合法。 |
| 400 | InvalidRedundantPhysicalConnect ion | redundant physical connection doesn't belong to current user. | 该冗余物理专线不属于您的账号。 |
| 400 | InvalidRedundantPhysicalConnect ionStatus | invalid redundant physical connection status. | 冗余物理专线状态不合法。 |
| 400 | InvalidCircuitCode.Malformed | circuitCode is illegal. | 该CircuitCode不合法。 |
| 400 | QuotaExceeded.freePconnPerAP | free physical connections count excceeded. | 超过物理专线配额。 |

#### 6.5.2. DescribeAccessPoints

高速通道

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAccessPoints | 要执行的操作。 取值：DescribeAccessPoints。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 接入点所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| Filter.N.Key | String | 否 | name | 过滤条件，最多可提供5个过滤条件。 |
| Filter.N.Value.N | RepeatList | 否 | test | 根据Key指定过滤值。一个Key支持指定多个过滤值，每个过滤值之间是或的关系，即只要符合其中一个过滤值，则视为匹配该过滤条件。 |
| Type | String | 否 | VPC | 物理专线的网络类型。默认值：VPC。 |
| Name | String | 否 | 杭州-余杭-C | 接入点名称。 |
| HostOperator | String | 否 | 中国电信 | 接入点所属的运营商。 中国移动中国联通中国电信中国其他国际运营商 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AccessPointSet | Array of AccessPointType |  | 接入点信息。 |
| AccessPointType |  |  |  |
| AccessPointId | String | ap-cn-hangzhou-**** | 接入点ID。 |
| AttachedRegionNo | String | cn-qingdao-env66-d01 | 接入点所在的地域ID。 |
| Description | String | 接入点描述信息 | 接入点描述信息。 |
| HostOperator | String | 中国电信 | 接入点所属的运营商。 中国移动中国联通中国电信中国其他国际运营商 |
| Location | String | 青岛 | 接入点所在的位置。 |
| Name | String | 青岛-崂山-A | 接入点名称。 |
| Status | String | recommended | 物理专线的接入点状态。 recommended ：表示接入点状态良好，推荐接入。 hot ：表示接入的物理专线较多，状态正常。 full ：表示接入物理专线已满，不允许新增接入。 disabled ：表示接入点不可用。 |
| Type | String | VPC | 物理专线接入的网络类型。 |
| TotalCount | Integer | 5 | 列表条条目数。 |
| PageNumber | Integer | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

高速通道

| RequestId | String | 3E85D803-C7CF-4BCD-9CFE- 6DBA1DFFA027 | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAccessPoints &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeAccessPointsResponse> <AccessPointSet> <Status>recommended</Status> <Type>VPC</Type> <Description>ap-cn-hangzhou-dq-A-EU95</Description> <AttachedRegionNo>cn-qingdao-env66-d01</AttachedRegionNo> <HostOperator>中国电信</HostOperator> <AccessPointId>ap-cn-hangzhou-xs-D</AccessPointId> <Name>青岛-崂山-A</Name> <Location>青岛</Location> </AccessPointSet> <TotalCount>5</TotalCount> <PageSize>10</PageSize> <RequestId>3E85D803-C7CF-4BCD-9CFE-6DBA1DFFA027</RequestId> <PageNumber>1</PageNumber> </DescribeAccessPointsResponse> |  |

| JSON | 格式 |
|---|---|
| { "DescribeAccessPointsResponse": { "AccessPointSet": { "Status": "recommended", "Type": "VPC", "Description": "ap-cn-hangzhou-dq-A-EU95", "AttachedRegionNo": "cn-qingdao-env66-d01", "HostOperator": "中国电信", "AccessPointId": "ap-cn-hangzhou-xs-D", "Name": "青岛-崂山-A", "Location": "青岛" }, "TotalCount": 5, "PageSize": 10, "RequestId": "3E85D803-C7CF-4BCD-9CFE-6DBA1DFFA027", "PageNumber": 1 } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotSupport | The RegionId provided does not support in our records. | 输入的地域ID不正确。 |

#### 6.5.3. CancelPhysicalConnection

在物理专线开通前，调用CancelPhysicalConnection接口取消物理专线接入，取消后物理专线进入**Canceled**状态。

**使用限制**

只能取消处于**Initial**、**Approved**、**Allocated**和**Confirmed**状态（未开通状态）的物理专线接入。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CancelPhysicalConnection | 要执行的操作。 取值：CancelPhysicalConnection。 |
| PhysicalConnectionId | String | 是 | pc-119mf**** | 物理专线实例ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |

高速通道

| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CancelPhysicalConnection &PhysicalConnectionId=pc-119mf**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CancelPhysicalConnectionResponse> <RequestId>BE36E95A-F83E-4127-A29E-F2F35D4C999A</RequestId> </CancelPhysicalConnectionResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidPhysicalConnectionId.NotF ound | The PhysicalConnectionId provided does not exist in our records. | 该物理专线不存在。 |
| 400 | Forbidden.NotAllowedInState | The request does not allow in this state. | 该状态无法执行请求。 |

#### 6.5.4. DescribePhysicalConnections

调用DescribePhysicalConnections接口查询指定地域内的物理专线。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePhysicalConnections | 要执行的操作。 取值：DescribePhysicalConnections。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| PageNumber | Integer | 否 | 10 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 1 | 分页查询时每页的行数，最大值为50，默认值为10。 |
| Filter.N.Key | String | 否 | 1 | 过滤条件。N的取值为1～5。支持的过滤条件如下： PhysicalConnectionId：物理专线ID。 AccessPointId：接入点ID。 Type：专线类型。 LineOperator：物理专线的运营商。 Spec：物理专线的规格。 Status：物理专线的状态。 Name：物理专线的名称。 一个过滤条件的多个值之间为或关系，只要与其中一个值吻合则视为符合该过滤条件。 各个过滤条件之间为与关系，符合所有的过滤条件，才会进入最终查询结果中。 |
| Filter.N.Value.N | RepeatList | 否 | 1 | 对应过滤条件的取值。N的取值范围为1～5。 |

高速通道

| IncludeReservationData | Boolean | 否 | false | 是否返回未生效订单。 true：返回。 false（默认值）：不返回。 |
|---|---|---|---|---|
| ClientToken | String | 否 | 23243242rggy**** | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PhysicalConnectionSet | Array of PhysicalConnectionType |  | 物理专线的详细信息。 |
| PhysicalConnectionType |  |  |  |
| AccessPointId | String | eip-2zeerraiwb7uj6i0******* | 物理专线接入点的ID。 |
| AdLocation | String | 广东省深圳市南山区滨海大道xxx基地 xx座 Ax-x Bxx | 专线接入设备所在的物理位置。 |
| Bandwidth | Long | 10 | 物理专线的带宽。单位：Mbps。 |
| BusinessStatus | String | Normal | 物理专线的付费状态。 Normal：正常。 FinancialLocked：欠费锁定。 SecurityLocked：因安全原因被锁定。 |
| ChargeType | String | Prepaid | 收费类型。 取值：Prepaid，预付费。 |
| CircuitCode | String | longtel001 | 运营商为物理专线提供的电路编码。 |
| CreationTime | String | 2017-06-08T12:20:55 | 物理专线的创建时间。 |
| Description | String | 物理专线 | 物理专线的描述。 |
| EnabledTime | String | 2017-06-08T12:20:55 | 物理专线的开通时间。 |
| EndTime | String | 2019-02-25T11:01:04Z | 到期时间。 |
| HasReservationData | String | true | 是否有订购消息。 true：有。 false：无。 |
| LineOperator | String | CT | 提供接入物理线路的运营商。 CT：中国电信。 CU：中国联通。 CM：中国移动。 CO：中国其他。 Equinix：Equinix。 Other：境外其他。 |
| LoaStatus | String | Available | LOA状态。 |
| Name | String | name | 物理专线的名称。 |
| PeerLocation | String | 浙江省杭州市XX区XX街道XX号 | 本地数据中心的地理位置。 |
| PhysicalConnectionId | String | pc-119mfjzm***** | 物理专线ID。 |
| PortNumber | String | 80 | 专线接入设备的端口号。 |

高速通道

| PortType | String | 1000Base-T | 物理专线接入端口类型。 100Base-T：百兆电口。 1000Base-T：千兆电口。 1000Base-LX：千兆单模光口（10千米）。 10GBase-T：万兆电口。 10GBase-LR：万兆单模光口（10千米）。 |
|---|---|---|---|
| RedundantPhysicalConnec tionId | String | pc-119mfjzm******* | 冗余物理专线ID。 |
| ReservationActiveTime | String | 2019-02-25T11:01:04Z | 续费生效时间。 |
| ReservationInternetCharg eType | String | PayByBandwidth | 续费类型。 |
| ReservationOrderType | String | RENEW | 续费订单类型。 |
| Spec | String | Large | 物理专线的规格。 |
| Status | String | Initial | 物理专线的状态。 Initial：申请中。 Approved：审批通过。 Allocating：正在分配资源。 Allocated：接入施工中。 Confirmed：等待用户确认。 Enabled：已开通。 Rejected：申请被拒绝。 Canceled：已取消。 Allocation Failed：资源分配失败。 Terminated：已终止。 |
| Type | String | VPC | 物理专线的类型。默认值为VPC。 |
| TotalCount | Integer | 10 | 列表条目数。 |
| PageNumber | Integer | 10 | 列表的页码，默认值为1。 |
| PageSize | Integer | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |
| RequestId | String | EEC8EAB1-F299-4F5C-8E54- 0A3129164C27 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePhysicalConnections &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式高速通道

```xml
      <PhysicalConnectionSet>
            <Status>Initial</Status>
            <Description>物理专线</Description>
            <EndTime>2019-02-25T11:01:04Z</EndTime>
            <LineOperator>CT</LineOperator>
            <CircuitCode>longtel001</CircuitCode>
            <PhysicalConnectionId>pc-119mfjzm*****</PhysicalConnectionId>
            <HasReservationData>true</HasReservationData>
            <RedundantPhysicalConnectionId>pc-119mfjzm*******</RedundantPhysicalConnectionId>
```

`<PeerLocation>`浙江省杭州市`XX`区`XX`街道`XX`号`</PeerLocation>`

```xml
            <BusinessStatus>Normal</BusinessStatus>
            <ReservationInternetChargeType>PayByBandwidth</ReservationInternetChargeType>
            <Name>name</Name>
            <ReservationOrderType>RENEW</ReservationOrderType>
            <LoaStatus>Available</LoaStatus>
            <Type>VPC</Type>
```

`<AdLocation>`广东省深圳市南山区滨海大道`xxx`基地`xx`座 `Ax-x Bxx</AdLocation>`

```xml
            <ChargeType>Prepaid</ChargeType>
            <Bandwidth>10</Bandwidth>
            <CreationTime>2017-06-08T12:20:55</CreationTime>
            <AccessPointId>eip-2zeerraiwb7uj6i0*******</AccessPointId>
            <EnabledTime>2017-06-08T12:20:55</EnabledTime>
            <ReservationActiveTime>2019-02-25T11:01:04Z</ReservationActiveTime>
            <PortNumber>80</PortNumber>
            <Spec>Large</Spec>
            <PortType>1000Base-T</PortType>
      </PhysicalConnectionSet>
      <TotalCount>10</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>EEC8EAB1-F299-4F5C-8E54-0A3129164C27</RequestId>
      <PageNumber>10</PageNumber>
```

| JSON | 格式 |
|---|---|
| { "PhysicalConnectionSet": { "Status": "Initial", "Description": "物理专线", "EndTime": "2019-02-25T11:01:04Z", "LineOperator": "CT", "CircuitCode": "longtel001", "PhysicalConnectionId": "pc-119mfjzm*****", "HasReservationData": true, "RedundantPhysicalConnectionId": "pc-119mfjzm*******", "PeerLocation": "浙江省杭州市XX区XX街道XX号", "BusinessStatus": "Normal", "ReservationInternetChargeType": "PayByBandwidth", "Name": "name", "ReservationOrderType": "RENEW", "LoaStatus": "Available", "Type": "VPC", "AdLocation": "广东省深圳市南山区滨海大道xxx基地xx座 Ax-x Bxx", "ChargeType": "Prepaid", "Bandwidth": 10, "CreationTime": "2017-06-08T12:20:55", "AccessPointId": "eip-2zeerraiwb7uj6i0*******", "EnabledTime": "2017-06-08T12:20:55", "ReservationActiveTime": "2019-02-25T11:01:04Z", "PortNumber": 80, "Spec": "Large", "PortType": "1000Base-T" }, "TotalCount": 10, "PageSize": 10, "RequestId": "EEC8EAB1-F299-4F5C-8E54-0A3129164C27", "PageNumber": 10 } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidFilterKey.ValueNotSupport ed | Specified filter key is not supported: Filter.X.key | 该过滤器的Key不支持：Filter.X.key。 |

#### 6.5.5. ModifyPhysicalConnectionAttribute

调用ModifyPhysicalConnectionAttribute接口修改物理专线的配置。

**使用说明**

调用该接口时，请注意以下事项： 只有处于**Initial**、**Enabled**和**Rejected**状态的物理专线可以修改规格和冗余专线ID。 高速通道无法修改处于**Canceled**、**Allocating**、**AllocationFailed**和**Terminated**状态的物理专线。 处于**Rejected**状态的物理专线被修改后会进入**Initial**状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyPhysicalConnectionAtt ribute | 要执行的操作。 取值： ModifyPhysicalConnectionAttribute。 |
| PhysicalConnectionId | String | 是 | pc-119mfjzm**** | 要修改的物理专线的ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要修改的物理专线所在地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| LineOperator | String | 否 | CT | 提供接入物理专线的运营商，取值： CT：中国电信。 CU：中国联通。 CM：中国移动。 CO：中国其他。 Equinix：Equinix。 Other：境外其他。 |
| bandwidth | Integer | 否 | 5 | 要修改的物理专线接入接口带宽。取值范围：2~10240。单位： Mbps。 |
| PeerLocation | String | 否 | 浙江省杭州市XX区XX街道XX号 | 本地数据中心的地理位置。 |
| PortType | String | 否 | 1000Base-LX | 物理专线接入端口类型，取值： 100Base-T：百兆电口。 1000Base-T（默认值）：千兆电口。 1000Base-LX：千兆单模光口（10千米）。 10GBase-T：万兆电口。 10GBase-LR：万兆单模光口（10千米）。 |
| RedundantPhysicalConnectio nId | String | 否 | pc-119mfjzm7**** | 冗余物理专线的ID，该专线的状态必须为Allocated、Confirmed或Enabled。 |
| Description | String | 否 | 物理专线的描述信息 | 物理专线的描述信息。 长度为 2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| Name | String | 否 | 物理专线的名称 | 物理专线的名称。 长度为 2~128个字符，必须以字母或中文开头，可包含数字，半角句号（.），下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
| CircuitCode | String | 否 | longtel001 | 运营商为物理专线提供的电路编码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 013EE132-A109-4247-91B0- 099A8FF49AD7 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyPhysicalConnectionAttribute &PhysicalConnectionId=pc-119mfjzm**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例高速通道 `XML` 格式

```xml
<ModifyPhysicalConnectionAttributeResponse>
  <RequestId>013EE132-A109-4247-91B0-099A8FF49AD7</RequestId>
</ModifyPhysicalConnectionAttributeResponse>
```

| JSON | 格式 |
|---|---|
| { "RequestId": "013EE132-A109-4247-91B0-099A8FF49AD7" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidPhysicalConnectionId.NotF ound | The PhysicalConnectionId provided does not exist in our records. | 该物理专线不存在。 |
| 400 | InvalidLineOperator.Malformd | The LineOperator provided was invalid. | 参数LineOperator的值不合法。 |
| 400 | InvalidPeerLocation.Malformd | The PeerLocation provided was invalid. | 参数PeerLocation的值不合法。 |
| 400 | InvalidPortType.Malformd | The PortType provided was invalid. | 该端口类型不合法。 |
| 400 | InvalidDescription.Malformed | The specifid ?Description? is not valid. | 指定的资源描述格式不合法。长度为2～256个字符，不能以http://和https://开头。 |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | 该名称格式不合法。 |
| 400 | InvalidStatus | invalid physical connection status. | 物理专线状态不合法。 |
| 400 | InvalidBandwidth | invalid physical connection banwidth. | 物理专线的带宽不合法。 |
| 400 | InvalidRedundantPhysicalConnect ion | redundant physical connection doesn't belong to current user. | 该冗余物理专线不属于您的账号。 |
| 400 | InvalidRedundantPhysicalConnect ionStatus | invalid redundant physical connection status. | 冗余物理专线状态不合法。 |
| 400 | InvalidCircuitCode.Malformed | circuitCode is illegal. | 该CircuitCode不合法。 |

#### 6.5.6. TerminatePhysicalConnection

在物理专线开通后，调用TerminatePhysicalConnection接口终止物理专线接入。

**使用说明**

调用TerminatePhysicalConnection接口后，物理专线进入**Terminating**状态，处理完成后进入**Terminated**状态。 调用本接口终止物理专线时，请注意： 只能终止处于**Enabled**状态的物理专线。 终止物理专线之前，必须删除与其关联的VBR。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TerminatePhysicalConnection | 要执行的操作。 取值：TerminatePhysicalConnection。 |
| PhysicalConnectionId | String | 是 | pc-119mfjzm**** | 物理专线实例ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 513E0A50-4F2D-4CBE-BF35- 40559DF65D79 | 请求ID。 |

**示例**

请求示例高速通道

```
http(s)://[Endpoint]/?Action=TerminatePhysicalConnection &PhysicalConnectionId=pc-119mfjzm**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <TerminatePhysicalConnectionResponse> <RequestId>513E0A50-4F2D-4CBE-BF35-40559DF65D79</RequestId> </TerminatePhysicalConnectionResponse> |  |

| JSON | 格式 |
|---|---|
| { "TerminatePhysicalConnectionResponse": { "RequestId": "513E0A50-4F2D-4CBE-BF35-40559DF65D79" } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidPhysicalConnectionId.NotF ound | The PhysicalConnectionId provided does not exist in our records. | 该物理专线不存在。 |
| 400 | Forbidden.NotAllowedInState | The request does not allow in this state. | 该状态无法执行请求。 |

#### 6.5.7. EnablePhysicalConnection

调用EnablePhysicalConnection接口开通处于**Confirmed**状态的物理专线，开通完成后物理专线进入**Enabled**状态。

**使用说明**

调用该接口时，请注意： 只允许开通处于**Confirmed**状态的物理专线。 开通完成后物理专线进入**Enabled**状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | EnablePhysicalConnection | 要执行的操作。 取值：EnablePhysicalConnection。 |
| PhysicalConnectionId | String | 是 | pc-119mfjz**** | 物理专线实例ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23-88ED- E11ED28DCAC0 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=EnablePhysicalConnection &PhysicalConnectionId=pc-119mfjz**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <EnablePhysicalConnectionResponse> <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId> </EnablePhysicalConnectionResponse> |  |

`JSON` 格式高速通道

```json
{
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidPhysicalConnectionId.NotF ound | The PhysicalConnectionId provided does not exist in our records. | 该物理专线不存在。 |
| 400 | Forbidden.NotAllowedInState | The request does not allow in this state. | 该状态无法执行请求。 |

#### 6.5.8. DeletePhysicalConnection

**使用限制**

只能删除**Rejected**、**Canceled**、**AllocationFailed**和**Terminated**状态的物理专线。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeletePhysicalConnection | 要执行的操作。 取值：DeletePhysicalConnection。 |
| PhysicalConnectionId | String | 是 | pc-119mfjzm7**** | 物理专线实例ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23-88ED- E11ED28DCAC0 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePhysicalConnection &PhysicalConnectionId=pc-119mfjzm7**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeletePhysicalConnectionResponse> <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId> </DeletePhysicalConnectionResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidPhysicalConnectionId.NotF ound | The PhysicalConnectionId provided does not exist in our records. | 该物理专线不存在。 |
| 400 | Forbidden.NotAllowedInState | The request does not allow in this state. | 该状态无法执行请求。 |
| 400 | InvalidPhysicalConnectionId.NotM atched | instance id not matched. | 实例ID不匹配。 |
| 400 | Forbidden.VBRExists | physical connection owner's vbr still exists. | 物理连接的VBR仍然存在。 |
| 400 | Forbidden.VBRExists | vbr owner's vbr still exists. | 边界路由器仍然存在。 |

高速通道

| 400 | Forbidden.AssociateToVBR | The physical connection still associate to VBR. | 该物理专线已经关联了边界路由器。 |
|---|---|---|---|

#### 6.5.9. CreatePhysicalConnectionOccupancyOrder

调用CreatePhysicalConnectionOccupancyOrder接口创建资源占用费订单。

**使用限制**

只有物理专线状态为**等待用户支付**的实例允许执行此操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreatePhysicalConnectionOc cupancyOrder | 要执行的操作。 取值：CreatePhysicalConnectionOccupancyOrder。 |
| PhysicalConnectionId | String | 是 | pc-bp1hp0wr072f6**** | 物理专线的ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| Period | Integer | 否 | 1 | 购买时长。 当PricingCycle取值Month时，Period取值范围为1～9。 当PricingCycle取值Year时，Period取值范围为1～5。 说明如果InstanceChargeType取值为PrePaid， 该参数必选；如果InstanceChargeType取值为PostPaid时，该参数不填。 |
| InstanceChargeType | String | 否 | PostPaid | 实例的付费方式。取值： PrePaid：包年包月。选择该类付费方式时，您必须确认自己的账号支持余额支付或信用支付。 PostPaid（默认值）：按量付费。 |
| AutoPay | Boolean | 否 | false | 是否自动支付。取值： true：自动支付。您需要确保账户余额充足，如果账户余额不足会生成异常订单，只能作废订单。 false（默认值）：只生成订单不扣费。 |
| PricingCycle | String | 否 | Month | 订购的周期单位。取值： Year：年。 Month：月。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 9B9300FE-11E2-4E3B-949C- BED3B44DD26D | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreatePhysicalConnectionOccupancyOrder &PhysicalConnectionId=pc-bp1hp0wr072f6**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreatePhysicalConnectionOccupancyOrder> <RequestId>9B9300FE-11E2-4E3B-949C-BED3B44DD26D</RequestId> </CreatePhysicalConnectionOccupancyOrder> |  |

`JSON` 格式高速通道

```json
{
    "RequestId": "9B9300FE-11E2-4E3B-949C-BED3B44DD26D"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidPhysicalConnectionId.NotF ound | The PhysicalConnectionId provided does not exist in our records. | 该物理专线不存在。 |
| 400 | Forbidden.NotAllowedInState | The request does not allow in this state. | 该状态无法执行请求。 |

#### 6.5.10. ApplyPhysicalConnectionLOA

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ApplyPhysicalConnectionLOA | 要执行的操作。 取值：ApplyPhysicalConnectionLOA。 |
| CompanyName | String | 是 | company | 物理专线接入的客户公司名称。 |
| ConstructionTime | String | 是 | 2021-02-28T16:00:00.000Z | 施工单位入场时间。 |
| InstanceId | String | 是 | pc-bp1qrb3044eqi**** | 物理专线ID。 |
| LineType | String | 是 | FIBRE | 物理专线类型。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 专线实例所属的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| Si | String | 是 | 阿里云 | 物理专线施工单位。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
| Bandwidth | Integer | 否 | 3 | 物理专线带宽值。 |
| PeerLocation | String | 否 | 杭州 | 物理专线部署地理位置。 |
| PMInfo.N.PMName | String | 否 | 张三 | 施工工程师姓名。 N是自然数，调用接口时需要替换。 |
| PMInfo.N.PMContactInfo | String | 否 | 1320000**** | 施工工程师联系方式。 N是自然数，调用接口时需要替换。 |
| PMInfo.N.PMCertificateType | String | 否 | IDCard | 施工工程师证件类型。 N是自然数，调用接口时需要替换。 |
| PMInfo.N.PMCertificateNo | String | 否 | 3210xxxxxxxxxxxxxx | 施工工程师证件号码。 N是自然数，调用接口时需要替换。 |
| PMInfo.N.PMGender | String | 否 | Male | 施工工程师性别。 N是自然数，调用接口时需要替换。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A47BD386-7FDE-42C4-8D22- C6223D18AA1C | 请求ID。 |

高速通道

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ApplyPhysicalConnectionLOA &CompanyName=company &ConstructionTime=2021-02-28T16:00:00.000Z &InstanceId=pc-bp1qrb3044eqi**** &LineType=FIBRE &RegionId=cn-qingdao-env66-d01
```

`&Si=`阿里云 `&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ApplyPhysicalConnectionLOAResponse> <RequestId>A47BD386-7FDE-42C4-8D22-C6223D18AA1C</RequestId> </ApplyPhysicalConnectionLOAResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"A47BD386-7FDE-42C4-8D22-C6223D18AA1C" } |  |

#### 6.5.11. CreatePhysicalConnectionSetupOrder

调用CreatePhysicalConnectionSetupOrder创建端口初装费订单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreatePhysicalConnectionSet upOrder | 要执行的操作。 取值：CreatePhysicalConnectionSetupOrder。 |
| AccessPointId | String | 是 | ap-cn-qingdao-ft-A | 接入点ID。 |
| LineOperator | String | 是 | CT | 提供接入物理线路的运营商。取值： CT：中国电信。 CU：中国联通。 CM：中国移动。 CO：中国其他。 Equinix：Equinix。 Other：境外其他。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| PortType | String | 否 | 100Base-T | 物理专线接入端口类型。取值： 100Base-T：百兆电口。 1000Base-T（默认值）：千兆电口。 1000Base-LX：千兆单模光口（10千米）。 10GBase-T：万兆电口。 10GBase-LR：万兆单模光口（10千米）。 |
| RedundantPhysicalConnectio nId | String | 否 | pc-bp10zsv5ntp**** | 冗余物理专线的ID，该专线的状态必须为Allocated、Confirmed或Enabled。 |
| AutoPay | Boolean | 否 | true | 是否开启自动支付。取值： true：自动支付。 false（默认值）：不开启自动支付。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

高速通道

| OrderId | String | 202844382740728 | 订单ID。 |
|---|---|---|---|
| PhysicalConnectionId | String | pc-2zegmc02v7ss4****** | 物理专线ID。 |
| RequestId | String | F7A6301A-64BA-41EC-8284- 8F4838C15D1F | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreatePhysicalConnectionSetupOrder &AccessPointId=ap-cn-beijing-ft-A &LineOperator=CT &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreatePhysicalConnectionSetupOrderResponse> <RequestId>F7A6301A-64BA-41EC-8284-8F4838C15D1F</RequestId> <PhysicalConnectionId>pc-2zegmc02v7ss4******</PhysicalConnectionId> <OrderId>202844382740728</OrderId> </CreatePhysicalConnectionSetupOrderResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "F7A6301A-64BA-41EC-8284-8F4838C15D1F", "PhysicalConnectionId": "pc-2zegmc02v7ss4******", "OrderId": 202844382740728 } |  |

#### 6.5.12. CompletePhysicalConnectionLOA

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CompletePhysicalConnection LOA | 要执行的操作。 取值：CompletePhysicalConnectionLOA。 |
| InstanceId | String | 是 | pc-bp10tvlhnwkw**** | 物理专线实例ID。 |
| LineCode | String | 是 | aaa111 | 运营商线路编码。 |
| LineLabel | String | 是 | bbb222 | 机房楼内线缆标签。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | F8983C74-E068-4509-B442- 89BD82C8F43B | 请求ID。 |

**示例**

请求示例高速通道

```
http(s)://[Endpoint]/?Action=CompletePhysicalConnectionLOA &InstanceId=pc-bp10tvlhnwkw**** &LineCode=aaa111 &LineLabel=bbb222 &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CompletePhysicalConnectionLOAResponse> <RequestId>F8983C74-E068-4509-B442-89BD82C8F43B</RequestId> </CompletePhysicalConnectionLOAResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "F8983C74-E068-4509-B442-89BD82C8F43B" } |  |

#### 6.5.13. DescribePhysicalConnectionLOA

调用DescribePhysicalConnectionLOA查询物理专线LOA信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePhysicalConnectionL OA | 要执行的操作。 取值：DescribePhysicalConnectionLOA。 |
| InstanceId | String | 是 | pc-bp1ca4wca27ex****** | 物理专线实例ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线部署的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| ClientToken | String | 否 | 318BB676-0A2B-43A0-9AD8- F1D34E93750F | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PhysicalConnectionLOATy pe | Struct |  | 物理专线LOA信息。 |
| CompanyLocalizedName | String | company | 施工单位名称。 |
| CompanyName | String | AppCompany**** | 需要部署物理专线的单位名称。 |
| ConstructionTime | String | 2019-02-26T08:00:00Z | 施工进场时间。 |
| InstanceId | String | pc-bp1ca4wca27****** | 物理专线实例ID。 |
| LineCode | String | lincode**** | 运营商线路编码。 |
| LineLabel | String | linetest**** | 机房楼内线缆标签。 |
| LineType | String | MSTP | 物理专线类型。取值： MSTP。 Other。 SDH。 MPLSVPN。 FIBRE。 |
| LoaUrl | String | http://****** | LOA文件下载地址。 |
| PMInfo | Array of PMInfo |  | 施工人员信息。 |
| PMInfo |  |  |  |

高速通道

| PMCertificateNo | String | engineer**** | 施工人员证件号码。 |
|---|---|---|---|
| PMCertificateType | String | Other | 施工人员证件类型，包含以下类型： IDCard：身份证。 Other：其他。 Passport：护照。 |
| PMContactInfo | String | 18910010****** | 施工人员联系电话。 |
| PMGender | String | Male | 施工人员性别。 |
| PMName | String | name | 施工人员姓名。 |
| SI | String | ctcu | 入场施工单位。 |
| Status | String | Enabled | 物理专线的状态。取值： Initial：申请中。 Approved：审批通过 。 Allocating：正在分配资源。 Allocated：接入施工中。 Confirmed：等待用户确认。 Enabled：已开通。 Rejected：申请被拒绝。 Canceled：已取消 。 Allocation Failed：资源分配失败。 Terminated：已终止。 |
| RequestId | String | 318BB676-0A2B-43A0-9AD8- F1D34E93750F | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePhysicalConnectionLOA &InstanceId=pc-bp1ca4wca27ex****** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribePhysicalConnectionLOAResponse> <code>200</code> <data> <companyName>test1234</companyName> <constructionTime>2019-02-26T08:00:00Z</constructionTime> <instanceId>pc-bp1ca4wca27ert****</instanceId> <lineType>MSTP</lineType> <loaUrl>http://********</loaUrl> <pmInfo> <nextPMIndex>1</nextPMIndex> <pmCertificateNo>12345**</pmCertificateNo> <pmCertificateType>Other</pmCertificateType> <pmContactInfo>189100100**0</pmContactInfo> <pmGender>Male</pmGender> <pmName>test</pmName> </pmInfo> <si>ctcu</si> <status>Available</status> </data> <message>successful</message> <requestId>318BB676-0A2B-43A0-9AD8-F1D34E93750F</requestId> <success>true</success> </DescribePhysicalConnectionLOAResponse> |  |

`JSON` 格式高速通道

```json
{
    "code": "200",
    "data": {
        "companyName": "test1234",
        "constructionTime": "2019-02-26T08:00:00Z",
        "instanceId": "pc-bp1ca4wca27erts****",
        "lineType": "MSTP",
        "loaUrl":"http://*******",
        "pmInfo": [
            {
                "nextPMIndex": 1,
                "pmCertificateNo": "1234567",
                "pmCertificateType": "Other",
                "pmContactInfo": "18910010***",
                "pmGender": "Male",
                "pmName": "test"
            }
```

`],`

```json
        "si": "ctcu",
        "status": "Available"
    },
    "message": "successful",
    "requestId": "318BB676-0A2B-43A0-9AD8-F1D34E93750F",
    "success": true
}
```

### 边界路由器

#### 6.6.1. CreateVbrHa

创建VBR倒换组

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Description | String | Query | 否 | This is my vswitch. | 交换机的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| Name | String | Query | 否 | test123 | 交换机的名称。 名称长度为2~128个字符，必须以字母或中文开头，可包含数字、下划线（_）和短划线（-）， 但不能以 http:// 或 https:// 开头。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-0016e04115b | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId可能不一样。 |
| DryRun | Boolean | Query | 否 | true | 是否检测此次请求。取值： true ：发送检查请求。 false （默认值）：发送正常请求。 |
| VbrId | String | Query | 是 | vbr-bp1lhl0taikrte**** | VBR实例ID。 |
| PeerVbrId | String | Query | 是 | vbr-bp12mw1f8k3jgygk9**** | VBR倒换组中另一个VBR的实例ID。 |
| RegionId | String | Query | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。 您可以通过调用DescribeRegions接口获取地域 ID。 |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |

| 高速通道 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| VbrHaId | String | vbrha-sa1sxheuxtd98**** | VBR倒换组实例ID。 |
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求 ID。 |

**示例**

请求示例

```
&VbrId=vbr-bp1lhl0taikrte**** &PeerVbrId=vbr-bp12mw1f8k3jgygk9**** &RegionId=cn-qingdao-env66-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "VbrHaId":"vbrha-sa1sxheuxtd98****", "RequestId":"5BE01CD7-5A50-472D-AC14-CA181C5C03BE" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationFailed.VbrCenNotConsis tent | OperationFailed.VbrCenNotConsistent | The VBR and the peer VBR are attached to different CENs. |
| 400 | OperationFailed.VbrAliUidNotCon sistent | OperationFailed.VbrAliUidNotConsistent | The VBR and the peer VBR belong to different AliUids. |
| 400 | OperationFailed.VbrAccessDevice Same | OperationFailed.VbrAccessDeviceSame | The VBR and the peer VBR are in the same device. |
| 400 | OperationFailed.VbrBandWidthEx ceed | OperationFailed.VbrBandWidthExceed | The VBR bandwidth exceeds the limit. |
| 400 | OperationFailed.VbrInUsedByOth erHa | OperationFailed.VbrInUsedByOtherHa | The VBR is used by another VBR HA. |
| 400 | OperationFailed.VbrBgpPeerNotE nableBfd | OperationFailed.VbrBgpPeerNotEnableBfd | The VBR BGP has not enabled BFD. |
| 400 | OperationFailed.VbrCenNotRelati on | OperationFailed.VbrCenNotRelation | The VBR is not attached to any CEN. |
| 404 | ResourceNotFound.Vbr | ResourceNotFound.Vbr | The VBR resource is not found. |

#### 6.6.2. DeleteVbrHa

删除VBR倒换组

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-0016e04115b | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId可能不一样。 |
| InstanceId | String | Query | 是 | pc-bp1qrb3044eqi**** | 资源实例id。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。 您可以通过调用DescribeRegions接口获取地域 ID。 |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求 ID。 |

**示例**

请求示例

```
&InstanceId=pc-bp1qrb3044eqi**** &RegionId=cn-qingdao-env66-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"5BE01CD7-5A50-472D-AC14-CA181C5C03BE" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | ResourceNotFound.VbrHa | ResourceNotFound.VbrHa | The VBR HA resource is not found. |

#### 6.6.3. DeleteNqa

删除指定的NQA实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteNqa | 系统规定参数。取值：DeleteNqa |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。 您可以通过调用DescribeRegions接口获取地域 ID。 |
| NqaId | String | Query | 是 | nqa-xxxxxxxxxxx | nqa资源实例id。 |

高速通道

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-0016e04115b | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId可能不一样。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求 ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env66-d01 &NqaId=nqa-xxxxxxxxxxx
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"5BE01CD7-5A50-472D-AC14-CA181C5C03BE" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | REGIONNOTFOUND _ _ | InvalidRegionId.NotFound | Specified value of "regionId" is not supported. |
| 400 | BGPPEERCOUNTPERVBRQUO _ _ _ _ _ TAEXCEED _ | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. |
| 400 | NQACOUNTPERVBRQUOTAE _ _ _ _ _ XCEED | QuotaExceeded.Nqa | nqa count per vbr quota exceed. |
| 400 | BGPNETWORKCOUNTPERVBR _ _ _ _ QUOTAEXCEED _ _ | QuotaExceeded.BgpNetwork | bgp network count per vbr quota exceed. |
| 400 | MULTIPCONNPEERIPADDRESS _ _ _ _ CANNOTBENULL _ _ _ | InvalidPeerIpAddress | multi pconn peer ip can not be null. |
| 400 | VBRNETWORKNOTEXISTS _ _ _ | InvalidVbrNetwork | vbr netowrk not exists |
| 400 | BGPGROUPNOTEXISTS _ _ _ | InvalidBgpGroup | bgp group not exists |
| 400 | NAMEILLEGAL _ | InvalidBgpName.Malformed | Specified Bgp Group name is not valid. |
| 400 | DESCRIPTIONILLEGAL _ | InvalidBgpDiscription.Malformed | Specified Bgp Group description is not valid. |
| 400 | AUTHKEYILLEGAL _ _ | InvalidBgpAuthkey.Malformed | Specified Bgp Group authkey is not valid. |
| 404 | REGIONNOTFOUND _ _ | InvalidRegionId.NotFound | The specified RegionId is not found. |
| 400 | IPMALFORMED _ | InvalidIP.Malformed | Ip malformed. |
| 400 | PEERASNCANNOTEQUALSALI _ _ _ _ YUNPUBLICASN _ _ | InvalidPeerAsn.Malformed | invalid peer asn cannot equals aliyun asn:45104 |
| 400 | PARAMETERMUSTNOTNULL _ _ _ | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 |
| 400 | INSTANCENOTEXISTS _ _ | InvalidParams.NotFound | instance not found |
| 400 | VPCNOTEXIST _ _ | InvalidParams.NotFound | vpc instance not found |
| 400 | BGPNETWORKCIDREXISTS _ _ _ | InvalidParams.AlreadyExists | bgp network already exists |
| 400 | NOTSTABLESTATUSCANNOT _ _ _ _ _ OPERATION | InvalidStatus.CannotOperate | invalid status cannot operate |
| 400 | ERRORVBRHAS0ORMORET _ _ _ _ _ _ HAN1SUBIF _ _ | InvalidParams.PeerIpAddressMustPointOut | vbr has 0 or more than 1 subif ,point out peerIpAddress. |

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | BGPPEERIPADDRESSALREADY _ _ _ _ USEDCANNOTCREATEBGPPE _ _ _ _ _ ER | InvalidParams.PeerIpAddressInUse | peer ip address in use ,cannot create bgp peer. |
| 404 | REGIONNOTFOUND _ _ | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. |

#### 6.6.4. CreateVirtualBorderRouter

调用CreateVirtualBorderRouter接口创建边界路由器VBR（Virtual Border Router）实例。

**使用说明**

为本组织创建VBR实例后，VBR实例状态为**Active**。 为其他组织创建VBR实例后，VBR实例状态为**Unconfirmed**，需要对方账号确认。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateVirtualBorderRouter | 要执行的操作。 取值：CreateVirtualBorderRouter。 |
| PhysicalConnectionId | String | 是 | pc-2zextbehcx**** | 物理专线实例ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VlanId | Integer | 是 | 0 | VBR的VLAN ID，取值范围：0～2999。 说明只有物理专线的所有者可以指定该参数，同一条物理专线下的两个VBR的VLAN ID不能相同。 |
| VbrOwnerId | Long | 否 | 253460731706911258 | VBR所有者的阿里云账号ID。 默认为当前用户的账号ID或物理专线所有者的账号ID。 |
| CircuitCode | String | 否 | longtel001 | 运营商为物理专线提供的电路编码。 说明只有物理专线的所有者可以指定该参数。 |
| LocalGatewayIp | String | 否 | 192.168.XX.XX | VBR实例的阿里云侧互联IP。 |
| PeerGatewayIp | String | 否 | 192.168.XX.XX | VBR实例的客户侧互联IP。 该属性只允许VBR所有者指定或修改。 为物理专线所有者创建VBR实例时必填，为其他组织创建VBR实例时无需填写。 |
| PeeringSubnetMask | String | 否 | 255.255.255.252 | VBR实例的阿里云侧和客户侧互联IP的子网掩码。 两个IP地址必须位于同一个子网中。 |
| Description | String | 否 | VBR描述信息 | VBR的描述信息。 长度为2～256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| Name | String | 否 | test | VBR的名称。 长度为2～128个字符，必须以字母或中文开头，可包含数字、下划线 （_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
| LocalIpv6GatewayIp | String | 否 | 2001:XXXX:3c4d:0015:0000: 0000:0000:1a2b | VBR实例的阿里云侧互联IPv6地址。 |
| PeerIpv6GatewayIp | String | 否 | 2001:XXXX:3c4d:0015:0000: 0000:0000:2a2b | VBR实例的客户侧互联IPv6地址。 该属性只允许VBR所有者指定或者修改。 为物理专线所有者创建VBR实例时必填，为其他组织创建VBR实例时无需填写。 |

高速通道

| PeeringIpv6SubnetMask | String | 否 | 2408:4004:cc:400::/56 | VBR实例的阿里云侧和客户侧互联IPv6的子网掩码。 两个IPv6地址必须位于同一个子网中。 |
|---|---|---|---|---|
| EnableIpv6 | Boolean | 否 | false | 是否启用IPv6。 true：开启。 false（默认值）：关闭。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VbrId | String | vbr-bp1jcg5cmxjbl9xgc**** | VBR实例ID。 |
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateVirtualBorderRouter &PhysicalConnectionId=pc-2zextbehcx**** &RegionId=cn-qingdao-env66-d01 &VlanId=0
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateRouterInterfaceResponse> <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId> <VbrId>vbr-bp1jcg5cmxjbl9xgc****</VbrId> </CreateRouterInterfaceResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF", "VbrId": "vbr-bp1jcg5cmxjbl9xgc****" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | The specified RegionId is not found. | 指定的RegionId不存在，请您检查此产品在该地域是否可用。 |
| 400 | InvalidPhysicalConnectionId.NotF ound | The specified PhysicalConnectionId is not found. | 该物理专线ID不存在。 |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | 该VLAN已经被占用。 |
| 400 | MissingParameter | The input parameter 'PhysicalConnectionId' that is mandatory for processing this request is not supplied. | 必须指定参数PhysicalConnectionId。 |
| 400 | InvalidPhysicalConnectionId.NotE nabled | The specified PhysicalConnectionId is not in Enabled state. | 该物理专线当前未处于正常状态，请检查物理专线后再创建。 |
| 404 | InvalidVbrOwnerId.NotFound | The specified VbrOwnerId is not valid. | 参数VbrOwnerId的值不合法。 |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | 参数VlanId的值不合法。 |
| 400 | InvalidCircuitCode.Malformed | The specified CircuitCode is not valid. | 该CircuitCode不合法。 |
| 400 | MissingParameter | The input parameter 'LocalGatewayIp' that is mandatory for processing this request is not supplied. | 必须指定参数LocalGatewayIp。 |
| 400 | InvalidLocalGatewayIp.Malformed | The specified LocalGatewayIp is not valid. | 该本端网关的IP不合法。 |
| 400 | MissingParameter | The input parameter 'PeerGatewayIp' that is mandatory for processing this request is not supplied. | 必须指定参数PeerGatewayIp。 |
| 400 | MissingParameter | The input parameter 'PeeringSubnetMask' that is mandatory for processing this request is not supplied. | 必须指定参数PeeringSubnetMask。 |
| 400 | InvalidPeeringSubnetMask.Malfor med | The specified PeeringSubnetMask is not valid. | 指定的PeeringSubnetMask不合法，请您检查该参数是否正确。 |
| 403 | Forbidden.LocalGatewayIpNotAllo wedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | 不允许指定LocalGatewayIp参数。 |

高速通道

| 403 | Forbidden.PeerGatewayIpNotAllo wedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | 不允许指定PeerGatewayIp参数。 |
|---|---|---|---|
| 403 | Forbidden.PeeringSubnetMaskNot AllowedByCaller | The caller is not allowed to specify the PeeringSubnetMask parameter. | 不允许指定PeeringSubnetMask参数。 |
| 403 | Forbidden.NameNotAllowedByCal ler | The caller is not allowed to specify the Name parameter. | 不允许指定Name参数。 |
| 403 | Forbidden.DescriptionNotAllowed ByCaller | The caller is not allowed to specify the Description parameter. | 不允许指定Description参数。 |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | 该名称格式不合法。 |
| 400 | InvalidDescription.Malformed | The specifid ?Description? is not valid. | 指定的资源描述格式不合法。长度为2～256个字符，不能以http://和https://开头。 |
| 400 | QuotaExceeded.vbrPerpConn | Virtual boarder router per PhysicalConnection quota exceed. | 超过了每个物理专线上的边界路由器配额上限，请您减少该物理专线上的边界路由器数量后再试。 |
| 400 | QuotaExceeded.freevbr | Free virtual boarder router quota exceed. | 超过边界路由器配额。 |
| 400 | InvalidIp.NotSameSubnet | Local gateway ip and peer gateway ip are not in the same subnet. | 本地网关IP地址与对端网关IP地址不在同一个子网内。 |
| 404 | CROSSBID.FORBIDDEN _ | Create VBR across bid is illegal | 禁止为其他站点的用户创建VBR。 |

#### 6.6.5. DeleteVirtualBorderRouter

调用DeleteVirtualBorderRouter接口删除边界路由器VBR（Virtual Border Router）。

**使用说明**

在调用本接口删除VBR之前，请注意以下事项： 只能删除**Unconfirmed**，**Enabled**或**Terminated**状态的VBR。 其他用户的VBR只有处于**Unconfirmed**状态时，才可以被物理专线的所有者删除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteVirtualBorderRouter | 要执行的操作。 取值： DeleteVirtualBorderRouter。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要删除的VBR所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VbrId | String | 是 | vbr-bp12mw1f8k3jgygk9**** | 要删除的VBR的ID。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | F8BF7D24-F3EB-4E23-9208- B77C6EB78E75 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteVirtualBorderRouter &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp12mw1f8k3jgygk9****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteVirtualBorderRouterResponse> <RequestId>F8BF7D24-F3EB-4E23-9208-B77C6EB78E75</RequestId> </DeleteVirtualBorderRouterResponse> |  |

`JSON` 格式高速通道

```json
{
    "RequestId": "F8BF7D24-F3EB-4E23-9208-B77C6EB78E75"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidOperation.RouterInterface NotDeleted | The specified VirutalBorderRouter still has routerInterface. | 该边界路由器还有关联的路由器接口。 |
| 400 | InvalidOperation.OperationNotAll owedInState | The specified VirutalBorderRouter is in invalid state. | 该VirutalBorderRouter状态不合法，请检查 VirutalBorderRouter状态。 |
| 403 | Forbidden.OperationNotAllowedB yUser | The caller is not allowed to delete the specified VirtualBorderRouter. | 不允许删除边界路由器。 |
| 403 | Forbidden.MultiVlanRi | Multiple vlan router interfaces are found. | 存在多个VLAN路由器接口。 |
| 403 | Forbidden.NoRiFound | No vlan router interfaces are found. | 没有可用的VLAN路由器接口。 |
| 400 | InvalidStatus.NotAllowed | The virtual border has been associated by physicalConnection. | 边界路由器已经关联了物理专线。 |

#### 6.6.6. DescribeVirtualBorderRouters

调用DescribeVirtualBorderRouters接口查询已创建的边界路由器VBR（Virtual Border Router）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVirtualBorderRouter s | 要执行的操作。 取值：DescribeVirtualBorderRouters。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要查询的VBR所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| PageNumber | Integer | 否 | 1 | 列表的页码。默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数。最大值：50。默认值：10。 |
| Filter.N.Key | String | 否 | Status | 第N个过滤条件的key，N的取值范围：1~5。 支持过滤参数为： PhysicalConnectionId：物理专线实例ID。 VbrId：边界路由器实例ID。 Status：边界路由器状态。 Name：边界路由器名称。 AccessPointId：接入点ID。 eccId：高速上云服务实例ID。 type：物理专线类型。 |
| Filter.N.Value.N | RepeatList | 否 | Active | 根据Key指定过滤值。一个Key支持指定多个过滤值，每个过滤值之间是或的关系，即只要符合其中一个过滤值，则视为匹配该过滤条件。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VirtualBorderRouterSet | Array of VirtualBorderRouterType |  | 查询到的VBR信息。 |
| VirtualBorderRouterType |  |  |  |
| AccessPointId | String | ap-cn-kojok1**** | 物理专线接入点ID。 |
| ActivationTime | String | 2020-06-08T12:20:55 | VBR第一次激活的时间。 |
| AssociatedCens | Array of AssociatedCen |  | 云企业网。 |
| AssociatedCen |  |  |  |
| CenId | String | cen-kojok19**** | 云企业网实例ID。 |

高速通道

| CenOwnerId | Long | 253460731706911258 | 云企业网实例所属阿里云账号。 |
|---|---|---|---|
| CenStatus | String | Attached | 云企业网状态。 |
| AssociatedPhysicalConnec tions | Array of AssociatedPhysicalConnec tion |  | 绑定的物理专线。 |
| AssociatedPhysicalConnec tion |  |  |  |
| CircuitCode | String | 12 | VBR专线侧接口对应运营商的电路编码。 |
| EnableIpv6 | Boolean | false | 是否开通IPv6。 |
| LocalGatewayIp | String | 116.62.XX.XX | VBR实例的阿里云侧互联IPv4地址。 |
| LocalIpv6GatewayIp | String | 2001:XXXX:4:4:4:4:4:4 | VBR实例的阿里云侧互联IPv6地址。 |
| PeerGatewayIp | String | 116.12.XX.XX | VBR实例的客户侧互联IPv4地址。 |
| PeerIpv6GatewayIp | String | 2001:XXXX:3:3:4:4:4:4 | VBR实例的客户侧互联IPv6地址。 |
| PeeringIpv6SubnetMask | String | 2408:4004:cc:400::/56 | VBR实例的阿里云侧互联IPv6与客户侧互联IPv6的子网掩码。 |
| PeeringSubnetMask | String | 255.255.255.252 | VBR实例的阿里云侧互联IPv6与客户侧互联IPv4的子网掩码。 |
| PhysicalConnectionBusine ssStatus | String | Normal | 物理专线业务状态。 |
| PhysicalConnectionId | String | pc-119mfjzm7**** | 物理专线ID。 |
| PhysicalConnectionOwner Uid | String | 283117732402483989 | 物理专线所有者的阿里云账号。 |
| PhysicalConnectionStatus | String | Normal | 物理专线连接状态。 |
| Status | String | Enabled | 物理专线状态。 |
| VlanId | String | 0 | VBR的VLAN ID。 |
| VlanInterfaceId | String | ri-kojok19x3j0q6k**** | VBR的路由器接口ID。 |
| CircuitCode | String | longtel001 | 运营商为物理专线提供的电路编码。 |
| CreationTime | String | 2020-06-08T20:20:55 | VBR的创建时间。 |
| Description | String | VBR | VBR的描述信息。 |
| DetectMultiplier | Long | 3 | 检测时间倍数，即接收方允许发送方发送报文的最大连接丢包数，用来检测链路是否正常。 取值：3~10。 |
| EccId | String | ecc-h**** | 高速上云服务实例ID。 |
| EnableIpv6 | Boolean | false | 是否开通IPv6。 |
| LocalGatewayIp | String | 116.62.XX.XX | 阿里云侧互联IPv4地址。 |
| LocalIpv6GatewayIp | String | 2001:XXXX:4:4:4:4:4:4 | 阿里云侧互联IPv6地址。 |
| MinRxInterval | Long | 200 | 配置BFD报文的接收间隔。取值范围：200~1000。单位：ms。 |
| MinTxInterval | Long | 200 | 配置BFD报文的发送间隔。取值范围：200~1000。单位：ms。 |
| Name | String | test | VBR的名称。 |

高速通道

| PConnVbrExpireTime | String | 2020-06-08T20:20:55 | 计费VBR的超期时间。 |
|---|---|---|---|
| PeerGatewayIp | String | 116.12.XX.XX | 客户侧互联IPv4地址。 |
| PeerIpv6GatewayIp | String | 2001:XXXX:3:3:4:4:4:4 | 客户侧互联IPv6地址。 |
| PeeringIpv6SubnetMask | String | 2000:1234:0:a000::/55 | VBR实例的阿里云侧互联IPv6与客户侧互联IPv6的子网掩码。 |
| PeeringSubnetMask | String | 255.255.255.252 | VBR实例的阿里云侧互联IPv6与客户侧互联IPv4的子网掩码。 |
| PhysicalConnectionBusine ssStatus | String | Normal | 物理专线业务状态。 |
| PhysicalConnectionId | String | pc-119mfjzm7x**** | VBR所属的物理专线的ID。 |
| PhysicalConnectionOwner Uid | String | 283117732402483989 | 物理专线所有者的阿里云账号。 |
| PhysicalConnectionStatus | String | Normal | 物理专线连接状态。 |
| RecoveryTime | String | 2020-06-09T12:20:55 | VBR最近一次从Terminated状态恢复到Active状态的时间。 |
| RouteTableId | String | rtb-bp1n**** | VBR的路由表的ID。 |
| Status | String | Enabled | 物理专线状态。取值： Initial：申请中。 Approved：审批通过。 Allocating：正在分配资源。 Allocated：接入施工中。 Confirmed：等待用户确认。 Enabled：已开通。 Rejected：申请被拒绝。 Canceled：已取消。 Allocation Failed：资源分配失败。 Terminated：已终止。 |
| TerminationTime | String | 2020-06-08T20:20:55 | VBR最近一次被终止的时间。 |
| Type | String | pconnVBR | VBR的类型。 |
| VbrId | String | vbr-kojok19xx**** | VBR的ID。 |
| VlanId | Integer | 10 | VBR的VLAN ID。 |
| VlanInterfaceId | String | ri-2zeo3xzyf38r4xx**** | VBR的路由器接口ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| PageNumber | Integer | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |
| RequestId | String | DE77A7F3-3B74-41C0-A5BC- CAFD188C28B6 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVirtualBorderRouters &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式高速通道

```xml
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6</RequestId>
  <PageNumber>1</PageNumber>
  <VirtualBorderRouterSet>
        <MinRxInterval>200</MinRxInterval>
        <PeerGatewayIp>116.12.XX.XX</PeerGatewayIp>
        <Description>VBR</Description>
        <RouteTableId>rtb-bp1n****</RouteTableId>
        <ActivationTime>2020-06-08T12:20:55</ActivationTime>
        <PhysicalConnectionId>pc-119mfjzm7x****</PhysicalConnectionId>
        <PhysicalConnectionStatus>Normal</PhysicalConnectionStatus>
        <VlanInterfaceId>ri-2zeo3xzyf38r4xx****</VlanInterfaceId>
        <VbrId>vbr-kojok19xx****</VbrId>
        <PhysicalConnectionOwnerUid>283117732402483989</PhysicalConnectionOwnerUid>
        <PeeringSubnetMask>255.255.255.252</PeeringSubnetMask>
        <TerminationTime>2020-06-08T20:20:55</TerminationTime>
        <EnableIpv6>false</EnableIpv6>
        <PeeringIpv6SubnetMask>2000:1234:0:a000::/55</PeeringIpv6SubnetMask>
        <Name>test</Name>
        <RecoveryTime>2020-06-09T12:20:55</RecoveryTime>
        <EccId>ecc-h****</EccId>
        <LocalIpv6GatewayIp>2001:XXXX:4:4:4:4:4:4</LocalIpv6GatewayIp>
        <VlanId>10</VlanId>
        <Status>Enabled</Status>
        <CircuitCode>longtel001</CircuitCode>
        <MinTxInterval>200</MinTxInterval>
        <PeerIpv6GatewayIp>2001:XXXX:3:3:4:4:4:4</PeerIpv6GatewayIp>
        <DetectMultiplier>3</DetectMultiplier>
        <Type>pconnVBR</Type>
        <LocalGatewayIp>116.62.XX.XX</LocalGatewayIp>
        <AccessPointId>ap-cn-kojok1****</AccessPointId>
        <CreationTime>2020-06-08T20:20:55</CreationTime>
        <PConnVbrExpireTime>2020-06-08T20:20:55</PConnVbrExpireTime>
        <PhysicalConnectionBusinessStatus>Normal</PhysicalConnectionBusinessStatus>
        <AssociatedPhysicalConnections>
              <Status>Enabled</Status>
              <PeerGatewayIp>116.12.XX.XX</PeerGatewayIp>
              <CircuitCode>12</CircuitCode>
              <PhysicalConnectionId>pc-119mfjzm7****</PhysicalConnectionId>
              <PhysicalConnectionStatus>Normal</PhysicalConnectionStatus>
              <VlanInterfaceId>ri-kojok19x3j0q6k****</VlanInterfaceId>
              <PeerIpv6GatewayIp>2001:XXXX:3:3:4:4:4:4</PeerIpv6GatewayIp>
              <PhysicalConnectionOwnerUid>283117732402483989</PhysicalConnectionOwnerUid>
              <PeeringSubnetMask>255.255.255.252</PeeringSubnetMask>
              <EnableIpv6>false</EnableIpv6>
              <PeeringIpv6SubnetMask>2408:4004:cc:400::/56</PeeringIpv6SubnetMask>
              <LocalGatewayIp>116.62.XX.XX</LocalGatewayIp>
              <LocalIpv6GatewayIp>2001:XXXX:4:4:4:4:4:4</LocalIpv6GatewayIp>
              <VlanId>0</VlanId>
              <PhysicalConnectionBusinessStatus>Normal</PhysicalConnectionBusinessStatus>
        </AssociatedPhysicalConnections>
        <AssociatedCens>
              <CenStatus>Attached</CenStatus>
              <CenOwnerId>253460731706911258</CenOwnerId>
              <CenId>cen-kojok19****</CenId>
        </AssociatedCens>
  </VirtualBorderRouterSet>
```

`JSON` 格式高速通道

```json
{
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6",
    "PageNumber": 1,
    "VirtualBorderRouterSet": {
        "MinRxInterval": 200,
        "PeerGatewayIp": "116.12.XX.XX",
        "Description": "VBR",
        "RouteTableId": "rtb-bp1n****",
        "ActivationTime": "2020-06-08T12:20:55",
        "PhysicalConnectionId": "pc-119mfjzm7x****",
        "PhysicalConnectionStatus": "Normal",
        "VlanInterfaceId": "ri-2zeo3xzyf38r4xx****",
        "VbrId": "vbr-kojok19xx****",
        "PhysicalConnectionOwnerUid": 283117732402484000,
        "PeeringSubnetMask": "255.255.255.252",
        "TerminationTime": "2020-06-08T20:20:55",
        "EnableIpv6": false,
        "PeeringIpv6SubnetMask": "2000:1234:0:a000::/55",
        "Name": "test",
        "RecoveryTime": "2020-06-09T12:20:55",
        "EccId": "ecc-h****",
        "LocalIpv6GatewayIp": "2001:XXXX:4:4:4:4:4:4",
        "VlanId": 10,
        "Status": "Enabled",
        "CircuitCode": "longtel001",
        "MinTxInterval": 200,
        "PeerIpv6GatewayIp": "2001:XXXX:3:3:4:4:4:4",
        "DetectMultiplier": 3,
        "Type": "pconnVBR",
        "LocalGatewayIp": "116.62.XX.XX",
        "AccessPointId": "ap-cn-kojok1****",
        "CreationTime": "2020-06-08T20:20:55",
        "PConnVbrExpireTime": "2020-06-08T20:20:55",
        "PhysicalConnectionBusinessStatus": "Normal",
        "AssociatedPhysicalConnections": {
            "Status": "Enabled",
            "PeerGatewayIp": "116.12.XX.XX",
            "CircuitCode": 12,
            "PhysicalConnectionId": "pc-119mfjzm7****",
            "PhysicalConnectionStatus": "Normal",
            "VlanInterfaceId": "ri-kojok19x3j0q6k****",
            "PeerIpv6GatewayIp": "2001:XXXX:3:3:4:4:4:4",
            "PhysicalConnectionOwnerUid": 283117732402484000,
            "PeeringSubnetMask": "255.255.255.252",
            "EnableIpv6": false,
            "PeeringIpv6SubnetMask": "2408:4004:cc:400::/56",
            "LocalGatewayIp": "116.62.XX.XX",
            "LocalIpv6GatewayIp": "2001:XXXX:4:4:4:4:4:4",
            "VlanId": 0,
            "PhysicalConnectionBusinessStatus": "Normal"
        },
        "AssociatedCens": {
            "CenStatus": "Attached",
            "CenOwnerId": 253460731706911260,
            "CenId": "cen-kojok19****"
        }
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidFilterKey.ValueNotSupport ed | Specified filter key is not supported: Filter.X.key | 该过滤器的Key不支持：Filter.X.key。 |

#### 6.6.7. DescribeVirtualBorderRoutersForPhysicalConnection

调用DescribeVirtualBorderRoutersForPhysicalConnection接口查询指定物理专线下的边界路由器（VBR），包括物理专线所有者的VBR和其他账号的VBR。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVirtualBorderRouter sForPhysicalConnection | 要执行的操作。 取值： DescribeVirtualBorderRoutersForPhysicalConnection。 |
| PhysicalConnectionId | String | 是 | pc-119mfj**** | 物理专线的ID。 |

高速通道

| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
|---|---|---|---|---|
| Filter.N.Key | String | 否 | 1 | 过滤条件的key，其中N取值范围：1~5。 支持过滤参数取值： PhysicalConnectionId：物理专线实例ID。 VbrId：边界路由器实例ID。 Status：边界路由器状态。 Name：边界路由器名称。 AccessPointId：接入点ID。 eccId：高速上云服务实例ID。 type：边界路由器类型。 |
| Filter.N.Value.N | RepeatList | 否 | 1 | 对应过滤条件的取值，其中N取值范围：1~5。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VirtualBorderRouterForPh ysicalConnectionSet | Array of VirtualBorderRouterForPh ysicalConnectionType |  | 查询到的VBR详细信息。 |
| VirtualBorderRouterForPh ysicalConnectionType |  |  |  |
| ActivationTime | String | 2021-06-08T12:20:55 | VBR第一次激活的时间。 |
| Bandwidth | String | 10 | 物理专线下绑定的边界路由器带宽，单位为Mbps。 |
| CircuitCode | String | longtel001 | 运营商为物理专线提供的电路编码。 |
| CreationTime | String | 2021-06-08T12:20:55 | VBR的创建时间。 |
| EccId | String | ecc-sjghe**** | 高速上云服务实例ID。 |
| EnableIpv6 | Boolean | false | 是否启用IPv6，取值： false：启用IPv6。 true：不启用IPv6。 |
| LocalGatewayIp | String | 10.0.XX.XX | VBR的阿里云侧互联IPv4地址。 |
| LocalIpv6GatewayIp | String | 2001:XXXX:3c4d:0015:0000:000 0:0000:1a2b | VBR的阿里云侧互联IPv6地址。 |
| PConnVbrBussinessStatus | String | Available | 物理专线绑定的边界路由器运行状态。 |
| PConnVbrChargeType | String | PrePaid | 物理专线绑定的边界路由器付费类型。取值： PrePaid：预付费，包年包月。选择该类付费方式时，您必须确认自己的账号支持余额支付/信用支付。 PostPaid：按量付费。 |
| PConnVbrExpireTime | String | 2021-06-22T12:20:55 | 物理专线绑定的边界路由器到期时间。 |
| PeerGatewayIp | String | 10.0.XX.XX | VBR的客户侧互联IPv4地址。 |
| PeerIpv6GatewayIp | String | 2001:XXXX:3c4d:0015:0000:000 0:0000:2a2b | VBR的客户侧互联IPv6地址。 |
| PeeringIpv6SubnetMask | String | 2000:1234:0:a000::/55 | VBR的阿里云侧互联IPv6与客户侧互联IPv6的子网掩码。 |
| PeeringSubnetMask | String | 255.255.255.252 | VBR的阿里云侧互联IPv6与客户侧互联IPv4的子网掩码。 |
| RecoveryTime | String | 2021-06-08T12:20:55 | VBR最近一次从Terminated状态恢复到Active状态的时间。 |

高速通道

| Status | String | Available | 边界路由器VBR状态。 |
|---|---|---|---|
| TerminationTime | String | 2021-06-08T20:20:55 | VBR最近一次被终止的时间。 |
| Type | String | pconnVBR | 边界路由器类型。 |
| VbrId | String | vbr-bp16ksp61j7e0tk**** | VBR的ID。 |
| VbrOwnerUid | Long | 253460731706911258 | VBR所有者的账号ID，VBR和物理专线的所有者相同时该参数为空。 |
| VlanId | Integer | 1678 | VBR的VLAN ID。 |
| TotalCount | Integer | 2 | 列表条条目数。 |
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页包含多少条目。 |
| RequestId | String | 7C5AE8B3-A2D8-428D-A2FF- 93A225C0821E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVirtualBorderRoutersForPhysicalConnection &PhysicalConnectionId=pc-119mfj**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeVirtualBorderRoutersResponse> <TotalCount>2</TotalCount> <PageSize>10</PageSize> <RequestId>7C5AE8B3-A2D8-428D-A2FF-93A225C0821E</RequestId> <PageNumber>1</PageNumber> <VirtualBorderRouterForPhysicalConnectionSet> <Status>Available</Status> <PeerGatewayIp>10.0.XX.XX</PeerGatewayIp> <ActivationTime>2021-06-08T12:20:55</ActivationTime> <VbrOwnerUid>253460731706911260</VbrOwnerUid> <CircuitCode>longtel001</CircuitCode> <PeerIpv6GatewayIp>2001:XXXX:3c4d:0015:0000:0000:0000:2a2b</PeerIpv6GatewayIp> <VbrId>vbr-bp16ksp61j7e0tk****</VbrId> <PConnVbrChargeType>PrePaid</PConnVbrChargeType> <PeeringSubnetMask>255.255.255.252</PeeringSubnetMask> <TerminationTime>2021-06-08T20:20:55</TerminationTime> <EnableIpv6>false</EnableIpv6> <PeeringIpv6SubnetMask>2000:1234:0:a000::/55</PeeringIpv6SubnetMask> <RecoveryTime>2021-06-08T12:20:55</RecoveryTime> <LocalGatewayIp>10.0.XX.XX</LocalGatewayIp> <Type>pconnVBR</Type> <Bandwidth>10</Bandwidth> <CreationTime>2021-06-08T12:20:55</CreationTime> <EccId>ecc-sjghe****</EccId> <PConnVbrExpireTime>2021-06-22T12:20:55</PConnVbrExpireTime> <LocalIpv6GatewayIp>2001:XXXX:3c4d:0015:0000:0000:0000:1a2b</LocalIpv6GatewayIp> <VlanId>1678</VlanId> <PConnVbrBussinessStatus>Available</PConnVbrBussinessStatus> </VirtualBorderRouterForPhysicalConnectionSet> </DescribeVirtualBorderRoutersResponse> |  |

`JSON` 格式高速通道

```json
{
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "7C5AE8B3-A2D8-428D-A2FF-93A225C0821E",
    "PageNumber": 1,
    "VirtualBorderRouterForPhysicalConnectionSet": {
        "Status": "Available",
        "PeerGatewayIp": "10.0.XX.XX",
        "ActivationTime": "2021-06-08T12:20:55",
        "VbrOwnerUid": 253460731706911260,
        "CircuitCode": "longtel001",
        "PeerIpv6GatewayIp": "2001:XXXX:3c4d:0015:0000:0000:0000:2a2b",
        "VbrId": "vbr-bp16ksp61j7e0tk****",
        "PConnVbrChargeType": "PrePaid",
        "PeeringSubnetMask": "255.255.255.252",
        "TerminationTime": "2021-06-08T20:20:55",
        "EnableIpv6": false,
        "PeeringIpv6SubnetMask": "2000:1234:0:a000::/55",
        "RecoveryTime": "2021-06-08T12:20:55",
        "LocalGatewayIp": "10.0.XX.XX",
        "Type": "pconnVBR",
        "Bandwidth": 10,
        "CreationTime": "2021-06-08T12:20:55",
        "EccId": "ecc-sjghe****",
        "PConnVbrExpireTime": "2021-06-22T12:20:55",
        "LocalIpv6GatewayIp": "2001:XXXX:3c4d:0015:0000:0000:0000:1a2b",
        "VlanId": 1678,
        "PConnVbrBussinessStatus": "Available"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidPhysicalConnectionId.NotF ound | The specified PhysicalConnectionId does not belong to user. | 该物理专线不属于您的账号。 |

#### 6.6.8. TerminateVirtualBorderRouter

调用TerminateVirtualBorderRouter接口终止边界路由器VBR（Virtual Border Router）。 调用该接口后VBR从**Enabled**状态进入**Terminating**状态，终止成功后进入**Terminated**状态。 只有物理专线的所有者可以调用该接口。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TerminateVirtualBorderRoute r | 要执行的操作。 取值： TerminateVirtualBorderRouter。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要终止的VBR所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VbrId | String | 是 | vbr-bp15zckdt37pq72**** | 要终止的VBR的ID。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=TerminateVirtualBorderRouter &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp15zckdt37pq72****
```

`&<`公共请求参数> 高速通道正常返回示例

| XML | 格式 |
|---|---|
| <TerminateVirtualBorderRouterResponse> <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId> </TerminateVirtualBorderRouterResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidOperation.OperationNotAll owedInState | The specified VirutalBorderRouter is in invalid state. | 该VirutalBorderRouter状态不合法，请检查 VirutalBorderRouter状态。 |
| 403 | Forbidden.OperationTerminateNo tAllowedByUser | The caller is not allowed to terminate the specified VirtualBorderRouter. | 此用户不允许终止此边界路由器。 |

#### 6.6.9. RecoverVirtualBorderRouter

调用RecoverVirtualBorderRouter接口恢复被终止的边界路由器VBR（Virtual Border Router）。

**使用说明**

调用该接口后VBR从**Terminated**状态变为**Recovering**状态，恢复成功后进入**Enabled**状态。 在调用本接口恢复VBR之前，请注意以下事项： 只有物理专线的所有者可以调用该接口。 VBR所属的物理专线必须处于**Enabled**状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RecoverVirtualBorderRouter | 要执行的操作。 取值： RecoverVirtualBorderRouter。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要恢复的VBR所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VbrId | String | 是 | vbr-bp1lhl0taikrte**** | 要恢复的VBR的ID。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RecoverVirtualBorderRouter &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp1lhl0taikrte****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RecoverVirtualBorderRouterResponse> <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId> </RecoverVirtualBorderRouterResponse> |  |

高速通道

| JSON | 格式 |
|---|---|
| { "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidOperation.OperationNotAll owedInState | The specified VirutalBorderRouter is in invalid state | 该边界路由器接口状态不支持该操作。 |
| 400 | OperationFailed.VlanIdAlreadyInU se | The specifed vlanId has been used. | 该VLAN已经被占用。 |
| 403 | Forbidden.OperationRecoverNotA llowedByUser | The caller is not allowed to recover the specified VirtualBorderRouter. | 此用户不允许恢复此边界路由器。 |

#### 6.6.10. ModifyVirtualBorderRouterAttribute

调用ModifyVirtualBorderRouterAttribute接口修改边界路由器VBR（Virtual Border Router）的配置。

**使用说明**

**VlanId**只允许物理专线的所有者修改。
同一物理专线下的同一VLAN ID不允许被两个VBR同时使用。 进入**Terminated**状态的VBR会在7天内自动保留其VLAN ID，不允许其他VBR使用。7天后可以被其他VBR使用。 其他账号的VBR实例，不能配置**LocalGatewayIp**、**PeerGatewayIp**和**PeeringSubnetMask**。
**PeeringSubnetMask**支持24～30位（255.255.255.0～255.255.255.252）。
**LocalGatewayIp**和**PeerGatewayIp**必须在同一个网段内。例如，LocalGatewayIp：192.168.XX.XX，PeerGatewayIp：
192.168.XX.XX，PeeringSubnetMask：255.255.255.248。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyVirtualBorderRouterAtt ribute | 要执行的操作。 取值：ModifyVirtualBorderRouterAttribute。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VBR所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| VbrId | String | 是 | vbr-2zehfr9ovv4b**** | VBR实例ID。 |
| VlanId | Integer | 否 | 0 | VBR的VLAN ID，取值范围：0～2999。 说明只有物理专线的所有者可以指定该参数，同一条物理专线下的两个VBR的VLAN ID不能相同。 |
| CircuitCode | String | 否 | longtel001 | 运营商为物理专线提供的电路编码。 说明只有物理专线的所有者可以指定该参数。 |
| LocalGatewayIp | String | 否 | 192.168.XX.XX | VBR实例的阿里云侧互联IP。 |
| PeerGatewayIp | String | 否 | 192.168.XX.XX | VBR实例的客户侧互联IP。 该属性只允许VBR所有者指定或修改。 为物理专线所有者创建VBR实例时必填，为其他账号创建VBR实例时无需填写。 |
| PeeringSubnetMask | String | 否 | 255.255.255.252 | VBR实例的阿里云侧和客户侧互联IP的子网掩码。 两个IP地址必须位于同一个子网中。 |
| MinTxInterval | Long | 否 | 300 | 配置BFD报文的发送间隔，取值为200～1000，单位为ms。 |
| MinRxInterval | Long | 否 | 300 | 配置BFD报文的接收间隔，取值为200～1000，单位为ms。 |
| DetectMultiplier | Long | 否 | 3 | 检测时间倍数，即接收方允许发送方发送报文的最大连接丢包数，用来检测链路是否正常。 取值：3～10。 |

高速通道

| Description | String | 否 | desc | VBR的描述信息。 长度为2～256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
|---|---|---|---|---|
| Name | String | 否 | VBR | VBR的名称。 长度为2～128个字符，必须以字母或中文开头，可包含数字、下划线 （_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
| AssociatedPhysicalConnectio ns | String | 否 | pc-kojok19****** | 物理专线实例ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 00xxxxxxxx | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| LocalIpv6GatewayIp | String | 否 | 2001:XXXX:3c4d:0015:0000: 0000:0000:1a2b | VBR实例的阿里云侧互联IPv6地址。 |
| PeerIpv6GatewayIp | String | 否 | 2001:XXXX:3c4d:0015:0000: 0000:0000:1a2b | VBR实例的客户侧互联IPv6地址。 该属性只允许VBR所有者指定或者修改。 为物理专线所有者创建VBR实例时必填，为其他账号创建VBR实例时 |
| PeeringIpv6SubnetMask | String | 否 | 2408:4004:cc:400::/56 | VBR实例的阿里云侧和客户侧互联IPv6的子网掩码。 两个IPv6地址必须位于同一个子网中。 |
| EnableIpv6 | Boolean | 否 | false | 是否启用IPv6。 true：开启。 false（默认值）：关闭。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF-8542- EBB34FD358AB | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyVirtualBorderRouterAttribute &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-2zehfr9ovv4b****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyVirtualBorderRouterAttributeResponse> <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId> </ModifyVirtualBorderRouterAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | The specified RegionId is not found. | 指定的RegionId不存在，请您检查此产品在该地域是否可用。 |
| 400 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | 该VLAN已经被占用。 |
| 400 | InvalidCircuitCode.Malformed | The specified CircuitCode is not valid. | 该CircuitCode不合法。 |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | 参数VlanId的值不合法。 |
| 400 | InvalidIp.Malformed | The specified ip address is not valid. | 指定的私网 IP 不合法，请您检查该私网IP是否正确。 |
| 400 | InvalidPeeringSubnetMask.Malfor med | The specified PeeringSubnetMask is not valid. | 指定的PeeringSubnetMask不合法，请您检查该参数是否正确。 |

高速通道

| 403 | Forbidden.CircuitCodeNotAllowed ByCaller | The caller is not allowed to modify. | 不允许修改CircuitCode参数。 |
|---|---|---|---|
| 403 | Forbidden.CircuitCodeNotAllowed ByCaller | The caller is not allowed to specify the CircuitCode parameter. | 不允许指定CircuitCode参数。 |
| 403 | Forbidden.LocalGatewayIpNotAllo wedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | 不允许指定LocalGatewayIp参数。 |
| 403 | Forbidden.PeerGatewayIpNotAllo wedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | 不允许指定PeerGatewayIp参数。 |
| 403 | Forbidden.PeeringSubnetMaskNot AllowedByCaller | The caller is not allowed to specify the PeeringSubnetMask parameter. | 不允许指定PeeringSubnetMask参数。 |
| 403 | Forbidden.VlanIdNotAllowedByCal ler | The caller is not allowed to specify the VlanId. | 不允许指定VLAN ID。 |
| 403 | Forbidden.NameNotAllowedByCal ler | The caller is not allowed to specify the Name parameter. | 不允许指定Name参数。 |
| 403 | Forbidden.DescriptionNotAllowed ByCaller | The caller is not allowed to specify the Description parameter. | 不允许指定Description参数。 |
| 400 | InvalidIp.NotSameSubnet | Local gateway ip and peer gateway ip are not in the same subnet. | 本地网关IP地址与对端网关IP地址不在同一个子网内。 |

#### 6.6.11. AssociatePhysicalConnectionToVirtualBorderRouter

调用AssociatePhysicalConnectionToVirtualBorderRouter接口将VBR关联至物理专线。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssociatePhysicalConnection ToVirtualBorderRouter | 要执行的操作。 取值：AssociatePhysicalConnectionToVirtualBorderRouter 。 |
| PhysicalConnectionId | String | 是 | pc-bp1qrb3044eqixog**** | 物理专线ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 物理专线实例所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VbrId | String | 是 | vbr-bp186tnz6rijyhj**** | 边界路由器ID。 |
| VlanId | String | 是 | 123 | 边界路由器的VLAN ID。 取值范围：1~2999。 说明只有物理专线的所有者可以指定该参数，同一条物理专线下的两个VBR的VLAN ID不能相同。 |
| CircuitCode | String | 否 | longtel001 | 运营商为物理专线提供的电路编码。 说明只有物理专线的所有者可以指定该参数。 |
| LocalGatewayIp | String | 否 | 10.10.XX.XX | VBR的阿里云侧互联IP。 |
| PeerGatewayIp | String | 否 | 10.10.XX.XX | VBR专线侧接口对端的IP地址。 该属性只允许VBR的所有者指定或者修改，不允许把Enabled状态的 VBR的该属性改为空。 |
| PeeringSubnetMask | String | 否 | 255.255.255.0 | VBR的阿里云侧和客户侧互联IP的子网掩码。 两个IP地址必须位于同一个子网中。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
| LocalIpv6GatewayIp | String | 否 | 2001:XXXX:3c4d:0015:0000: 0000:0000:1a2b | VBR实例的阿里云侧互联IPv6地址。 |

高速通道

| PeerIpv6GatewayIp | String | 否 | 2001:XXXX:3c4d:0015:0000: 0000:0000:2a2b | VBR实例的客户侧互联IPv6地址。 |
|---|---|---|---|---|
| PeeringIpv6SubnetMask | String | 否 | 2408:4004:cc:400::/56 | VBR实例的阿里云侧和客户侧互联IPv6的子网掩码。 两个IPv6地址必须位于同一个子网。 |
| EnableIpv6 | String | 否 | true | 是否启用IPv6。取值： true：开启。 false：关闭。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF-8542- EBB34FD358AB | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AssociatePhysicalConnectionToVirtualBorderRouter &PhysicalConnectionId= pc-bp1qrb3044eqixog**** &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp186tnz6rijyhj**** &VlanId=123
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <AssociatePhysicalConnectionToVirtualBorderRouterResponse> <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId> </AssociatePhysicalConnectionToVirtualBorderRouterResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.NotFound | The specified Instance does not exist in the specified region. | 该实例在该地域内不存在。 |
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidOperation.RouterInterface NotDeleted | The specified VirutalBorderRouter still has routerInterface. | 该边界路由器还有关联的路由器接口。 |
| 400 | InvalidOperation.OperationNotAll owedInState | The specified VirutalBorderRouter is in invalid state. | 该VirutalBorderRouter状态不合法，请检查 VirutalBorderRouter状态。 |
| 403 | Forbidden.OperationNotAllowedB yUser | The caller is not allowed to delete the specified VirtualBorderRouter. | 不允许删除边界路由器。 |
| 403 | Forbidden.MultiVlanRi | Multiple vlan router interfaces are found. | 存在多个VLAN路由器接口。 |
| 403 | Forbidden.NoRiFound | No vlan router interfaces are found. | 没有可用的VLAN路由器接口。 |
| 400 | InvalidStatus.NotAllowed | Invalid virtual border router status. | 当前边界路由器的状态不支持该操作。 |
| 404 | InvalidRegionId.NotFound | The specified RegionId is not found. | 指定的RegionId不存在，请您检查此产品在该地域是否可用。 |
| 400 | InvalidPhysicalConnectionId.NotF ound | The specified PhysicalConnectionId is not found. | 该物理专线ID不存在。 |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | 该VLAN已经被占用。 |
| 400 | MissingParameter | The input parameter 'PhysicalConnectionId' that is mandatory for processing this request is not supplied. | 必须指定参数PhysicalConnectionId。 |
| 400 | InvalidPhysicalConnectionId.NotE nabled | The specified PhysicalConnectionId is not in Enabled state. | 该物理专线当前未处于正常状态，请检查物理专线后再创建。 |
| 404 | InvalidVbrOwnerId.NotFound | The specified VbrOwnerId is not valid. | 参数VbrOwnerId的值不合法。 |
| 400 | MissingParameter | The input parameter 'VlanId' that is mandatory for processing this request is not supplied. | 必须指定参数VlanId。 |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | 参数VlanId的值不合法。 |

高速通道

| 400 | InvalidCircuitCode.Malformed | The specified CircuitCode is not valid. | 该CircuitCode不合法。 |
|---|---|---|---|
| 400 | MissingParameter | The input parameter 'LocalGatewayIp' that is mandatory for processing this request is not supplied. | 必须指定参数LocalGatewayIp。 |
| 400 | InvalidLocalGatewayIp.Malformed | The specified LocalGatewayIp is not valid. | 该本端网关的IP不合法。 |
| 400 | MissingParameter | The input parameter 'PeerGatewayIp' that is mandatory for processing this request is not supplied. | 必须指定参数PeerGatewayIp。 |
| 400 | InvalidPeerGatewayIp.Malformed | The specified PeerGatewayIp is not valid. | 参数PeerGatewayIp的值不合法。 |
| 400 | MissingParameter | The input parameter 'PeeringSubnetMask' that is mandatory for processing this request is not supplied. | 必须指定参数PeeringSubnetMask。 |
| 400 | InvalidPeeringSubnetMask.Malfor med | The specified PeeringSubnetMask is not valid. | 指定的PeeringSubnetMask不合法，请您检查该参数是否正确。 |
| 403 | Forbidden.LocalGatewayIpNotAllo wedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | 不允许指定LocalGatewayIp参数。 |
| 403 | Forbidden.PeerGatewayIpNotAllo wedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | 不允许指定PeerGatewayIp参数。 |
| 403 | Forbidden.PeeringSubnetMaskNot AllowedByCaller | The caller is not allowed to specify the PeeringSubnetMask parameter. | 不允许指定PeeringSubnetMask参数。 |
| 403 | Forbidden.NameNotAllowedByCal ler | The caller is not allowed to specify the Name parameter. | 不允许指定Name参数。 |
| 403 | Forbidden.DescriptionNotAllowed ByCaller | The caller is not allowed to specify the Description parameter. | 不允许指定Description参数。 |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | 该名称格式不合法。 |
| 400 | InvalidDescription.Malformed | The specifid ?Description? is not valid. | 指定的资源描述格式不合法。长度为2～256个字符，不能以http://和https://开头。 |
| 400 | QuotaExceeded.vbrPerpConn | Virtual boarder router per PhysicalConnection quota exceed. | 超过了每个物理专线上的边界路由器配额上限，请您减少该物理专线上的边界路由器数量后再试。 |
| 400 | EXCEEDASSOCIATEMAXNUM _ _ _ | assocaite virtual boarder num too many. | 关联的边界路由器达到配额上限。 |
| 400 | InvalidIP.Malformed | Ip malformed. | IP格式不合法。 |
| 400 | InvalidIp.NotSameSubnet | Local gateway ip and peer gateway ip are not in the same subnet. | 本地网关IP地址与对端网关IP地址不在同一个子网内。 |
| 400 | InvalidStatus.StatusNotEnabled | The physical connection status is invalid. | 物理专线状态不支持此操作，请检查物理专线状态。 |
| 400 | PHYSICALNOTALLOWASSOCIA _ _ _ TEVBR _ | The specified operation not allow. | 无法执行该操作，物理专线有关联的边界路由器。 |

#### 6.6.12. UnassociatePhysicalConnectionFromVirtualBorderRouter

调用UnassociatePhysicalConnectionFromVirtualBorderRouter接口解绑边界路由器VBR（Virtual Border Router）和物理专线。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UnassociatePhysicalConnecti onFromVirtualBorderRouter | 要执行的操作。 取值：UnassociatePhysicalConnectionFromVirtualBorderR outer。 |
| PhysicalConnectionId | String | 是 | pc-bp1qrb3044eqixog**** | 要解绑的物理专线ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要解绑的物理专线所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VbrId | String | 是 | vbr-bp16ksp61j7e0tkn***** | 要解绑的VBR的ID。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

高速通道

| RequestId | String | 980960B0-2969-40BF-8542- EBB34FD358AB | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UnassociatePhysicalConnectionFromVirtualBorderRouter &PhysicalConnectionId=pc-bp1qrb3044eqixog**** &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp16ksp61j7e0tkn*****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <UnassociatePhysicalConnectionFromVirtualBorderRouterResponse> <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId> </UnassociatePhysicalConnectionFromVirtualBorderRouterResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter or PhysicalConnection does not exist in our records. | 该边界路由器或物理专线不存在。 |
| 400 | PARAMETERMUSTNOTNULL _ _ _ | The specified physical connection id or vbrId must not be null. | 必须指定参数vbrId和physicalconnectionId。 |
| 400 | PHYSICALNOTASSOCIATETOV _ _ _ _ BR | The specified PhysicalConnection have not associate to the vbr. | 该物理专线没有创建边界路路由器。 |
| 400 | ROUTERINTERFACEREFEREDB _ _ _ YROUTEENTRY _ | The specified VlanInterface has been used by routeEntry. | 该VLAN接口已经使用在路由条目中。 |
| 400 | InvalidStatus.NotAllowed | Invalid virtual border router status. | 当前边界路由器的状态不支持该操作。 |
| 400 | PHYSICALNOTALLOWASSOCIA _ _ _ TEVBR _ | The specified operation not allow. | 无法执行该操作，物理专线有关联的边界路由器。 |

### BGP

#### 6.7.1. CreateBgpGroup

使用CreateBgpGroup为指定的边界路由器VBR（Virtual Border Router）创建一个BGP组。 您可以通过BGP实现VBR与本地IDC的互通。每个BGP组关联一个VBR，您仅需将与VBR通信的BGP邻居添加到对应的BGP组中，然后在VBR中宣告BGP网络即可。 BGP组主要是用于简化BGP配置，可以将需要不断重复的配置合并到一个组中，减少配置复杂度。您需根据AS号码建立一个BGP组。 调用本接口创建BGP组时，请注意： BGP组支持的BGP版本为BGP4。 BGP组支持IPv4 BGP，不支持IPv6 BGP。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateBgpGroup | 要执行的操作。 取值： CreateBgpGroup。 |
| PeerAsn | Long | 是 | 65515 | 本地侧设备AS号。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | BGP组所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterId | String | 是 | vbr-m5eadkqe6budw4sj**** | BGP组关联的VBR的ID。 |

高速通道

| Name | String | 否 | test | BGP组的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字，半角句号（.），下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
|---|---|---|---|---|
| Description | String | 否 | BGP | BGP组的描述信息。 长度为2~256个字符，必须以字母或中文开头， 但不能以 http:// 或 https:// 开头。 |
| LocalAsn | Long | 否 | 45104 | 阿里云侧设备AS号。 |
| AuthKey | String | 否 | !PWZ**** | BGP组的认证密钥。 |
| IsFakeAsn | Boolean | 否 | true | 是否指定伪AS号。取值： false（默认值）：否。 true：是。 说明运行BGP的路由器一般只能属于一个AS。当需要用新的AS替代原有的AS（例如AS需要迁移或者和其他AS合并），并且因为业务等客观因素无法立即修改BGP配置时，可以通过指定伪 AS号与本端建立连接，保证业务不中断。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
| IpVersion | String | 否 | ipv4 | IP版本。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BgpGroupId | String | bgpg-2zendnzngq9lkjkhv**** | 新建的BGP组的ID。 |
| RequestId | String | C1221A1F-2ACD-4592-8F27- 474E02883159 | 请求ID。 |

**示例**

请求示例

```
&PeerAsn=45103 &RegionId=cn-qingdao-env66-d01 &RouterId= vbr-m5eadkqe6budw4sj****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateBgpGroupResponse> <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId> <BgpGroupId>bgpg-2zendnzngq9lkjkhv****</BgpGroupId> </CreateBgpGroupResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "C1221A1F-2ACD-4592-8F27-474E02883159", "BgpGroupId": "bgpg-2zendnzngq9lkjkhv****" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | NQA数超过VBR配额。 |
| 400 | QuotaExceeded.BgpNetwork | bgp network count per vbr quota exceed. | 边界路由器的BGP网络数量已达到配额。 |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | 多物理专线的IP地址不能为空。 |

高速通道

| 400 | InvalidVbrNetwork | vbr netowrk not exists | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
|---|---|---|---|
| 400 | InvalidBgpGroup | bgp group not exists | 该BGP组不存在。 |
| 400 | InvalidBgpName.Malformed | Specified Bgp Group name is not valid. | 该BGP组的名称不合法。 |
| 400 | InvalidBgpDescription.Malformed | Specified Bgp Group description is not valid. | 该BGP组的描述不合法。 |
| 400 | InvalidBgpAuthkey.Malformed | Specified Bgp Group authkey is not valid. | 该BGP组的验证密钥不合法。 |
| 404 | InvalidRegionId.NotFound | The specified RegionId is not found. | 指定的RegionId不存在，请您检查此产品在该地域是否可用。 |
| 400 | InvalidIP.Malformed | Ip malformed. | IP格式不合法。 |
| 400 | InvalidPeerAsn.Malformed | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotFound | instance not found | 实例不存在。 |
| 400 | InvalidParams.NotFound | vpc instance not found | 该VPC不存在，请您检查输入的VPC是否正确。 |
| 400 | InvalidParams.AlreadyExists | bgp network already exists | BGP网络已经存在。 |
| 400 | InvalidStatus.CannotOperate | invalid status cannot operate | 状态不合法，无法执行该操作。 |
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |

#### 6.7.2. DescribeBgpGroups

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBgpGroups | 要执行的操作。 取值： DescribeBgpGroups。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | BGP组所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterId | String | 否 | vbr-m5eadkqe6budw4sj0**** | 要查询的BGP组关联的VBR ID。 |
| BgpGroupId | String | 否 | bgpg-wz9f62v4fbg2g**** | 要查询的BGP组ID。 |
| IsDefault | Boolean | 否 | false | 是否为默认BGP组。 |
| PageNumber | Integer | 否 | 1 | 列表的页码。默认值：1。 |
| PageSize | Integer | 否 | 1 | 分页查询时每页的行数。最大值：50。默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TotalCount | Integer | 10 | 列表条条目数。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| PageSize | Integer | 5 | 分页查询时每页的行数。 |
| BgpGroups | Array of BgpGroup |  | BGP组的详细信息。 |
| BgpGroup |  |  |  |
| AuthKey | String | !PWZ**** | BGP组使用的密钥。 |
| BgpGroupId | String | bgpg-wz9f62v4fbg2g**** | BGP组ID。 |
| Description | String | test | BGP组描述信息。 |
| Hold | String | 30 | 等待BGP消息传入的保持时间。如果超过保持时间还没有消息传入，则认为BGP 邻居断开了连接。 |

高速通道

| IpVersion | String | IPv4 | IP版本。 |
|---|---|---|---|
| IsFake | String | true | AS号是否为假。 |
| Keepalive | String | 10 | 保活时间。 |
| LocalAsn | String | 45104 | 阿里云侧设备的AS号。 |
| Name | String | BGP名称 | BGP组的名称。 |
| PeerAsn | String | 1**** | 本地侧设备的AS号。 |
| RegionId | String | cn-shangha | BGP组所属的地域ID。 |
| RouteLimit | String | 99 | 路由限制。 |
| RouterId | String | vbr-m5eadkqe6budw4sj0**** | VBR ID。 |
| Status | String | Available | BGP组的状态。 |
| RequestId | String | 1D0971B2-A35A-42C1-A44C- E91360C36C0B | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeBgpGroupsResponse> <TotalCount>10</TotalCount> <PageSize>5</PageSize> <RequestId>1D0971B2-A35A-42C1-A44C-E91360C36C0B</RequestId> <PageNumber>1</PageNumber> <BgpGroups> <Status>Available</Status> <Description>test</Description> <IpVersion>IPv4</IpVersion> <Keepalive>10</Keepalive> <RouterId>vbr-m5eadkqe6budw4sj0****</RouterId> <PeerAsn>1****</PeerAsn> <Name>BGP名称</Name> <LocalAsn>45104</LocalAsn> <IsFake>true</IsFake> <AuthKey>!PWZ****</AuthKey> <RouteLimit>99</RouteLimit> <RegionId>cn-shangha</RegionId> <Hold>30</Hold> <BgpGroupId>bgpg-wz9f62v4fbg2g****</BgpGroupId> </BgpGroups> </DescribeBgpGroupsResponse> |  |

`JSON` 格式高速通道

```json
{
    "TotalCount": 10,
    "PageSize": 5,
    "RequestId": "1D0971B2-A35A-42C1-A44C-E91360C36C0B",
    "PageNumber": 1,
    "BgpGroups": {
        "Status": "Available",
        "Description": "test",
        "IpVersion": "IPv4",
        "Keepalive": 10,
        "RouterId": "vbr-m5eadkqe6budw4sj0****",
        "PeerAsn": "1****",
        "Name": "BGP名称",
        "LocalAsn": 45104,
        "IsFake": true,
        "AuthKey": "!PWZ****",
        "RouteLimit": 99,
        "RegionId": "cn-shangha",
        "Hold": 30,
        "BgpGroupId": "bgpg-wz9f62v4fbg2g****"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 请求处理由于某些未知错误失败。 |
| 404 | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. | 指定的RegionId不存在。 |

#### 6.7.3. ModifyBgpGroupAttribute

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBgpGroupAttribute | 要执行的操作。 取值： ModifyBgpGroupAttribute。 |
| BgpGroupId | String | 是 | bgpg-wz9f62v4fbg2g**** | 要修改的BGP组的ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | BGP组所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| Name | String | 否 | test | BGP组的名称。 长度为2-128个字符，必须以字母或中文开头，可包含数字，半角句号 （.），下划线（_）和短划线（-），但不能以 http:// 或 https:// 开头。 |
| Description | String | 否 | BGP | BGP组的描述信息。 长度为2-256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| LocalAsn | Long | 否 | 45104 | 阿里云侧设备AS号。 |
| PeerAsn | Long | 否 | 65515 | 本地侧设备AS号。 |
| AuthKey | String | 否 | !PWZ2**** | BGP组的认证密钥。 |
| IsFakeAsn | Boolean | 否 | false | 是否指定伪AS号。取值： false（默认值）：否。 true：是。 说明运行BGP的路由器一般只能属于一个AS。当需要用新的AS替代原有的AS（例如AS需要迁移或者和其他AS合并），并且因为业务等客观因素无法立即修改BGP配置时，可以通过指定伪 AS号与本端建立连接，保证业务不中断。 |

高速通道

| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 8C3C6D7C-A1CE-4FD8-BC57- DC493A55F76F | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyBgpGroupAttribute &BgpGroupId=bgpg-wz9f62v4fbg2g**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyBgpGroupAttributeResponse> <RequestId>8C3C6D7C-A1CE-4FD8-BC57-DC493A55F76F</RequestId> </ModifyBgpGroupAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "8C3C6D7C-A1CE-4FD8-BC57-DC493A55F76F" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | Specified value of "regionId" is not supported. | 指定的 RegionId 不存在，请您检查此产品在该地域是否可用。 |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | NQA数超过VBR配额。 |
| 400 | QuotaExceeded.BgpNetwork | bgp network count per vbr quota exceed. | 边界路由器的BGP网络数量已达到配额。 |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | 多物理专线的IP地址不能为空。 |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidBgpGroup | bgp group not exists | 该BGP组不存在。 |
| 400 | InvalidBgpName.Malformed | Specified Bgp Group name is not valid. | 该BGP组的名称不合法。 |
| 400 | InvalidBgpDiscription.Malformed | Specified Bgp Group description is not valid. | 该BGP组的描述不合法。 |
| 400 | InvalidBgpAuthkey.Malformed | Specified Bgp Group authkey is not valid. | 该BGP组的验证密钥不合法。 |
| 400 | InvalidIP.Malformed | Ip malformed. | IP格式不合法。 |
| 400 | InvalidPeerAsn.Malformed | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotFound | instance not found | 实例不存在。 |
| 400 | InvalidParams.NotFound | vpc instance not found | 该VPC不存在，请您检查输入的VPC是否正确。 |
| 400 | InvalidParams.AlreadyExists | bgp network already exists | BGP网络已经存在。 |
| 400 | InvalidStatus.CannotOperate | invalid status cannot operate | 状态不合法，无法执行该操作。 |

#### 6.7.4. DeleteBgpGroup

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteBgpGroup | 要执行的操作。 取值： DeleteBgpGroup。 |

| 高速通道 |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|

| BgpGroupId | String | 是 | bgpg-wz9f62v4fbg2g**** | 要删除的BGP组的ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao-env66-d01 | BGP组所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 97E2E97F-968C-48AF-A310- AC4D068854DB | 请求ID。 |

**示例**

请求示例

```
&BgpGroupId=bgpg-wz9f62v4fbg2g**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteBgpGroupResponse> <RequestId>97E2E97F-968C-48AF-A310-AC4D068854DB</RequestId> </DeleteBgpGroupResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "97E2E97F-968C-48AF-A310-AC4D068854DB" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | Specified value of "regionId" is not supported. | 指定的 RegionId 不存在，请您检查此产品在该地域是否可用。 |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | NQA数超过VBR配额。 |
| 400 | QuotaExceeded.BgpNetwork | bgp network count per vbr quota exceed. | 边界路由器的BGP网络数量已达到配额。 |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | 多物理专线的IP地址不能为空。 |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidBgpGroup | bgp group not exists | 该BGP组不存在。 |
| 400 | InvalidBgpName.Malformed | Specified Bgp Group name is not valid. | 该BGP组的名称不合法。 |
| 400 | InvalidBgpDiscription.Malformed | Specified Bgp Group description is not valid. | 该BGP组的描述不合法。 |
| 400 | InvalidBgpAuthkey.Malformed | Specified Bgp Group authkey is not valid. | 该BGP组的验证密钥不合法。 |
| 400 | InvalidIP.Malformed | Ip malformed. | IP格式不合法。 |
| 400 | InvalidPeerAsn.Malformed | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotFound | instance not found | 实例不存在。 |
| 400 | InvalidParams.NotFound | vpc instance not found | 该VPC不存在，请您检查输入的VPC是否正确。 |
| 400 | InvalidParams.AlreadyExists | bgp network already exists | BGP网络已经存在。 |

高速通道

| 400 | InvalidStatus.CannotOperate | invalid status cannot operate | 状态不合法，无法执行该操作。 |
|---|---|---|---|

#### 6.7.5. CreateBgpPeer

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateBgpPeer | 要执行的操作。 取值： CreateBgpPeer。 |
| BgpGroupId | String | 是 | bgpg-wz9f62v4fbg**** | 要添加BGP邻居的BGP组的ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | BGP组所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| PeerIpAddress | String | 否 | 116.62.XX.XX | BGP邻居的IP地址。 |
| EnableBfd | Boolean | 否 | true | 是否开启BFD功能，取值： true：开启BFD功能。 false：不开启BFD功能。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
| IpVersion | String | 否 | ipv4 | IP版本。 |
| BfdMultiHop | Integer | 否 | 3 | BFD多跳。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BgpPeerId | String | bgp-m5eoyp2mwegk8ce9v**** | BGP邻居的ID。 |
| RequestId | String | D4B7649A-61BB-4C64-A586- 1DFF1EDA6A42 | 请求ID。 |

**示例**

请求示例

```
&BgpGroupId=bgpg-wz9f62v4fbg**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateBgpPeerResponse> <BgpPeerId>bgp-m5eoyp2mwegk8ce9v****</BgpPeerId> <RequestId>D4B7649A-61BB-4C64-A586-1DFF1EDA6A42</RequestId> </CreateBgpPeerResponse> |  |

| JSON | 格式 |
|---|---|
| { "BgpPeerId": "bgp-m5eoyp2mwegk8ce9v****", "RequestId": "D4B7649A-61BB-4C64-A586-1DFF1EDA6A42" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | Specified value of "regionId" is not supported. | 指定的 RegionId 不存在，请您检查此产品在该地域是否可用。 |

高速通道

| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | NQA数超过VBR配额。 |
| 400 | QuotaExceeded.BgpNetwork | bgp network count per vbr quota exceed. | 边界路由器的BGP网络数量已达到配额。 |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | 多物理专线的IP地址不能为空。 |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidBgpGroup | bgp group not exists | 该BGP组不存在。 |
| 400 | InvalidBgpName.Malformed | Specified Bgp Group name is not valid. | 该BGP组的名称不合法。 |
| 400 | InvalidBgpDiscription.Malformed | Specified Bgp Group description is not valid. | 该BGP组的描述不合法。 |
| 400 | InvalidBgpAuthkey.Malformed | Specified Bgp Group authkey is not valid. | 该BGP组的验证密钥不合法。 |
| 400 | InvalidIP.Malformed | Ip malformed. | IP格式不合法。 |
| 400 | InvalidPeerAsn.Malformed | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotFound | instance not found | 实例不存在。 |
| 400 | InvalidParams.NotFound | vpc instance not found | 该VPC不存在，请您检查输入的VPC是否正确。 |
| 400 | InvalidParams.AlreadyExists | bgp network already exists | BGP网络已经存在。 |
| 400 | InvalidStatus.CannotOperate | invalid status cannot operate | 状态不合法，无法执行该操作。 |

#### 6.7.6. DescribeBgpPeers

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBgpPeers | 要执行的操作。 取值： DescribeBgpPeers。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | BGP组所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterId | String | 否 | vbr-2zecmmvg5gvu8i4te**** | BGP邻居关联的VBR ID。 |
| BgpPeerId | String | 否 | bgp-2ze3un0ft1jd1xd**** | BGP邻居ID。 |
| BgpGroupId | String | 否 | bgpg-2zev8h2wo414sfh**** | 指定BGP组ID。 |
| IsDefault | Boolean | 否 | false | 是否是默认BGP组。取值 true：是默认BGP组。 false：不是默认BGP组。 |
| PageNumber | Integer | 否 | 1 | 列表的页码。默认值：1。 |
| PageSize | Integer | 否 | 1 | 分页查询时每页的行数。最大值：50。默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BgpPeers | Array of BgpPeer |  | BGP邻居的详细信息。 |
| BgpPeer |  |  |  |
| Name | String | test | BGP邻居名称。 |
| PeerIpAddress | String | 116.62.XX.XX | BGP邻居IP地址。 |
| AuthKey | String | !PWZ**** | BGP组认证密钥。 |

高速通道

| RouterId | String | vbr-2zecmmvg5gvu8i4te**** | BGP邻居关联的VBR ID。 |
|---|---|---|---|
| Status | String | Available | BGP邻居的状态。取值： Pending：配置中。 Available：可用。 Modifying：修改中。 Deleting：删除中。 Deleted：已删除。 |
| BfdMultiHop | Integer | 3 | BFD多跳。 |
| BgpGroupId | String | bgp-2zev8h2wo414sfh**** | BGP组ID。 |
| BgpPeerId | String | bgp-2ze3un0ft1jd1xd**** | BGP邻居ID。 |
| BgpStatus | String | Connect | BGP的连接状态。取值： creating：创建中。 Connect：使用中。 modifying：修改中。 deleting：删除中。 deleted：已删除。 |
| Description | String | test | BGP邻居的描述。 |
| EnableBfd | Boolean | true | 是否开启了BFD协议。 |
| Hold | String | 30 | 保持时间。 |
| IpVersion | String | ipv4 | IP版本。 |
| IsFake | String | true | 是否启用了Fake AS号。 |
| Keepalive | String | 10 | 保活时间。 |
| LocalAsn | String | 45104 | 阿里云设备AS号。 |
| PeerAsn | String | 65515 | BGP邻居的ASN。 |
| RegionId | String | cn-qingdao-env66-d01 | BGP邻居所属的地域ID。 |
| RouteLimit | String | 99 | 路由限制。 |
| TotalCount | Integer | 10 | 列表条目数。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| PageSize | Integer | 2 | 分页查询时每页的行数。 |
| RequestId | String | DE77A7F3-3B74-41C0-A5BC- CAFD188C28B6 | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式高速通道

```xml
  <TotalCount>10</TotalCount>
  <BgpPeers>
        <Status>active</Status>
        <Description>test</Description>
        <IpVersion>ipv4</IpVersion>
        <PeerIpAddress>116.62.XX.XX</PeerIpAddress>
        <Keepalive>10</Keepalive>
        <RouterId>vbr-2zecmmvg5gvu8i4te****</RouterId>
        <PeerAsn>65515</PeerAsn>
        <Name>test</Name>
        <BgpPeerId>bgp-2ze3un0ft1jd1xd****</BgpPeerId>
        <LocalAsn>45104</LocalAsn>
        <BfdMultiHop>3</BfdMultiHop>
        <EnableBfd>true</EnableBfd>
        <BgpStatus>Connect</BgpStatus>
        <IsFake>true</IsFake>
        <AuthKey>!PWZ****</AuthKey>
        <RouteLimit>99</RouteLimit>
        <RegionId>cn-qingdao-env66-d01</RegionId>
        <Hold>30</Hold>
        <BgpGroupId>bgp-2zev8h2wo414sfh****</BgpGroupId>
  </BgpPeers>
  <PageSize>2</PageSize>
  <RequestId>DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6</RequestId>
  <PageNumber>1</PageNumber>
```

| JSON | 格式 |
|---|---|
| { "TotalCount": 10, "BgpPeers": { "Status": "active", "Description": "test", "IpVersion": "ipv4", "PeerIpAddress": "116.62.XX.XX", "Keepalive": 10, "RouterId": "vbr-2zecmmvg5gvu8i4te****", "PeerAsn": 65515, "Name": "test", "BgpPeerId": "bgp-2ze3un0ft1jd1xd****", "LocalAsn": 45104, "BfdMultiHop": 3, "EnableBfd": true, "BgpStatus": "Connect", "IsFake": true, "AuthKey": "!PWZ****", "RouteLimit": 99, "RegionId": "cn-qingdao-env66-d01", "Hold": 30, "BgpGroupId": "bgp-2zev8h2wo414sfh****" }, "PageSize": 2, "RequestId": "DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6", "PageNumber": 1 } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 请求处理由于某些未知错误失败。 |
| 404 | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. | 指定的RegionId不存在。 |

#### 6.7.7. ModifyBgpPeerAttribute

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBgpPeerAttribute | 要执行的操作。 取值：ModifyBgpPeerAttribute。 |
| BgpPeerId | String | 是 | Bgp- m5eoyp2mwegk8ce9v**** | 要修改的BGP邻居的ID。 |

高速通道

| RegionId | String | 是 | cn-qingdao-env66-d01 | BGP邻居所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
|---|---|---|---|---|
| BgpGroupId | String | 否 | bgpg-wz9f62v4fbg**** | BGP组的ID。 |
| PeerIpAddress | String | 否 | 116.62.XX.XX | BGP邻居的IP地址。 |
| EnableBfd | Boolean | 否 | true | 是否开启BFD功能。取值： true：开启BFD功能。 false：不开启BFD功能。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
| BfdMultiHop | Integer | 否 | 3 | BFD多跳。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | D4B7649A-61BB-4C64-A586- 1DFF1EDA6A42 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyBgpPeerAttribute &BgpPeerId=Bgp-m5eoyp2mwegk8ce9v**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyBgpPeerAttributeResponse> <RequestId>D4B7649A-61BB-4C64-A586-1DFF1EDA6A42</RequestId> </ModifyBgpPeerAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "D4B7649A-61BB-4C64-A586-1DFF1EDA6A42" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. | 指定的RegionId不存在。 |

#### 6.7.8. DeleteBgpPeer

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteBgpPeer | 要执行的操作。 取值： DeleteBgpPeer。 |
| BgpPeerId | String | 是 | bgp-wz977wcrmb69a**** | 要删除的BGP邻居ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | BGP邻居所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |

高速通道

| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | AEBB1EB6-3C15-4A35-B4CE- 03485200C143 | 请求ID。 |

**示例**

请求示例

```
&BgpPeerId=bgp-wz977wcrmb69a**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteBgpPeerResponse> <RequestId>AEBB1EB6-3C15-4A35-B4CE-03485200C143</RequestId> </DeleteBgpPeerResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "AEBB1EB6-3C15-4A35-B4CE-03485200C143" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | Specified value of "regionId" is not supported. | 指定的 RegionId 不存在，请您检查此产品在该地域是否可用。 |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | NQA数超过VBR配额。 |
| 400 | QuotaExceeded.BgpNetwork | bgp network count per vbr quota exceed. | 边界路由器的BGP网络数量已达到配额。 |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | 多物理专线的IP地址不能为空。 |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidBgpGroup | bgp group not exists | 该BGP组不存在。 |
| 400 | InvalidBgpName.Malformed | Specified Bgp Group name is not valid. | 该BGP组的名称不合法。 |
| 400 | InvalidBgpDiscription.Malformed | Specified Bgp Group description is not valid. | 该BGP组的描述不合法。 |
| 400 | InvalidBgpAuthkey.Malformed | Specified Bgp Group authkey is not valid. | 该BGP组的验证密钥不合法。 |
| 400 | InvalidIP.Malformed | Ip malformed. | IP格式不合法。 |
| 400 | InvalidPeerAsn.Malformed | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotFound | instance not found | 实例不存在。 |
| 400 | InvalidParams.NotFound | vpc instance not found | 该VPC不存在，请您检查输入的VPC是否正确。 |
| 400 | InvalidParams.AlreadyExists | bgp network already exists | BGP网络已经存在。 |
| 400 | InvalidStatus.CannotOperate | invalid status cannot operate | 状态不合法，无法执行该操作。 |

#### 6.7.9. AddBgpNetwork

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

高速通道

| Action | String | 是 | AddBgpNetwork | 要执行的操作。 取值： AddBgpNetwork。 |
|---|---|---|---|---|
| DstCidrBlock | String | 是 | 10.10.XX.XX/32 | 需要和本地IDC互连的VPC或交换机的网段，即要宣告的IP地址。 您可以宣告IPv4地址，也可以宣告IPv6地址。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VBR所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterId | String | 是 | vbr-m5eadkqe6budw4sj0**** | 宣告的BGP网段所在的VBR ID。 |
| IpVersion | String | 否 | ipv4 | 宣告的IP地址的版本。取值： ipv4：宣告的IPv4地址。 ipv6：宣告的IPv6地址。 |
| VpcId | String | 否 | vpc-bp1qpo0kug3a2**** | VPC的ID。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 9C7FA9D6-72E0-48A9-A9C3- 2DA8569CD5EB | 请求ID。 |

**示例**

请求示例

```
&DstCidrBlock=10.10.XX.XX/32 &RegionId=cn-qingdao-env66-d01 &RouterId= vbr-m5eadkqe6budw4sj0****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <AddBgpNetworkResponse> <RequestId>9C7FA9D6-72E0-48A9-A9C3-2DA8569CD5EB</RequestId> </AddBgpNetworkResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "9C7FA9D6-72E0-48A9-A9C3-2DA8569CD5EB" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | NQA数超过VBR配额。 |
| 400 | QuotaExceeded.BgpNetwork | bgp network count per vbr quota exceed. | 边界路由器的BGP网络数量已达到配额。 |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | 多物理专线的IP地址不能为空。 |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidBgpGroup | bgp group not exists | 该BGP组不存在。 |
| 400 | InvalidBgpName.Malformed | Specified Bgp Group name is not valid. | 该BGP组的名称不合法。 |
| 400 | InvalidBgpDiscription.Malformed | Specified Bgp Group description is not valid. | 该BGP组的描述不合法。 |
| 400 | InvalidBgpAuthkey.Malformed | Specified Bgp Group authkey is not valid. | 该BGP组的验证密钥不合法。 |
| 400 | InvalidIP.Malformed | Ip malformed. | IP格式不合法。 |

高速通道

| 400 | InvalidPeerAsn.Malformed | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
|---|---|---|---|
| 400 | InvalidParams.NotNull | parameter must not null. | 参数不能为空。 |
| 400 | InvalidParams.NotFound | instance not found | 实例不存在。 |
| 400 | InvalidParams.NotFound | vpc instance not found | 该VPC不存在，请您检查输入的VPC是否正确。 |
| 400 | InvalidParams.AlreadyExists | bgp network already exists | BGP网络已经存在。 |
| 400 | InvalidStatus.CannotOperate | invalid status cannot operate | 状态不合法，无法执行该操作。 |
| 404 | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. | 指定的RegionId不存在。 |
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |

#### 6.7.10. DescribeBgpNetworks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBgpNetworks | 要执行的操作。 取值： DescribeBgpNetworks。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要查询的已宣告BGP网段所在VBR的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| IpVersion | String | 否 | ipv4 | IP版本。 |
| RouterId | String | 否 | vbr-m5eadkqe6budw4sj0**** | 要查询的已宣告BGP网段所在VBR ID。 |
| PageNumber | Integer | 否 | 1 | 列表的页码。默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数。最大值：50。默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BgpNetworks | Array of BgpNetwork |  | 查询的已宣告BGP网段详细信息。 |
| BgpNetwork |  |  |  |
| DstCidrBlock | String | 10.10.XX.XX/32 | 已宣告的BGP网段。 |
| RouterId | String | vbr-m5eadkqe6budw4sj**** | 已宣告的BGP网段所在VBR ID。 |
| Status | String | Available | 已宣告的BGP网段的状态。 |
| VpcId | String | vpc-bp1qpo0kug3a**** | VPC的ID。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| PageSize | Integer | 10 | 分页查询时每页的行数。 |
| RequestId | String | 6F513A15-669F-419D-B511- 08A85292059B | 请求ID。 |
| TotalCount | Integer | 1 | 已宣告的BGP网段的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeBgpNetworks &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式高速通道

```xml
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>6F513A15-669F-419D-B511-08A85292059B</RequestId>
  <PageNumber>1</PageNumber>
  <BgpNetworks>
        <Status>Available</Status>
        <DstCidrBlock>10.10.XX.XX/32</DstCidrBlock>
        <VpcId>vpc-bp1qpo0kug3a****</VpcId>
        <RouterId>vbr-m5eadkqe6budw4sj****</RouterId>
  </BgpNetworks>
```

| JSON | 格式 |
|---|---|
| { "TotalCount": 1, "PageSize": 10, "RequestId": "6F513A15-669F-419D-B511-08A85292059B", "PageNumber": 1, "BgpNetworks": { "Status": "Available", "DstCidrBlock": "10.10.XX.XX/32", "VpcId": "vpc-bp1qpo0kug3a****", "RouterId": "vbr-m5eadkqe6budw4sj****" } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 请求处理由于某些未知错误失败。 |
| 404 | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. | 指定的RegionId不存在。 |

#### 6.7.11. DeleteBgpNetwork

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteBgpNetwork | 要执行的操作。 取值： DeleteBgpNetwork。 |
| DstCidrBlock | String | 是 | 10.10.XX.XX/32 | 需要和IDC互联的VPC或交换机的网段。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VBR所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterId | String | 是 | vbr-m5eadkqe6budw4sj0**** | 要删除的BGP网段所在的VBR ID。 |
| IpVersion | String | 否 | ipv4 | IP版本。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 22F4C006-D3BB-4F96-9FF9- 4C8335276D70 | 请求ID。 |

**示例**

请求示例高速通道

```
&DstCidrBlock=10.10.XX.XX/32 &RegionId=cn-qingdao-env66-d01 &RouterId= vbr-m5eadkqe6budw4sj0****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteBgpNetworkResponse> <RequestId>22F4C006-D3BB-4F96-9FF9-4C8335276D70</RequestId> </DeleteBgpNetworkResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "22F4C006-D3BB-4F96-9FF9-4C8335276D70" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | Specified value of "regionId" is not supported. | 指定的 RegionId 不存在，请您检查此产品在该地域是否可用。 |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | 边界路由器的BGP组的数量已达到配额。 |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | NQA数超过VBR配额。 |
| 400 | QuotaExceeded.BgpNetwork | bgp network count per vbr quota exceed. | 边界路由器的BGP网络数量已达到配额。 |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | 多物理专线的IP地址不能为空。 |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | 该边界路由器不存在，请您检查输入的边界路由器是否正确。 |
| 400 | InvalidBgpGroup | bgp group not exists | 该BGP组不存在。 |
| 400 | InvalidBgpName.Malformed | Specified Bgp Group name is not valid. | 该BGP组的名称不合法。 |
| 400 | InvalidBgpDiscription.Malformed | Specified Bgp Group description is not valid. | 该BGP组的描述不合法。 |
| 400 | InvalidBgpAuthkey.Malformed | Specified Bgp Group authkey is not valid. | 该BGP组的验证密钥不合法。 |
| 400 | InvalidIP.Malformed | Ip malformed. | IP格式不合法。 |
| 400 | InvalidPeerAsn.Malformed | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | ASN号码不能和阿里云ASN号码一致。 |
| 400 | InvalidParams.NotFound | instance not found | 实例不存在。 |
| 400 | InvalidParams.NotFound | vpc instance not found | 该VPC不存在，请您检查输入的VPC是否正确。 |
| 400 | InvalidParams.AlreadyExists | bgp network already exists | BGP网络已经存在。 |
| 400 | InvalidStatus.CannotOperate | invalid status cannot operate | 状态不合法，无法执行该操作。 |

### 路由器接口

#### 6.8.1. CreateRouterInterface

**使用说明**

同一路由表下的路由条目的目标网段（DestinationCidrBlock）不允许相同。 边界路由器VBR（Virtual Border Router）只能是连接发起端，并且是已激活状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateRouterInterface | 要执行的操作。 取值：CreateRouterInterface。 |
| OppositeRegionId | String | 是 | cn-qingdao-env66-d01 | 连接接收端所在的地域ID。 |

高速通道

| RegionId | String | 是 | cn-qingdao-env33-d01 | 路由器接口所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
|---|---|---|---|---|
| Role | String | 是 | InitiatingSide | 路由器接口的角色。取值： InitiatingSide：连接发起端。 AcceptingSide：连接接收端。 |
| RouterId | String | 是 | vrt-n3619981j2qdfyhfc**** | 路由器接口关联的路由器ID。 |
| RouterType | String | 是 | VRouter | 路由器接口关联的路由器类型。取值： VRouter：VPC路由器。 VBR：边界路由器。 |
| Spec | String | 是 | Mini.2 | 路由器接口的规格。可用的规格和对应的带宽，取值： Mini.2：2 Mbps Mini.5：5 Mbps Small.1：10 Mbps Small.2：20 Mbps Small.5：50 Mbps Middle.1：100 Mbps Middle.2：200 Mbps Middle.5：500 Mbps Large.1：1000 Mbps Large.2：2000 Mbps Large.5：5000 Mbps Xlarge.1：10000 Mbps 说明当Role为AcceptingSide（连接接收端） 时，Spec取值为Negative。 |
| OppositeInterfaceId | String | 否 | ri-2zeo3xzyf38r4urzd**** | 对端路由器接口ID。 |
| OppositeRouterId | String | 否 | vrt-bp1lhl0taikrteen8**** | 对端的路由器的ID。 |
| OppositeRouterType | String | 否 | VRouter | 对端路由器接口关联的路由器类型。取值： VRouter：VPC路由器。 VBR：边界路由器。 |
| OppositeInterfaceOwnerId | String | 否 | 2348**** | 对端路由器接口的所有者ID。 |
| HealthCheckSourceIp | String | 否 | 116.62.XX.XX | 健康检查源IP地址，必须是本端VPC内的一个未被使用的IP。 说明物理专线接入场景下可指定该参数。 |
| HealthCheckTargetIp | String | 否 | 116.12.XX.XX | 健康检查目的IP地址。 说明当指定了HealthCheckSourceIp后，该参数为必选。 |
| AccessPointId | String | 否 | ap-cn-sha**** | VBR所属的接入点ID。 您可以通过调用 DescribeAccessPoints 接口获取物理专线接入点ID。 说明物理专线接入场景下需指定该参数。 |
| OppositeAccessPointId | String | 否 | ap-cn-sha**** | 对端所属的接入点ID。 说明对端路由器接口位于VBR上时需指定该参数，创建路由器接口后无法修改。 |
| Description | String | 否 | 路由器接口描述。 | 路由器接口的描述信息。 长度为2~255个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| Name | String | 否 | 接口名称 | 路由器接口的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-）。 |

高速通道

| Period | Integer | 否 | 3 | 购买时长。取值： 当选择按月付费时，取值范围为1~9。 当选择按年付费时，取值范围为1~3。 说明 InstanceChargeType参数的值为PrePaid时， 该参数必选。 |
|---|---|---|---|---|
| InstanceChargeType | String | 否 | PrePaid | 路由器接口的付费方式。取值： PrePaid：预付费。 PostPaid（默认值）：后付费。 |
| AutoPay | Boolean | 否 | false | 是否自动付费。取值： false：不开启自动付费，生成订单后需要到订单中心完成支付。 true：开启自动付费，自动支付订单。 说明 InstanceChargeType参数的值为PrePaid时， 该参数必选。 |
| PricingCycle | String | 否 | Month | 预付费的计费周期，取值： Month（默认值）：按月付费。 Year：按年付费。 说明 InstanceChargeType参数的值为PrePaid时，该参数必选。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| OrderId | Long | 202008594930117 | 订单号，选择预付费时返回该参数。 |
| RequestId | String | 079874CD-AEC1-43E6-AC03- ADD96B6E4907 | 请求ID。 |
| RouterInterfaceId | String | ri-2ze7fbuohm**** | 路由器接口的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateRouterInterface &OppositeRegionId=cn-qingdao-env66-d01 &RegionId=cn-qingdao-env33-d01 &Role=InitiatingSide &RouterId=vrt-123**** &RouterType=VRouter &Spec=Mini.2
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateRouterInterfaceResponse> <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId> <OrderId>202008594930117</OrderId> <RouterInterfaceId>ri-2ze7fbuohm****</RouterInterfaceId> </CreateRouterInterfaceResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907", "OrderId": 202008594930117, "RouterInterfaceId": "ri-2ze7fbuohm****" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

高速通道

| 404 | InvalidRegionId.NotFound | The regionId provided does not exist in our records. | 指定的RegionId不存在。请检查该参数是否正确。 |
|---|---|---|---|
| 400 | InvalidRole.ValueNotSupported | The specified Role is not valid. | 指定的 Role 不合法，请您检查该参数是否正确。 |
| 400 | InvalidSpec.ValudNotSupported | The specified Spec is not supported. | 该规格不支持该操作，请您更换规格后重试。 |
| 400 | InvalidRouterType.ValueNotSupp orted | The specified RouterType is not valid. | 该路由器类型不合法。 |
| 404 | InvalidRouterId.NotFound | The specified RouterId does not exist in our recored. | 该 RouterId 不存在。 |
| 400 | InvalidName.Malformed | The specified "Name" is not valid. | 该名称格式不合法。 |
| 400 | InvalidDescription.Malformed | The specifid "Description" is not valid. | 指定的资源描述格式不合法。长度为2-256个字符，不能以 http:// 和 https:// 开头。 |
| 400 | Forbidden.BillsOutstanding | You cannot create more RouterInterface because you have bills outstanding. | 无法创建路由器接口，您有未结算的账单。 |
| 400 | LimitationExceed.InterfaceNumbe rOnRouter | Total number of RouterInterfaces on a Router exceeded. | 路由器接口数量已达到配额上限。 |
| 400 | Forbidden.NotInRouterInterfaceCr eateWhitelist | Not in router interface create whitelist. | 不在路由器接口的白名单中。 |
| 400 | RICREATEONELIMITBYSYNC _ _ _ _ _ | Create ri only one limit by sync. | 限制同步创建路由器接口。 |
| 400 | InvalidAccessPoint.ValueNotAllow ed | The non-vbr router interface cannot have access point configured. | 非边界路由器的路由器接口不能配置接入点。 |
| 400 | InvalidAccessPoint.ValueNotAllow ed | The non-vbr opposite router interface cannot have opposite access point configured. | 非边界路由器的路由器接口不能配置接入点。 |
| 400 | InvalidAccessPoint.NotMatch | The accessPoint id is not matched | 该接入点ID不正确。 |
| 400 | InvalidAccessPoint.NotExist | The accessPoint not exit | 该接入点不存在。 |
| 400 | InvalidRouterType.ValueNotSupp orted | The specified RouterType is not valid | 该路由器类型不合法。 |

#### 6.8.2. ConnectRouterInterface

调用ConnectRouterInterface接口由发起端路由器接口向接收端发起连接。

**使用说明**

调用本接口后路由器接口进入**Connecting**状态，连接完成后进入**Active**状态。 调用该接口创建VPC时，请注意以下事项：

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ConnectRouterInterface | 要执行的操作。 取值： ConnectRouterInterface。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 路由器接口所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterInterfaceId | String | 是 | ri-2zeo3xzyf38r4urzd**** | 发起端路由器接口的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | DE77A7F3-3B74-41C0-A5BC- CAFD188C28B6 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConnectRouterInterface &RegionId= cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urzd****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ConnectRouterInterfaceResponse> <RequestId>DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6</RequestId> </ConnectRouterInterfaceResponse> |  |

高速通道

| JSON | 格式 |
|---|---|
| {"RequestId":"DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6"} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRouterInterfaceId.NotFoun d | The specified RouterInterfaceId does not exist in our record. | 指定的路由器接口不存在，请您检查填写的路由器接口是否正确。 |
| 400 | IncorrectRole.NotInitiatingSide | The specified RouterInterface is not InitiatingSide. | 该路由器接口不是发起端，请选择发起端的路由器接口进行发起连接。 |
| 400 | IncorrectOppositeInterfaceInfo | Cannot connect on the same router | 不允许连接相同的路由器。 |
| 400 | Forbidden.OnlyOneConnection | The Specified routers have a connection already | 该路由器已有路由器接口连接。 |
| 400 | Forbidden.OnlyOneConnection | Cannot connect concurrently between same routers | 不能在同一路由器上发起连接。 |
| 400 | Forbidden.BillsOutstanding | You cannot use this action because you have bills outstanding. | 无法执行该操作，您有未结算的账单。 |
| 404 | CROSSBID.FORBIDDEN _ | Connect RouterInterface across bid is illegal | 跨BID连接非法。 |

#### 6.8.3. DeactivateRouterInterface

**使用说明**

调用本接口后路由器接口进入**Deactivating**状态，冻结完成后进入**Inactive**状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeactivateRouterInterface | 要执行的操作。 取值： DeactivateRouterInterface。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 路由器接口所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterInterfaceId | String | 是 | ri-2zeo3xzyf38r4urz**** | 路由器接口的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | BE7EB53A-99AB-4DA8-AEDE- 75FA90D046A6 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeactivateRouterInterface &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ActivateRouterInterfaceResponse> <RequestId>BE7EB53A-99AB-4DA8-AEDE-75FA90D046A6</RequestId> </ActivateRouterInterfaceResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "BE7EB53A-99AB-4DA8-AEDE-75FA90D046A6" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRouterInterfaceId.NotFoun d | The specified RouterInterfaceId does not exist in our record. | 指定的路由器接口不存在，请您检查填写的路由器接口是否正确。 |
| 400 | IncorrectStatus | RouterInterface can be operated by this action only when it's status is Active. | 只有当路由器接口的状态为Active时，才可执行该操作。 |

高速通道

#### 6.8.4. ModifyRouterInterfaceSpec

**使用说明**

调用本接口后，路由器接口进入**Activating**（激活中）状态，激活成功后进入**Active**（已激活）状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyRouterInterfaceSpec | 要执行的操作。 取值： ModifyRouterInterfaceSpec。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 路由器接口所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterInterfaceId | String | 是 | ri-2zeo3xzyf38r4urzd**** | 路由器接口的ID。 |
| Spec | String | 是 | Mini.2 | 路由器接口的规格。可用的规格和对应的带宽： Mini.2：2 Mbps Mini.5：5 Mbps Small.1：10 Mbps Small.2：20 Mbps Small.5：50 Mbps Middle.1：100 Mbps Middle.2：200 Mbps Middle.5：500 Mbps Large.1：1000 Mbps Large.2：2000 Mbps Large.5：5000 Mbps Xlarge.1：10000 Mbps 说明当Role为AcceptingSide（连接接收端） 时，Spec取值为Negative。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |
| Spec | String | Mini.2 | 路由器接口的规格。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyRouterInterfaceSpec &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urzd**** &Spec=Mini.2
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyRouterInterfaceSpecResponse> <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId> <Spec>Mini.2</Spec> </ModifyRouterInterfaceSpecResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF", "Spec": "Mini.2" } |  |

高速通道

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidSpec.ValudNotSupported | The specified Spec is not supported. | 该规格不支持该操作，请您更换规格后重试。 |
| 404 | InvalidRouterInterfaceId.NotFoun d | The specified RouterInterfaceId does not exist in our record. | 指定的路由器接口不存在，请您检查填写的路由器接口是否正确。 |
| 400 | InvalidInstanceOwner.Error | The router instance owener error. | 路由器不属于您的账号。 |
| 400 | InvalidInstance.StatusError | The router instance owener error. | 实例状态错误 |
| 400 | InvalidOpposite.NotFound | The opposite not exit. | 对端不存在。 |

#### 6.8.5. DeleteRouterInterface

**使用说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteRouterInterface | 要执行的操作。 取值： DeleteRouterInterface。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 路由器接口所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterInterfaceId | String | 是 | ri-2zeo3xzyf38r4urz**** | 路由器接口的ID。 |
| ClientToken | String | 否 | 123e4567-e89b-12d3-a456- 426655440000 | 客户端Token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteRouterInterface &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteRouterInterfaceResponse> <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId> </DeleteRouterInterfaceResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IncorrectStatus | This openeration would be allowed only when status of this RouterInterface is Idle/Inactive. | 无法执行该操作。只有当路由器接口的状态是Idle/Inactive 时，才可以操作。 |

高速通道

| 400 | DependencyViolation.RouterInterf aceReferedByRouteEntry | RouterInterface cannot be deleted when it is refered by a route table entry as next hop. | 路由器接口被某个路由条目引用（将当做下一跳目标）时， 不能删除，请先删除指向该路由器接口的路由条目后再进行删除。 |
|---|---|---|---|
| 404 | InvalidInstanceId.NotFound | The InstanceId provided does not exist in our records. | 该 ECS 实例不存在（实例不在该 VPC 下）。 |
| 400 | InvalidRouterInterfaceChargeTyp e.Malformed | The prepaid routerinterface can not delete. | 无法删除预付费路由器接口。 |

#### 6.8.6. DescribeRouterInterfaces

调用DescribeRouterInterfaces接口查询指定地域内的路由器接口。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRouterInterfaces | 要执行的操作。 取值：DescribeRouterInterfaces。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 路由器接口所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| IncludeReservationData | Boolean | 否 | false | 是否包含续费数据，取值。 true：是。 false（默认值）：否。 |
| PageNumber | Integer | 否 | 1 | 列表的页码。默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数。最大值：50。默认值：10。 |
| Filter.N.Key | String | 否 | status | 过滤条件，最多可提供5个过滤条件。支持以下过滤条件： RouterInterfaceId：路由器接口ID。 RouterId：路由器ID。 RouterType：路由器类型，取值：VRouter或VBR。 RouterInterfaceOwnerId：路由器接口的所属账号ID。 OppositeInterfaceId：对端路由器接口ID。 OppositeRouterType：对端路由器接口类型，取值：VRouter或VBR。 OppositeRouterId：对端路由器接口ID。 OppositeInterfaceOwnerId：对端路由器接口所属账号ID。 Status：路由器接口状态。 Name：路由器接口名称。 说明每个过滤条件的多个值之间为或关系，即只要与其中一个值吻合则视为符合该过滤条件。各个过滤条件之间为与关系， 即符合所有指定的过滤条件，才会进入最终的查询结果。 |
| Filter.N.Value.N | RepeatList | 否 | Active | 根据Key指定过滤值。一个Key支持指定多个过滤值，每个过滤值之间是或的关系，即只要符合其中一个过滤值，则视为匹配该过滤条件。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TotalCount | Integer | 2 | 列表条目数。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| PageSize | Integer | 10 | 分页查询时每页的行数。 |
| RequestId | String | C7F6FCBD-F9CC-4501-8EF3- CDC9577CAE45 | 请求ID。 |
| RouterInterfaceSet | Array of RouterInterfaceType |  | 路由器接口的详细信息。 |
| RouterInterfaceType |  |  |  |
| AccessPointId | String | ap-cn-shanghaiSZ-**** | 接入点ID。 |
| Bandwidth | Integer | 10 | 路由器接口的带宽。单位：Mbps。 |

高速通道

| BusinessStatus | String | Normal | 路由器接口的业务状态。 Normal：正常。 FinancialLocked：欠费锁定。 SecurityLocked：安全风控锁定。 |
|---|---|---|---|
| ChargeType | String | PayByTraffic | 付费方式。 |
| ConnectedTime | String | 2021-06-08T12:20:55 | 连接建立的时间。 |
| CreationTime | String | 2021-06-08T12:20:55 | 路由表的创建时间。 |
| CrossBorder | Boolean | false | 是否是跨境连接。 |
| Description | String | 路由表接口描述。 | 路由表接口描述。 |
| EndTime | String | 2021-06-08T12:20:55 | 获取数据的结束时间点。 |
| HasReservationData | String | false | 是否有续费数据。 |
| HcRate | Integer | 1 | 健康检查速率。 |
| HcThreshold | Integer | 2 | 健康检查阈值。 |
| HealthCheckSourceIp | String | 116.62.XX.XX | 健康检查源IP。 |
| HealthCheckTargetIp | String | 116.62.XX.XX | 健康检查目标IP。 |
| Ipv6Status | String | on | 是否开启IPv6安全防护，取值： on：开启。 off：关闭。 unsupport：不支持。 |
| Name | String | test | 自定义名称。 |
| OppositeAccessPointId | String | ap-cn-shanghaiSZ-**** | 对端接入点ID。 |
| OppositeBandwidth | Integer | 12 | 对端带宽。单位：Mbps。 |
| OppositeInterfaceBusines sStatus | String | Normal | 连接对端的路由器接口的业务状态。 |
| OppositeInterfaceId | String | ri-bp1itx13bwe6f2wfh**** | 对端路由器接口ID。 |
| OppositeInterfaceOwnerId | String | 123157908552**** | 对端路由器接口所属的账号ID。 |
| OppositeInterfaceSpec | String | Large | 连接对端路由器接口的规格。 |
| OppositeInterfaceStatus | String | Normal | 连接对端的路由器接口的状态。 |
| OppositeRegionId | String | cn-qingdao-env66-d01 | 连接对端所在的地域ID。 |
| OppositeRouterId | String | vrt-bp1d3bxtdv68tfd7g**** | 连接对端的路由器接口所属的路由器ID。 |
| OppositeRouterType | String | VRouter | 连接对端的路由器接口所属的路由器类型。 |
| OppositeVpcInstanceId | String | vpc-bp1qpo0kug3a20qqe**** | 对端的VPC ID。 |
| ReservationActiveTime | String | 2021-08-11T16:00:00Z | 续费生效时间。 |
| ReservationBandwidth | String | 10 | 续费带宽。单位：Mbps。 |
| ReservationInternetCharg eType | String | PayByBandwidth | 续费付费类型。 |
| ReservationOrderType | String | RENEWCHANGE | 续费订单类型。 |

高速通道

| Role | String | InitiatingSide | 对等连接中的角色。 |
|---|---|---|---|
| RouterId | String | vrt-bp1d3bxtdv68tfd7g**** | 路由条目所在路由器的ID。 |
| RouterInterfaceId | String | ri-2zenfgfpyu3v93koa**** | 路由器接口ID。 |
| RouterType | String | VRouter | 路由表所在路由器的类型。取值； VRouter：VPC路由器。 VBR：边界路由器。 |
| Spec | String | Large | 路由器接口的规格。 |
| Status | String | active | 路由器接口的状态。 |
| VpcInstanceId | String | vpc-2ze3tq4uxhysg717x**** | 对等连接中本端VPC的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRouterInterfaces &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeRouterInterfacesResponse> <TotalCount>2</TotalCount> <PageSize>10</PageSize> <RequestId>C7F6FCBD-F9CC-4501-8EF3-CDC9577CAE45</RequestId> <PageNumber>1</PageNumber> <RouterInterfaceSet> <OppositeInterfaceStatus>Normal</OppositeInterfaceStatus> <OppositeInterfaceId>ri-bp1itx13bwe6f2wfh****</OppositeInterfaceId> <OppositeRouterId>vrt-bp1d3bxtdv68tfd7g****</OppositeRouterId> <Description>路由表接口描述。</Description> <EndTime>2021-06-08T12:20:55</EndTime> <RouterId>vrt-bp1d3bxtdv68tfd7g****</RouterId> <BusinessStatus>Normal</BusinessStatus> <Name>test</Name> <ReservationOrderType>RENEWCHANGE</ReservationOrderType> <OppositeRouterType>VRouter</OppositeRouterType> <OppositeBandwidth>12</OppositeBandwidth> <Bandwidth>10</Bandwidth> <ConnectedTime>2021-06-08T12:20:55</ConnectedTime> <ReservationActiveTime>2021-08-11T16:00:00Z</ReservationActiveTime> <HcThreshold>2</HcThreshold> <ReservationBandwidth>10</ReservationBandwidth> <Status>active</Status> <OppositeInterfaceOwnerId>123157908552****</OppositeInterfaceOwnerId> <OppositeRegionId>cn-qingdao-env66-d01</OppositeRegionId> <HealthCheckSourceIp>116.62.XX.XX</HealthCheckSourceIp> <HasReservationData>false</HasReservationData> <CrossBorder>false</CrossBorder> <HcRate>1</HcRate> <ReservationInternetChargeType>PayByBandwidth</ReservationInternetChargeType> <OppositeInterfaceSpec>Large</OppositeInterfaceSpec> <Role>InitiatingSide</Role> <OppositeVpcInstanceId>vpc-bp1qpo0kug3a20qqe****</OppositeVpcInstanceId> <RouterType>VRouter</RouterType> <Ipv6Status>on</Ipv6Status> <ChargeType>PayByTraffic</ChargeType> <AccessPointId>ap-cn-shanghaiSZ-****</AccessPointId> <CreationTime>2021-06-08T12:20:55</CreationTime> <VpcInstanceId>vpc-2ze3tq4uxhysg717x****</VpcInstanceId> <OppositeInterfaceBusinessStatus>Normal</OppositeInterfaceBusinessStatus> <OppositeAccessPointId>ap-cn-shanghaiSZ-****</OppositeAccessPointId> <Spec>Large</Spec> <HealthCheckTargetIp>116.62.XX.XX</HealthCheckTargetIp> <RouterInterfaceId>ri-2zenfgfpyu3v93koa****</RouterInterfaceId> </RouterInterfaceSet> </DescribeRouterInterfacesResponse> |  |

`JSON` 格式高速通道

```json
{
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "C7F6FCBD-F9CC-4501-8EF3-CDC9577CAE45",
    "PageNumber": 1,
    "RouterInterfaceSet": {
        "OppositeInterfaceStatus": "Normal",
        "OppositeInterfaceId": "ri-bp1itx13bwe6f2wfh****",
        "OppositeRouterId": "vrt-bp1d3bxtdv68tfd7g****",
```

`"Description": "`路由表接口描述。`",`

```json
        "EndTime": "2021-06-08T12:20:55",
        "RouterId": "vrt-bp1d3bxtdv68tfd7g****",
        "BusinessStatus": "Normal",
        "Name": "test",
        "ReservationOrderType": "RENEWCHANGE",
        "OppositeRouterType": "VRouter",
        "OppositeBandwidth": 12,
        "Bandwidth": 10,
        "ConnectedTime": "2021-06-08T12:20:55",
        "ReservationActiveTime": "2021-08-11T16:00:00Z",
        "HcThreshold": 2,
        "ReservationBandwidth": 10,
        "Status": "active",
        "OppositeInterfaceOwnerId": "123157908552****",
        "OppositeRegionId": "cn-qingdao-env66-d01",
        "HealthCheckSourceIp": "116.62.XX.XX",
        "HasReservationData": false,
        "CrossBorder": false,
        "HcRate": 1,
        "ReservationInternetChargeType": "PayByBandwidth",
        "OppositeInterfaceSpec": "Large",
        "Role": "InitiatingSide",
        "OppositeVpcInstanceId": "vpc-bp1qpo0kug3a20qqe****",
        "RouterType": "VRouter",
        "Ipv6Status": "on",
        "ChargeType": "PayByTraffic",
        "AccessPointId": "ap-cn-shanghaiSZ-****",
        "CreationTime": "2021-06-08T12:20:55",
        "VpcInstanceId": "vpc-2ze3tq4uxhysg717x****",
        "OppositeInterfaceBusinessStatus": "Normal",
        "OppositeAccessPointId": "ap-cn-shanghaiSZ-****",
        "Spec": "Large",
        "HealthCheckTargetIp": "116.62.XX.XX",
        "RouterInterfaceId": "ri-2zenfgfpyu3v93koa****"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidFilterKey.ValueNotSupport ed | Specified filter key is not supported: Filter.X.key | 该过滤器的Key不支持：Filter.X.key。 |
| 400 | InvalidParam.NotNull | The parameter must not be null. | 参数不能为空。 |

#### 6.8.7. ActivateRouterInterface

调用ActivateRouterInterface接口激活处于Inactive状态的路由器接口。

**使用说明**

调用本接口后，路由器接口进入**Activating**状态，激活成功后进入**Active**状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ActivateRouterInterface | 要执行的操作。 取值： ActivateRouterInterface。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 路由器接口所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterInterfaceId | String | 是 | ri-2zeo3xzyf38r4urz**** | 路由器接口的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6-AC03- ADD96B6E4907 | 请求ID。 |

高速通道

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ActivateRouterInterface &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ActivateRouterInterfaceResponse> <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId> </ActivateRouterInterfaceResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. | 指定的RegionId不存在。 |
| 404 | InvalidRouterInterfaceId.NotFoun d | The specified RouterInterfaceId does not exist in our records. | 指定的路由器接口不存在，请您检查填写的路由器接口是否正确。 |
| 400 | IncorrectStatus | RouterInterface can be operated by this action only when it's status is Inactive. | 只有当路由器接口的状态为Inactive时，才可执行该操作。 |
| 400 | Forbbiden | The Router instance owener error | 该路由器不属于您的账号。 |

#### 6.8.8. ModifyRouterInterfaceAttribute

调用ModifyRouterInterfaceAttribute接口修改路由器接口的配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyRouterInterfaceAttribu te | 要执行的操作。 取值：ModifyRouterInterfaceAttribute。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 路由器接口所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouterInterfaceId | String | 是 | ri-2zeo3xzyf38r4urz**** | 路由器接口ID。 |
| Name | String | 否 | test | 路由器接口的名称。 长度为2～128个字符，必须以字母或中文开头，可包含数字、下划线 （_）和短划线（-）。 |
| Description | String | 否 | 路由器接口 | 路由器接口的描述信息。 长度为2～255个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| OppositeInterfaceId | String | 否 | ri-2zeo3xzyf38r4urz**** | 对端路由器接口ID。 |
| OppositeRouterId | String | 否 | vrt-bp1jcg5cmxjbl9xgc**** | 对端路由器ID。 |
| OppositeRouterType | String | 否 | VRouter | 要连接的对端路由器接口所属的路由器类型。取值： VRouter VBR（默认值） |
| OppositeInterfaceOwnerId | Long | 否 | 10 | 对端路由器接口的所有者的账号ID。 |
| HealthCheckSourceIp | String | 否 | 116.62.XX.XX | 健康检查源IP地址，必须是本端VPC内的一个未被使用的IP。 说明物理专线接入场景下可指定该参数。 |

高速通道

| HealthCheckTargetIp | String | 否 | 116.62.XX.XX | 健康检查目的IP地址。 说明当指定了HealthCheckSourceIp后，该参数为必选。 |
|---|---|---|---|---|
| HcThreshold | Integer | 否 | 12 | 健康检查阈值。 |
| HcRate | Integer | 否 | 2 | 健康检查速率。 |
| DeleteHealthCheckIp | Boolean | 否 | true | 是否删除该路由器接口上配置的健康检查IP。取值： true：删除健康检查IP。 false（默认值）：不删除健康检查IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyRouterInterfaceAttribute &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyRouterInterfaceAttributeResponse> <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId> </ModifyRouterInterfaceAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. | 指定的RegionId不存在。 |
| 404 | InvalidRouterInterfaceId.NotFoun d | The specified RouterInterfaceId does not exist in our records. | 指定的路由器接口不存在，请您检查填写的路由器接口是否正确。 |
| 400 | Forbidden.FinancileLocked | This RouterInterface is financiel locked because of bills outstanding. | 该路由器接口已欠费锁定，因为您有未结算的账单。 |
| 400 | InvalidName.Malformd | The attribute name is illeagl. | 该名称格式不合法。 |
| 400 | InvalidOppositeRouterType.Value NotSupported | The specified OppositeRouterType is not valid. | 参数OppositeRouterType的值不合法。 |
| 400 | InvalidDescription.Malformed | The Description is illeagl. | 指定的资源描述格式不合法。长度为2～256个字符，不能以http://和https://开头。 |
| 400 | Forbbiden | The Router instance owener error | 该路由器不属于您的账号。 |
| 400 | LinkRole.NotSupport | This linkrole is not supported | 这个链接不支持。 |
| 400 | InvalidParam.ModifyRouterInterfa ce | Modify routerinterface param invalide | 编辑路由器接口参数不合法。 |

高速通道

## 附录

### STS概要

#### 7.1.1. 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

**使用RAM用户扮演角色时获取STS Token**

有权限的RAM用户可以使用其访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用STS Token访问阿里云资源。

**产品优势**

使用STS Token，减少长期访问密钥（Accesskey）泄露的风险。 STS Token具有时效性，可以自定义有效期，到期后将自动失效，无需定期轮换。 可以为STS Token绑定自定义权限策略，提供更加灵活和精细的云资源授权。

#### 7.1.2. AssumeRole

RAM用户调用AssumeRole接口获取一个扮演RAM角色的临时身份凭证STS Token。该接口中RAM用户扮演的是可信实体为阿里云账号类型的RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssumeRole | 要执行的操作。取值：AssumeRole |
| RoleArn | String | 是 | acs:ram::123456789012****:r ole/adminrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM角色。 |
| RoleSessionName | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、半角句号（.）、 at（@）、短划线（-）和下划线（_）。 |
| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。 具体如下： 如果指定该权限策略，则STS Token最终的权限策略取RAM角色权限策略与该权限策略的交集。 如果不指定该权限策略，则STS Token最终的权限策略取RAM角色的权限策略。 长度为1~1024个字符。 |

**返回结果**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71-4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | 无 | 无 | 访问凭证。 |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5U1**** | 访问密钥ID。 |
| AccessKeySecret | String | ***************************************** | 访问密钥。 |
| SecurityToken | String | ******** | 安全令牌。 |
| Expiration | String | 2015-04-09T11:52:19Z | 失效时间。 |
| AssumedRoleUser | 无 | 无 | 角色扮演时的临时身份。 |
| Arn | String | acs:ram::123456789012****:role/ adminrole/alice | 临时身份的ARN。 |
| AssumedRoleId | String | 34458433936495****:alice | 临时身份的ID。 |

高速通道

**示例**

**引入Pom依赖**

操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下：

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

| 以下代码示例为通过调用 | Sts::AssumeRole::2015-04-01 | 获取STS AccessKey三元组信息。 |
|---|---|---|
| package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo { public static void main(String[] args) { // 创建DefaultAcsClient实例并初始化。 DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>"); HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true); clientConfig.setProtocolType(ProtocolType.HTTPS); profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); CommonRequest request = new CommonRequest(); // "sts.aliyuns.com"要替换为实际的STS Endpoint，一般格式为sts-vpc.${global:region}.${global:internet-domain} request.setSysDomain("sts.aliyuns.com"); request.setSysProduct("Sts"); request.setSysAction("AssumeRole"); request.setSysVersion("2015-04-01"); request.setSysMethod(MethodType.POST); request.setHttpContentType(FormatType.FORM); // 业务参数，设置本次调用Session的别名，"<yourRoleSessionName>"请替换为实际值 request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>"); // 扮演的Role角色ARN，"<yourRoleArn>"请替换为上一步获取到的实际Ram Role ARN request.putQueryParameter("RoleArn", "<yourRoleArn>"); try { CommonResponse response = client.getCommonResponse(request); String assumeRole = response.getData(); if (StringUtils.isEmpty(assumeRole)) return; JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole); JSONObject credentials = assumeRoleJson.getJSONObject("Credentials"); // 获取到STS三元组 String stsAK = credentials.getString("AccessKeyId"); String stsSK = credentials.getString("AccessKeySecret"); String stsToken = credentials.getString("SecurityToken"); System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + stsToken); } catch (ServerException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } catch (ClientException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } } } |  |  |

**调用示例**

下列代码以调用ECS的 `DescribeZones` 接口为示例。 高速通道

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
```

`// "<yourRegionID>"`替换为真实的`RegionID` `// "<yourStsAccesskey>", "<yourStsAccessKeySecret>"`替换为上面获取到的`STS`三元组中`stsAk`、`stsSk`

```
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccessKey>", "<yourStsAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        request.setSysDomain("ecs.aliyuns.com");
        request.setSysProduct("Ecs");
        request.setSysAction("DescribeZones");
        request.setSysVersion("2014-05-26");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
```

`//"<yourRegionID>"`替换为真实的`RegionId`

```
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
```

`// "<yourStsToken>"`替换为上面获取到的`STS`三元组中`stsToken`

```
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
```

`//` 非必填,资源集`id`

```
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填,组织`id`

```java
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        }
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.RoleArn | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.RoleSessionName | The parameter RoleSessionName is wrongly formed. | RoleSessionName格式错误，支持输入 2~64个字符，请输入至少2个字符，允许输入英文字母、数字、半角句号（.）、 at（@）、短划线（-）和下划线（_）。 |
| 400 | InvalidParameter.DurationSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | DurationSeconds参数设置错误，过期时间最小值为900秒，最大值为MaxSessionDuration设置的时间。 |
| 400 | InvalidParameter.PolicyGrammar | The parameter Policy has not passed grammar check. | 权限策略语法错误。 |
| 400 | InvalidParameter.PolicySize | The size of Policy must be smaller than 1024 bytes. | 权限策略长度超限，最大不超过1024字符。 |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | STS Token没有权限。 |

高速通道

| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
|---|---|---|---|
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
