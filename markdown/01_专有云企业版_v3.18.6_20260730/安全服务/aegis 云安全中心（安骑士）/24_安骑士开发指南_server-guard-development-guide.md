---
title: "云安全中心（安骑士） 安骑士开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 251
source_pdf: "24_安骑士开发指南_server-guard-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/aegis/zh/server-guard-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云安全中心（安骑士） 安骑士开发指南

## 快速入门

### 开发文档使用说明

本文为您介绍在使用专有云API进行开发工作时，如何查看所需要的产品文档。

**使用流程**

您可以按照以下流程图中步骤，判断自己所需要使用的开发文档。

**前提条件**

通过运维人员或运营管理员获取专有云的版本。

**操作步骤**

您可以通过阿里云专有云文档中心，获取需要的产品文档。
1. 通过浏览器打开专有云文档中心。
2. 根据专有云的版本单击**飞天企业版**、**敏捷版****&XStack**或**一体机**标签。
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍如何通过POP网关调用专有云API。

**流程图**

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrga nizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListRe sourceGroup章节。

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。

## 准备工作

### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

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

**说明**

Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

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

请各云产品自行修改替换产品名及获取实例ID流程实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以ECS为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**弹性计算**>**云服务器****ECS**。
3. 在左侧导航栏中，单击**实例**。
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

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及Security Token三元组组成，使用STS方式调用云产品API时，三元组缺一不可。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourAccessKeyID>：请替换为您实际的AccessKey ID。 <yourAccessKeySecret>：请替换为您实际的AccessKey Secret。 <yourRoleSessionName>：请替换为您当前实际的会话名称。 该名称为用户自定义，通常设置为调用该API的用户身份，例如：用户名。在同一个RAM角色执行的操作中，可以根据不同的 `RoleSessionName` 来区分实际操作者，以实现用户级别的访问审计。长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-）和下划线（_）。 <yourRoleArn>：请替换为您实际的RAM Role。 "sts.aliyuns.com" ：请替换为实际的STS Endpoint。

```
public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。 `//` 请替换为您实际的地域`ID`、`AccessKey ID`、`AccessKey Secret`。

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

`//` 获取到`STS`三元组。

```java
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
} private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
```

`// "sts.aliyuns.com"` 请替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}。
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`"<yourRoleSessionName>"`请您替换为实际值。

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`"<yourRoleArn>"`请替换为上一步获取到的实际`Ram Role ARN`。

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

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourStsAccesskeyID>：请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>：请替换为您实际的STS Accesskey Secret。 <yourStsToken>：请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>：请替换为您实际的资源集ID。 <yourOrganizationID>：请替换为您实际的组织ID。

```
public static void main(String[] args) {
```

`// "<yourRegionID>"`请替换为您实际的地域`ID`。 `// "<yourStsAccessKeyID>"`、`"<yourStsAccessKeySecret>"`请替换为前一步获取到的`STS`三元组中

```xml
AccessKeyID、AccessKeySecret。
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

`//"<yourRegionID>"` 请替换为您实际的地域`ID`。

```
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
```

`// "<yourStsToken>"` 请替换为您前一步获取到的`STS`三元组中`SecurityToken`。

```
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
```

`//` 非必填，请替换为您实际的资源集`ID`。

```
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 非必填，请替换为您实际的组织`ID`。

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

## 调用示例

### Java SDK调用示例

#### 快速开始

本节介绍如何获取产品名Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体信息，请参见获取AccessKey，并在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用云盾的开发工具包，必须安装SDK核心库。其中，SDK核心库推荐使用4.5.17及以上版本。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your-region-id>，请替换为您实际的地域ID。 <your-access-key-id>，请替换为您实际的AccessKey ID。 <your-access-key-secret>>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您当前产品实际的Endpoint。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // 您的地域ID
            "<your-access-key-id>",      // 您的AccessKey ID
            "<your-access-key-secret>"); // 您的AccessKey Secret
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```
        CommonRequest request = new CommonRequest();
```

request.setDomain("<your-endpooint>");// 当前产品的服务地址

```java
        request.setVersion("<API-version>");// 接口的版本
        request.setAction("<your-action>");// 接口的名称
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
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

#### 使用手册

##### 安装Java SDK

本文介绍如何安装及调用云盾Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用云盾的开发工具包，必须安装阿里云Java SDK核心库。SDK核心库推荐使用4.5.17及以上版本。 您在安装阿里云Java SDK核心库时，需要在pom.xml文件中添加以下依赖。关于准确的SDK版本号，请参见阿里云开发工具包（SDK）。

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 使用CommonRequest进行调用

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **API****调试**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```xml
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
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

ROA调用，示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException;
```

```java
import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```xml
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
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

`//` 设置`HTTPS`访问

```
        request.setSysProtocol(ProtocolType.HTTP);
```

`//` 设置请求方式

```
        request.setSysMethod(MethodType.GET);
```

`//` 设置云产品`endpoint`

```
        request.setSysDomain("<crEndpoint>");
```

`//` 设置访问接口版本

```
        request.setSysVersion("2016-06-07");
```

`//` 设置`uriPattern` 只有`roa`调用需要传递此字段

```
        request.setSysUriPattern("/namespace");
        // 设置LocationProduct
        request.setSysLocationProduct("cr");
```

`//` 设置访问接口的名称

```
        request.setSysAction("GetNamespaceList");
```

`//` 必填值，调用来源说明

```
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
```

`//` 非必填，企业版`V3.15.0`之前历史版本需要

```
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
```

`//` 非必填,资源集`ID`

```
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
```

`//` 必填,组织`ID`

```
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
```

`//` 非必填，修改&删除操作需要

```
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
```

`//` 当使用`STS AK`调用`ROA`接口时需要在`Header`加上`x-acs-security-token`字段

```
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
try{
```

```
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

**重要**

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL/TLS 证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过以下参数设置： Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

`//` 设置不校验服务端证书

```
clientConfig.setIgnoreSSLCerts(true)
```

### Python SDK调用示例

#### 快速开始

本节介绍如何获取Python SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体信息， 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

**使用Python SDK**

以下示例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。
在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your_region_id>，请替换为您实际的地域ID。 <your_access_key_id>，请替换为您实际的AccessKey ID。 <your_access_key_secret>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您实际的产品访问地址。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}','{your_access_key_secret}', '{your_region_id}') request = CommonRequest()
```

`request.set_domain('<your-endpoint>') #` 当前产品的服务地址

```bash
request.set_version('<API-version>') # 接口的版本 request.set_action_name('<your-action>')# 接口的名称
# 或者request = CommonRequest(domain='<your-endpoint>', version='<API-version>',action
_name='<your-action>') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

#### 使用手册

##### 安装Python SDK

本文档介绍如何安装及调用Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。 使用产品的开发工具包，都必须安装阿里云Python SDK核心库。

**说明**

如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

##### 使用CommonRequest进行调用

本文为您介绍POP Python SDK调用云产品API的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **API****调试**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

目前仅支持通过RPC方式调用API。

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
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
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

#非必填
资源集`ID`
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

调用API时您或许需要通过环境变量设置HTTP_PROXY、HTTPS_PROXY。 示例代码如下：
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

### Go SDK调用示例

#### 快速开始

阿里云Go SDK让您不用复杂编程即可访问。本文介绍如何获取阿里云Go SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体信息， 请参见获取AccessKey，并在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。

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

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your_region_id>，请替换为您实际的地域ID。 <your_access_key_id>，请替换为您实际的AccessKey ID。 <your_access_key_secret>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您实际的产品访问地址。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。

```java
package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "fmt"
```

)

```
func main() { client, err := sdk.NewClientWithAccessKey("<your_region_id>", "{your_access_key_id}", "{your_access_key_secret}") if err != nil { panic(err)
 }
:= requests.NewCommonRequest() request.Domain = "<your-endpoint>"// 当前产品实际的Endpoint request.Version = "<API-version>"// 接口的版本 request.ApiName = "<your-action>" // 接口的名称 request.QueryParams["PageNumber"] = "1" request.QueryParams["PageSize"] = "30" response, err := client.ProcessCommonRequest(request) if err != nil { panic(err)
 }
fmt.Print(response.GetHttpContentString()) }
```

#### 使用手册

##### 安装Go SDK核心包

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### 使用CommonRequest进行调用

本文为您介绍POP Go SDK调用的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **API****调试**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 示例代码如下：

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<Ac
cessKey Secret>")
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

```xml
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "
<yourAccessSecret>")
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

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL证书有效性，若您代码环境没有证书环境， 则会报错证书校验失败。为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可参考如下内容进行设置。 `//` 设置请求 `HTTPSInsecure`（只影响当前）

```
request.SetHTTPSInsecure(true) // 设置请求 HTTPSInsecure 为 true isInsecure := request.GetHTTPSInsecure() // 获取请求 HTTPSInsecure
```

当请求未设置时，客户端设置才能生效。 `//` 设置客户端 `HTTPSInsecure`（用于客户端发送的所有请求）。

```
client.SetHTTPSInsecure(true) // 设置客户端 HTTPSInsecure 为 true isInsecure := client.GetHTTPSInsecure() // 获取客户端 HTTPSInsecure
```

## API公共参数

**公共请求参数**

公共请求参数是每个接口调用都需要提供的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | Strin g | 否 | 返回值的类型，仅支持JSON。 |
| Version | Strin g | 是 | API版本号，以日期形式YYYY-MM-DD输入，取值： 2018-01-16：Auditprivate。 2019-07-23：yundunnextsoc。 2018-12-03：Sas。 2016-11-11：aegis。 2021-10-11：yundun-css。 2019-08-05：secspy。 2018-01-16：Ddosprivate。 2018-06-30：hsm-private。 2017-12-07：Cloudfw。 2019-01-03：Sddp。 2020-07-01：semawaf。 2018-12-03：soar。 |
| AccessKeyId | Strin g | 是 | 访问服务使用的密钥ID。 |
| AccessKeySe cret | Strin g | 是 | 访问服务使用的密钥值。 |
| RegionId | Strin g | 是 | 服务所使用的地域ID。 |

| Product | Strin g | 是 | 接口对应的产品名称。取值： Auditprivate：云盾基础组件。 yundunnextsoc：云安全管理中心（SOC）。 Sas：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy：网络流量检测与响应。 Ddosprivate：DDos 清洗。 hsm-private：加密服务。 Cloudfw：云防火墙。 Sddp：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |
|---|---|---|---|
| EndpointPre | Strin g | 是 | 接口对应的域名前缀。取值： auditprivate：云盾基础组件。 yundunnextsoc-pop：云安全管理中心（SOC）。 tds：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy-share：网络流量检测与响应。 ddosprivate：DDos 清洗。 hsmprivate：加密服务。 cloudfw：云防火墙。 sddp-api：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

## API参考

### 调用方式

#### 请求结构

云盾的API是RPC风格，该章节介绍API请求格式。

**请求结构说明**

您可以通过发送HTTP请求的方式调用API，具体请求结构如下：

```
http://endpoint/?Action=xx&parameters
```

其中：

| endpoint |  |
|---|---|
| Action | ， |

例如，使用DescribeFeatures获取当前已经部署的云盾功能模块列表。 `parameters` ，表示请求参数，包括公共参数和API自定义参数，每个参数之间使用 & 分隔。 公共参数：包含API版本号、身份验证等信息。 API自定义参数：包含接口自定义的请求参数，具体参考各接口说明。

**举例说明**

调用DescribeFeatures获取当前已部署的云盾功能模块列表。

```
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-t est&Format=JSON&SecureTransport=true&SignatureMethod=HMAC- SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018- 03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

为了方便阅读，在文档中以如下格式展示API请求。

```
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2018-01-16 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 签名机制

云盾服务会对每个访问的请求进行身份验证，所以无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。

**API签名**

为保证API的安全调用，在调用API时阿里云会对每个API请求通过签名（Signature）进行身份验证。当您手动发起API请求时，需要按照RFC 2104的定义，使用AccessSecret对编码、排序后的整个请求串计算 HMAC值作为签名。 本章节以如下原始访问参数为例，说明API签名制作的流程：

| 参数 | 内容 |
|---|---|
| 接入点 | http://yundunprivate.[RegionId].example.com/? |
| API自定义参数 | Action=DescribeFeatures |
| 公共参数（不包含Signature） | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-01-16 &SignatureVersion=1.0 |
| Access Key Secret | <yourAccessKeySecret> |

1. 使用请求参数构造规范化的请求字符串（Canonicalized Query String）。

**说明**

请求参数由公共请求参数（不包括Signature参数自身）和接口自定义参数。 i. 参数排序。 按照参数名称的字典顺序对请求参数进行排序。 ii. 参数编码。 对排序之后请求参数的名称和值分别用UTF-8字符集进行URL编码。编码的规则如下： 对于字符 A-Z、a-z、0-9 以及字符“-”、“_”、“.”、“~”不编码。 对于其他字符编码成“%XY”的格式，其中 XY 是字符对应 ASCII 码的 16 进制表示。比如英文的双引号（”）对应的编码就是 %22。 对于扩展的 UTF-8 字符，编码成“%XY%ZA…”的格式。 需要说明的是英文空格（）要被编码是 %20，而不是加号（+）。 iii. 将编码后的参数名称和值用英文等号（=）进行连接。 iv. 将等号连接得到的参数组合按步骤(a)排好的顺序依次使用&符号连接，即得到规范化请求字符串。
2. 将上一步构造的规范化字符串按照下面的规则构造成待签名的字符串。

```
StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

3. 按照RFC 2104的定义，计算待签名字符串 StringToSign 的 HMAC 值。

**说明**

计算签名时使用的 Key 就是用户持有的 Access Key Secret 并加上一个 & 字符(ASCII:38)，使用的哈希算法是 SHA1。
4. 按照 Base64 编码规则把上面的 HMAC 值编码成字符串，即得到签名值（Signature）。

```
LEW8N4y7Uasop******
```

5. 将得到的签名值作为 Signature 参数添加到请求参数中，即完成对请求签名的过程。

#### 公共参数

公共参数是指每个API接口都需要使用到的请求参数，包含API版本号、身份验证等信息。

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Version | String | 是 | API版本号，为日期形式：YYYY-MM-DD。 取值：2016-11-11 |
| AccessKeyId | String | 是 | 阿里云颁发给用户的访问服务所用的密钥 ID。 |
| Signature | String | 是 | 签名结果串。 |
| SignatureMethod | String | 是 | 签名方式。 取值：HMAC-SHA1 |
| Timestamp | String | 是 | 请求的时间戳。日期格式按照ISO8601标准表示，并需要使用UTC时间。 格式为： YYYY-MM-DDThh:mm:ssZ 例如，2014-05-26T12:00:00Z（为北京时间 2014年5月26日20点0分0秒）。 |
| SignatureVersion | String | 是 | 签名算法版本。 取值：1.0 |
| SignatureNonce | String | 是 | 唯一随机数，用于防止网络重放攻击。用户在不同请求间要使用不同的随机数值。 |
| ResourceOwnerA ccount | String | 否 | 本次API请求访问到的资源拥有者账户，即登录用户名。 |
| Format | String | 否 | 返回响应的格式。 取值：JSON \| XML 说明默认值为XML。 |

#### 返回结构

云盾API返回结构支持XML和JSON两种格式。用户发送的每次接口调用请求，无论成功与否，系统都会返回一个唯一识别码**RequestId**。

**XML返回结构示例**

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

<!--结果的根结点`-->` <接口名称`+Response>` <!--返回请求标签`-->`

```xml
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
```

<!--返回结果数据`-->` `</`接口名称`+Response>`

**JSON返回结构示例**

```json
{ "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
```

`/*` 返回结果数据 `*/`

```
}
```

### 资产管理功能相关接口

#### DescribeCloudCenterInstances

调用DescribeCloudCenterInstances接口通过设置搜索条件查询符合条件的资产信息，例如通过资产实例名称、资产实例所属区域等条件搜索指定资产。目前提供分页和NextToken两种方式，推荐NextToken 方式。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- aegis:DescribeCloudCenterInsta nces | Read | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Lang | Strin g | Query | 否 | zh | 设置请求和接收消息的语言类型，默认为zh。 zh：中文。 en：英文。 |
| RegionId | Strin g | Query | 否 | cn-hangzhou | 要查询的实例所在地域的 ID。 |
| Criteria | Strin g | Query | 否 | [{"name":"riskStatus","v alue":"YES"}, {"name":"internetIp","va lue":"1.2.XX.XX"}] | 设置搜索资产的条件。该参数JSON格式，输入参数时注意大小写。 说明支持使用资产的实例ID、实例名称、所属VPC ID、地域、公网IP地址等条件搜索资产。 您可以调用DescribeCriteria接口查询支持的搜索条件。 |
| MachineT ypes | Strin g | Query | 否 | ecs | 要查询的资产的类型。取值： ecs：服务器。 cloud product：云产 _ 品。 |
| LogicalEx p | Strin g | Query | 否 | OR | 设置多个搜索条件间生效的逻辑关系。默认OR， 取值： OR：表示多个搜索条件之间是或的关系 AND：表示多个搜索条件之间是与的关系。 |
| NoPage | Boole an | Query | 否 | true | 设置是否启用分页查询。默认值为true。 取值： true：启用分页查询。 false：不启用分页查询。 |
| PageSize | Integ er | Query | 否 | 100 | 设置分页查询时，每页显示的资产的数量。默认值为 20，表示每页显示20条资产信息。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为 1，表示从第1页开始显示。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Importanc e | Integ er | Query | 否 | 2 | 设置资产重要性。 取值： 2：重要资产。 1：一般资产。 0：测试资产。 |
| ResourceS etIds | Strin g | Query | 否 | 123,456 | 资源集ID列表，多个用逗号隔开。 |
| ResourceS tatus | Strin g | Query | 否 | NORMAL | 资源状态。取值： NORMAL：正常。 DELETED：锁定。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Instances | Array |  | 资产详细信息。 |
| -InternetIp | String | 1.2.XX.XX | 实例的公网IP地址。 |
| -Os | String | Linux | 实例的操作系统。 |
| -InstanceId | String | i-m5*** | 实例ID。 |
| - InstanceName | String | yztest-l*** | 实例名称。 |
| -RegionName | String | China (Hangzhou) | 资产的地域名称。 |
| -Ip | String | 1.2.XX.XX | 实例的公网IP地址。 |
| -ClientStatus | String | online | 实例的客户端在线状态。 取值： online：在线，表示资产的Agent客户端状态为开启 offline：离线，表示资产的Agent客户端状态为关闭 pause：暂停，表示资产的Agent客户端状态为暂停保护 |
| -Region | String | cn-hangzhou- cm***-*** | 实例所属地域ID。 |
| -Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | 实例的UUID。 |

| 安骑士开发指南·AP | I参考 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -IntranetIp | String | 1.2.XX.XX | 实例的私网IP地址。 |
| -AssetType | String | 0 | 资产的类型。 取值： 0：云服务器 1：负载均衡 2：NAT网关 3：RDS数据库 4：MongoDb数据库 5：REDIS数据库 6：容器镜像 7：容器 |
| -Status | String | Running | 实例的运行状态。 取值： Running：运行中 notRunning：已关机 |
| -Tag | String | InternetIp,test | 资产实例的标签名称。 |
| -VpcInstanceId | String | vpc- uf60agqq65bs98zo o**** | 实例所属VPC的ID。 |
| -OsName | String | - | 实例的内核版本。 |
| -Flag | Integer | 0 | 实例是否为阿里云资产。 取值： 0：阿里云资产 1：非阿里云资产 |
| -HcStatus | String | YES | 实例是否检测出了基线风险项。 取值： YES：检测出了基线风险项 NO：未检测出基线风险项 |
| -VulStatus | String | YES | 实例是否存在漏洞。 取值： YES：存在漏洞 NO：不存在漏洞 |
| -AlarmStatus | String | NO | 资产是否存在安全告警。 取值： YES：存在安全告警 NO：不存在安全告警 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -RiskStatus | String | NO | 资产是否存在安全风险。 取值： YES：存在 NO：不存在 |
| - WeakPassword Status | String | NO | 是否存在弱口令。 取值： NO：无弱口令 YES：有弱口令 |
| - HealthCheckC ount | Integer | 1 | 实例中存在的基线风险数量。 |
| -VulCount | Integer | 2 | 实例上存在的漏洞数量。 |
| - SafeEventCou nt | Integer | 5 | 资产存在的安全告警数量。 |
| -RegionId | String | cn-hanghzou | 资产所在的地域的ID。 |
| -GroupId | String | 4120080 | 实例所属分组ID。 |
| -Importance | Integer | 2 | 资产的重要性。 取值： 2：重要资产 1：一般资产 0：测试资产 |
| -ClientVersion | String | 00 31 _ | 客户端版本。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -RiskCount | String | { "account": 0, "appNum": 0, "asapVulCount": 0, "baselineHigh": 0, "baselineLow": 0, "baselineMedium": 0, "baselineNum": 0, "cmsNum": 0, "containerAsap": 0, "containerLater": 0, "containerNntf": 0, "containerRemind": 0, "containerSerious": 0, "containerSuspicio us": 0, "cveNum": 0, "emgNum": 0, "health": 0, "imageBaselineHig h": 0, "imageBaselineLow ": 0, "imageBaselineMe dium": 0, "imageBaselineNu m": 0, "imageMaliciousFil eRemind": 0, "imageMaliciousFil eSerious": 0, "imageMaliciousFil eSuspicious": 0, "imageVulAsap": 0, "imageVulLater": 0, "imageVulNntf": 0, "laterVulCount": 0, "newSuspicious": 0, "nntfVulCount": 0, "remindNum": 0, "scaNum": 0, "seriousNum": 0, "suspNum": 0, "suspicious": 0, "sysNum": 0, "trojan": 0, "uuid": "inet-37316411- 37fe-4b72-b245- 346a2721****", "vul": 0, "weakPWNum": 0 } | 资产存在的风险项统计。JSON格式，包含以下字段： account：异地登录和爆破成功的账号数量 appNum：扫描器漏洞数量 asapVulCount：高危漏洞总数量 baselineHigh：高危基线风险数量 baselineLow：低危基线风险数量 baselineMedium：中危基线风险数量 baselineNum： 云产品配置风险总数量 cmsNum： WEB-CMS漏洞数量 containerAsap： 容器高危漏洞数量 containerLater：容器中危漏洞数量 containerNntf： 容器低危漏洞数量 containerRemind：容器提醒告警数量 containerSerious：容器紧急告警数量 containerSuspicious：容器可疑告警数量 cveNum：Linux 漏洞数量 emgNum：应急漏洞数量 health：未处理的基线告警数量 imageBaselineHigh：镜像高危基线风险数量 imageBaselineLow：镜像低危基线风险数量 imageBaselineMedium：镜像中危基线风险数量 imageBaselineNum：镜像基线风险总数量 imageMaliciousFileRemind：镜像提醒恶意文件数量 imageMaliciousFileSerious：镜像紧急恶意文件数量 imageMaliciousFileSuspicious：镜像可疑恶意文件数量 imageVulAsap：镜像高危漏洞数量 imageVulLater：镜像中危漏洞数量 imageVulNntf：镜像低危漏洞数量 laterVulCount：中危漏洞数量 newSuspicious：告警数量 nntfVulCount：低危漏洞数量 remindNum：提醒告警数量 scaNum：软件成分分析漏洞数量 seriousNum：紧急告警数量 suspNum：可疑告警数量 suspicious：告警总数量 sysNum：Windows漏洞数量 trojan：木马数量 uuid：资产UUID vul：漏洞数量 weakPWNum：弱口令数量。 |

| 参数名称 | 类型 | 示例 c690a0789419f428 | 说明 |
|---|---|---|---|
| -ClusterId | String | 4a4e0a29e12fe*** * | 集群ID。 |
| -ClusterName | String | cluster1 | 集群名称。 |
| -CreatedTime | Long | 1607365213000 | 集群创建的时间戳，单位为毫秒。 |
| -PodCount | Integer | 1 | 容器组个数。 |
| - ExposedStatus | Integer | 0 | 资产暴露状态。 取值： 0： 未暴露 1： 已暴露 |
| - AutoSnapshots Level | Integer | 0 | 快照恢复安全状态。 取值： 0：未知 1：安全 2：中危 3：高危 |
| - ExposedCount | Integer | 1 | 云外暴露数。 |
| - WeakPassword Count | Integer | 2 | 弱口令数。 |
| - FirstLoginTime | Long | 2023-12-11 12:41:51 | 第一次登录时间。 |
| - LastLoginTime | Long | 2024-01-04 22:58:22 | 最后一次登录时间。 |
| - AssetsSyncTim e | Long | 2024-01-04 22:58:22 | 资产同步时间。 |
| -ProviderName | String | test | 供应商名称。 |
| - ProviderRegio nName | String | region 1 _ | 供应商名下区域名称。 |
| - ProviderAzNa me | String | az1 | 机房名称。 |
| -ProviderId | Long | 34 | 供应商Id。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ProviderRegio nId | Long | 12 | 供应商名下的区域id。 |
| -ProviderAzId | Long | 56 | 供应商名下的机房id。 |
| -OrgId | String | 9 | 组织id。 |
| -OrgFullId | String | \|1\|8\|9\| | 全组织ID(分隔符为\|)。 |
| - ResourceSetId | String | 11 | 资源集id。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| Success | Boolean | true | 接口调用的结果状态。 取值： true：接口调用成功 false：接口调用失败 |
| PageInfo | Struct |  | 页面显示信息。 |
| -Count | Integer | 10 | 当前页显示的资产的条数。 |
| -PageSize | Integer | 20 | 分页查询时，每页显示的资产的数量。默认值为 20，表示每页显示20条资产信息。 |
| -TotalCount | Integer | 50 | 查询到的资产的总数量。 |
| -CurrentPage | Integer | 1 | 分页查询时，当前页的页码。 |

**示例**

请求示例

```json
https://[Endpoint]/?Action=DescribeCloudCenterInstances&RegionId=cnhangzhou&Lang=zh&Criteria=[{"name":"riskStatus","value":"YES"}, {"name":"internetIp","value":"1.2.XX.XX"}]&MachineTypes=ecs&LogicalExp=OR&NoPage=true&Pag ize=100&CurrentPage=1&Importance=2&Flags=1&ResourceSetIds=123,456&ResourceStatus=NORMAL
```

正常返回示例 `JSON` 格式

```
HTTP/1.1 200 OK Content-Type:application/json
```

`yp` `pp` `/j`

```json
{
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "PageInfo":{
        "TotalCount":50,
        "PageSize":20,
        "CurrentPage":1,
        "Count":10
    },
    "Instances":[
        {
            "ProviderId":34,
            "CreatedTime":1607365213000,
            "Os":"Linux",
            "VulStatus":"YES",
            "ExposedCount":1,
            "IntranetIp":"1.2.XX.XX",
            "Importance":2,
            "AutoSnapshotsLevel":0,
            "InternetIp":"1.2.XX.XX",
            "RegionName":"China (Hangzhou)",
            "AssetsSyncTime":"2024-01-04 22:58:22",
            "Status":"Running",
            "ExposedStatus":0,
            "SafeEventCount":5,
            "InstanceId":"i-m5***",
            "HealthCheckCount":1,
            "Flag":0,
            "ProviderAzId":56,
            "VulCount":2,
            "InstanceName":"yztest-l***",
            "Region":"cn-hangzhou-cm***-***",
            "ProviderAzName":"az1",
            "Ip":"1.2.XX.XX",
            "ClientVersion":"00_31",
            "ProviderRegionName":"region_1",
            "RiskCount":"{                    \"account\": 0,
\"appNum\": 0, \"asapVulCount\": 0, \"baselineHigh\": 0, \"baselineLow\": 0, \"baseline Medium\": 0, \"baselineNum\": 0, \"cmsNum\": 0, \"containerAsap\": 0, \"containerLater\": 0, \"cont ainerNntf\": 0, \"containerRemind\": 0, \"container Serious\": 0, \"containerSuspicious\": 0, \"cveNum\ ": 0, \"emgNum\": 0, \"health\": 0, \"imageBaselineHigh\": 0, \"imageBaselineLow\": 0, \"imageBaselineMedium\": 0, \"imageBaselineNum\": 0, \"imageMaliciousFileRemind\": 0, \"imageMaliciousFileSerious\": 0, \"imageMaliciousFileSuspicious\": 0, \"imageVulAsap\": 0, \"imageVulLater\": 0, \"imageVulNntf\": 0, \"laterV ulCount\": 0, \"newSuspicious\": 0, \"nntfVulCount\": 0, \"remindNum\": 0, \"scaNum\": 0, \"seriousNum\": 0, \"suspNum\": 0, \"suspicious\": 0, \"sysNum\": 0, \"trojan\": 0,
```

```json
\"uuid\": \"inet-37316411-37fe-4b72-b245-346a2721****\", \"vul\": 0, \"weakPWNum\": 0 }",
            "PodCount":1,
            "ProviderRegionId":12,
            "ClusterName":"cluster1",
            "ResourceSetId":"11",
            "FirstLoginTime":"2023-12-11 12:41:51",
            "ClientStatus":"online",
            "ClusterId":"c690a0789419f4284a4e0a29e12fe****",
            "WeakPasswordCount":2,
            "OsName":"-",
            "RiskStatus":"NO",
            "WeakPasswordStatus":"NO",
            "GroupId":"4120080",
            "LastLoginTime":"2024-01-04 22:58:22",
            "ProviderName":"test",
            "OrgId":"9",
            "AssetType":"0",
            "OrgFullId":"|1|8|9|",
            "Uuid":"c9107c04-942f-40c1-981a-f1c1***",
            "AlarmStatus":"NO",
            "VpcInstanceId":"vpc-uf60agqq65bs98zoo****",
            "Tag":"InternetIp,test",
            "RegionId":"cn-hanghzou",
            "HcStatus":"YES"
        }
```

]

```
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <PageInfo>
        <Count>10</Count>
        <PageSize>20</PageSize>
        <TotalCount>50</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
    <Instances>
        <InternetIp>1.2.XX.XX</InternetIp>
        <Os>Linux</Os>
        <InstanceId>i-m5***</InstanceId>
        <InstanceName>yztest-l***</InstanceName>
        <RegionName>China (Hangzhou)</RegionName>
        <Ip>1.2.XX.XX</Ip>
        <ClientStatus>online</ClientStatus>
        <Region>cn-hangzhou-cm***-***</Region>
        <Uuid>c9107c04-942f-40c1-981a-f1c1***</Uuid>
<IntranetIp>1.2.XX.XX</IntranetIp>
```

```json
        <IntranetIp>1.2.XX.XX</IntranetIp>
        <AssetType>0</AssetType>
        <Status>Running</Status>
        <Tag>InternetIp,test</Tag>
        <VpcInstanceId>vpc-uf60agqq65bs98zoo****</VpcInstanceId>
        <OsName>-</OsName>
        <Flag>0</Flag>
        <HcStatus>YES</HcStatus>
        <VulStatus>YES</VulStatus>
        <AlarmStatus>NO</AlarmStatus>
        <RiskStatus>NO</RiskStatus>
        <WeakPasswordStatus>NO</WeakPasswordStatus>
        <HealthCheckCount>1</HealthCheckCount>
        <VulCount>2</VulCount>
        <SafeEventCount>5</SafeEventCount>
        <RegionId>cn-hanghzou</RegionId>
        <GroupId>4120080</GroupId>
        <Importance>2</Importance>
        <ClientVersion>00_31</ClientVersion>
        <RiskCount>{ "account": 0, "appNum": 0, "asapVulCount": 0, "baselineHigh": 0,
"baselineLow": 0, "baselineMedium": 0, "baselineNum": 0, "cmsNum": 0, "containerAsap": 0, "containerLater": 0, "containerNntf": 0, "containerRemind": 0, "containerSerious": 0 , "containerSuspicious": 0, "cveNum": 0, "emgNum": 0, "health": 0, "imageBaselineHigh": 0, "imageBaselineLow": 0, "imageBaselineMedium": 0, "imageBaselineNum": 0, "imageMaliciousFileRemind": 0, "imageMaliciousFileSerious": 0, "imageMaliciousFileSuspicious": 0, "imageVulAsap": 0, "imageVulLater": 0, "imageVulNntf": 0, "laterVulCount": 0, "newSuspicious": 0, "nntfVulCount": 0, "remindNu m": 0, "scaNum": 0, "seriousNum": 0, "suspNum": 0, "suspicious": 0, "sysNum": 0, "trojan": 0, "uuid": "inet-37316411-37fe-4b72-b245-346a2721****", "vul": 0, "weakPWNum" : 0 }</RiskCount>
        <ClusterId>c690a0789419f4284a4e0a29e12fe****</ClusterId>
        <ClusterName>cluster1</ClusterName>
        <CreatedTime>1607365213000</CreatedTime>
        <PodCount>1</PodCount>
        <ExposedStatus>0</ExposedStatus>
        <AutoSnapshotsLevel>0</AutoSnapshotsLevel>
        <ExposedCount>1</ExposedCount>
        <WeakPasswordCount>2</WeakPasswordCount>
        <FirstLoginTime>2023-12-11 12:41:51</FirstLoginTime>
        <LastLoginTime>2024-01-04 22:58:22</LastLoginTime>
        <AssetsSyncTime>2024-01-04 22:58:22</AssetsSyncTime>
        <ProviderName>test</ProviderName>
        <ProviderRegionName>region_1</ProviderRegionName>
        <ProviderAzName>az1</ProviderAzName>
        <ProviderId>34</ProviderId>
        <ProviderRegionId>12</ProviderRegionId>
        <ProviderAzId>56</ProviderAzId>
        <OrgId>9</OrgId>
        <OrgFullId>|1|8|9|</OrgFullId>
        <ResourceSetId>11</ResourceSetId>
    </Instances>
```

#### DescribePropertyScaDetail

调用DescribePropertyScaDetail接口查询资产指纹调查页面中间件列表的详细信息。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- aegis:DescribePropertyScaDeta il | Read | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Lang | Strin g | Query | 否 | zh | 设置请求和接收消息的语言类型，默认为zh。 zh：中文。 en：英文。 |
| SearchIte m | Strin g | Query | 否 | type | 设置查询条件的类型。取值： name ：中间件、数据库或Web服务的名称 type ：中间件、数据库或Web服务的类型。 说明 SearchItem 和Se archInfo 这两个参数配合使用，通过同时设置这两个参数（设置一个无效）， 您可以按照资产指纹的名称或类型查看指定名称或类型资产指纹的所有数据。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SearchInf o | Strin g | Query | 否 | system service _ | 要查询的内容。根据SearchItem 取值的不同，您需要输入不同的查询内容： SearchItem 取值为name 时，您需要输入的查询条件为资产指纹的名称 SearchItem 取值为type 时，您需要选择要查询的资产指纹的类型。可选以下取值： system service _ ：系统服务 software librar _ y ：软件库 docker compone _ nt ：容器组件 database ：数据库 web container _ ：Web容器 jar ：Jar包 web framework _ ：Web框架说明 SearchItem 和Se archInfo 这两个参数配合使用，通过同时设置这两个参数（设置一个无效），您可以按照资产指纹的名称或类型查看指定名称或类型资产指纹的所有数据。 |
| ScaName | Strin g | Query | 否 | openssl | 要查询的资产指纹的名称。 |
| BizType | Strin g | Query | 否 | system service _ | 要查询的中间件、数据库或 Web服务的类型。取值： system service ： _ 系统服务 software library ： _ 软件库 docker componen _ t ：容器组件 database ：数据库 web container ： _ Web容器 jar ：Jar包 web framework ： _ Web框架。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SearchIte mSub | Strin g | Query | 否 | version | 子查询条件的类型。取值： port ：端口 pid ：进程ID version ：版本 user ：用户。 |
| SearchInf oSub | Strin g | Query | 否 | 1.0.2k | 子查询条件的内容。根据SearchItemSub 取值的不同，您需要输入不同的查询内容： SearchItemSub 取值为port 时，您需要输入的子查询条件为端口。 SearchItemSub 取值为pid 时，您需要输入的子查询条件为进程 ID。 SearchItemSub 取值为version 时，您需要输入的子查询条件为中间件、数据库或Web服务版本。 SearchItemSub 取值为user 时，您需要输入的子查询条件为用户名称。 说明子查询条件可以帮助您搜索具体的中间件、数据库或Web 服务的数据列表。 |
| Remark | Strin g | Query | 否 | 192.168 | 搜索条件（服务器名称或 IP）。 说明支持模糊搜索。 |
| Port | Strin g | Query | 否 | 68 | 进程监听端口。 |
| Pid | Strin g | Query | 否 | 756 | 进程ID。 |
| ScaVersio n | Strin g | Query | 否 | 1.0.2k | 中间件、数据库或Web服务版本。 |
| User | Strin g | Query | 否 | root | 运行用户。 |

|  |  |  |  |  | 安骑士开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Long | Query | 否 | 1 | 中间件、数据库或Web服务的名称。 说明此参数已废弃，无需关注。 |
| Uuid | Strin g | Query | 否 | uuid-02ebabe7-1c19- ab**** | 中间件、数据库或Web服务所在服务器的UUID。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为 1，表示从第1页开始显示。 |
| PageSize | Integ er | Query | 否 | 10 | 设置分页查询时，每页显示的资产指纹信息的数量。默认值为10，表示每页显示 10条资产指纹信息。 说明建议PageSize取值不要为空。 |
| SelectTyp e | Strin g | Query | 否 | equals | 查询类型。默认，like。 取值： equals :精确查询 like :模糊查询。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Propertys | Array |  | 资产指纹的列表详情。 |
| - InstanceName | String | Test01 | 中间件、数据库或Web服务所在服务器的名称。 |
| -Ip | String | 47.42.XX.XX | 中间件、数据库或Web服务所在服务器的公网 IP。 |
| -Create | String | 1597987834000 | 最新扫描的时间戳，即安骑士最近一次采集中间件、数据库或Web服务信息的时间戳，单位为毫秒。 |
| - CreateTimesta mp | Long | 1597987834000 | 最新扫描的时间戳，即安骑士最近一次采集中间件、数据库或Web服务信息的时间戳，单位为毫秒。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Uuid | String | uuid-02ebabe7- 1c19-a**** | 中间件、数据库或Web服务所在服务器的 UUID。 |
| -InstanceId | String | i-2zeclqj7ti**** | 中间件、数据库或Web服务所在服务器实例ID。 |
| -IntranetIp | String | 192.210.XX.XX | 中间件、数据库或Web服务所在服务器的私网 IP。 |
| -InternetIp | String | 47.42.XX.XX | 中间件、数据库或Web服务所在服务器的公网 IP。 |
| -Name | String | openssl | 中间件、数据库或Web服务的名称。 |
| -Type | String | library | 中间件、数据库或Web服务类型。 |
| -Version | String | 1.0.2k | 中间件、数据库或Web服务的版本。 |
| -Pid | String | 756 | 进程ID。 |
| -BizType | String | software library _ | 中间件、数据库或Web服务的类型。 取值： system service ：系统服务 _ software library ：软件库 _ docker component ：容器组件 _ database ：数据库 web container ：Web容器 _ jar ：Jar包 web framework ：Web框架。 _ |
| - BizTypeDispal y | String | 软件库 | 中间件、数据库或Web服务类型的名称。取值： 系统服务软件库容器组件数据库 Web容器 Jar包 Web框架 。 |
| -Port | String | 68 | 中间件、数据库或Web服务端口。 |
| - ContainerNam e | String | 5-rce web 1 _ _ | 容器名称。 |

|  |  |  |  | 安骑士开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Path | String | /usr/lib64/libssl.so. 1.0.2k | 中间件、数据库或Web服务的路径。 |
| -Ppid | String | 1 | 父进程ID。 |
| -ProcessUser | String | root | 运行进程的用户名。 |
| -ListenIp | String | 0.0.XX.XX | 进程监听IP。 |
| -ListenStatus | String | NONE | 进程监听状态。 取值： NONE ：未监听 LISTEN ：监听中。 |
| -ListenProtocol | String | UDP | 进程监听协议。取值： UDP TCP 。 |
| - ProcessStarted | Long | 1596539788 | 进程启动的时间戳，单位为毫秒。 |
| -Cmdline | String | /sbin/dhclient -H iz2zeflhhbtk8gtxzt0 87az -1 -q -lf /var/lib/dhclient/dh client--eth0.lease - pf /var/run/dhclient- eth0.pid eth0 | 进程命令行。 |
| -ConfigPath | String | /etc/my.cnf | 配置文件路径。 |
| -WebPath | String | /usr/share/nginx/ht ml | Web目录。 |
| -Proof | String | /usr/lib64/libssl.so. 1.0.2k | 中间件、数据库或Web服务的版本验证信息。 |
| -ImageName | String | registry-vpc.cn- beijing.aliyuncs.co m/acs/aliyun- ingress- controller**** | 镜像名称。 |
| -OrgId | String | 12 | 组织id。 |
| - ResourceSetId | String | 12 | 资源集id。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -OrgName | String | test | 组织名称。 |
| - ResourceSetN ame | String | test | 资源集名称。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| PageInfo | Struct |  | 分页信息。 |
| -Count | Integer | 2 | 分页查询时，当前页显示的数据条数。 |
| -PageSize | Integer | 20 | 分页查询时，每页显示的资产指纹信息的数量。 默认值为10，表示每页显示10条资产指纹信息。 |
| -TotalCount | Integer | 2 | 查询到的资产指纹数据的总数量。 |
| -CurrentPage | Integer | 1 | 分页查询时，当前页的页码。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=DescribePropertyScaDetail&RegionId=cnhangzhou&Lang=zh&SearchItem=type&SearchInfo=system_service&ScaName=openssl&BizType=system ervice&SearchItemSub=version&SearchInfoSub=1.0.2k&Remark=192.168&Port=68&Pid=756&ScaVersi =1.0.2k&User=root&Name=1&Uuid=uuid-02ebabe7-1c19ab****&CurrentPage=1&PageSize=10&SelectType=equals
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Propertys":[
        {
            "BizTypeDispaly":"软件库",
            "ProcessUser":"root",
            "ResourceSetName":"test",
            "Ip":"47.42.XX.XX",
            "Port":"68",
            "OrgName":"test",
            "IntranetIp":"192.210.XX.XX",
            "Name":"openssl",
            "ProcessStarted":1596539788,
            "InternetIp":"47.42.XX.XX",
            "Version":"1.0.2k",
            "ContainerName":"5-rce_web_1",
            "ListenProtocol":"UDP",
            "Create":"1597987834000",
            "WebPath":"/usr/share/nginx/html",
            "ResourceSetId":"12",
            "CreateTimestamp":1597987834000,
            "Ppid":"1",
            "Path":"/usr/lib64/libssl.so.1.0.2k",
            "InstanceId":"i-2zeclqj7ti****",
            "Pid":"756",
            "BizType":"software_library",
            "InstanceName":"Test01",
            "ImageName":"registry-vpc.cn-beijing.aliyuncs.com/acs/aliyun-ingress-
controller****",
            "OrgId":"12",
            "Type":"library",
            "Uuid":"uuid-02ebabe7-1c19-a****",
            "ListenStatus":"NONE",
            "ConfigPath":"/etc/my.cnf",
            "Proof":"/usr/lib64/libssl.so.1.0.2k",
            "ListenIp":"0.0.XX.XX",
            "Cmdline":"/sbin/dhclient -H iz2zeflhhbtk8gtxzt087az -1 -q -lf /var/lib/dhcl
ient/dhclient--eth0.lease -pf /var/run/dhclient-eth0.pid eth0"
        }
```

`],`

```json
    "PageInfo":{
        "TotalCount":2,
        "PageSize":20,
        "CurrentPage":1,
        "Count":2
    }
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Propertys>
        <InstanceName>Test01</InstanceName>
        <Ip>47.42.XX.XX</Ip>
        <Create>1597987834000</Create>
        <CreateTimestamp>1597987834000</CreateTimestamp>
        <Uuid>uuid-02ebabe7-1c19-a****</Uuid>
        <InstanceId>i-2zeclqj7ti****</InstanceId>
        <IntranetIp>192.210.XX.XX</IntranetIp>
        <InternetIp>47.42.XX.XX</InternetIp>
        <Name>openssl</Name>
        <Type>library</Type>
        <Version>1.0.2k</Version>
        <Pid>756</Pid>
        <BizType>software_library</BizType>
        <BizTypeDispaly>软件库</BizTypeDispaly>
        <Port>68</Port>
        <ContainerName>5-rce_web_1</ContainerName>
        <Path>/usr/lib64/libssl.so.1.0.2k</Path>
        <Ppid>1</Ppid>
        <ProcessUser>root</ProcessUser>
        <ListenIp>0.0.XX.XX</ListenIp>
        <ListenStatus>NONE</ListenStatus>
        <ListenProtocol>UDP</ListenProtocol>
        <ProcessStarted>1596539788</ProcessStarted>
        <Cmdline>/sbin/dhclient -H iz2zeflhhbtk8gtxzt087az -1 -q -lf
/var/lib/dhclient/dhclient--eth0.lease -pf /var/run/dhclient-eth0.pid eth0</Cmdline>
        <ConfigPath>/etc/my.cnf</ConfigPath>
        <WebPath>/usr/share/nginx/html</WebPath>
        <Proof>/usr/lib64/libssl.so.1.0.2k</Proof>
        <ImageName>registry-vpc.cn-beijing.aliyuncs.com/acs/aliyun-ingress-
controller****</ImageName>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <OrgName>test</OrgName>
        <ResourceSetName>test</ResourceSetName>
    </Propertys>
    <PageInfo>
        <Count>2</Count>
        <PageSize>20</PageSize>
        <TotalCount>2</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
```

#### DescribeAssetDetailByUuid

调用DescribeAssetDetailByUuid接口根据UUID查询服务器资产详情和扩展信息。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- aegis:DescribeAssetDetailByUui d | Read | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Quer y | 否 | 219.133.XX.XX | 访问源IP地址。 |
| Uuid | Strin g | Quer y | 是 | 9e6cad93-a379-46fd- a701-9bbf02f4**** | 要查询的资产的UUID。 说明调用 DescribeCloudCenterInsta nces接口获取该参数。 |
| Lang | Strin g | Quer y | 否 | zh | 设置请求和接收消息的语言类型。默认为zh。取值： zh： 中文 en：英文。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| AssetDetail | Struct |  | 资产信息详情。 |
| -IpList | Normal | ["192.168.XX.XX"," 192.168.XX.XX"] | IP地址列表。 |

| -MacList | Normal | ["00:16:3*:1*:9*:cf "] | MAC地址。 |
|---|---|---|---|
| -DiskInfoList | Normal |  | 磁盘信息。以下是磁盘相关参数的说明： * diskName：磁盘名称。 * totalSize：磁盘总容量，单位为GB。 * useSize：已使用磁盘容量， 单位为GB。 |
| -InternetIp | String | 192.168.XX.XX | 服务器的公网IP地址。 |
| -IntranetIp | String | 192.168.XX.XX | 服务器的私网IP地址。 |
| - InstanceName | String | i- fasdfasdfadfafa**** | 服务器名称。 |
| -InstanceId | String | i- uf6h7p2fgk6rkk0g* *** | 服务器ID。 |
| -Ip | String | 192.168.XX.XX | ECS分配的IP地址。 |
| -Uuid | String | 9e6cad93-a379- 46fd-a701- 9bbf02f4**** | 服务器UUID。 |
| -AssetType | String | 6 | 资产类型。取值： * 0：云服务器ECS。 * 1：负载均衡SLB。 * 2：NAT网关。 * 3：RDS数据库 * 4：MongoDb数据库。 * 5：REDIS数据库。 * 6：容器镜像IMAGE。 * 7：容器 CONTAINER。 |
| -Os | String | linux | 服务器的操作系统类型。 |
| -ClientStatus | String | online | Agent客户端状态。取值： * pause：暂停保护 * online：保护中 * offline：未受保护。 |
| -Region | String | cn-hangzhou-dg- a01 | 服务器所在地域。 |
| -RegionId | String | cn-hanghzou | 资产的地域ID。 |
| -RegionName | String | China (Hohhot) | 服务器所在地域名称。 |
| -Tag | String | InternetIp | 服务器的标签。 |

| -GroupTrace | String | default | 服务器所属的分组。未设置分组的服务器默认属于未分组。 |
|---|---|---|---|
| -Cpu | Integer | 2 | CPU内核数。 |
| -CpuInfo | String | Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz | CPU详细信息。 |
| -Kernel | String | 4.18.0- 80.11.2.el8 0.x86 _ _ 64 | 操作系统的内核版本。 |
| -OsDetail | String | Linux 64bit | 服务器的操作系统版本位数。 |
| -Mem | Integer | 32 | 内存大小，单位为GB。 |
| -SysInfo | String | CentOS Linux 8.0.1905 | 服务器的操作系统信息。 |
| -HostName | String | qewrqwerqs**** | 主机名称。 |
| -OsName | String | - | 服务器的操作系统名称。 |
| -VpcInstanceId | String | vpc- bp1fs3bwonlfq503 w**** | 服务器所在的VPC实例ID。 |
| -CreateTime | Long | 1603863599000 | 安骑士记录当前资产信息的时间戳，单位为毫秒。 |
| -Flag | Integer | 0 | 资产是否为阿里云资产。取值： * 0：阿里云资产 * 1：非阿里云资产。 |
| -OrgId | String | 12 | 组织id。 |
| - ResourceSetId | String | 12 | 资源集id。 |
| - FirstLoginTime | Long | 1603863599000 | 首次登录时间。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=DescribeAssetDetailByUuid&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&Uuid=9e6cad93-a379-46fd-a701-9bbf02f4****&Lang=zh
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "AssetDetail":{
        "GroupTrace":"default",
        "Os":"linux",
        "Ip":"192.168.XX.XX",
        "Cpu":2,
        "IntranetIp":"192.168.XX.XX",
        "OsDetail":"Linux 64bit",
        "InternetIp":"192.168.XX.XX",
        "RegionName":"China (Hohhot)",
        "InstanceStatus":"",
        "ResourceSetId":"12",
        "Kernel":"4.18.0-80.11.2.el8_0.x86_64",
        "HostName":"qewrqwerqs****",
        "FirstLoginTime":"",
        "ClientStatus":"online",
        "InstanceId":"i-uf6h7p2fgk6rkk0g****",
        "CpuInfo":"Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz",
        "IpList":[
            "192.168.XX.XX",
            "192.168.XX.XX"
```

`],`

```json
        "OsName":"-",
        "CreateTime":1603863599000,
        "SysInfo":"CentOS Linux 8.0.1905",
        "Flag":0,
        "InstanceName":"i-fasdfasdfadfafa****",
        "MacList":[
            "00:16:3*:1*:9*:cf"
```

`],`

```json
        "OrgId":"12",
        "AssetType":"6",
        "Uuid":"9e6cad93-a379-46fd-a701-9bbf02f4****",
        "Mem":32,
        "Region":"cn-hangzhou-dg-a01",
        "VpcInstanceId":"vpc-bp1fs3bwonlfq503w****",
        "RegionId":"cn-hanghzou",
        "Tag":"InternetIp"
    }
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <AssetDetail>
        <InternetIp>192.168.XX.XX</InternetIp>
        <IntranetIp>192.168.XX.XX</IntranetIp>
        <InstanceName>i-fasdfasdfadfafa****</InstanceName>
        <InstanceId>i-uf6h7p2fgk6rkk0g****</InstanceId>
        <Ip>192.168.XX.XX</Ip>
        <Uuid>9e6cad93-a379-46fd-a701-9bbf02f4****</Uuid>
        <AssetType>6</AssetType>
        <Os>linux</Os>
        <ClientStatus>online</ClientStatus>
        <Region>cn-hangzhou-dg-a01</Region>
        <RegionId>cn-hanghzou</RegionId>
        <RegionName>China (Hohhot)</RegionName>
        <Tag>InternetIp</Tag>
        <GroupTrace>default</GroupTrace>
        <Cpu>2</Cpu>
        <CpuInfo>Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz</CpuInfo>
        <Kernel>4.18.0-80.11.2.el8_0.x86_64</Kernel>
        <OsDetail>Linux 64bit</OsDetail>
        <Mem>32</Mem>
        <SysInfo>CentOS Linux 8.0.1905</SysInfo>
        <HostName>qewrqwerqs****</HostName>
        <OsName>-</OsName>
        <IpList>
            <Ip>["192.168.XX.XX","192.168.XX.XX"]</Ip>
        </IpList>
        <MacList>
            <Mac>["00:16:3*:1*:9*:cf"]</Mac>
        </MacList>
        <DiskInfoList>
            <DiskInfo></DiskInfo>
        </DiskInfoList>
        <VpcInstanceId>vpc-bp1fs3bwonlfq503w****</VpcInstanceId>
        <InstanceStatus></InstanceStatus>
        <CreateTime>1603863599000</CreateTime>
        <Flag>0</Flag>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <FirstLoginTime></FirstLoginTime>
    </AssetDetail>
```

#### DescribeDomainDetail

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- aegis:DescribeDomainDetail | Read | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：50QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| DomainNa me | Strin g | Query | 是 | example.com | 要查询的域名或网站的名称。 说明不支持模糊查询，您需要输入完整的域名或网站名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DomainDetailIt ems | Array |  | 域名相关的资产信息。 |
| -InternetIp | String | 1.2.XX.XX | 资产对应的公网的IP地址。 |
| -InstanceId | String | i- m5e6w7dzsktt6mz 4*** | 资产的实例ID。 |
| -Uuid | String | lb- bp1g9dohoyin9cjh n6**** | 资产实例的UUID。 |
| -AssetType | String | 0 | 域名下资产的资产类型。取值包括： 0：ECS。 1：负载均衡。 2：NAT网关。 3：RDS数据库。 4：MongoDB数据库。 |
| - InstanceName | String | iZm5e6w7dzsktt6 mz4yimeZ-6**** | 资产的名称。 |

| 安骑士开发指南·AP | I参考 |  |  |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -IntranetIp | String | 1.2.XX.XX | 资产对应的私网的IP地址。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| Domain | String | example.com | 域名。 |
| RootDomain | String | example.com | 域名对应的根域名的名称。 |
| VulCount | Integer | 2 | 您网站资产中的漏洞的总数量。 |
| AlarmCount | Integer | 2 | 您网站资产中的告警的总数量。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=DescribeDomainDetail&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&DomainName=example.com
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Domain":"example.com",
    "RootDomain":"example.com",
    "VulCount":2,
    "AlarmCount":2,
    "DomainDetailItems":[
        {
            "InstanceName":"iZm5e6w7dzsktt6mz4yimeZ-6****",
            "AssetType":"0",
            "Uuid":"lb-bp1g9dohoyin9cjhn6****",
            "InternetIp":"1.2.XX.XX",
            "InstanceId":"i-m5e6w7dzsktt6mz4***",
            "MachineIp":"",
            "IntranetIp":"1.2.XX.XX"
        }
```

]

```
}
```

`XML` 格式

| HTTP/1.1 200 OK Content-Type:application/xml <DescribeDomainDetailResponse> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Domain>example.com</Domain> <RootDomain>example.com</RootDomain> <VulCount>2</VulCount> <AlarmCount>2</AlarmCount> <DomainDetailItems> <InternetIp>1.2.XX.XX</InternetIp> <InstanceId>i-m5e6w7dzsktt6mz4***</InstanceId> <Uuid>lb-bp1g9dohoyin9cjhn6****</Uuid> <AssetType>0</AssetType> <InstanceName>iZm5e6w7dzsktt6mz4yimeZ-6****</InstanceName> <MachineIp></MachineIp> <IntranetIp>1.2.XX.XX</IntranetIp> </DomainDetailItems> </DescribeDomainDetailResponse> |  |
|---|---|

#### DescribeGroupSummary

获取分组的列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeGroupS ummary | 系统规定参数。取值：DescribeGroupSummary。 |
| SourceIp | String | 否 | 192.168.0.1 | 访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 10 | 分组个数。 |
| Groups | Array of Group |  | 分组的详情。 |
| GroupFather | Integer | 1 | 父节点ID。 |
| GroupFlag | Integer | 1 | 分组类型。 1：非叶子节点。 0：叶子节点。 |

| GroupId | Long | 1 | 分组ID。 |
|---|---|---|---|
| GroupIndex | Integer | 1 | 分组顺序。 |
| GroupLevel | Integer | 1 | 分组的层级。 |
| GroupName | String | 测试分组 | 分组名称。 |
| MachineNum | Integer | 1 | 机器的台数。 |
| RequestId | String | 485ABE58-4E27- 4416-997C- F8F3B8748EB6 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGroupSummary
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>485ABE58-4E27-4416-997C-F8F3B8748EB6</RequestId> <Groups>
    <GroupName>测试分组</GroupName>
    <MachineNum>1</MachineNum>
    <GroupLevel>1</GroupLevel>
    <GroupIndex>1</GroupIndex>
    <GroupFather>1</GroupFather>
    <GroupFlag>1</GroupFlag>
    <GroupId>1</GroupId>
</Groups> <Count>10</Count>
```

`JSON` 格式

```json
{
    "RequestId": "485ABE58-4E27-4416-997C-F8F3B8748EB6",
    "Groups": {
```

`"GroupName": "`测试分组`",`

```json
        "MachineNum": 1,
        "GroupLevel": 1,
        "GroupIndex": 1,
        "GroupFather": 1,
        "GroupFlag": 1,
        "GroupId": 1
    },
    "Count": 10
}
```

#### DescribeGroupStruct

获取分组结构。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeGroupS truct | 取值：DescribeGroupStruct。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源IP。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |
| remark | String | 否 | 47.100.XX.XX | 服务器IP或者实例名称。 |
| tagIdList | String | 否 | 1***,2*** | 标签ID列表。多个标签ID之间需要用英文逗号分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| GroupFather | Integer | 1 | 父节点ID。 |
| GroupFlag | Integer | 1 | 分组类型。 1：非叶子节点。 0：叶子节点。 |

| GroupId | Long | 1 | 分组ID。 |
|---|---|---|---|
| GroupIndex | Integer | 1 | 分组顺序。 |
| GroupLevel | Integer | 4 | 分组的层级。 |
| GroupName | String | 测试分组 | 分组名称。 |
| Groups | List | [] | 自分组。 |
| MachineNum | Integer | 1 | 机器的台数。 |
| RequestId | String | 485ABE58-4E27- 4416-997C- F8F3B8748EB6 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGroupStruct
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<GroupName>测试分组</GroupName> <MachineNum>1</MachineNum> <RequestId>485ABE58-4E27-4416-997C-F8F3B8748EB6</RequestId> <GroupLevel>4</GroupLevel> <Groups>[]</Groups> <GroupIndex>1</GroupIndex> <GroupFather>1</GroupFather> <GroupFlag>1</GroupFlag> <GroupId>1</GroupId>
```

`JSON` 格式

```
{
```

`"GroupName": "`测试分组`",`

```json
    "MachineNum": 1,
    "RequestId": "485ABE58-4E27-4416-997C-F8F3B8748EB6",
    "GroupLevel": 4,
    "Groups": "[]",
    "GroupIndex": 1,
    "GroupFather": 1,
    "GroupFlag": 1,
    "GroupId": 1
}
```

#### DescribeAllEntity

不分页获取所有的实例列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAllEntit y | 取值：DescribeAllEntity。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| Os | String | 否 | win | 操作系统的类型。 win：Windows。 linux：Linux。 |
| GroupId | Long | 否 | 1 | 服务器所在的分组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 15 | 当前页的数据条数。 |
| EntityList | Array of Entity |  | 实例列表信息。 |
| GroupId | Integer | 1 | 服务器所在的分组ID。 |
| InstanceName | String | test*** | 实例名称。 |
| Ip | String | 47.100.XX.XX | 展示的服务器的IP，先看服务器是否有公网IP， 没有公网IP展示私网IP。 |

| Uuid | String | cadda****** | 服务器唯一标识。 |
|---|---|---|---|
| RequestId | String | dacd******** | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>dacd********</RequestId> <EntityList>
    <InstanceName>test***</InstanceName>
    <Uuid>cadda******</Uuid>
    <Ip>47.100.XX.XX</Ip>
    <GroupId>1</GroupId>
</EntityList> <Count>15</Count>
```

`JSON` 格式

```json
{
    "RequestId": "dacd********",
    "EntityList": {
        "InstanceName": "test***",
        "Uuid": "cadda******",
        "Ip": "47.100.XX.XX",
        "GroupId": 1
    },
    "Count": 15
}
```

#### DescribeEntityList

获取实例列表，支持按照安全事件等分页查询。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeEntityLi st | 取值：DescribeEntityList。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |

| From | String | 否 | aqs | 产品。固定值：aqs。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| Remark | String | 否 | 47.100.XX.XX | 服务器IP或者实例名称。 |
| GroupId | Long | 否 | 1 | 服务器所在的分组ID。 |
| TagIdList | String | 否 | 1,*,* | 标签的ID列表。多个ID之间需要用英文逗号分隔。 |
| Os | String | 否 | windows | 操作系统类型。 windows：Windows。 linux：Linux。 |
| RegionNo | String | 否 | cn-beijing-**** | 地域编号。 |
| Status | String | 否 | offline | 按agent状态筛选服务器列表。 offline：离线列表。 pause：暂停保护列表。 |
| Patch | String | 否 | 无 | 已废弃。 |
| Health | String | 否 | 无 | 已废弃。 |
| Account | String | 否 | 无 | 已废弃。 |
| Trojan | String | 否 | 无 | 已废弃。 |
| Suspicious | String | 否 | 无 | 已废弃。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 当前页的页码。 |
| EntityList | Array of Entity |  | 实例列表。 |

| AegisOnline | Boolean | true | 是否在线。 true：是。 false：否。 |
|---|---|---|---|
| AegisVersion | String | aegis 10 ** _ _ | 安骑士版本。 |
| BuyVersion | String | 4 | 购买版本。 |
| ClientStatus | Boolean | false | 是否处于安全保护中（暂停保护功能）。 true：是。 false：否。 |
| Flag | Integer | 1 | 已废弃。 |
| GroupId | Long | 1 | 分组ID。 |
| InstanceName | String | test *** _ | 实例名称。 |
| Ip | String | 47.100.XX.XX | IP地址。 说明先取公网IP，没有公网IP再取私网IP地址。 |
| Os | String | linux | 操作系统类型。 windows：Windows。 linux：Linux。 |
| Region | String | cn-beijing-*** | 地区信息。 |
| Uuid | String | 00f2-xxx-xxx | 机器唯一标识。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| RequestId | String | unhgff-**** | 本次调用请求的ID。 |
| TotalCount | Integer | 20 | 总数据条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeEntityList
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>20</TotalCount> <PageSize>20</PageSize> <RequestId>unhgff-****</RequestId> <CurrentPage>1</CurrentPage> <EntityList>
    <InstanceName>test_***</InstanceName>
    <ClientStatus>false</ClientStatus>
    <Uuid>00f2-xxx-xxx</Uuid>
    <BuyVersion>4</BuyVersion>
    <AegisVersion>aegis_10_**</AegisVersion>
    <Os>linux</Os>
    <Ip>47.100.XX.XX</Ip>
    <Region>cn-beijing-***</Region>
    <AegisOnline>true</AegisOnline>
    <Flag>1</Flag>
    <GroupId>1</GroupId>
</EntityList>
```

`JSON` 格式

```json
{
    "TotalCount": 20,
    "PageSize": 20,
    "RequestId": "unhgff-****",
    "CurrentPage": 1,
    "EntityList": {
        "InstanceName": "test_***",
        "ClientStatus": false,
        "Uuid": "00f2-xxx-xxx",
        "BuyVersion": 4,
        "AegisVersion": "aegis_10_**",
        "Os": "linux",
        "Ip": "47.100.XX.XX",
        "Region": "cn-beijing-***",
        "AegisOnline": true,
        "Flag": 1,
        "GroupId": 1
    }
}
```

#### DescribeMachines

获取机器列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMachin es | 取值：DescribeMachines。 |
| SourceIp | String | 否 | 47.200.XX.XX | 访问者源IP。 |
| Remark | String | 否 | test1 | 服务器实例的IP或者名称。 |
| TagIdList | String | 否 | ["1","2"] | 标签列表，多个标签之间需要用英文逗号分隔。 |
| GroupId | Long | 否 | 123 | 分组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 10 | 总数。 |
| Machines | Array of Machine |  | 机器列表。 |
| GroupId | Long | 1 | 分组ID。 |
| InstanceName | String | i-adf234s*** | 实例名称。 |
| Ip | String | 10.1.x.x | IP地址。优先展示公网IP，若不存在公网IP，则显示私网IP。 |
| Os | String | linux | 操作系统的类型。 win：Windows。 linux：Linux。 |
| Uuid | String | 6dbdbfe7-06fa- 4d9a-8268-xxx | 机器唯一标识。 |
| RequestId | String | 485ABE58-******* | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>485ABE58-*******</RequestId> <Count>10</Count> <Machines>
    <InstanceName>i-adf234s***</InstanceName>
    <Uuid>6dbdbfe7-06fa-4d9a-8268-xxx</Uuid>
    <Os>linux</Os>
    <Ip>10.1.x.x</Ip>
    <GroupId>1</GroupId>
</Machines>
```

`JSON` 格式

```json
{
    "RequestId": "485ABE58-*******",
    "Count": 10,
    "Machines": {
        "InstanceName": "i-adf234s***",
        "Uuid": "6dbdbfe7-06fa-4d9a-8268-xxx",
        "Os": "linux",
        "Ip": "10.1.x.x",
        "GroupId": 1
    }
}
```

#### DescribeMachineDetail

获取服务器的信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMachin eDetail | 取值：DescribeMachineDetail。 |
| SourceIp | String | 否 | 1.1.XX.XX | 访问者源IP。 |
| Uuid | String | 否 | 6dbdbfe7-06fa- 4d9a-8268-xxx | 服务器的唯一标识。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MachineDetail | Struct |  | 机器详情。 |

| AegisOnline | Boolean | true | 是否在线。 true：在线。 false：不在线。 |
|---|---|---|---|
| AegisVersion | String | 10-73 | 安骑士版本。 |
| BuyVersion | String | 无 | 已废弃。 |
| ClientStatus | Boolean | true | 客户端状态。 true：保护中。 false：暂停保护 。 |
| Flag | Integer | 1 | 主机标识。 0：阿里云 。 1：非阿里云。 |
| GroupId | Long | 1 | 分组ID。 |
| GroupTrace | String | 分组1-分组2 | 分组路径。 |
| InstanceId | String | i-aaabcc22xxx | 实例ID。 |
| InstanceName | String | test*** | 实例名称。 |
| IntranetIp | String | 192.168.XX.XX | 私网IP。 |
| Ip | String | 47.200.XX.XX | IP地址。优先展示公网IP，若公网IP不存在，则显示私网IP。 |
| Os | String | linux | 操作系统的类型。 win：Windows。 linux：Linux。 |
| Region | String | cn-hangzhou-xxx | 地域名称。 |
| Tag | String | aaxxx | 标签名称。 |
| Uuid | String | 6dbdbfe7-06fa- 4d9a-8268-xxxx | 服务器标识。 |

| RequestId | String | 485ABE58-4E27- xxx | 本次调用请求的ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeMachineDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>485ABE58-4E27-xxx</RequestId> <MachineDetail>
    <GroupTrace>分组1-分组2</GroupTrace>
    <ClientStatus>true</ClientStatus>
    <AegisVersion>10-73</AegisVersion>
    <BuyVersion>无</BuyVersion>
    <Os>linux</Os>
    <InstanceId>i-aaabcc22xxx</InstanceId>
    <Ip>47.200.XX.XX</Ip>
    <AegisOnline>true</AegisOnline>
    <Flag>1</Flag>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <GroupId>1</GroupId>
    <InstanceName>test***</InstanceName>
    <Uuid>6dbdbfe7-06fa-4d9a-8268-xxxx</Uuid>
    <Region>cn-hangzhou-xxx</Region>
    <Tag>aaxxx</Tag>
</MachineDetail>
```

`JSON` 格式

```json
{
    "RequestId": "485ABE58-4E27-xxx",
    "MachineDetail": {
```

`"GroupTrace": "`分组`1-`分组`2",`

```json
        "ClientStatus": true,
        "AegisVersion": "10-73",
        "BuyVersion": "无",
        "Os": "linux",
        "InstanceId": "i-aaabcc22xxx",
        "Ip": "47.200.XX.XX",
        "AegisOnline": true,
        "Flag": 1,
        "IntranetIp": "192.168.XX.XX",
        "GroupId": 1,
        "InstanceName": "test***",
        "Uuid": "6dbdbfe7-06fa-4d9a-8268-xxxx",
        "Region": "cn-hangzhou-xxx",
        "Tag": "aaxxx"
    }
}
```

#### DescribePropertyStatistic

获取资产信息统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yStatistic | 系统规定参数。取值：DescribePropertyStatistic。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| Uuids | String | 否 | uuid1,uuid2 | UUID。多个UUID之间需要用英文逗号分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PropertyStatist ics | Array of PropertyStatist ic |  | 总计信息列表。 |
| PortCount | String | 2 | 端口总数。 |
| PortGetDate | String | 3 | 已废弃。 |

| ProcCount | String | 4 | 进程总数。 |
|---|---|---|---|
| ProcGetDate | String | 5 | 已废弃。 |
| RootUserCoun t | String | 6 | ROOT权限账号总数。 |
| UserCount | String | 7 | 账号总数。 |
| UserGetDate | String | 8 | 已废弃。 |
| Uuid | String | 9 | 服务器UUID。 |
| RequestId | String | C1CACE7E-E868- 4E44-A52E- 4CB1463B62BB | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyStatistic
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PropertyStatistics>
    <UserGetDate>1514373155000</UserGetDate>
    <Uuid>inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818</Uuid>
    <RootUserCount>1</RootUserCount>
    <UserCount>33</UserCount>
    <ProcCount>89</ProcCount>
    <PortGetDate>1514115614000</PortGetDate>
    <PortCount>6</PortCount>
    <ProcGetDate>1514373133000</ProcGetDate>
</PropertyStatistics> <PropertyStatistics>
    <UserGetDate>1514373139000</UserGetDate>
    <Uuid>inet-f6ac9a93-0818-4052-90e2-d24f18ee198b</Uuid>
    <RootUserCount>1</RootUserCount>
    <UserCount>33</UserCount>
    <ProcCount>34</ProcCount>
    <PortGetDate>1514373168000</PortGetDate>
    <PortCount>1</PortCount>
    <ProcGetDate>1514373131000</ProcGetDate>
</PropertyStatistics> <RequestId>C1CACE7E-E868-4E44-A52E-4CB1463B62BB</RequestId>
```

`JSON` 格式

```json
{
 "PropertyStatistics":[
  {
   "UserGetDate":1514373155000,
   "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
   "RootUserCount":1,
   "UserCount":33,
   "ProcCount":89,
   "PortGetDate":1514115614000,
   "PortCount":6,
   "ProcGetDate":1514373133000
  },
  {
   "UserGetDate":1514373139000,
   "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
   "RootUserCount":1,
   "UserCount":33,
   "ProcCount":34,
   "PortGetDate":1514373168000,
   "PortCount":1,
   "ProcGetDate":1514373131000
  }
```

`],`

```json
 "RequestId":"C1CACE7E-E868-4E44-A52E-4CB1463B62BB"
}
```

#### DescribePropertyPortItem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yPortItem | 系统规定参数。取值：DescribePropertyPortItem。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| Port | String | 否 | 22 | 端口号。 |
| ProcName | String | 否 | sshd | 进程名。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 2 | 分页查询时，显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| PropertyPortIt ems | Array of PropertyPortIt em |  | 端口信息列表。 |
| Count | Integer | 2 | 开放该端口的云服务器数量。 |
| Port | String | 22 | 端口号。 |
| Proto | String | tcp | 网络协议 。 |
| RequestId | String | cd756ccc-5040- 4a4d-9c55- a34be56e7af4 | 本次调用请求的ID。 |
| TotalCount | Integer | 2 | 端口总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyPortItem
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>2</TotalCount> <PageSize>20</PageSize> <RequestId>cd756ccc-5040-4a4d-9c55-a34be56e7af4</RequestId> <CurrentPage>1</CurrentPage> <PropertyPortItems>
    <Proto>tcp</Proto>
    <Port>22</Port>
    <Count>2</Count>
</PropertyPortItems> <Count>2</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 2,
    "PageSize": 20,
    "RequestId": "cd756ccc-5040-4a4d-9c55-a34be56e7af4",
    "CurrentPage": 1,
    "PropertyPortItems": {
        "Proto": "tcp",
        "Port": 22,
        "Count": 2
    },
    "Count": 2
}
```

#### DescribePropertyPortDetail

调用DescribePropertyPortDetail接口查询端口列表中一个端口的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yPortDetail | 取值：DescribePropertyPortDetail。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| TagIdListString | String | 否 | 1,2 | 标签信息。多个标签信息之间需要用英文逗号分隔。 |
| GroupId | String | 否 | 1 | 分组ID。 |
| Remark | String | 否 | 47.100.XX.XX | 服务器名称或IP。 |
| Ip | String | 否 | 47.100.XX.XX | 机器IP。 |
| Port | String | 否 | 22 | 端口号。 |
| ProcName | String | 否 | sshd | 进程名。 |
| Extend | String | 否 | 20 | 根据Port字段搜索是否使用模糊 。 1：使用。 0：不使用。 |
| Uuid | String | 否 | 46ef7c05-0c53- 486c-b446- ef6ff9725xxx | 服务器UUID。 |

| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 2 | 分页查询时，显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| PropertyPorts | Array of PropertyPort |  | 详情列表。 |
| BindIp | String | 47.100.XX.XX | 端口绑定的IP地址信息。 |
| Create | String | 1514373168000 | 数据的最新采集时间。 |
| InstanceName | String | test*** | 端口关联资产的名称。 |
| Ip | String | 47.100.XX.XX | 服务器IP。 |
| Port | String | 22 | 端口号。 |
| ProcName | String | sshd | 端口对应的进程名称。 |
| Proto | String | tcp | 端口对应网络协议。 |
| Uuid | String | 46ef7c05-0c53- 486c-b446- ef6ff972551c | 端口关联的资产实例的唯一标识ID。 |
| RequestId | String | D85484BB-4DC2- 44EC-AD67- 0B3765EC9213 | 本次调用请求的ID。 |
| TotalCount | Integer | 199 | 数据的总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyPortDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>199</TotalCount> <PageSize>20</PageSize> <RequestId>D85484BB-4DC2-44EC-AD67-0B3765EC9213</RequestId> <CurrentPage>1</CurrentPage> <PropertyPorts>
    <InstanceName>test***</InstanceName>
    <Uuid>46ef7c05-0c53-486c-b446-ef6ff972551c</Uuid>
    <Proto>tcp</Proto>
    <Create>1514373168000</Create>
    <ProcName>sshd</ProcName>
    <Ip>47.100.XX.XX</Ip>
    <Port>22</Port>
    <BindIp>47.100.XX.XX</BindIp>
</PropertyPorts> <Count>2</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 199,
    "PageSize": 20,
    "RequestId": "D85484BB-4DC2-44EC-AD67-0B3765EC9213",
    "CurrentPage": 1,
    "PropertyPorts": {
        "InstanceName": "test***",
        "Uuid": "46ef7c05-0c53-486c-b446-ef6ff972551c",
        "Proto": "tcp",
        "Create": 1514373168000,
        "ProcName": "sshd",
        "Ip": "47.100.XX.XX",
        "Port": 22,
        "BindIp": "47.100.XX.XX"
    },
    "Count": 2
}
```

#### DescribePropertyProcItem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribePropert yProcItem | 系统规定参数。取值：DescribePropertyProcItem。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| Name | String | 否 | sshd | 进程名称。 |
| User | String | 否 | root | 启动进程的用户名。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 3 | 显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| PropertyProcIt ems | Array of PropertyProcIt em |  | 进程的信息。 |
| Count | Integer | 2 | 进程名对应的服务器数量。 |
| Name | String | sshd | 进程名称。 |
| RequestId | String | 8BE95FB1-66B7- 4509-AF82- 3AA67368A5D8 | 本次调用请求的ID。 |
| TotalCount | Integer | 2 | 数据的总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyProcItem
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>1</TotalCount> <PropertyProcItems>
    <Count>2</Count>
    <Name>init</Name>
</PropertyProcItems> <PageSize>20</PageSize> <RequestId>8BE95FB1-66B7-4509-AF82-3AA67368A5D8</RequestId> <CurrentPage>1</CurrentPage> <Count>1</Count>
```

`JSON` 格式

```json
{
 "TotalCount":1,
 "PropertyProcItems":[
  {
   "Count":2,
   "Name":"init"
  }
```

`],`

```json
 "PageSize":20,
 "RequestId":"8BE95FB1-66B7-4509-AF82-3AA67368A5D8",
 "CurrentPage":1,
 "Count":1
}
```

#### DescribePropertyProcDetail

获取账户下服务器进程详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yProcDetail | 系统规定参数。取值：DescribePropertyProcDetail。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| TagIdListString | String | 否 | 1,2 | 标签筛选信息。 |
| GroupId | String | 否 | 1 | 分组ID。 |
| Remark | String | 否 | 47.100.XX.XX | 服务器名称或IP。 |

| Ip | String | 否 | 47.100.XX.XX | 服务器IP。 |
|---|---|---|---|---|
| Name | String | 否 | udevd | 进程名。 |
| User | String | 否 | root | 进程的运行用户信息。 |
| Cmdline | String | 否 | /sbin/udevd -d | 进程参数。 |
| Extend | String | 否 | 1 | Name是否使用模糊搜索。 1 ：是。 0 ：否。 |
| Uuid | String | 否 | inet-00f20b1a- e2dd-408b- b38e-xxx | 服务器UUID。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 12 | 分页查询时，显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| PropertyProcs | Array of PropertyProc |  | 进程详情信息。 |
| Cmdline | String | /sbin/udevd -d | 进程对应启动参数。 |
| Create | String | 1514373133000 | 数据的最新采集时间戳。单位：毫秒。 |
| EuidName | String | root | 进程对应的运行权限。 |
| InstanceName | String | test*** | 进程关联的资产名称。 |

| Md5 | String | 529b18a987bdbafc 91d523286bc0ac5 6 | 进程对应的文件MD5信息。 |
|---|---|---|---|
| Name | String | udevd | 进程名称。 |
| Path | String | /sbin/udevd | 进程所在路径。 |
| Pid | String | 12 | 运行进程的身份标识。 |
| Pname | String | init | 进程所属父进程名称。 |
| StartTime | String | 2017-12-26 22:35:00 | 进程启动时间。格式：yyyy-MM-dd HH:mm:ss。 |
| User | String | root | 进程的运行用户。 |
| Uuid | String | inet-00f20b1a- e2dd-408b-b38e- xxxx | 进程关联资产实例的唯一标识ID。 |
| RequestId | String | df5eafee-6add- 4cef-bbb0- c1b388e5ae77 | 本次调用请求的ID。 |
| TotalCount | Integer | 12 | 数据的总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyProcDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PropertyProcs>
    <Path>/sbin/udevd</Path>
    <InstanceName>test***</InstanceName>
    <Pname>init</Pname>
    <Uuid>inet-00f20b1a-e2dd-408b-b38e-xxxx</Uuid>
    <User>root</User>
    <Create>1514373133000</Create>
    <StartTime>2017-12-26 22:35:00</StartTime>
    <Pid>12</Pid>
    <Cmdline>/sbin/udevd -d</Cmdline>
    <EuidName>root</EuidName>
    <Md5>529b18a987bdbafc91d523286bc0ac56</Md5>
    <Name>udevd</Name>
</PropertyProcs> <TotalCount>12</TotalCount> <PageSize>20</PageSize> <RequestId>df5eafee-6add-4cef-bbb0-c1b388e5ae77</RequestId> <CurrentPage>1</CurrentPage> <Count>12</Count>
```

`JSON` 格式

```json
{
    "PropertyProcs": {
        "Path": "/sbin/udevd",
        "InstanceName": "test***",
        "Pname": "init",
        "Uuid": "inet-00f20b1a-e2dd-408b-b38e-xxxx",
        "User": "root",
        "Create": 1514373133000,
        "StartTime": "2017-12-26 22:35:00",
        "Pid": 12,
        "Cmdline": "/sbin/udevd -d",
        "EuidName": "root",
        "Md5": "529b18a987bdbafc91d523286bc0ac56",
        "Name": "udevd"
    },
    "TotalCount": 12,
    "PageSize": 20,
    "RequestId": "df5eafee-6add-4cef-bbb0-c1b388e5ae77",
    "CurrentPage": 1,
    "Count": 12
}
```

#### DescribePropertySoftwareItem

获取账户下服务器软件安装列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribePropert ySoftwareItem | 系统规定参数。取值：DescribePropertySoftwareIte m。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 192.1.x.x | 访问者源IP。 |
| Name | String | 否 | test | 软件名。 |
| Path | String | 否 | /etc/test | 软件路径。 |
| SoftwareVersion | String | 否 | 11 | 软件版本。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 2 | 当前页面软件信息计数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| PropertySoftw areItems | Array of PropertySoftw areItem |  | 软件信息列表。 |
| Count | Integer | 1 | 软件安装服务器数。 |
| Name | String | aaa basxx _ | 软件名。 |
| RequestId | String | 9C5AE850-7140- 4DE6-B892- 055EB0D9F28A | 本次调用请求的ID。 |
| TotalCount | Integer | 30 | 数据总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareItem
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>30</TotalCount> <PageSize>20</PageSize> <RequestId>9C5AE850-7140-4DE6-B892-055EB0D9F28A </RequestId> <PropertySoftwareItems>
    <Count>1</Count>
    <Name>aaa_basxx</Name>
</PropertySoftwareItems> <CurrentPage>1</CurrentPage> <Count>2</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 30,
    "PageSize": 20,
    "RequestId": "9C5AE850-7140-4DE6-B892-055EB0D9F28A",
    "PropertySoftwareItems": {
        "Count": 1,
        "Name": "aaa_basxx"
    },
    "CurrentPage": 1,
    "Count": 2
}
```

#### DescribePropertySoftwareDetail

获取软件资产详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert ySoftwareDetail | 系统规定参数。取值：DescribePropertySoftwareDe tail。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| Remark | String | 否 | 47.100.XX.XX | 服务器名称或IP。 |
| Ip | String | 否 | 47.100.XX.XX | 服务器IP。 |

| GroupId | String | 否 | 1 | 分组ID。 |
|---|---|---|---|---|
| Name | String | 否 | sshd | 软件名。 |
| Path | String | 否 | /usr/xxx | 软件安装路径。 |
| SoftwareVersion | String | 否 | 1.1.x.x | 软件版本。 |
| Extend | String | 否 | 1 | 软件名字段Name是否采用模糊搜索。 1：是 。 0：不是。 |
| Uuid | String | 否 | inet-f6ac9a93- xxx | 服务器UUID。 |
| CurrentPage | Integer | 否 | 1 | 分页查询时，当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 2 | 当前页数据的条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| PropertySoftw ares | Array of PropertySoftw are |  | 软件资产信息列表。 |
| Create | Long | 1514172615000 | 信息刷新时间。使用时间戳格式，单位：毫秒。 |
| InstallTime | String | 2016-06-29 06:55:22 | 软件安装时间。格式：yyyy-MM-dd HH:mm:ss。 |
| InstanceName | String | test*** | 服务器名。 |
| Ip | String | 47.100.XX.XX | 服务器IP。 |

| Path | String | /usr/sshd | 软件安装路径。 |
|---|---|---|---|
| Uuid | String | inet-f6ac9a93- 0818-4052-90e2- xxxx | 服务器UUID。 |
| Version | String | 1.1.2.x | 软件版本。 |
| RequestId | String | 31409246-AB88- 4B36-A2B8- 16D21BA9E170 | 本次调用请求的ID。 |
| TotalCount | Integer | 2 | 软件信息总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>2</TotalCount> <PropertySoftwares>
    <InstanceName>test***</InstanceName>
    <Path>/usr/sshd</Path>
    <Uuid>inet-f6ac9a93-0818-4052-90e2-xxxx</Uuid>
    <Version>1.1.2.x</Version>
    <InstallTime>2016-06-29 06:55:22</InstallTime>
    <Create>1514172615000</Create>
    <Ip>47.100.XX.XX</Ip>
</PropertySoftwares> <PageSize>20</PageSize> <RequestId>31409246-AB88-4B36-A2B8-16D21BA9E170</RequestId> <CurrentPage>1</CurrentPage> <Count>2</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 2,
    "PropertySoftwares": {
        "InstanceName": "test***",
        "Path": "/usr/sshd",
        "Uuid": "inet-f6ac9a93-0818-4052-90e2-xxxx",
        "Version": "1.1.2.x",
        "InstallTime": "2016-06-29 06:55:22",
        "Create": 1514172615000,
        "Ip": "47.100.XX.XX"
    },
    "PageSize": 20,
    "RequestId": "31409246-AB88-4B36-A2B8-16D21BA9E170",
    "CurrentPage": 1,
    "Count": 2
}
```

#### DescribePropertyUserItem

获取账户下服务器用户信息列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yUserItem | 系统规定参数。取值：DescribePropertyUserItem。 |
| SourceIp | String | 否 | 192.168.x.x | 访问者源IP。 |
| User | String | 否 | root | 资产指纹的账号信息。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 2 | 分页查询时，显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |

| PropertyUserIt ems | Array of PropertyUserIt em |  | 用户信息。 |
|---|---|---|---|
| Count | Integer | 2 | 用户对应的服务器数量。 |
| User | String | root | 用户名称。 |
| RequestId | String | 221406C5-9A8B- 4E65-B3DD- 50D9789BBB03 | 本次调用请求的ID。 |
| TotalCount | Integer | 20 | 数据的总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyUserItem
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>20</TotalCount> <PropertyUserItems>
    <User>root</User>
    <Count>2</Count>
</PropertyUserItems> <PageSize>20</PageSize> <RequestId>221406C5-9A8B-4E65-B3DD-50D9789BBB03</RequestId> <CurrentPage>1</CurrentPage> <Count>2</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 20,
    "PropertyUserItems": {
        "User": "root",
        "Count": 2
    },
    "PageSize": 20,
    "RequestId": "221406C5-9A8B-4E65-B3DD-50D9789BBB03",
    "CurrentPage": 1,
    "Count": 2
}
```

#### DescribePropertyUserDetail

获取账户下服务器账户详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yUserDetail | 系统规定参数。取值：DescribePropertyUserDetail。 |
| SourceIp | String | 否 | 47.200.XX.XX | 访问者源IP。 |
| Remark | String | 否 | 192.168.x.x | 服务器名称或IP。 |
| Ip | String | 否 | 47.200.XX.XX | 服务器IP。 |
| GroupId | String | 否 | 1 | 分组ID。 |
| TagIdListString | String | 否 | 1 | 标签列表。 |
| User | String | 否 | root | 用户名。 |
| IsRoot | String | 否 | 1 | 是否拥有ROOT权限。取值包括： 0：否。 1：是。 |
| Extend | String | 否 | 1 | User是否使用模糊搜索 。 1：是。 0：否。 |
| Uuid | String | 否 | inet-00f20b1a- e2dd-408b- b38e-***** | 返回结果中的资产UUID。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 2 | 当前页显示数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |

| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
|---|---|---|---|
| PropertyUsers | Array of PropertyUser |  | 返回的账号详情列表。 |
| AccountsExpir ationDate | String | 2017-12-27 10:22:25 | 返回账号的到期时间。格式：yyyy-MM-dd HH:mm:ss。 |
| Create | String | 1514373155000 | 返回结果中的最新采集时间。单位：毫秒。 |
| GroupNames | List | admin | 用户组。 |
| InstanceName | String | test*** | 返回结果中的资产名称。 |
| Ip | String | 192.168.x.x | 返回结果中的IP地址。 |
| IsRoot | String | 1 | 返回账号是否为ROOT权限。 0：否。 1：是。 |
| LastLoginIp | String | 192.168.x.x | 上次登录来源。 |
| LastLoginTime | String | 2017-12-27 10:22:25 | 上次登录时间。使用yyyy-MM-dd HH:mm:ss 格式。 |
| PasswordExpir ationDate | String | never | 已废弃。 |
| User | String | root | 账户名称。 |
| Uuid | String | inet-00f20b1a- e2dd-408b-b38e- *** | 返回结果中的资产UUID。 |
| RequestId | String | 405F855F-BE88- 4410-89B6-*** | 本次调用请求的ID。 |
| TotalCount | Integer | 20 | 数据的总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyUserDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>20</TotalCount> <PageSize>20</PageSize> <RequestId>405F855F-BE88-4410-89B6-3AB3168EDE76</RequestId> <CurrentPage>1</CurrentPage> <Count>2</Count> <PropertyUsers>
    <InstanceName>test***</InstanceName>
    <IsRoot>1</IsRoot>
    <LastLoginTime>2017-12-27 10:22:25</LastLoginTime>
    <Uuid>inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818</Uuid>
    <User>root</User>
    <LastLoginIp>192.168.x.x</LastLoginIp>
    <Create>1514373155000</Create>
    <Ip>192.168.x.x</Ip>
    <AccountsExpirationDate>2017-12-27 10:22:25</AccountsExpirationDate>
    <PasswordExpirationDate>never</PasswordExpirationDate>
    <GroupNames>adm</GroupNames>
</PropertyUsers>
```

`JSON` 格式

```json
{
    "TotalCount": 20,
    "PageSize": 20,
    "RequestId": "405F855F-BE88-4410-89B6-3AB3168EDE76",
    "CurrentPage": 1,
    "Count": 2,
    "PropertyUsers": {
        "InstanceName": "test***",
        "IsRoot": 1,
        "LastLoginTime": "2017-12-27 10:22:25",
        "Uuid": "inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
        "User": "root",
        "LastLoginIp": "192.168.x.x",
        "Create": 1514373155000,
        "Ip": "192.168.x.x",
        "AccountsExpirationDate": "2017-12-27 10:22:25",
        "PasswordExpirationDate": "never",
        "GroupNames": "adm"
    }
}
```

#### DescribeTopRiskyAssets

获取TOP风险资产。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeTopRisk yAssets | 系统规定参数。取值：DescribeTopRiskyAssets。 |
| SourceIp | String | 否 | 192.168.X.X | 访问者源IP。 |
| From | String | 否 | aegis | 取值：aegis。 |
| PageSize | Integer | 否 | 5 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5D8D4058-2EE3- 4599-9951- BDAA3340AD4D | 本次调用请求的ID。 |
| TopRiskyAsset s | Array of TopRiskyAsset |  | TOP风险资产列表。 |
| AssetInfos | Array of AssetInfo |  | 资产信息列表。 |
| Count | String | 123 | 资产数量。 |
| InstanceName | String | test | 实例名称。 |
| Ip | String | 192.168.X.X | 风险实例的IP。 |
| Uuid | String | ac23ca36-afe9- 4e82-ad24-XXX | 返回结果中的资产UUID。 |
| Type | String | vul | 风险种类。 warning：告警。 hc：基线。 vul：漏洞。 |
| TotalCount | Integer | 5 | 数据总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeTopRiskyAssets
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>5</TotalCount> <RequestId>5D8D4058-2EE3-4599-9951-BDAA3340AD4D</RequestId> <TopRiskyAssets>
    <Type>vul</Type>
    <AssetInfos>
        <InstanceName>test</InstanceName>
        <Uuid>ac23ca36-afe9-4e82-ad24-XXX</Uuid>
        <Ip>192.168.X.X</Ip>
        <Count>123</Count>
    </AssetInfos>
</TopRiskyAssets>
```

`JSON` 格式

```json
{
    "TotalCount": 5,
    "RequestId": "5D8D4058-2EE3-4599-9951-BDAA3340AD4D",
    "TopRiskyAssets": {
        "Type": "vul",
        "AssetInfos": {
            "InstanceName": "test",
            "Uuid": "ac23ca36-afe9-4e82-ad24-XXX",
            "Ip": "192.168.X.X",
            "Count": 123
        }
    }
}
```

#### DeleteInstallCode

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-aegis:DeleteInstallCode | Write | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CaptchaC ode | Strin g | Query | 是 | 1q**** | 安装码。 说明您可以调用 DescribeInstallCode s接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=DeleteInstallCode&RegionId=cn-hangzhou&CaptchaCode=1q****
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
```

#### CreateAssetGroup

用户登录接口

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| GroupNa me | Strin g | Query | 否 | 未分组 | 分组名称。 |
| GroupId | Strin g | Query | 否 | 1 | 分组ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| GroupId | String | 12345 | 服务器分组ID。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "GroupId":"12345"
}
```

#### DescribePropertyUserChangeItem

查询云安全中心中用户的属性变更记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Uuid | Strin g | Query | 否 | 00f2-xxx-xxx | 机器唯一标识。 |
| User | Strin g | Query | 否 | root | 用户名。 |
| UserId | Strin g | Query | 否 | 123 | 用户Id。 |

|  |  |  |  |  | 安骑士开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| IsRoot | Strin g | Query | 否 | 1 | 是否拥有ROOT权限。取值包括： 0 ：否 1 ：是。 |
| ChangeTi meStart | Long | Query | 否 | 1649066826000 | 变更开始时间点。 |
| ChangeTi meEnd | Long | Query | 否 | 1649066826000 | 变更截止时间点。 |
| CurrentPa ge | Integ er | Query | 否 | 4 | 分页查询时，当前页的页码。 |
| PageSize | Integ er | Query | 否 | 20 | 分页查询时，每页显示的记录数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PropertyUserC hangeItemList | Array | - | 用户属性变更记录唯一标识符。 |
| -UserId | Long | 123 | 用户ID。 |
| -UserName | String | test | 用户名。 |
| -Count | Integer | 1 | 分页查询时，当前页显示的数据条数。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| PageInfo | Struct | - | 分页查询时的页面信息。 |
| -Count | Integer | 1 | 分页查询时，当前页显示的数据条数。 |
| -PageSize | Integer | 10 | 分页查询时，每页最多显示的数据条数。 |
| -TotalCount | Integer | 10 | 数据总条数。 |
| -CurrentPage | Integer | 1 | 当前页的页码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyUserChangeItem
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "PageInfo":{
  "TotalCount":10,
  "PageSize":10,
  "CurrentPage":1,
  "Count":1
 },
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PropertyUserChangeItemList":[
  {
   "UserName":"test",
   "UserId":123,
   "Count":1
  }
```

]

```
}
```

### 漏洞管理功能相关接口

#### CreateSnapshot

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-aegis:CreateSnapshot | Write | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Uuid | Strin g | Query | 是 | 00f2-xxx-xxx | 机器唯一标识。 |
| InstanceId | Strin g | Query | 是 | i- bp17441ohwka0yuh**** | ECS实例ID。 |
| RegionId | Strin g | Query | 否 | hangzhou-01 | 地域唯一标识。 |
| Snapshot Name | Strin g | Query | 是 | auto-create-a9a95- ****** | 快照的显示名称。 说明长度为2~128 个英文或中文字符。必须以大小写字母或中文开头。可以包含数字、 半角冒号（:）、下划线（）或者短划线 _ （-）。为防止和自动快照的名称冲突，不能以auto开头。 |
| Retention Days | Integ er | Query | 是 | 30 | 设置快照的保留时间，单位为天。 说明保留时间到期后快照会被自动释放， 取值范围： 1~65536。默认值： 空，表示快照不会被自动释放。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| SnapshotId | Long | sp- 5w1x1nxsmkhdgva l1h5l**** | 快照ID。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=CreateSnapshot&RegionId=cn-hangzhou&Uuid=00f2-xxx-xxx&Instan ceId=i-bp17441ohwka0yuh****&SnapshotName=auto-create-a9a95-******&RetentionDays=30
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "SnapshotId":"sp-5w1x1nxsmkhdgval1h5l****"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <SnapshotId>sp-5w1x1nxsmkhdgval1h5l****</SnapshotId>
```

#### DescribeTarget

获取漏洞机器配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeTarget | 系统规定参数。取值：DescribeTarget。 |
| SourceIp | String | 否 | 47.200.XX.XX | 访问者源IP。 |
| Type | String | 否 | vul | 目标类型，此处传固定值vul。 |
| Config | String | 否 | {"vulType":"cve "} | 获取参数信息。JSON格式传入。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1FF54D56-47ED- 47FB-XXXX- 2BDF3857D526 | 本次调用请求的ID。 |
| Targets | Array of Target |  | 机器配置列表。 |
| Flag | String | del | 已废弃。 |

| Target | String | inet-00f20b1a- e2dd-408b-xxxx- 6a6e1ed5d818 | 目标内容。当TargetType=uuid，Target为 UUID的实际内容。 |
|---|---|---|---|
| TargetType | String | uuid | 目标类型。返回TargetType=uuid表示Target 的内容是UUID的实际值。 |
| TotalCount | Integer | 10 | 总数据条数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>10</TotalCount> <RequestId>1FF54D56-47ED-47FB-XXXX-2BDF3857D526</RequestId> <Targets>
    <Target>inet-00f20b1a-e2dd-408b-xxxx-6a6e1ed5d818</Target>
    <TargetType>uuid</TargetType>
    <Flag>del</Flag>
</Targets>
```

`JSON` 格式

```json
{
    "TotalCount": 10,
    "RequestId": "1FF54D56-47ED-47FB-XXXX-2BDF3857D526",
    "Targets": {
        "Target": "inet-00f20b1a-e2dd-408b-xxxx-6a6e1ed5d818",
        "TargetType": "uuid",
        "Flag": "del"
    }
}
```

#### DescribeVulTargetStatistics

获取漏洞配置机器统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribeVulTarg etStatistics | 系统规定参数。取值：DescribeVulTargetStatistics。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 47.200.XX.XX | 访问者源IP。 |
| Type | String | 否 | cve | 漏洞类型，固定取值cve。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| RequestId | String | 89DD84B4-B592- 476C-XXXX- 51D56B3E8EAC | 本次调用请求的ID。 |
| TargetStats | Array of TargetStat |  | 机器统计列表。 |
| Targets | Array of Target |  | 机器列表。 |
| Flag | String | off | 已废弃。 |
| Target | String | 577f9886-bf66- 4c3c-xxxx- 28c938cb527b | 机器信息，可以是分组ID或者机器UUID。 |
| TargetType | String | uuid | 机器类型。 |
| TotalCount | String | 10 | 总数据条数。 |
| UuidCount | String | 10 | 资产UUID数量。 |
| VulType | String | cve | 漏洞类型。 |
| TotalCount | Integer | 4 | 总数据条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVulTargetStatistics
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>4</TotalCount> <PageSize>20</PageSize> <RequestId>89DD84B4-B592-476C-XXXX-51D56B3E8EAC</RequestId> <CurrentPage>1</CurrentPage> <TargetStats>
    <TotalCount>10</TotalCount>
    <UuidCount>10</UuidCount>
    <VulType>cms</VulType>
    <Targets>
        <Target>577f9886-bf66-4c3c-xxxx-28c938cb527b</Target>
        <TargetType>uuid</TargetType>
        <Flag>off</Flag>
    </Targets>
</TargetStats>
```

`JSON` 格式

```json
{
    "TotalCount": 4,
    "PageSize": 20,
    "RequestId": "89DD84B4-B592-476C-XXXX-51D56B3E8EAC",
    "CurrentPage": 1,
    "TargetStats": {
        "TotalCount": 10,
        "UuidCount": 10,
        "VulType": "cms",
        "Targets": {
            "Target": "577f9886-bf66-4c3c-xxxx-28c938cb527b",
            "TargetType": "uuid",
            "Flag": "off"
        }
    }
}
```

#### DescribeTargetConfig

获取单台机器漏洞配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribeTargetC onfig | 系统规定参数。取值：DescribeTargetConfig。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 10.10.XX.XX | 访问者源IP。 |
| Type | String | 否 | cve | 要查询的漏洞类型。取值： cve：Linux软件漏洞 sys：Windows系统漏洞 cms：Web-CMS漏洞 app：应用漏洞 emg：应急漏洞 sca：软件成分分析漏洞 |
| Uuid | String | 否 | inet-00f20b1a- e2dd-408b- xxxx- 6a6e1ed5d818 | 机器UUID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 092094BF-910F- 4CE6-XXXX- C3989B607977 | 本次调用请求的ID。 |
| TargetConfigs | Array of TargetConfig |  | 漏洞扫描配置列表。 |
| Config | String | off | 扫描配置。 |
| OverAllConfig | String | on | 全局扫描配置。 |
| Type | String | cve | 漏洞类型。 cve：Linux软件漏洞 sys：Windows系统漏洞 cms：Web-CMS漏洞 app：应用漏洞 emg：应急漏洞 sca：软件成分分析漏洞 |
| TotalCount | Integer | 1 | 数据总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeTargetConfig
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>1</TotalCount> <TargetConfigs>
    <Type>cve</Type>
    <Config>off</Config>
    <OverAllConfig>on</OverAllConfig>
</TargetConfigs> <RequestId>092094BF-910F-4CE6-XXXX-C3989B607977</RequestId>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "TargetConfigs": {
        "Type": "cve",
        "Config": "off",
        "OverAllConfig": "on"
    },
    "RequestId": "092094BF-910F-4CE6-XXXX-C3989B607977"
}
```

#### DescribeVulConfig

获取漏洞全局配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulConf ig | 系统规定参数。取值：DescribeVulConfig。 |
| SourceIp | String | 否 | 10.10.XX.XX | 访问者源IP。 |
| Type | String | 否 | cve | 要查询的漏洞类型。取值： cve：Linux软件漏洞 sys：Windows系统漏洞 cms：Web-CMS漏洞 app：应用漏洞 emg：应急漏洞 sca：软件成分分析漏洞 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A8E09216-31DF- 45B6-XXXX- E3F053752C07 | 本次调用请求的ID。 |
| TargetConfigs | Array of TargetConfig |  | 漏洞配置列表。 |
| Config | String | on | 漏洞配置。 |
| OverAllConfig | String | on | 全局配置on，yes。 |
| Type | String | cve | 漏洞类型。 |
| TotalCount | Integer | 4 | 数据总数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>4</TotalCount> <TargetConfigs>
    <Type>cve</Type>
    <Config>on</Config>
    <OverAllConfig>on</OverAllConfig>
</TargetConfigs> <RequestId>A8E09216-31DF-45B6-XXXX-E3F053752C07</RequestId>
```

`JSON` 格式

```json
{
    "TotalCount": 4,
    "TargetConfigs": {
        "Type": "cve",
        "Config": "on",
        "OverAllConfig": "on"
    },
    "RequestId": "A8E09216-31DF-45B6-XXXX-E3F053752C07"
}
```

#### DescribeAutoDelConfig

获取漏洞管理设置中失效漏洞自动删除天数配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAutoDel Config | 系统规定参数。取值：DescribeAutoDelConfig。 |
| SourceIp | String | 否 | 10.10.XX.XX | 访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Days | Integer | 7 | 漏洞自动删除天数。 |
| RequestId | String | 43186B14-5A39- 44E0-XXXX- 8B24D1EF82CC | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAutoDelConfig
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>43186B14-5A39-44E0-XXXX-8B24D1EF82CC</RequestId> <Days>7</Days>
```

`JSON` 格式

```json
{
    "RequestId": "43186B14-5A39-44E0-XXXX-8B24D1EF82CC",
    "Days": 7
}
```

#### DescribeVulLevel

获取用户关心的漏洞等级。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribeVulLeve l | 系统规定参数。取值：DescribeVulLevel。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 47.200.XX.XX | 访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConcernLevels | List | high,medium | 用户关心的漏洞等级列表，多个用英文输入法逗号分隔。 |
| RequestId | String | 7935CB7A-D1B7- 4EE6-XXXX- FF3D040CF19B | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7935CB7A-D1B7-4EE6-XXXX-FF3D040CF19B</RequestId> <ConcernLevels>high,medium</ConcernLevels>
```

`JSON` 格式

```json
{
    "RequestId": "7935CB7A-D1B7-4EE6-XXXX-FF3D040CF19B",
    "ConcernLevels": "high,medium"
}
```

#### DescribeVulWhitelist

分页获取漏洞白名单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulWhit elist | 系统规定参数。取值：DescribeVulWhitelist。 |
| SourceIp | String | 否 | 1.1.XX.XX | 访问者源IP。 |

| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| RequestId | String | 74F97EF7-B543- 43FD-XXXX- 18456731F9C5 | 本次调用请求的ID。 |
| TotalCount | Integer | 1 | 数据总数。 |
| VulWhitelists | Array of VulWhitelist |  | 漏洞白名单列表。 |
| AliasName | String | RHSA-2017:3263: curl security update | 漏洞别名。 |
| Name | String | oval:com.redhat.rh sa:def:20173263 | 漏洞名称。 |
| Reason | String | 暂不修复 | 加白原因。 |
| Type | String | cve | 漏洞类型。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVulWhitelist
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>1</TotalCount> <PageSize>20</PageSize> <RequestId>74F97EF7-B543-43FD-XXXX-18456731F9C5</RequestId> <VulWhitelists>
    <Type>cve</Type>
    <AliasName>RHSA-2017:3263: curl security update</AliasName>
```

`<Reason>`暂不修复`</Reason>`

```xml
    <Name>oval:com.redhat.rhsa:def:20173263</Name>
</VulWhitelists> <CurrentPage>1</CurrentPage>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "PageSize": 20,
    "RequestId": "74F97EF7-B543-43FD-XXXX-18456731F9C5",
    "VulWhitelists": {
        "Type": "cve",
        "AliasName": "RHSA-2017:3263: curl security update",
```

`"Reason": "`暂不修复`",`

```json
        "Name": "oval:com.redhat.rhsa:def:20173263"
    },
    "CurrentPage": 1
}
```

#### DescribeGroupedVul

分页查询漏洞分组信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeGroupe dVul | 系统规定参数。取值：DescribeGroupedVul。 |
| SourceIp | String | 否 | 47.200.XX.XX | 访问者源IP。 |
| Lang | String | 否 | zh | 设置请求和接收消息的语言类型。取值： zh：中文。 en：英文。 |

| Type | String | 否 | cve | 要查询的漏洞类型。取值： cve：Linux漏洞。 sys：Windows漏洞。 cms：WebCMS漏洞。 app：应用漏洞。 emg：应急漏洞。 sca：软件成分分析。 |
|---|---|---|---|---|
| GroupId | String | 否 | 62 | 资产分组的ID。 |
| CveId | String | 否 | CVE-2017- 18190 | 漏洞CVE ID。 |
| Uuids | String | 否 | 46ef7c05-0c53- 486c-xxxx- ef6ff972551c,b6 88bf9f-1fd9- 42c8-bb34- 28697f562dc5 | 机器UUID列表。 |
| Name | String | 否 | oval:com.redhat .****:20170817 | 漏洞名称。 |
| AliasName | String | 否 | RHSA- 2019:0230- Important: polkit security update | 漏洞别名。 |
| PatchId | Long | 否 | 27001 | 补丁ID。 |
| Level | String | 否 | high | 漏洞等级。 high：高等级漏洞。 middle：中等级漏洞。 low：低等级漏洞。 |
| LastTsStart | Long | 否 | 1517414500000 | 漏洞最后发现时间的起始时间戳，单位为毫秒。 |
| LastTsEnd | Long | 否 | 1517414400000 | 漏洞最后发现时间的结束时间戳，单位为毫秒。 |

| StatusList | String | 否 | 1,2 | 状态列表，多个状态需要用英文逗号分割。 1：未修复。 2：修复失败。 3：回滚失败。 4：修复中。 5：回滚中。 6：验证中。 7：修复成功。 8：修复成功待重启。 9：回滚成功。 10：已忽略。 11：回滚成功待重启。 12：漏洞已不存在。 20：已失效。 |
|---|---|---|---|---|
| OrderBy | String | 否 | name | 排序字段。 |
| Direction | String | 否 | asc | 排序方向。 |
| Necessity | String | 否 | asap | 漏洞修复必要性。 asap：高。 later：中。 nntf：低。 |
| Dealed | String | 否 | y | 漏洞是否处理。取值： y：已处理。 n：未处理。 |
| CreateTsStart | Long | 否 | 1517414400000 | 创建漏洞记录的开始时间，格式：时间戳。单位：毫秒。 |
| CreateTsEnd | Long | 否 | 1517414500000 | 创建漏洞记录的结束时间，格式：时间戳。单位：毫秒。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| SearchTags | String | 否 | 无 | 已废弃。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| CurrentPage | Integer | 1 | 当前页的页码。 |
|---|---|---|---|
| GroupedVulIte ms | Array of GroupedVulIte m |  | 漏洞分组。 |
| AliasName | String | RHSA-2017:0817: kernel security, bug fix, and enhancement update | 漏洞别名。 |
| AsapCount | Integer | 0 | 需尽快修复漏洞数。 |
| GmtLast | Long | 1513695612000 | 漏洞最后发现的时间，格式：时间戳。单位：毫秒。 |
| HandledCount | Integer | 1 | 已处理漏洞数。 |
| LaterCount | Integer | 0 | 修复优先级为中的漏洞的数量。 |
| Name | String | oval:com.redhat.rh sa:def:20170817 | 漏洞名称。 |
| NntfCount | Integer | 0 | 修复优先级为低的漏洞的数量。 |
| Status | Integer | 7 | 漏洞状态。 |
| Tags | String | 需要重启 | 漏洞标签。取值： 需要重启。 远程利用。 存在EXP。 可被利用。 本地提权。 代码执行。 |
| TotalFixCount | Long | 10 | 已修复漏洞的总数量。 |
| Type | String | cve | 漏洞类型。取值： cve：Linux漏洞。 sys：Windows漏洞。 cms：WebCMS漏洞。 app：应用漏洞。 emg：应急漏洞。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |

| RequestId | String | 6FCF95BE-7A78- 4AD8-XXXX- BF12FC34AC34 | 本次调用请求的ID。 |
|---|---|---|---|
| TotalCount | Integer | 5 | 数据总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGroupedVul
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>5</TotalCount> <PageSize>20</PageSize> <RequestId>6FCF95BE-7A78-4AD8-XXXX-BF12FC34AC34</RequestId> <CurrentPage>1</CurrentPage> <GroupedVulItems>
    <Status>7</Status>
    <Type>cve</Type>
    <LaterCount>0</LaterCount>
    <GmtLast>1513695612000</GmtLast>
    <HandledCount>1</HandledCount>
    <AliasName>RHSA-2017:0817: kernel security, bug fix, and enhancement
update</AliasName>
    <AsapCount>0</AsapCount>
    <TotalFixCount>10</TotalFixCount>
    <NntfCount>0</NntfCount>
```

`<Tags>`需要重启`</Tags>`

```xml
    <Name>oval:com.redhat.rhsa:def:20170817</Name>
</GroupedVulItems>
```

`JSON` 格式

```json
{
    "TotalCount": 5,
    "PageSize": 20,
    "RequestId": "6FCF95BE-7A78-4AD8-XXXX-BF12FC34AC34",
    "CurrentPage": 1,
    "GroupedVulItems": {
        "Status": 7,
        "Type": "cve",
        "LaterCount": 0,
        "GmtLast": 1513695612000,
        "HandledCount": 1,
        "AliasName": "RHSA-2017:0817: kernel security, bug fix, and enhancement update"
```

,

```json
        "AsapCount": 0,
        "TotalFixCount": 10,
        "NntfCount": 0,
```

`"Tags": "`需要重启`",`

```json
        "Name": "oval:com.redhat.rhsa:def:20170817"
    }
}
```

#### DescribeVulList

根据漏洞类型查询对应漏洞信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulList | 系统规定参数。取值：DescribeVulList。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值包括： zh：中文。 en：英文。 |
| CveId | String | 否 | CVE-2017- 18190 | CVE ID。 |
| Ids | String | 否 | 1,2 | 漏洞ID列表，多个漏洞ID需要用英文逗号分割。 |
| Remark | String | 否 | test-123**** | 查询标记，可以为资产私网IP、公网IP或资产名称。 |

| GroupId | String | 否 | 13****** | 要查询的资产分组ID。 |
|---|---|---|---|---|
| Type | String | 否 | cve | 漏洞类型。取值包括： cve：Linux软件漏洞。 sys：Windows系统漏洞。 cms：Web-CMS漏洞。 app：应用漏洞。 emg：应急漏洞。 |
| Uuids | String | 否 | f293ade2-e5b1- 4cc0-****- ************* | 机器UUID列表，多个UUID需要用英文逗号分割。 |
| Name | String | 否 | RHSA- 2017:1100: nss and nss-util security update | 漏洞名称。 |
| AliasName | String | 否 | RHSA- 2019:0230- Important: polkit security update | 漏洞别名。 |
| Level | String | 否 | serious | 漏洞等级。取值： serious：严重。 medium：高危。 low：中危。 high：低危。 |
| StatusList | String | 否 | 1 | 漏洞状态列表，多个状态值需要用英文逗号分隔。取值： 1：未修复。 2：修复失败。 3：回滚失败。 4：修复中。 5：回滚中。 6：验证中。 7：修复成功。 8：修复成功待重启。 9：回滚成功。 10：已忽略。 11：回滚成功待重启。 12：漏洞已不存在。 20：已失效。 |

| Necessity | String | 否 | asap | 漏洞修复紧急程度。多个值之间需要用英文逗号分隔。取值： asap：高。 later：中。 nntf：低。 |
|---|---|---|---|---|
| Dealed | String | 否 | n | 事件处理状态。取值： n: 待处理。 y: 已处理。 |
| BatchName | String | 否 | test | 批量名称。 |
| Resource | String | 否 | vulnerability | 批次来源。 |
| CreateTsStart | Long | 否 | 1517414400000 | 创建漏洞记录的开始时间，格式：时间戳。单位：毫秒。 |
| CreateTsEnd | Long | 否 | 1517414500000 | 创建漏洞记录结束的时间，格式：时间戳。单位：毫秒。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| ModifyTsStart | Long | 否 | 1517414400000 | 修改漏洞记录的开始时间，格式：时间戳。单位：毫秒。 |
| ModifyTsEnd | Long | 否 | 1517414500000 | 修改漏洞记录的结束时间，格式：时间戳。单位：毫秒。 |
| AttachTypes | String | 否 | sca | 查询应用漏洞时的附加漏洞类型。查询应用漏洞（即Type设置为app）时需要设置该参数。该参数固定取值为sca。 |
| ContainerFieldN ame | String | 否 | 无 | 已废弃。 |
| ContainerFieldV alue | String | 否 | 无 | 已废弃。 |
| TargetType | String | 否 | groupId | Target参数值的类型。取值： groupId：表示资产分组ID。 uuid：表示主机资产UUID。 |

| ClusterId | String | 否 | 无 | 已废弃。 |
|---|---|---|---|---|
| MinScore | Integer | 否 | 100 | 最小分数。 |
| VpcInstanceIds | String | 否 | vpc-xxxx | VPC实例ID，多个实例ID需要用英文逗号分割。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| RequestId | String | 07C8BF34-0C84- 4B97-XXXX- 231EC729F6C3 | 本次调用请求的ID。 |
| TotalCount | Integer | 32 | 数据总条数。 |
| VulRecords | Array of VulRecord |  | 漏洞记录列表。 |
| AliasName | String | RHSA-2017:0036: kernel security and bug fix update | 漏洞别名。 |
| CanFix | String | yes | 是否可修复。取值： yes：是。 no：否。 |
| ContainerId | String | 无 | 已废弃。 |
| ContainerImag eId | String | 无 | 已废弃。 |
| ContainerImag eName | String | 无 | 已废弃。 |
| ContainerInner Path | String | 无 | 已废弃。 |
| ContainerNam e | String | 无 | 已废弃。 |
| ExtendContent Json | Struct |  | 扩展信息。 |

| AbsolutePath | String | /roo/www/web | 漏洞相关软件包的路径。 |
|---|---|---|---|
| AliasName | String | RHSA-2019:0230- Important: polkit security update | 漏洞名称。 |
| Cwe | String | 无 | 已废弃。 |
| Description | String | 无 | 已废弃。 |
| Effect | String | 无 | 已废弃。 |
| EmgProof | String | 无 | 已废弃。 |
| Ip | String | 47.100.XX.XX | 漏洞关联资产的公网IP地址。 |
| LastTs | Long | 1620404763000 | 最后发现漏洞的时间，格式：时间戳。单位：毫秒。 |
| Level | String | high | 漏洞等级。 high：高等级漏洞。 middle：中等级漏洞。 low：低等级漏洞。 |
| Necessity | Struct |  | 必要性描述。 |
| Assets factor _ | String | 1 | 资产重要性因子。以下是资产重要性因子和资产类型的对应关系： 2：重要资产。 1：一般资产。 0：测试资产。 |
| Cvss factor _ | String | 7.8 | CVSS因子。 |
| Enviroment fa _ ctor | String | 1.0 | 环境因子。 |
| Gmt create _ | String | 1620404763000 | 创建时间的时间戳，单位为毫秒。 |
| Is calc _ | String | 1 | 是否计算出分数。取值： 0：未计算。 1：已计算。 |

| Status | String | pending | 漏洞修复建议得分状态。取值： none：未生成分数。 pending：等待计算中。 miss：未计算出分数。 normal：正常。 |
|---|---|---|---|
| Time factor _ | String | 1.0 | 时间因子。 |
| Total score _ | String | 7.8 | 漏洞修复紧急度得分。 根据漏洞得分提供以下修复建议： 13.5~15分（含13.5分和15分）：通常代表高危漏洞，需尽快修复。 7~13.5分（含7分）：通常代表中危漏洞， 可延后修复。 7分以下：通常代表低危漏洞，暂可不修复。 |
| Os | String | centos | 操作系统名称。 |
| OsRelease | String | 7 | 操作系统版本描述。 |
| Owasp | String | 无 | 安全计划。 |
| PreCheck | Struct |  | 预检查描述。 |
| Code | Long | 1 | 检查CODE。 |
| Msg | String | demo | 检查描述。 |
| PrimaryId | Long | 111 | 漏洞ID。 |
| Proof | String | 无 | 已废弃。 |
| Reason | String | 无 | 已废弃。 |
| Reference | String | 无 | 已废弃。 |
| RpmEntityList | Array of RpmEntity |  | RPM列表。 |
| ContainerNam e | String | k8s 67895c4 xxx _ _ | 容器名称。 |

| FullVersion | String | 3.10.0-693.2.2.el7 | RPM版本。 |
|---|---|---|---|
| ImageName | String | registry 387ytb xx _ _ x | 镜像名称。 |
| MatchDetail | String | python-perf version less than 0:3.10.0- 693.21.1.el7 | 匹配详情。 |
| MatchList | String | [] | 匹配列表。 |
| Name | String | python-perf | RPM名称。 |
| Path | String | /usr/lib64/python2. 7/site-packages | 存在漏洞的软件所在路径。 |
| Pid | String | 100** | 进程ID。 |
| UpdateCmd | String | *** update python- perf | 更新命令。 |
| Version | String | 3.x.x | RPM包的版本。 |
| Solution | String | 解决方案 | 解决方案。 |
| Status | Integer | 1 | 漏洞状态。 1：未修复。 2：修复失败。 3：回滚失败。 4：修复中。 5：回滚中。 6：验证中。 7：修复成功。 8：修复成功待重启。 9：回滚成功。 10：已忽略。 11：回滚成功待重启。 12：漏洞已不存在。 20：已失效。 |
| Tag | String | oval | 已废弃。 |
| Target | String | 无 | 已废弃。 |

| Title | String | 无 | 已废弃。 |
|---|---|---|---|
| VulType | String | 无 | 已废弃。 |
| Wasc | String | 无 | 已废弃。 |
| FirstTs | Long | 1517414400000 | 首次发现的时间，格式：时间戳。单位：毫秒。 |
| GroupId | Integer | 1 | 资产分组ID。 |
| InstanceId | String | i-bp18t*** | 资产实例ID。 |
| InstanceName | String | 测试ECS | 资产实例名称。 |
| InternetIp | String | 47.100.XX.XX | 资产公网IP。 |
| IntranetIp | String | 192.168.0.1 | 资产私网IP。 |
| Ip | String | 47.100.XX.XX | 漏洞关联资产的IP地址。 说明有公网展示公网IP，无公网展示私网IP。 |
| K8sClusterId | String | 无 | 已废弃。 |
| K8sNamespac e | String | 无 | 已废弃。 |
| K8sNodeId | String | 无 | 已废弃。 |
| K8sNodeName | String | 无 | 已废弃。 |
| K8sPodName | String | 无 | 已废弃。 |
| LastTs | Long | 1517414400000 | 最后一次发现漏洞的时间，格式：时间戳。单位：毫秒。 |
| Level | String | high | 漏洞等级。 high：高等级漏洞。 middle：中等级漏洞。 low：低等级漏洞。 |

| ModifyTs | Long | 1517414400000 | 漏洞修改时间，格式：时间戳。单位：毫秒。 |
|---|---|---|---|
| Name | String | oval:com.redhat.rh sa:def:20162824 | 漏洞名称。 |
| Necessity | String | nntf | 漏洞修复紧急程度。取值： asap：高。 later：中。 nntf：低。 |
| NeedReboot | String | 无 | 已废弃。 |
| Online | Boolean | true | 是否在线。 true：是。 false：否。 |
| OsName | String | CentOS 7.6 64 位 | 操作系统名称。 |
| OsVersion | String | linux | 操作系统版本。 |
| PrimaryId | Long | 123 | 数据的ID。 |
| ProcessInfo | Struct |  | 进程信息。 |
| GmtLastTs | Long | 1517414400000 | 进程最新时间，格式：时间戳。单位：毫秒。 |
| ProcessList | Array of Process |  | 进程列表。 |
| Pid | String | 100** | 进程ID。 |
| Pname | String | test | 进程名称。 |
| Rpm | String | python-perf | RPM包名称。 |
| SubProcessList | Array of SubProcess |  | 子进程列表。 |
| Pid | String | 116** | 进程ID。 |
| Pname | String | test | 进程名称。 |

| Rpm | String | python-perf-xxx | RPM包名称。 |
|---|---|---|---|
| TotalCount | Integer | 2 | 进程数据总条数。 |
| Product | String | 无 | 已废弃。 |
| Progress | Integer | 20 | 进度，以百分比形式出现。例如，取值为20，表示进度为20%。 |
| RecordId | Long | 111 | 漏洞记录ID。 |
| RegionId | String | region-xxxx | 环境区域ID。 |
| Related | String | CVE-2017-0019 | 关联的CVE ID。 |
| RepairTs | Long | 1541207563000 | 漏洞修复时间。格式：时间戳。单位：毫秒。 |
| ResultCode | String | 101 | 操作的结果。 |
| ResultMessage | String | success | 操作结果信息。 |
| Status | Integer | 1 | 漏洞状态。 1：未修复。 2：修复失败。 3：回滚失败。 4：修复中。 5：回滚中。 6：验证中。 7：修复成功。 8：修复成功待重启。 9：回滚成功。 10：已忽略。 11：回滚成功待重启。 12：漏洞已不存在。 20：已失效。 |
| Tag | String | oval | 已废弃。 |
| Type | String | cve | 漏洞类型。 |

| Uuid | String | 577f9886-bf66- 4c3c-****- ************ | 机器UUID。 |
|---|---|---|---|

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>32</TotalCount> <PageSize>20</PageSize> <RequestId>07C8BF34-0C84-4B97-XXXX-231EC729F6C3</RequestId> <VulRecords>
    <K8sNodeId>无</K8sNodeId>
    <K8sNodeName>无</K8sNodeName>
    <OsVersion>linux</OsVersion>
    <Ip>47.100.XX.XX</Ip>
    <ContainerInnerPath>无</ContainerInnerPath>
    <Product>无</Product>
    <IntranetIp>192.168.0.1</IntranetIp>
    <K8sClusterId>无</K8sClusterId>
    <Name>oval:com.redhat.rhsa:def:20162824</Name>
    <K8sNamespace>无</K8sNamespace>
    <RepairTs>1541207563000</RepairTs>
    <ModifyTs>1517414400000</ModifyTs>
    <InternetIp>47.100.XX.XX</InternetIp>
    <ContainerId>无</ContainerId>
    <ContainerName>无</ContainerName>
    <AliasName>RHSA-2017:0036: kernel security and bug fix update</AliasName>
    <CanFix>yes</CanFix>
    <RecordId>111</RecordId>
    <Status>1</Status>
    <Progress>20</Progress>
    <InstanceId>i-bp18t***</InstanceId>
    <OsName>CentOS 7.6 64 位</OsName>
    <Necessity>nntf</Necessity>
    <LastTs>1517414400000</LastTs>
    <NeedReboot>无</NeedReboot>
    <K8sPodName>无</K8sPodName>
    <ResultMessage>success</ResultMessage>
    <ContainerImageId>无</ContainerImageId>
    <GroupId>1</GroupId>
    <InstanceName>测试ECS</InstanceName>
    <FirstTs>1517414400000</FirstTs>
    <Type>cve</Type>
    <Related>CVE-2017-0019</Related>
    <Uuid>577f9886-bf66-4c3c-****-************</Uuid>
    <ContainerImageName>无</ContainerImageName>
    <Level>high</Level>
```

ee g

```xml
/ee
    <RegionId>region-xxxx</RegionId>
    <Tag>oval</Tag>
    <Online>true</Online>
    <ResultCode>101</ResultCode>
    <PrimaryId>123</PrimaryId>
    <ExtendContentJson>
        <Status>1</Status>
        <Description>无</Description>
        <Os>centos</Os>
        <Reference>无</Reference>
        <Owasp>无</Owasp>
        <Ip>47.100.XX.XX</Ip>
        <LastTs>1620404763000</LastTs>
        <Title>无</Title>
        <AbsolutePath>/roo/www/web</AbsolutePath>
        <Reason>无</Reason>
        <Cwe>无</Cwe>
        <Target>无</Target>
        <Wasc>无</Wasc>
        <AliasName>RHSA-2019:0230-Important: polkit security update</AliasName>
        <Proof>无</Proof>
        <Effect>无</Effect>
        <Level>high</Level>
        <Tag>oval</Tag>
        <OsRelease>7</OsRelease>
        <EmgProof>无</EmgProof>
```

`<Solution>`解决方案`</Solution>`

```xml
        <PrimaryId>111</PrimaryId>
        <VulType>无</VulType>
        <RpmEntityList>
            <Path>/usr/lib64/python2.7/site-packages</Path>
            <ImageName>registry_387ytb_xxx</ImageName>
            <UpdateCmd>*** update python-perf</UpdateCmd>
            <MatchList>[]</MatchList>
            <ContainerName>k8s_67895c4_xxx</ContainerName>
            <Version>3.x.x</Version>
            <Pid>100**</Pid>
            <FullVersion>3.10.0-693.2.2.el7</FullVersion>
            <MatchDetail>python-perf version less than 0:3.10.0-
693.21.1.el7</MatchDetail>
            <Name>python-perf</Name>
        </RpmEntityList>
        <Necessity>
            <Total_score>7.8</Total_score>
            <Status>pending</Status>
            <Gmt_create>1620404763000</Gmt_create>
            <Time_factor>1.0</Time_factor>
            <Cvss_factor>7.8</Cvss_factor>
            <Is_calc>1</Is_calc>
            <Enviroment_factor>1.0</Enviroment_factor>
            <Assets_factor>1</Assets_factor>
        </Necessity>
        <PreCheck>
            <Msg>demo</Msg>
```

```xml
            <Code>1</Code>
        </PreCheck>
    </ExtendContentJson>
    <ProcessInfo>
        <TotalCount>2</TotalCount>
        <GmtLastTs>1517414400000</GmtLastTs>
        <ProcessList>
            <Pname>test</Pname>
            <Pid>100**</Pid>
            <Rpm>python-perf </Rpm>
            <SubProcessList>
                <Pname>test</Pname>
                <Pid>116**</Pid>
                <Rpm>python-perf-xxx</Rpm>
            </SubProcessList>
        </ProcessList>
    </ProcessInfo>
</VulRecords> <CurrentPage>1</CurrentPage>
```

`JSON` 格式

```json
{
    "TotalCount": 32,
    "PageSize": 20,
    "RequestId": "07C8BF34-0C84-4B97-XXXX-231EC729F6C3",
    "VulRecords": {
        "K8sNodeId": "无",
        "K8sNodeName": "无",
        "OsVersion": "linux",
        "Ip": "47.100.XX.XX",
        "ContainerInnerPath": "无",
        "Product": "无",
        "IntranetIp": "192.168.0.1",
        "K8sClusterId": "无",
        "Name": "oval:com.redhat.rhsa:def:20162824",
        "K8sNamespace": "无",
        "RepairTs": 1541207563000,
        "ModifyTs": 1517414400000,
        "InternetIp": "47.100.XX.XX",
        "ContainerId": "无",
        "ContainerName": "无",
        "AliasName": "RHSA-2017:0036: kernel security and bug fix update",
        "CanFix": "yes",
        "RecordId": 111,
        "Status": 1,
        "Progress": 20,
        "InstanceId": "i-bp18t***",
        "OsName": "CentOS 7.6 64 位",
        "Necessity": "nntf",
        "LastTs": 1517414400000,
        "NeedReboot": "无",
        "K8sPodName": "无",
"ResultMessage":"success",
```

```json
        ResultMessage: success,
        "ContainerImageId": "无",
        "GroupId": 1,
        "InstanceName": "测试ECS",
        "FirstTs": 1517414400000,
        "Type": "cve",
        "Related": "CVE-2017-0019",
        "Uuid": "577f9886-bf66-4c3c-****-************",
        "ContainerImageName": "无",
        "Level": "high",
        "RegionId": "region-xxxx",
        "Tag": "oval",
        "Online": true,
        "ResultCode": 101,
        "PrimaryId": 123,
        "ExtendContentJson": {
            "Status": 1,
            "Description": "无",
            "Os": "centos",
            "Reference": "无",
            "Owasp": "无",
            "Ip": "47.100.XX.XX",
            "LastTs": 1620404763000,
            "Title": "无",
            "AbsolutePath": "/roo/www/web",
            "Reason": "无",
            "Cwe": "无",
            "Target": "无",
            "Wasc": "无",
            "AliasName": "RHSA-2019:0230-Important: polkit security update",
            "Proof": "无",
            "Effect": "无",
            "Level": "high",
            "Tag": "oval",
            "OsRelease": 7,
            "EmgProof": "无",
```

`"Solution": "`解决方案`",`

```json
            "PrimaryId": 111,
            "VulType": "无",
            "RpmEntityList": {
                "Path": "/usr/lib64/python2.7/site-packages",
                "ImageName": "registry_387ytb_xxx",
                "UpdateCmd": "*** update python-perf",
                "MatchList": "[]",
                "ContainerName": "k8s_67895c4_xxx",
                "Version": "3.x.x",
                "Pid": "100**",
                "FullVersion": "3.10.0-693.2.2.el7",
                "MatchDetail": "python-perf version less than 0:3.10.0-693.21.1.el7",
                "Name": "python-perf"
            },
            "Necessity": {
                "Total_score": 7.8,
                "Status": "pending",
                "Gmtcreate": 1620404763000,
```

_ ,

```json
                "Time_factor": 1,
                "Cvss_factor": 7.8,
                "Is_calc": 1,
                "Enviroment_factor": 1,
                "Assets_factor": 1
            },
            "PreCheck": {
                "Msg": "demo",
                "Code": 1
            }
        },
        "ProcessInfo": {
            "TotalCount": 2,
            "GmtLastTs": 1517414400000,
            "ProcessList": {
                "Pname": "test",
                "Pid": "100**",
                "Rpm": "python-perf",
                "SubProcessList": {
                    "Pname": "test",
                    "Pid": "116**",
                    "Rpm": "python-perf-xxx"
                }
            }
        }
    },
    "CurrentPage": 1
}
```

#### DescribeVulDetails

获取漏洞的详情，需要传入漏洞的名称及类型。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulDeta ils | 系统规定参数。取值：DescribeVulDetails。 |
| Name | String | 是 | oval:com.redhat .rhsa:def:20170 036 | 漏洞名称。 |
| Type | String | 是 | cve | 要查询的漏洞类型。取值： cve：Linux软件漏洞。 sys：Windows系统漏洞。 cms：Web-CMS漏洞。 app：应用漏洞。 emg：应急漏洞。 sca：软件成分分析漏洞。 |

| SourceIp | String | 否 | 47.200.XX.XX | 访问者源IP。 |
|---|---|---|---|---|
| Lang | String | 否 | zh | 设置请求和接收消息的语言类型。取值： zh：中文。 en：英文。 |
| AliasName | String | 否 | oval:com.redhat .rhsa:def:20170 036 | 漏洞别名。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Cves | Array of Cve |  | 关联的CVE信息。 |
| Classify | String | local elevation of _ _ _ privilege | 漏洞分类。 |
| Classifys | Array of Classify |  | 分类详情列表。 |
| Classify | String | iprivesc | 漏洞分类。 |
| DemoVideoUrl | String | http://cloud.video.t aobao.com//play/u/ ***/p/1/e/6/t/1/500 75276363.mp4 | 演示视频地址。 |
| Description | String | 本地提权漏洞 | 漏洞分类描述。 |
| CnvdId | String | CNVD-2017-27466 | 漏洞CNVD ID。 |
| Complexity | String | 无 | 已废弃。 |
| Content | String | Apache Tomcat是由 Apache软件基金会属下Jakarta项目开发的 Servlet容器。 Tomcat官方于7月份修复了CVE-2020- 13935 websocket 拒绝服务漏洞。近日，国外某安全团队公开了相关poc代码， 在受影响版本内的 Tomcat开启 websocket的情况下将会导致拒绝服务。 | 漏洞详情。 |

| CveId | String | CVE-2017-1000112 | 漏洞CVE ID。 |
|---|---|---|---|
| CvssScore | String | 7.0 | CVSS分数。CVSS打分范围： 9.0~10.0：严重的。 7.0~8.9：高危的。 4.0~6.9：中危的。 0.1~3.9：低位的。 0.0：无危险。 |
| CvssVector | String | CVSS:3.0/AV:L/AC: H/PR:L/UI:*****N/S: U/C:H/I:H/A:H | CVSS打分串。 |
| OtherId | String | CVE-2017-1000112 | 漏洞ID。 |
| Poc | String | 无 | 已废弃。 |
| PocCreateTim e | Long | 1519677041000 | POC创建时间，格式：时间戳。单位：毫秒。 |
| PocDisclosure Time | Long | 1519677041000 | POC披露时间，格式：时间戳。单位：毫秒。 |
| Product | String | openssl | 漏洞所属产品。 |
| Reference | String | 无 | 引用信息。 |
| ReleaseTime | Long | 1519677041000 | 漏洞披露时间，格式：时间戳，单位：毫秒。 |
| Solution | String | 无 | 解决方法。 |
| Summary | String | 无 | 漏洞概述。 |
| Title | String | Linux kernel内存破坏漏洞（CNVD- 2017-27466） | 漏洞标题。 |
| Vendor | String | Linux | 影响厂商。 |
| VulLevel | String | high | 漏洞等级。 high：高等级漏洞。 middle：中等级漏洞。 low：低等级漏洞。 |

| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 本次调用请求的ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVulDetails &Name=oval:com.redhat.rhsa:def:20170036 &Type=cve
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Cves>
    <CvssVector>CVSS:3.0/AV:L/AC:H/PR:L/UI:*****N/S:U/C:H/I:H/A:H</CvssVector>
    <CvssScore>7.0</CvssScore>
    <Classify>local_elevation_of_privilege</Classify>
    <PocDisclosureTime>1519677041000</PocDisclosureTime>
    <Poc>无</Poc>
    <Reference>无</Reference>
    <Product>openssl</Product>
```

`<Title>Linux kernel`内存破坏漏洞（`CNVD-2017-27466`）`</Title>`

```xml
    <CveId>CVE-2017-1000112</CveId>
    <Vendor>Linux</Vendor>
    <OtherId>CVE-2017-1000112</OtherId>
    <CnvdId>CNVD-2017-27466</CnvdId>
    <Complexity>无</Complexity>
    <PocCreateTime>1519677041000</PocCreateTime>
    <ReleaseTime>1519677041000</ReleaseTime>
```

`<Content>Apache Tomcat`是由`Apache`软件基金会属下`Jakarta`项目开发的`Servlet`容器。`Tomcat`官方于7 月份修复了`CVE-2020-13935 websocket` 拒绝服务漏洞。近日，国外某安全团队公开了相关`poc`代码，在受影响版本内的`Tomcat`开启`websocket`的情况下将会导致拒绝服务。`</Content>`

```xml
    <Summary>无</Summary>
    <Solution>无</Solution>
    <VulLevel>high</VulLevel>
    <Classifys>
<DemoVideoUrl>http://cloud.video.taobao.com//play/u/***/p/1/e/6/t/1/50075276363.mp4</Demo deoUrl>
```

`<Description>`本地提权漏洞`</Description>`

```xml
        <Classify>iprivesc</Classify>
    </Classifys>
</Cves> <RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2</RequestId>
```

`JSON` 格式

```json
{
    "Cves": {
        "CvssVector": "CVSS:3.0/AV:L/AC:H/PR:L/UI:*****N/S:U/C:H/I:H/A:H",
        "CvssScore": 7,
        "Classify": "local_elevation_of_privilege",
        "PocDisclosureTime": 1519677041000,
        "Poc": "无",
        "Reference": "无",
        "Product": "openssl",
```

`"Title": "Linux kernel`内存破坏漏洞（`CNVD-2017-27466`）`",`

```json
        "CveId": "CVE-2017-1000112",
        "Vendor": "Linux",
        "OtherId": "CVE-2017-1000112",
        "CnvdId": "CNVD-2017-27466",
        "Complexity": "无",
        "PocCreateTime": 1519677041000,
        "ReleaseTime": 1519677041000,
```

`"Content": "Apache Tomcat`是由`Apache`软件基金会属下`Jakarta`项目开发的`Servlet`容器。`Tomcat` 官方于7月份修复了`CVE-2020-13935 websocket` 拒绝服务漏洞。近日，国外某安全团队公开了相关`poc`代码，在受影响版本内的`Tomcat`开启`websocket`的情况下将会导致拒绝服务。`",`

```json
        "Summary": "无",
        "Solution": "无",
        "VulLevel": "high",
        "Classifys": {
            "DemoVideoUrl":
"http://cloud.video.taobao.com//play/u/***/p/1/e/6/t/1/50075276363.mp4",
```

`"Description": "`本地提权漏洞`",`

```json
            "Classify": "iprivesc"
        }
    },
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2"
}
```

#### DescribeVulNumStatistics

获取漏洞数量统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulNum Statistics | 系统规定参数。取值：DescribeVulNumStatistics。 |
| SourceIp | String | 否 | 47.200.XX.XX | 访问源IP地址。 |
| From | String | 否 | sas | 数据来源，默认sas。 |

| Uuids | String | 否 | 577f9886-bf66- 4c3c-****- *********** | 机器UUID列表,多个UUID需要用英文逗号分割。 |
|---|---|---|---|---|
| IncludeApp | String | 否 | 无 | 已废弃。 |
| StartTs | Long | 否 | 1514736000000 | 查询开始时间，格式：时间戳。单位：毫秒。 |
| EndTs | Long | 否 | 1514736000000 | 查询结束时间，格式：时间戳。单位：毫秒。 |
| CreateTsStart | Long | 否 | 1517414400000 | 创建漏洞记录开始时间，格式：时间戳。 单位：毫秒。 |
| CreateTsEnd | Long | 否 | 1517414500000 | 创建漏洞结束时间，格式：时间戳。单位：毫秒。 |
| ContainerFieldN ame | String | 否 | 无 | 已废弃。 |
| ContainerFieldV alue | String | 否 | 无 | 已废弃。 |
| TargetType | String | 否 | groupId | Target参数值的类型： groupId：表示资产分组ID。 uuid：表示主机资产UUID。 |
| ClusterId | String | 否 | 无 | 已废弃。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AppCnt | Integer | 0 | 已废弃。 |
| AppNum | Integer | 0 | 已废弃。 |
| CmsDealedTot alNum | Integer | 0 | CMS已处理漏洞数量。 |
| CmsNum | Integer | 0 | CMS漏洞数量。 |
| CveNum | Integer | 2 | CVE漏洞数量。 |

| EmgNum | Integer | 1 | 其他漏洞数量。 |
|---|---|---|---|
| ImageVulAsap Sum | Integer | 0 | 需要尽快处理的容器漏洞数量。 |
| ImageVulLater Sum | Integer | 0 | 可延后处理的容器漏洞数量。 |
| ImageVulNntfS um | Integer | 0 | 暂时可以不修复的容器漏洞数量。 |
| ImageVulTotal Sum | Integer | 0 | 容器漏洞总数。 |
| RequestId | String | 093C121C-2981- 4E69-XXXX- CD1BDD8C872A | 本次调用请求的ID。 |
| ScaNum | Integer | 1 | SCA漏洞数量。 |
| ScaNum | Integer | 1 | SCA漏洞数量。 |
| SysNum | Integer | 2 | Windows系统漏洞数量。 |
| VulAsapSum | Integer | 0 | 需要尽快处理的漏洞数量。 |
| VulDealedTota lNum | Integer | 0 | 已处理漏洞总数量。 |
| VulLaterSum | Integer | 1 | 可延后处理的漏洞数量。 |
| VulNntfSum | Integer | 1 | 暂时可以不修复的漏洞数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVulNumStatistics
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<VulHighTotal>0</VulHighTotal> <CveNum>1</CveNum> <VulMediumTotal>0</VulMediumTotal> <EmgNum>0</EmgNum> <VulLowTotal>0</VulLowTotal> <VulNntfSum>1</VulNntfSum> <VulAsapSum>0</VulAsapSum> <SysNum>0</SysNum> <VulDealedTotalNum>1</VulDealedTotalNum> <RequestId>093C121C-2981-4E69-XXXX-CD1BDD8C872A</RequestId> <CmsNum>0</CmsNum> <VulSeriousTotal>0</VulSeriousTotal> <CmsDealedTotalNum>0</CmsDealedTotalNum> <VulLaterSum>0</VulLaterSum>
```

`JSON` 格式

```json
{
    "VulHighTotal": 0,
    "CveNum": 1,
    "VulMediumTotal": 0,
    "EmgNum": 0,
    "VulLowTotal": 0,
    "VulNntfSum": 1,
    "VulAsapSum": 0,
    "SysNum": 0,
    "VulDealedTotalNum": 1,
    "RequestId": "093C121C-2981-4E69-XXXX-CD1BDD8C872A",
    "CmsNum": 0,
    "VulSeriousTotal": 0,
    "CmsDealedTotalNum": 0,
    "VulLaterSum": 0
}
```

#### DescribeVulLevelStatistics

获取漏洞按等级统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulLeve lStatistics | 系统规定参数。取值：DescribeVulLevelStatistics。 |
| SourceIp | String | 否 | 1.1.XX.XX | 访问者源IP。 |
| From | String | 否 | sas | 数据来源，默认sas。 |

| Uuids | String | 否 | 46ef7c05-0c53- 486c-****- ***********,b688 bf9f-1fd9-42c8- ****-************ | 机器UUID列表，多个UUID之前需要用英文逗号分割。 |
|---|---|---|---|---|
| IncludeApp | String | 否 | 无 | 已废弃。 |
| StartTs | Long | 否 | 1514736000000 | 统计开始时间戳，单位为毫秒。 |
| EndTs | Long | 否 | 1514736000000 | 统计结束时间戳，单位为毫秒。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LevelStatistics | Array of LevelStatistic |  | 漏洞等级统计列表。 |
| AppNum | Integer | 0 | 已废弃。 |
| CmsDealedTot alNum | Integer | 0 | CMS漏洞已处理总数。 |
| CmsNum | Integer | 0 | CMS漏洞数量。 |
| CveNum | Integer | 0 | CVE漏洞数量。 |
| EmgNum | Integer | 0 | 其他漏洞数量。 |
| Level | String | low | 漏洞等级。取值： serious：严重。 medium：高危。 low：中危。 high：低危。 |
| SysNum | Integer | 0 | Windows系统漏洞数量。 |
| VulAsapSum | Integer | 0 | 需尽快修复漏洞数量。 |
| VulDealedTota lNum | Integer | 0 | 已处理漏洞总数。 |
| VulHighTotal | Integer | 0 | 高危漏洞总数。 |

| VulLaterSum | Integer | 0 | 可延后处理漏洞数量 |
|---|---|---|---|
| VulLowTotal | Integer | 0 | 低危漏洞数量。 |
| VulMediumTot al | Integer | 0 | 中危漏洞数量。 |
| VulNntfSum | Integer | 0 | 暂可不修复漏洞数量。 |
| VulSeriousTota l | Integer | 0 | 严重漏洞数量。 |
| RequestId | String | 9B062D3F-AD5A- 4D3E-XXXX- 45CAC2713FC0 | 本次调用请求的ID。 |
| TotalCount | Integer | 4 | 数据总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVulLevelStatistics
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>4</TotalCount> <RequestId>9B062D3F-AD5A-4D3E-XXXX-45CAC2713FC0</RequestId> <LevelStatistics>
    <VulHighTotal>0</VulHighTotal>
    <VulDealedTotalNum>0</VulDealedTotalNum>
    <VulLaterSum>0</VulLaterSum>
    <VulLowTotal>0</VulLowTotal>
    <EmgNum>0</EmgNum>
    <AppNum>0</AppNum>
    <VulSeriousTotal>0</VulSeriousTotal>
    <VulAsapSum>0</VulAsapSum>
    <VulNntfSum>0</VulNntfSum>
    <CveNum>0</CveNum>
    <CmsNum>0</CmsNum>
    <CmsDealedTotalNum>0</CmsDealedTotalNum>
    <SysNum>0</SysNum>
    <Level>low</Level>
    <VulMediumTotal>0</VulMediumTotal>
</LevelStatistics>
```

`JSON` 格式

```json
{
    "TotalCount": 4,
    "RequestId": "9B062D3F-AD5A-4D3E-XXXX-45CAC2713FC0",
    "LevelStatistics": {
        "VulHighTotal": 0,
        "VulDealedTotalNum": 0,
        "VulLaterSum": 0,
        "VulLowTotal": 0,
        "EmgNum": 0,
        "AppNum": 0,
        "VulSeriousTotal": 0,
        "VulAsapSum": 0,
        "VulNntfSum": 0,
        "CveNum": 0,
        "CmsNum": 0,
        "CmsDealedTotalNum": 0,
        "SysNum": 0,
        "Level": "low",
        "VulMediumTotal": 0
    }
}
```

#### DescribeVulMachineList

获取单台机器漏洞统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulMac hineList | 系统规定参数。取值：DescribeVulMachineList。 |
| SourceIp | String | 否 | 1.2.XX.XX | 访问源IP地址。 |
| From | String | 否 | sas | 数据来源，默认sas。 |
| Uuids | String | 否 | 577f9886-bf66- 4c3c-****- ************** | 机器UUID列表。 |
| IncludeApp | String | 否 | 无 | 已废弃。 |
| StartTs | Long | 否 | 1514736000000 | 查询开始时间戳，单位为毫秒。 |
| EndTs | Long | 否 | 1514736000000 | 查询结束时间戳，单位为毫秒。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MachineStatist ics | Array of MachineStatist ic |  | 机器漏洞统计列表。 |
| CmsDealedTot alNum | Integer | 0 | CMS漏洞已处理数量。 |
| CmsNum | Integer | 0 | CMS漏洞数。 |
| CveNum | Integer | 1 | CVE漏洞数。 |
| EmgNum | Integer | 0 | 其他漏洞数。 |
| SysNum | Integer | 0 | Windows系统漏洞数。 |
| Uuid | String | 577f9886-bf66- 4c3c-xxxx- ************* | 机器UUID。 |
| VulAsapSum | Integer | 0 | 需要尽快处理的漏洞数量。 |
| VulDealedTota lNum | Integer | 0 | 已处理漏洞总数量。 |
| VulHighTotal | Integer | 0 | 高危漏洞总数量。 |
| VulLaterSum | Integer | 0 | 可延后处理的漏洞数量。 |
| VulLowTotal | Integer | 0 | 低危漏洞总数量。 |
| VulMediumTot al | Integer | 0 | 中危漏洞总数量。 |
| VulNntfSum | Integer | 0 | 暂时可以不修复的漏洞数量。 |
| VulSeriousTota l | Integer | 0 | 严重漏洞总数量。 |
| RequestId | String | A3F8BE63-9BA1- 450D-XXXX- CE9205E6645D | 本次调用请求的ID。 |
| TotalCount | Integer | 1 | 数据总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVulMachineList
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>1</TotalCount> <RequestId>A3F8BE63-9BA1-450D-XXXX-CE9205E6645D</RequestId> <MachineStatistics>
    <VulHighTotal>0</VulHighTotal>
    <VulDealedTotalNum>0</VulDealedTotalNum>
    <VulLaterSum>0</VulLaterSum>
    <VulLowTotal>0</VulLowTotal>
    <EmgNum>0</EmgNum>
    <VulSeriousTotal>0</VulSeriousTotal>
    <VulAsapSum>0</VulAsapSum>
    <VulNntfSum>0</VulNntfSum>
    <Uuid>577f9886-bf66-4c3c-xxxx-*************</Uuid>
    <CveNum>1</CveNum>
    <CmsNum>0</CmsNum>
    <CmsDealedTotalNum>0</CmsDealedTotalNum>
    <SysNum>0</SysNum>
    <VulMediumTotal>0</VulMediumTotal>
</MachineStatistics>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "RequestId": "A3F8BE63-9BA1-450D-XXXX-CE9205E6645D",
    "MachineStatistics": {
        "VulHighTotal": 0,
        "VulDealedTotalNum": 0,
        "VulLaterSum": 0,
        "VulLowTotal": 0,
        "EmgNum": 0,
        "VulSeriousTotal": 0,
        "VulAsapSum": 0,
        "VulNntfSum": 0,
        "Uuid": "577f9886-bf66-4c3c-xxxx-*************",
        "CveNum": 1,
        "CmsNum": 0,
        "CmsDealedTotalNum": 0,
        "SysNum": 0,
        "VulMediumTotal": 0
    }
}
```

### 基线检查功能相关接口

#### DescribeStratetyDetail

查询策略详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeStratety Detail | 系统规定参数。取值：DescribeStratetyDetail。 |
| SourceIp | String | 否 | 47.200.XX.XX | 访问源IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |
| Id | String | 否 | 1 | 策略ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 本次调用请求的ID。 |
| Strategy | Struct |  | 策略信息。 |
| CycleDays | Integer | 1 | 策略运行周期。单位：天。 |
| CycleStartTim e | Integer | 0 | 策略执行开始时间： 0：表示0到6点执行。 6：表示6到12点执行。 12：表示12到18点执行。 18：表示18到24点执行。 |
| Id | Integer | 123 | 策略ID。 |
| Name | String | test2 | 策略名称。 |
| RiskTypeWhite ListQueryResul tList | Array of RiskTypeWhite ListQueryResul t |  | 策略对应的风险分类信息。 |

| Alias | String | 高危风险利用 | 分类显示名称。 |
|---|---|---|---|
| On | Boolean | true | 该分类是否开启。 |
| SubTypes | Array of SubType |  | 子分类信息。 |
| Alias | String | 高危风险利用- ActiveMQ未授权访问高危风险 | 子分类的显示名称。 |
| On | Boolean | true | 子分类是否开启。 true：是。 false：否。 |
| TypeName | String | hc exploit activem _ _ q | 子分类编号。 |
| TypeName | String | hc exploit _ | 主分类编号。 |
| Type | Integer | 2 | 策略类型。 1：表示系统默认策略。 2：表示用户自定义策略。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeStratetyDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2</RequestId> <Strategy>
    <CycleStartTime>0</CycleStartTime>
    <Type>2</Type>
    <CycleDays>1</CycleDays>
    <Id>123</Id>
    <Name>test2</Name>
    <RiskTypeWhiteListQueryResultList>
        <TypeName>hc_exploit</TypeName>
```

`<Alias>`高危风险利用`</Alias>`

```xml
        <On>true</On>
        <SubTypes>
            <TypeName>hc_exploit_activemq</TypeName>
```

`<Alias>`高危风险利用`-ActiveMQ`未授权访问高危风险`</Alias>`

```xml
            <On>true</On>
        </SubTypes>
    </RiskTypeWhiteListQueryResultList>
</Strategy>
```

`JSON` 格式

```json
{
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2",
    "Strategy": {
        "CycleStartTime": 0,
        "Type": 2,
        "CycleDays": 1,
        "Id": 123,
        "Name": "test2",
        "RiskTypeWhiteListQueryResultList": {
            "TypeName": "hc_exploit",
```

`"Alias": "`高危风险利用`",`

```json
            "On": true,
            "SubTypes": {
                "TypeName": "hc_exploit_activemq",
```

`"Alias": "`高危风险利用`-ActiveMQ`未授权访问高危风险`",`

```json
                "On": true
            }
        }
    }
}
```

#### DescribeStrategyTarget

查询策略包含的机器分组白名单或者黑名单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribeStrateg yTarget | 系统规定参数。取值：DescribeStrategyTarget。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 47.200.XX.XX | 访问源IP地址。 |
| Type | String | 否 | hc strategy _ | 设置查询类型。此处为固定值：hc strategy，表示查询基线策略。 _ |
| Config | String | 否 | {"strategyId":15 161} | 配置信息，这里通过JSON传入策略的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 001BAB34-D70A- 54B0-XXXX- 91B76DCDD8E8 | 本次调用请求的ID。 |
| StrategyTarge ts | Array of StrategyTarge t |  | 策略包含的分组信息列表。 |
| Flag | String | add | 系统恶略使用黑名单。用户策略使用白名单。 add 表示白名单，该分组会应用在当前策略上。 del 表示黑名单，该分组不会应用在当前策略上。 |
| Target | String | 9165712 | 目标ID，当前均为分组ID。 |
| TargetType | String | groupId | 当前取值均为groupId，表示Target字段的值是分组ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeStrategyTarget
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>001BAB34-D70A-54B0-XXXX-91B76DCDD8E8</RequestId> <StrategyTargets>
    <Target>9165712</Target>
    <TargetType>groupId</TargetType>
    <Flag>add</Flag>
</StrategyTargets>
```

`JSON` 格式

```json
{
    "RequestId": "001BAB34-D70A-54B0-XXXX-91B76DCDD8E8",
    "StrategyTargets": {
        "Target": 9165712,
        "TargetType": "groupId",
        "Flag": "add"
    }
}
```

#### DescribeUuidConfig

查询一台机器是否开启基线配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeUuidCo nfig | 系统规定参数。取值：DescribeUuidConfig。 |
| SourceIp | String | 否 | 无 | 已废弃。 |
| Uuid | String | 否 | 4bc19998-e100- 4b04-****- **************** | 服务器唯一标识。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 基线配置数据。 |
| Flag | String | add | 是否开启基线。 add：表示开启。 del：表示不开启。 |
| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeUuidConfig
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2</RequestId> <Data>
    <Flag>add</Flag>
</Data>
```

`JSON` 格式

```json
{
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2",
    "Data": {
        "Flag": "add"
    }
}
```

#### DescribeUserSetting

查询用户基线设置信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeUserSet ting | 系统规定参数。取值：DescribeUserSetting。 |
| SourceIp | String | 否 | 2.2.XX.XX | 接口访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AlertLevels | List | [ "high", "low", "medium"] | 基线检查等级。 |
| InvalidWarning KeepDays | Integer | 30 | 失效告警保存时间天数。 |
| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求> 正常返回示例 `XML` 格式

```xml
<RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2 </RequestId> <InvalidWarningKeepDays>30</InvalidWarningKeepDays> <AlertLevels>[ "high", "low", "medium"]</AlertLevels>
```

`JSON` 格式

```json
{
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2",
    "InvalidWarningKeepDays": 30,
    "AlertLevels": "[ \"high\", \"low\", \"medium\"]"
}
```

#### DescribeRiskWhiteList

查询用户风险白名单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRiskWhi teList | 系统规定参数。取值：DescribeRiskWhiteList。 |
| SourceIp | String | 否 | 47.200.XX.XX | 接口访问者源IP。 |
| RiskName | String | 否 | redis | 风险名称，模糊匹配过滤条件。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 20 | 返回数据总数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 本次调用请求的ID。 |

| TotalCount | Integer | 100 | 数据总条数。 |
|---|---|---|---|
| WhiteLists | Array of White |  | 白名单列表。 |
| Reason | String | 测试机 | 加白原因。 |
| RiskId | Long | 1 | 风险项ID。 |
| RiskName | String | redis 基础 | 风险项名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRiskWhiteList
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>100</TotalCount> <PageSize>20</PageSize> <RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2 </RequestId> <CurrentPage>1</CurrentPage> <WhiteLists>
    <RiskId>1</RiskId>
    <Reason>测试机</Reason>
    <RiskName>redis 基础</RiskName>
</WhiteLists> <Count>20</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 100,
    "PageSize": 20,
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2",
    "CurrentPage": 1,
    "WhiteLists": {
        "RiskId": 1,
```

`"Reason": "`测试机`",`

```json
        "RiskName": "redis 基础"
    },
    "Count": 20
}
```

#### DescribeStratety

查询基线执行策略列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeStratety | 系统规定参数。取值：DescribeStratety。 |
| SourceIp | String | 否 | 47.200.XX.XX | 接口访问者源IP。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |
| StrategyIds | String | 否 | 1,2,3 | 基线检查策略ID，多个策略ID需要用英文逗号分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 本次调用请求的ID。 |
| Strategies | Array of Strategy |  | 基线策略列表。 |
| ConfigTargets | Array of ConfigTarget |  | 策略包含或者排除的机器分组列表。 |
| Flag | String | add | 包含或者排除： add 包含该分组。 del 排除该分组。 |
| Target | String | 5078483 | 分组ID。 |
| TargetType | String | groupId | 固定取值groupId。 |
| CycleDays | Integer | 3 | 基线检查周期。 1：每隔1天。 3：每隔3天。 7：每隔7天。 30：每隔30天。 |

| CycleStartTim e | Integer | 6 | 基线检查开始时间，可在0:00、06:00、 12:00、18:00四个时间点开始执行基线检查。 |
|---|---|---|---|
| EcsCount | Integer | 10 | ECS数量。 |
| ExecStatus | Integer | 1 | 当前的执行状态。 1：执行完毕。 2：执行中。 |
| Id | Integer | 10 | 策略ID。 |
| Name | String | web服务器策略 | 策略名称。 |
| PassRate | Integer | 80 | 上一次检测通过率。 |
| ProcessRate | Integer | 80 | 当前执行完成百分比。 |
| RiskCount | Integer | 14 | 测试包含基线风险数量。 |
| Type | Integer | 1 | 策略类型。 1：系统。 2：用户 。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2</RequestId> <Strategies>
    <CycleStartTime>6</CycleStartTime>
    <EcsCount>10</EcsCount>
    <PassRate>80</PassRate>
    <ExecStatus>1</ExecStatus>
    <Type>1</Type>
    <ProcessRate>80</ProcessRate>
    <CycleDays>3</CycleDays>
    <Id>10</Id>
    <RiskCount>14</RiskCount>
```

`<Name>web`服务器策略`</Name>`

```xml
    <ConfigTargets>
        <Target>5078483</Target>
        <TargetType>groupId</TargetType>
        <Flag>add</Flag>
    </ConfigTargets>
</Strategies>
```

`JSON` 格式

```json
{
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2",
    "Strategies": {
        "CycleStartTime": 6,
        "EcsCount": 10,
        "PassRate": 80,
        "ExecStatus": 1,
        "Type": 1,
        "ProcessRate": 80,
        "CycleDays": 3,
        "Id": 10,
        "RiskCount": 14,
```

`"Name": "web`服务器策略`",`

```json
        "ConfigTargets": {
            "Target": 5078483,
            "TargetType": "groupId",
            "Flag": "add"
        }
    }
}
```

#### DescribeStrategyExecDetail

查询单个基线检测策略最近一次检查的结果详情，包括最近一次执行检查的时间、检测出的风险项数量及基线配置风险详情等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribeStrateg yExecDetail | 系统规定参数。取值：DescribeStrategyExecDetail。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 47.200.XX.XX | 接口访问者源IP。 |
| StrategyId | Integer | 否 | 1 | 策略ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| EndTime | String | 2018-04-08 12:17:20 | 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss。 |
| FailCount | Integer | 2 | 失败机器数量。 |
| FailedEcsList | Array of FailedEcs |  | 失败机器列表。 |
| IP | String | 172.33.XX.XX | 失败机器IP。 |
| InstanceName | String | mysql服务器 | 失败机器名称。 |
| InternetIp | String | 115.28.XX.XX | 公网IP地址。 |
| IntranetIp | String | 192.168.XX.XX | 私网IP地址。 |
| Reason | String | 客户端离线 | 失败原因。 |
| InProcessCoun t | Integer | 3 | 状态为执行中的基线检查任务的个数。 |
| Percent | String | 2 | 基线检查策略执行的进度，例如数值2表示当前进度2%。 |
| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 请求ID。 |
| Source | String | Schedule | 基线检查执行类型。取值： Schedule：周期性自动检查。 Manual：即时手动检查。 |

| StartTime | String | 2018-04-08 12:15:20 | 执行开始时间，时间格式为yyyy-MM-dd HH:mm:ss。 |
|---|---|---|---|
| SuccessCount | Integer | 19 | 执行成功数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeStrategyExecDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<EndTime>2018-04-08 12:17:20</EndTime> <RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2 </RequestId> <Percent>2</Percent> <FailCount>2</FailCount> <StartTime>2018-04-08 12:15:20</StartTime> <SuccessCount>19</SuccessCount> <Source>Schedule</Source> <FailedEcsList>
    <InstanceName>mysql服务器</InstanceName>
    <InternetIp>115.28.XX.XX</InternetIp>
    <IP>172.33.XX.XX</IP>
    <IntranetIp>192.168.XX.XX</IntranetIp>
```

`<Reason>`客户端离线`</Reason>`

```xml
</FailedEcsList> <InProcessCount>3</InProcessCount>
```

`JSON` 格式

```json
{
    "EndTime": "2018-04-08 12:17:20",
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2",
    "Percent": 2,
    "FailCount": 2,
    "StartTime": "2018-04-08 12:15:20",
    "SuccessCount": 19,
    "Source": "Schedule",
    "FailedEcsList": {
        "InstanceName": "mysql服务器",
        "InternetIp": "115.28.XX.XX",
        "IP": "172.33.XX.XX",
        "IntranetIp": "192.168.XX.XX",
```

`"Reason": "`客户端离线"

```json
    },
    "InProcessCount": 3
}
```

#### DescribeRiskType

查询所有风险分类，并查询改分类下通过策略ID以及UUID过滤后的待处理风险数量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRiskTyp e | 系统规定参数。取值：DescribeRiskType。 |
| SourceIp | String | 否 | 47.200.XX.XX | 调用源IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |
| Uuids | String | 否 | 2738e842-7d46- 42f7-****- ************** | 机器UUID风险数量过滤条件, 多个UUID需要用英文逗号隔开。 |
| StrategyId | Long | 否 | 10 | 策略ID，风险数量过滤条件。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 3 | 父风险分类数量。 |
| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 本次调用请求的ID。 |
| RiskTypes | Array of RiskType |  | 风险分类列表。 |
| Alias | String | 数据库 | 父分类展示名称。 |
| SubTypes | Array of subType |  | 子分类列表。 |
| Alias | String | Redis基础检查 | 子分类展示名称。 |
| TypeName | String | reids check _ | 子分类编号。 |
| WarnCount | String | 10 | 告警数量。 |

| TypeName | String | database | 父分类编号。 |
|---|---|---|---|
| WarnCount | String | 20 | 对应告警数量。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2 </RequestId> <RiskTypes>
    <TypeName>database</TypeName>
```

`<Alias>`数据库`</Alias>`

```xml
    <WarnCount>20</WarnCount>
    <SubTypes>
        <TypeName>reids_check</TypeName>
```

`<Alias>Redis`基础检查`</Alias>`

```xml
        <WarnCount>10</WarnCount>
    </SubTypes>
</RiskTypes> <Count>3</Count>
```

`JSON` 格式

```json
{
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2",
    "RiskTypes": {
        "TypeName": "database",
```

`"Alias": "`数据库`",`

```json
        "WarnCount": 20,
        "SubTypes": {
            "TypeName": "reids_check",
```

`"Alias": "Redis`基础检查`",`

```json
            "WarnCount": 10
        }
    },
    "Count": 3
}
```

#### Describesummary

按照风险分类汇总查询用户基线风险信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | Describesumma ry | 系统规定参数。取值：Describesummary。 |
| SourceIp | String | 否 | 47.200.XX.XX | 接口访问者源IP。 |
| Uuids | String | 否 | 2738e842-7d46- 42f7-****- ************** | 机器UUID列表，多个值用英文逗号隔开。 |
| TypeNames | String | 否 | weak passw*** _ | 主分类名称列表。 |
| SubTypeNames | String | 否 | postsql weak pa _ _ ssw** | 自分类名称列表，多个名称需要用英文逗号隔开。 |
| RiskLevels | String | 否 | low,high | 风险等级。取值： high：高。 medium：中。 low：低。 |
| RiskName | String | 否 | redis | 风险名称，模糊查询。 |
| Dealed | String | 否 | Y | 是否已经处理。取值： Y：是。 N：否。 |
| StrategyId | Long | 否 | 1 | 策略ID。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 10 | 返回结果数量。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |

| RequestId | String | FD0112DE-E4FA- 48E5-XXXX- 2DDB450934C2 | 本次调用请求的ID。 |
|---|---|---|---|
| TotalCount | Integer | 10 | 数据的总条数。 |
| WarningSumm arys | Array of WarningSumm ary |  | 风险结果列表。 |
| LastFoundTim e | String | 2018-04-08 01:04:20 | 上次发现时间，时间格式：yyyy-MM-dd HH:mm:ss。 |
| Level | String | low | 风险等级。取值： high：高。 medium：中。 low：低。 |
| PendingCount | Integer | 2 | 待处理数量。 |
| RiskDetail | String | 检测Redis是否对公网开放 | 风险详情。 |
| RiskId | Long | 1 | 风险ID。 |
| RiskName | String | Redis配置漏洞检测 | 风险名称。 |
| SubTypeAlias | String | Redis合规检查 | 子分类名称。 |
| TotalCount | Integer | 19 | 总风险数量。 |
| TypeAlias | String | 数据库 | 父分类名称。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>10</TotalCount> <PageSize>20</PageSize> <RequestId>FD0112DE-E4FA-48E5-XXXX-2DDB450934C2</RequestId> <CurrentPage>1</CurrentPage> <Count>10</Count> <WarningSummarys>
    <PendingCount>2</PendingCount>
    <LastFoundTime>2018-04-08 01:04:20</LastFoundTime>
    <RiskId>1</RiskId>
    <TotalCount>19</TotalCount>
```

`<RiskDetail>`检测`Redis`是否对公网开放`</RiskDetail>`

```xml
    <TypeAlias>数据库</TypeAlias>
    <Level>serious</Level>
    <SubTypeAlias>Redis合规检查</SubTypeAlias>
```

`<RiskName>Redis`配置漏洞检测`</RiskName>`

```
</WarningSummarys>
```

`JSON` 格式

```json
{
    "TotalCount": 10,
    "PageSize": 20,
    "RequestId": "FD0112DE-E4FA-48E5-XXXX-2DDB450934C2",
    "CurrentPage": 1,
    "Count": 10,
    "WarningSummarys": {
        "PendingCount": 2,
        "LastFoundTime": "2018-04-08 01:04:20",
        "RiskId": 1,
        "TotalCount": 19,
```

`"RiskDetail": "`检测`Redis`是否对公网开放`",` `"TypeAlias": "`数据库`",`

```json
        "Level": "serious",
        "SubTypeAlias": "Redis合规检查",
```

`"RiskName": "Redis`配置漏洞检测"

```
    }
}
```

#### ListBaselineCheckWhiteRecord

获取基线检查白名单记录的详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |

|  | 安骑士开发指南 | ·API参考 |  |  |  |  |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Lang | Strin g | Query | 否 | en | 设置请求和接收消息的语言类型，默认为zh。 zh：中文。 en：英文。 |
| Source | Strin g | Query | 否 | console batch _ | 增加任务的来源。 |
| CheckIte mFuzzy | Strin g | Query | 否 | redis | 检查项名称模糊匹配。 |
| CheckIds | Array | Query | 否 | 21313 | 检查项的ID。 说明您可调用 DescribeRiskType接口获取检查项ID。 |
| RecordIds | Array | Query | 否 | ["rec1001", "rec1002", "rec1003"] | 白名单记录的ID列表。 |
| CurrentPa ge | Integ er | Query | 否 | 4 | 分页查询时，当前页的页码。 |
| PageSize | Integ er | Query | 否 | 10 | 分页查询时，每页显示的记录数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| List | Array | - | 服务器信息列表。 |
| -RecordId | Long | 20201105144514 | 记录ID。 |
| -CheckId | Long | 696 | 检查项ID。 |
| -TargetType | String | RD-Account | 生效资产的选择模式。取值： uuid：按单个资产添加 groupId：按照服务器分组添加 global：表示选择所有资产。 |
| -Target | String | foo2,foo3 | 目标ID，当前均为分组ID。 |
| -Reason | String | Started | 添加为白名单的原因。 |

|  |  |  | 安骑士开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Source | String | Local | 数据来源。取值： API：API检测 OSS：OSS检测。 |
| -Lang | String | zh | 语言。 |
| -CheckItem | String | CHECK CONN SRC _ _ | 检测项。 |
| -CheckType | String | code scan _ | 检查项类型。 取值： hc.check.type.identity auth：身份鉴别。 _ hc.check.type.access control：访问控 _ 制。 hc.check.type.network service：网络及 _ 服务。 hc.check.type.service conf：服务配置。 _ hc.check.type.file rights：文件权限。 _ hc.check.type.security audit：安全审 _ 计。 hc.check.type.attack defense：入侵防 _ 范。 hc.check.type.others：其他。 |
| - CheckTypeDis Name | String | Data Integrity | 检查项类型展示名称。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| PageInfo | Struct | - | 分页查询时的页面信息。 |
| -CurrentPage | Integer | 1 | 当前页的页码。 |
| -PageSize | Integer | 10 | 分页查询时，每页最多显示的数据条数。 |
| -TotalCount | Integer | 10 | 数据总条数。 |
| -Count | Integer | 1 | 分页查询时，当前页显示的数据条数。 |

**示例**

`JSON` 格式

```json
{
 "PageInfo":{
  "TotalCount":10,
  "PageSize":10,
  "CurrentPage":1,
  "Count":1
 },
 "RequestId":"",
 "List":[
  {
   "Target":"foo2,foo3",
   "CheckId":696,
   "CheckItem":"CHECK_CONN_SRC",
   "CheckTypeDisName":"Data Integrity",
   "CheckType":"code_scan",
   "TargetType":"RD-Account",
   "Lang":"zh",
   "RecordId":20201105144514,
   "Reason":"Started",
   "Source":"Local"
  }
```

]

```
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | ServerError | ServerError | ServerError |
| 403 | NoPermission | NoPermission | caller has no permission |

### 异常登录检测相关接口

#### DescribeBaseConfigs

获取异地登录相关的配置信息，包括常用登录地址，常用登录IP，常用登录时间，用户登录账号。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBaseCo nfigs | 取值：DescribeBaseConfigs。 |

| Type | String | 是 | login common l _ _ ocation | 常用登录配置类型。 login common location：常用登 _ _ 录地点。 login common ip：常用登录IP。 _ _ login common time：常用登录时 _ _ 间。 login common account：常用登 _ _ 录账号。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 192.168.x.x | 访问者源IP。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| Target | String | 否 | [{"targetType":" uuid","target":"6 dbdbfe7-06fa- 4d9a-8268- xxxx"}] | 已废弃。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BaseConfigs | Array of StringItem |  | 关联的配置信息。 |
| Account | String | dem****** | 常用登录账号。 |
| EndTime | String | 14:08 | 常用登录时间的结束时间。使用HH:mm格式。 |
| Ip | String | 42.2.2.1 | 常用登录IP。 |
| Location | String | 杭州市 | 常用登录地点。 |
| StartTime | String | 14:08 | 常用登录时间的开始时间。使用HH:mm格式。 |
| TargetList | Array of Target |  | 目标配置信息。 |
| Target | String | a63ed848-f002- 4d63-995e-*** | 服务器分组ID或者服务器UUID的实际内容。 |

| TargetType | String | uuid | groupId或者uuid。 groupId：Target的内容是分组ID实际值。 uuid：Target的内容是UUID实际值。 |
|---|---|---|---|
| TotalCount | Integer | 10 | 总服务器台数。 |
| UuidCount | Integer | 3 | 关联的服务器的台数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| RequestId | String | 485ABE58-4E27- 4416-***- F8F3B8748EB6 | 本次调用请求的ID。 |
| TotalCount | Integer | 32 | 总数据条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeBaseConfigs &Type=login_common_location
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>32</TotalCount> <PageSize>20</PageSize> <RequestId>485ABE58-4E27-4416-***-F8F3B8748EB6</RequestId> <CurrentPage>1</CurrentPage> <BaseConfigs>
    <Account>dem******</Account>
    <TotalCount>10</TotalCount>
    <EndTime>14:08</EndTime>
    <Ip>42.2.2.1</Ip>
    <StartTime>14:08</StartTime>
    <UuidCount>3</UuidCount>
    <Location>杭州市</Location>
    <TargetList>
        <Target>a63ed848-f002-4d63-995e-***</Target>
        <TargetType>uuid</TargetType>
    </TargetList>
</BaseConfigs>
```

`JSON` 格式

```json
{
    "TotalCount": 32,
    "PageSize": 20,
    "RequestId": "485ABE58-4E27-4416-***-F8F3B8748EB6",
    "CurrentPage": 1,
    "BaseConfigs": {
        "Account": "dem******",
        "TotalCount": 10,
        "EndTime": "14:08",
        "Ip": "42.2.2.1",
        "StartTime": "14:08",
        "UuidCount": 3,
```

`"Location": "`杭州市`",`

```json
        "TargetList": {
            "Target": "a63ed848-f002-4d63-995e-***",
            "TargetType": "uuid"
        }
    }
}
```

#### DescribeSwitchConfigs

获取异常登录日志分析开关。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSwitchC onfigs | 取值：DescribeSwitchConfigs。 |
| SourceIp | String | 否 | 192.168.x.x | 访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConfigList | Array of Config |  | 配置项的开关信息。 |
| Item | String | login common loc _ _ ation | 配置项名称。 login common location：常用登录地 _ _ 点。 login common ip：常用登录IP。 _ _ login common time：常用登录时间。 _ _ login common account：常用登录账 _ _ 号。 |

| Status | Integer | 1 | 配置状态。 1:开。 0:关。 |
|---|---|---|---|
| Count | Integer | 3 | 数据的总条数。 |
| RequestId | String | 485ABE58-4E27- 4416-997C- F8F3B8748EB6 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSwitchConfigs
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>485ABE58-4E27-4416-997C-F8F3B8748EB6</RequestId> <Count>3</Count> <ConfigList>
    <Status>1</Status>
    <Item>login_common_location</Item>
</ConfigList>
```

`JSON` 格式

```json
{
    "RequestId": "485ABE58-4E27-4416-997C-F8F3B8748EB6",
    "Count": 3,
    "ConfigList": {
        "Status": 1,
        "Item": "login_common_location"
    }
}
```

#### DescribeConfigTarget

获取特定配置，如常用IP地址，常用登录时间，常用登录IP，常用登录账号，对应关联的分组或者服务器。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeConfigT arget | 取值：DescribeConfigTarget。 |

| Config | String | 是 | {"location":"赣州市"} | 特定的配置。字段说明： location：常用登录地址。 ip：常用登录IP。 startTime：常用登录开始时间。 endTime：常用登录结束时间。 account：常用登录账号。 示例： 常用登录地址：{"location":"赣州市"}。 常用登录IP： {"ip":"120.44.55.66"}。 常用登录时间： {"startTime":"16:18","endTime":"1 7:18"}。 常用登录账号： {"account":"dbaadmin"}。 |
|---|---|---|---|---|
| Type | String | 是 | login common l _ _ ocation | 类型说明。 login common location：常用登 _ _ 录地点。 login common ip：常用登录IP。 _ _ login common time：常用登录时 _ _ 间。 login common account：常用登 _ _ 录账号。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问者源IP。 |
| Target | String | 否 | [{"targetType":" uuid","target":"6 dbdbfe7-***-- 8268- ce2dc6d673ac"} ] | 获取单台机器的配置的时候需要。字段说明： targetType：配置的类型。取值uuid或groupId。 target：1、当 targetType=uuid，target的内容为 UUID的实际值。2、当 targetType=groupId，target的内容为分组ID的实际值。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 32 | 数据的总条数。 |
| RequestId | String | 485ABE58-4E27- 4416-997C- F8F3B8748EB6 | 本次调用请求的ID。 |
| TargetList | Array of Targe |  | 目标列表。 |

| Target | String | a63ed848-f002- 4d63-995e-xxx | 分组ID或者服务器UUID。 |
|---|---|---|---|
| TargetType | String | uuid | groupId或者uuid。 groupId：Target的实际内容是分组ID实际值。 uuid：Target的实际内容是UUID实际值。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeConfigTarget &Config={"location":"赣州市"} &Type=login_common_location
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TargetList>
    <Target>a63ed848-f002-4d63-995e-xxx</Target>
    <TargetType>uuid</TargetType>
</TargetList> <RequestId>485ABE58-4E27-4416-997C-F8F3B8748EB6</RequestId> <Count>32</Count>
```

`JSON` 格式

```json
{
    "TargetList": {
        "Target": "a63ed848-f002-4d63-995e-xxx",
        "TargetType": "uuid"
    },
    "RequestId": "485ABE58-4E27-4416-997C-F8F3B8748EB6",
    "Count": 32
}
```

#### ModifyBaseConfig

**描述**

修改登录安全设置记录。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：ModifyBaseConfig |

| Type | String |  | 是 | 常用登录配置记录类型，取值范围： login common location：表示常用登 _ _ 录地 login common ip：表示常用登录IP _ _ login common time：表示常用登录时 _ _ 间 login common account：表示常用登 _ _ 录账号 |  |  |
|---|---|---|---|---|---|---|
| Target | String |  | 否 | 指定主机资产。 说明获取指定资产的登录安全配置记录时需要指定该参数，具体格式参考请求示例。 |  |  |
| Config | String |  | 否 | 登录配置记录，例如： 常用登录地址： {"location":"赣州市"} 常用登录IP： {"ip":"x.x.x.x"} 常用登录时间： {"startTime":"16:18","endTi me":"16:18"} 常用登录账号： {"account":"dbaadmin"} |  |  |
|  |  |  |  |  | {"startTime":"16:18","endTi |  |
|  |  |  |  | me":"16:18"} |  |  |

| {"location":"赣州 |  |
|---|---|

|  | 市"} |
|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=ModifyBaseConfig &Config={"startTime":"16:18","endTime":"16:18"} &Target=[{"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917a7e6cbbb4b2e","flag":"add"},{"targetType":"uuid","target":"1759b0ea-6dd7-438b-b60d-c9 0179bd9ebc","flag":"del"}] &Type=login_common_location
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"BB8F5902-BD50-49AB-B124-18E9CA92BB99"
}
```

#### DeleteBaseConfig

**描述**

从登录安全设置中删除指定常用登录地或常用登录IP等记录。

**请求参数**

| 名称 | 类型 |  | 是否必须 | 描述 |  |
|---|---|---|---|---|---|
| Action | String |  | 是 | 接口名，系统规定参数。 取值：DeleteBaseConfig |  |
| Config | String |  | 是 | 常用登录地配置信息，参数和举例如下： 常用登录地址： {"location":"赣州市"} 常用登录IP： {"ip":" x.x.x.x"} 常用登录时间： {"startTime":"16:18","endTi me":"16:18"} 常用登录账号： {"account":"dbaa****"} |  |
|  |  |  |  |  | {"startTime":"16:18","endTi |
|  |  |  |  | me":"16:18"} |  |
| Type | String |  | 是 | 常用登录配置记录类型，取值范围： login common location：表示常用登 _ _ 录地 login common ip：表示常用登录IP _ _ login common time：表示常用登录时 _ _ 间 login common account：表示常用登 _ _ 录账号 |  |
| Target | String |  | 否 | 指定主机资产。 说明删除指定资产的登录安全配置记录时需要指定该参数，具体格式参考请求示例。 |  |

| {"location":"赣州 |  |
|---|---|

|  | 市"} |
|---|---|

| 是 |  |
|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=DeleteBaseConfig &Config={"location":"赣州市"} &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
    "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
}
```

#### ModifySwitchConfig

**描述**

修改登录安全设置中合法登录开关配置。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：ModifySwitchConfig |
| Item | String | 是 | 常用登录配置项： login common location：表示常用登 _ _ 录地 login common ip：表示常用登录IP _ _ login common time：表示常用登录时 _ _ 间 login common account：表示常用登 _ _ 录账号 |
| Status | Integer | 是 | 配置开关状态： 1：表示开启 0：表示关闭 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |
| Count | Integer | 返回总记录数。 |
| ConfigList | Array | 登录安全设置开关状态，具体子项说明见以下参数描述。 |

| Item | String | 常用登录配置项： login common location：表示常用登录地 _ _ login common ip：表示常用登录IP _ _ login common time：表示常用登录时间 _ _ login common account：表示常用登录账号 _ _ |
|---|---|---|
| Status | Integer | 配置开关状态： 1：表示开启 0：表示关闭 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=ModifySwitchConfig &Item=login_common_location &Status=1
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4"
}
```

### 网站后门检测相关接口

#### DescribeCategoryCount

查询用户的Webshell数量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCategor yCount | 取值：DescribeCategoryCount。 |
| SourceIp | String | 否 | 47.100.XX.XX | 接口访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0112DE-E4FA- ****-974F- 2DDB450934C2 | 本次调用请求的ID。 |

| Webshell | Integer | 1 | Webshell的数量。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCategoryCount
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>FD0112DE-E4FA-****-974F-2DDB450934C2 </RequestId> <Webshell>1</Webshell>
```

`JSON` 格式

```json
{
    "RequestId": "FD0112DE-E4FA-****-974F-2DDB450934C2",
    "Webshell": 1
}
```

#### DescribeWebshell

获取安骑士检测到的网站后门（Webshell）文件记录。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeWebshe ll | 取值：DescribeWebshell。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源IP。 |
| GroupId | Integer | 否 | 1 | 资产分组ID。 |
| Remark | String | 否 | 测试机器1 | 模糊搜索条件：资产名称。 |
| Tag | Integer | 否 | 1 | 资产标签。 |
| Dealed | String | 否 | N | 处理状态。取值： Y：表示已处理。 N：表示未处理。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B41B3780-337A- 472D-B82E- 9FD3642B9350 | 本次调用请求的ID。 |
| WebshellList | Array of Webshell |  | Webshell列表。 |
| Domain | String | http://example.co m/ | 域名。 |
| FirstFoundTim e | String | 2021-01-01 00:00:00 | 首次发现时间。格式：yyyy-MM-dd HH:mm:ss。 |
| FoundTime | String | 2021-01-01 00:00:00 | 发现时间。格式：yyyy-MM-dd HH:mm:ss。 |
| GroupId | Long | 1 | 分组ID。 |
| InstanceId | String | i-dasjdhaks**** | 资产实例ID |
| InstanceName | String | test*** | 实例名。 |
| Ip | String | 47.100.XX.XX | 资产的IP。 |
| Os | String | linux | 操作系统。 |
| Region | String | cn-hang*** | 地域ID。 |
| Status | Integer | 0 | 标识Webshell的状态。 0：所有的Webshell。 1：未处理的Webshell。 2：已删除的Webshell。 4：隔离失败。 3：信任文件。 5：隔离时发现文件不存在。 6：恢复时失败。 7：隔离中。 8：恢复中。 9：失效。 |
| TrojanPath | String | /xx/xx/xx/xx.jsp | 路径。 |
| TrojanSize | Long | 1 | 已废弃。 |

| TrojanType | String | Webshell | 异常文件类型。 |
|---|---|---|---|
| Uuid | String | 228c63db-ac3b- 45f1-840f-xxx | 资产UUID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <WebshellList>
    <Status>0</Status>
    <FoundTime>2021-01-01 00:00:00</FoundTime>
    <TrojanSize>1</TrojanSize>
    <Os>linux</Os>
    <TrojanType>Webshell</TrojanType>
    <InstanceId>i-dasjdhaks****</InstanceId>
    <Ip>47.100.XX.XX</Ip>
    <TrojanPath>/xx/xx/xx/xx.jsp</TrojanPath>
    <FirstFoundTime>2021-01-01 00:00:00</FirstFoundTime>
    <GroupId>1</GroupId>
    <InstanceName>test***</InstanceName>
    <Uuid>228c63db-ac3b-45f1-840f-xxx</Uuid>
    <Region>cn-hang***</Region>
    <Domain>xxx</Domain>
</WebshellList>
```

`JSON` 格式

```json
{
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "WebshellList": {
        "Status": 0,
        "FoundTime": "2021-01-01 00:00:00",
        "TrojanSize": 1,
        "Os": "linux",
        "TrojanType": "Webshell",
        "InstanceId": "i-dasjdhaks****",
        "Ip": "47.100.XX.XX",
        "TrojanPath": "/xx/xx/xx/xx.jsp",
        "FirstFoundTime": "2021-01-01 00:00:00",
        "GroupId": 1,
        "InstanceName": "test***",
        "Uuid": "228c63db-ac3b-45f1-840f-xxx",
        "Region": "cn-hang***",
        "Domain": "xxx"
    }
}
```

#### DescribeQuaraFile

查询隔离文件列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeQuaraFi le | 取值：DescribeQuaraFile。 |
| SourceIp | String | 否 | 47.100.XX.XX | 接口访问者源IP。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| QuaraFiles | Array of QuaraFile |  | 隔离文件列表。 |

| EventName | String | DDOS木马 | 事件名称。 |
|---|---|---|---|
| EventType | String | 恶意进程（云查杀） | 事件分类。 |
| FileStatus | String | quaraDone | 隔离文件状态。取值： 0：隔离失败。 1：回滚失败。 2：隔离成功。 3：回滚成功。 4：隔离中。 5：回滚中。 |
| Md5 | String | 008241a52014ee2 b14cf8bc3db90**** | 文件MD5。 |
| Online | Boolean | false | 机器客户端在线状态。取值： true：是。 false：否。 |
| Path | String | /root/008241a5201 4ee2b14cf8bc3db9 0*** | 隔离文件路径。 |
| Tag | String | a50f96f958fbd59f6 8e4bca4d90*** | 异常事件唯一标识。 |
| Uuid | String | 00f11fcb-1a9a- 4fd5-a48a- e0e5bd*** | 机器唯一标识。 |
| RequestId | String | FD0112DE-E4FA- 48E5-***- 2DDB450*** | 本次调用请求的ID。 |
| TotalCount | Integer | 10 | 总数据条数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>10</TotalCount> <PageSize>20</PageSize> <RequestId>FD0112DE-E4FA-48E5-***-2DDB450*** </RequestId> <CurrentPage>1</CurrentPage> <QuaraFiles>
    <Path>/root/008241a52014ee2b14cf8bc3db90***</Path>
    <FileStatus>quaraDone</FileStatus>
    <Uuid>00f11fcb-1a9a-4fd5-a48a-e0e5bd***</Uuid>
```

`<EventType>`恶意进程（云查杀）`</EventType>`

```xml
    <Tag>a50f96f958fbd59f68e4bca4d90***</Tag>
    <EventName>DDOS木马</EventName>
    <Online>false</Online>
    <Md5>008241a52014ee2b14cf8bc3db90****</Md5>
</QuaraFiles>
```

`JSON` 格式

```json
{
    "TotalCount": 10,
    "PageSize": 20,
    "RequestId": "FD0112DE-E4FA-48E5-***-2DDB450***",
    "CurrentPage": 1,
    "QuaraFiles": {
        "Path": "/root/008241a52014ee2b14cf8bc3db90***",
        "FileStatus": "quaraDone",
        "Uuid": "00f11fcb-1a9a-4fd5-a48a-e0e5bd***",
```

`"EventType": "`恶意进程（云查杀）`",`

```json
        "Tag": "a50f96f958fbd59f68e4bca4d90***",
        "EventName": "DDOS木马",
        "Online": false,
        "Md5": "008241a52014ee2b14cf8bc3db90****"
    }
}
```

#### RollbackQuaraFile

**描述**

恢复指定已隔离文件。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：RollbackQuaraFile |
| EventName | String | 否 | 异常事件名称。 |
| EventType | String | 否 | 异常事件类型。 |

| Tag | String | 否 | 异常事件唯一标识ID。 |
|---|---|---|---|
| Uuid | String | 否 | 主机资产UUID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=RollbackQuaraFile &EventName=DDOS木马
```

`&EventType=`恶意进程（云查杀）

```
&Tag=a50f96f958fbd59f68e4bca4d90679d6 &Uuid=00f11fcb-1a9a-4fd5-a48a-e0e5bd12a6a4
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
}
```

#### DescribeWebPath

**描述**

获取网站后门设置中的Web目录定义信息。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：DescribeWebPath |
| PageSize | Integer | 否 | 指定返回结果中每页最大显示记录数。 默认值：20 |
| CurrentPage | Integer | 否 | 指定当前返回页数。 默认值：1 |

| Type | String | 否 | 配置类型，系统规定参数。 取值：web path，表示Web目录定义配 _ 置。 |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |
| TotalCount | Integer | 总返回记录数。 |
| CurrentPage | Integer | 当前返回页码。 |
| PageSize | Integer | 页面显示最大记录数量。 |
| Count | Integer | Web目录配置记录数量。 |
| ConfigList | Array | Web目录列表，具体子项说明见以下参数描述。 |
| WebPath | String | Web目录路径。 |
| TargetList | Array | 应用该Web目录路径的目标主机列表，具体子项说明见以下参数描述。 |
| TargetType | String | 固定返回值为uuid，表示Target参数的值是主机资产 UUID。 |
| Target | String | 主机资产UUID。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=DescribeWebPath
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "TotalCount":1,
 "PageSize":5,
 "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534",
 "CurrentPage":1,
 "Count":1,
 "ConfigList":[
  {
   "TargetList":[
    {
     "Target":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
     "TargetType":"uuid"
    }
```

`],`

```json
   "WebPath":"/usr/local/tomcat/webroot18"
  }
```

]

```
}
```

#### ModifyWebPath

**描述**

修改网站后门设置中的Web目录。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：ModifyWebPath |
| Type | String | 否 | 配置类型，系统规定参数。 取值：web path，表示Web目录定义配 _ 置。 |
| Config | String | 否 | Web目录定义配置信息，以JSON格式描述， 具体参见请求示例。 |
| Target | String | 否 | 该Web目录定义配置的目标主机列表，以 JSON格式描述，具体参见请求示例。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=ModifyWebPath &Type=web_path &Config={"webPath":"/test"} &Target={"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917a7e6cbbb4b2e","flag":"add"}
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534"
}
```

#### OperateTrojan

**描述**

处理检测到的网站后门（webshell）文件。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：OperateTrojan |
| Info | String | 否 | Webshell事件信息，以JSON格式描述，具体参见请求示例。 |
| OperateType | String | 否 | 处理操作类型，取值范围： isolate：表示隔离文件 trust：表示信任该文件 untrust：表示取消信任文件 restore：表示恢复文件 |
| Type | Integer | 否 | 木马类型，系统规定参数。 取值：1 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |
| FailedCount | Integer | 操作失败记录数。 |
| SuccessCount | Integer | 操作成功记录数。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=OperateTrojan &Info=[{"uuid":"97988c2b-de9d-4159-90ab- 7cc73561c64c","filePath":"/home/test/Z02.php","webshellId":""}] &OperateType=trust &Type=1
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "FailedCount": 0,
    "SuccessCount": 1
}
```

### 主机异常检测相关接口

#### DescribeSuspEventTypes

查询异常事件分类信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSuspEv entTypes | 取值：DescribeSuspEventTypes。 |
| SourceIp | String | 否 | 192.168.x.x | 接口访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| EventTypes | Array of Data |  | 事件类型列表。 |
| AliseEventTyp e | String | 进程异常行为 | 异常类型名称。 |
| EventType | String | 进程异常行为 | 异常类型标识。 |
| RequestId | String | FD0112DE-E4FA- 48E5-974F- 2DDB450934C2 | 本次调用请求的ID。 |
| TotalCount | Integer | 10 | 总数据条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSuspEventTypes
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>10</TotalCount> <RequestId> FD0112DE-E4FA-48E5-974F-2DDB450934C2</RequestId> <EventTypes>
```

`<EventType>`进程异常行为`</EventType>` `<AliseEventType>`进程异常行为`</AliseEventType>`

```
</EventTypes>
```

`JSON` 格式

```json
{
    "TotalCount": 10,
    "RequestId": "FD0112DE-E4FA-48E5-974F-2DDB450934C2",
    "EventTypes": {
```

`"EventType": "`进程异常行为`",` `"AliseEventType": "`进程异常行为"

```
    }
}
```

#### DescribeSuspTrendStatistics

获取异常事件每天每种类型发现数据量的统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSuspTre ndStatistics | 取值：DescribeSuspTrendStatistics 。 |
| SourceIp | String | 否 | 192.168.x.x | 接口访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Interval | Integer | 86400000 | 周期。格式：时间戳。单位：毫秒数。 |

| RequestId | String | B41B3780-337A- 472D-B82E- 9FD3642B9350 | 本次调用请求的ID。 |
|---|---|---|---|
| StartTime | Integer | 1 | 已废弃。 |
| SuspiciousIte ms | List | [1,0,4,3] | 每天事件统计数。例如返回内容为 [1,0,4,3]， 表示第一天统计数据为1，第二天统计数据为0， 依次类推，默认返回近7天内数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSuspTrendStatistics
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <StartTime>1</StartTime> <SuspiciousItems>[1,0,4,3]</SuspiciousItems> <Interval>86400000</Interval>
```

`JSON` 格式

```json
{
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "StartTime": 1,
    "SuspiciousItems": "[1,0,4,3]",
    "Interval": 86400000
}
```

#### DescribeSuspiciousExportInfo

查询异常事件导出信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSuspici ousExportInfo | 取值：DescribeSuspiciousExportInf o。 |
| SourceIp | String | 否 | 192.168.XX.XX | 接口访问者源IP。 |

| ExportId | Integer | 否 | 10 | 导出记录ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CurrentCount | Integer | 10 | 当前数据条数。 |
| ExportStatus | String | init | 导出状态。 init：初始化。 pending：等待执行。 exporting ：导出中。 success ：导出成功。 fail：导出失败。 |
| FileName | String | suspicious 201xxx _ | 导出文件名称。 |
| GmtCreate | Long | 1234567890123 | 创建时间。使用时间戳格式，单位：毫秒。 |
| Id | Integer | 1 | 导出记录ID。 |
| Link | String | http://suspicious- export.oss-cn- ***.aliyuncs.com/e xport/demo.zip? Expires=15180751 76&OSSAccessKeyI d=***&Signature= ***%3D | 下载链接。 |
| Message | String | 处理中 | 处理信息。 |
| Progress | Integer | 80 | 导出进度。单位百分比。 |
| RequestId | String | FD0112DE-E4FA- 48E5-***- 2DDB450934C2 | 本次调用请求的ID。 |
| TotalCount | Integer | 28 | 总数据条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSuspiciousExportInfo
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Progress>80</Progress> <TotalCount>28</TotalCount> <GmtCreate>1234567890123</GmtCreate> <Message>处理中</Message> <RequestId>FD0112DE-E4FA-48E5-***-2DDB450934C2 </RequestId> <FileName>suspicious_201xxx</FileName> <ExportStatus>init</ExportStatus> <CurrentCount>10</CurrentCount> <Id>1</Id> <Link>http://suspicious-export.oss-cn-***.aliyuncs.com/export/demo.zip? Expires=1518075176&amp;OSSAccessKeyId=***&amp;Signature=***%3D</Link>
```

`JSON` 格式

```json
{
    "Progress": 80,
    "TotalCount": 28,
    "GmtCreate": 1234567890123,
```

`"Message": "`处理中`",`

```json
    "RequestId": "FD0112DE-E4FA-48E5-***-2DDB450934C2",
    "FileName": "suspicious_201xxx",
    "ExportStatus": "init",
    "CurrentCount": 10,
    "Id": 1,
    "Link": "http://suspicious-export.oss-cn-***.aliyuncs.com/export/demo.zip?
Expires=1518075176&amp;OSSAccessKeyId=***&amp;Signature=***%3D" }
```

#### OperateSuspiciousEvent

**描述**

处理检测到的异常事件。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：OperateSuspiciousEvent |
| Data | String | 否 | 需要操作的异常事件记录，以JSON格式描述，具体参见请求示例。 |

| OperateType | String | 否 | 处理操作类型，取值范围： deal：表示修复 confirm：表示标记为已处理 mark misinformation：表示标记为误 _ 报 unmark misinformation：表示取消标 _ 记为误报 ignore：表示忽略 |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

**错误码**

**示例**

请求示例

```json
https://aegis.[RegionId].example.com/?Action=OperateSuspiciousEvent &OperateType=ignore &Data={"uuid":"97988c2b-de9d-4159-90ab- 7cc73561c64c","tag":"f87eb0ee5934f6f65343ec601ce71c2f","eventType":"恶意进程（云查杀）", "eventName":"DDOS木马"},{"uuid":"97988c2b-de9d-4159-90ab- 7cc73561c64c","tag":"95347a77b8c0d6dae99a23ab69aa90f4","eventType":"恶意进程（云查杀）", "eventName":"GateDDoS木马"}
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B"
}
```

#### OperateLoginLog

**描述**

修改异常登录事件的状态标记，即将检测到的异常登录事件标记为已处理。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：OperateLoginLog |
| Ids | String | 是 | 异常登录日志ID，指定多个日志ID以“,”隔开。 |

| OperateType | String | 是 | 处理操作类型。 取值：confirm，标记为已处理。 |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=OperateLoginLog &Ids=2006434 &OperateType=confirm
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905"
}
```

#### DescribeVirusInfo

**描述**

通过上传文件MD5值，利用云查杀功能判断该文件是否为恶意程序。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：DescribeVirusInfo |
| Md5 | String | 是 | 文件的MD5值。 |
| Lang | String | 否 | 文件的语言属性，例如zh。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

| Data | Boolean | 判断结果： True：表示该文件是恶意文件 False：表示该文件不是恶意文件 |
|---|---|---|

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].aliyuncs.com/?Action= DescribeVirusInfo &Md5=6f6628d923f9018b28acc5f905e03244
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId": "A2423F39-3272-4491-804E-D0EBDE3E894D",
 "Data": true
}
```

#### CreateSuspiciousExport

**描述**

根据查询条件导出主机异常事件信息。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：CreateSuspiciousExport |
| Dealed | String | 否 | 异常事件是否已处理，取值范围： Y：表示已处理 N：表示未处理 |
| EventNameRema rk | String | 否 | 异常事件名称，支持模糊查询匹配。 |
| EventType | String | 否 | 异常事件分类名称，取值范围： 异常登录进程异常行为异常账号敏感文件篡改异常网络连接异常事件可疑文件恶意进程（云查杀） |

| GroupId | String | 否 | 资产分组ID。 |
|---|---|---|---|
| Level | String | 否 | 事件等级，取值范围： serious：表示严重 high：表示高危 medium：表示中危 low：表示低危支持指定多个事件等级，以“,”隔开。 |
| Remark | String | 否 | 主机名称或主机IP，支持模糊查询匹配。 |
| StatusList | String | 否 | 异常事件处理状态，取值范围： 1：表示待处理 2：表示已忽略 3：表示已确认 8：表示已标记为误报 16：表示处理中 32：表示处理完毕支持指定多个状态，以“,”隔开。 |
| Tag | String | 否 | 主机标签。 |
| Uuids | String | 否 | 主机资产UUID，指定多个主机资产UUID 以“,”隔开。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |
| FileName | String | 导出文件名称。 |
| Id | Long | 导出任务记录ID。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=CreateSuspiciousExport &Remark=23
```

`&EventType=`进程异常行为

```
&Level=serious,high,medium,low &Dealed=n
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "FileName": "suspicious_20180408",
    "Id": 387
}
```

#### CreateFileProtectRule

用户登录接口

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| Lang | Strin g | Query | 否 | en | 设置请求和接收消息的语言类型，默认为zh。 zh：中文。 en：英文。 |
| Id | Long | Query | 否 | 245 | 基线策略ID。 |
| RuleName | Strin g | Query | 是 | 规则**** | 系统规则名称。 |
| ProcPaths | Repe atList | Query | 是 | D:\Games\Launcher.exe | 对进程监听的路径列表，支持通配。 |
| FilePaths | Repe atList | Query | 是 | /static/test.png | 监控的文件路径列表，支持通配。 |
| FileOps | Repe atList | Query | 是 | EXISTS | 对文件进行的操作列表。 |
| RuleActio n | Strin g | Query | 是 | 1 | 规则动作:close,alert,drop。 |

|  |  |  |  |  |  | 安骑士开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AlertLevel | Integ er | Query | 否 | 0 | 报警通知级别。取值如下： 0: 不告警 1: 提醒 2: 可疑 3: 高危 |
| SwitchId | Strin g | Query | 否 | vs-abcdef**** | 规则对应的开关ID。 |
| Status | Integ er | Query | 否 | 1 | 设置需要查询的隔离文件的状态。取值： quaraFailed：隔离失败 quaraDone：隔离成功 quaraing：隔离中 rollbackFailed：撤销隔离失败 rollbackDone：撤销隔离成功 rollbacking：撤销隔离中。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| RuleId | Long | 123 | 规则ID |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateFileProtectRule &RuleName=规则**** &ProcPaths=D:\Games\Launcher.exe &FilePaths=/static/test.png &FileOps=EXISTS &RuleAction=1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "RuleId":123
}
```

#### UpdateFileProtectRule

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- aegis:UpdateFileProtectRule | Write | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| Lang | Strin g | Query | 否 | zh | 设置请求和接收消息的语言类型，默认为zh。 zh：中文。 en：英文。 |
| Id | Long | Query | 否 | 1062 | 规则 ID。 |
| RuleName | Strin g | Query | 是 | test-rule-1 | 规则名称。 |
| ProcPaths | Repe atList | Query | 是 | ["/usr/local/*","/tmp/*"] | 对进程监听的路径列表。 |
| FilePaths | Repe atList | Query | 是 | ["/usr/local/*","/tmp/*"] | 监控的文件路径列表，支持通配。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileOps | Repe atList | Query | 是 | ["WRITE"] | 对文件进行的操作列表。 取值： READ：读操作 WRITE：写操作 EXECUTE：执行操作 RENAME： 重命名 CHMOD： 修改权限 |
| RuleActio n | Strin g | Query | 否 | pass | 规则在客户端的表现形式。 取值如下： pass： 放过 alert： 告警 |
| SwitchId | Strin g | Query | 否 | 无 | 已废弃。 |
| AlertLevel | Integ er | Query | 否 | 0 | 报警通知级别。 取值如下： 0: 不告警 1: 提醒 2: 可疑 3: 高危 |
| Status | Integ er | Query | 否 | 0 | 设置规则状态。 0：未启用 1：已启用 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=UpdateFileProtectRule&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&Lang=zh&Id=1062&RuleName=test-rule- 1&ProcPaths.1=/usr/local/*&FilePaths.1=/usr/local/*&FileOps.1=WRITE&RuleAction=pass&Switc d=RISK-COMMAND-AUDIT-RULE-SWITCH-TYPE_200****&AlertLevel=0&Status=
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
```

#### ListFileProtectEventExport

调用ListFileProtectEventExport接口查询核心文件监控告警事件。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- aegis:ListFileProtectEventExpor t | Read | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 219.133.XX.XX | 访问源IP地址。 默认值： 196.0.0.0 |
| Lang | Strin g | Query | 否 | zh | 设置请求和接收消息的语言类型，默认为zh。 zh：中文。 en：英文。 默认值：zh |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| EventDTOList | Array | [ { "LatestTimeStr":"1 694576692000", "Status":"0,1,2", "FilePath":"/etc/pa m.d/su", "FirstTime":169457 6692000, "ResourceSetName ":"test", "GmtModified":"16 7118088****", "CmdLine":" [\"touch\",\"/test/aa aa\"]", "OrgName":"test", "Operation":"READ ", "IntranetIp":"192.1 68.176.75", "Remark":"test", "InstanceName":"c a cpm ****", _ _ "OrgId":"12", "ProcPermission":"r wxr-xr-x", "Uuid":"c9107c04- 942f-40c1-981a- f1c1***", "InternetIp":"43.11 6.5.5", "LatestTime":1694 576692000, "FirstTimeStr":"169 4576692000", "AlertLevel":1, "ProcessId":"52636 ", "ProcPath":" /usr/bin/sshpass", "ResourceSetId":"1 2", "HandleTime":1694 576692000, "RuleName":"test- rule-1" } ] | 告警列表生成 |
| -AlertLevel | Integer | 1 | 报警通知级别。取值如下： 0：不告警 1： 提醒 2： 可疑 3： 高危 |
| -Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | 实例的UUID。 |
| -RuleName | String | test-rule-1 | 规则名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -FirstTime | Long | 1694576692000 | 事件第一次发生时间。 |
| -FirstTimeStr | String | 1694576692000 | 事件第一次发生时间。 |
| -LatestTime | Long | 1694576692000 | 事件最近一次发生时间。 |
| -LatestTimeStr | String | 1694576692000 | 事件最近一次发生时间。 |
| -Status | Integer | 0,1,2 | 事件状态。取值如下： 0： 未处理 1： 我已手工处理 2： 已加白 3： 已忽略 |
| -ProcPath | String | /usr/bin/sshpass | 进程路径。 |
| -FilePath | String | /etc/pam.d/su | 进程操作的文件路径。 |
| -CmdLine | String | ["touch","/test/aaa a"] | 事件命令行。 |
| - ProcPermissio n | String | rwxr-xr-x | 进程权限。 |
| -Operation | String | READ | 操作类型。取值如下： 对文件的操作类型。取值： DELETE： 对文件删除操作。 WRITE：对文件写操作。 READ：对文件读操作。 RENAME：对文件重命名操作。 CHOWN：设置文件所有者和文件关联组操作。 |
| - InstanceName | String | ca cpm **** _ _ | 指定要查询的服务器名称。 |
| -IntranetIp | String | 192.168.176.75 | 内网ip |
| -InternetIp | String | 43.116.5.5 | 外网ip |
| -GmtModified | Long | 167118088**** | 最新一次修改时间。 |

|  |  |  | 安骑士开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Remark | String | test | 备注。 |
| -HandleTime | Long | 1694576692000 | 事件处理时间。 |
| -ProcessId | String | 52636 | 事件进程 ID。 |
| -OrgId | String | 12 | 组织id。 |
| - ResourceSetId | String | 12 | 资源集id。 |
| -OrgName | String | test | 组织名称。 |
| - ResourceSetN ame | String | test | 资源集名称。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| PageInfo | Struct | { "TotalCount":2, "PageSize":20, "CurrentPage":1, "Count":2 } | 分页信息。 |
| -Count | Integer | 2 | 分页查询时，当前页显示的数据条数。 |
| -PageSize | Integer | 20 | 分页查询时，每页最多显示的数据条数。 |
| -TotalCount | Integer | 2 | 暴露在互联网的服务器数据的总条数。 |
| -CurrentPage | Integer | 1 | 分页查询时，当前页的页码。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=ListFileProtectEventExport&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&Lang=zh
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "EventDTOList":[
        {
            "LatestTimeStr":"1694576692000",
            "Status":"0,1,2",
            "FilePath":"/etc/pam.d/su",
            "FirstTime":1694576692000,
            "ResourceSetName":"test",
            "GmtModified":"167118088****",
            "CmdLine":"[\"touch\",\"/test/aaaa\"]",
            "OrgName":"test",
            "Operation":"READ",
            "IntranetIp":"192.168.176.75",
            "Remark":"test",
            "InstanceName":"ca_cpm_****",
            "OrgId":"12",
            "ProcPermission":"rwxr-xr-x",
            "Uuid":"c9107c04-942f-40c1-981a-f1c1***",
            "InternetIp":"43.116.5.5",
            "LatestTime":1694576692000,
            "FirstTimeStr":"1694576692000",
            "AlertLevel":1,
            "ProcessId":"52636",
            "ProcPath":" /usr/bin/sshpass",
            "ResourceSetId":"12",
            "HandleTime":1694576692000,
            "RuleName":"test-rule-1"
        }
```

`],`

```json
    "PageInfo":{
        "TotalCount":2,
        "PageSize":20,
        "CurrentPage":1,
        "Count":2
    }
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <EventDTOList>
        <AlertLevel>1</AlertLevel>
        <Uuid>c9107c04-942f-40c1-981a-f1c1***</Uuid>
        <RuleName>test-rule-1</RuleName>
        <FirstTime>1694576692000</FirstTime>
        <FirstTimeStr>1694576692000</FirstTimeStr>
        <LatestTime>1694576692000</LatestTime>
        <LatestTimeStr>1694576692000</LatestTimeStr>
        <Status>0,1,2</Status>
        <ProcPath>/usr/bin/sshpass</ProcPath>
        <FilePath>/etc/pam.d/su</FilePath>
        <CmdLine>["touch","/test/aaaa"]</CmdLine>
        <ProcPermission>rwxr-xr-x</ProcPermission>
        <Operation>READ</Operation>
        <InstanceName>ca_cpm_****</InstanceName>
        <IntranetIp>192.168.176.75</IntranetIp>
        <InternetIp>43.116.5.5</InternetIp>
        <GmtModified>167118088****</GmtModified>
        <Remark>test</Remark>
        <HandleTime>1694576692000</HandleTime>
        <ProcessId>52636</ProcessId>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <OrgName>test</OrgName>
        <ResourceSetName>test</ResourceSetName>
    </EventDTOList>
    <PageInfo>
        <Count>2</Count>
        <PageSize>20</PageSize>
        <TotalCount>2</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -2000 | DefenceAtLeastOneConfig | At least one protection directory is needed. |
| 500 | -100 | InternalError | The request processing has failed due to some unknown error. |

### 主机日志检索相关接口

#### DescribeFilterFields

获取日志的字段列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeFilterFie lds | 取值：DescribeFilterFields。 |
| Query | String | 是 | aegis-log- login@warn port _ :22 | 搜索日志条件。 |
| SourceIp | String | 否 | 192.168.XX.XX | 访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LogFilterList | Array of LogFilterListAr r |  | 日志过滤字段列表。 |
| Fields | String | "ip;ip地址,uuid;客户端编号","fieldsName":"d efault" | 过滤字段名。 |
| RequestId | String | CACC278C-3A9C- 41C8-A829- 1D8049AE8F16 | 本次调用请求的ID。 |
| Total | Long | 20 | 过滤规则总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeFilterFields &Query=aegis-log-login@warn_port:22
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>CACC278C-3A9C-41C8-A829-1D8049AE8F16</RequestId> <LogFilterList>
    <Fields>"ip;ip地址,uuid;客户端编号","fieldsName":"default"</Fields>
</LogFilterList> <Total>20</Total>
```

`JSON` 格式

```json
{
    "RequestId": "CACC278C-3A9C-41C8-A829-1D8049AE8F16",
    "LogFilterList": {
        "Fields": "\"ip;ip地址,uuid;客户端编号\",\"fieldsName\":\"default\""
    },
    "Total": 20
}
```

#### DescribeHistogram

获取日志数量统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeHistogr am | 取值：DescribeHistogram。 |
| EndTime | String | 是 | 2018-03-03 17:41:03 | 查询结束时间。格式：yyyy-MM-dd HH:mm:ss。 |
| Query | String | 是 | aegis-log- login@warn port _ :22 | 查询筛选字段。 |
| StartTime | String | 是 | 2018-03-02 17:41:03 | 查询开始时间。格式：yyyy-MM-dd HH:mm:ss。 |
| SourceIp | String | 否 | 192.168.x.x | 访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Categories | List | ["1519983663000, 1519984800000"," 1519984800000] | 时间集合。使用时间戳格式，单位：毫秒。 |
| Items | Array of Items |  | 数据量统计列表。 |
| Data | List | [0,0,0,0,0,0,0,0,0,0, 0,0,0,155,61] | 数据统计量。 |
| RequestId | String | CACC278C-3A9C- 41C8-A829- 1D8049AE8F16 | 本次调用请求的ID。 |

**示例**

请求示例

```
&EndTime=2018-03-03 17:41:03 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>CACC278C-3A9C-41C8-A829-1D8049AE8F16</RequestId> <Categories>["1519983663000,1519984800000","1519984800000]</Categories> <Items>
    <Data>[0,0,0,0,0,0,0,0,0,0,0,0,0,155,61]</Data>
</Items>
```

`JSON` 格式

```json
{
    "RequestId": "CACC278C-3A9C-41C8-A829-1D8049AE8F16",
    "Categories": "[\"1519983663000,1519984800000\",\"1519984800000]",
    "Items": {
        "Data": "[0,0,0,0,0,0,0,0,0,0,0,0,0,155,61]"
    }
}
```

#### DescribeLogInfo

获取日志信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLogInfo | 取值：DescribeLogInfo。 |
| CurrentPage | String | 是 | 1 | 当前页的页码。 |
| EndTime | String | 是 | 2018-03-03 17:41:03 | 日志查询结束时间。 格式：yyyy-MM-dd HH:mm:ss。 |
| PageSize | String | 是 | 20 | 每页最多显示的数据条数。 |
| Query | String | 是 | aegis-log- **@warn port:2 _ 2 | 日志查询条件。 |

| StartTime | String | 是 | 2018-03-02 17:41:03 | 日志查询开始时间。使用yyyy-MM-dd HH:mm:ss格式。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 192.168.XX.XX | 访问者源IP。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LogInfoItems | Array of Item |  | 查询日志列表。 |
| Fields | Array of Field |  | 查询日志记录列表。 |
| Desc | String | 客户端编号 | 日筛选字段名。 |
| Name | String | uuid | 筛选字段ID。 |
| Type | String | string | 字段类型。 |
| Id | String | aegis-snapshot-xxx | 日志分类ID。 |
| Name | String | 账号快照 | 日志分类名。 |
| RequestId | String | EF1F4AAF-DBF6- 481C-XXX- D1F23BCEF61A | 本次调用请求的ID。 |
| TotalCount | Integer | 202 | 总数据条数。 |

**示例**

请求示例

```
&CurrentPage=1 &EndTime=2018-03-03 17:41:03 &PageSize=20 &Query=aegis-log-**@warn_port:22 &StartTime=2018-03-02 17:41:03
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>202</TotalCount> <RequestId>EF1F4AAF-DBF6-481C-XXX-D1F23BCEF61A</RequestId> <LogInfoItems>
    <Id>aegis-snapshot-xxx</Id>
```

`<Name>`账号快照`</Name>`

```xml
    <Fields>
```

`<Desc>`客户端编号`</Desc>`

```xml
        <Type>string</Type>
        <Name>uuid</Name>
    </Fields>
</LogInfoItems>
```

`JSON` 格式

```json
{
    "TotalCount": 202,
    "RequestId": "EF1F4AAF-DBF6-481C-XXX-D1F23BCEF61A",
    "LogInfoItems": {
        "Id": "aegis-snapshot-xxx",
```

`"Name": "`账号快照`",`

```json
        "Fields": {
```

`"Desc": "`客户端编号`",`

```json
            "Type": "string",
            "Name": "uuid"
        }
    }
}
```

#### DescribeLogItems

获取日志详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLogIte ms | 取值：DescribeLogItems。 |
| CurrentPage | String | 是 | 1 | 当前页的页码。 |
| PageSize | String | 是 | 100 | 每页最多显示的数据条数。 |
| SourceIp | String | 否 | 192.168.x.x | 访问者源IP。 |
| Query | String | 否 | aegis-log- login@warn port _ :22 | 日志搜索查询。 |

| StartTime | String | 否 | 2018-03-02 17:41:03 | 开始时间。格式：yyyy-MM-dd HH:mm:ss。 |
|---|---|---|---|---|
| EndTime | String | 否 | 2018-03-05 11:46:07 | 结束时间。 格式：yyyy-MM-dd HH:mm:ss。 |
| AccountSnapsho tOffset | Integer | 否 | 1000 | 帐号快照日志偏移量。 |
| PortSnapshotOff set | Integer | 否 | 1000 | 端口日志数据偏移量。 |
| NetworkOffset | Integer | 否 | 1000 | 网络日志数据偏移量。 |
| ProcessSnapshot Offset | Integer | 否 | 1000 | 进程快照日志数据偏移量。 |
| LoginOffset | Integer | 否 | 1000 | 登录流水查询偏移量。 |
| ProcessOffset | Integer | 否 | 1000 | 进程日志数据偏移量。 |
| CrackOffset | Integer | 否 | 1000 | 暴力破解业务偏移量。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AccountSnaps hotOffset | Integer | 1000 | 帐号快照偏移量。 |
| AccountSnaps hotTotalCount | Integer | 100000 | 帐号快照总记录量。 |
| CrackOffset | Integer | 100 | 暴力破解偏移量。 |
| CrackTotalCou nt | Integer | 100000 | 暴力破解总记录数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| LoginTotalCou nt | Integer | 100000 | 登录流水数据总量。 |
| LogsList | Array of LogsListArr |  | 日志详情列表。 |
| LogSource | String | 登录流水 | 日志类型名称。 |

| LogSourceId | String | aegis-log-** | 日志类型ID |
|---|---|---|---|
| MContents | Array of MContents |  | 日志内容。 |
| MKey | String | ip | 日志KEY。 |
| MValue | String | 47.200.XX.XX | 日志值。 |
| MLogTime | String | 1520181983000 | 日志记录时间。 |
| NetworkOffset | Integer | 100 | 网络日志偏移量。 |
| NetworkTotalC ount | Integer | 100000 | 网络日志总量。 |
| PortSnapshotO ffset | Integer | 1000 | 端口快照偏移量。 |
| PortSnapshotT otalCount | Integer | 100000 | 端口快照偏移总量。 |
| ProcessOffset | Integer | 1000 | 进程偏移量。 |
| ProcessSnapsh otOffset | Integer | 1000 | 进程快照偏移量。 |
| ProcessSnapsh otTotalCount | Integer | 100000 | 进程快照总量。 |
| ProcessTotalC ount | Integer | 100000 | 进程总量。 |
| RequestId | String | CACC278C-3A9C- 41C8-A829- 1D8049AE8F16 | 本次调用请求的ID。 |
| SetPageSize | Integer | 100 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 1000000000 | 总数据条数。 |

**示例**

请求示例

```
&CurrentPage=1 &PageSize=100
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<SetPageSize>100</SetPageSize> <RequestId>CACC278C-3A9C-41C8-A829-1D8049AE8F16</RequestId> <AccountSnapshotTotalCount>100000</AccountSnapshotTotalCount> <CrackOffset>100</CrackOffset> <LogsList>
    <LogSource>登录流水</LogSource>
    <MLogTime>1520181983000</MLogTime>
    <LogSourceId>aegis-log-**</LogSourceId>
    <MContents>
        <MKey>ip</MKey>
        <MValue>47.200.XX.XX</MValue>
    </MContents>
</LogsList> <ProcessOffset>1000</ProcessOffset> <NetworkOffset>100</NetworkOffset> <ProcessSnapshotOffset>1000</ProcessSnapshotOffset> <TotalCount>1000000000</TotalCount> <CurrentPage>1</CurrentPage> <LoginTotalCount>100000</LoginTotalCount> <NetworkTotalCount>100000</NetworkTotalCount> <PortSnapshotOffset>1000</PortSnapshotOffset> <AccountSnapshotOffset>1000</AccountSnapshotOffset> <CrackTotalCount>100000</CrackTotalCount> <ProcessTotalCount>100000</ProcessTotalCount> <PortSnapshotTotalCount>100000</PortSnapshotTotalCount> <ProcessSnapshotTotalCount>100000</ProcessSnapshotTotalCount>
```

`JSON` 格式

```json
{
    "SetPageSize": 100,
    "RequestId": "CACC278C-3A9C-41C8-A829-1D8049AE8F16",
    "AccountSnapshotTotalCount": 100000,
    "CrackOffset": 100,
    "LogsList": {
```

`"LogSource": "`登录流水`",`

```json
        "MLogTime": 1520181983000,
        "LogSourceId": "aegis-log-**",
        "MContents": {
            "MKey": "ip",
            "MValue": "47.200.XX.XX"
        }
    },
    "ProcessOffset": 1000,
    "NetworkOffset": 100,
    "ProcessSnapshotOffset": 1000,
    "TotalCount": 1000000000,
    "CurrentPage": 1,
    "LoginTotalCount": 100000,
    "NetworkTotalCount": 100000,
    "PortSnapshotOffset": 1000,
    "AccountSnapshotOffset": 1000,
    "CrackTotalCount": 100000,
    "ProcessTotalCount": 100000,
    "PortSnapshotTotalCount": 100000,
    "ProcessSnapshotTotalCount": 100000
}
```

#### CreateLogQuery

**描述**

创建或保存主机日志查询条件。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：CreateLogQuery |
| Conditions | String | 否 | 日志查询条件。 |
| QueryDetail | String | 否 | 日志查询子条件 |
| QueryName | String | 否 | 保存后的查询名称。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|

| RequestId | String | 请求ID。 |
|---|---|---|

**错误码**

**示例**

请求示例

```json
https://aegis.[RegionId].example.com/?Action=CreateLogQuery &Conditions=aegis-log-login@warn_port:22 &QueryDetail=[[{"itemForm":{},"d":{"name":"登录流水","id":"aegis-log-login","fields":[ {"name":"ip","type":"string","desc":"ip地址","text":"ip（ip地址）"}]] &QueryName=test
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
}
```

#### DescribeLogQuery

**描述**

获取已保存的主机日志查询条件。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：DescribeLogQuery |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |
| ListTotal | Integer | 返回总记录数。 |
| QueryItems | Array | 日志查询条件详情，具体子项说明见以下参数描述。 |
| Conditions | String | 日志查询条件。 |
| QueryDetail | String | 日志查询子条件 |
| QueryName | String | 日志查询名称。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=DescribeLogQuery
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"65802B9B-4D30-40F0-8691-F126652DBEBE",
 "ListTotal":1,
 "QueryItems":[
  {
   "QueryDetail":"[[{\"itemForm\":{},\"d\":{\"name\":\"账号快照\",\"id\":\"aegis-
snapshot-host\",\"fields\":[{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"ip地址 \"},{\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"客户端编号\"}, {\"name\":\"perm\",\"type\":\"string\",\"desc\":\"是否拥有root权限\"}, {\"name\":\"home_dir\",\"type\":\"string\",\"desc\":\"home目录\"}, {\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"密码到期提醒时间\"},{\"name\":\"g roups\",\"type\":\"array\",\"desc\":\"用户属于的组\"}, {\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"最后一次登录的ip地址\"},{\"name\": \"last_chg\",\"type\":\"string\",\"desc\":\"密码最后修改时间\"}, {\"name\":\"shell\",\"type\":\"string\",\"desc\":\"linux的shell命令\"}, {\"name\":\"domain\",\"type\":\"string\",\"desc\":\"windows域\"}, {\"name\":\"tty\",\"type\":\"string\",\"desc\":\"登录的终端\"}, {\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"账号超期时间\"},{\"name\":\ "passwd_expire\",\"type\":\"string\",\"desc\":\"密码超期时间\"}, {\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"最后登录时间\"}, {\"name\":\"user\",\"type\":\"string\",\"desc\":\"用户\"},
```

{\"name\":\"status\",\"type\":\"string\",\"desc\":\"用户状态：`0-`禁用、`1-`正常

```json
\"}]},\"searchFields\":[{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"ip地址\"}, {\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"客户端编号\"}, {\"name\":\"perm\",\"type\":\"string\",\"desc\":\"是否拥有root权限\"}, {\"name\":\"home_dir\",\"type\":\"string\",\"desc\":\"home目录\"}, {\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"密码到期提醒时间\"},{\"name\":\"g roups\",\"type\":\"array\",\"desc\":\"用户属于的组\"}, {\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"最后一次登录的ip地址\"},{\"name\": \"last_chg\",\"type\":\"string\",\"desc\":\"密码最后修改时间\"}, {\"name\":\"shell\",\"type\":\"string\",\"desc\":\"linux的shell命令\"}, {\"name\":\"domain\",\"type\":\"string\",\"desc\":\"windows域\"}, {\"name\":\"tty\",\"type\":\"string\",\"desc\":\"登录的终端\"}, {\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"账号超期时间\"},{\"name\":\ "passwd_expire\",\"type\":\"string\",\"desc\":\"密码超期时间\"}, {\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"最后登录时间\"}, {\"name\":\"user\",\"type\":\"string\",\"desc\":\"用户\"}, {\"name\":\"status\",\"type\":\"string\",\"desc\":\"用户状态：0-禁用、1-正常\"}],\"f\":{ \"name\":\"ip\",\"type\":\"string\",\"desc\":\"ip地址\"},\"searchLimit\":[{\"name\":\" 包含\",\"value\":\":\"}],\"l\":\":\",\"kw\":\"string\"}]]",
   "Conditions":"aegis-snapshot-host@ip:string",
   "QueryName":"aa"
  }
```

]

```
}
```

#### DeleteLogQuery

**描述**

删除已保存的主机日志查询条件。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名，系统规定参数。 取值：DeleteLogQuery |
| QueryName | String | 否 | 已保存的查询名称。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

**错误码**

**示例**

请求示例

```
https://aegis.[RegionId].example.com/?Action=DeleteLogQuery &QueryName=test
```

`&<`公共请求参数> 返回示例（JSON格式）

```json
{
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
}
```

### 主机规则设置相关接口

#### CreateAntiBruteForceRule

创建防暴力破解规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| Resource OwnerId | Long | Query | 否 | 1000000**** | 鉴权相关的系统参数，不填。 |
| Name | Strin g | Query | 否 | 规则**** | 漏洞名称。 |
| Span | Integ er | Query | 否 | 1 | 设置账号登录失败的时间的阈值，单位为分钟。取值： 1 ：1分钟 2 ：2分钟 5 ：5分钟 10 ：10分钟 15 ：15分钟 Span、FailCount、 ForbiddenTime这三个参数组合成一个防暴力破解规则，表示XX 分钟内账号登录失败超过XX次，该账号禁止登录XX分钟。 |
| FailCount | Integ er | Query | 否 | 2 | 设置账号登录失败次数的阈值。单位为次。取值：2、 3、4、5、10、50、80、 100。 |
| Forbidden Time | Integ er | Query | 否 | 5 | 禁止账号登录的时长，单位为分钟。取值： 5 ：5分钟 15 ：15分钟 30 ：30分钟 60 ：1小时 120 ：2小时 360 ：6小时 720 ：12小时 1440 ：24小时 10080 ：7天 52560000 ：永久 （100年） |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UuidList | Repe atList | Query | 否 | a9a95aad-2b60-4812- b22d- ***********,a9a95aad- 2b60-4812-b22d- *********** | 要修改的标签下的资产实例的UUID列表。多个UUID使用半角逗号（,）分隔。 说明：您可调用 DescribeCloudCent erInstances接口查询资产标签下的资产实例的UUID列表。如果该参数为空，将清空 TagList参数指定的标签下的所有资产实例。 |
| DefaultRul e | Boole an | Query | 否 | true | 默认转发规则。按照IP地址，通过指定端口转发流量到指定应用。参数说明如下： appId ：应用ID。 containerPort ：应用实例端口。 所有未匹配或不满足Rules 转发规则的请求都会转到该指定应用。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| CreateAntiBrut eForceRule | Struct | {"ruleName": "block after 5 atte _ _ _ mpts", "maxAttempts": 5, "lockoutTime": 300} | 创建的防暴力破解规则的信息。 |
| -RuleId | Long | 123 | 规则ID |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateAntiBruteForceRule
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
  "RuleId":123
 }
}
```

#### ModifyAntiBruteForceRule

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- aegis:ModifyAntiBruteForceRule | Write | acs:yundun-aegis:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| Id | Long | Query | 否 | 65778 | 暴力破解防御规则的ID。 |
| Name | Strin g | Query | 否 | TestRule | 暴力破解防御规则的名称。 |
| Span | Integ er | Query | 否 | 1 | 账号登录失败的时间间隔， 单位为分钟。取值： 1：1分钟 2：2分钟 5：5分钟 10：10分钟 15：15分钟。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FailCount | Integ er | Query | 否 | 10 | 账号登录失败次数的阈值。 取值： 2：2次 3：3次 4：4次 5：5次 10：10次 50：50次 80：80次 100：100次。 |
| Forbidden Time | Integ er | Query | 否 | 5 | 禁止账号登录的时长，单位为分钟。取值： 5：5分钟 15：15分钟 30：30分钟 60：1小时 120：2小时 360：6小时 720：12小时 1440：24小时 10080：7天 52560000：永久（100 年）。 |
| UuidList | Repe atList | Query | 否 | [ { "uuid": "a9a95aad- 2b60-4812-b22d- ***********" }, { "uuid": "a9a95aad-2b60-4812- b22d-***********" } ] | 暴力破解防御规则生效的服务器列表。 |
| DefaultRul e | Boole an | Query | 否 | true | 添加的暴力破解防御规则是否设置为默认策略。取值： true：设置为默认策略 false：不设置为默认策略。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=ModifyAntiBruteForceRule&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&ResourceOwnerId=&Id=65778&Name=TestRule&Span=1&FailCount= &ForbiddenTime=5&UuidList.1={"uuid":"a9a95aad-2b60-4812-b22d-
***********"}&DefaultRule=true
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
```

**文档补充说明**

{ "PageInfo":{ "TotalCount":10, "PageSize":10, "CurrentPage":1, "Count":1 }, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Rules":[ { "Uuid":"49e25e0f-bb51-4a5a-a1b3-13a4ddaa****", "Id":1, "Name":"test" } ] }

#### DescribeAntiBruteForceRules

查询您已创建的防暴力破解规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 1000000**** | 访问源IP地址。 |
| Resource OwnerId | Long | Query | 否 | 1000000**** | 鉴权相关的系统参数，不填。 |
| Id | Long | Query | 否 | 245 | 基线策略ID。 |
| CurrentPa ge | Integ er | Query | 否 | 4 | 分页查询时，当前页的页码。 |
| PageSize | Strin g | Query | 否 | 无 | 分页查询时，每页显示的记录数。 |
| Name | Strin g | Query | 否 | 规则**** | 漏洞名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Rules | Array | - | 检查项支持的规则列表。 |
| -UuidList | List | ["3bb30859-b3b5- 4f28-868f- b0892c98****"] | 指定待查询的资产UUID。多个用半角英文逗号分割。 |
| -Id | Long | 1 | 策略ID。 |
| -DefaultRule | Boolean | true | 当前规则是否为默认规则。取值： true ：是默认规则。 false ：不是默认规则。 设置为默认规则的防暴力破解规则会对所有未添加防御规则的服务器生效。 |
| -Name | String | test | 漏洞名称。 |
| -Span | Integer | 10 | 暴力破解防御规则生效的时间阈值，单位为分钟。例如span 为10，表示如果在10分钟内登录失败次数超过设置的阈值，防暴力破解规则会生效并在指定时间内拦截登录。 |
| -FailCount | Integer | 0 | 失败数量。 |

| 安骑士开发指南·AP | I参考 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ForbiddenTime | Integer | 360 | 暴力破解防御规则生效后对攻击方IP禁用的时间，单位（分钟）。 |
| - EnableSmartR ule | Boolean | false | 该参数已废弃，无需关注。 |
| -MachineCount | Integer | 1 | 存在安全告警的服务器的数量。 |
| - CreateTimesta mp | Long | 1527690629357 | 最新扫描时间。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| PageInfo | Struct | - | 分页查询时的页面信息。 |
| -Count | Integer | 1 | 分页查询时，当前页显示的数据条数。 |
| -PageSize | Integer | 10 | 分页查询时，每页最多显示的数据条数。 |
| -TotalCount | Integer | 10 | 数据总条数。 |
| -CurrentPage | Integer | 1 | 当前页的页码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAntiBruteForceRules
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "PageInfo":{
  "TotalCount":10,
  "PageSize":10,
  "CurrentPage":1,
  "Count":1
 },
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Rules":[
  {
   "DefaultRule":true,
   "ForbiddenTime":360,
   "UuidList":[
                                                   "3bb30859-b3b5-4f28-868f-b0892c98****"
```

`],`

```json
   "FailCount":0,
   "EnableSmartRule":false,
   "MachineCount":1,
   "Id":1,
   "Span":10,
   "CreateTimestamp":1527690629357,
   "Name":"test"
  }
```

]

```
}
```

`XML` 格式

#### DescribeInstanceAntiBruteForceRules

查询暴力破解防御规则生效的服务器信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| Resource OwnerId | Long | Query | 否 | 1000000**** | 鉴权相关的系统参数，不填。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UuidList | Repe atList | Query | 否 | a9a95aad-2b60-4812- b22d- ***********,a9a95aad- 2b60-4812-b22d- *********** | 要修改的标签下的资产实例的UUID列表。多个UUID使用半角逗号（,）分隔。 说明：您可调用 DescribeCloudCent erInstances接口查询资产标签下的资产实例的UUID列表。如果该参数为空，将清空 TagList参数指定的标签下的所有资产实例。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Rules | Array | dubbo | 检查项支持的规则列表。 |
| -Id | Long | 1 | 策略ID。 |
| -Name | String | test | 漏洞名称。 |
| -Uuid | String | 49e25e0f-bb51- 4a5a-a1b3- 13a4ddaa**** | 服务器UUID。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| PageInfo | Struct | - | 分页查询时的页面信息。 |
| -Count | Integer | 1 | 分页查询时，当前页显示的数据条数。 |
| -PageSize | Integer | 10 | 分页查询时，每页最多显示的数据条数。 |
| -TotalCount | Integer | 10 | 数据总条数。 |
| -CurrentPage | Integer | 1 | 当前页的页码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeInstanceAntiBruteForceRules
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "PageInfo":{
  "TotalCount":10,
  "PageSize":10,
  "CurrentPage":1,
  "Count":1
 },
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Rules":[
  {
   "Uuid":"49e25e0f-bb51-4a5a-a1b3-13a4ddaa****",
   "Id":1,
   "Name":"test"
  }
```

]

```
}
```

## 错误代码表

本文介绍云盾API返回的错误代码信息。 表 1. 云盾通用错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.all.10001 | 权限不够 | 请检查账户权限。 |
| yd.error.all.10002 | 系统错误，请稍后重试 | 请稍后重试。 |
| yd.error.all.10003 | 参数错误 | 请检查请求参数后重试。 |
| yd.error.all.other | 系统异常 | 请稍后重试。 |
| yd.error.all.ConsoleSystemError 1001 _ | 未知异常 | 请稍后重试。 |
| yd.error.all.ConsoleSystemError 1007 _ | api已下线 | 请联系阿里云技术支持人员。 |
| yd.error.all.ConsoleSystemError 1008 _ | postOnly校验失败 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError 1009 _ | csrfToken为空 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError 1010 _ | csrfToken校验失败 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError 1011 _ | regionId为空 | 请检查RegionId请求参数。 |
| yd.error.all.ConsoleSystemError 1012 _ | regionId格式错误 | 请检查RegionId请求参数。 |
| yd.error.all.ConsoleSystemError 1013 _ | 参数为空 | 请检查请求参数后重试。 |
| yd.error.all.ConsoleSystemError 1014 _ | 参数格式错误 | 请检查请求参数后重试。 |
| yd.error.all.ConsoleNeedLogin | 未登录 | 请检查账户权限。 |
| yd.error.all.InvalidApi | 接口异常 | 请稍后重试。 |
| yd.error.all.InvalidParameter | 参数异常 | 请检查请求参数后重试。 |
| yd.error.all.InvalidResult | 返回值异常 | 请稍后重试。 |
| yd.error.all.PropertyConvertFail ed | 转换异常 | 请稍后重试。 |
| yd.error.all.NoPermission | 无权限 | 请检查账户权限。 |
| yd.error.all.ServerError | 服务器异常 | 请稍后重试或联系阿里云技术支持人员。 |

| yd.error.all.UnkownError | 未知异常 | 请稍后重试或联系阿里云技术支持人员。 |
|---|---|---|

表 2. 态势感知错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.sas.1 | 您要查询的字段并不在元数据里 | 请检查后重试。 |
| yd.error.sas.2 | 调用任务引擎失败，请重试 | 请稍后重试。 |
| yd.error.sas.3 | 启动任务失败，请重试 | 请稍后重试。 |
| yd.error.sas.4 | 停止任务失败，请重试 | 请稍后重试。 |
| yd.error.sas.5 | 重启任务失败，请重试 | 请稍后重试。 |
| yd.error.sas.6 | 获取任务状态失败，请重试 | 请稍后重试。 |
| yd.error.sas.7 | 删除任务失败，请重试 | 请稍后重试。 |
| yd.error.sas.8 | 您要查询的表还没有配置元数据 | 请检查后重试。 |
| yd.error.sas.100 | 当前请求失败，建议您刷新页面或者稍后重试 | 请稍后重试。 |
| yd.error.sas.101 | 参数错误 | 请检查后重试。 |
| yd.error.sas.103 | 请求失败 | 请稍后重试。 |
| yd.error.sas.400 | 该资产的防护状态为在线，请先卸载安骑士客户端后再尝试删除 | 请先从该主机中卸载安骑士Agent客户端后重试。 |
| yd.error.sas.500 | 系统错误 | 请联系阿里云技术支持人员。 |
| yd.error.sas.501 | 当前版本无此功能 | 您当前版本不支持此功能。 |
| yd.error.sas.502 | 用户没有这台机器的权限 | 您没有操作该主机的权限。 |

表 3. DDoS防护错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.ddos.400 | 访问服务端异常，请检查请求重试 | 请检查后重试。 |
| yd.error.ddos.500 | 服务端异常，请联系研发 | 请联系阿里云技术支持人员。 |
| yd.error.ddos.UNKNOWN EXCE _ PTION | 未知异常 | 请联系阿里云技术支持人员。 |
| yd.error.ddos.REQUEST TIMEO _ UT | 请求超时 | 请稍后重试。 |
| yd.error.ddos.SERVER FAILED _ | 操作失败 | 请联系阿里云技术支持人员。 |
| yd.error.ddos.NOT AUTHORIZE _ D | 没有权限 | 请检查账户权限。 |

| yd.error.ddos.PARAMETER INVA _ LID | 参数无效或缺少 | 请求参数有误，请检查后重试。 |
|---|---|---|
| yd.error.ddos.IP SEGMENT INV _ _ ALID | IP段不合法，请检查后重新输入 | 请检查请求参数中的IP网段。 |
| yd.error.ddos.IP SEGMENT REP _ _ EAT | 同一网段不能配置不同区域，请检查后重新输入 | 请检查请求参数中的IP网段。 |
| yd.error.ddos.IP SEGMENT ALR _ _ EADY | 网段已存在，请重新输入 | 请检查请求参数中的IP网段。 |
| yd.error.ddos.IP SEGMENT MAS _ _ K LENGTH ERR _ _ | 掩码长度需小于或等于24字符 | 请检查请求参数中的IP网段的掩码。 |
| yd.error.ddos.QUERY REGION L _ _ IST ERR _ | 读取区域列表失败 | 请稍后重试。 |
| yd.error.ddos.IP SEGMENT OPE _ _ RATION ERR _ | 处理网段操作失败 | 请稍后重试。 |
| yd.error.ddos.QUERY IP SEGME _ _ NT ERR _ | 读取网段信息失败 | 请稍后重试。 |
| yd.error.ddos.MODIFY IP SEGM _ _ ENT ERR _ | 修改网段信息失败 | 请稍后重试。 |
| yd.error.ddos.IP SEGMENT TYP _ _ E ERR _ | 请检查是否设置网段类型（外网网段或内网网段） | 请检查网段类型后重试。 |
| yd.error.ddos.CANCEL FLOW C _ _ LEAN ERR _ | 取消清洗失败，请确认与beaver的网络连接是否正常 | 请检查与流量安全监控模块的网络连接后重试。 |
| yd.error.ddos.QUERY FLOW AN _ _ ALYSIS ERR _ | 获取流量分析结果失败，请确认与 beaver的网络连接是否正常 | 请检查与流量安全监控模块的网络连接后重试。 |
| yd.error.ddos.QUERY BEAVER _ _ URL ERR _ | 获取beaver Url失败 | 请检查与流量安全监控模块的网络连接后重试。 |
| yd.error.ddos.SET VALVE INVA _ _ LID | 阈值校验失败，请确认各阈值后重新输入 | 请检查阈值参数后重试。 |
| yd.error.ddos.VALVE DEFAULT _ _ ALREADY | 无效的请求，不允许再次添加 default阈值 | 无法再次添加默认阈值，只能修改。 |
| yd.error.ddos.NOT BELONG BE _ _ AVER IP SEGMENT _ _ | 请检查输入网段是否属于Beaver内网网段 | 请检查网段是否属于流量监控内网网段。 |
| yd.error.ddos.VALVE DELETE E _ _ RR | default或128.0.XX.XX/XX，阈值不允许删除 | 默认阈值或128.0.XX.XX/XX网段的阈值无法删除 |
| yd.error.ddos.QUERY CODE ER _ _ R | 读取字典异常 | 请稍后重试。 |
| yd.error.ddos.IS OPENED _ | 已开启 | 指定开关已处于开启状态，无法再次开启。 |
| yd.error.ddos.IS CLOSED _ | 已关闭 | 指定开关已处于关闭状态，无法再次关闭。 |

表 4. 安骑士错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.aqs.REQUEST FAILED _ | 请求失败， 请稍后重试 | 请稍后重试。 |

表 5. 安全审计错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.audit.Alert.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Alert.IdNotExist | 接收人不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.IdNotExi st | 接收人不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.LogTyp eEmpty | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.LogTyp ePatternWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.LogSour ceidNotExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.NameE mpty | 【名称】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.NameLe ngthWrong | 【名称】不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.Contact Empty | 【联系方式】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.Contact LengthWrong | 【联系方式】不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.Contact NotEmail | 【联系方式】必须为邮件格式 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotExist | 字典值【%s】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotBoolean | 字典值非Boolean类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotInteger | 字典值非Integer类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotLong | 字典值非Long类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotFloat | 字典值非Float类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotDouble | 字典值非Double类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotString | 字典值非String类型 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.IdEmp ty | 【id】不能为空 | 请检查请求参数后重试。 |

| yd.error.audit.EventType.IdNot Exist | 事件类型不存在 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.EventType.LogTy peEmpty | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.LogTy pePatternWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.LogSo urceIdNotExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.Reser vedEmpty | 【是否预留】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.Name Empty | 【名称】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.Name LengthWrong | 【名称】不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.Rema rkLengthWrong | 【备注】不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.IdNotExist | 规则不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.LogTypeEm pty | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.LogTypePatt ernWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.LogSourceId NotExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.NameEmpty | 【名称】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.NameLengt hWrong | 【名称】长度不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.ExpressionE mpty | 【表达式】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.ExpressionL engthWrong | 【表达式】长度不成超过500字符 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.ExpressionP atternWrong | 【表达式】正则表达式格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.EventTypeE mpty | 【事件类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.EventTypeN otExist | 【事件类型】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.RiskLevelEm pty | 【风险级别】不能为空 | 请检查请求参数后重试。 |

| yd.error.audit.Rule.ReserverEm pty | 【是否预留】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.Rule.EnableEmpt y | 【是否启用】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.AlerttAbleE mpty | 【是否告警】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.AlerttAction Empty | 【告警动作】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.AlerttAciton PatternWrong | 【告警动作】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.RemarkLeng thWrong | 【备注】不能超过20000字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.IdEmpt y | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.Enable Empty | 【是否启用】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.AlerttA bleEmpty | 【是否告警】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.TypeE mpty | 【类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.TypeP atternWrong | 【类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogSto rePeriodEmpty | 【日志存储周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogArc hivePeriodEmpty | 【日志归档周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogArc hivePeriodLengthWrong | 【日志归档周期】不能超过1095天 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogArc hiveIntervalEmpty | 【日志归档间隔】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogArc hiveIntervalPatternWrong | 【日志归档间隔】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventS torePeriodEmpty | 【事件存储周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventS torePeriodLengthWrong | 【事件存储周期】不能超过1095天 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventA rchivePeriodEmpty | 【事件归档周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventA rchivePeriodLengthWrong | 【事件归档周期】不能超过1095天 | 请检查请求参数后重试。 |

| yd.error.audit.LogConfig.EventA rchiveIntervalEmpty | 【事件归档间隔】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.LogConfig.EventA rchiveIntervalPatternWrong | 【事件归档间隔】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.IdNotExi st | 【id】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.TypeEm pty | 【类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.TypePat ternWrong | 【类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.UserIdE mpty | 【用户】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.UserIdL engthWrong | 【用户】长度不成超过500字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.LogType .emtpy | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.LogType PatternWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.LogSour ceIdNotExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.IdEmp ty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.LogTy peEmpty | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeE mpty | 【编码】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeL engthWrong | 【编码】长度不能超过50字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeP atternWrong | 【编码】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeN otExist | 【编码】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeE xist | 【编码】已存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.Name Empty | 【名称】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.Name LengthWrong | 【名称】长度不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.Enabl eEmpty | 【是否启用】不能为空 | 请检查请求参数后重试。 |

|  |  | 安骑士开发指南·错误代码表 |
|---|---|---|

| yd.error.audit.LogSource.Alertt AbleEmpty | 【是否告警】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.LogSource.TypeP atternWrong | 【类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.Remar kLengthWrong | 【备注】长度不能超过20000字符 | 请检查请求参数后重试。 |
| yd.error.audit.log.LogSourceIdN otExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.ProcessTask.IdE mpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.ProcessTask.Type Empty | 【任务类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.ProcessTask.Para mEmpty | 【执行参数】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.ProcessTask.Para mPatternWrong | 【执行参数】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.System.Error | 系统内部错误 | 请联系阿里云技术支持人员。 |
| yd.error.audit.System.NotFind | 资源未找到 | 请稍后重试。 |
| yd.error.audit.System.AuthError | 权限认证失败 | 请检查账户权限。 |

表 6. 同步中心错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.scs.100 | 请求参数错误 | 请求参数有误，请检查后重试。 |
| yd.error.scs.101 | 未授权 | 请检查账户权限。 |
| yd.error.scs.102 | 无需更新 | 指定业务规则库无需更新。 |
| yd.error.scs.500 | 内部异常 | 请联系阿里云技术支持人员。 |
| yd.error.ddos.UPGRADE SWITC _ H ERR _ | 升级通道开关失败 | 请稍后重试。 |
| yd.error.ddos.AUTO UPGRADE _ _ SWITCH | 自动升级通道操作失败 | 请稍后重试。 |

表 7. 云防火墙错误码

| 错误代码 | 错误信息 |
|---|---|
| yd.error.code.200 | 请求成功 |
| yd.error.code.-360100 | 请求方式错误 |

| yd.error.code.-360101 | 认证失败 |
|---|---|
| yd.error.code.-360102 | 本地调用错误 |
| yd.error.code.-360103 | 参数错误，请重试 |
| yd.error.code.-360104 | 应用选择错误，请重试 |
| yd.error.code.-360105 | 获取日志失败 |
| yd.error.code.-360106 | 获取日志失败 |
| yd.error.code.-360107 | uid错误，请重试 |
| yd.error.code.-360108 | 分页错误 |
| yd.error.code.-360109 | 产品不支持 |
| yd.error.code.-360110 | IP地址格式错误，请重新输入 |
| yd.error.code.-360111 | 时间选择错误，请重新选择 |
| yd.error.code.-360112 | 解析错误 |
| yd.error.code.-360113 | 防火墙名错误，请重新输入 |
| yd.error.code.-360114 | 互通类型选择错误，请重新选择 |
| yd.error.code.-360115 | VPC选择错误，请重新选择 |
| yd.error.code.-360116 | 地域选择错误，请重新输入 |
| yd.error.code.-360117 | 目标网段错误，请正确配置目标网段 |
| yd.error.code.-360118 | 指定的VPC防火墙不存在，请重新选择 |
| yd.error.code.-360119 | 防火墙已配置，不能重复新建 |
| yd.error.code.-360120 | 未授权，不可访问，请先授权防火墙权限 |
| yd.error.code.-360121 | 安全组错误 |
| yd.error.code.-360122 | 安全组错误 |
| yd.error.code.-360123 | 调用ECS接口错误 |
| yd.error.code.-360124 | 调用VPC接口错误 |
| yd.error.code.-360125 | 网段CIDR格式错误，请重新选择 |
| yd.error.code.-360126 | 创建交换机错误 |
| yd.error.code.-360127 | 创建网络接口错误 |
| yd.error.code.-360128 | 删除网络接口错误 |
| yd.error.code.-360129 | 未授权，请重试 |

| yd.error.code.-360130 | ECS不可用 |
|---|---|
| yd.error.code.-360131 | 未知错误 |
| yd.error.code.-360132 | 路由表查找失败 |
| yd.error.code.-360133 | 防火墙ID错误 |
| yd.error.code.-360134 | 防火墙状态错误，请稍后再试 |
| yd.error.code.-360135 | 防火墙开关参数错误，请重新选择 |
| yd.error.code.-360136 | 防火墙状态参数错误，请重新选择 |
| yd.error.code.-360137 | 未知用户，请重试 |
| yd.error.code.-360138 | 防火墙VPC参数错误，请重新选择 |
| yd.error.code.-360139 | 防火墙VPC参数错误，请重新选择 |
| yd.error.code.-360140 | 指定的防火墙不存在，请重新选择 |
| yd.error.code.-360141 | 防火墙未配置，请先新建配置 |
| yd.error.code.-360142 | 防火墙已开启 |
| yd.error.code.-360143 | 防火墙已关闭 |
| yd.error.code.-360144 | 防火墙状态错误，不能开启，请稍后再试 |
| yd.error.code.-360145 | 防火墙状态错误，不能关闭，请稍后再试 |
| yd.error.code.-360146 | 防火墙网卡错误，请确认网卡配置 |
| yd.error.code.-360147 | 目标网段错误，请重新选择 |
| yd.error.code.-360148 | 相同网段不能重复配置，请重新选择网段 |
| yd.error.code.-360149 | 目标网段数量超过最大数量限制，请减少网段数量 |
| yd.error.code.-360150 | 防火墙ID错误 |
| yd.error.code.-360151 | 网络接口状态错误 |
| yd.error.code.-360152 | 网络接口错误 |
| yd.error.code.-360153 | 网络接口错误 |
| yd.error.code.-360154 | 网络接口创建超时 |
| yd.error.code.-360155 | 网络接口删除超时 |
| yd.error.code.-360156 | 权限不足，请重试 |
| yd.error.code.-360157 | 路由表不存在 |
| yd.error.code.-360158 | 路由条目错误 |

| yd.error.code.-360159 | 路由创建失败 |
|---|---|
| yd.error.code.-360160 | 路由删除失败 |
| yd.error.code.-360161 | 路由创建超时 |
| yd.error.code.-360162 | 路由删除超时 |
| yd.error.code.-360163 | 路由非法 |
| yd.error.code.-360164 | 任务状态错误 |
| yd.error.code.-360165 | 防火墙开启失败，请重试 |
| yd.error.code.-360166 | 防火墙关闭失败，请重试 |
| yd.error.code.-360167 | 参数错误，请重试 |
| yd.error.code.-360168 | 参数错误，请重试 |
| yd.error.code.-360169 | 参数错误，请重试 |
| yd.error.code.-360170 | 参数错误，请重试 |
| yd.error.code.-360171 | Region错误 |
| yd.error.code.-360172 | 路由操作太频繁 |
| yd.error.code.-360173 | 已配置的VPC防火墙达到最大数量，请购买扩容 |
| yd.error.code.-360174 | 已配置的VPC防火墙达到最大数量，请购买扩容 |
| yd.error.code.-360175 | 参数错误，请重试 |
| yd.error.code.-360176 | 参数错误，请重试 |
| yd.error.code.-360177 | 参数错误，请重试 |
| yd.error.code.-360178 | 未知错误 |
| yd.error.code.-360179 | 调用接口失败 |
| yd.error.code.-360180 | cen对应的VPC数量不足 |
| yd.error.code.-360181 | cen的防火墙已经覆盖，不需要再新建 |
| yd.error.code.-360182 | 安全组不存在 |
| yd.error.code.-360183 | 安全组无法删除 |
| yd.error.code.-360184 | 未知错误 |
| yd.error.code.-360185 | 更新防火墙路由失败 |
| yd.error.code.-360186 | 当前防火墙状态，不允许配置 |
| yd.error.code.-360187 | 此地域VPC数量不足，无法开启VPC防火墙 |

| yd.error.code.-360188 | 配额不足，无法配置VPC防火墙，请先增加配额 |
|---|---|
| yd.error.code.-360189 | 删除时ECS不存在 |
| yd.error.code.-360190 | 调用接口失败 |
| yd.error.code.-360191 | 参数错误，请重试 |
| yd.error.code.-360192 | 所属账号错误，请重新输入 |
| yd.error.code.-360193 | 所属账号未授权，未购买云防火墙 |
| yd.error.code.-360194 | 配置IPS失败 |
| yd.error.code.-360195 | 云企业网VPC数量不足，无法开启VPC边界防火墙 |
| yd.error.code.-360196 | VPC边界防火墙仅支持同地域，不支持跨地域 |
| yd.error.code.-360197 | 任务冲突 |
| yd.error.code.-360198 | 目标网段为空，不允许创建 |
| yd.error.code.-360199 | 加入cen超时 |
| yd.error.code.-360200 | VSwitch创建超时 |
| yd.error.code.-360201 | VSwitch删除超时 |
| yd.error.code.-360202 | 网络实例ID非法 |
| yd.error.code.-360203 | VPC不存在 |
| yd.error.code.-360204 | 创建VPC超时 |
| yd.error.code.-360205 | 创建VPC超时 |
| yd.error.code.-360206 | ECS实例不存在 |
| yd.error.code.-360207 | ECS实例关闭失败，请重试 |
| yd.error.code.-360208 | 获取备份ECS实例失败 |
| yd.error.code.-360209 | HUB VPC不允许创建防火墙 |
| yd.error.code.-360210 | cen ID错误 |
| yd.error.code.-360211 | 参数错误，请重试 |
| yd.error.code.-360212 | 云企业网VPC数量限制，无法开启VPC边界防火墙 |
| yd.error.code.-360213 | cen未找到 |
| yd.error.code.-360214 | 请求超时，请重试 |
| yd.error.code.-360215 | 参数错误，请重试 |
| yd.error.code.-360216 | IDC专线错误 |

| yd.error.code.-360217 | 防火墙模式错误 |
|---|---|
| yd.error.code.-360218 | 调用xnet接口失败 |
| yd.error.code.-360300 | 后台错误 |
| yd.error.code.-360301 | 后台错误 |
| yd.error.code.-360302 | 后台错误 |
| yd.error.code.-360303 | 后台错误 |
| yd.error.code.-360304 | 后台错误 |
| yd.error.code.-360305 | 后台错误 |
| yd.error.code.-360306 | 后台错误 |
| yd.error.code.-360307 | 后台错误 |
| yd.error.code.-360308 | 查询集群ID失败 |
| yd.error.code.-360309 | 更新集群信息失败 |
| yd.error.code.-360310 | 更新物理专线失败 |
| yd.error.code.-360311 | 插入Vlan失败 |
| yd.error.code.-360312 | 查询IP池失败 |
| yd.error.code.-360313 | 更新IP池失败 |
| yd.error.code.-360314 | 更新VPC路由信息失败 |
| yd.error.code.-360315 | 更新VPC状态失败 |
| yd.error.code.-360316 | 插入防火墙ns失败 |
| yd.error.code.-360317 | 更新Vlan失败 |
| yd.error.code.-360318 | 更新防火墙接口信息失败 |
| yd.error.code.-360319 | 更新防火墙网络信息失败 |
| yd.error.code.-360320 | 更新健康检查配置失败 |
| yd.error.code.-360321 | 更新路由表失败 |
| yd.error.code.-360322 | 更新IDC专线失败 |
| yd.error.code.-360323 | 更新IDC路由信息失败 |
| yd.error.code.-360400 | 未知错误 |
| yd.error.code.-360401 | 没有可用的Vlan |
| yd.error.code.-360402 | 调用VPC接口失败 |

| yd.error.code.-360403 | 创建虚墙失败 |
|---|---|
| yd.error.code.-360404 | 物理专线创建失败 |
| yd.error.code.-360405 | 物理专线使能失败 |
| yd.error.code.-360406 | 创建VBR失败 |
| yd.error.code.-360407 | 更新VBR属性失败 |
| yd.error.code.-360408 | 查询VBR失败 |
| yd.error.code.-360409 | 创建RI失败 |
| yd.error.code.-360410 | 更新RI属性失败 |
| yd.error.code.-360411 | 连接RI失败 |
| yd.error.code.-360412 | IDC专线创建失败 |
| yd.error.code.-360413 | IDC专线使能失败 |
| yd.error.code.-360414 | 查询RI失败 |
| yd.error.code.-360415 | 查询VPC探测IP列表失败（VPC-VPC） |
| yd.error.code.-360416 | 查询VPC探测IP列表失败（IDC-VPC） |
| yd.error.code.-360417 | VPC探测模式异常 |
| yd.error.code.-360418 | 实例状态无效 |
| yd.error.code.-193000 | 未知错误 |
| yd.error.code.-193001 | HTTP请求方法不匹配 |
| yd.error.code.-193002 | HTTP调用失败 |
| yd.error.code.-193003 | 操作权限不足 |
| yd.error.code.-193004 | 不支持的操作 |
| yd.error.code.-193005 | 认证错误 |
| yd.error.code.-193006 | DB访问错误 |
| yd.error.code.-193007 | 访问了本地方法 |
| yd.error.code.-193101 | JSON编码失败 |
| yd.error.code.-193102 | JSON解析失败 |
| yd.error.code.-193103 | 解析INT失败 |
| yd.error.code.-193104 | 解析BOOL失败 |
| yd.error.code.-193105 | 解析HTTP BODY失败 |

| yd.error.code.-193201 | 参数不足 |
|---|---|
| yd.error.code.-193202 | 参数超范围 |
| yd.error.code.-193203 | 时间参数超范围 |
| yd.error.code.-193204 | 无效的参数 |
| yd.error.code.-193205 | IP不在引流配置网段内 |
| yd.error.code.-193301 | 重复的网段 |
| yd.error.code.-193302 | 无效的防火墙UUID |
| yd.error.code.-193303 | FW模式正在切换中 |
| yd.error.code.-193304 | FW模式无效 |
| yd.error.code.-193305 | FW模式非法切换 |
| yd.error.code.-193306 | 设备模式切换中 |
| yd.error.code.-193307 | 实例健康检查异常，实例模式无法切换为正常模式 |
| yd.error.code.-193308 | 所有设备均旁路，无法切换实例模式 |
| yd.error.code.-193309 | 实例的工作模式高于设备的工作模式 |
| yd.error.code.-193310 | 传递过来的页码无效 |
| yd.error.code.-193311 | 路由类型错误 |
| yd.error.code.-193312 | 路由删除失败 |
| yd.error.code.-193313 | 路由删除失败 |
| yd.error.code.-193314 | 路由添加失败 |
| yd.error.code.-193315 | 路由添加失败 |
| yd.error.code.-193316 | 错误的防火墙实例ID |
| yd.error.code.-193317 | 防火墙实例不能为空 |
| yd.error.code.-200100 | 请求方式错误 |
| yd.error.code.-200101 | 认证失败 |
| yd.error.code.-200102 | 本地调用错误 |
| yd.error.code.-200103 | 参数错误，请重试 |
| yd.error.code.-200104 | uid错误，请重试 |
| yd.error.code.-200105 | 分页错误 |
| yd.error.code.-200106 | 地址簿IP地址错误，请检查输入 |

| yd.error.code.-200107 | 地址簿已存在 |
|---|---|
| yd.error.code.-200108 | 请求错误，请稍后重试 |
| yd.error.code.-200109 | 地址簿在使用中，无法删除 |
| yd.error.code.-200110 | 参数无效 |
| yd.error.code.-200111 | 参数无效 |
| yd.error.code.-200112 | 参数无效 |
| yd.error.code.-200113 | 参数无效 |
| yd.error.code.-200114 | 参数无效 |
| yd.error.code.-200115 | 参数无效 |
| yd.error.code.-200116 | 参数无效 |
| yd.error.code.-200117 | 安全组规则不存在 |
| yd.error.code.-200118 | 优先级配置错误或已经达到规则数目上限 |
| yd.error.code.-200119 | 优先级配置错误或已经达到规则数目上限 |
| yd.error.code.-200120 | 请求错误，请稍后重试 |
| yd.error.code.-200121 | 域名参数错误，请检查输入 |
| yd.error.code.-200122 | 地址簿内地址数量超出上限 |
| yd.error.code.-200123 | 参数无效 |
| yd.error.code.-200124 | 参数无效 |
| yd.error.code.-200125 | 参数无效 |
| yd.error.code.-200126 | 参数无效 |
| yd.error.code.-200127 | 地址簿内端口数量超出上限 |
| yd.error.code.-200128 | 地址簿端口错误，请检查输入 |
| yd.error.code.-200129 | 地址簿数量超出上限 |
| yd.error.code.-200130 | 地址簿数量超出上限 |
| yd.error.code.-200200 | 后台错误 |
| yd.error.code.-200201 | 后台错误 |
| yd.error.code.-200202 | 后台错误 |
| yd.error.code.-200203 | 后台错误 |
| yd.error.code.-200300 | 后台错误 |

| yd.error.code.-200301 | 后台错误 |
|---|---|
| yd.error.code.-200302 | 后台错误 |
| yd.error.code.-200400 | 未知错误 |
| yd.error.code.-200500 | API调用错误 |
| yd.error.code.200 | 请求成功 |
| yd.error.code.-210100 | 请求方式错误 |
| yd.error.code.-210101 | 认证失败 |
| yd.error.code.-210102 | 本地调用错误 |
| yd.error.code.-210103 | 参数错误，请重试 |
| yd.error.code.-210104 | uid错误，请重试 |
| yd.error.code.-210105 | 分页错误，请重试 |
| yd.error.code.-210106 | 参数错误，请重试 |
| yd.error.code.-210107 | 参数错误，请重试 |
| yd.error.code.-210108 | 参数错误，请重试 |
| yd.error.code.-210109 | 参数错误，请重试 |
| yd.error.code.-210110 | 参数错误，请重试 |
| yd.error.code.-210111 | 参数错误，请重试 |
| yd.error.code.-210200 | 后台错误 |
| yd.error.code.-210201 | 后台错误 |
| yd.error.code.-210202 | 后台错误 |
| yd.error.code.-210203 | 后台错误 |
| yd.error.code.-210300 | 后台错误 |
| yd.error.code.-210301 | 后台错误 |
| yd.error.code.-210302 | 请求错误，请稍后重试 |
| yd.error.code.-210400 | 请求错误，请稍后重试 |
| yd.error.code.200 | 成功 |
| yd.error.code.-230100 | 请求方法错误 |
| yd.error.code.-230101 | 认证失败 |
| yd.error.code.-230102 | 本地请求失败 |

| yd.error.code.-230103 | 接口认证失败 |
|---|---|
| yd.error.code.-230104 | 参数失败 |
| yd.error.code.-230105 | 策略模板已存在 |
| yd.error.code.-230106 | 策略模板不存在 |
| yd.error.code.-230107 | 用户ID错误 |
| yd.error.code.-230108 | 安全组ID错误 |
| yd.error.code.-230109 | 安全组ID错误 |
| yd.error.code.-230110 | 规则方向错误 |
| yd.error.code.-230111 | IP协议错误 |
| yd.error.code.-230112 | 规则策略错误 |
| yd.error.code.-230113 | 策略优先级错误，请重新输入 |
| yd.error.code.-230114 | 策略端口错误，请重新输入 |
| yd.error.code.-230115 | 网段地址错误，请重新输入 |
| yd.error.code.-230116 | 描述内容错误，请重新输入 |
| yd.error.code.-230117 | 策略已存在 |
| yd.error.code.-230118 | 策略不存在 |
| yd.error.code.-230119 | 规则ID错误 |
| yd.error.code.-230120 | 策略数超过规格限制，请排查删除多余的策略 |
| yd.error.code.-230121 | 分页错误 |
| yd.error.code.-230122 | 规则发布中，请稍后重试 |
| yd.error.code.-230123 | 提交状态错误 |
| yd.error.code.-230124 | 策略组回退 |
| yd.error.code.-230125 | 提交信息错误 |
| yd.error.code.-230126 | 没有规则变化，不需要发布 |
| yd.error.code.-230127 | 安全组ID错误 |
| yd.error.code.-230128 | 规则地址铺错误 |
| yd.error.code.-230129 | 规则的网络类型错误，请重选 |
| yd.error.code.-230130 | 规则操作错误 |
| yd.error.code.-230131 | 策略不支持提交 |

| yd.error.code.-230150 | 策略组不存在，请重选 |
|---|---|
| yd.error.code.-230151 | 策略组超出限制 |
| yd.error.code.-230152 | 策略组不允许修改 |
| yd.error.code.-230153 | 策略组前置 |
| yd.error.code.-230154 | 规则ID不合法 |
| yd.error.code.-230200 | 后台错误 |
| yd.error.code.-230300 | 后台错误 |
| yd.error.code.-230301 | 后台错误 |
| yd.error.code.-230302 | 后台错误 |
| yd.error.code.-230400 | 未知错误 |

**流量安全监控**

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| ErrorNeedLogin.-210204 | need login（未登录） | 未登录，需要进行登录后访问。 |
| ErrorAuthentication.-210101 | authentication error（身份验证错误） | 身份验证错误，请使用正确的角色登录访问。 |
| ErrorParametersAliUid.-210902 | invalid AliUid（无效AliUid参数） | AliUid参数无效，需要传入正确的 AliUid。 |
| ErrorParametersIpType.-210920 | invalid para ip type（无效的IP类型参数） | ipType参数无效，需要传入有效的 ipType。 |
| ErrorParametersSrcIP.-210919 | invalid para src ip（无效的源IP参数） | SrcIP参数无效，需要传入有效的 SrcIP。 |
| ErrorParametersDstIP.-210921 | invalid para dst ip（无效的目的IP 参数） | dstIP参数无效，需要传入有效的 dstIP。 |
| ErrorParametersPort.-210208 | invalid port, must 0~65535（无效的端口，端口范围0~65535） | 无效的端口参数，端口范围 0~65535。 |
| ErrorParametersLiveTime.- 210922 | invalid para live time（无效的 liveTime参数） | liveTime参数无效，需要传入有效的liveTime。 |
| ErrorDBInsert.-210122 | internal error: sql insert（内部错误:sql insert发生错误） | 内部错误：sql insert发生错误。 |
| ErrorInnerUuid.-210606 | internal error: uuid list is 0（内部错误：UUID列表为空） | 内部错误：UUID列表为空。 |
| ErrorDBSelect.-210124 | internal error: sql select（内部错误:sql select发生错误） | 内部错误:sql select发生错误。 |
| ErrorParasAddressCidrFeild.- 210915 | paras addressCidrList filed （重置addressCidrList规则失败） | 重置addressCidrList规则失败。 |

| ErrorPortAddressGroup.-210303 | get port in address group failed（在群组中获取prot失败） | 在群组中获取prot失败。 |
|---|---|---|
| ErrorPortAddressGroup.-210303 | get port in address group failed（在群组中获取prot失败） | 在群组中获取prot失败。 |
| ErrorSourceAddressGroup.- 210304 | get source address in address group failed（在群组中获取源地址失败） | 在群组中获取源地址失败。 |
| ErrorSourceAddressRange.- 210306 | source address range error, must be like \"192.168.XX.XX/192.168.XX.X X\"（源地址范围错误，举例： \"192.168.XX.XX/192.168.XX.X X\"） | 源地址范围错误，举例： \"192.168.XX.XX/192.168.XX.X X\"。 |
| ErrorDestAddressGroup.- 210305 | get dest address in address group failed（在群组中获取目的地址失败） | 在群组中获取目的地址失败。 |
| ErrorNoBeaverRules.-210226 | no beaver rules for online（没有对应的beaver rules） | 没有对应的beaver rules。 |
| ErrorDBUpdate.-210121 | internal error: sql update（内部错误：sql update发生错误） | 内部错误：sql update发生错误。 |
| ErrorDBDelete.-210123 | internal error: sql delete（内部错误：sql delete发生错误） | 内部错误：sql delete发生错误。 |
| ErrorMarshalJSON.-210125 | internal error: marshal json（内部错误：marshal json发生错误） | 内部错误：marshal json发生错误。 |
