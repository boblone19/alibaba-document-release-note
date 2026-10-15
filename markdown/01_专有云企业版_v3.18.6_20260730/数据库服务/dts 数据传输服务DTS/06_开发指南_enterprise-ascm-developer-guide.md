---
title: "数据传输服务DTS 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 493
source_pdf: "06_开发指南_enterprise-ascm-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/dts/zh/enterprise-ascm-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 数据传输服务DTS 开发指南

数据传输

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
2. 根据专有云的版本单击**企业版**、**敏捷版**或**一体机**标签。
数据传输
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

数据传输

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
数据传输

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
3. 单击**账号登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：
管理员强制开启MFA后的首次登录： a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**账号登录**。 c. 输入6位MFA码后单击**认证**。 您已开启并绑定MFA： 输入6位MFA码后单击**认证**。
5. 在页面顶部的菜单栏中，选择**产品** > **开发工具** **> API****与工具** > **开发者门户**。

### 获取API信息及其EndPoint

您在使用SDK时，需要获取产品名称、API名称和API版本。本文介绍如何查看API信息。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** **> API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
数据传输
4. 在左上角的
中，选择**数据库** > **数据传输服务** **DTS**
5. 在**版本**下拉列表中，选择目标API版本。
在下方API列表中可浏览当前版本的所有API接口。
6. 选中对应的接口，在**参数名**页签可以获取**Endpoint**信息。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》章节。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》章节。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。
数据传输 Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
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
数据传输

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com> ，请替换为实际的STS Endpoint。 数据传输

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
数据传输

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

数据传输

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

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以DTS为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**数据库**>**数据传输服务** **DTS** 。
3. 在页面中心，选择实例所在**组织**和**地域**，单击**管理员权限访问**。
4. 在左侧导航栏，单击目标服务，在页面右侧查看对应服务的**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。 数据传输

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 获取DTS的Endpoint

**背景信息**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。您也可以通过如下方法自行获取Endpoint。

**操作步骤**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏中，选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏中，选择**运维工具** > **服务注册变量大盘**。
4. 在**服务注册变量大盘**页面，在搜索框选择**服务**并输入 `dts-dts` 。
5. 在 `dts-dts` 服务的**Service Registration**列中，单击
图标展示隐藏的内容，然后单击该内容。 在弹出的**注册变量**对话框中，查看**dts.openapi.endpoint**的值，即 `Endpoint` 。 数据传输

## Java SDK调用示例

### 快速开始

本节介绍如何获取DTS Java SDK并开始调用。 使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。参见获取AccessKey在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云 Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用DTS的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17及以上版本，SDK的版本为5.1.25。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Product>，请替换为您实际的产品名称。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <readTimeout>，请您根据实际情况设置读取超时时间，单位为毫秒。 <connectionTimeout>，请您根据实际情况设置连接超时时间，单位为毫秒。 <maxRequestsPerHost>，请您根据实际情况设置每个主机的最大请求数。 <maxRequests>，请您根据实际情况设置最大请求数。 <http://192.168.XX:33XX>，请替换为您实际的代理IP+端口。 数据传输

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dts.model.v20180801.*; public class CreateMigrationJob {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", "<>", "<>")
;
        IAcsClient client = new DefaultAcsClient(profile);
        CreateMigrationJobRequest request = new CreateMigrationJobRequest();
        request.setRegionId("cn-hangzhou");
        request.setRegion("cn-hangzhou");
        request.setMigrationJobClass("large");
        try {
            CreateMigrationJobResponse response = client.getAcsResponse(request);
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

#### 安装Java SDK

本文介绍如何安装及调用DTS Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用DTS的开发工具包，必须安装阿里云Java SDK核心库以及DTS Java SDK。SDK核心库推荐使用 4.5.17及以上版本，Java SDK的版本为5.1.25。 以使用DTS Java SDK为例，您需要安装阿里云Java SDK核心库和DTS Java SDK，并在pom.xml文件中添加以下依赖即可。准确的SDK版本号，请参见SDK中心。 数据传输

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- dts java sdk --> <dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-dts</artifactId>
  <version>5.1.25</version>
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

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。 数据传输

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

本文介绍如何使用DTS Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例如CreateMigrationJob。 在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。 数据传输

```
CreateMigrationJobRequest request = new CreateMigrationJobRequest();
```

`//` 业务参数

```
request.setRegion("cn-hangzhou"); request.setMigrationJobClass("large");
```

`//` 设置地域和迁移规格
3. 发起调用并处理应答。

```java
try {
    CreateMigrationJobResponse response = client.getAcsResponse(request);
    System.out.println(new Gson().toJson(response));
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    System.out.println("ErrCode:" + e.getErrCode());
    System.out.println("ErrMsg:" + e.getErrMsg());
    System.out.println("RequestId:" + e.getRequestId());
}
```

正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 `response.getXXX()` 来获得应答中的字段。

```
instanceStatus := response.getStatus();
```

如果出现了异常，或您需要原始HTTP应答的情况下，您可以通过以使用 `doAction()` 来获取原始应答。

```
HttpResponse response = client.doAction(request);
```

#### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码： 数据传输

```
try {
    FooResponse response = client.getAcsResponse(request);
```

`//` 处理`Response`

```
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

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。 例如CreateMigrationJob接口，在发起CommonRequest请求时，需要使用 `request.setSysAction("CreateMigrationJob")` 来指定API名称。

**示例：调用RPC风格的API**

数据传输以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
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
        request.setDomain("dts.aliyuncs.com");
        request.setSysProduct("Dts");
        request.setVersion("2020-01-01");
        request.setAction("CreateMigrationJob");
        request.putQueryParameter("Region", "cn-hangzhou");
        request.putQueryParameter("MigrationJobClass", "large");
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

源说明 "<yourRegionID>");//非必填(企业版

```
requestputHeadParameter("x-acs-regionid"
```

数据传输

```
        request.putHeadParameter(xacsregionid, <yourRegionID>);// 非必填(企业版
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

数据传输

## Python SDK调用示例

### 快速开始

本节介绍如何获取DTS Python SDK并开始调用。

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
以下以安装数据传输DTS的SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装数据传输DTS的SDK：

```
pip install aliyun-python-sdk-dts
```

如果您使用的是Python 3.x，执行以下命令，安装数据传输DTS的SDK：

```
pip3 install aliyun-python-sdk-dts
```

**使用Python SDK**

以下示例以DTS为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中尖括号（<>）部分可变参数，均需替换为您实际的相关信息，尖括号

**说明**

（<>）在最终代码中不保留。 数据传输

```
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdts.request.v20200101.CreateMigrationJobRequest import CreateMigrationJobRequest credentials = AccessKeyCredential('<您的AccessKey ID>', '<您的AccessKey Secret>')
```

# 使用`STS Token`时使用如下语句

```python
# credentials = StsTokenCredential('<您的AccessKey ID>', '<您的AccessKey Secret>', '<
您的STS TOKEN>') client = AcsClient(region_id='<您的地域ID>', credential=credentials) request = CreateMigrationJobRequest() request.set_accept_format('json') request.set_Region("cn-hangzhou") request.set_MigrationJobClass("large") response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### 使用手册

#### 安装Python SDK

本文档介绍如何安装及调用DTS Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。 使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用DTS

**说明**

的Python SDK，您需要安装阿里云Python SDK核心库和DTS的Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

安装云产品的SDK，以下以安装DTS的SDK为例。 如果您使用的是Python 2.x，执行以下命令，安装ECS的SDK：

```
pip install aliyun-python-sdk-dts
```

如果您使用的是Python 3.x，执行以下命令，安装ECS的SDK：

```
pip3 install aliyun-python-sdk-dts
```

数据传输

#### 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危

**重要**

害您的信息安全。

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。 产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**说明**

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。OpenSSL支持TLS1.2及以上版本。 运行 `python -c "import ssl"` 检查Python环境是否支持OpenSSL。运行后，如果没有出现 `ImportError: No module named ssl` 的错误信息，说明已经支持OpenSSL。 若没有OpenSSL，运行以下命令安装：

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

#### 发起调用

本节介绍如何使用DTS Python SDK发起请求。

**操作步骤**

数据传输
1. 导入相关产品的SDK。

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdts.request.v20200101.CreateMigrationJobRequest import CreateMigrationJobRequest
```

2. 新建一个AcsClient。

```
credentials = AccessKeyCredential('<your-access-key-id>', '<your-access-key-secret>') client = AcsClient(region_id='cn-hangzhou', credential=credentials)
```

3. 创建Request对象。

```
request = CreateMigrationJobRequest() request.set_accept_format('json')
```

4. 发起调用并处理返回。

```python
response = client.do_action_with_exception(request) print(str(response, encoding='utf-8'))
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

#### 使用CommonRequest进行调用

数据传输当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.set_action_name('Action')` 的方式来指定API名称。 例如CreateMigrationJob接口，在发起CommonRequest请求时，需要使用 `request.set_action_name('CreateMigrationJob')` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为数据传输DTS的CreateMigrationJob接口，购买迁移实例的调用示例：

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <dts.aliyuncs.com>，请替换为您实际的产品访问地址。 数据传输

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`。

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Dts') request.set_action_name('CreateMigrationJob') request.set_version('2020-01-01')
```

`request.set_domain('<dts.aliyuncs.com>') #`产品访问域名,当前为示例值,请替换为您实际的产品访问地址 。

```bash
# or:
# request = = CommonRequest(product='Dts',
action_name='CreateMigrationJob',version='2020-01-01',domain='dts.aliyuncs.com')
######
```

# 设置请求协议类型,支持`https`或`http,`默认为`http`。
# 设置`https`方法如下：

```bash
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('Region', 'cn-hangzhou') request.add_query_param('MigrationJobClass', 'large')
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

# 非必填（企业版`V3.15.0`及之前历史版本需要），请替换为您实际的地域`ID`。

```
request.add_header("x-acs-regionid", "<yourRegionID>")
```

# 非必填（修改、删除、查询单实例详情时需要），请替换为您实际的实例`ID`。

```python
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

数据传输

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问。本操作介绍如何获取阿里云DTS Go SDK并开始调用。

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

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您实际的Endpoint。 数据传输

```java
package main import (
        "fmt"
        dts "github.com/aliyun/alibaba-cloud-sdk-go/services/dts"  )
func main() {
```

`//` 创建`Client`实例

```
    client, err := dts.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

`//` 创建`API`请求并设置参数

```
    request := dts.CreateCreateMigrationJobRequest()
```

`//` 传入请求参数

```
request.Region = "cn-hangzhou"
    request.MigrationJobClass = "large"
```

`//` 发起请求并处理异常

```
    response, err := client.CreateMigrationJob(request)
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

害您的阿里云账号的信息安全。 以下代码以DTS为例，展示初始化Client实例。 数据传输 `//` 初始化`Client`实例

```
Client, err := ecs.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。

#### 发起调用

本文介绍如何使用阿里云DTS Go SDK发起调用。 以下步骤以DTS为例，展示使用DTS Go SDK发起调用。
1. 导入DTS SDK。

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/dts
```

2. 新建一个Client，该Client中包含DTS的所有API。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 `Client,err := <dts>.NewClientWithAccessKey( //`请替换为您实际的产品名称 `"<yourRegionID>", //` 请替换为您实际的`RegionID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>") //` 请替换为您实际的`AccessKeySecret` `Client.Domain = "dts.aliyuns.com" //`设置请求域名地址，当前为示例值，请求根据实际请求地址替换。

| xxx.CreateXXXRequest |  | 方法创建一个请求。 |
|---|---|---|
| 法的命名规范为 |  |  |

**${service}**为产品名称(小写)。例如dts。
**${apiName}**为API名称，例如CreateMigrationJob。

```
request := dts.CreateCreateMigrationJobRequest() request.Region = "cn-hangzhou" request.MigrationJobClass = "large"
```

4. 发起调用。

```
response, err := Client.CreateMigrationJob(request)
```

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。 数据传输

```
response,err := Client.CreateMigrationJob(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个 `ClientError` 。 以下以DTS为例，您可以通过以下代码来判断并获取 `ClientError` 中的错误信息：

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/dts" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

```
response, err := Client.CreateMigrationJob(request) if clientError, ok := err.(*errors.ClientError); ok{
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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以DTS为例，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息： 数据传输

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/dts" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

```
response, err := Client.CreateMigrationJob(request) if serverError, ok := err.(*errors.ServerError); ok{
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

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**示例**

以下代码为数据传输DTS的CreateMigrationJob接口的调用示例：

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 数据传输

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

`request.Domain = "<dts.aliyuncs.com>" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "Dts"
    request.Version = "2020-01-01"
    // 指定APIName(Action)
    request.ApiName = "CreateMigrationJob"
```

`//` 业务参数

```
    request.QueryParams["Region"] = "cn-hangzhou"
    request.QueryParams["MigrationJobClass"] = "large"
```

`/*` 当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段调用方式如下：

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

数据传输

## API参考

### 公共参数

公共参数是指所有接口在调用时都需要用到的参数，包含公共请求参数和公共返回参数。

**公共请求参数**

| 名称 | 类型 | 是否必选 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回值的类型，支持JSON和XML，默认为XML。 |
| Version | String | 是 | OpenAPI版本号，版本号为日期格式：YYYY-MM-DD。当前版本号为2020-01-01。 |
| AccessKeyID | String | 是 | 阿里云颁发给用户的访问服务所用的密钥ID。 |
| Signature | String | 是 | 签名结果串。 |
| SignatureMetho d | String | 是 | 签名方式，目前仅支持HMAC-SHA1。 |
| Timestamp | String | 是 | 请求的时间戳，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| SignatureVersio n | String | 是 | 签名算法版本，目前版本为1.0。 |
| SignatureNonce | String | 是 | 唯一随机数，用于防止网络重放攻击。不同的请求需使用不同的随机数值。 |

**公共返回参数**

用户发送的每次接口调用请求，无论成功与否，系统都会返回一个唯一识别码（RequestId）给用户，可用来跟踪请求的执行情况。

**返回示例**

DTS OpenAPI使用标准的HTTP状态码表示请求处理的结果，具体状态码如下所示： 返回的HTTP状态码为2xx，代表调用成功。 返回的HTTP状态码为4xx或5xx，代表调用失败。 数据格式主要有XML和JSON两种，默认为XML格式，外部系统可以在请求时指定返回的数据格式。为便于查看，本文档中的返回示例做了格式化处理，实际返回结果是没有进行换行、缩进等处理的。 成功结果 XML示例

```xml
<?xml version="1.0" encoding="utf-8"?>
```

<!—结果的根结点`-->` <接口名称`+Response>` <!—返回请求标签`-->`

```xml
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
```

<!—返回结果数据`-->` `</`接口名称`+Response>` JSON示例数据传输

```json
{
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
```

`/*` 返回结果数据 `*/`

```
}
```

错误结果调用出错后，HTTP请求会返回一个4xx或5xx的HTTP状态码。返回的消息中包含具体的错误代码及错误信息，还包含一个全局唯一的请求ID（RequestId）和一个本次请求访问的站点ID（HostId）。 您可以根据返回的错误码来定位错误原因，详情请参见错误码。若您无法定位错误原因，

**说明**

请联系阿里云客服人员，并提供调用出错返回的HostId和RequestId，以便我们能尽快帮您解决问题。 XML示例

```xml
<?xml version="1.0" encoding="UTF-8"?> <Error>
   <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId>
   <HostId>dts.aliyuncs.com</HostId>
   <Code>UnsupportedOperation</Code>
   <Message>The specified action is not supported.</Message>
</Error>
```

JSON示例

```json
{
    "RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF",
    "HostId": "dts.aliyuncs.com",
    "Code": "UnsupportedOperation",
    "Message": "The specified action is not supported."
}
```

### 请求结构

DTS支持基于URL发起HTTP或HTTPS GET请求，您需要按照接口说明在请求中加入相应的请求参数，调用后系统会返回处理结果。

**服务地址**

| 地域（部署位置） | 接入地址（Endpoint） |
|---|---|
| 华东2（上海） | dts.cn-shanghai.aliyuncs.com |
| 华北1（青岛） | dts.cn-qingdao.aliyuncs.com |
| 华北2（北京） | dts.cn-beijing.aliyuncs.com |
| 华北3（张家口） | dts.cn-zhangjiakou.aliyuncs.com |
| 华北5（呼和浩特） | dts.cn-huhehaote.aliyuncs.com |
| 华南1（深圳） | dts.cn-shenzhen.aliyuncs.com |
| 中国（香港） | dts.cn-hongkong.aliyuncs.com |
| 美国东部 1（弗吉利亚） | dts.us-east-1.aliyuncs.com |

数据传输

| 美国西部 1（硅谷） | dts.us-west-1.aliyuncs.com |
|---|---|
| 金融云上海 | dts.cn-shanghai-finance-1.aliyuncs.com |
| 金融云深圳 | dts.cn-shenzhen-finance-1.aliyuncs.com |

**通信协议**

支持通过HTTP或HTTPS通道进行请求通信。为获得更高的安全性，推荐您使用HTTPS通道发送请求。

**请求方法**

支持HTTP GET方法发送请求，请求参数需包含在请求的URL中。

**请求参数**

每个请求都需要指定要执行的操作，即Action参数（例如CreateMigrationJob），以及每个操作都需要包含的公共请求参数和指定操作所特有的请求参数。

**字符编码**

请求及返回结果都使用UTF-8字符集进行编码。

### 支持的地域列表

| 地域名称 | 所在城市 | Region ID |
|---|---|---|
| 华东1 | 杭州 | cn-hangzhou |
| 华东2 | 上海 | cn-shanghai |
| 华北1 | 青岛 | cn-qingdao |
| 华北2 | 北京 | cn-beijing |
| 华北3 | 张家口 | cn-zhangbei |
| 华北5 | 呼和浩特 | cn-huhehaote |
| 华南1 | 深圳 | cn-shenzhen |
| 西南1 | 成都 | cn-chengdu |
| 中国（香港） | 中国（香港） | cn-hongkong |
| 亚太东南 1 | 新加坡 | ap-southeast-1 |
| 亚太东南 2 | 悉尼 | ap-southeast-2 |
| 亚太东南 3 | 吉隆坡 | ap-southeast-3 |
| 亚太东南 5 | 雅加达 | ap-southeast-5 |
| 亚太南部 1 | 孟买 | ap-south-1 |
| 亚太东北 1 | 东京 | ap-northeast-1 |

数据传输

| 美国西部 1 | 硅谷 | us-west-1 |
|---|---|---|
| 美国东部 1 | 弗吉尼亚 | us-east-1 |
| 欧洲中部 1 | 法兰克福 | eu-central-1 |
| 英国 | 伦敦 | eu-west-1 |
| 中东东部 1 | 迪拜 | me-east-1 |
| 华东1金融云 | 杭州 | cn-hangzhou-finance |
| 华东2金融云 | 上海 | cn-shanghai-finance |
| 华北1金融云 | 青岛 | cn-qingdao-finance |
| 华南1金融云 | 深圳 | cn-shenzhen-finance |
| 华北2阿里政务云1 | 北京 | cn-north-2-gov-1 |

### 新版API（推荐）

#### 购买DTS实例

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDtsInstan ce | 系统规定参数，取值：CreateDtsInstance。 |
| JobId | String | 否 | bi6e22ay243*** * | 任务ID。 |
| InstanceClass | String | 否 | xxlarge | 迁移或同步实例的规格。 迁移实例支持的规格：xxlarge 、xlarge、large、medium、sma ll。 同步实例支持的规格：large、medium、small、mic ro。 |
| PayType | String | 否 | PrePaid | 支付类型： PrePaid：预付费。 PostPaid：后付费。 说明本参数为必填参数。 |

数据传输

| Period | String | 否 | Month | 预付费实例的计费方式，取值：Year（年）Month（月）。 说明当PayType为PrePaid（预付费） 时，该参数才有效且必须传入。 |
|---|---|---|---|---|
| SyncArchitectur e | String | 否 | oneway | 同步拓扑，取值： oneway：单向同步，为默认值。 bidirectional：双向同步。 |
| AutoStart | Boolean | 否 | false | 购买完成后是否自动启动任务，取值： false：否。 true：是。 |
| UsedTime | Integer | 否 | 5 | 预付费实例购买时长。 说明当PayType为PrePaid（ 预付费）时，该参数才有效且必须传入。 预付费实例的计费方式，您可在参数Period中进行设置。 |
| Quantity | Integer | 否 | 1 | 购买实例数量。 说明暂时只支持购买一个实例。 |
| AutoPay | Boolean | 否 | false | 到期是否自动续费，取值： false：否。 true：是。 |
| Type | String | 否 | MIGRATION | 实例类型，取值为： MIGRATION：迁移。 SYNC：同步。 SUBSCRIBE：订阅。 |
| DatabaseCount | Integer | 否 | 3 | PolarDB-X下的私有定制RDS实例的数量，默认值为1。 说明仅SourceEndpointEngineNam e为drds时需要传入该参数。 |

数据传输

| SourceRegion | String | 否 | cn-hangzhou | 源实例区域。 |
|---|---|---|---|---|
| DestinationRegi on | String | 否 | cn-hangzhou | 目标实例区域。 |
| SourceEndpointE ngineName | String | 否 | MYSQL | 源实例数据库引擎类型。 MySQL：MySQL数据库（包括RDS MySQL和自建MySQL）。 PolarDB：PolarDB MySQL。 polardb o：PolarDB O引擎。 _ polardb pg：PolarDB _ PostgreSQL。 Redis：Redis数据库（包括云数据库 Redis和自建Redis）。 DRDS：云原生分布式数据库PolarDB- X 1.0和2.0。 PostgreSQL：自建PostgreSQL。 odps：MaxCompute。 oracle：自建Oracle。 mongodb：MongoDB数据库（包括云数据库MongoDB和自建 MongoDB）。 tidb：TiDB数据库。 ADS：云原生数仓 AnalyticDB MySQL 2.0。 ADB30：云原生数仓 AnalyticDB MySQL 3.0。 Greenplum：云原生数仓 AnalyticDB PostgreSQL。 MSSQL：SQL Server数据库（包括 RDS SQL Server和自建SQL Server）。 kafka：Kafka数据库（包括消息队列 Kafka版和自建Kafka）。 DataHub：阿里云流式数据服务 DataHub。 clickhouse：云数据库 ClickHouse。 DB2：自建DB2 LUW。 as400：AS/400。 Tablestore：表格存储Tablestore。 说明默认取值为MySQL。 |

数据传输

| DestinationEndp ointEngineName | String | 否 | MySQL | 目标数据库引擎类型。 MySQL：MySQL数据库（包括RDS MySQL和自建MySQL）。 PolarDB：PolarDB MySQL。 polardb o：PolarDB O引擎。 _ polardb pg：PolarDB _ PostgreSQL。 Redis：Redis数据库（包括云数据库 Redis和自建Redis）。 DRDS：云原生分布式数据库PolarDB- X 1.0和2.0。 PostgreSQL：自建PostgreSQL。 odps：MaxCompute。 oracle：自建Oracle。 mongodb：MongoDB数据库（包括云数据库MongoDB和自建 MongoDB）。 tidb：TiDB数据库。 ADS：云原生数仓 AnalyticDB MySQL 2.0。 ADB30：云原生数仓 AnalyticDB MySQL 3.0。 Greenplum：云原生数仓 AnalyticDB PostgreSQL。 MSSQL：SQL Server数据库（包括 RDS SQL Server和自建SQL Server）。 kafka：Kafka数据库（包括消息队列 Kafka版和自建Kafka）。 DataHub：阿里云流式数据服务 DataHub。 clickhouse：云数据库 ClickHouse。 DB2：自建DB2 LUW。 as400：AS/400。 Tablestore：表格存储Tablestore。 说明默认取值为MySQL。 |
|---|---|---|---|---|
| ComputeUnit | Integer | 否 | 5 | ETL的规格。单位为计算单元 ComputeUnit（CU），1CU=1vCPU​+4 GB内存。取值范围为大于等于2的整数。 传入该参数，开通ETL功能，进行数据清洗和转换。 |
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| InstanceId | String | dtsbi6e22ay243*** * | 实例ID。 |
| JobId | String | bi6e22ay243**** | 任务ID。 |
| RequestId | String | C166D79D-436B- 45F0-B5A5- 25E1**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=CreateDtsInstance
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateDtsInstanceResponse>
  <RequestId>C166D79D-436B-45F0-B5A5-25E1****</RequestId>
  <Success>true</Success>
</CreateDtsInstanceResponse>
```

`JSON` 格式

```json
{
    "RequestId":"C166D79D-436B-45F0-B5A5-25E1****",
    "Success":"true"
}
```

#### 配置DTS迁移或同步任务

调用ConfigureDtsJob接口配置一个迁移或同步任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | ConfigureDtsJob | 系统规定参数，取值：ConfigureDtsJob。 |
|---|---|---|---|---|
| DataInitialization | Boolean | 是 | true | 是否执行全量数据迁移或全量数据初始化，取值： true：是，为默认值。 false：否。 说明若JobType取值为CHECK，只能取值为false。 |
| DataSynchroniza tion | Boolean | 是 | true | 是否执行增量数据迁移或同步，取值： false：否，为默认值。 true：是。 说明若JobType取值为CHECK，只能取值为false。 |
| DbList | String | 是 | {"dtstest": {"name":"dtstes t","all":true}} | 待迁移或同步的对象，格式为JSON串。 |

数据传输

| DestinationEndp ointInstanceTyp e | String | 是 | EXPRESS | 目标实例类型，取值： 阿里云数据库 RDS：RDS MySQL、RDS SQLServer、RDS PostgreSQL、RDS MariaDB。 PolarDB：PolarDB MySQL。 POLARDBX20：PolarDB-X 2.0。 ADS：AnalyticDB MySQL 2.0、 3.0。 MONGODB：云数据库MongoDB。 GREENPLUM：AnalyticDB PostgreSQL。 DATAHUB：阿里云流数据处理平台 DataHub。 REDIS：云数据库Redis。 自建数据库 OTHER：有公网IP的自建数据库。 ECS：ECS上的自建数据库。 EXPRESS：通过专线接入的自建数据库。 CEN：通过云企业网CEN接入的自建数据库。 DG：通过数据库网关接入的自建数据库。 说明如目标实例为PolarDB O引擎集群，则目标实例类型需选择OTHER或者EXPRESS，作为自建数据库，且通过公网IP或者专线的方式接入。 目标实例为消息队列Kafka 版，则目标实例类型需选择ECS或者EXPRESS，作为自建数据库，且通过ECS 或者专线的方式接入。 当目标实例为自建数据库时，您还需要执行相应的准备工作。 |
|---|---|---|---|---|
| DtsJobName | String | 是 | rdsmysql至专线接入的自建mysql | DTS实例名称。 |

数据传输

| JobType | String | 是 | SYNC | 任务类型，取值为： MIGRATION：迁移。 SYNC：同步。 CHECK：数据校验。 说明若需要配置数据校验任务，还需配置DataCheckConfigure参数。 |
|---|---|---|---|---|
| DataCheckConfi gure | String | 否 | {"fullCheckMode l":1,"fullCheckRa tio":20,"checkM aximumHourEna ble":1,"checkMa ximumHour":1,"f ullCheckErrorNo tice":true,"fullCh eckValidFailNoti ce":true,"fullChe ckNoticeValue": 8,"incrementalC heckErrorNotice ":true,"incremen talCheckValidFai lNotice":true,"in crementalCheck ValidFailNoticeTi mes":2,"increme ntalCheckValidF ailNoticePeriod": 1,"incrementalC heckValidFailNot iceValue":1,"incr ementalCheckD elayNotice":true, "incrementalChe ckDelayNoticeTi mes":2,"increme ntalCheckDelay NoticePeriod":1, "incrementalChe ckDelayNoticeV alue":60,"fullDat aCheck":true,"in crementalDataC heck":true,"data CheckNoticePho ne":"13126800* ***","dataCheck DbList":"{"dts": {"name":"dts"," all":true}}"} | 数据校验任务的参数，格式为JSON字符串，如参数限制或告警配置等信息。更多信息请参见DataCheckConfigure参数说明。 |

数据传输

| SourceEndpointI nstanceType | String | 是 | RDS | 源实例类型，取值： 阿里云数据库 RDS：RDS MySQL、RDS SQL Server、RDS PostgreSQL、RDS MariaDB。 PolarDB：PolarDB MySQL。 POLARDBX20：PolarDB-X 2.0。 MONGODB：云数据库MongoDB。 DISTRIBUTED DMSLOGICDB：数 _ 据管理DMS逻辑库。 REDIS：云数据库Redis。 自建数据库 OTHER：有公网IP的自建数据库。 ECS：ECS上的自建数据库。 EXPRESS：通过专线接入的自建数据库。 CEN：通过云企业网CEN接入的自建数据库。 DG：通过数据库网关接入的自建数据库。 说明如源实例为PolarDB O引擎集群，则源实例类型需选择OTHER或者EXPRESS， 作为自建数据库，且通过公网IP或者专线的方式接入。 当源实例为自建数据库时， 您还需要执行相应的准备工作。 |
|---|---|---|---|---|
| StructureInitializ ation | Boolean | 是 | true | 是否执行库表结构迁移或初始化，取值： true：是，为默认值。 false：否。 说明若JobType取值为CHECK，只能取值为false。 |

数据传输

| SourceEndpointI nstanceID | String | 否 | rm- bp1imrtn6fq7h* *** | 源实例ID。 如源实例为阿里云数据库（如RDS MySQL），则您需要传入阿里云数据库的 ID（如RDS MySQL的实例ID）。 如源实例为自建数据库，则根据SourceEndpointInstanceType的取值不同，本参数的取值有所变化，例如SourceEndpointInstanceType取值为： ECS，则该参数需传入ECS的实例ID。 DG，则该参数需传入数据库网关ID。 EXPRESS、CEN：则该参数需传入已和源库互联的VPC ID。 说明取值为CEN时，您还需要在预留参数 Reserve中传入云企业网CEN的实例 ID。 |
|---|---|---|---|---|

数据传输

| SourceEndpointE ngineName | String | 否 | MYSQL | 源实例的数据库类型。 MYSQL：MySQL数据库（包括RDS MySQL和自建MySQL）。 PolarDB：PolarDB MySQL。 POLARDB O：PolarDB O引擎。 _ POLARDBX20：云原生分布式数据库 PolarDB-X 2.0。 ORACLE：自建Oracle。 POSTGRESQL：PostgreSQL数据库 （包括RDS PostgreSQL、自建 PostgreSQL）。 MSSQL：SQL Server数据库（包括 RDS SQL Server和自建SQL Server）。 MONGODB：MongoDB数据库（包括自建MongoDB、云数据库 MongoDB）。 DB2：自建DB2 LUW。 AS400：自建Db2 for i。 DMSPOLARDB：数据管理DMS逻辑库。 HBASE：自建HBase数据库。 TERADATA：Teradata数据库。 REDIS：Redis数据库引擎。 说明默认取值为MYSQL。 当源实例的数据库类型取值为MONGODB时，您还需要在预留参数Reserve中传入部分信息。 |
|---|---|---|---|---|
| SourceEndpoint Region | String | 否 | cn-hangzhou | 源实例区域。 说明如源为阿里云数据库，则该参数必须传入。 |
| SourceEndpointI P | String | 否 | 172.16.**.*** | 源实例的IP地址。 说明当SourceEndpointInstanceTy pe为OTHER、EXPRESS、DG、 CEN时，本参数才可用且必须传入。 |

数据传输

| SourceEndpointP ort | String | 否 | 3306 | 源实例的数据库服务端口。 说明当源实例为自建数据库时，本参数才可用且必须传入。 |
|---|---|---|---|---|
| SourceEndpoint OracleSID | String | 否 | testsid | Oracle数据库的SID信息。 说明当SourceEndpointEngineNam e取值为Oracle，且Oracle数据库为非RAC实例时，本参数才可用且必须传入。 |
| SourceEndpoint DatabaseName | String | 否 | dtstestdatabase | 源实例中迁移对象所属的数据库名称。 说明当源实例或者源实例的数据库类型为 PolarDB O引擎、PostgreSQL、 MongoDB数据库时，本参数才可用且必须传入。 |
| SourceEndpoint UserName | String | 否 | dtstest | 源库的数据库账号。 说明大部分情况下，您需要传入源库的数据库账号。 迁移或同步不同的数据库所需的权限有所差异。 |
| SourceEndpointP assword | String | 否 | Test123456 | 源库数据库账号密码。 |
| SourceEndpoint OwnerID | String | 否 | 140692647406* *** | 源实例所属的阿里云账号ID。 说明传入本参数即代表执行跨阿里云账号的数据迁移或同步，同时您还需要传入SourceEndpointRole参数。 |

数据传输

| SourceEndpoint Role | String | 否 | ram-for-dts | 源实例所属云账号配置的角色名称。 说明执行跨阿里云账号的数据迁移或同步时须传入本参数。 |
|---|---|---|---|---|
| DestinationEndp ointInstanceID | String | 否 | vpc- bp1opxu1zkhn0 0gzv**** | 目标实例ID。 如目标实例为云数据库（如RDS MySQL），则您需要传入云数据库的实例 ID（如RDS MySQL的实例ID）。 如目标实例为自建数据库，则根据DestinationEndpointInstanceTy pe的取值不同，本参数的取值有所变化， 例如DestinationEndpointInstanceTy pe取值为： ECS，则该参数需传入ECS的实例ID。 DG，则该参数需传入数据库网关ID。 EXPRESS、CEN：则该参数需传入已和源库互联的VPC ID。 说明取值为CEN时，您还需要在预留参数 Reserve中传入云企业网CEN的实例 ID。 |

数据传输

| DestinationEndp ointEngineName | String | 否 | MySQL | 目标实例的数据库类型。 MySQL：MySQL数据库（包括RDS MySQL和自建MySQL）。 PolarDB：PolarDB MySQL。 POLARDB O：PolarDB O引擎。 _ POLARDBX20：云原生分布式数据库 PolarDB-X 2.0。 ORACLE：自建Oracle。 PostgreSQL：PostgreSQL数据库 （包括RDS PostgreSQL、自建 PostgreSQL）。 MSSQL：SQL Server数据库（包括 RDS SQL Server和自建SQL Server）。 ADS：AnalyticDB MySQL 2.0。 ADB30：AnalyticDB MySQL 3.0。 MONGODB：MongoDB数据库（包括自建MongoDB、云数据库 MongoDB）。 GREENPLUM：AnalyticDB PostgreSQL。 KAFKA：Kafka数据库（包括消息队列 Kafka版和自建Kafka）。 DATAHUB：阿里云流式数据服务 DataHub。 DB2：自建DB2 LUW。 AS400：Db 2 for i。 REDIS：Redis数据库引擎。 说明默认取值为MYSQL。 当目标实例的数据库类型取值为KAFKA、MONGODB时 ，您还需要在预留参数 Reserve中传入部分信息。 |
|---|---|---|---|---|
| DestinationEndp ointRegion | String | 否 | cn-hangzhou | 目标实例区域。 说明如目标为阿里云数据库，则该参数必须传入。 |

数据传输

| DestinationEndp ointIP | String | 否 | 172.16.**.*** | 目标实例的IP地址。 说明当DestinationEndpointInstan ceType为OTHER、EXPRESS、 DG、CEN时，本参数才可用且必须传入。 |
|---|---|---|---|---|
| DestinationEndp ointPort | String | 否 | 3306 | 目标实例的数据库服务端口。 说明当目标实例为自建数据库时，本参数才可用且必须传入。 |
| DestinationEndp ointDataBaseNa me | String | 否 | dtstestdata | 目标实例中迁移对象所属的数据库名称。 说明当目标实例或目标数据库的类型为 PolarDB O引擎、AnalyticDB PostgreSQL、PostgreSQL、 MongoDB数据库时，本参数才可用且必须传入。 |
| DestinationEndp ointUserName | String | 否 | dtstest | 目标库的数据库账号。 说明大部分情况下，您需要传入源库的数据库账号。 迁移或同步不同的数据库所需的权限有所差异。 |
| DestinationEndp ointPassword | String | 否 | Test123456 | 目标库数据库账号密码。 |
| Reserve | String | 否 | { "srcInstanceId": "cen- 9kqshqum****** *" } | DTS预留参数，格式为JSON串，您可以传入本参数完善源目库信息（如目标Kafka数据库的数据存储格式、云企业网CEN的实例ID）。 |
| Checkpoint | String | 否 | 1610540493 | 增量数据迁移的启动位点或者同步位点， 格式为Unix时间戳，单位为秒。 |

数据传输

| DestinationEndp ointOracleSID | String | 否 | testsid | Oracle数据库的SID信息。 说明当DestinationEndpointEngine Name取值为Oracle，且Oracle数据库为非RAC实例时，本参数才可用且必须传入。 |
|---|---|---|---|---|
| DtsJobId | String | 否 | k2gm967v16f*** * | 迁移、同步或订阅任务ID。 说明本参数和参数DtsInstanceId两者中至少传入一个。可调用 DescribeDtsJobs获取任务ID。 |
| DtsInstanceId | String | 否 | dtsk2gm967v16 f**** | 迁移、同步或订阅实例ID。 说明本参数和参数DtsJobId两者中至少传入一个。可调用DescribeDtsJobs 获取实例ID。 |
| DelayPhone | String | 否 | 1361234****,13 71234**** | 延迟报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持中国内地手机号码， 且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |

数据传输

| DelayRuleTime | Long | 否 | 10 | 触发延迟报警的阈值，单位为秒且需为整数，可根据业务需要设置阈值，建议设置 10秒以上，避免因网络、数据库负载等原因导致的延迟波动。 说明当DelayNotice取值为true时，本参数必须传入。 |
|---|---|---|---|---|
| DelayNotice | Boolean | 否 | true | 是否监控延迟状态，取值： true：是。 false：否。 |
| ErrorPhone | String | 否 | 1361234****,13 71234**** | 异常报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持中国内地手机号码， 且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |
| ErrorNotice | Boolean | 否 | true | 是否监控异常状态，取值： true：是。 false：否。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 只有当同步任务的同步拓扑为双向时，本参数传入Reverse才会生效。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| DtsInstanceId | String | dtsk2gm967v16f** ** | 迁移、同步或订阅实例ID。 |
|---|---|---|---|
| DtsJobId | String | k2gm967v16f**** | 迁移、同步或订阅任务ID。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| HttpStatusCod e | String | 200 | 状态码。 |
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=ConfigureDtsJob &RegionId=cn-hangzhou &SourceEndpointInstanceType=RDS &DestinationEndpointInstanceType=EXPRESS &StructureInitialization=true &DataInitialization=true &DataSynchronization=true &DbList={"dtstest":{"name":"dtstest","all":true}} &JobType=SYNC &SourceEndpointInstanceID=rm-bp1imrtn6fq7h**** &SourceEndpointEngineName=MYSQL &SourceEndpointRegion=cn-hangzhou &SourceEndpointUserName=dtstest &SourceEndpointPassword=Test123456 &DestinationEndpointInstanceID=vpc-bp1opxu1zkhn00gzv**** &DestinationEndpointEngineName=MYSQL &DestinationEndpointIP=172.16.**.*** &DestinationEndpointRegion=cn-hangzhou &DestinationEndpointPort=3306 &DestinationEndpointUserName=dtstest &DestinationEndpointPassword=Test123456 &DtsJobId=k2gm967v16f**** &DtsInstanceId=dtsk2gm967v16f****
```

`&DtsJobName=rdsmysql`至专线接入的自建`mysql` `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ConfigureDtsJobResponse>
      <DtsJobId>k2gm967v16f****</DtsJobId>
      <RequestId>224DB9F7-3100-4899-AB9C-C938BCCB****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <DtsInstanceId>dtsk2gm967v16f****</DtsInstanceId>
      <Success>true</Success>
</ConfigureDtsJobResponse>
```

`JSON` 格式

```json
{
    "DtsJobId":"k2gm967v16f****",
    "RequestId":"224DB9F7-3100-4899-AB9C-C938BCCB****",
    "HttpStatusCode":200,
    "DtsInstanceId":"dtsk2gm967v16f****",
    "Success":true
}
```

#### 配置DTS订阅任务

数据传输

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ConfigureSubscr iption | 系统规定参数，取值：ConfigureSubscription。 |
| DbList | String | 是 | {"dtstest": {"name":"dtstes t","all":true}} | 订阅对象，格式为JSON串。 |
| DtsJobName | String | 是 | MySQL订阅 | 订阅任务名称。 说明建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| RegionId | String | 是 | cn-hangzhou | DTS实例所在地域。 |
| SubscriptionInst anceNetworkTyp e | String | 是 | classic | 订阅任务的网络类型，取值： classic：经典网络。 vpc：专有网络。 说明如果传入了本参数，则订阅任务被定义为新版，如果不传入该参数，则订阅任务被定义为旧版。 旧版订阅任务支持订阅自建 MySQL、RDS MySQL和 PolarDB-X 1.0的数据，新版订阅任务支持订阅自建 MySQL、RDS MySQL、 PolarDB MySQL和Oracle 的数据。 如果本参数传入的值为vpc时，您还需要传入SubscriptionInstanc eVPCId和SubscriptionI nstanceVSwitchID参数。 |
| DtsInstanceId | String | 否 | dtsy0zz3t13h7d* *** | 订阅实例ID。 |
| DtsJobId | String | 否 | y0zz3t13h7d**** | 订阅任务ID。 |

数据传输

| SourceEndpointE ngineName | String | 否 | MySQL | 源数据库类型，取值为MySQL或Oracle。 说明当源数据库为自建数据库，本参数必须传入。 |
|---|---|---|---|---|
| SourceEndpointI nstanceType | String | 否 | RDS | 源数据库的实例类型，取值： RDS：RDS MySQL。 PolarDB：PolarDB MySQL。 DRDS: PolarDB-X 1.0。 LocalInstance：有公网IP的自建数据库。 ECS：ECS上的自建数据库。 Express：通过专线接入的自建数据库。 CEN：通过云企业网CEN接入的自建数据库。 dg：通过数据库网关接入的自建数据库。 |
| SourceEndpoint Region | String | 否 | cn-hangzhou | 源实例所属地域。 说明如果源实例为有公网IP 的自建数据库，则可以传入cn- hangzhou或者离自建数据库物理距离最近的区域ID。 |
| SourceEndpointI nstanceID | String | 否 | rm- bp1zc3iyqe3qw* *** | 源实例ID。 说明源数据库的实例类型为 RDS MySQL、PolarDB-X 1.0、 PolarDB MySQL时，本参数才可用且必须传入。 |
| SourceEndpointI P | String | 否 | 172.16.8*.*** | 源数据库的连接地址。 说明当源数据库为自建数据库时，本参数才可用且必须传入。 |
| SourceEndpointP ort | String | 否 | 3306 | 源数据库的服务端口。 说明当源数据库为自建数据库时，本参数才可用且必须传入。 |

数据传输

| SourceEndpoint OracleSID | String | 否 | testsid | Oracle数据库的SID信息。 说明当源数据库为自建 Oracle时，且Oracle数据库为非 RAC实例时，本参数才可用且必须传入。 |
|---|---|---|---|---|
| SourceEndpoint DatabaseName | String | 否 | dtstestdata | 待订阅的数据库名称。 |
| SourceEndpoint UserName | String | 否 | dtstest | 源实例的数据库账号。 说明订阅不同的数据库所需的权限有所差异。 |
| SourceEndpointP assword | String | 否 | Test123456 | 源实例的数据库账号密码。 |
| SourceEndpoint OwnerID | String | 否 | 140692647406* *** | 源实例所属的阿里云账号ID。 说明仅在配置跨阿里云账号的数据订阅时本参数才可用，且必须传入。 |
| SourceEndpoint Role | String | 否 | ram-for-dts | 源实例的授权角色。当源实例与配置订阅任务所属阿里云账号不同时，需传入该参数，来指定源实例的授权角色，以允许配置订阅任务所属阿里云账号访问源实例的实例信息。 |
| Reserve | String | 否 | { "srcInstanceId": "cen- 9kqshqum****** *" } | DTS预留参数，格式为JSON串，您可以传入本参数完善源目库信息（如目标Kafka数据库的数据存储格式、云企业网CEN的实例ID）。 |
| Checkpoint | String | 否 | 1616902385 | 订阅启动时间，格式为Unix时间戳。 说明 Unix时间戳转换工具可用搜索引擎获取。 |
| SubscriptionInst anceVPCId | String | 否 | vpc- bp1vwnn14rqpyi czj**** | 订阅实例的专有网络ID。 说明当SubscriptionInstanceNetwo rkType取值为vpc时，本参数才可用且必须传入。 |

数据传输

| SubscriptionInst anceVSwitchId | String | 否 | vsw- bp10df3mxae6l pmku**** | 订阅实例的虚拟交换机ID。 说明当SubscriptionInstanceNetwo rkType取值为vpc时，本参数才可用且必须传入。 |
|---|---|---|---|---|
| SubscriptionDat aTypeDDL | Boolean | 否 | true | 是否订阅DDL类型的数据，取值： true：是，为默认值。 false：否。 |
| SubscriptionDat aTypeDML | Boolean | 否 | true | 是否订阅DML类型的数据，取值： true：是，为默认值。 false：否。 |
| DelayPhone | String | 否 | 1361234****,13 71234**** | 延迟报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |
| DelayRuleTime | Long | 否 | 10 | 触发延迟报警的阈值，单位为秒且需为整数，可根据业务需要设置阈值，建议设置 10秒以上，避免因网络、数据库负载等原因导致的延迟波动。 说明当DelayNotice取值为true时，本参数必须传入。 |
| DelayNotice | Boolean | 否 | true | 是否监控延迟状态，取值： true：是。 false：否。 |
| ErrorPhone | String | 否 | 1361234****,13 71234**** | 异常报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |

数据传输

| ErrorNotice | Boolean | 否 | true | 是否监控异常状态，取值： true：是。 false：否。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DtsInstanceId | String | dtsy0zz3t13h7d*** * | 订阅实例ID。 |
| DtsJobId | String | y0zz3t13h7d**** | 订阅任务ID。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回对应的错误信息。 |
| HttpStatusCod e | String | 200 | 状态码。 |
| RequestId | String | 1D6ECADF-C5E9- 4C96-8811- 77602B31**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSubscription &DbList={"dtstest":{"name":"dtstest","all":true}} &DtsJobName=MySQL订阅 &JobType=SUBSCRIBE &SourceEndpointInstanceType=RDS &SubscriptionInstanceNetworkType=classic &SourceEndpointInstanceID=rm-bp1zc3iyqe3qw**** &SourceEndpointUserName=dtstest &SourceEndpointPassword=Test123456
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<ConfigureSubscriptionResponse>
      <DtsJobId>y0zz3t13h7d****</DtsJobId>
      <RequestId>1D6ECADF-C5E9-4C96-8811-77602B31****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <DtsInstanceId>dtsy0zz3t13h7d****</DtsInstanceId>
      <Success>true</Success>
</ConfigureSubscriptionResponse>
```

`JSON` 格式

```json
{
    "DtsJobId":"y0zz3t13h7d****",
    "RequestId":"1D6ECADF-C5E9-4C96-8811-77602B31****",
    "HttpStatusCode":200,
    "DtsInstanceId":"dtsy0zz3t13h7d****",
    "Success":true
}
```

#### 启动DTS实例

调用StartDtsJob接口启动一个迁移、同步或订阅任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartDtsJob | 系统规定参数。取值：StartDtsJob。 |
| DtsJobId | String | 是 | l3m1213ye7l*** * | 迁移、同步或订阅任务ID。 |
| DtsInstanceId | String | 否 | dtsl3m1213ye7l **** | 迁移、同步或订阅实例ID。 说明可以通过调用查询迁移实例列表及各实例详情、查询数据订阅实例列表及各实例详情、查询数据同步实例列表及各实例详情接口进行查询。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向，默认值。 Reverse：反向。 说明当数据同步实例的拓扑类型为双向时，才可以传入Reverse以启动反向同步链路。 |
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

数据传输

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 601B6F25-21E7- 4484-99D5- 3EF2625C**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=StartDtsJob &DtsJobId=l3m1213ye7l****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StartDtsJobResponse>
      <RequestId>2D3B4615-923F-49AA-AF21-6D8E3967****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</StartDtsJobResponse>
```

`JSON` 格式数据传输

```json
{
    "RequestId":"2D3B4615-923F-49AA-AF21-6D8E3967****",
    "HttpStatusCode":200,
    "Success":true
}
```

#### 批量启动DTS任务

调用StartDtsJobs接口批量启动数据迁移或同步任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartDtsJobs | 系统规定参数。取值：StartDtsJobs。 |
| DtsJobIds | String | 是 | l5o11f9029c**** | 迁移、同步任务ID。 说明当有多个任务ID时，使用','隔开。 可调用DescribeDtsJobs获取DTS任务ID。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |

数据传输

| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | AD823BD3-1BA6- 4117-A536- 165CB280**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=StartDtsJobs &DtsJobIds=l5o11f9029c**** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StartDtsJobsResponse>
      <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</StartDtsJobsResponse>
```

`JSON` 格式

```json
{
    "RequestId": "AD823BD3-1BA6-4117-A536-165CB280****",
    "HttpStatusCode": 200,
    "Success": true
}
```

#### 订阅任务的消费组管理

##### 新增订阅任务的消费组

调用CreateConsumerChannel接口为DTS订阅任务新增消费组，用于下游客户端消费订阅数据。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | CreateConsumer Channel | 系统规定参数，取值：CreateConsumerChannel。 |
|---|---|---|---|---|
| ConsumerGroup Name | String | 是 | 订阅组A | 消费组的名称，不超过128个字符。建议配置具有业务意义的名称，便于后续识别。 |
| ConsumerGroup Password | String | 是 | Test123456 | 消费组的账号密码。 由大写字母、小写字母、数字、特殊字符中的任意两种或两种以上组成。 密码长度为8~32个字符。 |
| ConsumerGroup UserName | String | 是 | dtstest | 消费组的账号。 由大写字母、小写字母、数字、下划线中的任意一种或多种组成。 最长16个字符。 |
| RegionId | String | 是 | cn-hangzhou | DTS订阅实例所在地域的ID。 |
| DtsInstanceId | String | 否 | dtsboss6pn1w** **** | 订阅实例ID，可以调用DescribeDtsJobs 查询。 说明参数DtsInstanceId与DtsJobId， 两者必须传入其一。 |
| DtsJobId | String | 否 | boss6pn1w***** * | 订阅任务ID，可以调用DescribeDtsJobs 查询。 说明参数DtsInstanceId与DtsJobId， 两者必须传入其一。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConsumerGrou pID | String | dtsor2y66j4219*** * | 消费组ID，可在下游客户端消费订阅数据时传入。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回对应的错误信息。 |
| HttpStatusCod e | String | 200 | 状态码。 |

数据传输

| RequestId | String | 5F566C5B-E5B0- 4020-A531- FC6F5005**** | 请求ID。 |
|---|---|---|---|
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=CreateConsumerChannel &ConsumerGroupName=订阅组A &ConsumerGroupPassword=Test123456 &ConsumerGroupUserName=dtstest &RegionId=cn-hangzhou &DtsInstanceId=dtsboss6pn1w******
```

正常返回示例 `XML` 格式

```xml
<CreateConsumerChannelResponse>
      <ConsumerGroupID>dtsor2y66j4219****</ConsumerGroupID>
      <RequestId>5F566C5B-E5B0-4020-A531-FC6F5005****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</CreateConsumerChannelResponse>
```

`JSON` 格式

```json
{
 "ConsumerGroupID": "dtsor2y66j4219****",
 "RequestId": "5F566C5B-E5B0-4020-A531-FC6F5005****",
 "HttpStatusCode": 200,
 "Success": true
}
```

##### 查询订阅任务的消费组详情

调用DescribeConsumerChannel接口查询DTS订阅任务的消费组信息，如消费组ID、名称和账号，消费延迟时间等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeConsum erChannel | 系统规定参数，取值：DescribeConsumerChannel。 |
| RegionId | String | 是 | cn-hangzhou | DTS订阅实例所在地域的ID。 |

数据传输

| DtsInstanceId | String | 否 | dtsboss6pn1w** **** | 订阅实例ID，可以调用DescribeDtsJobs 查询。 说明参数DtsInstanceId与DtsJobId， 两者必须传入其一。 |
|---|---|---|---|---|
| DtsJobId | String | 否 | boss6pn1w***** * | 订阅任务ID，可以调用DescribeDtsJobs 查询。 说明参数DtsInstanceId与DtsJobId， 两者必须传入其一。 |
| PageSize | Integer | 否 | 20 | 每页记录数，取值范围为1~100，默认值为20。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| ParentChannelId | String | 否 | dtsan5114c522q g08c | 分布式任务的父任务ChannelId。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConsumerCha nnels | Array of ConsumerCha nnel |  | 消费组列表。 |
| ConsumerGrou pId | String | dtsor2y66j4219*** * | 消费组ID。 |
| ConsumerGrou pName | String | 订阅组A | 消费组的名称。 |
| ConsumerGrou pUserName | String | dtstest | 消费组的账号。 |
| ConsumptionC heckpoint | String | 2021-06- 20T12:00:00Z | 消费位点，即客户端在订阅通道内消费最后一条信息的时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

数据传输

| MessageDelay | Long | 1500 | 消息延迟时间，该时间=下游客户端最新消费数据的时间戳-数据订阅任务中最新订阅数据的时间戳，格式为Unix时间戳，单位为秒。 例如，源库最新的数据于10点产生，目前DTS订阅任务已读取到源库9点55分的数据，下游客户端消费到9点30分的数据，此时消息延迟时间应为9点55分至9点30分的unix时间戳差值。 说明如果该参数返回-1，则表示当前没有客户端连接该消费组。 |
|---|---|---|---|
| UnconsumedD ata | Long | 186600 | 未消费的消息总数，为未消费的订阅数据数量与心跳消息数量的和。 说明如果该参数返回-1，则表示当前没有客户端连接该消费组。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回对应的错误信息。 |
| HttpStatusCod e | String | 200 | 状态码。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 20 | 一页最多可展示的消费组数量。 |
| RequestId | String | D66140B3-C747- 42B6-8315- BAF6490E**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |
| TotalRecordCo unt | Long | 1 | 消费组总数。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeConsumerChannel &RegionId=cn-hangzhou &DtsInstanceId=dtsboss6pn1w******
```

正常返回示例 `XML` 格式数据传输

```xml
<DescribeConsumerChannelResponse>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>20</PageRecordCount>
      <RequestId>D66140B3-C747-42B6-8315-BAF6490E****</RequestId>
      <PageNumber>1</PageNumber>
      <HttpStatusCode>200</HttpStatusCode>
      <ConsumerChannels>
            <ConsumptionCheckpoint></ConsumptionCheckpoint>
            <ConsumerGroupId>dtsor2y66j4219****</ConsumerGroupId>
            <ConsumerGroupUserName>dtstest</ConsumerGroupUserName>
            <ConsumerGroupName>订阅组A</ConsumerGroupName>
            <MessageDelay>-1</MessageDelay>
            <UnconsumedData>-1</UnconsumedData>
      </ConsumerChannels>
      <Success>true</Success>
</DescribeConsumerChannelResponse>
```

`JSON` 格式

```json
{
 "TotalRecordCount": 1,
 "PageRecordCount": 20,
 "RequestId": "D66140B3-C747-42B6-8315-BAF6490E****",
 "PageNumber": 1,
 "HttpStatusCode": 200,
 "ConsumerChannels": [
  {
   "ConsumptionCheckpoint": "",
   "ConsumerGroupId": "dtsor2y66j4219****",
   "ConsumerGroupUserName": "dtstest",
   "ConsumerGroupName": "订阅组A",
   "MessageDelay": -1,
   "UnconsumedData": -1
  }
```

`],`

```json
 "Success": true
}
```

##### 修改订阅任务的消费组详情

调用ModifyConsumerChannel接口修改DTS订阅任务的消费组信息，包括消费组名称、账号名以及密码。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyConsumer Channel | 系统规定参数，取值：ModifyConsumerChannel。 |

数据传输

| ConsumerGroupI d | String | 是 | dtsor2y66j4219* *** | 消费组ID，您可以调用 DescribeConsumerChannel接口查询消费组ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-hangzhou | DTS订阅实例所在地域的ID。 |
| DtsInstanceId | String | 否 | dtsboss6pn1w73 **** | 订阅实例ID，可以调用DescribeDtsJobs 查询。 说明参数DtsInstanceId与DtsJobId， 两者必须传入其一。 |
| DtsJobId | String | 否 | boss6pn1w73*** * | 订阅任务ID，可以调用DescribeDtsJobs 查询。 说明参数DtsInstanceId与DtsJobId， 两者必须传入其一。 |
| ConsumerGroup Password | String | 否 | Test123456 | 修改后的消费组账号密码。 由大写字母、小写字母、数字、特殊字符中的任意两种或两种以上组成。 密码长度为8~32个字符。 |
| ConsumerGroup UserName | String | 否 | dtstest | 修改后的消费组的账号。 由大写字母、小写字母、数字、下划线中的任意一种或多种组成。 最长16个字符。 |
| ConsumerGroup Name | String | 否 | 订阅组B | 修改后的消费组名称，不超过128个字符。建议配置具有业务意义的名称，便于后续识别。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| HttpStatusCod e | String | 200 | 状态码。 |

数据传输

| RequestId | String | 055CAF9B-C15D- 4799-BB9E- E62D417**** | 请求ID。 |
|---|---|---|---|
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifyConsumerChannel &ConsumerGroupId=dtsor2y66j4219**** &RegionId=cn-hangzhou &DtsInstanceId=dtsboss6pn1w73**** &ConsumerGroupName=订阅组B
```

正常返回示例 `XML` 格式

```xml
<ModifyConsumerChannelResponse>
      <RequestId>055CAF9B-C15D-4799-BB9E-E62D417****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</ModifyConsumerChannelResponse>
```

`JSON` 格式

```json
{
 "RequestId": "055CAF9B-C15D-4799-BB9E-E62D417****",
 "HttpStatusCode": 200,
 "Success": true
}
```

##### 删除订阅任务的消费组

调用DeleteConsumerChannel接口删除DTS订阅任务的消费组。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteConsumer Channel | 系统规定参数，取值：DeleteConsumerChannel。 |
| ConsumerGroupI d | String | 是 | dtsktbb6jdn2*** *** | 消费组ID。 |
| RegionId | String | 是 | cn-hangzhou | DTS订阅实例所在地域的ID。 |

数据传输

| DtsInstanceId | String | 否 | dtsboss6pn1w73 **** | 订阅实例ID。 说明参数DtsInstanceId与DtsJobId， 两者必须传入其一。 |
|---|---|---|---|---|
| DtsJobId | String | 否 | boss6pn1w73*** * | 订阅任务ID。 说明参数DtsInstanceId与DtsJobId， 两者必须传入其一。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回对应的错误信息。 |
| HttpStatusCod e | String | 200 | 状态码。 |
| RequestId | String | F9E00ABE-2AD9- 40A9-8C3C- D817E648**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DeleteConsumerChannel &ConsumerGroupId=dtsktbb6jdn2****** &RegionId=cn-hangzhou &DtsInstanceId=dtsboss6pn1w73****
```

正常返回示例 `XML` 格式数据传输

```xml
<DeleteConsumerChannelResponse>
      <RequestId>F9E00ABE-2AD9-40A9-8C3C-D817E648****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</DeleteConsumerChannelResponse>
```

`JSON` 格式

```json
{
 "RequestId": "F9E00ABE-2AD9-40A9-8C3C-D817E648****",
 "HttpStatusCode": 200,
 "Success": true
}
```

#### 是否屏蔽预检查告警项目

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SkipPreCheck | 系统规定参数，取值：SkipPreCheck。 |
| JobId | String | 是 | b4my3zg929a** ** | 预检查任务ID，可以调用DescribePreCheckStatus查询。 |
| SkipPreCheckIte ms | String | 是 | CHECK SAME O _ _ BJ | 需屏蔽或取消屏蔽的预检查项目简称，取值： CHECK SAME OBJ：同名对象存在 _ _ 性检查。 CHECK SAME USER：不同名账号 _ _ 存在性检查。 CHECK SRC：源库版本检查。 _ CHECK TOPOLOGY：拓扑版本检 _ 查。 CHECK SERVER ID：源库 _ _ server id检查。 _ 说明多个项目简称用英文逗号（,）分隔。 |

数据传输

| SkipPreCheckNa mes | String | 是 | CHECK SAME O _ _ BJ DETAIL _ | 需屏蔽或取消屏蔽的预检查项目名称，对应参数SkipPreCheckItems，取值： CHECK SAME OBJ DETAIL：同名 _ _ _ 对象存在性检查。 CHECK SAME USER DETAIL：不 _ _ _ 同名账号存在性检查。 CHECK SRC DETAIL：源库版本检 _ _ 查。 CHECK TOPOLOGY DETAIL拓扑 _ _ 版本检查。 CHECK SERVER ID DETAIL：源 _ _ _ 库server id检查。 _ 说明多个项目名称用英文逗号（,）分隔。 |
|---|---|---|---|---|
| Skip | Boolean | 否 | true | 是否屏蔽该预检查项目，取值： true：屏蔽。 false：取消屏蔽。 说明本参数为必填参数。 |
| DtsJobId | String | 否 | c7412z57g8k*** * | 迁移、同步或订阅任务ID。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | 200 | 错误码，本参数即将下线。 |
| DynamicMess age | String | JobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回JobId，则代表所传入的请求参数JobId不合法。 |
| ErrCode | String | InternalError | 调用错误时返回的错误码。 |

数据传输

| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | 状态码。 |
| MigrationJobId | String | kyri3z9w29a**** | 预检查所属DTS任务的ID。 |
| RequestId | String | 8C498360-7892- 433C-847A- BA71A850**** | 请求ID。 |
| ScheduleJobId | String | b4my3zg929a**** | 预检查任务ID。 |
| SkipItems | String | CHECK SAME OBJ _ _ | 需屏蔽或取消屏蔽的预检查项目简称。 |
| SkipNames | String | CHECK SAME OBJ _ _ _ DETAIL | 需屏蔽或取消屏蔽的预检查项目名称。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=SkipPreCheck &JobId= b4my3zg929a**** &SkipPreCheckItems=CHECK_SAME_OBJ &SkipPreCheckNames=CHECK_SAME_OBJ_DETAIL
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<SkipPreCheckResponse>
      <RequestId>8C498360-7892-433C-847A-BA71A850****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
      <MigrationJobId>kyri3z9w29a****</MigrationJobId>
      <ScheduleJobId> b4my3zg929a****</ScheduleJobId>
      <SkipItems>CHECK_SAME_OBJ</SkipItems>
      <SkipNames>CHECK_SAME_OBJ_DETAIL</SkipNames>
</SkipPreCheckResponse>
```

`JSON` 格式数据传输

```json
{
  "RequestId": "8C498360-7892-433C-847A-BA71A850****",
  "HttpStatusCode": 200,
  "Success": true,
  "MigrationJobId": "kyri3z9w29a****",
  "ScheduleJobId": " b4my3zg929a****",
  "SkipItems": "CHECK_SAME_OBJ",
  "SkipNames": "CHECK_SAME_OBJ_DETAIL"
}
```

#### 查询DTS任务

##### 查询一个DTS任务详情

调用DescribeDtsJobDetail查询指定DTS任务（迁移/同步/订阅）的完整配置与运行状态信息。需确保调用方具备对应DTS资源的读取权限。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DtsJobId | Strin g | Quer y | 否 | ta7w132u12h**** | 迁移、同步或订阅任务ID。 |
| DtsInstanc eID | Strin g | Quer y | 否 | dtsta7w132u12h**** | 迁移、同步或订阅实例ID。 |
| Synchroniz ationDirect ion | Strin g | Quer y | 否 | Forward | 同步方向，取值： Forward（默认值）：正向。 Reverse：反向。 只有当数据同步实例的同步拓扑为双向同步时，本参数传入Reverse才会生效。 |
| RegionId | Strin g | Quer y | 否 | cn-hangzhou | 任务所属地域ID。 |
| SyncSubJo bHistory | Bool ean | Quer y | 否 | false | 是否返回所有的同步子任务。 默认为false，返回最近的一个同步子任务。 |

数据传输

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SubDistributed Job | Array | 子任务列表 | 分布式子任务的信息，如主任务不是分布式任务，此项为null。 目前仅当主任务为同步任务时，才会有此字段。 |
| -SubSyncJob | List | 详见以下结构体 | 同步子任务信息。 |
| -TagList | Array | 详见以下结构体 | 标签集合。 |
| --Id | Long | 2 | 主键。 |
| --GmtCreate | String | 2022-03- 16T08:01:19Z | 创建时间。 |
| --GmtModified | String | 2022-03- 16T08:01:19Z | 修改时间。 |
| --ResourceId | String | dtsnjuc14kp12u*** * | 数据迁移、同步和订阅的实例ID。 |
| -- ResourceType | String | ALIYUN::DTS::INST ANCE | 资源类型。 |
| --RegionId | String | 否 | cn-hangzhou |
| --AliUid | Long | 191448876515**** | 阿里云账号ID。 |
| --TagKey | String | key1 | 标签键tagkey。 |
| --TagValue | String | value1 | 标签值tagvalue。 |
| --TagCategory | String | System | 标签类型，取值： System：系统创建的标签。 Custom：用户添加的标签。 当值为空时，默认返回可公示的标签。 |

| > 文档版本：20260 | 729 |  | 8 |
|---|---|---|---|

数据传输

| --SrcRegion | String | cn-hangzhou | 任务所在地域，通常指目标端地域。 |
|---|---|---|---|
| --Scope | String | 0 | 标签的可见性，取值： 0：public 1：private |
| --Creator | Long | 191448876515**** | 标签操作者。 |
| -DtsInstanceID | String | 否 | dtsta7w132u12h**** |
| -DtsJobId | String | 是 | ta7w132u12h**** |
| -DtsJobName | String | api test _ | 迁移、同步或订阅任务名称。 |
| -GroupId | String | rg- acfmzawhxxc**** | 资源组ID。 |
| - DatabaseCoun t | Integer | 2 | 如源实例为PolarDB-X 1.0时，需要输入其下挂 RDS MySQL的数量。 |
| -DtsJobClass | String | xlarge | 链路规格。 |
| - DtsJobDirectio n | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 当数据同步实例的拓扑为双向时，才会返回本参数。 |
| - Synchronizatio nDirection | String | 否 | Forward |
| -PayType | String | PrePaid | 实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| -ExpireTime | String | 2023-06- 16T08:01:19Z | 实例的到期时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 当PayType参数的返回值为PrePaid时才会返回本参数。 |
| 5 |  |  | > 文档版本：2026072 |

数据传输

| -CreateTime | String | 2022-03- 16T08:01:19Z | 任务创建时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| -FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -DbObject | String | {\\"dtstestdata\\": {\\"all\\":true,\\"na me\\":\\"dtstestdat a\\",\\"state\\":\\"no rmal\\"}} | 迁移、同步或订阅对象。 |
| -Status | String | Migrating | 迁移或同步任务的状态，返回值为： NotStarted：未启动。 NotConfigured：未配置。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 Initializing：同步初始化中。 InitializeFailed：同步初始化失败。 synchronizing：同步中。 Migrating：迁移中。 Failed：同步失败。 MigrationFailed：迁移失败。 Suspending：暂停中。 Modifying：同步对象变更中。 Retrying：重试中。 Upgrade：升级中。 Downgrade：降级中。 Locked：锁定中。 Finished：完成。 |

数据传输

| -ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| -Delay | Long | 0 | 增量数据迁移或者同步的延迟时间，单位为毫秒。 |
| -Checkpoint | String | 1616405159 | 增量数据迁移的启动位点或者同步位点，格式为 Unix时间戳，单位为秒。 |

数据传输

| -Reserved | String | {\\"srcHostPorts\\": \\"\\",\\"whitelist.dm s.online.ddl.enable\ \":false,\\"filterDDL\ \":false,\\"sqlparser .dms.original.ddl\\" :true,\\"srcOracleTy pe\\":\\"sid\\",\\"ma xRetryTime\\":4320 0,\\"destSSL\\":\\"0\ \",\\"destOracleTyp e\\":\\"sid\\",\\"srcS SL\\":\\"0\\",\\"dbLis tCaseChangeMode\ \":\\"default\\",\\"So urceEngineVersion\ \":\\"8.0.18\\",\\"src NetType\\":\\"VPC\\ ",\\"destNetType\\": \\"VPC\\",\\"srcVpcN etMappingInst\\":\\" 172.16.1.:10803\\", \\"destVpcNetMapp ingInst\\":\\"172.16. 1.:11077\\",\\"useJo bTask\\":\\"1\\"} | DTS预留参数，格式为JSON串，可传入本参数实现特殊需求（例如是否自动启动预检查）。 |
|---|---|---|---|
| - SubscribeTopi c | String | cn hangzhou rm b _ _ _ p1162kryivb8**** _ dtstest version2 _ | 订阅Topic。 当该订阅实例为新版，且调用 CreateConsumerGroup接口创建了消费组时， 才会返回本参数。 |
| - ConsumptionC heckpoint | String | 2022-03- 23T07:30:31Z | 订阅任务的下游消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| - BeginTimesta mp | String | 2022-03- 15T08:25:34Z | 订阅实例中保存的数据范围的起始时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| - EndTimestamp | String | 2022-03- 26T14:03:21Z | 订阅实例中保存的数据范围的截止时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| - ConsumptionC lient | String | 114.*.*.:dts** | 下游消费客户端信息，由IP地址和DTS随机生成的随机数组成。 |
| -DestNetType | String | VPC | 消费客户端所属网络类型： CLASSIC：经典网络。 VPC：专有网络。 |
| -AppName | String | new | 是否为新版订阅，new（新版订阅）。 该参数仅在新版订阅实例中返回。 |

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| -EtlCalculator | String | { "cells ": \ [{\\"shape\\":\\"edg e\\",\\"attrs\\": {\\"line\\": {\\"stroke\\":\\"#b1 b1b1\\",\\"strokeWi dth\\":1,\\"targetMa rker\\": {\\"name\\":\\"bloc k\\",\\"args\\": {\\"size\\":\\"8\\"}}, \\"strokeDasharray\ \":\\"\\"}},\\"id\\":\\" cd1ec473-f9b9- 4e9b-a742- ac23f442**\\",\\"so urce\\": {\\"cell\\":\\"8b261 182-bfab-4803- ad8e- 6bb08e3e\\",\\"port \\":\\"out1\\"},\\"tar get\\": {\\"cell\\":\\"b3677 0df-f48c-4d6b- 9644- 54c5e924**\\",\\"po rt\\":\\"in1\\"},\\"zIn dex\\":7 }\] } | ETL任务的算子信息。 当任务为ETL时，才会返回本参数。 |
|---|---|---|---|

数据传输

| -OriginType | String | DTS任务 | 任务来源： PTS任务 DMS任务 DTS任务 |
|---|---|---|---|
| -JobType | String | SYNC | DTS实例的任务类型，取值： online：迁移。 SYNC：同步。 SUBSCRIBE：订阅。 |
| -IsDemoJob | Boolean | false | 是否子任务，返回值： true：是。 false：否。 |
| -TaskType | String | rds | 任务类型。 |
| - SourceEndpoin t | Struct | 详见以下结构体 | 源实例连接信息。 |
| --InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| --Region | String | cn-hangzhou | 源实例所在区域。 |
| --InstanceType | String | RDS | 源实例类型。 |
| --EngineName | String | MySQL | 源实例的数据库类型。 |
| --Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| --Port | String | 3306 | 源实例的数据库服务端口。 |
| -- DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| --OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |

| > 文档版本：20260 | 729 |  | 9 |
|---|---|---|---|

数据传输

| --UserName | String | dtstest | 源实例的数据库账号。 |
|---|---|---|---|
| -- SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
| --TlsVersion | String | TLSv1.2 | TLS版本。 |
| --RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |
| --AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
| - DestinationEn dpoint | Struct | 详见以下结构体 | 目标实例的连接信息。 |
| --InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| --Region | String | cn-hangzhou | 源实例所在区域。 |
| --InstanceType | String | RDS | 源实例类型。 |
| --EngineName | String | MySQL | 源实例的数据库类型。 |
| --Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| --Port | String | 3306 | 源实例的数据库服务端口。 |
| -- DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| --OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |
| 1 |  |  | > 文档版本：2026072 |

数据传输

| --UserName | String | dtstest | 源实例的数据库账号。 |
|---|---|---|---|
| -- SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
| --TlsVersion | String | TLSv1.2 | TLS版本。 |
| --RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |
| --AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
| - MigrationMode | Struct | 详见以下结构体 | 迁移类型或同步初始化类型。 |
| -- StructureInitial ization | Boolean | true | 是否执行库表结构迁移或初始化，返回值： true：是。 false：否。 |
| -- DataInitializati on | Boolean | true | 是否执行全量数据迁移或全量数据初始化，返回值： true：是。 false：否。 |
| -- DataSynchroni zation | Boolean | true | 是否执行增量数据迁移或同步，返回值： true：是。 false：否。 |
| -- DataExtractTr ansformLoad | Boolean | false | 是否执行数据加工，返回值： true：是。 false：否。 |
| - PrecheckStatu s | Struct | 详见以下结构体 | 预检查状态。 |

| > 文档版本：20260 | 729 |  | 9 |
|---|---|---|---|

数据传输

| --Detail | Array | 详见以下结构体 | 各预检查项的执行情况。 |
|---|---|---|---|
| ---CheckItem | String | CHECK CONN SRC _ _ | 预检查项目。 |
| --- CheckItemDes cription | String | CHECK CONN SRC _ _ DETAIL _ | 预检查项目描述。 |
| ---CheckResult | String | Success | 预检查结果，返回值为： Success：通过该项检查。 Failed：未通过该项检查。 |
| --- FailedReason | String | Original error: Access denied for user 'dtstest'@'100.104. *.' (using password: YES) | 预检查未通过的错误提示。 当CheckResult参数返回值为Failed时， 才会返回本参数。 |
| --- RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 当CheckResult参数返回值为Failed时， 才会返回本参数。 |
| --Status | String | Finished | 预检查状态，返回值为： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Finished：完成。 |
| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |

数据传输

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| - StructureInitial izationStatus | Struct | 详见以下结构体 | 库表结构初始化状态。 |
| --Status | String | Finished | 库表结构初始化状态，取值包括： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |

| 5 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| --Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
|---|---|---|---|
| -- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| - DataInitializati onStatus | Struct | 详见以下结构体 | 全量数据迁移或初始化的状态。 |
| --Status | String | Finished | 全量数据迁移或初始化状态，取值： NotStarted：未启动。 Migrating：迁移或初始化中。 Failed：迁移或初始化失败。 Finished：迁移或初始化完成。 |
| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |

| > 文档版本：20260 | 729 |  | 9 |
|---|---|---|---|

数据传输

| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |
|---|---|---|---|
| --Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| -- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| --NetioCurrent | String | 10MB/s | 当前网络IO。 |
| --TotalRow | String | 10000 | 总行数。 |
| --FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| --BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| - DataSynchroni zationStatus | Struct | 详见以下结构体 | 增量数据迁移或同步的状态。 |
| --Status | String | Catched | 增量数据迁移或同步状态，返回值： NotStarted：未启动。 Migrating：迁移或同步中。 Suspending：暂停中。 Checking：检查中。 Failed：迁移或同步失败。 Finished：迁移或同步完成。 Catched：无延迟。 |

数据传输

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| --Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| -- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| --NetioCurrent | String | 10MB/s | 当前网络IO。 |
| --TotalRow | String | 10000 | 总行数。 |

| > 文档版本：20260 | 729 |  | 9 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| --FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| --BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -DataEtlStatus | Struct | 详见以下结构体 | ETL任务的状态。 配置ETL任务后，才会返回该参数集合。 |
| --Status | String | Finished | ETL任务状态，返回值为： NotStarted：未启动。 Migrating：执行中。 Failed：执行失败。 Finished：完成。 Catched：无延迟。 |
| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |

| 9 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |
|---|---|---|---|
| --Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| -- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| -Performance | Struct | 详见以下结构体 | 迁移或同步链路的性能信息。 |
| --Rps | String | 100 | 每秒迁移或同步SQL语句的次数，包括BEGIN、 COMMIT 、DML语句（INSERT、DELETE、 UPDATE）及DDL语句。 |
| --Flow | String | 1 | 每秒迁移或同步数据的流量，单位为MB/s。 |
| -ReverseJob | Struct | 详见以下结构体 | 反向同步任务执行详情。 当该任务为数据同步，且拓扑类型为双向时，才会返回该参数合集。 |
| --TagList | Array | 详见以下结构体 | 标签集合。 |
| ---Id | Long | 2 | 主键。 |
| ---GmtCreate | String | 2022-03- 16T08:01:19Z | 创建时间。 |
| ---GmtModified | String | 2022-03- 16T08:01:19Z | 修改时间。 |
| ---ResourceId | String | dtsnjuc14kp12u*** * | 数据迁移、同步和订阅的实例ID。 |
| --- ResourceType | String | ALIYUN::DTS::INST ANCE | 资源类型。 |
| ---RegionId | String | cn-hangzhou | 地域。 |
| ---AliUid | Long | 191448876515**** | 阿里云账号ID。 |

| > 文档版本：20260 | 729 |  | 10 |
|---|---|---|---|

| ---TagKey | String | key1 | 标签键tagkey。 |
|---|---|---|---|
| ---TagValue | String | value1 | 标签值tagvalue。 |
| ---TagCategory | String | System | 标签类型，取值： System：系统创建的标签。 Custom：用户添加的标签。 当值为空时，默认返回可公示的标签。 |
| ---SrcRegion | String | cn-hangzhou | 任务所在地域，通常指目标端地域。 |
| ---Scope | String | 0 | 标签的可见性，取值： 0：public 1：private |
| ---Creator | Long | 191448876515**** | 标签操作者。 |
| -- DtsInstanceID | String | dtsta7w132u12h** ** | 迁移、同步或订阅实例ID。 |
| --DtsJobId | String | ta7w132u12h**** | 迁移、同步或订阅任务ID。 |
| --DtsJobName | String | api test _ | 迁移、同步或订阅任务名称。 |
| --GroupId | String | rg- acfmzawhxxc**** | 资源组ID。 |
| -- DatabaseCoun t | Integer | 2 | 如源实例为PolarDB-X 1.0时，需要输入其下挂 RDS MySQL的数量。 |
| --DtsJobClass | String | xlarge | 链路规格。 |
| -- DtsJobDirectio n | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 当数据同步实例的拓扑为双向时，才会返回本参数。 |

| 01 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| -- Synchronizatio nDirection | String | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 |
|---|---|---|---|
| --PayType | String | PrePaid | 实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| --ExpireTime | String | 2023-06- 16T08:01:19Z | 实例的到期时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 当PayType参数的返回值为PrePaid时才会返回本参数。 |
| --CreateTime | String | 2022-03- 16T08:01:19Z | 任务创建时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| --FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| --DbObject | String | {\\"dtstestdata\\": {\\"all\\":true,\\"na me\\":\\"dtstestdat a\\",\\"state\\":\\"no rmal\\"}} | 迁移、同步或订阅对象。 |

数据传输

| --Status | String | Migrating | 迁移或同步任务的状态，返回值： NotStarted：未启动。 NotConfigured：未配置。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 Initializing：同步初始化中。 InitializeFailed：同步初始化失败。 synchronizing：同步中。 Migrating：迁移中。 Failed：同步失败。 MigrationFailed：迁移失败。 Suspending：暂停中。 Modifying：同步对象变更中。 Retrying：重试中。 Upgrade：升级中。 Downgrade：降级中。 Locked：锁定中。 Finished：完成。 |
|---|---|---|---|

数据传输

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|

| > 文档版本：20260 | 729 |  | 10 |
|---|---|---|---|

数据传输

| --Delay | Long | 0 | 增量数据迁移或者同步的延迟时间，单位为毫秒。 |
|---|---|---|---|
| --Checkpoint | String | 1616405159 | 增量数据迁移的启动位点或者同步位点，格式为 Unix时间戳，单位为秒。 |
| --ReverseJob | String | **** | 反向同步任务执行详情。 当该任务为数据同步，且拓扑类型为双向时，才会返回该参数合集。 |
| --Reserved | String | {\\"srcHostPorts\\": \\"\\",\\"whitelist.dm s.online.ddl.enable\ \":false,\\"filterDDL\ \":false,\\"sqlparser .dms.original.ddl\\" :true,\\"srcOracleTy pe\\":\\"sid\\",\\"ma xRetryTime\\":4320 0,\\"destSSL\\":\\"0\ \",\\"destOracleTyp e\\":\\"sid\\",\\"srcS SL\\":\\"0\\",\\"dbLis tCaseChangeMode\ \":\\"default\\",\\"So urceEngineVersion\ \":\\"8.0.18\\",\\"src NetType\\":\\"VPC\\ ",\\"destNetType\\": \\"VPC\\",\\"srcVpcN etMappingInst\\":\\" 172.16.1.:10803\\", \\"destVpcNetMapp ingInst\\":\\"172.16. 1.:11077\\",\\"useJo bTask\\":\\"1\\"} | DTS预留参数，格式为JSON串，可传入本参数实现特殊需求（例如是否自动启动预检查）。 |
| -- SubscribeTopi c | String | cn hangzhou rm b _ _ _ p1162kryivb8**** _ dtstest version2 _ | 订阅Topic。 当该订阅实例为新版，且调用 CreateConsumerGroup接口创建了消费组时，才会返回本参数。 |
| -- ConsumptionC heckpoint | String | 2022-03- 23T07:30:31Z | 订阅任务的下游消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

| 05 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| -- BeginTimesta mp | String | 2022-03- 15T08:25:34Z | 订阅实例中保存的数据范围的起始时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| -- EndTimestamp | String | 2022-03- 26T14:03:21Z | 订阅实例中保存的数据范围的截止时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| -- ConsumptionC lient | String | 114.*.*.:dts** | 下游消费客户端信息，由IP地址和DTS随机生成的随机数组成。 |
| --DestNetType | String | VPC | 消费客户端所属网络类型： CLASSIC：经典网络。 VPC：专有网络。 |
| --AppName | String | new | 是否为新版订阅，new（新版订阅）。 该参数仅在新版订阅实例中返回。 |
| --EtlCalculator | String | { "cells ": \ [{\\"shape\\":\\"edg e\\",\\"attrs\\": {\\"line\\": {\\"stroke\\":\\"#b1 b1b1\\",\\"strokeWi dth\\":1,\\"targetMa rker\\": {\\"name\\":\\"bloc k\\",\\"args\\": {\\"size\\":\\"8\\"}}, \\"strokeDasharray\ \":\\"\\"}},\\"id\\":\\" cd1ec473-f9b9- 4e9b-a742- ac23f442**\\",\\"so urce\\": {\\"cell\\":\\"8b261 182-bfab-4803- ad8e- 6bb08e3e\\",\\"port \\":\\"out1\\"},\\"tar get\\": {\\"cell\\":\\"b3677 0df-f48c-4d6b- 9644- 54c5e924**\\",\\"po rt\\":\\"in1\\"},\\"zIn dex\\":7 }\] } | ETL任务的算子信息。 当任务为ETL时，才会返回本参数。 |

数据传输

| --OriginType | String | DTS任务 | 任务来源： PTS任务 DMS任务 DTS任务 |
|---|---|---|---|
| --JobType | String | SYNC | DTS实例的任务类型，取值： online：迁移。 SYNC：同步。 SUBSCRIBE：订阅。 |
| --IsDemoJob | Boolean | false | 是否子任务，返回值： true：是。 false：否。 |
| --TaskType | String | rds | 任务类型。 |
| -- SourceEndpoin t | Struct | 详见以下结构体 | 源实例连接信息。 |
| ---InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| ---Region | String | cn-hangzhou | 源实例所在区域。 |
| --- InstanceType | String | RDS | 源实例类型。 |
| ---EngineName | String | MySQL | 源实例的数据库类型。 |
| ---Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| ---Port | String | 3306 | 源实例的数据库服务端口。 |
| --- DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |

数据传输

| ---OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |
|---|---|---|---|
| ---UserName | String | dtstest | 源实例的数据库账号。 |
| --- SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
| ---RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |
| ---AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
| -- DestinationEn dpoint | Struct | 详见以下结构体 | 目标实例的连接信息。 |
| ---InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| ---Region | String | cn-hangzhou | 源实例所在区域。 |
| --- InstanceType | String | RDS | 源实例类型。 |
| ---EngineName | String | MySQL | 源实例的数据库类型。 |
| ---Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| ---Port | String | 3306 | 源实例的数据库服务端口。 |
| --- DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| ---OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |
|---|---|---|---|
| ---UserName | String | dtstest | 源实例的数据库账号。 |
| --- SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
| ---RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |
| ---AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
| -- MigrationMode | Struct | 详见以下结构体 | 迁移类型或同步初始化类型。 |
| --- StructureInitial ization | Boolean | true | 是否执行库表结构迁移或初始化，返回值： true：是。 false：否。 |
| --- DataInitializati on | Boolean | true | 是否执行全量数据迁移或全量数据初始化，返回值： true：是。 false：否。 |
| --- DataSynchroni zation | Boolean | true | 是否执行增量数据迁移或同步，返回值： true：是。 false：否。 |
| --- DataExtractTr ansformLoad | Boolean | false | 是否执行数据加工，返回值： true：是。 false：否。 |

| 09 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| -- PrecheckStatu s | Struct | 详见以下结构体 | 预检查状态。 |
|---|---|---|---|
| ---Detail | Array | 详见以下结构体 | 各预检查项的执行情况。 |
| ----CheckItem | String | CHECK CONN SRC _ _ | 预检查项目。 |
| ---- CheckItemDes cription | String | CHECK CONN SRC _ _ DETAIL _ | 预检查项目描述。 |
| ---- CheckResult | String | Success | 预检查结果，返回值为： Success：通过该项检查。 Failed：未通过该项检查。 |
| ---- FailedReason | String | Original error: Access denied for user 'dtstest'@'100.104. *.' (using password: YES) | 预检查未通过的错误提示。 当CheckResult参数返回值为Failed时， 才会返回本参数。 |
| ---- RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 当CheckResult参数返回值为Failed时， 才会返回本参数。 |
| ---Status | String | Finished | 预检查状态，返回值： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Finished：完成。 |
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |

数据传输

| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| -- StructureInitial izationStatus | Struct | 详见以下结构体 | 库表结构初始化状态。 |

| 数据传输 |  |  | 开发指南·API参考 |
|---|---|---|---|

| ---Status | String | Finished | 库表结构初始化状态，取值： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
|---|---|---|---|
| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| ---Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| --- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |

| > 文档版本：20260 | 729 |  | 11 |
|---|---|---|---|

数据传输

| -- DataInitializati onStatus | Struct | 详见以下结构体 | 全量数据迁移或初始化的状态。 |
|---|---|---|---|
| ---Status | String | Finished | 全量数据迁移或初始化状态，取值： NotStarted：未启动。 Migrating：迁移或初始化中。 Failed：迁移或初始化失败。 Finished：迁移或初始化完成。 |

数据传输

| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |

| > 文档版本：20260 | 729 |  | 11 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| ---Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
|---|---|---|---|
| --- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| ---NetioCurrent | String | 10MB/s | 当前网络IO。 |
| ---TotalRow | String | 10000 | 总行数。 |
| ---FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| ---BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -- DataSynchroni zationStatus | Struct | 详见以下结构体 | 增量数据迁移或同步的状态。 |
| ---Status | String | Catched | 增量数据迁移或同步状态，返回值为： NotStarted：未启动。 Migrating：迁移或同步中。 Suspending：暂停中。 Checking：检查中。 Failed：迁移或同步失败。 Finished：迁移或同步完成。 Catched：无延迟。 |

数据传输

| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|

| > 文档版本：20260 | 729 |  | 11 |
|---|---|---|---|

数据传输

| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |
|---|---|---|---|
| ---Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| --- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| ---NetioCurrent | String | 10MB/s | 当前网络IO。 |
| ---TotalRow | String | 10000 | 总行数。 |
| ---FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| ---BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -- DataEtlStatus | Struct | 详见以下结构体 | ETL任务的状态。 配置ETL任务后，才会返回该参数集合。 |
| ---Status | String | Finished | ETL任务状态，返回值为： NotStarted：未启动。 Migrating：执行中。 Failed：执行失败。 Finished：完成。 Catched：无延迟。 |

数据传输

| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| ---Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| --- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| --Performance | Struct | 详见以下结构体 | 迁移或同步链路的性能信息。 |

| > 文档版本：20260 | 729 |  | 11 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| ---Rps | String | 100 | 每秒迁移或同步SQL语句的次数，包括BEGIN、 COMMIT 、DML语句（INSERT、DELETE、 UPDATE）及DDL语句。 |  |  |
|---|---|---|---|---|---|
| ---Flow | String | 1 | 每秒迁移或同步数据的流量，单位为MB/s。 |  |  |
| -- SubscriptionH ost | Struct | 详见以下结构体 | 订阅任务的连接地址。 |  |  |
| ---PublicHost | String | dts-cn- ****.aliyuncs.com: 18001 | 订阅任务的公网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| ---PrivateHost | String | dts-cn-****- internal.aliyuncs.co m:18002 | 订阅任务的私网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| ---VpcHost | String | dts-cn-****- vpc.aliyuncs.com:1 8003 | 订阅任务的专有网络VPC（Virtual Private Cloud）连接信息，格式为地址：端口号 。 |  |  |
| ---VpcHostIpV6 | String | dts-cn-****- vpc6.aliyuncs.com: 18003 | 订阅任务的VPC IPv6连接信息。 |  |  |
| -- SubscriptionD ataType | Struct | 详见以下结构体 | 订阅数据的类型。 |  |  |
| ---Ddl | Boolean | true | 订阅数据是否包含DDL语句，返回值： true：是。 false：否。 |  |  |
| ---Dml | Boolean | true | 订阅数据是否包含DML语句，返回值： true：是。 false：否。 |  |  |
| --RetryState | Struct | 详见以下结构体 | 由于任务异常，DTS正在重试。 |  |  |
| ---JobId | String | ta7w132u12h**** | 任务ID。 |  |  |
| --- MaxRetryTime | Integer | 7200 | 最大重试时间，单位为秒。 |  |  |

| s.com: | 号 |
|---|---|

| uncs.co | 号 |
|---|---|

| 19 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| 数据传输 |  |  | 开发指南·API参考 |
|---|---|---|---|

| ---RetryTime | Integer | 3600 | 已重试时间，单位为秒。 |  |  |
|---|---|---|---|---|---|
| ---RetryCount | Integer | 5 | 已重试次数。 |  |  |
| ---Retrying | Boolean | true | 是否在重试中，返回值： true：是。 false：否。 |  |  |
| ---Module | String | 03 | 实例进展。 |  |  |
| ---RetryTarget | String | srcDB | 重试目标，返回值： srcDB：源数据库。 destDB：目标数据库。 inner module：DTS内部模块。 _ |  |  |
| ---ErrMsg | String | CHECK ERROR SA __ _ ME OBJ _ | 报错信息。 |  |  |
| - SubscriptionH ost | Struct | 详见以下结构体 | 订阅任务的连接地址。 |  |  |
| --PublicHost | String | dts-cn- ****.aliyuncs.com: 18001 | 订阅任务的公网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| --PrivateHost | String | dts-cn-****- internal.aliyuncs.co m:18002 | 订阅任务的私网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| --VpcHost | String | dts-cn-****- vpc.aliyuncs.com:1 8003 | 订阅任务的专有网络VPC（Virtual Private Cloud）连接信息，格式为地址：端口号 。 |  |  |
| --VpcHostIpV6 | String | dts-cn-****- vpc6.aliyuncs.com: 18003 | 订阅任务的VPC IPv6连接信息。 |  |  |
| - SubscriptionD ataType | Struct | 详见以下结构体 | 订阅数据的类型。 |  |  |

| s.com: | 号 |
|---|---|

| uncs.co | 号 |
|---|---|

| > 文档版本：20260 | 729 |  | 12 |
|---|---|---|---|

数据传输

| --Ddl | Boolean | true | 订阅数据是否包含DDL语句，返回值： true：是。 false：否。 |
|---|---|---|---|
| --Dml | Boolean | true | 订阅数据是否包含DML语句，返回值： true：是。 false：否。 |
| -RetryState | Struct | 详见以下结构体 | 由于任务异常，DTS正在重试。 |
| --JobId | String | ta7w132u12h**** | 任务ID。 |
| -- MaxRetryTime | Integer | 7200 | 最大重试时间，单位为秒。 |
| --RetryTime | Integer | 3600 | 已重试时间，单位为秒。 |
| --RetryCount | Integer | 5 | 已重试次数。 |
| --Retrying | Boolean | true | 是否在重试中，返回值： true：是。 false：否。 |
| --Module | String | 03 | 实例进展。 |
| --RetryTarget | String | srcDB | 重试目标，返回值： srcDB：源数据库。 destDB：目标数据库。 inner module：DTS内部模块。 _ |
| --ErrMsg | String | CHECK ERROR SA __ _ ME OBJ _ | 报错信息。 |
| SubSyncJob | Array | 详见以下结构体 | 同步子任务信息。 |
| -SubSyncJob | List | 详见以下结构体 | 同步子任务信息。 |
| -TagList | Array | 详见以下结构体 | 标签集合。 |

| 21 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| 数据传输 |  |  | 开发指南·API参考 |
|---|---|---|---|

| --Id | Long | 2 | 主键。 |
|---|---|---|---|
| --GmtCreate | String | 2022-03- 16T08:01:19Z | 创建时间。 |
| --GmtModified | String | 2022-03- 16T08:01:19Z | 修改时间。 |
| --ResourceId | String | dtsnjuc14kp12u*** * | 数据迁移、同步和订阅的实例ID。 |
| -- ResourceType | String | ALIYUN::DTS::INST ANCE | 资源类型。 |
| --RegionId | String | cn-hangzhou | 地域ID。 |
| --AliUid | Long | 191448876515**** | 阿里云账号ID。 |
| --TagKey | String | key1 | 标签键。 |
| --TagValue | String | value1 | 标签值。 |
| --TagCategory | String | System | 标签类型，取值： System：系统创建的标签。 Custom：用户添加的标签。 当值为空时，默认返回可公示的标签。 |
| --SrcRegion | String | cn-hangzhou | 任务所在地域，通常指目标端地域。 |
| --Scope | String | 0 | 标签的可见性，取值： 0：public 1：private |
| --Creator | Long | 191448876515**** | 标签操作者。 |
| -DtsInstanceID | String | dtsta7w132u12h** ** | 实例ID。 |
| -DtsJobId | String | ta7w132u12h**** | 任务ID。 |

| > 文档版本：20260 | 729 |  | 12 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| -DtsJobName | String | api test _ | 迁移、同步或订阅任务名称。 |
|---|---|---|---|
| -GroupId | String | rg- acfmzawhxxc**** | 资源组ID。 |
| - DatabaseCoun t | Integer | 2 | 如源实例为PolarDB-X 1.0时，需要输入其下挂 RDS MySQL的数量。 |
| -DtsJobClass | String | xlarge | 链路规格。 |
| - DtsJobDirectio n | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 当数据同步实例的拓扑为双向时，才会返回本参数。 |
| - Synchronizatio nDirection | String | Forward | Forward |
| -PayType | String | PrePaid | 实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| -ExpireTime | String | 2023-06- 16T08:01:19Z | 实例的到期时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 当PayType参数的返回值为PrePaid时才会返回本参数。 |
| -CreateTime | String | 2022-03- 16T08:01:19Z | 任务创建时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -DbObject | String | {\\"dtstestdata\\": {\\"all\\":true,\\"na me\\":\\"dtstestdat a\\",\\"state\\":\\"no rmal\\"}} | 迁移、同步或订阅对象。 |

数据传输

| -Status | String | Migrating | 迁移或同步任务的状态，返回值为： NotStarted：未启动。 NotConfigured：未配置。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 Initializing：同步初始化中。 InitializeFailed：同步初始化失败。 synchronizing：同步中。 Migrating：迁移中。 Failed：同步失败。 MigrationFailed：迁移失败。 Suspending：暂停中。 Modifying：同步对象变更中。 Retrying：重试中。 Upgrade：升级中。 Downgrade：降级中。 Locked：锁定中。 Finished：完成。 |
|---|---|---|---|

数据传输

| -ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|

| 25 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| -Delay | Long | 0 | 增量数据迁移或者同步的延迟时间，单位为毫秒。 |
|---|---|---|---|
| -Checkpoint | String | 1616405159 | 增量数据迁移的启动位点或者同步位点，格式为 Unix时间戳，单位为秒。 |
| -Reserved | String | {\\"srcHostPorts\\": \\"\\",\\"whitelist.dm s.online.ddl.enable\ \":false,\\"filterDDL\ \":false,\\"sqlparser .dms.original.ddl\\" :true,\\"srcOracleTy pe\\":\\"sid\\",\\"ma xRetryTime\\":4320 0,\\"destSSL\\":\\"0\ \",\\"destOracleTyp e\\":\\"sid\\",\\"srcS SL\\":\\"0\\",\\"dbLis tCaseChangeMode\ \":\\"default\\",\\"So urceEngineVersion\ \":\\"8.0.18\\",\\"src NetType\\":\\"VPC\\ ",\\"destNetType\\": \\"VPC\\",\\"srcVpcN etMappingInst\\":\\" 172.16.1.:10803\\", \\"destVpcNetMapp ingInst\\":\\"172.16. 1.:11077\\",\\"useJo bTask\\":\\"1\\"} | DTS预留参数，格式为JSON串，可以传入本参数实现特殊需求（例如是否自动启动预检查）。 |
| - SubscribeTopi c | String | cn hangzhou rm b _ _ _ p1162kryivb8**** _ dtstest version2 _ | 订阅Topic。 当该订阅实例为新版，且调用 CreateConsumerGroup接口创建了消费组时， 才会返回本参数。 |
| - ConsumptionC heckpoint | String | 2022-03- 23T07:30:31Z | 订阅任务的下游消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| - BeginTimesta mp | String | 2022-03- 15T08:25:34Z | 订阅实例中保存的数据范围的起始时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| - EndTimestamp | String | 2022-03- 26T14:03:21Z | 订阅实例中保存的数据范围的截止时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| - ConsumptionC lient | String | 114.*.*.:dts** | 下游消费客户端信息，由IP地址和DTS随机生成的随机数组成。 |

| > 文档版本：20260 | 729 |  | 12 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| -DestNetType | String | VPC | 消费客户端所属网络类型： CLASSIC：经典网络。 VPC：专有网络。 |
|---|---|---|---|
| -AppName | String | new | 是否为新版订阅，new（新版订阅）。 该参数仅在新版订阅实例中返回。 |
| -EtlCalculator | String | { "cells ": \ [{\\"shape\\":\\"edg e\\",\\"attrs\\": {\\"line\\": {\\"stroke\\":\\"#b1 b1b1\\",\\"strokeWi dth\\":1,\\"targetMa rker\\": {\\"name\\":\\"bloc k\\",\\"args\\": {\\"size\\":\\"8\\"}}, \\"strokeDasharray\ \":\\"\\"}},\\"id\\":\\" cd1ec473-f9b9- 4e9b-a742- ac23f442**\\",\\"so urce\\": {\\"cell\\":\\"8b261 182-bfab-4803- ad8e- 6bb08e3e\\",\\"port \\":\\"out1\\"},\\"tar get\\": {\\"cell\\":\\"b3677 0df-f48c-4d6b- 9644- 54c5e924**\\",\\"po rt\\":\\"in1\\"},\\"zIn dex\\":7 }\] } | ETL任务的算子信息。 当任务为ETL时，才会返回本参数。 |
| -OriginType | String | DTS任务 | 任务来源： PTS任务 DMS任务 DTS任务 |

数据传输

| -JobType | String | SYNC | DTS实例的任务类型，取值： online：迁移。 SYNC：同步。 SUBSCRIBE：订阅。 |
|---|---|---|---|
| -IsDemoJob | Boolean | false | 是否子任务，返回值： true：是。 false：否。 |
| -TaskType | String | rds | 任务类型。 |
| - SourceEndpoin t | Struct | 详见以下结构体 | 源实例连接信息。 |
| --InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| --Region | String | cn-hangzhou | 源实例所在区域。 |
| --InstanceType | String | RDS | 源实例类型。 |
| --EngineName | String | MySQL | 源实例的数据库类型。 |
| --Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| --Port | String | 3306 | 源实例的数据库服务端口。 |
| -- DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| --OracleSID | String | testsid | Oracle数据库的SID信息。 说明当源实例的 EngineName取值为Oracle，且Oracle数据库为非RAC实例时，才会返回本参数。 |
| --UserName | String | dtstest | 源实例的数据库账号。 |

数据传输

| -- SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
|---|---|---|---|
| --RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |
| --AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
| - DestinationEn dpoint | Struct | 详见以下结构体 | 目标实例的连接信息。 |
| --InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| --Region | String | cn-hangzhou | 源实例所在区域。 |
| --InstanceType | String | RDS | 源实例类型。 |
| --EngineName | String | MySQL | 源实例的数据库类型。 |
| --Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| --Port | String | 3306 | 源实例的数据库服务端口。 |
| -- DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| --OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |
| --UserName | String | dtstest | 源实例的数据库账号。 |

数据传输

| -- SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
|---|---|---|---|
| --RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |
| --AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
| - MigrationMode | Struct | 详见以下结构体 | 迁移类型或同步初始化类型。 |
| -- StructureInitial ization | Boolean | true | 是否执行库表结构迁移或初始化，返回值： true：是。 false：否。 |
| -- DataInitializati on | Boolean | true | 是否执行全量数据迁移或全量数据初始化，返回值： true：是。 false：否。 |
| -- DataSynchroni zation | Boolean | true | 是否执行增量数据迁移或同步，返回值： true：是。 false：否。 |
| -- DataExtractTr ansformLoad | Boolean | false | 是否执行数据加工，返回值： true：是。 false：否。 |
| - PrecheckStatu s | Struct | 详见以下结构体 | 预检查状态。 |
| --Detail | Array | 详见以下结构体 | 各预检查项的执行情况。 |
| ---CheckItem | String | CHECK CONN SRC _ _ | 预检查项目。 |

| > 文档版本：20260 | 729 |  | 13 |
|---|---|---|---|

数据传输

| --- CheckItemDes cription | String | CHECK CONN SRC _ _ DETAIL _ | 预检查项目描述。 |
|---|---|---|---|
| ---CheckResult | String | Success | 预检查结果，返回值为： Success：通过该项检查。 Failed：未通过该项检查。 |
| --- FailedReason | String | Original error: Access denied for user 'dtstest'@'100.104. *.' (using password: YES) | 预检查未通过的错误提示。 当CheckResult参数返回值为Failed时， 才会返回本参数。 |
| --- RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 当CheckResult参数返回值为Failed时， 才会返回本参数。 |
| --Status | String | Finished | 预检查状态，返回值为： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Finished：完成。 |
| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |

数据传输

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| - StructureInitial izationStatus | Struct | 详见以下结构体 | 库表结构初始化状态。 |
| --Status | String | Finished | 库表结构初始化状态，取值包括： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |

数据传输

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| --Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| -- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| - DataInitializati onStatus | Struct | 详见以下结构体 | 全量数据迁移或初始化的状态。 |

数据传输

| --Status | String | Finished | 全量数据迁移或初始化状态，取值包括： NotStarted：未启动。 Migrating：迁移或初始化中。 Failed：迁移或初始化失败。 Finished：迁移或初始化完成。 |
|---|---|---|---|
| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| --Progress | String | 1 | 已完成库表结构初始化的表的数量。 |

| > 文档版本：20260 | 729 |  | 13 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| -- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
|---|---|---|---|
| --NetioCurrent | String | 10MB/s | 当前网络IO。 |
| --TotalRow | String | 10000 | 总行数。 |
| --FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| --BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| - DataSynchroni zationStatus | Struct | 详见以下结构体 | 增量数据迁移或同步的状态。 |
| --Status | String | Catched | 增量数据迁移或同步状态，返回值为： NotStarted：未启动。 Migrating：迁移或同步中。 Suspending：暂停中。 Checking：检查中。 Failed：迁移或同步失败。 Finished：迁移或同步完成。 Catched：无延迟。 |

数据传输

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| --Progress | String | 1 | 已完成库表结构初始化的表的数量。 |

| > 文档版本：20260 | 729 |  | 13 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| -- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
|---|---|---|---|
| --NetioCurrent | String | 10MB/s | 当前网络IO。 |
| --TotalRow | String | 10000 | 总行数。 |
| --FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| --BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -DataEtlStatus | Struct | 详见以下结构体 | ETL任务的状态。 配置ETL任务后，才会返回该参数集合。 |
| --Status | String | Finished | ETL任务状态，返回值为： NotStarted：未启动。 Migrating：执行中。 Failed：执行失败。 Finished：完成。 Catched：无延迟。 |

数据传输

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| --Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| --Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| -- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| -Performance | Struct | 详见以下结构体 | 迁移或同步链路的性能信息。 |
| --Rps | String | 100 | 每秒迁移或同步SQL语句的次数，包括BEGIN、 COMMIT 、DML语句（INSERT、DELETE、 UPDATE）及DDL语句。 |

| > 文档版本：20260 | 729 |  | 13 |
|---|---|---|---|

数据传输

| --Flow | String | 1 | 每秒迁移或同步数据的流量，单位为MB/s。 |
|---|---|---|---|
| -ReverseJob | Struct | 详见以下结构体 | 反向同步任务执行详情。 当该任务为数据同步，且拓扑类型为双向时，才会返回该参数合集。 |
| --TagList | Array | 详见以下结构体 | 标签集合。 |
| ---Id | Long | 2 | 主键。 |
| ---GmtCreate | String | 2022-03- 16T08:01:19Z | 创建时间。 |
| ---GmtModified | String | 2022-03- 16T08:01:19Z | 修改时间。 |
| ---ResourceId | String | dtsnjuc14kp12u*** * | 数据迁移、同步和订阅的实例ID。 |
| --- ResourceType | String | ALIYUN::DTS::INST ANCE | 资源类型。 |
| ---RegionId | String | cn-hangzhou | 地域ID。 |
| ---AliUid | Long | 191448876515**** | 阿里云账号ID。 |
| ---TagKey | String | key1 | 标签键。 |
| ---TagValue | String | value1 | 标签值。 |
| ---TagCategory | String | System | 标签类型，取值： System：系统创建的标签。 Custom：用户添加的标签。 当值为空时，默认返回可公示的标签。 |
| ---SrcRegion | String | cn-hangzhou | 任务所在地域。 |

| 39 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| ---Scope | String | 0 | 标签的可见性，取值： 0：public 1：private |
|---|---|---|---|
| ---Creator | Long | 191448876515**** | 标签操作者。 |
| -- DtsInstanceID | String | 否 | dtsta7w132u12h**** |
| --DtsJobId | String | 是 | ta7w132u12h**** |
| --DtsJobName | String | api test _ | 迁移、同步或订阅任务名称。 |
| --GroupId | String | rg- acfmzawhxxc**** | 资源组ID。 |
| -- DatabaseCoun t | Integer | 2 | 如源实例为PolarDB-X 1.0时，需要输入其下挂 RDS MySQL的数量。 |
| --DtsJobClass | String | xlarge | 链路规格。 |
| -- DtsJobDirectio n | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 当数据同步实例的拓扑为双向时，才会返回本参数。 |
| -- Synchronizatio nDirection | String | 否 | Forward |
| --PayType | String | PrePaid | 实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| --ExpireTime | String | 2023-06- 16T08:01:19Z | 实例的到期时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明当 PayType参数的返回值为PrePaid时才会返回本参数。 |

| > 文档版本：20260 | 729 |  | 14 |
|---|---|---|---|

数据传输

| --CreateTime | String | 2022-03- 16T08:01:19Z | 任务创建时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| --FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| --DbObject | String | {\\"dtstestdata\\": {\\"all\\":true,\\"na me\\":\\"dtstestdat a\\",\\"state\\":\\"no rmal\\"}} | 迁移、同步或订阅对象。 |
| --Status | String | Migrating | 迁移或同步任务的状态，返回值为： NotStarted：未启动。 NotConfigured：未配置。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 Initializing：同步初始化中。 InitializeFailed：同步初始化失败。 synchronizing：同步中。 Migrating：迁移中。 Failed：同步失败。 MigrationFailed：迁移失败。 Suspending：暂停中。 Modifying：同步对象变更中。 Retrying：重试中。 Upgrade：升级中。 Downgrade：降级中。 Locked：锁定中。 Finished：完成。 |

数据传输

| -- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| --Delay | Long | 0 | 增量数据迁移或者同步的延迟时间，单位为毫秒。 |
| --Checkpoint | String | 1616405159 | 增量数据迁移的启动位点或者同步位点，格式为 Unix时间戳，单位为秒。 |
| --ReverseJob | String | **** | 反向同步任务执行详情。 当该任务为数据同步，且拓扑类型为双向时，才会返回该参数合集。 |

数据传输

| --Reserved | String | {\\"srcHostPorts\\": \\"\\",\\"whitelist.dm s.online.ddl.enable\ \":false,\\"filterDDL\ \":false,\\"sqlparser .dms.original.ddl\\" :true,\\"srcOracleTy pe\\":\\"sid\\",\\"ma xRetryTime\\":4320 0,\\"destSSL\\":\\"0\ \",\\"destOracleTyp e\\":\\"sid\\",\\"srcS SL\\":\\"0\\",\\"dbLis tCaseChangeMode\ \":\\"default\\",\\"So urceEngineVersion\ \":\\"8.0.18\\",\\"src NetType\\":\\"VPC\\ ",\\"destNetType\\": \\"VPC\\",\\"srcVpcN etMappingInst\\":\\" 172.16.1.:10803\\", \\"destVpcNetMapp ingInst\\":\\"172.16. 1.:11077\\",\\"useJo bTask\\":\\"1\\"} | DTS预留参数，格式为JSON串，可以传入本参数实现特殊需求（例如是否自动启动预检查）。 |
|---|---|---|---|
| -- SubscribeTopi c | String | cn hangzhou rm b _ _ _ p1162kryivb8**** _ dtstest version2 _ | 订阅Topic。 当该订阅实例为新版，且调用 CreateConsumerGroup接口创建了消费组时，才会返回本参数。 |
| -- ConsumptionC heckpoint | String | 2022-03- 23T07:30:31Z | 订阅任务的下游消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -- BeginTimesta mp | String | 2022-03- 15T08:25:34Z | 订阅实例中保存的数据范围的起始时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| -- EndTimestamp | String | 2022-03- 26T14:03:21Z | 订阅实例中保存的数据范围的截止时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| -- ConsumptionC lient | String | 114.*.*.:dts** | 下游消费客户端信息，由IP地址和DTS随机生成的随机数组成。 |
| --DestNetType | String | VPC | 消费客户端所属网络类型： CLASSIC：经典网络。 VPC：专有网络。 |

| 43 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| --AppName | String | new | 是否为新版订阅，new（新版订阅）。 说明该参数仅在新版订阅实例中返回。 |
|---|---|---|---|
| --EtlCalculator | String | { "cells ": \ [{\\"shape\\":\\"edg e\\",\\"attrs\\": {\\"line\\": {\\"stroke\\":\\"#b1 b1b1\\",\\"strokeWi dth\\":1,\\"targetMa rker\\": {\\"name\\":\\"bloc k\\",\\"args\\": {\\"size\\":\\"8\\"}}, \\"strokeDasharray\ \":\\"\\"}},\\"id\\":\\" cd1ec473-f9b9- 4e9b-a742- ac23f442**\\",\\"so urce\\": {\\"cell\\":\\"8b261 182-bfab-4803- ad8e- 6bb08e3e\\",\\"port \\":\\"out1\\"},\\"tar get\\": {\\"cell\\":\\"b3677 0df-f48c-4d6b- 9644- 54c5e924**\\",\\"po rt\\":\\"in1\\"},\\"zIn dex\\":7 }\] } | ETL任务的算子信息。 当任务为ETL时，才会返回本参数。 |
| --OriginType | String | DTS任务 | 任务来源： PTS任务 DMS任务 DTS任务 |
| --JobType | String | SYNC | DTS实例的任务类型，取值： online：迁移。 SYNC：同步。 SUBSCRIBE：订阅。 |
| --IsDemoJob | Boolean | false | 是否子任务，返回值： true：是。 false：否。 |
| --TaskType | String | rds | 任务类型。 |

| > 文档版本：20260 | 729 |  | 14 |
|---|---|---|---|

数据传输

| -- SourceEndpoin t | Struct | 详见以下结构体 | 源实例连接信息。 |
|---|---|---|---|
| ---InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| ---Region | String | cn-hangzhou | 源实例所在区域。 |
| --- InstanceType | String | RDS | 源实例类型。 |
| ---EngineName | String | MySQL | 源实例的数据库类型。 |
| ---Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| ---Port | String | 3306 | 源实例的数据库服务端口。 |
| --- DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| ---OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |
| ---UserName | String | dtstest | 源实例的数据库账号。 |
| --- SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
| ---TlsVersion | String | TLSv1.2 | TLS版本。 |
| ---RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |

| 45 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| ---AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
|---|---|---|---|
| -- DestinationEn dpoint | Struct | 详见以下结构体 | 目标实例的连接信息。 |
| ---InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| ---Region | String | cn-hangzhou | 源实例所在区域。 |
| --- InstanceType | String | RDS | 源实例类型。 |
| ---EngineName | String | MySQL | 源实例的数据库类型。 |
| ---Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| ---Port | String | 3306 | 源实例的数据库服务端口。 |
| --- DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| ---OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |
| ---UserName | String | dtstest | 源实例的数据库账号。 |
| --- SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
| ---TlsVersion | String | TLSv1.2 | TLS版本。 |

| > 文档版本：20260 | 729 |  | 14 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| ---RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |
|---|---|---|---|
| ---AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
| -- MigrationMode | Struct | 详见以下结构体 | 迁移类型或同步初始化类型。 |
| --- StructureInitial ization | Boolean | true | 是否执行库表结构迁移或初始化，返回值： true：是。 false：否。 |
| --- DataInitializati on | Boolean | true | 是否执行全量数据迁移或全量数据初始化，返回值： true：是。 false：否。 |
| --- DataSynchroni zation | Boolean | true | 是否执行增量数据迁移或同步，返回值： true：是。 false：否。 |
| --- DataExtractTr ansformLoad | Boolean | false | 是否执行数据加工，返回值： true：是。 false：否。 |
| -- PrecheckStatu s | Struct | 详见以下结构体 | 预检查状态。 |
| ---Detail | Array | 详见以下结构体 | 各预检查项的执行情况。 |
| ----CheckItem | String | CHECK CONN SRC _ _ | 预检查项目。 |
| ---- CheckItemDes cription | String | CHECK CONN SRC _ _ DETAIL _ | 预检查项目描述。 |
| ---- CheckResult | String | Success | 预检查结果，返回值为： Success：通过该项检查。 Failed：未通过该项检查。 |

数据传输

| ---- FailedReason | String | Original error: Access denied for user 'dtstest'@'100.104. *.' (using password: YES) | 预检查未通过的错误提示。 当CheckResult参数返回值为Failed时， 才会返回本参数。 |
|---|---|---|---|
| ---- RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 当CheckResult参数返回值为Failed时， 才会返回本参数。 |
| ---Status | String | Finished | 预检查状态，返回值为： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Finished：完成。 |
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |

数据传输

| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| -- StructureInitial izationStatus | Struct | 详见以下结构体 | 库表结构初始化状态。 |

数据传输

| ---Status | String | Finished | 库表结构初始化状态，取值包括： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
|---|---|---|---|
| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| ---Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| --- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| -- DataInitializati onStatus | Struct | 详见以下结构体 | 全量数据迁移或初始化的状态。 |

|  | 开发指南·API参考 |  |  | 数据传输 |  |
|---|---|---|---|---|---|

| ---Status | String | Finished | 全量数据迁移或初始化状态，取值包括： NotStarted：未启动。 Migrating：迁移或初始化中。 Failed：迁移或初始化失败。 Finished：迁移或初始化完成。 |
|---|---|---|---|
| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| ---Progress | String | 1 | 已完成库表结构初始化的表的数量。 |

| 51 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| 数据传输 |  |  | 开发指南·API参考 |
|---|---|---|---|

| --- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
|---|---|---|---|
| ---NetioCurrent | String | 10MB/s | 当前网络IO。 |
| ---TotalRow | String | 10000 | 总行数。 |
| ---FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| ---BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -- DataSynchroni zationStatus | Struct | 详见以下结构体 | 增量数据迁移或同步的状态。 |
| ---Status | String | Catched | 增量数据迁移或同步状态，返回值为： NotStarted：未启动。 Migrating：迁移或同步中。 Suspending：暂停中。 Checking：检查中。 Failed：迁移或同步失败。 Finished：迁移或同步完成。 Catched：无延迟。 |

数据传输

| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| ---Progress | String | 1 | 已完成库表结构初始化的表的数量。 |

| 53 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| --- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
|---|---|---|---|
| ---NetioCurrent | String | 10MB/s | 当前网络IO。 |
| ---TotalRow | String | 10000 | 总行数。 |
| ---FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| ---BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -- DataEtlStatus | Struct | 详见以下结构体 | ETL任务的状态。 配置ETL任务后，才会返回该参数集合。 |
| ---Status | String | Finished | ETL任务状态，返回值为： NotStarted：未启动。 Migrating：执行中。 Failed：执行失败。 Finished：完成。 Catched：无延迟。 |

数据传输

| --- ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| ---Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| ---Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| --- NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| --Performance | Struct | 详见以下结构体 | 迁移或同步链路的性能信息。 |
| ---Rps | String | 100 | 每秒迁移或同步SQL语句的次数，包括BEGIN、 COMMIT 、DML语句（INSERT、DELETE、 UPDATE）及DDL语句。 |
| ---Flow | String | 1 | 每秒迁移或同步数据的流量，单位为MB/s。 |

| 55 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| -- SubscriptionH ost | Struct | 详见以下结构体 | 订阅任务的连接地址。 |  |  |
|---|---|---|---|---|---|
| ---PublicHost | String | dts-cn- ****.aliyuncs.com: 18001 | 订阅任务的公网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| ---PrivateHost | String | dts-cn-****- internal.aliyuncs.co m:18002 | 订阅任务的私网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| ---VpcHost | String | dts-cn-****- vpc.aliyuncs.com:1 8003 | 订阅任务的专有网络VPC（Virtual Private Cloud）连接信息，格式为地址：端口号 。 |  |  |
| ---VpcHostIpV6 | String | dts-cn-****- vpc6.aliyuncs.com: 18003 | 订阅任务的VPC IPv6连接信息。 |  |  |
| -- SubscriptionD ataType | Struct | 详见以下结构体 | 订阅数据的类型。 |  |  |
| ---Ddl | Boolean | true | 订阅数据是否包含DDL语句，返回值： true：是。 false：否。 |  |  |
| ---Dml | Boolean | true | 订阅数据是否包含DML语句，返回值： true：是。 false：否。 |  |  |
| --RetryState | Struct | 详见以下结构体 | 由于任务异常，DTS正在重试。 |  |  |
| ---JobId | String | ta7w132u12h**** | 任务ID。 |  |  |
| --- MaxRetryTime | Integer | 7200 | 最大重试时间，单位为秒。 |  |  |
| ---RetryTime | Integer | 3600 | 已重试时间，单位为秒。 |  |  |
| ---RetryCount | Integer | 5 | 已重试次数。 |  |  |

| s.com: | 号 |
|---|---|

| uncs.co | 号 |
|---|---|

| > 文档版本：20260 | 729 |  | 15 |
|---|---|---|---|

数据传输

| ---Retrying | Boolean | true | 是否在重试中，返回值： true：是。 false：否。 |  |  |
|---|---|---|---|---|---|
| ---Module | String | 03 | 实例进展。 |  |  |
| ---RetryTarget | String | srcDB | 重试目标，返回值： srcDB：源数据库。 destDB：目标数据库。 inner module：DTS内部模块。 _ |  |  |
| ---ErrMsg | String | CHECK ERROR SA __ _ ME OBJ _ | 报错信息。 |  |  |
| - SubscriptionH ost | Struct | 详见以下结构体 | 订阅任务的连接地址。 |  |  |
| --PublicHost | String | dts-cn- ****.aliyuncs.com: 18001 | 订阅任务的公网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| --PrivateHost | String | dts-cn-****- internal.aliyuncs.co m:18002 | 订阅任务的私网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| --VpcHost | String | dts-cn-****- vpc.aliyuncs.com:1 8003 | 订阅任务的专有网络VPC（Virtual Private Cloud）连接信息，格式为地址：端口号 。 |  |  |
| --VpcHostIpV6 | String | dts-cn-****- vpc6.aliyuncs.com: 18003 | 订阅任务的VPC IPv6连接信息。 |  |  |
| - SubscriptionD ataType | Struct | 详见以下结构体 | 订阅数据的类型。 |  |  |
| --Ddl | Boolean | true | 订阅数据是否包含DDL语句，返回值： true：是。 false：否。 |  |  |

| s.com: | 号 |
|---|---|

| uncs.co | 号 |
|---|---|

| 57 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| --Dml | Boolean | true | 订阅数据是否包含DML语句，返回值： true：是。 false：否。 |
|---|---|---|---|
| -RetryState | Struct | 详见以下结构体 | 由于任务异常，DTS正在重试。 |
| --JobId | String | ta7w132u12h**** | 任务ID。 |
| -- MaxRetryTime | Integer | 7200 | 最大重试时间，单位为秒。 |
| --RetryTime | Integer | 3600 | 已重试时间，单位为秒。 |
| --RetryCount | Integer | 5 | 已重试次数。 |
| --Retrying | Boolean | true | 是否在重试中，返回值： true：是。 false：否。 |
| --Module | String | 03 | 实例进展。 |
| --RetryTarget | String | srcDB | 重试目标，返回值： srcDB：源数据库。 destDB：目标数据库。 inner module：DTS内部模块。 _ |
| --ErrMsg | String | CHECK ERROR SA __ _ ME OBJ _ | 报错信息。 |

数据传输

| Status | String | Migrating | 迁移或同步任务的状态，返回值为： NotStarted：未启动。 NotConfigured：未配置。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 Initializing：同步初始化中。 InitializeFailed：同步初始化失败。 synchronizing：同步中。 Migrating：迁移中。 Failed：同步失败。 MigrationFailed：迁移失败。 Suspending：暂停中。 Modifying：同步对象变更中。 Retrying：重试中。 Upgrade：升级中。 Downgrade：降级中。 Locked：锁定中。 Finished：完成。 |
|---|---|---|---|
| DtsJobName | String | api test _ | 迁移、同步或订阅任务名称。 |
| FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

数据传输

| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| DtsJobId | String | 是 | ta7w132u12h**** |
| CreateTime | String | 2022-03- 16T08:01:19Z | 任务创建时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| PayType | String | PrePaid | 实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |

数据传输

| Reserved | String | {\\"srcHostPorts\\": \\"\\",\\"whitelist.dm s.online.ddl.enable\ \":false,\\"filterDDL\ \":false,\\"sqlparser .dms.original.ddl\\" :true,\\"srcOracleTy pe\\":\\"sid\\",\\"ma xRetryTime\\":4320 0,\\"destSSL\\":\\"0\ \",\\"destOracleTyp e\\":\\"sid\\",\\"srcS SL\\":\\"0\\",\\"dbLis tCaseChangeMode\ \":\\"default\\",\\"So urceEngineVersion\ \":\\"8.0.18\\",\\"src NetType\\":\\"VPC\\ ",\\"destNetType\\": \\"VPC\\",\\"srcVpcN etMappingInst\\":\\" 172.16.1.:10803\\", \\"destVpcNetMapp ingInst\\":\\"172.16. 1.:11077\\",\\"useJo bTask\\":\\"1\\"} | DTS预留参数，格式为JSON串，可以传入本参数实现特殊需求（例如是否自动启动预检查）。 |
|---|---|---|---|
| DatabaseCoun t | Integer | 2 | 如源实例为PolarDB-X 1.0时，需要输入其下挂 RDS MySQL的数量。 |
| DtsJobClass | String | xlarge | 链路规格。 |
| EndTimestamp | String | 2022-03- 26T14:03:21Z | 订阅实例中保存的数据范围的截止时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| AppName | String | new | 是否为新版订阅，new（新版订阅）。 该参数仅在新版订阅实例中返回。 |
| DestNetType | String | VPC | 消费客户端所属网络类型： CLASSIC：经典网络。 VPC：专有网络。 |
| SubscribeTopi c | String | cn hangzhou rm b _ _ _ p1162kryivb8**** _ dtstest version2 _ | 订阅Topic。 当该订阅实例为新版，且调用 CreateConsumerGroup接口创建了消费组时，才会返回本参数。 |
| DtsInstanceID | String | 否 | dtsta7w132u12h**** |

| 61 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| RequestId | String | 29207299-7C41- 493A-BA4F- 2FAC5DE4**** | 请求ID。 |
|---|---|---|---|
| Code | Integer | 200 | 错误码，本参数即将下线。 |
| Checkpoint | Long | 1616405159 | 增量数据迁移的启动位点或者同步位点，格式为 Unix时间戳，单位为秒。 |
| InitCheckpoint | Long | 1616405159 | 增量迁移或同步的初始化位点，格式为Unix时间戳，单位为秒。 |
| Delay | Long | 0 | 增量数据迁移或者同步的延迟时间，单位为毫秒。 |
| ExpireTime | String | 2023-06- 16T08:01:19Z | 实例的到期时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 当PayType参数的返回值为PrePaid时才会返回本参数。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| ConsumptionC lient | String | 114.*.*.:dts** | 下游消费客户端信息，由IP地址和DTS随机生成的随机数组成。 |
| DbObject | String | {\\"dtstestdata\\": {\\"all\\":true,\\"na me\\":\\"dtstestdat a\\",\\"state\\":\\"no rmal\\"}} | 迁移、同步或订阅对象。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的%s。 如果ErrMessage返回The Value of Input Parameter %s is not valid，且 DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |

| > 文档版本：20260 | 729 |  | 16 |
|---|---|---|---|

数据传输

| ConsumptionC heckpoint | String | 2022-03- 23T07:30:31Z | 订阅任务的下游消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| EtlCalculator | String | { "cells ": \ [{\\"shape\\":\\"edg e\\",\\"attrs\\": {\\"line\\": {\\"stroke\\":\\"#b1 b1b1\\",\\"strokeWi dth\\":1,\\"targetMa rker\\": {\\"name\\":\\"bloc k\\",\\"args\\": {\\"size\\":\\"8\\"}}, \\"strokeDasharray\ \":\\"\\"}},\\"id\\":\\" cd1ec473-f9b9- 4e9b-a742- ac23f442**\\",\\"so urce\\": {\\"cell\\":\\"8b261 182-bfab-4803- ad8e- 6bb08e3e\\",\\"port \\":\\"out1\\"},\\"tar get\\": {\\"cell\\":\\"b3677 0df-f48c-4d6b- 9644- 54c5e924**\\",\\"po rt\\":\\"in1\\"},\\"zIn dex\\":7 }\] } | ETL任务的算子信息。 当任务为ETL时，才会返回本参数。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| BeginTimesta mp | String | 2022-03- 15T08:25:34Z | 订阅实例中保存的数据范围的起始时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| GroupId | String | rg- acfmzawhxxc**** | 资源组ID。 |
| Synchronizatio nDirection | String | 否 | Forward |
| DtsJobDirectio n | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 当数据同步实例的拓扑为双向时，才会返回本参数。 |

| 63 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| DemoJob | Boolean | false | 是否子任务，返回值： true：是。 false：否。 |
|---|---|---|---|
| JobType | String | SYNC | DTS实例的任务类型，取值： online：迁移。 SYNC：同步。 SUBSCRIBE：订阅。 |
| TaskType | String | rds | 任务类型。 |
| DedicatedClus terId | String | dtsxxxxx | 专属集群ID。 |
| BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Binlog | String | **** | Binlog信息。 |
| BinlogSite | String | 156629109**** | 当前位点。 |
| BinlogTime | String | **** | 位点范围。 |
| LastUpdateTi me | String | 156629109**** | 最后一次更新的时间戳。 |
| ResourceGrou pId | String | rg- acfmzawhxxc**** | 资源组ID。 |
| ResourceGrou pDisplayName | String | default resource group | 资源组名称。 |
| DtsBisLabel | String | normal | DTS实例的环境标签，返回值： normal：普通 online：线上 |
| SourceEndpoin t | Struct | 详见以下结构体 | 源实例连接信息。 |

数据传输

| -OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |
|---|---|---|---|
| - SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
| -Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| -InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| -RoleName | String | ram-for-dts | 源实例所属云账号配置的角色名称。 |
| -InstanceType | String | RDS | 源实例类型。 |
| -Port | String | 3306 | 源实例的数据库服务端口。 |
| -EngineName | String | MySQL | 源实例的数据库类型。 |
| -Region | String | cn-hangzhou | 源实例所在区域。 |
| - DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| -AliyunUid | String | 140692647406**** | 源实例所属的阿里云账号ID。 |
| -UserName | String | dtstest | 源实例的数据库账号。 |
| - CanModifyPass word | Boolean | false | 是否可以修改密码，返回值： true：是。 false：否。 |

| 65 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| DestinationEn dpoint | Struct | 详见以下结构体 | 目标实例的连接信息。 |
|---|---|---|---|
| - SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：未使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用SSL安 _ _ 全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS：使 _ _ _ _ 用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SHA 2 _ _ _ _ _ _ 56：使用SCRAM-SHA-256连接Kafka。 |
| -OracleSID | String | testsid | Oracle数据库的SID信息。 当源实例的EngineName取值为Oracle， 且Oracle数据库为非RAC实例时，才会返回本参数。 |
| - DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| -Region | String | cn-hangzhou | 源实例所在区域。 |
| -Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| -InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| -Port | String | 3306 | 源实例的数据库服务端口。 |
| -InstanceType | String | RDS | 源实例类型。 |
| -UserName | String | dtstest | 源实例的数据库账号。 |
| -EngineName | String | MySQL | 源实例的数据库类型。 |
| - CanModifyPass word | Boolean | false | 是否可以修改密码，返回值： true：是。 false：否。 |
| MigrationMode | Struct | 详见以下结构体 | 迁移类型或同步初始化类型。 |

| > 文档版本：20260 | 729 |  | 16 |
|---|---|---|---|

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| - DataExtractTr ansformLoad | Boolean | false | 是否执行数据加工，返回值： true：是。 false：否。 |  |  |
|---|---|---|---|---|---|
| - DataInitializati on | Boolean | true | 是否执行全量数据迁移或全量数据初始化，返回值： true：是。 false：否。 |  |  |
| - DataSynchroni zation | Boolean | true | 是否执行增量数据迁移或同步，返回值： true：是。 false：否。 |  |  |
| - StructureInitial ization | Boolean | true | 是否执行库表结构迁移或初始化，返回值： true：是。 false：否。 |  |  |
| SubscriptionH ost | Struct | 详见以下结构体 | 订阅任务的连接地址。 |  |  |
| -VpcHost | String | dts-cn-****- vpc.aliyuncs.com:1 8003 | 订阅任务的专有网络VPC（Virtual Private Cloud）连接信息，格式为地址：端口号 。 |  |  |
| -PublicHost | String | dts-cn- ****.aliyuncs.com: 18001 | 订阅任务的公网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| -PrivateHost | String | dts-cn-****- internal.aliyuncs.co m:18002 | 订阅任务的私网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| -VpcHostIpV6 | String | dts-cn-****- vpc6.aliyuncs.com: 18003 | 订阅任务的VPC IPv6连接信息。 |  |  |
| SubscriptionD ataType | Struct | 详见以下结构体 | 订阅数据的类型。 |  |  |
| -Dml | Boolean | true | 订阅数据是否包含DML语句，返回值： true：是。 false：否。 |  |  |

| s.com: | 号 |
|---|---|

| uncs.co | 号 |
|---|---|

| 67 |  |  | > 文档版本：2026072 |
|---|---|---|---|

数据传输

| -Ddl | Boolean | true | 订阅数据是否包含DDL语句，返回值： true：是。 false：否。 |
|---|---|---|---|
| DataSynchroni zationStatus | Struct | 详见以下结构体 | 增量数据迁移或同步的状态。 |
| -Status | String | Catched | 增量数据迁移或同步状态，返回值： NotStarted：未启动。 Migrating：迁移或同步中。 Suspending：暂停中。 Checking：检查中。 Failed：迁移或同步失败。 Finished：迁移或同步完成。 Catched：无延迟。 |
| -NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| -Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| -Progress | String | 1 | 已完成库表结构初始化的表的数量。 |

数据传输

| -ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |
|---|---|---|---|
| -NetioCurrent | String | 10MB/s | 当前网络IO。 |
| -TotalRow | String | 10000 | 总行数。 |
| -FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -SrcTotalRow | String | 10000 | 源端总行数。 |
| DataInitializati onStatus | Struct | 详见以下结构体 | 全量数据迁移或初始化的状态。 |

数据传输

| -Status | String | Finished | 全量数据迁移或初始化状态，取值： NotStarted：未启动。 Migrating：迁移或初始化中。 Failed：迁移或初始化失败。 Finished：迁移或初始化完成。 |
|---|---|---|---|
| -ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by \ [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.\]\ [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\ \ The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.\]\ [java.net.ConnectE xception:Connectio n timed out (Connection timed out)\] About more information in \ [https://yq.aliyun.c om/articles/499178 \]. | 任务失败的错误提示。 |

数据传输

| -Percent | String | 100 | 预检查整体进度，单位为百分比。 |
|---|---|---|---|
| -Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| -NeedUpgrade | Boolean | true | 是否显示提升升级规格，返回值： true：是。 false：否。 |
| -NetioCurrent | String | 10MB/s | 当前网络IO。 |
| -TotalRow | String | 10000 | 总行数。 |
| -FinishTime | String | 2023-06- 16T10:34:17Z | 任务结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -BootTime | String | 2022-03- 30T03:36:11.000 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -SrcTotalRow | String | 10000 | 源端总行数。 |
| RetryState | Struct | 详见以下结构体 | 由于任务异常，DTS正在重试。 |
| -RetryCount | Integer | 5 | 已重试次数。 |
| - MaxRetryTime | Integer | 7200 | 最大重试时间，单位为秒。 |
| -ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |

数据传输

| -RetryTarget | String | srcDB | 重试目标，返回值： srcDB：源数据库。 destDB：目标数据库。 inner module：DTS内部模块。 _ |
|---|---|---|---|
| -RetryTime | Integer | 3600 | 已重试时间，单位为秒。 |
| -Module | String | 03 | 实例进展。 |
| -JobId | String | ta7w132u12h**** | 任务ID。 |
| -Retrying | Boolean | true | 是否在重试中，返回值： true：是。 false：否。 |
| DataDeliveryC hannelInfo | Struct | 详见以下结构体 | 数据投递通道信息。 |
| - PublicDproxyU rl | String | dts- **.aliyuncs.com:18 * | 投递通道的公网地址。 |
| -VpcDproxyUrl | String | dts- **.aliyuncs.com:18 * | 投递通道的VPC网络地址。 |
| -Topic | String | cn hangzhou ** d _ _ _ ata delivery versio _ _ n2 | 投递的目标Topic。 |
| -Region | String | cn-hangzhou | 源实例所在区域。 |
| -PartitionNum | Integer | 3 | 投递Topic的分片数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDtsJobDetail
```

&公共请求参数正常返回示例 `JSON` 格式数据传输

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "DtsJobName" : "api测试",
  "DtsInstanceID" : "dtsi03e3zty16i****",
  "Success" : true,
  "Delay" : 0,
  "MigrationMode" : {
    "DataInitialization" : true,
    "DataSynchronization" : true,
    "StructureInitialization" : true
  },
  "DtsJobClass" : "xlarge",
  "DtsJobId" : "i03e3zty16i****",
  "HttpStatusCode" : 200,
  "Status" : "Migrating",
  "RequestId" : "29207299-7C41-493A-BA4F-2FAC5DE4****",
  "DbObject" : "{\"dtstestdata\":
{\"all\":true,\"name\":\"dtstestdata\",\"state\":\"normal\"}}",
  "CreateTime" : "2021-03-16T08:01:19Z",
  "PayType" : "PostPaid",
  "Checkpoint" : "1616405159",
  "DestinationEndpoint" : {
    "UserName" : "dtstest",
    "InstanceID" : "rm-bp1imrtn6fq7h****",
    "SslSolutionEnum" : "DISABLE",
    "Port" : "3306",
    "DatabaseName" : "dtstestdata",
    "Region" : "cn-hangzhou",
    "InstanceType" : "RDS",
    "EngineName" : "MySQL"
  },
  "SourceEndpoint" : {
    "RoleName" : "",
    "UserName" : "dtstest",
    "InstanceID" : "rm-bp1162kryivb8****",
    "SslSolutionEnum" : "DISABLE",
    "Port" : "3306",
    "AliyunUid" : "140692647406****",
    "Region" : "cn-hangzhou",
    "InstanceType" : "RDS",
    "EngineName" : "MySQL"
  },
  "Reserved" : "
{\"srcHostPorts\":\"\",\"whitelist.dms.online.ddl.enable\":false,\"filterDDL\":false,\"sq arser.dms.original.ddl\":true,\"srcOracleType\":\"sid\",\"maxRetryTime\":43200,\"destSSL\ \"0\",\"destOracleType\":\"sid\",\"srcSSL\":\"0\",\"dbListCaseChangeMode\":\"default\",\" urceEngineVersion\":\"8.0.18\",\"srcNetType\":\"VPC\",\"destNetType\":\"VPC\",\"srcVpcNet ppingInst\":\"172.16.1**.**:1****\",\"destVpcNetMappingInst\":\"172.16.1**.**:1****\",\"u JobTask\":\"1\"}" }
```

数据传输 `XML` 格式

```xml
<DtsJobName>api测试</DtsJobName> <DtsInstanceID>dtsi03e3zty16i****</DtsInstanceID> <Success>true</Success> <Delay>0</Delay> <MigrationMode>
  <DataInitialization>true</DataInitialization>
  <DataSynchronization>true</DataSynchronization>
  <StructureInitialization>true</StructureInitialization>
</MigrationMode> <DtsJobClass>xlarge</DtsJobClass> <DtsJobId>i03e3zty16i****</DtsJobId> <HttpStatusCode>200</HttpStatusCode> <Status>Migrating</Status> <RequestId>29207299-7C41-493A-BA4F-2FAC5DE4****</RequestId> <DbObject>{&quot;dtstestdata&quot;: {&quot;all&quot;:true,&quot;name&quot;:&quot;dtstestdata&quot;,&quot;state&quot;:&quot;no al&quot;}}</DbObject> <CreateTime>2021-03-16T08:01:19Z</CreateTime> <PayType>PostPaid</PayType> <Checkpoint>1616405159</Checkpoint> <DestinationEndpoint>
  <UserName>dtstest</UserName>
  <InstanceID>rm-bp1imrtn6fq7h****</InstanceID>
  <SslSolutionEnum>DISABLE</SslSolutionEnum>
  <Port>3306</Port>
  <DatabaseName>dtstestdata</DatabaseName>
  <Region>cn-hangzhou</Region>
  <InstanceType>RDS</InstanceType>
  <EngineName>MySQL</EngineName>
</DestinationEndpoint> <SourceEndpoint>
  <RoleName  />
  <UserName>dtstest</UserName>
  <InstanceID>rm-bp1162kryivb8****</InstanceID>
  <SslSolutionEnum>DISABLE</SslSolutionEnum>
  <Port>3306</Port>
  <AliyunUid>140692647406****</AliyunUid>
  <Region>cn-hangzhou</Region>
  <InstanceType>RDS</InstanceType>
  <EngineName>MySQL</EngineName>
</SourceEndpoint> <Reserved> {&quot;srcHostPorts&quot;:&quot;&quot;,&quot;whitelist.dms.online.ddl.enable&quot;:false, uot;filterDDL&quot;:false,&quot;sqlparser.dms.original.ddl&quot;:true,&quot;srcOracleType uot;:&quot;sid&quot;,&quot;maxRetryTime&quot;:43200,&quot;destSSL&quot;:&quot;0&quot;,&qu ;destOracleType&quot;:&quot;sid&quot;,&quot;srcSSL&quot;:&quot;0&quot;,&quot;dbListCaseCh geMode&quot;:&quot;default&quot;,&quot;SourceEngineVersion&quot;:&quot;8.0.18&quot;,&quot rcNetType&quot;:&quot;VPC&quot;,&quot;destNetType&quot;:&quot;VPC&quot;,&quot;srcVpcNetMa ingInst&quot;:&quot;172.16.1**.**:1****&quot;,&quot;destVpcNetMappingInst&quot;:&quot;172 6.1**.**:1****&quot;,&quot;useJobTask&quot;:&quot;1&quot;}</Reserved>
```

数据传输

##### 查询DTS任务列表及各任务执行详情

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDtsJobs | 系统规定参数，取值：DescribeDtsJobs。 |
| Region | String | 是 | cn-hangzhou | DTS实例所在地域。 |
| Type | String | 否 | instance | 传入本参数，指定查询条件，取值： instance：根据DTS实例ID查询。 name：根据DTS实例名称查询，支持模糊查询。 srcRds：根据RDS源实例ID查询。 rds：根据RDS目标实例ID查询。 说明您需要传入Params， 指定查询条件的具体内容。 |
| Params | String | 否 | dtspk3f13r731m **** | 查询条件的具体内容。 说明您需要提前传入Type，指定查询条件。 |

数据传输

| Status | String | 否 | Migrating | DTS实例状态，取值： 迁移任务状态： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 NotConfigured：未配置。 Migrating：迁移中。 Suspending：暂停中。 MigrationFailed：迁移失败。 Finished：完成。 Retrying：重试中。 Upgrade：升级中。 Locked：锁定中。 Downgrade：降级中。 同步任务状态： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 NotConfigured：未配置。 Initializing：同步初始化中。 InitializeFailed：同步初始化失败。 Synchronizing：同步中。 Failed：同步失败。 Suspending：暂停中。 Modifying：修改子对象中。 Finished：完成。 Retrying：重试中。 Upgrade：升级中。 Locked：锁定中。 Downgrade：降级中。 订阅任务的状态： NotConfigured：未配置。 NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 Starting：启动中。 Normal：正常。 Retrying：重试中。 Abnormal：异常。 Upgrade：升级中。 Locked：锁定中。 Downgrade：降级中。 |
|---|---|---|---|---|

数据传输

| OrderDirection | String | 否 | ASC | 传入本参数指定实例排序顺序，取值： ASC：正序，为默认值。 DESC：倒序。 |
|---|---|---|---|---|
| OrderColumn | String | 否 | CreateTime | 当返回结果包含多个DTS实例时，传入本参数指定实例的排序依据，取值： CreateTime：按照实例的任务创建顺序排序。 FinishTime：按照实例的任务完成顺序排序。 说明您还可以传入OrderDirection，指定实例排序顺序为正序或倒序。 |
| Tags | String | 否 | [ { \"key\": \"testK\", \"value\": \"testV\" } ] | 标签搜索条件，格式为JSON。 说明标签的键和值，可通过调用ListTagResources接口查询。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30、50、100，默认值为30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| JobType | String | 否 | MIGRATION | DTS实例的任务类型，取值： MIGRATION：迁移（默认值）。 SYNC：同步。 SUBSCRIBE：订阅。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所在地域。 |
| GroupId | String | 否 | pk13r731m**** | DTS任务ID。 说明一般情况下无需设置该参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DtsJobList | Array of DtsJobStatus |  | 任务列表及各任务执行详情。 |

数据传输

| AppName | String | new | 是否为新版订阅，new（新版订阅）。 说明该参数仅在新版订阅实例中返回。 |
|---|---|---|---|
| BeginTimesta mp | String | 2021-03- 15T08:25:34Z | 订阅实例中保存的数据范围的起始时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| Checkpoint | String | 1616899019 | 增量数据迁移的启动位点或者同步位点，格式为 Unix时间戳，单位为秒。 |
| ConsumptionC heckpoint | String | 2021-03- 23T07:30:31Z | 订阅实例的下游消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| ConsumptionC lient | String | 114...:dts****** | 下游消费客户端信息，由IP地址和DTS随机生成的随机数组成。 |
| CreateTime | String | 2021-03- 16T08:01:19Z | 任务创建时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| DataEtlStatus | Struct |  | ETL任务的状态。 说明配置ETL任务后，才会返回该参数集合。 |
| ErrorMessage | String | 任务失败太久无法恢复 | ETL任务失败的错误提示。 |
| Percent | String | 95 | ETL任务进度。 |
| Progress | String | 0/0 | 已完成ETL任务的记录数。 |
| Status | String | Finished | ETL任务状态，返回值为： NotStarted：未启动。 Migrating：执行中。 Failed：执行失败。 Finished：完成。 Catched：无延迟。 |
| DataInitializati onStatus | Struct |  | 全量数据迁移或初始化的状态。 |

数据传输

| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据迁移或初始化失败的错误提示。 |
|---|---|---|---|
| Percent | String | 100 | 全量数据迁移或初始化进度，单位为百分比。 |
| Progress | String | 44755 | 已完成全量数据迁移或初始化的记录数。 |
| Status | String | Finished | 全量数据迁移或初始化状态，取值包括： NotStarted：未启动。 Migrating：迁移或初始化中。 Failed：迁移或初始化失败。 Finished：迁移或初始化完成。 |
| DataSynchroni zationStatus | Struct |  | 增量数据迁移或同步的状态。 |
| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据迁移或同步失败的错误提示。 |
| NeedUpgrade | Boolean | true | 是否需要升级实例规格，返回值： true：需要。 false：不需要。 说明如需升级实例规格，请调用 TransferInstanceClass进行升级。 |
| Percent | String | 95 | 增量数据迁移或同步进度。 |
| Progress | String | 0/0 | 已完成增量数据迁移或同步的记录数。 |
| Status | String | Catched | 增量数据迁移或同步状态，返回值为： NotStarted：未启动。 Migrating：迁移或同步中。 Failed：迁移或同步失败。 Finished：迁移或同步完成。 Catched：无延迟。 |
| DbObject | String | {"dtstestdata": { "name": "dtstestdata", "all": true }} | 迁移、同步或订阅对象。 |

数据传输

| Delay | Long | 0 | 增量数据迁移或者同步的延迟时间。 说明如查询迁移任务，该参数的单位为毫秒，如查询同步任务，该参数的单位为秒。 |
|---|---|---|---|
| DestinationEn dpoint | Struct |  | 目标实例的连接信息。 |
| DatabaseNam e | String | dtstestdata | 目标实例中迁移对象所属数据库的名称。 |
| EngineName | String | MySQL | 目标实例的数据库类型。 |
| InstanceID | String | rm- bp1imrtn6fq7h**** | 目标实例ID。 |
| InstanceType | String | RDS | 目标实例类型。 |
| Ip | String | 172.16.88.*** | 目标实例的连接地址。 |
| OracleSID | String | testsid | Oracle数据库的SID信息。 说明当目标实例的EngineName取值为Oracle，且 Oracle数据库为非RAC实例时，才会返回本参数。 |
| Port | String | 3306 | 目标实例的数据库服务端口。 |
| Region | String | cn-hangzhou | 目标实例所在区域。 |
| SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：不使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用 _ _ SSL安全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS _ _ _ _ ：使用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SH _ _ _ _ _ A 256：使用SCRAM-SHA-256连接 _ Kafka。 |
| UserName | String | dtstest | 目标实例的数据库账号。 |
| DtsInstanceID | String | dtsi03e3zty16i**** | 迁移、同步或订阅实例ID。 |

数据传输

| DtsJobClass | String | large | 链路规格。 |
|---|---|---|---|
| DtsJobDirectio n | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 说明当数据同步实例的拓扑为双向时，才会返回本参数。 |
| DtsJobId | String | i03e3zty16i**** | 迁移、同步或订阅任务ID。 |
| DtsJobName | String | RDS间迁移 | 迁移、同步或订阅任务名称。 |
| EndTimestamp | String | 2021-03- 26T14:03:21Z | 订阅实例中保存的数据范围的截止时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectE xception:Connectio n timed out (Connection timed out)] About more information in [https://yq.aliyun.c om/articles/499178 ]. | 任务失败的错误提示。 |

数据传输

| ExpireTime | String | 2022-03- 16T08:01:19Z | 实例的到期时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明当PayType参数的返回值为PrePaid时才会返回本参数。 |
|---|---|---|---|
| MigrationMode | Struct |  | 迁移类型或同步初始化类型。 |
| DataInitializati on | Boolean | true | 是否执行全量数据迁移或全量数据初始化，返回值： true：是。 false：否。 |
| DataSynchroni zation | Boolean | true | 是否执行增量数据迁移或同步，返回值： true：是。 false：否。 |
| StructureInitial ization | Boolean | true | 是否执行库表结构迁移或初始化，返回值： true：是。 false：否。 |
| OriginType | String | DTS任务 | 标注任务来源： PTS任务 DMS任务 DTS任务 |
| PayType | String | PrePaid | 实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| Performance | Struct |  | 迁移或同步链路的性能信息。 |
| Flow | String | 1 | 每秒迁移或同步数据的流量，单位为MB/s。 |
| Rps | String | 100 | 每秒迁移或同步SQL语句的次数，包括BEGIN、 COMMIT 、DML语句（INSERT、DELETE、 UPDATE）及DDL语句。 |
| PrecheckStatu s | Struct |  | 预检查状态。 |
| Detail | Array of PrecheckDetail |  | 各预检查项的执行情况。 |

数据传输

| CheckItem | String | CHECK CONN SRC _ _ | 预检查项目。 |
|---|---|---|---|
| CheckItemDes cription | String | CHECK CONN SRC _ _ DETAIL _ | 预检查项目描述。 |
| CheckResult | String | Success | 检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
| FailedReason | String | Original error: Access denied for user 'dtstest'@'100.104. ***.**' (using password: YES) | 预检查未通过的错误提示。 说明当CheckResult参数返回值为Failed时，才会返回本参数。 |
| RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 说明当CheckResult参数返回值为Failed时，才会返回本参数。 |
| ErrorMessage | String | CHECK ERROR SA __ _ ME OBJ. _ | 预检查失败的原因。 |
| Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| Status | String | Finished | 预检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
| Reserved | String | {\"srcHostPorts\":\" \",\"whitelist.dms.o nline.ddl.enable\":f alse,\"filterDDL\":fa lse,\"sqlparser.dms .original.ddl\":true,\ "srcOracleType\":\" sid\",\"maxRetryTi me\":43200,\"destS SL\":\"0\",\"destOra cleType\":\"sid\",\"s rcSSL\":\"0\",\"dbLi stCaseChangeMod e\":\"default\",\"So urceEngineVersion\ ":\"8.0.18\",\"srcNet Type\":\"VPC\",\"de stNetType\":\"VPC\" ,\"srcVpcNetMappi ngInst\":\"172.16.1 **.**:10803\",\"des tVpcNetMappingIns t\":\"172.16.1**.**: 11077\",\"useJobTa sk\":\"1\"} | DTS预留参数，格式为JSON串，您可以传入本参数实现特殊需求（例如是否自动启动预检查）。 |

数据传输

| RetryState | Struct |  | 由于任务异常，DTS正在重试。 |
|---|---|---|---|
| ErrMessage | String | Unexpected error | 重试失败的错误提示。 |
| MaxRetryTime | Integer | 7200 | 最大重试时间，单位为秒。 |
| RetryCount | Integer | 5 | 已重试次数。 |
| RetryTarget | String | srcDB | 重试目标，返回值： srcDB：源数据库。 destDB：目标数据库。 inner module：DTS内部模块。 _ |
| RetryTime | Integer | 3600 | 已重试时间，单位秒。 |
| ReverseJob | Struct |  | 反向同步任务执行详情。 说明当该任务为数据同步，且拓扑类型为双向时，才会返回该参数合集。 |
| Checkpoint | String | 1616980369 | 增量数据同步位点，格式为Unix时间戳，单位为秒。 |
| CreateTime | String | 2021-03- 16T08:01:19Z | 任务创建时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| DataInitializati onStatus | Struct |  | 全量数据初始化的状态。 |
| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据初始化失败的错误提示。 |
| Percent | String | 100 | 全量数据初始化进度，单位为百分比。 |
| Progress | String | 43071 | 已完成全量数据初始化的记录数。 |
| Status | String | Finished | 全量数据初始化状态，取值包括： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |

数据传输

| DataSynchroni zationStatus | Struct |  | 增量数据同步的状态。 |
|---|---|---|---|
| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据同步失败的错误提示。 |
| NeedUpgrade | Boolean | true | 是否需要升级实例规格，返回值： true：需要。 false：不需要。 说明如需升级实例规格，请调用 TransferInstanceClass进行升级。 |
| Percent | String | 100 | 增量数据同步进度。 |
| Progress | String | 20001 | 已完成增量数据迁移或同步的记录数。 |
| Status | String | Migrating | 增量数据同步状态。 |
| DbObject | String | {"dtstestdata": { "name": "dtstestdata", "all": true }} | 同步对象的库表结构定义，格式为JSON串，且支持一定的正则表达式。更多相关介绍和示例，请参见迁移、同步或订阅对象配置说明。 |
| Delay | Long | 0 | 增量数据同步的延迟时间，单位为秒。 |
| DestinationEn dpoint | Struct |  | 目标实例的连接信息。 |
| DatabaseNam e | String | dtstestdata | 目标实例中同步对象所属数据库的名称。 |
| EngineName | String | MySQL | 目标实例的数据库类型。 |
| InstanceID | String | rm- bp1162kryivb8**** | 目标实例ID。 |
| InstanceType | String | RDS | 目标实例类型。 |
| Ip | String | 172.16.88.*** | 目标实例的连接地址。 |
| OracleSID | String | testsid | Oracle数据库的SID信息。 说明当目标实例的EngineName取值为Oracle，且 Oracle数据库为非RAC实例时，才会返回本参数。 |

数据传输

| Port | String | 3306 | 目标实例的数据库服务端口。 |
|---|---|---|---|
| Region | String | cn-hangzhou | 目标实例所在区域。 |
| SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：不使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用 _ _ SSL安全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS _ _ _ _ ：使用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SH _ _ _ _ _ A 256：使用SCRAM-SHA-256连接 _ Kafka。 |
| UserName | String | dtstest | 目标实例的数据库账号。 |
| DtsInstanceID | String | dtsi03e3zty16i**** | 同步实例ID。 |
| DtsJobClass | String | large | 链路规格。 |
| DtsJobDirectio n | String | Reverse | 同步方向，固定为Reverse（反向）。 |
| DtsJobId | String | i03e3zty16i**** | 同步任务ID。 |
| DtsJobName | String | RDS间迁移 | 同步任务名称。 |

数据传输

| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectE xception:Connectio n timed out (Connection timed out)] About more information in [https://yq.aliyun.c om/articles/499178 ]. | 任务失败的错误提示。 |
|---|---|---|---|
| ExpireTime | String | 2022-03- 16T08:01:19Z | 实例的到期时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明当PayType参数的返回值为PrePaid时才会返回本参数。 |
| MigrationMode | Struct |  | 同步初始化类型。 |
| DataInitializati on | Boolean | true | 是否执行全量数据初始化，返回值： true：是。 false：否。 |
| DataSynchroni zation | Boolean | true | 是否执行增量数据同步，返回值： true：是。 false：否。 |

数据传输

| StructureInitial ization | Boolean | true | 是否执行库表结构初始化，返回值： true：是。 false：否。 |
|---|---|---|---|
| PayType | String | PostPaid | 实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| Performance | Struct |  | 同步链路的性能信息。 |
| Flow | String | 1 | 每秒同步数据的流量，单位为MB/s。 |
| Rps | String | 100 | 每秒同步SQL语句的次数，包括BEGIN、 COMMIT 、DML语句（INSERT、DELETE、 UPDATE）及DDL语句。 |
| PrecheckStatu s | Struct |  | 预检查状态。 |
| Detail | Array of PrecheckDetail |  | 各预检查项的执行情况。 |
| CheckItem | String | CHECK CONN SRC _ _ | 预检查项目。 |
| CheckItemDes cription | String | CHECK CONN SRC _ _ DETAIL _ | 预检查项目描述。 |
| CheckResult | String | Success | 检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
| FailedReason | String | Original error: Access denied for user 'dtstest'@'100.104. ***.**' (using password: YES) | 预检查未通过的错误提示。 |
| RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 |
| ErrorMessage | String | CHECK ERROR SA __ _ ME OBJ. _ | 预检查失败的原因。 |
| Percent | String | 100 | 预检查整体进度，单位为百分比。 |

数据传输

| Status | String | Finished | 预检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
|---|---|---|---|
| Reserved | String | {\"srcHostPorts\":\" \",\"whitelist.dms.o nline.ddl.enable\":f alse,\"filterDDL\":fa lse,\"sqlparser.dms .original.ddl\":true,\ "srcOracleType\":\" sid\",\"maxRetryTi me\":43200,\"destS SL\":\"0\",\"destOra cleType\":\"sid\",\"s rcSSL\":\"0\",\"dbLi stCaseChangeMod e\":\"default\",\"So urceEngineVersion\ ":\"8.0.18\",\"srcNet Type\":\"VPC\",\"de stNetType\":\"VPC\" ,\"srcVpcNetMappi ngInst\":\"172.16.1 **.**:10803\",\"des tVpcNetMappingIns t\":\"172.16.1**.**: 11077\",\"useJobTa sk\":\"1\"} | DTS预留参数，格式为JSON串，您可以传入本参数实现特殊需求（例如是否自动启动预检查）。 |
| SourceEndpoin t | Struct |  | 源实例连接信息。 |
| DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| EngineName | String | MySQL | 源实例的数据库类型。 |
| InstanceID | String | rm- bp1imrtn6fq7h**** | 源实例ID。 |
| InstanceType | String | RDS | 源实例类型。 |
| Ip | String | 172.16.88.*** | 源实例的连接地址。 |
| OracleSID | String | testsid | Oracle数据库的SID信息。 说明当源实例的EngineName取值为Oracle，且Oracle数据库为非RAC实例时，才会返回本参数。 |
| Port | String | 3306 | 源实例的数据库服务端口。 |

数据传输

| Region | String | cn-hangzhou | 源实例所在区域。 |
|---|---|---|---|
| SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：不使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用 _ _ SSL安全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS _ _ _ _ ：使用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SH _ _ _ _ _ A 256：使用SCRAM-SHA-256连接 _ Kafka。 |
| UserName | String | dtstest | 源实例的数据库账号。 |
| Status | String | Synchronizing | DTS实例状态，返回值及意思，请参见本接口请求参数Status的描述。 |
| StructureInitial izationStatus | Struct |  | 库表结构初始化状态。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | 库表结构初始化失败的错误提示。 |
| Percent | String | 100 | 库表结构初始化进度，单位为百分比。 |
| Progress | String | 1 | 已完成库表结构初始化的表的数量。 |
| Status | String | Finished | 库表结构初始化状态，取值包括： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
| SourceEndpoin t | Struct |  | 源实例连接信息。 |
| DatabaseNam e | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| EngineName | String | MySQL | 源实例的数据库类型。 |
| InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| InstanceType | String | RDS | 源实例类型。 |

数据传输

| Ip | String | 172.16.88.*** | 源实例的连接地址。 |
|---|---|---|---|
| OracleSID | String | testsid | Oracle数据库的SID信息。 说明当源实例的EngineName取值为Oracle，且Oracle数据库为非RAC实例时，才会返回本参数。 |
| Port | String | 3306 | 源实例的数据库服务端口。 |
| Region | String | cn-hangzhou | 源实例所在区域。 |
| SslSolutionEnu m | String | DISABLE | 是否使用SSL安全连接，返回值： DISABLE：不使用SSL安全连接。 ENABLE WITH CERTIFICATE：使用 _ _ SSL安全连接，并上传CA证书。 ENABLE ONLY 4 MONGODB ALTAS _ _ _ _ ：使用SSL安全连接AWS MongoDB Altas。 ENABLE ONLY 4 KAFKA SCRAM SH _ _ _ _ _ A 256：使用SCRAM-SHA-256连接 _ Kafka。 |
| UserName | String | dtstest | 源实例的数据库账号。 |
| Status | String | Migrating | DTS实例状态，返回值及意思，请参见本接口请求参数Status的描述。 |
| StructureInitial izationStatus | Struct |  | 库表结构迁移或初始化状态。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | 库表结构迁移或初始化失败的错误提示。 |
| Percent | String | 100 | 库表结构迁移或初始化进度，单位为百分比。 |
| Progress | String | 1 | 已完成库表结构迁移或初始化的表的数量。 |
| Status | String | Finished | 库表结构迁移或初始化状态，取值包括： NotStarted：未启动。 Migrating：迁移或初始化中。 Failed：迁移或初始化失败。 Finished：迁移或初始化完成。 |

数据传输

| TagList | Array of DtsTag |  | 标签集合。 |
|---|---|---|---|
| TagKey | String | testkey | 标签的键。 |
| TagValue | String | testvalue | 标签的值。 |
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | Type | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回Type，则代表所传入的请求参数Type不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| JobType | String | MIGRATION | DTS实例的任务类型，取值： MIGRATION：迁移。 SYNC：同步。 SUBSCRIBE：订阅。 |
| PageNumber | Integer | 2 | 页码。 |
| PageRecordCo unt | Integer | 20 | 当前页可展示的最大记录数。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalRecordCo unt | Integer | 15 | 所有符合条件的DTS实例数量。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=DescribeDtsJobs &Region=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```json
<DescribeDtsJobsResponse>
      <TotalRecordCount>15</TotalRecordCount>
      <PageRecordCount>1</PageRecordCount>
      <DtsJobList>
            <Status>Migrating</Status>
            <DataInitializationStatus>
                  <Status>Finished</Status>
                  <Progress>44755</Progress>
                  <Percent>100</Percent>
            </DataInitializationStatus>
            <DbObject>{"DTSTEST":
{"name":"dtstest","all":true,"state":"normal","edit":false}}</DbObject>
            <CreateTime>2021-03-16T08:01:19Z</CreateTime>
            <DtsJobName>RDS间迁移</DtsJobName>
            <ReverseJob>
                  <PrecheckStatus></PrecheckStatus>
                  <DataInitializationStatus></DataInitializationStatus>
                  <DestinationEndpoint></DestinationEndpoint>
                  <SourceEndpoint></SourceEndpoint>
                  <Performance></Performance>
                  <MigrationMode></MigrationMode>
                  <StructureInitializationStatus></StructureInitializationStatus>
                  <DataSynchronizationStatus></DataSynchronizationStatus>
            </ReverseJob>
            <PayType>PrePaid</PayType>
            <DtsInstanceID>dtsi03e3zty16i****</DtsInstanceID>
            <Delay>0</Delay>
            <MigrationMode>
                  <DataInitialization>true</DataInitialization>
                  <DataSynchronization>true</DataSynchronization>
                  <StructureInitialization>true</StructureInitialization>
            </MigrationMode>
            <PrecheckStatus>
                  <Status>Finished</Status>
                  <Percent>100</Percent>
                  <Detail>
                        <CheckItem>CHECK_CONN_SRC</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_CONN_SRC_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_CONN_DEST</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_CONN_DEST_DETAIL</CheckItemDescription>
```

数据传输

```xml
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_AUTH_SRC</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_AUTH_SRC_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_AUTH_DEST</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_AUTH_DEST_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_BINLOG_ON</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_BINLOG_ON_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_BINLOG_MODE</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_BINLOG_MODE_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_BINLOG_ROW_IMAGE</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_BINLOG_ROW_IMAGE_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_SERVER_ID</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_SERVER_ID_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_BINLOG_EXIST</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_BINLOG_EXIST_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_ENGINE</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_ENGINE_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_MYSQL_PASSOWRD_FORMAT</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL</CheckItemDescription>
                  </Detail>
```

数据传输

```xml
                  <Detail>
                        <CheckItem>CHECK_SRC</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_SRC_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_SAME_OBJ</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_SAME_OBJ_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_SQL_MODE</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_SQL_MODE_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_SAME_USER</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_SAME_USER_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_TOPOLOGY</CheckItem>
                        <CheckResult>Success</CheckResult>
<CheckItemDescription>CHECK_TOPOLOGY_DETAIL</CheckItemDescription>
                  </Detail>
            </PrecheckStatus>
            <DtsJobClass>large</DtsJobClass>
            <Checkpoint>1616902385</Checkpoint>
            <DtsJobId>i03e3zty16i****</DtsJobId>
            <DestinationEndpoint>
                  <UserName>dtstest</UserName>
                  <InstanceID>rm-bp1imrtn6fq7h****</InstanceID>
                  <SslSolutionEnum>DISABLE</SslSolutionEnum>
                  <Port>3306</Port>
                  <DatabaseName></DatabaseName>
                  <Region>cn-hangzhou</Region>
                  <InstanceType>RDS</InstanceType>
                  <EngineName>MySQL</EngineName>
            </DestinationEndpoint>
            <SourceEndpoint>
                  <UserName>dtstest</UserName>
                  <InstanceID>rm-bp1162kryivb8****</InstanceID>
                  <SslSolutionEnum>DISABLE</SslSolutionEnum>
                  <Port>3306</Port>
                  <Region>cn-hangzhou</Region>
                  <InstanceType>RDS</InstanceType>
                  <EngineName>MySQL</EngineName>
            </SourceEndpoint>
            <TagList>
                  <TagKey>testkey</TagKey>
```

`<T` Vl `>t` t l

```
</T
```

Vl > 数据传输

```json
                  <TagValue>testvalue</TagValue>
            </TagList>
            <Performance></Performance>
            <Reserved>
{"srcHostPorts":"","whitelist.dms.online.ddl.enable":false,"filterDDL":false,"sqlparser.d .original.ddl":true,"srcOracleType":"sid","maxRetryTime":43200,"destSSL":"0","destOracleT e":"sid","srcSSL":"0","dbListCaseChangeMode":"default","SourceEngineVersion":"8.0.18","sr etType":"VPC","destNetType":"VPC","srcVpcNetMappingInst":"172.16.1**.**:10803","destVpcNe appingInst":"172.16.1**.**:11077","useJobTask":"1"}</Reserved>
            <StructureInitializationStatus>
                  <Status>Finished</Status>
                  <Progress>1</Progress>
                  <Percent>100</Percent>
            </StructureInitializationStatus>
            <DataSynchronizationStatus>
                  <Status>Catched</Status>
                  <Progress>0/0</Progress>
                  <Percent>95</Percent>
            </DataSynchronizationStatus>
      </DtsJobList>
      <RequestId>621BB4F8-3016-4FAA-8D5A-5D3163CC****</RequestId>
      <PageNumber>2</PageNumber>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</DescribeDtsJobsResponse>
```

`JSON` 格式

```json
{
 "TotalRecordCount": 15,
 "PageRecordCount": 1,
 "DtsJobList": [
  {
   "Status": "Migrating",
   "DataInitializationStatus": {
    "Status": "Finished",
    "Progress": "44755",
    "Percent": "100"
   },
   "DbObject": "{\"DTSTEST\":
{\"name\":\"dtstest\",\"all\":true,\"state\":\"normal\",\"edit\":false}}",
   "CreateTime": "2021-03-16T08:01:19Z",
   "DtsJobName": "RDS间迁移",
   "ReverseJob": {
    "PrecheckStatus": {},
    "DataInitializationStatus": {},
    "DestinationEndpoint": {},
    "SourceEndpoint": {},
    "Performance": {},
    "MigrationMode": {},
    "StructureInitializationStatus": {},
    "DataSynchronizationStatus": {}
   },
   "PayType": "PrePaid",
```

数据传输

```json
   "DtsInstanceID": "dtsi03e3zty16i****",
   "Delay": 0,
   "MigrationMode": {
    "DataInitialization": true,
    "DataSynchronization": true,
    "StructureInitialization": true
   },
   "PrecheckStatus": {
    "Status": "Finished",
    "Percent": "100",
    "Detail": [
     {
      "CheckItem": "CHECK_CONN_SRC",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_CONN_SRC_DETAIL"
     },
     {
      "CheckItem": "CHECK_CONN_DEST",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_CONN_DEST_DETAIL"
     },
     {
      "CheckItem": "CHECK_AUTH_SRC",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_AUTH_SRC_DETAIL"
     },
     {
      "CheckItem": "CHECK_AUTH_DEST",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_AUTH_DEST_DETAIL"
     },
     {
      "CheckItem": "CHECK_BINLOG_ON",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_BINLOG_ON_DETAIL"
     },
     {
      "CheckItem": "CHECK_BINLOG_MODE",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_BINLOG_MODE_DETAIL"
     },
     {
      "CheckItem": "CHECK_BINLOG_ROW_IMAGE",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_BINLOG_ROW_IMAGE_DETAIL"
     },
     {
      "CheckItem": "CHECK_SERVER_ID",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SERVER_ID_DETAIL"
     },
     {
      "CheckItem": "CHECK_BINLOG_EXIST",
      "CheckResult": "Success",
```

数据传输

```json
      "CheckItemDescription": "CHECK_BINLOG_EXIST_DETAIL"
     },
     {
      "CheckItem": "CHECK_ENGINE",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_ENGINE_DETAIL"
     },
     {
      "CheckItem": "CHECK_MYSQL_PASSOWRD_FORMAT",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL"
     },
     {
      "CheckItem": "CHECK_SRC",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SRC_DETAIL"
     },
     {
      "CheckItem": "CHECK_SAME_OBJ",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SAME_OBJ_DETAIL"
     },
     {
      "CheckItem": "CHECK_SQL_MODE",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SQL_MODE_DETAIL"
     },
     {
      "CheckItem": "CHECK_SAME_USER",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SAME_USER_DETAIL"
     },
     {
      "CheckItem": "CHECK_TOPOLOGY",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_TOPOLOGY_DETAIL"
     }
```

]

```json
   },
   "DtsJobClass": "large",
   "Checkpoint": "1616902385",
   "DtsJobId": "i03e3zty16i****",
   "DestinationEndpoint": {
    "UserName": "dtstest",
    "InstanceID": "rm-bp1imrtn6fq7h****",
    "SslSolutionEnum": "DISABLE",
    "Port": "3306",
    "DatabaseName": "",
    "Region": "cn-hangzhou",
    "InstanceType": "RDS",
    "EngineName": "MySQL"
   },
   "SourceEndpoint": {
    "UserName": "dtstest",
"InstanceID":"rmbp1162kryivb8****"
```

数据传输

```json
    "InstanceID": "rm-bp1162kryivb8****",
    "SslSolutionEnum": "DISABLE",
    "Port": "3306",
    "Region": "cn-hangzhou",
    "InstanceType": "RDS",
    "EngineName": "MySQL"
   },
   "TagList": [
    {
     "TagKey": "testkey",
     "TagValue": "testvalue"
    }
```

`],`

```json
   "Performance": {},
   "Reserved":
```

"

```json
{\"srcHostPorts\":\"\",\"whitelist.dms.online.ddl.enable\":false,\"filterDDL\":false,\"sq arser.dms.original.ddl\":true,\"srcOracleType\":\"sid\",\"maxRetryTime\":43200,\"destSSL\ \"0\",\"destOracleType\":\"sid\",\"srcSSL\":\"0\",\"dbListCaseChangeMode\":\"default\",\" urceEngineVersion\":\"8.0.18\",\"srcNetType\":\"VPC\",\"destNetType\":\"VPC\",\"srcVpcNet ppingInst\":\"172.16.1**.**:10803\",\"destVpcNetMappingInst\":\"172.16.1**.**:11077\",\"u JobTask\":\"1\"}",
   "StructureInitializationStatus": {
    "Status": "Finished",
    "Progress": "1",
    "Percent": "100"
   },
   "DataSynchronizationStatus": {
    "Status": "Catched",
    "Progress": "0/0",
    "Percent": "95"
   }
  }
```

`],`

```json
 "RequestId": "621BB4F8-3016-4FAA-8D5A-5D3163CC****",
 "PageNumber": 2,
 "HttpStatusCode": 200,
 "Success": true
}
```

##### 按条件统计任务数量

调用CountJobByCondition按条件统计DTS任务的数量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CountJobByCond ition | 系统规定参数。取值：CountJobByCondition。 |

数据传输

| Region | String | 是 | cn-hangzhou | DTS实例所在地域的ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-hangzhou | DTS实例所在地域的ID，需与Region保持一致。 |
| Type | String | 否 | name | 传入此参数，指定查询类型： name：根据job名称查询。 rds：根据目标端实例ID查询。 instance：根据DTS实例ID查询。 srcRds：根据源端实例ID查询。 说明您需要传入Params， 指定查询条件的具体内容。 |
| JobType | String | 否 | SYNC | DTS实例的任务类型，取值为： MIGRATION：迁移。 SYNC：同步。 SUBSCRIBE：订阅。 |
| Params | String | 否 | dtspk3f13r731m **** | 查询的参数值。 说明您需要提前传入Type，指定查询条件。 |

数据传输

| Status | String | 否 | Finished | DTS实例状态，取值： 迁移任务状态： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 NotConfigured：未配置。 Migrating：迁移中。 Suspending：暂停中。 MigrationFailed：迁移失败。 Finished：完成。 Retrying：重试中。 Upgrade：升级中。 Locked：锁定中。 Downgrade：降级中。 同步任务状态： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 NotConfigured：未配置。 Initializing：同步初始化中。 InitializeFailed：同步初始化失败。 Synchronizing：同步中。 Failed：同步失败。 Suspending：暂停中。 Modifying：修改子对象中。 Finished：完成。 Retrying：重试中。 Upgrade：升级中。 Locked：锁定中。 Downgrade：降级中。 订阅任务的状态： NotConfigured：未配置。 NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 PreCheckPass：预检查通过。 Starting：启动中。 Normal：正常。 Retrying：重试中。 Abnormal：异常。 Upgrade：升级中。 Locked：锁定中。 Downgrade：降级中。 |
|---|---|---|---|---|

数据传输

| GroupId | String | 否 | pk13r731m**** | 分布式同步任务的父任务ID。 |
|---|---|---|---|---|
| SrcDbType | String | 否 | mongodb | 源端数据库类型，取值如下： MySQL：MySQL数据库（包括RDS MySQL和自建MySQL）。 PolarDB：PolarDB MySQL。 polardb o：PolarDB O引擎。 _ polardb pg：PolarDB _ PostgreSQL。 Redis：Redis数据库（包括云数据库 Redis和自建Redis）。 DRDS：云原生分布式数据库PolarDB- X（包括1.0和2.0）。 PostgreSQL：自建PostgreSQL。 odps：MaxCompute。 oracle：自建Oracle。 mongodb：MongoDB数据库（包括云数据库MongoDB和自建 MongoDB）。 tidb：TiDB数据库。 ADS：云原生数仓 AnalyticDB MySQL 2.0。 ADB30：云原生数仓 AnalyticDB MySQL 3.0。 Greenplum：云原生数仓 AnalyticDB PostgreSQL。 MSSQL：SQL Server数据库（包括 RDS SQL Server和自建SQL Server）。 kafka：Kafka数据库（包括消息队列 Kafka版和自建Kafka）。 DataHub：阿里云流式数据服务 DataHub。 clickhouse：云数据库 ClickHouse。 DB2：自建DB2 LUW。 as400：AS/400。 Tablestore：表格存储Tablestore。 |

数据传输

| DestDbType | String | 否 | mongodb | 目标端数据库类型，取值如下： MySQL：MySQL数据库（包括RDS MySQL和自建MySQL）。 PolarDB：PolarDB MySQL。 polardb o：PolarDB O引擎。 _ polardb pg：PolarDB _ PostgreSQL。 Redis：Redis数据库（包括云数据库 Redis和自建Redis）。 DRDS：云原生分布式数据库PolarDB- X（包括1.0和2.0）。 PostgreSQL：自建PostgreSQL。 odps：MaxCompute。 oracle：自建Oracle。 mongodb：MongoDB数据库（包括云数据库MongoDB和自建 MongoDB）。 tidb：TiDB数据库。 ADS：云原生数仓 AnalyticDB MySQL 2.0。 ADB30：云原生数仓 AnalyticDB MySQL 3.0。 Greenplum：云原生数仓 AnalyticDB PostgreSQL。 MSSQL：SQL Server数据库（包括 RDS SQL Server和自建SQL Server）。 kafka：Kafka数据库（包括消息队列 Kafka版和自建Kafka）。 DataHub：阿里云流式数据服务 DataHub。 clickhouse：云数据库 ClickHouse。 DB2：自建DB2 LUW。 as400：AS/400。 Tablestore：表格存储Tablestore。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 服务内部错误码，该参数即将下线。 |
| DynamicMess age | String | Type | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回Type，则代表所传入的请求参数Type不合法。 |

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | FC3BAAF2-74E3- 4471-8EB5- 96202D6A**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TotalRecordCo unt | Long | 100 | 阿里云主账号下所有符合条件的任务数量。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=CountJobByCondition &Region=cn-hangzhou &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalRecordCount>6</TotalRecordCount> <RequestId>4586B7A9-73E0-57DC-8C0D-61D****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success>
```

`JSON` 格式

```json
{
    "TotalRecordCount": 6,
    "RequestId": "4586B7A9-73E0-57DC-8C0D-61D****",
    "HttpStatusCode": 200,
    "Success": true
}
```

##### 查询DTS子任务执行状态

调用DescribePreCheckStatus查询DTS任务的子任务执行详情，包括预检查、库表结构迁移或初始化、全量迁移或初始化、增量迁移或同步。

**请求参数**

数据传输

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePreChe ckStatus | 系统规定参数。取值： DescribePreCheckStatus。 |
| DtsJobId | String | 是 | i03e3zty16i**** | 迁移、同步或订阅任务ID。 |
| JobCode | String | 是 | 01 | 任务码，传入本参数指定所需查询的DTS 任务的子任务类型，取值为： 01：预检查。 02 ：库表结构迁移或初始化。 03：全量迁移或初始化。 04：增量迁移或同步。 |
| StructType | String | 是 | before | 结构定义的类型，取值： before：库表结构迁移或初始化。 after：增量数据迁移或同步的DDL操作。 |
| PageNo | String | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| PageSize | String | 否 | 30 | 每页记录数，默认值为20。 |
| RegionId | String | 否 | cn-beijing | DTS实例所在地域的ID。 |
| StructPhase | String | 否 | View | 过滤项，结构迁移中的表、视图、函数。 |
| Name | String | 否 | dewuprop | 过滤项，模糊匹配表名。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| JobProgress | Array of ProgressInfo |  | 子任务的具体项目列表及项目执行进度。 |
| BootTime | String | 2021-03- 16T08:01:31.000+ 00:00 | 具体项目启动时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| CanSkip | Boolean | true | DTS是否支持在具体项目失败后，跳过该项目。 |

数据传输

| DdlSql | String | CREATE TABLE `dtstestdata`.`orde r` (\n`orderid` int(11) COMMENT '' NOT NULL , \n`username` char(32) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NULL , \n`ordertime` datetime COMMENT '' NULL , \n`commodity` varchar(32) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NULL , \n`phonenumber` int(11) COMMENT '' NULL , \n`address` text CHARSET `utf8mb4` COLLATE `utf8mb4 general _ _ ci` COMMENT '' NULL \n, PRIMARY KEY (`orderid`)) engine=InnoDB DEFAULT CHARSET=`gbk` DEFAULT COLLATE `gbk chinese ci` _ _ ROW FORMAT= _ Dynamic comment = '' ;\n | 执行的DDL操作。 |
|---|---|---|---|
| DelaySeconds | Integer | 0 | 增量迁移或同步延迟时间。 说明如查询迁移任务，该参数的单位为毫秒，如查询同步任务，该参数的单位为秒。 |
| DestSchema | String | dtstestdata new _ | 目标实例中迁移对象所属数据库名称。 |
| DiffRow | Long | 1 | 本参数即将下线。 |
| ErrDetail | String | CHECK ERROR SA __ _ ME OBJ DETAIL _ _ | 具体项目出错时的错误详情。 |
| ErrMsg | String | CHECK ERROR SA __ _ ME OBJ _ | 具体项目出错时的报错提示。 |
| FinishTime | String | 2021-03- 16T08:01:34.000+ 00:00 | 具体项目完成时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

数据传输

| Id | String | 5632 | 记录在元数据库中的id。 |
|---|---|---|---|
| IgnoreFlag | String | N | 是否直接忽略该具体项目，跳至下一个具体项目，返回值： N：否。 Y：是。 |
| Item | String | CHECK CONN DES _ _ T | 具体项目的简称。 |
| JobId | String | fj1c33ro168**** | 子任务ID。 |
| Logs | Array of JobLog |  | 具体报错的执行日志。 |
| ErrData | String | CREATE TABLE `dtstestdata`.`cust omer` (\n`runoob id` _ int(10) unsigned auto increment _ COMMENT '' NOT NULL , \n`runoob title` _ varchar(100) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NOT NULL , \n`runoob author1 _ 216` varchar(40) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NOT NULL , \n`submission date _ 1216` date COMMENT '' NULL \n, PRIMARY KEY (`runoob id`)) _ engine=InnoDB AUTO INCREMENT _ =200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8 general ci` _ _ ROW FORMAT= _ Dynamic comment = '' ;\n | 报错记录。 |
| ErrMsg | String | DTS-1020042 Execute sql error sql: Table 'customer' already exists | 具体项目出错时DTS的报错提示。 |

数据传输

| ErrType | String | ForeignKey | 报错类型。 |
|---|---|---|---|
| LogLevel | String | ERROR | 该日志的级别。 |
| Names | String | CHECK CONN DES _ _ T DETAIL _ | 具体项目名称。 |
| OrderNum | Integer | 10 | 项目编号。 |
| ParentObj | String | demo | 本参数即将下线。 |
| RepairMethod | String | CHECK ERROR SA __ _ ME OBJ REPAIR _ _ | 具体项目未通过时对应的修复方法。 |
| Skip | Boolean | false | 该具体项目失败后，您是否设置跳过该项目。 |
| SourceSchema | String | dtstestdata | 源实例中迁移对象所属数据库名称。 |
| State | String | Success | 具体项目的执行进度状态，返回值为： NotStarted：未启动。 Checking：检查中。 Migrating：迁移中。 Failed：失败。 Warning：警告。 Success：完成。 |
| Sub | String | [] | 具体项目的子项目进度。 说明如返回[]，则表示没有子项目。 |
| TargetNames | String | order | 待迁移或同步的对象名称。 |
| Total | Integer | 1 | 子任务的具体项目总数。 |
| ErrorItem | Integer | 0 | 导致子任务失败的具体项目数量。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| JobName | String | 预检查 | 所查询子任务的名称。 |

数据传输

| Code | String | 01 | 任务码，代表所查询的子任务，取值为： 01：预检查。 02 ：库表结构迁移或初始化。 03：全量迁移或初始化。 04：增量迁移或同步。 |
|---|---|---|---|
| RequestId | String | C096FA97-B6BA- 4575-899D- 61E12B59**** | 请求ID。 |
| State | String | Finished | 子任务的执行状态，返回值为： NotStarted：未启动。 Suspending：暂停中。 Checking：检查中。 Migrating：迁移中。 Failed：失败。 Catched：增量迁移或同步中。 Finished：完成。 |
| Success | Boolean | true | 请求是否成功。 |
| Total | Integer | 0 | 子任务的总数。 |
| JobId | String | b4my3zg929a**** | 迁移或同步任务ID。 |
| PageNumber | Long | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| PageRecordCo unt | Long | 20 | 当前页可展示的最大记录数。 |
| SubDistributed JobStatus | Array of SubDistributed JobStatus |  | 分布式子任务的详情。 |
| Code | String | 02 | 任务码，代表所查询的子任务，取值为： 01：预检查。 02：库表结构迁移或初始化。 03：全量迁移或初始化。 04：增量迁移或同步。 |
| ErrorItem | Integer | 0 | 当前执行失败的任务数量。 |
| JobId | String | n0gm1682j6563np | 任务ID。 |

数据传输

| JobName | String | dts.step.struct.load | 查询到的任务关联的分布式子任务的名称。 |
|---|---|---|---|
| JobProgress | Array of ProgressInfo |  | 子任务的具体项目列表及项目执行进度。 |
| BootTime | String | 2022-03- 30T03:36:11.000+ 00:00 | 具体项目启动时间，格式为 yyyy-MM- _ ddTHH:mm:ss Z（UTC时间）。 _ |
| CanSkip | Boolean | false | DTS是否支持在项目失败后，跳过该项目。返回值： true：是 false：否 |
| DdlSql | String | None | 执行的ddl操作。 |
| DelaySeconds | Integer | 0 | 增量迁移或同步延迟时间。 |
| DestSchema | String | databasetest | 目标实例中迁移对象所属数据库名称。 |
| DiffRow | Long | 1 | 本参数即将下线。 |
| ErrDetail | String | 增量迁移或同步延迟时间。 | 具体项目出错时的错误详情。 |
| ErrMsg | String | ODPS project does not exist odps.`huijin | 具体项目出错时的报错提示。 |
| FinishTime | String | 2022-03- 31T03:36:11.000+ 00:00 | 完成时间，格式为yyyy-mm- ddthh:mm:ssz（utc时间）。 |
| Id | String | 3890 | 该条记录在元数据库中的id。 |
| IgnoreFlag | String | N | 是否直接忽略该具体项目，跳至下一个具体项目，返回值： N：否。 Y：是。 |
| Item | String | login common tim _ _ e | 具体项目名称。 |
| JobId | String | l3m1213ye7l**** | 任务id。 |
| Logs | Array of JobLog |  | 具体报错的执行日志。 |

数据传输

| ErrData | String | CREATE TABLE `dtstestdata`.`cust omer` (\n`runoob id` _ int(10) unsigned auto increment _ COMMENT '' NOT NULL , \n`runoob title` _ varchar(100) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NOT NULL , \n`runoob author1 _ 216` varchar(40) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NOT NULL , \n`submission date _ 1216` date COMMENT '' NULL \n, PRIMARY KEY (`runoob id`)) _ engine=InnoDB AUTO INCREMENT _ =200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8 general ci` _ _ ROW FORMAT= _ Dynamic comment = '' ;\n | 报错记录。 |
|---|---|---|---|
| ErrMsg | String | get metric list fail | 具体的错误信息。 |
| ErrType | String | ForeignKey | 报错类型。 |
| LogLevel | String | INFO | 日志级别。 |
| Names | String | metricRuleTargets- 20180308houe | 具体项目名称。 |
| OrderNum | Integer | 1 | 项目编号。 |
| ParentObj | String | None | 本参数即将下线。 |
| RepairMethod | String | CHECK ERROR SA __ _ ME OBJ REPAIR _ _ | 预检查未通过时对应的修复方法。 |

数据传输

| Skip | Boolean | true | 是否有跳过该项工作，返回值： true：是。 false：否。 |
|---|---|---|---|
| SourceSchema | String | databasetest | 源实例中迁移对象所属数据库名称。 |
| State | String | Finished | 子任务的执行状态，返回值为： NotStarted：未启动。 Suspending：暂停中。 Checking：检查中。 Migrating：迁移中。 Failed：失败。 Catched：增量迁移或同步中。 Finished：完成。 |
| Sub | String | [] | 具体项目的子项目进度。 说明如返回[]，则表示没有子项目。 |
| TargetNames | String | order | 目标名称。 |
| Total | Integer | 11 | 总条数。 |
| State | String | Finished | 子任务的执行状态，返回值为： NotStarted：未启动。 Suspending：暂停中。 Checking：检查中。 Migrating：迁移中。 Failed：失败。 Catched：增量迁移或同步中。 Finished：完成。 |
| Total | Integer | 11 | 返回数据的总数量。 |
| TotalRecordCo unt | Long | 100 | 总记录数。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=DescribePreCheckStatus &DtsJobId=i03e3zty16i**** &JobCode=01 &StructType=before
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribePreCheckStatusResponse>
      <RequestId>C096FA97-B6BA-4575-899D-61E12B59****</RequestId>
      <State>Finished</State>
      <Total>0</Total>
      <HttpStatusCode>200</HttpStatusCode>
      <JobName>预检查</JobName>
      <ErrorItem>0</ErrorItem>
      <Code>01</Code>
      <Success>true</Success>
      <JobProgress>
            <BootTime>2021-03-16T08:01:31.000+00:00</BootTime>
            <Names>CHECK_CONN_SRC_DETAIL</Names>
            <Item>CHECK_CONN_SRC</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:31.000+00:00</FinishTime>
            <OrderNum>10</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:31.000+00:00</BootTime>
            <Names>CHECK_CONN_DEST_DETAIL</Names>
            <Item>CHECK_CONN_DEST</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:31.000+00:00</FinishTime>
            <OrderNum>20</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:32.000+00:00</BootTime>
            <Names>CHECK_AUTH_SRC_DETAIL</Names>
            <Item>CHECK_AUTH_SRC</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>15</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
```

数据传输

```xml
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_AUTH_DEST_DETAIL</Names>
            <Item>CHECK_AUTH_DEST</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>25</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_BINLOG_ON_DETAIL</Names>
            <Item>CHECK_BINLOG_ON</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>30</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_BINLOG_MODE_DETAIL</Names>
            <Item>CHECK_BINLOG_MODE</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>40</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_BINLOG_ROW_IMAGE_DETAIL</Names>
            <Item>CHECK_BINLOG_ROW_IMAGE</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>50</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
```

数据传输

```xml
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_SERVER_ID_DETAIL</Names>
            <Item>CHECK_SERVER_ID</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>60</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_BINLOG_EXIST_DETAIL</Names>
            <Item>CHECK_BINLOG_EXIST</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>70</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_ENGINE_DETAIL</Names>
            <Item>CHECK_ENGINE</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>80</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL</Names>
            <Item>CHECK_MYSQL_PASSOWRD_FORMAT</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>90</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
<JbP
```

> 数据传输

```xml
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_SRC_DETAIL</Names>
            <Item>CHECK_SRC</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>100</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_SAME_OBJ_DETAIL</Names>
            <Item>CHECK_SAME_OBJ</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>110</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_SQL_MODE_DETAIL</Names>
            <Item>CHECK_SQL_MODE</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>140</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_SAME_USER_DETAIL</Names>
            <Item>CHECK_SAME_USER</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>200</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
<Names>CHECKTOPOLOGYDETAIL</Names>
```

数据传输

```xml
            <Names>CHECK_TOPOLOGY_DETAIL</Names>
            <Item>CHECK_TOPOLOGY</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:35.000+00:00</FinishTime>
            <OrderNum>220</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
</DescribePreCheckStatusResponse>
```

`JSON` 格式

```json
{
 "RequestId": "C096FA97-B6BA-4575-899D-61E12B59****",
 "State": "Finished",
 "Total": 0,
 "HttpStatusCode": 200,
```

`"JobName": "`预检查`",`

```json
 "ErrorItem": 0,
 "Code": "01",
 "Success": true,
 "JobProgress": [
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:31.000+00:00",
   "Logs": [],
   "Names": "CHECK_CONN_SRC_DETAIL",
   "Item": "CHECK_CONN_SRC",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:31.000+00:00",
   "OrderNum": 10,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:31.000+00:00",
   "Logs": [],
   "Names": "CHECK_CONN_DEST_DETAIL",
   "Item": "CHECK_CONN_DEST",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:31.000+00:00",
   "OrderNum": 20,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

数据传输

```json
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:32.000+00:00",
   "Logs": [],
   "Names": "CHECK_AUTH_SRC_DETAIL",
   "Item": "CHECK_AUTH_SRC",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 15,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_AUTH_DEST_DETAIL",
   "Item": "CHECK_AUTH_DEST",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 25,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_BINLOG_ON_DETAIL",
   "Item": "CHECK_BINLOG_ON",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 30,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_BINLOG_MODE_DETAIL",
   "Item": "CHECK_BINLOG_MODE",
   "CanSkip": false,
   "DelaySeconds": 0,
"FinishTime":"20210316T08:01:33000+00:00"
```

数据传输

```json
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 40,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_BINLOG_ROW_IMAGE_DETAIL",
   "Item": "CHECK_BINLOG_ROW_IMAGE",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 50,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_SERVER_ID_DETAIL",
   "Item": "CHECK_SERVER_ID",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 60,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_BINLOG_EXIST_DETAIL",
   "Item": "CHECK_BINLOG_EXIST",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 70,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
"BootTime":"2021-03-16T08:01:34.000+00:00",
```

数据传输

```json
   BootTime: 20210316T08:01:34.000+00:00,
   "Logs": [],
   "Names": "CHECK_ENGINE_DETAIL",
   "Item": "CHECK_ENGINE",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 80,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL",
   "Item": "CHECK_MYSQL_PASSOWRD_FORMAT",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 90,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_SRC_DETAIL",
   "Item": "CHECK_SRC",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 100,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_SAME_OBJ_DETAIL",
   "Item": "CHECK_SAME_OBJ",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 110,
   "IgnoreFlag": "N",
   "State": "Success",
```

数据传输

```json
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_SQL_MODE_DETAIL",
   "Item": "CHECK_SQL_MODE",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 140,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_SAME_USER_DETAIL",
   "Item": "CHECK_SAME_USER",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 200,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  },
  {
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_TOPOLOGY_DETAIL",
   "Item": "CHECK_TOPOLOGY",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:35.000+00:00",
   "OrderNum": 220,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
  }
```

]

```
}
```

##### 查询DTS服务的IP地址

数据传输调用WhiteIpList接口查询DTS服务器的IP地址。 如果**源或目标实例**是**自建数据库**或**第三方云数据库**，您需要调用该接口查询DTS服务的IP地址，然后将查询所得的IP地址添加至源或目标实例的安全设置（通常为该类数据库的防火墙）中。 如果**源或目标数据库**是**阿里云数据库实例**（例如RDS、MongoDB等）或**ECS****上的自建数据库**，在配置源或目标实例信息时，如您点击**授权白名单并进入下一步**，系统会自动把DTS服务IP地址添加至实例的安全设置，您无需手动添加。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | WhiteIpList | 系统规定参数，取值：WhiteIpList。 |
| Region | String | 是 | cn-hangzhou | 源实例所属地域ID。 说明如果源实例为有公网IP 的自建数据库或第三方云数据库，则可以传入cn-hangzhou或者离该类数据库物理距离最近的区域ID。 |
| Type | String | 是 | vpc | 自建数据库或第三方云数据库的接入方式，取值为 internet：通过公网接入。 vpc：通过专线/VPN网关/智能网关接入。 |
| DestinationRegi on | String | 否 | cn-hangzhou | 目标实例所属地域ID。 说明如果目标实例为有公网IP的自建数据库或第三方云数据库，则可以传入cn- hangzhou或者离该类数据库物理距离最近的区域ID。 当DTS任务为迁移或同步时，本参数必须传入。 |
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | Type | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 |

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| IpList | String | 10.151.12.0/24,47. 102.181.0/24,47.1 01.109.0/24,120.5 5.129.0/24,11.115. 103.0/24,47.102.2 34.0/24 | IP白名单列表，多个IP地址中间使用英文逗号 （,）分隔。 |
| RequestId | String | AD823BD3-1BA6- 4117-A536- 165CB280**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值： true：请求成功。 false：请求失败。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=WhiteIpList &Region=cn-hangzhou &Type=vpc &DestinationRegion=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<WhiteIpListResponse>
      <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
<IpList>10.151.12.0/24,47.102.181.0/24,47.101.109.0/24,120.55.129.0/24,11.115.103.0/24,47 02.234.0/24</IpList> </WhiteIpListResponse>
```

`JSON` 格式数据传输

```json
{
    "RequestId":"AD823BD3-1BA6-4117-A536-165CB280****",
    "HttpStatusCode":200,
    "Success":true,
    "IpList":
"10.151.12.0/24,47.102.181.0/24,47.101.109.0/24,120.55.129.0/24,11.115.103.0/24,47.102.23 0/24" }
```

##### 查询PolarDB-X 1.0分布式订阅任务的子任务信息

调用DescribeSubscriptionMeta查询PolarDB-X 1.0分布式订阅任务下子任务的信息。 由于PolarDB-X 1.0订阅任务为分布式订阅，其下挂的一个RDS MySQL对应一个订阅子任务，您可调用本接口查询订阅子任务的信息。 PolarDB-X 1.0订阅任务的实例ID、消费组ID等信息，均可以通过调用DescribeDtsJobs接口查询。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSubscri ptionMeta | 系统规定参数，取值：DescribeSubscriptionMeta。 |
| Sid | String | 是 | z38m91gg2***** * | 消费组ID。 |
| DtsInstanceId | String | 否 | dtsbr4m9luv2** **** | 分布式订阅的实例ID。 |
| SubMigrationJobI ds | Json | 否 | z38m91gg2***** * | 分布式订阅任务下所有的子订阅任务ID。 多个子订阅任务ID间以英文逗号（,）分隔。 说明本参数和参数Topics两者中至少传入一个。推荐填入本参数。 |
| Topics | Json | 否 | cn hangzhou r _ _ m bp1n0x0x5tz _ ****** dtstestda _ ta version2 _ | 分布式订阅任务下所有的订阅Topic。多个订阅Topic间以英文逗号（,）分隔。 说明本参数和参数SubMigrationJobIds两者中至少传入一个。推荐填入参数SubMigrationJobIds。 |
| RegionId | String | 否 | cn-hangzhou | 订阅实例所在地域。 |

**返回数据**

数据传输

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | String | 200 | 状态码。 |
| RequestId | String | C12E7A51-09A4- 5796-94BE- 08B6DA****** | 请求ID。 |
| SubscriptionM etaList | Array of SubscriptionM etaList |  | 订阅子任务的数据信息。 |
| Checkpoint | Long | 1610524452 | 子任务的消费位点，即客户端消费第一条数据的时间戳，格式为Unix时间戳。 说明 Unix时间戳转换工具可用搜索引擎获取。 |
| DBList | String | {\"dtstestdata\": {\"name\":\"dtstest data\",\"all\":false,\ "Table\":{\"order\": {\"name\":\"order\" ,\"all\":true}}}} | 子任务的订阅对象。 |
| DProxyUrl | String | dts-cn- hangzhou.aliyuncs. com:18001 | 数据订阅通道的网络地址及端口号信息。 |
| Sid | String | z38m91gg2****** | 子任务的消费组ID。 |
| Topic | String | cn hangzhou rm b _ _ _ p1n0x0x5tz****** _ dtstestdata versio _ n2 | 子任务的订阅Topic。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSubscriptionMeta &Sid=z38m91gg2****** &DtsInstanceId=dtsbr4m9luv2****** &SubMigrationJobIds=z38m91gg2****** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 数据传输正常返回示例 `XML` 格式

```xml
<DescribeSubscriptionMetaResponse>
      <SubscriptionMetaList>
            <Checkpoint>1610524452</Checkpoint>
            <DBList>{\"dtstestdata\":{\"name\":\"dtstestdata\",\"all\":false,\"Table\":
{\"order\":{\"name\":\"order\",\"all\":true}}}}</DBList>
            <DProxyUrl>dts-cn-hangzhou.aliyuncs.com:18001</DProxyUrl>
            <Topic>cn_hangzhou_rm_bp1n0x0x5tz******_dtstestdata_version2</Topic>
            <Sid>z38m91gg2******</Sid>
      </SubscriptionMetaList>
      <RequestId>C12E7A51-09A4-5796-94BE-08B6DA******</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</DescribeSubscriptionMetaResponse>
```

`JSON` 格式

```json
{
    "SubscriptionMetaList": [
        {
            "Checkpoint": "1610524452",
            "DBList": "{\\\"dtstestdata\\\":
{\\\"name\\\":\\\"dtstestdata\\\",\\\"all\\\":false,\\\"Table\\\":{\\\"order\\\":{\\\"n ame\\\":\\\"order\\\",\\\"all\\\":true}}}}",
            "DProxyUrl": "dts-cn-hangzhou.aliyuncs.com:18001",
            "Topic": "cn_hangzhou_rm_bp1n0x0x5tz******_dtstestdata_version2",
            "Sid": "z38m91gg2******"
        }
```

`],`

```json
    "RequestId": "C12E7A51-09A4-5796-94BE-08B6DA*******",
    "HttpStatusCode": "200",
    "Success": "true"
}
```

##### 查询全量或增量校验任务详情

调用DescribeDataCheckTableDetails接口查询全量或增量数据校验任务的详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

数据传输

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeDataCheckTabl eDetails | 系统规定参数。取值： DescribeDataCheckTabl eDetails |
| Status | Strin g | Query | 否 | -1 | 校验结果对应的状态，取值为： -1 （默认值）：所有状态。 6 ：存在不一致数据的表。 |
| PageSize | Integ er | Query | 否 | 10 | 每页记录数。 |
| PageNum ber | Integ er | Query | 否 | 1 | 页码，取值为大于0 且不超过Integer数据类型的最大值，默认值为1 。 |
| CheckTyp e | Integ er | Query | 是 | 1 | 数据校验方式，取值： 1 ：全量校验。 2 ：增量校验。 |
| TableNam e | Strin g | Query | 否 | student | 源数据库中校验的表名。 |
| RegionId | Strin g | Host | 否 | cn-qingdao-env***-d** | DTS实例所属的地域。 |
| DtsJobId | Strin g | Query | 是 | k2gm967v16f**** | 迁移、同步或订阅任务ID。 |
| SchemaN ame | Strin g | Query | 否 | dtstest | 源数据库中校验对象的 Schema名称。 |
| Resource GroupId | Strin g | Query | 否 | rg-acfmzawhxxc**** | 资源组ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TableDetails | Array | 参考下面的详细字段即可 | 数据表校验的结果详情。 |

数据传输

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Status | String | 0 | 校验结果对应的状态，返回值为： 0 ：已完成。 2 ：初始化中。 3 ：运行中。 5 ：失败。 |
| -Id | Long | 167401241974**** | 用于标识一条校验结果数据的自增主键。 |
| - SourceDbNam e | String | testdb | 源端数据库名称。 |
| - TargetDbNam e | String | testdb | 目标端数据库名称。 |
| - SourceTbNam e | String | student | 源端表名称。 |
| - TargetTbName | String | person | 目标端表名称。 |
| -TotalCount | Long | 8 | 校验数据的总行数。 |
| -FinishCount | Long | 7 | 表中已完成校验的数据行数。 |
| -DiffCount | Long | 1 | 数据不一致的行数。 |
| -BootTime | String | 2023-01-18 11:26:59 | 进行校验的时间。 |
| -ErrorCode | Integer | 1 | 任务运行出错时，返回报错信息的错误编码。 1 ：无主键表的数量超过限制。 2 ：差异数据超过300行。 3 ：待查询的表不存在。 4 ：查询数据的SQL语法错误。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的**%s**。 如果ErrMessage 返回The Value of Input Parameter %s is not valid ，且DynamicMessage 返回DtsJobId ，则代表所传入的请求参数DtsJobId 不合法。 |
| PageNumber | Integer | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| TotalCount | Long | 8 | 校验数据的总行数。 |
| FinishedCount | Long | 7 | 表中已完成校验的数据行数。 |
| DiffTableCount | Long | 1 | 数据不一致表的数量。 |

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Throttling.User | Throttling.User | Request was denied due to user flow control. |
| 500 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 403 | InvalidSecurityToke n.Expired | InvalidSecurityToken.Expired | Specified SecurityToken is expired. |

##### 查询校验任务不一致信息

调用DescribeDataCheckTableDiffDetails接口查询校验任务不一致信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 数据传输

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeDataCheckTabl eDiffDetails | 系统规定参数。取值： DescribeDataCheckTabl eDiffDetails |
| CheckTyp e | Integ er | Query | 是 | 2 | 数据校验方式，取值： 1：全量校验。 2：增量校验。 |
| DbName | Strin g | Query | 是 | db dtstest _ | 存在不一致数据的表所在的数据库的名称。 |
| TbName | Strin g | Query | 是 | test person _ | 存在不一致数据的表名。 |
| PageSize | Long | Query | 否 | 10 | 每页记录数。 |
| PageNum ber | Long | Query | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| RegionId | Strin g | Host | 否 | cn-hangzhou | 区域 |
| DtsJobId | Strin g | Query | 是 | xd4e4xb419q**** | 迁移或同步任务ID，您可以调用 DescribeDtsJobs接口查询。 |
| Resource GroupId | Strin g | Query | 否 | rg-acfmzawhxxc**** | 隶属资源集 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DiffDetails | Array | / | 不一致信息。 |
| -Id | Long | 13058**** | 用于标识一条校验结果数据的自增主键。 |
| -GmtCreated | String | 2023-04- 23T10:36:05.000+ 00:00 | 执行校验的时间。 |

数据传输

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Diff | String | [ { "column": "id", "source": "9511", "dest": "9511", "isPrimary": true }, { "column": "state", "source": "3", "dest": "2", "isPrimary": false }, { "column": "create time", _ "source": "2023- 04-11 14:07:17.0", "dest": "NULL", "isPrimary": false }, { "column": "update time", _ "source": "2023- 04-11 06:07:17.0", "dest": "2023-04- 11 06:02:29.0", "isPrimary": false } ] | 具体不一致信息，是一个JSON字符串。 column：字段名称。 source：源库中的值。 dest：目标库中的值。 isPrimary：字段是否是主键。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |
| HttpStatusCod e | Integer | 403 | 状态码。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrMessage | String | The value of the parameter tbName is invalid. | 调用错误时返回的错误信息。 |
| DynamicMess age | String | Type | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的%s。 |
| TbName | String | test person _ | 存在不一致数据的表名。 |
| DbName | String | db dtstest _ | 数据库名称。 |
| DiffCount | Long | 1 | 数据不一致的行数。 |
| InstanceId | String | dtsog8q1z3tc9t**** | 实例ID。 |

**错误码**

数据传输

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Throttling.User | Throttling.User | Request was denied due to user flow control. |
| 500 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 403 | InvalidSecurityToke n.Expired | InvalidSecurityToken.Expired | Specified SecurityToken is expired. |

##### 查询实例规格限制情况

调用DescribeInstanceClassLimit接口查询实例规格限制情况。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DtsJobId | Strin g | Query | 是 | l3m1213ye7l**** | 迁移、同步或订阅任务ID。 |
| RegionId | Strin g | Query | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| OwnerId | Strin g | Query | 否 | 123456**** | 鉴权相关的系统参数，不填。 |
| ZeroEtlJob | Boole an | Query | 否 | rg-aek2xs5u3or**** | 是否无感集成（Zero- ETL）任务，取值： true ：是 false ：否 |
| Resource GroupId | Strin g | Query | 否 | rg-acfmzawhxxc**** | 资源集ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| Success | Boolean | true | 请求是否成功。 |

数据传输

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的**%s**。 如果ErrMessage 返回The Value of Input Parameter %s is not valid ，且DynamicMessage 返回DtsJobId ，则代表所传入的请求参数DtsJobId 不合法。 |
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| HttpStatusCod e | Integer | 403 | 状态码。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |
| ClassCheckRes ult | Struct | NotImplemented | 类检查未执行，可能由于环境或配置原因导致跳过。 |
| -JobSteps | Array | End | 任务执行的最后一步，常用于清理资源或保存最终结果。 |
| --JobStepId | String | 1001 | 表示任务流程中第一步的唯一标识符 |
| --JobStepCode | String | 008 | 表示任务步骤的唯一编码，用于标识作业流程中的具体步骤；示例值中“JSC”为前缀，后续为步骤编号。 |
| --AvgRps | String | 50 | 平均每秒处理的请求数为50，表示系统在观测期间每秒钟平均响应并处理了50个请求。 |
| --MaxRps | String | true | 最大RPS，RPS模式下生效。 |
| --MinRps | String | 5 | 每秒最少请求处理数量为5个 |
| --Limit | String | 10 | CPU使用上限（CPU核数*1000）。 |
| -DtsJobId | String | n99m9jx822k**** | 迁移、同步或订阅任务ID。 |

|  | 数据传输 |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DtsJobType | String | BatchDataExport | 批量数据导出任务类型，用于一次性导出大量数据。 |
| -InstanceClass | String | 14C70G | 实例规格。 |
| -MaxRps | Integer | 100 | 最大RPS，RPS模式下生效。 |
| -NoLimit | Boolean | true | 是否限流。 |
| -SbeJob | Boolean | true | 是否为订阅任务。 |
| -NoInstance | Boolean | true | 实例是否为空。 |
| -Limit | Boolean | true | 是否限流。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeInstanceClassLimit &DtsJobId=l3m1213ye7l****
```

&公共请求参数正常返回示例 `JSON` 格式数据传输

```json
{
 "RequestId":"621BB4F8-3016-4FAA-8D5A-5D3163CC****",
 "HttpStatusCode":403,
 "DynamicCode":"403",
 "DynamicMessage":"DtsJobId",
 "ErrMessage":"The request processing has failed due to some unknown error.",
 "Success":true,
 "ErrCode":"InternalError",
 "ClassCheckResult":{
  "SbeJob":true,
  "MaxRps":100,
  "JobSteps":[
   {
    "MaxRps":"true",
    "MinRps":"5",
    "JobStepId":"1001",
    "JobStepCode":"008",
    "AvgRps":"50",
    "Limit":"10"
   }
```

`],`

```json
  "DtsJobId":"n99m9jx822k****",
  "InstanceClass":"14C70G",
  "NoLimit":true,
  "DtsJobType":"BatchDataExport",
  "NoInstance":true,
  "Limit":true
 }
}
```

`XML` 格式数据传输

```xml
<RequestId>621BB4F8-3016-4FAA-8D5A-5D3163CC****</RequestId> <HttpStatusCode>403</HttpStatusCode> <DynamicCode>403</DynamicCode> <DynamicMessage>DtsJobId</DynamicMessage> <ErrMessage>The request processing has failed due to some unknown error.</ErrMessage> <Success>true</Success> <ErrCode>InternalError</ErrCode> <ClassCheckResult>
 <SbeJob>true</SbeJob>
 <MaxRps>100</MaxRps>
 <JobSteps>
  <MaxRps>true</MaxRps>
  <MinRps>5</MinRps>
  <JobStepId>1001</JobStepId>
  <JobStepCode>008</JobStepCode>
  <AvgRps>50</AvgRps>
  <Limit>10</Limit>
 </JobSteps>
 <DtsJobId>n99m9jx822k****</DtsJobId>
 <InstanceClass>14C70G</InstanceClass>
 <NoLimit>true</NoLimit>
 <DtsJobType>BatchDataExport</DtsJobType>
 <NoInstance>true</NoInstance>
 <Limit>true</Limit>
</ClassCheckResult>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Throttling.User | Throttling.User | Request was denied due to user flow control. |
| 500 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 403 | InvalidSecurityToke n.Expired | InvalidSecurityToken.Expired | Specified SecurityToken is expired. |

##### 获取一键诊断详情

调用DescribeRecentAnalysisDetail接口获取一键诊断详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

数据传输

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| JobId | Strin g | Query | 是 | b4my3zg929a**** | 预检查任务ID，可调用DescribePreCheckSt atus 查询。 |
| Source | Strin g | Query | 否 | agentless | 日志源。 |
| RegionId | Strin g | Query | 否 | cn-hangzhou | 地域ID，传入本参数指定实例所在地域。 |
| PageNum ber | Strin g | Query | 否 | 1 | 页码，取值为大于0 且不超过Integer数据类型的最大值，默认值为1 。 |
| PageSize | Strin g | Query | 否 | 10 | 每页记录数，取值：30 、50 、100 ，默认值为30 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DetailList | Array | ["订单明细", "费用清单", "操作记录"] | 明细数组。 |
| -ReportList | Array | ["Report1", "Report2", "Report3"] | 安全报告信息列表。 |
| --Id | Long | 3890 | 用于标识一条校验结果数据的自增主键。 |
| --RecordId | Long | 20201105144514 | 记录ID。 |
| --ItemName | String | CHECK CONN SRC _ _ | 预检查项目。 |
| --Result | String | SUCCESS | 返回结果。 |
| --State | String | Success | 子任务的执行状态，返回值： NotStarted ：未启动。 Suspending ：暂停中。 Checking ：检查中。 Migrating ：迁移中。 Failed ：失败。 Catched ：增量迁移或同步中。 Finished ：完成。 |

数据传输

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --CreatedAt | String | 2020-07- 14T14:01:41.000+ 08:00 | 创建时间。 |
| --CompletedAt | String | 2024-04-02 10:10:23 | 完成时间。 |
| --Feedback | Boolean | good | 点赞或点踩，返回值： good ：点赞 bad ：点踩 |
| -Record | Struct | 192.168.0.1 | 解析记录列表。 |
| --State | String | Success | 子任务的执行状态，返回值为： NotStarted ：未启动。 Suspending ：暂停中。 Checking ：检查中。 Migrating ：迁移中。 Failed ：失败。 Catched ：增量迁移或同步中。 Finished ：完成。 |
| --CreatedAt | String | 2020-07- 14T14:01:41.000+ 08:00 | 创建时间 |
| --UpdatedAt | String | 2022-03-18 14:24:54 | 更新时间 |
| -StatContent | Struct | {"stats": [{"name":"内存使用率","value":"75%"," unit":"%"}, {"name":"CPU使用率","value":"55%"," unit":"%"}]} | 对订单总数进行统计的结果内容。 |
| --Score | Integer | 100 | 置信度。 |
| HttpStatusCod e | Integer | 403 | 状态码。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| Success | Boolean | true | 请求是否成功。 |

| 开发指南·API参考 |  |  | 数据传输 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的%s。 如果ErrMessage 返回The Value of Input Parameter %s is not valid ，且DynamicMessage 返回DtsJobId ，则代表所传入的请求参数DtsJobId 不合法。 |
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRecentAnalysisDetail &JobId= b4my3zg929a****
```

&公共请求参数正常返回示例 `JSON` 格式数据传输

```json
{
 "RequestId":"621BB4F8-3016-4FAA-8D5A-5D3163CC****",
 "DetailList":[
  {
   "StatContent":[
    {
     "Score":100
    }
```

`],`

```json
   "Record":[
    {
     "State":"Success",
     "CreatedAt":"2020-07-14T14:01:41.000+08:00",
     "UpdatedAt":"2022-03-18 14:24:54"
    }
```

`],`

```json
   "ReportList":[
    {
     "Feedback":false,
     "State":"Success",
     "CreatedAt":"2020-07-14T14:01:41.000+08:00",
     "CompletedAt":"2024-04-02 10:10:23",
     "ItemName":"CHECK_CONN_SRC",
     "Id":3890,
     "RecordId":20201105144514,
     "Result":"SUCCESS"
    }
```

]

```
  }
```

`],`

```json
 "HttpStatusCode":403,
 "DynamicCode":"403",
 "DynamicMessage":"DtsJobId",
 "ErrMessage":"The request processing has failed due to some unknown error.",
 "Success":true,
 "ErrCode":"InternalError"
}
```

`XML` 格式数据传输

```xml
<RequestId>621BB4F8-3016-4FAA-8D5A-5D3163CC****</RequestId> <DetailList>
 <StatContent>
  <Score>100</Score>
 </StatContent>
 <Record>
  <State>Success</State>
  <CreatedAt>2020-07-14T14:01:41.000+08:00</CreatedAt>
  <UpdatedAt>2022-03-18 14:24:54</UpdatedAt>
 </Record>
 <ReportList>
  <Feedback>false</Feedback>
  <State>Success</State>
  <CreatedAt>2020-07-14T14:01:41.000+08:00</CreatedAt>
  <CompletedAt>2024-04-02 10:10:23</CompletedAt>
  <ItemName>CHECK_CONN_SRC</ItemName>
  <Id>3890</Id>
  <RecordId>20201105144514</RecordId>
  <Result>SUCCESS</Result>
 </ReportList>
</DetailList> <HttpStatusCode>403</HttpStatusCode> <DynamicCode>403</DynamicCode> <DynamicMessage>DtsJobId</DynamicMessage> <ErrMessage>The request processing has failed due to some unknown error.</ErrMessage> <Success>true</Success> <ErrCode>InternalError</ErrCode>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Throttling.User | Throttling.User | Request was denied due to user flow control. |
| 500 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 403 | InvalidSecurityToke n.Expired | InvalidSecurityToken.Expired | Specified SecurityToken is expired. |

##### 查询DTS升级试验详情

调用DescribeUpgradeTrials接口查询DTS升级试验的详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

数据传输

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | 否 | cn-hangzhou | 地域ID，传入本参数指定实例所在地域。 |
| OwnerId | Strin g | Query | 否 | 123456**** | 鉴权相关的系统参数，不填。 |
| DtsInstanc eId | Strin g | Query | 否 | dtsl3m1213ye7l**** | 迁移、同步或订阅实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Trials | Array | 3 | 某个实验或测试中尝试的次数。 |
| -CreateTime | String | 2021-03- 16T08:01:19Z | 任务创建时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -Creator | String | 10000000 | 标签操作者。 |
| -Owner | String | 1107550004****** | 节点责任人的阿里云UID。 |
| -DtsInstanceId | String | dtsi03e3zty16i**** | 迁移、同步或订阅实例ID。 |
| -OldCutoff | Integer | 1 | 旧截止时间。 |
| -NewCutoff | Integer | 1 | 新截止时间。 |
| -ExpireTime | String | 2022-03- 16T08:01:19Z | 实例的到期时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 当PayType 参数返回值为PrePaid 时，才会返回本参数。 |
| -Status | String | Migrating | NotStarted ：未启动 Suspending ：暂停中 Checking ：检查中 Migrating :：迁移中 Failed ：失败 Catched ：同步中或增量迁移中 Finished ：完成 |

数据传输

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| Success | Boolean | true | 请求是否成功。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的%s。 如果ErrMessage 返回The Value of Input Parameter %s is not valid ，且DynamicMessage 返回DtsJobId ，则代表所传入的请求参数DtsJobId 不合法。 |
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| HttpStatusCod e | Integer | 403 | 状态码。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |
| Visible | Boolean | true | 自动SQL限流规则是否开启，返回值： true ：是 false ：否 |
| Support | Boolean | true | 是否支持检测，返回值： true ：支持 false ：不支持 |
| CurrentTrial | Struct | 3 | 当前正在进行的实验或测试的次数编号，用于跟踪实验的迭代次数。 |
| -CreateTime | String | 2021-03- 16T08:01:19Z | 任务创建时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| -Creator | String | 10000000 | 标签操作者。 |

| 数据传输 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Owner | String | 1107550004****** | 节点责任人的阿里云UID。 |
| -DtsInstanceId | String | dtsi03e3zty16i**** | 迁移、同步或订阅实例ID。 |
| -OldCutoff | Integer | 1 | 旧截止时间。 |
| -NewCutoff | Integer | 1 | 新截止时间。 |
| -ExpireTime | String | 2022-03- 16T08:01:19Z | 实例的到期时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 当PayType 参数的返回值为PrePaid 时才会返回本参数。 |
| -Status | String | Migrating | NotStarted ：未启动 Suspending ：暂停中 Checking ：检查中 Migrating ：迁移中 Failed ：失败 Catched ：同步中或增量迁移中 Finished ：完成 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeUpgradeTrials
```

&公共请求参数正常返回示例 `JSON` 格式数据传输

```json
{
 "CurrentTrial":{
  "Status":"Migrating",
  "Owner":"1107550004******",
  "CreateTime":"2021-03-16T08:01:19Z",
  "Creator":"10000000",
  "OldCutoff":1,
  "NewCutoff":1,
  "ExpireTime":"2022-03-16T08:01:19Z",
  "DtsInstanceId":"dtsi03e3zty16i****"
 },
 "Trials":[
  {
   "Status":"Migrating",
   "Owner":"1107550004******",
   "CreateTime":"2021-03-16T08:01:19Z",
   "Creator":"10000000",
   "OldCutoff":1,
   "NewCutoff":1,
   "ExpireTime":"2022-03-16T08:01:19Z",
   "DtsInstanceId":"dtsi03e3zty16i****"
  }
```

`],`

```json
 "RequestId":"621BB4F8-3016-4FAA-8D5A-5D3163CC****",
 "Support":true,
 "HttpStatusCode":403,
 "Visible":true,
 "DynamicCode":"403",
 "DynamicMessage":"DtsJobId",
 "ErrMessage":"The request processing has failed due to some unknown error.",
 "Success":true,
 "ErrCode":"InternalError"
}
```

`XML` 格式数据传输

```xml
<CurrentTrial>
 <Status>Migrating</Status>
 <Owner>1107550004******</Owner>
 <CreateTime>2021-03-16T08:01:19Z</CreateTime>
 <Creator>10000000</Creator>
 <OldCutoff>1</OldCutoff>
 <NewCutoff>1</NewCutoff>
 <ExpireTime>2022-03-16T08:01:19Z</ExpireTime>
 <DtsInstanceId>dtsi03e3zty16i****</DtsInstanceId>
</CurrentTrial> <Trials>
 <Status>Migrating</Status>
 <Owner>1107550004******</Owner>
 <CreateTime>2021-03-16T08:01:19Z</CreateTime>
 <Creator>10000000</Creator>
 <OldCutoff>1</OldCutoff>
 <NewCutoff>1</NewCutoff>
 <ExpireTime>2022-03-16T08:01:19Z</ExpireTime>
 <DtsInstanceId>dtsi03e3zty16i****</DtsInstanceId>
</Trials> <RequestId>621BB4F8-3016-4FAA-8D5A-5D3163CC****</RequestId> <Support>true</Support> <HttpStatusCode>403</HttpStatusCode> <Visible>true</Visible> <DynamicCode>403</DynamicCode> <DynamicMessage>DtsJobId</DynamicMessage> <ErrMessage>The request processing has failed due to some unknown error.</ErrMessage> <Success>true</Success> <ErrCode>InternalError</ErrCode>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Throttling.User | Throttling.User | Request was denied due to user flow control. |
| 500 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 403 | InvalidSecurityToke n.Expired | InvalidSecurityToken.Expired | Specified SecurityToken is expired. |

#### 修改DTS任务

##### 修改DTS同步任务

调用ModifyDtsJob接口修改同步任务。

**请求参数**

数据传输

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | 否 | cn-hangzhou | 实例所在区域。 |
| DtsInstanc eId | Strin g | Quer y | 是 | dtsbi6e22ay243**** | 同步实例ID。 |
| Synchroniz ationDirect ion | Strin g | Quer y | 否 | Forward | 指定同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 只有当数据同步实例的同步拓扑为双向同步时，才需要传入本参数。 |
| ClientToke n | Strin g | Quer y | 否 | 0c593ea1-3bea-11e9- b96b-88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持 ASCII字符，且不能超过64个字符。 |
| AccessKeyI d | Strin g | Quer y | 否 | LTAI5t7k7Zz8bFUu5z2s** ** | 访问服务所用的密钥ID。 |

数据传输

| DbList | Strin g | Body | 否 | {"dtstest": {"name":"dtstest","all":tr ue}} | 修改后的同步对象。 说明建议您提前调用DescribeDtsJobD etail接口查询当前同步对象，然后根据业务需要输入修改后的同步对象。例如，当前对象为表A、B，现需要新增对象表C，那么您需要在本参数同时传入表A、B、 C。 |
|---|---|---|---|---|---|
| EtlOperato rColumnRe ference | Strin g | Body | 否 | { "configKeyMap": [ { "moduleCode": "03", "etlOperatorColumnRefer ence": "etlOperatorColumnRefer ence", "etlOperatorSetting": "etlOperatorSetting" }, { "moduleCode": "07", "etlOperatorColumnRefer ence": "etlOperatorColumnRefer ence", "etlOperatorSetting": "etlOperatorSetting" } ], "amp.increment.replicato r.compare.all.columns.en able": false, "srcNetType": "VPC", "etlOperatorColumnRefer ence": { "MODIFY TIME": [ _ { "datasynchron.test timin _ g user 000": _ _ "user create date" _ _ }, { | T+1业务专用的字段，ETL算子，为业务专用字段。 |

数据传输

|  |  |  |  | "datasynchron.test timin _ g user 001": _ _ "user create date" _ _ }, { "datasynchron.test timin _ g user 002": _ _ "user create date" _ _ }, { "datasynchron.test timin _ g user 003": _ _ "user create date" _ _ } ] }, "destNetType": "VPC", "originalSrcDbInst": "sg- sit-db2- primary.mysql.polardb.rd s.aliyuncs.com", "etlOperatorSetting": "adb time travel", _ _ "sjobUseJobTask": "1", "srcVpcNetMappingInst": |  |
|---|---|---|---|---|---|
|  |  |  |  | "172.19.XXX.XXX:4261", "destVpcNetMappingInst" : "172.19.XXX.XXX:4260", "useJobTask": "1" |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DtsJobId | String | bi6e22a**** | DTS任务ID。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | Boolean | true | 调用出错时返回的错误信息。 说明该参数的数据类型应为String，实际示例值为The request processing has failed due to some unknown error. |

数据传输

| RequestId | String | 1D6ECADF-C5E9- 4C96-8811- 77602B31**** | 请求ID。 |
|---|---|---|---|
| Status | String | 200 | 状态码。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifyDtsJob &DtsInstanceId=dtsbi6e22ay243**** &DbList={"dtstest":{"name":"dtstest","all":true}}
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "Status":"200",
 "DtsJobId":"bi6e22a****",
 "RequestId":"1D6ECADF-C5E9-4C96-8811-77602B31****",
 "Success":true
}
```

`XML` 格式

```xml
<Status>200</Status> <DtsJobId>bi6e22a****</DtsJobId> <RequestId>1D6ECADF-C5E9-4C96-8811-77602B31****</RequestId> <Success>true</Success>
```

##### 修改DTS订阅任务

调用ModifySubscription接口修改DTS订阅任务的订阅对象及订阅数据的类型。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySubscripti on | 系统规定参数，取值：ModifySubscription。 |

数据传输

| DbList | String | 是 | {"dtstest": {"name":"dtstes t","all":true}} | 修改后的订阅对象，格式为JSON串。 说明原订阅对象，可调用 DescribeDtsJobDetail进行查询。 |
|---|---|---|---|---|
| DtsInstanceId | String | 是 | dtsboss6pn1w** **** | 订阅实例ID，可以调用DescribeDtsJobs 查询。 |
| DtsJobId | String | 是 | boss6pn1w***** * | 订阅任务ID，可以调用DescribeDtsJobs 查询。 |
| SubscriptionDat aTypeDDL | Boolean | 是 | true | 修改后任务是否订阅DDL类型的数据，取值： true：是。 false：否。 |
| SubscriptionDat aTypeDML | Boolean | 是 | true | 修改后任务是否订阅DML类型的数据，取值： true：是。 false：否。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所在地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回对应的错误信息。 |
| HttpStatusCod e | String | 200 | 状态码。 |
| RequestId | String | 068FA72F-4800- 4A54-90BB- 94806068**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=ModifySubscription &DbList={"dtstest":{"name":"dtstest","all":true}} &DtsInstanceId=dtsboss6pn1w****** &DtsJobId=boss6pn1w****** &SubscriptionDataTypeDDL=true &SubscriptionDataTypeDML=true
```

正常返回示例 `XML` 格式

```xml
<ModifySubscriptionResponse>
      <RequestId>068FA72F-4800-4A54-90BB-94806068****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</ModifySubscriptionResponse>
```

`JSON` 格式

```json
{
 "RequestId": "068FA72F-4800-4A54-90BB-94806068****",
 "HttpStatusCode": 200,
 "Success": true
}
```

##### 修改DTS任务源或目标库的账号密码

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDtsJobPas sword | 系统规定参数，取值：ModifyDtsJobPassword。 |
| DtsJobId | String | 是 | l3m1213ye7l*** * | 迁移、同步或订阅任务ID。 |
| Endpoint | String | 否 | src | 待修改的账号密码所属的数据库，取值： src：源库。 dest：目标库。 说明本参数为必填参数。 |
| UserName | String | 否 | dtstest | 待修改数据库的账号名称。 说明本参数为必填参数。 |

数据传输

| Password | String | 否 | Test123456 | 修改后的账号密码。 说明本参数应为必填参数， 且不能与当前密码一致。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | 200 | 错误码，本参数即将下线。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | InternalError | 调用错误时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 8C498360-7892- 433C-847A- BA71A850**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifyDtsJobPassword &DtsJobId=l3m1213ye7l**** &Endpoint=src &UserName=dtstest &Password=Test123456
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<ModifyDtsJobPasswordResponse>
      <RequestId>8C498360-7892-433C-847A-BA71A850****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</ModifyDtsJobPasswordResponse>
```

`JSON` 格式

```json
{
  "RequestId": "8C498360-7892-433C-847A-BA71A850****",
  "HttpStatusCode": 200,
  "Success": true
}
```

##### 修改DTS任务名称

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDtsJobNa me | 系统规定参数，取值：ModifyDtsJobName。 |
| DtsJobId | String | 是 | l3m1213ye7l*** * | 迁移、同步或订阅任务ID。 |
| DtsJobName | String | 否 | RDS间迁移 | 修改后的任务名称。 说明本参数为必填参数，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| RegionId | String | 否 | cn-beijing | 任务所属地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | 200 | 错误码，本参数即将下线。 |

数据传输

| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用错误时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 8C498360-7892- 433C-847A- BA71A850**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifyDtsJobName &DtsJobId=l3m1213ye7l****
```

`&DtsJobName=RDS`间迁移 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDtsJobNameResponse>
      <RequestId>8C498360-7892-433C-847A-BA71A850****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</ModifyDtsJobNameResponse>
```

`JSON` 格式

```json
{
  "RequestId": "8C498360-7892-433C-847A-BA71A850****",
  "HttpStatusCode": 200,
  "Success": true
}
```

数据传输

##### 升级单向同步至双向同步

调用UpgradeTwoWay接口将DTS同步实例的同步拓扑从单向同步升级为双向同步，目前只支持后付费任务的升级。 使用该接口需注意： 数据同步任务的源实例和目标实例的数据库类型均为**MySQL**。 数据同步任务的同步拓扑为**单向同步**。 数据同步任务的状态为**同步中**。 升级生效期间数据同步会出现5秒左右的延迟，请在业务低峰期操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpgradeTwoWa y | 系统规定参数，取值：UpgradeTwoWay。 |
| InstanceClass | String | 是 | large | 双向同步的实例规格，取值为large、medium、micro 、small。 |
| InstanceId | String | 是 | dtsh77p49x4k28 **** | 实例ID，可通过调用DescribeDtsJobs获取。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域，详情请参见支持的地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | InstanceId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回InstanceId，则代表所传入的请求参数InstanceId不合法。 |
| ErrCode | String | InternalError | 调用错误时返回的错误码。 |

数据传输

| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 2D3B4615-923F- 49AA-AF21- 6D8E3967**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值： true：请求成功。 false：请求失败。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=UpgradeTwoWay &InstanceClass=large &InstanceId=dtsh77p49x4k28****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StartDtsJobResponse>
        <RequestId>2D3B4615-923F-49AA-AF21-6D8E3967****</RequestId>
        <HttpStatusCode>200</HttpStatusCode>
        <Success>true</Success>
</StartDtsJobResponse>
```

`JSON` 格式

```json
{
    "RequestId":"2D3B4615-923F-49AA-AF21-6D8E3967****",
    "HttpStatusCode":200,
    "Success":true
}
```

##### 修改付费方式或实例规格

调用TransferPayType接口修改DTS产品的付费方式或实例规格。 包年包月的实例无法转换为按量付费的实例，为避免您的资源浪费，在实例转换付费方式操作前确认要进行转换操作。 数据迁移任务只支持按量付费，无需转换。 按量付费转包年包月只是进行付费方式的切换，对于底层运行链路不会有任何影响。

**请求参数**

数据传输

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TransferPayType | 系统规定参数，取值：TransferPayType。 |
| ChargeType | String | 是 | PostPaid | 修改后的付费方式，取值： PrePaid：预付费，即包年包月。 PostPaid：后付费，即按量付费。 说明包年包月实例无法转换为按量付费实例，为避免您的资源浪费，在实例转换付费方式前，请确认要进行的转换操作。 如无需修改付费方式，则传入当前付费方式即可。 |
| DtsJobId | String | 是 | o4nh3g7jg56*** * | 迁移、同步或订阅任务ID，可调用 DescribeDtsJobs查询。 |
| Period | String | 否 | Year | 预付费实例的计费方式，取值： Year：包年。 Month：包月。 说明当ChargeType为PrePaid（预付费）时，该参数才有效且必须传入。 |
| BuyCount | String | 否 | 5 | 预付费实例购买时长。 当Period为Year（包年）时，取值范围为1~5。 当Period为Month（包月）时，取值范围为1~60。 说明当ChargeType为Prepaid（预付费）时，该参数才有效且必须传入。 |
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ChargeType | String | PostPaid | 修改后的付费方式，返回值： PrePaid：预付费。 PostPaid：后付费。 |

数据传输

| Code | String | 200 | 错误码，本参数即将下线。 |
|---|---|---|---|
| DtsJobId | String | o4nh3g7jg56**** | 任务ID。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| EndTime | String | 1614916318 | 预付费实例到期时间，格式为Unix时间戳。 说明如修改后的实例为后付费实例，则该值为空值。 Unix时间戳转换工具可用搜索引擎获取。 |
| ErrCode | String | InternalError | 调用错误时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| InstanceId | String | dtso4nh3g7jg56*** * | 实例ID。 |
| RequestId | String | 601B6F25-21E7- 4484-99D5- 3EF2625C**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值： true：请求成功。 false：请求失败。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=TransferPayType &ChargeType=PostPaid &DtsJobId=o4nh3g7jg56**** &Period=Year &BuyCount=5
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TransferPayTypeResponse>
      <DtsJobId>o4nh3g7jg56****</DtsJobId>
      <RequestId>601B6F25-21E7-4484-99D5-3EF2625C****</RequestId>
      <InstanceId>dtso4nh3g7jg56****</InstanceId>
      <ChargeType>PostPaid</ChargeType>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</TransferPayTypeResponse>
```

`JSON` 格式

```json
{
  "DtsJobId": "o4nh3g7jg56****",
  "RequestId": "601B6F25-21E7-4484-99D5-3EF2625C****",
  "InstanceId": "dtso4nh3g7jg56****",
  "ChargeType": "PostPaid",
  "HttpStatusCode": 200,
  "Success": true
}
```

##### 升级或降级DTS实例规格

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TransferInstance Class | 系统规定参数，取值：TransferInstanceClass。 |
| DtsJobId | String | 是 | r4yr723m199*** * | 迁移或同步任务ID，可调用 DescribeDtsJobs查询。 |

数据传输

| InstanceClass | String | 是 | large | 升降级后的实例规格，可以调用 DescribeDtsJobDetail查询升降级前的实例规格。 迁移实例支持的规格：xxlarge、xlarge、large、me dium、small。 同步实例支持的规格：large、medium、small、mic ro。 |
|---|---|---|---|---|
| OrderType | String | 是 | UPGRADE | 升级或降级实例规格，可选值： UPGRADE（升级） DOWNGRADE（降级） |
| RegionId | String | 否 | cn-hangzhou | DTS实例所在地域的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ChargeType | String | POSTPAY | 付费类型，返回值： POSTPAY：按量付费（后付费）。 PREPAY：包年包月（预付费）。 |
| Code | String | 200 | 错误码。 |
| DtsJobId | String | r4yr723m199**** | 迁移或同步任务ID。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则表示所传入的请求参数DtsJobId不合法。 |
| EndTime | String | 2021-08- 04T16:00:00.000+ 00:00 | 实例到期时间。 说明 ChargeType为PREPAY， 才会返回此参数。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |

数据传输

| HttpStatusCod e | Integer | 200 | 状态码。 |
|---|---|---|---|
| InstanceId | String | dtsr4yr723m199** ** | 实例ID。 |
| RequestId | String | 716DB03E-2D0B- 4DC3-BC4C- F7A9EE21**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。返回值： true：请求成功。 false：请求失败。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=TransferInstanceClass &OrderType=UPGRADE &InstanceClass=large &DtsJobId=r4yr723m199****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TransferInstanceClassResponse>
        <DtsJobId>r4yr723m199****</DtsJobId>
        <RequestId>716DB03E-2D0B-4DC3-BC4C-F7A9EE21****</RequestId>
        <InstanceId>dtsr4yr723m199****</InstanceId>
        <ChargeType>POSTPAY</ChargeType>
        <HttpStatusCode>200</HttpStatusCode>
        <Success>true</Success>
</TransferInstanceClassResponse>
```

`JSON` 格式

```json
{
        "DtsJobId": "r4yr723m199****",
        "RequestId": "716DB03E-2D0B-4DC3-BC4C-F7A9EE21****",
        "InstanceId": "dtsr4yr723m199****",
        "ChargeType": "POSTPAY",
        "HttpStatusCode": 200,
        "Success": true
}
```

##### 为DTS实例续费

调用RenewInstance可以为DTS实例续费。本接口仅适用于预付费类型的DTS实例。 数据传输

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RenewInstance | 系统规定参数。取值：RenewInstance。 |
| ChargeType | String | 是 | PREPAY | 付费类型为PREPAY，包年包月（预付费）。 |
| DtsJobId | String | 是 | qi0r643lc31**** | 同步或订阅任务ID，可调用 DescribeDtsJobs查询。 |
| Period | String | 否 | Month | 续费实例的计费方式，取值： Year：包年。 Month：包月（默认值）。 |
| BuyCount | String | 否 | 1 | 续费实例购买时长。 当Period为Year（包年）时，取值范围为1~5。 当Period为Month（包月）时，取值范围为1~60。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所在地域的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ChargeType | String | PREPAY | 付费类型为PREPAY，包年包月（预付费）。 |
| Code | String | 200 | 错误码。 说明本参数即将下线。 |
| DtsJobId | String | qi0r643lc31**** | 同步或订阅任务ID。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则表示所传入的请求参数DtsJobId不合法。 |

数据传输

| EndTime | String | 2021-08- 04T16:00:00.000+ 00:00 | 续费实例到期时间。 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| InstanceId | String | dtsqi0r643lc31**** | 实例ID。 |
| RequestId | String | 1112E255-0C38- 4970-8159- 1D54AD92**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值： true：请求成功。 false：请求失败。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=RenewInstance &ChargeType=PREPAY &DtsJobId=qi0r643lc31**** &Period=Month &BuyCount=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RenewInstanceResponse>
  <DtsJobId>qi0r643lc31****</DtsJobId>
  <EndTime>2021-08-04T16:00:00.000+00:00</EndTime>
  <RequestId>1112E255-0C38-4970-8159-1D54AD92****</RequestId>
  <InstanceId>dtsqi0r643lc31****</InstanceId>
  <ChargeType>PREPAY</ChargeType>
  <HttpStatusCode>200</HttpStatusCode>
  <Success>true</Success>
</RenewInstanceResponse>
```

`JSON` 格式数据传输

```json
{
   "DtsJobId": "qi0r643lc31****",
   "EndTime": "2021-08-04T16:00:00.000+00:00",
   "RequestId": "1112E255-0C38-4970-8159-1D54AD92****",
   "InstanceId": "dtsqi0r643lc31****",
   "ChargeType": "PREPAY",
   "HttpStatusCode": 200,
   "Success": true
}
```

#### 重置DTS任务

调用ResetDtsJob重置一个数据同步或订阅任务。 清空数据同步或订阅任务配置后，原先的任务就会被删除，DTS将重新创建一个未配置的

**说明**

任务，您需要调用接口ConfigureDtsJob重新配置该任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ResetDtsJob | 系统规定参数。取值：ResetDtsJob。 |
| DtsJobId | String | 是 | l3m1213ye7l*** * | 同步或订阅任务ID。 |
| DtsInstanceId | String | 否 | dtsl3m1213ye7l **** | 同步或订阅实例ID。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 当数据同步实例的拓扑为双向时，才可以传入Reverse以重置反向同步链路。 |
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |

数据传输

| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 01B6F25-21E7- 4484-99D5- 3EF2625C**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ResetDtsJob &DtsJobId=l3m1213ye7l****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ResetDtsJobResponse>
      <RequestId>01B6F25-21E7-4484-99D5-3EF2625C****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</ResetDtsJobResponse>
```

`JSON` 格式

```json
{
    "RequestId":"01B6F25-21E7-4484-99D5-3EF2625C****",
    "HttpStatusCode":200,
    "Success":true
}
```

#### 暂停DTS任务

数据传输调用SuspendDtsJob暂停一个数据迁移、同步或订阅任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SuspendDtsJob | 系统规定参数。取值：SuspendDtsJob。 |
| DtsJobId | String | 是 | l3m1213ye7l*** * | 迁移、同步或订阅任务ID。 |
| DtsInstanceId | String | 否 | dtsl3m1213ye7l **** | 迁移、同步或订阅实例ID。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 当数据同步实例的拓扑为双向时，才可以传入Reverse以暂停反向同步链路。 |
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |

数据传输

| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 01B6F25-21E7- 4484-99D5- 3EF2625C**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=SuspendDtsJob &DtsJobId=l3m1213ye7l****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<SuspendDtsJobResponse>
      <RequestId>01B6F25-21E7-4484-99D5-3EF2625C****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</SuspendDtsJobResponse>
```

`JSON` 格式

```json
{
    "RequestId":"01B6F25-21E7-4484-99D5-3EF2625C****",
    "HttpStatusCode":200,
    "Success":true
}
```

#### 批量暂停DTS任务

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SuspendDtsJobs | 系统规定参数，取值：SuspendDtsJobs。 |

数据传输

| DtsJobIds | String | 是 | hfi12iv4z7e**** | 迁移、同步任务ID。 说明当有多个任务ID时，使用','隔开。 可调用DescribeDtsJobs获取DTS任务ID。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | AD823BD3-1BA6- 4117-A536- 165CB280**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=SuspendDtsJobs &DtsJobIds=hfi12iv4z7e**** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例数据传输 `XML` 格式

```xml
<StartDtsJobResponse>
      <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</StartDtsJobResponse>
```

`JSON` 格式

```json
{
    "RequestId": "AD823BD3-1BA6-4117-A536-165CB280****",
    "HttpStatusCode": 200,
    "Success": true
}
```

#### 结束DTS任务

调用StopDtsJob结束一个数据迁移、同步或订阅任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StopDtsJob | 系统规定参数。取值：StopDtsJob。 |
| DtsJobId | String | 是 | l3m1213ye7l*** * | 迁移、同步或订阅任务ID。 |
| DtsInstanceId | String | 否 | dtsl3m1213ye7l **** | 迁移、同步或订阅实例ID。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 当数据同步实例的拓扑为双向时，才可以传入Reverse以结束反向同步链路。 |
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
|---|---|---|---|
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 01B6F25-21E7- 4484-99D5- 3EF2625C**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=StopDtsJob &DtsJobId=l3m1213ye7l****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StopDtsJobResponse>
      <RequestId>01B6F25-21E7-4484-99D5-3EF2625C****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</StopDtsJobResponse>
```

`JSON` 格式

```json
{
    "RequestId":"01B6F25-21E7-4484-99D5-3EF2625C****",
    "HttpStatusCode":200,
    "Success":true
}
```

数据传输

#### 批量结束DTS任务

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StopDtsJobs | 系统规定参数。取值：StopDtsJobs。 |
| DtsJobIds | String | 是 | l5o11f9029c**** | 迁移、同步任务ID。 说明当有多个任务ID时，使用','隔开。 可调用DescribeDtsJobs获取DTS任务ID。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | AD823BD3-1BA6- 4117-A536- 165CB280**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

数据传输

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=StopDtsJobs &DtsJobIds=l5o11f9029c**** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StopDtsJobResponse>
      <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</StopDtsJobResponse>
```

`JSON` 格式

```json
{
    "RequestId": "AD823BD3-1BA6-4117-A536-165CB280****",
    "HttpStatusCode": 200,
    "Success": true
}
```

#### 释放DTS实例

调用DeleteDtsJob接口释放一个数据迁移、同步或订阅实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDtsJob | 系统规定参数。取值：DeleteDtsJob。 |
| DtsJobId | String | 是 | l3m1213ye7l*** * | 迁移、同步或订阅任务ID。 |
| DtsInstanceId | String | 否 | dtsl3m1213ye7l **** | 迁移、同步或订阅实例ID。 |

数据传输

| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 当数据同步实例的拓扑为双向时，才可以传入Reverse以释放反向同步链路。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 01B6F25-21E7- 4484-99D5- 3EF2625C**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DeleteDtsJob &DtsJobId=l3m1213ye7l****
```

`&<`公共请求参数> 数据传输正常返回示例 `XML` 格式

```xml
<DeleteDtsJobResponse>
      <RequestId>01B6F25-21E7-4484-99D5-3EF2625C****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</DeleteDtsJobResponse>
```

`JSON` 格式

```json
{
    "RequestId":"01B6F25-21E7-4484-99D5-3EF2625C****",
    "HttpStatusCode":200,
    "Success":true
}
```

#### 批量释放DTS任务

调用DeleteDtsJobs接口批量释放数据迁移、同步或订阅任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDtsJobs | 系统规定参数。取值：DeleteDtsJobs。 |
| DtsJobIds | String | 是 | l5o11f9029c**** | 迁移、同步或订阅任务ID。 说明当有多个任务ID时，使用','隔开。 可调用DescribeDtsJobs获取DTS任务ID。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 动态错误码，本参数即将下线。 |

数据传输

| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | AD823BD3-1BA6- 4117-A536- 165CB280**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DeleteDtsJobs &DtsJobIds=l5o11f9029c**** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteDtsJobsResponse>
      <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</DeleteDtsJobsResponse>
```

`JSON` 格式

```json
{
    "RequestId": "AD823BD3-1BA6-4117-A536-165CB280****",
    "HttpStatusCode": 200,
    "Success": true
}
```

数据传输

#### 统计DTS任务迁移表的数量

调用SummaryJobDetail接口统计DTS数据迁移或同步任务中迁移表的数量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SummaryJobDet ail | 系统规定参数。取值： SummaryJobDetail。 |
| DtsJobId | String | 是 | l3m1213ye7l*** * | 迁移或同步任务ID。 说明与实例ID两者至少需填一个。 |
| JobCode | String | 是 | 02 | 迁移阶段，取值： 02：结构迁移阶段。 03：增量迁移阶段。 |
| Synchronization Direction | String | 是 | Forward | 同步链路方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 当数据同步实例的拓扑为双向时，才可以传入Reverse以释放反向同步链路。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |
| DtsInstanceId | String | 否 | dtsl3m1213ye7l **** | 迁移或同步实例ID。 说明与任务ID两者至少需填一个。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | 200 | 错误码，本参数即将下线。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |

数据传输

| JobId | String | l3m1213ye7l**** | 迁移或同步任务ID。 |
|---|---|---|---|
| ProgressSum maryDetails | Array of ProgressSum maryDetail |  | 迁移对象数组返回信息。 说明数组返回格式如下： [{"key":"Function","state":5,"totalCou nt":22}, {"key":"Procedure","state":5,"totalCo unt":26}, {"key":"Table","state":0,"totalCount": 68}, {"key":"View","state":5,"totalCount":1 00}]。 |
| Key | String | Table | 迁移对象类型，返回值：Table（表）、Constraint（约束）、Index（索引）、View（视图）、Materialize View（物化视图）、Type（自定义类型）、Synonym（同义词）、Trigger（触发器）、Function（函数）、Procedure（存储过程）、Package（包）、Default（默认值）、Rule（规则）、PlanGuide（执行计划）、Sequence（序列）。 |
| State | Integer | 0 | 迁移状态，返回值： 0：finish（结束）。 1：catched（等待同步）。 2：init（初始化）。 3：running（同步中）。 4：warning（报错）。 5：failed（失败）。 |
| TotalCount | Long | 100 | 迁移对象总数。 |
| RequestId | String | 65EE90A6-9062- 51B0-9997- 75F7E574**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值： true：请求成功。 false：请求失败。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=SummaryJobDetail &DtsJobId=l3m1213ye7l**** &JobCode=02 &SynchronizationDirection=Forward &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<SummaryJobDetailResponse>
      <requestId>65EE90A6-9062-51B0-9997-75F7E574****</requestId>
      <success>true</success>
      <progressSummaryDetails>
            <key>Function</key>
            <state>5</state>
            <totalCount>22</totalCount>
      </progressSummaryDetails>
      <progressSummaryDetails>
            <key>Procedure</key>
            <state>5</state>
            <totalCount>26</totalCount>
      </progressSummaryDetails>
      <progressSummaryDetails>
            <key>Table</key>
            <state>0</state>
            <totalCount>68</totalCount>
      </progressSummaryDetails>
      <progressSummaryDetails>
            <key>View</key>
            <state>5</state>
            <totalCount>100</totalCount>
      </progressSummaryDetails>
      <httpStatusCode>200</httpStatusCode>
</SummaryJobDetailResponse>
```

`JSON` 格式数据传输

```json
{
    "requestId": "65EE90A6-9062-51B0-9997-75F7E574****",
    "success": true,
    "progressSummaryDetails": [
        {
            "key": "Function",
            "state": 5,
            "totalCount": 22
        },
        {
            "key": "Procedure",
            "state": 5,
            "totalCount": 26
        },
        {
            "key": "Table",
            "state": 0,
            "totalCount": 68
        },
        {
            "key": "View",
            "state": 5,
            "totalCount": 100
        }
```

`],`

```json
    "httpStatusCode": 200
}
```

#### 初始化单元节点中DTS使用的内置账号

调用InitDtsRdsInstance接口在全球多活数据库集群的节点中初始化一个内置账号，DTS使用该账号连接节点并进行同步任务。 单元节点需为RDS MySQL或云企业网CEN接入的自建MySQL。 该接口用于在全球多活数据库集群的单元节点中，初始化一个内置账号 `rdsdt_dtsacct` ，DTS使用该账号连接节点并进行同步任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | InitDtsRdsInstance | 系统规定参数。取值： InitDtsRdsInstance |
| RegionId | Strin g | Query | 否 | cn-hangzhou | 全球数据多活集群所属的地域。 |

数据传输

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| EndpointI nstanceTy pe | Strin g | Query | 否 | RDS | 单元节点的实例类型，取值： RDS ：RDS MySQL实例。 CEN ：通过云企业网 CEN接入的自建MySQL 数据库。 |
| EndpointR egion | Strin g | Query | 否 | cn-hangzhou | 如单元节点为RDS MySQL 实例，则您需要传入RDS MySQL实例所属地域。 您还需要传入参数EndpointInstanceI d 。 本参数与EndpointCenId ，两者必须传入其一。 |
| EndpointI nstanceId | Strin g | Query | 否 | rm-bp1162kryivb8**** | 如单元节点为RDS MySQL 实例，则您需要传入RDS MySQL实例ID。 您还需要传入参数EndpointRegion 。 本参数与EndpointCenId ，两者必须传入其一。 |
| EndpointC enId | Strin g | Query | 否 | cen-9kqshqum******* | 如单元节点为云企业网CEN 接入的自建MySQL，则您需要传入云企业网CEN的实例 ID。 本参数与RDS MySQL 相关参数 （EndpointRegio n 、EndpointInst anceId ），两组参数必须传入其中一组。 |
| AccessKey Id | Strin g | Query | 否 | LTAI4G28PhwnizaSC**** **** | 访问密钥ID。 |
| DtsInstanc eId | Strin g | Query | 否 | dtsl3m1213ye7l**** | 同步实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

数据传输

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | String | 200 | 状态码。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| Success | String | true | 请求是否成功，返回值： true ：请求成功。 false ：请求失败。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| AdminAccount | String | rdsdt dtsacct _ | DTS连接单元节点时使用的内置账号。 |
| AdminPasswor d | String | 1jecpqrtc**** | 内置账号的密码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=InitDtsRdsInstance &Action=InitDtsRdsInstance
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"621BB4F8-3016-4FAA-8D5A-5D3163CC****",
 "HttpStatusCode":"200",
 "AdminAccount":"rdsdt_dtsacct",
 "ErrMessage":"The Value of Input Parameter %s is not valid.",
 "Success":"true",
 "AdminPassword":"1jecpqrtc****",
 "ErrCode":"InternalError "
}
```

`XML` 格式数据传输

```xml
<RequestId>621BB4F8-3016-4FAA-8D5A-5D3163CC****</RequestId> <HttpStatusCode>200</HttpStatusCode> <AdminAccount>rdsdt_dtsacct</AdminAccount> <ErrMessage>The Value of Input Parameter %s is not valid.</ErrMessage> <Success>true</Success> <AdminPassword>1jecpqrtc****</AdminPassword> <ErrCode>InternalError </ErrCode>
```

#### 调转双向同步任务方向

调用ReverseTwoWayDirection接口调转双向同步任务的方向。 DTS双向同步任务中的反向任务会自动过滤DDL，当业务场景要求主备数据库切换或者双云切换时，需要调转双向同步任务的方向。使用该接口需注意： 操作前请仔细阅读双向同步文档。 分布式同步任务不支持调转任务方向。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | ReverseTwoWayDirectio n | 系统规定参数。取值： ReverseTwoWayDirectio n。 |
| RegionId | Strin g | Query | 是 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| DtsInstanc eId | Strin g | Query | 否 | dtsl3m1213ye7l**** | 双向同步任务的实例ID。 |
| IgnoreErro rSubJob | Boole an | Query | 否 | false | 是否忽略异常的同步子任务，默认不忽略，该参数暂时不开放。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |

数据传输

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| Success | Boolean | true | 请求是否成功，返回值： true ：请求成功。 false ：请求失败。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| Code | String | 403 | 错误码，本参数即将下线。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的%s。 如果ErrMessage 返回The Value of Input Parameter %s is not valid ，且DynamicMessage 返回DtsJobId ，则代表所传入的请求参数DtsJobId 不合法。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ReverseTwoWayDirection &Action=ReverseTwoWayDirection &RegionId=cn-hangzhou
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"621BB4F8-3016-4FAA-8D5A-5D3163CC****",
 "HttpStatusCode":200,
 "DynamicMessage":"DtsJobId",
 "ErrMessage":"The request processing has failed due to some unknown error.",
 "Code":"403",
 "Success":true,
 "ErrCode":"InternalError"
}
```

`XML` 格式数据传输

```xml
<RequestId>621BB4F8-3016-4FAA-8D5A-5D3163CC****</RequestId> <HttpStatusCode>200</HttpStatusCode> <DynamicMessage>DtsJobId</DynamicMessage> <ErrMessage>The request processing has failed due to some unknown error.</ErrMessage> <Code>403</Code> <Success>true</Success> <ErrCode>InternalError</ErrCode>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Throttling.User | Throttling.User | Request was denied due to user flow control. |
| 500 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 403 | InvalidSecurityToke n.Expired | InvalidSecurityToken.Expired | Specified SecurityToken is expired. |

#### 跳过DTS全量阶段无需同步的表

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | SkipFullJobTable | 系统规定参数。取值： SkipFullJobTable |
| JobProgre ssId | Long | Query | 是 | 1001 | JobProgress主键ID，全量迁移任务中每个对象对应一个JobProgress，指定该项确定需要跳过的表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | 200 | 错误码。 |

数据传输

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage 错误信息中的%s。 如果ErrMessage 返回The Value of Input Parameter %s is not valid ，且DynamicMessage 返回DtsJobId ，则代表所传入的请求参数DtsJobId 不合法。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 403 | 状态码。 |
| RequestId | String | 621BB4F8-3016- 4FAA-8D5A- 5D3163CC**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值： true ：请求成功。 false ：请求失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SkipFullJobTable &Action=SkipFullJobTable &JobProgressId=1001
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"621BB4F8-3016-4FAA-8D5A-5D3163CC****",
 "HttpStatusCode":403,
 "DynamicMessage":"DtsJobId",
 "ErrMessage":"The request processing has failed due to some unknown error.",
 "Code":"200",
 "Success":true,
 "ErrCode":"InternalError"
}
```

`XML` 格式数据传输

```xml
<RequestId>621BB4F8-3016-4FAA-8D5A-5D3163CC****</RequestId> <HttpStatusCode>403</HttpStatusCode> <DynamicMessage>DtsJobId</DynamicMessage> <ErrMessage>The request processing has failed due to some unknown error.</ErrMessage> <Code>200</Code> <Success>true</Success> <ErrCode>InternalError</ErrCode>
```

#### 任务告警规则

##### 创建或修改任务告警规则

DTS目前支持的监控项为**延迟**、**迁移状态**和**全量运行耗时**：
**延迟**：监控增量数据迁移延迟信息，当迁移延迟、同步延迟或订阅延迟的时间超过设定值时（单位为
秒），触发告警规则。
**迁移状态**：监控任务的状态，当任务的状态为**异常**或**恢复**时，触发告警规则。
**全量运行耗时**：全量运行的耗时，超过设定值时（单位为小时），触发告警规则。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateJobMonito rRule | 系统规定参数，取值：CreateJobMonitorRule。 |
| DtsJobId | String | 是 | i03e3zty16i**** | 迁移、同步或订阅任务ID。 |
| Type | String | 否 | delay | 监控项的类型，取值： delay：延迟监控项。 error：迁移状态监控项。 full timeout：全量运行耗时监控 _ 项。 默认值：error；需手动填入。 |
| State | String | 否 | Y | 是否启用告警规则，取值： Y：启用。 N：不启用。 默认值：Y |

数据传输

| Phone | String | 否 | 1361234****,13 71234**** | 告警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |
|---|---|---|---|---|
| DelayRuleTime | Long | 否 | 11 | 触发告警的阈值。 当Type取值为delay时，单位为秒且需为整数，可根据业务需要设置阈值， 建议设置10秒以上，避免因网络、数据库负载等原因导致的延迟波动。 当Type取值为full timeout时，单位 _ 为小时且需为整数。 说明当Type取值为delay或full timeout且State _ 取值为Y时，本参数必须传入。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | 200 | 错误码，本参数即将下线。 |
| DtsJobId | String | i03e3zty16i**** | 迁移、同步或订阅任务ID。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | 403 | 调用错误时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |

数据传输

| RequestId | String | 8C498360-7892- 433C-847A- BA71A850**** | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功，返回值： true：请求成功。 false：请求失败。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=CreateJobMonitorRule &DtsJobId=i03e3zty16i**** &Type=delay &State=Y &Phone=1361234****,1371234**** &DelayRuleTime=11
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateJobMonitorRuleResponse>
      <RequestId>8C498360-7892-433C-847A-BA71A850****</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
      <DtsJobId>i03e3zty16i****</DtsJobId>
</CreateJobMonitorRuleResponse>
```

`JSON` 格式

```json
{
    "RequestId":"8C498360-7892-433C-847A-BA71A850****",
    "HttpStatusCode":200,
    "Success":true,
    "DtsJobId":"i03e3zty16i****"
}
```

##### 查询DTS任务告警规则

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | DescribeJobMoni torRule | 系统规定参数，取值：DescribeJobMonitorRule。 |
|---|---|---|---|---|
| DtsJobId | String | 是 | ta7w132u12h*** * | 迁移、同步或订阅任务ID，可通过调用 DescribeDtsJobs获取。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | 200 | 错误码，本参数即将下线。 |
| DtsJobId | String | ta7w132u12h**** | 迁移、同步或订阅任务ID。 |
| DynamicMess age | String | DtsJobId | 动态错误信息，用于替换返回参数ErrMessage错误信息中的%s。 说明如果ErrMessage返回The Value of Input Parameter %s is not valid，且DynamicMessage返回DtsJobId，则代表所传入的请求参数DtsJobId不合法。 |
| ErrCode | String | 403 | 调用出错时返回的错误码。 |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | 调用错误时返回的错误信息。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| MonitorRules | Array of MonitorRule |  | DTS任务的监控规则信息。 |
| DelayRuleTim e | Long | 11 | 触发告警的阈值。 当CreateJobMonitorRule接口的请求参数Type取值为delay时，单位为秒。 当CreateJobMonitorRule接口的请求参数Type取值为full timeout时，单位为小 _ 时。 |
| Phone | String | 1361234****,1371 234**** | 告警触发后需通知的联系人手机号码，多个手机号码之间以英文逗号（,）分隔。 |

数据传输

| State | String | Y | 是否启用监控规则，返回值： Y：启用。 N：不启用。 |
|---|---|---|---|
| Type | String | delay | 监控规则的类型，返回值： delay：延迟告警。 error：异常告警。 |
| RequestId | String | 0CA14388-DD89- 4A7B-8CDD- 884A10CE**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值： true：请求成功。 false：请求失败。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeJobMonitorRule &DtsJobId=ta7w132u12h****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DtsJobId>ta7w132u12h****</DtsJobId> <RequestId>0CA14388-DD89-4A7B-8CDD-884A10CE****</RequestId> <HttpStatusCode>200</HttpStatusCode> <MonitorRules>
    <Type>delay</Type>
    <Phone>1361234****,1371234****</Phone>
    <State>Y</State>
    <DelayRuleTime>11</DelayRuleTime>
</MonitorRules> <DynamicMessage>DtsJobId</DynamicMessage> <ErrMessage>The Value of Input Parameter %s is not valid.</ErrMessage> <Code>200</Code> <Success>true</Success> <ErrCode>403</ErrCode>
```

`JSON` 格式数据传输

```json
{
    "DtsJobId": "ta7w132u12h****",
    "RequestId": "0CA14388-DD89-4A7B-8CDD-884A10CE****",
    "HttpStatusCode": 200,
    "MonitorRules": {
        "Type": "delay",
        "Phone": "1361234****,1371234****",
        "State": "Y",
        "DelayRuleTime": 11
    },
    "DynamicMessage": "DtsJobId",
    "ErrMessage": "The Value of Input Parameter %s is not valid.",
    "Code": 200,
    "Success": true,
    "ErrCode": 403
}
```

#### 查询ETL任务

##### 查询ETL任务详情

调用DescribeDtsEtlJobVersionInfo接口查看ETL任务详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDtsEtlJo bVersionInfo | 系统规定参数。取值：DescribeDtsEtlJobVersionInfo 。 |
| PageSize | Integer | 否 | 20 | 分页查询时设置的每页行数，默认为20。 |
| PageNumber | Integer | 否 | 1 | 当前实例状态列表的页码，默认为1。 |
| DtsInstanceId | String | 否 | dtsggk12iwya1a **** | DTS实例ID，您可以调用 DescribeDtsJobs接口查询实例ID。 |
| DtsJobId | String | 否 | l5512es7w15*** * | ETL任务ID，您可以调用 DescribeDtsJobs接口查询任务ID。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域ID。您可以调用 DescribeRegions接口查询阿里云地域列表。 |

**返回数据**

数据传输

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DtsEtlJobVersi onInfos | Array of DtsEtlJobVersi onInfo |  | 返回ETL任务信息对象数组。 |
| CreateTime | String | 1637229315000 | 创建ETL任务的时间戳。 |
| Creator | String | 10000000 | 创建者ID。 |
| CreatorName | String | ***@****.com | 创建者用户名。 |
| DtsInstanceId | String | dtsg******gd | DTS实例ID。 |
| DtsJobId | String | l5512es7w15**** | ETL任务ID。 |
| DtsJobName | String | test sql _ | ETL任务名称。 |
| ModifyTime | String | 1637230117000 | 修改时间戳。 |
| SafeCheckpoin t | String | 1637230117000 | 安全检查点，即ETL任务的当前位点。 |
| Status | String | INFO | 日志等级，有ERROR、WARN、INFO、 DEBUG4种等级。 |
| Version | Integer | 9 | ETL任务版本号。 |
| DynamicCode | String | 403 | 与本次请求相关的动态错误码。 |
| DynamicMess age | String | present environment is not support,so skip | 与本次请求相关的动态错误信息。 |
| ErrCode | String | InvalidJobId | 传入的ETL任务ID错误，找不到对应的任务。 |
| ErrMessage | String | The specified dts job id %s is not exists. | 传入的ETL任务ID错误，找不到对应的任务（任务可能已删除）。 |
| HttpStatusCod e | String | 200 | 状态码。 |
| PageNumber | Integer | 1 | 当前实例状态列表的页码，默认为1。 |

数据传输

| Success | Boolean | true | 请求是否成功，如果失败则返回false。 |
|---|---|---|---|
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB43E7 | 请求ID。 |
| PageRecordCo unt | Integer | 20 | 当前分页的记录数。 |
| TotalRecordCo unt | Integer | 200 | 记录的总行数。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeDtsEtlJobVersionInfo &pageSize=20 &pageNumber=0 &dtsInstanceId=dtsggk12iwya1a**** &DtsJobId=l5512es7w15**** &RegionId=cn-hangzhou
```

`&<`必填参数> `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDtsEtlJobVersionInfoResponse>
  <requestId>62E37CD4-586B-50A4-99AA-3E60D2485F6C</requestId>
  <success>true</success>
  <dtsEtlJobVersionInfos>
        <createTime>1637229315000</createTime>
        <creator>10000000</creator>
        <creatorName>***@****.com</creatorName>
        <dtsInstanceId>dtsggk12iwya1a****</dtsInstanceId>
        <dtsJobId>l5512es7w15****</dtsJobId>
        <dtsJobName>test_sql</dtsJobName>
        <modifyTime>1637230117000</modifyTime>
        <status>INFO</status>
        <version>9</version>
  </dtsEtlJobVersionInfos>
  <httpStatusCode>200</httpStatusCode>
</DescribeDtsEtlJobVersionInfoResponse>
```

`JSON` 格式数据传输

```json
{
    "requestId": "62E37CD4-586B-50A4-99AA-3E60D2485F6C",
    "success": true,
    "dtsEtlJobVersionInfos": [
        {
            "createTime": 1637229315000,
            "creator": "10000000",
            "creatorName": "***@****.com",
            "dtsInstanceId": "dtsggk12iwya1a****",
            "dtsJobId": "l5512es7w15****",
            "dtsJobName": "test_sql",
            "modifyTime": 1637230117000,
            "status": "INFO",
            "version": 9
        }
```

`],`

```json
    "httpStatusCode": 200
}
```

##### 查询ETL任务日志

调用DescribeEtlJobLogs接口查看ETL任务运行日志。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeEtlJobLo gs | 系统规定参数。取值：DescribeEtlJobLogs。 |
| DtsJobId | String | 是 | l5512es7w15*** * | ETL任务ID，您可以调用 DescribeDtsJobs接口查询任务ID。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所属的地域ID。您可以调用 DescribeRegions接口查询阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DynamicCode | String | 403 | 与本次请求相关的动态错误码。 |
| DynamicMess age | String | present environment is not support,so skip. | 与本次请求相关的动态错误信息。 |
| ErrCode | String | InvalidJobId | 传入的ETL任务ID错误，找不到对应的任务。 |

数据传输

| ErrMessage | String | The specified dts job id %s is not exists. | 传入的ETL任务ID错误，找不到对应的任务（任务可能已删除）。 |
|---|---|---|---|
| EtlRunningLog s | Array of EtlRunningLog |  | 返回ETL任务运行日志对象数组。 |
| Content | String | Starting DTS-ETL... | ETL任务运行状态描述。 |
| ContentKey | String | DTS-ETL | 状态，即产生日志的模块名，比如ETL任务的转换模块。 |
| EtlId | String | u**********5 | ETL任务的ID。 |
| LogDatetime | String | 1637306503000 | 记录时间戳（产生日志的时间）。 |
| Status | String | INFO | 日志等级，有ERROR、WARN、INFO、 DEBUG4种等级。 |
| UserId | String | 121323*******454 512 | 用户ID。 |
| HttpStatusCod e | Integer | 200 | 状态码。 |
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB43E7 | 请求ID。 |
| Success | Boolean | true | 请求是否成功，如果失败则返回false。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeEtlJobLogs &DtsJobId=l5512es7w15**** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<DescribeEtlJobLogsResponse>
  <requestId>62E37CD4-586B-50A4-99AA-3E60D2485F6C</requestId>
  <success>true</success>
  <etlRunningLogs>
        <content>Starting DTS-ETL...</content>
        <contentKey>DTS-ETL</contentKey>
        <etlId>u**********5</etlId>
        <gmtCreate>1637306505000</gmtCreate>
        <id>941</id>
        <logDatetime>1637306503000</logDatetime>
        <status>INFO</status>
  </etlRunningLogs>
  <httpStatusCode>200</httpStatusCode>
</DescribeEtlJobLogsResponse>
```

`JSON` 格式

```json
{
    "requestId": "62E37CD4-586B-50A4-99AA-3E60D2485F6C",
    "success": true,
    "etlRunningLogs": [
        {
            "content": "Starting DTS-ETL...",
            "contentKey": "DTS-ETL",
            "etlId": "u**********5",
            "gmtCreate": 1637306505000,
            "id": 941,
            "logDatetime": 1637306503000,
            "status": "INFO"
        }
```

`],`

```json
    "httpStatusCode": 200
}
```

#### 参数补充说明

##### 迁移、同步或订阅对象说明

DTS支持调用API接口，配置或查询DTS任务的迁移、同步或订阅对象。本文将为您介绍相关API接口，并提供对象的定义和配置案例。

**相关接口及参数**

| API | 说明 |
|---|---|
| 配置DTS迁移或同步任务配置DTS订阅任务 | 在请求参数 Dblist 中配置DTS任务的迁移、同步或订阅的对象。 |

数据传输

| 查询一个DTS任务详情查询DTS任务列表及各任务执行详情 | 在返回参数 DbObject 中查询DTS任务的迁移、同步或订阅的对象。 |
|---|---|

**迁移、同步或订阅对象定义说明**

迁移、同步或订阅对象的数据类型为JSON，详细定义如下： 请按需配置斜体部分的内容。

**说明**

如迁移、同步或订阅对象包含多个库，则您可参考如下定义：

```
{
```

"待迁移、同步或订阅的库1的名称`": {` `"name": "`迁移、同步或订阅的库1在目标实例中的名称`",` `"all": true`（表示迁移、同步或订阅对象为整库）

```
    },
```

"待迁移、同步或订阅的库2的名称`": {` `"name": "`迁移、同步或订阅的库2在目标实例中的名称`",` `"all": false`（表示迁移、同步或订阅对象为非整库）,

```json
        "Table": {
```

"待迁移、同步或订阅的表A的名称`": {` `"name": "`迁移、同步或订阅的表A在目标实例中的名称`",` `"all": true`（表示迁移、同步或订阅对象为整表）, `"dml_op": "`需增量迁移或同步的`DML`操作`",` `"ddl_op": "`需增量迁移或同步的`DDL`操作"

```
            }
        }
    },
```

"待迁移、同步或订阅的库3的名称`": {` `"name": "`迁移、同步或订阅的库3在目标实例中的名称`",` `"all": true`（表示迁移、同步或订阅对象为整库）, `"dml_op": "`需增量迁移或同步的`DML`操作`",` `"ddl_op": "`需增量迁移或同步的`DDL`操作"

```
    }
}
```

如迁移、同步或订阅对象的颗粒度为列，或者包含过滤条件，则您可参考如下定义： 数据传输

```
{
```

"待迁移、同步或订阅的库名`": {` `"name": "`迁移、同步或订阅的库在目标实例中的库名`",` `"all": false`（表示迁移、同步或订阅对象为非整库）,

```json
        "Table": {
```

"待迁移、同步或订阅的表名`A": {` `"name": "`迁移、同步或订阅的表在目标实例中的表名`A",` `"all": false`（表示迁移、同步或订阅对象为非整表）,

```json
                "filter": "id>10"
                "column": {
                    "id": {
                        "key": "PRI",
                        "name": "id",
                        "type": "int(11)",
                        "sharedKey": false,
                        "state": "checked"
                    }
                },
                "shard": 12
            }
        },
    }
}
```

如迁移、同步对象所属目标实例为云原生数据仓库AnalyticDB MySQL版、AnalyticDB PostgreSQL 版时，则您可参考如下定义：

```
{
```

"待迁移、同步的库的名称`": {` `"name": "`迁移、同步的库在目标实例中的名称`",` `"all": false`（固定为`false`。无论是对象为整库还是表级，如目标实例为`AnalyticDB MySQL`或`Ana` `lyticDB PostgreSQL`，固定传入`false`，且还需传入表对应的分区键等信息）,

```json
        "Table": {
```

"待迁移、同步的表A的名称`": {` `"all": true`（表示迁移、同步对象为整表）, `"name": "`迁移、同步的表A在目标实例中的名称`",` `"primary_key": "id`（指定主键）`",` `"type": "dimension`（表的类型）`",`

```
            }
```

"待迁移、同步的表B的名称`": {` `"all": true`（表示迁移、同步对象为整表）, `"name": "`迁移、同步的表B在目标实例中的名称`",` `"part_key": "id`（指定分区键）`",` `"primary_key": "id`（指定主键）`",` `"type": "partition`（表的类型）`",`

```
            }
        }
    }
}
```

| 参数 | 说明 |
|---|---|

数据传输

| name | 源库、表、列名映射到目标库、表、列的名称。如源库名为dtssource，目标库名为dtstarget，则您需在name中传入dtstarget，表示把源库名映射成dtstarget后写入目标库中。 |
|---|---|
| all | 是否选择全部表、列，取值： true ：是。 说明如选择全部表或列，则无需在配置具体的表或列信息。 false ：否。 |
| Table | 待迁移、同步或订阅的表信息。 |
| filter | 设置过滤条件，过滤待迁移、同步或订阅的数据。目前仅支持在表级别中体现。 例如您可传入 id>10 ，选择只迁移、同步该表中ID列的值大于10的数据。 说明订阅任务暂不支持设置过滤条件。 |
| column | 待迁移、同步或订阅的列信息。 |
| key | 是否为主键，取值： PRI ：是。 空值：否。 |
| sharedKey | 是否为分片键，取值： true ：是。 false ：否。 说明当迁移、同步对象所属数据库的类型为Kafka时，才需配置本参数。 |
| type | 该字段的数据类型。 |
| state | 如为 checked ，则表示该列被选中。 |
| shard | 待迁移、同步的表的分片数量。 说明当迁移、同步数据所属数据库的类型为Kafka时，才需配置本参数。 |
| dml op _ | 选择增量迁移或同步的DML操作，取值及意思如下： i ：INSERT。 u ：UPDATE。 d ：DELETE。 如该值为空，则表示增量迁移或同步该任务所有支持的DML操作。 none ：不增量迁移或同步DML操作。 |

数据传输

| ddl op _ | 选择增量迁移或同步的DDL操作。取值及意思如下： ct ：CREATE TABLE。 at ：ALTER TABLE。 dt ：DROP TABLE。 rt ：RENAME TABLE。 tt ：TRUNCATE TABLE。 如该值为空，则表示增量迁移或同步该任务所有支持的DDL操作。 none ：不增量迁移或同步DDL操作。 |
|---|---|
| primary key _ | 表示主键。当目标实例为云原生数据仓库AnalyticDB MySQL版、AnalyticDB PostgreSQL版时，本参数才可用且必须传入。 |
| part key _ | 表示分区键。当目标实例为云原生数据仓库AnalyticDB MySQL版、AnalyticDB PostgreSQL版时，本参数才可用且必须传入。 |
| type 重要此处的 type 参数与代表字段数据类型的 type 参数。 | 当目标实例为云原生数据仓库AnalyticDB MySQL版、AnalyticDB PostgreSQL 版时，您需要指明迁移、同步对象的表类型： dimension：维度表。 partition：分区表。 |

**迁移、同步或订阅对象配置示例**

示例一：迁移、同步或订阅dtstestdata库中所有的表。

```json
{"dtstestdata": { "name": "dtstestdata", "all": true }}
```

示例二：迁移、同步或订阅dtstestdata库，并修改库名为dtstestdata_new。

```json
{"dtstestdata": { "name": "dtstestdata_new", "all": true }}
```

示例三：迁移、同步或订阅dtstestdata库中部分表（如customer）。 数据传输

```json
{"dtstestdata": {
   "name": "dtstestdata",
   "all": false,
   "Table": {
     "customer": {
       "name": "customer",
       "all": true,
       "column": {
         "id": {
           "key": "PRI",
           "name": "id",
           "type": "int(11)",
           "sharedKey": false,
           "state": "checked"
         },
         "gmt_create": {
           "key": "",
           "name": "gmt_create",
           "type": "datetime",
           "sharedKey": false,
           "state": "checked"
         },
         "gmt_modify": {
           "key": "",
           "name": "gmt_modify",
           "type": "datetime",
           "sharedKey": false,
           "state": "checked"
         },
         "valid_time": {
           "key": "",
           "name": "valid_time",
           "type": "datetime",
           "sharedKey": false,
           "state": "checked"
         },
         "creator": {
           "key": "",
           "name": "creator",
           "type": "varchar(200)",
           "sharedKey": false,
           "state": "checked"
         }
       },
       "shard": 12
     }
   },
 }
}
```

示例四：迁移、同步或订阅dtstestdata库中的表（如customer和order）的部分列。 数据传输

```json
{"dtstestdata": {
   "name": "dtstestdata",
   "all": false,
   "Table": {
     "customer": {
       "name": "customer",
       "all": false,
       "column": {
         "id": {
           "key": "PRI",
           "name": "id",
           "type": "int(11)",
           "sharedKey": false,
           "state": "checked"
         },
         "level": {
           "key": "",
           "name": "level",
           "type": "varchar(5000)",
           "sharedKey": false,
           "state": "checked"
         },
         "name": {
           "key": "",
           "name": "name",
           "type": "varchar(500)",
           "sharedKey": false,
           "state": "checked"
         },
       },
       "shard": 12
     },
     "order": {
       "name": "order",
       "all": false,
      "column": {
         "id": {
           "key": "PRI",
           "name": "id",
           "type": "int(11)",
           "sharedKey": false,
           "state": "checked"
         }
       },
       "shard": 12
     }
   },
 }
}
```

示例五：迁移、同步或订阅dtstestdata库中的表（如customer、order、commodity）至目标实例云原生数据仓库AnalyticDB MySQL版、AnalyticDB PostgreSQL版中。 数据传输

```json
{
    "dtstestdata": {
        "name": "dtstestdatanew",
        "all": false,
        "Table": {
            "order": {
                "name": "ordernew",
                "all": true,
                "part_key": "id",
                "primary_key": "id",
                "type": "partition"
            },
            "customer": {
                "name": "customernew",
                "all": true,
                "primary_key": "id",
                "type": "dimension"
            },
            "commodity": {
                "name": "commoditynew",
                "all": false,
                "filter": "id>10",
                "column": {
                    "id": {
                        "key": "PRI",
                        "name": "id",
                        "type": "int(11)"
                    }
                },
                "part_key": "id",
                "primary_key": "id",
                "type": "partition"
            }
        }
    }
}
```

**支持的正则表达式**

| 符号 | 规则描述 |
|---|---|
| 英文句号（.） | 表示匹配除‘\r\n’之外的任何单个字符。 |
| 星号（*） | 表示匹配前面子表达式任意次，例如： h.*llo 将匹配 hllo或heeeello等字符串。 |
| 英文问号（?） | 表示匹配前面子表达式零次或1次，例如： h.?llo 将匹配hllo或hello，但不能匹配haello。 |
| [characters] 字符集合 | 表示匹配方括号内任意一个字符，例如： h[ae]llo 将匹配hallo或hello。 |
| [^characters] 负值字符集合 | 表示不匹配方括号内任意一个字符，例如： h[^ae]llo 将匹配hcllo或 hdllo，但不能匹配hallo或hello。 |

数据传输

| [character1-character2] 字符范围 | 表示匹配character1-character2范围内的字符，例如： [0-9]、[a-z]。 |
|---|---|

##### Reserve参数说明

在调用部分接口配置或查询迁移或同步、订阅任务时，您需要配置或查询预留参数Reserve来完善或查看源或目标实例的配置信息（比如目标Kafka数据库的数据存储格式、云企业网CEN的实例ID）。本文将介绍 Reserve参数的适用场景和配置说明。

**相关接口**

**Reserve的配置说明**

Reserve的数据类型为字符串String，传入格式为JSON，其适用场景和配置说明如下所示。 如所传入数据为数值，则您需加英文双引号（""），将其转变为字符串String。

**说明**

| 参数 | 是否必填 | 说明 |
|---|---|---|
| targetTableMode | 是 | 目标已存在表的处理模式： 0：预检查并报错拦截。 2：忽略报错并继续执行。 |

当目标实例的数据库类型为Kafka时，您需在Reserve参数中配置Kafka数据库的信息，以及投递到 Kafka数据库中的数据存储格式。

| 参数 | 是否必填 | 说明 |
|---|---|---|
| destTopic | 是 | 目标Kafka数据库中迁移或同步对象所属Topic。 |
| destVersion | 是 | 目标Kafka数据库的版本。支持传入1.0、0.9、0.10。 说明如Kafka数据库版本为1.0及以上， 则需传入1.0。 |
| destSSL | 是 | 连接目标Kafka数据库的方式，取值为： 0：非加密连接。 3：使用SCRAM-SHA-256进行加密连接。 |
| dest.kafka.schema.r egistry.url | 否 | 如使用 Kafka Schema Registry ，您需要输入在 Kafka Schema Registry中用于注册Avro Schema的 URL或IP。 |
| sink.kafka.ddl.topic | 否 | 输入具体的Topic，用于存储DDL信息。如果未输入，DDL信息默认存储在destTopic输入的Topic中。 |

数据传输

| kafkaRecordFormat | 是 | 数据投递到目标Kafka数据库中的存储格式，取值为： canal json：使用Canal来解析数据库增量日志， _ 并将增量数据传输至目标Kafka数据库中，数据存储格式为Canal Json。 dts avro：一种数据序列化格式，可将数据结构或 _ 对象转化成便于存储或传输的格式。 shareplex json：使用数据复制软 _ 件Shareplex读取源库中的数据，将数据写入至目标 Kafka数据库时，数据存储格式为Shareplex Json。 debezium：一种捕获数据变更的工具，支持将源 PolarDB O引擎集群中的数据更新实时流式传输到目标Kafka数据库中。 |
|---|---|---|
| destKafkaPartition Key | 是 | Kafka Partition（分区）同步策略，取值为： none：将所有数据和DDL信息都投递到目标Topic 的Partition 0。 database table：将库名与表名合并作为 _ Partition Key来计算Hash值，然后将各个表的数据和DDL信息投递到目标Topic中的各个Partition。 columns：将表中的列（默认为主键，如果无主键则使用唯一键）作为Partition Key来计算Hash值， 然后将不同的行投递到目标Topic的各个Partition 中。您也可以指定单个或多个列作为Partition Key 来计算Hash值。 |

示例：

```json
{
    "destTopic": "dtstestdata",
    "destVersion": "1.0",
    "destSSL": "0",
    "dest.kafka.schema.registry.url": "http://12.1.12.3/api",
    "sink.kafka.ddl.topic": "dtstestdata",
    "kafkaRecordFormat": "canal_json",
    "destKafkaPartitionKey": "none"
}
```

当源和目标实例的数据库类型为MongoDB时，您需在Reserve参数中指定MongoDB数据库的架构。

| 参数 | 是否必填 | 说明 | 示例 |
|---|---|---|---|
| srcEngineAr chType | 是 | 源数据库MongoDB的架构类型。 0 ：单节点架构。 1：副本集架构。 2：分片集群架构。 | { "srcEngineArchType": "1" } |
| destEngine ArchType | 是 | 目标数据库MongoDB的架构类型。 0 ：单节点架构。 1：副本集架构。 2：分片集群架构。 | { "destEngineArchType": "1" } |

当源或目标实例为通过云企业网CEN接入的自建数据库时，您需在Reserve参数中配置云企业网实例ID。 数据传输

| 参数 | 是否必填 | 说明 | 示例 |
|---|---|---|---|
| srcInstanceI d | 是 | 源实例的云企业网实例ID。 | { "srcInstanceId": "cen-9kqshqum*******" } |
| destInstanc eId | 是 | 目标实例的云企业网实例ID。 | { "destInstanceId": "cen-9kqshqum*******" } |

##### DataCheckConfigure参数说明

在调用ConfigureDtsJob接口配置迁移或同步时，您可以根据需求配置DataCheckConfigure参数。

**参数说明**

| 参数 | 类型 | 说明 |
|---|---|---|
| dataCheckDbList | String | 数据校验对象，为JSON格式。 |
| fullDataCheck | Boolean | 是否进行全量数据校验，取值为true或false。 |
| fullCheckModel | Integer | 全量数据校验任务的模式： 1：按抽样比例进行校验。 2：按行进行校验。 |
| fullCheckFixData | Boolean | 是否补齐数据，取值为true或false，默认值为false。 说明当取值为true时，若目标库有跟原库不一致的数据， 则会用源库的数据值替换目标库的数据值。 |
| fullCheckRatio | Integer | 全量数据校验任务的抽样比例。取值为10~100的整数， 单位为%。 说明当fullCheckModel取值为1时必填。 |

数据传输

| checkMaximumHourEnabl e | Integer | 全量数据校验任务是否配置超时设置： 0：不配置超时设置。 1：配置超时设置。 说明当fullCheckModel取值为1时必填。 |
|---|---|---|
| checkMaximumHour | Integer | 全量数据校验任务的超时设置，取值为1~72的整数。在全量数据校验任务启动后开始计时，若校验任务未在指定时间完成则强制结束。 |
| fullCheckReferEndpoint | String | 全量数据校验的基准，取值为： all：以源库和目标库数据的合集为基准，校验源库和目标库不一致的数据。 src：以源库为基准，校验目标库与源库数据的一致性 （不校验目标库比源库多的数据）。 dest：以目标库为基准，校验源库与目标库数据的一致性（不校验源库比目标库多的数据）。 |
| fullCheckMaxReadRps | Integer | 每秒读取数据的最大行数，取值为 0~9007199254740991的整数。 说明取值为0时表示不做限制。 |
| fullCheckMaxReadBps | Integer | 每秒读取的最大数据量（Byte），取值为 0~9007199254740991的整数。 说明取值为0时表示不做限制。 |
| dataCheckNoticePhone | String | 全量或增量数据校验任务告警联系人的手机号。当校验任务触发告警时，将以短信的形式通知告警联系人。 |
| fullCheckErrorNotice | Boolean | 是否进行全量数据校验失败告警。取值为true或false。 说明当取值为true时，全量数据校验任务失败则触发告警。 |

数据传输

| fullCheckValidFailNotice | Boolean | 是否进行全量校验数据不一致告警。取值为true或false。 说明当取值为true时，全量校验任务不一致数据的数量大于等于设置的阈值则触发告警。 |
|---|---|---|
| fullCheckNoticeValue | Integer | 全量数据校验不一致数据的告警阈值。 说明当fullCheckValidFailNotice取值为true时必填。 |
| incrementalDataCheck | Boolean | 是否进行增量数据校验，取值为true或false。 |
| incrementalCheckErrorNo tice | Boolean | 是否进行增量数据校验失败告警。取值为true或false。 说明当取值为true时，增量数据校验任务失败则触发告警。 |
| incrementalCheckValidFai lNotice | Boolean | 是否进行增量校验数据不一致告警。取值为true或false。 说明当取值为true时，若增量校验任务累计在若干个周期的不一致记录量均大于等于设置的阈值则触发告警。 |
| incrementalCheckValidFai lNoticePeriod | Integer | 增量数据校验任务不一致告警统计的周期： 1：表示周期为1分钟。 2：表示周期为5分钟。 3：表示周期为10分钟。 4：表示周期为30分钟。 说明当incrementalCheckValidFailNotice取值为true时必填。 |

数据传输

| incrementalCheckValidFai lNoticeTimes | Integer | 增量数据校验任务不一致告警统计周期的数量。 说明当incrementalCheckValidFailNotice取值为true时必填。 |
|---|---|---|
| incrementalCheckValidFai lNoticeValue | Integer | 增量数据校验任务不一致数据的告警阈值。 说明当incrementalCheckValidFailNotice取值为true时必填。 |
| incrementalCheckDelayNo tice | Boolean | 是否进行增量数据延迟告警。取值为true或false。 说明当取值为true时，若增量校验任务累计在若干个周期的延迟均大于等于设置的阈值则触发告警。 |
| incrementalCheckDelayNo ticePeriod | Integer | 增量数据校验任务延迟告警的统计周期： 1：表示周期为1分钟。 2：表示周期为5分钟。 3：表示周期为10分钟。 4：表示周期为30分钟。 说明当incrementalCheckDelayNotice取值为true时必填。 |
| incrementalCheckDelayNo ticeTimes | Integer | 增量数据校验任务延迟告警统计周期的数量。 说明当incrementalCheckDelayNotice取值为true时必填。 |
| incrementalCheckDelayNo ticeValue | Long | 增量数据校验任务延迟时间的告警阈值，单位为秒。 说明当incrementalCheckDelayNotice取值为true时必填。 |
| structureCheck | Boolean | 是否进行结构校验，取值为true或false。 |

数据传输

### 旧版API（即将停止维护）

#### 数据迁移

##### 购买迁移实例

调用CreateMigrationJob购买一个数据迁移实例。 此接口为旧版API，建议您使用新版API。

**说明**

购买完成后，还需要调用ConfigureMigrationJob接口配置迁移任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateMigrationJ ob | 系统规定参数，取值：CreateMigrationJob。 |
| MigrationJobClas s | String | 是 | 2xlarge | 数据迁移实例的规格，取值为：small、medium、large、xlarg e、2xlarge。 说明各个规格的测试性能。 实例规格及定价。 |
| Region | String | 是 | cn-hangzhou | 数据迁移实例所属的地域，即迁移的目标数据库实例所属地域。 |
| RegionId | String | 否 | cn-hangzhou | 数据迁移实例所属的地域，无需设置，该参数即将下线。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken参数只支持传入ASCII 字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

数据传输

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| MigrationJobId | String | dtsi8911td9233*** * | 数据迁移实例ID。 |
| RequestId | String | C166D79D-436B- 45F0-B5A5- 25E1959F**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=CreateMigrationJob &MigrationJobClass=2xlarge &Region=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateMigrationJobResponse>
      <RequestId>C166D79D-436B-45F0-B5A5-25E1959F****</RequestId>
      <Success>true</Success>
      <MigrationJobId>dtsi8911td9233****</MigrationJobId>
</CreateMigrationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "C166D79D-436B-45F0-B5A5-25E1959F****",
 "Success": true,
 "MigrationJobId": "dtsi8911td9233****"
}
```

##### 配置迁移实例

调用ConfigureMigrationJob接口配置数据迁移实例。 本接口调用成功后，将自动启动数据迁移任务，您无需手动调用StartMigrationJob接口。 数据传输如果数据迁移任务未成功启动，可能是由于预检查失败，您可以调用DescribeMigrationJobStatus接口查询预检查失败的错误提示并修复问题。问题修复后，您需要手动调用StartMigrationJob接口来重启数据迁移任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ConfigureMigrati onJob | 系统规定参数，取值：ConfigureMigrationJob。 |
| DestinationEndp oint.InstanceTyp e | String | 是 | RDS | 目标库的实例类型，取值： 说明 ECS：ECS上的自建数据库。 LocalInstance：有公网IP 的自建数据库。 RDS：阿里云RDS实例。 DRDS：阿里云PolarDB-X 实例。 MongoDB：阿里云 MongoDB实例。 Redis：阿里云Redis实例。 PetaData：阿里云 HybridDB for MySQL实例。 POLARDB：阿里云 PolarDB MySQL、PolarDB PostgreSQL。 PolarDB o：阿里云 _ PolarDB O引擎集群。 AnalyticDB：阿里云云原生数据仓库AnalyticDB MySQL 3.0和2.0版本。 Greenplum：阿里云云原生数据仓库AnalyticDB PostgreSQL。 |

数据传输

| MigrationJobId | String | 是 | dtsl3m1213ye7l **** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
|---|---|---|---|---|
| MigrationJobNa me | String | 是 | MySQL TO RDS _ _ | 迁移任务名称，不超过32个字符。建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| MigrationMode.D ataIntialization | Boolean | 是 | true | 是否进行全量数据迁移，取值： true：是。 false：否。 说明 DTS对全量数据迁移的支持情况因数据库类型不同而有所差异。 |
| MigrationMode.D ataSynchronizati on | Boolean | 是 | true | 是否进行增量数据迁移，取值： true：是。 false：否。 说明 DTS对增量数据迁移的支持情况因数据库类型不同而有所差异。 |
| MigrationMode.S tructureIntializat ion | Boolean | 是 | true | 是否进行结构迁移，取值： true：是。 false：否。 说明 DTS对结构迁移的支持情况因数据库类型不同而有所差异。 |
| MigrationObject | String | 是 | [{"DBName":"dt stestdata","Tabl eIncludes": [{"TableName":" customer"}]}] | 待迁移的对象，格式为JSON串，且支持一定的正则表达式。 |

数据传输

| SourceEndpoint.I nstanceType | String | 是 | RDS | 源库的实例类型，取值： RDS：阿里云RDS实例。 ECS：ECS上的自建数据库。 LocalInstance：有公网IP的自建数据库。 Express：通过专线/VPN网关/智能接入网关接入的自建数据库。 dg：通过数据库网关DG接入的自建数据库。 cen：通过云企业网CEN接入的自建数据库。 MongoDB：阿里云MongoDB实例。 POLARDB：阿里云PolarDB MySQL、PolarDB PostgreSQL。 PolarDB o：阿里云PolarDB O引擎 _ 集群。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 数据迁移实例所在地域的ID。 说明与目标库所属的地域ID 保持一致。 |
| SourceEndpoint.I nstanceID | String | 否 | rm- bp1i99e8l7913* *** | 源库的实例ID。 说明当SourceEndpoint.Inst anceType取值为RDS、ECS、Express 、MongoDB、POLARDB 或PolarDB o时，本参数才 _ 可用且必须传入对应的实例 ID（例如取值为ECS，则本参数传入ECS实例的ID）。 当SourceEndpoint.Inst anceType取值为Express时，本参数传入 VPC ID（即专有网络ID）。 |
| SourceEndpoint. EngineName | String | 否 | MySQL | 源库的数据库类型，取值：MySQL、TiDB、SQLServer、P ostgreSQL、Oracle、MongoDB、R edis、POLARDB、polardb pg。 _ 说明当DestinationEndpoint.Instan ceType取值为RDS、POLARDB、ECS、Loca lInstance或Express时，本参数才可用且必须传入。 |

数据传输

| SourceEndpoint. Region | String | 否 | cn-hangzhou | 源库所属的地域ID。 说明当SourceEndpoint.InstanceTy pe取值为LocalInstance时，您可以传入cn-hangzhou或者离自建数据库地物理距离最近的地域ID。 |
|---|---|---|---|---|
| SourceEndpoint.I P | String | 否 | 172.16.88.*** | 源库的连接地址。 说明当SourceEndpoint.InstanceTy pe取值为LocalInstance或Express时， 本参数才可用且必须传入。 |
| SourceEndpoint. Port | String | 否 | 3306 | 源库的服务端口。 说明当SourceEndpoint.InstanceTy pe取值为ECS、LocalInstance或Expre ss时，本参数才可用且必须传入。 |
| SourceEndpoint. OracleSID | String | 否 | testsid | Oracle数据库的SID信息。 说明当SourceEndpoint.EngineNa me取值为Oracle，且Oracle数据库为非RAC实例时，本参数才可用且必须传入。 |
| SourceEndpoint. DatabaseName | String | 否 | dtstestdatabase | 待迁移的数据库名称或鉴权数据库名称。 说明当SourceEndpoint.Engi neName取值为PostgreSQL或Mongo DB时，本参数才可用且必须传入。 当SourceEndpoint.Engi neName取值为PostgreSQL时，传入待迁移的数据库名称；取值为MongoDB时，传入数据库账号的鉴权数据库名称。 |
| SourceEndpoint. UserName | String | 否 | dtstestaccount | 源库的数据库账号。 说明迁移不同的数据库所需的权限有所差异。 |

数据传输

| SourceEndpoint. Password | String | 否 | Test123456 | 源库数据库账号的密码。 |
|---|---|---|---|---|
| SourceEndpoint. OwnerID | String | 否 | 140692647406* *** | 源实例所属的阿里云账号ID。 说明仅在配置跨阿里云账号的数据迁移时本参数才可用，且必须传入。 |
| SourceEndpoint. Role | String | 否 | ram-for-dts | 当源实例与目标实例所属阿里云账号不同时，需传入该参数，来指定源实例的授权角色，以允许目标实例阿里云账号访问源实例的实例信息。 |
| DestinationEndp oint.InstanceID | String | 否 | rm- bp1r46452ai50* *** | 目标实例ID。 说明当DestinationEndpoint.Instan ceType取值为RDS、ECS、MongoDB、Redi s、DRDS、PetaData、OceanB ase、POLARDB、PolarDB o、 _ AnalyticDB或Greenplum时，本参数才可用且必须传入对应的实例 ID（例如取值为ECS，则需要传入 ECS实例ID）。 |
| DestinationEndp oint.EngineNam e | String | 否 | MySQL | 目标库的数据库类型。取值：MySQL、DRDS、SQLServer、P ostgreSQL、PPAS、MongoDB、Re dis、POLARDB、polardb pg _ 说明当DestinationEndpoint.Instan ceType取值为RDS、POLARDB、ECS、Loca lInstance或Express时，本参数才可用且必须传入。 |
| DestinationEndp oint.Region | String | 否 | cn-hangzhou | 目标库所属的地域ID。 说明当DestinationEndpoint.Instan ceType取值为LocalInstance时，您可以传入cn-hangzhou或者离自建数据库地物理距离最近的地域ID。 |

数据传输

| DestinationEndp oint.IP | String | 否 | 172.16.88.*** | 目标库的连接地址。 说明当DestinationEndpoint.Instan ceType取值为LocalInstance或Express时， 本参数才可用且必须传入。 |
|---|---|---|---|---|
| DestinationEndp oint.Port | String | 否 | 3306 | 目标库的服务端口。 说明当DestinationEndpoint.Instan ceType取值为ECS、LocalInstance或Expre ss时，本参数才可用且必须传入。 |
| DestinationEndp oint.DataBaseNa me | String | 否 | dtstestdatabase | 待迁入的数据库名称或鉴权数据库名称。 说明当DestinationEndpoint .EngineName取值为PostgreSQL、DRDS或 MongoDB时，本参数才可用且必须传入。 当DestinationEndpoint .EngineName取值为PostgreSQL或DRDS时 ，传入待迁移的数据库名称；取值为MongoDB时， 传入数据库账号的鉴权数据库名称。 |
| DestinationEndp oint.UserName | String | 否 | dtstestaccount | 目标库的数据库账号。 说明迁移不同的数据库所需的权限有所差异。 |
| DestinationEndp oint.Password | String | 否 | Test123456 | 目标库数据库账号的密码。 |

数据传输

| MigrationReserv ed | String | 否 | { "autoStartModul esAfterConfig": "none", "targetTableMod e": 2 } | DTS预留参数，格式为JSON串，您可以传入本参数实现特殊需求（例如是否自动启动预检查）。 |
|---|---|---|---|---|
| Checkpoint | String | 否 | 111 | 增量数据迁移的启动位点，格式为Unix时间戳，单位为秒。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |
| DestinationEndp oint.OracleSID | String | 否 | testsid | Oracle数据库的SID信息。 说明当DestinationEndpoint.Engin eName取值为Oracle， 且Oracle数据库为非RAC实例时， 本参数才可用且必须传入。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 40E35BD9-002E- 4D63-9BE5- FBA48833**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ConfigureMigrationJob &DestinationEndpoint.InstanceType=RDS &MigrationJobId=dtsl3m1213ye7l**** &MigrationJobName=MySQL_TO_RDS &MigrationMode.DataIntialization=true &MigrationMode.DataSynchronization=true &MigrationMode.StructureIntialization=true &MigrationObject=[{"DBName":"dtstestdata","TableIncludes":[{"TableName":"customer"}]}] &SourceEndpoint.InstanceType=RDS
```

`&<`公共请求参数> 数据传输正常返回示例 `XML` 格式

```xml
<ConfigureMigrationJobResponse>
      <RequestId>40E35BD9-002E-4D63-9BE5-FBA48833****</RequestId>
      <Success>true</Success>
</ConfigureMigrationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "40E35BD9-002E-4D63-9BE5-FBA48833****",
 "Success": true
}
```

##### 启动迁移实例

调用StartMigrationJob接口启动数据迁移实例。 调用本接口时，数据迁移任务须处于未启动、暂停或迁移失败状态。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartMigrationJo b | 系统规定参数，取值：StartMigrationJob。 |
| MigrationJobId | String | 是 | dtss0611o8vv90 **** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |

数据传输

| RequestId | String | FDC111B1-ACBF- 457D-9656- 247FDEE9**** | 请求ID。 |
|---|---|---|---|
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=StartMigrationJob &MigrationJobId=dtss0611o8vv90****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StartMigrationJobResponse>
      <RequestId>FDC111B1-ACBF-457D-9656-247FDEE9****</RequestId>
      <Success>true</Success>
</StartMigrationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "FDC111B1-ACBF-457D-9656-247FDEE9****",
 "Success": true
}
```

##### 修改迁移对象

调用ModifyMigrationObject修改处于未启动状态下的数据迁移实例的迁移对象。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyMigration Object | 系统规定参数，取值：ModifyMigrationObject。 |
| MigrationJobId | String | 是 | dtskfq1149w254 **** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| MigrationObject | String | 是 | [{"DBName": "dtstestdata"}] | 待迁移的对象（修改后），格式为JSON串且支持一定的正则表达式。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |

数据传输

| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
|---|---|---|---|---|
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | DFF8D631-18BF- 5768-934F- 55A6613*** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifyMigrationObject &MigrationJobId=dtskfq1149w254**** &MigrationObject=[{"DBName": "dtstestdata"}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>DFF8D631-18BF-5768-934F-55A6613***</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "DFF8D631-18BF-5768-934F-55A6613***",
    "Success": true
}
```

##### 暂停迁移实例

调用SuspendMigrationJob接口暂停处于迁移中的数据迁移实例。 数据传输

**说明**

如果数据迁移任务已进入增量数据迁移阶段，请勿将迁移任务暂停超过6个小时，否则将无法调用StartMigrationJob接口重启该任务。 如果按量付费的数据迁移任务配置了增量迁移，即使处于暂停状态，DTS依然会收取费用。这是由于DTS只是暂停向目标库写入数据，仍然会继续拉取源库的日志以便重启任务后快速恢复运行，因此还是会占用源数据库的带宽等资源。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SuspendMigratio nJob | 系统规定参数，取值：SuspendMigrationJob。 |
| MigrationJobId | String | 是 | dtsj1x11y51g3b **** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | C306C198-7807- 409D-930A- D6CE6C32**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=SuspendMigrationJob &SynchronizationJobId=dtsj1x11y51g3b****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<SuspendMigrationJobResponse>
      <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId>
      <Success>true</Success>
</SuspendMigrationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "C306C198-7807-409D-930A-D6CE6C32****",
 "Success": true
}
```

##### 查询迁移实例列表及各实例详情

调用DescribeMigrationJobs查询数据迁移实例列表和各迁移实例的详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMigrati onJobs | 系统规定参数，取值：DescribeMigrationJobs。 |
| RegionId | String | 否 | cn-hangzhou | 数据迁移实例所在地域的ID。 |
| PageSize | Integer | 否 | 30 | 每页记录的数据迁移实例的数量，取值：30、50、100，默认值为30。 |
| PageNum | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| MigrationJobNa me | String | 否 | MySQL迁移 | 迁移实例名称。 说明支持模糊查询。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

数据传输

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| MigrationJobs | Array of MigrationJob |  | 数据迁移实例列表和各迁移实例的详情。 |
| MigrationJob |  |  |  |
| DataInitializati on | Struct |  | 全量数据迁移情况。 |
| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据迁移失败的错误提示。 |
| Percent | String | 100 | 全量数据迁移进度，单位为百分比。 |
| Progress | String | 200001 | 已完成全量数据初始化的记录数。 |
| status | String | Finished | 全量数据迁移状态，取值包括： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 |
| DataSynchroni zation | Struct |  | 增量数据迁移情况。 |
| Delay | String | 0 | 增量数据迁移延迟，单位为秒。 |
| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据迁移失败的错误提示。 |
| Percent | String | 95 | 增量数据迁移进度，单位为百分比。 |
| status | String | Catched | 增量数据迁移状态，取值包括： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 Catched：无延迟。 |

数据传输

| DestinationEn dpoint | Struct |  | 目标实例的连接信息。 |
|---|---|---|---|
| DatabaseNam e | String | dtstestdata | 目标实例中待迁移对象所属数据库的名称。 |
| EngineName | String | MySQL | 目标实例的数据库类型。 |
| IP | String | 172.16.88.*** | 目标实例的连接地址。 |
| InstanceID | String | rm- bp1zc3iyqe3qw**** | 目标实例ID。 |
| InstanceType | String | RDS | 目标实例类型。 |
| OracleSID | String | testsid | 当目标实例的数据库类型为Oracle时，才会返回该参数。 |
| Port | String | 3306 | 目标实例的数据库服务端口。 |
| UserName | String | dtstest | 目标实例的数据库账号。 |
| MigrationJobCl ass | String | 2xlarge | 数据迁移实例的规格，返回值为：small、medium、large、xlarge或2x large。 |
| MigrationJobID | String | dtson2z28evm33** ** | 数据迁移实例ID。 |
| MigrationJobN ame | String | MySQL迁移 | 数据迁移实例名称。 |
| MigrationJobSt atus | String | Migrating | 迁移实例状态，返回值为： NotStarted：未启动。 Prechecking：表示预检查中。 PrecheckFailed：表示预检查失败。 Migrating：表示迁移中。 Suspending：表示暂停中。 MigrationFailed：表示迁移失败。 Finished：表示完成。 |
| MigrationMode | Struct |  | 迁移类型。 |
| DataInitializati on | Boolean | true | 是否迁移全量数据，取值： true：是。 false：否。 |

数据传输

| DataSynchroni zation | Boolean | true | 是否迁移增量数据，取值： true：是。 false：否。 |
|---|---|---|---|
| StructureInitial ization | Boolean | true | 是否执行结构迁移，取值： true：是。 false：否。 |
| MigrationObje ct | Array of SynchronousO bject |  | 迁移对象。 |
| SynchronousO bject |  |  |  |
| DatabaseNam e | String | dtstestdata | 源实例中待迁移对象所属数据库的名称。 |
| TableList | List | customer | 迁移对象的表名。 |
| WholeDatabas e | String | false | 是否迁移整库，返回值： true：是。 false：否。 |
| PayType | String | PostPaid | 迁移实例的付费类型，返回值固定为PostPaid（按量付费）。 |
| Precheck | Struct |  | 预检查情况。 |
| Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| Status | String | Success | 预检查结果，返回值： Success：通过。 Failed：未通过。 |
| SourceEndpoin t | Struct |  | 源实例的连接信息。 |
| DatabaseNam e | String | dtstestdata | 源实例中待迁移对象所属数据库的名称。 |
| EngineName | String | MySQL | 源实例的数据库类型。 |
| IP | String | 172.16.88.*** | 源实例的连接地址。 |
| InstanceID | String | rm- bp1i99e8l7913**** | 源实例ID。 |

数据传输

| InstanceType | String | RDS | 源实例类型。 |
|---|---|---|---|
| OracleSID | String | testsid | 当源实例的数据库类型为Oracle时，才会返回该参数。 |
| Port | String | 3306 | 源实例的数据库服务端口。 |
| UserName | String | dtstest | 源实例的数据库账号。 |
| StructureInitial ization | Struct |  | 结构迁移情况。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | 结构迁移失败的错误提示。 |
| Percent | String | 100 | 结构迁移进度，单位为百分比。 |
| Progress | String | 1 | 已完成结构迁移的表的数量。 |
| status | String | Finished | 结构迁移状态，取值包括： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 当前页可展示的最大记录数。 |
| RequestId | String | 0ED4846D-ED60- 435D-88C0- 7EC0CE4D**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |
| TotalRecordCo unt | Long | 300 | 阿里云主账号下所有符合条件的数据迁移实例数量。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=DescribeMigrationJobs &Tag.1.Key=testkey1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeMigrationJobsResponse>
      <TotalRecordCount>300</TotalRecordCount>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>0ED4846D-ED60-435D-88C0-7EC0CE4D****</RequestId>
      <PageNumber>1</PageNumber>
      <MigrationJobs>
            <MigrationJob>
                  <DataSynchronization>
                        <Percent>95</Percent>
                        <Delay>0</Delay>
                        <status>Catched</status>
                  </DataSynchronization>
                  <Precheck></Precheck>
                  <InstanceCreateTime>2021-06-22T09:02:13Z</InstanceCreateTime>
                  <JobCreateTime>2021-06-22T08:53:55Z</JobCreateTime>
                  <MigrationJobName>MySQL迁移</MigrationJobName>
                  <PayType>PostPaid</PayType>
                  <MigrationJobStatus>Migrating</MigrationJobStatus>
                  <MigrationMode>
                        <DataInitialization>true</DataInitialization>
                        <DataSynchronization>true</DataSynchronization>
                        <StructureInitialization>true</StructureInitialization>
                  </MigrationMode>
                  <MigrationJobID>dtson2z28evm33****</MigrationJobID>
                  <MigrationObject>
                        <SynchronousObject>
                              <DatabaseName>dtstest</DatabaseName>
                              <WholeDatabase>false</WholeDatabase>
                              <TableList>
                                    <Table>customer</Table>
                              </TableList>
                        </SynchronousObject>
                  </MigrationObject>
                  <DataInitialization>
                        <Progress>200001</Progress>
                        <Percent>100</Percent>
                        <status>Finished</status>
                  </DataInitialization>
                  <DestinationEndpoint>
                        <UserName>dtstest</UserName>
                        <InstanceID>rm-bp1zc3iyqe3qw****</InstanceID>
                        <InstanceType>RDS</InstanceType>
                        <EngineName>MySQL</EngineName>
                  </DestinationEndpoint>
                  <MigrationJobClass>2xlarge</MigrationJobClass>
                  <SourceEndpoint>
```

数据传输

```xml
                        <UserName>dtstest</UserName>
                        <InstanceID>rm-bp1i99e8l7913****</InstanceID>
                        <InstanceType>RDS</InstanceType>
                        <EngineName>MySQL</EngineName>
                  </SourceEndpoint>
                  <StructureInitialization>
                        <Progress>1</Progress>
                        <Percent>100</Percent>
                        <status>Finished</status>
                  </StructureInitialization>
                  <Tags></Tags>
            </MigrationJob>
      </MigrationJobs>
      <Success>true</Success>
</DescribeMigrationJobsResponse>
```

`JSON` 格式

```json
{
 "TotalRecordCount": 300,
 "PageRecordCount": 30,
 "RequestId": "0ED4846D-ED60-435D-88C0-7EC0CE4D****",
 "PageNumber": 1,
 "MigrationJobs": {
  "MigrationJob": [
   {
    "DataSynchronization": {
     "Percent": "95",
     "Delay": "0",
     "status": "Catched"
    },
    "Precheck": {},
                "InstanceCreateTime": "2021-06-22T09:02:13Z",
    "JobCreateTime": "2021-06-22T08:53:55Z",
    "MigrationJobName": "MySQL迁移",
    "PayType": "PostPaid",
    "MigrationJobStatus": "Migrating",
    "MigrationMode": {
     "DataInitialization": true,
     "DataSynchronization": true,
     "StructureInitialization": true
    },
    "MigrationJobID": "dtson2z28evm33****",
    "MigrationObject": {
     "SynchronousObject": [
      {
       "DatabaseName": "dtstest",
       "WholeDatabase": false,
       "TableList": {
        "Table": [
         "customer"
```

]

```
       }
      }
```

数据传输

```
}
```

]

```json
    },
    "DataInitialization": {
     "Progress": "200001",
     "Percent": "100",
     "status": "Finished"
    },
    "DestinationEndpoint": {
     "UserName": "dtstest",
     "InstanceID": "rm-bp1zc3iyqe3qw****",
     "InstanceType": "RDS",
     "EngineName": "MySQL"
    },
    "MigrationJobClass": "2xlarge",
    "SourceEndpoint": {
     "UserName": "dtstest",
     "InstanceID": "rm-bp1i99e8l7913****",
     "InstanceType": "RDS",
     "EngineName": "MySQL"
    },
    "StructureInitialization": {
     "Progress": "1",
     "Percent": "100",
     "status": "Finished"
    },
    "Tags": {
     "Tag": []
    }
   }
```

]

```json
 },
 "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请您稍后重试。 |

##### 查询一个迁移实例详情

调用DescribeMigrationJobDetail接口查询数据迁移任务执行详情。 调用本接口时，数据迁移任务需处于迁移中、迁移失败、暂停或迁移完成状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | DescribeMigrati onJobDetail | 系统规定参数，取值：DescribeMigrationJobDetail。 |
|---|---|---|---|---|
| MigrationJobId | String | 是 | dtsta7w132u12h **** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据迁移实例所在地域的ID。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30、50、100，默认值为30。 |
| PageNum | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| MigrationMode.S tructureInitializa tion | Boolean | 否 | true | 是否查询结构迁移详情，取值： true：是。 false：否。 说明默认值为false。 |
| MigrationMode.D ataInitialization | Boolean | 否 | true | 是否查询全量数据迁移详情，取值： true：是。 false：否。 说明默认值为false。 |
| MigrationMode.D ataSynchronizati on | Boolean | 否 | true | 是否查询增量数据迁移详情，取值： true：是。 false：否。 说明默认值为false。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| DataSynchroni zationDetailLis t | Array of DataSynchroni zationDetail |  | 增量数据迁移执行详情。 |
|---|---|---|---|
| DataSynchroni zationDetail |  |  |  |
| DestinationOw nerDBName | String | dtstestdata | 目标实例中迁移对象所属数据库的名称。 |
| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据迁移失败的错误提示。 |
| SourceOwnerD BName | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| Status | String | Migrating | 增量数据迁移状态，返回值： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 |
| TableName | String | customer | 待迁移对象的表名。 |
| DataInitializati onDetailList | Array of DataInitializati onDetail |  | 全量数据迁移执行详情。 |
| DataInitializati onDetail |  |  |  |
| DestinationOw nerDBName | String | dtstestdata | 目标实例中迁移对象所属数据库的名称。 |
| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据迁移失败的错误提示。 |
| FinishRowNum | String | 200001 | 已迁移的记录数。 |
| MigrationTime | String | 0.0 | 全量数据迁移的耗时。 |
| SourceOwnerD BName | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| Status | String | Finished | 全量数据迁移状态，返回值： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 |

数据传输

| TableName | String | customer | 待迁移对象的表名。 |
|---|---|---|---|
| TotalRowNum | String | 201477 | 需迁移的总记录数。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 一页最多可展示的迁移实例数量。 |
| RequestId | String | 0AE3CD0B-4148- 426F-A90E- 952467CC**** | 请求ID。 |
| StructureInitial izationDetailLi st | Array of StructureInitial izationDetail |  | 结构迁移执行详情。 |
| StructureInitial izationDetail |  |  |  |
| ConstraintList | Array of StructureInitial izationDetail |  | 迁移对象对应的约束（例如索引、外键等）。 说明只有当ObjectType为Table，且迁移对象有约束时，才会返回本参数。 |
| StructureInitial izationDetail |  |  |  |
| DestinationOw nerDBName | String | dtstestdata | 目标实例中迁移对象所属数据库的名称。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist； | 约束创建失败的错误提示。 |
| ObjectDefinitio n | String | CREATE SEQUENCE "public"."collection s id seq" _ _ MINVALUE 1 MAXVALUE 922337203685477 5807 START 249 INCREMENT BY 1 ; | 创建约束的结构语法定义。 |

数据传输

| ObjectName | String | customer | 迁移对象名称。 |
|---|---|---|---|
| ObjectType | String | Table | 迁移对象的类型，固定为Table。 |
| SourceOwnerD BName | String | dtstestdata | 源实例中迁移对象所属数据库的名称。 |
| Status | String | Finished | 约束创建状态，返回值： NotStarted：未启动。 Migrating：创建中。 Failed：创建失败。 Finished：创建完成。 |
| DestinationOw nerDBName | String | dtstestdata | 目标实例中待迁移对象所属数据库的名称。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: DTS-1020042 Execute sql error sql: ERROR: column \"id\" named in key does not exist | 结构迁移失败的错误提示。 |

数据传输

| ObjectDefinitio n | String | CREATE TABLE `dtstestdata`.`cust omer` (\n`runoob id` _ int(10) unsigned auto increment _ COMMENT '' NOT NULL , \n`runoob title` _ varchar(100) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NOT NULL , \n`runoob author1 _ 216` varchar(40) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NOT NULL , \n`submission date _ 1216` date COMMENT '' NULL \n, PRIMARY KEY (`runoob id`)) _ engine=InnoDB AUTO INCREMENT _ =200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8 general ci` _ _ ROW FORMAT= _ Dynamic comment = '' ;\n | 迁移对象的结构语法定义。 |
|---|---|---|---|
| ObjectName | String | customer | 迁移对象名称。 |
| ObjectType | String | Table | 迁移对象类型，返回值：Table（表）、Constraint（约束）、Index（索引）、View（视图）、Materialize View（物化视图）、Type（自定义类型）、Synonym（同义词）、Trigger（触发器）、Function（函数）、Procedure（存储过程）、Package（包）、Default（默认值）、Rule（规则）、PlanGuide（执行计划）、Sequence（序列）。 |
| SourceOwnerD BName | String | dtstestdata | 源实例中待迁移对象所属数据库的名称。 |
| Status | String | Finished | 结构迁移状态，返回值： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 |

数据传输

| Success | String | true | 请求是否成功。 |
|---|---|---|---|
| TotalRecordCo unt | Long | 1 | 总记录数。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeMigrationJobDetail &MigrationJobId=dtsta7w132u12h****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<DescribeMigrationJobDetailResponse>
      <DataSynchronizationDetailList>
            <DataSynchronizationDetail>
                  <Status>Migrating</Status>
                  <TableName>customer</TableName>
                  <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
                  <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
            </DataSynchronizationDetail>
      </DataSynchronizationDetailList>
      <RequestId>0AE3CD0B-4148-426F-A90E-952467CC****</RequestId>
      <DataInitializationDetailList>
            <DataInitializationDetail>
                  <Status>Finished</Status>
                  <TableName>customer</TableName>
                  <TotalRowNum>201477</TotalRowNum>
                  <MigrationTime>0.0</MigrationTime>
                  <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
                  <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
                  <FinishRowNum>200001</FinishRowNum>
            </DataInitializationDetail>
      </DataInitializationDetailList>
      <Success>true</Success>
      <StructureInitializationDetailList>
            <StructureInitializationDetail>
                  <Status>Finished</Status>
                  <ObjectType>Table</ObjectType>
                  <ObjectDefinition>CREATE TABLE `dtstestdata`.`customer` (
`runoob_id` int(10) unsigned auto_increment COMMENT '' NOT NULL , `runoob_title` varchar(100) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , `runoob_author1216` varchar(40) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT ' ' NOT NULL , `submission_date1216` date COMMENT '' NULL , PRIMARY KEY (`runoob_id`)) engine=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8_general_ci` ROW_FORMAT= Dynamic comment = '' ; </ObjectDefinition>
                  <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
                  <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
                  <ObjectName>customer</ObjectName>
            </StructureInitializationDetail>
      </StructureInitializationDetailList>
</DescribeMigrationJobDetailResponse>
```

`JSON` 格式数据传输

```json
{
 "DataSynchronizationDetailList": {
  "DataSynchronizationDetail": [
   {
    "Status": "Migrating",
    "TableName": "customer",
    "SourceOwnerDBName": "dtstestdata",
    "DestinationOwnerDBName": "dtstestdata"
   }
```

]

```json
 },
 "RequestId": "0AE3CD0B-4148-426F-A90E-952467CC****",
 "DataInitializationDetailList": {
  "DataInitializationDetail": [
   {
    "Status": "Finished",
    "TableName": "customer",
    "TotalRowNum": "201477",
    "MigrationTime": "0.0",
    "SourceOwnerDBName": "dtstestdata",
    "DestinationOwnerDBName": "dtstestdata",
    "FinishRowNum": "200001"
   }
```

]

```json
 },
 "Success": true,
 "StructureInitializationDetailList": {
  "StructureInitializationDetail": [
   {
    "Status": "Finished",
    "ObjectType": "Table",
    "ObjectDefinition": "CREATE TABLE `dtstestdata`.`customer` (\n`runoob_id`  int(10)
unsigned auto_increment COMMENT '' NOT NULL , \n`runoob_title` varchar(100) CH ARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , \n`runoob_author1216` varchar(40) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , \n`submission_date1216` date COMMENT '' NULL \n, PRIMARY KEY (`runoob_id`)) engine=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=`utf8` DEFAULT COLLA TE `utf8_general_ci` ROW_FORMAT= Dynamic comment = '' ;\n",
    "SourceOwnerDBName": "dtstestdata",
    "DestinationOwnerDBName": "dtstestdata",
    "ObjectName": "customer"
   }
```

]

```
 }
}
```

##### 查询一个迁移实例状态

调用DescribeMigrationJobStatus接口查询一个数据迁移实例的状态。

**请求参数**

数据传输

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMigrati onJobStatus | 系统规定参数，取值：DescribeMigrationJobStatus。 |
| MigrationJobId | String | 是 | dtsz2v12jfo309* *** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据迁移实例所在地域的ID。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DataInitializati onStatus | Struct |  | 全量数据迁移执行状态。 |
| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据迁移失败的错误提示。 |
| Percent | String | 100 | 全量数据迁移进度，单位为百分比。 |
| Progress | String | 200001 | 已完成全量数据初始化的记录数。 |
| Status | String | Finished | 全量数据迁移状态，取值包括： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 |
| DataSynchroni zationStatus | Struct |  | 增量数据迁移执行状态。 |
| Checkpoint | String | 1612507847 | 迁移最新一条增量数据的时间戳，格式为Unix时间戳，单位为秒。 |
| Delay | String | 0 | 增量数据迁移延迟，单位为秒。 |

数据传输

| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据迁移失败的错误提示。 |
|---|---|---|---|
| Percent | String | 95 | 增量数据迁移进度，单位为百分比。 |
| Status | String | Catched | 增量数据迁移状态，取值包括： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 Catched：无延迟。 |
| DestinationEn dpoint | Struct |  | 目标实例的连接信息。 |
| DatabaseNam e | String | dtstestdata | 目标实例中待迁移对象所属数据库的名称。 |
| EngineName | String | MySQL | 目标实例的数据库类型。 |
| IP | String | 172.16.88.*** | 目标实例的连接地址。 |
| InstanceId | String | rm- bp1zc3iyqe3qw**** | 目标实例ID。 |
| InstanceType | String | RDS | 目标实例类型。 |
| Port | String | 3306 | 目标实例的数据库服务端口。 |
| UserName | String | dtstest | 目标实例的数据库账号。 |
| oracleSID | String | testsid | Oracle数据库的SID信息。 说明当目标实例的数据库类型为Oracle时，才会返回该参数。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| MigrationJobCl ass | String | 2xlarge | 数据迁移实例的规格，返回值为：small、medium、large、xlarge或2x large。 |

数据传输

| MigrationJobId | String | dtsz2v12jfo309**** | 数据迁移实例ID。 |
|---|---|---|---|
| MigrationJobN ame | String | MySQL迁移 | 数据迁移实例名称。 |
| MigrationJobSt atus | String | Migrating | 迁移实例状态，返回值： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Migrating：迁移中。 Suspending：暂停中。 MigrationFailed：迁移失败。 Finished：迁移完成。 |
| MigrationMode | Struct |  | 迁移类型。 |
| dataInitializati on | Boolean | true | 是否迁移全量数据，取值： true：是。 false：否。 |
| dataSynchroni zation | Boolean | true | 是否迁移增量数据，取值： true：是。 false：否。 |
| structureInitial ization | Boolean | true | 是否执行结构迁移，取值： true：是。 false：否。 |
| MigrationObje ct | String | [{\"DBName\":\"dts testdata\",\"TableIn cludes\": [{\"TableName\":\" customer\"}]}] | 迁移对象。 |
| PayType | String | PostPaid | 迁移实例的付费类型，返回值固定为PostPaid（按量付费）。 |
| PrecheckStatu s | Struct |  | 预检查情况。 |
| Detail | Array of CheckItem |  | 各预检查项的执行情况。 |
| CheckItem |  |  |  |

数据传输

| CheckStatus | String | Success | 检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
|---|---|---|---|
| ErrorMessage | String | Original error: Access denied for user 'dtstest'@'100.104. ***.**' (using password: YES) | 预检查未通过的错误提示。 说明当CheckStatus参数返回值为Failed时，才会返回本参数。 |
| ItemName | String | CHECK CONN SRC _ _ | 预检查项目。 |
| RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 说明当CheckStatus参数返回值为Failed时，才会返回本参数。 |
| Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| Status | String | Success | 预检查状态，返回值： NotStarted：未启动。 Checking：预检查中。 Failed：预检查失败。 Finished：预检查完成。 |
| RequestId | String | A032E3B4-929B- 48E9-97B9- 37587CBF**** | 请求ID。 |
| SourceEndpoin t | Struct |  | 源实例的连接信息。 |
| DatabaseNam e | String | dtstestdatabase | 源实例中待迁移对象所属数据库的名称。 |
| EngineName | String | MySQL | 源实例的数据库类型。 |
| IP | String | 172.16.88.*** | 源实例的连接地址。 |
| InstanceId | String | rm- bp1i99e8l7913**** | 源实例ID。 |

数据传输

| InstanceType | String | RDS | 源实例类型。 RDS：阿里云RDS实例。 ECS：ECS上的自建数据库。 LocalInstance：有公网IP的自建数据库。 Express：通过专线/VPN网关/智能网关接入的自建数据库。 MongoDB：阿里云MongoDB实例。 POLARDB：阿里云PolarDB for MySQL集群（该值仅适用于中国站）。 |
|---|---|---|---|
| Port | String | 3306 | 源实例的数据库服务端口。 |
| UserName | String | dtstest | 源实例的数据库账号。 |
| oracleSID | String | dtstestdatabase | Oracle数据库的SID信息。 说明当源实例的数据库类型为Oracle时，才会返回该参数。 |
| StructureInitial izationStatus | Struct |  | 结构迁移执行状态。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | 结构迁移失败的错误提示。 |
| Percent | String | 100 | 结构迁移进度，单位为百分比。 |
| Progress | String | 1 | 已完成结构迁移的表的数量。 |
| Status | String | Finished | 结构迁移状态，取值包括： NotStarted：未启动。 Migrating：迁移中。 Failed：迁移失败。 Finished：迁移完成。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeMigrationJobStatus &MigrationJobId=dtsta7w132u12h****
```

`&<`公共请求参数> 数据传输正常返回示例 `XML` 格式

```xml
<DescribeMigrationJobStatusResponse>
      <TaskId>z2v12jfo309****</TaskId>
      <DataInitializationStatus>
            <Status>Finished</Status>
            <Progress>200001</Progress>
            <Percent>100</Percent>
      </DataInitializationStatus>
      <RequestId>A032E3B4-929B-48E9-97B9-37587CBF****</RequestId>
      <MigrationJobName>MySQL迁移</MigrationJobName>
      <PayType>PostPaid</PayType>
      <MigrationJobStatus>Migrating</MigrationJobStatus>
      <Success>true</Success>
      <MigrationMode>
            <structureInitialization>true</structureInitialization>
            <dataSynchronization>true</dataSynchronization>
            <dataInitialization>true</dataInitialization>
      </MigrationMode>
      <MigrationJobId>dtsz2v12jfo309****</MigrationJobId>
      <PrecheckStatus>
            <Status>Finished</Status>
            <Percent>100</Percent>
            <Detail>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_CONN_SRC</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_AUTH_SRC</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_CONN_DEST</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_AUTH_DEST</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_ON</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_MODE</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_ROW_IMAGE</ItemName>
                  </CheckItem>
                  <CheckItem>
```

数据传输

```xml
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SERVER_ID</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_EXIST</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_ENGINE</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_MYSQL_PASSOWRD_FORMAT</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SRC</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SQL_MODE</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SAME_USER</ItemName>
                  </CheckItem>
            </Detail>
      </PrecheckStatus>
      <DestinationEndpoint>
            <UserName>dtstest</UserName>
            <InstanceId>rm-bp1zc3iyqe3qw****</InstanceId>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </DestinationEndpoint>
      <MigrationJobClass>2xlarge</MigrationJobClass>
      <SourceEndpoint>
            <UserName>dtstest</UserName>
            <InstanceId>rm-bp1i99e8l7913****</InstanceId>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </SourceEndpoint>
      <DataSynchronizationStatus>
            <Status>Catched</Status>
            <Checkpoint>1612507847</Checkpoint>
            <Percent>95</Percent>
            <Delay>0</Delay>
      </DataSynchronizationStatus>
      <StructureInitializationStatus>
            <Status>Finished</Status>
            <Progress>1</Progress>
            <Percent>100</Percent>
      </StructureInitializationStatus>
</DescribeMigrationJobStatusResponse>
```

数据传输 `JSON` 格式

```json
{
 "TaskId": "z2v12jfo309****",
    "DataInitializationStatus": {
  "Status": "Finished",
  "Progress": "200001",
  "Percent": "100"
 },
 "RequestId": "A032E3B4-929B-48E9-97B9-37587CBF****",
 "MigrationJobName": "MySQL迁移",
 "PayType": "PostPaid",
 "MigrationJobStatus": "Migrating",
 "Success": true,
 "MigrationMode": {
  "structureInitialization": true,
  "dataSynchronization": true,
  "dataInitialization": true
 },
 "MigrationJobId": "dtsz2v12jfo309****",
 "PrecheckStatus": {
  "Status": "Finished",
  "Percent": "100",
  "Detail": {
   "CheckItem": [
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_CONN_SRC"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_AUTH_SRC"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_CONN_DEST"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_AUTH_DEST"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_BINLOG_ON"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_BINLOG_MODE"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_BINLOG_ROW_IMAGE"
    },
```

数据传输

```json
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_SERVER_ID"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_BINLOG_EXIST"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_ENGINE"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_MYSQL_PASSOWRD_FORMAT"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_SRC"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_SQL_MODE"
    },
    {
     "CheckStatus": "Success",
     "ItemName": "CHECK_SAME_USER"
    }
```

]

```json
  }
 },
 "DestinationEndpoint": {
  "UserName": "dtstest",
  "InstanceId": "rm-bp1zc3iyqe3qw****",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
 },
 "MigrationJobClass": "2xlarge",
 "SourceEndpoint": {
  "UserName": "dtstest",
  "InstanceId": "rm-bp1i99e8l7913****",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
 },
 "DataSynchronizationStatus": {
  "Status": "Catched",
  "Checkpoint": "1612507847",
  "Percent": "95",
  "Delay": "0"
 },
 "StructureInitializationStatus": {
  "Status": "Finished",
  "Progress": "1",
  "Percent": "100"
```

数据传输

```
 }
}
```

##### 结束迁移实例

调用StopMigrationJob接口结束处于迁移状态的数据迁移实例。 调用本接口结束数据迁移任务后，该任务的状态将转变为已完成，且无法通过调用

**说明**

StartMigrationJob接口重启该任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StopMigrationJo b | 系统规定参数，取值：StopMigrationJob。 |
| MigrationJobId | String | 是 | dtsb2c11sxpi3j* *** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | C306C198-7807- 409D-930A- D6CE6C32**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

数据传输

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=StopMigrationJob &MigrationJobId=dtsb2c11sxpi3j****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StopMigrationJobResponse>
      <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId>
      <Success>true</Success>
</StopMigrationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "C306C198-7807-409D-930A-D6CE6C32****",
 "Success": true
}
```

##### 释放迁移实例

调用DeleteMigrationJob释放数据迁移实例。 数据迁移实例一旦释放将无法找回。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteMigrationJ ob | 系统规定参数，取值：DeleteMigrationJob。 |
| MigrationJobId | String | 是 | dtsyiwe9b0gp2p **** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | F28A96B1-F897- 4246-833B- 310A3345**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DeleteMigrationJob &MigrationJobId=dtsyiwe9b0gp2p****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteMigrationJobResponse>
      <RequestId>F28A96B1-F897-4246-833B-310A3345****</RequestId>
      <Success>true</Success>
</DeleteMigrationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "F28A96B1-F897-4246-833B-310A3345****",
 "Success": true
}
```

#### 数据同步

##### 购买同步实例

调用CreateSynchronizationJob接口购买一个数据同步实例。 购买完成后，需要调用接口ConfigureSynchronizationJob配置同步任务，才能成功启动同步任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | CreateSynchroni zationJob | 系统规定参数，取值：CreateSynchronizationJob。 |
|---|---|---|---|---|
| DestRegion | String | 是 | cn-hangzhou | 数据同步的目标数据库所属地域的ID。 说明如果SourceRegion参数传入的地域为中国香港或海外地区，那么本参数须传入相同地域的ID。 |
| PayType | String | 是 | PostPaid | 付费类型。 PrePaid：预付费。 PostPaid：按量付费，默认付费类型。 |
| SourceRegion | String | 是 | cn-hangzhou | 数据同步的源数据库所属地域的ID。 |
| SynchronizationJ obClass | String | 是 | small | 数据同步链路的规格，取值：micro、small、medium、large 。 |
| RegionId | String | 否 | cn-hangzhou | 数据同步实例地域的ID， 与DestRegion参数保持一致。 |
| Topology | String | 否 | oneway | 同步拓扑，取值： oneway：单向同步 bidirectional：双向同步。 说明默认取值为oneway。 当SourceEndpoint.Inst anceType和Destinatio nEndpoint.InstanceTy pe参数取值为MySQL、PolarDB或Re dis时，本参数才可以传入bidirectional。 |
| Period | String | 否 | Year | 预付费实例的计费方式，取值： Year：包年。 Month：包月。 说明当付费类型为PrePaid（预付费）时，该参数才有效且必须传入。 |

数据传输

| UsedTime | Integer | 否 | 1 | 预付费实例购买时长。 当计费方式为Year（包年）时，取值范围为1~5。 当计费方式为Month（包月）时，取值范围为1~60。 说明当付费类型为PrePaid（预付费）时，该参数才有效且必须传入。 |
|---|---|---|---|---|
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| SourceEndpoint.I nstanceType | String | 否 | MySQL | 源库的实例类型，取值： MySQL：MySQL数据库（包括RDS MySQL和自建MySQL）。 PolarDB：PolarDB集群（仅支持 MySQL或兼容Oracle语法的引擎）。 Redis：Redis数据库。 DRDS：云原生分布式数据库PolarDB- X 1.0。 说明默认取值为MySQL。 |
| DestinationEndp oint.InstanceTyp e | String | 否 | MySQL | 目标库的实例类型，取值： MySQL：MySQL数据库（包括RDS MySQL和自建MySQL）。 PolarDB：PolarDB集群（仅支持 MySQL或兼容Oracle语法的引擎）。 Redis：Redis数据库。 MaxCompute：MaxCompute实例。 说明默认取值为MySQL。 |
| networkType | String | 否 | Intranet | 数据传输网络类型，固定取值为Intranet（专线）。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

数据传输

| DBInstanceCoun t | Integer | 否 | 3 | 当SourceEndpoint.InstanceType 传入DRDS时，您需要传入本参数来指定源PolarDB-X下挂的私有定制RDS实例数量，默认值为1。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 9056C8B0-5799- 493A-9655- 70F607B8**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |
| Synchronizatio nJobId | String | dtshvj11k25255*** * | 数据同步实例ID。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=CreateSynchronizationJob &SourceRegion=cn-hangzhou &DestRegion=cn-hangzhou &SynchronizationJobClass=small &PayType=PostPaid
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateSynchronizationJobResponse>
      <SynchronizationJobId>dtshvj11k25255****</SynchronizationJobId>
      <RequestId>9056C8B0-5799-493A-9655-70F607B8****</RequestId>
      <Success>true</Success>
</CreateSynchronizationJobResponse>
```

`JSON` 格式数据传输

```json
{
 "SynchronizationJobId": "dtshvj11k25255****",
 "RequestId": "9056C8B0-5799-493A-9655-70F607B8****",
 "Success": true
}
```

##### 配置同步实例

调用ConfigureSynchronizationJob接口配置数据同步实例。 调用本接口前，已调用CreateSynchronizationJob接口创建了数据同步实例。

**说明**

本接口调用成功后，数据同步实例会自动启动并执行预检查，您无需调用 StartSynchronizationJob接口来启动。 如果数据同步实例没有被成功启动，可能是预检查失败，您可以调用 DescribeSynchronizationJobStatus接口查询数据同步实例的状态，获取预检查失败的错误提示并进行参数调整。调整完成后，您可以调用StartSynchronizationJob接口来重启数据同步实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ConfigureSynchr onizationJob | 系统规定参数，取值：ConfigureSynchronizationJob 。 |
| DataInitialization | Boolean | 是 | true | 是否执行全量数据初始化，取值： true：是。 false：否。 说明默认取值：true。 |
| StructureInitializ ation | Boolean | 是 | true | 是否执行结构初始化，取值： true：是。 false：否。 说明默认取值：true。 |
| SynchronizationJ obId | String | 是 | dtsz4ao1dor13d **** | 数据同步实例ID。 |
| Synchronization Objects | String | 是 | [{"DBName":"dt stestdata","Tabl eIncludes": [{"TableName":" customer"}]}] | 同步对象，格式为JSON串且支持一定的正则表达式。 |

数据传输

| RegionId | String | 否 | cn-hangzhou | 数据同步实例所在地域的ID。 |
|---|---|---|---|---|
| SynchronizationJ obName | String | 否 | MySQL同步 | 同步任务名称。 说明建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 只有当数据同步实例的同步拓扑为双向同步时，本参数传入Reverse才会生效。 |
| SourceEndpoint.I nstanceId | String | 否 | rm- bp1i99e8l7913* *** | 源实例ID。 |
| SourceEndpoint.I nstanceType | String | 否 | RDS | 源实例类型，取值为： RDS：阿里云RDS实例。 Redis：阿里云Redis实例。 PolarDB：阿里云PolarDB集群（仅支持MySQL或兼容Oracle语法的引擎）。 ECS：ECS上的自建数据库。 Express：通过专线接入的自建数据库。 dg：通过数据库网关DG接入的自建数据库。 cen：通过云企业网CEN接入的自建数据库。 说明默认取值为RDS。 |
| SourceEndpoint.I P | String | 否 | 172.16.88.*** | 源库的IP地址。 说明当SourceEndpoint.InstanceTy pe取值为ECS、Express、dg或cen时， 本参数才可用且必须传入。 |

数据传输

| SourceEndpoint. Port | String | 否 | 3306 | 源库的数据库服务端口。 说明当SourceEndpoint.InstanceTy pe取值为ECS、Express、dg或cen时， 本参数才可用且必须传入。 |
|---|---|---|---|---|
| SourceEndpoint. UserName | String | 否 | dtstestaccount | 源库的数据库账号。 说明当SourceEndpoint.Inst anceType取值为ECS、Express、dg或c en时，本参数才可用且必须传入。 当SourceEndpoint.Inst anceType取值为Redis时，本参数无需传入。 同步不同的数据库所需的权限有所差异。 |
| SourceEndpoint. Password | String | 否 | Test123456 | 源库数据库账号密码。 说明当SourceEndpoint.InstanceTy pe取值为ECS、Express、dg或cen时， 本参数必须传入。 |
| DestinationEndp oint.InstanceId | String | 否 | rm- bp1r46452ai50* *** | 同步目标实例的实例ID 说明当DestinationEndpoint.Instan ceType取值为MaxCompute或DataHub时， 本参数传入MaxCompute实例或 DataHub的Project名称。 当目标实例为阿里云分析型数据库MySQL 版时，传入分析型数据库MySQL版的集群 ID。 |

数据传输

| DestinationEndp oint.InstanceTyp e | String | 否 | RDS | 目标实例类型，取值为： Redis：阿里云Redis实例。 RDS：阿里云RDS实例。 PolarDB：阿里云PolarDB集群（仅支持MySQL或兼容Oracle语法的引擎）。 ECS：ECS上的自建数据库。 Express：通过专线接入的本地数据库。 DataHub：阿里云DataHub实例。 MaxCompute：阿里云 MaxCompute实例。 AnalyticDB：云原生数据仓库 AnalyticDB MySQL 3.0和2.0版本。 Greenplum：云原生数据仓库ADB PostgreSQL版（原分析型数据库 PostgreSQL版）。 说明默认取值为RDS。 |
|---|---|---|---|---|
| DestinationEndp oint.IP | String | 否 | 172.16.88.*** | 目标库的IP地址。 说明当DestinationEndpoint.Instan ceType取值为Express、dg或cen时，本参数必须传入本参数才可用且必须传入。 |
| DestinationEndp oint.Port | String | 否 | 3306 | 目标库的数据库服务端口。 说明当DestinationEndpoint.Instan ceType取值为ECS、Express、dg或cen时， 本参数才可用且必须传入。 |

数据传输

| DestinationEndp oint.UserName | String | 否 | dtstestaccount | 目标库的数据库账号。 说明同步不同的数据库所需的权限有所差异。 当DestinationEndpoint .InstanceType取值为ECS、Express、dg或c en时，本参数必须传入。 当DestinationEndpoint .InstanceType取值为 RDS且数据库版本为MySQL 5.5或MySQL 5.6，无需传入本参数和DestinationEndpoint .Password参数。 当DestinationEndpoint .InstanceType取值为Redis时，无需传入本参数。 |
|---|---|---|---|---|
| DestinationEndp oint.Password | String | 否 | Test654321 | 目标库数据库账号密码。 说明当DestinationEndpoint .InstanceType取值为ECS、Express、dg或c en时，本参数必须传入。 |
| SourceEndpoint. OwnerID | String | 否 | 140692647406* *** | 源RDS实例所属的阿里云账号ID。 说明传入本参数即代表执行跨阿里云账号的数据同步，同时您还需要传入SourceEndpoint.Role参数。 |
| SourceEndpoint. Role | String | 否 | ram-for-dts | 源实例所属云账号配置的角色名称。 说明执行跨阿里云账号的数据同步时须传入本参数。 |
| PartitionKey.Mod ifyTime Year _ | Boolean | 否 | true | 设置增量日志表是否包含以增量更新时间对应年份信息定义的分区，取值：true或false。 说明当DestinationEndpoint.Instan ceType参数取值为Maxcompute时，本参数才可用。 |

数据传输

| PartitionKey.Mod ifyTime Month _ | Boolean | 否 | true | 设置增量日志表是否包含以增量更新时间对应月份信息定义的分区，取值：true或false。 说明当DestinationEndpoint.Instan ceType参数取值为Maxcompute时，本参数才可用。 |
|---|---|---|---|---|
| PartitionKey.Mod ifyTime Day _ | Boolean | 否 | true | 设置增量日志表是否包含以增量更新时间对应日期信息定义的分区，取值：true或false。 说明当DestinationEndpoint.Instan ceType参数取值为Maxcompute时，本参数才可用。 |
| PartitionKey.Mod ifyTime Hour _ | Boolean | 否 | true | 设置增量日志表是否包含以增量更新时间对应小时信息定义的分区，取值：true或false。 说明当DestinationEndpoint.Instan ceType参数取值为Maxcompute时，本参数才可用。 |
| PartitionKey.Mod ifyTime Minute _ | Boolean | 否 | true | 设置增量日志表是否包含以增量更新时间对应分钟信息定义的分区，取值：true或false。 说明当DestinationEndpoint.Instan ceType参数取值为Maxcompute时，本参数才可用。 |
| MigrationReserv ed | String | 否 | { "autoStartModul esAfterConfig": "none", "targetTableMod e": 2 } | DTS预留参数，格式为JSON串，您可以传入本参数实现特殊需求（例如是否自动启动预检查）。 说明如在Redis企业版实例间的数据同步可使用该参数。 |
| Checkpoint | String | 否 | 1610540493 | 同步位点。 |

数据传输

| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |
|---|---|---|---|---|
| SourceEndpoint. DatabaseName | String | 否 | dtstestdata | 源实例中的同步对象所属数据库名称。 |
| DestinationEndp oint.DataBaseNa me | String | 否 | dtstestdata | 目标实例中的同步对象所属数据库名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 2690E467-7773- 43BC-A009- 370EE2E7**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSynchronizationJob &DataInitialization=true &StructureInitialization=true &SynchronizationJobId=dtsz4ao1dor13d**** &SynchronizationObjects=[{"DBName":"dtstestdata","TableIncludes": [{"TableName":"customer"}]}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ConfigureSynchronizationJobResponse>
      <RequestId>2690E467-7773-43BC-A009-370EE2E7****</RequestId>
      <Success>true</Success>
</ConfigureSynchronizationJobResponse>
```

`JSON` 格式数据传输

```json
{
 "RequestId": "2690E467-7773-43BC-A009-370EE2E7****",
 "Success": true
}
```

##### 启动同步实例

调用StartSynchronizationJob接口启动数据同步实例。 调用本接口时，数据同步作业须处于未启动、同步失败、暂停状态。调用成功后，处于未启动状态的任务需要进行预检查。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartSynchroniz ationJob | 系统规定参数，取值：StartSynchronizationJob。 |
| SynchronizationJ obId | String | 是 | dtsf19100l2186* *** | 数据同步实例ID，可以通过调用DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 当数据同步实例的拓扑类型为双向时，才可以传入Reverse以启动反向同步链路。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |

数据传输

| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
|---|---|---|---|
| RequestId | String | FDC111B1-ACBF- 457D-9656- 247FDEE9**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=StartSynchronizationJob &SynchronizationJobId=dtsf19100l2186****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StartSynchronizationJobresponse>
      <RequestId>FDC111B1-ACBF-457D-9656-247FDEE9****</RequestId>
      <Success>true</Success>
</StartSynchronizationJobresponse>
```

`JSON` 格式

```json
{
 "RequestId": "FDC111B1-ACBF-457D-9656-247FDEE9****",
 "Success": true
}
```

##### 暂停同步实例

调用SuspendSynchronizationJob接口暂停处于同步中的数据同步实例。

**说明**

调用本接口时，同步作业须处于同步中状态。 暂停同步作业不能超过6个小时，否则将无法被再次启动。 按量付费类型的同步作业即使处于暂停状态，DTS依然会收取费用。这是由于DTS只是暂停向目标库写入数据，仍然会继续拉取源库的日志以便重启任务后快速恢复运行，因此还是会占用源数据库的带宽等资源。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | SuspendSynchro nizationJob | 系统规定参数，取值：SuspendSynchronizationJob。 |
|---|---|---|---|---|
| SynchronizationJ obId | String | 是 | dtsmr1q4mc215 2**** | 数据同步实例ID，可以通过调用DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 当数据同步实例的拓扑为双向时，才可以传入Reverse以暂停反向同步链路。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | C306C198-7807- 409D-930A- D6CE6C32**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=SuspendSynchronizationJob &SynchronizationJobId=dtsmr1q4mc2152****
```

`&<`公共请求参数> 数据传输正常返回示例 `XML` 格式

```xml
<SuspendSynchronizationJobResponse>
      <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId>
      <Success>true</Success>
</SuspendSynchronizationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "C306C198-7807-409D-930A-D6CE6C32****",
 "Success": true
}
```

##### 清空同步实例配置

调用ResetSynchronizationJob清空数据同步实例配置。 清空数据同步任务配置后，原先的同步任务就会被释放，您需要调用接

**说明**

口**ConfigureSynchronizationJob**重新配置同步任务，才能成功启动该任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ResetSynchroniz ationJob | 系统规定参数，取值：ResetSynchronizationJob。 |
| SynchronizationJ obId | String | 是 | dtsm761239l27 m**** | 数据同步实例ID，可以通过调用DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 当数据同步实例的拓扑为双向时，才可以传入Reverse以清空反向同步链路。 |

数据传输

| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | FDC111B1-ACBF- 457D-9656- 247FDEE9**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ResetSynchronizationJob &SynchronizationJobId=dtsm761239l27m****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ResetSynchronizationJobResponse>
      <RequestId>FDC111B1-ACBF-457D-9656-247FDEE9****</RequestId>
      <Success>true</Success>
</ResetSynchronizationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "FDC111B1-ACBF-457D-9656-247FDEE9****",
 "Success": true
}
```

##### 修改同步对象

调用ModifySynchronizationObject接口修改数据同步实例中的同步对象。 调用本接口时，数据同步实例需处于未启动或同步中状态。

**说明**

数据传输

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySynchroni zationObject | 系统规定参数，取值：ModifySynchronizationObject 。 |
| SynchronizationJ obId | String | 是 | dtskfq1149w254 **** | 数据同步实例ID，可以通过调用 DescribeSynchronizationJobs接口查询。 |
| Synchronization Objects | String | 是 | [{"DBName": "dtstestdata"}] | 修改后的同步对象，格式为JSON串且支持一定的正则表达式。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| Synchronization Direction | String | 否 | Forward | 指定同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 只有当数据同步实例的同步拓扑为双向同步时，才需要传入本参数。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 902DDCDE-C755- 4458-85DA- DF9A323C**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

数据传输

| TaskId | String | tl911uvi25z**** | 任务ID，您可以根据此参数调用 DescribeSynchronizationObjectModifyStat us接口查询同步对象变更的状态及进度。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifySynchronizationObject &SynchronizationJobId=dtskfq1149w254**** &SynchronizationObjects=[{"DBName": "dtstestdata"}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifySynchronizationObjectResponse>
      <TaskId>tl911uvi25z****</TaskId>
      <RequestId>902DDCDE-C755-4458-85DA-DF9A323C****</RequestId>
      <Success>true</Success>
</ModifySynchronizationObjectResponse>
```

`JSON` 格式

```json
{
 "TaskId": "tl911uvi25z****",
 "RequestId": "902DDCDE-C755-4458-85DA-DF9A323C****",
 "Success": true
}
```

##### 查询同步对象修改情况

调用DescribeSynchronizationObjectModifyStatus接口修改同步对象任务的执行情况。 调用本接口前，您需要成功调用ModifySynchronizationObject接口并获取到TaskId信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSynchro nizationObjectM odifyStatus | 系统规定参数，取值：DescribeSynchronizationObje ctModifyStatus。 |
| TaskId | String | 是 | k71r16fj13g**** | 任务ID，调用 ModifySynchronizationObject接口修改同步对象时会返回该值。 |
| RegionId | String | 否 | cn-hangzhou | 数据同步实例所在地域的ID。 |

数据传输

| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
|---|---|---|---|---|
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DataInitializati onStatus | Struct |  | 全量数据初始化状态。 |
| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据初始化失败的错误提示。 |
| Percent | String | 100 | 全量数据初始化进度，单位为百分比。 |
| Progress | String | 39754 | 已完成全量数据初始化的记录数。 |
| Status | String | Finished | 全量数据初始化状态，取值包括： NotStarted：未启动。 Migrating ：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
| DataSynchroni zationStatus | Struct |  | 增量数据同步状态。 说明该参数合集及包含的返回参数即将下线。 |
| Delay | String | 0 | 增量数据同步延迟，单位为秒。 |
| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据同步失败的错误提示。 |
| Percent | String | 100 | 增量数据同步进度，单位为百分比。 |
| Status | String | Migrating | 增量数据同步状态，取值包括： NotStarted：未启动。 Migrating：同步中。 Failed：同步失败。 Finished：同步完成。 |

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectE xception:Connectio n timed out (Connection timed out)] About more information in [https://yq.aliyun.c om/articles/499178 ]. | 修改同步对象任务失败的错误提示。 |
| PrecheckStatu s | Struct |  | 预检查状态。 |
| Detail | Array of CheckItem |  | 各预检查项的执行情况。 |
| CheckStatus | String | Success | 检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
| ErrorMessage | String | Original error: Access denied for user 'dtstest'@'100.104. xxx.xx' (using password: YES) | 预检查未通过的错误提示。 说明当CheckStatus参数返回值为Failed时，才会返回本参数。 |

数据传输

| ItemName | String | CHECK CONN SRC _ _ | 预检查项目。 |
|---|---|---|---|
| RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 说明当CheckStatus参数返回值为Failed时，才会返回本参数。 |
| Percent | String | 100 | 预检查进度，单位为百分比。 |
| Status | String | Finished | 预检查状态。 |
| RequestId | String | B38C644B-4395- 4F6F-86E3- 592F26BE**** | 请求ID。 |
| Status | String | Finished | 同步对象变更状态，取值： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Migrating：同步中。 Failed：同步失败。 Finished：同步完成。 |
| StructureInitial izationStatus | Struct |  | 结构初始化状态。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: Table 'customer' already exists | 结构初始化失败的错误提示。 |
| Percent | String | 100 | 结构初始化进度，单位为百分比。 |
| Progress | String | 1 | 已完成结构初始化的表的数量。 |
| Status | String | Finished | 结构初始化状态，取值包括： NotStarted：未启动。 Migrating ：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例数据传输

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationObjectModifyStatus &TaskId=k71r16fj13g****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Status>Migrating</Status> <PrecheckStatus>
    <Status>Finished</Status>
    <Percent>100</Percent>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_CONN_SRC</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_CONN_DEST</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_AUTH_SRC</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_AUTH_DEST</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_BINLOG_ON</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_BINLOG_MODE</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_BINLOG_ROW_IMAGE</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SERVER_ID</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_BINLOG_EXIST</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_ENGINE</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
```

数据传输

```xml
        <ItemName>CHECK_MYSQL_PASSOWRD_FORMAT</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SRC</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SAME_OBJ</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SQL_MODE</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SAME_USER</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_TOPOLOGY</ItemName>
    </Detail>
</PrecheckStatus> <DataInitializationStatus>
    <Status>Finished</Status>
    <Progress>0</Progress>
    <Percent>100</Percent>
</DataInitializationStatus> <RequestId>0C3D6348-79D8-43F8-9788-60C30CCC****</RequestId> <Success>true</Success> <StructureInitializationStatus>
    <Status>Finished</Status>
    <Progress>0</Progress>
    <Percent>100</Percent>
</StructureInitializationStatus>
```

`JSON` 格式

```json
{
 "Status": "Migrating",
 "PrecheckStatus": {
  "Status": "Finished",
  "Percent": "100",
  "Detail": [
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_CONN_SRC"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_CONN_DEST"
   },
   {
    "CheckStatus": "Success",
```

数据传输

```json
CecStatus: Success,
    "ItemName": "CHECK_AUTH_SRC"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_AUTH_DEST"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_ON"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_MODE"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_ROW_IMAGE"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SERVER_ID"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_EXIST"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_ENGINE"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_MYSQL_PASSOWRD_FORMAT"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SRC"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SAME_OBJ"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SQL_MODE"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SAME_USER"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_TOPOLOGY"
   }
```

数据传输 ]

```json
 },
 "DataInitializationStatus": {
  "Status": "Finished",
  "Progress": "0",
  "Percent": "100"
 },
 "RequestId": "0C3D6348-79D8-43F8-9788-60C30CCC****",
 "Success": true,
 "StructureInitializationStatus": {
  "Status": "Finished",
  "Progress": "0",
  "Percent": "100"
 }
}
```

##### 修改数据库连接信息

当数据同步作业的源数据库或目标数据库发生了主备切换时，您可以调用 SwitchSynchronizationEndpoint接口，将主备切换后新数据库的连接信息传给DTS，DTS将从断点处重新启动数据同步任务。 如发生主备切换的源或目标实例是公网、ECS或专线接入的自建MySQL，您需调用本接口，来更新主备切换后的新数据库的连接信息。 如发生主备切换的源或目标实例是阿里云数据库实例（例如RDS、MongoDB等），DTS会自动更新连接信息，您无需手动调用本接口。

**说明**

如果数据同步实例的同步拓扑为双向，且源或目标实例发生主备切换，则需要调用两次本接口，更新主备切换后新数据库的连接信息。 比如当正向的目标数据库发生主备切换时，您需要调用两次本接口。第一次调用时，**SynchronizationDirection**为**Forward**，**Endpoint.Type** 为**Destination**，并传入新数据库的连接信息。第二次调用时，**SynchronizationDirection**为**Reverse**，**Endpoint.Type** 为**Source**，并传入新数据库的连接信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SwitchSynchroni zationEndpoint | 系统规定参数，取值：SwitchSynchronizationEndpoi nt。 |

数据传输

| Endpoint.Instanc eId | String | 是 | i- bp11haem1kpkh oup**** | ECS或专有网络的实例ID。 说明当Endpoint.InstanceTy pe取值为ECS时，本参数需传入ECS实例的ID。 当Endpoint.InstanceTy pe取值为Express时，本参数需传入专有网络ID。 |
|---|---|---|---|---|
| Endpoint.Instanc eType | String | 是 | ECS | 新数据库所属的实例类型，取值： LocalInstance：有公网IP的自建数据库； ECS：ECS上的自建数据库。 Express：通过专线接入的自建数据库。 |
| Endpoint.Port | String | 是 | 3306 | 新的数据库服务端口。 |
| Endpoint.Type | String | 是 | Destination | 待调整连接信息的实例，取值： Source：源实例。 Destination：目标实例。 |
| SynchronizationJ obId | String | 是 | dtsexjk1alb116* *** | 数据同步实例ID，可以通过调用 DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 只有当数据同步实例的同步拓扑为双向同步时，本参数传入Reverse才会生效。 |
| Endpoint.IP | String | 否 | 172.15.185.*** | 新数据库的IP地址。 说明当Endpoint.InstanceType取值为Express时，本参数才可用且必须传入。 |

数据传输

| SourceEndpoint. OwnerID | String | 否 | 14069264**** | 当源实例与目标实例所属阿里云账号不同时，您需要传入该参数指定源实例的所属阿里云账号的ID。 |
|---|---|---|---|---|
| SourceEndpoint. Role | String | 否 | ram-for-dts | 当源实例与目标实例所属阿里云账号不同时，需传入该参数，来指定源实例的授权角色，以允许目标实例阿里云账号访问源实例的实例信息。 |
| AccountId | String | 否 | 12323344**** | 阿里云账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 3232F84C-C961- 4811-B014- 4EA7A27C**** | 请求ID。 |
| Success | String | true | 是否成功。 |
| TaskId | String | 11**** | 任务ID，您可以根据此返回值调用 DescribeEndpointSwitchStatus接口查询该任务的执行状态。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=SwitchSynchronizationEndpoint &Endpoint.InstanceId=i-bp11haem1kpkhoup**** &Endpoint.InstanceType=ECS &Endpoint.Port=3306 &Endpoint.Type=Destination &SynchronizationJobId=dtsexjk1alb116****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<SwitchSynchronizationEndpointResponse>
      <RequestId>3232F84C-C961-4811-B014-4EA7A27C****</RequestId>
      <Success>true</Success>
      <TaskId>11****</TaskId>
</SwitchSynchronizationEndpointResponse>
```

`JSON` 格式

```json
{
    "SwitchSynchronizationEndpointResponse": {
        "RequestId": "3232F84C-C961-4811-B014-4EA7A27C****",
        "Success": true,
        "TaskId": "11****"
    }
}
```

##### 查询数据库连接信息的修改状态

调用DescribeEndpointSwitchStatus接口查询修改数据库连接信息任务的状态。 在调用本接口前，您需要调用SwitchSynchronizationEndpoint接口修改数据库连接信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeEndpoin tSwitchStatus | 系统规定参数，取值：DescribeEndpointSwitchStatu s。 |
| TaskId | String | 是 | 11**** | 任务ID，成功调用 SwitchSynchronizationEndpoint接口后会返回该值。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| ErrorMessage | String | 400 | 本参数已下线。 |
| RequestId | String | 0DD6B201-604B- 4CAB-B6A8- 4B2953B5**** | 请求ID。 |
| Status | String | Finished | 任务执行状态，返回为： NotStarted：未启动。 Initializing：初始化中。 Switching：切换中。 Failed：执行失败。 Finished：执行成功。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeEndpointSwitchStatus &TaskId=11****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<SwitchSynchronizationEndpointResponse>
      <RequestId>0DD6B201-604B-4CAB-B6A8-4B2953B5****</RequestId>
      <Status>Finished</Status>
      <Success>true</Success>
</SwitchSynchronizationEndpointResponse>
```

`JSON` 格式

```json
{
    "SwitchSynchronizationEndpointResponse": {
        "RequestId": "0DD6B201-604B-4CAB-B6A8-4B2953B5****",
        "Status": "Finished",
        "Success": true
    }
}
```

数据传输

##### 配置全镜像匹配开关

调用ConfigureSynchronizationJobReplicatorCompare，配置一个同步实例的全镜像匹配开关。 使用DTS进行数据同步时，除DTS外还有其他数据写入目标实例，可能会导致同步对象在源和目标实例数据不一致，如需确保数据一致性，您需要开启全镜像匹配开关。 配置成功后，您可以调用DescribeSynchronizationJobReplicatorCompare查询一个同步实例的全镜像匹配开关情况。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ConfigureSynchr onizationJobRepl icatorCompare | 系统规定参数，取值：ConfigureSynchronizationJob ReplicatorCompare。 |
| SynchronizationJ obId | String | 是 | dtsexjk1alb116* *** | 数据同步实例ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| Synchronization Direction | String | 否 | Forward | 指定同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 只有当数据同步实例的同步拓扑为双向同步时，才需要传入本参数。 |
| Synchronization ReplicatorComp areEnable | Boolean | 否 | true | 全镜像开关，取值： true：打开。 false：关闭。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 86A8FF0F-FA92- 449D-B559- 05CFF9F9**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSynchronizationJobReplicatorCompare &SynchronizationJobId=dtsexjk1alb116****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ConfigureSynchronizationJobReplicatorCompareResponse>
      <RequestId>86A8FF0F-FA92-449D-B559-05CFF9F9****</RequestId>
      <Success>true</Success>
</ConfigureSynchronizationJobReplicatorCompareResponse>
```

`JSON` 格式

```json
{
 "RequestId": "86A8FF0F-FA92-449D-B559-05CFF9F9****",
 "Success": true
}
```

##### 查询全镜像匹配开关状态

调用DescribeSynchronizationJobReplicatorCompare，查询一个同步实例的全镜像匹配开关状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSynchro nizationJobRepli catorCompare | 系统规定参数，取值：DescribeSynchronizationJobR eplicatorCompare。 |

数据传输

| SynchronizationJ obId | String | 是 | dtsexjk1alb116* *** | 数据同步实例ID，可以通过调用 DescribeSynchronizationJobs接口查询。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| Synchronization Direction | String | 否 | Forward | 指定同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 只有当数据同步实例的同步拓扑为双向同步时，才需要传入本参数。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | E6EB407F-C59F- 4682-A682- A00FA6A2**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

数据传输

| Synchronizatio nReplicatorCo mpareEnable | Boolean | true | 全镜像开关，返回值： true：打开。 false：关闭。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobReplicatorCompare &SynchronizationJobId=dtsexjk1alb116****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSynchronizationJobReplicatorCompareResponse>
      <RequestId>E6EB407F-C59F-4682-A682-A00FA6A2****</RequestId>
<SynchronizationReplicatorCompareEnable>true</SynchronizationReplicatorCompareEnable>
      <Success>true</Success>
</DescribeSynchronizationJobReplicatorCompareResponse>
```

`JSON` 格式

```json
{
 "RequestId": "E6EB407F-C59F-4682-A682-A00FA6A2****",
 "SynchronizationReplicatorCompareEnable": true,
 "Success": true
}
```

##### 查询数据同步实例列表及各实例详情

通过DescribeSynchronizationJobs查询数据同步实例列表和各同步实例的详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSynchro nizationJobs | 系统规定参数，取值：DescribeSynchronizationJobs 。 |
| RegionId | String | 否 | cn-hangzhou | 数据同步实例所在地域的ID。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30、50、100，默认值为30。 |

数据传输

| PageNum | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
|---|---|---|---|---|
| SynchronizationJ obName | String | 否 | MySQL同步 | 同步实例名称。 说明支持模糊查询。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 当前页可展示的最大记录数。 |
| RequestId | String | 92E1E99D-5224- 4AD3-8C94- 23A3516B**** | 请求ID。 |
| Synchronizatio nInstances | Array of Synchronizatio nInstance |  | 数据同步实例列表和各同步实例的详情。 |
| CreateTime | String | 2021-06-28 17:34:53.0 | 同步任务创建时间，yyyy-MM-dd HH:mm:ss.0（北京时间）。 |
| DataInitializati on | String | true | 是否执行全量数据初始化，取值： true：是。 false：否。 |
| DataInitializati onStatus | Struct |  | 全量数据初始化状态。 |
| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据初始化失败的错误提示。 |
| Percent | String | 100 | 全量数据初始化进度，单位为百分比。 |

数据传输

| Progress | String | 200001 | 已完成全量数据初始化的记录数。 |
|---|---|---|---|
| Status | String | Finished | 全量数据初始化状态，取值包括： NotStarted：未初始化。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
| DataSynchroni zationStatus | Struct |  | 增量数据同步状态。 说明本参数集合及所包含的参数已下线。 |
| Delay | String | 0 | 增量数据同步延迟。 说明本参数已下线。 |
| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据同步失败的错误提示。 说明本参数已下线。 |
| Percent | String | 100 | 增量数据同步进度。 说明本参数已下线。 |
| Status | String | Finished | 增量数据同步状态。 说明本参数已下线。 |
| Delay | String | 0 | 同步延迟，单位为秒。 |
| DestinationEn dpoint | Struct |  | 目标实例的连接信息。 |
| EngineName | String | MySQL | 目标实例的数据库类型。 |
| IP | String | 172.16.88.*** | 目标实例的连接地址。 |
| InstanceId | String | rm- bp162d4tp0500*** * | 目标实例ID。 |
| InstanceType | String | RDS | 目标实例类型。 |

数据传输

| Port | String | 3306 | 目标实例的数据库服务端口。 |
|---|---|---|---|
| UserName | String | dtstest | 目标实例的数据库账号。 |
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectE xception:Connectio n timed out (Connection timed out)] About more information in [https://yq.aliyun.c om/articles/499178 ]. | 数据同步失败的错误提示。 |
| ExpireTime | String | 2021-07- 07T16:00:00Z | 同步实例的到期时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明当PayType参数的返回值为PrePaid时才会返回本参数。 |
| PayType | String | PrePaid | 同步实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| Performance | Struct |  | 同步链路概况信息。 |
| FLOW | String | 1 | 每秒同步数据的流量，单位为MB/s。 |

数据传输

| RPS | String | 100 | 每秒同步SQL语句的次数，包括BEGIN、 COMMIT 、DML语句（INSERT、DELETE、 UPDATE）及DDL语句。 |
|---|---|---|---|
| PrecheckStatu s | Struct |  | 预检查状态。 |
| Detail | Array of CheckItem |  | 各预检查项的执行情况。 |
| CheckStatus | String | Success | 检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
| ErrorMessage | String | Original error: Access denied for user 'dtstest'@'100.104. ***.**' (using password: YES) | 预检查未通过的错误提示。 说明当CheckStatus参数返回值为Failed时，才会返回本参数。 |
| ItemName | String | CHECK CONN SRC _ _ | 预检查项目。 |
| RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 说明当CheckStatus参数返回值为Failed时，才会返回本参数。 |
| Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| Status | String | Success | 预检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
| SourceEndpoin t | Struct |  | 源实例连接信息。 |
| EngineName | String | MySQL | 源实例的数据库类型。 |
| IP | String | 172.16.88.*** | 源实例的连接地址。 |
| InstanceId | String | rm- bp1i99e8l7913**** | 源实例ID。 |
| InstanceType | String | RDS | 源实例类型。 |

数据传输

| Port | String | 3306 | 源实例的数据库服务端口。 |
|---|---|---|---|
| UserName | String | dtstest | 源实例的数据库账号。 |
| Status | String | synchronizing | 同步实例的状态，返回值： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Initializating ：同步初始化。 InitializeFailed：同步初始化失败。 Synchronizing ：同步中。 Failed：同步失败。 Suspending：暂停。 Modifying：同步对象变更中。 Finished：完成。 |
| StructureInitial ization | String | true | 是否执行结构初始化，返回值： true：是 false：否 |
| StructureInitial izationStatus | Struct |  | 结构初始化状态。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | 结构初始化失败的错误提示。 |
| Percent | String | 100 | 结构初始化进度，单位为百分比。 |
| Progress | String | 1 | 已完成结构初始化的表的数量。 |
| Status | String | Finished | 结构初始化状态，取值包括： NotStarted：未启动。 Migrating ：初始化中。 Failed ：初始化失败。 Finished：初始化完成。 |
| Synchronizatio nDirection | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 |
| Synchronizatio nJobClass | String | large | 同步链路规格。 |

数据传输

| Synchronizatio nJobId | String | dtsexjk1alb116**** | 数据同步实例ID。 |
|---|---|---|---|
| Synchronizatio nJobName | String | MySQL同步 | 同步实例名称。 |
| Synchronizatio nObjects | Array of Synchronizatio nObject |  | 同步对象。 |
| NewSchemaN ame | String | newdtstestdatabas e | 待同步的库在目标数据库中映射的名称。 |
| SchemaName | String | dtstestdatabase | 待同步的库名。 |
| TableExcludes | Array of TableExclude |  | 待同步库中排除的表，这些表将不会被同步。 |
| TableName | String | order | 排除的表的名称。 |
| TableIncludes | Array of TableInclude |  | 待同步的表。 |
| TableName | String | customer | 待同步表名。 |
| TotalRecordCo unt | Long | 100 | 阿里云主账号下所有符合条件的数据同步实例数量。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobs &Tag.1.Key=testkey1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSynchronizationJobsResponse>
      <TotalRecordCount>100</TotalRecordCount>
      <SynchronizationInstances>
            <Status>synchronizing</Status>
            <SynchronizationObjects>
                  <SchemaName>dtstestdatabase</SchemaName>
                  <NewSchemaName>newdtstestdatabase</NewSchemaName>
            </SynchronizationObjects>
            <DataInitializationStatus>
                  <Status>Finished</Status>
                  <Progress>200001</Progress>
                  <Percent>100</Percent>
            </DataInitializationStatus>
<SynchronizationJobName>MySQL同步</SynchronizationJobName>
```

数据传输

```xml
            <SynchronizationJobName>MySQL同步</SynchronizationJobName>
            <InstanceCreateTime>2021-06-28T09:36:32Z</InstanceCreateTime>
            <CreateTime>2021-06-28 17:34:53.0</CreateTime>
            <JobCreateTime>2021-06-28T09:34:53Z</JobCreateTime>
            <PayType>PostPaid</PayType>
            <Delay>0</Delay>
            <PrecheckStatus>
                  <Status>Finished</Status>
                  <Percent>100</Percent>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_CONN_SRC</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_AUTH_SRC</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_CONN_DEST</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_AUTH_DEST</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_ON</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_MODE</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_ROW_IMAGE</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SERVER_ID</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_EXIST</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_ENGINE</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_MYSQL_PASSOWRD_FORMAT</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
```

数据传输

```xml
CecStatusSuccess/CecStatus
                        <ItemName>CHECK_SRC</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SAME_OBJ</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SQL_MODE</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SAME_USER</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_TOPOLOGY</ItemName>
                  </Detail>
            </PrecheckStatus>
            <SynchronizationJobId>dtsexjk1alb116lbf1</SynchronizationJobId>
            <DataInitialization>true</DataInitialization>
            <DestinationEndpoint>
                  <InstanceId>rm-bp162d4tp0500****</InstanceId>
                  <InstanceType>RDS</InstanceType>
                  <EngineName>MySQL</EngineName>
            </DestinationEndpoint>
            <SourceEndpoint>
                  <InstanceId>rm-bp1i99e8l7913****</InstanceId>
                  <InstanceType>RDS</InstanceType>
                  <EngineName>MySQL</EngineName>
            </SourceEndpoint>
            <StructureInitialization>true</StructureInitialization>
            <ExpireTime>2021-07-07T16:00:00Z</ExpireTime>
            <Performance>
                  <RPS>0</RPS>
                  <FLOW>0.00MB/s</FLOW>
            </Performance>
            <SynchronizationJobClass>large</SynchronizationJobClass>
            <DataSynchronizationStatus></DataSynchronizationStatus>
            <StructureInitializationStatus>
                  <Status>Finished</Status>
                  <Progress>1</Progress>
                  <Percent>100</Percent>
            </StructureInitializationStatus>
      </SynchronizationInstances>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>92E1E99D-5224-4AD3-8C94-23A3516B****</RequestId>
      <PageNumber>1</PageNumber>
</DescribeSynchronizationJobsResponse>
```

`JSON` 格式

```json
{ "TotalRecordCont"
```

数据传输

```json
 "TotalRecordCount": 100,
 "SynchronizationInstances": [
  {
   "Status": "synchronizing",
   "SynchronizationObjects": [
    {
     "TableIncludes": [],
     "TableExcludes": [],
     "SchemaName": "dtstestdatabase",
     "NewSchemaName": "newdtstestdatabase"
    }
```

`],`

```json
   "DataInitializationStatus": {
    "Status": "Finished",
    "Progress": "200001",
    "Percent": "100"
   },
   "SynchronizationJobName": "MySQL同步",
   "InstanceCreateTime": "2021-06-28T09:36:32Z",
            "CreateTime": "2021-06-28 17:34:53.0",
            "JobCreateTime": "2021-06-28T09:34:53Z",
   "PayType": "PostPaid",
   "Delay": "0",
   "PrecheckStatus": {
    "Status": "Finished",
    "Percent": "100",
    "Detail": [
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_CONN_SRC"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_AUTH_SRC"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_CONN_DEST"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_AUTH_DEST"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_BINLOG_ON"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_BINLOG_MODE"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_BINLOG_ROW_IMAGE"
},
```

数据传输

```json
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_SERVER_ID"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_BINLOG_EXIST"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_ENGINE"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_MYSQL_PASSOWRD_FORMAT"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_SRC"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_SAME_OBJ"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_SQL_MODE"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_SAME_USER"
     },
     {
      "CheckStatus": "Success",
      "ItemName": "CHECK_TOPOLOGY"
     }
```

]

```json
   },
   "SynchronizationJobId": "dtsexjk1alb116lbf1",
   "DataInitialization": true,
   "DestinationEndpoint": {
    "InstanceId": "rm-bp162d4tp0500****",
    "InstanceType": "RDS",
    "EngineName": "MySQL"
   },
   "SourceEndpoint": {
    "InstanceId": "rm-bp1i99e8l7913****",
    "InstanceType": "RDS",
    "EngineName": "MySQL"
   },
   "StructureInitialization": true,
   "ExpireTime": "2021-07-07T16:00:00Z",
            "Performance": {
    "RPS": "0",
```

数据传输 ,

```json
    "FLOW": "0.00MB/s"
   },
   "SynchronizationJobClass": "large",
   "Tags": [],
   "DataSynchronizationStatus": {},
   "StructureInitializationStatus": {
    "Status": "Finished",
    "Progress": "1",
    "Percent": "100"
   }
  }
```

`],`

```json
 "PageRecordCount": 30,
 "RequestId": "92E1E99D-5224-4AD3-8C94-23A3516B****",
 "PageNumber": 1
}
```

##### 查询同步初始化详情

调用DescribeInitializationStatus查询同步初始化详情，即待同步对象的结构和存量数据初始化到目标库的情况。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInitializ ationStatus | 系统规定参数，取值：DescribeInitializationStatus。 |
| SynchronizationJ obId | String | 是 | dtsi76118o3w92 **** | 数据同步实例ID，可以通过调用 DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据同步实例所在地域的ID。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：1~100，默认值为30。 |
| PageNum | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| DataInitializati onDetails | Array of DataInitializati onDetail |  | 全量数据初始化详情。 |
|---|---|---|---|
| DestinationOw nerDBName | String | dtstestdata | 目标实例中待同步对象所属数据库的名称。 |
| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据初始化失败时返回对应的失败信息。 |
| FinishRowNum | String | 9993 | 已完成同步的行数。 说明该参数表示实际同步的总行数，而参数TotalRowNum的值来源于同步开始前源库的系统表，由于同步时间差， 会导致两者的值会有出入。 |
| SourceOwnerD BName | String | dtstestdata | 源实例中待同步对象所属数据库的名称。 |
| Status | String | Finished | 全量数据初始化的状态，返回值： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
| TableName | String | customer | 同步对象的表名。 |
| TotalRowNum | String | 9981 | 需同步的总行数。 说明该参数的值来源于同步开始前源库的系统表，而参数FinishRowNum表示实际同步的总行数，由于同步时间差，会导致两者的值会有出入。 |
| UsedTime | String | 0.0 | 全量同步初始化的耗时。 |
| DataSynchroni zationDetails | Array of DataSynchroni zationDetail |  | 增量数据同步详情。 说明该参数合集及包含的返回参数即将下线。 |
| DestinationOw nerDBName | String | dtstestdata | 目标实例中待同步对象所属数据库的名称。 |
| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据同步失败时返回对应的失败信息。 |

数据传输

| SourceOwnerD BName | String | dtstestdata | 源实例中待同步对象所属数据库的名称。 |
|---|---|---|---|
| Status | String | Migrating | 增量数据同步的状态，返回值： NotStarted：未启动。 Migrating：同步中。 Failed：同步失败。 Finished：同步完成。 |
| TableName | String | customer | 同步对象的表名。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 150DECD9-13FF- 4929-A5DE- 855BE9CC**** | 请求ID。 |
| StructureInitial izationDetails | Array of StructureInitial izationDetail |  | 结构初始化详情。 |
| Constraints | Array of StructureInitial izationDetail |  | 同步对象对应的约束（例如索引、外键等）。 说明只有ObjectType为Table，且同步对象有约束，才会返回本参数。 |
| DestinationOw nerDBName | String | dtstestdata | 目标实例中待同步对象所属数据库的名称。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist | 约束创建失败的错误提示。 |
| ObjectDefinitio n | String | CREATE SEQUENCE "public"."collection s id seq" _ _ MINVALUE 1 MAXVALUE 922337203685477 5807 START 249 INCREMENT BY 1 ; | 创建约束的结构语法定义。 |
| ObjectName | String | customer | 该同步对象的名称。 |
| ObjectType | String | Table | 同步对象的类型，固定为Table。 |

数据传输

| SourceOwnerD BName | String | dtstestdata | 源实例中待同步对象所属数据库的名称。 |
|---|---|---|---|
| Status | String | Finished | 约束创建状态，返回值： NotStarted：未启动。 Migrating：创建中。 Failed：创建失败。 Finished：创建完成。 |
| DestinationOw nerDBName | String | dtstestdata | 目标实例中待同步对象所属数据库的名称。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: Table 'customer' already exists | 结构初始化失败时返回对应的失败信息。 |
| ObjectDefinitio n | String | CREATE TABLE `dtstestdata`.`cust omer` (\n`customer id` _ int(10) unsigned auto increment _ COMMENT '' NOT NULL , \n`customer title` _ varchar(100) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NOT NULL , \n`customer comp _ any1216` varchar(40) CHARSET `utf8` COLLATE `utf8 general ci` _ _ COMMENT '' NOT NULL , \n`submission date _ 1216` date COMMENT '' NULL \n, PRIMARY KEY (`customer id`)) _ engine=InnoDB AUTO INCREMENT _ =200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8 general ci` _ _ ROW FORMAT= _ Dynamic comment = '' ;\n | 同步对象的结构语法定义。 |
| ObjectName | String | customer | 同步对象的名称。 |

数据传输

| ObjectType | String | Table | 同步对象的类型。返回值如下： Table（表）、Constraint（约束）、Index（索引）、View（视图）、Materialize View（物化视图）、Type（自定义类型）、Synonym（同义词）、Trigger（触发器）、Function（函数）、Procedure（存储过程）、Package（包）、Default（默认值）、Rule（规则）、PlanGuide（执行计划）、Sequence（序列）。 |
|---|---|---|---|
| SourceOwnerD BName | String | dtstestdata | 源实例中待同步对象所属数据库的名称。 |
| Status | String | Finished | 结构初始化的状态。返回值： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeInitializationStatus &SynchronizationJobId=dtsi76118o3w92****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<DescribeInitializationStatusResponse>
      <StructureInitializationDetails>
            <Status>Finished</Status>
            <ObjectType>Table</ObjectType>
            <ObjectDefinition>CREATE TABLE `dtstestdata`.`customer` (
`customer_id` int(10) unsigned auto_increment COMMENT '' NOT NULL , `customer_title` varchar(100) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , `customer_author1216` varchar(40) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , `submission_date1216` date COMMENT '' NULL , PRIMARY KEY (`customer_id`)) engine=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8_general_ci` ROW_FORMAT= Dynamic comment = '' ; </ObjectDefinition>
            <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
            <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
            <ObjectName>customer</ObjectName>
      </StructureInitializationDetails>
      <RequestId>150DECD9-13FF-4929-A5DE-855BE9CC****</RequestId>
      <DataInitializationDetails>
            <Status>Finished</Status>
            <TableName>customer</TableName>
            <TotalRowNum>9981</TotalRowNum>
            <UsedTime>0.0</UsedTime>
            <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
            <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
            <FinishRowNum>9993</FinishRowNum>
      </DataInitializationDetails>
      <Success>true</Success>
</DescribeInitializationStatusResponse>
```

`JSON` 格式数据传输

```json
{
 "StructureInitializationDetails": [
  {
   "Status": "Finished",
   "ObjectType": "Table",
   "ObjectDefinition": "CREATE TABLE `dtstestdata`.`customer` (\n`customer_id`  int(10)
unsigned auto_increment COMMENT '' NOT NULL , \n`customer_title` varchar(100) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , \n`customer_author1216` varchar(40) CHARSET `utf8` COLLATE `utf8_general_ci` COMME NT '' NOT NULL , \n`submission_date1216` date COMMENT '' NULL \n, PRIMARY KEY (`customer_id`)) engine=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8_general_ci` ROW_FORMAT= Dynamic comment = '' ;\n",
   "SourceOwnerDBName": "dtstestdata",
   "DestinationOwnerDBName": "dtstestdata",
   "ObjectName": "customer"
  }
```

`],`

```json
 "RequestId": "150DECD9-13FF-4929-A5DE-855BE9CC****",
 "DataInitializationDetails": [
  {
   "Status": "Finished",
   "TableName": "customer",
   "TotalRowNum": "9981",
   "UsedTime": "0.0",
   "SourceOwnerDBName": "dtstestdata",
   "DestinationOwnerDBName": "dtstestdata",
   "FinishRowNum": "9993"
  }
```

`],`

```json
 "Success": true
}
```

##### 查询一个或多个同步实例状态

调用DescribeSynchronizationJobStatusList查询一个或多个数据同步实例同步状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSynchro nizationJobStatu sList | 系统规定参数，取值：DescribeSynchronizationJobS tatusList。 |
| SynchronizationJ obIdListJsonStr | String | 是 | ["dtsexjk1alb11 6****","dtskfq11 49w254****"] | 数据同步实例ID，格式为JSON数组，可以通过调用DescribeSynchronizationJobs 接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |

数据传输

| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
|---|---|---|---|---|
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 2 | 一页展示的同步实例数量。 |
| RequestId | String | 1413460B-138A- 48D1-836C- B24EDDC1**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |
| Synchronizatio nJobListStatus List | Array of Synchronizatio nJobStatusInfo |  | 同步任务状态列表。 |
| Synchronizatio nDirectionInfo List | Array of Synchronizatio nDirectionInfo |  | 同步方向详情列表。 |
| Checkpoint | String | 1610524452 | 同步最新一条数据的时间戳，格式为Unix时间戳。 说明 Unix时间戳转换工具可用搜索引擎获取。 |

数据传输

| Status | String | synchronizing | 同步实例在该方向上的同步状态，返回值： NotStarted：未启动 Prechecking：预检查中 PrecheckFailed：预检查失败 Initializing：同步初始化 InitializeFailed：同步初始化失败 Synchronizing：同步中 Failed：同步失败 Suspending：暂停 Modifying：同步对象变更中 Finished：完成 |
|---|---|---|---|
| Synchronizatio nDirection | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 |
| Synchronizatio nJobId | String | dtsexjk1alb116**** | 数据同步实例ID。 |
| TotalRecordCo unt | Long | 2 | 所查询的同步实例总数。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobStatusList &SynchronizationJobIdListJsonStr=["dtsexjk1alb116****","dtskfq1149w254****"]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<DescribeSynchronizationJobStatusListResponse>
      <TotalRecordCount>2</TotalRecordCount>
      <PageRecordCount>2</PageRecordCount>
      <RequestId>1413460B-138A-48D1-836C-B24EDDC1****</RequestId>
      <PageNumber>1</PageNumber>
      <SynchronizationJobListStatusList>
            <SynchronizationJobId>dtsexjk1alb116****</SynchronizationJobId>
            <SynchronizationDirectionInfoList>
                  <Status>synchronizing</Status>
                  <Checkpoint>1610524452</Checkpoint>
                  <SynchronizationDirection>Forward</SynchronizationDirection>
            </SynchronizationDirectionInfoList>
      </SynchronizationJobListStatusList>
      <SynchronizationJobListStatusList>
            <SynchronizationJobId>dtskfq1149w254****</SynchronizationJobId>
            <SynchronizationDirectionInfoList>
                  <Status>synchronizing</Status>
                  <Checkpoint>1610524457</Checkpoint>
                  <SynchronizationDirection>Forward</SynchronizationDirection>
            </SynchronizationDirectionInfoList>
      </SynchronizationJobListStatusList>
      <Success>true</Success>
</DescribeSynchronizationJobStatusListResponse>
```

`JSON` 格式数据传输

```json
{
 "TotalRecordCount": 2,
 "PageRecordCount": 2,
 "RequestId": "1413460B-138A-48D1-836C-B24EDDC1****",
 "PageNumber": 1,
 "SynchronizationJobListStatusList": [
  {
   "SynchronizationJobId": "dtsexjk1alb116****",
   "SynchronizationDirectionInfoList": [
    {
     "Status": "synchronizing",
     "Checkpoint": "1610524452",
     "SynchronizationDirection": "Forward"
    }
```

]

```json
  },
  {
   "SynchronizationJobId": "dtskfq1149w254****",
   "SynchronizationDirectionInfoList": [
    {
     "Status": "synchronizing",
     "Checkpoint": "1610524457",
     "SynchronizationDirection": "Forward"
    }
```

]

```
  }
```

`],`

```json
 "Success": true
}
```

##### 查询一个数据同步实例状态

调用DescribeSynchronizationJobStatus查询一个同步实例的运行状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSynchro nizationJobStatu s | 系统规定参数，取值：DescribeSynchronizationJobS tatus。 |
| SynchronizationJ obId | String | 是 | dtsexjk1alb116* *** | 数据同步实例ID，可以通过调用 DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据同步实例所在地域的ID。 |

数据传输

| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 只有当数据同步实例的同步拓扑为双向同步时，本参数传入Reverse才会生效。 |
|---|---|---|---|---|
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Checkpoint | String | 1610616144 | 同步最新一条数据的时间戳，格式为Unix时间戳。 说明 Unix时间戳转换工具可用搜索引擎获取。 |
| DataInitializati on | String | true | 是否执行全量数据初始化，取值： true：是。 false：否。 |
| DataInitializati onStatus | Struct |  | 全量数据初始化状态。 |
| ErrorMessage | String | java.lang.NumberF ormatException: For input string: "" | 全量数据初始化失败的错误提示。 |
| Percent | String | 100 | 全量数据初始化进度，单位为百分比。 |
| Progress | String | 200001 | 已完成全量数据初始化的记录数。 |
| Status | String | Finished | 全量数据初始化状态，取值包括： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |

数据传输

| DataSynchroni zationStatus | Struct |  | 增量数据同步状态。 |
|---|---|---|---|
| Checkpoint | String | 1610709865 | 同步最新一条数据的时间戳，格式为Unix时间戳。 |
| Delay | String | 0 | 增量数据同步延迟，单位为秒。 |
| DelayMillis | Long | 856 | 增量数据同步延迟，单位为毫秒。 |
| ErrorMessage | String | 任务失败太久无法恢复 | 增量数据同步失败的错误提示。 |
| Percent | String | 100 | 增量数据同步进度，单位为百分比。 |
| Status | String | Finished | 增量数据同步状态，取值包括： NotStarted：未启动。 Migrating：同步中。 Failed：同步失败。 Finished：同步完成。 |
| Delay | String | 0 | 同步延迟，单位为秒。 |
| DelayMillis | Long | 506 | 同步延迟，单位为毫秒。 |
| DestinationEn dpoint | Struct |  | 目标实例的连接信息。 |
| EngineName | String | MySQL | 目标实例的数据库类型。 |
| IP | String | 172.16.88.*** | 目标实例的连接地址。 |
| InstanceId | String | rm- bp162d4tp0500*** * | 目标实例ID。 |
| InstanceType | String | RDS | 目标实例类型。 |
| Port | String | 3306 | 目标实例的数据库服务端口。 |
| UserName | String | dtstest | 目标实例的数据库账号。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |

数据传输

| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
|---|---|---|---|
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.ex ceptions.jdbc4.MyS QLNonTransientCo nnectionException: Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.ex ceptions.jdbc4.Co mmunicationsExce ption:Communicati ons link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectE xception:Connectio n timed out (Connection timed out)] About more information in [https://yq.aliyun.c om/articles/499178 ]. | 数据同步失败的错误提示。 |
| ExpireTime | String | 2021-03- 07T16:00:00Z | 同步实例的到期时间，yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明当PayType参数的返回值为PrePaid时才会返回本参数。 |
| PayType | String | PrePaid | 同步实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| Performance | Struct |  | 同步链路概况信息。 |
| FLOW | String | 1 | 每秒同步数据的流量，单位为MB/s。 |

数据传输

| RPS | String | 100 | 每秒同步SQL语句的次数，包括BEGIN、 COMMIT 、DML语句（INSERT、DELETE、 UPDATE）及DDL语句。 |
|---|---|---|---|
| PrecheckStatu s | Struct |  | 预检查状态。 |
| Detail | Array of CheckItem |  | 各预检查项的执行情况。 |
| CheckStatus | String | Success | 检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
| ErrorMessage | String | Original error: Access denied for user 'dtstest'@'100.104. ***.**' (using password: YES) | 预检查未通过的错误提示。 说明当CheckStatus参数返回值为Failed时，才会返回本参数。 |
| ItemName | String | CHECK CONN SRC _ _ | 预检查项目。 |
| RepairMethod | String | CHECK ERROR DE _ _ ST CONN REPAIR2 _ _ | 预检查未通过时对应的修复方法。 说明当CheckStatus参数返回值为Failed时，才会返回本参数。 |
| Percent | String | 100 | 预检查整体进度，单位为百分比。 |
| Status | String | Success | 预检查结果，返回值： Success：通过该项检查。 Failed：未通过该项检查。 |
| RequestId | String | DACDF659-AFC6- 4DC8-ADB8- 4569419A4**** | 请求ID。 |
| SourceEndpoin t | Struct |  | 源实例连接信息。 |
| EngineName | String | MySQL | 源实例的数据库类型。 |
| IP | String | 172.16.88.*** | 源实例的连接地址。 |
| InstanceId | String | rm- bp1i99e8l7913**** | 源实例ID。 |

数据传输

| InstanceType | String | RDS | 源实例类型。 |
|---|---|---|---|
| Port | String | 3306 | 源实例的数据库服务端口。 |
| UserName | String | dtstest | 源实例的数据库账号。 |
| Status | String | synchronizing | 同步实例的状态，返回值： notStarted：未启动。 prechecking：预检查中。 precheckFailed：预检查失败。 initializating：同步初始化中。 initializeFailed：同步初始化失败。 synchronizing：同步中。 failed：同步失败。 suspending：暂停。 modifying：同步对象变更中。 finished：完成。 |
| StructureInitial ization | String | true | 是否执行结构初始化，返回值： true：是 false：否 |
| StructureInitial izationStatus | Struct |  | 结构初始化状态。 |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | 结构初始化出现异常的错误提示。 |
| Percent | String | 100 | 结构初始化进度，单位为百分比。 |
| Progress | String | 1 | 已完成结构初始化的表的数量。 |
| Status | String | Finished | 结构初始化状态，取值包括： NotStarted：未启动。 Migrating：初始化中。 Failed：初始化失败。 Finished：初始化完成。 |
| Success | String | true | 请求是否成功。 |

数据传输

| Synchronizatio nDirection | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 |
|---|---|---|---|
| Synchronizatio nJobClass | String | large | 同步链路规格。 |
| Synchronizatio nJobName | String | MySQL同步 | 同步实例名称。 |
| Synchronizatio nJobId | String | dtsexjk1alb116**** | 数据同步实例ID。 |
| Synchronizatio nObjects | Array of Synchronizatio nObject |  | 同步对象。 |
| NewSchemaN ame | String | newdtstestdatabas e | 待同步的库在目标数据库中映射的名称。 |
| SchemaName | String | dtstestdatabase | 待同步的库名。 |
| TableExcludes | Array of TableExclude |  | 待同步库中排除的表，这些表将不会被同步。 |
| TableName | String | order | 排除的表的名称。 |
| TableIncludes | Array of TableInclude |  | 待同步的表。 |
| TableName | String | customer | 待同步表名。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobStatus &SynchronizationJobId=dtsexjk1alb116****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSynchronizationJobStatusResponse>
      <TaskId>exjk1alb116****</TaskId>
      <SynchronizationObjects>
            <SchemaName>newdtstestdatabase</SchemaName>
            <NewSchemaName>dtstestdatabase</NewSchemaName>
      </SynchronizationObjects>
      <DataInitializationStatus>
            <Status>Finished</Status>
            <Progress>200001</Progress>
```

数据传输

```xml
            <Percent>100</Percent>
      </DataInitializationStatus>
      <Delay>0</Delay>
      <Success>true</Success>
      <DelayMillis>0</DelayMillis>
      <DataInitialization>true</DataInitialization>
      <SynchronizationJobClass>large</SynchronizationJobClass>
      <Status>synchronizing</Status>
      <RequestId>DACDF659-AFC6-4DC8-ADB8-4569419A****</RequestId>
      <SynchronizationJobName>MySQL同步</SynchronizationJobName>
      <PayType>PostPaid</PayType>
      <ErrMessage></ErrMessage>
      <PrecheckStatus>
            <Status>Finished</Status>
            <Percent>100</Percent>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_CONN_SRC</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_AUTH_SRC</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_CONN_DEST</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_AUTH_DEST</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_BINLOG_ON</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_BINLOG_MODE</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_BINLOG_ROW_IMAGE</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SERVER_ID</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_BINLOG_EXIST</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_ENGINE</ItemName>
```

数据传输

```xml
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_MYSQL_PASSOWRD_FORMAT</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SRC</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SAME_OBJ</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SQL_MODE</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SAME_USER</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_TOPOLOGY</ItemName>
            </Detail>
      </PrecheckStatus>
      <Checkpoint>1610616144</Checkpoint>
      <SynchronizationJobId>dtsexjk1alb116****</SynchronizationJobId>
      <DestinationEndpoint>
            <InstanceId>rm-bp1u40w1ip917****</InstanceId>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </DestinationEndpoint>
      <SourceEndpoint>
            <InstanceId>rm-bp1i99e8l7913****</InstanceId>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </SourceEndpoint>
      <StructureInitialization>true</StructureInitialization>
      <Performance>
            <RPS>0</RPS>
            <FLOW>0.00MB/s</FLOW>
      </Performance>
      <StructureInitializationStatus>
            <Status>Finished</Status>
            <Progress>1</Progress>
            <Percent>100</Percent>
      </StructureInitializationStatus>
</DescribeSynchronizationJobStatusResponse>
```

`JSON` 格式

```json
{
 "TaskId": "exjk1alb116****",
```

数据传输 j ,

```json
    "SynchronizationObjects": [
  {
   "TableIncludes": [],
   "TableExcludes": [],
   "SchemaName": "newdtstestdatabase",
   "NewSchemaName": "dtstestdatabase"
  }
```

`],`

```json
 "DataInitializationStatus": {
  "Status": "Finished",
  "Progress": "200001",
  "Percent": "100"
 },
 "Delay": "0",
 "Success": true,
 "DelayMillis": 0,
 "DataInitialization": true,
 "SynchronizationJobClass": "large",
 "Status": "synchronizing",
 "RequestId": "DACDF659-AFC6-4DC8-ADB8-4569419A****",
 "SynchronizationJobName": "MySQL同步",
 "PayType": "PostPaid",
 "ErrMessage": "",
 "PrecheckStatus": {
  "Status": "Finished",
  "Percent": "100",
  "Detail": [
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_CONN_SRC"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_AUTH_SRC"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_CONN_DEST"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_AUTH_DEST"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_ON"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_MODE"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_ROW_IMAGE"
```

数据传输

```json
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SERVER_ID"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_EXIST"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_ENGINE"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_MYSQL_PASSOWRD_FORMAT"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SRC"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SAME_OBJ"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SQL_MODE"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_SAME_USER"
   },
   {
    "CheckStatus": "Success",
    "ItemName": "CHECK_TOPOLOGY"
   }
```

]

```json
 },
 "Checkpoint": "1610616144",
 "SynchronizationJobId": "dtsexjk1alb116****",
 "DestinationEndpoint": {
  "InstanceId": "rm-bp1u40w1ip917****",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
 },
 "SourceEndpoint": {
  "InstanceId": "rm-bp1i99e8l7913****",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
 },
 "StructureInitialization": true,
 "Performance": {
  "RPS": "0",
```

数据传输

```json
  "FLOW": "0.00MB/s"
 },
 "StructureInitializationStatus": {
  "Status": "Finished",
  "Progress": "1",
  "Percent": "100"
 }
}
```

##### 释放同步实例

调用DeleteSynchronizationJob释放数据同步实例。 数据同步实例一旦释放将无法找回。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteSynchroni zationJob | 系统规定参数，取值：DeleteSynchronizationJob。 |
| SynchronizationJ obId | String | 是 | dtshn6107ve26 4**** | 数据同步实例ID，可以通过调用 DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据同步实例所在地域的ID。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | C306C198-7807- 409D-930A- D6CE6C32**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

数据传输

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DeleteSynchronizationJob &SynchronizationJobId=dtshn6107ve264****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteSynchronizationJobResponse>
      <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId>
      <Success>true</Success>
</DeleteSynchronizationJobResponse>
```

`JSON` 格式

```json
{
 "RequestId": "C306C198-7807-409D-930A-D6CE6C32****",
 "Success": true
}
```

#### 数据订阅

##### 购买订阅实例

调用CreateSubscriptionInstance接口购买DTS数据订阅实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateSubscripti onInstance | 系统规定参数，取值：CreateSubscriptionInstance。 |
| Region | String | 是 | cn-hangzhou | 地域ID，与订阅对象所在地域保持一致。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所属的地域，无需设置，该参数即将下线。 |
| SourceEndpoint.I nstanceType | String | 否 | MySQL | 数据订阅的实例类型，取值为：MySQL、PolarDB、DRDS、Ora cle。 说明默认取值为：MySQL。 |

数据传输

| PayType | String | 否 | Prepaid | 付费类型。 Postpaid：按量付费，默认付费类型。 Prepaid：预付费。 |
|---|---|---|---|---|
| Period | String | 否 | Month | 预付费实例的计费方式，取值： Year：包年。 Month：包月。 说明当付费类型为Prepaid（预付费）时，该参数才有效且必须传入。 |
| UsedTime | Integer | 否 | 12 | 预付费实例购买时长。 当计费方式为Year（包年）时，取值范围为1~5。 当计费方式为Month（包月）时，取值范围为1~60。 说明当付费类型为Prepaid（预付费）时，该参数才有效且必须传入。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 4E9564C5-F99D- 4176-A6BA- 2D7F2DC8**** | 请求ID。 |
| SubscriptionIn stanceId | String | dtsfen11q2g23x*** * | 数据订阅实例ID。 |
| Success | String | true | 请求是否成功。 |

数据传输

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=CreateSubscriptionInstance &Region=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateSubscriptionInstanceResponse>
      <RequestId>4E9564C5-F99D-4176-A6BA-2D7F2DC8****</RequestId>
      <SubscriptionInstanceId>dtsfen11q2g23x****</SubscriptionInstanceId>
      <Success>true</Success>
</CreateSubscriptionInstanceResponse>
```

`JSON` 格式

```json
{
 "RequestId": "4E9564C5-F99D-4176-A6BA-2D7F2DC8****",
 "SubscriptionInstanceId": "dtsfen11q2g23x****",
 "Success": true
}
```

##### 配置订阅实例

调用本接口前，已调用CreateSubscriptionInstance接口创建了数据订阅实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ConfigureSubscr iptionInstance | 系统规定参数，取值：ConfigureSubscriptionInstanc e。 |
| SubscriptionDat aType.DDL | Boolean | 是 | true | 是否订阅DDL类型的数据，取值： true：是，为默认值。 false：否。 |
| SubscriptionDat aType.DML | Boolean | 是 | true | 是否订阅DML类型的数据，取值： true：是，为默认值。 false：否。 |
| SubscriptionObje ct | String | 是 | [{ "DBName": "dtstestdata" }] | 订阅对象，格式为JSON串且支持一定的正则表达式。 |

数据传输

| SubscriptionInst anceId | String | 是 | dtshp8n2ze4r5x **** | 数据订阅实例ID。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| SubscriptionInst anceName | String | 否 | MySQL订阅 | 订阅实例名称。 说明建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| SourceEndpoint.I nstanceType | String | 否 | RDS | 源数据库的实例类型，取值： RDS：RDS MySQL。 PolarDB：PolarDB MySQL。 LocalInstance：有公网IP的自建数据库。 ECS：ECS上的自建数据库。 Express：通过专线接入的自建数据库。 CEN：通过云企业网CEN接入的自建数据库。 dg：通过数据库网关接入的自建数据库。 说明支持自建数据库的数据库类型为MySQL、Oracle，您需要提前调用 CreateSubscriptionInstance设置。 |
| SourceEndpoint.I nstanceID | String | 否 | rm- bp1zc3iyqe3qw* *** | 源实例ID。 说明源数据库的实例类型为 RDS MySQL、PolarDB-X 1.0、 PolarDB MySQL时，本参数才可用且必须传入。 |
| SourceEndpoint.I P | String | 否 | 172.16.88.*** | 源数据库的连接地址。 说明当源数据库为自建数据库时，本参数才可用且必须传入。 |
| SourceEndpoint. Port | String | 否 | 3306 | 源数据库的服务端口。 说明当源数据库为自建数据库时，本参数才可用且必须传入。 |

数据传输

| SourceEndpoint. UserName | String | 否 | dtstestaccount | 源实例的数据库账号。 说明订阅不同的数据库所需的权限有所差异。 |
|---|---|---|---|---|
| SourceEndpoint. Password | String | 否 | Test123456 | 源实例的数据库账号密码。 |
| SourceEndpoint. OracleSID | String | 否 | testsid | Oracle数据库的SID信息。 说明当源数据库为自建 Oracle时，且Oracle数据库为非 RAC实例时，本参数才可用且必须传入。 |
| SourceEndpoint. DatabaseName | String | 否 | dtstestdata | 待订阅的数据库名称。 |
| SourceEndpoint. OwnerID | String | 否 | 140692647406* *** | 源实例所属的阿里云账号ID。 说明仅在配置跨阿里云账号的数据订阅时本参数才可用，且必须传入。 |
| SourceEndpoint. Role | String | 否 | ram-for-dts | 源实例的授权角色。当源实例与配置订阅任务所属阿里云账号不同时，需传入该参数，来指定源实例的授权角色，以允许配置订阅任务所属阿里云账号访问源实例的实例信息。 |
| SubscriptionInst anceNetworkTyp e | String | 否 | vpc | 订阅实例的网络类型，取值： classic：经典网络。 vpc：专有网络。 说明如果传入了本参数，则订阅实例被定义为新版，如果不传入该参数，则订阅实例被定义为旧版。 旧版订阅实例支持订阅自建 MySQL、RDS for MySQL 和DRDS的数据，新版订阅实例支持订阅自建MySQL、 RDS for MySQL、PolarDB MySQL和Oracle的数据。 如果本参数传入的值为vpc时，您还需要传入SubscriptionInstanc e.VPCId和Subscription Instance.VSwitchID参数。 |

数据传输

| SubscriptionInst ance.VPCId | String | 否 | vpc- bp1vwnn14rqpyi czj**** | 订阅实例的专有网络ID。 说明当SubscriptionInstanceNetwo rkType取值为vpc时，本参数才可用且必须传入。 |
|---|---|---|---|---|
| SubscriptionInst ance.VSwitchId | String | 否 | vsw- bp10df3mxae6l pmku**** | 订阅实例的虚拟交换机ID。 说明当SubscriptionInstanceNetwo rkType取值为vpc时，本参数才可用且必须传入。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| RequestId | String | 0CC15092-8957- 4532-B559- B4FB80AC**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSubscriptionInstance &SubscriptionDataType.DDL=true &SubscriptionDataType.DML=true &SubscriptionInstanceId=dtshp8n2ze4r5x**** &SubscriptionObject=[{"DBName":"dtstestdata","TableIncludes": [{"TableName":"customer"}]}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<ConfigureSubscriptionInstanceResponse>
      <RequestId>0CC15092-8957-4532-B559-B4FB80AC****</RequestId>
      <Success>true</Success>
</ConfigureSubscriptionInstanceResponse>
```

`JSON` 格式

```json
{
 "RequestId": "0CC15092-8957-4532-B559-B4FB80AC****",
 "Success": true
}
```

##### 启动订阅实例

调用StartSubscriptionInstance接口启动数据订阅实例。 调用本接口时，数据订阅实例需处于未启动或启动失败状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartSubscriptio nInstance | 系统规定参数。取值： StartSubscriptionInstance。 |
| SubscriptionInst anceId | String | 是 | dtso6m11cxt26 q**** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | B083F9AB-BE9B- 4716-8AD3- CFA04391**** | 请求ID。 |

数据传输

| Success | String | true | 请求是否成功。 |
|---|---|---|---|
| TaskId | String | 11**** | 任务ID，该参数即将下线。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=StartSubscriptionInstance &SubscriptionInstanceId=dtso6m11cxt26q****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StartSubscriptionInstanceResponse>
      <TaskId>11****</TaskId>
      <RequestId>B083F9AB-BE9B-4716-8AD3-CFA04391****</RequestId>
      <Success>true</Success>
</StartSubscriptionInstanceResponse>
```

`JSON` 格式

```json
{
 "TaskId": "11****",
 "RequestId": "B083F9AB-BE9B-4716-8AD3-CFA04391****",
 "Success": true
}
```

##### 修改订阅对象

调用本接口时，订阅通道需处于正常、未启动或启动失败状态。

**说明**

StartSubscriptionInstance重启订阅通道。 当订阅通道处于未启动或启动失败状态时，成功调用本接口修改订阅对象后，DTS不会自动启动订阅通道，您需要手动调用StartSubscriptionInstance重启订阅通道。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | ModifySubscripti onObject | 系统规定参数，取值：ModifySubscriptionObject。 |
|---|---|---|---|---|
| SubscriptionInst anceId | String | 是 | dtsl8zl9ek6292* *** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| SubscriptionObje ct | String | 是 | [{"DBName":"dt stestdata"}] | 订阅对象，格式为JSON串且支持一定的正则表达式。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| RequestId | String | ABBACEFC-CBA9- 4F80-A337- 42F202F5**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifySubscriptionObject &SubscriptionInstanceId=dtsl8zl9ek6292**** &SubscriptionObject=[{"DBName":"dtstestdata"}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<ModifySubscriptionObjectResponse>
      <RequestId>ABBACEFC-CBA9-4F80-A337-42F202F5****</RequestId>
      <Success>true</Success>
</ModifySubscriptionObjectResponse>
```

`JSON` 格式

```json
{
 "RequestId": "ABBACEFC-CBA9-4F80-A337-42F202F5****",
 "Success": true
}
```

##### 管理消费组

###### 创建消费组

调用CreateConsumerGroup接口为数据订阅实例新增消费组。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateConsumer Group | 系统规定参数，取值：CreateConsumerGroup。 |
| ConsumerGroup Name | String | 是 | 测试订阅组 | 消费组名称，不超过128个字符。建议配置具有业务意义的名称，便于后续识别。 |
| ConsumerGroup Password | String | 是 | Test123456 | 消费组账号的密码。 由大写字母、小写字母、数字、特殊字符中的任意两种或两种以上组成。 密码长度为8~32个字符。 |
| ConsumerGroup UserName | String | 是 | dtstest | 消费组的账号。 由大写字母、小写字母、数字、下划线中的任意一种或多种组成。 最长16个字符。 |
| SubscriptionInst anceId | String | 是 | dtsg2m10r1x15 a**** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

数据传输

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConsumerGrou pID | String | dtswc411cg617p** ** | 消费组ID。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| RequestId | String | 6063641E-BAD1- 4BA7-B70B- 26FFFD18**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=CreateConsumerGroup
```

`&ConsumerGroupName=`测试订阅组

```
&ConsumerGroupPassword=Test123456 &ConsumerGroupUserName=dtstest &SubscriptionInstanceId=dtsg2m10r1x15a****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateConsumerGroupResponse>
      <ConsumerGroupID>dtswc411cg617p****</ConsumerGroupID>
      <RequestId>6063641E-BAD1-4BA7-B70B-26FFFD18****</RequestId>
      <Success>true</Success>
</CreateConsumerGroupResponse>
```

`JSON` 格式

```json
{
 "ConsumerGroupID": "dtswc411cg617p****",
 "RequestId": "6063641E-BAD1-4BA7-B70B-26FFFD18****",
 "Success": true
}
```

###### 查询消费组详情

调用DescribeConsumerGroup接口查询数据订阅实例中的消费组详情。 数据传输

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeConsum erGroup | 系统规定参数，取值：DescribeConsumerGroup。 |
| SubscriptionInst anceId | String | 是 | dtso5xx5t9u19e **** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30、50、100，默认值为30。 |
| PageNum | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConsumerCha nnels | Array of DescribeConsu merChannel |  | 消费组列表。 |
| DescribeConsu merChannel |  |  |  |
| ConsumerGrou pID | String | dtspis1110z232*** * | 消费组ID。 |
| ConsumerGrou pName | String | consumergrouptest | 消费组名称。 |
| ConsumerGrou pUserName | String | test | 消费组账号。 |
| ConsumptionC heckpoint | String | 2019-10- 02T12:00:00Z | 消费位点，即客户端在订阅通道内消费最后一条信息的时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

数据传输

| MessageDelay | Long | 172714 | 消息延迟时间=当前时间-数据订阅通道中存在时间最早的未被消费的消息的时间戳，单位为秒。 说明如果该参数返回-1，则表示当前没有客户端连接该消费组。 |
|---|---|---|---|
| UnconsumedD ata | Long | 186600 | 未消费的消息总数=未被消费的订阅数据数量 +心跳消息数量说明如果该参数返回-1，则表示当前没有客户端连接该消费组。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 一页最多可展示的消费组数量。 |
| RequestId | String | 4204E899-8193- 4D7D-A4FB- 3A7F9063**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |
| TotalRecordCo unt | Integer | 1 | 消费组总数。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeConsumerGroup &SubscriptionInstanceId=dtso5xx5t9u19e****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<DescribeConsumerGroupResponse>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>4204E899-8193-4D7D-A4FB-3A7F9063****</RequestId>
      <PageNumber>1</PageNumber>
      <ConsumerChannels>
            <DescribeConsumerChannel>
                  <ConsumptionCheckpoint></ConsumptionCheckpoint>
                  <ConsumerGroupID>dtspis1110z232gbm4</ConsumerGroupID>
                  <ConsumerGroupUserName>test</ConsumerGroupUserName>
                  <ConsumerGroupName>consumergrouptest</ConsumerGroupName>
                  <MessageDelay>-1</MessageDelay>
                  <UnconsumedData>-1</UnconsumedData>
            </DescribeConsumerChannel>
      </ConsumerChannels>
      <Success>true</Success>
</DescribeConsumerGroupResponse>
```

`JSON` 格式

```json
{
 "TotalRecordCount": 1,
 "PageRecordCount": 30,
 "RequestId": "4204E899-8193-4D7D-A4FB-3A7F9063****",
 "PageNumber": 1,
 "ConsumerChannels": {
  "DescribeConsumerChannel": [
   {
    "ConsumptionCheckpoint": "2019-10-02T12:00:00Z",
    "ConsumerGroupID": "dtspis1110z232gbm4",
    "ConsumerGroupUserName": "test",
    "ConsumerGroupName": "consumergrouptest",
    "MessageDelay": -1,
    "UnconsumedData": -1
   }
```

]

```json
 },
 "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请您稍后重试。 |

###### 修改消费组密码

数据传输

**说明**

本接口仅适用于新版订阅通道。在调用ConfigureSubscriptionInstance接口配置数据订阅通道时，如果传入了**SubscriptionInstanceNetworkType**参数，则订阅通道被定义为新版；如果不传入则订阅通道被定义为旧版。 调用本接口时，订阅通道需处于未启动、启动失败、正常或异常状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyConsumer GroupPassword | 系统规定参数，取值：ModifyConsumerGroupPassw ord。 |
| ConsumerGroupI D | String | 是 | dtswc411cg617 p**** | 消费组ID， 您可以调用DescribeConsumerGroup接口查询消费组ID。 |
| consumerGroup NewPassword | String | 是 | Test654321 | 消费组的新密码。 密码由大写字母、小写字母、数字、特殊字符中的任意两种或两种以上组成。 密码长度为8~32个字符。 |
| ConsumerGroup Password | String | 是 | Test123456 | 消费组当前的密码。 |
| SubscriptionInst anceId | String | 是 | dtsg2m10r1x15 a**** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| ConsumerGroup Name | String | 否 | dts订阅测试 | 消费组名称，您可以调用 DescribeConsumerGroup接口查询。 |
| ConsumerGroup UserName | String | 否 | dtstest | 消费组账号，您可以调用 DescribeConsumerGroup接口查询。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| RequestId | String | A06B5CFF-9576- 4BC1-BE62- A3D43E1F**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifyConsumerGroupPassword &ConsumerGroupID=dtswc411cg617p**** &consumerGroupNewPassword=Test654321 &ConsumerGroupPassword=Test123456 &SubscriptionInstanceId=dtsg2m10r1x15a****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyConsumerGroupPasswordResponse>
      <RequestId>A06B5CFF-9576-4BC1-BE62-A3D43E1F****</RequestId>
      <Success>true</Success>
</ModifyConsumerGroupPasswordResponse>
```

`JSON` 格式

```json
{
 "RequestId": "A06B5CFF-9576-4BC1-BE62-A3D43E1F****",
 "Success": true
}
```

###### 删除消费组

调用DeleteConsumerGroup接口删除订阅通道中的消费组。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | DeleteConsumer Group | 系统规定参数，取值：DeleteConsumerGroup。 |
|---|---|---|---|---|
| ConsumerGroupI D | String | 是 | dtssb911ydd192 **** | 消费组ID。 |
| SubscriptionInst anceId | String | 是 | dtsg2m10r1x15 a**** | 数据订阅实例ID，可以通过调用DescribeSubscriptionInstances 接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 4D0ADAD5-DD97- 41B6-B78F- D1961AB1**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DeleteConsumerGroup &ConsumerGroupID=dtssb911ydd192**** &SubscriptionInstanceId=dtsg2m10r1x15a****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteConsumerGroupResponse>
      <RequestId>4D0ADAD5-DD97-41B6-B78F-D1961AB1****</RequestId>
      <Success>true</Success>
</DeleteConsumerGroupResponse>
```

数据传输 `JSON` 格式

```json
{
 "RequestId": "4D0ADAD5-DD97-41B6-B78F-D1961AB1****",
 "Success": true
}
```

###### 修改消费时间点

调用ModifyConsumptionTimestamp接口修改数据订阅实例的消费时间点。

**说明**

本接口仅适用于旧版订阅通道。在调用ConfigureSubscriptionInstance接口配置数据订阅通道时，如果不传入了**SubscriptionInstanceNetworkType**参数，则订阅通道被定义为旧版；如果传入则订阅通道被定义为新版。 如果订阅通道为新版，您需要在客户端自定义消费时间点。 调用本接口时，需要停止消费的客户端，并且数据订阅通道需处于正常状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyConsumpt ionTimestamp | 系统规定参数，取值：ModifyConsumptionTimestam p。 |
| ConsumptionTim estamp | String | 是 | 2019-10- 15T17:20:03Z | 消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| SubscriptionInst anceId | String | 是 | dtsg2m10r1x15 a**** | 数据订阅实例ID，可以通过调用DescribeSubscriptionInstances 接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |

数据传输

| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
|---|---|---|---|
| RequestId | String | ABBACEFC-CBA9- 4F80-A337- 42F202F5**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ModifyConsumptionTimestamp &ConsumptionTimestamp=2019-10-15T17:20:03Z &SubscriptionInstanceId=dtsg2m10r1x15a****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyConsumptionTimestampResponse>
      <RequestId>ABBACEFC-CBA9-4F80-A337-42F202F5****</RequestId>
      <Success>true</Success>
</ModifyConsumptionTimestampResponse>
```

`JSON` 格式

```json
{
 "RequestId": "ABBACEFC-CBA9-4F80-A337-42F202F5****",
 "Success": true
}
```

##### 查询订阅实例列表及各实例详情

调用DescribeSubscriptionInstances接口查询订阅实例列表和各订阅实例详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSubscri ptionInstances | 系统规定参数，取值：DescribeSubscriptionInstance s。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |

数据传输

| PageSize | Integer | 否 | 30 | 每页记录数，取值：30、50、100，默认值为30。 |
|---|---|---|---|---|
| PageNum | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| SubscriptionInst anceName | String | 否 | MySQL订阅 | 订阅实例名称。 说明传入本参数后，DTS将在调用结果中返回包含该名称的订阅实例。 |
| ClientToken | String | 否 | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 当前页可展示的最大记录数。 |
| RequestId | String | FC3BAAF2-74E3- 4471-8EB5- 96202D6A**** | 请求ID。 |
| SubscriptionIn stances | Array of SubscriptionIn stance |  | 数据订阅实例列表和各订阅实例的详情。 |
| SubscriptionIn stance |  |  |  |
| BeginTimesta mp | String | 2021-06- 21T08:25:43Z | 订阅实例保存数据范围的起始时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |

数据传输

| ConsumptionC heckpoint | String | 2021-06- 21T09:30:31Z | 订阅实例的下游消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| ConsumptionC lient | String | 114.***.***.**:dts** ****** | 下游链接对应的IP和随机标识信息，其中IP为下游客户端的IP地址，随机标示为DTS生成的随机 ID。 |
| EndTimestamp | String | 2021-06- 21T10:17:21Z | 订阅实例保存数据范围的末尾时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| ErrorMessage | String | xxxxxxxx | 数据订阅异常的错误提示。 |
| PayType | String | PrePaid | 订阅实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
| SourceEndpoin t | Struct |  | 源实例的连接信息。 |
| InstanceID | String | rm- bp1162kryivb8**** | 源实例ID。 |
| InstanceType | String | RDS | 源实例类型。 说明当该订阅实例为新版时，才会返回该参数。 |
| Status | String | Normal | 订阅实例的状态，返回值为： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Starting：启动中。 Normal：正常。 Abnormal：异常。 |
| SubscribeTopi c | String | cn hangzhou rm b _ _ _ p1162kryivb8**** _ dtstest version2 _ | 订阅Topic。 说明当该订阅实例为新版，且调用 CreateConsumerGroup接口创建了消费组时，才会返回本参数。 |
| SubscriptionD ataType | Struct |  | 订阅数据的类型。 |

数据传输

| DDL | Boolean | true | 订阅数据是否包含DDL语句，返回值： true：是。 false：否。 |  |  |
|---|---|---|---|---|---|
| DML | Boolean | true | 订阅数据是否包含DML语句，返回值： true：是。 false：否。 |  |  |
| SubscriptionH ost | Struct |  | 订阅实例的连接地址。 |  |  |
| PrivateHost | String | dts-cn-****- internal.aliyuncs.co m:18002 | 订阅实例的私网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| PublicHost | String | dts-cn- ****.aliyuncs.com: 18001 | 订阅实例的公网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| VPCHost | String | dts-cn-****- vpc.aliyuncs.com:1 8003 | 订阅实例的专有网络VPC（Virtual Private Cloud）连接信息，格式为地址：端口号 。 |  |  |
| SubscriptionIn stanceID | String | rm- bp1162kryivb8**** | 数据订阅实例ID。 |  |  |
| SubscriptionIn stanceName | String | mysql订阅 | 数据订阅实例名称。 |  |  |
| SubscriptionO bject | Array of SynchronousO bject |  | 订阅对象。 |  |  |
| SynchronousO bject |  |  |  |  |  |
| DatabaseNam e | String | dtstestdata | 订阅对象所属数据库的名称。 |  |  |
| TableList | List | test1 | 订阅对象的表名。 |  |  |
| WholeDatabas e | String | false | 是否订阅整库，返回值： true：是。 false：否。 |  |  |
| Success | String | true | 请求是否成功。 |  |  |
| TotalRecordCo unt | Long | 1 | 阿里云主账号下所有符合条件的数据订阅实例数量。 |  |  |

| uncs.co | 号 |
|---|---|

| s.com: | 号 |
|---|---|

数据传输

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSubscriptionInstances &Tag.1.Key=testkey1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<DescribeSubscriptionInstancesResponse>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>FC3BAAF2-74E3-4471-8EB5-96202D6A****</RequestId>
      <PageNumber>1</PageNumber>
      <Success>true</Success>
      <SubscriptionInstances>
            <SubscriptionInstance>
                  <Status>Normal</Status>
                  <SubscriptionObject>
                        <SynchronousObject>
                              <DatabaseName>dtstestdata</DatabaseName>
                              <WholeDatabase>false</WholeDatabase>
                              <TableList>
                                    <Table>test1</Table>
                              </TableList>
                        </SynchronousObject>
                  </SubscriptionObject>
                  <SubscriptionDataType>
                        <DML>true</DML>
                        <DDL>true</DDL>
                  </SubscriptionDataType>
                  <SubscriptionInstanceName>mysql订阅</SubscriptionInstanceName>
                  <SubscriptionHost>
                        <PublicHost>dts-cn-hangzhou.aliyuncs.com:18001</PublicHost>
                        <PrivateHost>dts-cn-hangzhou-
internal.aliyuncs.com:18002</PrivateHost>
                        <VPCHost>dts-cn-hangzhou-vpc.aliyuncs.com:18003</VPCHost>
                  </SubscriptionHost>
<SubscribeTopic>cn_hangzhou_rm_bp1162kryiv******_dtstest_version2</SubscribeTopic>
                  <SourceEndpoint>
                        <InstanceID>rm-bp1162kryivb8****</InstanceID>
                        <InstanceType>RDS</InstanceType>
                  </SourceEndpoint>
                  <InstanceCreateTime>2021-06-21T10:17:21Z</InstanceCreateTime>
                  <JobCreateTime>2021-06-21T10:17:21Z</JobCreateTime>
                  <EndTimestamp>2021-06-21T10:17:21Z</EndTimestamp>
                  <PayType>PrePaid</PayType>
                  <SubscriptionInstanceID>dtsy0zz3t13h******</SubscriptionInstanceID>
                  <BeginTimestamp>2021-06-21T08:25:43Z</BeginTimestamp>
                  <Tags></Tags>
            </SubscriptionInstance>
      </SubscriptionInstances>
</DescribeSubscriptionInstancesResponse>
```

`JSON` 格式数据传输

```json
{
 "TotalRecordCount": 1,
 "PageRecordCount": 30,
 "RequestId": "FC3BAAF2-74E3-4471-8EB5-96202D6A****",
 "PageNumber": 1,
 "Success": true,
 "SubscriptionInstances": {
  "SubscriptionInstance": [
   {
    "Status": "Normal",
    "SubscriptionObject": {
     "SynchronousObject": [
      {
       "DatabaseName": "dtstestdata",
       "WholeDatabase": false,
       "TableList": {
        "Table": [
         "test1"
```

]

```
       }
      }
```

]

```json
    },
    "SubscriptionDataType": {
     "DML": true,
     "DDL": true
    },
    "SubscriptionInstanceName": "mysql订阅",
    "SubscriptionHost": {
     "PublicHost": "dts-cn-hangzhou.aliyuncs.com:18001",
     "PrivateHost": "dts-cn-hangzhou-internal.aliyuncs.com:18002",
     "VPCHost": "dts-cn-hangzhou-vpc.aliyuncs.com:18003"
    },
    "SubscribeTopic": "cn_hangzhou_rm_bp1162kryiv******_dtstest_version2",
    "SourceEndpoint": {
     "InstanceID": "rm-bp1162kryivb8****",
     "InstanceType": "RDS"
    },
    "InstanceCreateTime": "2021-06-21T10:17:21Z",
    "JobCreateTime": "2021-06-21T10:17:21Z",
                "EndTimestamp": "2021-06-21T10:17:21Z",
    "PayType": "PrePaid",
    "SubscriptionInstanceID": "dtsy0zz3t13h******",
    "BeginTimestamp": "2021-06-21T08:25:43Z",
    "Tags": {
     "Tag": []
    }
   }
```

]

```
 }
}
```

数据传输

##### 查询一个订阅实例状态

调用DescribeSubscriptionInstanceStatus接口查询一个数据订阅实例的状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSubscri ptionInstanceSta tus | 系统规定参数，取值：DescribeSubscriptionInstance Status。 |
| SubscriptionInst anceId | String | 是 | dtsy0zz3t13h7d* *** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BeginTimesta mp | String | 2021-03- 15T08:25:34Z | 订阅实例中保存的数据范围的起始时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| ConsumptionC heckpoint | String | 2021-03- 23T07:30:31Z | 订阅实例的下游消费时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| ConsumptionC lient | String | 114.***.***.**:dts** ****** | 下游消费客户端信息，由IP地址和DTS随机生成的随机数组成。 |
| EndTimestamp | String | 2021-03- 26T14:03:21Z | 订阅实例中保存的数据范围的截止时间点，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回的错误信息。 |
| ErrorMessage | String | ****** | 数据订阅异常的错误提示。 |
| ErrorMessage | String | ****** | 数据订阅异常的错误提示。 |

数据传输

| PayType | String | PrePaid | 订阅实例的付费类型，返回值： PrePaid：包年包月（预付费）。 PostPaid：按量付费（后付费）。 |
|---|---|---|---|
| RequestId | String | E0845D0A-6D36- 4EEB-BE26- CF191E1A**** | 请求ID。 |
| SourceEndpoin t | Struct |  | 源实例的连接信息。 |
| InstanceID | String | rm- bp1162kryivb8**** | 源库的实例ID。 |
| InstanceType | String | RDS | 源库的实例类型。 说明当该订阅实例为新版时，才会返回该参数。 |
| Status | String | Normal | 订阅实例的状态，返回值： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Starting：启动中。 Normal：正常。 Abnormal：异常。 |
| SubscribeTopi c | String | cn hangzhou rm b _ _ _ p1162kryivb8**** _ dtstest version2 _ | 订阅Topic。 说明当该订阅实例为新版，且调用 CreateConsumerGroup接口创建了消费组时，才会返回本参数。 |
| SubscriptionD ataType | Struct |  | 订阅数据的类型。 |
| DDL | Boolean | true | 订阅数据是否包含DDL语句，返回值： true：是。 false：否。 |
| DML | Boolean | true | 订阅数据是否包含DML语句，返回值： true：是。 false：否。 |
| SubscriptionH ost | Struct |  | 订阅实例的连接地址。 |

数据传输

| PrivateHost | String | dts-cn-****- internal.aliyuncs.co m:18002 | 订阅实例的私网连接信息，格式为地址：端口号 。 |  |  |
|---|---|---|---|---|---|
|  |  |  |  | 地址：端口 |  |
| PublicHost | String | dts-cn- ****.aliyuncs.com: 18001 | 订阅实例的公网连接信息，格式为地址：端口号 。 |  |  |
|  |  |  |  | 地址：端口 |  |
| VPCHost | String | dts-cn-****- vpc.aliyuncs.com:1 8003 | 订阅实例的专有网络VPC（Virtual Private Cloud）连接信息，格式为地址：端口号 。 |  |  |
| SubscriptionIn stanceID | String | rm- bp1162kryivb8**** | 数据订阅实例ID。 |  |  |
| SubscriptionIn stanceName | String | api测试 | 数据订阅实例名称。 |  |  |
| SubscriptionO bject | Array of SynchronousO bject |  | 订阅对象。 |  |  |
| SynchronousO bject |  |  |  |  |  |
| DatabaseNam e | String | dtstestdata | 订阅对象所属数据库的名称。 |  |  |
| TableList | List | test1 | 订阅对象的表名。 |  |  |
| WholeDatabas e | String | false | 是否订阅整库，返回值： true：是。 false：否。 |  |  |
| Success | String | true | 请求是否成功。 |  |  |

| uncs.co | 号 |
|---|---|

| s.com: | 号 |
|---|---|

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSubscriptionInstanceStatus &SubscriptionInstanceId=dtsy0zz3t13h7d****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<DescribeSubscriptionInstanceStatusResponse>
      <Status>Normal</Status>
      <TaskId>y0zz3t13h7d****</TaskId>
      <RequestId>E0845D0A-6D36-4EEB-BE26-CF191E1A****</RequestId>
      <SubscriptionHost>
            <PublicHost>dts-cn-****.aliyuncs.com:18001</PublicHost>
            <PrivateHost>dts-cn-****-internal.aliyuncs.com:18002</PrivateHost>
            <VPCHost>dts-cn-****-vpc.aliyuncs.com:18003</VPCHost>
      </SubscriptionHost>
      <EndTimestamp>2021-03-26T14:03:21Z</EndTimestamp>
      <PayType>PrePaid</PayType>
      <SubscriptionInstanceID>dtsy0zz3t13h7d****</SubscriptionInstanceID>
      <Success>true</Success>
      <SubscriptionObject>
            <SynchronousObject>
                  <DatabaseName>dtstestdata</DatabaseName>
                  <WholeDatabase>false</WholeDatabase>
                  <TableList>
                        <Table>test1</Table>
                  </TableList>
            </SynchronousObject>
      </SubscriptionObject>
      <SubscriptionDataType>
            <DML>true</DML>
            <DDL>true</DDL>
      </SubscriptionDataType>
      <SubscriptionInstanceName>api测试</SubscriptionInstanceName>
<SubscribeTopic>cn_hangzhou_rm_bp1162kryivb8****_dtstest_version2</SubscribeTopic>
      <SourceEndpoint>
            <InstanceID>rm-bp1162kryivb8****</InstanceID>
            <InstanceType>RDS</InstanceType>
      </SourceEndpoint>
      <BeginTimestamp>2021-03-15T08:25:34Z</BeginTimestamp>
</DescribeSubscriptionInstanceStatusResponse>
```

`JSON` 格式数据传输

```json
{
 "Status": "Normal",
 "TaskId": "y0zz3t13h7d****",
 "RequestId": "E0845D0A-6D36-4EEB-BE26-CF191E1A****",
 "SubscriptionHost": {
  "PublicHost": "dts-cn-****.aliyuncs.com:18001",
  "PrivateHost": "dts-cn-****-internal.aliyuncs.com:18002",
  "VPCHost": "dts-cn-****-vpc.aliyuncs.com:18003"
 },
 "EndTimestamp": "2021-03-26T14:03:21Z",
 "PayType": "PrePaid",
 "SubscriptionInstanceID": "dtsy0zz3t13h7d****",
 "Success": true,
 "SubscriptionObject": {
  "SynchronousObject": [
   {
    "DatabaseName": "dtstestdata",
    "WholeDatabase": false,
    "TableList": {
     "Table": [
      "test1"
```

]

```
    }
   }
```

]

```json
 },
 "SubscriptionDataType": {
  "DML": true,
  "DDL": true
 },
 "SubscriptionInstanceName": "api测试",
 "SubscribeTopic": "cn_hangzhou_rm_bp1162kryivb8****_dtstest_version2",
 "SourceEndpoint": {
  "InstanceID": "rm-bp1162kryivb8****",
  "InstanceType": "RDS"
 },
 "BeginTimestamp": "2021-03-15T08:25:34Z"
}
```

##### 释放订阅实例

调用DeleteSubscriptionInstance接口释放数据订阅实例。 数据订阅实例一旦释放将无法找回。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | DeleteSubscripti onInstance | 系统规定参数，取值：DeleteSubscriptionInstance。 |
|---|---|---|---|---|
| SubscriptionInst anceId | String | 是 | dtsmxg11pfp23 1**** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | C306C198-7807- 409D-930A- D6CE6C32**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DeleteSubscriptionInstance &SubscriptionInstanceId=dtsmxg11pfp231****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteSubscriptionInstanceResponse>
      <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId>
      <Success>true</Success>
</DeleteSubscriptionInstanceResponse>
```

`JSON` 格式数据传输

```json
{
 "RequestId": "C306C198-7807-409D-930A-D6CE6C32****",
 "Success": true
}
```

#### 网络设置

##### 查询DTS的IP地址

如果**源或目标实例**是**本地自建数据库**，您需要调用该接口查询DTS服务的IP地址，然后将查询所得的IP地址添加至源或目标实例的安全设置（通常为您自建数据库的防火墙）中。 如果**源或目标数据库**是**阿里云数据库实例**（例如RDS、MongoDB等）或**ECS****上的自建数**

**说明**

**据库**，在配置源或目标实例信息时，如您点击**授权白名单并进入下一步**，DTS会自动添加对应的IP地
址，您无需手动添加。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDTSIP | 系统规定参数，取值：DescribeDTSIP。 |
| SourceEndpoint Region | String | 是 | cn-hangzhou | 源实例所属地域ID。 说明如果源实例为有公网IP 的自建数据库，则可以传入cn- hangzhou或者离自建数据库物理距离最近的区域ID。 |
| RegionId | String | 否 | cn-hangzhou | DTS任务实例所在地域。 |
| DestinationEndp ointRegion | String | 否 | cn-hangzhou | 目标实例所属地域ID。 说明如果目标实例为有公网 IP的自建数据库，则可以传入cn- hangzhou或者离自建数据库物理距离最近的区域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| DynamicCode | String | 500 | 服务内部错误码，该参数即将下线。 |
|---|---|---|---|
| DynamicMess age | String | 10.151.12.0/24,47. 102.181.0/24,47.1 01.109.0/24,120.5 5.129.0/24,11.115. 103.0/24,47.102.2 34.0/24 | DTS服务的IP地址。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 0C99C0BE-F312- 40FA-ADFA- 4DC1166B**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeDTSIP &SourceEndpointRegion=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDTSIPResponse>
      <RequestId>0C99C0BE-F312-40FA-ADFA-4DC1166B****</RequestId>
<DynamicMessage>10.151.12.0/24,47.102.181.0/24,47.101.109.0/24,120.55.129.0/24,11.115.103 /24,47.102.234.0/24</DynamicMessage>
      <ErrMessage></ErrMessage>
      <Success>true</Success>
      <ErrCode></ErrCode>
</DescribeDTSIPResponse>
```

`JSON` 格式数据传输

```json
{
 "RequestId": "0C99C0BE-F312-40FA-ADFA-4DC1166B****",
 "DynamicMessage":
"10.151.12.0/24,47.102.181.0/24,47.101.109.0/24,120.55.129.0/24,11.115.103.0/24,47.102.23 0/24",
 "ErrMessage": "",
 "Success": true,
 "ErrCode": ""
}
```

##### 查询源库和目标库的连通性

调用DescribeConnectionStatus查询DTS服务器与源库和目标库的连通性。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeConnec tionStatus | 系统规定参数，取值：DescribeConnectionStatus。 |
| DestinationEndp ointArchitecture | String | 是 | testsid | 当SourceEndpointEngineName为 Oracle时，才需要传入本参数，取值为： SID：非集群架构。 RAC：集群架构。 说明该参数的类型应为 String，且为非必填参数。 |

数据传输

| DestinationEndp ointInstanceTyp e | String | 是 | PolarDB o _ | 目标库的实例类型，取值： 说明 ECS：ECS上的自建数据库。 LocalInstance：有公网IP 的自建数据库。 RDS：阿里云RDS实例。 DRDS：阿里云PolarDB-X 实例。 MongoDB：阿里云 MongoDB实例。 Redis：阿里云Redis实例。 PetaData：阿里云 HybridDB for MySQL实例。 POLARDB：阿里云 PolarDB MySQL集群。 PolarDB o：阿里云 _ PolarDB O引擎集群。 AnalyticDB：阿里云云原生数据仓库AnalyticDB MySQL 3.0和2.0版本。 Greenplum：阿里云云原生数据仓库AnalyticDB PostgreSQL。 |
|---|---|---|---|---|
| DestinationEndp ointOracleSID | String | 是 | testsid | 当DestinationEndpointEngineNa me为Oracle时，才需要传入本参数，取值为： SID：非集群架构。 RAC：集群架构。 说明该参数的类型应为 String，且为非必填参数。 |
| SourceEndpoint Architecture | String | 是 | SID | 当SourceEndpointEngineName为 Oracle时，才需要传入本参数，取值为： SID：非集群架构。 RAC：集群架构。 说明该参数为非必填参数。 |

数据传输

| SourceEndpointI nstanceType | String | 是 | RDS | 源实例类别： RDS ：RDS实例。 LocalInstance：本地自建数据库。 ECS：ECS上的自建数据库。 Express：通过专线接入的自建数据库。 dg：通过DG网关接入的数据库。 MongoDB：阿里云MongoDB实例。 POLARDB：阿里云PolarDB MySQL 集群。 PolarDB o：阿里云PolarDB O引擎 _ 集群。 |
|---|---|---|---|---|
| SourceEndpointI nstanceID | String | 否 | rm- bp1imrtn6fq7h* *** | 源实例ID。 |
| SourceEndpointE ngineName | String | 否 | MySQL | 源实例数据库引擎类型，取值包括：MySQL、TiDB、SQLServer、P ostgreSQL、Oracle、MongoDB、R edis。 说明默认取值为MySQL。 |
| SourceEndpoint Region | String | 否 | cn-hangzhou | 源实例所属地域。 |
| SourceEndpointI P | String | 否 | 172.16.88.*** | 源库的连接地址。 说明当SourceEndpointInstanceTy pe取值为LocalInstance或Express时， 本参数才可用且必须传入。 |
| SourceEndpointP ort | String | 否 | 3306 | 源库的服务端口。 说明当SourceEndpointInstanceTy pe取值为ECS、LocalInstance或Expre ss时，本参数才可用且必须传入。 |
| SourceEndpoint OracleSID | String | 否 | testsid | Oracle数据库的SID信息。 说明当SourceEndpointEngineNam e取值为Oracle，且Oracle数据库为非RAC实例时，本参数才可用且必须传入。 |

数据传输

| SourceEndpoint DatabaseName | String | 否 | dtstestdata | 待迁移的数据库名称或鉴权数据库名称。 说明当SourceEndpointEngi neName取值为PostgreSQL或Mongo DB，或者SourceEndpointInsta nceType为PolarDB o时 _ ，本参数才可用且必须传入。 当SourceEndpointEngi neName取值为PostgreSQL或DRDS时 ，传入待迁移的数据库名称；取值为MongoDB时， 传入数据库账号的鉴权数据库名称。 当SourceEndpointInsta nceType取值为PolarDB o时，传入待迁 _ 移的数据库名称。 |
|---|---|---|---|---|
| SourceEndpoint UserName | String | 否 | dtstest | 源库的数据库账号。 说明迁移或同步不同的数据库所需的权限有所差异。 |
| SourceEndpointP assword | String | 否 | Test123456 | 源库数据库账号的密码。 |
| DestinationEndp ointInstanceID | String | 否 | testsid | 目标实例ID。 |
| DestinationEndp ointEngineName | String | 否 | MySQL | 目标库的数据库类型。取值：MySQL、DRDS、SQLServer、P ostgreSQL、PPAS、MongoDB或Re dis。 说明当DestinationEndpointInstan ceType取值为RDS、DRDS、ECS、LocalIns tance或Express时，本参数才可用且必须传入。 |
| DestinationEndp ointRegion | String | 否 | cn-hangzhou | 目标实例所属地域。 |

数据传输

| DestinationEndp ointIP | String | 否 | 172.16.88.*** | 目标库连接地址。 说明当DestinationEndpointInstan ceType取值为LocalInstance或Express时， 本参数才可用且必须传入。 |
|---|---|---|---|---|
| DestinationEndp ointPort | String | 否 | 3306 | 源库的服务端口。 说明当SourceEndpointInstanceTy pe取值为ECS、LocalInstance或Expre ss时，本参数才可用且必须传入。 |
| DestinationEndp ointDatabaseNa me | String | 否 | dtstestdata | 待迁入的数据库名称或鉴权数据库名称。 说明当DestinationEndpoint EngineName取值为PostgreSQL、DRDS或 MongoDB时，或者DestinationEndpoint InstanceType取值为PolarDB o时，本参数才 _ 可用且必须传入。 当DestinationEndpoint EngineName取值为PostgreSQL或DRDS时 ，传入待迁移的数据库名称；取值为MongoDB时， 传入数据库账号的鉴权数据库名称。 当DestinationEndpoint InstanceType取值为PolarDB o时，传入待迁 _ 移的数据库名称。 |
| DestinationEndp ointUserName | String | 否 | dtstest | 目标库的数据库账号。 说明迁移或同步不同的数据库所需的权限有所差异。 |
| DestinationEndp ointPassword | String | 否 | Test123456 | 目标库数据库账号的密码。 |
| RegionId | String | 否 | cn-hangzhou | DTS实例所在地域。 |

**返回数据**

数据传输

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DestinationCo nnectionStatus | Map | { "connectDetail": [ { "testName": "PolarDB o JDBC _ Connect", "testSuccess": true }, { "testName": "Ping ", "testSuccess": true }, { "testName": "Telnet ", "testSuccess": true } ], "connectRes": true, "connectAdvice": "" } | 目标库测试连接结果。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 0A47C784-70EF- 4111-8677- 369CAA00**** | 请求ID。 |
| SourceConnec tionStatus | Map | { "connectDetail": [ { "testName": "Oracle JDBC Connect", "testSuccess": true }, { "testName": "Ping ", "testSuccess": false }, { "testName": "Telnet ", "testSuccess": true } ], "connectRes": true, "connectAdvice": "" } | 源库测试连接结果。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeConnectionStatus &DestinationEndpointArchitecture=SID &DestinationEndpointInstanceType=PolarDB_o &DestinationEndpointOracleSID=testsid &SourceEndpointArchitecture=SID &SourceEndpointInstanceType=RDS
```

`&<`公共请求参数> 数据传输正常返回示例 `XML` 格式

```xml
<DescribeConnectionStatusResponse>
      <RequestId>0A47C784-70EF-4111-8677-369CAA00****</RequestId>
      <SourceConnectionStatus>
            <connectDetail>
                  <testName>Oracle JDBC Connect</testName>
                  <testSuccess>true</testSuccess>
            </connectDetail>
            <connectDetail>
                  <testName>Ping </testName>
                  <testSuccess>false</testSuccess>
            </connectDetail>
            <connectDetail>
                  <testName>Telnet </testName>
                  <testSuccess>true</testSuccess>
            </connectDetail>
            <connectRes>true</connectRes>
            <connectAdvice></connectAdvice>
      </SourceConnectionStatus>
      <DestinationConnectionStatus>
            <connectDetail>
                  <testName>PolarDB_o JDBC Connect</testName>
                  <testSuccess>true</testSuccess>
            </connectDetail>
            <connectDetail>
                  <testName>Ping </testName>
                  <testSuccess>true</testSuccess>
            </connectDetail>
            <connectDetail>
                  <testName>Telnet </testName>
                  <testSuccess>true</testSuccess>
            </connectDetail>
            <connectRes>true</connectRes>
            <connectAdvice></connectAdvice>
      </DestinationConnectionStatus>
      <Success>true</Success>
</DescribeConnectionStatusResponse>
```

`JSON` 格式数据传输

```json
{
  "RequestId": "0A47C784-70EF-4111-8677-369CAA00****",
  "SourceConnectionStatus": {
    "connectDetail": [
      {
        "testName": "Oracle JDBC Connect",
        "testSuccess": true
      },
      {
        "testName": "Ping ",
        "testSuccess": false
      },
      {
        "testName": "Telnet ",
        "testSuccess": true
      }
```

`],`

```json
    "connectRes": true,
    "connectAdvice": ""
  },
  "DestinationConnectionStatus": {
    "connectDetail": [
      {
        "testName": "PolarDB_o JDBC Connect",
        "testSuccess": true
      },
      {
        "testName": "Ping ",
        "testSuccess": true
      },
      {
        "testName": "Telnet ",
        "testSuccess": true
      }
```

`],`

```json
    "connectRes": true,
    "connectAdvice": ""
  },
  "Success": true
}
```

#### 监控报警

##### 配置迁移实例的监控报警

调用ConfigureMigrationJobAlert接口配置监控报警，来监控迁移实例的延迟和异常状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | ConfigureMigrati onJobAlert | 系统规定参数，取值：ConfigureMigrationJobAlert。 |
|---|---|---|---|---|
| MigrationJobId | String | 是 | dtslb9113qq11n **** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据迁移实例所在地域的ID。 |
| DelayAlertStatus | String | 否 | enable | 是否监控延迟状态，取值： enable：是。 disable：否。 说明默认取值为enable。 本参数和ErrorAlertStatus参数两者中至少传入一个。 |
| DelayAlertPhone | String | 否 | 1361234****,13 71234**** | 延迟报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |
| ErrorAlertStatus | String | 否 | enable | 是否监控异常状态，取值： enable：是。 disable：否。 说明默认取值为enable。 本参数和DelayAlertStatus参数两者中至少传入一个。 开启监控异常状态功能后， 如果检测到异常，将触发报警。 |

数据传输

| ErrorAlertPhone | String | 否 | 1361234****,13 71234**** | 异常报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |
|---|---|---|---|---|
| DelayOverSecon ds | String | 否 | 10 | 触发延迟报警的阈值，单位为秒且需为整数，可根据业务需要设置阈值，建议设置 10秒以上，避免因网络、数据库负载等原因导致的延迟波动。 说明当DelayAlertStatus取值为enable时，本参数必须传入。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| RequestId | String | 0a2a04751605197 3705541561d**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ConfigureMigrationJobAlert &MigrationJobId=dtslb9113qq11n**** &DelayAlertStatus=enable &DelayOverSeconds=10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<ConfigureMigrationJobAlertResponse>
      <RequestId>0a2a047516051973705541561d****</RequestId>
      <Success>true</Success>
</ConfigureMigrationJobAlertResponse>
```

`JSON` 格式

```json
{
 "RequestId": "0a2a047516051973705541561d****",
 "Success": true
}
```

##### 查询迁移实例的监控报警

调用DescribeMigrationJobAlert接口查询迁移实例的监控报警设置详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMigrati onJobAlert | 系统规定参数，取值：DescribeMigrationJobAlert。 |
| MigrationJobId | String | 是 | dtslb9113qq11n **** | 数据迁移实例ID，可以通过调用DescribeMigrationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCz**** | 用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DelayAlertPho ne | String | 1361234****,1371 234**** | 延迟报警的联系人手机号码。 |
| DelayAlertStat us | String | enable | 是否监控延迟状态，返回值： enable：是。 disable：否。 |

数据传输

| ErrorAlertPhon e | String | 1361234****,1371 234**** | 异常报警的联系人手机号码。 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| DelayOverSec onds | String | 10 | 触发延迟报警的阈值，单位为秒。 |
| ErrorAlertStatu s | String | enable | 是否监控异常状态，返回值： enable：是。 disable：否。 |
| MigrationJobId | String | lb9113qq11n**** | 数据迁移实例ID。 |
| MigrationJobN ame | String | PolarDB MySQL to RDS _ _ MySQL | 数据迁移任务名称。 |
| RequestId | String | 210ec2191605518 7057342533d**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeMigrationJobAlert &MigrationJobId=dtslb9113qq11n****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeMigrationJobAlertresponse>
      <RequestId>210ec21916055187057342533d****</RequestId>
      <DelayAlertPhone>1361234****,1371234****</DelayAlertPhone>
      <ErrorAlertStatus>enable</ErrorAlertStatus>
      <MigrationJobName>PolarDB MySQL_to_RDS MySQL</MigrationJobName>
      <DelayAlertStatus>enable</DelayAlertStatus>
      <DelayOverSeconds>10</DelayOverSeconds>
      <Success>true</Success>
      <MigrationJobId>lb9113qq11n****</MigrationJobId>
</DescribeMigrationJobAlertresponse>
```

`JSON` 格式数据传输

```json
{
 "RequestId": "210ec21916055187057342533d****",
 "DelayAlertPhone": "1361234****,1371234****",
    "ErrorAlertStatus": "enable",
 "MigrationJobName": "PolarDB MySQL_to_RDS MySQL",
 "DelayAlertStatus": "enable",
 "DelayOverSeconds": "10",
 "Success": true,
 "MigrationJobId": "lb9113qq11n****"
}
```

##### 配置订阅实例的监控报警

调用ConfigureSubscriptionInstanceAlert接口配置监控报警，来监控订阅实例的延迟和异常状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ConfigureSubscr iptionInstanceAl ert | 系统规定参数，取值：ConfigureSubscriptionInstanc eAlert。 |
| SubscriptionInst anceId | String | 是 | dtsl8zl9ek6292* *** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| DelayAlertStatus | String | 否 | enable | 是否监控延迟状态，取值： enable：是。 disable：否。 说明默认取值为enable。 本参数和ErrorAlertStatus参数两者中至少传入一个。 |

数据传输

| DelayAlertPhone | String | 否 | 1361234****,13 71234**** | 延迟报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |
|---|---|---|---|---|
| ErrorAlertStatus | String | 否 | enable | 是否监控异常状态，取值： enable：是。 disable：否。 说明默认取值为enable。 本参数和DelayAlertStatus参数两者中至少传入一个。 开启监控异常状态功能后， 如果检测到异常，将触发报警。 |
| ErrorAlertPhone | String | 否 | 1361234****,13 71234**** | 异常报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |
| DelayOverSecon ds | String | 否 | 10 | 触发延迟报警的阈值，单位为秒且需为整数，可根据业务需要设置阈值，建议设置 10秒以上，避免因网络、数据库负载等原因导致的延迟波动。 说明当DelayAlertStatus取值为enable时，本参数必须传入。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | InternalError The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| RequestId | String | 0a2a04751605197 3705541561d**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSubscriptionInstanceAlert &SubscriptionInstanceId=dtsl8zl9ek6292**** &DelayAlertStatus=enable &DelayAlertPhone=1361234****,1371234**** &DelayOverSeconds=10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ConfigureSubscriptionInstanceAlertResponse>
      <RequestId>0a2a047516051973705541561d****</RequestId>
      <Success>true</Success>
</ConfigureSubscriptionInstanceAlertResponse>
```

`JSON` 格式

```json
{
 "RequestId": "0a2a047516051973705541561d****",
 "Success": true
}
```

##### 查询订阅实例的监控报警

调用DescribeSubscriptionInstanceAlert接口查询数据订阅实例的监控报警设置详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | DescribeSubscri ptionInstanceAle rt | 系统规定参数，取值：DescribeSubscriptionInstance Alert。 |
|---|---|---|---|---|
| SubscriptionInst anceId | String | 是 | dtsl8zl9ek6292* *** | 数据订阅实例ID，可以通过调用 DescribeSubscriptionInstances接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 数据订阅实例所在地域的ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCz**** | 用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DelayAlertPho ne | String | 1361234****,1371 234**** | 延迟报警的联系人手机号码。 |
| DelayAlertStat us | String | enable | 是否监控延迟状态，返回值： enable：是。 disable：否。 |
| DelayOverSec onds | String | 10 | 触发延迟报警的阈值，单位为秒且需为整数，建议取值为10秒。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| ErrorAlertPhon e | String | 1361234****,1371 234**** | 异常报警的联系人手机号码。 |
| ErrorAlertStatu s | String | enable | 是否监控异常状态，返回值： enable：是。 disable：否。 |

数据传输

| RequestId | String | 210ec2e11605519 8849072222d**** | 请求ID。 |
|---|---|---|---|
| SubscriptionIn stanceID | String | dtsl8zl9ek6292**** | 数据订阅实例ID。 |
| SubscriptionIn stanceName | String | test | 数据订阅实例名称。 |
| Success | String | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSubscriptionInstanceAlert &SubscriptionInstanceId=dtsl8zl9ek6292****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSubscriptionInstanceAlertResponse>
      <SubscriptionInstanceName>test</SubscriptionInstanceName>
      <RequestId>210ec2e116055198849072222d****</RequestId>
      <DelayAlertPhone>1361234****,1371234****</DelayAlertPhone>
      <ErrorAlertStatus>enable</ErrorAlertStatus>
      <DelayAlertStatus>enable</DelayAlertStatus>
      <DelayOverSeconds>10</DelayOverSeconds>
      <Success>true</Success>
</DescribeSubscriptionInstanceAlertResponse>
```

`JSON` 格式

```json
{
 "SubscriptionInstanceName": "test",
 "RequestId": "210ec2e116055198849072222d****",
 "DelayAlertPhone": "1361234****,1371234****",
 "ErrorAlertStatus": "enable",
 "DelayAlertStatus": "enable",
 "DelayOverSeconds": "10",
 "Success": true
}
```

##### 配置同步实例的监控报警

您可以调用ConfigureSynchronizationJobAlert接口配置监控报警，来监控同步实例的延迟和异常状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

数据传输

| Action | String | 是 | ConfigureSynchr onizationJobAler t | 系统规定参数，取值：ConfigureSynchronizationJob Alert。 |
|---|---|---|---|---|
| SynchronizationJ obId | String | 是 | dtskxz1170c10p **** | 数据同步实例ID，可以通过调用 DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 |
| DelayAlertStatus | String | 否 | enable | 是否监控延迟状态，取值： enable：是。 disable：否。 说明默认取值为enable。 本参数和ErrorAlertStatus参数两者中至少传入一个。 |
| DelayAlertPhone | String | 否 | 1361234****,13 71234**** | 延迟报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |

数据传输

| ErrorAlertStatus | String | 否 | enable | 是否监控异常状态，取值： enable：是。 disable：否。 说明默认取值为enable。 本参数和DelayAlertStatus参数两者中至少传入一个。 开启监控异常状态功能后， 如果检测到异常，将触发报警。 |
|---|---|---|---|---|
| ErrorAlertPhone | String | 否 | 1361234****,13 71234**** | 异常报警的联系人手机号码，多个手机号码以英文逗号（,）分隔。 说明本参数目前只支持中国站， 仅支持大陆手机号码，且最多传入10个手机号码。 国际站不支持手机告警，仅支持通过云监控平台为DTS 任务设置报警规则。 |
| DelayOverSecon ds | String | 否 | 10 | 触发延迟报警的阈值，单位为秒且需为整数，可根据业务需要设置阈值，建议设置 10秒以上，避免因网络、数据库负载等原因导致的延迟波动。 说明当DelayAlertStatus取值为enable时，本参数必须传入。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| RequestId | String | 8EEE7858-7D41- 4EDF-9435- AEED2A34**** | 请求ID。 |

数据传输

| Success | String | true | 请求是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSynchronizationJobAlert &SynchronizationJobId=dtskxz1170c10p**** &DelayAlertStatus=enable &DelayAlertPhone=1361234****,1371234**** &DelayOverSeconds=10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ConfigureSynchronizationJobAlertResponse>
      <RequestId>8EEE7858-7D41-4EDF-9435-AEED2A34****</RequestId>
      <Success>true</Success>
</ConfigureSynchronizationJobAlertResponse>
```

`JSON` 格式

```json
{
 "RequestId": "8EEE7858-7D41-4EDF-9435-AEED2A34****",
 "Success": true
}
```

##### 查询同步实例的监控报警

调用DescribeSynchronizationJobAlert接口查询同步实例的监控报警设置详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSynchro nizationJobAlert | 系统规定参数，取值：DescribeSynchronizationJobA lert。 |
| SynchronizationJ obId | String | 是 | dtskxz1170c10p **** | 数据同步实例ID，可以通过调用DescribeSynchronizationJobs接口查询。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，传入本参数来指定订阅通道所在地域。 |

数据传输

| Synchronization Direction | String | 否 | Forward | 同步方向，取值： Forward：正向。 Reverse：反向。 说明默认取值为Forward。 |
|---|---|---|---|---|
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCz**** | 用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。 |
| AccountId | String | 否 | 12323344**** | 阿里云主账号ID，无需设置，该参数即将下线。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DelayAlertPho ne | String | 1361234****,1371 234**** | 延迟报警的联系人手机号码。 |
| DelayAlertStat us | String | enable | 是否监控延迟状态，返回值： enable：是。 disable：否。 |
| DelayOverSec onds | String | 10 | 触发延迟报警的阈值，单位为秒。 |
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用出错时返回的错误信息。 |
| ErrorAlertPhon e | String | 1361234****,1371 234**** | 异常报警的联系人手机号码。 |
| ErrorAlertStatu s | String | enable | 是否监控异常状态，返回值： enable：是。 disable：否。 |
| RequestId | String | 210ec20e1605520 5968635339d**** | 请求ID。 |
| Success | String | true | 请求是否成功。 |

数据传输

| Synchronizatio nDirection | String | Forward | 同步方向，返回值： Forward：正向。 Reverse：反向。 说明只有在数据同步的拓扑为双向同步时，才会返回该参数。 |
|---|---|---|---|
| Synchronizatio nJobId | String | kxz1170c10p**** | 数据同步实例ID。 |
| Synchronizatio nJobName | String | Polar MySQL TO RDS _ _ MySQL | 数据同步作业名称。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobAlert &SynchronizationJobId=dtskxz1170c10p****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSynchronizationJobAlertresponse>
      <SynchronizationJobId>kxz1170c10p****</SynchronizationJobId>
      <RequestId>210ec20e16055205968635339d****</RequestId>
      <SynchronizationJobName>Polar MySQL_TO_RDS MySQL</SynchronizationJobName>
      <DelayAlertPhone>1361234****,1371234****</DelayAlertPhone>
      <ErrorAlertStatus>enable</ErrorAlertStatus>
      <DelayAlertStatus>enable</DelayAlertStatus>
      <DelayOverSeconds>10</DelayOverSeconds>
      <Success>true</Success>
</DescribeSynchronizationJobAlertresponse>
```

`JSON` 格式

```json
{
 "SynchronizationJobId": "kxz1170c10p****",
 "RequestId": "210ec20e16055205968635339d****",
 "SynchronizationJobName": "Polar MySQL_TO_RDS MySQL",
    "DelayAlertPhone": "1361234****,1371234****",
 "ErrorAlertStatus": "enable",
 "DelayAlertStatus": "enable",
 "DelayOverSeconds": "10",
 "Success": true
}
```

数据传输

#### 任务管理

##### 屏蔽预检查告警项

调用ShieldPrecheck屏蔽迁移或同步时导致预检查失败的告警项。 成功调用该接口屏蔽所有预检查失败的告警项后，您需要调用StartMigrationJob和 StartSynchronizationJob接口，DTS将重新进入预检查状态，成功通过预检查后，将自动开启迁移或同步任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ShieldPrecheck | 系统规定参数，取值：ShieldPrecheck。 |
| DtsInstanceId | String | 是 | dtsi76118o3w92 **** | 数据迁移或同步实例ID，可以通过调用DescribeMigrationJobs、 DescribeSynchronizationJobs接口查询。 |
| PrecheckItems | String | 是 | CHECK SAME O _ _ BJ | 预检查项，取值如下，多个预检查项以英文逗号（,）分隔。 CHECK SAME OBJ：同名对象存在 _ _ 性检查。 CHECK SAME USER：不同名账号 _ _ 存在性检查。 CHECK SRC：源库版本检查。 _ CHECK TOPOLOGY：拓扑版本检 _ 查。 CHECK SERVER ID：源库 _ _ server id检查。 _ |
| RegionId | String | 否 | cn-hangzhou | 实例所在地域的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | 6F4B5BC4-34B1- 49C9-9C8F- C8F16AC4**** | 请求ID。 |

数据传输

| Success | Boolean | true | 请求是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ShieldPrecheck &DtsInstanceId=dtsi76118o3w92**** &PrecheckItems=CHECK_SAME_OBJ
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ShieldPrecheck>
      <RequestId>6F4B5BC4-34B1-49C9-9C8F-C8F16AC4****</RequestId>
      <Success>true</Success>
</ShieldPrecheck>
```

`JSON` 格式

```json
{
 "RequestId": "6F4B5BC4-34B1-49C9-9C8F-C8F16AC4****",
 "Success": true
}
```

#### 标签管理

##### 创建标签

调用TagResources接口为一个或多个迁移、同步和订阅实例绑定标签。 在实例数量较多的情况下，您可以创建多个标签，为实例绑定不同的标签对其进行分类，之后通过标签进行实例筛选。 标签由一对键（key）值（value）组成，键在同账号同地域下唯一，值无此限制。 若设置的标签不存在，则自动创建该标签并绑定到目标实例。 若实例已经绑定了有相同键的标签，则进行覆盖绑定。 每个实例最多可以绑定20个标签。 每次调用最多设置50个实例进行批量标签绑定。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TagResources | 系统规定参数，取值：TagResources。 |

数据传输

| RegionId | String | 是 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
|---|---|---|---|---|
| ResourceId.N | RepeatL ist | 是 | dtsntk10k6r12v* *** | 数据迁移、同步和订阅的实例ID，可以通过调用DescribeDtsJobs接口查询。 说明 N表示传入第几个实例 ID。例如ResourceId.1表示传入第一个实例ID；ResourceId.2表示传入第二个实例ID。 |
| ResourceType | String | 是 | ALIYUN::DTS::IN STANCE | 资源类型定义，固定取值为：ALIYUN::DTS::INSTANCE。 |
| Tag.N.Key | String | 是 | testkey1 | 标签的键。 说明 N表示传入第几个标签的键。 例如Tag.1.Key表示传入第一个标签的键；Tag.2.Key 表示传入第二个标签的键。 不允许传入空字符串。 |
| Tag.N.Value | String | 是 | testvalue1 | 标签的值。 说明 N表示传入第几个标签的值。 例如Tag.1.Value表示传入第一个标签的值； Tag.2.Value表示传入第二个标签的值。 允许传入空字符串。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |

数据传输

| RequestId | String | 755D7B84-6813- 42B0-BC9D- 2699CFEA**** | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=TagResources &RegionId=cn-hangzhou &ResourceId.1=dtsntk10k6r12v**** &ResourceType=ALIYUN::DTS::INSTANCE &Tag.1.Key=testkey1 &Tag.1.Value=testvalue1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TagResourcesResponse>
      <RequestId>755D7B84-6813-42B0-BC9D-2699CFEA****</RequestId>
      <Success>true</Success>
</TagResourcesResponse>
```

`JSON` 格式

```json
{
    "RequestId": "755D7B84-6813-42B0-BC9D-2699CFEA****",
    "Success": true
}
```

##### 查询标签

调用ListTagResources查询迁移、同步和订阅实例绑定的标签，也可以查询标签所绑定的实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTagResource s | 系统规定参数，取值：ListTagResources。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |
| ResourceType | String | 是 | ALIYUN::DTS::IN STANCE | 资源类型定义，取值固定为：ALIYUN::DTS::INSTANCE。 |

数据传输

| NextToken | String | 否 | 212db86sca438 4811e0b5e8707 ec2**** | 查询凭证。 说明如果一次查询没有返回全部结果，则可在后续查询中传入上一次查询返回的NextToken参数继续查询。 |
|---|---|---|---|---|
| ResourceId.N | RepeatL ist | 否 | dtsntk10k6r12v* *** | 数据迁移、同步和订阅的实例ID。 说明 N表示传入第几个实例ID。例如：ResourceId.1表示传入第一个实例ID； ResourceId.2表示传入第二个实例ID。可以同时查询 1~50个实例ID。 该参数和Tag.N.Key参数至少传入一个。 |
| Tag.N.Key | String | 否 | testkey1 | 标签键。 说明 N表示传入第几个标签的键。 例如：Tag.1.Key表示传入第一个标签的键； Tag.2.Key表示传入第二个标签的键。可以同时查询 1~20个标签键。 该参数和ResourceId.N参数至少传入一个，且传入时不允许传入空字符串。 |
| Tag.N.Value | String | 否 | testvalue1 | 标签的值。 说明 N表示传入第几个标签的值。 例如：Tag.1.Value表示传入第一个标签的值； Tag.2.Value表示传入第二个标签的值。可以同时查询 1~20个标签值。 允许传入空字符串。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

数据传输

| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| NextToken | String | 212db86sca43848 11e0b5e8707ec2** ** | 查询凭证。 说明如果此次查询没有返回全部结果，则可在后续查询中传入此NextToken参数继续查询。 |
| RequestId | String | 609AD332-F2B1- 48B7-BF43- 41FEE641**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| TagResources | Array of TagResource |  | 返回标签集合。 |
| TagResource |  |  |  |
| ResourceId | String | dtsntk10k6r12v*** * | 实例ID。 |
| ResourceType | String | ALIYUN::DTS::INST ANCE | 资源类型定义，取值固定为ALIYUN::DTS::INSTANCE。 |
| TagKey | String | testkey1 | 标签键。 |
| TagValue | String | testvalue1 | 标签键对应的标签值。 |

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=ListTagResources &RegionId=cn-hangzhou &ResourceType=ALIYUN::DTS::INSTANCE &ResourceId.1=dtsntk10k6r12v**** &Tag.1.Key=testkey1 &Tag.1.Value=testvalue1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式数据传输

```xml
<ListTagResourcesResponse>
      <RequestId>609AD332-F2B1-48B7-BF43-41FEE641****</RequestId>
      <TagResources>
            <ResourceId>dtsntk10k6r12v****</ResourceId>
            <TagKey>testkey1</TagKey>
            <ResourceType>ALIYUN::DTS::INSTANCE</ResourceType>
            <TagValue>testvalue1</TagValue>
      </TagResources>
      <Success>true</Success>
</ListTagResourcesResponse>
```

`JSON` 格式

```json
{
 "RequestId": "609AD332-F2B1-48B7-BF43-41FEE641****",
 "TagResources": [
  {
   "ResourceId": "dtsntk10k6r12v****",
   "TagKey": "testkey1",
   "ResourceType": "ALIYUN::DTS::INSTANCE",
   "TagValue": "testvalue1"
  }
```

`],`

```json
 "Success": true
}
```

##### 解绑标签

调用UntagResources接口为迁移、同步和订阅实例解绑标签。 标签从一个实例解绑后，如果没有绑定到其它实例，则该标签自动被删除。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UntagResources | 系统规定参数，取值：UntagResources。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，传入本参数来指定实例所在地域。 |

数据传输

| ResourceId.N | RepeatL ist | 是 | dtsntk10k6r12v* *** | 数据迁移、同步和订阅实例的ID，可以通过调用DescribeDtsJobs接口查询。 说明 N表示传入第几个实例 ID。例如ResourceId.1表示传入第一个实例ID；ResourceId.2表示传入第二个实例ID。可以同时对1~50 个实例解绑标签。 |
|---|---|---|---|---|
| ResourceType | String | 是 | ALIYUN::DTS::IN STANCE | 资源类型定义。唯一取值：ALIYUN::DTS::INSTANCE。 |
| TagKey.N | RepeatL ist | 否 | testkey1 | 标签键。 说明 N表示传入第几个标签的键。 例如TagKey.1表示传入第一个标签的键；TagKey.2表示传入第二个标签的键。可以同时解绑1~20个标签键。 不允许传入空字符串。 All和本参数至少传入一个。 如果同时传入了All和本参数，则只有本参数生效。 |
| All | Boolean | 否 | false | 是否解绑实例的全部标签，取值： true：是。解绑实例的全部标签。 false：否。需在TagKey.N参数传入需解绑的实例标签。 说明 TagKey.N和本参数至少传入一个。 如果同时传入了TagKey.N和本参数，则本参数不生效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InternalError | 调用出错时返回的错误码。 |
| ErrMessage | String | The request processing has failed due to some unknown error. | 调用错误时返回对应的错误信息。 |
| RequestId | String | ED3A8FE0-EEFA- 4416-BC42- 34D61A52**** | 请求ID。 |

数据传输

| Success | Boolean | true | 请求是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://dts.aliyuncs.com/?Action=UntagResources &RegionId=cn-hangzhou &ResourceId.1=dtsntk10k6r12v**** &ResourceType=ALIYUN::DTS::INSTANCE
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<UntagResourcesResponse>
      <RequestId>ED3A8FE0-EEFA-4416-BC42-34D61A52****</RequestId>
      <Success>true</Success>
</UntagResourcesResponse>
```

`JSON` 格式

```json
{
 "RequestId": "ED3A8FE0-EEFA-4416-BC42-34D61A52****",
 "Success": true
}
```

#### 参数补充说明

##### 迁移对象配置说明

在调用ConfigureMigrationJob接口时，您需要传入迁移对象参数。本文为您介绍迁移对象参数的定义和配置案例。

**相关接口**

**迁移对象定义说明**

迁移对象（MigrationObject）的取值类型为Object，支持一定的正则表达式，详细定义如下。 数据传输 [

```
    {
```

`"DBName":"`待迁移的库名`",` `"NewDBName":"`待迁移的库在目标实例中映射的库名`",` `"SchemaName":"`待迁移的`Schema`名`",` `"NewSchemaName":"`待迁移的`Schema`在目标实例中映射的`Schema`名`",`

```json
        "AllTable": false,
        "TableIncludes":[
            {
```

`"TableName":"`待迁移的表名`",` `"NewTableName":"`待迁移的表在目标实例中映射的别名`",`

```json
                "FilterCondition":"where condition",
```

`"PrimaryKey":"`待迁移表的主键列，多列用逗号分隔`",` `"PartKey":"`待迁移表的分布列，多列用逗号分隔`",`

```json
                "ColumnIncludes":[
                    {
```

`"ColumnName":"`待迁移表中需迁移列名`",` `"NewColumnName":"`待迁移的列在目标实例中映射的列名"

```
                    }
```

`],`

```json
                "ColumnExcludes":[{
```

`"ColumnName":"`待迁移表中不需要迁移的列名"

```
                }]
            }
```

`],`

```json
        "TableExcludes":[{
```

`"TableName":"`待迁移库中不需要迁移的表名"

```
        }]
    }
```

] 表 1. 补充说明

| 参数 | 说明 |
|---|---|
| SchemaName | 当源库为SQL Server或PostgreSQL时，本参数才可用且必须传入。 |
| NewSchemaName | 当目标库为SQL Server或PostgreSQL时，本参数才可用。 |
| ALLTABLE | 待迁移schema下所有表是否都需配置，默认为false，也可填true。 填写为false时，需传入参数TableIncludes和TableExcludes 填写为true时，只需传入参数TableIncludes。 |
| PrimaryKey | 当目标库为云原生数仓AnalyticDB MySQL、AnalyticDB PostgreSQL时，本参数才可用且必须传入。 |
| PartKey | 当目标库为云原生数仓AnalyticDB MySQL、AnalyticDB PostgreSQL时，本参数才可用且必须传入。 |
| ColumnName、ColNewC olumnNameumnName | 需保障源表的列名和目标表的列名的顺序一一对应，否则DTS可能找不到对应的列。 |

数据传输

| FilterCondition | 过滤条件，只有满足过滤条件的数据才会被迁移到目标数据库中。 说明过滤条件支持标准的SQL WHERE语句。 过滤条件中如需使用引号，请使用英文单引号（'），例如 address in('hangzhou','shanghai') 。 |
|---|---|

| address |  |
|---|---|

|  | in('hangzhou','shanghai') |
|---|---|

**迁移对象配置示例**

示例一：迁移dtstestdata库中所有的表。

```json
[{
    "DBName": "dtstestdata"
}]
```

示例二：将dtstestdata库中所有的表迁移至目标实例的mysqltest库中。

```json
[{
    "DBName": "dtstestdata",
    "NewDBName": "mysqltest"
}]
```

示例三：迁移dtstestdata和mysqltest库中所有的表。

```json
[{
    "DBName": "dtstestdata"
},{
    "DBName": "mysqltest"
}]
```

示例四：迁移dtstestdata库中除表名前缀为order以外的所有表。

```json
[{
    "DBName": "dtstestdata",
    "AllTable": false,
    "TableExcludes": [{
        "TableName": "order.*"
    }]
}]
```

示例六：迁移dtstestdata库中的customer表，且只迁移ID列中的值大于100的数据。

```json
[{
    "SchemaName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer",
        "FilterCondition": "id > 100"
    }]
}]
```

示例七：迁移dtstestdata库中的customer表，且只迁移表中的ID和address列。 数据传输

```json
[{
    "SchemaName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer",
        "ColumnIncludes": [{
                "ColumnName": "id"
            },
            {
                "ColumnName": "address"
            }
```

]

```
    }]
}]
```

示例八：迁移dtstestdata库中的customer表至云原生数仓AnalyticDB MySQL、AnalyticDB PostgreSQL，且源表customer在目标表中的主键、分布键设为CREATE_TIME。

```json
[{
    "SchemaName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer",
        "PrimaryKey":"CREATE_TIME",
        "PartKey":"CREATE_TIME",
    }]
}]
```

**支持的正则表达式**

| 符号 | 规则描述 |
|---|---|
| 英文句号（.） | 表示匹配除‘\r\n’之外的任何单个字符。 |
| 星号（*） | 表示匹配前面子表达式任意次，例如： h.*llo 将匹配 hllo或heeeello等字符串。 |
| 英文问号（?） | 表示匹配前面子表达式零次或1次，例如： h.?llo 将匹配hllo或hello，但不能匹配haello。 |
| [characters] 字符集合 | 表示匹配方括号内任意一个字符，例如： h[ae]llo 将匹配hallo或hello。 |
| [^characters] 负值字符集合 | 表示不匹配方括号内任意一个字符，例如： h[^ae]llo 将匹配hcllo或 hdllo，但不能匹配hallo或hello。 |
| [character1-character2] 字符范围 | 表示匹配character1-character2范围内的字符，例如： [0-9]、[a-z]。 |

##### 订阅对象配置说明

在调用ConfigureSubscriptionInstance接口时，您需要传入订阅对象参数。本文为您介绍订阅对象的定义和配置案例。

**相关接口**

数据传输

**订阅对象定义说明**

订阅对象（SubscriptionObjects）的取值类型为Object，支持一定的正则表达式，详细定义如下。

```
[{
```

`"DBName": "`待订阅的库名`",`

```json
    "TableIncludes": [{
```

`"TableName": "`待订阅的表名"

```json
    }],
    "TableExluces": [{
```

`"TableName": "`待订阅的库中不需要订阅的表名"

```
    }]
}]
```

**订阅对象配置示例**

示例一：订阅dtstestdata库中所有的表。

```json
[{
    "DBName": "dtstestdata"
}]
```

示例二：订阅dtstestdata和mysqltest库中所有的表。

```json
[{
    "DBName": "dtstestdata"
},{
    "DBName": "mysqltest"
}]
```

示例三：订阅dtstestdata库中的customer和order表。

```json
[{
    "DBName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer"
    }, {
        "TableName": "order"
    }]
}]
```

示例四：订阅dtstestdata库中除表名前缀为order以外的所有表。

```json
[{
    "DBName": "dtstestdata",
    "TableExcludes": [{
        "TableName": "order.*"
    }]
}]
```

**支持的正则表达式**

数据传输

| 符号 | 规则描述 |
|---|---|
| 英文句号（.） | 表示匹配除‘\r\n’之外的任何单个字符。 |
| 星号（*） | 表示匹配前面子表达式任意次，例如： h.*llo 将匹配 hllo或heeeello等字符串。 |
| 英文问号（?） | 表示匹配前面子表达式零次或1次，例如： h.?llo 将匹配hllo或hello，但不能匹配haello。 |
| [characters] 字符集合 | 表示匹配方括号内任意一个字符，例如： h[ae]llo 将匹配hallo或hello。 |
| [^characters] 负值字符集合 | 表示不匹配方括号内任意一个字符，例如： h[^ae]llo 将匹配hcllo或 hdllo，但不能匹配hallo或hello。 |
| [character1-character2] 字符范围 | 表示匹配character1-character2范围内的字符，例如： [0-9]、[a-z]。 |

##### 同步对象配置说明

在调用ConfigureSynchronizationJob接口或ModifySynchronizationObject接口时，您需要传入同步对象参数。本文为您介绍同步对象的定义和配置案例。

**相关接口**

**同步对象定义说明**

同步对象（SynchronizationObjects）的取值类型为Object，支持一定的正则表达式，详细定义如下所示。 数据传输

```
[{
```

`"DBName":"`待同步的库名`",` `"NewDBName":"`待同步的库在目标实例中映射的别名`",` `"SchemaName":"`待同步`Schema`名`",` `"NewSchemaName":"`待同步`Schema`在目标实例中映射的`Schema`名`",`

```json
    "AllTable": false,
    "TableIncludes":[{
```

`"TableName":"`待同步的表名`",` `"NewTableName":"`待同步的表在目标实例中映射的别名`",`

```json
    "FilterCondition":"where condition",
```

`"PrimaryKey":"`待同步表的主键列，多列用逗号分隔`",` `"PartKey":"`待同步表的分布列，多列用逗号分隔`",`

```json
    "ColumnIncludes":[{
```

`"ColumnName":"`待同步表中需同步的列名`",` `"NewColumnName":"`待同步的列在目标表中映射的列名"

```json
    }],
    "ColumnExcludes":[{
```

`"ColumnName":"`待同步表中不需要同步的列名"

```json
    }]
    }],
    "TableExcludes": [{
```

`"TableName": "`该库中不需要同步的表名"

```
    }]
}]
```

**补充说明**

| 参数 | 说明 |
|---|---|
| SchemaName | 当源库为SQL Server或PostgreSQL时，本参数才可用且必须传入。 |
| NewSchemaName | 当目标库为SQL Server或PostgreSQL时，本参数才可用。 |
| ALLTABLE | 待同步schema下所有表是否都需同步，默认为false，也可填true。 填写为false时，需传入参数TableIncludes和TableExcludes 填写为true时，只需传入参数TableIncludes。 |
| PrimaryKey | 当目标库为云原生数仓AnalyticDB MySQL、AnalyticDB PostgreSQL时，本参数才可用且必须传入。 |
| PartKey | 当目标库为云原生数仓AnalyticDB MySQL、AnalyticDB PostgreSQL时，本参数才可用且必须传入。 |
| ColumnName、NewColu mnName | 需保障源表的列名和目标表的列名的顺序一一对应，否则DTS可能找不到对应的列。 |
| FilterCondition | 过滤条件，只有满足过滤条件的数据才会被同步到目标数据库中。 说明过滤条件支持标准的SQL WHERE语句。 过滤条件中如需使用引号，请使用英文单引号（'），例如 address in('hangzhou','shanghai') 。 |

| address |  |
|---|---|

|  | in('hangzhou','shanghai') |
|---|---|

数据传输

**同步对象配置示例**

示例一：同步dtstestdata库中所有的表。

```json
[{
    "DBName": "dtstestdata"
}]
```

示例二：同步dtstestdata库中除表名前缀为order以外的所有表。

```json
[{
    "DBName": "dtstestdata",
    "AllTable": false,
    "TableExcludes": [{
        "TableName": "order.*"
    }]
}]
```

示例三：同步dtstestdata库中的customer表至云原生数仓AnalyticDB MySQL、AnalyticDB PostgreSQL，且源表customer在目标表中的主键、分布键设为CREATE_TIME。

```json
[{
    "SchemaName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer",
        "PrimaryKey":"CREATE_TIME",
        "PartKey":"CREATE_TIME",
    }]
}]
```

**支持的正则表达式**

| 符号 | 规则描述 |
|---|---|
| 英文句号（.） | 表示匹配除‘\r\n’之外的任何单个字符。 |
| 星号（*） | 表示匹配前面子表达式任意次，例如： h.*llo 将匹配 hllo或heeeello等字符串。 |
| 英文问号（?） | 表示匹配前面子表达式零次或1次，例如： h.?llo 将匹配hllo或hello，但不能匹配haello。 |
| [characters] 字符集合 | 表示匹配方括号内任意一个字符，例如： h[ae]llo 将匹配hallo或hello。 |
| [^characters] 负值字符集合 | 表示不匹配方括号内任意一个字符，例如： h[^ae]llo 将匹配hcllo或 hdllo，但不能匹配hallo或hello。 |

数据传输

| [character1-character2] 字符范围 | 表示匹配character1-character2范围内的字符，例如： [0-9]、[a-z]。 |
|---|---|

##### MigrationReserved参数说明

在调用ConfigureMigrationJob或ConfigureSynchronizationJob接口配置任务时，您可以传入本参数实现特殊需求（例如是否自动启动预检查）。

**注意事项**

如需正常使用该参数，您需要使用最新版本的SDK，详情请参见： Java SDK：快速开始 Python SDK：快速开始 Go SDK：快速开始

**相关接口**

**MigrationReserved定义说明**

MigrationReserved（DTS预留参数）的取值类型为String，传入数据的格式为JSON，详细定义如下所示。

| 参数 | 适用的接口 | 说明 |
|---|---|---|
| autoStartModules AfterConfig | 配置迁移实例配置同步实例 | 启动控制参数，取值： all：完成DTS任务的配置后，自动启动预检查模块及其后续所有模块。 none：完成DTS任务的配置后，不启动预检查等模块，即需要手动启动任务。 默认值为all。 |
| targetTableMode | 配置迁移实例配置同步实例 | 同名对象存在性检查，取值： 0：报错并拦截。 2：忽略报错并继续执行。 |
| srcRedisType | 配置同步实例 | 取值固定为enterprise：阿里云Redis企业版实例。 说明本参数仅在Redis企业版实例间的数据同步场景下适用。 |
| destRedisType |  |  |

**请求示例**

```json
{
  "autoStartModulesAfterConfig": "none",
  "targetTableMode": 2
}
```

数据传输

## 附录

### STS概要

#### 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

**使用RAM用户扮演角色时获取STS Token**

有权限的RAM用户可以使用其访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用STS Token访问阿里云资源。

**产品优势**

使用STS Token，减少长期访问密钥（Accesskey）泄露的风险。 STS Token具有时效性，可以自定义有效期，到期后将自动失效，无需定期轮换。 可以为STS Token绑定自定义权限策略，提供更加灵活和精细的云资源授权。

#### AssumeRole

RAM用户调用AssumeRole接口获取一个扮演RAM角色的临时身份凭证（STS Token）。该接口中RAM用户扮演的是可信实体为阿里云账号类型的RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssumeRole | 要执行的操作。取值：AssumeRole |
| RoleArn | String | 是 | acs:ram::123456 789012****:role/ adminrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM 角色。 |
| RoleSessionNa me | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-） 和下划线（ ）。 _ |

数据传输

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 长度为1~1024个字符。 |

**返回结果**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | 无 | 无 | 访问凭证。 |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | 访问密钥ID。 |
| AccessKeySecret | String | wyLTSmsyPGP1ohv vw8xYgB29dlGI8KM iH2pK**** | 访问密钥。 |
| SecurityToken | String | ******** | 安全令牌。 |
| Expiration | String | 2015-04- 09T11:52:19Z | 失效时间。 |
| AssumedRoleUser | 无 | 无 | 角色扮演时的临时身份。 |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | 临时身份的ARN。 |
| AssumedRoleId | String | 34458433936495** **:alice | 临时身份的ID。 |

**示例**

**引入Pom依赖**

数据传输操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

以下代码示例为通过调用 `Sts::AssumeRole::2015-04-01` 获取STS AccessKey三元组信息。

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
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
if(S
```

i `il` i

```
( l))
```

数据传输

```
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

下列代码以调用ECS的 `DescribeZones` 接口为示例。 数据传输

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

数据传输

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | 角色ARN格式错误 |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | RoleSessionName格式错误，支持输入2~64 个字符，请输入至少2个字符，允许输入英文字母、数字、半角句号 （.）、at（@）、短划线 （-）和下划线（ ）。 _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | DurationSeconds参数设置错误，过期时间最小值为900秒，最大值为MaxSessionDurati on设置的时间。 |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | 权限策略语法错误。 |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | 权限策略长度超限，最大不超过1024字符。 |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | STS Token没有权限。 |
| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
