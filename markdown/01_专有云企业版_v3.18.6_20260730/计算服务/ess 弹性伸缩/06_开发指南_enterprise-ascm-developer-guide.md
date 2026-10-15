---
title: "弹性伸缩 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 339
source_pdf: "06_开发指南_enterprise-ascm-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/ess/zh/enterprise-ascm-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 弹性伸缩 开发指南

弹性伸缩 ESS

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
弹性伸缩 ESS
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公共云更一致的体验，自企业版V3.16.0 开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

弹性伸缩 ESS

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，详情请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
获取调用时所需要的RegionID参数，获取方式请参见获取弹性伸缩的Endpoint。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrga nizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListRe sourceGroup章节。

**说明**

| <x-acs- |  |
|---|---|

|  | resourcegroupid> |
|---|---|

不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
弹性伸缩 ESS 您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法，请参
5. 获取云产品的Endpoint。
6. 获取云产品SDK并调用云产品API。
弹性伸缩 ESS

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

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。 弹性伸缩 ESS

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密的方法，来验证某个请求发送者的身份。其中，AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret以及Security Token。获取方式， Apsara Uni-manager运营控制台提供了个人账号AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足。 弹性伸缩 ESS 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域。例如：cn-hangzhou-****。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方式，请参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方式，请参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID。例如，ECS的实例ID可以从ECS列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。
Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的操作方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取STS AccessKey

本文为您介绍如何使用STS方式，调用专有云的产品API。

**背景信息**

弹性伸缩 ESS 阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限的管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret以及SecurityToken三元组组成，使用STS方式调

**操作步骤**

1. 获取用户角色的RAM Role。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看RAM Role。
2. 获取STS Accesskey三元组。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下所示： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 "sts.aliyuns.com" ，请替换为实际的STS Endpoint。 弹性伸缩 ESS

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

3. 通过STS AccessKey三元组调用云产品的接口，下列代码以弹性伸缩的CreateScalingGroup接口为示
例。 弹性伸缩 ESS 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>，请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。

```
public static void main(String[] args) {
```

`// "<yourRegionID>"`请替换为您实际的地域`ID` `// "<yourStsAccessKeyID>"`和`"<yourStsAccessKeySecret>"`请替换为前一步获取到的`STS`三元组中

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
    request.setSysDomain("ess.aliyuncs.com");
    request.setSysProduct("ess");
    request.setSysAction("CreateScalingGroup");
    request.setSysVersion("2014-08-28");
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

`//` 非必填，请替换为您实际的资源集`ID`

```
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填，请替换为您实际的组织`ID`

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
```

### 获取公共Header参数

弹性伸缩 ESS 调用专有云API时需要提供多个Header参数。本文为您介绍这些参数的含义及其获取方式，并对调用后的一些返回值做出解释。

**Header参数描述**

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，获取方式，请参见获取Region ID。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID，获取方式，请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID，获取方式，请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID，获取方式，请参见获取实例ID。 |

**获取Region ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看Region ID。

**获取组织ID**

组织ID需要通过API进行获取，获取方式，请参见《**Apsara Uni-manager****运营控制台开发指南》**中的《**GetOrganizationList**》章节。

**获取资源集ID**

资源集ID需要通过API进行获取，获取方式，请参见《**Apsara Uni-manager****运营控制台开发指南》**中的《**ListResourceGroup**》章节。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以弹性伸缩为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品** > **弹性计算** > **弹性伸缩**。
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

弹性伸缩 ESS

### 获取弹性伸缩的SDK包

通过POP网关调用专有云API时，您需要使用弹性伸缩的SDK。本文为您介绍如何获取阿里云开发工具包 （SDK）。

**背景介绍**

实现弹性伸缩功能需要您同时安装弹性伸缩SDK和阿里云核心库。以Java SDK为例，您需要下载aliyunjava-sdk-ess以及aliyun-java-sdk-core。 弹性伸缩SDK封装了2014-08-28版本API，以访问密钥（AccessKey）识别调用者身份，提供自动签名等功能，方便您通过API创建和管理资源。阿里云开发工具包（SDK）包括代码以及示例，您可以自行选择语言来创建云应用。 SDK核心库推荐您使用阿里云官网的SDK核心库，该内容适用于所有云产品，也同样适用于专有云产品。

**操作指导**

目前SDK工具包支持Java、Python、Go等多种语言，您可以前往弹性伸缩开发工具包（SDK）中选择对应版本。

**重要**

推荐您使用 Java、Python、Go三种语言的SDK工具包，使用其他语言的SDK工具包可能会发生不兼容的情况。 弹性伸缩 ESS

## Java SDK调用示例

### 快速开始

本节为您介绍如何获取弹性伸缩的Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体获取弹性伸缩的Endpoint，具体操作，请参见获取弹性伸缩的Endpoint。 阿里云专有云Java SDK需要1.8及以上版本的JDK。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用弹性伸缩的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17 及以上版本，SDK的版本为2.1.1。

**使用Java SDK**

本示例以SubmitJob为例，为您介绍调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际产品的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下所示： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Product>，请替换为您实际的产品名称。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <readTimeout>，请您根据实际情况设置读取超时时间，单位为毫秒。 <connectionTimeout>，请您根据实际情况设置连接超时时间，单位为毫秒。 <maxRequestsPerHost>，请您根据实际情况设置每个主机的最大请求数。 <maxRequests>，请您根据实际情况设置最大请求数。 <http://192.168.XX:33XX>，请替换为您实际的代理IP和相应端口。

```java
 import com.aliyuncs.profile.DefaultProfile;
 import com.aliyuncs.DefaultAcsClient;
 import com.aliyuncs.IAcsClient;
 import com.aliyuncs.exceptions.ClientException;
 import com.aliyuncs.exceptions.ServerException;
 import com.aliyuncs.ess.model.v20140828.*;
 public class Main {
publicstaticvoidmain(String[]args){
```

弹性伸缩 ESS

```
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
        clientConfig.setIgnoreSSLCerts(true);                        // 忽略证书
        clientConfig.setReadTimeoutMillis(<readTimeout>);            // 读取超时时间（可
```

选），单位为毫秒（`ms`）

```
        clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// 连接超时时间（可
```

选），单位为毫秒（`ms`）

```
        clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);    // 设置每个主机的最
```

大请求数（可选）

```
        clientConfig.setMaxRequests(<maxRequests>);                  // 设置最大请求数（
```

可选）

```
        clientConfig.setProtocolType(ProtocolType.HTTP);             // 设置请求协议，默
```

认`HTTP`（可选） `/*` 设置代理(可选)，替换为代理`IP`和`Port`

```
        clientConfig.setHttpProxy("http://192.168.XX:33XX");
```

或

```
        clientConfig.setHttpsProxy("https://192.168.XX:33XX");
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```
        DescribeScalingGroupsRequest request = new DescribeScalingGroupsRequest();
```

`//` 业务参数

```
        request.setPageSize(10);
        request.setPageNumber(1);
```

`//` 特殊`Header`参数，设置组织`ID`和资源集`ID`，资源隔离使用

```
        request.putHeadParameter("x-acs-organizationid", "1");
        request.putHeadParameter("x-acs-resourcegroupid", "11");
```

`//` 发起请求并处理应答或异常

```
        DescribeScalingGroupsResponse response;
        try {
            response = client.getAcsResponse(request);
            }
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
        }
     }
 }
```

### 使用手册

#### 安装Java SDK

弹性伸缩 ESS 本文为您介绍如何安装及调用弹性伸缩的Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，您可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用弹性伸缩的开发工具包，您必须安装阿里云Java SDK核心库以及弹性伸缩的Java SDK。SDK核心库推荐使用4.5.17及以上版本，Java SDK的版本为2.1.1。 以使用弹性伸缩的Java SDK为例，您需要安装阿里云Java SDK核心库和弹性伸缩 Java SDK，并在 pom.xml文件中添加以下依赖即可。关于准确的SDK版本号，请参见阿里云开发工具包（SDK）。

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- ess java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-ess</artifactId>
    <version>2.1.1</version>
</dependency>
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文为您介绍了目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的具体方法，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 请您确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将

**重要**

会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret` 以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。

#### 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。 弹性伸缩 ESS

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

本文为您介绍如何使用弹性伸缩的Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。 弹性伸缩 ESS

```
CreateScalingGroupRequest request = new CreateScalingGroupRequest();
```

`//` 业务参数

```
request.setPageSize(10); request.setPageNumber(1);
```

`//` 特殊`Header`参数，设置组织`ID`和资源集`ID`，资源隔离使用

```
request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "");
```

3. 发起调用并处理应答。

```java
CreateScalingGroupRequest request = new CreateScalingGroupRequest(); request.setRegionId("cn-hangzhou"); request.setMinSize("0"); request.setMaxSize(1); try { client.getCreateScalingGroupResponse(request);
    System.out.println(response.getScalingGroups());
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
}
```

正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 `response.getXXX()` 来获得应答中的字段。

```java
System.out.println(response.getScalingGroups());
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

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码： 弹性伸缩 ESS

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

#### 使用CommonRequest进行调用

当您要调用的弹性伸缩的某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回 Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用 CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下所示：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。您需要获取**Action**参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 例如查看伸缩活动的API接口**DescribeScalingActivities**，在发起CommonRequest请求时，要使用 `request.ApiName = "DescribeScalingActivities"` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为弹性伸缩的**CreateScalingGroup**接口获取实例状态列表的调用示例。 弹性伸缩 ESS 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP和相应端口。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile;
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
        clientConfig.setHttpProxy("http://192.168.XX.XX:33XX");
```

请替换为实际代理`IP`和端口 `*/`

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
        request.setDomain("ess.aliyuncs.com");
        request.setSysProduct("ess");
        request.setVersion("2014-08-28");
        request.setAction("CreateScalingGroup");
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

弹性伸缩 ESS

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

弹性伸缩 ESS

## Python SDK调用示例

### 快速开始

本文为您介绍如何获取弹性伸缩的Python SDK并开始调用。

**环境准备**

使用阿里云专有云Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret 获取弹性伸缩的Endpoint，具体操作，请参见获取弹性伸缩的Endpoint。
1. 安装SDK核心库。
如果您使用的是Python 2.x.x，请执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x.x，请执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

2. 安装SDK。
以下以安装弹性伸缩的SDK为例： 如果您使用的是Python 2.x.x，请执行以下命令，安装弹性伸缩的SDK：

```
pip install aliyun-python-sdk-ess
```

如果您使用的是Python 3.x.x，请执行以下命令，安装弹性伸缩的SDK：

```
pip3 install aliyun-python-sdk-ess
```

**使用Python SDK**

本文以为**CreateScalingGroup**例，介绍调用阿里云专有云Python SDK的主要操作步骤：
1. 创建Client实例。
在创建Client实例时，您需要获取Region ID、AccessKey ID以及AccessKey Secret信息。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下所示： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ess.aliyuncs.com>，请替换为您实际的产品访问地址。 弹性伸缩 ESS

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkess.request.v20140828 import CreateScalingGroupRequest
# global config
```

`region_id = '<yourRegionID>' #` 请替换为您实际的地域`ID` `access_key = '<yourAccessKeyID>' #` 请替换为您实际的的`AccessKey ID`

```bash
acces_secret = '<yourAccessKeySecret>' # 请替换为您实际的AccessKey Secret
# product config
```

`product_name = 'ess' #` 填写产品名称 `endpoint = '<ess.aliyuncs.com>' #` 产品访问域名，当前为示例值，请替换为您实际的产品访问地址

```bash
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
```

`request.set_accept_format('json') #` 设置返回数据格式

```bash
# get response
response = clt.do_action_with_exception(request) print response
```

### 使用手册

#### 安装Python SDK

本文为您介绍如何安装及调用弹性伸缩的Python SDK。

**背景信息**

阿里云专有云Python SDK支持Python 2.7、Python 3.x环境，您可以通过pip安装专有云Python SDK。

**说明**

使用产品的开发工具包，必须安装阿里云Python SDK核心库。例如，如果您想使用弹性伸缩的Python SDK，您需要安装阿里云Python SDK核心库和弹性伸缩的Python SDK。

**操作步骤**

本文以使用Python 2.7或Python 3.x为例。

**重要**

Python代码的最后一行需要添加空行，否则会引起提示性的告警。
1. 执行以下命令安装阿里云SDK核心库。
如果您使用的是Python 2.7或Python 3.x，请执行以下命令安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

2. 执行以下命令，安装弹性伸缩的SDK。

```
pip install aliyun-python-sdk-ess==2.3.19
```

弹性伸缩 ESS

**说明**

`aliyun-python-sdk-ess` 的版本为2.3.19作为示例，最新版本请以SDK的发布版本为准。

#### 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的具体方法，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 请您确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将

**重要**

会危害您的信息安全。

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。

#### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。

**说明**

产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。

| 行 | python -c "import ssl" | 检查Pyth |
|---|---|---|
| ImportError: No module named ssl |  |  |

若没有OpenSSL，运行以下命令安装： `pip install pyopenssl # Python 2`使用此命令。

**说明**

若本地环境为Python 3，则运行 `pip3 install pyopenssl` 命令。

**设置单个请求的HTTP/HTTPS协议**

参考以下代码示例为一个接口设置HTTPS调用： 弹性伸缩 ESS

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

#### 发起调用

本文为您介绍如何使用弹性伸缩的Python SDK发起请求。

**操作步骤**

1. 导入弹性伸缩的SDK。

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkess.request.v20140828 import DescribeScalingGroupsRequest
```

2. 新建一个AcsClient。

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. 创建Request对象。

```
request.set_accept_format('json')
```

4. 发起调用并打印返回结果。

```
response = clt.do_action_with_exception(request) print response
```

#### 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

弹性伸缩 ESS 如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

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

当您要调用的弹性伸缩的API没有提供SDK时，或者提供的SDK中的请求Request参数以及返回Response 值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下所示：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在弹性伸缩的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。您需要获取**Action**参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 例如查看伸缩活动的API接口**DescribeScalingActivities**，在发起CommonRequest请求时，要使用 `request.ApiName = "DescribeScalingActivities"` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为弹性伸缩的**CreateScalingGroup**接口获取实例状态列表的调用示例： 弹性伸缩 ESS 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <ess.aliyuncs.com>，请替换为您实际的产品访问地址。 弹性伸缩 ESS

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('ess') request.set_version('2014-08-28')
```

`request.set_domain('<ess.aliyuncs.com>') #`产品访问域名，当前为示例值，请替换为您实际的产品访问地址

```bash
# or:
# request = = CommonRequest(product='ess',
action_name='CreateScalingGroup',version='2014-08-28',domain='ess.aliyuncs.com')
######
```

# 设置请求协议类型，支持`https`或`http`，默认为`http`
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

弹性伸缩 ESS

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您无需进行复杂编程即可访问。本文为您介绍如何获取阿里云弹性伸缩的Go SDK并开始调用。

**环境准备**

使用阿里云专有云Go SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具获取弹性伸缩的Endpoint，具体操作，请参见获取弹性伸缩的Endpoint。

**安装阿里云Go SDK核心包**

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**使用Go SDK**

以下代码以**DescribeScalingGroups**接口为例，展示了调用阿里云Go SDK的主要操作步骤：
1. 初始化Client实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您实际的Endpoint。 弹性伸缩 ESS

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ess"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

)

```
func main() {
```

`//` 创建`essClient`实例

```
    essClient, err := ess.NewClientWithAccessKey(
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
    request := ess.CreateDescribeScalingGroupsRequest()
```

`//` 设置当前产品的`Endpoint`

```
    request.Domain = "<Endpoint>"
    // 等价于 request.PageSize = "10"
    request.PageSize = requests.NewInteger(10)
```

`//` 发起请求并处理异常

```
    response, err := Client.DescribeScalingGroups(request)
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

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文为您介绍了目前Go SDK支持通过AccessKey进行身份验证，获取AccessKey的具体方法，请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。 弹性伸缩 ESS 请您确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将

**重要**

会危害您的阿里云账号的信息安全。 以下代码以弹性伸缩为例，展示初始化essClient实例的方法。 `//` 初始化`ecsClient`实例

```
essClient, err := ess.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。

#### 发起调用

本文介绍使用弹性伸缩的Go SDK发起调用的方法。 以下步骤以弹性伸缩为例，展示使用弹性伸缩的Go SDK发起调用的方法。
1. 导入弹性伸缩的Go SDK。

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/ess
```

2. 新建一个AcsClient，该client中包含产品名的所有API。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 `essClient,err := <ess>.NewClientWithAccessKey( //`请替换为您实际的产品名称 `"<yourRegionID>", //` 请替换为您实际的`RegionID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>") //` 请替换为您实际的`AccessKeySecret` `essClient.Domain = "ess.aliyuncs.com" //`设置请求域名地址，当前为示例值，请求根据实际请求地址替换。

| xxx.CreateXXXRequest |  | 方法创建一个请求。 |
|---|---|---|
| 法的命名规范为 |  |  |

**${service}**为产品名称(小写)。例如ess。
**${apiName}**为API名称，例如DescribeScalingGroups。

```
request := ess.CreateDescribeScalingGroupsAttributeRequest() request.InstanceId = ""
```

4. 发起调用。

```
response, err := essClient.DescribeScalingGroupsAttribute(request)
```

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。 弹性伸缩 ESS

**简单处理异常**

以**DescribeScalingGroups**接口为例，您可以通过以下代码来简单处理错误。

```
response,err := essClient.DescribeScalingGroups(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现error且无法自动化处理时，SDK会返回一个 `ClientError` 。 以下以弹性伸缩的**DescribeScalingGroups**接口为例，您可以通过以下代码来判断并获取 `ClientError` 中的错误信息：

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，具体引入方法请参见： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/ess" //请替换为您实际的产品名称 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

```
response, err := essClient.DescribeScalingGroups(request) if clientError, ok := err.(*errors.ClientError); ok{
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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以弹性伸缩的**DescribeScalingGroups**接口为例，您可以通过以下代码来判断并获取ServerError 以及Response中的错误信息： 弹性伸缩 ESS

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，具体引入方法请参见： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/ess" //请替换为您实际的产品名称 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

```
response, err := essClient.DescribeScalingGroups(request) if serverError, ok := err.(*errors.ServerError); ok{
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

当您要调用的弹性伸缩的某个API没有提供SDK时，或者提供的SDK中的请求Request参数以及返回 Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用 CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下所示：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在弹性伸缩的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。您需要获取**Action**参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 例如查看伸缩活动的API接口**DescribeScalingActivities**，在发起CommonRequest请求时，要使用 `request.ApiName = "DescribeScalingActivities"` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为弹性伸缩的**DescribeScalingActivities**接口获取实例状态列表的调用示例： 弹性伸缩 ESS 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ess.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 弹性伸缩 ESS

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

`request.Domain = "<ess.aliyuncs.com>" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "ess"
    request.Version = "2014-08-28"
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

弹性伸缩 ESS

## API参考

### API使用须知

在调用弹性伸缩OpenAPI之前，您需要在弹性伸缩控制台将OpenAPI权限授予弹性伸缩。 如果不符合条件，将出现异常，如下表所示。表 1. 错误说明

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unsubscribe d | Do not have permission to access this API. | 您未开通弹性伸缩，无权调用该API。 |
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您未向弹性伸缩完整授权 OpenAPI接口。 |

### 调用方式

对弹性伸缩API接口调用是通过向弹性伸缩API的服务端地址发送HTTP GET请求，并按照接口说明在请求中加入相应请求参数来完成的。根据请求的处理情况，系统会返回处理结果。

### 请求结构

本章节介绍发起API请求的结构。 服务地址通信协议支持通过HTTP或HTTPS通道进行请求通信。为了获得更高的安全性，推荐您使用HTTPS通道发送请求。 请求方法支持HTTP GET方法发送请求，这种方式的请求参数需要包含在请求的URL中。 请求参数每个请求都需要指定要执行的操作，即Action参数（例如CreateScalingGroup），并且每个操作都需要包含公共请求参数和指定操作所特有的请求参数。 字符编码请求及返回结果都使用UTF-8字符集进行编码。

### 公共参数

**公共请求参数**

公共请求参数是每个接口调用都需要提供的请求参数，如下表所示：

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| Format | Strin g | 否 | 返回参数的语言类型，仅支持JSON。 |
|---|---|---|---|
| Version | Strin g | 是 | API版本号，以日期形式YYYY-MM-DD输入，取值： 2014-08-28。 |
| AccessKeyId | Strin g | 是 | 访问服务使用的密钥ID。 |
| AccessKeySe cret | Strin g | 是 | 访问服务使用的密钥值。 |
| RegionId | Strin g | 是 | 访问服务所使用的地域ID。 |
| Action | Strin g | 是 | API的名称。 |
| Product | Strin g | 是 | 接口对应的产品名称，取值：Ess。 |

| 名称 | 描述 |
|---|---|
| x-acs-organizationId | Apsara Uni-manager运营控制台上的组织ID，获取方式，请参见获取组织 ID。 |
| x-acs-resourcegroupId | Apsara Uni-manager运营控制台上的资源集ID，获取方式，请参见获取资源集ID。 |
| x-acs-instanceId | 进行操作的实例ID，获取方式，请参见获取实例ID。 |

**说明**

在调用弹性伸缩API接口时，您需要在调用代码的请求头Header中添加**x-acs-organizationid**、**x-**
**acs-resourcegroupid**、**x-acs-instanceid**等参数的实际值，用于指定当前实例的实例ID（在创
建实例和查询实例列表的场景下，实例ID不存在），及其所属的组织和资源集。若未添加相关Header 参数实际值，调用时则会默认指向root组织和root资源集。

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx HTTP或5xx HTTP状态码代表调用失败。 弹性伸缩 ESS 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

### 返回结果

#### 成功结果

调用API服务后返回数据采用统一格式，返回的HTTP状态码为2xx，代表调用成功；返回4xx或5xx的HTTP 状态码代表调用失败。调用成功返回的数据格式主要有XML和JSON两种。外部系统可以在请求时传入参数来制定返回的数据格式，默认为XML格式。 本文档中的返回示例为了便于查看，做了格式化处理，实际返回结果没有进行换行、缩进

**说明**

等处理。 XML示例： XML返回结果包括请求是否成功信息和具体的业务数据。

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

<!--结果的根结点`-->` <接口名称`+Response>` <!--返回请求标签`-->`

```xml
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
```

<!--返回结果数据`-->` `</`接口名称`+Response>` JSON示例

```json
{
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
```

`/*` 返回结果数据 `*/`

```
}
```

#### 错误结果

调用接口出错后，将不会返回结果数据。调用方可根据各个接口定义的错误码或附表客户端错误以及服务器端错误来定位错误原因。 当调用出错时，HTTP请求返回一个4xx或5xx的HTTP状态码。返回的消息体中是具体的错误代码及错误信息。另外还包含一个全局唯一的请求ID：RequestId和一个您该次请求访问的站点ID：HostId。 XML示例

```xml
<?xml version="1.0" encoding="UTF-8"?> <Error>
   <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId>
   <HostId>ess.example.com</HostId>
   <Code>UnsupportedOperation</Code>
   <Message>The specified action is not supported.</Message>
</Error>
```

JSON示例弹性伸缩 ESS

```json
{
    "RequestId": "8906582E-6722-409A-A6C4-0E7863B733A5",
    "HostId": "ess.example.com",
    "Code": "UnsupportedOperation",
    "Message": "The specified action is not supported."
}
```

### 签名机制

本章节介绍如何在访问过程中使用签名机制标识身份。 弹性伸缩会对每个访问的请求进行身份验证，因此使用HTTP或者HTTPS协议提交请求时，都需要在请求中包含签名（Signature）信息。弹性伸缩使用AccessKey ID和AccessKey Secret进行对称加密，以验证请求发送者的身份。您可以在Apsara Stack控制台中获取AccessKey ID和AccessKey Secret，获取方式请参见获取AccessKey。其中AccessKey ID用于标识访问者的身份，AccessKey Secret用于加密签名字符串和服务器端验证签名字符串，必须严格保密。 在访问时，请按照下面的步骤对请求进行签名处理：
1. 使用请求参数构造规范化的请求字符串（Canonicalized Query String）。
i. 按照参数名称的字母顺序对请求中所有的请求参数进行排序，其中请求参数包括文档中描述的公共请求参数和给定请求接口的自定义参数，但不能包括公共请求参数中提到的Signature参数本身。 当使用GET方法提交请求时，这些参数是请求URL中的参数部分，即URL中 ? 之后由 & 连接的部分。 ii. 对每个请求参数的名称和值进行编码。 名称和值要使用UTF-8字符集进行URL编码，URL编码的编码规则是： 不编码字符A-Z、a-z、0-9以及字符连接号（-）、下划线（_）、点号（.）和波浪线（~）。

| 成 | %XY |  |  |  |
|---|---|---|---|---|
| %22 |  |  |  |  |
|  |  | 。 |  |  |
|  |  |  | 成 %XY%ZA… |  |
|  |  |  | %20 | ，而不 |

一般支持URL编码的库（例如Java中的java.net.URLEncoder）都按

**说明**

照 `application/x-www-form-urlencoded` 的MIME类型规则进行编码。实现时可以直接使用这类方式进行编码，将编码后的字符串中的加号（+）替换成 %20 、星号（*）替换成 %2A 、 %7E 替换回波浪线（~），即可得到上述规则描述的编码字符串。 iii. 使用英文等号（=）连接编码后的参数名称和值。 iv. 将英文等号（=）连接得到的字符串按参数名称的字母顺序使用and（&）符号连接，即得到规范化请求字符串。
2. 使用构造出的规范化字符串，按照以下规则构造用于计算签名的字符串。

```
 StringToSign=
 HTTPMethod + “&” +
 percentEncode(“/”) + “&” +
 percentEncode(CanonicalizedQueryString)
```

3. 按照RFC2104的定义，使用构造出的用于计算签名的字符串计算签名HMAC值。
计算签名时使用的Key就是用户持有的AccessKey Secret并加上一个and（&）字符（ASCII为38）， 使用的哈希算法是SHA1。
4. 按照Base64编码规则将HMAC值编码成字符串，即得到签名值（Signature）。
弹性伸缩 ESS
5. 将得到的签名值作为Signature参数添加到请求参数中，即完成请求签名的过程。
得到的签名值在作为最后的请求参数值提交给ECS服务器的时候，要和其他参数一样，按照RFC3986的规则进行URL编码。

```
http://ess.example.com/?TimeStamp=2014-08- 15T11%3A10%3A07Z&Format=xml&AccessKeyId=testid&Action=DescribeScalingGroups&SignatureMeth =HMAC-SHA1&RegionId=cn-qingdao&SignatureNonce=1324fd0e-e2bb-4bb1-917cbd6e437f****&SignatureVersion=1.0&Version=2014-08-28
```

则StringToSign后为：

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeScalingGroups&Format%3Dxml&RegionId%3Dcnqingdao&SignatureMethod%3DHMAC-SHA1&SignatureNonce%3D1324fd0e-e2bb-4bb1-917c-bd6e437f** *&SignatureVersion%3D1.0&TimeStamp%3D2014-08-15T11%253A10%253A07Z&Version%3D2014-08-28
```

假设使用的AccessKey ID为testid， AccessKey Secret为testsecret，用于计算HMAC的Key就是 testsecret&，则计算得到的签名值是**SmhZuLUnXmqxSEZ%2FGqyiwGqmf%2BM=**。 签名后的请求URL为：

```
http://ess.example.com/?TimeStamp=2014-08- 15T11%3A10%3A07Z&Format=xml&AccessKeyId=testid&Action=DescribeScalingGroups&SignatureMeth =HMAC-SHA1&RegionId=cn-qingdao&SignatureNonce=1324fd0e-e2bb-4bb1-917cbd6e437f****&SignatureVersion=1.0&Version=2014-08- 28&Signature=SmhZuLUnXmqxSEZ%2FGqyiwGqmf%****
```

请求URL中增加了Signature参数。

### 伸缩组

#### CreateScalingGroup

**接口说明**

伸缩组是具有相同应用场景的ECS实例的集合。 最多支持在一个地域下创建50个伸缩组。 伸缩组创建成功后不会立即生效。您需要先调用API EnableScalingGroup接口启用伸缩组，伸缩组才能触发伸缩活动和执行伸缩规则。 伸缩组关联的负载均衡实例和关联的RDS实例必须在同一个地域。更多信息，请参见云服务器ECS文档中的地域与可用区章节。 如果您为伸缩组关联了负载均衡实例，伸缩组会自动将加入伸缩组的ECS实例添加到负载均衡实例的后端服务器组。ECS实例在加入负载均衡实例的后端服务器组后，权重默认为50。负载均衡实例需要满足以下条件： 该负载均衡实例的状态必须是active，您可以调用 API DescribeLoadBalancers接口查看指定负载均衡实例的状态。 该负载均衡实例配置的所有监听端口必须开启健康检查，否则伸缩组创建失败。 如果您为伸缩组关联了RDS实例，伸缩组会自动将加入伸缩组的ECS实例的内网IP添加到RDS实例的访问白名单。RDS实例需要满足以下条件： 该RDS实例的状态必须是Running，您可以调用API DescribeDBInstances接口查看指定RDS实例的状态。 弹性伸缩 ESS 该RDS实例访问白名单的IP数不能超过上限值。更多信息，请参见云数据库RDS文档中的设置白名单相关内容。 如果伸缩组的MultiAZPolicy设置为COST_OPTIMIZED： 当指定OnDemandBaseCapacity、OnDemandPercentageAboveBaseCapacity参数时，即指定成本优化策略下的实例分配方式，在扩缩容时将优先满足该实例分配方式。 当不指定OnDemandBaseCapacity、OnDemandPercentageAboveBaseCapacity参数时，成本优化策略下将仅按照成本最低的方式进行实例创建。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateScalingGr oup | 系统规定参数。取值： CreateScalingGroup。 |
| MaxSize | Integer | 是 | 20 | 伸缩组内ECS实例台数的最大值，取值范围：0~1000。当伸缩组内ECS实例数大于MaxSize时，弹性伸缩会自动移出ECS 实例。 |
| MinSize | Integer | 是 | 2 | 伸缩组内ECS实例台数的最小值，取值范围：0~1000 。当伸缩组内ECS实例数小于MinSize时，弹性伸缩会自动创建ECS实例。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。更多信息，请参见云服务器ECS文档中的地域与可用区章节。 |
| ScalingGroupNa me | String | 否 | scalinggroup**** | 伸缩组的名称，同一地域下伸缩组名称唯一。长度为2~64个英文或中文字符，以数字、大小英文字母或中文开头，可以包含数字、下划线（ ）、短划线（-）和半角 _ 句号（.）。 如果没有指定该参数，默认值为伸缩组 ID。 |
| LaunchTemplate Id | String | 否 | lt- m5e3ofjr1zn1aw 7**** | 实例启动模板ID，用于指定伸缩组从实例启动模板获取启动配置信息。 |
| LaunchTemplate Version | String | 否 | Default | 实例启动模板的版本，取值范围： 固定的模板版本号。 Default：始终使用模板默认版本。 Latest：始终使用模板最新版本。 |
| InstanceId | String | 否 | i-28wt4**** | ECS实例的ID。创建伸缩组时，将从指定的实例获取所需的配置信息，并自动创建伸缩配置。 |

弹性伸缩 ESS

| DefaultCooldow n | Integer | 否 | 300 | 一次伸缩活动（添加或移出ECS实例）结束后的一段冷却时间。取值范围： 0~86400，单位：秒。 默认值：300。 说明冷却时间内，该伸缩组不执行其他的伸缩活动，仅针对云监控报警任务触发的伸缩活动有效。 |
|---|---|---|---|---|
| LoadBalancerIds | String | 否 | ["lb- bp1u7etiogg38y vwz****", "lb- bp168cqrux9ai9l 7f****", "lb- bp1jv3m9zvj22u fxp****"] | 负载均衡实例ID。取值可以是由多台负载均衡实例ID组成一个JSON数组，最多支持 5个ID，ID之间用半角逗号（,）隔开。 |
| DBInstanceIds | String | 否 | ["rm- bp142f86de0t7* ***", "rm- bp18l1z42ar4o* ***", "rm- bp1lqr97h4aqk* ***"] | RDS实例ID。取值可以是由多台RDS实例 ID组成一个JSON数组，最多支持8个 ID，ID之间用半角逗号（,）隔开。 |
| RemovalPolicy.1 | String | 否 | OldestScalingCo nfiguration | 指定实例移出策略的第一段筛选策略。更多详情，请参见移出策略相关内容。取值范围： OldestInstance：移出最早加入伸缩组的ECS实例。 NewestInstance：移出最新加入伸缩组的ECS实例。 OldestScalingConfiguration：移出最早伸缩配置创建的ECS实例。 仅当RemovalPolicy.1和 RemovalPolicy.2均未设置取值时，RemovalPolicy.1的默认值为 OldestScalingConfiguration。 |
| RemovalPolicy.2 | String | 否 | OldestInstance | 指定实例移出策略的第二段筛选策略，不允许与RemovalPolicy.1取值相同。更多详情，请参见移出策略相关内容。取值范围： OldestInstance：移出最早加入伸缩组的ECS实例。 NewestInstance：移出最新加入伸缩组的ECS实例。 OldestScalingConfiguration：移出最早伸缩配置创建的ECS实例。 仅当RemovalPolicy.1和 RemovalPolicy.2均未设置取值时，RemovalPolicy.2的默认值为 OldestInstance。 |

弹性伸缩 ESS

| VSwitchId | String | 否 | vsw- 5le3tkkyc8b7jhr 2g**** | 创建VPC类型的伸缩组时，指定的虚拟交换机ID。 |
|---|---|---|---|---|
| MultiAZPolicy | String | 否 | PRIORITY | 多可用区伸缩组ECS实例扩缩容策略。取值范围： PRIORITY：根据您定义的虚拟交换机 （VSwitchIds.N）扩缩容。当优先级较高的虚拟交换机所在可用区无法创建 ECS实例时，自动使用下一优先级的虚拟交换机创建ECS实例。 BALANCE：在伸缩组指定的多可用区之间均匀分配ECS实例。如果由于库存不足等原因可用区之间变得不平衡，您可以调用API RebalanceInstance接口平衡资源。 默认值：PRIORITY 。 |
| HealthCheckTyp e | String | 否 | ECS | 伸缩组的健康检查方式，取值范围： NONE：不做健康检查。 ECS：对伸缩组内的ECS实例做健康检查。 |
| ScalingPolicy | String | 否 | recycle | 指定伸缩组的回收模式，取值范围： recycle：伸缩组的回收模式为停机回收模式。 release：伸缩组的回收模式为释放模式。 关于被移出实例的动作，请参见API RemoveInstances。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多详情，请参见云服务器ECS文档中的如何保证幂等性章节。 |
| OnDemandBase Capacity | Integer | 否 | 30 | 伸缩组所需要按量实例个数的最小值，取值范围：0~1000。当按量实例个数少于该值时，将优先创建按量实例。 |
| OnDemandPerce ntageAboveBase Capacity | Integer | 否 | 20 | 伸缩组满足最小按量实例数 （OnDemandBaseCapacity）要求后， 超出的实例中按量实例应占的比例，取值范围：0～100。 |
| DesiredCapacity | Integer | 否 | 5 | 伸缩组内ECS实例的期望数量，伸缩组会自动将ECS实例数量维持在期望实例数。 取值不得大于MaxSize，且不得小于 MinSize。 |

弹性伸缩 ESS

| GroupDeletionPr otection | Boolean | 否 | true | 是否开启伸缩组删除保护。取值范围： true：开启伸缩组删除保护，此时不能删除该伸缩组。 false：关闭伸缩组删除保护。 默认值：false。 |
|---|---|---|---|---|
| GroupType | String | 否 | ECS | 伸缩组管理的实例类型。取值范围： ECS：伸缩组内管理的伸缩为ECS实例。 ECI：伸缩组内管理的伸缩为ECI实例。 默认值：ECS。 |
| ContainerGroupI d | String | 否 | eci- bp13fm93jggsvj nuad3z | ECI容器组ID。 |
| AzBalance | Boolean | 否 | false | 伸缩组的容量是否在多个可用区间均衡分布（仅当 MultiAZPolicy 参数取值为 COMPOSABLE 策略时生效），取值范围： true：伸缩组的容量在多个可用区间均衡分布。 false：伸缩组的容量不在多个可用区间均衡分布。 默认值：false。 |
| AllocationStrate gy | String | 否 | priority | 容量分配策略，决定了伸缩组如何选择可用的实例规格类型满足容量。容量分布策略同时对按量容量生效（仅当 MultiAZPolicy 参数取值为 COMPOSABLE 策略时生效）。取值范围： priority：按照配置的实例规格的顺序创建实例。 lowestPrice：按照实例规格单位vCpu 价格从低到高创建实例。 默认值：priority。 |

|  | MultiAZPolicy |
|---|---|
| COMPOSABLE |  |

弹性伸缩 ESS

| VSwitchIds.N | RepeatL ist | 否 | vsw- 5le3tkkyc8b7jhr 2g**** | 一台或多台虚拟交换机的ID，N的取值范围：1~5。 如果您使用了VSwitchIds.N参数，VSwitchId参数将被忽略。 只有当伸缩组网络类型为VPC时，当前参数才生效。指定虚拟交换机所属的 VPC必须和伸缩组所属的VPC相同。 虚拟交换机可以来自多个可用区。虚拟交换机的优先级按照数字升序排序，1 表示最高优先级。当优先级较高的虚拟交换机所在可用区无法创建ECS实例时，自动选择下一优先级的虚拟交换机创建ECS实例。 |
|---|---|---|---|---|
| LifecycleHook.N. DefaultResult | String | 否 | CONTINUE | 等待状态结束后的下一步动作，取值范围： CONTINUE：继续响应弹性扩张活动或者继续响应弹性收缩活动。 ABANDON：直接释放弹性扩张活动创建出来的ECS实例或者直接将弹性收缩活动中的ECS实例从伸缩组移除。 默认值：CONTINUE。 当伸缩组发生弹性收缩活动（SCALE IN） _ 并触发多个生命周期挂钩时，DefaultResult取值为ABANDON的生命周期挂钩触发的等待状态结束时，会提前将其他对应的等待状态结束。其他情况下，均以最后一个结束等待状态的下一步动作为准。 |
| LifecycleHook.N. LifecycleHookNa me | String | 否 | lifecycle hook _ | 生命周期挂钩名称，用于指定生命周期挂钩，不支持修改。 |
| LifecycleHook.N. LifecycleTransiti on | String | 否 | SCALE OUT _ | 生命周期挂钩适用的伸缩活动类型，取值范围： SCALE OUT：伸缩组弹性扩张活动。 _ SCALE IN：伸缩组弹性收缩活动。 _ |
| LifecycleHook.N. NotificationMeta data | String | 否 | Test | 伸缩活动的等待状态的固定字符串信息。 参数长度不能超过128个字符。弹性伸缩每次推送消息到通知对象时，会同时发送您预先指定的NotificationMetadata参数值，便于管理和标记不同类别的通知信息。当您同时指定了NotificationArn参数时，NotificationMetadata参数方可生效。 |

弹性伸缩 ESS

| LifecycleHook.N. NotificationArn | String | 否 | acs:ess:cn- hangzhou-env1- d01:111111111 1:queue/queue2 d01d | 生命周期挂钩通知对象标识符，支持消息服务MNS队列或主题，参数取值格式： acs:ess:{region}:{account-id}: {resource-relative-id}。 region：伸缩组所在的地域。 account-id：阿里云账号ID。 例如： MNS队列：acs:ess:{region}: {account- id}:queue/{queuename}。 MNS主题：acs:ess:{region}: {account-id}:topic/{topicname}。 |
|---|---|---|---|---|
| LifecycleHook.N. HeartbeatTimeo ut | Integer | 否 | 600 | 生命周期挂钩为伸缩组活动设置的等待时间，等待状态超时后会执行下一步动作。 取值范围：30~21600，单位：秒。 默认值：600。 创建了生命周期挂钩后，您可以调用API RecordLifecycleActionHeartbeat接口延长ECS实例的等待时间，也可以调用 CompleteLifecycleAction接口提前结束伸缩活动的等待状态。 |
| VServerGroup.N. VServerGroupAtt ribute.N.VServer GroupId | String | 否 | rsp- bp1443g77**** | 虚拟服务器组ID。 更多信息，请参见API AttachVServerGroups。 |
| VServerGroup.N. VServerGroupAtt ribute.N.Weight | Integer | 否 | 100 | 弹性伸缩将ECS实例添加到虚拟服务器组时设置的权重，取值范围：0~100。 默认值：50。 更多信息，请参见API AttachVServerGroups。 |
| VServerGroup.N. VServerGroupAtt ribute.N.Port | Integer | 否 | 22 | 弹性伸缩将ECS实例添加到虚拟服务器组时使用的端口号，取值范围：1~65535。 更多信息，请参见API AttachVServerGroups。 |
| VServerGroup.N. LoadBalancerId | String | 否 | lb- bp1u7etiogg38y vwz**** | 虚拟服务器组所属负载均衡实例的ID。 更多信息，请参见API AttachVServerGroups。 |
| Tag.N.Key | String | 否 | Department | 伸缩组的标签键。 |
| Tag.N.Value | String | 否 | Finance | 伸缩组的标签值。 |

弹性伸缩 ESS

| Tag.N.Propagate | Boolean | 否 | false | 标识该标签是否为可传播标签，取值范围： true：伸缩组上的标签只会传播到新创建的实例上，而不会传播到已经在伸缩组中运行的实例上。 false：伸缩组上的标签不会传播到实例上。 默认值：false。 |
|---|---|---|---|---|
| LaunchTemplate Override.N.Insta nceType | String | 否 | ecs.c5.xlarge | 当您需要伸缩组按照实例规格容量进行伸缩时，请同时指定本参数和 LaunchTemplateOverride.N.Weighte dCapacity。 本参数用于指定实例规格，会覆盖启动模板中的实例规格。您可以指定N个本参数， 扩展启动模板支持N个实例规格。N的取值范围：1~10。 说明仅当 LaunchTemplateId参数指定了启动模板时，本参数生效。 InstanceType的取值范围：在售的ECS实例规格，请参见云服务器ECS文档中的实例规格族章节。 |
| LaunchTemplate Override.N.Weig htedCapacity | Integer | 否 | 4 | 当您需要伸缩组按照实例规格容量进行伸缩时，在指定 LaunchTemplateOverride.N.Instance Type后，再指定本参数。两个参数一一对应，N需要保持一致。 本参数用于指定实例规格的权重，即实例规格的单台实例在伸缩组中表示的容量大小。权重越大，满足期望容量所需的本实例规格的实例数量越少。 由于每个实例规格的vCPU个数、内存大小等性能指标会有差异，您可以根据自身需求，给不同的实例规格配置不同的权重。 例如： 当前容量：0。 期望容量：6。 ecs.c5.xlarge规格容量：4。 为满足期望容量，伸缩组将为用户扩容2台 ecs.c5.xlarge实例。 说明扩容时伸缩组的容量不得超过最大容量与实例规格的最大权重之和。 WeightedCapacity的取值范围： 1~500。 |

弹性伸缩 ESS

| AlbServerGroup. N.AlbServerGrou pId | String | 否 | sgp- ddwb0y0g6y9bj m**** | ALB服务器组ID。 N为ALB服务器组的编号。一个伸缩组支持关联的ALB服务器组数量有限，如需查看或手动申请提升配额值，请前往配额中心。 |
|---|---|---|---|---|
| AlbServerGroup. N.Weight | Integer | 否 | 100 | 弹性伸缩将ECS实例添加到ALB服务器组后，ECS实例作为后端服务器的权重。权重越高，ECS实例将被分配到越多的访问请求。如果权重为0，则ECS实例不会收到访问请求。取值范围：0~100。 N为ALB服务器组的编号。 |
| AlbServerGroup. N.Port | Integer | 否 | 22 | 弹性伸缩将ECS实例添加到ALB服务器组后，ECS实例使用的端口号，取值范围： 1~65535。 N为ALB服务器组的编号。 说明如果N相同，Port不同，系统会默认向伸缩组关联多个不同Port的该ALB服务器组。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ScalingGroupI d | String | asg- bp14wlu85wrpchm 0**** | 伸缩组ID。由系统生成，全局唯一。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例弹性伸缩 ESS

```
http(s)://ess.example.com/?Action=CreateScalingGroup &ScalingGroupName=scalinggroup**** &LaunchTemplateId=lt-m5e3ofjr1zn1aw7**** &LaunchTemplateVersion=Default &InstanceId=i-28wt4**** &RegionId=cn-qingdao-env17-d01 &MinSize=2 &MaxSize=20 &DefaultCooldown=300 &LoadBalancerIds=["lb-bp1u7etiogg38yvwz****", "lb-bp168cqrux9ai9l7f****", "lb-bp1jv3m9z vj22ufxp****"] &DBInstanceIds=["rm-bp142f86de0t7****", "rm-bp18l1z42ar4o****", "rm-bp1lqr97h4aqk****"] &RemovalPolicy.1=OldestScalingConfiguration &RemovalPolicy.2=OldestInstance &VSwitchId=vsw-bp14zolna43z266bq**** &MultiAZPolicy=PRIORITY &HealthCheckType=ECS &ScalingPolicy=recycle &ClientToken=123e4567-e89b-12d3-a456-42665544**** &OnDemandBaseCapacity=30 &OnDemandPercentageAboveBaseCapacity=20 &DesiredCapacity=5 &GroupDeletionProtection=true &GroupType=ECS &ContainerGroupId=eci-uf6fonnghi50u374**** &VSwitchIds=["vsw-bp14zolna43z266bq****"] &LifecycleHook= [{"DefaultResult":"CONTINUE","LifecycleHookName":"lifecyclehook****","LifecycleTransition "SCALE_OUT","NotificationMetadata":"Test","NotificationArn":"acs:ess:cn-hangzhou-env17d01:1111111111:queue/queue2","HeartbeatTimeout":600}] &VServerGroup=[{"VServerGroupAttribute":[{"VServerGroupId":"rspbp1443g77****","Weight":100,"Port":22}],"LoadBalancerId":"lb-bp1u7etiogg38yvwz****"}] &Tag=[{"Key":"Department","Value":"Finance","Propagate":false}] &LaunchTemplateOverride=[{"InstanceType":"ecs.c5.xlarge","WeightedCapacity":4}] &AlbServerGroup=[{"AlbServerGroupId":"sgp-ddwb0y0g6y9bjm****","Weight":100,"Port":22}] &AzBalance=false &AllocationStrategy=priority
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScalingGroupId>asg-bp14wlu85wrpchm0****</ScalingGroupId>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingGroupId": "asg-bp14wlu85wrpchm0****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IncorrectDBInstanceSt atus | The current status of DB instance "XXX" does not support this action. | 指定RDS实例的状态必须是Running。 |
| 400 | IncorrectLoadBalancer HealthCheck | The current health check type of specified load balancer does not support this action. | 指定的负载均衡实例必须开启健康检查。 |
| 400 | IncorrectLoadBalancer Status | The current status of the specified load balancer does not support this action. | 指定负载均衡实例的状态必须是active。 |
| 400 | IncorrectVSwitchStatu s | The current status of virtual switch does not support this operation. | 虚拟交换机不可用，无法创建ECS实例。 |
| 400 | InvalidDBInstanceId. RegionMismatch | DB instance "XXX" and the specified scaling group are not in the same Region. | 指定的RDS实例与伸缩组必须在同一地域。 |
| 400 | InvalidLoadBalancerId. IncorrectAddressType | The current address type of specified load balancer does not support this action. | 指定虚拟交换机后，负载均衡实例为私网类型。 |
| 400 | InvalidLoadBalancerId. IncorrectInstanceNetw orkType | The network type of the instance in specified Load Balancer does not support this action. | 指定的负载均衡实例内搭载的ECS实例的网络类型与伸缩组的网络类型必须一致。 |
| 400 | InvalidLoadBalancerId. RegionMismatch | The specified Load Balancer and the specified scaling group are not in the same Region. | 指定的负载均衡实例与伸缩组必须在同一地域。 |

弹性伸缩 ESS

| 400 | InvalidLoadBalancerId. VPCMismatch | The specified virtual switch and the instance in specified Load Balancer are not in the same VPC. | 伸缩组内的负载均衡实例搭载的ECS实例与虚拟交换机应该在同一个VPC 中。 |
|---|---|---|---|
| 400 | InvalidParameter | The specified value of parameter "ScalingPolicy" is not valid. | 指定的回收模式参数不存在。 |
| 400 | InvalidParameter.Confl ict | The value of parameter <parameter name> and parameter <parameter name> are conflict. | 指定的MinSize不能大于 MaxSize。 |
| 400 | InvalidScalingGroupNa me.Duplicate | The specified value of parameter <parameter name> is duplicated. | 伸缩组名已存在。 |
| 400 | QuotaExceeded.DBInst anceSecurityIP | Security IP quota exceeded in DB instance "XXX". | 指定的RDS实例访问白名单的IP个数达到上限。 |
| 400 | QuotaExceeded.Privat eIpAddress | Private IP address quota exceeded in the specified virtual switch. | 虚拟交换机无法再分配多余的私有IP地址。 |
| 400 | QuotaExceeded.Scalin gGroup | Scaling group quota exceeded. | 用户的伸缩组使用个数达到上限。 |
| 400 | QuotaExceeded.VPCIn stance | Instance quota exceeded in the specified VPC. | 该VPC内的实例数超过数量限制。 |
| 404 | InvalidDBInstanceId.N otFound | DB instance "XXX" does not exist. | 指定的RDS实例不存在。 |
| 404 | InvalidLoadBalancerId. NotFound | The specified Load Balancer does not exist. | 指定的负载均衡实例不存在。 |
| 404 | InvalidRegionId.NotFou nd | The specified region does not exist. | 指定的地域不存在。 |

弹性伸缩 ESS

| 404 | InvalidVSwitchId.NotFo und | The specified virtual switch does not exist. | 指定的虚拟交换机不存在。 |
|---|---|---|---|
| 400 | LaunchTemplateVersio nSet.NotFound | The specific version of launch template is not exist. | 实例启动模板指定版本不存在。 |
| 400 | LaunchTemplateSet.N otFound | The specified launch template set is not found. | 指定实例启动模板不存在。 |
| 400 | TemplateMissingPara meter.ImageId | The input parameter "ImageId" that is mandatory for processing this request is not supplied. | 实例启动模板指定版本缺少镜像信息。 |
| 400 | TemplateMissingPara meter.InstanceTypes | The input parameter "InstanceTypes" that is mandatory for processing this request is not supplied. | 实例启动模板指定版本缺少实例规格信息。 |
| 400 | TemplateMissingPara meter.SecurityGroup | The input parameter "SecurityGroup" that is mandatory for processing this request is not supplied. | 实例启动模板指定版本缺少安全组信息。 |
| 400 | TemplateVersion.NotN umber | The input parameter "LaunchTemplateVersi on" is supposed to be a string representing the version number. | 指定实例启动模板固定版本号为非数字。 |

#### ModifyScalingGroup

**接口说明**

不支持修改以下参数： RegionId LoadBalancerId

**说明**

弹性伸缩 ESS DBInstanceId 如果需要修改RDS实例，请使用API AttachDBInstances和DetachDBInstances接

**说明**

口。 当伸缩组的状态为Active或Inactive时才能调用该接口。 启用新的伸缩配置不会影响通过早前伸缩配置创建并正在运行的ECS实例。 如果修改了MaxSize，导致伸缩组的ECS实例数超过最大容量（MaxSize），伸缩组会自动移出ECS实例，使得伸缩组的ECS实例数等于MaxSize。 如果修改了MinSize，导致伸缩组的ECS实例数低于最小容量（MinSize），伸缩组会自动加入ECS实例，使得伸缩组的ECS实例数等于MinSize。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyScalingGr oup | 系统规定参数。取值： ModifyScalingGroup。 |
| ScalingGroupId | String | 是 | asg- bp1ffogfdauy0jw 0**** | 待修改伸缩组的ID。 |
| ScalingGroupNa me | String | 否 | Scalinggroup*** * | 伸缩组的名称，同一地域下伸缩组名称唯一。长度为2~64个英文或中文字符，以数字、大小英文字母或中文开头，可以包含数字、下划线（ ）、短划线（-）和半角 _ 句号（.）。 |
| MinSize | Integer | 否 | 1 | 伸缩组内ECS实例台数的最小值，取值范围：0~1000 。当伸缩组内ECS实例数小于 MinSize 时，弹性伸缩会自动创建 ECS实例。 |
| MaxSize | Integer | 否 | 99 | 伸缩组内ECS实例台数的最大值，取值范围：0~1000。 当伸缩组内ECS实例数大于 MaxSize 时，弹性伸缩会自动移出 ECS实例。 |
| DefaultCooldow n | Integer | 否 | 600 | 一次伸缩活动（添加或移出ECS实例）结束后的一段冷却时间。取值范围： 0~86400，单位：秒。 冷却时间内，该伸缩组不执行其它的伸缩活动，仅针对云监控报警任务触发的伸缩活动有效。 |

弹性伸缩 ESS

| RemovalPolicy.1 | String | 否 | OldestScalingCo nfiguration | 指定实例移出策略的第一段筛选策略，取值范围： OldestInstance：移出最早加入伸缩组的ECS实例。 NewestInstance：移出最新加入伸缩组的ECS实例。 OldestScalingConfiguration：移出最早伸缩配置创建的ECS实例。 |
|---|---|---|---|---|
| RemovalPolicy.2 | String | 否 | NewestInstance | 指定实例移出策略的第二段筛选策略，取值范围： OldestInstance：移出最早加入伸缩组的ECS实例。 NewestInstance：移出最新加入伸缩组的ECS实例。 OldestScalingConfiguration：移出最早伸缩配置创建的ECS实例。 |
| ActiveScalingCo nfigurationId | String | 否 | asc- bp17pelvl720x5 ub**** | 伸缩组内生效的伸缩配置的ID。 |
| HealthCheckTyp e | String | 否 | ECS | 伸缩组的健康检查方式，取值范围： NONE：不进行健康检查。 ECS：对伸缩组内的ECS实例做健康检查。 |
| LaunchTemplate Id | String | 否 | lt- m5e3ofjr1zn1aw 7**** | 实例启动模板ID，用于指定伸缩组从实例启动模板获取启动配置信息。 |
| LaunchTemplate Version | String | 否 | Default | 实例启动模板的版本，取值范围： 固定的模板版本号。 Default：始终使用模板默认版本。 Latest：始终使用模板最新版本。 |
| OnDemandBase Capacity | Integer | 否 | 30 | 伸缩组所需要按量实例个数的最小值，取值范围：0~1000。当按量实例个数少于该值时，将优先创建按量实例。 |
| OnDemandPerce ntageAboveBase Capacity | Integer | 否 | 20 | 伸缩组满足最小按量实例数 （OnDemandBaseCapacity）要求后， 超出的实例中按量实例应占的比例，取值范围：0～100。 |
| DesiredCapacity | Integer | 否 | 5 | 伸缩组内ECS实例的期望数量，伸缩组会自动将ECS实例数量维持在期望实例数。 取值不得大于 MaxSize ，且不得小于 MinSize 。 |

|  | MaxSize |
|---|---|
| MinSize |  |

弹性伸缩 ESS

| GroupDeletionPr otection | Boolean | 否 | true | 是否开启伸缩组删除保护。取值范围： true：开启伸缩组删除保护，此时不能删除该伸缩组。 false：关闭伸缩组删除保护。 |
|---|---|---|---|---|
| MultiAZPolicy | String | 否 | PRIORITY | 多可用区伸缩组ECS实例扩缩容策略。取值范围： PRIORITY：根据虚拟交换机 （VSwitchIds.N）的优先级进行扩缩容。弹性伸缩优先在优先级最高的交换机所在可用区尝试扩缩容，如果无法扩缩容，则自动在下一优先级的交换机所在可用区进行扩缩容。 BALANCE：在伸缩组指定的多可用区之间均匀分配ECS实例。如果由于库存不足等原因可用区之间变得不平衡，您可以通过API RebalanceInstance平衡资源。 |
| VSwitchIds.N | RepeatL ist | 否 | vsw- bp1oo2a7isyrb8i gf**** | 一台或多台虚拟交换机的ID，N的取值范围：1~5。 只有当伸缩组网络类型为VPC时，当前参数才生效。指定虚拟交换机所属的 VPC必须和伸缩组所属的VPC相同。 虚拟交换机可以来自多个可用区。虚拟交换机的优先级按照数字升序排序，1 表示最高优先级。当优先级较高的虚拟交换机所在可用区无法创建ECS实例时，自动选择下一优先级的虚拟交换机创建ECS实例。 |
| LaunchTemplate Override.N.Insta nceType | String | 否 | ecs.c5.xlarge | 当您需要伸缩组按照实例规格容量进行伸缩时，请同时指定本参数和 LaunchTemplateOverride.N.Weighte dCapacity。 本参数用于指定实例规格，会覆盖启动模板中的实例规格。您可以指定N个本参数， 扩展启动模板支持N个实例规格。N的取值范围：1~10。 说明仅当 LaunchTemplateId参数指定了启动模板时，本参数生效。 InstanceType的取值范围：ECS实例支持的实例规格，请参见云服务器ECS文档中的实例规格族&实例规格简介章节。 |

弹性伸缩 ESS

| LaunchTemplate Override.N.Weig htedCapacity | Integer | 否 | 4 | 当您需要伸缩组按照实例规格容量进行伸缩时，在指定 LaunchTemplateOverride.N.Instance Type后，再指定本参数。两个参数一一对应，N需要保持一致。 本参数用于指定实例规格的权重，即实例规格的单台实例在伸缩组中表示的容量大小。 权重越大，满足期望容量所需的本实例规格的实例数量越少。 由于每个实例规格的vCPU个数、内存大小等性能指标会有差异，您可以根据自身需求，给不同的实例规格配置不同的权重。 例如： 当前容量：0。 期望容量：6。 ecs.c5.xlarge规格容量：4。 为满足期望容量，伸缩组将为用户扩容2台 ecs.c5.xlarge实例。 说明扩容时伸缩组的容量不得超过最大容量与实例规格的最大权重之和。 WeightedCapacity的取值范围： 1~500。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例弹性伸缩 ESS

```
http(s)://ess.example.com/?Action=ModifyScalingGroup &ScalingGroupId=asg-bp1ffogfdauy0jw0**** &ScalingGroupName=scalinggroup**** &MinSize=1 &MaxSize=99 &DefaultCooldown=600 &RemovalPolicy.1=OldestScalingConfiguration &RemovalPolicy.2=NewestInstance &ActiveScalingConfigurationId=asc-bp17pelvl720x5ub**** &HealthCheckType=ECS &LaunchTemplateId=lt-m5e3ofjr1zn1aw7**** &LaunchTemplateVersion=Default &OnDemandBaseCapacity=30 &OnDemandPercentageAboveBaseCapacity=20 &DesiredCapacity=5 &GroupDeletionProtection=true &MultiAZPolicy=PRIORITY &VSwitchIds=["vsw-bp1oo2a7isyrb8igf****"] &LaunchTemplateOverride=[{"InstanceType":"ecs.c5.xlarge","WeightedCapacity":4}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 400 | InvalidScalingGroupNa me.Duplicate | The specified value of parameter <parameter name> is duplicated. | 伸缩组名已存在。 |
| 404 | InvalidScalingConfigur ationId.NotFound | The specified scaling configuration does not exist. | 伸缩组中不存在指定的伸缩配置。 |

弹性伸缩 ESS

| 400 | InvalidScalingConfigur ationId.InstanceTypeM ismatch | The specified scaling configuration and existing active scaling configuration have different instance type. | 指定的伸缩配置的实例规格与当前生效的伸缩配置的实例规格不匹配。 |
|---|---|---|---|
| 400 | InvalidParameter.Confl ict | The value of parameter <parameter name> and parameter <parameter name> are confilict. | 指定的MinSize大于 MaxSize。 |
| 400 | LaunchTemplateVersio nSet.NotFound | The specific version of launch template is not exist. | 不存在指定的实例启动模板版本。 |
| 400 | LaunchTemplateSet.N otFound | The specified launch template set is not found. | 不存在指定的实例启动模板。 |
| 400 | TemplateMissingPara meter.ImageId | The input parameter "ImageId" that is mandatory for processing this request is not supplied. | 实例启动模板指定版本缺少镜像信息。 |
| 400 | TemplateMissingPara meter.InstanceTypes | The input parameter "InstanceTypes" that is mandatory for processing this request is not supplied. | 指定的实例启动模板版本缺少实例规格信息。 |
| 400 | TemplateMissingPara meter.SecurityGroup | The input parameter "SecurityGroup" that is mandatory for processing this request is not supplied. | 指定的实例启动模板版本缺少安全组信息。 |
| 400 | TemplateVersion.NotN umber | The input parameter "LaunchTemplateVersi on" is supposed to be a string representing the version number. | 指定的实例启动模板固定版本号应该是数字。 |

#### EnableScalingGroup

弹性伸缩 ESS

**接口说明**

当伸缩组处于Inactive状态，且伸缩组配置了组内实例的配置信息来源（伸缩配置、启动模板或者在创建伸缩组时指定的ECS实例）时，才可以调用该接口来启用伸缩组。否则，会调用失败。 一个伸缩组在同一时刻有且只有一个生效的实例配置信息来源。在调用接口时，您可以为

**说明**

伸缩组指定伸缩配置或启动模板。如果调用该接口前您已经为伸缩组配置了实例配置信息来源，在调用时再指定伸缩配置或启动模板会覆盖原有的配置信息。 当该接口指定了加入伸缩组的ECS实例（InstanceId.N），调用该接口后，弹性伸缩会判断在加入ECS实例后伸缩组的ECS实例数量（Total Capactiy）是否在最小值（MinSize）和最大值（MaxSize）之间： 如果伸缩组的Total Capactiy小于MinSize，调用成功后，弹性伸缩服务会自动创建差额的按量付费的 ECS实例。例如：创建伸缩组时，指定MinSize为5，在启用伸缩组的InstanceId.N参数中指定2台已有ECS实例，则弹性伸缩在加入2台已有ECS实例之后，再自动创建3台ECS实例。 如果伸缩组的Total Capactiy大于MaxSize，则调用失败。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | EnableScalingGr oup | 系统规定参数，取值： EnableScalingGroup。 |
| ScalingGroupId | String | 是 | asg- bp14wlu85wrpc hm0**** | 伸缩组的ID。 |
| ActiveScalingCo nfigurationId | String | 否 | asc- bp1ffogfdauy0n u5**** | 需要在伸缩组内激活的伸缩配置的ID。 |
| InstanceId.N | RepeatL ist | 否 | i-283vv**** | InstanceId.N为启用后需要加入伸缩组的 ECS实例的ID，N的取值范围：1～20。 指定加入伸缩组的ECS实例需要满足以下条件： 必须与伸缩组在同一个地域。 必须处于Running状态。 不能已加入到其他伸缩组中。 付费方式为包年包月、按量付费或抢占式实例。 如果伸缩组指定VswitchID，则不支持 Classic类型的ECS实例加入伸缩组，也不支持其他VPC的ECS实例加入伸缩组。 如果伸缩组没有指定VswitchID，则不支持VPC类型的ECS实例加入伸缩组。 |
| LoadBalancerWe ight.N | RepeatL ist | 否 | 50 | LoadBalancerWeight.N为对应ECS实例后端服务器的权重，N的取值范围：1～ 20，该参数取值范围：1~100。 默认值：50 |

弹性伸缩 ESS

| LaunchTemplate Id | String | 否 | lt- m5e3ofjr1zn1aw 7**** | 实例启动模板的ID，用于指定伸缩组从实例启动模板获取启动配置信息。 |
|---|---|---|---|---|
| LaunchTemplate Version | String | 否 | Default | 实例启动模板的版本，取值范围： 固定的模板版本号。 Default：始终使用模板默认版本。 Latest：始终使用模板最新版本。 |
| LaunchTemplate Override.N.Insta nceType | String | 否 | ecs.c5.xlarge | 当您需要伸缩组按照实例规格容量进行伸缩时，请同时指定本参数和 LaunchTemplateOverride.N.Weighte dCapacity。 本参数用于指定实例规格，会覆盖启动模板中的实例规格。您可以指定N个本参数， 扩展启动模板支持N个实例规格。N的取值范围：1~10。 说明仅当 LaunchTemplateId参数指定了启动模板时，本参数生效。 InstanceType的取值范围：在售的ECS实例规格，请参见云服务器ECS文档中的实例规格族章节。 |

弹性伸缩 ESS

| LaunchTemplate Override.N.Weig htedCapacity | Integer | 否 | 4 | 当您需要伸缩组按照实例规格容量进行伸缩时，先指定 LaunchTemplateOverride.N.Instance Type，再指定本参数。两个参数一一对应，N需要保持一致。 本参数用于指定实例规格的权重，即实例规格的单台实例在伸缩组中表示的容量大小。权重越大，满足期望容量所需的本实例规格的实例数量越少。 由于每个实例规格的vCPU个数、内存大小等性能指标会有差异，您可以根据自身需求，给不同的实例规格配置不同的权重。 例如： 当前容量：0 期望容量：6 ecs.c5.xlarge规格容量：4 为满足期望容量，伸缩组将为用户扩容2台 ecs.c5.xlarge实例。 说明扩容时伸缩组的容量不得超过最大容量与实例规格的最大权重之和。 WeightedCapacity的取值范围： 1~500。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http://ess.example.com/?Action=EnableScalingGroup &ScalingGroupId=asg-bp1ffogfdauy0jw0**** &InstanceId.1=i-283vv****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在该账号下不存在。 |
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 用户并未向弹性伸缩完整授权Open API接口。 |
| 400 | IncorrectScalingGroup Status | The current status of the specified scaling group does not support this action. | 指定的伸缩组处于 deleting状态。 |
| 404 | InvalidScalingConfigur ationId.NotFound | The specified scaling configuration does not exist. | 指定的伸缩配置不存在指定的伸缩组中。 |
| 400 | InvalidScalingConfigur ationId.InstanceTypeM ismatch | The specified scaling configuration and existing active scaling configuration have different instance type. | 指定的伸缩配置的实例规格与当前生效的伸缩配置的实例规格不匹配。 |
| 400 | MissingActiveScalingC onfiguration | An active scaling configuration for the specified scaling group is not supplied. | 伸缩组中未指定生效的伸缩配置。 |
| 404 | InvalidInstanceId.NotF ound | Instance “XXX” does not exist. | 指定的ECS实例在该用户账号下不存在。 |
| 400 | InvalidInstanceId. RegionMismatch | Instance “XXX” and the specified scaling group are not in the same Region. | 指定的ECS实例与伸缩组所处的地域不匹配。 |

弹性伸缩 ESS

| 400 | InvalidInstanceId. InstanceTypeMismatch | Instance “XXX” and existing active scaling configuration have different instance type. | 指定的 ECS 实例与伸缩配置的实例规格不匹配。 |
|---|---|---|---|
| 400 | IncorrectInstanceStatu s | The current status of instance “XXX” does not support this action. | 指定的ECS实例为非 running状态。 |
| 400 | InvalidInstanceId. NetworkTypeMismatch | The network type of instance “XXX” does not support this action. | 指定的ECS实例的网络类型与伸缩组的网络类型不匹配。 |
| 400 | InvalidInstanceId.VPC Mismatch | Instance “XXX” and the specified scaling group are not in the same VPC. | 指定的伸缩组与添加的 ECS实例不在同一个VPC 当中。 |
| 400 | InvalidInstanceId.InUs e | Instance “XXX” is already attached to another scaling group. | 指定的ECS实例已加入其它伸缩组。 |
| 400 | IncorrectLoadBalancer Status | The current status of the specified load balancer does not support this action. | 指定的负载均衡实例未处于active状态。 |
| 400 | IncorrectLoadBalancer HealthCheck | The current health check type of specified load balancer does not support this action. | 指定的负载均衡实例未开启健康检查。 |
| 400 | InvalidLoadBalancerId. IncorrectInstanceNetw orkType | The network type of the instance in specified Load Balancer does not support this action. | 指定的负载均衡实例含有的ECS实例的网络类型与伸缩组的网络类型不匹配。 |
| 400 | InvalidLoadBalancerId. VPCMismatch | The specified virtual switch and the instance in specified Load Balancer are not in the same VPC. | 指定的伸缩组的负载均衡实例含有的ECS实例与 VSwitchId不在同一个 VPC当中。 |
| 400 | IncorrectDBInstanceSt atus | The current status of DB instance “XXX” does not support this action. | 指定的RDS实例未处于 running状态。 |

弹性伸缩 ESS

| 400 | IncorrectCapacity.Max Size | To attach the instances, the total capacity will be greater than the max size. | 加入的 ECS 实例数使得 Total Capacity超过 MaxSize。 |
|---|---|---|---|
| 400 | LaunchTemplateVersio nSet.NotFound | The specific version of launch template is not exist. | 实例启动模板指定版本不存在。 |
| 400 | LaunchTemplateSet.N otFound | The specified launch template set is not found. | 指定实例启动模板不存在。 |
| 400 | TemplateMissingPara meter.ImageId | The input parameter "ImageId" that is mandatory for processing this request is not supplied. | 实例启动模板指定版本缺少镜像信息。 |
| 400 | TemplateMissingPara meter.InstanceTypes | The input parameter "InstanceTypes" that is mandatory for processing this request is not supplied. | 实例启动模板指定版本缺少实例规格信息。 |
| 400 | TemplateMissingPara meter.SecurityGroup | The input parameter "SecurityGroup" that is mandatory for processing this request is not supplied. | 实例启动模板指定版本缺少安全组信息。 |
| 400 | TemplateVersion.NotN umber | The input parameter "LaunchTemplateVersi on" is supposed to be a string representing the version number. | 指定实例启动模板固定版本号为非数字。 |

#### DisableScalingGroup

**接口说明**

停用伸缩组之前发生的伸缩活动，会继续完成，而之后触发的伸缩活动会直接拒绝。 当伸缩组为Active状态，才可以调用该接口。

**请求参数**

弹性伸缩 ESS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DisableScalingG roup | 系统规定参数，取值： DisableScalingGroup。 |
| ScalingGroupId | String | 是 | dmIDKNcyWfznc X9MWX1**** | 伸缩组的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http://ess.example.com/?Action=DisableScalingGroup &ScalingGroupId=dmIDKNcyWfzncX9MWX1****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在当前账号下不存在。 |

#### DeleteScalingGroup

弹性伸缩 ESS

**接口说明**

删除伸缩组，包括删除相关联的伸缩配置、伸缩规则、伸缩活动、伸缩请求的信息。 删除伸缩组，不会删除以下任务或实例：定时任务、云监控报警任务、负载均衡实例、RDS实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteScalingGr oup | 系统规定参数，取值： DeleteScalingGroup。 |
| ScalingGroupId | String | 是 | dmIDKNcyWfznc X9MWX1**** | 伸缩组的ID。 |
| ForceDelete | Boolean | 否 | false | 如伸缩组存在ECS实例或正在进行伸缩活动，是否强制删除伸缩组并移出和释放 ECS实例。取值范围： true：强制删除伸缩组。会先停用伸缩组，拒绝接收新的伸缩活动请求，然后等待已有的伸缩活动完成，最后将伸缩组内所有ECS实例移出伸缩组（手动添加的ECS实例会被移出伸缩组，弹性伸缩自动创建的ECS实例会被自动删除） 并删除伸缩组。 false：不强制删除伸缩组。满足以下两个条件时，会先停用伸缩组，然后再删除伸缩组。 伸缩组没有任何伸缩活动正在执行。 伸缩组当前的ECS实例数量（Total Capacity）为0。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http://ess.example.com/?Action=DeleteScalingGroup &ScalingGroupId=dmIDKNcyWfzncX9MWX1****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在该账号下不存在。 |
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您并未向弹性伸缩完整授权Open API接口。 |
| 400 | InstanceInUse | You cannot delete a scaling configuration or scaling group while there is an instance associated with it. | 指定的伸缩组中存在ECS 实例。 |

#### DescribeScalingGroups

**接口说明**

伸缩组具有以下几种状态（LifecycleState）： Active：生效状态。在该状态下才能接收执行伸缩规则的请求并触发伸缩活动。 Inacitve：失效状态。在该状态下不接收任何执行伸缩规则的请求。 Deleting：伸缩组正在删除。在该状态下不接收任何执行伸缩规则的请求。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeScaling Groups | 系统规定参数。取值： DescribeScalingGroups。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 伸缩组所属地域的ID。 |

弹性伸缩 ESS

| PageNumber | Integer | 否 | 1 | 伸缩组列表的页码。起始值：1。 默认值：1。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。最大值： 50。 默认值：10。 |
| ScalingGroupNa me | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName为待查询伸缩组的 ID，取值范围： ScalingGroupName.1~ScalingGroup Name.20。 查询结果会忽略失效的伸缩组ID，并且不会报错。 |
| ScalingGroupNa me.1 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.1为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.2 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.2为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.3 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.3为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.4 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.4为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.5 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.5为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.6 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.6为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.7 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.7为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.8 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.8为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |

弹性伸缩 ESS

| ScalingGroupNa me.9 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.9为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
|---|---|---|---|---|
| ScalingGroupNa me.10 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.10为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.11 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.11为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.12 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.12为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.13 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.13为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.14 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.14为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.15 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.15为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.16 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.16为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.17 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.17为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.18 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.18为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
| ScalingGroupNa me.19 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.19为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |

弹性伸缩 ESS

| ScalingGroupNa me.20 | String | 否 | dyrSuvBOtO1dE dIlIbp**** | ScalingGroupName.20为待查询的伸缩组的名称。查询结果会忽略失效的伸缩组名称，并且不报错。 |
|---|---|---|---|---|
| GroupType | String | 否 | ECS | 伸缩组管理的实例类型。取值范围： ECS：伸缩组内管理的伸缩为ECS实例。 ECI：伸缩组内管理的伸缩为ECI实例。 默认值：ECS。 |
| ScalingGroupId. N | RepeatL ist | 否 | asg- bp14wlu85wrpc hm0**** | ScalingGroupId.N为待查询伸缩组的 ID，N的取值范围：1～20。 查询结果会忽略失效的伸缩组ID，并且不报错。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingGroups | Array of ScalingGroup |  | 伸缩组信息的集合。 |
| ScalingGroup |  |  |  |
| ActiveCapacity | Integer | 1 | 已成功加入伸缩组，并正常运行的ECS实例数量。 |
| ActiveScalingC onfigurationId | String | asc- bp1et2qekq3ojr33* *** | 伸缩组内生效的伸缩配置的ID。 |
| AlbServerGrou ps | Array of AlbServerGrou p |  | ALB服务器组的相关信息集合。 |
| AlbServerGrou p |  |  |  |
| AlbServerGrou pId | String | sgp- ddwb0y0g6y9bjm* *** | ALB服务器组的ID。 |

弹性伸缩 ESS

| Port | Integer | 80 | 弹性伸缩将ECS实例添加到ALB服务器组后，ECS实例使用的端口号。 |
|---|---|---|---|
| Weight | Integer | 100 | 弹性伸缩将ECS实例添加到ALB服务器组后，ECS实例作为后端服务器的权重。 |
| AllocationStrat egy | String | priority | 容量分配策略，决定了伸缩组如何选择可用的实例规格类型满足容量。容量分布策略同时对按量和抢占式容量生效（仅当 MultiAZPolicy 参数取值为 COMPOSABLE 策略时生效）。可能值： priority：按照配置的实例规格的顺序创建实例。 lowestPrice：按照实例规格单位vCpu价格从低到高创建实例。 默认值：priority。 |
| AzBalance | Boolean | false | 伸缩组的容量是否在多个可用区间均衡分布（仅当 MultiAZPolicy 参数取值为 COMPOSABLE 策略时生效），可能值： true：伸缩组的容量在多个可用区间均衡分布。 false：伸缩组的容量不在多个可用区间均衡分布。 默认值：false。 |
| CompensateW ithOnDemand | Boolean | true | 说明该参数未开放使用。 |
| CreationTime | String | 2014-08- 14T10:58Z | 伸缩组的创建时间。 |
| DBInstanceIds | List | rm- bp15556qzebg1*** * | 伸缩组关联RDS实例的ID。 |
| DefaultCooldo wn | Integer | 60 | 伸缩组默认的冷却时间。冷却时间内，该伸缩组不执行其他的伸缩活动，仅针对云监控报警任务触发的伸缩活动有效。 |
| DesiredCapaci ty | Integer | 5 | 伸缩组内ECS实例的期望数量，伸缩组会自动将 ECS实例数量维持在期望实例数。 |
| GroupDeletion Protection | Boolean | true | 是否开启了伸缩组删除保护。可能值： true：开启伸缩组删除保护，此时不能删除该伸缩组。 false：关闭伸缩组删除保护。 |

弹性伸缩 ESS

| GroupType | String | ECS | 伸缩组管理的实例类型。 |
|---|---|---|---|
| HealthCheckT ype | String | ECS | 伸缩组的健康检查方式，可能值： NONE：不做健康检查。 ECS：对伸缩组内的ECS实例做健康检查。 |
| LaunchTempla teId | String | lt- m5e3ofjr1zn1aw7* *** | 伸缩组使用的实例启动模板的ID。 |
| LaunchTempla teOverrides | Array of LaunchTempla teOverride |  | 扩展启动模板的实例规格信息。 |
| LaunchTempla teOverride |  |  |  |
| InstanceType | String | ecs.c5.xlarge | 指定的实例规格，会覆盖启动模板中的实例规格。 |
| WeightedCapa city | Integer | 4 | 指定实例规格的权重，即实例规格的单台实例在伸缩组中表示的容量大小。权重越大，满足期望容量所需的本实例规格的实例数量越少。 |
| LaunchTempla teVersion | String | Default | 伸缩组使用的实例启动模板的版本。 |
| LifecycleState | String | Active | 伸缩组的状态信息，可能值： Active：生效状态，处于生效状态的伸缩组才能接收执行伸缩规则的请求并触发伸缩活动。 Inacitve：失效状态，处于失效状态的伸缩组不接收任何执行伸缩规则的请求。 Deleting：伸缩组正在删除，处于删除中状态的伸缩组不接收任何执行伸缩规则的请求，并且不能修改伸缩组相关参数。 |
| LoadBalancerI ds | List | lb- bp19byhscefk3x0li **** | 伸缩组关联的负载均衡实例的ID列表。 |
| MaxSize | Integer | 2 | 伸缩组内ECS实例台数的最大值。 |
| MinSize | Integer | 1 | 伸缩组内ECS实例台数的最小值。 |
| ModificationTi me | String | 2014-08- 14T10:58Z | 修改时间。 |
| MonitorGroupI d | String | 1497**** | 伸缩组关联的云监控应用分组ID。 |

弹性伸缩 ESS

| MultiAZPolicy | String | PRIORITY | 多可用区伸缩组ECS实例扩缩容策略。可能值： PRIORITY：根据您定义的虚拟交换机 （VSwitchIds.N）扩缩容。当优先级较高的虚拟交换机所在可用区无法创建ECS实例时， 自动使用下一优先级的虚拟交换机创建ECS实例。 COST OPTIMIZED：按vCPU单价从低到高 _ 进行尝试创建。当伸缩配置设置了抢占式计费方式的多实例规格时，优先创建对应抢占式计费实例。当抢占式计费实例由于库存等原因无法创建时，自动尝试以按量付费的方式创建。 说明 COST OPTIMIZED仅在伸 _ 缩配置设置了多实例规格或者选用了抢占式实例的情况下生效。 BALANCE：在伸缩组指定的多可用区之间均匀分配ECS实例。如果由于库存不足等原因可用区之间变得不平衡，您可以调用API RebalanceInstance接口平衡资源。 |
|---|---|---|---|
| OnDemandBas eCapacity | Integer | 30 | 伸缩组所需要按量实例个数的最小值，取值范围：0~1000。当按量实例个数少于该值时，将优先创建按量实例。 |
| OnDemandPer centageAbove BaseCapacity | Integer | 20 | 伸缩组满足最小按量实例数 （OnDemandBaseCapacity）要求后，超出的实例中按量实例应占的比例。取值范围：0～ 100。 |
| PendingCapaci ty | Integer | 0 | 正在加入伸缩组，还未完成相关配置的ECS实例的数量。 |
| PendingWaitC apacity | Integer | 1 | 伸缩组中处于加入挂起状态的ECS实例的数量。 |
| ProtectedCapa city | Integer | 1 | 伸缩组中处于保护中状态的ECS实例的数量。 |
| RegionId | String | cn-qingdao-env17- d01 | 伸缩组所属的地域的ID。 |
| RemovalPolici es | List | OldestScalingConfi guration | ECS实例移出伸缩组的策略的集合。可能值： OldestInstance：取最早创建的ECS实例。 NewestInstance：取最新创建的实例。 OldestScalingConfiguration：取最早伸缩配置创建的ECS实例。 |
| RemovingCap acity | Integer | 0 | 正在移出伸缩组的ECS实例的数量。 |
| RemovingWait Capacity | Integer | 1 | 伸缩组中处于移除挂起状态的ECS实例的数量。 |

弹性伸缩 ESS

| ScalingGroupI d | String | asg- bp14wlu85wrpchm 0**** | 伸缩组的ID。 |
|---|---|---|---|
| ScalingGroupN ame | String | dyrSuvBOtO1dEdIlI bp**** | 伸缩组的名称。 |
| ScalingPolicy | String | recycle | 指定伸缩组的回收模式，可能值： recycle：伸缩组的回收模式为停机回收模式。 release：伸缩组的回收模式为释放模式。 关于被移出实例的动作，请参见API RemoveInstances。 |
| SpotAllocation Strategy | String | lowestPrice | 说明该参数未开放使用。 |
| SpotInstanceP ools | Integer | 5 | 说明该参数未开放使用。 |
| SpotInstanceR emedy | Boolean | true | 说明该参数未开放使用。 |
| StandbyCapaci ty | Integer | 1 | 伸缩组中处于备用状态的实例数量。 |
| StoppedCapac ity | Integer | 1 | 伸缩组中处于停机不收费状态的实例数量。 |
| SuspendedPro cesses | List | ScaleIn | 暂停中的流程，没有则返回空。可能值： ScaleIn：缩容流程。 ScaleOut：扩容流程。 HealthCheck：健康检查。 AlarmNotification：报警任务。 ScheduledAction：定时任务。 |
| SystemSuspen ded | Boolean | true | 弹性伸缩是否停止执行伸缩组内的伸缩活动。可能值： true：停止执行伸缩组内的伸缩活动，说明该伸缩组已经连续扩缩容失败超过7天。您需要修改伸缩组或者伸缩配置，来恢复伸缩活动的执行。 false：执行伸缩组内的伸缩活动。 |
| TotalCapacity | Integer | 1 | 当伸缩组设置了实例规格权重，表示伸缩组内所有ECS实例的加权容量总和。否则，表示伸缩组内所有ECS实例的数量。 |
| TotalInstanceC ount | Integer | 1 | 伸缩组内所有ECS实例的数量。 |

弹性伸缩 ESS

| VServerGroup s | Array of VServerGroup |  | 后端服务器组列表。 |
|---|---|---|---|
| VServerGroup |  |  |  |
| LoadBalancerI d | String | 147b46d767c-cn- qingdao-cm5**** | 后端服务器组所属的负载均衡实例的ID。 |
| VServerGroup Attributes | Array of VServerGroup Attribute |  | 后端服务器组属性。 |
| VServerGroup Attribute |  |  |  |
| Port | Integer | 22 | 负载均衡实例对外提供服务的端口号。 |
| VServerGroupI d | String | rsp-bp12bjrny**** | 后端服务器组的ID。 |
| Weight | Integer | 1 | 后端服务器组的权重。 |
| VSwitchId | String | vsw- bp1whw2u46cn8zu bm**** | 伸缩组关联虚拟交换机的ID。如果您使用了 VSwitchIds参数，VSwitchId参数将被忽略。 |
| VSwitchIds | List | vsw- bp1whw2u46cn8zu bm**** | 伸缩组关联虚拟交换机的ID集合。如果您使用了 VSwitchIds参数，VSwitchId参数将被忽略。 |
| VpcId | String | vpc-**** | 伸缩组所属VPC的ID。 |
| TotalCount | Integer | 1 | 伸缩组的总数。 |

**示例**

请求示例弹性伸缩 ESS

```
http(s)://ess.example.com/?Action=DescribeScalingGroups &RegionId=cn-qingdao-env17-d01 &PageNumber=1 &PageSize=10 &ScalingGroupName=scalinggroup**** &ScalingGroupName.1=scalinggroup**** &ScalingGroupName.2=scalinggroup**** &ScalingGroupName.3=scalinggroup**** &ScalingGroupName.4=scalinggroup**** &ScalingGroupName.5=scalinggroup**** &ScalingGroupName.6=scalinggroup**** &ScalingGroupName.7=scalinggroup**** &ScalingGroupName.8=scalinggroup**** &ScalingGroupName.9=scalinggroup**** &ScalingGroupName.10=scalinggroup**** &ScalingGroupName.11=scalinggroup**** &ScalingGroupName.12=scalinggroup**** &ScalingGroupName.13=scalinggroup**** &ScalingGroupName.14=scalinggroup**** &ScalingGroupName.15=scalinggroup**** &ScalingGroupName.16=scalinggroup**** &ScalingGroupName.17=scalinggroup**** &ScalingGroupName.18=scalinggroup**** &ScalingGroupName.19=scalinggroup**** &ScalingGroupName.20=scalinggroup**** &GroupType=ECS &ScalingGroupId=["asg-bp14wlu85wrpchm0****"]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <PageNumber>1</PageNumber>
      <ScalingGroups>
            <ScalingGroup>
                  <ScalingGroupId>asg-bp14wlu85wrpchm0****</ScalingGroupId>
                  <ScalingGroupName>b8pYCVbIV5k9cz4PWpbe****</ScalingGroupName>
                  <RegionId>cn-qingdao-env17-d01</RegionId>
                  <RemovingCapacity>0</RemovingCapacity>
                  <DefaultCooldown>300</DefaultCooldown>
                  <MinSize>1</MinSize>
                  <MaxSize>2</MaxSize>
                  <LifecycleState>Inactive</LifecycleState>
                  <ActiveScalingConfigurationId>asc-bp1et2qekq3ojr33****</ActiveScalingC
onfigurationId>
                  <LoadBalancerIds>
                        <LoadBalancerId>lb-bp19byhscefk3x0li****</LoadBalancerId>
                  </LoadBalancerIds>
                  <PendingCapacity>0</PendingCapacity>
                  <TotalCapacity>0</TotalCapacity>
                  <ActiveCapacity>0</ActiveCapacity>
                  <CreationTime>2014-08-14T10:58Z</CreationTime>
                  <DBInstanceIds>
                        <DBInstanceId>rm-bp15556qzebg1****</DBInstanceId>
                        <DBInstanceId>rm-bp52316qzhbg6****</DBInstanceId>
                  </DBInstanceIds>
                  <VSwitchId>vsw-bp1whw2u46cn8zubm****</VSwitchId>
                  <RemovalPolicies>
                        <RemovalPolicy>OldestScalingConfiguration</RemovalPolicy>
                        <RemovalPolicy>OldestInstance</RemovalPolicy>
                  </RemovalPolicies>
            </ScalingGroup>
      </ScalingGroups>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "TotalCount": 1,
    "PageSize": 10,
    "PageNumber": 1,
    "ScalingGroups": {
        "ScalingGroup": [
            {
                "ScalingGroupId": "asg-bp14wlu85wrpchm0****",
                "ScalingGroupName": "b8pYCVbIV5k9cz4PWpbe****",
                "RegionId": "cn-qingdao-env17-d01",
                "RemovingCapacity": 0,
                "DefaultCooldown": 300,
                "MinSize": 1,
                "MaxSize": 2,
                "LifecycleState": "Inactive",
                "ActiveScalingConfigurationId": "asc-bp1et2qekq3ojr33****",
                "LoadBalancerIds": {
                    "LoadBalancerId": [
                        "lb-bp19byhscefk3x0li****"
```

]

```json
                },
                "PendingCapacity": 0,
                "TotalCapacity": 0,
                "ActiveCapacity": 0,
                "CreationTime": "2014-08-14T10:58Z",
                "DBInstanceIds": {
                    "DBInstanceId": [
                        "rm-bp15556qzebg1****",
                        "rm-bp52316qzhbg6****"
```

]

```json
                },
                "VSwitchId": "vsw-bp1whw2u46cn8zubm****",
                "RemovalPolicies": {
                    "RemovalPolicy": [
                        "OldestScalingConfiguration",
                        "OldestInstance"
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

#### DescribeScalingInstances

调用DescribeScalingInstances查询伸缩组内ECS实例的列表，并列出ECS实例的信息。

**接口说明**

您可以通过指定伸缩组ID查询该伸缩组内ECS实例的列表，查询时可以指定伸缩配置ID、健康状态、生命周期状态、创建类型进行过滤。 弹性伸缩 ESS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeScalingI nstances | 系统规定参数，取值： DescribeScalingInstances。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 伸缩组所属地域的ID。 |
| ScalingGroupId | String | 否 | asg-**** | 伸缩组的ID。 |
| ScalingConfigura tionId | String | 否 | asc-**** | 关联伸缩配置的ID。 |
| HealthStatus | String | 否 | Healthy | ECS实例在伸缩组中的健康状态，未处于运行中（Running）状态的ECS实例会被判定为不健康的ECS实例，取值范围： Healthy：健康的ECS实例。 Unhealthy：不健康的ECS实例。 弹性伸缩会自动移出伸缩组中不健康的 ECS实例。弹性伸缩会停止和释放自动创建的ECS实例，但不会停止和释放手动添加的ECS实例。 |
| LifecycleState | String | 否 | InService | ECS实例在伸缩组中的生命周期状态，取值范围： InService：已成功加入伸缩组并正常提供服务。 Pending：正在加入伸缩组但还未完成相关配置，包括创建实例、加入负载均衡、添加RDS访问名单等过程。 Removing：正在移出伸缩组。 |
| CreationType | String | 否 | AutoCreated | ECS实例的创建类型，取值范围： AutoCreated：伸缩组根据伸缩配置和伸缩规则自动创建的ECS实例。 Attached：不是通过弹性伸缩服务创建，而是手动添加到伸缩组中的ECS实例。 |
| PageNumber | Integer | 否 | 1 | ECS实例列表的页码，起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数，最大值： 50。 默认值：10。 |

弹性伸缩 ESS

| ScalingActivityId | String | 否 | asa- bp1c9djwrgxjyk 31**** | 伸缩活动的ID。 |
|---|---|---|---|---|
| InstanceId.N | RepeatL ist | 否 | i- bp109k5j3dum1 ce6**** | InstanceId.N为ECS实例的ID，N的取值范围：1～20。返回查询结果时忽略失效的InstanceId，并且不报错。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页行数。 |
| RequestId | String | E481B3F5-F290- 4F3E-AB40- F980FB8E**** | 请求ID。 |
| ScalingInstanc es | Array of ScalingInstanc e |  | ECS实例信息组成的集合。 |
| ScalingInstanc e |  |  |  |
| CreatedTime | String | 2019-03- 06T08:06:39Z | ECS实例加入伸缩组的时间，精确到秒。 |
| CreationTime | String | 2019-03- 06T08:06Z | 加入伸缩组的时间。 |
| CreationType | String | AutoCreated | ECS实例的创建类型，可能值： AutoCreated：伸缩组根据伸缩配置和伸缩规则自动创建的ECS实例。 Attached：不是通过弹性伸缩服务创建，而是手动添加到伸缩组中的ECS实例。 |
| Entrusted | Boolean | false | 手动添加ECS实例到伸缩组时，是否将ECS实例托管给伸缩组，托管状态的手动添加ECS实例， 在移除伸缩组（不包括手动移除）时，将执行释放操作。可能值： true：将ECS实例托管给伸缩组。 false：不将ECS实例托管给伸缩组。 |
| HealthStatus | String | Healthy | 在伸缩组中的健康状态，可能值： Healthy：健康的ECS实例。 Unhealthy：不健康的ECS实例。 |

弹性伸缩 ESS

| InstanceId | String | i-283vv**** | ECS实例的ID。 |
|---|---|---|---|
| LaunchTempla teId | String | lt- m5e3ofjr1zn1aw7* *** | 实例启动模板的ID。 |
| LaunchTempla teVersion | String | 1 | 实例启动模板的版本。 |
| LifecycleState | String | InService | 在伸缩组中的生命周期状态，可能值： InService：已成功加入伸缩组并正常提供服务。 Pending：正在加入伸缩组但还未完成相关配置，包括创建实例、加入负载均衡、添加RDS 访问名单等过程。 Removing：正在移出伸缩组。 |
| LoadBalancer Weight | Integer | 1 | 负载均衡实例权重。 |
| ScalingActivity Id | String | asa- bp1c9djwrgxjyk31* *** | ECS实例加入伸缩组时，伸缩活动的ID。 |
| ScalingConfigu rationId | String | asc-**** | 关联伸缩配置的ID。 |
| ScalingGroupI d | String | asg-**** | 所属伸缩组的ID。 |
| SpotStrategy | String | SpotWithPriceLimit | 说明该参数未开放使用。 |
| WarmupState | String | NoNeedWarmup | 实例的预热状态，可能值： NoNeedWarmup：不需要预热。 WaitingForInstanceWarmup：等待预热结束。 InstanceWarmupFinish：预热结束。 |
| WeightedCapa city | Integer | 4 | 实例规格的权重，即实例规格的单台实例在伸缩组中表示的容量大小。权重越大，满足期望容量所需的本实例规格的实例数量越少。 |
| ZoneId | String | cn-qingdao-env17- g | ECS实例所属的可用区ID。 |
| TotalCount | Integer | 1 | ECS实例的总数。 |
| TotalSpotCoun t | Integer | 4 | 说明该参数未开放使用。 |

弹性伸缩 ESS

**示例**

请求示例

```
https://ess.example.com/?Action=DescribeScalingInstances &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>E481B3F5-F290-4F3E-AB40-F980FB8E****</RequestId>
      <TotalCount>1</TotalCount>
      <PageNumber>1</PageNumber>
      <PageSize>50</PageSize>
      <ScalingInstances>
            <ScalingInstance>
                  <ScalingConfigurationId>asc-****</ScalingConfigurationId>
                  <CreationType>AutoCreated</CreationType>
                  <InstanceId>i-28sov****</InstanceId>
                  <CreationTime>2014-08-14T10:59Z</CreationTime>
                  <HealthStatus>Healthy</HealthStatus>
                  <LifecycleState>InService</LifecycleState>
                  <Entrusted>false</Entrusted>
                  <ScalingGroupId>asg-****</ScalingGroupId>
            </ScalingInstance>
      </ScalingInstances>
```

`JSON` 格式

```json
{
    "RequestId": "E481B3F5-F290-4F3E-AB40-F980FB8E****",
    "TotalCount": 1,
    "PageNumber": 1,
    "PageSize": 50,
    "ScalingInstances": {
        "ScalingInstance": [
            {
                "ScalingConfigurationId": "asc-****",
                "CreationType": "AutoCreated",
                "InstanceId": "i-28sov****",
                "CreationTime": "2014-08-14T10:59Z",
                "HealthStatus": "Healthy",
                "LifecycleState": "InService",
                "Entrusted": "false",
                "ScalingGroupId": "asg-****"
            }
```

]

```
    }
}
```

弹性伸缩 ESS

#### DescribeScalingActivityDetail

调用DescribeScalingActivityDetail查询一个伸缩活动的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeScaling ActivityDetail | 系统规定参数，取值： DescribeScalingActivityDetail。 |
| ScalingActivityId | String | 是 | asa- bp1c9djwrgxjyk 31**** | 待查询伸缩活动的ID。您可以通过调用API DescribeScalingActivities 接口查询伸缩活动ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Detail | String | new ECS instances \"i- bp16t2cgmiiymeqv ****\" are created. | 伸缩活动的详细信息。 |
| RequestId | String | B13527BF-1FBD- 4334-A512- 20F5E9D3**** | 请求ID。 |
| ScalingActivity Id | String | asa- bp1c9djwrgxjyk31* *** | 伸缩活动的ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DescribeScalingActivityDetail &ScalingActivityId=asa-bp1c9djwrgxjyk31****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>B13527BF-1FBD-4334-A512-20F5E9D3****</RequestId>
      <ScalingActivityId>asa-bp1c9djwrgxjyk31****</ScalingActivityId>
      <Detail>new ECS instances \"i-bp16t2cgmiiymeqv****\" are created.</Detail>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "RequestId": "B13527BF-1FBD-4334-A512-20F5E9D3****",
    "ScalingActivityId": "asa-bp1c9djwrgxjyk31****",
    "Detail": "new ECS instances \"i-bp16t2cgmiiymeqv****\" are created."
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The input parameter "ScalingActivityId" that is mandatory for processing this request is not supplied | 没有提供待查询伸缩活动的ID。 |

#### DescribeScalingActivities

**接口说明**

查询时可以指定伸缩组ID来查询该伸缩组下的所有伸缩活动。 查询时可以通过伸缩活动的状态来过滤查询结果。 可以查询30日内的伸缩活动。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeScaling Activities | 系统规定参数，取值： DescribeScalingActivities。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 伸缩活动所属伸缩组的地域ID。 |
| PageNumber | Integer | 否 | 1 | 伸缩活动列表的页码，起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 50 | 分页查询时设置的每页行数，最大值： 50。 默认值：10。 |
| ScalingGroupId | String | 否 | AG6CQdPU8OKd wLjgZcJ**** | 伸缩组的ID。 |

弹性伸缩 ESS

| StatusCode | String | 否 | Successful | 伸缩活动的状态，取值范围： Successful：执行成功的伸缩活动。 Warning：部分执行成功的伸缩活动。 Failed：执行失败的伸缩活动。 InProgress：正在执行的伸缩活动。 Rejected：执行伸缩活动请求被拒绝。 |
|---|---|---|---|---|
| ScalingActivityId .N | RepeatL ist | 否 | asa- bp161xudmuxdz ofe**** | ScalingActivityId.N为待查询伸缩活动的 ID，N的取值范围：1～20。 说明调用该API 时，ScalingGroupId或 ScalingActivityId.N参数必选。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 50 | 每页行数。 |
| ScalingActiviti es | Array of ScalingActivity |  | 伸缩活动信息组成的集合。 |
| ScalingActivity |  |  |  |
| AttachedCapa city | String | 1 | 执行完伸缩活动后，伸缩组中用户手动添加的实例的总数。 |
| AutoCreatedC apacity | String | 1 | 执行完伸缩活动后，伸缩组中由伸缩组负责自动创建的实例的总数。 |
| Cause | String | A user requests to execute scaling rule "asr- 1kx06p7kys0e6cy2 ****", changing the Total Capacity from "0" to "1". | 触发伸缩活动的原因。 |
| Description | String | Add "1" ECS instance | 伸缩活动的描述信息。 |
| EndTime | String | 2014-08- 17T12:39Z | 伸缩活动的结束时间。 |
| Progress | Integer | 100 | 伸缩活动的运行进度。 |

弹性伸缩 ESS

| ScalingActivity Id | String | ebta5WbUzC8gcw UWvfch**** | 伸缩活动的ID。 |
|---|---|---|---|
| ScalingGroupI d | String | AG6CQdPU8OKdwL jgZcJ**** | 伸缩组的ID。 |
| ScalingInstanc eNumber | Integer | 1 | 如果伸缩活动类型为扩容，该参数表示本次伸缩活动中被创建或从停机回收状态启动的实例的个数。 如果伸缩活动类型为缩容，该参数表示本次伸缩活动中被删除或进入停机回收状态的实例的个数。 |
| StartTime | String | 2014-08- 17T12:39Z | 伸缩活动的开始时间。 |
| StatusCode | String | Successful | 伸缩活动的状态，取值范围： Successful：执行成功的伸缩活动。 Warning：部分执行成功的伸缩活动。 Failed：执行失败的伸缩活动。 InProgress：正在执行的伸缩活动。 Rejected：执行伸缩活动请求被拒绝。 |
| StatusMessag e | String | "1" ECS instance is added. | 伸缩活动的状态信息。 |
| TotalCapacity | String | 2 | 执行完伸缩活动后，伸缩组中实例的总数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 1 | 伸缩活动总数。 |

**示例**

请求示例

```
http://ess.example.com/?Action=DescribeScalingActivities &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <RequestId>8FAAE99E-EB43-4838-85AD-93F62454904C</RequestId>
      <TotalCount>1</TotalCount>
      <PageNumber>1</PageNumber>
      <PageSize>10</PageSize>
      <ScalingActivities>
            <ScalingActivity>
                  <Cause>A scheduled task excuete scaling rule "sr****"，changing the To
tal Capacity from "0" to "1".</Cause>
                  <Description>Add "1" ECS instance</Description>
                  <EndTime>2014-08-17T12:39Z</EndTime>
                  <Progress>100</Progress>
                  <ScalingActivityId>ebta5WbUzC8gcwUWvfch****</ScalingActivityId>
                  <ScalingGroupId>AG6CQdPU8OKdwLjgZcJ****</ScalingGroupId>
                  <StartTime>2014-08-17T12:39Z</StartTime>
                  <StatusCode>Successful</StatusCode>
                  <StatusMessage>"1" ECS instances is added. </StatusMessage>
            </ScalingActivity>
      </ScalingActivities>
```

`JSON` 格式

```json
{
        "RequestId": "8FAAE99E-EB43-4838-85AD-93F62454904C",
        "TotalCount": 1,
        "PageNumber": 1,
        "PageSize": 10,
        "ScalingActivities": {
            "ScalingActivity": {
                "Cause": "A scheduled task excuete scaling rule \"sr****\"，changing the
Total Capacity from \"0\" to \"1\".",
                "Description": "Add \"1\" ECS instance",
                "EndTime": "2014-08-17T12:39Z",
                "Progress": 100,
                "ScalingActivityId": "ebta5WbUzC8gcwUWvfch****",
                "ScalingGroupId": "AG6CQdPU8OKdwLjgZcJ****",
                "StartTime": "2014-08-17T12:39Z",
                "StatusCode": "Successful",
                "StatusMessage": "\"1\" ECS instances is added."
            }
        }
}
```

#### AttachDBInstances

**接口说明**

向伸缩组添加RDS实例时需要满足以下条件： RDS实例与伸缩组必须属于同一账号。 弹性伸缩 ESS RDS实例必须处于未锁定状态，关于锁定策略，请参见弹性伸缩的使用限制章节。 RDS实例必须处于运行中状态。 添加RDS实例后，RDS IP白名单的default分组中包含的IP不能超过1000条。关于IP白名单，请参见云数据库RDS中的通过客户端、命令行连接RDS MySQL实例章节。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AttachDBInstanc es | 系统规定参数。取值： AttachDBInstances。 |
| DBInstance.N | RepeatL ist | 是 | rm-bp12cy3**** | RDS实例的ID，N的取值范围：1~5。 |
| ScalingGroupId | String | 是 | asg- bp1avr6ensitts3 w**** | 伸缩组的ID。 |
| ForceAttach | Boolean | 否 | false | 是否把当前伸缩组内实例的私网IP全部添加到RDS实例IP白名单中。取值范围： true：添加。 false：不添加。 默认值：false。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多详情，请参见弹性伸缩中的如何保证幂等性章节。 |
| RegionId | String | 否 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=AttachDBInstances &ScalingGroupId=asg-bp1avr6ensitts3w**** &ForceAttach=false &ClientToken=123e4567-e89b-12d3-a456-42665544**** &DBInstance=["rm-bp12cy3****"] &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 弹性伸缩 ESS 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 400 | QuotaExceeded.RDS | "RDS" quota exceeded. | 伸缩组中RDS实例超出配额限制。 |
| 400 | InvalidDBInstanceId.N otFound | The specified value of parameter "%s" is not valid. | 不存在指定的RDS实例。 |
| 400 | IncorrectDBInstanceSt atus | The current status of DB instance "%s" does not support this action. | 当前RDS实例状态不支持该操作。 |
| 400 | QuotaExceeded.DBInst anceSecurityIP | Security IP quota exceeded in DB instance "%s". | RDS实例后端IP白名单个数超出配额。 |
| 400 | InvalidInstanceIds.Priv ateIpNotFound | Can not find all private ips of instances in specific scaling group. | 无法获取组内RDS实例的私网IP。 |

#### DetachDBInstances

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

弹性伸缩 ESS

| Action | String | 是 | DetachDBInstan ces | 系统规定参数，取值： DetachDBInstances。 |
|---|---|---|---|---|
| DBInstance.N | RepeatL ist | 是 | rm-bp12cy3**** | RDS实例的ID，单次最多支持移除5个 RDS实例。 |
| ScalingGroupId | String | 是 | asg- bp1igpak5ft1fly p**** | 伸缩组的ID。 |
| ForceDetach | Boolean | 否 | false | 是否移除RDS实例IP白名单中属于伸缩组内实例的私网IP。取值范围： true：移除实例的私网IP。 false：不移除实例的私网IP。 默认值：false。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |
| RegionId | String | 否 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DetachDBInstances &ScalingGroupId=asg-bp1igpak5ft1flyp**** &ForceDetach=false &ClientToken=123e4567-e89b-12d3-a456-42665544**** &DBInstance=["rm-bp12cy3****"] &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 400 | InvalidDBInstanceId.N otFound | DB instance "%s" does not exist. | 不存在指定的RDS实例。 |

#### SetGroupDeletionProtection

调用SetGroupDeletionProtection为伸缩组开启或关闭删除保护。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetGroupDeletio nProtection | 系统规定参数。取值： SetGroupDeletionProtection。 |
| GroupDeletionPr otection | Boolean | 是 | true | 是否为伸缩组开启删除保护。取值范围： true：开启删除保护。开启删除保护后，不能在控制台或者通过调用API删除伸缩组。如果需要删除伸缩组，必须先关闭删除保护。 false：关闭删除保护。 默认值：false。 |
| ScalingGroupId | String | 是 | asg- bp1igpak5ft1fly p**** | 伸缩组的ID。 |
| RegionId | String | 否 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

弹性伸缩 ESS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CCC29E24-3AEC- 4F2C-8A14- 78B14FA7**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=SetGroupDeletionProtection &GroupDeletionProtection=true &ScalingGroupId=asg-bp1igpak5ft1flyp**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>CCC29E24-3AEC-4F2C-8A14-78B14FA7****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "CCC29E24-3AEC-4F2C-8A14-78B14FA7****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 伸缩组不存在。 |
| 400 | InvalidOperation.Confli ct | Specific operation may conflicts with other operations, please retry later. | 操作冲突，请稍后再试。 |

#### ResumeProcesses

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

弹性伸缩 ESS

| Action | String | 是 | ResumeProcess es | 系统规定参数。取值： ResumeProcesses。 |
|---|---|---|---|---|
| Process.N | RepeatL ist | 是 | ScaleIn | 需要恢复的活动类型，N的取值范围： 1~100。取值范围： ScaleIn：缩容流程。 ScaleOut：扩容流程。 HealthCheck：健康检查。 AlarmNotification：报警任务。 ScheduledAction：定时任务。 目前支持恢复5种活动类型，如果您指定超过以上5种，会自动去掉重复的活动类型。 |
| ScalingGroupId | String | 是 | asg- bp15oubotmrq1 1xe**** | 伸缩组的ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |
| RegionId | String | 否 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | E38EB733-D714- 4658-8A5F- 0688AB68**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=ResumeProcesses &ScalingGroupId=asg-bp15oubotmrq11xe**** &ClientToken=123e4567-e89b-12d3-a456-42665544**** &Process=["ScaleIn"] &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>E38EB733-D714-4658-8A5F-0688AB68****</RequestId>
```

弹性伸缩 ESS `JSON` 格式

```json
{
 "RequestId": "E38EB733-D714-4658-8A5F-0688AB68****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 400 | InvalidParameter | The specified value of parameter "%s" is not valid. | 指定的参数非法。 |

#### SuspendProcesses

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SuspendProcess es | 系统规定参数。取值： SuspendProcesses。 |
| Process.N | RepeatL ist | 是 | ScaleIn | 需要暂停的活动类型，N的取值范围： 1~100。取值范围： ScaleIn：缩容流程。 ScaleOut：扩容流程。 HealthCheck：健康检查 。 AlarmNotification：报警任务。 ScheduledAction：定时任务。 目前支持暂停5种活动类型，如果您指定超过以上5种，会自动去掉重复的活动类型。 |
| ScalingGroupId | String | 是 | asg- bp15oubotmrq1 1xe**** | 伸缩组的ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |

弹性伸缩 ESS

| RegionId | String | 否 | cn-hangzhou- env17-d01 | 伸缩组所属的地域ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 3E2033F0-03B4- 419D-BCE2- C2339DB5**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=SuspendProcesses &ScalingGroupId=asg-bp15oubotmrq11xe**** &ClientToken=123e4567-e89b-12d3-a456-42665544**** &Process=["ScaleIn"] &RegionId=cn-hangzhou-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>3E2033F0-03B4-419D-BCE2-C2339DB5****</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "3E2033F0-03B4-419D-BCE2-C2339DB5****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 400 | InvalidParameter | The specified value of parameter "%s" is not valid. | 指定的参数非法。 |

#### AttachVServerGroups

调用AttachVServerGroups添加负载均衡实例下的一个或者多个虚拟服务器组。 弹性伸缩 ESS

**接口说明**

向伸缩组添加虚拟服务器组时需要满足以下条件： 负载均衡实例与伸缩组必须属于同一账号。 负载均衡实例与伸缩组必须处于同一地域。 负载均衡实例必须处于运行中状态。 负载均衡实例至少配置有一个监听且必须开启健康检查。 如果负载均衡实例与伸缩组的网络类型均为VPC，必须处于同一VPC。 当伸缩组的网络类型为VPC，负载均衡实例的网络类型为经典网络时，如果虚拟服务器组包含VPC实例， 该实例必须与伸缩组处于同一VPC。 待添加虚拟服务器组必须属于对应的负载均衡实例。 不超过伸缩组内虚拟服务器组的限额，具体限额请参见专有云文档中心《弹性伸缩用户指南》文档中的使章节。

**用须知 > 使用限制**

确定伸缩组内虚拟服务器组时，需要同时指定以下属性： 负载均衡实例ID（LoadBalancerId） 虚拟服务器组ID（VServerGroupId） 虚拟服务器组端口号（Port） 如果通过不同的端口号将同一虚拟服务器组添加至伸缩组，视为伸缩组内添加了多个虚拟服务器组。如果请求参数中的虚拟服务器组ID和端口号同时重复，默认使用最先配置的一组，忽略其余虚拟服务器组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  |  |  | 说明 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Action | Strin g | Query | 是 | AttachVServerGroups |  |  |  | 系统规定参数，取值： AttachVServerGroup s 。 |  |  |  |  |
| RegionId | Strin g | Query | 是 | cn-hangzhou-env17-d01 |  |  |  | 伸缩组所属地域的ID， 如 cn-hangzhou- env17-d01 、 cn- shanghai-env17- d01 。 |  |  |  |  |
|  |  |  |  |  |  |  |  |  | cn-hangzhou- |  |  |  |
|  |  |  |  |  |  | -env17-d01 |  | env17-d01 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 、 | cn- |  |
|  |  |  |  |  |  |  |  | d01 |  |  |  |  |
| ScalingGr oupId | Strin g | Query | 是 | asg- bp18p2yfxow2dloq**** |  |  |  | 伸缩组的ID。 |  |  |  |  |
| ClientToke n | Strin g | Query | 否 | 123e4567-e89b-12d3- a456-42665544**** |  |  |  | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息， 请参见公共云文档中心 《弹性伸缩开发参考》 文 _ _ 档中的API参考（2014- 08-28）> 如何保证幂等性章节。 |  |  |  |  |

弹性伸缩 ESS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ForceAtta ch | Boole an | Query | 否 | false | 是否将当前伸缩组内的ECS 实例添加到新增的虚拟服务器组。 true：添加。 false：不添加。 默认值：false。 |
| VServerGr oup | Repe atList | Query | 是 | VServerGroup | 虚拟服务器组。 |
| - VServerGr oupAttribu te | Repe atList |  | 否 | VServerGroupAttribute | 虚拟服务器组属性。 |
| -- VServerGr oupId | Strin g |  | 否 | rsp-bp1jp1rge**** | 虚拟服务器组的ID。 |
| --Weight | Integ er |  | 否 | 100 | 弹性伸缩将ECS实例添加到虚拟服务器组时设置的权重，取值范围：0~100。 默认值：50。 |
| --Port | Integ er |  | 否 | 22 | 弹性伸缩将ECS实例添加到虚拟服务器组时使用的端口号，取值范围： 1~65535。 |
| - LoadBalan cerId | Strin g |  | 否 | lb- bp1u7etiogg38yvwz**** | 虚拟服务器组所属负载均衡实例的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=AttachVServerGroups &RegionId=cn-hangzhou-env17-d01 &ScalingGroupId=asg-bp18p2yfxow2dloq**** &VServerGroup=VServerGroup
```

&公共请求参数弹性伸缩 ESS 正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

`XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

**文档补充说明**

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您未授予弹性伸缩完整的 Open API调用权限。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 404 | InvalidLoadBalancerId. NotFound | The load balancer "%s" does not exist. | 账号下不存在指定的负载均衡实例。 |
| 400 | InvalidLoadBalancerId. RegionMismatch | The load balancer "%s" and the specified scaling group are not in the same Region. | 负载均衡实例与伸缩组不在同一地域。 |
| 400 | IncorrectLoadBalancer Status | The current status of the load balancer "%s" does not support this action. | 当前负载均衡实例状态不支持此操作。 |
| 400 | IncorrectLoadBalancer HealthCheck | The current health check type of the load balancer "%s" does not support this action. | 当前负载均衡实例未开启健康检查。 |
| 400 | InvalidLoadBalancerId. VPCMismatch | The specified virtual switch and the instance in the load balancer "%s" are not in the same VPC. | 负载均衡实例与伸缩组不在同一VPC下。 |
| 400 | InvalidVServerGroupId. ForLoadBalancer | Invalid VServerGroupId For LoadBalancer "%s". | VServerGroupId对应的虚拟服务器组不属于指定的负载均衡实例。 |

弹性伸缩 ESS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | QuotaExceeded.VServ erGroup | VServerGroup quota exceeded in the specified scaling group. | 当前伸缩组内可配置的虚拟服务器组个数达到上限。 |

#### DetachVServerGroups

**接口说明**

确定待移除的虚拟服务器组时，需要同时指定以下参数： 负载均衡实例ID（LoadBalancerId） 虚拟服务器组ID（VServerGroupId） 虚拟服务器组端口号（Port） 如果请求参数中的虚拟服务器组与伸缩组中的虚拟服务器组相匹配，则移除该虚拟服务器组。如果未能匹配，则忽略移除请求，且接口不报错。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 |  | 描述 |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Action | String | 是 | DetachVServerG roups |  | 系统规定参数，取值： DetachVServerGroups。 |  |  |  |
| RegionId | String | 是 | cn-hangzhou- env17-d01 |  | 伸缩组所属地域的ID，如 cn- hangzhou-env17-d01 、 cn- shanghai-env17-d01 。更多信息，请参见新云上手指南中的地域和可用区章节。 |  |  |  |
|  |  |  |  |  |  | cn- |  |  |
|  |  |  |  |  | hangzhou-env17-d01 |  |  |  |
|  |  |  |  |  |  |  | cn- |  |
|  |  |  |  |  | shanghai-env17-d01 |  |  |  |
| ScalingGroupId | String | 是 | asg- bp1fo0dbtsbmq a9h**** |  | 伸缩组的ID。 |  |  |  |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** |  | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |  |  |  |
| VServerGroup.N. LoadBalancerId | String | 否 | lb- bp1p90y3ya9h8 s62d**** |  | 虚拟服务器组所属负载均衡实例的ID。 N为负载均衡实例编号，取值范围： 1~5。 |  |  |  |

弹性伸缩 ESS

| VServerGroup.N. VServerGroupAtt ribute.N.VServer GroupId | String | 否 | rsp- bp1jp1rge**** | 虚拟服务器组ID。其中： 第一个N为负载均衡实例编号，取值范围：1~5。 第二个N为负载均衡实例下虚拟服务器组的编号，取值范围：1~5。 |
|---|---|---|---|---|
| VServerGroup.N. VServerGroupAtt ribute.N.Port | Integer | 否 | 22 | 弹性伸缩将ECS实例添加到虚拟服务器组时使用的端口号，取值范围：1~65535。 其中： 第一个N为负载均衡实例编号，取值范围：1~5。 第二个N为负载均衡实例下虚拟服务器组的编号，取值范围：1~5。 |
| ForceDetach | Boolean | 否 | false | 是否从待移除虚拟服务器组中移除当前伸缩组内的ECS实例。 true：移除ECS实例。 false：不移除ECS实例。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DetachVServerGroups &RegionId=cn-hangzhou-env17-d01 &ScalingGroupId=asg-bp1fo0dbtsbmqa9h**** &VServerGroup.1.LoadBalancerId=lb-bp1p90y3ya9h8s62d**** &VServerGroup.1.VServerGroupAttribute.1.VServerGroupId=rsp-bp1jp1rge**** &VServerGroup.1.VServerGroupAttribute.1.Port=22
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "requestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您未授予弹性伸缩完整的 Open API调用权限。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 400 | InvalidParameter | The specified value of parameter "%s" is not valid. | 参数值不合法。 |
| 400 | MissingParameter | The input parameter "%s" that is mandatory for processing this request is not supplied. | 缺少必要的参数。 |

#### AttachAlbServerGroups

调用AttachAlbServerGroups向伸缩组添加一个或多个ALB服务器组。

**接口说明**

向伸缩组添加ALB服务器组时，需要满足以下条件： 伸缩组的网络类型必须为VPC，且与ALB服务器组处于同一VPC。 ALB服务器组必须处于可用状态。 伸缩组支持添加的ALB服务组数量有限，不支持添加超出数量的ALB服务器组。如需查看或手动申请提升配额值，请前往配额中心控制台查看。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AttachAlbServer Groups | 系统规定参数。取值： AttachAlbServerGroups。 |

弹性伸缩 ESS

| AlbServerGroup. N.AlbServerGrou pId | String | 是 | sgp- ddwb0y0g6y9bj m**** | ALB服务器组的ID。 N为ALB服务器组的编号。一个伸缩组支持关联的ALB服务器组数量有限，如需查看或手动申请提升配额值，请前往配额中心控制台查看。 |
|---|---|---|---|---|
| AlbServerGroup. N.Port | Integer | 是 | 22 | 弹性伸缩将ECS实例添加到ALB服务器组后，ECS实例使用的端口号，取值范围： 1~65535。 N为ALB服务器组的编号。 说明如果N相同，Port不同，系统会默认向伸缩组关联多个不同Port的该ALB服务器组。 |
| AlbServerGroup. N.Weight | Integer | 是 | 100 | 弹性伸缩将ECS实例添加到ALB服务器组后，ECS实例作为后端服务器的权重。权重越高，ECS实例将被分配到越多的访问请求。如果权重为0，则ECS实例不会收到访问请求。取值范围：0~100。 N为ALB服务器组的编号。 |
| RegionId | String | 是 | cn-hangzhou- env17-d01 | 伸缩组所属地域的ID，如cn-hangzhou- env17-d01、cn-shanghai-env17- d01。更多信息，请参见新手上云指南中的地域和可用区章节。 |
| ScalingGroupId | String | 是 | asg- bp18p2yfxow2dl oq**** | 伸缩组的ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |
| ForceAttach | Boolean | 否 | false | 是否将当前伸缩组内的ECS实例添加到新增的ALB服务器组。 true：添加，并返回 ScalingActivityId ，您可以通过查看该伸缩活动ID来确定已有实例是否添加成功。 false：不添加。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
|---|---|---|---|
| ScalingActivity Id | String | asa- 2ze6wxj8vsohn6j9* *** | 添加ALB服务器组，并将伸缩组内的ECS实例添加到该ALB服务器组时，伸缩活动的ID。仅当 ForceAttach 取值为 true 时，返回该参数。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=AttachAlbServerGroups &AlbServerGroup.1.AlbServerGroupId=sgp-ddwb0y0g6y9bjm**** &AlbServerGroup.1.Port=22 &AlbServerGroup.1.Weight=100 &RegionId=cn-hangzhou-env17-d01 &ScalingGroupId=asg-bp18p2yfxow2dloq****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScalingActivityId>asa-2ze6wxj8vsohn6j9****</ScalingActivityId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingActivityId": "asa-2ze6wxj8vsohn6j9****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AlbServerGroup.NotExi st | The ServerGroup "%s" do(es) not exist. | 账号下不存在指定的ALB 服务器组。 |
| 400 | AlbServerGroup.Alread yAttached | The ALB ServerGroups are already attached. | 当前ALB服务器组已经添加到伸缩组中。 |

#### DetachAlbServerGroups

弹性伸缩 ESS 调用DetachAlbServerGroups从伸缩组移出一个或多个ALB服务器组。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DetachAlbServer Groups | 系统规定参数。取值： DetachAlbServerGroups。 |
| AlbServerGroup. N.AlbServerGrou pId | String | 是 | sgp- ddwb0y0g6y9bj m**** | ALB服务器组的ID。N为ALB服务器组的编号。 |
| AlbServerGroup. N.Port | Integer | 是 | 22 | ALB服务器组中ECS实例使用的端口号。N 为ALB服务器组的编号。 |
| RegionId | String | 是 | cn-hangzhou- env17-d01 | 伸缩组所属的地域ID，如cn-hangzhou- env17-d01、cn-shanghai-env17- d01。更多信息，请参见新手入门指南中的地域和可用区章节。 |
| ScalingGroupId | String | 是 | asg- bp18p2yfxow2dl oq**** | 伸缩组的ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |
| ForceDetach | Boolean | 否 | false | 是否将从待移出ALB服务器组中移出已有的ECS实例。 true：移出，并返回 ScalingActivityId ，您可以通过查看该伸缩活动ID来确定已有实例是否移出成功。 false：不移出。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingActivity Id | String | asa- 2ze6wxj8vsohn6j9* *** | 移出ALB服务器组，并移出该ALB服务器组内的 ECS实例时，伸缩活动的ID。仅当 ForceDetach 取值为 true 时，返回该参数。 |

弹性伸缩 ESS

**示例**

请求示例

```
http(s)://ess.example.com?Action=DetachAlbServerGroups &AlbServerGroup.1.AlbServerGroupId=sgp-ddwb0y0g6y9bjm**** &AlbServerGroup.1.Port=22 &RegionId=cn-hangzhou-env17-d01 &ScalingGroupId=asg-bp18p2yfxow2dloq****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScalingActivityId>asa-2ze6wxj8vsohn6j9****</ScalingActivityId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingActivityId": "asa-2ze6wxj8vsohn6j9****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AlbServerGroup.NotAtt ached | The ALB server groups are not attached to specific ScalingGroup. | 当前ALB服务器组未添加到伸缩组中。 |

#### AttachLoadBalancers

**接口说明**

向伸缩组添加负载均衡实例时需要满足以下条件： 负载均衡实例与伸缩组必须属于同一账号。 负载均衡实例与伸缩组必须处于同一地域。 负载均衡实例必须处于运行中状态。 负载均衡实例至少配置有一个监听且必须开启健康检查。 如果负载均衡实例与伸缩组的网络类型均为VPC，必须处于同一VPC。 当伸缩组的网络类型为VPC，负载均衡实例的网络类型为经典网络时，如果负载均衡实例后端服务器中包含VPC实例，该实例必须与伸缩组处于同一VPC。 不超过伸缩组关联负载均衡实例的限额，具体限额，请参见弹性伸缩中的使用限制章节。 弹性伸缩 ESS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AttachLoadBala ncers | 系统规定参数，取值： AttachLoadBalancers。 |
| LoadBalancer.N | RepeatL ist | 是 | lb- 2zeur05gfs**** | 负载均衡实例的ID，单次最多支持添加5个负载均衡实例。 |
| ScalingGroupId | String | 是 | asg- bp1avr6ensitts3 w**** | 伸缩组的ID。 |
| ForceAttach | Boolean | 否 | false | 是否把当前伸缩组内的实例全部添加为负载均衡实例的后端服务器，取值范围： true：添加。 false：不添加。 默认值：false。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |
| Async | Boolean | 否 | false | 添加负载均衡实例时，是否采用异步调用的方式。异步调用能保证操作的事务性， 即所有操作都执行成功或者某个操作失败时所有操作的执行结果都不生效，建议您采用异步调用。 取值范围： true：异步调用。请求将返回伸缩活动的ID。 false：同步调用。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingActivity Id | String | asa- bp140qd7mak8k63 f**** | 伸缩活动的ID。 仅当 Async=true 时返回该值。您可使用API DescribeScalingActivities 遍历查询返回的伸缩活动ID，查看伸缩活动的执行状态。 |

弹性伸缩 ESS

**示例**

请求示例

```
http(s)://ess.example.com/?Action=AttachLoadBalancers &LoadBalancer.1=lb-2zeur05gfs**** &ScalingGroupId=asg-bp1avr6ensitts3w****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScalingActivityId>asa-bp140qd7mak8k63f****</ScalingActivityId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingActivityId": "asa-bp140qd7mak8k63f****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您并未授予弹性伸缩完整的Open API调用权限。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 400 | QuotaExceeded.LoadB alancer | LoadBalancer quota exceeded in the scaling group "%s". | 伸缩组中负载均衡实例超出配额限制。 |
| 404 | InvalidLoadBalancerId. NotFound | The load balancer "%s" does not exist. | 不存在指定的负载均衡实例。 |
| 400 | InvalidLoadBalancerId. RegionMismatch | The load balancer "%s" and the specified scaling group are not in the same Region. | 负载均衡实例与伸缩组不在同一地域。 |

弹性伸缩 ESS

| 400 | IncorrectLoadBalancer Status | The current status of the load balancer "%s" does not support this action. | 当前负载均衡实例状态不支持此操作。 |
|---|---|---|---|
| 400 | IncorrectLoadBalancer HealthCheck | The current health check type of the load balancer "%s" does not support this action. | 当前负载均衡实例未开启健康检查。 |
| 400 | InvalidLoadBalancerId. VPCMismatch | The specified virtual switch and the instance in the load balancer "%s" are not in the same VPC. | 负载均衡实例与伸缩组不在同一VPC下。 |
| 400 | QuotaExceeded.Backe ndServer | Backend server quota exceeded in the load balancer "%s". | 负载均衡实例后端服务器数量超出限额。 |
| 404 | InvalidScalingConfigur ationId.NotFound | The specified scaling configuration does not exist. | 未找到当前伸缩组启用的伸缩配置。 |

#### DetachLoadBalancers

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DetachLoadBala ncers | 系统规定参数，取值： DetachLoadBalancers。 |
| LoadBalancer.N | RepeatL ist | 是 | lb- 2zeur05gfs**** | 负载均衡实例的ID，单次最多支持移除5个负载均衡实例。 |
| ScalingGroupId | String | 是 | asg- bp1ffogfdauy0jw 0**** | 伸缩组的ID。 |
| ForceDetach | Boolean | 否 | false | 是否移除负载均衡实例后端服务器中属于当前伸缩组的ECS实例。取值范围： true：移除ECS实例。 false：不移除ECS实例。 默认值：false。 |

弹性伸缩 ESS

| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |
|---|---|---|---|---|
| Async | Boolean | 否 | false | 添加负载均衡实例时，是否采用异步调用的方式。异步调用能保证操作的事务性， 即所有操作都执行成功或者某个操作失败时所有操作的执行结果都不生效，建议您采用异步调用。 取值范围： true：异步调用。请求将返回伸缩活动的ID。 false：同步调用。 默认值：false。 |
| RegionId | String | 否 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingActivity Id | String | asa- bp140qd7mak8k63 f**** | 伸缩活动的ID。 仅当 Async=true 时返回该值。您可使用API DescribeScalingActivities 遍历查询返回的伸缩活动ID，查看伸缩活动的执行状态。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DetachLoadBalancers &ScalingGroupId=asg-bp1ffogfdauy0jw0**** &ForceDetach=false &ClientToken=123e4567-e89b-12d3-a456-42665544**** &Async=false &LoadBalancer=["lb-2zeur05gfs****"] &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScalingActivityId>asa-bp140qd7mak8k63f****</ScalingActivityId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingActivityId": "asa-bp140qd7mak8k63f****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您并未授予弹性伸缩完整的Open API调用权限。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 账号下不存在指定的伸缩组。 |
| 404 | InvalidLoadBalancerId. NotFound | The Load Balancer "%s" does not exist. | 伸缩组中不存在指定的负载均衡实例。 |

### 伸缩配置

#### CreateScalingConfiguration

**接口说明**

伸缩配置用来指定弹性扩张时使用的ECS实例模板，支持以下实例配置方式： InstancePatternInfo.N：智能配置模式，无需指定具体的实例规格，只需根据业务需求指定实例的 vCPU核数、内存大小、规格族级别以及最高价格，系统会自动筛选符合要求的实例规格，并优先选择价格最低的实例规格创建ECS实例。该模式仅适用于网络类型为专有网络的伸缩组，能够有效降低扩容时实例规格库存不足的情况。 InstanceType：指定一种实例规格。 InstanceTypes.N：指定多种实例规格。 InstanceTypeOverride.N：指定多种实例规格，并为不同的实例规格配置权重。 Cpu和Memory：指定CPU和内存定义实例规格的范围。该方式仅适用于扩缩容策略为成本优化策略的伸缩组，且伸缩配置未指定实例规格的场景。 弹性伸缩 ESS InstanceType、InstanceTypes.N、InstanceTypeOverride.N、Cpu和Memory这

**说明**

四种方式不能同时指定。如果指定了InstanceTypes.N，InstanceType将被忽略，但 InstanceType或InstanceTypes.N可以与InstancePatternInfo.N同时指定，与 InstancePatternInfo.N同时指定时，弹性伸缩优先使用您指定的实例规格扩容，当指定的实例规格无库存时，再使用符合InstancePatternInfo.N配置的实例规格。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateScalingCo nfiguration | 系统规定参数。取值： CreateScalingConfiguration。 |
| ScalingGroupId | String | 是 | asg- bp14wlu85wrpc hm0**** | 伸缩配置所属的伸缩组的ID。 |
| ImageId | String | 否 | centos6u5 64 2 _ _ 0G aliaegis****. _ vhd | 镜像文件ID，自动创建实例时使用的镜像资源。 |
| ImageName | String | 否 | image**** | 镜像文件名称，同一个地域内镜像名称唯一。 如果设置了ImageId，ImageName将被忽略。不支持通过ImageName设置镜像市场镜像。 |
| InstanceType | String | 否 | ecs.g6.large | ECS实例的实例规格，更多信息，请参见云服务器ECS文档中的实例规格族章节。 |
| Cpu | Integer | 否 | 2 | vCPU个数。单位：核。 同时指定CPU和Memory可以定义实例规格范围，例如，CPU等于2且Memory等于 16时，可以定义配置为2 vCPU和16 GiB 的所有实例规格。 |
| Memory | Integer | 否 | 16 | 内存大小。单位：GiB。 同时指定CPU和Memory可以定义实例规格范围。例如，CPU等于2且Memory等于 16时，可以定义配置为2 vCPU和16 GiB 的所有实例规格。 |
| DeploymentSetI d | String | 否 | ds- bp1frxuzdg87zh 4pz**** | ECS实例所属的部署集的ID。 |
| SecurityGroupId | String | 否 | sg-280ih**** | ECS实例所属的安全组的ID，同一个安全组内的ECS实例可以互相访问。 |

弹性伸缩 ESS

| IoOptimized | String | 否 | optimized | 是否为I/O优化实例。已停售的实例规格实例默认值是none，其他实例规格默认值是 optimized。取值范围： none：非I/O优化实例。 optimized：I/O优化实例。 |
|---|---|---|---|---|
| InternetMaxBan dwidthIn | Integer | 否 | 100 | 公网入带宽最大值，单位：Mbps (Mega bit per second)，取值范围：1~200。 如果您没有指定该参数，则入带宽将自动被设置为200 Mbps。 |
| InternetMaxBan dwidthOut | Integer | 否 | 50 | 公网出带宽最大值，单位：Mbps (Mega bit per second)，取值范围： 按带宽计费：0~100，如果您没有指定该参数，则出带宽将自动被设置为0 Mbps。 按流量计费：0~100，如果您没有指定该参数，则会出现报错。 |
| SystemDisk.Cate gory | String | 否 | cloud ssd _ | 系统盘的磁盘种类。取值范围： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ ephemeral ssd：本地SSD盘。 _ InstanceType为系列I的实例规格且实例属于非I/O优化实例时，默认值：cloud。 否则，默认值：cloud efficiency。 _ |
| SystemDisk.Size | Integer | 否 | 100 | 系统盘的大小，单位：GiB。取值范围： cloud：20~500。 cloud efficiency：20~500。 _ cloud ssd：20~500。 _ ephemeral ssd：20~500。 _ 默认值：max{40, ImageSize}。 指定该参数后，系统盘大小必须大于等于 max{20, ImageSize}。 |
| SystemDisk.Disk Name | String | 否 | cloud ssdSyste _ m | 系统盘的名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 和 https:// 开头。 可以包含数字、半角冒号（:）、下划线 （ ）或者短划线（-）。 _ |
| SystemDisk.Des cription | String | 否 | Test system disk. | 系统盘的描述。长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。 |

弹性伸缩 ESS

| SystemDisk.Auto SnapshotPolicyId | String | 否 | sp- bp12m37ccmxv bmi5**** | 系统盘使用的自动快照策略ID。 |
|---|---|---|---|---|
| ScalingConfigura tionName | String | 否 | scalingconfig*** * | 伸缩配置的名称，2~64英文或中文字符， 以数字、大小写字母或中文开头，可包含数字、下划线（ ）、短划线（-）或英文 _ 句号（.）。 在同一地域下同一伸缩组内伸缩配置名称唯一。如果您没有指定该参数，则默认使用伸缩配置的ID。 |
| LoadBalancerWe ight | Integer | 否 | 50 | 后端服务器的权重，取值范围：1~100。 默认值：50。 |
| Tags | String | 否 | {"key1":"value1 ","key2":"value2 ", ... "key5":"value5" } | ECS实例的标签。标签以键值对方式传入，最多可以使用5组标签。Key和Value 的使用要求如下： Key最多支持64个字符，不能以aliyun 和acs:开头，不能包含 http:// 或者 https:// 。一旦使用标签，Key 不允许为空字符串。 Value最多支持128个字符，不能以 aliyun和acs:开头，不能包含 http:// 或者 https:// 。 Value可以为空字符串。 |
| UserData | String | 否 | echo hello ecs! | ECS实例的自定义数据，需要以Base64方式编码，编码前的原始数据最多为16 KB。 |
| KeyPairName | String | 否 | KeyPairTest | 登录ECS实例时使用的密钥对的名称。 对Windows实例，该参数将被忽略，默认为空。 对Linux实例，密码登录方式会被初始化成禁止。 |
| RamRoleName | String | 否 | RamRoleTest | ECS实例的RAM角色名称。RAM角色名称由RAM提供和维护，您可调用API ListRoles查询可用的RAM角色。创建 RAM角色的方法请参见API CreateRole。 |
| SecurityEnhance mentStrategy | String | 否 | Active | 是否开启安全加固。取值范围： Active：启用安全加固，只对公共镜像生效。 Deactive：不启用安全加固，对所有镜像类型生效。 |

弹性伸缩 ESS

| InstanceName | String | 否 | Instance**** | 使用本伸缩配置自动创建的ECS实例的名称。 |
|---|---|---|---|---|
| HostName | String | 否 | Host**** | 云服务器的主机名。半角句号（.）或短划线（-）不能作为首尾字符，不能连续使用半角句号（.）或短划线（-）。另外，不同类型实例的命名要求如下： Windows实例：主机名长度为2~15字符，可以包含大小写字母、数字和短划线（-）。不能包含半角句号（.），不能全是数字。 其他类型实例（例如Linux等）：主机名长度为2~64字符，可以包含多个半角句号（.）。两个半角句号（.）之间为一段，每段可以包含大小写字母、数字和短划线（-）。 |
| PasswordInherit | Boolean | 否 | false | 是否使用镜像预设的密码。使用该参数时，您需要确保使用的镜像已经设置了密码。 |
| Password | String | 否 | 123-abc**** | ECS实例的密码。长度为8至30个字符， 必须同时包含大小写英文字母、数字和特殊符号中的三类字符。特殊符号如下所示： ()` ~!@#$%^&*- +=\\|{} _ []:;'<>,.?/ 其中，Windows实例不能以斜线号（/） 为密码首字符。 说明如果传入Password参数，建议您使用HTTPS协议发送请求，避免密码泄露。 |
| HpcClusterId | String | 否 | hpc-clusterid | ECS实例所属的HPC集群的ID。 |
| InstanceDescript ion | String | 否 | Test instance. | ECS实例的描述。长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见云服务器ECS文档中的如何保证幂等性章节。 |
| Ipv6AddressCou nt | Integer | 否 | 1 | 为弹性网卡指定随机生成的IPv6地址数量。 |

弹性伸缩 ESS

| CreditSpecificati on | String | 否 | Standard | 指定突发性能实例的运行模式。取值范围： Standard：标准模式。 Unlimited：无性能约束模式。 更多信息，请参见云服务器ECS文档中的突发性能实例概述下的性能模式章节。 |
|---|---|---|---|---|
| ImageFamily | String | 否 | hangzhou-daily- update | 镜像族系名称，通过设置该参数来获取当前镜像族系内最新可用的自定义镜像，用于创建实例。如果已经设置了参数 ImageId，则不能设置该参数。 |
| DedicatedHostId | String | 否 | dh- bp67acfmxazb4 p**** | 是否在专有宿主机上创建ECS实例。由于专有宿主机不支持创建抢占式实例，指定 DedicatedHostId参数后，会自动忽略请求中的SpotStrategy和SpotPriceLimit设置。 您可以调用API DescribeDedicatedHosts接口查询专有宿主机ID列表。 |
| Affinity | String | 否 | default | 专有宿主机实例是否与专有宿主机关联。 取值范围： default：实例不与专有宿主机关联。已启用节省停机模式的实例，停机后再次启动时，若原专有宿主机可用资源不足，则实例被放置在自动部署资源池的其它专有宿主机上。 host：实例与专有宿主机关联。已启用节省停机模式的实例，停机后再次启动时，仍放置在原专有宿主机上。若原专有宿主机可用资源不足，则实例重启失败。 默认值：default。 |
| Tenancy | String | 否 | default | 是否在专有宿主机上创建实例。取值范围： default：创建非专有宿主机实例。 host：创建专有宿主机实例。若您不指定DedicatedHostId，则由阿里云自动选择专有宿主机放置实例。 默认值：default。 |

弹性伸缩 ESS

| PrivatePoolOptio ns.MatchCriteria | String | 否 | Open | 实例启动的私有池容量选项。弹性保障服务或容量预定服务在生效后会生成私有池容量，供实例启动时选择。取值范围： Open：开放模式。将自动匹配开放类型的私有池容量。如果没有符合条件的私有池容量，则使用公共池资源启动。 该模式下无需设置 PrivatePoolOptions.Id参数。 Target：指定模式。使用指定的私有池容量启动实例，如果该私有池容量不可用，则实例会启动失败。该模式下必须指定私有池ID，即 PrivatePoolOptions.Id参数为必填项。 None：不使用模式。实例启动将不使用私有池容量。 |
|---|---|---|---|---|
| PrivatePoolOptio ns.Id | String | 否 | eap- bp67acfmxazb4 **** | 私有池ID。即弹性保障服务ID或容量预定服务ID。 |
| SystemDisk.Encr ypted | Boolean | 否 | false | 是否加密系统盘。取值范围： true：加密。 false：不加密。 默认值：false。 |
| SystemDisk.KMS KeyId | String | 否 | 0e478b7a-4262- 4802-b8cb- 00d3fb40**** | 系统盘使用的KMS密钥ID。 |
| SystemDisk.Encr yptAlgorithm | String | 否 | AES-256 | 系统盘采用的加密算法。取值范围： AES-256。 SM4-128。 默认值：AES-256。 |
| InstanceTypes.N | RepeatL ist | 否 | ecs.g6.large | 多实例规格参数。 如果使用了 InstanceTypes.N，InstanceType将被忽略。 InstanceTypes.N参数中，N的取值范围：1~10，即一个伸缩配置内最多可以设置10种实例规格，其中N代表当前伸缩配置中实例规格的优先级，编号为 1的实例规格优先级最高，实例规格优先级随着编号的增大依次降低。 当无法根据优先级较高的实例规格创建出实例时，弹性伸缩服务会自动选择下一优先级的实例规格来创建实例。 |

弹性伸缩 ESS

| InstanceTypeOv erride.N.Instanc eType | String | 否 | ecs.c5.xlarge | 当您需要指定伸缩配置中实例规格的容量时，请同时指定本参数和 InstanceTypeOverride.N.WeightedCa pacity参数。 本参数用于指定实例规格。您可以指定N个本参数，结合 InstanceTypeOverride.N.WeightedCa pacity参数，扩展多实例规格支持自定义权重。N的取值范围：1~10。 说明指定本参数时，不允许同时指定InstanceTypes.N或 InstanceType。 InstanceType的取值范围：关于在售的 ECS实例规格信息，请参见云服务器 ECS文档中的实例规格族章节。 |
|---|---|---|---|---|
| InstanceTypeOv erride.N.Weighte dCapacity | Integer | 否 | 4 | 当您需要指定伸缩配置中实例规格的容量时，在指定 InstanceTypeOverride.N.InstanceTyp e后，再指定本参数。两个参数一一对应，N需要保持一致。 本参数用于指定实例规格的权重，即实例规格的单台实例在伸缩组中表示的容量大小。权重越大，满足期望容量所需的本实例规格的实例数量越少。 由于每个实例规格的vCPU个数、内存大小等性能指标会有差异，您可以根据自身需求，给不同的实例规格配置不同的权重。 例如： 当前容量：0。 期望容量：6。 ecs.g5.xlarge规格容量：4。 为满足期望容量，伸缩组将为用户扩容2台 ecs.g5.xlarge实例。 说明扩容时伸缩组的容量不得超过最大容量（MaxSize）与实例规格的最大权重之和。 WeightedCapacity的取值范围： 1~500。 |
| DataDisk.N.Auto SnapshotPolicyId | String | 否 | sp- bp19nq9enxqko mib**** | 数据盘使用的自动快照策略ID，N的取值范围：1~16。 |
| DataDisk.N.Encr ypted | String | 否 | false | 数据盘N是否加密，N的取值范围： 1~16。该参数取值范围： true：加密。 false：不加密。 默认值：false。 |

弹性伸缩 ESS

| DataDisk.N.Desc ription | String | 否 | Test data disk. | 数据盘的描述，N的取值范围：1~16。长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。 |
|---|---|---|---|---|
| DataDisk.N.Snap shotId | String | 否 | s-280s7**** | 创建数据盘时使用的快照，N的取值范围： 1~16。指定该参数后，DataDisk.N.Size 会被忽略，实际创建的磁盘大小为指定快照的大小。 如果该快照创建于2013年7月15日或之前，调用会被拒绝，返回参数中会提示 InvalidSnapshot.TooOld。 |
| DataDisk.N.Cate gories.N | RepeatL ist | 否 | cloud | 数据盘N的多磁盘类型。第一个N表示第N 块数据盘，取值范围：1~16。第二个N表示第N块数据盘的第N种磁盘类型，取值范围：1~4，即一个伸缩配置内最多可以为数据盘指定4种磁盘类型。N越小，优先级越高。 当无法使用高优先级的磁盘类型时，弹性伸缩自动尝试下一优先级的磁盘类型创建数据盘。取值范围： cloud：普通云盘。随实例创建的普通云盘的DeleteWithInstance属性为 true。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ 说明指定本参数时，不允许同时指定DataDisk.N.Category参数。 |
| DataDisk.N.Size | Integer | 否 | 100 | 数据盘N的磁盘大小，N的取值范围： 1~16，内存单位：GiB。取值范围： cloud：5~2000。 cloud efficiency：20~32768。 _ cloud ssd：20~32768。 _ ephemeral ssd：5~800。 _ 指定该参数后，磁盘大小必须大于等于快照大小（快照通过SnapshotId指定）。 |
| DataDisk.N.Devi ce | String | 否 | /dev/xvdb | 数据盘挂载点，N的取值范围：1~16。如果您没有指定该参数，则默认在自动创建 ECS实例时由系统分配，从/dev/xvdb开始，到/dev/xvdz结束。 |

弹性伸缩 ESS

| DataDisk.N.Disk Name | String | 否 | cloud ssdData _ | 数据盘的名称，N的取值范围：1~16。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 和 https:// 开头。可以包含数字、半角冒号（:）、下划线 （ ）或者短划线（-）。 _ |
|---|---|---|---|---|
| DataDisk.N.Cate gory | String | 否 | cloud ssd _ | 数据盘N的磁盘种类，N的取值范围： 1~16。该参数取值范围： cloud：普通云盘。随实例创建的普通云盘的DeleteWithInstance属性为 true。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ ephemeral ssd：本地SSD盘。 _ 对于I/O优化实例，默认值为 cloud efficiency。对于非I/O优化实例， _ 默认值为cloud。 |
| DataDisk.N.Dele teWithInstance | Boolean | 否 | true | 指定数据盘是否随实例释放，N的取值范围：1~16。该参数取值范围： true：释放实例时，该磁盘随实例一起释放。 false：释放实例时，该磁盘保留不释放。 默认值：true。 说明该参数只可对独立云盘设置（例如，DataDisk.N.Category 设置为cloud、cloud efficiency、 _ cloud ssd），否则会出现报错。 _ |
| DataDisk.N.KMS KeyId | String | 否 | 0e478b7a-4262- 4802-b8cb- 00d3fb40**** | 数据盘对应的KMS密钥的ID，N的取值范围：1~16。 |
| SecurityGroupId s.N | RepeatL ist | 否 | sg-280ih**** | ECS实例所属的安全组的ID，同一个安全组内的ECS实例可以互相访问。 |

弹性伸缩 ESS

| InstancePatternI nfo.N.Cores | Integer | 否 | 2 | 智能配置模式下，实例规格的vCPU内核数目，用于筛选符合要求的实例规格范围。 更多信息，请参见云服务器ECS文档中的实例规格族章节。N的取值范围： 1~10。 请注意以下信息： InstancePatternInfo.N参数仅适用于伸缩组的网络类型为专有网络。 InstancePatternInfo.N参数必须同时配置InstancePatternInfo.N.Cores和 InstancePatternInfo.N.Memory。 如果您已经通过InstanceType或 InstanceTypes.N参数指定了实例规格，弹性伸缩优先使用您指定的实例规格扩容，当指定的实例规格无库存时， 再从符合InstancePatternInfo.N参数值的实例规格中优先使用价格最低的实例规格扩容。 |
|---|---|---|---|---|
| InstancePatternI nfo.N.InstanceFa milyLevel | String | 否 | EnterpriseLevel | 智能配置模式下，实例规格族级别，用于筛选符合要求的实例规格范围。N的取值范围：1~10。取值范围： EntryLevel：入门级，即共享型实例规格。成本更低，但是无法保证实例计算性能的稳定。适用于平时CPU使用率低的业务场景。更多信息，请参见云服务器ECS文档中的共享型。 EnterpriseLevel：企业级。性能稳定，资源独享，适用于对稳定性要求高的业务场景。更多信息，请参见云服务器ECS文档中的实例规格族章节。 CreditEntryLevel：积分入门级，即突发性能实例。通过CPU积分来保证计算性能，适用于平时CPU使用率低、偶有突发CPU使用率的情况。更多信息，请参见云服务器ECS文档中的突发型章节。 |
| InstancePatternI nfo.N.MaxPrice | Float | 否 | 2 | 智能配置模式下，按量付费实例或者抢占式实例可接受的每小时最高价格，用于筛选符合要求的实例规格范围。N的取值范围：1~10。 |
| InstancePatternI nfo.N.Memory | Float | 否 | 4 | 智能配置模式下，实例规格的内存大小， 单位：GiB，用于筛选符合要求的实例规格范围。更多信息，请参见云服务器ECS文档中的实例规格族章节。N的取值范围： 1~10。 |

弹性伸缩 ESS

| SystemDiskCate gories.N | RepeatL ist | 否 | cloud | 系统盘的多磁盘类型。N的取值范围： 1~4，即一个伸缩配置内最多可以为系统盘指定4种磁盘类型。N越小，优先级越高。当无法使用高优先级的磁盘类型时， 弹性伸缩自动尝试下一优先级的磁盘类型创建系统盘。取值范围： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ 说明指定本参数时，不允许同时指定SystemDisk.Category。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingConfigu rationId | String | asc- bp1ffogfdauy0nu5* *** | 伸缩配置ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=CreateScalingConfiguration &ScalingGroupId=asg-bp14wlu85wrpchm0**** &ImageId=centos6u5_64_20G_aliaegis****.vhd &ImageName=image**** &InstanceType=ecs.g6.large &Cpu=2 &Memory=16 &DeploymentSetId=ds-bp1frxuzdg87zh4pz**** &SecurityGroupId=sg-280ih**** &IoOptimized=optimized &InternetMaxBandwidthIn=100 &InternetMaxBandwidthOut=50 &SystemDisk.Category=cloud_ssd &SystemDisk.Size=100 &SystemDisk.DiskName=cloud_ssdSystem &SystemDisk.Description=Test system disk. &SystemDisk.AutoSnapshotPolicyId=sp-bp12m37ccmxvbmi5**** &ScalingConfigurationName=scalingconfig**** &LoadBalancerWeight=50 &Tags={"key1":"value1","key2":"value2", ... "key5":"value5"} &UserData=echo hello ecs! &KeyPairName=KeyPairTest &RamRoleName=RamRole**** &SecurityEnhancementStrategy=Active &InstanceName=instance**** &HostName=host****
```

弹性伸缩 ESS

```json
&ostae ost &PasswordInherit=false &Password=123abc**** &HpcClusterId=hpc-clusterid &InstanceDescription=Test instance. &ClientToken=123e4567-e89b-12d3-a456-42665544**** &Ipv6AddressCount=1 &CreditSpecification=Standard &ImageFamily=hangzhou-daily-update &DedicatedHostId=dh-bp67acfmxazb4p**** &Affinity=default &Tenancy=default &PrivatePoolOptions.MatchCriteria=Open &PrivatePoolOptions.Id=eap-bp67acfmxazb4**** &InstanceTypes=["ecs.g6.large"] &InstanceTypeOverride=[{"InstanceType":"ecs.c5.xlarge","WeightedCapacity":4}] &DataDisk=[{"PerformanceLevel":"PL1","AutoSnapshotPolicyId":"spbp19nq9enxqkomib****","Encrypted":"false","Description":"Test data disk.","SnapshotId":"s-280s7****","Categories": ["cloud"],"Size":100,"Device":"/dev/xvdb","DiskName":"cloud_ssdData","Category":"cloud_ss ,"DeleteWithInstance":true,"KMSKeyId":"0e478b7a-4262-4802-b8cb- 00d3fb40****","ProvisionedIops":100,"BurstingEnabled":false}] &SpotPriceLimit=[{"PriceLimit":0.5,"InstanceType":"ecs.g6.large"}] &SecurityGroupIds=["sg-bp18kz60mefs****"] &InstancePatternInfo= [{"Cores":2,"InstanceFamilyLevel":"EnterpriseLevel","MaxPrice":2.0,"Memory":4.0,"Excluded stanceType":["ecs.n1.small/ecs.n1.*/*7*"],"Architecture": ["X86"],"BurstablePerformance":"Include"}] &SystemDiskCategories=["cloud"] &SystemDisk.Encrypted=false &SystemDisk.KMSKeyId=0e478b7a-4262-4802-b8cb-00d3fb40**** &SystemDisk.EncryptAlgorithm=AES-256 &SystemDisk.ProvisionedIops=100 &SystemDisk.BurstingEnabled=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <ScalingConfigurationId>asc-bp1ffogfdauy0nu5****</ScalingConfigurationId>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingConfigurationId": "asc-bp1ffogfdauy0nu5****"
}
```

**错误码**

弹性伸缩 ESS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InstanceType.Mismatc h | The specified scaling configuration and existing active scaling configuration have different instance type. | 指定的伸缩配置的实例规格与当前的伸缩配置的实例规格不匹配。 |
| 404 | InvalidDataDiskSnapsh otId.NotFound | Snapshot “XXX” does not exist. | 不存在指定的快照。 |
| 400 | InvalidDataDiskSnapsh otId.SizeNotSupported | The capacity of snapshot “XXX” exceeds the size limit of the specified disk category. | 指定快照的大小超过了磁盘大小的限制。 |
| 403 | InvalidDevice.InUse | Device “XXX” has been occupied. | 数据盘挂载点重复。 |
| 400 | InvalidImageId.Instanc eTypeMismatch | The specified image does not support the specified instance type. | 不允许在指定的实例规格下使用该镜像。 |
| 404 | InvalidImageId.NotFou nd | The specified image does not exist. | 该账号下不存在指定的镜像。 |
| 400 | InvalidKeyPairName.N otFound | The specified KeyPairName does not exist in our records. | 指定的KeyPairName不存在。 |
| 400 | InvalidNetworkType.Fo rRAMRole | RAMRole can't be used For classic instance. | 经典网络实例不支持 RamRoleName参数。 |
| 400 | InvalidParameter | The specified value of parameter KeyPairName is not valid. | Windows系统不支持 KeyPairName参数。 |
| 400 | InvalidParameter.Confl ict | The value of parameter SystemDisk.Category and parameter DataDisk.N.Category are conflict. | 指定的系统盘类型和数据盘类型冲突。 |

弹性伸缩 ESS

| 400 | InvalidRamRole.NotFo und | The specified RamRoleName does not exist. | 不存在指定的 RamRoleName。 |
|---|---|---|---|
| 400 | InvalidScalingConfigur ationName.Duplicate | The specified value of parameter ScalingConfigurationN ame is duplicated. | 已存在相同伸缩配置名。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 该账号下不存在指定的伸缩组。 |
| 400 | InvalidSecurityGroupId .IncorrectNetworkType | The network type of specified security Group does not support this action. | 指定的安全组与伸缩组指定网络类型不一致。 |
| 404 | InvalidSecurityGroupId .NotFound | The specified security group does not exist. | 该账号下不存在指定的安全组。 |
| 400 | InvalidSecurityGroupId .VPCMismatch | The specified security group and the specified virtual switch are not in the same VPC. | 指定的安全组和虚拟交换机不属于同一个虚拟专有网络。 |
| 403 | InvalidSnapshot.TooOl d | This operation is denied because the specified snapshot is created before 2013- 07-15. | 该快照创建于2013年7月 15日或之前，调用被拒绝。 |
| 403 | InvalidSystemDiskCate gory.ValueUnauthorize d | The system disk category is not authorized. | 没有创建临时磁盘系统盘的权限。 |
| 400 | InvalidUserData.Base6 4FormatInvalid | The specified parameter UserData must be base64 encoded. | UserData不符合Base64 编码规范。 |
| 400 | InvalidUserData.SizeEx ceeded | The specified parameter UserData exceeds the size. | 指定的UserData过长。 |
| 403 | QuotaExceeded.Ephe meralDiskSize | Ephemeral disk size quota exceeded. | 临时磁盘数据盘总容量超过2TiB（2048GiB）。 |

弹性伸缩 ESS

| 400 | QuotaExceeded.Scalin gConfiguration | Scaling configuration quota exceeded in the specified scaling group. | 您目前拥有的伸缩配置个数已经达到上限。 |
|---|---|---|---|
| 400 | QuotaExceeded.Securi tyGroupInstance | Instance quota exceeded in the specified security group. | 指定的安全组中添加的 ECS实例个数已经达到上限。 |

#### DescribeScalingConfigurations

调用DescribeScalingConfigurations查询现有的伸缩配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeScaling Configurations | 系统规定参数，取值： DescribeScalingConfigurations。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 伸缩配置所属伸缩组的地域ID。 |
| PageNumber | Integer | 否 | 1 | 伸缩配置列表的页码。起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 50 | 分页查询时设置的每页行数。最大值： 50。 默认值：10。 |
| ScalingGroupId | String | 否 | asg- bp17pelvl720x3 v7**** | 伸缩组的ID，您可以查询该伸缩组下所有的伸缩配置。 |
| ScalingConfigura tionId.N | RepeatL ist | 否 | asc- bp17pelvl720x5 ub**** | ScalingConfigurationId.N为待查询伸缩配置的ID，N的取值范围：1～10。 查询结果包括生效和未生效的伸缩配置， 并通过返回参数LifecycleState进行标识。 |
| ScalingConfigura tionName.N | RepeatL ist | 否 | scalingcon**** | ScalingConfigurationName.N为待查询伸缩配置的名称，N的取值范围：1～10。 查询结果会忽略失效的伸缩配置名称，并且不报错。 |

**返回数据**

弹性伸缩 ESS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 50 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingConfigu rations | Array of ScalingConfigu ration |  | 伸缩配置信息的集合。 |
| ScalingConfigu ration |  |  |  |
| Affinity | String | default | 专有宿主机实例是否与专有宿主机关联。可能值： default：实例不与专有宿主机关联。已启用节省停机模式的实例，停机后再次启动时，如果原专有宿主机可用资源不足，则实例被放置在自动部署资源池的其他专有宿主机上。 host：实例与专有宿主机关联。已启用节省停机模式的实例，停机后再次启动时，仍放置在原专有宿主机上。如果原专有宿主机可用资源不足，则实例重启失败。 |
| Cpu | Integer | 2 | vCPU个数。单位：核。 同时指定CPU和Memory可以定义实例规格范围，例如，CPU=2且Memory=16可以定义配置为2 vCPU和16 GiB的所有实例规格。弹性伸缩会结合I/O优化、可用区等因素确定可用实例规格集合，并根据价格排序为您创建价格最低的实例。 说明该区间配置效果仅在成本优化模式下且伸缩配置未设置实例规格时生效。 |
| CreationTime | String | 2014-08- 14T10:58Z | 伸缩配置的创建时间。 |
| CreditSpecifica tion | String | Standard | 突发性能实例的运行模式，可能值： Standard：标准模式，更多信息，请参见云服务器ECS文档的突发性能实例概述下的性能约束模式内容。 Unlimited：无性能约束模式，更多信息，请参见云服务器ECS文档的突发性能实例概述下的无性能约束模式内容。 |
| DataDisks | Array of DataDisk |  | 数据盘信息的集合。 |
| DataDisk |  |  |  |

弹性伸缩 ESS

| AutoSnapshot PolicyId | String | sp- bp19nq9enxqkomi b**** | 数据盘使用的自动快照策略ID。 |
|---|---|---|---|
| BurstingEnabl ed | Boolean | false | 数据盘是否开启Burst（性能突发）。可能值： true：开启。 false：未开启。 |
| Categories | List | cloud ssd _ | 数据盘的多磁盘类型。第一个磁盘类型优先级最高，其他磁盘类型的优先级依次递减。当无法使用高优先级的磁盘类型时，弹性伸缩自动尝试下一优先级的磁盘类型创建数据盘。可能值： cloud：普通云盘。随实例创建的普通云盘的 DeleteWithInstance属性为true。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ |
| Category | String | cloud | 数据盘的磁盘种类，可能值： cloud：普通云盘。随实例创建的普通云盘的 DeleteWithInstance属性为true。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ ephemeral ssd：本地SSD盘。 _ |
| DeleteWithInst ance | Boolean | true | 数据盘是否随实例释放，可能值： true：释放实例时，该磁盘随实例一起释放。 false：释放实例时，该磁盘保留不释放。 |
| Description | String | FinanceDept | 数据盘的描述。 |
| Device | String | /dev/xvdb | 数据盘的挂载点。 |
| DiskName | String | cloud ssdData _ | 数据盘的名称。 |
| Encrypted | String | false | 数据盘是否加密，可能值： true：加密。 false：不加密。 |
| KMSKeyId | String | 0e478b7a-4262- 4802-b8cb- 00d3fb40**** | 数据盘对应的KMS密钥的ID。 |
| PerformanceL evel | String | PL1 | 说明该参数未开放使用。 |

弹性伸缩 ESS

| ProvisionedIop s | Long | 100 | 数据盘预配置的IOPS（Input/Output Operations Per Second）性能指标。 说明 IOPS（Input/Output Operations Per Second）指每秒能处理的I/O个数，表示块存储处理读写（输出/输入）的能力，单位为次。 |
|---|---|---|---|
| Size | Integer | 200 | 数据盘的磁盘大小，内存单位为GiB。可能值： cloud：5~2000。 cloud efficiency：20~32768。 _ cloud ssd：20~32768。 _ ephemeral ssd：5~800。 _ |
| SnapshotId | String | s-23f2i**** | 创建数据盘使用的快照ID。 |
| DedicatedHost Id | String | dh- bp67acfmxazb4p** ** | 是否在专有宿主机上创建ECS实例。由于专有宿主机不支持创建抢占式实例，指定 DedicatedHostId参数后，会自动忽略请求中的 SpotStrategy和SpotPriceLimit设置。 您可以通过API DescribeDedicatedHosts查询专有宿主机ID列表。 |
| DeploymentSe tId | String | ds- bp1frxuzdg87zh4p **** | ECS实例所属的部署集的ID。 |
| HostName | String | LocalHost | 云服务器的主机名。 |
| HpcClusterId | String | hpc-clusterid | ECS实例所属的EHPC集群的ID。 |
| ImageFamily | String | null | 说明该参数未开放使用。 |
| ImageId | String | centos6u5 64 20G _ _ aliaegis 2014****. _ _ vhd | 镜像文件ID，自动创建实例时使用的镜像资源。 |
| ImageName | String | centos6u5 64 20G _ _ aliaegis 2014070 _ _ 3.vhd | 镜像文件名称。 |
| InstanceDescri ption | String | FinaceDept | ECS实例的描述。 |
| InstanceGener ation | String | ecs-3 | ECS实例的系列。 |
| InstanceName | String | fortest | ECS实例的名称。 |

弹性伸缩 ESS

| InstancePatter nInfos | Array of InstancePatter nInfo |  | 智能配置的信息集合，用于筛选符合要求的实例规格范围。 |
|---|---|---|---|
| InstancePatter nInfo |  |  |  |
| Architectures | List | X86 | 实例规格所属的架构类型。可能值： X86：X86计算。 Heterogeneous：异构计算，例如GPU或 FPGA等。 BareMental：弹性裸金属服务器。 Arm：Arm计算。 SuperComputeCluster：超级计算集群。 默认值：包含所有架构类型。 |
| BurstablePerfo rmance | String | Include | 是否为性能突发实例规格。可能值： Exclude：不包含性能突发实例规格。 Include：包含性能突发实例规格。 Required：只包含性能突发实例规格。 默认值：Include。 |
| Cores | Integer | 2 | 实例规格的vCPU内核数目。 |
| ExcludedInsta nceTypes | List | ecs.n1.small/ecs.n 1.*/*7* | 需要排除的实例规格。通过使用通配符（*）可以排除单个规格或者整个规格族。例如： ecs.c6.large：表示排除ecs.c6.large实例规格。 ecs.c6.*：表示排除整个c6规格族 |
| InstanceFamil yLevel | String | EnterpriseLevel | 实例规格族级别。 EntryLevel：入门级，即共享型实例规格。成本更低，但是无法保证实例计算性能的稳定。 适用于平时CPU使用率低的业务场景。更多信息，请参见云服务器ECS文档中的共享型章节。 EnterpriseLevel：企业级。性能稳定，资源独享，适用于对稳定性要求高的业务场景。更多信息，请参见云服务器ECS文档中的实例规格族章节。 CreditEntryLevel：积分入门级，即突发性能实例。通过CPU积分来保证计算性能，适用于平时CPU使用率低、偶有突发CPU使用率的情况。更多信息，请参见云服务器ECS文档中的突发型章节。 |
| MaxPrice | Float | 2 | 说明该参数未开放使用。 |

弹性伸缩 ESS

| Memory | Float | 4 | 实例规格的内存大小，单位为GiB。 |
|---|---|---|---|
| InstanceType | String | ecs.t1.xsmall | ECS实例的实例规格。 |
| InstanceTypes | List | ecs.t1.xsmall | ECS实例的实例规格的集合。 |
| InternetCharg eType | String | PayByTraffic | 说明该参数未开放使用。 |
| InternetMaxBa ndwidthIn | Integer | 200 | 公网入带宽最大值，单位为Mbps (Mega bit per second)，可能值：1~200。 |
| InternetMaxBa ndwidthOut | Integer | 0 | 公网出带宽最大值，单位：Mbps (Mega bit per second)，可能值： 按带宽计费：0~100，如果您没有指定该参数，则出带宽将自动被设置为0 Mbps。 按流量计费：0~100，如果您没有指定该参数，则会出现报错。 |
| IoOptimized | String | none | 是否为I/O优化实例。可能值： none：非I/O优化。 optimized：I/O优化。 |
| Ipv6AddressCo unt | Integer | 1 | 为弹性网卡指定随机生成的IPv6地址数量。 |
| KeyPairName | String | fortest | 登录ECS实例时使用的密钥对的名称。 |
| LifecycleState | String | Active | 伸缩配置在伸缩组中的状态，可能值： Active：生效状态。伸缩组会使用处于生效状态的伸缩配置自动创建ECS实例。 Inacitve：失效状态。处于失效状态的伸缩配置存在于伸缩组中，但伸缩组不会使用此类伸缩配置自动创建ECS实例。 |
| LoadBalancer Weight | Integer | 1 | 后端服务器的权重，可能值：1~100。 |
| Memory | Integer | 16 | 内存大小。单位：GiB。 同时指定CPU和Memory可以定义实例规格范围，例如，CPU=2且Memory=16可以定义配置为2 vCPU和16 GiB的所有实例规格。弹性伸缩会结合IO优化、可用区等因素确定可用实例规格集合，并根据价格排序为您创建价格最低的实例。 说明该区间配置效果仅在成本优化模式下且伸缩配置未设置实例规格时生效。 |

弹性伸缩 ESS

| PasswordInher it | Boolean | true | 是否使用镜像预设的密码。 |
|---|---|---|---|
| PrivatePoolOpt ions.Id | String | eap- bp67acfmxazb4*** * | 私有池ID。即弹性保障服务ID或容量预定服务 ID。 |
| PrivatePoolOpt ions.MatchCrit eria | String | Open | 实例启动的私有池容量选项。弹性保障服务或容量预定服务在生效后会生成私有池容量，供实例启动时选择。可能值： Open：开放模式。将自动匹配开放类型的私有池容量。如果没有符合条件的私有池容量， 则使用公共池资源启动。 Target：指定模式。使用指定的私有池容量启动实例，如果该私有池容量不可用，则实例会启动失败。 None：不使用模式。实例启动将不使用私有池容量。 |
| RamRoleName | String | RamRoleTest | ECS实例的RAM角色名称。RAM角色名称由 RAM提供和维护，您可调用API ListRoles查询可用的RAM角色。创建RAM角色的方法请参见 API CreateRole。 |
| ResourceGrou pId | String | rg- resourcegroupid1 | 说明该参数未开放使用。 |
| ScalingConfigu rationId | String | asc- bp1ezrfgoyn5kijl*** * | 伸缩配置的ID。 |
| ScalingConfigu rationName | String | c1908dd1-690f- 4c9b-ab73- 350f1f06**** | 伸缩配置的名称。 |
| ScalingGroupI d | String | sg-280ih**** | 伸缩配置所属伸缩组的ID。 |
| SchedulerOpti ons | Struct |  | 调度选项。 |
| ManagedPrivat eSpaceId | String | testManagedPrivat eSpaceId | 智能全托管资源池。 |
| SecurityEnhan cementStrateg y | String | Active | 是否开启安全加固。可能值： Active：启用安全加固，只对公共镜像生效。 Deactive：不启用安全加固，对所有镜像类型生效。 |
| SecurityGroupI d | String | sg- bp18kz60mefs**** | ECS实例所属的安全组的ID，同一个安全组内的 ECS实例可以互相访问。 |

弹性伸缩 ESS

| SecurityGroupI ds | List | sg- bp18kz60mefs**** | ECS实例所属的多个安全组的ID，同一个安全组内的ECS实例可以互相访问。 |
|---|---|---|---|
| SpotDuration | Integer | 1 | 说明该参数未开放使用。 |
| SpotInterrupti onBehavior | String | Terminate | 说明该参数未开放使用。 |
| SpotPriceLimit | Array of SpotPriceMode l |  | 说明该参数未开放使用。 |
| SpotPriceMode l |  |  |  |
| InstanceType | String | ecs.t1.xsmall | 说明该参数未开放使用。 |
| PriceLimit | Float | 0.125 | 说明该参数未开放使用。 |
| SpotStrategy | String | NoSpot | 说明该参数未开放使用。 |
| SystemDisk.Bu rstingEnabled | Boolean | false | 系统盘是否开启Burst（性能突发）。可能值： true：开启。 false：未开启。 |
| SystemDisk.En cryptAlgorithm | String | AES-256 | 系统盘采用的加密算法。可能值： AES-256。 SM4-128。 默认值：AES-256。 |
| SystemDisk.En crypted | Boolean | false | 是否加密系统盘。可能值： true：加密。 false：不加密。 默认值：false。 |
| SystemDisk.K MSKeyId | String | 0e478b7a-4262- 4802-b8cb- 00d3fb40**** | 系统盘使用的KMS密钥ID。 |

弹性伸缩 ESS

| SystemDisk.Pr ovisionedIops | Long | 100 | 系统盘预配置的IOPS（Input/Output Operations Per Second）性能指标。 说明 IOPS（Input/Output Operations Per Second）指每秒能处理的I/O个数，表示块存储处理读写（输出/输入）的能力，单位为次。 |
|---|---|---|---|
| SystemDiskAu toSnapshotPoli cyId | String | sp- bp12m37ccmxvbm i5**** | 系统盘使用的自动快照策略ID。 |
| SystemDiskCa tegories | List | cloud | 系统盘的多磁盘类型。第一个磁盘类型优先级最高，其他磁盘类型的优先级依次递减。当无法使用高优先级的磁盘类型时，弹性伸缩自动尝试下一优先级的磁盘类型创建系统盘。可能值： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ |
| SystemDiskCa tegory | String | cloud | 系统盘的磁盘种类。可能值： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ ephemeral ssd：本地SSD盘。 _ |
| SystemDiskDe scription | String | TestDescription | 系统盘的描述。 |
| SystemDiskNa me | String | cloud ssd Test _ _ | 系统盘的名称。 |
| SystemDiskPer formanceLevel | String | PL1 | 说明该参数未开放使用。 |
| SystemDiskSiz e | Integer | 100 | 系统盘的磁盘大小。 |
| Tags | Array of Tag |  | 标签信息的集合。 |
| Tag |  |  |  |
| Key | String | binary | 标签键。 |
| Value | String | alterTable | 标签值。 |

弹性伸缩 ESS

| Tenancy | String | default | 是否在专有宿主机上创建实例。可能值： default：创建非专有宿主机实例。 host：创建专有宿主机实例。若您不指定 DedicatedHostId，则由阿里云自动选择专有宿主机放置实例。 |
|---|---|---|---|
| UserData | String | echo hello ecs! | ECS实例的自定义数据。 |
| WeightedCapa cities | List | 4 | 对应指定实例规格的权重，即实例规格的单台实例在伸缩组中表示的容量大小。权重越大，满足期望容量所需的本实例规格的实例数量越少。 |
| ZoneId | String | cn-hangzhou- env17-d01-g | 实例所属的可用区ID，您可以调用API DescribeZones获取可用区列表。 |
| TotalCount | Integer | 1 | 伸缩配置的总数。 |

**示例**

请求示例

```
http://ess.example.com/?Action=DescribeScalingConfigurations &RegionId=cn-qingdao-env17-d01 &PageNumber=1 &PageSize=50 &ScalingGroupId=asg-bp17pelvl720x3v7**** &ScalingConfigurationId=["asc-bp17pelvl720x5ub****"] &ScalingConfigurationName=["scalingcon****"]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <PageNumber>1</PageNumber>
      <PageSize>50</PageSize>
      <TotalCount>1</TotalCount>
      <ScalingConfigurations>
            <DeploymentSetId>ds-bp1frxuzdg87zh4p****</DeploymentSetId>
            <CreationTime>2014-08-14T10:58Z</CreationTime>
            <ScalingConfigurationName>scalingconfigura****</ScalingConfigurationName>
            <SystemDiskDescription>Test system disk.</SystemDiskDescription>
            <KeyPairName>keypair****</KeyPairName>
            <SecurityGroupId>sg-bp18kz60mefs****</SecurityGroupId>
            <PrivatePoolOptions.Id>eap-bp67acfmxazb4****</PrivatePoolOptions.Id>
            <SystemDiskAutoSnapshotPolicyId>sp-bp12m37ccmxvbmi5****
</SystemDiskAutoSnapshotPolicyId>
            <SpotStrategy>NoSpot</SpotStrategy>
            <ScalingGroupId>asg-bp17pelvl720x3v7****</ScalingGroupId>
```

弹性伸缩 ESS

```xml
            <Affinity>default</Affinity>
            <Tenancy>default</Tenancy>
            <SystemDiskSize>100</SystemDiskSize>
            <Ipv6AddressCount>1</Ipv6AddressCount>
            <SpotDuration>1</SpotDuration>
            <LifecycleState>Active</LifecycleState>
            <InstanceName>instance****</InstanceName>
            <SecurityEnhancementStrategy>Active</SecurityEnhancementStrategy>
            <UserData>echo hello ecs!</UserData>
            <PrivatePoolOptions.MatchCriteria>Open</PrivatePoolOptions.MatchCriteria>
            <DedicatedHostId>dh-bp67acfmxazb4p****</DedicatedHostId>
            <InstanceGeneration>ecs-3</InstanceGeneration>
            <HpcClusterId>hpc-clus****</HpcClusterId>
            <PasswordInherit>true</PasswordInherit>
            <Memory>16</Memory>
            <ImageId>centos6u5_64_20G_aliaegis_2014****.vhd</ImageId>
            <ImageFamily>hangzhou-daily-update</ImageFamily>
            <LoadBalancerWeight>1</LoadBalancerWeight>
            <SystemDiskCategory>cloud</SystemDiskCategory>
            <HostName>LocalHost</HostName>
            <SystemDiskName>cloud_ssd_Test</SystemDiskName>
            <InternetMaxBandwidthOut>0</InternetMaxBandwidthOut>
            <InternetMaxBandwidthIn>200</InternetMaxBandwidthIn>
            <InstanceType>ecs.g6.large</InstanceType>
            <InstanceDescription>FinanceDept</InstanceDescription>
            <IoOptimized>none</IoOptimized>
            <RamRoleName>ramrole****</RamRoleName>
            <SystemDiskPerformanceLevel>PL1</SystemDiskPerformanceLevel>
            <Cpu>2</Cpu>
            <ResourceGroupId>rg-aekzn2ou7xo****</ResourceGroupId>
            <ZoneId>cn-hangzhou-g</ZoneId>
            <InternetChargeType>PayByTraffic</InternetChargeType>
            <ImageName>centos6u5_64_20G_aliaegis_20140703.vhd</ImageName>
            <ScalingConfigurationId>asc-bp1ezrfgoyn5kijl****</ScalingConfigurationId>
            <CreditSpecification>Standard</CreditSpecification>
            <SpotInterruptionBehavior>Terminate</SpotInterruptionBehavior>
            <DataDisks>
                  <PerformanceLevel>PL1</PerformanceLevel>
                  <Description>FinanceDept</Description>
                  <SnapshotId>s-23f2i****</SnapshotId>
                  <Device>/dev/xvdb</Device>
                  <Size>200</Size>
                  <DiskName>cloud_ssdData</DiskName>
                  <AutoSnapshotPolicyId>sp-bp19nq9enxqkomib****</AutoSnapshotPolicyId>
                  <Category>cloud</Category>
                  <KMSKeyId>0e478b7a-4262-4802-b8cb-00d3fb40****</KMSKeyId>
                  <DeleteWithInstance>true</DeleteWithInstance>
                  <Encrypted>false</Encrypted>
                  <Categories>cloud_essd</Categories>
                  <ProvisionedIops>100</ProvisionedIops>
                  <BurstingEnabled>false</BurstingEnabled>
            </DataDisks>
            <Tags>
                  <Key>binary</Key>
```

/ 弹性伸缩 ESS

```xml
                  <Value>alterTable</Value>
            </Tags>
            <SpotPriceLimit>
                  <InstanceType>ecs.g6.large</InstanceType>
                  <PriceLimit>0.125</PriceLimit>
            </SpotPriceLimit>
            <InstancePatternInfos>
                  <MaxPrice>2</MaxPrice>
                  <Cores>2</Cores>
                  <Memory>4</Memory>
                  <InstanceFamilyLevel>EnterpriseLevel</InstanceFamilyLevel>
                  <Architectures>X86</Architectures>
                  <BurstablePerformance>Include</BurstablePerformance>
                  <ExcludedInstanceTypes>ecs.n1.small/ecs.n1.*/*7*
</ExcludedInstanceTypes>
            </InstancePatternInfos>
            <SystemDiskCategories>cloud</SystemDiskCategories>
            <WeightedCapacities>4</WeightedCapacities>
            <SecurityGroupIds>sg-bp18kz60mefs****</SecurityGroupIds>
            <SchedulerOptions>
<ManagedPrivateSpaceId>testManagedPrivateSpaceId</ManagedPrivateSpaceId>
            </SchedulerOptions>
            <SystemDisk.Encrypted>false</SystemDisk.Encrypted>
            <SystemDisk.KMSKeyId>0e478b7a-4262-4802-b8cb-00d3fb40****
</SystemDisk.KMSKeyId>
            <SystemDisk.EncryptAlgorithm>AES-256</SystemDisk.EncryptAlgorithm>
            <SystemDisk.ProvisionedIops>100</SystemDisk.ProvisionedIops>
            <SystemDisk.BurstingEnabled>false</SystemDisk.BurstingEnabled>
      </ScalingConfigurations>
```

`JSON` 格式

```json
{
        "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
        "PageNumber": 1,
        "PageSize": 50,
        "TotalCount": 1,
        "ScalingConfigurations": {
            "DeploymentSetId": "ds-bp1frxuzdg87zh4p****",
            "CreationTime": "2014-08-14T10:58Z",
            "ScalingConfigurationName": "scalingconfigura****",
            "SystemDiskDescription": "Test system disk.",
            "KeyPairName": "keypair****",
            "SecurityGroupId": "sg-bp18kz60mefs****",
            "PrivatePoolOptions.Id": "eap-bp67acfmxazb4****",
            "SystemDiskAutoSnapshotPolicyId": "sp-bp12m37ccmxvbmi5****",
            "ScalingGroupId": "asg-bp17pelvl720x3v7****",
            "Affinity": "default",
            "Tenancy": "default",
            "SystemDiskSize": 100,
            "Ipv6AddressCount": 1,
```

弹性伸缩 ESS

```json
            "LifecycleState": "Active",
            "InstanceName": "instance****",
            "SecurityEnhancementStrategy": "Active",
            "UserData": "echo hello ecs!",
            "PrivatePoolOptions.MatchCriteria": "Open",
            "DedicatedHostId": "dh-bp67acfmxazb4p****",
            "InstanceGeneration": "ecs-3",
            "HpcClusterId": "hpc-clus****",
            "PasswordInherit": true,
            "Memory": 16,
            "ImageId": "centos6u5_64_20G_aliaegis_2014****.vhd",
            "ImageFamily": "hangzhou-daily-update",
            "LoadBalancerWeight": 1,
            "SystemDiskCategory": "cloud",
            "HostName": "LocalHost",
            "SystemDiskName": "cloud_ssd_Test",
            "InternetMaxBandwidthOut": 0,
            "InternetMaxBandwidthIn": 200,
            "InstanceType": "ecs.g6.large",
            "InstanceDescription": "FinanceDept",
            "IoOptimized": "none",
            "RamRoleName": "ramrole****",
            "SystemDiskPerformanceLevel": "PL1",
            "Cpu": 2,
            "ResourceGroupId": "rg-aekzn2ou7xo****",
            "ZoneId": "cn-hangzhou-g",
            "InternetChargeType": "PayByTraffic",
            "ImageName": "centos6u5_64_20G_aliaegis_20140703.vhd",
            "ScalingConfigurationId": "asc-bp1ezrfgoyn5kijl****",
            "CreditSpecification": "Standard",
            "SpotInterruptionBehavior": "Terminate",
            "DataDisks": {
                "PerformanceLevel": "PL1",
                "Description": "FinanceDept",
                "SnapshotId": "s-23f2i****",
                "Device": "/dev/xvdb",
                "Size": 200,
                "DiskName": "cloud_ssdData",
                "AutoSnapshotPolicyId": "sp-bp19nq9enxqkomib****",
                "Category": "cloud",
                "KMSKeyId": "0e478b7a-4262-4802-b8cb-00d3fb40****",
                "DeleteWithInstance": true,
                "Encrypted": false,
                "Categories": "cloud_essd",
                "ProvisionedIops": 100,
                "BurstingEnabled": false
            },
            "Tags": {
                "Key": "binary",
                "Value": "alterTable"
            },
            "SpotPriceLimit": {
                "InstanceType": "ecs.g6.large",
                "PriceLimit": 0.125
```

弹性伸缩 ESS

```json
            },
            "InstancePatternInfos": {
                "MaxPrice": 2,
                "Cores": 2,
                "Memory": 4,
                "InstanceFamilyLevel": "EnterpriseLevel",
                "Architectures": "X86",
                "BurstablePerformance": "Include",
                "ExcludedInstanceTypes": "ecs.n1.small/ecs.n1.*/*7*"
            },
            "SystemDiskCategories": "cloud",
            "WeightedCapacities": 4,
            "SecurityGroupIds": "sg-bp18kz60mefs****",
            "SchedulerOptions": {
                "ManagedPrivateSpaceId": "testManagedPrivateSpaceId"
            },
            "SystemDisk.Encrypted": false,
            "SystemDisk.KMSKeyId": "0e478b7a-4262-4802-b8cb-00d3fb40****",
            "SystemDisk.EncryptAlgorithm": "AES-256",
            "SystemDisk.ProvisionedIops": 100,
            "SystemDisk.BurstingEnabled": false
        }
    }
}
```

#### ModifyScalingConfiguration

**接口说明**

如果修改伸缩配置的名称，请注意同一伸缩组下不能存在名称相同的伸缩配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyScalingCo nfiguration | 系统规定参数，取值： ModifyScalingConfiguration。 |
| ScalingConfigura tionId | String | 是 | asc- bp16har3jpj6fjb x**** | 待修改伸缩配置的ID。 |
| IoOptimized | String | 否 | none | 是否为I/O优化实例。取值范围： none：非I/O优化实例。 optimized：I/O优化实例。 |

弹性伸缩 ESS

| ScalingConfigura tionName | String | 否 | test-modify | 伸缩配置的名称，2~64个英文或中文字符，以数字、大小写字母或中文开头，可包含数字、下划线（ ）、短划线（-）或 _ 半角句号（.）。 在同一地域下同一伸缩组内伸缩配置名称唯一。如果您没有指定该参数，则默认使用伸缩配置的ID。 |
|---|---|---|---|---|
| InstanceName | String | 否 | inst**** | 使用本伸缩配置自动创建的ECS实例的名称。 |
| HostName | String | 否 | hos**** | 云服务器ECS的主机名。半角句号（.）或短划线（-）不能作为首尾字符，不能连续使用半角句号（.）或短划线（-）。另外， 不同类型实例的命名要求如下： Windows实例：主机名长度为2~15个字符，可以包含大小写字母、数字和短划线（-）。不能包含半角句号（.）， 不能全是数字。 其他类型实例（Linux等）：主机名长度为2~64个字符，可以包含多个半角句号（.）。两个半角句号（.）之间为一段，每段可以包含大小写字母、数字和短划线（-）。 |
| ImageId | String | 否 | centos6u5 64 2 _ _ 0G aliaegis 201 _ _ 4****.vhd | 镜像文件ID，自动创建实例时使用的镜像资源。 说明如果伸缩配置之前使用的镜像包括系统盘和数据盘，修改此镜像后，原数据盘信息会被清除。 |
| ImageName | String | 否 | suse11sp3 64 2 _ _ 0G aliaegis 201 _ _ 5****.vhd | 镜像文件名称，同一个地域内镜像名称唯一。如果设置了ImageId，ImageName 将被忽略。 不支持通过ImageName设置镜像市场镜像。 |
| Cpu | Integer | 否 | 2 | vCPU个数。单位：核。 同时指定CPU和Memory可以定义实例规格范围，例如，CPU=2且Memory=16可以定义配置为2 vCPU和16 GiB的所有实例规格。弹性伸缩会结合I/O优化、可用区等因素确定可用实例规格集合，并根据价格排序为您创建价格最低的实例。 说明该区间配置效果仅在成本优化模式下且伸缩配置未设置实例规格时生效。 |

弹性伸缩 ESS

| Memory | Integer | 否 | 16 | 内存大小。单位：GiB。 同时指定CPU和Memory可以定义实例规格范围，例如，CPU=2且Memory=16可以定义配置为2 vCPU和16 GiB的所有实例规格。弹性伸缩会结合I/O优化、可用区等因素确定可用实例规格集合，并根据价格排序为您创建价格最低的实例。 说明该区间配置效果仅在成本优化模式下且伸缩配置未设置实例规格时生效。 |
|---|---|---|---|---|
| InternetMaxBan dwidthOut | Integer | 否 | 50 | 公网出带宽最大值，单位为Mbps (Mega bit per second)，取值范围： 按带宽计费：0~100，如果您没有指定该参数，则出带宽将自动被设置为0 Mbps。 按流量计费：0~100，如果您没有指定该参数，则会出现报错。 |
| SystemDisk.Cate gory | String | 否 | cloud efficiency _ | 系统盘的磁盘种类。取值范围： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ ephemeral ssd：本地SSD盘。 _ 该参数不能与 SystemDiskCategories.N 同时指定。当该参数与 SystemDiskCategories.N 都未指定时，该参数有默认值。InstanceType 为系列I的实例规格且实例属于非I/O优化实例时，默认值：cloud。否则，默认值： cloud efficiency。 _ |
| SystemDisk.Size | Integer | 否 | 50 | 系统盘的大小，单位：GiB。取值范围： cloud：20~500。 cloud efficiency：20~500。 _ cloud ssd：20~500。 _ ephemeral ssd：20~500。 _ 指定该参数后，系统盘大小必须大于等于 max{20, ImageSize}。 |
| SystemDisk.Disk Name | String | 否 | cloud ssdSyste _ m | 系统盘的名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 和 https:// 开头。 可以包含数字、半角冒号（:）、下划线 （ ）或者短划线（-）。 _ |

弹性伸缩 ESS

| SystemDisk.Des cription | String | 否 | Test system disk. | 系统盘的描述。长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。 |
|---|---|---|---|---|
| SystemDisk.Auto SnapshotPolicyId | String | 否 | sp- bp12m37ccmxv bmi5**** | 系统盘使用的自动快照策略ID。 |
| LoadBalancerWe ight | Integer | 否 | 50 | 后端服务器的权重，取值范围：1~100。 |
| UserData | String | 否 | echo hello ecs! | ECS实例的自定义数据，需要以Base64方式编码，编码前的原始数据最多为16 KB。 |
| KeyPairName | String | 否 | KeyPair Name _ | 登录ECS实例时使用的密钥对的名称。 对Windows实例，该参数将被忽略，默认为空。 对Linux实例，密码登录方式会被初始化成禁止。 |
| RamRoleName | String | 否 | RamRoleTest | ECS实例的RAM角色名称。RAM角色名称由RAM提供和维护，您可调用API ListRoles 查询可用的RAM角色。创建RAM角色的方法请参见API CreateRole 。 |
| PasswordInherit | Boolean | 否 | false | 是否使用镜像预设的密码。使用该参数时，您需要确保使用的镜像已经设置了密码。 |
| Tags | String | 否 | {"key1":"value1 ","key2":"value2 ", ... "key5":"value5" } | ECS实例的标签。标签以键值对方式传入，最多可以使用20组标签。Key和 Value的使用要求如下： Key最多支持64个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。一旦使用标签，Key 不允许为空字符串。 Value最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。Value可以为空字符串。 |
| DeploymentSetI d | String | 否 | ds- bp13v7bjnj9gis* *** | ECS实例所属的部署集的ID。 |
| SecurityGroupId | String | 否 | sg-F876F**** | ECS实例所属的安全组的ID，同一个安全组内的ECS实例可以互相访问。 |

|  |  | acs: |
|---|---|---|
|  | http:// |  |
| https:// |  |  |

|  |  | acs: |
|---|---|---|
|  | http:// |  |
| https:// |  |  |

弹性伸缩 ESS

| Override | Boolean | 否 | true | 是否覆盖。取值范围： true：覆盖。 false：不覆盖。 |
|---|---|---|---|---|
| HpcClusterId | String | 否 | hpc-clusterid | ECS实例所属的HPC集群的ID。 |
| InstanceDescript ion | String | 否 | Test instance. | ECS实例的描述。长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。 |
| Ipv6AddressCou nt | Integer | 否 | 1 | 为弹性网卡指定随机生成的IPv6地址数量。 |
| CreditSpecificati on | String | 否 | Standard | 修改突发性能实例的运行模式。取值范围： Standard：标准模式，实例性能请参见云服务器ECS文档中突发性能实例概述下的性能约束模式。 Unlimited：无性能约束模式，实例性能请参见云服务器ECS文档中突发性能实例概述下的无性能约束模式。 |
| ImageFamily | String | 否 | hangzhou-daily- update | 镜像族系名称，通过设置该参数来获取当前镜像族系内最新可用的自定义镜像，用于创建实例。如果已经设置了参数 ImageId，则不能设置该参数。 |
| ZoneIdInvalid | String | 否 | cn-hangzhou-g | ECS实例所属的可用区ID。 |
| DedicatedHostId | String | 否 | dh- bp67acfmxazb4 p**** | 是否在专有宿主机上创建ECS实例。 您可以调用 DescribeDedicatedHosts 接口查询专有宿主机ID列表。 |
| Affinity | String | 否 | default | 专有宿主机实例是否与专有宿主机关联。 取值范围： default：实例不与专有宿主机关联。已启用节省停机模式的实例，停机后再次启动时，若原专有宿主机可用资源不足，则实例被放置在自动部署资源池的其它专有宿主机上。 host：实例与专有宿主机关联。已启用节省停机模式的实例，停机后再次启动时，仍放置在原专有宿主机上。若原专有宿主机可用资源不足，则实例重启失败。 |

弹性伸缩 ESS

| Tenancy | String | 否 | default | 是否在专有宿主机上创建实例。取值范围： default：创建非专有宿主机实例。 host：创建专有宿主机实例。若您不指定 DedicatedHostId ，则由阿里云自动选择专有宿主机放置实例。 |
|---|---|---|---|---|
| PrivatePoolOptio ns.MatchCriteria | String | 否 | Open | 实例启动的私有池容量选项。弹性保障服务或容量预定服务在生效后会生成私有池容量，供实例启动时选择。取值范围： Open：开放模式。将自动匹配开放类型的私有池容量。如果没有符合条件的私有池容量，则使用公共池资源启动。 该模式下无需设置 PrivatePoolOptions.Id参数。 Target：指定模式。使用指定的私有池容量启动实例，如果该私有池容量不可用，则实例会启动失败。该模式下必须指定私有池ID，即 PrivatePoolOptions.Id参数为必填项。 None：不使用模式。实例启动将不使用私有池容量。 |
| PrivatePoolOptio ns.Id | String | 否 | eap- bp67acfmxazb4 **** | 私有池ID。即弹性保障服务ID或容量预定服务ID。 |
| SystemDisk.Encr ypted | Boolean | 否 | false | 是否加密系统盘。取值范围： true：加密。 false：不加密。 默认值：false。 |
| SystemDisk.KMS KeyId | String | 否 | 0e478b7a-4262- 4802-b8cb- 00d3fb40**** | 系统盘使用的KMS密钥ID。 |
| SystemDisk.Encr yptAlgorithm | String | 否 | AES-256 | 系统盘采用的加密算法。取值范围： AES-256。 SM4-128。 默认值：AES-256。 |
| DataDisk.N.Auto SnapshotPolicyId | String | 否 | sp- bp19nq9enxqko mib**** | 数据盘使用的自动快照策略ID，N的取值范围：1~16。 |
| DataDisk.N.Encr ypted | String | 否 | false | 数据盘N是否加密，N的取值范围： 1~16。该参数取值范围： true：加密。 false：不加密。 |

弹性伸缩 ESS

| DataDisk.N.Desc ription | String | 否 | Test data disk. | 数据盘的描述，N的取值范围：1~16。长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。 |
|---|---|---|---|---|
| DataDisk.N.Snap shotId | String | 否 | s-snapshot**** | 创建数据盘时使用的快照，N的取值范围： 1~16。指定该参数后，DataDisk.N.Size 会被忽略，实际创建的磁盘大小为指定快照的大小。 如果该快照创建于2013年7月15日或之前，调用会被拒绝，返回参数中会提示 InvalidSnapshot.TooOld。 |
| DataDisk.N.Cate gories.N | RepeatL ist | 否 | cloud | 数据盘N的多磁盘类型。第一个N表示第N 块数据盘，取值范围：1~16。第二个N表示第N块数据盘的第N种磁盘类型，取值范围：1~4，即一个伸缩配置内最多可以为数据盘指定4种磁盘类型。N越小，优先级越高。当无法使用高优先级的磁盘类型时，弹性伸缩自动尝试下一优先级的磁盘类型创建数据盘。取值范围： cloud：普通云盘。随实例创建的普通云盘的 DeleteWithInstance 属性为true。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ |
| DataDisk.N.Size | Integer | 否 | 100 | 数据盘N的磁盘大小，N的取值范围： 1~16，内存单位为GiB。取值范围： cloud：5~2000。 cloud efficiency：20~32768。 _ cloud ssd：20~32768。 _ ephemeral ssd：5~800。 _ 指定该参数后，磁盘大小必须大于等于快照大小（快照通过SnapshotId指定）。 |
| DataDisk.N.Devi ce | String | 否 | /dev/xvdb | 数据盘挂载点，N的取值范围：1~16。如果您没有指定该参数，则默认在自动创建 ECS实例时由系统分配，从/dev/xvdb开始，到/dev/xvdz结束。 |
| DataDisk.N.Disk Name | String | 否 | cloud ssdData _ | 数据盘的名称，N的取值范围：1~16。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 和 https:// 开头。可以包含数字、半角冒号（:）、下划线 （ ）或者短划线（-）。 _ |

弹性伸缩 ESS

| DataDisk.N.Cate gory | String | 否 | cloud ssd _ | 数据盘N的磁盘种类，N的取值范围： 1~16。该参数取值范围： cloud：普通云盘。随实例创建的普通云盘的 DeleteWithInstance 属性为true。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ ephemeral ssd：本地SSD盘。 _ 该参数不能与 DataDisk.N.Categories.N 同时指定。当该参数与 DataDisk.N.Categories.N 都未指定时，该参数的默认值为： 对于I/O优化实例，默认值为 cloud efficiency。 _ 对于非I/O优化实例，默认值为cloud。 |
|---|---|---|---|---|
| DataDisk.N.Dele teWithInstance | Boolean | 否 | true | 指定数据盘是否随实例释放，N的取值范围：1~16。该参数取值范围： true：释放实例时，该磁盘随实例一起释放。 false：释放实例时，该磁盘保留不释放。 该参数只可对独立云盘设置 （DataDisk.N.Category为cloud、 cloud efficiency、cloud ssd），否则 _ _ 会出现报错。 |
| DataDisk.N.KMS KeyId | String | 否 | 0e478b7a-4262- 4802-b8cb- 00d3fb40**** | 数据盘对应的KMS密钥的ID，N的取值范围：1~16。 |
| InstanceTypes.N | RepeatL ist | 否 | ecs.g6.large | 多实例规格参数。如果使用了 InstanceTypes.N，InstanceType将被忽略，其中N的取值范围：1~10，即一个伸缩配置内最多可以设置10种实例规格。 N代表当前伸缩配置中实例规格的优先级， 编号为1的实例规格优先级最高，实例规格优先级随着编号的增大依次降低。当无法根据优先级较高的实例规格创建出实例时，弹性伸缩服务会自动选择下一优先级的实例规格来创建实例。 |

弹性伸缩 ESS

| InstanceTypeOv erride.N.Instanc eType | String |  |  |  | 当您需要指定伸缩配置中实例规格的容量时，请同时指定本参数和 InstanceTypeOverride.N.Weight edCapacity 。 本参数用于指定实例规格。您可以指定N个本参数，结合 InstanceTypeOverride.N.Weight edCapacity 参数，扩展多实例规格支持自定义权重。N的取值范围：1~10。 说明指定本参数时，不允许同时指定 InstanceTypes 。 InstanceType的取值范围：在售的ECS实例规格，请参见云服务器ECS中的实例规格族章节。 |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | InstanceTypeOverride.N.Weight |  |
|  |  |  |  |  | edCapacity |  |  |
|  |  |  |  |  |  | InstanceTypeOverride.N.Weight |  |
|  |  |  |  |  | edCapacity |  |  |
|  |  |  | 否 | ecs.c5.xlarge |  |  |  |
| InstanceTypeOv erride.N.Weighte dCapacity | Integer |  |  |  | 当您需要指定伸缩配置中实例规格的容量时，在指定 InstanceTypeOverride.N.Instan ceType 后，再指定本参数。两个参数一一对应，N需要保持一致。 本参数用于指定实例规格的权重，即实例规格的单台实例在伸缩组中表示的容量大小。权重越大，满足期望容量所需的本实例规格的实例数量越少。 由于每个实例规格的vCPU个数、内存大小等性能指标会有差异，您可以根据自身需求，给不同的实例规格配置不同的权重。 例如： 当前容量：0。 期望容量：6。 ecs.c5.xlarge规格容量：4。 为满足期望容量，伸缩组将为用户扩容2台 ecs.c5.xlarge实例。 说明扩容时伸缩组的容量不得超过最大容量（MaxSize）与实例规格的最大权重之和。 WeightedCapacity的取值范围： 1~500。 |  |  |
|  |  |  |  |  |  | InstanceTypeOverride.N.Instan |  |
|  |  |  |  |  | ceType |  |  |
|  |  |  | 否 | 4 |  |  |  |
| SecurityGroupId s.N | RepeatL ist |  | 否 | sg- bp18kz60mefs** ** | 所属安全组ID。 |  |  |

弹性伸缩 ESS

| InstancePatternI nfo.N.Cores | Integer | 否 | 2 | 智能配置模式下，实例规格的vCPU内核数目，用于筛选符合要求的实例规格范围。 更多信息，请参见云服务器ECS中的实例规格族章节。N的取值范围：1~10。 请注意以下信息： InstancePatternInfo.N参数仅适用于伸缩组的网络类型为专有网络。 InstancePatternInfo.N参数必须同时配置InstancePatternInfo.N.Cores和 InstancePatternInfo.N.Memory。 如果您已经通过InstanceType或 InstanceTypes.N参数指定了实例规格，弹性伸缩优先使用您指定的实例规格扩容，当指定的实例规格无库存时， 再从符合InstancePatternInfo.N参数值的实例规格中优先使用价格最低的实例规格扩容。 |
|---|---|---|---|---|
| InstancePatternI nfo.N.InstanceFa milyLevel | String | 否 | EnterpriseLevel | 智能配置模式下，实例规格族级别，用于筛选符合要求的实例规格范围。取值范围： EntryLevel：入门级，即共享型实例规格。成本更低，但是无法保证实例计算性能的稳定。适用于平时CPU使用率低的业务场景。更多信息，请参见云服务器ECS中的共享型章节。 EnterpriseLevel：企业级。性能稳定，资源独享，适用于对稳定性要求高的业务场景。更多信息，请参见云服务器ECS中的实例规格族章节。 CreditEntryLevel：积分入门级，即突发性能实例。通过CPU积分来保证计算性能，适用于平时CPU使用率低、偶有突发CPU使用率的情况。更多信息，请参见云服务器ECS中的突发性能实例章节。 N的取值范围：1~10。 |
| InstancePatternI nfo.N.MaxPrice | Float | 否 | 2 | 智能配置模式下，按量付费实例或者抢占式实例可接受的每小时最高价格，用于筛选符合要求的实例规格范围。N的取值范围：1~10。 |
| InstancePatternI nfo.N.Memory | Float | 否 | 4 | 智能配置模式下，实例规格的内存大小， 单位为GiB，用于筛选符合要求的实例规格范围。更多信息，请参见云服务器ECS中的实例规格族章节。N的取值范围： 1~10。 |

弹性伸缩 ESS

| SystemDiskCate gories.N | RepeatL ist | 否 | cloud | 系统盘的多磁盘类型。N的取值范围： 1~4，即一个伸缩配置内最多可以为系统盘指定4种磁盘类型。N越小，优先级越高。当无法使用高优先级的磁盘类型时， 弹性伸缩自动尝试下一优先级的磁盘类型创建系统盘。取值范围： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=ModifyScalingConfiguration &ScalingConfigurationId=asc-bp16har3jpj6fjbx**** &IoOptimized=none &ScalingConfigurationName=test-modify &InstanceName=inst**** &HostName=hos**** &ImageId=centos6u5_64_20G_aliaegis_2014****.vhd &ImageName=suse11sp3_64_20G_aliaegis_2015****.vhd &Cpu=2 &Memory=16 &InternetChargeType=PayByBandwidth &InternetMaxBandwidthOut=50 &SystemDisk.Category=cloud_efficiency &SystemDisk.Size=50 &SystemDisk.DiskName=cloud_ssdSystem &SystemDisk.Description=Test system disk. &SystemDisk.AutoSnapshotPolicyId=sp-bp12m37ccmxvbmi5**** &SystemDisk.PerformanceLevel=PL0 &LoadBalancerWeight=50 &UserData=echo hello ecs! &KeyPairName=KeyPair_Name &RamRoleName=RamRoleTest &PasswordInherit=false &Tags={"key1":"value1","key2":"value2", ... "key5":"value5"} &DeploymentSetId=ds-bp13v7bjnj9gis**** &SecurityGroupId=sg-F876F**** &Override=true &HpcClusterId=hpc-clusterid &InstanceDescription=Test instance. &Ipv6AddressCount=1 &CreditSpecification=Standard &ImageFamily=hangzhou-daily-update
```

弹性伸缩 ESS

```json
&ZoneId=cn-hangzhou-g &DedicatedHostId=dh-bp67acfmxazb4p**** &Affinity=default &Tenancy=default &PrivatePoolOptions.MatchCriteria=Open &PrivatePoolOptions.Id=eap-bp67acfmxazb4**** &DataDisk=[{"PerformanceLevel":"PL1","AutoSnapshotPolicyId":"spbp19nq9enxqkomib****","Encrypted":"false","Description":"Test data disk.","SnapshotId":"s-snapshot****","Categories": ["cloud"],"Size":100,"Device":"/dev/xvdb","DiskName":"cloud_ssdData","Category":"cloud_ss ,"DeleteWithInstance":true,"KMSKeyId":"0e478b7a-4262-4802-b8cb- 00d3fb40****","ProvisionedIops":100,"BurstingEnabled":false}] &InstanceTypes=["ecs.g6.large"] &InstanceTypeOverride=[{"InstanceType":"ecs.c5.xlarge","WeightedCapacity":4}] &SecurityGroupIds=["sg-bp18kz60mefs****"] &InstancePatternInfo= [{"Cores":2,"InstanceFamilyLevel":"EnterpriseLevel","MaxPrice":2.0,"Memory":4.0,"Architec re":["X86"],"BurstablePerformance":"Include","ExcludedInstanceType": ["ecs.n1.small/ecs.n1.*/*7*"]}] &SystemDiskCategories=["cloud"] &SystemDisk.Encrypted=false &SystemDisk.KMSKeyId=0e478b7a-4262-4802-b8cb-00d3fb40**** &SystemDisk.EncryptAlgorithm=AES-256 &SystemDisk.ProvisionedIops=100 &SystemDisk.BurstingEnabled=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "requestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 未授权操作当前Action。 |

弹性伸缩 ESS

| 404 | InvalidDataDiskSnapsh otId.NotFound | Snapshot "XXX" does not exist. | 不存在指定的快照。 |
|---|---|---|---|
| 400 | InvalidDataDiskSnapsh otId.SizeNotSupported | The capacity of snapshot "XXX" exceeds the size limit of the specified disk category. | 指定快照的大小超过了磁盘大小的限制。 |
| 404 | InvalidImageId.NotFou nd | The specified image does not exist. | 指定的镜像不存在。 |
| 400 | InvalidKeyPairName.N otFound | The specified KeyPairName does not exist in our records. | 指定的KeyPairName不存在。 |
| 400 | InvalidNetworkType.Fo rRAMRole | RAMRole can't be used For classic instance. | 经典网络实例不支持 RamRoleName参数。 |
| 400 | InvalidParamter | The specified value of parameter is not valid. | 指定的参数值无效。 |
| 400 | InvalidScalingConfigur ationName.Duplicate | The specified value of parameter is duplicated. | 伸缩配置名已存在。 |
| 400 | InvalidSecurityGroupId .IncorrectNetworkType | The network type of specified Security Group does not support this action. | 指定的安全组与伸缩组指定网络类型不一致。 |
| 400 | InvalidSecurityGroupId .VPCMismatch | The specified security group and the specified virtual switch are not in the same VPC. | 指定的安全组和虚拟交换机不属于同一个虚拟专有网络。 |
| 400 | InvalidTags.KeyValue | The specified tags key/value cannot be empty. | 必须指定Tags参数。 |
| 400 | InvalidTags.ListSize | The specified tags list size cannot be more than "5". | Tags列表长度超过限制长度。 |

弹性伸缩 ESS

| 400 | InvalidUserData.Base6 4FormatInvalid | The specified parameter UserData must be base64 encoded. | UserData不符合Base64 编码规范。 |
|---|---|---|---|
| 400 | InvalidUserData.SizeEx ceeded | The specified parameter UserData exceeds the size. | 指定的UserData过长。 |

#### DeleteScalingConfiguration

**接口说明**

以下情况不能删除伸缩配置： 伸缩配置在伸缩组中处于生效状态。 伸缩组中仍然存在使用该伸缩配置创建的ECS实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteScalingCo nfiguration | 系统规定参数，取值： DeleteScalingConfiguration。 |
| ScalingConfigura tionId | String | 是 | eOs27Kb0oXvQc UYjEGel**** | 待删除伸缩配置的ID。您可以调用 DescribeScalingConfigurations参数查询伸缩配置的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。无论调用接口成功与否，都会返回请求 ID。 |

**示例**

请求示例

```
http://ess.example.com/?Action=DeleteScalingConfiguration &ScalingConfigurationId=eOs27Kb0oXvQcUYjEGel****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingConfigur ationId.NotFound | The specified scaling configuration does not exist. | 指定的伸缩配置在该账号下不存在。 |
| 400 | IncorrectScalingConfig urationLifecycleState | The current lifecycle state of specified scaling configuration does not support this action. | 指定的伸缩配置未处于 Inactive状态。 |
| 400 | InstanceInUse | You cannot delete a scaling configuration or scaling group while there is an instance associated with it. | 指定的伸缩配置还有关联的ECS实例未被删除。 |

#### CreateEciScalingConfiguration

调用CreateEciScalingConfiguration创建一个ECI类型的伸缩配置。

**接口说明**

伸缩配置用来指定弹性扩张时使用的ECI实例模板。 参数Cpu和Memory用于指定CPU和内存定义实例规格的范围，弹性伸缩会结合IO优化、可用区等因素确定可用实例规格集合，并根据价格排序为您创建价格最低的实例。该方式仅适用于伸缩组的扩缩容策略为成本优化策略，且伸缩配置未指定实例规格的场景。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateEciScaling Configuration | 系统规定参数。取值： CreateEciScalingConfiguration。 |
| ContainerGroup Name | String | 是 | nginx-test | ECI实例名称，即容器组名称。 |

弹性伸缩 ESS

| ScalingConfigura tionName | String | 是 | scalingconfig*** * | 伸缩配置的名称。长度为2~64个英文或中文字符组成，以数字、大小写字母或中文开头，可包含数字、下划线（ ）、短划线 _ （-）或半角句号（.）。 在同一地域下同一伸缩组内伸缩配置名称唯一。如果您没有指定该参数，则默认使用伸缩配置的ID。 |
|---|---|---|---|---|
| ScalingGroupId | String | 是 | asg- bp14wlu85wrpc hm0**** | 伸缩配置所属的伸缩组的ID。 |
| SecurityGroupId | String | 是 | sg- uf66jeqopgqa9h dn**** | ECI实例所属的安全组ID。同一个安全组内的ECI实例之间可以互相访问。 如果没有指定安全组，系统将自动使用您选择的地域下的默认安全组，您需要确保该安全组的入方向规则中包含容器需要暴露的协议和端口。 如果您在该地域下没有默认安全组，系统将自动创建一个默认安全组，并将您声明的容器协议和端口添加到该安全组的入方向规则中。 |
| RestartPolicy | String | 否 | Always | ECI实例重启策略。取值范围： Always：总是重启。 Never：从不重启。 OnFailure：失败时重启。 默认值：Always。 |
| Cpu | Float | 否 | 1.0 | 实例级别vCPU大小。单位：核。 |
| Memory | Float | 否 | 2.0 | 实例级别内存大小。单位：GiB。 |
| DnsPolicy | String | 否 | Default | DNS策略。取值范围： None：使用DnsConfig字段设置的 DNS。 Default：继承运行环境的DNS设置。 |
| ImageSnapshotI d | String | 否 | imc- 2zebxkiifuyzzlhl* *** | 镜像缓存ID。 |
| RamRoleName | String | 否 | RamTestRole | 实例RAM角色名称。其中，ECI与ECS共用实例RAM角色，更多信息，请参见通过云服务器ECS中的API使用实例RAM角色章节。 |
| TerminationGrac ePeriodSeconds | Long | 否 | 60 | 程序的缓冲时间，用于处理关闭之前的操作。 |

| 弹性伸缩 ESS |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|

| AutoMatchImage Cache | Boolean | 否 | false | 是否自动匹配镜像缓存。取值范围： true：是。 false：否。 默认值：false。 |
|---|---|---|---|---|
| Ipv6AddressCou nt | Integer | 否 | 1 | IPv6地址数。固定为1，即一个ECI实例支持绑定一个IPv6地址。 |
| ActiveDeadlineS econds | Long | 否 | 1000 | 有效期限。单位为秒。 |
| AutoCreateEip | Boolean | 否 | true | 是否自动创建弹性公网IP，并绑定ECI实例。 |
| EipBandwidth | Integer | 否 | 5 | 弹性公网IP的带宽。 默认值：5 Mbit/s。 |
| HostName | String | 否 | test | 主机名称，即容器组名称。 |
| IngressBandwidt h | Long | 否 | 1024000 | 入方向带宽限制。单位：Byte。 |
| EgressBandwidt h | Long | 否 | 1024000 | 出方向带宽限制。单位：Byte。 |
| CpuOptionsCore | Integer | 否 | 2 | CPU物理核心数。仅部分规格支持自定义设置。更多信息，请参见弹性容器实例中的自定义CPU选项章节。 |
| CpuOptionsThre adsPerCore | Integer | 否 | 2 | 每核线程数。仅部分规格支持自定义设置。配置为1时表示关闭超线程。更多信息，请参见弹性容器实例中的自定义CPU 选项章节。 |
| EphemeralStora ge | Integer | 否 | 20 | 临时存储空间大小。单位：GiB。 |
| LoadBalancerWe ight | Integer | 否 | 50 | ECI实例作为负载均衡后端服务器时的权重，取值范围：1~100。 默认值：50。 |

弹性伸缩 ESS

| Tag.N.Key | String | 否 | version | 实例的标签键。N的取值范围：1~20。 如果传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
|---|---|---|---|---|
| Tag.N.Value | String | 否 | 3 | 实例的标签键。N的取值范围：1~20。 如果传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| ImageRegistryCr edential.N.Passw ord | String | 否 | yourpaasword | 镜像仓库密码。 |
| ImageRegistryCr edential.N.Serve r | String | 否 | registry-vpc.cn- shanghai-env17- d01.aliyuncs.co m | 镜像仓库注册地址。 |
| ImageRegistryCr edential.N.UserN ame | String | 否 | yourusername | 镜像仓库用户名。 |
| Container.N.Rea dinessProbe.Tim eoutSeconds | Integer | 否 | 5 | 检查超时的时间，默认值为1秒，最小值为 1秒。 |
| Container.N.Rea dinessProbe.Suc cessThreshold | Integer | 否 | 1 | 从上次检查失败后重新认定检查成功的检查次数阈值（必须是连续成功），当前值仅支持设置为1。 默认值：1。 |
| Container.N.Sec urityContext.Cap ability.Add.N | RepeatL ist | 否 | NET ADMIN _ | 为容器内的进程授予某些特定的权限。目前仅支持配置为NET ADMIN和 _ NET RAW。 _ 说明 NET RAW默认不支 _ 持，需提交工单申请。 |
| Container.N.Rea dinessProbe.Tcp Socket.Port | Integer | 否 | 8000 | 使用TCP Socket方式进行健康检查时，TCP Socket检测的端口。 |
| Container.N.Rea dinessProbe.Htt pGet.Scheme | String | 否 | HTTP | 使用HTTP请求方式进行健康检查时，HTTP Get请求对应的协议类型，取值范围： HTTP。 HTTPS。 |

弹性伸缩 ESS

| Container.N.Live nessProbe.Perio dSeconds | Integer | 否 | 5 | 检查执行的周期，默认值为10秒，最小值为1秒。 |
|---|---|---|---|---|
| Container.N.Port .N.Protocol | String | 否 | TCP | 协议类型。取值范围： TCP。 UDP。 |
| Container.N.Port .N.Port | Integer | 否 | 80 | 端口号。取值范围：1~65535。 |
| Container.N.Envi ronmentVar.N.K ey | String | 否 | PATH | 环境变量名。长度为1~128个字符。格式要求： [0-9a-zA-Z] ，以及下划线 （ ），不能以数字开头。 _ |
| Container.N.Envi ronmentVar.N.V alue | String | 否 | /usr/local/bin | 环境变量值。长度为0~256位。 |
| Container.N.Live nessProbe.TcpSo cket.Port | Integer | 否 | 8000 | 使用TCP Socket方式进行健康检查时，TCP Socket检测的端口。 |
| Container.N.Tty | Boolean | 否 | false | 是否开启交互。取值范围： true：开启。 false：未开启。 默认值：false。 当 Command 为 /bin/bash 命令时，需要设置为true。 |
| Container.N.Wor kingDir | String | 否 | /usr/local/ | 容器工作目录。 |
| Container.N.Live nessProbe.HttpG et.Scheme | String | 否 | HTTP | 使用HTTP请求方式进行健康检查时，HTTP Get请求对应的协议类型，取值范围： HTTP。 HTTPS。 |
| Container.N.Rea dinessProbe.Htt pGet.Port | Integer | 否 | 8080 | 使用HTTP请求方式进行健康检查时，HTTP Get请求检测的端口号。 |
| Container.N.Arg. N | RepeatL ist | 否 | 100 | 容器启动命令对应的参数。最多10个。 |
| Container.N.Gpu | Integer | 否 | 1 | 指定容器使用的GPU个数。 |

弹性伸缩 ESS

| Container.N.Rea dinessProbe.Initi alDelaySeconds | Integer | 否 | 3 | 检查开始执行的时间，以容器启动完成为起点计算。 |
|---|---|---|---|---|
| Container.N.Stdi n | Boolean | 否 | false | 此容器是否应在容器运行时为标准输入分配缓冲区。如果未设置，则容器中标准输入的读取值将导致EOF。 默认值：false。 |
| Container.N.Me mory | Float | 否 | 0.5 | 容器内存大小。单位：GiB。 |
| Container.N.Na me | String | 否 | nginx | 容器镜像名称。 |
| Container.N.Ima ge | String | 否 | registry-vpc.cn- shanghai-env17- d01.aliyuncs.co m/eci open/ngin _ x:latest | 容器镜像。 |
| Container.N.Live nessProbe.Initial DelaySeconds | Integer | 否 | 5 | 检查开始执行的时间，以容器启动完成为起点计算。 |
| Container.N.Volu meMount.N.Mou ntPropagation | String | 否 | None | 数据卷的挂载传播设置。挂载传播允许将 Container挂载的卷共享到同一Pod中的其他Container，甚至可以共享到同一节点上的其他Pod。取值范围： None：该卷不感知任何后续在此卷或其子目录上执行的挂载操作。 HostToCotainer：该卷将会感知到后续在此卷或其子目录上的挂载操作。 Bidirectional：和HostToCotainer类似，能感知挂载操作。另外，该卷将被传播回主机和使用同一卷的所有Pod的所有容器。 默认值：None。 |
| Container.N.Volu meMount.N.Mou ntPath | String | 否 | /pod/data | 容器挂载数据卷的目录。 说明容器挂载目录下的内容会被Volume的内容直接覆盖，请谨慎使用。 |
| Container.N.Volu meMount.N.Rea dOnly | Boolean | 否 | false | 数据卷是否只读。取值范围： true：是。 false：否。 默认值：false。 |
| Container.N.Volu meMount.N.Nam e | String | 否 | default-volume1 | 数据卷名称。同Volume中的Name。 |

弹性伸缩 ESS

| Container.N.Volu meMount.N.Sub Path | String | 否 | data2/ | 数据卷子路径。 |
|---|---|---|---|---|
| Container.N.Live nessProbe.Failur eThreshold | Integer | 否 | 3 | 从上次检查成功后认定检查失败的检查次数阈值（必须是连续失败）。 默认值：3。 |
| Container.N.Rea dinessProbe.Exe c.Command.N | RepeatL ist | 否 | cat /tmp/healthy | 使用命令行方式进行健康检查时，在容器内执行的命令。 |
| Container.N.Rea dinessProbe.Fail ureThreshold | Integer | 否 | 3 | 从上次检查成功后认定检查失败的检查次数阈值（必须是连续失败）。 默认值：3。 |
| Container.N.Ima gePullPolicy | String | 否 | Always | 容器的镜像拉取策略。取值范围： Alway：总是拉取。每次都拉取镜像。 IfNotPresent：按需拉取。优先使用本地镜像，本地没有镜像时则拉取镜像。 Never：从不拉取。使用本地镜像，不拉取镜像。 |
| Container.N.Cpu | Float | 否 | 0.25 | 容器的vCPU大小。单位：核。 |
| Container.N.Stdi nOnce | Boolean | 否 | false | 当标准输入为true时，标准输入流将在多个附加会话中是否保持开启状态。 如果 StdinOnce 设为 true ，标准输入在容器开启时被打开，在首个客户端附加到标准输入之前都为空，然后会一直保持开启状态，接收数据，直到客户端连接断开，此时标准输入被关闭，在容器重启前一直保持关闭状态。 |
| Container.N.Live nessProbe.HttpG et.Port | Integer | 否 | 8888 | 使用HTTP请求方式进行健康检查时，HTTP Get请求检测的端口号。 |
| Container.N.Live nessProbe.HttpG et.Path | String | 否 | /healthyz | 使用HTTP请求方式进行健康检查时，HTTP Get请求检测的路径。 |
| Container.N.Live nessProbe.Succe ssThreshold | Integer | 否 | 1 | 从上次检查失败后重新认定检查成功的检查次数阈值（必须是连续成功）。当前值仅支持设置为1。 默认值：1。 |

弹性伸缩 ESS

| Container.N.Rea dinessProbe.Peri odSeconds | Integer | 否 | 3 | 检查执行的周期，默认值为10秒，最小值为1秒。 |
|---|---|---|---|---|
| Container.N.Live nessProbe.Time outSeconds | Integer | 否 | 1 | 检查超时的时间，默认值为1秒，最小值为 1秒。 |
| Container.N.Co mmand.N | RepeatL ist | 否 | sleep | 容器启动命令。最多20个。每个命令最多包含256个字符。 |
| Container.N.Sec urityContext.Run AsUser | Long | 否 | 1000 | 设置运行容器的用户ID。 |
| Container.N.Rea dinessProbe.Htt pGet.Path | String | 否 | /healthz | 使用HTTP请求方式进行健康检查时，HTTP Get请求检测的路径。 |
| Container.N.Live nessProbe.Exec. Command.N | RepeatL ist | 否 | cat/tmp/healthy | 使用命令行方式进行健康检查时，在容器内执行的命令。 |
| Volume.N.Type | String | 否 | ConfigFileVolum e | 数据卷类型，取值范围： EmptyDirVolume：EmptyDir类型的数据卷，表示空目录。 NFSVolume：NFS类型的数据卷，表示网络文件系统。 ConfigFileVolume：ConfigFile类型的数据卷，表示配置文件。 FlexVolume：使用FlexVolume插件扩展存储类型，支持挂载云盘。 HostPathVolume：HostPath类型的数据卷，表示主机节点的文件或目录。 DiskVolume（不推荐）：云盘数据卷。建议使用FlexVolume挂载云盘。 |
| Volume.N.DiskV olume.DiskSize | Integer | 否 | 15 | DiskVolume的大小。单位：GiB。 |
| Volume.N.NFSVo lume.Path | String | 否 | /share | NFS数据卷路径。 |
| Volume.N.FlexVo lume.FsType | String | 否 | ext4 | 挂载的文件系统类型，默认取决于 FlexVolume的script。 |
| Volume.N.DiskV olume.FsType | String | 否 | xfs | DiskVolume的系统类型。 |
| Volume.N.HostP athVolume.Type | String | 否 | Directory | HostPath Volume的类型。取值范围： Directory：目录。 File：文件。 |

弹性伸缩 ESS

| Volume.N.NFSVo lume.ReadOnly | Boolean | 否 | false | NFS数据卷是否只读。取值范围： true：是。 false：否。 默认值：false。 |
|---|---|---|---|---|
| Volume.N.HostP athVolume.Path | String | 否 | /xx/xx/path | HostPath Volume在主机上的目录路径。 |
| Volume.N.FlexVo lume.Options | String | 否 | {"volumeId":"d- 2zehdahrwoa7sr g****","perform anceLevel": "PL2"} | FlexVolume对象选项列表。为KV形式， 采用JSON传递。 例如通过FlexVolume挂载云盘时，Options表示云盘的配置参数，可配置的参数如下： volumeId：已有云盘ID。 volumeSize：云盘大小，单位为GiB。 取值范围为20~32768。 performanceLevel：云盘性能等级。 更多信息，请参见云服务器ECS用户指南的云盘概述。 deleteWithInstance：是否随实例释放，默认为false。 encrypted：是否加密云盘，默认为 false。更多信息，请参见云服务器ECS 用户指南的加密概述。 kmsKeyId：加密云盘时，云盘使用的 KMS密钥ID。 |
| Volume.N.DiskV olume.DiskId | String | 否 | d-xx | DiskVolume的ID。 |
| Volume.N.Config FileVolumeDefau ltMode | Integer | 否 | 0644 | ConfigFileVolume默认的权限。 |
| Volume.N.NFSVo lume.Server | String | 否 | 3f9cd4a596- naw76.cn- shanghai-env17- d01.nas.aliyuncs .com | NFS服务器地址。 |
| Volume.N.FlexVo lume.Driver | String | 否 | flexvolume | 用于FlexVolume的驱动程序名称。 |
| Volume.N.Name | String | 否 | default-volume1 | 数据卷名称。 |
| Volume.N.Empty DirVolume.Medi um | String | 否 | memory | EmptyDirVolume的存储媒介，默认为空，使用node文件系统；如果设置为 memory ，则表示使用内存。 |

弹性伸缩 ESS

| Volume.N.Config FileVolumeConfi gFileToPath.N.Pa th | String | 否 | PATH | 环境变量名。长度为1~128个字符。格式要求： [0-9a-zA-Z] ，以及下划线 （ ），不能以数字开头。 _ |
|---|---|---|---|---|
| Volume.N.Config FileVolumeConfi gFileToPath.N.M ode | Integer | 否 | 0644 | ConfigFileVolume目录权限。 |
| Volume.N.Config FileVolumeConfi gFileToPath.N.Co ntent | String | 否 | bGl1bWk= | 配置文件内容。其中配置文件大小最大为 32 KB。 |
| InitContainer.N.I nitContainerEnvi ronmentVar.N.K ey | String | 否 | Path | 环境变量名。长度为1~128个字符。格式要求： [0-9a-zA-Z] ，以及下划线 （ ），不能以数字开头。 _ |
| InitContainer.N.I nitContainerEnvi ronmentVar.N.V alue | String | 否 | /usr/bin/ | 环境变量值。长度为0~256位。 |
| InitContainer.N.S ecurityContext.C apability.Add.N | RepeatL ist | 否 | NET ADMIN _ | 为容器内的进程授予某些特定的权限。目前仅支持配置为NET ADMIN和 _ NET RAW。 _ 说明 NET RAW默认不支 _ 持，需提交工单申请。 |
| InitContainer.N.I mage | String | 否 | nginx | 容器使用的镜像。 |
| InitContainer.N.I nitContainerVolu meMount.N.Mou ntPropagation | String | 否 | None | 数据卷的挂载传播设置。挂载传播允许将 Container挂载的卷共享到同一Pod中的其他Container，甚至可以共享到同一节点上的其他Pod。可能值： None：该卷不感知任何后续在此卷或其子目录上执行的挂载操作。 HostToCotainer：该卷将会感知到后续在此卷或其子目录上的挂载操作。 Bidirectional：和HostToCotainer类似，能感知挂载操作。另外，该卷将被传播回主机和使用同一卷的所有Pod的所有容器。 |
| InitContainer.N.I nitContainerVolu meMount.N.Mou ntPath | String | 否 | /usr/share/ | 挂载目录。 重要容器挂载目录下的内容会被Volume的内容直接覆盖，请您谨慎使用。 |

弹性伸缩 ESS

| InitContainer.N.I nitContainerVolu meMount.N.Rea dOnly | Boolean | 否 | false | 挂载路径是否只读。 默认值：false。 |
|---|---|---|---|---|
| InitContainer.N.I nitContainerVolu meMount.N.Nam e | String | 否 | test-empty | 挂载数据卷的名称。 |
| InitContainer.N.I nitContainerVolu meMount.N.Sub Path | String | 否 | /usr/sub/ | 数据卷下的子目录，方便Pod将同一个 Volume下不同目录挂载到容器不同目录。 |
| InitContainer.N.I magePullPolicy | String | 否 | Always | 镜像拉取策略。取值范围： Always：总是拉取。每次都拉取镜像。 IfNotPresent：按需拉取。优先使用本地镜像，本地没有镜像时则拉取镜像。 Never：从不拉取。使用本地镜像，不拉取镜像。 |
| InitContainer.N. Cpu | Float | 否 | 0.5 | 容器的vCPU大小。单位：核。 |
| InitContainer.N. WorkingDir | String | 否 | /usr/local | 工作目录。 |
| InitContainer.N. Command.N | RepeatL ist | 否 | sleep | 容器启动指令。 |
| InitContainer.N. Arg.N | RepeatL ist | 否 | 10 | 容器启动参数。 |
| InitContainer.N.S ecurityContext.R unAsUser | Long | 否 | 587 | 设置运行容器的用户ID。 |
| InitContainer.N. Gpu | Integer | 否 | 1 | 指定容器使用的GPU个数。 |
| InitContainer.N. Memory | Float | 否 | 1.0 | 容器的内存大小。单位：GiB。 |
| InitContainer.N. Name | String | 否 | test-init | 容器名称。 |
| DnsConfigName Server.N | RepeatL ist | 否 | 172.10.*.** | DNS服务器的IP地址列表。 |
| DnsConfigSearc h.N | RepeatL ist | 否 | svc.local.kubene tes | DNS搜索域列表。 |
| DnsConfigOption .N.Value | String | 否 | value | 对象变量值。 |
| DnsConfigOption .N.Name | String | 否 | name | 对象变量名。 |

| 开发指南·API参考 |  |  |  | 弹性伸缩 ES |
|---|---|---|---|---|

| HostAliase.N.Ip | String | 否 | 1.1.1.1 | 添加IP地址。 |
|---|---|---|---|---|
| HostAliase.N.Hos tname.N | RepeatL ist | 否 | hehe.com | 添加主机名。 |
| SecurityContext Sysctl.N.Value | String | 否 | 65536 | 实例运行的安全上下文的变量值。 |
| SecurityContext Sysctl.N.Name | String | 否 | kernel.msgmax | 实例运行的安全上下文系统名称。 |
| NtpServer.N | RepeatL ist | 否 | ntp.cloud.aliyun cs.com | NTP服务器。 |
| AcrRegistryInfo. N.Domain.N | RepeatL ist | 否 | *****-****- registry.cn- shanghai-env17- d01.cr.aliyuncs.c om | ACR企业版实例的域名。默认为相应实例的所有域名。支持指定个别域名，多个以半角逗号（,）分隔。 |
| AcrRegistryInfo. N.InstanceName | String | 否 | acr-test | ACR企业版实例的名称。 |
| AcrRegistryInfo. N.InstanceId | String | 否 | cri- nwj395hgf6f3*** * | ACR企业版实例ID。 |
| AcrRegistryInfo. N.RegionId | String | 否 | cn-shanghai- env17-d01 | ACR企业版实例所属地域。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 89945DD3-9072- 47D0-A318- 353284CF**** | 请求ID，唯一标识。 |
| ScalingConfigu rationId | String | eci- uf6fonnghi50u374* *** | 实例ID，即容器组ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=CreateEciScalingConfiguration &ScalingGroupId=asg-bp14wlu85wrpchm0**** &ScalingConfigurationName=scalingconfig**** &SecurityGroupId=sg-uf66jeqopgqa9hdn**** &ContainerGroupName=nginx-test &RestartPolicy=Always &Cpu=1.0 &Memory=2.0
```

弹性伸缩 ESS

```json
&DnsPolicy=Default &ImageSnapshotId=imc-2zebxkiifuyzzlhl**** &RamRoleName=RamTestRole &TerminationGracePeriodSeconds=60 &AutoMatchImageCache=false &Ipv6AddressCount=1 &ActiveDeadlineSeconds=1000 &AutoCreateEip=true &EipBandwidth=5 &HostName=test &IngressBandwidth=1024000 &EgressBandwidth=1024000 &CpuOptionsCore=2 &CpuOptionsThreadsPerCore=2 &EphemeralStorage=20 &LoadBalancerWeight=50 &Tag=[{"Key":"version","Value":"3"}] &ImageRegistryCredential=[{"Password":"yourpaasword","Server":"registry-vpc.cn-shanghai -env17-d01.aliyuncs.com","UserName":"yourusername"}] &Container= [{"ReadinessProbe.TimeoutSeconds":5,"ReadinessProbe.SuccessThreshold":1,"SecurityContext. pability.Add": ["NET_ADMIN"],"ReadinessProbe.TcpSocket.Port":8000,"ReadinessProbe.HttpGet.Scheme":"HTTP" LivenessProbe.PeriodSeconds":5,"Port":[{"Protocol":"TCP","Port":80}],"EnvironmentVar":[ {"Key":"PATH","Value":"/usr/local/bin"}],"LivenessProbe.TcpSocket.Port":8000,"Tty":false, orkingDir":"/usr/local/","LivenessProbe.HttpGet.Scheme":"HTTP","ReadinessProbe.HttpGet.Po ":8080,"Arg": ["100"],"Gpu":1,"ReadinessProbe.InitialDelaySeconds":3,"Stdin":false,"Memory":0.5,"Name": ginx","Image":"registry-vpc.cn-shanghai-env17d01.aliyuncs.com/eci_open/nginx:latest","LivenessProbe.InitialDelaySeconds":5,"VolumeMoun :[{"MountPropagation":"None","MountPath":"/pod/data","ReadOnly":false,"Name":"default-v olume1","SubPath":"data2/"}],"LivenessProbe.FailureThreshold":3,"ReadinessProbe.Exec.Comm d":["cat /tmp/healthy"],"ReadinessProbe.FailureThreshold":3,"ImagePullPolicy":"Always","StdinOnce" alse,"Cpu":0.25,"LivenessProbe.HttpGet.Port":8888,"LivenessProbe.HttpGet.Path":"/healthyz "LivenessProbe.SuccessThreshold":1,"ReadinessProbe.PeriodSeconds":3,"LivenessProbe.Timeou econds":1,"Command": ["sleep"],"SecurityContext.RunAsUser":1000,"ReadinessProbe.HttpGet.Path":"/healthz","Live ssProbe.Exec.Command":["cat/tmp/healthy"]}] &Volume= [{"Type":"ConfigFileVolume","DiskVolume.DiskSize":15,"NFSVolume.Path":"/share","FlexVolum FsType":"ext4","DiskVolume.FsType":"xfs","HostPathVolume.Type":"Directory","NFSVolume.Rea nly":false,"HostPathVolume.Path":"/xx/xx/path","FlexVolume.Options":"{\"volumeId\":\"d- 2zehdahrwoa7srg****\",\"performanceLevel\": \"PL2\"}","FlexVolume.Driver":"flexvolume","ConfigFileVolumeDefaultMode":644,"NFSVolume.S ver":"3f9cd4a596-naw76.cn-shanghai-env17-d01.nas.aliyuncs.com","DiskVolume.DiskId":"d-x x","Name":"defaultvolume1","EmptyDirVolume.Medium":"memory","ConfigFileVolumeConfigFileToPath":[{"Path":" PATH","Mode":644,"Content":"bGl1bWk="}]}] &InitContainer=[{"InitContainerEnvironmentVar": [{"Key":"Path","Value":"/usr/bin/"}],"SecurityContext.Capability.Add": ["NET_ADMIN"],"Image":"nginx","InitContainerVolumeMount": [{"MountPropagation":"None","MountPath":"/usr/share/","ReadOnly":false,"Name":"test-emp ty","SubPath":"/usr/sub/"}],"ImagePullPolicy":"Always","Cpu":0.5,"WorkingDir":"/usr/local "Command":["sleep"]"Arg":
```

弹性伸缩 ESS

```json
"Command":["sleep"],"Arg": ["10"],"SecurityContext.RunAsUser":587,"Gpu":1,"Memory":1.0,"Name":"test-init"}] &DnsConfigNameServer=["172.10.*.**"] &DnsConfigSearch=["svc.local.kubenetes"] &DnsConfigOption=[{"Value":"value","Name":"name"}] &HostAliase=[{"Ip":"1.1.1.1","Hostname":["hehe.com"]}] &SecurityContextSysctl=[{"Value":"65536","Name":"kernel.msgmax"}] &NtpServer=["ntp.cloud.aliyuncs.com"] &AcrRegistryInfo=[{"Domain":["*****-****-registry.cn-shanghai-env17d01.cr.aliyuncs.com"],"InstanceName":"acr-test","InstanceId":"crinwj395hgf6f3****","RegionId":"cn-shanghai-env17-d01"}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>89945DD3-9072-47D0-A318-353284CF****</RequestId>
      <ScalingConfigurationId>eci-uf6fonnghi50u374****</ScalingConfigurationId>
```

`JSON` 格式

```json
{
    "RequestId": "89945DD3-9072-47D0-A318-353284CF****",
    "ScalingConfigurationId": "eci-uf6fonnghi50u374****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InstanceType.Mismatc h | The specified scaling configuration and existing active scaling configuration have different instance type. | 指定的伸缩配置的实例规格与当前的伸缩配置的实例规格不匹配。 |
| 404 | InvalidDataDiskSnapsh otId.NotFound | Snapshot "XXX" does not exist. | 不存在指定的快照。 |
| 400 | InvalidDataDiskSnapsh otId.SizeNotSupported | The capacity of snapshot "XXX" exceeds the size limit of the specified disk category. | 指定快照的大小超过了磁盘大小的限制。 |
| 403 | InvalidDevice.InUse | Device "XXX" has been occupied. | 数据盘挂载点重复。 |

弹性伸缩 ESS

| 400 | InvalidImageId.Instanc eTypeMismatch | The specified image does not support the specified instance type. | 不允许在指定的实例规格下使用该镜像。 |
|---|---|---|---|
| 404 | InvalidImageId.NotFou nd | The specified image does not exist. | 该账号下不存在指定的镜像。 |
| 400 | InvalidKeyPairName.N otFound | The specified KeyPairName does not exist in our records. | 指定的KeyPairName不存在。 |
| 400 | InvalidNetworkType.Fo rRAMRole | RAMRole can't be used For classic instance. | 经典网络实例不支持 RamRoleName参数。 |
| 400 | InvalidParameter | The specified value of parameter KeyPairName is not valid. | Windows操作系统不支持 KeyPairName参数。 |
| 400 | InvalidParameter.Confl ict | The value of parameter SystemDisk.Category and parameter DataDisk.N.Category are conflict. | 指定的系统盘类型和数据盘类型冲突。 |
| 400 | InvalidRamRole.NotFo und | The specified RamRoleName does not exist. | 不存在指定的 RamRoleName。 |
| 400 | InvalidScalingConfigur ationName.Duplicate | The specified value of parameter ScalingConfigurationN ame is duplicated. | 已存在相同的伸缩配置名。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 该账号下不存在指定的伸缩组。 |
| 400 | InvalidSecurityGroupId .IncorrectNetworkType | The network type of specified security Group does not support this action. | 指定的安全组与伸缩组指定网络类型不一致。 |
| 404 | InvalidSecurityGroupId .NotFound | The specified security group does not exist. | 该账号下不存在指定的安全组。 |

弹性伸缩 ESS

| 400 | InvalidSecurityGroupId .VPCMismatch | The specified security group and the specified virtual switch are not in the same VPC. | 指定的安全组和虚拟交换机不属于同一个虚拟专有网络。 |
|---|---|---|---|
| 403 | InvalidSnapshot.TooOl d | This operation is denied because the specified snapshot is created before 2013- 07-15. | 该快照创建于2013年7月 15日或之前，调用被拒绝。 |
| 403 | InvalidSystemDiskCate gory.ValueUnauthorize d | The system disk category is not authorized. | 没有创建临时磁盘系统盘的权限。 |
| 400 | InvalidUserData.Base6 4FormatInvalid | The specified parameter UserData must be base64 encoded. | UserData不符合Base64 编码规范。 |
| 400 | InvalidUserData.SizeEx ceeded | The specified parameter UserData exceeds the size. | 指定的UserData过长。 |
| 403 | QuotaExceeded.Ephe meralDiskSize | Ephemeral disk size quota exceeded. | 临时磁盘数据盘总容量超过2 TiB（2048 GiB）。 |
| 400 | QuotaExceeded.Scalin gConfiguration | Scaling configuration quota exceeded in the specified scaling group. | 您目前拥有的伸缩配置个数已经达到上限。 |
| 400 | QuotaExceeded.Securi tyGroupInstance | Instance quota exceeded in the specified security group. | 指定的安全组中添加的 ECI实例个数已经达到上限。 |

#### DescribeEciScalingConfigurations

调用DescribeEciScalingConfigurations查询ECI类型的伸缩配置信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeEciScali ngConfiguration s | 系统规定参数。取值： DescribeEciScalingConfigurations。 |

弹性伸缩 ESS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 伸缩配置所属伸缩组的地域ID。 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 伸缩配置列表的页码，起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 50 | 分页查询时设置的每页行数，最大值： 50。 默认值：10。 |
| ScalingGroupId | String | 否 | asg- bp17pelvl720x3 v7**** | 伸缩组的ID，您可以查询该伸缩组下所有的伸缩配置。 |
| ScalingConfigura tionId.N | RepeatL ist | 否 | asc- bp17pelvl720x5 ub**** | ScalingConfigurationId.N为待查询伸缩配置的ID，N的取值范围：1~10。 查询结果包括生效和未生效的伸缩配置， 并通过返回参数LifecycleState进行标识。 |
| ScalingConfigura tionName.N | RepeatL ist | 否 | scalingcon**** | ScalingConfigurationName.N为待查询伸缩配置的名称，N的取值范围：1~10。 查询结果会忽略失效的伸缩配置名称，并且不报错。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 50 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingConfigu rations | Array of ScalingConfigu ration |  | 伸缩配置信息的集合。 |
| AcrRegistryInf os | Array of AcrRegistryInf o |  | ACR企业版实例的信息。 |
| Domains | List | *****-****- registry.cn-beijing- env17- d01.cr.aliyuncs.co m | ACR企业版实例的域名。默认为相应实例的所有域名。支持指定个别域名，多个以半角逗号（,） 分隔。 |

弹性伸缩 ESS

| InstanceId | String | cri- nwj395hgf6f3**** | ACR企业版实例ID。 |
|---|---|---|---|
| InstanceName | String | acr-test | ACR企业版实例的名称。 |
| RegionId | String | cn-hangzhou- env17-d01 | ACR企业版实例所属地域。 |
| ActiveDeadlin eSeconds | Integer | 1000 | 有效期限。单位为秒。 |
| AutoCreateEip | Boolean | true | 是否自动创建弹性公网IP，并绑定ECI实例。 |
| AutoMatchIma geCache | Boolean | false | 是否自动匹配镜像缓存。 默认值：false。 |
| ContainerGrou pName | String | test | ECI实例名称，即容器组名称。 |
| Containers | Array of Container |  | 实例包含的容器列表。 |
| Args | List | 10 | 容器启动命令对应的参数。最多10个。 |
| Commands | List | sleep | 容器启动命令。最多20个。每个命令最多包含 256个字符。 |
| Cpu | Float | 2.0 | 容器的vCPU大小。单位：核。 |
| EnvironmentV ars | Array of EnvironmentV ar |  | 环境变量的信息。 |
| Key | String | PATH | 环境变量名。长度为1~128位。格式要求： [0-9a-zA-Z] ，以及下划线，不能以数字开头。 |
| Value | String | /usr/bin/ | 环境变量值。长度为0~256位。 |
| Gpu | Integer | 1 | 容器使用的GPU个数。 |
| Image | String | mysql | 容器镜像。 |

弹性伸缩 ESS

| ImagePullPolic y | String | Always | 镜像拉取策略。可能值： Alway：总是拉取。每次都拉取镜像。 IfNotPresent：按需拉取。优先使用本地镜像，本地没有镜像时则拉取镜像。 Never：从不拉取。使用本地镜像，不拉取镜像。 |
|---|---|---|---|
| LivenessProbe ExecCommand s | List | cat/tmp/healthy | 使用命令行方式进行健康检查时，在容器内执行的命令。 |
| LivenessProbe FailureThresho ld | Integer | 3 | 从上次检查成功后认定检查失败的检查次数阈值 （必须是连续失败）。 默认值：3。 |
| LivenessProbe HttpGetPath | String | /usr/nginx/ | HttpGet检测的路径。 |
| LivenessProbe HttpGetPort | Integer | 80 | HttpGet检测的端口。 |
| LivenessProbe HttpGetSchem e | String | HTTP | 使用HTTP请求方式进行健康检查时，HTTP Get 请求对应的协议类型，可能值： HTTP。 HTTPS。 |
| LivenessProbeI nitialDelaySec onds | Integer | 10 | 检查开始执行的时间，以容器启动完成为起点计算。 |
| LivenessProbe PeriodSeconds | Integer | 1 | 检查执行的周期，默认为10秒，最小为1秒。 |
| LivenessProbe SuccessThresh old | Integer | 1 | 从上次检查失败后重新认定检查成功的检查次数阈值（必须是连续成功），当前值仅支持设置为 1。 默认值：1。 |
| LivenessProbe TcpSocketPort | Integer | 80 | TcpSocket的端口号。 |
| LivenessProbe TimeoutSecon ds | Integer | 10 | 检查超时的时间，默认为1秒，最小值为1秒。 |
| Memory | Float | 2.0 | 容器内存大小。单位：GiB。 |
| Name | String | nginx | 容器名称。 |
| Ports | Array of Port |  | 暴露端口和协议。 |

弹性伸缩 ESS

| Port | Integer | 8888 | 端口号。可能值：1~65535。 |
|---|---|---|---|
| Protocol | String | TCP | 协议类型。可能值： TCP。 UDP。 |
| ReadinessProb eExecComman ds | List | cat/tmp/healthy | 使用命令行方式进行健康检查时，在容器内执行的命令。 |
| ReadinessProb eFailureThresh old | Integer | 3 | 从上次检查成功后认定检查失败的检查次数阈值 （必须是连续失败）。 默认值：3。 |
| ReadinessProb eHttpGetPath | String | /usr/local | HttpGet检测的路径。 |
| ReadinessProb eHttpGetPort | Integer | 80 | HttpGet检测的端口。 |
| ReadinessProb eHttpGetSche me | String | HTTP | 使用HTTP请求方式进行健康检查时，HTTP Get 请求对应的协议类型，可能值： HTTP。 HTTPS。 |
| ReadinessProb eInitialDelaySe conds | Integer | 5 | 检查开始执行的时间，以容器启动完成为起点计算。 |
| ReadinessProb ePeriodSecond s | Integer | 1 | 检查执行的周期，默认为10秒，最小为1秒。 |
| ReadinessProb eSuccessThres hold | Integer | 1 | 从上次检查失败后重新认定检查成功的检查次数阈值（必须是连续成功），当前值仅支持设置为 1。 默认值：1。 |
| ReadinessProb eTcpSocketPor t | Integer | 8888 | 使用TCP Socket方式进行健康检查时，TCP Socket检测的端口。 |
| ReadinessProb eTimeoutSeco nds | Integer | 5 | 检查超时的时间，默认为1秒，最小为1秒。 |
| SecurityConte xtCapabilityAd ds | List | NET ADMIN _ | 为容器内的进程授予某些特定的权限。目前仅支持配置为 NET ADMIN 和 NET RAW 。 _ _ 说明 NET RAW 默认不支持，需 _ 提交工单申请。 |

弹性伸缩 ESS

| SecurityConte xtRunAsUser | Long | 1000 | 设置运行容器的用户ID。 |
|---|---|---|---|
| Stdin | Boolean | true | 此容器是否应在容器运行时为标准输入分配缓冲区。如果未设置，则容器中标准输入的读取值将导致EOF。 默认值：false。 |
| StdinOnce | Boolean | true | 当标准输入为true时，标准输入流将在多个附加会话中保持开启状态。 如果StdinOnce设为true，标准输入在容器开启时被打开，在首个客户端附加到标准输入之前都为空，然后会一直保持开启状态，接收数据，直到客户端连接断开，此时标准输入被关闭，在容器重启前一直保持关闭状态。 |
| Tty | Boolean | false | 是否开启交互。可能值： true：开启。 false：未开启。 例如：当Command配置为 /bin/bash 时， 需要配置为true。 默认值：false。 |
| VolumeMounts | Array of VolumeMount |  | 挂载数据卷。 |
| MountPath | String | /pod/data | 容器挂载数据卷的目录。 重要容器挂载目录下的内容会被 Volume的内容直接覆盖，请谨慎使用。 |
| MountPropaga tion | String | None | 数据卷的挂载传播设置。挂载传播允许将 Container挂载的卷共享到同一Pod中的其他 Container，甚至可以共享到同一节点上的其他 Pod。可能值： None：该卷不感知任何后续在此卷或其子目录上执行的挂载操作。 HostToCotainer：该卷将会感知到后续在此卷或其子目录上的挂载操作。 Bidirectional：和HostToCotainer类似，能感知挂载操作。另外，该卷将被传播回主机和使用同一卷的所有Pod的所有容器。 默认值：None。 |
| Name | String | default-volume1 | 数据卷名称。同Volume中的Name。 |

弹性伸缩 ESS

| ReadOnly | Boolean | false | 数据卷是否只读。 默认值：false。 |
|---|---|---|---|
| SubPath | String | data2/ | 数据卷子路径。 |
| WorkingDir | String | /usr/local/nginx | 容器工作目录。 |
| CostOptimizati on | Boolean | false | 是否开启成本优化开关。可能值： true：开启。 false：未开启。 默认值：false。 |
| Cpu | Float | 2.0 | 容器的vCPU大小。单位：核。 |
| CpuOptionsCo re | Integer | 2 | CPU物理核心数。仅部分规格支持自定义设置。 更多信息，请参见弹性容器实例中的自定义CPU 选项章节。 |
| CpuOptionsThr eadsPerCore | Integer | 2 | 每核线程数。仅部分规格支持自定义设置。配置为1时表示关闭超线程。更多信息，请参见弹性容器实例中的自定义CPU选项章节。 |
| CreationTime | String | 2014-08- 14T10:58Z | 伸缩配置的创建时间。 |
| DnsConfigNam eServers | List | 172.10.*.** | DNS服务器的IP地址列表。 |
| DnsConfigOpti ons | Array of DnsConfigOpti on |  | 对象选项列表，每个对象由Name和Value（可选）构成。 |
| Name | String | name | 对象的变量名。 |
| Value | String | value | 对象变量值。 |
| DnsConfigSear ches | List | svc.local.kubenete s | DNS搜索域列表。 |
| DnsPolicy | String | Default | DNS策略。可能值： None：使用DnsConfig字段设置的DNS。 Default：继承运行环境的DNS设置。 |
| EgressBandwi dth | Long | 1024000 | 出方向带宽限制。单位：Byte。 |

弹性伸缩 ESS

| EipBandwidth | Integer | 5 | 弹性公网IP的带宽。 默认值：5 Mbit/s。 |
|---|---|---|---|
| EphemeralStor age | Integer | 20 | 临时存储空间大小。单位：GiB。 |
| HostAliases | Array of HostAlias |  | 自定义实例内一个容器的Hostname映射。 |
| Hostnames | List | ['hehe.com', 'haha.com'] | 添加主机名。 |
| Ip | String | 192.0.XX.XX | 添加IP地址。 |
| HostName | String | ['hehe.com', 'haha.com'] | 主机名。 |
| ImageRegistry Credentials | Array of ImageRegistry Credential |  | 镜像仓库信息。 |
| Password | String | yourpaasword | 镜像仓库密码。 |
| Server | String | registry-vpc.cn- shanghai-env17- d01.aliyuncs.com | 镜像仓库注册地址。 |
| UserName | String | yourusername | 镜像仓库用户名。 |
| ImageSnapsho tId | String | imc- 2zebxkiifuyzzlhl*** * | 镜像缓存ID。 |
| IngressBandwi dth | Long | 1024000 | 入方向带宽限制。单位：Byte。 |
| InitContainers | Array of InitContainer |  | Init容器列表。 |
| Cpu | Float | 0.5 | 容器的vCPU大小。单位：核。 |
| Gpu | Integer | 1 | 指定容器使用的GPU个数。 |
| Image | String | nginx | 容器使用的镜像。 |

弹性伸缩 ESS

| ImagePullPolic y | String | Always | 镜像拉取策略。可能值： Always：总是拉取。每次都拉取镜像。 IfNotPresent：按需拉取。优先使用本地镜像，本地没有镜像时则拉取镜像。 Never：从不拉取。使用本地镜像，不拉取镜像。 |
|---|---|---|---|
| InitContainerA rgs | List | 10 | 容器启动参数。 |
| InitContainerC ommands | List | sleep | 容器启动指令。 |
| InitContainerE nvironmentVar s | Array of InitContainerE nvironmentVar |  | 环境变量的信息。 |
| Key | String | PATH | 环境变量名。长度为1~128位。格式要求： [0-9a-zA-Z] ，以及下划线，不能以数字开头。 |
| Value | String | /usr/local/bin | 环境变量值。长度为0~256位。 |
| InitContainerV olumeMounts | Array of InitContainerV olumeMount |  | 数据卷挂载。 |
| MountPath | String | /usr/share/ | 挂载目录。 重要容器的挂载目录下的内容被 Volume的内容直接覆盖，所以要慎用。 |
| MountPropaga tion | String | None | 数据卷的挂载传播设置。挂载传播允许将 Container挂载的卷共享到同一Pod中的其他 Container，甚至可以共享到同一节点上的其他 Pod。可能值： None：该卷不感知任何后续在此卷或其子目录上执行的挂载操作。 HostToCotainer：该卷将会感知到后续在此卷或其子目录上的挂载操作。 Bidirectional：和HostToCotainer类似，能感知挂载操作。另外，该卷将被传播回主机和使用同一卷的所有Pod的所有容器。 默认值：None。 |
| Name | String | test-empty | 挂载数据卷的名称。 |
| ReadOnly | Boolean | false | 挂载路径是否只读。 默认值：false。 |

弹性伸缩 ESS

| SubPath | String | /usr/sub/ | 数据卷下的子目录，方便Pod将同一个Volume 下不同目录挂载到容器不同目录。 |
|---|---|---|---|
| Memory | Float | 1.0 | 容器的内存大小。单位：GiB。 |
| Name | String | test-init | 容器名称。 |
| SecurityConte xtCapabilityAd ds | List | NET ADMIN _ | 为容器内的进程授予某些特定的权限。目前仅支持配置为 NET ADMIN 和 NET RAW 。 _ _ 说明 NET RAW 默认不支持，需 _ 提交工单申请。 |
| SecurityConte xtReadOnlyRo otFilesystem | Boolean | true | 容器运行的根文件系统是否为只读。目前仅支持配置为true。 |
| SecurityConte xtRunAsUser | String | 587 | 设置运行容器的用户ID。 |
| WorkingDir | String | /usr/local | 工作目录。 |
| InstanceFamil yLevel | String | EnterpriseLevel | 实例规格族级别，用于筛选符合要求的实例规格范围，当 CostOptimization 开启时生效。 可能值： EntryLevel：入门级，即共享型实例规格。成本更低，但是无法保证实例计算性能的稳定。 适用于平时CPU使用率低的业务场景。更多信息，请参见云服务器ECS的共享型章节。 EnterpriseLevel：企业级。性能稳定且资源独享，适用于对稳定性要求高的业务场景。更多信息，请参见云服务器ECS的实例规格族章节。 CreditEntryLevel：积分入门级，即突发性能实例。通过CPU积分来保证计算性能，适用于平时CPU使用率低、偶有突发CPU使用率的业务场景。更多信息，请参见云服务器ECS的突发性能实例概述章节。 |
| Ipv6AddressCo unt | Integer | 1 | IPv6地址数。固定为1，即一个ECI实例支持绑定一个IPv6地址。 |
| LifecycleState | String | Active | 伸缩配置在伸缩组中的状态。可能值： Active：生效状态。伸缩组会使用处于生效状态的伸缩配置自动创建ECI实例。 Inacitve：未生效状态。处于未生效状态的伸缩配置存在于伸缩组中，但伸缩组不会使用此类伸缩配置自动创建ECI实例。 |

弹性伸缩 ESS

| LoadBalancer Weight | Integer | 1 | ECI实例作为后端服务器时的权重，可能值： 1~100。 |
|---|---|---|---|
| Memory | Float | 16 | 内存大小，单位：GiB。 同时指定CPU和Memory可以定义实例规格范围。例如，CPU=2且Memory=16可以定义配置为2 vCPU和16 GiB的所有实例规格。弹性伸缩会结合IO优化、可用区等因素确定可用实例规格集合，并根据价格排序为您创建价格最低的实例。 说明该区间配置效果仅在成本优化模式下且伸缩配置未设置实例规格时生效。 |
| NtpServers | List | ntp.cloud.aliyuncs. com | NTP服务器。 |
| RamRoleName | String | ram:PassRole | 实例RAM角色名称，ECI与ECS共用实例RAM角色，具体操作，请参见云服务器ECS中的通过API 使用实例RAM角色章节。 |
| RegionId | String | cn-hangzhou- env17-d01 | ECI实例所属的地域ID。 |
| ResourceGrou pId | String | rg- 8db03793gfrz**** | 说明该参数未开放使用。 |
| RestartPolicy | String | Never | 容器组的重启策略。可能值： Never：不重启。 Always：始终重启。 OnFailure：失败时重启。 |
| ScalingConfigu rationId | String | asc- bp1ezrfgoyn5kijl*** * | 伸缩配置的ID。 |
| ScalingConfigu rationName | String | scalingconfi**** | 伸缩配置的名称。 |
| ScalingGroupI d | String | asg- bp17pelvl720x3v7* *** | 伸缩配置所属伸缩组的ID。 |
| SecurityConte xtSysCtls | Array of SecurityConte xtSysCtl |  | 实例运行的安全上下文的系统信息。 |
| Name | String | kernel.msgmax | 实例运行的安全上下文系统名称。 |
| Value | String | 65536 | 实例运行的安全上下文的变量值。 |

弹性伸缩 ESS

| SecurityGroupI d | String | sg- bp18kz60mefs**** | ECI实例所属的安全组的ID，同一个安全组内的 ECI实例可以互相访问。 |
|---|---|---|---|
| SpotPriceLimit | Float | 0.025 | 说明该参数未开放使用。 |
| SpotStrategy | String | NoSpot | 说明该参数未开放使用。 |
| Tags | Array of Tag |  | 实例的标签键值对。 |
| Key | String | version | 标签键。 |
| Value | String | 3 | 标签值。 |
| TerminationGr acePeriodSeco nds | Integer | 60 | 程序的缓冲时间，用于处理关闭之前的操作。 |
| Volumes | Array of Volume |  | 数据卷信息。 |
| ConfigFileVolu meConfigFileT oPaths | Array of ConfigFileVolu meConfigFileT oPath |  | 配置文件路径列表。 |
| Content | String | bGl1bWk= | 配置文件内容。其中，配置文件大小最大为32 KB。 |
| Mode | Integer | 644 | ConfigFileVolume目录权限。 |
| Path | String | /usr/bin/ | 相对文件路径。 |
| ConfigFileVolu meDefaultMod e | Integer | 644 | ConfigFileVolume默认的权限。 |
| DiskVolumeDis kId | String | d-xxxx | DiskVolume的ID。 |
| DiskVolumeDis kSize | Integer | 15 | DiskVolume的大小。单位为GiB。 |
| DiskVolumeFs Type | String | xfs | DiskVolume的系统类型。 |

弹性伸缩 ESS

| EmptyDirVolu meMedium | String | memory | EmptyDirVolume的存储媒介，默认为空，使用 node文件系统。如果设置为memory，则表示使用内存。 |
|---|---|---|---|
| FlexVolumeDri ver | String | alicloud/disk | 使用FlexVolume插件挂载数据卷时的驱动类型。目前支持alicloud/disk，表示挂载阿里云云盘。 |
| FlexVolumeFs Type | String | ext4 | 挂载的文件系统类型，默认取决于FlexVolume 的script。 |
| FlexVolumeOp tions | String | {"volumeId":"d- 2zehdahrwoa7srg* ***","performanceL evel": "PL2"} | FlexVolume对象选项列表。为KV形式，采用 JSON传递。 例如通过FlexVolume挂载云盘时，Options表示云盘的配置参数，可配置的参数如下： volumeId：已有云盘ID。 volumeSize：云盘大小，单位为GiB。取值范围为20~32768。 performanceLevel：云盘性能等级。更多信息，请参见云服务器ECS用户指南中的云盘概述。 deleteWithInstance：是否随实例释放，默认为false。 encrypted：是否加密云盘，默认为false。 更多信息，请参见云服务器ECS用户指南中的加密概述。 kmsKeyId：加密云盘时，云盘使用的KMS密钥ID。 |
| NFSVolumePat h | String | /share | NFS数据卷路径。 |
| NFSVolumeRe adOnly | Boolean | false | NFS数据卷是否只读。 默认值：false。 |
| NFSVolumeSer ver | String | 3f9cd4a596- naw76.cn- shanghai-env17- d01.nas.aliyuncs.c om | NFS服务器地址。 |
| Name | String | default-volume1 | 数据卷名称。 |

弹性伸缩 ESS

| Type | String | EmptyDirVolume | 数据卷类型，可能值： EmptyDirVolume：EmptyDir类型的数据卷，表示空目录。 NFSVolume：NFS类型的数据卷，表示网络文件系统。 ConfigFileVolume：ConfigFile类型的数据卷，表示配置文件。 FlexVolume：使用FlexVolume插件扩展存储类型，支持挂载云盘。 HostPathVolume：HostPath类型的数据卷，表示主机节点的文件或目录。 DiskVolume（不推荐）：云盘数据卷。建议使用FlexVolume挂载云盘。 |
|---|---|---|---|
| TotalCount | Integer | 1 | 伸缩配置的总数。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DescribeEciScalingConfigurations &RegionId=cn-qingdao-env17-d01 &PageNumber=1 &PageSize=50 &ScalingGroupId=asg-bp17pelvl720x3v7**** &ScalingConfigurationId=["asc-bp17pelvl720x5ub****"] &ScalingConfigurationName=["scalingcon****"]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeEciScalingConfigurationsResponse>
      <TotalCount>1</TotalCount>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <PageSize>50</PageSize>
      <PageNumber>1</PageNumber>
      <ScalingConfigurations>
            <ScalingConfigurationName>scalingconfi****</ScalingConfigurationName>
            <Memory>16</Memory>
            <Cpu>2</Cpu>
            <LifecycleState>Active</LifecycleState>
            <ContainerGroupName>test</ContainerGroupName>
            <IngressBandwidth>1024000</IngressBandwidth>
            <ImageSnapshotId>imc-2zebxkiifuyzzlhl****</ImageSnapshotId>
            <RamRoleName>ram:PassRole</RamRoleName>
            <EgressBandwidth>1024000</EgressBandwidth>
            <AutoMatchImageCache>false</AutoMatchImageCache>
            <Ipv6AddressCount>1</Ipv6AddressCount>
            <HostName>['hehe.com', 'haha.com']</HostName>
            <ActiveDeadlineSeconds>1000</ActiveDeadlineSeconds>
            <LoadBalancerWeight>1</LoadBalancerWeight>
```

弹性伸缩 ESS

```xml
            <CpuOptionsThreadsPerCore>2</CpuOptionsThreadsPerCore>
            <TerminationGracePeriodSeconds>60</TerminationGracePeriodSeconds>
            <ScalingGroupId>asg-bp17pelvl720x3v7****</ScalingGroupId>
            <SecurityGroupId>sg-bp18kz60mefs****</SecurityGroupId>
            <CpuOptionsCore>2</CpuOptionsCore>
            <RestartPolicy>Never</RestartPolicy>
            <AutoCreateEip>true</AutoCreateEip>
            <EipBandwidth>5</EipBandwidth>
            <DnsPolicy>Default</DnsPolicy>
            <CreationTime>2014-08-14T10:58Z</CreationTime>
            <RegionId>cn-hangzhou-env17-d01</RegionId>
            <ScalingConfigurationId>asc-bp1ezrfgoyn5kijl****</ScalingConfigurationId>
            <EphemeralStorage>20</EphemeralStorage>
            <HostAliases>
                  <Ip>192.0.XX.XX</Ip>
                  <Hostnames>['hehe.com', 'haha.com']</Hostnames>
            </HostAliases>
            <AcrRegistryInfos>
                  <InstanceName>acr-test</InstanceName>
                  <InstanceId>cri-nwj395hgf6f3****</InstanceId>
                  <RegionId>cn-hangzhou-env17-d01</RegionId>
                  <Domains>*****-****-registry.cn-beijing-env17-
d01.cr.aliyuncs.com</Domains>
            </AcrRegistryInfos>
            <InitContainers>
                  <WorkingDir>/usr/local</WorkingDir>
                  <ImagePullPolicy>Always</ImagePullPolicy>
<SecurityContextReadOnlyRootFilesystem>true</SecurityContextReadOnlyRootFilesystem>
                  <Memory>1</Memory>
                  <SecurityContextRunAsUser>587</SecurityContextRunAsUser>
                  <Cpu>0.5</Cpu>
                  <Image>nginx</Image>
                  <Gpu>1</Gpu>
                  <Name>test-init</Name>
                  <InitContainerVolumeMounts>
                        <MountPath>/usr/share/</MountPath>
                        <ReadOnly>false</ReadOnly>
                        <SubPath>/usr/sub/</SubPath>
                        <MountPropagation>None</MountPropagation>
                        <Name>test-empty</Name>
                  </InitContainerVolumeMounts>
                  <InitContainerEnvironmentVars>
                        <Value>/usr/local/bin</Value>
                        <Key>PATH</Key>
                  </InitContainerEnvironmentVars>
<SecurityContextCapabilityAdds>NET_ADMIN</SecurityContextCapabilityAdds>
                  <InitContainerCommands>sleep</InitContainerCommands>
                  <InitContainerArgs>10</InitContainerArgs>
            </InitContainers>
            <Volumes>
                  <NFSVolumePath>/share</NFSVolumePath>
                  <Type>EmptyDirVolume</Type>
<Fl
```

Vl Di

```
>lil d/dik</Fl
```

Vl Di > 弹性伸缩 ESS

```xml
                  <FlexVolumeDriver>alicloud/disk</FlexVolumeDriver>
                  <FlexVolumeFsType>ext4</FlexVolumeFsType>
                  <DiskVolumeDiskId>d-xxxx</DiskVolumeDiskId>
                  <NFSVolumeServer>3f9cd4a596-naw76.cn-shanghai-env17-
d01.nas.aliyuncs.com</NFSVolumeServer>
                  <FlexVolumeOptions>{"volumeId":"d-
2zehdahrwoa7srg****","performanceLevel": "PL2"}</FlexVolumeOptions>
                  <ConfigFileVolumeDefaultMode>644</ConfigFileVolumeDefaultMode>
                  <DiskVolumeDiskSize>15</DiskVolumeDiskSize>
                  <EmptyDirVolumeMedium>memory</EmptyDirVolumeMedium>
                  <Name>default-volume1</Name>
                  <NFSVolumeReadOnly>false</NFSVolumeReadOnly>
                  <DiskVolumeFsType>xfs</DiskVolumeFsType>
                  <ConfigFileVolumeConfigFileToPaths>
                        <Path>/usr/bin/</Path>
                        <Content>bGl1bWk=</Content>
                        <Mode>644</Mode>
                  </ConfigFileVolumeConfigFileToPaths>
            </Volumes>
            <SecurityContextSysCtls>
                  <Value>65536</Value>
                  <Name>kernel.msgmax</Name>
            </SecurityContextSysCtls>
            <ImageRegistryCredentials>
                  <UserName>yourusername</UserName>
                  <Server>registry-vpc.cn-shanghai-env17-d01.aliyuncs.com</Server>
                  <Password>yourpaasword</Password>
            </ImageRegistryCredentials>
            <Containers>
                  <Memory>2</Memory>
                  <ReadinessProbeTcpSocketPort>8888</ReadinessProbeTcpSocketPort>
                  <Cpu>2</Cpu>
                  <ReadinessProbeHttpGetPath>/usr/local</ReadinessProbeHttpGetPath>
                  <ReadinessProbeHttpGetScheme>HTTP</ReadinessProbeHttpGetScheme>
                  <Image>mysql</Image>
                  <Gpu>1</Gpu>
                  <StdinOnce>true</StdinOnce>
                  <LivenessProbeTimeoutSeconds>10</LivenessProbeTimeoutSeconds>
                  <Name>nginx</Name>
                  <LivenessProbeHttpGetScheme>HTTP</LivenessProbeHttpGetScheme>
                  <LivenessProbeFailureThreshold>3</LivenessProbeFailureThreshold>
                  <LivenessProbeHttpGetPath>/usr/nginx/</LivenessProbeHttpGetPath>
<LivenessProbeInitialDelaySeconds>10</LivenessProbeInitialDelaySeconds>
                  <SecurityContextRunAsUser>1000</SecurityContextRunAsUser>
                  <Tty>false</Tty>
                  <LivenessProbeTcpSocketPort>80</LivenessProbeTcpSocketPort>
                  <ReadinessProbePeriodSeconds>1</ReadinessProbePeriodSeconds>
                  <LivenessProbePeriodSeconds>1</LivenessProbePeriodSeconds>
                  <LivenessProbeSuccessThreshold>1</LivenessProbeSuccessThreshold>
<ReadinessProbeInitialDelaySeconds>5</ReadinessProbeInitialDelaySeconds>
                  <ReadinessProbeSuccessThreshold>1</ReadinessProbeSuccessThreshold>
                  <ReadinessProbeFailureThreshold>3</ReadinessProbeFailureThreshold>
<ReadinessProbeHttpGetPort>80</ReadinessProbeHttpGetPort>
```

弹性伸缩 ESS

```xml
                  <ReadinessProbeHttpGetPort>80</ReadinessProbeHttpGetPort>
                  <Stdin>true</Stdin>
                  <WorkingDir>/usr/local/nginx</WorkingDir>
                  <ImagePullPolicy>Always</ImagePullPolicy>
                  <LivenessProbeHttpGetPort>80</LivenessProbeHttpGetPort>
                  <ReadinessProbeTimeoutSeconds>5</ReadinessProbeTimeoutSeconds>
                  <EnvironmentVars>
                        <Value>/usr/bin/</Value>
                        <Key>PATH</Key>
                  </EnvironmentVars>
                  <Ports>
                        <Port>8888</Port>
                        <Protocol>TCP</Protocol>
                  </Ports>
                  <VolumeMounts>
                        <MountPath>/pod/data</MountPath>
                        <ReadOnly>false</ReadOnly>
                        <SubPath>data2/</SubPath>
                        <MountPropagation>None</MountPropagation>
                        <Name>default-volume1</Name>
                  </VolumeMounts>
                  <Commands>sleep</Commands>
                  <LivenessProbeExecCommands>cat/tmp/healthy</LivenessProbeExecCommands>
                  <Args>10</Args>
<ReadinessProbeExecCommands>cat/tmp/healthy</ReadinessProbeExecCommands> <SecurityContextCapabilityAdds>NET_ADMIN</SecurityContextCapabilityAdds>
            </Containers>
            <DnsConfigOptions>
                  <Value>value</Value>
                  <Name>name</Name>
            </DnsConfigOptions>
            <Tags>
                  <Value>3</Value>
                  <Key>version</Key>
            </Tags>
            <DnsConfigNameServers>172.10.*.**</DnsConfigNameServers>
            <DnsConfigSearches>svc.local.kubenetes</DnsConfigSearches>
            <NtpServers>ntp.cloud.aliyuncs.com</NtpServers>
      </ScalingConfigurations>
</DescribeEciScalingConfigurationsResponse>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "PageSize": 50,
    "PageNumber": 1,
    "ScalingConfigurations": {
        "ScalingConfigurationName": "scalingconfi****",
        "Memory": 16,
        "Cpu": 2,
```

弹性伸缩 ESS

```json
        "LifecycleState": "Active",
        "ContainerGroupName": "test",
        "IngressBandwidth": 1024000,
        "ImageSnapshotId": "imc-2zebxkiifuyzzlhl****",
        "RamRoleName": "ram:PassRole",
        "EgressBandwidth": 1024000,
        "AutoMatchImageCache": false,
        "Ipv6AddressCount": 1,
        "HostName": "['hehe.com', 'haha.com']",
        "ActiveDeadlineSeconds": 1000,
        "LoadBalancerWeight": 1,
        "CpuOptionsThreadsPerCore": 2,
        "TerminationGracePeriodSeconds": 60,
        "ScalingGroupId": "asg-bp17pelvl720x3v7****",
        "SecurityGroupId": "sg-bp18kz60mefs****",
        "CpuOptionsCore": 2,
        "RestartPolicy": "Never",
        "AutoCreateEip": true,
        "EipBandwidth": 5,
        "DnsPolicy": "Default",
        "CreationTime": "2014-08-14T10:58Z",
        "RegionId": "cn-hangzhou-env17-d01",
        "ScalingConfigurationId": "asc-bp1ezrfgoyn5kijl****",
        "EphemeralStorage": 20,
        "HostAliases": {
            "Ip": "192.0.XX.XX",
            "Hostnames": "['hehe.com', 'haha.com']"
        },
        "AcrRegistryInfos": {
            "InstanceName": "acr-test",
            "InstanceId": "cri-nwj395hgf6f3****",
            "RegionId": "cn-hangzhou-env17-d01",
            "Domains": "*****-****-registry.cn-beijing-env17-d01.cr.aliyuncs.com"
        },
        "InitContainers": {
            "WorkingDir": "/usr/local",
            "ImagePullPolicy": "Always",
            "SecurityContextReadOnlyRootFilesystem": true,
            "Memory": 1,
            "SecurityContextRunAsUser": 587,
            "Cpu": 0.5,
            "Image": "nginx",
            "Gpu": 1,
            "Name": "test-init",
            "InitContainerVolumeMounts": {
                "MountPath": "/usr/share/",
                "ReadOnly": false,
                "SubPath": "/usr/sub/",
                "MountPropagation": "None",
                "Name": "test-empty"
            },
            "InitContainerEnvironmentVars": {
                "Value": "/usr/local/bin",
                "Key": "PATH"
}
```

弹性伸缩 ESS

```json
            },
            "SecurityContextCapabilityAdds": "NET_ADMIN",
            "InitContainerCommands": "sleep",
            "InitContainerArgs": 10
        },
        "Volumes": {
            "NFSVolumePath": "/share",
            "Type": "EmptyDirVolume",
            "FlexVolumeDriver": "alicloud/disk",
            "FlexVolumeFsType": "ext4",
            "DiskVolumeDiskId": "d-xxxx",
            "NFSVolumeServer": "3f9cd4a596-naw76.cn-shanghai-env17-
d01.nas.aliyuncs.com",
            "FlexVolumeOptions": "{\"volumeId\":\"d-
2zehdahrwoa7srg****\",\"performanceLevel\": \"PL2\"}",
            "ConfigFileVolumeDefaultMode": 644,
            "DiskVolumeDiskSize": 15,
            "EmptyDirVolumeMedium": "memory",
            "Name": "default-volume1",
            "NFSVolumeReadOnly": false,
            "DiskVolumeFsType": "xfs",
            "ConfigFileVolumeConfigFileToPaths": {
                "Path": "/usr/bin/",
                "Content": "bGl1bWk=",
                "Mode": 644
            }
        },
        "SecurityContextSysCtls": {
            "Value": 65536,
            "Name": "kernel.msgmax"
        },
        "ImageRegistryCredentials": {
            "UserName": "yourusername",
            "Server": "registry-vpc.cn-shanghai-env17-d01.aliyuncs.com",
            "Password": "yourpaasword"
        },
        "Containers": {
            "Memory": 2,
            "ReadinessProbeTcpSocketPort": 8888,
            "Cpu": 2,
            "ReadinessProbeHttpGetPath": "/usr/local",
            "ReadinessProbeHttpGetScheme": "HTTP",
            "Image": "mysql",
            "Gpu": 1,
            "StdinOnce": true,
            "LivenessProbeTimeoutSeconds": 10,
            "Name": "nginx",
            "LivenessProbeHttpGetScheme": "HTTP",
            "LivenessProbeFailureThreshold": 3,
            "LivenessProbeHttpGetPath": "/usr/nginx/",
            "LivenessProbeInitialDelaySeconds": 10,
            "SecurityContextRunAsUser": 1000,
            "Tty": false,
            "LivenessProbeTcpSocketPort": 80,
"ReadinessProbePeriodSeconds":1,
```

弹性伸缩 ESS

```json
            ReadinessProbePeriodSeconds: 1,
            "LivenessProbePeriodSeconds": 1,
            "LivenessProbeSuccessThreshold": 1,
            "ReadinessProbeInitialDelaySeconds": 5,
            "ReadinessProbeSuccessThreshold": 1,
            "ReadinessProbeFailureThreshold": 3,
            "ReadinessProbeHttpGetPort": 80,
            "Stdin": true,
            "WorkingDir": "/usr/local/nginx",
            "ImagePullPolicy": "Always",
            "LivenessProbeHttpGetPort": 80,
            "ReadinessProbeTimeoutSeconds": 5,
            "EnvironmentVars": {
                "Value": "/usr/bin/",
                "Key": "PATH"
            },
            "Ports": {
                "Port": 8888,
                "Protocol": "TCP"
            },
            "VolumeMounts": {
                "MountPath": "/pod/data",
                "ReadOnly": false,
                "SubPath": "data2/",
                "MountPropagation": "None",
                "Name": "default-volume1"
            },
            "Commands": "sleep",
            "LivenessProbeExecCommands": "cat/tmp/healthy",
            "Args": 10,
            "ReadinessProbeExecCommands": "cat/tmp/healthy",
            "SecurityContextCapabilityAdds": "NET_ADMIN"
        },
        "DnsConfigOptions": {
            "Value": "value",
            "Name": "name"
        },
        "Tags": {
            "Value": 3,
            "Key": "version"
        },
        "DnsConfigNameServers": "172.10.*.**",
        "DnsConfigSearches": "svc.local.kubenetes",
        "NtpServers": "ntp.cloud.aliyuncs.com"
    }
}
```

#### ModifyEciScalingConfiguration

调用ModifyEciScalingConfiguration修改一个ECI类型的伸缩配置。

**接口说明**

如果修改伸缩配置的名称，请注意同一伸缩组下不能存在名称相同的伸缩配置。 弹性伸缩 ESS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyEciScaling Configuration | 系统规定参数。取值： ModifyEciScalingConfiguration。 |
| ScalingConfigura tionId | String | 是 | asc- bp16har3jpj6fjb x**** | 待修改伸缩配置的ID。 |
| ContainerGroup Name | String | 否 | nginx-test | ECI实例名称，即容器组名称。格式要求如下： 长度为2~128个字符。 支持英文小写字母、数字或者短划线 （-），不能以短划线（-）开头或者结尾。 |
| ScalingConfigura tionName | String | 否 | test-modify | 伸缩配置的名称。长度为2~64个英文或中文字符，以数字、大小写字母或中文开头，可包含数字、下划线（ ）、短划线 _ （-）或半角句号（.）。 在同一地域下同一伸缩组内伸缩配置名称唯一。如果您没有指定该参数，则默认使用伸缩配置的ID。 |
| SecurityGroupId | String | 否 | sg- uf66jeqopgqa9h dn**** | ECI实例所属的安全组ID。同一个安全组内的ECI实例之间可以互相访问。 如果没有指定安全组，系统将自动使用您选择的地域下的默认安全组，您需要确保该安全组的入方向规则中包含容器需要暴露的协议和端口。如果您在该地域下没有默认安全组，系统将自动创建一个默认安全组，并将您声明的容器协议和端口添加到该安全组的入方向规则中。 |
| RestartPolicy | String | 否 | Always | 实例重启策略。取值范围： Always：总是重启。 Never：从不重启。 OnFailure：失败时重启。 默认值：Always。 |
| Cpu | Float | 否 | 1.0 | 实例级别vCPU大小。单位：核。 |
| Memory | Float | 否 | 2.0 | 实例级别内存大小。单位：GiB。 |

弹性伸缩 ESS

| DnsPolicy | String | 否 | Default | DNS策略。取值范围： None：使用DnsConfig字段设置的 DNS。 Default：继承运行环境的DNS设置。 |
|---|---|---|---|---|
| ImageSnapshotI d | String | 否 | imc- 2zebxkiifuyzzlhl* *** | 镜像缓存ID。 |
| RamRoleName | String | 否 | RamTestRole | 实例RAM角色名称。ECI与ECS共用实例 RAM角色，更多信息，请参见云服务器 ECS的通过API使用实例RAM角色章节。 |
| TerminationGrac ePeriodSeconds | Long | 否 | 60 | 程序的缓冲时间，用于处理关闭之前的操作。 |
| AutoMatchImage Cache | Boolean | 否 | false | 是否自动匹配镜像缓存。 默认值：false。 |
| Ipv6AddressCou nt | Integer | 否 | 1 | IPv6地址数。固定为1，即一个ECI实例支持绑定一个IPv6地址。 |
| ActiveDeadlineS econds | Long | 否 | 1000 | 有效期限。单位为秒。 |
| AutoCreateEip | Boolean | 否 | true | 是否自动创建弹性公网IP，并绑定ECI实例。 |
| EipBandwidth | Integer | 否 | 5 | 弹性公网IP的带宽。 默认值：5 Mbit/s。 |
| HostName | String | 否 | test | 主机名称，即容器组名称。 |
| IngressBandwidt h | Long | 否 | 1024000 | 入方向带宽限制。单位：Byte。 |
| EgressBandwidt h | Long | 否 | 1024000 | 出方向带宽限制。单位：Byte。 |
| CpuOptionsCore | Integer | 否 | 2 | CPU物理核心数。仅部分规格支持自定义设置。更多信息，请参见弹性容器实例中的自定义CPU选项章节。 |
| CpuOptionsThre adsPerCore | Integer | 否 | 2 | 每核线程数。仅部分规格支持自定义设置。配置为1时表示关闭超线程。更多信息，请参见弹性容器实例中的自定义CPU 选项章节。 |

弹性伸缩 ESS

| EphemeralStora ge | Integer | 否 | 20 | 临时存储空间大小。单位：GiB。 |
|---|---|---|---|---|
| LoadBalancerWe ight | Integer | 否 | 50 | ECI实例作为负载均衡后端服务器时的权重，取值范围：1~100。 默认值：50。 |
| Tag.N.Key | String | 否 | version | 实例的标签键。N的取值范围：1~20。 如果传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Tag.N.Value | String | 否 | 3 | 实例的标签值。N的取值范围：1~20。 如果传入该值，则允许为空字符串。最多支持128个字符，不能以 acs: 开头， 不能包含 http:// 或者 https:// 。 |
| ImageRegistryCr edential.N.Passw ord | String | 否 | yourpaasword | 镜像仓库密码。 |
| ImageRegistryCr edential.N.Serve r | String | 否 | registry-vpc.cn- shanghai-env17- d01.aliyuncs.co m | 镜像仓库注册地址。 |
| ImageRegistryCr edential.N.UserN ame | String | 否 | yourusername | 镜像仓库用户名。 |
| Container.N.Rea dinessProbe.Tim eoutSeconds | Integer | 否 | 1 | 检查超时的时间，默认值为1秒，最小值为 1秒。 |
| Container.N.Rea dinessProbe.Suc cessThreshold | Integer | 否 | 1 | 从上次检查失败后重新认定检查成功的检查次数阈值（必须是连续成功），默认值为1。当前值必须为1。 |
| Container.N.Sec urityContext.Cap ability.Add.N | RepeatL ist | 否 | NET ADMIN _ | 为容器内的进程授予某些特定的权限。目前仅支持配置为 NET ADMIN 和 NET RAW 。 _ _ 说明 NET RAW 默认不支 _ 持，需提交工单申请。 |
| Container.N.Rea dinessProbe.Tcp Socket.Port | Integer | 否 | 8000 | 使用TCP Socket方式进行健康检查时，TCP Socket检测的端口。 |

|  | http:// |
|---|---|
| https:// |  |

弹性伸缩 ESS

| Container.N.Rea dinessProbe.Htt pGet.Scheme | String | 否 | HTTP | 使用HTTP请求方式进行健康检查时，HTTP Get请求对应的协议类型，取值范围： HTTP。 HTTPS。 |
|---|---|---|---|---|
| Container.N.Live nessProbe.Perio dSeconds | Integer | 否 | 5 | 检查执行的周期，默认为值10秒，最小值为1秒。 |
| Container.N.Port .N.Protocol | String | 否 | TCP | 协议类型。取值范围： TCP。 UDP。 |
| Container.N.Port .N.Port | Integer | 否 | 80 | 端口号。取值范围：1~65535。 |
| Container.N.Sec urityContext.Rea dOnlyRootFilesy stem | Boolean | 否 | true | 容器运行的根文件系统是否为只读，目前仅支持配置为 true 。 |
| Container.N.Envi ronmentVar.N.K ey | String | 否 | PATH | 环境变量名。长度为1~128位，格式要求： [0-9a-zA-Z] ，以及下划线，不能以数字开头。 |
| Container.N.Envi ronmentVar.N.V alue | String | 否 | /usr/local/bin | 环境变量值。长度为0~256位。 |
| Container.N.Live nessProbe.TcpSo cket.Port | Integer | 否 | 8000 | 使用TCP Socket方式进行健康检查时，TCP Socket检测的端口。 |
| Container.N.Tty | Boolean | 否 | false | 是否开启交互。默认为false。 当 Command 为 /bin/bash 命令时，需要设置为 true 。 |
| Container.N.Wor kingDir | String | 否 | /usr/local/ | 容器工作目录。 |
| Container.N.Live nessProbe.HttpG et.Scheme | String | 否 | HTTP | 使用HTTP请求方式进行健康检查时，HTTP Get请求对应的协议类型，取值范围： HTTP。 HTTPS。 |
| Container.N.Rea dinessProbe.Htt pGet.Port | Integer | 否 | 8080 | 使用HTTP请求方式进行健康检查时，HTTP Get请求检测的端口号。 |

|  | /bin/bash |
|---|---|
| true |  |

弹性伸缩 ESS

| Container.N.Arg. N | RepeatL ist | 否 | 100 | 容器启动命令对应的参数。最多10个。 |
|---|---|---|---|---|
| Container.N.Gpu | Integer | 否 | 1 | 指定容器使用的GPU个数。 |
| Container.N.Rea dinessProbe.Initi alDelaySeconds | Integer | 否 | 3 | 检查开始执行的时间，以容器启动完成为起点计算。 |
| Container.N.Stdi n | Boolean | 否 | false | 此容器是否应在容器运行时为标准输入分配缓冲区。如果未设置，则容器中标准输入的读取值将导致EOF。 默认值：false。 |
| Container.N.Me mory | Float | 否 | 0.5 | 容器内存大小。单位：GiB。 |
| Container.N.Na me | String | 否 | nginx | 容器镜像名称。 |
| Container.N.Ima ge | String | 否 | registry-vpc.cn- hangzhou- env17- d01.aliyuncs.co m/eci open/ngin _ x:latest | 容器镜像。 |
| Container.N.Live nessProbe.Initial DelaySeconds | Integer | 否 | 5 | 检查开始执行的时间，以容器启动完成为起点计算。 |
| Container.N.Volu meMount.N.Mou ntPropagation | String | 否 | None | 数据卷的挂载传播设置。挂载传播允许将 Container挂载的卷共享到同一Pod中的其他Container，甚至可以共享到同一节点上的其他Pod。取值范围： None：该卷不感知任何后续在此卷或其子目录上执行的挂载操作。 HostToCotainer：该卷将会感知到后续在此卷或其子目录上的挂载操作。 Bidirectional：和HostToCotainer类似，能感知挂载操作。另外，该卷将被传播回主机和使用同一卷的所有Pod的所有容器。 默认值：None。 |
| Container.N.Volu meMount.N.Mou ntPath | String | 否 | /pod/data | 容器挂载数据卷的目录。 重要容器挂载目录下的内容会被Volume的内容直接覆盖，请您谨慎使用。 |

弹性伸缩 ESS

| Container.N.Volu meMount.N.Rea dOnly | Boolean | 否 | false | 数据卷是否只读。 默认值：false。 |
|---|---|---|---|---|
| Container.N.Volu meMount.N.Nam e | String | 否 | default-volume1 | 数据卷名称。同Volume中的Name。 |
| Container.N.Volu meMount.N.Sub Path | String | 否 | data2/ | 数据卷子路径。 |
| Container.N.Live nessProbe.Failur eThreshold | Integer | 否 | 3 | 从上次检查成功后认定检查失败的检查次数阈值（必须是连续失败）。 默认值：3。 |
| Container.N.Rea dinessProbe.Exe c.Command.N | RepeatL ist | 否 | cat/tmp/healthy | 使用命令行方式进行健康检查时，在容器内执行的命令。 |
| Container.N.Rea dinessProbe.Fail ureThreshold | Integer | 否 | 3 | 从上次检查成功后认定检查失败的检查次数阈值（必须是连续失败）。 默认值：3。 |
| Container.N.Ima gePullPolicy | String | 否 | Always | 容器的镜像拉取策略。可能值： Alway：总是拉取。每次都拉取镜像。 IfNotPresent：按需拉取。优先使用本地镜像，本地没有镜像时则拉取镜像。 Never：从不拉取。使用本地镜像，不拉取镜像。 |
| Container.N.Stdi nOnce | Boolean | 否 | false | 当标准输入为true时，标准输入流将在多个附加会话中是否保持开启状态。 如果 StdinOnce 设为true，标准输入在容器开启时被打开，在首个客户端附加到标准输入之前都为空，然后会一直保持开启状态，接收数据，直到客户端连接断开，此时标准输入被关闭，在容器重启前一直保持关闭状态。 |
| Container.N.Cpu | Float | 否 | 0.25 | 容器的vCPU大小。单位：核。 |
| Container.N.Live nessProbe.HttpG et.Port | Integer | 否 | 8888 | 使用HTTP请求方式进行健康检查时，HTTP Get请求检测的端口号。 |
| Container.N.Live nessProbe.HttpG et.Path | String | 否 | /healthyz | 使用HTTP请求方式进行健康检查时，HTTP Get请求检测的路径。 |

弹性伸缩 ESS

| Container.N.Live nessProbe.Succe ssThreshold | Integer | 否 | 1 | 从上次检查失败后重新认定检查成功的检查次数阈值（必须是连续成功），当前值仅支持设置为1。 默认值：1。 |
|---|---|---|---|---|
| Container.N.Rea dinessProbe.Peri odSeconds | Integer | 否 | 3 | 检查执行的周期，默认值为10秒，最小值为1秒。 |
| Container.N.Live nessProbe.Time outSeconds | Integer | 否 | 1 | 检查超时的时间，默认值为1秒，最小值为 1秒。 |
| Container.N.Co mmand.N | RepeatL ist | 否 | sleep | 容器启动命令。最多20个。每个命令最多包含256个字符。 |
| Container.N.Sec urityContext.Run AsUser | Long | 否 | 1000 | 设置运行容器的用户ID。 |
| Container.N.Rea dinessProbe.Htt pGet.Path | String | 否 | /healthz | 使用HTTP请求方式进行健康检查时，HTTP Get请求检测的路径。 |
| Container.N.Live nessProbe.Exec. Command.N | RepeatL ist | 否 | cat /tmp/healthy | 使用命令行方式进行健康检查时，在容器内执行的命令。 |
| Volume.N.Type | String | 否 | EmptyDirVolum e | 数据卷类型，取值范围： EmptyDirVolume：EmptyDir类型的数据卷，表示空目录。 NFSVolume：NFS类型的数据卷，表示网络文件系统。 ConfigFileVolume：ConfigFile类型的数据卷，表示配置文件。 FlexVolume：使用FlexVolume插件扩展存储类型，支持挂载云盘。 HostPathVolume：HostPath类型的数据卷，表示主机节点的文件或目录。 DiskVolume（不推荐）：云盘数据卷。建议使用FlexVolume挂载云盘。 |
| Volume.N.DiskV olume.DiskSize | Integer | 否 | 15 | DiskVolume的大小。单位：GiB。 |
| Volume.N.NFSVo lume.Path | String | 否 | /share | NFS数据卷路径。 |
| Volume.N.FlexVo lume.FsType | String | 否 | ext4 | 挂载的文件系统类型，默认取决于 FlexVolume的script。 |
| Volume.N.DiskV olume.FsType | String | 否 | xfs | DiskVolume的系统类型。 |

弹性伸缩 ESS

| Volume.N.HostP athVolume.Type | String | 否 | Directory | HostPath Volume的类型。取值范围： Directory：目录。 File：文件。 |
|---|---|---|---|---|
| Volume.N.NFSVo lume.ReadOnly | Boolean | 否 | false | NFS数据卷是否只读。 默认值：false。 |
| Volume.N.HostP athVolume.Path | String | 否 | /xx/xx/name | HostPath Volume在主机上的目录路径。 |
| Volume.N.FlexVo lume.Options | String | 否 | {"volumeId":"d- 2zehdahrwoa7sr g****","perform anceLevel": "PL2"} | FlexVolume对象选项列表。为KV形式， 采用JSON传递。 例如通过FlexVolume挂载云盘时，Options表示云盘的配置参数，可配置的参数如下： volumeId：已有云盘ID。 volumeSize：云盘大小，单位为GiB。 取值范围为20~32768。 performanceLevel：云盘性能等级。 更多信息，请参见云服务器ECS用户指南中的云盘概述章节。 deleteWithInstance：是否随实例释放，默认为false。 encrypted：是否加密云盘，默认为 false。更多信息，请参见云服务器ECS 指南中的加密概述章节。 kmsKeyId：加密云盘时，云盘使用的 KMS密钥ID。 |
| Volume.N.FlexVo lume.Driver | String | 否 | flexvolume | 使用FlexVolume插件挂载数据卷时的驱动类型。目前支持alicloud/disk，表示挂载阿里云云盘。 |
| Volume.N.Config FileVolumeDefau ltMode | Integer | 否 | 0644 | ConfigFileVolume默认的权限。 |
| Volume.N.NFSVo lume.Server | String | 否 | 3f9cd4a596- naw76.cn- shanghai-env17- d01.nas.aliyuncs .com | NFS服务器地址。 |
| Volume.N.DiskV olume.DiskId | String | 否 | d-xx | DiskVolume的ID。 |
| Volume.N.Name | String | 否 | default-volume1 | 数据卷名称。 |
| Volume.N.Empty DirVolume.Medi um | String | 否 | memory | EmptyDirVolume的存储媒介，默认为空，使用node文件系统；如果设置为 memory时，则表示使用内存。 |

弹性伸缩 ESS

| Volume.N.Config FileVolumeConfi gFileToPath.N.Pa th | String | 否 | /usr/bin/ | 相对文件路径。 |
|---|---|---|---|---|
| Volume.N.Config FileVolumeConfi gFileToPath.N.M ode | Integer | 否 | 0644 | ConfigFileVolume目录权限。 |
| Volume.N.Config FileVolumeConfi gFileToPath.N.Co ntent | String | 否 | bGl1bWk= | 配置文件内容。其中配置文件大小最大为 32 KB。 |
| InitContainer.N.I nitContainerEnvi ronmentVar.N.K ey | String | 否 | Path | 环境变量名。长度为1~128位。格式要求： 0-9a-zA-Z ，以及下划线，不能以数字开头。 |
| InitContainer.N.I nitContainerEnvi ronmentVar.N.V alue | String | 否 | /usr/bin/ | 环境变量值。长度为0~256位。 |
| InitContainer.N.S ecurityContext.C apability.Add.N | RepeatL ist | 否 | NET ADMIN _ | 为容器内的进程授予某些特定的权限。目前仅支持配置为 NET ADMIN 和 NET RAW 。 _ _ 说明 NET RAW 默认不支 _ 持，需提交工单申请。 |
| InitContainer.N.I mage | String | 否 | nginx | 容器使用的镜像。 |
| InitContainer.N.I nitContainerVolu meMount.N.Mou ntPath | String | 否 | /usr/share/ | 挂载目录。 重要容器挂载目录下的内容会被Volume的内容直接覆盖，请您谨慎使用。 |
| InitContainer.N.I nitContainerVolu meMount.N.Mou ntPropagation | String | 否 | None | 数据卷的挂载传播设置。挂载传播允许将 Container挂载的卷共享到同一Pod中的其他Container，甚至可以共享到同一节点上的其他Pod。取值范围： None：该卷不感知任何后续在此卷或其子目录上执行的挂载操作。 HostToCotainer：该卷将会感知到后续在此卷或其子目录上的挂载操作。 Bidirectional：和HostToCotainer类似，能感知挂载操作。另外，该卷将被传播回主机和使用同一卷的所有Pod的所有容器。 默认值：None。 |

弹性伸缩 ESS

| InitContainer.N.I nitContainerVolu meMount.N.Rea dOnly | Boolean | 否 | false | 挂载路径是否只读。 默认值：false。 |
|---|---|---|---|---|
| InitContainer.N.I nitContainerVolu meMount.N.Nam e | String | 否 | test-empty | 挂载数据卷的名称。 |
| InitContainer.N.I nitContainerVolu meMount.N.Sub Path | String | 否 | /usr/sub/ | 数据卷下的子目录，方便Pod将同一个 Volume下不同目录挂载到容器不同目录。 |
| InitContainer.N.I magePullPolicy | String | 否 | Always | 镜像拉取策略。取值范围： Always：总是拉取。每次都拉取镜像。 IfNotPresent：按需拉取。优先使用本地镜像，本地没有镜像时则拉取镜像。 Never：从不拉取。使用本地镜像，不拉取镜像。 |
| InitContainer.N. Cpu | Float | 否 | 0.5 | 容器的vCPU大小。单位：核。 |
| InitContainer.N. WorkingDir | String | 否 | /usr/local | 工作目录。 |
| InitContainer.N. Command.N | RepeatL ist | 否 | sleep | 容器启动指令。 |
| InitContainer.N. Arg.N | RepeatL ist | 否 | 10 | 容器启动参数。 |
| DnsConfigOption .N.Name | String | 否 | name | 对象变量名。 |
| InitContainer.N. Gpu | Integer | 否 | 1 | 指定容器使用的GPU个数。 |
| InitContainer.N. Memory | Float | 否 | 1.0 | 容器的内存大小。单位：GiB。 |
| InitContainer.N. Name | String | 否 | test-init | 容器名称。 |
| DnsConfigName Server.N | RepeatL ist | 否 | 172.10.*.** | DNS服务器的IP地址列表。 |
| DnsConfigSearc h.N | RepeatL ist | 否 | svc.local.kubene tes | DNS搜索域列表。 |
| DnsConfigOption .N.Value | String | 否 | value | 对象变量值。 |
| InitContainer.N.S ecurityContext.R unAsUser | Long | 否 | 587 | 设置运行容器的用户ID。 |

| 开发指南·API参考 |  |  |  | 弹性伸缩 ES |
|---|---|---|---|---|

| HostAliase.N.Ip | String | 否 | 192.0.XX.XX | 添加IP地址。 |
|---|---|---|---|---|
| HostAliase.N.Hos tname.N | RepeatL ist | 否 | ['hehe.com', 'haha.com'] | 添加主机名。 |
| SecurityContext Sysctl.N.Value | String | 否 | 65536 | 实例运行的安全上下文的变量值。 |
| AcrRegistryInfo. N.Domain.N | RepeatL ist | 否 | *****-****- registry.cn- beijing-env17- d01.cr.aliyuncs.c om | ACR企业版实例的域名。默认为相应实例的所有域名。支持指定个别域名，多个以半角逗号（,）分隔。 |
| NtpServer.N | RepeatL ist | 否 | ntp.cloud.aliyun cs.com | NTP服务器。 |
| SecurityContext Sysctl.N.Name | String | 否 | kernel.msgmax | 实例运行的安全上下文系统名称。 |
| AcrRegistryInfo. N.InstanceName | String | 否 | acr-test | ACR企业版实例的名称。 |
| AcrRegistryInfo. N.RegionId | String | 否 | cn-hangzhou- env17-d01 | ACR企业版实例所属地域。 |
| AcrRegistryInfo. N.InstanceId | String | 否 | cri- nwj395hgf6f3*** * | ACR企业版实例ID。 |
| CostOptimizatio n | Boolean | 否 | false | 是否开启成本优化开关。取值范围： true：开启。 false：未开启。 默认值：false。 |

弹性伸缩 ESS

| InstanceFamilyL evel | String | 否 | EnterpriseLevel | 实例规格族级别，用于筛选符合要求的实例规格范围，当CostOptimization开启时生效。取值范围： EntryLevel：入门级，即共享型实例规格。成本更低，但是无法保证实例计算性能的稳定。适用于平时CPU使用率低的业务场景。更多信息，请参见云服务器ECS中的共享型。 EnterpriseLevel：企业级。性能稳定且资源独享，适用于对稳定性要求高的业务场景。更多信息，请参见云服务器 ECS中的实例规格族。 CreditEntryLevel：积分入门级，即突发性能实例。通过CPU积分来保证计算性能，适用于平时CPU使用率低、偶有突发CPU使用率的业务场景。更多信息，请参见云服务器ECS中的突发性能实例概述。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 89945DD3-9072- 47D0-A318- 353284CF**** | 请求ID，唯一标识。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=ModifyEciScalingConfiguration &ScalingConfigurationId=asc-bp16har3jpj6fjbx**** &ScalingConfigurationName=test-modify &SecurityGroupId=sg-uf66jeqopgqa9hdn**** &ContainerGroupName=nginx-test &RestartPolicy=Always &Cpu=1.0 &Memory=2.0 &DnsPolicy=Default &ImageSnapshotId=imc-2zebxkiifuyzzlhl**** &RamRoleName=RamTestRole &TerminationGracePeriodSeconds=60 &AutoMatchImageCache=false &Ipv6AddressCount=1 &ActiveDeadlineSeconds=1000 &AutoCreateEip=true &EipBandwidth=5 &HostName=test &IngressBandwidth=1024000 &EgressBandwidth=1024000 &CpuOptionsCore=2 &CpuOptionsThreadsPerCore=2 &EphemeralStorage=20 &LoadBalancerWeight=50 &Tag=[{"Key":"version","Value":"3"}]
```

弹性伸缩 ESS

```json
&ImageRegistryCredential=[{"Password":"yourpaasword","Server":"registry-vpc.cn-shanghai -env17-d01.aliyuncs.com","UserName":"yourusername"}] &Container= [{"ReadinessProbe.TimeoutSeconds":1,"ReadinessProbe.SuccessThreshold":1,"SecurityContext. pability.Add": ["NET_ADMIN"],"ReadinessProbe.TcpSocket.Port":8000,"ReadinessProbe.HttpGet.Scheme":"HTTP" LivenessProbe.PeriodSeconds":5,"Port": [{"Protocol":"TCP","Port":80}],"SecurityContext.ReadOnlyRootFilesystem":true,"Environment r": [{"Key":"PATH","Value":"/usr/local/bin"}],"LivenessProbe.TcpSocket.Port":8000,"Tty":false WorkingDir":"/usr/local/","LivenessProbe.HttpGet.Scheme":"HTTP","ReadinessProbe.HttpGet.P t":8080,"Arg": ["100"],"Gpu":1,"ReadinessProbe.InitialDelaySeconds":3,"Stdin":false,"Memory":0.5,"Name": ginx","Image":"registry-vpc.cn-hangzhou-env17d01.aliyuncs.com/eci_open/nginx:latest","LivenessProbe.InitialDelaySeconds":5,"VolumeMoun :[{"MountPropagation":"None","MountPath":"/pod/data","ReadOnly":false,"Name":"default-v olume1","SubPath":"data2/"}],"LivenessProbe.FailureThreshold":3,"ReadinessProbe.Exec.Comm d": ["cat/tmp/healthy"],"ReadinessProbe.FailureThreshold":3,"ImagePullPolicy":"Always","Stdin ce":false,"Cpu":0.25,"LivenessProbe.HttpGet.Port":8888,"LivenessProbe.HttpGet.Path":"/hea hyz","LivenessProbe.SuccessThreshold":1,"ReadinessProbe.PeriodSeconds":3,"LivenessProbe.T eoutSeconds":1,"Command": ["sleep"],"SecurityContext.RunAsUser":1000,"ReadinessProbe.HttpGet.Path":"/healthz","Live ssProbe.Exec.Command":["cat /tmp/healthy"]}] &Volume= [{"Type":"EmptyDirVolume","DiskVolume.DiskSize":15,"NFSVolume.Path":"/share","FlexVolume. Type":"ext4","DiskVolume.FsType":"xfs","HostPathVolume.Type":"Directory","NFSVolume.ReadO y":false,"HostPathVolume.Path":"/xx/xx/name","FlexVolume.Options":"{\"volumeId\":\"d-2z ehdahrwoa7srg****\",\"performanceLevel\": \"PL2\"}","FlexVolume.Driver":"flexvolume","ConfigFileVolumeDefaultMode":644,"NFSVolume.S ver":"3f9cd4a596-naw76.cn-shanghai-env17-d01.nas.aliyuncs.com","DiskVolume.DiskId":"d-x x","Name":"defaultvolume1","EmptyDirVolume.Medium":"memory","ConfigFileVolumeConfigFileToPath":[{"Path":" /usr/bin/","Mode":644,"Content":"bGl1bWk="}]}] &InitContainer=[{"InitContainerEnvironmentVar": [{"Key":"Path","Value":"/usr/bin/"}],"SecurityContext.Capability.Add": ["NET_ADMIN"],"Image":"nginx","InitContainerVolumeMount": [{"MountPropagation":"None","MountPath":"/usr/share/","ReadOnly":false,"Name":"test-emp ty","SubPath":"/usr/sub/"}],"ImagePullPolicy":"Always","Cpu":0.5,"WorkingDir":"/usr/local "Command":["sleep"],"Arg": ["10"],"SecurityContext.RunAsUser":587,"Gpu":1,"Memory":1.0,"Name":"test-init"}] &DnsConfigNameServer=["172.10.*.**"] &DnsConfigSearch=["svc.local.kubenetes"] &DnsConfigOption=[{"Value":"value","Name":"name"}] &HostAliase=[{"Ip":"192.0.XX.XX","Hostname":["['hehe.com', 'haha.com']"]}] &SecurityContextSysctl=[{"Value":"65536","Name":"kernel.msgmax"}] &NtpServer=["ntp.cloud.aliyuncs.com"] &AcrRegistryInfo=[{"Domain":["*****-****-registry.cn-beijing-env17d01.cr.aliyuncs.com"],"InstanceName":"acr-test","InstanceId":"crinwj395hgf6f3****","RegionId":"cn-hangzhou-env17-d01"}] &CostOptimization=false &InstanceFamilyLevel=EnterpriseLevel
```

`&<`公共请求参数> 弹性伸缩 ESS 正常返回示例 `XML` 格式

```xml
      <RequestId>89945DD3-9072-47D0-A318-353284CF****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "89945DD3-9072-47D0-A318-353284CF****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 未授权操作当前Action。 |
| 404 | InvalidDataDiskSnapsh otId.NotFound | Snapshot "XXX" does not exist. | 不存在指定的快照。 |
| 400 | InvalidDataDiskSnapsh otId.SizeNotSupported | The capacity of snapshot "XXX" exceeds the size limit of the specified disk category. | 指定快照的大小超过了磁盘大小的限制。 |
| 404 | InvalidImageId.NotFou nd | The specified image does not exist. | 指定的镜像不存在。 |
| 400 | InvalidKeyPairName.N otFound | The specified KeyPairName does not exist in our records. | 指定的KeyPairName不存在。 |
| 400 | InvalidNetworkType.Fo rRAMRole | RAMRole can't be used For classic instance. | 经典网络实例不支持 RamRoleName参数。 |
| 400 | InvalidParamter | The specified value of parameter is not valid. | 指定的参数值无效。 |
| 400 | InvalidScalingConfigur ationName.Duplicate | The specified value of parameter is duplicated. | 伸缩配置名已存在。 |

弹性伸缩 ESS

| 400 | InvalidSecurityGroupId .IncorrectNetworkType | The network type of specified Security Group does not support this action. | 指定的安全组与伸缩组指定网络类型不一致。 |
|---|---|---|---|
| 400 | InvalidSecurityGroupId .VPCMismatch | The specified security group and the specified virtual switch are not in the same VPC. | 指定的安全组和虚拟交换机不属于同一个虚拟专有网络。 |
| 400 | InvalidTags.KeyValue | The specified tags key/value cannot be empty. | 必须指定Tags参数。 |
| 400 | InvalidTags.ListSize | The specified tags list size cannot be more than "20". | Tags列表长度超过限制长度。 |
| 400 | InvalidUserData.Base6 4FormatInvalid | The specified parameter UserData must be base64 encoded. | UserData不符合Base64 编码规范。 |
| 400 | InvalidUserData.SizeEx ceeded | The specified parameter UserData exceeds the size. | 指定的UserData过长。 |

#### DeleteEciScalingConfiguration

调用DeleteEciScalingConfiguration删除一个ECI类型的伸缩配置。

**接口说明**

以下情况不能删除伸缩配置： 伸缩配置在伸缩组中处于生效（Active）状态。 伸缩组中仍然存在使用该伸缩配置创建的ECI实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteEciScaling Configuration | 系统规定参数。取值： DeleteEciScalingConfiguration。 |
| ScalingConfigura tionId | String | 是 | asc- bp1bx8mzur534 edp**** | 待删除伸缩配置的ID。 |
| RegionId | String | 否 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |

弹性伸缩 ESS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 45D5B0AD-3B00- 4A9B-9911- 6D5303B0**** | 请求ID。无论调用接口成功与否，系统都会返回请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DeleteEciScalingConfiguration &ScalingConfigurationId=asc-bp1bx8mzur534edp**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>45D5B0AD-3B00-4A9B-9911-6D5303B0****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "45D5B0AD-3B00-4A9B-9911-6D5303B0****"
}
```

### 伸缩规则

#### CreateScalingRule

**接口说明**

伸缩规则定义了具体的扩张或收缩操作，例如加入或移出N台实例。 如果执行伸缩规则会造成伸缩组的ECS实例数低于MinSize或高于MaxSize，则弹性伸缩会自动调整需要加入或移出的ECS实例数，使得伸缩组的ECS实例数调整到MinSize或MaxSize，但伸缩规则的设定值不会变化。 例如，某个伸缩组，MaxSize=3，当前实例数Total Capacity=2，伸缩规则指定加3台ECS实例，则在实际执行过程中只会加1台ECS实例，但伸缩规则的设定值仍然为3。 例如，某个伸缩组，MinSize=2，当前实例数Total Capacity=3，伸缩规则指定减去5台ECS实例，则在实际执行过程中只会减1台ECS实例，但伸缩规则的设定值仍然为5。 根据传入参数创建伸缩规则： 当AdjustmentType是TotalCapacity时，表示将当前伸缩组的ECS实例数量调整到指定数量，对应的 AdjustmentValue值必须大于等于0。 当AdjustmentType是QuantityChangeInCapacity或PercentChangeInCapacity，对应的 AdjustmentValue值为正数表示增加实例、为负数表示减少实例。 弹性伸缩 ESS 当AdjustmentType是PercentChangeInCapacity，弹性伸缩服务以伸缩组当前实例数（Total Capacity）×AdjusmentValue/100，并使用四舍五入原则来确认增加或减少的ECS实例个数。 当伸缩规则指定了冷却时间（Cooldown），则执行该伸缩规则的伸缩活动完成后，会以伸缩规则中指定的冷却时间对伸缩组进行冷却处理，如果伸缩规则未指定冷却时间，则以伸缩组指定的冷却时间 （DefaultCooldown）为准。 一个伸缩组内最多只能创建50条伸缩规则。 返回的伸缩规则唯一标识符（ScalingRuleAri），主要可以被以下接口所使用： 在执行伸缩规则（ExecuteScalingRule）的ScalingRuleAri参数中指定，您可以手动执行该伸缩规则。 在创建定时任务（CreateScheduledTask）的ScheduledAction参数中指定，您可以定时执行该伸缩规则。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateScalingRu le | 系统规定参数，取值： CreateScalingRule。 |
| ScalingGroupId | String | 是 | asg- bp1ffogfdauy0jw 0**** | 伸缩规则所属伸缩组的ID。 |
| ScalingRuleNam e | String | 否 | scalingrule**** | 伸缩规则的名称，2~64个英文或中文字符，以数字、大小字母或中文开头，可包含数字、下划线（ ）、短划线（-）或半 _ 角句号（.）。同一账号同一地域同一伸缩组内唯一。 如果没有指定该参数，默认值为 ScalingRuleId的值。 |
| Cooldown | Integer | 否 | 60 | 伸缩规则的冷却时间，仅适用于简单伸缩规则。取值范围：0~86400，单位：秒。 默认值：空。 |
| MinAdjustmentM agnitude | Integer | 否 | 1 | 伸缩规则最小调整实例数，仅当伸缩规则类型为SimpleScalingRule或 StepScalingRule，且AdjustmentType 为PercentChangeInCapacity时生效。 |
| AdjustmentType | String | 否 | QuantityChangeI nCapacity | 伸缩规则的调整方式，仅适用于简单伸缩规则，且该项必选。取值范围： QuantityChangeInCapacity：增加或减少指定数量的ECS实例。 PercentChangeInCapacity：增加或减少指定比例的ECS实例。 TotalCapacity：将当前伸缩组的ECS 实例数量调整到指定数量。 |

弹性伸缩 ESS

| AdjustmentValu e | Integer | 否 | 100 | 伸缩规则的调整值，仅适用于简单伸缩规则，且该项必选。任何情况下，单次调整的ECS实例台数都不能超过500。不同调整方式对应的取值范围： QuantityChangeInCapacity：- 500~500。 PercentChangeInCapacity：- 100~10000。 TotalCapacity：0~1000。 |
|---|---|---|---|---|
| ScalingRuleType | String | 否 | SimpleScalingRu le | 伸缩规则类型，取值范围： SimpleScalingRule：简单伸缩规则。 根据调整方式（AdjustmentType）和调整值（AdjustmentValue）调整ECS 实例数量。 TargetTrackingScalingRule：目标追踪伸缩规则。根据预定义监控 （MetricName）项动态计算需要扩缩容的ECS实例数量，尽量将预定义监控项的指标值维持在目标值 （TargetValue）附近。 StepScalingRule：步进伸缩规则，根据阈值和指标值提供分步扩展方式。 PredictiveScalingRule：预测伸缩规则，基于机器学习能力分析伸缩组的历史监控数据预测未来监控指标值，并支持自动创建定时任务设置伸缩组边界。 默认值：SimpleScalingRule。 |
| EstimatedInstan ceWarmup | Integer | 否 | 300 | ECS实例预热时间，适用于目标追踪伸缩规则和步进伸缩规则。处于预热状态的 ECS实例将正常的加入伸缩组，但期间不会向云监控上报监控数据。 说明动态计算需要扩缩容的 ECS实例数量时，处于预热状态的 ECS实例不计入现有实例数量。 取值范围：0~86400，单位：秒。 默认值：300。 |

弹性伸缩 ESS

| MetricName | String | 否 | CpuUtilization | 预定义监控项，适用于目标追踪伸缩规则和预测规则，且此时该项必选。 目标追踪伸缩规则取值范围： CpuUtilization：平均CPU使用率。 ClassicInternetRx：经典网络公网入流量平均值。 ClassicInternetTx：经典网络公网出流量平均值。 VpcInternetRx：VPC网络公网入流量平均值。 VpcInternetTx：VPC网络公网出流量平均值。 IntranetRx：内网入流量平均值。 IntranetTx：内网出流量平均值。 预测规则取值范围： CpuUtilization：平均CPU使用率。 IntranetRx：内网入流量平均值。 IntranetTx：内网出流量平均值。 |
|---|---|---|---|---|
| TargetValue | Float | 否 | 0.125 | 目标值，适用于目标追踪伸缩规则和预测规则，且此时该项必选。TargetValue最多保留小数点后三位，且必须大于0。 |
| DisableScaleIn | Boolean | 否 | false | 是否禁用缩容，仅适用于目标追踪伸缩规则。 默认值：false。 |
| ScaleInEvaluatio nCount | Integer | 否 | 15 | 创建目标追踪规则后，会自动创建报警任务。本参数用于指定对应的缩容报警任务触发报警时，所需连续满足阈值条件的次数。 默认值：15。 |
| ScaleOutEvaluati onCount | Integer | 否 | 3 | 创建目标追踪规则后，会自动创建报警任务。本参数用于指定对应的扩容报警任务触发报警时，所需连续满足阈值条件的次数。 默认值：3。 |
| StepAdjustment. N.MetricInterval LowerBound | Float | 否 | 1.0 | 分步步骤的下边界，仅适用于步进规则， 取值范围：- 9.999999E18~9.999999E18。 |
| StepAdjustment. N.MetricInterval UpperBound | Float | 否 | 5.0 | 分步步骤的上边界，仅适用于步进规则， 取值范围：- 9.999999E18~9.999999E18。 |

弹性伸缩 ESS

| StepAdjustment. N.ScalingAdjust ment | Integer | 否 | 1 | 分步步骤对应的实例扩展数量，仅适用于步进规则。 |
|---|---|---|---|---|
| PredictiveScalin gMode | String | 否 | PredictAndScale | 预测规则的模式，取值范围： PredictAndScale：产生预测结果并创建预测任务。 PredictOnly：产生预测结果，但不会创建预测任务。 默认值：PredictAndScale。 |
| PredictiveValueB ehavior | String | 否 | MaxOverridePre dictiveValue | 预测规则最大值处理方式，取值范围： MaxOverridePredictiveValue：初始最大值会覆盖预测值。预测值大于初始最大值时，预测任务的最大值采用初始最大值。 PredictiveValueOverrideMax：预测值会覆盖初始最大值。预测值大于初始最大值时，预测任务的最大值采用预测值。 PredictiveValueOverrideMaxWithB uffer：预测值会附加一定比例。预测值会按照PredictiveValueBuffer比例增加，当增加后的值大于初始最大值时， 会采用增加后的值。 默认值： MaxOverridePredictiveValue。 |
| PredictiveValueB uffer | Integer | 否 | 50 | PredictiveValueBehavior为 PredictiveValueOverrideMaxWithBuff er时生效，预测值会按照该比例增加，当增加后的值大于初始最大值时，会采用增加后的值。取值范围：0~100。 默认值：0。 |
| PredictiveTaskB ufferTime | Integer | 否 | 30 | 预测规则自动创建的预测任务默认均在整点执行，您可以设置预启动时间提前执行预测任务，预先准备资源。取值范围： 0~60，单位：分钟。 默认值：0。 |
| InitialMaxSize | Integer | 否 | 100 | 伸缩组实例数上限，和 PredictiveValueBehavior结合使用。 默认值为伸缩组最大实例数（MaxSize的值）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
|---|---|---|---|
| ScalingRuleAri | String | ari:acs:ess:cn- hangzhou-env17- d01:14069264740 6****:scalingrule/a sr- bp1dvirgwkoowxk7 **** | 伸缩规则的唯一标识符。 |
| ScalingRuleId | String | asr- bp1dvirgwkoowxk7 **** | 伸缩规则的ID，由系统生成，全局唯一。 |

**示例**

请求示例

```
http://ess.example.com/?Action=CreateScalingRule &ScalingGroupId=asg-bp1ffogfdauy0jw0**** &AdjustmentType=QuantityChangeInCapacity &AdjustmentValue=-10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <ScalingRuleAri>ari:acs:ess:cn-hangzhou-env17-
d01:140692647406****:scalingrule/asr-bp1dvirgwkoowxk7****</ScalingRuleAri>
      <ScalingRuleId>asr-bp1dvirgwkoowxk7****</ScalingRuleId>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "ScalingRuleId": "asr-bp1dvirgwkoowxk7****",
    "ScalingRuleAri": "ari:acs:ess:cn-hangzhou-env17-
d01:140692647406****:scalingrule/asr-bp1dvirgwkoowxk7****" }
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在该账号下不存在。 |

弹性伸缩 ESS

| 400 | InvalidScalingRuleNam e.Duplicate | The specified value of parameter <parameter name> is duplicated. | 伸缩规则名字已存在。 |
|---|---|---|---|
| 400 | QuotaExceeded.Scalin gRule | Scaling rule quota exceeded in the specified scaling group. | 您的伸缩规则使用个数达到上限。 |
| 400 | TargetTrackingScaling Rule.UnsupportedMetri c | Specific metric is not supported for target tracking scaling rule. | 目标追踪伸缩规则不支持当前监控指标。 |
| 400 | TargetTrackingScaling Rule.DumplicateMetric | Only one TargetTrackingScaling rule for a given metric specification is allowed. | 一个伸缩组中，同一监控指标只能存在一条目标追踪规则。 |
| 400 | InvalidMinAdjustment MagnitudeMismatchAd justmentType | MinAdjustmentMagnitu de is not supported by the specified adjustment type. | MinAdjustmentMagnitu de不支持当前伸缩规则调整类型。 |
| 400 | InvalidStepAdjustment s.MultipleNullUpperBo und | At most one StepAdjustment may have an unspecified upper bound. | 最多只能有一个分步步骤不指定分步上界。 |
| 400 | InvalidStepAdjustment s.MultipleNullLowerBo und | At most one StepAdjustment may have an unspecified lower bound. | 最多只能有一个分步步骤不指定分步下界。 |
| 400 | InvalidStepAdjustment s.NoNullLowerBound | There must be a StepAdjustment with an unspecified lower bound when one StepAdjustment has a negative lower bound. | 当存在一个分步下界为负数时，则必须有一个未指定分步下界的分步步骤。 |
| 400 | InvalidStepAdjustment s.NoNullUpperBound | There must be a StepAdjustment with an unspecified upper bound when one StepAdjustment has a positive upper bound. | 当存在一个正数的分步上界时，则必有一个未指定分步上界的分步步骤。 |

弹性伸缩 ESS

| 400 | InvalidStepAdjustment s.Gap | StepAdjustment intervals can not have gaps between them. | 分步步骤之间不能有间隔。 |
|---|---|---|---|
| 400 | InvalidStepAdjustment s.Overlap | StepAdjustment intervals can not overlap. | 分步步骤之间不能重叠。 |
| 400 | InvalidStepAdjustment s.LowerGtUpper | LowerBound must be less than the UpperBound for StepAdjustment :%s. | 同一分步步骤中，分步下界必须小于分步上界。 |
| 400 | InvalidStepAdjustment s.BothNull | Both lower and upper bounds of a StepAdjustment can not be left unspecified. | 同一分步步骤中，分步上界和分步下界不能同时不指定。 |
| 400 | InvalidStepAdjustment s.MaxNum | Your scaling rule can have at most %s StepAdjustments. | 同一伸缩组中分步步骤数量超过阈值。 |
| 400 | StepBeyondPermitRan ge | Specific parameter "%s" beyond permit range. | 分步步骤的上界或下界超过了可选范围。 |

#### ModifyScalingRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyScalingRu le | 系统规定参数，取值： ModifyScalingRule。 |
| ScalingRuleId | String | 是 | eMKWG8SRNb9 dBLAjweN**** | 待修改伸缩规则的ID。 |
| ScalingRuleNam e | String | 否 | scalingrule**** | 伸缩规则的显示名称，2~64个英文或中文字符，以数字、大小字母或中文开头，可包含数字、下划线（ ）、短划线（-）或 _ 半角句号（.）。同一账号同一地域同一伸缩组内唯一。 |
| Cooldown | Integer | 否 | 60 | 伸缩规则的冷却时间，仅适用于简单伸缩规则。 取值范围：0~86400，单位：秒。 |

弹性伸缩 ESS

| MinAdjustmentM agnitude | Integer | 否 | 1 | 伸缩规则最小调整实例数，仅当伸缩规则类型为SimpleScalingRule或 StepScalingRule，且AdjustmentType 为PercentChangeInCapacity时生效。 |
|---|---|---|---|---|
| AdjustmentType | String | 否 | QuantityChangeI nCapacity | 伸缩规则的调整方式，仅适用于简单伸缩规则。取值范围： QuantityChangeInCapacity：增加或减少指定数量的ECS实例。 PercentChangeInCapacity：增加或减少指定比例的ECS实例。 TotalCapacity：将当前伸缩组的ECS 实例数量调整到指定数量。 |
| AdjustmentValu e | Integer | 否 | 100 | 伸缩规则的调整值，仅适用于简单伸缩规则。任何情况下，单次调整的ECS实例台数都不能超过500。不同调整方式对应的取值范围： QuantityChangeInCapacity：- 500~500。 PercentChangeInCapacity：- 100~10000。 TotalCapacity：0~1000。 |
| EstimatedInstan ceWarmup | Integer | 否 | 60 | ECS实例预热时间，适用于目标追踪伸缩规则和步进伸缩规则。处于预热状态的 ECS实例将正常的加入伸缩组，但期间不会向云监控上报监控数据。 说明动态计算需要扩缩容的 ECS实例数量时，处于预热状态的 ECS实例不计入现有实例数量。 取值范围：0~86400，单位：秒。 |

弹性伸缩 ESS

| MetricName | String | 否 | CpuUtilization | 预定义监控项，适用于目标追踪伸缩规则和预测规则，且此时该项必选。 目标追踪伸缩规则取值范围： CpuUtilization：平均CPU使用率。 ClassicInternetRx：经典网络公网入流量平均值。 ClassicInternetTx：经典网络公网出流量平均值。 VpcInternetRx：VPC网络公网入流量平均值。 VpcInternetTx：VPC网络公网出流量平均值。 IntranetRx：内网入流量平均值。 IntranetTx：内网出流量平均值。 预测规则取值范围： CpuUtilization：平均CPU使用率。 IntranetRx：内网入流量平均值。 IntranetTx：内网出流量平均值。 |
|---|---|---|---|---|
| TargetValue | Float | 否 | 0.125 | 目标值，适用于目标追踪伸缩规则和预测规则。TargetValue最多保留小数点后三位，且必须大于0。 |
| DisableScaleIn | Boolean | 否 | true | 是否禁用缩容，仅适用于目标追踪伸缩规则。 |
| ScaleInEvaluatio nCount | Integer | 否 | 15 | 创建目标追踪规则后，会自动创建报警任务。本参数用于指定对应的缩容报警任务触发报警时，所需连续满足阈值条件的次数。 |
| ScaleOutEvaluati onCount | Integer | 否 | 3 | 创建目标追踪规则后，会自动创建报警任务。本参数用于指定对应的扩容报警任务触发报警时，所需连续满足阈值条件的次数。 |
| StepAdjustment. N.MetricInterval LowerBound | Float | 否 | 1.0 | 分步步骤的下边界，仅适用于步进规则。 取值范围：- 9.999999E18~9.999999E18。 |
| StepAdjustment. N.MetricInterval UpperBound | Float | 否 | 5.0 | 分步步骤的上边界，仅适用于步进规则。 取值范围：- 9.999999E18~9.999999E18。 |
| StepAdjustment. N.ScalingAdjust ment | Integer | 否 | 1 | 分步步骤对应的实例扩展数量，仅适用于步进规则。 |

弹性伸缩 ESS

| PredictiveScalin gMode | String | 否 | PredictAndScale | 预测规则的模式。取值范围： PredictAndScale：产生预测结果并创建预测任务。 PredictOnly：产生预测结果，但不会创建预测任务。 |
|---|---|---|---|---|
| PredictiveValueB ehavior | String | 否 | MaxOverridePre dictiveValue | 预测规则最大值处理方式。取值范围： MaxOverridePredictiveValue：初始最大值会覆盖预测值。预测值大于初始最大值时，预测任务的最大值采用初始最大值。 PredictiveValueOverrideMax：预测值会覆盖初始最大值。预测值大于初始最大值时，预测任务的最大值采用预测值。 PredictiveValueOverrideMaxWithB uffer：预测值会附加一定比例。预测值会按照PredictiveValueBuffer比例增加，当增加后的值大于初始最大值时， 会采用增加后的值。 |
| PredictiveValueB uffer | Integer | 否 | 50 | PredictiveValueBehavior为 PredictiveValueOverrideMaxWithBuff er时生效，预测值会按照该比例增加，当增加后的值大于初始最大值时，会采用增加后的值。取值范围：0~100。 |
| PredictiveTaskB ufferTime | Integer | 否 | 30 | 预测规则自动创建的预测任务默认均在整点执行，您可以设置预启动时间提前执行预测任务，预先准备资源。取值范围： 0~60。 |
| InitialMaxSize | Integer | 否 | 100 | 伸缩组实例数上限，和 PredictiveValueBehavior结合使用。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http://ess.example.com/?Action=ModifyScalingRule &ScalingRuleId=eMKWG8SRNb9dBLAjweN****
```

`&<`公共请求参数> 正常返回示例弹性伸缩 ESS `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在该账号下不存在。 |
| 400 | InvalidScalingRuleNam e.Duplicate | The specified value of parameter <parameter name> is duplicated. | 伸缩规则名字已存在。 |
| 400 | QuotaExceeded.Scalin gRule | Scaling rule quota exceeded in the specified scaling group. | 您的伸缩规则使用个数达到上限。 |
| 400 | TargetTrackingScaling Rule.UnsupportedMetri c | Specific metric is not supported for target tracking scaling rule. | 目标追踪伸缩规则不支持当前监控指标。 |
| 400 | TargetTrackingScaling Rule.DumplicateMetric | Only one TargetTrackingScaling rule for a given metric specification is allowed. | 一个伸缩组中，同一监控指标只能存在一条目标追踪规则。 |
| 400 | InvalidMinAdjustment MagnitudeMismatchAd justmentType | MinAdjustmentMagnitu de is not supported by the specified adjustment type. | MinAdjustmentMagnitu de不支持当前伸缩规则调整类型。 |
| 400 | InvalidStepAdjustment s.MultipleNullUpperBo und | At most one StepAdjustment may have an unspecified upper bound. | 最多只能有一个分步步骤不指定分步上界。 |

弹性伸缩 ESS

| 400 | InvalidStepAdjustment s.MultipleNullLowerBo und | At most one StepAdjustment may have an unspecified lower bound. | 最多只能有一个分步步骤不指定分步下界。 |
|---|---|---|---|
| 400 | InvalidStepAdjustment s.NoNullLowerBound | There must be a StepAdjustment with an unspecified lower bound when one StepAdjustment has a negative lower bound. | 当存在一个分步下界为负数时，则必须有一个未指定分步下界的分步步骤。 |
| 400 | InvalidStepAdjustment s.NoNullUpperBound | There must be a StepAdjustment with an unspecified upper bound when one StepAdjustment has a positive upper bound. | 当存在一个正数的分步上界时，则必有一个未指定分步上界的分步步骤。 |
| 400 | InvalidStepAdjustment s.Gap | StepAdjustment intervals can not have gaps between them. | 分步步骤之间不能有间隔。 |
| 400 | InvalidStepAdjustment s.Overlap | StepAdjustment intervals can not overlap. | 分步步骤之间不能重叠。 |
| 400 | InvalidStepAdjustment s.LowerGtUpper | LowerBound must be less than the UpperBound for StepAdjustment :%s. | 同一分步步骤中，分步下界必须小于分步上界。 |
| 400 | InvalidStepAdjustment s.BothNull | Both lower and upper bounds of a StepAdjustment can not be left unspecified. | 同一分步步骤中，分步上界和分步下界不能同时不指定。 |
| 400 | InvalidStepAdjustment s.MaxNum | Your scaling rule can have at most %s StepAdjustments. | 同一伸缩组中分步步骤数量超过阈值。 |
| 400 | StepBeyondPermitRan ge | Specific parameter "%s" beyond permit range. | 分步步骤的上界或下界超过了可选范围。 |

#### DescribeScalingRules

调用DescribeScalingRules查询伸缩组下的伸缩规则，并列出伸缩规则的信息。

**接口说明**

弹性伸缩 ESS 您可以通过指定伸缩组ID来查询该伸缩组下的所有伸缩规则，查询时可以输入伸缩规则ID、伸缩规则名称、 伸缩规则唯一标识符、伸缩规则类型进行过滤。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeScaling Rules | 系统规定参数，取值： DescribeScalingRules。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 伸缩规则所属伸缩组的地域ID。 |
| PageNumber | Integer | 否 | 1 | 伸缩规则列表的页码，起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 50 | 分页查询时设置的每页行数，最大值： 50。 默认值：10。 |
| ScalingGroupId | String | 否 | AG6CQdPU8OKd wLjgZcJ**** | 伸缩组的ID。 |
| ScalingRuleType | String | 否 | SimpleScalingRu le | 伸缩规则的类型，取值范围： SimpleScalingRule：简单伸缩规则。 根据调整方式（AdjustmentType）和调整值（AdjustmentValue）调整ECS 实例数量。 TargetTrackingScalingRule：目标追踪伸缩规则。根据预定义监控 （MetricName）项动态计算需要扩缩容的ECS实例数量，尽量将预定义监控项的指标值维持在目标值 （TargetValue）附近。 StepScalingRule：步进伸缩规则，根据阈值和指标值提供分步扩展方式。 PredictiveScalingRule：预测伸缩规则，基于机器学习能力分析伸缩组的历史监控数据预测未来监控指标值，并支持自动创建定时任务设置伸缩组边界。 默认值：SimpleScalingRule。 |
| ShowAlarmRules | Boolean | 否 | false | 是否返回伸缩规则关联的云监控报警任务，取值范围： true：返回伸缩规则关联的云监控报警任务。 false：不返回伸缩规则关联的云监控报警任务。 默认值：false。 |

弹性伸缩 ESS

| ScalingRuleId.N | RepeatL ist | 否 | asr- bp1dvirgwkoow xk7**** | ScalingRuleId.N为待查询伸缩规则的 ID，N的取值范围：1～10。 |
|---|---|---|---|---|
| ScalingRuleNam e.N | RepeatL ist | 否 | scalingrule**** | ScalingRuleName.N为待查询伸缩规则的名称，N的取值范围：1～10。 |
| ScalingRuleAri.N | RepeatL ist | 否 | ari:acs:ess:cn- hangzhou- env17- d01:140692647 406****:scalingr ule/asr- bp1dvirgwkoow xk7**** | ScalingRuleAri.N为待查询伸缩规则的唯一标识符，N的取值范围：1～10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 50 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| ScalingRules | Array of ScalingRule |  | 伸缩规则信息组成的集合。 |
| ScalingRule |  |  |  |
| AdjustmentTy pe | String | QuantityChangeInC apacity | 伸缩规则的调整方式，取值范围： QuantityChangeInCapacity：增加或减少指定数量的ECS实例。 PercentChangeInCapacity：增加或减少指定比例的ECS实例。 TotalCapacity：将当前伸缩组的ECS实例数量调整到指定数量。 |
| AdjustmentVal ue | Integer | 1 | 伸缩规则的调整值。 |
| Alarms | Array of Alarm |  | 伸缩规则关联的云监控报警任务。仅在 ShowAlarmRules参数为true时返回伸缩规则关联的云监控报警任务，否则返回空列表。 |
| Alarm |  |  |  |

弹性伸缩 ESS

| AlarmTaskId | String | asg- bp18p2yfxow2dloq **** 1f9458d1- _ 70e1-4bee-8c7f- 7a47695b**** | 伸缩规则关联的报警任务的ID。 |
|---|---|---|---|
| AlarmTaskNa me | String | event-notified**** | 伸缩规则关联的报警任务的名称。 |
| ComparisonOp erator | String | >= | 伸缩规则关联的报警任务使用的监控项统计值与阈值的比较符，用于指定监控项统计值与阈值在什么关系下满足条件。取值范围： 监控项统计值大于等于阈值。取值：>= 监控项统计值小于等于阈值。取值：<= 监控项统计值大于阈值。取值：> 监控项统计值小于阈值。取值：< |
| Dimensions | Array of Dimension |  | 伸缩规则关联的报警任务的维度信息。 |
| Dimension |  |  |  |
| DimensionKey | String | scaling group _ | 监控项关联的维度信息键值。取值范围： scaling group：伸缩组ID。 _ userId：用户账号ID。 |
| DimensionValu e | String | asg- bp18p2yfxow2dloq **** | 监控项关联的维度信息属性值。 |
| EvaluationCou nt | Integer | 3 | 伸缩规则关联的报警任务到达报警状态需要连续满足阈值表达式的次数。 |
| MetricName | String | CpuUtilization | 伸缩规则关联的报警任务监控项名称。 |
| MetricType | String | system | 伸缩规则关联的报警任务的类型。取值范围： system：系统监控报警任务。 custom：自定义监控报警任务。 |
| Statistics | String | Average | 伸缩规则关联的报警任务的统计方式。取值范围： Average：统计平均值。 Maximum：统计最大值。 Minimum：统计最小值。 |
| Threshold | Float | 50 | 伸缩规则关联的报警任务的报警阈值。 |

弹性伸缩 ESS

| Cooldown | Integer | 20 | 伸缩规则的冷却时间，仅适用于简单伸缩规则。 取值范围：0~86400，单位：秒。 |
|---|---|---|---|
| DisableScaleIn | Boolean | true | 是否禁用缩容，仅适用于目标追踪伸缩规则，取值范围： true：禁用缩容。 false：允许缩容。 |
| EstimatedInsta nceWarmup | Integer | 300 | 实例预热时间。 |
| InitialMaxSize | Integer | 100 | 伸缩组实例数的上限，和 PredictiveValueBehavior结合使用。 |
| MaxSize | Integer | 2 | 伸缩组最大实例数。 |
| MetricName | String | CpuUtilization | 预定义监控项，适用于目标追踪伸缩规则和预测规则。 目标追踪伸缩规则取值范围： CpuUtilization：平均CPU使用率 ClassicInternetRx：经典网络公网入流量平均值 ClassicInternetTx：经典网络公网出流量平均值 VpcInternetRx：VPC网络公网入流量平均值 VpcInternetTx：VPC网络公网出流量平均值 IntranetRx：内网入流量平均值 IntranetTx ：内网出流量平均值预测规则取值范围： CpuUtilization：平均CPU使用率 IntranetRx：内网入流量平均值 IntranetTx：内网出流量平均值 |
| MinAdjustment Magnitude | Integer | 1 | 伸缩规则最小调整实例数，仅当伸缩规则类型为 SimpleScalingRule或StepScalingRule，且 AdjustmentType为 PercentChangeInCapacity时生效。 |
| MinSize | Integer | 1 | 伸缩组最小实例数。 |
| PredictiveScali ngMode | String | PredictAndScale | 预测规则的模式。取值范围： PredictAndScale：产生预测结果并创建预测任务。 PredictOnly：产生预测结果，但不会创建预测任务。 |

弹性伸缩 ESS

| PredictiveTask BufferTime | Integer | 30 | 预测规则自动创建的预测任务默认均在整点执行，您可以设置预启动时间提前执行预测任务， 预先准备资源。取值范围：0~60，单位：分钟。 |
|---|---|---|---|
| PredictiveValu eBehavior | String | MaxOverridePredic tiveValue | 预测规则最大值处理方式。取值范围： MaxOverridePredictiveValue：初始最大值会覆盖预测值。预测值大于初始最大值时，预测任务的最大值采用初始最大值。 PredictiveValueOverrideMax：预测值会覆盖初始最大值。预测值大于初始最大值时，预测任务的最大值采用预测值。 PredictiveValueOverrideMaxWithBuffer ：预测值会附加一定比例。预测值会按照 PredictiveValueBuffer比例增加，当增加后的值大于初始最大值时，会采用增加后的值。 |
| PredictiveValu eBuffer | Integer | 50 | PredictiveValueBehavior为 PredictiveValueOverrideMaxWithBuffer时生效，预测值会按照该比例增加，当增加后的值大于初始最大值时，会采用增加后的值。取值范围：0~100。 |
| ScaleInEvaluat ionCount | Integer | 15 | 创建目标追踪规则后，会自动创建报警任务。本参数用于指定对应的缩容报警任务触发报警时， 所需连续满足阈值条件的次数。 |
| ScaleOutEvalu ationCount | Integer | 3 | 创建目标追踪规则后，会自动创建报警任务。本参数用于指定对应的扩容报警任务触发报警时， 所需连续满足阈值条件的次数。 |
| ScalingGroupI d | String | AG6CQdPU8OKdwL jgZcJ**** | 伸缩组的ID。 |
| ScalingRuleAri | String | ari:acs:ess:cn- qingdao-env17- d01:134****:scalin gRule/eMKWG8SRN b9dBLAjweN**** | 伸缩规则的唯一标识符。 |
| ScalingRuleId | String | eMKWG8SRNb9dBL AjweN**** | 伸缩规则的ID。 |
| ScalingRuleNa me | String | eMKWG8SRNb9dBL AjweN**** | 伸缩规则的名称。 |

弹性伸缩 ESS

| ScalingRuleTy pe | String | SimpleScalingRule | 伸缩规则类型，取值范围： SimpleScalingRule：简单伸缩规则。根据调整方式（AdjustmentType）和调整值 （AdjustmentValue）调整ECS实例数量。 TargetTrackingScalingRule：目标追踪伸缩规则。根据预定义监控（MetricName）项动态计算需要扩缩容的ECS实例数量，尽量将预定义监控项的指标值维持在目标值 （TargetValue）附近。 StepScalingRule：步进伸缩规则，根据阈值和指标值提供分步扩展方式。 PredictiveScalingRule：预测伸缩规则，基于机器学习能力分析伸缩组的历史监控数据预测未来监控指标值，并支持自动创建定时任务设置伸缩组边界。 |
|---|---|---|---|
| StepAdjustme nts | Array of StepAdjustme nt |  | 步进规则的分步步骤。 |
| StepAdjustme nt |  |  |  |
| MetricIntervalL owerBound | Float | 1.0 | 分步步骤的下边界，取值范围：- 9.999999E18~9.999999E18。 |
| MetricInterval UpperBound | Float | 5.0 | 分步步骤的上边界，取值范围：- 9.999999E18~9.999999E18。 |
| ScalingAdjust ment | Integer | 1 | 分步步骤对应的实例扩展数量。 |
| TargetValue | Float | 0.125 | 目标值。 |
| TotalCount | Integer | 1 | 伸缩规则总数。 |

**示例**

请求示例

```
http://ess.example.com/?Action=DescribeScalingRules &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <PageNumber>1</PageNumber>
      <PageSize>50</PageSize>
      <ScalingRules>
            <ScalingRule>
                  <AdjustmentType>QuantityChangeInCapacity</AdjustmentType>
                  <AdjustmentValue>1</AdjustmentValue>
                  <Cooldown>20</Cooldown>
                  <ScalingGroupId>AG6CQdPU8OKdwLjgZcJ****</ScalingGroupId>
                  <ScalingRuleAri>ari:acs:ess:cn-qingdao-env17-
d01:134****:scalingRule/eMKWG8SRNb9dBLAjweN****</ScalingRuleAri>
                  <ScalingRuleId>eMKWG8SRNb9dBLAjweN****</ScalingRuleId>
                  <ScalingRuleName>eMKWG8SRNb9dBLAjweN****</ScalingRuleName>
            </ScalingRule>
      </ScalingRules>
      <TotalCount>1</TotalCount>
      <RequestId>3306A40D-3412-4101-9F19-5F81E3055DAD</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "B583BFEF-A779-427A-9B74-262DDD249702",
    "TotalCount": 1,
    "PageNumber": 1,
    "PageSize": 10,
    "ScalingRules": {
        "ScalingRule": [
            {
                "ScalingRuleId": "efcqrZdjlookc0UkE3dA****",
                "ScalingRuleAri": "ari:acs:ess:cn-qingdao-env17-
d01:134****:scalingRule/efcqrZdjlookc0UkE3dA****",
                "Cooldown": 500,
                "ScalingGroupId": "ccMvs9dcZlE5c9CtrwbX****",
                "AdjustmentType": "TotalCapacity",
                "ScalingRuleName": "KFJoxG****",
                "AdjustmentValue": 5
            }
```

]

```
    }
}
```

#### DeleteScalingRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

弹性伸缩 ESS

| Action | String | 是 | DeleteScalingRu le | 系统规定参数，取值： DeleteScalingRule。 |
|---|---|---|---|---|
| ScalingRuleId | String | 是 | eMKWG8SRNb9 dBLAjweN**** | 待删除伸缩规则的ID。您可以调用 DescribeScalingRules参数查询伸缩规则的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http://ess.example.com/?Action=DeleteScalingRule &ScalingRuleId=eMKWG8SRNb9dBLAjweN****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
  "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingRuleId.N otFound | The specified scaling rule does not exist. | 指定的伸缩规则在该账号下不存在。 |

### 触发任务

#### ExecuteScalingRule

弹性伸缩 ESS

**接口说明**

调用该接口前请确保满足以下条件： 伸缩组为Active状态。 伸缩组没有伸缩活动正在执行。 当伸缩组没有伸缩活动正在执行时，该接口可以绕过冷却时间（Cooldown）直接执行。 调用该接口返回成功，只是表示弹性伸缩服务接受了该接口的调用请求，伸缩活动可以执行，但不代表伸缩活动能够执行成功。用户需要通过返回的ScalingActivityId查看该伸缩活动的执行状态。 如果该伸缩规则需要增加的ECS实例数加上当前伸缩组的实例数（Total Capacity）大于MaxSize，则按 Total Capacity = MaxSize的规则进行执行。 如果当前伸缩组的实例数（Total Capacity）减去该伸缩规则需要减少的ECS实例数小于MinSize，则按 Total Capacity = MinSize的规则进行执行。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ExecuteScalingR ule | 系统规定参数，取值： ExecuteScalingRule。 |
| ScalingRuleAri | String | 是 | ari:acs:ess:cn- hangzhou- env17- d01:140692647 406****:scalingr ule/asr- bp1dvirgwkoow xk7**** | 伸缩规则唯一标识符。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 426655440000 | 用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一，最大不超过64个ASCII字符。更多信息，请参见如何保证幂等性。 |
| BreachThreshold | Float | 否 | 1.0 | 执行步进伸缩规则时指定的当前阈值，取值范围：- 9.999999E18~9.999999E18。 |
| MetricValue | Float | 否 | 1.0 | 执行步进伸缩规则时指定的当前指标值， 取值范围：- 9.999999E18~9.999999E18。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

弹性伸缩 ESS

| ScalingActivity Id | String | asa- bp13o672yeautiil** ** | 伸缩活动的ID。 |
|---|---|---|---|

**示例**

请求示例

```
http://ess.example.com/?Action=ExecuteScalingRule &ScalingRuleAri=ari:acs:ess:cn-hangzhou-env17-d01:140692647406****:scalingrule/asr-bp1d virgwkoowxk7****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <ScalingActivityId>asa-bp13o672yeautiil****</ScalingActivityId>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "ScalingActivityId": "asa-bp13o672yeautiil****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingRuleAri.N otFound | The specified scaling rule Ari does not exist. | 指定的伸缩规则在该账号下不存在。 |
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您并未向弹性伸缩完整授权Open API接口。 |
| 400 | IncorrectScalingGroup Status | The current status of the specified scaling group does not support this action. | 指定伸缩规则所属的伸缩组未处于active状态。 |

弹性伸缩 ESS

| 400 | ScalingActivityInProgre ss | You cannot delete a scaling group or launch a new scaling activity while there is a scaling activity in progress for the specified scaling group. | 指定伸缩规则所属的伸缩组有伸缩活动正在进行。 |
|---|---|---|---|
| 400 | InsufficientBalance | Your account does not have enough balance. | 您的账号余额不足。 |
| 400 | QuotaExceed.Instance | Living instance quota exceeded. | 您的ECS实例个数使用达到上限。 |
| 400 | IncorrectLoadBalancer Status | The current status of the specified load balancer does not support this action. | 指定伸缩规则所属的伸缩组的负载均衡实例未处于 active状态。 |
| 400 | IncorrectLoadBalancer HealthCheck | The current health check type of specified load balancer does not support this action. | 指定伸缩规则所属的伸缩组的负载均衡实例未开启健康检查。 |
| 400 | InvalidLoadBalancerId. IncorrectInstanceNetw orkType | The network type of the instance in specified load balancer does not support this action. | 指定的负载均衡实例含有的ECS实例的网络类型与伸缩组的网络类型不匹配。 |
| 400 | InvalidLoadBalancerId. VPCMismatch | The specified virtual switch and the instance in specified load balancer are not in the same VPC. | 指定的伸缩组的负载均衡实例含有的ECS实例与 VSwitchId不在同一个 VPC中。 |
| 400 | IncorrectDBInstanceSt atus | The current status of DB instance "XXX" does not support this action. | 指定伸缩规则所属的伸缩组的RDS实例未处于 running状态。 |
| 400 | QuotaExceeded.DBInst anceSecurityIP | Security IP quota exceeded in DB instance "XXX". | 指定伸缩规则所属的伸缩组的RDS实例访问白名单的IP个数达到上限。 |
| 400 | QuotaExceeded.Securi tyGroupInstance | Instance quota exceeded in the specified security group. | 指定的安全组已添加的 ECS实例个数达到上限。 |

弹性伸缩 ESS

| 400 | IncorrectCapacity.NoC hange | To execute the specified scaling rule, the total capacity will not change. | 伸缩规则未造成伸缩组实例数的变化。 |
|---|---|---|---|
| 400 | QuotaExceeded.Scalin gInstance | Scaling instance quota exceeded. | 弹性伸缩的ECS实例使用个数达到上限。 |
| 400 | QuotaExceeded.Afterp ayInstance | Living afterpay instance quota exceeded. | 按量付费ECS实例的使用个数达到上限。 |
| 400 | ResourceNotAvailable. ECS | The specified region or zone does not offer the specified disk or instance category. | 指定的区域无法创建指定的ECS实例类型或磁盘类型。 |
| 400 | ScalingRule.InvalidScal ingRuleType | Specific scaling rule type: %s can not be executed. | 无法执行当前类型的伸缩规则。 |
| 400 | InvalidStepAdjustment s.NoStepFound | No adjustment step found for a metric value of: %s. | 未找到符合条件的分步执行步骤。 |
| 400 | MissingParameter.Metr icValue | Metric value must be specified for StepScalingRule. | 执行分步伸缩规则必须指定指标值。 |
| 400 | MissingParameter.Bre achThreshold | Breach threshold must be specified for StepScalingRule. | 执行分步伸缩规则必须指定阈值。 |
| 400 | MetricValueBeyondPer mitRange | Specific parameter "%s" beyond permit range. | 指标值超过了可选范围。 |
| 400 | BreachThresholdBeyon dPermitRange | Specific parameter "%s" beyond permit range. | 阈值超过了可选范围。 |

#### ScaleWithAdjustment

**接口说明**

弹性伸缩 ESS 调用该接口需注意以下几点： 调用该接口前，请确保满足以下条件： 伸缩组处于Active状态。 伸缩组内没有执行中的伸缩活动。 当伸缩组没有执行中的伸缩活动时，该接口可以绕过冷却时间（Cooldown）直接执行伸缩活动。 如果伸缩规则需要增加的ECS实例数加上当前伸缩组的实例数（Total Capacity）大于最大实例数 （MaxSize），则按Total Capacity=MaxSize执行伸缩活动。 如果当前伸缩组的实例数（Total Capacity）减去伸缩规则需要减少的ECS实例数小于最小实例数 （MinSize），则按Total Capacity=MinSize执行伸缩活动。 调用该接口返回成功，只是表示弹性伸缩服务接受了该接口的调用请求，可以执行伸缩活动，但不代表伸缩活动能够执行成功。您需要通过返回的ScalingActivityId查看该伸缩活动的执行状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |  |  |
|---|---|---|---|---|---|---|
| Action | String | 是 | ScaleWithAdjust ment | 系统规定参数。取值： ScaleWithAdjustment。 |  |  |
| AdjustmentType | String | 是 | QuantityChangeI nCapacity | 伸缩活动调整方式，取值范围： QuantityChangeInCapacity：增加或减少指定数量的ECS实例。 PercentChangeInCapacity：增加或减少指定比例的ECS实例。 TotalCapacity：将当前伸缩组的ECS 实例数量调整到指定数量。 |  |  |
| AdjustmentValu e | Integer | 是 | 100 | 伸缩活动调整值。任何情况下，单次调整的ECS实例台数都不能超过1000，否则会导致调整失败。不同调整方式对应的取值范围： QuantityChangeInCapacity：- 1000~1000。 PercentChangeInCapacity：- 100~10000。 TotalCapacity：0~2000。 |  |  |
| ScalingGroupId | String | 是 | asg- j6c1o397427hyj dc**** | 伸缩组的ID。 |  |  |
| MinAdjustmentM agnitude | Integer | 否 | 1 | 伸缩活动最小调整实例数，仅当 AdjustmentType 为 PercentCh angeInCapacity 时生效。 |  |  |
|  |  |  |  |  | PercentCh |  |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |  |  |

|  |  | AdjustmentType |
|---|---|---|
|  | angeInCapacity |  |

弹性伸缩 ESS

| SyncActivity | Boolean | 否 | false | 伸缩活动同步执行开关，仅对具有期望实例数配置项的伸缩组有效。取值范围： true：同步流程，即执行伸缩规则时会直接触发伸缩组的扩缩容活动。 false：异步流程，即修改伸缩组内的期望实例数时，不会立刻触发伸缩组的实际扩缩容活动，需等待期望实例数变化后，系统自动检测期望实例数与伸缩组内当前实例数不一致，才会触发扩缩容活动。 说明关于期望实例数的更多信息，请参见弹性伸缩用户指南章节的期望实例数章节。 默认值：false。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingActivity Id | String | asa- bp175o6f6ego3r2j* *** | 伸缩活动的ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=ScaleWithAdjustment &AdjustmentType=QuantityChangeInCapacity &AdjustmentValue=100 &MinAdjustmentMagnitude=1 &ClientToken=123e4567-e89b-12d3-a456-42665544**** &SyncActivity=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
    <ScalingActivityId>asa-bp175o6f6ego3r2j****</ScalingActivityId>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingActivityId": "asa-bp175o6f6ego3r2j****"
}
```

#### AttachInstances

**接口说明**

加入的ECS实例的限定条件包括： 加入的ECS实例必须与伸缩组在同一个地域。 加入的ECS实例必须处于Running状态。 加入的ECS实例未加入其他伸缩组。 加入的ECS实例支持包年包月和按量付费两种类型。 如果伸缩组指定VswitchID，既不支持经典网络类型的ECS实例加入伸缩组，也不支持专有网络类型的 ECS实例加入伸缩组。 如果伸缩组没有指定VswitchID，不支持专有网络类型的ECS实例加入伸缩组。 当伸缩组处于Active状态时，才可以调用该接口。 当伸缩组没有伸缩活动正在执行时，才可以调用该接口。 当伸缩组没有伸缩活动正在执行时，该接口可以绕过冷却时间（Cooldown）直接执行。 调用该接口返回成功，只是表示弹性伸缩服务接受了该接口调用的请求，伸缩活动可以执行，但不代表伸缩活动能够执行成功。您需要通过返回的ScalingActivityId查看该伸缩活动的执行状态。 如果该接口指定的实例数加上当前伸缩组的实例数（Total Capacity）大于MaxSize，则调用失败。 手动添加的ECS实例不能与伸缩组生效的伸缩配置进行关联。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AttachInstances | 系统规定参数，取值： AttachInstances。 |
| ScalingGroupId | String | 是 | asg- bp18p2yfxow2dl oq**** | 伸缩组的ID。 |
| InstanceId.N | RepeatL ist | 否 | i-28wt4**** | InstanceId.N为待添加ECS实例的ID，N 的取值范围：1～20。 |
| LoadBalancerWe ight.N | RepeatL ist | 否 | 50 | LoadBalancerWeight.N为ECS实例作为负载均衡实例后端服务器时的权重，N的取值范围：1～20，该参数取值范围： 1~100。 默认值：50。 |

弹性伸缩 ESS

| Entrusted | Boolean | 否 | false | 将已经存在的ECS实例手动添加到伸缩组时，是否将该ECS实例的生命周期托管给伸缩组。取值范围： true：托管。该ECS实例的生命周期由弹性伸缩管理，与伸缩组自动创建的 ECS实例一致。ECS实例被移出伸缩组 （不包括通过调用DetachInstances移出）时会自动释放。 false：不托管。该ECS实例在被移出伸缩组时不会被释放。 说明不支持托管包年包月 ECS实例。 默认值：false。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| ScalingActivity Id | String | asa- bp1crxor24s28xf1* *** | 伸缩活动的ID。 |

**示例**

请求示例

```
&InstanceId.1=i-28wt4**** &ScalingGroupId=asg-bp18p2yfxow2dloq****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <ScalingActivityId>asa-bp1crxor24s28xf1****</ScalingActivityId>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "ScalingActivityId": "asa-bp1crxor24s28xf1****"
}
```

**错误码**

弹性伸缩 ESS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在该账号下不存在。 |
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您并未向伸缩组完整授权 Open API接口。 |
| 400 | IncorrectScalingGroup Status | The current status of the specified scaling group does not support this action. | 指定的伸缩组未处于 active状态。 |
| 404 | InvalidInstanceId.NotF ound | Instance "XXX" does not exist. | 指定的ECS实例在该账号下不存在。 |
| 400 | InvalidInstanceId. RegionMismatch | Instance "XXX" and the specified scaling group are not in the same Region. | 指定的ECS实例与伸缩组所属的地域不匹配。 |
| 400 | InvalidInstanceId.Insta nceTypeMismatch | Instance "XXX" and existing active scaling configurations have different instance types. | 指定的ECS实例与伸缩配置的实例规格不匹配。 |
| 400 | IncorrectInstanceStatu s | The current status of instance "XXX" does not support this action. | 指定的ECS实例未处于 running状态。 |
| 400 | InvalidInstanceId. NetworkTypeMismatch | The network type of instance "XXX" does not support this action. | ECS实例的网络类型与伸缩组的网络类型不匹配。 |
| 400 | InvalidInstanceId.VPC Mismatch | Instance "XXX" and the specified scaling group are not in the same VPC. | 指定的伸缩组与添加的 ECS实例不在同一个VPC 中。 |
| 400 | InvalidInstanceId.InUs e | Instance "XXX" is already attached to another scaling group. | 指定的ECS实例已加入其他伸缩组。 |

弹性伸缩 ESS

| 400 | ScalingActivityInProgre ss | You cannot delete a scaling group or launch a new scaling activity while there is a scaling activity in progress for the specified scaling group. | 指定的伸缩组有伸缩活动正在进行。 |
|---|---|---|---|
| 400 | IncorrectLoadBalancer Status | The current status of the specified load balancer does not support this action. | 指定的伸缩组的负载均衡实例未处于active状态。 |
| 400 | IncorrectLoadBalancer HealthCheck | The current health check type of specified load balancer does not support this action. | 指定的伸缩组的负载均衡实例未开启健康检查。 |
| 400 | InvalidLoadBalancerId. IncorrectInstanceNetw orkType | The network type of the instance in specified load balancer does not support this action. | 指定的负载均衡实例含有的ECS实例的网络类型与伸缩组的网络类型不匹配。 |
| 400 | InvalidLoadBalancerId. VPCMismatch | he specified virtual switch and the instance in specified load balancer are not in the same VPC. | 指定的伸缩组的负载均衡实例含有的ECS实例与 VSwitchId不在同一个 VPC中。 |
| 400 | IncorrectDBInstanceSt atus | The current status of DB instance "XXX" does not support this action. | 指定的伸缩组的RDS实例未处于running状态。 |
| 400 | QuotaExceeded.DBInst anceSecurityIP | Security IP quota exceeded in DB instance "XXX". | 指定的伸缩组的RDS实例访问白名单的IP个数达到上限。 |
| 400 | QuotaExceeded.Securi tyGroupInstance | Instance quota exceeded in the specified security group. | 指定的安全组已添加的 ECS实例个数达到上限。 |
| 400 | IncorrectCapacity.Max Size | To attach the instances, the total capacity will be greater than the MaxSize. | 加入的ECS实例数使得 Total Capacity超过 MaxSize。 |

弹性伸缩 ESS

#### RemoveInstances

**接口说明**

调用本接口前请确保满足以下条件： 伸缩组处于启用（Active）状态。 伸缩组中没有正在执行的伸缩活动。 当伸缩组没有伸缩活动正在执行时，该接口可以绕过冷却时间（DefaultCooldown）直接执行。 从伸缩组移出弹性伸缩自动创建的ECS实例时，ECS实例进入停机不收费状态或者被释放。 从伸缩组移出用户手工加入的ECS实例时，不停止和释放该ECS实例。 调用该接口返回成功，只是表示弹性伸缩服务接受了该接口调用的请求，伸缩活动可以执行，但不代表伸缩活动能够执行成功。用户需要通过返回的ScalingActivityId查看该伸缩活动的执行状态。 如果当前伸缩组的实例数（TotalCapacity）减去该接口指定的实例数小于伸缩组内最小实例数 （MinSize），则调用失败。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RemoveInstance s | 系统规定参数，取值： RemoveInstances。 |
| InstanceId.N | RepeatL ist | 是 | i- 1kx0159ruc4x22 ek**** | 待移出ECS实例的ID。N的取值范围： 1~20。 |
| ScalingGroupId | String | 是 | AG6CQdPU8OKd wLjgZcJ**** | 伸缩组的ID。 |
| RemovePolicy | String | 否 | release | 指定被移出实例的动作，取值范围： recycle：实例进入停机不收费状态。 说明仅在ScalingPolicy 为recycle时生效。 release：实例被释放。 默认值：release。 |
| DecreaseDesire dCapacity | Boolean | 否 | true | 是否修改期望实例数。取值范围： true：从伸缩组删除ECS实例后，期望实例数也减少相应台数。 false：从伸缩组删除ECS实例后，期望实例数不会变化。 默认值：true |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
|---|---|---|---|
| ScalingActivity Id | String | bybj9OcaOT4ucPM bFhcq**** | 伸缩活动的ID。 |

**示例**

请求示例

```
&ScalingGroupId=AG6CQdPU8OKdwLjgZcJ**** &InstanceId.1=i-28wt4****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <ScalingActivityId>bybj9OcaOT4ucPMbFhcq****</ScalingActivityId>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "ScalingActivityId":"bybj9OcaOT4ucPMbFhcq****",
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在该用户账号下不存在。 |
| 404 | InvalidInstanceId.NotF ound | Instance "XXX" does not exist. | 指定的ECS实例在伸缩组下不存在。 |
| 400 | InvalidParameter | The specified group does not support the specified RemovePolicy. | 当前伸缩组不支持停机回收策略。 |

弹性伸缩 ESS

| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您未向弹性伸缩授予完整的OpenAPI接口权限。 |
|---|---|---|---|
| 400 | IncorrectScalingGroup Status | The current status of the specified scaling group does not support this action. | 指定的伸缩组未处于 Active状态。 |
| 400 | ScalingActivityInProgre ss | You cannot delete a scaling group or launch a new scaling activity while there is a scaling activity in progress for the specified scaling group. | 指定的伸缩组有进行中的伸缩活动。 |
| 400 | IncorrectLoadBalancer Status | The current status of the specified load balancer does not support this action. | 指定伸缩规则所属的伸缩组的负载均衡实例未处于 active状态。 |
| 400 | IncorrectDBInstanceSt atus | The current status of DB instance "XXX" does not support this action. | 指定伸缩规则所属的伸缩组的RDS实例未处于 Running状态。 |
| 400 | IncorrectCapacity.MinS ize | To remove the instances, the total capacity will be lesser than the MinSize. | 移出的实例数使得 TotalCapacity小于 MinSize。 |

#### DetachInstances

**接口说明**

移出ECS实例之后，ECS实例可以独立于伸缩组存在，您可以调用API AttachInstances接口将ECS实例附加到其他伸缩组。 调用该接口移出一台ECS实例并不会停止或释放该实例。 调用该接口前，请确保满足以下条件： 目标伸缩组必须处于启用（Enable）状态。 目标伸缩组不能有正在进行的伸缩活动。 目标伸缩组没有正在进行的伸缩活动时，该接口可以绕过冷却时间直接执行。 接口成功调用后，仅表示接受了该接口调用的请求。可以照常触发伸缩活动，但不能保证伸缩活动执行成功，您需要通过返回的ScalingActivityId查看伸缩活动的状态。 目标伸缩组的ECS数量减去当前分离的ECS数不能小于伸缩组最小实例数（MinSize），否则会报错。 弹性伸缩 ESS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DetachInstances | 系统规定参数，取值： DetachInstances。 |
| InstanceId.N | RepeatL ist | 是 | i-28wt4**** | 待分离ECS实例的ID。N的取值范围： 1~20。 |
| ScalingGroupId | String | 是 | AG6CQdPU8OKd wLjgZcJ**** | 伸缩组的ID。 |
| DecreaseDesire dCapacity | Boolean | 否 | true | 是否修改期望实例数。取值范围： true：ECS实例移出伸缩组后，期望实例数也减少相应台数。 false：ECS实例移出伸缩组后，期望实例数不会变化。 默认值：true。 |
| DetachOption | String | 否 | both | 指定是否停止使用ECS实例作为负载均衡实例的后端服务器（即将ECS实例移出负载均衡实例的默认服务器组和虚拟服务器组），以及是否将ECS实例移出RDS实例的访问白名单。 both表示将ECS实例移出负载均衡实例的默认服务器组和虚拟服务器组，并将ECS 实例移出RDS实例的访问白名单。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| ScalingActivity Id | String | asa-**** | 伸缩活动的ID。 |

**示例**

请求示例

```
&ScalingGroupId=AG6CQdPU8OKdwLjgZcJ**** &InstanceId.1=i-28wt4****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
      <ScalingActivityId>asa-****</ScalingActivityId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "ScalingActivityId": "asa-****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IncorrectScalingGroup Status | The current status of the specified scaling group does not support this action. | 目标伸缩组必须处于启用 （Enable）状态。 |
| 400 | ScalingActivityInProgre ss | You cannot delete a scaling group or launch a new scaling activity while there is a scaling activity in progress for the specified scaling group. | 目标伸缩组不能有正在进行的伸缩活动。 |
| 400 | IncorrectLoadBalancer Status | The current status of the specified load balancer does not support this action. | 目标伸缩组内的负载均衡实例必须处于运行中 （Active）状态。 |
| 400 | IncorrectDBInstanceSt atus | The current status of DB instance “XXX” does not support this action. | 目标伸缩组内的RDS实例必须处于运行中 （Running）状态。 |
| 400 | IncorrectCapacity.MinS ize | To remove the instances, the total capacity will be lesser than the MinSize. | 目标伸缩组的ECS实例数量减去当前分离的ECS实例数量不能小于伸缩组最少实例数（MinSize）。 |
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您暂未被授权调用 DetachInstances接口。 |

弹性伸缩 ESS

| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组不存在。 |
|---|---|---|---|
| 404 | InvalidInstanceId.NotF ound | Instance “XXX” does not exist. | 指定的ECS实例不存在。 |

### 定时任务

#### CreateScheduledTask

**接口说明**

一个账号下最多创建20个定时任务。 由于伸缩组正在发生伸缩活动或者伸缩组停用等原因，导致定时任务触发执行伸缩规则失败后，在 LaunchExpirationTime内，定时任务会自动重试触发，否则放弃本次定时触发。 如果多个定时任务在相近的时间内触发执行同一个伸缩组的伸缩规则，则最早触发的定时任务会先执行伸缩活动。由于同一个伸缩组同一时刻内只能有一个伸缩活动，排在后面的定时任务会在 LaunchExpirationTime内自动重试定时触发。如上一个伸缩活动完成之后，排在后面的定时任务还在 LaunchExpirationTime内重试，则执行该定时任务的伸缩规则并触发相应的伸缩活动。 定时任务支持两种伸缩方式。 通过 `ScheduledAction` 参数设置需要执行的伸缩规则。 通过 `ScalingGroupId` 参数设置伸缩组内实例数量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateSchedule dTask | 系统规定参数，取值： CreateScheduledTask。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 定时任务所属地域的ID。 |
| ScheduledTaskN ame | String | 否 | scheduled**** | 定时任务的显示名称。2~64个英文或中文字符，以数字、大小字母或中文开头，可包含数字、下划线（ ）、短划线（-）或 _ 半角句号（.）。同一账号同一地域内唯一。 如果没有指定该函数，默认值： ScheduledScalingTaskId。 |
| Description | String | 否 | Test scheduled task. | 定时任务的描述信息。2~200个英文或中文字符。 |

弹性伸缩 ESS

| ScheduledAction | String | 否 | ari:acs:ess:cn- qingdao-env17- d01:134****:scal ingRule/cCBpdY dQuBe2cUxOdu 6**** | 定时任务触发时需要执行的伸缩规则，填写伸缩规则的唯一标识符。指定 ScheduledAction 后，定时任务的伸缩方式为选择已有伸缩规则。 说明不支持同时设置 ScheduledAction和 ScalingGroupId参数。 |
|---|---|---|---|---|
| RecurrenceEndTi me | String | 否 | 2014-08- 17T16:55Z | 重复执行定时任务的结束时间。 按照ISO8601标准表示，并需要使用UTC 时间。格式： YYYY-MM- DDThh:mmZ 。不能填写自创建当天起 365日后的时间。 您需要同时指定RecurrenceType、 RecurrenceValue和 RecurrenceEndTime参数。 |
| LaunchTime | String | 否 | 2014-08- 17T16:52Z | 定时任务触发的时间点。 按照ISO8601标准表示，并需要使用UTC 时间。格式： YYYY-MM- DDThh:mmZ 。不能填写自创建当天起90 日后的时间。 如果指定了RecurrenceType，则此属性指定的时间点，默认为循环执行的时间点。 如果未指定RecurrenceType，则按指定的日期和时间执行一次。 |
| RecurrenceType | String | 否 | Daily | 重复执行定时任务的类型，取值范围： Daily：每多少天重复执行一次定时任务。 Weekly：每周指定几天重复执行一次定时任务。 Monthly：每月内指定几天重复执行一次定时任务。 Cron：按照指定的Cron表达式执行定时任务。 您需要同时指定RecurrenceType、 RecurrenceValue和 RecurrenceEndTime参数。 |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

弹性伸缩 ESS

| RecurrenceValu e | String | 否 | 1 | 重复执行定时任务的数值。 RecurrenceType取Daily时，只能填一个值，取值范围：1~31。 RecurrenceType取Weekly时，可以填入多个值，填多个值时使用半角逗号 （,）分隔。例如，周日、周一、周二、 周三、周四、周五、周六的值依次为： 0,1,2,3,4,5,6。 RecurrenceType取Monthly时，格式为A-B。A、B的取值范围为1~31，并且B必须大于等于A。 RecurrenceType取Cron时，表示UTC 时间，支持分、时、日、月、星期的5 域表达式，支持通配符半角逗号（,）、 半角问号（?）、短划线（-）、星号 （*）、井号（#）、正斜线（/）、L和 W。 您需要同时指定RecurrenceType、 RecurrenceValue和 RecurrenceEndTime参数。 |
|---|---|---|---|---|
| TaskEnabled | Boolean | 否 | true | 是否启动定时任务。 true：启动任务。 false：停止任务 。 默认值：true。 |
| LaunchExpiratio nTime | Integer | 否 | 600 | 定时任务触发操作失败后，在此时间内重试。单位为秒，取值范围：0~21600。 默认值：600。 |
| MinValue | Integer | 否 | 0 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的最小数量。 |
| MaxValue | Integer | 否 | 10 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的最大数量。 |
| DesiredCapacity | Integer | 否 | 10 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的期望实例数。 说明伸缩组必须支持设置期望实例数，即在创建该伸缩组时指定了DesiredCapacity。 |

弹性伸缩 ESS

| ScalingGroupIdI nvalid | String | 否 | asg- bp18p2yfxow2dl oq**** | 定时任务触发时需要修改实例数量的伸缩组，填写伸缩组ID。指定ScalingGroupId 后，定时任务的伸缩方式为设置伸缩组内实例数量，您需要为MinValue、 MaxValue和DesiredCapacity中至少一个参数指定数量。 说明不支持同时设置 ScheduledAction和 ScalingGroupId参数。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScheduledTas kId | String | edRtShc57WGXdt8 TlPbr**** | 定时任务的ID，由系统生成，全局唯一。 |

**示例**

请求示例

```
http://ess.example.com/?Action=CreateScheduledTask &RegionId=cn-qingdao-env17-d01 &ScheduledAction=ari:acs:ess:cn-qingdao-env17d01:134****:scalingRule/cCBpdYdQuBe2cUxOdu6****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScheduledTaskId>edRtShc57WGXdt8TlPbr****</ScheduledTaskId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScheduledTaskId": "edRtShc57WGXdt8TlPbr****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| 404 | InvalidRegionId.NotFou nd | The specified region does not exist. | 指定的地域不存在。 |
|---|---|---|---|
| 400 | InvalidScheduledTask Name.Duplicate | The specified value of parameter ScheduledTaskName is duplicated. | 定时任务名已存在。 |
| 400 | QuotaExceeded.Sched uledTask | Scheduled task quota exceeded. | 您的定时任务使用个数达到上限。 |
| 400 | ScheduledAction.Regio nMismatch | The specified scheduled task and the specified scheduled action are not in the same Region. | 指定的ScheduledAction 与定时任务所在的地域不匹配。 |

#### ModifyScheduledTask

**接口说明**

定时任务支持两种伸缩方式。 通过 `ScheduledAction` 参数设置需要执行的伸缩规则。 通过 `ScalingGroupId` 参数设置伸缩组内实例数量。 不支持同时设置ScheduledAction和ScalingGroupId参数。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySchedule dTask | 系统规定参数，取值： ModifyScheduledTask。 |
| ScheduledTaskId | String | 是 | edRtShc57WGX dt8TlPbr**** | 定时任务的ID。 |
| ScheduledTaskN ame | String | 否 | scheduled**** | 定时任务的名称。2~64个英文或中文字符，以数字、大小字母或中文开头，可包含数字、下划线（ ）、短划线（-）或半 _ 角句号（.）。同一账号同一地域内唯一。 |

弹性伸缩 ESS

| Description | String | 否 | fortest | 定时任务的描述信息。2~200个英文或中文字符。 |
|---|---|---|---|---|
| ScheduledAction | String | 否 | ari:acs:ess:cn- qingdao-env17- d01:134****:scal ingRule/cCBpdY dQuBe2cUxOdu 6**** | 定时任务触发时需要执行的伸缩规则，填写伸缩规则的唯一标识符。指定 ScheduledAction 后，定时任务的伸缩方式为选择已有伸缩规则。 说明不支持同时设置 ScheduledAction和 ScalingGroupId参数。 |
| RecurrenceEndTi me | String | 否 | 2014-08- 20T16:55Z | 重复执行定时任务的结束时间。按照 ISO8601标准表示，并需要使用UTC时间。格式为： YYYY-MM- DDThh:mmZ 。不能填写自修改当天起 365日后的时间。 修改后，RecurrenceType、 RecurrenceValue和 RecurrenceEndTime参数需要同时有效。 |
| LaunchTime | String | 否 | 2014-08- 18T10:52Z | 定时任务触发的时间点。按照ISO8601标准表示，并需要使用UTC时间。格式为： YYYY-MM-DDThh:mmZ 。不能填写自修改当天起90日后的时间。 如果指定了RecurrenceType，则此属性指定的时间点，默认为循环执行的时间点。 如果未指定RecurrenceType，则按指定的日期和时间执行一次。 |
| RecurrenceType | String | 否 | Daily | 重复执行定时任务的类型，取值范围： Daily：每多少天重复执行一次定时任务。 Weekly：每周指定几天重复执行一次定时任务。 Monthly：每月内指定几天重复执行一次定时任务。 Cron：按照指定的Cron表达式执行定时任务。 修改后，RecurrenceType、 RecurrenceValue和 RecurrenceEndTime参数需要同时有效。 |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

弹性伸缩 ESS

| RecurrenceValu e | String | 否 | 2 | 重复执行定时任务的数值。 RecurrenceType取Daily时，只能填一个值，取值范围：1~31。 RecurrenceType取Weekly时，可以填入多个值，填多个值时使用半角逗号 （,）分隔。比如，周日、周一、周二、 周三、周四、周五、周六的值依次为： 0,1,2,3,4,5,6 。 RecurrenceType取Monthly时，格式为A-B。A、B的取值范围为1~31，并且B必须大于等于A。 RecurrenceType取Cron时，表示UTC 时间，支持分、时、日、月、星期的5 域表达式，支持通配符半角逗号（,）、 半角问号（?）、短划线（-）、星号 （*）、井号（#）、正斜线（/）、L和 W。 修改后，RecurrenceType、 RecurrenceValue和 RecurrenceEndTime参数需要同时有效。 |
|---|---|---|---|---|
| TaskEnabled | Boolean | 否 | true | 是否启动定时任务。 true：启动定时任务。 false：停止定时任务。 |
| LaunchExpiratio nTime | Integer | 否 | 600 | 定时任务触发操作失败后，在此时间内重试。单位：秒，取值范围：0~21600。 |
| MinValue | Integer | 否 | 0 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的最小数量。 |
| MaxValue | Integer | 否 | 10 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的最大数量。 |
| DesiredCapacity | Integer | 否 | 10 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的期望实例数。 说明伸缩组必须支持设置期望实例数，即在创建该伸缩组时指定了DesiredCapacity。 |

弹性伸缩 ESS

| ScalingGroupIdI nvalid | String | 否 | asg- bp18p2yfxow2dl oq**** | 定时任务触发时需要修改实例数量的伸缩组，填写伸缩组ID。指定ScalingGroupId 后，定时任务的伸缩方式为设置伸缩组内实例数量，您需要为MinValue、 MaxValue和DesiredCapacity中至少一个参数指定数量。 说明不支持同时设置 ScheduledAction和 ScalingGroupId。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http://ess.example.com/?Action=ModifyScheduledTask &ScheduledTaskId=edRtShc57WGXdt8TlPbr**** &LaunchTime=2014-08-18T10:52Z &RecurrenceEndTime=2014-08-20T16:55Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScheduledTaskI d.NotFound | The specified scheduled task does not exist. | 指定的定时任务在该用户账号下不存在。 |

弹性伸缩 ESS

| 400 | InvalidScheduledTask Name.Duplicate | The specified value of parameter ScheduledTaskName is duplicated. | 定时任务名已存在。 |
|---|---|---|---|
| 400 | ScheduledAction.Regio nMismatch | The specified scheduled task and the specified scheduled action are not in the same Region. | 指定的ScheduledAction 与定时任务所在的地域不匹配。 |

|  |  | ScheduledTaskName |
|---|---|---|
| e.Duplicate |  |  |

#### DescribeScheduledTasks

**接口说明**

您可以通过定时任务的ID、定时任务的名称、定时任务执行的伸缩规则等查询定时任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSchedul edTasks | 系统规定参数，取值： DescribeScheduledTasks。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 定时任务所属伸缩组的地域ID。 |
| PageNumber | Integer | 否 | 1 | 定时任务列表的页码，起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 50 | 分页查询时设置的每页行数，最大值： 50。 默认值：10。 |
| ScheduledAction .N | RepeatL ist | 否 | ari:acs:ess:cn- qingdao-env17- d01:101582792 734****:scalingr ule/asr- 1kx06vd223809 dlb**** | ScheduledAction.N为对应定时任务在触发时需要执行的操作，N的取值范围：1～ 20。 |
| ScheduledTaskId .N | RepeatL ist | 否 | edRtShc57WGX dt8TlPbr**** | ScheduledTaskId.N为待查询定时任务的 ID，N的取值范围：1～20。 |

弹性伸缩 ESS

| ScheduledTaskN ame.N | RepeatL ist | 否 | scheduled**** | ScheduledTaskName.N为待查询定时任务的名称，N的取值范围：1～20。 |
|---|---|---|---|---|
| ScalingGroupId | String | 否 | asg- bp1bo5tca4m56 nap**** | 执行定时任务的伸缩组的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 50 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| ScheduledTas ks | Array of ScheduledTas k |  | 定时任务信息组成的集合。 |
| ScheduledTas k |  |  |  |
| Description | String | fortest | 定时任务的描述信息。 |
| DesiredCapaci ty | Integer | 10 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的期望实例数。 |
| LaunchExpirati onTime | Integer | 600 | 定时任务触发操作失败后，在此时间内重试。单位为秒，取值范围：0~21600。 |
| LaunchTime | String | 2014-08- 18T10:52Z | 定时任务触发的时间点。 |
| MaxValue | Integer | 10 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的最大数量。 |
| MinValue | Integer | 0 | 定时任务的伸缩方式为设置伸缩组内实例数量时，指定伸缩组内实例的最小数量。 |
| RecurrenceEn dTime | String | 2014-08- 20T16:55Z | 重复执行定时任务的结束时间。 |
| RecurrenceTy pe | String | Daily | 重复执行定时任务的类型。 |

弹性伸缩 ESS

| RecurrenceVal ue | String | 1 | 重复执行定时任务的数值。 |  |  |  |
|---|---|---|---|---|---|---|
| ScalingGroupI d | String | asg- bp1bo5tca4m56na p**** | 执行定时任务的伸缩组的ID。 |  |  |  |
| ScheduledActi on | String | ari:acs:ess:cn- qingdao-env17- d01:134****:scalin grule/cCBpdYdQuB e2cUxOdu6**** | 定时任务触发时执行的伸缩规则。 说明 ScheduledAction 和 ScalingGrou pId 不会同时存在。 |  |  |  |
|  |  |  |  | ScalingGrou |  |  |
| ScheduledTas kId | String | edRtShc57WGXdt8 TlPbr**** | 定时任务的ID。 |  |  |  |
| ScheduledTas kName | String | edRtShc57WGXdt8 TlPbr**** | 定时任务的名称。 |  |  |  |
| TaskEnabled | Boolean | true | 是否启动定时任务。 |  |  |  |
| TotalCount | Integer | 1 | 定时任务总数。 |  |  |  |

|  |  |  | ScheduledAction |
|---|---|---|---|
| 6**** |  | pId |  |

**示例**

请求示例

```
http://ess.example.com/?Action=DescribeScheduledTasks &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式弹性伸缩 ESS

```xml
      <ScheduledTasks>
            <ScheduledTask>
                  <LaunchExpirationTime>600</LaunchExpirationTime>
                  <RecurrenceType>Daily</RecurrenceType>
                  <RecurrenceEndTime>2020-03-02T00:00Z</RecurrenceEndTime>
                  <ScalingGroupId>asg-****</ScalingGroupId>
                  <TaskEnabled>false</TaskEnabled>
                  <ScheduledTaskName>demo1</ScheduledTaskName>
                  <MaxValue>1</MaxValue>
                  <LaunchTime>2020-03-01T00:00Z</LaunchTime>
                  <ScheduledTaskId>cV0bJbAXpipdbFI1NbM****</ScheduledTaskId>
                  <RecurrenceValue>31</RecurrenceValue>
            </ScheduledTask>
            <ScheduledTask>
                  <LaunchExpirationTime>600</LaunchExpirationTime>
                  <MinValue>1</MinValue>
                  <RecurrenceType>Daily</RecurrenceType>
                  <RecurrenceEndTime>2020-02-27T00:00Z</RecurrenceEndTime>
                  <ScalingGroupId>asg-****</ScalingGroupId>
                  <TaskEnabled>true</TaskEnabled>
                  <ScheduledTaskName>demo2</ScheduledTaskName>
                  <LaunchTime>2020-02-26T00:00Z</LaunchTime>
                  <ScheduledTaskId>cD3G3pesE65NcSTmkld1****</ScheduledTaskId>
                  <RecurrenceValue>31</RecurrenceValue>
            </ScheduledTask>
      </ScheduledTasks>
      <PageNumber>1</PageNumber>
      <TotalCount>34</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>4CF33369-7318-4BD5-BE1C-A776BA2C6627</RequestId>
```

`JSON` 格式弹性伸缩 ESS

```json
{
 "ScheduledTasks": {
  "ScheduledTask": [
   {
    "LaunchExpirationTime": 600,
    "RecurrenceType": "Daily",
    "RecurrenceEndTime": "2020-03-02T00:00Z",
    "ScalingGroupId": "asg-****",
    "TaskEnabled": false,
    "ScheduledTaskName": "demo1",
    "MaxValue": 1,
    "LaunchTime": "2020-03-01T00:00Z",
    "ScheduledTaskId": "cV0bJbAXpipdbFI1NbM****",
    "RecurrenceValue": "31"
   },
   {
    "LaunchExpirationTime": 600,
    "MinValue": 1,
    "RecurrenceType": "Daily",
    "RecurrenceEndTime": "2020-02-27T00:00Z",
    "ScalingGroupId": "asg-****",
    "TaskEnabled": true,
    "ScheduledTaskName": "demo2",
    "LaunchTime": "2020-02-26T00:00Z",
    "ScheduledTaskId": "cD3G3pesE65NcSTmkld1****",
    "RecurrenceValue": "31"
   }
```

]

```json
 },
 "PageNumber": 1,
 "TotalCount": 34,
 "PageSize": 10,
 "RequestId": "4CF33369-7318-4BD5-BE1C-A776BA2C6627"
}
```

#### DeleteScheduledTask

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteSchedule dTask | 系统规定参数，取值： DeleteScheduledTask。 |
| ScheduledTaskId | String | 是 | edRtShc57WGX dt8TlPbr**** | 定时任务的ID。您可以调用 DescribeScheduledTasks参数查询定时任务的ID。 |

**返回数据**

弹性伸缩 ESS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http://ess.example.com/?Action=DeleteScheduledTask &ScheduledTaskId=edRtShc57WGXdt8TlPbr****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScheduledTaskI d.NotFound | The specified scheduled task does not exist. | 指定的定时任务在该账号下不存在。 |

### 报警任务

#### CreateAlarm

**接口说明**

如果您创建自定义监控类型的报警任务（MetricType=custom），您需要先将自定义监控项指标上报到云监控。具体操作，请参见弹性伸缩的自定义监控报警任务章节。 创建报警任务时，您需要指定监控项（MetricName），并配合维度信息 （Dimension.N.DimensionKey和Dimension.N.DimensionValue），来确定伸缩组中该监控项数据的聚合范围。例如，指定user_id和scaling_group来确定聚合该用户、该伸缩组下所有ECS实例或ECI实例的监控项数据。 自定义监控报警任务（MetricType=custom）的监控项取决于您自有的监控指标。 弹性伸缩 ESS 系统监控报警任务（MetricType=system）支持的监控项的更多信息，请参见弹性伸缩的系统监控报警任务章节。 维度信息中，user_id和scaling_group由系统自动填充，device、state需要您手动指

**说明**

定。更多信息，请参见 `Dimension.N.DimensionKey` 和 `Dimension.N.DimensionValue` 参数。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateAlarm | 系统规定参数，取值：CreateAlarm。 |

弹性伸缩 ESS

| MetricName | String | 是 | CpuUtilization | 监控项名称。取值范围与报警任务的监控类型有关： 当报警任务为自定义监控类型（即 MetricType=custom）时，取值范围是您自有的监控项范围。 当报警任务为系统监控类型（即 MetricType=system）时，取值范围如下： CpuUtilization：（ECS）CPU使用率（%）。 IntranetTx：（ECS）内网出流量 （KByte/min）。 IntranetRx：（ECS）内网入流量 （KByte/min）。 VpcInternetTx：（ECS）外网出流量（KByte/min）。 VpcInternetRx：（ECS）外网入流量（KByte/min）。 SystemDiskReadBps：（ECS）系统盘读BPS（Byte/s）。 SystemDiskWriteBps：（ECS）系统盘写BPS（Byte/s）。 SystemDiskReadOps：（ECS）系统盘读IOPS（次/s）。 SystemDiskWriteOps：（ECS） 系统盘写IOPS（次/s）。 CpuUtilizationAgent： （Agent）CPU使用率（%）。 GpuUtilizationAgent： （Agent）GPU使用率（%）。 GpuMemoryFreeUtilizationAgent ：（Agent）GPU内存空闲率 （%）。 GpuMemoryUtilizationAgent： （Agent）GPU内存使用率（%）。 MemoryUtilization：（Agent）内存（%）。 LoadAverage：（Agent）系统平均负载。 TcpConnection：（Agent）TCP总连接数（个）。 TcpConnection：（Agent）TCP已建立连接数（个）。 PackagesNetOut：（Agent）内网网卡发包数（个）。 PackagesNetIn：（Agent）内网网卡收包数（个）。 EciPodCpuUtilization：CPU使用率 （%）。 EciPodMemoryUtilization：内存 （%）。 更多信息，请参见弹性伸缩的系统监控报警任务章节。 |
|---|---|---|---|---|

弹性伸缩 ESS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |
|---|---|---|---|---|
| ScalingGroupId | String | 是 | asg- bp18p2yfxow2dl oq**** | 报警任务关联的伸缩组的ID。 |
| Threshold | Float | 是 | 80.0 | 监控指标的阈值，满足阈值表达式达到指定次数即触发执行伸缩规则。 |
| Name | String | 否 | TestAlarmTask | 报警任务的名称。 |
| Description | String | 否 | Test alarm task. | 报警任务的描述。 |
| MetricType | String | 否 | system | 监控项类型，取值范围： system：使用云监控系统指标。 custom：使用上报到云监控的自定义指标。 |
| Period | Integer | 否 | 300 | 统计监控项数据的周期，单位为秒，取值范围： 15。 60。 120。 300。 900。 说明 15秒的统计周期仅适合监控ECS类型伸缩组时，使用云监控 （Agent开头的监控项）客户端采集的监控项指标，除此之外的其他监控项指标的统计周期可以设置为60秒、 120秒、300秒和900秒。 默认值：300。 |
| Statistics | String | 否 | Average | 统计监控项数据的方法，取值范围： Average：平均值。 Minimun：最小值。 Maximum：最大值。 默认值：Average。 |

弹性伸缩 ESS

| ComparisonOper ator | String | 否 | >= | 监控项统计值与阈值的比较符，用于指定监控项统计值与阈值在什么关系下满足条件。取值范围： 监控项统计值大于等于阈值。取值： >=。 监控项统计值小于等于阈值。取值： <=。 监控项统计值大于阈值。取值：>。 监控项统计值小于阈值。取值：<。 默认值：>=。 |  |  |  |
|---|---|---|---|---|---|---|---|
| EvaluationCount | Integer | 否 | 3 | 触发执行伸缩规则需要满足阈值表达式的次数，例如，CPU使用率平均值3次的统计结果均大于等于80%。 默认值：3。 |  |  |  |
| GroupId | Integer | 否 | 4055401 | 自定义监控项所属云监控应用分组的ID， 仅在监控项类型为 custom 时需要指定该参数。 |  |  |  |
| Effective | String | 否 | TZ=+00 * * 1-2 * * ? | 指定报警任务的生效时间段，默认所有时间都生效。 该参数遵循Cron表达式，默认格式为 X X X X X ? ，含义如下： X ：一个域的占位符，依次表示秒、 分钟、小时、日期和月。X可以是确定的取值，也可以是具有逻辑意义的特殊字符。X的取值范围，请参见报警任务概述章节的Cron表达式。 ？ ：表示不指定值。 说明该参数指定值默认为 UTC+8时区，支持在Cron表达式之前添加时区信息TZ=+yy来指定时区，其中y表示时区的数值。例如， TZ=+00 * * 1-2 * * ? 表示报警任务在UTC+0时区每天 01:00~02:59之间生效。 取值示例及含义如下： * * * * * ? ：所有时间都生效。 * * 17-18 * * ? ：在UTC+8 时区每天17:00~18:59之间生效。 TZ=+00 * * 1-2 * * ? ：在 UTC+0时区每天01:00~02:59之间生效。 |  |  |  |
|  |  |  |  |  |  | X |  |
|  |  |  |  |  | ? |  |  |

弹性伸缩 ESS

| AlarmAction.N | RepeatL ist | 否 | ari:acs:ess:cn- hangzhou- env17- d01:1406926*** *:scalingrule/asr - bp163l21e07uh n**** | 报警任务关联伸缩规则的唯一标识符。 |
|---|---|---|---|---|
| Dimension.N.Di mensionKey | String | 否 | device | 监控项关联的维度信息键。取值范围与报警任务的监控类型有关： 当报警任务为自定义监控类型（即 MetricType=custom）时，不限制取值范围，由您自行指定。 当报警任务为系统监控类型（即 MetricType=system）时，取值范围如下： user id：您的账号ID。 _ scaling group：被监控的伸缩组。 _ device：网卡设备的类型。 state：TCP连接的状态。 |
| Dimension.N.Di mensionValue | String | 否 | eth0 | 监控项关联的维度信息值，取值范围由 Dimension.N.DimensionKey决定： 当Dimension.N.DimensionKey的取值是自定义的，即报警任务是自定义监控类型（即MetricType=custom） 时，该参数不限制取值范围，由您自行指定。 当Dimension.N.DimensionKey的取值是系统指定的取值范围中的，即报警任务为系统监控类型（即 MetricType=system）时，该参数取值范围如下： user id：由系统自动填充。 _ scaling group：由系统自动填充。 _ device： eth0：对于经典网络实例，eth0 表示内网网卡。对于VPC实例，只存在eth0一张网卡。 eth1：对于经典网络实例，eth1 代表外网网卡。 state： TCP TOTAL：表示总的TCP连接 _ 数。 ESTABLISHED：表示已建立的 TCP连接数。 |

**返回数据**

弹性伸缩 ESS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AlarmTaskId | String | asg- bp1hvbnmkl10vll5* *** f95ce797- _ dc2e-4bad-9618- 14fee7d1**** | 报警任务ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou-env17-d01 &Name=TestAlarmTask &Description=Test alarm task. &ScalingGroupId=asg-bp18p2yfxow2dloq**** &MetricName=CpuUtilization &MetricType=system &Period=300 &Statistics=Average &Threshold=80.0 &ComparisonOperator=>= &EvaluationCount=3 &GroupId=4055401 &Effective=TZ=+00 * * 1-2 * * ? &AlarmAction=["ari:acs:ess:cn-hangzhou-env17-d01:1406926****:scalingrule/asr-bp163l21e0 7uhn****"] &Dimension=[{"DimensionKey":"device","DimensionValue":"eth0"}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <AlarmTaskId>asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1****</AlarmTa
skId>
    <RequestId>ADD82C07-7A7C-4DD4-907F-1D114742****</RequestId>
```

`JSON` 格式

```json
{
        "AlarmTaskId": "asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1****",
        "RequestId": "ADD82C07-7A7C-4DD4-907F-1D114742****"
}
```

**错误码**

弹性伸缩 ESS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidParameter | The specified value of parameter "%s" is not valid. | 指定参数“%s”不合法。 |

#### DescribeAlarms

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAlarms | 系统规定参数，取值： DescribeAlarms。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 报警任务所属地域的ID。 |
| ScalingGroupId | String | 否 | asg- bp18p2yfxow2dl oq**** | 报警任务关联的伸缩组的ID。 |
| AlarmTaskId | String | 否 | asg- bp1hvbnmkl10vl l5**** f95ce797 _ -dc2e-4bad- 9618- 14fee7d1**** | 报警任务ID。 |
| State | String | 否 | OK | 报警任务的状态，取值范围： ALARM：报警，已满足报警条件。 OK：正常，尚未满足报警条件。 INSUFFICIENT DATA：数据不足，不 _ 足以判断是否满足了报警条件。 |
| IsEnable | Boolean | 否 | true | 报警任务是否启用，取值范围： true：已启用。 false：已停用。 |
| MetricType | String | 否 | system | 监控项类型，取值范围： system：使用云监控系统指标。 custom：使用上报到云监控的自定义指标。 |
| MetricName | String | 否 | CpuUtilization | 报警任务的名称。 |

弹性伸缩 ESS

| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。最大值： 50。 默认值：10。 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 报警任务列表的页码。起始值：1。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AlarmList | Array of Alarm |  | 报警任务的列表。 |
| Alarm |  |  |  |
| AlarmActions | List | ari:acs:ess:cn- qingdao-env17- d01:1344371:scali ngrule/eMKWG8SR Nb9dBLAjweN**** | 报警任务关联伸缩规则的唯一标识符的列表。 |
| AlarmTaskId | String | asg- bp1hvbnmkl10vll5* *** f95ce797- _ dc2e-4bad-9618- 14fee7d1**** | 报警任务ID。 |
| ComparisonOp erator | String | >= | 监控项统计值与阈值的比较符，用于指定监控项统计值与阈值在什么关系下满足条件。可能值： 监控项统计值大于等于阈值。取值：>=。 监控项统计值小于等于阈值。取值：<=。 监控项统计值大于阈值。取值：>。 监控项统计值小于阈值。取值：<。 |
| Description | String | Test alarm task. | 报警任务的描述。 |
| Dimensions | Array of Dimension |  | 监控项关联的维度信息。 |
| Dimension |  |  |  |
| DimensionKey | String | device | 监控项关联的维度信息键，可能值： user id：您的账号ID。 _ scaling group：被监控的伸缩组。 _ device：网卡设备的类型。 state：TCP连接的状态。 |

弹性伸缩 ESS

| DimensionValu e | String | eth0 | 监控项关联的维度信息值，可能值由维度信息键决定。 user id：由系统自动填充。 _ scaling group：由系统自动填充。 _ device可能值： eth0：对于经典网络实例，eth0表示内网网卡。对于VPC实例，只存在eth0一张网卡。 eth1：对于经典网络实例，eth1代表外网网卡。 state可能值： TCP TOTAL：表示总的TCP连接数。 _ ESTABLISHED：表示已建立的TCP连接数。 |
|---|---|---|---|
| Effective | String | Test | 说明该参数正在邀测中，暂未开放使用。 |
| Enable | Boolean | true | 报警任务是否启用，可能值： true：已启用。 false：已停用。 |
| EvaluationCou nt | Integer | 3 | 触发执行伸缩规则需要满足阈值表达式的次数， 例如，CPU使用率平均值3次的统计结果均大于等于80%。 |

弹性伸缩 ESS

| MetricName | String | CpuUtilization | 监控项名称。可能值： CpuUtilization：（ECS）CPU使用率 （%）。 IntranetTx：（ECS）内网出流量 （KByte/min）。 IntranetRx：（ECS）内网入流量 （KByte/min）。 VpcInternetTx：（ECS）外网出流量 （KByte/min）。 VpcInternetRx：（ECS）外网入流量 （KByte/min）。 SystemDiskReadBps：（ECS）系统盘读 BPS（Byte/s）。 SystemDiskWriteBps：（ECS）系统盘写 BPS（Byte/s）。 SystemDiskReadOps：（ECS）系统盘读 IOPS（次/s）。 SystemDiskWriteOps：（ECS）系统盘写 IOPS（次/s）。 CpuUtilizationAgent：（Agent）CPU使用率（%）。 GpuUtilizationAgent：（Agent）GPU使用率（%）。 GpuMemoryFreeUtilizationAgent： （Agent）GPU内存空闲率（%）。 GpuMemoryUtilizationAgent： （Agent）GPU内存使用率（%）。 MemoryUtilization：（Agent）内存 （%）。 LoadAverage：（Agent）系统平均负载。 TcpConnection：（Agent）TCP总连接数 （个）。 TcpConnection：（Agent）TCP已建立连接数（个）。 PackagesNetOut：（Agent）内网网卡发包数（个）。 PackagesNetIn：（Agent）内网网卡收包数（个）。 EciPodCpuUtilization：CPU使用率（%）。 EciPodMemoryUtilization：内存（%）。 更多信息，请参见弹性伸缩的系统监控报警任务章节。 |
|---|---|---|---|
| MetricType | String | system | 监控项类型，可能值： system：使用云监控系统指标。 custom：使用上报到云监控的自定义指标。 |
| Name | String | TestAlarmTask | 报警任务的名称。 |

弹性伸缩 ESS

| Period | Integer | 300 | 统计监控项数据的周期，单位为秒。可能值： 15。 60。 120。 300。 900。 说明仅当监控ECS类型伸缩组时， 使用云监控（Agent开头的监控项）客户端采集的监控项指标，才可以选择15秒的统计周期。 |
|---|---|---|---|
| ScalingGroupI d | String | asg- bp18p2yfxow2dloq **** | 报警任务关联的伸缩组的ID。 |
| State | String | ALARM | 报警任务的状态，可能值： ALARM：报警，已满足报警条件。 OK：正常，尚未满足报警条件。 INSUFFICIENT DATA：数据不足，不足以判 _ 断是否满足了报警条件。 |
| Statistics | String | Average | 统计监控项数据的方法，可能值： Average：平均值。 Minimun：最小值。 Maximum：最大值。 |
| Threshold | Float | 80.0 | 监控指标的阈值，满足阈值表达式达到指定次数即触发执行伸缩规则。 |
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页行数。 |
| RequestId | String | 871C7C53-34A4- 45AA-8C14- 4B72FA6A**** | 请求ID。 |
| TotalCount | Integer | 2 | 报警任务的总数。 |

**示例**

请求示例弹性伸缩 ESS

```
&RegionId=cn-qingdao-env17-d01 &ScalingGroupId=asg-bp18p2yfxow2dloq**** &AlarmTaskId=asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1**** &State=OK &IsEnable=true &MetricType=system &MetricName=CpuUtilization &PageSize=10 &PageNumber=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>2</TotalCount> <PageSize>10</PageSize> <RequestId>871C7C53-34A4-45AA-8C14-4B72FA6A****</RequestId> <PageNumber>1</PageNumber> <AlarmList>
    <ComparisonOperator>&gt;=</ComparisonOperator>
    <Description>Test alarm task.</Description>
    <ScalingGroupId>asg-bp18p2yfxow2dloq****</ScalingGroupId>
    <MetricType>system</MetricType>
    <EvaluationCount>3</EvaluationCount>
    <Period>300</Period>
    <Statistics>Average</Statistics>
    <Effective>Test</Effective>
    <Name>TestAlarmTask</Name>
    <MetricName>CpuUtilization</MetricName>
    <State>ALARM</State>
    <Enable>true</Enable>
    <AlarmTaskId>asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1****</AlarmTa
skId>
    <Threshold>80.0</Threshold>
    <Dimensions>
        <DimensionValue>eth0</DimensionValue>
        <DimensionKey>device</DimensionKey>
    </Dimensions>
    <AlarmActions>ari:acs:ess:cn-qingdao-env17-
d01:1344371:scalingrule/eMKWG8SRNb9dBLAjweN****</AlarmActions> </AlarmList>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "871C7C53-34A4-45AA-8C14-4B72FA6A****",
    "PageNumber": 1,
    "AlarmList": {
        "ComparisonOperator": "&gt;=",
        "Description": "Test alarm task.",
        "ScalingGroupId": "asg-bp18p2yfxow2dloq****",
        "MetricType": "system",
        "EvaluationCount": 3,
        "Period": 300,
        "Statistics": "Average",
        "Effective": "Test",
        "Name": "TestAlarmTask",
        "MetricName": "CpuUtilization",
        "State": "ALARM",
        "Enable": true,
        "AlarmTaskId": "asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1****",
        "Threshold": 80,
        "Dimensions": {
            "DimensionValue": "eth0",
            "DimensionKey": "device"
        },
        "AlarmActions": "ari:acs:ess:cn-qingdao-env17-
d01:1344371:scalingrule/eMKWG8SRNb9dBLAjweN****"
    }
}
```

#### ModifyAlarm

**接口说明**

如果您创建自定义监控类型的报警任务（MetricType=custom），您需要先将自定义监控项指标上报到云监控。具体操作，请参见弹性伸缩的自定义监控报警任务章节。 创建报警任务时，您需要指定监控项（MetricName），并配合维度信息 （ `Dimension.N.DimensionKey` 和 `Dimension.N.DimensionValue` ），来确定伸缩组中该监控项数据的聚合范围。例如，指定user_id和scaling_group来确定聚合该用户、该伸缩组下所有ECS实例或ECI 实例的监控项数据。 自定义监控报警任务（MetricType=custom）的监控项取决于您自有的监控指标。 系统监控报警任务（MetricType=system）支持的监控项的更多信息，请参见弹性伸缩的系统监控报警任务章节。 维度信息中，user_id和scaling_group由系统自动填充，device、state需要您手动指

**说明**

定。更多信息，请参见 `Dimension.N.DimensionKey` 和 `Dimension.N.DimensionValue` 参数。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

弹性伸缩 ESS

| Action | String | 是 | ModifyAlarm | 系统规定参数，取值：ModifyAlarm。 |
|---|---|---|---|---|
| AlarmTaskId | String | 是 | asg- bp1hvbnmkl10vl l5**** f95ce797 _ -dc2e-4bad- 9618- 14fee7d1**** | 报警任务的ID。 |
| RegionId | String | 是 | cn-hangzhou- env17-d01 | 报警任务所属地域的ID。 |
| Name | String | 否 | TestAlarmTask | 报警任务的名称。 |
| Description | String | 否 | Test alarm task. | 报警任务的描述。 |

弹性伸缩 ESS

| MetricName | String | 否 | MemoryUtilizatio n | 监控项名称。取值范围与报警任务的监控类型有关： 当报警任务为自定义监控类型（即 MetricType=custom）时，取值范围是您自有的监控项范围。 当报警任务为系统监控类型（即 MetricType=system）时，取值范围如下： CpuUtilization：（ECS）CPU使用率（%）。 IntranetTx：（ECS）内网出流量 （KByte/min）。 IntranetRx：（ECS）内网入流量 （KByte/min）。 VpcInternetTx：（ECS）外网出流量（KByte/min）。 VpcInternetRx：（ECS）外网入流量（KByte/min）。 SystemDiskReadBps：（ECS）系统盘读BPS（Byte/s）。 SystemDiskWriteBps：（ECS）系统盘写BPS（Byte/s）。 SystemDiskReadOps：（ECS）系统盘读IOPS（次/s）。 SystemDiskWriteOps：（ECS） 系统盘写IOPS（次/s）。 CpuUtilizationAgent： （Agent）CPU使用率（%）。 GpuUtilizationAgent： （Agent）GPU使用率（%）。 GpuMemoryFreeUtilizationAgent ：（Agent）GPU内存空闲率 （%）。 GpuMemoryUtilizationAgent： （Agent）GPU内存使用率（%）。 MemoryUtilization：（Agent）内存（%）。 LoadAverage：（Agent）系统平均负载。 TcpConnection：（Agent）TCP总连接数（个）。 TcpConnection：（Agent）TCP已建立连接数（个）。 PackagesNetOut：（Agent）网卡发包数（个）。 PackagesNetIn：（Agent）网卡收包数（个）。 EciPodCpuUtilization：CPU使用率 （%）。 EciPodMemoryUtilization：内存 （%）。 更多信息，请参见弹性伸缩的系统监控报警任务章节。 |
|---|---|---|---|---|

弹性伸缩 ESS

| MetricType | String | 否 | system | 监控项类型，取值范围： system：使用云监控系统指标。 custom：使用上报到云监控的自定义指标。 |
|---|---|---|---|---|
| Period | Integer | 否 | 300 | 统计监控项数据的周期，单位：秒。取值范围： 15。 60。 120。 300。 900。 说明 15秒的统计周期仅适合监控ECS类型伸缩组时，使用云监控 （Agent开头的监控项）客户端采集的监控项指标，除此之外的其他监控项指标的统计周期可以设置为60秒、 120秒、300秒和900秒。 |
| Statistics | String | 否 | Average | 统计监控项数据的方法，取值范围： Average：平均值。 Minimun：最小值。 Maximum：最大值。 |
| Threshold | Float | 否 | 80.0 | 监控指标的阈值，满足阈值表达式达到指定次数即触发执行伸缩规则。 |
| ComparisonOper ator | String | 否 | >= | 监控项统计值与阈值的比较符，用于指定监控项统计值与阈值在什么关系下满足条件。取值范围： 监控项统计值大于等于阈值。取值： >=。 监控项统计值小于等于阈值。取值： <=。 监控项统计值大于阈值。取值：>。 监控项统计值小于阈值。取值：<。 |
| EvaluationCount | Integer | 否 | 3 | 触发执行伸缩规则需要满足阈值表达式的次数，例如，CPU使用率平均值3次的统计结果均大于等于80%。 |
| GroupId | Integer | 否 | 4055401 | 自定义监控项所属云监控应用分组的ID， 仅在监控项类型为 custom 时需要指定该参数。 |

弹性伸缩 ESS

| Effective | String | 否 | TZ=+00 * * 1-2 * * ? | 指定报警任务的生效时间段。 该参数遵循Cron表达式，默认格式为 X X X X X ? ，含义如下： X ：一个域的占位符，依次表示秒、 分钟、小时、日期和月。X可以是确定的取值，也可以是具有逻辑意义的特殊字符。X的取值范围，请参见Cron表达式。 ？ ：表示不指定值。 说明该参数指定值默认为 UTC+8时区，支持在Cron表达式之前添加时区信息TZ=+yy来指定时区，其中y表示时区的数值。例如， TZ=+00 * * 1-2 * * ? 表示报警任务在UTC+0时区每天01:00~02:59之间生效。 取值示例及含义如下： * * * * * ? ：所有时间都生效。 * * 17-18 * * ? ：在UTC+8 时区每天17:00~18:59之间生效。 TZ=+00 * * 1-2 * * ? ：在 UTC+0时区每天01:00~02:59之间生效。 |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | X |  |
| AlarmAction.N | RepeatL ist | 否 | ari:acs:ess:cn- hangzhou- env17- d01:140692647 ****:scalingrule/ asr- bp163l21e07uh n**** | 报警任务关联伸缩规则的唯一标识符。 |  |  |
| Dimension.N.Di mensionKey | String | 否 | device | 监控项关联的维度信息键。取值范围与报警任务的监控类型有关： 当报警任务为自定义监控类型（即 MetricType=custom）时，不限制取值范围，由您自行指定。 当报警任务为系统监控类型（即 MetricType=system）时，取值范围如下： user id：您的账号ID。 _ scaling group：被监控的伸缩组。 _ device：网卡设备的类型。 state：TCP连接的状态。 |  |  |

|  |  | ? |
|---|---|---|

弹性伸缩 ESS

| Dimension.N.Di mensionValue | String | 否 | eth0 | 监控项关联的维度信息值，取值范围由 Dimension.N.DimensionKey 决定： 当 Dimension.N.DimensionKey 的取值是自定义的，即报警任务是自定义监控类型（即 MetricType=custom）时，该参数不限制取值范围，由您自行指定。 当 Dimension.N.DimensionKey 的取值是系统指定的取值范围中的，即报警任务为系统监控类型（即 MetricType=system）时，该参数取值范围如下： user id：由系统自动填充。 _ scaling group：由系统自动填充。 _ device： eth0：对于经典网络实例，eth0 表示内网网卡。对于VPC实例，只存在eth0一张网卡。 eth1：对于经典网络实例，eth1 代表外网网卡。 state： TCP TOTAL：表示总的TCP连接 _ 数。 ESTABLISHED：表示已建立的 TCP连接数。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AlarmTaskId | String | asg- bp1hvbnmkl10vll5* *** 83948190- _ acdd-483f-98f7- b77f4778**** | 报警任务ID。 |
| RequestId | String | BACACF83-7070- 4953-A8FD- D81F89F1**** | 请求ID。 |

**示例**

请求示例弹性伸缩 ESS

```
&RegionId=cn-hangzhou-env17-d01 &AlarmTaskId=asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1**** &Name=alarmtask**** &Description=Test alarm task. &MetricName=MemoryUtilization &MetricType=system &Period=300 &Statistics=Average &Threshold=80.0 &ComparisonOperator=>= &EvaluationCount=3 &GroupId=4055401 &Effective=TZ=+00 * * 1-2 * * ? &AlarmAction=["ari:acs:ess:cn-hangzhou-env17-d01:140692647****:scalingrule/asr-bp163l21 e07uhn****"] &Dimension=[{"DimensionKey":"device","DimensionValue":"eth0"}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <AlarmTaskId>asg-bp1hvbnmkl10vll5****_83948190-acdd-483f-98f7-b77f4778****</AlarmTa
skId>
    <RequestId>BACACF83-7070-4953-A8FD-D81F89F1****</RequestId>
```

`JSON` 格式

```json
{
 "AlarmTaskId": "asg-bp1hvbnmkl10vll5****_83948190-acdd-483f-98f7-b77f4778****",
 "RequestId": "BACACF83-7070-4953-A8FD-D81F89F1****"
}
```

#### EnableAlarm

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | EnableAlarm | 系统规定参数，取值：EnableAlarm。 |
| AlarmTaskId | String | 是 | asg- bp1hvbnmkl10vl l5**** f95ce797 _ -dc2e-4bad- 9618- 14fee7d1**** | 报警任务ID。 |

弹性伸缩 ESS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 688B18B8-FB1E- 42EB-A1ED- 7F55B090**** | 请求ID。 |

**示例**

请求示例

```
&AlarmTaskId=asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>688B18B8-FB1E-42EB-A1ED-7F55B090****</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "688B18B8-FB1E-42EB-A1ED-7F55B090****"
}
```

#### DisableAlarm

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DisableAlarm | 系统规定参数，取值：DisableAlarm。 |
| AlarmTaskId | String | 是 | asg- bp1hvbnmkl10vl l5**** f95ce797 _ -dc2e-4bad- 9618- 14fee7d1**** | 报警任务ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。 |

弹性伸缩 ESS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 086EFCD4-C76F- 4DC6-9EE9- 0D9B711E**** | 请求ID。 |

**示例**

请求示例

```
&AlarmTaskId=asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>086EFCD4-C76F-4DC6-9EE9-0D9B711E****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "086EFCD4-C76F-4DC6-9EE9-0D9B711E****"
}
```

#### DeleteAlarm

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteAlarm | 系统规定参数，取值：DeleteAlarm。 |
| AlarmTaskId | String | 是 | asg- bp1hvbnmkl10vl l5**** f95ce797 _ -dc2e-4bad- 9618- 14fee7d1**** | 报警任务ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| AlarmTaskId | String | asg- bp1hvbnmkl10vll5* *** f95ce797- _ dc2e-4bad-9618- 14fee7d1**** | 报警任务ID。 |
|---|---|---|---|
| RequestId | String | 6EF9BFEE-FE07- 4627-B8FB- 14326FB9**** | 请求ID。 |

**示例**

请求示例

```
&AlarmTaskId=asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <AlarmTaskId>asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1****</AlarmTa
skId>
    <RequestId>6EF9BFEE-FE07-4627-B8FB-14326FB9****</RequestId>
```

`JSON` 格式

```json
{
 "AlarmTaskId": "asg-bp1hvbnmkl10vll5****_f95ce797-dc2e-4bad-9618-14fee7d1****",
 "RequestId": "6EF9BFEE-FE07-4627-B8FB-14326FB9****"
}
```

### 生命周期挂钩

#### CreateLifecycleHook

**接口说明**

一个伸缩组最多可以创建6个生命周期挂钩。创建了生命周期挂钩的伸缩组，在发生伸缩活动时，生命周期挂钩会暂停伸缩活动一段时间，具体等待时长可以通过HeartbeatTimeout参数指定。您可以在等待期间进行初始化ECS实例配置、获取ECS实例数据等操作。 弹性扩张活动时，ECS实例添加至RDS实例白名单后进入等待状态，等待状态结束后再加入SLB实例后端服务器组。弹性收缩活动时，ECS实例从SLB实例后端服务器组移出后进入等待状态，等待状态结束后再从 RDS实例白名单移出。 生命周期挂钩可以配置通知方式，支持MNS主题、MNS队列和OOS模板。如果配置OOS模板，您需要为 OOS服务创建RAM角色。具体操作，请参见运维编排服务中的为OOS服务设置RAM权限章节。 弹性伸缩 ESS 如果伸缩组有存量的ECS实例，且配置的OOS模板用于加入或移出除RDS外的其他云数据

**说明**

库白名单，则您必须手动将存量的ECS实例加入云数据库的白名单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateLifecycle Hook | 系统规定参数。取值： CreateLifecycleHook。 |
| LifecycleTransiti on | String | 是 | SCALE OUT _ | 生命周期挂钩适用的伸缩活动类型，取值范围： SCALE OUT：伸缩组弹性扩张活动 _ SCALE IN：伸缩组弹性收缩活动 _ |
| ScalingGroupId | String | 是 | asg- bp1eyv4qn8ssg v43**** | 伸缩组的ID。 |
| LifecycleHookNa me | String | 否 | lifecyclehook*** * | 生命周期挂钩的名称。不能与当前伸缩组其他生命周期挂钩重名，长度为2~64个英文或中文字符，以数字、大小写字母或中文开头，可包含数字、下划线（ ）、短划 _ 线（-）和半角句号（.）。 默认值为生命周期挂钩ID。 |
| DefaultResult | String | 否 | CONTINUE | 等待状态结束后的下一步动作，取值范围： CONTINUE：继续响应弹性扩张活动或者继续响应弹性收缩活动。 ABANDON：直接释放弹性扩张活动创建出来的ECS实例或者直接将弹性收缩活动中的ECS实例从伸缩组移除。 当伸缩组发生弹性收缩活动（SCALE IN） _ 并触发多个生命周期挂钩时，DefaultResult为ABANDON的生命周期挂钩触发的等待状态结束时，会提前将其它对应的等待状态提前结束。其他情况下，下一步动作均以最后一个结束等待状态的下一步动作为准。 默认值：CONTINUE。 |

弹性伸缩 ESS

| HeartbeatTimeo ut |  |  | Integer |  |  |  |  | 生命周期挂钩为伸缩组活动设置的等待时间，等待状态超时后会执行下一步动作。 取值范围：30~21600，单位：秒。 创建了生命周期挂钩后，您可以调用API RecordLifecycleActionHeartbeat 接口延长ECS实例的等待时间，也可以调用API CompleteLifecycleAction 接口提前结束伸缩活动的等待状态。 默认值：600。 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | 否 |  | 600 |  |  |  |  |
| NotificationMeta data |  |  |  |  |  |  |  | 生命周期挂钩暂停伸缩活动时推送给 NotificationArn（通知对象）的通知信息，便于管理和标记不同类别的通知信息。必须同时指定NotificationArn。参数长度不能超过4096个字符。 如果NotificationArn指定为OOS模板，包括公共模板或者自定义模板，则 NotificationMetadata必须指定为JSON 字符串，且与OOS模板的参数相符。 例如， {"dbInstanceId": "dds- |  |  |  |
|  |  |  |  |  |  |  |  |  | {"dbInstanceId": "dds- |  |  |
|  |  |  |  |  |  |  |  | bp17661e0135****", |  |  |  |
|  |  |  |  |  |  |  |  | "modifyMode": |  |  |  |
|  |  |  |  |  |  |  |  | "Append"} |  |  |  |
|  |  |  | String |  | 否 |  | Test lifecycle hook. |  |  |  |  |

弹性伸缩 ESS

| NotificationArn | String | 否 |  |  |  | 生命周期挂钩通知对象标识符，不设置本参数表示不发送通知，设置本参数时支持以下通知方式： 消息服务MNS队列，参数取值格式： acs:mns:{region-id}: |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | acs:mns:{region-id}: |  |
|  |  |  |  |  |  | {account- |  |  |
|  |  |  |  |  |  | id}:queue/{queuename} |  |  |
|  |  |  |  |  |  |  | acs:mns:{region-id}: |  |
|  |  |  |  |  |  | {account- |  |  |
|  |  |  |  |  |  | id}:topic/{topicname} |  |  |
|  |  |  |  |  | acs:mns:cn- beijing-env17- d01:161456884 |  |  |  |
|  |  |  |  |  |  |  | acs:oos:{region-id}: |  |
|  |  |  |  |  | 340****:queue/ | {account- |  |  |
|  |  |  |  |  | modifyLifecycle Ho**** | id}:template/{templatename} |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LifecycleHookI d | String | ash- bp1at9ufhmcf9cmy **** | 生命周期挂钩的D。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=CreateLifecycleHook &ScalingGroupId=asg-bp1eyv4qn8ssgv43**** &LifecycleHookName=lifecyclehook**** &LifecycleTransition=SCALE_OUT &NotificationArn=acs:mns:cn-beijing-env17d01:161456884340****:queue/modifyLifecycleHo**** &NotificationMetadata=Test lifecycle hook.
```

`&<`公共请求参数> 正常返回示例弹性伸缩 ESS `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <LifecycleHookId>ash-bp1at9ufhmcf9cmy****</LifecycleHookId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "LifecycleHookId": "ash-bp1at9ufhmcf9cmy****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParamter | The specified value of parameter is not valid. | 参数值不合法。 |
| 400 | InvalidNotificationArn | The specified parameter notificationArn is invalid. | 指定的NotificationArn不合法。 |
| 400 | UnsupportedNotificatio nType.CurrentRegion | The notificationType is not supported in the special region which scalingGroup belongs to. | 当前地域不支持该通知方式。 |
| 400 | QueueNotExist | The specified queue does not exist. | 指定的MNS队列不存在。 |
| 400 | TopicNotExist | The specified topic does not exist. | 指定的MNS主题不存在。 |
| 400 | InvalidLifecycleHookN ame.Duplicate | The specified value of parameter lifecycleHookName is duplicated. | 生命周期挂钩已存在。 |
| 400 | QuotaExceeded.Lifecy cleHook | Lifecycle hook quota exceeded in the specified scaling group. | 一个伸缩组最多可以创建 6个生命周期挂钩。 |

弹性伸缩 ESS

#### ModifyLifecycleHook

**接口说明**

```
略 ScalingGroupId 和 LifecycleHookName 参数。
```

同时指定伸缩组ID（ `ScalingGroupId` ）与生命周期挂钩名称（ `LifecycleHookName` ）。

**请求参数**

| 名称 | 类型 |  | 是否必选 | 示例值 | 描述 |  |
|---|---|---|---|---|---|---|
| Action | String |  | 是 | ModifyLifecycleH ook | 系统规定参数，取值： ModifyLifecycleHook。 |  |
| LifecycleHookId | String |  | 否 | ash- bp1fxuqyi98w0a ib**** | 待修改生命周期挂钩的ID，用于指定生命周期挂钩。 |  |
| ScalingGroupId | String |  | 否 | asg- bp18p2yfxow2dl oq**** | 伸缩组的ID，用于指定生命周期挂钩。 |  |
| LifecycleHookNa me | String |  | 否 | test SCALE IN _ _ | 待修改生命周期挂钩的名称，用于指定生命周期挂钩。 |  |
| DefaultResult | String |  | 否 | CONTINUE | 等待状态结束后的下一步动作，取值范围： CONTINUE：继续响应弹性扩张活动或者继续响应弹性收缩活动。 ABANDON：直接释放弹性扩张活动创建出来的ECS实例或者直接将弹性收缩活动中的ECS实例从伸缩组移除。 当伸缩组发生弹性收缩活动（SCALE IN） _ 并触发多个生命周期挂钩时，DefaultResult为ABANDON的生命周期挂钩触发的等待状态结束时，会提前将其它对应的等待状态提前结束。其他情况下，下一步动作均以最后一个结束等待状态的下一步动作为准。 |  |
| HeartbeatTimeo ut | Integer |  | 否 | 600 | 生命周期挂钩为伸缩组活动设置的等待时间，等待状态超时后会执行下一步动作。 取值范围：30~21600，单位：秒。 您可以调用API RecordLifecycleActionHeartbeat 接口延长ECS实例的等待时间，也可以调用API CompleteLifecycleAction 接口提前结束伸缩活动的等待状态。 |  |
|  |  |  |  |  |  | RecordLifecycleActionHeartbeat |

弹性伸缩 ESS

| LifecycleTransiti on | String | 否 |  |  | SCALE IN _ | 生命周期挂钩适用的伸缩活动类型，取值范围： SCALE OUT：伸缩组弹性扩张活动 。 _ SCALE IN：伸缩组弹性收缩活动。 _ |  |  |
|---|---|---|---|---|---|---|---|---|
| NotificationMeta data | String | 否 |  |  | Test | 伸缩活动的等待状态的固定字符串信息。 参数长度不能超过128个字符。 弹性伸缩每次推送消息到通知对象时，会同时发送您预先指定的 NotificationMetadata参数值，便于管理和标记不同类别的通知信息。当您同时指定了NotificationArn参数时，NotificationMetadata参数方可生效。 |  |  |
| NotificationArn | String | 否 |  |  |  | 生命周期挂钩通知对象标识符，设置本参数时支持以下通知方式： 消息服务MNS队列，参数取值格式： acs:mns:{region-id}: |  |  |
|  |  |  |  |  |  |  | acs:mns:{region-id}: |  |
|  |  |  |  |  |  | {account- |  |  |
|  |  |  |  |  |  | id}:queue/{queuename} |  |  |
|  |  |  |  |  |  |  | acs:mns:{region-id}: |  |
|  |  |  |  |  |  | {account- |  |  |
|  |  |  |  |  | acs:mns:cn- | id}:topic/{topicname} |  |  |
|  |  |  |  |  | beijing-env17- d01:161456884 |  |  |  |
|  |  |  |  |  |  |  | acs:oos:{region-id}: |  |
|  |  |  |  |  | 340****:queue/ | {account- |  |  |
|  |  |  |  |  | modifyLifecycle Ho**** | id}:template/{templatename} |  |  |
| RegionId | String | 否 |  |  | cn-beijing- env17-d01 | 伸缩组所属的地域ID。 |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

弹性伸缩 ESS 请求示例

```
http(s)://ess.example.com/?Action=ModifyLifecycleHook &LifecycleHookId=ash-bp1fxuqyi98w0aib**** &ScalingGroupId=asg-bp18p2yfxow2dloq**** &LifecycleHookName=test_SCALE_IN &DefaultResult=CONTINUE &HeartbeatTimeout=600 &LifecycleTransition=SCALE_IN &NotificationMetadata=Test &NotificationArn=acs:mns:cn-beijing-env17d01:161456884340****:queue/modifyLifecycleHo**** &RegionId=cn-beijing-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParamter | The specified value of parameter is not valid. | 参数值不合法。 |
| 400 | InvalidLifecycleHookId. NotExist | The specified LifecycleHookId not exist. | 指定的LifecycleHookId 不存在。 |
| 400 | InvalidLifecycleHookN ame.NotExist | The specified LifecycleHookName you provided not exist. | 指定的 LifecycleHookName不存在。 |
| 400 | InvalidNotificationArn | The specified parameter NotificationArn is invalid. | 指定的NotificationArn不存在。 |

弹性伸缩 ESS

| 400 | UnsupportedNotificatio nType.CurrentRegion | The NotificationType is not supported in the special region which scalingGroup belongs to. | 当前地域不支持该通知方式。 |
|---|---|---|---|
| 400 | LifecycleHook | The specified queue does not exist. | 指定的MNS队列不存在。 |
| 400 | TopicNotExist | The specified topic does not exist. | 指定的MNS主题不存在。 |

#### RecordLifecycleActionHeartbeat

调用RecordLifecycleActionHeartbeat延长一个生命周期挂钩触发后被挂起的ECS实例的等待时间。

**接口说明**

ECS实例的等待时间不能超过6小时，每次等待状态最多能被延时20次。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RecordLifecycle ActionHeartbeat | 系统规定参数，取值： RecordLifecycleActionHeartbeat。 |
| lifecycleActionTo ken | String | 是 | F324B880-900E- 4968-85DD- 81691113**** | 伸缩活动的等待状态标识符，您可以从生命周期挂钩指定的消息服务队列或主题中获取该值。 |
| lifecycleHookId | String | 是 | ash- bp1fxuqyi98w0a ib**** | 生命周期挂钩的ID。 |
| heartbeatTimeo ut | Integer | 否 | 600 | 生命周期挂钩为伸缩组活动设置的等待时间，等待状态超时后会执行下一步动作。 取值范围：30~21600，单位：秒。 创建了生命周期挂钩后，您可以调用本接口延长ECS实例的等待时间，也可以调用 API CompleteLifecycleAction 接口提前结束伸缩活动的等待状态。 默认值：600。 |
| RegionId | String | 否 | cn-hangzhou- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://ess.example.com/?Action=RecordLifecycleActionHeartbeat &lifecycleHookId=ash-bp1fxuqyi98w0aib**** &lifecycleActionToken=F324B880-900E-4968-85DD-81691113**** &heartbeatTimeout=600 &RegionId=cn-hangzhou-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParamter | The specified value of parameter is not valid. | 指定的参数值不合法。 |
| 400 | LifecycleHookIdAndLif ecycleActionToken.Inv alid | The specified LifecycleActionToken and LifecycleHookId you provided does not match any in process lifecycle action. | 根据指定的 LifecycleActionToken无法匹配 LifecycleHookId。 |
| 400 | LifecycleAction.TimeEx ceeded | The specified parameter heartbeatTime exceed lifecycleAction max suspend time. | 等待时间最长不能超过6 小时。 |

弹性伸缩 ESS

| 400 | LifecycleAction.Record TimesExceeded | The specified lifecycleAction exceed lifecycleAction max record times. | 每次等待状态最多能被延时20次。 |
|---|---|---|---|

#### DescribeLifecycleHooks

**接口说明**

| 定一个生命周期挂钩ID列表（ LifecycleHookId.N ScalingGroupId 和 LifecycleHookName 参数。 定伸缩组ID（ ScalingGroupId ）。 时指定伸缩组ID（ ScalingGroupId ）和生命周期挂 | LifecycleHookId.N |
|---|---|

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLifecycl eHooks | 系统规定参数，取值： DescribeLifecycleHooks。 |
| ScalingGroupId | String | 否 | asg- bp1igpak5ft1fly p**** | 伸缩组的ID。 |
| LifecycleHookNa me | String | 否 | lifecyclehook*** * | 生命周期挂钩的名称。 |
| PageNumber | Integer | 否 | 1 | 实例状态列表的页码。起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 50 | 分页查询时设置的每页行数。最大值： 50。 默认值：50。 |
| RegionId | String | 否 | cn-beijing- env17d01 | 伸缩组所属地域的ID。 |
| LifecycleHookId. N | RepeatL ist | 否 | ash- bp1at9ufhmcf9c my**** | 生命周期挂钩的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| LifecycleHooks | Array of LifecycleHook |  | 生命周期挂钩信息列表。 |
|---|---|---|---|
| LifecycleHook |  |  |  |
| DefaultResult | String | CONTINUE | 等待状态结束后的下一步动作。 |
| HeartbeatTime out | Integer | 60 | 生命周期挂钩为伸缩组活动设置的等待时间，等待状态超时后会执行下一步动作。 |
| LifecycleHookI d | String | ash- bp19d1032y9kij96 **** | 生命周期挂钩ID。 |
| LifecycleHook Name | String | lifecyclehook**** | 生命周期挂钩名称。 |
| LifecycleTransi tion | String | SCALE OUT _ | 生命周期挂钩对应伸缩活动类型。 |
| NotificationArn | String | acs:ess:cn-beijing- env17- d01:16145688434 0****:null/null | 生命周期挂钩通知对象标识符，参数格式如下： 未设置通知：acs:ess:{region-id}: {account-id}:null/null。 消息服务MNS队列：acs:mns:{region-id}: {account-id}:queue/{queuename}。 消息服务MNS主题：acs:mns:{region-id}: {account-id}:topic/{topicname}。 运维编排OOS模板：acs:oos:{region-id}: {account- id}:template/{templatename}。 参数格式中的变量含义如下： region-id：伸缩组所在的地域的ID。 account-id：阿里云账号ID。 queuename：MNS队列的名称。 topicname：MNS主题的名称。 templatename：OOS模板的名称。 |
| NotificationMe tadata | String | Test Lifecycle Hook. | 伸缩活动的等待状态的固定字符串信息。 |
| ScalingGroupI d | String | asg- bp1igpak5ft1flyp** ** | 伸缩组ID。 |
| PageNumber | Integer | 1 | 查询起始页数。 |
| PageSize | Integer | 50 | 查询每页返回行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C**** | 请求ID。 |

弹性伸缩 ESS

| TotalCount | Integer | 1 | 生命周期挂钩总个数。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DescribeLifecycleHooks &ScalingGroupId=asg-bp1igpak5ft1flyp**** &LifecycleHookName=lifecyclehook**** &PageNumber=1 &PageSize=50 &LifecycleHookId=["ash-bp1at9ufhmcf9cmy****"] &RegionId=cn-beijing-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <TotalCount>1</TotalCount>
    <PageSize>50</PageSize>
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C****</RequestId>
    <PageNumber>1</PageNumber>
    <LifecycleHooks>
        <LifecycleHookName>lifecyclehook****</LifecycleHookName>
        <NotificationArn>acs:ess:cn-beijing-env17-
d01:161456884340****:null/null</NotificationArn>
        <ScalingGroupId>asg-bp1igpak5ft1flyp****</ScalingGroupId>
        <LifecycleTransition>SCALE_OUT</LifecycleTransition>
        <HeartbeatTimeout>60</HeartbeatTimeout>
        <NotificationMetadata>Test Lifecycle Hook.</NotificationMetadata>
        <DefaultResult>CONTINUE</DefaultResult>
        <LifecycleHookId>ash-bp19d1032y9kij96****</LifecycleHookId>
    </LifecycleHooks>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "TotalCount": 1,
    "PageSize": 50,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C****",
    "PageNumber": 1,
    "LifecycleHooks": {
        "LifecycleHookName": "lifecyclehook****",
        "NotificationArn": "acs:ess:cn-beijing-env17-d01:161456884340****:null/null",
        "ScalingGroupId": "asg-bp1igpak5ft1flyp****",
        "LifecycleTransition": "SCALE_OUT",
        "HeartbeatTimeout": 60,
        "NotificationMetadata": "Test Lifecycle Hook.",
        "DefaultResult": "CONTINUE",
        "LifecycleHookId": "ash-bp19d1032y9kij96****"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParamter | The specified value of parameter is not valid. | 指定的参数值不合法。 |

#### DescribeLifecycleActions

调用DescribeLifecycleActions查看伸缩活动对应的生命周期操作。

**接口说明**

如果发生了和生命周期挂钩适用类型一致的伸缩活动，每个生命周期挂钩都会触发一次生命周期操作，生命周期操作有三种状态： Pending：挂起中。表示ECS实例仍处于挂起中状态。 Timeout：已超时。表示已超过生命周期挂钩的超时时间，自动结束了ECS实例的挂起中状态。 Completed：已处理。表示您手动提前结束了ECS实例的挂起中状态。 如果在创建生命周期挂钩时没有设置后续动作，例如在结束挂起后触发执行指定的OOS模板。您可以调用本接口获取当前伸缩活动对应生命周期操作的标识符，以便自行定制后续动作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLifecycl eActions | 系统规定参数。取值： DescribeLifecycleActions。 |
| ScalingActivityId | String | 是 | asa- bp17mug9t0peg agw**** | 伸缩活动的ID。 |

弹性伸缩 ESS

| LifecycleActionS tatus | String | 否 | Pending | 生命周期操作的状态。取值范围： Pending：挂起中。表示ECS实例仍处于挂起中状态。 Timeout：已超时。表示已到达生命周期挂钩的超时时间，自动结束ECS实例的挂起中状态。 Completed：已处理。表示您手动提前结束了ECS实例的挂起中状态。 |
|---|---|---|---|---|
| NextToken | String | 否 | AAAAAcSz4VTb1 Nq**** | 查询凭证，用于指定开始查询的位置。 例如上次查询10条生命周期操作后，本次从第11条生命周期操作开始查询。取值为上次调用本接口返回的NextToken参数值，如果不填写取值则表示从头开始查询。 |
| RegionId | String | 否 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |
| MaxResults | Integer | 否 | 10 | 设置单页查询的最大条目数。取值范围： 1~50。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LifecycleAction s | Array of LifecycleAction |  | 各个生命周期挂钩对应的生命周期操作列表。 |
| LifecycleAction |  |  |  |
| InstanceIds | List | ["i- bp11m3fzlqrgk5vh ****","i- bp11m3fzlqrgk5vh ****"] | 该生命周期挂钩挂起的ECS实例的ID列表。 |
| LifecycleAction Result | String | CONTINUE | 该生命周期挂钩触发的生命周期操作结束后的下一步动作。取值范围： CONTINUE：继续响应弹性扩张活动，将ECS 实例添加至伸缩组；继续响应弹性收缩活动， 将ECS实例从伸缩组移除。 ABANDON：终止弹性扩张活动，直接释放创建出来的ECS实例；继续响应弹性收缩活动， 将ECS实例从伸缩组移除。 |
| LifecycleAction Status | String | Pending | 生命周期操作的状态。 |
| LifecycleAction Token | String | 9C2E9DA7-F794- 449A-ACF6- CEE24444F7BB | 生命周期操作的标识符。 |

弹性伸缩 ESS

| LifecycleHookI d | String | ash- bp18uoft0deax0f7* *** | 生命周期挂钩的ID。 |
|---|---|---|---|
| MaxResults | Integer | 3 | 单页查询的最大条目数。 |
| NextToken | String | AAAAAcSz4VTb1Nq **** | 本次调用返回的查询凭证。 |
| RequestId | String | 42A742EB-FCF3- 459E-9C62- E107048C**** | 请求ID。 |
| TotalCount | Integer | 3 | 本次查询到的生命周期操作的总数。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DescribeLifecycleActions &ScalingActivityId=asa-bp17mug9t0pegagw**** &LifecycleActionStatus=Pending &NextToken=AAAAAcSz4VTb1Nq**** &MaxResults=10 &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <TotalCount>3</TotalCount>
    <RequestId>42A742EB-FCF3-459E-9C62-E107048C****</RequestId>
    <NextToken>AAAAAcSz4VTb1Nq****</NextToken>
    <MaxResults>3</MaxResults>
    <LifecycleActions>
        <LifecycleActionStatus>Pending</LifecycleActionStatus>
        <LifecycleActionResult>CONTINUE</LifecycleActionResult>
        <LifecycleActionToken>9C2E9DA7-F794-449A-ACF6-
CEE24444F7BB</LifecycleActionToken>
        <LifecycleHookId>ash-bp18uoft0deax0f7****</LifecycleHookId>
        <InstanceIds>["i-bp11m3fzlqrgk5vh****","i-bp11m3fzlqrgk5vh****"]</InstanceIds>
    </LifecycleActions>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "TotalCount": 3,
    "RequestId": "42A742EB-FCF3-459E-9C62-E107048C****",
    "NextToken": "AAAAAcSz4VTb1Nq****",
    "MaxResults": 3,
    "LifecycleActions": {
        "LifecycleActionStatus": "Pending",
        "LifecycleActionResult": "CONTINUE",
        "LifecycleActionToken": "9C2E9DA7-F794-449A-ACF6-CEE24444F7BB",
        "LifecycleHookId": "ash-bp18uoft0deax0f7****",
        "InstanceIds": "[\"i-bp11m3fzlqrgk5vh****\",\"i-bp11m3fzlqrgk5vh****\"]"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The specified value of parameter "ScalingActivityId" is not valid. | 指定的参数 （ScalingActivityId）无效。 |
| 400 | InvalidParameter | The specified value of parameter "MaxResults" is not valid. | 指定的参数 （MaxResults）无效。 |
| 400 | InvalidParameter | The specified value of parameter "LifecycleActionStatus " is not valid. | 指定的参数 （LifecycleActionStatu s）无效。 |

#### CompleteLifecycleAction

**接口说明**

设置结束伸缩活动的等待状态后，系统支持继续完成伸缩活动（CONTINUE）或者终止此次伸缩活动 （ABANDON）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CompleteLifecyc leAction | 系统规定参数，取值： CompleteLifecycleAction。 |

弹性伸缩 ESS

| LifecycleActionT oken | String | 是 | aaaa-bbbbb- cccc-ddddd | 伸缩活动的等待状态标识符，您可以从生命周期挂钩指定的消息服务队列或主题中获取该值。 |
|---|---|---|---|---|
| LifecycleHookId | String | 是 | ash- bp14g3ee6bt3sc 98**** | 生命周期挂钩的ID。 |
| LifecycleActionR esult | String | 否 | CONTINUE | 生命周期挂钩等待状态结束后的下一步动作。取值范围： CONTINUE：继续响应弹性扩张活动， 将ECS实例添加至伸缩组；继续响应弹性收缩活动，将ECS实例从伸缩组移除。 ABANDON：终止弹性扩张活动，直接释放创建出来的ECS实例；继续响应弹性收缩活动，将ECS实例从伸缩组移除。 默认值：CONTINUE。 伸缩组中存在多个生命周期挂钩时同步触发，最终的下一步动作如下： 对弹性收缩活动，在ABANDON类型生命周期挂钩触发的等待状态结束时，会将提前结束后续生命周期挂钩的等待状态，将ECS实例从伸缩组移除。 在挂起弹性收缩活动的生命周期挂钩类型为CONTINUE时，或者对弹性扩张活动，后续生命周期挂钩会继续挂起伸缩活动，直到最后一个生命周期挂钩触发的等待状态结束。最终的下一步动作以最后一个结束等待状态的生命周期挂钩类型为准。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多详情，请参见弹性伸缩中的如何保证幂等性章节。 |
| RegionId | String | 否 | cn-qingdao- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例弹性伸缩 ESS

```
http(s)://ess.example.com/?Action=CompleteLifecycleAction &LifecycleHookId=ash-bp14g3ee6bt3sc98**** &LifecycleActionToken=aaaa-bbbbb-cccc-ddddd &LifecycleActionResult=CONTINUE &ClientToken=123e4567-e89b-12d3-a456-42665544**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParamter | The specified value of parameter is invalid. | 指定的参数值不合法。 |
| 400 | LifecycleHookIdAndLif ecycleActionToken.Inv alid | The specified LifecycleActionToken and LifecycleHookId you provided does not match any in process lifecycle action. | 根据指定的 LifecycleActionToken无法匹配 LifecycleHookId。 |

#### DeleteLifecycleHook

**接口说明**

如果生命周期挂钩已触发伸缩活动等待状态，删除生命周期挂钩时，对应的等待状态会被提前结束。您可以

| 定生命周期挂钩ID（ |  | LifecycleHookId |  | ）， |
|---|---|---|---|---|
| ScalingGroupId |  |  |  |  |
|  |  | 和 |  |  |
| 时指定伸缩组ID（ | ScalingGroupId |  | ）与生命 |  |

**请求参数**

弹性伸缩 ESS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteLifecycleH ook | 系统规定参数，取值： DeleteLifecycleHook。 |
| LifecycleHookId | String | 否 | ash- bp14g3ee6bt3sc 98**** | 生命周期挂钩的ID。 |
| ScalingGroupId | String | 否 | asg- bp18p2yfxow2dl oq**** | 伸缩组的ID。 |
| LifecycleHookNa me | String | 否 | lifecyclehook*** * | 生命周期挂钩的名称。 |
| RegionId | String | 否 | cn-hangzhou- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DeleteLifecycleHook &LifecycleHookId=ash-bp14g3ee6bt3sc98**** &ScalingGroupId=asg-bp18p2yfxow2dloq**** &LifecycleHookName=lifecyclehook**** &RegionId=cn-hangzhou-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

弹性伸缩 ESS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParamter | The specified value of parameter is invalid. | 参数值不合法。 |
| 400 | InvalidLifecycleHookId. NotExist | The specified LifecycleHookId does not exist. | 生命周期挂钩ID不存在。 |
| 400 | InvalidLifecycleHookN ame.NotExist | The specified LifecycleHookName you provided does not exist. | 生命周期挂钩名称不存在。 |

### 事件通知

#### CreateNotificationConfiguration

调用CreateNotificationConfiguration创建弹性伸缩事件及资源变化通知。

**接口说明**

您可以设置由云监控系统事件、消息服务MNS队列或MNS主题接收消息通知。当伸缩组发生指定类型的伸缩事件或者资源变化时，弹性伸缩会发送消息通知云监控或消息服务MNS。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateNotificatio nConfiguration | 系统规定参数。取值： CreateNotificationConfiguration。 |

弹性伸缩 ESS

| NotificationArn | String | 是 |  |  |  |  | 通知对象标识符，设置本参数时支持以下通知方式： 云监控，参数取值格式： acs:ess: |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | acs:ess: |  |
|  |  |  |  |  |  |  | {region-id}:{account- |  |  |  |
|  |  |  |  |  |  |  | id}:cloudmonitor |  |  |  |
|  |  |  |  |  |  |  |  | acs:mns:{region-id}: |  |  |
|  |  |  |  |  | acs:mns:cn- |  | {account- |  |  |  |
|  |  |  |  |  | beijing-env17- |  |  |  |  |  |
|  |  |  |  |  | d01:161456884 |  | id}:queue/{queuename} |  |  |  |
|  |  |  |  |  | 340****:queue/ modifyLifecycle |  |  |  |  |  |
|  |  |  |  |  |  |  |  | acs:mns:{region-id}: |  |  |
|  |  |  |  |  | Ho**** |  | {account- |  |  |  |
|  |  |  |  |  |  |  | id}:topic/{topicname} |  |  |  |
| NotificationType. N | RepeatL ist | 是 |  |  | AUTOSCALING:S CALE OUT SUCC _ _ ESS |  | 一类或者多类弹性伸缩事件及资源变化通知。N的取值范围：1~8，多个取值使用重复列表的形式。 您可以调用API DescribeNotificationTypes 接口查询参数取值。 |  |  |  |
| ScalingGroupId | String | 是 |  |  | AG6CQdPU8OKd wLjgZcJ**** |  | 伸缩组的ID。 |  |  |  |
| RegionId | String | 否 |  |  | cn-beijing- env17-d01 |  | 伸缩组所属的地域ID。 |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=CreateNotificationConfiguration &NotificationArn=acs:mns:cn-beijing-env17d01:161456884340****:queue/modifyLifecycleHo**** &NotificationType.1=AUTOSCALING:SCALE_OUT_SUCCESS &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ****
```

`&<`公共请求参数> 弹性伸缩 ESS 正常返回示例 `XML` 格式

```xml
<CreateNotificationConfigurationResponse>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
</CreateNotificationConfigurationResponse>
```

`JSON` 格式

```json
{
    "requestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidNotificationArn | The specified parameter notificationArn is invalid. | 指定的NotificationArn不合法。 |
| 400 | InvalidNotificationType s | The specified notificationType is invalid. | 指定的 NotificationType.N不合法。 |
| 400 | NotificationConfigurati onExist | The specified notificationConfigurati on already exist for the scalingGroup. | 指定的事件通知已经存在于当前伸缩组中。 |
| 400 | NotificationConfigurati onQuotaExceed.ForSc alingGroup | NotificationConfigurati on num exceed for the specified scalingGroup. | 当前伸缩组配置的通知功能超出允许的上限值。 |
| 400 | QueueNotExist | The specified queue queuename does not exist. | 指定的MNS队列不存在。 |
| 400 | TopicNotExist | The specified topic topicname does not exist. | 指定的MNS主题不存在。 |
| 400 | UnsupportedNotificatio nType.CurrentRegion | The notificationType is not supported in the special region which scalingGroup belongs to. | 当前地域不支持该通知方式。 |

弹性伸缩 ESS

| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组不存在。 |
|---|---|---|---|

#### ModifyNotificationConfiguration

调用ModifyNotificationConfiguration修改一条弹性伸缩事件及资源变化通知的信息。

**请求参数**

| 名称 | 类型 | 是否必选 |  |  | 示例值 |  | 描述 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| Action | String | 是 |  |  | ModifyNotificatio nConfiguration |  | 系统规定参数。取值： ModifyNotificationConfiguration。 |  |  |  |
| NotificationArn | String | 是 |  |  |  |  | 通知对象标识符，设置本参数时支持以下通知方式： 云监控，参数取值格式： acs:ess: |  |  |  |
|  |  |  |  |  |  |  |  |  | acs:ess: |  |
|  |  |  |  |  |  |  | {region-id}:{account- |  |  |  |
|  |  |  |  |  |  |  | id}:cloudmonitor |  |  |  |
|  |  |  |  |  |  |  |  | acs:mns:{region-id}: |  |  |
|  |  |  |  |  |  |  | {account- |  |  |  |
|  |  |  |  |  | acs:ess:cn- |  |  |  |  |  |
|  |  |  |  |  | beijing-env17- |  | id}:queue/{queuename} |  |  |  |
|  |  |  |  |  | d01:161456884 340****:cloudm |  |  |  |  |  |
|  |  |  |  |  |  |  |  | acs:mns:{region-id}: |  |  |
|  |  |  |  |  | onitor |  | {account- |  |  |  |
|  |  |  |  |  |  |  | id}:topic/{topicname} |  |  |  |
| NotificationType. N | RepeatL ist | 是 |  |  | AUTOSCALING:S CALE OUT SUCC _ _ ESS |  | 一类或者多类弹性伸缩事件及资源变化通知。N的取值范围：1~8，多个取值使用重复列表的形式。 您可以调用API DescribeNotificationTypes 接口查询参数取值。 |  |  |  |
| ScalingGroupId | String | 是 |  |  | AG6CQdPU8OKd wLjgZcJ**** |  | 伸缩组的ID。 |  |  |  |
| RegionId | String | 否 |  |  | cn-beijing- env17-d01 |  | 伸缩组所属的地域ID。 |  |  |  |

**返回数据**

弹性伸缩 ESS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=ModifyNotificationConfiguration &NotificationArn=acs:ess:cn-beijing-env17-d01:161456884340****:cloudmonitor &NotificationType.1=AUTOSCALING:SCALE_OUT_SUCCESS &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyNotificationConfigurationResponse>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
</ModifyNotificationConfigurationResponse>
```

`JSON` 格式

```json
{
        "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidNotificationType s | The specified notification type is invalid. | 指定的 NotificationType.N不合法。 |
| 400 | NotificationConfigurati onNotExist | The specified notification configuration not exist for the scaling group. | 当前伸缩组不存在指定的弹性伸缩事件及资源变化通知类型。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组不存在。 |

#### DescribeNotificationConfigurations

调用DescribeNotificationConfigurations查询您创建的弹性伸缩事件及资源变化通知。

**请求参数**

弹性伸缩 ESS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeNotifica tionConfiguratio ns | 系统规定参数。取值： DescribeNotificationConfigurations。 |
| ScalingGroupId | String | 是 | AG6CQdPU8OKd wLjgZcJ**** | 伸缩组的ID。 |
| RegionId | String | 否 | cn-beijing | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 |  | 示例值 |  |  | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| NotificationCo nfigurationMo dels | Array of NotificationCo nfigurationMo del |  |  |  |  | 弹性伸缩事件及资源变化通知的集合。 |  |  |  |  |
| NotificationCo nfigurationMo del |  |  |  |  |  |  |  |  |  |  |
| NotificationArn | String |  |  |  |  | 通知对象标识符，参数格式如下： 云监控： acs:ess:{region-id}: {account-id}:cloudmonitor 。 |  |  |  |  |
|  |  |  |  |  |  |  | acs:ess:{region-id}: |  |  |  |
|  |  |  |  |  |  | {account-id}:cloudmonitor |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 。 |
|  |  |  |  |  |  | 消息服务MNS队列： |  | acs:mns:{region- |  |  |
|  |  |  |  |  |  | id}:{account- |  |  |  |  |
|  |  |  | acs:mns:cn- |  |  |  |  |  |  |  |
|  |  |  |  |  |  | id}:queue/{queuename} |  |  | 。 |  |
|  |  |  | beijing:161456884 340****:topic/modi |  |  | 消息服务MNS主题： |  | acs:mns:{region- |  |  |
|  |  |  |  |  | ***:topic/modi | id}:{account- |  |  |  |  |
|  |  |  | fyLifecycleHo**** |  | ecycleHo**** |  |  |  |  |  |
|  |  |  |  |  |  | id}:topic/{topicname} |  |  |  |  |
| NotificationTy pes | List |  | AUTOSCALING:SCA LE IN SUCCESS _ _ |  |  | 弹性伸缩事件及资源变化通知类型列表。 |  |  |  |  |
| ScalingGroupI d | String |  | asg- bp1igpak5ft1flyp** ** |  |  | 伸缩组的ID。 |  |  |  |  |
| RequestId | String |  | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** |  |  | 请求ID。 |  |  |  |  |

**示例**

请求示例弹性伸缩 ESS

```
http(s)://ess.aliyuncs.com/?Action=DescribeNotificationConfigurations &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeNotificationConfigurationsResponse>
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
    <NotificationConfigurationModels>
        <NotificationArn>acs:mns:cn-
beijing:161456884340****:topic/modifyLifecycleHo****</NotificationArn>
        <ScalingGroupId>asg-bp1igpak5ft1flyp****</ScalingGroupId>
        <NotificationTypes>AUTOSCALING:SCALE_IN_SUCCESS</NotificationTypes>
    </NotificationConfigurationModels>
<DescribeNotificationConfigurationsResponse>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "NotificationConfigurationModels": {
        "NotificationArn": "acs:mns:cn-
beijing:161456884340****:topic/modifyLifecycleHo****",
        "ScalingGroupId": "asg-bp1igpak5ft1flyp****",
        "NotificationTypes": "AUTOSCALING:SCALE_IN_SUCCESS"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组不存在。 |

#### DescribeNotificationTypes

调用DescribeNotificationTypes查询弹性伸缩事件及资源变化通知的类型。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeNotifica tionTypes | 系统规定参数。取值： DescribeNotificationTypes。 |

**返回数据**

弹性伸缩 ESS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NotificationTy pes | List | AUTOSCALING:SCA LE OUT SUCCESS _ _ | 弹性伸缩事件及资源变化通知类型的列表。 AUTOSCALING:SCALE OUT SUCCESS： _ _ 扩容伸缩活动成功。 AUTOSCALING:SCALE IN SUCCESS：缩 _ _ 容伸缩活动成功。 AUTOSCALING:SCALE OUT ERROR：扩 _ _ 容伸缩活动失败。 AUTOSCALING:SCALE IN ERROR：缩容伸 _ _ 缩活动失败。 AUTOSCALING:SCALE REJECT：伸缩活动 _ 拒绝执行。 AUTOSCALING:SCALE OUT START：扩容 _ _ 伸缩活动开始。 AUTOSCALING:SCALE IN START：缩容伸 _ _ 缩活动开始。 AUTOSCALING:SCHEDULE TASK EXPIRI _ _ NG：任务到期提醒。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.aliyuncs.com/?Action=DescribeNotificationTypes
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>66046F31-AF8C-44B4-9992-453F33CF****</RequestId>
    <NotificationTypes>
        <NotificationType>AUTOSCALING:SCALE_OUT_SUCCESS</NotificationType>
        <NotificationType>AUTOSCALING:SCALE_IN_SUCCESS</NotificationType>
        <NotificationType>AUTOSCALING:SCALE_OUT_ERROR</NotificationType>
        <NotificationType>AUTOSCALING:SCALE_IN_ERROR</NotificationType>
        <NotificationType>AUTOSCALING:SCALE_REJECT</NotificationType>
        <NotificationType>AUTOSCALING:SCALE_OUT_START</NotificationType>
        <NotificationType>AUTOSCALING:SCALE_IN_START</NotificationType>
        <NotificationType>AUTOSCALING:SCHEDULE_TASK_EXPIRING</NotificationType>
    </NotificationTypes>
```

`JSON` 格式弹性伸缩 ESS

```json
{
 "RequestId": "66046F31-AF8C-44B4-9992-453F33CF****",
 "NotificationTypes": {
  "NotificationType": [
   "AUTOSCALING:SCALE_OUT_SUCCESS",
   "AUTOSCALING:SCALE_IN_SUCCESS",
   "AUTOSCALING:SCALE_OUT_ERROR",
   "AUTOSCALING:SCALE_IN_ERROR",
   "AUTOSCALING:SCALE_REJECT",
   "AUTOSCALING:SCALE_OUT_START",
   "AUTOSCALING:SCALE_IN_START",
   "AUTOSCALING:SCHEDULE_TASK_EXPIRING"
```

]

```
 }
}
```

#### DeleteNotificationConfiguration

调用DeleteNotificationConfiguration删除一条弹性伸缩事件及资源变化通知。

**请求参数**

| 名称 | 类型 | 是否必选 |  |  | 示例值 |  | 描述 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| Action | String | 是 |  |  | DeleteNotificatio nConfiguration |  | 系统规定参数。取值： DeleteNotificationConfiguration。 |  |  |  |
| NotificationArn | String | 是 |  |  |  |  | 通知对象标识符，各通知方式的参数格式如下： 云监控，参数取值格式： acs:ess: |  |  |  |
|  |  |  |  |  |  |  |  |  | acs:ess: |  |
|  |  |  |  |  |  |  | {region-id}:{account- |  |  |  |
|  |  |  |  |  |  |  | id}:cloudmonitor |  |  |  |
|  |  |  |  |  |  |  |  | acs:mns:{region-id}: |  |  |
|  |  |  |  |  |  |  | {account- |  |  |  |
|  |  |  |  |  | acs:ess:cn- |  | id}:queue/{queuename} |  |  |  |
|  |  |  |  |  | beijing-env17- d01:161456884 340****:cloudm |  |  |  |  |  |
|  |  |  |  |  |  |  |  | acs:mns:{region-id}: |  |  |
|  |  |  |  |  | onitor |  | {account- |  |  |  |
|  |  |  |  |  |  |  | id}:topic/{topicname} |  |  |  |

弹性伸缩 ESS

| ScalingGroupId | String | 是 | asg- bp18p2yfxow2dl oq**** | 伸缩组的ID。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-beijing- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DeleteNotificationConfiguration &ScalingGroupId=asg-bp18p2yfxow2dloq**** &NotificationArn=acs:ess:cn-beijing-env17-d01:161456884340****:cloudmonitor &RegionId=cn-beijing-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteNotificationConfigurationResponse>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
</DeleteNotificationConfigurationResponse>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NotificationConfigurati onNotExist | The specified NotificationConfigurati on not exist for the scalingGroup. | 当前伸缩组不存在指定的伸缩事件及资源变化通知。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组不存在。 |

弹性伸缩 ESS

### 实例

#### EnterStandby

**接口说明**

如果伸缩组关联了负载均衡实例，会把负载均衡中对应的ECS实例权重设置为0。 当ECS实例处于备用状态时，如果您手动移出伸缩组并释放实例，可以正常移出伸缩组并释放。 对于伸缩组数量变化或监控任务触发的自动缩容的伸缩活动，不会移出处于备用状态的ECS实例。 当ECS实例处于备用状态时，ECS实例如果处于非健康状态（例如停止中、重启中等），ECS实例的健康检查状态不会被更新，并且不会触发移出不健康实例的伸缩活动，只有ECS实例退出备用状态后才会重新更新健康检查状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | EnterStandby | 系统规定参数，取值：EnterStandby。 |
| InstanceId.N | RepeatL ist | 是 | i-28wt4**** | ECS实例的ID。 |
| ScalingGroupId | String | 是 | asg- bp1fo0dbtsbmq a9h**** | 伸缩组的ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见如何弹性伸缩中的如何保证幂等性章节。 |
| Async | Boolean | 否 | false | 是否采用异步任务方式执行。取值范围： true：异步任务执行。 false：同步执行。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingActivity Id | String | asa- 2zeb04oym05qace q**** | 调用伸缩活动ID。 |

**示例**

弹性伸缩 ESS 请求示例

```
&ScalingGroupId=asg-bp1fo0dbtsbmqa9h**** &ClientToken=123e4567-e89b-12d3-a456-42665544**** &InstanceId=["i-28wt4****"] &Async=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScalingActivityId>asa-2zeb04oym05qaceq****</ScalingActivityId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingActivityId": "asa-2zeb04oym05qaceq****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | RAM用户无权限调用该接口，请联系主账号授权后重试。 |
| 404 | InvalidInstanceId.NotF ound | Instance "XXX" does not exist. | 指定的ECS实例不存在。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组不存在。 |

#### ExitStandby

**接口说明**

如果伸缩组设置了负载均衡服务，会将ECS实例权重设置为伸缩配置中定义的权重值。

**请求参数**

弹性伸缩 ESS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ExitStandby | 系统规定参数，取值：ExitStandby。 |
| InstanceId.N | RepeatL ist | 是 | i-28wt4**** | ECS实例的ID。取值可以由多个实例ID组成一个JSON数组，最多支持20个ID，ID 之间用半角逗号（,）隔开。 |
| ScalingGroupId | String | 是 | asg- bp1fo0dbtsbmq a9h**** | 伸缩组的ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 只支持ASCII字符，且不能超过64个字符。更多信息，请参见弹性伸缩中的如何保证幂等性章节。 |
| Async | Boolean | 否 | false | 是否采用异步任务方式执行。取值范围： true：异步任务执行。 false：同步执行。 默认值： false。 |
| RegionId | String | 否 | cn-hangzhou- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingActivity Id | String | asa- 2zeb04oym05qace q**** | 调用伸缩活动ID。 |

**示例**

请求示例

```
&ScalingGroupId=asg-bp1fo0dbtsbmqa9h**** &ClientToken=123e4567-e89b-12d3-a456-42665544**** &InstanceId=["i-28wt4****"] &Async=false &RegionId=cn-hangzhou-env17-d01
```

`&<`公共请求参数> 正常返回示例弹性伸缩 ESS `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScalingActivityId>asa-2zeb04oym05qaceq****</ScalingActivityId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingActivityId": "asa-2zeb04oym05qaceq****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | RAM用户无权限调用该接口，请联系主账号授权后重试。 |
| 404 | InvalidInstanceId.NotF ound | A required authorization for the specified action is not supplied. | 指定的ECS实例不存在。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在该用户账号下不存在。 |

#### SetInstancesProtection

调用SetInstancesProtection保护或者停止保护伸缩组内的一台或者多台ECS实例。

**接口说明**

ECS实例开启保护状态后： 实例保持此状态，直至您停止保护状态。 即使伸缩组内实例数量的变化和监控任务触发自动缩容的伸缩活动，也不会移除处于保护状态的ECS实例。您需要自行ECS实例后才能释放ECS实例。具体的移出操作，请参见API `RemoveInstances` 。 ECS实例被停止或者重启时，不会更新ECS实例的健康检查状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

弹性伸缩 ESS

| Action | String | 是 | SetInstancesProt ection | 系统规定参数，取值： SetInstancesProtection。 |
|---|---|---|---|---|
| InstanceId.N | RepeatL ist | 是 | i-28wt4**** | ECS实例的ID，N的取值范围为：1~20。 |
| ProtectedFromS caleIn | Boolean | 是 | true | 伸缩组自动缩容时是否保护ECS实例，使其不被终止或移出伸缩组，取值范围： true：保护ECS实例。 false ：不保护ECS实例。 |
| ScalingGroupId | String | 是 | asg- bp18p2yfxow2dl oq**** | 伸缩组的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=SetInstancesProtection &InstanceId.1=i-28wt4**** &ProtectedFromScaleIn=true &ScalingGroupId=asg-bp18p2yfxow2dloq****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| 400 | IncorrectScalingGroup Status | The current status of the specified scaling group does not support this action. | 您需要启用伸缩组。 |
|---|---|---|---|
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您还未被授权使用 SetInstancesProtection 接口。 |
| 404 | InvalidInstanceId.NotF ound | Instance “XXX” does not exist. | 指定的ECS实例不存在。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组不存在。 |

#### SetInstanceHealth

**接口说明**

伸缩组会检测并移出处于不健康状态的ECS实例，如果您需要保留指定的ECS实例，请将ECS实例转入备用或者保护状态，更多说明，请参见 `EnterStandby` 和 `SetInstancesProtection` 。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetInstanceHeal th | 系统规定参数。取值： SetInstanceHealth。 |
| HealthStatus | String | 是 | Healthy | 设置ECS实例的健康状态，取值范围： Healthy：设置为健康状态。 Unhealthy：设置为不健康状态。 |
| InstanceId | String | 是 | i- bp1ap6bro51a7f sa**** | 伸缩组内ECS实例的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B755AE57-6093- 43E4-938E- DEA422A9**** | 请求ID。 |

**示例**

请求示例弹性伸缩 ESS

```
http(s)://ess.example.com/?Action=SetInstanceHealth &HealthStatus=Healthy &InstanceId=i-bp1ap6bro51a7fsa****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <RequestId>B755AE57-6093-43E4-938E-DEA422A9****</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "B755AE57-6093-43E4-938E-DEA422A9****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInstanceId.NotF ound | Instance "%s" does not exist. | 伸缩组内不存在指定的实例。 |
| 400 | InvalidParameter | The specified value of parameter "%s" is not valid. | 指定的参数非法。 |

#### RebalanceInstances

调用RebalanceInstances重新平衡多可用区伸缩组内ECS实例的分布。

**接口说明**

分布再平衡会通过新建ECS实例替换已有ECS实例补偿平衡可用区，终止已有ECS实例前会先启动新ECS实例，分布再平衡不会影响您的应用程序性能或可用性。 只支持设置了MultiAZPolicy为BALANCE的多可用区伸缩组，用于平衡多可用区间ECS实例的分布。 只有伸缩组内实例分布严重不平衡时可以执行再平衡操作。 一次分布再平衡活动最多替换20台ECS实例。 分布再平衡活动期间，如果组内实例数量接近或达到指定的最大ECS实例台数（MaxSize），但需要继续分布再平衡，弹性伸缩允许暂时超出MaxSize的10%，最低允许超出1台ECS实例。该超出状态持续重新平衡该伸缩组所需的时间，通常为1分钟至6分钟。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

弹性伸缩 ESS

| Action | String | 是 | RebalanceInstan ces | 系统规定参数，取值： RebalanceInstances。 |
|---|---|---|---|---|
| ScalingGroupId | String | 是 | asg- bp18p2yfxow2dl oq**** | 伸缩组的ID。 |
| RegionId | String | 否 | cn-hangzhou- env17-d01 | 伸缩组所属的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| ScalingActivity Id | String | asa- kjgffgdfadah**** | 伸缩活动的ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=RebalanceInstances &ScalingGroupId=asg-bp18p2yfxow2dloq**** &RegionId=cn-hangzhou-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <ScalingActivityId>asa-kjgffgdfadah****</ScalingActivityId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "ScalingActivityId": "asa-kjgffgdfadah****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| 400 | IncorrectScalingGroup Status | The current status of the specified scaling group does not support this action. | 您需要启用伸缩组。 |
|---|---|---|---|
| 400 | OperationDenied | This operation is denied because the specified scaling group does not support this action. | 指定伸缩组的扩缩容策略 MultiAZPolicy不是 BALANCE，或者ECS实例分布不存在严重不平衡的情况。 |
| 403 | Forbidden.Unauthorize d | A required authorization for the specified action is not supplied. | 您还未被授权使用 RebalanceInstances接口。 |
| 404 | InvalidScalingGroupId. NotFound | The specified scaling group does not exist. | 指定的伸缩组在该用户账号下不存在。 |

### 地域

#### DescribeRegions

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRegions | 系统规定参数，取值： DescribeRegions。 |
| AcceptLanguage | String | 否 | zh-CN | 根据所选语言筛选返回结果。取值范围： zh-CN：根据汉语筛选。 en-US：根据英语筛选。 ja：根据日语筛选。 默认值：zh-CN。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Regions | Array of Region |  | 地域信息的集合。 |
| Region |  |  |  |

弹性伸缩 ESS

| ClassicUnavail able | Boolean | false | 当前地域是否支持经典网络类型伸缩组。可能值： true：不支持。 false：支持。 |
|---|---|---|---|
| LocalName | String | 华北2 | 地域名称。 |
| RegionEndpoin t | String | ess.example.com | 地域对应的接入地址（Endpoint）。 |
| RegionId | String | cn-beijing-env17- d01 | 地域ID。 |
| VpcUnavailabl e | Boolean | false | 当前地域是否支持VPC网络类型伸缩组。可能值： true：不支持。 false：支持。 |
| RequestId | String | 73469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=DescribeRegions &AcceptLanguage=zh-CN
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>73469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
      <Regions>
            <VpcUnavailable>false</VpcUnavailable>
            <ClassicUnavailable>false</ClassicUnavailable>
            <RegionId>cn-beijing-env17-d01</RegionId>
            <RegionEndpoint>ess.example.com</RegionEndpoint>
            <LocalName>华北2</LocalName>
      </Regions>
```

`JSON` 格式弹性伸缩 ESS

```json
{
    "RequestId": "73469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "Regions": {
        "VpcUnavailable": false,
        "ClassicUnavailable": false,
        "RegionId": "cn-beijing-env17-d01",
        "RegionEndpoint": "ess.example.com",
        "LocalName": "华北2"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidAcceptLanguag e.NotFound | Only Chinese (zh-CN), English (en-US), and Japanese (ja) are allowed. | 不支持指定的语言。 |

### 标签

#### TagResources

**接口说明**

伸缩组最多支持绑定20个标签。 绑定标签前，阿里云会校验资源已有标签数量。超过限制值时返回报错信息。 如果 `Propagate` 参数设置为 `true` 时，伸缩组设置的标签只会同步传播到伸缩组中即将扩容的实例上，而不会传播到已经在伸缩组中运行的实例上。 如果伸缩配置设置了标签，且将伸缩组设置的标签进行传播，则即将扩容的实例标签预期如下： 包含伸缩配置与伸缩组设置传播的所有标签。 如果伸缩配置设置的标签与伸缩组传播的标签具有相同的标签键，则伸缩组传播的标签会被伸缩配置设置的标签覆盖。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TagResources | 系统规定参数。取值：TagResources。 |
| RegionId | String | 是 | cn-hangzhou- env17-d01 | 资源所属的地域ID。您可以调用API DescribeRegions 查看最新的阿里云地域列表。 |

弹性伸缩 ESS

| ResourceId.N | RepeatL ist | 是 | asg- bp17xb4x1vr29l gt**** | 资源ID，N的取值范围为1~50。 |
|---|---|---|---|---|
| ResourceType | String | 是 | scalinggroup | 资源类型定义，目前只支持伸缩组。取值为scalinggroup。 |
| Tag.N.Key | String | 否 | TestKey | 资源的标签键。N的取值范围：1~20。 一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Tag.N.Value | String | 否 | TestValue | 资源的标签值。N的取值范围：1~20。 传入该值时，可以为空字符串。最多支持 128个字符，不能以 acs: 开头，不能包含 http:// 或者 https:// 。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 74C4E313-8570- 479F-8791- DC25360D**** | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou-env17-d01 &ResourceId.1=asg-bp17xb4x1vr29lgt**** &ResourceType=scalinggroup
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>74C4E313-8570-479F-8791-DC25360D****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "74C4E313-8570-479F-8791-DC25360D****"
}
```

弹性伸缩 ESS

#### ListTagResources

调用ListTagResources查询一个或多个弹性伸缩资源已经绑定的标签列表。

**接口说明**

请求中至少指定一个参数： `ResourceId.N` 或者 `Tag.N` （ `Tag.N.Key` 与 `Tag.N.Value` ），用以确定查询对象。 如果同时指定参数 `Tag.N` 和 `ResourceId.N` 时，返回结果中仅包含同时满足这两个条件的弹性伸缩资源。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTagResource s | 系统规定参数。取值： ListTagResources。 |
| RegionId | String | 是 | cn-hangzhou- env17-d01 | 资源所属的地域ID。您可以调用API DescribeRegions 查看最新的阿里云地域列表。 |
| ResourceType | String | 是 | scalinggroup | 资源类型，目前只支持伸缩组。取值为 scalinggroup。 |
| ResourceId.N | RepeatL ist | 否 | asg- bp17xb4x1vr29l gt**** | 资源ID。N的取值范围：1~50。 |
| Tag.N.Key | String | 否 | TestKey | 精确查找弹性伸缩资源时使用的标签键。 标签键长度的取值范围：1~128。N的取值范围：1~20。 Tag.N 用于精确查找绑定了指定标签的ECS资源，由一个键值对组成。 仅指定 Tag.N.Key 时，则返回关联该标签键的所有资源。 仅指定 Tag.N.Value 时，则报错 MissingParameter.TagKey 。 同时指定多个标签键值对时，仅同时满足所有标签键值对的弹性伸缩资源会被查找到。 |
| Tag.N.Value | String | 否 | TestValue | 精确查找弹性伸缩资源时使用的标签值。 标签值长度的取值范围：1~128。N的取值范围：1~20。 |
| NextToken | String | 否 | caeba0bbb2be0 3f84eb48b699f0 a**** | 下一个查询开始的 Token。 NextToken 为空表示没有下一个。 |

弹性伸缩 ESS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f8 4eb48b699f0a**** | 下一个查询开始的Token。 |
| RequestId | String | DE65F6B7-7566- 4802-9007- 96F2494A**** | 请求ID。 |
| TagResources | Array of TagResource |  | 由资源及其标签组成的集合，包含了资源ID、资源类型和标签键值等信息。 |
| TagResource |  |  |  |
| ResourceId | String | asg- bp17xb4x1vr29lgt* *** | 资源ID。 |
| ResourceType | String | ALIYUN::ESS::SCALI NGGROUP | 资源类型。 |
| TagKey | String | TestKey | 标签键。 |
| TagValue | String | TestValue | 标签值。 |

**示例**

请求示例

```
http(s)://ess.example.com/?Action=ListTagResources &RegionId=cn-hangzhou-env17-d01 &ResourceType=scalinggroup &NextToken=caeba0bbb2be03f84eb48b699f0a4883 &ResourceId=["asg-bp17xb4x1vr29lgt****"] &Tag=[{"Key":"TestKey","Value":"TestValue"}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <NextToken>caeba0bbb2be03f84eb48b699f0a****</NextToken>
    <RequestId>DE65F6B7-7566-4802-9007-96F2494A****</RequestId>
        <ResourceId>asg-bp17xb4x1vr29lgt****</ResourceId>
        <TagKey>TestKey</TagKey>
        <ResourceType>ALIYUN::ESS::SCALINGGROUP</ResourceType>
        <TagValue>TestValue</TagValue>
```

弹性伸缩 ESS `JSON` 格式

```json
{
    "NextToken":"caeba0bbb2be03f84eb48b699f0a****",
    "RequestId":"DE65F6B7-7566-4802-9007-96F2494A****",
        "ResourceId":"asg-bp17xb4x1vr29lgt****",
        "TagKey":"TestKey",
        "ResourceType":"ALIYUN::ESS::SCALINGGROUP",
        "TagValue":"TestValue"
    }]
}
```

#### UntagResources

调用UntagResources为指定的弹性伸缩资源列表统一解绑标签。解绑后，如果该标签没有绑定其他任何资源，会被自动删除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UntagResources | 系统规定参数。取值： UntagResources。 |
| RegionId | String | 是 | cn-hangzhou- env17-d01 | 资源所属的地域ID。您可以调用API DescribeRegions 查看最新的阿里云地域列表。 |
| ResourceId.N | RepeatL ist | 是 | asg- bp17xb4x1vr29l gt**** | 资源ID。N的取值范围为1~50。 |
| ResourceType | String | 是 | scalinggroup | 资源类型，目前只支持伸缩组。取值为 scalinggroup。 |
| TagKey.N | RepeatL ist | 否 | TestKey | 资源的标签键。N的取值范围为1~20。 |
| All | Boolean | 否 | false | 是否解绑资源上全部的标签。当请求中未设置 TagKey.N 时，该参数才有效。取值范围： true：解绑资源上的全部标签。 false：不解绑标签。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| RequestId | String | 3AEBB1B9-5B13- 4311-951F- C3C7FA2B**** | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
&RegionId=cn-hangzhou-env17-d01 &ResourceId.1=asg-bp17xb4x1vr29lgt**** &ResourceType=scalinggroup
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>3AEBB1B9-5B13-4311-951F-C3C7FA2B****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "3AEBB1B9-5B13-4311-951F-C3C7FA2B****"
}
```

#### ListTagKeys

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTagKeys | 系统规定参数。取值：ListTagKeys。 |
| RegionId | String | 是 | cn-hangzhou- env17-d01 | 弹性伸缩资源所属地域的ID。 |
| ResourceType | String | 是 | scalinggroup | 弹性伸缩资源类型。取值为 scalinggroup 时，表示标签绑定的对象是伸缩组。 |
| NextToken | String | 否 | caeba0bbb2be0 3f84eb48b699f0 a**** | 下一个查询开始的 Token， NextToken 为空表示没有下一个。 |

弹性伸缩 ESS

| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。最大值： 50。 默认值：10。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Keys | List | ESS | 标签键信息。 |
| NextToken | String | caeba0bbb2be03f8 4eb48b699f0a**** | 下一个查询开始的Token， NextToken 为空表示没有下一个。 |
| PageSize | Integer | 10 | 输入时设置的每页行数。 |
| RequestId | String | DC09A6AA-2713- 4E10-A2E9- E6C5C43A**** | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou-env17-d01 &ResourceType=scalinggroup
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <PageSize>10</PageSize>
      <NextToken>caeba0bbb2be03f84eb48b699f0a****</NextToken>
      <RequestId>DC09A6AA-2713-4E10-A2E9-E6C5C43A****</RequestId>
      <Keys>ESS</Keys>
```

`JSON` 格式

```json
{
    "PageSize": 10,
    "NextToken": "caeba0bbb2be03f84eb48b699f0a****",
    "RequestId": "DC09A6AA-2713-4E10-A2E9-E6C5C43A****",
    "Keys": "ESS"
}
```

**错误码**

弹性伸缩 ESS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidResourceType.N otFound | The ResourceType provided does not exist in our records. | 资源类型参数非法。 |

#### ListTagValues

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTagValues | 系统规定参数。取值：ListTagValues。 |
| Key | String | 是 | ESS | 标签键。 |
| RegionId | String | 是 | cn-hangzhou- env17-d01 | 弹性伸缩资源所属地域的ID。 |
| ResourceType | String | 是 | scalinggroup | 弹性伸缩资源类型。取值为scalinggroup 时，表示标签绑定的对象是伸缩组。 |
| NextToken | String | 否 | caeba0bbb2be0 3f84eb48b699f0 a**** | 下一个查询开始的 Token， NextToken 为空表示没有下一个。 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。最大值： 50。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f8 4eb48b699f0a**** | 下一个查询开始的Token， NextToken 为空表示没有下一个。 |
| PageSize | Integer | 10 | 输入时设置的每页行数。 |
| RequestId | String | AB444F46-1CFF- 4B06-B8F0- B45D3158**** | 请求ID。 |

弹性伸缩 ESS

| Values | List | Doc | 标签值信息。 |
|---|---|---|---|

**示例**

请求示例

```
&Key=ESS &RegionId=cn-hangzhou-env17-d01 &ResourceType=scalinggroup
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <PageSize>10</PageSize>
      <NextToken>caeba0bbb2be03f84eb48b699f0a****</NextToken>
      <RequestId>AB444F46-1CFF-4B06-B8F0-B45D3158****</RequestId>
      <Values>Doc</Values>
```

`JSON` 格式

```json
{
    "PageSize": 10,
    "NextToken": "caeba0bbb2be03f84eb48b699f0a****",
    "RequestId": "AB444F46-1CFF-4B06-B8F0-B45D3158****",
    "Values": "Doc"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidResourceType.N otFound | The ResourceType provided does not exist in our records. | 资源类型参数非法。 |
| 400 | InvalidTagKey.Malform ed | The specified tag key "%s" is not valid. | 指定的标签键不存在。 |

### 其他

#### DescribeLimitation

弹性伸缩 ESS

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKey Id | Strin g | Query | 否 | 2442****45 | 系统规定参数。用户账号 AcessKeyId。 |
| Action | Strin g | Query | 是 | DescribeLimitation | 系统规定参数。取值： DescribeLimitation。 |
| OwnerId | Long | Query | 否 | 3554****2 | 系统规定参数。用户账号 ID。 |
| Resource OwnerAcc ount | Strin g | Query | 否 | 233****67 | 系统规定参数。资源归属者账号ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| MaxNumberOf ScalingInstanc es | Integer | 1000 | 一个伸缩组单次支持伸缩ECS实例的最大数量。 |
| RequestId | String | BE9BEB41-E7B8- 4C7D-A3CF- 2DCB106665E9 | 请求ID。 |
| MaxNumberOf ScheduledTas ks | Integer | 20 | 一个账号在一个地域下支持创建定时任务的最大数量。 |
| MaxNumberOf VServerGroup s | Integer | 5 | 关联传统型负载均衡CLB（原SLB）实例时，一个伸缩组支持指定虚拟服务器组的最大数量。 |
| MaxNumberOf LoadBalancers | Integer | 10 | 一个伸缩组支持关联传统型负载均衡CLB（原 SLB）实例的最大数量。 |
| MaxNumberOf AlbServerGrou p | Integer | 30 | 一个伸缩组支持关联应用型负载均衡ALB服务器组的最大数量。 |
| MaxNumberOf MinSize | Integer | 2000 | 一个伸缩组支持为最小实例数设置的最大数量。 |
| MaxNumberOf ScalingGroups | Integer | 50 | 一个账号在一个地域下支持创建伸缩组的最大数量。 |

| 开发指南·API参考 |  |  | 弹性伸缩 ES |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| MaxNumberOf NotificationCo nfigurations | Integer | 6 | 一个伸缩组支持创建事件通知的最大数量。 |
| MaxNumberOf MaxSize | Integer | 2000 | 一个伸缩组支持为最大实例数设置的最大数量。 |
| MaxNumberOf DBInstances | Integer | 8 | 一个伸缩组支持关联RDS实例的最大数量。 |
| MaxNumberOf LifecycleHooks | Integer | 6 | 一个伸缩组支持创建生命周期挂钩的最大数量。 |
| MaxNumberOf ScalingRules | Integer | 50 | 一个伸缩组支持创建伸缩规则的最大数量。 |
| MaxNumberOf ScalingConfigu rations | Integer | 10 | 一个伸缩组支持创建伸缩配置的最大数量。 |
| MaxNumberOf NlbServerGrou p | Integer | 30 | 一个伸缩组支持关联网络型负载均衡NLB服务器组的最大数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLimitation
```

&公共请求参数正常返回示例 `JSON` 格式弹性伸缩 ESS

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "MaxNumberOfScalingInstances":1000,
 "RequestId":"BE9BEB41-E7B8-4C7D-A3CF-2DCB106665E9",
 "MaxNumberOfScheduledTasks":20,
 "MaxNumberOfVServerGroups":5,
 "MaxNumberOfLoadBalancers":10,
 "MaxNumberOfAlbServerGroup":30,
 "MaxNumberOfMinSize":2000,
 "MaxNumberOfScalingGroups":50,
 "MaxNumberOfNotificationConfigurations":6,
 "MaxNumberOfMaxSize":2000,
 "MaxNumberOfDBInstances":8,
 "MaxNumberOfLifecycleHooks":6,
 "MaxNumberOfScalingRules":50,
 "MaxNumberOfNlbServerGroup":"",
 "MaxNumberOfScalingConfigurations":10
}
```

`XML` 格式

```xml
<MaxNumberOfScalingInstances>1000</MaxNumberOfScalingInstances> <RequestId>BE9BEB41-E7B8-4C7D-A3CF-2DCB106665E9</RequestId> <MaxNumberOfScheduledTasks>20</MaxNumberOfScheduledTasks> <MaxNumberOfVServerGroups>5</MaxNumberOfVServerGroups> <MaxNumberOfLoadBalancers>10</MaxNumberOfLoadBalancers> <MaxNumberOfAlbServerGroup>30</MaxNumberOfAlbServerGroup> <MaxNumberOfMinSize>2000</MaxNumberOfMinSize> <MaxNumberOfScalingGroups>50</MaxNumberOfScalingGroups> <MaxNumberOfNotificationConfigurations>6</MaxNumberOfNotificationConfigurations> <MaxNumberOfMaxSize>2000</MaxNumberOfMaxSize> <MaxNumberOfDBInstances>8</MaxNumberOfDBInstances> <MaxNumberOfLifecycleHooks>6</MaxNumberOfLifecycleHooks> <MaxNumberOfScalingRules>50</MaxNumberOfScalingRules> <MaxNumberOfNlbServerGroup /> <MaxNumberOfScalingConfigurations>10</MaxNumberOfScalingConfigurations>
```

### 错误代码表

#### 客户端错误

本节介绍客户端导致的报错的详情。 表 1. 错误说明

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| 400 | MissingParameter | The input parameter <parameter name> that is mandatory for processing this request is not supplied. | 缺少参数。 |
|---|---|---|---|
| 400 | InvalidParameter | The specified value of parameter <parameter name> is not valid. | 参数取值无效。 |
| 400 | UnsupportedOperation | The specified action is not supported. | 无效的接口。 |
| 400 | NoSuchVersion | The specified version does not exist. | 无效的版本。 |
| 400 | Throttling | Request was denied due to request throttling. | 操作被流量控制系统拒绝。 |
| 400 | InvalidAccessKeyId.No tFound | The Access Key ID provided does not exist in our records. | 无效的AccessKey。 |
| 403 | Forbidden | Users are not authorized to operate on the specified resource. | 操作被禁止。 |
| 403 | Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 操作被风险控制系统禁止。 |
| 403 | SignatureDoesNotMatc h | The signature we calculated does not match the one you provided. | 无效的签名。 |
| 403 | Forbidden.Unsubscribe d | Do not have permission to access this API. | 您未开通弹性伸缩，无权调用该API。 |
| 403 | Forbidden.UserVerifica tion | Your user account is not verified by Aliyun. | 未实名验证。 |
| 400 | ResourceNotAvailable | Resource you requested is not available in this region or zone. | 指定的地域不支持弹性伸缩。 |

#### 服务器端错误

本节介绍服务器端导致的报错的详情。 表 1. 错误说明

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

弹性伸缩 ESS

| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 服务器无法完成对请求的处理。 |
|---|---|---|---|
| 503 | ServiceUnavailable | The request has failed due to a temporary failure of the server. | 服务器当前无法处理请求。 |

### 如何保证幂等性

本节介绍如何通过ClientToken保证请求的幂等性。 当调用执行伸缩规则接口创建或释放ECS实例时，如果发生请求超时或服务器内部错误，客户端可能会尝试重发请求，这时客户端可以通过提供可选参数ClientToken避免创建或释放出比预期要多的实例，即通过提供ClientToken参数保证请求的幂等性。ClientToken是一个由客户端生成的唯一的、大小写敏感、不超过 64个ASCII字符的字符串。 如果您使用同一个ClientToken值调用创建实例接口，则服务端会返回相同的请求结果，包含相同的 ScalingActivityId。因此您在遇到错误进行重试的时候，可以通过提供相同的ClientToken值，来确保只创建一个伸缩活动，并得到这个伸缩活动的ScalingActivityId。 如果您提供了一个已经使用过的ClientToken，但其他请求参数不同，则弹性伸缩会返回 `IdempotentParameterMismatch` 的错误代码。需要注意的是，SignatureNonce、Timestamp和 Signature参数在重试时是需要变化的，因为弹性伸缩使用SignatureNonce来防止重放攻击，使用 Timestamp来标记每次请求时间，所以再次请求必须提供不同的SignatureNonce和Timestamp参数值， 这同时也会导致Signature值的变化。 通常，客户端只需要在503（ServiceUnavailable）错误、或者无法得到响应结果的情况下进行重试操作。返回结果是200时，重试可以得到与上次相同的结果，但不会对服务端状态产生任何影响。而对4xx或 500的返回错误，除非提示信息里明确出现try it later，否则重试也无法成功。 弹性伸缩 ESS

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

弹性伸缩 ESS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 长度为1~1024个字符。 |

### 返回结果

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | 无 | 无 | 访问凭证。 |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | 访问密钥ID。 |
| AccessKeySecret | String | ****************************************** | 访问密钥。 |
| SecurityToken | String | ******** | 安全令牌。 |
| Expiration | String | 2015-04- 09T11:52:19Z | 失效时间。 |
| AssumedRoleUser | 无 | 无 | 角色扮演时的临时身份。 |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | 临时身份的ARN。 |
| AssumedRoleId | String | 34458433936495** **:alice | 临时身份的ID。 |

**示例**

**引入Pom依赖**

弹性伸缩 ESS 操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下:

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
if(Sti Util
```

iE

```
t( Rl))
```

t 弹性伸缩 ESS

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

下列代码以调用ECS的 `DescribeZones` 接口为示例。 弹性伸缩 ESS

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

弹性伸缩 ESS

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
