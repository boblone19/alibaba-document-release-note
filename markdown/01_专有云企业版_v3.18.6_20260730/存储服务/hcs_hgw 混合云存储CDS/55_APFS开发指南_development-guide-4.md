---
title: "混合云存储CDS APFS开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 53
source_pdf: "55_APFS开发指南_development-guide-4.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/hcs_hgw/zh/development-guide-4.pdf"
converter: line-classifier (PyMuPDF)
---

# 混合云存储CDS APFS开发指南

## 使用前须知

使用APFS API实现具体功能前，开发人员需要了解调用APFS API时使用的产品名称和API版本。 当使用APFS的文件系统功能时，请通过POP SDK调用对应API来实现。使用POP SDK调用API时，请设置产品名称为EFS，API版本为2017-06-26。 具体调用流程如下图所示。 获取组织ID 准备工 AccessSecret 查找API开发文档获取产品APFS的endpoint 正式调

## 快速入门

## 快速入门

### API调用流程说明

阿里云专有云支持通过POP网关或ASAPI网关调用专有云API，为了使您拥有与公有云更一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**说明**

历史版本使用ASAPI网关调用专有云API的方式仍然有效。

**流程图**

| 获取RegionID 获取组织ID 获取AccessKey和 AccessSecret 查找API开发文档获取产品APFS的endpoint |  |
|---|---|
| 获取POP SDK并调用API |  |

准备工正式调

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，具体操作，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
获取调用时所需要的RegionID参数。具体操作，请参见获取RegionID和Endpoint信息。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrga nizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListRe sourceGroup章节。

## 快速入门

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式。
5. 获取云产品Endpoint。
关于如何获取Endpoint的更多信息，请参见获取RegionID和Endpoint信息。
6. 获取云产品SDK并调用云产品API。

## 准备工作

## 准备工作

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您描述如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，以验证某个请求发送者的身份。其中 AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式，请 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方式，请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方式，请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。

## 准备工作

**说明**

Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云APFS的API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用云产品API时，三元组缺一不可。。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com> ，请替换为实际的STS Endpoint。

## 准备工作

```
public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。 `// <yourRegionID>`、`<yourAccessKeyID>`和`<yourAccessKeySecret>`请分别替换为您实际的地域`ID`

```xml
、AccessKey ID和AccessKey Secret。
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    String assumeRole = callAssumeRole(client);
    if (StringUtils.isEmpty(assumeRole)) return;
    JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
    JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
```

`//` 获取到`STS`三元组。

```java
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
} private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
```

`// sts.aliyuns.com`请替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}。
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`<yourRoleSessionName>`请您替换为实际值。

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`<yourRoleArn>`请替换为上一步获取到的实际`RAM Role ARN`。

```java
    request.putQueryParameter("RoleArn", "<yourRoleArn>");
    try {
        CommonResponse response = client.getCommonResponse(request);
        return response.getData();
    } catch (ServerException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    } catch (ClientException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    }
    return null;
}
```

3. 通过STS AccessKey三元组调用云产品的接口。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

## 准备工作

### 获取RegionID和Endpoint信息

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**企业**。
3. 在左侧导航栏选择**资源管理** > **地域管理**。
4. 在搜索栏输入组织名称，并单击组织名称，可查看该组织的RegionID信息。

**获取Endpoint**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在**服务注册变量大盘**页面，选择**服务**并输入**efs-yaochi**。
4. 单击**Service Registration**列
图标，单击显示的信息。
5. 在**注册变量**对话框，查看**efs.openapi-pub.endpoint**的值即为APFS文件系统的Endpoint。

### 通过POP网关调用专有云API

通过POP Java SDK访问产品域名，需要了解该产品调用方式（RPC或ROA）。

**前提条件**

## 准备工作

目前专有云推荐使用CommonRequest进行调用，您可以从SDK中心下载V1.0版本的SDK。

**CommonRequest调用示例**

RPC调用，示例接口信息：产品名（EFS）、接口（DescribeFileSystems）、版本（2017-06-26）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`。 `//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值。

```
        profile.addEndpoint("<Endpoint>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
```

`/**` 设置代理(可选`),`替换为代理`IP+Port`

```
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

或

```
        clientConfig.setHttpsProxy("<https://192.168.XX:33XX>");
```

请替换为实际代理`IP+`端口。 `*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`//` 替换为真实的产品域名。

```
        request.setDomain("<Endpoint>");
        request.setSysProduct("EFS");
        request.setVersion("2017-06-26");
        request.setAction("CreateFileSystem");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// 非
```

必填，请替换为您实际的资源集`ID`。

```
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// 必填
```

，请替换为您实际的组织`ID`。

```
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// 必填，调用来
```

源说明。

```
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// 非必填（企业版V3.1
```

`5.0`及之前历史版本必填）,请替换为您实际的地域`ID`。

```
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修
```

改、删除、查询单实例详情时必填）,请替换为您实际的实例`ID`。

```
        /**
```

## 准备工作

当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段。 调用方法如下：

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

**重要**

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL/TLS 证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过以下参数设置：

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

`//` 设置不校验服务端证书

```
clientConfig.setIgnoreSSLCerts(true)
```

## Java SDK调用示例

本文介绍如何获取Java SDK并开始调用。

### 快速开始

本文介绍如何获取Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体根据所用功能获取相应产品的Endpoint。具体操作，请参见获取RegionID和Endpoint信息。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用产品的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17及以

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

### 使用手册

#### 安装Java SDK

本文介绍如何安装及调用Java SDK 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用APFS功能，必须安装阿里云Java SDK核心库，SDK核心库推荐使用4.5.17及以上版本

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Java SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <readTimeout>，请您根据自身服务的能力，配置读取超时时间，单位为毫秒（ms）。 <connectionTimeout>，请您根据自身服务的能力，配置连接超时时间，单位为毫秒 （ms）。 <maxRequestsPerHost>，请您根据自身服务的能力，配置每台服务器的最大请求数，数据类型为INT。 <maxRequests>，请您根据自身服务的能力，配置最大请求数，数据类型为INT。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。 `//` 获取`HttpClientConfig`对象

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

#### 使用CommonRequest进行调用

当您要调用某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在ECS的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。

| 如 | RunInstances | 接口，在发起 | CommonRequest |  |
|---|---|---|---|---|
| request.setSysAction("RunInstances") |  |  |  |  |
|  |  |  |  | 来指定 |

**示例：调用RPC风格的API**

使用APFS的DescribeFileSystems接口获取文件系统信息的示例代码如下：

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP和端口。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`。 `//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值。

```
        profile.addEndpoint("<Endpoint>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
```

`/**` 设置代理(可选`),`替换为代理`IP+Port`

```
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

或

```
        clientConfig.setHttpsProxy("<https://192.168.XX:33XX>");
```

请替换为实际代理`IP+`端口。 `*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`//` 替换为真实的产品域名。

```
        request.setDomain("<Endpoint>");
        request.setSysProduct("EFS");
        request.setVersion("2017-06-26");
        request.setAction("CreateFileSystem");
```

t `tQ` P t

```
("P
```

N b "

```
"1")
```

```
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// 非
```

必填，请替换为您实际的资源集`ID`。

```
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// 必填
```

，请替换为您实际的组织`ID`。

```
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// 必填，调用来
```

源说明。

```
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// 非必填（企业版V3.1
```

`5.0`及之前历史版本必填）,请替换为您实际的地域`ID`。

```
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修
```

改、删除、查询单实例详情时必填）,请替换为您实际的实例`ID`。

```
        /**
```

当使用`STS AccessKey`调用接口时需要在参数中加上`SecurityToken`字段。 调用方法如下：

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

#### 错误处理

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

## Python SDK调用示例

### 快速开始

本文介绍如何获取SDK并开始调用。

**环境准备**

使用阿里云专有云Python SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。 根据所用功能获取相应产品的Endpoint。具体操作，请参见获取RegionID和Endpoint信息。 要使用APFS功能，您必须安装阿里云Python SDK核心库。 具体安装步骤如下： 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

**使用Python SDK**

调用Python SDK的3个主要步骤如下：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

### 使用手册

#### 安装Python SDK

本文介绍如何安装及调用Python SDK。

**背景信息**

阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。

**说明**

使用产品的开发工具包，都必须安装阿里云Python SDK核心库。 要使用APFS功能，您必须安装阿里云Java SDK核心库。 具体安装步骤如下： 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Python SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```python
from aliyunsdkcore import client clt = client.AcsClient(access_key, acces_secret, region_id)
```

#### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。

**说明**

产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。 运行 `python -c "import ssl"` 检查Python环境是否支持OpenSSL。运行后，如果没有出现 `ImportError: No module named ssl` 的错误信息，说明已经支持OpenSSL。 若没有OpenSSL，运行以下命令安装：

```
pip install pyopenssl
```

**设置单个请求的HTTP/HTTPS协议**

参考以下代码示例为一个接口设置HTTPS调用：

```
request = DescribeInstancesRequest() request.set_protocol_type("https")
```

# 取值：`"https"` 或 `"http"`

**设置全局默认协议**

参考以下代码示例设置全局默认协议：

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
```

# 创建请求并调用 `client.do_action_with_exception()` 来发送请求

#### 使用CommonRequest进行调用

当您要调用的APFS的某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.set_action_name('Action')` 的方式来指定API名称。

| 如 | RunInstances | 接口，在发起 | CommonRequest |  |
|---|---|---|---|---|
| request.set action name('RunInstances') _ _ |  |  |  |  |
|  |  |  |  | 来 |

**示例：调用RPC风格的API**

使用文件系统的DescribeFileSystems接口获取文件系统信息的示例代码如下：

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <Endpoint>，请替换为您当前产品实际的Endpoint。

```bash
#!/usr/bin/env python
# coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`。

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('EFS') request.set_action_name('DescribeFileSystems') request.set_version('2017-06-26')
```

`request.set_domain('<Endpoint>') #`产品访问域名，当前为示例值，请替换为您实际的产品访问地址。

```bash
# or:
# request = = CommonRequest(product='EFS',
action_name='DescribeFileSystems',version='2017-06-26',domain='<Endpoint>')
######
```

# 设置请求协议类型，支持`https`或`http`，默认为`http`。
# 设置`https`方法如下：

```bash
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
```

# 当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段。
# 调用方法如下：

```bash
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
```

# 请替换为您实际的`SecurityToken`。

```
######
```

# 非必填，请替换为您实际的资源集`ID`。

```
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
```

# 必填，请替换为您实际的组织`ID`。

```
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
```

# 必填，调用来源说明。

```
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
```

# 非必填（企业版`V3.15.0`及之前历史版本必填），请替换为您实际的地域`ID`。

```
request.add_header("x-acs-regionid", "<yourRegionID>")
```

# 非必填（修改、删除、查询单实例详情时必填），请替换为您实际的实例`ID`。

```python
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))
```

#### 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

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

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问云产品。本操作介绍如何获取阿里云Go SDK并开始调用。

**环境准备**

使用Go SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参根据所用功能获取相应产品的Endpoint。具体操作，请参见获取RegionID和Endpoint信息。

**安装阿里云Go SDK核心包**

阿里云Go SDK支持Go 1.10.x及更高版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**使用Go SDK**

使用Go SDK的主要步骤如下：
1. 初始化Client实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

### 使用手册

#### 安装Go SDK核心包

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Go SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。 代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

**初始化Client实例**

```
   client, err := sdk.NewClientWithAccessKey(
```

`"<yourRegionID>", //`请替换为您实际的地域`ID`， `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID`， `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`，

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在ECS的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。

| 如 | RunInstances | 接口，在发起 | CommonRequest |  |
|---|---|---|---|---|
| request.setSysAction("RunInstances") |  |  |  |  |
|  |  |  |  | 来指定 |

**示例：调用RPC风格的API**

使用云盘的DescribeDisks接口获取云盘信息的示例代码如下：

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <Endpoint>，请替换为您当前产品实际的Endpoint。

```java
package main
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey(
```

`"<yourRegionID>", //`请替换为您实际的地域`ID`， `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID`， `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`，

```
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Method = "POST"
```

`request.Domain = "<endpoint>" //` 请求访问地址，当前为示例值，请根据实际请求地址替换，

```
    request.Product = "EFS"
    request.Version = "2017-06-26"
```

`//` 因为是`RPC`接口，因此需指定`APIName(Action)`， `//` 业务参数

```
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*` 当使用`STS AccessKey`调用`RPC`接口时，需要在参数中加上`SecurityToken`字段。 调用方式如下：

```
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
```

请替换为您实际的`SecurityToken`。 `*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // 必填，调用来源说明。
```

`request.Headers["x-acs-regionid"] = "<yourRegionID>" //` 非必填（企业版`V3.15.0`及之前历史版本必填），请替换为您实际的地域`ID`。

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // 非必填，请替换为
```

您实际的资源集`ID`。

```
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // 必填，请替换为您实
```

际的组织`ID`。 `// request.Headers["x-acs-instanceid"] = "<yourInstanceID>" //` 非必填（修改、删除、查看单实例详情时必填），请替换为您实际的实例`ID`

```
。 response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。

```
response,err := ecsClient.DescribeDisks(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个 `ClientError` 。 以下以ECS为例，您可以通过以下代码来判断并获取 `ClientError` 中的错误信息：

**说明**

使用具体异常结构时需要引入异常结构包github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors，引入方法请参考：

```java
package main
```

`"github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" //ecs`请替换为您实际的产品名称

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
response, err := ecsClient.DescribeDisks(request) if clientError, ok := err.(*errors.ClientError); ok{
```

`//` 获取错误码，

```
    clientError.ErrorCode()
```

`//` 获取错误描述，

```
    clientError.Message()
```

`//` 获取原始错误（可能为`nil`），

```
    clientError.OriginError()
}
```

**ServerError**

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以ECS为例，您可以通过以下代码来判断并获取 `ServerError` 以及 `Response` 中的错误信息：

**说明**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-` `go/sdk/errors` ，引入方法请参考： `"github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" //ecs`请替换为您实际的产品名称 。

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包。

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := ecsClient.DescribeDisks(request) if serverError, ok := err.(*errors.ServerError); ok{
```

`//` 获取错误码。

```
    serverError.ErrorCode()
```

`//` 获取错误描述。

```
    serverError.Message()
```

`//` 获取原始`http`应答。

```
    response.GetOriginHttpResponse()
}
```

## API参考

### 调用API

#### 概述

API接口调用是向产品的服务端地址发送HTTP GET请求。您需要按照接口描述在请求中加入相应请求参数。调用后系统会返回处理结果。请求及返回结果都使用UTF-8字符集编码。

#### 请求结构

**服务地址**

如何获取产品的endpoint，请参见获取RegionID和Endpoint信息。

**请求方法**

支持HTTP GET方法发送请求，这种方式下请求参数需要包含在请求的URL中。

**通信协议**

支持通过HTTP或HTTPS通道进行请求通信。为了获得更高的安全性，推荐您使用HTTPS通道发送请求。

**请求参数**

每个请求都需要指定要执行的操作，即Action参数（例如CreateFileSystem），以及每个操作都需要包含的公共请求参数和指定操作所特有的请求参数。

**字符编码**

请求及返回结果都使用UTF-8字符集进行编码。

#### API授权

为了确保您的账号安全，建议您使用RAM用户的身份凭证调用API。如果使用RAM用户调用块存储API，则您需要为该RAM用户创建并附加相应的授权策略。 在RAM中，可以对一个APFS资源进行以下Action的授权。

| 分类 | Action名称列表 |
|---|---|
| 文件系统 | CreateFileSystem DeleteFileSystem DescribeFileSystems ModifyFileSystem DescribeZones |

#### 返回结果

调用API服务后返回数据采用统一格式，返回的HTTP状态码为2xx，代表调用成功；返回4xx或5xx的HTTP 状态码代表调用失败。

### RAM鉴权

当RAM用户通过OpenAPI对阿里云账号的资源进行访问时，系统会向RAM进行权限检查，以确保资源拥有者的确将相关资源的相关权限授予了调用者。

**背景信息**

默认情况下，阿里云账号或者RAM用户均能使用APFS控制台或APFS API操作自己创建的资源。在以下场景中，会涉及到操作授权问题： RAM用户刚创建时没有权限操作阿里云账号的资源时。 从其他阿里云服务访问APFS资源，或者APFS访问其他阿里云服务时。 操作具有权限控制的APFS资源前，需要资源拥有者授权目标资源和目标API行为权限。 当其他账号通过APFS API访问阿里云账号资源时，阿里云APFS首先向RAM发起权限检查，以确保资源拥有者已经将相关权限授予调用者。不同的APFS API会根据涉及的资源以及API语义确定需要检查哪些资源的权限。

**规则详情**

每个不同的APFS API，会根据涉及到的资源以及API的语义，确定需要检查的资源的权限。

### 公共参数

公共参数分为公共请求参数、公共Header参数和公共返回参数。

**公共请求参数**

公共请求参数是指每个接口都需要使用到的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回值的类型，仅支持JSON。 |
| Version | String | 是 | API版本号，以日期形式YYYY-MM-DD输入。取值为2017-06-26。 |
| AccessKeyId | String | 是 | 访问服务使用的密钥ID。 |
| AccessKeySecret | String | 是 | 访问服务使用的密钥值。 |
| RegionId | String | 是 | 访问服务所使用的地域ID。 |
| Product | String | 是 | 接口对应的产品名称，产品名称取值为EFS。 |

**公共Header参数**

| 名称 | 描述 |
|---|---|
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID。具体获取方式，请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID。具体获取方式，请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID。具体获取方式，请参见获取实例ID。 |

**说明**

在调用各云产品接口调用时，您需要在调用代码的请求头Header中添加**x-acs-instanceid**、**x-acs-**
**organizationid**、**x-acs-resourcegroupid**等参数的实际值，用于指定当前实例的实例ID（在创
建实例和查询实例列表的场景下，实例ID不存在），及其所属的组织和资源集。若未添加相关Header 参数实际值，调用时则会默认指向root组织和root资源集。

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

### 地域

#### DescribeZones

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeZones | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值： DescribeZones。 |
| FileSystemType | String | 是 | efs |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 3E966328-66F0- 458D-B9C8- 02ADB59D7E53 | 请求id |
| ZoneId | String | cn-wulan-env38- amtest38001-a | 区域id |
| ClusterId | String | EfsStorageCluster- A-20250401-03ee | 天基集群id |
| StorageType | String | efs | 支持的文件系统规格 |

**示例**

正常返回示例

```json
{
    "RequestId": "2400D634-8E18-4E9E-B516-39081731B09A",
    "Zones": {
        "Zone": [
            {
                "ZoneId": "cn-wulan-env38-amtest38001-a",
                "Clusters": {
                    "Cluster": [
                        {
                            "ClusterId": "EfsStorageCluster-A-20250401-03ee",
                            "InstanceTypes": {
                                "InstanceType": [
                                    {
                                        "StorageType": "parastor_advance_300"
                                    }
```

]

```
                            }
                        }
```

]

```
                }
            }
```

]

```
    }
}
```

### 文件系统

#### CreateFileSystem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateFileSyste m | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值： CreateFileSystem。 |
| RegionId | String | 是 | cn-qingdao- env38-d01 | 所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ZoneId | String | 否 | cn-qingdao- env38- amtest11001-a | 可用区ID。必填参数。 |
| FileSystemType | String | 是 | efs | 文件系统类型, 目前只支持 efs |
| Capacity | Long | 是 | 20480 | 容量(GB), 1024以上, 1024的倍数。 |
| StorageType | String | 是 | parastor advanc _ e 300 _ | 文件系统规格, 对应fscd的fsSpec, 目前只支持: parastor advance 300(性能型) _ _ |
| ZoneId | String | 是 | cn-wulan-env38- amtest38001-a | ZoneId |
| ClusterId | String | 是 | EfsStorageClust er-A-20250401- 03ee | 天基集群id, 调用DescribeZones即可获取 |
| ProtocolType | String | 是 | EFS | 文件传输协议类型, 目前只支持 EFS |
| EncryptType | String | 是 | 0 | 0表示不加密, 1表示加密, 专有云场景不支持加密 |
| Description | String | 否 | - | 描述信息, 传入字符串信息, 要求: 1. 长度为2~128个英文或中文字符。 2. 必须以大小字母或中文开头，不能以 http:// 和 https:// 开头。 3. 可以包含数字、半角冒号（:）、下划线 （ ）或者连字符（-） _ |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

正常返回示例

```json
{"RequestId":"7EA4C27A-7EB5-47FD-89DE-EB274970CF87","FileSystemId":"efs-01b06fa3"}
```

#### DescribeFileSystems

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeFileSyst ems | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值： DescribeFileSystems。 |
| RegionId | String | 是 | cn-qingdao- env38-d01 | 所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ZoneId | String | 否 | cn-qingdao- env38- amtest11001-a | 可用区ID。必填参数。 |
| FileSystemId | String | 否 | efs-0156ec1d | 文件系统id |
| Description | String | 否 | - | 描述 |
| FileSystemType | String | 是 | efs |  |
| PageSize | Integer | 否 | 10(默认值) | 每页多少数据 |
| PageNumber | Integer | 否 | 1(默认值) | 第几页 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FileSystemId | String | efs-0156ec1d | 文件系统id |
| Status | String | Running | 文件系统状态, 所有状态如下: Pending 初始化中 Running 运行中 Deleting 删除中 Extending 扩容中 Shrinking 缩容中 Starting 启动中 Stopping 停止中 Stopped 已停止 |
| MeteredSize | Integer | 1000 | 已使用容量, 单位GB |
| Capacity | Integer | 1000 | 总容量, 单位GB |
| MountTarget | String |  | 挂载点信息 |
| MountTargetDomain | String |  | 挂载点名称 |

**示例**

正常返回示例

```json
{
    "FileSystems": {
        "FileSystem": [
            {
                "Status": "Running",
                "Description": "efs",
                "StorageType": "performance",
                "MountTargetCountLimit": 100,
                "ZoneId": "cn-wulan-env38-amtest38001-a",
                "CreateTime": "2024-03-26T19:22:47CST",
                "MeteredIASize": 0,
                "SupportedFeatures": {
                    "SupportedFeature": [
```

]

```json
                },
                "MountTargets": {
                    "MountTarget": [
```

]

```json
                },
                "MeteredSize": 0,
                "QuotaSize": 40960,
                "EncryptType": 0,
                "ProtocolType": "EFS",
                "Packages": {
                    "Package": [
```

]

```json
                },
                "FileSystemType": "efs",
                "FileSystemId": "efs-0156ec1d",
                "RegionId": "cn-wulan-env38-d01",
                "VolumeSize": 40960
            }
```

]

```json
    },
    "TotalCount": 1,
    "RequestId": "4306B744-C87D-45C7-8083-64C4E153F46C",
    "PageSize": 10,
    "PageNumber": 1
}
```

#### ModifyFileSystem

调用ModifyFileSystem修改一个APFS文件系统（注意：每次调用仅支持修改**文件系统容量**或者**描述**）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | ModifyFileSyste m | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值： ModifyFileSystem。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao- env38-d01 | 所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ZoneId | String | 否 | cn-qingdao- env38- amtest11001-a | 可用区ID。必填参数。 |
| FileSystemId | String | 是 | efs-0156ec1d | 文件系统id |
| Description | String | 否 | - | 描述 |
| Capacity | Long | 否 | 20480 | 容量, 1024以上1024的倍数, 目前只支持扩容 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

正常返回示例

```json
{
    "RequestId": "7EA4C27A-7EB5-47FD-89DE-EB274970CF87",
    "FileSystemId": "efs-01b06fa3"
}
```

#### DeleteFileSystem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DeleteFileSyste m | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值： DeleteFileSystem。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao- env38-d01 | 所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ZoneId | String | 否 | cn-qingdao- env38- amtest11001-a | 可用区ID。必填参数。 |
| FileSystemId | String | 是 | efs-0156ec1d | 文件系统id |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

正常返回示例

```json
{"RequestId":"7EA4C27A-7EB5-47FD-89DE-EB274970CF87","FileSystemId":"efs-01b06fa3"}
```

### 数据流动

#### CreateBackupPlan

创建备份计划。 该接口用于在APFS产品中创建备份计划，调用时需注意参数的必填性以及数据类型的要求。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanName | Strin g | Query | 是 | MyBackupPlan | 备份计划的名称。 |
| SourceFile SystemId | Strin g | Query | 是 | efs-12345678 | 源文件系统的ID。 |

| 高性能并行文件 PI参考 | 存储 APFS | 开发指南· |  |  |  |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

| SourcePat h | Strin g | Query | 是 | /source/path | 源路径。 |
|---|---|---|---|---|---|
| ScheduleE xpression | Strin g | Query | 是 | 0 0 * * * | 计划表达式，定义备份任务的执行时间。调度间隔不得小于1天。 |
| Migration Speed | Strin g | Query | 否 | LOW | 迁移速度限制。 枚举值: LOW(LOW) MEDIUM(MEDIUM) HIGH(HIGH) |
| TargetSto rageLocati on | Strin g | Query | 否 | oss-bucket-name/oss- path | 目标存储位置。 |
| ExcludePa ths | Strin g | Query | 否 | /tmp,/logs,/cache | 系统排除目录列表，被排除的路径下的文件不会备份。 |
| FileNameP attern | Strin g | Query | 否 | *.log,*.tmp,*.bak | 需要备份的文件名模式，只有命中的文件会被备份。 |
| FileSizeTh reshold | Strin g | Query | 否 | 1G,100G | 需要备份的文件大小阈值。 格式: 数字 + 单位，支持单个值或范围（逗号分隔的两个值） 支持单位: B（字节）、 K（KB）、M（MB）、 G（GB）、T（TB），不区分大小写单个值：表示只备份大于等于该大小的文件。例如 "1G" 表示只备份 ≥ 1GB 的文件范围写法: "最小值,最大值"，最小值必须严格小于最大值 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileOperat ionTimeTh reshold | Strin g | Query | 否 | 1h,1d | 文件修改时间阈值。 格式: 数字 + 单位，支持单个值或范围（逗号分隔的两个值）。单个值表示支持单位: ms 表示毫秒，s 表示秒，m（小写）表示分钟，h 表示小时，d 表示天，w 表示周，M（大写，按 30 天计算）表示月，y（按 365 天计算）表示年。需特别注意 m（分钟）和 M（月）大小写敏感。 单个值：表示只备份文件操作时间（如 mtime） 距今超过该时长的文件。 例如 "3d" 表示只备份最后修改时间在 3 天前及更早的文件（即文件年龄 ≥ 3 天）。 范围写法: "最小值,最大值"，最小值必须严格小于最大值。如"1d,5d"表示仅备份操作时间在 1 天 ~ 5 天之间的文件。 约束: 注意 m（分钟）和 M（月）大小写敏感范围模式下只能有恰好 2 个值范围模式下 min 必须 < max 数字部分必须为整数 （不支持小数） |
| MaxCapac ityGB | Integ er | Query | 否 | 5120 | 备份计划创建的所有副本占用的OSS容量限制 （GiB），默认为1024。 默认值：1024 |
| Descriptio n | Strin g | Query | 否 | TestDescription | 描述 |
| DryRun | Boole an | Query | 否 | false | 是否为试运行，默认为 false。 默认值：false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1234567890abcdef | 请求唯一标识。 |
| PlanId | String | bp-12345678 | 备份计划的唯一标识。 |

**示例**

请求示例

```
&PlanName=MyBackupPlan &SourceFileSystemId=fs-12345678 &SourcePath=/source/path &ScheduleExpression=‘0 0 * * *’
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1234567890abcdef",
 "PlanId":"bp-12345678"
}
```

#### DescribeImportJobs

查询导入任务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| JobId | Strin g | Query | 否 | job-123456 | 导入任务的ID。 |
| FileSyste mId | Strin g | Query | 否 | fs-123456 | 文件系统的ID。 |
| Status | Strin g | Query | 否 | Running | 任务状态。 |
| PageSize | Integ er | Query | 否 | 10 | 分页大小，默认为10，最大值为100。 默认值：10 取值范围：<1, 100> |

|  |  |  |  | 高性能 | 并行文件存储 APFS 开发指南 API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Query | 否 | 1 | 分页页码，默认为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ImportJobs | Array | [{...},{...}] | 导入任务列表。 |
| -JobId | String | job-123456 | 任务ID。 |
| -JobName | String | ImportTask1 | 任务名称。 |
| -UserId | String | 1234567890 | 用户ID。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |
| -ZoneId | String | cn-hangzhou-a | 可用区ID。 |
| -Status | String | Running | 任务状态。 |
| -Progress | Integer | 50 | 任务进度。 |
| -FileSystemId | String | fs-123456 | 文件系统ID。 |
| - FileSystemPat h | String | /test/ | 目标文件系统下的路径。 |
| - OssBucketNa me | String | backup- 1857XXXXX489 | OSS Bucket名称。 |
| -OssPath | String | /test/abc | OSS路径。 |
| - StorageLocatio n | String | NULL | 存储位置，该字段目前暂未使用。 |
| -ReplicaSize | Long | 1024000 | 备份占用空间。单位: Byte。 |
| -FileCount | Long | 1600 | 当前已导入的文件数量。 |

| 高性能并行文件存储 | APFS 开发指南· |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -TotalBytes | Long | 254166333 | 总文件大小。单位：Byte。 |
| - TotalFileCount | Long | 34200073 | 总文件个数。 |
| -CreateTime | String | 2024-10-14 08:00:00 | 创建时间。 |
| -StartTime | String | 2024-10-14 12:00:00 | 开始时间。 |
| - CompletedTim e | String | 2024-10-14 12:15:00 | 任务完成时间。 |
| -Description | String | testDescription | 描述。 |
| -Speed | String | 204800 | 实际的平均备份/导入速度。单位为Byte/s。 |
| -ErrorMessage | String | Failed | 错误信息。 |
| -UpdatedTime | String | 2021-03-08 15:34:49.0 | 更新时间。 |
| -BwLimit | String | 100M | 每个存储节点的传输带宽限制。 |
| -ExcludePaths | String | *.log | 排除的目录。 |
| - FileNamePatte rn | String | *.log | 文件名匹配规则。 |
| RequestId | String | 1234567890ABCD EF | 请求唯一标识符。 |
| TotalCount | Integer | 100 | 总记录数。 |
| PageSize | Integer | 10 | 分页大小。 |
| PageNumber | Integer | 1 | 当前页码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeImportJobs
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "ImportJobs":[
  {
   "FileSystemPath":"",
   "Description":"",
   "CompletedTime":"",
   "TotalFileCount":"",
   "JobName":"ImportTask1",
   "BwLimit":"",
   "TotalBytes":"",
   "FileSystemId":"fs-123456",
   "StorageLocation":"",
   "JobId":"job-123456",
   "Status":"Running",
   "Speed":"",
   "Progress":50,
   "FileCount":"",
   "ZoneId":"",
   "CreateTime":"",
   "StartTime":"",
   "FileNamePattern":"",
   "UserId":"1234567890",
   "ExcludePaths":"",
   "OssPath":"",
   "OssBucketName":"",
   "RegionId":"cn-hangzhou",
   "UpdatedTime":"",
   "ErrorMessage":"",
   "ReplicaSize":""
  }
```

`],`

```json
 "TotalCount":100,
 "RequestId":"1234567890ABCDEF",
 "PageSize":10,
 "PageNumber":1
}
```

#### CreateImportJob

创建导入任务，用于将文件从OSS导入到文件系统。

**注意事项**

调用此接口前，请确保您已开通相关服务并具备调用权限。 请求中 `FileSystemId` 、 `FileSystemPath` 、 `OssBucket` 和 `OssPath` 为必填参数。 接口支持HTTPS和HTTP协议，推荐使用HTTPS以保证数据传输安全。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSyste mId | Strin g | Query | 是 | fs-xxxxxxxx | 文件系统的唯一标识符。 |
| FileSyste mPath | Strin g | Query | 是 | /mnt/data | 文件系统中的路径。 |
| OssBucket | Strin g | Query | 是 | my-bucket | OSS存储桶名称。 |
| OssPath | Strin g | Query | 是 | /oss/path | OSS中的路径。 |
| BwLimit | Strin g | Query | 否 | 100MB/s | 带宽限制，单位为MB/s。 |
| ExcludePa ths | Strin g | Query | 否 | /tmp,/logs,/cache | 系统排除目录列表，被排除的路径下的文件不会备份。 |
| FileNameP attern | Strin g | Query | 否 | *.log,*.tmp,*.bak | 需要备份的文件名模式，只有命中的文件会被备份。 |
| DryRun | Boole an | Query | 否 | false | 是否仅进行预检查，默认为 false。 默认值：false |
| JobName | Strin g | Query | 否 | testjob | 任务名称。 |
| Descriptio n | Strin g | Query | 否 | TestDescription | 描述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | uniqueRequestId | 唯一请求ID，用于追踪请求。 |
| JobId | String | job-xxxxxxxx | 创建的导入任务的唯一标识符。 |

**示例**

请求示例

```
&FileSystemId=fs-xxxxxxxx &FileSystemPath=/mnt/data &OssBucket=my-bucket &OssPath=/oss/path
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"uniqueRequestId",
 "JobId":"job-xxxxxxxx"
}
```

#### DeleteImportJob

删除导入任务。 该接口用于删除指定的导入任务。调用此接口前，请确保任务已完成或不再需要，避免误删造成数据丢失。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| JobId | Strin g | Query | 是 | job-1234567890abcdef | 要删除的导入任务ID。 |
| DryRun | Boole an | Query | 否 | false | 是否进行试运行，默认为 false。 默认值：false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 12345678-1234- 1234-1234- 1234567890ab | 请求唯一标识符。 |

**示例**

请求示例

```
&JobId=job-1234567890abcdef
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"12345678-1234-1234-1234-1234567890ab"
}
```

#### ControlReplicaTask

用于控制副本任务的操作，例如取消任务。 该接口支持通过 `ReplicaId` 和 `Operation` 参数来执行特定的副本任务操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ReplicaId | Strin g | Query | 是 | replica-12345 | 需要操作的副本ID。 |
| Operation | Strin g | Query | 是 | CANCEL | 对副本执行的操作，目前仅支持 CANCEL 。 |
| DryRun | Boole an | Query | 否 | false | 是否为试运行模式，默认值为 false 。 默认值： false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1234567890abcdef | 返回请求的唯一标识符。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ControlReplicaTask &ReplicaId=replica-12345 &Operation=CANCEL
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1234567890abcdef"
}
```

#### ControlImportJob

控制导入任务的API，用于执行取消操作。

**注意事项**

`Operation` 参数固定为 `CANCEL` ，表示取消操作。 可选参数 `DryRun` 可用于测试调用是否成功，而不实际执行操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| JobId | Strin g | Query | 是 | JOB-1234567890 | 需要控制的导入任务ID。 |
| Operation | Strin g | Query | 是 | CANCEL | 操作类型，目前仅支持取消操作（CANCEL）。 枚举值: CANCEL(CANCEL) |
| DryRun | Boole an | Query | 否 | false | 是否为预检调用，默认为 false 。 默认值： false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1234567890ABCD EF | 请求唯一标识符，用于追踪请求结果。 |

**示例**

请求示例

```
&JobId=JOB-1234567890 &Operation=CANCEL
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1234567890ABCDEF"
}
```
