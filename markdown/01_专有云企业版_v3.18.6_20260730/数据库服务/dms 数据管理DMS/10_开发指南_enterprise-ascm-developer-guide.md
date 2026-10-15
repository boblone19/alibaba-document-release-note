---
title: "数据管理DMS 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 399
source_pdf: "10_开发指南_enterprise-ascm-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/dms/zh/enterprise-ascm-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 数据管理DMS 开发指南

数据管理

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
数据管理
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

为了使您拥有与阿里云公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

数据管理

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
获取调用时所需要的RegionID参数，请参见获取公共Header参数。
3. 获取组织ID与资源集ID。
资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListRe sourceGroup章节。

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参数据管理
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
数据管理

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

绑定并开启MFA的操作请参见《**Apsara Uni-manager****运营控制台用户指南》**中的**《绑定并开**
**启虚拟****MFA****设备》**章节。
5. 在页面顶部的菜单栏中，选择**产品** > **应用服务** > **开发者门户**。

### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

数据管理 Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey

数据管理 AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。
Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。

**获取组织AccessKey**

数据管理获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com> ，请替换为实际的STS Endpoint。 数据管理

```
public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。 `//` 请替换为您实际的地域`ID`、`AccessKey ID`、`AccessKey Secret`

```xml
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

`//` 获取到`STS`三元组

```java
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
} private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
```

`// "sts.aliyuns.com"` 请替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`"<yourRoleSessionName>"`请您替换为实际值

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`"<yourRoleArn>"`请替换为上一步获取到的实际`Ram Role ARN`

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

3. 通过STS AccessKey三元组调用云产品的接口，下列代码以ECS的 `DescribeZones` 接口为示例。
数据管理

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>,请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>请替换为您实际的组织ID。

```
public static void main(String[] args) {
```

`// "<yourRegionID>"`请替换为您实际的地域`ID` `// "<yourStsAccessKeyID>", "<yourStsAccessKeySecret>"`请替换为前一步获取到的`STS`三元组中

```xml
AccessKeyID、AccessKeySecret
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
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

数据管理

### 获取DMS的Endpoint

**背景信息**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。您也可以通过如下方法自行获取Endpoint。

**操作步骤**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏中，选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏中，选择**运维工具** > **服务注册变量大盘**。
4. 在**服务注册变量大盘**页面，在搜索框选择**服务**并输入 `dts-dtm` 。
5. 在 `dts-dtm` 服务的**Service Registration**列中，单击
图标展示隐藏的内容，然后单击该内容。 在弹出的**注册变量**对话框中，查看**dms.openapi.endpoint**的值，即 `Endpoint` 。

### 获取DMS的SDK包

通过POP网关调用专有云API时，需使用数据管理DMS的SDK。本文为您介绍如何获取阿里云开发工具包 （SDK）。

| 语言 | 数据管理DMS SDK下载地址 | 文档 |
|---|---|---|
| Alibaba Cloud SDK for Java | DMS SDK for Java 说明推荐SDK的版本为1.18.0。 | 快速开始（Java） |
| Alibaba Cloud SDK for Python | DMS SDK for Python | 快速开始（Python） |
| Alibaba Cloud SDK for Go | DMS SDK for Go | 快速开始（Go） |

**说明**

推荐使用 Java、Python、Go三种语言的SDK包，使用其他语言的SDK包可能发生不兼容情况。 数据管理

## Java SDK调用示例

### 快速开始

本节介绍如何获取数据管理DMSJava SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。参见获取AccessKey在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用数据管理DMS的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用 4.5.17及以上版本，SDK的版本为1.18.0。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <DMSProductCode>，请替换为您专有云环境DMS的产品Code。 <DMSProductEndpoint>，请替换为您专有云环境DMS产品的Endpoint地址。 数据管理

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.dms_enterprise.model.v20181101.GetOpLogRequest; import com.aliyuncs.dms_enterprise.model.v20181101.GetOpLogResponse; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile;
    public static void main(String[] args) {
        String regionId = "<yourRegionID>";
        String accessKey = "<yourAccessKeyID>";
        String secretKey = "<yourAccessKeySecret>";
        String product = "<DMSProductCode>";
        String endpoint = "<DMSProductEndpoint>";
        DefaultProfile.addEndpoint(regionId, product, endpoint);
        DefaultProfile profile = DefaultProfile.getProfile(regionId, accessKey,
secretKey);
        IAcsClient client = new DefaultAcsClient(profile);
        GetOpLogRequest request = new GetOpLogRequest();
        request.setStartTime("2022-01-01 00:00:00");
        request.setEndTime("2022-01-02 00:00:00");
        request.setPageNumber(1);
        request.setPageSize(100);
        try {
            GetOpLogResponse response = client.getAcsResponse(request);
            System.out.println("RequestId: " + response.getRequestId());
            System.out.println("OpLogCount: " + response.getTotalCount());
        }
        catch (ServerException e) {
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

#### 安装Java SDK

本文介绍如何安装及调用数据管理DMS Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 数据管理要使用数据管理DMS的开发工具包，必须安装阿里云Java SDK核心库以及数据管理DMS的Java SDK。 SDK核心库推荐使用4.5.17及以上版本，SDK的版本为1.18.0。 以使用数据管理DMS的Java SDK为例，您需要安装阿里云Java SDK核心库和DMS Java SDK，并在 pom.xml文件中添加以下依赖即可。准确的SDK版本号，请参见获取DMS的SDK包。

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- dms-enterprise java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-dms-enterprise</artifactId>
    <version>1.18.0</version>
</dependency>
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。 数据管理

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

#### 发起调用

本文介绍如何使用数据管理DMS Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例如GetOpLog。 在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。 数据管理

```
GetOpLogRequest request = new GetOpLogRequest(); request.setStartTime("2022-01-01 00:00:00"); request.setEndTime("2022-01-02 00:00:00"); request.setPageNumber(1); request.setPageSize(100);
```

3. 发起调用并处理应答。

```
GetOpLogResponse response = client.getAcsResponse(request);
```

正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 `response.getXXX()` 来获得应答中的字段。

```
OpLogCount := response.getTotalCount()
```

如果出现了异常，或您需要原始HTTP应答的情况下，您可以通过使用 `doAction()` 来获取原始应答。

```
HttpResponse response = client.doAction(request);
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

数据管理

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。 用 `request.setSysAction("RegisterUser")` 来指定API名称。

**调用RPC风格的API示例**

以下代码为获取实例状态列表的调用示例（DMS产品属于RPC的调用风格)。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; importcomaliyuncsprofileDefaultProfile;
```

数据管理

```java
import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionUD>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

```
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
        request.setDomain("dms.aliyuncs.com");
        request.setSysProduct("Dms");
        request.setVersion("2018-11-01");
        request.setAction("RegisterUser");
        request.putQueryParameter("Region", "cn-hangzhou");
        request.putQueryParameter("Uid", "1234****");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// 非
```

必填，请替换为您实际的资源集`ID`

```
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// 必填
```

，请替换为您实际的组织`ID`

```
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// 必填，调用来
```

源说明

```
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// 非必填(企业版
```

`V3.15.0`及之前历史版本需要`),`请替换为您实际的地域`ID`

```
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修
```

改、删除、查询单实例详情时需要）,请替换为您实际的实例`ID`

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

数据管理

## Python SDK调用示例

### 快速开始

本节介绍如何获取数据管理DMS的Python SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体请参
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
以下以安装数据管理DMS的SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装DMS的SDK：

```
pip install aliyun-python-sdk-dms-enterprise
```

如果您使用的是Python 3.x，执行以下命令，安装DMS的SDK：

```
pip3 install aliyun-python-sdk-dms-enterprise
```

**使用Python SDK**

以下示例以数据管理DMS为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <DMSProductCode>，请替换为您专有云环境DMS的产品Code。 <DMSProductEndpoint>，请替换为您专有云环境DMS产品的Endpoint地址。 数据管理

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdms_enterprise.request.v20181101.GetOpLogRequest import GetOpLogRequest credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials) request.set_accept_format('json') request.set_endpoint('<DMSProductEndpoint>') response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### 使用手册

#### 安装Python SDK

本文档介绍如何安装及调用数据管理DMS Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。 使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用DMS

**说明**

的Python SDK，您需要安装阿里云Python SDK核心库和DMS的Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

安装云产品的SDK，以下以安装DMS的SDK为例。 如果您使用的是Python 2.x，执行以下命令，安装DMS的SDK：

```
pip install aliyun-python-sdk-dms-enterprise
```

如果您使用的是Python 3.x，执行以下命令，安装DMS的SDK：

```
pip3 install aliyun-python-sdk-dms-enterprise
```

#### 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 数据管理使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危

**重要**

害您的信息安全。

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。 产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**说明**

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。

| 行 | python -c "import ssl" | 检查Pyth |
|---|---|---|
| ImportError: No module named ssl |  |  |

若没有OpenSSL，运行以下命令安装： `pip install pyopenssl #Python2`使用此命令。 若本地环境为Python3，则运行 `pip3 install pyopenssl` 命令。

**说明**

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

#### 发起调用

本节介绍如何使用数据管理DMS Python SDK发起请求。

**操作步骤**

1. 导入DMS的SDK。
数据管理

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdms_enterprise.request.v20181101.GetOpLogRequest import GetOpLogRequest
```

2. 新建一个AcsClient。

```
credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials)
```

3. 创建Request对象。

```
request.set_accept_format('json') request.set_endpoint('<DMSProductEndpoint>')
```

4. 发起调用并处理返回。

```python
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8')) response = clt.do_action_with_exception(request) print response
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

数据管理

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.set_action_name('Action')` 的方式来指定API名称。 用 `request.set_action_name('ListUsers')` 来指定API名称。

**调用RPC风格的API示例**

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <ecs.aliyuncs.com>，请替换为您实际的产品访问地址。 数据管理

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('dms-enterprise') request.set_version('2018-11-01')
```

`request.set_domain('<dms-enterprise.aliyuncs.com>') #`产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# or:
# request = = CommonRequest(product='dms-enterprise',
action_name='ListUsers',version='2018-11-01',domain='dms-enterprise.aliyuncs.com')
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

# 必填，调用来源说明

```
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
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

数据管理

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问。本操作介绍如何获取阿里云数据管理DMS Go SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。参见获取 AccessKey在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。

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
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <DMSProductCode>，请替换为您专有云环境DMS的产品Code。 <DMSProductEndpoint>，请替换为您专有云环境DMS产品的Endpoint地址。 数据管理

```java
package main
 "fmt"
   dms_enterprise "github.com/aliyun/alibaba-cloud-sdk-go/services/dms-enterprise"
```

)

```
func main() {
 client, err := dms_enterprise.NewClientWithAccessKey("<yourRegionID>", "<yourAccessK
eyID>", "<yourAccessKeySecret>")
 request := dms_enterprise.CreateGetOpLogRequest()
 request.Scheme = "https"
    request.Domain = "<DMSProductEndpoint>"
 if err != nil {
  fmt.Print(err.Error())
 }
 fmt.Printf("response is %#v\n", response)
}
```

4. （可选）切换HTTP/HTTPS协议。

```
request.Scheme = "HTTPS"
```

### 使用手册

#### 安装Go SDK核心包

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危

**重要**

害您的阿里云账号的信息安全。 以下代码以DMS为例，展示初始化Client实例。 数据管理 `//` 初始化`Client`实例

```
Client, err := dms-enterprise.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。

#### 发起调用

本文介绍如何使用阿里云数据管理DMS Go SDK发起调用。 以下步骤以数据管理DMS为例，展示使用DMS Go SDK发起调用。
1. 导入数据管理DMS SDK。

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/dms-enterprise
```

2. 新建一个产品名Client，该Client中包含产品名的所有API。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 `Client,err := dms_enterprise.NewClientWithAccessKey( //`请替换为您实际的产品名称 `"<yourRegionID>", //` 请替换为您实际的`RegionID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>") //` 请替换为您实际的`AccessKeySecret`
3. 使用 `xxx.CreateXXXRequest` 方法创建一个请求。
该方法的命名规范为 ${service}.Create${apiName}Request ，其中：
**${service}**为产品名称(小写)。例如dms_enterprise。

```
request := dms_enterprise.CreateGetOpLogRequest() request.Scheme = "https" request.Domain = "<DMSProductEndpoint>"
```

4. 发起调用。

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。 数据管理

```
response,err := Client.DescribeInstances(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个 `ClientError` 。 以下以DMS为例，您可以通过以下代码来判断并获取 `ClientError` 中的错误信息：

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/dms-enterprise" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

```
if clientError, ok := err.(*errors.ClientError); ok{
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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以DMS为例，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息： 数据管理

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/dms-enterprise" //dms请替换为您实际的产品名称 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

```
response, err := Client.DescribeInstances(request) if serverError, ok := err.(*errors.ServerError); ok{
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

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**调用RPC风格的API示例**

以下代码为数据管理DMS的ListUserTenants接口，获取当前的租户列表的调用示例（DMS产品属于RPC 的调用风格）：

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 数据管理

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

`"<yourRegionID>", //`请替换为您实际的地域`ID` `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID` `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`

```
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Method = "POST"
```

`request.Domain = "<dms-enterprise.aliyuncs.com>" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "dms-enterprise"
    request.Version = "2018-11-01"
```

`//` 因为是`RPC`接口，因此需指定`APIName(Action)` `//` 业务参数

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
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // 必填，调用来源说明
```

`request.Headers["x-acs-regionid"] = "<yourRegionID>" //` 非必填（企业版`V3.15.0`及之前历史版本需要），请替换为您实际的地域`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // 非必填，请替换为
```

您实际的资源集`ID`

```
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // 必填，请替换为您实
```

际的组织`ID` `// request.Headers["x-acs-instanceid"] = "<yourInstanceID>" //` 非必填（修改、删除、查看单实例详情时需要），请替换为您实际的实例`ID`

```
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

数据管理

## API参考

### API概览

数据管理DMS提供以下API接口。

### 用户管理

| API | 描述 |
|---|---|
| RegisterUser | 录入新的用户。 |
| DisableUser | 禁用用户。 |
| EnableUser | 启用用户。 |
| UpdateUser | 更新用户信息。 |
| DeleteUser | 删除用户。 |
| ListUsers | 获取用户详情列表。 |
| ListUserTenants | 获取当前的租户列表。 |
| GetUserActiveTenant | 获取当前租户信息。 |
| GetUser | 获取用户信息。 |

### 实例管理

| API | 描述 |
|---|---|
| RegisterInstance | 录入新的数据库实例。 |
| ListInstances | 进行实例列表检索并获取实例详情。 |
| GetInstance | 获取实例详细信息。 |
| UpdateInstance | 更新实例信息，检查连通性。 |
| DeleteInstance | 删除DMS管理的实例。 |

### 操作日志

| API | 描述 |
|---|---|
| GetOpLog | 获取指定时间内的操作日志详情列表。 |

### 审批流程

| API | 描述 |
|---|---|
| ListWorkFlowTemplates | 获取审批模板列表。 |

数据管理

| ListWorkFlowNodes | 获取审批节点列表。 |
|---|---|

| API | 描述 |
|---|---|
| SearchDatabase | 搜索数据库的详情信息。 |
| SearchTable | 搜索表详情列表 |
| ListDatabases | 获取实例下的数据列表详情信息。 |
| ListLogicDatabases | 获取逻辑库详情列表。 |
| ListTables | 获取数据库下面的表详情列表。 |
| ListLogicTables | 获取指定逻辑库下逻辑表的详情列表。 |
| ListColumns | 获取表的列信息。 |
| ListIndexes | 获取表的索引信息。 |
| GetDatabase | 获取数据库详情信息。 |
| GetLogicDatabase | 获取逻辑库的详情信息。 |
| GetMetaTableDetailInfo | 获取表的字段、索引等信息。 |
| GetTableDBTopology | 获取数据表的拓扑图。 |
| GetMetaTableColumn | 获取表的字段信息。 |
| SyncDatabaseMeta | 同步数据库字典元数据。 |
| SyncInstanceMeta | 同步实例下所有数据库字典元数据。 |
| GetPhysicalDatabase | 获取物理库的详情。 |
| GetTableTopology | 获取数据表的拓扑信息。 |

### 工单操作

| 分类 | API | 描述 |
|---|---|---|
| 通用 | ApproveOrder | 处理工单审批。 |
|  | CloseOrder | 关闭工单。 |
|  | GetApprovalDetail | 获取工单审批详情。 |
|  | GetOrderBaseInfo | 获取工单基本信息。 |
|  | ListOrders | 获取工单列表信息。 |
|  | SubmitOrderApproval | 提交工单审批。 |
|  | CreateOrder | 创建工单。 |

数据管理

| 数据变更 | ExecuteDataCorrect | 执行数据变更工单。 |
|---|---|---|
|  | GetDataCorrectBackupFiles | 获取数据变更备份文件附件下载地址。 |
|  | GetDataCorrectOrderDetail | 获取数据变更工单详情信息。 |
|  | CreateFreeLockCorrectOrder | 在DMS中创建无锁变更工单。 |
|  | CreateDataCorrectOrder | 在DMS中创建普通数据变更工单。 |
|  | GetDataCronClearTaskDetailList | 获取历史数据清理任务执行列表。 |
|  | GetDataCorrectTaskDetail | 获取普通数据变更、无锁变更、数据导入工单任务执行详情。 |
|  | GetDataCorrectSQLFile | 获取数据变更工单的SQL脚本附件。 |
|  | CreateDataCronClearOrder | 创建历史数据清理工单。 |
|  | CreateDataImportOrder | 在DMS中创建数据导入工单。 |
| 结构设计 | CreatePublishGroupTask | 执行结构设计变更。 |
|  | ListDDLPublishRecords | 获取结构设计工单的发布详情。 |
| 数据导出 | ExecuteDataExport | 执行数据导出工单。 |
|  | GetDataExportDownloadURL | 获取数据导出结果附件下载地址。 |
|  | GetDataExportOrderDetail | 获取数据导出工单详情。 |
| 库表同步 | GetStructSyncOrderDetail | 获取结构同步的工单详情信息。 |
|  | GetStructSyncExecSqlDetail | 获取结构同步的执行SQL脚本。 |
|  | ExecuteStructSync | 执行结构同步工单。 |
|  | GetStructSyncJobAnalyzeResult | 获取结构同步的任务分析结果。 |
|  | SubmitStructSyncOrderApproval | 提交结构同步工单至审批流程。 |
|  | CreateStructSyncOrder | 创建结构同步工单。 |
|  | GetStructSyncJobDetail | 获取结构同步的任务详情。 |
| SQL审核 | GetSQLReviewCheckResultStatu s | 获取SQL审核工单的审核结果。 |
|  | CreateSQLReviewOrder | 创建SQL审核工单。 |
|  | ListSQLReviewOriginSQL | 获取SQL审核工单的SQL详情结果。 |
| 附件上传 | CreateUploadOSSFileJob | 创建上传OSS附件任务。 |
|  | GetUserUploadFileJob | 获取上传附件的任务信息。 |
|  | CreateUploadFileJob | 创建上传附件任务。 |
| 权限申请 | GetOwnerApplyOrderDetail | 获取申请库Owner、表Owner、实例Owner的工单详情。 |

| 权限申请 |  |  |
|---|---|---|
|  | GetPermApplyOrderDetail | 获取权限申请的工单详情。 |

| API | 描述 |
|---|---|
| ListDBTaskSQLJob | 获取SQL任务列表。 |
| ListDBTaskSQLJobDetail | 获取SQL任务详情列表。 |

### 权限管理

| API | 描述 |
|---|---|
| RevokeUserPermission | 回收用户权限。 |
| ListDatabaseUserPermssions | 获取指定数据库权限的用户权限详情。 |
| SetOwners | 设置库表Owner。 |
| ListUserPermissions | 展示指定用户所具备的库表权限。 |
| GrantUserPermission | 授权用户库表权限。 |

### 安全管理

| API | 描述 |
|---|---|
| ListSensitiveColumns | 搜索敏感字段列表。 |
| ListSensitiveColumnsDetail | 获取敏感字段详情信息。 |
| ChangeColumnSecLevel | 调整字段敏感等级。 |
| AddDesensitizationRule | 添加脱敏规则。 |
| ListDesensitizationRule | 获取脱敏规则列表。 |
| ModifyDesensitizationStrategy | 修改字段绑定的脱敏规则。 |

### 数据查询

| API | 描述 |
|---|---|
| ExecuteScript | 执行SQL脚本。 |

### 任务编排

| API | 描述 |
|---|---|
| UpdateTaskFlowConstants | 更新任务流常量列表。 |
| DeleteTaskFlow | 删除任务流。 |
| OfflineTaskFlow | 下线已发布的任务流。 |

数据管理

| ListTaskFlow | 获取任务流信息列表。 |
|---|---|
| GetTaskInstanceRelation | 获取任务流运行记录的节点信息。 |
| ListTaskFlowInstance | 获取任务流运行记录。 |
| ListDAGVersions | 获取任务流历史发布版本信息列表。 |
| ReDeployLhDagVersion | 重新部署任务流历史版本。 |
| UpdateScenario | 更新任务流业务场景名称和描述。 |
| ResumeTaskFlowInstance | 恢复已暂停运行的任务流。 |
| UpdateTaskContent | 更新任务流中的任务。 |
| ListTaskFlowsByPage | 获取任务流运行记录列表。 |
| ListScenarios | 获取业务场景列表。 |
| UpdateTaskConfig | 更新任务高级配置。 |
| ListTaskFlowConstants | 获取任务流常量列表。 |
| BackFill | 给任务编排补数据。 |
| UpdateTaskTimeVariables | 更新任务时间变量。 |
| ListTaskFlowTimeVariables | 获取任务流时间变量列表。 |
| UpdateTaskFlowCooperators | 更新任务流相关人员列表。 |
| UpdateTaskFlowTimeVariables | 更新任务流时间变量。 |
| CreateScenario | 创建业务场景，也可以将任务流按业务场景进行分组。 |
| DeleteScenario | 删除业务场景。 |
| UpdateSLARules | 更新任务流SLA超时提醒。 |
| GetRuleNumLimitOfSLA | 获取任务编排自定义SLA规则的限制数量，自定义的SLA规则数量不可超过该限制数。 |
| GetIntervalLimitOfSLA | 获取任务流允许配置SLA超时规则时，其最小调度周期限制。 |
| ListDefaultSLARules | 获取默认SLA超时提醒规则。 |
| ListTaskFlowCooperators | 获取任务流相关人列表。 |
| ListSLARules | 获取自定义SLA规则列表。 |
| GetTask | 移动任务流至指定业务场景。 |
| MoveTaskFlowToScenario | 按照任务流节点ID获取指定节点的配置，包括任务的时间变量。 |
| GetTaskFlowNotification | 获取任务流通知设置。 |
| UpdateTaskName | 更新任务名称。 |

数据管理

| UpdateTaskOutput | 更新任务节点的输出变量。 |
|---|---|
| DeleteTaskFlowEdgesByCondition | 按照多条件删除任务流边。 |
| ListTaskFlowEdgesByCondition | 多条件获取指定任务流DAG图的边。 |
| AddTaskFlowEdges | 为已存在的任务流节点建立有向边。 |
| UpdateTaskFlowNameAndDesc | 更新任务流名称和描述。 |
| GetTaskFlowGraph | 获取任务流的DAG图。 |
| UpdateTaskFlowEdges | 批量更新指定任务流的指定边的起点节点和终点节点。 |
| UpdateTaskFlowOwner | 更新任务流Owner。 |
| UpdateTaskFlowSchedule | 更新任务流调度配置。 |
| UpdateTaskFlowRelations | 全量更新任务流边。 |
| UpdateTaskFlowNotification | 更新任务流通知设置。 |
| ListTasksInTaskFlow | 获取指定任务流的任务节点列表。 |
| CreateTaskFlow | 创建任务流。 |
| SuspendTaskFlowInstance | 暂停运行中的任务流实例。 |
| ReRunTaskFlowInstance | 重跑任务流实例。 |
| MakeTaskFlowInstanceSuccess | 将指定任务流的状态设置为成功。 |
| DeleteTask | 删除任务流任务。 |
| PublishAndDeployTaskFlow | 发布并部署指定任务流。 |
| StopTaskFlowInstance | 停止运行中的任务流实例。 |
| CreateTask | 创建任务流任务。 |

### 逻辑库表

| API | 描述 |
|---|---|
| GetDBTopology | 获取逻辑库与其对应物理分库的拓扑信息。 |

### 用户管理

#### RegisterUser

DMS企业版用户的**管理员**（即产品内【系统管理】-【用户管理】中的管理员角色的用户）都可以通过这个接口增加录入本企业的新用户。

**请求参数**

数据管理

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RegisterUser | 系统规定参数。取值：RegisterUser。 |
| Tid | Long | 否 | -1 | 租户ID。 |
| Uid | String | 是 | 12345678 | 需要录入用户的阿里云UID。 |
| UserNick | String | 否 | dmstest | 用户名称。 |
| RoleNames | String | 否 | USER,DBA | 用户角色，取值和说明如下： USER：普通用户 DBA：DBA ADMIN：管理员 SECURITY ADMIN：安全管理员 _ 说明为空则初始化为“普通用户”，可选”普通用户”、”DBA”、”管理员”、”安全管理员”四个的任意组合，组合多个角色，传递时用*英文逗号*拼接。 |
| Mobile | String | 否 | 130000000xx | 联系电话。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 403 | 错误码。 |
| ErrorMessage | String | The specified user already exists. | 错误消息。 |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例数据管理

```
&Tid=-1 &Uid=12345678 &UserNick=dmstest
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
      <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success": true
}
```

#### DisableUser

此OpenAPI为产品内【系统管理】-【用户管理】内的“禁用用户”功能，支持DMS企业版内的“管理员”角色用户通过调用API的方式对暂时不需要的云账号进行产品内的禁用操作。禁用后，对应云账号开通的数据源权限、数据owner配置、DBA配置均会回收与失效。 禁用只是临时限制该云账号不能登录本企业的DMS企业版产品，并不是禁用云账号本身。

**说明**

禁用的效果是用户通过该账号不再能登录到DMS企业版（除非再次启用），此时仍占用企业开通规格。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DisableUser | 系统规定参数。取值：DisableUser。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Uid | String | 是 | 12345 | 阿里云账号UID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据管理

| ErrorCode | String | 403 | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | The specified user not exists. | 错误消息。 |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Tid=-1 &Uid=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId":"34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success":true
}
```

#### EnableUser

此OpenAPI为产品内【系统管理】-【用户管理】内的“启用用户”功能，支持DMS企业版内的“管理员”角色用户，通过调用API的方式对先前禁用的云账号进行产品内的启用操作。启用后，对应云账号可恢复产品的登录和相关使用。 启用只是解除该云账号之前禁用不能登录本企业的DMS企业版产品的限制，非云账号本身

**说明**

的其他操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据管理

| Action | String | 是 | EnableUser | 系统规定参数。取值：EnableUser。 |
|---|---|---|---|---|
| Tid | Long | 是 | -1 | 租户ID。 |
| Uid | String | 是 | 12345 | 阿里云账号UID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 403 | 错误码。 |
| ErrorMessage | String | The specified user not exists. | 错误消息。 |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Tid=-1 &Uid=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success": true
}
```

数据管理

#### UpdateUser

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateUser | 系统规定参数。取值：UpdateUser。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Uid | Long | 是 | 123456789 | 待更新的用户UID。 |
| UserNick | String | 否 | test | 用户名称。 |
| RoleNames | String | 否 | ADMIN,DBA | 用户角色列表，角色取值参考RegisterUser接口。 |
| Mobile | String | 否 | 188xxxxxxxx | 用户钉钉号（手机号码）。 |
| MaxExecuteCou nt | Long | 否 | 1000 | 当天查询上限次数。 |
| MaxResultCount | Long | 否 | 1000 | 当天查询上限行数。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | E9BEBF41-4F69- 4605-A5D5- A67955173941 | API请求唯一ID。 |
| Success | Boolean | false | 更新用户是否成功。 |

**示例**

数据管理请求示例

```
&Tid=-1 &Uid=123456789 &UserNick=test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E9BEBF41-4F69-4605-A5D5-A67955173941</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "E9BEBF41-4F69-4605-A5D5-A67955173941",
  "Success": true
}
```

#### DeleteUser

此OpenAPI为产品内【系统管理】-【用户管理】内的“删除用户”功能，支持DMS企业版内的“管理员”角色用户通过调用API的方式对不再需要的云账号进行产品内的删除操作。删除后，对应云账号开通的数据源权限、数据owner配置、DBA配置均会回收与失效。 删除只是去除与本企业的DMS企业版产品内的用户的关联关系，并不是删除云账号本身。

**说明**

删除的效果是用户通过该账号不再能登录到DMS企业版（除非再次加入）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteUser | 系统规定参数。取值：DeleteUser。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Uid | String | 是 | 12345 | 阿里云账号UID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据管理

| ErrorCode | String | 403 | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | The specified user not exists. | 错误消息。 |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Tid=-1 &Uid=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId":"34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success":true
}
```

#### ListUsers

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListUsers | 系统规定参数。取值：ListUsers。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Role | String | 否 | DBA | 角色，取值为参考RegisterUser接口。 |

数据管理

| UserState | String | 否 | NORMAL | 用户状态，取值和说明如下： NORMAL：正常 DISABLE：禁用 DELETE：已删除 |
|---|---|---|---|---|
| SearchKey | String | 否 | test | 搜索关键字。 |
| PageNumber | Integer | 否 | 1 | 页码。 |
| PageSize | Integer | 否 | 50 | 每页记录数。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 98D35416-2B92- 4CE5-8FD2- B1E61E165536 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 1 | 满足条件的记录总数。 |
| UserList | Array of User |  | 用户详情列表。 |
| User |  |  |  |
| CurExecuteCo unt | Long | 0 | 当天查询次数。 |
| CurResultCoun t | Long | 0 | 当天查询行数。 |
| LastLoginTime | String | 2020-02-02 00:00:00 | 最后登录时间。 |
| MaxExecuteCo unt | Long | 1000 | 当天查询次数上限。 |

数据管理

| MaxResultCou nt | Long | 1000 | 当天查询行数上限。 |
|---|---|---|---|
| Mobile | String | 188xxxxx | 钉钉号（手机号）。 |
| NickName | String | test | 名称。 |
| ParentUid | String | 143214352 | 父账号UID。 |
| RoleIdList | List | 1 | 角色ID列表。 |
| RoleNameList | List | ADMIN | 角色列表。 |
| State | String | NORMAL | 用户状态。 |
| Uid | String | 14324321533 | 用户阿里云UID。 |
| UserId | String | 1 | 用户ID。 |

**示例**

请求示例

```
&Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<UserList>
    <User>
        <RoleIdList>
            <RoleIds>3</RoleIds>
            <RoleIds>1</RoleIds>
        </RoleIdList>
        <State>NORMAL</State>
        <RoleNameList>
            <RoleNames>ADMIN</RoleNames>
            <RoleNames>USER</RoleNames>
        </RoleNameList>
        <NickName>xxx</NickName>
        <UserId>2</UserId>
        <Uid>111</Uid>
    </User>
    <User>
        <RoleIdList>
            <RoleIds>1</RoleIds>
            <RoleIds>3</RoleIds>
        </RoleIdList>
        <State>NORMAL</State>
        <RoleNameList>
            <RoleNames>USER</RoleNames>
            <RoleNames>ADMIN</RoleNames>
        </RoleNameList>
        <NickName>xxx[子账号]</NickName>
        <ParentUid>111</ParentUid>
        <UserId>1</UserId>
        <Uid>111</Uid>
    </User>
</UserList> <TotalCount>2</TotalCount> <RequestId>2D346B20-BF4A-4C96-8295-DE8EB9BF5B90</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "UserList": {
    "User": [
      {
        "RoleIdList": {
          "RoleIds": [
```

`3,` ]

```json
        },
        "State": "NORMAL",
        "RoleNameList": {
          "RoleNames": [
            "ADMIN",
            "USER"
```

]

```json
        },
        "NickName": "xxx",
        "UserId": 2,
        "Uid": "111"
      },
      {
        "RoleIdList": {
          "RoleIds": [
```

`1,` ]

```json
        },
        "State": "NORMAL",
        "RoleNameList": {
          "RoleNames": [
            "USER",
            "ADMIN"
```

]

```json
        },
        "NickName": "xxx[子账号]",
        "ParentUid": "111",
        "UserId": 1,
        "Uid": "111"
      }
```

]

```json
  },
  "TotalCount": 2,
  "RequestId": "2D346B20-BF4A-4C96-8295-DE8EB9BF5B90",
  "Success": true
}
```

#### ListUserTenants

**请求参数**

数据管理

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListUserTenants | 系统规定参数。取值：ListUserTenants。 |
| RegionId | String | 是 | cn-hangzhou | 选择DMS的服务地域，用于调用该接口。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | CA1F4A4D-EE49- 472F-8DF9- F537101E263A | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TenantList | Array of Tenant |  | 租户信息列表。 |
| Status | String | ACTIVE | 租户状态。取值： ACTIVE：活跃，表示用户正处于当前租户下。 IN ACTIVE：非活跃。 _ |
| TenantName | String | test | 租户名。 |
| Tid | Long | -1 | 租户ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<RequestId>CA1F4A4D-EE49-472F-8DF9-F537101E263A</RequestId> <TenantList>
    <Status>ACTIVE</Status>
    <TenantName>test1</TenantName>
    <Tid>-1</Tid>
</TenantList> <TenantList>
    <Status>IN_ACTIVE</Status>
    <TenantName>test2</TenantName>
    <Tid>-2</Tid>
</TenantList> <TenantList>
    <Status>IN_ACTIVE</Status>
    <TenantName>tes</TenantName>
    <Tid>-3</Tid>
</TenantList>
```

`JSON` 格式

```json
{
  "RequestId": "CA1F4A4D-EE49-472F-8DF9-F537101E263A",
  "TenantList": [
    {
      "Status": "ACTIVE",
      "TenantName": "test1",
      "Tid": -1
    },
    {
      "Status": "IN_ACTIVE",
      "TenantName": "test2",
      "Tid": -2
    },
    {
      "Status": "IN_ACTIVE",
      "TenantName": "tes",
      "Tid": -3
    }
```

]

```
}
```

#### GetUserActiveTenant

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetUserActiveTe nant | 系统规定参数。取值：GetUserActiveTenant。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域，用于调用该接口。 说明请根据应用所在地就近选择。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | E20EAB9F-A3DB- 42EC-BD0C- 102A886340F5 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| Tenant | Struct |  | 租户信息。 |
| Status | String | ACTIVE | 租户状态。取值： ACTIVE：活跃，表示用户正处于当前租户下。 IN ACTIVE：非活跃。 _ |
| TenantName | String | test | 租户名。 |
| Tid | Long | -1 | 租户ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetUserActiveTenant
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<Tenant>
    <Status>ACTIVE</Status>
    <TenantName>test</TenantName>
    <Tid>-1</Tid>
</Tenant> <RequestId>E20EAB9F-A3DB-42EC-BD0C-102A886340F5</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "Tenant": {
    "Status": "ACTIVE",
    "TenantName": "test",
    "Tid": -1
  },
  "RequestId": "E20EAB9F-A3DB-42EC-BD0C-102A886340F5",
  "Success": true
}
```

#### GetUser

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetUser | 系统规定参数。取值：GetUser。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Uid | String | 否 | 123344235 | 阿里云UID。 |
| UserId | String | 否 | 1343 | 用户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |

数据管理

| RequestId | String | CFF30064-5985- 4ACB-B3F9- 9557596913C8 | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |
| User | Struct |  | 用户信息。 |
| CurExecuteCo unt | Long | 0 | 当天查询次数。 |
| CurResultCoun t | Long | 0 | 当天查询行数。 |
| LastLoginTime | String | 2020-02-02 00:00:00 | 最后登录时间。 |
| MaxExecuteCo unt | Long | 1000 | 当天查询次数上限。 |
| MaxResultCou nt | Long | 1000 | 当天查询行数上限。 |
| Mobile | String | 138xxxxxxxx | 用户手机号码。 |
| NickName | String | nickName | 用户名称。 |
| ParentUid | Long | 12345352 | 主账号阿里云Uid。 |
| RoleIdList | List | 1 | 角色ID列表。 |
| RoleNameList | List | 普通用户 | 角色列表。 |
| State | String | NORMAL | 用户状态。 |
| Uid | String | 1243215435 | 用户阿里云UID。 |
| UserId | String | 122 | 用户ID。 |

**示例**

请求示例

```
&Tid=-1
```

`&<`公共请求参数> 数据管理正常返回示例 `XML` 格式

```xml
<User>
    <RoleIdList>
        <RoleIds>1</RoleIds>
        <RoleIds>4</RoleIds>
        <RoleIds>3</RoleIds>
        <RoleIds>2</RoleIds>
    </RoleIdList>
    <State>NORMAL</State>
    <RoleNameList>
        <RoleNames>普通用户</RoleNames>
```

`<RoleNames>`安全管理员`</RoleNames>`

```xml
        <RoleNames>管理员</RoleNames>
        <RoleNames>DBA</RoleNames>
    </RoleNameList>
    <NickName>xxx</NickName>
    <ParentUid>114324325</ParentUid>
    <UserId>432143</UserId>
    <Uid>41234234324</Uid>
</User> <RequestId>CFF30064-5985-4ACB-B3F9-9557596913C8</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "User": {
    "RoleIdList": {
      "RoleIds": [
```

`1,` `4,` `3,` ]

```json
    },
    "State": "NORMAL",
    "RoleNameList": {
      "RoleNames": [
```

"普通用户`",` "安全管理员`",` "管理员`",`

```
        "DBA"
```

]

```json
    },
    "NickName": "xxx",
    "ParentUid": "114324325",
    "UserId": 432143,
    "Uid": "41234234324"
  },
  "RequestId": "CFF30064-5985-4ACB-B3F9-9557596913C8",
  "Success": true
}
```

### 实例管理

#### ListServers

提供对DMS中机器的查询能力，支持灵活的分页与排序功能。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Tid | Long | Query | 否 | -1 | 租户ID。 取值范围：<1, 9223372036854775807 > |
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| Keyword | Strin g | Query | 否 | sg- bp1i4c0xgq0g7uw**** | 搜索关键词。 |

| 数据管理 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageIndex | Integ er | Query | 否 | 1 | 第几页。 |
| PageSize | Integ er | Query | 否 | 10 | 每页数据量。 |
| Sorter | Strin g | Query | 否 | XXX | 用于排序的字段，可选值为机器名称或机器IP。 |
| Order | Strin g | Query | 否 | ASC | 排列顺序，取值： DESC： 降序排列。 ASC： 升序排列。 |
| body | Array | Query | 否 | 二进制文件 | 请求体参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ServerList | Array | test | 机器列表。 |
| -Id | String | 1 | 机器ID。 |
| -ServerName | String | test | 机器名称。 |
| -Ip | String | 127.XX.XX.1 | IP地址。 |
| -SshPort | Integer | 22 | SSH服务默认使用的端口号，用于安全的远程登录和文件传输。 |
| -User | String | root | 用户名。 |
| -Password | String | ****** | 密码。 |
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。可用于定位日志，排查问题。 |
| ErrorCode | String | UnknownError | 调用失败时，返回的错误码。 |
| ErrorMessage | String | UnknownError | 调用失败时，返回的错误信息。 |

| 开发指南·API参考 |  |  | 数据管理 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功，返回值： true ：请求成功。 false ：请求失败。 |
| TotalCount | Integer | 1 | 数据总数。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "TotalCount":1,
 "RequestId":"0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
 "ServerList":[
  {
   "User":"root",
   "ServerName":"test",
   "Ip":"127.XX.XX.1",
   "Id":"1",
   "SshPort":22,
   "Password":"******"
  }
```

`],`

```json
 "ErrorCode":"UnknownError",
 "ErrorMessage":"UnknownError",
 "Success":true
}
```

`XML` 格式数据管理

```xml
<TotalCount>1</TotalCount> <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId> <ServerList>
 <User>root</User>
 <ServerName>test</ServerName>
 <Ip>127.XX.XX.1</Ip>
 <Id>1</Id>
 <SshPort>22</SshPort>
 <Password>******</Password>
</ServerList> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

#### ListServerGroups

提供对DMS中机器集群的查询功能，支持灵活的筛选条件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Tid | Long | Query | 否 | -1 | 租户ID。 取值范围：<1, 9223372036854775807 > |
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| Keyword | Strin g | Query | 否 | sg- bp1i4c0xgq0g7uw**** | 搜索关键词。 |
| PageIndex | Integ er | Query | 否 | 1 | 第几页。 |
| PageSize | Integ er | Query | 否 | 10 | 每页数据量。 |
| Sorter | Strin g | Query | 否 | XXX | 用于排序的字段，可选值为机器集群ID或机器集群名称。 |
| Order | Strin g | Query | 否 | DESC | 排列顺序，取值： DESC： 降序排列。 ASC： 升序排列。 |

**返回数据**

数据管理

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ServerGroupLi st | Array | test | 机器集群的列表，用于对机器进行逻辑分组管理。 |
| - SlaveServerLis t | Array | test | 从机器信息列表。 |
| --Id | String | 1 | 机器ID。 |
| --ServerName | String | test | 机器名称。 |
| --Ip | String | 192.XXX.XX.1 | IP地址。 |
| --SshPort | Integer | 22 | SSH服务默认使用的端口号，用于安全的远程登录和文件传输。 |
| --User | String | root | 用户名。 |
| --Password | String | ****** | 密码。 |
| -Id | String | sg- bp1i4c0xgq0g7uw* *** | 机器集群ID。 |
| -GroupName | String | test | 机器集群名称。 |
| -MasterServer | Struct | 192.XXX.XX.1:8080 | 主机器信息。 |
| --Id | String | 1 | 机器ID。 |
| --ServerName | String | test | 机器名称。 |
| --Ip | String | 192.XXX.XX.1 | IP地址。 |
| --SshPort | Integer | 22 | SSH服务默认使用的端口号，用于安全的远程登录和文件传输。 |
| --User | String | root | 用户名。 |
| --Password | String | ****** | 密码。 |

| 数据管理 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。可用于定位日志，排查问题。 |
| ErrorCode | String | UnknownError | 调用失败时，返回的错误码。 |
| ErrorMessage | String | UnknownError | 调用失败时，返回的错误信息。 |
| Success | Boolean | true | 请求是否成功，返回值： true ：请求成功。 false ：请求失败。 |
| TotalCount | Integer | 1 | 数据总数。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式数据管理

```json
{
 "TotalCount":1,
 "RequestId":"0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
 "ErrorCode":"UnknownError",
 "ErrorMessage":"UnknownError",
 "ServerGroupList":[
  {
   "GroupName":"test",
   "MasterServer":[
    {
     "User":"root",
     "ServerName":"test",
     "Ip":"192.XXX.XX.1",
     "Id":"1",
     "SshPort":22,
     "Password":"******"
    }
```

`],`

```json
   "SlaveServerList":[
    {
     "User":"root",
     "ServerName":"test",
     "Ip":"192.XXX.XX.1",
     "Id":"1",
     "SshPort":22,
     "Password":"******"
    }
```

`],`

```json
   "Id":"sg-bp1i4c0xgq0g7uw****"
  }
```

`],`

```json
 "Success":true
}
```

`XML` 格式数据管理

```xml
<TotalCount>1</TotalCount> <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <ServerGroupList>
 <GroupName>test</GroupName>
 <MasterServer>
  <User>root</User>
  <ServerName>test</ServerName>
  <Ip>192.XXX.XX.1</Ip>
  <Id>1</Id>
  <SshPort>22</SshPort>
  <Password>******</Password>
 </MasterServer>
 <SlaveServerList>
  <User>root</User>
  <ServerName>test</ServerName>
  <Ip>192.XXX.XX.1</Ip>
  <Id>1</Id>
  <SshPort>22</SshPort>
  <Password>******</Password>
 </SlaveServerList>
 <Id>sg-bp1i4c0xgq0g7uw****</Id>
</ServerGroupList> <Success>true</Success>
```

#### RegisterInstance

DMS企业版用户的**管理员、****DBA**（即产品内【系统管理】-【用户管理】中的管理员与DBA角色的用户）都可以通过这个接口增加录入本企业的新数据库实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RegisterInstance | 系统规定参数。取值：RegisterInstance。 |
| Tid | Long | 是 | -1 | 租户ID。 |

数据管理

| InstanceType | String | 是 | MySQL | 数据库类型，取值为： MySQL SQLServer PostgreSQL Oracle DRDS OceanBase Mongo Redis |
|---|---|---|---|---|
| InstanceSource | String | 是 | RDS | 数据库实例来源，取值和说明如下： PUBLIC OWN：代表公网自建实例 _ RDS：代表RDS实例 ECS OWN：代表ECS自建实例 _ VPC IDC：代表VPC IDC自建实例 _ |
| NetworkType | String | 是 | VPC | 网络类型。 |
| EnvType | String | 是 | product | 环境类型，取值和说明如下： product：生产环境 dev：开发环境 pre：预发环境 test：测试环境 sit：SIT环境 uat：UAT环境 pet：压测环境 stag：STAG环境 |
| Host | String | 是 | dmstest.rds.aliy un.com | 目标数据库的主机地址。 |
| Port | Integer | 是 | 3306 | 目标数据库的访问端口。 |
| DatabaseUser | String | 是 | dmstest | 数据库访问账号。 |
| DatabasePasswo rd | String | 是 | password | 数据库访问密码。 |
| InstanceAlias | String | 是 | 测试实例 | 实例名称，后续帮助用户快速区分定位。 |
| DbaUid | Long | 是 | 12345678 | 实例的DBA，传入DBA的阿里云UID。 |
| SafeRule | String | 是 | 测试使用 | 实例的安全规则，传入企业内的安全规则名称。 |

数据管理

| QueryTimeout | Integer | 是 | 60 | 查询超时时间，单位：s（秒）。 |
|---|---|---|---|---|
| ExportTimeout | Integer | 是 | 600 | 导出超时时间，单位：s（秒）。 |
| EcsInstanceId | String | 否 | i-xxxxxxxxx | ECS的实例ID。 说明 InstanceSource取值为ECS自建库此值必传。 |
| VpcId | String | 否 | vpc- xxxxxxxxxxxxxx xxxxxxx | VPC ID。 说明 InstanceSource取值为VPC专线IDC时此值必传。 |
| EcsRegion | String | 否 | cn-hangzhou | 实例所在区域。 说明 InstanceSource取值为RDS、ECS自建库、VPC专线 IDC时此值必传。 |
| Sid | String | 否 | dmstest | SID/数据库。 说明 InstanceType取值为PostgreSQL、Oracle时此值必传。 |
| DataLinkName | String | 否 | dblink test _ | 跨库查询DataLink名称。 |
| DdlOnline | Integer | 否 | 2 | 【重点关注】是否使用online服务，目前仅支持MySQL和PolarDB。 0 ：不使用 1 ：原生onlineDDL优先 2 ：DMS无锁表结构变更优先 |
| UseDsql | Integer | 否 | 1 | 是否启用跨实例查询，取值： 0：不开启 1：开启 |
| SkipTest | Boolean | 否 | true | 是否跳过测试连接，取值： true：跳过测试连接。 false：不跳过测试连接。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

数据管理

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 404 | 错误码。 |
| ErrorMessage | String | The specified instance already exists. | 错误消息。 |
| RequestId | String | F4E2A94B-604F- 43FF-93E7- F4EE3DCF412E | 请求唯一ID。 |
| Success | Boolean | true | true：录入成功 false：录入失败 |

**示例**

请求示例

```
&Tid=-1 &InstanceType=MySQL &InstanceSource=RDS &NetworkType=VPC &EnvType=product &Host=dmstest.rds.aliyun.com &Port=3306 &DatabaseUser=dmstest &DatabasePassword=password
```

`&InstanceAlias=`测试实例

```
&DbaUid=12345678
```

`&SafeRule=`测试使用

```
&QueryTimeout=60 &ExportTimeout=600
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>D4F02899-CE79-4DFD-9893-5217DA70B363</RequestId>
      <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "F4E2A94B-604F-43FF-93E7-F4EE3DCF412E",
    "Success": true
}
```

数据管理

**Python sdk示例**

示例为VPC专线实例的录入。

```
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkdms_enterprise.request.v20181101.RegisterInstanceRequest import RegisterI nstanceRequest client = AcsClient(
    "<your-access-key-id>",
    "<your-access-key-secret>",
    "<your-region-id>"
```

)
# VPC_IDC实例注册示例
# 租户`ID`

```
request.set_Tid(1)
```

# 实例`host`

```
request.set_Host("192.168.16.113")
```

# 实例`port`

```
request.set_Port(3314)
```

# 实例`db`类型 `eg : MySQL`

```
request.set_InstanceType("MySQL")
```

# 实例来源 `eg : VPC_IDC`

```
request.set_InstanceSource("VPC_IDC")
```

# 网络类型 `type: eg : VPC`

```bash
request.set_NetworkType("VPC") request.set_EnvType("PRODUCT")
# request.set_EcsInstanceId()
```

# 实例 `vpc id`

```bash
request.set_VpcId（"实例 VPC ID"）
# 实例 ecs region eg: cn-hangzhou
request.set_EcsRegion（"实例 ecs region"）
# request.set_Sid();
```

# 实例`db`登录用户
`request.set_DatabaseUser`（"实例`db`登录用户"）
# 实例`db`登录密码
`request.set_DatabasePassword`（"实例`db`登录密码"）
# 实例别名, 方便`DMS`企业版里面区分实例用
`request.set_InstanceAlias`（"实例别名"）
# 实例`dba` 阿里云`uid`（此用户必须先在`DMS`企业版录入, 或者使用`API`提前录入）

```
request.set_DbaUid(-1)
```

`request.set_SafeRule`（`"DMS`企业版里面配置的安全规则的规则名"）

```
request.set_QueryTimeout(60) request.set_ExportTimeout(600) response = client.do_action_with_exception(request) print response
```

#### ListInstances

数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListInstances | 系统规定参数。取值：ListInstances。 |
| Tid | Long | 否 | -1 | 租户ID。 |
| SearchKey | String | 否 | test | 搜索关键字。 |
| DbType | String | 否 | MySQL | 数据库类型。 |
| EnvType | String | 否 | product | 环境类型。 |
| InstanceSource | String | 否 | RDS | 实例来源。 |
| NetType | String | 否 | VPC | 实例网络环境，取值参考RegisterInstance接口。 |
| InstanceState | String | 否 | NORMAL | 实例状态，取值和解释如下： NORMAL：正常使用 DISABLE：禁用 |
| PageNumber | Integer | 否 | 1 | 页码。 |
| PageSize | Integer | 否 | 50 | 每页多少条数据，取值不超过100。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| InstanceList | Array of Instance |  | 实例列表。 |
| Instance |  |  |  |

数据管理

| DataLinkName | String | dblink test _ | DataLink名称。 |
|---|---|---|---|
| DatabasePass word | String | ****** | 数据库用户密码。 |
| DatabaseUser | String | dbUser | 数据库用户名。 |
| DbaId | String | 1 | 实例DBA ID。 |
| DbaNickName | String | dbaName | DBA名称。 |
| DdlOnline | Integer | 1 | 实例onlineddl配置。 |
| EcsInstanceId | String | xxx | ECS实例ID。 |
| EcsRegion | String | cn-hangzhou | ECS实例所属地域。 |
| EnvType | String | product | 实例环境。 |
| ExportTimeout | Integer | 600 | 导出超时时间。 |
| Host | String | xxx.xxx.xxx.xxx | 实例连接地址。 |
| InstanceAlias | String | test | 实例别名。 |
| InstanceId | String | 1 | 实例ID。 |
| InstanceSourc e | String | RDS | 实例来源。 |
| InstanceType | String | mysql | 实例数据库类型。 |
| OwnerIdList | List | 1 | 数据库所属Owner ID列表。 |
| OwnerNameLi st | List | 11 | 数据库所属Owner名称列表。 |
| Port | Integer | 3306 | 实例端口。 |
| QueryTimeout | Integer | 60 | 查询超时时间。 |

数据管理

| SafeRuleId | String | 1 | 实例安全规则ID。 |
|---|---|---|---|
| Sid | String | test | 实例SID。 |
| State | String | NORMAL | 实例状态。 |
| UseDsql | Integer | 1 | 实例是否开启跨库查询。 |
| VpcId | String | xxx | VPC ID。 |
| RequestId | String | B4B07137-F6AE- 4756-8474- 7F92BB6C4E04 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 0 | 满足条件的实例总个数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>7</TotalCount> <RequestId>98D35416-2B92-4CE5-8FD2-B1E61E165536</RequestId> <Success>true</Success> <InstanceList> </InstanceList>
```

`JSON` 格式

```json
{
  "TotalCount": 7,
  "RequestId": "98D35416-2B92-4CE5-8FD2-B1E61E165536",
  "Success": true,
  "InstanceList": {
    "Instance": [
```

]

```
  }
}
```

数据管理

#### GetInstance

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetInstance | 系统规定参数。取值：GetInstance。 |
| Host | String | 是 | xxxx.mysql.rds.a liyuncs.com | 实例连接地址。 |
| Port | Integer | 是 | 3306 | 实例连接端口。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Sid | String | 否 | test | 实例SID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| Instance | Struct |  | 实例详细信息。 |
| DataLinkName | String | test | 实例DataLink名称。 |
| DatabasePass word | String | ****** | 实例登录账号密码。 |
| DatabaseUser | String | dbuser | 实例登录用户名。 |
| DbaId | String | 1 | 实例DBA ID，与ListUsers中的ID对应。 |
| DbaNickName | String | dbaname | 实例DBA名称。 |

数据管理

| DdlOnline | Integer | 1 | 实例onlineddl配置。 |
|---|---|---|---|
| EcsInstanceId | String | xxx | ECS实例ID。 |
| EcsRegion | String | cn-hangzhou | 实例所属地域。 |
| EnvType | String | test | 实例所属环境。 |
| ExportTimeout | Integer | 600 | 实例导出超时时间。 |
| Host | String | xxx.rwlb.rds.aliyun cs.com | 实例连接地址。 |
| InstanceAlias | String | test | 实例别名。 |
| InstanceId | String | 1 | 实例ID。 |
| InstanceSourc e | String | RDS | 实例来源。 |
| InstanceType | String | polardb | 实例DB类型。 |
| OwnerIdList | List | 88656 | Owner ID列表。 |
| OwnerNameLi st | List | xxx | Owner名称列表。 |
| Port | Integer | 3306 | 实例连接端口。 |
| QueryTimeout | Integer | 60 | 实例查询超时时间 |
| SafeRuleId | String | 1 | 实例所对应安全规则ID。 |
| Sid | String | test | 实例SID。 |
| State | String | NORMAL | 实例状态。 |
| UseDsql | Integer | 1 | 实例是否开启跨库查询。 |
| VpcId | String | xxx | 实例所属VPC ID。 |

数据管理

| RequestId | String | 8BE73E78-76E2- 46AA-970D- A4579A16CD4A | API请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 接口调用是否成功。 |

**示例**

请求示例

```
&Host=xxxx.mysql.rds.aliyuncs.com &Port=3306 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Instance>
    <SafeRuleId>1037</SafeRuleId>
    <UseDsql>1</UseDsql>
    <EcsInstanceId>pc-xxx</EcsInstanceId>
    <QueryTimeout>80</QueryTimeout>
    <Host>xxx.rwlb.rds.aliyuncs.com</Host>
    <InstanceAlias>test</InstanceAlias>
    <InstanceSource>RDS</InstanceSource>
    <InstanceId>24710</InstanceId>
    <DataLinkName>dblink_test</DataLinkName>
    <EnvType>dev</EnvType>
    <DdlOnline>0</DdlOnline>
    <VpcId>vpc-xxx</VpcId>
    <InstanceType>polardb</InstanceType>
    <DbaId>104442</DbaId>
    <Port>3306</Port>
    <DbaNickName>test[子账号]</DbaNickName>
    <State>NORMAL</State>
    <DatabaseUser>dmstest</DatabaseUser>
    <DatabasePassword>******</DatabasePassword>
    <EcsRegion>cn-hangzhou</EcsRegion>
    <ExportTimeout>300</ExportTimeout>
</Instance> <RequestId>8BE73E78-76E2-46AA-970D-A4579A16CD4A</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "Instance": {
    "SafeRuleId": 1037,
    "UseDsql": "1",
    "EcsInstanceId": "pc-xxx",
    "QueryTimeout": 80,
    "Host": "xxx.rwlb.rds.aliyuncs.com",
    "InstanceAlias": "test",
    "InstanceSource": "RDS",
    "InstanceId": 24710,
    "DataLinkName": "dblink_test",
    "EnvType": "dev",
    "DdlOnline": 0,
    "VpcId": "vpc-xxx",
    "InstanceType": "polardb",
    "DbaId": 104442,
    "Port": 3306,
    "DbaNickName": "test[子账号]",
    "State": "NORMAL",
    "DatabaseUser": "dmstest",
    "DatabasePassword": "******",
    "EcsRegion": "cn-hangzhou",
    "ExportTimeout": 300
  },
  "RequestId": "8BE73E78-76E2-46AA-970D-A4579A16CD4A",
  "Success": true
}
```

#### UpdateInstance

调用UpdateInstance更新实例，请先通过GetInstance API获取对应实例的完整信息，再根据具体需要修改的内容进行设置，然后再调用此API

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateInstance | 系统规定参数。取值：UpdateInstance。 |
| DatabasePasswo rd | String | 是 | ****** | 数据库账号密码。 |
| DatabaseUser | String | 是 | dbuser | 数据库账号。 |
| DbaId | String | 是 | 1 | 实例DBA ID，与ListUsers接口中的ID对应。 |

数据管理

| EnvType | String | 是 | test | 实例所属环境。 |
|---|---|---|---|---|
| ExportTimeout | Integer | 是 | 600 | 实例导出超时时间。 |
| Host | String | 是 | xxxx.mysql.rds.a liyuncs.com | 实例连接地址。 |
| InstanceAlias | String | 是 | test | 实例别名。 |
| InstanceId | String | 是 | 1 | 实例ID，与GetInstance中返回的ID对应。 |
| InstanceSource | String | 是 | RDS | 实例来源，取值可参考RegisterInstance中的提示。 |
| InstanceType | String | 是 | MySQL | 实例数据库类型，取值可参考RegisterInstance中的提示。 |
| Port | Integer | 是 | 3306 | 实例端口。 |
| QueryTimeout | Integer | 是 | 60 | 实例查询超时时间。 |
| SafeRuleId | String | 是 | 1 | 实例所属安全规则ID。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| EcsInstanceId | String | 否 | xxx | ECS实例ID。 |
| VpcId | String | 否 | xxx | 实例所属VPC ID。 |
| EcsRegion | String | 否 | cn-hangzhou | 实例所属地域。 |
| Sid | String | 否 | xxx | 实例SID。 |
| DataLinkName | String | 否 | datalink test _ | 实例DataLink名称。 |
| DdlOnline | Integer | 否 | 1 | 实例onlineddl设置，取值请参考RegisterInstance接口。 |
| UseDsql | Integer | 否 | 1 | 实例是否启用跨库查询。 |

数据管理

| SkipTest | Boolean | 否 | true | 是否跳过测试连接，取值如下： true：跳过测试连接。 false：不跳过测试连接。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | E9BEBF41-4F69- 4605-A5D5- A67955173941 | API请求ID。 |
| Success | Boolean | false | 更新实例是否成功。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E9BEBF41-4F69-4605-A5D5-A67955173941</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "E9BEBF41-4F69-4605-A5D5-A67955173941",
  "Success": true
}
```

#### DeleteInstance

注意此删除是指将DMS企业版中录入的实例从企业版的管理里面移除，不会导致您的实例下线

**请求参数**

数据管理

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteInstance | 系统规定参数，取值：DeleteInstance。 |
| Host | String | 是 | xxx.mysql.rds.ali yuncs.com | 待删除的实例连接地址。 |
| Port | Integer | 是 | 3306 | 待删除的实例链接端口。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Sid | String | 否 | testSid | 待删除的实例SID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误消息。 |
| RequestId | String | B4B07137-F6AE- 4756-8474- 7F92BB6C4E04 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Host=xxx.mysql.rds.aliyuncs.com &Port=3306 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>B4B07137-F6AE-4756-8474-7F92BB6C4E04</RequestId> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

数据管理 `JSON` 格式

```json
{"RequestId":"B4B07137-F6AE-4756-8474- 7F92BB6C4E04","ErrorCode":"UnknownError","ErrorMessage":"UnknownError","Success":"true"}
```

### 操作日志

#### GetOpLog

账户角色为**管理员**、**安全管理员**可调用该接口。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetOpLog | 系统规定参数。取值：GetOpLog。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| StartTime | String | 是 | 2018-11-01 10:00:00 | 开始时间，时间格式为*yyyy-MM-DD HH:mm:ss*。 |
| EndTime | String | 是 | 2018-11-01 11:00:00 | 结束时间，时间格式为*yyyy-MM-DD HH:mm:ss*。 |
| PageNumber | Integer | 是 | 3 | 页码，从1开始。 |
| PageSize | Integer | 是 | 30 | 每页记录数，取值： 30 50 100 |

数据管理

| Module | String | 否 | PERMISSION | 日志模块，缺省则对应时间段内所有模块返回，日志模块取值和说明如下： PERMISSION：权限 OWNER：数据Owner SQL CONSOLE：数据查询 _ SQL CONSOLE EXPORT：查询结 _ _ 果导出 DATA CHANGE：数据变更 _ DATA EXPORT：数据导出 _ SQL REVIEW：SQL审核 _ DT SYNC：库表同步 _ DT DETAIL：库表详情 _ DB TASK：任务管理 _ INSTANCE MANAGE：实例管理 _ USER MANAGE：用户管理 _ SECURITY RULE：安全规则 _ CONFIG MANAGE：配置管理 _ RESOURCE AUTH：资源授权 _ ACCESS WHITE IP：访问IP白名单 _ _ |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 403 | 错误码。 |
| ErrorMessage | String | 请求参数不合法 | 错误消息。 |
| OpLogDetails | Array of OpLogDetail |  | 操作日志详情列表。 |
| OpLogDetail |  |  |  |
| Database | String | dmstest prod data _ _ base@dmstest.rds. ..【测试实例】 | 数据库访问地址，只有当实例类型为LocalInstance时，这个参数才有值。 说明仅任务类型区域的各功能模块操作才有这个属性。 |
| Module | String | PERMISSION | 功能模块。 |
| OpContent | String | 申请权限 | 操作内容。 |

数据管理

| OpTime | String | 2018-11-01 10:00:00 | 操作时间。 |
|---|---|---|---|
| OrderId | Long | 1 | 工单号或任务号。 说明仅任务类型区域的各功能模块操作与系统管理任务管理功能模块的操作才有这个属性。 |
| UserId | Long | 12345678 | 阿里云UID。 |
| UserNick | String | dmstest | 用户显示名。 |
| RequestId | String | 47D56208-DB1D- 4FD3-BE32- 300E43185488 | 请求唯一ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 22 | 操作日志总条数。 |

**示例**

请求示例

```
&Tid=-1 &StartTime=2018-11-01 10:00:00 &EndTime=2018-11-01 11:00:00 &PageNumber=3 &PageSize=30
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<OpLogDetails>
    <OpLogDetail>
        <OpContent>(成功,行数:1)SELECT (data_length + index_length) AS store_capacity FRO
M information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39; AND `table_ schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;multi_db_multi_tbl&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:04:10</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:1)SELECT (data_length + index_length) AS store_capacity FRO
```

#
#
` 数据管理

```xml
M information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39; AND `table_ schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;multi_db_multi_tbl&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:04:06</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:24)show topology FROM multi_db_multi_tbl</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:03:55</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:1)SELECT (data_length + index_length) AS store_capacity FRO
M information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39; AND `table_ schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;user_log3&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:02:59</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:1)SELECT (data_length + index_length) AS store_capacity FRO
M information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39; AND `table_ schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;user_log3&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:02:49</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:1)show CREATE TABLE user_log3</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:34:05</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:9)SELECT `TABLE_NAME` FROM information_schema.tables WHERE
TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmstest_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
<OpTime>2018112214:33:54</OpTime>
```

数据管理

```xml
        <OpTime>2018-11-22 14:33:54</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:26:57</OpTime>
```

`<Module>`任务管理`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:55</OpTime>
```

`<Module>`任务管理`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:30</OpTime>
```

`<Module>`任务管理`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:11</OpTime>
```

`<Module>`任务管理`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:1)show CREATE TABLE multi_db_single_tbl</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:22:30</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:2)SELECT `TABLE_NAME` FROM information_schema.tables WHERE
TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmstest_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:22:15</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
<OpContent>(成功,行数:2)SELECT`TABLENAME`FROMinformationschema.tablesWHERE
```

数据管理

```xml
        <OpContent>(成功,行数:2)SELECT TABLE_NAME FROM information_schema.tables WHERE
TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmstest_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:19:31</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:19:25</OpTime>
```

`<Module>`任务管理`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:1)SELECT `TABLE_NAME` FROM information_schema.tables WHERE
TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmstest_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:18:57</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:18:46</OpTime>
```

`<Module>`任务管理`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:0)SELECT `TABLE_NAME` FROM information_schema.tables WHERE
TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmstest_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:04:13</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(成功,行数:0)SELECT `TABLE_NAME` FROM information_schema.tables WHERE
TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmstest_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:04:08</OpTime>
```

`<Module>`数据查询`</Module>`

```
    </OpLogDetail>
```

数据管理

```xml
    <OpLogDetail>
        <OpContent>(成功,行数:0)SELECT `TABLE_NAME` FROM information_schema.tables WHERE
TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmstest_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 12:11:41</OpTime>
```

`<Module>`数据查询`</Module>`

```xml
    </OpLogDetail>
    <OpLogDetail>
```

`<OpContent>`管理员或`DBA`编辑库`OWNER`，库名：`dmstest_database@dmstest.rds...(test)</OpC`

```xml
ontent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 12:11:14</OpTime>
        <Module>数据Owner</Module>
    </OpLogDetail>
    <OpLogDetail>
```

`<OpContent>`管理员或`DBA`编辑库`OWNER`，库名：`dmstest_prod_database@dmstest.rds...(test)`

```xml
</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_prod_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 12:11:07</OpTime>
        <Module>数据Owner</Module>
    </OpLogDetail>
</OpLogDetails> <TotalCount>22</TotalCount> <RequestId>47D56208-DB1D-4FD3-BE32-300E43185488</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "OpLogDetails": {
        "OpLogDetail": [{
            "OpContent": "(成功,行数:1)SELECT (data_length + index_length) AS store_capac
ity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `table_s chema` = &#39;dmstest_database&#39; AND `table_name` = &#39;multi_db_multi_tbl&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 20:04:10",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:1)SELECT (data_length + index_length) AS store_capac
ity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `table_s chema` = &#39;dmstest_database&#39; AND `table_name` = &#39;multi_db_multi_tbl&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
"OpTime":"2018-11-2220:04:06"
```

数据管理

```
            OpTime: 20181122 20:04:06,
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:24)show topology FROM multi_db_multi_tbl",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 20:03:55",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:1)SELECT (data_length + index_length) AS store_capac
ity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `table_s chema` = &#39;dmstest_database&#39; AND `table_name` = &#39;user_log3&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 20:02:59",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:1)SELECT (data_length + index_length) AS store_capac
ity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `table_s chema` = &#39;dmstest_database&#39; AND `table_name` = &#39;user_log3&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 20:02:49",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:1)show CREATE TABLE user_log3",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:34:05",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:9)SELECT `TABLE_NAME` FROM information_schema.tables
WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:33:54",
```

`"Module": "`数据查询"

```
        }, {
```

`"OpContent": "`新增`SQL`任务，任务号：`5486",`

```json
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:26:57",
```

`"Module": "`任务管理"

```
        }, {
```

`"OpContent": "`新增`SQL`任务，任务号：`5485",`

```json
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:23:55",
```

数据管理 p , `"Module": "`任务管理"

```
        }, {
```

`"OpContent": "`新增`SQL`任务，任务号：`5484",`

```json
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:23:30",
```

`"Module": "`任务管理"

```
        }, {
```

`"OpContent": "`新增`SQL`任务，任务号：`5483",`

```json
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:23:11",
```

`"Module": "`任务管理"

```json
        }, {
            "OpContent": "(成功,行数:1)show CREATE TABLE multi_db_single_tbl",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:22:30",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:2)SELECT `TABLE_NAME` FROM information_schema.tables
WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:22:15",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:2)SELECT `TABLE_NAME` FROM information_schema.tables
WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:19:31",
```

`"Module": "`数据查询"

```
        }, {
```

`"OpContent": "`新增`SQL`任务，任务号：`5482",`

```json
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:19:25",
```

`"Module": "`任务管理"

```json
        }, {
            "OpContent": "(成功,行数:1)SELECT `TABLE_NAME` FROM information_schema.tables
WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:18:57",
```

`"Module": "`数据查询"

```
        }, {
```

数据管理 `"OpContent": "`新增`SQL`任务，任务号：`5481",`

```json
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:18:46",
```

`"Module": "`任务管理"

```json
        }, {
            "OpContent": "(成功,行数:0)SELECT `TABLE_NAME` FROM information_schema.tables
WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:04:13",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:0)SELECT `TABLE_NAME` FROM information_schema.tables
WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 14:04:08",
```

`"Module": "`数据查询"

```json
        }, {
            "OpContent": "(成功,行数:0)SELECT `TABLE_NAME` FROM information_schema.tables
WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&#39;",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 12:11:41",
```

`"Module": "`数据查询"

```
        }, {
```

`"OpContent": "`管理员或`DBA`编辑库`OWNER`，库名：`dmstest_database@dmstest.rds...(tes`

```json
t)",
            "UserNick": "dmstest",
            "Database": "dmstest_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 12:11:14",
            "Module": "数据Owner"
        }, {
```

`"OpContent": "`管理员或`DBA`编辑库`OWNER`，库名：

```json
dmstest_prod_database@dmstest.rds...(test)",
            "UserNick": "dmstest",
            "Database": "dmstest_prod_database@dmstest.rds...(test)",
            "UserId": 12345678,
            "OpTime": "2018-11-22 12:11:07",
            "Module": "数据Owner"
        }]
    },
    "TotalCount": 22,
    "RequestId": "47D56208-DB1D-4FD3-BE32-300E43185488",
    "Success": true
}
```

数据管理

**SDK示例**

SDK使用基础信息参考：快速开始。 示例如下：

```
from aliyunsdkcore.client import AcsClient from aliyunsdkdms_enterprise.request.v20181101.GetOpLogRequest import GetOpLogRequest client = AcsClient(
    "<your-access-key-id>",
   "<your-access-key-secret>",
   "<your-region-id>"
```

) `request.set_Tid("`请输入你的企业租户`id")`

```
request.set_StartTime("2018-11-20 00:00:00") request.set_EndTime("2018-11-23 00:00:00") request.set_PageNumber(1) request.set_PageSize(50) response = client.do_action_with_exception(request) print response
```

### 审批流程

#### ListWorkFlowTemplates

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListWorkFlowTe mplates | 系统规定参数。取值：ListWorkFlowTemplates。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| SearchName | String | 否 | Admin | 搜索模板名。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |

数据管理

| ErrorMessage | String | UnknownError | 错误消息。 |
|---|---|---|---|
| RequestId | String | 41067071-0243- 4AAB-B3CF- 4DE6D54F53B4 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| WorkFlowTem plates | Array of WorkFlowTem plate |  | 审批模板列表。 |
| WorkFlowTem plate |  |  |  |
| Comment | String | test | 备注。 |
| CreateUserId | Long | 1234 | 创建人ID。 |
| Enabled | String | Y | 模板是否启用，取值和说明如下： Y：启用 N：禁用 |
| IsSystem | Integer | 1 | 是否系统定义的审批模板，取值和说明如下： 1：是 0：否 |
| TemplateId | Long | 12345 | 模板ID。 |
| TemplateNam e | String | Admin | 模板名称。 |
| WorkflowNode s | Array of WorkflowNode |  | 审批节点信息。 |
| WorkflowNode |  |  |  |
| Comment | String | test | 备注。 |
| CreateUserId | Long | 1234 | 创建人ID。 |
| NodeId | Long | 123 | 节点ID。 |
| NodeName | String | test | 节点名称。 |

数据管理

| NodeType | String | SYS | 节点类型，取值和说明如下： SYS：系统定义 USER LIST：用户自定义 _ |
|---|---|---|---|
| Position | Integer | 1 | 顺序。 |
| TemplateId | Long | 12345 | 模板ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListWorkFlowTemplates &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>41067071-0243-4AAB-B3CF-4DE6D54F53B4</RequestId> <Success>true</Success> <WorkFlowTemplates>
    <WorkFlowTemplate>
```

`<Comment>`系统定义审批线，仅需管理员审批`</Comment>`

```xml
        <WorkFlowNodes>
            <WorkFlowNode>
```

`<Comment>`系统节点，动态计算，由管理员来完成审批`</Comment>`

```xml
                <NodeName>Admin</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3763</NodeId>
                <TemplateId>6243</TemplateId>
            </WorkFlowNode>
        </WorkFlowNodes>
        <TemplateName>Admin</TemplateName>
        <Enabled>Y</Enabled>
        <IsSystem>1</IsSystem>
        <TemplateId>6243</TemplateId>
    </WorkFlowTemplate>
    <WorkFlowTemplate>
```

`<Comment>`系统定义审批线，先数据`Owner`审批，再`DBA`审批，最后`Admin`审批`</Comment>`

```xml
        <WorkflowNodes>
            <WorkFlowNode>
```

`<Comment>`系统节点，动态计算，由用户操作的资源对应的`Owner`来完成审批`</Comment>`

```xml
                <NodeName>Owner</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3762</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
<WorkFlowNode>
```

数据管理

```xml
            <WorkFlowNode>
```

`<Comment>`系统节点，动态计算，由用户操作的资源对应的`DBA`来完成审批`</Comment>`

```xml
                <NodeName>DBA</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3761</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
            <WorkFlowNode>
```

`<Comment>`系统节点，动态计算，由管理员来完成审批`</Comment>`

```xml
                <NodeName>Admin</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3763</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
        </WorkflowNodes>
        <TemplateName>Owner--&gt;DBA--&gt;Admin</TemplateName>
        <Enabled>Y</Enabled>
        <IsSystem>1</IsSystem>
        <TemplateId>6244</TemplateId>
    </WorkFlowTemplate>
</WorkFlowTemplates>
```

`JSON` 格式

```json
{
  "RequestId": "41067071-0243-4AAB-B3CF-4DE6D54F53B4",
  "Success": true,
  "WorkFlowTemplates": {
    "WorkFlowTemplate": [
      {
```

`"Comment": "`系统定义审批线，仅需管理员审批`",`

```json
        "WorkFlowNodes": {
          "WorkFlowNode": [
            {
```

`"Comment": "`系统节点，动态计算，由管理员来完成审批`",`

```json
              "NodeName": "Admin",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3763,
              "TemplateId": 6243
            }
```

]

```json
        },
        "TemplateName": "Admin",
        "Enabled": "Y",
        "IsSystem": 1,
        "TemplateId": 6243
      },
      {
```

`"Comment": "`系统定义审批线，先数据`Owner`审批，再`DBA`审批，最后`Admin`审批`",`

```json
        "WorkflowNodes": {
          "WorkFlowNode": [
{
```

数据管理

```
            {
```

`"Comment": "`系统节点，动态计算，由用户操作的资源对应的`Owner`来完成审批`",`

```json
              "NodeName": "Owner",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3762,
              "TemplateId": 6244
            },
            {
```

`"Comment": "`系统节点，动态计算，由用户操作的资源对应的`DBA`来完成审批`",`

```json
              "NodeName": "DBA",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3761,
              "TemplateId": 6244
            },
            {
```

`"Comment": "`系统节点，动态计算，由管理员来完成审批`",`

```json
              "NodeName": "Admin",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3763,
              "TemplateId": 6244
            }
```

]

```json
        },
        "TemplateName": "Owner-->DBA-->Admin",
        "Enabled": "Y",
        "IsSystem": 1,
        "TemplateId": 6244
      }
```

]

```
  }
}
```

#### ListWorkFlowNodes

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListWorkFlowNo des | 系统规定参数。取值：ListWorkFlowNodes。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| SearchName | String | 否 | admin | 搜索审批节点名称。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误消息。 |
| RequestId | String | CFD8FE00-36D9- 4C1B-940D- 65A7B73D9066 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| WorkflowNode s | Array of WorkflowNode |  | 审批节点信息。 |
| WorkflowNode |  |  |  |
| AuditUsers | Array of AuditUser |  | 审批人信息。 |
| AuditUser |  |  |  |
| NickName | String | test | 审批人名称。 |
| RealName | String | test | 审批人真实名。 |
| UserId | Long | 123 | 审批人用户ID，注意不是阿里云UID。 |
| Comment | String | test | 备注。 |
| CreateUserId | Long | 123 | 创建者用户ID，注意不是阿里云UID。 |
| CreateUserNic kName | String | test | 创建人名称。 |
| NodeId | Long | 123 | 节点ID。 |
| NodeName | String | test | 节点名称。 |

数据管理

| NodeType | String | SYS | 节点类型，取值和说明如下： SYS：系统定义 USER LIST：用户自定义 _ |
|---|---|---|---|

**示例**

请求示例

```
&Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<WorkFlowNodes>
    <WorkflowNode>
```

`<Comment>`系统节点，动态计算，由管理员来完成审批`</Comment>`

```xml
        <NodeName>Admin</NodeName>
        <NodeType>SYS</NodeType>
        <NodeId>3763</NodeId>
        <AuditUsers>
        </AuditUsers>
    </WorkflowNode>
</WorkFlowNodes> <RequestId>CFD8FE00-36D9-4C1B-940D-65A7B73D9066</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "WorkFlowNodes": {
    "WorkflowNode": [
      {
```

`"Comment": "`系统节点，动态计算，由管理员来完成审批`",`

```json
        "NodeName": "Admin",
        "NodeType": "SYS",
        "NodeId": 3763,
        "AuditUsers": {
          "AuditUser": []
        }
      }
```

]

```json
  },
  "RequestId": "CFD8FE00-36D9-4C1B-940D-65A7B73D9066",
  "Success": true
}
```

### 库表元数据

数据管理

#### SearchDatabase

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SearchDatabase | 系统规定参数。取值：SearchDatabase。 |
| PageNumber | Integer | 否 | 1 | 页码。 |
| SearchKey | String | 否 | testdb | 搜索数据库名称的关键字。 |
| Tid | Long | 否 | 1 | 租户ID。 |
| PageSize | Integer | 否 | 10 | 每页记录数。 |
| EnvType | String | 否 | product | 数据库的环境类型。 |
| SearchRange | String | 否 | HAS PERMSSION _ | 权限范围，取值和说明： HAS PERMSSION：有权限的 _ OWNER：我所有的 MY FOCUS：我关注的 _ UNKNOWN：不限 |
| SearchTarget | String | 否 | SINGLE DB _ | 搜索目标，取值和说明如下： DB：不限（不区分单库或逻辑库） SINGLE DB：单库 _ LOGIC DB：逻辑库 _ |
| DbType | String | 否 | MySQL | 数据库类型，取值为： MySQL SQLServer PostgreSQL Oracle DRDS OceanBase Mongo Redis |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

数据管理

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | E0D21075-CD3E- 4D98-8264- FD8AD04A63B6 | API请求ID。 |
| SearchDataba seList | Array of SearchDataba se |  | 搜索库详情列表。 |
| SearchDataba se |  |  |  |
| Alias | String | test | 数据库别名。 |
| DatabaseId | String | 1 | 数据库ID。 |
| DatalinkName | String | datalink name _ | 数据库所对应DataLink。 |
| DbType | String | mysql | 数据库类型，取值为： MySQL SQLServer PostgreSQL Oracle DRDS OceanBase Mongo Redis |
| DbaId | String | 1 | 数据库的DBA ID。 |
| Encoding | String | utf8 | 数据库编码。 |
| EnvType | String | product | 数据库的环境类型。 |
| Host | String | xxx.xxx.xxx.xxx | 库所在的实例对应连接地址。 |

数据管理

| Logic | Boolean | false | 是否为逻辑库，取值： true：是 false：否 |
|---|---|---|---|
| OwnerIdList | List | 1 | 数据库Owner ID列表。 |
| OwnerNameLi st | List | user1 | 数据库Owner名称列表。 |
| Port | Integer | 3306 | 数据库所对应实例端口。 |
| SchemaName | String | test | 数据库名。 |
| SearchName | String | test@xxx.xxx.xxx.x xx:3306 | 数据库搜索名。 |
| Sid | String | testSid | 库所对应实例SID。 |
| TotalCount | Long | 1 | 满足条件的记录总数。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&PageNumber=1 &SearchKey=testdb &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<TotalCount>1</TotalCount> <RequestId>E0D21075-CD3E-4D98-8264-FD8AD04A63B6</RequestId>
        <Encoding>utf8mb4</Encoding>
        <Host>pc-xxx.mysql.polardb.rds.aliyuncs.com</Host>
        <DbType>polardb</DbType>
        <EnvType>dev</EnvType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Logic>false</Logic>
        <DbaId>88653</DbaId>
        <OwnerNameList>
            <OwnerNames>dmstest</OwnerNames>
            <OwnerNames>xx</OwnerNames>
            <OwnerNames>xx[子账号]</OwnerNames>
        </OwnerNameList>
        <Port>3306</Port>
        <DatabaseId>117567</DatabaseId>
        <Alias>xx线下库</Alias>
        <SearchName>xxx@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306【xx线下库】</SearchNam
```

`e>`

```xml
        <DatalinkName>dblink_38</DatalinkName>
        <SchemaName>xxx_0000</SchemaName>
<Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "TotalCount": 1,
  "RequestId": "E0D21075-CD3E-4D98-8264-FD8AD04A63B6",
      {
        "Encoding": "utf8mb4",
        "Host": "pc-xxx.mysql.polardb.rds.aliyuncs.com",
        "DbType": "polardb",
        "EnvType": "dev",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            88656,
            104442
```

]

```json
        },
        "Logic": false,
        "DbaId": 88653,
        "OwnerNameList": {
          "OwnerNames": [
            "dmstest",
            "xx",
```

`"xx[`子账号`]"` ]

```json
        },
        "Port": 3306,
        "DatabaseId": 117567,
```

`"Alias": "xx`线下库`",`

```json
        "SearchName": "xxx@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306【xx线下库】",
        "DatalinkName": "dblink_38",
        "SchemaName": "xxx_0000"
      }
```

]

```json
  },
  "Success": true
}
```

#### SearchTable

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SearchTable | 系统规定参数。取值：SearchTable。 |
| Tid | Long | 否 | 1 | 租户ID。 |

数据管理

| SearchKey | String | 否 | test | 搜索表名称的关键字。 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 第几页。 |
| PageSize | Integer | 否 | 10 | 每页记录数。 |
| EnvType | String | 否 | PRODUCT | 数据库的环境类型。 |
| SearchTarget | String | 否 | LOGIC TABLE _ | 搜索表类型，取值如下： TABLE：表，包含物理表和逻辑表 SINGLE TABLE：物理表 _ LOGIC TABLE：逻辑表 _ |
| SearchRange | String | 否 | OWNER | 权限范围，取值和说明： HAS PERMSSION：有权限的 _ OWNER：我所有的 MY FOCUS：我关注的 _ UNKNOWN：不限 |
| DbType | String | 否 | MySQL | 数据库类型，取值为： MySQL SQLServer PostgreSQL Oracle DRDS OceanBase Mongo Redis |
| ReturnGuid | Boolean | 否 | false | 是否返回表GUID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |

数据管理

| RequestId | String | 1489257F-1B5D- 4B5B-89EF- 923C12CEEBD1 | 请求ID。 |
|---|---|---|---|
| SearchTableLi st | Array of SearchTable |  | 搜索表详情列表。 |
| SearchTable |  |  |  |
| DBSearchNam e | String | test | 表所对应的库搜索名。 |
| DatabaseId | String | 1 | 所属的库ID。 |
| DbName | String | test | 数据库名。 |
| DbType | String | mysql | 数据库类型，取值为： MySQL SQLServer PostgreSQL Oracle DRDS OceanBase Mongo Redis |
| Description | String | test | 描述信息。 |
| Encoding | String | utf8 | 表编码。 |
| Engine | String | innodb | 表引擎。 |
| EnvType | String | test | 环境类型。 |
| Logic | Boolean | false | 是否为逻辑表，取值： true：是 false：否 |
| OwnerIdList | List | 1 | 表Owner ID列表。 |
| OwnerNameLi st | List | user | 表Owner昵称列表。 |
| TableGuid | String | IDB L 9032.db- _ _ test.yuyang test _ | 表GUID。 |

数据管理

| TableId | String | 1 | 表ID。 |
|---|---|---|---|
| TableName | String | test table _ | 表名。 |
| TableSchemaN ame | String | test@xxx.xxx.xxx.x xx:3306 | 表所对应库名。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 1 | 满足搜索条件的记录总数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <TableGuid>IDB_L_9032.db-test.yuyang_test</TableGuid>
        <Logic>false</Logic>
        <TableSchemaName>xxx_0000</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DBSearchName>xxx_0000@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306【xxx线下库】</D
BSearchName>
        <DatabaseId>117567</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <TableName>test_aaaa</TableName>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <EnvType>dev</EnvType>
        <Engine>InnoDB</Engine>
        <TableId>18396767</TableId>
<TotalCount>1</TotalCount> <RequestId>1489257F-1B5D-4B5B-89EF-923C12CEEBD1</RequestId> <Success>true</Success>
```

数据管理 `JSON` 格式

```json
{
      {
        "TableGuid" : "IDB_L_9032.db-test.yuyang_test",
        "Logic": false,
        "TableSchemaName": "xxx_0000",
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx",
            "xxx"
```

]

```json
        },
        "DBSearchName": "xxx_0000@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306【xxx线下库】
```

`",`

```json
        "DatabaseId": 117567,
        "Encoding": "utf8mb4",
        "TableName": "test_aaaa",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            88656,
            104442
```

]

```json
        },
        "EnvType": "dev",
        "Engine": "InnoDB",
        "TableId": 18396767
      }
```

]

```json
  },
  "TotalCount": 1,
  "RequestId": "1489257F-1B5D-4B5B-89EF-923C12CEEBD1",
  "Success": true
}
```

#### ListDatabases

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDatabases | 系统规定参数。取值：ListDatabases。 |

数据管理

| InstanceId | String | 是 | 1 | 实例ID，取值来自ListInstances接口返回的实例信息中的实例ID，注意不是RDS 的实例ID。 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 页码。 |
| Tid | Long | 否 | -1 | 租户ID。 |
| PageSize | Integer | 否 | 10 | 每页记录数。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DatabaseList | Array of Database |  | 数据库详情列表。 |
| Database |  |  |  |
| CatalogName | String | 1 | 数据库目录名称。 说明若数据库类型为PG系列，此处表示PG数据库名。 |
| DatabaseId | String | 1 | 数据库ID。 |
| DbType | String | mysql | 数据库类型。 |
| DbaId | String | 1 | 数据库所属DBA ID。 |
| DbaName | String | dba user _ | 数据库所属DBA名称。 |
| Encoding | String | utf-8 | 数据库编码。 |
| EnvType | String | dev | 数据库所属环境类型。 |
| Host | String | xxx.xxx.xxx.xxx | 实例连接地址。 |
| InstanceId | String | 1 | 数据库所属实例ID。 |

数据管理

| OwnerIdList | List | 1 | 数据库Owner ID列表。 |
|---|---|---|---|
| OwnerNameLi st | List | owner name _ | 数据库Owner名称列表。 |
| Port | Integer | 3306 | 实例连接端口。 |
| SchemaName | String | test | 数据库名。 |
| SearchName | String | test@xxx.xxx.xxx.x xx:3306 | 数据库搜索名。 |
| Sid | String | test | 库所属实例SID。 |
| State | String | NORMAL | 库状态，取值和说明如下： NORMAL： 正常 DISABLE：禁用 OFFLINE：下线 NOT EXIST：不存在 _ |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 5541CDA6-F674- 435C-81BD- 40C2FB926CE3 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 1 | 实例下面的数据库个数。 |

**示例**

请求示例

```
&InstanceId=1 &PageNumber=1 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<TotalCount>1</TotalCount> <RequestId>5541CDA6-F674-435C-81BD-40C2FB926CE3</RequestId> <Success>true</Success> <DatabaseList>
    <Database>
        <Encoding>utf8</Encoding>
        <Host>pc-xxx.rwlb.rds.aliyuncs.com</Host>
        <InstanceId>24710</InstanceId>
        <DbType>polardb</DbType>
        <EnvType>product</EnvType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
        </OwnerIdList>
        <DbaId>104442</DbaId>
        <OwnerNameList>
            <OwnerNames>dmstest</OwnerNames>
        </OwnerNameList>
        <Port>3306</Port>
        <DatabaseId>116366</DatabaseId>
        <State>NORMAL</State>
        <SearchName>xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306【xxx_test】</SearchName>
        <DbaName>xxx[子账号]</DbaName>
        <SchemaName>xxx_test</SchemaName>
    </Database>
</DatabaseList>
```

`JSON` 格式数据管理

```json
{
  "TotalCount": 1,
  "RequestId": "5541CDA6-F674-435C-81BD-40C2FB926CE3",
  "Success": true,
  "DatabaseList": {
    "Database": [
      {
        "Encoding": "utf8",
        "Host": "pc-xxx.rwlb.rds.aliyuncs.com",
        "InstanceId": 24710,
        "DbType": "polardb",
        "EnvType": "product",
        "OwnerIdList": {
          "OwnerIds": [
            88653
```

]

```json
        },
        "DbaId": 104442,
        "OwnerNameList": {
          "OwnerNames": [
            "dmstest"
```

]

```json
        },
        "Port": 3306,
        "DatabaseId": 116366,
        "State": "NORMAL",
        "SearchName": "xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306【xxx_test】",
        "DbaName": "xxx[子账号]",
        "SchemaName": "xxx_test"
      }
```

]

```
  }
}
```

#### ListLogicDatabases

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListLogicDataba ses | 系统规定参数。取值：ListLogicDatabases。 |
| PageNumber | Integer | 否 | 1 | 页码。 |
| Tid | Long | 否 | -1 | 租户ID。 |

数据管理

| PageSize | Integer | 否 | 50 | 每页记录数。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| LogicDatabase List | Array of LogicDatabase |  | 逻辑库详情列表。 |
| LogicDatabase |  |  |  |
| DatabaseId | String | 1 | 逻辑库ID。 |
| DbType | String | mysql | 逻辑库数据库类型。 |
| EnvType | String | test | 逻辑库所属环境。 |
| Logic | Boolean | true | 是否逻辑库，固定为true。 |
| OwnerIdList | List | 1 | 逻辑库Owner ID列表。 |
| OwnerNameLi st | List | owner name _ | 逻辑库Owner名称列表。 |
| SchemaName | String | logic db _ | 逻辑库名。 |
| SearchName | String | loigc db _ | 逻辑库搜索名。 |
| RequestId | String | BAD154C0-DA38- 48FA-97AB- E72912EEAA24 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 13 | 逻辑库总数。 |

**示例**

数据管理请求示例

```
http(s)://[Endpoint]/?Action=ListLogicDatabases &PageNumber=1 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>13</TotalCount> <RequestId>BAD154C0-DA38-48FA-97AB-E72912EEAA24</RequestId> <LogicDatabaseList>
    <LogicDatabase>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>257</DatabaseId>
```

`<SearchName>test_db`（我是逻辑库）`</SearchName>`

```xml
        <DbType>mysql</DbType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
        </OwnerIdList>
        <EnvType>dev</EnvType>
        <SchemaName>test_db</SchemaName>
    </LogicDatabase>
    <LogicDatabase>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>258</DatabaseId>
```

`<SearchName>xxx_test`（我是逻辑库）`</SearchName>`

```xml
        <DbType>mysql</DbType>
        <OwnerIdList>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>101252</OwnerIds>
        </OwnerIdList>
        <EnvType>product</EnvType>
        <SchemaName>idb_test</SchemaName>
    </LogicDatabase>
</LogicDatabaseList> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "TotalCount": 13,
  "RequestId": "BAD154C0-DA38-48FA-97AB-E72912EEAA24",
  "LogicDatabaseList": {
    "LogicDatabase": [
      {
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx"
```

]

```json
        },
        "DatabaseId": 257,
```

`"SearchName": "test_db`（我是逻辑库）`",`

```json
        "DbType": "mysql",
        "OwnerIdList": {
          "OwnerIds": [
            88653
```

]

```json
        },
        "EnvType": "dev",
        "SchemaName": "test_db"
      },
      {
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx",
            "xxx"
```

]

```json
        },
        "DatabaseId": 258,
```

`"SearchName": "xxx_test`（我是逻辑库）`",`

```json
        "DbType": "mysql",
        "OwnerIdList": {
          "OwnerIds": [
            88656,
            88653,
            101252
```

]

```json
        },
        "EnvType": "product",
        "SchemaName": "idb_test"
      }
```

]

```json
  },
  "Success": true
}
```

#### ListTables

数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTables | 系统规定参数。取值：ListTables。 |
| DatabaseId | String | 是 | 1 | 数据库ID。 |
| PageNumber | Integer | 是 | 1 | 页码。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| PageSize | Integer | 否 | 10 | 每页记录数。 |
| SearchName | String | 否 | test | 表关键字，前缀匹配。 |
| ReturnGuid | Boolean | 否 | true | 是否返回表的GUID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | B16FB618-5E96- 4FFD-BB0D- 490C890A4030 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TableList | Array of Table |  | 表详情列表。 |
| Table |  |  |  |
| DatabaseId | String | 1 | 数据库ID。 |
| Description | String | test | 表描述信息。 |

数据管理

| Encoding | String | utf8 | 表编码。 |
|---|---|---|---|
| Engine | String | innodb | 表引擎。 |
| NumRows | Long | 1 | 表行数（统计值，非精确行数）。 |
| OwnerIdList | List | 1 | 表Owner ID列表。 |
| OwnerNameLi st | List | owner name _ | 表Owner昵称列表。 |
| StoreCapacity | Long | 1024 | 表占用存储空间容量（统计值，非精确容量）。 |
| TableGuid | String | IDB 308302.yuyan _ g test.test ch _ _ | 表GUID。 |
| TableId | String | 1 | 表ID。 |
| TableName | String | test | 表名。 |
| TableSchemaN ame | String | test db _ | 表所对应库名。 |
| TableType | String | NORMAL | 表类型，默认为NORMAL。 |
| TotalCount | Long | 12 | 满足条件的表总个数。 |

**示例**

请求示例

```
&DatabaseId=1 &PageNumber=1 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<TableList>
    <Table>
        <TableSchemaName>yuyang_test</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>116367</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <NumRows>3</NumRows>
        <StoreCapacity>1</StoreCapacity>
        <TableName>base_user</TableName>
        <TableGuid>IDB_18396363.yuyang_test.base_user</TableGuid>
        <TableType>NORMAL</TableType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Engine>InnoDB</Engine>
        <TableId>18396363</TableId>
    </Table>
    <Table>
        <TableSchemaName>yuyang_test</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>116367</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <NumRows>2</NumRows>
        <StoreCapacity>1</StoreCapacity>
        <TableName>biz_orders</TableName>
        <TableType>NORMAL</TableType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Engine>InnoDB</Engine>
        <TableId>18390459</TableId>
    </Table>
</TableList> <TotalCount>12</TotalCount> <RequestId>B16FB618-5E96-4FFD-BB0D-490C890A4030</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "TableList": {
    "Table": [
      {
        "TableSchemaName": "yuyang_test",
        "OwnerNameList": {
```

`"O` N " [ 数据管理

```json
          "OwnerNames": [
            "xxx",
            "xxx"
```

]

```json
        },
        "DatabaseId": 116367,
        "Encoding": "utf8mb4",
        "NumRows": 3,
        "StoreCapacity": 1,
        "TableName": "base_user",
        "TableGuid": "IDB_18396363.yuyang_test.base_user",
        "TableType": "NORMAL",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

]

```json
        },
        "Engine": "InnoDB",
        "TableId": 18396363
      },
      {
        "TableSchemaName": "yuyang_test",
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx"
```

]

```json
        },
        "DatabaseId": 116367,
        "Encoding": "utf8mb4",
        "NumRows": 2,
        "StoreCapacity": 1,
        "TableName": "biz_orders",
        "TableType": "NORMAL",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

]

```json
        },
        "Engine": "InnoDB",
        "TableId": 18390459
      }
```

]

```json
  },
  "TotalCount": 12,
  "RequestId": "B16FB618-5E96-4FFD-BB0D-490C890A4030",
  "Success": true
}
```

#### ListLogicTables

数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListLogicTables | 系统规定参数。取值：ListLogicTables。 |
| DatabaseId | String | 是 | 1 | 逻辑库ID。 |
| PageNumber | Integer | 是 | 1 | 页码。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| PageSize | Integer | 否 | 10 | 每页记录数。 |
| SearchName | String | 否 | test | 逻辑表搜索关键字，前缀匹配。 |
| ReturnGuid | Boolean | 否 | true | 是否返回表的GUID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| LogicTableList | Array of LogicTable |  | 逻辑表详情列表。 |
| LogicTable |  |  |  |
| DatabaseId | String | 1 | 逻辑库ID。 |
| Logic | Boolean | true | 是否为逻辑表，固定为true。 |
| OwnerIdList | List | 1 | 逻辑表Owner ID列表。 |
| OwnerNameLi st | List | owner name _ | 逻辑表Owner名称列表。 |

数据管理

| SchemaName | String | yuyang test _ | 逻辑表对应逻辑库名。 |
|---|---|---|---|
| TableCount | String | 4 | 分表个数。 |
| TableExpr | String | test[1-4] | 逻辑表表达式。 |
| TableGuid | String | IDB L 308302.yuy _ _ ang test.test ch _ _ | 逻辑表GUID。 |
| TableId | String | 1 | 逻辑表ID。 |
| TableName | String | test | 逻辑表表名。 |
| RequestId | String | F1E6484F-9DF1- 4406-9BDE- 0861C4629B69 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 1 | 满足条件记录数。 |

**示例**

请求示例

```
&DatabaseId=1 &PageNumber=1 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<TotalCount>1</TotalCount> <RequestId>F1E6484F-9DF1-4406-9BDE-0861C4629B69</RequestId> <LogicTableList>
    <LogicTable>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <TableExpr>t[1-4]</TableExpr>
        <DatabaseId>267</DatabaseId>
        <SchemaName>yuyang_test</SchemaName>
        <TableName>t</TableName>
        <TableGuid>IDB_L_3057.yuyang_test.t</TableGuid>
        <TableCount>4</TableCount>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <TableId>3057</TableId>
    </LogicTable>
</LogicTableList> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "TotalCount": 1,
  "RequestId": "F1E6484F-9DF1-4406-9BDE-0861C4629B69",
  "LogicTableList": {
    "LogicTable": [
      {
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx"
```

]

```json
        },
        "TableExpr": "t[1-4]",
        "DatabaseId": 267,
        "SchemaName": "yuyang_test",
        "TableName": "t",
        "TableGuid": "IDB_L_3057.yuyang_test.t",
        "TableCount": 4,
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

]

```json
        },
        "TableId": 3057
      }
```

]

```json
  },
  "Success": true
}
```

#### ListColumns

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListColumns | 系统规定参数。取值：ListColumns。 |
| Logic | Boolean | 否 | false | 是否为逻辑表。 |
| TableId | String | 是 | 1 | 表ID。 |
| Tid | Long | 是 | 0 | 租户ID。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ColumnList | Array of Column |  | 列信息详情。 |
| Column |  |  |  |
| AutoIncrement | Boolean | false | 当前字段是否自增。取值： true：自增。 false：不自增。 |
| ColumnId | String | 1 | 字段ID。 |
| ColumnName | String | name | 字段名。 |
| ColumnType | String | varchar | 字段类型。 |
| DataLength | Long | 32 | 字段长度。 |
| DataPrecision | Integer | 0 | 字段精度。 |
| DataScale | Integer | 0 | 字段精度。 |
| DefaultValue | String | def value _ | 字段默认值。 |
| Description | String | test | 字段描述。 |
| FunctionType | String | default | 字段遮掩算法类型，取值如下： null：无遮掩 DEFAULT：全遮掩 FIX POS：固定位置遮掩 _ FIX CHAR：固定字符替换 _ |
| Nullable | Boolean | true | 字段是否可空。 |

数据管理

| SecurityLevel | String | INNER | 安全级别，取值如下： INNER：内部（非敏感） SENSITIVE：敏感 CONFIDENTIAL：机密 |
|---|---|---|---|
| Sensitive | Boolean | false | 是否敏感字段。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 0AD9AC55-5873- 474A-9F33- 4285806A3619 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Logic=false &TableId=1 &Tid=0
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<ColumnList>
    <Column>
        <ColumnId>314036829</ColumnId>
        <DataScale>0</DataScale>
        <Sensitive>false</Sensitive>
        <Description>主键ID</Description>
        <DataPrecision>20</DataPrecision>
        <ColumnType>bigint(20) unsigned</ColumnType>
        <ColumnName>id</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>true</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036830</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>创建时间</Description>
        <DefaultValue>CURRENT_TIMESTAMP</DefaultValue>
        <ColumnType>datetime</ColumnType>
        <ColumnName>gmt_create</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036831</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>修改时间</Description>
        <DefaultValue>CURRENT_TIMESTAMP</DefaultValue>
        <ColumnType>datetime</ColumnType>
        <ColumnName>gmt_modified</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036832</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>base_user</Description>
        <ColumnType>varchar(64)</ColumnType>
        <DataLength>64</DataLength>
        <ColumnName>user_name</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>true</Nullable>
    </Column>
</ColumnList> <RequestId>0AD9AC55-5873-474A-9F33-4285806A3619</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "ColumnList": {
    "Column": [
      {
        "ColumnId": 314036829,
        "DataScale": 0,
        "Sensitive": false,
        "Description": "主键ID",
        "DataPrecision": 20,
        "ColumnType": "bigint(20) unsigned",
        "ColumnName": "id",
        "SecurityLevel": "INNER",
        "AutoIncrement": true,
        "Nullable": false
      },
      {
        "ColumnId": 314036830,
        "Sensitive": false,
```

`"Description": "`创建时间`",`

```json
        "DefaultValue": "CURRENT_TIMESTAMP",
        "ColumnType": "datetime",
        "ColumnName": "gmt_create",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": false
      },
      {
        "ColumnId": 314036831,
        "Sensitive": false,
```

`"Description": "`修改时间`",`

```json
        "DefaultValue": "CURRENT_TIMESTAMP",
        "ColumnType": "datetime",
        "ColumnName": "gmt_modified",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": false
      },
      {
        "ColumnId": 314036832,
        "Sensitive": false,
        "Description": "base_user",
        "ColumnType": "varchar(64)",
        "DataLength": 64,
        "ColumnName": "user_name",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": true
      }
```

]

```json
  },
  "RequestId": "0AD9AC55-5873-474A-9F33-4285806A3619",
  "Success": true
}
```

数据管理

#### ListIndexes

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListIndexes | 系统规定参数。取值：ListIndexes。 |
| Logic | Boolean | 否 | false | 是否为逻辑表。 |
| TableId | String | 否 | 1 | 表ID。 |
| Tid | Long | 是 | 0 | 租户ID。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| IndexList | Array of Index |  | 索引详情列表。 |
| Index |  |  |  |
| IndexCommen t | String | test | 索引描述。 |
| IndexId | String | 1 | 索引ID。 |
| IndexName | String | idx test _ | 索引名称。 |
| IndexType | String | Primary | 索引类型，取值如下： Primary Unique Normal FullText Spatial |

数据管理

| TableId | String | 1 | 表ID。 |
|---|---|---|---|
| RequestId | String | 1F4DE2F1-5B47- 462A-A973- E02EB7AF386B | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Logic=false &TableId=1 &Tid=0
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>1F4DE2F1-5B47-462A-A973-E02EB7AF386B</RequestId> <IndexList>
    <Index>
        <IndexComment/>
        <IndexType>Primary</IndexType>
        <IndexName>PRIMARY</IndexName>
        <IndexId>49331416</IndexId>
        <TableId>18396274</TableId>
    </Index>
</IndexList> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "1F4DE2F1-5B47-462A-A973-E02EB7AF386B",
  "IndexList": {
    "Index": [
      {
        "IndexComment": "",
        "IndexType": "Primary",
        "IndexName": "PRIMARY",
        "IndexId": 49331416,
        "TableId": 18396274
      }
```

]

```json
  },
  "Success": true
}
```

数据管理

#### GetDatabase

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDatabase | 系统规定参数。取值：GetDatabase。 |
| Host | String | 是 | xxx.xxx.xxx.xxx | 实例连接地址。 |
| Port | Integer | 是 | 3306 | 实例连接端口。 |
| SchemaName | String | 是 | test db _ | 数据库名。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Sid | String | 否 | test sid _ | 实例SID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Database | Struct |  | 库详情信息。 |
| CatalogName | String | def | 数据库目录名。 说明若数据库类型为PG系列，此处表示PG数据库名。 |
| DatabaseId | String | 1 | 数据库ID。 |
| DbType | String | mysql | 数据库类型。 |
| DbaId | String | 1 | DBA ID。 |
| DbaName | String | dba name _ | DBA名称。 |
| Encoding | String | utf8mb4 | 数据库编码。 |

数据管理

| EnvType | String | test | 库环境类型。 |
|---|---|---|---|
| Host | String | xxx.xxx.xxx.xxx | 实例连接地址。 |
| InstanceId | String | 1 | 实例ID。 |
| OwnerIdList | List | 1 | 数据库Owner ID列表。 |
| OwnerNameLi st | List | test | 数据库Owner名称列表。 |
| Port | Integer | 3306 | 实例连接端口。 |
| SchemaName | String | test db _ | Schema名称。 |
| SearchName | String | test db@xxx.xxx.xx _ x.xxx:3306 | 逻辑库搜索名。 |
| Sid | String | test sid _ | 实例SID。 |
| State | String | NORMAL | 库状态，取值参考ListDatabases。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 3CDB8601-AD74- 4A47-8114- 08E08CD6319D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Host=xxx.xxx.xxx.xxx &Port=3306 &SchemaName=test_db &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<Database>
    <Encoding>utf8mb4</Encoding>
    <Host>pc-xxx.rwlb.rds.aliyuncs.com</Host>
    <InstanceId>24710</InstanceId>
    <DbType>polardb</DbType>
    <OwnerIdList>
        <OwnerIds>88653</OwnerIds>
        <OwnerIds>104442</OwnerIds>
    </OwnerIdList>
    <EnvType>product</EnvType>
    <DbaId>104442</DbaId>
    <OwnerNameList>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx[子账号]</OwnerNames>
    </OwnerNameList>
    <Port>3306</Port>
    <DatabaseId>116367</DatabaseId>
    <State>NORMAL</State>
    <SearchName>xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306【xxx_test】</SearchName>
    <DbaName>xxx[子账号]</DbaName>
    <SchemaName>xxx_test</SchemaName>
</Database> <RequestId>3CDB8601-AD74-4A47-8114-08E08CD6319D</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "Database": {
    "Encoding": "utf8mb4",
    "Host": "pc-xxx.rwlb.rds.aliyuncs.com",
    "InstanceId": 24710,
    "DbType": "polardb",
    "OwnerIdList": {
      "OwnerIds": [
        88653,
        104442
```

]

```json
    },
    "EnvType": "product",
    "DbaId": 104442,
    "OwnerNameList": {
      "OwnerNames": [
        "xxx",
```

`"xxx[`子账号`]"` ]

```json
    },
    "Port": 3306,
    "DatabaseId": 116367,
    "State": "NORMAL",
    "SearchName": "xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306【xxx_test】",
    "DbaName": "xxx[子账号]",
    "SchemaName": "xxx_test"
  },
  "RequestId": "3CDB8601-AD74-4A47-8114-08E08CD6319D",
  "Success": true
}
```

#### GetLogicDatabase

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetLogicDataba se | 系统规定参数。取值：GetLogicDatabase。 |
| DbId | String | 是 | 1 | 逻辑库DB ID。 |
| Tid | Long | 是 | 0 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

数据管理

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| LogicDatabase | Struct |  | 逻辑库详情信息。 |
| DatabaseId | String | 1 | 逻辑库ID。 |
| DbType | String | mysql | 数据库类型。 |
| EnvType | String | dev | 库环境类型。 |
| Logic | Boolean | true | 是否逻辑库，固定为true。 |
| OwnerIdList | List | 1 | 库Owner ID列表。 |
| OwnerNameLi st | List | owner name _ | 库Owner名称列表。 |
| SchemaName | String | test logic db _ _ | 逻辑库库名。 |
| SearchName | String | test logic db[xxx] _ _ | 逻辑库搜索名。 |
| RequestId | String | 90260530-565C- 42B9-A6E8- 893481FE6AB6 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&DbId=1 &Tid=0
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<LogicDatabase>
    <Logic>true</Logic>
    <OwnerNameList>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx</OwnerNames>
    </OwnerNameList>
    <DatabaseId>265</DatabaseId>
    <SearchName>test_logic_db(xxx)</SearchName>
    <DbType>mysql</DbType>
    <OwnerIdList>
        <OwnerIds>88653</OwnerIds>
        <OwnerIds>97787</OwnerIds>
        <OwnerIds>88654</OwnerIds>
    </OwnerIdList>
    <EnvType>dev</EnvType>
    <SchemaName>test_logic_db</SchemaName>
</LogicDatabase> <RequestId>90260530-565C-42B9-A6E8-893481FE6AB6</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "LogicDatabase": {
    "Logic": true,
    "OwnerNameList": {
      "OwnerNames": [
        "xxx",
        "xxx",
        "xxx"
```

]

```json
    },
    "DatabaseId": 265,
    "SearchName": "test_logic_db(xxx)",
    "DbType": "mysql",
    "OwnerIdList": {
      "OwnerIds": [
        88653,
        97787,
        88654
```

]

```json
    },
    "EnvType": "dev",
    "SchemaName": "test_logic_db"
  },
  "RequestId": "90260530-565C-42B9-A6E8-893481FE6AB6",
  "Success": true
}
```

#### GetMetaTableDetailInfo

数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableDe tailInfo | 系统规定参数。取值：GetMetaTableDetailInfo。 |
| TableGuid | String | 是 | IDB L 9032.db- _ _ test.yuyang test _ | 表在DMS中的唯一识别码 GUID（Globally Unique Identifier）。 说明逻辑库：可调用ListLogicTables接口获取，需要将ReturnGuid参数设置为true。 物理库：可调用ListTables接口获取，需要将ReturnGuid参数设置为true。 |
| Tid | Long | 否 | 123 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DetailInfo | Struct |  | 表详情。 |
| ColumnList | Array of Column |  | 字段列表。 |
| AutoIncrement | Boolean | true | 当前字段是否自增。取值： true：自增。 false：不自增。 |
| ColumnId | String | 191234849 | 字段ID。 |
| ColumnName | String | id | 字段名。 |
| ColumnType | String | bigint(20) unsigned | 字段的数据类型。例如：Bigint、Int、Varchar。 |
| DataLength | Integer | 0 | 字段长度。 |

数据管理

| DataPrecision | Integer | 0 | 字段精度。 |
|---|---|---|---|
| DataScale | Integer | 0 | 该字段小数后的位数。 |
| Description | String | test | 字段描述。 |
| Nullable | Boolean | false | 是否可空。取值： true：允许为空。 false：不允许为空。 |
| Position | String | 1 | 字段在表中的顺序。 |
| IndexList | Array of Index |  | 索引列表。 |
| IndexColumns | List | id,name | 索引字段。 |
| IndexId | String | 123 | 索引ID。 |
| IndexName | String | PRIMARY | 索引名。 |
| IndexType | String | Primary | 索引类型。例如：Primary、Unique、Normal。 |
| Unique | Boolean | false | 是否为唯一索引。取值： true：是唯一索引。 false：不是唯一索引。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | E881CB2F-DE42- 42E5-90EB- 8B3173DCB9B9 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例数据管理

```
http(s)://[Endpoint]/?Action=GetMetaTableDetailInfo &TableGuid=IDB_L_9032.db-test.yuyang_test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E881CB2F-DE42-42E5-90EB-8B3173DCB9B9</RequestId> <DetailInfo>
    <ColumnList>
        <ColumnId>191234849</ColumnId>
        <ColumnName>id</ColumnName>
        <Description>test</Description>
        <ColumnType>bigint(20) unsigned</ColumnType>
        <Position>1</Position>
        <AutoIncrement>true</AutoIncrement>
        <DataScale>0</DataScale>
        <DataPrecision>20</DataPrecision>
        <Nullable>false</Nullable>
    </ColumnList>
    <ColumnList>
        <ColumnId>191234850</ColumnId>
        <ColumnName>gmt_create</ColumnName>
        <Description>test</Description>
        <ColumnType>datetime</ColumnType>
        <Position>2</Position>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </ColumnList>
    <ColumnList>
        <ColumnId>191234851</ColumnId>
        <ColumnName>gmt_modified</ColumnName>
        <Description>test</Description>
        <ColumnType>datetime</ColumnType>
        <Position>3</Position>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </ColumnList>
    <IndexList>
        <IndexName>PRIMARY</IndexName>
        <IndexId>33008763</IndexId>
        <IndexColumns>id</IndexColumns>
        <Unique>false</Unique>
        <IndexType>Primary</IndexType>
    </IndexList>
</DetailInfo> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "RequestId": "E881CB2F-DE42-42E5-90EB-8B3173DCB9B9",
  "DetailInfo": {
    "ColumnList": [
      {
        "ColumnId": 191234849,
        "ColumnName": "id",
        "Description": "test",
        "ColumnType": "bigint(20) unsigned",
        "Position": 1,
        "AutoIncrement": true,
        "DataScale": 0,
        "DataPrecision": 20,
        "Nullable": false
      },
      {
        "ColumnId": 191234850,
        "ColumnName": "gmt_create",
        "Description": "test",
        "ColumnType": "datetime",
        "Position": 2,
        "AutoIncrement": false,
        "Nullable": false
      },
      {
        "ColumnId": 191234851,
        "ColumnName": "gmt_modified",
        "Description": "test",
        "ColumnType": "datetime",
        "Position": 3,
        "AutoIncrement": false,
        "Nullable": false
      }
```

`],`

```json
    "IndexList": [
      {
        "IndexName": "PRIMARY",
        "IndexId": 33008763,
        "IndexColumns": [
          "id"
```

`],`

```json
        "Unique": false,
        "IndexType": "Primary"
      }
```

]

```json
  },
  "Success": true
}
```

#### GetTableDBTopology

数据管理目前仅支持逻辑库实例调用该API。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetTableDBTopo logy | 系统规定参数。取值：GetTableDBTopology。 |
| TableGuid | String | 是 | IDB L 9032.db- _ _ test.yuyang test _ | 表在DMS中的唯一识别码 GUID（Globally Unique Identifier）。 说明逻辑库：可调用ListLogicTables接口获取，需要将ReturnGuid参数设置为true。 物理库：可条用ListTables接口获取，需要将ReturnGuid参数设置为true。 |
| Tid | Long | 否 | 123 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域，用于调用该接口。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBTopology | Struct |  | 数据库拓扑信息。 |
| DataSourceLis t | Array of DataSource |  | 数据源列表。 |
| DatabaseList | Array of Database |  | 物理分库列表。 |
| DbId | String | 489347 | 数据库ID。 |
| DbName | String | db-test | 物理库库名。 |
| DbType | String | mysql | 数据库类型。 |

数据管理

| EnvType | String | pre | 环境类型，取值和说明如下： product：生产环境 dev：开发环境 pre：预发环境 test：测试环境 sit：SIT环境 uat：UAT环境 pet：压测环境 stag：STAG环境 |
|---|---|---|---|
| TableList | Array of Table |  | 物理分表列表。 |
| TableId | String | 151977812 | 表ID。 |
| TableName | String | yuyang test 0000 _ _ | 物理表表名。 |
| TableType | String | NORMAL | 表类型，保留字段。 |
| DbType | String | mysql | 数据库类型。 |
| Host | String | xxx.mysql.polardb. rds.aliyuncs.com | 数据源的连接地址。 |
| Port | Integer | 3306 | 数据源连接端口。 |
| Sid | String | def | 数据源SID。 |
| TableGuid | String | IDB L 9032.db- _ _ test.yuyang test _ | 表在DMS中的唯一识别码GUID（Globally Unique Identifier）。 |
| TableName | String | yuyang test _ | 表名。 说明如果查询逻辑表，将返回逻辑表表名。 如果查询物理表，将返回物理表表名。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |

数据管理

| RequestId | String | 853F7FD4-D922- 4EFB-931C- D253EF159E06 | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetTableDBTopology &TableGuid=IDB_L_9032.db-test.yuyang_test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<RequestId>55B7CF50-4610-4707-B2B2-5EF2BE000367</RequestId> <DBTopology>
    <TableName>yuyang_test</TableName>
    <TableGuid>IDB_L_9032.db-test.yuyang_test</TableGuid>
    <DataSourceList>
        <DatabaseList>
            <DbId>489347</DbId>
            <DbName>db-test</DbName>
            <TableList>
                <TableId>151977811</TableId>
                <TableName>yuyang_test_0000</TableName>
            </TableList>
            <TableList>
                <TableId>151977812</TableId>
                <TableName>yuyang_test_0001</TableName>
            </TableList>
            <TableList>
                <TableId>151977813</TableId>
                <TableName>yuyang_test_0002</TableName>
            </TableList>
            <TableList>
                <TableId>151977814</TableId>
                <TableName>yuyang_test_0003</TableName>
            </TableList>
            <TableList>
                <TableId>151977815</TableId>
                <TableName>yuyang_test_0004</TableName>
            </TableList>
            <EnvType>dev</EnvType>
            <DbType>polardb</DbType>
        </DatabaseList>
        <Port>3306</Port>
        <Host>xxx.mysql.polardb.rds.aliyuncs.com</Host>
        <DbType>polardb</DbType>
    </DataSourceList>
</DBTopology> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "RequestId": "55B7CF50-4610-4707-B2B2-5EF2BE000367",
  "DBTopology": {
    "TableName": "yuyang_test",
    "TableGuid": "IDB_L_9032.db-test.yuyang_test",
    "DataSourceList": [
      {
        "DatabaseList": [
          {
            "DbId": 489347,
            "DbName": "db-test",
            "TableList": [
              {
                "TableId": 151977811,
                "TableName": "yuyang_test_0000"
              },
              {
                "TableId": 151977812,
                "TableName": "yuyang_test_0001"
              },
              {
                "TableId": 151977813,
                "TableName": "yuyang_test_0002"
              },
              {
                "TableId": 151977814,
                "TableName": "yuyang_test_0003"
              },
              {
                "TableId": 151977815,
                "TableName": "yuyang_test_0004"
              }
```

`],`

```json
            "EnvType": "dev",
            "DbType": "polardb"
          }
```

`],`

```json
        "Port": 3306,
        "Host": "xxx.mysql.polardb.rds.aliyuncs.com",
        "DbType": "polardb"
      }
```

]

```json
  },
  "Success": true
}
```

#### GetMetaTableColumn

**请求参数**

数据管理

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableCo lumn | 系统规定参数。取值：GetMetaTableColumn。 |
| TableGuid | String | 是 | IDB L 11345.yu _ _ yang test.base _ _ user | 表在DMS中的唯一识别码 GUID（Globally Unique Identifier）。 说明逻辑库：可调用ListLogicTables接口获取，需要将ReturnGuid参数设置为true。 物理库：可调用ListTables接口获取，需要将ReturnGuid参数设置为true。 |
| Tid | Long | 否 | 123 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ColumnList | Array of Column |  | 字段列表。 |
| AutoIncrement | Boolean | true | 字段是否自增。取值： true：自增。 false：不自增。 |
| ColumnId | String | 191234849 | 字段ID。 |
| ColumnName | String | id | 字段名。 |
| ColumnType | String | bigint(20) unsigned | 字段的数据类型。例如：Bigint 、Int、Varchar。 |
| DataLength | Integer | 0 | 字段长度。 |
| DataPrecision | Integer | 0 | 字段精度。 |
| DataScale | Integer | 0 | 字段小数后的位数。 |

数据管理

| Description | String | test | 字段描述。 |
|---|---|---|---|
| Nullable | Boolean | false | 字段是否允许为空。取值： true：允许为空。 false：不允许为空。 |
| Position | Integer | 1 | 字段在表中顺序。 |
| PrimaryKey | String | true | 字段是否为主键，取值： true：主键。 false：非主键。 |
| SecurityLevel | String | INNER | 字段的安全级别，取值如下： INNER：内部（非敏感） SENSITIVE：敏感 CONFIDENTIAL：机密 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 2B581A5E-D4FE- 4F77-BADE- DD944D7BEBE2 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableColumn &TableGuid=IDB_L_11345.yuyang_test.base_user
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
      <RequestId>2B581A5E-D4FE-4F77-BADE-DD944D7BEBE2</RequestId>
      <ErrorCode>UnknownError</ErrorCode>
      <ColumnList>
            <ColumnId>191234849</ColumnId>
            <ColumnName>id</ColumnName>
            <Description>test</Description>
            <ColumnType>bigint(20) unsigned</ColumnType>
            <Position>1</Position>
            <AutoIncrement>true</AutoIncrement>
            <SecurityLevel>INNER</SecurityLevel>
            <DataScale>0</DataScale>
            <DataLength>0</DataLength>
            <DataPrecision>0</DataPrecision>
            <PrimaryKey>true</PrimaryKey>
            <Nullable>false</Nullable>
      </ColumnList>
      <ErrorMessage>UnknownError</ErrorMessage>
      <Success>true</Success>
```

`JSON` 格式

```json
{
 "RequestId": "2B581A5E-D4FE-4F77-BADE-DD944D7BEBE2",
 "ErrorCode": "UnknownError",
 "ColumnList": [{
  "ColumnId": "191234849",
  "ColumnName": "id",
  "Description": "test",
  "ColumnType": "bigint(20) unsigned",
  "Position": "1",
  "AutoIncrement": "true",
  "SecurityLevel": "INNER",
  "DataScale": "0",
  "DataLength": "0",
  "DataPrecision": "0",
  "PrimaryKey": "true",
  "Nullable": "false"
 }],
 "ErrorMessage": "UnknownError",
 "Success": "true"
}
```

#### SyncDatabaseMeta

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据管理

| Action | String | 是 | SyncDatabaseM eta | 系统规定参数。取值：SyncDatabaseMeta。 |
|---|---|---|---|---|
| DbId | String | 是 | 123 | 数据库ID。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| Logic | Boolean | 否 | false | 是否为逻辑库。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&DbId=123 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
}
```

数据管理

#### SyncInstanceMeta

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SyncInstanceMe ta | 系统规定参数，取值：SyncInstanceMeta。 |
| InstanceId | String | 是 | 1234 | 实例ID。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| IgnoreTable | Boolean | 否 | true | 是否忽略表字典元数据同步。取值： true false |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误消息。 |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
}
```

#### GetPhysicalDatabase

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetPhysicalData base | 系统规定参数。取值：GetPhysicalDatabase。 |
| DbId | Long | 是 | 43153 | 物理库ID，您可以调用SearchDatabase接口获取该值。 |
| Tid | Long | 否 | 1 | 租户ID，您可以调用GetUserActiveTenant接口获取该参数。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 7FAD400F-7A5C- 4193-8F9A- 39D86C4F0231 | 请求ID。 |
| Database | object |  | 物理库信息。 |
| DatabaseId | String | 43125312 | 物理库ID。 |
| Host | String | rm- xxxab3r272.mysql. rds.aliyuncs.com | 数据库连接地址。 |

数据管理

| CatalogName | String | def | 数据库目录名。 说明 PG系列的数据库将显示数据库名。 |
|---|---|---|---|
| DbaName | String | dmstest | 目标库的DBA昵称。 |
| State | String | NORMAL | 库状态，取值说明： NORMAL：正常 DISABLE：禁用 OFFLINE：下线 NOT EXIST：不存在 _ |
| DbaId | String | 43253 | 目标库的DBA的用户ID。 |
| SchemaName | String | dmstest | 数据库名。 说明 PG系列的数据库将显示模式名。 |
| InstanceId | String | 43215325 | 目标库的实例ID。 |
| Port | Integer | 3306 | 数据库的连接端口。 |
| EnvType | String | product | 数据库的环境类型。 |
| Sid | String | def | 数据库SID。 说明仅Oracle数据库显示。 |
| OwnerIdList | Array of String | 43215325 | 库Owner User ID。 |
| Encoding | String | utf8mb4 | 数据库编码。 |
| DbType | String | mysql | 数据库类型。 |
| OwnerNameLi st | Array of String | dmstest | 库Owner昵称。 |
| SearchName | String | dmstest@rm- xxxab3r272.mysql. rds.aliyuncs.com:3 306 | 库搜索名称。 |

数据管理

| ErrorCode | String | UnknownError | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | UnknownError | 错误信息。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetPhysicalDatabase &DbId=43153 &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>4EE2B004-9131-44B7-B6EE-6151B6329F68</RequestId>
    <Database>
        <SearchName>film@rm-uf64e.mysql.rds.aliyuncs.com:3306</SearchName>
        <InstanceId>1400000</InstanceId>
        <Port>3306</Port>
        <Encoding>utf8</Encoding>
        <Host>rm-uf64e.mysql.rds.aliyuncs.com</Host>
        <DatabaseId>7000000</DatabaseId>
        <DbType>mysql</DbType>
        <EnvType>dev</EnvType>
        <DbaName>enlun00</DbaName>
        <DbaId>260000</DbaId>
        <State>NORMAL</State>
        <CatalogName>def</CatalogName>
        <OwnerNameList>
            <OwnerNames>enlun</OwnerNames>
        </OwnerNameList>
        <SchemaName>film</SchemaName>
        <OwnerIdList>
            <OwnerIds>26000</OwnerIds>
        </OwnerIdList>
    </Database>
    <Success>true</Success>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "4EE2B004-9131-44B7-B6EE-6151B6329F68",
  "Database" : {
    "SearchName" : "film@rm-uf64e.mysql.rds.aliyuncs.com:3306",
    "InstanceId" : 1400000,
    "Port" : 3306,
    "Encoding" : "utf8",
    "Host" : "rm-uf64e.mysql.rds.aliyuncs.com",
    "DatabaseId" : 7000000,
    "DbType" : "mysql",
    "EnvType" : "dev",
    "DbaName" : "enlun00",
    "DbaId" : 260000,
    "State" : "NORMAL",
    "CatalogName" : "def",
    "OwnerNameList" : {
      "OwnerNames" : [ "enlun" ]
    },
    "SchemaName" : "film",
    "OwnerIdList" : {
      "OwnerIds" : [ 26000 ]
    }
  },
  "Success" : true
}
```

#### GetTableTopology

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| TableGuid | String | 是 | IDB L 308302.y _ _ uyang test.test _ _ ch | 表在DMS中的唯一识别码 GUID（Globally Unique Identifier）。 说明逻辑库：可调用ListLogicTables接口获取，需要将ReturnGuid参数设置为true。 物理库：可调用ListTables接口获取，需要将ReturnGuid参数设置为 true。 |
| Tid | Long | 否 | 1 | 租户ID。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | F5ED6A40-F344- 4C7D-A8F0- 5685CA584CA7 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| TableTopology | object |  | 拓扑信息。 |
| TableGuid | String | IDB L 308302.yuy _ _ ang test.test ch _ _ | 表在DMS中的唯一识别码GUID（Globally Unique Identifier）。 |
| TableName | String | test ch _ | 表名。 |
| TableTopology InfoList | Array of TableTopology Info |  | 表拓扑信息列表。 |
| TableNameList | String | test ch 0000,test _ _ _ ch 0001,test ch 0 _ _ _ 002,test ch 0003,t _ _ est ch 0004,test c _ _ _ h 0005 _ | 表名列表。 说明以逗号隔开。 |
| TableNameEx pr | String | test ch [0000- _ _ 0005] | 逻辑表的表名表达式。 说明物理表则不会显示该参数。 |
| TableCount | Long | 6 | 表数量。 |
| DbId | Long | 43215 | 物理库ID。 |
| DbSearchNam e | String | yuyang test@local _ host:3306【yuyang test dev】 _ _ | 库搜索名。 |

数据管理

| InstanceId | Long | 4325325 | 物理库对应的实例ID。 |
|---|---|---|---|
| RegionId | String | cn-hangzhou | 实例RegionId。 |
| InstanceResou rceId | String | rm-xxx | 实例资源ID，取值如下： RDS：阿里云数据库实例ID ECS OWN：阿里云ECS实例ID _ PUBLIC OWN：空 _ VPC ID：VPC ID _ GATEWAY：数据库网关实例ID |
| InstanceSourc e | String | RDS | 实例来源，取值如下： RDS：阿里云数据库实例 ECS OWN：阿里云ECS自建库实例 _ PUBLIC OWN：公网自建库实例 _ VPC ID：VPC专线IDC数据库实例 _ GATEWAY：数据库网关实例 |
| DbName | String | yuyang test _ | 库名。 |
| DbType | String | mysql | 数据库类型。 |
| Logic | Boolean | true | 是否为逻辑表，取值： true：是 false：否 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetTableTopology &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>7A7F0E34-8E21-4CF7-93C8-27212B122145</RequestId>
    <TableTopology>
        <TableName>big_table</TableName>
        <TableGuid>IDB_279000000.film.big_table</TableGuid>
        <Logic>false</Logic>
        <TableTopologyInfoList>
            <DbSearchName>film@rm-uf00000000240000l.mysql.rds.aliyuncs.com:3306【nissi g
o】</DbSearchName>
            <InstanceSource>RDS</InstanceSource>
            <InstanceResourceId>rm-uf00000000240000l</InstanceResourceId>
            <InstanceId>1000000</InstanceId>
            <TableNameList>big_table</TableNameList>
            <TableCount>1</TableCount>
            <DbId>4000000</DbId>
            <DbName>film</DbName>
            <RegionId>cn-shanghai</RegionId>
            <DbType>mysql</DbType>
        </TableTopologyInfoList>
    </TableTopology>
    <Success>true</Success>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "7A7F0E34-8E21-4CF7-93C8-27212B122145",
  "TableTopology" : {
    "TableName" : "big_table",
    "TableGuid" : "IDB_279000000.film.big_table",
    "Logic" : false,
    "TableTopologyInfoList" : [ {
      "DbSearchName" : "film@rm-uf00000000240000l.mysql.rds.aliyuncs.com:3306【nissi go
```

】`",`

```json
      "InstanceSource" : "RDS",
      "InstanceResourceId" : "rm-uf00000000240000l",
      "InstanceId" : 1000000,
      "TableNameList" : "big_table",
      "TableCount" : 1,
      "DbId" : 4000000,
      "DbName" : "film",
      "RegionId" : "cn-shanghai",
      "DbType" : "mysql"
    } ]
  },
  "Success" : true
}
```

### 工单操作

#### 通用

##### ApproveOrder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ApproveOrder | 系统规定参数。取值：ApproveOrder。 |
| ApprovalType | String | 是 | agree | 审批动作，取值和说明如下： AGREE：同意 CANCEL：取消 REJECT：拒绝 |

数据管理

| Tid | Long | 是 | -1 | 租户ID。 说明 DMS控制台右上角头像处悬停鼠标即可展示租户ID信息。 |
|---|---|---|---|---|
| WorkflowInstanc eId | Long | 是 | 1234 | 审批流ID，该值可从GetOrderBaseInfo接口获取，针对需要审批的工单，此值是大于0的整数。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| Comment | String | 否 | test | 备注信息。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&ApprovalType=agree &Tid=-1 &WorkflowInstanceId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
  "Success": true
}
```

##### CloseOrder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CloseOrder | 系统规定参数。取值：CloseOrder。 |
| CloseReason | String | 是 | close reason | 关闭原因。 |
| OrderId | Long | 是 | 1343 | 工单号。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 操作是否成功。 |

**示例**

请求示例

```
&CloseReason=close reason &OrderId=1343 &Tid=-1
```

`&<`公共请求参数> 数据管理正常返回示例 `XML` 格式

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
  "Success": true
}
```

##### GetApprovalDetail

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetApprovalDet ail | 系统规定参数。取值：GetApprovalDetail。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| WorkflowInstanc eId | Long | 是 | 12345 | 审批流ID。您可以通过GetOrderBaseInfo接口获取该参数，仅针对需要审批的工单，此值是大于0 的整数。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ApprovalDetail | Struct |  | 审批详情信息。 |
| AuditId | Long | 277 | 审批流ID。 |
| CurrentHandle rs | Array of CurrentHandle r |  | 当前审批处理人信息。 |
| CurrentHandle r |  |  |  |

数据管理

| Id | Long | 1 | 用户ID。 |
|---|---|---|---|
| NickName | String | nickName | 用户名称。 |
| Description | String | test | 审批描述信息。 |
| OrderId | Long | 1234 | 工单ID。 |
| OrderType | String | DATA EXPORT _ | 工单类型。 |
| ReasonList | List | ["reason1"] | 审批原因。 |
| Title | String | 数据导出工单-1234 | 审批标题。 |
| WorkflowInsCo de | String | APPROVED | 审批状态码。 |
| WorkflowNode s | Array of WorkflowNode |  | 审批流程节点信息。 |
| WorkflowNode |  |  |  |
| AuditUserIdLis t | List | 104442 | 审批人ID列表。 |
| NodeName | String | DBA | 审批节点名称。 |
| OperateComm ent | String | 理由：同意 | 审批操作备注。 |
| OperateTime | String | 2019-10-15 13:47:54 | 审批操作时间。 |
| OperatorId | Long | 13434 | 审批操作人ID。 |
| WorkflowInsCo de | String | APPROVED | 审批状态码。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |

数据管理

| Success | Boolean | true | 请求是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
&Tid=-1 &WorkflowInstanceId=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ApprovalDetail>
    <Description>xxx</Description>
    <WorkflowInsCode>APPROVED</WorkflowInsCode>
    <CurrentHandlers>
    </CurrentHandlers>
    <OrderId>737047</OrderId>
    <OrderType>DATA_EXPORT</OrderType>
    <ReasonList>
        <Reasons>xxx</Reasons>
    </ReasonList>
    <AuditId>277</AuditId>
```

`<Title>`数据导出工单`-737047</Title>`

```xml
    <WorkflowNodes>
        <WorkflowNode>
            <OperatorId>104442</OperatorId>
            <WorkflowInsCode>APPROVED</WorkflowInsCode>
            <OperateComment>理由：同意</OperateComment>
            <AuditUserIdList>
                <AuditUserIds>104442</AuditUserIds>
            </AuditUserIdList>
            <OperateTime>2019-10-15 13:47:54</OperateTime>
            <NodeName>DBA</NodeName>
        </WorkflowNode>
    </WorkflowNodes>
</ApprovalDetail> <RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "ApprovalDetail": {
    "Description": "xxx",
    "WorkflowInsCode": "APPROVED",
    "CurrentHandlers": {
      "CurrentHandler": []
    },
    "OrderId": 737047,
    "OrderType": "DATA_EXPORT",
    "ReasonList": {
      "Reasons": [
        "xxx"
```

]

```json
    },
    "AuditId": 277,
```

`"Title": "`数据导出工单`-737047",`

```json
    "WorkflowNodes": {
      "WorkflowNode": [
        {
          "OperatorId": 104442,
          "WorkflowInsCode": "APPROVED",
```

`"OperateComment": "`理由：同意`",`

```json
          "AuditUserIdList": {
            "AuditUserIds": [
              104442
```

]

```json
          },
          "OperateTime": "2019-10-15 13:47:54",
          "NodeName": "DBA"
        }
```

]

```json
    }
  },
  "RequestId": "FE8EE2F1-4880-46BC-A704-5CF63EAF9A04",
  "Success": true
}
```

##### GetOrderBaseInfo

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetOrderBaseInf o | 系统规定参数。取值：GetOrderBaseInfo。 |
| OrderId | Long | 是 | 12345 | 工单ID。 |

数据管理

| Tid | Long | 是 | -1 | 租户ID。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| OrderBaseInfo | Struct |  | 工单基本信息。 |
| Comment | String | test | 备注信息。 |
| Committer | String | xxx | 提交者。 |
| CommitterId | Long | 1 | 提交者ID，注意不是提交者的阿里云UID。 |
| CreateTime | String | 2019-10-10 00:00:00 | 工单创建时间。 |
| LastModifyTim e | String | 2019-10-10 00:00:00 | 工单最后修改时间。 |
| OrderId | Long | 12345 | 工单号。 |
| PluginType | String | DC COMMON _ | 工单类型，取值和说明参考CreateOrder接口相对应入参说明。 |
| RelatedUserLis t | List | 1,2,3 | 工单相关人ID列表。 |
| RelatedUserNi ckList | List | a,b,c | 工单相关人名称列表。 |

数据管理

| StatusCode | String | success | 工单状态码，取值和说明如下： new：新建 toaudit：审批中 approved：审批通过 reject：审批拒绝 processing：执行中 success：执行成功 closed：已关闭 |
|---|---|---|---|
| StatusDesc | String | success | 状态描述信息。 |
| WorkflowInsta nceId | Long | 1 | 审批流ID。 |
| WorkflowStatu sDesc | String | approved | 审批描述信息。 |
| RequestId | String | 7133DF67-5B25- 460F-8285- C4CC93472C2F | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&OrderId=12345 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<OrderBaseInfo>
    <Comment>test</Comment>
    <CreateTime>2019-10-10 00:00:00</CreateTime>
    <LastModifyTime>2019-10-10 00:00:00</LastModifyTime>
    <OrderId>12345</OrderId>
    <CommitterId>1</CommitterId>
    <PluginType>DC_COMMON</PluginType>
    <StatusCode>success</StatusCode>
    <RelatedUserNickList>
        <UserNicks>a,b,c</UserNicks>
    </RelatedUserNickList>
    <StatusDesc>success</StatusDesc>
    <WorkflowStatusDesc>approved</WorkflowStatusDesc>
    <WorkflowInstanceId>1</WorkflowInstanceId>
    <Committer>xxx</Committer>
    <RelatedUserList>
        <UserIds>1,2,3</UserIds>
    </RelatedUserList>
</OrderBaseInfo> <RequestId>7133DF67-5B25-460F-8285-C4CC93472C2F</RequestId> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{"OrderBaseInfo":{"Comment":"test","CreateTime":"2019-10-10 00:00:00","LastModifyTime":"2019-10-10 00:00:00","OrderId":"12345","CommitterId":"1","PluginType":"DC_COMMON","StatusCode":"succ s","RelatedUserNickList": {"UserNicks":"a,b,c"},"StatusDesc":"success","WorkflowStatusDesc":"approved","WorkflowIns nceId":"1","Committer":"xxx","RelatedUserList": {"UserIds":"1,2,3"}},"RequestId":"7133DF67-5B25-460F-8285- C4CC93472C2F","ErrorCode":"UnknownError","ErrorMessage":"UnknownError","Success":"true"}
```

##### ListOrders

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListOrders | 系统规定参数。取值：ListOrders。 |
| Tid | Long | 否 | -1 | 租户ID。 |

数据管理

| PluginType | String | 否 | PERM APPLY _ | 工单类型，取值和说明如下： PERM APPLY：权限申请 _ OWNER APPLY： owner申请 _ DATA CORRECT：数据变更 _ NDDL：结构设计 DATA TRACK：数据追踪 _ TABLE SYNC：库表同步 _ DATA EXPORT：数据导出 _ SENSITIVITY：敏感列等级调整 |
|---|---|---|---|---|
| OrderResultType | String | 否 | AS ADMIN _ | 搜索类型，取值和说明如下： AS ADMIN：工单大盘 _ AS COMMITTER：我发起的工单 _ AS HANDLER：待我处理的工单 _ AS OWNER：我已处理的工单 _ AS Related：与我相关 _ |
| SearchDateType | String | 否 | CREATE TIME _ | 时间搜索条件，取值： CREATE TIME： 创建时间 _ MODIFY TIME： 修改时间 _ |
| StartTime | String | 否 | 2019-10-10 00:00:00 | 开始时间。 |
| EndTime | String | 否 | 2019-10-10 00:00:00 | 结束时间。 |
| SearchContent | String | 否 | test | 搜索内容。 |
| OrderStatus | String | 否 | ALL | 工单状态，取值和说明如下： ALL：不限 FINISHED：已结束 RUNNING：进行中 |
| PageSize | Integer | 否 | 10 | 每页记录数。 |
| PageNumber | Integer | 否 | 1 | 第几页。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据管理

| ErrorCode | String | UnknownError | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | UnknownError | 错误信息。 |
| Orders | Array of Order |  | 工单列表信息。 |
| Order |  |  |  |
| Comment | String | test | 工单备注信息。 |
| Committer | String | test | 工单提交者。 |
| CommitterId | Long | 1 | 工单提交者ID。 |
| CreateTime | String | 2019-10-10 00:00:00 | 工单创建时间。 |
| LastModifyTim e | String | 2019-10-10 00:00:00 | 工单最后修改时间。 |
| OrderId | Long | 1432 | 工单ID。 |
| PluginType | String | DC COMMON _ | 工单类型。 |
| StatusCode | String | success | 工单状态码。 |
| StatusDesc | String | success | 工单状态描述。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 100 | 记录总数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例数据管理 `XML` 格式

```xml
<TotalCount>5</TotalCount> <RequestId>7AC17A86-9E6F-484B-AE8D-F9416986A108</RequestId> <Orders>
    <Order>
        <StatusCode>success</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[子账号]</Committer>
```

`<StatusDesc>`数据变更成功`</StatusDesc>`

```xml
        <LastModifyTime>2019-11-19 13:53:05</LastModifyTime>
        <CreateTime>2019-11-19 13:52:36</CreateTime>
        <OrderId>737160</OrderId>
```

`<Comment>`测试数据变更`</Comment>`

```xml
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>new</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[子账号]</Committer>
```

`<StatusDesc>`待提交审批`</StatusDesc>`

```xml
        <LastModifyTime>2019-10-29 20:51:37</LastModifyTime>
        <CreateTime>2019-10-29 20:51:36</CreateTime>
        <OrderId>737116</OrderId>
```

`<Comment>`测试创建数据变更工单`</Comment>`

```xml
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>closed</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[子账号]</Committer>
```

`<StatusDesc>`工单已关闭：还是不支持库级别操作`</StatusDesc>`

```xml
        <LastModifyTime>2019-10-20 22:09:38</LastModifyTime>
        <CreateTime>2019-10-20 22:08:19</CreateTime>
        <OrderId>737089</OrderId>
```

`<Comment>`测试建库`</Comment>`

```xml
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>new</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[子账号]</Committer>
```

`<StatusDesc>`预检查失败`</StatusDesc>`

```xml
        <LastModifyTime>2019-09-30 16:58:35</LastModifyTime>
        <CreateTime>2019-09-30 16:58:34</CreateTime>
        <OrderId>737016</OrderId>
        <Comment>测试</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>success</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[子账号]</Committer>
```

`<StatusDesc>`数据变更成功`</StatusDesc>`

```
tMdifTi 20190817140754/L tMdifTi
```

数据管理

```xml
        <LastModifyTime>2019-08-17 14:07:54</LastModifyTime>
        <CreateTime>2019-08-17 14:07:42</CreateTime>
        <OrderId>736774</OrderId>
```

`<Comment>`测试普通数据变更`</Comment>`

```xml
        <CommitterId>104442</CommitterId>
    </Order>
</Orders> <Success>true</Success>
```

`JSON` 格式

```json
{
  "TotalCount": 5,
  "RequestId": "7AC17A86-9E6F-484B-AE8D-F9416986A108",
  "Orders": {
    "Order": [
      {
        "StatusCode": "success",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[子账号]",
```

`"StatusDesc": "`数据变更成功`",`

```json
        "LastModifyTime": "2019-11-19 13:53:05",
        "CreateTime": "2019-11-19 13:52:36",
        "OrderId": 737160,
```

`"Comment": "`测试数据变更`",`

```json
        "CommitterId": 104442
      },
      {
        "StatusCode": "new",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[子账号]",
```

`"StatusDesc": "`待提交审批`",`

```json
        "LastModifyTime": "2019-10-29 20:51:37",
        "CreateTime": "2019-10-29 20:51:36",
        "OrderId": 737116,
```

`"Comment": "`测试创建数据变更工单`",`

```json
        "CommitterId": 104442
      },
      {
        "StatusCode": "closed",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[子账号]",
```

`"StatusDesc": "`工单已关闭：还是不支持库级别操作`",`

```json
        "LastModifyTime": "2019-10-20 22:09:38",
        "CreateTime": "2019-10-20 22:08:19",
        "OrderId": 737089,
```

`"Comment": "`测试建库`",`

```json
        "CommitterId": 104442
      },
      {
        "StatusCode": "new",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[子账号]",
```

`"StatusDesc": "`预检查失败`",` 数据管理

```json
        "LastModifyTime": "2019-09-30 16:58:35",
        "CreateTime": "2019-09-30 16:58:34",
        "OrderId": 737016,
        "Comment": "测试",
        "CommitterId": 104442
      },
      {
        "StatusCode": "success",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[子账号]",
```

`"StatusDesc": "`数据变更成功`",`

```json
        "LastModifyTime": "2019-08-17 14:07:54",
        "CreateTime": "2019-08-17 14:07:42",
        "OrderId": 736774,
```

`"Comment": "`测试普通数据变更`",`

```json
        "CommitterId": 104442
      }
```

]

```json
  },
  "Success": true
}
```

##### SubmitOrderApproval

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SubmitOrderApp roval | 系统规定参数。取值：SubmitOrderApproval。 |
| OrderId | Long | 是 | 12345 | 工单ID。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |

数据管理

| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SubmitOrderApproval &OrderId=12345 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7AC17A86-9E6F-484B-AE8D-F9416986A108</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "7AC17A86-9E6F-484B-AE8D-F9416986A108",
  "Success": true
}
```

##### CreateOrder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateOrder | 系统规定参数。取值：CreateOrder。 |
| Comment | String | 是 | test | 创建工单描述信息。 |

| 开发指南·API参考 |  |  |  | 数据管理 |
|---|---|---|---|---|
| PluginParam | Json | 是 | {} | 创建工单参数，格式为JSON形式的字符串，每个工单类型的参数设置不一致。详情请参考PluginParam参数补充说明JSON # 普通数据变更 "pluginParam" : { "classify" : "测试", // 原因分类 "estimateAffectRows" : 1, // 用户预估影响行数 "execSQL" : "update base op log set id=1 where id=1;", _ _ // 执行SQL "dbItemList" : [ { // 执行的 db列表 "dbId" : 179694, "logic" : false } ], "rbSQL" : "update base op log _ _ set id=1 where id=1;", // 用户填写的回滚SQL "rbAttachmentName" : null, // 回滚SQL附件 "sqlType" : "TEXT", // SQL类型，取值为TEXT, ATTACHMENT "rbSQLType" : "TEXT", // 回滚SQL类型，取值同上 "attachmentName" : // SQL附件 } # 无锁数据变更 "pluginParam" : { "classify" : "测试", "execSQL" : "update base op log set _ _ op type=op type where 1=1;", // 执 _ _ 行SQL "dbItemList" : [ { "dbId" : 179694, // 变更库id "logic" : false } ] } # 历史数据清理 "pluginParam" : { "duration" : 10, // 指定时长（小时）， 当不指定时长时，值为0； "specifyDuration" : true, // 是否指定时长，true：是，false：否，默认是false "classify" : "测试", "cronFormat" : "0 1 21 * * ?", // 定时执行的表达式 "execSql" : null, "dbItemList" : [ { "dbId" : 179694, // 变更库id "logic" : false } ], "cronClearItemList" : [ { "filterSQL" : null, // 过滤条件 "columnName" : "gmt create", // 时间 _ 字段 "remainDays" : 60, // 保留时长 "tableName" : "base app" // 表名 } ] _ } # 结构设计 “pluginParam”: { "title": "test", // 标题 "description": "test", // 描述 "dbId": 118989, // 基准库 "logic": false, // 是否逻辑库 "relatedIds": [], // 变更相关人id } # 数据导出 "pluginParam" : { "classify": "原因分类", // 原因分类 "dbId": 179719, // 导出库id "exeSQL": "select 1", // 导出SQL "logic": false, // 是否逻辑库 "ignoreAffectRows": false, // 是否忽略校验影响行数 "affectRows": 1, // 用户预估影响行数 "ignoreAffectRowsReason": "" // 忽略影响行数校验原因 }。 |

数据管理

| PluginType | String | 是 | DATA EXPORT _ | 工单类型。取值如下： DC COMMON：普通数据变更 _ DC CHUNK：无锁数据变更 _ DC CRON CLEAR：历史数据清理 _ _ NDDL：结构设计 DATA EXPORT：数据导出 _ PERM APPLY：权限申请 _ OWNER APPLY：Owner申请 _ |
|---|---|---|---|---|
| RelatedUserList | String | 否 | 1,2,3 | 工单相关人ID列表。多个相关人ID使用半角逗号（,）进行分隔。 |
| Tid | Long | 否 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**PluginParam参数补充说明**

```
JSON
```

# 普通数据变更

```json
"pluginParam" : {
```

`"classify" : "`测试`", //` 原因分类 `"estimateAffectRows" : 1, //` 用户预估影响行数

```json
    "execSQL" : "update base_op_log set id=1 where id=1;", // 执行SQL
```

`"dbItemList" : [ { //` 执行的`db`列表

```json
      "dbId" : 179694,
      "logic" : false
    } ],
    "rbSQL" : "update base_op_log set id=1 where id=1;", // 用户填写的回滚SQL
    "rbAttachmentName" : null, // 回滚SQL附件
    "sqlType" : "TEXT", // SQL类型，取值为TEXT, ATTACHMENT
```

`"rbSQLType" : "TEXT", //` 回滚`SQL`类型，取值同上数据管理

```json
    "attachmentName" : // SQL附件
  }
```

# 无锁数据变更

```json
"pluginParam" : {
    "classify" : "测试",
    "execSQL" : "update base_op_log set op_type=op_type where 1=1;", // 执行SQL
    "dbItemList" : [ {
      "dbId" : 179694, // 变更库id
      "logic" : false
    } ]
  }
```

# 历史数据清理

```json
"pluginParam" : {
```

`"duration" : 10, //` 指定时长（小时），当不指定时长时，值为0； `"specifyDuration" : true, //` 是否指定时长，`true`：是，`false`：否，默认是`false`

```json
    "classify" : "测试",
```

"cronFormat" : "0 1 21 * * ?", // 定时执行的表达式

```json
    "execSql" : null,
    "dbItemList" : [ {
      "dbId" : 179694, // 变更库id
      "logic" : false
    } ],
    "cronClearItemList" : [ {
```

`"filterSQL" : null, //` 过滤条件

```json
      "columnName" : "gmt_create", // 时间字段
```

`"remainDays" : 60, //` 保留时长

```json
      "tableName" : "base_app" // 表名
    } ]
  }
```

# 结构设计

```json
“pluginParam”: {
    "title": "test", // 标题
    "description": "test", // 描述
    "dbId": 118989, // 基准库
```

`"logic": false, //` 是否逻辑库 `"relatedIds": [], //` 变更相关人`id`

```
  }
```

# 数据导出

```json
"pluginParam" : {
```

`"classify": "`原因分类`", //` 原因分类

```json
  "dbId": 179719, // 导出库id
  "exeSQL": "select 1", // 导出SQL
```

`"logic": false, //` 是否逻辑库 `"ignoreAffectRows": false, //` 是否忽略校验影响行数 `"affectRows": 1, //` 用户预估影响行数 `"ignoreAffectRowsReason": "" //` 忽略影响行数校验原因数据管理

```
 }
```

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CreateOrderRe sult | List | 123 | 创建工单成功后返回的工单号。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Comment=test &PluginParam={} &PluginType=DATA_EXPORT &RelatedUserList=1,2,3
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId>
    <OrderIds>123</OrderIds>
<Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
    "OrderIds": [123]
  },
  "Success": true
}
```

数据管理

#### 数据变更

##### ExecuteDataCorrect

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ExecuteDataCor rect | 系统规定参数。取值：ExecuteDataCorrect。 |
| OrderId | Long | 是 | 123 | 工单ID。 |
| Tid | String | 否 | -1 | 租户ID。 |
| ActionDetail | Json | 否 | { "startTime" : null, "endTime" : null, "transaction" : false, "backupData" : true } | 执行数据变更的参数设置： json "actionDetail" : { "startTime" : null, // 设置定时执行的执行时间，若您选择立即执行不需要设置该参数。 "endTime" : null, // 设置定时执行的结束时间，若您选择立即执行不需要设置该参数。 "transaction" : false, // 选择是否以事务方式运行。 "backupData" : true // 选择是否备份数据。 } |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |

数据管理

| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ExecuteDataCorrect &OrderId=123
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7133DF67-5B25-460F-8285-C4CC93472C2F</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "7133DF67-5B25-460F-8285-C4CC93472C2F",
  "Success": true
}
```

##### GetDataCorrectBackupFiles

调用GetDataCorrectBackupFiles接口获取数据变更备份文件附件下载地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataCorrect BackupFiles | 系统规定参数。取值：GetDataCorrectBackupFiles。 |
| OrderId | Long | 是 | 12345 | 工单ID。 |
| Tid | Long | 否 | -1 | 租户ID。 |
| ActionDetail | Json | 否 | {} | 操作参数，无需传递。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

数据管理

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DataCorrectBa ckupFiles | List | xxx | 备份文件附件下载地址信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDataCorrectBackupFiles &OrderId=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DataCorrectBackupFiles>
    <FileUrl>https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.zip?
Expires=1574382979&amp;OSSAccessKeyId=wSa97B52GzF****&amp;Signature=ykWSysajKcQjXjG0X4ApO lIXQ%3D</FileUrl> </DataCorrectBackupFiles> <RequestId>4AFF4109-FEFB-44E8-96A3-923B1FA8C46E</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "DataCorrectBackupFiles": {
    "FileUrl": [
      "https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.zip?
Expires=1574382979&OSSAccessKeyId=wSa97B52GzF****&Signature=ykWSysajKcQjXjG0X4ApOQvlIXQ%3
```

]

```json
  },
  "RequestId": "4AFF4109-FEFB-44E8-96A3-923B1FA8C46E",
  "Success": true
}
```

##### GetDataCorrectOrderDetail

调用GetDataCorrectOrderDetail接口获取数据变更工单详情信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataCorrect OrderDetail | 系统规定参数。取值：GetDataCorrectOrderDetail。 |
| OrderId | Long | 是 | 12345 | 工单ID。 |
| Tid | Long | 否 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DataCorrectOr derDetail | Struct |  | 数据变更工单详情信息。 |
| DatabaseList | Array of Database |  | 变更数据库信息。 |
| Database |  |  |  |
| DbId | Integer | 123456 | 数据库ID。 |
| DbType | String | mysql | 数据库类型。 |
| EnvType | String | product | 环境类型。 |

数据管理

| Logic | Boolean | false | 是否为逻辑库。 |
|---|---|---|---|
| SearchName | String | xxx@xxx:3306 | 逻辑库的搜索名。 |
| OrderDetail | Struct |  | 工单详情信息。 |
| ActualAffectRo ws | Long | 100 | 系统校验的影响行数。 |
| AttachmentNa me | String | xxx | SQL附件。 |
| Classify | String | test | 变更原因分类。 |
| EstimateAffect Rows | Long | 100 | 用户预估影响行数。 |
| ExeSQL | String | update t1 set name = 'xxx' where id <= 100 | 执行的SQL。 |
| IgnoreAffectRo ws | Boolean | false | 是否忽略预校验。 |
| IgnoreAffectRo wsReason | String | test | 忽略预校验原因。 |
| RbAttachment Name | String | test | 回滚SQL附件。 |
| RbSQL | String | empty | 用户填写的回滚SQL。 |
| RbSQLType | String | text | 回滚SQL类型，取值和说明如下： TEXT：文本 ATTACHMENT：附件 |
| SqlType | String | text | SQL类型，取值和说明如下： TEXT：文本 ATTACHMENT：附件 |
| PreCheckDetai l | Array of TaskCheckDO |  | 预校验详情信息。 |
| TaskCheckDO |  |  |  |

数据管理

| CheckStatus | String | SUCCESS | 预校验状态，取值和说明如下： WAITING：等待检查 RUNNING：检查中 SUCCESS：通过 FAIL：不通过 |
|---|---|---|---|
| CheckStep | String | PERMISSION CHEC _ K | 检查步骤，取值和说明如下： SQL PARSE：解析 _ SQL TYPE CHECK：类型检查 _ _ PERMISSION CHECK：权限检查 _ ROW CHECK：行数检查 _ |
| UserTip | String | tip messsage | 校验步骤提示信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDataCorrectOrderDetail &OrderId=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<RequestId>ACE263E5-CF5F-44DD-A7B1-42C5E78E9650</RequestId> <DataCorrectOrderDetail>
    <PreCheckDetail>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>SQL_PARSE</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>SQL_TYPE_CHECK</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>PERMISSION_CHECK</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
```

`<UserTip>`系统统计值，实际影响行数仍然以`SQL`执行为准!</UserTip>

```xml
            <CheckStep>ROW_CHECK</CheckStep>
        </TaskCheckDO>
    </PreCheckDetail>
    <OrderDetail>
        <ActualAffectRows>0</ActualAffectRows>
        <RbSQLType>TEXT</RbSQLType>
        <ExeSQL>update base_user set id = 1 where id = 1;</ExeSQL>
        <EstimateAffectRows>1</EstimateAffectRows>
        <SqlType>TEXT</SqlType>
        <Classify>test</Classify>
        <IgnoreAffectRowsReason/>
    </OrderDetail>
</DataCorrectOrderDetail> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "RequestId": "ACE263E5-CF5F-44DD-A7B1-42C5E78E9650",
  "DataCorrectOrderDetail": {
    "PreCheckDetail": {
      "TaskCheckDO": [
        {
          "CheckStatus": "SUCCESS",
          "CheckStep": "SQL_PARSE"
        },
        {
          "CheckStatus": "SUCCESS",
          "CheckStep": "SQL_TYPE_CHECK"
        },
        {
          "CheckStatus": "SUCCESS",
          "CheckStep": "PERMISSION_CHECK"
        },
        {
          "CheckStatus": "SUCCESS",
```

`"UserTip": "`系统统计值，实际影响行数仍然以`SQL`执行为准!",

```json
          "CheckStep": "ROW_CHECK"
        }
```

]

```json
    },
    "OrderDetail": {
      "ActualAffectRows": 0,
      "RbSQLType": "TEXT",
      "ExeSQL": "update base_user set id = 1 where id = 1;",
      "EstimateAffectRows": 1,
      "SqlType": "TEXT",
      "Classify": "test",
      "IgnoreAffectRowsReason": ""
    }
  },
  "Success": true
}
```

##### CreateFreeLockCorrectOrder

调用CreateFreeLockCorrectOrder接口，在DMS中创建无锁变更工单。 目前仅支持管控模式为安全协同的实例调用该API。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateFreeLock CorrectOrder | 系统规定参数。取值：CreateFreeLockCorrectOrder 。 |

数据管理

| Comment | String | 是 | test | 业务背景，以减少沟通成本。 |
|---|---|---|---|---|
| RelatedUserList | Array of Long | 否 | 51**** | 变更相关人的用户ID，设置的相关人员可查看工单，并协同工作，非相关人员则不能查看工单（管理员、DBA除外）。 |
| Param | Object | 是 |  | 工单参数。 |
| Classify | String | 否 | test | 数据变更原因。 |
| ExecSQL | String | 是 | delete from base user _ where 1 = 1; | 变更SQL语句。 |
| SqlType | String | 是 | TEXT | 变更SQL的提交方式，取值如下： TEXT：文本 ATTACHMENT：附件，暂不支持。 |
| AttachmentNam e | String | 否 | test.sql | 变更SQL附件Key，暂不支持该参数。 |
| RollbackSQL | String | 否 | empty | 回滚SQL语句。 |
| RollbackAttachm entName | String | 否 | test rollback.sql _ | 回滚SQL附件Key，暂不支持该参数。 |
| RollbackSqlType | String | 否 | TEXT | 回滚SQL的提交方式，取值： TEXT：文本 ATTACHMENT：附件，暂不支持。 |
| DbItemList | Array | 是 |  | 变更的数据库列表。 |
| DbId | Long | 是 | 1860**** | 数据库ID（DatabaseId），数据库分为物理库和逻辑库两种： 物理库ID：可通过调用接口ListDatabases或SearchDatabase 获取该参数的值。 逻辑库ID：可通过调用接口ListLogicDatabases或SearchData base获取该参数的值。 |
| Logic | Boolean | 是 | false | 是否为逻辑库，取值如下： true：逻辑库 false：物理库 |

数据管理

| ExecMode | String | 否 | COMMITOR | 工单执行方式，取值如下： COMMITOR : 审批通过后，提交者执行。 AUTO : 审批通过后，自动执行。 LAST AUDITOR : 审批通过后，最后 _ 一个审批人执行。 |
|---|---|---|---|---|
| AttachmentKey | String | 否 | order attachme _ nt.txt | 工单附件Key，补充当前工单信息。可通过调用GetUserUploadFileJob接口获取该参数的值。 |
| Tid | Long | 否 | 3*** | 租户ID，可通过调用接口GetUserActiveTenant或ListUserTen ants获取该参数的值。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| CreateOrderRe sult | Array of Long | 134**** | 工单号。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Comment=test &RelatedUserList=[51****] &Param={"Classify":"test","ExecSQL":"delete from base_user where 1 = 1;","SqlType":"TEXT","DbItemList": [{"DbId":1860****,"Logic":false}],"ExecMode":"COMMITOR"} &AttachmentKey=order_attachment.txt
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId>
    <Success>true</Success>
    <ErrorMessage>UnknownError</ErrorMessage>
    <ErrorCode>UnknownError</ErrorCode>
    <CreateOrderResult>1340000</CreateOrderResult>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
  "Success" : true,
}
```

##### CreateDataCorrectOrder

调用CreateDataCorrectOrder接口，在DMS中创建普通数据变更工单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDataCorr ectOrder | 系统规定参数。取值：CreateDataCorrectOrder。 |
| Comment | String | 是 | test | 业务背景，以减少沟通成本。 |
| RelatedUserList | Array of Long | 否 | 51**** | 变更相关人的用户ID，设置的相关人员可查看工单，并协同工作，非相关人员则不能查看工单（管理员、DBA除外）。 |
| Param | Object | 是 |  | 工单参数。 |
| Classify | String | 否 | test | 数据变更原因。 |
| EstimateAffectR ows | Long | 是 | 1 | 预估本次变更会影响的数据行数。 |

数据管理

| ExecSQL | String | 否 | update base user set id _ = 1 where id = 1; | 变更SQL语句。 说明如果SqlType为TEXT，该参数必填。 |
|---|---|---|---|---|
| SqlType | String | 是 | TEXT | 变更SQL的提交方式，取值如下： TEXT：文本 ATTACHMENT：附件 |
| AttachmentNam e | String | 否 | test.sql | 变更SQL附件Key（AttachmentKey）， 可通过调用GetUserUploadFileJob接口获取该参数的值。 说明如果SqlType为ATTACHMENT，该参数必填。 |
| RollbackSQL | String | 否 | update base user set id _ = 1 where id = 1; | 回滚SQL语句。 说明如果RollbackSqlType为TE XT，该参数必填。 |
| RollbackAttachm entName | String | 否 | test rollback.sql _ | 回滚SQL附件Key（AttachmentKey）， 可通过调用GetUserUploadFileJob接口获取该参数的值。 说明如果RollbackSqlType为ATTACH MENT，该参数必填。 |
| RollbackSqlType | String | 否 | TEXT | 回滚SQL的提交方式，取值如下： TEXT：文本 ATTACHMENT：附件 |
| DbItemList | Array | 是 |  | 变更的数据库列表。 |
| DbId | Long | 是 | 1860**** | 数据库ID（DatabaseId），数据库分为物理库和逻辑库两种： 物理库ID：可通过调用接口ListDatabases或SearchDatabase 获取该参数的值。 逻辑库ID：可通过调用接口ListLogicDatabases或SearchData base获取该参数的值。 |

数据管理

| Logic | Boolean | 是 | false | 是否为逻辑库，取值如下： true：逻辑库 false：物理库 |
|---|---|---|---|---|
| ExecMode | String | 否 | COMMITOR | 工单执行方式，取值如下： COMMITOR : 审批通过后，提交者执行。 AUTO : 审批通过后，自动执行。 LAST AUDITOR : 审批通过后，最后 _ 一个审批人执行。 |
| AttachmentKey | String | 否 | order attachme _ nt.txt | 工单附件Key，补充当前工单信息。可通过调用GetUserUploadFileJob接口获取该参数的值。 |
| Tid | Long | 否 | 3*** | 租户ID，可通过调用接口GetUserActiveTenant或ListUserTen ants获取该参数的值。 |
| RegionId | String | 否 | cn-hangzhou | DMS服务地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| CreateOrderRe sult | Array of Long | 142**** | 普通数据变更工单号。 |

**示例**

请求示例数据管理

```
http(s)://dms-enterprise.aliyuncs.com/?Action=CreateDataCorrectOrder &Comment=test &Param={"Classify":"test","EstimateAffectRows":1,"ExecSQL":"update base_user set id = 1 where id = 1;","SqlType":"TEXT","DbItemList": [{"DbId":1860****,"Logic":false}],"ExecMode":"COMMITOR"}
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId>
    <Success>true</Success>
    <CreateOrderResult>142****</CreateOrderResult>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
  "Success" : true,
}
```

##### GetDataCronClearTaskDetailList

调用GetDataCronClearTaskDetailList接口，获取历史数据清理任务执行列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 432532 | 工单号，您可以调用CreateDataCronClearOrder接口获取该参数。 |
| PageNumber | Long | 否 | 1 | 第几页。 |
| PageSize | Long | 否 | 20 | 每页数据量。 |
| Tid | Long | 否 | 12345 | 租户ID。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | C1D39814-9808- 47F8-AFE0- AF167239AC9B | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| DataCronClear TaskDetailList | Array of DataCronClear TaskDetail |  | 历史数据清理任务执行列表。 |
| DBTaskGroupI d | Long | 432523 | SQL任务分组ID。 |
| jobStatus | String | SUCCESS | SQL详情状态，取值： INIT：初始化状态 PENDING：等待任务抓取 BE SCHEDULED：待调度 _ FAIL：执行失败 SUCCESS：执行成功 PAUSE：暂停 DELETE：删除 RUNNING：正在执行 |
| ActualAffectRo ws | Long | 1 | 影响行数。 |
| CreateTime | String | 2021-01-14 10:00:00 | 任务创建时间。 |
| TotalCount | Long | 1 | SQL任务列表总数。 |

**示例**

请求示例数据管理

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetDataCronClearTaskDetailList &PageNumber=1 &PageSize=20 &Tid=12345
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>C1D39814-9808-47F8-AFE0-AF167239AC9B</RequestId>
    <Success>true</Success>
    <DataCronClearTaskDetailList>
        <DBTaskGroupId>432523</DBTaskGroupId>
        <jobStatus>SUCCESS</jobStatus>
        <ActualAffectRows>1</ActualAffectRows>
        <CreateTime>2021-01-14 10:00:00</CreateTime>
    </DataCronClearTaskDetailList>
    <TotalCount>1</TotalCount>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "C1D39814-9808-47F8-AFE0-AF167239AC9B",
  "Success" : true,
  "DataCronClearTaskDetailList" : [ {
    "DBTaskGroupId" : 432523,
    "jobStatus" : "SUCCESS",
    "ActualAffectRows" : 1,
    "CreateTime" : "2021-01-14 10:00:00"
  } ],
  "TotalCount" : 1
}
```

##### GetDataCorrectTaskDetail

调用GetDataCorrectTaskDetail接口，获取普通数据变更、无锁变更、数据导入工单任务执行详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据管理

| OrderId | Long | 是 | 12435523 | 工单号，您可以调用CreateDataCorrectOrder、CreateD ataImportOrder、CreateFreeLockCorr ectOrder接口获取该参数。 |
|---|---|---|---|---|
| Tid | Long | 否 | 14325432 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B5FD0BC8-2D90- 4478-B8EC- A0E92E0B1773 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| DataCorrectTa skDetail | object |  | 变更任务执行详情。 |
| DBTaskGroupI d | Long | 1234235 | SQL任务分组ID。 |
| jobStatus | String | SUCCESS | SQL详情状态，取值： INIT：初始化状态 PENDING：等待任务抓取 BE SCHEDULED：待调度 _ FAIL：执行失败 SUCCESS：执行成功 PAUSE：暂停 DELETE：删除 RUNNING：正在执行 |
| ActualAffectRo ws | Long | 1 | 影响行数。 |
| CreateTime | String | 2021-03-05 15:08:55 | 任务创建时间。 |

**示例**

数据管理请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetDataCorrectTaskDetail &Tid=14325432
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml <RequestId>B5FD0BC8-2D90-4478-B8EC-A0E92E0B1773</RequestId> <Success>true</Success> <DataCorrectTaskDetail>
    <DBTaskGroupId>1234235</DBTaskGroupId>
    <jobStatus>SUCCESS</jobStatus>
    <ActualAffectRows>1</ActualAffectRows>
    <CreateTime>2021-03-05 15:08:55</CreateTime>
</DataCorrectTaskDetail>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "B5FD0BC8-2D90-4478-B8EC-A0E92E0B1773",
  "Success" : true,
  "DataCorrectTaskDetail" : {
    "DBTaskGroupId" : 1234235,
    "jobStatus" : "SUCCESS",
    "ActualAffectRows" : 1,
    "CreateTime" : "2021-03-05 15:08:55"
  }
}
```

##### GetDataCorrectSQLFile

调用GetDataCorrectSQLFile接口，获取数据变更工单的SQL脚本附件。 本接口适用于数据变更和数据导入。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 730000 | 工单号。 |
| Tid | Long | 否 | -1 | 租户ID。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 283C461F-11D8- 48AA-B695- DF092DA32AF3 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 请求异常信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| FileUrl | String | https://dmsxxx | SQL附件下载地址。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetDataCorrectSQLFile &Tid=-1
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <FileUrl>https://dms-idb-hangzhou.oss-cn-
hangzhou.aliyuncs.com/uplJMIpQ%3D</FileUrl>
    <RequestId>386EAA20-67FB-4D06-B7BF-2ABA11241185</RequestId>
    <Success>true</Success>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "FileUrl" : "https://dms-idb-hangzhou.oss-cn-hangzhou.aliyuncs.com/uplJMIpQ%3D",
  "RequestId" : "386EAA20-67FB-4D06-B7BF-2ABA11241185",
  "Success" : true
}
```

##### CreateDataCronClearOrder

目前仅支持MySQL实例调用此接口。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDataCron ClearOrder | 系统规定参数。取值：CreateDataCronClearOrder。 |
| Comment | String | 是 | test | 业务背景，以减少沟通成本。 |
| RelatedUserList | Array of Long | 否 | 243253 | 相关人ID，设置的相关人员可查看工单， 并协同工作，非相关人员则不能查看工单 （管理员、DBA除外）。 |
| Param | Object | 是 |  | 工单参数。 |
| Classify | String | 否 | test | 数据变更原因。 |
| DbItemList | Array | 是 |  | 变更的数据库列表。 |
| DbId | Long | 是 | 10**** | 数据库ID，可调用SearchDatabase接口获取。 |
| Logic | Boolean | 是 | false | 是否为逻辑库，取值： true：是 false：否 |
| CronFormat | String | 是 | 0 0 2 * * ? | Crontab表达式。 |
| CronClearItemLi st | Array | 是 |  | 待清理的数据表列表。 |

数据管理

| TableName | String | 是 | t1 | 表名，您可以调用ListTables接口获取该参数。 |
|---|---|---|---|---|
| ColumnName | String | 是 | gmt create _ | 字段名。 |
| RemainDays | Long | 是 | 7 | 保留时长，即历史数据清理的规则，单位为天。例如您配置为7天，DMS将在执行时删除7天前的数据。 |
| TimeUnit | String | 否 | MILLISECONDS | 时间精度类型，当选择字段为日期数值型存储时使用，取值： MILLISECONDS：毫秒 SECONDS：秒 |
| FilterSQL | String | 否 | where 1 = 1 | 过滤条件。 |
| specifyDuration | Boolean | 是 | true | 是否指定执行时长，取值： true：指定执行时长，到达指定时间后即停止执行。 false：不指定执行时长，直到清理结束。 |
| DurationHour | Long | 否 | 4 | 执行时长，单位为小时。 说明当specifyDuration参数为true时，该参数必填。 |
| AttachmentKey | String | 否 | order attachem _ ent.txt | 工单补充附件，对本次操作进行补充说明。 您可以调用GetUserUploadFileJob接口获取该参数。 |
| Tid | Long | 否 | 123454324 | 租户ID。 说明取自系统右上角头像处悬停展示的租户ID信息。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据管理

| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| CreateOrderRe sult | Array of Long | 1341532 | 工单号。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=CreateDataCronClearOrder &Comment=test &RelatedUserList=[243253] &Param={"Classify":"test","DbItemList":[{"DbId":10****,"Logic":false}],"CronFormat":"0 0 2 * * ?","CronClearItemList": [{"TableName":"t1","ColumnName":"gmt_create","RemainDays":7,"TimeUnit":"MILLISECONDS","Fi erSQL":"where 1 = 1"}],"specifyDuration":true,"DurationHour":4} &AttachmentKey=order_attachement.txt &Tid=123454324
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId>
    <Success>true</Success>
    <CreateOrderResult>1341532</CreateOrderResult>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
  "Success" : true,
}
```

数据管理

##### CreateDataImportOrder

关于该功能的更多说明，请参见数据导入。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDataImpo rtOrder | 系统规定参数。取值：CreateDataImportOrder。 |
| Comment | String | 是 | test | 数据导入的业务背景，以减少沟通成本。 |
| RelatedUserList | Array of Long | 否 | 51**** | 变更相关人的用户ID，设置的相关人员可查看工单，并协同工作，非相关人员则不能查看工单（管理员、DBA除外）。 |
| Param | Object | 是 |  | 工单参数。 |
| Classify | String | 否 | test | 数据导入原因。 |
| AttachmentNam e | String | 是 | order text _ | 导入数据的附件 Key（AttachmentKey），可通过调用接口GetUserUploadFileJob获取该参数的值。 |
| DbItemList | Array | 是 |  | 待导入的数据库列表，当前仅支持导入一个库。 |
| DbId | Long | 是 | 1860**** | 数据库ID（DatabaseId），数据库分为物理库和逻辑库两种： 物理库ID：可通过调用接口ListDatabases或SearchDatabase 获取该参数的值。 逻辑库ID：可通过调用接口ListLogicDatabases或SearchData base获取该参数的值。 |
| Logic | Boolean | 是 | false | 是否为逻辑库，取值如下： true：逻辑库 false：物理库说明如果取值为true，目标数据库必须为逻辑库。 |

数据管理

| FileType | String | 是 | CSV | 文件类型，取值如下： SQL：SQL文件 CSV：CSV文件 |
|---|---|---|---|---|
| FileEncoding | String | 否 | AUTO | 文件编码，取值如下： AUTO：自动识别 UTF-8：UTF8编码 GBK：GBK编码 ISO-8859-1：ISO-8859-1编码 |
| TableName | String | 否 | Table text _ | 选择CSV格式文件导入数据的目标表。 说明如果FileType为CSV，该参数必填。 |
| InsertType | String | 否 | INSERT | 插入类型，取值： INSERT：插入数据时数据库会检查主键（PrimaryKey），如果出现重复会报错。 INSERT IGNORE：如果表中已经存 _ 在相同的记录，则忽略当前新数据。 REPLACE INTO：如果表中已经有某 _ 行数据（根据主键或者唯一索引判断），则先删除此行数据，然后插入新的数据。 说明如果FileType为CSV，该参数必填。 |
| CsvFirstRowIsCol umnDef | Boolean | 否 | true | CSV格式的类型，取值如下： true：CSV表格首行是字段名。 false：CSV表格首行是数据。 说明如果FileType为CSV，该参数必填。 |
| IgnoreError | Boolean | 否 | false | 是否忽略报错，取值如下： true：忽略，遇到错误会跳过当前失败 SQL脚本，继续执行。 false：不忽略，遇到出错则中断后面的SQL脚本，不再执行。 |

数据管理

| ImportMode | String | 否 | FAST MODE _ | 导入模式，取值如下： FAST MODE：极速模式，在执行阶 _ 段读取文件，将SQL语句直接执行到指定的目标库。该模式安全性相比安全模式要低，但是执行时效较高。 SAFE MODE：安全模式，在预检查 _ 阶段会解析文件并将SQL或CSV数据缓存入库，执行时再从缓存库中读出来执行到指定的目标库。该模式安全性较好，但是执行时效相比极速模式要低。 |
|---|---|---|---|---|
| RollbackSQL | String | 否 | empty | 回滚SQL语句。 说明如果RollbackSqlType为TEXT，该参数必填。 |
| RollbackAttachm entName | String | 否 | rollback.sql | 回滚SQL附件Key（AttachmentKey）， 可通过调用接口GetUserUploadFileJob获取该参数的值。 说明如果RollbackSqlType为ATTACH MENT，该参数必填。 |
| RollbackSqlType | String | 否 | TEXT | 回滚SQL的提交方式，取值如下： TEXT：文本 ATTACHMENT：附件 |
| AttachmentKey | String | 否 | order attachme _ nt.txt | 工单附件Key，补充当前工单信息。可通过调用接口GetUserUploadFileJob获取该参数的值。 |
| Tid | Long | 否 | 3*** | 租户ID，可通过调用接口GetUserActiveTenant或ListUserTen ants获取该参数的值。 |
| RegionId | String | 否 | cn-hangzhou | DMS服务地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。 |

数据管理

| Success | Boolean | true | 请求是否成功，返回值： true：请求成功 false：请求失败 |
|---|---|---|---|
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| CreateOrderRe sult | Array of Long | 1**** | 工单号。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=CreateDataImportOrder &Comment=test &RelatedUserList=[51****] &Param={"Classify":"test","AttachmentName":"order_text","DbItemList": [{"DbId":1860****,"Logic":false}],"FileType":"CSV","FileEncoding":"AUTO","TableName":"Tab _text","InsertType":"INSERT","CsvFirstRowIsColumnDef":true,"IgnoreError":false,"ImportMod :"FAST_MODE"} &AttachmentKey=order_attachment.txt
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId>
    <Success>true</Success>
    <CreateOrderResult>1****</CreateOrderResult>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
  "Success" : true,
}
```

数据管理

#### 结构设计

##### CreatePublishGroupTask

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreatePublishGr oupTask | 系统规定参数。取值：CreatePublishGroupTask。 |
| DbId | Integer | 是 | 12345 | 执行的数据库ID。 |
| Logic | Boolean | 是 | false | 是否为逻辑库。 |
| OrderId | Long | 是 | 142435 | 工单ID。 |
| PublishStrategy | String | 是 | IMMEDIATELY | 执行策略，取值和说明： IMMEDIATELY： 立即执行 REGULARLY： 定时执行 |
| Tid | Long | 是 | -1 | 租户ID。 |
| PlanTime | String | 否 | 2019-10-10 00:00:00 | 定时执行计划时间。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

数据管理

| TaskId | Long | 413452 | 任务ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreatePublishGroupTask &DbId=12345 &Logic=false &OrderId=142435 &PublishStrategy=IMMEDIATELY &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>78C93646-D9B1-4E6E-B5FD-C69F94A7905A</RequestId> <Success>true</Success> <TaskId>13424</TaskId>
```

`JSON` 格式

```json
{
  "RequestId": "78C93646-D9B1-4E6E-B5FD-C69F94A7905A",
  "Success": true,
  "TaskId": 13424
}
```

##### ListDDLPublishRecords

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 3214325 | 工单ID。 说明您可以通过调用CreateOrder接口创建结构设计工单，并获取工单ID。 |
| Tid | Long | 否 | 1 | 租户ID。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A1549FB0-D4B8- 4140-919F- 17322C1072B8 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| DDLPublishRec ordList | Array of DDLPublishRec ord |  | 发布记录列表。 |
| AuditStatus | String | CANCEL | 审批状态，取值如下： EXEMPT PASS：免批通过 _ TO AUDIT：等待审批 _ CANCEL：撤销审批 SUCCESS：审批通过 FAIL：未通过 |
| AuditExpireTi me | String | 2020-12-14 20:52:38 | 审批过期时间。 |
| CreatorId | Long | 1423 | 工单创建人的用户ID，非阿里云UID。可通过调用GetUser接口获取的UserId参数获取。 |
| Finality | Boolean | true | 是否终止，取值： true：是 false：否说明导致终止的原因有审批撤回或在指定执行时间前未完成审批等。 |
| FinalityReason | String | CANCEL | 终止原因。 |

数据管理

| PublishStatus | String | AUDIT | 发布状态，取值如下： START：创建 ANALYZE：分析 AUDIT：审批 DISPATCH：调度 SUCCESS：成功 |
|---|---|---|---|
| RiskLevel | String | LOW RISK _ | 风险等级，取值： NONE RISK：无风险 _ LOW RISK：低风险 _ MIDDLE RISK：中风险 _ HIGH RISK：高风险 _ |
| StatusDesc | String | CANCEL | 发布状态描述。 |
| WorkflowInsta nceId | Long | 432153 | 审批流ID。 |
| PublishTaskInf oList | Array of PublishTaskInf o |  | 发布任务信息列表。 |
| DbId | Long | 4325 | 数据库ID。 |
| Logic | Boolean | false | 是否为逻辑库，取值： true：是 false：否 |
| PlanTime | String | 2020-12-14 20:52:38 | 计划发布时间。 |
| PublishStrateg y | String | IMMEDIATELY | 发布策略，取值： IMMEDIATELY：立即执行 REGULARLY：定时执行 |
| StatusDesc | String | NONE | 状态描述。 |
| TaskJobStatus | String | NONE | 任务状态。 |
| PublishJobList | Array of PublishJob |  | 发布任务列表。 |
| ExecuteCount | Long | 0 | 已经执行的SQL数量。 |

数据管理

| Scripts | String | ALTER TABLE test toolkit renam _ _ e table after rena _ _ _ me MODIFY COLUMN gmt modified _ datetime NOT NULL | 变更脚本。 |
|---|---|---|---|
| TableName | String | test toolkit renam _ _ e table after rena _ _ _ me | 变更的表名。 |
| StatusDesc | String | NONE | 状态描述。 |
| TaskJobStatus | String | NONE | 发布任务状态，取值如下： NONE：未知 SUCCESS：执行成功 FAIL：执行失败 |
| DBTaskGroupI d | Long | 423515 | SQL任务分组ID。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=ListDDLPublishRecords
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>AEF89401-5456-431A-9709-2C6C45657B51</RequestId>
    <Success>true</Success>
    <DDLPublishRecordList>
```

`<StatusDesc>`所有库均执行成功`</StatusDesc>`

```xml
        <PublishTaskInfoList>
```

`<StatusDesc>`所有表均执行成功，回调完成`</StatusDesc>`

```xml
            <TaskJobStatus>SUCCESS</TaskJobStatus>
            <PublishStrategy>IMMEDIATELY</PublishStrategy>
            <DbId>8000009</DbId>
            <PublishJobList>
```

`<StatusDesc>`执行成功，回调成功`</StatusDesc>`

```xml
                <TableName>big_table</TableName>
                <Scripts>CREATE TABLE `big_table` (
                    `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
                    `name` varchar(64) NOT NULL COMMENT '名称',
                    `long_text_a` varchar(1024) NULL COMMENT 'A文本',
`longtextb`varchar(1024)NULLCOMMENT'B文本',
```

数据管理

```xml
                    long_text_b varchar(1024) NULL COMMENT B文本,
                    PRIMARY KEY (`id`)
                    ) DEFAULT CHARACTER SET=utf8 COMMENT='大表变更';</Scripts>
                <TaskJobStatus>SUCCESS</TaskJobStatus>
                <ExecuteCount>1</ExecuteCount>
                <DBTaskGroupId>2220000</DBTaskGroupId>
            </PublishJobList>
            <PublishJobList>
```

`<StatusDesc>`执行成功，回调成功`</StatusDesc>`

```xml
                <TableName>data_modify</TableName>
                <Scripts>CREATE TABLE `data_modify` (
                    `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
                    `name` varchar(256) NOT NULL COMMENT '姓名',
                    `phone` varchar(32) NULL COMMENT '电话',
                    `sex` varchar(32) NULL COMMENT '性别',
                    `email` varchar(256) NULL COMMENT '邮箱',
                    `user_desc` varchar(1024) NULL COMMENT '备注',
                    PRIMARY KEY (`id`)
                    ) DEFAULT CHARACTER SET=utf8 COMMENT='数据修改测试表';</Scripts>
                <TaskJobStatus>SUCCESS</TaskJobStatus>
                <ExecuteCount>1</ExecuteCount>
                <DBTaskGroupId>2220800</DBTaskGroupId>
            </PublishJobList>
            <PlanTime>2020-12-23 11:37:00</PlanTime>
            <Logic>false</Logic>
        </PublishTaskInfoList>
        <AuditStatus>SUCCESS</AuditStatus>
        <CreatorId>260006</CreatorId>
        <Finality>true</Finality>
        <AuditExpireTime>2020-12-23 11:37:00</AuditExpireTime>
        <WorkflowInstanceId>850007</WorkflowInstanceId>
        <RiskLevel>LOW_RISK</RiskLevel>
```

`<FinalityReason>`执行成功，任务结束`</FinalityReason>`

```xml
        <PublishStatus>SUCCESS</PublishStatus>
    </DDLPublishRecordList>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "AEF89401-5456-431A-9709-2C6C45657B51",
  "Success" : true,
  "DDLPublishRecordList" : [ {
```

`"StatusDesc" : "`所有库均执行成功`",`

```json
    "PublishTaskInfoList" : [ {
```

`"StatusDesc" : "`所有表均执行成功，回调完成`",`

```json
      "TaskJobStatus" : "SUCCESS",
      "PublishStrategy" : "IMMEDIATELY",
      "DbId" : 8000009,
      "PublishJobList" : [ {
```

`"StatusDesc" : "`执行成功，回调成功`",`

```json
        "TableName" : "big_table",
        "Scripts" : "CREATE TABLE `big_table` (\n\t`id` bigint unsigned NOT NULL AUTO_I
NCREMENT COMMENT '主键',\n\t`name` varchar(64) NOT NULL COMMENT '名称',\n\t`long_text_a` varchar(1024) NULL COMMENT 'A文本',\n\t`long_text_b` varchar(1024) NULL COMMENT 'B文本',\n\tPRIMARY KEY (`id`)\n) DEFAULT CHARACTER SET=utf8 COMMENT='大表变更';",
        "TaskJobStatus" : "SUCCESS",
        "ExecuteCount" : 1,
        "DBTaskGroupId" : 2220000
      }, {
```

`"StatusDesc" : "`执行成功，回调成功`",`

```json
        "TableName" : "data_modify",
        "Scripts" : "CREATE TABLE `data_modify` (\n\t`id` bigint unsigned NOT NULL AUTO
_INCREMENT COMMENT '主键',\n\t`name` varchar(256) NOT NULL COMMENT '姓名',\n\t`phone` va rchar(32) NULL COMMENT '电话',\n\t`sex` varchar(32) NULL COMMENT '性别',\n\t`email` varc har(256) NULL COMMENT '邮箱',\n\t`user_desc` varchar(1024) NULL COMMENT '备注',\n\tPRIMARY KEY (`id`)\n) DEFAULT CHARACTER SET=utf8 COMMENT='数据修改测试表';",
        "TaskJobStatus" : "SUCCESS",
        "ExecuteCount" : 1,
        "DBTaskGroupId" : 2220800
      } ],
      "PlanTime" : "2020-12-23 11:37:00",
      "Logic" : false
    } ],
    "AuditStatus" : "SUCCESS",
    "CreatorId" : 260006,
    "Finality" : true,
    "AuditExpireTime" : "2020-12-23 11:37:00",
    "WorkflowInstanceId" : "850007",
    "RiskLevel" : "LOW_RISK",
```

`"FinalityReason" : "`执行成功，任务结束`",`

```json
    "PublishStatus" : "SUCCESS"
  } ]
}
```

#### 数据导出

数据管理

##### ExecuteDataExport

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ExecuteDataExp ort | 系统规定参数。取值：ExecuteDataExport。 |
| ActionDetail | Json | 否 | { "fileType": "CSV", "encoding": "" } | 执行操作参数： json { "fileType": "CSV", // 导出格式 "encoding": "" // 编码 } |
| OrderId | Long | 是 | 1234 | 工单ID。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | FE8EE2F1-4880- 46BC-A704- 5CF63EAF9A04 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例数据管理

```
http(s)://[Endpoint]/?ActionDetail={ "fileType": "CSV", "encoding": "" } &OrderId=1234 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "FE8EE2F1-4880-46BC-A704-5CF63EAF9A04",
  "Success": true
}
```

##### GetDataExportDownloadURL

调用GetDataExportDownloadURL接口获取数据导出结果附件下载地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataExportD ownloadURL | 系统规定参数。取值：GetDataExportDownloadURL 。 |
| OrderId | Long | 是 | 12345 | 工单ID。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DownloadURL Result | Struct |  | 导出文件下载地址。 |
| HasResult | Boolean | true | 是否有下载结果。 |

数据管理

| TipMessage | String | tip message | 异常提示信息。 |
|---|---|---|---|
| URL | String | xxx | 导出文件下载地址。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDataExportDownloadURL &OrderId=12345 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DownloadURLResult>
    <URL>https://dms-idb-hangzhou.oss-cn-hangzhou.aliyuncs.com/xxx.zip?
Expires=1574384313&amp;OSSAccessKeyId=wSa97B52GzF****&amp;Signature=HQQWBRSKiVV6cupugh1/e SqXg%3D</URL>
    <HasResult>true</HasResult>
</DownloadURLResult> <RequestId>4BF24EA5-9013-4C85-AE68-6C23AF5E0097</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "DownloadURLResult": {
    "URL": "https://dms-idb-hangzhou.oss-cn-hangzhou.aliyuncs.com/xxx.zip?
Expires=1574384313&OSSAccessKeyId=wSa97B52GzF****&Signature=HQQWBRSKiVV6cupugh1/eAVSqXg%3
```

,

```json
    "HasResult": true
  },
  "RequestId": "4BF24EA5-9013-4C85-AE68-6C23AF5E0097",
  "Success": true
}
```

数据管理

##### GetDataExportOrderDetail

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataExportO rderDetail | 系统规定参数。取值：GetDataExportOrderDetail。 |
| OrderId | Long | 是 | 123456 | 工单ID。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DataExportOrd erDetail | Struct |  | 数据导出工单详情信息。 |
| KeyInfo | Struct |  | 状态信息。 |
| JobStatus | String | EXPORT SUCCESS _ | 导出工单状态，取值和说明如下： PRE CHECKING: 执行预校验 _ PRE CHECK SUCCESS: 预校验成功 _ _ PRE CHECK FAIL: 预校验失败 _ _ WAITING APPLY AUDIT: 等待提交审批 _ _ APPLY AUDIT SUCESS: 提交审批成功 _ _ ENABLE EXPORT: 审批通过,允许导出 _ WAITING EXPORT: 等待调度进行导出 _ DOING EXPORT: 执行导出 _ EXPORT FAIL: 导出失败 _ EXPORT SUCCESS: 导出成功 _ |
| PreCheckId | Long | 123 | 预校验ID。 |
| OrderDetail | Struct |  | 工单详情信息。 |
| ActualAffectRo ws | Long | 1 | 系统校验影响行数。 |

数据管理

| Classify | String | text | 导出原因分类。 |
|---|---|---|---|
| Database | String | xxx@xxx:3306 | 导出数据库。 |
| DbId | Integer | 123 | 导出数据库ID。 |
| EnvType | String | test | 导出数据库环境信息。 |
| ExeSQL | String | select 1 | 执行的导出SQL。 |
| IgnoreAffectRo ws | Boolean | false | 是否忽略影响行数。 |
| IgnoreAffectRo wsReason | String | empty | 忽略校验原因。 |
| Logic | Boolean | false | 是否逻辑库。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDataExportOrderDetail &OrderId=123456 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<DataExportOrderDetail>
    <KeyInfo>
        <PreCheckId>15544</PreCheckId>
        <JobStatus>EXPORT_SUCCESS</JobStatus>
    </KeyInfo>
    <OrderDetail>
        <Logic>false</Logic>
        <ActualAffectRows>1</ActualAffectRows>
        <ExeSQL>select 1;</ExeSQL>
        <Database>yuyang_test@xxx:3306【yuyang_test_xxx】杭州非单元化</Database>
        <IgnoreAffectRows>false</IgnoreAffectRows>
        <DbId>116367</DbId>
        <Classify>测试</Classify>
        <EnvType>product</EnvType>
    </OrderDetail>
</DataExportOrderDetail> <RequestId>78C93646-D9B1-4E6E-B5FD-C69F94A7905A</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "DataExportOrderDetail": {
    "KeyInfo": {
      "PreCheckId": 15544,
      "JobStatus": "EXPORT_SUCCESS"
    },
    "OrderDetail": {
      "Logic": false,
      "ActualAffectRows": 1,
      "ExeSQL": "select 1;",
      "Database": "yuyang_test@xxx:3306【yuyang_test_xxx】杭州非单元化",
      "IgnoreAffectRows": false,
      "DbId": 116367,
      "Classify": "测试",
      "EnvType": "product"
    }
  },
  "RequestId": "78C93646-D9B1-4E6E-B5FD-C69F94A7905A",
  "Success": true
}
```

#### 库表同步

##### GetStructSyncOrderDetail

调用GetStructSyncOrderDetail接口，获取结构同步的工单详情信息。

**请求参数**

数据管理

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 否 | 432553 | 工单号。 |
| Tid | Long | 否 | 3*** | 租户ID。 说明鼠标移动到界面右上角的头像处，查看租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4E1D2B4D-3E53- 4ABC-999D- 1D2520B3471A | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| StructSyncOrd erDetail | object |  | 结构同步工单详情。 |
| SourceDataba seInfo | object |  | 源库信息。 |
| DbId | Long | 432532 | 库ID。 |
| SearchName | String | test | 库搜索名。 |
| DbType | String | MySQL | 数据库类型。 |
| EnvType | String | dev | 实例的环境类型。 |
| Logic | Boolean | false | 是否为逻辑库，取值： true：是 false：否 |

数据管理

| TargetDatabas eInfo | object |  | 目标库信息。 |
|---|---|---|---|
| DbId | Long | 432543 | 库ID。 |
| SearchName | String | test | 库搜索名。 |
| DbType | String | MySQL | 数据库类型。 |
| EnvType | String | dev | 实例的环境类型。 |
| Logic | Boolean | false | 是否为逻辑库，取值： true：是 false：否 |
| SourceType | String | VERSION | 表结构类型，取值和说明如下： DATASOURCE：系统默认的最新版。 VERSION：手动输入的历史版本。 |
| SourceVersionI nfo | object |  | 源版本信息。 说明仅当SourceType为VERSION时显示。 |
| VersionId | String | e179bbb8163dcdcf acda24858bedb4d 8006ae2b8 | 版本号。 |
| TargetType | String | DATASOURCE | 表结构类型，取值和说明如下： DATASOURCE：系统默认的最新版。 VERSION：手动输入的历史版本。 |
| TargetVersionI nfo | object |  | 目标版本信息。 说明仅当SourceType为VERSION时显示。 |
| VersionId | String | e179bbb8163dcdcf acda24858bedb4d 8006ae2b8 | 版本号。 |
| TableInfoList | Array of TableInfo |  | 同步的表信息。 |
| SourceTableN ame | String | test tbl _ | 源表表名。 |

数据管理

| TargetTableNa me | String | test tbl _ | 目标表表名。 |
|---|---|---|---|
| IgnoreError | Boolean | false | 是否忽略报错，取值： true：忽略，遇到错误会跳过当前失败SQL 脚本，继续执行。 false：不忽略，遇到出错则中断后面的SQL 脚本，不再执行。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?OrderId=432553 &Tid=3***
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>CA4E966B-1A57-4230-B0BB-CBB9CAF2CEDC</RequestId>
    <StructSyncOrderDetail>
        <SourceDatabaseInfo>
            <SearchName>poc_dev@rm-uxxxxx.mysql.rds.aliyuncs.com:3306</SearchName>
            <DbId>800000</DbId>
            <Logic>false</Logic>
            <EnvType>dev</EnvType>
            <DbType>mysql</DbType>
        </SourceDatabaseInfo>
        <SourceType>DATASOURCE</SourceType>
        <TargetType>DATASOURCE</TargetType>
        <IgnoreError>false</IgnoreError>
            <SearchName>film@rm-uf64xxxxe.mysql.rds.aliyuncs.com:3306</SearchName>
            <DbId>700000</DbId>
            <Logic>false</Logic>
            <EnvType>dev</EnvType>
            <DbType>mysql</DbType>
        <TableInfoList>
            <SourceTableName>*</SourceTableName>
            <TargetTableName>*</TargetTableName>
        </TableInfoList>
    </StructSyncOrderDetail>
    <Success>true</Success>
```

`JSON` 格式数据管理

|  | HTTP/1.1 200 OK Content-Type:application/json { "RequestId" : "CA4E966B-1A57-4230-B0BB-CBB9CAF2CEDC", "StructSyncOrderDetail" : { "SourceDatabaseInfo" : { "SearchName" : "poc dev@rm-uxxxxx.mysql.rds.aliyuncs.com:3306", _ "DbId" : 800000, "Logic" : false, "EnvType" : "dev", "DbType" : "mysql" }, "SourceType" : "DATASOURCE", "TargetType" : "DATASOURCE", "IgnoreError" : false, "TargetDatabaseInfo" : { "SearchName" : "film@rm-uf64xxxxe.mysql.rds.aliyuncs.com:3306", "DbId" : 700000, "Logic" : false, "EnvType" : "dev", "DbType" : "mysql" }, "TableInfoList" : [ { "SourceTableName" : "*", "TargetTableName" : "*" } ] }, "Success" : true } |  |
|---|---|---|

##### GetStructSyncExecSqlDetail

调用GetStructSyncExecSqlDetail接口，获取结构同步的执行SQL脚本。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 342153 | 工单号。 |
| PageNumber | Long | 否 | 1 | 第几页。 |
| PageSize | Long | 否 | 20 | 每页数据量。 |
| Tid | Long | 否 | 1 | 租户ID。 说明鼠标移动到界面右上角的头像处，查看租户ID。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1810E635-A2D7- 428B-BAA9- 85DAEB9B1A77 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| StructSyncExe cSqlDetail | object |  | 执行SQL脚本的详情信息。 |
| TotalSqlCount | Long | 1 | SQL总数。 |

数据管理

| ExecSql | String | /* origin table[helloz bak] _ exist, target table[helloz bak] _ not exist */\n/* generate [helloz bak] create _ table sql */\ncreate table `helloz bak`(\n\t`id _ ` bigint(20) UNSIGNED NOT NULL AUTO INCREMENT _ COMMENT '主键',\n\t`gmt create _ ` datetime NOT NULL COMMENT '创建时间',\n\t`gmt modifi _ ed` datetime NOT NULL COMMENT '修改时间',\n\t`num` int(11) NOT NULL COMMENT '编号',\n\t`addr` varchar(50) CHARACTER SET utf8 COLLATE utf8 general ci _ _ NOT NULL COMMENT '地址',\n\tPRIMARY KEY (`id`)\n)\nDEFAULT CHARACTER SET=utf8 COLLATE=utf8 gen _ eral ci\nCOMMENT _ ='test'\n\n; | 执行的SQL脚本。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?OrderId=342153 &PageNumber=1 &PageSize=20 &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <StructSyncExecSqlDetail>
        <ExecSql>/****** 目标库：film@rm-uxxxxxxxx.mysql.rds.aliyuncs.com:3306 ******/
            /* origin table[data_modify] exist, target table[data_modify] not exist */
            /* generate [data_modify] create table sql */
            create table `data_modify` (
            `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
            `name` varchar(256) NOT NULL COMMENT '姓名',
            `phone` varchar(32) DEFAULT NULL COMMENT '电话',
            `sex` varchar(32) DEFAULT NULL COMMENT '性别',
            `email` varchar(256) DEFAULT NULL COMMENT '邮箱',
            `user_desc` varchar(1024) DEFAULT NULL COMMENT '备注',
            PRIMARY KEY (`id`)
```

`) DEFAULT CHARSET=utf8 COMMENT='`数据修改测试表';

```
            /* origin table[task_data] exist, target table[task_data] not exist */
            /* generate [task_data] create table sql */
            create table `task_data` (
            `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
            `gmt_create` datetime NOT NULL COMMENT '创建时间',
            `gmt_modified` datetime NOT NULL COMMENT '修改时间',
            `content` text COMMENT '测试数据',
            PRIMARY KEY (`id`)
```

`) DEFAULT CHARSET=utf8mb4 COMMENT='`任务编排测试表';

```xml
        </ExecSql>
        <TotalSqlCount>2</TotalSqlCount>
    </StructSyncExecSqlDetail>
    <RequestId>1E4E71DA-9346-4254-B19D-BC5FF6BF34EC</RequestId>
    <Success>true</Success>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "StructSyncExecSqlDetail" : {
    "ExecSql" : "/****** 目标库：film@rm-uxxxxxxxx.mysql.rds.aliyuncs.com:3306
******/\n\n/* origin table[data_modify] exist, target table[data_modify] not exist */\n
/* generate [data_modify] create table sql */\ncreate table `data_modify` (\n `id` big int(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',\n `name` varchar(256) NOT NULL COMMENT '姓名',\n `phone` varchar(32) DEFAULT NULL COMMENT '电话',\n `sex` varchar(32) DEFAULT NULL COMMENT '性别',\n `email` varchar(256) DEFAULT NULL COMMENT ' 邮箱',\n `user_desc` varchar(1024) DEFAULT NULL COMMENT '备注',\n PRIMARY KEY (`id`)\n) DEFAULT CHARSET=utf8 COMMENT='数据修改测试表';\n\n/* origin table[task_data] ex ist, target table[task_data] not exist */\n/* generate [task_data] create table sql */\ ncreate table `task_data` (\n `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',\n `gmt_create` datetime NOT NULL COMMENT '创建时间',\n `gmt_modified` datetime NOT NULL COMMENT '修改时间',\n `content` text COMMENT '测试数据',\n PRIMARY KEY (`id`)\n) DEFAULT CHARSET=utf8mb4 COMMENT='任务编排测试表';\n\n\n\n",
    "TotalSqlCount" : 2
  },
  "RequestId" : "1E4E71DA-9346-4254-B19D-BC5FF6BF34EC",
  "Success" : true
}
```

##### ExecuteStructSync

若实例的安全规则需要通过审批才能进行同步，请先调用SubmitStructSyncOrderApproval接口发起审批流程，并完成审批。 您可以调用GetStructSyncJobDetail接口查询目标实例是否需要审批。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 112345 | 工单号。 |
| Tid | Long | 否 | 1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据管理

| RequestId | String | 4E1D2B4D-3E53- 4ABC-999D- 1D2520B3471A | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=ExecuteStructSync &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>4E1D2B4D-3E53-4ABC-999D-1D2520B3471A</RequestId>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "4E1D2B4D-3E53-4ABC-999D-1D2520B3471A",
  "Success" : true
}
```

##### GetStructSyncJobAnalyzeResult

调用GetStructSyncJobAnalyzeResult接口，获取结构同步的任务分析结果。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 1342355 | 工单号 |

数据管理

| CompareType | String | 否 | CREATE TABLE _ | 比较类型，取值： CREATE TABLE：创建表 _ ALTER TABLE：修改表 _ EQUAL TABLE：相同的表 _ PASS TABLE：跳过的表 _ NOT COMPARE：待分析的表 _ |
|---|---|---|---|---|
| PageNumber | Long | 否 | 1 | 第几页。 |
| PageSize | Long | 否 | 20 | 每页数据量。 |
| Tid | Long | 否 | 1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1810E635-A2D7- 428B-BAA9- 85DAEB9B1A77 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| StructSyncJob AnalyzeResult | object |  | 结构同步任务分析结果。 |
| SummaryList | Array of Summary |  | 统计结果列表。 |
| CompareType | String | CREATE TABLE _ | 比较类型，取值： CREATE TABLE：创建表 _ ALTER TABLE：修改表 _ EQUAL TABLE：相同的表 _ PASS TABLE：跳过的表 _ NOT COMPARE：待分析的表 _ |

数据管理

| Count | Long | 1 | 表的数量。 |
|---|---|---|---|
| ResultList | Array of Result |  | 分析结果详情列表。 |
| SourceTableN ame | String | helloz bak _ | 源表表名。 |
| TargetTableNa me | String | helloz bak _ | 目标表表名。 |
| Script | String | /* origin table[helloz bak] _ exist, target table[helloz bak] _ not exist */\n/* generate [helloz bak] create _ table sql */\ncreate table `helloz bak`(\n\t`id _ ` bigint(20) UNSIGNED NOT NULL AUTO INCREMENT _ COMMENT '主键',\n\t`gmt create _ ` datetime NOT NULL COMMENT '创建时间',\n\t`gmt modifi _ ed` datetime NOT NULL COMMENT '修改时间',\n\t`num` int(11) NOT NULL COMMENT '编号',\n\t`addr` varchar(50) CHARACTER SET utf8 COLLATE utf8 general ci _ _ NOT NULL COMMENT '地址',\n\tPRIMARY KEY (`id`)\n)\nDEFAULT CHARACTER SET=utf8 COLLATE=utf8 gen _ eral ci\nCOMMENT _ ='test'\n\n; | SQL脚本。 |

**示例**

请求示例数据管理

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetStructSyncJobAnalyzeResult &CompareType=CREATE_TABLE &PageNumber=1 &PageSize=20 &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <StructSyncJobAnalyzeResult>
        <ResultList>
            <SourceTableName>data_modify</SourceTableName>
            <Script>/* origin table[data_modify] exist, target table[data_modify] not
exist */
                /* generate [data_modify] create table sql */
                create table `data_modify` (
                `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
                `name` varchar(256) NOT NULL COMMENT '姓名',
                `phone` varchar(32) DEFAULT NULL COMMENT '电话',
                `sex` varchar(32) DEFAULT NULL COMMENT '性别',
                `email` varchar(256) DEFAULT NULL COMMENT '邮箱',
                `user_desc` varchar(1024) DEFAULT NULL COMMENT '备注',
                PRIMARY KEY (`id`)
                ) DEFAULT CHARSET=utf8 COMMENT='数据修改测试表';</Script>
            <TargetTableName>data_modify</TargetTableName>
        </ResultList>
        <ResultList>
            <SourceTableName>task_data</SourceTableName>
            <Script>/* origin table[task_data] exist, target table[task_data] not exist
```

`*/`

```xml
                /* generate [task_data] create table sql */
                create table `task_data` (
                `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
                `gmt_create` datetime NOT NULL COMMENT '创建时间',
                `gmt_modified` datetime NOT NULL COMMENT '修改时间',
                `content` text COMMENT '测试数据',
                PRIMARY KEY (`id`)
                ) DEFAULT CHARSET=utf8mb4 COMMENT='任务编排测试表';</Script>
            <TargetTableName>task_data</TargetTableName>
        </ResultList>
        <SummaryList>
            <CompareType>CREATE_TABLE</CompareType>
            <Count>2</Count>
        </SummaryList>
        <SummaryList>
            <CompareType>EQUAL_TABLE</CompareType>
            <Count>1</Count>
        </SummaryList>
    </StructSyncJobAnalyzeResult>
    <RequestId>472C5F33-198B-4A41-BF83-B2322636B583</RequestId>
    <Success>true</Success>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "StructSyncJobAnalyzeResult" : {
    "ResultList" : [ {
      "SourceTableName" : "data_modify",
      "Script" : "/* origin table[data_modify] exist, target table[data_modify] not exi
st */\n/* generate [data_modify] create table sql */\ncreate table `data_modify` (\n ` id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',\n `name` varchar(256) NOT NULL COMMENT '姓名',\n `phone` varchar(32) DEFAULT NULL COMMENT '电话',\n `sex` va rchar(32) DEFAULT NULL COMMENT '性别',\n `email` varchar(256) DEFAULT NULL COMMENT '邮箱',\n `user_desc` varchar(1024) DEFAULT NULL COMMENT '备注',\n PRIMARY KEY (`id`)\n)
```

`DEFAULT CHARSET=utf8 COMMENT='`数据修改测试表';",

```json
      "TargetTableName" : "data_modify"
    }, {
      "SourceTableName" : "task_data",
      "Script" : "/* origin table[task_data] exist, target table[task_data] not exist *
/\n/* generate [task_data] create table sql */\ncreate table `task_data` (\n `id` bigi nt(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',\n `gmt_create` datetime NOT NULL COMMENT '创建时间',\n `gmt_modified` datetime NOT NULL COMMENT '修改时间',\n `content` text COMMENT '测试数据',\n PRIMARY KEY (`id`)\n) DEFAULT CHARSET=utf8mb4 COMM
```

`ENT='`任务编排测试表';",

```json
      "TargetTableName" : "task_data"
    } ],
    "SummaryList" : [ {
      "CompareType" : "CREATE_TABLE",
      "Count" : 2
    }, {
      "CompareType" : "EQUAL_TABLE",
      "Count" : 1
    } ]
  },
  "RequestId" : "472C5F33-198B-4A41-BF83-B2322636B583",
  "Success" : true
}
```

##### SubmitStructSyncOrderApproval

调用SubmitStructSyncOrderApproval接口，提交结构同步工单至审批流程。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 4324535 | 工单号。 |
| Tid | Long | 否 | 1 | 租户ID。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4E1D2B4D-3E53- 4ABC-999D- 1D2520B3471D | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| WorkflowInsta nceId | Long | 432523 | 审批流程ID。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=SubmitStructSyncOrderApproval &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>72768811-B970-4733-85BE-A8659613BF23</RequestId>
    <WorkflowInstanceId>1000000</WorkflowInstanceId>
    <Success>true</Success>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "72768811-B970-4733-85BE-A8659613BF23",
  "WorkflowInstanceId" : 1000000,
  "Success" : true
}
```

##### CreateStructSyncOrder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Comment | String | 是 | test | 工单备注。 |
| RelatedUserList | Array of Long | 否 | 432435 | 相关人ID。 |
| Param | Object | 是 |  | 工单参数。 |
| Source | Object | 是 |  | 基准库信息。 |
| DbId | Long | 是 | 4324532 | 库ID，可调用SearchDatabase接口获取。 |
| DbSearchName | String | 是 | test | 库搜索名，可调用SearchDatabase接口获取。 |
| Logic | Boolean | 否 | false | 是否为逻辑库，取值： true：是 false：否 |
| VersionId | String | 否 | e179bbb8163dc dcfacda24858be db4d8006ae2b8 | 版本号，默认为最新的表结构版本。 |
| Target | Object | 是 |  | 目标库信息。 |
| DbId | Long | 是 | 432432 | 库ID，可调用SearchDatabase接口获取。 |

数据管理

| DbSearchName | String | 是 | test | 库搜索名，可调用SearchDatabase接口获取。 |
|---|---|---|---|---|
| Logic | Boolean | 否 | false | 是否为逻辑库，取值： true：是 false：否 |
| VersionId | String | 否 | e179bbb8163dc dcfacda24858be db4d8006ae2b8 | 版本号（默认不填）。 说明当您输入目标库的表结构版本号时，该工单仅会对比两个库之间的表结构。 |
| IgnoreError | Boolean | 否 | false | 是否忽略报错，取值： true：忽略，遇到错误会跳过当前失败 SQL脚本，继续执行。 false：不忽略，遇到出错则中断后面的SQL脚本，不再执行。 |
| TableInfoList | Array | 否 |  | 同步的表信息列表。 |
| SourceTableNa me | String | 否 | test tbl _ | 源表表名。 |
| TargetTableNam e | String | 否 | test tbl _ | 目标表表名。 |
| AttachmentKey | String | 否 | upload 3c7edea _ 3-e4c3-4403- 857d- 737043036f69 t _ est.sql | 上传附件成功后返回的附件Key，您可以调用GetUserUploadFileJob接口获取。 |
| Tid | Long | 否 | 1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4E1D2B4D-3E53- 4ABC-999D- 1D2520B3471A | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

数据管理

| ErrorMessage | String | UnknownError | 错误信息。 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| CreateOrderRe sult | Array of Long | 4325353 | 工单号。 |

**示例**

请求示例

```json
http(s)://dms-enterprise.aliyuncs.com/?Action=CreateStructSyncOrder &RelatedUserList=[432435] &Param={"Source": {"DbId":4324532,"DbSearchName":"test","Logic":false,"VersionId":"e179bbb8163dcdcfacda2485 edb4d8006ae2b8"},"Target": {"DbId":432432,"DbSearchName":"test","Logic":false,"VersionId":"e179bbb8163dcdcfacda24858 db4d8006ae2b8"},"SyncType":"STRUCT_TABLES","IgnoreError":false,"TableInfoList":[{"Sourc eTableName":"test_tbl","TargetTableName":"test_tbl"}]} &AttachmentKey=-1 &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <CreateOrderResult>2000000</CreateOrderResult>
    <RequestId>0DF19315-DCAF-4376-8006-1CEB0BBC6B13</RequestId>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "CreateOrderResult" : [ 2000000 ],
  "RequestId" : "0DF19315-DCAF-4376-8006-1CEB0BBC6B13",
  "Success" : true
}
```

##### GetStructSyncJobDetail

数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 432**** | 工单号。 |
| Tid | Long | 否 | 1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 48602B78-0DDF- 414C-8688- 70CAB6070115 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| StructSyncJob Detail | object |  | 结构同步任务详情。 |
| JobStatus | String | DBTASK SUCCESS _ | 任务状态，取值和说明如下： NEW：新创建。 COMPARING：正在对比结构。 COMPARE BREAK：对比手动中断。 _ COMPARE FINISH：对比完成。 _ NOT SCRIPTS：对比完成, 没有可执行脚 _ 本。 SUBMITED DBTASK：已提交DBTask。 _ DBTASK SUCCESS：DBTask执行成功。 _ SUBMITED WORKFLOW：提交审批。 _ WORKFLOW SUCCESS：审批结束。 _ |

数据管理

| Message | String | test | 任务描述信息。 |
|---|---|---|---|
| TableAnalyzed | Long | 2 | 已经分析的表。 |
| TableCount | Long | 2 | 表的总数。 |
| SqlCount | Long | 1 | SQL总数。 |
| ExecuteCount | Long | 1 | 已执行的SQL数量。 |
| SecurityRule | String | WITHOUT APPROV _ E | 安全规则描述，取值： CANNOT SYNC：不允许同步。 _ WITH APPROVE：需通过审批后进行同 _ 步，可调用 SubmitStructSyncOrderApproval接口发起审批流程。 WITHOUT APPROVE：不需要审批即可进 _ 行同步。 |
| DBTaskGroupI d | Long | 12345 | SQL任务分组ID。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetStructSyncJobDetail &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>C29D0A5F-BB9B-4CB9-A6B7-19B5433983CA</RequestId>
    <StructSyncJobDetail>
        <JobStatus>COMPARE_FINISH</JobStatus>
```

`<Message>`结构对比完成, 预览`SQL`已经生成`</Message>`

```xml
        <TableAnalyzed>6</TableAnalyzed>
        <TableCount>6</TableCount>
        <SecurityRule>WITH_APPROVE</SecurityRule>
        <DBTaskGroupId>3000000</DBTaskGroupId>
    </StructSyncJobDetail>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "C29D0A5F-BB9B-4CB9-A6B7-19B5433983CA",
  "StructSyncJobDetail" : {
    "JobStatus" : "COMPARE_FINISH",
```

`"Message" : "`结构对比完成, 预览`SQL`已经生成`",`

```json
    "TableAnalyzed" : 6,
    "TableCount" : 6,
    "SecurityRule" : "WITH_APPROVE",
    "DBTaskGroupId" : 3000000
  },
  "Success" : true
}
```

#### SQL审核

##### GetSQLReviewCheckResultStatus

调用GetSQLReviewCheckResultStatus接口，获取SQL审核工单的审核结果。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetSQLReviewC heckResultStatu s | 系统规定参数。取值：GetSQLReviewCheckResultSt atus。 |

数据管理

| OrderId | Long | 是 | 123321 | 工单号，您可以调用CreateSQLReviewOrder接口获取该参数。 |
|---|---|---|---|---|
| Tid | Long | 否 | 1 | 租户ID，您可以调用GetUserActiveTenant或ListUserTen ants接口获取该参数。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| Success | Boolean | true | 请求是否成功。 |
| CheckResultSt atus | Object |  | SQL审核结果。 |
| TotalSQLCount | Long | 10 | 总SQL数量，单位：条。 |
| CheckedCount | Long | 10 | 已审核SQL数量，单位：条。 |
| CheckStatusR esult | Object |  | 检测状态。 |
| New | Long | 0 | 等待审核的SQL数量，单位：条。 |
| Unknown | Long | 0 | 解析异常的SQL数量，单位：条。 |
| CheckNotPass | Long | 1 | 检测不通过的SQL数量，单位：条。 |
| CheckPass | Long | 8 | 检测通过的SQL数量，单位：条。 |

数据管理

| ForcePass | Long | 1 | 人工通过的SQL数量，单位：条。 |
|---|---|---|---|
| ForceNotPass | Long | 0 | 人工不通过的SQL数量，单位：条。 |
| SQLReviewRes ult | Object |  | SQL审核优化建议。 |
| MustImprove | Long | 1 | 必须改进的SQL数量，单位：条。 |
| PotentialIssue | Long | 0 | 潜在问题的SQL数量，单位：条。 |
| SuggestImpro ve | Long | 3 | 建议改进的SQL数量，单位：条。 |
| UseDmsToolkit | Long | 0 | 推荐使用无锁结构变更的SQL数量，单位：条。 |
| UseDmsDmlUn lock | Long | 0 | 推荐使用无锁数据变更的SQL数量，单位：条。 |
| TableIndexSug gest | Long | 2 | 索引推荐的SQL数量，单位：条。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetSQLReviewCheckResultStatus &OrderId=123321 &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>E1ABE358-14A0-4DFA-9776-1A3CB59192DF</RequestId>
    <CheckResultStatus>
        <SQLReviewResult>
            <TableIndexSuggest>1</TableIndexSuggest>
            <MustImprove>1</MustImprove>
            <SuggestImprove>1</SuggestImprove>
            <PotentialIssue>2</PotentialIssue>
        </SQLReviewResult>
        <TotalSQLCount>4</TotalSQLCount>
        <CheckedCount>4</CheckedCount>
        <CheckStatusResult>
            <CheckNotPass>1</CheckNotPass>
            <CheckPass>3</CheckPass>
        </CheckStatusResult>
    </CheckResultStatus>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "E1ABE358-14A0-4DFA-9776-1A3CB59192DF",
  "CheckResultStatus" : {
    "SQLReviewResult" : {
      "TableIndexSuggest" : 1,
      "MustImprove" : 1,
      "SuggestImprove" : 1,
      "PotentialIssue" : 2
    },
    "TotalSQLCount" : 4,
    "CheckedCount" : 4,
    "CheckStatusResult" : {
      "CheckNotPass" : 1,
      "CheckPass" : 3
    }
  },
  "Success" : true
}
```

##### CreateSQLReviewOrder

**请求参数**

数据管理

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateSQLRevie wOrder | 系统规定的参数。取值：CreateSQLReviewOrder。 |
| Comment | String | 是 | test | 业务背景，描述任务的原因或目标，以减少沟通成本。 |
| RelatedUserList | Array of Long | 否 | 123443 | 相关人ID。 |
| Param | Object | 是 |  | 工单参数。 |
| ProjectName | String | 是 | xxx业务SQL审核 | 项目名称。 |
| DbId | Long | 是 | 123321 | 数据库ID，可调用SearchDatabase接口获取。 说明当前仅支持物理库，暂不支持逻辑库。 |
| AttachmentKeyL ist | Array of String | 是 | upload xxxx.sql _ | 附件Key，支持添加多个附件，您可以调用GetUserUploadFileJob接口获取该参数。 说明仅支持iBatis框架或 MyBatis框架的.xml文件与.sql格式的SQL文件。 |
| Tid | Long | 否 | 1 | 租户ID。您可以调用GetUserActiveTenant或ListUserTen ants接口获取该参数。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

数据管理

| ErrorMessage | String | UnknownError | 错误信息。 |
|---|---|---|---|
| ErrorCode | String | 200 | 错误码。 |
| CreateOrderRe sult | Array of Long | 1423532 | 工单号。 |

**示例**

请求示例

```json
http(s)://dms-enterprise.aliyuncs.com/?Action=CreateSQLReviewOrder &Comment=test &RelatedUserList=[123443] &Param={"ProjectName":"xxx业务SQL审核","DbId":123321,"AttachmentKeyList": ["upload_xxxx.sql"]} &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId>
    <Success>true</Success>
    <ErrorMessage>UnknownError</ErrorMessage>
    <ErrorCode>UnknownError</ErrorCode>
    <CreateOrderResult>1423532</CreateOrderResult>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
  "Success" : true,
  "ErrorMessage" : "UnknownError",
  "ErrorCode" : "UnknownError",
}
```

##### ListSQLReviewOriginSQL

调用ListSQLReviewOriginSQL接口，获取SQL审核工单的SQL详情结果。 数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListSQLReviewO riginSQL | 系统规定参数。取值：ListSQLReviewOriginSQL。 |
| OrderId | Long | 是 | 123321 | 工单号。您可以调用CreateSQLReviewOrder接口获取该参数。 |
| OrderActionDeta il | Object | 否 |  | 工单参数（过滤条件）。 |
| FileId | Long | 否 | 123345 | 审核文件ID。 |
| SQLReviewResul t | String | 否 | MUST IMPROVE _ | SQL审核优化建议。取值如下： MUST IMPROVE：必须改进。 _ POTENTIAL ISSUE：潜在问题。 _ SUGGEST IMPROVE：建议改进。 _ USE DMS TOOLKIT：使用无锁结构 _ _ 变更。 USE DMS DML UNLOCK：使用无 _ _ _ 锁数据变更。 TABLE INDEX SUGGEST：索引推 _ _ 荐。 |
| CheckStatusRes ult | String | 否 | check not pass _ _ | 检测结果。取值如下： new：等待分析 unknown：解析异常 check not pass：检测不通过 _ _ check pass：检测通过 _ force pass：人工通过 _ force not pass：人工不通过 _ _ |
| Page | Object | 否 |  | 分页参数。 |
| PageNumber | Integer | 否 | 1 | 第几页。 |
| PageSize | Integer | 否 | 20 | 每页数据量。 |
| Tid | Long | 否 | 1 | 租户ID。您可以调用GetUserActiveTenant或ListUserTen ants接口获取该参数。 |

数据管理

| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Integer | 10 | 总SQL条数。 |
| OriginSQLList | Array of OriginSQLList |  | 解析的SQL列表。 |
| SQLId | Long | 1111 | SQL语句ID。 |
| FileId | Long | 123321 | 文件ID。 |
| FileName | String | test.sql | 文件名。 |
| SQLContent | String | select id from table name _ | SQL内容。 |
| CheckStatus | String | check pass _ | 检测结果。返回值如下： new：等待分析。 unknown：解析异常。 check not pass：检测不通过。 _ _ check pass：检测通过。 _ force pass：人工通过。 _ force not pass：人工不通过。 _ _ |
| StatusDesc | String | 检测通过 | 检测结果描述。 |
| CheckedTime | String | 2021-06-09 21:07:00 | 检测时间。 |

数据管理

| SqlHash | String | 95adb6e77a0884d 9e50232cb8c5c96 9d | SQL内容的MD5值。 |
|---|---|---|---|
| ReviewSumma ry | String | {"POTENTIAL ISSU _ E":1,"SUGGEST IM _ PROVE":1} | SQL审核优化建议的统计信息（JSON字符串）。 统计信息如下： MUST IMPROVE：必须改进。 _ POTENTIAL ISSUE：潜在问题。 _ SUGGEST IMPROVE：建议改进。 _ USEDMSTOOLKIT：使用无锁结构变更。 USEDMSDML UNLOCK：使用无锁数据 _ 变更。 TABLEINDEXSUGGEST：索引推荐。 |
| SQLReviewQu eryKey | String | a57e54ec5433475 ea3082d882fdb89c 5 | SQL审核优化建议详情信息的查询KEY。 |

**示例**

请求示例

```json
http(s)://dms-enterprise.aliyuncs.com/?Action=ListSQLReviewOriginSQL &OrderId=123321 &OrderActionDetail= {"FileId":123345,"SQLReviewResult":"MUST_IMPROVE","CheckStatusResult":"check_not_pass","P e":{"PageNumber":1,"PageSize":20}} &Tid=1
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId>
    <ErrorCode>UnknownError</ErrorCode>
    <ErrorMessage>UnknownError</ErrorMessage>
    <Success>true</Success>
    <TotalCount>10</TotalCount>
    <OriginSQLList>
        <SQLId>1111</SQLId>
        <FileId>123321</FileId>
        <FileName>test.sql</FileName>
        <SQLContent>select id from table_name</SQLContent>
        <CheckStatus>check_pass</CheckStatus>
        <StatusDesc>检测通过</StatusDesc>
        <CheckedTime>2021-06-09 21:07:00</CheckedTime>
        <SqlHash>95adb6e77a0884d9e50232cb8c5c969d</SqlHash>
        <ReviewSummary>{"POTENTIAL_ISSUE":1,"SUGGEST_IMPROVE":1}</ReviewSummary>
        <SQLReviewQueryKey>a57e54ec5433475ea3082d882fdb89c5</SQLReviewQueryKey>
    </OriginSQLList>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
  "ErrorCode" : "UnknownError",
  "ErrorMessage" : "UnknownError",
  "Success" : true,
  "TotalCount" : 10,
  "OriginSQLList" : [ {
    "SQLId" : 1111,
    "FileId" : 123321,
    "FileName" : "test.sql",
    "SQLContent" : "select id from table_name",
    "CheckStatus" : "check_pass",
```

`"StatusDesc" : "`检测通过`",`

```json
    "CheckedTime" : "2021-06-09 21:07:00",
    "SqlHash" : "95adb6e77a0884d9e50232cb8c5c969d",
    "ReviewSummary" : "{\"POTENTIAL_ISSUE\":1,\"SUGGEST_IMPROVE\":1}",
    "SQLReviewQueryKey" : "a57e54ec5433475ea3082d882fdb89c5"
  } ]
}
```

#### 附件上传

数据管理

##### CreateUploadOSSFileJob

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| FileSource | String | 是 | datacorrect | 上传附件的使用目的，取值和说明如下： datacorrect：数据变更工单 order info attachment：工单附 _ _ 件 big-file：批量数据导入 sqlreview：SQL审核 |
| FileName | String | 是 | test.sql | 文件名。 说明需要以TXT、SQL格式结尾，例如test.txt文件。 |
| UploadTarget | Object | 是 |  | OSS信息。 |
| Endpoint | String | 是 | http://oss-cn- hangzhou.aliyun cs.com | OSS的连接地址。 |
| BucketName | String | 是 | test bucket _ | OSS Bucket唯一标识。 |
| ObjectName | String | 是 | test.sql | OSS对象名称。 |
| Tid | Long | 否 | -1 | 租户ID。 说明鼠标移动到界面右上角的头像处，查看租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4E1D2B4D-3E53- 4ABC-999D- 1D2520B3471A | 请求ID。 |

数据管理

| Success | Boolean | true | 请求是否成功。 |
|---|---|---|---|
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| JobKey | String | 65254a4c1614235 217749100e | 上传附件任务Key，可查询附件上传进展与任务详情，详情请参见GetUserUploadFileJob。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?FileSource=datacorrect &FileName=test.sql &UploadType=OSS &UploadTarget={"Endpoint":"http://oss-cnhangzhou.aliyuncs.com","BucketName":"test_bucket","ObjectName":"test.sql"} &Tid=-1
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <JobKey>7000005000007000009000000</JobKey>
    <RequestId>44355324-9534-4AF4-B7AA-8EDE3C767889</RequestId>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "JobKey" : "7000005000007000009000000",
  "RequestId" : "44355324-9534-4AF4-B7AA-8EDE3C767889",
  "Success" : true
}
```

##### GetUserUploadFileJob

数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| JobKey | String | 是 | 65254a49100e | 上传附件任务JobKey，您可以通过调用CreateUploadFileJob、CreateUploa dOSSFileJob接口获取该参数。 |
| Tid | Long | 否 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | BDEFE9F2-B3B4- 42D0-83AE- ECF9FC067DCD | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| UploadFileJob Detail | object |  | 上传附件任务详情。 |
| JobKey | String | 65254a4c1614235 217749100e | 上传附件任务JobKey。 |
| FileName | String | test.sql | 文件名。 |
| FileSize | Long | 2968269 | 文件大小，单位：字节。 |
| FileSource | String | datacorrect | 文件上传的使用目的，取值： datacorrect：数据变更工单 order info attachment：工单附件 _ _ big-file：批量数据导入 sqlreview：SQL审核 |

数据管理

| UploadType | String | URL | 上传附件任务类型，取值： URL OSS |
|---|---|---|---|
| UploadURL | String | http://xxxx/test.sql | 上传附件URL链接。 说明当UploadType参数为URL时显示。 |
| UploadOSSPar am | object |  | 上传附件OSS信息。 说明当UploadType参数为OSS时显示。 |
| Endpoint | String | http://oss-cn- hangzhou.aliyuncs. com | OSS的连接地址。 |
| BucketName | String | test bucket _ | OSS Bucket唯一标识。 |
| ObjectName | String | test.sql | OSS对象名称。 |
| UploadedSize | Long | 2968269 | 已上传的大小，单位为字节。 |
| JobStatus | String | SUCCESS | 上传附件任务状态，取值： INIT：初始化状态 PENDING：等待任务抓取 BE SCHEDULED：待调度 _ FAIL：执行失败 SUCCESS：执行成功 RUNNING：正在执行 |
| JobStatusDesc | String | success | 任务状态描述。 |
| AttachmentKe y | String | upload 3c7edea3- _ e4c3-4403-857d- 737043036f69 test _ .sql | 上传附件成功后返回的附件Key，可在创建工单时使用。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetUserUploadFileJob &Tid=-1
```

&公共请求参数数据管理正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>22FFF57C-6E85-4C3D-90AF-C1BFE79E1FAF</RequestId>
    <UploadFileJobDetail>
        <JobStatus>INIT</JobStatus>
        <JobKey>7000005000007000009000000</JobKey>
        <UploadURL>https://dbxxx.oss-cn-hangzhou.aliyuncs.com/dm/1.txt</UploadURL>
        <UploadedSize>0</UploadedSize>
        <JobStatusDesc/>
        <FileSource>datacorrect</FileSource>
        <FileName>1.txt</FileName>
        <UploadType>URL</UploadType>
        <FileSize>-1</FileSize>
    </UploadFileJobDetail>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "22FFF57C-6E85-4C3D-90AF-C1BFE79E1FAF",
  "UploadFileJobDetail" : {
    "JobStatus" : "INIT",
    "JobKey" : "7000005000007000009000000",
    "UploadURL" : "https://dbxxx.oss-cn-hangzhou.aliyuncs.com/dm/1.txt",
    "UploadedSize" : 0,
    "JobStatusDesc" : "",
    "FileSource" : "datacorrect",
    "FileName" : "1.txt",
    "UploadType" : "URL",
    "FileSize" : -1
  },
  "Success" : true
}
```

##### CreateUploadFileJob

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据管理

| Action | String | 是 | CreateUploadFil eJob | 系统规定参数。取值：CreateUploadFileJob。 |
|---|---|---|---|---|
| FileSource | String | 是 | datacorrect | 上传附件的使用目的，取值： datacorrect：数据变更工单。 order info attachment：工单附 _ _ 件。 big-file：批量数据导入。 sqlreview：SQL审核。 |
| FileName | String | 是 | test.txt | 文件名称。 说明文件名称需要以.txt 或.sql结尾。例如test.txt、 test.sql。 |
| UploadURL | String | 是 | https://XXX.oss- cn- hangzhou.aliyun cs.com/test.txt | 上传附件URL链接，此处链接仅支持HTTP 和HTTPS链接。 说明您可以将文件 （Object）上传至存储空间 （Bucket）后，获取文件的分享 URL。 |
| Tid | Long | 否 | 3*** | 租户ID。 说明您可以通过调用GetUserActiveTenant接口获取该参数。 |
| RegionId | String | 否 | cn-hangzhou | DMS服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | E103C5F9-DE47- 53F2-BF34- D71DF38F**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值说明如下： true：请求成功。 false：请求失败。 |

数据管理

| ErrorMessage | String | Unsupported url scheme : null, scheme must be https or http | 错误信息。 |
|---|---|---|---|
| ErrorCode | String | InvalidParameterV alid | 错误码。 |
| JobKey | String | 761f18031635736 380812**** | 上传附件任务值。 说明您可以通过调用GetUserUploadFileJob接口查询附件上传的进展与任务详情。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=CreateUploadFileJob &FileName=test.txt &UploadType=URL &UploadURL=https://XXX.oss-cn-hangzhou.aliyuncs.com/test.txt &Tid=3***
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <JobKey>761f18031635736380812****</JobKey>
    <RequestId>E103C5F9-DE47-53F2-BF34-D71DF38F****</RequestId>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "JobKey" : "761f18031635736380812****",
  "RequestId" : "E103C5F9-DE47-53F2-BF34-D71DF38F****",
  "Success" : true
}
```

#### 权限申请

数据管理

##### GetOwnerApplyOrderDetail

调用GetOwnerApplyOrderDetail接口获取申请库Owner、表Owner、实例Owner的工单详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 730000 | 工单号。 |
| Tid | Long | 否 | 3*** | 租户ID。 说明鼠标移动到界面右上角的头像处，查看租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CB784055-E8CB- 4461-AB0B- 483A1DA32BB5 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| OwnerApplyOr derDetail | object |  | 工单详情。 |
| ApplyType | String | DB | 申请类型，取值： INSTANCE：实例Owner DB：库Owner TABLE：表Owner |
| Resources | Array of Resource |  | 申请资源详情。 |

数据管理

| Logic | Boolean | true | 是否为逻辑库，取值： true：是 false：否 |
|---|---|---|---|
| TargetId | String | 12345 | 资源ID。 |
| ResourceDetai l | object |  | 资源详情。 |
| SearchName | String | yuyang【test】 | 资源搜索名。 |
| DbType | String | MYSQL | 数据库类型。 |
| EnvType | String | PRODUCT | 实例的环境类型。 |
| TableName | String | test | 表名。 说明申请表Owner时，将返回此参数。 |
| OwnerIds | Array of Long | 132453 | Owner ID。 |
| OwnerNickNa mes | Array of String | test user _ | Owner昵称。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?OrderId=730000 &Tid=3***
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <OwnerApplyOrderDetail>
    <ApplyType>DB</ApplyType>
    <Resources>
        <ResourceDetail>
            <SearchName>gp_toolkit@gp-
bp18anxxxxxxxt48z.gpdb.rds.aliyuncs.com:3432</SearchName>
            <OwnerNickNames>gctest</OwnerNickNames>
            <EnvType>PRODUCT</EnvType>
            <DbType>ADB_POSTGRESQL</DbType>
            <OwnerIds>128000</OwnerIds>
        </ResourceDetail>
        <Logic>false</Logic>
        <TargetId>116000</TargetId>
    </Resources>
    </OwnerApplyOrderDetail>
    <RequestId>6976762B-AEA4-4EF0-9C42-46EC5477D780</RequestId>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "OwnerApplyOrderDetail" : {
    "ApplyType" : "DB",
    "Resources" : [ {
      "ResourceDetail" : {
        "SearchName" : "gp_toolkit@gp-bp18anxxxxxxxt48z.gpdb.rds.aliyuncs.com:3432",
        "OwnerNickNames" : [ "gctest" ],
        "EnvType" : "PRODUCT",
        "DbType" : "ADB_POSTGRESQL",
        "OwnerIds" : [ 128000 ]
      },
      "Logic" : false,
      "TargetId" : 116000
    } ]
  },
  "RequestId" : "6976762B-AEA4-4EF0-9C42-46EC5477D780",
  "Success" : true
}
```

##### GetPermApplyOrderDetail

本接口可以获取：**库权限**、**表权限**、**敏感列权限**。 数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| OrderId | Long | 是 | 730000 | 工单号。 |
| Tid | Long | 否 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A4C4499E-5AC2- 4318-9FCF- 03E426781A04 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| PermApplyOrd erDetail | object |  | 权限申请详情。 |
| Resources | Array of Resource |  | 资源详情列表。 |
| DatabaseInfo | object |  | 库信息。 |
| DbId | Long | 12345 | 库ID。 |
| Logic | Boolean | false | 是否逻辑库，取值： true：是 false：否 |
| DbType | String | MySQL | 数据库类型。 |
| SearchName | String | test@xxxx:3306【t est】 | 库搜索名。 |

数据管理

| OwnerIds | Array of Long | 123** | Owner ID。 |
|---|---|---|---|
| OwnerNickNa mes | Array of String | test user _ | Owner昵称。 |
| EnvType | String | product | 实例的环境类型。 |
| TableInfo | object |  | 表信息。 |
| TableName | String | test tb _ | 表名。 |
| ColumnInfo | object |  | 字段信息。 |
| TableName | String | test tb _ | 表名。 |
| ColumnName | String | test col _ | 字段名。 |
| InstanceInfo | object |  | 实例信息。 |
| InstanceId | String | 123** | 实例ID。 |
| SearchName | String | xxxx:3306 | 搜索名。 |
| DbType | String | MySQL | 数据库类型。 |
| EnvType | String | product | 实例的环境类型。 |
| Host | String | xxxx | 连接地址。 |
| Port | Long | 3306 | 连接端口。 |
| OwnerIds | Array of Long | 12345 | Owner ID。 |
| OwnerNickNa me | Array of String | test owner _ | Owner昵称。 |
| DbaId | Long | 12345 | 实例DBA的ID。 |
| DbaNickName | String | test dba _ | 实例DBA昵称。 |

数据管理

| PermType | Long | 7 | 权限类型，取值： 1：查询 2：导出 3：查询+导出 4：变更 5：查询+变更 6：导出+变更 7：查询+导出+变更 |
|---|---|---|---|
| Seconds | Long | 3600 | 权限时长，单位：秒。 |
| ApplyType | String | DB | 申请权限类型，取值和说明如下： DB：库权限 TAB：表权限 COL：列权限 INSTANT：实例权限 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetPermApplyOrderDetail &Tid=-1
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <PermApplyOrderDetail>
        <ApplyType>DB</ApplyType>
        <PermType>1</PermType>
        <Seconds>2592000</Seconds>
        <Resources>
            <DatabaseInfo>
                <SearchName>rds_db@rm-
bpxxxxxxxxffxxxxxxi.mysql.rds.aliyuncs.com:3306</SearchName>
                <OwnerNickNames>gctest</OwnerNickNames>
                <DbId>1250000</DbId>
                <Logic>false</Logic>
                <EnvType>dev</EnvType>
                <DbType>mysql</DbType>
                <OwnerIds>120000</OwnerIds>
            </DatabaseInfo>
            <ColumnInfo/>
            <TableInfo/>
            <InstanceInfo/>
        </Resources>
    </PermApplyOrderDetail>
    <RequestId>806FBC5B-2AED-401C-9E00-0B91C1DB2F1A</RequestId>
    <Success>true</Success>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "PermApplyOrderDetail" : {
    "ApplyType" : "DB",
    "PermType" : 1,
    "Seconds" : 2592000,
    "Resources" : [ {
      "DatabaseInfo" : {
        "SearchName" : "rds_db@rm-bpxxxxxxxxffxxxxxxi.mysql.rds.aliyuncs.com:3306",
        "OwnerNickNames" : [ "gctest" ],
        "DbId" : 1250000,
        "Logic" : false,
        "EnvType" : "dev",
        "DbType" : "mysql",
        "OwnerIds" : [ 120000 ]
      },
      "ColumnInfo" : { },
      "TableInfo" : { },
      "InstanceInfo" : { }
    } ]
  },
  "RequestId" : "806FBC5B-2AED-401C-9E00-0B91C1DB2F1A",
  "Success" : true
}
```

### SQL任务

#### ListDBTaskSQLJob

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDBTaskSQLJo b | 系统规定参数。取值：ListDBTaskSQLJob。 |
| DBTaskGroupId | Long | 是 | 132**** | SQL任务分组ID，您可以调用GetStructSyncJobDetail接口获取该参数。 |
| PageNumber | Long | 否 | 1 | 开始页码。 |
| PageSize | Long | 否 | 20 | 每页数据量。 |

数据管理

| Tid | Long | 否 | 1*** | 租户ID。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | DMS服务地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | F6C47680-8D2D- 43A4-8902- F2740D71A398 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| DBTaskSQLJob List | Array of DBTaskSQLJob |  | SQL任务列表。 |
| JobId | Long | 12**** | SQL任务ID。 |
| JobType | String | STRUCT SYNC _ | SQL任务类型。 |
| Comment | String | test | SQL任务备注信息。 |
| DbSearchNam e | String | test@xxx:3306【te st】 | 库搜索名。 |
| DbId | Long | 43214523 | 库ID。 |
| Logic | Boolean | false | 是否为逻辑库，取值： true：是 false：否 |
| CreateTime | String | 2021-02-18 17:49:20 | 创建时间。 |
| LastExecTime | String | 2021-02-18 17:49:31 | 最后执行时间。 |
| DbTaskGroupI d | Long | 432**** | SQL任务分组ID。 |

数据管理

| Status | String | SUCCESS | SQL详情状态，取值： INIT：初始化状态 PENDING：等待任务抓取 BE SCHEDULED：待调度 _ FAIL：执行失败 SUCCESS：执行成功 PAUSE：暂停 DELETE：删除 RUNNING：正在执行 |
|---|---|---|---|
| Transactional | Boolean | false | 是否以事务方式执行，取值： true：是 false：否 |
| TotalCount | Long | 1 | SQL任务列表总数。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=ListDBTaskSQLJob &PageNumber=1 &PageSize=20
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F6C47680-8D2D-43A4-8902-F2740D71A398</RequestId>
    <Success>true</Success>
    <ErrorMessage>UnknownError</ErrorMessage>
    <ErrorCode>UnknownError</ErrorCode>
    <DBTaskSQLJobList>
        <JobType>STRUCT_SYNC</JobType>
        <Comment>test</Comment>
        <DbSearchName>test@xxx:3306【test】</DbSearchName>
        <DbId>43214523</DbId>
        <Logic>false</Logic>
        <CreateTime>2021-02-18 17:49:20</CreateTime>
        <LastExecTime>2021-02-18 17:49:31</LastExecTime>
        <Status>SUCCESS</Status>
        <Transactional>false</Transactional>
    </DBTaskSQLJobList>
    <TotalCount>1</TotalCount>
```

数据管理 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "F6C47680-8D2D-43A4-8902-F2740D71A398",
  "Success" : true,
  "ErrorMessage" : "UnknownError",
  "ErrorCode" : "UnknownError",
  "DBTaskSQLJobList" : [ {
    "JobType" : "STRUCT_SYNC",
    "Comment" : "test",
    "DbSearchName" : "test@xxx:3306【test】",
    "DbId" : 43214523,
    "Logic" : false,
    "CreateTime" : "2021-02-18 17:49:20",
    "LastExecTime" : "2021-02-18 17:49:31",
    "Status" : "SUCCESS",
    "Transactional" : false
  } ],
  "TotalCount" : 1
}
```

#### ListDBTaskSQLJobDetail

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDBTaskSQLJo bDetail | 系统规定参数。取值：ListDBTaskSQLJobDetail。 |
| JobId | Long | 是 | 1276**** | SQL任务ID，可通过调用接口ListDBTaskSQLJob获取该参数的值。 |
| PageNumber | Long | 否 | 1 | 开始页码。 |
| PageSize | Long | 否 | 20 | 每页数据量。 |
| Tid | Long | 否 | 3*** | 租户ID，可通过调用接口GetUserActiveTenant获取该参数的值。 |
| RegionId | String | 否 | cn-hangzhou | DMS服务地域。 |

数据管理

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 3F044E33-FE09- 58F1-8C61- A0F612EC**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值： true：请求成功 false：请求失败 |
| ErrorMessage | String | JobId is mandatory for this action. | 错误信息。 |
| ErrorCode | String | MissingJobId | 错误码。 |
| DBTaskSQLJob DetailList | Array of DBTaskSQLJob Detail |  | SQL任务详情列表。 |
| JobDetailId | Long | 24723**** | SQL任务详情ID。 |
| CurrentSql | String | update a set id = 1 where id = 1; | 当前执行的SQL。 |
| ExecuteCount | Long | 1 | 执行次数。 |
| JobId | Long | 1276**** | SQL任务ID。 |
| DbId | Long | 1988**** | 物理库ID。 |
| Logic | Boolean | false | 是否为逻辑库，返回值如下： true：逻辑库 false：物理库 |
| Skip | Boolean | false | 是否存在跳过执行SQL脚本的情况，返回值如下： true：存在 false：不存在 |
| SqlType | String | CREATE TABLE _ | SQL类型，例如，DELETE、UPDATE、 ALTER TABLE等。 _ |

数据管理

| Status | String | SUCCESS | SQL详情状态，返回值如下： INIT：初始化状态 PENDING：等待任务抓取 BE SCHEDULED：待调度 _ FAIL：执行失败 SUCCESS：执行成功 PAUSE：暂停 DELETE：删除 RUNNING：正在执行 |
|---|---|---|---|
| Log | String | log info _ | 日志详情信息。 |
| StartTime | String | 2021-12-16 00:00:00 | SQL执行开始时间。 |
| EndTime | String | 2021-12-16 00:00:01 | SQL执行结束时间。 |
| TimeDelay | Long | 38 | SQL执行耗时，单位为毫秒。 |
| AffectRows | Long | 0 | SQL执行影响行数。 |
| TotalCount | Long | 1 | SQL任务总数。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=ListDBTaskSQLJobDetail &JobId=1276**** &PageNumber=1 &PageSize=20 &Tid=3***
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>3F044E33-FE09-58F1-8C61-A0F612EC****</RequestId>
    <Success>true</Success>
    <ErrorMessage>JobId is mandatory for this action.</ErrorMessage>
    <ErrorCode>MissingJobId</ErrorCode>
    <DBTaskSQLJobDetailList>
        <CurrentSql>update a set id = 1 where id  = 1;</CurrentSql>
        <ExecuteCount>1</ExecuteCount>
        <Logic>false</Logic>
        <Skip>false</Skip>
        <SqlType>CREATE_TABLE</SqlType>
        <Status>SUCCESS</Status>
        <Log>log_info</Log>
        <StartTime>2021-12-16 00:00:00</StartTime>
        <EndTime>2021-12-16 00:00:01</EndTime>
        <TimeDelay>38</TimeDelay>
        <AffectRows>0</AffectRows>
    </DBTaskSQLJobDetailList>
    <TotalCount>1</TotalCount>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "3F044E33-FE09-58F1-8C61-A0F612EC****",
  "Success" : true,
  "ErrorMessage" : "JobId is mandatory for this action.",
  "ErrorCode" : "MissingJobId",
  "DBTaskSQLJobDetailList" : [ {
    "CurrentSql" : "update a set id = 1 where id  = 1;",
    "ExecuteCount" : 1,
    "Logic" : false,
    "Skip" : false,
    "SqlType" : "CREATE_TABLE",
    "Status" : "SUCCESS",
    "Log" : "log_info",
    "StartTime" : "2021-12-16 00:00:00",
    "EndTime" : "2021-12-16 00:00:01",
    "TimeDelay" : 38,
    "AffectRows" : 0
  } ],
  "TotalCount" : 1
}
```

### 权限管理

数据管理

#### RevokeUserPermission

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RevokeUserPer mission | 系统规定参数，取值：RevokeUserPermission。 |
| DbId | String | 是 | 142345 | 数据库ID。 |
| DsType | String | 是 | DATABASE | 资源类型，取值和说明请参考GrantUserPermission接口。 |
| PermTypes | String | 是 | QUERY | 权限类型，取值和说明请参考GrantUserPermission接口。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| UserAccessId | String | 是 | 123 | 用户权限信息ID。 |
| UserId | String | 是 | 1234 | 用户ID，对应GetUser里面的用户ID。 说明注意不是用户的阿里云 UID。 |
| Logic | Boolean | 否 | false | 是否为逻辑库，取值： true false |
| TableId | String | 否 | 1342345 | 表ID，授权表权限时需要指定。 |
| TableName | String | 否 | table name _ | 表名，授权表权限时需要指定。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |

数据管理

| ErrorMessage | String | UnknownError | 错误消息。 |
|---|---|---|---|
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RevokeUserPermission
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
}
```

#### ListDatabaseUserPermssions

调用ListDatabaseUserPermssions接口获取具备指定数据库的用户权限详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDatabaseUse rPermssions | 要执行的操作，取值：ListDatabaseUserPermssions 。 |
| DbId | String | 是 | 123 | 数据库ID。 |
| PermType | String | 是 | DATABASE | 权限类型，取值和说明如下： DATABASE： 库权限 TABLE：表权限 COLUMN：列权限 |

数据管理

| Tid | Long | 是 | -1 | 租户ID。 |
|---|---|---|---|---|
| Logic | Boolean | 否 | false | 是否逻辑库。 |
| UserName | String | 否 | search user na _ _ me | 用户昵称。 |
| PageNumber | Integer | 否 | 1 | 第几页。 |
| PageSize | Integer | 否 | 10 | 每页数据量。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 68075D06-7406- 4887-83A7- F558A4D28C13 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 1 | 满足条件的记录总数。 |
| UserPermissio ns | Array of UserPermissio n |  | 用户权限详情。 |
| UserPermissio n |  |  |  |
| Alias | String | instance alias _ | 实例别名。 |
| ColumnName | String | column name _ | 字段名。 |
| DbId | String | 1234 | 数据库ID。 |
| DbType | String | mysql | 数据库类型。 |

数据管理

| DsType | String | DATABASE | 资源权限类型。 |
|---|---|---|---|
| EnvType | String | product | 数据库所属环境。 |
| InstanceId | String | 1443 | 实例ID。 |
| Logic | Boolean | false | 是否逻辑库。 |
| PermDetails | Array of PermDetail |  | 用户权限详情。 |
| PermDetail |  |  |  |
| CreateDate | String | 2019-12-12 00:00:00 | 权限创建时间。 |
| ExpireDate | String | 2020-12-12 00:00:00 | 权限过期时间。 |
| ExtraData | String | DEFAULT | 附加信息，预留属性。 |
| OriginFrom | String | xxx grant | 权限申请来源描述。 |
| PermType | String | QUERY | 权限类型，取值和说明如下： QUERY：查询 EXPORT：导出 CORRECT：变更 |
| UserAccessId | String | 13434 | 权限记录ID。 |
| SchemaName | String | xxx@xxxx:3306 | Schema名称。 |
| SearchName | String | xxx | 数据库搜索名。 |
| TableId | String | 42345 | 表ID。 |
| TableName | String | table name _ | 表名。 |
| UserId | String | 14324 | 用户ID。 |
| UserNickName | String | user nick name _ _ | 用户名称。 |

**示例**

数据管理请求示例

```
http(s)://[Endpoint]/?Action=ListDatabaseUserPermssions &DbId=123 &PermType=DATABASE &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<UserPermissions>
    <UserPermission>
        <Logic>false</Logic>
        <UserNickName>xxx</UserNickName>
        <DsType>DATABASE</DsType>
        <Alias>beihe_ent_prod</Alias>
        <PermDetails>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390915</UserAccessId>
                <PermType>QUERY</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390916</UserAccessId>
                <PermType>EXPORT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390917</UserAccessId>
                <PermType>CORRECT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
        </PermDetails>
        <InstanceId>1434</InstanceId>
        <SearchName>xxx@xxxx:3306</SearchName>
        <DbId>123434</DbId>
        <UserId>432423</UserId>
        <DbType>drds</DbType>
        <EnvType>product</EnvType>
        <SchemaName>xxx</SchemaName>
    </UserPermission>
</UserPermissions> <TotalCount>1</TotalCount> <RequestId>68075D06-7406-4887-83A7-F558A4D28C13</RequestId> <Success>true</Success>
```

数据管理 `JSON` 格式

```json
{
  "UserPermissions": {
    "UserPermission": [
      {
        "Logic": false,
        "UserNickName": "xxx",
        "DsType": "DATABASE",
        "Alias": "beihe_ent_prod",
        "PermDetails": {
          "PermDetail": [
            {
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390915",
              "PermType": "QUERY",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
            },
            {
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390916",
              "PermType": "EXPORT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
            },
            {
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390917",
              "PermType": "CORRECT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
            }
```

]

```json
        },
        "InstanceId": 1434,
        "SearchName": "xxx@xxxx:3306",
        "DbId": 123434,
        "UserId": 432423,
        "DbType": "drds",
        "EnvType": "product",
        "SchemaName": "xxx"
      }
```

]

```json
  },
  "TotalCount": 1,
  "RequestId": "68075D06-7406-4887-83A7-F558A4D28C13",
  "Success": true
}
```

#### SetOwners

数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetOwners | 系统规定参数，取值：SetOwners。 |
| OwnerIds | String | 是 | 123, 456 | 设置为Owner的用户ID，多个用户ID用逗号分开。 |
| OwnerType | String | 是 | DATABASE | Owner类型，取值和说明如下： DATABASE：物理库Owner LOGIC DATABASE：逻辑库Owner _ TABLE：物理表Owner LOGIC TABLE：逻辑表Owner _ |
| ResourceId | String | 是 | 123 | 资源ID，根据OwnerType的不同，指向不同的资源，OwnerType和对应资源ID 的解释如下： DATABASE： 物理库ID LOGIC DATABASE：逻辑库ID _ TABLE：物理表ID LOGIC TABLE：逻辑表ID _ |
| Tid | Long | 是 | -1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误消息。 |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例数据管理

```
&OwnerIds=123, 456 &OwnerType=DATABASE &ResourceId=123 &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
}
```

#### ListUserPermissions

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListUserPermissi ons | 要执行的操作，取值：ListUserPermissions。 |
| PermType | String | 是 | DATABASE | 资源权限类型，取值和说明请参考ListDatabaseUserPermssions。 |
| Tid | Long | 是 | -1 | 租户ID。 |
| UserId | String | 是 | 13435 | 用户ID，对应GetUser里面的用户ID，注意不是用户的阿里云UID。 |
| DatabaseName | String | 否 | db name _ | 数据库名。 |
| Logic | Boolean | 否 | false | 是否逻辑库，取值： true false |

数据管理

| EnvType | String | 否 | dev | 数据库所属环境类型。 |
|---|---|---|---|---|
| DbType | String | 否 | MySQL | 数据库类型。 |
| PageNumber | Integer | 否 | 1 | 页码。 |
| PageSize | Integer | 否 | 1 | 每页记录数。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | C51420E3-144A- 4A94-B473- 8662FCF4AD10 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 6 | 满足条件记录总数。 |
| UserPermissio ns | Array of UserPermissio n |  | 用户权限信息列表。 |
| UserPermissio n |  |  |  |
| Alias | String | instance alias _ | 实例别名。 |
| ColumnName | String | column name _ | 字段名。 |
| DbId | String | 1324 | 数据库ID。 |
| DbType | String | mysql | 数据库类型。 |
| DsType | String | DATABASE | 权限资源类型。 |

数据管理

| EnvType | String | dev | 数据库所属环境类型。 |
|---|---|---|---|
| InstanceId | String | 134 | 实例ID。 |
| Logic | Boolean | false | 是否逻辑库，取值： true false |
| PermDetails | Array of PermDetail |  | 权限详情。 |
| PermDetail |  |  |  |
| CreateDate | String | 2019-12-12 00:00:00 | 权限授予时间 |
| ExpireDate | String | 2020-12-12 00:00:00 | 授权到期时间 |
| ExtraData | String | xxx | 额外数据，预留参数 |
| OriginFrom | String | xxx | 权限授予来源信息 |
| PermType | String | QUERY | 权限类型 |
| UserAccessId | String | 1345 | 授权记录ID |
| SchemaName | String | test db _ | 数据库名。 |
| SearchName | String | test db@xxx:3306 _ | 库搜索名。 |
| TableId | String | 13434 | 表ID。 |
| TableName | String | test table _ | 表名。 |
| UserId | String | 423245 | 用户ID。 |
| UserNickName | String | nick name _ | 用户名。 |

**示例**

请求示例数据管理

```
http(s)://[Endpoint]/?Action=ListUserPermissions &PermType=DATABASE &Tid=-1 &UserId=13435
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<UserPermissions>
    <UserPermission>
        <Logic>false</Logic>
        <UserNickName>xxx</UserNickName>
        <DsType>DATABASE</DsType>
        <Alias>xxx_ent_dev</Alias>
        <PermDetails>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390913</UserAccessId>
                <PermType>EXPORT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390914</UserAccessId>
                <PermType>CORRECT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
        </PermDetails>
        <InstanceId>24671</InstanceId>
        <SearchName>xxx@xxx:3306</SearchName>
        <DbId>111369</DbId>
        <UserId>88658</UserId>
        <DbType>drds</DbType>
        <EnvType>dev</EnvType>
        <SchemaName>xxx_ent_dev</SchemaName>
    </UserPermission>
</UserPermissions> <TotalCount>6</TotalCount> <RequestId>C51420E3-144A-4A94-B473-8662FCF4AD10</RequestId> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "UserPermissions": {
    "UserPermission": [
      {
        "Logic": false,
        "UserNickName": "xxx",
        "DsType": "DATABASE",
        "Alias": "xxx_ent_dev",
        "PermDetails": {
          "PermDetail": [
            {
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390913",
              "PermType": "EXPORT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
            },
            {
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390914",
              "PermType": "CORRECT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
            }
```

]

```json
        },
        "InstanceId": 24671,
        "SearchName": "xxx@xxx:3306",
        "DbId": 111369,
        "UserId": 88658,
        "DbType": "drds",
        "EnvType": "dev",
        "SchemaName": "xxx_ent_dev"
      }
```

]

```json
  },
  "TotalCount": 6,
  "RequestId": "C51420E3-144A-4A94-B473-8662FCF4AD10",
  "Success": true
}
```

#### GrantUserPermission

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据管理

| Action | String | 是 | GrantUserPermi ssion | 系统规定参数。取值：GrantUserPermission。 |
|---|---|---|---|---|
| DbId | String | 是 | 1234 | 数据库ID。 |
| DsType | String | 是 | DATABASE | 权限类型，取值和说明如下： DATABASE： 物理库权限 LOGIC DATABASE：逻辑库权限 _ TABLE：物理表权限 LOGIC TABLE：逻辑表权限 _ |
| ExpireDate | String | 是 | 2019-12-12 00:00:00 | 权限过期时间。 |
| PermTypes | String | 是 | QUERY, EXPORT, CORRECT | 权限类型，多个权限类型用逗号隔开，取值和说明如下： QUERY： 查询权限 EXPORT：导出权限 CORRECT：变更权限 |
| Tid | Long | 是 | -1 | 租户ID。 |
| UserId | String | 是 | 12345 | 用户ID，对应GetUser接口里面的用户 ID，注意不是用户的阿里云UID。 |
| Logic | Boolean | 否 | false | 是否逻辑库。 |
| TableId | String | 否 | 1324245 | 表ID，授权表权限时需要指定。 |
| TableName | String | 否 | table name _ | 表名，授权表权限时需要指定。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |

数据管理

| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GrantUserPermission &DbId=1234 &DsType=DATABASE &ExpireDate=2019-12-12 00:00:00 &PermTypes=QUERY, EXPORT, CORRECT &Tid=-1 &UserId=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
}
```

### 安全管理

#### ListSensitiveColumns

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListSensitiveCol umns | 系统规定参数。取值：ListSensitiveColumns。 |
| Tid | Long | 是 | -1 | 租户ID。 |

数据管理

| SchemaName | String | 否 | test | 数据库名。 |
|---|---|---|---|---|
| TableName | String | 否 | test | 表名。 |
| ColumnName | String | 否 | test | 字段名。 |
| SecurityLevel | String | 否 | SENSITIVE | 字段敏感等级，取值和说明如下： INNER：内部 SENSITIVE： 敏感 CONFIDENTIAL： 机密 |
| PageNumber | Integer | 否 | 1 | 页码。 |
| PageSize | Integer | 否 | 10 | 每页数据量。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 0E714EF1-E617- 4BBC-A3D2- 9552063BA942 | 请求ID。 |
| SensitiveColu mnList | Array of SensitiveColu mn |  | 敏感字段列表。 |
| SensitiveColu mn |  |  |  |
| ColumnCount | Long | 1 | 字段个数。 |
| ColumnName | String | test | 字段名。 |
| FunctionType | String | DEFAULT | 脱敏算法类型，取值和说明参考： DEFAULT：全遮掩（默认） FIX POS：固定位置 _ FIX CHAR：固定字符 _ |

数据管理

| SchemaName | String | test | 数据库名。 |
|---|---|---|---|
| SecurityLevel | String | SENSITIVE | 敏感字段级别。 |
| TableName | String | test | 表名。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalCount | Long | 10 | 数据总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListSensitiveColumns &Tid=-1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据管理

```xml
<TotalCount>5</TotalCount> <RequestId>0E714EF1-E617-4BBC-A3D2-9552063BA942</RequestId> <SensitiveColumnList>
    <SensitiveColumn>
        <TableName>yuyang_test</TableName>
        <ColumnName>c1</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_luanma</TableName>
        <ColumnName>c1</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_luanma</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_json</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>CONFIDENTIAL</SecurityLevel>
        <SchemaName>test_demo</SchemaName>
    </SensitiveColumn>
</SensitiveColumnList> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "TotalCount": 5,
  "RequestId": "0E714EF1-E617-4BBC-A3D2-9552063BA942",
  "SensitiveColumnList": {
    "SensitiveColumn": [
      {
        "TableName": "yuyang_test",
        "ColumnName": "c1",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
      },
      {
        "TableName": "yuyang_test_luanma",
        "ColumnName": "c1",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
      },
      {
        "TableName": "yuyang_test",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
      },
      {
        "TableName": "yuyang_test_luanma",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
      },
      {
        "TableName": "yuyang_test_json",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "CONFIDENTIAL",
        "SchemaName": "test_demo"
      }
```

]

```json
  },
  "Success": true
}
```

#### ListSensitiveColumnsDetail

调用ListSensitiveColumnsDetail接口获取敏感字段详情信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据管理

| Action | String | 是 | ListSensitiveCol umnsDetail | 系统规定参数。取值：ListSensitiveColumnsDetail。 |
|---|---|---|---|---|
| ColumnName | String | 是 | test | 字段名。 |
| SchemaName | String | 是 | test | 数据库名。 |
| TableName | String | 是 | test | 表名。 |
| Tid | Long | 是 | 1 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | 7629888F-C9FB- 4D16-A7D3- B443FE06FBD4 | 请求ID。 |
| SensitiveColu mnsDetailList | Array of SensitiveColu mnsDetail |  | 敏感字段详情列表。 |
| SensitiveColu mnsDetail |  |  |  |
| ColumnDescri ption | String | test | 字段描述。 |
| ColumnName | String | test | 字段名。 |
| ColumnType | String | varchar(32) | 字段类型。 |
| DbId | Long | 124 | 数据库ID。 |
| DbType | String | mysql | 数据库类型。 |
| EnvType | String | product | 数据库所属环境。 |

数据管理

| Logic | Boolean | false | 是否逻辑库。 |
|---|---|---|---|
| SchemaName | String | test | 数据库名。 |
| SearchName | String | test@xxx:3306 | 数据库搜索名。 |
| TableName | String | test | 表名。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListSensitiveColumnsDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7629888F-C9FB-4D16-A7D3-B443FE06FBD4</RequestId> <SensitiveColumnsDetailList>
    <SensitiveColumnsDetail>
        <TableName>king_info</TableName>
        <ColumnName>mobile</ColumnName>
        <ColumnType>varchar(64)</ColumnType>
        <SearchName>p***@xxx.mysql.rds.aliyuncs.com:3306【xxx】</SearchName>
        <ColumnDescription>mobile</ColumnDescription>
        <DbId>8511149</DbId>
        <Logic>false</Logic>
        <SchemaName>poc_prod</SchemaName>
        <EnvType>product</EnvType>
        <DbType>mysql</DbType>
    </SensitiveColumnsDetail>
</SensitiveColumnsDetailList> <Success>true</Success>
```

`JSON` 格式数据管理

```json
{
  "RequestId": "7629888F-C9FB-4D16-A7D3-B443FE06FBD4",
  "SensitiveColumnsDetailList": {
    "SensitiveColumnsDetail": [
      {
        "TableName": "king_info",
        "ColumnName": "mobile",
        "ColumnType": "varchar(64)",
        "SearchName": "p***@xxx.mysql.rds.aliyuncs.com:3306【xxx】",
        "ColumnDescription": "mobile",
        "DbId": 8511149,
        "Logic": false,
        "SchemaName": "poc_prod",
        "EnvType": "product",
        "DbType": "mysql"
      }
```

]

```json
  },
  "Success": true
}
```

#### ChangeColumnSecLevel

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ChangeColumnS ecLevel | 系统规定参数。取值：ChangeColumnSecLevel。 |
| Tid | Long | 是 | 43253 | 租户ID。 说明鼠标移动到界面右上角的头像处，查看租户ID。 |
| DbId | Long | 是 | 325 | 数据库ID（DatabaseId），可通过调用接口SearchDatabase获取该参数的值。 说明您也可以通过调用接口ListDatabases获取物理库的 DatabaseId值，调用接口ListLogicDatabases获取逻辑库的DatabaseId值。 |
| RegionId | String | 否 | cn-hangzhou | DMS服务地域。 说明请根据应用所在地就近选择。 |

数据管理

| IsLogic | Boolean | 是 | false | 数据库是逻辑库，取值： true：物理库 false：逻辑库 |
|---|---|---|---|---|
| SchemaName | String | 是 | test schema _ | 数据库名，可通过调用接口ListSensitiveColumns获取该参数的值。 您也可以通过调用接口SearchDatabase获取该参数的值。 您也可以通过调用接口ListDatabases获取物理库的 SchemaName值，调用接口ListLogicDatabases获取逻辑库的 SchemaName值。 |
| TableName | String | 是 | test table _ | 表名，可通过调用接口ListSensitiveColumns获取该参数的值。 说明您也可以通过调用接口ListTables获取该参数的值。 |
| ColumnName | String | 是 | test column _ | 字段名，通过调用接口ListSensitiveColumns获取该参数的值。 说明您也可以通过调用接口ListColumns获取该参数的值。 |
| NewLevel | String | 是 | SENSITIVE | 输入新的字段敏感等级，取值如下： INNER：低敏感 SENSITIVE： 中敏感 CONFIDENTIAL： 高敏感 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | C51420E3-144A- 4A94-B473- 8662FCF4AD10 | 请求ID。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |

数据管理

| Success | Boolean | false | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=ChangeColumnSecLevel &Tid=3*** &DbId=1860**** &IsLogic=true &SchemaName=test_schema &TableName=test_table &ColumnName=test_column &NewLevel=SENSITIVE
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>C51420E3-144A-4A94-B473-8662FCF4AD10</RequestId>
    <Success>false</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "C51420E3-144A-4A94-B473-8662FCF4AD10",
  "Success" : false
}
```

#### AddDesensitizationRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据管理

| Action | String | 是 | AddDesensitizati onRule | 系统规定参数。取值：AddDesensitizationRule。 |
|---|---|---|---|---|
| RuleName | String | 是 | 脱敏算法测试 | 规则名称。 |
| RuleType | String | 是 | HASH | 脱敏算法。 |
| RuleDescription | String | 否 | 哈希算法 | 规则描述。 |
| FunctionType | String | 是 | MD5 | 脱敏算法类型。 |
| Tid | Long | 否 | 3*** | 租户ID。 说明鼠标移动到界面右上角的头像处，查看租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0C1CB646-1DE4- 4AD0-B4A4- 7D47DD52E931 | 请求ID。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误消息。 |
| Success | Boolean | true | 请求是否成功，取值： true：请求成功。 false：请求失败。 |
| RuleId | Integer | 35*** | 生成的脱敏规则ID。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=AddDesensitizationRule
```

`&RuleName=`脱敏算法测试

```
&RuleType=HASH
```

`&RuleDescription=`哈希算法

```
&FunctionType=MD5 &FunctionParams=[{"key":"{paramName: salt, paramValue: 1}"}]
```

&公共请求参数数据管理正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931</RequestId>
    <ErrorCode>UnknownError</ErrorCode>
    <ErrorMessage>UnknownError</ErrorMessage>
    <Success>true</Success>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "0C1CB646-1DE4-4AD0-B4A4-7D47DD52E931",
  "ErrorCode" : "UnknownError",
  "ErrorMessage" : "UnknownError",
  "Success" : true
}
```

#### ListDesensitizationRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDesensitizati onRule | 系统规定参数。取值：ListDesensitizationRule。 |
| PageNumber | Integer | 否 | 1 | 开始页码。 |
| PageSize | Integer | 否 | 20 | 每页数据量。最大值不超过100。 |
| RuleType | String | 否 | HASH | 脱敏算法。 |
| FuncType | String | 否 | MD5 | 脱敏算法类型。 |
| RuleName | String | 否 | 脱敏规则测试 | 脱敏规则名称。 |

数据管理

| RuleId | Integer | 否 | 1 | 脱敏规则ID。 |
|---|---|---|---|---|
| Tid | Long | 否 | 3*** | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TotalCount | Integer | 1 | 本次请求条件下的数据总量，此参数为可选参数，默认不返回。 |
| RequestId | String | E76DD2E7-EBAC- 5724-B163- 19AAC233F8F2 | 请求ID。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| Success | Boolean | true | 请求是否成功，取值： true：请求成功。 false：请求失败。 |
| Desensitizatio nRuleList | Array of Desensitizatio nRule |  | 脱敏规则列表。 |
| RuleName | String | 脱敏规则测试 | 脱敏规则名称。 |
| RuleType | String | HASH | 脱敏算法。 |
| RuleDesc | String | 哈希脱敏算法 | 规则描述。 |
| FunctionType | String | MD5 | 算法类型。 |
| FuncParams | String | {paramName: salt, paramValue: 1} | 参数。 |
| FuncSample | String | [{paramName: testStr, paramValue: 1}] | 示例。 |
| LastModifierId | String | 2 | 近期修改脱敏规则用户ID。 |
| LastModifierNa me | String | 测试用户 | 最后修改脱敏规则的用户名称。 |

数据管理

| ReferenceCou nt | Integer | 1 | 使用脱敏规则次数。 |
|---|---|---|---|
| RuleId | Integer | 23 | 脱敏规则ID。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=ListDesensitizationRule &PageNumber=1 &PageSize=20
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <TotalCount>1</TotalCount>
    <RequestId>E76DD2E7-EBAC-5724-B163-19AAC233F8F2</RequestId>
    <ErrorCode>UnknownError</ErrorCode>
    <ErrorMessage>UnknownError</ErrorMessage>
    <Success>true</Success>
    <DesensitizationRuleList>
```

`<RuleName>`脱敏规则测试`</RuleName>`

```xml
        <RuleType>HASH</RuleType>
```

`<RuleDesc>`哈希脱敏算法`</RuleDesc>`

```xml
        <FunctionType>MD5</FunctionType>
        <FuncParams>{paramName: salt, paramValue: 1}</FuncParams>
        <FuncSample>[{paramName: testStr, paramValue: 1}]</FuncSample>
        <LastModifierId>2</LastModifierId>
        <LastModifierName>测试用户</LastModifierName>
        <ReferenceCount>1</ReferenceCount>
        <RuleId>23</RuleId>
    </DesensitizationRuleList>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "TotalCount" : 1,
  "RequestId" : "E76DD2E7-EBAC-5724-B163-19AAC233F8F2",
  "ErrorCode" : "UnknownError",
  "ErrorMessage" : "UnknownError",
  "Success" : true,
  "DesensitizationRuleList" : [ {
```

`"RuleName" : "`脱敏规则测试`",`

```json
    "RuleType" : "HASH",
```

`"RuleDesc" : "`哈希脱敏算法`",`

```json
    "FunctionType" : "MD5",
    "FuncParams" : "{paramName: salt, paramValue: 1}",
    "FuncSample" : "[{paramName: testStr, paramValue: 1}]",
    "LastModifierId" : "2",
    "LastModifierName" : "测试用户",
    "ReferenceCount" : 1,
    "RuleId" : 23
  } ]
}
```

#### ModifyDesensitizationStrategy

调用ModifyDesensitizationStrategy接口，修改字段绑定的脱敏规则。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDesensiti zationStrategy | 系统规定参数。取值：ModifyDesensitizationStrateg y。 |
| DbId | Integer | 是 | 123 | 数据库ID，可以调用ListDatabases接口获取。 |
| IsLogic | Boolean | 是 | false | 数据库是逻辑库，取值： true：物理库。 false：逻辑库。 |

数据管理

| SchemaName | String | 是 | test schema _ | 数据库名，可以调用ListSensitiveColumns接口获取该参数的值。 说明物理库名：您还可以调用ListDatabases或Search Database接口获取该参数的值。 逻辑库名：您还可以调用ListLogicDatabases或S earchDatabase接口获取该参数的值。 |
|---|---|---|---|---|
| TableName | String | 是 | test table _ | 表名，可以调用ListSensitiveColumns接口获取该参数的值。 说明您也可以调用ListTables接口获取该参数的值。 |
| ColumnName | String | 是 | test column _ | 字段名，可调用ListSensitiveColumns接口获取该参数的值。 说明您也可以调用ListColumns接口获取该参数的值。 |
| RuleId | Integer | 否 | 53 | 脱敏规则ID。 |
| IsReset | Boolean | 否 | false | 是否重置脱敏规则。取值： true：重置脱敏规则。 false（默认）：不重置脱敏规则。 |
| Tid | Long | 否 | 3*** | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 283C461F-11D8- 48AA-B695- DF092DA32AF3 | 请求ID。 |
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误消息。 |

数据管理

| Success | Boolean | false | 请求是否成功，取值： true：请求成功。 false：请求失败。 |
|---|---|---|---|
| Result | Boolean | True | 结果值。 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=ModifyDesensitizationStrategy &DbId=123 &IsLogic=false
```

&公共请求参数正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>283C461F-11D8-48AA-B695-DF092DA32AF3</RequestId>
    <ErrorCode>UnknownError</ErrorCode>
    <ErrorMessage>UnknownError</ErrorMessage>
    <Success>false</Success>
    <Result>true</Result>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "283C461F-11D8-48AA-B695-DF092DA32AF3",
  "ErrorCode" : "UnknownError",
  "ErrorMessage" : "UnknownError",
  "Success" : false,
  "Result" : true
}
```

### 数据查询

#### ExecuteScript

目前仅支持管控模式为安全协同的实例调用该API。 数据管理

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ExecuteScript | 系统规定参数。取值：ExecuteScript。 |
| DbId | Integer | 是 | 123 | 数据库ID。 说明您可以通过GetDatabase接口返回参数DatabaseId中获取该值。 |
| Logic | Boolean | 是 | false | 是否为逻辑库。 |
| Script | String | 是 | select dt from report daily _ | 要执行的具体SQL脚本。包括DQL、DDL 和DML，其中DDL和DML是否允许依赖于实例的安全管控配置。 |
| Tid | Long | 否 | 234 | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | UnknownError | 错误码。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| RequestId | String | FE8EE2F1-4880- 46BC-A704- 5CF63EAF9A04 | 请求ID。 |
| Results | Array of Result |  | 脚本执行返回结果列表，列表中每一项对应一个脚本执行结果。 |
| ColumnNames | List | ["col1", "col2"] | 执行查询脚本时，返回的结果集字段列表。 |
| Message | String | UnknownError | 执行失败时，返回的错误信息。 |
| RowCount | Long | 1 | 返回的结果记录数。 |
| Rows | List | [{"col1": "value1", "col2":"value2"}] | 执行查询脚本时，返回的结果数据。 |

数据管理

| Success | Boolean | true | 单个脚本执行是否成功。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&DbId=123 &Logic=false &Script=select dt from report_daily
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Results>
    <Message>UnknownError</Message>
    <RowCount>1</RowCount>
    <Success>true</Success>
</Results> <Results>
    <ColumnNames>["col1", "col2"]</ColumnNames>
    <Rows>[{"col1": "value1", "col2":"value2"}]</Rows>
</Results> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{"RequestId":"FE8EE2F1-4880-46BC-A704-5CF63EAF9A04","Results": [{"Message":"UnknownError","RowCount":"1","Success":"true"},{"ColumnNames":"[\"col1\", \"col2\"]","Rows":"[{\"col1\": \"value1\", \"col2\":\"value2\"}]"}],"ErrorCode":"UnknownError","ErrorMessage":"UnknownError","Succes :"true"}
```

### 任务编排

#### UpdateTaskFlowConstants

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|

| 开发指南·API参考 |  |  |  | 数据管理 |
|---|---|---|---|---|

| Tid | long | 否 | 租户ID。 | 3*** |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 3**** |
| DagConstants | array | 是 | 任务流常量列表。 |  |
|  | object | 否 |  |  |
| Key | string | 否 | 任务流常量键名。 | poc test _ |
| Value | string | 否 | 任务流常量键值。 | poc test _ |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。可用于定位日志，排查问题。 | C4CCC000-C193- 5A32-B701- 573F497BF729 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "C4CCC000-C193-5A32-B701-573F497BF729",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### DeleteTaskFlow

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 134137*** |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 9AFE13F6-A4FD-581B- BFDE-B63B1CDC2336 |
| ErrorCode | string | 错误码。 | 403 |
| ErrorMessage | string | 错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "9AFE13F6-A4FD-581B-BFDE-B63B1CDC2336",
  "ErrorCode": "403",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### OfflineTaskFlow

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 7*** |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | A8FE12AA-300D-5FDF- 806F-C2CB99161F32 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "A8FE12AA-300D-5FDF-806F-C2CB99161F32",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### ListTaskFlow

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 4116147E-C628-5816- 8779-8EEAF8E973F4 |
| ErrorCode | string | 错误码。 | 403 |
| ErrorMessage | string | 错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| TaskFlowList | array | 任务流信息列表。 |  |
|  | object | 任务流程列表。 |  |
| Id | long | 任务流ID。 | 134137**** |
| CreatorId | string | 创建人的用户ID。 | 51**** |

数据管理

| CreatorNickName | string | 创建人的昵称。 | Creator NickName _ |
|---|---|---|---|
| DagOwnerNickName | string | 任务流Owner的昵称。 | Owner NickName _ |
| DeployId | long | 最近一次部署记录的ID。 | 12** |
| Status | integer | 任务流状态，返回值如下： 0：无效 1：无调度配置 2：等待调度 | 2 |
| LatestInstanceStatus | integer | 最后一个运行记录的状态，返回值如下： 0：无效 1：无调度配置 2：等待调度 | 0 |
| LatestInstanceTime | string | 最近一个运行记录的创建时间。 | 2022-04-13 |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "4116147E-C628-5816-8779-8EEAF8E973F4",
  "ErrorCode": "403",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "TaskFlowList": {
    "TaskFlow": [
      {
        "Id": 0,
        "CreatorId": "51****",
        "CreatorNickName": "Creator_NickName",
        "DagOwnerNickName": "Owner_NickName",
        "DeployId": 0,
        "Status": 2,
        "LatestInstanceStatus": 0,
        "LatestInstanceTime": "2022-04-13"
      }
```

]

```
  }
}
```

数据管理

#### GetTaskInstanceRelation

调用GetTaskInstanceRelation接口，获取任务流运行记录的节点信息。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 7*** |
| DagInstanceId | long | 是 | 任务流运行记录 ID（Id）。您可调用ListTaskFlowInsta nce接口获取该参数的值。 | 47**** |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 028BF827-3801-5869- 8548-F4A039256304 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| NodeList | array | 任务流运行记录的节点信息列表。 |  |
|  | object | 运行记录的节点信息列表。 |  |
| Id | long | 任务节点运行记录ID。 | 14059 |

数据管理

| NodeId | long | 任务节点ID。 | 14059 |
|---|---|---|---|
| NodeName | string | 任务节点名称。 | Spark SQL-1 |
| NodeType | integer | 任务节点类型，返回值请参见NodeType参数说明。 | 2 |
| BusinessTime | string | 业务时间。 | 2021-11-09 14:37:26 |
| Status | integer | 任务节点运行状态，取值如下： 0：等待调度 1：正在运行 2：挂起 3：运行失败 4：运行成功 5：已完成 | 4 |
| Message | string | 任务描述信息。 | test |
| ExecuteTime | long | 任务执行时间，单位为毫秒。 | 170655 |
| EndTime | string | 任务流运行结束时间，时间格式为yyyy-MM-DD HH:mm:ss。 | 2021-11-11 14:38:57 |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "028BF827-3801-5869-8548-F4A039256304",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "NodeList": {
    "Node": [
      {
        "Id": 14059,
        "NodeId": 14059,
        "NodeName": "Spark SQL-1",
        "NodeType": 36,
        "BusinessTime": "2021-11-09 14:37:26",
        "Status": 4,
        "Message": "test",
        "ExecuteTime": 170655,
        "EndTime": "2021-11-11 14:38:57"
      }
```

]

```
  }
}
```

#### ListTaskFlowInstance

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 7*** |
| TriggerType | integer | 否 | 触发类型，取值如下： 0：周期调度 1：手动运行 | 1 |
| StartTimeBegin | string | 否 | 筛选出指定时间之后开始的任务流运行记录。时间格式为yyyy-MM-DD。 | 2022-01-07 |
| StartTimeEnd | string | 否 | 筛选出指定时间之前开始的任务流运行记录。时间格式为yyyy-MM-DD。 | 2022-04-08 |
| PageIndex | integer | 是 | 第几页。 | 1 |

数据管理

| PageSize | integer | 是 | 每页数据量。 | 20 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 8CFF2295-8249-5287- B888-DBD4F0D76CB0 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| DAGInstanceList | array | 任务流运行记录列表。 |  |
|  | object | 任务流运行记录列表。 |  |
| Id | long | 运行记录ID。 | 9234 |
| BusinessTime | string | 任务流业务时间，时间格式为yyyy-MM-DD HH:mm:ss。 | 2021-11-10 14:37:26 |
| EndTime | string | 任务流运行结束时间，时间格式为yyyy-MM-DD HH:mm:ss。 | 2021-11-11 14:38:57 |
| DagId | string | 任务流ID。 | 7*** |

数据管理

| TriggerType | integer | 触发类型。返回值如下： 0：周期调度 1：手动运行 | 1 |
|---|---|---|---|
| Status | integer | 任务流状态，返回值如下： 0：等待调度 1：运行中 2：暂停 3：失败 4：成功 5：完成 | 4 |
| Message | string | 任务描述信息。 | test |
| HistoryDagId | long | 历史任务流版本ID。 | 2**** |
| DagName | string | 任务流名称。 | Spark SQL test _ _ |
| OwnerName | string | 任务流Owner的名称。 | test name _ |
| DagVersion | string | 任务流版本。 | [] |
| TotalCount | integer | 满足条件运行记录总个数。 | 1 |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "8CFF2295-8249-5287-B888-DBD4F0D76CB0",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "DAGInstanceList": {
    "DAGInstance": [
      {
        "Id": 9234,
        "BusinessTime": "2021-11-10 14:37:26",
        "EndTime": "2021-11-11 14:38:57",
        "DagId": "7***",
        "TriggerType": 1,
        "Status": 4,
        "Message": "test",
        "HistoryDagId": 0,
        "DagName": "Spark_SQL_test",
        "OwnerName": "test_name",
        "DagVersion": "[]"
      }
```

]

```json
  },
  "TotalCount": 1
}
```

#### ListDAGVersions

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 7*** |
| PageIndex | integer | 是 | 第几页。 | 1 |
| PageSize | integer | 是 | 每页数据量。 | 20 |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|

数据管理

|  | object |  |  |
|---|---|---|---|
| RequestId | string | 请求ID。 | C7775630-7901-51B9- 8782-9B585EC0799A |
| ErrorCode | string | 错误码。 | 403 |
| ErrorMessage | string | 错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| TotalCount | integer | 查询结果总数。 | 1 |
| DagVersionList | array | 发布版本列表。 |  |
|  | object | 发布版本列表。 |  |
| DagName | string | 任务流名称。 | Spark SQL |
| DagOwnerId | string | 任务流Owner的用户ID。 | 51**** |
| DagOwnerNickName | string | 任务流Owner的昵称。 | name |
| VersionComments | string | 任务流版本描述。 | test OSS _ |
| VersionId | long | 任务流版本ID。 | 2**** |
| LastVersionId | long | 上一个发布版本ID。 | 2**** |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "C7775630-7901-51B9-8782-9B585EC0799A",
  "ErrorCode": "403",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "TotalCount": 1,
  "DagVersionList": {
    "DagVersion": [
      {
        "DagName": "Spark SQL",
        "DagOwnerId": "51****",
        "DagOwnerNickName": "name",
        "VersionComments": "test_OSS",
        "VersionId": 0,
        "LastVersionId": 0
      }
```

]

```
  }
}
```

#### ReDeployLhDagVersion

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 7*** |
| DagVersion | long | 否 | 任务流版本 ID（VersionId）。 | 2**** |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 035C92E0-2EAD-50E5- A6DD-550F5F73D7CE |

数据管理

| ErrorCode | string | 错误码。 | 403 |
|---|---|---|---|
| ErrorMessage | string | 错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| DeployId | long | 部署记录ID。 | 15990 |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "035C92E0-2EAD-50E5-A6DD-550F5F73D7CE",
  "ErrorCode": "403",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "DeployId": 15990
}
```

#### UpdateScenario

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| ScenarioId | string | 是 | 业务场景ID。 | 12*** |
| ScenarioName | string | 是 | 业务场景名称。 | 业务场景-测试 |
| Description | string | 否 | 业务场景描述。 | test |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|

数据管理

|  | object |  |  |
|---|---|---|---|
| RequestId | string | 请求ID。 | 7FAD400F-7A5C-4193- 8F9A-39D86C4F0231 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "7FAD400F-7A5C-4193-8F9A-39D86C4F0231",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### ResumeTaskFlowInstance

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID。 | 11**** |
| DagInstanceId | long | 是 | 任务流运行记录 ID（Id）。您可调用ListTaskFlowIns tance接口获取该参数的值。 | 3**** |

数据管理

| DagVersion | string | 是 | 任务流版本号。您可调用ListDAGVersion s接口获取该参数的值。 | [] |
|---|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 7FF2E325-763F-5E27- 9157-C3CFA02F4CBF |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "7FF2E325-763F-5E27-9157-C3CFA02F4CBF",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### UpdateTaskContent

**接口说明**

该接口可用于修改节点配置内容。

**请求参数**

数据管理

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| NodeId | string | 是 | 任务节点ID。 | 43**** |
| NodeContent | string | 否 | 修改后的节点配置内容。 | { "dbId":12****, "sql":"select * from test table", _ "dbType":"lindor m sql" } _ |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | 39557312-28D5-528F- 9554-80C0700EB489 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "39557312-28D5-528F-9554-80C0700EB489",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

数据管理

#### ListTaskFlowsByPage

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| PageIndex | integer | 否 | 第几页。 | 1 |
| PageSize | integer | 否 | 每页数据量。 | 20 |
| SearchKey | string | 否 | 搜索任务流名称关键字。 | 测试节点 |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 6CB28697-BFE2-5739- 9228-3971990E982C |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |
| TaskFlowList | array | 任务流信息列表。 |  |
|  | object |  |  |
| Id | long | 任务流ID。 | 7*** |

数据管理

| DagName | string | 任务流名称。 | poc task test _ _ |
|---|---|---|---|
| Description | string | 任务流描述。 | test |
| CreatorId | string | 创建人的用户ID。 | 51**** |
| CreatorNickName | string | 创建任务流用户的昵称。 | Creator NickName _ |
| DagOwnerNickName | string | 任务流Owner的昵称。 | Owner NickName _ |
| DeployId | long | 最近一次部署记录的ID。 | 65*** |
| Status | integer | 任务流状态，返回值如下： 0：无效。 1：无调度配置。 2：等待调度。 | 1 |
| LatestInstanceStatus | integer | 最后一个运行记录的状态，返回值如下： 0：无效。 1：无调度配置。 2：等待调度。 | 0 |
| LatestInstanceTime | string | 最近一个运行记录的创建时间。 | 2022-04-13 |
| TotalCount | integer | 记录总数。 | 24 |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "6CB28697-BFE2-5739-9228-3971990E982C",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "TaskFlowList": {
    "TaskFlow": [
      {
        "Id": 0,
        "DagName": "poc_task_test",
        "Description": "test",
        "CreatorId": "51****",
        "CreatorNickName": "Creator_NickName",
        "DagOwnerNickName": "Owner_NickName",
        "DeployId": 0,
        "Status": 1,
        "LatestInstanceStatus": 0,
        "LatestInstanceTime": "2022-04-13"
      }
```

]

```json
  },
  "TotalCount": 24
}
```

#### ListScenarios

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 7FAD400F-7A5C-4193- 8F9A-39D86C4F0231 |
| ErrorCode | string | 错误码。 | UnknownError |

数据管理

| ErrorMessage | string | 调用失败时，返回的出错信息。 | UnknownError |
|---|---|---|---|
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |
| ScenarioList | array | 业务场景列表。 |  |
|  | object |  |  |
| Id | long | 业务场景ID。 | 41*** |
| ScenarioName | string | 业务场景名称。 | test |
| CreatorId | string | 创建人的用户ID。 | 23*** |
| Description | string | 业务场景描述。 | test |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "7FAD400F-7A5C-4193-8F9A-39D86C4F0231",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "ScenarioList": [
    {
      "Id": 0,
      "ScenarioName": "test",
      "CreatorId": "23***",
      "Description": "test"
    }
```

]

```
}
```

#### UpdateTaskConfig

数据管理

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| NodeId | string | 是 | 任务节点ID。 | 43**** |
| NodeConfig | string | 是 | 节点高级配置。取值为JSON字符串格式。 | { "rerun":{ "rerunEnable":tru e, "rerunCount":1, "rerunInterval":1 0 } } |

NodeConfig为JSON字符串格式，如下：

```
{
```

`"rerun":{ //` 必填固定值 `"rerunEnable":true, //` 是否开启重跑 `"rerunCount":1, //` 重跑次数 `"rerunInterval":10 //` 重跑间隔

```
    }
}
```

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | F4E2A94B-604F-43FF- 93E7-F4EE3DCF412E |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |

**示例**

数据管理正常返回示例 `JSON` 格式

```json
{
  "RequestId": "F4E2A94B-604F-43FF-93E7-F4EE3DCF412E",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### ListTaskFlowConstants

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID。 | 3**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | 028BF827-3801-5869- 8548-F4A039256304 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，取值： true：请求成功。 false：请求失败。 | true |
| DagConstants | array | 任务流常量键值对列表。 |  |
|  | object |  |  |

数据管理

| Key | string | 常量键。 | example |
|---|---|---|---|
| Value | string | 常量值。 | 0 |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "028BF827-3801-5869-8548-F4A039256304",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "DagConstants": {
    "DagConstant": [
      {
        "Key": "example",
        "Value": "0"
      }
```

]

```
  }
}
```

#### BackFill

**接口说明**

补充数据时，任务流按照日期串行执行，可指定按日期升序或降序执行。补充数据完成后，可指定日期或日期范围，以及节点范围来运行任务流。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID。 | 15*** |
| StartNodeIds | array | 否 | 补数据开始节点ID 列表。 |  |
|  | long | 否 | 待补数据的任务节点数。 | 2 |

数据管理

| IsTriggerSubTree | boolean | 否 | 是否运行下游节点。缺省时默认为 false。 | false |
|---|---|---|---|---|
| BackFillDate | string | 否 | 补数据业务时间。 指定时间补数据需要填写该参数。 | 2022-01-14 |
| BackFillDateBegi n | string | 否 | 补数据开始业务时间。指定时间范围补数据需要填写该参数。 | 2022-01-14 |
| BackFillDateEnd | string | 否 | 补数据结束业务时间。指定时间范围补数据需要填写该参数。 | 2022-09-29 |
| Interval | integer | 否 | 补数据时间间隔， 单位：小时。最小值：1，默认值： 24。 | 24 |
| Asc | boolean | 否 | 补数据任务流运行顺序。取值： false：降序。 从大日期到小日期。 true：默认值， 升序。从小日期到大日期。 | true |
| HistoryDagId | long | 否 | 历史任务流ID。 | 16*** |

指定日期补数据，需提供BackFillDate参数。指定时间范围补数据，需提供BackFillDateBegin和

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 7FAD400F-7A5C-4193- 8F9A-39D86C4F0231 |
| ErrorCode | string | 错误码。 | UnknownError |

数据管理

| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
|---|---|---|---|
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| NodeId | long | 任务节点ID。 | 43**** |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "7FAD400F-7A5C-4193-8F9A-39D86C4F0231",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "NodeId": 0
}
```

#### UpdateTaskTimeVariables

更新任务时间变量。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| NodeId | string | 是 | 任务节点ID。 | 43**** |
| TimeVariables | string | 是 | 节点变量，时间变量配置。取值类型为JSON格式的字符串。 | {"variables":[ {"name":"var", "pattern":"yyyy- MM-dd\|+0m+0h- 2d+0w+0M+1y" } ]} |

**返回参数**

数据管理

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 39557312-28D5-528F- 9554-80C0700EB489 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "39557312-28D5-528F-9554-80C0700EB489",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### ListTaskFlowTimeVariables

调用ListTaskFlowTimeVariables接口，获取任务流时间变量列表。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 11**** |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

数据管理

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | EC12A3BE-149F-5365- AF33-12CC8C963923 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |
| TimeVariables | array | 任务流时间变量。 |  |
|  | object |  |  |
| Name | string | 时间变量名称。 | time test _ |
| Pattern | string | 时间变量格式。 | 2018-09-26\|+7h |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "EC12A3BE-149F-5365-AF33-12CC8C963923",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "TimeVariables": {
    "timeVariable": [
      {
        "Name": "time_test",
        "Pattern": "2018-09-26|+7h"
      }
```

]

```
  }
}
```

数据管理

#### UpdateTaskFlowTimeVariables

调用UpdateTaskFlowTimeVariables接口，更新任务流时间变量。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID。 | 43**** |
| TimeVariables | string | 是 | 任务流时间变量。 | {"variables":[ {"name":"var", "pattern":"yyyy- MM-dd\|+0m+0h- 2d+0w+0M+1y" } ]} |

TimeVariables为JSON字符串格式，示例说明如下：

```json
{
    "variables":[
        {
```

`"name":"var",//` 变量命名 `/*` 变量格式语法示例如示例值所示——在运行时日期的基础上，偏移“分”、“时”、“日”、“周”、“月”、“年”(可缺省，可不按照此顺序)。 `*/`

```json
            "pattern":"yyyy-MM-dd|+0d"
        },
        {
            "name":"test",
            "pattern":"yyyy-MM-dd|+0d"
        }
```

]

```
}
```

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | 39557312-28D5-528F- 9554-80C0700EB489 |

数据管理

| ErrorCode | string | 错误码。 | UnknownError |
|---|---|---|---|
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "39557312-28D5-528F-9554-80C0700EB489",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### UpdateTaskFlowCooperators

调用UpdateTaskFlowCooperators接口，更新任务流相关人员列表。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID。 | 11**** |
| CooperatorIds | array | 否 | 待更新的相关人员用户Id列表。 |  |
|  | string | 否 | 相关人员的用户 ID。 | 12**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|

数据管理

|  | object | Schema of Response |  |
|---|---|---|---|
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | D05B3EE1-B6D3- 5B17-8CA6- A8054828E5B2 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "D05B3EE1-B6D3-5B17-8CA6-A8054828E5B2",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### CreateScenario

调用CreateScenario接口，创建业务场景，也可以将任务流按业务场景进行分组。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| ScenarioName | string | 是 | 业务场景名称。 | 业务场景-测试 |
| Description | string | 否 | 业务场景描述。 | test |

**返回参数**

数据管理

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 4E1D2B4D-3E53- 4ABC-999D- 1D2520B3471A |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |
| ScenarioId | long | 业务场景ID。 | 36*** |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "4E1D2B4D-3E53-4ABC-999D-1D2520B3471A",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "ScenarioId": 0
}
```

#### DeleteScenario

**接口说明**

使用此接口时，您需要保证当前业务场景下的任务流为空。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|

数据管理

| Tid | long | 否 | 租户ID。 | 3*** |
|---|---|---|---|---|
| ScenarioId | long | 是 | 业务场景ID。您可调用ListScenarios或 CreateScenario获取该参数的值。 | 12*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | 12*** |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功。 false：请求失败。 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "12***",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### UpdateSLARules

**接口说明**

SLA规则随着任务流的部署、发布而生效。 数据管理

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID。 | 11**** |
| Tid | long | 否 | 租户ID。 | 3*** |
| SlaRuleList | array | 否 | SLA规则列表。 |  |
|  | object | 否 |  |  |
| DagId | long | 是 | 任务流ID。 | 15*** |
| NodeId | long | 否 | 任务节点ID。 | 0 |
| Type | integer | 是 | 规则类型： 0：任务流SLA规则。 1：任务节点SLA 规则。 | 0 |
| IntervalMinutes | integer | 是 | 超时时间(单位: 分钟)。 | 1080 |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | Schema of Response |  |
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | 88E053F7-347B-52DD- A186-1F340EEC0C27 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |

数据管理

| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
|---|---|---|---|

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "88E053F7-347B-52DD-A186-1F340EEC0C27",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### GetRuleNumLimitOfSLA

调用GetRuleNumLimitOfSLA接口，获取任务编排自定义SLA规则的限制数量，自定义的SLA规则数量不可超过该限制数。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 11**** |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | Schema of Response |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | D05B3EE1-B6D3- 5B17-8CA6- A8054828E5B2 |
| ErrorCode | string | 错误码。 | UnknownError |

数据管理

| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
|---|---|---|---|
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| RuleNumLimit | integer | SLA规则数量限制。 | 12 |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "D05B3EE1-B6D3-5B17-8CA6-A8054828E5B2",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "RuleNumLimit": 12
}
```

#### GetIntervalLimitOfSLA

调用GetIntervalLimitOfSLA接口，获取任务流允许配置SLA超时规则时，其最小调度周期限制。

**接口说明**

设置SLA规则时，任务流的调度周期需要大于SLA规则数量限制。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 11**** |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|

数据管理

|  | object | Schema of Response |  |
|---|---|---|---|
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | 5B96E35F-A58E-5399- 9041-09CF9A1E46EA |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| IntervalLimit | integer | 周期限制（单位：分钟）。 | 59 |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "5B96E35F-A58E-5399-9041-09CF9A1E46EA",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "IntervalLimit": 59
}
```

#### ListDefaultSLARules

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 11**** |
| Tid | long | 否 | 租户ID。 | 3*** |

数据管理

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | Schema of Response |  |
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | 3E8AF4C3-A822-53A8- 970C-059EE83BBD5A |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| SLARuleList | array | SLA规则列表。 |  |
|  | object |  |  |
| Id | long | SLA规则ID。 | 1 |
| DagId | long | 任务流ID。 | 0 |
| NodeId | long | 任务流节点ID。 | 0 |
| RuleType | integer | 规则类型： 0：任务流SLA规则。 1：任务节点SLA规则。 | 0 |
| IntervalMinutes | integer | 超时时间(单位: 分钟)。 | 1080 |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "3E8AF4C3-A822-53A8-970C-059EE83BBD5A",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "SLARuleList": {
    "SLARule": [
      {
        "Id": 1,
        "DagId": 0,
        "NodeId": 0,
        "RuleType": 0,
        "IntervalMinutes": 1080
      }
```

]

```
  }
}
```

#### ListTaskFlowCooperators

获取任务流相关人列表。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 15**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | 54C99C70-2DFF-5A8C- A252-EBAA1EB668EC |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |

数据管理

| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
|---|---|---|---|
| CooperatorList | array | 相关人员列表。 |  |
|  | object | 相关人员信息。 |  |
| NickName | string | 用户昵称。 | name |
| Email | string | 用户邮箱。 | t***@XX.com |
| LoginName | string | 用户名。 | name |
| UserId | string | 用户ID。 | 123 |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "54C99C70-2DFF-5A8C-A252-EBAA1EB668EC",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "CooperatorList": {
    "Cooperator": [
      {
        "NickName": "name",
        "Email": "t***@XX.com",
        "LoginName": "name",
        "UserId": "123"
      }
```

]

```
  }
}
```

#### ListSLARules

**请求参数**

数据管理

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 11**** |
| Tid | long | 否 | 租户ID。 | 3*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | Schema of Response |  |
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | 3D1A59F4-EB2B- 5D24-80A5- 90C446A00DE2 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| SLARuleList | array | SLA规则列表。 |  |
|  | object |  |  |
| Id | long | SLA规则ID。 | 2 |
| DagId | long | 任务流ID。 | 11**** |
| NodeId | long | 任务流节点ID。 | 1 |

数据管理

| RuleType | integer | 规则类型： 0：任务流SLA规则。 1：任务节点SLA规则。 | 0 |
|---|---|---|---|
| IntervalMinutes | integer | 超时时间(单位: 分钟)。 | 1080 |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "3D1A59F4-EB2B-5D24-80A5-90C446A00DE2",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "SLARuleList": {
    "SLARule": [
      {
        "Id": 2,
        "DagId": 0,
        "NodeId": 1,
        "RuleType": 0,
        "IntervalMinutes": 1080
      }
```

]

```
  }
}
```

#### GetTask

调用GetTask接口，按照任务流节点ID获取指定节点的配置，包括任务的时间变量。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| NodeId | long | 是 | 任务节点ID。可调用GetTaskInstanc eRelation接口获取此参数的值。 | 51*** |

**返回参数**

数据管理

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | Schema of Response |  |
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | 7838266C-E17B-58F4- B072-4DC356B58258 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| Task | object | 任务流任务。 |  |
| DagId | long | 节点所在的任务流ID。 | 7321 |
| NodeName | string | 任务节点名称。 | 跨库Spark SQL-1 |
| NodeType | string | 任务节点类型，返回值请参见NodeType参数说明。 | 单实例SQL |
| NodeContent | string | 节点配置内容。 | {\"dbList\": [{\"instanceId\":177*** *}" } |
| TimeVariables | string | 节点变量（时间变量配置）。 | {\"variables\": [{\"name\":\"Today\",\" pattern\":\"yyyy-MM- dd\|+1d\"}]} |

数据管理

| NodeConfig | string | 节点高级配置。 | {\"dbId\":39****,\"dbT ype\":\"mysql\",\"local e\":\"zh\",\"sql\":\"/* 请确认以下SQL符合您的变更需求，务必确认无误后再提交执行 */\\n\\nCREATE TABLE IF NOT EXISTS `momo weekGather` _ (\\n\\t`id` bigint AUTO INCREMENT _ DEFAULT '0',\\n\\t`age` bit NULL,\\n\\t`action` varchar(150) NULL,\\n\\t`elapse tim _ e` datetime NULL,\\n\\tPRIMARY KEY (`id`)\\n) ENGINE=InnoDB\\nDEF AULT CHARACTER SET=utf8;\"} |
|---|---|---|---|
| NodeOutput | string | 节点输出变量，仅部分类型节点存在此参数。 | { "outputs":[ "extractMethod":"json" , "variableName":"var", "description":"demo desc" } ] } |
| GraphParam | string | 节点在图上的显示位置。 | {" {\"x\":0,\"y\":0,\"layout Type\":\"Horizontal\"}" , "id": 51***} |

TimeVariables为JSON字符串格式，示例及说明如下： 数据管理

```json
{
    "variables":[
        {
```

`"name":"var",//` 变量命名 `/*` 变量格式语法示例如示例值所示-在运行时日期的基础上，偏移“分”、“时”、“日”、“周”、“月”、“年”(可缺省 ，可不按照此顺序)。 `*/`

```json
            "pattern":"yyyy-MM-dd|+0d"
        },
        {
            "name":"test",
            "pattern":"yyyy-MM-dd|+0d"
        }
```

]

```
}
```

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "7838266C-E17B-58F4-B072-4DC356B58258",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "Task": {
    "DagId": 7321,
    "NodeName": "跨库Spark SQL-1",
    "NodeType": "SPARK_SQL",
    "NodeContent": "{\\\"dbList\\\":[{\\\"instanceId\\\":177****}\"   }",
    "TimeVariables": "{\\\"variables\\\":
[{\\\"name\\\":\\\"Today\\\",\\\"pattern\\\":\\\"yyyy-MM-dd|+1d\\\"}]}",
    "NodeConfig": "
{\\\"dbId\\\":39****,\\\"dbType\\\":\\\"mysql\\\",\\\"locale\\\":\\\"zh\\\",\\\"sql\\\":\
```

`"/*` 请确认以下`SQL`符合您的变更需求，务必确认无误后再提交执行 */\\\\n\\\\nCREATE TABLE IF NOT EXIS

```json
TS `momo_weekGather` (\\\\n\\\\t`id` bigint AUTO_INCREMENT DEFAULT '0',\\\\n\\\\t`age` bit NULL,\\\\n\\\\t`action` varchar(150) NULL,\\\\n\\\\t`elapse_time` datetime NULL,\\\ \n\\\\tPRIMARY KEY (`id`)\\\\n) ENGINE=InnoDB\\\\nDEFAULT CHARACTER SET=utf8;\\\"}",
    "NodeOutput": "{ \"outputs\":[ \"extractMethod\":\"json\" ,
\"variableName\":\"var\", \"description\":\"demo desc\" } ] }",
    "GraphParam": "{\"
{\\\"x\\\":0,\\\"y\\\":0,\\\"layoutType\\\":\\\"Horizontal\\\"}\", \"id\": 51***}"
  }
}
```

#### MoveTaskFlowToScenario

数据管理

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID。可通过调用接口ListTaskFlow获取该参数的值。 | 11**** |
| ScenarioId | long | 否 | 目标业务场景ID。 参数缺省或小于等于0时移动至默认业务场景。您可调用CreateScenario 接口获取该参数的值。 | 1**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID，用于定位日志， 排查问题。 | D85FD18C-4322- 5D49-8C14- 5A10E668F86C |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "D85FD18C-4322-5D49-8C14-5A10E668F86C",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### GetTaskFlowNotification

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 15*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | F19D575F-EBEA-5683- AFA3-A8F6D9A7DE03 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值说明如下： true：请求成功。 false：请求失败。 | true |
| Notification | object | 用户指定消息通知配置。 |  |

数据管理

| DagNotificationFail | boolean | 任务流运行失败通知开关。返回值说明如下： true：开启。 false：关闭。 | true |
|---|---|---|---|
| DagNotificationSucces s | boolean | 任务流运行成功通知开关。返回值说明如下： true：开启。 false：关闭。 | true |
| DagNotificationSla | boolean | 任务流SLA通知全局开关。返回值说明如下： true：开启。 false：关闭。 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "F19D575F-EBEA-5683-AFA3-A8F6D9A7DE03",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "Notification": {
    "DagNotificationFail": true,
    "DagNotificationSuccess": true,
    "DagNotificationSla": true
  }
}
```

#### UpdateTaskName

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| NodeId | string | 是 | 任务节点ID。可调用GetTaskInstanc eRelation接口获取该参数的值。 | 449*** |

数据管理

| NodeName | string | 是 | 任务节点名称。可调用GetTaskInstanc eRelation接口获取该参数的值。 | Spark-test |
|---|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | C4604178-3BE1-5973- ACF0-7D561AEEF3A8 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "C4604178-3BE1-5973-ACF0-7D561AEEF3A8",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### UpdateTaskOutput

**接口说明**

仅单实例SQL赋值、脚本代码、ECS远程命令任务节点具有输出变量。

**请求参数**

数据管理

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| NodeId | string | 是 | 任务节点ID。可调用GetTaskInstanc eRelation接口获取此参数的值。 | 14059 |
| NodeOutput | string | 否 | 任务输出变量。 | {“outputs”: [{"row":0, "column":- 1,"combiner":","} "extractMethod": " {\"row\":0,\"colu mn\":- 1,\"combiner\":\", \"}", "variableName":" var", // 变量 "description":"For demo" // 变量介绍}]} |

**单实例SQL赋值**

NodeOutput样例如下： 数据管理

```json
{
    "outputs":[
        {
```

`/*` 变量提取设置

```
            {
```

`"row":0, //` 行，`-1`为所有行 `"column":-1, //` 列，`-1`为所有列 `/*` 分隔符当选中所有行或所有列时，需要指定连接符。变量返回值为字符串 `*/`

```json
                "combiner":","
            }
```

`*/`

```json
            "extractMethod":"{\"row\":0,\"column\":-1,\"combiner\":\",\"}",
            "variableName":"var", // 变量名
            "description":"For demo" // 变量介绍
        }
```

]

```
}
```

**脚本代码/ECS远程命令**

NodeOutput样例如下：

```json
{
    "outputs":[
        {
            "extractMethod":"json", // 固定为JSON
            "variableName":"var",  // 变量名
            "description":"demo desc" // 变量描述
        }
```

]

```
}
```

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | AB524768-8A5F-523A- 91BD-1147187FCD62 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |

数据管理

| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
|---|---|---|---|

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "AB524768-8A5F-523A-91BD-1147187FCD62",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### DeleteTaskFlowEdgesByCondition

调用DeleteTaskFlowEdgesByCondition接口，按照多条件删除任务流边。

**接口说明**

此接口为多条件查询接口，可用于删除指定任务流中，满足所有指定条件的任务流边，请谨慎操作。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 15**** |
| Id | long | 否 | 待删除任务流边的 ID。 | 24*** |
| NodeFrom | long | 否 | 待删除边的起点节点ID。 | 44*** |
| NodeEnd | long | 否 | 待删除边的终点节点ID。 | 44*** |

**返回参数**

数据管理

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | 21234B66-6859-5558- 9E5B-006EFE915CD0 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的出错信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "21234B66-6859-5558-9E5B-006EFE915CD0",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### ListTaskFlowEdgesByCondition

调用ListTaskFlowEdgesByMultiCondition接口，多条件获取指定任务流DAG图的边。

**接口说明**

此接口为多条件查询接口，可用于获取指定任务流中，满足所有指定条件的任务流边。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |

数据管理

| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 15*** |
|---|---|---|---|---|
| Id | long | 否 | 任务流边ID。 | 24*** |
| NodeFrom | long | 否 | 边的起点节点ID。 | 44*** |
| NodeEnd | long | 否 | 边的终点节点Id。 | 44*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | D86249CD-422F-5ACF- 85BA-9187C986AE0B |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| Edges | array | 任务流边列表。 |  |
|  | object |  |  |
| Id | long | 任务流边ID。 | 24*** |
| NodeEnd | long | 边的终点节点ID。 | 44*** |
| NodeFrom | long | 边的起点节点ID。 | 44*** |

**示例**

数据管理正常返回示例 `JSON` 格式

```json
{
  "RequestId": "D86249CD-422F-5ACF-85BA-9187C986AE0B",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "Edges": {
    "Edge": [
      {
        "Id": 0,
        "NodeEnd": 0,
        "NodeFrom": 0
      }
```

]

```
  }
}
```

#### AddTaskFlowEdges

为已存在的任务流节点建立有向边。

**接口说明**

新增的边需要满足以下限制，否则将无法成功添加：
1. 指定的边端点存在于DagId指定的任务流DAG图中。
2. 添加后有向边后，DAG图不出现环。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 15*** |
| Edges | array | 是 | 任务流边列表。 |  |
|  | object | 否 | 任务流边信息。 |  |
| NodeEnd | long | 是 | 边的终点节点ID。 | 44*** |
| NodeFrom | long | 是 | 边的起点节点ID。 | 44*** |

数据管理

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | Schema of Response |  |
| RequestId | string | 请求ID。请求的唯一标识，用于定位日志，排查问题。 | E5EE2B9E-2F95-57FA- B284-CB441CEE49D6 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的出错信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| EdgeIds | array | 任务流边ID列表。 |  |
|  | long | 任务流边ID。 | 24*** |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "E5EE2B9E-2F95-57FA-B284-CB441CEE49D6",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "EdgeIds": {
    "EdgeId": [
```

]

```
  }
}
```

#### UpdateTaskFlowNameAndDesc

调用UpdateTaskFlowNameAndDesc接口，更新任务流名称和描述。

**请求参数**

数据管理

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，任务流的唯一标识。可通过调用接口ListTaskFlow获取该参数的值。 | 15*** |
| DagName | string | 是 | 待更新的任务流名称。 | test |
| Description | string | 否 | 待更新的任务流描述。 | test |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | F73CCB9D-0CF3- 5D3D-97B0- D852A8022663 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "F73CCB9D-0CF3-5D3D-97B0-D852A8022663",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### GetTaskFlowGraph

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 15*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。 | D9D91166-A626-5F4E- 9CA6-7AB10C59DBD8 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| TaskFlowGraph | object | 任务流的DAG图变量列表。 |  |

数据管理

| DagName | string | 任务流名称。 | test |
|---|---|---|---|
| Nodes | array | 任务流节点列表。 |  |
|  | object |  |  |
| DagId | long | 任务流ID。 | 15*** |
| NodeId | long | 任务节点ID。 | 44*** |
| NodeName | string | 任务节点名称。 | test |
| NodeType | long | 任务节点类型，返回值请参见NodeType参数说明。 | 32 |
| NodeContent | string | 节点配置内容。 | {ODI3OTNRVC****UHV FT29"} |
| TimeVariables | string | 节点变量（时间变量配置）。 | {\"variables\": [{\"name\":\"Today\",\" pattern\":\"yyyy-MM- dd\|+1d\"}]} |
| NodeConfig | string | 节点高级配置。 | {\"dbId\":39****,\"dbT ype\":\"mysql\",\"local e\":\"zh\",\"sql\":\"/* 请确认以下SQL符合您的变更需求，务必确认无误后再提交执行 */\\n\\nCREATE TABLE IF NOT EXISTS `momo weekGather` _ (\\n\\t`id` bigint AUTO INCREMENT _ DEFAULT '0',\\n\\t`age` bit NULL,\\n\\t`action` varchar(150) NULL,\\n\\t`elapse tim _ e` datetime NULL,\\n\\tPRIMARY KEY (`id`)\\n) ENGINE=InnoDB\\nDEF AULT CHARACTER SET=utf8;\"} |
| GraphParam | string | 节点在图上的显示位置。 | {\"x\":541,\"y\":322,\"l ayoutType\":\"Horizont al\"} |

数据管理

| Edges | array | 任务流边列表。 |  |
|---|---|---|---|
|  | object |  |  |
| DagId | long | 任务流ID。 | 15*** |
| Id | long | 任务流边ID。 | 24*** |
| NodeEnd | long | 边的终点节点ID。 | 44*** |
| NodeFrom | long | 边的起点节点ID。 | 44*** |
| Status | long | 任务流状态，返回值如下： 0：无效 1：无调度配置 2：等待调度 | 2 |
| CanEdit | boolean | 任务流是否支持编辑，返回值如下： true：支持修改 false：不支持修改 | true |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "D9D91166-A626-5F4E-9CA6-7AB10C59DBD8",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true,
  "TaskFlowGraph": {
    "DagName": "test",
    "Nodes": {
      "Node": [
        {
          "DagId": 0,
          "NodeId": 0,
          "NodeName": "test",
          "NodeType": 36,
          "NodeContent": "{ODI3OTNRVC****UHVFT29\"}",
          "TimeVariables": "{\\\"variables\\\":
[{\\\"name\\\":\\\"Today\\\",\\\"pattern\\\":\\\"yyyy-MM-dd|+1d\\\"}]}",
          "NodeConfig": "
{\\\"dbId\\\":39****,\\\"dbType\\\":\\\"mysql\\\",\\\"locale\\\":\\\"zh\\\",\\\"sql\\\":\
```

`"/*` 请确认以下`SQL`符合您的变更需求，务必确认无误后再提交执行 */\\\\n\\\\nCREATE TABLE IF NOT EXIS

```json
TS `momo_weekGather` (\\\\n\\\\t`id` bigint AUTO_INCREMENT DEFAULT '0',\\\\n\\\\t`age` bit NULL,\\\\n\\\\t`action` varchar(150) NULL,\\\\n\\\\t`elapse_time` datetime NULL,\\\ \n\\\\tPRIMARY KEY (`id`)\\\\n) ENGINE=InnoDB\\\\nDEFAULT CHARACTER SET=utf8;\\\"}",
          "GraphParam": "
{\\\"x\\\":541,\\\"y\\\":322,\\\"layoutType\\\":\\\"Horizontal\\\"}"
        }
```

]

```json
    },
    "Edges": {
      "Edge": [
        {
          "DagId": 0,
          "Id": 0,
          "NodeEnd": 0,
          "NodeFrom": 0
        }
```

]

```json
    },
    "Status": 2,
    "CanEdit": true
  }
}
```

#### UpdateTaskFlowEdges

批量更新指定任务流的指定边的起点节点和终点节点。

**接口说明**

更新的边需要满足以下限制，否则将无法成功更新：
1. 指定的边存在于DagId指定的任务流DAG图中。
2. 指定的边端点存在于DagId指定的任务流DAG图中。
数据管理
3. 更新后，DAG图不出现环。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 15*** |
| Edges | array | 是 | 更新后的任务流边列表。 |  |
|  | object | 否 |  |  |
| Id | long | 是 | 任务流边ID。 | 24*** |
| NodeEnd | long | 是 | 边的终点节点ID。 | 44*** |
| NodeFrom | long | 是 | 边的起点节点ID。 | 44*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求的ID，可用于定位日志，排查问题。 | 93FC1AE1-EC54-52B1- B146-650180FB82E8 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

数据管理

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "93FC1AE1-EC54-52B1-B146-650180FB82E8",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### UpdateTaskFlowOwner

**接口说明**

转交限制：新的任务流Owner必须在同一租户下。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，任务流的唯一标识。可通过调用ListTaskFlowIns tance接口获取该参数的值。 | 15*** |
| NewOwnerId | string | 是 | 新Owner的用户 ID。可通过调用接口GetUser获取 UserId的值。 | 51**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | 482C61C1-2537-5BFB- 8E58-34D9F17AD3C3 |

数据管理

| ErrorCode | string | 错误码。 | UnknownError |
|---|---|---|---|
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "482C61C1-2537-5BFB-8E58-34D9F17AD3C3",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### UpdateTaskFlowSchedule

**接口说明**

该接口用于更新编辑态任务流的调度设置。可配置**定时调度**、**周期调度**、**事件调度**；其中**定时调度**可配置调度一次或周期调度，**事件调度**可配置的订阅包括任务流和任务流节点。配置更新后，将任务流重新发布并部署，新的任务流实例将按照配置的调度设置进行调度。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，任务流的唯一标识。 | 7*** |
| ScheduleSwitch | boolean | 是 | 是否开启调度。 true false | false |

数据管理

| CronBeginDate | string | 否 | 此时间点之前任务流不进行调度。 | CronBeginDate t _ est |
|---|---|---|---|---|
| CronEndDate | string | 否 | 定时调度结束时间，此时间点之后任务流不进行调度。 | CronEndDate tes _ t |
| ScheduleParam | string | 是 | 事件调度配置，JSON字符串格式。 | ScheduleParam t _ est |
| CronStr | string | 否 | 定时调度Cron。 | CronStr test _ |
| TriggerType | string | 是 | 触发类型，取值如下： Cron：定时调度 Event：事件触发 | Event |
| CronType | string | 否 | 调度周期类型。取值如下： HOUR：小时级调度 DAY：日级调度 WEEK: 周级调度 MONTH：月级调度 | HOUR |
| TimeZoneId | string | 否 | 时区设置，默认为东八区 （Asia/Shanghai ）。 | Asia/Shanghai |

**调度配置相关参数说明**

配置定时调度：可配置周期调度或调度一次。 必填参数如下： ScheduleSwitch：True TriggerType：Cron CronBeginDate CronEndDate CronStr CronType ScheduleParam：分为按天、周、月、调度一次。 数据管理示例如下：

**按“天”调度：**

```json
{
    "triggerType":"0",
    "dateTime":"00:00"
}
```

按“周”**调度**：周日为1，周一为2，…，周六为7。

```json
{
    "triggerType":"0",
    "dateWeek":[
        "1",
        "5"
```

`],`

```json
    "weekTime":"00:00"
}
```

**按“月”调度：**

```json
{
    "triggerType":"0",
    "dateMonth":"1",
    "MonthTime":"00:00"
}
```

**调度一次：**

```json
{
    "triggerType":"1",
    "specificTime":"2022-09-02 00:00"
}
```

**参数说明**

1. CronStr：任务流实际调度以CronStr指定为准。
2. CronBeginDate和CronEndDate：周期调度时，CronBeginDate、CronEndDate及CronStr共同定义
了任务流调度。若CronStr指定的时间点在CronBeginDate、CronEndDate的时间范围内，任务将被触发。
3. CronType：验证使用，按照CronStr定义的周期填写。
4. ScheduleParam：需按照CronStr指定的调度填写。
**配置事件调度**（跨任务流自动触发）
必填参数如下： ScheduleSwitch：True TriggerType： Event ScheduleParam 示例如下： 数据管理

```
{
```

`"triggerType":"2" //` 事件调度时置为2 `"deps":[ //` 任务流、节点订阅配置

```
        {
```

`"eventType":1, //` 订阅类型`: 0`为任务流; 1为任务节点 `"lisDagId":12345, //` 订阅节点所在的任务流 `"lisNodeId":2134 //` 订阅节点的`Id`

```json
        },
        {
            "eventType":0,
```

`"lisDagId":12343 //` 订阅任务流的`Id`

```json
        },
        {
            "eventType":0,
            "lisDagId":23456
        }
```

`],` `"maxWait":21600 //` 在所有以上订阅运行成功前，最大等待时间

```
}
```

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | 返回参数详情如下。 |  |
| RequestId | string | 请求ID，用于定位日志， 排查问题。 | 7BF38A13-C181-5B5E- 97F1-8643F8A10093 |
| ErrorCode | string | 错误码。 | InvalidParameterValid |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | InvalidParameterValid |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "7BF38A13-C181-5B5E-97F1-8643F8A10093",
  "ErrorCode": "InvalidParameterValid",
  "ErrorMessage": "InvalidParameterValid",
  "Success": true
}
```

#### UpdateTaskFlowRelations

**接口说明**

此接口为全量更新接口。如需增量调整，请参考：AddTaskFlowEdges、UpdateTaskFlowEdges、DeleteTaskFlowEdgesByCondition。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 15*** |
| Edges | array | 否 | 待更新的任务流边列表。 |  |
|  | object | 否 |  |  |
| Id | long | 否 | 任务流边ID。 | 24*** |
| NodeEnd | long | 否 | 边的终点节点ID。 | 44*** |
| NodeFrom | long | 否 | 边的起点节点ID。 | 44*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |

数据管理

| RequestId | string | 请求ID。用于定位日志， 排查问题。 | 15D9E71C-405B- 57D7-BE6E- 707C2C7A8E0B |
|---|---|---|---|
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "15D9E71C-405B-57D7-BE6E-707C2C7A8E0B",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### UpdateTaskFlowNotification

调用UpdateTaskFlowNotification接口，更新任务流通知设置。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，任务流的唯一标识。可通过调用ListTaskFlow接口获取该参数的值。 | 15*** |
| DagNotificationFa il | boolean | 是 | 任务流运行失败通知开关。默认关闭，请手动开启。 | true |

数据管理

| DagNotificationS uccess | boolean | 是 | 任务流运行成功通知开关。默认关闭，请手动开启。 | true |
|---|---|---|---|---|
| DagNotificationSl a | boolean | 是 | 任务流SLA通知全局开关。默认关闭， 请手动开启。 | true |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object |  |  |
| RequestId | string | 请求ID。用于定位日志， 排查问题。 | 3BDC762F-2525-5E47- 8748-D6C58BDB3B38 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值说明如下： true：请求成功。 false：请求失败。 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "3BDC762F-2525-5E47-8748-D6C58BDB3B38",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### ListTasksInTaskFlow

**请求参数**

数据管理

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 32*** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | 返回参数详情如下。 |  |
| RequestId | string | 请求ID，用于定位日志， 排查问题。 | 8B36B063-6B7D-5595- 9FCF-3844B7B7ACD4 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | 任务流不存在或没有权限 |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| Tasks | array | 任务列表。 |  |
|  | object | 任务列表详情如下。 |  |
| NodeName | string | 节点名称。 | Cross-Database Spark SQL-1 |
| NodeType | string | 任务节点类型，返回值请参见NodeType参数说明。 | 单实例SQL |

数据管理

| NodeContent | string | 节点配置内容。 | { "dbId":123456, // 数据库Id "sql":"/* 请使用当前节点所选择的数据库语法编写SQL */", // sql语句 "dbType":"polardb" // 数据库类型 } |
|---|---|---|---|
| TimeVariables | string | 节点变量（时间变量配置）。 | { "variables":[ // "variables"为固定值 { "name":"var", // name 指定变量名 "pattern":"yyyy-MM- dd\|+0m+0h- 2d+0w+0M+1y" // 见后面解释 } ] } |
| NodeConfig | string | 节点高级配置。 | { "rerun":{ // 必填固定值 "rerunEnable":true, // 是否开启重跑 "rerunCount":1, // 重跑次数 "rerunInterval":10 // 重跑间隔 } } |
| NodeOutput | string | 任务输出变量。 | { "outputs":[ { /* 变量提取设置 { "row":0, // 行，-1为所有行 "column":-1, // 列，-1为所有列 /* 分隔符当选中所有行或所有列时，需要指定连接符。变量返回值为字符串 */ "combiner":"," } */ "extractMethod":" {\"row\":0,\"column\":- 1,\"combiner\":\",\"}", "variableName":"var", // 变量名 "description":"For demo" // 变量介绍 } ] } |
| GraphParam | string | 节点在图上的显示位置。 | {\"x\":435,\"y\":192,\"l ayoutType\":\"Horizont al\"} |
| NodeId | string | 节点ID。 | 92*** |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "8B36B063-6B7D-5595-9FCF-3844B7B7ACD4",
  "ErrorCode": "UnknownError",
```

`"ErrorMessage": "`任务流不存在或没有权限`",`

```json
  "Success": true,
  "Tasks": {
    "Task": [
      {
        "NodeName": "Cross-Database Spark SQL-1",
        "NodeType": "SPARK_SQL",
        "NodeContent": "{     \"dbId\":123456, // 数据库Id     \"sql\":\"/* 请使用当前节点
```

所选择的数据库语法编写SQL */\", // sql语句 \"dbType\":\"polardb\" // 数据库类型 `}",`

```json
        "TimeVariables": "{   \"variables\":[     // \"variables\"为固定值     {
\"name\":\"var\", // name指定变量名 \"pattern\":\"yyyy-MM-dd|+0m+0h-2d+0w+0M+1y\" /
```

/ 见后面解释 `} ] }",`

```json
        "NodeConfig": "{     \"rerun\":{ // 必填固定值         \"rerunEnable\":true, // 是
```

否开启重跑 \"rerunCount\":1, // 重跑次数 \"rerunInterval\":10 // 重跑间隔

```json
} }",
        "NodeOutput": "{     \"outputs\":[         {             /*             变量提取设
置 { \"row\":0, // 行，-1为所有行 \"column\":-1
```

`, //` 列，`-1`为所有列 `/*` 分隔符当选中所有行或所有列时，需要指定连接符。变量返回值为字符串 `*/`

```json
\"combiner\":\",\" } */ \"extractMethod\":\"{\\\"row \\\":0,\\\"column\\\":-1,\\\"combiner\\\":\\\",\\\"}\", \"variableName\":\"var\", // 变量名 \"description\":\"For demo\" // 变量介绍 } ] }",
        "GraphParam": "
{\\\"x\\\":435,\\\"y\\\":192,\\\"layoutType\\\":\\\"Horizontal\\\"}",
        "NodeId": "92***"
      }
```

]

```
  }
}
```

#### CreateTaskFlow

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID，可通过调用接口ListUserTenant s获取该参数的值。 | 3*** |
| DagName | string | 是 | 任务流名称。 | Dag Name _ |

数据管理

| Description | string | 否 | 任务流描述。 | zht test _ |
|---|---|---|---|---|
| ScenarioId | long | 否 | 应用场景ID。 | 2** |

DagName具有唯一性，指定已存在的DagName会导致调用失败。

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | 返回参数详情如下。 |  |
| RequestId | string | 请求ID。此次请求的唯一标识，用于定位日志，排查问题。 | 19DA51A9-AC3E- 5C36-8351- 07EBCD2B89A1 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | User can not access to Tenant [1] |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| DagId | long | 任务流ID，任务流的唯一标识。 | 33*** |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "19DA51A9-AC3E-5C36-8351-07EBCD2B89A1",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "User can not access to Tenant [1]",
  "Success": true,
  "DagId": 0
}
```

#### SuspendTaskFlowInstance

数据管理

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 7*** |
| DagInstanceId | long | 是 | 任务流运行记录 ID，可通过调用接口ListTaskFlowIns tance获取该参数的值。 | 47**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | Schema of Response |  |
| RequestId | string | 请求ID，用于定位日志， 排查问题。 | 028BF827-3801-5869- 8548-F4A039256305 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式数据管理

```json
{
  "RequestId": "028BF827-3801-5869-8548-F4A039256305",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### ReRunTaskFlowInstance

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 7*** |
| DagInstanceId | long | 是 | 任务流运行记录 ID（Id），可通过调用接口ListTaskFlowIns tance获取该参数的值。 | 47**** |
| DagVersion | string | 是 | 任务流版本号，可调用ListDAGVersion s接口获取该参数的值。 | 2**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | 返回参数值如下。 |  |
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | 8CFF2295-8249-5287- B888-DBD4F0D76CB0 |
| ErrorCode | string | 错误码。 | UnknownError |

数据管理

| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
|---|---|---|---|
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "8CFF2295-8249-5287-B888-DBD4F0D76CB0",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### MakeTaskFlowInstanceSuccess

调用MakeTaskFlowInstanceSuccess接口，将指定任务流的状态设置为成功。

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 7*** |
| DagInstanceId | long | 是 | 任务流运行记录 ID，可通过调用接口ListTaskFlowIns tance获取该参数的值。 | 47**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|

数据管理

|  | object | 返回参数如下。 |  |
|---|---|---|---|
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | 028BF827-3801-5869- 8548-F4A039256304 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "028BF827-3801-5869-8548-F4A039256304",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### DeleteTask

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| NodeId | string | 是 | 待删除任务流节点的ID。 | 54**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|

数据管理

|  | object | 返回参数详情如下。 |  |
|---|---|---|---|
| RequestId | string | 请求ID。 | 3B460770-40D9-5F07- B68A-173D1D708B72 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | Unknown server error |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "3B460770-40D9-5F07-B68A-173D1D708B72",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "Unknown server error",
  "Success": true
}
```

#### PublishAndDeployTaskFlow

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 36*** |
| VersionComment s | string | 否 | 任务流版本描述。 | vc test _ |

数据管理

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | 返回参数详情如下。 |  |
| RequestId | string | 请求的ID。用于定位日志，排查问题。 | A7160423-2A83-592B- 97E2-D8AE7B11C520 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | Unknown server error |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| DeployId | long | 部署记录ID。 | 61*** |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "A7160423-2A83-592B-97E2-D8AE7B11C520",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "Unknown server error",
  "Success": true,
  "DeployId": 0
}
```

#### StopTaskFlowInstance

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |

数据管理

| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 7*** |
|---|---|---|---|---|
| DagInstanceId | long | 是 | 任务流运行记录 ID，可通过调用接口ListTaskFlowIns tance获取该参数的值。 | 47**** |

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|
|  | object | 返回参数详情如下。 |  |
| RequestId | string | 请求ID，用于定位日志， 排查问题。 | 028BF827-3801-5869- 8548-F4A039256308 |
| ErrorCode | string | 错误码。 | UnknownError |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | UnknownError |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "028BF827-3801-5869-8548-F4A039256308",
  "ErrorCode": "UnknownError",
  "ErrorMessage": "UnknownError",
  "Success": true
}
```

#### CreateTask

数据管理

**请求参数**

| 名称 | 类型 | 必填 | 描述 | 示例值 |
|---|---|---|---|---|
| Tid | long | 否 | 租户ID。 | 3*** |
| DagId | long | 是 | 任务流ID，可通过调用接口ListTaskFlow获取该参数的值。 | 7*** |
| NodeName | string | 是 | 任务节点名称。 | zhttest |
| NodeType | string | 是 | 任务节点类型，取值请参见NodeType参数说明。 | 32 |
| NodeContent | string | 否 | 节点配置内容。 | test |
| TimeVariables | string | 否 | 节点变量（时间变量配置）。 | test |
| NodeOutput | string | 否 | 任务输出变量。 | test |
| GraphParam | string | 否 | 节点在图上的显示位置。您可通过调用GetTaskFlowGr aph接口获取该参数的值。 | test |

节点配置相关参数说明根据节点类型的不同，节点的配置有所区别。此文档为任务流任务相关接口，如CreateTask、 UpdateTaskOutput等接口的补充说明，其中NodeParam、NodeContent、GraphParam的配置具有通用性。当前仅“单实例SQL赋值”、“脚本代码”、“Ecs远程命令”任务节点具有输出变量，配置方式有所区

**单实例SQL**

DagId NodeName NodeType: 1 NodeParam GraphParam NodeContent: 样例如下数据管理

```json
{
    "dbId":123456, // 数据库Id
```

`"sql":"/*` 请使用当前节点所选择的数据库语法编写`SQL */", // sql`语句 `"dbType":"lindorm_sql" //` 数据库类型

```
}
```

**脚本代码**

DagId NodeName NodeType: 28 NodeParam GraphParam NodeOutput

```json
{
    "outputs":[
        {
            "extractMethod":"json", // 固定为json
            "variableName":"var",  // 变量名
            "description":"demo desc" // 变量描述
        }
```

]

```
}
```

NodeContent：样例如下

```json
{
    "regionId":"cn-hangzhou", // 地域
    "gatewayId":"dg-xxxxxxxxxxxxxx", // 网关ID
    "gatewayInstanceId":"dg-node-xxxxxxxxxxxxxx", // 网关实例ID
    "scriptFileName":"demo.sh", // 文件名
```

`"args":[ //` 运行参数

```
        "-n value",
        "-n1 value1"
```

]

```
}
```

**无锁数据变更**

DagId NodeName NodeType: 24 NodeParam GraphParam NodeContent: 样例如下数据管理

```json
{
    "dbId":123456, // 数据库Id
```

`"sql":"/*` 请使用当前节点所选择的数据库语法编写`SQL */", // sql`语句 `"dbType":"polardb" //` 数据库类型

```
}
```

**单实例SQL赋值**

DagId NodeName NodeType: 32 NodeParam GraphParam NodeOutput: 样例如下

```json
{
    "outputs":[
        {
```

`/*` `//` 变量提取设置

```
            {
```

`"row":0, //` 行，`-1`为所有行 `"column":-1, //` 列，`-1`为所有列 `"combiner":"," //` 分隔符,当选中所有行或所有列时，需要指定连接符。变量返回值为字符串

```
            }
```

`*/`

```json
            "extractMethod":"{\"row\":0,\"column\":-1,\"combiner\":\",\"}",
            "variableName":"var", // 变量名
            "description":"For demo" // 变量介绍
        }
```

]

```
}
```

NodeContent: 样例如下

```json
{
    "dbId":123456, // 数据库Id
```

`"sql":"/*` 请使用当前节点所选择的数据库语法编写`SQL`，仅支持`SELECT`语句，且默认返回最大行数为`30 *",` `// sql`语句 `"dbType":"lindorm_cql" //` 数据库类型

```
}
```

**依赖检查**

DagId NodeName NodeType: 2 NodeParam 数据管理 GraphParam NodeContent: 样例如下

```
{
```

`"dependentDAGId":132, //` 依赖项：任务流 `"dependentNodeId":"", //` 依赖项：单个节点，缺省时依赖项为指定的任务流

```json
    "dependentStartTimePattern":"yyyy-MM-dd HH:mm|-2d+0h+0m", // 开始时间偏移点
    "dependentEndTimePattern":"yyyy-MM-dd HH:mm|+1d+0h+0m", // 结束时间偏移点
```

`"multiSuccessStrategy":2, //` 实例检查策略： `0.`最后一次成功； `1.`全部成功； `2.`指定单次成功 `"multiSuccessStrategyIndex":1 //` 实例检查策略：第 `x+1` 次

```
}
```

**表时间列状态检查**

DagId NodeName NodeType: 2 NodeParam GraphParam NodeContent: 样例如下

```
{
```

`"dependentDAGId":132, //` 依赖项：任务流 `"dependentNodeId":"", //` 依赖项：单个节点，缺省时依赖项为指定的任务流

```json
    "dependentStartTimePattern":"yyyy-MM-dd HH:mm|-2d+0h+0m", // 开始时间偏移点
    "dependentEndTimePattern":"yyyy-MM-dd HH:mm|+1d+0h+0m", // 结束时间偏移点
```

`"multiSuccessStrategy":2, //` 实例检查策略： `0.`最后一次成功； `1.`全部成功； `2.`指定单次成功 `"multiSuccessStrategyIndex":1 //` 实例检查策略：第 `x+1` 次

```
}
```

**SQL状态检查**

DagId NodeName NodeType: 25 NodeParam GraphParam NodeContent: 样例如下

```json
{
    "dbId":123456,
```

`"sql":"/*` 请使用当前节点所选择的数据库语法编写SQL */ \n\n select 1 from abc",

```json
    "dbType":"lindorm_cql"
}
```

**返回参数**

| 名称 | 类型 | 描述 | 示例值 |
|---|---|---|---|

数据管理

|  | object | 返回参数值如下。 |  |
|---|---|---|---|
| RequestId | string | 请求ID，用于定位日志， 排查问题。 | CFD8FE00-36D9-4C1B- 940D-65A7B73D9066 |
| ErrorCode | string | 错误码。 | InvalidParameterValid |
| ErrorMessage | string | 调用失败时，返回的错误信息。 | InvalidParameterValid |
| Success | boolean | 请求是否成功，返回值如下： true：请求成功 false：请求失败 | true |
| NodeId | long | 创建成功时，返回的任务节点ID。 | 3*** |

**示例**

正常返回示例 `JSON` 格式

```json
{
  "RequestId": "CFD8FE00-36D9-4C1B-940D-65A7B73D9066",
  "ErrorCode": "InvalidParameterValid",
  "ErrorMessage": "InvalidParameterValid",
  "Success": true,
  "NodeId": 0
}
```

### 逻辑库表

#### GetDBTopology

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据管理

| LogicDbId | Long | 是 | 134325 | 逻辑库ID。 说明您可以通过调用ListLogicDatabases接口获取该参数。 |
|---|---|---|---|---|
| Tid | Long | 否 | 3*** | 租户ID。 |
| RegionId | String | 否 | cn-hangzhou | 选择DMS的服务地域。 说明请根据应用所在地就近选择。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | C5B8E84B-42B6- 4374-AD5A- 6264E1753378 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrorMessage | String | UnknownError | 错误信息。 |
| ErrorCode | String | UnknownError | 错误码。 |
| DBTopology | object |  | 拓扑信息 |
| LogicDbId | Long | 1234 | 逻辑库ID。 |
| LogicDbName | String | logic db test _ _ | 逻辑库名。 |
| SearchName | String | logic db test _ _ | 逻辑库搜索名。 |
| Alias | String | logic db test _ _ | 逻辑库别名。 |
| DbType | String | polardb | 数据库类型。 |

数据管理

| EnvType | String | dev | 逻辑库的环境类型，取值： product：生产环境 dev：开发环境 pre：预发环境 test：测试环境 sit：SIT环境 uat：UAT环境 pet：压测环境 stag：STAG环境 |
|---|---|---|---|
| DBTopologyInf oList | Array of DBTopologyInf o |  | 分库拓扑信息列表。 |
| DbId | Long | 423532 | 库ID。 |
| SchemaName | String | db test@rm- _ xxx:3306 | 库名。 说明若数据库类型是PG系列，此处为PG模式名。 |
| CatalogName | String | def | 数据库目录名。 说明若数据库类型为PG系列，此处表示PG数据库名。 |
| SearchName | String | db test _ | 库搜索名。 |
| DbType | String | polardb | 数据库类型。 |
| EnvType | String | dev | 逻辑库的环境类型，取值： product：生产环境 dev：开发环境 pre：预发环境 test：测试环境 sit：SIT环境 uat：UAT环境 pet：压测环境 stag：STAG环境 |
| InstanceId | Long | 4325325 | 实例ID。 |
| RegionId | String | cn-hangzhou | 实例所在地域。 |

数据管理

| InstanceResou rceId | String | rm-xxx | 实例资源ID，取值： RDS：阿里云数据库实例ID ECS OWN：阿里云ECS实例ID _ PUBLIC OWN：空 _ VPC ID：VPC ID _ GATEWAY：数据库网关实例ID |
|---|---|---|---|
| InstanceSourc e | String | RDS | 实例来源，取值： RDS：阿里云数据库实例 ECS OWN：阿里云ECS自建库实例 _ PUBLIC OWN：公网自建库实例 _ VPC ID：VPC专线IDC数据库实例 _ GATEWAY：数据库网关实例 |

**示例**

请求示例

```
http(s)://dms-enterprise.aliyuncs.com/?Action=GetDBTopology &Tid=43215
```

&公共请求参数正常返回示例 `XML` 格式数据管理

```xml
HTTP/1.1 200 OK Content-Type:application/xml <RequestId>C5B8E84B-42B6-4374-AD5A-6264E1753378</RequestId> <Success>true</Success> <ErrorMessage>UnknownError</ErrorMessage> <ErrorCode>UnknownError</ErrorCode> <DBTopology>
    <LogicDbId>1234</LogicDbId>
    <LogicDbName>logic_db_test</LogicDbName>
    <SearchName>logic_db_test</SearchName>
    <Alias>logic_db_test</Alias>
    <DbType>polardb</DbType>
    <EnvType>dev</EnvType>
    <DBTopologyInfoList>
        <DbId>423532</DbId>
        <SchemaName>db_test@rm-xxx:3306</SchemaName>
        <CatalogName>def</CatalogName>
        <SearchName>db_test</SearchName>
        <DbType>polardb</DbType>
        <EnvType>dev</EnvType>
        <InstanceId>4325325</InstanceId>
        <RegionId>cn-hangzhou</RegionId>
        <InstanceResourceId>rm-xxx</InstanceResourceId>
        <InstanceSource>RDS</InstanceSource>
    </DBTopologyInfoList>
</DBTopology>
```

`JSON` 格式数据管理

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId" : "C5B8E84B-42B6-4374-AD5A-6264E1753378",
  "Success" : true,
  "ErrorMessage" : "UnknownError",
  "ErrorCode" : "UnknownError",
  "DBTopology" : {
    "LogicDbId" : 1234,
    "LogicDbName" : "logic_db_test",
    "SearchName" : "logic_db_test",
    "Alias" : "logic_db_test",
    "DbType" : "polardb",
    "EnvType" : "dev",
    "DBTopologyInfoList" : [ {
      "DbId" : 423532,
      "SchemaName" : "db_test@rm-xxx:3306",
      "CatalogName" : "def",
      "SearchName" : "db_test",
      "DbType" : "polardb",
      "EnvType" : "dev",
      "InstanceId" : 4325325,
      "RegionId" : "cn-hangzhou",
      "InstanceResourceId" : "rm-xxx",
      "InstanceSource" : "RDS"
    } ]
  }
}
```

数据管理

## 附录

### NodeType参数说明

| 任务节点类型 | NodeType |
|---|---|
| 单实例SQL | 1 |
| 任务流依赖检查 | 2 |
| 表时间列状态检查 | 17 |
| 无锁数据变更 | 24 |
| SQL状态检查 | 25 |
| 条件分支 | 31 |
| 单实例SQL赋值 | 32 |
| SSH远程命令 | 45 |
| Impala | 46 |

### STS概要

#### 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

**使用RAM用户扮演角色时获取STS Token**

有权限的RAM用户可以使用其访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用STS Token访问阿里云资源。

**产品优势**

使用STS Token，减少长期访问密钥（Accesskey）泄露的风险。 STS Token具有时效性，可以自定义有效期，到期后将自动失效，无需定期轮换。 可以为STS Token绑定自定义权限策略，提供更加灵活和精细的云资源授权。 数据管理

#### AssumeRole

RAM用户调用AssumeRole接口获取一个扮演RAM角色的临时身份凭证STS Token。该接口中RAM用户扮演的是可信实体为阿里云账号类型的RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssumeRole | 要执行的操作。取值：AssumeRole |
| RoleArn | String | 是 | acs:ram::123456 789012****:role/ adminrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM 角色。 |
| RoleSessionNa me | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-） 和下划线（ ）。 _ |
| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 如果指定该权限策略，则STS Token最终的权限策略取RAM角色权限策略与该权限策略的交集。 如果不指定该权限策略，则STS Token最终的权限策略取RAM角色的权限策略。 长度为1~1024个字符。 |

**返回结果**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | 无 | 无 | 访问凭证。 |

数据管理

| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | 访问密钥ID。 |
|---|---|---|---|
| AccessKeySecret | String | ****************************************** | 访问密钥。 |
| SecurityToken | String | ******** | 安全令牌。 |
| Expiration | String | 2015-04- 09T11:52:19Z | 失效时间。 |
| AssumedRoleUser | 无 | 无 | 角色扮演时的临时身份。 |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | 临时身份的ARN。 |
| AssumedRoleId | String | 34458433936495** **:alice | 临时身份的ID。 |

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

以下代码示例为通过调用 `Sts::AssumeRole::2015-04-01` 获取STS AccessKey三元组信息。

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType;
```

数据管理

```java
import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```xml
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
```

`// "sts.aliyuns.com"`要替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`"<yourRoleSessionName>"`请替换为实际值

```
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`"<yourRoleArn>"`请替换为上一步获取到的实际`Ram Role ARN`

```
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
```

`//` 获取到`STS`三元组

```java
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: "
+ stsToken);
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

**调用示例**

下列代码以调用ECS的 `DescribeZones` 接口为示例。 数据管理

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
```

`// "<yourRegionID>"`替换为真实的`RegionID` `// "<yourStsAccesskey>", "<yourStsAccessKeySecret>"`替换为上面获取到的`STS`三元组中

```xml
stsAk、stsSk
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccessKey>", "<yourStsAccessKeySecret>");
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

数据管理

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | RoleSessionName格式错误，支持输入2~64 个字符，请输入至少2个字符，允许输入英文字母、数字、半角句号 （.）、at（@）、短划线 （-）和下划线（ ）。 _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | DurationSeconds参数设置错误，过期时间最小值为900秒，最大值为MaxSessionDurati on设置的时间。 |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | 权限策略语法错误。 |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | 权限策略长度超限，最大不超过1024字符。 |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | STS Token没有权限。 |
| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
