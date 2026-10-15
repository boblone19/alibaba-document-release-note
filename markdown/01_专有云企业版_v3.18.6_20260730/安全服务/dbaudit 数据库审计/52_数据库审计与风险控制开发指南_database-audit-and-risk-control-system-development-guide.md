---
title: "数据库审计 数据库审计与风险控制开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 222
source_pdf: "52_数据库审计与风险控制开发指南_database-audit-and-risk-control-system-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/dbaudit/zh/database-audit-and-risk-control-system-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 数据库审计 数据库审计与风险控制开发指南

入门

## 快速入门

本文介绍功能的接口调用信息。

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
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrga nizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListRe sourceGroup章节。 入门

|  | 说明调用API时，请在Header参数中增加组织ID <x-acs-organizationid> 和资源集ID <x-acs- resourcegroupid>， 指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID <x-acs-organizationid> ，则默认获取当前用户所属的组织。 不指定资源集ID <x-acs-resourcegroupid> ，则默认为空，如果指定资源集需要同时指定组织ID。 |  |  |
|---|---|---|---|
|  |  | <x-acs- |  |

4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。

### 开发文档使用说明

本文为您介绍在使用专有云API进行开发工作时，如何查看所需要的产品文档。

**使用流程**

您可以按照以下流程图中步骤，判断自己所需要使用的开发文档。

**前提条件**

通过运维人员或运营管理员获取专有云的版本。

**操作步骤**

您可以通过阿里云专有云文档中心，获取需要的产品文档。
1. 通过浏览器打开专有云文档中心。
2. 根据专有云的版本单击**企业版**、**敏捷版**或**一体机**标签。
入门
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。
工作

## 准备工作

### 登录开发者门户控制台

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

通过POP网关调用API需要您了解产品开放API接口的相关信息，本文为您介绍获取云产品的Endpoint的两种方式。

**背景信息**

工作为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

**说明**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南为准。

**操作步骤**

**通过开发者门户获取Endpoint**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

**通过飞天基础运维平台获取Endpoint**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。 您也可以自行获取Endpoint，本文以API网关为例为您介绍获取云产品业务域Endpoint的方法。
1. 登录Apsara Uni-manager运维控制台。
2. 顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务注册变量大盘**。
4. 在服务注册变量大盘页面，单击**高级筛选**。
工作
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
apigateway.openapi.endpoint值，即 `Endpoint` 。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey。使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

工作

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。

**说明**

Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及Security Token三元组组成，使用STS方式调用云产品API时，三元组缺一不可。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。
工作

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourAccessKeyID>：请替换为您实际的AccessKey ID。 <yourAccessKeySecret>：请替换为您实际的AccessKey Secret。 <yourRoleSessionName>：请替换为您当前实际的会话名称。 该名称为用户自定义，通常设置为调用该API的用户身份，例如：用户名。在同一个RAM角色执行的操作中，可以根据不同的 `RoleSessionName` 来区分实际操作者，以实现用户级别的访问审计。长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-）和下划线（_）。 <yourRoleArn>：请替换为您实际的RAM Role。 "sts.aliyuns.com" ：请替换为实际的STS Endpoint。 工作

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
工作

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

工作

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

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以ECS为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**弹性计算**>**云服务器****ECS**。
3. 在左侧导航栏中，单击**实例**。
4. 在实例列表中查看**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。 工作

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

示例

## 调用示例

### Java SDK调用示例

#### 快速开始

本节介绍如何获取产品名Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体信息，请参见获取AccessKey，并在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。 获取Endpoint，具体操作，请参见获取Endpoint。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用云盾的开发工具包，必须安装SDK核心库。其中，SDK核心库推荐使用4.5.17及以上版本。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your-region-id>，请替换为您实际的地域ID。 <your-access-key-id>，请替换为您实际的AccessKey ID。 <your-access-key-secret>>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您当前产品实际的Endpoint。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。 示例

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

阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用云盾的开发工具包，必须安装阿里云Java SDK核心库。SDK核心库推荐使用4.5.17及以上版本。 您在安装阿里云Java SDK核心库时，需要在pom.xml文件中添加以下依赖。关于准确的SDK版本号，请参见阿里云开发工具包（SDK）。 示例

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 设置身份验证凭证

目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留

##### 请求连接配置

您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <readTimeout>，请您根据自身服务的能力，配置读取超时时间，单位为毫秒（ms）。 <connectionTimeout>，请您根据自身服务的能力，配置连接超时时间，单位为毫秒 （ms）。 <maxRequestsPerHost>，请您根据自身服务的能力，配置每台服务器的最大请求数，数据类型为INT。 <maxRequests>，请您根据自身服务的能力，配置最大请求数，数据类型为INT。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。 示例 `//` 获取`HttpClientConfig`对象

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

##### 发起调用

本文介绍如何使用产品名Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例如DescribeInstances。 在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。

```
DescribeInstancesRequest request = new DescribeInstancesRequest();
```

`//` 业务参数

```
request.setPageSize(10); request.setPageNumber(1);
```

`//` 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用

```
request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "");
```

3. 发起调用并处理应答。
示例

```java
DescribeInstancesResponse response; try {
    response = client.getAcsResponse(request);
    for (DescribeInstancesResponse.Instance instance:response.getInstances()) {
        System.out.println(instance.getPublicIpAddress());
    }
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
}
```

正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 `response.getXXX()` 来获得应答中的字段。

```
instanceStatus := response.getStatus()
```

如果出现了异常，或您需要原始HTTP应答的情况下，您可以通过以使用 `doAction()` 来获取原始应答。

```
HttpResponse response = client.doAction(request);
```

##### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码： 示例

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

##### 使用CommonRequest进行调用

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

`//` 忽略`SSL` 示例 `//`忽略`SS`

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

示例 ROA调用，示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
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

`//` 非必填,资源集`ID` t `tH` `dP` t

```
(" id"
```

`"<`

```
id>")
```

示例

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

### Python SDK调用示例

#### 快速开始

本节介绍如何获取Python SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体信息， 获取到Endpoint。具体操作，请参见获取Endpoint。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

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
示例
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your_region_id>，请替换为您实际的地域ID。 <your_access_key_id>，请替换为您实际的AccessKey ID。 <your_access_key_secret>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您实际的产品访问地址。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest()
```

`request.set_domain('<your-endpoint>')//` 当前产品的服务地址

```bash
request.set_version('<API-version>')// 接口的版本 request.set_action_name('<your-action>')// 接口的名称
# or:
# request =
CommonRequest(domain='<your-endpoint>', version='<API-version>', action_name='<your-action>') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

#### 使用手册

##### 安装Python SDK

本文档介绍如何安装及调用Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。

**说明**

使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用ECS的Python SDK，您需要安装阿里云Python SDK核心库和ECS的Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

示例如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

安装云产品的SDK，以下以安装ECS的SDK为例。 如果您使用的是Python 2.x，执行以下命令，安装ECS的SDK：

```
pip install aliyun-python-sdk-ecs
```

如果您使用的是Python 3.x，执行以下命令，安装ECS的SDK：

```
pip3 install aliyun-python-sdk-ecs
```

##### 安装Python SDK

本文档介绍如何安装及调用Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。

**说明**

使用产品的开发工具包，都必须安装阿里云Python SDK核心库。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

##### 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**重要**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

##### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。 示例

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

##### 发起调用

本节介绍如何使用Python SDK发起请求。

**操作步骤**

1. 导入相关产品的SDK。

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
```

2. 新建一个AcsClient。

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. 创建Request对象。

```
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json')
```

4. 发起调用并处理返回。
示例

```
response = clt.do_action_with_exception(request) print response
```

##### 错误处理

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

##### 使用CommonRequest进行调用

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
from aliyunsdkcore.client import AcsClient import os
```

示例

```
from aliyunsdkcore.request import CommonRequest
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

示例

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

示例

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

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体信息， 请参见获取AccessKey，并在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。 获取到Endpoint。具体操作，请参见获取Endpoint。

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

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your_region_id>，请替换为您实际的地域ID。 <your_access_key_id>，请替换为您实际的AccessKey ID。 <your_access_key_secret>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您实际的产品访问地址。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。 示例

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

##### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。

**重要**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的阿里云账号的信息安全。 以下代码以ECS为例，展示初始化ecsClient实例。 示例 `//` 初始化`ecsClient`实例

```
ecsClient, err := ecs.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

##### 发起调用

本文介绍如何使用阿里云产品名Go SDK发起调用。 以下步骤以ECS为例，展示使用ECS Go SDK发起调用。
1. 导入云产品SDK。

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/ecs
```

2. 新建一个产品名Client，该client中包含产品名的所有API。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 `ecsClient,err := <ecs>.NewClientWithAccessKey( //`请替换为您实际的产品名称 `"<yourRegionID>", //` 请替换为您实际的`RegionID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>") //` 请替换为您实际的`AccessKeySecret` `ecsClient.Domain = "ecs.aliyuns.com" //`设置请求域名地址，当前为示例值，请求根据实际请求地址替换。
3. 使用 `xxx.CreateXXXRequest` 方法创建一个请求。
该方法的命名规范为 ${service}.Create${apiName}Request ，其中：
**${service}**为产品名称(小写)。例如ecs。
**${apiName}**为API名称，例如DescribeInstances。

```
request := ecs.CreateDescribeInstanceAttributeRequest() request.InstanceId = ""
```

4. 发起调用。

```
response, err := ecsClient.DescribeInstanceAttribute(request)
```

##### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

示例您可以通过以下代码来简单处理错误。

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个 `ClientError` 。 以下以ECS为例，您可以通过以下代码来判断并获取 `ClientError` 中的错误信息：

**重要**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-` `go/sdk/errors` ，引入方法请参考：

```java
package main import (
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
response, err := ecsClient.DescribeInstances(request) if clientError, ok := err.(*errors.ClientError); ok{
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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以ECS为例，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息： 示例

**重要**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-` `go/sdk/errors` ，引入方法请参考：

```java
package main import (
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
response, err := ecsClient.DescribeInstances(request) if serverError, ok := err.(*errors.ServerError); ok{
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

##### 使用CommonRequest进行调用

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **API****调试**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 示例代码如下： 示例

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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 示例

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

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 示例

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

公共参数

## API公共参数

**公共请求参数**

公共请求参数是每个接口调用都需要提供的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | Strin g | 否 | 返回值的类型，仅支持JSON。 |
| Version | Strin g | 是 | API版本号，以日期形式YYYY-MM-DD输入，取值： Auditprivate：2018-01-16。 yundunnextsoc：2019-07-23。 Sas：2018-12-03。 aegis：2016-11-11。 yundun-css：2021-10-11。 secspy：2019-08-05。 Ddosprivate：2018-01-16。 hsm-private：2018-06-30。 Cloudfw：2017-12-07。 Sddp：2019-01-03。 semawaf：2020-07-01。 soar：2018-12-03。 |
| AccessKeyId | Strin g | 是 | 访问服务使用的密钥ID。 |
| AccessKeySe cret | Strin g | 是 | 访问服务使用的密钥值。 |
| RegionId | Strin g | 是 | 服务所使用的地域ID。 |

公共参数

| Product | Strin g | 是 | 接口对应的产品名称。取值： Auditprivate：云盾基础组件。 yundunnextsoc：云安全管理中心（SOC）。 Sas：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy：网络流量检测与响应。 Ddosprivate：DDos 清洗。 hsm-private：加密服务。 Cloudfw：云防火墙。 Sddp：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |
|---|---|---|---|
| EndpointPre | Strin g | 是 | 接口对应的域名前缀。取值： auditprivate：云盾基础组件。 yundunnextsoc-pop：云安全管理中心（SOC）。 tds：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy-share：网络流量检测与响应。 ddosprivate：DDos 清洗。 hsmprivate：加密服务。 cloudfw：云防火墙。 sddp-api：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

## 数据库审计与风险控制系统

### 审计代理

#### agent代理

##### 获取agent列表

**基本信息**

ID：DescribeAgents URL：/DescribeAgents.json Method：GET

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| Sort | Enum | 排序列的名称 | 否 | 取值：见sort字段的枚举值列表默认值：agentIp |
| Dir | Enum | 排序方式 | 否 | 默认值：desc |
| CurrentPage | Int | 首条记录的偏移量 | 否 | 默认值：0 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| AgentIp | String | 查询条件agentIP | 否 | 默认值：空字符串 |
| AgentState | Strint | 查询条件agent状态 | 否 | 默认值：空字符串 |
| TagIdList | String | agent标签ID | 否 | 标签ID列表 |
| AssetIdList | String | 资产ID集合 | 否 | 资产ID列表 |

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|

| agentIp | aegnt的IP |
|---|---|
| agentState | agent状态 |
| createTime | 创建时间 |
| agentVersion | 版本信息 |
| systemType | 系统类型 |

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |
| asc | 升序 |

返回数据

| key | 类型 | 描述 |
|---|---|---|
| Agents | array | agent列表 |
| AgentIp | String | agent的IP |
| ConfigJson | String | agent配置的JSON |
| AgentState | Integer | agent的状态 |
| UpgradeState | Integer | 更新时间 |
| AgentVersion | null | 版本 |
| SystemType | null | 操作系统 |
| CreateTime | String | agent首次连接时间（yyyy-MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为 null） |

| LastReceiveTime | String | agent上次收包时间（yyyy-MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为 null） |
|---|---|---|
| ConnectionTime | String | agent本次连接上来的时间（yyyy- MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为null） |
| AgentFlow | String | agent当前流量（单位Mb）（如果状态为已停止或已挂起或连接异常， 此字段为null） |
| AgentCpu | String | agent的CPU百分比（0到100的小数，单位%)（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| SysCpu | String | 系统当前CPU百分比（0到100的小数，单位%)（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| AgentMem | String | agent内存百分比（0到100的小数，单位%）（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| SysMem | String | 系统的内存百分比（0到100的小数，单位%）（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| DropPackets | String | agent当前丢包数量 |
| SampleTime | String | 实时信息采样时间(yyyy-MM-dd HH:mm:ss) |
| SysReadIO | String | 系统IO读速度 |
| SysWriteIO | String | 系统IO写速度 |
| AgentReadIO | String | agent的IO读速度 |
| AgentWriteIO | String | agent的IO写速度 |

| TagList | array | agent的标签 |
|---|---|---|
| AgentAssetIdList | String | agent的关联资产 |
| TotalCount | Integer | agent的总数 |

##### 下载agent

**基本信息**

ID：DescribeAgentPkg Method：GET URL：/DescribeAgentPkg.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| Platform | Enum | 平台 | 是 | 操作系统类型 |
| RevIp | String | 接收流量的服务器 IP | 是 | 数据库审计系统接收流量的IP |

platform字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| linux | Linux |
| win | Windows |
| arm | ARM |
| aix5.3 | AIX 5.3 |
| aix6.1 | AIX 6.1 |
| aix7.1 | AIX 7.1 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Url | String | agent下载链接 |

##### 添加agent安装任务

**基本信息**

ID：CreateAgentInstallTask URL：/CreateAgentInstallTask.json Method：POST

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| HostConfig | Array<Object> | 安装agent的服务器信息 | 是 | 安装agent的服务器信息 |
| HostIp | Ip | 服务器IP | 是 | 安装agent的服务器 IP |
| RootPasswd | String | 服务器root密码 | 是 | 安装agent的服务器 root账号密码 |
| sshPort | Portx | SSH端口号 | 是 | SSH端口号 |
| serverIp | Ipdomain | agent的接收端IP | 否 | 默认值：空字符串 |

**返回数据**

无返回数据

**错误码**

| code | 说明 |
|---|---|
| appErr.agent.package | agent打包失败 |

**示例**

**失败返回示例**

请求（双大括号包含部分为变量，在postman中可以通过环境变量预先设置）

```bash
curl -X POST '{{host}}/dbaudit/agents/installTasks' -d 'requestId= {{requestId}}&version={{version}}&clusterKey={{clusterKey}}&clusterTime= {{clusterTime}}&clusterUuid={{clusterUuid}}&clusterSign={{clusterSign}}'
```

返回

```json
{
 "code": "appErr.agent.package",
 "success": false,
```

`"message": "agent`打包失败`",`

```json
 "requestId": "704f63c8-38d8-4907-a4d7-a761a8986b34",
 "requestTotalCost": 22
}
```

**成功返回示例**

请求（双大括号包含部分为变量，在postman中可以通过环境变量预先设置）

```bash
curl -X POST '{{host}}/dbaudit/agents/installTasks' -d 'requestId= {{requestId}}&version={{version}}&clusterKey={{clusterKey}}&clusterTime= {{clusterTime}}&clusterUuid={{clusterUuid}}&clusterSign={{clusterSign}}'
```

返回

```json
{
 "code": "200",
 "message": "success",
 "success": true,
 "requestId": "3d77a658-3626-4a79-bd60-1ddb85722b47",
 "requestTotalCost": 493
}
```

##### 添加agent卸载任务

**基本信息**

ID：CreateAgentUninstallTask URL：/CreateAgentUninstallTask.json Method：POST

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| HostConfig | Array<Object> | 卸载Agent的服务器信息 | 是 | 卸载agent的服务器信息 |

| hostIp | Ip | 服务器IP | 是 | 卸载agent的服务器 IP |
|---|---|---|---|---|
| rootPasswd | String? | 服务器root账号的密码 | 是 | 卸载agent的服务器 root账号的密码 |
| sshPort | Portx | SSH端口号 | 是 | SSH端口号 |

**返回数据**

无返回数据

##### 修改agent配置

**基本信息**

ID：ModifyAgentConfig URL：/ModifyAgentConfig.json Method：POST

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AgentIp | String | AgentIP | 是 | agent的地址 |
| ConfigJson | String | Agent的配置信息 | 是 | agent的配置信息 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | array | 批量修改配置的agent列表 |
| AgentIp | String | agent的IP |
| ConfigJson | String | agent配置 |
| AgentState | Integer | agent的状态 |
| UpgradeState | Integer | 升级状态 |

| AgentVersion | String | 版本 |
|---|---|---|
| SystemType | String | 系统类型 |
| CreateTime | String | agent首次连接时间（yyyy-MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为 null） |
| LastReceiveTime | String | agent上次收包时间（yyyy-MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为 null） |
| ConnectionTime | String | agent本次连接上来的时间（yyyy- MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为null） |
| Flow | String | agent当前流量（单位Mb）（如果状态为已停止或已挂起或连接异常， 此字段为null） |
| AgentCpu | String | agent的CPU百分比（0到100的小数，单位%)（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| SysCpu | String | 系统当前CPU百分比（0到100的小数，单位%)（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| AgentMem | String | agent内存百分比（0到100的小数，单位%）（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| SysMem | String | 系统的内存百分比（0到100的小数，单位%）（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| DropPackets | String | agent当前丢包数量 |
| SampleTime | String | 实时信息采样时间(yyyy-MM-dd HH:mm:ss) |

| SysReadIO | String | 系统IO读速度 |
|---|---|---|
| SysWriteIO | String | 系统IO写速度 |
| AgentReadIO | String | agent的IO读速度 |
| AgentWriteIO | String | agent的IO写速度 |
| SupportFrontEndStart | null |  |

##### 修改agent状态

**基本信息**

ID：ModifyAgentState URL：/ModifyAgentState.json Method：POST

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AgentIp | String | agentIp | 是 | agent的地址 |
| AgentState | Strint | agent状态 | 是 | agent的状态 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | array | 删除列表 |
| AgentIp | String | agent的IP |
| ConfigJson | String | agent配置 |
| AgentState | Integer | agent的状态 |
| UpgradeState | Integer | 升级状态 |

| AgentVersion | String | 版本 |
|---|---|---|
| SystemType | String | 系统类型 |
| CreateTime | String | agent首次连接时间（yyyy-MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为 null） |
| LastReceiveTime | String | agent上次收包时间（yyyy-MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为 null） |
| ConnectionTime | String | agent本次连接上来的时间（yyyy- MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为null） |
| Flow | String | agent当前流量（单位Mb）（如果状态为已停止或已挂起或连接异常， 此字段为null） |
| AgentCpu | String | agent的CPU百分比（0到100的小数，单位%)（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| SysCpu | String | 系统当前CPU百分比（0到100的小数，单位%)（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| AgentMem | String | agent内存百分比（0到100的小数，单位%）（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| SysMem | String | 系统的内存百分比（0到100的小数，单位%）（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| DropPackets | String | agent当前丢包数量 |

| SampleTime | String | 实时信息采样时间(yyyy-MM-dd HH:mm:ss) |
|---|---|---|
| SysReadIO | String | 系统IO读速度 |
| SysWriteIO | String | 系统IO写速度 |
| AgentReadIO | String | agent的IO读速度 |
| AgentWriteIO | String | agent的IO写速度 |
| SupportFrontEndStart | null |  |

##### 获取agent日志

**基本信息**

ID：DescribeAgentsLog Method：GET URL：/DescribeAgentsLog.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AgentIp | String | agent地址 | 是 | 服务器连接数据库审计系统用的地址 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Url | String | agent日志保存文件访问链接 |

**错误码**

| code | 说明 |
|---|---|
| appErr.agent.noLogFile | 无此agent的日志 |

##### 删除agent

**基本信息**

ID：DeleteAgents Method：POST URL：/DeleteAgents.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AgentIp | Ips | agentIp | 是 | 安装agent服务器和数据库审计系统通信的地址 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | array | 删除列表 |
| AgentIp | String | agent的IP |
| ConfigJson | String | agent配置 |
| AgentState | Integer | agent的状态 |
| UpgradeState | Integer | 升级状态 |
| AgentVersion | String | 版本 |
| SystemType | String | 系统类型 |
| CreateTime | String | agent首次连接时间（yyyy-MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为 null） |
| LastReceiveTime | String | agent上次收包时间（yyyy-MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为 null） |

| ConnectionTime | String | agent本次连接上来的时间（yyyy- MM-dd HH:mm:ss）（如果状态为已停止或已挂起或连接异常，此字段为null） |
|---|---|---|
| Flow | String | agent当前流量（单位Mb）（如果状态为已停止或已挂起或连接异常， 此字段为null） |
| AgentCpu | String | agent的CPU百分比（0到100的小数，单位%)（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| SysCpu | String | 系统当前CPU百分比（0到100的小数，单位%)（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| AgentMem | String | agent内存百分比（0到100的小数，单位%）（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| SysMem | String | 系统的内存百分比（0到100的小数，单位%）（如果状态为已停止或已挂起或连接异常或未采集到数据， 此字段为null） |
| DropPackets | String | agent当前丢包数量 |
| SampleTime | String | 实时信息采样时间(yyyy-MM-dd HH:mm:ss) |
| SysReadIO | String | 系统IO读速度 |
| SysWriteIO | String | 系统IO写速度 |
| AgentReadIO | String | agent的IO读速度 |
| AgentWriteIO | String | agent的IO写速度 |
| SupportFrontEndStart | null |  |

##### 获取agent版本号

**基本信息**

ID：DescribeAgentVersion Method：GET URL：/DescribeAgentVersion.json

**请求参数**

无请求参数

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| AgentVersion | String | agent版本号 |

##### agent状态诊断

**基本信息**

ID：DescribeAgentStat Method：GET URL：/DescribeAgentStat.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AgentIp | String | AgentIP | 是 | 安装agent的服务器和数据库审计系统通信的地址 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| AgentIp | String | 安装agent的服务器和数据库审计系统通信的地址 |
| SelfCheckResult | String | 诊断结果 |

| SelfCheckState | Integer | 诊断状态 |
|---|---|---|

##### 下载agent

**基本信息**

ID：DownloadAgent URL：/dbagent/:filename Method：GET

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| revIp | String | 接收流量的IP | 是 | 数据库审计系统接收流量的地址 |

**返回数据**

无返回数据

##### 查询agent标签列表

**基本信息**

ID：DescribeAgentTag Method：GET URL：/DescribeAgentTag.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| CurrentPage | Int | 显示页页码 | 否 | 默认值：0 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| TagName | String | 标签名称 | 否 | 标签名称 |

**返回数据**

| 0 |  | > 文档版本：2026072 |
|---|---|---|

| key | 类型 | 描述 |
|---|---|---|
| List | array | 标签列表 |
| Id | String | 标签ID |
| TagName | String | 标签名称 |
| CreateTime | String | 创建时间 |
| UpdateTime | String | 更新时间 |
| Deleted | Integer |  |
| TotalCount | Integer | 标签总数 |

##### 更新单个agent的标签列表

**基本信息**

ID：UpdateTagRelate Method：POST URL：/UpdateTagRelate.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AgentIp | String | agent端的IP | 否 | 安装agent的服务器和数据库审计系统通信的地址 |
| TagIdList | String | 标签ID列表 | 否 | 标签ID列表 |

**返回数据**

无返回数据

##### 批量操作agent和标签关联

**基本信息**

ID：UpdateBatchOperateTag Method：POST URL：/UpdateBatchOperateTag.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AgentIpList | String | agentIP列表 | 是 | agent地址列表 |
| AddAgentTagIdLi st | String | 给agent加上标签 | 否 | 添加agent标签 |
| DelAgentTagIdLis t | String | 给agent去掉标签 | 否 | 删除agent标签 |

**返回数据**

无返回数据

##### 新增agent标签

**基本信息**

ID：CreateAgentTag URL：/CreateAgentTag.json Method：POST

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| TagName | String | 标签名称 | 是 | 标签名称 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| TagId | String | 标签ID |
| TagName | String | 标签名称 |
| CreateTime | String |  |

| UpdateTime | String |  |
|---|---|---|
| Deleted | null |  |

##### 修改agent标签

**基本信息**

ID：UpdateAgentTag Method：POST URL：/UpdateAgentTag.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| Id | String | 标签ID | 是 | 标签ID值 |
| TagName | String | 标签名称 | 是 | 标签的名称 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Id | String | 标签ID值 |
| TagName | String | 标签的名称 |
| CreateTime | null |  |
| UpdateTime | String | 更新时间 |
| Deleted | null |  |

##### 删除agent标签

**基本信息**

ID：DeleteAgentTag Method：POST URL：/DeleteAgentTag.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| TagIdList | String | 标签ID列表 | 是 | 标签ID列表 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | array | 删除标签列表 |
| Id | String | 标签ID |
| TagName | String | 标签名称 |
| CreateTime | String |  |
| UpdateTime | String |  |
| Deleted | Integer |  |

##### 卸载agent

**基本信息**

ID：DeleteNormalAgent URL：/DeleteNormalAgent.json Method：POST

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AgentIp | Ips | agentIp | 是 | 安装agent的服务器和数据库审计系统通信的地址 |

**返回数据**

无返回数据

### 数审数据库管理

#### 资产类型

##### 获取资产类型

**基本信息**

ID：DescribeAppTypes Method：GET URL：/DescribeAppTypes.json

**请求参数**

无请求参数

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| AppTypes | array | 所有资产类型 |
| AppTypeId | Integer | 类型ID |
| Groups | array | 类型所属的组ID |
| AppTypeName | String | 类型名称 |
| SaveName | String | 存储名称 |
| Twoway | Boolean | 是否双向审计 |
| SetRow | Boolean | 存储行数是否可配 |
| RequestJson | Boolean | 请求是否是JSON |
| ResponseJson | Boolean | 响应是否是JSON |
| Runat | array | 运行环境 |
| Versions | array | 支持的版本 |

| Encodes | array | 支持的编码 |
|---|---|---|

#### 数据库管理

##### 获取数据库列表信息

**基本信息**

ID：DescribeDatabases Method：GET URL：/DescribeDatabases.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 查询条件-ID | 否 | 默认值：空字符串 |
| Sort | Enum | 排序列的名称 | 否 | 取值：见sort字段的枚举值列表默认值： createTime |
| Dir | Enum | 排序方式 | 否 | 取值：见dir字段的枚举值列表默认值：desc |
| CurrentPage | Int | 页码 | 否 | 默认值：1 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| DbName | String | 查询条件-名称关键字 | 否 | 默认值：空字符串 |
| DbType | Enum(多选) | 查询条件-数据库类型 | 否 | 见type字段的枚举值列表 |
| Ip | String | 查询条件-IP | 否 | 默认值：空字符串 |
| DepartmentIds | Noxss | 查询条件-部门ID | 否 | 默认值：空字符串 |

| Extend | String | 查询拓展信息 | 否 | 默认值：空字符串 |
|---|---|---|---|---|

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| createTime | 创建时间 |
| name | 名称 |
| assetId | 资产ID |
| type | 资产类型 |
| lastActiveTime | 最后一次活跃时间 |

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |
| asc | 升序 |

DbType字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号隔开

| 枚举值 | 值描述 |
|---|---|
| 1 | Oracle |
| 2 | MySQL |
| 3 | SQL Server |
| 4 | Sybase ASE |
| 5 | DB2 |

| 6 | Informix |
|---|---|
| 7 | Oscar |
| 8 | 达梦(DM) |
| 9 | Cache |
| 10 | PostgreSQL |
| 12 | Teradata |
| 13 | 人大金仓(Kingbase) |
| 14 | GBase |
| 15 | MariaDB |
| 16 | HTTP |
| 17 | TELNET |
| 18 | FTP |
| 22 | Hana |
| 23 | MongoDB |
| 24 | HBase(protobuf) |
| 25 | HBase(thrift) |
| 26 | Hive |
| 27 | Redis |
| 28 | Elasticsearch |

| 29 | Cassandra |
|---|---|
| 30 | HDFS |
| 31 | Impala |
| 32 | GaussDB |
| 33 | LibrA |
| 34 | Graphbase |
| 35 | Greenplum |
| 36 | Spark SQL(thrift) |
| 37 | Spark SQL(RESTful) |
| 38 | SSDB |
| 40 | K-DB |
| 41 | Sybase IQ |
| 42 | ArangoDB |
| 43 | Neo4j |
| 44 | OrientDB |
| 46 | TiDB |
| 48 | Vertica |
| 49 | OceanBase |
| 50 | PolarDB |

| 51 | PolarDB-X |
|---|---|
| 52 | AnalyticDB |
| 55 | HTTPS |
| 56 | MaxCompute(ODPS) |
| 57 | TBase |
| 58 | HighGo |
| 59 | TDSQL-C MySQL |
| 60 | TDSQL-C PostgreSQL |
| 62 | Percona MySQL |
| 64 | Percona MongoDB |
| 65 | Vastbase |
| 68 | Clickhouse HTTP |
| 69 | Clickhouse MySQL |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Databases | array | 资产列表 |
| AssetId | String | 资产ID |
| Name | String | 资产名称 |
| Type | String | 协议类型 |

| Version | String | 协议版本 |
|---|---|---|
| Charset | String | 字符集 |
| Environment | String | 运行环境 |
| Twoway | String | 是否双向审计 |
| IsAudit | String | 是否启用审计 |
| SaveLine | String | 返回结果保存行数 |
| IpFilter | String |  |
| IpPort | String | 服务的IP和端口信息 |
| Internet | String |  |
| ConnInfo | Password | 连接数据库的账号密码信息 |
| CertInfo | Password | 加密证书信息 |
| ExtendInfo | String |  |
| CreateTime | String | 创建时间 |
| UpdateTime | String | 最后变更时间 |
| SaveSize | String | 最大保存长度 |
| DepartmentIds | String | 所属资产组的ID |
| IsFocused | dict yesOrNo _ | 是否关注 |
| AuditType | Integer | 审计方式 |
| ProjectSpace | String | 项目空间 |

| Instance | String | RDS实例 |
|---|---|---|
| Region | String | 地域(Region) |
| TypeGroup | String | 资产类型分组 |
| ActiveNodes | String | 节点最后活跃时间列表 |
| NodeIp | String | 日志采集配置所属节点IP |
| ConfigId | String | 日志采集配置ID |
| TotalCount | Integer | 总数 |

##### 添加数据库

**基本信息**

ID：CreateDatabase Method：POST URL：/CreateDatabase.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbName | ChsName | 数据库名称 | 是 | 数据库的名称 |
| DbVersion | String | 数据库版本 | 否 | 默认值：空字符串 |
| Environment | Noxss | 运行环境 | 否 | 默认值：空字符串 |
| Charset | Noxss | 编码 | 否 | 默认值：空字符串 |
| DbType | Enum | 数据库类型 | 是 | 数据库的类型 |
| SaveLine | Strint | 保存行数 | 否 | 默认值：0 |
| Twoway | Enum | 流量方向 | 否 | 默认值：0 |

| IsAudit | Enum | 状态 | 是 | 是否审计，默认值：1 |
|---|---|---|---|---|
| IpPorts | Array<Object> | IP与端口 | 否 | 数据库的IP和端口 |
| ip | Ipdomain |  | 是 |  |
| port | Portx |  | 是 |  |
| RdsInstanceId | Noxss | 实例ID | 否 | 实例ID信息 |
| Region | String | 地域(Region) | 否 | 地域信息 |
| TypeGroup | String | 资产类型分组 | 否 | 资产类型分组 |
| ConnInfo | Object | 连接数据库账号信息 | 否 | 默认值：{} |
| CertInfo | Object | 数据库加密证书信息 | 否 | 默认值：{} |
| DepartmentIds | Noxss | 所属部门ID | 否 | 默认值：空字符串 |
| SaveSize | Strint | 最大保存长度 | 否 | 默认值：64 |
| AuditType | Enum | 审计方式 | 否 | 默认值：1 |
| ProjectSpace | Array<String> | 项目空间 | 否 | 项目空间 |
| NodeIp | String | 日志采集配置所属节点IP | 否 | 日志采集配置所属节点IP |
| ConfigId | String | 日志采集配置ID | 否 | 日志采集配置ID |

Type字段Enum枚举值列表

| 枚举值 | 值描述 |
|---|---|
| 1 | Oracle |

| 2 | MySQL |
|---|---|
| 3 | SQL Server |
| 4 | Sybase ASE |
| 5 | DB2 |
| 6 | Informix |
| 7 | Oscar |
| 8 | 达梦(DM) |
| 9 | Cache |
| 10 | PostgreSQL |
| 12 | Teradata |
| 13 | 人大金仓(Kingbase) |
| 14 | GBase |
| 15 | MariaDB |
| 16 | HTTP |
| 17 | TELNET |
| 18 | FTP |
| 22 | Hana |
| 23 | MongoDB |
| 24 | HBase(protobuf) |

| 25 | HBase(thrift) |
|---|---|
| 26 | Hive |
| 27 | Redis |
| 28 | Elasticsearch |
| 29 | Cassandra |
| 30 | HDFS |
| 31 | Impala |
| 32 | GaussDB |
| 33 | LibrA |
| 34 | Graphbase |
| 35 | Greenplum |
| 36 | Spark SQL(thrift) |
| 37 | Spark SQL(RESTful) |
| 38 | SSDB |
| 40 | K-DB |
| 41 | Sybase IQ |
| 42 | ArangoDB |
| 43 | Neo4j |
| 44 | OrientDB |

| 46 | TiDB |
|---|---|
| 48 | Vertica |
| 49 | OceanBase |
| 50 | PolarDB |
| 51 | PolarDB-X |
| 52 | AnalyticDB |
| 55 | HTTPS |
| 56 | MaxCompute(ODPS) |
| 57 | TBase |
| 58 | HighGo |
| 59 | TDSQL-C MySQL |
| 60 | TDSQL-C PostgreSQL |
| 62 | Percona MySQL |
| 64 | Percona MongoDB |
| 65 | Vastbase |
| 68 | Clickhouse HTTP |
| 69 | Clickhouse MySQL |

twoway字段的枚举值

| 枚举值 | 值描述 |
|---|---|

| 0 | 单向审计 |
|---|---|
| 1 | 双向审计 |

isAudit的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

auditType的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | 解析流量 |
| 2 | 解析自审计日志 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| DbId | String | 资产ID |
| AssetName | String | 资产名称 |
| AssetType | String | 协议类型 |
| Version | String | 协议版本 |
| Charset | String | 字符集 |
| Environment | String | 运行环境 |
| Twoway | String | 是否双向审计 |
| IsAudit | String | 是否启用审计 |

| SaveLine | String | 返回结果保存行数 |
|---|---|---|
| SaveSize | String | 最大保存长度 |
| IpPort | String | 服务的IP和端口信息 |
| ConnInfo | Password | 连接数据库的账号密码信息 |
| CertInfo | Password | 加密证书信息 |
| CreateTime | String | 创建时间 |
| UpdateTime | String | 最后变更时间 |
| DepartmentIds | String | 所属资产组的ID |
| IsFocused | null | 是否关注 |
| NodeIp | String | 日志采集配置所属节点IP |
| ConfigId | String | 日志采集配置ID |

##### 更改数据库

**基本信息**

ID：ModifyDatabase Method：PUT URL：/ModifyDatabase.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuid | 数据库资产ID | 是 | 数据库资产ID |
| DbName | ChsName | 数据库名称 | 是 | 数据库名称 |
| DbVersion | String | 数据库版本 | 否 | 默认值：空字符串 |

| Environment | Noxss | 运行环境 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| Charset | Noxss | 编码 | 否 | 默认值：空字符串 |
| DbType | Enum | 数据库类型 | 是 | 数据库类型 |
| SaveLine | Strint | 保存行数 | 是 | 保存行数 |
| Twoway | Enum | 流量方向 | 否 | 默认值：0 |
| IsAudit | Enum | 状态 | 是 | 是否审计，默认值：1 |
| ipPorts | Array<Object> | IP与端口 | 否 | 数据库的IP和端口 |
| ip | Ipdomain |  | 是 |  |
| port | Portx |  | 是 |  |
| Instance | Noxss | 实例ID | 否 | 默认值：空字符串 |
| Region | String | 地域(Region) | 否 | 地域 |
| TypeGroup | String | 资产类型分组 | 否 | 资产类型分组 |
| ConnInfo | Object | 连接数据库账号信息 | 否 | 默认值：{} |
| CertInfo | Object | 数据库加密证书信息 | 否 | 默认值：{} |
| DepartmentIds | Noxss | 所属部门ID | 否 | 默认值：空字符串 |
| SaveSize | Strint | 最大保存长度 | 否 | 默认值：64 |
| AuditType | Enum | 审计方式 | 否 | 默认值：1 |
| ProjectSpace | Array<String> | 项目空间 | 否 | 项目空间 |

| NodeIp | String | 日志采集配置所属节点IP | 否 | 日志采集配置所属节点IP |
|---|---|---|---|---|
| ConfigId | String | 日志采集配置ID | 否 | 日志采集配置ID |

DbType字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | Oracle |
| 2 | MySQL |
| 3 | SQL Server |
| 4 | Sybase ASE |
| 5 | DB2 |
| 6 | Informix |
| 7 | Oscar |
| 8 | 达梦(DM) |
| 9 | Cache |
| 10 | PostgreSQL |
| 12 | Teradata |
| 13 | 人大金仓(Kingbase) |
| 14 | GBase |
| 15 | MariaDB |
| 16 | HTTP |

| 17 | TELNET |
|---|---|
| 18 | FTP |
| 22 | Hana |
| 23 | MongoDB |
| 24 | HBase(protobuf) |
| 25 | HBase(thrift) |
| 26 | Hive |
| 27 | Redis |
| 28 | Elasticsearch |
| 29 | Cassandra |
| 30 | HDFS |
| 31 | Impala |
| 32 | GaussDB |
| 33 | LibrA |
| 34 | Graphbase |
| 35 | Greenplum |
| 36 | Spark SQL(thrift) |
| 37 | Spark SQL(RESTful) |
| 38 | SSDB |

| 40 | K-DB |
|---|---|
| 41 | Sybase IQ |
| 42 | ArangoDB |
| 43 | Neo4j |
| 44 | OrientDB |
| 46 | TiDB |
| 48 | Vertica |
| 49 | OceanBase |
| 50 | PolarDB |
| 51 | PolarDB-X |
| 52 | AnalyticDB |
| 55 | HTTPS |
| 56 | MaxCompute(ODPS) |
| 57 | TBase |
| 58 | HighGo |
| 59 | TDSQL-C MySQL |
| 60 | TDSQL-C PostgreSQL |
| 62 | Percona MySQL |
| 64 | Percona MongoDB |

| 65 | Vastbase |
|---|---|
| 68 | Clickhouse HTTP |
| 69 | Clickhouse MySQL |

twoway字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 单向审计 |
| 1 | 双向审计 |

IsAudit字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

Audittype字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | 解析流量 |
| 2 | 解析自审计日志 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| DbId | String | 资产ID |
| AssetName | String | 资产名称 |
| AssetType | String | 协议类型 |

| Version | String | 协议版本 |
|---|---|---|
| Charset | String | 字符集 |
| Environment | String | 运行环境 |
| Twoway | String | 是否双向审计 |
| IsAudit | String | 是否启用审计 |
| SaveLine | String | 返回结果保存行数 |
| SaveSize | String | 最大保存长度 |
| IpPort | String | 服务的IP和端口信息 |
| ConnInfo | Password | 连接数据库的账号密码信息 |
| CertInfo | Password | 加密证书信息 |
| CreateTime | String | 创建时间 |
| UpdateTime | String | 最后变更时间 |
| DepartmentIds | String | 所属资产组的ID |
| IsFocused | null | 是否关注 |
| NodeIp | String | 日志采集配置所属节点IP |
| ConfigId | String | 日志采集配置ID |

**示例**

**成功返回示例**

请求（双大括号包含部分为变量，在postman中可以通过环境变量预先设置）

```bash
curl -X POST '{{host}}/dbaudit/databases' -d 'requestId={{requestId}}&version={{version }}&clusterKey={{clusterKey}}&clusterTime={{clusterTime}}&clusterUuid= {{clusterUuid}}&clusterSign={{clusterSign}}'
```

返回

```json
{
  "code": "200",
  "message": "success",
  "success": true,
  "data": {
    "assetId": "ff80808171955d3d01719a7630cd0002",
    "name": "12111111111",
    "type": "2",
    "version": "1.0",
    "charset": "",
    "environment": "",
    "twoway": "1",
    "isAudit": "1",
    "saveLine": "4",
    "saveSize": "33",
    "ipFilter": "",
    "ipPort": "[{\"ip\":\"10.16.80.1\",\"port\":\"3936\"}]",
    "internet": "",
    "connInfo": "{}",
    "certInfo": "{}",
    "extendInfo": "{}",
    "createTime": "2020-04-21 01:59:29",
    "updateTime": "2020-04-21 02:00:02",
    "departmentIds": "",
    "isFocused": null
  },
  "requestId": "9a06d139-5c05-41db-88d5-65635e5b5f57",
  "requestTotalCost": 266
}
```

##### 删除数据库

**基本信息**

ID：DeleteDatabase Method：POST URL：/DeleteDatabase.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 数据库资产ID | 是 | 数据库资产ID |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | array | 返回数据 |
| AssetId | String | 资产ID |
| Name | String | 资产名称 |
| Type | dict dbType _ | 资产类型 |
| Version | String | 协议版本 |
| Charset | String | 字符集 |
| Environment | String | 运行环境 |
| Twoway | String | 是否双向审计 |
| IsAudit | String | 是否启用审计 |
| SaveLine | String | 返回结果保存行数 |
| SaveSize | String | 最大保存长度 |
| IpFilter | String |  |
| IpPort | String | 服务的IP和端口信息 |
| Internet | String |  |
| ConnInfo | Password | 连接数据库的账号密码信息 |
| CertInfo | Password | 加密证书信息 |
| CreateTime | String | 创建时间 |
| UpdateTime | String | 最后变更时间 |

| SaveSize | String | 最大保存长度 |
|---|---|---|
| DepartmentIds | String | 所属资产组的ID |
| IsFocused | null | 是否关注 |
| NodeIp | String | 日志采集配置所属节点IP |
| ConfigId | String | 日志采集配置ID |
| Total | Integer |  |

##### 导入数据库

**基本信息**

ID：CreateImportAssets Method：POST URL：/CreateImportAssets.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| FileId | FileId | 文件ID | 是 | 文件ID |

**返回数据**

无返回数据

##### 导出数据库

**基本信息**

ID：DescribeExportAssets Method：GET URL：/DescribeExportAssets.json

**请求参数**

无请求参数

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| DownLoadUrl | String | 下载URL |

##### 下载资产信息模板

**基本信息**

ID：DescribeAssetsTemplate Method：GET URL：/DescribeAssetsTemplate.json

**请求参数**

无请求参数

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| DownLoadUrl | String | 下载URL |

##### 修改数据库状态

**基本信息**

ID：ModifyDatabaseEnable Method：POST URL：/ModifyDatabaseEnable.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 查询条件-ID | 否 | 默认值：空字符串 |
| DbName | String | 查询条件-名称关键字 | 否 | 默认值：空字符串 |
| DbType | Enum | 查询条件-数据库类型 | 否 | 数据库类型 |

| Ip | String | 查询条件-IP | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| DepartmentIds | Noxss | 查询条件-部门ID | 否 | 默认值：空字符串 |
| IsAudit | Enum | 状态 | 是 | 是否审计，默认值：1 |

DbType字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | Oracle |
| 2 | MySQL |
| 3 | SQL Server |
| 4 | Sybase ASE |
| 5 | DB2 |
| 6 | Informix |
| 7 | Oscar |
| 8 | 达梦(DM) |
| 9 | Cache |
| 10 | PostgreSQL |
| 12 | Teradata |
| 13 | 人大金仓(Kingbase) |
| 14 | GBase |
| 15 | MariaDB |

| 16 | HTTP |
|---|---|
| 17 | TELNET |
| 18 | FTP |
| 22 | Hana |
| 23 | MongoDB |
| 24 | HBase(protobuf) |
| 25 | HBase(thrift) |
| 26 | Hive |
| 27 | Redis |
| 28 | Elasticsearch |
| 29 | Cassandra |
| 30 | HDFS |
| 31 | Impala |
| 32 | GaussDB |
| 33 | LibrA |
| 34 | Graphbase |
| 35 | Greenplum |
| 36 | Spark SQL(thrift) |
| 37 | Spark SQL(RESTful) |

| 38 | SSDB |
|---|---|
| 40 | K-DB |
| 41 | Sybase IQ |
| 42 | ArangoDB |
| 43 | Neo4j |
| 44 | OrientDB |
| 46 | TiDB |
| 48 | Vertica |
| 49 | OceanBase |
| 50 | PolarDB |
| 51 | PolarDB-X |
| 52 | AnalyticDB |
| 55 | HTTPS |
| 56 | MaxCompute(ODPS) |
| 57 | TBase |
| 58 | HighGo |
| 59 | TDSQL-C MySQL |
| 60 | TDSQL-C PostgreSQL |
| 62 | Percona MySQL |

| 64 | Percona MongoDB |
|---|---|
| 65 | Vastbase |
| 68 | Clickhouse HTTP |
| 69 | Clickhouse MySQL |

IsAudit字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

**返回数据**

无返回数据

##### 查询资产最后活跃时间

**基本信息**

ID：DescribeLastActiveTime Method：GET URL：/DescribeLastActiveTime.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetId | String | 数据库资产ID | 是 | 数据库资产ID |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| AssetId | String | 资产ID |
| Name | String | 资产名称 |

| Type | String |  |
|---|---|---|
| Version | String |  |
| Charset | String |  |
| Environment | String |  |
| Twoway | String |  |
| IsAudit | String |  |
| SaveLine | String |  |
| IpFilter | String |  |
| IpPort | String |  |
| Internet | String |  |
| ConnInfo | String |  |
| CertInfo | String |  |
| ExtendInfo | String |  |
| CreateTime | String |  |
| UpdateTime | String |  |
| SaveSize | String |  |
| DepartmentIds | String |  |
| IsFocused | null |  |
| Active | Integer |  |

| LastActiveTime | String | 最后活跃名称 |
|---|---|---|
| NodeName | String |  |

##### 查询资产离线阈值配置

**基本信息**

ID：DescribeAssetActiveConfig Method：GET URL：/DescribeAssetActiveConfig.json

**请求参数**

无请求参数

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| AssetActiveTime | Integer | 资产活跃阈值 |

##### 修改资产离线阈值配置

**基本信息**

ID：UpdateAssetActiveConfig Method：POST URL：/UpdateAssetActiveConfig.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetActiveTime | Int | 资产离线阈值 | 是 | 资产离线阈值 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| AssetActiveTime | Integer | 资产活跃阈值 |

#### 资产组管理

##### 获取资产组列表

**基本信息**

ID：DescribeDepartmentList Method：GET URL：/DescribeDepartmentList.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| Sort | Enum | 排序列的名称 | 否 | 取值：createTime、 id、name、desc 默认值：createTime |
| Dir | Enum | 排序方式 | 否 | 默认值：desc |
| CurrentPage | Int | 显示页页码 | 否 | 默认值：1 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| Name | String | 资产组名称 | 否 | 默认值：空字符串 |
| Desc | String | 资产组描述 | 否 | 默认值：空字符串 |
| Id | Noxss | 资产组ID | 否 | 默认值：空字符串 |

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| createTime | 创建资产组的时间 |
| id | 资产组ID信息 |
| name | 资产组的名称 |

| desc | 降序排序 |
|---|---|

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |
| asc | 升序 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| List | array | 资产组列表 |
| DepartmentId | String | 资产组ID |
| DepartmentName | String | 资产组名称 |
| Desc | String | 描述 |
| ParentId | String |  |
| Path | null |  |
| CreateTime | Integer | 创建时间 |
| AssetIds | String |  |
| Assets | null |  |
| RuleIds | null |  |
| Priority | null |  |
| TotalCount | Integer | 资产组总数 |

##### 编辑资产组

**基本信息**

ID：ModifyDepartment Method：POST URL：/ModifyDepartment.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DepartmentId | Noxss | 资产组ID | 是 |  |
| DepartmentNam e | ChsName | 资产组名称 | 是 |  |
| Desc | String | 资产组描述 | 否 | 默认值：空字符串 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| DepartmentId | String | 资产组ID |
| DepartmentName | String | 资产组名称 |
| ParentId | String |  |
| Path | null |  |
| CreateTime | Integer | 创建时间 |
| AssetIds | String |  |

##### 创建资产组

**基本信息**

ID：CreateDepartment Method：POST URL：/CreateDepartment.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| Name | ChsName | 部门名称 | 是 | 部门名称 |
| Desc | String | 部门描述 | 否 | 默认值：空字符串 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| DepartmentId | String | 资产组ID |
| DepartmentName | String | 资产组名称 |
| ParentId | String |  |
| Path | null |  |
| CreateTime | Integer | 创建时间 |
| AssetIds | String |  |

##### 删除资产组

**基本信息**

ID：DeleteDepartment Method：POST URL：/DeleteDepartment.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| ld | Noxss | id | 是 | 资产组ID |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | array | 返回数据 |
| DepartmentId | String | 资产组ID |
| DepartmentName | String | 资产组名称 |
| Desc | String | 描述 |
| ParentId | String |  |
| Path | null |  |
| CreateTime | Integer | 创建时间 |
| AssetIds | String |  |
| Total | Integer | 返回数据总数 |

##### 设置资产组下的资产

**基本信息**

ID：ModifyAssetOfDepartment Method：POST URL：/ModifyAssetOfDepartment.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetId | Uuids | 数据库ID | 否 | 默认值：空字符串 |
| DepartmentId | Noxss | 资产组ID | 是 | 资产组ID |

**返回数据**

无返回数据

##### 更新单个资产组中的规则列表

**基本信息**

ID：ModifyRulesToDepartment Method：POST URL：/ModifyRulesToDepartment.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetGroupId | String | 资产组ID | 是 | 资产组ID |
| RuleIdList | String | 规则ID列表 | 否 | 规则ID列表 |

**返回数据**

无返回数据

##### 更新多个资产组中的规则列表

**基本信息**

ID：ModifyRulesToDepartments Method：POST URL：/ModifyRulesToDepartments.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetGroupIdList | String | 资产组ID列表 | 是 | 资产组ID列表 |
| DelRuleIdList | String | 禁用的规则ID列表 | 否 | 禁用的规则ID列表 |
| AddRuleIdList | String | 启用的规则ID列表 | 否 | 启用的规则ID列表 |

**返回数据**

无返回数据

##### 批量启禁用资产组中的资产

**基本信息**

ID：ModifyAssetToDepartment Method：POST URL：/ModifyAssetToDepartment.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetGroupIdList | String | 资产组ID列表 | 是 | 资产组ID列表 |
| DelAssetIdList | String | 移出的资产ID列表 | 否 | 移出的资产ID列表 |
| AddAssetIdList | String | 移入的资产ID列表 | 否 | 移入的资产ID列表 |

**返回数据**

无返回数据

#### 关注资产

##### 添加关注资产

**基本信息**

ID：CreateFocusedDatabase Method：POST URL：/CreateFocusedDatabase.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetId | Uuid | 数据库资产ID | 是 | 数据库资产ID |

**返回数据**

无返回数据

##### 删除关注资产

**基本信息**

ID：DeleteFocusedDatabase Method：POST URL：/DeleteFocusedDatabase.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetId | Uuid | 数据库资产ID | 是 | 数据库资产ID |

**返回数据**

无返回数据

### 安全规则

#### 规则的启用禁用

##### 启用满足条件的规则

**基本信息**

ID：CreateEnabledRule Method：POST URL：/CreateEnabledRule.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetId | String | 数据库资产ID | 否 | 数据库资产ID |
| RuleId | RuleIds | 查询条件-规则ID | 否 | 默认值：空字符串 |
| Name | String | 查询条件-名称关键字 | 否 | 默认值：空字符串 |
| RuleType | String | 查询条件-规则类型 | 否 | 规则类型 |
| Level | String | 查询条件-规则等级 （逗号分隔） | 否 | 规则等级 |
| GroupId | GroupId | 查询条件-规则组 | 否 | 默认值：空字符串 |

| RecommendInde x | Number | 推荐规则Index | 否 | 推荐规则Index |
|---|---|---|---|---|
| RangeOperation | String | 推荐范围操作符 | 否 | 推荐范围操作符 |
| AssetGroupIds | String | 资产组ID | 否 | 资产组ID |

**返回数据**

无返回数据

##### 禁用满足条件的规则

**基本信息**

ID：DeleteEnabledRule Method：POST URL：/DeleteEnabledRule.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetId | String | 数据库资产ID | 否 | 数据库资产ID |
| RuleId | RuleIds | 查询条件-规则ID | 否 | 默认值：空字符串 |
| Name | String | 查询条件-名称关键字 | 否 | 默认值：空字符串 |
| RuleType | String | 查询条件-规则类型 | 否 | 默认值：空字符串 |
| Level | String | 查询条件-规则等级 （逗号分隔） | 否 | 默认值：空字符串 |
| GroupId | GroupId | 查询条件-规则组 | 否 | 默认值：空字符串 |
| RecommendInde x | Number | 推荐规则Index | 否 | 推荐规则Index |
| RangeOperation | String | 推荐范围操作符 | 否 | 推荐范围操作符 |

| AssetGroupIds | String | 资产组ID | 否 | 资产组ID |
|---|---|---|---|---|

**返回数据**

无返回数据

##### 设置使用规则的资产

**基本信息**

ID：setEnableRule Method：POST URL：/UpdateAssetsToRule.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| AssetIds | Uuids | 资产ID | 是 | 数据库资产ID |
| RuleId | RuleId | 规则ID | 是 | 安全规则ID |
| AssetGroupIds | String | 资产组 | 否 | 资产组 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | array |  |
| Total | Integer |  |

#### 规则组管理

##### 添加规则组

**基本信息**

ID：CreateRuleGroup Method：POST URL：/CreateRuleGroup.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| GroupName | ChsName | 规则组名称 | 是 | 规则组名称 |
| ParentGroupId | Noxss | 上级规则组ID | 是 | 上级规则组ID |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| RuleGroupId | String | 规则组ID |
| RuleGroupName | String | 规则组名称 |
| ParentGroupId | String | 上级规则组ID |
| RuleGroupType | Integer | 规则类型 |

**示例**

**成功返回示例**

请求（双大括号包含部分为变量，在postman中可以通过环境变量预先设置）

```bash
curl -X POST '{{host}}/公共参数/CreateRuleGroup.json' -d 'requestId= {{requestId}}&version={{version}}&clusterKey={{clusterKey}}&clusterTime= {{clusterTime}}&clusterUuid={{clusterUuid}}&clusterSign={{clusterSign}}'
```

返回

```json
{
  "code": "200",
  "message": "success",
  "success": true,
  "data": {
    "rulegroupId": "1316294283803754496",
    "rulegroupName": "22222",
    "parentGroupId": "default",
    "rulegroupType": 1
  },
  "requestId": "63c6f02a-d949-4f35-9ae9-20f891a8fed3",
  "requestTotalCost": 35
}
```

##### 更改规则目录

**基本信息**

ID：ModifyRuleGroup Method：PUT URL：/ModifyRuleGroup.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| GroupId | Noxss | 规则组ID | 是 | 规则组ID |
| GroupName | ChsName | 规则组名称 | 是 | 规则组名称 |
| ParentGroupId | Noxss | 上级规则组ID | 是 | 上级规则组ID |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| RuleGroupId | String | 规则组ID |
| RuleGroupName | String | 规则组名称 |
| ParentGroupId | String | 上级规则组ID |
| RuleGroupType | Integer | 规则类型 |

##### 删除规则目录

**基本信息**

ID：DeleteRuleGroup Method：POST URL：/DeleteRuleGroup.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| GroupId | Noxss | 规则目录ID | 是 | 规则目录ID |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | array | 返回内容 |
| RuleGroupId | String | 规则组ID |
| RuleGroupName | String | 规则组名称 |
| ParentGroupId | String | 上级规则组ID |
| RuleGroupType | Integer | 规则类型 |
| Total | Integer | 耗时 |

##### 获取所有规则组

**基本信息**

ID：DescribeRuleGroups Method：GET URL：/DescribeRuleGroups.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| GroupIds | String | 规则组ID | 否 | 规则组ID |
| GroupName | String | 规则组名称 | 否 | 规则组名称 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|

| List | array | 规则组列表 |
|---|---|---|
| GroupId | String | 规则组ID |
| GroupName | String | 规则组名称 |
| ParentGroupId | String | 父级规则组ID |
| GroupType | Integer | 规则组类型 |
| TotalCount | Integer | 规则组总数 |

#### 内置规则组管理

##### 获取内置规则组列表信息

**基本信息**

ID：getSystemRuleGroups Method：GET URL：/DescribeSystemRuleGroups.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| Sort | Enum | 排序列的名称 | 否 | 取值：参见sort字段的枚举值默认值：groupId |
| Dir | Enum | 排序方式 | 否 | 默认值：desc |
| CurrentPage | Int | 显示页页码 | 否 | 默认值：1 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| AssetId | Uuid | 查询资产可用的规则组 | 否 | 默认值：空字符串 |
| GroupIds | String | 查询规则组ID | 否 | 默认值：空字符串 |

| Name | String | 查询条件名称 | 否 | 默认值：空字符串 |
|---|---|---|---|---|

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| groupId | 规则组ID |
| groupName | 规则组名称 |

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |
| asc | 升序 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| List | array | 规则组信息 |
| GroupId | String | 规则组ID |
| GroupName | String | 规则组名称 |
| ParentGroupId | String | 父级规则组ID |
| GroupType | Integer | 规则组类型 |
| TotalCount | Integer | 规则组总数 |

#### 内置规则管理

##### 获取内置规则列表

**基本信息**

ID：DescribeSystemRules Method：GET URL：/DescribeSystemRules.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| GroupId | GroupId | 规则组ID | 否 | 默认值：空字符串 |
| AssetId | Uuid | 查询资产可用的规则 | 否 | 默认值：空字符串 |
| Sort | Enum | 排序列的名称 | 否 | 默认值：ruleId |
| Dir | Enum | 排序方式 | 否 | 默认值：desc |
| CurrentPage | Int | 显示页页码 | 否 | 默认值：1 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| Name | String | 查询条件-名称 | 否 | 默认值：空字符串 |
| RuleIds | String | 查询条件-规则ID | 否 | 默认值：空字符串 |
| Level | Enum | 查询条件-等级 | 否 | 取值：空字符串1,2,3 默认值：空字符串 |

sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| ruleId | 规则ID |

dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |

| asc | 升序 |
|---|---|

level字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | 低风险 |
| 2 | 中风险 |
| 3 | 高风险 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| list | array | 规则列表 |
| ruleId | String | 规则ID |
| name | String | 规则名称 |
| level | Integer | 规则风险等级 |
| groupId | String | 规则组ID |
| dbtype | String | 数据库类型 |
| whiteList | null | 白名单列表 |
| whiteIds | String | 白名单ID |
| ruleType | Integer | 规则类型 |
| assetIds | String | 资产ID |
| totalCount | Integer | 规则总数 |

### 数审日志查询

#### 日志分析

##### 查询TOP SQL列表

**基本信息**

ID：DescribeTopSql Method：GET URL：/DescribeTopSql.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| StartTime | DateTime | 开始时间 | 是 | 开始时间 |
| EndTime | DateTime | 结束时间 | 是 | 结束时间 |
| AssetId | String | 资产ID | 否 | 默认值：空字符串 |
| TopType | Enum | TOP类型 | 是 | TOP类型 |
| TopCount | Number | TOP数量 | 是 | TOP数量 |
| Cost | Number | 执行时长TOP | 否 | 执行时长TOP |
| AvgCosts | Number | 平均执行时长TOP | 否 | 平均执行时长TOP |
| TotalCount | Number | 执行次数TOP | 否 | 执行次数TOP |
| TotalCosts | Number | 总执行时长 | 否 | 总执行时长 |
| CurrentPage | Number | 显示页页码 | 否 | 默认值：1 |
| PageSize | Number | 每页显示的条数 | 否 | 默认值：10 |

TopType字段的枚举值

| 枚举值 | 值描述 |
|---|---|

| 1 | 平均执行时长 |
|---|---|
| 2 | 执行次数TOP |
| 3 | 总执行时长 |
| 4 | 执行时长TOP |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| List | array | TOPSQL列表 |
| TopId | Integer | TOP排序ID |
| Accessid | String | 审计ID |
| SqlId | String | SQL模板ID |
| Payload | null | SQL语句 |
| SqlModule | String | SQL模板 |
| Dip | String | 服务端IP |
| Sip | null | 客户端IP |
| ClientPrg | null | 客户端工具 |
| LoginUser | null | 数据库账号 |
| Cost | null | 执行时长 |
| TotalCount | Integer | 执行次数 |
| TotalCosts | Integer | 总执行时长 |

| AvgCosts | Integer | 平均执行时长 |
|---|---|---|
| AssetName | String | 资产名称 |
| DbName | String | 库名 |
| TableName | String | 表名 |
| AuditCount | String | 审计数 |
| TotalCount | Integer | 总数 |

##### 导出TOP SQL分析

**基本信息**

ID：ExportTopSql Method：POST URL：/ExportTopSql.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| StartTime | DateTime | 开始时间 | 是 | 开始时间 |
| EndTime | DateTime | 结束时间 | 是 | 结束时间 |
| AssetId | Uuids | 资产ID | 否 | 默认值：空字符串 |
| TopType | Enum | TOP类型 | 是 | TOP类型 |
| TopCount | Number | TOP数量 | 是 | TOP数量 |
| Cost | Number | 执行时长TOP | 否 | 执行时长TOP |
| AvgCosts | Number | 平均执行时长TOP | 否 | 平均执行时长TOP |

| TotalCount | Number | 执行次数TOP | 否 | 执行次数TOP |
|---|---|---|---|---|
| TotalCosts | Number | 总执行时长 | 否 | 总执行时长 |
| CurrentPage | Number | 显示页页码 | 否 | 默认值：1 |
| PageSize | Number | 每页显示的条数 | 否 | 默认值：10 |

TopType字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | 平均执行时长 |
| 2 | 执行次数TOP |
| 3 | 总执行时长 |
| 4 | 执行时长TOP |

**返回数据**

无返回数据

#### 审计日志查询

##### 审计日志查询

**基本信息**

ID：DescribeAuditLogs Method：GET URL：/DescribeAuditLogs.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 数据库 | 否 | 默认值：空字符串 |
| StartTime | String | 起始时间 | 是 | 起始时间 |

| EndTime | String | 结束时间 | 是 | 结束时间 |
|---|---|---|---|---|
| QueryStr | String | 条件表达式 | 否 | 默认值：空字符串 |
| Payload | String | 报文 | 否 | 默认值：空字符串 |
| LoginUser | String | 数据库账号 | 否 | 默认值：空字符串 |
| OpType | Enum(多选) | 操作类型 | 否 | 默认值：空字符串 |
| Sip | String | 客户端IP | 否 | 默认值：空字符串 |
| Dip | String | 服务端IP | 否 | 默认值：空字符串 |
| Result | Enum(多选) | 执行状态 | 否 | 默认值：空字符串 |
| Accessid | Uuids | 审计ID | 否 | 默认值：空字符串 |
| Sessionid | Uuids | 会话ID | 否 | 默认值：空字符串 |
| Sqlid | String | SQL模板ID | 否 | 默认值：空字符串 |
| DbType | Enum | 数据库类型 | 否 | 默认值：空字符串 |
| Sport | String | 客户端端口 | 否 | 默认值：空字符串 |
| Dport | String | 服务端端口 | 否 | 默认值：空字符串 |
| Smac | Macs | 客户端MAC | 否 | 默认值：空字符串 |
| Dmac | Macs | 服务端MAC | 否 | 默认值：空字符串 |
| DbName | String | 数据库名/实例名 | 否 | 默认值：空字符串 |
| ClientPrg | String | 客户端工具 | 否 | 默认值：空字符串 |
| HostName | String | 主机名 | 否 | 默认值：空字符串 |

| ClientUser | String | 操作系统用户名 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| SqlLen | String | 原始SQL长度 | 否 | 默认值：空字符串 |
| EffectRow | String | 影响行数 | 否 | 默认值：空字符串 |
| Cost | String | 执行时长 | 否 | 默认值：空字符串 |
| ResultDesc | String | 执行结果描述 | 否 | 默认值：空字符串 |
| DataSet | String | 返回结果集 | 否 | 默认值：空字符串 |
| AlarmName | String | 规则名称 | 否 | 默认值：空字符串 |
| AlarmLevel | Enum | 告警等级 | 否 | 默认值：空字符串 |
| CurrentPage | Int | 页码 | 否 | 默认值：1 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| Sort | Enum | 排序列的名称 | 否 | 默认值：dateTime |
| Dir | Enum | 排序方式 | 否 | 默认值：desc |
| RelateIp | Ips | 关联IP | 否 | 关联IP |
| RelateUser | String | 关联账号 | 否 | 关联账号 |
| DepartmentId | String | 资产分组ID | 否 | 资产分组ID |
| MaxMatches | Int | 最大返回条数 | 否 | 默认值：100000 |
| MaxQueryTime | Int | 最大查询时间 | 否 | 默认值：10000 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0: 不汇总; 1: 汇总默认值：0 |

| QueryStrategy | Enum | 数据查询策略 | 否 | 0：既查询本页数据又查询总数；1：只查询本页数据不查询总数；2：不查询本页数据只查询总数取值：0,1,2 默认值：0 |
|---|---|---|---|---|
| TableName | String | 表名 | 否 | 表名 |

OpType字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号隔开

| 枚举值 | 值描述 |
|---|---|
| 0 | UNKNOWN |
| 1 | Select |
| 2 | Insert |
| 3 | Update |
| 4 | Delete |
| 5 | Truncate |
| 6 | Create |
| 7 | Alter |
| 8 | Drop |
| 9 | Savepoint |
| 10 | Commit |
| 11 | Rollback |
| 12 | Grant |

| 13 | Revoke |
|---|---|
| 14 | Call |
| 15 | Desc |
| 16 | Describe |
| 17 | Comment |
| 18 | Rename |
| 19 | Load |
| 20 | Unload |
| 21 | Abort |
| 22 | Explain |
| 23 | Shutdown |
| 24 | Kill |
| 25 | Exec |
| 26 | Execute |
| 27 | Login |
| 28 | Logout |
| 29 | Begin |
| 30 | Set |
| 31 | Use |

| 32 | Disassociate |
|---|---|
| 33 | Audit |
| 34 | Associate |
| 35 | Analyze |
| 36 | Noaudit |
| 37 | Lock |
| 38 | Merge |
| 39 | User |
| 40 | Description |
| 41 | If |
| 42 | With |
| 43 | Declare |
| 44 | Flashback |
| 45 | Terminate |
| 46 | Show |
| 47 | Upsert |
| 48 | Ping |
| 49 | Replace |
| 50 | Database |

| 51 | Flush |
|---|---|
| 52 | Mysqladmin |
| 53 | Reset |
| 54 | Cancel |
| 55 | Find |
| 56 | Get |
| 57 | Ismaster |
| 58 | Runcommand |
| 59 | Admincommand |
| 60 | Do |
| 61 | Return |
| 62 | Copy |
| 63 | Repair |
| 64 | Dbstats |
| 65 | Uploadlog |
| 66 | Downloadlog |
| 67 | Fileuploadlog |
| 68 | Filedownloadlog |
| 69 | Purge |

Result字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号隔开

| 枚举值 | 值描述 |
|---|---|
| 0 | 执行失败 |
| 1 | 执行成功 |
| -1 | 未知 |

DbType字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| ORACLE | Oracle |
| MYSQL | MySQL |
| SQLSERVER | SQL Server |
| SYBASE | Sybase ASE |
| DB2 | DB2 |
| INFORMIX | Informix |
| OSCAR | Oscar |
| DM | 达梦(DM) |
| CACHE | Cache |
| POSTGRESQL | PostgreSQL |
| TERADATA | Teradata |
| KINGBASE | 人大金仓(Kingbase) |
| GBASE | GBase |

| MARIADB | MariaDB |
|---|---|
| HTTP | HTTP |
| TELNET | TELNET |
| FTP | FTP |
| HANA | Hana |
| MONGODB | MongoDB |
| HBASEPROTOBUF | HBase(protobuf) |
| HABASETHRIFT | HBase(thrift) |
| HIVE | Hive |
| REDIS | Redis |
| ELASTICSEARCH | Elasticsearch |
| CASSANDRA | Cassandra |
| HDFS | HDFS |
| IMPALA | Impala |
| GAUSSDB | GaussDB |
| LIBRA | LibrA |
| GRAPHBASE | Graphbase |
| GREENPLUM | Greenplum |
| SPARKSQLTHRIFT | Spark SQL(thrift) |

| SPARKSQLRESTFUL | Spark SQL(RESTful) |
|---|---|
| SSDB | SSDB |
| K-DB | K-DB |
| SYBASEIQ | Sybase IQ |
| ARANGODB | ArangoDB |
| NEO4J | Neo4j |
| ORIENTDB | OrientDB |
| TIDB | TiDB |
| VERTICA | Vertica |
| OCEANBASE | OceanBase |
| POLARDB | PolarDB |
| POLARDBX | PolarDB-X |
| ANALYTICDB | AnalyticDB |
| HTTPS | HTTPS |
| MAXCOMPUTE(ODPS) | MaxCompute(ODPS) |
| TBASE | TBase |
| HIGHGO | HighGo |
| TDSQL-C-MYSQL | TDSQL-C MySQL |
| TDSQL-C-POSTGRESQL | TDSQL-C PostgreSQL |

| PERCONA-MYSQL | Percona MySQL |
|---|---|
| PERCONA-MONGODB | Percona MongoDB |
| VASTBASE | Vastbase |
| CLICKHOUSE-HTTP | Clickhouse HTTP |
| CLICKHOUSE-MYSQL | Clickhouse MySQL |

AlarmLevel字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | 低风险 |
| 2 | 中风险 |
| 3 | 高风险 |
| 4 | 信任规则 |

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| dateTime | 时间 |
| effectRow | 影响行数 |
| cost | 执行时长 |

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |
| asc | 升序 |

SearchAllnode字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| List | array | 数据列表 |
| Id | String | ID |
| DateTime | String | 发生时间 |
| SqlLen | String | SQL长度 |
| ClientUser | String | 操作系统用户名 |
| HostName | String | 主机名 |
| Dmac | String | 服务端MAC |
| OpType | String | 操作类型 |
| DbName | String | 数据库名 |
| Smac | String | 客户端MAC |
| Dip | String | 服务端IP |
| Sessionid | String | 会话ID |
| AlarmFlag | String | 是否告警 |
| Result | String | 执行结果 |

| Dport | String | 服务端端口 |
|---|---|---|
| LoginUser | String | 数据库用户名 |
| RelateIp | String | 关联IP |
| Payload | String | SQL语句 |
| AlarmLevel | String | 告警等级 |
| Sip | String | 客户端IP |
| ClientPrg | String | 客户端工具 |
| DataSet | String | 返回结果集 |
| DataSetSize | String | 返回结果集大小 |
| RelateUser | String | 关联用户 |
| Sqlid | String | SQL模板ID |
| PickUser | String | 提取用户名 |
| Cost | String | 执行时长 |
| DbType | String | 数据库类型 |
| AlarmName | String | 告警名称 |
| ResultDesc | String | 执行错误信息 |
| C1 | String | 关联URL |
| C2 | String | 预留字段 |
| Accessid | String | 审计记录ID |

| C3 | String | 预留字段 |
|---|---|---|
| C4 | String | 预留字段 |
| C5 | String | 预留字段 |
| RelateInfo | String | 关联人具体信息 |
| EffectRow | String | 影响行数 |
| PickIp | String | 提取IP |
| Sport | String | 客户端端口 |
| SqlTranslationOverview | String | 描述 |
| TableName | String | 表对象 |
| ExecutorList | String | 执行人 |
| SqlTemplate | String | SQL模板 |
| ParamList | String | 参数列表 |
| ParamId | string | 应用身份识别ID |
| ParamLocation | string | 参数位置 |
| AssetId | string | 资产ID |
| Name | string | 资产名称 |
| AssetName | String | 资产名称 |
| LoginUserAliasName | String | 数据库账号别名 |
| SipName | String | 客户端IP别名 |

| AssetDepartment | String | 资产组名称 |
|---|---|---|
| TotalCount | Integer | 总数 |

**示例**

成功返回示例

**请求双大括号包含部分为变量，在postman中可以通过环境变量预先设置**

```bash
curl '{{host}}/公共参数/DescribeAuditLogs.json?accessKey={{accessKey}}&accessTime= {{accessTime}}&accessSign={{accessSign}}'
```

**返回**

```json
{ "code":string"200" "message":string"success" "success":booltrue "data":{ "List":[ 0:{ "Id":string"5305357806451621925" "DateTime":string"2020-06-12 13:18:36" "SqlLen":string"375" "ClientUser":string"" "HostName":string"" "Dmac":string"00:0c:29:86:de:bc" "OpType":string"2" "DbName":string"" "Smac":string"70:57:bf:d8:c8:01" "Dip":string"192.168.75.51" "Sessionid":string"5305357743815327791" "AlarmFlag":string"0" "Result":string"1" "Dport":string"3306" "LoginUser":string"aaa" "RelateIp":string"" "Payload":string"INSERT INTO `opeAccess` (`id`,`ol_time`,`ol_from`,`ol_user`,`ol_name`,`ol_desc`,`ol_result`) VALUES (DEFAULT,15
```

`91939070,'127.0.0.1','admin','`审计日志查询`','`起始时间：`2020-06-12 00:00:00`，结束时间：`2020-` `06-12 23:59:59`，每页显示的条数：`10`，排序列的名称：`id`，排序方式：降序，最大返回条数：`100000`，最大查询时间：10','1');"

```json
"AlarmLevel":string"0" "Sip":string"192.168.84.36" "ClientPrg":string"" "DataSet":string"" "DataSetSize":string"0" "RelateUser":string"" "Sqlid":string"3705636804216274251" "PickUser":string"" "Cost":string"1"
```

```json
"DbType":string"MYSQL" "AlarmName":string"" "ResultDesc":string"success" "C1":string"" "C2":string"" "Accessid":string"5305357806451621925" "C3":string"" "C4":string"" "C5":string"" "RelateInfo":string"" "EffectRow":string"1" "PickIp":string"" "Sport":string"55195" "SipName":string"" }
```

]

```json
"TotalCount":int18 } "requestId":string"2ca4711a-d8b6-4bdc-aa62-f1f86c8bab88" "requestTotalCost":int917 }
```

##### 审计日志导出

**基本信息**

ID：DescribeExportAuditLog Method：GET URL：/DescribeExportAuditLog.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 数据库 | 否 | 默认值：空字符串 |
| SstartTime | String | 起始时间 | 是 | 起始时间 |
| EndTime | String | 结束时间 | 是 | 结束时间 |
| QueryStr | String | 条件表达式 | 否 | 默认值：空字符串 |
| Payload | String | 报文 | 否 | 默认值：空字符串 |
| LoginUser | String | 数据库账号 | 否 | 默认值：空字符串 |

| OpType | Enum(多选) | 操作类型 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| Sip | String | 客户端IP | 否 | 默认值：空字符串 |
| Dip | String | 服务端IP | 否 | 默认值：空字符串 |
| Result | Enum(多选) | 执行状态 | 否 | 默认值：空字符串 |
| Accessid | Uuids | 审计ID | 否 | 默认值：空字符串 |
| Sessionid | Uuids | 会话ID | 否 | 默认值：空字符串 |
| Sqlid | String | SQL模板ID | 否 | 默认值：空字符串 |
| DbType | Enum | 数据库类型 | 否 | 默认值：空字符串 |
| Sport | String | 客户端端口 | 否 | 默认值：空字符串 |
| Dport | String | 服务端端口 | 否 | 默认值：空字符串 |
| Smac | Macs | 客户端MAC | 否 | 默认值：空字符串 |
| Dmac | Macs | 服务端MAC | 否 | 默认值：空字符串 |
| DbName | String | 数据库名/实例名 | 否 | 默认值：空字符串 |
| ClientPrg | String | 客户端工具 | 否 | 默认值：空字符串 |
| HostName | String | 主机名 | 否 | 默认值：空字符串 |
| ClientUser | String | 操作系统用户名 | 否 | 默认值：空字符串 |
| SqlLen | String | 原始SQL长度 | 否 | 默认值：空字符串 |
| EffectRow | String | 影响行数 | 否 | 默认值：空字符串 |
| Cost | String | 执行时长 | 否 | 默认值：空字符串 |

| ResultDesc | String | 执行结果描述 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| DataSet | String | 返回结果集 | 否 | 默认值：空字符串 |
| AlarmName | String | 规则名称 | 否 | 默认值：空字符串 |
| AlarmLevel | Enum | 告警等级 | 否 | 默认值：空字符串 |
| RelateIp | Ips | 关联IP | 否 | 关联IP |
| RelateUser | String | 关联账号 | 否 | 关联账号 |
| DepartmentId | String | 资产分组ID | 否 | 资产分组ID |
| MaxMatches | Int | 最大返回条数 | 否 | 默认值：100000 |
| MaxQueryTime | Int | 最大查询时间 | 否 | 默认值：10000 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0: 不汇总; 1: 汇总默认值：0 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0: 不汇总; 1: 汇总默认值：0 |
| TableName | String | 表名 | 否 | 默认值：空字符串 |

OpType字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号隔开

| 枚举值 | 值描述 |
|---|---|
| 0 | UNKNOWN |
| 1 | Select |
| 2 | Insert |
| 3 | Update |

| 4 | Delete |
|---|---|
| 5 | Truncate |
| 6 | Create |
| 7 | Alter |
| 8 | Drop |
| 9 | Savepoint |
| 10 | Commit |
| 11 | Rollback |
| 12 | Grant |
| 13 | Revoke |
| 14 | Call |
| 15 | Desc |
| 16 | Describe |
| 17 | Comment |
| 18 | Rename |
| 19 | Load |
| 20 | Unload |
| 21 | Abort |
| 22 | Explain |

| 23 | Shutdown |
|---|---|
| 24 | Kill |
| 25 | Exec |
| 26 | Execute |
| 27 | Login |
| 28 | Logout |
| 29 | Begin |
| 30 | Set |
| 31 | Use |
| 32 | Disassociate |
| 33 | Audit |
| 34 | Associate |
| 35 | Analyze |
| 36 | Noaudit |
| 37 | Lock |
| 38 | Merge |
| 39 | User |
| 40 | Description |
| 41 | If |

| 42 | With |
|---|---|
| 43 | Declare |
| 44 | Flashback |
| 45 | Terminate |
| 46 | Show |
| 47 | Upsert |
| 48 | Ping |
| 49 | Replace |
| 50 | Database |
| 51 | Flush |
| 52 | Mysqladmin |
| 53 | Reset |
| 54 | Cancel |
| 55 | Find |
| 56 | Get |
| 57 | Ismaster |
| 58 | Runcommand |
| 59 | Admincommand |
| 60 | Do |

| 61 | Return |
|---|---|
| 62 | Copy |
| 63 | Repair |
| 64 | Dbstats |
| 65 | Uploadlog |
| 66 | Downloadlog |
| 67 | Fileuploadlog |
| 68 | Filedownloadlog |
| 69 | Purge |

Result字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号隔开

| 枚举值 | 值描述 |
|---|---|
| 0 | 执行失败 |
| 1 | 执行成功 |
| -1 | 未知 |

DbType字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| ORACLE | Oracle |
| MYSQL | MySQL |
| SQLSERVER | SQL Server |

| SYBASE | Sybase ASE |
|---|---|
| DB2 | DB2 |
| INFORMIX | Informix |
| OSCAR | Oscar |
| DM | 达梦(DM) |
| CACHE | Cache |
| POSTGRESQL | PostgreSQL |
| TERADATA | Teradata |
| KINGBASE | 人大金仓(Kingbase) |
| GBASE | GBase |
| MARIADB | MariaDB |
| HTTP | HTTP |
| TELNET | TELNET |
| FTP | FTP |
| HANA | Hana |
| MONGODB | MongoDB |
| HBASEPROTOBUF | HBase(protobuf) |
| HABASETHRIFT | HBase(thrift) |
| HIVE | Hive |

| REDIS | Redis |
|---|---|
| ELASTICSEARCH | Elasticsearch |
| CASSANDRA | Cassandra |
| HDFS | HDFS |
| IMPALA | Impala |
| GAUSSDB | GaussDB |
| LIBRA | LibrA |
| GRAPHBASE | Graphbase |
| GREENPLUM | Greenplum |
| SPARKSQLTHRIFT | Spark SQL(thrift) |
| SPARKSQLRESTFUL | Spark SQL(RESTful) |
| SSDB | SSDB |
| K-DB | K-DB |
| SYBASEIQ | Sybase IQ |
| ARANGODB | ArangoDB |
| NEO4J | Neo4j |
| ORIENTDB | OrientDB |
| TIDB | TiDB |
| VERTICA | Vertica |

| OCEANBASE | OceanBase |
|---|---|
| POLARDB | PolarDB |
| POLARDBX | PolarDB-X |
| ANALYTICDB | AnalyticDB |
| HTTPS | HTTPS |
| MAXCOMPUTE(ODPS) | MaxCompute(ODPS) |
| TBASE | TBase |
| HIGHGO | HighGo |
| TDSQL-C-MYSQL | TDSQL-C MySQL |
| TDSQL-C-POSTGRESQL | TDSQL-C PostgreSQL |
| PERCONA-MYSQL | Percona MySQL |
| PERCONA-MONGODB | Percona MongoDB |
| VASTBASE | Vastbase |
| CLICKHOUSE-HTTP | Clickhouse HTTP |
| CLICKHOUSE-MYSQL | Clickhouse MySQL |

AlarmLevel字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | 低风险 |

| 2 | 中风险 |
|---|---|
| 3 | 高风险 |
| 4 | 信任规则 |

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| dateTime | 时间 |
| effectRow | 影响行数 |
| cost | 执行时长 |

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |
| asc | 升序 |

SearchAllnode字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| FileUrl | String | 导出文件的下载URL |

**示例**

成功返回示例

**请求双大括号包含部分为变量，在postman中可以通过环境变量预先设置**

```bash
curl '{{host}}/公共参数/DescribeExportAuditLog.json?accessKey={{accessKey}}&accessTime={ {accessTime}}&accessSign={{accessSign}}'
```

**返回**

```json
{ "code":string"200" "message":string"success" "success":booltrue "data":{ "FileUrl":string"/data/download/auditLog_20200612131839.xlsx? file=_MlEtgoFl6gwrtoiSLAYmRSdS.WmPvQjjQHk0zMigMUEtdLNioop4R8oHrF8utLxP.GZpr2kB7f.eVKZwCqV 0gYwzE54_IvxvFwkehqkStx9FrIXfDLjUZzETj0gzW8rXxk2t3jqVoEXNiHWrVJIZyAoda0l8C" } "requestId":string"4c492f32-f5a6-4e35-82ef-c6e656cc897d" "requestTotalCost":int4369 }
```

#### 告警分析

##### 查询告警分析列表

**基本信息**

ID：DescribeEventAnalyseList Method：GET URL：/DescribeEventAnalyseList.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| StartTime | Number | 开始时间 | 是 | 开始时间 |
| EndTime | Number | 结束时间 | 是 | 结束时间 |
| RuleName | String | 规则名称 | 否 | 规则名称 |
| DbId | String | 资产和资产组ID | 否 | 资产和资产组ID |
| LoginUser | String | 数据库账号 | 否 | 数据库账号 |

| Sip | String | 客户端IP | 否 | 客户端IP |
|---|---|---|---|---|
| Sort | Enum | 排序列的名称 | 否 | 取值：空字符串 alarmCount 默认值：空字符串 |
| Dir | Enum | 排序方式 | 否 | 取值：desc asc 默认值：desc |
| CurrentPage | Int | 显示页页码 | 否 | 默认值：1 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| alarmCount | 告警数量 |

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |
| asc | 升序 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| list | array | 告警分析列表 |
| RuleName | String | 规则名称 |
| AlarmCount | Integer | 告警数量 |
| AlarmLevel | Integer | 告警等级 |

| RuleDesc | String | 规则描述 |
|---|---|---|
| RuleId | String | 规则ID |
| AssetList | String | 告警资产列表 |
| LoginUserList | String | 数据库名称列表 |
| SipList | String | 客户端IP列表 |
| TotalCount | Integer | 告警列表总数 |

#### 告警日志查询

##### 告警日志查询

**基本信息**

ID：DescribeEventLogs Method：GET URL：/DescribeEventLogs.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 数据库 | 否 | 默认值：空字符串 |
| StartTime | String | 起始时间 | 是 | 起始时间 |
| EndTime | String | 结束时间 | 是 | 结束时间 |
| QueryString | String | 条件表达式 | 否 | 默认值：空字符串 |
| Payload | String | 报文 | 否 | 默认值：空字符串 |
| LoginUser | String | 数据库账号 | 否 | 默认值：空字符串 |
| EventName | String | 规则名称 | 否 | 默认值：空字符串 |

| EventLevel | Enum | 告警等级 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| Accessid | Uuids | 审计ID | 否 | 默认值：空字符串 |
| Sessionid | Uuids | 会话ID | 否 | 默认值：空字符串 |
| Sqlid | String | SQL模板ID | 否 | 默认值：空字符串 |
| DbType | Enum | 数据库类型 | 否 | 默认值：空字符串 |
| Sip | String | 客户端IP | 否 | 默认值：空字符串 |
| Sport | String | 客户端端口 | 否 | 默认值：空字符串 |
| Dip | String | 服务端IP | 否 | 默认值：空字符串 |
| Dport | String | 服务端端口 | 否 | 默认值：空字符串 |
| Smac | Macs | 客户端MAC | 否 | 默认值：空字符串 |
| Dmac | Macs | 服务端MAC | 否 | 默认值：空字符串 |
| DbName | String | 数据库名/实例名 | 否 | 默认值：空字符串 |
| ClientPrg | String | 客户端工具 | 否 | 默认值：空字符串 |
| HostName | String | 主机名 | 否 | 默认值：空字符串 |
| ClientUser | String | 操作系统用户名 | 否 | 默认值：空字符串 |
| SqlLen | String | 原始SQL长度 | 否 | 默认值：空字符串 |
| EffectRow | String | 影响行数 | 否 | 默认值：空字符串 |
| Cost | String | 执行时长 | 否 | 默认值：空字符串 |
| ResultDesc | String | 执行结果描述 | 否 | 默认值：空字符串 |

| DataSet | String | 返回结果集 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| Result | Enum(多选) | 执行状态 | 否 | 默认值：空字符串 |
| OpType | Enum(多选) | 操作类型 | 否 | 默认值：空字符串 |
| Start | Int | 页码 | 否 | 默认值：0 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| Sort | Enum | 排序列的名称 | 否 | 取值：参见sort字段的枚举值默认值：dateTime |
| Dir | Enum | 排序方式 | 否 | 默认值：desc |
| DepartmentId | String | 资产分组ID | 否 | 资产分组ID |
| IsStatistics | Enum | 规则类型(是否统计规则) | 否 | 默认值：空字符串 |
| MaxMatches | Int | 最大返回条数 | 否 | 默认值：100000 |
| MaxQueryTime | Int | 最大查询时间 | 否 | 默认值：10000 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0: 不汇总; 1: 汇总默认值：0 |
| IndustryVersion | Enum | 规则类型 | 否 | 取值:参见a2字段的枚举值 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0: 不汇总; 1: 汇总默认值：0 |
| QueryStrategy | Enum | 数据查询策略 | 否 | 0：既查询本页数据又查询总数；1：只查询本页数据不查询总数；2：不查询本页数据只查询总数取值：0,1,2 默认值：0 |

| TableName | String | 表名 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| Id | Uuids | 告警ID | 否 | 默认值：空字符串 |
| GroupId | String | 规则组 | 否 | 默认值：空字符串 |

EventLevel字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | 低风险 |
| 2 | 中风险 |
| 3 | 高风险 |
| 4 | 信任规则 |

DbType字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| ORACLE | Oracle |
| MYSQL | MySQL |
| SQLSERVER | SQL Server |
| SYBASE | Sybase ASE |
| DB2 | DB2 |
| INFORMIX | Informix |
| OSCAR | Oscar |
| DM | 达梦(DM) |

| CACHE | Cache |
|---|---|
| POSTGRESQL | PostgreSQL |
| TERADATA | Teradata |
| KINGBASE | 人大金仓(Kingbase) |
| GBASE | GBase |
| MARIADB | MariaDB |
| HTTP | HTTP |
| TELNET | TELNET |
| FTP | FTP |
| HANA | Hana |
| MONGODB | MongoDB |
| HBASEPROTOBUF | HBase(protobuf) |
| HABASETHRIFT | HBase(thrift) |
| HIVE | Hive |
| REDIS | Redis |
| ELASTICSEARCH | Elasticsearch |
| CASSANDRA | Cassandra |
| HDFS | HDFS |
| IMPALA | Impala |

| GAUSSDB | GaussDB |
|---|---|
| LIBRA | LibrA |
| GRAPHBASE | Graphbase |
| GREENPLUM | Greenplum |
| SPARKSQLTHRIFT | Spark SQL(thrift) |
| SPARKSQLRESTFUL | Spark SQL(RESTful) |
| SSDB | SSDB |
| K-DB | K-DB |
| SYBASEIQ | Sybase IQ |
| ARANGODB | ArangoDB |
| NEO4J | Neo4j |
| ORIENTDB | OrientDB |
| TIDB | TiDB |
| VERTICA | Vertica |
| OCEANBASE | OceanBase |
| POLARDB | PolarDB |
| POLARDBX | PolarDB-X |
| ANALYTICDB | AnalyticDB |
| HTTPS | HTTPS |

| MAXCOMPUTE(ODPS) | MaxCompute(ODPS) |
|---|---|
| TBASE | TBase |
| HIGHGO | HighGo |
| TDSQL-C-MYSQL | TDSQL-C MySQL |
| TDSQL-C-POSTGRESQL | TDSQL-C PostgreSQL |
| PERCONA-MYSQL | Percona MySQL |
| PERCONA-MONGODB | Percona MongoDB |
| VASTBASE | Vastbase |
| CLICKHOUSE-HTTP | Clickhouse HTTP |
| CLICKHOUSE-MYSQL | Clickhouse MySQL |

Result字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号(,)隔开

| 枚举值 | 值描述 |
|---|---|
| 0 | 执行失败 |
| 1 | 执行成功 |
| -1 | 未知 |

OpType字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号(,)隔开

| 枚举值 | 值描述 |
|---|---|
| 0 | UNKNOWN |

| 1 | Select |
|---|---|
| 2 | Insert |
| 3 | Update |
| 4 | Delete |
| 5 | Truncate |
| 6 | Create |
| 7 | Alter |
| 8 | Drop |
| 9 | Savepoint |
| 10 | Commit |
| 11 | Rollback |
| 12 | Grant |
| 13 | Revoke |
| 14 | Call |
| 15 | Desc |
| 16 | Describe |
| 17 | Comment |
| 18 | Rename |
| 19 | Load |

| 20 | Unload |
|---|---|
| 21 | Abort |
| 22 | Explain |
| 23 | Shutdown |
| 24 | Kill |
| 25 | Exec |
| 26 | Execute |
| 27 | Login |
| 28 | Logout |
| 29 | Begin |
| 30 | Set |
| 31 | Use |
| 32 | Disassociate |
| 33 | Audit |
| 34 | Associate |
| 35 | Analyze |
| 36 | Noaudit |
| 37 | Lock |
| 38 | Merge |

| 39 | User |
|---|---|
| 40 | Description |
| 41 | If |
| 42 | With |
| 43 | Declare |
| 44 | Flashback |
| 45 | Terminate |
| 46 | Show |
| 47 | Upsert |
| 48 | Ping |
| 49 | Replace |
| 50 | Database |
| 51 | Flush |
| 52 | Mysqladmin |
| 53 | Reset |
| 54 | Cancel |
| 55 | Find |
| 56 | Get |
| 57 | Ismaster |

| 58 | Runcommand |
|---|---|
| 59 | Admincommand |
| 60 | Do |
| 61 | Return |
| 62 | Copy |
| 63 | Repair |
| 64 | Dbstats |
| 65 | Uploadlog |
| 66 | Downloadlog |
| 67 | Fileuploadlog |
| 68 | Filedownloadlog |
| 69 | Purge |

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| dateTime | 发生时间 |
| effectRow | 影响行数 |
| cost | 执行时长 |

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|

| desc | 降序 |
|---|---|
| asc | 升序 |

IsStatistics字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 普通规则 |
| 1 | 统计规则 |

IndustryVersion字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 内置规则 |
| 1 | 用户规则 |
| 2 | 统方规则 |
| 3 | 特征库规则 |

SearchAllNode字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| EventLogs | array | 数据列表 |
| LoginUser | String | 数据库用户名 |

| EventName | String | 规则名称 |
|---|---|---|
| EventLevel | String | 规则等级 |
| Accessid | String | 审计记录ID |
| Sessionid | String | 会话记录ID |
| Sqlid | String | SQL模板ID |
| opType | String | 操作类型 |
| Sip | String | 客户端IP |
| Dip | String | 服务端IP |
| Sport | String | 客户端端口 |
| Dport | String | 服务端端口 |
| Smac | String | 客户端MAC |
| Dmac | String | 服务端MAC |
| DbName | String | 数据库名 |
| ClientPrg | String | 客户端工具 |
| HostName | String | 主机名 |
| ClientUser | String | 操作系统用户名 |
| SqlLen | String | SQL长度 |
| EffectRow | String | 影响行数 |
| Cost | String | 执行时长 |

| ResultDesc | String | 执行结果描述 |
|---|---|---|
| DataSet | String | 返回结果集 |
| Result | String | 执行结果 |
| DbType | String | 数据库类型 |
| Id | String | ID |
| DateTime | String | 发生时间 |
| Payload | String | SQL语句 |
| ErrorInfo | String | 错误信息 |
| DataSetSize | String | 返回结果集大小 |
| RelateUser | String | 关联用户 |
| RelateIp | String | 关联IP |
| RelateInfo | String | 关联信息 |
| C1 | String |  |
| C2 | String |  |
| C3 | String |  |
| C4 | String |  |
| C5 | String |  |
| RuleId | String | 规则ID |
| GroupId | String | 规则组ID |

| IsStatistics | String | 是否为统计规则 |
|---|---|---|
| A1 | String |  |
| A2 | String |  |
| A3 | String |  |
| A4 | String |  |
| A5 | String |  |
| TableName | String | 表对象 |
| AssetId | String | 资产ID |
| AssetName | String | 资产名称 |
| ExecutorList | String | 执行人 |
| SqlTranslationOverview | String | 语句描述 |
| LoginUserAliasName | String | 数据库账号别名 |
| SipName | String | 客户端IP别名 |
| AssetDepartment | String | 资产组名称 |
| TotalCount | Integer | 总数 |

**示例**

成功返回示例

**请求双大括号包含部分为变量，在postman中可以通过环境变量预先设置**

```bash
curl '{{host}}/公共参数/DescribeEventLogs.json?accessKey={{accessKey}}&accessTime= {{accessTime}}&accessSign={{accessSign}}'
```

**返回**

```
{
```

```json
"code":string"200" "message":string"success" "success":booltrue "data":{ "EventLogs":[ 0:{ "LoginUser":string"aaa" "EventName":string"select_高风险" "EventLevel":string"3" "Accessid":string"5305413797265211433" "Sessionid":string"5305404758543368227" "Sqlid":string"3971616368224711388" "OpType":string"1" "Sip":string"192.168.84.36" "Dip":string"192.168.75.51" "Sport":string"56819" "Dport":string"3306" "Smac":string"70:57:bf:d8:c8:01" "Dmac":string"00:0c:29:86:de:bc" "DbName":string"" "ClientPrg":string"" "HostName":string"" "ClientUser":string"" "SqlLen":string"112" "EffectRow":string"1" "Cost":string"2" "ResultDesc":string"success" "DataSet":string"value ~ expire |E$L| {"userId":"00000000000000000000000000000001","username":"admin","loginType":"passwd","org ":"","currentOrgId":"","role":"superAdmin","maxAge":300000000,"pwdExpire":false,"pwdExpir ime":"","isFirstLogin":false,"expire":1592225032} ~ 1592239752 |E$L| " "Result":string"1" "DbType":string"MYSQL" "Id":string"5305413797265211433" "DateTime":string"2020-06-12 13:32:11" "Payload":string"SELECT `value`, `expire` FROM `session` AS `session` WHERE `session`.` key` = 'd4e61bc70d22472387ff75e9d26171dc';" "ErrorInfo":string"success" "DataSetSize":string"252" "RelateUser":string"" "RelateIp":string"" "PickUser":string"" "PickIp":string"" "RelateInfo":string"" "C1":string"" "C2":string"" "C3":string"" "C4":string"" "C5":string"" "RuleId":string"1271311369458679808" "GroupId":string"default" "IsStatistics":string"0" "A1":string"0" "A2":string"" "A3":string""
```

```json
"A3":string"" "A4":string"" "A5":string"" "SipName":string"" }
```

]

```json
"TotalCount":int13 } "requestId":string"dce0162b-5282-4dee-8d7d-d6c42029711f" "requestTotalCost":int974 }
```

##### 告警日志导出

**基本信息**

ID：DescribeExportEventLog URL：/dbaudit/log/eventLogs/export Method：GET

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 数据库 | 否 | 默认值：空字符串 |
| StartTime | String | 起始时间 | 是 | 起始时间 |
| EndTime | String | 结束时间 | 是 | 结束时间 |
| QueryString | String | 条件表达式 | 否 | 默认值：空字符串 |
| Payload | String | 报文 | 否 | 默认值：空字符串 |
| LoginUser | String | 数据库账号 | 否 | 默认值：空字符串 |
| EventName | String | 规则名称 | 否 | 默认值：空字符串 |
| EventLevel | Enum | 告警等级 | 否 | 默认值：空字符串 |
| Accessid | Uuids | 审计ID | 否 | 默认值：空字符串 |
| Sessionid | Uuids | 会话ID | 否 | 默认值：空字符串 |

| Sqlid | String | SQL模板ID | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| DbType | Enum | 数据库类型 | 否 | 默认值：空字符串 |
| Sip | String | 客户端IP | 否 | 默认值：空字符串 |
| Sport | String | 客户端端口 | 否 | 默认值：空字符串 |
| Dip | String | 服务端IP | 否 | 默认值：空字符串 |
| Dport | String | 服务端端口 | 否 | 默认值：空字符串 |
| Smac | Macs | 客户端MAC | 否 | 默认值：空字符串 |
| Dmac | Macs | 服务端MAC | 否 | 默认值：空字符串 |
| DbName | String | 数据库名/实例名 | 否 | 默认值：空字符串 |
| ClientPrg | String | 客户端工具 | 否 | 默认值：空字符串 |
| HostName | String | 主机名 | 否 | 默认值：空字符串 |
| ClientUser | String | 操作系统用户名 | 否 | 默认值：空字符串 |
| SqlLen | String | 原始SQL长度 | 否 | 默认值：空字符串 |
| EffectRow | String | 影响行数 | 否 | 默认值：空字符串 |
| Cost | String | 执行时长 | 否 | 默认值：空字符串 |
| ResultDesc | String | 执行结果描述 | 否 | 默认值：空字符串 |
| DataSet | String | 返回结果集 | 否 | 默认值：空字符串 |
| Result | Enum(多选) | 执行状态 | 否 | 默认值：空字符串 |
| OpType | Enum(多选) | 操作类型 | 否 | 默认值：空字符串 |

| DepartmentId | String | 资产分组ID | 否 | 资产分组ID |
|---|---|---|---|---|
| IsStatistics | Enum | 规则类型(是否统计规则) | 否 | 默认值：空字符串 |
| MaxMatches | Int | 最大返回条数 | 否 | 默认值：100000 |
| MaxQueryTime | Int | 最大查询时间 | 否 | 默认值：10000 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0: 不汇总; 1: 汇总默认值：0 |
| IndustryVersion | Enum | 规则类型 | 否 | 取值:参见a2字段的枚举值 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0: 不汇总; 1: 汇总默认值：0 |
| QueryStrategy | Enum | 数据查询策略 | 否 | 0：既查询本页数据又查询总数；1：只查询本页数据不查询总数；2：不查询本页数据只查询总数取值：0,1,2 默认值：0 |
| TableName | String | 表名 | 否 | 默认值：空字符串 |
| GroupId | String | 规则组 | 否 | 默认值：空字符串 |

EventLevel字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 1 | 低风险 |
| 2 | 中风险 |
| 3 | 高风险 |

| 4 | 信任规则 |
|---|---|

DbType字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| ORACLE | Oracle |
| MYSQL | MySQL |
| SQLSERVER | SQL Server |
| SYBASE | Sybase ASE |
| DB2 | DB2 |
| INFORMIX | Informix |
| OSCAR | Oscar |
| DM | 达梦(DM) |
| CACHE | Cache |
| POSTGRESQL | PostgreSQL |
| TERADATA | Teradata |
| KINGBASE | 人大金仓(Kingbase) |
| GBASE | GBase |
| MARIADB | MariaDB |
| HTTP | HTTP |
| TELNET | TELNET |

| FTP | FTP |
|---|---|
| HANA | Hana |
| MONGODB | MongoDB |
| HBASEPROTOBUF | HBase(protobuf) |
| HABASETHRIFT | HBase(thrift) |
| HIVE | Hive |
| REDIS | Redis |
| ELASTICSEARCH | Elasticsearch |
| CASSANDRA | Cassandra |
| HDFS | HDFS |
| IMPALA | Impala |
| GAUSSDB | GaussDB |
| LIBRA | LibrA |
| GRAPHBASE | Graphbase |
| GREENPLUM | Greenplum |
| SPARKSQLTHRIFT | Spark SQL(thrift) |
| SPARKSQLRESTFUL | Spark SQL(RESTful) |
| SSDB | SSDB |
| K-DB | K-DB |

| SYBASEIQ | Sybase IQ |
|---|---|
| ARANGODB | ArangoDB |
| NEO4J | Neo4j |
| ORIENTDB | OrientDB |
| TIDB | TiDB |
| VERTICA | Vertica |
| OCEANBASE | OceanBase |
| POLARDB | PolarDB |
| POLARDBX | PolarDB-X |
| ANALYTICDB | AnalyticDB |
| HTTPS | HTTPS |
| MAXCOMPUTE(ODPS) | MaxCompute(ODPS) |
| TBASE | TBase |
| HIGHGO | HighGo |
| TDSQL-C-MYSQL | TDSQL-C MySQL |
| TDSQL-C-POSTGRESQL | TDSQL-C PostgreSQL |
| PERCONA-MYSQL | Percona MySQL |
| PERCONA-MONGODB | Percona MongoDB |
| VASTBASE | Vastbase |

| CLICKHOUSE-HTTP | Clickhouse HTTP |
|---|---|
| CLICKHOUSE-MYSQL | Clickhouse MySQL |

OpType字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号隔开

| 枚举值 | 值描述 |
|---|---|
| 0 | UNKNOWN |
| 1 | Select |
| 2 | Insert |
| 3 | Update |
| 4 | Delete |
| 5 | Truncate |
| 6 | Create |
| 7 | Alter |
| 8 | Drop |
| 9 | Savepoint |
| 10 | Commit |
| 11 | Rollback |
| 12 | Grant |
| 13 | Revoke |
| 14 | Call |

| 15 | Desc |
|---|---|
| 16 | Describe |
| 17 | Comment |
| 18 | Rename |
| 19 | Load |
| 20 | Unload |
| 21 | Abort |
| 22 | Explain |
| 23 | Shutdown |
| 24 | Kill |
| 25 | Exec |
| 26 | Execute |
| 27 | Login |
| 28 | Logout |
| 29 | Begin |
| 30 | Set |
| 31 | Use |
| 32 | Disassociate |
| 33 | Audit |

| 34 | Associate |
|---|---|
| 35 | Analyze |
| 36 | Noaudit |
| 37 | Lock |
| 38 | Merge |
| 39 | User |
| 40 | Description |
| 41 | If |
| 42 | With |
| 43 | Declare |
| 44 | Flashback |
| 45 | Terminate |
| 46 | Show |
| 47 | Upsert |
| 48 | Ping |
| 49 | Replace |
| 50 | Database |
| 51 | Flush |
| 52 | Mysqladmin |

| 53 | Reset |
|---|---|
| 54 | Cancel |
| 55 | Find |
| 56 | Get |
| 57 | Ismaster |
| 58 | Runcommand |
| 59 | Admincommand |
| 60 | Do |
| 61 | Return |
| 62 | Copy |
| 63 | Repair |
| 64 | Dbstats |
| 65 | Uploadlog |
| 66 | Downloadlog |
| 67 | Fileuploadlog |
| 68 | Filedownloadlog |
| 69 | Purge |

IsStatistics字段的枚举值

| 枚举值 | 值描述 |
|---|---|

| 0 | 普通规则 |
|---|---|
| 1 | 统计规则 |

searchAllNode字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| FileUrl | String | 导出文件的下载URL |

**示例**

成功返回示例

**请求双大括号包含部分为变量，在postman中可以通过环境变量预先设置**

```bash
curl '{{host}}/公共参数/DescribeExportEventLog.json?accessKey={{accessKey}}&accessTime={ {accessTime}}&accessSign={{accessSign}}'
```

**返回**

```json
{ "code":string"200" "message":string"success" "success":booltrue "data":{ "FileUrl":string"/data/download/eventLog_20200612133222.xlsx? file=_MlEtgoFl6gwrtoiSLAYmRSdS.WmPvQjS4J92DrHAcQEtdLNioop4dfQDKCP1Q3pVItd3mnU727.eVKZwCqV 4X7GUz3sFHPSbr1qAqA5Wtx9FrIXfDLuL0dVcAsdzS8rXxk2t3jqVoEXNiHWrVJIZyAoda0l8C" } "requestId":string"6dde888f-b9fc-4fbb-8926-0441b2f6bd37" "requestTotalCost":int1348 }
```

#### 会话日志查询

##### 会话日志查询

**基本信息**

ID：DescribeSessionLogs Method：GET URL：/DescribeSessionLogs.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 数据库 | 否 | 默认值：空字符串 |
| StartTime | String | 起始时间 | 是 | 起始时间 |
| EndTime | String | 结束时间 | 是 | 结束时间 |
| Sip | String | 客户端IP | 否 | 默认值：空字符串 |
| Sport | String | 客户端端口 | 否 | 默认值：空字符串 |
| LoginUser | String | 数据库账号 | 否 | 默认值：空字符串 |
| Dip | String | 服务端IP | 否 | 默认值：空字符串 |
| Dport | String | 服务端端口 | 否 | 默认值：空字符串 |
| Sessionid | Uuids | 会话ID | 否 | 默认值：空字符串 |
| DbType | Enum | 数据库类型 | 否 | 默认值：空字符串 |
| Smac | Macs | 客户端MAC | 否 | 默认值：空字符串 |
| Dmac | Macs | 服务端MAC | 否 | 默认值：空字符串 |
| ClientPrg | String | 客户端工具 | 否 | 默认值：空字符串 |
| HostName | String | 主机名 | 否 | 默认值：空字符串 |
| ClientUser | String | 操作系统用户名 | 否 | 默认值：空字符串 |

| DbName | String | 数据库名/实例名 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| SessionState | Enum | 状态标识 | 否 | 默认值：空字符串 |
| SqlCount | String | SQL总记录数 | 否 | 默认值：空字符串 |
| RequestFlow | String | 会话请求总流量 | 否 | 默认值：空字符串 |
| ResponseFlow | String | 会话返回总流量 | 否 | 默认值：空字符串 |
| CurrentPage | Int | 页码 | 否 | 默认值：0 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值：10 |
| Sort | Enum | 排序列的名称 | 否 | 默认值：startTime |
| Dir | Enum | 排序方式 | 否 | 默认值：desc |
| DepartmentId | String | 资产分组ID | 否 | 资产分组ID |
| MaxMatches | Int | 最大返回条数 | 否 | 默认值：100000 |
| MaxQueryTime | Int | 最大查询时间 | 否 | 默认值：10000 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0:不汇总; 1:汇总默认值：0 |
| QueryStrategy | Enum | 数据查询策略 | 否 | 0：既查询本页数据又查询总数；1：只查询本页数据不查询总数； 2：不查询本页数据只查询总数取值：0,1,2 默认值：0 |

DbType字段的枚举值

| 枚举值 | 值描述 |
|---|---|

| ORACLE | Oracle |
|---|---|
| MYSQL | MySQL |
| SQLSERVER | SQL Server |
| SYBASE | Sybase ASE |
| DB2 | DB2 |
| INFORMIX | Informix |
| OSCAR | Oscar |
| DM | 达梦(DM) |
| CACHE | Cache |
| POSTGRESQL | PostgreSQL |
| TERADATA | Teradata |
| KINGBASE | 人大金仓(Kingbase) |
| GBASE | GBase |
| MARIADB | MariaDB |
| HTTP | HTTP |
| TELNET | TELNET |
| FTP | FTP |
| HANA | Hana |
| MONGODB | MongoDB |

| HBASEPROTOBUF | HBase(protobuf) |
|---|---|
| HABASETHRIFT | HBase(thrift) |
| HIVE | Hive |
| REDIS | Redis |
| ELASTICSEARCH | Elasticsearch |
| CASSANDRA | Cassandra |
| HDFS | HDFS |
| IMPALA | Impala |
| GAUSSDB | GaussDB |
| LIBRA | LibrA |
| GRAPHBASE | Graphbase |
| GREENPLUM | Greenplum |
| SPARKSQLTHRIFT | Spark SQL(thrift) |
| SPARKSQLRESTFUL | Spark SQL(RESTful) |
| SSDB | SSDB |
| K-DB | K-DB |
| SYBASEIQ | Sybase IQ |
| ARANGODB | ArangoDB |
| NEO4J | Neo4j |

| ORIENTDB | OrientDB |
|---|---|
| TIDB | TiDB |
| VERTICA | Vertica |
| OCEANBASE | OceanBase |
| POLARDB | PolarDB |
| POLARDBX | PolarDB-X |
| ANALYTICDB | AnalyticDB |
| HTTPS | HTTPS |
| MAXCOMPUTE(ODPS) | MaxCompute(ODPS) |
| TBASE | TBase |
| HIGHGO | HighGo |
| TDSQL-C-MYSQL | TDSQL-C MySQL |
| TDSQL-C-POSTGRESQL | TDSQL-C PostgreSQL |
| PERCONA-MYSQL | Percona MySQL |
| PERCONA-MONGODB | Percona MongoDB |
| VASTBASE | Vastbase |
| CLICKHOUSE-HTTP | Clickhouse HTTP |
| CLICKHOUSE-MYSQL | Clickhouse MySQL |

SessionState字段的枚举值

| 枚举值 | 值描述 |
|---|---|

|  | 数据库审计与风险控制开发指南·数据库审计与风险控制系统 |
|---|---|

| 0 | 登入失败 |
|---|---|
| 1 | 登入成功 |
| 2 | 未知 |
| -1 | 未知 |

Sort字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| startTime | 开始时间 |

Dir字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| desc | 降序 |
| asc | 升序 |

SearchAllNode字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| SessionLogs | array | 数据列表 |
| StartTime | String | 会话开始时间 |

| EndTime | String | 会话结束时间 |
|---|---|---|
| Id | String | ID |
| LoginUser | String | 数据库账号 |
| Sip | String | 客户端IP |
| Dip | String | 服务端IP |
| Sessionid | String | 会话ID |
| DbType | String | 数据库类型 |
| Sport | String | 客户端端口 |
| Dport | String | 服务端端口 |
| Smac | String | 客户端MAC |
| Dmac | String | 服务端MAC |
| DbName | String | 数据库名 |
| ClientPrg | String | 客户端工具 |
| HostName | String | 主机名 |
| ClientUser | String | 操作系统用户名 |
| SqlCount | String | SQL总记录数 |
| RequestFlow | String | 会话请求总流量 |
| ResponseFlow | String | 会话返回总流量 |
| SessionState | String | 会话状态标识 |

| StrInfo | String |  |
|---|---|---|
| Encode | String |  |
| ProtocolConnection | String |  |
| NormalEnd | String |  |
| FilterSqlCount | String |  |
| AssetId | String | 资产ID |
| AssetName | String | 资产名称 |
| LoginUserAliasName | String | 数据库账号别名 |
| SipName | String | 客户端IP别名 |
| AssetDepartment | String | 资产组名称 |
| TotalCount | Integer | 总数 |

**示例**

成功返回示例

**请求双大括号包含部分为变量，在postman中可以通过环境变量预先设置**

```bash
curl '{{host}}/公共参数/DescribeSessionLogs.json?accessKey={{accessKey}}&accessTime={{ac cessTime}}&accessSign={{accessSign}}'
```

**返回**

```json
{ "code":string"200" "message":string"success" "success":booltrue "data":{ "SessionLogs":[ 0:{26 items "StartTime":string"2020-06-12 13:33:26" "EndTime":string"2020-06-12 13:33:26" "LogId":string"5305419291123777576" "LoginUser":string"aaa" "Sip":string"192.168.84.36" "Dip":string"192.168.75.51" "Sessionid":string"5305418945180336169" "DbType":string"MYSQL" "Sport":string"57412" "Dport":string"3306" "Smac":string"70:57:bf:d8:c8:01" "Dmac":string"00:0c:29:86:de:bc" "DbName":string"" "ClientPrg":string"" "HostName":string"" "ClientUser":string"" "SqlCount":string"4" "RequestFlow":string"353" "ResponseFlow":string"399" "SessionState":string"1" "StrInfo":string"" "Encode":string"" "ProtocolConnection":string"0" "NormalEnd":string"1" "FilterSqlCount":string"0" "SipName":string"" }
```

]

```json
"TotalCount":int2 } "requestId":string"ff79e2a4-a3cf-4ab4-af22-3d7597ae11e6" "requestTotalCost":int908 }
```

##### 会话日志导出

**基本信息**

ID：DescribeExportSessionLog Method：GET URL：/DescribeExportSessionLog.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| DbId | Uuids | 数据库 | 否 | 默认值：空字符串 |
| StartTime | String | 起始时间 | 是 | 起始时间 |
| EndTime | String | 结束时间 | 是 | 结束时间 |
| Sip | String | 客户端IP | 否 | 默认值：空字符串 |
| Sport | String | 客户端端口 | 否 | 默认值：空字符串 |
| LoginUser | String | 数据库账号 | 否 | 默认值：空字符串 |
| Dip | String | 服务端IP | 否 | 默认值：空字符串 |
| Dport | String | 服务端端口 | 否 | 默认值：空字符串 |
| Sessionid | Uuids | 会话ID | 否 | 默认值：空字符串 |
| DbType | Enum | 数据库类型 | 否 | 默认值：空字符串 |
| Smac | Macs | 客户端MAC | 否 | 默认值：空字符串 |
| Dmac | Macs | 服务端MAC | 否 | 默认值：空字符串 |
| ClientPrg | String | 客户端工具 | 否 | 默认值：空字符串 |
| HostName | String | 主机名 | 否 | 默认值：空字符串 |
| ClientUser | String | 操作系统用户名 | 否 | 默认值：空字符串 |
| DbName | String | 数据库名/实例名 | 否 | 默认值：空字符串 |
| SessionState | Enum | 状态标识 | 否 | 默认值：空字符串 |
| SqlCount | String | SQL总记录数 | 否 | 默认值：空字符串 |

| RequestFlow | String | 会话请求总流量 | 否 | 默认值：空字符串 |
|---|---|---|---|---|
| ResponseFlow | String | 会话返回总流量 | 否 | 默认值：空字符串 |
| DepartmentId | String | 资产分组ID | 否 | 资产分组ID |
| MaxMatches | Int | 最大返回条数 | 否 | 默认值：100000 |
| MaxQueryTime | Int | 最大查询时间 | 否 | 默认值：10000 |
| SearchAllNode | Enum | 是否汇总节点日志 | 否 | 0:不汇总; 1:汇总默认值：0 |

dbType字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| ORACLE | Oracle |
| MYSQL | MySQL |
| SQLSERVER | SQL Server |
| SYBASE | Sybase ASE |
| DB2 | DB2 |
| INFORMIX | Informix |
| OSCAR | Oscar |
| DM | 达梦(DM) |
| CACHE | Cache |
| POSTGRESQL | PostgreSQL |
| TERADATA | Teradata |

| KINGBASE | 人大金仓(Kingbase) |
|---|---|
| GBASE | GBase |
| MARIADB | MariaDB |
| HTTP | HTTP |
| TELNET | TELNET |
| FTP | FTP |
| HANA | Hana |
| MONGODB | MongoDB |
| HBASEPROTOBUF | HBase(protobuf) |
| HABASETHRIFT | HBase(thrift) |
| HIVE | Hive |
| REDIS | Redis |
| ELASTICSEARCH | Elasticsearch |
| CASSANDRA | Cassandra |
| HDFS | HDFS |
| IMPALA | Impala |
| GAUSSDB | GaussDB |
| LIBRA | LibrA |
| GRAPHBASE | Graphbase |

| GREENPLUM | Greenplum |
|---|---|
| SPARKSQLTHRIFT | Spark SQL(thrift) |
| SPARKSQLRESTFUL | Spark SQL(RESTful) |
| SSDB | SSDB |
| K-DB | K-DB |
| SYBASEIQ | Sybase IQ |
| ARANGODB | ArangoDB |
| NEO4J | Neo4j |
| ORIENTDB | OrientDB |
| TIDB | TiDB |
| VERTICA | Vertica |
| OCEANBASE | OceanBase |
| POLARDB | PolarDB |
| POLARDBX | PolarDB-X |
| ANALYTICDB | AnalyticDB |
| HTTPS | HTTPS |
| MAXCOMPUTE(ODPS) | MaxCompute(ODPS) |
| TBASE | TBase |
| HIGHGO | HighGo |

| TDSQL-C-MYSQL | TDSQL-C MySQL |
|---|---|
| TDSQL-C-POSTGRESQL | TDSQL-C PostgreSQL |
| PERCONA-MYSQL | Percona MySQL |
| PERCONA-MONGODB | Percona MongoDB |
| VASTBASE | Vastbase |
| CLICKHOUSE-HTTP | Clickhouse HTTP |
| CLICKHOUSE-MYSQL | Clickhouse MySQL |

sessionState字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 登入失败 |
| 1 | 登入成功 |
| 2 | 未知 |
| -1 | 未知 |

serachAllNode字段的枚举值

| 枚举值 | 值描述 |
|---|---|
| 0 | 禁用 |
| 1 | 启用 |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|

| FileUrl | String | 导出文件的下载URL |
|---|---|---|

**示例**

成功返回示例

**请求双大括号包含部分为变量，在postman中可以通过环境变量预先设置**

```bash
curl '{{host}}/公共参数/DescribeExportSessionLog.json?accessKey= {{accessKey}}&accessTime={{accessTime}}&accessSign={{accessSign}}'
```

**返回**

```json
{ "code":string"200" "message":string"success" "success":booltrue "data":{ "FileUrl":string"/data/download/sessionLog_20200612133323.xlsx? file=_MlEtgoFl6gwrtoiSLAYmU6KpsLUtXNhJJssynTv4Tc9Wqy8JF4kg41GdBe364MiQEWVb8InmKMXws0GjYCH YF_xsADxCKx4nvEjxntKjf0dG2yLp6G9xgS6wWizZs8F.yRrBoYAkkRgQJwhown5L51vstkXSKWjfmaJ1UAlM" } "requestId":string"77c4ef66-c9f4-4ef9-a94d-2b9877701d3a" "requestTotalCost":int1079 }
```

#### SQL模板

##### 获取SQL模板列表

**基本信息**

ID：DescribeSqlTemplates Method：GET URL：/DescribeSqlTemplates.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| Dip | String | 服务端IP | 否 | 服务端IP |
| EndTime | String | 结束时间 | 否 | 结束时间 |
| StartTime | String | 开始时间 | 否 | 开始时间 |

| OpType | Enum(多选) | 操作类型 | 否 | 操作类型 |
|---|---|---|---|---|
| SqlTemplate | String | 报文 | 否 | 报文 |
| SqlId | String | SQL模板ID | 否 | SQL模板ID |
| CurrentPage | Int | 显示页页码 | 否 | 默认值： 1 |
| PageSize | Int | 每页显示的条数 | 否 | 默认值： 10 |

opType字段的枚举值该参数可设多个枚举值，多个值之间用英文逗号隔开

| 枚举值 | 值描述 |
|---|---|
| 0 | UNKNOWN |
| 1 | Select |
| 2 | Insert |
| 3 | Update |
| 4 | Delete |
| 5 | Truncate |
| 6 | Create |
| 7 | Alter |
| 8 | Drop |
| 9 | Savepoint |
| 10 | Commit |
| 11 | Rollback |

| 12 | Grant |
|---|---|
| 13 | Revoke |
| 14 | Call |
| 15 | Desc |
| 16 | Describe |
| 17 | Comment |
| 18 | Rename |
| 19 | Load |
| 20 | Unload |
| 21 | Abort |
| 22 | Explain |
| 23 | Shutdown |
| 24 | Kill |
| 25 | Exec |
| 26 | Execute |
| 27 | Login |
| 28 | Logout |
| 29 | Begin |
| 30 | Set |

| 31 | Use |
|---|---|
| 32 | Disassociate |
| 33 | Audit |
| 34 | Associate |
| 35 | Analyze |
| 36 | Noaudit |
| 37 | Lock |
| 38 | Merge |
| 39 | User |
| 40 | Description |
| 41 | If |
| 42 | With |
| 43 | Declare |
| 44 | Flashback |
| 45 | Terminate |
| 46 | Show |
| 47 | Upsert |
| 48 | Ping |
| 49 | Replace |

| 50 | Database |
|---|---|
| 51 | Flush |
| 52 | Mysqladmin |
| 53 | Reset |
| 54 | Cancel |
| 55 | Find |
| 56 | Get |
| 57 | Ismaster |
| 58 | Runcommand |
| 59 | Admincommand |
| 60 | Do |
| 61 | Return |
| 62 | Copy |
| 63 | Repair |
| 64 | Dbstats |
| 65 | Uploadlog |
| 66 | Downloadlog |
| 67 | Fileuploadlog |
| 68 | Filedownloadlog |

| 69 | Purge |
|---|---|

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| List | array | 数据列表 |
| Id | Integer | ID |
| SqlId | Integer | SQL模板ID |
| Dip | String | 目的IP |
| OpType | Integer | 操作类型 |
| OpObj | String | 操作对象 |
| SqlTemplate | String | SQL末班 |
| DateTime | String | 发生时间 |
| Payload | String | 报文 |
| TotalCount | Integer | 总数 |

**示例**

**成功返回示例**

**请求（双大括号包含部分为变量，在postman中可以通过环境变量预先设置)**

```bash
curl '{{host}}/sqlTemplates?requestId={{requestId}}&version={{version}}&clusterKey={{cl usterKey}}&clusterTime={{clusterTime}}&clusterUuid={{clusterUuid}}&clusterSign={{cluste rSign}}'
```

**返回**

```json
{
  "code": "200",
  "message": "success",
  "success": true,
  "data": {
    "list": [
```

```json
      {
        "id": 5106,
        "sqlId": 0,
        "dip": "192.168.50.89",
        "opType": 0,
        "opObj": "",
        "sqlTemplate": "",
        "dateTime": "2020-01-03 15:21:34",
        "payload": "-"
      },
      {
        "id": 5079,
        "sqlId": "1367040878257519143",
        "dip": "10.2.5.33",
        "opType": 1,
        "opObj": "",
        "sqlTemplate": "SELECT * FROM cltj_tb168 WHERE (sys_unitguid= :1 ) AND
(sys_datayear= :2 AND sys_datatime= :3 AND sys_timetype= :4 )",
        "dateTime": "2020-01-03 15:21:34",
        "payload": "SELECT * FROM cltj_tb168 WHERE
(sys_unitguid='0000012977F691083C4291887314B8E0') AND (sys_datayear='2011' AND sys_data time=1 AND sys_timetype='N')"
      },
      {
        "id": 5078,
        "sqlId": "4182849518253780682",
        "dip": "10.2.5.33",
        "opType": 1,
        "opObj": "",
        "sqlTemplate": "SELECT * FROM cltj_tb163 WHERE (sys_unitguid= :1 ) AND
(sys_datayear= :2 AND sys_datatime= :3 AND sys_timetype= :4 )",
        "dateTime": "2020-01-03 15:21:34",
        "payload": "SELECT * FROM cltj_tb163 WHERE
(sys_unitguid='0000012977F691083C4291887314B8E0') AND (sys_datayear='2011' AND sys_data time=1 AND sys_timetype='N')"
      },
      {
        "id": 5064,
        "sqlId": "552135666239538229",
        "dip": "10.2.5.33",
        "opType": 2,
        "opObj": "",
        "sqlTemplate": "INSERT INTO cltj_tb646
(sys_unitguid,sys_datayear,sys_timetype,sys_datatime,fd_ :1 ,fd_ :2 ,fd_ :3 ,fd_ :4 ,fd _ :5 ,fd_ :6 ,fd_ :7 ,fd_ :8 ,fd_ :9 ,fd_ :10 ,fd_ :11 ,fd_ :12 ,fd_ :13 ,fd_ :14 ,fd_ :15 ,fd_ :16 ,fd_ :17 ,fd_ :18 ,sys_floatguid,sys_unitorder) VALUES :19",
        "dateTime": "2020-01-03 15:21:33",
        "payload": "INSERT INTO cltj_tb646
(sys_unitguid,sys_datayear,sys_timetype,sys_datatime,fd_0,fd_1,fd_10,fd_11,fd_12,fd_13,fd 4,fd_15,fd_16,fd_17,fd_2,fd_3,fd_4,fd_5,fd_6,fd_7,fd_8,fd_9,sys_floatguid,sys_unitorder)
```

`VALUES ('000001294553A286846B928676563F4C' ,'2016' ,'N' ,1 ,'4' ,'`常山县残疾人劳动就业服务

```
所' ,'2' ,2 ,2 ,9 , ,'118.525778' ,'28.89918' ,16 ,'726615610' ,'县天马镇文峰东路113－1号' ,'324200' ,'5890236' ,'李军，5890208' ,'1995-10-20 00:00:00' ,'5' ,'2' ,'000001569B6331BF88CA2236A87DE08E' ,'00000001' )"
```

```json
      },
      {
        "id": 4901,
        "sqlId": "2179030142124202523",
        "dip": "10.2.5.33",
        "opType": 1,
        "opObj": "",
        "sqlTemplate": "select
evt_guid,tsk_prefix,evt_time,evt_type,evt_catalog,evt_module,evt_user,evt_host,evt_info,e _data from sys_event where evt_guid = :1",
        "dateTime": "2020-01-03 15:21:24",
        "payload": "select
evt_guid,tsk_prefix,evt_time,evt_type,evt_catalog,evt_module,evt_user,evt_host,evt_info,e _data from sys_event where evt_guid = '0000015017100CE389524F014C3F8442' "
      },
      {
        "id": 4750,
        "sqlId": "262654979860189396",
        "dip": "192.168.50.75",
        "opType": 29,
        "opObj": "",
        "sqlTemplate": "begin\n  if  :1  =  :2  then\n    sys.dbms_output.disable;\n  el
se\n sys.dbms_output.enable( :3 );\n end if;\nend;\n",
        "dateTime": "2020-01-03 15:21:21",
        "payload": "begin\n  if 1 = 0 then\n    sys.dbms_output.disable;\n  else\n
sys.dbms_output.enable(10000);\n end if;\nend;\n"
      },
      {
        "id": 4749,
        "sqlId": "20170795767163474",
        "dip": "192.168.50.75",
        "opType": 29,
        "opObj": "",
        "sqlTemplate": "begin\n  sys.dbms_output.get_line(line =>  :1 , status =>  :2 )
;\nend;\n",
        "dateTime": "2020-01-03 15:21:21",
        "payload": "begin\n  sys.dbms_output.get_line(line => 'NULL', status =>
'NULL');\nend;\n"
      },
      {
        "id": 4748,
        "sqlId": "254851615248227696",
        "dip": "192.168.50.75",
        "opType": 29,
        "opObj": "",
        "sqlTemplate": "begin  :1  := sys.dbms_transaction.local_transaction_id;
end;\n",
        "dateTime": "2020-01-03 15:21:21",
        "payload": "begin 'NULL' := sys.dbms_transaction.local_transaction_id; end;\n"
      },
      {
        "id": 4744,
        "sqlId": "1743068826118189730",
        "dip": "192.168.50.75",
```

```json
        "opType": 1,
        "opObj": "",
        "sqlTemplate": "select lengthb(nchr( :1 )), nchr( :2 ) from dual\n",
        "dateTime": "2020-01-03 15:21:21",
        "payload": "select lengthb(nchr(20)), nchr(20) from dual\n"
      },
      {
        "id": 4743,
        "sqlId": "58962124245471750",
        "dip": "192.168.50.75",
        "opType": 1,
        "opObj": "",
        "sqlTemplate": "select length(chr( :1 )) l4, length(chr( :2 )) l3,  length(chr(
:3 )) l2, :4 c1 from dual\n",
        "dateTime": "2020-01-03 15:21:21",
        "payload": "select length(chr(2000000000)) l4, length(chr(2000000)) l3,
length(chr(20000)) l2, 'c' c1 from dual\n"
      }
```

`],`

```json
    "totalCount": 3255
  },
  "requestId": "dda75dab-1080-4b27-9a1d-a58a8655c053",
  "requestTotalCost": 22
}
```

##### 获取SQL模板详情

**基本信息**

ID：DescribeSqlTemplateDetail Method：GET URL：/DescribeSqlTemplateDetail.json

**请求参数**

| key | 类型 | 名称 | 必须 | 描述 |
|---|---|---|---|---|
| TemplateId | String | 模板ID | 是 | 模板ID |
| Dip | String | 服务端IP | 是 | 服务端IP |

**返回数据**

| key | 类型 | 描述 |
|---|---|---|

| Data | String | 返回数据 |
|---|---|---|
| Timestamp | String | 执行时间 |

##### 获取SQL模板配置信息

**基本信息**

ID：DescribeSqlTemplateConfig Method：GET URL：/DescribeSqlTemplateConfig.json

**请求参数**

无请求参数

**返回数据**

| key | 类型 | 描述 |
|---|---|---|
| Data | String | 返回数据 |
| Timestamp | String | 时间 |

代码表

## 错误代码表

本文介绍云盾API返回的错误代码信息。 表 1. 云盾通用错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.all.10001 | 权限不够 | 请检查账户权限。 |
| yd.error.all.10002 | 系统错误，请稍后重试 | 请稍后重试。 |
| yd.error.all.10003 | 参数错误 | 请检查请求参数后重试。 |
| yd.error.all.other | 系统异常 | 请稍后重试。 |
| yd.error.all.ConsoleSystemError 1001 _ | 未知异常 | 请稍后重试。 |
| yd.error.all.ConsoleSystemError 1007 _ | API已下线 | 请联系阿里云技术支持人员。 |
| yd.error.all.ConsoleSystemError 1008 _ | postOnly校验失败 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError 1009 _ | csrfToken为空 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError 1010 _ | csrfToken校验失败 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError 1011 _ | regionId为空 | 请检查RegionId请求参数。 |
| yd.error.all.ConsoleSystemError 1012 _ | regionId格式错误 | 请检查RegionId请求参数。 |
| yd.error.all.ConsoleSystemError 1013 _ | 参数为空 | 请检查请求参数后重试。 |
| yd.error.all.ConsoleSystemError 1014 _ | 参数格式错误 | 请检查请求参数后重试。 |

代码表

| yd.error.all.ConsoleNeedLogin | 未登录 | 请检查账户权限。 |
|---|---|---|
| yd.error.all.InvalidApi | 接口异常 | 请稍后重试。 |
| yd.error.all.InvalidParameter | 参数异常 | 请检查请求参数后重试。 |
| yd.error.all.InvalidResult | 返回值异常 | 请稍后重试。 |
| yd.error.all.PropertyConvertFail ed | 转换异常 | 请稍后重试。 |
| yd.error.all.NoPermission | 无权限 | 请检查账户权限。 |
| yd.error.all.ServerError | 服务器异常 | 请稍后重试或联系阿里云技术支持人员。 |
| yd.error.all.UnkownError | 未知异常 | 请稍后重试或联系阿里云技术支持人员。 |

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

代码表

| yd.error.sas.100 | 当前请求失败，建议您刷新页面或者稍后重试 | 请稍后重试。 |
|---|---|---|
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
| yd.error.ddos.IP SEGMENT INV _ _ ALID | IP段不合法，请检查后重新输入 | 请检查请求参数中的IP网段。 |

代码表

| yd.error.ddos.IP SEGMENT REP _ _ EAT | 同一网段不能配置不同区域，请检查后重新输入 | 请检查请求参数中的IP网段。 |
|---|---|---|
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

代码表

| yd.error.ddos.QUERY CODE ER _ _ R | 读取字典异常 | 请稍后重试。 |
|---|---|---|
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

代码表

| yd.error.audit.Receiver.Contact Empty | 【联系方式】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
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
| yd.error.audit.EventType.LogTy peEmpty | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.LogTy pePatternWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.LogSo urceIdNotExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.Reser vedEmpty | 【是否预留】不能为空 | 请检查请求参数后重试。 |

代码表

| yd.error.audit.EventType.Name Empty | 【名称】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
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

代码表

| yd.error.audit.Rule.RiskLevelEm pty | 【风险级别】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.Rule.ReserverEm pty | 【是否预留】不能为空 | 请检查请求参数后重试。 |
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

代码表

| yd.error.audit.LogConfig.LogArc hiveIntervalEmpty | 【日志归档间隔】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.LogConfig.LogArc hiveIntervalPatternWrong | 【日志归档间隔】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventS torePeriodEmpty | 【事件存储周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventS torePeriodLengthWrong | 【事件存储周期】不能超过1095天 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventA rchivePeriodEmpty | 【事件归档周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventA rchivePeriodLengthWrong | 【事件归档周期】不能超过1095天 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventA rchiveIntervalEmpty | 【事件归档间隔】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventA rchiveIntervalPatternWrong | 【事件归档间隔】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.IdNotExi st | 【id】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.TypeEm pty | 【类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.TypePat ternWrong | 【类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.UserIdE mpty | 【用户】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.UserIdL engthWrong | 【用户】长度不成超过500字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.LogType .emtpy | 【日志类型】不能为空 | 请检查请求参数后重试。 |

代码表

| yd.error.audit.LogFilter.LogType PatternWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
|---|---|---|
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
| yd.error.audit.LogSource.Alertt AbleEmpty | 【是否告警】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.TypeP atternWrong | 【类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.Remar kLengthWrong | 【备注】长度不能超过20000字符 | 请检查请求参数后重试。 |

代码表

| yd.error.audit.log.LogSourceIdN otExist | 【日志源】不存在 | 请检查请求参数后重试。 |
|---|---|---|
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

表 7. 云防火墙错误码代码表

| 错误代码 | 错误信息 |
|---|---|
| yd.error.code.200 | 请求成功 |
| yd.error.code.-360100 | 请求方式错误 |
| yd.error.code.-360101 | 认证失败 |
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

代码表

| yd.error.code.-360117 | 目标网段错误，请正确配置目标网段 |
|---|---|
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
| yd.error.code.-360131 | 未知错误 |
| yd.error.code.-360132 | 路由表查找失败 |
| yd.error.code.-360133 | 防火墙ID错误 |
| yd.error.code.-360134 | 防火墙状态错误，请稍后再试 |
| yd.error.code.-360135 | 防火墙开关参数错误，请重新选择 |

代码表

| yd.error.code.-360136 | 防火墙状态参数错误，请重新选择 |
|---|---|
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

代码表

| yd.error.code.-360155 | 网络接口删除超时 |
|---|---|
| yd.error.code.-360156 | 权限不足，请重试 |
| yd.error.code.-360157 | 路由表不存在 |
| yd.error.code.-360158 | 路由条目错误 |
| yd.error.code.-360159 | 路由创建失败 |
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

代码表

| yd.error.code.-360174 | 已配置的VPC防火墙达到最大数量，请购买扩容 |
|---|---|
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
| yd.error.code.-360189 | 删除时ECS不存在 |
| yd.error.code.-360190 | 调用接口失败 |
| yd.error.code.-360191 | 参数错误，请重试 |
| yd.error.code.-360192 | 所属账号错误，请重新输入 |

代码表

| yd.error.code.-360193 | 所属账号未授权，未购买云防火墙 |
|---|---|
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

代码表

| yd.error.code.-360212 | 云企业网VPC数量限制，无法开启VPC边界防火墙 |
|---|---|
| yd.error.code.-360213 | cen未找到 |
| yd.error.code.-360214 | 请求超时，请重试 |
| yd.error.code.-360215 | 参数错误，请重试 |
| yd.error.code.-360216 | IDC专线错误 |
| yd.error.code.-360217 | 防火墙模式错误 |
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

代码表

| yd.error.code.-360312 | 查询IP池失败 |
|---|---|
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
| yd.error.code.-360404 | 物理专线创建失败 |
| yd.error.code.-360405 | 物理专线使能失败 |
| yd.error.code.-360406 | 创建VBR失败 |

代码表

| yd.error.code.-360407 | 更新VBR属性失败 |
|---|---|
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

代码表

| yd.error.code.-193007 | 访问了本地方法 |
|---|---|
| yd.error.code.-193101 | JSON编码失败 |
| yd.error.code.-193102 | JSON解析失败 |
| yd.error.code.-193103 | 解析INT失败 |
| yd.error.code.-193104 | 解析BOOL失败 |
| yd.error.code.-193105 | 解析HTTP BODY失败 |
| yd.error.code.-193201 | 参数不足 |
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

代码表

| yd.error.code.-193309 | 实例的工作模式高于设备的工作模式 |
|---|---|
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
| yd.error.code.-200108 | 请求错误，请稍后重试 |
| yd.error.code.-200109 | 地址簿在使用中，无法删除 |

代码表

| yd.error.code.-200110 | 参数无效 |
|---|---|
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

代码表

| yd.error.code.-200129 | 地址簿数量超出上限 |
|---|---|
| yd.error.code.-200130 | 地址簿数量超出上限 |
| yd.error.code.-200200 | 后台错误 |
| yd.error.code.-200201 | 后台错误 |
| yd.error.code.-200202 | 后台错误 |
| yd.error.code.-200203 | 后台错误 |
| yd.error.code.-200300 | 后台错误 |
| yd.error.code.-200301 | 后台错误 |
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

代码表

| yd.error.code.-210107 | 参数错误，请重试 |
|---|---|
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
| yd.error.code.-230104 | 参数失败 |

代码表

| yd.error.code.-230105 | 策略模板已存在 |
|---|---|
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

代码表

| yd.error.code.-230124 | 策略组回退 |
|---|---|
| yd.error.code.-230125 | 提交信息错误 |
| yd.error.code.-230126 | 没有规则变化，不需要发布 |
| yd.error.code.-230127 | 安全组ID错误 |
| yd.error.code.-230128 | 规则地址铺错误 |
| yd.error.code.-230129 | 规则的网络类型错误，请重选 |
| yd.error.code.-230130 | 规则操作错误 |
| yd.error.code.-230131 | 策略不支持提交 |
| yd.error.code.-230150 | 策略组不存在，请重选 |
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

代码表

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
| ErrorPortAddressGroup.-210303 | get port in address group failed（在群组中获取prot失败） | 在群组中获取prot失败。 |

代码表

| ErrorSourceAddressGroup.- 210304 | get source address in address group failed（在群组中获取源地址失败） | 在群组中获取源地址失败。 |
|---|---|---|
| ErrorSourceAddressRange.- 210306 | source address range error, must be like \"192.168.XX.XX/192.168.XX.X X\"（源地址范围错误，举例： \"192.168.XX.XX/192.168.XX.X X\"） | 源地址范围错误，举例： \"192.168.XX.XX/192.168.XX.X X\"。 |
| ErrorDestAddressGroup.- 210305 | get dest address in address group failed（在群组中获取目的地址失败） | 在群组中获取目的地址失败。 |
| ErrorNoBeaverRules.-210226 | no beaver rules for online（没有对应的beaver rules） | 没有对应的beaver rules。 |
| ErrorDBUpdate.-210121 | internal error: sql update（内部错误：sql update发生错误） | 内部错误：sql update发生错误。 |
| ErrorDBDelete.-210123 | internal error: sql delete（内部错误：sql delete发生错误） | 内部错误：sql delete发生错误。 |
| ErrorMarshalJSON.-210125 | internal error: marshal json（内部错误：marshal json发生错误） | 内部错误：marshal json发生错误。 |
