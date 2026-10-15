---
title: "VPN网关 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 103
source_pdf: "05_开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/vpn/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# VPN网关 开发指南

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
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。

**说明**

调用API时，请在Header参数中增加组织ID `<x-acs-organizationid>` 和资源集ID `<x-acs-resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参见开发文档使用说明。
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。

## 准备工作

### 登录开发者门户

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
2. 输入正确的用户名及密码。
请向运营管理员获取登录控制台的用户名和密码。

**说明**

首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且至少包含以下两种类型： 英文大写或小写字母（A~Z、a~z） 阿拉伯数字（0~9） 特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）
3. 单击**登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：
管理员强制开启MFA后的首次登录： a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**登录**。 c. 输入6位MFA码后单击**认证**。 您已开启并绑定MFA： 输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《**Apsara Uni-manager****运营控制台用户指南》**中的**《绑定并开启虚拟****MFA****设备》**章节。
5. 在页面顶部的菜单栏中，选择**产品** > **应用服务** > **开发者门户**。

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

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参见获取STS AccessKey。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号 AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域ID。例如cn-hangzhou-* 。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni- manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方法可参见《Apsara Uni- manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID。实例ID可以从实例列表中查询到。 |

**获取个人账号AccessKey**

1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。
****************和********************是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**说明**

**获取组织AccessKey**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用云产品API时，三元组缺一不可。更多STS内容请参见什么是STS。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

| 说明以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com>，请替换为实际的STS Endpoint。 |  |  |
|---|---|---|
| public static void main(String[] args) { // 创建DefaultAcsClient实例并初始化。 // 请替换为您实际的地域ID、AccessKey ID、AccessKey Secret DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>"); HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true); clientConfig.setProtocolType(ProtocolType.HTTPS); profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); String assumeRole = callAssumeRole(client); if (StringUtils.isEmpty(assumeRole)) return; JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole); JSONObject credentials = assumeRoleJson.getJSONObject("Credentials"); // 获取到STS三元组 String stsAK = credentials.getString("AccessKeyId"); String stsSK = credentials.getString("AccessKeySecret"); String stsToken = credentials.getString("SecurityToken"); } private static String callAssumeRole(IAcsClient client) { CommonRequest request = new CommonRequest(); // "<sts.aliyuns.com>" 请替换为实际的STS Endpoint，一般格式为sts-vpc.${global:region}.${global:internet-domain} request.setSysDomain("<sts.aliyuns.com>"); request.setSysProduct("Sts"); request.setSysAction("AssumeRole"); request.setSysVersion("2015-04-01"); request.setSysMethod(MethodType.POST); request.setHttpContentType(FormatType.FORM); // 业务参数，设置本次调用Session的别名，"<yourRoleSessionName>"请您替换为实际值 request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>"); // 扮演的Role角色ARN，"<yourRoleArn>"请替换为上一步获取到的实际Ram Role ARN request.putQueryParameter("RoleArn", "<yourRoleArn>"); try { CommonResponse response = client.getCommonResponse(request); return response.getData(); } catch (ServerException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } catch (ClientException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } return null; } |  |  |
| 通过STS AccessKey三元组调用云产品的接口，下列代码以VPN网关的 | DescribeCustomerGateway | 接口为示例。 |

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>,请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。

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
    request.setSysDomain("vpc.aliyuncs.com");
    request.setSysProduct("Vpc");
    request.setSysAction("DescribeCustomerGateway");
    request.setSysVersion("2016-04-28");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//"<yourRegionID>"` 请替换为您实际的地域`ID`

```
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
```

`// "<yourStsToken>"` 请替换为您前一步获取到的`STS`三元组中`SecurityToken`

```
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
```

`//` 非必填,请替换为您实际的资源集`ID`

```
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填,请替换为您实际的组织`ID`

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
```

### 获取公共Header参数

调用专有云API时需要提供多个Header参数。本文为您介绍这些参数的含义及其获取方式，并对调用后的一些返回值做出解释。

**Header参数描述**

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，获取方式请参见获取Region ID。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID，获取方式请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID，获取方式请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID，获取方式请参见获取实例ID。 |

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

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以VPN网关为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**网络**>**专有网络****VPC**。
3. 在左侧导航栏中，选择**VPN**>**VPN****网关**。
4. 在**VPN****网关**页面查看**实例****ID/****名称**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 获取VPN网关的Endpoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取VPN网关的SDK包

通过POP网关调用专有云API时，需使用相应云产品的SDK。本文为您介绍如何获取阿里云开发工具包（SDK）。 软件开发工具包（SDK）包括代码以及示例，用户可以自行选择语言创建云应用。

**背景信息**

实现VPN网关功能需要您同时安装VPC SDK（VPN网关使用VPC SDK实现功能）和阿里云核心库。以Java SDK为例，您需要下载 `aliyun-java-sdk-vpc` 以及 `aliyun-`

```
java-sdk-core 。
```

VPC SDK封装了2016-04-28版本API，以访问密钥（AccessKey）识别调用者身份，提供自动签名等功能，方便您通过API创建和管理资源。阿里云开发工具包（SDK） 包括代码以及示例，您可以自行选择语言来创建云应用。 SDK核心库推荐您使用阿里云官网的SDK核心库，该内容适用于所有云产品，也同样适用于专有云产品。

**获取VPC SDK包**

目前SDK的语言支持：Java、Python、Go，您可以前往阿里云开发工具包（SDK）中进行选择。

**说明**

推荐使用 Java、Python、Go三种语言的SDK包，使用其他语言的SDK包可能发生不兼容情况。

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

使用CommonRequest调用方式可实现任意Open API接口的调用。 `//` 创建`API`请求并设置参数。

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

可参考以下代码发起请求并处理返回结果。

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

以下代码为通过Apsara Uni-manager运营控制台的 `GetOrganizationList` 接口获取组织列表的调用示例。

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

本节介绍如何获取VPC Java SDK并开始调用。VPN网关使用VPC SDK实现功能。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参见获取AccessKey。 获取VPN网关的Endpoint，具体操作，参见获取VPN网关的Endpoint。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云 Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入Maven文件。 要使用VPC的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17及以上版本，SDK的版本为3.2.0。

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

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Product>，请替换为您实际的产品名称。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <readTimeout>，请您根据实际情况设置读取超时时间，单位为毫秒。 <connectionTimeout>，请您根据实际情况设置连接超时时间，单位为毫秒。 <maxRequestsPerHost>，请您根据实际情况设置每个主机的最大请求数。 <maxRequests>，请您根据实际情况设置最大请求数。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。

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
        DescribeCustomerGatewayRequest request = new DescribeCustomerGatewayRequest();
```

`//` 业务参数

```
        request.setCustomerGatewayId("<yourInstanceID>");
```

`//` 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用

```
        request.putHeaderParameter("x-acs-organizationid", "appstrea****");
        request.putHeaderParameter("x-acs-resourcegroupid", "rs-1018fc75f29c0aab491e****");
```

`//` 发起请求并处理应答或异常

```java
        DescribeCustomerGatewayResponse response;
       try {
            DescribeCustomerGatewayResponse response = client.getAcsResponse(request);
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

阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包（SDK）的方式安装专有云Java SDK。 要使用VPC的开发工具包，必须安装阿里云Java SDK核心库以及VPC的Java SDK。SDK核心库推荐使用4.5.17及以上版本，Java SDK的版本为3.2.0。 以使用VPC的Java SDK为例，您需要安装阿里云Java SDK核心库和VPC Java SDK，并在pom.xml文件中添加以下依赖。准确的SDK版本号，请参见阿里云开发工具包 （SDK）。

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

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。 目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法，请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

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

本文介绍如何使用VPC Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例如DescribeCustomerGateway。 在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。

```
DescribeCustomerGatewayRequest request = new DescribeCustomerGatewayRequest();
```

`//` 业务参数，以下以输入用户网关`ID`为例，请将用户网关`ID`替换为您的实际用户网关`ID`

```
request.setCustomerGatewayId("cgw-ow25mqjb6mxnk****");
```

`//` 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用

```
request.putHeaderParameter("x-acs-organizationid", "appstrea****"); request.putHeaderParameter("x-acs-resourcegroupid", "rs-1018fc75f29c0aab****");
```

3. 发起调用并处理应答。

| DescribeCustomerGatewayResponse response; try { DescribeCustomerGatewayResponse response = client.getAcsResponse(request); System.out.println(new Gson().toJson(response)); } catch (ServerException e) { e.printStackTrace(); } catch (ClientException e) { e.printStackTrace(); } |  |  |  |  |
|---|---|---|---|---|
| 正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 |  | response.getXXX() |  | 来获得应答中的字段。 |
| instanceStatus := response.getStatus(); |  |  |  |  |
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

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07-14）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAccessKeyId>", "<yourAccessSecret>");
```

`//` 忽略`SSL`

```
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
```

`//` 设置连接超时

```
        // clientConfig.setConnectionTimeoutMillis(3000L);
```

`//` 设置读取超时

```
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`//` 设置请求方式

```
        request.setSysMethod(MethodType.POST);
```

`//` 设置云产品`Endpoint`

```
        request.setSysDomain("<apigatewayEndpoint>");
```

`//` 设置访问接口版本

```
        request.setSysVersion("2016-07-14");
        // 设置LocationProduct
        request.setSysLocationProduct("apigateway");
```

`//` 设置访问接口的名称

```
        request.setSysAction("DescribeApiGroups");
```

`//` 当使用`sts ak`调用`RPC`接口时需要在参数中加上`SecurityToken`字段

```
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
```

`//` 业务参数

```
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
```

`//` 必填值，调用来源说明

```
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
```

`//` 非必填，企业版`V3.15.0`之前历史版本需要

```
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
```

`//` 非必填，资源集`ID`

```
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
```

`//` 必填, 组织`ID`

```
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
```

`//` 非必填，修改&删除操作需要

```
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        try {
```

`//` 发起请求并处理应答或异常。

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

使用CommonRequest调用方式可实现任意Open API接口的调用。
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

本节介绍如何获取VPC Python SDK并开始调用。VPN网关使用VPC SDK实现功能。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参见获取AccessKey。 获取VPN网关的Endpoint。具体操作，参见获取VPN网关的Endpoint。
1. 安装SDK核心库。
如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

2. 安装SDK。
以下以安装VPC SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装VPC的SDK：

```
pip install aliyun-python-sdk-vpc
```

如果您使用的是Python 3.x，执行以下命令，安装VPC的SDK：

```
pip3 install aliyun-python-sdk-vpc
```

**使用Python SDK**

以下示例以VPC为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

**说明**

涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkvpc.request.v20160428 import DescribeCustomerGateways
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
request = DescribeCustomerGatewaysRequest.DescribeCustomerGatewaysRequest()
```

`request.set_accept_format('json') #` 设置返回数据格式

```bash
# get response
response = clt.do_action_with_exception(request)
```

`print response #` 如果您使用的`Python 3.x`，此处为`print (response)`

### 使用手册

#### 4.2.1. 安装Python SDK

本文档介绍如何安装及调用VPC Python SDK。VPN网关使用VPC SDK实现功能。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。 使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用VPC的Python SDK，您需要安装阿里云Python SDK核心库和VPC的

**说明**

Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

安装云产品的SDK，以下以安装VPC的SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装VPC的SDK：

```
pip install aliyun-python-sdk-vpc
```

如果您使用的是Python 3.x，执行以下命令，安装VPC的SDK：

```
pip3 install aliyun-python-sdk-vpc
```

#### 4.2.2. 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证。获取AccessKey的方法，请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

**重要**

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 4.2.3. 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。

**说明**

产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。

| 运行 | python -c "import ssl" | 检查Py |
|---|---|---|
| ImportError: No module named ssl |  |  |

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

#### 4.2.4. 发起调用

本节介绍如何使用VPC Python SDK发起请求。VPN网关使用VPC SDK实现功能。

**操作步骤**

1. 导入VPC的SDK。

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkvpc.request.v20160428 import DescribeCustomerGateways
```

2. 新建一个AcsClient。

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. 创建Request对象。

```
request = DescribeCustomerGatewaysRequest.DescribeCustomerGatewaysRequest() request.set_accept_format('json')
```

4. 发起调用并处理返回。

```
response = clt.do_action_with_exception(request) print response
```

#### 4.2.5. 错误处理

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

#### 4.2.6. 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式 （CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

**CommonRequest调用示例**

调用示例接口信息：产品（ECS）、接口（DescribeInstances）、版本（2014-05-26）。 示例代码如下：

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
```

# 创建`AcsClient`实例

```
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
    "<your-RegionID>",
```

`timeout=1000, #` 设置超时时间 `verify=False, #` 忽略证书或者`verify='<`证书位置`>'`

```
);
```

# 和`https`一起使用

```python
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
```

# 创建`request`，并设置参数

```
    request = CommonRequest()
```

# 当使用`sts ak`调用`rpc`接口时需要在参数中加上`SecurityToken`字段

```bash
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
```

# 必填值，调用来源说明

```
        "x-acs-caller-sdk-source":"ApiTestDemo",
```

# 非必填，企业版`V3.15.0`之前历史版本需要

```
        "x-acs-regionid":"<your-RegionID>",
```

# 非必填，资源集`ID`

```
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
```

# 必填，组织`ID`

```
        "x-acs-organizationid":"<your-OrganizationID>"
```

# 非必填，修改&删除操作需要

```bash
        # "x-acs-instanceid":"<your-InstanceID>"
    }
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   //Endpoint请替换为真实地址
    request.set_product("apigateway")
    request.set_method("POST")
```

# 发起`API`请求并显示返回值

```python
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

**设置代理**

示例代码如下：
# https的代理

```
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
```

# http的代理

```
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS配置**

下面介绍使用HTTPS协议进行OpenAPI访问。

**使用HTTPS协议**

SDK默认使用HTTPS协议。

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
```

)

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # 使用https client.do_action_with_exception(request)
```

**忽略证书**

**重要**

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL/TLS证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过参数 `verify` 设置。

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
```

`verify=False #` 忽略对 `SSL` 证书的验证 )

**指定CA证书文件**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
    verify='./cacert.pem'  # 证书路径
```

)

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

使用CommonRequest调用方式可实现任意Open API接口的调用。 `//` 创建`API`请求并设置参数。

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

可参考以下代码发起请求并处理返回结果。

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

以下代码为通过ASCM的 `GetOrganizationList` 接口获取组织列表的调用示例。

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

阿里云Go SDK让您不用复杂编程即可访问。本操作介绍如何获取阿里云 VPC Go SDK并开始调用。VPN网关使用VPC SDK实现功能。

**环境准备**

使用Go SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参见获取AccessKey。 获取VPN网关的Endpoint。具体操作，请参见获取VPN网关的Endpoint。

**安装阿里云Go SDK核心包**

阿里云Go SDK支持Go 1.10.x及更高版本，您可以通过执行以下命令安装Go SDK核心包。

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
    request := vpc.CreateDescribeCustomerGatewaysRequest()
```

`//` 设置当前产品的`Endpoint`

```
    request.Domain = "<Endpoint>"
    // 等价于 request.PageSize = "10"
    request.PageSize = requests.NewInteger(10)
```

`//` 发起请求并处理异常

```
    response, err := vpcClient.DescribeCustomerGateways(request)
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

当使用阿里云的专有云SDK访问其专有云服务时，您需要提供授权的账号进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证。获取AccessKey的方法，请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的阿里云账号的信息安全。

**重要**

`//` 初始化`vpcClient`实例

```
vpcClient, err := vpc.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 5.2.3. 发起调用

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
**${apiName}**为API名称，例如DescribeCustomerGateways。

```
request := vpc.CreateDescribeCustomerGatewaysRequest() request.InstanceId = ""
```

4. 发起调用。

```
response, err := vpcClient.DescribeCustomerGateways(request)
```

#### 5.2.4. 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。

```
response,err := vpcClient.DescribeCustomerGateways(request) if err != nil {
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
response, err := vpcClient.DescribeCustomerGateways(request) if clientError, ok := err.(*errors.ClientError); ok{
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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从Response中获得原始的HTTP应答。 以下以VPN网关为例，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息：

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
response, err := vpcClient.DescribeCustomerGateways(request) if serverError, ok := err.(*errors.ServerError); ok{
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

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07-14）。 示例代码如下：

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<AccessKey Secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
```

`//` 当使用`sts ak`调用`rpc`接口时需要在参数中加上`SecurityToken`字段

```
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
```

`//` 必填值，调用来源说明

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
```

`//` 非必填，企业版`V3.15.0`之前历史版本需要

```
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
```

`//` 非必填，资源集`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
```

`//` 必填，组织`ID`

```
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
```

`//` 非必填，修改&删除操作需要

```
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下：

```java
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "<yourAccessSecret>")
 request := requests.NewCommonRequest()
 request.Method = "GET"
 request.Domain = "<crEndpoint>"
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"
 request.PathPattern = "/namespace"
```

`//` 当使用`sts ak`调用`ROA`接口时需要在`header`中加上`x-acs-security-token`字段

```
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
```

`//` 必填值，调用来源说明

```
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
```

`//` 非必填，企业版`V3.15.0`之前历史版本需要

```
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
```

`//` 非必填，资源集`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
```

`//` 必填，组织`ID`

```
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
```

`//` 非必填，修改&删除操作需要

```
 // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
 }
 fmt.Print(response.GetHttpContentString())
}
```

**设置代理**

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下：

```java
import (
    "os"
```

)

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // 设置 HTTP_PROXY 环境变量
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // 设置 HTTPS_PROXY 环境变量
}
```

通过客户端设置。 设置代码如下： `//` 客户端设置代理优先级比环境变量高

```
client.SetHttpProxy("http://x.x.x.x:xxxx") // 设置http代理 client.GetHttpProxy() // 获取http代理 client.SetHttpsProxy("https://x.x.x.x:xxxx") // 设置https代理 client.GetHttpsProxy() // 获取https代理 client.SetNoProxy("127.0.0.1,localhost") // 设置代理白名单 client.GetNoProxy() // 获取代理白名单
```

**SSL验证**

**摘要**

请求时验证SSL证书行为。 设置成 `true` ，禁用证书验证（这是不安全的，请设置证书！）。 设置成 `false` ，启用SSL证书验证，默认使用操作系统提供的CA证书。

**默认值**

默认值为 `false` 。

**设置**

**重要**

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可参考如下内容进行设置。 `//` 设置请求 `HTTPSInsecure`（只影响当前）

```
request.SetHTTPSInsecure(true) // 设置请求 HTTPSInsecure 为 true isInsecure := request.GetHTTPSInsecure() // 获取请求 HTTPSInsecure
```

当请求未设置时，客户端设置才能生效。 `//` 设置客户端 `HTTPSInsecure`（用于客户端发送的所有请求）。

```
client.SetHTTPSInsecure(true) // 设置客户端 HTTPSInsecure 为 true isInsecure := client.GetHTTPSInsecure() // 获取客户端 HTTPSInsecure
```

## API参考

### API概览

| API | 说明 |
|---|---|
| CreateVpnGateway | 创建VPN网关。 |
| ModifyVpnGatewayAttribute | 修改VPN网关的名称和描述信息。 |
| DescribeVpnGateways | 查询已创建的VPN网关。 |
| DescribeVpnGateway | 查询指定VPN网关的详细信息。 |
| DeleteVpnGateway | 删除VPN网关。 |
| DescribeRegions | 查询可用的地域。 |

### 用户网关

| API | 说明 |
|---|---|
| CreateCustomerGateway | 创建用户网关。 |
| ModifyCustomerGatewayAttribute | 修改用户网关的名称和描述信息。 |
| DescribeCustomerGateways | 查询已创建的用户网关。 |
| DescribeCustomerGateway | 查询已创建的用户网关的详细信息。 |
| DeleteCustomerGateway | 删除指定的用户网关。 |

| API | 说明 |
|---|---|
| CreateVpnRouteEntry | 创建VPN目的路由。 |
| CreateVpnPbrRouteEntry | 创建VPN策略路由。 |
| PublishVpnRouteEntry | 发布VPN路由到VPC。 |
| DescribeVpnRouteEntries | 查询VPN目的路由。 |
| DescribeVpnPbrRouteEntries | 查询VPN策略路由。 |
| ModifyVpnRouteEntryWeight | 修改VPN目的路由的权重值。 |
| ModifyVpnPbrRouteEntryWeight | 修改VPN策略路由的权重值。 |
| DeleteVpnRouteEntry | 删除VPN目的路由。 |
| DeleteVpnPbrRouteEntry | 删除VPN策略路由。 |

| API | 说明 |
|---|---|
| CreateVpnConnection | 创建IPsec连接。 |
| ModifyVpnConnectionAttribute | 修改IPsec连接的配置信息。 |
| DescribeVpnConnections | 查询已创建的IPsec连接。 |
| DescribeVpnConnection | 查询已创建的IPsec连接的详细信息。 |
| DownloadVpnConnectionConfig | 下载IPsec连接的配置信息。 |
| DeleteVpnConnection | 删除指定的IPsec连接。 |

| API | 说明 |
|---|---|
| CreateSslVpnServer | 创建SSL-VPN服务端。 |
| ModifySslVpnServer | 修改SSL-VPN服务端的配置信息。 |
| DescribeSslVpnServers | 查询已创建的SSL-VPN服务端。 |
| DescribeVpnSslServerLogs | 查询SSL服务端的日志。 |
| DeleteSslVpnServer | 删除SSL-VPN服务端实例。 |
| CreateSslVpnClientCert | 创建SSL-VPN客户端证书。 |

| ModifySslVpnClientCert | 修改SSL-VPN客户端证书的名称。 |
|---|---|
| DescribeSslVpnClientCerts | 查询已创建的SSL-VPN客户端证书。 |
| DescribeSslVpnClientCert | 查询指定的SSL客户端证书信息。 |
| DeleteSslVpnClientCert | 删除SSL-VPN客户端证书。 |

### 调用API

#### 6.2.1. 请求结构

调用VPN网关接口是向VPN网关API的服务端地址发送HTTP GET请求。您需要按照接口描述在请求中加入相应请求参数，调用后系统会返回处理结果。请求及返回结果都使用UTF-8字符集进行编码。 VPN网关的API是RPC风格，您可以通过发送HTTP GET请求调用VPN网关API。 其请求结构如下：

```
http://Endpoint/?Action=xx&Parameters
```

其中：

| Endpoint：VPN网关API的服务接入地址为 | vpc.example.com | 。 |
|---|---|---|
| 说明 example.com 是项目自定义的访问域名。您可以在Apsara Stack运维系统获取Endpoint，具体操作，请参见获取VPN网关的Endpoint。 |  |  |

**Action**：要执行的操作，例如使用DescribeVpnGateways查询已创建的VPN网关。
**Parameters**：请求参数，每个参数之间用and（&）符号分隔。
请求参数由公共请求参数和API自定义参数组成。公共参数中包含API版本号、身份验证等信息，关于公共参数的更多信息，请参见公共参数。 下面是一个调用DescribeVpnGateways接口查询已创建的VPN网关的示例：

**说明**

为了便于您查看，本文中的示例都做了格式化处理。

```
https://vpc.example.com/?Action=DescribeVpnGateways &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 6.2.2. API授权

为了确保您的账号安全，建议您使用子账号的身份凭证调用API。如果您使用RAM账号调用VPN网关API，您需要为该RAM账号创建、附加相应的授权策略。

#### 6.2.3. API签名

VPN网关服务会对每个API请求进行身份验证，无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。 VPN网关通过使用AccessKey ID和AccessKey Secret进行对称加密的方法来验证请求的发送者身份。AccessKey是为阿里云账号和RAM用户发布的一种身份凭证（类似于用户的登录密码），其中AccessKey ID 用于标识访问者的身份，AccessKey Secret是用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密。关于如何创 RPC API需按如下格式在请求中增加签名（Signature）：

| https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf |  |  |  |
|---|---|---|---|
| 以DescribeVpnGateways为例，假设AccessKey ID是 | testid | ， AccessKey Secret是 | testsecret |
| http://vpc.example.com/?Action=DescribeVpnGateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 |  |  |  |

完成以下步骤计算签名：
1. 使用请求参数创建待签名字符串：

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpnGateways&Format%3DXML&SignatureMethod%3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f- 4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2016-04-28
```

2. 计算待签名的HMAC的值。

| 在AccessKey Secret后添加一个“&”作为计算HMAC值的key。本示例中的key为 | testsecret& | 。 |
|---|---|---|
| CT9X0VtwR86fNWSnsc6v8YGOjuE= |  |  |

3. 将签名加到请求参数中：

```
http://vpc.example.com/?Action=DescribeVpnGateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

#### 6.2.4. RAM鉴权

在使用RAM账号调用VPN网关API前，需要主账号通过创建授权策略对RAM账号进行授权。在授权策略中，使用资源描述符（Alibaba Cloud Resource Name, ARN）指定授权资源。

| 资源类型 | 授权策略中的资源描述方法 |
|---|---|
| VPN网关（VPN Gateway） | acs:vpc:$regionid:$accountid:vpngateway/$vpngatewayid |
|  | acs:vpc:$regionid:$accountid:vpngateway/* |
|  | acs:vpc:*:$accountid:vpngateway/* |
| 用户网关（Customer Gateway） | acs:vpc:$regionid:$accountid:customergateway/$customergatewayid |
|  | acs:vpc:$regionid:$accountid:customergateway/* |
|  | acs:vpc:*:$accountid:customergateway/* |
| IPsec连接（IPsec Connection） | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |
|  | acs:vpc:$regionid:$accountid:vpnconnection/* |
|  | acs:vpc:*:$accountid:vpnconnection/* |
| SSL-VPN服务器（sslvpnserver） | acs:vpc:$regionid:$accountid:sslvpnserver/$sslvpnserverid |
|  | acs:vpc:$regionid:$accountid:sslvpnserver/* |
|  | acs:vpc:*:$accountid:sslvpnserver/* |
| SSL-VPN客户端证书 （sslvpnclientcert） | acs:vpc:$regionid:$accountid:sslvpnclientcert/$sslvpnclientcertid |
|  | acs:vpc:$regionid:$accountid:sslvpnclientcert/* |
|  | acs:vpc:*:$accountid:sslvpnclientcert/* |
| 通用资源 | acs:vpc:$regionid:$accountid:* |
|  | acs:vpc:*:$accountid:* |

其中 $regionid/accoutid/vrouterid 为具体的资源ID， * 代表对应的所有资源。

| API | 资源描述 |
|---|---|
| ModifyVpnGatewayAttribute | acs:vpc:$regionid:$accountid:vpngateway/$vpngatewayid |
| DescribeVpnGateways | acs:vpc:$regionid:$accountid:vpngateway/* |
| DescribeVpnGateway | acs:vpc:$regionid:$accountid:vpngateway/$vpngatewayid |
| DeleteVpnGateway | acs:vpc:$regionid:$accountid:vpngateway/$vpngatewayid |
| CreateCustomerGateway | acs:vpc:$regionid:$accountid:customergateway/* |
| DeleteCustomerGateway | acs:vpc:$regionid:$accountid:customergateway/$customergatewayid |
| DescribeCustomerGateway | acs:vpc:$regionid:$accountid:customergateway/$customergatewayid |
| DescribeCustomerGateways | acs:vpc:$regionid:$accountid:customergateway/* |
| ModifyCustomerGatewayAttribute | acs:vpc:$regionid:$accountid:customergateway/$customergatewayid |

| CreateVpnConnection | acs:vpc:$regionid:$accountid:vpnconnection/* |
|---|---|
| DeleteVpnConnection | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |
| DescribeVpnConnection | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |
| DescribeVpnConnections | acs:vpc:$regionid:$accountid:vpnconnection/* |
| ModifyVpnConnectionAttribute | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |
| DownloadVpnConnectionConfig | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |

#### 6.2.5. 公共参数

公共参数包括为公共请求参数和公共返回参数。

**公共请求参数**

公共请求参数是每个接口都需要使用到的请求参数，公共请求参数如下表所示。

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回消息的格式。取值： JSON（默认值）\| XML |
| Version | String | 是 | API版本号，使用 YYYY-MM-DD 日期格式。取值： 2016-04-28 |
| AccessKeyId | String | 是 | 访问服务使用的密钥ID。 |
| Signature | String | 是 | 签名结果串。 |
| SignatureMethod | String | 是 | 签名方式，取值： HMAC-SHA1 |
| Timestamp | String | 是 | 请求的时间戳，为日期格式。使用UTC时间按照ISO8601标准，格式为 YYYY-MM-DDThh:mm:ssZ 。 例如，北京时间2022年01月10日09点00分00秒表示为2022-01-10T01:00:00Z。 |
| SignatureVersion | String | 是 | 签名算法版本，取值： 1.0 |
| SignatureNonce | String | 是 | 唯一随机数，用于防止网络重放攻击。 在不同请求中要使用不同的随机数值。 |

**公共返回参数**

API返回结果采用统一格式，返回2xx HTTP状态码代表调用成功；返回4xx或5xx HTTP状态码代表调用失败。调用成功返回的数据格式有XML和JSON两种，可以在发送请求时指定返回的数据格式，默认为JSON格式。 每次调用接口，无论成功与否，系统都会返回一个唯一识别码**RequestId**。 XML格式

```xml
<?xml version="1.0" encoding="utf-8"?>
```

<!--结果的根结点`-->` <接口名称`+Response>` <!--返回请求标签`-->`

```xml
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
```

<!--返回结果数据`-->` `</`接口名称`+Response>` JSON格式

```json
{
    "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
```

`/*`返回结果数据`*/`

```
}
```

### VPN网关

#### 6.3.1. CreateVpnGateway

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateVpnGateway | 要执行的操作，取值：CreateVpnGateway。 |
| Bandwidth | Integer | 是 | 5 | VPN网关的公网带宽，单位Mbps。 取值：5、10、20、50、100。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN网关所在的地域ID。您可以通过调用DescribeRegions接口获取地域ID。 |
| VpcId | String | 是 | vpc-bp1ub1yt9cvakoelj**** | VPN网关所属的VPC的ID。 |
| EnableIpsec | Boolean | 否 | true | 是否开启IPsec-VPN功能，取值： true：开启IPsec-VPN功能。 false（默认值）：不开启IPsec-VPN功能。 |
| EnableSsl | Boolean | 否 | true | 是否开启SSL-VPN功能，取值： true：开启SSL-VPN功能。 false（默认值）：不开启SSL-VPN功能。 |
| Name | String | 否 | MYVPN | VPN网关的名称，默认值为VPN网关的ID。 长度为2~128个英文或中文字符，必须以大小字母或中文开头，可包含数字、下划线（_）和短划线（-），不能以 http:// 或 https:// 开头。 |
| SslConnections | Integer | 否 | 5 | 允许同时连接的最大客户端数量，取值：5、10、20。 |
| VSwitchId | String | 否 | vsw-bp1j5miw2bae9s2vt**** | VPN网关所属的交换机的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Name | String | myVpn | VPN网关的名称。 |
| RequestId | String | 54B48E3D-DF70-471B-AA93- 08E683A1B457 | 请求ID。 |
| VpnGatewayId | String | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关的ID。 |

**示例**

请求示例

```
http(s)://vpc.example.com/?Action=CreateVpnGateway &Bandwidth=5 &RegionId=cn-qingdao-env66-d01 &VpcId=vpc-bp1ub1yt9cvakoelj****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateVpnGatewayResponse> <Name>myVpn</Name> <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId> <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId> </CreateVpnGatewayResponse> |  |

| JSON | 格式 |
|---|---|
| { "CreateVpnGatewayResponse":{ "Name":"myVpn", "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****", "RequestId":"54B48E3D-DF70-471B-AA93-08E683A1B457" } } |  |

#### 6.3.2. ModifyVpnGatewayAttribute

调用ModifyVpnGatewayAttribute接口修改VPN网关的名称和描述信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyVpnGatewayAttribute | 要执行的操作。 取值： ModifyVpnGatewayAttribute。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN网关实例所在的地域ID。 您可以通过调用DescribeRegions接口获取地域ID。 |
| VpnGatewayId | String | 是 | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关实例的ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大不值过64个 ASCII字符。 |
| Description | String | 否 | vpn网关 | VPN网关的描述信息。 长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| Name | String | 否 | myvpn | VPN网关的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VpnGatewayId | String | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关实例的ID。 |
| VpcId | String | vpc-bp1ub1yt9cvakoel**** | VPN网关实例所属VPC的ID。 |
| VSwitchId | String | vsw-bp1y9ovl1cu9ou4tv**** | VPN网关实例所属交换机的ID。 |
| InternetIp | String | 116.XX.XX.69 | VP网关实例的公网IP地址。 |
| CreateTime | Long | 1492753580000 | VPN网关实例的创建时间戳。 |
| EndTime | Long | 1495382400000 | VPN网关实例的到期时间戳。 |
| Spec | String | 5 Mbps | VPN网关实例的规格。 |
| Name | String | test | VPN网关实例的名称。 |
| Description | String | test | VPN网关实例的描述信息。 |
| Status | String | active | VPN网关的状态。 |
| IntranetIp | String | 172.XX.XX.104 | VPN网关的私网IP。 |
| RequestId | String | 54B48E3D-DF70-471B-AA93- 08E683A1B457 | 请求ID。 |

**示例**

请求示例

```
https://vpc.example.com/?Action=ModifyVpnGatewayAttribute &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <Name>aaa</Name>
      <Status>active</Status>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <Spec>5M</Spec>
      <CreateTime>1492753580000</CreateTime>
      <IntranetIp>172.XX.XX.104</IntranetIp>
      <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
      <InternetIp>116.XX.XX.69</InternetIp>
      <EndTime>1495382400000</EndTime>
      <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
      <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
```

| JSON | 格式 |
|---|---|
| { "Name":"aaa", "Status":"active", "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****", "Spec":"5M", "RequestId":"BA56EAF8-E3A9-4BE6-8511-8F03512153E2", "IntranetIp":"172.XX.XX.104", "CreateTime":1492753580000, "InternetIp":"116.XX.XX.69", "EndTime":1495382400000, "VSwitchId":"vsw-bp1y9ovl1cu9ou4tv****", "VpcId":"vpc-bp1ub1yt9cvakoelj****" } |  |

#### 6.3.3. DescribeVpnGateways

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVpnGateways | 要执行的操作。 取值：DescribeVpnGateways。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpcId | String | 否 | vpc-bp1ub1yt9cvakoelj**** | VPN网关所属VPC的ID。 |
| VpnGatewayId | String | 否 | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关的ID。 |
| Status | String | 否 | init | VPN网关的状态，取值： init ：初始化。 provisioning：准备中。 active ：正常。 updating ：更新中。 deleting ：删除中。 |
| BusinessStatus | String | 否 | Normal | VPN网关的付费状态。取值： Normal ：正常。 FinancialLocked：欠费锁定。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VpnGateways | Array of VpnGateway |  | VPN网关的详细信息。 |
| VpnGateway |  |  |  |
| VpnGatewayId | String | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关的ID。 |

| VpcId | String | vpc-bp1ub1yt9cvakoelj**** | VPN网关所属VPC的ID。 |
|---|---|---|---|
| VSwitchId | String | vsw-bp1y9ovl1cu9ou4tv**** | VPN网关所属交换机的ID。 |
| InternetIp | String | 116.XX.XX.69 | VPN网关的公网IP地址。 |
| CreateTime | Long | 1515383700000 | VPN网关的创建时间戳。 |
| EndTime | Long | 1518105600000 | VPN网关的到期时间戳。 |
| Spec | String | 5 Mbps | VPN网关的带宽峰值。 |
| Name | String | test | VPN网关的名称。 |
| Description | String | test | VPN网关的描述。 |
| Status | String | active | VPN网关的状态。 |
| BusinessStatus | String | Normal | VPN网关的付费状态。 |
| ChargeType | String | Prepay | 计费类型。取值：PostpayByFlow。 |
| IpsecVpn | String | enable | 是否开启了IPSec-VPN功能。 enable：已开启。 disable：未开启。 |
| SslMaxConnections | Long | 5 | 允许连接的最大SSL-VPN客户端。 |
| SslVpn | String | enable | 是否开启了SSL-VPN功能。 enable：已开启。 disable：未开启。 |
| Tag | String | 1 | 标签。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 当前分页包含的条目数。 |
| RequestId | String | DF11D6F6-E35A-41C3-9B20- 6FC8A901FE65 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVpnGateways &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <VpnGateways>
            <VpnGateway>
                  <Status>active</Status>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <BusinessStatus>Normal</BusinessStatus>
                  <Spec>5M</Spec>
                  <CreateTime>1492753580000</CreateTime>
                  <InternetIp>116.XX.XX.69</InternetIp>
                  <EndTime>1495382400000</EndTime>
                  <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
                  <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
            </VpnGateway>
      </VpnGateways>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
```

| JSON | 格式 |
|---|---|
| { "PageNumber": 1, "TotalCount": 1, "VpnGateways": { "VpnGateway": [ { "Status": "active", "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****", "BusinessStatus": "Normal", "Spec": "5M", "CreateTime": 1492753580000, "InternetIp": "116.XX.XX.69", "EndTime": 1495382400000, "VSwitchId": "vsw-bp1y9ovl1cu9ou4tv****", "VpcId": "vpc-bp1ub1yt9cvakoelj****" } ] }, "PageSize": 10, "RequestId": "B2CD1315-CA2B-47B1-9DA5-8F1D69C48E82" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |

#### 6.3.4. DescribeVpnGateway

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVpnGateway | 要执行的操作，取值：DescribeVpnGateway。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnGatewayId | String | 是 | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VpnGatewayId | String | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关的ID。 |
| VpcId | String | vpc-bp1ub1yt9cvakoelj**** | VPN网关所属VPC的ID。 |
| VSwitchId | String | vsw-bp1y9ovl1cu9ou4tv**** | VPN网关所属交换机的ID。 |

| InternetIp | String | 116.XX.XX.222 | 公网IP地址。 |
|---|---|---|---|
| CreateTime | Long | 1495382400000 | VPN网关的创建时间戳。 |
| EndTime | Long | 1495382400000 | VPN网关的到期时间戳。 |
| Spec | String | 5M | VPN网关的带宽规格。单位：Mbps。 |
| Name | String | vpngatewayname | VPN网关的名称。 |
| Description | String | vpngatewaydescription | VPN网关的描述信息。 |
| Status | String | init | VPN网关的状态。 init ：初始化。 provisioning ：准备中。 active ：正常。 updating ：更新中。 deleting ：删除中。 |
| BusinessStatus | String | Normal | VPN网关的付费状态。 Normal：正常。 FinancialLocked：欠费锁定。 |
| ChargeType | String | PostpayByFlow | 付费类型。取值：PostpayByFlow。 |
| IpsecVpn | String | enable | 是否开启了IPsec-VPN功能。 enable：已开启。 disable：未开启。 |
| RequestId | String | E98A9651-7098-40C7-8F85- C818D1EBBA85 | 请求ID。 |
| SslMaxConnections | Long | 5 | 最大SSL-VPN并发连接用户数的规格。 |
| SslVpn | String | enable | 是否开启了SSL-VPN功能。 enable：已开启。 disable：未开启。 |
| Tag | String | tag1 | VPN网关标签。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVpnGateway &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeVpnGatewayResponse> <Status>active</Status> <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId> <Spec>5M</Spec> <BusinessStatus>Normal</BusinessStatus> <RequestId>E98A9651-7098-40C7-8F85-C818D1EBBA85</RequestId> <CreateTime>1492753580000</CreateTime> <InternetIp>116.XX.XX.222</InternetIp> <EndTime>1495382400000</EndTime> <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId> <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId> </DescribeVpnGatewayResponse> |  |

`JSON` 格式

```json
{
    "Status": "active",
    "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
    "BusinessStatus": "Normal",
    "Spec": "5M",
    "CreateTime": 1492753580000,
    "RequestId": "E98A9651-7098-40C7-8F85-C818D1EBBA85",
    "InternetIp": "116.XX.XX.222",
    "EndTime": 1495382400000,
    "VSwitchId": "vsw-bp1y9ovl1cu9ou4tv****",
    "VpcId": "vpc-bp1ub1yt9cvakoelj****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |

#### 6.3.5. DeleteVpnGateway

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteVpnGateway | 要执行的操作。 取值：DeleteVpnGateway。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN网关实例所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnGatewayId | String | 是 | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关实例的ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大不值过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23-88ED- E11ED28DCAC0 | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteNatGatewayResponse> <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId> </DeleteNatGatewayResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 403 | ForbiddenRelease | Forbidden to release a prepaid instance within validity period | 不允许在合同期内释放预付费实例。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.Configuring | The specified VPN gateway is being configured. | VPN网关正在配置中。 |

#### 6.3.6. DescribeRegions

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRegions | 要执行的操作，取值：DescribeRegions。 |
| ProductType | String | 否 | ECS | 云产品类型。 |
| AcceptLanguage | String | 否 | zh-CN | 返回值语言，取值： zh-CN（默认值）：中文。 en-US：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Regions | Array of Region |  | 可用地域的集合。 |
| Region |  |  |  |
| LocalName | String | 华北 1 | 地域名称。 |
| RegionEndpoint | String | vpc.aliyuncs.com | 地域服务的Endpoint。 |
| RegionId | String | cn-qingdao-env17-d01 | 地域ID。 |
| RequestId | String | 611CB80C-B6A9-43DB-9E38- 0B0AC3D9B58F | 请求ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeRegionsResponse> <RequestId>611CB80C-B6A9-43DB-9E38-0B0AC3D9B58F</RequestId> <Regions> <RegionId>cn-qingdao-env17-d01</RegionId> <RegionEndpoint>vpc.aliyuncs.com</RegionEndpoint> <LocalName>华北 1</LocalName> </Regions> </DescribeRegionsResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "611CB80C-B6A9-43DB-9E38-0B0AC3D9B58F", "Regions": { "RegionId": "cn-qingdao-env17-d01", "RegionEndpoint": "vpc.aliyuncs.com", "LocalName": "华北 1" } } |  |

### 用户网关

#### 6.4.1. CreateCustomerGateway

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateCustomerGateway | 要执行的操作。 取值：CreateCustomerGateway。 |
| IpAddress | String | 是 | 116.XX.XX.222 | 用户网关的IP地址。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 用户网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| Name | String | 否 | Gateway | 用户网关的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
| Description | String | 否 | Gateway | 用户网关的描述信息。 描述在2~256个字符之间，以大小写字母或中文开始，可包含数字、短划线（-）、下划线（_）、全角句号（。）、全角逗号（，）和全角冒号（：），但不能以 http:// 或 https:// 开头。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CustomerGatewayId | String | cgw-bp1aw0a5nfff03xp1**** | 用户网关的ID。 |
| IpAddress | String | 100.XX.XX.1 | 用户网关的IP地址。 |
| Name | String | test | 用户网关的名称。 |
| Description | String | test | 用户网关的描述信息。 |
| CreateTime | Long | 1493363486000 | 创建用户网关的时间戳。 |
| RequestId | String | cgw-bp1aw0a5nfff03xp1pcqc | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateCustomerGateway &IpAddress=116.XX.XX.222 &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateCustomerGatewayResponse> <CustomerGatewayId>cgw-bp1aw0a5nfff03xp****</CustomerGatewayId> <RequestId>185E81B1-3916-4667-B48F-C52409B33F2B</RequestId> <CreateTime>1493363486000</CreateTime> <IpAddress>100.XX.XX.1</IpAddress> </CreateCustomerGatewayResponse> |  |

`JSON` 格式

```json
{
    "CustomerGatewayId": "cgw-bp1jrawp82av6bws9****",
    "CreateTime": 1493363599000,
    "RequestId": "D32B3C26-6C6C-4988-93E9-D2A6444CE6AE",
    "IpAddress": "100.XX.XX.1"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | InvalidIpAddress.AlreadyExist | Specified IpAddress is already exist. | 该IP已经存在，原因是同一个用户在同一个region内，IP不可重复。 |
| 400 | InvalidIpAddress.WrongFormat | Specified IpAddress is invalid. | 该IP不合法。 |
| 400 | InvalidName | The name is not valid | 该名称格式不合法。 |
| 400 | InvalidDescription | The description is not valid | 描述格式不合法。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |

#### 6.4.2. ModifyCustomerGatewayAttribute

调用ModifyCustomerGatewayAttribute接口修改用户网关的名称和描述信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyCustomerGatewayAttri bute | 要执行的操作。 取值： ModifyCustomerGatewayAttribute。 |
| CustomerGatewayId | String | 是 | vpn-bp1q8bgx4xnkm2ogj**** | 用户网关的ID。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 用户网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| Name | String | 否 | test | 用户网关的名称。 长度为2~128个字符，必须以大小写字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
| Description | String | 否 | test | 用户网关的描述信息。 描述在2~256个字符之间，以大小写字母或中文开始，可包含数字、短划线（-）、下划线（_）、全角句号（。）、全角逗号（，）和全角冒号（：），但不能以 http:// 或 https:// 开头。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CustomerGatewayId | String | cgw-bp1pvpl9r9adju6l5**** | 用户网关的ID。 |
| Name | String | test | 用户网关的名称。 |
| Description | String | test | 用户网关的描述信息。 |
| IpAddress | String | 139.XX.XX.55 | 用户网关的IP地址。 |
| CreateTime | Long | 1492747187000 | 创建用户网关的时间戳。 |
| RequestId | String | E61293C8-AF07-4E87-A272- 542680038F93 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyCustomerGatewayAttribute &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyCustomerGatewayAttributeResponse> <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId> <RequestId>E61293C8-AF07-4E87-A272-542680038F93</RequestId> <CreateTime>1492747187000</CreateTime> <IpAddress>139.XX.XX.55</IpAddress> <Description>modify</Description> </ModifyCustomerGatewayAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****", "RequestId": "8AA5CE21-2E6A-4530-BDF5-F055849476E6", "CreateTime": 1492747187000, "IpAddress": "139.XX.XX.55", "Description": "modify" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 404 | InvalidCustomerGatewayInstance Id.NotFound | The specified customer gateway instance id does not exist. | 指定的 Instance 不存在，请您检查 Instance 是否正确。 |
| 400 | InvalidName | The name is not valid | 该名称格式不合法。 |
| 400 | InvalidDescription | The description is not valid | 描述格式不合法。 |

#### 6.4.3. DescribeCustomerGateways

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCustomerGateways | 系统规定参数。取值：DescribeCustomerGateways。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 用户网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| CustomerGatewayId | String | 否 | cgw-bp1pvpl9r9adju6l5**** | 用户网关的ID。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CustomerGateways | Array of CustomerGateway |  | 用户网关的详细信息。 |
| CustomerGateway |  |  |  |
| CustomerGatewayId | String | cgw-bp1pvpl9r9adju6l5**** | 用户网关的ID。 |
| Name | String | test | 用户网关的名称。 |
| Description | String | test | 用户网关的描述信息。 |

| IpAddress | String | 139.XX.XX.55 | 用户网关的IP地址。 |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | 创建用户网关的时间戳。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| PageSize | Integer | 10 | 分页查询时每页的条目数。 |
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCustomerGateways &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeCustomerGatewaysResponse> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId> <CustomerGateways> <CustomerGateway> <Name>test</Name> <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId> <CreateTime>1492747187000</CreateTime> <IpAddress>139.XX.XX.55</IpAddress> </CustomerGateway> </CustomerGateways> </DescribeCustomerGatewaysResponse> |  |

| JSON | 格式 |
|---|---|
| { "PageNumber": 1, "TotalCount": 1, "PageSize": 10, "RequestId": "E82612A9-CB90-4D7E-B394-1DB7F6509B29", "CustomerGateways": { "CustomerGateway": [ { "Name": "test", "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****", "CreateTime": 1492747187000, "IpAddress": "139.XX.XX.55" } ] } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请申请权限后再操作。 |

#### 6.4.4. DescribeCustomerGateway

调用DescribeCustomerGateway接口查询已创建的用户网关的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCustomerGateway | 系统规定参数。 取值： DescribeCustomerGateway。 |

| CustomerGatewayId | String | 是 | cgw-bp1pvpl9r9adju6l5**** | 用户网关的ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao-env66-d01 | 用户网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CustomerGatewayId | String | cgw-bp1pvpl9r9adju6l5**** | 用户网关的ID。 |
| Name | String | test | 用户网关的名称。 |
| Description | String | test | 用户网关的描述信息。 |
| IpAddress | String | 139.XX.XX.32 | 用户网关的IP地址。 |
| RequestId | String | 99506ECB-218F-45A5-AE8E- 79518451F615 | 请求ID。 |
| CreateTime | Long | 1492747187000 | 创建用户网关的时间戳。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeCustomerGatewayResponse> <Name>test</Name> <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId> <CreateTime>1492747187000</CreateTime> <RequestId>99506ECB-218F-45A5-AE8E-79518451F615</RequestId> <IpAddress>139.XX.XX.32</IpAddress> </DescribeCustomerGatewayResponse> |  |

| JSON | 格式 |
|---|---|
| { "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****", "Name": "test", "RequestId": "A0457BC9-6C0F-4437-AB9D-FB2EABC1D6A2", "CreateTime": 1492747187000, "IpAddress": "139.XX.XX.32" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请申请权限后再操作。 |
| 404 | InvalidCustomerGatewayInstance Id.NotFound | The specified customer gateway instance id does not exist. | 指定的用户网关实例不存在，请您检查用户网关实例ID是否正确。 |

#### 6.4.5. DeleteCustomerGateway

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteCustomerGateway | 要执行的操作，取值：DeleteCustomerGateway。 |
| CustomerGatewayId | String | 是 | cgw-2zllmw9lqrcdis3bd**** | 用户网关的ID。 |

| RegionId | String | 是 | cn-qingdao-env66-d01 | 用户网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
|---|---|---|---|---|
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE-8316- ACA81BB230DA | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteCustomerGatewayResesponse> <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId> </DeleteCustomerGatewayResesponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 404 | InvalidCustomerGatewayInstance Id.NotFound | The specified customer gateway instance id does not exist. | 指定的 Instance 不存在，请您检查 Instance 是否正确。 |

### VPN网关路由

#### 6.5.1. CreateVpnRouteEntry

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateVpnRouteEntry | 要执行的操作，取值：CreateVpnRouteEntry。 |
| NextHop | String | 是 | vco-bp15oes1py4i66rmd**** | 目的路由的下一跳。 |
| PublishVpc | Boolean | 是 | true | 是否发布目的路由到VPC，取值： true：发布目的路由到VPC。 false：不发布目的路由到VPC。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN目的路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouteDest | String | 是 | 10.0.0.0/24 | 目的路由的目标网段。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |

| Weight | Integer | 是 | 0 | 目的路由的权重值，取值： 0：低优先级。 100：高优先级。 说明相同目标网段的目的路由，不支持同时设置权重值为 100。 |
|---|---|---|---|---|
| ClientToken | String | 否 | d7d24a21-f4ba-4454-9173- b3828dae492b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| Description | String | 否 | mytest | VPN目的路由的描述信息。 |
| OverlayMode | String | 否 | Ipsec | 覆盖模式。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | 创建VPN目的路由的时间戳。 |
| Description | String | mytest | VPN目的路由的描述信息。 |
| NextHop | String | vco-bp15oes1py4i66rmd**** | 目的路由的下一跳。 |
| OverlayMode | String | Ipsec | 覆盖模式。 |
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |
| RouteDest | String | 10.0.0.0/24 | 目的路由的目标网段。 |
| State | String | published | VPN目的路由的状态。 published：已发布。 normal：未发布。 |
| VpnInstanceId | String | vpn-bp1cmw7jh1nfe43m9**** | VPN网关的ID。 |
| Weight | Integer | 0 | 目的路由的权重值，取值：0或100。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateVpnRouteEntryResponse> <RouteDest>10.0.0.0/24</RouteDest> <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId> <OverlayMode>Ipsec</OverlayMode> <State>published</State> <Weight>100</Weight> <CreateTime>1563873294331</CreateTime> <NextHop>vco-bp1tui07ob10fmuro****</NextHop> <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId> </CreateVpnRouteEntryResponse> |  |

`JSON` 格式

```json
{
    "RouteDest": "10.0.0.0/24",
    "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
    "OverlayMode": "Ipsec",
    "State": "published",
    "Weight": 100,
    "CreateTime": 1563873294331,
    "NextHop": "vco-bp1tui07ob10fmuro****",
    "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.5.2. ModifyVpnRouteEntryWeight

调用ModifyVpnRouteEntryWeight修改VPN目的路由的权重值。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyVpnRouteEntryWeight | 要执行的操作，取值：ModifyVpnRouteEntryWeight。 |
| NewWeight | Integer | 是 | 100 | 要设置的权重值，取值： 0：低优先级。 100：高优先级。 说明相同目标网段的目的路由，不支持同时设置权重值为 100。 |
| NextHop | String | 是 | vco-bp15oes1py4i66rmd**** | 目的路由的下一跳。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN目的路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouteDest | String | 是 | 10.0.0.0/24 | 目的路由的目标网段。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |
| Weight | Integer | 是 | 0 | VPN目的路由在修改之前设置的权重值，取值：0或100。 |
| ClientToken | String | 否 | d7d24a21-f4ba-4454-9173- b3828dae492b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| OverlayMode | String | 否 | Ipsec | 覆盖模式，取值：Ipsec（IPsec隧道协议）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyVpnRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyVpnRouteEntryWeightResponse> <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId> </ModifyVpnRouteEntryWeightResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "E82612A9-CB90-4D7E-B394-1DB7F6509B29" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.5.3. DeleteVpnRouteEntry

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteVpnRouteEntry | 要执行的操作，取值：DeleteVpnRouteEntry。 |
| NextHop | String | 是 | vco-bp15oes1py4i66rmd**** | 目的路由的下一跳。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN目的路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouteDest | String | 是 | 10.0.0.0/24 | 目的路由的目标网段。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |
| Weight | Integer | 是 | 0 | 目的路由的权重值，取值： 0：低优先级。 100：高优先级。 说明相同目标网段的目的路由，不支持同时设置权重值为 100。 |
| ClientToken | String | 否 | d7d24a21-f4ba-4454-9173- b3828dae492b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| OverlayMode | String | 否 | Ipsec | 覆盖模式，取值：Ipsec（IPsec隧道协议）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteVpnRouteEntryResponse> <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId> </DeleteVpnRouteEntryResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.5.4. DescribeVpnRouteEntries

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVpnRouteEntries | 要执行的操作，取值：DescribeVpnRouteEntries。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN目的路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 10 | 当前页码。 |
| PageSize | Integer | 10 | 每页包含的条目数。 |
| RequestId | String | 0ED8D006-F706-4D23-88ED- E11ED28DCAC0 | 请求ID。 |
| TotalCount | Integer | 10 | 列表条目数。 |

| VpnRouteEntries | Array of VpnRouteEntry |  | VPN目的路由的详细信息。 |
|---|---|---|---|
| VpnRouteEntry |  |  |  |
| CreateTime | Long | 1492747187000 | 创建VPN目的路由的时间戳。 |
| NextHop | String | vco-bp15oes1py4i66rmd**** | 目的路由的下一跳。 |
| RouteDest | String | 10.0.0.0/24 | 目的路由的目标网段。 |
| State | String | published | VPN目的路由的状态。 published：已发布。 normal：未发布。 |
| VpnInstanceId | String | vpn-bp1cmw7jh1nfe43m9**** | VPN网关的ID。 |
| Weight | Integer | 0 | 目的路由的权重值，取值： 0：低优先级。 100：高优先级。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVpnRouteEntries &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeVpnRouteEntriesResponse> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> <VpnRouteEntries> <VpnRouteEntry> <RouteDest>10.0.0.0/24</RouteDest> <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId> <State>normal</State> <Weight>100</Weight> <CreateTime>1563874074000</CreateTime> <NextHop>vco-bp1tui07ob10fmuro****</NextHop> </VpnRouteEntry> </VpnRouteEntries> <PageSize>10</PageSize> <RequestId>BF3995A6-FA4F-4C74-B90F-89ECF4BFF4D5</RequestId> </DescribeVpnRouteEntriesResponse> |  |

| JSON | 格式 |
|---|---|
| { "PageNumber": 1, "TotalCount": 1, "VpnRouteEntries": { "VpnRouteEntry": [ { "RouteDest": "10.0.0.0/24", "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****", "State": "normal", "Weight": 100, "CreateTime": 1563874074000, "NextHop": "vco-bp1tui07ob10fmuro****" } ] }, "PageSize": 10, "RequestId": "BF3995A6-FA4F-4C74-B90F-89ECF4BFF4D5" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |

#### 6.5.5. PublishVpnRouteEntry

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | PublishVpnRouteEntry | 要执行的操作，取值：PublishVpnRouteEntry。 |
| NextHop | String | 是 | vco-bp15oes1py4i66rmd**** | VPN路由的下一跳。 |
| PublishVpc | Boolean | 是 | true | 是否发布VPN路由到VPC，取值： true：发布VPN路由到VPC。 false：不发布VPN路由到VPC。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouteDest | String | 是 | 10.0.0.0/24 | VPN路由的目标网段。 |
| RouteType | String | 是 | pbr | VPN路由类型，取值： pbr：策略路由。 dbr：目的路由。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |
| ClientToken | String | 否 | d7d24a21-f4ba-4454-9173- b3828dae492b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=PublishVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteType=pbr &VpnGatewayId=vpn-bp1a3kqjiiq9legfx****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <PublishVpnRouteEntryResponse> <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId> </PublishVpnRouteEntryResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |

| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
|---|---|---|---|
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.5.6. CreateVpnPbrRouteEntry

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateVpnPbrRouteEntry | 要执行的操作，取值：CreateVpnPbrRouteEntry。 |
| NextHop | String | 是 | vco-bp15oes1py4i66rmd**** | 策略路由的下一跳。 |
| PublishVpc | Boolean | 是 | true | 是否发布策略路由到VPC，取值： true：发布策略路由到VPC。 false：不发布策略路由到VPC。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN策略路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouteDest | String | 是 | 10.0.0.0/24 | 策略路由的目标网段。 |
| RouteSource | String | 是 | 192.168.1.0/24 | 策略路由的源网段。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |
| Weight | Integer | 是 | 0 | 策略路由的权重值，取值： 0：低优先级。 100：高优先级。 说明相同目标网段的策略路由，不支持同时设置权重值为 100。 |
| ClientToken | String | 否 | d7d24a21-f4ba-4454-9173- b3828dae492b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| Description | String | 否 | vpnroute1 | 策略路由的描述信息。 |
| OverlayMode | String | 否 | Ipsec | 覆盖模式。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | 创建VPN策略路由的时间戳。 |
| Description | String | vpnroute1 | 策略路由的描述信息。 |
| NextHop | String | vco-bp15oes1py4i66rmd**** | 策略路由的下一跳。 |
| OverlayMode | String | Ipsec | 覆盖模式。 |
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |
| RouteDest | String | 10.0.0.0/24 | 策略路由的目标网段。 |
| RouteSource | String | 192.168.1.0/24 | 策略路由的源网段。 |
| State | String | normal | 策略路由的状态，取值： published：已发布。 normal：未发布。 |
| VpnInstanceId | String | vpn-bp1cmw7jh1nfe43m9**** | VPN网关的ID。 |

| Weight | Integer | 0 | 策略路由的权重值，取值：0或100。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateVpnPbrRouteEntryResponse> <RouteDest>10.0.0.0/24</RouteDest> <RouteSource>192.168.1.0/24</RouteSource> <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId> <OverlayMode>Ipsec</OverlayMode> <State>published</State> <Weight>100</Weight> <CreateTime>1563873294331</CreateTime> <NextHop>vco-bp1tui07ob10fmuro****</NextHop> </CreateVpnPbrRouteEntryResponse> |  |

| JSON | 格式 |
|---|---|
| { "RouteDest": "10.0.0.0/24", "RouteSource": "192.168.1.0/24", "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****", "OverlayMode": "Ipsec", "State": "published", "Weight": 100, "CreateTime": 1563873294331, "NextHop": "vco-bp1tui07ob10fmuro****" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.5.7. ModifyVpnPbrRouteEntryWeight

调用ModifyVpnPbrRouteEntryWeight接口修改VPN策略路由的权重值。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyVpnPbrRouteEntryWei ght | 要执行的操作，取值：ModifyVpnPbrRouteEntryWeight。 |
| NewWeight | Integer | 是 | 100 | 要设置的权重值，取值： 0：低优先级。 100：高优先级。 说明相同目标网段的策略路由，不支持同时设置权重值为 100。 |
| NextHop | String | 是 | vco-bp15oes1py4i66rmd**** | 策略路由的下一跳。 |

| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN策略路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
|---|---|---|---|---|
| RouteDest | String | 是 | 10.0.0.0/24 | 策略路由的目标网段。 |
| RouteSource | String | 是 | 192.168.1.0/24 | 策略路由的源网段。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |
| Weight | Integer | 是 | 0 | VPN策略路由在修改之前设置的权重值，取值：0或100。 |
| ClientToken | String | 否 | d7d24a21-f4ba-4454-9173- b3828dae492b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| OverlayMode | String | 否 | Ipsec | 覆盖模式，取值：Ipsec（IPsec隧道协议）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyVpnPbrRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyVpnPbrRouteEntryWeightResponse> <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId> </ModifyVpnPbrRouteEntryWeightResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.5.8. DeleteVpnPbrRouteEntry

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DeleteVpnPbrRouteEntry | 要执行的操作，取值：DeleteVpnPbrRouteEntry。 |
|---|---|---|---|---|
| NextHop | String | 是 | vco-bp15oes1py4i66rmd**** | 策略路由的下一跳。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN策略路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RouteDest | String | 是 | 10.0.0.0/24 | 策略路由的目标网段。 |
| RouteSource | String | 是 | 192.168.1.0/24 | 策略路由的源网段。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |
| Weight | Integer | 是 | 0 | 策略路由的权重值，取值： 0：低优先级。 100：高优先级。 说明相同目的网段的策略路由，不支持同时设置权重值为 100。 |
| ClientToken | String | 否 | d7d24a21-f4ba-4454-9173- b3828dae492b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| OverlayMode | String | 否 | Ipsec | 覆盖模式，取值：Ipsec（IPsec隧道协议）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteVpnPbrRouteEntryResponse> <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId> </DeleteVpnPbrRouteEntryResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.5.9. DescribeVpnPbrRouteEntries

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVpnPbrRouteEntries | 要执行的操作，取值：DescribeVpnPbrRouteEntries。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN策略路由所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnGatewayId | String | 是 | vpn-bp1a3kqjiiq9legfx**** | VPN网关的ID。 |
| PageNumber | Integer | 否 | 10 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页包含的条目数。 |
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |
| TotalCount | Integer | 12 | 列表条目数。 |
| VpnPbrRouteEntries | Array of VpnPbrRouteEntry |  | VPN策略路由的详细信息。 |
| VpnPbrRouteEntry |  |  |  |
| CreateTime | Long | 1492747187000 | 创建VPN策略路由的时间戳。 |
| NextHop | String | vco-bp15oes1py4i66rmd**** | 策略路由的下一跳。 |
| RouteDest | String | 10.0.0.0/24 | 策略路由的目标网段。 |
| RouteSource | String | 192.xx.0.0/24 | 策略路由的源网段。 |
| State | String | published | VPN策略路由的状态，取值： published：已发布。 normal：未发布。 |
| VpnInstanceId | String | vpn-bp1cmw7jh1nfe43m9**** | VPN网关的ID。 |
| Weight | Integer | 0 | 策略路由的权重值，取值： 0：低优先级。 100：高优先级。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVpnPbrRouteEntries &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
   <RequestId>E5D94DC7-AEC7-4E73-A203-61B04D1F1160</RequestId>
   <PageSize>10</PageSize>
   <VpnPbrRouteEntries>
      <VpnPbrRouteEntry>
         <RouteDest>10.0.0.0/32</RouteDest>
         <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
         <State>published</State>
         <Weight>100</Weight>
         <CreateTime>1563881012000</CreateTime>
         <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
         <RouteSource>11.0.0.0/32</RouteSource>
      </VpnPbrRouteEntry>
   </VpnPbrRouteEntries>
```

| JSON | 格式 |
|---|---|
| { "PageNumber": 1, "TotalCount": 1, "RequestId": "E5D94DC7-AEC7-4E73-A203-61B04D1F1160", "PageSize": 10, "VpnPbrRouteEntries": { "VpnPbrRouteEntry": [ { "RouteDest": "10.0.0.0/32", "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****", "State": "published", "Weight": 100, "CreateTime": 1563881012000, "NextHop": "vco-bp1tui07ob10fmuro****", "RouteSource": "11.0.0.0/32" } ] } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |

### IPsec-VPN

#### 6.6.1. CreateVpnConnection

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateVpnConnection | 要执行的操作，取值：CreateVpnConnection。 |
| CustomerGatewayId | String | 是 | vpn-bp1q8bgx4xnk**** | 用户网关的ID。 |
| LocalSubnet | String | 是 | 10.1.1.0/24,10.1.2.0/24 | 需要和本地IDC互连的VPC侧的网段，用于第二阶段协商。 多个网段之间用逗号（,）分隔，例如： 192.168.1.0/24,192.168.2.0/24。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。您可以通过调用 DescribeRegions 接口获取地域ID。 |
| RemoteSubnet | String | 是 | 10.10.1.0/24,10.10.2.0/24 | 本地IDC的网段，用于第二阶段协商。 多个网段之间用逗号（,）分隔，例如： 192.168.3.0/24,192.168.4.0/24。 |
| VpnGatewayId | String | 是 | vpn-bp1q8bgx4xnkm**** | VPN网关的ID。 |

| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 001**** | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
|---|---|---|---|---|
| Name | String | 否 | IPsec | IPsec连接的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-），但不能以 http:// 或 https:// 开头。 |
| EffectImmediately | Boolean | 否 | false | 是否删除当前已协商成功的IPsec隧道并重新发起协商。取值： true：配置完成后立即进行协商。 false（默认值）：当有流量进入时进行协商。 |
| IkeConfig | String | 否 | {"IkeVersion":"ikev1","IkeMo de":"main","IkeEncAlg":"aes" ,"IkeAuthAlg":"sha1","IkePfs": "group2","IkeLifetime":86400 } | 第一阶段协商的配置信息： IkeConfig.Psk：用于IPsec VPN网关与用户网关之间的身份认证。默认情况下会随机生成，也可以手动指定密钥。长度限制为100 个字符。 IkeConfig.IkeVersion：IKE协议的版本。取值：ikev1或ikev2，默认值：ikev1。 IkeConfig.IkeMode：IKE V1版本的协商模式。取值：main或aggressive，默认值：main。 IkeConfig.IkeEncAlg：第一阶段协商的加密算法，取值：aes、aes192、aes256、des或3des，默认值：aes。 IkeConfig.IkeAuthAlg：第一阶段协商的认证算法，取值：md5或sha1，默认值：md5。 IkeConfig.IkePfs：第一阶段协商使用的Diffie-Hellman密钥交换算法，取值：group1、group2、group5、group14或group24，默认值：group2。 IkeConfig.IkeLifetime：第一阶段协商出的SA的生存周期。取值范围为0~86400，单位为秒，默认值：86400。 IkeConfig.LocalIdIPsec：VPN网关的标识，长度限制为100个字符，默认值为VPN网关的公网IP地址。 IkeConfig.RemoteId：用户网关的标识，长度限制为100个字符，默认值为用户网关的公网IP地址。 |
| IpsecConfig | String | 否 | {"IpsecEncAlg":"aes","IpsecA uthAlg":"sha1","IpsecPfs":"gr oup2","IpsecLifetime":86400 } | 第二阶段协商的配置信息： IpsecConfig.IpsecEncAlg：第二阶段协商的加密算法，取值：aes、aes192、aes256、des或3des，默认值：aes。 IpsecConfig. IpsecAuthAlg：第二阶段协商的认证算法，取值：md5或sha1，默认值：md5。 IpsecConfig. IpsecPfs：转发所有协议的报文。第二阶段协商使用的Diffie-Hellman密钥交换算法，取值：group1、group2、group5、group14或group24，默认值：group2。 IpsecConfig. IpsecLifetime：第二阶段协商出的SA的生存周期。取值范围为0~86400，单位为秒，默认值：86400。 |
| HealthCheckConfig | String | 否 | {"enable":"true","dip":"192.1 68.xx.2","sip":"192.168.xx.2", "interval":"3","retry":"3"} | 健康检查配置信息： HealthCheckConfig.enable：是否开启健康检查，取值：true 或false（默认值）。 HealthCheckConfig.dip：健康检查的目的IP地址。 HealthCheckConfig.sip：健康检查的源IP地址。 HealthCheckConfig.interval：健康检查的重试间隔时间，单位是秒。 HealthCheckConfig.retry：健康检查的重试发包次数。 |
| AutoConfigRoute | Boolean | 否 | true | 是否自动配置路由，取值： true：自动配置路由。 false（默认值）：不自动配置路由。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VpnConnectionId | String | vco-bp15oes1py4i6**** | IPsec连接的ID。 |
| CreateTime | Long | 1544666102000 | 创建IPsec连接的时间戳。 |
| Name | String | test | IPsec连接的名称。 |
| RequestId | String | 082AD562-B8DB-4BB2-861F- DA1FCA01FD76 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateVpnConnection &CustomerGatewayId=vpn-bp1q8bgx4xnk**** &LocalSubnet=10.1.1.0/24,10.1.2.0/24 &RegionId=cn-qingdao-env66-d01 &RemoteSubnet=10.10.1.0/24,10.10.2.0/24 &VpnGatewayId=vpn-bp1q8bgx4xnkm****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateVpnConnectionResponse> <VpnConnectionId>vco-bp1bbi27hojx8****</VpnConnectionId> <CreateTime>1493363928000</CreateTime> </CreateVpnConnectionResponse> |  |

| JSON | 格式 |
|---|---|
| { "CreateTime": 1544666102000, "VpnConnectionId": "vco-bp15oes1py4i6****" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 404 | InvalidCustomerGatewayInstance Id.NotFound | The specified customer gateway instance id does not exist. | 指定的 Instance 不存在，请您检查 Instance 是否正确。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 400 | InvalidVpnConnection.AlreadyExi sts | Vpn connection already exists. | VPN 连接已经存在，不用再次添加。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.6.2. ModifyVpnConnectionAttribute

调用ModifyVpnConnectionAttribute接口修改IPsec连接的配置信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyVpnConnectionAttribut e | 要执行的操作，取值：ModifyVpnConnectionAttribute。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnConnectionId | String | 是 | vco-bp1bbi27hojx80nck**** | IPsec连接的ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |
| Name | String | 否 | IPsec | IPsec连接的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
| LocalSubnet | String | 否 | 10.1.1.0/24,10.1.2.0/24 | 需要和本地IDC互连的VPC侧的网段，用于第二阶段协商。 多个网段之间用逗号（,）分隔，例如： 192.168.1.0/24,192.168.2.0/24。 |
| RemoteSubnet | String | 否 | 10.10.1.0/24,10.10.2.0/24 | 本地IDC的网段，用于第二阶段协商。 多个网段之间用逗号（,）分隔，例如： 192.168.3.0/24,192.168.4.0/24。 |

| EffectImmediately | Boolean | 否 | false | 是否删除当前已协商成功的IPsec隧道并重新发起协商。取值： true：配置完成后立即进行协商。 false（默认值）：当有流量进入时进行协商。 |
|---|---|---|---|---|
| IkeConfig | String | 否 | {"IkeVersion":"ikev1","IkeMo de":"main","IkeEncAlg":"aes" ,"IkeAuthAlg":"sha1","IkePfs": "group2","IkeLifetime":86400 } | 第一阶段协商的配置信息： IkeConfig.Psk：用于IPsec VPN网关与用户网关之间的身份认证。默认情况下会随机生成，也可以手动指定密钥。长度限制为100 个字符。 IkeConfig.IkeVersion：IKE协议的版本。取值：ikev1或ikev2，默认值：ikev1。 IkeConfig.IkeMode：IKE V1版本的协商模式。取值：main（主模式）或aggressive（野蛮模式），默认值：main。 IkeConfig.IkeEncAlg：第一阶段协商的加密算法，取值：aes、aes192、aes256、des或3des，默认值：aes。 IkeConfig.IkeAuthAlg：第一阶段协商的认证算法，取值：md5或sha1，默认值：sha。 IkeConfig.IkePfs：第一阶段协商使用的Diffie-Hellman密钥交换算法，取值：group1、group2、group5、group14或group24，默认值：group2。 IkeConfig.IkeLifetime：第一阶段协商出的SA的生存周期。取值范围为0~86400，单位为秒，默认值：86400。 IkeConfig.LocalIdIPsec：VPN网关的标识，长度限制为100个字符，默认值为VPN网关的公网IP地址。 IkeConfig.RemoteId：用户网关的标识，长度限制为100个字符，默认值为用户网关的公网IP地址。 |
| IpsecConfig | String | 否 | {"IpsecEncAlg":"aes","IpsecA uthAlg":"sha1","IpsecPfs":"gr oup2","IpsecLifetime":86400 } | 第二阶段协商的配置信息： IpsecConfig.IpsecEncAlg：第二阶段协商的加密算法，取值：aes、aes192、aes256、des或3des，默认值：aes。 IpsecConfig. IpsecAuthAlg：第二阶段协商的认证算法，取值：md5或sha1，默认值：sha1。 IpsecConfig. IpsecPfs：转发所有协议的报文。第一阶段协商使用的Diffie-Hellman密钥交换算法，取值：group1、group2、group5、group14或group24，默认值：group2。 IpsecConfig. IpsecLifetime：第二阶段协商出的SA的生存周期。取值范围为0~86400，单位为秒，默认值：86400。 |
| HealthCheckConfig | String | 否 | {"enable":"true","dip":"192.1 68.xx.2","sip":"192.168.xx.2", "interval":"3","retry":"3"} | 健康检查配置信息： HealthCheckConfig.enable：是否开启健康检查，取值：true 或false（默认值）。 HealthCheckConfig.dip：健康检查的目的IP地址。 HealthCheckConfig.sip：健康检查的源IP地址。 HealthCheckConfig.interval：健康检查的重试间隔时间，单位是秒。 HealthCheckConfig.retry：健康检查的重试发包次数。 |
| AutoConfigRoute | Boolean | 否 | true | 是否自动发布路由，取值： true：自动发布。 false（默认值）：不自动发布。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VpnConnectionId | String | vco-bp1bbi27hojx80nck**** | IPsec连接的ID。 |
| CustomerGatewayId | String | vpn-bp1q8bgx4xnkm2ogj**** | 用户网关的ID。 |
| VpnGatewayId | String | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关的ID。 |
| Name | String | test | IPsec连接的名称。 |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0/24 | VPC侧的网段。 |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2.0/24 | 本地IDC侧的网段。 |
| CreateTime | Long | 1492753817000 | IPsec连接的创建时间戳。 |
| Description | String | description | IPsec描述信息。 |

| EffectImmediately | Boolean | false | IPsec连接是否立即生效。 true：配置完成后立即进行协商。 false：当有流量进入时进行协商。 |
|---|---|---|---|
| IkeConfig | Struct |  | 第一阶段协商的配置。 |
| IkeAuthAlg | String | sha1 | IKE认证算法。 |
| IkeEncAlg | String | aes | IKE加密算法。 |
| IkeLifetime | Long | 86400 | IKE生存时间。 |
| IkeMode | String | main | IKE模式。 |
| IkePfs | String | group2 | DH分组。 |
| IkeVersion | String | ikev1 | IKE版本。 |
| LocalId | String | 116.XX.XX.64 | 本端ID，支持FQDN和IP格式，默认为当前选取的VPN网关IP地址。 |
| Psk | String | pgw6dy7d1i8i**** | 预共享密钥。 |
| RemoteId | String | 139.XX.XX.167 | 对端ID，支持FQDN和IP格式，默认为当前选取的用户网关IP地址。 |
| IpsecConfig | Struct |  | 第二阶段协商的配置。 |
| IpsecAuthAlg | String | sha1 | IPsec认证算法。 |
| IpsecEncAlg | String | aes | IPsec加密算法。 |
| IpsecLifetime | Long | 86400 | IPsec生存时间。 |
| IpsecPfs | String | group2 | DH分组。 |
| RequestId | String | 7DB79D0C-5F27-4AB5-995B- 79BE55102F90 | 请求ID。 |
| VcoHealthCheck | Struct |  | 健康检查配置。 |
| Dip | String | 1.XX.XX.1 | 目标IP。 |
| Enable | String | true | 是否开启健康检查。 true：已开启。 false：未开启。 |
| Interval | Integer | 3 | 健康检查的重试间隔时间，单位是秒。 |
| Retry | Integer | 1 | 健康检查的重试发包次数。 |
| Sip | String | 2.XX.XX.2 | 源IP。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyVpnConnectionAttribute &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <Name>vpn</Name>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <RemoteSubnet>172.16.2.0/24</RemoteSubnet>
      <IpsecConfig>
            <IpsecLifetime>86400</IpsecLifetime>
            <IpsecAuthAlg>sha1</IpsecAuthAlg>
            <IpsecPfs>group2</IpsecPfs>
            <IpsecEncAlg>aes</IpsecEncAlg>
      </IpsecConfig>
      <EffectImmediately>false</EffectImmediately>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <CreateTime>1492753817000</CreateTime>
      <VpnConnectionId>vco-bp10lz7aejumd2vxo****</VpnConnectionId>
      <RequestId>57070A3D-38F2-40A6-A1C9-DB14542EF54D</RequestId>
      <LocalSubnet>10.1.1.0/24,10.1.2.0/24</LocalSubnet>
      <IkeConfig>
            <IkeEncAlg>aes</IkeEncAlg>
            <RemoteId>139.XX.XX.32</RemoteId>
            <IkePfs>group2</IkePfs>
            <IkeAuthAlg>sha1</IkeAuthAlg>
            <Psk>pgw6dy7d1i8i****</Psk>
            <IkeMode>main</IkeMode>
            <IkeLifetime>86400</IkeLifetime>
            <IkeVersion>ikev1</IkeVersion>
            <LocalId>116.XX.XX.69</LocalId>
      </IkeConfig>
```

| JSON | 格式 |
|---|---|
| { "Name": "vpn", "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****", "RemoteSubnet": "172.16.2.0/24", "IpsecConfig": { "IpsecLifetime": 86400, "IpsecAuthAlg": "sha1", "IpsecPfs": "group2", "IpsecEncAlg": "aes" }, "EffectImmediately": false, "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****", "CreateTime": 1492753817000, "VpnConnectionId": "vco-bp10lz7aejumd2vxo****", "RequestId": "7DB79D0C-5F27-4AB5-995B-79BE55102F90", "LocalSubnet": "10.1.1.0/24,10.1.2.0/24", "IkeConfig": { "IkeEncAlg": "aes", "RemoteId": "139.XX.XX.32", "IkePfs": "group2", "IkeAuthAlg": "sha1", "Psk": "pgw6dy7d1i8i****", "IkeMode": "main", "IkeLifetime": 86400, "IkeVersion": "ikev1", "LocalId": "116.XX.XX.69" } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 404 | InvalidVpnConnectionInstanceId. NotFound | The specified vpn connection instance id does not exist. | 指定的 VPN 连接不存在，请您检查该 VPN 链接是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |
| 400 | InvalidName | The name is not valid | 该名称格式不合法。 |

#### 6.6.3. DescribeVpnConnections

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVpnConnections | 要执行的操作，取值：DescribeVpnConnections。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnGatewayId | String | 否 | vpn-bp1q8bgx4xnkx**** | VPN网关的ID。 |
| CustomerGatewayId | String | 否 | cgw-bp1mvj4g9kogw**** | 用户网关的ID。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |
| VpnConnectionId | String | 否 | vco-bp15oes1py4i6**** | IPsec连接的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VpnConnections | Array of VpnConnection |  | IPsec连接列表的详细信息。 |
| VpnConnection |  |  |  |
| IkeConfig | Struct |  | 第一阶段协商的配置。 |
| IkeAuthAlg | String | sha1 | IKE认证算法，取值：sha1和MD5。 |
| IkeEncAlg | String | aes | IKE加密算法。 |
| IkeLifetime | Long | 86400 | IKE生存时间。单位：秒。 |
| IkeMode | String | main | IKE模式，取值：main和aggressive模式。 main模式安全性高，如果启用了NAT穿越，建议选择aggressive模式。 |
| IkePfs | String | group2 | DH分组，取值：group1、group2、group5、group14和group24。 |
| IkeVersion | String | ikev1 | IKE版本。 |
| LocalId | String | 116.XX.XX.64 | 本端ID，支持FQDN和IP格式，默认为当前选取的VPN网关IP地址。 |
| Psk | String | pgw6dy7d**** | 预共享密钥。 |
| RemoteId | String | 139.XX.XX.167 | 对端ID，支持FQDN和IP格式，默认为当前选取的用户网关IP地址。 |
| IpsecConfig | Struct |  | 第二阶段协商的配置。 |
| IpsecAuthAlg | String | sha1 | IPsec认证算法，取值：sha1和md5。 |
| IpsecEncAlg | String | aes | IPsec加密算法。 |
| IpsecLifetime | Long | 86400 | IPsec生存时间。 |
| IpsecPfs | String | group2 | DH分组。 |
| VpnConnectionId | String | vco-bp10lz7aejumd**** | IPsec连接的ID。 |
| CustomerGatewayId | String | cgw-bp1mvj4g9kogw**** | 用户网关的ID。 |
| VpnGatewayId | String | vpn-bp1q8bgx4xnkm**** | VPN网关的ID。 |
| Name | String | name | IPsec连接的名称。 |

| LocalSubnet | String | 10.1.1.0/24,10.1.2.0/24 | VPC侧的网段。 |
|---|---|---|---|
| RemoteSubnet | String | 10.10.1.0/24,10.10.2.0/24 | 本地IDC侧的网段。 |
| CreateTime | Long | 1492753817000 | IPsec连接的创建时间戳。 |
| Status | String | ipsecsaestablished _ _ | 连接状态。分别为： ike _sa _not _established表示第一阶段协商失败。 ike _sa _established表示第一阶段协商成功。 ipsec _sa _not _established表示第二阶段协商失败。 ipsec _sa _established表示第二阶段协商成功。 |
| EffectImmediately | Boolean | true | 是否立即生效： true：配置变更时触发重连。 false：有流量时触发重连。重连有可能导致流量闪断。 |
| VcoHealthCheck | Struct |  | 健康检查。 |
| Dip | String | 8.XX.XX.8 | 目的IP地址。 |
| Enable | String | true | 健康检查的开启状态。 true：已开启。 false：未开启。 |
| Interval | Integer | 2 | 健康检查的时间间隔。单位：秒。 |
| Retry | Integer | 1 | 健康检查的重试发包次数。 |
| Sip | String | 192.XX.XX.66 | 源IP地址。 |
| Status | String | failed | 健康检查状态。 failed：异常。 success：正常。 |
| TotalCount | Integer | 10 | 列表条条目数。 |
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页包含多少条目。 |
| RequestId | String | 54A4B3D0-DF4D-4C54-B8DC- 5DC8DD49C939 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVpnConnections &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <PageNumber>1</PageNumber>
   <VpnConnections>
      <VpnConnection>
```

`<Name>vpn`连接测试`</Name>`

```xml
         <CustomerGatewayId>cgw-bp1pvpl9r9adjxxxxxxxx</CustomerGatewayId>
         <RemoteSubnet>172.16.2.0/24</RemoteSubnet>
         <IpsecConfig>
            <IpsecLifetime>86400</IpsecLifetime>
            <IpsecAuthAlg>sha1</IpsecAuthAlg>
            <IpsecPfs>group2</IpsecPfs>
            <IpsecEncAlg>aes</IpsecEncAlg>
         </IpsecConfig>
         <EffectImmediately>true</EffectImmediately>
         <VpnGatewayId>vpn-bp1q8bgx4xnkmxxxxxxxx</VpnGatewayId>
         <CreateTime>1492753817000</CreateTime>
         <VpnConnectionId>vco-bp10lz7aejumdxxxxxxxx</VpnConnectionId>
         <status>ipsec_sa_established</status>
         <LocalSubnet>10.1.1.0/24,10.1.2.0/24</LocalSubnet>
         <IkeConfig>
            <IkeEncAlg>aes</IkeEncAlg>
            <RemoteId>139.XX.XX.167</RemoteId>
            <IkePfs>group2</IkePfs>
            <IkeAuthAlg>sha1</IkeAuthAlg>
            <Psk>pgw6dy****</Psk>
            <IkeMode>main</IkeMode>
            <IkeLifetime>86400</IkeLifetime>
            <IkeVersion>ikev1</IkeVersion>
            <LocalId>116.XX.XX.64</LocalId>
         </IkeConfig>
      </VpnConnection>
   </VpnConnections>
   <TotalCount>1</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>54A4B3D0-DF4D-4C54-B8DC-5DC8DD49C939</RequestId>
```

| JSON | 格式 |
|---|---|
| { "PageNumber": 1, "VpnConnections": { "VpnConnection": [ { "Name": "vpn连接测试", "CustomerGatewayId": "cgw-bp1pvpl9r9adjxxxxxxxx", "RemoteSubnet": "172.16.2.0/24", "IpsecConfig": { "IpsecLifetime": 86400, "IpsecAuthAlg": "sha1", "IpsecPfs": "group2", "IpsecEncAlg": "aes" }, "EffectImmediately": true, "VpnGatewayId": "vpn-bp1q8bgx4xnkmxxxxxxxx", "CreateTime": 1492753817000, "VpnConnectionId": "vco-bp10lz7aejumdxxxxxxxx", "status": "ipsec_sa_established", "LocalSubnet": "10.1.1.0/24,10.1.2.0/24", "IkeConfig": { "IkeEncAlg": "aes", "RemoteId": "139.XX.XX.167", "IkePfs": "group2", "IkeAuthAlg": "sha1", "Psk": "pgw6dy****", "IkeMode": "main", "IkeLifetime": 86400, "IkeVersion": "ikev1", "LocalId": "116.XX.XX.64" } } ] }, "TotalCount": 1, "PageSize": 10, "RequestId": "54A4B3D0-DF4D-4C54-B8DC-5DC8DD49C939" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |

| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
|---|---|---|---|

#### 6.6.4. DescribeVpnConnection

调用DescribeVpnConnection接口查询已创建的IPsec连接的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVpnConnection | 要执行的操作，取值：DescribeVpnConnection。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnConnectionId | String | 是 | vco-bp1bbi27hojx80nck**** | IPsec连接的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VpnConnectionId | String | vco-bp1bbi27hojx80nck**** | IPsec连接的ID。 |
| CustomerGatewayId | String | cgw-bp1mvj4g9kogwwcxk**** | 用户网关的ID。 |
| VpnGatewayId | String | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关的ID。 |
| Name | String | ipsec1 | IPsec连接的名称。 |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0/24 | VPC侧的网段。 |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2.0/24 | 本地IDC侧的网段。 |
| CreateTime | Long | 1492753817000 | IPsec连接的创建时间。 |
| Status | String | ikesanotestablished _ _ _ | 连接状态。 ike _sa _not _established表示第一阶段协商失败。 ike _sa _established表示第一阶段协商成功。 ipsec _sa _not _established表示第二阶段协商失败。 ipsec _sa _established表示第二阶段协商成功。 |
| EffectImmediately | Boolean | true | IPsec连接是否立即生效。 true：配置变更时触发重连。 false：有流量时触发重连。重连有可能导致流量闪断。 |
| IkeConfig | Struct |  | 第一阶段协商的配置。 |
| IkeAuthAlg | String | sha1 | IKE认证算法。 |
| IkeEncAlg | String | aes | IKE加密算法。 |
| IkeLifetime | Long | 86400 | IKE生存时间。 |
| IkeMode | String | main | IKE模式，支持main和aggressive模式。main模式安全性高，如果启用了 NAT穿越，建议使用aggressive模式。 |
| IkePfs | String | group2 | DH分组。 |
| IkeVersion | String | ikev1 | IKE版本。 |
| LocalId | String | 116.XX.XX.69 | 本端ID，支持FQDN和IP格式，默认为当前选取的VPN网关IP地址。 |
| Psk | String | pgw6dy7d1i8in7x5 | 预共享密钥。 |
| RemoteId | String | 139.XX.XX.32 | 对端ID，支持FQDN和IP格式，默认为当前选取的用户网关IP地址。 |

| IpsecConfig | Struct |  | 第二阶段协商的配置。 |
|---|---|---|---|
| IpsecAuthAlg | String | sha1 | IPsec认证算法。 |
| IpsecEncAlg | String | aes | IPsec加密算法。 |
| IpsecLifetime | Long | 86400 | IPsec生存时间。 |
| IpsecPfs | String | group2 | DH分组。 |
| RequestId | String | F2310D45-BCF6-4E2E-9082- B4503844BA4C | 请求ID。 |
| VcoHealthCheck | Struct |  | 健康检查信息。 |
| Dip | String | 10.XX.XX.1 | 目标IP。 |
| Enable | String | true | 是否已开启健康检查。 false：未开启。 true：已开启。 |
| Interval | Integer | 3 | 健康检查的重试间隔时间，单位是秒。 |
| Retry | Integer | 3 | 健康检查的重试发包次数。 |
| Sip | String | 192.XX.XX.2 | 源IP。 |
| Status | String | failed | 健康检查的状态。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVpnConnection &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <PageNumber>1</PageNumber>
      <VpnConnections>
            <VpnConnection>
                  <Name>c2</Name>
                  <CustomerGatewayId>cgw-bp1wl8dtz3auwlav****</CustomerGatewayId>
                  <Status>ike_sa_not_established</Status>
                  <RemoteSubnet>192.168.0.0/16</RemoteSubnet>
                  <IpsecConfig>
                        <IpsecLifetime>86400</IpsecLifetime>
                        <IpsecAuthAlg>md5</IpsecAuthAlg>
                        <IpsecPfs>group2</IpsecPfs>
                        <IpsecEncAlg>aes</IpsecEncAlg>
                  </IpsecConfig>
                  <EffectImmediately>false</EffectImmediately>
                  <VpnGatewayId>vpn-bp1yfrjxn4d5t63tb****</VpnGatewayId>
                  <CreateTime>1519391420000</CreateTime>
                  <VpnConnectionId>vco-bp1w3m1p23iftycvs****</VpnConnectionId>
                  <LocalSubnet>172.16.0.0/12</LocalSubnet>
                  <IkeConfig>
                        <IkeEncAlg>aes</IkeEncAlg>
                        <RemoteId>47.XX.XX.176</RemoteId>
                        <IkePfs>group2</IkePfs>
                        <IkeAuthAlg>sha1</IkeAuthAlg>
                        <Psk>1234567</Psk>
                        <IkeMode>aggressive</IkeMode>
                        <IkeLifetime>86400</IkeLifetime>
                        <IkeVersion>ikev1</IkeVersion>
                        <LocalId>116.XX.XX.119</LocalId>
                  </IkeConfig>
            </VpnConnection>
      </VpnConnections>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>7D598A10-26EF-44F2-9F47-E417842F3CEA</RequestId>
```

| JSON | 格式 |
|---|---|
| { "PageNumber": 1, "VpnConnections": { "VpnConnection": [ { "Name": "c2", "CustomerGatewayId": "cgw-bp1wl8dtz3auwlavw****", "Status": "ike_sa_not_established", "RemoteSubnet": "192.168.0.0/16", "IpsecConfig": { "IpsecLifetime": 86400, "IpsecAuthAlg": "md5", "IpsecPfs": "group2", "IpsecEncAlg": "aes" }, "EffectImmediately": false, "VpnGatewayId": "vpn-bp1yfrjxn4d5t63t****", "CreateTime": 1519391420000, "VpnConnectionId": "vco-bp1w3m1p23iftycv****", "LocalSubnet": "172.16.0.0/12", "IkeConfig": { "IkeEncAlg": "aes", "RemoteId": "47.XX.XX.176", "IkePfs": "group2", "IkeAuthAlg": "sha1", "Psk": "1234567", "IkeMode": "aggressive", "IkeLifetime": 86400, "IkeVersion": "ikev1", "LocalId": "116.XX.XX.119" } } ] }, "TotalCount": 1, "PageSize": 10, "RequestId": "7D598A10-26EF-44F2-9F47-E417842F3CEA" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |

| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
|---|---|---|---|
| 404 | InvalidVpnConnectionInstanceId. NotFound | The specified vpn connection instance id does not exist. | 指定的 VPN 连接不存在，请您检查该 VPN 链接是否正确。 |

#### 6.6.5. DownloadVpnConnectionConfig

调用DownloadVpnConnectionConfig接口获取IPsec连接的配置信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DownloadVpnConnectionConf ig | 要执行的操作，取值： DownloadVpnConnectionConfig。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnConnectionId | String | 是 | vco-bp1bbi27hojx80nck**** | IPsec连接的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0C68048B-0F70-40DA-B8AE- 1B79B5CF62E3 | 请求ID。 |
| VpnConnectionConfig | Struct |  | IPsec连接的配置信息。 |
| IkeConfig | Struct |  | IKE配置相关配置信息。 |
| IkeAuthAlg | String | sha1 | IKE认证算法，支持sha1和md5。 |
| IkeEncAlg | String | aes | IKE加密算法。 |
| IkeLifetime | Long | 86400 | IKE生存时间。单位为秒。 |
| IkeMode | String | main | IKE模式，支持main和aggressive模式。main模式安全性高，如果启用了 NAT穿越，建议使用aggressive模式。 |
| IkePfs | String | group2 | DH分组。 |
| IkeVersion | String | ikev1 | IKE版本。 |
| LocalId | String | 116.XX.XX.69 | 本端ID，支持FQDN和IP格式，默认为当前选取的VPN网关IP地址。 |
| Psk | String | pgw6dy7d1i8i**** | 预共享密钥。 |
| RemoteId | String | 139.XX.XX.32 | 对端ID，支持FQDN和IP格式，默认为当前选取的用户网关IP地址。 |
| IpsecConfig | Struct |  | IPsec配置信息。 |
| IpsecAuthAlg | String | sha1 | IPsec认证算法，支持sha1和md5。 |
| IpsecEncAlg | String | aes | IPsec加密算法。 |
| IpsecLifetime | Long | 86400 | IPsec生存时间。单位为秒。 |
| IpsecPfs | String | group2 | DH分组。 |
| Local | String | 139.XX.XX.32 | IPsec VPN网关的标识。 |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0/24 | VPC侧的网段。 |
| Remote | String | 116.XX.XX.69 | 用户网关的标识。 |

| RemoteSubnet | String | 10.10.1.0/24,10.10.2.0/24 | 本地IDC侧的网段。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DownloadVpnConnectionConfig &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DownloadVpnConnectionConfigResponse> <RequestId>0C68048B-0F70-40DA-B8AE-1B79B5CF62E3</RequestId> <VpnConnectionConfig> <RemoteSubnet>10.10.1.0/24,10.10.2.0/24</RemoteSubnet> <Local>139.XX.XX.32</Local> <IpsecConfig> <IpsecLifetime>86400</IpsecLifetime> <IpsecAuthAlg>sha1</IpsecAuthAlg> <IpsecPfs>group2</IpsecPfs> <IpsecEncAlg>aes</IpsecEncAlg> </IpsecConfig> <Remote>116.XX.XX.69x</Remote> <LocalSubnet>172.16.2.0/24</LocalSubnet> <IkeConfig> <IkeEncAlg>aes</IkeEncAlg> <IkePfs>group2</IkePfs> <RemoteId>116.XX.XX.69</RemoteId> <IkeAuthAlg>sha1</IkeAuthAlg> <Psk>pgw6dy7d1i8i****</Psk> <IkeMode>main</IkeMode> <IkeLifetime>86400</IkeLifetime> <IkeVersion>ikev1</IkeVersion> <LocalId>139.XX.XX.32</LocalId> </IkeConfig> </VpnConnectionConfig> </DownloadVpnConnectionConfigResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "0C68048B-0F70-40DA-B8AE-1B79B5CF62E3", "VpnConnectionConfig": { "RemoteSubnet": "10.10.1.0/24,10.10.2.0/24", "Local": "139.XX.XX.32", "IpsecConfig": { "IpsecLifetime": 86400, "IpsecAuthAlg": "sha1", "IpsecPfs": "group2", "IpsecEncAlg": "aes" }, "Remote": "116.XX.XX.69", "LocalSubnet": "172.16.2.0/24", "IkeConfig": { "IkeEncAlg": "aes", "IkePfs": "group2", "RemoteId": "116.XX.XX.69", "IkeAuthAlg": "sha1", "Psk": "pgw6dy7d1i8i****", "IkeMode": "main", "IkeLifetime": 86400, "IkeVersion": "ikev1", "LocalId": "139.XX.XX.32" } } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 404 | InvalidVpnConnectionInstanceId. NotFound | The specified vpn connection instance id does not exist. | 指定的 VPN 连接不存在，请您检查该 VPN 链接是否正确。 |

#### 6.6.6. DeleteVpnConnection

删除IPSec连接后，VPC与本地IDC之间的连接将中断。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteVpnConnection | 要执行的操作。 取值： DeleteVpnConnection。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | IPsec连接所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnConnectionId | String | 是 | vco-bp1bbi27hojx80nck**** | IPsec连接的ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE-8316- ACA81BB230DA | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteVpnConnection &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteVpnConnectionResponse> <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId> </DeleteVpnConnectionResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 404 | InvalidVpnConnectionInstanceId. NotFound | The specified vpn connection instance id does not exist. | 指定的 VPN 连接不存在，请您检查该 VPN 链接是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |

### SSL-VPN

#### 6.7.1. CreateSslVpnServer

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateSslVpnServer | 要执行的操作，取值：CreateSslVpnServer。 |

| ClientIpPool | String | 是 | 192.168.1.0/24 | 是给客户端虚拟网卡分配访问地址的地址段，不是指客户端已有的内网网段。 当客户端通过SSL-VPN连接访问本端时，VPN网关会从指定的客户端网段中分配一个IP地址给客户端使用。 该网段不能与LocalSubnet地址段冲突。 |
|---|---|---|---|---|
| LocalSubnet | String | 是 | 10.0.0.0/8 | 是客户端通过SSL-VPN连接要访问的地址段。 本端网段可以是VPC的网段、交换机的网段、通过专线和VPC互连的 IDC的网段、云服务如RDS/OSS等的网段。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnGatewayId | String | 是 | vpn-bp1hgim8by0kc9nga**** | VPN网关的ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大不值过64个 ASCII字符。 |
| Name | String | 否 | sslvpnname | SSL-VPN服务端的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
| Proto | String | 否 | UDP | SSL-VPN服务端所使用的协议，取值： TCP：TCP协议。 UDP（默认值）：UDP协议。 |
| Cipher | String | 否 | AES-128-CBC | SSL-VPN使用的加密算法，取值： AES-128-CBC（默认值）：AES-128-CBC算法。 AES-192-CBC：AES-192-CBC算法。 AES-256-CBC：AES-256-CBC算法。 none：不使用加密算法。 |
| Port | Integer | 否 | 1194 | SSL-VPN服务端所使用的端口，默认值为1194。 不能用使用以下端口： 22、2222、22222、9000、9001、9002、7505、80、443、 53、68、123、4510、4560、500、4500。 |
| Compress | Boolean | 否 | false | 指定是否对通信进行压缩， 取值： true：对通信进行压缩。 false（默认值）：对通信不进行压缩。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Name | String | test | SSL-VPN服务端的名称。 |
| RequestId | String | E98A9651-7098-40C7-8F85- C818D1EBBA85 | 请求ID。 |
| SslVpnServerId | String | vss-bp18q7hzj6largv4v**** | SSL-VPN服务端的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateSslVpnServer &ClientIpPool=192.168.1.0/24 &LocalSubnet=10.0.0.0/8 &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1hgim8by0kc9nga****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateSslVpnServerResponse> <RequestId>E98A9651-7098-40C7-8F85-C818D1EBBA85</RequestId> <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId> <Name>test</Name> </CreateSslVpnServerResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "E98A9651-7098-40C7-8F85-C818D1EBBA85", "SslVpnServerId": "vss-bp18q7hzj6largv4v****", "Name": "test" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 400 | InvalidName | The name is not valid | 该名称格式不合法。 |
| 404 | InvalidVpnGatewayInstanceId.Not Found | The specified vpn gateway instance id does not exist. | 指定的 VPN 网关不存在，请您检查 VPN 网关是否正确。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.7.2. ModifySslVpnServer

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySslVpnServer | 要执行的操作，取值：ModifySslVpnServer。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| SslVpnServerId | String | 是 | vss-bp18q7hzj6largv4v**** | SSL-VPN服务端实例ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大不值过64个 ASCII字符。 |
| Name | String | 否 | test | SSL-VPN服务端的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |
| ClientIpPool | String | 否 | 10.30.30.0/24 | 客户端IP地址池。 |
| LocalSubnet | String | 否 | 10.20.20.0/24 | 本地客户端的网段。 |
| Proto | String | 否 | UDP | SSL-VPN服务端所使用的协议，取值： TCP：TCP协议。 UDP（默认值）：UDP协议。 |
| Cipher | String | 否 | AES-128-CBC | SSL-VPN使用的加密算法，取值： AES-128-CBC（默认值）：AES-128-CBC算法。 AES-192-CBC：AES-192-CBC算法。 AES-256-CBC：AES-256-CBC算法。 none：不使用加密算法。 |
| Port | Integer | 否 | 1194 | SSL-VPN服务端所使用的端口，默认值为1194。 不能用使用以下端口： 22、2222、22222、9000、9001、9002、7505、80、443、 53、68、123、4510、4560、500、4500。 |
| Compress | Boolean | 否 | false | 指定是否对通信进行压缩， 取值： true：对通信进行压缩。 false（默认值）：对通信不进行压缩。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Cipher | String | AES-128-CBC | 使用的加密算法。 |
| ClientIpPool | String | 10.30.30.0/24 | 客户端IP地址池。 |
| Compress | Boolean | false | 是否压缩通信。 |
| Connections | Integer | 0 | 当前连接数。 |
| CreateTime | Long | 1492753580000 | SSL-VPN服务端的创建时间。 |
| InternetIp | String | 47.XX.XX.98 | 公网IP。 |
| LocalSubnet | String | 10.20.20.0/24 | 本地客户端地址段。 |
| MaxConnections | Integer | 5 | 最大连接数。 |
| Name | String | test | SSL-VPN服务端的名称。 |
| Port | Integer | 1194 | SSL-VPN服务端的端口。 |
| Proto | String | UDP | SSL-VPN服务端使用的协议。 |
| RegionId | String | cn-qingdao-env66-d01 | SSL-VPN服务端的地域。 |
| RequestId | String | DF11D6F6-E35A-41C3-9B20- 6FC8A901FE65 | 请求ID。 |
| SslVpnServerId | String | vss-bp18q7hzj6largv4v**** | SSL-VPN服务端的ID。 |
| VpnGatewayId | String | vpn-bp1q8bgx4xnkm2ogj**** | VPN网关实例ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifySslVpnServer &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifySslVpnServerResponse> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> <PageSize>10</PageSize> <SslVpnServers> <SslVpnServer> <RegionId>cn-qingdao-env66-d01</RegionId> <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId> <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId> <Name>test</Name> <CLientIpPool>10.30.30.0/24</CLientIpPool> <LocalSubnet>10.20.20.0/24</LocalSubnet> <Proto>UDP</Proto> <Port>1194</Port> <Cipher>AES-128-CBC</Cipher> <Compress>true</Compress> <CreateTime>1492753580000</CreateTime> <Connections>0</Connections> <MaxConnections>5</MaxConnections> <InternetIp>47.XX.XX.98</InternetIp> </SslVpnServer> </SslVpnServers> <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId> </ModifySslVpnServerResponse> |  |

`JSON` 格式

```json
{
    "PageNumber": "1",
    "TotalCount": "1",
    "PageSize": "10",
            "RegionId": "cn-qingdao-env66-d01",
            "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
            "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
            "Name": "test",
            "CLientIpPool": "10.30.30.0/24",
            "LocalSubnet": "10.20.20.0/24",
            "Proto": "UDP",
            "Port": "1194",
            "Cipher": "AES-128-CBC",
            "Compress": "true",
            "CreateTime": "1492753580000",
            "Connections": "0",
            "MaxConnections": "5",
            "InternetIp": "47.XX.XX.98"
        }
    },
    "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | InvalidName | The name is not valid | 该名称格式不合法。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.7.3. DescribeSslVpnServers

调用DescribeSslVpnServers接口查询已创建的SSL-VPN服务端。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSslVpnServers | 要执行的操作。 取值： DescribeSslVpnServers。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | SSL-VPN服务端所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| SslVpnServerId | String | 否 | vss-bp15j3du13gq1dgey**** | SSL-VPN服务端的ID。 |
| VpnGatewayId | String | 否 | vpn-bp1on0xae9d771ggi**** | VPN网关的ID。 |
| Name | String | 否 | test | SSL-VPN服务端的名称。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页包含多少条目。 |
| RequestId | String | 085CA5EA-1E76-43A8-981B- E0208DECA0CB | 请求ID。 |
| SslVpnServers | Array of SslVpnServer |  | SSL-VPN服务端的详细信息。 |

| SslVpnServer |  |  |  |
|---|---|---|---|
| Cipher | String | AES-128-CBC | 使用的加密算法。 |
| ClientIpPool | String | 10.10.1.0/24 | 客户端IP地址池。 |
| Compress | Boolean | false | 是否压缩。 |
| Connections | Integer | 0 | 当前连接数。 |
| CreateTime | Long | 1544668844000 | 创建时间戳。 |
| InternetIp | String | 47.XX.XX.167 | 公网IP。 |
| LocalSubnet | String | 192.168.0.0/24 | 本地客户端网段。 |
| MaxConnections | Integer | 5 | 最大连接数。 |
| Name | String | test | SSL VPN服务端名称。 |
| Port | Integer | 1194 | SSL-VPN服务端所使用的端口。 |
| Proto | String | UDP | SSL-VPN服务端所使用的协议。 |
| RegionId | String | cn-qingdao-env66-d01 | SSL-VPN服务端的地域。 |
| SslVpnServerId | String | vss-bp15j3du13gq1dgey**** | SSL-VPN服务端的ID。 |
| VpnGatewayId | String | vpn-bp1on0xae9d771ggi**** | VPN网关ID。 |
| TotalCount | Integer | 1 | 列表条条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSslVpnServers &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeSslVpnServersResponse> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> <PageSize>10</PageSize> <SslVpnServers> <SslVpnServer> <RegionId>cn-qingdao-env66-d01</RegionId> <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId> <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId> <Name>test</Name> <CLientIpPool>10.10.10.0/24</CLientIpPool> <LocalSubnet>10.10.20.0/24</LocalSubnet> <Proto>UDP</Proto> <Port>1194</Port> <Cipher>AES-128-CBC</Cipher> <Compress>true</Compress> <CreateTime>1492753580000</CreateTime> <Connections>0</Connections> <MaxConnections>5</MaxConnections> <InternetIp>47.XX.XX.167</InternetIp> </SslVpnServer> </SslVpnServers> <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId> </DescribeSslVpnServersResponse> |  |

`JSON` 格式

```json
{
    "PageNumber": "1",
    "TotalCount": "1",
    "PageSize": "10",
            "RegionId": "cn-qingdao-env66-d01",
            "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
            "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
            "Name": "test",
            "CLientIpPool": "10.10.10.0/24",
            "LocalSubnet": "10.10.20.0/24",
            "Proto": "UDP",
            "Port": "1194",
            "Cipher": "AES-128-CBC",
            "Compress": "true",
            "CreateTime": "1492753580000",
            "Connections": "0",
            "MaxConnections": "5",
            "InternetIp": "47.XX.XX.167"
        }
    },
    "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |

#### 6.7.4. DescribeVpnSslServerLogs

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVpnSslServerLogs | 要执行的操作，取值：DescribeVpnSslServerLogs。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | SSL服务端所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| VpnSslServerId | String | 是 | vss-bp155e9yclsg1xgq4**** | SSL服务端的ID。 |
| From | Integer | 否 | 2018020201 | 日志起始时间，时间格式为yyyymmddhh。 如果指定From，则必须指定To或MinutePeriod。 |
| To | Integer | 否 | 2018020206 | 日志结束时间，时间格式为yyyymmddhh。 如果指定To，则必须指定From或MinutePeriod。 |
| MinutePeriod | Integer | 否 | 10 | 日志周期。 如果不指定From和To，则必须指定或MinutePeriod。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 10 | 日志条目数。 |
| Data | List | test | 数组，数组中的每一项都为一条日志。 |
| IsCompleted | Boolean | true | 查询的日志是否精确，取值： true：精确。 false：不精确。 |

| PageNumber | Integer | 1 | 当前页码。 |
|---|---|---|---|
| PageSize | Integer | 1 | 每页包含的条目数。 |
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVpnSslServerLogs &RegionId=cn-qingdao-env66-d01 &VpnSslServerId=vss-bp155e9yclsg1xgq4****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeVpnSslServerLogsResponse> <Data></Data> <PageNumber>1</PageNumber> <Count>0</Count> <PageSize>10</PageSize> <IsCompleted>true</IsCompleted> <RequestId>26641E42-66C7-4942-9FEC-F99213914F8F</RequestId> </DescribeVpnSslServerLogsResponse> |  |

| JSON | 格式 |
|---|---|
| { "Data": { "Logs": [] }, "PageNumber": 1, "Count": 0, "PageSize": 10, "IsCompleted": true, "RequestId": "26641E42-66C7-4942-9FEC-F99213914F8F" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |

#### 6.7.5. DeleteSslVpnServer

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteSslVpnServer | 要执行的操作。 取值： DeleteSslVpnServer。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | SSL-VPN服务端所在的地域。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| SslVpnServerId | String | 是 | vss-bp18q7hzj6largv4v**** | SSL-VPN服务端的ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大不值过64个 ASCII 字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE-8316- ACA81BB230DA | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteSslVpnServer &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteSslVpnServerResponse> <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId> </DeleteSslVpnServerResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |

#### 6.7.6. CreateSslVpnClientCert

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateSslVpnClientCert | 要执行的操作。 取值： CreateSslVpnClientCert。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | VPN网关所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| SslVpnServerId | String | 是 | vss-m5et0q3iy1qex328w**** | SSL-VPN服务端的ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大不值过64个 ASCII字符。 |
| Name | String | 否 | SslVpnClientCert1 | 客户端证书的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Name | String | SslVpnClientCert | 客户端证书的名称。 |
| RequestId | String | 079874CD-AEC1-43E6-AC03- ADD96B6E4907 | 请求ID。 |
| SslVpnClientCertId | String | vsc-m5euof6s5jy8vs5kd**** | 客户端证书的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateSslVpnClientCert &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateSslVpnClientCertResponse> <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId> <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId> </CreateSslVpnClientCertResponse> |  |

| JSON | 格式 |
|---|---|
| { "SslVpnClientCertId": "vsc-bp1n8wcf134yl0osr****", "RequestId": "606998F0-B94D-48FE-8316-ACA81BB230DA" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | Resource.QuotaFull | The quota of resource is full | 资源配额已达上限。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |
| 400 | VpnGateway.FinancialLocked | The specified service is financial locked. | 该服务已欠费，请您先充值再操作。 |
| 400 | InvalidName | The name is not valid | 该名称格式不合法。 |

#### 6.7.7. ModifySslVpnClientCert

调用ModifySslVpnClientCert接口修改SSL-VPN客户端证书的名称。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySslVpnClientCert | 要执行的操作。 取值：ModifySslVpnClientCert。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | SSL-VPN客户端证书所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| SslVpnClientCertId | String | 是 | vsc-bp1n8wcf134yl0osrc**** | SSL-VPN客户端证书的ID。 |
| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大不值过64个 ASCII 字符。 |
| Name | String | 否 | cert2 | SSL-VPN客户端证书的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（_）和短划线（-）。但不能以 http:// 或 https:// 开头。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Name | String | cert2 | 客户端证书的名称。 |
| RequestId | String | 606998F0-B94D-48FE-8316- ACA81BB230DA | 请求ID。 |
| SslVpnClientCertId | String | vsc-bp1n8wcf134yl0osr**** | SSL-VPN客户端证书的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifySslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp1n8wcf134yl0osrc****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifySslVpnClientCertResponse> <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId> <Name>cert2</Name> <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId> </ModifySslVpnClientCertResponse> |  |

| JSON | 格式 |
|---|---|
| { "SslVpnClientCertId": "vsc-bp1n8wcf134yl0osr****", "Name": "cert2", "RequestId": "606998F0-B94D-48FE-8316-ACA81BB230DA" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | InvalidName | The name is not valid | 该名称格式不合法。 |

#### 6.7.8. DescribeSslVpnClientCerts

调用DescribeSslVpnClientCerts接口查询已创建的SSL客户端证书。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSslVpnClientCerts | 要执行的操作，取值：DescribeSslVpnClientCerts。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要查询的SSL客户端证书所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| SslVpnServerId | String | 否 | vss-bp18q7hzj6largv4v**** | SSL服务端ID。 |
| SslVpnClientCertId | String | 否 | vsc-bp1n8wcf134yl0osr**** | SSL客户端证书ID。 |
| Name | String | 否 | cert1 | SSL客户端证书的名称。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值为1。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值为50，默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页包含的条目数。 |
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |
| SslVpnClientCertKeys | Array of SslVpnClientCertKey |  | SSL客户端证书的详细信息。 |
| SslVpnClientCertKey |  |  |  |
| CreateTime | Long | 1492747187000 | SSL客户端证书的创建时间戳。 |

| EndTime | Long | 1494966335000 | SSL客户端证书的到期时间戳。 |
|---|---|---|---|
| Name | String | cert1 | SSL客户端证书的名称。 |
| RegionId | String | cn-qingdao-env66-d01 | SSL客户端证书的地域ID。 |
| SslVpnClientCertId | String | vsc-bp1n8wcf134yl0osr**** | SSL客户端证书的ID。 |
| SslVpnServerId | String | vss-bp18q7hzj6largv4v**** | SSL服务端ID。 |
| Status | String | normal | 客户端证书的状态。 expiring-soon：证书将在1周后过期。 normal：正常。 expired：已过期。 |
| TotalCount | Integer | 1 | 列表条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSslVpnClientCerts &RegionId=cn-qingdao-env66-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeSslVpnServersResponse> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> <PageSize>10</PageSize> <SslVpnServers> <SslVpnServer> <RegionId>cn-qingdao-env66-d01</RegionId> <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId> <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId> <Name>test</Name> <CLientIpPool>10.10.20.0/24</CLientIpPool> <LocalSubnet>10.10.10.0/24</LocalSubnet> <Proto>UDP</Proto> <Port>1194</Port> <Cipher>AES-128-CBC</Cipher> <Compress>true</Compress> <CreateTime>1492753580000</CreateTime> <Connections>0</Connections> <MaxConnections>5</MaxConnections> <InternetIp>47.XX.XX.98</InternetIp> </SslVpnServer> </SslVpnServers> <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId> </DescribeSslVpnServersResponse> |  |

`JSON` 格式

```json
{
        "PageNumber": "1",
        "TotalCount": "1",
        "PageSize": "10",
                "RegionId": "cn-qingdao-env66-d01",
                "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
                "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
                "Name": "test",
                "CLientIpPool": "10.10.20.0/24",
                "LocalSubnet": "10.10.10.0/24",
                "Proto": "UDP",
                "Port": "1194",
                "Cipher": "AES-128-CBC",
                "Compress": "true",
                "CreateTime": "1492753580000",
                "Connections": "0",
                "MaxConnections": "5",
                "InternetIp": "47.XX.XX.98"
            }
        },
        "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |

#### 6.7.9. DescribeSslVpnClientCert

调用DescribeSslVpnClientCert接口查询指定的的SSL客户端证书信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSslVpnClientCert | 要执行的操作，取值：DescribeSslVpnClientCert。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | 要查询的SSL客户端证书所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| SslVpnClientCertId | String | 是 | vsc-bp17r58rjf5r1gjyr**** | 要查询的SSL客户端证书的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CaCert | String | Ca证书 | CA证书。 |
| ClientCert | String | 客户端证书 | 客户端证书。 |
| ClientConfig | String | 客户端配置 | 客户端配置。 |
| ClientKey | String | 客户端密钥 | 客户端密钥。 |
| CreateTime | Long | 1552550980000 | SSL客户端证书的创建时间戳。 |
| EndTime | Long | 1647158980000 | SSL客户端证书的到期时间戳。 |
| Name | String | abc | 客户端证书的名称。 |
| RegionId | String | cn-qingdao-env66-d01 | SSL客户端证书所在的地域ID。 |
| RequestId | String | 5BE01CD7-5A50-472D-AC14- CA181C5C03BE | 请求ID。 |

| SslVpnClientCertId | String | vsc-bp13k5mp4tg8v3z9b**** | SSL客户端证书的ID。 |
|---|---|---|---|
| SslVpnServerId | String | vss-bp155e9yclsg1xgq4**** | SSL服务端ID。 |
| Status | String | normal | 客户端证书的状态。 expiring-soon：证书将在1周后过期。 normal：正常。 expired：已过期。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp17r58rjf5r1gjyr****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeSslVpnServersResponse> <Name>df</Name> <Status>normal</Status> <ClientConfig>****</ClientConfig> <ClientCert>****</ClientCert> <CreateTime>1552550980000</CreateTime> <RegionId>cn-qingdao-env66-d01</RegionId> <RequestId>49D54005-6E0E-4132-B305-F3A24DEDDDC9</RequestId> <EndTime>1647158980000</EndTime> <SslVpnClientCertId>vsc-bp13k5mp4tg8v3z9b****</SslVpnClientCertId> <ClientKey>****</ClientKey> <CaCert>****</CaCert> <SslVpnServerId>vss-bp155e9yclsg1xgq4****</SslVpnServerId> </DescribeSslVpnServersResponse> |  |

| JSON | 格式 |
|---|---|
| { "Name": "df", "Status": "normal", "ClientConfig": "****", "ClientCert": "****", "CreateTime": 1552550980000, "RegionId": "cn-qingdao-env66-d01", "RequestId": "49D54005-6E0E-4132-B305-F3A24DEDDDC9", "EndTime": 1647158980000, "SslVpnClientCertId": "vsc-bp13k5mp4tg8v3z9b****", "ClientKey": "****", "CaCert": "****", "SslVpnServerId": "vss-bp155e9yclsg1xgq4****" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |

#### 6.7.10. DeleteSslVpnClientCert

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteSslVpnClientCert | 要执行的操作。 取值： DeleteSslVpnClientCert。 |
| RegionId | String | 是 | cn-qingdao-env66-d01 | SSL-VPN客户端证书所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 |
| SslVpnClientCertId | String | 是 | vsc-bp1n8wcf134yl0osr**** | SSL-VPN客户端证书的ID。 |

| ClientToken | String | 否 | 02fb3da4-130e-11e9-8e44- 0016e04115b | 客户端token，用于保证请求的幂等性。 由客户端生成该参数值，要保证在不同请求间唯一，最大不值过64个 ASCII字符。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE-8316- ACA81BB230DA | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteSslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp1n8wcf134yl0osr****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
```

`JSON` 格式

```json
{
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | 您没有权限操作该资源，请您申请操作权限后再试。 |
| 403 | Forbidden | User not authorized to operate on the specified resource. | 您没有权限操作指定资源，请提交工单咨询。 |
| 400 | VpnGateway.Configuring | The specified service is configuring. | 服务正在配置中，请您稍后再试。 |

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

下列代码以调用ECS的 `DescribeZones` 接口为示例。

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

| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
|---|---|---|---|
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
