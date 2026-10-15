---
title: "负载均衡 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 206
source_pdf: "06_开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/slb/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 负载均衡 开发指南

负载均衡

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
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

负载均衡

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
负载均衡

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
负载均衡

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参见获取STS AccessKey。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号 AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni- manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方法可参见《Apsara Uni- manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
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
负载均衡
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

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 "sts.aliyuns.com" ，请替换为实际的STS Endpoint。 负载均衡

```
public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。 `//` 请替换为您实际的地域`ID`、`AccessKey ID`、`AccessKey Secret`

```
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>");
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
    // "sts.aliyuns.com" 请替换为实际的STS Endpoint，一般格式为sts-vpc.${global:region}.${global:internet-domain}
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
        } catch (com.aliyuncs.exceptions.ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
        }
    return null;
}
```

3. 通过STS AccessKey三元组调用云产品的接口，下列代码以SLB的DescribeLoadBalancers接口为示例。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>,请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>请替换为您实际的组织ID。 负载均衡

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
    request.setSysDomain("ecs.aliyuns.com");
    request.setSysProduct("Slb");
    request.setSysAction("DescribeLoadBalancers");
    request.setSysVersion("2014-05-15");
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

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以SLB为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**网络**>**负载均衡** **SLB**。
3. 在左侧导航栏中，单击**实例**。
4. 在实例列表中查看**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。 负载均衡

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 获取负载均衡 SLB的SDK包

通过POP网关调用专有云API时，需使用负载均衡 SLB的SDK。本文为您介绍如何获取阿里云开发工具包（SDK）。

**背景介绍**

实现SLB功能需要您同时安装SLB SDK和阿里云核心库。以Java SDK为例，您需要下载 `aliyun-java-sdk-slb` 以及 `aliyun-java-sdk-core` 。 负载均衡 SDK封装了2014-05-15版本API，以访问密钥（AccessKey）识别调用者身份，提供自动签名等功能，方便您通过API创建和管理资源。阿里云开发工具包 （SDK）包括代码以及示例，您可以自行选择语言来创建云应用。 SDK核心库推荐您使用阿里云官网的SDK核心库，该内容适用于所有云产品，也同样适用于专有云产品。

**操作指导**

目前SDK的语言支持：Java、Python、Go，您可以前往阿里云开发工具包（SDK）中进行选择。

**说明**

推荐使用 Java、Python、Go三种语言的SDK包，使用其他语言的SDK包可能发生不兼容情况。 负载均衡

## 通过POP网关调用专有云API

### 调用前置

阿里云专有云与公共云一样，可通过POP网关的方式进行API调用。本文为您介绍调用前需要进行的准备工作。

**背景信息**

为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

**获取云产品的Endpoint**

**通过开发者门户获取**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

**通过飞天基础运维平台获取**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。 您也可以自行获取Endpoint，本文以API网关为例为您介绍获取云产品业务域Endpoint的方法。
1. 登录Apsara Uni-manager运维控制台。
2. 顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务注册变量大盘**。
4. 在服务注册变量大盘页面，单击**高级筛选**。
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看apigateway.openapi.endpoint值，即 `Endpoint` 。
负载均衡

**获取公共参数**

通过POP网关调用专有云API过程中所使用的参数，如组织ID、资源集ID、RegionID和实例ID，获取方式请参见本手册**准备工作**下的**获取公共****Header****参数**章节。

### Java版

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07-14）。 调用示例如下： 负载均衡

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

ROA调用，示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 负载均衡

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
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

负载均衡

### Go版

本文为您介绍POP Go SDK调用的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 负载均衡

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

负载均衡使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可参考如下内容进行设置。 `//` 设置请求 `HTTPSInsecure`（只影响当前）

```
request.SetHTTPSInsecure(true) // 设置请求 HTTPSInsecure 为 true isInsecure := request.GetHTTPSInsecure() // 获取请求 HTTPSInsecure
```

当请求未设置时，客户端设置才能生效。 `//` 设置客户端 `HTTPSInsecure`（用于客户端发送的所有请求）。

```
client.SetHTTPSInsecure(true) // 设置客户端 HTTPSInsecure 为 true isInsecure := client.GetHTTPSInsecure() // 获取客户端 HTTPSInsecure
```

### Python版

本文为您介绍POP Python SDK调用云产品API的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

目前仅支持通过RPC方式调用API。

**CommonRequest调用示例**

调用示例接口信息：产品（ECS）、接口（DescribeInstances）、版本（2014-05-26）。 示例代码如下： 负载均衡

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

负载均衡

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

) 负载均衡

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

使用CommonRequest调用方式可实现任意Open API接口的调用。 负载均衡 `//` 创建`API`请求并设置参数。

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

可参考以下代码发起请求并处理返回结果。 负载均衡

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

以下代码为通过Apsara Uni-manager运营控制台的 `GetOrganizationList` 接口获取组织列表的调用示例。 负载均衡

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

本节介绍如何获取负载均衡 SLB的Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。参见获取AccessKey在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。 获取负载均衡 SLB的Endpoint，具体操作参见获取负载均衡 SLB的Endpoint。 阿里云专有云Java SDK需要1.8及以上的JDK。 负载均衡

**安装阿里云专有云 Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用负载均衡 SLB的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17及以上版本，SDK的版本为3.3.8。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 负载均衡

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.alibaba.fastjson.JSON; import java.util.*; import com.aliyuncs.slb.model.v20140515.*; public class DescribeImages {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",
            "<yourAccessKeyID>",
            "<yourAccessKeySecret>");
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```
        DescribeLoadBalancersRequest request = new DescribeLoadBalancersRequest();
```

request.setResourceOwnerAccount("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setResourceOwnerId("1"); // 该参数值为假设值，请您根据实际情况进行填写 request.setRegionId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setServerId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setAddressIPVersion("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setLoadBalancerStatus("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setLoadBalancerId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setLoadBalancerName("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setServerIntranetAddress("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setAddressType("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setInternetChargeType("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setVpcId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setVSwitchId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setNetworkType("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setAddress("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setMasterZoneId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setSlaveZoneId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setOwnerAccount("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setTags("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setPayType("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setResourceGroupId("test"); // 该参数值为假设值，请您根据实际情况进行填写

```java
        try {
            DescribeLoadBalancersResponse response = client.getAcsResponse(request);
            System.out.println(JSON.toJSONString(response));
```

`//` 打印您需要的返回值，此处打印的是此次请求的 `RequestId`

```java
            System.out.println(response.getRequestId());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
```

`//` 打印错误码

```java
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
        }
    }
}
```

### 使用手册

#### 4.2.1. 安装Java SDK

负载均衡本文介绍如何安装及调用负载均衡 SLB的Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包（SDK）的方式安装专有云Java SDK。 要使用SLB的开发工具包，必须安装阿里云Java SDK核心库以及SLB的Java SDK。SDK核心库推荐使用4.5.17及以上版本，Java SDK的版本为3.3.9。 以使用SLB的Java SDK为例，您需要安装阿里云Java SDK核心库和SLB Java SDK，并在pom.xml文件中添加以下依赖即可。准确的SDK版本号，请参见阿里云开发工具包 （SDK）。

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-slb</artifactId>
            <version>3.3.9</version>
        </dependency>
</dependencies>
```

#### 4.2.2. 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。 目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 4.2.3. 发起调用

本文介绍如何使用负载均衡 SLB的Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例如DescribeLoadBalancers。 在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。 负载均衡

```
DescribeLoadBalancersRequest request = new DescribeLoadBalancersRequest();
```

`//` 业务参数 request.setResourceOwnerAccount("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setResourceOwnerId("1"); // 该参数值为假设值，请您根据实际情况进行填写 request.setRegionId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setServerId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setAddressIPVersion("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setLoadBalancerStatus("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setLoadBalancerId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setLoadBalancerName("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setServerIntranetAddress("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setAddressType("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setInternetChargeType("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setVpcId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setVSwitchId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setNetworkType("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setAddress("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setMasterZoneId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setSlaveZoneId("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setOwnerAccount("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setTags("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setPayType("test"); // 该参数值为假设值，请您根据实际情况进行填写 request.setResourceGroupId("test"); // 该参数值为假设值，请您根据实际情况进行填写
3. 发起调用并处理应答。

```java
DescribeLoadBalancersResponse response = client.getAcsResponse(request); System.out.println(JSON.toJSONString(response));
```

#### 4.2.4. 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现以下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考以下示例编写代码：

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

负载均衡

## Python SDK调用示例

### 快速开始

本节介绍如何获取负载均衡 SLB的Python SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体请参见获取AccessKey。 获取负载均衡 SLB的Endpoint，具体操作参见获取负载均衡 SLB的Endpoint。
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
以下以安装负载均衡 SLB的SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装负载均衡 SLB的SDK：

```
pip install aliyun-python-sdk-slb==3.3.8
```

如果您使用的是Python 3.x，执行以下命令，安装负载均衡 SLB的SDK：

```
pip3 install aliyun-python-sdk-slb==3.3.8
```

**使用Python SDK**

以下示例以ECS为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuns.com>，请替换为您实际的产品访问地址。 负载均衡

```
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBalancersRequest client = AcsClient('<yourAccessKeyID>', '<yourAccessKeySecret>', '<yourRegionID>')
```

`//` 创建`API`请求并设置参数 `//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ResourceOwnerAccount("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ResourceOwnerId("1")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_RegionId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ServerId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_AddressIPVersion("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写 `//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_LoadBalancerId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写 `//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ServerIntranetAddress("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_AddressType("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_InternetChargeType("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_VpcId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_VSwitchId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_NetworkType("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_Address("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_MasterZoneId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_SlaveZoneId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_OwnerAccount("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_Tags("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_PayType("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ResourceGroupId("test") response = client.do_action_with_exception(request)
```

`//` 打印您需要的返回值

```python
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### 使用手册

#### 5.2.1. 安装Python SDK

负载均衡本文档介绍如何安装及调用负载均衡SLB的Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。 使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用SLB的Python SDK，您需要安装阿里云Python SDK核心库和SLB的

**说明**

Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

安装云产品的SDK，以下以安装SLB的SDK为例。 如果您使用的是Python 2.x，执行以下命令，安装SLB的SDK：

```
pip install aliyun-python-sdk-slb==3.3.8
```

如果您使用的是Python 3.x，执行以下命令，安装SLB的SDK：

```
pip3 install aliyun-python-sdk-slb==3.3.8
```

#### 5.2.2. 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

**重要**

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 5.2.3. 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。 产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**说明**

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
request.set_protocol_type("https")
```

# 取值：`"https"` 或 `"http"`

**设置全局默认协议**

参考以下代码示例设置全局默认协议：

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
```

# 创建请求并调用 `client.do_action_with_exception()` 来发送请求

#### 5.2.4. 发起调用

本节介绍如何使用负载均衡 SLB的Python SDK发起请求。

**操作步骤**

1. 导入相关产品的SDK。

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBalancersRequest
```

2. 新建一个AcsClient。

```
client = AcsClient('<yourAccessKeyId>', '<yourAccessKeySecret>', '<yourRegionID>')
```

3. 创建Request对象。
负载均衡 `//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ResourceOwnerAccount("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ResourceOwnerId("1")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_RegionId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ServerId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_AddressIPVersion("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写 `//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_LoadBalancerId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写 `//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ServerIntranetAddress("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_AddressType("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_InternetChargeType("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_VpcId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_VSwitchId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_NetworkType("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_Address("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_MasterZoneId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_SlaveZoneId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_OwnerAccount("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_Tags("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_PayType("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
request.set_ResourceGroupId("test")
```

4. 发起调用并处理返回。

```
response = client.do_action_with_exception(request)
```

`//` 打印您需要的返回值

```python
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

#### 5.2.5. 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码： 负载均衡

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

负载均衡

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问。本操作介绍如何获取阿里云负载均衡 SLB的Go SDK并开始调用。

**环境准备**

使用Go SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。参见获取AccessKey在Apsara Uni-manager运营控制台上获取和查看您的 AccessKey。 获取负载均衡 SLB的Endpoint，具体操作参见获取负载均衡 SLB的Endpoint。

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

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您实际的Endpoint。 负载均衡

```java
package main import (
  "fmt"
  slb "github.com/aliyun/alibaba-cloud-sdk-go/services/slb"
```

)

```
func main() {
  client, err := slb.NewClientWithAccessKey("cn-hangzhou", "<yourAccessKeyID>", "<yourAccessKeySecret>")
```

`//` 创建`API`请求并设置参数

```
  request := ecs.CreateDescribeLoadBalancersRequest()
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ResourceOwnerAccount = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ResourceOwnerId = "1"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.RegionId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ServerId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.AddressIPVersion = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.LoadBalancerStatus = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.LoadBalancerId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.LoadBalancerName = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ServerIntranetAddress = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.AddressType = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.InternetChargeType = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.VpcId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.VSwitchId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.NetworkType = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.Address = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.MasterZoneId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.SlaveZoneId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.OwnerAccount = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.Tags = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.PayType = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ResourceGroupId = "test"
  response, err := client.DescribeLoadBalancers(request)
  if err != nil {
    fmt.Println(err)
    return
  }
```

`//` 打印您需要的返回值，此处打印的是此次请求的 `RequestId`

```
  fmt.Println(response.RequestId)
}
```

4. （可选）切换HTTP/HTTPS协议。
负载均衡

```
request.Scheme = "HTTPS"
```

### 使用手册

#### 6.2.1. 安装Go SDK核心包

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 6.2.2. 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。

**重要**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的阿里云账号的信息安全。

```
client, err := slb.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>")
```

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 6.2.3. 发起调用

本文介绍如何使用负载均衡 SLB的Go SDK发起调用。
1. 导入云产品SDK。

```java
import (
  "fmt"
  slb "github.com/aliyun/alibaba-cloud-sdk-go/services/slb"
```

)
2. 新建一个产品名Client，该client中包含产品名的所有API。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

**说明**

```
client, err := slb.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>")
```

3. 使用 `xxx.CreateXXXRequest` 方法创建一个请求。
该方法的命名规范为 ${service}.Create${apiName}Request ，其中：
**${service}**为产品名称(小写)。例如slb。
**${apiName}**为API名称，例如DescribeLoadBalancers。
负载均衡

```
request := slb.CreateDescribeLoadBalancersRequest()
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ResourceOwnerAccount = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ResourceOwnerId = "1"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.RegionId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ServerId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.AddressIPVersion = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.LoadBalancerStatus = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.LoadBalancerId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.LoadBalancerName = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ServerIntranetAddress = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.AddressType = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.InternetChargeType = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.VpcId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.VSwitchId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.NetworkType = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.Address = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.MasterZoneId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.SlaveZoneId = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.OwnerAccount = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.Tags = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.PayType = "test"
```

`//` 该参数值为假设值，请您根据实际情况进行填写

```
  request.ResourceGroupId = "test"
```

4. 发起调用。

```
response, err := client.DescribeLoadBalancers(request)
```

#### 6.2.4. 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。

```
  response, err := client.DescribeLoadBalancers(request)
  if err != nil {
    fmt.Println(err)
    return
  }
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个 `ClientError` 。 负载均衡您可以通过以下代码来判断并获取 `ClientError` 中的错误信息： 使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法请参考：

**重要**

```java
package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := client.DescribeLoadBalancers(request) if clientError, ok := err.(*errors.ClientError); ok{
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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从Response中获得原始的HTTP应答。 您可以通过以下代码来判断并获取ServerError以及Response中的错误信息： 使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法请参考：

**重要**

```java
package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := client.DescribeLoadBalancers(request) if serverError, ok := err.(*errors.ServerError); ok{
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

负载均衡

## API参考

### 调用方式

负载均衡接口调用是向负载均衡API的服务端地址发送HTTP GET请求，并按照接口说明在请求中加入相应请求参数，调用后系统会返回处理结果。请求及返回结果都使用 UTF-8字符集进行编码。

**请求结构**

负载均衡的API是RPC风格，您可以通过发送HTTP GET请求调用负载均衡API。 其请求结构如下：

```
http://Endpoint/?Action=xx&Parameters
```

其中：

| Endpoint：负载均衡 API 的服务接入地址为 | slb.example.com | 。 |
|---|---|---|
| 说明 example.com 是项目自定义的访问域名，请联系管理员获取该域名，具体操作，请参见获取负载均衡SLB的Endpoint。 |  |  |

**Action**：要执行的操作，如使用DescribeLoadBalancers查询已创建的负载均衡实例。
**Version**：要使用的API版本，负载均衡的API版本是2014-05-15。
**Parameters**：请求参数，每个参数之间用“&”分隔。
请求参数由公共请求参数和API自定义参数组成。公共参数中包含API版本号、身份验证等信息，更多信息，请参见公共参数。 下面是一个调用DescribeLoadBalancers接口查询已创建的负载均衡实例的示例：

**说明**

为了便于用户查看，本文档中的示例都做了格式化处理。

```
https://slb.example.com/?Action=DescribeLoadBalancers &Format=xml &Version=2014-05-15 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &TimeStamp=2016-02-23T12:46:24Z
```

…

**API授权**

为了确保您的账号安全，建议您使用RAM用户的身份凭证调用API。如果您使用RAM用户调用负载均衡API，您需要为该RAM用户创建、附加相应的授权策略。

**API签名**

负载均衡服务会对每个API请求进行身份验证，无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。 负载均衡通过使用AccessKey ID和AccessKey Secret进行对称加密的方法来验证请求的发送者身份。AccessKey是为阿里云账号和RAM用户发布的一种身份凭证(类似于用户的登录密码)，其中AccessKey ID 用于标识访问者的身份，AccessKey Secret是用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密，具体操作，请 RPC API需按如下格式在请求中增加签名（Signature）：

| https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf |  |  |  |
|---|---|---|---|
| 以DescribeLoadBalancers为例，假设AccessKey ID是 | testid | ， AccessKey Secret是 | testsecret |
| http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-26 &SignatureVersion=1.0 |  |  |  |

完成以下步骤计算签名：
1. 使用请求参数创建待签名字符串：

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeLoadBalancers&Format%3DXML&SignatureMethod%3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94 f-4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. 计算待签名的HMAC的值。

| 在AccessKey Secret后添加一个and（&）符号作为计算HMAC值的key。本示例中的key为 | testsecret& | 。 |
|---|---|---|
| CT9X0VtwR86fNWSnsc6v8YG****E= |  |  |

3. 将签名加到请求参数中：
负载均衡

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-15 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### RAM鉴权

在使用RAM账号调用SLB API前，需要主账号通过创建授权策略对RAM账号进行授权。在授权策略中，使用资源描述符（Alibaba Cloud Resource Name, ARN）指定授权资源。

**可授权的负载均衡资源类型**

在进行RAM子账号授权时，SLB资源的描述方式如下：

| 资源类型 | 授权策略中的资源描述方法 |
|---|---|
| LoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:slb:$regionid:$accountid:loadbalancer/* |
|  | acs:slb:*:$accountid:loadbalancer/* |
|  | acs:slb:*:*:loadbalancer/* |
| Certificate | acs:slb:$regionid:$accountid:certificate/$servercertificateId |
|  | acs:slb:$regionid:$accountid:certificate/* |

其中 $regionid/accoutid/servercertificateId ... 为具体的资源ID， * 代表对应的所有资源。

**可授权的SLB接口**

下表列举了SLB中可授权的API及其描述方式：

| API | 资源描述 |
|---|---|
| CreateLoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/* |
| ModifyLoadBalancerInternetSpec | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DeleteLoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerStatus | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerName | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancers | acs:slb:$regionid:$accountid:loadbalancer/* |
| DescribeLoadBalancerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeRegions | acs:slb:*:$accountid:* |
| UploadServerCertificate | acs:slb:%s:%s:certificate/* |
| DeleteServerCertificate | acs:slb:%s:%s:certificate/% |
| DescribeServerCertificate | acs:slb:%s:%s:certificate/% |
| SetServerCertificateName | acs:slb:%s:%s:certificate/% |
| DescribeServerCertificates | acs:slb:%s:%s:certificate/* |
| CreateLoadBalancerHTTPListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| CreateLoadBalancerHTTPSListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:slb:%s:%s:certificate/% |
| CreateLoadBalancerTCPListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| CreateLoadBalancerUDPListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DeleteLoadBalancerListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| StartLoadBalancerListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| StopLoadBalancerListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerHTTPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerHTTPSListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |

|  | acs:slb:%s:%s:certificate/% |
|---|---|
| SetLoadBalancerTCPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerUDPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancerHTTPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancerHTTPSListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancerTCPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancerUDPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| AddBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| RemoveBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| SetBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| DescribeHealthStatus | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| CreateVServerGroup | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| SetVServerGroupAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DeleteVServerGroup | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeVServerGroups | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeVServerGroupAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| AddVServerGroupBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| RemoveVServerGroupBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |
| ModifyVServerGroupBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|  | acs:ecs:$regionid:$accountid:instance/$instanceid |

### 公共参数

**公共请求参数**

公共请求参数是每个接口都需要使用到的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回消息的格式。取值： JSON (默认值) \| XML |
| Version | String | 是 | API版本号，使用 YYYY-MM-DD 日期格式。取值： 2014-05-15 |
| AccessKeyId | String | 是 | 访问服务使用的密钥ID。 |
| Signature | String | 是 | 签名结果串。 |
| SignatureMethod | String | 是 | 签名方式，取值： HMAC-SHA1 |
| Timestamp | String | 是 | 请求的时间戳，为日期格式。使用UTC时间按照 ISO8601标，格式为 YYYY-MM-DDThh:mm:ssZ 。 例如，北京时间2013年1月10日20点0分0秒，表示为2013-01-10T12:00:00Z。 |
| SignatureVersion | String | 是 | 签名算法版本，取值： 1.0 |

负载均衡

| SignatureNonce | String | 是 | 唯一随机数，用于防止网络重放攻击。 在不同请求间要使用不同的随机数值。 |
|---|---|---|---|

**示例**

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2014-05-19T10%3A33%3A56Z &Format=xml &AccessKeyId=testid &SignatureMethod=Hmac-SHA1 &LoadBalancerId=loadBalancerID &SignatureNonce=NwDAxvLU6tFE0DVb &Version=2014-05-15 &SignatureVersion=1.0 &Signature=Signature
```

**公共返回参数**

API返回结果采用统一格式，返回2xx HTTP状态码代表调用成功；返回4xx或5xx HTTP状态码代表调用失败。调用成功返回的数据格式有XML和JSON两种，可以在发送请求时指定返回的数据格式，默认是JSON格式。 每次接口调用，无论成功与否，系统都会返回一个唯一识别码**RequestId**。 XML格式

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

### 负载均衡实例

#### 7.4.1. DescribeLoadBalancerListeners

调用DescribeLoadBalancerListeners接口查询负载均衡实例监听列表。

**前提条件**

您已安装v3.16.2r-slb-SP009。

**使用说明**

公共请求参数请参考本手册中公共参数章节。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 否 | cn-hangzhou | 负载均衡实例所在的地域ID。 您可以通过调用 DescribeRegions 接口获取地域ID。 当您所选地域的Enpoint（服务地址）为 slb.aliyuncs.com时， RegionId 必填。 |
| Action | String | Query | 否 | DescribeLoadBalancerListeners | 系统规定参数。取值：DescribeLoadBalancerListeners 。 |
| OwnerId | Long | Query | 否 |  |  |

| 开发指南·API参 | 考 |  |  |  | 负载均衡 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceOwnerAcc ount | String | Query | 否 |  |  |
| ResourceOwnerId | Long | Query | 否 |  |  |
| OwnerAccount | String | Query | 否 |  |  |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| MaxResults | Integer | Query | 否 | 50 | 分批次查询时每次显示的条目数。 取值范围：1 ~100 ，入参为空时，默认值：20 。 |
| ListenerProtocol | String | Query | 否 | http | 负载均衡监听协议。取值： tcp udp http https |
| LoadBalancerId | RepeatList | Query | 否 | LoadBalancerId.1=lb- uf6so8u4g35prnvsw****,LoadBalancerId.2 =lb-uf6s1l1kukqv4u5nt**** | 负载均衡实例的ID列表，最多支持10个实例 ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Listeners | Array |  | 返回负载均衡的监听列表。 实例未配置监听时，不会返回该参数。 |
| -AclId | String | nacl-a2do9e413e0spzasx**** | 访问控制策略组ID。 |
| -AclStatus | String | off | 是否开启访问控制功能。取值： on ：是 off ：否 |
| -AclType | String | white | 访问控制类型。取值： white ：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求， 白名单适用于只允许特定IP访问的场景。设置白名单存在一定业务风险。一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black ：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 |
| -BackendServerPort | Integer | 80 | 后端服务器的端口。 VServerGroupId 和 MasterSlaveServerGroupId 均为空时，此参数有效。 |
| -Bandwidth | Integer | -1 | 监听的带宽峰值。单位：Mbps。取值： -1 ：不限制带宽峰值。 1~5120 ：监听的带宽峰值，所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
| -Description | String | test | 监听描述。 |
| -ListenerPort | Integer | 80 | 监听端口。 |
| -ListenerProtocol | String | http | 负载均衡监听协议。 |
| -LoadBalancerId | String | lb-bp1b6c719dfa**** | 负载均衡实例的ID。 |

|  |  |  | ·API |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Scheduler | String | wrr | 调度算法。取值： wrr ：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 rr ：按照访问顺序依次将外部请求依序分发到后端服务器。 |
| -Status | String | running | 监听的状态。取值： running ：表示监听正常运行。 stopped ：表示监听运行停止。 |
| -VServerGroupId | String | rsp-cige6j**** | 监听绑定的虚拟服务器组ID。 |
| -HTTPListenerConfig | Struct |  | HTTP监听配置。 |
| --Cookie | String | B490B5EBF6F3CD402E515D22BC DA**** | 服务器上配置的Cookie。 |
| --CookieTimeout | Integer | 500 | Cookie超时时间。单位：秒。 取值：1 ~86400 。 |
| --ForwardPort | Integer | 80 | HTTP转发至HTTPS的监听端口。 如果ListenerForward 的值为off ，该参数不显示。 |
| --Gzip | String | on | 是否开启Gzip压缩。取值： on ：是 off ：否 |
| --HealthCheck | String | on | 是否开启健康检查。取值： on ：是 off ：否 |
| --HealthCheckConnectPort | Integer | 8080 | 健康检查的端口。 当HealthCheck 值为on 时该参数有效。 |
| --HealthCheckDomain | String | www.example.com | 健康检查的域名。 |
| --HealthCheckHttpCode | String | http2xx,http3xx _ _ | 健康检查正常的HTTP状态码。 |
| --HealthCheckHttpVersion | String | HTTP 1.0 | 健康检查HTTP协议版本。 |
| --HealthCheckInterval | Integer | 5 | 健康检查的时间间隔，单位：秒。 |
| --HealthCheckMethod | String | get | 健康检查方式。取值：head 或get 。 |
| --HealthCheckTimeout | Integer | 3 | 每次健康检查响应的最大超时间，单位：秒。 |
| --HealthCheckType | String | tcp | 健康检查协议。 |
| --HealthCheckURI | String | /test/index.html | 健康检查的URI。 |
| --HealthyThreshold | Integer | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功 。 取值范围：2 ~10 。 |
| --IdleTimeout | Integer | 15 | 指定连接空闲超时时间。单位：秒。取值范围：1 ~60 。 在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到下一次请求来临时重新建立连接。 |
| --ListenerForward | String | on | 是否开启HTTP至HTTPS监听转发。取值： on ：是 off ：否 |

负载均衡

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --RequestTimeout | Integer | 60 | 指定请求超时时间。单位：秒。取值范围：1 ~180 。 在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。 |
| --StickySession | String | on | 是否开启会话保持。取值： on ：是 off ：否 |
| --StickySessionType | String | insert | Cookie的处理方式。取值： insert ：植入Cookie。客户端第一次访问时，负载均衡会在返回请求中植入 Cookie（即在HTTP和HTTPS响应报文中插入SERVERID），下次客户端携带此Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server ：重写Cookie。负载均衡发现用户自定义了Cookie，将会对原来的 Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。 |
| --UnhealthyThreshold | Integer | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败 。 取值范围：2 ~10 。 |
| --XForwardedFor | String | on | 是否通过 XForwardedFor 的方式获取来访者真实IP。取值： on ：是。 off ：否。 |
| -- XForwardedForClientSrcP _ ort | String | on | 是否通过 XForwardedFor_ClientSrcPort 头字段获取访问负载均衡实例客户端的端口。取值： on ：是 off ：否 |
| --XForwardedForSLBID _ | String | on | 是否通过 SLB-ID 头字段获取负载均衡实例ID。取值： on ：是 off ：否 |
| --XForwardedForSLBIP _ | String | on | 是否通过 SLB-IP 头字段获取客户端请求的VIP（Virtual IP address）。取值： on ：是 off ：否 |
| -- XForwardedForSLBPORT _ | String | on | 是否通过 XForwardedFor_SLBPORT 头字段获取负载均衡实例的监听端口。 取值： on ：是 off ：否 |
| --XForwardedForproto _ | String | on | 是否通过 X-Forwarded-Proto 头字段获取负载均衡实例的监听协议。取值： on ：是 off ：否 |
| -HTTPSListenerConfig | Struct |  | HTTPS监听配置。 |
| --CACertificateId | String | idkp-234-cn-test-0**** | CA证书ID。 |
| --Cookie | String | B490B5EBF6F3CD402E515D22BC DA**** | 服务器上配置的Cookie。 |
| --CookieTimeout | Integer | 500 | Cookie超时时间。单位：秒。 取值：1 ~86400 。 |
| --EnableHttp2 | String | off | 是否开启 HTTP 2.0 特性。取值： on ：是 off ：否 |
| --Gzip | String | on | 是否开启Gzip压缩。取值： on ：是 off ：否 |

| 负载均衡 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --HealthCheck | String | on | 是否开启健康检查。取值： on ：是。 off ：否。 |
| --HealthCheckConnectPort | Integer | 8080 | 健康检查的端口。 |
| --HealthCheckDomain | String | www.example.com | 健康检查的域名。 |
| --HealthCheckHttpCode | String | http2xx,http3xx _ _ | 健康检查正常的HTTP状态码。 |
| --HealthCheckHttpVersion | String | HTTP 1.0 | 健康检查HTTP协议版本。 |
| --HealthCheckInterval | Integer | 5 | 健康检查的时间间隔。单位：秒。 |
| --HealthCheckMethod | String | get | 健康检查方式。 |
| --HealthCheckTimeout | Integer | 3 | 每次健康检查响应的最大超时间。单位：秒。 |
| --HealthCheckType | String | tcp | 健康检查协议。 |
| --HealthCheckURI | String | /test/index.html | 健康检查的URI。 |
| --HealthyThreshold | Integer | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功 。 取值范围：2 ~10 。 |
| --IdleTimeout | Integer | 15 | 指定连接空闲超时时间。单位：秒。取值范围：1 ~60 。 在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到下一次请求来临时重新建立连接。 |
| --RequestTimeout | Integer | 60 | 指定请求超时时间，单位：秒。取值范围：1 ~180 。 在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。 |
| --ServerCertificateId | String | idkp-123-cn-test-0**** | 服务器证书的ID。 |
| --StickySession | String | on | 是否开启会话保持。取值： on ：是 off ：否 |
| --StickySessionType | String | insert | Cookie的处理方式。 insert ：植入Cookie。客户端第一次访问时，负载均衡会在返回请求中植入 Cookie（即在HTTP和HTTPS响应报文中插入SERVERID），下次客户端携带此Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server ：重写Cookie。负载均衡发现用户自定义了Cookie，将会对原来的 Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。 |

负载均衡

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --TLSCipherPolicy | String | tlscipherpolicy10 _ _ _ _ | 安全策略包含HTTPS可选的TLS协议版本和配套的加密算法套件。 tls _cipher _policy _1 _0 ： 支持TLS版本： TLSv1.0、TLSv1.1和TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA- AES256-GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA- AES256-SHA384、AES128-GCM-SHA256、AES256-GCM-SHA384、 AES128-SHA256、AES256-SHA256、ECDHE-RSA-AES128-SHA、 ECDHE-RSA-AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tls _cipher _policy _1 _1 ： 支持TLS版本： TLSv1.1和TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA- AES256-GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA- AES256-SHA384、AES128-GCM-SHA256、AES256-GCM-SHA384、 AES128-SHA256、AES256-SHA256、ECDHE-RSA-AES128-SHA、 ECDHE-RSA-AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tlscipherpolicy12 _ _ _ _ 支持TLS版本：TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA- AES256-GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA- AES256-SHA384、AES128-GCM-SHA256、AES256-GCM-SHA384、 AES128-SHA256、AES256-SHA256、ECDHE-RSA-AES128-SHA、 ECDHE-RSA-AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tlscipherpolicy12strict _ _ _ _ _ 支持TLS版本：TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA- AES256-GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA- AES256-SHA384、ECDHE-RSA-AES128-SHA和ECDHE-RSA-AES256- SHA。 tlscipherpolicy12strictwith13 _ _ _ _ _ _ _ _ 支持TLS版本：TLSv1.2及TLSv1.3。 支持的加密算法套件：TLS _AES _128 _GCM _SHA256、 TLS _AES _256 _GCM _SHA384、TLS _CHACHA20 _POLY1305 _SHA256、 TLS _AES _128 _CCM _SHA256、TLS _AES _128 _CCM _8 _SHA256、ECDHE- ECDSA-AES128-GCM-SHA256、ECDHE-ECDSA-AES256-GCM- SHA384、ECDHE-ECDSA-AES128-SHA256、ECDHE-ECDSA-AES256- SHA384、ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA-AES256- GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA-AES256- SHA384、ECDHE-ECDSA-AES128-SHA、ECDHE-ECDSA-AES256- SHA、ECDHE-RSA-AES128-SHA、ECDHE-RSA-AES256-SHA。 |
| --UnhealthyThreshold | Integer | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败 。 取值范围：2 ~10 。 |
| --XForwardedFor | String | on | 否开启通过 XForwardedFor 的方式获取来访者真实IP。取值： on ：是 off ：否 |
| -- XForwardedForClientCert _ ClientVerify | String | off | 是否通过 XForwardedFor_ClientCertClientVerify 头字段获取对访问负载均衡实例客户端证书的校验结果。取值： on ：是 off ：否 |
| -- XForwardedForClientCert _ Fingerprint | String | off | 是否通过 XForwardedFor_ClientCertFingerprint 头字段获取访问负载均衡实例客户端证书的指纹。取值： on ：是 off ：否 |
| -- XForwardedForClientCert _ IssuerDN | String | off | 是否通过 XForwardedFor_ClientCertIssuerDN 头字段获取访问负载均衡实例客户端证书的发行者信息。取值： on ：是 off ：否 |
| -- XForwardedForClientCert _ SubjectDN | String | off | 是否通过 XForwardedFor_ClientCertSubjectDN 头字段获取访问负载均衡实例客户端证书的所有者信息。取值： on ：是。 off ：否。 |

负载均衡

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- XForwardedForClientSrcP _ ort | String | off | 是否通过 XForwardedFor_ClientSrcPort 头字段获取访问负载均衡实例客户端的端口。取值： on ：是 off ：否 |
| --XForwardedForSLBID _ | String | on | 是否通过 SLB-ID 头字段获取负载均衡实例ID。取值： on ：是 off ：否 |
| --XForwardedForSLBIP _ | String | on | 是否通过 SLB-IP 头字段获取客户端请求的VIP（Virtual IP address）。取值： on ：是 off ：否 |
| -- XForwardedForSLBPORT _ | String | off | 是否通过 XForwardedFor_SLBPORT 头字段获取负载均衡实例的监听端口。 取值： on ：是 off ：否 |
| --XForwardedForproto _ | String | on | 是否通过 X-Forwarded-Proto 头字段获取负载均衡实例的监听协议。取值： on ：是 off ：否 |
| -TCPListenerConfig | Struct |  | TCP监听配置。 |
| --ConnectionDrain | String | off | 是否开启连接优雅中断。取值： on ：是 off ：否 |
| --ConnectionDrainTimeout | Integer | 300 | 设置连接优雅中断超时时间。单位：秒。 取值范围：10~900 。 |
| --EstablishedTimeout | Integer | 500 | 连接超时时间。单位：秒。 |
| --HealthCheck | String | on | 是否开启健康检查。取值： on ：是 off ：否 |
| --HealthCheckConnectPort | Integer | 8080 | 健康检查使用的端口。 |
| -- HealthCheckConnectTime out | Integer | 100 | 健康检查超时时间。单位：秒。 取值范围：1 ~300 。 |
| --HealthCheckDomain | String | www.example.com | 健康检查的域名。 |
| --HealthCheckHttpCode | String | http2xx,http3xx _ _ | 健康检查正常的HTTP状态码。 |
| --HealthCheckInterval | Integer | 5 | 健康检查的时间间隔，单位为秒。 |
| --HealthCheckMethod | String | get | 健康检查方式。 |
| --HealthCheckType | String | tcp | 健康检查协议。 |
| --HealthCheckURI | String | /test/index.html | 健康检查的URI。 |
| --HealthyThreshold | Integer | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功 。 取值范围：2 ~10 。 |
| -- MasterSlaveServerGroupI d | String | rsp-0bfucw***** | 监听绑定的主备服务器组ID。 |

| 开发指南·API参考 |  |  | 负载均衡 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --PersistenceTimeout | Integer | 0 | 是否开启了会话保持。单位：秒。 取值范围：0 ~3600 。 取值为0 时，表示未开启。 |
| --UnhealthyThreshold | Integer | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败 。 取值范围：2 ~10 。 |
| -UDPListenerConfig | Struct |  | UDP监听配置。 |
| --ConnectionDrain | String | off | 是否开启连接优雅中断。取值： on ：是 off ：否 |
| --ConnectionDrainTimeout | Integer | 300 | 设置连接优雅中断超时时间。单位：秒。 取值范围：10 ~900 。 |
| --HealthCheck | String | on | 是否开启健康检查。取值： on ：是 off ：否 |
| --HealthCheckConnectPort | Integer | 8080 | 健康检查的端口。 |
| -- HealthCheckConnectTime out | Integer | 100 | 健康检查响应超时时间。 |
| --HealthCheckExp | String | ok | UDP监听健康检查的响应串。 |
| --HealthCheckInterval | Integer | 5 | 健康检查的时间间隔，单位为秒。 |
| --HealthCheckReq | String | hello | UDP监听健康检查的请求串。 |
| --HealthyThreshold | Integer | 4 | 健康检查阈值。 |
| -- MasterSlaveServerGroupI d | String | rsp-0bfucw**** | 绑定的主备服务器组ID。 |
| --UnhealthyThreshold | Integer | 4 | 不健康检查阈值。 |
| MaxResults | Integer | 50 | 分批次查询时每次显示的条目数。 取值范围：1 ~100 ，入参为空时，默认值：20 。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |
| TotalCount | Integer | 10 | 本次请求条件下的数据总量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerListeners
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "Listeners":{ "Status":"running", "ListenerPort":80, "VServerGroupId":"rsp-cige6j****", "Description":"test", |  |

负载均衡 p ,

```json
  "Scheduler":"wrr",
  "AclId":"nacl-a2do9e413e0spzasx****",
  "-HTTPListenerConfig":{
   "CookieTimeout":500,
   "UnhealthyThreshold":4,
   "HealthCheckURI":"/test/index.html",
   "HealthCheck":"on",
   "IdleTimeout":15,
   "XForwardedFor_SLBID":"on",
   "HealthCheckConnectPort":8080,
   "XForwardedFor_SLBPORT":"on",
   "HealthCheckMethod":"get",
   "Gzip":"on",
   "StickySessionType":"insert",
   "XForwardedFor_SLBIP":"on",
   "HealthCheckHttpCode":"http_2xx,http_3xx",
   "Cookie":"B490B5EBF6F3CD402E515D22BCDA****",
   "RequestTimeout":60,
   "HealthCheckInterval":5,
   "HealthCheckHttpVersion":"HTTP 1.0",
   "HealthCheckTimeout":3,
   "ListenerForward":"on",
   "StickySession":"on",
   "ForwardPort":80,
   "HealthyThreshold":4,
   "XForwardedFor":"on",
   "XForwardedFor_ClientSrcPort":"on",
   "HealthCheckDomain":"www.example.com",
   "XForwardedFor_proto":"on",
   "HealthCheckType":"tcp"
  },
  "-UDPListenerConfig":{
   "ConnectionDrainTimeout":300,
   "HealthCheckInterval":5,
   "HealthCheckConnectPort":8080,
   "HealthCheckReq":"hello",
   "UnhealthyThreshold":4,
   "HealthCheckExp":"ok",
   "HealthyThreshold":4,
   "HealthCheck":"on",
   "HealthCheckConnectTimeout":100,
   "MasterSlaveServerGroupId":"rsp-0bfucw****",
   "ConnectionDrain":"off"
  },
  "LoadBalancerId":"lb-bp1b6c719dfa****",
  "BackendServerPort":80,
  "ListenerProtocol":"http",
  "-HTTPSListenerConfig":{
   "CookieTimeout":500,
   "UnhealthyThreshold":4,
   "HealthCheckURI":"/test/index.html",
   "HealthCheck":"on",
   "IdleTimeout":15,
   "XForwardedFor_SLBID":"on",
   "HealthCheckConnectPort":8080,
   "XForwardedFor_SLBPORT":"off",
   "HealthCheckMethod":"get",
   "Gzip":"on",
   "ServerCertificateId":"idkp-123-cn-test-0****",
   "StickySessionType":"insert",
   "XForwardedFor_SLBIP":"on",
   "HealthCheckHttpCode":"http_2xx,http_3xx",
   "Cookie":"B490B5EBF6F3CD402E515D22BCDA****",
   "RequestTimeout":60,
   "HealthCheckInterval":5,
   "TLSCipherPolicy":"tls_cipher_policy_1_0",
   "CACertificateId":"idkp-234-cn-test-0****",
   "XForwardedFor_ClientCertSubjectDN":"off",
   "HealthCheckHttpVersion":"HTTP 1.0",
   "HealthCheckTimeout":3,
   "XForwardedFor_ClientCertIssuerDN":"off",
   "StickySession":"on",
   "HealthyThreshold":4,
   "XForwardedFor":"on",
   "XForwardedFor_ClientSrcPort":"off",
   "HealthCheckDomain":"www.example.com",
   "XForwardedFor_proto":"on",
   "EnableHttp2":"off",
   "XForwardedFor_ClientCertClientVerify":"off",
   "XForwardedFor_ClientCertFingerprint":"off",
   "HealthCheckType":"tcp"
  },
  "-TCPListenerConfig":{
   "HealthCheckInterval":5,
   "UnhealthyThreshold":4,
   "HealthCheckURI":"/test/index.html",
"HealthCheck":"on"
```

负载均衡

```json
   HealthCheck:on,
   "HealthCheckConnectTimeout":100,
   "ConnectionDrain":"off",
   "ConnectionDrainTimeout":300,
   "PersistenceTimeout":0,
   "HealthCheckConnectPort":8080,
   "HealthCheckMethod":"get",
   "HealthyThreshold":4,
   "HealthCheckDomain":"www.example.com",
   "MasterSlaveServerGroupId":"rsp-0bfucw*****",
   "HealthCheckHttpCode":"http_2xx,http_3xx",
   "HealthCheckType":"tcp",
   "EstablishedTimeout":500
  },
  "AclStatus":"off",
  "Bandwidth":-1,
  "AclType":"white"
 },
 "TotalCount":10,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710",
 "MaxResults":50
}
```

| XML | 格式 |
|---|---|
| <Listeners> <Status>running</Status> <ListenerPort>80</ListenerPort> <VServerGroupId>rsp-cige6j****</VServerGroupId> <Description>test</Description> <Scheduler>wrr</Scheduler> <AclId>nacl-a2do9e413e0spzasx****</AclId> <-HTTPListenerConfig> <CookieTimeout>500</CookieTimeout> <UnhealthyThreshold>4</UnhealthyThreshold> <HealthCheckURI>/test/index.html</HealthCheckURI> <HealthCheck>on</HealthCheck> <IdleTimeout>15</IdleTimeout> <XForwardedFor_SLBID>on</XForwardedFor_SLBID> <HealthCheckConnectPort>8080</HealthCheckConnectPort> <XForwardedFor_SLBPORT>on</XForwardedFor_SLBPORT> <HealthCheckMethod>get</HealthCheckMethod> <Gzip>on</Gzip> <StickySessionType>insert</StickySessionType> <XForwardedFor_SLBIP>on</XForwardedFor_SLBIP> <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode> <Cookie>B490B5EBF6F3CD402E515D22BCDA****</Cookie> <RequestTimeout>60</RequestTimeout> <HealthCheckInterval>5</HealthCheckInterval> <HealthCheckHttpVersion>HTTP 1.0</HealthCheckHttpVersion> <HealthCheckTimeout>3</HealthCheckTimeout> <ListenerForward>on</ListenerForward> <StickySession>on</StickySession> <ForwardPort>80</ForwardPort> <HealthyThreshold>4</HealthyThreshold> <XForwardedFor>on</XForwardedFor> <XForwardedFor_ClientSrcPort>on</XForwardedFor_ClientSrcPort> <HealthCheckDomain>www.example.com</HealthCheckDomain> <XForwardedFor_proto>on</XForwardedFor_proto> <HealthCheckType>tcp</HealthCheckType> </-HTTPListenerConfig> <-UDPListenerConfig> <ConnectionDrainTimeout>300</ConnectionDrainTimeout> <HealthCheckInterval>5</HealthCheckInterval> <HealthCheckConnectPort>8080</HealthCheckConnectPort> <HealthCheckReq>hello</HealthCheckReq> <UnhealthyThreshold>4</UnhealthyThreshold> <HealthCheckExp>ok</HealthCheckExp> <HealthyThreshold>4</HealthyThreshold> <HealthCheck>on</HealthCheck> <HealthCheckConnectTimeout>100</HealthCheckConnectTimeout> <MasterSlaveServerGroupId>rsp-0bfucw****</MasterSlaveServerGroupId> <ConnectionDrain>off</ConnectionDrain> </-UDPListenerConfig> <LoadBalancerId>lb-bp1b6c719dfa****</LoadBalancerId> <BackendServerPort>80</BackendServerPort> <ListenerProtocol>http</ListenerProtocol> <-HTTPSListenerConfig> <CookieTimeout>500</CookieTimeout> <UnhealthyThreshold>4</UnhealthyThreshold> <HealthCheckURI>/test/index.html</HealthCheckURI> <HealthCheck>on</HealthCheck> <IdleTimeout>15</IdleTimeout> <XForwardedFor_SLBID>on</XForwardedFor_SLBID> <HealthCheckConnectPort>8080</HealthCheckConnectPort> <XForwardedFor SLBPORT>off</XForwardedFor SLBPORT> |  |

负载均衡 _ _

```xml
  <HealthCheckMethod>get</HealthCheckMethod>
  <Gzip>on</Gzip>
  <ServerCertificateId>idkp-123-cn-test-0****</ServerCertificateId>
  <StickySessionType>insert</StickySessionType>
  <XForwardedFor_SLBIP>on</XForwardedFor_SLBIP>
  <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
  <Cookie>B490B5EBF6F3CD402E515D22BCDA****</Cookie>
  <RequestTimeout>60</RequestTimeout>
  <HealthCheckInterval>5</HealthCheckInterval>
  <TLSCipherPolicy>tls_cipher_policy_1_0</TLSCipherPolicy>
  <CACertificateId>idkp-234-cn-test-0****</CACertificateId>
  <XForwardedFor_ClientCertSubjectDN>off</XForwardedFor_ClientCertSubjectDN>
  <HealthCheckHttpVersion>HTTP 1.0</HealthCheckHttpVersion>
  <HealthCheckTimeout>3</HealthCheckTimeout>
  <XForwardedFor_ClientCertIssuerDN>off</XForwardedFor_ClientCertIssuerDN>
  <StickySession>on</StickySession>
  <HealthyThreshold>4</HealthyThreshold>
  <XForwardedFor>on</XForwardedFor>
  <XForwardedFor_ClientSrcPort>off</XForwardedFor_ClientSrcPort>
  <HealthCheckDomain>www.example.com</HealthCheckDomain>
  <XForwardedFor_proto>on</XForwardedFor_proto>
  <EnableHttp2>off</EnableHttp2>
  <XForwardedFor_ClientCertClientVerify>off</XForwardedFor_ClientCertClientVerify>
  <XForwardedFor_ClientCertFingerprint>off</XForwardedFor_ClientCertFingerprint>
  <HealthCheckType>tcp</HealthCheckType>
 </-HTTPSListenerConfig>
 <-TCPListenerConfig>
  <HealthCheckInterval>5</HealthCheckInterval>
  <UnhealthyThreshold>4</UnhealthyThreshold>
  <HealthCheckURI>/test/index.html</HealthCheckURI>
  <HealthCheck>on</HealthCheck>
  <HealthCheckConnectTimeout>100</HealthCheckConnectTimeout>
  <ConnectionDrain>off</ConnectionDrain>
  <ConnectionDrainTimeout>300</ConnectionDrainTimeout>
  <PersistenceTimeout>0</PersistenceTimeout>
  <HealthCheckConnectPort>8080</HealthCheckConnectPort>
  <HealthCheckMethod>get</HealthCheckMethod>
  <HealthyThreshold>4</HealthyThreshold>
  <HealthCheckDomain>www.example.com</HealthCheckDomain>
  <MasterSlaveServerGroupId>rsp-0bfucw*****</MasterSlaveServerGroupId>
  <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
  <HealthCheckType>tcp</HealthCheckType>
  <EstablishedTimeout>500</EstablishedTimeout>
 </-TCPListenerConfig>
 <AclStatus>off</AclStatus>
 <Bandwidth>-1</Bandwidth>
 <AclType>white</AclType>
</Listeners> <TotalCount>10</TotalCount> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <MaxResults>50</MaxResults>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParam.ListenerProtocol | IllegalParam.ListenerProtocol | The param of ListenerProtocol is illegal. |
| 400 | InvalidParam.PageSize | IllegalParam.MaxResults | The param of MaxResults is illegal. |
| 400 | QueryTokenInvalid | IllegalParam.NextToken | The param of NextToken is illegal. |
| 400 | InvalidParamSize.LoadBalancerId | IllegalParamSize.LoadBalancerId | The param size of LoadBalancerId is illegal. |

#### 7.4.2. DeleteLoadBalancerListener

只有当监听的状态为**stopped**或者**running**时，才可以删除。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteLoadBalancerListener | 要执行的操作。 取值：DeleteLoadBalancerListener。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |

负载均衡

| LoadBalancerId | String | 是 | lb-bp13jaf5qli5xm**** | 负载均衡实例ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xm****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteLoadBalancerListenerResponse> <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId> </DeleteLoadBalancerListenerResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54" } |  |

#### 7.4.3. StopLoadBalancerListener

在调用该接口时，注意： 接口调用成功后，监听进入stopped状态。 停止监听会使访问中断，请谨慎操作。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StopLoadBalancerListener | 要执行的操作。 取值：StopLoadBalancerListener。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp13jaf5qli5xmgl**** | 负载均衡实例ID。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 标签键和值。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=StopLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xmgl****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <StopLoadBalancerListenerResponse> <RequestId>21D2B318-650E-4B0B-A3B5-693D462247B3</RequestId> </StopLoadBalancerListenerResponse> |  |

负载均衡 `JSON` 格式

```json
{
    "RequestId": "21D2B318-650E-4B0B-A3B5-693D462247B3"
}
```

#### 7.4.4. StartLoadBalancerListener

在调用该接口时，注意： 监听状态必须为stopped时，才可以调用该接口。 接口调用成功后，监听进入starting状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartLoadBalancerListener | 要执行的操作。 取值：StartLoadBalancerListener。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp13jaf5qli5**** | 负载均衡实例ID。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 标签键和值。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=StartLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <StartLoadBalancerListenerResponse> <RequestId>CC000321-00F2-49B8-9BCA-60D822414960</RequestId> </StartLoadBalancerListenerResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "CC000321-00F2-49B8-9BCA-60D822414960" } |  |

#### 7.4.5. SetLoadBalancerModificationProtection

调用SetLoadBalancerModificationProtection设置负载均衡实例的修改保护属性。

**前提条件**

您已安装v3.16.2r-slb-hotfeature-SP006。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetLoadBalancerModification Protection | 系统规定的参数： SetLoadBalancerModifyProtection。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08e***** | 负载均衡实例ID。 |

负载均衡

| ModificationProtectionStatus | String | 是 | ConsoleProtection | 负载均衡修改保护状态： NonProtection：不限制修改保护，设置后会清空之前设置的 ModificationProtectionReason 。 ConsoleProtection：实例控制台修改保护状态。 |
|---|---|---|---|---|
| LoadBalancerName | String | 否 | test1 | 传统型负载均衡实例的名称。 |
| accesskeyid _ _ | String | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | 否 | [{"tagKey":"Key1","tagValue" :"Value1"}] | 传统型负载均衡实例绑定的标签列表，其结构是一个JSON dictionary，包含标签键和标签值。 一次请求中，绑定的标签列表中最多支持10个标签。 |
| ModificationProtectionReason | String | 否 | 配置变更 | 设置修改保护状态的原因，长度为1~80个字符，必须以字母或中文开头，支持数字、英文句点（.）、下划线（_）和短划线（-）。 说明仅在 ModificationProtectionStatus 为ConsoleProtect ion时有效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 791D8B68-AE0F-4174-AF54- 088C8B3C5D54 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetLoadBalancerModificationProtection &LoadBalancerId=lb-bp1b6c719dfa08e***** &ModificationProtectionStatus=ConsoleProtection
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationUnsupported.SetLoadB alancerStatus | The zone of the loadBalancer does not support this operation. | 当前负载均衡实例不支持此操作。 |
| 400 | InvalidParam.ModificationProtecti onStatus | The param ModificationProtectionStatus is invalid. | 指定的ModificationProtectionStatus无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.ModificationProtecti onReason | The param ModificationProtectionReason is invalid. | 指定的ModificationProtectionReason无效。请检查参数约束，并在修改后重试。 |

#### 7.4.6. SetLoadBalancerDeleteProtection

调用SetLoadBalancerDeleteProtection设置实例删除保护状态。

**前提条件**

您已安装v3.16.2r-slb-hotfeature-SP006。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetLoadBalancerDeleteProte ction | 要执行的操作。 取值：SetLoadBalancerDeleteProtection。 |
| DeleteProtection | String | 是 | off | 是否开启负载均衡删除保护状态，取值： on：是。 off：否。 |

负载均衡

| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08e***** | 负载均衡实例的ID。 |
|---|---|---|---|---|
| LoadBalancerName | String | 否 | test1 | 传统型负载均衡实例的名称。 |
| accesskeyid _ _ | String | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | 否 | [{"tagKey":"Key1","tagValue" :"Value1"}] | 传统型负载均衡实例绑定的标签列表，其结构是一个JSON dictionary，包含标签键和标签值。一次请求中，绑定的标签列表中最多支持10个标签。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 791D8B68-AE0F-4174-AF54- 088C8B3C5D54 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetLoadBalancerDeleteProtection &DeleteProtection=off &LoadBalancerId=lb-bp1b6c719dfa08e*****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationUnsupported.DeletePro tectionForPrePayInstance | The operation failed because prepay instance does not support delete protection. | 操作失败，预付费负载均衡实例不支持开启删除保护。 |

#### 7.4.7. SwitchMasterSlaveServerGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | SwitchMasterSlaveServerGroup | 系统规定参数。取值： SwitchMasterSlaveServerGroup |
| AccessKeyId | String | Query | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| accesskeyid _ _ | String | Query | 否 | LTAI******************** | 阿里云颁发给用户的访问服务所用的密钥ID。 |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-east-hangzhou-01 | 传统型负载均衡实例的地域ID。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| LoadBalancerId | String | Query | 是 | lb-8vb86hxixo8lvsja8**** | 传统型负载均衡实例的ID。 |

| 开发指南·API参 | 考 |  |  |  | 负载均衡 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TargetServerGroup Id | String | Query | 是 | 1234567890 | 需要切换为工作服务器组的服务器组ID。 |
| ListenerProtocol | String | Query | 是 | https | 负载均衡实例前端使用的协议。 相同端口存在不同协议监听时，此字段必填。 |
| ListenerPort | Integer | Query | 是 | 443 | 监听端口。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SwitchMasterSlaveServerGroup &RegionId=cn-east-hangzhou-01 &LoadBalancerId=lb-8vb86hxixo8lvsja8**** &TargetServerGroupId=1234567890 &ListenerProtocol=https &ListenerPort=443
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ListenerNotSupportSuchAction | ListenerNotSupportSuchAction | The specified listener doesn't support such action for FailoverStrategy. |

#### 7.4.8. SetLoadBalancerListenerAttributeEx

用于修改负载均衡监听器的高级属性配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ListenerPort | Integer | Query | 是 | 443 | 监听端口。 |
| LoadBalancerId | String | Query | 是 | lb-8vb86hxixo8lvsja8**** | 传统型负载均衡实例的ID。 |
| Protocol | String | Query | 是 | https | 负载均衡实例前端使用的协议。 相同端口存在不同协议监听时，此字段必选。 |
| RegionId | String | Query | 是 | cn-east-hangzhou-01 | 传统型负载均衡实例的地域ID。 |
| KvAttribute | RepeatList | Query | 否 | role | 用户偏好的货币类型，如CNY、USD等 |
| -Key | String |  | 否 | TestKey | 资源的标签键。N的取值范围：1~20 。一旦输入该值，则不允许为空字符串。 最多支持64个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

| aliyun | acs: |
|---|---|
| http:// |  |

| 负载均衡 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -Value | String |  | 否 | TestValue | 资源的标签值。N的取值范围：1~20 。一旦输入该值，可以为空字符串。 最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

| aliyun |  |
|---|---|
|  | https:// |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetLoadBalancerListenerAttributeEx &ListenerPort=443 &LoadBalancerId=lb-8vb86hxixo8lvsja8**** &Protocol=https &RegionId=cn-east-hangzhou-01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AccessLogNotConfig | AccessLogNotConfig | Access log is not activated for specified instance. |
| 400 | InvalidParam.Procotol | InvalidParam.Protocol | The param protocol is invalid. |
| 400 | ParamDuplicateError.ListenerAttri buteEx | ParamDuplicateError.ListenerAttributeEx | The param is duplicate in request. |
| 400 | UnsupportedParam.Procotol | UnsupportedParam.Procotol | The specified protocol is not supported. |
| 400 | VipNotSupportConfig | VipNotSupportConfig | The vip does not support config. |
| 400 | ListenerNotExist | ListenerNotExist | The specified listener is not exist. Please check protocol and listener port, and try again. |
| 400 | InvalidParam.ListenerAttributeEx | InvalidParam.ListenerAttributeEx | The key of attribute is invalid. |
| 400 | InvalidParam.ListenerPort | InvalidParam.ListenerPort | The param listener port is invalid. |
| 400 | MissingParam.ListenerAttributeEx | MissingParam.ListenerAttributeEx | The KvAttribute is required. |
| 400 | InvalidParam.AccessLogTracingE nable | InvalidParam.AccessLogTracingEnable | The specified value of key AccessLogTracingEnable in KvAttribute is invalid. |
| 400 | InvalidParam.AccessLogTracingS ample | InvalidParameter.AccessLogTracingSample | The specified value of key AccessLogTracingSample in KvAttribute is invalid. |
| 400 | InvalidParam.AccessLogTracingTy pe | InvalidParameter.AccessLogTracingType | The specified value of key AccessLogTracingType in KvAttribute is invalid. |
| 400 | MissingParam.AccessLogTracingS ample | MissingParameter.AccessLogTracingSample | The key AccessLogTracingSample in KvAttribute is required. |
| 400 | MissingParam.AccessLogTracingT ype | MissingParameter.AccessLogTracingType | The key AccessLogTracingType in KvAttribute is required. |
| 400 | REGIONNOTSUPPORTPARAMET _ _ _ ER | InvalidParameter.RegionNotSupport | The region doesn't support the parameter: %s. |
| 400 | HDMonitorRegionalNotConfig | OperationNotAllowed.HighDefinitionMonitorNotEnabl ed | The operation is not allowed because HighDefinitionMonitor is not enabled in this region. |
| 400 | OperationDenied.MasterSlaveGro upModeDisabled | OperationDenied.MasterSlaveGroupModeDisabled | The operation is not allowed because of MasterSlaveGroupModeDisabled. |
| 400 | OperationDenied.MissingMasterSl aveGroupMonitor | OperationDenied.MissingMasterSlaveGroupMonitor | The operation is not allowed because of MissingMasterSlaveGroupMonitor. |
| 400 | HDMonitorQuotaExceed | HDMonitorQuotaExceed | The number of listeners with hdmonitor enabled exceeds the limit. |

负载均衡

#### 7.4.9. ModifyHighDefinationMonitor

修改高精度秒级监控的配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ModifyHighDefinationMonitor | 系统规定参数。取值： ModifyHighDefinationMonitor |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-east-hangzhou-01 | 传统型负载均衡实例的地域ID。 |
| LogProject | String | Query | 是 | my-project | 日志服务LogProject的名称。日志服务 LogProject的名称。长度为4~63个字符，支持数字、小写字母，可包含短划线（-），开头和结尾必须为数字或字母。 |
| LogStore | String | Query | 是 | my-log-store | 日志服务LogStore的名称。长度为2~64个字符，支持数字、小写字母，可包含短划线（-）和下划线（_），开头和结尾必须为数字或字母。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | String | true | 结果是否成功。 |
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyHighDefinationMonitor &RegionId=cn-east-hangzhou-01 &LogProject=my-project &LogStore=my-log-store
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984", "Success":"true" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | HDMONITORREGIONCONFIGE _ _ _ _ XISTED | OperationNotAllowed.HighDefinitionMonitorEnabled | The operation is not allowed because HighDefinationMonitor is already enabled in this region. |
| 400 | UnsupportedFeature.User | UnsupportedFeature.User | The feature of HighDefinationMonitor is not supported. |
| 400 | NoPermission.AliyunServiceRoleF orSlbLogDelivery | NoPermission.AliyunServiceRoleForSlbLogDelivery | You are not authorized to create the service linked role. Role Name: AliyunServiceRoleForSlbLogDelivery. Service Name: logdelivery.slb.aliyuncs.com. Please ensure the user has been granted the ram:CreateServiceLinkedRole permission |

| 负载均衡 |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | HdMonitorVipExist | OperationDenied.HdMonitorListenerExist | The operation is denied because there are still listeners enabling HighDefinationMonitor. |
| 400 | HDMonitorRegionalNotConfig | OperationNotAllowed.HighDefinitionMonitorNotEnabl ed | The operation is not allowed because HighDefinationMonitor is not enabled in this region. |

#### 7.4.10. EnableHighDefinationMonitor

开启实例的秒级监控

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | EnableHighDefinationMonitor | 系统规定参数。取值： EnableHighDefinationMonitor |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| Tags | String | Query | 否 | [{"tagKey":"Key1","tagValue":"Value1"}] | 传统型负载均衡实例绑定的标签列表，其结构是一个JSON dictionary，包含标签键和标签值。 一次请求中，绑定的标签列表中最多支持10个标签。 |
| RegionId | String | Query | 是 | cn-east-hangzhou-01 | 传统型负载均衡实例的地域ID。 |
| LogProject | String | Query | 是 | my-project | 日志服务LogProject的名称。日志服务 LogProject的名称。长度为4~63个字符，支持数字、小写字母，可包含短划线（-），开头和结尾必须为数字或字母。 |
| LogStore | String | Query | 是 | my-log-store | 日志服务LogStore的名称。长度为2~64个字符，支持数字、小写字母，可包含短划线（-）和下划线（_），开头和结尾必须为数字或字母。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | String | true | 结果是否成功。 |
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=EnableHighDefinationMonitor &RegionId=cn-east-hangzhou-01 &LogProject=my-project &LogStore=my-log-store
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984", "Success":"true" } |  |

**错误码**

负载均衡

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | HDMONITORREGIONCONFIGE _ _ _ _ XISTED | OperationNotAllowed.HighDefinitionMonitorEnabled | The operation is not allowed because HighDefinationMonitor is already enabled in this region. |
| 400 | UnsupportedFeature.User | UnsupportedFeature.User | The feature of HighDefinationMonitor is not supported. |
| 400 | NoPermission.AliyunServiceRoleF orSlbLogDelivery | NoPermission.AliyunServiceRoleForSlbLogDelivery | You are not authorized to create the service linked role. Role Name: AliyunServiceRoleForSlbLogDelivery. Service Name: logdelivery.slb.aliyuncs.com. Please ensure the user has been granted the ram:CreateServiceLinkedRole permission |

#### 7.4.11. CreateLoadBalancer

在使用该接口创建实例时，请注意： 实例创建前，请调用 `DescribeAvailableResource` 查询可用区支持的资源售卖情况。 实例创建后，会产生费用。 如果不指定实例规格**LoadBalancerSpec**，则创建性能共享型实例。建议在创建负载均衡实例时，通过规格参数**LoadBalancerSpec**指定实例的规格。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateLoadBalancer | 系统规定的参数。取值：CreateLoadBalancer。 |
| RegionId | String | 是 | cn-qingdao-env66-b01 | 负载均衡实例所在的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AddressType | String | 否 | internet | 负载均衡实例的网络类型。取值： internet：创建公网负载均衡实例后，系统会分配一个公网IP地址，可以转发公网请求。 intranet：创建内网负载均衡实例后，系统会分配一个内网IP地址，仅可转发内网请求。 |
| InternetChargeType | String | 否 | paybytraffic | 公网类型实例的付费方式。取值： paybybandwidth：按带宽计费。 paybytraffic（默认值）：按流量计费。 paybytraffic：按流量计费。 |
| Bandwidth | Integer | 否 | 10 | 监听的带宽峰值，单位Mbps。取值： -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为- 1，即不限制带宽峰值。 1~5120 ： 对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。更多信息，请参见共享实例带宽 。 |
| ClientToken | String | 否 | 5A2CFF0E-5718-45B5-9D4D- 70B3FF3898 | 用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一，最大不超过64个ASCII字符。 说明若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId可能不一样。 |
| LoadBalancerName | String | 否 | lb-bp1o94dp5i6ea**** | 负载均衡实例的名称。 长度为1~80个英文或中文字符，必须以大小字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-）。 不指定该参数时，默认由系统分配一个实例名称。 |
| VpcId | String | 否 | vpc-bp1aevy8sofi8mh1***** | 负载均衡实例所属的VPC ID。 |
| VSwitchId | String | 否 | vsw-bp12mw1f8k3jgy***** | 专有网络实例所属的交换机ID。 创建专有网络类型的负载均衡实例，必须指定该参数。如果指定了该参数，AddessType参数的值默认被设置为intranet。 |
| MasterZoneId | String | 否 | cn-qingdao-b | 负载均衡实例的主可用区ID。 您可以通过调用 DescribeZone 接口查看相应地域下的主备可用区信息。 |

负载均衡

| SlaveZoneId | String | 否 | cn-qingdao-d | 负载均衡实例的备可用区ID。 您可以通过调用 DescribeZone 接口查看相应地域下的主备可用区信息。 |
|---|---|---|---|---|
| accesskeyid _ _ | String | 否 | acc-nacl- hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | 否 | [{"tagKey":"Key1","tagValue" :"Value1"}] | 负载均衡实例绑定的标签列表。 |
| EnableVpcVipFlow | String | 否 | 1 | 流日志。 |
| LoadBalancerSpec | String | 否 | slb.s2.small | 负载均衡实例的规格。取值： slb.s1.small slb.s2.small slb.s3.small slb.s2.medium slb.s3.medium slb.s3.large 说明若不指定规格，则创建性能共享型实例。目前，共享型实例已停止售卖，请指定实例规格。 |
| AddressIPVersion | String | 否 | ipv4 | 负载均衡实例的IP版本，取值：ipv4或ipv6。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LoadBalancerId | String | lb-hddhfjg******* | 负载均衡实例ID。 |
| Address | String | 42.250.**.** | 分配的负载均衡实例IP地址。 |
| VpcId | String | vpc-25dvzy9***** | 负载均衡实例所属专有网络的ID。 |
| VSwitchId | String | vsw-255ecr*** | 负载均衡实例所属交换机的ID。 |
| LoadBalancerName | String | lb-bp1o94dp5i6ea**** | 负载均衡实例名称。 |
| AddressIPVersion | String | ipv4 | 负载均衡实例的IP地址类型。 |
| NetworkType | String | classic | 负载均衡实例的网络类型。取值： vpc：专有网络实例 classic：经典网络实例 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateLoadBalancer &RegionId=cn-qingdao-env66-b01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateLoadBalancerResponse> <NetworkType>vpc</NetworkType> <LoadBalancerName>lb-bp1o94dp5i6ea****</LoadBalancerName> <Address>192.168.0.**</Address> <ResourceGroupId>rg-acfmxazb***</ResourceGroupId> <RequestId>AB197CF0-D9E9-4475-A89D-35DBCCF13BBE</RequestId> <AddressIPVersion>ipv4</AddressIPVersion> <LoadBalancerId>lb-bp1b6c719dfa0***</LoadBalancerId> <VSwitchId>vsw-bp12mw1f8k3jgygk9****</VSwitchId> <VpcId>vpc-bp1aevy8sofi8mh1q***</VpcId> </CreateLoadBalancerResponse> |  |

`JSON` 格式负载均衡

```json
{
    "LoadBalancerName": "lb-bp1o94dp5i6ea****",
    "VpcId": "vpc-25dvzy9*****",
    "Address": "42.250.**.**",
    "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
    "NetworkType": "classic",
    "AddressIPVersion": "ipv4",
    "VSwitchId": "vsw-255ecr***",
    "LoadBalancerId": "lb-hddhfjg*******"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationFailed.ZoneResourceLi mit | The operation failed because of resource limit of the specified zone. | 操作失败，原因是当前可用区资源不足。 |
| 400 | OperationFailed.RegionResourceL imit | The operation failed because of resource limit of the specified region. | 操作失败，原因是指定地域资源不足。 |
| 400 | Operation.NotAllowed | Operation Denied. The charge type of internet prepay instance can only be paybybandwidth. | 操作被拒绝，原因是公网预付费实例只支持按带宽计费。 |
| 400 | Operation.NotAllowed | Operation Denied. The charge type of intranet prepay instance can only be paybytraffic. | 操作被拒绝，原因是私网预付费实例只支持按流量计费。 |
| 400 | OperationFailed.UnpaidBillsExist | The account has unpaid bills. Please pay your overdue bill first. | 操作失败，原因是当前帐户下存在未支付帐单。 请先支付您的逾期账单。 |
| 400 | RegionOrZonesNotSupportIpv6 | The specified region or master/slave zones does not support ipv6. | 指定地域或主备可用区不支持Ipv6。 |
| 400 | InvalidParameter.Mismatch | AddressType and IpVersion is conflict, IPv6 does not support intranet instance. | 网络类型和IP版本冲突，私网实例不支持IPv6。 |
| 400 | HighRiskOperationDenied | The operation is denied because of high risk. | 操作被拒绝，原因是当前操作为高危操作。 |
| 400 | VSwitchAvailableIpNotExist | The specified VSwitch has no availabe ip. | 指定的交换机没有可用的Ip。 |
| 400 | VSwitchNotExist | The specified VSwitch does not exist. | 指定的交换机不存在。 |
| 400 | InvalidParameter | Illegal parameter. The IP address is not in subnet. | 参数非法，IP地址不在子网中。 |
| 400 | Instance.ShareSlbNotSupportPay 95 | Illegal parameter. The share instance not support PayBy95 or PayByOld95. | 共享型实例不支持PayBy95或PayByOld95。 |
| 400 | Instance.Pay95RateInvalid | Illegal parameter. The rate is illegal. | 指定的Rate无效。请检查参数约束，并在修改后重试。 |
| 400 | Instance.Pay95BandwidthIllegal | Illegal parameter. The bandwidth is illegal. | 指定的Bandwidth无效。请检查参数约束，并在修改后重试。 |
| 400 | Instance.InternetChargeTypeNot Allowed | Illegal parameter. The specified InternetChargeType not allowed. | 参数非法，指定的InternetChargeType不支持。 |
| 400 | OperationFailed.TokenIsProcessin g | The operation is failed, because the Client Token is processing. | 操作失败，原因是当前请求正在处理中。 |
| 400 | MissingParam.VSwitchId | The parameter VSwitchId is required. | 参数VSwitchId缺失。 |
| 400 | InvalidVpcId.NotExist | The specified VPC not exist. | 指定的VPC不存在。 |
| 400 | InvalidParameter.CloudType | The specified CloudType is invalid. | 指定的CloudType无效。请检查参数约束，并在修改后重试。 |
| 400 | OperationFailed.InvalidAccount | The account information is incomplete. | 操作失败，原因是账户信息不完整。 |
| 400 | RegionOrZonesNotSupportCEN | The specified region or master/slave zones does not support cloudType of hybridcen. _ | 指定的地域或主备可用区不支持CEN。 |
| 400 | MissingParam.LoadBalancerSpec | The param LoadBalancerSpec is required. | 参数LoadBalancerSpec缺失。 |
| 400 | InvalidParameter.Bandwidth | The param Bandwidth is invalid. | 指定的Bandwidth无效。请检查参数约束，并在修改后重试。 |
| 400 | OperationForbidden.AccountRisk Reject | The operation failed because of account risk reject. | 操作失败，原因是当前账户已被风控。 |
| 400 | OperationForbidden.QuotaLimit | The operation failed because of quota limit of shared loadbalancers. | 操作失败，原因是共享性实例数量已达配额上限。 |
| 400 | InvalidParam.ModificationProtecti onStatus | The param ModificationProtectionStatus is invalid. | 指定的ModificationProtectionStatus无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.ModificationProtecti onReason | The param ModificationProtectionReason is invalid. | 指定的ModificationProtectionReason无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.ModificationProtecti onReason | %s. | 指定的ModificationProtectionReason无效。请检查参数约束，并在修改后重试。 |
| 400 | ShareSlbHaltSales | The share instance has been discontinued. | 共享型负载均衡实例已售罄。 |
| 400 | OperationFailed.CashBookInsuffic ient | No payment method is specified for your account, We recommend that you add a payment method or maintain a prepayment balance. | 操作失败，原因是您的帐户未指定付款方式，我们建议您添加付款方式或保持预付款余额。 |

负载均衡

| 400 | OperationFailed.OnlyInnerCommo ditySupportToPurchase | AliCroup2Cloud user only can buy inner commodity. | 操作失败，原因是集团上云用户只能购买内部商品。 |
|---|---|---|---|
| 400 | OperationFailed.InvokeLingXiaoF ailed | Failed to invoke lingxiao service. | 操作失败，原因是调用凌霄服务失败。 |
| 503 | SDK.ServerUnreachable | Service is unreachable. | 暂时无法访问服务，请稍后重试。 |
| 400 | AllocateVpcInstanceFailed | Failed to allocate vpc instance. | 分配vpc实例失败。 |
| 400 | QueryCreditCtrlInfoFailed | Failed to query credit ctrl info. | 查询用户信息失败。 |
| 400 | QueryCommodityCenterFailed | Failed to query commodity center. | 商品中心查询失败。 |
| 400 | RegionNotSupportParameter | Current region does not support the param of %s. | 当前地域不支持指定参数。 |
| 400 | QueryAccountBookInfoFailed | Failed to invoke account book info. | 调用账本信息失败。 |
| 400 | RateAccountFailed | Failed to rate account for pricing. | 调用定价服务失败。 |
| 400 | TradeWaitDistributorAudit | The trade needs distributor to audit. | 此次交易待经销商审核。 |
| 400 | OperationFailed.InvokeProxyFaile d | Failed to invoke proxy. | 操作失败，原因是调用管控失败。 |
| 400 | QueryAccountCompleteProgressF ailed | Failed to query account progress. | 查询账户进度失败。 |
| 400 | QueryVoucherInfoFailed | Failed to query voucher info. | 查询凭证信息失败。 |
| 400 | InvalidVSwitchId.NotFound | The specified vSwitch instance is invalid. | 非法的vswitch实例。 |
| 400 | IllegalParam.SpecType | The param of SpecType is illegal. | 指定的SpecType无效。请检查参数约束，并在修改后重试。 |
| 400 | MissingParam.SpecType | The param of SpecType is missing. | 参数SpecType缺失。 |
| 400 | UnsupportedRegion | The feature is not supported in current region. | 当前地域不支持该功能。 |

#### 7.4.12. DeleteLoadBalancer

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteLoadBalancer | 要执行的操作。 取值：DeleteLoadBalancer。 |
| LoadBalancerId | String | 是 | lb-bp1h66tp5uat8**** | 负载均衡实例的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

如果删除的实例开启了删除保护，系统会报以下错误： JSON格式

```json
    {
 "RequestId": "7B7AB375-1EA6-4A18-9D1C-F258F2D57638",
 "HostId": "slb.aliyuncs.com",
 "Code": "OperationDenied.DeleteProtectionIsOn",
 "Message": "The loadbalancer can't be deleted due to DeleteProtection is enabled."
     }
```

XML格式

```xml
   <?xml version="1.0" encoding="UTF-8" ?>
        <DeleteLoadBabalancerResponse>
 <RequestId>7B7AB375-1EA6-4A18-9D1C-F258F2D57638</RequestId>
 <HostId>slb.aliyuncs.com</HostId>
 <Code>OperationDenied.DeleteProtectionIsOn</Code>
 <Message>The loadbalancer can't be deleted due to DeleteProtection is enabled.</Message>
       </DeleteLoadBabalancerResponse>
```

**示例**

负载均衡请求示例

```
http(s)://[Endpoint]/?Action=DeleteLoadBalancer &LoadBalancerId=lb-bp1h66tp5uat8********
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteLoadBabalancerResponse> <RequestId>E3F602B8-A162-4683-A7EC-49364E597259</RequestId> </DeleteLoadBabalancerResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "0D9B7343-AC1F-498C-A18A-78FE14A7C3A3" } |  |

#### 7.4.13. ModifyLoadBalancerInstanceSpec

调用ModifyLoadBalancerInstanceSpec修改负载均衡的实例规格。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyLoadBalancerInstance Spec | 系统规定的参数。取值：ModifyLoadBalancerInstanceSpec。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719df**** | 负载均衡实例ID。 |
| LoadBalancerSpec | String | 是 | slb.s1.small | 负载均衡实例的规格。取值： slb.s1.small slb.s2.small slb.s3.small slb.s2.medium slb.s3.medium slb.s3.large 每个地域支持的规格不同。 说明将共享型实例变更为保障型实例，SLB将有小概率可能性出现短暂的业务中断（10~30秒），建议您在业务低谷期进行变配，或者使用DNS将业务调度至其他的SLB实例后，再进行变配操作。 |
| accesskeyid _ _ | String | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 负载均衡实例绑定的标签列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyLoadBalancerInstanceSpec &LoadBalancerId=lb-bp1b6c719df**** &LoadBalancerSpec=slb.s2.small
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyLoadBalancerInstanceSpecResponse> <RequestId>D456A34A-6E40-4379-8DAF-9175760FE215</RequestId> </ModifyLoadBalancerInstanceSpecResponse> |  |

`JSON` 格式负载均衡

```json
{
    "ModifyLoadBalancerInstanceSpecResponse": {
        "RequestId": "D456A34A-6E40-4379-8DAF-9175760FE215"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ModifySpecNotAllowed | LoadBalancerSpec not allowed for this instance | 该负责均衡不支持这种实例规格。 |
| 400 | Operation.NotAllowed | Operation Denied, Your account does not have enough balance. | 操作被拒绝，原因是账户余额不足。 |
| 400 | Operation.NotAllowed | Operation Denied. Unfinished order exists. | 操作被拒绝，原因是存在未完成的订单。 |
| 400 | Operation.NotAllowed | Operation Denied. Unfinished purchase exists. | 不允许该操作，存在未完成的购买订单。 |
| 400 | Operation.NotAllowed | Operation Denied. Prepay instance only permitted to increase loadBalancerSpec. | 操作被拒绝，原因是预付费实例只允许提升规格。 |
| 400 | Operation.NotAllowed | Operation Denied. The Purchase status of the instance is not valid. | 操作被拒绝，原因是负载均衡实例下单参数非法。 |
| 400 | InvalidParameter.Bandwidth | The param Bandwidth is invalid. | 指定的Bandwidth无效。请检查参数约束，并在修改后重试。 |
| 400 | ChangeLbSpecNotAllowed | You cannot change the specification for the specified load balancer. | 指定的实例不支持修改规格。 |

#### 7.4.14. ModifyLoadBalancerInternetSpec

调用ModifyLoadBalancerInternetSpec修改公网负载均衡实例的计费方式。 调整按带宽计费实例的带宽峰值，修改完成后，立即生效。 从按流量计费转换为按带宽计费。计费类型的变更从第二天凌晨开始生效。 从按带宽计费转换为按流量计费。计费类型的变更从第二天凌晨开始生效。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyLoadBalancerInternetS pec | 要执行的操作。 取值：ModifyLoadBalancerInternetSpec。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08ex**** | 负载均衡实例的ID。 |
| Bandwidth | Integer | 否 | 10 | 按固定带宽计费方式的公网类型实例的带宽峰值。单位Mbps。 取值：1~5000（各地域的带宽峰值会有不同）。 说明按流量计费的实例不需要指定该参数 （即InternetChargeType为paybytraffic）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyLoadBalancerInternetSpec &LoadBalancerId=lb-bp1b6c719dfa08ex****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyLoadBalancerInternetSpecResponse> <RequestId>E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED</RequestId> </ModifyLoadBalancerInternetSpecResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED" } |  |

负载均衡

#### 7.4.15. SetLoadBalancerName

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetLoadBalancerName | 要执行的操作。 取值：SetLoadBalancerName。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08e**** | 负载均衡实例ID。 |
| LoadBalancerName | String | 是 | lb-instance-test | 负载均衡实例的名称。 长度为2~128个英文或中文字符，可包含数字、英文句点（.）、下划线（_）和短划线（-）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetLoadBalancerName &LoadBalancerId=lb-bp1b6c719dfa08e**** &LoadBalancerName=abc1
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetLoadBalancerStatusResponse> <RequestId>3C7F675E-9F82-4806-BA47-FF57E3ACC850</RequestId> </SetLoadBalancerStatusResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "3C7F675E-9F82-4806-BA47-FF57E3ACC850" } |  |

#### 7.4.16. SetLoadBalancerStatus

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetLoadBalancerStatus | 要执行的操作。 取值：SetLoadBalancerStatus。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08e**** | 负载均衡实例的ID。 |
| LoadBalancerStatus | String | 是 | active | 负载均衡实例状态。取值：active或inactive。 active（默认值） 当负载均衡实例的状态为active时，实例中的监听可以根据规则转发接收的流量。 inactive 当负载均衡实例的状态为inactive时，实例中的监听不会再转发接收的流量。 说明当一个实例下的所有监听都被删除后，实例状态会被自动改为inactive。 |
| accesskeyid _ _ | String | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 标签键和值。 |

**返回数据**

负载均衡

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetLoadBalancerStatus &LoadBalancerId=lb-bp1b6c719dfa08e****** &LoadBalancerStatus=active
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetLoadBalancerStatusResponse> <RequestId>E6DDFE22-F019-4F34-B8DD-FD14973450A6</RequestId> </SetLoadBalancerStatusResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "E6DDFE22-F019-4F34-B8DD-FD14973450A6" } |  |

#### 7.4.17. DescribeLoadBalancerAttribute

调用DescribeLoadBalancerAttribute查询指定负载均衡实例的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLoadBalancerAttribu te | 要执行的操作。 取值：DescribeLoadBalancerAttribute。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08ex**** | 负载均衡实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LoadBalancerId | String | lb-dhhd**** | 负载均衡实例ID。 |
| RegionId | String | cn-qingdao-env17-d01 | 负载均衡实例所在地域ID。 |
| RegionIdAlias | String | cn-qingdao-env17-d01 | 负载均衡实例所属的地域别名。 |
| LoadBalancerName | String | abc | 负载均衡实例的名称。 |
| LoadBalancerStatus | String | active | 负载均衡实例状态： inactive：实例已停止，此状态的实例监听不会再转发流量。 active：实例运行中，实例创建后，默认状态为active。 locked：实例已锁定，实例已经欠费或被阿里云锁定。 |
| Address | String | 42.XX.XX.6 | 负载均衡实例的服务地址。 |
| AddressType | String | internet | 负载均衡实例的地址类型。 |
| NetworkType | String | vpc | 负载均衡实例的网络类型。 |
| VpcId | String | vpc-25dvzy9f8**** | 私网负载均衡实例的专有网络ID。 |
| Bandwidth | Integer | 5 | 按带宽计费的公网型实例的带宽峰值。 |
| CreateTime | String | 2017-08-31T02:49:05Z | 负载均衡实例的创建时间。 |
| ListenerPorts | List | 80 | 负载均衡实例前端使用的端口列表。 |

负载均衡

| ListenerPortsAndProtocol | Array of ListenerPortAndProtocol |  | 负载均衡实例前端使用的端口和协议列表。 |
|---|---|---|---|
| ListenerPortAndProtocol |  |  |  |
| ListenerPort | Integer | 443 | 负载均衡实例前端使用的端口。 |
| ListenerProtocol | String | https | 负载均衡实例前端使用的协议。 |
| BackendServers | Array of BackendServer |  | 负载均衡实例的后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | i-djghr2**** | 后端服务器实例ID。 |
| Weight | Integer | 90 | 后端服务器的权重。 |
| ServerIp | String | 192.168.0.1 | 后端服务器IP。 |
| Type | String | ecs | 后端服务器类型。 |
| MasterZoneId | String | cn-hangzhou-b | 负载均衡实例的主可用区ID。 |
| AutoReleaseTime | Long | 1513947075 | 释放时间的时间戳。 |
| CreateTimeStamp | Long | 1504147745000 | 负载均衡实例创建时间戳。 |
| EndTime | String | 2999-09-08T16:00:00Z | 负载均衡实例结束时间。 |
| EndTimeStamp | Long | 32493801600000 | 负载均衡实例结束时间戳。 |
| InternetChargeType | String | paybybandwidth | 公网类型实例付费方式。 取值：paybybandwidth或paybytraffic。 paybybandwidth：按带宽计费。 paybytraffic：按流量计费（默认值）。 |
| ListenerPortsAndProtocal | Array of ListenerPortAndProtocal |  | 监听端口和协议。 |
| ListenerPortAndProtocal |  |  |  |
| ListenerPort | Integer | 443 | 负载均衡实例前端使用的端口。 |
| ListenerProtocal | String | http | 负载均衡实例前端使用的协议。 |
| LoadBalancerSpec | String | slb.s2.small | 负载均衡实例的的性能规格。 |
| PayType | String | PrePay | 负载均衡实例付费类型，取值PayOnDemand或者PrePay。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |
| SlaveZoneId | String | cn-hangzhou-d | 负载均衡实例的备可用区ID。 |
| VSwitchId | String | vsw-255ecrwq5**** | 私网负载均衡实例的交换机ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerAttribute &LoadBalancerId=lb-bp1b6c719dfa08ex****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式负载均衡

```xml
      <CreateTimeStamp>1541679713000</CreateTimeStamp>
   <RegionIdAlias>cn-hangzhou</RegionIdAlias>
   <BackendServers>
      <BackendServer>
         <ServerId>i-bp1c3zrr37ablp8ujo7v</ServerId>
         <Weight>100</Weight>
         <Type>ecs</Type>
      </BackendServer>
   </BackendServers>
   <HasReservedInfo>false</HasReservedInfo>
   <ListenerPorts></ListenerPorts>
   <InternetChargeType>paybytraffic</InternetChargeType>
   <VSwitchId>vsw-bp12mw1f8k3*********</VSwitchId>
   <VpcId>vpc-bp1aevy8sofi8mh*****</VpcId>
   <SlaveZoneId>cn-hangzhou-d</SlaveZoneId>
   <LoadBalancerSpec>slb.s2.small</LoadBalancerSpec>
   <NetworkType>vpc</NetworkType>
   <ListenerPortsAndProtocol></ListenerPortsAndProtocol>
   <PayType>PayOnDemand</PayType>
   <Bandwidth>5120</Bandwidth>
   <LoadBalancerName>abc1</LoadBalancerName>
   <ResourceGroupId>rg-acfmxazb4p*****</ResourceGroupId>
   <AddressIPVersion>ipv4</AddressIPVersion>
   <LoadBalancerId>lb-bp1b6c719dfa08e*****</LoadBalancerId>
   <EndTimeStamp>32493801600000</EndTimeStamp>
   <MasterZoneId>cn-hangzhou-b</MasterZoneId>
   <ListenerPortsAndProtocal></ListenerPortsAndProtocal>
   <Address>192.168.0.1</Address>
   <RegionId>cn-hangzhou</RegionId>
   <RequestId>35D745B3-1567-4855-9EF1-F5CED3C1670C</RequestId>
   <CreateTime>2018-11-08T12:21:53Z</CreateTime>
   <AddressType>intranet</AddressType>
   <EndTime>2999-09-08T16:00:00Z</EndTime>
   <LoadBalancerStatus>active</LoadBalancerStatus>
```

| JSON | 格式 |
|---|---|
| { "CreateTimeStamp": 1541679713000, "RegionIdAlias": "cn-hangzhou", "BackendServers": { "BackendServer": [ { "ServerId": "i-bp1c3zrr37ab*****", "Weight": 100, "Type": "ecs" } ] }, "HasReservedInfo": "false", "ListenerPorts": { "ListenerPort": [ ] }, "InternetChargeType": "paybytraffic", "VSwitchId": "vsw-bp12mw1f8k******", "VpcId": "vpc-bp1aevy8sofi8mh******", "SlaveZoneId": "cn-hangzhou-d", "LoadBalancerSpec": "slb.s2.small", "NetworkType": "vpc", "ListenerPortsAndProtocol": { "ListenerPortAndProtocol": [ ] }, "PayType": "PayOnDemand", "Bandwidth": 5120, "LoadBalancerName": "abc1", "ResourceGroupId": "rg-acfmxazb*****", "AddressIPVersion": "ipv4", "LoadBalancerId": "lb-bp1b6c719dfa08*****", "EndTimeStamp": 32493801600000, "MasterZoneId": "cn-hangzhou-b", "ListenerPortsAndProtocal": { "ListenerPortAndProtocal": [ ] }, "Address": "192.168.0.1", "RegionId": "cn-hangzhou", "RequestId": "35D745B3-1567-4855-9EF1-F5CED3C1670C", "CreateTime": "2018-11-08T12:21:53Z", "AddressType": "intranet", "EndTime": "2999-09-08T16:00:00Z", "LoadBalancerStatus": "active" } |  |

负载均衡

#### 7.4.18. DescribeLoadBalancers

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLoadBalancers | 要执行的操作。 取值：DescribeLoadBalancers。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 您可以从地域和可用区列表或通过调用DescribeRegions接口查询地域 ID。 |
| ServerId | String | 否 | vm-23**** | 添加的后端服务器ID。 |
| LoadBalancerId | String | 否 | lb-bp1b6c719dfa**** | 负载均衡实例ID。 支持多值查询，最多可输入10个ID，以半角逗号（,）分隔。 |
| LoadBalancerName | String | 否 | abc1 | 负载均衡实例名称。 支持多值查询，最多可输入10个名称，以半角逗号（,）分隔。 |
| ServerIntranetAddress | String | 否 | 10.XX.XX.6 | 添加的后端服务器的内网地址。 支持多值查询，以半角逗号（,）分隔。 |
| AddressType | String | 否 | intranet | 负载均衡实例的网络类型。 取值：intranet或internet。 internet：创建公网负载均衡实例后，系统会分配一个公网IP地址，可以转发公网请求。 intranet：创建内网负载均衡实例后，系统会分配一个内网IP地址，仅可转发内网请求。 |
| InternetChargeType | String | 否 | paybybandwidth | 公网类型实例付费方式。 取值：paybybandwidth或paybytraffic。 paybybandwidth：按带宽计费。 paybytraffic：按流量计费 。 说明如果不指定该参数，则表示保持原有的计费方式。 |
| VpcId | String | 否 | vpc-bp1aevy8sof**** | 负载均衡实例所属的VPC ID。 |
| VSwitchId | String | 否 | vsw-bp12mw1f8k3**** | 负载均衡实例所属的交换机ID。 |
| NetworkType | String | 否 | vpc | 私网负载均衡实例的网络类型，取值：vpc或classic。 vpc：专有网络实例。 classic：经典网络实例。 |
| Address | String | 否 | 192.168.0.1 | 负载均衡实例的服务地址。 |
| MasterZoneId | String | 否 | cn-hangzhou-b | 负载均衡实例的主可用区ID。 |
| SlaveZoneId | String | 否 | cn-hangzhou-d | 负载均衡实例的备可用区ID。 目前对金融云用户暂时不支持多可用区功能。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 负载均衡实例绑定的标签列表，其结构是一个json dictionary，包含 TagKey和TagValue。 一次请求中，标签列表中最多支持10个元素。 |
| PayType | String | 否 | PayOnDemand | 负载均衡实例付费类型。 取值：PayOnDemand或PrePay。 PayOnDemand：按量付费。 PrePay：包年包月。 |

负载均衡

| AddressIPVersion | String | 否 | ipv4 | IP版本，可以设置为ipv4或ipv6。 说明目前支持创建IPv6实例且实例类型必须为性能保障型实例的可用区如下： 华东1地域的E和F可用区、华北2地域的F和G可用区、华东3地域的D和 E可用区、华北3地域的A和B两个可用区和华南1地域的D和E可用区。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LoadBalancers | Array of LoadBalancer |  | 数组格式，返回负载均衡实例列表。 |
| LoadBalancer |  |  |  |
| LoadBalancerId | String | lb-hjfng**** | 负载均衡实例ID。 |
| LoadBalancerName | String | def | 负载均衡实例的名称。 |
| LoadBalancerStatus | String | active | 负载均衡实例状态： inactive: 此状态的实例监听不会再转发流量。 active: 实例创建后，默认状态为active。 locked: 实例已经被锁定。 |
| Address | String | 100.XX.XX.28 | 负载均衡实例服务地址。 |
| RegionId | String | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |
| RegionIdAlias | String | cn-qingdao-env17-d01 | 负载均衡实例的地域名称。 |
| AddressType | String | intranet | 负载均衡实例的网络类型。 |
| VSwitchId | String | vsw-255ecr**** | 私网负载均衡实例的交换机ID。 |
| VpcId | String | vpc-25dvzy9f8**** | 私网负载均衡实例的专有网络ID。 |
| NetworkType | String | vpc | 私网负载均衡实例的网络类型，取值： vpc：专有网络实例。 classic：经典网络实例。 |
| CreateTime | String | 2017-08-31T02:49:05Z | 负载均衡实例创建时间。 |
| MasterZoneId | String | cn-hangzhou-b | 实例的主可用区ID。 |
| SlaveZoneId | String | cn-hangzhou-d | 实例的备可用区ID。 |
| AddressIPVersion | String | ipv4 | IP版本，可以设置为ipv4或者ipv6。 |
| CreateTimeStamp | Long | 1504147745000 | 负载均衡实例创建时间戳。 |
| InternetChargeType | String | paybybandwidth | 公网实例的计费方式。取值： paybybandwidth，按带宽计费。 paybytraffic，按流量计费（默认值）。 说明当PayType参数的值为PrePay时，只支持按带宽计费。 |
| PayType | String | PrePay | 负载均衡实例付费类型，取值：PayOnDemand或PrePay。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancers &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例负载均衡

| XML | 格式 |
|---|---|
| <DescribeLoadBalancersResponse> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> <PageSize>50</PageSize> <LoadBalancers> <LoadBalancer> <CreateTimeStamp>1541679713000</CreateTimeStamp> <LoadBalancerName>abc1</LoadBalancerName> <RegionIdAlias>cn-hangzhou</RegionIdAlias> <ResourceGroupId>rg-acfmxaz*******y</ResourceGroupId> <AddressIPVersion>ipv4</AddressIPVersion> <LoadBalancerId>lb-bp1b6c********fuca5</LoadBalancerId> <VSwitchId>vsw-bp12mw1f********bmlj</VSwitchId> <InternetChargeType>4</InternetChargeType> <VpcId>vpc-bp1aevy8*********5cm</VpcId> <SlaveZoneId>cn-hangzhou-d</SlaveZoneId> <NetworkType>vpc</NetworkType> <MasterZoneId>cn-hangzhou-b</MasterZoneId> <CreateTime>2018-11-08T20:21Z</CreateTime> <Address>192.168.0.**</Address> <RegionId>cn-hangzhou</RegionId> <AddressType>intranet</AddressType> <PayType>PayOnDemand</PayType> <LoadBalancerStatus>active</LoadBalancerStatus> </LoadBalancer> </LoadBalancers> <RequestId>1C7445CB-C21C-4C19-9A3C-65C3190D1944</RequestId> </DescribeLoadBalancersResponse> |  |

| JSON | 格式 |
|---|---|
| { "DescribeLoadBalancersResponse": { "PageNumber": 1, "TotalCount": 1, "PageSize": 50, "LoadBalancers": { "LoadBalancer": { "CreateTimeStamp": 1541679713000, "LoadBalancerName": "abc1", "RegionIdAlias": "cn-hangzhou", "ResourceGroupId": "rg-acfmxaz*******y", "AddressIPVersion": "ipv4", "LoadBalancerId": "lb-bp1b6c********fuca5", "VSwitchId": "vsw-bp12mw1f********bmlj", "InternetChargeType": 4, "VpcId": "vpc-bp1aevy8*********5cm", "SlaveZoneId": "cn-hangzhou-d", "NetworkType": "vpc", "MasterZoneId": "cn-hangzhou-b", "CreateTime": "2018-11-08T20:21Z", "Address": "192.168.0.**", "RegionId": "cn-hangzhou", "AddressType": "intranet", "PayType": "PayOnDemand", "LoadBalancerStatus": "active" } }, "RequestId": "1C7445CB-C21C-4C19-9A3C-65C3190D1944" } } |  |

#### 7.4.19. DescribeRegions

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRegions | 要执行的操作。 取值：DescribeRegions。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Regions | Array of Region |  | 地域列表。 |
| Region |  |  |  |

负载均衡

| RegionId | String | cn-qingdao-env17-d01 | 地域ID。 |
|---|---|---|---|
| LocalName | String | 华北1（青岛） | 地域名称。 |
| RequestId | String | 1651FBB6-4FBF-49FF-A9F5- DF5D696C7EC6 | 请求ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RequestId>1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6</RequestId> <Regions> <Region> <RegionId>cn-beijing</RegionId> <LocalName>华北2（北京）</LocalName> </Region> </Regions> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6", "Regions": { "Region": { "RegionId": "cn-beijing", "LocalName": "华北2（北京）" } } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | query.namespace未授权，请您先授权再操作。 |

#### 7.4.20. DescribeZones

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeZones | 要执行的操作。 取值：DescribeZones。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例所属地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Zones | Array of Zone |  | 可用区列表。 |
| Zone |  |  |  |
| ZoneId | String | cn-hangzhou-b | 可用区ID。 |
| LocalName | String | 华东 1 可用区 | 可用区名称。 |
| SlaveZones | Array of SlaveZone |  | 主可用区对应的备可用区列表。 |
| SlaveZone |  |  |  |
| ZoneId | String | cn-hangzhou-g | 备可用区ID。 |
| LocalName | String | 华东 1 可用区 G | 备可用区名称。 |

负载均衡

| RequestId | String | A48D35FF-440A-4BC0-A4A2- A9BF69B7E43A | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
&RegionId=cn-east-hangzhou-01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式负载均衡

```xml
  <RequestId>3FF183FF-F4AA-40E8-8B5D-90788C6799C2</RequestId>
   <Zones>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-g</ZoneId>
```

`<LocalName>`华东 1 可用区 `G</LocalName>`

```xml
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-d</ZoneId>
```

`<LocalName>`华东 1 可用区 `D</LocalName>`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-b</ZoneId>
```

`<LocalName>`华东 1 可用区 `B</LocalName>`

```xml
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-e</ZoneId>
```

`<LocalName>`华东 1 可用区 `E</LocalName>`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-d</ZoneId>
```

`<LocalName>`华东 1 可用区 `D</LocalName>`

```xml
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-f</ZoneId>
```

`<LocalName>`华东 1 可用区 `F</LocalName>`

```xml
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-d</ZoneId>
```

`<LocalName>`华东 1 可用区 `D</LocalName>`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-e</ZoneId>
```

`<LocalName>`华东 1 可用区 `E</LocalName>`

```xml
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-e</ZoneId>
```

`<LocalName>`华东 1 可用区 `E</LocalName>`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-f</ZoneId>
```

`<LocalName>`华东 1 可用区 `F</LocalName>`

```xml
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-h</ZoneId>
```

`<LocalName>`华东 1 可用区 `H</LocalName>`

```xml
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-b</ZoneId>
```

`<LocalName>`华东 1 可用区 `B</LocalName>`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-g</ZoneId>
```

`<LocalName>`华东 1 可用区 `G</LocalName>`

```xml
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-g</ZoneId>
```

`<LocalName>`华东 1 可用区 `G</LocalName>`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-h</ZoneId>
```

`<LocalName>`华东 1 可用区 `H</LocalName>`

```
      </Zone>
   </Zones>
```

| JSON | 格式 |
|---|---|
| { "DescribeZonesResponse": { "RequestId": "3FF183FF-F4AA-40E8-8B5D-90788C6799C2", "Zones": { "Zone": [ { |  |

负载均衡

```json
                    "SlaveZones": {
                        "SlaveZone": [
                            {
                                "ZoneId": "cn-hangzhou-g",
```

`"LocalName": "`华东 1 可用区 `G"`

```json
                            },
                            {
                                "ZoneId": "cn-hangzhou-d",
```

`"LocalName": "`华东 1 可用区 `D"`

```
                            }
```

]

```json
                    },
                    "ZoneId": "cn-hangzhou-b",
```

`"LocalName": "`华东 1 可用区 `B"`

```json
                },
                {
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-e",
```

`"LocalName": "`华东 1 可用区 `E"`

```json
                        }
                    },
                    "ZoneId": "cn-hangzhou-d",
```

`"LocalName": "`华东 1 可用区 `D"`

```json
                },
                {
                    "SlaveZones": {
                        "SlaveZone": [
                            {
                                "ZoneId": "cn-hangzhou-f",
```

`"LocalName": "`华东 1 可用区 `F"`

```json
                            },
                            {
                                "ZoneId": "cn-hangzhou-d",
```

`"LocalName": "`华东 1 可用区 `D"`

```
                            }
```

]

```json
                    },
                    "ZoneId": "cn-hangzhou-e",
```

`"LocalName": "`华东 1 可用区 `E"`

```json
                },
                {
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-e",
```

`"LocalName": "`华东 1 可用区 `E"`

```json
                        }
                    },
                    "ZoneId": "cn-hangzhou-f",
```

`"LocalName": "`华东 1 可用区 `F"`

```json
                },
                {
                    "SlaveZones": {
                        "SlaveZone": [
                            {
                                "ZoneId": "cn-hangzhou-h",
```

`"LocalName": "`华东 1 可用区 `H"`

```json
                            },
                            {
                                "ZoneId": "cn-hangzhou-b",
```

`"LocalName": "`华东 1 可用区 `B"`

```
                            }
```

]

```json
                    },
                    "ZoneId": "cn-hangzhou-g",
```

`"LocalName": "`华东 1 可用区 `G"`

```json
                },
                {
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-g",
```

`"LocalName": "`华东 1 可用区 `G"`

```json
                        }
                    },
                    "ZoneId": "cn-hangzhou-h",
```

`"LocalName": "`华东 1 可用区 `H"`

```
                }
```

]

```
        }
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

负载均衡

| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | query.namespace未授权，请您先授权再操作。 |
|---|---|---|---|

#### 7.4.21. CreateLoadBalancerPro

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKeyId | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| Action | String | Query | 否 | CreateLoadBalancerPro | 要执行的操作。取值： CreateLoadBalancerPro。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-hangzhou | 传统型负载均衡的地域ID。 |
| AddressType | String | Query | 否 | internet | 传统型负载均衡实例的网络类型。默认值为 internet。 internet：创建公网负载均衡实例后，系统会分配一个公网IP地址，可以转发公网请求。 intranet：创建专有网络类型的负载均衡实例后，系统会分配一个内网IP地址，仅可转发内网请求。 |
| InternetChargeTyp e | String | Query | 否 | paybytraffic | 公网类型实例的付费方式。取值： paybytraffic：按使用流量计费。 paybybandwidth：按固定带宽计费。 默认值为paybytraffic。 |
| Bandwidth | Integer | Query | 否 | 10 | 监听的带宽峰值，单位：Mbps。取值范围：1～ 5120。对于按带宽计费的公网负载均衡实例， 可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
| ClientToken | String | Query | 否 | 593B0448-D13E-4C56-AC0D- FDF0FDE0E9A3 | 客户端 Token，用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一。 |
| LoadBalancerName | String | Query | 否 | slb-test | 传统型负载均衡的名称。 |
| LoadBalancerMode | String | Query | 否 | nat | 传统型负载均衡的模式。默认值为nat。 nat：将内部私有网络的IP地址转换为公共网络的IP地址。 fnat _ext：将内部网络中的所有请求都转发到外部网络。 |
| Address | String | Query | 否 | 192.168.1.1 | 指定实例的私网IP地址，该地址必须包含在交换机的目标网段下。 |
| VpcId | String | Query | 否 | vpc-25dvzy9**** | 传统型负载均衡实例的所属专有网络的ID。 |
| VSwitchId | String | Query | 否 | vsw-255ecr**** | 传统型负载均衡实例的所属交换机的ID。 |
| SuName | String | Query | 否 | su0 _ | 服务售卖单元，默认值为su _0，一般su _0为售卖SU。 su _cloudops：运维域。 su _cloudmgmt：管理域。 su _0：业务域。 |

负载均衡

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CidrType | String | Query | 否 | public | CIDR类型。 public：公共CIDR。 link _local：链路本地CIDR。 |
| TunnelType | String | Query | 否 | singleTunnel | Tunnel类型。 singleTunnel：一对一。 anyTunnel：一对多或者多对多。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| MasterZoneId | String | Query | 否 | cn-hangzhou-b | 传统型负载均衡实例的主可用区ID。 |
| SlaveZoneId | String | Query | 否 | cn-hangzhou-d | 传统型负载均衡实例的备可用区ID。 |
| accesskeyid _ _ | String | Query | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | Query | 否 | {"tagKey":"Key1","tagValue":"Value1"} | 标签列表。 |
| EnableVpcVipFlow | String | Query | 否 | off | 是否启动Vpc Vip Flow。 on：启动。 off：不启动。 |
| LoadBalancerSpec | String | Query | 否 | slb.s1.small | 传统型负载均衡实例的规格。 |
| AddressIPVersion | String | Query | 否 | ipv4 | 传统型负载均衡实例的IP地址类型。默认值为 ipv4。 ipv4：ipv4协议。 ipv6：ipv6协议。 |
| ServiceProvider | String | Query | 否 | BGP | 服务提供商。 |
| DeleteProtection | String | Query | 否 | off | 是否开启实例删除保护。默认值为off。 on：开启。 off：不开启。 |
| ModificationProtect ionStatus | String | Query | 否 | NonProtection | 修改实例保护状态。默认值为NonProtection。 NonProtection：不保护。 ConsoleProtection：控制台保护。 |
| ModificationProtect ionReason | String | Query | 否 | none | 修改实例保护原因。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F6643F77-C62F-4BA7-867A- 4CB4EEB0E106 | 请求的ID。 |
| LoadBalancerId | String | lb-hddhfjg**** | 传统型负载均衡实例的ID。 |
| Address | String | 42.10.10.6 | 分配的负载均衡实例的IP地址。 |
| LoadBalancerName | String | slb-test | 传统型负载均衡实例的名称。 |
| VpcId | String | vpc-25dvzy9**** | 传统型负载均衡实例的所属专有网络的ID。 |
| VSwitchId | String | vsw-255ecr**** | 传统型负载均衡实例的所属交换机的ID。 |
| NetworkType | String | classic | 传统型负载均衡实例的网络类型。 vpc：专有网络实例。 classic：经典网络实例。 |
| AddressIPVersion | String | ipv4 | 传统型负载均衡实例的IP地址类型。 |

负载均衡

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerPro &RegionId=cn-hangzhou
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "LoadBalancerName":"slb-test", "RequestId":"F6643F77-C62F-4BA7-867A-4CB4EEB0E106", "Address":"42.10.10.6", "VpcId":"vpc-25dvzy9****", "NetworkType":"classic", "VSwitchId":"vsw-255ecr****", "AddressIPVersion":"ipv4", "LoadBalancerId":"lb-hddhfjg****" } |  |

| XML | 格式 |
|---|---|
| <LoadBalancerName>slb-test</LoadBalancerName> <RequestId>F6643F77-C62F-4BA7-867A-4CB4EEB0E106</RequestId> <Address>42.10.10.6</Address> <VpcId>vpc-25dvzy9****</VpcId> <NetworkType>classic</NetworkType> <VSwitchId>vsw-255ecr****</VSwitchId> <AddressIPVersion>ipv4</AddressIPVersion> <LoadBalancerId>lb-hddhfjg****</LoadBalancerId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ZONERESOURCENOTENOUGH _ _ _ | OperationFailed.ZoneResourceLimit | The operation failed because of resource limit of the specified zone. |
| 400 | REGIONRESOURCENOTENOUG _ _ _ H | OperationFailed.RegionResourceLimit | The operation failed because of resource limit of the specified region. |
| 400 | SLBPREPAYINTERNETPAYBYBA _ _ _ NDWIDTHALLOW _ | Operation.NotAllowed | Operation Denied. The charge type of internet prepay instance can only be paybybandwidth. |
| 400 | SYSTEM.SALEVALIDATENOSPE _ _ _ CIFICCODEFAILED _ _ | OperationFailed.UnpaidBillsExist | The account has unpaid bills. Please pay your overdue bill first. |
| 400 | -90019 | InvalidParameter | Illegal parameter. The IP address is not in subnet. |
| 400 | RegionOrZonesNotSupportIpv6 | RegionOrZonesNotSupportIpv6 | The specified region or master/slave zones does not support ipv6. |
| 400 | InvalidParameter.Mismatch | InvalidParameter.Mismatch | AddressType and IpVersion is conflict, IPv6 does not support intranet instance. |
| 400 | PAYFOR.CREDITPAYINSUFFICIE _ _ NTBALANCE _ | PAYFOR.CREDITPAYINSUFFICIENTBALANCE _ _ _ | Your account does not have enough balance. |
| 400 | MatchedHistoryIpNotExist | HighRiskOperationDenied | The operation is denied because of high risk. |
| 400 | VSwitchNoAvailableIp | VSwitchAvailableIpNotExist | The specified VSwitch has no availabe ip. |
| 400 | VSwitchNotExist | VSwitchNotExist | The specified VSwitch doesn't exist. |
| 400 | -90019 | InvalidParameter | Illegal parameter. The IP address is not in subnet. |
| 400 | ShareSlbNotSupportPay95 | Instance.ShareSlbNotSupportPay95 | Illegal parameter. The share instance not support PayBy95 or PayByOld95. |
| 400 | Pay95RateInvalid | Instance.Pay95RateInvalid | Illegal parameter. The rate is illegal. |
| 400 | RAM.ApiNotSupported | IllegalUser | Illegal user. |
| 400 | Pay95BandwidthIllegal | Instance.Pay95BandwidthIllegal | Illegal parameter. The bandwidth is illegal. |
| 400 | InternetChargeTypeNotAllowed | Instance.InternetChargeTypeNotAllowed | Illegal parameter. The specified InternetChargeType not allowed. |
| 400 | TOKENPROCESSING _ | OperationFailed.TokenIsProcessing | The operation is failed, because the Client Token is processing. |
| 400 | PAY.MAYIWITHHOLDINGAGREE _ _ MENTILLEGAL _ | PAY.MAYIWITHHOLDINGAGREEMENTILLEGAL _ _ _ | Your account did not sign a withholding agreement or no coupons in Alipay. |
| 400 | InvalidParam.Bandwidth | InvalidParameter.Bandwidth | The param Bandwidth is invalid. |

| 开发指南·API参 | 考 |  | 负载均衡 |
|---|---|---|---|

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ShareSlbHaltSales | ShareSlbHaltSales | The share instance has been discontinued. |
| 400 | -2725 | OperationDenied.SuNotOnSale | The specified service unit is not on sale. |
| 400 | -2756 | NotSupportIpv6 | The specified service unit does not support ipv6. |

#### 7.4.22. DescribeLoadBalancersPro

调用DescribeLoadBalancersPro接口查询已创建的负载均衡实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeLoadBalancersPro | 要执行的操作。取值： DescribeLoadBalancersPro。 |
| LoadBalancerStatu s | String | Query | 否 | active | 实例状态。 inactive：实例已停止，此状态的实例监听不会再转发流量。 active：实例运行中，实例创建后，默认状态为active。 locked：实例已锁定。当负载均衡实例到期后，但到期时间未超过 7 天时，负载均衡实例进入锁定状态。此种状态下，您不能对负载均衡实例进行任何操作，并且实例不再会进行流量转发，但会保留实例的 IP 和其它配置。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-hangzhou | 传统型负载均衡实例的地域 ID。 |
| ServerId | String | Query | 否 | vm-server-23**** | 添加的后端服务器ID。 |
| LoadBalancerId | String | Query | 否 | lb-bp1b6c719dfa**** | 传统型负载均衡实例ID。 |
| LoadBalancerName | String | Query | 否 | slb-test | 传统型负载均衡实例的名称。 |
| ServerIntranetAddr ess | String | Query | 否 | 10.20.20.102 | 添加的后端服务器的内网地址。 |
| AddressType | String | Query | 否 | intranet | 传统型负载均衡实例的网络类型。 internet：创建公网负载均衡实例后，系统会分配一个公网IP地址，可以转发公网请求。 intranet：创建内网负载均衡实例后，系统会分配一个内网IP地址，仅可转发内网请求。 |
| InternetChargeTyp e | String | Query | 否 | paybytraffic | 公网计费方式。 paybybandwidth：按带宽计费。 paybytraffic：按流量计费。 |
| VpcId | String | Query | 否 | vpc-bp1aevy8sof**** | 传统型负载均衡实例所属的VPC ID。 |
| VSwitchId | String | Query | 否 | vsw-bp12mw1f8k3**** | 传统型负载均衡实例所属的交换机ID。 |
| NetworkType | String | Query | 否 | vpc | 私网实例的网络类型。 vpc：专有网络实例。 classic：经典网络实例。 |
| Address | String | Query | 否 | 192.168.1.1 | 传统型负载均衡实例的服务地址。 |
| MasterZoneId | String | Query | 否 | cn-hangzhou-b | 负载均衡实例的主可用区ID。 |

| 负载均衡 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SlaveZoneId | String | Query | 否 | cn-hangzhou-d | 负载均衡实例的备可用区ID。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| Tags | String | Query | 否 | {"tagKey":"Key1","tagValue":"Value1"} | 标签列表。 |
| PayType | String | Query | 否 | PayOnDemand | 传统型负载均衡实例付费模式。 PayOnDemand：按量付费。 PrePay：包年包月。 |
| ResourceGroupId | String | Query | 否 | rg-atstuj3rtop**** | 企业资源组ID。 |
| PageNumber | Integer | Query | 否 | 1 | 分页查询时的页码。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时设置的每页行数。 |
| FilterFuzzyMode | String | Query | 否 | off | 模糊过滤模式。 on：开启。 off：关闭。 |
| AddressIPVersion | String | Query | 否 | ipv4 | IP版本，可以设置为ipv4或者ipv6。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| LoadBalancers | Array |  | 负载均衡实例列表。 |
| -LoadBalancerId | String | lb-bp1b6c719dfa**** | 负载均衡实例ID。 |
| -LoadBalancerName | String | slb-test | 负载均衡实例的名称。 |
| -LoadBalancerStatus | String | active | 负载均衡实例状态。 inactive：实例已停止，此状态的实例监听不会再转发流量。 active：实例运行中，实例创建后，默认状态为active。 locked：实例已锁定，实例已经被锁定。 |
| -Address | String | 10.20.20.102 | 负载均衡实例服务地址。 |
| -AddressType | String | intranet | 实例的网络类型。 internet：创建公网负载均衡实例后，系统会分配一个公网IP地址，可以转发公网请求。 intranet：创建内网负载均衡实例后，系统会分配一个内网IP地址，仅可转发内网请求。 |
| -RegionId | String | cn-hangzhou | 负载均衡实例所在的地域ID。 |
| -RegionIdAlias | String | hangzhou | 传统型负载均衡实例所在的地域别名。 |
| -VSwitchId | String | vsw-255ecr**** | 私网负载均衡实例的交换机ID。 |
| -VpcId | String | vpc-25dvzy9f8**** | 私网负载均衡实例的专有网络ID。 |
| -NetworkType | String | vpc | 私网负载均衡实例的网络类型。 vpc：专有网络实例。 classic：经典网络实例。 |
| -MasterZoneId | String | cn-hangzhou-b | 实例的主可用区ID。 |
| -SlaveZoneId | String | cn-hangzhou-d | 实例的备可用区ID。 |

负载均衡

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -InternetChargeType | String | paybytraffic | 公网类型实例付费方式。 paybybandwidth：按带宽计费。 paybytraffic：按流量计费。 |
| -CreateTime | String | 2021-12-02T02:49:05Z | 实例创建时间，格式为：YYYY-MM-DDThh:mm:ssZ。 |
| -CreateTimeStamp | Long | 1504147745000 | 实例创建时间戳。 |
| -PayType | String | PayOnDemand | 负载均衡实例付费模式。 PayOnDemand：按量付费。 PrePay：包年包月。 |
| -AddressIPVersion | String | ipv4 | IP版本，可以设置为ipv4或者ipv6。 |
| -ResourceGroupId | String | rg-atstuj3r**** | 企业资源组ID。 |
| -SuName | String | su0 _ | 服务售卖单元，默认值为su _0，一般su _0为售卖SU。 su _cloudops：运维域。 su _cloudmgmt：管理域。 su _0：业务域。 |
| -LoadBalancerSpec | String | slb.s1.small | 负载均衡实例的性能规格。 |
| - ModificationProtectionRea son | String | 托管实例 | 设置修改保护状态的原因，长度为 1~80 个字符，必须以字母或中文开头，支持数字、半角句号（.）、下划线（_）和短划线（-）。 |
| - ModificationProtectionStat us | String | NonProtection | 负载均衡修改保护状态： NonProtection：不限制修改保护，设置后会清空之前设置的 ModificationProtectionReason。 ConsoleProtection：实例控制台修改保护状态。 |
| -BusinessStatus | String | Normal | 业务状态。 Normal：普通状态。 FinancialLocked：财务锁定状态。 SecurityLocked：安全锁定状态。 |
| -DeleteProtection | String | off | 负载均衡删除保护状态。 on：开启。 off：关闭。 |
| -InstanceChargeType | String | PayBySpec | 实例计费方式。 PayBySpec：按规格计费。 PayByCLCU：按使用量计费。 |
| RequestId | String | 8B9DB03B-ED39-5DB8-9C9F- 1ED5F548D61E | 请求的ID。 |
| PageNumber | Integer | 1 | 实例列表页码。 |
| PageSize | Integer | 10 | 当前分页的行数。 |
| TotalCount | Integer | 1 | 根据过滤条件得到的实例总个数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancersPro &RegionId=cn-hangzhou
```

&公共请求参数正常返回示例 `JSON` 格式负载均衡

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "RequestId":"8B9DB03B-ED39-5DB8-9C9F-1ED5F548D61E",
 "PageSize":10,
 "PageNumber":1,
 "LoadBalancers":{
  "Address":"10.20.20.102",
  "ResourceGroupId":"rg-atstuj3r****",
  "InstanceChargeType":"PayBySpec",
  "AddressIPVersion":"ipv4",
  "LoadBalancerId":"lb-bp1b6c719dfa****",
  "BusinessStatus":"Normal",
  "ModificationProtectionStatus":"NonProtection",
  "LoadBalancerSpec":"slb.s1.small",
  "NetworkType":"vpc",
  "ModificationProtectionReason":"托管实例",
  "SuName":"su_0",
  "MasterZoneId":"cn-hangzhou-b",
  "VSwitchId":"vsw-255ecr****",
  "CreateTime":"2021-12-02T02:49:05Z",
  "PayType":"PayOnDemand",
  "SlaveZoneId":"cn-hangzhou-d",
  "InternetChargeType":"paybytraffic",
  "RegionIdAlias":"hangzhou",
  "LoadBalancerName":"slb-test",
  "VpcId":"vpc-25dvzy9f8****",
  "DeleteProtection":"off",
  "RegionId":"cn-hangzhou",
  "AddressType":"intranet",
  "LoadBalancerStatus":"active",
  "CreateTimeStamp":1504147745000
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <RequestId>8B9DB03B-ED39-5DB8-9C9F-1ED5F548D61E</RequestId> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <LoadBalancers> <Address>10.20.20.102</Address> <ResourceGroupId>rg-atstuj3r****</ResourceGroupId> <InstanceChargeType>PayBySpec</InstanceChargeType> <AddressIPVersion>ipv4</AddressIPVersion> <LoadBalancerId>lb-bp1b6c719dfa****</LoadBalancerId> <BusinessStatus>Normal</BusinessStatus> <ModificationProtectionStatus>NonProtection</ModificationProtectionStatus> <LoadBalancerSpec>slb.s1.small</LoadBalancerSpec> <NetworkType>vpc</NetworkType> <ModificationProtectionReason>托管实例</ModificationProtectionReason> <SuName>su_0</SuName> <MasterZoneId>cn-hangzhou-b</MasterZoneId> <VSwitchId>vsw-255ecr****</VSwitchId> <CreateTime>2021-12-02T02:49:05Z</CreateTime> <PayType>PayOnDemand</PayType> <SlaveZoneId>cn-hangzhou-d</SlaveZoneId> <InternetChargeType>paybytraffic</InternetChargeType> <RegionIdAlias>hangzhou</RegionIdAlias> <LoadBalancerName>slb-test</LoadBalancerName> <VpcId>vpc-25dvzy9f8****</VpcId> <DeleteProtection>off</DeleteProtection> <RegionId>cn-hangzhou</RegionId> <AddressType>intranet</AddressType> <LoadBalancerStatus>active</LoadBalancerStatus> <CreateTimeStamp>1504147745000</CreateTimeStamp> </LoadBalancers> |  |

#### 7.4.23. ProducePrepaidSlbInstance

调用ProducePrepaidSlbInstance接口生产预付的负载均衡实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKeyId | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |

| 开发指南·API参 | 考 |  |  |  | 负载均衡 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ProducePrepaidSlbInstance | 要执行的操作。取值： ProducePrepaidSlbInstance。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-hangzhou | 传统型负载均衡实例的地域ID。 |
| data | String | Query | 是 | data | 内容。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| accesskeyid _ _ | String | Query | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | 09F364C0-B149-40CE-AA59- 3363BF14F989 | 请求的ID。 |
| data | String | data | 内容。 |
| code | String | 200 | 结果的状态码。 |
| success | Boolean | true | 结果是否成功。 |
| message | String | successful | 结果的信息。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ProducePrepaidSlbInstance &RegionId=cn-hangzhou &data=data
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "code":"200", "data":"data", "requestId":"09F364C0-B149-40CE-AA59-3363BF14F989", "success":true, "message":"successful" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>data</data> <requestId>09F364C0-B149-40CE-AA59-3363BF14F989</requestId> <success>true</success> <message>successful</message> |  |

#### 7.4.24. FillSlbParams

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

负载均衡

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKeyId | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| Action | String | Query | 否 | FillSlbParams | 要执行的操作。取值：FillSlbParams。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-hangzhou | 传统型负载均衡实例的地域ID。 |
| data | String | Query | 是 | data | 填充的内容。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| accesskeyid _ _ | String | Query | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |
| data | String | data | 填充的内容。 |
| code | String | 200 | 结果的状态码。 |
| success | Boolean | true | 结果是否成功。 |
| message | String | successful | 结果的信息。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou &data=data
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "code":"200", "data":"data", "requestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984", "success":true, "message":"successful" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>data</data> <requestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</requestId> <success>true</success> <message>successful</message> |  |

### 监听

#### 7.5.1. TCP监听

##### 7.5.1.1. CreateLoadBalancerTCPListener

负载均衡

**说明**

新建的监听的状态为stopped。创建完成后，调用 `StartLoadBalancerListener` 接口启动监听来转发流量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateLoadBalancerTCPListe ner | 要执行的操作。 取值：CreateLoadBalancerTCPListener。 |
| Bandwidth | Integer | 是 | -1 | 监听的带宽峰值，单位为Mbps。取值：-1或1~5120。 -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为- 1，即不限制带宽峰值。 1~5120： 对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08ex**** | 负载均衡实例的ID。 |
| BackendServerPort | Integer | 否 | 80 | 负载均衡实例后端使用的端口。 取值范围：1~65535。 如果不使用服务器组（不指定VServerGroupId），则该参数必选。 |
| Scheduler | String | 否 | wrr | 调度算法。取值： wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。 tch：基于四元组的一致性哈希（源IP、目的IP、源端口和目的端口），相同的流会调度到相同的后端服务器。 说明仅性能保障型实例支持sch和tch一致性哈希算法。 |
| PersistenceTimeout | Integer | 否 | 0 | 会话保持的超时时间。单位：秒。 取值范围：0~3600。 默认值：0，表示关闭会话保持。 |
| HealthyThreshold | Integer | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值范围： 2~10。 |
| UnhealthyThreshold | Integer | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。 取值范围：2~10。 |
| HealthCheckConnectTimeout | Integer | 否 | 100 | 每次健康检查响应的最大超时时间。单位：秒。 取值范围：1~300。 默认值：5。 |
| HealthCheckConnectPort | Integer | 否 | 80 | 健康检查使用的端口。 取值范围：1~65535。 不设置此参数时，表示使用后端服务端口。 |
| healthCheckInterval | Integer | 否 | 3 | 健康检查的时间间隔。单位：秒。 取值范围：1~50。 |
| HealthCheckDomain | String | 否 | 172.XX.XX.6 | 用于健康检查的域名。取值： $ _ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用后端服务器的私网IP当做健康检查使用的域名。 domain：域名长度为1~80，只能包含字母、数字、英文句点（.） 和短划线（-）。 |

负载均衡

| HealthCheckURI | String | 否 | /test/index.html | 用于健康检查的URI。长度限制为1~80，只能使用字母、数字、短划线 （-）、正斜线（/）、英文句点（.）、百分号（%）、井号（#）和 and(&amp;)这些字符。 URL不能只为正斜线（/），但必须以正斜线 （/）开头。 当TCP监听需要使用HTTP健康检查时可配置此参数，如不配置则按TCP 健康检查。 |
|---|---|---|---|---|
| HealthCheckHttpCode | String | 否 | http2xx,http3xx _ _ | 健康检查正常的HTTP状态码，多个状态码用逗号（,）分割。 取值：http _2xx（默认值）、http _3xx、http _4xx或http _5xx。 |
| HealthCheckType | String | 否 | tcp | 健康检查类型。 取值：tcp（默认值）或http。 |
| VServerGroupId | String | 否 | rsp-cige6j**** | 虚拟服务器组ID。 |
| MasterSlaveServerGroupId | String | 否 | rsp-0bfucw**** | 主备服务器组ID。 说明服务器组ID和主备服务器组ID只能选择一个。 |
| EstablishedTimeout | Integer | 否 | 500 | 连接超时时间。单位：秒。 取值范围：10~900。 |
| Description | String | 否 | 创建监听 | 设置监听的描述信息。 长度限制为1~80个字符，允许包含字母、数字、短划线（-）、正斜线 （/）、英文句点（.）和下划线（_）等字符。支持中文描述。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclId | String | 否 | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
| AclType | String | 否 | off | 是否开启访问控制功能。取值： on：开启。 off（默认值）：关闭。 |
| AclStatus | String | 否 | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
| ConnectionDrain | String | 否 | off | 是否开启连接优雅中断。取值： on：开启。 off：不开启。 |
| ConnectionDrainTimeout | Integer | 否 | 300 | 设置连接优雅中断超时时间。单位：秒。 取值范围：10~900。 说明当ConnectionDrain取值为on时，该选项必选。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例负载均衡

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerTCPListener &Bandwidth=-1 &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateLoadBalancerTCPListenerResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </CreateLoadBalancerTCPListenerResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameterValue.SpecNotS upport | The loadBalancer of shared spec does not support the parameter value, %s. | 共享型负载均衡实例不支持指定的参数取值。 |
| 400 | InvalidParameterValue.RegionNot Support | The region does not support the parameter value, %s. | 当前地域不支持指定的参数取值。 |
| 400 | Abs.VServerGroupIdAndMasterSla veServerGroupId.MissMatch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | 参数VServerGroupId或MasterSlaveServerGroupId不匹配。 |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | 指定负载均衡的IP版本与ACL支持的IP类型冲突。 |
| 400 | InvalidParameterValue.ZoneNotS upport | The zone does not support the parameter value, %s. | 当前可用区不支持指定参数取值。 |
| 400 | ListenerProcessing | A previous configuration of the listener is pending, please try again later. | 当前监听正在配置中，请稍后重试。 |
| 400 | InvalidParameter.ListenerPortCon flict | There is conflict listener port exists. | 指定的监听端口已存在。 |
| 400 | InvalidParameter.ZoneNotSuppor t | The zone does not support the parameter %s. | 当前可用区不支持指定参数。 |
| 400 | InvalidParam.VServerGroupId | The specified VServerGroupId is invalid. | 指定的VServerGroupId无效。请检查参数约束，并在修改后重试。 |
| 400 | MissingParam.HealthCheckConne ctPort | The parameter HealthCheckConnectPort is required. | 参数HealthCheckConnectPort缺失。 |
| 400 | InvalidParam.ListenerPort | The specified ListenerPort is invalid. | 指定的ListenerPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.StartPort | The specified StartPort is invalid. | 指定的StartPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParamSize.PortRange | The size of param PortRange is invalid. | 指定的PortRange无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.EndPort | The specified EndPort is invalid. | 指定的EndPort无效。请检查参数约束，并在修改后重试。 |
| 400 | QuotaLimitExceeds.AclAttachedT oListener | %s. | Acl绑定监听数已达到配额上限。 |
| 400 | QuotaLimitExceeds.TotalAclEntry | %s. | Acl条目数已达到配额上限。 |
| 400 | Duplicated.AclEntry | %s. | Acl条目重复。 |
| 400 | OperationUnsupported.SetAccess Control | The singleTunnel/anyTunnel loadbalancer does not support config AccessControlList. | 操作被拒绝，原因是Single Tunnel和Any Tunnel 类型负载均衡实例不支持配置Acl。 |
| 400 | InvalidParam.PortRange | The specified PortRange is invalid. | 指定的PortRange无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParameter.RegionNotSupp ort | The region does not support the parameter: %s. | 当前区域不支持指定参数。 |
| 400 | LbNotSupportTcpssl | You cannot create a TCP SSL type listener for the specified load balancer. | 指定的实例不支持创建tcpssl类型的监听。 |
| 400 | LbSupportTcpsslOnly | The specified load balancer supports TCP SSL type listener only. | 指定的实例只支持创建tcpssl类型的监听。 |
| 400 | ListenerNotSupportRule | You cannot create a rule for the specified listener. | 指定的监听不支持创建转发规则。 |
| 400 | ListenerPortConflict | The specified ListenerPort is conflict with other listener. | 指定的监听端口号已被占用。 |
| 400 | ResourceNotFound.VServerGroup | %s. | 指定的服务器组不存在。 |
| 400 | IllegalParam.FailoverThreshold | The parameter FailoverThreshold is illegal. | 指定的FailoverThreshold无效。请检查参数约束，并在修改后重试。 |

负载均衡

| 400 | IllegalParam.FailoverStrategy | The parameter FailoverStrategy is illegal. | 指定的FailoverStrategy无效。请检查参数约束，并在修改后重试。 |
|---|---|---|---|
| 400 | MasterSlaveServerConflict | The servers are conflict for MasterSlaveGroup. | 主备服务器组的后端服务器冲突。 |
| 400 | OperationDenied.HealthCheckClo sedForMasterSlaveMode | The operation is denied because of HealthCheckClosedForMasterSlaveMode. | 操作被拒绝，原因是主备模式下要求必须开启健康检查。 |
| 400 | IllegalParam.HealthCheck | The param of HelathCheck is illegal. | 指定的HealthCheck无效。请检查参数约束，并在修改后重试。 |
| 400 | Mismatch.SlbSpecTypeAndListen erProtocol | The SlbSpecType and ListenerProtocol are mismatched. | 实例规格类型和监听类型不匹配。 |

##### 7.5.1.2. SetLoadBalancerTCPListenerAttribute

调用SetLoadBalancerTCPListenerAttribute修改TCP监听的配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetLoadBalancerTCPListener Attribute | 要执行的操作。 取值：SetLoadBalancerTCPListenerAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1ygod3yctvg1y**** | 负载均衡实例的ID。 |
| Bandwidth | Integer | 否 | 43 | 监听的带宽峰值，单位：Mbps。取值： -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为- 1，即不限制带宽峰值。 1~5120：对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
| Scheduler | String | 否 | wrr | 调度算法。取值： wrr：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。 tch：基于四元组的一致性哈希（源IP、目的IP、源端口和目的端口），相同的流会调度到相同的后端服务器。 说明仅性能保障型实例支持sch和tch一致性哈希算法。 |
| PersistenceTimeout | Integer | 否 | 0 | 会话保持的超时时间。单位：秒。 取值范围：0~3600，默认值：0，表示关闭会话保持。 |
| HealthyThreshold | Integer | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值范围：2~10。 |
| UnhealthyThreshold | Integer | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。 取值范围：2~10。 |
| HealthCheckConnectTimeout | Integer | 否 | 100 | 接收来自运行状况检查的响应需要等待的时间。单位：秒。 如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。 取值范围：1~300。 说明如果HealthCheckConnectTimeout的值小于HealthCheckInterval的值，则HCTimeout无效，超时时间为HealthCheckInterval的值。 |
| HealthCheckConnectPort | Integer | 否 | 8080 | 健康检查使用的端口。 取值范围：1-65535。 不设置此参数时，表示使用后端服务端口 （BackendServerPort）。 |
| HealthCheckInterval | Integer | 否 | 5 | 健康检查的时间间隔。单位：秒。 取值范围：1~50。 |

负载均衡

| HealthCheckDomain | String | 否 | 172.16.6.6 | 用于健康检查的域名。当TCP监听需要使用HTTP健康检查时可配置此参数，如不配置则按TCP健康检查。 $ _ip：后端服务器的私网IP。 当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网 IP当做健康检查使用的域名。 domain：域名长度为1~80，只能包含字母、数字、半角句号（.） 和短划线（-）。 |
|---|---|---|---|---|
| HealthCheckURI | String | 否 | /test/index.html | 用于健康检查的URI。长度为1~80个字符，支持字母、数字和短划线 （-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、 井号（#）和and （&）这些字符。URL不能只为正斜线（/），但必须以正斜线（/）开头。 当TPC监听需要使用HTTP健康检查时，可配置此参数。如不配置，则使用TPC健康检查。 |
| HealthCheckHttpCode | String | 否 | http2xx _ | 健康检查正常的HTTP状态码，多个状态码用半角逗号（,）分割。 取值：http _2xx、http _3xx、http _4xx或http _5xx。 |
| HealthCheckType | String | 否 | tcp | 健康检查类型。 取值：tcp或http。 |
| SynProxy | String | 否 | enable | 是否开启SynProxy攻击防护功能。 建议用户一般情况下不要调整此参数，由负载均衡控制。 取值：enable或disable。 |
| MaxConnection | Integer | 否 | 20 | 最大连接数。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 标签键和值。 |
| VServerGroup | String | 否 | on | 是否使用虚拟服务器组。 取值：on或off。 VserverGroup和MasterSlaveServerGroup只允许一个值为on。 |
| VServerGroupId | String | 否 | rsp-cige6j5**** | 虚拟服务器组ID。 |
| MasterSlaveServerGroupId | String | 否 | rsp-cige**** | 主备服务器组ID。 说明服务器组ID和主备服务器组ID只能选择一个。 |
| MasterSlaveServerGroup | String | 否 | on | 是否使用主备服务器组。 取值：on或off。 VserverGroup和MasterSlaveServerGroup只允许一个值为on。 |
| EstablishedTimeout | Integer | 否 | 500 | 连接超时时间。单位：秒。 取值范围：10~900。 |
| Description | String | 否 | test | TCP监听描述。长度限制为1~80个字符，支持中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）等字符。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclId | String | 否 | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |

负载均衡

| AclType | String | 否 | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
|---|---|---|---|---|
| AclStatus | String | 否 | off | 是否开启访问控制功能。取值： on：开启。 off：关闭。 |
| ConnectionDrain | String | 否 | off | 是否开启连接优雅中断。取值： on：开启。 off：不开启。 |
| ConnectionDrainTimeout | Integer | 否 | 300 | 设置连接优雅中断超时时间。单位：秒。 取值范围：10~900。 说明当ConnectionDrain取值为on时，该选项必选。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetLoadBalancerTCPListenerAttributeResponse> <RequestId>59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1</RequestId> </SetLoadBalancerTCPListenerAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameterValue.SpecNotS upport | The loadBalancer of shared spec does not support the parameter value, %s. | 共享型负载均衡实例不支持指定的参数取值。 |
| 400 | InvalidParameterValue.RegionNot Support | The region does not support the parameter value, %s. | 当前地域不支持指定的参数取值。 |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | 指定负载均衡的IP版本与ACL支持的IP类型冲突。 |
| 400 | InvalidParameterValue.ZoneNotS upport | The zone does not support the parameter value, %s. | 当前可用区不支持指定参数取值。 |
| 400 | InvalidParameter.ZoneNotSuppor t | The zone does not support the parameter %s. | 当前可用区不支持指定参数。 |
| 400 | OperationFailed.ServerGroupInUs e | The VServerGroup or MasterSlaveServerGroup can not be close for this listener. | 操作失败，原因是当前监听不支持关闭服务器组。 |
| 400 | InvalidParam.VServerGroupId | The specified VServerGroupId is invalid. | 指定的VServerGroupId无效。请检查参数约束，并在修改后重试。 |
| 400 | MissingParam.HealthCheckConne ctPort | The parameter HealthCheckConnectPort is required. | 参数HealthCheckConnectPort缺失。 |

负载均衡

| 400 | InvalidParam.ListenerPort | The specified ListenerPort is invalid. | 指定的ListenerPort无效。请检查参数约束，并在修改后重试。 |
|---|---|---|---|
| 400 | InvalidParam.StartPort | The specified StartPort is invalid. | 指定的StartPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParamSize.PortRange | The size of param PortRange is invalid. | 指定的PortRange无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.EndPort | The specified EndPort is invalid. | 指定的EndPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.PortRange | The specified PortRange is invalid. | 指定的PortRange无效。请检查参数约束，并在修改后重试。 |
| 400 | QuotaLimitExceeds.AclAttachedT oListener | %s. | Acl绑定监听数已达到配额上限。 |
| 400 | QuotaLimitExceeds.TotalAclEntry | %s. | Acl条目数已达到配额上限。 |
| 400 | Duplicated.AclEntry | %s. | Acl条目重复。 |
| 400 | ResourceNotFound.VServerGroup | %s. | 指定的服务器组不存在。 |
| 400 | IllegalParam.FailoverStrategy | The parameter FailoverStrategy is illegal. | 指定的FailoverStrategy无效。请检查参数约束，并在修改后重试。 |
| 400 | IllegalParam.FailoverThreshold | The parameter FailoverThreshold is illegal. | 指定的FailoverThreshold无效。请检查参数约束，并在修改后重试。 |
| 400 | MasterSlaveServerConflict | The servers are conflict for MasterSlaveGroup. | 主备服务器组的后端服务器冲突。 |
| 400 | MissingParam.VServerGroupId | The parameter VServerGroupId is missing. | 参数VServerGroupId缺失。 |
| 400 | OperationDenied.HealthCheckClo sedForMasterSlaveMode | The operation is denied because of HealthCheckClosedForMasterSlaveMode. | 操作被拒绝，原因是主备模式下要求必须开启健康检查。 |
| 400 | InvalidParam.HealthCheck | The param of HealthCheck is illegal. | 指定的HealthCheck无效。请检查参数约束，并在修改后重试。 |
| 400 | OperationDenied.MasterSlaveGro upLogEnabled | The operation is denied because of MasterSlaveGroupLogEnabled. | 操作被拒绝，原因是主备服务器组日志已启用。 |
| 400 | OperationDenied.NotSupportAcl | The operation is denied because The single Tunnel or any Tunnel loadbalancer does not support config AccessControlList. | 操作被拒绝，原因是Single Tunnel和Any Tunnel 类型负载均衡实例不支持配置Acl。 |

##### 7.5.1.3. DescribeLoadBalancerTCPListenerAttribute

调用DescribeLoadBalancerTCPListenerAttribute查询TCP监听配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLoadBalancerTCPList enerAttribute | 要执行的操作。 取值：DescribeLoadBalancerTCPListenerAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1ygod3yctvg1y**** | 负载均衡实例的ID。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ListenerPort | Integer | 80 | 负载均衡实例前端使用的端口。 |
| BackendServerPort | Integer | 80 | 负载均衡实例后端使用的端口。 说明当后端服务器组为虚拟服务器组时，该参数不显示。 |
| Bandwidth | Integer | -1 | 监听的带宽峰值，单位Mbps。取值： -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为-1，即不限制带宽峰值。 1~5120：对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。 |

负载均衡

| Status | String | stopped | 当前监听的状态。取值： running：监听正常运行中。 stopped：监听停止。 |
|---|---|---|---|
| SynProxy | String | enable | 是否开启SynProxy。SynProxy是负载均衡的攻击防护功能。取值： enable：开启。 disable：关闭。 建议用户一般情况下不要调整这个参数，由负载均衡控制。 |
| Scheduler | String | wrr | 调度算法。取值： wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |
| PersistenceTimeout | Integer | 0 | 是否开启了会话保持。 取值为0时，表示没有开启。 |
| HealthCheckType | String | tcp | TCP协议监听的健康检查方式。 取值：tcp或http。 |
| HealthCheck | String | on | 是否开启健康检查。 取值：on或off。 |
| HealthyThreshold | Integer | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。 取值范围： 2~10。 |
| UnhealthyThreshold | Integer | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。 取值范围：2~10。 |
| HealthCheckConnectPort | Integer | 8080 | 健康检查使用的端口。 |
| HealthCheckInterval | Integer | 5 | 健康检查的时间间隔，单位为秒。 |
| HealthCheckDomain | String | www.example.com | 用于健康检查的域名。 |
| HealthCheckURI | String | /test/index.html | 用于健康检查的URI。 长度限制为1~80，只能使用字母、数字和 -/.%?#&amp; 这些字符。 URL不能只为正斜线（/），但必须以正斜线（/）开头。 |
| HealthCheckHttpCode | String | http2xx _ | 健康检查正常的HTTP状态码。取值：http _2xx（默认值）、http _3xx、http _4xx或http _5xx。 |
| VServerGroupId | String | rsp-cige6******8 | 绑定的服务器组ID。 |
| AclId | String | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
| AclStatus | String | off | 是否开启访问控制功能。取值： on：开启。 off：关闭。 |
| AclType | String | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |

负载均衡

| ConnectionDrain | String | off | 是否开启连接优雅中断。取值： on：开启。 off：不开启。 |
|---|---|---|---|
| ConnectionDrainTimeout | Integer | 300 | 设置连接优雅中断超时时间。单位：秒。 取值范围：10~900。 说明当ConnectionDrain取值为on时，该选项必选。 |
| Description | String | 监听描述。 | 监听描述。长度限制为1~80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、英文句点（.）和下划线（_）等字符。支持中文描述。 |
| EstablishedTimeout | Integer | 500 | 连接超时时间。取值：10~900秒。 |
| HealthCheckConnectTime out | Integer | 100 | 超时时间。 |
| HealthCheckMethod | String | TCP | 健康检查方式。 |
| MasterSlaveServerGroupI d | String | rsp-0bfucw**** | 绑定的主备服务器组ID。 |
| MaxConnection | Integer | 10 | 最大连接数。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y******
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeLoadBalancerTCPListenerAttributeResponse> <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode> <PersistenceTimeout>0</PersistenceTimeout> <HealthCheckType>tcp</HealthCheckType> <HealthyThreshold>3</HealthyThreshold> <Scheduler>wrr</Scheduler> <UnhealthyThreshold>3</UnhealthyThreshold> <Bandwidth>-1</Bandwidth> <Description>tcp_80</Description> <AclStatus>off</AclStatus> <HealthCheckURI>/</HealthCheckURI> <HealthCheck>on</HealthCheck> <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout> <ListenerPort>80</ListenerPort> <Status>running</Status> <EstablishedTimeout>900</EstablishedTimeout> <HealthCheckDomain></HealthCheckDomain> <HealthCheckInterval>2</HealthCheckInterval> <RequestId>9A113A8C-BB8F-475E-9533-7819ECA2FFC1</RequestId> <BackendServerPort>80</BackendServerPort> </DescribeLoadBalancerTCPListenerAttributeResponse> |  |

`JSON` 格式负载均衡

```json
{
    "HealthCheckHttpCode": "http_2xx,http_3xx",
    "PersistenceTimeout": 0,
    "HealthCheckType": "tcp",
    "HealthyThreshold": 3,
    "Scheduler": "wrr",
    "UnhealthyThreshold": 3,
    "Bandwidth": -1,
    "Description": "tcp_80",
    "AclStatus": "off",
    "HealthCheckURI": "/",
    "HealthCheck": "on",
    "HealthCheckConnectTimeout": 5,
    "ListenerPort": 80,
    "Status": "running",
    "EstablishedTimeout": 900,
    "HealthCheckDomain": "",
    "HealthCheckInterval": 2,
    "RequestId": "9A113A8C-BB8F-475E-9533-7819ECA2FFC1",
    "BackendServerPort": 80
}
```

#### 7.5.2. UDP监听

##### 7.5.2.1. CreateLoadBalancerUDPListener

经典网络的负载均衡的UDP协议监听暂不支持查看源地址。另外，新建的监听的状态为**stopped**。创建完成后，调用 `StartLoadBalancerListener` 接口

**说明**

启动监听来转发流量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateLoadBalancerUDPListe ner | 要执行的操作。 取值：CreateLoadBalancerUDPListener。 |
| Bandwidth | Integer | 是 | 34 | 监听的带宽峰值，单位：Mbps。取值： -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为- 1，即不限制带宽峰值。 1~5120：对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。 更多信息，请参见共享实例带宽 。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1ygod3yctvg1y7**** | 负载均衡实例ID。 |
| BackendServerPort | Integer | 否 | 80 | 负载均衡实例后端使用的端口，取值范围：1~65535。 如果不使用服务器组（不指定VServerGroupId），则该参数必选。 |
| Scheduler | String | 否 | wrr | 调度算法。取值： wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。 tch：基于四元组的一致性哈希（源IP、目的IP、源端口和目的端口），相同的流会调度到相同的后端服务器。 qch：基于QUIC Connection ID一致性哈希，相同的QUIC Connection ID会调度到相同的后端服务器。 说明仅有性能保障型实例支持 sch、 tch和qch一致性 hash算法。 |
| HealthyThreshold | Integer | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值范围：2~10。 |

负载均衡

| UnhealthyThreshold | Integer | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。 取值范围：2~10。 |
|---|---|---|---|---|
| HealthCheckConnectTimeout | Integer | 否 | 100 | 接收来自运行状况检查的响应需要等待的时间。单位：秒。取值范围：1~300。 如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。 |
| HealthCheckConnectPort | Integer | 否 | 80 | 健康检查使用的端口。取值范围：1~65535。 不设置此参数时，表示使用后端服务端口。 |
| healthCheckInterval | Integer | 否 | 3 | 健康检查的时间间隔。单位：秒。取值范围：1~50。 |
| healthCheckReq | String | 否 | hello | UDP监听健康检查的请求串，长度为1~500个字符，只支持字母和数字。 |
| healthCheckExp | String | 否 | ok | UDP监听健康检查的响应串，长度为1~500个字符，只支持字母和数字。 |
| VServerGroupId | String | 否 | rsp-cige6j675**** | 服务器组ID。 |
| MasterSlaveServerGroupId | String | 否 | rsp-0bfucwu**** | 主备服务器组ID。 说明服务器组ID和主备服务器组ID只能选择一个。 |
| Tags | String | 否 | 11111 | 标签。 |
| Description | String | 否 | test | 设置监听的描述信息。 长度限制为1~80个字符，允许包含字母、数字、短划线（-）、正斜线 （/）、半角句号（.）和下划线（_）等字符，且支持中文描述。 |
| RegionId | String | 是 | cn-hangzhou | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclId | String | 否 | acl-bp1l0kk4gxce43kz**** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
| AclType | String | 否 | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 当AclStatus参数的值为on时，该参数有效。 |
| AclStatus | String | 否 | off | 是否开启访问控制功能。取值： on：开启。 off（默认值）：关闭。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerUDPListener &Bandwidth=34 &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y7****
```

`&<`公共请求参数> 正常返回示例负载均衡

| XML | 格式 |
|---|---|
| <CreateLoadBalancerUDPListenerResponse> <RequestId>06F00FBB-3D9E-4CCE-9D43-1A6946A75456</RequestId> </CreateLoadBalancerUDPListenerResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameterValue.SpecNotS upport | The loadBalancer of shared spec does not support the parameter value, %s. | 共享型负载均衡实例不支持指定的参数取值。 |
| 400 | InvalidParameterValue.RegionNot Support | The region does not support the parameter value, %s. | 当前地域不支持指定的参数取值。 |
| 400 | Abs.VServerGroupIdAndMasterSla veServerGroupId.MissMatch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | 参数VServerGroupId或MasterSlaveServerGroupId不匹配。 |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | 指定负载均衡的IP版本与ACL支持的IP类型冲突。 |
| 400 | InvalidParameterValue.ZoneNotS upport | The zone does not support the parameter value, %s. | 当前可用区不支持指定参数取值。 |
| 400 | ListenerProcessing | A previous configuration of the listener is pending,please try again later. | 当前监听正在配置中，请稍后重试。 |
| 400 | InvalidParameter.ListenerPortCon flict | There is conflict listener port exists. | 指定的监听端口已存在。 |
| 400 | InvalidParam.VServerGroupId | The specified VServerGroupId is invalid. | 指定的VServerGroupId无效。请检查参数约束，并在修改后重试。 |
| 400 | MissingParam.HealthCheckConne ctPort | The parameter HealthCheckConnectPort is required. | 参数HealthCheckConnectPort缺失。 |
| 400 | InvalidParam.ListenerPort | The specified ListenerPort is invalid. | 指定的ListenerPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.StartPort | The specified StartPort is invalid. | 指定的StartPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParamSize.PortRange | The size of param PortRange is invalid. | 指定的PortRange无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.EndPort | The specified EndPort is invalid. | 指定的EndPort无效。请检查参数约束，并在修改后重试。 |
| 400 | QuotaLimitExceeds.AclAttachedT oListener | %s. | Acl绑定监听数已达到配额上限。 |
| 400 | QuotaLimitExceeds.TotalAclEntry | %s. | Acl条目数已达到配额上限。 |
| 400 | Duplicated.AclEntry | %s. | Acl条目重复。 |
| 400 | InvalidParameter.RegionNotSupp ort | The region does not support the parameter: %s. | 当前区域不支持指定参数。 |
| 400 | LbNotSupportTcpssl | You cannot create a TCP SSL type listener for the specified load balancer. | 指定的实例不支持创建tcpssl类型的监听。 |
| 400 | LbSupportTcpsslOnly | The specified load balancer supports TCP SSL type listener only. | 指定的实例只支持创建tcpssl类型的监听。 |
| 400 | ListenerNotSupportRule | You cannot create a rule for the specified listener. | 指定的监听不支持创建转发规则。 |
| 400 | InvalidParamLength.HealthCheck Exp | The length of the parameter HealthCheckReq is invalid. | 指定的HealthCheckExp无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParamLength.HealthCheck Req | The length of the parameter HealthCheckReq is invalid. | 指定的HealthCheckReq无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.HealthCheckReq | The param HealthCheckReq is invalid. | 指定的HealthCheckReq无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.HealthCheckExp | The param HealthCheckExp is invalid. | 指定的HealthCheckExp无效。请检查参数约束，并在修改后重试。 |
| 400 | ResourceNotFound.VServerGroup | %s. | 指定的服务器组不存在。 |
| 400 | IllegalParam.FailoverThreshold | The parameter FailoverThreshold is illegal. | 指定的FailoverThreshold无效。请检查参数约束，并在修改后重试。 |
| 400 | IllegalParam.FailoverStrategy | The parameter FailoverStrategy is illegal. | 指定的FailoverStrategy无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParameter.ZoneNotSuppor t | The zone does not support the parameter %s. | 当前可用区不支持指定参数。 |
| 400 | MasterSlaveServerConflict | The servers are conflict for MasterSlaveGroup. | 主备服务器组的后端服务器冲突。 |

负载均衡

| 400 | VipNotSupportQuicVersion | The listener does not support the parameter of QuicVersion. | 当前监听不支持QuicVersion参数。 |
|---|---|---|---|
| 400 | IllegalParam.HealthCheckType | The param of HealthCheckType is illegal. | 指定的HealthCheckType无效。请检查参数约束，并在修改后重试。 |
| 400 | MissingParam.HealthCheckMetho d | The param of HealthCheckMethod is missing. | 参数HealthCheckMethod缺失。 |
| 400 | IllegalParam.HealthCheckMethod | The param of HealthCheckMethod is illegal. | 指定的HealthCheckMethod无效。请检查参数约束，并在修改后重试。 |
| 400 | IllegalParam.HealthCheck | The param of HealthCheck is illegal. | 指定的HealthCheck无效。请检查参数约束，并在修改后重试。 |
| 400 | OperationDenied.SpecialListener PortNotAllowed | The operation is not allowed because port 4789 is reserved by the system. | 操作被拒绝，原因是4789是系统保留端口。 |
| 400 | Mismatch.SlbSpecTypeAndListen erProtocol | The SlbSpecType and ListenerProtocol are mismatched. | 实例规格类型和监听类型不匹配。 |

##### 7.5.2.2. SetLoadBalancerUDPListenerAttribute

调用SetLoadBalancerUDPListenerAttribute修改UDP协议监听的配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetLoadBalancerUDPListener Attribute | 要执行的操作。 取值：SetLoadBalancerUDPListenerAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1rtfnodmywb43ecu4sf- c**** | 负载均衡实例的ID。 |
| Bandwidth | Integer | 否 | -1 | 监听的带宽峰值，单位：Mbps。取值： -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为- 1，即不限制带宽峰值。 1~5120： 对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。详细信息，请参见共享实例带宽 。 |
| Scheduler | String | 否 | wrr | 调度算法。取值： wrr：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性哈希，相同的源地址会调度到相同的后端服务器。 tch：基于四元组的一致性哈希（源IP、目的IP、源端口和目的端口），相同的流会调度到相同的后端服务器。 qch：基于QUIC Connection ID一致性哈希，相同的QUIC Connection ID会调度到相同的后端服务器。 说明仅有性能保障型实例支持sch、 tch和 qch一致性哈希算法。 |
| HealthyThreshold | Integer | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值范围：2~10。 |
| UnhealthyThreshold | Integer | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。 取值范围：2~10。 |
| HealthCheckConnectTimeout | Integer | 否 | 100 | 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。单位：秒。 取值范围：1~300。 说明如果HealthCheckConnectTimeout的值小于HealthCheckInterval的值， 则HealthCheckConnectTimeout无效，超时时间为HealthCheckInterval的值。 |
| HealthCheckConnectPort | Integer | 否 | 80 | 健康检查使用的端口。 取值范围：1~65535。 |

负载均衡

| HealthCheckInterval | Integer | 否 | 5 | 健康检查的时间间隔。单位：秒。 取值范围：1~50。 |
|---|---|---|---|---|
| healthCheckReq | String | 否 | hello | UDP监听健康检查的请求字符串，只允许包含字母、数字字符，最大长度限制为500个字符。 |
| healthCheckExp | String | 否 | ok | UDP监听健康检查的响应字符串，只允许包含字母、数字字符，最大长度限制为500个字符。 |
| MaxConnection | Integer | 否 | 10 | 最大连接数。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 标签键和值。 |
| VServerGroup | String | 否 | on | 是否使用虚拟服务器组。 取值：on或off。 说明 VserverGroup和MasterSlaveServerGroup只允许一个值为on。 |
| VServerGroupId | String | 否 | rsp-cige64356q**** | 虚拟服务器组ID。 |
| MasterSlaveServerGroupId | String | 否 | rsp-0bfuqwedcc**** | 主备服务器组ID。 说明服务器组ID和主备服务器组ID只能选择一个。 |
| MasterSlaveServerGroup | String | 否 | on | 是否使用主备服务器组。 取值：on或off。 VserverGroup和MasterSlaveServerGroup只允许一个值为on。 |
| Description | String | 否 | test | 设置监听的描述信息。 长度限制为1~80个字符，允许包含字母、数字、短划线（-）、正斜线 （/）、半角句号（.）和下划线（_）等字符，支持中文描述。 |
| RegionId | String | 是 | cn-hangzhou | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclId | String | 否 | acl-bp1l0kk4gxce43kz**** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
| AclType | String | 否 | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
| AclStatus | String | 否 | off | 是否开启访问控制功能。取值： on：开启。 off：关闭。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例负载均衡

```
http(s)://[Endpoint]/?Action=SetLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43ecu4sf-c****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetLoadBalancerUDPListenerAttributeResponse> <RequestId>A0F0643E-D653-4F6F-A67F-205B2A92BE18</RequestId> </SetLoadBalancerUDPListenerAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameterValue.RegionNot Support | The region does not support the parameter value, %s. | 当前地域不支持指定的参数取值。 |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | 指定负载均衡的IP版本与ACL支持的IP类型冲突。 |
| 400 | InvalidParameterValue.ZoneNotS upport | The zone does not support the parameter value, %s. | 当前可用区不支持指定参数取值。 |
| 400 | InvalidParam.VServerGroupId | The specified VServerGroupId is invalid. | 指定的VServerGroupId无效。请检查参数约束，并在修改后重试。 |
| 400 | MissingParam.HealthCheckConne ctPort | The parameter HealthCheckConnectPort is required. | 参数HealthCheckConnectPort缺失。 |
| 400 | InvalidParam.ListenerPort | The specified ListenerPort is invalid. | 指定的ListenerPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.StartPort | The specified StartPort is invalid. | 指定的StartPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParamSize.PortRange | The size of param PortRange is invalid. | 指定的PortRange无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.EndPort | The specified EndPort is invalid. | 指定的EndPort无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.PortRange | The specified PortRange is invalid. | 指定的PortRange无效。请检查参数约束，并在修改后重试。 |
| 400 | QuotaLimitExceeds.AclAttachedT oListener | %s. | Acl绑定监听数已达到配额上限。 |
| 400 | QuotaLimitExceeds.TotalAclEntry | %s. | Acl条目数已达到配额上限。 |
| 400 | Duplicated.AclEntry | %s. | Acl条目重复。 |
| 400 | InvalidParamLength.HealthCheck Req | The length of the parameter HealthCheckReq is invalid. | 指定的HealthCheckReq无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParamLength.HealthCheck Exp | The length of the parameter HealthCheckExp is invalid. | 指定的HealthCheckExp无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.HealthCheckReq | The param HealthCheckReq is invalid. | 指定的HealthCheckReq无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.HealthCheckExp | The param HealthCheckExp is invalid. | 指定的HealthCheckExp无效。请检查参数约束，并在修改后重试。 |
| 400 | IllegalParam.FailoverThreshold | The parameter FailoverThreshold is illegal. | 指定的FailoverThreshold无效。请检查参数约束，并在修改后重试。 |
| 400 | IllegalParam.FailoverStrategy | The parameter FailoverStrategy is illegal. | 指定的FailoverStrategy无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParameter.ZoneNotSuppor t | The zone does not support the parameter %s. | 当前可用区不支持指定参数。 |
| 400 | MasterSlaveServerConflict | The servers are conflict for MasterSlaveGroup. | 主备服务器组的后端服务器冲突。 |
| 400 | MissingParam.VServerGroupId | The parameter VServerGroupId is missing. | 参数VServerGroupId缺失。 |
| 400 | VipNotSupportQuicVersion | The listener does not support the parameter of QuicVersion. | 当前监听不支持QuicVersion参数。 |
| 400 | IllegalParam.HealthCheckType | The param of HealthCheckType is illegal. | 指定的HealthCheckType无效。请检查参数约束，并在修改后重试。 |
| 400 | IllegalParam.HealthCheckMethod | The param of HealthCheckMethod is illegal. | 指定的HealthCheckMethod无效。请检查参数约束，并在修改后重试。 |
| 400 | IllegalParam.HealthCheck | The param of HealthCheck is illegal. | 指定的HealthCheck无效。请检查参数约束，并在修改后重试。 |

负载均衡

| 400 | OperationDenied.MasterSlaveGro upLogEnabled | The operation is denied because of MasterSlaveGroupLogEnabled. | 操作被拒绝，原因是主备服务器组日志已启用。 |
|---|---|---|---|

##### 7.5.2.3. DescribeLoadBalancerUDPListenerAttribute

调用DescribeLoadBalancerUDPListenerAttribute查询UDP监听的配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLoadBalancerUDPLis tenerAttribute | 要执行的操作。 取值：DescribeLoadBalancerUDPListenerAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1rtfnodmywb43e**** | 负载均衡实例ID。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ListenerPort | Integer | 80 | 负载均衡实例前端使用的端口。 |
| BackendServerPort | Integer | 53 | 负载均衡实例后端使用的端口。 说明如果后端服务器组为虚拟服务器组，则不返回该参数。 |
| Bandwidth | Integer | -1 | 监听的带宽峰值，单位Mbps。取值： -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为-1，即不限制带宽峰值。 1~5120：对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
| Status | String | stopped | 当前监听的状态。取值： running：表示监听正常运行。 stopped：表示监听运行停止。 |
| Scheduler | String | wrr | 调度算法。 wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。 当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |
| HealthCheck | String | on | 是否开启健康检查。 取值：on或off。 |
| HealthyThreshold | Integer | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值范围：2~10。 |
| UnhealthyThreshold | Integer | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。 取值范围：2~10。 |
| HealthCheckConnectTime out | Integer | 100 | 健康检查响应超时时间。 |
| HealthCheckConnectPort | Integer | 8080 | 健康检查的端口。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckInterval | Integer | 5 | 健康检查的时间间隔，单位为秒。 |
| VServerGroupId | String | rsp-cige6j**** | 绑定的虚拟服务器组ID。 |

负载均衡

| AclId | String | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
|---|---|---|---|
| AclStatus | String | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
| AclType | String | off | 是否开启访问控制功能。取值： on：开启。 off：关闭。 |
| Description | String | test | 监听的描述信息。 长度限制为1~80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）等字符，支持中文描述。 |
| HealthCheckExp | String | ok | UDP监听健康检查的响应串。 |
| HealthCheckReq | String | hello | UDP监听健康检查的请求串。 |
| MasterSlaveServerGroupI d | String | rsp-0bfucw**** | 绑定的主备服务器组ID。 |
| MaxConnection | Integer | 10 | 最大连接数。 |
| PersistenceTimeout | Integer | 0 | 会话保持超时时间。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43e****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeLoadBalancerUDPListenerAttributeResponse> <AclStatus>off</AclStatus> <HealthCheck>on</HealthCheck> <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout> <PersistenceTimeout>0</PersistenceTimeout> <ListenerPort>80</ListenerPort> <Status>stopped</Status> <Scheduler>wrr</Scheduler> <HealthyThreshold>3</HealthyThreshold> <HealthCheckInterval>2</HealthCheckInterval> <RequestId>9C103591-2533-432B-9E6B-6DB098C0E65C</RequestId> <UnhealthyThreshold>3</UnhealthyThreshold> <BackendServerPort>34</BackendServerPort> <Bandwidth>67</Bandwidth> </DescribeLoadBalancerUDPListenerAttributeResponse> |  |

`JSON` 格式负载均衡

```json
{
 "AclStatus":"off",
 "HealthCheck":"on",
 "HealthCheckConnectTimeout":5,
 "PersistenceTimeout":0,
 "ListenerPort":80,
 "Status":"stopped",
 "Scheduler":"wrr",
 "HealthyThreshold":3,
 "HealthCheckInterval":2,
 "RequestId":"9C103591-2533-432B-9E6B-6DB098C0E65C",
 "UnhealthyThreshold":3,
 "BackendServerPort":34,
 "Bandwidth":67
}
```

#### 7.5.3. HTTP监听

##### 7.5.3.1. CreateLoadBalancerHTTPListener

调用CreateLoadBalancerHTTPListener创建HTTP监听。

| 说明新建的监听的状态为stopped。 |  |  |
|---|---|---|
| 创建完成后，调用 | StartLoadBalancerListener | 接口启动监听来转发流量。 |

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateLoadBalancerHTTPList ener | 要执行的操作。 取值：CreateLoadBalancerHTTPListener。 |
| Bandwidth | Integer | 是 | -1 | 监听的带宽峰值，单位Mbps。取值： -1：不限制带宽峰值。 1~5120：监听的带宽峰值，所有监听的带宽峰值之和不能超过实例的带宽峰值。 说明该参数只适用于中国内地。 |
| HealthCheck | String | 是 | on | 是否开启健康检查。 取值：on或off。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1c9vixxjh92q83tw**** | 负载均衡实例的ID。 |
| StickySession | String | 是 | off | 是否开启会话保持。 取值：on或off。 |
| BackendServerPort | Integer | 否 | 80 | 负载均衡实例后端使用的端口。 取值：1~65535。 说明如果不使用服务器组（不指定VServerGroupId参数），则该参数必选。 |
| XForwardedFor | String | 否 | on | 是否开启通过 X-Forwarded-For 头字段获取来访者真实 IP。 取值为on或off。 |
| Scheduler | String | 否 | wrr | 调度算法。取值： wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |

负载均衡

| StickySessionType | String | 否 | insert | Cookie的处理方式。取值： insert：植入Cookie。 客户端第一次访问时，负载均衡会在返回请求中植入Cookie（即在 HTTP或HTTPS响应报文中插入ServerId），下次客户端携带此 Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server：重写Cookie。 负载均衡发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。 说明当StickySession的值为on时，必须指定该参数。 |
|---|---|---|---|---|
| CookieTimeout | Integer | 否 | 500 | Cookie超时时间，单位：秒。 取值范围：1~86400。 说明当StickySession为on且StickySessionType为insert时， 该参数必选。 |
| Cookie | String | 否 | B490B5EBF6F3CD402E515D 22BCDA1598 | 服务器上配置的Cookie。 长度为1~200个字符，支持ASCII英文字母和数字字符，但不能包含半角逗号（,）、半角分号（;）、空格或美元符号（$）这些符号。 说明当StickySession为on且StickySessionType为server时， 该参数必选。 |
| HealthCheckMethod | String | 否 | head | 监听HTTP类型健康检查的健康检查方法。取值：head或get。 说明 HealthCheck值为on时才会有效。 |
| HealthCheckDomain | String | 否 | 172.16.22.22 | 用于健康检查的域名，取值： $ _ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。 domain：域名长度为1~80字符，只能包含字母、数字、半角句号 （.）和短划线（-）。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckURI | String | 否 | /test/index.html | 用于健康检查的URI。 长度限制为1~80字符，支持英文字母、数字、短划线（-）、正斜线 （/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和 and（&）字符。URI不能只包含正斜线（/），但必须以正斜线（/）开头。 说明在HealthCheck值为on时才会有效。 |
| HealthyThreshold | Integer | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值：2~10。 说明在HealthCheck值为on时才会有效。 |
| UnhealthyThreshold | Integer | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。 取值：2~10。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckTimeout | Integer | 否 | 3 | 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。在HealthCheck值为on时才会有效。 取值：1~300秒。 说明如果HealthCHeckTimeout的值小于HealthCheckInterval的值， 则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。 |
| HealthCheckConnectPort | Integer | 否 | 80 | 健康检查的后端服务器的端口。 取值： 1~65535。 说明在HealthCheck值为on时才会有效。 |

负载均衡

| HealthCheckInterval | Integer | 否 | 5 | 健康检查的时间间隔。 取值： 1~50秒。 说明在HealthCheck值为on时才会有效。 |
|---|---|---|---|---|
| HealthCheckHttpCode | String | 否 | http2xx,http3xx _ _ | 健康检查正常的HTTP状态码，多个状态码用半角逗号（,）分隔。 默认值为http _2xx。 取值：http _2xx、http _3xx、http _4xx或http _5xx。 说明在HealthCheck值为on时才会有效。 |
| VServerGroupId | String | 否 | rsp-cige6j**** | 虚拟服务器组ID。 |
| XForwardedForSLBIP _ | String | 否 | on | 是否通过 SLB-IP 头字段获取客户端请求的真实IP。 取值：on或off（默认值）。 |
| XForwardedForSLBID _ | String | 否 | on | 是否通过 SLB-ID 头字段获取负载均衡实例ID。 取值：on或off（默认值）。 |
| XForwardedForproto _ | String | 否 | on | 是否通过 X-Forwarded-Proto 头字段获取负载均衡实例的监听协议。 取值：on或off（默认值）。 |
| Gzip | String | 否 | on | 是否开启Gzip压缩，对特定文件类型进行压缩。默认值为on。 取值：on或off（默认值）。 |
| IdleTimeout | Integer | 否 | 3 | 指定连接空闲超时时间，单位：秒。 取值范围：1~60，默认值：15。 在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到下一次请求来临时重新建立新的连接。 |
| RequestTimeout | Integer | 否 | 6 | 指定请求超时时间，单位：秒。 取值范围：1~180，默认值：60。 在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。 |
| ListenerForward | String | 否 | off | 是否开启HTTP至HTTPS的转发。 取值：on或off。 |
| ForwardPort | Integer | 否 | 443 | HTTP至HTTPS的监听转发端口。 |
| Description | String | 否 | 监听说明 | 设置监听的描述信息。 长度限制为1~80个字符，允许包含字母、数字、短划线（-）、正斜线 （/）、半角句号（.）和下划线（_）等字符。支持中文描述。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclId | String | 否 | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
| AclType | String | 否 | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |

负载均衡

| AclStatus | String | 否 | off | 是否开启访问控制功能。取值： on：开启。 off（默认值）：关闭。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPListener &Bandwidth=-1 &HealthCheck=on &ListenerPort=80 &LoadBalancerId=lb-bp1c9vixxjh92q83tw**** &StickySession=off
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateLoadBalancerHTTPListenerResponse> <RequestId>1FF504CB-BFFF-4508-A51A-58A416604FC8</RequestId> </CreateLoadBalancerHTTPListenerResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter.RegionNotSupp ort | The region does not support the parameter: %s. | 当前区域不支持指定参数。 |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | 指定负载均衡的IP版本与ACL支持的IP类型冲突。 |
| 400 | InvalidParameter | The specified ListenerPort or ForwardPort is invalid. | 指定的ListenerPort or ForwardPort无效。请检查参数约束，并在修改后重试。 |
| 400 | ListenerForwardNotSupport | X-Forward-For is not supported to a ipv6 instance. | Ipv6负载均衡实例不支持X-Forward-For。 |
| 400 | InvalidParameter.IdleTimeout | The specified IdleTimeout exceeds the limit. | 指定的IdleTimeout无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParameter.RequestTimeou t | The specified RequestTimeout exceeds the limit. | 指定的RequestTimeout无效。请检查参数约束，并在修改后重试。 |
| 400 | ListenerProcessing | A previous configuration of the listener is pending,please try again later. | 当前监听正在配置中，请稍后重试。 |
| 400 | InvalidParameter.ListenerPortCon flict | There is conflict listener port exists. | 指定的监听端口已存在。 |
| 400 | ResourceNotAvailible.HttpListene r | The specified Zone did not have enough resource. | 指定可用区资源不足。 |
| 400 | OperationUnsupported.CreateLoa dBalancerLayer7Listener | The slb instance does not support create HTTP or HTTPS listener. | 当前负载均衡实例不支持创建Http或者Https类型的监听。 |
| 400 | InvalidParameter.VServerGroupId | The MasterSlaveServerGroup can not be attached to HTTP or HTTPS listener. | HTTP或HTTPS监听不支持挂载主备服务器组。 |
| 400 | MissingParam.HealthCheckDomai n | The HealthCheckDomain is required when HealthCheckHttpVersion is http1.1. | 参数HealthCheckDomain缺失。 |
| 400 | InvalidParameter.HealthCheckHtt pVersion | The param HealthCheckHttpVersion is invalid. | 指定的HealthCheckHttpVersion无效。请检查参数约束， 并在修改后重试。 |
| 400 | QuotaLimitExceeds.AclAttachedT oListener | %s. | Acl绑定监听数已达到配额上限。 |
| 400 | QuotaLimitExceeds.TotalAclEntry | %s. | Acl条目数已达到配额上限。 |
| 400 | Duplicated.AclEntry | %s. | Acl条目重复。 |
| 400 | OperationFailed.InsufficientResou rces | The loadbalancer does not support this operation because of insufficient resources. | 操作失败，原因是由于资源不足，负载均衡器不支持此操作。 |
| 400 | InvalidParameter.ForwardCode | The specified ForwardCode is invalid. | 指定的ForwardCode无效。请检查参数约束，并在修改后重试。 |

负载均衡

| 400 | LbNotSupportTcpssl | You cannot create a TCP SSL type listener for the specified load balancer. | 指定的实例不支持创建tcpssl类型的监听。 |
|---|---|---|---|
| 400 | LbSupportTcpsslOnly | The specified load balancer supports TCP SSL type listener only. | 指定的实例只支持创建tcpssl类型的监听。 |
| 400 | ListenerNotSupportRule | You cannot create a rule for the specified listener. | 指定的监听不支持创建转发规则。 |
| 400 | Mismatch.SlbSpecTypeAndListen erProtocol | The SlbSpecType and ListenerProtocol are mismatched. | 实例规格类型和监听类型不匹配。 |

##### 7.5.3.2. SetLoadBalancerHTTPListenerAttribute

调用SetLoadBalancerHTTPListenerAttribute修改HTTP监听的配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetLoadBalancerHTTPListene rAttribute | 要执行的操作。 取值：SetLoadBalancerHTTPListenerAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1qjwo61pqz3ah**** | 负载均衡实例的ID。 |
| Bandwidth | Integer | 否 | -1 | 监听的带宽峰值，单位：Mbps。取值：-1或1~5120。 -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为- 1，即不限制带宽峰值。 1~5120：对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。 详细信息，请参见共享实例带宽 。 |
| XForwardedFor | String | 否 | on | 是否通过X-Forwarded-For获取客户端请求的真实IP。 取值：on或off。 |
| Scheduler | String | 否 | wrr | 调度算法。取值： wrr：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |
| StickySession | String | 否 | on | 是否开启会话保持。 取值：on或off。 |
| StickySessionType | String | 否 | insert | Cookie的处理方式。取值： insert：植入Cookie。 客户端第一次访问时，负载均衡会在返回请求中植入Cookie（即在 HTTP或HTTPS响应报文中插入ServerId），下次客户端携带此 Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server：重写Cookie。 负载均衡发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。 说明当StickySession的值为on时，必须指定该参数。 |
| CookieTimeout | Integer | 否 | 500 | Cookie超时时间。单位：秒。 取值范围：1~86400。 说明当StickySession为on且StickySessionType为insert时， 该参数必选。 |
| Cookie | String | 否 | B490B5EBF6F3CD402E515D 22BCDA1598 | 服务器上配置的Cookie。长度为1~200个字符，支持ASCII英文字母和数字字符，不能以半角逗号（,）、半角分号（;）、空格或美元符号 （$）开头。 说明当StickySession为on且StickySessionType为server时， 该参数必选。 |

负载均衡

| HealthCheck | String | 否 | on | 是否开启健康检查。 取值：on或off。 |
|---|---|---|---|---|
| HealthCheckMethod | String | 否 | get | 监听HTTP类型健康检查的健康检查方法。取值：head或get。 说明 HealthCheck值为on时才会有效。 |
| HealthCheckDomain | String | 否 | 172.XX.XX.6 | 用于健康检查的域名，取值： $ _ip： 后端服务器的私网IP。当指定了$ _ip或 HealthCheckDomain未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。 domain：域名长度为1~80字符，只能包含字母、数字、半角句号 （.）和短划线（-）。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckURI | String | 否 | /test/index.html | 用于健康检查的URI。 长度限制为1~80，只能使用字母、数字、短划线（-）、正斜线（/）、 半角句号（.）、百分号（%）、半角问号（?）、井号（#）和 and（&）这些字符。 URL不能只为正斜线（/），但必须以正斜线 （/）开头。 说明在HealthCheck值为on时才会有效。 |
| HealthyThreshold | Integer | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值范围：2~10。 说明在HealthCheck值为on时才会有效。 |
| UnhealthyThreshold | Integer | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。 取值范围：2~10。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckTimeout | Integer | 否 | 3 | 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。在HealthCheck值为on时才会有效。单位：秒。 取值范围：1~300。 说明如果HealthCHeckTimeout的值小于HealthCheckInterval的值， 则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。 |
| HealthCheckInterval | Integer | 否 | 5 | 健康检查的时间间隔。单位：秒。 取值范围：1~50。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckConnectPort | Integer | 否 | 8080 | 健康检查使用的端口。 取值范围：1~65535。 说明当HealthCheck值为on时才会有效。 |
| HealthCheckHttpCode | String | 否 | http2xx _ | 健康检查正常的HTTP状态码，多个状态码用半角逗号（,）分割。 取值：http _2xx、http _3xx、http _4xx或http _5xx。 说明在HealthCheck值为on时才会有效。 |
| MaxConnection | Integer | 否 | 10 | 最大连接数。 |
| VServerGroup | String | 否 | on | 是否使用虚拟服务器组。 取值：on或off。 |
| VServerGroupId | String | 否 | rsp-cige6j**** | 服务器组ID。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 标签键和值。 |

负载均衡

| XForwardedForSLBIP _ | String | 否 | on | 是否通过 SLB-IP 头字段获取客户端请求的真实IP。 取值：on或off。 |
|---|---|---|---|---|
| XForwardedForSLBID _ | String | 否 | on | 是否通过 SLB-ID 头字段获取负载均衡实例ID。 取值：on或off。 |
| XForwardedForproto _ | String | 否 | on | 是否通过 X-Forwarded-Proto 头字段获取负载均衡实例的监听协议。 取值：on或off。 |
| Gzip | String | 否 | on | 是否开启Gzip压缩，对特定文件类型进行压缩。 取值：on或off。 |
| IdleTimeout | Integer | 否 | 12 | 指定连接空闲超时时间。单位：秒。取值范围：1~60，默认值：15。 在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。 |
| RequestTimeout | Integer | 否 | 3 | 指定请求超时时间。单位：秒。取值范围：1~180，默认值：60。 在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。 |
| Description | String | 否 | test | 设置监听的描述信息。 长度限制为1~80个字符，允许包含字母、数字、短划线（-）、正斜线 （/）、半角句号（.）和下划线（_）等字符。支持中文描述。 |
| RegionId | String | 是 | cn-hangzhou | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclId | String | 否 | acl-bp1l0kk4gxce43kz**** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
| AclType | String | 否 | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
| AclStatus | String | 否 | off | 是否开启访问控制功能。取值： on：开启。 off：关闭。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1qjwo61pqz3ah****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetLoadBalancerHTTPListenerAttributeResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </SetLoadBalancerHTTPListenerAttributeResponse> |  |

负载均衡

| JSON | 格式 |
|---|---|
| {"RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | 指定负载均衡的IP版本与ACL支持的IP类型冲突。 |
| 400 | Operation.NotAllowed | Operation Denied. The HTTP listener does not support this action. | 操作被拒绝，原因是HTTP 类型监听不支持此操作。 |
| 400 | InvalidParameter.IdleTimeout | The specified IdleTimeout exceeds the limit. | 指定的IdleTimeout无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParameter.RequestTimeou t | The specified RequestTimeout exceeds the limit. | 指定的RequestTimeout无效。请检查参数约束，并在修改后重试。 |
| 400 | ListenerForwardNotSupport | X-Forward-For is not supported to a ipv6 instance. | Ipv6负载均衡实例不支持X-Forward-For。 |
| 400 | InvalidParameter.RegionNotSupp ort | The region does not support the parameter: %s. | 当前区域不支持指定参数。 |
| 400 | OperationFailed.ServerGroupInUs e | The VServerGroup or MasterSlaveServerGroup can not be close for this listener. | 操作失败，原因是当前监听不支持关闭服务器组。 |
| 400 | InvalidParameter.VServerGroupId | The MasterSlaveServerGroup can not be attached to HTTP or HTTPS listener. | HTTP或HTTPS监听不支持挂载主备服务器组。 |
| 400 | MissingParam.HealthCheckDomai n | The HealthCheckDomain is required when HealthCheckHttpVersion is http1.1. | 参数HealthCheckDomain缺失。 |
| 400 | InvalidParameter.HealthCheckHtt pVersion | The param HealthCheckHttpVersion is invalid. | 指定的HealthCheckHttpVersion无效。请检查参数约束， 并在修改后重试。 |
| 400 | QuotaLimitExceeds.AclAttachedT oListener | %s. | Acl绑定监听数已达到配额上限。 |
| 400 | QuotaLimitExceeds.TotalAclEntry | %s. | Acl条目数已达到配额上限。 |
| 400 | Duplicated.AclEntry | %s. | Acl条目重复。 |
| 400 | InvalidParameter.ForwardCode | The specified ForwardCode is invalid. | 指定的ForwardCode无效。请检查参数约束，并在修改后重试。 |

##### 7.5.3.3. DescribeLoadBalancerHTTPListenerAttribute

调用DescribeLoadBalancerHTTPListenerAttribute查询HTTP监听配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLoadBalancerHTTPLi stenerAttribute | 要执行的操作。 取值：DescribeLoadBalancerHTTPListenerAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1o94dp5**** | 负载均衡实例的ID。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ListenerPort | Integer | 80 | 负载均衡实例前端使用的端口。 |
| Bandwidth | Integer | -1 | 监听的带宽峰值，单位Mbps。取值： -1：不限制带宽峰值。 1~5120：监听的带宽峰值，所有监听的带宽峰值之和不能超过实例的带宽峰值。 说明该参数只适用于中国内地。 |
| Status | String | stopped | 当前监听的状态。取值： running：表示监听正常运行。 stopped：表示监听停止。 |

负载均衡

| XForwardedFor | String | on | 是否开启通过X-Forwarded-For的方式获取来访者真实IP。 取值：on或off。 |
|---|---|---|---|
| Scheduler | String | wrr | 调度算法。 取值：wrr、wlc或rr。 wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |
| StickySession | String | on | 是否开启会话保持。 取值：on或off（默认值）。 |
| StickySessionType | String | insert | Cookie的处理方式。 取值：insert或server。 insert：植入Cookie。 客户端第一次访问时，负载均衡会在返回请求中植入Cookie（即在HTTP或 HTTPS响应报文中插入ServerId），下次客户端携带此Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server：重写Cookie。 负载均衡发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。 说明当StickySession的值为on时，必须指定该参数。 |
| CookieTimeout | Integer | 500 | Cookie超时时间，单位：秒。 取值范围：1~86400。 |
| Cookie | String | B490B5EBF6F3CD402E515D22BC DA1598 | 服务器上配置的Cookie。长度为1~200个字符，支持ASCII英文字母和数字字符，但不能包含半角逗号（,）、半角分号（;）、空格或美元符号（$）这些符号。 |
| HealthCheck | String | on | 是否开启健康检查。 取值：on或off。 |
| HealthCheckDomain | String | www.example.com | 用于健康检查的域名。 |
| HealthCheckURI | String | /test/index.html | 用于健康检查的URI。 长度限制为1~80个字符，支持字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%），半角问号（?）、井号（#）和and (&）这些字符。 URL不能只为正斜线（/），但必须以正斜线（/）开头。 ) |
| HealthyThreshold | Integer | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。 取值范围： 2~10。 |
| UnhealthyThreshold | Integer | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。 取值范围：2~10。 |
| HealthCheckTimeout | Integer | 3 | 每次健康检查响应的最大超时间。单位：秒。取值范围：1~300。 |
| HealthCheckInterval | Integer | 5 | 健康检查的时间间隔，单位：秒。取值范围：1~50。 |
| HealthCheckHttpCode | String | http2xx _ | 健康检查正常的HTTP状态码，多个状态码用半角逗号（,）分割。取值：http _2xx（默认值）、http _3xx、http _4xx或http _5xx。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckConnectPort | Integer | 8080 | 健康检查的端口。 说明当HealthCheck值为on时才会有效。 |
| VServerGroupId | String | rsp-cige6j**** | 转发规则的目标服务器组ID。 |
| Gzip | String | on | 是否开启Gzip压缩，对特定文件类型进行压缩。 取值：on或off。 |

负载均衡

| AclId | String | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
|---|---|---|---|
| AclStatus | String | off | 是否开启访问控制功能。取值：on或off。 |
| AclType | String | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
| BackendServerPort | Integer | 80 | 负载均衡实例后端使用的端口。 |
| Description | String | test | HTTP监听描述。长度为1~80个字符，支持中文描述，以及字母、数字、短划线 （-）、正斜线（/）、半角句号（.）和下划线（_）等字符。 |
| ForwardPort | Integer | 80 | HTTP至HTTPS的监听转发端口。 说明如果ListenerForward的值为off，该参数不显示。 |
| IdleTimeout | Integer | 2 | 指定连接空闲超时时间，单位：秒。 取值范围：1~60，默认值：15。 在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到下一次请求来临时重新建立新的连接。 |
| ListenerForward | String | on | 表示是否开启HTTP至HTTPS的监听转发。 on：表示开启。 off：表示未开启。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |
| RequestTimeout | Integer | 34 | 指定请求超时时间，单位：秒。 取值范围：1~180，默认值：60。 在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504错误码。 |
| Rules | Array of Rule |  | 转发规则描述。 |
| Rule |  |  |  |
| Domain | String | www.example.com | 域名。 |
| RuleId | String | rule-xjsq****** | 转发规则ID。 |
| RuleName | String | example | 转发规则名称。 |
| Url | String | /example | 访问路径。 |
| VServerGroupId | String | rsp-bp****** | 转发规则的目标服务器组ID。 |
| SecurityStatus | String | on | 是否开启安全状态。 取值：on或off。 |
| XForwardedForSLBID _ | String | on | 是否通过 SLB-ID 头字段获取负载均衡实例ID。 |
| XForwardedForSLBIP _ | String | on | 是否通过 SLB-IP 头字段获取客户端请求的真实IP。 |
| XForwardedForproto _ | String | on | 是否通过 X-Forwarded-Proto 头字段获取负载均衡实例的监听协议。 |

**示例**

负载均衡请求示例

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5*********
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeLoadBalancerHTTPListenerAttributeResponse> <ForwardPort>443</ForwardPort> <ListenerPort>80</ListenerPort> <Status>stopped</Status> <RequestId>99439CEF-192C-4B01-A45A-2D5BD5BCDA62</RequestId> <ListenerForward>on</ListenerForward> </DescribeLoadBalancerHTTPListenerAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| {"CookieTimeout":"500","VServerGroupId":"rsp- cige6j****","Description":"test","UnhealthyThreshold":"4","HealthCheckURI":"/test/index.html","Scheduler":"wrr","HealthCheck":"on","IdleTimeout" "BackendServerPort":"80","XForwardedFor_SLBID":"on","HealthCheckConnectPort":"8080","SecurityStatus":"on","Bandwidth":"- 1","Gzip":"on","StickySessionType":"insert ","XForwardedFor_SLBIP":"on","HealthCheckHttpCode":"http_2xx","Cookie":"B490B5EBF6F3CD402E515D22BCDA1598","Status":"stopped","RequestTimeout":"3 istenerPort":"80","HealthCheckInterval":"5","RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710","AclId":"acl- bp1l0kk4gxce43kz******","HealthCheckTimeout":"3","Rules":[{"VServerGroupId":"rsp-bp******","RuleId":"rule- xjsq******","Domain":"www.example.com","Url":"/example","RuleName":"example"}],"ListenerForward":"on","StickySession":"on","ForwardPort":"80","A tus":"off","HealthyThreshold":"4","XForwardedFor":"on","HealthCheckDomain":"www.example.com","AclType":"white","XForwardedFor_proto":"on"} |  |

##### 7.5.3.4. CreateLoadBalancerHTTPListenerPro

调用CreateLoadBalancerHTTPListenerPro接口创建HTTP监听。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKeyId | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| Action | String | Query | 否 | CreateLoadBalancerHTTPListenerPro | 要执行的操作。取值： CreateLoadBalancerHTTPListenerPro。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| LoadBalancerId | String | Query | 是 | lb-bp1c9vixxjh92q83tw***** | 传统型负载均衡实例ID。 |
| Bandwidth | Integer | Query | 否 | -1 | 监听的带宽峰值，单位：Mbps。 -1：不限制带宽峰值。 1~5120：监听的带宽峰值，所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
| ListenerPort | Integer | Query | 是 | 80 | 实例前端使用的端口。 |
| BackendServerPort | Integer | Query | 否 | 80 | 实例后端使用的端口。 |
| XForwardedFor | String | Query | 否 | on | 是否开启通过X-Forwarded-For头字段获取来访客户端 IP。默认值为on。 on：是。 off：否。 |
| Scheduler | String | Query | 否 | wrr | 调度算法。 默认值是wrr。 wrr：权重值越高的后端服务器，被轮询到的概率也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |

| 开发指南·API参 | 考 |  |  |  | 负载均衡 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| StickySession | String | Query | 是 | off | 是否开启会话保持。默认值为off。 on：是。 off：否。 |
| StickySessionType | String | Query | 否 | insert | Cookie 处理方式。 insert：植入Cookie。客户端第一次访问时，负载均衡会在返回请求中植入 Cookie（即在HTTP或HTTPS响应报文中插入 ServerId），下次客户端携带此 Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server：重写Cookie。 |
| CookieTimeout | Integer | Query | 否 | 500 | Cookie超时时间。单位：秒。 |
| Cookie | String | Query | 否 | B490B5EBF6F3CD402E515D22BCDA1598 | 服务器上配置的Cookie。长度为 1~200 个字符，只能包含ASCII英文字母和数字字符，不能包含半角逗号（,）、半角分号（;）或空格，也不能以美元符号（$）开头。 |
| HealthCheck | String | Query | 是 | on | 是否开启健康检查。 on：开启健康检查。 off：不开启健康检查。 |
| HealthCheckMetho d | String | Query | 否 | head | 监听HTTP类型健康检查的健康检查方法。取值： head。 get。 默认值为head。 |
| HealthCheckDomai n | String | Query | 否 | 172.16.0.0/12 | 用于健康检查的域名。 $ _ip：后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。 domain：域名长度为1~80字符，只能包含字母、数字、半角句号（.）和短划线（-）。 |
| HealthCheckURI | String | Query | 否 | /test/index.html | 用于健康检查的 URI。长度限制为 1~80 个字符，只能使用字母、数字和短划线（-）、正斜线 （/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和 and（&）这些字符。 URI 不能只为正斜线（/），但必须以正斜线 （/）开头。 |
| HealthyThreshold | Integer | Query | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值：2~10。 |
| UnhealthyThreshol d | Integer | Query | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。取值：2~10。 |
| HealthCheckTimeo ut | Integer | Query | 否 | 3 | 接收来自运行状况检查的响应需要等待的时间。 如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。单位：秒。 |
| HealthCheckConne ctPort | Integer | Query | 否 | 80 | 健康检查的后端服务器的端口。 |
| HealthCheckInterv al | Integer | Query | 否 | 5 | 健康检查的时间间隔。单位：秒。 |
| HealthCheckHttpC ode | String | Query | 否 | http2xx _ | 健康检查正常的HTTP状态码，多个状态码用逗号分隔。取值： http _2xx（默认值）。 http _3xx。 http _4xx。 http _5xx。 |
| MaxConnection | Integer | Query | 否 | 5000 | 最大连接数。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| accesskeyid _ _ | String | Query | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |
|---|---|---|---|---|---|---|
| VServerGroupId | String | Query | 否 | rsp-cige6j***** | 虚拟服务器组ID。 |  |
| PpuName | String | Query | 否 | ppu-A-30cji12**** | ppu的名称。 |  |
| Tags | String | Query | 否 | {"tagKey":"Key1","tagValue":"Value1"} | 标签列表。 |  |
| XForwardedForSL _ BIP | String | Query | 否 | off | 是否通过SLB-IP头字段获取客户端请求的 VIP（Virtual IP address）。默认值为off。 on：是。 off：否。 |  |
| XForwardedForSL _ BID | String | Query | 否 | off | 是否通过SLB-ID头字段获取负载均衡实例ID。默认值为off。 on：是。 off：否。 |  |
| XForwardedForpro _ to | String | Query | 否 | off | 是否通过X-Forwarded-Proto头字段获取负载均衡实例的监听协议。默认值为off。 on：是。 off：否。 |  |
| Gzip | String | Query | 否 | on | 是否开启Gzip压缩，对特定文件类型进行压缩。 默认值为on。 on：是。 off：否。 |  |
| IdleTimeout | Integer | Query | 否 | 3 | 指定连接空闲超时时间。单位：秒。默认值为 15，取值范围：1~60。在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。 |  |
| RequestTimeout | Integer | Query | 否 | 6 | 指定请求超时时间。单位：秒。默认值为 60， 取值范围为 1~180。在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回HTTP 504错误码。 |  |
| ListenerForward | String | Query | 否 | off | 是否开启HTTP至HTTPS的转发。默认值为off。 on：是。 off：否。 |  |
| ForwardPort | Integer | Query | 否 | 443 | HTTP至HTTPS的监听转发端口。 |  |
| Description | String | Query | 否 | HTTP443 _ | 自定义监听名称。长度限制为1~256个字符，支持中文、字母、数字、短划线（-）、正斜线 （/）、半角句号（.）和下划线（_）。 |  |
| RegionId | String | Query | 否 | cn-hangzhou | 传统型负载均衡实例的地域ID。 |  |
| AclId | String | Query | 否 | 123 | 监听绑定的访问策略组ID。 |  |
| AclType | String | Query | 否 | white | 访问控制类型。 white：仅转发来自所选访问控制策略组中设置的 IP 地址或地址段的请求，白名单适用于只允许特定 IP 访问的场景。设置白名单存在一定业务风险。一旦设置白名单，就只有白名单中的 IP 可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何 IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的 IP 地址或地址段的所有请求都不会转发，黑名单适用于只限制某些特定 IP 访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何 IP，则负载均衡监听会转发全部请求。 |  |
| AclStatus | String | Query | 否 | off | 是否开启访问控制功能。默认值为off。 on：是。 off：否。 |  |

**返回数据**

负载均衡

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPListenerPro &LoadBalancerId=lb-bp1c9vixxjh92q83tw***** &ListenerPort=80 &StickySession=off &HealthCheck=on
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } |  |

| XML | 格式 |
|---|---|
| <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | REGIONNOTSUPPORTPARAMET _ _ _ ER | InvalidParameter.RegionNotSupport | The region does not support the parameter: %s. |
| 400 | IpVersionConflict | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. |
| 400 | InvalidFrontPortOrForwardPort | InvalidParameter | The specified ListenerPort or ForwardPort is invalid. |
| 400 | ListenerForwardNotSupport | ListenerForwardNotSupport | X-Forward-For is not supported to a ipv6 instance. |
| 400 | IdleTimeoutExceedsLimit | InvalidParameter.IdleTimeout | The specified IdleTimeout exceeds the limit. |
| 400 | RequestTimeoutExceedsLimit | InvalidParameter.RequestTimeout | The specified RequestTimeout exceeds the limit. |
| 400 | ListenerProcessing | ListenerProcessing | A previous configuration of the listener is pending,please try again later. |
| 400 | ListenerPortConflict | InvalidParameter.ListenerPortConflict | There is conflict listener port exists. |
| 400 | -2753 | ResourceNotAvailible.HttpListener | The specified Zone did not have enough resource. |
| 400 | -6002 | AclNotExist | Acl does not exist |
| 400 | OperationUnsupported.CreateLoa dBalancerListener | OperationUnsupported.CreateLoadBalancerLayer7Li stener | The slb instance does not support create HTTP or HTTPS listener. |
| 400 | MSVGROUPCANNOTSUPPORT _ _ _ _ SEVENLAYERPROTOCOL _ _ _ | InvalidParameter.VServerGroupId | The MasterSlaveServerGroup can not be attached to HTTP or HTTPS listener. |
| 400 | -2173 | MissingParam.HealthCheckDomain | The HealthCheckDomain is required when HealthCheckHttpVersion is http1.1. |
| 400 | InvalidParam.HealthCheckHttpVe rsion | InvalidParameter.HealthCheckHttpVersion | The param HealthCheckHttpVersion is invalid. |
| 400 | MissingParam.HealthCheckDomai n | MissingParam.HealthCheckDomain | The HealthCheckDomain is required when HealthCheckHttpVersion is http1.1. |
| 400 | QuotaLimitExceeds.AclAttachedT oVip | QuotaLimitExceeds.AclAttachedToListener | %s. |
| 400 | QuotaLimitExceeds.AclEntryTotal | QuotaLimitExceeds.TotalAclEntry | %s. |
| 400 | QuotaLimitExceeds.AclListenerOv erLimit | AclListenerOverLimit | %s. |
| 400 | Duplicated.AclEntry | Duplicated.AclEntry | %s. |
| 400 | -3237 | OperationFailed.InsufficientResources | The loadbalancer does not support this operation because of insufficient resources. |
| 400 | InvalidParam.ForwardCode | InvalidParameter.ForwardCode | The specified ForwardCode is invalid. |
| 400 | -5237 | ResourceNotAvailible.HttpListener | The specified Zone did not have enough resource. |
| 400 | LbNotSupportTcpssl | LbNotSupportTcpssl | You cannot create a TCP SSL type listener for the specified load balancer. |

| 负载均衡 |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | LbSupportTcpsslOnly | LbSupportTcpsslOnly | The specified load balancer supports TCP SSL type listener only. |
| 400 | ListenerNotSupportRule | ListenerNotSupportRule | You cannot create a rule for the specified listener. |
| 400 | Mismatch.SlbSpecTypeAndListen erProtocol | Mismatch.SlbSpecTypeAndListenerProtocol | The SlbSpecType and ListenerProtocol are mismatched. |

#### 7.5.4. HTTPS监听

##### 7.5.4.1. CreateLoadBalancerHTTPSListener

调用CreateLoadBalancerHTTPSListener创建HTTPS监听。

**说明**

新建的监听的状态为stopped。创建完成后，调用 `StartLoadBalancerListener` 接口启动监听来转发流量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateLoadBalancerHTTPSLis tener | 要执行的操作。 取值：CreateLoadBalancerHTTPSListener。 |
| Bandwidth | Integer | 是 | -1 | 监听的带宽峰值，单位：Mbps。取值： -1：对于按流量计费的公网负载均衡实例，可以将带宽峰值设置为- 1，即不限制带宽峰值。 1~5120：对于按带宽计费的公网负载均衡实例，可以设置每个监听的带宽峰值，但所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
| HealthCheck | String | 是 | on | 是否开启健康检查。 取值：on或off。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1o94dp5i6earr**** | 负载均衡实例ID。 |
| StickySession | String | 是 | on | 是否开启会话保持。 取值：on或off。 |
| BackendServerPort | Integer | 否 | 80 | 负载均衡实例后端使用的端口，取值范围：1~65535。 如果不使用服务器组（不指定VServerGroupId），则该参数必选。 |
| XForwardedFor | String | 否 | on | 是否通过 X-Forwarded-For 获取客户端请求的真实IP。 取值：on。 |
| Scheduler | String | 否 | wrr | 调度算法。取值： wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |
| StickySessionType | String | 否 | insert | Cookie的处理方式。取值： insert：植入Cookie。 客户端第一次访问时，负载均衡会在返回请求中植入Cookie（即在 HTTP或HTTPS响应报文中插入ServerId），下次客户端携带此 Cookie访问，负载均衡服务会将请求定向转发给之前记录的后端服务器。 server：重写Cookie。 负载均衡发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问时，负载均衡服务会将请求定向转发给之前记录的后端服务器。 说明当StickySession的值为on时，必须指定该参数。 |

负载均衡

| CookieTimeout | Integer | 否 | 500 | Cookie超时时间。单位：秒。 取值范围：1~86400。 说明当StickySession为on且StickySessionType为insert时， 该参数必选。 |
|---|---|---|---|---|
| Cookie | String | 否 | B490B5EBF6F3CD402E515D 22BCDA1598 | 服务器上配置的Cookie。 长度为1~200个字符，只能包含ASCII英文字母和数字字符，不能包含逗号（,）、分号（;）或空格，也不能以美元符号（$）开头。 说明当StickySession为on且StickySessionType为server时， 该参数必选。 |
| HealthCheckMethod | String | 否 | get | 监听HTTP类型健康检查的健康检查方法。取值：head或get。 说明 HealthCheck值为on时才会有效。 |
| HealthCheckDomain | String | 否 | 172.XX.XX.6 | 健康检查的域名。取值： $ _ip：后端服务器的私网IP。该参数未指定或指定了后端服务器的私网IP时，负载均衡会使用各后端服务器的私网IP作为健康检查的域名。 domain：长度为1~80个字符，只能包含字母、数字、英文句号 （.）和短划线（-）。 说明在HealthCheck值为on时有效。 |
| HealthCheckURI | String | 否 | /test/index.html | 用于健康检查的URI。 长度为1~80个字符，只能使用字母、数字和 -/.%?#&amp; 这些字符。 URL不能只为正斜线（/），但必须以正斜线（/）开头。 说明在HealthCheck值为on时有效。 |
| HealthyThreshold | Integer | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值范围：2~10。 说明在HealthCheck值为on时才会有效。 |
| UnhealthyThreshold | Integer | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。 取值范围：2~10。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckTimeout | Integer | 否 | 3 | 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。单位：秒。 取值范围：1~300。 如果HealthCHeckTimeout的值小于HealthCheckInterval的值，则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckConnectPort | Integer | 否 | 8080 | 健康检查使用的端口。 取值范围：1~65535。 说明当HealthCheck值为on时才会有效。 |
| HealthCheckInterval | Integer | 否 | 5 | 健康检查的时间间隔。单位：秒。 取值范围：1~50。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckHttpCode | String | 否 | http2xx _ | 健康检查正常的HTTP状态码，多个状态码用逗号（,）分割。默认值：http _2xx。 取值：http _2xx、http _3xx、http _4xx或http _5xx。 说明在HealthCheck值为on时才会有效。 |
| ServerCertificateId | String | 否 | idkp-123-cn-test-**** | 服务器证书ID。 |

负载均衡

| VServerGroupId | String | 否 | rsp-cige6j5e7p**** | 服务器组ID。 |
|---|---|---|---|---|
| CACertificateId | String | 否 | 139a00604ad-cn-east- hangzh**** | CA证书ID。 双向认证：同时上传CA证书和服务器证书。 单向认证：只上传服务器证书。 |
| XForwardedForSLBIP _ | String | 否 | on | 是否通过 SLB-IP 头字段获取来访者真实IP。 取值：on或off （默认值）。 |
| XForwardedForSLBID _ | String | 否 | on | 是否通过 SLB-ID 头字段获取SLB实例ID。 取值：on或off （默认值）。 |
| XForwardedForproto _ | String | 否 | on | 是否通过 X-Forwarded-Proto 头字段获取SLB的监听协议。 取值：on或off （默认值）。 |
| Gzip | String | 否 | on | 是否开启Gzip压缩，对特定文件类型进行压缩。 取值：on或off （默认值）。 |
| IdleTimeout | Integer | 否 | 12 | 指定连接空闲超时时间，取值范围为1~60秒，默认值为15秒。 在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。 |
| RequestTimeout | Integer | 否 | 23 | 指定请求超时时间，取值范围为1~180秒，默认值为60秒。 在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回HTTP 504错误码。 |
| TLSCipherPolicy | String | 否 | tlscipherpolicy11 _ _ _ _ | 只有性能保障型实例才可以指定TLSCipherPolicy参数，每种策略定义了一种安全策略，安全策略包含HTTPS可选的TLS协议版本和配套的加密算法套件。 目前支持以下四种安全策略，详细区别请参见TLS安全策略差异说明， 请根据实际情况选择对应的策略。 tls _cipher _policy _1 _0： 支持TLS版本： TLSv1.0、TLSv1.1和TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、 ECDHE-RSA-AES256-GCM-SHA384、ECDHE-RSA-AES128- SHA256、ECDHE-RSA-AES256-SHA384、AES128-GCM- SHA256、AES256-GCM-SHA384、AES128-SHA256、 AES256-SHA256、ECDHE-RSA-AES128-SHA、ECDHE-RSA- AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tls _cipher _policy _1 _1： 支持TLS版本： TLSv1.1和TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、 ECDHE-RSA-AES256-GCM-SHA384、ECDHE-RSA-AES128- SHA256、ECDHE-RSA-AES256-SHA384、AES128-GCM- SHA256、AES256-GCM-SHA384、AES128-SHA256、 AES256-SHA256、ECDHE-RSA-AES128-SHA、ECDHE-RSA- AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tlscipherpolicy12 _ _ _ _ 支持TLS版本：TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、 ECDHE-RSA-AES256-GCM-SHA384、ECDHE-RSA-AES128- SHA256、ECDHE-RSA-AES256-SHA384、AES128-GCM- SHA256、AES256-GCM-SHA384、AES128-SHA256、 AES256-SHA256、ECDHE-RSA-AES128-SHA、ECDHE-RSA- AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tlscipherpolicy12strict _ _ _ _ _ 支持TLS版本：TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、 ECDHE-RSA-AES256-GCM-SHA384、ECDHE-RSA-AES128- SHA256、ECDHE-RSA-AES256-SHA384、ECDHE-RSA- AES128-SHA和ECDHE-RSA-AES256-SHA。 |
| Description | String | 否 | 创建监听 | 监听描述信息。长度为1~80个字符，支持中文描述，以及字母、数字、短划线（-）、正斜线（/）、英文句号（.）和下划线（_）等字符。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclId | String | 否 | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |

负载均衡

| AclType | String | 否 | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
|---|---|---|---|---|
| AclStatus | String | 否 | off | 是否开启访问控制功能。取值： 取值：on或off （默认值）。 |
| EnableHttp2 | String | 否 | off | 是否开启HTTP2特性。 取值：on或off（默认值）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPSListener &Bandwidth=-1 &HealthCheck=on &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5i6earr***** &StickySession=on
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateLoadBalancerHTTPSListenerResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </CreateLoadBalancerHTTPSListenerResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertSubjectDNAlias is _ duplicate. Please change to a different one. | 参数XForwardedFor _ClientCertSubjectDNAlias重复。 |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertIssuerDNAlias is duplicate. _ Please change to a different one. | 参数XForwardedFor _ClientCertIssuerDNAlias重复。 |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertFingerprintAlias is _ duplicate. Please change to a different one. | 参数XForwardedFor _ClientCertFingerprintAlias重复。 |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertClientVerifyAlias is _ duplicate. Please change to a different one. | 参数XForwardedFor _ClientCertClientVerifyAlias重复。 |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | 指定负载均衡的IP版本与ACL支持的IP类型冲突。 |
| 400 | InvalidParameter.IdleTimeout | The specified IdleTimeout exceeds the limit. | 指定的IdleTimeout无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParameter.RequestTimeou t | The specified RequestTimeout exceeds the limit. | 指定的RequestTimeout无效。请检查参数约束，并在修改后重试。 |
| 400 | ListenerForwardNotSupport | X-Forward-For is not supported to a ipv6 instance. | Ipv6负载均衡实例不支持X-Forward-For。 |
| 400 | InvalidParameter.RegionNotSupp ort | The region does not support the parameter: %s. | 当前区域不支持指定参数。 |

负载均衡

| 400 | InvalidParameter.SpecNotSupport | The loadBalancer of shared spec does not support the parameter: %s. | 共享型负载均衡实例不支持当前参数。 |
|---|---|---|---|
| 400 | ListenerProcessing | A previous configuration of the listener is pending,please try again later. | 当前监听正在配置中，请稍后重试。 |
| 400 | Certkey.Forbidden | The specified certkey is not owned by the current user. | 指定的certkey不属于当前用户。 |
| 400 | InvalidParameter.ListenerPortCon flict | There is conflict listener port exists. | 指定的监听端口已存在。 |
| 400 | ResourceNotAvailible.HttpsListen er | The specified Zone did not have enough resource. | 指定可用区资源不足。 |
| 400 | OperationUnsupported.CreateLoa dBalancerLayer7Listener | The slb instance does not support create HTTP or HTTPS listener. | 当前负载均衡实例不支持创建Http或者Https类型的监听。 |
| 400 | InvalidParameter.VServerGroupId | The MasterSlaveServerGroup can not be attached to HTTP or HTTPS listener. | HTTP或HTTPS监听不支持挂载主备服务器组。 |
| 400 | MissingParam.HealthCheckDomai n | The HealthCheckDomain is required when HealthCheckHttpVersion is http1.1. | 参数HealthCheckDomain缺失。 |
| 400 | InvalidParameter.HealthCheckHtt pVersion | The param HealthCheckHttpVersion is invalid. | 指定的HealthCheckHttpVersion无效。请检查参数约束， 并在修改后重试。 |
| 400 | QuotaLimitExceeds.AclAttachedT oListener | %s. | Acl绑定监听数已达到配额上限。 |
| 400 | QuotaLimitExceeds.TotalAclEntry | %s. | Acl条目数已达到配额上限。 |
| 400 | Duplicated.AclEntry | %s. | Acl条目重复。 |
| 400 | CertificateNotExist | The specified CertificateId does not exist. | 指定的证书不存在。 |
| 400 | OperationFailed.InsufficientResou rces | The loadbalancer does not support this operation because of insufficient resources. | 操作失败，原因是由于资源不足，负载均衡器不支持此操作。 |
| 400 | InvalidTLSPolicyId.NotExist | The specified TLS cipher policy does not exist. | 指定的TLS策略不存在。 |
| 400 | TLSPolicyConfiguring | The specified TLS cipher policy is configuring. | 指定的TLSCipherPolicy正在变配中。 |
| 400 | TLSCipherPolicyVipRelationOverLi mit | The number of listeners associated with a policy has exceeded. | 监听关联TLSCipherPolicy的数量已达到配额上限。 |
| 400 | CertificateTypeMismatched | The certificate type does not match. | 指定证书的类型不匹配。 |
| 400 | MissingParam.ServerCertificates | Server certificates are required. | 参数ServerCertificates缺失。 |
| 400 | TooManyCertificates | The number of certificates must not be greater than one. | 证书的数量不得大于1个。 |
| 400 | CnCertificateNotSupport | The cn certificate is not support. | 不支持国密证书。 |
| 400 | InvalidParam.CertificateBindingTy pe | The param CertificateBindingType is invalid. | 指定的CertificateBindingType无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParamSize.ServerCertificat es | The size of param ServerCertificates is invalid. | 指定的ServerCertificates长度无效。请检查参数约束，并在修改后重试。 |
| 400 | TooManyCertificates.ServerCertifi cates | The number of certificates must not be greater than one. | 证书的数量不得大于1个。 |
| 400 | LbNotSupportTcpssl | You cannot create a TCP SSL type listener for the specified load balancer. | 指定的实例不支持创建tcpssl类型的监听。 |
| 400 | LbSupportTcpsslOnly | The specified load balancer supports TCP SSL type listener only. | 指定的实例只支持创建tcpssl类型的监听。 |
| 400 | ListenerNotSupportRule | You cannot create a rule for the specified listener. | 指定的监听不支持创建转发规则。 |
| 400 | Mismatch.SlbSpecTypeAndListen erProtocol | The SlbSpecType and ListenerProtocol are mismatched. | 实例规格类型和监听类型不匹配。 |

##### 7.5.4.2. SetLoadBalancerHTTPSListenerAttribute

调用SetLoadBalancerHTTPSListenerAttribute修改HTTPS监听的配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetLoadBalancerHTTPSListen erAttribute | 要执行的操作。 取值：SetLoadBalancerHTTPSListenerAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-sjhfdji**** | 负载均衡实例的ID。 |

负载均衡

| Bandwidth | Integer | 否 | -1 | 监听的带宽峰值。单位：Mbps。取值： -1：不限制带宽峰值。 1~5120：监听的带宽峰值，所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
|---|---|---|---|---|
| XForwardedFor | String | 否 | on | 是否开启通过X-Forwarded-For头字段获取客户真实IP。 取值：on或off。 |
| Scheduler | String | 否 | wrr | 调度算法。取值： wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |
| StickySession | String | 否 | on | 是否开启会话保持。 取值：on或off。 |
| StickySessionType | String | 否 | insert | Cookie的处理方式。取值： insert：植入Cookie。 客户端第一次访问时，负载均衡会在返回请求中植入Cookie（即在 HTTP或HTTPS响应报文中插入ServerId），下次客户端携带此 Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server：重写Cookie。 负载均衡发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。 说明当StickySession的值为on时，必须指定该参数。 |
| CookieTimeout | Integer | 否 | 500 | Cookie超时时间。单位：秒。 取值范围：1~86400。 说明当StickySession为on且StickySessionType为insert时， 该参数必选。 |
| Cookie | String | 否 | B490B5EBF6F3CD402E515D 22BCDA1598 | 服务器上配置的Cookie。 长度为1~200个字符，支持ASCII英文字母和数字字符，但不能包含半角逗号（,）、半角分号（;）、空格或美元符号（$）这些符号。 说明当StickySession为on且StickySessionType为server时， 该参数必选。 |
| HealthCheck | String | 否 | on | 是否开启健康检查。 取值：on或off。 |
| HealthCheckMethod | String | 否 | get | 监听HTTP类型健康检查的健康检查方法。 取值：head或get。 说明 HealthCheck值为on时才会有效。 |
| HealthCheckDomain | String | 否 | 172.16.6.6 | 用于健康检查的域名，取值： $ _ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。 domain：域名长度为1~80字符，只能包含字母、数字、半角句号 （.）和短划线（-）。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckURI | String | 否 | /test/index.html | 用于健康检查的URI。 长度限制为1~80，只能使用字母、数字、短划线（-）、正斜线（/）、 半角句号（.）、百分号（%）、半角问号（?）、井号（#）和 and（&）字符。 URL不能只为正斜线（/），但必须以正斜线（/）开头。 说明在HealthCheck值为on时才会有效。 |

负载均衡

| HealthyThreshold | Integer | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功。 取值范围：2~10。 说明在HealthCheck值为on时才会有效。 |
|---|---|---|---|---|
| UnhealthyThreshold | Integer | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败。 取值范围：2~10。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckTimeout | Integer | 否 | 3 | 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。单位：秒。 取值范围：1~300。 说明如果HealthCHeckTimeout的值小于HealthCheckInterval的值， 则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。 在HealthCheck值为on时才会有效。 |
| HealthCheckInterval | Integer | 否 | 5 | 健康检查的时间间隔。单位：秒。 取值范围：1~50。 说明在HealthCheck值为on时才会有效。 |
| HealthCheckConnectPort | Integer | 否 | 8080 | 健康检查使用的端口。 取值范围：1~65535。 说明当HealthCheck值为on时才会有效。 |
| HealthCheckHttpCode | String | 否 | http2xx,http3xx _ _ | 健康检查正常的HTTP状态码，多个状态码用半角逗号（,）分割。 取值：http _2xx、http _3xx、http _4xx或http _5xx。 说明在HealthCheck值为on时才会有效。 |
| ServerCertificateId | String | 否 | idkp-123-cn-te**** | 服务器证书的ID。 |
| CACertificateId | String | 否 | 139a00604ad-cn-east-**** | CA证书ID。 若既上传CA证书又上传服务器证书，即采用双向认证。 若用户只上传服务器证书，即为单向认证。 |
| VServerGroup | String | 否 | on | 是否使用服务器组。 取值：on或off。 |
| VServerGroupId | String | 否 | rsp-cige6j**** | 虚拟服务器组ID。 |
| Tags | String | 否 | loadbalancerhttps**** | 标签。 |
| XForwardedForSLBIP _ | String | 否 | on | 是否通过 SLB-IP 头字段获取客户端请求的真实IP。 取值：on或off。 |
| XForwardedForSLBID _ | String | 否 | on | 是否通过 SLB-ID 头字段获取负载均衡实例ID。 取值：on或off。 |
| XForwardedForproto _ | String | 否 | on | 是否通过 X-Forwarded-Proto 头字段获取负载均衡实例的监听协议。 取值：on或off。 |
| Gzip | String | 否 | on | 是否开启Gzip压缩，对特定文件类型进行压缩。 取值：on或off。 |
| IdleTimeout | Integer | 否 | 23 | 指定连接空闲超时时间。单位：秒。 取值范围为1~60，默认值：15。 在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。 |

负载均衡

| RequestTimeout | Integer | 否 | 60 | 指定请求超时时间。单位：秒。 取值范围：1~180，默认值：60。 在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回HTTP 504错误码。 |
|---|---|---|---|---|
| TLSCipherPolicy | String | 否 | tlscipherpolicy12 _ _ _ _ | 只有性能保障型实例才可以指定TLSCipherPolicy参数，每种策略定义了一种安全策略，安全策略包含HTTPS可选的TLS协议版本和配套的加密算法套件。 目前支持以下四种安全策略，请根据实际情况选择对应的policy。 tls _cipher _policy _1 _0： 支持TLS版本： TLSv1.0、TLSv1.1和TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、 ECDHE-RSA-AES256-GCM-SHA384、ECDHE-RSA-AES128- SHA256、ECDHE-RSA-AES256-SHA384、AES128-GCM- SHA256、AES256-GCM-SHA384、AES128-SHA256、 AES256-SHA256、ECDHE-RSA-AES128-SHA、ECDHE-RSA- AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tls _cipher _policy _1 _1： 支持TLS版本： TLSv1.1和TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、 ECDHE-RSA-AES256-GCM-SHA384、ECDHE-RSA-AES128- SHA256、ECDHE-RSA-AES256-SHA384、AES128-GCM- SHA256、AES256-GCM-SHA384、AES128-SHA256、 AES256-SHA256、ECDHE-RSA-AES128-SHA、ECDHE-RSA- AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tlscipherpolicy12 _ _ _ _ 支持TLS版本：TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、 ECDHE-RSA-AES256-GCM-SHA384、ECDHE-RSA-AES128- SHA256、ECDHE-RSA-AES256-SHA384、AES128-GCM- SHA256、AES256-GCM-SHA384、AES128-SHA256、 AES256-SHA256、ECDHE-RSA-AES128-SHA、ECDHE-RSA- AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tlscipherpolicy12strict _ _ _ _ _ 支持TLS版本：TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、 ECDHE-RSA-AES256-GCM-SHA384、ECDHE-RSA-AES128- SHA256、ECDHE-RSA-AES256-SHA384、ECDHE-RSA- AES128-SHA和ECDHE-RSA-AES256-SHA。 |
| Description | String | 否 | 监听描述 | 监听描述。长度为2~256个字符，必须是中文和以下字符串中的字符： ^([^\x00-\xff]\|[\w.,;/@-]){2,256}$ 。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclId | String | 否 | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
| AclType | String | 否 | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
| AclStatus | String | 否 | off | 是否开启访问控制功能。取值： 取值：on或off。 |
| EnableHttp2 | String | 否 | off | 是否开启HTTP2特性。取值： 取值：on或off。 |

**返回数据**

负载均衡

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-sjhfdji****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetLoadBalancerHTTPSListenerAttributeResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </SetLoadBalancerHTTPSListenerAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertSubjectDNAlias is _ duplicate. Please change to a different one. | 参数XForwardedFor _ClientCertSubjectDNAlias重复。 |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertIssuerDNAlias is duplicate. _ Please change to a different one. | 参数XForwardedFor _ClientCertIssuerDNAlias重复。 |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertFingerprintAlias is _ duplicate. Please change to a different one. | 参数XForwardedFor _ClientCertFingerprintAlias重复。 |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertClientVerifyAlias is _ duplicate. Please change to a different one. | 参数XForwardedFor _ClientCertClientVerifyAlias重复。 |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | 指定负载均衡的IP版本与ACL支持的IP类型冲突。 |
| 400 | InvalidParameter.IdleTimeout | The specified IdleTimeout exceeds the limit. | 指定的IdleTimeout无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParameter.RequestTimeou t | The specified RequestTimeout exceeds the limit. | 指定的RequestTimeout无效。请检查参数约束，并在修改后重试。 |
| 400 | ListenerForwardNotSupport | X-Forward-For is not supported to a ipv6 instance. | Ipv6负载均衡实例不支持X-Forward-For。 |
| 400 | InvalidParameter.RegionNotSupp ort | The region does not support the parameter: %s. | 当前区域不支持指定参数。 |
| 400 | InvalidParameter.SpecNotSupport | The loadBalancer of shared spec does not support the parameter: %s. | 共享型负载均衡实例不支持当前参数。 |
| 400 | OperationFailed.ServerGroupInUs e | The VServerGroup or MasterSlaveServerGroup can not be close for this listener. | 操作失败，原因是当前监听不支持关闭服务器组。 |
| 400 | InvalidParameter.VServerGroupId | The MasterSlaveServerGroup can not be attached to HTTP or HTTPS listener. | HTTP或HTTPS监听不支持挂载主备服务器组。 |
| 400 | MissingParam.HealthCheckDomai n | The HealthCheckDomain is required when HealthCheckHttpVersion is http1.1. | 参数HealthCheckDomain缺失。 |
| 400 | InvalidParameter.HealthCheckHtt pVersion | The param HealthCheckHttpVersion is invalid. | 指定的HealthCheckHttpVersion无效。请检查参数约束， 并在修改后重试。 |
| 400 | QuotaLimitExceeds.AclAttachedT oListener | %s. | Acl绑定监听数已达到配额上限。 |
| 400 | QuotaLimitExceeds.TotalAclEntry | %s. | Acl条目数已达到配额上限。 |
| 400 | Duplicated.AclEntry | %s. | Acl条目重复。 |
| 400 | CertificateNotExist | The specified CertificateId does not exist. | 指定的证书不存在。 |
| 400 | InvalidTLSPolicyId.NotExist | The specified TLS cipher policy does not exist. | 指定的TLS策略不存在。 |
| 400 | TLSPolicyConfiguring | The specified TLS cipher policy is configuring. | 指定的TLSCipherPolicy正在变配中。 |
| 400 | TLSCipherPolicyVipRelationOverLi mit | The number of listeners associated with a policy has exceeded. | 监听关联TLSCipherPolicy的数量已达到配额上限。 |

负载均衡

| 400 | TooManyCertificates | The number of certificates must not be greater than one. | 证书的数量不得大于1个。 |
|---|---|---|---|
| 400 | CertificateTypeMismatched | The certificate type does not match. | 指定证书的类型不匹配。 |
| 400 | MissingParam.ServerCertificates | Server certificates are required. | 参数ServerCertificates缺失。 |
| 400 | CnCertificateNotSupport | The cn certificate is not support. | 不支持国密证书。 |
| 400 | InvalidParam.CertificateBindingTy pe | The param CertificateBindingType is invalid. | 指定的CertificateBindingType无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParamSize.ServerCertificat es | The size of param ServerCertificates is invalid. | 指定的ServerCertificates长度无效。请检查参数约束，并在修改后重试。 |
| 400 | TooManyCertificates.ServerCertifi cates | The number of certificates must not be greater than one. | 证书的数量不得大于1个。 |

##### 7.5.4.3. DescribeLoadBalancerHTTPSListenerAttribute

调用DescribeLoadBalancerHTTPSListenerAttribute查询HTTPS监听配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLoadBalancerHTTPS ListenerAttribute | 要执行的操作。 取值：DescribeLoadBalancerHTTPSListenerAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值范围：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1mxu5r8lau**** | 负载均衡实例ID。 |
| RegionId | String | 是 | cn-east-hangzhou-01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ListenerPort | Integer | 80 | 负载均衡实例前端使用的端口。 |
| BackendServerPort | Integer | 80 | 负载均衡实例后端使用的端口。 |
| Bandwidth | Integer | -1 | 监听的带宽峰值。单位Mbps。取值： -1：不限制带宽峰值。 1~5120：监听的带宽峰值，所有监听的带宽峰值之和不能超过实例的带宽峰值。 |
| Status | String | stopped | 当前监听的状态。取值： running：运行中。 stopped：已停止。 |
| XForwardedFor | String | on | 是否开启通过X-Forwarded-For的方式获取来客户真实IP。 取值：on或off。 |
| Scheduler | String | wrr | 调度算法。取值： wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 |
| StickySession | String | on | 是否开启会话保持。 取值：on或off。 |

负载均衡

| StickySessionType | String | insert | Cookie的处理方式。取值： insert：植入Cookie。 客户端第一次访问时，负载均衡会在返回请求中植入Cookie（即在HTTP或 HTTPS响应报文中插入ServerId），下次客户端携带此Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server：重写Cookie。 负载均衡发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。 说明当StickySession的值为on时，必须指定该参数。 |
|---|---|---|---|
| CookieTimeout | Integer | 500 | Cookie超时时间，单位：秒。 取值范围：1~86400。 |
| Cookie | String | B490B5EBF6F3CD402E515D22BC DA1598 | 服务器上配置的Cookie。 |
| HealthCheck | String | on | 是否开启健康检查。 取值：on或off。 |
| HealthCheckDomain | String | www.example.com | 用于健康检查的域名。 |
| HealthCheckURI | String | /test/index.html | 用于健康检查的URI。 长度限制为1~80，只能使用字母、数字和短划线（-）、正斜线（/）、半角句号 （.）、百分号（%）、半角问号（?）、井号（#）和and（&）这些字符。 URL 不能只为正斜线（/），但必须以正斜线（/）开头。 |
| HealthyThreshold | Integer | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。 取值范围： 2~10。 |
| UnhealthyThreshold | Integer | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。 取值范围：2~10。 |
| HealthCheckTimeout | Integer | 3 | 每次健康检查响应的最大超时间，单位为秒。 |
| HealthCheckInterval | Integer | 5 | 健康检查的时间间隔，单位：秒。 取值范围：1~50。 |
| HealthCheckHttpCode | String | http2xx _ | 健康检查正常的HTTP状态码。多个状态码用逗号分割。取值：http _2xx（默认值）、http _3xx、http _4xx或http _5xx。 |
| HealthCheckConnectPort | Integer | 8080 | 健康检查的端口。 说明当HealthCheck值为on时才会有效。 |
| ServerCertificateId | String | idkp-123-cn-test-**** | 服务器证书ID。 |
| CACertificateId | String | idkp-234-cn-test-**** | CA证书ID。 |
| VServerGroupId | String | rsp-cige6j5e**** | 绑定的服务器组ID。 |
| Gzip | String | on | 是否开启Gzip压缩。 取值：on或off。 |
| AclId | String | acl-bp1l0kk4gxce43kz****** | 监听绑定的访问策略组ID。 当AclStatus参数的值为on时，该参数必选。 |
| AclStatus | String | off | 是否开启访问控制功能。取值： 取值：on或off。 |

负载均衡

| AclType | String | white | 访问控制类型，取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求，白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险，一旦设置白名单，就只有白名单中的IP可以访问负载均衡监听。 如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发，黑名单适用于应用只限制某些特定IP访问的场景。 如果开启了黑名单访问，但访问策略组中没有添加任何IP，则负载均衡监听会转发全部请求。 说明当AclStatus参数的值为on时，该参数有效。 |
|---|---|---|---|
| Description | String | 监听描述 | 监听描述信息。长度限制为1~80个字符，支持英文字母、中文、数字、短划线 （-）、正斜线（/）、半角句号（.）和下划线（_）等字符。 |
| DomainExtensions | Array of DomainExtension |  | 域名扩展列表。 |
| DomainExtension |  |  |  |
| Domain | String | www.example.com | 扩展域名。 |
| DomainExtensionId | String | 1243**** | 域名扩展ID。 |
| ServerCertificateId | String | 13344444**** | 与域名对应的证书ID。 |
| EnableHttp2 | String | off | 是否开启HTTP2特性。 取值：on或off。 |
| IdleTimeout | Integer | 23 | 指定连接空闲超时时间，单位：秒。 取值范围：1~60，默认值：15。 在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |
| RequestTimeout | Integer | 43 | 指定请求超时时间，单位：秒。 取值范围：1~180，默认值：60。 在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504错误码。 |
| Rules | Array of Rule |  | 监听下的转发规则列表。 |
| Rule |  |  |  |
| Domain | String | www.example.com | 转发规则域名。 |
| RuleId | String | rule-48772**** | 转发规则ID。 |
| RuleName | String | example | 转发规则名称。 |
| Url | String | /example | 访问路径。 |
| VServerGroupId | String | rsp-1287****** | 转发规则的目标服务器组ID。 |
| SecurityStatus | String | on | 安全状态。 取值：on或off。 |

负载均衡

| TLSCipherPolicy | String | tlscipherpolicy10 _ _ _ _ | 只有性能保障型实例才可以指定TLSCipherPolicy参数，每种策略定义了一种安全策略，安全策略包含HTTPS可选的TLS协议版本和配套的加密算法套件。 目前支持以下四种安全策略，详细区别请参见TLS安全策略差异说明。请根据实际情况选择对应的policy。 tls _cipher _policy _1 _0： 支持TLS版本： TLSv1.0、TLSv1.1和TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA- AES256-GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA- AES256-SHA384、AES128-GCM-SHA256、AES256-GCM-SHA384、 AES128-SHA256、AES256-SHA256、ECDHE-RSA-AES128-SHA、 ECDHE-RSA-AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tls _cipher _policy _1 _1： 支持TLS版本： TLSv1.1和TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA- AES256-GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA- AES256-SHA384、AES128-GCM-SHA256、AES256-GCM-SHA384、 AES128-SHA256、AES256-SHA256、ECDHE-RSA-AES128-SHA、 ECDHE-RSA-AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tlscipherpolicy12 _ _ _ _ 支持TLS版本：TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA- AES256-GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA- AES256-SHA384、AES128-GCM-SHA256、AES256-GCM-SHA384、 AES128-SHA256、AES256-SHA256、ECDHE-RSA-AES128-SHA、 ECDHE-RSA-AES256-SHA、AES128-SHA、AES256-SHA和DES-CBC3- SHA。 tlscipherpolicy12strict _ _ _ _ _ 支持TLS版本：TLSv1.2。 支持加密算法套件：ECDHE-RSA-AES128-GCM-SHA256、ECDHE-RSA- AES256-GCM-SHA384、ECDHE-RSA-AES128-SHA256、ECDHE-RSA- AES256-SHA384、ECDHE-RSA-AES128-SHA和ECDHE-RSA-AES256- SHA。 |
|---|---|---|---|
| XForwardedForClientCert _ ClientVerify | String | off | 是否通过 XForwardedFor_ClientCertClientVerify 头字段获取对访问负载均衡实例客户端证书的校验结果。 取值：on或off。 |
| XForwardedForClientCert _ Fingerprint | String | off | 是否通过 XForwardedFor_ClientCertFingerprint 头字段获取访问负载均衡实例客户端证书的指纹。 取值：on或off。 |
| XForwardedForClientCert _ IssuerDN | String | off | 是否通过 XForwardedFor_ClientCertIssuerDN 头字段获取访问负载均衡实例客户端证书的发行者信息。 取值：on或off。 |
| XForwardedForClientCert _ SubjectDN | String | off | 是否通过 XForwardedFor_ClientCertSubjectDN 头字段获取访问负载均衡实例客户端证书的所有者信息。 取值：on或off。 |
| XForwardedForClientSrcP _ ort | String | off | 是否通过 XForwardedFor_ClientSrcPort 头字段获取访问负载均衡实例客户端的端口。 取值：on或off。 |
| XForwardedForSLBID _ | String | on | 是否通过 SLB-ID 头字段获取负载均衡实例ID。 取值：on或off。 |
| XForwardedForSLBIP _ | String | on | 是否通过 SLB-IP 头字段获取客户端请求的真实IP。 取值：on或off。 |
| XForwardedForSLBPORT _ | String | off | 是否通过 XForwardedFor_SLBPORT 头字段获取负载均衡实例的监听端口。 取值：on或off。 |
| XForwardedForproto _ | String | on | 是否通过 X-Forwarded-Proto 头字段获取负载均衡实例的监听协议。 取值：on或off。 |

**示例**

请求示例负载均衡

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1mxu5r8lau*******
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeLoadBalancerHTTPSListenerAttributeResponse> <RequestId>11F52428-64ED-40F7-98C2-DBB6D0BB0AD7</RequestId> <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode> <HealthCheckTimeout>5</HealthCheckTimeout> <ServerCertificateId>1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746</ServerCertificateId> <XForwardedFor_SLBID>off</XForwardedFor_SLBID> <Gzip>on</Gzip> <HealthyThreshold>3</HealthyThreshold> <Scheduler>wrr</Scheduler> <StickySession>off</StickySession> <UnhealthyThreshold>3</UnhealthyThreshold> <XForwardedFor_SLBIP>off</XForwardedFor_SLBIP> <XForwardedFor_proto>off</XForwardedFor_proto> <Bandwidth>-1</Bandwidth> <HealthCheckURI>/</HealthCheckURI> <VServerGroupId>rsp-0xiju72x******</VServerGroupId> <HealthCheck>on</HealthCheck> <ListenerPort>443</ListenerPort> <Status>running</Status> <XForwardedFor>on</XForwardedFor> <HealthCheckDomain></HealthCheckDomain> <HealthCheckInterval>2</HealthCheckInterval> <BackendServerPort>443</BackendServerPort> </DescribeLoadBalancerHTTPSListenerAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "11F52428-64ED-40F7-98C2-DBB6D0BB0AD7", "HealthCheckHttpCode": "http_2xx,http_3xx", "HealthCheckTimeout": 5, "ServerCertificateId": "1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746", "XForwardedFor_SLBID": "off", "Gzip": "on", "HealthyThreshold": 3, "Scheduler": "wrr", "StickySession": "off", "UnhealthyThreshold": 3, "XForwardedFor_SLBIP": "off", "XForwardedFor_proto": "off", "Bandwidth": -1, "HealthCheckURI": "/", "VServerGroupId": "rsp-0xiju72x******", "HealthCheck": "on", "ListenerPort": 443, "Status": "running", "XForwardedFor": "on", "HealthCheckDomain": "", "HealthCheckInterval": 2, "BackendServerPort": 443 } |  |

##### 7.5.4.4. DescribeHealthStatus

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeHealthStatus | 要执行的操作。 取值：DescribeHealthStatus。 |
| LoadBalancerId | String | 是 | lb-bp1qjwo61pqz3ah**** | 负载均衡实例ID。 |
| ListenerPort | Integer | 否 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535 说明不设置该参数表示获取所有端口的健康检查状态。 |
| RegionId | String | 是 | cn-hangzhou | 负载均衡实例的地域ID。 |

负载均衡

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | i-bp1h5u3fv54ytf**** | ECS实例ID或者ENI实例ID。 |
| ServerHealthStatus | String | abnormal | 后端服务器的健康状况。 normal：后端服务器健康。 abnormal：后端服务器不健康。 unavailable：未完成健康检查。 |
| ListenerPort | Integer | 80 | 负载均衡实例前端使用的端口。 |
| port | Integer | 80 |  |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeHealthStatus &LoadBalancerId=lb-bp1qjwo61pqz3ah****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeHealthStatusResponse> <RequestId>E69BA4CE-2B55-45EC-94CA-E47B16759459</RequestId> <BackendServers> <BackendServer> <ListenerPort>80</ListenerPort> <ServerId>i-bp1h5u3fv54ytf0******</ServerId> <Port>80</Port> <ServerIp>192.168.0.**</ServerIp> <ServerHealthStatus>abnormal</ServerHealthStatus> <Protocol>http</Protocol> </BackendServer> <BackendServer> <ListenerPort>8080</ListenerPort> <ServerId>i-bp1h5u3fv54ytf0******</ServerId> <Port>80</Port> <ServerIp>192.168.0.**</ServerIp> <ServerHealthStatus>abnormal</ServerHealthStatus> <Protocol>tcp</Protocol> </BackendServer> </BackendServers> </DescribeHealthStatusResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "E69BA4CE-2B55-45EC-94CA-E47B16759459", "BackendServers": { "BackendServer": [ { "ListenerPort": 80, "ServerId": "i-bp1h5u3fv54ytf*****", "Port": 80, "ServerIp": "192.168.**.**", "ServerHealthStatus": "abnormal", "Protocol": "http" }, { "ListenerPort": 8080, "ServerId": "i-bp1h5u3fv54ytf0******", "Port": 80, "ServerIp": "192.168.**.**", "ServerHealthStatus": "abnormal", "Protocol": "tcp" } ] } } |  |

负载均衡

#### 7.5.5. 访问控制

##### 7.5.5.1. SetListenerAccessControlStatus

调用SetListenerAccessControlStatus是否开启指定监听的白名单访问控制。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetListenerAccessControlStat us | 要执行的操作。 取值：SetListenerAccessControlStatus。 |
| AccessControlStatus | String | 是 | openwhitelist _ _ | 是否开启访问控制。取值： open _white _list：开启白名单访问控制。 close：关闭白名单访问控制。 说明如果开启访问控制后，没有设置白名单则无法访问负载均衡服务。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08ex**** | 负载均衡实例的ID。 |
| accesskeyid _ _ | String | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | 否 | {"tagKey":"Key1","tagValue": "Value1"} | 标签键和值。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetListenerAccessControlStatus &AccessControlStatus=open_white_list &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetListenerAccessControlStatusResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </SetListenerAccessControlStatusResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |  |

##### 7.5.5.2. DescribeListenerAccessControlAttribute

调用DescribeListenerAccessControlAttribute查询监听的白名单配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeListenerAccessContr olAttribute | 要执行的操作。 取值：DescribeListenerAccessControlAttribute。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | lb-8vb86hxixo8*******6jaz | 负载均衡实例ID。 |
| Tags | String | 否 | listeneraccesscontrolslb**** | 标签。 |

负载均衡

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AccessControlStatus | String | openwhitelist _ _ | 是否开启访问控制： open _white _list：开启白名单访问控制功能。 close：关闭访问控制功能。 |
| SourceItems | String | 192.168.0.1 | 访问控制列表。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeListenerAccessControlAttribute &ListenerPort=80 &LoadBalancerId=lb-8vb86hxixo8*******6jaz
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeListenerAccessControlAttributeResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <AccessControlStatus>open_white_list</AccessControlStatus> <SourceItems>192.168.0.1</SourceItems> </DescribeListenerAccessControlAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| {"AccessControlStatus":"open_white_list", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "SourceItems":"192.168.0.1"} |  |

##### 7.5.5.3. AddListenerWhiteListItem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AddListenerWhiteListItem | 要执行的操作。 取值：AddListenerWhiteListItem。 |
| ListenerPort | Integer | 是 | 80 | 负载均衡实例前端使用的端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | 139a00604ad-cn-east- hangzhou-01 | 负载均衡实例ID。 |
| SourceItems | String | 是 | 1.XX.XX.1,1.XX.XX.0/21 | 访问控制列表。 监听的AccessControlStatus为open _white _list时有效。 支持输入IP地址或IP地址段（CIDR block形式），多个IP地址或地址段用半角逗号（,）分隔。 不允许输入0.0.0.0或0.0.0.0/0。您可以通过调用 SetListenerAccessControlStatus 接口将AccessControlStatus的值设置为close，关闭访问控制。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=139a00604ad-cn-east-hangzhou-01 &SourceItems=1.XX.XX.1,XX.XX.1.0/21
```

`&<`公共请求参数> 负载均衡正常返回示例

| XML | 格式 |
|---|---|
| <AddListenerWhiteListItemResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </AddListenerWhiteListItemResponse> |  |

| JSON | 格式 |
|---|---|
| { "AddListenerWhiteListItemResponse": { "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } } |  |

##### 7.5.5.4. RemoveListenerWhiteListItem

调用RemoveListenerWhiteListItem删除监听白名单中的IP。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RemoveListenerWhiteListIte m | 要执行的操作。 取值：RemoveListenerWhiteListItem。 |
| ListenerPort | Integer | 是 | 80 | 监听端口。 取值：1~65535。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08ex**** | 负载均衡实例的ID。 |
| SourceItems | String | 是 | 192.168.0.1/24 | 访问控制列表。支持输入IP地址或IP地址段（CIDR block形式），多个 IP地址或地址段用逗号（,）分隔。 说明如果所有IP都被删除，则无法访问该监听。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex**** &SourceItems=192.168.0.1
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RemoveListenerWhiteListItemResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </RemoveListenerWhiteListItemResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |  |

##### 7.5.5.5. CreateAccessControlList

您可以创建多个访问控制策略组，每个策略组可包含多个IP地址条目或IP地址段条目。访问控制策略组的限制如下： 每个地域单账号可创建的访问控制策略组个数为50。 单账号每次可添加的IP地址条目个数为50。 每个访问控制策略组可包含的条目个数为300。 每个监听可绑定的访问控制策略组个数为50。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

负载均衡

| Action | String | 是 | CreateAccessControlList | 要执行的操作，取值：CreateAccessControlList |
|---|---|---|---|---|
| AclName | String | 是 | rule1 | 访问控制策略组名称，需要保证Region内唯一。 |
| RegionId | String | 是 | cn-hangzhou | 访问控制策略组的地域ID。 |
| AddressIPVersion | String | 否 | ipv4 | IP版本，可以设置为ipv4或者ipv6。 说明目前支持创建IPv6实例且创建实例类型必须为性能保障型，实例的可用区如下：华东1地域的E、F两个可用区、华北2 地域的F、G两个可用区、华东2地域的所有可用区和华南1地域的 D、E两个可用区。 |
| ResourceGroupId | String | 否 | rg-atstuj3rt**** | 访问控制策略组所在的资源组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AclId | String | acl-rj9xpxzcwxrukois**** | 访问控制策略组ID。 |
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA49 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateAccessControlList &AclName=rule1 &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateAccessControlListResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> <AclId>acl-rj9xpxzcwxrukois******</AclId> </CreateAccessControlListResponse> |  |

| JSON | 格式 |
|---|---|
| {"RequestId":"988CB45E-1643-48C0-87B4-928DDF77EA49","AclId":"acl-rj9xpxzcwxrukois****"} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAction.RegionNotSupport | The region does not support this action. | 当前地域不支持指定功能。 |
| 400 | AclNumberOverLimit | The Acl number has reached to the max quota limit. | Acl数量已达到最大配额限制。 |
| 400 | InvalidResourceGroupId.NotFoun d | The specified ResourceGroupId is not found. | 指定的资源组不存在。 |
| 400 | ResourceInConfiguring.Acl | The specified resource is configuring, please try again later. | 指定的Acl正在配置中，请稍后重试。 |

##### 7.5.5.6. DeleteAccessControlList

只有当要删除的访问控制策略组没有绑定任何监听时，才可以删除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteAccessControlList | 要执行的操作，取值：DeleteAccessControlList。 |
| AclId | String | 是 | acl-bp1l0kk4gxce43kz**** | 访问控制策略组ID。 |
| RegionId | String | 是 | cn-hangzhou | 访问控制策略组的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |

**返回数据**

负载均衡

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA49 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteAccessControlList &AclId=acl-bp1l0kk4gxce43kz****** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteAccessControlListResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> </DeleteAccessControlListResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationFailed.AclBindedWithVi p | The ACL has binded with vip. | 操作失败，原因是Acl已与监听绑定。 |

##### 7.5.5.7. DescribeAccessControlLists

调用DescribeAccessControlLists查询已创建的访问控制策略组。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAccessControlLists | 要执行的操作，取值：DescribeAccessControlLists。 |
| RegionId | String | 是 | cn-hangzhou | 访问控制策略组的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclName | String | 否 | acl | 访问控制策略组名称。长度限制为1~80个字符，只支持中文、字母、 数字和半角句号（.）、短划线（-）、正斜线（/）和下划线（_）。访问控制策略组名称必须为地域内唯一。 |
| AddressIPVersion | String | 否 | ipv4 | 访问控制策略组绑定的实例的IP类型。取值： ipv4：负载均衡实例的IP地址是IPv4类型。 ipv6：负载均衡实例的IP地址是IPv6类型。 |
| PageSize | Integer | 否 | 10 | 分页查询时每页的行数，最大值：50，默认值：10。 |
| PageNumber | Integer | 否 | 1 | 列表的页码，默认值：1。 |
| ResourceGroupId | String | 否 | rg-atstuj3rtop**** | 企业资源组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Acls | Array of Acl |  | 查询到的访问控制策略组列表。 |
| Acl |  |  |  |
| AclId | String | acl-bp1l0kk4gxce43k***** | 访问控制策略组ID。 |
| AclName | String | rule1 | 访问控制策略组名称。 |
| AddressIPVersion | String | ipv4 | 关联的负载均衡实例的IP地址类型。 |

负载均衡

| ResourceGroupId | String | rg-jfenf*********** | 资源组ID。 |
|---|---|---|---|
| Count | Integer | 5 | 当前页展示的访问控制策略组个数。 |
| PageNumber | Integer | 2 | 实例列表页码，起始值1，默认值1。 |
| PageSize | Integer | 3 | 分页查询时每页的行数。 默认值：10。 |
| RequestId | String | 3CB646EF-6147-4566-A9D9- CE8FBE86F971 | 请求ID。 |
| TotalCount | Integer | 3 | 已创建的访问控制组策略组个数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAccessControlLists &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeAccessControlListsResponse> <RequestId>3CB646EF-6147-4566-A9D9-CE8FBE86F971</RequestId> <Acls> <Acl> <AclId>acl-bp1j9vn2g7wm9wn0*****</AclId> <AclName>test</AclName> <AddressIPVersion>ipv4</AddressIPVersion> </Acl> <Acl> <AclId>acl-bp1l0kk4gxce43*****</AclId> <AclName>doctest</AclName> <AddressIPVersion>ipv4</AddressIPVersion> </Acl> </Acls> </DescribeAccessControlListsResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "3CB646EF-6147-4566-A9D9-CE8FBE86F971", "Acls": { "Acl": [ { "AclId": "acl-bp1j9vn2g7wm9wn0****", "AclName": "test", "AddressIPVersion": "ipv4" }, { "AclId": "acl-bp1l0kk4gxce43*****", "AclName": "doctest", "AddressIPVersion": "ipv4" } ] } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidResourceGroupId.NotFoun d | The specified ResourceGroupId is not found. | 指定的资源组不存在。 |

##### 7.5.5.8. DescribeAccessControlListAttribute

调用DescribeAccessControlListAttribute查询访问控制策略组的配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAccessControlListAtt ribute | 要执行的操作，取值：DescribeAccessControlListAttribute。 |

负载均衡

| AclId | String | 是 | acl-bp1l0kk4gxce43kzet04s | 要查询的访问控制策略组ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-hangzhou | 访问控制策略组的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AclEntryComment | String | 否 | test | 访问控制策略组的条目的备注信息。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AclEntrys | Array of AclEntry |  | 访问控制策略组的信息列表。 |
| AclEntry |  |  |  |
| AclEntryComment | String | 访问控制条目。 | 访问控制条目备注。 |
| AclEntryIP | String | 192.168.0.1 | 访问控制条目IP。 |
| AclId | String | acl-bp1l0kk4gxce43kzet04s | 访问控制策略组ID。 |
| AclName | String | doctest | 访问控制策略组名称。 |
| AddressIPVersion | String | ipv4 | 关联的实例的IP类型。 |
| RelatedListeners | Array of RelatedListener |  | 该访问控制策略组已绑定的监听列表。 |
| RelatedListener |  |  |  |
| AclType | String | white | 访问控制的类型。取值： black：黑名单 white：白名单 |
| ListenerPort | Integer | 443 | 绑定的监听的前端端口。 |
| LoadBalancerId | String | lb-bp13jaf5qli5xmgl1miup | 负载均衡实例的ID。 |
| Protocol | String | https | 绑定的监听的协议类型。取值： tcp udp http https |
| RequestId | String | C9906A1D-86F7-4C9C-A369- 54DA42EF206A | 请求ID。 |
| ResourceGroupId | String | rg-atstuj3rtop**** | 企业资源组ID。 |

**示例**

请求示例

```
/?Action=DescribeAccessControlListAttribute &AclId=acl-bp1l0kk4gxce43kzet04s &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式负载均衡

```xml
<DescribeAccessControlListAttributeResponse>
   <AclId>acl-bp1l0kk4gxce43kzet04s</AclId>
   <RelatedListeners>
      <RelatedListener>
         <AclType>white</AclType>
         <LoadBalancerId>lb-bp13jaf5qli5xmgl1miup</LoadBalancerId>
         <Protocol>https</Protocol>
         <ListenerPort>443</ListenerPort>
      </RelatedListener>
   </RelatedListeners>
   <AclName>doctest</AclName>
   <RequestId>C9906A1D-86F7-4C9C-A369-54DA42EF206A</RequestId>
   <AddressIPVersion>ipv4</AddressIPVersion>
</DescribeAccessControlListAttributeResponse>
```

| JSON | 格式 |
|---|---|
| clEntrys":{"AclEntry":[{"AclEntryComment":"访问控制条目。","AclEntryIP":"192.168.0.1"}]},"ResourceGroupId":"rg- ******************","RequestId":"C9906A1D-86F7-4C9C-A369-54DA42EF206A","AddressIPVersion":"ipv4","AclId":"acl- bp1l0kk4gxce43kzet04s","RelatedListeners":{"RelatedListener":[{"ListenerPort":"443","AclType":"white","LoadBalancerId":"lb- bp13jaf5qli5xmgl1miup","Protocol":"https"}]},"AclName":"doctest"}{"A |  |

##### 7.5.5.9. SetAccessControlListAttribute

调用SetAccessControlListAttribute修改访问控制策略组的名称。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetAccessControlListAttribute | 要执行的操作，取值：SetAccessControlListAttribute。 |
| AclId | String | 是 | acl-bp1l0kk4gxce43kzet04s | 访问控制策略组ID。 |
| AclName | String | 是 | test1 | 访问控制策略组名称。长度限制为1~80个字符，只支持中文、字母、 数字和半角句号（.）、短划线（-）、正斜线（/）和下划线（_）。访问控制策略组名称必须为地域内唯一。 |
| RegionId | String | 是 | cn-hangzhou | 访问控制策略组的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AclId | String | acl-bp1l0kk4gxce43kzet04s | 访问控制策略组ID。 |
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA49 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetAccessControlListAttribute &AclId=acl-bp1l0kk4gxce43kzet04s &AclName=test1 &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetAccessControlListAttributeResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> </SetAccessControlListAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49" } |  |

##### 7.5.5.10. AddAccessControlListEntry

调用AddAccessControlListEntry在访问控制策略组中添加IP条目。 每个策略组可包含多个IP地址条目或IP地址段条目，访问控制策略组的条目限制如下： 负载均衡单账号每次可添加的IP地址条目个数：**50**。 每个访问控制策略组可包含的条目个数：**300**。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AddAccessControlListEntry | 要执行的操作，取值：AddAccessControlListEntry。 |
| AclId | String | 是 | acl-bp1l0kk4gxce43kze***** | 访问控制策略组ID。 |
| RegionId | String | 是 | cn-hangzhou | 访问控制策略组的地域ID。 |
| AclEntrys | String | 否 | [{"entry":"10.0.**.**/24","co mment":"privaterule1"}, {"entry":"192.168.**.**/16"," comment":"privaterule2"}] | 设置访问控制策略组。 entry：访问控制策略组中要添加的IP条目，可以指定IP地址或IP地址段（CIDR block），多个IP地址或IP地址段之间用半角逗号（,） 隔开。 comment：访问控制策略组备注说明。 说明每次最多可添加50个条目，如果添加的IP条目重复， 则只会添加一条，其余重复条目会被忽略。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA4 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddAccessControlListEntry &AclId=acl-bp1l0kk4gxce43kze***** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <AddAccessControlListEntryResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> </AddAccessControlListEntryResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParam.AclEntryExists | The specified aclEntry already exists in the acl. | 当前Acl中已包含指定的条目。 |
| 400 | IllegalEntry | Entry version is conflict to the acl version. | 条目版本与acl版本冲突。 |
| 400 | InvalidEntry | %s. | 参数无效。请检查参数约束，并在修改后重试。 |
| 400 | InvalidParam.Comment | The specified comment is invalid. | Comment 参数非法 |
| 503 | ServiceUnavailable | Service is unavailable now. | 服务现在不可用。 |
| 400 | AclEntryExceedLimit | The maximum number of ACL entries is exceeded. | 访问控制条目超限 |

##### 7.5.5.11. RemoveAccessControlListEntry

调用RemoveAccessControlListEntry删除访问控制策略组中的IP条目。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RemoveAccessControlListEnt ry | 要执行的操作，取值：RemoveAccessControlListEntry。 |
| AclId | String | 是 | acl-bp1l0kk4gxce43k****** | 访问控制策略组ID。 |

负载均衡

| RegionId | String | 是 | cn-hangzhou | 访问控制策略组的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
|---|---|---|---|---|
| AclEntrys | String | 否 | [{"entry":"10.0.**.**/24","co mment":"privaterule1"}] | 设置访问控制策略组。 entry：访问控制策略组中的IP条目，可以指定IP地址或IP地址段 （CIDR block），多个IP地址或地址段之间用半角逗号（,）隔开。 comment：访问控制策略组备注说明。 说明如果访问控制策略组关联了监听，不允许删除组内的所有IP条目。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA49 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveAccessControlListEntry &AclId=acl-bp1l0kk4gxce43k****** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RemoveAccessControlListEntryResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> </RemoveAccessControlListEntryResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49" } |  |

### 转发规则

#### 7.6.1. CreateRules

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 传统型负载均衡实例的地域ID。 |
| LoadBalancerId | String | Query | 是 | lb-bp1ca0zt07t934w****** | 传统型负载均衡实例ID。 |
| ListenerPort | Integer | Query | 是 | 443 | 负载均衡实例前端使用的监听端口。 取值范围：1~65535 。 |
| ListenerProtocol | String | Query | 否 | https | 负载均衡实例前端使用的协议。 相同端口存在不同协议监听时，此字段必选。 |

负载均衡

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RuleList | String | Query | 是 | [{"RuleName":"Rule2","Domain":"test.co m","VServerGroupId":"rsp- bp114ni******"}] | 要添加的转发规则。一次请求中，最多可添加10 条转发规则。每条转发规则包含以下参数： RuleName （必选）：String类型。转发规则名称，长度为1~40个字符，支持字母、 数字、短划线（-）、正斜线（/）、半角句号 （.）和下划线（_）这些字符。同一个监听内不同规则的名称必须唯一。 Domain （可选）： String类型。转发规则关联的请求域名，与Url 参数至少选择一个。 Url （可选）：String类型，可选，访问路径，长度限制为1~80个字符，只能使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、问号（?）、井号 （#）和and（&）这些字符。 URL不能只为正斜线（/），但必须以正斜线（/）开头， 与Domain 参数至少选择一个。 VServerGroupId （必选）：String类型。该转发规则的目标虚拟服务器组ID。 Domain 和 Url 两者必须指定一个，也可以同时指定。 Domain 和 Url 的组合在同一个监听内必须唯一。 |
| AccessKeyId | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| Action | String | Query | 否 | CreateRules | 要执行的操作。取值：CreateRules。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| accesskeyid _ _ | String | Query | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | Query | 否 | {"tagKey":"Key1","tagValue":"Value1"} | 标签列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |
| Rules | Array |  | 转发规则列表。 |
| -RuleId | String | rule-bp12jzy0***** | 转发规则ID。 |
| -RuleName | String | Rule2 | 转发规则名称。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou &LoadBalancerId=lb-bp1ca0zt07t934w****** &ListenerPort=443 &RuleList=[{"RuleName":"Rule2","Domain":"test.com","VServerGroupId":"rsp-bp114ni******"}]
```

&公共请求参数正常返回示例 `JSON` 格式负载均衡

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
 "Rules":{
  "RuleId":"rule-bp12jzy0*****",
  "RuleName":"Rule2"
 }
}
```

| XML | 格式 |
|---|---|
| <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <Rules> <RuleId>rule-bp12jzy0*****</RuleId> <RuleName>Rule2</RuleName> </Rules> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | LbIdMissMatch | InvalidParameter | The specified VServerGroupId does not belong to the LoadBalancerId of rule. |
| 400 | REGIONNOTSUPPORTPARAMET _ _ _ ERVALUE _ | InvalidParameterValue.RegionNotSupport | The region does not support the parameter value, %s. |
| 400 | TooManyListeners | TooManyListeners | More than 1 listener is found, please be more specified. |
| 400 | RuleExists | DomainExist | rule with same domain and url already exists in specified vip |
| 400 | -2337 | OperationFailed.ListenerStatusNotSupport | The status of the listener does not support this operation. Please try again later. |
| 400 | ListenerProcessing | OperationFailed.ListenerStatusNotSupport | The status of the listener does not support this operation. Please try again later. |
| 400 | LBNotSupportOldRule | OperationFailed.ActionNotSupport | The loadbalancer does not support such action. |
| 400 | MissingParam.RuleName | MissingParameter.RuleName | The parameter RuleName is required. |

#### 7.6.2. DescribeRuleAttribute

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 负载均衡实例的地域ID。 |
| RuleId | String | Query | 是 | rule-bp1efemp9**** | 转发规则ID。 |
| AccessKeyId | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| Action | String | Query | 否 | DescribeRuleAttribute | 要执行的操作。取值： DescribeRuleAttribute。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| accesskeyid _ _ | String | Query | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | Query | 否 | {"tagKey":"Key1","tagValue":"Value1"} | 标签列表。 |

**返回数据**

负载均衡

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Cookie | String | wwe | 服务器上配置的Cookie。 长度为1~200个字符，只能包含ASCII英文字母和数字字符，不能包含逗号、分号或空格，也不能以$开头。 当StickySession 为on 且StickySessionType 为server 时，该参数必选且有效。 |
| CookieTimeout | Integer | 12 | Cookie超时时间。 取值：1~86400 秒。 当StickySession 为on 且StickySessionType 为insert 时， 该参数必选且有效。 |
| VServerGroupId | String | rsp-cige6j**** | 转发规则关联的服务器组ID。 |
| ListenerPort | String | 90 | 负载均衡实例前端使用的监听端口。 |
| HealthCheckInterval | Integer | 34 | 健康检查的时间间隔。 取值：1 ~50 秒。 HealthCheck 为on 时，该参数有效。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |
| UnhealthyThreshold | Integer | 3 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由success 判定为fail 。 取值：2 ~10 。 HealthCheck 为on 时，该参数有效。 |
| HealthCheckURI | String | 10.21.22.1 | 用于健康检查的URI。 HealthCheck 为on 时，该参数有效。 |
| Scheduler | String | wrr | 调度算法。取值： wrr （默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 rr ：按照访问顺序依次将外部请求依序分发到后端服务器。 ListenerSync 为off 时有效，为on 时表明与监听配置一致。 |
| HealthCheck | String | off | 是否开启健康检查。 取值：on 或off 。 ListenerSync 为off 时有效，为on 时表明与监听配置一致。 |
| LoadBalancerId | String | lb-bp1ca0zt07t934wxe**** | 负载均衡实例ID。 |
| HealthCheckTimeout | Integer | 34 | 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。 取值：1 ~300 秒。 如果HealthCHeckTimeout 的值小于HealthCheckInterval 的值，则HealthCHeckTimeout 无效，超时时间为HealthCheckInterval 的值。HealthCheck 为on 时，该参数有效。 |
| Url | String | /cache | 转发规则路径。 |
| StickySession | String | off | 是否开启会话保持。 取值：on 或off 。 在ListenerSync 为off 时必选且有效，为on 时表明与监听配置一致。 |
| HealthCheckConnectPort | Integer | 23 | 健康检查的后端服务器的端口。 取值：1 ~65535 。 HealthCheck 为on 时该参数有效，若为空且HealthCheck 为on ，表明默认使用监听后端端口配置。 |

| 负载均衡 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HealthyThreshold | Integer | 2 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail 判定为success 。 取值：2 ~10 。 HealthCheck 为on 时，该参数有效。 |
| HealthCheckDomain | String | www.example.com | 用于健康检查的域名，取值： $ _ip ： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。 domain ：域名长度为1~80字符，只能包含字母、数字、半角句号（.）和短划线（-）。 HealthCheck 为on 时，该参数有效。 |
| ListenerSync | String | off | 转发规则是否从监听上继承健康检查、会话保持和调度算法配置。 取值：on 或off 。 off ：不继承监听配置，转发规则自定义健康检查及会话保持配置。 on ：继承监听配置。 |
| StickySessionType | String | insert | Cookie的处理方式。取值： insert ：植入Cookie。客户端第一次访问时，负载均衡会在返回请求中植入 Cookie（即在HTTP/HTTPS响应报文中插入SERVERID），下次客户端携带此 Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。 server ：重写Cookie。负载均衡发现用户自定义了Cookie，将会对原来的 Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。 当StickySession 的值为on 时，该参数有效。 |
| Domain | String | test.com | 转发规则域名。 |
| HealthCheckHttpCode | String | http3xx _ | 健康检查正常的HTTP状态码，多个状态码用逗号分隔。默认值为http _2xx 。 取值： http _2xx 。 http _3xx 。 http _4xx 。 http _5xx 。 HealthCheck 为on 时，该参数有效。 |
| RuleName | String | Rule1 | 转发规则名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRuleAttribute &RegionId=cn-hangzhou &RuleId=rule-bp1efemp9****
```

&公共请求参数正常返回示例 `JSON` 格式负载均衡

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "Cookie":"wwe",
 "CookieTimeout":12,
 "VServerGroupId":"rsp-cige6j****",
 "ListenerPort":"90",
 "HealthCheckInterval":34,
 "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
 "UnhealthyThreshold":3,
 "HealthCheckURI":"10.21.22.1",
 "Scheduler":"wrr",
 "HealthCheck":"off",
 "LoadBalancerId":"lb-bp1ca0zt07t934wxe****",
 "HealthCheckTimeout":34,
 "Url":"/cache",
 "StickySession":"off",
 "HealthCheckConnectPort":23,
 "HealthyThreshold":2,
 "HealthCheckDomain":"www.example.com",
 "ListenerSync":"off",
 "StickySessionType":"insert",
 "Domain":"test.com",
 "HealthCheckHttpCode":"http_3xx ",
 "RuleName":"Rule1"
}
```

| XML | 格式 |
|---|---|
| <Cookie>wwe</Cookie> <CookieTimeout>12</CookieTimeout> <VServerGroupId>rsp-cige6j****</VServerGroupId> <ListenerPort>90</ListenerPort> <HealthCheckInterval>34</HealthCheckInterval> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <UnhealthyThreshold>3</UnhealthyThreshold> <HealthCheckURI>10.21.22.1</HealthCheckURI> <Scheduler>wrr</Scheduler> <HealthCheck>off</HealthCheck> <LoadBalancerId>lb-bp1ca0zt07t934wxe****</LoadBalancerId> <HealthCheckTimeout>34</HealthCheckTimeout> <Url>/cache</Url> <StickySession>off</StickySession> <HealthCheckConnectPort>23</HealthCheckConnectPort> <HealthyThreshold>2</HealthyThreshold> <HealthCheckDomain>www.example.com</HealthCheckDomain> <ListenerSync>off</ListenerSync> <StickySessionType>insert</StickySessionType> <Domain>test.com</Domain> <HealthCheckHttpCode>http_3xx </HealthCheckHttpCode> <RuleName>Rule1</RuleName> |  |

#### 7.6.3. SetRule

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 传统型负载均衡实例的地域ID。 |
| RuleId | String | Query | 是 | rule-3ejhkt**** | 转发规则ID。 |
| VServerGroupId | String | Query | 否 | rsp-cige6**** | 转发规则的目标服务器组ID。 |
| RuleName | String | Query | 否 | doctest | 转发规则名称，长度限制为1~80个字符，支持字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）这些字符。 同一个监听内不同规则的名称必须唯一。 |
| ListenerSync | String | Query | 否 | off | 是否继承监听的健康检查、会话保持和调度算法配置。取值： on ：继承监听配置。 off ：不继承监听配置。转发规则自定义健康检查及会话保持配置。 |

| 负载均衡 |  |  |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |
| Scheduler | String | Query | 否 | wrr | 调度算法。取值： wrr ：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 rr ：按照访问顺序依次将外部请求依序分发到后端服务器。 在ListenerSync 为off 时必选且有效。 |  |
| StickySession | String | Query | 否 | off | 是否开启会话保持，取值： on ：开启。 off ：不开启。 在ListenerSync 为off 时必选且有效。 |  |
| StickySessionType | String | Query | 否 | insert | Cookie的处理方式。取值： insert ：植入Cookie。 客户端第一次访问时，负载均衡会在返回请求中植入 Cookie（即在HTTP或HTTPS响应报文中插入后端服务器ID），客户端下次携带此Cookie 访问时，负载均衡服务会将请求定向转发给第一次访问时记录到的后端服务器上。 server ：重写Cookie。 负载均衡发现用户自定义Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问时， 负载均衡服务会将请求定向转发给之前记录到的后端服务器。 StickySession 为on 时必选且有效。 |  |
| CookieTimeout | Integer | Query | 否 | 123 | Cookie超时时间。单位：秒。取值范围：1 ~86400 。 当StickySession 为on 且StickyS essionType 为insert 时必选且有效。 |  |
| Cookie | String | Query | 否 | 23ffsa | 服务器上配置的Cookie。 长度为1~200个字符，只能包含ASCII英文字母和数字字符，不能包含半角逗号（,）、半角分号 （;）或空格，也不能以美元（$）开头。 当StickySession 为on 且StickyS essionType 为server 时必选且有效。 |  |
| HealthCheck | String | Query | 否 | off | 是否开启健康检查。取值： on ：开启。 off ：不开启。 ListenerSync 为off 时必选且有效，其他情况会忽略此参数。 |  |
| HealthCheckDomai n | String | Query | 否 | $ip _ | 用于健康检查的域名，取值： $ _ip ： 后端服务器的私网IP。当指定了 $ _ip或HealthCheckDomain未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。 domain ：域名长度为1~80字符，只能包含字母、数字、半角句号（.）和短划线 （-）。 ** HealthCheck为 on**时有效。 |  |
| HealthCheckURI | String | Query | 否 | /example | 用于健康检查的URI。 HealthCheck 为on 时必选且有效。 |  |
| HealthyThreshold | Integer | Query | 否 | 4 | 健康检查连续成功多少次后，将后端服务器的健康检查状态由失败判定为成功 。 取值范围：2 ~10 。 HealthCheck 为on 时必选且有效。 |  |

负载均衡

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UnhealthyThreshol d | Integer | Query | 否 | 4 | 健康检查连续失败多少次后，将后端服务器的健康检查状态由成功判定为失败 。 取值范围：2 ~10 。 HealthCheck 为on 时必选且有效。 |
| HealthCheckTimeo ut | Integer | Query | 否 | 20 | 接收来自运行状况检查的响应需要等待的时间。 如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。单位：秒。取值范围：1 ~300 。 HealthCheck 为on 时必选且有效。 |
| HealthCheckInterv al | Integer | Query | 否 | 20 | 健康检查的时间间隔。单位：秒。取值范围：1 ~50 。 HealthCheck 为on 时必选且有效。 |
| HealthCheckConne ctPort | Integer | Query | 否 | 80 | 健康检查使用的端口。取值范围：1 ~65535 。 HealthCheck 为on 时有效。 |
| HealthCheckHttpC ode | String | Query | 否 | http2xx _ | 健康检查正常的HTTP状态码，多个状态码用半角逗号（,）分割。 取值： http _2xx 。 http _3x x。 http _4xx 。 http _5xx 。 HealthCheck 为on 时必选且有效。 |
| Action | String | Query | 否 | SetRule | 要执行的操作。取值：SetRule。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou &RuleId=rule-3ejhkt****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C" } |  |

| XML | 格式 |
|---|---|
| <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> |  |

**错误码**

负载均衡

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | LbIdMissMatch | InvalidParameter | The specified VServerGroupId doesn't belong to the rule's LoadBalancerId. |
| 400 | REGIONNOTSUPPORTPARAMET _ _ _ ER | InvalidParameter.RegionNotSupport | The region doesn't support the parameter: %s. |

#### 7.6.4. DeleteRules

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 负载均衡实例的地域ID。 |
| RuleIds | String | Query | 是 | ["rule-bp1z9ce******","rule- bp1tuc******4"] | 要删除的转发规则列表。 要删除的转发规则列表不能为空，并且可删除的转发规则条目数不能超过10条。 |
| AccessKeyId | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| Action | String | Query | 否 | DeleteRules | 要执行的操作。取值：DeleteRules。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| accesskeyid _ _ | String | Query | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |
| Tags | String | Query | 否 | {"tagKey":"Key1","tagValue":"Value1"} | 标签列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou &RuleIds=["rule-bp1z9ce******","rule-bp1tuc******4"]
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C" } |  |

| XML | 格式 |
|---|---|
| <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RulesInDiffVip | Operation.NotAllowed | The specified rules must be in the same listener. |

负载均衡

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -2337 | OperationFailed.ListenerStatusNotSupport | The status of the listener does not support this operation. Please try again later. |
| 400 | -2314 | OperationFailed.ListenerConflict | The rule does not support this operation because of same port listener. |

### 访问日志

#### 7.7.1. DescribeAccessLogsDownloadAttribute

调用DescribeAccessLogsDownloadAttribute接口查询指定传统型负载均衡实例的访问日志。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 传统型负载均衡实例的地域ID。 |
| Tags | String | Query | 否 | [{"tagKey":"Key1","tagValue":"Value1"}] | 标签列表。 |
| LoadBalancerId | String | Query | 否 | lb-bp1b6c719dfa08ex***** | 传统型负载均衡实例ID。 |
| LogType | String | Query | 否 | layer7 | 访问日志类型。仅取值layer7 ，表示七层访问日志。 |
| PageNumber | Integer | Query | 否 | 1 | 列表的页码。默认值：1 。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页的行数。最大值：50 。默认值：10 。 |
| Action | String | Query | 否 | DescribeAccessLogsDownloadAttribute | 要执行的操作。取值： DescribeAccessLogsDownloadAttribute。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalCount | Integer | 10 | 列表条目数。 |
| PageSize | Integer | 10 | 分页查询时每页的行数。 |
| RequestId | String | 8B9DB03B-ED39-5DB8-9C9F- 1ED5F548D61E | 请求ID。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| LogsDownloadAttributes | Array |  | 访问日志配置信息。 |
| -LogProject | String | test-log-project | 日志服务LogProject的名称。 |
| -LogStore | String | test-log-store | 日志服务LogStore的名称。 |
| -LoadBalancerId | String | lb-bp1b6c719dfa08ex***** | 传统型负载均衡实例的ID。 |
| -LogType | String | layer7 | 访问日志类型。仅取值layer7 ，表示七层访问日志。 |
| -RoleArn | String | su | 角色名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Region | String | cn-hangzhou | 传统型负载均衡实例所在的地域ID。 |
| Count | Integer | 1 | 数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAccessLogsDownloadAttribute &RegionId=cn-hangzhou
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":10, "PageSize":10, "RequestId":"8B9DB03B-ED39-5DB8-9C9F-1ED5F548D61E", "PageNumber":1, "Count":1, "LogsDownloadAttributes":{ "LogStore":"test-log-store", "LogType":"layer7", "Region":"cn-hangzhou", "LoadBalancerId":"lb-bp1b6c719dfa08ex*****", "LogProject":"test-log-project", "RoleArn":"su" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>10</TotalCount> <PageSize>10</PageSize> <RequestId>8B9DB03B-ED39-5DB8-9C9F-1ED5F548D61E</RequestId> <PageNumber>1</PageNumber> <Count>1</Count> <LogsDownloadAttributes> <LogStore>test-log-store</LogStore> <LogType>layer7</LogType> <Region>cn-hangzhou</Region> <LoadBalancerId>lb-bp1b6c719dfa08ex*****</LoadBalancerId> <LogProject>test-log-project</LogProject> <RoleArn>su</RoleArn> </LogsDownloadAttributes> |  |

### 服务器证书

#### 7.8.1. UploadServerCertificate

该接口保证事务性，即上传的证书和私钥要么都上传成功，要么都不成功。上传成功后，返回该用户的所有服务器证书列表的Fingerprint。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UploadServerCertificate | 要执行的操作。 取值：UploadServerCertificate。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 服务器证书的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| AliCloudCertificateId | String | 否 | 730912673******15d97e77 _ 09a71445759hr7892****** _ _ | 阿里云的云上证书ID。 使用阿里云的云上证书，该参数必选。 |
| AliCloudCertificateName | String | 否 | testcertkey | 阿里云的云上证书名称。 |

负载均衡

| ServerCertificate | String | 否 | test | 需要上传的公钥证书。 说明如果不使用阿里云的云上证书，该参数必选。 |
|---|---|---|---|---|
| PrivateKey | String | 否 | wmsa**** | 需要上传的私钥。 说明如果不使用阿里云的云上证书，该参数必选。 |
| ServerCertificateName | String | 否 | mycert01 | 要上传的服务器证书的名称。 名称长度为 1~80 个英文或中文字符，必须以大小字母或中文开头，可包含数字、英文句点（.）、下划线（_）和短划线（-）。 |
| Tags | String | 否 | ServerCertificate**** | 标签。 |
| StandardType | String | 否 | ServerCertificate | 标准类型。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ServerCertificateId | String | xxxxidkp-123-cn-test**** | 服务器证书ID。 |
| ServerCertificateName | String | mycert01 | 服务器证书名称。 |
| Fingerprint | String | 01:DF:AB:** | 服务器证书的指纹。 |
| AliCloudCertificateId | String | 730912xxxxx15d97e7709a714 _ _ 45759hr7**** _ | 阿里云证书服务中的服务器证书ID。 |
| AliCloudCertificateName | String | testcert**** | 阿里云证书服务中的服务器证书名称。 |
| IsAliCloudCertificate | Integer | 0 | 是否为阿里云证书服务中的证书。 0：表示不是阿里云证书。 1：表示是阿里云证书。 |
| RegionId | String | cn-qingdao-env17-d01 | 证书所属的地域ID。 |
| RegionIdAlias | String | hangzhou | 实例地域名称。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UploadServerCertificate &RegionId=cn-east-hangzhou-01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <UploadServerCertificateResponse> <RegionIdAlias>cn-east-hangzhou-01</RegionIdAlias> <Fingerprint>01:DF:AB:**</Fingerprint> <AliCloudCertificateName>testcert***</AliCloudCertificateName> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <IsAliCloudCertificate>0</IsAliCloudCertificate> <ServerCertificateId>xxxxidkp-123-cn-test******</ServerCertificateId> <ServerCertificateName>mycert01</ServerCertificateName> <RegionId>cn-hangzhou</RegionId> <AliCloudCertificateId>730912xxxxx_15d97e7709a_71445759hr_7*******</AliCloudCertificateId> </UploadServerCertificateResponse> |  |

`JSON` 格式负载均衡

```json
{
        "RegionIdAlias": "cn-east-hangzhou-01",
        "Fingerprint": "01:DF:AB:**",
        "AliCloudCertificateName": "testcert***",
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "IsAliCloudCertificate": 0,
        "ServerCertificateId": "xxxxidkp-123-cn-test******",
        "ServerCertificateName": "mycert01",
        "RegionId": "cn-hangzhou",
        "AliCloudCertificateId": "730912xxxxx_15d97e7709a_71445759hr_7*******"
    }
}
```

#### 7.8.2. DeleteServerCertificate

**说明**

如果指定删除的证书被引用，则无法删除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteServerCertificate | 要执行的操作。 取值：DeleteServerCertificate。 |
| ServerCertificateId | String | 是 | 123157****166f820468917 _ _ 147634087099**** _ | 服务器证书ID。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteServerCertificate &ServerCertificateId=123157****_166f8204689_1714763408_7099****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteServerCertificateResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </DeleteServerCertificateResponse> |  |

| JSON | 格式 |
|---|---|
| { "DeleteServerCertificateResponse": { "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } } |  |

#### 7.8.3. DescribeServerCertificates

调用DescribeServerCertificates查询指定地域的服务器证书列表。 为了保证安全性，只返回证书的指纹和名称，不返回证书和私钥的内容。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeServerCertificates | 要执行的操作。 取值：DescribeServerCertificates。 |

负载均衡

| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
|---|---|---|---|---|
| ServerCertificateId | String | 否 | 12315790xxxxxxx166f8204 _ 6891714763408709***** _ _ | 服务器证书ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ServerCertificates | Array of ServerCertificate |  | 服务器证书列表。 |
| ServerCertificate |  |  |  |
| ServerCertificateId | String | 123157xxxxxxxx166f82046891 _ _ 714763408709981430-cn-east- _ hangz****** | 服务器证书ID。 |
| ServerCertificateName | String | slb | 服务器证书名称。 |
| RegionId | String | cn-qingdao-env17-d01 | 服务器证书的地域ID。 |
| Fingerprint | String | 68:08:1a:f8:2c:97:69:a3:a1:e6:16 :41:4b:ca:4f:5d:ee:a5:ef:0d | 服务器证书的指纹。 |
| AliCloudCertificateId | String | 7309xxxxxxxx15d97e7709a71 _ _ 445759hr78928***** _ | 阿里云证书服务的服务器证书ID。 |
| AliCloudCertificateName | String | testcertkey | 阿里云证书服务的服务器证书名称。 |
| IsAliCloudCertificate | Integer | 0 | 是否是阿里云证书服务中的证书： 1：是。 0：不是。 |
| RegionIdAlias | String | cn-qingdao-env17-d01 | 负载均衡实例地域名称。 |
| StandardType | String | ServerCertificate | 标准类型。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeServerCertificates
```

`&<`公共请求参数> 正常返回示例 `XML` 格式负载均衡

```xml
      <RequestId>9FFF450B-CC09-4FFB-900F-E347EB7AA2CC</RequestId>
      <ServerCertificates>
            <ServerCertificate>
                  <CreateTimeStamp>1541761156000</CreateTimeStamp>
                  <CommonName>*.example1.com</CommonName>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxazb4ph6aiy</ResourceGroupId>
                  <Fingerprint>68:08:1a:f8:2c:97:69:a3:a1:e6:16:41:4b:ca:4f:5d:ee:a5:ef:0d</Fingerprint>
                  <ServerCertificateId>1231579xxxxxx_166f8204689_1714763408_709981430</ServerCertificateId>
                  <ExpireTimeStamp>1558161264000</ExpireTimeStamp>
                  <AliCloudCertificateId>1501739</AliCloudCertificateId>
                  <ExpireTime>2019-05-18T06:34:24Z</ExpireTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <CreateTime>2018-11-09T10:59:16Z</CreateTime>
                  <ServerCertificateName>*.example1.com</ServerCertificateName>
                  <IsAliCloudCertificate>1</IsAliCloudCertificate>
                  <AliCloudCertificateName>slb</AliCloudCertificateName>
            </ServerCertificate>
            <ServerCertificate>
                  <CreateTimeStamp>1481623069000</CreateTimeStamp>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxazb4ph6aiy</ResourceGroupId>
                  <Fingerprint>cd:90:1b:7b:49:4d:1d:90:f6:01:de:9a:81:7d:31:a7:38:1d:84:8d</Fingerprint>
                  <ServerCertificateId>1231579085xxxx_158f79de306</ServerCertificateId>
                  <ExpireTimeStamp>1732169065000</ExpireTimeStamp>
                  <AliCloudCertificateId>0</AliCloudCertificateId>
                  <ExpireTime>2024-11-21T06:04:25Z</ExpireTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <CreateTime>2016-12-13T09:57:49Z</CreateTime>
                  <ServerCertificateName>test_certificate</ServerCertificateName>
                  <IsAliCloudCertificate>0</IsAliCloudCertificate>
                  <AliCloudCertificateName></AliCloudCertificateName>
            </ServerCertificate>
      </ServerCertificates>
```

| JSON | 格式 |
|---|---|
| { "DescribeServerCertificatesResponse": { "RequestId": "9FFF450B-CC09-4FFB-900F-E347EB7AA2CC", "ServerCertificates": { "ServerCertificate": [ { "CreateTimeStamp": 1541761156000, "CommonName": "*.example1.com", "RegionIdAlias": "cn-hangzhou", "ResourceGroupId": "rg-acfmxazb4ph6aiy", "Fingerprint": "68:08:1a:f8:2c:97:69:a3:a1:e6:16:41:4b:ca:4f:5d:ee:a5:ef:0d", "ServerCertificateId": "1231579xxxxxx_166f8204689_1714763408_709981430", "ExpireTimeStamp": 1558161264000, "AliCloudCertificateId": 1501739, "ExpireTime": "2019-05-18T06:34:24Z", "RegionId": "cn-hangzhou", "CreateTime": "2018-11-09T10:59:16Z", "ServerCertificateName": "*.example1.com", "IsAliCloudCertificate": 1, "AliCloudCertificateName": "slb" }, { "CreateTimeStamp": 1481623069000, "RegionIdAlias": "cn-hangzhou", "ResourceGroupId": "rg-acfmxazb4ph6aiy", "Fingerprint": "cd:90:1b:7b:49:4d:1d:90:f6:01:de:9a:81:7d:31:a7:38:1d:84:8d", "ServerCertificateId": "1231579085xxxx_158f79de306", "ExpireTimeStamp": 1732169065000, "AliCloudCertificateId": 0, "ExpireTime": "2024-11-21T06:04:25Z", "RegionId": "cn-hangzhou", "CreateTime": "2016-12-13T09:57:49Z", "ServerCertificateName": "test_certificate", "IsAliCloudCertificate": 0, "AliCloudCertificateName": "" } ] } } } |  |

#### 7.8.4. SetServerCertificateName

负载均衡

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetServerCertificateName | 要执行的操作。 取值：SetServerCertificateName。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| ServerCertificateId | String | 是 | 139a****-cn-qingdao-env17- d01 | 服务器证书ID。 |
| ServerCertificateName | String | 是 | slb-servercertificate-cn-east- hangzhou**** | 服务器证书名称。长度为 1~80 个英文或中文字符，必须以大小字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FE7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetServerCertificateName &RegionId=cn-east-hangzhou-01 &ServerCertificateId=139a****-cn-east-hangzhou-01 &ServerCertificateName=slb-servercertificate-cn-east-hangzhou****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetServerCertificateNameResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId> </SetServerCertificateNameResponse> |  |

| JSON | 格式 |
|---|---|
| { "SetServerCertificateNameResponse": { "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FE7BA984" } } |  |

#### 7.8.5. UploadCACertificate

一次只能上传一份CA证书内容。添加成功后，返回该用户的该证书的ID、名称和指纹。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UploadCACertificate | 要执行的操作。 取值：UploadCACertificate。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| CACertificate | String | 是 | test | 要上传CA证书的内容。 |
| CACertificateName | String | 否 | mycacert01 | CA证书名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CACertificateId | String | 139a00604ad-cn-east-hangzh**** | CA证书ID。 |
| CACertificateName | String | mycacert01 | CA证书的名称。 |

负载均衡

| Fingerprint | String | 02:DF:AB:ED | CA证书的指纹。 |
|---|---|---|---|
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UploadCACertificate &RegionId=cn-qingdao-env17-d01 &CACertificate=test
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <UploadCACertificateResponse> <Fingerprint>02:DF:AB:ED</Fingerprint> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <CACertificateId>139a00604ad-cn-east-hangzh*****</CACertificateId> <CACertificateName>mycacert01</CACertificateName> </UploadCACertificateResponse> |  |

| JSON | 格式 |
|---|---|
| { "UploadCACertificateResponse": { "Fingerprint": "02:DF:AB:ED", "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "CACertificateId": "139a00604ad-cn-east-hangzh*****", "CACertificateName": "mycacert01" } } |  |

#### 7.8.6. DeleteCACertificate

无法删除正在使用的CA证书。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteCACertificate | 要执行的操作。 取值：DeleteCACertificate。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| CACertificateId | String | 是 | 123157908****15c73d7720 _ 3-986300114-2110544**** _ _ | CA证书ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteCACertificate &RegionId=cn-east-hangzhou-01 &CACertificateId=123157908****_15c73d77203_-986300114_-211054****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteCACertificateResponse> <RequestId>CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </DeleteCACertificateResponse> |  |

`JSON` 格式负载均衡

```json
{
        "RequestId": "CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984"
    }
}
```

#### 7.8.7. DescribeCACertificates

**说明**

为了保证安全性，只返回证书的指纹和名称，不返回证书的内容。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCACertificates | 要执行的操作。 取值：DescribeCACertificates。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | CA证书的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| CACertificateId | String | 否 | 139a006****-cn-qingdao- env17-d01 | CA证书ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CACertificates | Array of CACertificate |  | CA证书信息。 |
| CACertificate |  |  |  |
| CACertificateId | String | 139a006****-cn-qingdao-env17- d01 | CA证书ID。 |
| CACertificateName | String | test | CA证书名称。 |
| RegionId | String | cn-qingdao-env17-d01 | CA证书所属地域ID。 |
| Fingerprint | String | AC:BE:FD | CA证书的指纹。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCACertificates &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeCACertificateResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <CACertificates> <CACertificateName>test</CACertificateName> <Fingerprint>AC:BE:FD</Fingerprint> <RegionId>cn-east-hangzhou-01</RegionId> <CACertificateId>139a006****-cn-east-hangzhou-02</CACertificateId> </CACertificates> </DescribeCACertificateResponse> |  |

`JSON` 格式负载均衡

```json
{
    "DescribeCACertificateResponse": {
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "CACertificates": {
            "CACertificateName": "test",
            "Fingerprint": "AC:BE:FD",
            "RegionId": "cn-east-hangzhou-01",
            "CACertificateId": "139a006****-cn-east-hangzhou-02"
        }
    }
}
```

#### 7.8.8. SetCACertificateName

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetCACertificateName | 要执行的操作。 取值：SetCACertificateName。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 您可以通过调用 DescribeRegions 接口查询地域ID。 |
| CACertificateId | String | 是 | 139a0****-cn-qingdao- env17-d01 | CA证书ID。 |
| CACertificateName | String | 是 | mycacert02 | CA证书名称。长度为1~80个英文或中文字符，必须以大小字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-）。 |
| accesskeyid _ _ | String | 否 | acc-hp34s2h0xx1ht4nwo**** | 访问密钥ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FE7BA984 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetCACertificateName &RegionId=cn-qingdao-env17-d01 &CACertificateId=139a0****-cn-qingdao-env17-d01 &CACertificateName=mycacert02
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <SetCACertificateNameResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId> </SetCACertificateNameResponse> |  |

| JSON | 格式 |
|---|---|
| { "SetCACertificateNameResponse": { "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FE7BA984" } } |  |

#### 7.8.9. DescribeDomainExtensions

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 负载均衡实例的地域ID。 |

| 开发指南参 | 考 |  |  |  | 负载均衡 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| LoadBalancerId | String | Query | 是 | lb-bp1b6c719dfa08ex**** | 负载均衡实例的ID。 |
| ListenerPort | Integer | Query | 是 | 443 | 负载均衡实例HTTPS监听的前端端口，取值：1- 65535 。 |
| DomainExtensionId | String | Query | 否 | de-bp1rp7ta1**** | 扩展域名ID。 |
| Action | String | Query | 否 | DescribeDomainExtensions | 要执行的操作。取值： DescribeDomainExtensions。 |
| OwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 |  | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 |  | 鉴权相关的系统参数，不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 48C1B671-C6DB-4DDE-9B30- 10557E36CDE0 | 请求ID。 |
| DomainExtensions | Array |  | 扩展域名列表。 |
| -DomainExtensionId | String | de-bp1rp7ta1**** | 扩展域名ID。 |
| -Domain | String | www.example.com | 域名。 |
| -ServerCertificateId | String | 1231579085529123166f820468 _ 9171476340870998**** _ _ | 域名使用的证书ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDomainExtensions &RegionId=cn-hangzhou &LoadBalancerId=lb-bp1b6c719dfa08ex**** &ListenerPort=443
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"48C1B671-C6DB-4DDE-9B30-10557E36CDE0", "DomainExtensions":{ "DomainExtensionId":"de-bp1rp7ta1****", "ServerCertificateId":"1231579085529123_166f8204689_1714763408_70998****", "Domain":"www.example.com" } } |  |

| XML | 格式 |
|---|---|
| <RequestId>48C1B671-C6DB-4DDE-9B30-10557E36CDE0</RequestId> <DomainExtensions> <DomainExtensionId>de-bp1rp7ta1****</DomainExtensionId> <ServerCertificateId>1231579085529123_166f8204689_1714763408_70998****</ServerCertificateId> <Domain>www.example.com</Domain> </DomainExtensions> |  |

#### 7.8.10. DescribeCertificateRelations

用于查询指定证书在负载均衡中的关联关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 负载均衡

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeCertificateRelations | 系统规定参数。取值： DescribeCertificateRelations |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| ResourceOwnerAcc ount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| ResourceOwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-east-hangzhou-01 | 传统型负载均衡实例的地域ID。 |
| CertificateId | String | Query | 是 | 12345678-1234-1234-1234-12345678**** | 证书ID。 |
| CertType | String | Query | 是 | ca/server | 证书类型。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| Tags | String | Query | 否 | [{"tagKey":"Key1","tagValue":"Value1"}] | 传统型负载均衡实例绑定的标签列表，其结构是一个JSON dictionary，包含标签键和标签值。 一次请求中，绑定的标签列表中最多支持10个标签。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DomainExtensions | Array | uk | 扩展域名列表。 |
| -LoadBalancerId | String | lb-bp1b6c719dfa**** | 传统型负载均衡实例ID。 |
| -ListenerPort | Integer | 53 | 实例前端使用的端口。 |
| -DomainExtensionId | String | de-bp1rp7ta19****** | 扩展域名ID。 |
| -Domain | String | example.com | 域名。 |
| Listeners | Array | [{\"InstanceId\":\"ddosDip-sg- 4hr2b3l****\",\"FrontendPort\":20 20,\"Protocol\":\"udp\"}] | 监听列表。 |
| -LoadBalancerId | String | lb-bp1b6c719dfa**** | 传统型负载均衡实例ID。 |
| -ListenerPort | Integer | 53 | 实例前端使用的端口。 |
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCertificateRelations &RegionId=cn-east-hangzhou-01 &CertificateId=12345678-1234-1234-1234-12345678**** &CertType=cas
```

&公共请求参数正常返回示例 `JSON` 格式负载均衡

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "Listeners":[
  {
   "ListenerPort":53,
   "LoadBalancerId":"lb-bp1b6c719dfa****"
  }
```

`],`

```json
 "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984",
 "DomainExtensions":[
  {
   "ListenerPort":53,
   "DomainExtensionId":"de-bp1rp7ta19******",
   "LoadBalancerId":"lb-bp1b6c719dfa****",
   "Domain":"example.com"
  }
```

]

```
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | CertificateNotExist | CertificateNotExist | The specified CertificateId does not exist. |

### 后端服务器

#### 7.9.1. AddBackendServers

如果一次请求中添加多个相同的ECS实例，只会取第一个，其他相同实例会被忽略。新增后端服务器不能与同监听下已有服务器重复，否则会报错。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AddBackendServers | 要执行的操作。 取值：AddBackendServers。 |
| LoadBalancerId | String | 是 | lb-2ze7o5h52g02kkzz**** | 负载均衡实例ID。 |

负载均衡

| BackendServers |  | String | 是 |  |  | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"tes t-112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"tes | 要添加的后端服务器列表。 服务器列表需要包含以下参数： ServerId：String类型，必选，后端服务器的实例ID。分为ECS实例ID或者ENI实例ID，当ServerId参数值为ENI实例ID时，Type参数值必选。 Weight：后端服务器的权重。 取值：0~100。 默认值：100。 说明如果值为0，负载均衡不会将请求转发给该后端服务器。 Description ：String类型，非必选。长度为1~80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_），支持中文。 Type：后端服务器类型，取值： ecs（默认）: ECS实例 eni：弹性网卡实例 ServerIp：ECS或ENI的实例IP。 示例说明如下： 挂载ECS示例： [{ "ServerId": "i-xxxxxxxxx", |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | [{ "ServerId": "i-xxxxxxxxx", |  |  |
|  |  |  |  |  |  | t-113" }] | "Weight": "100", "Type": "ecs", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI： | [{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "192.168.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI多IP： |  | [{ "ServerId": "eni-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "eni", "ServerIp": |  |  |  |  |
|  |  |  |  |  |  |  | "192.168.**.**", "Port":"80","Description":"test- |  |  |  |  |
|  |  |  |  |  |  |  | 112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "172.166.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-113" }] |  |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LoadBalancerId | String | lb-2ze7o5h52g02kkzz**** | 负载均衡实例ID。 |
| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | i-2zej4lxhjoq1icu**** | ECS实例ID或ENI的实例ID。 |
| Weight | String | 100 | 后端服务器的权重。 取值：0~100 默认值为100，如果值为0，则不会将请求转发给该后端服务器。 |
| Description | String | 后端服务器 | 后端服务器描述。 |
| RequestId | String | 34B82C81-F13B-4EEB-99F6- A048C67CC830 | 请求ID。 |

**示例**

请求示例

```
&LoadBalancerId=lb-2ze7o5h52g02kkzz****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式负载均衡

```xml
    <BackendServers>
        <BackendServer>
            <ServerId>i-2zej4lxhjoq1icu*****</ServerId>
            <Weight>100</Weight>
            <Type>ecs</Type>
        </BackendServer>
        <BackendServer>
            <ServerId>i-2ze1u9ywulp5pbv*****</ServerId>
            <Weight>100</Weight>
            <Type>ecs</Type>
        </BackendServer>
    </BackendServers>
    <RequestId>34B82C81-F13B-4EEB-99F6-A048C67CC830</RequestId>
    <LoadBalancerId>lb-2ze7o5h52g02kkzz*****</LoadBalancerId>
```

| JSON | 格式 |
|---|---|
| { "AddBackendServersResponse": { "BackendServers": { "BackendServer": [ { "ServerId": "i-2zej4lxhjoq1icu*****", "Weight": 100, "Type": "ecs" }, { "ServerId": "i-2ze1u9ywulp5pbv*****", "Weight": 100, "Type": "ecs" } ] }, "RequestId": "34B82C81-F13B-4EEB-99F6-A048C67CC830", "LoadBalancerId": "lb-2ze7o5h52g02kkzz*****" } } |  |

#### 7.9.2. RemoveBackendServers

如果要移除的后端服务器不在指定的负载均衡实例的服务器列表中，会直接忽略，不会报错。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 |  |  | 示例值 | 描述 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Action | String | 是 |  |  | RemoveBackendServers | 要执行的操作。 取值：RemoveBackendServers。 |  |  |  |
| BackendServers | String | 是 |  |  | [{"ServerId":"i- 2zej4lxhjoq****", "Type": "ecs","Weight":"100"}] | 要移除的后端服务器。 ServerId：String类型，必选，后端服务器ID。 Weight：Integer类型，必选，后端服务器的权重，取值范围：0~100。 Type：后端服务器类型，取值： ecs: ECS实例（默认） eni：弹性网卡实例说明一次调用最多可以移除20个后端服务器。 示例说明如下： 移除ECS： [{"ServerId":"i-2zej4lxhjoq***", "Type": |  |  |  |
|  |  |  |  |  |  |  | [{"ServerId":"i-2zej4lxhjoq***", "Type": |  |  |
|  |  |  |  |  |  | "ecs","Weight":"100"}] |  |  |  |
|  |  |  |  |  |  | 移除ENI： | [{"ServerId":"eni-2ze1sdp5***","Type": |  |  |
|  |  |  |  |  |  | "eni","Weight":"100"}] |  |  |  |
| LoadBalancerId | String | 是 |  |  | lb-bp1qjwo61pqz3ahl**** | 负载均衡实例ID。 |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LoadBalancerId | String | lb-bp1vjkb671z53**** | 负载均衡实例ID。 |

负载均衡

| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
|---|---|---|---|
| BackendServer |  |  |  |
| ServerId | String | i-jjgjgjgggd**** | 后端服务器的实例ID。 |
| Weight | Integer | 100 | 后端服务器的权重，范围为0~100。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveBackendServers &BackendServers=[{"ServerId":"i-2zej4lxhjoq****", "Type": "ecs","Weight":"100"}] &LoadBalancerId=lb-bp1qjwo61pqz3ahl****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RemoveBackendServersResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <LoadBalancerId>lb-bp1vjkb671z53cy******</LoadBalancerId> <BackendServers> <BackendServer> <ServerId>i-jjgjgjg*****</ServerId> <Weight>100</Weight> </BackendServer> <BackendServer> <ServerId>i-jjgjgituitu****</ServerId> <Weight>100</Weight> </BackendServer> </BackendServers> </RemoveBackendServersResponse> |  |

| JSON | 格式 |
|---|---|
| { "RemoveBackendServers": { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "LoadBalancerId": "lb-bp1vjkb671z53cy******", "BackendServers": { "BackendServer": [ { "ServerId": "i-jjgjgjg*****", "Weight": 100 }, { "ServerId": "i-jjgjgituitu****", "Weight": 100 } ] } } } |  |

#### 7.9.3. SetBackendServers

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetBackendServers | 要执行的操作。 取值：SetBackendServers。 |
| LoadBalancerId | String | 是 | lb-bp1qjwo61pqz3a**** | 负载均衡实例ID。 |

负载均衡

| BackendServers |  | String | 是 |  |  | [{ "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description":"tes | 要添加的后端服务器列表。 取值：是一个Json string，其结构是一个JsonList。一次请求中，列表中最多支持20个元素。 ServerId：String类型，必选，后端服务器的实例ID。 Port：Integer类型，必选，后端服务器使用的端口，取值范围：1~65535。 Weight：Integer类型，必选，后端服务器的权重，取值范围：0~100。 Description ：String类型，非必选，后端服务器描述，长度为1- 80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_），支持中文。 Type：String类型，表示后端服务器的实例类型，取值： ecs（默认）: ECS实例。 eni：弹性网卡实例。 ServerIp：ECS或ENI的实例IP。 示例说明如下： 挂载ECS示例： [{ "ServerId": "i-xxxxxxxxx", |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | [{ "ServerId": "i-xxxxxxxxx", |  |  |
|  |  |  |  |  |  | t-112" }] | "Weight": "100", "Type": "ecs", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI： | [{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "192.168.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI多IP： |  | [{ "ServerId": "eni-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "eni", "ServerIp": |  |  |  |  |
|  |  |  |  |  |  |  | "192.168.**.**", "Port":"80","Description":"test- |  |  |  |  |
|  |  |  |  |  |  |  | 112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "172.166.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-113" }] |  |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| LoadBalancerId | String | lb-bp1qjwo61pqz3a**** | 负载均衡实例ID。 |
| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | eni-hg231**** | ECS实例ID。 |
| Weight | String | 100 | 后端服务器的权重。 |
| Description | String | 后端服务器 | 后端服务器描述。 |
| Type | String | ecs | 后端服务器类型，取值： ecs（默认）：ECS实例。 eni：弹性网卡实例。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
&LoadBalancerId=lb-bp1qjwo61pqz3a****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式负载均衡

```xml
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <LoadBalancerId>lb-dhf13*******</LoadBalancerId>
      <BackendServers>
            <BackendServer>
                  <ServerId>eni-hg231**</ServerId>
                  <Weight>100</Weight>
                              <Type>eni</Type>
            </BackendServer>
            <BackendServer>
                  <ServerId>eni-hfhf***</ServerId>
                  <Weight>100</Weight>
                              <Type>eni</Type>
            </BackendServer>
      </BackendServers>
```

| JSON | 格式 |
|---|---|
| { "SetBackendServersResponse": { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "LoadBalancerId": "lb-dhf13*******", "BackendServers": { "BackendServer": [ { "ServerId": "eni-hg231**", "Weight": 100, "Type": "eni" }, { "ServerId": "eni-hfhf***", "Weight": 100, "Type": "eni" } ] } } } |  |

### 虚拟服务器组

#### 7.10.1. CreateVServerGroup

调用CreateVServerGroup添加后端服务器组并向指定的后端服务器组中添加后端服务器。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateVServerGroup | 要执行的操作。 取值：CreateVServerGroup。 |
| LoadBalancerId | String | 是 | lb-bp1qjwo61pqz3ahl**** | 负载均衡实例ID。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡地域ID。 |
| VServerGroupName | String | 否 | Group1 | 虚拟服务器组名称。 长度限制为1~80个字符，只允许包含中文、字母、数字、短划线 （-）、正斜线（/）、英文句点（.）和下划线（_）。 |

负载均衡

| BackendServers |  | String | 否 |  |  | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"tes t-112" }, { "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"tes | 需要添加的后端服务器列表。 取值：是一个Json string，其结构是一个JsonList。一次请求中，List 中的元素个数最多20个。 ServerId：String类型，必选，后端服务器实例ID，为ECS实例ID 或者ENI实例ID。 Port：Integer类型，必选，后端服务器使用的端口，取值范围：1~65535。 Weight：Integer类型，必选，后端服务器的权重，取值范围：0~100。 Description ：String类型，非必选，后端服务器描述，长度为 1~80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、 英文句点（.）和下划线（_），支持中文。 Type：String类型，必选，表示后端服务器的实例类型，取值： ecs（默认）：ECS实例。 eni：弹性网卡实例。 ServerIp：ECS或者ENI的实例IP。 示例说明如下： 挂载ECS示例： [{ "ServerId": "i-xxxxxxxxx", |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | [{ "ServerId": "i-xxxxxxxxx", |  |  |
|  |  |  |  |  |  | t-112" }] | "Weight": "100", "Type": "ecs", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI： | [{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "192.168.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI多IP： |  | [{ "ServerId": "eni-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "eni", "ServerIp": |  |  |  |  |
|  |  |  |  |  |  |  | "192.168.**.**", "Port":"80","Description":"test- |  |  |  |  |
|  |  |  |  |  |  |  | 112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "172.166.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-113" }] |  |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | 后端服务器组ID。 |
| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | vm-2**** | ECS实例ID或ENI实例ID。 |
| Port | Integer | 70 | 后端服务器使用的端口。 |
| Weight | Integer | 100 | 后端服务器的权重。 |
| Description | String | 后端服务器组 | 后端服务器组描述。 |
| ServerType | String | ECS |  |
| Type | String | Type | 后端服务器类型，取值： ecs（默认）：ECS实例。 eni：弹性网卡实例。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateVServerGroup &LoadBalancerId=lb-bp1qjwo61pqz3ahl**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式负载均衡

```xml
  <VServerGroupId>rsp-bp1i4c******</VServerGroupId>
  <RequestId>3EBBDBAE-8E8B-438F-A109-95C2FDB2C333</RequestId>
  <BackendServers>
        <BackendServer>
              <Type>ecs</Type>
              <ServerId>i-bp1ds2yjlk66********</ServerId>
              <Description>test-11244</Description>
              <Port>80</Port>
              <Weight>100</Weight>
        </BackendServer>
  </BackendServers>
```

| JSON | 格式 |
|---|---|
| { "VServerGroupId": "rsp-bp1i4c3******", "RequestId": "3EBBDBAE-8E8B-438F-A109-95C2FDB2C333", "BackendServers": { "BackendServer": [ { "Type": "ecs", "ServerId": "i-bp1ds2yjlk666******", "Description": "test-11244", "Port": 80, "Weight": 100 } ] } } |  |

#### 7.10.2. SetVServerGroupAttribute

如果您需要修改后端服务器组，请参见接口 `ModifyVServerGroupBackendServers` 。 如果您需要添加后端服务器，请参见接口 `AddVServerGroupBackendServers` 。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetVServerGroupAttribute | 要执行的操作。 取值：SetVServerGroupAttribute。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡地域ID。 |
| VServerGroupId | String | 是 | rsp-cige6**** | 后端服务器组ID。 |
| VServerGroupName | String | 否 | vserver-group-test | 虚拟服务器组名称。 |

负载均衡

| BackendServers |  | String | 否 |  |  | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"tes t-112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"tes | 虚拟服务器组列表。 单次调用最多可添加20个后端服务器。 ServerId：String类型，必选，后端服务器的实例ID或ENI实例 ID。 Port：Integer类型，必选，后端服务器使用的端口，取值范围：1~65535。 Weight：Integer类型，必选，后端服务器的权重，取值范围：0~100。 Description ：String类型，非必选，后端服务器描述，长度为 1~80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、 半角句号（.）和下划线（_），支持中文。 Type：String类型，表示后端服务器的实例类型，取值： ecs（默认）：ECS实例。 eni：弹性网卡实例。 ServerIp：ECS或ENI的实例IP。 示例说明如下： 挂载ECS示例： [{ "ServerId": "i-xxxxxxxxx", |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | [{ "ServerId": "i-xxxxxxxxx", |  |  |
|  |  |  |  |  |  | t-113" }] | "Weight": "100", "Type": "ecs", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI： | [{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "192.168.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI多IP： |  | [{ "ServerId": "eni-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "eni", "ServerIp": |  |  |  |  |
|  |  |  |  |  |  |  | "192.168.**.**", "Port":"80","Description":"test- |  |  |  |  |
|  |  |  |  |  |  |  | 112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "172.166.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-113" }] |  |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | 服务器组ID。 |
| VServerGroupName | String | Group1 | 虚拟服务器组名称。 |
| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | i-bp1ek6yd7jvkx**** | ECS实例ID或ENI实例ID。 |
| Port | Integer | 70 | 后端服务器使用的端口。 |
| Weight | Integer | 100 | 后端服务器的权重。 |
| Description | String | 后端服务器组描述。 | 后端服务器组描述。 |
| Type | String | ecs | 后端服务器类型，取值： ecs：ECS实例。 eni：弹性网卡实例。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetVServerGroupAttribute &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式负载均衡

```xml
  <BackendServers>
        <BackendServer>
              <ServerId>i-bp1ek6yd7jvkx*****</ServerId>
              <Port>80</Port>
              <Weight>100</Weight>
              <Type>ecs</Type>
        </BackendServer>
  </BackendServers>
  <RequestId>A4FDF333-F904-4540-88FC-ED6F87AEFFCB</RequestId>
  <VServerGroupId>rsp-bp1d2e3*****</VServerGroupId>
  <VServerGroupName>test1</VServerGroupName>
```

| JSON | 格式 |
|---|---|
| {"VServerGroupId":"rsp-cige6****","RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C","VServerGroupName":"Group1","BackendServers": [{"Type":"ecs","Description":"后端服务器组描述。","ServerId":"i-bp1ek6yd7jvkx****","Port":"70","Weight":"100"}]} |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | The VServerGroupName or BackendServers is required at lease one. | 参数VServerGroupName和BackendServers至少需要配置一个。 |
| 400 | InvalidParameter.ZoneNotSuppor t | The zone does not support the parameter %s. | 当前可用区不支持指定参数。 |

#### 7.10.3. AddVServerGroupBackendServers

调用AddVServerGroupBackendServers向指定的后端服务器组中添加后端服务器。

**请求参数**

| 名称 |  | 类型 | 是否必选 |  |  | 示例值 | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Action |  | String | 是 |  |  | AddVServerGroupBackendSe rvers | 要执行的操作。 取值：AddVServerGroupBackendServers。 |  |  |  |  |
| BackendServers |  | String | 是 |  |  | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6*", "Port":"80","Description":"tes t-112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", | 服务器组列表。单次调用最多可添加20个后端服务器。 服务器组列表需要包含以下参数： ServerId：后端服务器的实例ID。为ECS实例ID或者ENI实例ID。 Port：必选参数，表示后端服务器使用的端口。取值范围：1~65535。 Weight：后端服务器的权重，取值：0~100。默认值为100。如果值为0，则不会将请求转发给该后端服务器。 Type：后端服务器类型，取值： ecs： ECS实例（默认）。 eni：弹性网卡实例。 Description：String类型，非必选，后端服务器描述，长度为 1~80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、 英文句点（.）和下划线（_），支持中文。 ServerIp：ECS或者ENI的实例IP。 示例说明如下： 挂载ECS示例： [{ "ServerId": "i-xxxxxxxxx", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | [{ "ServerId": "i-xxxxxxxxx", |  |  |
|  |  |  |  |  |  | "Port":"80","Description":"tes t-113" }] | "Weight": "100", "Type": "ecs", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI： | [{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "192.168.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI多IP： |  | [{ "ServerId": "eni-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "eni", "ServerIp": |  |  |  |  |
|  |  |  |  |  |  |  | "192.168.**.**", "Port":"80","Description":"test- |  |  |  |  |
|  |  |  |  |  |  |  | 112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "172.166.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-113" }] |  |  |  |  |
| RegionId |  | String | 是 |  |  | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |  |  |  |  |
| VServerGroupId |  | String | 是 |  |  | rsp-cige6**** | 服务器组ID。 |  |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | 服务器组ID。 |

负载均衡

| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
|---|---|---|---|
| BackendServer |  |  |  |
| ServerId | String | vm-231 | ECS实例ID或者ENI实例ID。 |
| Port | Integer | 70 | 后端服务器使用的端口。 |
| Weight | Integer | 100 | 后端服务器的权重。 |
| Description | String | test | 后端服务器组描述。 |
| Type | String | ecs | 后端服务器类型，取值： ecs（默认）：ECS实例。 eni：弹性网卡实例。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"test-112 " },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"test-113" }] &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <AddVServerGroupBackendServersResponse> <VServerGroupId>rsp-cige6j******</VServerGroupId> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <BackendServers> <Type>ecs</Type> <Description>test</Description> <ServerId>vm-231</ServerId> <Weight>100</Weight> <Port>70</Port> </BackendServers> </AddVServerGroupBackendServersResponse> |  |

| JSON | 格式 |
|---|---|
| {"VServerGroupId":"rsp-cige6j******", "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "BackendServers":[ {"Type":"ecs","Description":"test","ServerId":"vm-231","Weight":"100","Port":"70"} ] } |  |

#### 7.10.4. RemoveVServerGroupBackendServers

调用RemoveVServerGroupBackendServers从指定的后端服务器组中移除后端服务器。 如果**BackendServers**中参数的某些后端服务器不存在于这个虚拟服务器组中，会直接忽略，不会报错。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RemoveVServerGroupBacken dServers | 要执行的操作。 取值：RemoveVServerGroupBackendServers。 |

负载均衡

| BackendServers | String | 是 | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"tes t-112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"tes t-113" }] | 后端服务器组列表。 单次调用每个服务器组最多可包含20个后端服务器。 取值：是一个Json string，其结构是一个JsonList。一次请求中，列表中最多支持20个元素。 ServerId：String类型，必选，后端服务器的实例ID，为ECS实例 ID或者ENI实例ID。 Port：Integer类型，必选，后端服务器使用的端口，取值范围：1~65535。 Weight：Integer类型，必选，后端服务器的权重，取值范围：0~100。 Description ：String类型，非必选，后端服务器描述，长度为 1~80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、 英文句点（.）和下划线（_），支持中文。 Type：String类型，表示后端服务器的实例类型，取值： ecs：ECS实例（默认）。 eni：弹性网卡实例。 ServerIp：ECS或者ENI的实例IP。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |
| VServerGroupId | String | 是 | rsp-cige6**** | 后端服务器组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | 服务器组ID。 |
| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | vm-230 | ECS实例ID或ENI的实例ID。 |
| Port | Integer | 80 | 后端服务器使用的端口。 |
| Weight | Integer | 100 | 后端服务器的权重。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"test-112 " },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"test-113" }] &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RemoveVServerGroupBackendServersResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <VServerGroupId>rsp-cige6******</VServerGroupId> <BackendServers> <BackendServer> <ServerId>vm-231</ServerId> <Port>70</Port> <Weight>100</Weight> <Type>ecs</Type> </BackendServer> </BackendServers> </RemoveVServerGroupBackendServersResponse> |  |

`JSON` 格式负载均衡

```json
{
  "RemoveVServerGroupBackendServersResponse": {
    "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
    "VServerGroupId": "rsp-cige6******",
    "BackendServers": {
      "BackendServer": {
        "ServerId": "vm-231",
        "Port": "70",
        "Weight": "100",
        "Type": "ecs"
      }
    }
  }
}
```

#### 7.10.5. ModifyVServerGroupBackendServers

调用ModifyVServerGroupBackendServers替换服务器组中的后端服务器。 该接口只用于替换服务器中的后端服务器，如果您需要修改后端服务器的端口权重等配置，请参见 `SetVServerGroupAttribute` 。

**请求参数**

| 名称 |  | 类型 | 是否必选 |  |  | 示例值 | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Action |  | String | 是 |  |  | ModifyVServerGroupBackend Servers | 要执行的操作。 取值：ModifyVServerGroupBackendServers。 |  |  |  |  |
| RegionId |  | String | 是 |  |  | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |  |  |  |  |
| VServerGroupId |  | String | 是 |  |  | rsp-cige6j**** | 服务器组ID。 |  |  |  |  |
| OldBackendServers |  | String | 否 |  |  | [{ "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description":"tes t-112" }] | 要被替换的后端服务器列表。 取值：是一个Json string，其结构是一个JsonList。一次请求中，列表中最多支持20个元素。 ServerId：String类型，必选，后端服务器的实例ID。 Port：Integer类型，必选，后端服务器使用的端口，取值范围：1~65535。 Weight：Integer类型，必选，后端服务器的权重，取值范围：0~100。 Description ：String类型，非必选，后端服务器描述，长度为 1~80个字符，支持字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_），支持中文。 Type：String类型，表示后端服务器的实例类型，取值： ecs（默认）：ECS实例。 eni：弹性网卡实例。 ServerIp：ECS或ENI的实例IP。 示例说明如下： 挂载ECS示例： [{ "ServerId": "i-xxxxxxxxx", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | [{ "ServerId": "i-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "ecs", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI： | [{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "192.168.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI多IP： |  | [{ "ServerId": "eni-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "eni", "ServerIp": |  |  |  |  |
|  |  |  |  |  |  |  | "192.168.**.**", "Port":"80","Description":"test- |  |  |  |  |
|  |  |  |  |  |  |  | 112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "172.166.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-113" }] |  |  |  |  |

负载均衡

| NewBackendServers |  | String | 否 |  |  | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"tes t-112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"tes t-113" }] | 新的后端服务器列表。 单次调用每个服务器组最多可调用20个后端服务器。 取值：是一个Json string，其结构是一个JsonList。一次请求中，列表中最多支持20个元素。 ServerId：String类型，必选，后端服务器的实例ID。 Port：Integer类型，必选，后端服务器使用的端口，取值范围：1~65535。 Weight：Integer类型，必选，后端服务器的权重，取值范围：0~100。 Description ：String类型，非必选，后端服务器描述，允许包含字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线 （_），支持中文。 Type：String类型，表示后端服务器的实例类型，取值： ecs（默认）： ECS实例。 eni：弹性网卡实例。 ServerIp：ECS或ENI的实例IP。 示例说明如下： 挂载ECS示例： [{ "ServerId": "i-xxxxxxxxx", |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | [{ "ServerId": "i-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "ecs", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI： | [{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "192.168.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-112" }] |  |  |  |  |
|  |  |  |  |  |  |  | 挂载ENI多IP： |  | [{ "ServerId": "eni-xxxxxxxxx", |  |  |
|  |  |  |  |  |  |  | "Weight": "100", "Type": "eni", "ServerIp": |  |  |  |  |
|  |  |  |  |  |  |  | "192.168.**.**", "Port":"80","Description":"test- |  |  |  |  |
|  |  |  |  |  |  |  | 112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |  |  |
|  |  |  |  |  |  |  | "100", "Type": "eni", "ServerIp": "172.166.**.**", |  |  |  |  |
|  |  |  |  |  |  |  | "Port":"80","Description":"test-113" }] |  |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | 服务器组ID。 |
| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | vm-236 | ECS实例ID或ENI的实例ID。 |
| Port | Integer | 70 | 后端服务器使用的端口。 |
| Weight | Integer | 100 | 后端服务器的权重。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyVServerGroupBackendServers &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6j****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <ModifyVServerGroupBackendServersResponse> <VServerGroupId>rsp-cige6j******</VServerGroupId> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <BackendServers> <ServerId>vm-236</ServerId> <Weight>100</Weight> <Port>70</Port> </BackendServers> </ModifyVServerGroupBackendServersResponse> |  |

`JSON` 格式负载均衡

```json
{
    "ModifyVServerGroupBackendServersResponse": {
        "VServerGroupId": "rsp-cige6j******",
        "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
        "BackendServers": {
            "ServerId": "vm-236",
            "Weight": 100,
            "Port": 70
        }
    }
}
```

#### 7.10.6. DeleteVServerGroup

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteVServerGroup | 要执行的操作。 取值：DeleteVServerGroup。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |
| VServerGroupId | String | 是 | rsp-cige6j**** | 服务器组ID。 说明如果服务器组被引用，将无法删除。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteVServerGroup &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6j****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteVServerGroupResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> </DeleteVServerGroupResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C" } |  |

#### 7.10.7. DescribeVServerGroups

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVServerGroups | 要执行的操作。 取值：DescribeVServerGroups。 |
| LoadBalancerId | String | 是 | lb-bp1o94dp5i6ea**** | 负载均衡实例ID。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

负载均衡

| VServerGroups | Array of VServerGroup |  | 后端服务器列表。 |
|---|---|---|---|
| VServerGroup |  |  |  |
| VServerGroupId | String | rsp-bp1oygn**** | 服务器组ID。 |
| VServerGroupName | String | k8s/31065/nginx-ingress-lb/kube- system/clust****" | 服务器组名称。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVServerGroups &LoadBalancerId=lb-bp1o94dp5i6ea**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeVServerGroupsResponse> <VServerGroups> <VServerGroup> <VServerGroupId>rsp-bp1oygn******</VServerGroupId> <VServerGroupName>k8s/31065/nginx-ingress-lb/kube-system/clust****</VServerGroupName> <AssociatedObjects> <Listeners> </Listeners> <Rules> </Rules> </AssociatedObjects> </VServerGroup> <VServerGroup> <VServerGroupId>rsp-bp1i6sn******</VServerGroupId> <VServerGroupName>k8s/31605/nginx-ingress-lb/kube-system/clusterid</VServerGroupName> <AssociatedObjects> <Listeners> </Listeners> <Rules> </Rules> </AssociatedObjects> </VServerGroup> <VServerGroup> <VServerGroupId>rsp-bp1f85n******</VServerGroupId> <VServerGroupName>VSG1</VServerGroupName> <AssociatedObjects> <Listeners> </Listeners> <Rules> </Rules> </AssociatedObjects> </VServerGroup> </VServerGroups> <RequestId>31ADDBCD-275F-4C37-B0A3-5DFC8564E686</RequestId> </DescribeVServerGroupsResponse> |  |

`JSON` 格式负载均衡

```json
{
 "VServerGroups": {
  "VServerGroup": [
   {
    "VServerGroupId": "rsp-bp1oygn******",
    "VServerGroupName": "k8s/31065/nginx-ingress-lb/kube-system/clust****",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
     },
     "Rules": {
      "Rule": []
     }
    }
   },
   {
    "VServerGroupId": "rsp-bp1i6sn******",
    "VServerGroupName": "k8s/31605/nginx-ingress-lb/kube-system/clusterid",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
     },
     "Rules": {
      "Rule": []
     }
    }
   },
   {
    "VServerGroupId": "rsp-bp1f85n******",
    "VServerGroupName": "VSG1",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
     },
     "Rules": {
      "Rule": []
     }
    }
   }
```

]

```json
 },
 "RequestId": "31ADDBCD-275F-4C37-B0A3-5DFC8564E686"
}
```

#### 7.10.8. DescribeVServerGroupAttribute

调用DescribeVServerGroupAttribute查询服务器组的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVServerGroupAttribu te | 要执行的操作。 取值：DescribeVServerGroupAttribute。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |
| VServerGroupId | String | 是 | rsp-cige6**** | 虚拟服务器组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | 虚拟服务器组ID。 |
| VServerGroupName | String | Group1 | 虚拟服务器组名称。长度为1~80个字符，支持中文、字母、数字、短划线 （-）、正斜线（/）、英文句点（.）和下划线（_）。 |
| BackendServers | Array of BackendServer |  | 后端服务器列表。 |
| BackendServer |  |  |  |
| ServerId | String | vm-233 | ECS实例ID。 |
| Port | Integer | 90 | 后端服务器使用的端口。 |
| Weight | Integer | 100 | 后端服务器的权重。 |

负载均衡

| Description | String | 服务器组描述。 | 服务器组描述。 |
|---|---|---|---|
| ServerType | String | ecs |  |
| Type | String | ecs | 后端服务器类型，取值： ecs（默认）：ECS实例 eni：弹性网卡实例 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVServerGroupAttribute &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6****
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeVServerGroupAttributeResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <VServerGroupId>rsp-cige6******</VServerGroupId> <VServerGroupName>Group1</VServerGroupName> <BackendServers> <BackendServer> <ServerId>vm-232</ServerId> <Port>80</Port> <Weight>100</Weight> </BackendServer> <BackendServer> <ServerId>vm-233</ServerId> <Port>90</Port> <Weight>100</Weight> </BackendServer> </BackendServers> </DescribeVServerGroupAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| {"VServerGroupId":"rsp-cige6*****","RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C","VServerGroupName":"Group1","BackendServers": [{"ServerType":"ecs","Type":"ecs","ServerId":"vm-233","Description":"服务器组描述。","VpcId":"vpc- **","Port":"90","ServerIp":"192.168.*.*","Weight":"100"}]} |  |

### 主备服务器组

#### 7.11.1. CreateMasterSlaveServerGroup

调用CreateMasterSlaveServerGroup创建主备服务器组。一个主备服务器组只能包含两个ECS实例，一个为主服务器，另一个为备服务器。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateMasterSlaveServerGro up | 要执行的操作。 取值：CreateMasterSlaveServerGroup。 |
| LoadBalancerId | String | 是 | lb-bp1hv944r69al4j**** | 负载均衡实例ID。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |
| MasterSlaveServerGroupNam e | String | 否 | sg-atstuj3rtopty**** | 主备虚拟服务器组名称。 |

负载均衡

|  | MasterSlaveBackendServers |  | String | 否 |  |  |  | [{ "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","ServerType":"Ma ster","Description":"test-112" }, { "ServerId": "i- | 主备服务器组列表。 取值：是一个Json string，其结构是一个JsonList。一次请求中，列表中最多支持20个元素。 ServerId：String类型，必选，后端服务器实例ID。 Port：Integer类型，必选，后端服务器使用的端口，取值范围：1~65535。 Weight：Integer类型，必选，后端服务器的权重，取值范围：0~100。 Description ：String类型，非必选，后端服务器描述，长度为 1~80个字符，允许包含字母、数字、短划线（-）、正斜线（/）、 半角句号（.）和下划线（_）。支持中文。 ServerType：String类型，表示后端服务器的主备类型，取值： Master：主服务器。 Slave：备服务器。 Type：String类型，表示后端服务器的实例类型，取值： ecs（默认）：ECS实例。 eni：弹性网卡实例。 ServerIp：ECS或者ENI的实例IP。 一个主备服务器组最多可包含2个后端服务器。 如果不指定该参数，则创建一个空的主备服务器组列表。 示例说明如下： 挂载ECS： [{ "ServerId": "i-xxxxxxxxx", "Weight": |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | [{ "ServerId": "i-xxxxxxxxx", "Weight": |  |  |
|  |  |  |  |  |  |  |  | xxxxxxxxx", "Weight": "100", | "100", "Type": "ecs", |  |  |  |
|  |  |  |  |  |  |  |  | "Type": "ecs", | "Port":"80","ServerType":"Master","Description":"tes |  |  |  |
|  |  |  |  |  |  |  |  | "Port":"80","ServerType":"Sla | -112" }, |  |  |  |
|  |  |  |  |  |  |  |  | ve","Description":"test-112" }] | { "ServerId": "i-xxxxxxxxx", "Weight": "100", |  |  |  |
|  |  |  |  |  |  |  |  |  | "Type": "ecs", |  |  |  |
|  |  |  |  |  |  |  |  |  | "Port":"80","ServerType":"Slave","Description":"test |  |  | - |
|  |  |  |  |  |  |  |  |  | 112" }] |  |  |  |
|  |  |  |  |  |  |  |  |  | 挂载ENI： | [{ "ServerId": "eni-xxxxxxxxx", "Weight": |  |  |
|  |  |  |  |  |  |  |  |  | "100", "Type": "eni", |  |  |  |
|  |  |  |  |  |  |  |  |  | "Port":"80","ServerType":"Master","Description":"tes |  |  |  |
|  |  |  |  |  |  |  |  |  | -112" }, |  |  |  |
|  |  |  |  |  |  |  |  |  | { "ServerId": "eni-xxxxxxxxx", "Weight": "100", |  |  |  |
|  |  |  |  |  |  |  |  |  | "Type": "eni", "ServerIp": "192.168.**.**", |  |  |  |
|  |  |  |  |  |  |  |  |  | "Port":"80","ServerType":"Slave","Description":"test |  |  | - |
|  |  |  |  |  |  |  |  |  | 112" }] |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | [{ "ServerId": "eni-xxxxxxxxx", |  |
|  |  |  |  |  |  |  |  |  | "Weight": "100", "Type": "eni","ServerIp": |  |  |  |
|  |  |  |  |  |  |  |  |  | "192.168.**.**", |  |  |  |
|  |  |  |  |  |  |  |  |  | "Port":"80","ServerType":"Master","Description":"tes |  |  |  |
|  |  |  |  |  |  |  |  |  | -112" }, |  |  |  |
|  |  |  |  |  |  |  |  |  | { "ServerId": "eni-xxxxxxxxx", "Weight": "100", |  |  |  |
|  |  |  |  |  |  |  |  |  | "Type": "eni","ServerIp": "192.168.**.**", |  |  |  |
|  |  |  |  |  |  |  |  |  | "Port":"80","ServerType":"Slave","Description":"test |  |  | - |
|  |  |  |  |  |  |  |  |  | 112" }] |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MasterSlaveServerGroupI d | String | rsp-cige6j**** | 主备服务器组ID。 |
| MasterSlaveBackendServe rs | Array of MasterSlaveBackendServe r |  | 主备服务器组列表。 |
| MasterSlaveBackendServe r |  |  |  |
| ServerId | String | vm-2h**** | 要添加的ECS实例ID或者ENI实例ID。 |
| Port | Integer | 90 | 后端服务器使用的端口。 |
| Weight | Integer | 100 | 后端服务器的权重。 |
| ServerType | String | Slave | 服务器类型。 取值：Master（默认值）或Slave。 |
| Description | String | 主备服务器组描述。 | 主备服务器组描述。长度限制为1~80个字符，只允许包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）。 |
| Type | String | ecs | 后端服务器类型，取值： ecs（默认）：ECS实例 eni：弹性网卡实例 |

负载均衡

| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateMasterSlaveServerGroup &LoadBalancerId=lb-bp1hv944r69al4j**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <CreateMasterSlaveServerGroupResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <MasterSlaveServerGroupId>rsp-cige******</MasterSlaveServerGroupId> <MasterSlaveBackendServers> <MasterSlaveBackendServers> <ServerId>vm-gtgt***</ServerId> <Port>80</Port> <Weight>100</Weight> <ServerType>Master</ServerType> </MasterSlaveBackendServers> <MasterSlaveBackendServers> <ServerId>vm-tygtyg****</ServerId> <Port>90</Port> <Weight>100</Weight> <ServerType>Slave</ServerType> </MasterSlaveBackendServers> </MasterSlaveBackendServers> </CreateMasterSlaveServerGroupResponse> |  |

| JSON | 格式 |
|---|---|
| { "CreateMasterSlaveServerGroupResponse": { "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "MasterSlaveServerGroupId": "rsp-cige******", "MasterSlaveBackendServers": { "MasterSlaveBackendServers": [ { "ServerId": "vm-gtgt***", "Port": 80, "Weight": 100, "ServerType": "Master" }, { "ServerId": "vm-tygtyg****", "Port": 90, "Weight": 100, "ServerType": "Slave" } ] } } } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | BACKENDSERVERSNUMMUST _ _ _ _ BETWO _ | Backend servers num must be 2. | 后端服务器数量必须是2。 |
| 400 | BACKENDSERVERSHAVESAME _ _ _ _ PORTANDSERVERID _ _ | Backend servers have same port and serverId. | 后端服务器组中已存在具有相同的端口和服务器ID的虚拟服务器。 |
| 400 | BACKENDSERVERSCANONLYC _ _ _ _ ONTAINONEMASTERANDONE _ _ _ _ _ SLAVE | Backend servers can only contain one master and one slave. | 主备虚拟服务器组只能包含一个主服务器和一个备服务器。 |
| 400 | BACKENDSERVERIDCANNOT _ _ _ _ _ EMPTY | Backend server id can not empty. | 后端服务器ID不能为空。 |
| 400 | INVALIDSERVERTYPE _ _ | Invalid server type. | 非法的服务器类型。 |
| 400 | BACKENDSERVERPORTCANN _ _ _ _ OTEMPTY _ | Backend server port can not empty. | 后端服务器端口不允许为空。 |
| 400 | RealServerPortNotSupport | Real server port not support. | 后端服务器端口不支持。 |

#### 7.11.2. DeleteMasterSlaveServerGroup

调用DeleteMasterSlaveServerGroup删除指定的主备服务器组。 负载均衡

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteMasterSlaveServerGro up | 要执行的操作。 取值：DeleteMasterSlaveServerGroup。 |
| MasterSlaveServerGroupId | String | 是 | rsp-cige6**** | 主备服务器组ID。 说明如果主备服务器组正在使用中，无法删除。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteMasterSlaveServerGroup &MasterSlaveServerGroupId=rsp-cige6**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DeleteMasterSlaveServerGroupResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> </DeleteMasterSlaveServerGroupResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C" } |  |

#### 7.11.3. DescribeMasterSlaveServerGroups

调用DescribeMasterSlaveServerGroups查询主备服务器组列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMasterSlaveServerG roups | 要执行的操作。 取值：DescribeMasterSlaveServerGroups。 |
| LoadBalancerId | String | 是 | lb-bp14zi0n66zpg6o**** | 负载均衡实例ID。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MasterSlaveServerGroups | Array of MasterSlaveServerGroup |  | 主备服务器组列表。 |
| MasterSlaveServerGroup |  |  |  |
| MasterSlaveServerGroupI d | String | rsp-0bfuc**** | 主备服务器组ID。 |
| MasterSlaveServerGroupN ame | String | Group3 | 主备服务器组的名称。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例负载均衡

```
http(s)://[Endpoint]/?Action=DescribeMasterSlaveServerGroups &LoadBalancerId=lb-bp14zi0n66zpg6o**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeMasterSlaveServerGroupsResponse> <RequestId>2631BB5E-B576-4925-BDED-07A66D23E5DE</RequestId> <MasterSlaveServerGroups> <MasterSlaveServerGroup> <MasterSlaveServerGroupId>rsp-bp1ro3mw******</MasterSlaveServerGroupId> <MasterSlaveServerGroupName>test</MasterSlaveServerGroupName> </MasterSlaveServerGroup> </MasterSlaveServerGroups> </DescribeMasterSlaveServerGroupsResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "265989FE-136B-4D6A-B549-FD40E7", "MasterSlaveServerGroups": { "MasterSlaveServerGroup": [ { "MasterSlaveServerGroupId": "rsp-bp1nly******", "MasterSlaveServerGroupName": "主备1", "AssociatedObjects": { "Listeners": { "Listener": [ ] } } } ] } } |  |

#### 7.11.4. DescribeMasterSlaveServerGroupAttribute

调用DescribeMasterSlaveServerGroupAttribute查询指定主备服务器组的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMasterSlaveServerG roupAttribute | 要执行的操作。 取值：DescribeMasterSlaveServerGroupAttribute。 |
| MasterSlaveServerGroupId | String | 是 | rsp-cige6j**** | 主备服务器组ID。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MasterSlaveServerGroupI d | String | rsp-cige6**** | 主备服务器组ID。 |
| MasterSlaveServerGroupN ame | String | Group1 | 主备服务器组的名称。 |
| MasterSlaveBackendServe rs | Array of MasterSlaveBackendServe r |  | 主备服务器组列表。 |
| MasterSlaveBackendServe r |  |  |  |
| ServerId | String | vm-hrf**** | ECS实例ID或者ENI的实例ID。 |
| Port | Integer | 90 | 后端服务器使用的端口。 |
| Weight | Integer | 100 | 后端服务器的权重。 |
| ServerType | String | Slave | 服务器类型，取值：Master（默认值）或Slave。 |

负载均衡

| Description | String | 主备服务器组描述。 | 主备服务器组描述。 |
|---|---|---|---|
| Type | String | ecs | 后端服务器类型，取值： ecs：ECS实例（默认）。 eni：弹性网卡实例。 |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeMasterSlaveServerGroupAttribute &MasterSlaveServerGroupId=rsp-cige6j**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeMasterSlaveServerGroupAttributeResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <MasterSlaveServerGroupId>rsp-cige6******</MasterSlaveServerGroupId> <MasterSlaveBackendServers> <MasterSlaveBackendServers> <ServerId>vm-sshssh****</ServerId> <Port>80</Port> <Weight>100</Weight> <ServerType>Master</ServerType> </MasterSlaveBackendServers> <MasterSlaveBackendServers> <ServerId>vm-ffff*****</ServerId> <Port>90</Port> <Weight>100</Weight> <ServerType>Slave</ServerType> </MasterSlaveBackendServers> </MasterSlaveBackendServers> </DescribeMasterSlaveServerGroupAttributeResponse> |  |

| JSON | 格式 |
|---|---|
| { "DescribeMasterSlaveServerGroupAttributeResponse": { "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "MasterSlaveServerGroupId": "rsp-cige6******", "MasterSlaveBackendServers": { "MasterSlaveBackendServers": [ { "ServerId": "vm-sshssh****", "Port": "80", "Weight": "100", "ServerType": "Master" }, { "ServerId": "vm-ffff*****", "Port": "90", "Weight": "100", "ServerType": "Slave" } ] } } } |  |

### 标签

#### 7.12.1. AddTags

调用该接口时，请注意： 单次绑定的标签数最多为5对。 当添加的标签与原有标签Key相同，但Value不同时，则覆盖原有的标签。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

负载均衡

| Action | String | 是 | AddTags | 要执行的操作。 取值：AddTags。 |
|---|---|---|---|---|
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08ex**** | 负载均衡实例ID。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |
| Tags | String | 是 | [{"TagKey":"Key1","TagValue ":"Value1"}, {"TagKey":"Key2","TagValue ":"Value2"}] | 需要添加的Tag列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
&LoadBalancerId=lb-bp1b6c719dfa08ex**** &RegionId=cn-qingdao-env17-d01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}]
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <AddTagsResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> </AddTagsResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710" } |  |

#### 7.12.2. DescribeTags

调用该接口时，请注意： 允许根据实例ID、Tagkey和Tagvalue等条件查询所有符合条件的标签。 指定的条件为 `and` 关系，只有满足所有指定条件的TagSet才会被返回。 如果指定了Tagkey而没有指定Tagvalue，就查询所有该Tagkey关联的标签。 不允许用户只指定Tagvalue而不指定Tagkey。 若指定了Tagkey和Tagvalue对，则精确匹配该标签。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeTags | 要执行的操作。 取值：DescribeTags。 |
| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |
| LoadBalancerId | String | 否 | lb-bp1b6c719dfa08ex**** | 负载均衡实例ID。 |
| Tags | String | 否 | [{"TagKey":"Key1","TagValue ":"Value1"}, {"TagKey":"Key2","TagValue ":"Value2"}] | 要查询的标签列表。 |
| DistinctKey | Boolean | 否 | false | 是否为DistinctKey。 取值：true或false。 |
| PageSize | Integer | 否 | 50 | 单页结果数量，接口默认50，最大100。 |
| PageNumber | Integer | 否 | 1 | 实例列表页码，起始值1，默认值1。 |

负载均衡

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TagSets | Array of TagSet |  | Tag列表。 |
| TagSet |  |  |  |
| TagKey | String | test | 标签Key。 |
| TagValue | String | api | 标签Value。 |
| InstanceCount | Integer | 10 | 该标签绑定的实例总数。 |
| PageSize | Integer | 50 | 单页结果数量，接口默认50，最大100。 |
| PageNumber | Integer | 1 | 实例列表页码，起始值1，默认值1。 |
| TotalCount | Integer | 1 | 根据过滤条件得到的实例总个数。 |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <DescribeTagsResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <TagSets> <TagSet> <TagKey>test</TagKey> <TagValue>api</TagValue> </TagSet> </TagSets> <PageSize>50</PageSize> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> </DescribeTagsResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "TagSets": { "TagSet": [ { "TagKey": "test", "TagValue": "api" } ], "PageNumber": 1, "PageSize": 50, "TotalCount": 1 } } |  |

#### 7.12.3. RemoveTags

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RemoveTags | 要执行的操作。 取值：RemoveTags。 |
| LoadBalancerId | String | 是 | lb-bp1b6c719dfa08ex**** | 负载均衡实例ID。 |

负载均衡

| RegionId | String | 是 | cn-qingdao-env17-d01 | 负载均衡实例的地域ID。 |
|---|---|---|---|---|
| Tags | String | 是 | [{"TagKey":"Key1","TagValue ":"Value1"}, {"TagKey":"Key2","TagValue ":"Value2"}] | 需要解绑的Tag列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | 请求ID。 |

**示例**

请求示例

```
&LoadBalancerId=lb-bp1b6c719dfa08ex**** &RegionId=cn-qingdao-env17-d01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}]
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <RemoveTagsResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> </RemoveTagsResponse> |  |

| JSON | 格式 |
|---|---|
| { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710" } |  |

#### 7.12.4. UntagResources

解除指定资源的标签。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | UntagResources | 系统规定参数。取值：UntagResources |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-east-hangzhou-01 | 传统型负载均衡实例的地域ID。 |
| ResourceType | String | Query | 是 | instance | 资源类型定义，取值： instance ：负载均衡实例。 certificate ：证书。 acl ：访问控制。 |
| ResourceId | RepeatList | Query | 是 | lb-bp16qjewdsunr41m1**** | 需要修改资源组的目标资源的id。 |
| TagKey | RepeatList | Query | 否 | TestKey | 资源的标签值。N的取值范围：1 ~20 。 最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 如果不指定TagKey ，这个实例的所有标签将被删除。 |
| All | Boolean | Query | 否 | false | 是否全部删除，只针对TagKey.N 为空时有效。 取值：true 或false 。 |

| aliyun | acs: |
|---|---|
| http:// |  |

**返回数据**

负载均衡

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
&RegionId=cn-east-hangzhou-01 &ResourceType=instance &ResourceId=lb-bp16qjewdsunr41m1****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | TagTypeNotSame | TagTypeNotSame | The category of tags in the same request must be the same. |
| 400 | ResourceNotExist | ResourceNotExist | %s. |
| 400 | DeniedForNoneTagCreator | DeniedForNoneTagCreator | %s. |
| 400 | DeniedForScopeNotEqual | DeniedForScopeNotEqual | %s. |
| 400 | InvalidParam.ResourceType | InvalidParam.ResourceType | The specified ResourceType is invalid. |
| 400 | InvalidParam.TagKey | InvalidParam.TagKey | The specified TagKey is invalid. |
| 400 | InvalidParam.TagValue | InvalidParam.TagValue | The specified TagValue is invalid. |
| 400 | InvalidParam.Category | InvalidParam.TagKeyOrValue | The specified TagKey or TagValue is invalid. |
| 400 | InvalidParam.TagOwnerUid | InvalidParam.TagOwnerUid | The specified TagOwnerUid is invalid. |
| 400 | InvalidParam.TagOwnerBid | InvalidParam.TagOwnerBid | The specified TagOwnerBid is invalid. |
| 400 | MissingParam.TagOwnerUid | MissingParam.TagOwnerUid | The parameter TagOwnerUid is required. |
| 400 | MissingParam.TagOwnerBid | MissingParam.TagOwnerBid | The parameter TagOwnerBid is required. |
| 400 | RegionNotExist | InvalidParameter.RegionId | The specified RegionId does not exist. |
| 400 | MissingParam.ResourceId | MissingParam.ResourceId | The parameter ResourceId is required. |
| 400 | DeniedForOperateCustomTag | DeniedForOperateCustomTag | %s. |
| 400 | Duplicate.TagKey | Duplicate.TagKey | The param TagKey has duplicate value. |
| 400 | SizeLimitExceeded.ResourceId | SizeLimitExceeded.ResourceId | The maximum size of ResourceId is exceeded. |
| 400 | SizeLimitExceeded.TagKey | SizeLimitExceeded.TagKey | The maximum size of TagKey is exceeded. |

#### 7.12.5. TagResources

给指定资源打标签。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | TagResources | 系统规定参数。取值：TagResources |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-east-hangzhou-01 | 传统型负载均衡实例的地域ID。 |

| 负载均衡 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceType | String | Query | 是 | instance | 资源类型定义，取值： instance ：负载均衡实例。 certificate ：证书。 acl ：访问控制。 |
| ResourceId | RepeatList | Query | 是 | lb-bp16qjewdsunr41m1**** | 需要修改资源组的目标资源的id。 |
| Tag | RepeatList | Query | 是 | UploadCACertificate | 监听的标签集合。 |
| -Key | String |  | 否 | TestKey | 资源的标签键。N的取值范围：1~20 。一旦输入该值，则不允许为空字符串。 最多支持64个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| -Value | String |  | 否 | TestValue | 资源的标签值。N的取值范围：1~20 。一旦输入该值，可以为空字符串。 最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

| aliyun | acs: |
|---|---|
| http:// |  |

| aliyun |  |
|---|---|
|  | https:// |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
&RegionId=cn-east-hangzhou-01 &ResourceType=instance &ResourceId=lb-bp16qjewdsunr41m1****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | TagTypeNotSame | TagTypeNotSame | The category of tags in the same request must be the same. |
| 400 | ResourceNotExist | ResourceNotExist | %s. |
| 400 | DeniedForNoneTagCreator | DeniedForNoneTagCreator | %s. |
| 400 | DeniedForScopeNotEqual | DeniedForScopeNotEqual | %s. |
| 400 | QuotaLimitExceeds | QuotaLimitExceeds | %s. |
| 400 | InvalidParam.Scope | InvalidParam.Scope | The specified Scope is invalid. |
| 400 | InvalidParam.ResourceType | InvalidParam.ResourceType | The specified ResourceType is invalid. |
| 400 | InvalidParam.TagKey | InvalidParam.TagKey | The specified TagKey is invalid. |
| 400 | InvalidParam.TagValue | InvalidParam.TagValue | The specified TagValue is invalid. |
| 400 | InvalidParam.Category | InvalidParam.TagKeyOrValue | The specified TagKey or TagValue is invalid. |
| 400 | InvalidParam.TagOwnerUid | InvalidParam.TagOwnerUid | The specified TagOwnerUid is invalid. |
| 400 | InvalidParam.TagOwnerBid | InvalidParam.TagOwnerBid | The specified TagOwnerBid is invalid. |
| 400 | MissingParam.TagKey | MissingParam.TagKey | The parameter TagKey is required. |
| 400 | MissingParam.Scope | MissingParam.Scope | The parameter Scope is required. |

| 开发指南·API参 | 考 |  | 负载均衡 |
|---|---|---|---|

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParam.TagOwnerUid | MissingParam.TagOwnerUid | The parameter TagOwnerUid is required. |
| 400 | MissingParam.TagOwnerBid | MissingParam.TagOwnerBid | The parameter TagOwnerBid is required. |
| 400 | RegionNotExist | InvalidParameter.RegionId | The specified RegionId does not exist. |
| 400 | DeniedForOperateCustomTag | DeniedForOperateCustomTag | %s. |
| 400 | MissingParam.ResourceId | MissingParam.ResourceId | The parameter ResourceId is required. |
| 400 | Duplicate.TagKey | Duplicate.TagKey | The param TagKey has duplicate value. |
| 400 | SizeLimitExceeded.ResourceId | SizeLimitExceeded.ResourceId | The maximum size of ResourceId is exceeded. |
| 400 | SizeLimitExceeded.Tag | SizeLimitExceeded.Tag | The maximum size of Tag is exceeded. |

#### 7.12.6. ListTagResources

展示指定资源的标签列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTagResources | 系统规定参数。取值：ListTagResources |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| OwnerAccount | String | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| RegionId | String | Query | 是 | cn-east-hangzhou-01 | 传统型负载均衡实例的地域ID。 |
| ResourceType | String | Query | 是 | instance | 资源类型定义，取值： instance ：负载均衡实例。 certificate ：证书。 acl ：访问控制。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| ResourceId | RepeatList | Query | 否 | lb-bp16qjewdsunr41m1**** | 需要修改资源组的目标资源的id。 |
| Tag | RepeatList | Query | 否 | UploadCACertificate | 监听的标签集合。 |
| -Key | String |  | 否 | TestKey | 资源的标签键。N的取值范围：1~20 。一旦输入该值，则不允许为空字符串。 最多支持64个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| -Value | String |  | 否 | TestValue | 资源的标签值。N的取值范围：1~20 。一旦输入该值，可以为空字符串。 最多支持128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

| aliyun | acs: |
|---|---|
| http:// |  |

| aliyun |  |
|---|---|
|  | https:// |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TagResources | Array | resource123 | 由资源及其标签组成的集合，包含了资源ID、资源类型和标签键值等信息。 |
| -TagValue | String | api | 监听的标签值。N的取值范围：1 ~20 。一旦传入该值，可以为空字符串。最多支持128个字符，不能以 acs: 开头，不能包含 http:// 或者 https:// 。 |
| -ResourceType | String | instance | 资源类型。 |

| 负载均衡 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ResourceId | String | lb-bp16qjewdsunr4**** | 资源ID。 |
| -TagKey | String | TestKey | 实例的标签键。N的取值范围：1 ~20 。一旦输入该值，则不允许为空字符串。 最多支持64个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | 请求的ID。 |

**示例**

请求示例

```
&RegionId=cn-east-hangzhou-01 &ResourceType=instance
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984", "TagResources":[ { "ResourceId":"lb-bp16qjewdsunr4****", "TagKey":"TestKey", "ResourceType":"instance", "TagValue":"api" } ] } |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | TagTypeNotSame | TagTypeNotSame | The category of tags in the same request must be the same. |
| 400 | ResourceNotExist | ResourceNotExist | %s. |
| 400 | QueryTokenNotExist | QueryTokenNotExist | The specified NextToken does not exist. |
| 400 | QueryTokenInvalid | InvalidParam.NextToken | The specified NextToken is invalid. |
| 400 | InvalidParam.Scope | InvalidParam.Scope | The specified Scope is invalid. |
| 400 | InvalidParam.ResourceType | InvalidParam.ResourceType | The specified ResourceType is invalid. |
| 400 | InvalidParam.TagKey | InvalidParam.TagKey | The specified TagKey is invalid. |
| 400 | InvalidParam.TagValue | InvalidParam.TagValue | The specified TagValue is invalid. |
| 400 | InvalidParam.Category | InvalidParam.TagKeyOrValue | The specified TagKey or TagValue is invalid. |
| 400 | InvalidParam.TagOwnerUid | InvalidParam.TagOwnerUid | The specified TagOwnerUid is invalid. |
| 400 | InvalidParam.TagOwnerBid | InvalidParam.TagOwnerBid | The specified TagOwnerBid is invalid. |
| 400 | MissingParam.Scope | MissingParam.Scope | The parameter Scope is required. |
| 400 | MissingParam.TagOwnerUid | MissingParam.TagOwnerUid | The parameter TagOwnerUid is required. |
| 400 | MissingParam.TagOwnerBid | MissingParam.TagOwnerBid | The parameter TagOwnerBid is required. |
| 400 | RegionNotExist | InvalidParameter.RegionId | The specified RegionId does not exist. |
| 400 | MissingParam.TagOrResourceId | MissingParam.TagOrResourceId | The parameter Tag or ResourceId is required at least one. |
| 400 | SizeLimitExceeded.ResourceId | SizeLimitExceeded.ResourceId | The maximum size of ResourceId is exceeded. |
| 400 | SizeLimitExceeded.Tag | SizeLimitExceeded.Tag | The maximum size of Tag is exceeded. |

负载均衡

### 错误码列表

|  |  |  |  | 错误码 |  |  |  |  |  |  |  |  |  | 错误信息 |  |  | HTTP状态码 | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | CertificateAndPrivateKeyIsRefered |  |  |  |  |  |  |  |  |  |  | Certificate and PrivateKey |  | 400 | 证书已经被使用。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | Is Refered. |  |  |  |  |  |
|  |  |  |  | CertificateNotMatchPrivateKey |  |  |  |  |  |  |  |  |  | Certificate and key does |  |  | 400 | 证书和私钥不匹配。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | not match. |  |  |  |  |  |
|  |  |  |  | CheckedListenerNotFound |  |  |  |  |  |  |  |  |  | No health-checked Listener |  |  |  |  |  |
|  |  |  |  |  | Checked |  | ListenerNotFound |  |  |  |  |  |  | to the specified port of the |  |  | 404 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | Load |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | Balancer. |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | User not authorized to |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | operate on the specified |  |  |  |  |  |
|  |  |  |  |  | Forbbiden.SubUser |  |  |  |  |  |  |  |  | resource as your |  |  | 403 | 没有操作该资源的权 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | account is |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | created by another user. |  |  |  |  |  |
|  |  |  |  | Forbidden |  |  |  |  |  |  |  |  |  | User not authorized to |  |  |  |  |  |
|  |  |  |  |  | Forbidden |  |  |  |  |  |  |  |  | operate on the specified |  |  | 403 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | resource. |  |  |  |  |  |
|  |  |  |  | IncorrectListenerAccessControlSta |  |  |  |  |  |  |  |  |  | Current listener access |  |  |  |  |  |
|  |  |  |  |  | IncorrectL |  |  | istenerAccessControlSta |  |  |  |  |  | control s |  | tatus does not | 500 |  |  |
|  |  |  |  | tusStatus |  |  |  |  |  |  |  |  |  | support this |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | operation. |  |  |  |  |  |
|  |  |  |  | InternalError |  |  |  |  |  |  |  |  |  | The request processing has |  |  |  |  |  |
|  |  |  |  |  | Interna |  | lError |  |  |  |  |  |  | failed due to backend |  |  | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | service |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | exception. |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | The request processing has |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | failed due to some unknown |  |  |  |  |  |
|  |  |  |  |  | InternalInvokeError |  |  |  |  |  |  |  |  | error, exception |  |  | 500 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | or |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | failure. |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | Specified LoadBalancer |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | instance's addresstype is |  |  |  |  |  |
|  |  |  |  |  | InvalidBackendServers.Inconsisten |  |  |  |  |  |  |  |  |  | private, so it is |  | 400 | ECS SLB |  |
|  |  |  |  | t |  |  |  |  |  |  |  |  |  | forbidden |  |  |  | 后端的网络 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | to add ecs vpc |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | backendservers for now. |  |  |  |  |  |
|  |  |  |  | InvalidBackendServers.Inconsisten |  |  |  |  |  |  |  |  |  | All BackendServers on one |  |  |  |  |  |
|  |  |  |  |  | Invalid |  | BackendServers.Inconsisten |  |  |  |  |  |  |  | Specified LoadBalancer have |  |  | 负载均衡实例的后端服务器中不可以 |  |
|  |  |  |  | t |  |  |  |  |  |  |  |  |  | to be in the same vpc or all |  |  | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | classic |  |  |  |  |  |
|  |  |  |  | InvalidIdentity |  |  |  |  |  |  |  |  |  | The request identity was |  |  | 400 | 没有操作的权限。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | not allowed operated. |  |  |  |  |  |
|  |  |  |  | InvalidLoadBalancerId.NotFound |  |  |  |  |  |  |  |  |  | LoadBalancerId does not |  |  | 4 | 负载均衡实例不存在。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | exist. |  |  |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  |  | The specified parameter |  |  |  |  |  |
|  |  |  |  |  | InvalidPar |  |  | ameter |  |  |  |  |  | ServerCertificate format is |  |  | 404 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | error. |  |  |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  |  | The specified parameter |  |  |  |  |  |
|  |  |  |  |  | InvalidPar |  |  | ameter |  |  |  |  |  | ServerCertificateId is |  |  | 404 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | empty. |  |  |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  |  | The specified parameter |  |  |  |  |  |
|  |  |  |  |  | InvalidPar |  |  | ameter |  |  |  |  |  | ServerCertificateId is not |  |  | 404 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | support. |  |  |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  |  | The specified parameter |  |  |  |  |  |
|  |  |  |  |  | InvalidPar |  |  | ameter |  |  |  |  |  | ServerCertificate or Key is |  |  | 404 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | empty. |  |  |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  |  | The specified parameter key |  |  | 404 | 指定的私钥格式错误。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | format is error. |  |  |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  |  | Specified region does not |  |  | 404 | 指定的地域不支持。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | supported. |  |  |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  |  | Port is not Integer. |  |  | 400 | 指定端口号范围应为1-65535。 |  |

负载均衡

|  |  |  |  | InvalidParameter |  |  |  | The specified port is not | 400 | 指定端口号范围应为1-65535。 |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified bandwidth is | 400 | 指定的带宽值不合法。 |
|  |  |  |  |  |  |  |  | not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | Specified parameter Check | 400 | 参数不合法。 |
|  |  |  |  |  |  |  |  | is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter |  |  |
|  |  |  |  |  | InvalidPa | rameter |  | HealthCheckHttpCode is not | 400 |  |
|  |  |  |  |  |  |  |  | valid. |  |  |
|  |  |  |  |  |  |  |  | The specified parameter |  |  |
|  |  |  |  |  |  |  |  | bandwidth is not valid, out |  |  |
|  |  |  |  |  | InvalidParameter |  |  | of the instance | 400 |  |
|  |  |  |  |  |  |  |  | total |  |  |
|  |  |  |  |  |  |  |  | bandwidth. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 指定的Bandwidth值不合法。 |
|  |  |  |  |  |  |  |  | bandwidth is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 健康检查参数不合法。 |
|  |  |  |  |  |  |  |  | HealthCheck is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 参数SourceItem的值不合法。 |
|  |  |  |  |  |  |  |  | SourceItem is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified protocol is | 400 | 指定的协议类型不合法。 |
|  |  |  |  |  |  |  |  | not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | RS Pool is empty. | 400 | 没有可用的后端服务器。 |
|  |  |  |  | InvalidParameter |  |  |  | RS Pool doesn't exist. | 400 | 没有可用的后端服务器。 |
|  |  |  |  | InvalidParameter |  |  |  | Illegal user ID. | 400 | 账号不合法。 |
|  |  |  |  | InvalidParameter |  |  |  | User ID is null | 400 | 账号ID不能为空。 |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 负载均衡实例类型不合法。 |
|  |  |  |  |  |  |  |  | lb_type is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 参数Mode的值不合法。 |
|  |  |  |  |  |  |  |  | mode is not valid.. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter |  |  |
|  |  |  |  |  | InvalidPa | rameter |  | AccessControlStatus is not | 400 |  |
|  |  |  |  |  |  |  |  | valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 参数SourceItem的值不合法。 |
|  |  |  |  |  |  |  |  | SourceItems is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter |  | 指定的BackendServers的值不合法。 |
|  |  |  |  |  | InvalidPa | rameter |  | BackendServers is not | 404 |  |
|  |  |  |  |  |  |  |  | valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | Specified parameter is not | 400 | 指定的参数不合法。 |
|  |  |  |  |  |  |  |  | valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 指定的Domain的值不合法。 |
|  |  |  |  |  |  |  |  | Domain is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter URI | 400 | 指定的URI的值不合法。 |
|  |  |  |  |  |  |  |  | is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 指定的Scheduler的值不合法。 |
|  |  |  |  |  |  |  |  | Scheduler is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter |  | 指定的ListenerStatus的值不合法。 |
|  |  |  |  |  | InvalidPa | rameter |  | ListenerStatus is not | 400 |  |
|  |  |  |  |  |  |  |  | valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter |  |  |
|  |  |  |  |  | InvalidPa | rameter |  | PersistenceTimeout is not | 400 |  |
|  |  |  |  |  |  |  |  | valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 指定的ConnectPort的值不合法。 |
|  |  |  |  |  |  |  |  | ConnectPort is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter | 400 | 指定的ConnectTimeout的值不合法。 |
|  |  |  |  |  |  |  |  | ConnectTimeou is not valid. |  |  |
|  |  |  |  | InvalidParameter |  |  |  | The specified parameter |  |  |
|  |  |  |  |  | InvalidPa | rameter |  | StickySessionType is not | 400 |  |
|  |  |  |  |  |  |  |  | valid. |  |  |

负载均衡

|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  | The specified parameter |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | InvalidPa |  | rameter |  |  |  |  | HealthyThreshold is not | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | valid. |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  | The specified parameter |  |  |  |
|  |  |  |  |  | InvalidPa |  | rameter |  |  |  |  | UnhealthyThreshold is not | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | valid. |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  | The specified parameter | 400 | 指定的Interval的值不合法。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | Interval is not valid. |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  | The specified parameter | 400 | 指定的XForwardedFor的值不合法。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | XForwardedFor is not valid. |  |  |  |
|  |  |  |  | InvalidParameter |  |  |  |  |  |  |  | The specified parameter |  | 指定的IsPublicAddress的值不合法。 |  |
|  |  |  |  |  | InvalidPa |  | rameter |  |  |  |  | IsPublicAddress is not | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | valid. |  |  |  |
|  |  |  |  | InvalidRegionId.NotFound |  |  |  |  |  |  |  | Specified region does not exist. | 404 | 指定的地域不存在。 |  |
|  |  |  |  | InvalidServerId.Malformed |  |  |  |  |  |  |  | A specified server ID is |  |  |  |
|  |  |  |  |  | InvalidSe |  | rverId.Malformed |  |  |  |  | not valid, flush control ip | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | chain |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | fail. |  |  |  |
|  |  |  |  | InvalidServerId.NotFound |  |  |  |  |  |  |  | The specified server is not | 400 | 指定的后端服务器不存在。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | found. |  |  |  |
|  |  |  |  | InvalidWeight.Malformed |  |  |  |  |  |  |  | A specified weight is not | 400 | 指定的weight的值不合法。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | valid. |  |  |  |
|  |  |  |  | IpNotAvailable |  |  |  |  |  |  |  | The specified parameter | 400 | 指定的Address的值不合法。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | Address is not valid. |  |  |  |
|  |  |  |  | ListenerAlreadyExists |  |  |  |  |  |  |  | There is already a listener |  |  |  |
|  |  |  |  |  | Listene | rAlreadyExists |  |  |  |  |  | bound to the port on the | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | specified load |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | balancer. |  |  |  |
|  |  |  |  | ListenerNotFound |  |  |  |  |  |  |  | No Listener to the |  |  |  |
|  |  |  |  |  | ListenerNotFou |  |  | nd |  |  |  | specified port of the Load | 404 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | Balancer. |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | The input parameter Cookie |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | that is mandatory for |  |  |  |
|  |  |  |  |  | MissingParameter |  |  |  |  |  |  | processing this | 400 | 缺 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | request is |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | not supplied. |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | The input parameter |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | BackendServerPort that is |  |  |  |
|  |  |  |  |  | MissingParameter |  |  |  |  |  |  | mandatory for processing | 400 | 缺少BackendServe |  |
|  |  |  |  |  |  |  |  |  |  |  |  | this |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | request is not supplied. |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | The input parameter |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | LoadBalancerId that is |  |  |  |
|  |  |  |  |  | MissingParameter |  |  |  |  |  |  | mandatory for processing | 400 | 缺少LoadBalancerI |  |
|  |  |  |  |  |  |  |  |  |  |  |  | this |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | request is not supplied. |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | The input parameter |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | RegionId that is mandatory |  |  |  |
|  |  |  |  |  | MissingParameter |  |  |  |  |  |  | for processing this | 400 | 缺少Reg |  |
|  |  |  |  |  |  |  |  |  |  |  |  | request is |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | not supplied. |  |  |  |
|  |  |  |  | MissingParameter |  |  |  |  |  |  |  | The combination of some |  | 缺少必要参数。 |  |
|  |  |  |  |  | MissingPa |  | rameter |  |  |  |  | parameters violates the | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | spec. |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | The input parameter |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | OwnerId,OwnerAccount that is |  |  |  |
|  |  |  |  |  | MissingParameter |  |  |  |  |  |  | mandatory for | 403 | OwnerAccount |  |
|  |  |  |  |  |  |  |  |  |  |  |  | processing |  | 缺 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | this request is not |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | supplied. |  |  |  |
|  |  |  |  | PrivateKeyEncryption |  |  |  |  |  |  |  | Key has Encrypted . | 400 | 私钥已加密。 |  |
|  |  |  |  | ProcessingSameRequest |  |  |  |  |  |  |  | The same request is being |  | 相同的请求正在处理，请稍后重试。 |  |
|  |  |  |  |  | Process | ingSameRequest |  |  |  |  |  | processed. Please try | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | later. |  |  |  |

负载均衡

|  |  |  |  |  |  | ServerCertificateId.NotFound |  |  |  |  |  |  |  |  | Specified |  |  | 指定的证书不存在。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | ServerCertificateId.No |  |  |  |  | tFound |  |  | ServerCertificateId does not |  | 404 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | exist. |  |  |  |  |
|  |  |  |  |  |  | ServiceUnavailable |  |  |  |  |  |  |  |  | The request has failed due |  |  |  |  |
|  |  |  |  |  |  |  | Servic | eUnavailable |  |  |  |  |  |  | to a temporary failure of |  | 503 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | the |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | server. |  |  |  |  |
|  |  |  |  |  |  | ServiceUnavailable |  |  |  |  |  |  |  |  | The specified loadbalancer |  | 503 | 实例名称已存在。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | name has been used. |  |  |  |  |
|  |  |  |  |  |  | TcpNotSupportForHybridLb |  |  |  |  |  |  |  |  | Hybrid type loadbalancer |  |  |  |  |
|  |  |  |  |  |  |  | TcpNotSup |  | portForHybridLb |  |  |  |  |  | doesn't support TCP type |  | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | listener. |  |  |  |  |
|  |  |  |  |  |  | TooManyBackendServers |  |  |  |  |  |  |  |  | The total number of input |  |  |  |  |
|  |  |  |  |  |  |  | TooMan | yBackendServers |  |  |  |  |  |  | real servers exceeds max |  | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | supported number: |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 20. |  |  |  |  |
|  |  |  |  |  |  | TooManyBackendServers |  |  |  |  |  |  |  |  | The backend server |  | 400 | 后端服务器数量超过限额。 |  |
|  |  |  |  |  |  |  | TooManyBackend |  |  | Servers |  |  |  |  | parameter has too many |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | entries. |  |  |  |  |
|  |  |  |  |  |  | UnsupportedOperation |  |  |  |  |  |  |  |  | The Loadbalancer doesn't |  | 400 | 负载均衡实例类型不支持该操作。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | support this function. |  |  |  |  |
|  |  |  |  |  |  | UnsupportedOperation |  |  |  |  |  |  |  |  | The specified action is not |  | 400 | 指定的操作不支持。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | supported. |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | The specified port has been |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | assigned one type of |  |  |  |  |
|  |  |  |  |  |  |  | UnsupportedOperationonfixedprotoc |  |  |  |  |  |  |  | protoc | al, and this | 400 |  |  |
|  |  |  |  |  |  | alport |  |  |  |  |  |  |  |  | protocal |  |  | 指定 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | doesn't support this |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | operation. |  |  |  |  |
|  |  |  |  |  |  | UnsupportedParameter |  |  |  |  |  |  |  |  | The input parameter is not |  | 400 | 输入参数不支持。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | unsupported. |  |  |  |  |
|  |  |  |  |  |  | VipNotMatchRspool |  |  |  |  |  |  |  |  | The vip protocol is not |  | 400 | 监听的协议类型和后端服务器的应用协议不匹配。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | match with Rspool. |  |  |  |  |
|  |  |  |  |  |  | VipTooManyListeners |  |  |  |  |  |  |  |  | The total number of input |  |  |  |  |
|  |  |  |  |  |  |  | VipToo | ManyListeners |  |  |  |  |  |  | listeners exceeds max |  | 400 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | supported number: |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 50. |  |  |  |  |
|  |  |  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  | The specified resource does |  | 400 | 指定的资源不存在。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | not exist. |  |  |  |  |
|  |  |  |  |  |  | ServiceUnavailable |  |  |  |  |  |  |  |  | The specified loadbalancer |  |  |  |  |
|  |  |  |  |  |  |  | Servic | eUnavailable |  |  |  |  |  |  | is configuring, please retry |  | 503 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | later. |  |  |  |  |
|  |  |  |  |  |  | ServiceUnavailable |  |  |  |  |  |  |  |  | Obtain Ip Fail, please make |  |  |  |  |
|  |  |  |  |  |  |  | Servic | eUnavailable |  |  |  |  |  |  | sure the ECS exists and the |  | 503 | IP |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | status is |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | running. |  |  |  |  |
|  |  |  |  |  |  | ServiceUnavailable |  |  |  |  |  |  |  |  | The specified region not |  | 503 | 指定的地域不支持VPC。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | support VPC. |  |  |  |  |
|  |  |  |  |  |  | InvalidParameter |  |  |  |  |  |  |  |  | The specified vpc cloud |  | 400 | 指定的VPC已经删除。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | instance has deleted. |  |  |  |  |

负载均衡

## 附录

### STS概要

#### 8.1.1. 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

**使用RAM用户扮演角色时获取STS Token**

有权限的RAM用户可以使用其访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用STS Token访问阿里云资源。

**产品优势**

使用STS Token，减少长期访问密钥（Accesskey）泄露的风险。 STS Token具有时效性，可以自定义有效期，到期后将自动失效，无需定期轮换。 可以为STS Token绑定自定义权限策略，提供更加灵活和精细的云资源授权。

#### 8.1.2. AssumeRole

RAM用户调用AssumeRole接口获取一个扮演RAM角色的临时身份凭证（STS Token）。该接口中RAM用户扮演的是可信实体为阿里云账号类型的RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssumeRole | 要执行的操作。取值：AssumeRole |
| RoleArn | String | 是 | acs:ram::123456789012****:r ole/adminrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM角色。 |
| RoleSessionName | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、半角句号（.）、 at（@）、短划线（-）和下划线（_）。 |
| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。 具体如下： 长度为1~1024个字符。 |

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

负载均衡操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下:

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

负载均衡

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile;
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
| 400 | InvalidParameter.RoleArn | The parameter RoleArn is wrongly formed. | 角色ARN格式错误 |
| 400 | InvalidParameter.RoleSessionName | The parameter RoleSessionName is wrongly formed. | RoleSessionName格式错误，支持输入 2~64个字符，请输入至少2个字符，允许输入英文字母、数字、半角句号（.）、 at（@）、短划线（-）和下划线（_）。 |
| 400 | InvalidParameter.DurationSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | DurationSeconds参数设置错误，过期时间最小值为900秒，最大值为MaxSessionDuration设置的时间。 |
| 400 | InvalidParameter.PolicyGrammar | The parameter Policy has not passed grammar check. | 权限策略语法错误。 |
| 400 | InvalidParameter.PolicySize | The size of Policy must be smaller than 1024 bytes. | 权限策略长度超限，最大不超过1024字符。 |

负载均衡

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | STS Token没有权限。 |
| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
