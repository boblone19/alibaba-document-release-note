---
title: "云接入网关 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 67
source_pdf: "06_开发指南_development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/cgw/zh/development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云接入网关 开发指南

云接入网关

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
云接入网关
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关或ASAPI网关调用专有云API，为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**说明**

历史版本使用ASAPI网关调用专有云API的方式仍然有效，详情请参见ASAPI网关调用流程说明、生成 ASAPI的Endpoint、获取ASAPI的SDK包。

**流程图**

云接入网关

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

|  | resourcegroupid>， |
|---|---|

不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
云接入网关您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
云接入网关

## 准备工作

### 登录API与工具控制台

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
5. 在页面顶部的菜单栏中，选择**产品** > **其他** **> API****与工具**。

### 查看API信息

您在使用SDK时，需要获取产品名称、API名称和API版本。本文介绍如何查看API信息。

**背景信息**

API审计中的API仅供调用参考，具体API的使用方式需要参见各云产品的API文档。如果发生不一致情况，以 API支持情况为准。

**操作步骤**

1. 登录API与工具控制台。
2. 在左侧导航栏中选择**API****审计**。
云接入网关
3. 在**API****审计**页面，输入**API** **名称**等关键词进行搜索。
4. 查看并记录对应的产品名称、API名称和调用状态等。

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
云接入网关
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

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。
云接入网关

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com>，请替换为实际的STS Endpoint。 云接入网关

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

`// <sts.aliyuns.com>` 请替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}
    request.setSysDomain("<sts.aliyuns.com>");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`<yourRoleSessionName>`请您替换为实际值

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`<yourRoleArn>`请替换为上一步获取到的实际`Ram Role ARN`

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
云接入网关

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>，请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。

```
public static void main(String[] args) {
```

`// <yourRegionID>`请替换为您实际的地域`ID` `// <yourStsAccessKeyID>, <yourStsAccessKeySecret>`请替换为前一步获取到的`STS`三元组中`Acce`

```xml
ssKeyID、AccessKeySecret
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

`//<yourRegionID>`请替换为您实际的地域`ID`

```
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
```

`// <yourStsToken>`请替换为您前一步获取到的`STS`三元组中`SecurityToken`

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

云接入网关

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

云接入网关对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 获取产品名的Endpoint

本文介绍了如何获取产品名Endpoint。标题及短描述中产品名，请各云产品自行替换

**背景信息**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。您也可以通过如下方法自行获取Endpoint。

**操作步骤**

**警告**

1. 2. 3. 4. 云接入网关

## Java SDK调用示例

### 快速开始

本节介绍如何获取产品名Java SDK并开始调用。产品名需要替换为您自己的产品名。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。参见获取AccessKey在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。 获取产品名的Endpoint，具体操作参见获取产品名的Endpoint。产品名及链接请各云产品自行替换。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云 Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用产品名的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17及以上版本，SDK的版本为X.X.X。产品名需要替换为您自己的产品名；X.X.X需要替换为您自己产品的SDK 版本。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
替换为自己产品的示例

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Product>，请替换为您实际的产品名称。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <readTimeout>，请您根据实际情况设置读取超时时间，单位为毫秒。 <connectionTimeout>，请您根据实际情况设置连接超时时间，单位为毫秒。 <maxRequestsPerHost>，请您根据实际情况设置每个主机的最大请求数。 <maxRequests>，请您根据实际情况设置最大请求数。 <http://192.168.XX:33XX>，请替换为您实际的代理IP+端口。

```java
 import com.aliyuncs.profile.DefaultProfile;
 import com.aliyuncs.DefaultAcsClient;
 import com.aliyuncs.IAcsClient;
 import com.aliyuncs.exceptions.ClientException;
 import com.aliyuncs.exceptions.ServerException;
```

云接入网关

```
potco.a yucs.eceptos.Se
```

e

```java
cepto;
 import com.aliyuncs.ecs.model.v20140526.*;
 public class Main {
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

clientConfig.setReadTimeoutMillis(<readTimeout>);// 读取超时时间（可选）,单位为毫秒（`ms`）

```
        clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// 连接超时时间（可
```

选）,单位为毫秒（`ms`）

```
        clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// 设置每个主机的最大请
```

求数（可选） clientConfig.setMaxRequests(<maxRequests>);// 设置最大请求数（可选） clientConfig.setProtocolType(ProtocolType.HTTP); // 设置请求协议,默认`HTTP`（可选） `/*` 设置代理(可选`),`替换为代理`IP+Port`

```
        clientConfig.setHttpProxy("<http://192.168.XX:33XX>");
```

或

```
        clientConfig.setHttpsProxy("<https://192.168.XX:33XX>");
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```
        DescribeInstancesRequest request = new DescribeInstancesRequest();
```

`//` 业务参数

```
        request.setPageSize(10);
        request.setPageNumber(1);
```

`//` 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用

```
        request.putHeadParameter("x-acs-organizationid", "1");
        request.putHeadParameter("x-acs-resourcegroupid", "11");
```

`//` 发起请求并处理应答或异常

```java
        DescribeInstancesResponse response;
        try {
            response = client.getAcsResponse(request);
            for (DescribeInstancesResponse.Instance instance:response.getInstances())
{
                System.out.println(instance.getPublicIpAddress());
            }
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
        }
     }
 }
```

云接入网关

### 使用手册

#### 安装Java SDK

本文介绍如何安装及调用产品名 Java SDK。产品名需要替换为您自己的产品名。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用产品名的开发工具包，必须安装阿里云Java SDK核心库以及产品名的Java SDK。SDK核心库推荐使用4.5.17及以上版本，Java SDK的版本为X.X.X。产品名需要替换为您自己的产品名；X.X.X需要替换为您自己产品的SDK版本。 以使用ECS的Java SDK为例，您需要安装阿里云Java SDK核心库和ECS Java SDK，并在pom.xml文件中添加以下依赖即可。准确的SDK版本号，请参见阿里云开发工具包（SDK）。请各云产品替换为自己产品的示例

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- ecs java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-ecs</artifactId>
    <version>4.23.2</version>
</dependency>
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取Accesskey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 云接入网关

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

#### 发起调用

本文介绍如何使用产品名Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
云接入网关请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例如DescribeInstances。 在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。

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

#### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK对返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码： 云接入网关

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

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。 例如RunInstances接口，在发起CommonRequest请求时，需要使用 `request.setSysAction("RunInstances")` 来指定API名称。 您需要获取**PathPattern**参数，使用 `request.setSysUriPattern("<PathPattern>")` 的方式来指定 RESTful路径。

| 有集群实例的API的PathPattern为 | /api/v1/clusters |  |
|---|---|---|
| request.setSysUriPattern("/api/v1/clusters") |  |  |
|  |  | 指定 |

**示例：调用RPC风格的API**

以下代码为获取实例状态列表的调用示例（ECS产品属于RPC的调用风格)。 云接入网关以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

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
        request.setDomain("ecs.aliyuncs.com");
        request.setSysProduct("Ecs");
        request.setVersion("2014-05-26");
        request.setAction("DescribeInstanceStatus");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
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

云接入网关

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

**示例：调用RESTful风格的API**

当调用RESTful风格的API时，业务参数传参方式根据接口请求方式和ContentType分为两种： 接口请求方式为 `GET` 或 `DELETE` ，或ContentType为 `application/x-www-form-urlencoded` ， 使用以下方式传参： 将请求参数放在Query中，例如 request.putQueryParameter("page_number", "1"); 。 接口请求方式为 `POST` 或 `PUT` ，且ContentType为 `application/json` ，使用以下方式传参： 将请求参数放在Body中，例如：

```
String requestBody = "{\"page_number\":\"1\",\"page_size\":\"5\",\"SecurityToken\", \ "<yourSecurityToken>\"}"; request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
```

以下代码为，获取集群列表的调用示例（CS产品属于RESTful的调用风格）。 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。 <yourSecurityToken>，请替换为您实际的SecurityToken。

```java
import com.aliyuncs.CommonRequest;
```

云接入网关

|  | p y q ; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample { /** * DemoAPI: DescribeClusterV1 */ public static void main(String[] args) { // 创建DefaultAcsClient实例并初始化 DefaultProfile profile = DefaultProfile.getProfile( "<yourRegionID>", // 请替换为您实际的地域ID "<yourAccessKeyID>", // 请替换为您实际的AccessKey ID "<yourAccessKeySecret>"); // 请替换为您实际的AccessKey Secret HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true); clientConfig.setProtocolType(ProtocolType.HTTP); /** 请根据实际情况判断是否需要设置HTTP代理设置方法如下： clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); 请替换为实际代理IP+端口 */ profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); // 创建API请求并设置参数 CommonRequest request = new CommonRequest(); // 接口实际请求方式,详细请参考接口开发文档 request.setMethod(MethodType.GET); request.setDomain("cs.aliyuncs.com"); request.setSysProduct("CS"); request.setSysVersion("2015-12-15"); request.setSysUriPattern("/api/v1/clusters"); request.putHeadParameter("Content-Type", "application/json"); request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// 非必填，请替换为您实际的资源集ID request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// 必填 ，请替换为您实际的组织ID request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// 必填，调用来源说明 request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// 非必填（企业版V3.1 5.0及之前历史版本需要）,请替换为您实际的地域ID // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修改、删除、查询单实例详情时需要），请替换为您实际的实例ID // 业务参数,请求方式是GET、DELETE 或 ContentType为application/x-www-form- urlencoded,则使用以下方式传参 request.putQueryParameter("page number", "1"); _ request.putQueryParameter("page size", "5"); _ String requestBody = "{}"; /** 当使用STS AccessKey调用接口时,需要在参数中加上SecurityToken字段调用方法如下： |  |
|---|---|---|

云接入网关

```
        String requestBody = "{\"SecurityToken\": \"<yourSecurityToken>\"}";
```

请替换为实际`Token` `*/`

```
        /**
```

若接口请求方式是`POST`、`PUT`且`ContentType`为`application/json,`则以下方式传数据

```
        String requestBody = "
{\"page_number\":\"1\",\"page_size\":\"5\",\"SecurityToken\", \"<your- SecurityToken>\"}";
        request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
```

`*/`

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

云接入网关

## Python SDK调用示例

### 快速开始

本节介绍如何获取Python SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体请参获取的Endpoint，具体操作参见获取ECS的Endpoint。
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
以下以安装云服务器ECS的SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装云服务器ECS的SDK：

```
pip install aliyun-python-sdk-ecs
```

如果您使用的是Python 3.x，执行以下命令，安装云服务器ECS的SDK：

```
pip3 install aliyun-python-sdk-ecs
```

**使用Python SDK**

以下示例以ECS为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuns.com>，请替换为您实际的产品访问地址。 云接入网关

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
# global config
```

`region_id = '<yourRegionID>' #` 请替换为您实际的地域`ID` `access_key = '<yourAccessKeyID>' #` 请替换为您实际的的`AccessKey ID`

```bash
acces_secret = '<yourAccessKeySecret>' # 请替换为您实际的AccessKey Secret
# product config
```

`product_name = 'ECS' #` 填写产品名称 `endpoint = '<ecs.aliyuns.com>' #` 产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeInstancesRequest.DescribeInstancesRequest()
```

`request.set_accept_format('json') #` 设置返回数据格式

```bash
# get response
response = clt.do_action_with_exception(request) print response
```

### 使用手册

#### 安装Python SDK

本文档介绍如何安装及调用Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。 使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用ECS的

**说明**

Python SDK，您需要安装阿里云Python SDK核心库和ECS的Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

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

#### 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 云接入网关目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危

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

本节介绍如何使用Python SDK发起请求。

**操作步骤**

1. 导入相关产品的SDK。

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
```

云接入网关
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

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
云接入网关发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 RPC风格的API： 您需要获取**Action**参数，使用 `request.set_action_name('Action')` 的方式来指定API名称。 例如RunInstances接口，在发起CommonRequest请求时，需要使用 `request.set_action_name('RunInstances')` 来指定API名称。 RESTful风格的API： 您需要获取**PathPattern**参数，使用 `request.set_uri_pattern('Pattern')` 的方式来指定 RESTful。

| 集群实例的API的PathPattern为 | /api/v1/clusters |  |
|---|---|---|
| request.set uri pattern ('/api/v1/clusters') _ _ |  |  |
|  |  | 指 |

**示例：调用RPC风格的API**

以下代码为云服务器（ECS）的DescribeInstanceStatus接口，获取实例状态列表的调用示例： 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <ecs.aliyuncs.com>，请替换为您实际的产品访问地址。 云接入网关

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Ecs') request.set_action_name('DescribeInstanceStatus') request.set_version('2014-05-26')
```

`request.set_domain('<ecs.aliyuncs.com>') #`产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# or:
# request = = CommonRequest(product='Ecs',
action_name='DescribeInstanceStatus',version='2014-05-26',domain='ecs.aliyuncs.com')
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

**示例：调用RESTful风格的API**

当调用RESTful风格的API时，业务参数传参方式根据接口请求方式和ContentType分为两种： 接口请求方式为 `GET` 或 `DELETE` ，或ContentType为 `application/x-www-form-urlencoded` ， 使用以下方式传参： 将请求参数放在Query中，例如 `request.add_query_param("page_number", "1")` 。 接口请求方式为 `POST` 或 `PUT` ，且ContentType为 `application/json` ，使用以下方式传参： 将请求参数放在Body中，例如： 云接入网关

```
body = '{"page_number":"1",page_size"5":"SecurityToken","":"<yourSecurityToken>"}' request.set_content(body.encode('utf-8'))
```

以下代码为容器服务（CS）的DescribeClusterV1接口，获取集群列表的调用示例： 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <cs.aliyuncs.com>，请替换为您实际的产品访问地址。 云接入网关

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
######
# API:CS-DescribeClusterV1
######
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('CS') request.set_version('2015-12-15') request.set_uri_pattern('/api/v1/clusters') # Pattern
```

`request.set_domain('<cs.aliyuncs.com>') #` 产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# or:
# request = CommonRequest(product='CS', version='2015-12-15',
uri_pattern='/api/v1/clusters', domain='cs.aliyuns.com')
######
```

# 设置请求协议类型,支持 `HTTP` 或 `HTTPS,`默认为`HTTP`
# 设置`https`方法如下：

```bash
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('GET') request.add_header('Content-Type', 'application/json')
```

# 非必填，请替换为您实际的资源集`ID`

```
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID")
```

# 必填，请替换为您实际的组织`ID`

```
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
```

# 必填，调用来源说明

```
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
```

# 非必填（企业版`V3.15.0`及之前历史版本需要）,请替换为您实际的地域`ID`

```
request.add_header("x-acs-regionid", "<yourRegionID>")
```

# 非必填（修改、删除、查询单实例详情时需要）,请替换为您实际的实例`ID`

```bash
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
```

# 业务参数,请求方式为`GET`、`DELETE` 或`ContentType`为`application/x-www-form-urlencoded,`则使用以下
方式传数据

```
request.add_query_param("page_number", "1") request.add_query_param("page_size", "5")
######
```

# 当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段
# 调用方法如下：

```bash
# body = '''{\"SecurityToken\", \"<yourSecurityToken>\"}'''
```

# 请替换为您实际的`SecurityToken`

```
######
######
```

# 若接口请求方式是`POST`、`PUT` 且`ContentType`为`application/json,`则以下方式传数据

```python
# body = '{"page_number":"1",page_size"5":"SecurityToken","":"<your-SecurityToken>"}'
# request.set_content(body.encode('utf-8'))
######
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

云接入网关

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问。本操作介绍如何获取阿里云Go SDK并开始调用。

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

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您实际的Endpoint。 云接入网关

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

)

```
func main() {
```

`//` 创建`ecsClient`实例

```
    ecsClient, err := ecs.NewClientWithAccessKey(
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
    request := ecs.CreateDescribeInstancesRequest()
```

`//` 设置当前产品的`Endpoint`

```
    request.Domain = "<Endpoint>"
    // 等价于 request.PageSize = "10"
    request.PageSize = requests.NewInteger(10)
```

`//` 发起请求并处理异常

```
    response, err := ecsClient.DescribeInstances(request)
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

#### 安装Go SDK核心包

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。 云接入网关确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危

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

#### 发起调用

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

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。 云接入网关

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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以ECS为例，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息： 云接入网关

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

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**示例：调用RPC风格的API**

以下代码为云产品 ECS（云服务器）的DescribeInstanceStatus接口，获取实例状态列表的调用示例 （ECS产品属于RPC的调用风格）： 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 云接入网关

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

`request.Domain = "<ecs.aliyuncs.com>" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "Ecs"
    request.Version = "2014-05-26"
```

`//` 因为是`RPC`接口，因此需指定`APIName(Action)`

```
    request.ApiName = "DescribeInstanceStatus"
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

**示例：调用RESTful风格的API**

当调用RESTful风格的API时，业务参数传参方式根据接口请求方式和ContentType分为两种： 接口请求方式为 `GET` 或 `DELETE` ，或ContentType为 `application/x-www-form-urlencoded` ， 使用以下方式传参： 将请求参数放在Query中，例如 `request.QueryParams["page_number"] = "1"` 。 云接入网关接口请求方式为 `POST` 或 `PUT` ，且ContentType为 `application/json` ，使用以下方式传参： 将请求参数放在Body中，例如：

```
body := "{\"page_number\":\"1\",page_size:\"5\"}" request.SetContent([]byte(body)) request.SetContentType("application/json")
```

以下代码为云产品 CS(容器服务) 的DescribeClusterV1接口，获取集群列表的调用示例（CS产品属于 RESTful的调用风格）： 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <cs.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 云接入网关

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
    request.Method = "GET"
```

`request.Domain = "cs.aliyuncs.com" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "CS"
    request.Version = "2015-12-15"
```

`//` 因为是`Restful`接口，因此需指定`PathPattern`

```
    request.PathPattern = "/api/v1/clusters"
```

`//` 当使用`STS AccesssKey`调用`ROA`接口时需要在`header`中加上`x-acs-security-token`字段

```
    // request.Headers["x-acs-security-token"] = "<yourSecurityToken>"
```

`//` 必填值，调用来源说明

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
```

`//` 非必填，企业版`V3.15.0`及之前历史版本需要

```
    request.Headers["x-acs-regionid"] = "<yourRegionID>"
```

`//` 非必填，请替换为您实际的资源集`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>"
```

`//` 必填，请替换为您实际的组织`ID`

```
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"
```

`//` 非必填，修改、删除、查看单实例详情时需要，请替换为您实际的实例`ID`

```
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>"
```

`//` 业务参数,当请求方式为`GET`、`DELETE` 或 `ContentType`为`application/x-www-form-urlencoded`时 ，使用以下方式传数据

```
    // request.QueryParams["page_number"] =  "1"
    // request.QueryParams["page_size"] = "5"
```

`//` 当接口请求方式是`POST`、`PUT` 且`ContentType`为`application/json`时，则使用以下方式传数据

```
    // body := "{\"page_number\":\"1\",page_size:\"5\"}"
    // request.SetContent([]byte(body))
    // request.SetContentType("application/json")
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

云接入网关

## API参考

### API概览

专有网络提供以下接口供您使用。

| API | 描述 |
|---|---|
| ListDynamicVIPs | 获取动态vip 资源。 |
| GetDynamicVIP | 获取动态vip资源详情。 |
| UpdateDynamicVIP | 修改动态vip状态码。 |
| DeleteDynamicVIP | 解除EIP与云产品实例的绑定关系。 |
| ListCloudNames | 获取云名称列表。 |
| ListCloudRegions | 获取Region列表。 |
| ListProducts | 获取产品列表。 |
| ListClusters | 获取集群列表。 |
| ListServices | 获取service列表。 |
| ListServerRoles | 获取servicerole列表。 |
| ListApplications | 获取应用列表。 |
| ListTempVipByNames | 获取该app 注册的vip的名称。 |
| GetTmplVipDetailByName | 获取该app 注册的vip的详情。 |
| ListSupportIPTypes | 支持的类型。 |
| ListSupportTunnelTypes | 支持的tunnel类型。 |

云接入网关

| CreateDynamicVIP | 创建动态 vip。 |
|---|---|
| ListDynamicVipParams | 获取动态vip Params。 |
| UpdateDynamicVipParams | 更新动态vip Params。 |
| DeleteDynamicVipParams | 删除动态vip Params。 |
| GetDynamicVipParam | 获取动态vip Params详情。 |

| API | 描述 |
|---|---|
| CreateDynamicDns | 创建动态DNS 资源。 |
| DeleteDynamicDns | 删除动态DNS资源。 |
| UpdateDynamicDns | 更新动态DNS资源（仅支持dns product）。 |
| ListDynamicDnses | 获取动态DNS资源。 |

### 调用API

#### 请求结构

专有网络接口调用是向专有网络API的服务端地址发送HTTP GET请求。您需要按照接口描述在请求中加入相应请求参数，调用后系统会返回处理结果。请求及返回结果都使用UTF-8字符集进行编码。 专有网络的API是RPC风格，您可以通过发送HTTP GET请求调用专有网络API。 其请求结构如下：

```
http://Endpoint/?Action=xx&Parameters
```

其中：
**Endpoint**：专有网络API的服务接入地址为 `vpc.example.com` 。

**说明**

`example.com` 是项目自定义的访问域名。
**Action**：要执行的操作，如使用DescribeVpcs查询已创建的专有网络实例。
云接入网关
**Version**：要使用的API版本，专有网络的API版本是2016-04-28。
**Parameters**：请求参数，每个参数之间用and（&）符号分隔。
请求参数由公共请求参数和API自定义参数组成。公共参数中包含API版本号、身份验证等信息，关于公共参数的更多信息，请参见公共参数。 下面是一个调用DescribeVpcs接口查询已创建的专有网络的示例：

**说明**

为了便于用户查看，本文中的示例都做了格式化处理。

```
https://vpc.example.com/?Action=DescribeVpcs &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2021-06-01T12:00:00Z
```

#### API授权

为了确保您的账号安全，建议您使用子账号的身份凭证调用API。如果您使用RAM账号调用专有网络API， 您需要为该RAM账号创建、附加相应的授权策略。

#### API签名

专有网络服务会对每个API请求进行身份验证，无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。 专有网络通过使用AccessKey ID和AccessKey Secret进行对称加密的方法来验证请求的发送者身份。 AccessKey是为阿里云账号和RAM用户发布的一种身份凭证(类似于用户的登录密码)，其中AccessKey ID 用于标识访问者的身份，AccessKey Secret是用于加密签名字符串和服务器端验证签名字符串的密钥，必 RPC API需按如下格式在请求中增加签名（Signature）：

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
```

以DescribeVpcs为例，假设AccessKey ID是 `testid` ， AccessKey Secret是 `testsecret` ，则签名前的请求URL如下：

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

云接入网关完成以下步骤计算签名：
1. 使用请求参数创建待签名字符串：

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpcs&Format%3DXML&SignatureMethod%3DHMAC- SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f- 4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02- 23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. 计算待签名的HMAC的值。
在AccessKey Secret后添加一个“&”作为计算HMAC值的key。本示例中的key为 `testsecret&` 。

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. 将签名加到请求参数中：

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### RAM鉴权

在使用RAM账号调用VPC API前，需要主账号通过创建授权策略对RAM账号进行授权。在授权策略中，使用资源描述符（Alibaba Cloud Resource Name, ARN）指定授权资源。

**可授权的专有网络资源类型**

下表列举了VPC中可授权的资源及其描述方式：

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

云接入网关

| 路由表（Route Table） | acs:vpc:$regionid:$accountid:routetable/$routetableid |  |
|---|---|---|
|  | acs:vpc:$regionid:$accountid:routetable/* |  |
|  | acs:vpc:*:$accountid:routetable/* |  |
| 弹性公网IP（EIP） | acs:vpc:$regionid:$accountid:eip/$allocationid |  |
|  | acs:vpc:$regionid:$accountid:eip/* |  |
|  | acs:vpc:*:$accountid:eip/* |  |
| NAT网关（NAT Gateway） | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |
|  | acs:vpc:$regionid:$accountid:natgateway/* |  |
|  | acs:vpc*:$accountid:vpc/* |  |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |  |
|  |  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| NAT网关带宽包（NAT Gateway Bandwidth Package） |  |  |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/* |  |
|  | aacs:vpc:*:$accountid:vpc/* |  |
| 端口转发表（Forward Table） | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |  |
|  | acs:vpc:$regionid:$accountid:forwardtable/* |  |
|  | acs:vpc:*:$accountid:vpc/* |  |
| SNAT表（SNAT Table） | acs:vpc:$regionid:$accountid:snattable/$snattableid |  |
|  | acs:vpc:$regionid:$accountid:snattable/* |  |
|  | acs:vpc:*:$accountid:vpc/* |  |
| 通用资源 | acs:vpc:$regionid:$accountid:* |  |
|  | acs:vpc:*:$accountid:* |  |

其中 $regionid/accoutid/vrouterid 为具体的资源ID， * 代表对应的所有资源。

**可授权的VPC接口**

下表列举了VPC中可授权的API及其描述方式：

| API | 资源描述 |
|---|---|
| vpc:CreateVpc | acs:vpc:$regionid:$accountid:vpc/* |
| vpc:DeleteVpc | acs:vpc:$regionid:$accountid:vpc/$vpcid |

| > 文档版本：20260729 | 4 |
|---|---|

| 开发指南·API参考 | 云接入网关 |
|---|---|

|  | vpc:DescribeVpcs | vpc:$regionid:$accountid:vpc/* |  |  |
|---|---|---|---|---|
|  | vpc:ModifyVpcAttribute | acs:vpc:$regionid:$accountid:vpc/$vpcid |  |  |
|  |  | acs:vpc:$regionid:$accountid:vrouter/* |  |  |
|  |  | 指定要查询的 VRouterId： "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/ $vpcid" |  |  |
|  | vpc:DescribeVRouters | $vpcid" |  |  |
|  |  | 未指定要查询的 VRouterId： "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/ *" |  |  |
|  |  | *" |  |  |
|  | vpc:ModifyVRouterAttribute | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |  |  |
|  | vpc:CreateVSwitch | acs:vpc:$regionid:$accountid:vswitch/* |  |  |
|  |  | acs:vpc:$regionid:$accountid:vpc/$vpcid |  |  |
|  | vpc:DeleteVSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |  |  |
|  | vpc:DescribeVSwitches | acs:vpc:$regionid:$accountid:vswitch/* |  |  |
|  |  | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |  |  |
|  |  |  | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |  |
|  | vpc:ModifyVSwitchAttribute | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |  |  |
|  |  | acs:vpc:$regionid:$accountid:routetable/$routetableid |  |  |
|  |  |  | acs:vpc:$regionid:$accountid:routetable/$routetableid |  |
|  | vpc:CreateRouteEntry |  |  |  |
|  |  | acs:vpc:$regionid:$accountid:routetable/$routetableid |  |  |
|  |  |  | acs:vpc:$regionid:$accountid:routetable/$routetableid |  |
|  | vpc:DeleteRouteEntry |  |  |  |
|  | vpc:DescribeRouteTables | acs:vpc:$regionid:$accountid:routetable/* |  |  |
|  |  | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vr outerid" |  |  |
|  |  |  | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vr |  |
|  | vpc:AllocateEipAddress | acs:vpc:$regionid:$accountid:eip/* |  |  |
|  | vpc:AssociateEipAddres | acs:vpc:$regionid:$accountid:eip/* |  |  |
|  |  | 绑定ECS实例 acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |  |  |
|  | vpc:DescribeEipAddresses | acs:vpc:$regionid:$accountid:eip/* |  |  |

| "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/ |  |
|---|---|

| "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/ |  |
|---|---|

| 0 | > 文档版本：2026072 |
|---|---|

云接入网关

| vpc:UnassociateEipAddress | 绑定ECS实例 acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |  |  |
|---|---|---|---|
| vpc:ReleaseEipAddress | acs:vpc:$regionid:$accountid:eip/$allocationid |  |  |
| vpc:DescribeEipMonitorData | acs:vpc:$regionid:$accountid:eip/$allocationid |  |  |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |  |  |
| vpc:CreateNatGateway | acs:vpc:$regionid:$accountid:natgateway/* |  |  |
|  | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |  |
|  |  | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |
| vpc:DescribeNatGateways |  |  |  |
|  | acs:vpc:$regionid:$accountid:natgateway/* |  |  |
|  | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |  |
|  |  | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |
| vpc:ModifyNatGatewaySpec |  |  |  |
|  | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |  |
|  |  | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |
| vpc:ModifyNatGatewayAttribute |  |  |  |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |  |  |
|  | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |  |
|  |  | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |  |
| vpc:DeleteNatGateway |  |  |  |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |  |  |
| vpc:CreateBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/* |  |  |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |  |  |
|  |  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |  |
| vpc:DescribeBandwidthPackages | thpackageid |  |  |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/* |  |  |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |  |  |
|  |  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |  |
| vpc:ModifyBandwidthPackageSpec | thpackageid |  |  |
| vpc:ModifyBandwidthPackageAttrib | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |  |  |
|  |  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |  |
| ute | thpackageid |  |  |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |  |  |
|  |  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |  |
| vpc:AddBandwidthPackageIps | thpackageid |  |  |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |  |  |
|  |  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |  |
| vpc:RemoveBandwidthPackageIps | thpackageid |  |  |
|  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |  |  |
|  |  | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |  |
| vpc:DeleteBandwidthPackage | thpackageid |  |  |

| > 文档版本：20260729 | 5 |
|---|---|

|  | 开发指南·API参考 | 云接入网关 |  |
|---|---|---|---|

|  | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |  |  |
|---|---|---|---|
|  |  | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |  |
| vpc:CreateForwardEntry | eid |  |  |
|  | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |  |  |
|  |  | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |  |
| vpc:DeleteForwardEntry | eid |  |  |
|  | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |  |  |
|  |  | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |  |
| vpc:ModifyForwardEntry | eid |  |  |
|  | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |  |  |
|  |  | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |  |
| vpc:DescribeForwardTableEntries | eid |  |  |
| vpc:CreateSnatEntry | acs:vpc:$regionid:$accountid:snattable/* |  |  |
|  | acs:vpc:$regionid:$accountid:snattable/$snattableid |  |  |
|  |  | acs:vpc:$regionid:$accountid:snattable/$snattableid |  |
| vpc:ModifySnatEntry |  |  |  |
|  | acs:vpc:$regionid:$accountid:snattable/$snattableid |  |  |
|  |  | acs:vpc:$regionid:$accountid:snattable/$snattableid |  |
| vpc:DescribeSnatTableEntries |  |  |  |
|  | acs:vpc:$regionid:$accountid:snattable/$snattableid |  |  |
|  |  | acs:vpc:$regionid:$accountid:snattable/$snattableid |  |
| vpc:DeleteSnatEntry |  |  |  |

### 公共参数

**公共请求参数**

公共请求参数是每个接口调用都需要提供的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | Strin g | 否 | 返回值的类型，仅支持JSON。 |
| Version | Strin g | 是 | API 版本号，以日期形式YYYY-MM-DD输入，取值： 2019-05-10。 |
| AccessKeyId | Strin g | 是 | 访问服务使用的密钥ID。 |
| AccessKeySe cret | Strin g | 是 | 访问服务使用的密钥值。 |
| RegionId | Strin g | 是 | 访问服务所使用的的地域ID。 |
| Product | Strin g | 是 | 接口对应的产品名称。 |

您也可以通过Apsara Uni-manager运营控制台获取接口所需要的 `Product` 和 `Version` 参数。具体操作步骤如下。
1. 登录Apsara Uni-manager运营控制台。
云接入网关
2. 在顶部菜单栏中选择**产品** > **其他** **> API****与工具**。
3. 在左侧导航栏中单击**API****目录**。
4. 在**API****名称**文本框中输入接口名称，即可查询接口的信息。

| 名称 | 描述 |
|---|---|
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID，获取方式请参见获取组织 ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID，获取方式请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID，获取方式请参见获取实例ID。 |

在调用各云产品接口调用时，您需要在调用代码的请求头Header中添加**x-acs-**

**说明**

**organizationid**、**x-acs-resourcegroupid**、**x-acs-instanceid**等参数的实际值，用于指定当
前实例的实例ID（在创建实例和查询实例列表的场景下，实例ID不存在），及其所属的组织和资源集。 若未添加相关Header参数实际值，调用时则会默认指向root组织和root资源集。

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

### 动态VIP

#### ListDynamicVIPs

**API描述**

调用该接口时，请注意： 不加Filter参数为获取所有资源。 JSON中使用参数filter查询指定字段，请看请求示例。 默认开启分页查询。

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Info | Json | 是 | {key,valu e} | 查看下面请求参数说明 |

**请求参数说明**

| > 文档版本：2026 | 0729 |  |  | 5 |
|---|---|---|---|---|

云接入网关

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDynamicVIPs | 要执行的操作， 取值：ListDynamicVIPs。 |
| PageSize | Integ er | 否 | 1 | 分页查询时每页的行数，最大值为50，默认值为 10。。 |
| PageNumbe r | Integ er | 否 | 10 | 列表的页码，默认值为1。 |
| Filter | Array | 否 | [] | 查看如下Filter详情 |

**Filter参数说明**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Key | String | 否 | DynVipIp |  |
| Value | Array | 否 | [ "100.231.244.247 ", "198.146.15.31" ] |  |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 861E6630-AEC0- 4B2D-B214- 6CB5E44B7F04 | 请求ID。 |
| VSwitchId | String | vsw- 25nsdf2aue4g**** | 交换机的ID。 |

#### GetDynamicVIP

**API描述**

调用该接口时，请注意：

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDynamicVIP | 要执行的操作， 取值：GetDynamicVIP。 |

云接入网关

| VIP | String | 是 | 172.16.1.2 | 查询过滤条件。 |
|---|---|---|---|---|

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | 请求ID。 |
| Application | String | resource init _ | 应用。 |
| ClusterName | String | Oss2L54Cluster | 集群名称。 |
| DynVipLbId | String | 171ed137b50-cn- qingdao-env17- d01 825176289 - _ _ 1320843925 | 动态VIP LoadBalancer ID。 |
| DynVipIp | String | 172.16.1.2 | VIP |
| DynVipResour ceId | String | 7b87d5f0b3248d00 7cb8b3c3f32d086a | VIP 资源ID，一条动态vip资源时一个唯一的ID, 本地根据其他字段组合，通过MD5生成。 |
| DynVipTunnel Type | String | classic to any tunn _ _ _ el | Tunnel 类型，四种取值['none', 'single tunnel', _ 'classic to any tunnel', _ _ _ 'xregion any tunnel']。 _ _ |
| DynVipType | String | internet | 负载均衡实例的类型。取值： internet，intranet。 internet：负载均衡实例仅提供公网IP，可以通过Internet访问的负载均衡服务。 intranet：负载均衡实例仅提供私网IP地址 （或VPC内的地址），只能通过内部网络访问该负载均衡服务。 |
| RegionId | String | cn-hangzhou | 动态VIP的地域。 |
| RelatedTempl ateResId | String | 047004a37bbc9e9e bf628e2b2a170ab2 6cea65d3 | VIP模板的res.id，是唯一值，用于区分模板。 |
| ServerRole | String | TEngine2# | 服务角色。 |

云接入网关

| ServiceName | String | oss-server | 服务名称。 |
|---|---|---|---|
| VipTemplateN ame | String | oss cluster _ | VIP模板名称。 |
| IntranetDoma in | String | intra.env17e.shugua ng.com | 用于构建飞天基础运维平台URL。 |
| ProductName | String | opsapi | 产品名称。 |
| ListenerId | Json | {"80": "8a91b49b7443987 9017447aac23d001 4"} | 用于适配层SDK，修改删除接口。 |
| ServerGroupI d | String | 8a91b49b74439879 017447aac4ae0015 | 用于适配层SDK，修改删除接口。 |
| DynVipStatus | String | 8000 | 状态码。 |

#### UpdateDynamicVIP

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateDynamicVI P | 要执行的操作，取值：UpdateDynamicVIP。 |
| VIP | String | 是 | 172.16.1.2 | 修改的VIP。 |
| DynVipStat us | String | 是 | 8000 | 动态VIP状态8000 为正常。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | 请求ID。 |

#### DeleteDynamicVIP

云接入网关

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDynamicVI P | 要执行的操作，取值： DeleteDynamicVIP。 |
| VIP | String | 是 | 172.16.1.2 | 要删除的VIP。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 9A572171-4E27- 40D1-BD36- D26C9E71E29E | 请求ID。 |

#### CreateDynamicVIP

1. 通过调用飞天基础运维平台获取模板详情数据。
2. 前端传入的数据，如果有重复的字段，前端数据覆盖掉飞天基础运维平台数据。
3. 调用适配层SDK，成功后得到创建的VIP。
4. vip信息存入本地数据库 dynamic_vip_info。
5. vip关联的params相关信息存入本地数据库dynamic_vip_template_parameter以上，创建动态VIP成
功

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDynamicVI P | 要执行的操作， 取值：CreateDynamicVIP。 |
| ProductNam e | String | 是 | opsapi | 产品名称。 |
| ClusterNam e | String | 是 | Oss2L54Cluster | 集群名称。 |
| ServiceNam e | String | 是 | opsapi | 服务名称。 |

云接入网关

| ServiceRole | String | 是 | ApiServer# | SR名称 |
|---|---|---|---|---|
| Application | String | 是 | api-server | 应用名称。 |
| Name | String | 是 | opsapiserver | 模板VIP名称。 |
| Region | String | 是 | cn-qingdao- env17-d01 | 所属地域的ID。 |
| IntranetDo main | String | 是 | http://intra.env17 e.shuguang.com/ | 域。 |
| Ipprotocol | String | 是 | ipv4 | VIP资源类型ipv4/ipv6。 |
| DynVipType | String | 是 | internet | 负载均衡实例的类型。取值： internet，intranet。 internet：负载均衡实例仅提供公网IP，可以通过Internet访问的负载均衡服务。 intranet：负载均衡实例仅提供私网IP地址 （或VPC内的地址），只能通过内部网络访问该负载均衡服务。 |
| DynVipTunn elType | String | 是 | classic to any tu _ _ _ nnel | tunnel类型，四种取值['none', 'single tunnel', _ 'classic to any tunnel', _ _ _ 'xregion any tunnel']。 _ _ |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 9A572171-4E27- 40D1-BD36- D26C9E71E29E | 请求ID。 |
| VIP | String | 66.248.51.171 | 创建出的VIP |

### 动态DNS

#### CreateDynamicDns

**API描述**

**请求参数**

云接入网关

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDynamicDn s | 要执行的操作，取值： CreateDynamicDns |
| Region | String | 是 | hangzhou | 所在的地域。 |
| LocalCloudI d | String | 是 |  | 本地云ID。 |
| RemoteClou dId | String | 是 |  | 远端云ID。 |
| DnsType | String | 否 | dns product | DNS类型，可选值：dns product：租户DNSops dns：OPS DNS。 |
| DnsRecordT ype | String | 是 | Forward-Zone | 记录类型，可选值：[Forward-Zone，A]ops dns 对应A记录dns product对应forward zone |
| DnsZone | String | 否 | domain1.com,do main2.com | DNS类型为dns product填写：多个Zone可以用逗号分隔，例如： domain1.com,domain2.com。 |
| DnsDomain | String | 否 | asd.inter.env17e. shuguang.com | DNS类型为OPS DNS填写：填写一条 DNSDomain记录，例如： asd.inter.env17e.shuguang.com注意，DomainName需要是环境中已经注册了的域。 |
| DnsRecord | String | 是 | 10.0.0.1,10.0.0.2 | Forwarders/Records，多个记录用逗号分隔。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | pc- bp1qrb3044eqixog0 **** | 请求ID。 |
| DnsRecordId | Array | [120,121] | 创建成功的DNS记录ID。 |

#### DeleteDynamicDns

**API描述**

删除租户DNS和OPS DNS共用一个接口, 通过DNS类型[DnsType]字段来区分: DNS product：租户DNS, ops dns：OPS DNS 删除租户DNS, 必选参数：DnsRecordId 删除OPS DNS，必选参数：DnsDomain，DnsRecord 云接入网关

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDynamicDn s | 要执行的操作，取值： DeleteDynamicDns |
| DnsType | String | 是 | dns product | DNS类型，可选值：dns product：租户DNSops dns：OPS DNS。 |
| DnsRecordI d | String | 否 | 4819 | DNS类型为dns product必填：DNS记录ID。 |
| DnsDomain | String | 否 | domain1.com | DNS类型为OPS DNS填写：DNS地址。 |
| DnsRecord | String | 否 | 10.0.0.1 | DNS类型为OPS DNS填写： Forwarders/Records记录 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | 请求ID。 |

#### UpdateDynamicDns

**API描述**

支持修改租户DNS（dns product）（OPS DNS不支持修改，只能添加和删除）。

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateDynamicD ns | 要执行的操作，取值：UpdateDynamicDns。 |
| DnsRecordI d | String | 是 | 4819 | 要修改的DNS记录ID。 |
| RemoteClou dId | String | 否 | AliDevCloud2 | 远端云ID。 |
| DnsRecord | String | 是 | 10.0.0.1,10.0.0.2 | Forwarders/Records，多个记录用逗号分隔。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云接入网关

| RequestId | String | 2B3670CD-670E- 4540-8C13- 6DE929AEDD3B | 请求ID。 |
|---|---|---|---|

云接入网关

## 附录

### STS概要

#### 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

**使用RAM用户扮演角色时获取STS Token**

有权限的RAM用户可以使用其访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用STS Token访问阿里云资源。

**产品优势**

使用STS Token，减少长期访问密钥（Accesskey）泄露的风险。 STS Token具有时效性，可以自定义有效期，到期后将自动失效，无需定期轮换。 可以为STS Token绑定自定义权限策略，提供更加灵活和精细的云资源授权。

#### AssumeRole

RAM用户调用AssumeRole接口获取一个扮演RAM角色的临时身份凭证STS Token。该接口中RAM用户扮演的是可信实体为阿里云账号类型的RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssumeRole | 要执行的操作。取值：AssumeRole |
| RoleArn | String | 是 | acs:ram::123456 789012****:role/ adminrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM 角色。 |
| RoleSessionNa me | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-） 和下划线（ ）。 _ |

云接入网关

| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 如果指定该权限策略，则STS Token最终的权限策略取RAM角色权限策略与该权限策略的交集。 如果不指定该权限策略，则STS Token最终的权限策略取RAM角色的权限策略。 长度为1~1024个字符。 |
|---|---|---|---|---|

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

操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下： 云接入网关

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
            if (StringUtils.isEmpty(assumeRole)) return;
JSONObjectassumeRoleJson=JSONObject.parseObject(assumeRole);
```

云接入网关

```
            JSONObject assumeRoleJson  JSONObject.parseObject(assumeRole);
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

下列代码以调用ECS的 `DescribeZones` 接口为示例。 云接入网关

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

云接入网关

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
