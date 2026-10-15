---
title: "数据库审计 数据库安全审计开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 100
source_pdf: "33_数据库安全审计开发指南_database-audit-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/dbaudit/zh/database-audit-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 数据库审计 数据库安全审计开发指南

## 快速入门

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
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

## 准备工作

### 登录开发者门户

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。

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
6. 在页面上方的菜单栏，选择**产品** > **开发工具** > **开发者门户**。

### 获取API信息及其EndPoint

通过POP网关调用API需要您了解产品开放API接口的相关信息，本文为您介绍获取云产品的Endpoint的两种方式。

**背景信息**

为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

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
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
apigateway.openapi.endpoint值，即 `Endpoint` 。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey。使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |

| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |
|---|---|

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

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

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

##### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取Accesskey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

##### 请求连接配置

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

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

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

`//`忽略`SSL` `//`忽略`SS`

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
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <your_region_id>，请替换为您实际的地域ID。 <your_access_key_id>，请替换为您实际的AccessKey ID。 <your_access_key_secret>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您实际的产品访问地址。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。

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

##### 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危

**重要**

害您的信息安全。

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

##### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。 产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**说明**

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
```

t th d

```
(h
```

d )

```
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

##### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危

**重要**

害您的阿里云账号的信息安全。 以下代码以ECS为例，展示初始化ecsClient实例。 `//` 初始化`ecsClient`实例

```
ecsClient, err := ecs.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。

##### 发起调用

本文介绍如何使用阿里云产品名Go SDK发起调用。 以下步骤以ECS为例，展示使用ECS Go SDK发起调用。
1. 导入云产品SDK。

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/ecs
```

2. 新建一个产品名Client，该client中包含产品名的所有API。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 `ecsClient,err := <ecs>.NewClientWithAccessKey( //`请替换为您实际的产品名称 `"<yourRegionID>", //` 请替换为您实际的`RegionID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>") //` 请替换为您实际的`AccessKeySecret` `ecsClient.Domain = "ecs.aliyuns.com" //`设置请求域名地址，当前为示例值，请求根据实际请求地址替换。

| xxx.CreateXXXRequest |  | 方法创建一个请求。 |
|---|---|---|
| 法的命名规范为 |  |  |

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

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个 `ClientError` 。 以下以ECS为例，您可以通过以下代码来判断并获取 `ClientError` 中的错误信息：

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" //ecs请替换为您实际的产品名称 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以ECS为例，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息：

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" //ecs请替换为您实际的产品名称 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

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

数

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
| Product | Strin g | 是 | 接口对应的产品名称。取值： Auditprivate：云盾基础组件。 yundunnextsoc：云安全管理中心（SOC）。 Sas：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy：网络流量检测与响应。 Ddosprivate：DDos 清洗。 hsm-private：加密服务。 Cloudfw：云防火墙。 Sddp：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |

数

| EndpointPre | Strin g | 是 | 接口对应的域名前缀。取值： auditprivate：云盾基础组件。 yundunnextsoc-pop：云安全管理中心（SOC）。 tds：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy-share：网络流量检测与响应。 ddosprivate：DDos 清洗。 hsmprivate：加密服务。 cloudfw：云防火墙。 sddp-api：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |
|---|---|---|---|

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

## 数据库审计

### 数据库

#### ListSupportDbTypesForDataSource

调用ListSupportDbTypesForDataSource接口查询数据库审计系统支持的数据库类型。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListSupportDbT ypesForDataSo urce | 接口名，系统规定参数。取值：ListSupportDbTypesForDat aSource。 |
| RegionId | String | 是 | cn-hangzhou | 要查询实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| DbTypes | Array | 无 | 本次请求的数据库的名称组。 |
| └ DbTypeName | String | Mysql | 本次请求的数据库的名称。 |
| └ DbType | Integer | 3 | 数据库类型。 说明具体类型跟您要审计的数据库类型版本有关，需在添加数据库时传入对应的Code值。 |
| └ DbVersions | Array | 无 | 数据库版本组。 |
| └ DbVersionNa me | String | 5.7 | 数据库版本名称。 |
| └ DbVersion | Integer | 5700 | 数据库版本。 说明具体版本跟您要审计的数据库类型版本有关，需在添加数据库时传入对应的code值。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=ListSupportDbTypesForDataSource &RegionId=cn-hangzhou &InstanceId=dbaudit-****
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "DbTypes":[
        {
            "DbVersions":[
                {
                    "DbVersion":5700,
                    "DbVersionName":"5.7"
                }
```

`],`

```json
            "DbType":3,
            "DbTypeName":"Mysql"
        }
```

]

```
}
```

`XML` 格式

```xml
<ListSupportDbTypesForDataSourceResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <DbTypes>
        <info>
            <DbTypeName>Mysql</DbTypeName>
            <DbType>3</DbType>
            <DbVersions>
                <info>
                    <DbVersionName>5.7</DbVersionName>
                    <DbVersion>5700</DbVersion>
                </info>
            </DbVersions>
        </info>
    </DbTypes>
</ListSupportDbTypesForDataSourceResponse>
```

#### ListDataSources

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDataSource s | 接口名，系统规定参数。取值：ListDataSources。 |

| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
|---|---|---|---|---|
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库审计的实例ID。 |
| DbId | Integer | 是 | 1 | 要查询的数据源的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| DataSources | Array | 无 | 数据库列表。 |
| └ DbId | Integer | 1 | 已添加的数据源的ID。 |
| └ DbName | String | 平台库 | 已添加的数据源的名称。 |
| └ DbType | Integer | 3 | 已添加的数据库的类型。 |
| └ DbTypeName | String | Mysql | 已添加的数据库类型的名称。 |
| └ DbVersion | Integer | 5700 | 已添加的数据库的版本。 |
| └ DbVersionNa me | String | 5.7 | 已添加的数据库版本的名称。 |
| └ DbAddress | List | 无 | 数据源地址。 |
| └ CreateTime | String | 2019-06-06 00:00:00 | 数据源的创建日期。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=ListDataSources &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "DataSources":[
        {
            "DbVersion":5700,
            "CreateTime":"2019-06-06 00:00:00",
            "DbId":1,
```

`"DbName":"`平台库`",`

```json
            "DbVersionName":"5.7",
            "DbType":3,
            "DbTypeName":"Mysql"
        }
```

]

```
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <DataSources>
        <info>
            <DbId>1</DbId>
            <DbName>平台库</DbName>
            <DbType>3</DbType>
            <DbTypeName>Mysql</DbTypeName>
            <DbVersion>5700</DbVersion>
            <DbVersionName>5.7</DbVersionName>
            <DbAddresses>
                <info></info>
            </DbAddresses>
            <CreateTime>2019-06-06 00:00:00</CreateTime>
        </info>
    </DataSources>
```

#### CreateDataSource

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDataSou rce | 接口名，系统规定参数。取值：CreateDataSource。 |
| RegionId | String | 是 | cn-hangzhou | 要创建的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要创建的数据库实例的ID。 |
| DbName | String | 是 | 平台库 | 要创建的数据源名称。 |

| DbType | Integer | 是 | 32 | 数据源类型，具体值接口为ListSupportDbTypesForDataSour ce。 |
|---|---|---|---|---|
| DbVersion | Integer | 是 | 6 | 数据源版本，具体值接口为ListSupportDbTypesForDataSour ce。 |
| DbAddresses | String | 是 | 192.168.XX.XX | 数据源IP和端口。多个数据源IP使用英文逗号（,）隔开。 |

**返回数据**

无。

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=CreateDataSource &RegionId=cn-hangzhou &InstanceId=dbaudit-****
```

`&DbName=`平台库

```
&DbType=32 &DbVersion=6 &DbAddresses=192.168.XX.XX
```

正常返回示例 `JSON` 格式

```
{}
```

`XML` 格式

```xml
<CreateDataSourceResponse></CreateDataSourceResponse>
```

#### ModifyDataSource

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDataSou rce | 接口名，系统规定参数。取值：ModifyDataSource。 |
| RegionId | String | 是 | cn-hangzhou | 要修改的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要修改的数据库实例ID。 |
| DbId | Integer | 是 | 1 | 要修改的数据源ID。 |
| DbName | String | 是 | 平台库 | 要修改的数据源名称。 |

| DbVersion | Integer | 是 | 6 | 数据源版本，具体值接口【查询支持的数据源类型列表】。 |
|---|---|---|---|---|
| DbAddresses | String | 是 | 192.168.XX.XX | 数据源IP和端口。多个数据源IP和端口使用英文逗号（,）隔开。 |

**返回数据**

无。

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=ModifyDataSource &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1
```

`&DbName=`平台库

```
&DbVersion=6 &DbAddresses=192.168.XX.XX
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "DataSources":[
        {
            "DbVersion":5700,
            "CreateTime":"2019-06-06 00:00:00",
            "DbId":1,
```

`"DbName":"`平台库`",`

```json
            "DbVersionName":"5.7",
            "DbType":3,
            "DbTypeName":"Mysql"
        }
```

]

```
}
```

{} `XML` 格式

```xml
<ModifyDataSourceResponse></ModifyDataSourceResponse>
```

#### DeleteDataSource

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DeleteDataSou rce | 接口名，系统规定参数。取值：DeleteDataSource。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-hangzhou | 要删除的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要删除的数据库审计的实例ID。 |
| DbId | Integer | 是 | 1 | 要删除的数据源ID。 |

**返回数据**

无。

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=DeleteDataSource &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1
```

正常返回示例 `JSON` 格式

```
{}
```

`XML` 格式

```xml
<DeleteDataSourceResponse></DeleteDataSourceResponse>
```

### Agent

#### GetAgentList

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetAgentList | 接口名，系统规定参数。取值：GetAgentList。 |
| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库审计的实例ID。 |
| AgentIp | String | 否 | 192.168.XX.XX | 要查询的Agent的IP地址。 |

| AgentStatus | String | 否 | 0 | Agent状态。取值： 0：全部。 1：正常。 2：挂起中。 3：主动挂起。 4：超限挂起。 5：唤醒中。 6：中断中。 7：中断。 8：异常。 9：版本异常。 10：认证中。 12：配置中。 13：升级中。 14：升级失败。 15：升级超时。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| AgentList | Array | 无 | Agent列表。 |
| └ AgentIp | String | 192.168.XX.XX | 本次请求的Agent地址。 |
| └ AgentOs | String | redhat6 | Agent的系统类型。 |
| └ AgentVersio n | String | 3.2.5.3 | Agent的版本。 |
| └ AgentCpu | String | 3 | 探针CPU(%)。 |
| └ AgentMem | String | 3 | 探针内存(%)。 |
| └ SendPacketC ount | String | 10000 | 发包总数。 |
| └ SendPackets | String | 100 | 包速率，单位：包/秒。 |

| └ AgentStatus | String | 1 | Agent状态。取值： 0：全部。 1：正常。 2：挂起中。 3：主动挂起。 4：超限挂起。 5：唤醒中。 6：中断中。 7：中断。 8：异常。 9：版本异常。 10：认证中。 12：配置中。 13：升级中。 14：升级失败。 15：升级超时。 |
|---|---|---|---|
| └ FirstLoginTi me | String | 2020-09-01 00:00:00 | 首次登录时间。 |
| └ LastActiveTi me | String | 2020-09-02 00:00:00 | 最后发包时间。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetAgentList &RegionId=cn-hangzhou &InstanceId=dbaudit-****
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
        {
            "AgentOs":"redhat6",
            "AgentStatus":"1",
            "AgentVersion":"3.2.5.3",
            "AgentIp":"192.168.XX.XX",
            "AgentCpu":"3",
            "LastActiveTime":"2020-09-01 00:00:00",
            "SendPackets":"100",
            "AgentMem":"3",
            "SendPacketCount":"10000",
            "FirstLoginTime":"2020-09-01 00:00:00"
        }
```

]

```
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
        <info>
            <SendPacketCount>10000</SendPacketCount>
            <SendPackets>100</SendPackets>
            <FirstLoginTime>2020-09-01 00:00:00</FirstLoginTime>
            <LastActiveTime>2020-09-01 00:00:00</LastActiveTime>
        </info>
```

**错误码**

### 风险规则

#### GetRuleList

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | GetRuleList | 接口名，系统规定参数。取值：GetRuleList。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库审计的实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| RuleGroupLis t | Array | 无 | 规则组的列表。 |
| └ GroupId | Integer | 1001 | 规则组的ID。 |
| └ GroupName | String | 规则组1 | 规则组的名称。 |
| └ RuleList | Array | 无 | 规则列表。 |
| └ RuleId | Integer | 2000001 | 规则的ID。 |
| └ RuleName | String | 批量操作删除 | 规则的名称。 |
| └ RiskLevel | Integer | 3 | 风险级别。 |
| └ RiskType | Integer | 5 | 风险类型。 |
| └ SysDefn | Integer | 0 | 系统默认。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetRuleList &RegionId=cn-hangzhou &InstanceId=dbaudit-****
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "RuleGroupList":[
        {
```

`"GroupName":"`规则组`1",`

```json
            "RuleList":[
                {
                    "SysDefn":"0",
                    "RuleId":"2000001",
                    "RiskLevel":"3",
```

`"RuleName":"`批量操作删除`",`

```json
                    "RiskType":"5"
                }
```

`],`

```json
            "GroupId":"1001"
        }
```

]

```
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <RuleGroupList>
        <info>
            <GroupId>1001</GroupId>
            <GroupName>规则组1</GroupName>
            <RuleList>
                <info>
                    <RuleId>2000001</RuleId>
```

`<RuleName>`批量操作删除`</RuleName>`

```xml
                    <RiskLevel>3</RiskLevel>
                    <RiskType>5</RiskType>
                    <SysDefn>0</SysDefn>
                </info>
            </RuleList>
        </info>
    </RuleGroupList>
```

#### EnableRulesForThisDB

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | EnableRulesFor ThisDB | 接口名，系统规定参数。取值：EnableRulesForThisDB。 |
| RegionId | String | 是 | cn-hangzhou | 要启用的实例所属的地域ID。 |

| InstanceId | String | 是 | dbaudit-**** | 要启用的数据库审计的实例ID。 |
|---|---|---|---|---|
| DbId | Integer | 是 | 1 | 要启用的数据库ID。 |
| RuleIds | String | 是 | 94,106 | 规则ID。多个规则ID使用英文逗号 （,）隔开。 |

**返回数据**

无。

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=EnableRulesForThisDB &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1 &RuleIds=94,106
```

正常返回示例 `JSON` 格式

```
{}
```

`XML` 格式

```xml
<EnableRulesForThisDBResponse></EnableRulesForThisDBResponse>
```

#### DisableRulesForThisDB

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DisableRulesFo rThisDB | 接口名，系统规定参数。取值：DisableRulesForThisDB。 |
| RegionId | String | 是 | cn-hangzhou | 实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 数据库审计的实例ID。 |
| DbId | Integer | 是 | 1 | 数据库ID。 |
| RuleIds | String | 是 | 94,106 | 规则ID。多个规则ID使用英文逗号 （,）隔开。 |

**返回数据**

无。

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=DisableRulesForThisDB &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1 &RuleIds=94,106
```

正常返回示例 `JSON` 格式

```
{}
```

`XML` 格式

```xml
<DisableRulesForThisDBResponse></DisableRulesForThisDBResponse>
```

### 审计

#### GetDBAuditCount

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDBAuditCo unt | 接口名，系统规定参数。取值：GetDBAuditCount。 |
| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库审计的实例ID。 |
| DbId | String | 是 | 1 | 要查询的数据库ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| AuditInfo | Struct | 无 | 审计状况。 |
| └ RunTime | Long | 10000 | 审计时长，单位：毫秒。 |
| └ AuditCount | Long | 20000 | 总审计语句数。 |

| └ SqlCount | Long | 15000 | 可查询在线语句数。 |
|---|---|---|---|
| └ CurrentSqlCo unt | Long | 30000 | 今日语句数。 |
| └ CurrentSessi onCount | Long | 40000 | 今日会话数。 |
| └ CurrentFailS essionCount | Long | 10000 | 今日失败会话数。 |
| └ CurrentRiskC ount | Long | 10000 | 今日风险数。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetDBAuditCount &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "AuditInfo":{
        "SqlCount":10000,
        "CurrentSqlCount":20000,
        "AuditCount":15000,
        "RunTime":30000,
        "CurrentSessionCount":40000,
        "CurrentFailSessionCount":10000,
        "CurrentRiskCount":10000
    }
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <AuditInfo>
        <RunTime>10000</RunTime>
        <AuditCount>20000</AuditCount>
        <SqlCount>15000</SqlCount>
        <CurrentSqlCount>30000</CurrentSqlCount>
        <CurrentSessionCount>40000</CurrentSessionCount>
        <CurrentFailSessionCount>10000</CurrentFailSessionCount>
        <CurrentRiskCount>10000</CurrentRiskCount>
    </AuditInfo>
```

#### GetAuditSearchList

调用GetAuditSearchList接口查询连接数据库时执行的语句被审计的日志列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetAuditSearc hList | 接口名，系统规定参数。取值：GetAuditSearchList。 |
| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库审计的实例ID。 |
| PageNumber | Integer | 是 | 1 | 页码。 |
| PageSize | Integer | 是 | 50 | 分页查询时，每页显示的数据的条数。 默认值：50。 |
| Dbid | String | 是 | 1 | 数据库的ID。 |
| StartTime | String | 否 | 2020-01-01 00:00:00 | 起始时间。 |
| EndTime | String | 否 | 2020-01-01 23:59:59 | 结束时间。 |
| ClientIps | String | 否 | 192.168.XX.XX | 客户端IP。多个客户端IP使用英文逗号 （,）分隔。 |
| DbUsers | String | 否 | root | 数据库用户。多个用户使用英文逗号 （,）分隔。 |
| RiskLevels | String | 否 | 1 | 风险等级。多个风险等级使用英文逗号 （,）分隔。取值： 1：低风险 。 3：中风险。 5：高风险。 |
| KeyWords | String | 否 | select,update | 关键字。多个关键字使用英文逗号（,） 分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| ApiAuditSear chResult | Struct | 无 | 本次查询的结果。 |
| └ FinalSize | Integer | 10000 | 返回结果的总条数，最大10000。 |
| └ Data | Array | 无 | 日志列表。 |
| └ Logsecquenc e | String | 162183812690744 01037 | 日志的关键字。 |
| └ Dbid | String | 1 | 数据库的ID。 |
| └ Writeprepare dsql | String | SELECT*FROM G STATUS LIMIT _ 0,1000 | SQL语句。 |
| └ Capturetime | String | 2020-05-24 14:17:26 | 捕获时间。 |
| └ Dbserver | String | 100.100.XX.XX | 数据库地址。 |
| └ Serverport | String | 3306 | 数据库端口。 |
| └ Dbuser | String | root | 数据库用户。 |
| └ Dbclient | String | 192.168.XX.XX | 客户端的IP地址。 |
| └ Responsecod e | Integer | 0 | DB应答码。 |
| └ Responsetex t | String | 无 | 执行的结果。 |
| └ Affectrows | String | 100 | 影响行数。 |
| └ Execcostus | String | 323 | 响应时间，单位：微妙。 |
| └ Fetchcostus | String | 323 | 语句总耗时，单位：微妙。 |
| └ Clientmac | String | 0EB6EF12**** | MAC地址。 |
| └ Programnm | String | libmysql | 工具或应用。 |
| └ Sid | String | test | OS用户。 |
| └ Machinenam e | String | compute-internal | 主机的名称。 |

| └ Sessionid | String | 106288711982206 1570 | 会话标识。 |
|---|---|---|---|
| └ Logintime | String | 2020-05-24 14:17:15 | 会话开始时间。 |
| └ Logouttime | String | 2020-05-24 15:05:27 | 会话结束时间。 |
| └ RiskLevel | String | 1 | 风险等级。多个风险等级使用英文逗号（,）分隔。取值： 1：低风险 。 3：中风险。 5：高风险。 |
| └ Appusernam e | String | user1 | 应用用户名称。 |
| └ Appclientip | String | 111.164.XX.XX | 应用客户端的IP地址。 |
| └ DbName | String | SCHEMA | 数据库的名称。 |
| └ Dbinstancen ame | String | INS | 实例名称。 |
| └ Dbsessionid | String | 0E320477 | 数据库会话标识。 |
| └ RelatedRule Name | String | 信任语句 | 所属语句的规则。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetAuditSearchList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root &RiskLevels=1,3,5 &KeyWords=select,update
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiAuditSearchResult":{
        "FinalSize":10000,
        "Data":[
            {
                "Dbsessionid":"0E320477",
                "Machinename":"compute-internal",
                "Dbuser":"root",
                "Programnm":"libmysql",
                "Logintime":"2020-05-24 14:17:15",
                "Logouttime":"2020-05-24 15:05:27",
                "Dbserver":"100.100.XX.XX",
                "Responsecode":"0",
                "Logsecquence":"16218381269074401037",
                "Dbid":"1",
                "DbName":"SCHEMA",
                "Appusername":"user1",
                "Dbinstancename":"INS",
```

`"RelatedRuleName":"`信任语句`",`

```json
                "Capturetime":"2020-05-24 14:17:26",
                "Execcostus":"323",
                "Fetchcostus":"323",
                "Dbclient":"192.168.XX.XX",
                "Responsetext":"",
                "Serverport":"3306",
                "Writepreparedsql":"SELECT*FROM G_STATUS LIMIT 0,1000",
                "Sid":"test",
                "Clientmac":"0EB6EF124C47",
                "Affectrows":"100",
                "Appclientip":"111.164.XX.XX",
                "Sessionid":"0E320477",
                "RiskLevel":"1"
            }
```

]

```
    }
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiAuditSearchResult>
        <FinalSize>10000</FinalSize>
        <Data>
            <info>
                <Logsecquence>16218381269074401037</Logsecquence>
                <Dbid>1</Dbid>
                <Writepreparedsql>SELECT*FROM G_STATUS LIMIT 0,1000</Writepreparedsql>
                <Capturetime>2020-05-24 14:17:26</Capturetime>
                <Dbserver>100.100.XX.XX</Dbserver>
                <Serverport>3306</Serverport>
                <Dbuser>root</Dbuser>
                <Dbclient>192.168.XX.XX</Dbclient>
                <Responsecode>0</Responsecode>
                <Responsetext></Responsetext>
                <Affectrows>100</Affectrows>
                <Execcostus>323</Execcostus>
                <Fetchcostus>323</Fetchcostus>
                <Clientmac>0EB6EF124C47</Clientmac>
                <Programnm>libmysql</Programnm>
                <Sid>test</Sid>
                <Machinename>compute-internal</Machinename>
                <Sessionid>1062887119822061570</Sessionid>
                <Logintime>2020-05-24 14:17:15</Logintime>
                <Logouttime>2020-05-24 15:05:27</Logouttime>
                <RiskLevel>0</RiskLevel>
                <Appusername>user1</Appusername>
                <Appclientip>111.164.XX.XX</Appclientip>
                <DbName>SCHEMA</DbName>
                <Dbinstancename>INS</Dbinstancename>
                <Dbsessionid>0E320477</Dbsessionid>
                <RelatedRuleName>信任语句</RelatedRuleName>
            </info>
        </Data>
    </ApiAuditSearchResult>
```

#### GetFailedSqlList

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetFailedSqlLis t | 接口名，系统规定参数。取值：GetFailedSqlList。 |
| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库审计的实例ID。 |

| PageNumber | Integer | 是 | 1 | 页码。 |
|---|---|---|---|---|
| PageSize | Integer | 是 | 50 | 分页查询时，每页显示的数据的条数。 默认值：50。 |
| Dbid | String | 是 | 1 | 数据库ID。 |
| StartTime | String | 否 | 2020-01-01 00:00:00 | 起始时间。 |
| EndTime | String | 否 | 2020-01-01 23:59:59 | 结束时间。 |
| ClientIps | String | 否 | 192.168.XX.XX | 客户端IP。多个客户端IP使用英文逗号 （,）分隔。 |
| DbUsers | String | 否 | root | 数据库用户。多个数据库用户使用英文逗号（,）分隔。 |
| AckNum | Integer | 否 | 100002 | 错误号。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| ApiAuditSear chResult | Struct | 无 | 查询结果。 |
| └ FinalSize | Integer | 10000 | 结果总条数，最大10000。 |
| └ Data | Array | 无 | 日志列表。 |
| └ Logsecquenc e | String | 162183812690744 01037 | 语句标识。 |
| └ Dbid | String | 1 | 数据库ID。 |
| └ Writeprepare dsql | String | SELECT*FROM G STATUS LIMIT _ 0,1000 | SQL语句。 |
| └ Capturetime | String | 2020-05-24 14:17:26 | 捕获时间。 |
| └ Dbserver | String | 100.100.XX.XX | 数据库地址。 |
| └ Serverport | String | 3306 | 数据库端口。 |
| └ Dbuser | String | root | 数据库用户。 |
| └ Dbclient | String | 192.168.XX.XX | 客户端IP。 |

| └ Responsecod e | Integer | 1001 | DB的应答码。 |
|---|---|---|---|
| └ Responsetex t | String | Table G STATUS _ doesn't exist | 执行结果。 |
| └ Clientmac | String | 0EB6EF124C47 | MAC地址。 |
| └ Programnm | String | libmysql | 工具或应用。 |
| └ Sid | String | test | OS用户。 |
| └ Sessionid | String | 106288711982206 1570 | 会话标识。 |
| └ Logintime | String | 2020-05-24 14:17:15 | 会话开始时间。 |
| └ Logouttime | String | 2020-05-24 15:05:27 | 会话结束时间。 |
| └ Appusernam e | String | user1 | 应用用户。 |
| └ Appclientip | String | 111.164.XX.XX | 应用客户端IP。 |
| └ DbName | String | SCHEMA | 数据库名称。 |
| └ Dbinstancen ame | String | INS | 服务（实例）名。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetFailedSqlList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root &AckNum=100002
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiAuditSearchResult":{
        "FinalSize":10000,
        "Data":[
            {
                "Dbuser":"root",
                "Dbclient":"192.168.XX.XX",
                "Responsetext":"Table G_STATUS doesn't exist",
                "Serverport":"3306",
                "Writepreparedsql":"SELECT*FROM G_STATUS LIMIT 0,1000",
                "Sid":"test",
                "Clientmac":"0EB6EF124C47",
                "Programnm":"libmysql",
                "Logintime":"2020-05-24 14:17:15",
                "Logouttime":"2020-05-24 15:05:27",
                "Dbserver":"100.100.XX.XX",
                "Responsecode":"1001",
                "Logsecquence":"16218381269074401037",
                "Dbid":"1",
                "DbName":"SCHEMA",
                "Appusername":"user1",
                "Appclientip":"111.164.XX.XX",
                "Dbinstancename":"INS",
                "Capturetime":"2020-05-24 14:17:26",
                "Sessionid":"1062887119822061570"
            }
```

]

```
    }
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiAuditSearchResult>
        <FinalSize>10000</FinalSize>
        <Data>
            <info>
                <Logsecquence>16218381269074401037</Logsecquence>
                <Dbid>1</Dbid>
                <Writepreparedsql>SELECT*FROM G_STATUS LIMIT 0,1000</Writepreparedsql>
                <Capturetime>2020-05-24 14:17:26</Capturetime>
                <Dbserver>100.100.100.81</Dbserver>
                <Serverport>3306</Serverport>
                <Dbuser>root</Dbuser>
                <Dbclient>192.168.XX.XX</Dbclient>
                <Responsecode>1001</Responsecode>
                <Responsetext>Table G_STATUS doesn't exist</Responsetext>
                <Clientmac>0EB6EF124C47</Clientmac>
                <Programnm>libmysql</Programnm>
                <Sid>test</Sid>
                <Sessionid>1062887119822061570</Sessionid>
                <Logintime>2020-05-24 14:17:15</Logintime>
                <Logouttime>2020-05-24 15:05:27</Logouttime>
                <Appusername>user1</Appusername>
                <Appclientip>111.164.XX.XX</Appclientip>
                <DbName>SCHEMA</DbName>
                <Dbinstancename>INS</Dbinstancename>
            </info>
        </Data>
    </ApiAuditSearchResult>
```

#### GetSessionSearchList

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetSessionSea rchList | 接口名，系统规定参数。取值：GetSessionSearchList。 |
| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库审计的实例ID。 |
| PageNumber | Integer | 是 | 1 | 页码。 |
| PageSize | Integer | 是 | 50 | 分页查询时，每页显示的数据的条数。 默认值：50。 |
| Dbid | String | 是 | 1 | 数据库的ID。 |

| StartTime | String | 否 | 2020-01-01 00:00:00 | 起始时间。 |
|---|---|---|---|---|
| EndTime | String | 否 | 2020-01-01 23:59:59 | 结束时间。 |
| ClientIps | String | 否 | 192.168.XX.XX | 客户端IP。多个客户端IP使用英文逗号 （,）分隔。 |
| DbUsers | String | 否 | root | 数据库用户。多个数据库用户使用英文逗号（,）分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| ApiAuditSear chResult | Struct | 无 | 本次查询的结果。 |
| └ FinalSize | Integer | 10000 | 结果总条数，最大10000。 |
| └ Data | Array | 无 | 日志列表。 |
| └ Sessionid | String | 106288711982206 1570 | 日志的关键字。 |
| └ Dbserver | String | 100.100.XX.XX | 数据库地址。 |
| └ Serverport | String | 3306 | 数据库端口。 |
| └ Dbuser | String | root | 数据库用户。 |
| └ Dbclient | String | 192.168.XX.XX | 客户端的IP地址。 |
| └ Clientmac | String | 0EB6EF12**** | MAC地址。 |
| └ Programnm | String | libmysql | 工具或应用。 |
| └ Sid | String | test | OS用户。 |
| └ Logintime | String | 2020-05-24 14:00:00 | 会话开始时间。 |
| └ Logouttime | String | 2020-05-24 15:00:00 | 会话结束时间。 |
| └ Statetime | String | 60 | 停留时间。单位：分钟。 |
| └ Dback | String | 0 | 应答错误号。 |
| └ Dbackmessa ge | String | 无 | 登录信息。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetSessionSearchList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiSessionSearchResult":{
        "FinalSize":10000,
        "Data":[
            {
                "Dback":"0",
                "Dbuser":"root",
                "Dbclient":"192.168.XX.XX",
                "Serverport":"3306",
                "Sid":"test",
                "Clientmac":"0EB6EF124C47",
                "Programnm":"libmysql",
                "Logintime":"2020-05-24 14:00:00",
                "Logouttime":"2020-05-24 15:00:00",
                "Statetime":"60",
                "Dbackmessage":"",
                "Dbserver":"100.100.XX.XX",
                "Sessionid":"1062887119822061570"
            }
```

]

```
    }
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiSessionSearchResult>
        <FinalSize>10000</FinalSize>
        <Data>
            <info>
                <Sessionid>1062887119822061570</Sessionid>
                <Dbserver>100.100.XX.XX</Dbserver>
                <Serverport>3306</Serverport>
                <Dbuser>root</Dbuser>
                <Dbclient>192.168.XX.XX</Dbclient>
                <Clientmac>0EB6EF124C47</Clientmac>
                <Programnm>libmysql</Programnm>
                <Sid>test</Sid>
                <Logintime>2020-05-24 14:00:00</Logintime>
                <Logouttime>2020-05-24 15:00:00</Logouttime>
                <Statetime>60</Statetime>
                <Dback>0</Dback>
                <Dbackmessage></Dbackmessage>
            </info>
        </Data>
    </ApiSessionSearchResult>
```

#### GetFailedSessionList

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetFailedSessi onList | 接口名，系统规定参数。取值：GetFailedSessionList。 |
| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库实例ID。 |
| PageNumber | Integer | 是 | 1 | 页码。 |
| PageSize | Integer | 是 | 50 | 分页查询时，每页显示的数据的条数。 默认值：50。 |
| Dbid | String | 是 | 1 | 要查询的数据库的ID。 |
| StartTime | String | 否 | 2020-01-01 00:00:00 | 会话的起始时间。 |
| EndTime | String | 否 | 2020-01-01 23:59:59 | 会话的结束时间。 |
| ClientIps | String | 否 | 192.168.XX.XX | 客户端IP。多个客户端IP使用英文逗号 （,）分隔。 |

| DbUsers | String | 否 | root | 数据库用户。多个数据库用户使用英文逗号（,）分隔。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| SessionList | Array | 无 | 会话列表。 |
| └ Sessionid | String | 106288711982206 1570 | 会话的关键字。 |
| └ Dbserver | String | 100.100.XX.XX | 数据库地址。 |
| └ Serverport | String | 3306 | 数据库端口。 |
| └ Dbuser | String | root | 数据库用户。 |
| └ Dbclient | String | 192.168.XX.XX | 客户端的IP地址。 |
| └ Clientmac | String | 0EB6EF12**** | MAC地址。 |
| └ Programnm | String | libmysql | 工具或应用。 |
| └ Sid | String | test | OS用户。 |
| └ Connecttime | String | 2020-05-24 14:00:00 | 连接时间。 |
| └ Dback | String | 1045 | 应答错误号。 |
| └ Dbackmessa ge | String | Access denied for user 'root'@ (using password: YES) | 登录信息。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetFailedSessionList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "SessionList":[
        {
            "Clientmac":"0EB6EF12****",
            "Programnm":"libmysql",
            "Dbackmessage":"Access denied for user 'root'@ (using password: YES)",
            "Dbserver":"100.100.XX.XX",
            "Dback":"1045",
            "Dbuser":"root",
            "Dbclient":"192.168.XX.XX",
            "Sessionid":"1062887119822061570",
            "Serverport":"3306",
            "Connecttime":"2020-05-24 14:00:00",
            "Sid":"test"
        }
```

]

```
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <SessionList>
        <info>
            <Sessionid>1062887119822061570</Sessionid>
            <Dbserver>100.100.XX.XX</Dbserver>
            <Serverport>3306</Serverport>
            <Dbuser>root</Dbuser>
            <Dbclient>192.168.XX.XX</Dbclient>
            <Clientmac>0EB6EF12****</Clientmac>
            <Programnm>libmysql</Programnm>
            <Sid>test</Sid>
            <Connecttime>2020-05-24 14:00:00</Connecttime>
            <Dback>1045</Dback>
            <Dbackmessage>Access denied for user 'root'@ (using password: YES)
</Dbackmessage>
        </info>
    </SessionList>
```

#### GetRiskSqlSearchList

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRiskSqlSear chList | 接口名，系统规定参数。取值：GetRiskSqlSearchList。 |

| RegionId | String | 是 | cn-hangzhou | 要查询的实例所属的地域ID。 |
|---|---|---|---|---|
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库实例ID。 |
| PageNumber | Integer | 是 | 1 | 分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。 |
| PageSize | Integer | 是 | 50 | 分页查询时，每页显示的数据的条数。 默认值：50。 |
| Dbid | String | 是 | 1 | 数据库的ID。 |
| StartTime | String | 否 | 2020-01-01 00:00:00 | 设置查询的起始时间。 |
| EndTime | String | 否 | 2020-01-01 23:59:59 | 设置查询的结束时间。 |
| ClientIps | String | 否 | 192.168.XX.XX | 客户端IP。多个客户端IP使用英文逗号 （,）分隔。 |
| DbUsers | String | 否 | root | 数据库用户。多个数据库用户使用英文逗号（,）分隔。 |
| RiskLevels | String | 否 | 1 | SQL的风险等级。多个风险等级使用英文逗号（,）分隔。取值： 1：低风险。 3：中风险。 5：高风险。 |
| RiskTypes | String | 否 | 5 | SQL的风险类型。多个风险类型使用英文逗号（,）分隔。取值： 2：敏感语句 。 3：注入攻击。 4：漏洞攻击。 5：操作规则。 6：访问规则。 7：口令攻击。 |
| RuleName | String | 否 | 批量查询规则1 | 执行SQL语句命中的风险规则的名称。 |
| ExcuteResult | String | 否 | 0 | SQL语句的执行结果。取值： 0：失败。 1：成功。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| ApiAuditSear chResult | Struct | 无 | 本次查询的结果。 |

| └ FinalSize | Integer | 10000 | 本次查询结果的总条数，最大10000。 |
|---|---|---|---|
| └ Data | Array | 无 | 本次查询的日志列表。 |
| └ Logsecquenc e | String | 162183812690744 01037 | 日志的关键字。 |
| └ Dbid | String | 1 | 本次查询的数据库的ID。 |
| └ Writeprepare dsql | String | SELECT*FROM G STATUS LIMIT _ 0,1000 | 本次查询的SQL语句。 |
| └ Capturetime | String | 2020-05-24 14:17:26 | 本次查询的时间。 |
| └ RiskType | String | 5 | SQL的风险类型。多个风险类型使用英文逗号 （,）分隔。取值： 2：敏感语句 。 3：注入攻击。 4：漏洞攻击。 5：操作规则。 6：访问规则。 7：口令攻击。 |
| └ RuleName | String | 批量查询规则1 | 执行SQL语句后命中的风险规则的名称。 |
| └ RiskLevel | String | 1 | SQL的风险等级。多个风险等级使用英文逗号 （,）分隔。取值： 1：低风险。 3：中风险。 5：高风险。 |
| └ Dbserver | String | 100.100.XX.XX | 数据库地址。 |
| └ Serverport | String | 3306 | 数据库端口。 |
| └ Dbuser | String | root | 数据库用户。 |
| └ Dbclient | String | 192.168.XX.XX | 客户端IP。 |
| └ Responsetex t | String | 0 | SQL语句的执行结果。取值： 0：失败。 1：成功。 |
| └ Affectrows | String | 1000 | SQL语句影响的行数。 |
| └ Programnm | String | libmysql | 连接数据库用的工具。 |
| └ Appusernam e | String | user1 | 应用的用户名称。 |
| └ Appclientip | String | 111.164.XX.XX | 应用客户端IP。 |

| └ Dbinstancen ame | String | INS | 实例名称。 |
|---|---|---|---|

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetRiskSqlSearchList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root &RiskLevels=1,3,5 &RiskTypes=5
```

`&RuleName=`批量查询规则1

```
&ExcuteResult=0
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiRiskSearchResult":{
        "FinalSize":10000,
        "Data":[
            {
                "Dbuser":"root",
                "Dbclient":"192.168.XX.XX",
                "Responsetext":"",
                "Serverport":"3306",
                "Writepreparedsql":"SELECT*FROM G_STATUS LIMIT 0,1000",
                "Programnm":"libmysql",
                "Affectrows":"1000",
                "Dbserver":"100.100.100.81",
                "Logsecquence":"16218381269074401037",
                "Dbid":"1",
                "Appusername":"user1",
                "Appclientip":"111.164.XX.XX",
                "Dbinstancename":"INS",
                "Capturetime":"2020-05-24 14:17:26",
                "RiskLevel":"1",
                "RiskType":"5",
```

`"RuleName":"`批量查询规则`1"`

```
            }
```

]

```
    }
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiRiskSearchResult>
        <FinalSize>10000</FinalSize>
        <Data>
            <info>
                <Logsecquence>16218381269074401037</Logsecquence>
                <Dbid>1</Dbid>
                <Writepreparedsql>SELECT*FROM G_STATUS LIMIT 0,1000</Writepreparedsql>
                <Capturetime>2020-05-24 14:17:26</Capturetime>
                <RiskType>5</RiskType>
```

`<RuleName>`批量查询规则`1</RuleName>`

```xml
                <RiskLevel>1</RiskLevel>
                <Dbserver>100.100.XX.XX</Dbserver>
                <Serverport>3306</Serverport>
                <Dbuser>root</Dbuser>
                <Dbclient>192.168.XX.XX</Dbclient>
                <Responsetext>0</Responsetext>
                <Affectrows>1000</Affectrows>
                <Programnm>libmysql</Programnm>
                <Appusername>user1</Appusername>
                <Appclientip>111.164.XX.XX</Appclientip>
                <Dbinstancename>INS</Dbinstancename>
            </info>
        </Data>
    </ApiRiskSearchResult>
```

#### GetRiskBitsList

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRiskBitsList | 接口名，系统规定参数。取值：GetRiskBitsList。 |
| RegionId | String | 是 | cn-hangzhou | 要查询的服务器的地域ID。 |
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库实例ID。 |
| Dbid | String | 是 | 1 | 要查询的数据库ID。 |
| StartTime | String | 否 | 2020-01-01 00:00:00 | 设置查询的起始时间。 |
| EndTime | String | 否 | 2020-01-01 23:59:59 | 设置查询的结束时间。 |

| RiskLevel | String | 否 | 5 | 风险等级。取值： 1：低风险。 3：中风险。 5：高风险。 |
|---|---|---|---|---|
| RiskType | String | 否 | 5 | 风险类型。取值： 2：敏感语句。 3：注入攻击。 4：漏洞攻击。 5：操作规则。 6：访问规则。 7：口令攻击。 |
| RuleName | String | 否 | 批量操作删除规则1 | 规则的名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| ApiRiskHitLis t | Array | 无 | 风险命中列表。 |
| └ RuleId | String | 2000001 | 规则的ID。 |
| └ RuleName | String | 批量操作删除规则1 | 规则的名称。 |
| └ RiskType | String | 5 | 风险类型。多个风险类型使用英文逗号（,）分隔。取值： 2：敏感语句 。 3：注入攻击。 4：漏洞攻击。 5：操作规则。 6：访问规则。 7：口令攻击。 |
| └ RiskLevel | String | 1 | 风险等级。多个风险等级使用英文逗号（,）分隔。取值： 1：低风险。 3：中风险。 5：高风险。 |
| └ HitCount | String | 35 | 风险命中的数量。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetRiskBitsList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &RiskLevel=5 &RiskType=5
```

`&RuleName=`批量操作删除规则1 正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiRiskHitList":[
        {
            "HitCount":"35",
            "RuleId":"2000001",
            "RiskLevel":"1",
```

`"RuleName":"`批量操作删除规则`1",`

```json
            "RiskType":"5"
        }
```

]

```
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiRiskHitList>
        <info>
            <RuleId>2000001</RuleId>
```

`<RuleName>`批量操作删除规则`1</RuleName>`

```xml
            <RiskType>5</RiskType>
            <RiskLevel>1</RiskLevel>
            <HitCount>35</HitCount>
        </info>
    </ApiRiskHitList>
```

#### GetApiSearchConditionResult

调用GetApiSearchConditionResult接口查询语句检索可用的检索条件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetApiSearchC onditionResult | 接口名，系统规定参数。取值：GetApiSearchConditionResult |

| RegionId | String | 是 | cn-hangzhou | 要查询的服务器的地域ID。 |
|---|---|---|---|---|
| InstanceId | String | 是 | dbaudit-**** | 要查询的数据库实例ID。 |
| Dbid | String | 是 | 1 | 要查询的数据库ID。 |
| StartTime | String | 否 | 2020-01-01 00:00:00 | 设置查询的起始时间。 |
| EndTime | String | 否 | 2020-01-01 23:59:59 | 设置查询的结束时间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | 本次请求的ID。 |
| Conditions | Struct | 无 | 本次查询的结果。 |
| └ DbClientList | List | 192.168.XX.XX | 客户端IP。 |
| └ DbUserList | List | root | 数据库用户。 |

**示例**

请求示例

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetApiSearchConditionResult &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &Dbid=1
```

正常返回示例 `JSON` 格式

```json
{
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "Conditions":[
      {
        "DbClientList":"192.168.XX.XX",
        "DbUserList":"root",
      }
}
```

`XML` 格式

```xml
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Conditions>
        <DbClientList>
            <info>192.168.XX.XX</info>
        </DbClientList>
        <DbUserList>
            <info>root</info>
        </DbUserList>
    </Conditions>
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

| 数据库安全审计开发指南·错误代码表 |  |  |
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
