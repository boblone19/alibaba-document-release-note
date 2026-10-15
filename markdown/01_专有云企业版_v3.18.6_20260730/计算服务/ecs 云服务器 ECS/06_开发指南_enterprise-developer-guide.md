---
title: "云服务器 ECS 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 717
source_pdf: "06_开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/ecs/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云服务器 ECS 开发指南

云服务器ECS

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
云服务器ECS
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公共云更一致的体验，自企业版V3.16.0开始， 专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

云服务器ECS

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，具体操作，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
获取调用时所需要的RegionID参数，具体操作，请参见获取公共Header参数。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganiza tionList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResour ceGroup章节。

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织 ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法，请参见开发文档使用说明。 云服务器ECS
5. 获取云产品Endpoint。
关于如何获取ECS Endpoint，请参见获取云服务器ECS的Endpoint。
6. 获取云产品SDK并调用云产品API。
云服务器ECS

## 准备工作

### 登录开发者门户

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
2. 输入正确的用户名及密码。
请向运营管理员获取登录控制台的用户名和密码。

**说明**

首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。 为提高安全性，密码长度必须为10~32位，且至少包含以下两种类型： 英文大写或小写字母（A~Z、a~z） 阿拉伯数字（0~9） 特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）
3. 单击**登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：
管理员强制开启MFA后的首次登录： a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**登录**。 c. 输入6位MFA码后单击**认证**。 您已开启并绑定MFA： 输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《**Apsara Uni-manager****运营控制台用户指南》**中的**《绑定并开启虚** 拟**MFA****设备》**章节。
5. 在页面顶部的菜单栏中，选择**产品** > **应用服务** > **开发者门户**。

### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

云服务器ECS
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您描述如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，以验证某个请求发送者的身份。其中 AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式，请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。 云服务器ECS

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方式，请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方式，请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。

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

本文为您介绍如何利用STS方式，调用专有云ECS的API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用云产

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
云服务器ECS i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称，具体操作，请参 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com> ，请替换为实际的STS Endpoint，具体操作，请参见AssumeRole。 云服务器ECS

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
云服务器ECS

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>，请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。

```
public static void main(String[] args) {
```

`// "<yourRegionID>"`请替换为您实际的地域`ID`。 `// "<yourStsAccessKeyID>", "<yourStsAccessKeySecret>"`请替换为前一步获取到的`STS`三元组中`Acce`

```xml
ssKeyID、AccessKeySecret。
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("ecs.aliyuns.com");
    request.setSysProduct("ECS");
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

`//` 非必填,请替换为您实际的资源集`ID`。

```
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填,请替换为您实际的组织`ID`。

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

云服务器ECS 调用专有云API时需要提供多个Header参数。本文为您介绍这些参数的含义及其获取方式，并对调用后的一些返回值做出解释。

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
3. 在左侧导航栏中，选择**资源管理** > **地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看Region ID。

**获取组织ID**

组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。

**获取资源集ID**

资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以ECS为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品** > **弹性计算** > **云服务器****ECS**。
3. 在左侧导航栏中，单击**实例**。
4. 在实例列表中查看**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |

| 开发指南·准备工作 | 云服务器EC |
|---|---|

| 名称 | 描述 |
|---|---|
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 获取ECS的SDK包

通过POP网关调用专有云API时，需使用ECS的SDK。本文为您介绍如何获取阿里云开发工具包（SDK）。 云服务器ECS SDK封装了2014-05-26版本API，以访问密钥（AccessKey）识别调用者身份，提供自动签名等功能，方便您通过API创建和管理资源。 实现云服务器ECS功能需要您同时安装ECS SDK和阿里云核心库。以Java SDK为例，您需要下载aliyun-javasdk-core以及aliyun-java-sdk-ecs。 软件开发工具包（SDK）包括代码以及示例，您可以自行选择语言创建云应用。 目前SDK的语言支持：Java、Python、Go，您可以前往阿里云开发工具包（SDK）中进行选择。

**说明**

推荐使用 Java、Python、Go三种语言的SDK包，使用其他语言的SDK包可能发生不兼容情况。 SDK核心库推荐使用阿里云官网的SDK核心库，其内容所有云产品共用，且适用于专有云。 云服务器ECS

## Java SDK调用示例

### 快速开始

本文介绍如何获取ECS Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操获取ECS的Endpoint。具体操作，请参见获取云服务器ECS的Endpoint。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云 Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用ECS的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17及以上版本，SDK的版本为4.23.2。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Product>，请替换为您实际的产品名称。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <readTimeout>，请您根据实际情况设置读取超时时间，单位为毫秒。 <connectionTimeout>，请您根据实际情况设置连接超时时间，单位为毫秒。 <maxRequestsPerHost>，请您根据实际情况设置每个主机的最大请求数。 <maxRequests>，请您根据实际情况设置最大请求数。 <http://192.168.XX:33XX>，请替换为您实际的代理IP+端口。

```java
 import com.aliyuncs.profile.DefaultProfile;
 import com.aliyuncs.DefaultAcsClient;
 import com.aliyuncs.IAcsClient;
 import com.aliyuncs.exceptions.ClientException;
 import com.aliyuncs.exceptions.ServerException;
 import com.aliyuncs.http.HttpClientConfig;
 import com.aliyuncs.http.ProtocolType;
 import com.aliyuncs.ecs.model.v20140526.*;
 public class Main {
publicstaticvoidmain(String[]args){
```

云服务器ECS

```
     public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`。 `//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值。

```
        profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
```

`//` 设置请求配置。

```
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);// 忽略证书。
```

clientConfig.setReadTimeoutMillis(<readTimeout>);// 读取超时时间（可选）,单位为毫秒（`ms` ）。

```
        clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// 连接超时时间（可选）,
```

单位为毫秒（`ms`）。 clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// 设置每个主机的最大请求数（ 可选）。 clientConfig.setMaxRequests(<maxRequests>);// 设置最大请求数（可选）。 clientConfig.setProtocolType(ProtocolType.HTTP); // 设置请求协议,默认`HTTP`（可选）。 `/*` 设置代理(可选`),`替换为代理`IP+Port`。

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

`//` 创建`API`请求并设置参数。

```
        DescribeInstancesRequest request = new DescribeInstancesRequest();
```

`//` 业务参数。

```
        request.setPageSize(10);
        request.setPageNumber(1);
```

`//` 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用，请根据实际情况修改。

```
        request.putHeaderParameter("x-acs-organizationid", "1");
        request.putHeaderParameter("x-acs-resourcegroupid", "11");
```

`//` 发起请求并处理应答或异常。

```java
        DescribeInstancesResponse response;
        try {
            response = client.getAcsResponse(request);
            for (DescribeInstancesResponse.Instance instance:response.getInstances()) {
                System.out.println(instance.getInstanceName());
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

本文介绍如何安装及调用ECS Java SDK。 云服务器ECS 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用ECS的开发工具包，必须安装阿里云Java SDK核心库以及ECS的Java SDK。SDK核心库推荐使用4.5.17 及以上版本，Java SDK的版本为4.23.2。 以使用ECS的Java SDK为例，您需要安装阿里云Java SDK核心库和ECS Java SDK，并在pom.xml文件中添加以下依赖即可。准确的SDK版本号，请参见阿里云开发工具包（SDK）。

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

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。 目前，Java SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。 云服务器ECS

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

#### 发起调用

本文介绍如何使用ECS Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。

| 求类的命名规范为 | ${apiName}Request |  |
|---|---|---|
| DescribeInstances |  | 。 |

在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。 云服务器ECS

```
DescribeInstancesRequest();
```

`//` 业务参数

```
request.setPageSize(10); request.setPageNumber(1);
```

`//` 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用，请根据实际修改

```
request.putHeaderParameter("x-acs-organizationid", "1"); request.putHeaderParameter("x-acs-resourcegroupid", "");
```

3. 发起调用并处理应答。

```java
DescribeInstancesResponse response; try {
    response = client.getAcsResponse(request);
    for (DescribeInstancesResponse.Instance instance:response.getInstances()) {
        System.out.println(instance.instance.getInstanceName());
    }
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
}
```

正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 `response.getXXX()` 来获得应答中的字段。

```
String instanceStatus = instance.getStatus()
```

如果出现了异常，或您需要原始HTTP应答的情况下，您可以通过以使用 `doAction()` 来获取原始应答。

```
HttpResponse response = client.doAction(request);
```

#### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息，包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码： 云服务器ECS

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

当您要调用ECS的某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意 OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在ECS的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。 用 `request.setSysAction("RunInstances")` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为使用ECS的 `DescribeInstanceStatus` 接口获取实例状态列表的调用示例： 云服务器ECS

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP和端口。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret` `//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值

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
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// 非必填
```

云服务器ECS ，请替换为您实际的资源集`ID`

```
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// 必填，请
```

替换为您实际的组织`ID`

```
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// 必填，调用来源说
```

明

```
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// 非必填(企业版V3.15.0及
```

之前历史版本必填`),`请替换为您实际的地域`ID`

```
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修改、
```

删除、查询单实例详情时必填）,请替换为您实际的实例`ID`

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

云服务器ECS

## Python SDK调用示例

### 快速开始

本文介绍如何获取ECS Python SDK并开始调用。

**环境准备**

使用阿里云专有云Python SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操获取ECS的Endpoint。具体操作，请参见获取云服务器ECS的Endpoint。
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

**说明**

本文操作步骤中ECS示例代码同时适用于Python 2和Python 3。 以下示例以ECS为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
云服务器ECS

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuns.com>，请替换为您实际的产品访问地址。 <http://192.168.XX:33XX>，请替换为您实际的代理IP+端口。

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
# global config
```

`region_id = '<yourRegionID>' #` 请替换为您实际的地域`ID` `access_key = '<yourAccessKeyID>' #` 请替换为您实际的的`AccessKey ID`

```bash
access_secret = '<yourAccessKeySecret>' # 请替换为您实际的AccessKey Secret http_proxy='<http://192.168.XX:33XX>', # 请替换为您实际的http_proxy
# product config
```

`product_name = 'ECS' #` 填写产品名称 `endpoint = '<ecs.aliyuns.com>' #` 产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
# setup request
request = DescribeInstancesRequest.DescribeInstancesRequest()
```

`request.set_accept_format('json') #` 设置返回数据格式

```python
# get response
response = clt.do_action_with_exception(request) print(response)
```

### 使用手册

#### 安装Python SDK

本文介绍如何安装及调用ECS Python SDK。

**背景信息**

阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。

**说明**

使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用ECS的Python SDK，您需要安装阿里云Python SDK核心库和ECS的Python SDK。
1. 安装SDK核心库。
云服务器ECS 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

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

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。 目前，Python SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```python
from aliyunsdkcore import client clt = client.AcsClient(access_key, acces_secret, region_id)
```

#### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。 产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**说明**

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。

| 运行 | python -c "import ssl" |  |
|---|---|---|
| No module named ssl |  | 的错误信 |

若没有OpenSSL，运行以下命令安装： `pip install pyopenssl #Python2`使用此命令。 云服务器ECS 若本地环境为Python3，则运行 `pip3 install pyopenssl` 命令。

**说明**

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

#### 发起调用

本文介绍如何使用ECS Python SDK发起请求。

**操作步骤**

1. 导入ECS Python SDK。

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

```python
response = clt.do_action_with_exception(request) print(response)
```

#### 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。 云服务器ECS

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

当您要调用的ECS的某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.set_action_name('Action')` 的方式来指定API名称。 用 `request.set_action_name('RunInstances')` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为ECS的 `DescribeInstanceStatus` 接口获取实例状态列表的调用示例： 云服务器ECS

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <ecs.aliyuncs.com>，请替换为您实际的产品访问地址。 云服务器ECS

```bash
#!/usr/bin/env python
# coding=utf-8
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

# 非必填（企业版`V3.15.0`及之前历史版本必填），请替换为您实际的地域`ID`

```
request.add_header("x-acs-regionid", "<yourRegionID>")
```

# 非必填（修改、删除、查询单实例详情时必填），请替换为您实际的实例`ID`

```python
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))
```

云服务器ECS

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问ECS。本操作介绍如何获取阿里云ECS Go SDK并开始调用。

**环境准备**

使用Go SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参见获取 AccessKey。 获取ECS的Endpoint。具体操作，请参见获取云服务器ECS的Endpoint。

**安装阿里云Go SDK核心包**

阿里云Go SDK支持Go 1.10.x及更高版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**使用Go SDK**

以下代码示例展示了调用阿里云Go SDK的3个主要步骤：
1. 初始化Client实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <http://192.168.XX:33XX>，请替换为您实际的代理IP+端口。 云服务器ECS

```java
package main
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

`//` 设置代理

```
    ecsClient.SetHttpProxy("https://192.168.XX:33XX>")   // 设置Http代理
    ecsClient.GetHttpProxy()                          // 获取Http代理
    ecsClient.SetHttpsProxy("<https://192.168.XX:33XX>")   // 设置Https代理
    ecsClient.GetHttpsProxy()                           // 获取Https代理
    ecsClient.SetNoProxy("127.0.0.1,localhost")     // 设置代理白名单
    ecsClient.GetNoProxy()                          // 获取代理白名单
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

云服务器ECS

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。 目前，Go SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。 以下代码以ECS为例，展示初始化ecsClient实例。 `//` 初始化`ecsClient`实例

```
ecsClient, err := ecs.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 发起调用

本文介绍如何使用ECS Go SDK发起请求。 以下步骤以ECS为例，展示使用ECS Go SDK发起调用。
1. 导入ECS Go SDK。

```java
import "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs"
```

2. 新建一个AcsClient，该client中包含产品名的所有API。
`ecsClient,err := <ecs>.NewClientWithAccessKey( //`请替换为您实际的产品名称 `"<yourRegionID>", //` 请替换为您实际的`RegionID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>") //` 请替换为您实际的`AccessKeySecret` `ecsClient.Domain = "ecs.aliyuns.com" //`设置请求域名地址，当前为示例值，请求根据实际请求地址替换。
3. 使用 `xxx.CreateXXXRequest` 方法创建一个请求。
该方法的命名规范为 ${service}.Create${apiName}Request ，其中： ${service} 为产品名称(小写)。例如ecs。ecs替换为自己的产品名称。

```
request := ecs.CreateDescribeInstanceRequest() request.InstanceIds = ""
```

4. 发起调用并处理返回。

```
response, err := ecsClient.DescribeInstanceAttribute(request)
```

云服务器ECS

#### 错误处理

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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以ECS为例，您可以通过以下代码来判断并获取 `ServerError` 以及 `Response` 中的错误信息： 云服务器ECS

**说明**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法请参考： `"github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" //ecs`请替换为您实际的产品名称

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

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在ECS的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。 用 `request.setSysAction("RunInstances")` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为ECS的 `DescribeInstanceStatus` 接口获取实例状态列表的调用示例： 云服务器ECS

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 云服务器ECS

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

`request.Domain = "<ecs.aliyuncs.com>" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "Ecs"
    request.Version = "2014-05-26"
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

`request.Headers["x-acs-regionid"] = "<yourRegionID>" //` 非必填（企业版`V3.15.0`及之前历史版本必填），请替换为您实际的地域`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // 非必填，请替换为您实
```

际的资源集`ID`

```
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // 必填，请替换为您实际的
```

组织`ID` `// request.Headers["x-acs-instanceid"] = "<yourInstanceID>" //` 非必填（修改、删除、查看单实例详情时必填），请替换为您实际的实例`ID`

```
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

云服务器ECS

## API参考

### ECS API参考

#### 调用API

##### 概述

ECS API 接口调用是向 ECS API 的服务端地址发送 HTTP GET 请求。您需要按照接口描述在请求中加入相应请求参数。调用后系统会返回处理结果。请求及返回结果都使用UTF-8字符集编码。

##### 请求结构

**服务地址**

如何获取产品的endpoint，请参见获取云服务器ECS的Endpoint。

**请求方法**

支持HTTP GET方法发送请求，这种方式下请求参数需要包含在请求的URL中。

**通信协议**

支持通过HTTP或HTTPS通道进行请求通信。为了获得更高的安全性，推荐您使用HTTPS通道发送请求。

**请求参数**

每个请求都需要指定要执行的操作，即Action参数（例如StartInstance），以及每个操作都需要包含的公共请求参数和指定操作所特有的请求参数。

**字符编码**

请求及返回结果都使用UTF-8字符集进行编码。

##### API授权

为了确保您的账号安全，建议您使用子账号的身份凭证调用API。如果您使用RAM账号调用弹性计算API，您需要为该RAM账号创建、附加相应的授权策略。 在RAM中，可以对一个ECS资源进行以下Action的授权。 云服务器ECS DescribeInstanceMonitorData

##### 签名机制

ECS服务会对每个访问的请求进行身份验证，使用HTTP和HTTPS协议提交请求时，都需要在请求中包含签名 （Signature）信息。 ECS通过使用AccessKey ID和AccessKey Secret进行对称加密，以验证请求的发送者身份。AccessKey ID和 AccessKey Secret由阿里云官方颁发给访问者，其中AccessKey ID用于标识访问者的身份，AccessKey Secret是用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密。关于如何获取AccessKey，请您在访问ECS服务时，请按照以下方法对请求进行签名处理：
1. 使用请求参数构造规范化的请求字符串（Canonicalized Query String）。
i. 参数排序。按照参数名称的字典顺序对请求中所有的请求参数排序（包括**公共请求参数**和接口的自定义参数，但不能包括**公共请求参数**中提到的 **Signature****参数**本身）。 当使用GET方法提交请求时，这些参数就是请求URI中的参数部分（即URI中? 之后由&连

**说明**

接的部分）。 云服务器ECS ii. 参数编码。对排序之后的请求参数的名称和值分别用UTF-8字符集进行URL编码。编码的规则如下： 对于字符A-Z、a-z、0-9以及字符“-”、“_”、“.”、“~”不编码。 对于其他字符编码成“%XY”的格式，其中XY是字符对应ASCII码的16进制表示。例如英文的双引号（”） 对应的编码就是%22。 对于扩展的UTF-8字符，编码成“%XY%ZA…”的格式。 英文空格（）编码为%20，而不是加号（+）。 该编码方式和一般采用的 `application/x-www-form-urlencoded` MIME格式编码算法类似（例如Java标准库中的 java.net.URLEncoder的实现），但又存在差异。实现时，可以先用标准库的方式进行编码，然后把编码后的字符串中加号（+）替换成%20、星号（*）替换成%2A、%7E替换回波浪号（~），即可得到上述规则描述的编码字符串。这个算法可以用下面的percentEncode方法来实现：

```java
  private static final String ENCODING = "UTF-8";
  private static String percentEncode(String value) throws UnsupportedEncodingException
{
     return value != null ? URLEncoder.encode(value, ENCODING).replace("+",
"%20").replace("*", "%2A").replace("%7E", "~") : null;
 }
```

iii. 将编码后的参数名称和值用英文等号（ = ）连接。 iv. 将等号连接得到的参数组合按步骤(a)排好的顺序依次使用&符号连接，即得到规范化请求字符串。
2. 将上一步构造的规范化字符串按照下面的规则构造成待签名的字符串：

```
 StringToSign=
     HTTPMethod + “&” +
     percentEncode(“/”) + ”&” +
      percentEncode(CanonicalizedQueryString)
```

其中HTTPMethod是提交请求用的HTTP方法，例如GET。 percentEncode(“/”)是按照1.b中描述的URL编码规则对字符“/”进行编码得到的值，即“%2F”。 percentEncode(CanonicalizedQueryString)是对第1步中构造的规范化请求字符串按1.b中描述的URL 编码规则编码后得到的字符串。
3. 按照RFC2104的定义，计算待签名字符串StringToSign的HMAC值。
计算签名时使用的Key就是您持有的********************并加上一个&字符（ASCII:38），

**说明**

使用的哈希算法是SHA1。
4. 按照Base64编码规则把上面的HMAC值编码成字符串，即得到签名值（Signature）。
5. 将得到的签名值作为**Signature**参数添加到请求参数中，即完成对请求签名的过程。
得到的签名值在作为最后的请求参数值提交给ECS服务器时，要和其他参数一样，按

**说明**

照RFC3986的规则进行URL编码。 以DescribeRegions为例，假设使用的****************是testid，********************是testsecret。则签名前的请求URL为：

```
http://ecs.example.com/?TimeStamp=2016-02- 23T12:46:24Z&Format=XML&AccessKeyId=testid&Action=DescribeRegions&SignatureMethod=HMAC-SH A1&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82f****&Version=2014-05- 26&SignatureVersion=1.0
```

计算得到的待签名字符串**StringToSign**为：

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeRegions%26Format%3DXML%26SignatureMethod%3D C-SHA1%26SignatureNonce%3D3ee8c1b8-83d3-44af-a94f- 4e0ad82f****%26SignatureVersion%3D1.0%26TimeStamp%3D2016-02- 23T12%253A46%253A24Z%26Version%3D2014-05-26
```

云服务器ECS 因为********************是testsecret，所以用于计算HMAC的Key为testsecret&，计算得到的签名值是：*************************** 。 将签名作为Signature参数加入到URL请求中，最后得到的URL为：

```
http://ecs.example.com/? SignatureVersion=1.0&Action=DescribeRegions&Format=XML&SignatureNonce=3ee8c1b8-83d3-44afa94f-4e0ad82f****&Version=2014-05- 26&AccessKeyId=testid&Signature=CT9X0VtwR86fNWSnsc6v8YGO****&SignatureMethod=HMAC- SHA1&TimeStamp=2016-02-23T12%3A46%3A24Z
```

##### 返回结果

调用 API 服务后返回数据采用统一格式，返回的 HTTP 状态码为 2xx，代表调用成功；返回 4xx 或 5xx 的 HTTP 状态码代表调用失败。调用成功返回的数据格式主要有 XML 和 JSON 2种。外部系统可以在请求时传入参数来制定返回的数据格式，默认为 XML 格式。 本文档中的返回示例为了便于用户查看，做了格式化处理，实际返回结果是没有进行换行、缩进

**说明**

等处理的。

**成功结果**

XML 示例

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

<!--结果的根结点`-->` <接口名称`+Response>` <!--返回请求标签`-->`

```xml
    <RequestId>4C467B38-3910-447D-87BC-AC04916*****</RequestId>
```

<!--返回结果数据`-->` `</`接口名称`+Response>` JSON 示例

```json
{
    "RequestId": "4C467B38-3910-447D-87BC-AC04916*****",
```

`/*` 返回结果数据 `*/`

```
}
```

**错误结果**

调用接口出错后，将不会返回结果数据。调用方可根据每个接口对应的错误码以及公共错误码来定位错误原因。 当调用出错时，HTTP 请求返回一个 4xx 或 5xx 的 HTTP 状态码。返回的消息体中是具体的错误代码及错误信息。另外还包含一个全局唯一的请求 ID：RequestId 和一个您本次请求访问的站点 ID：HostId。 XML 示例

```xml
<?xml version="1.0" encoding="UTF-8"?> <Error>
   <RequestId>8906582E-6722-409A-A6C4-0E7863B*****</RequestId>
   <HostId>ecs.example.com</HostId>
   <Code>InvalidOwnerId</Code>
   <Message>The specified OwnerId is not valid.</Message>
</Error>
```

JSON 示例云服务器ECS

```json
{
    "RequestId": "8906582E-6722-409A-A6C4-0E7863B*****",
    "HostId": "ecs.example.com",
    "Code": "InvalidOwnerId",
    "Message": "The specified OwnerId is not valid."
}
```

#### RAM鉴权

当子账号通过ECS OpenAPI对主账号的ECS资源进行访问时，ECS后台向RAM进行权限检查，以确保资源拥有者的确将相关资源的相关权限授予了调用者。 每个不同的ECS API，会根据涉及到的资源以及API的语义，确定需要检查的资源的权限。各API的鉴权规则如API鉴权规则所示。 表 1. API鉴权规则

| Action | 鉴权规则 |
|---|---|
| AttachDisk | acs:ecs:$regionid:$accountid:disk/$diskid acs:ecs:$regionid:$accountid:instance/$instanceid |
| AuthorizeSecurityGroup | acs:ecs:$regionid:$accountid:securitygroup/$securitygroupid[and acs:ecs:$regionid:$accountid:securitygroup/$sourcegroupid] 说明如果指定了SourceGroupId参数，必须填入sourcegroupid。 |
| CreateDisk | acs:ecs:$regionid:$accountid:disk/*[and acs:ecs:$regionid:$accountid:snapshot/$snapshotid] 说明如果指定了SnapshotId参数，必须填入SnapshotId。 |
| CreateImage | acs:ecs:$regionid:$accountid:image/*acs:ecs:$regionid:$accountid:snapsh ot/$snapshotid |
| CreateInstance | acs:ecs:$regionid:$accountid:instance/*acs:ecs:$regionid:$accountid:securi tygroup/$securitygroupidacs:ecs:$regionid:$accountid:image/$imageid[an d acs:ecs:$regionid:$accountid:snapshot/$snapshotid] 说明如果指定了DataDisk.n.SnapshotId参数，必须填入 snapshotid。 |
| CreateSecurityGroup | acs:ecs:$regionid:$accountid:securitygroup/* |
| CreateSnapshot | acs:ecs:$regionid:$accountid:disk/$diskid acs:ecs:$regionid:$accountid:snapshot/* |
| DeleteDisk | acs:ecs:$regionid:$accountid:disk/$diskid |
| DeleteImage | acs:ecs:$regionid:$accountid:image/$imageid |
| DeleteInstance | acs:ecs:$regionid:$accountid:instance/$instanceid |
| DeleteSecurityGroup | acs:ecs:$regionid:$accountid:securitygroup/$securitygroupid |
| DeleteSnapshot | acs:ecs:$regionid:$accountid:snapshot/$snapshotid |
| DescribeAutoSnapshotPolicy | acs:ecs:*:$accountid:snapshot/* |
| DescribeDisks | acs:ecs:$regionid:$accountid:disk/* |

云服务器ECS

| DescribeImages | acs:ecs:$regionid:$accountid:image/* |
|---|---|
| DescribeInstanceMonitorDat a | acs:ecs:$regionid:$accountid:instance/$instanceid |
| DescribeInstanceStatus | acs:ecs:$regionid:$accountid:instance/* |
| DescribeInstanceTypes | acs:ecs:*:$accountid:* |
| DescribeRegions | acs:ecs:*:$accountid:* |
| DescribeSecurityGroupAttrib ute | acs:ecs:$regionid:$accountid:securitygroup/$securitygroupid |
| DescribeSecurityGroups | acs:ecs:$regionid:$accountid:securitygroup/* |
| DescribeSnapshots | acs:ecs:$regionid:$accountid:snapshot/* |
| DescribeZones | acs:ecs:*:$accountid:* |
| DetachDisk | acs:ecs:$regionid:$accountid:disk/$diskid acs:ecs:$regionid:$accountid:instance/$instanceid |
| JoinSecurityGroup | acs:ecs:$regionid:$accountid:instance/$instanceid acs:ecs:$regionid:$accountid:securitygroup/$securitygroupid |
| LeaveSecurityGroup | acs:ecs:$regionid:$accountid:instance/$instanceid acs:ecs:$regionid:$accountid:securitygroup/$securitygroupid |
| ModifyAutoSnapshotPolicy | acs:ecs:*:$accountid:snapshot/* |
| ModifyDiskAttribute | acs:ecs:$regionid:$accountid:disk/$diskid |
| ModifyInstanceAttribute | acs:ecs:$regionid:$accountid:instance/$instanceid |
| ModifyInstanceNetworkSpec | acs:ecs:$regionid:$accountid:instance/$instanceid |
| RebootInstance | acs:ecs:$regionid:$accountid:instance/$instanceid |
| ReplaceSystemDisk | acs:ecs:$regionid:$accountid:instance/$instanceid[and acs:ecs:$regionid:$accountid:image/$imageid] 说明如果是使用了自定义镜像，必须填入imageid。 |
| ReInitDisk | acs:ecs:$regionid:$accountid:disk/$diskid |
| ResetDisk | acs:ecs:$regionid:$accountid:snapshot/$snapshotid acs:ecs:$regionid:$accountid:disk/$diskid |
| RevokeSecurityGroup | acs:ecs:$regionid:$accountid:securitygroup/$securitygroupid[and acs:ecs:$regionid:$accountid:securitygroup/$sourcegroupid] 说明如果指定了SourceGroupid参数，必须填入sourcegroupid。 |
| StartInstance | acs:ecs:$regionid:$accountid:instance/$instanceid |
| StopInstance | acs:ecs:$regionid:$accountid:instance/$instanceid |
| DescribeInstances | acs:ecs:$regionid:$accountid:instance/* |
| CreateVpc | acs:ecs:$regionid:$accountid:vpc/* |

云服务器ECS

| ModifyVpcAttribute | acs:ecs:$regionid:$accountid:vpc/$vpcid |
|---|---|
| DescribeVRouters | acs:ecs:$regionid:$accountid:vrouter/* |
| CreateVSwitch | acs:ecs:$regionid:$accountid:vswitch/* |
| CreateRouteTable | acs:ecs:$regionid:$accountid:routetable/* |
| CreateRouteEntry | acs:ecs:$regionid:$accountid:routetable/$routetableid |
| AllocateEipAddress | acs:ecs:$regionid:$accountid:eip/* |
| AssociateEipAddress | acs:ecs:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |
| ReleaseEipAddress | acs:ecs:$regionid:$accountid:eip/$allocationid |
| DescribeVpcs | acs:ecs:$regionid:$accountid:vpc/* |
| DeleteVpc | acs:ecs:$regionid:$accountid:vpc/$vpcid |
| ModifyVRouterAttribute | acs:ecs:$regionid:$accountid:vrouter/$vrouterid |
| DescribeVSwitches | acs:ecs:$regionid:$accountid:vswitch/* |
| DeleteVSwitch | acs:ecs:$regionid:$accountid:vswitch/$vswitchid |
| DescribeRouteTables | acs:ecs:$regionid:$accountid:routetable/* |
| DeleteRouteEntry | acs:ecs:$regionid:$accountid:routetable/$routetableid |
| DescribeEipAddresses | acs:ecs:$regionid:$accountid:eip/* |
| UnassociateEipAddresses | acs:ecs:$regionid:$accountid:eip/$eipid acs:ecs:$regionid:$accountid:instance/$instanceid |
| ModifySecurityGroupAttribut e | acs:ecs:$regionid:$accountid:securitygroup/$securitygroupid |
| DescribeEipMonitorData | acs:ecs:$regionid:$accountid:eip/$allocationid |
| ModifyVSwitchAttribute | acs:ecs:$regionid:$accountid:vswitch/$vswitchid |
| DescribeInstanceVncUrl | acs:ecs:$regionid:$accountid:instance/$instanceid |
| ModifySnapshotAttribute | acs:ecs:$regionid:$accountid:snapshot/$snapshotid |
| ModifyInstanceVpcAttribute | acs:ecs:$regionid:$accountid:instance/$instanceid |
| ModifyEipAddressAttribute | acs:ecs:$regionid:$accountid:eip/$allocationid |
| DescribeDiskMonitorData | acs:ecs:$regionid:$accountid:disk/$diskid |

#### 公共参数

公共参数分为公共请求参数、公共Header参数和公共返回参数。

**公共请求参数**

公共请求参数是指每个接口都需要使用到的请求参数。 云服务器ECS 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回值的类型，仅支持 JSON。 |
| Version | String | 是 | API 版本号，以日期形式YYYY-MM-DD输入，取值： 2014- 05-26。 |
| AccessKeyId | String | 是 | 访问服务使用的密钥ID。 |
| AccessKeySecret | String | 是 | 访问服务使用的密钥值。 |
| RegionId | String | 是 | 访问服务所使用的地域ID。 |
| Product | String | 是 | 接口对应的产品名称。 |

| 名称 | 描述 |
|---|---|
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID。具体获取方式，请参见获取组织 ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID。具体获取方式，请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID。具体获取方式，请参见获取实例ID |

**说明**

在调用各云产品接口调用时，您需要在调用代码的请求头Header中添加**x-acs-instanceid**、**x-acs-**
**organizationid**、**x-acs-resourcegroupid**等参数的实际值，用于指定当前实例的实例ID（在创建实
例和查询实例列表的场景下，实例ID不存在），及其所属的组织和资源集。若未添加相关Header参数实际值，调用时则会默认指向root组织和root资源集。

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码RequestId。

#### 实例

云服务器ECS

##### CreateInstance

接口说明

| DescribeAvailableResource |  |  |  | 查看 |
|---|---|---|---|---|
| 实例自动进入 | 运行中 | （ | Running |  |

创建ECS实例时，您需要注意：

**实例规格**

可以通过参数 `IoOptimized` 指定是否创建I/O优化实例。

| DescribeInstanceTypes |  | 查看目标实例规 |
|---|---|---|
| 库存：调用 | DescribeAvailableResource |  |

**镜像**

镜像确定实例的系统盘配置，实例的系统盘即为指定镜像的完全克隆。 实例内存为512 MiB时，不能使用除半年渠道之外的Windows Server镜像。 实例内存为4 GiB以上时，不能使用32位操作系统的镜像。

**网络类型**

专有网络VPC类型实例必须且只能属于一个交换机。

| 指定 |  | VSwitchId |  |  |
|---|---|---|---|---|
| PrivateIpAddress |  |  |  |  |
| 定 | VSwitchId |  | 和 | PrivateIpAddress |

| VSwitchId 必须属于同一个VPC 不能单独指定 PrivateIpAddress | VSwitchId |  | 必须属于同一个VPC |  |
|---|---|---|---|---|
|  |  | PrivateIpAddress |  |  |
| PrivateIpAddress |  |  |  | 必须包含在交 |

#### 安全组

同一个安全组内可容纳的实例数量视安全组类型而定。 同一个安全组内的实例内网可以相互访问。不同安全组之间默认隔离，不可相互访问，但是可以授权访问。更多信息，请参见专有云文档中心《云服务器ECS开发指南》文档中

```
的 AuthorizeSecurityGroup 和 AuthorizeSecurityGroupEgress 章节。
```

**存储**

根据您指定的镜像，实例被分配一个相应大小的系统盘。系统盘容量必须大于或者等于 `max{20,` `ImageSize}` 。系统盘的种类请参见 `SystemDisk.Category` 参数描述。 当系统盘是普通云盘（ `cloud` ）、高效云盘（ `cloud_efficiency` ）或SSD云盘（ `cloud_ssd` ）时， 数据盘不能是本地SSD盘（ `ephemeral_ssd` ）。 I/O优化实例的系统盘只能选择高效云盘（ `cloud_efficiency` ）及SSD云盘（ `cloud_ssd` ）。 不同类型云盘的数据盘最大容量不同。更多信息，请参见 `DataDisk.N.Size` 参数描述。 一台实例最多添加16块数据盘。数据盘挂载点由系统默认顺序分配，/dev/xvdb开始到/dev/xvdz。

**自定义数据**

若实例满足使用实例自定义数据的限制，您可传入 `UserData` 信息。 `UserData` 以Base64的方式编码。因为传输API请求时，不会加密您设置的 `UserData` ，建议不要以明文方式传入机密的信息，例如密码和私钥等。如果必须传入，建议加密后，然后以Base64的方式编码后再传入，在实例内部以同样的方式反解密。

**其他**

在阿里云SDK中使用API时，部分带半角句号（.）的入参需要去掉半角句号（.）再使用。例如，使用 SystemDiskCategory表示入参SystemDisk.Category。 云服务器ECS

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| Action | String | Query | 是 | CreateInstance |  | 系统规定参数。取值： CreateInstance。 |  |  |
| RegionId | String | Query | 是 | cn-qingdao-**** |  | 实例所属的地域ID。您可以调用 DescribeRegions 查询地域ID。 |  |  |
| ImageId | String | Query | 否 | ubuntu 18 04 64 20G ali _ _ _ _ _ base 20190624.vhd _ |  | 镜像文件ID，启动实例时选择的镜像资源。 |  |  |
| InstanceTy pe | String | Query | 是 | ecs.g6.large |  | 实例的资源规格。 产品选型：请参见专有云文档中心《云服务器ECS实例规格族&实例规格简介》 文档中的实例规格或调用 DescribeInstanceT ypes 查看目标实例规格的性能数据。 查询库存：调用 DescribeAvailable Resource 查看指定地域或者可用区内的资源供给情况。 |  |  |
|  |  |  |  |  |  |  | DescribeAvailable |  |
|  |  |  |  |  |  | Resource |  |  |
| SecurityGr oupId | String | Query | 否 | sg- bp15ed6xe1yxeycg**** |  | 指定新创建实例所属于的安全组ID，同一个安全组内的实例之间可以互相访问。 |  |  |
| InstanceNa me | String | Query | 否 | 2018-12-06T103200Z |  | 实例的名称。长度为2~128 个字符，支持Unicode中 letter分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号（:）、下划线（ ）、半角句号（.）或者 _ 短划线（-）。 如果没有指定该参数，默认值为实例的InstanceId。 |  |  |

|  |  | DescribeInstanceT |  |
|---|---|---|---|
| ge | ypes |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  |  | 说明 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| InternetMa xBandwidt hIn | Intege r | Query | 否 | 50 |  |  | 网络入带宽最大值，单位为 Mbit/s。取值范围： 当出网带宽小于等于10 Mbit/s时：1~10，默认为 10。 当出网带宽大于10 Mbit/s 时： 1~ InternetMaxBandw idthOut的取值 ，默认为 InternetMaxBandwi dthOut的取值 。 |  |  |  |  |
|  |  |  |  |  |  |  |  |  | InternetMaxBandw |  |  |
|  |  |  |  |  |  |  | idthOut的取值 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | ，默认 |  |
|  |  |  |  |  |  |  | 为 |  |  |  |  |
|  |  |  |  |  |  |  | dthOut的取值 |  |  |  |  |
| InternetMa xBandwidt hOut | Intege r | Query | 否 | 5 |  |  | 网络出带宽最大值，单位为 Mbit/s。取值范围： 0~100。 默认值：0。 |  |  |  |  |
| HostName | String | Query | 否 | LocalHostName |  |  | 云服务器的主机名。 英文句号（.）和短划线 （-）不能作为首尾字符， 更不能连续使用。 Windows实例：字符长度为2~15，不支持英文句号 （.），不能全是数字。允许大小写英文字母、数字和短划线（-）。 其他类型实例（Linux 等）：字符长度为2~64， 支持多个英文句号（.）， 英文句号（.）之间为一段，每段允许大小写英文字母、数字和短划线 （-）。 |  |  |  |  |
| Password | String | Query | 否 | TestEcs123! |  |  | 实例的密码。长度为8~30个字符，必须同时包含大小写英文字母、数字和特殊符号中的三类字符。特殊符号可以是： ()`~!@#$%^&*- +=\|{} _ []:;'<>,.?/ 您需要注意： 如果传入Password参数， 建议您使用HTTPS协议发送请求，避免密码泄露。 Windows实例不能以正斜线（/）为密码首字符。 部分操作系统的实例不支持配置密码，仅支持配置密钥对。例如：Others Linux、Fedora CoreOS。 |  |  |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| PasswordIn herit | Boole an | Query | 否 | false | 是否使用镜像预设的密码。使用该参数时， Password 参数必须为空，同时您需要确保使用的镜像已经设置了密码。 |  |  |
| Deployme ntSetId | String | Query | 否 | ds-bp1brhwhoqinyjd6**** | 部署集ID。 |  |  |
| ZoneId | String | Query | 否 | cn-qingdao-env17- amtest11001-a | 实例所属的可用区ID。更多信息，请参见 DescribeZones 获取可用区列表。 如果您指定了 VSwitchId 参数，则指定的 ZoneId 参数必须和交换机所在的可用区保持一致。您也可以不指定 ZoneId 参数，系统将自动选择指定的交换机所在的可用区。 |  |  |
| ClusterId | String | Query | 否 | c-bp67acfmxazb4p**** | 实例所在的集群ID。 该参数即将被弃用，为提高兼容性，请尽量使用其他参数。 |  |  |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多信息，请参见专有云文档中心《云服务器ECS开发指南》文档中的如何保证幂等性章节。 |  |  |
|  |  |  |  |  |  | 如何保证幂等 |  |
| VlanId | String | Query | 否 | 10 | 虚拟局域网ID。 |  |  |
| InnerIpAdd ress | String | Query | 否 | 192.168.*.* | 实例的内网IP。 |  |  |
| SystemDis k.Size | Intege r | Query | 否 | 40 | 系统盘大小，单位：GiB。取值范围：20~2048。 该参数的取值必须大于或者等于max{20, ImageSize }。 默认值：max{40, ImageSize } 。 |  |  |

|  | 性 |
|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| SystemDis k.Category | String | Query | 否 | cloud ssd _ | 系统盘的云盘种类。取值范围： cloud efficiency：高效 _ 云盘。 san efficiency：共享高 _ 效云盘。 cloud ssd：SSD云盘。 _ san ssd：共享SSD盘。 _ cloud pperf：高性能云 _ 盘。 cloud sperf：普通性能云 _ 盘。 默认值：cloud efficiency。 _ 默认ECS实例不支持创建共享 SSD盘和共享高效云盘。 |  |  |
| SystemDis k.DiskNam e | String | Query | 否 | SystemDiskName | 系统盘名称。长度为 2~128 个字符，支持Unicode中 letter分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号（:）、下划线（ ）、半角句号（.）或者 _ 短划线（-）。 默认值：空。 |  |  |
| SystemDis k.Descripti on | String | Query | 否 | TestDescription | 系统盘描述。长度为2~256 个英文或中文字符，不能以 http:// 或 https:/ / 开头。 默认值：空。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| Descriptio n | String | Query | 否 | InstanceTest | 实例的描述。长度为2~256 个英文或中文字符，不能以 http:// 或 https:/ / 开头。 默认值：空。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| VSwitchId | String | Query | 否 | vsw- bp1s5fnvk4gn2tws0**** | 如果是创建VPC类型的实例， 需要指定交换机ID。您可以调用 DescribeVSwitches 查询已创建的交换机的相关信息。 如果您指定了 VSwitchId 参数，则指定的 ZoneId 参数必须和交换机所在的可用区保持一致。您也可以不指定 ZoneId 参数，系统将自动选择指定的交换机所在的可用区。 |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PrivateIpA ddress | String | Query | 否 | 172.16.236.** | 实例私有IP地址。该IP地址必须为交换机 （ VSwitchId ）网段的空闲地址。 |
| IoOptimize d | String | Query | 否 | optimized | 是否为I/O优化实例。取值范围： none：非I/O优化。 optimized：I/O优化。 |
| UseAdditio nalService | Boole an | Query | 否 | true | 是否使用阿里云提供的虚拟机系统配置（Windows： NTP、KMS；Linux：NTP、 YUM）。 |
| UserData | String | Query | 否 | ZWNobyBoZWxsbyBlY3M h | 实例自定义数据，需要以 Base64方式编码，原始数据最多为16 KB。 |
| KeyPairNa me | String | Query | 否 | KeyPairTestName | 密钥对名称。 Windows实例，忽略该参数。默认为空。即使填写了该参数，仍旧只执行 Password的内容。 Linux实例的密码登录方式会被初始化成禁止。为提高实例安全性，强烈建议您使用密钥对的连接方式。 |
| RamRoleN ame | String | Query | 否 | RAMTestName | 实例RAM角色名称。您可以调用RAM API ListRoles 查询您已创建的实例RAM角色。 |
| SecurityEn hancement Strategy | String | Query | 否 | Active | 是否开启安全加固。取值范围： Active：启用安全加固， 只对系统镜像生效。 Deactive：不启用安全加固，对所有镜像类型生效。 |
| ResourceG roupId | String | Query | 否 | rg-bp67acfmxazb4p**** | 实例所在的企业资源组ID。 |
| HpcCluster Id | String | Query | 否 | hpc-bp67acfmxazb4p**** | 实例所属的HPC集群ID。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| DryRun | Boole an | Query | 否 | false |  | 是否只预检此次请求。取值范围： true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数、请求格式、业务限制和ECS库存。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认）：发送正常请求，通过检查后直接创建实例。 |  |  |
| Dedicated HostId | String | Query | 否 | dh-bp67acfmxazb4p**** |  | 专有宿主机ID。您可以通过 DescribeDedicatedHo sts 查询专有宿主机ID列表。 |  |  |
|  |  |  |  |  |  |  | DescribeDedicatedHo |  |
|  |  |  |  |  | 67acfmxazb4p**** | sts |  |  |
| CreditSpec ification | String | Query | 否 | Standard |  | 修改突发性能实例的运行模式。取值范围： Standard：标准模式。 Unlimited：无性能约束模式。 默认值：无。 |  |  |
| DeletionPr otection | Boole an | Query | 否 | false |  | 实例释放保护属性，指定是否支持通过控制台或 API（ DeleteInstance ）释放实例。 取值范围： true：开启实例释放保护。 false（默认）：关闭实例释放保护。 该属性只能限制手动释放操作，对系统释放操作不生效。 |  |  |
| Affinity | String | Query | 否 | default |  | 专有宿主机实例是否与专有宿主机关联。取值范围： default：实例不与专有宿主机关联。 host：实例与专有宿主机关联。 默认值：default。 |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| Tenancy | String | Query | 否 | default |  | 是否在专有宿主机上创建实例。取值范围： default：在非专有宿主机上创建实例。 host：在专有宿主机上创建实例。若您不指定 DedicatedHostId ，则由阿里云自动选择专有宿主机部署实例。 默认值：default。 |  |  |
| StorageSet Id | String | Query | 否 | ss-bp1j4i2jdf3owlhe**** |  | 存储集ID。您可以调用 DescribeStorageSets 查询存储集ID。 |  |  |
| StorageSet PartitionNu mber | Intege r | Query | 否 | 2 |  | 存储集中的最大分区数量。取值范围：大于等于2。 在指定了 StorageSetId 时，该参数为必填。 |  |  |
| DataDisk | Repea tList | Query | 否 | - |  | 数据盘列表。 |  |  |
| - Descriptio n | String |  | 否 | TestDescription |  | 数据盘N的描述，参数格式为 DataDisk.N.Descript ion 。长度为2~256个英文或中文字符，不能以 http:// 或 https:/ / 开头。 |  |  |
| - SnapshotId | String |  | 否 | s-bp17441ohwka0yuh**** |  | 创建数据盘N使用的快照。参数格式为 DataDisk.N.Snapshot Id ，N的取值范围为 1~16。 指定参数 DataDisk.N.Snapsh otId 后，参数 DataDisk.N.Size 会被忽略，实际创建的云盘大小为指定的快照的大小。 不能使用早于2013年7月 15日（含）创建的快照， 请求会报错被拒绝。 |  |  |
|  |  |  |  |  |  |  | DataDisk.N.Snapsh |  |
|  |  |  |  |  | ohwka0yuh**** | otId |  |  |

|  |  | DataDisk.N.Descript |  |
|---|---|---|---|
| escription | ion |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

|  |  | DataDisk.N.Snapshot |  |
|---|---|---|---|
|  | Id |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -Size | Intege r |  | 否 | 2000 | 第N个数据盘的容量大小。参数格式为 DataDisk.N.Size ， N的取值范围为1~16，内存单位为GiB。取值范围： cloud efficiency： _ 20~32768。 san efficiency： _ 20~32768。 cloud ssd： _ 20~32768。 san ssd：20~32768。 _ cloud pperf： _ 20~32768。 cloud sperf： _ 20~32768。 该参数的取值必须大于等于参数 SnapshotId 指定的快照的大小。 当数据盘的类型选择为高效云盘（cloud efficiency）或者 _ SSD盘（cloud ssd）时，如 _ 果填写的容量超过2 TB，注意按照以下EBS集群的机器数量与推荐的云盘最大建议值 （机器数量：云盘最大值）进行填写。 6台：2 TB 12台：4 TB 15台：5 TB 24台：8 TB 云盘最大建议值的计算公式为：云盘最大大小S = N/3， 其中N为相应EBS集群的机器数量，结果向下取整。例如： 如果EBS集群的机器数量为6 台，则建议创建的云盘容量不超过2 TB。 |
| -Device | String |  | 否 | null | 数据盘的挂载点。 该参数即将停止使用，为提高代码兼容性，建议您尽量不要使用该参数。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| -DiskName | String |  | 否 | DataDiskName |  | 数据盘名称，参数格式为 DataDisk.N.DiskName 。长度为 2~128 个字符， 支持Unicode中letter分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号（:）、下划线（ ）、半角 _ 句号（.）或者短划线（-）。 默认值：空。 |  |  |
| -Category | String |  | 否 | cloud ssd _ |  | 数据盘N的云盘种类，参数格式为 DataDisk.N.Category 。取值范围： cloud efficiency：高效 _ 云盘。 san efficiency：共享高 _ 效云盘。 cloud ssd：SSD云盘。 _ san ssd：共享SSD盘。 _ cloud pperf：高性能云 _ 盘。 cloud sperf：普通性能云 _ 盘。 默认值：cloud efficiency。 _ |  |  |
| - DeleteWith Instance | Boole an |  | 否 | true |  | 数据盘是否随实例释放，参数格式为 DataDisk.N.DeleteWi thInstance 。取值范围： true：数据盘随实例释放。 false：数据盘不随实例释放。 默认值：true。 |  |  |
|  |  |  |  |  |  |  | DataDisk.N.DeleteWi |  |
|  |  |  |  |  |  | thInstance |  |  |
| -KMSKeyId | String |  | 否 | 0e478b7a-4262-4802- b8cb-00d**** |  | 云盘使用的KMS密钥ID，参数格式为 DataDisk.N.KMSKeyId 。 |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| -Encrypted | Boole an |  | 否 | false |  | 是否加密，参数格式为 DataDisk.N.Encrypte d 。取值范围： true：加密。 false：不加密。 默认值：false。 |  |  |  |
|  |  |  |  |  |  |  | DataDisk.N.Encrypte |  |  |
|  |  |  |  |  |  | d |  |  |  |
| Tag | Repea tList | Query | 否 | - |  | 标签列表。 |  |  |  |
| -key | String |  | 否 | null |  | 标签键。 为提高兼容性，建议您尽量使用 Tag.N.Key 参数。 |  |  |  |
| -Key | String |  | 否 | TestKey |  | 实例、云盘和主网卡的标签键。参数格式为 Tag.N.Key ，N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 或 https:/ / 。 |  |  |  |
|  |  |  |  |  |  |  |  | https:/ |  |
| -Value | String |  | 否 | TestValue |  | 实例、云盘和主网卡的标签值。参数格式为 Tag.N.Value ，N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128个字符，不能包含 http:// 或 https:/ / 。 |  |  |  |
|  |  |  |  |  |  |  |  | https:/ |  |
| -value | String |  | 否 | null |  | 标签值。 为提高兼容性，建议您尽量使用 Tag.N.Value 参数。 |  |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE***** | 请求ID。 |
| InstanceId | String | i- bp67acfmxazb4p*** * | 实例ID。 |

| 开发指南·API参考 |  |  | 云服务器EC |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| OrderId | String | 1234567890 | 该参数暂未支持。 |
| TradePrice | Float | 0.165 | 该参数暂未支持。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-**** &ImageId=ubuntu_18_04_64_20G_alibase_20190624.vhd &SecurityGroupId=sg-bp15ed6xe1yxeycg**** &HostName=LocalHostName &InstanceType=ecs.g6.large
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE*****",
    "InstanceId": "i-bp67acfmxazb4p****"
}
```

`XML` 格式

```xml
      <RequestId>04F0F334-1335-436C-A1D7-6C044FE*****</RequestId>
      <InstanceId>i-bp67acfmxazb4p****</InstanceId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDedicatedBlo ckStorageClusterId. CapacityNotEnough | InvalidStorageClusterId.Capacity NotEnough | The remaining capacity of the current dedicated storage cluster is less than the size of disk. |
| 400 | InvalidDedicatedBlo ckStorageClusterId. StatusNotSupport | InvalidStorageClusterId.StatusN otSupport | The current status of the dedicated storage cluster cannot create a cloud disk yet. |
| 400 | Abs.InvalidDedicate dBlockStorageCluste rId.ZoneIdEmpty | InvalidStorageClusterId.ZoneIdE mpty | The specified param ZoneId cannot be empty when StorageClusterId given. |
| 400 | InvalidDedicatedBlo ckStorageClusterId. PerformanceLevelN otMatch | InvalidStorageClusterId.Perform anceLevelNotMatch | The current dedicated storage cluster cannot create this performance level of disk. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDedicatedBlo ckStorageClusterId. CategoryNotMatch | InvalidStorageClusterId.Categor yNotMatch | The current dedicated storage cluster cannot create this category of disk. |
| 400 | Abs.InvalidDedicate dBlockStorageCluste rId.DiskSizeEmpty | InvalidStorageClusterId.DiskSize Empty | The specified param DiskSize cannot be empty when StorageClusterId given. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 02297613 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 02367840 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085207 | InvalidInternetChargeType.Value NotSupported | The specified InternetChargeType is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00119147 | InvalidParameter | The specified parameter "InternetMaxBandwidthOut" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 02367767 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | PARAMETER DISK SI _ _ ZE ILLEGAL 100179 _ _ 280 | InvalidDataDiskSize.ValueNotSu pported | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085824 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084424 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084573 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000086416 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084873 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085149 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085202 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |

|  | 开发指南·API参 | 考 |  | 云服务器EC | S |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00356432 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00356653 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357727 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357790 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357913 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357948 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357734 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00838302 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00838290 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | Abs.InvalidInstanceT ype.ValueNotSuppor ted | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | Abs.InvalidDescripti on.Malformed | InvalidDescription.Malformed | The specified parameter "Description" is not valid. |
| 400 | Abs.InvalidInternetC hargeType.ValueNot Supported | InvalidInternetChargeType.Value NotSupported | The specified InternetChargeType is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000092309 | InvalidParameter | The specified parameter "InternetMaxBandwidthOut" is not valid. |
| 400 | -251 | InvalidHostName.Malformed | The specified parameter "HostName" is not valid. |
| 400 | -217 | InvalidPassword.Malformed | The specified parameter "Password" is not valid. |
| 400 | Abs.InvalidPassword .Malformed | InvalidPassword.Malformed | The specified parameter "Password" is not valid. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidPassword .Mismatch | InvalidPasswordParam.Mismatch | The input password should be null when passwdInherit is true. |
| 400 | Abs.InvalidSystemDi skCategory.ValueNo tSupported | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter "SystemDisk.Category" is not valid. |
| 400 | PARAMETER DISK N _ _ AME IS ILLEGAL _ _ | InvalidDiskName.Malformed | The specified parameter "SystemDisk.DiskName or DataDisk.n.DiskName" is not valid. |
| 400 | PARAMETER DISK D _ _ ESC IS ILLEGAL _ _ | InvalidDiskDescription.Malforme d | The specified parameter "SystemDisk.DiskDescription" or "DataDisk.n.Description" is not valid. |
| 400 | PARAMETER DISK SI _ _ ZE ILLEGAL _ | InvalidDataDiskSize.ValueNotSu pported | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179244 | InvalidDataDiskSize.ValueNotSu pported | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. |
| 400 | Abs.InvalidDataDisk Category.ValueNotS upported | InvalidDataDiskCategory.ValueN otSupported | The specified parameter "DataDisk.n.Category" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084440 | InvalidDataDiskCategory.ValueN otSupported | The specified parameter "DataDisk.n.Category" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199823 | InvalidDataDiskCategory.ValueN otSupported | The specified parameter "DataDisk.n.Category" is not valid. |
| 400 | DISK MOUNT POINT _ _ ILLEGAL _ | InvalidDataDevice.Malformed | The specified parameter "DataDisk.n.Device" is not valid. |
| 400 | -731 | InvalidNodeControllerId.Malform ed | The specified parameter "NodeControllerId" is not valid. |
| 400 | -700 | InvalidNodeControllerId.Malform ed | The specified parameter "NodeControllerId" is not valid. |
| 400 | -405 | InvalidInnerIpAddress.Malformed | The specified parameter "InnerIpAddress" is not valid. |
| 400 | -5001 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -5003 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -5005 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -498 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -221 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -410 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -226 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -190 | OperationDenied | The specified parameter "VlanId" is not valid or vlan has not enough IP address. |
| 400 | -192 | OperationDenied | The specified parameter "VlanId" is not valid or vlan has not enough IP address. |
| 400 | -1015001 | OperationDenied | The specified parameter "VlanId" is not valid or vlan has not enough IP address. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000092281 | InvalidParameter.Conflict | The specified image does not support the specified instance type. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 707398 | InvalidParameter.Conflict | The specified image does not support the specified instance type. |
| 400 | ImageNotSupportCl oudInit | ImageNotSupportCloudInit | The specified image does not support cloud-init. |
| 400 | SNAPSHOT AT BEF _ _ ORE ASSIGN DATE _ _ | InvalidSnapshotId.BasedSnapsh otTooOld | The specified snapshot is created before 2013-07-15. |
| 400 | ECS BIZ QUOTA US _ _ _ ER | QuotaExceed.AfterpayInstance | The maximum number of Pay- As-You-Go instances is exceeded: %s. |
| 400 | YUNMARKET BIZ IM _ _ AGE IS UNSUPPORT _ _ ED | InvalidMarketImageChargeType. NotSupport | The specified chargeType of marketImage is unsupported. |
| 400 | Abs.InvalidInstance Name.Malformed | InvalidInstanceName.Malformed | The specified parameter "InstanceName" is not valid. |
| 400 | NICKNAME ILLEGAL _ | InvalidInstanceName.Malformed | The specified parameter "InstanceName" is not valid. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DESCRIPTION ILLEG _ AL | InvalidDescription.Malformed | The specified parameter "Description" is not valid. |
| 400 | Abs.InvalidDiskNam e.Malformed | InvalidDiskName.Malformed | The specified parameter "SystemDisk.DiskName or DataDisk.n.DiskName" is not valid. |
| 400 | Abs.InvalidDiskDesc ription.Malformed | InvalidDiskDescription.Malforme d | The specified parameter "SystemDisk.DiskDescription or DataDisk.n.Description" is not valid. |
| 400 | ZONE NOT IN AVAI _ _ _ LABLE IZ _ | InvalidParameter.Conflict | The specified region and cluster do not match. |
| 400 | GROUP VSW VPC M _ _ _ ISMATCH | InvalidParameter.Mismatch | Specified security group and virtual switch are not in the same VPC. |
| 400 | -1201004 | InvalidParameter.Mismatch | Specified security group and virtual switch are not in the same VPC. |
| 400 | VSW INTERNET BAN _ _ DWIDTH CONFLICT _ | InvalidNetworkType.Mismatch | Specified parameter InternetMaxBandwidthIn or InternetMaxBandwidthOut conflict with instance network type. |
| 400 | VPC INSTANCE NOT _ _ NEED BANDWIDTH _ _ | InvalidNetworkType.Mismatch | Specified parameter InternetMaxBandwidthIn or InternetMaxBandwidthOut conflict with instance network type. |
| 400 | VPC INSTANCE NOT _ _ NEED INTERNET C _ _ _ HARGETYPE | InvalidNetworkType.Mismatch | Specified parameter "InternetChargeType" conflict with instance network type. |
| 400 | PRIVATE IP INVALID _ _ | InvalidPrivateIpAddress | Specified private IP address is not in the CIDR block of virtual switch. |
| 400 | InvalidIp.Address | InvalidPrivateIpAddress.Malform ed | Specified private IP address is invalid. |
| 400 | IP ALREADY USED _ _ | InvalidPrivateIpAddress.Duplicat ed | Specified private IP address is duplicated. |
| 400 | VPC PRIVATE IP NO _ _ _ ENOUGH _ | QuotaExceeded.PrivateIpAddres s | Don't have enough private IPs in this switch. |
| 400 | QUOTA FULL _ | QuotaExceeded | Living instances quota exceeded in this VPC. |
| 400 | VPC VSWITCH STAT _ _ US ILLEGAL _ | IncorrectVSwitchStatus | The current status of virtual switch does not support this operation. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IZ IS EMPTY _ _ | InvalidParameter.Mismatch | Specified virtual switch is not in the specified zone. |
| 400 | ZONE NO RESOURC _ _ E SUPPORT _ | ResourceNotAvailable | Resource you requested is not available in this region or zone. |
| 400 | VPC VSWITCHID IN _ _ VALID | MissingParameter | The input parameter "VSwitchId" that is mandatory for processing this request is not supplied. |
| 400 | PASSWORD ILLEGAL _ | InvalidPassword.Malformed | The specified parameter "Password" is not valid. |
| 400 | DISK CATEGORY NO _ _ TMATCH | InvalidDiskCategory.Mismatch | The specified disk categories' combination is not supported. |
| 400 | Abs.InvalidDiskSize. ValueNotSupported | InvalidDataDiskSize.ValueNotSu pported | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. |
| 400 | Abs.IoOptimized.Val ueNotSupported | InvalidIoOptimizedValue.ValueN otSupported | IoOptimized value not supported. |
| 400 | Abs.MissingParamte r.Period | MissingParamter | The specified parameter "Period" is not null. |
| 400 | Abs.InvalidPeriod.Va lueNotSupported | InvalidPeriod | The specified period is not valid. |
| 400 | ORDER.PERIOD INV _ ALID | InvalidPeriod | The specified period is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085155 | InvalidDataDiskCategory.ValueN otSupported | The specified parameter " DataDisk.n.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085127 | InvalidDataDiskCategory.ValueN otSupported | The specified parameter " DataDisk.n.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085156 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084451 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084502 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199822 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085137 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | PARAMETER DISK SI _ _ ZE ILLEGAL 100199 _ _ 834 | InstanceDiskCategoryLimitExcee d | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. |
| 400 | ECS GET INSTANCE _ _ TYPE FAIL _ _ | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | ECS NO INSTANCE _ _ _ TYPE MATCH _ | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00379127 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00358417 | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00458642 | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00358158 | InvalidParameter | The specified vm bandwidth is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085472 | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00374288 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter SystemDisk.Category is not valid. |
| 400 | IMAGE NOT SUPPO _ _ RTED | InvalidParameter.Conflict | The specified image does not support the specified instance type. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00615988 | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00390589 | InvalidParameter.Bandwidth | The specified parameter Bandwidth is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00390177 | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | PARAMETER DISK SI _ _ ZE ILLEGAL 100179 _ _ 277 | InvalidDataDiskSize.ValueNotSu pported | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. |
| 400 | -90020 | InvalidIPAddress.AlreadyUsed | The specified IPAddress is already used by other resource. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |

| 400 | InvalidUserData.Size Exceeded | InvalidUserData.SizeExceeded | The specified parameter "UserData" exceeds the size. |
|---|---|---|---|
| 400 | InvalidUserData.Not Vpc | InvalidUserData.NotSupported | The specified parameter "UserData" only support the vpc and IoOptimized Instance. |
| 400 | InvalidUserData.Not Kvm | InvalidUserData.NotSupported | The specified parameter "UserData" only support the vpc and IoOptimized Instance. |
| 400 | Abs.InvalidDataDisk s.MalFormed | InstanceDiskNumber.LimitExcee d | The total number of specified disk in an instance exceeds. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL A _ _ _ RREARAGE | Account.Arrearage | Your account has an outstanding payment. |
| 400 | INVALID DISK CATE _ _ GORY | InvalidDiskCategory.ValueNotSu pported | The specified parameter "DiskCategory" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 01433416 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | Abs.InvalidAutoRene wPeriod.ValueNotSu pported | InvalidAutoRenewPeriod.ValueN otSupported | The specified autoRenewPeriod is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL Q _ _ _ UOTA EXCEED _ | QuotaExceed.AfterpayInstance | The maximum number of Pay- As-You-Go instances is exceeded. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 01570138 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 01893140 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 02080588 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 02080334 | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | Abs.InvalidSpotStrat egy | InvalidSpotStrategy | The specified SpotStrategy is not valid. |
| 400 | Abs.SpotStrategy.E mptyZoneID | InvalidSpotParam.EmptyZoneID | The specified ZoneId is empty when SpotStrategy is set. |
| 400 | Abs.InvalidSpotPrice Limit | InvalidSpotPriceLimit | The specified SpotPriceLimitis not valid. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidSpotDura tion | InvalidSpotDuration | The specified SpotDuration is not valid. |
| 400 | Abs.InvalidSpotAuth | InvalidSpotAuthorized | The specified Spot param is unauthorized. |
| 400 | Abs.InvalidSpotPreP ay | InvalidSpotPrepaid | The specified Spot type is not support PrePay Instance. |
| 400 | Abs.Abs.InvalidSpotI nstanceUID | InvalidSpotAliUid | The specified UID is not authorized to use SPOT instance. |
| 400 | InvalidTagKey.Malfo rmed | InvalidTagKey.Malformed | The specified Tag.n.Key is not valid. |
| 400 | Invalid.Bandwidth.P ublicOut | InvalidParameter.Bandwidth | %s |
| 400 | Invalid.DataDisk.Cat egory | InvalidDataDiskCategory.ValueN otSupported | %s |
| 400 | Invalid.SystemDisk. Category | InvalidSystemDiskCategory.Valu eNotSupported | %s |
| 400 | Invalid.Conflict | InvalidParameter.Conflict | %s |
| 400 | Invalid.Bandwidth.P ayType | InvalidInternetChargeType.Value NotSupported | %s |
| 400 | Invalid.Instance.Typ e | InvalidInstanceType.ValueNotSu pported | %s |
| 400 | Invalid.location.Regi on | RegionUnauthorized | %s |
| 400 | Invalid.location.Zon e | Zone.NotOnSale | %s |
| 400 | Invalid.SystemDisk. Size | InvalidSystemDiskSize.ValueNot Supported | %s |
| 400 | Invalid.DataDisk.Siz e | InvalidDataDiskSize.ValueNotSu pported | %s |
| 400 | InvalidParams.Hostn ame | InvalidHostName.Malformed | The specified parameter "HostName" is not valid. |
| 400 | -1018002 | InvalidInstanceType.ValueNotSu pported | The specified parameter "KeyPairName" only support IoOptimized Instance. |
| 400 | KeyPairInstance.Not Kvm | InvalidInstanceType.ValueNotSu pported | The specified parameter "KeyPairName" only support IoOptimized Instance. |
| 400 | Invalid.ValueUnauth orized | OperationDenied | The specified InstanceType or Zone is not available or not authorized. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1017012 | InvalidParameter.EncryptedIlleg al | %s |
| 400 | -1017013 | InvalidParameter.EncryptedNotS upported | %s |
| 400 | PARAMETER CONFLI _ CT | EncryptedOption.Conflict | %s |
| 400 | DISK CATEGORY IS _ _ _ NOT SUPPORT ENC _ _ RYPTED | InvalidParameter.EncryptedNotS upported | %s |
| 400 | ECS SPOT USER PRI _ _ _ CE MUST LARGE TH _ _ _ AN PUBLIC PRICE _ _ | InvalidSpotPriceLimit.LowerThan PublicPrice | The specified parameter "soptPriceLimit" can't be lower than current public price. |
| 400 | HPC CLUSTER ID IS _ _ _ UNNECESSARY _ | InvalidHpcClusterId.Unnecessary | The specified HpcClusterId is unnecessary. |
| 400 | VSWITCH IS EMPTY _ _ | InvalidVSwitchId.Necessary | The VSwitchId is necessary. |
| 400 | HPC CLUSTER ID IS _ _ _ EMPTY _ | InvalidHpcClusterId.Necessary | The HpcClusterId is necessary. |
| 400 | HPC CLUSTER ID IS _ _ _ NOT EXIST _ _ | InvalidHpcClusterId.NotFound | The specified HpcClusterId is not found. |
| 400 | HPC CLUSTER IS C _ _ _ REATING | InvalidHpcClusterId.Creating | The specified HpcClusterId is creating. |
| 400 | -1014097 | QuotaExceeded.PrivateIpAddres s | Don't have enough private IPs in this switch. |
| 400 | Abs.InvalidPeriodTy pe.Malformed | InvalidPeriodUnit.ValueNotSupp orted | The specified parameter PeriodUnit is not valid. |
| 400 | UNSUPPORTED ENC _ RYPTED SNAPSHOT _ | IncorrectImageStatus | Encrypted snapshots do not support this operation. |
| 400 | InvalidTagValue.Mal formed | InvalidTagValue.Malformed | The specified Tag.n.Value is not valid. |
| 400 | GROUP NOT IN DEF _ _ _ AULTVPC | InvalidSecurityGroup.NotInDefau ltVpc | %s |
| 400 | VPC NOT FOUND F _ _ _ ROM VSW _ | VpcNotFound | Vpc is not found according to the specified VSwitch or the vpc does not belong to you. |
| 400 | PRICE.PRICING PLAN _ RESULT NOT FOUN _ _ _ D | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | Abs.InvalidSpotInter ruptionBehavior | InvalidSpotInterruptionBehavior | %s |
| 400 | PAY.MAYI WITHHOL _ DING AGREEMENT I _ _ LLEGAL | OperationDenied.IllegalPayment Policy | The current payment policy is illegal, please connect your service provider to authenticate relative agreement. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 400 | Abs.InvalidDeploym entOnHost.ValueNot Supported | InvalidDeploymentOnHost | %s |
| 400 | Abs.InvalidSpotStrat egyOnHost.ValueNo tSupported | InvalidInstanceChargeType.NotS upport | The Dedicated host not support the specified Instance charge type. |
| 400 | Abs.InvalidSpotPrice LimitOnHost.ValueN otSupported | InvalidInstanceChargeType.NotS upport | The Dedicated host not support the specified Instance charge type. |
| 400 | CLASSIC NOT SUPP _ _ ORT | InvalidNetworkType.NotSupport ed | The classic networkType not support create ECS on dedicatedHost. |
| 400 | HOST NOT EXIST _ _ | InvalidDedicatedHostId.NotFoun d | The specified DedicatedHostId does not exist. |
| 400 | HOST BUSINESS ST _ _ ATUS NOT VALID _ _ | InvalidDedicatedHostStatus.Not Support | Operation denied due to dedicated host status. |
| 400 | HOST STATUS NOT _ _ _ VALID | IncorrectDedicatedHostStatus | The current status of the resource does not support this operation. |
| 400 | HOST CHARGE TYP _ _ E NOT SUPPORT _ _ | ChargeTypeViolation.PostPaidDe dicatedHost | Prepaid instance onto postpaid dedicated host is not allowed. |
| 400 | ECS ON HOST NOT _ _ _ SUPPORT _ | InvalidPeriod.ExceededDedicate dHost | Instance expired date can't exceed dedicated host expired date. |
| 400 | DEDICATED HOST T _ _ YPE IS ILLEGAL _ _ | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorize. |
| 400 | DEDICATED HOST N _ _ OT SUPPORT THE I _ _ _ NSTANCE TYPE _ | DedicatedHostType.Unmatched | The specified DedicatedHostType doesn?t match the instance type. |
| 400 | DEDICATED HOST R _ _ ESOURCE NOT ENO _ _ UGH | NoAvaliableDedicatedHost | There's no enough resource on the specified dedicated host. |
| 400 | -305 | InvalidDedicatedHostId.NotFoun d | The specified DedicatedHostId does not exist. |
| 400 | DEDICATED HOST P _ _ AY TYPE NOT SUPP _ _ _ ORTED THE VM PA _ _ _ Y TYPE _ | ChargeTypeViolation.PostPaidDe dicatedHost | Prepaid instance onto postpaid dedicated host is not allowed. |
| 400 | DEDICATED HOST N _ _ O AVAILABLE HOST _ _ | NoAvaliableDedicatedHost | No available dedicated host or not enough resource on dedicated host. |
| 400 | INVALID PARAMETE _ R AFFINITY _ | InvalidParameter.Affinity | The specified Affinity is invalid. |
| 400 | INVALID PARAMETE _ R TENANCY _ | InvalidParameter.Tenancy | The specified Tenancy is invalid. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter.Aff inity | InvalidParameter.Affinity | The specified Affinity is invalid. |
| 400 | InvalidParameter.Te nancy | InvalidParam.Tenancy | The specified Tenancy is invalid. |
| 400 | InvalidParameter.Cr editSpecification | InvalidParameter.CreditSpecifica tion | The specified CreditSpecification is not supported in this region. |
| 400 | YUNMARKET BIZ MI _ _ RROR IMAGE IS UN _ _ _ USABLE | IncorrectImageStatus | The specified image is an Alibaba Cloud Marketplace image. The sale of this image has ended. For more information, contact the image service provider. |
| 400 | INSTANCE TYPE NO _ _ T SUPPORT BY DEP _ _ _ LOYMENT SET _ | InvalidInstanceType.NotSupport ed | The specified instanceType is not supported by the deployment set. |
| 400 | IMAGE ARCHITECTU _ RE NOT MATCH INS _ _ _ TANCE TYPE _ | InvalidInstanceType.NotSupport ed | The specified instanceType is not supported by the image architecture. |
| 400 | VPC ZONE NOT SU _ _ _ PPORT CREATE _ | InvalidVpcZone.NotSupported | Zone of the specified VSwitch is not available for creating, please try in other zones. |
| 400 | VPC DEFAULT DEFA _ _ ULTVPC STATUS ILL _ _ EAGE | IncorrectDefaultVpcStatus | The status of the default VPC is invalid. |
| 400 | InvalidKMSKeyId.Not MatchParamEncrypt ed | InvalidParameter.EncryptedIlleg al | The specified parameter Encrypted must be true when kmsKeyId is not empty. |
| 400 | InvalidKMSKeyId.Inst anceTypeNotSuppor ted | IoOptimized.NotSupported | The specified instance must be IoOptimized instance when kmsKeyId is not empty. |
| 400 | Abs.InvalidClientTok en.Malformed | InvalidClientToken.ValueNotSup ported | The ClientToken provided is invalid. |
| 400 | Trade Not Support _ _ _ Async Pay _ | OperationDenied | The current user does not support this operation. |
| 400 | ORDER.BID USER O _ _ RDER FORBIDDEN _ | OperationDenied | The current user does not support this operation. |
| 400 | CR NOT EXIST _ _ | InvalidCapacityReservationId.No tFound | The specified CapacityReservationId does not exist. |
| 400 | CR RESOURCE NOT _ _ ENOUGH _ | LackResource | There's no enough resource on the specified capacity reservation. |
| 400 | Abs.InvalidInstanceT ype.Null | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Duplicate.TagKey | Duplicate.TagKey | The Tag.N.Key contain duplicate key. |
| 400 | InvalidParam.Arns | InvalidParameter.Arns | The specified Arns is not valid. |
| 400 | INSTANCE NOT SUP _ _ PORT ENTERPRISE _ _ GROUP | InvalidOperation.NotSupportEnt erpriseGroup | The specified instance type doesn't support enterprise level security group. |
| 400 | DEDICATED HOST V _ _ M TENANCY ILLEGA _ _ L | InvalidParam.Tenancy | The specified Tenancy is invalid. |
| 400 | DEDICATED HOST N _ _ O AVAILABLE HOST _ _ FOR AUTOPLACEM _ _ ENT | NoAvaliableDedicatedHost | A dedicated host with sufficient available resources cannot be found. |
| 400 | NO AVAILABLE HOS _ _ T EXIST _ | NoAvaliableDedicatedHost | A dedicated host with sufficient available resources cannot be found. |
| 400 | DEDICATED HOST V _ _ M AFFINITY ILLEGAL _ _ | InvalidParameter.Affinity | The specified Affinity is invalid. |
| 400 | VPC SWITCH STATU _ _ S ERROR _ | IncorrectVSwitchStatus | The current status of vSwitch does not support this operation. |
| 400 | INSTANCE NOT SUP _ _ PORT MULTI GROUP _ _ TYPE _ | InvalidOperation.MultiGroupTyp e | The specified instance can't join different types of security group. |
| 400 | PAY.AMOUNT LIMIT _ _ EXCEEDED | InvalidAccountStatus.PayAmoun tLimitExceeded | Your account is being restricted, because you have no default payment method or you are not authorized. |
| 400 | PARAMETER PERFO _ RMANCE LEVEL ILL _ _ EGAL | InvalidPerformanceLevel.Malfor med | The specified parameter DataDisk.n.PerformanceLevel is not valid. |
| 400 | Abs.InvalidPerforma nceLevel.ValueNotS upported | InvalidPerformanceLevel.Malfor med | The specified parameter DataDisk.n.PerformanceLevel is not valid. |
| 400 | InvalidSecurityGrou p.NetworkType | InvalidSecurityGroup.NetworkTy pe | %s |
| 400 | PREPAY DISK QUOT _ _ A EXCEEDED _ | QuotaExceeded.PrepayDataDisk Capacity | The quota of prepay data disk capacity exceeds. |
| 400 | INVALID CUSTOM I _ _ NSTANCE TYPE _ | InvalidCustomInstanceType.Not Supported | The specified custom instance type is invalid. |
| 400 | -1201007 | InvalidParameter | %s |
| 400 | -90030 | QuotaExceeded.PrivateIpAddres s | There is not enough private ip in the specified VSwitch. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | EnterpriseSecurityG roupEniLimitExceed | InvalidOperation.EniCountExcee ded | The maximum number of eni in a enterprise security group is exceeded. |
| 400 | ALI CROUP 2 CLOU _ _ _ D USER CANNOT B _ _ _ UY NOT INNER CO _ _ _ MMODITY | AccountForbidden.ProductCreati onLimited | The commodity must be officially operated by Aliyun and in pay-as-you-go billing method. |
| 400 | UnexpectedImageFa mily.ImageIdProvide d | UnexpectedImageFamily.ImageI dSupplied | The input parameter ImageFamily must be null when image id is set. |
| 400 | InvalidEncrypted.No tMatchEncryptAlgori thm | InvalidEncrypted.NotMatchEncry ptAlgorithm | The specified parameter Encrypted must be true when EncryptAlgorithm is not empty. |
| 400 | InvalidEncrypted.No tMatchKmsKeyId | InvalidEncrypted.NotMatchKmsK eyId | The specified parameter Encrypted must be true when KmsKeyId is not empty. |
| 400 | InvalidEncrypted.No tMatchSnapshot | InvalidEncrypted.NotMatchSnap shot | The specified parameter Encrypted is different from the Encrypted of the snapshot. |
| 400 | InvalidEncryptAlgori thm.NotMatchSnaps hot | InvalidEncryptAlgorithm.NotMat chSnapshot | The specified parameter EncryptAlgorithm is different from the encrypt algorithm of the snapshot. |
| 400 | InvalidKmsKeyId.Not MatchSnapshot | InvalidKmsKeyId.NotMatchSnaps hot | The specified parameter KmsKeyId is different from the KmsKeyId of the snapshot. |
| 400 | InvalidEncryptAlgori thm | InvalidEncryptAlgorithm | The specified parameter EncryptAlgorithm is not valid. |
| 400 | InvalidHttpEndpoint. NotSupported | InvalidHttpEndpoint.NotSupport ed | The specified HttpEndpoint not supported, you can use enabled(default) or disabled. |
| 400 | InvalidHttpTokens.N otSupported | InvalidHttpTokens.NotSupported | The specified HttpTokens not supported, you can use optional(default) or required. |
| 400 | InvalidHttpPutRespo nseHopLimit.NotSup ported | InvalidHttpPutResponseHopLimit .NotSupported | The specified HttpPutResponseHopLimit not supported, more than 1 and less than 64 is reasonable. |
| 400 | IP MALFORMED _ | InvalidPrivateIpAddress.Malform ed | Specified private IP address is malformed. |
| 400 | VPC HAS ENABLED _ _ _ SENIOR NETWORK _ _ FEATURE | InvalidOperation.VpcHasEnabled AdvancedNetworkFeature | The specified vpc has enabled advanced network feature. |
| 400 | CR NOT SUPPORT T _ _ _ HE VM PAY TYPE _ _ _ | InvalidChargeType.CapacityRese rvationNotSupported | %s |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IZ OR INSTANCE TY _ _ _ PE FAMILY NOT SU _ _ _ PPORT PL0 _ | InvalidPerformanceLevel.ValueN otSupported | The current ZoneId or InstanceType does not support PL0 of cloud essd. _ |
| 400 | KMS KEY ID MUST _ _ _ _ BE SYMMETRICAL _ | InvalidKMSKeyId.NotSymmetric | The specified parameter KmsKeyId must be symmetric. |
| 400 | DDH CLUSTER NOT _ _ EXIST _ | InvalidDedicatedHostClusterId.N otFound | The specified DedicatedHostClusterId does not exist. |
| 400 | DDH CLUSTER NOT _ _ VALID _ | InvalidDedicatedHostClusterId.In Valid | The specified Dedicated Host Cluster is invalid. |
| 400 | TRADE DISTRIBUTO _ R CHECK FAIL _ _ | InvalidOperation.UserNotSuppor ted | Reseller user do not support purchase at the moment. |
| 400 | DEPLOYMENT SET _ _ NOT FOUND _ | InvalidDeploymentSetId.NotFoun d | The parameter DeploymentSetId is invalid. |
| 400 | Abs.MissingParamet er.PackageId | MissingParameter.PrivatePoolOp tionsId | The specified PrivatePoolOptions.Id should not be null. |
| 400 | Abs.InvalidResource PackageIds | Invalid.PrivatePoolOptionsId | The specified PrivatePoolOptions.Id is invalid. |
| 400 | Abs.NoNeed.Packag eId | Invalid.PrivatePoolOptionsId | The parameter PrivatePoolOptions.Id should be null when PrivatePoolOptions.MatchCriteria is not Target. |
| 400 | RP DDH NOT SUPP _ _ _ ORT | DedicatedHostNotSupported | DedicatedHost is not supported for PrivatePool. |
| 400 | RP SPOT NOT SUPP _ _ _ ORT | SpotNotSupported | Spot is not supported for PrivatePool. |
| 400 | RP CLASSICAL NOT _ _ _ SUPPORT | ClassicNetworkNotSupported | Classic network is not supported for PrivatePool. |
| 400 | RP INSTANCE NOT _ _ _ EXISTS | Invalid.InstanceId | Instance does not exist. |
| 400 | TARGET MODE NOT _ _ SUPPORT THE OPE _ _ _ RATION | Invalid.PrivatePoolOptions.Match Criteria | Target mode does not support this operation. |
| 400 | RP MISSING ATTAC _ _ HMENT ID _ | MissingParameter.PrivatePoolOp tions.Id | The specified PrivatePoolOptions.Id should not be null. |
| 400 | RP RESOURCE PAC _ _ KAGE NOT EXISTS _ _ | Invalid.PrivatePoolOptions.Id | The PrivatePool does not exist. |
| 400 | RP CR NOT EXISTS _ _ _ | Invalid.PrivatePoolOptions.Id | The PrivatePool does not exist. |
| 400 | RP INSTANCE TYPE _ _ _ MISS MATCH _ | Invalid.InstanceType | The InstanceType does not match the PrivatePool. |

|  | 开发指南·API参 | 考 |  | 云服务器EC | S |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RP INSTANCE CHAR _ _ GE TYPE MISS MAT _ _ _ CH | Invalid.InstanceChargeType | The InstanceChargeType does not match the PrivatePool. |
| 400 | RP ZONE ID NOT M _ _ _ _ ATCH | Invalid.ZoneId | The ZoneId does not match the PrivatePool. |
| 400 | RP PACKAGE USED _ _ _ UP | Invalid.PrivatePoolOptions.NoSto ck | The PrivatePool has been used up. |
| 400 | RP INSTANCE MATC _ _ H CRITERIA NOT M _ _ _ ATCH | Invalid.PrivatePoolOptions.Match Criteria | The PrivatePoolOptions.MatchCriteria does not match the PrivatePool. |
| 400 | RP PLATFORM NOT _ _ _ MATCH | InvalidPlatform.ValueNotSupport ed | The Platform does not match the PrivatePool. |
| 400 | RP PACKAGE EXPIR _ _ ED | Invalid.PrivatePoolOptions.status | The PrivatePool is expired or inactive. |
| 400 | RP PACKAGE STATU _ _ S NOT VALID _ _ | Invalid.PrivatePoolOptions.status | The PrivatePool status is not valid. |
| 400 | RP INSTANCE OPER _ _ ATE TOO LATE _ _ | Invalid.PrivatePoolOptions.status | The Instance should be created within 48 hours once the PrivatePool is started. |
| 400 | RP PACKAGE INSTA _ _ NCE NOT CONSISTE _ _ NT | InvalidAliUid | The PrivatePool does not belong to the user of the Instance. |
| 400 | RP INSTANCE NOT _ _ _ ATTACHED | Invalid.InstanceId | The Instance dose not attached to a PrivatePool. |
| 400 | HibernationConfigur ed.InstanceType.Not Support | HibernationConfigured.InstanceT ypeNotSupport | The specified instance type is not support. |
| 400 | HibernationConfigur ed.Image.NotEncryp ted | HibernationConfigured.ImageNo tEncrypted | The hibernation configured instance only support encrypted image. |
| 400 | HibernationConfigur ed.MemorySize.Too Big | HibernationConfigured.MemoryS izeTooBig | The hibernation configured instance memory size is too big. |
| 400 | InvalidSystemDiskSi ze.LessThanMemSiz e | InvalidSystemDiskSize.LessThan MemSize | The specified parameter SystemDisk.Size is less than the memory size. |
| 400 | CLOUD BOX IZ NOT _ _ _ SUPPORT THIS OP _ _ _ ERATION | InvalidCloudBoxZone.Operation NotSupported | The cloud box zone does not support creating prepaid or encrypted resources. |
| 400 | CMKUnauthorized | InvalidParameter.KMSKeyId.CMK Unauthorized | This operation for kmsKeyId is forbidden by KMS. If you need further assistance, you can contact the KMS Technical Support. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidMaxBand widthOut.Malformed | InvalidInternetMaxBandwidthOut .Malformed | The specified parameter InternetMaxBandwidthOut is not valid. |
| 400 | Abs.InvalidMaxBand widthIn.Malformed | InvalidInternetMaxBandwidthIn. Malformed | The specified parameter InternetMaxBandwidthIn is not valid. |
| 400 | InvalidParameter.Cl oudboxNotSupporte d | InvalidParameter.CloudboxNotS upported | %s |
| 400 | NOT SUPPORT SHA _ _ RE SNAPSHOT ENC _ _ RYPT | NotSupportSnapshotEncrypted.S hareImage | Shared snapshot creating encrypted disks with native snapshot encrypt is not supported. |
| 400 | ELASIC COMMON R _ _ ESOUCE QUOTA EX _ _ CEEDED | QuotaExceed.DiskCapacity | The used capacity of disk type has exceeded the quota in the zone, %s. |
| 400 | ECS ON HOST EXC _ _ _ EEDED | InvalidPeriod.ExceededDedicate dHost | Instance expired date can not exceed dedicated host expired date. |
| 400 | CREATE ENCRYPTE _ D KEY FAIL _ _ | InvalidParameter.DataEncrypted KeyCreateFailed | Create kms data encrypted key fail. If you need further assistance, you can contact the KMS Technical Support. |
| 400 | CREATE ENCRYPTE _ D KEY FAIL _ _ | InvalidParameter.DataEncrypted KeyCreateFailed | Create kms data encrypted key fail. If you need further assistance, you can contact the KMS Technical Support. |
| 400 | DISK CATEGORY IS _ _ _ NOT SUPPORT _ | InvalidDiskCategory.NotSupport ed | The specified disk category is not supported. |
| 400 | INSTANCE MUST IN _ _ DEPLOYMENT SET _ _ _ IZ | InvalidDestinationZone.Deploym entSetMismatch | Error happened, %s. |
| 400 | InvalidPermission.Q ueryPriceRequired | NoPermission.Price | The operation requires price permission. Please either apply for permission from your main account, or set the parameter AutoPay as true. |
| 400 | InvalidParameter.De dicatedRegionNotSu pported | InvalidParameter.DedicatedRegi onNotSupported | The specified action is rejected because the specified ECS instance in the dedicated region does not support public IP. |
| 400 | KMS SERVICE NOT _ _ _ ENABLED | InvalidParameter.KmsNotEnable d | Failed to perform this operation because KMS is not activated. |
| 400 | KMS.Not.Enabled | InvalidParameter.Encrypted.Kms NotEnable | Failed to perform this operation because KMS is not activated. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NOT SUPPORT SHA _ _ RE ENCRYPTED IMA _ _ GE CREATE DISK W _ _ _ ITHOUT ENCRYPTIO _ N | InvalidParam.EncryptedMismatc h | Creating encrypted disks with shared encrypted image requires replacing encryption keys. |
| 400 | SNAPSHOT ENCRYP _ T CONFLICT _ | InvalidParameter.Encrypted | Creating non-encrypted disks with encrypted snapshots is not supported. |
| 400 | InvalidPrivateIpAddr ess.Duplicated | InvalidPrivateIpAddress.Duplicat ed | The specified private IP address "%s" is duplicated. |
| 400 | QuotaExceeded.Inte rnetBandwidth | QuotaExceeded.InternetBandwid th | %s. |
| 400 | -1000008 | InvalidVSwitchId.NotFound | The specified VSwitch does not exist in the specified region. |
| 400 | Forbid.Create.TestA ccount | OperationDenied.TestAccountRe tricted | Test-account for testing has been prohibited from creating instance in this region. Please contact 400181. |
| 401 | NoPermission | InvalidRamRole.NotEcsRole | The specified ram role is not authorized for ecs, please check your role policy. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199819 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | YUNMARKET BIZ MI _ _ RROR USER NO SU _ _ _ BSCRIPTION | ImageNotSubscribed | The specified image has not be subscribed. |
| 403 | -300 | OperationDenied | The specified Image is disabled or is deleted. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179229 | InvalidSystemDiskCategory.Valu eUnauthorized | The disk category is not authorized. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179231 | InvalidSystemDiskCategory.Valu eUnauthorized | The disk category is not authorized. |
| 403 | SNAPSHOT CREATE _ NOT FINISHED _ _ | InvalidSnapshotId.NotReady | The specified snapshot has not completed yet. |
| 403 | SNAPSHOT DISK IN _ _ _ BLACK LIST _ | OperationDenied | The specified snapshot is not allowed to create disk. |
| 403 | SNAPSHOT IN BLAC _ _ K LIST _ | OperationDenied | The specified snapshot is not allowed to create disk. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179249 | InstanceDiskCategoryLimitExcee d | The total size of specified disk category in an instance exceeds. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | DISK MOUNT POINT _ _ DUPLICATE _ | InvalidDevice.InUse | The specified device has been occupied. |
| 403 | YUNMARKET BIZ MI _ _ RROR SALE OFF _ _ | ImageRemovedInMarket | The specified market image is not available, Or the specified user defined image includes product code because it is based on an image subscribed from marketplace, and that image in marketplace includeing exact the same product code has been removed. |
| 403 | IZ NOT IN SALE _ _ _ | OperationDenied | The creation of Instance to the specified Zone is not allowed. |
| 403 | IZ NOT SUPPORT C _ _ _ ATEGORIES | CategoryNotSupported | The specified zone does not offer the specified disk category. |
| 403 | ZONE NOT SUPPOR _ _ T SYSTEM CATEGO _ _ RY | OperationDenied | The specified Zone or cluster does not offer the specified disk category or the speicified zone and cluster do not match. |
| 403 | NOT AVAILABLE IZ _ _ _ SUPPORT CATEGORI _ ES EXISTS _ | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | ECS BIZ DISK QUO _ _ _ TA USER _ | QuotaExceed.PortableCloudDisk | The quota of portable cloud disk exceeds. |
| 403 | ECS NO BUY NOW _ _ _ | OperationDenied | Sales of this resource are temporarily suspended in the specified region; please try again later. |
| 403 | -503 | SecurityGroupInstanceLimitExce ed | The maximum number of instances in a security group is exceeded. |
| 403 | -3135 | NodeControllerUnavailable | The Node Controller is temporarily unavailable. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 006444 | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | NOT AVAILABLE IZ _ _ _ EXISTS | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | NOT AVAILABLE ZO _ _ NE SUPPORT SYSTE _ _ M CATEGORY EXIST _ _ S | CategoryNotSupported | The specified Zone or cluster does not offer the specified disk category. |
| 403 | PARAMETER SNAPS _ HOT CHECK DATA _ _ | InvalidSnapshotId.NotDataDiskS napshot | The specified snapshot is system disk snapshot. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | NOT AVAILABLE ZO _ _ NE SUPPORT CATE _ _ GORIES EXISTS _ | CategoryNotSupported | The specified cluster does not offer the specified disk category. |
| 403 | DISK PORTABLE DE _ _ LETE NOTMATCH _ | DeleteWithInstance.Conflict | The specified disk is not a portable disk and cannot be set to DeleteWithInstance attribute. |
| 403 | DISK CATEGORY PO _ _ RTABLE DELETE NO _ _ TMATCH | DeleteWithInstance.Conflict | The specified disk is not a portable disk and cannot be set to DeleteWithInstance attribute. |
| 403 | EXCEED DISK NUM _ _ _ FOR ONE ECS _ _ | InstanceDiskNumLimitExceed | The number of specified disk in an instance exceeds. |
| 403 | IMAGE MUST SUPP _ _ ORT IOOPTIMIZED _ | IoOptimized.NotSupported | The specified image is not support IoOptimized Instance. |
| 403 | ImageNotSupportIns tanceType | ImageNotSupportInstanceType | The specified image don't support the InstanceType instance. |
| 403 | -602 | InvalidDiskSize.TooSmall | Specified disk size is less than the size of snapshot. |
| 403 | -605 | OperationDenied | The type of the disk does not support the operation. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179235 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179240 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199830 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199826 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199813 | IoOptimized.NotSupported | Vpc is not support IoOptimized instance. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179448 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199821 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | ECS BIZ IMAGE IS _ _ _ _ DELETED | OperationDenied | The specified Image is disabled or is deleted. |
| 403 | ECS SNAPSHOTID I _ _ NVALID | OperationDenied | The specified snapshot is not allowed to create disk. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179252 | InstanceDiskCategoryLimitExcee d | The total size of specified disk category in an instance exceeds. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199839 | InstanceDiskCategoryLimitExcee d | The total size of specified disk category in an instance exceeds. |
| 403 | ECS BIZ CHECK NO _ _ _ T HAS ENOUGH ST _ _ _ OCK | OperationDenied | The resource is out of usage. |
| 403 | ECS IMAGE PRODU _ _ CT QUOTA USER _ _ | QuotaExceed.BuyImage | The specified image is from the image market, You have not bought it or your quota has been exceeded. |
| 403 | VSWITCH NOT EXIS _ _ T | InvalidVSwitchId.NotFound | The VSwitchId provided does not exist in our records. |
| 403 | InvalidParameter.Re sourceOwnerAccoun t | InvalidParameter.ResourceOwne rAccount | ResourceOwnerAccount is Invalid. |
| 403 | FUWU BIZ REGION _ _ _ FAIL 1006444 _ | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | InvalidUserData.NotI nWhiteList | InvalidUserData.Forbidden | User not authorized to input the parameter "UserData", please apply for permission "UserData". |
| 403 | NOT AVAILABLE IZ _ _ _ BIZ EXISTS _ | Zone.NotOpen | The specified zone is not granted to you to buy resources yet. |
| 403 | NOT AVAILABLE IZ _ _ _ AUZ EXISTS _ | Zone.NotOnSale | The specified zone is not available for purchase. |
| 403 | NOT AVAILABLE IZ _ _ _ ZONE SPECIFY EXIS _ _ TS | InvalidClusterId.NotFound | The specified clusterId does not exist. |
| 403 | INVALID RESOURCE _ TYPE NOT FOUND _ _ _ | InvalidResourceType.NotSupport ed | %s |
| 403 | ECS NOT HAS ENO _ _ _ UGH STOCK _ | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | NOT AVAILABLE IZ _ _ _ FLAVOR STOCK _ | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | INSTANCE TYPE NO _ _ T EXIST _ | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 403 | INSTANCE TYPE NO _ _ ZONE SUPPORT _ _ | InvalidInstanceType.ZoneNotSup ported | The specified zone does not support this instancetype. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | PARAMETER GROUP _ ECS QUOTA FULL _ _ _ | SecurityGroupInstanceLimitExce ed | The maximum number of instances in a security group is exceeded. |
| 403 | -60001 | OperationDenied | The resource is out of usage. |
| 403 | -60002 | OperationDenied | The resource is out of usage. |
| 403 | -60003 | OperationDenied | The resource is out of usage. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 01570141 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 01847383 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 01892808 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL I _ _ _ NVALID PAY METHO _ _ D | InvalidPayMethod | The specified pay method is not valid. |
| 403 | 2004 | OperationDenied.ImageNotValid | The specified Image is disabled or is deleted. |
| 403 | -60010 | OperationDenied | The resource is out of usage. |
| 403 | InvalidUserData.Bas e64FormatInvalid | InvalidUserData.Base64FormatIn valid | The specified UserData is not valid. |
| 403 | Offline.Instance.Typ e | InstanceType.Offline | %s |
| 403 | DependencyViolatio n.WindowsInstance | DependencyViolation.WindowsIn stance | The instance creating is window, cannot use ssh key pair to login. |
| 403 | DISK CATEGORY NO _ _ TMATCH COMPUTE _ _ INTENSIVE | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL N _ _ _ EED IDENTITY REGI _ _ STRATION | RealNameAuthenticationError | Your account has not passed the real-name authentication yet. |
| 403 | Abs.InvalidNetworkT ype.ValueNotSuppor ted | InvalidNetworkType.MismatchRa mRole | Ram role cannot be applied to instances of Classic network type. |
| 403 | InvalidUser.PassRole Forbidden | InvalidUser.PassRoleForbidden | The RAM user does not have the privilege to pass a RAM role. |
| 403 | IMAGE NOT SUPPO _ _ RT VSGX INSTANCE _ _ | InvalidImage.NotSupported | The specified image does not support vSGX instance. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | PAY.INSUFFICIENT B _ ALANCE | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |
| 403 | INSUFFICIENT BALA _ NCE | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |
| 403 | VPC INCORRECT ST _ _ ATUS | IncorrectVpcStatus | Current VPC status does not support this operation. |
| 403 | -60004 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60005 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60006 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60007 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60008 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60009 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60010 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60011 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60013 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60020 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | -60022 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60023 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60012 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -1015002 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | -60014 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | VALIDATION FORBI _ DDEN | InvalidParameter.NotMatch | %s |
| 403 | NetworkNotSupport CreateEcs | OperationDenied.InvalidNetwork Type | %s |
| 403 | CLASSIC NOT SUPP _ _ ORT | InvalidSpotInterruptionBehavior. ClassicNetworkNotSupport | The specified SpotInterruptionBehavior does not support Classic network Instance. |
| 403 | VM IS LOCAL NOT _ _ _ _ ALLOWED ARCHIVE _ | InvalidSpotInterruptionBehavior. LocalDiskNotSupport | The specified SpotInterruptionBehavior does not support local disk instance. |
| 403 | IMAGE NOT SUPPO _ _ RTED | OperationDenied.ImageNotValid | %s |
| 403 | DATA DISK QUOTA _ _ _ FULL | QuotaExceed.PostPaidDisk | Living postPaid disks quota exceeded. |
| 403 | DEPLOYMENT SET I _ _ NSTANCE QUOTA F _ _ ULL | QuotaExceed.DeploymentSetIns tanceQuotaFull | Instance quota in one deployment set exceeded. |
| 403 | -1017025 | InvalidDiskCategory.NotSupport ed | The specified disk category is not supported. |
| 403 | VPC DEFAULT VSWI _ _ TCH NOT ALLOWID _ _ _ IN VPC _ | InvalidVSwitch.DefaultVSwitchN otSupport | The specified zone in vpc can't support create default vSwitch. |
| 403 | ImageBIDNotPublish edToSpecifiedRegio n | OperationDenied.ImageNotValid | The specified image is not published in the region. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ImageNotPublishedT oSpecifiedRegion | OperationDenied.ImageNotValid | The specified image is not published in the region. |
| 403 | ImageNotAuthorized ToSpecifiedBid | OperationDenied.ImageNotValid | The specified image is not authorized. |
| 403 | ProductImageNotFo undInMarketplace | OperationDenied.ImageNotValid | The specified image is not found in marketplace. |
| 403 | DISK TYPE NOT SU _ _ _ PPORT | OperationDenied.LocalDiskUnsu pported | The configuration change is not allowed when the specified instance has local disks mounted. |
| 403 | INCONSISTENT SEC _ URITY GROUP AND _ _ _ VSWITCH | OperationDenied.InconsistentNe twork | The specified security group and vswitch are not in the same vpc. |
| 403 | VPC DEFAULT VSWI _ _ TCH NOT ALLOWED _ _ IN VPC _ _ | OperationDenied | If the network segment of the vswitch is the same as that of its VPC. Therefore, the VPC cannot create other vswitchs across the region. |
| 403 | VPC DEFAULT VSWI _ _ TCH EXIST _ | DefaultVswitch.Existed | The default vswitch for VPC already exists. |
| 403 | -60017 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | Abs.InvalidInstance ChargeType.WithDel etionProtection | InvalidChargeType.ValueNotSup ported | Deletion protection is only valid for postPaid instance, not for prePaid or spot instance. |
| 403 | PAY.INVALID INSTA _ NCE STATUS _ | IncorrectInstanceStatus | The current status of the resource does not support this operation. |
| 403 | vm with ephemeral _ _ disk _ | CategoryViolation | The specified instance does not support this operation because of its disk category. |
| 403 | IZ NOT MATCHED _ _ | ResourcesNotInSameZone | The specified instance and dedicated host are not in the same zone. |
| 403 | InvalidRegionId.Not Support | InvalidRegion.NotSupport | The specified region does not support byok. |
| 403 | InvalidUserId.NotIn WhiteList | UserNotInTheWhiteList | The user is not in byok white list. |
| 403 | CMKNotEnabled | InvalidParameter.KMSKeyId.CMK NotEnabled | The CMK needs to be enabled. |
| 403 | KMSUnauthorized | InvalidParameter.KMSKeyId.KMS Unauthorized | ECS service have no right to access your KMS. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | RR307 | SecurityRisk.3DVerification | We have detected a security risk with your default credit or debit card. Please proceed with verification via the link in your email. |
| 403 | PARAMETER SYSTE _ M DISK SIZE ILLEG _ _ _ AL | InvalidDisk.SystemDiskSize | The specified SystemDiskSize beyond the permitted range. |
| 403 | 12034 | InsufficientBalance | Your account does not have enough balance. |
| 403 | USERPROFILECOMPL ETE | OperationDenied | The user profile is not complete; try complete your basic info in account management page. |
| 403 | ORDER.MAYI SYNC _ _ ORDER ERROR _ | Mayi.InternalError | The request processing has failed due to some unknown error. |
| 403 | Invalid.Network.Typ e | InvalidNetworkType | The network type is not support in this region. |
| 403 | ORDER.ACCOUNT S _ TATUS ILLEGAL _ | InvalidAccountStatus | Your account status is invalid, please contact customer service. |
| 403 | InvalidUserId.NotInA rnsWhiteList | UserNotInTheWhiteList | The user is not in Arns white list. |
| 403 | InvalidVSwitchId.IpN otEnough | QuotaExceeded.PrivateIpAddres s | %s |
| 403 | InvalidVSwitchId.IpI nvalid | InvalidVSwitchId.IpInvalid | %s |
| 403 | PERFORMANCE LEV _ EL MUST LOWER _ _ | OperationDenied.PerformanceLe velNotMatch | The specified DataDisk.n.PerformanceLevel and DataDisk.n.Size do not match. |
| 403 | Abs.InvalidPerforma nceLevel.ValueMust Lower | OperationDenied.PerformanceLe velNotMatch | The specified DataDisk.n.PerformanceLevel and DataDisk.n.Size do not match. |
| 403 | InvalidStorageSetNa me.Malformed | InvalidStorageSetName.Malform ed | Specified parameter StorageSetName is not valid. |
| 403 | InvalidDescription.M alformed | InvalidDescription.Malformed | Specified parameter Description is not valid. |
| 403 | InvalidMaxPartitionN umber.Malformed | InvalidMaxPartitionNumber.Malf ormed | Specified parameter MaxPartitionNumber is not valid. |
| 403 | InvalidParameter.St orageSetPartitionNu mber | InvalidParameter.StorageSetPart itionNumber | Specified parameter StorageSetPartitionNumber is not valid. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidParameter.St orageSetId | InvalidParameter.StorageSetId | Specified parameter StorageSetId is not valid. |
| 403 | InvalidParameter.St orageSetZoneId | InvalidParameter.StorageSetZon eId | Specified parameter StorageSetZoneId is not valid. |
| 403 | ZONE NOT MATCH _ _ | InvalidParameter.StorageSetZon eId | Specified parameter ZoneNo does not match with StorageSet info. |
| 403 | QuotaExceed.Tags | QuotaExceed.Tags | %s |
| 403 | REGION NOT SUPPO _ _ RT SPOT DURATION _ _ INSTANCE _ | OperationDenied.RegionIdNotSu pported | Region not support spot duration instance. |
| 403 | FLAVOR NOT SUPP _ _ ORT SPOT DURATIO _ _ N INSTANCE _ | OperationDenied.FlavorNotSupp orted | Flavor not support spot duration instance. |
| 403 | TIMESTAMP NOT SU _ _ PPORT SPOT DURA _ _ TION INSTANCE _ | OperationDenied.TimestampNot Supported | Timestamp not support spot duration instance. |
| 403 | Forbid.VmCreate | OperationDenied.PrepayNotAvail able | Prepay instance is not available now. |
| 403 | Forbid.EcsCreate | OperationDenied.PaygNotAvaila ble | Pay-as-you-go instance is not available now. |
| 403 | INSTANCE NOT SUP _ _ PORT MULTI GROUP _ _ TYPE _ | EnterpriseGroupLimited.MutliGro upType | The specified instance can not join multi SecurityGroup types. |
| 403 | INSTANCE NOT SUP _ _ PORT ENTERPRISE _ _ GROUP | EnterpriseGroupLimited.Instance Type | The specified instance type does not support Enterprise SecurityGroup. |
| 403 | ALLOCATE UNDERL _ AY IP ERROR _ _ | InternalError.AllocateUnderlayIp | Allocate underlay ip for the instance error. |
| 403 | Abs.BidCreateResou rceForbid | OperationDenied.BidOwnResour ce | Bid user can not own resource. |
| 403 | CloudSSD.NotSuppo rted | OperationDenied.CloudSSDNotS upported | The specified available zone does not offer the cloud ssd _ disk, use cloud essd instead. _ |
| 403 | -1013041 | InvalidVPCStatus.NotWorking | The specified VPC subnet status is not working. |
| 403 | NO AVAILABLE ECS _ _ QUOTA _ | QuotaExceed.ElasticQuota | No additional quota is available for the specified ECS instance type. |
| 403 | ECS INSTANCE TYP _ _ E QUOTA EXCEEDE _ _ D | QuotaExceed.ElasticQuota | The number of the specified ECS instances has exceeded the quota of the specified instance type. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ECS VCPU QUOTA _ _ _ EXCEEDED | QuotaExceed.ElasticQuota | The number of vCPUs assigned to the ECS instances has exceeded the quota in the zone. |
| 403 | ECS INSTANCE TYP _ _ E OR VCPU QUOTA _ _ _ EXCEEDED _ | QuotaExceed.ElasticQuota | The number of the specified ECS instances has exceeded the quota of the specified instance type, or the number of vCPUs assigned to the ECS instances has exceeded the quota in the zone. |
| 403 | DISK CAPACITY QU _ _ OTA FULL _ | QuotaExceeded.PostpaidDataDis kCapacity | The quota of postpaid data disk capacity exceeds. |
| 403 | InvalidImageFamily. MissingAvailableIma ge | InvalidImageFamily.MissingAvail ableImage | There is no available image related to the specified image family. |
| 403 | InvalidRegionId.Not SupportEncryptAlgo rithm | InvalidRegionId.NotSupportEncr yptAlgorithm | The current region does not support creating encrypted disks with EncryptAlgorithm. |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | InvalidOperation.ResourceMana gedByCloudProduct | %s |
| 403 | InvalidDiskSize.TooS mall | InvalidDiskSize.TooSmall | Specified disk size is too small when choosing PL0 of cloud essd. _ |
| 403 | IMAGE CATEGORY _ _ NOT SUPPORT _ | DeleteWithInstance.Conflict | The specified image is from the image market, you cannot set DeleteWithInstance attribute to false. |
| 403 | PARAMETER GROUP _ TYPE MUST BE EN _ _ _ _ TERPRISE | Forbidden.OnlySupportEnterpris eGroup | %s |
| 403 | HibernationConfigur ed.Instance.Operati onForbidden | HibernationConfigured.Instance OperationForbidden | The operation is not permitted due to limit of the hibernation configured instance. |
| 403 | DISK NUMBER EXCE _ _ EDED | InstanceDiskLimitExceeded | The amount of the disk on instance reach its limits. |
| 403 | -60021 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | INSTANCE TYPE NO _ _ T SUPPORT DISK C _ _ _ ATEGORY | InvalidInstanceType.NotSupport DiskCategory | The instanceType of the specified instance does not support this disk category. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | DISK CATEGORY NO _ _ T SUPPORT SNAPSH _ _ OT ENCRYPT _ | NotSupportSnapshotEncrypted. DiskCategory | The specified disk category does not support creating encrypted system disks or creating encrypted data disks from snapshots. Check the DiskCategory or Encrypted parameter, or check your account for default encryption settings. |
| 403 | InvalidEncrypted.No tMatchDiskDefaultE ncryption | InvalidEncrypted.DefaultEncrypti onUnsupported | The specified parameter Encrypted must be true when default encryption is enabled. |
| 403 | InvalidOperation.Pu blicIpAddressNoStoc k | InvalidOperation.PublicIpAddress NoStock | The public IP address for the specified Region or ChargeType of the instance is out of stock. Please try another Region or ChargeType. |
| 403 | ELASTIC QUOTA RE _ _ CORD NOT FOUND _ _ | QuotaExceed.ElasticQuota | The request failed due to elastic quota check, details as follows: %s. |
| 403 | ELASTIC QUOTA EX _ _ CEEDED | QuotaExceed.ElasticQuota | The request failed due to elastic quota check, details as follows: %s. |
| 403 | IMAGE NOT AVAILA _ _ BLE | OperationDenied | The specified image is not available, please check the status of the image. |
| 404 | InvalidDedicatedBlo ckStorageClusterId. NotExist | InvalidStorageClusterId.NotExist | The specified StorageClusterId does not exist in current region. |
| 404 | -140 | InvalidRegionId.NotFound | The RegionId provided does not exist in our records. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 02367641 | InvalidRegionId.NotFound | The RegionId provided does not exist in our records. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00337079 | InvalidRegionId.NotFound | The RegionId provided does not exist in our records. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 02367793 | IoOptimized.NotSupported | The specified instancetype is not support IoOptimized instance. |
| 404 | IZ NOT EXISTS _ _ | InvalidZoneId.NotFound | The ZoneId provided does not exist in our records. |
| 404 | -560 | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |
| 404 | InvalidSecurityGrou pId.NotFound | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | PARAMETER SNAPS _ HOT | InvalidDataDiskSnapshotId.NotF ound | The specified parameter "DataDisk.n.SnapshotId" is not valid. |
| 404 | -910 | InvalidDataDiskSnapshotId.NotF ound | The specified parameter "DataDisk.n.SnapshotId" is not valid. |
| 404 | -150 | InvalidClusterId.NotFound | The ClusterId provided does not exist in our records. |
| 404 | ECS BIZ IMAGE NO _ _ _ T FOUND _ | OperationDenied | The specified Image is disabled or is deleted. |
| 404 | ECS BIZ IZ INVALID _ _ _ | InvalidZoneId.NotFound | The ZoneId provided does not exist in our records. |
| 404 | ECS SYSTEM IZ QU _ _ _ ERY ERROR _ | InvalidZoneId.NotFound | The ZoneId provided does not exist in our records. |
| 404 | IZ INVALID _ | InvalidZoneId.NotFound | The ZoneId provided does not exist in our records. |
| 404 | ECS BIZ SNAPSHOT _ _ INVALID _ | InvalidDataDiskSnapshotId.NotF ound | The specified parameter "DataDisk.n.SnapshotId" is not valid. |
| 404 | ECS SYSTEM SNAPS _ _ HOT QUERY ERROR _ _ | InvalidDataDiskSnapshotId.NotF ound | The specified parameter "DataDisk.n.SnapshotId" is not valid. |
| 404 | VSW NOT EXIST IN _ _ _ _ IZ | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 404 | USER NOT ALLOW _ _ _ BUY COMMODITY _ | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 404 | VPC VSWITCHID NO _ _ T EXISTS _ | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 404 | InvalidVSwitchId.Not Found | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 404 | InvalidImageId.NotF ound | InvalidImageId.NotFound | The specified ImageId does not exist. |
| 404 | Abs.ImageNotFound | InvalidImageId.NotFound | The specified ImageId does not exist. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199815 | IoOptimized.NotSupported | The specified instancetype is not support IoOptimized instance. |
| 404 | ECS CREATE ONE L _ _ _ IMIT BY SYNC _ _ | OperationDenied | Another Instance has been creating. |
| 404 | Abs.InvalidInstance ChargeType.ValueN otSupported | InvalidInstanceChargeType.NotF ound | The InstanceChargeType does not exist in our records. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | DependencyViolatio n.IoOptimized | DependencyViolation.IoOptimize d | The specified instancetype must be IoOptimized instance. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL N _ _ _ OCARD | PaymentMethodNotFound | No payment method has been registered on the account. |
| 404 | HOSTNAME ILLEGAL _ | HOSTNAME ILLEGAL _ | The specified parameter Hostname is not valid. |
| 404 | -101 | HOSTNAME ILLEGAL _ | The specified parameter Hostname is not valid. |
| 404 | InvalidSystemDiskSi ze.LessThanImageSi ze | InvalidSystemDiskSize.LessThan ImageSize | The specified parameter SystemDisk.Size is less than the image size. |
| 404 | SYSTEM DISK SIZE _ _ _ MUST LARGE THAN _ _ IMAGE _ | InvalidSystemDiskSize.LessThan ImageSize | The specified parameter SystemDisk.Size is less than the image size. |
| 404 | InvalidSystemDiskSi ze.LessThanMinSize | InvalidSystemDiskSize.LessThan MinSize | The specified parameter SystemDisk.Size is less than the min size. |
| 404 | InvalidSystemDiskSi ze.MoreThanMaxSiz e | InvalidSystemDiskSize.MoreTha nMaxSize | The specified SystemDisk.Size parameter exceeds the maximum size. |
| 404 | GROUP NOT EXIST _ _ | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |
| 404 | Abs.SnapshotNotFo und | InvalidDataDiskSnapshotId.NotF ound | The specified parameter DataDisk.n.SnapshotId is not valid. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00358157 | InvalidParameter | The specified vm bandwidth is not valid. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00458124 | InvalidSystemDiskSize | The specified parameter SystemDisk.Size is invalid. |
| 404 | NOT AVAILABLE IZ _ _ _ SPECIFY EXISTS _ | InvalidZoneId.NotFound | The specified ZoneId does not exist. |
| 404 | -1011020 | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |
| 404 | InvalidKeyPairName. NotFound | InvalidKeyPairName.NotFound | The specified parameter KeyPairName does not exist in our records. |
| 404 | InvalidRamRole.Not Found | InvalidRamRole.NotFound | The specified RAMRoleName does not exist. |
| 404 | InvalidResourceGro up | InvalidResourceGroup.NotFound | The ResourceGroup provided does not exist in our records. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | ImageNotFound | InvalidMarketImage.NotFound | The specified marketplace image does not exist, please change the imageId and try again. |
| 404 | -1023003 | DeploymentSet.NotFound | The specified deployment set does not exist. |
| 404 | INVALID INSTANCE _ _ TYPE | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 404 | KMSKeyIdNotFound | InvalidParameter.KMSKeyId.NotF ound | The specified KMSKeyId does not exist. |
| 404 | InvalidSecurityGrou pId.NotFound | InvalidSecurityGroupId.NotFoun d | %s |
| 404 | Abs.InvalidPortable. ValueNotSupported | InvalidDiskIds.NotPortable | The specified DiskId is not portable. |
| 404 | VSW NOT EXIST _ _ | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 409 | ECS TASK CONFLIC _ _ T | OperationConflict | Request was denied due to conflict with a previous request,please try again later. |
| 429 | Throttle.Resource | Throttling.Resource | The request throttle by resource operation. |
| 500 | SP SYS RESOURCE _ _ _ QUERY ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | -1 | InternalError | The request processing has failed due to some unknown error. |
| 500 | -1015019 | InternalError | The request processing has failed due to some unknown error. |
| 500 | GET COMMODITY F _ _ AILED | InternalError | The request processing has failed due to some unknown error. |
| 500 | -1000000 | InternalError | The request processing has failed due to some unknown error. |
| 500 | GET PURCHASEINFO _ FAILED _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | GENERATE YUNDISK _ INSTANCEID ERRO _ _ R | InternalError | The request processing has failed due to some unknown error. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | GENERATE ECS INS _ _ TANCEID ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | Constraint.Forbidde n | InternalError | %s |
| 500 | LxCheckService.Not Pass | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | CreditAndWhitelistC heck.NotPass | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | KMS.Service.Unavail able | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | SDK.ServerUnreach able | InternalError | The request processing has failed due to some unknown error. |
| 500 | Trade Sync Create _ _ _ Sub ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | SYSTEM.SYSTEM ER _ ROR | InternalError | The request processing has failed due to some unknown error. |
| 500 | SYSTEM.SALE VALID _ ATE UNEXPECTED E _ _ RROR | InternalError | The request processing has failed due to some unknown error. |
| 500 | PRICE.PRICING HSF _ _ TIMEOUT ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | -1023102 | InternalError | The request processing has failed due to some unknown error. |
| 500 | PRICE.WAN HUA TO _ _ NG SYS _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | Abs.InnerServiceFail ed | InternalError | The request processing has failed due to some unknown error. |
| 500 | Trade Complete Art _ _ icle ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | RAMSerivceUnavaila bleTemporary | InternalError | The request processing has failed due to some unknown error, exception or failure. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | SYSTEM.UNKNOWN _ ERROR | InternalError | The request processing has failed due to some unknown error. |
| 500 | INSERT ECS DEVICE _ _ FAILED _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | -15000 | InternalError | The request processing has failed due to some unknown error. |
| 500 | ORDER.DEDUCE AC _ TIVITY INVENTORY _ _ ERROR | InternalError | The request processing has failed due to some unknown error. |
| 500 | PRICE.HSF TIMEOUT _ ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |
| 500 | Trade GetOrder ER _ _ ROR | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | SYSTEM.USE STORE _ D CARD FAILED _ _ | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -1201004 | InternalError | The request processing has failed due to some unknown error. |
| 500 | INTERNAL ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | Invalid.Image.Type | InvalidImage.OSType | The image OSType does not support this instance type. |

##### RunInstances

接口说明

## 准备工作

| DescribeInstanceTypes | 查看 |
|---|---|
| DescribeAvailableResource |  |

网络规划：您需要确保您已经有可用的安全组。更多详情，请参见专有云文档中心《云服务器ECS开发指南》 章节。创建专有网络VPC类型实例前，您需要预先在相应的阿里云地域创建VPC。

**注意事项**

单次最多能创建100台实例。 云服务器ECS 您可以指定参数 `AutoReleaseTime` 设置实例自动释放时间。 创建成功后会返回实例ID列表，您可以通过 `DescribeInstances` 查询新建实例状态。 创建实例时，默认自动启动实例，直到实例状态变成运行中（ `Running` ）。 提交创建任务后，参数不合法或者库存不足的情况下会报错，具体的报错原因请参见下文**错误码** 。

**最佳实践**

`RunInstances` 可以执行批量创建任务，为便于管理与检索，建议您为每批次启动的实例指定标签 （ `Tag.N.Key` 和 `Tag.N.Value` ），并且为主机名（ `HostName` ）和实例名称（ `InstanceName` ）添加有序后缀（ `UniqueSuffix` ）。 实例启动模板能免除您每次创建实例时都需要填入大量配置参数，您可以创建实例启动模板 （ `CreateLaunchTemplate` ）后，在 `RunInstances` 请求中指定 `LaunchTemplateId` 和 `LaunchTemplateVersion` 使用启动模板。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | RunInstances | 系统规定参数。取值： RunInstances。 |
| RegionId | String | Query | 是 | cn-qingdao-env***-d** | 实例所属的地域ID。您可以调用 DescribeRegions 查询地域ID。 |
| ImageId | String | Query | 否 | aliyun 2 1903 x64 20G _ _ _ _ _ alibase 20200324.vhd _ | 镜像ID，启动实例时选择的镜像资源。您可以通过 DescribeImages 查询您可以使用的镜像资源。如果您不指定 LaunchTemplateId 或 LaunchTemplateName 以确定启动模板， 则 ImageId 为必选参数。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| ImageFami ly | String | Query | 否 | daily-update |  | 镜像族系名称，通过设置该参数来获取当前镜像族系内最新可用的自定义镜像来创建实例。 设置了参数ImageId，则不能设置该参数。 未设置参数ImageId，但指定的 LaunchTemplateId或 LaunchTemplateName 对应的启动模板设置了 ImageId，则不能设置该参数。 未设置ImageId，且指定的LaunchTemplateId或 LaunchTemplateName 对应的启动模板未设置 ImageId，则可以设置该参数。 未设置ImageId，且未设置LaunchTemplateId、 LaunchTemplateName 参数，则可以设置该参数。 |  |  |
| InstanceTy pe | String | Query | 否 | ecs.g6.large |  | 实例的资源规格。如果您不指定 LaunchTemplateId 或 LaunchTemplateName 以确定启动模板， InstanceType 为必选参数。 产品选型：参见专有云文档中心《云服务器ECS实例规格族&实例规格简介》文档或调用 DescribeInstanceT ypes 查看目标实例规格的性能数据。 查询库存：调用 DescribeAvailable Resource 查看指定地域或者可用区内的资源供给情况。 |  |  |
|  |  |  |  |  |  |  | DescribeAvailable |  |
|  |  |  |  |  |  | Resource |  |  |

|  |  | DescribeInstanceT |  |
|---|---|---|---|
|  | ypes |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |
|---|---|---|---|---|---|---|
| SecurityGr oupId | String | Query | 否 | sg- bp15ed6xe1yxeycg7**** | 指定新创建实例所属于的安全组ID。同一个安全组内的实例之间可以互相访问，一个安全组能容纳的实例数量视安全组类型而定。 您需要注意如下事项： SecurityGroupId 决定了实例的网络类型，例如，如果设置的安全组的网络类型为专有网络 VPC，实例则为VPC类型，并同时需要指定参数 VSwitchId 。 如果您不设置 LaunchTemplateId 或 LaunchTemplateN ame 以确定实例启动模板，则安全组ID为必选参数。 将实例同时加入多个安全组时，您需要添加的参数为 SecurityGroupIds. N 。N的取值范围与实例能够加入安全组配额有关。不支持同时设置 SecurityGroupId 和 SecurityGroupIds. N 。 |  |
| VSwitchId | String | Query | 否 | vsw- bp1s5fnvk4gn2tws0**** | 虚拟交换机ID。如果您创建的是VPC类型ECS实例，必须指定虚拟交换机ID，且安全组和虚拟交换机在同一个专有网络 VPC中。 如果您设置了 VSwitchId 参数，则设置的 ZoneId 参数必须和交换机所在的可用区保持一致。您也可以不设置 ZoneId 参数，系统将自动选择指定交换机所在的可用区。 |  |

|  |  |  | LaunchTemplateId |
|---|---|---|---|
|  |  |  | 或 |

| SecurityGroupIds. |  |
|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 |  | 是否必选 | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|
| InstanceNa me | String | Query |  |  |  |  | 实例名称。长度为2~128个字符，支持Unicode中letter 分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号（:）、下划线 （ ）、半角句号（.）或者短 _ 划线（-）。 默认值为实例的 InstanceId 。 创建多台ECS实例时，您可以使用 UniqueSuffix 为这些实例设置不同的实例名称。 您也可以使用 name prefix[begin n _ _ |  |
|  |  |  |  |  |  |  |  | name prefix[begin n _ _ |
|  |  |  |  |  |  |  | umber,bits]name suffix _ |  |
|  |  |  |  |  | k8s-node-[1,4]- |  |  |  |
|  |  |  |  | 否 | alibabacloud |  |  |  |
| Descriptio n | String | Query |  | 否 | Instance Description _ |  | 实例的描述。长度为2~256 个英文或中文字符，不能以 http:// 或 https:/ / 开头。 |  |
| InternetMa xBandwidt hIn | Intege r | Query |  | 否 | 10 |  | 网络入带宽最大值，单位为 Mbit/s。取值范围： 当网络出带宽小于等于10 Mbit/s时：1~10，默认为 10。 当网络出带宽大于10 Mbit/s时： 1~ InternetMaxBandw idthOut 参数的取值， 默认为 InternetMaxBandwi dthOut 参数的取值。 |  |

|  | alibabacloud |  |
|---|---|---|

|  |  | k8s-node-0001- |  |
|---|---|---|---|
|  | alibabacloud |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

|  |  | InternetMaxBandw |  |
|---|---|---|---|
|  | idthOut |  |  |

|  |  | InternetMaxBandwi |  |
|---|---|---|---|
|  | dthOut |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 |  | 是否必选 | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|
| InternetMa xBandwidt hOut | Intege r | Query |  | 否 | 10 |  | 网络出带宽最大值，单位为 Mbit/s。取值范围： 0~100。 默认值：0。 |  |
| HostName | String | Query |  | 否 | k8s-node-[1,4]-ecshost |  | 实例主机名称。限制说明如下： 半角句号（.）和短划线 （-）不能作为首尾字符， 更不能连续使用。 Windows实例：字符长度为2~15，不支持半角句号 （.），不能全是数字。允许包含大小写英文字母、 数字和短划线（-）。 其他类型实例（Linux 等）： 字符长度为2~64，支持多个半角句号（.），点之间为一段，每段允许包含大小写英文字母、 数字和短划线（-）。 支持通过占位符 ${instance id} _ 将实例ID写入 HostName 参数。 例如： HostName=k8s- ${instance id} ， _ 并且创建的ECS实例ID 为 i- 123abc**** ，则该实例的主机名为 k8s- i-123abc**** 。 创建多台ECS实例时，您可以使用 UniqueSuffix 为这些实例设置不同的主机名称。 您也可以使用 name prefix[begin n _ _ |  |
|  |  |  |  |  |  |  |  | name prefix[begin n _ _ |
|  |  |  |  |  |  |  | umber,bits]name suffix _ |  |

|  |  | HostName=k8s- |  |
|---|---|---|---|
| shost | ${instance id} _ |  |  |

|  | i- |
|---|---|
| 123abc**** |  |

|  | k8s- |  |
|---|---|---|
| i-123abc**** |  |  |

|  |  | k8s- |
|---|---|---|
|  | node-[1,4]-ecshost |  |

|  |  | k8s-node-0001- |  |
|---|---|---|---|
|  | ecshost |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| UniqueSuff ix | Boole an | Query | 否 | true |  |  | 当创建多台实例时，是否为 HostName 和 Instan ceName 自动添加有序后缀。有序后缀从001开始递增，最大不能超过999。取值范围： true：添加。 false：不添加。 默认值：false。 当 HostName 或 Instan ceName 按照指定排序格式设置，未设置命名后缀 name suffix ，即命 _ 名格式为 name prefix[begin n _ _ umber,bits] 时， Uniq ueSuffix 不生效，名称仅按照指定顺序排序。 |  |  |  |
|  |  |  |  |  |  |  |  | name prefix[begin n _ _ |  |  |
|  |  |  |  |  |  |  | umber,bits] |  |  |  |
|  |  |  |  |  |  |  |  |  | Uniq |  |
|  |  |  |  |  |  |  | ueSuffix |  |  |  |
| Password | String | Query | 否 | EcsV587! |  |  | 实例的密码。长度为8至30个字符，必须同时包含大小写英文字母、数字和特殊符号中的三类字符。特殊符号可以是： ()`~!@#$%^&*- +=\|{} _ []:;'<>,.?/ 其中，Windows实例不能以正斜线（/）为密码首字符。 如果传入 Password 参数，建议您使用HTTPS协议发送请求，避免密码泄露。 |  |  |  |
| PasswordIn herit | Boole an | Query | 否 | false |  |  | 是否使用镜像预设的密码。取值范围： true：使用。 false：不使用。 使用该参数时， Password 参数必须为空，同时您需要确保使用的镜像已经设置了密码。 |  |  |  |
| ZoneId | String | Query | 否 | cn-qingdao-env***- test001-a |  |  | 实例所属的可用区ID，您可以调用 DescribeZones 获取可用区列表。 默认值：系统随机选择。 |  |  |  |

|  |  | HostName |
|---|---|---|
|  | ceName |  |

| Instan |  |
|---|---|

|  |  | HostName |
|---|---|---|
|  | ceName |  |

| Instan |  |
|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| SystemDis k.Size | String | Query | 否 | 40 | 系统盘大小，单位：GiB。取值范围：20~2048。 该参数的取值必须大于或者等于 max{20, ImageSize } 。 默认值： max{40, ImageSize } 。 |  |  |
| SystemDis k.Category | String | Query | 否 | cloud ssd _ | 系统盘的云盘种类。取值范围： cloud efficiency：高效 _ 云盘。 cloud ssd：SSD云盘。 _ cloud pperf：高性能云 _ 盘。 cloud sperf：普通性能云 _ 盘。 默认值：cloud efficiency。 _ 原共享SSD盘和共享高效云盘已下线。 |  |  |
| SystemDis k.DiskNam e | String | Query | 否 | cloud ssdSystem _ | 系统盘名称。长度为2~128 个字符，支持Unicode中 letter分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号（:）、下划线（ ）、半角句号（.）或者 _ 短划线（-）。 默认值：空。 |  |  |
| SystemDis k.Descripti on | String | Query | 否 | SystemDisk Description _ | 系统盘的描述。长度为 2~256个英文或中文字符， 不能以 http:// 或 https:/ / 开头。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| SystemDis k.AutoSna pshotPolic yId | String | Query | 否 | sp-bp67acfmxazb4p**** | 系统盘采用的自动快照策略 ID。 |  |  |
| IoOptimize d | String | Query | 否 | optimized | 是否为I/O优化实例。已停售的实例规格实例默认值是 none ，其他实例规格默认值是 optimized 。 取值范围： none：非I/O优化。 optimized：I/O优化。 |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| UserData | String | Query | 否 | ZWNobyBoZWxsbyBlY3M h |  | 实例自定义数据。需要以 Base64方式编码，原始数据最多为16 KB。 |  |  |  |
| KeyPairNa me | String | Query | 否 | KeyPair Name _ |  | 密钥对名称。 Windows实例，忽略该参数。默认为空。即使填写了该参数，仍旧只执行 Password 的内容。 Linux实例的密码登录方式会被初始化成禁止。 |  |  |  |
| RamRoleN ame | String | Query | 否 | RAM Name _ |  | 实例RAM角色名称。您可以使用RAM API（ ListRoles ）查询您已创建的实例RAM角色。 |  |  |  |
| Amount | Intege r | Query | 否 | 3 |  | 指定创建ECS实例的数量。取值范围：1~100。 默认值：1。 |  |  |  |
| MinAmoun t | Intege r | Query | 否 | 2 |  | 指定ECS实例最小创建数量。 取值范围：1~100。 当ECS库存数量小于最小创建数量，会创建失败。 当ECS 库存数量大于等于最小创建数量，按照库存数量创建。 |  |  |  |
| AutoReleas eTime | String | Query | 否 | 2018-01-01T12:05:00Z |  | 自动释放时间。按照 ISO8601标准表示，使用 UTC+0时间。格式为： yyyy-MM- ddTHH:mm:ssZ 。 如果秒（ ss ）取值不是 00 ，则自动取为当前分钟（ mm ）开始时。 最短释放时间为当前时间半小时之后。 最长释放时间不能超过当前时间三年。 |  |  |  |
|  |  |  |  |  |  |  | yyyy-MM- |  |  |
|  |  |  |  |  |  | ddTHH:mm:ssZ |  |  |  |
|  |  |  |  |  |  |  |  | ss |  |
| SecurityEn hancement Strategy | String | Query | 否 | Active |  | 是否开启安全加固。取值范围： Active：启用安全加固， 只对公共镜像生效。 Deactive：不启用安全加固，对所有镜像类型生效。 |  |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 |  | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken 只支持ASCII字符，且不能超过64 个字符。更多信息，请参见专有云文档中心《云服务器ECS 开发指南》文档的如何保证幂等性章节。 |  |  |
| HpcCluster Id | String | Query | 否 | hpc-bp67acfmxazb4p**** |  | 实例所属的EHPC集群ID。 |  |  |
| DryRun | Boole an | Query | 否 | false |  | 是否只预检此次请求。取值范围： true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数、请求格式、业务限制和ECS库存。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false：发送正常请求，通过检查后直接创建实例。 默认值：false。 |  |  |
| Dedicated HostId | String | Query | 否 | dh-bp67acfmxazb4p**** |  | 专有宿主机ID。您可以通过 DescribeDedicatedHo sts 查询专有宿主机ID列表。 |  |  |
| LaunchTe mplateId | String | Query | 否 | lt-bp1apo0bbbkuy0rj**** |  | 启动模板ID。更多信息，请调用 DescribeLaunchTempl ates 获取。 使用启动模板创建实例时，您必须指定 LaunchTemplateId 或 LaunchTemplateName 参数来确定启动模板。 |  |  |
|  |  |  |  |  |  |  | DescribeLaunchTempl |  |
|  |  |  |  |  |  | ates |  |  |
| LaunchTe mplateNa me | String | Query | 否 | LaunchTemplate Name _ |  | 启动模板名称。 使用启动模板创建实例时，您必须指定 LaunchTemplateId 或 LaunchTemplateName 参数来确定启动模板。 |  |  |

|  |  | DescribeDedicatedHo |  |
|---|---|---|---|
| 67acfmxazb4p**** | sts |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| LaunchTe mplateVer sion | Long | Query | 否 | 3 | 启动模板版本。 如果您指定了 LaunchTemplateId 或 LaunchTemplateName 参数而不指定启动模板版本号，则采用默认版本。 |
| Deployme ntSetId | String | Query | 否 | ds-bp1brhwhoqinyjd6**** | 部署集ID。 |
| PrivateIpA ddress | String | Query | 否 | 10.1.**.** | 实例私网IP地址。专有网络 VPC类型ECS实例设置私网IP 地址时，必须从虚拟交换机 （ VSwitchId ）的空闲网段中选择。 设置 PrivateIpAddress 后： 如果 Amount 参数取值为1，则表示为创建的一台 ECS实例分配私网IP地址。 如果 Amount 参数取值大于1，则表示在批量创建 ECS实例时，以指定的私网 IP地址为起始地址，依次为多台ECS实例分配连续的私网IP地址，但需要注意，此时不支持再为实例绑定辅助网卡（即不支持再设置 NetworkInterface. N.* 这类参数）。 |
| CreditSpec ification | String | Query | 否 | Standard | 修改突发性能实例的运行模式。取值范围： Standard：标准模式。 Unlimited：无性能约束模式。 默认值：无。 |
| Ipv6Addres sCount | Intege r | Query | 否 | 1 | 为主网卡指定随机生成的IPv6 地址数量。取值范围： 1~10。 您不能同时设置 Ipv6Address.N 和 I pv6AddressCount 。 |

|  |  | NetworkInterface. |  |
|---|---|---|---|
|  | N.* |  |  |

|  |  | Ipv6Address.N |
|---|---|---|
|  | pv6AddressCount |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  |  | 说明 |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NetworkInt erfaceQue ueNumber | Intege r | Query | 否 | 8 |  |  | 主网卡队列数。 不能超过实例规格允许的单块网卡最大队列数。 实例的所有网卡累加队列数不能超过实例规格允许的队列数总配额。实例规格的单块网卡最大队列数和总配额可以通过 DescribeInstanceT ypes 接口查询 MaximumQueueNumbe rPerEni 、 TotalEni QueueQuantity 字段。 |  |  |  |  |  |
|  |  |  |  |  |  |  |  | DescribeInstanceT |  |  |  |  |
|  |  |  |  |  |  |  | ypes |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 接口查 |  |  |  |
|  |  |  |  |  |  |  | 询 |  |  |  |  |  |
|  |  |  |  |  |  |  | rPerEni |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 、 | TotalEni |  |
| DeletionPr otection | Boole an | Query | 否 | false |  |  | 实例释放保护属性，指定是否支持通过控制台或 API（ DeleteInstance ）释放实例。取值范围： true：开启实例释放保护。 false：关闭实例释放保护。 默认值：false。 您需要注意，该属性只能限制手动释放操作，对系统释放操作不生效。 |  |  |  |  |  |
| Affinity | String | Query | 否 | default |  |  | 专有宿主机实例是否与专有宿主机关联。取值范围： default：实例不与专有宿主机关联。 host：实例与专有宿主机关联。 默认值：default。 |  |  |  |  |  |
| Tenancy | String | Query | 否 | default |  |  | 是否在专有宿主机上创建实例。取值范围： default：创建非专有宿主机实例。 host：创建专有宿主机实例。若您不指定 DedicatedHostId ，则由阿里云自动选择专有宿主机放置实例。 默认值：default。 |  |  |  |  |  |
| StorageSet Id | String | Query | 否 | ss-bp67acfmxazb4p**** |  |  | 存储集ID。您可以调用 StorageSetPartition Number 查询存储集ID。 |  |  |  |  |  |

|  |  | StorageSetPartition |  |
|---|---|---|---|
|  | Number |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| StorageSet PartitionNu mber | Intege r | Query | 否 | 2 |  |  | 存储集中的最大分区数量。取值范围：大于等于2。在指定了 StorageSetId 时，该参数为必填。 |  |  |  |
| CpuOption s.Core | Intege r | Query | 否 | 2 |  |  | CPU核心数。该参数不支持自定义设置，只能采用默认值。 |  |  |  |
| CpuOption s.ThreadsP erCore | Intege r | Query | 否 | 2 |  |  | CPU线程数。ECS实例的 vCPU数 = CpuOptions.Core 取值 * CpuOptions.ThreadsPe rCore 取值。 |  |  |  |
|  |  |  |  |  |  |  |  | CpuOptions.ThreadsPe |  |  |
|  |  |  |  |  |  |  | rCore |  |  |  |
|  |  |  |  |  |  |  |  |  | 取值。 |  |
|  |  |  |  |  |  |  | erCore=1 |  |  |  |
| CpuOption s.Numa | String | Query | 否 | 1 |  |  | CPU Numa节点数。 |  |  |  |
| Scheduler Options.De dicatedHos tClusterId | String | Query | 否 | dc- bp12wlf6am0vz9v2**** |  |  | 指定ECS实例所属的专有宿主机集群，系统会自动选择该专有宿主机集群中的一台专有宿主机部署ECS实例。 仅在 Tenancy 设置为 host 时生效。 在您同时指定了专有宿主机 （ DedicatedHostId ） 和专有宿主机集群 （ SchedulerOptions.De dicatedHostClusterId ）时： 如果专有宿主机属于专有宿主机集群，则优先将ECS 实例部署在指定的专有宿主机上。 如果专有宿主机不属于专有宿主机集群，则ECS实例创建失败。 您可以通过 DescribeDedicatedHo stClusters 查询专有宿主机集群ID列表。 |  |  |  |

|  | Tenancy |
|---|---|
| host |  |

|  |  | SchedulerOptions.De |
|---|---|---|
|  | dicatedHostClusterId |  |

|  |  | DescribeDedicatedHo |  |
|---|---|---|---|
|  | stClusters |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|
| SecurityGr oupIds | Repea tList | Query | 否 |  | sg- bp15ed6xe1yxeycg7**** |  | 将实例同时加入多个安全组。 参数格式为 SecurityGroupIds.N ，N的取值范围与实例能够加入安全组配额有关。 不支持同时设置 SecurityGroupId 和 SecurityGroupIds.N 。 |  |  |
| HostName s | Repea tList | Query | 否 |  | ecs-host-01 |  | 创建多台ECS实例时，为每台实例指定不同的主机名。参数格式为 HostNames.N 。 Hos tNames.N 限制说明如下： N的个数需要和Amount参数值保持一致。例如，Amount=2时，通过该参数指定主机名的格式为HostNames.1=test1 和 HostNames.2=test2。 不支持同时设置 HostName 参数和 HostNames.N 参数。 您可以使用 UniqueSuffix 为这些实例设置不同的主机名称。您也可以使用 name prefix[begin _ |  |  |
|  |  |  |  |  |  |  |  | name prefix[begin _ |  |
|  |  |  |  |  |  | 1 | number,bits]name su _ _ |  |  |
|  |  |  |  |  |  |  | ffix |  |  |

|  |  | HostNames.N |
|---|---|---|
|  | tNames.N |  |

| Hos |  |
|---|---|

|  | ecshost |  |
|---|---|---|

|  |  | k8s-node-0001- |  |
|---|---|---|---|
|  | ecshost |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| DataDisk | Repea tList | Query | 否 | - |  | 实例数据盘信息。 |  |  |
| - AutoSnaps hotPolicyId | String |  | 否 | sp-bp67acfmxazb4p**** |  | 数据盘N采用的自动快照策略 ID。参数格式为 DataDisk.N.AutoSnap shotPolicyId 。 |  |  |
|  |  |  |  |  |  |  | DataDisk.N.AutoSnap |  |
|  |  |  |  |  |  | shotPolicyId |  |  |
| -Encrypted | String |  | 否 | false |  | 数据盘N是否加密。参数格式为 DataDisk.N.Encrypte d 。取值范围： true：加密。 false：不加密。 默认值：false。 |  |  |
| - Descriptio n | String |  | 否 | Network Description _ |  | 弹性网卡的描述，参数格式为 NetworkInterface.N. Description ，N的取值为1。长度为2~256个英文或中文字符，不能以 http:// 或 https:/ / 开头。 |  |  |
| - SnapshotId | String |  | 否 | s-bp17441ohwka0yuh**** |  | 创建数据盘N使用的快照。参数格式为 DataDisk.N.Snapshot Id ，N的取值范围为 1~16。 指定参数 DataDisk.N.Snapshot Id 后，参数 DataDisk.N.Size 会被忽略，实际创建的云盘大小为指定的快照的大小。 |  |  |

|  |  | DataDisk.N.Encrypte |  |
|---|---|---|---|
|  | d |  |  |

|  |  | NetworkInterface.N. |  |
|---|---|---|---|
|  | Description |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

|  |  | DataDisk.N.Snapshot |  |
|---|---|---|---|
|  | Id |  |  |

|  |  | DataDisk.N.Snapshot |  |
|---|---|---|---|
|  | Id |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| -Device | String |  | 否 | /dev/xvdb |  | 数据盘的挂载点。参数格式为 DataDisk.N.Device ，挂载的数据盘数量不同，挂载点的命名不同： 1~25块数据盘： /dev/xvd[b-z] 大于25块数据盘： /dev/xvd[aa- zz] ，例如第26块数据盘会被命名为 /dev/xvdaa ，第 27块数据盘为 /dev/xvdab ，以此类推。 该参数仅用于全镜像（整机镜像）场景，使用普通镜像时， 该参数无意义。您可以通过将此参数设置为全镜像中数据盘对应的挂载点，并修改对应的 DataDisk.N.Size 和 DataDisk.N.Category 参数，达到修改全镜像中数据盘磁盘种类和大小的目的。 使用说明如下： DataDisk.N.Device 参数取值必须通过如下方式获取： 调用 DescribeImages 接口，然后查看接口返回的 DiskDeviceMapping s 列表信息， 当 Type 参数值为 data 时，对应的 Device 参数值即为 DataDisk.N.Device 参数取值。 DataDisk.N.Size 参数取值必须大于或等于调用 DescribeImages 接口返回的 Size 参数值。 |  |  |
|  |  |  |  |  |  |  | DiskDeviceMapping |  |
|  |  |  |  |  |  | s |  |  |
|  |  |  |  |  |  | 当为的为 |  |  |

|  |  | /dev/xvd[aa- |
|---|---|---|
|  | zz] |  |

|  |  | DataDisk.N.Category |
|---|---|---|
| xvdb |  |  |

|  |  | DataDisk.N.Device |
|---|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -Size | Intege r |  | 否 | 2000 | 第N个数据盘的容量大小。参数格式为 DataDisk.N.Size ， N的取值范围为1~16，单位为GiB。取值范围： cloud efficiency： _ 20~32768。 cloud ssd： _ 20~32768。 cloud pperf： _ 20~131072。 cloud sperf： _ 20~32768。 该参数的取值必须大于等于参数 SnapshotId 指定的快照的大小。 当数据盘的类型选择为高效云盘（cloud efficiency）或者 _ SSD盘（cloud ssd）时，如 _ 果填写的容量超过2 TB，注意按照以下EBS集群的机器数量与推荐的云盘最大建议值 （机器数量：云盘最大值）进行填写。 6台：2 TB 12台：4 TB 15台：5 TB 24台：8 TB 云盘最大建议值的计算公式为：云盘最大大小S = N/3， 其中N为相应EBS集群的机器数量，结果向下取整。例如： 如果EBS集群的机器数量为6 台，则建议创建的云盘容量不超过2 TB。 |
| -DiskName | String |  | 否 | cloud ssdData _ | 数据盘名称，参数格式为 DataDisk.N.DiskName 。长长度为2~128个字符，支持Unicode中letter分类下的字符（其中包括英文、 中文和数字等）。可以包含半角冒号（:）、下划线（ ）、 _ 半角句号（.）或者短划线 （-）。 默认值：空。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -Category | String |  | 否 | cloud ssd _ | 数据盘N的云盘种类，参数格式为 DataDisk.N.Category 。取值范围： cloud efficiency：高效 _ 云盘。 cloud ssd：SSD云盘。 _ cloud pperf：高性能云 _ 盘。 cloud sperf：普通性能云 _ 盘。 默认值：cloud efficiency。 _ 原共享SSD盘和共享高效云盘已下线。 |
| - DeleteWith Instance | Boole an |  | 否 | rue | 数据盘是否随实例释放，参数格式为 DataDisk.N.DeleteWi thInstance 。取值范围： true：数据盘随实例释放。 false：数据盘不随实例释放。 默认值：true。 |
| -KMSKeyId | String |  | 否 | 0e478b7a-4262-4802- b8cb-00d3fb40**** | 数据盘对应的KMS密钥ID， 参数格式为 DataDisk.N.KMSKeyId 。 |
| NetworkInt erface | Repea tList | Query | 否 | - | 弹性网卡信息。 |
| -VSwitchId | String |  | 否 | vsw-bp67acfmxazb4p**** | 弹性网卡所属的虚拟交换机 ID，参数格式为 NetworkInterface.N. VSwitchId ，N的取值为 1。 |
| - NetworkInt erfaceNam e | String |  | 否 | Network Name _ | 弹性网卡名称，参数格式为 NetworkInterface.N. NetworkInterfaceName ，N的取值为1。长度为 2~128个字符，支持 Unicode中letter分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号 （:）、下划线（ ）、半角句 _ 号（.）或者短划线（-）。 |

|  |  | DataDisk.N.DeleteWi |  |
|---|---|---|---|
|  | thInstance |  |  |

|  |  | NetworkInterface.N. |  |
|---|---|---|---|
|  | VSwitchId |  |  |

|  |  | NetworkInterface.N. |
|---|---|---|
|  | NetworkInterfaceName |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| - Descriptio n | String |  | 否 | Network Description _ | 弹性网卡的描述，参数格式为 NetworkInterface.N. Description ，N的取值为1。长度为2~256个英文或中文字符，不能以 http:// 或 https:/ / 开头。 |
| - SecurityGr oupId | String |  | 否 | sg-bp67acfmxazb4p**** | 弹性网卡所属的安全组ID，参数格式为 NetworkInterface.N. SecurityGroupId ，N的取值为1。 |
| - PrimaryIpA ddress | String |  | 否 | 172.16.**.** | 添加一张弹性网卡并设置主IP 地址，参数格式为 NetworkInterface.N. PrimaryIpAddress 。 您需要注意，创建ECS实例时，您最多能添加一张辅助网卡。实例创建成功后，您可以调用 CreateNetworkInterf ace 和 AttachNetworkI nterface 添加更多的辅助网卡。 默认值：从网卡所属的交换机网段中随机选择一个IP地址。 |
| - QueueNum ber | Intege r |  | 否 | 8 | 弹性网卡队列数，参数格式为 NetworkInterface.N. QueueNumber 。 N的取值为1，表示仅支持设置1个主网卡。 不能超过实例规格允许的单块网卡最大队列数。 实例的所有网卡累加队列数不能超过实例规格允许的队列数总配额。实例规格的单块网卡最大队列数和总配额可以通过 DescribeInstanceT ypes 接口查询 MaximumQueueNumbe rPerEni 、 TotalEni QueueQuantity 字段。 |

|  |  | NetworkInterface.N. |  |
|---|---|---|---|
|  | Description |  |  |

| https:/ |  |
|---|---|

|  | / |  |
|---|---|---|

|  |  | NetworkInterface.N. |
|---|---|---|
|  | SecurityGroupId |  |

|  |  | NetworkInterface.N. |
|---|---|---|
|  | PrimaryIpAddress |  |

|  |  |  | CreateNetworkInterf |  |  |  |
|---|---|---|---|---|---|---|
|  |  | ace |  |  |  |  |
|  |  |  |  | 和 | AttachNetworkI |  |

|  |  | NetworkInterface.N. |  |
|---|---|---|---|
|  | QueueNumber |  |  |

|  |  |  | DescribeInstanceT |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | ypes |  |  |  |  |  |
|  |  |  |  | 接口查 |  |  |  |
|  |  | 询 |  |  |  |  |  |
|  |  | rPerEni |  |  |  |  |  |
|  |  |  |  |  | 、 | TotalEni |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| - SecurityGr oupIds | Repea tList |  | 否 | sg- bp15ed6xe1yxeycg7**** | 弹性网卡所属的一个或多个安全组ID，参数格式为 NetworkInterface.N. SecurityGroupIds.N 。 第一个N的取值为1，表示仅支持设置1个主网卡。 第二个N表示可以指定一个或多个安全组ID。N的取值范围与实例能够加入安全组配额有关。 |
| - InstanceTy pe | String |  | 否 | Secondary | 弹性网卡类型，参数格式为 NetworkInterface.N. InstanceType ，N的取值范围为1~2。 设置1个弹性网卡时，支持设置1个主网卡或1个辅助网卡；设置2个弹性网卡时，仅支持同时设置1个主网卡和1 个辅助网卡。 取值范围： Primary：主网卡。 Secondary：辅助网卡。 默认值：Secondary。 |
| - Ipv6Addres sCount | Long |  | 否 | 1 | 为主网卡指定随机生成的IPv6 地址数量，参数格式为 NetworkInterface.N. Ipv6AddressCount 。N 的取值范围：1~10。 您需要注意： NetworkInterface.N. InstanceType 取值为 Primary 时，设置该参数才会生效。如果 NetworkInterface. N.InstanceType 取值为 Secondary 或空值，则不能设置该参数。 设置该参数后，您不能再设置 Ipv6AddressCount 、 Ipv6Address.N 或 NetworkInterface. N.Ipv6Address.N 。 |

|  |  | NetworkInterface.N. |
|---|---|---|
|  | SecurityGroupIds.N |  |

|  |  | NetworkInterface.N. |  |
|---|---|---|---|
|  | InstanceType |  |  |

|  |  | NetworkInterface.N. |
|---|---|---|
|  | Ipv6AddressCount |  |

|  | InstanceType |
|---|---|

|  |  | NetworkInterface. |  |
|---|---|---|---|
|  | N.InstanceType |  |  |

|  |  |  | Ipv6AddressCount |  |
|---|---|---|---|---|
|  |  |  | 、 | Ipv6Address.N |
|  |  |  | NetworkInterface. |  |
|  |  | 或 |  |  |
|  |  | N.Ipv6Address.N |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| - Ipv6Addres s | Repea tList |  | 否 | 2001:db8:1234:1a00::*** | 为主网卡指定一个或多个IPv6 地址，参数格式为 NetworkInterface.N. Ipv6Address.N 。支持设置最多10个IPv6地址，即第二个N的取值范围：1~10。 取值示例： Ipv6Address.1=200 1:db8:1234:1a00::*** 您需要注意： NetworkInterface.N. InstanceType 取值为 Primary 时，设置该参数才会生效。如果 NetworkInterface. N.InstanceType 取值为 Secondary 或空值，则不能设置该参数。 设置该参数后， Amount 取值只能为1，且不能再设置 Ipv6AddressCount 、 Ipv6Address.N 或 NetworkInterface. N.Ipv6AddressCount 。 |
| Tag | Repea tList | Query | 否 | - | 实例、云盘和主网卡的标签信息。 |
| -Key | String |  | 否 | TestKey | 实例、云盘和主网卡的标签键。参数格式为 Tag.N.Key ，N的取值范围：1~20。 一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 或 https:/ / 。 |

|  |  | NetworkInterface.N. |  |
|---|---|---|---|
|  | Ipv6Address.N |  |  |

|  |  | Ipv6Address.1=200 |
|---|---|---|
|  | 1:db8:1234:1a00::*** |  |

|  |  | NetworkInterface.N. |  |
|---|---|---|---|
|  | InstanceType |  |  |

|  |  | NetworkInterface. |  |
|---|---|---|---|
|  | N.InstanceType |  |  |

|  |  |  | Ipv6AddressCount |  |
|---|---|---|---|---|
|  |  |  | 、 | Ipv6Address.N |
|  |  |  | NetworkInterface. |  |
|  |  | 或 |  |  |
|  |  | N.Ipv6AddressCount |  |  |

| https:/ |  |
|---|---|

|  | / |
|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -Value | String |  | 否 | TestValue | 实例、云盘和主网卡的标签值。参数格式为 Tag.N.Value ，N的取值范围：1~20。 一旦传入该值，可以为空字符串。最多支持128个字符，不能包含 http:// 或 https:/ / 。 |
| Ipv6Addres s | Repea tList | Query | 否 | 2001:db8:1234:1a00::*** | 为主网卡指定一个或多个IPv6 地址，参数格式为 Ipv6Address.N 。支持设置最多10个IPv6地址， 即N的取值范围：1~10。 取值示例： Ipv6Address.1=200 1:db8:1234:1a00::*** 。 您需要注意： 设置该参数后， Amount 取值只能为1，且不能再设置 Ipv6AddressCount 、 Ipv6Address.N 或 NetworkInterface. N.Ipv6AddressCount 。 如果 NetworkInterface. N.InstanceType 取值为 Primary ，则不能设置 Ipv6Addresses.N 或 Ipv6AddressCount ，而是需要设置 NetworkInterface. N.Ipv6Addresses.N 或 NetworkInterface. N.Ipv6AddressCount 。 |

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

|  |  | Ipv6Address.1=200 |
|---|---|---|
|  | 1:db8:1234:1a00::*** |  |

|  |  |  | Ipv6AddressCount |  |
|---|---|---|---|---|
|  |  |  | 、 | Ipv6Address.N |
|  |  |  | NetworkInterface. |  |
|  |  | 或 |  |  |
|  |  | N.Ipv6AddressCount |  |  |

|  |  | NetworkInterface. |  |
|---|---|---|---|
|  | N.InstanceType |  |  |

|  |  |  | NetworkInterface. |  |
|---|---|---|---|---|
|  |  | 置 |  |  |
|  |  | N.Ipv6Addresses.N |  |  |
|  |  | 或 |  |  |
|  |  | N.Ipv6AddressCount |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| InstanceIdSets | List | ["i- bp67acfmxazb4pd2 ****","i- bp1i43l28m7u48p1* ***","i- bp12yqg7jdyxl11f** **"] | 实例ID（ InstanceIdSet ）列表。 |

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE***** | 请求ID。 |
| OrderId | String | 1234567890 | 该参数暂未支持。 |
| TradePrice | Float | 0.165 | 该参数暂未支持。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env***-d** &ImageId=aliyun_2_1903_x64_20G_alibase_20200324.vhd &InstanceType=ecs.g6.large &SecurityGroupId=sg-bp67acfmxazb4p**** &VSwitchId=vsw-bp1s5fnvk4gn2tws0**** &SystemDisk.AutoSnapshotPolicyId=sp-bp67acfmxazb4p**** &Amount=3**
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{ "InstanceIdSets":{ "InstanceIdSet":[ "i-bp67acfmxazb4pd2****", "i-bp1i43l28m7u48p1****", "i-bp12yqg7jdyxl11f****"
```

]

```json
}, "RequestId":"04F0F334-1335-436C-A1D7-6C044FE*****" }
```

`XML` 格式

```xml
<InstanceIdSets> <InstanceIdSet>i-bp67acfmxazb4pd2****</InstanceIdSet> <InstanceIdSet>i-bp1i43l28m7u48p1****</InstanceIdSet> <InstanceIdSet>i-bp12yqg7jdyxl11f****</InstanceIdSet> </InstanceIdSets> <RequestId>04F0F334-1335-436C-A1D7-6C044FE*****</RequestId>
```

**错误码**

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IMAGE NOT SUPPO _ _ RT LOG AS NON R _ _ _ _ OOT | LoginAsNonRoot.ImageNotSupp ort | The specified image does not support login as non-root. |
| 400 | NOT SUPPORT JUMB _ _ O FRAME _ | InvalidParam.NotSupportJumboF rame | Not support jumbo frame. |
| 400 | ACCOUNT MONEY V _ _ ALIDATE ERROR _ | InsufficientBalance.AgentCredit | Insufficient agent credit. Please contact your agent. |
| 400 | ELASIC COMMON R _ _ ESOUCE QUOTA EX _ _ CEEDED | QuotaExceed.DiskCapacity | The used capacity of disk type has exceeded the quota in the zone, %s. |
| 400 | ECS ON HOST NOT _ _ _ SUPPORT _ | InvalidPeriod.ExceededDedicate dHost | Instance expired date can't exceed dedicated host expired date. |
| 400 | InvalidParam.Secon daryNetworkInterfac e | InvalidParam.SecondaryNetwork Interface | When min amount greater than 1 and the PrivateIpAddress or Primary NetworkInterface is specified,the Secondary NetworkInterface IP parameter cannot be specified. |
| 400 | InvalidPrimaryIpAdd ress.SizeInvalid | InvalidPrimaryIpAddress.SizeInv alid | The NetworkInterface PrimaryIpAddress is used to create only one instance. |
| 400 | InvalidDedicatedBlo ckStorageClusterId. CapacityNotEnough | InvalidStorageClusterId.Capacity NotEnough | The remaining capacity of the current dedicated storage cluster is less than the size of disk. |
| 400 | InvalidDedicatedBlo ckStorageClusterId. StatusNotSupport | InvalidStorageClusterId.StatusN otSupport | The current status of the dedicated storage cluster cannot create a cloud disk yet. |
| 400 | Abs.InvalidDedicate dBlockStorageCluste rId.ZoneIdEmpty | InvalidStorageClusterId.ZoneIdE mpty | The specified param ZoneId cannot be empty when StorageClusterId given. |
| 400 | InvalidDedicatedBlo ckStorageClusterId. PerformanceLevelN otMatch | InvalidStorageClusterId.Perform anceLevelNotMatch | The current dedicated storage cluster cannot create this performance level of disk. |
| 400 | InvalidDedicatedBlo ckStorageClusterId. CategoryNotMatch | InvalidStorageClusterId.Categor yNotMatch | The current dedicated storage cluster cannot create this category of disk. |
| 400 | Abs.InvalidDedicate dBlockStorageCluste rId.DiskSizeEmpty | InvalidStorageClusterId.DiskSize Empty | The specified param DiskSize cannot be empty when StorageClusterId given. |
| 400 | DEDICATED HOST T _ _ YPE IS ILLEGAL _ _ | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorize. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084424 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |

|  | 开发指南·API参 | 考 |  | 云服务器EC | S |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084573 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000086416 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084873 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085149 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085202 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00458642 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00356432 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00356653 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357727 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357790 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357913 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357948 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 403 | INSTANCE TYPE NO _ _ T EXIST _ | InvalidInstanceType.ValueNotSu pported | The specified InstanceType beyond the permitted range. |
| 403 | InvalidDescription.M alformed | InvalidDescription.Malformed | Specified parameter Description is not valid. |
| 400 | Invalid.Bandwidth.P ayType | InvalidInternetChargeType.Value NotSupported | %s |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000092309 | InvalidParameter | The specified parameter "InternetMaxBandwidthOut" is not valid. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParams.Hostn ame | InvalidHostName.Malformed | The specified parameter "HostName" is not valid. |
| 400 | PASSWORD ILLEGAL _ | InvalidPassword.Malformed | The specified parameter "Password" is not valid. |
| 400 | Abs.InvalidPassword .Malformed | InvalidPassword.Malformed | The specified parameter "Password" is not valid. |
| 400 | Abs.InvalidPassword .Mismatch | InvalidPasswordParam.Mismatch | The input password should be null when passwdInherit is true. |
| 400 | Invalid.SysDisk.Cate gory | InvalidSystemDiskCategory.Valu eNotSupported | %s |
| 400 | Abs.InvalidDiskNam e.Malformed | InvalidDiskName.Malformed | The specified parameter "SyatemDisk.DiskName or DataDisk.n.DiskName" is not valid. |
| 400 | Abs.InvalidDiskDesc ription.Malformed | InvalidDiskDescription.Malforme d | The specified parameter "SyatemDisk.DiskDescription or DataDisk.n.Description" is not valid. |
| 400 | Invalid.DataDisk.Siz e | InvalidDataDiskSize.ValueNotSu pported | %s |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179244 | InvalidDataDiskSize.ValueNotSu pported | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. |
| 400 | Invalid.DataDisk.Cat egory | InvalidDataDiskCategory.ValueN otSupported | %s |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084440 | InvalidDataDiskCategory.ValueN otSupported | The specified parameter "DataDisk.n.Category" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199823 | InvalidDataDiskCategory.ValueN otSupported | The specified parameter "DataDisk.n.Category" is not valid. |
| 400 | DISK MOUNT POINT _ _ ILLEGAL _ | InvalidDataDevice.Malformed | The specified parameter "DataDisk.n.Device" is not valid. |
| 400 | -700 | InvalidNodeControllerId.Malform ed | The specified parameter "NodeControllerId" is not valid. |
| 400 | -700 | InvalidNodeControllerId.Malform ed | The specified parameter "NodeControllerId" is not valid. |
| 400 | Abs.InvalidInnerIpAd dress.Malformed | InvalidInnerIpAddress.Malformed | The specified parameter InnerIpAddress is not valid. |
| 400 | -226 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -5003 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -5005 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -498 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -221 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -410 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | -226 | InvalidInnerIpAddress.Unusable | The specified InnerIpAddress is already used or not found in usable ip range. |
| 400 | PARAMETER CONFLI _ CT | InvalidParameter.Conflict | %s |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 707398 | InvalidParameter.Conflict | The specified image does not support the specified instance type. |
| 400 | ImageNotSupportCl oudInit | ImageNotSupportCloudInit | The specified image does not support cloud-init. |
| 400 | SNAPSHOT AT BEF _ _ ORE ASSIGN DATE _ _ | InvalidSnapshotId.BasedSnapsh otTooOld | The specified snapshot is created before 2013-07-15. |
| 400 | ECS BIZ QUOTA US _ _ _ ER | QuotaExceed.AfterpayInstance | Living afterpay instances quota exceeded. |
| 400 | NICKNAME ILLEGAL _ | InvalidInstanceName.Malformed | The specified parameter "InstanceName" is not valid. |
| 400 | NICKNAME ILLEGAL _ | InvalidInstanceName.Malformed | The specified parameter "InstanceName" is not valid. |
| 400 | Abs.InvalidInstance Name.CustomMalfor med | InvalidInstanceName.CustomMal formed | Customized section of instance or host name is invalid, please use valid format: [], [,], [m,], [,n], [m,n]. |
| 400 | DESCRIPTION ILLEG _ AL | InvalidDescription.Malformed | The specified parameter "Description" is not valid. |
| 400 | Abs.InvalidDiskNam e.Malformed | InvalidDiskName.Malformed | The specified parameter "SyatemDisk.DiskName or DataDisk.n.DiskName" is not valid. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidDiskDesc ription.Malformed | InvalidDiskDescription.Malforme d | The specified parameter "SyatemDisk.DiskDescription or DataDisk.n.Description" is not valid. |
| 400 | ZONE NOT IN AVAI _ _ _ LABLE IZ _ | InvalidParameter.Conflict | The speicified region and cluster do not match. |
| 400 | IZ IS EMPTY _ _ | InvalidParameter.Mismatch | Specified virtual switch is not in the specified zone. |
| 400 | VPC INSTANCE NOT _ _ NEED INTERNET C _ _ _ HARGETYPE | InvalidNetworkType.Mismatch | Specified parameter "InternetChargeType" conflict with instance network type. |
| 400 | VPC INSTANCE NOT _ _ NEED BANDWIDTH _ _ | InvalidNetworkType.Mismatch | Specified parameter "InternetMaxBandwidthIn" or "InternetMaxBandwidthOut" conflict with instance network type. |
| 400 | VPC INSTANCE NOT _ _ NEED INTERNET C _ _ _ HARGETYPE | InvalidNetworkType.Mismatch | Specified parameter "InternetChargeType" conflict with instance network type. |
| 400 | PRIVATE IP INVALID _ _ | InvalidPrivateIpAddress | Specified private IP address is not in the CIDR block of virtual switch. |
| 400 | Abs.InvalidPrivateIp Address.Malformed | InvalidPrivateIpAddress.Malform ed | The specified parameter PrivateIpAddress is not valid. |
| 403 | InvalidVSwitchId.IpN otEnough | QuotaExceeded.PrivateIpAddres s | %s |
| 400 | QUOTA FULL _ | QuotaExceeded | Living instances quota exceeded in this VPC. |
| 400 | VPC SWITCH STATU _ _ S ERROR _ | IncorrectVSwitchStatus | The current status of vSwitch does not support this operation. |
| 400 | IZ IS EMPTY _ _ | InvalidParameter.Mismatch | Specified virtual switch is not in the specified zone. |
| 400 | ZONE NO RESOURC _ _ E SUPPORT _ | ResourceNotAvailable | Resource you requested is not available in this region or zone. |
| 400 | Abs.MissingParamet er.InstanceType | MissingParameter | The input parameter InstanceType that is mandatory for processing this request is not supplied. |
| 400 | PASSWORD ILLEGAL _ | InvalidPassword.Malformed | The specified parameter "Password" is not valid. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199826 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidDiskSize. ValueNotSupported | InvalidDataDiskSize.ValueNotSu pported | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. |
| 400 | Abs.MissingParamte r.Period | MissingParamter | The specified parameter "Period" is not null. |
| 400 | ORDER.PERIOD INV _ ALID | InvalidPeriod | The specified period is not valid. |
| 400 | ORDER.PERIOD INV _ ALID | InvalidPeriod | The specified period is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085155 | InvalidDataDiskCategory.ValueN otSupported | The specified parameter " DataDisk.n.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085127 | InvalidDataDiskCategory.ValueN otSupported | The specified parameter " DataDisk.n.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085156 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084451 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000084502 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199822 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00000085137 | InvalidSystemDiskCategory.Valu eNotSupported | The specified parameter " SystemDisk.Category " is not valid. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199839 | InstanceDiskCategoryLimitExcee d | The total size of specified disk category in an instance exceeds. |
| 400 | ECS GET INSTANCE _ _ TYPE FAIL _ _ | InvalidInstanceType.ValueNotSu pported | The specified InstanceType beyond the permitted range. |
| 400 | ECS NO INSTANCE _ _ _ TYPE MATCH _ | InvalidInstanceType.ValueNotSu pported | The specified InstanceType beyond the permitted range. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00358157 | InvalidInstanceType.ValueNotSu pported | InternetMaxBandwidthOut should be set. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00357734 | InvalidInstanceType.ValueNotSu pported | The specified InstanceType beyond the permitted range. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidClientTok en.Malformed | InvalidClientToken.ValueNotSup ported | The ClientToken provided is invalid. |
| 400 | Abs.IoOptimized.Val ueNotSupported | InvalidIoOptimize.ValueNotSupp orted | The specified IoOptimize is not valid. |
| 404 | InvalidSecurityGrou pId.NotFound | InvalidSecurityGroupId.NotFoun d | %s |
| 400 | HOSTNAME ILLEGAL _ | InvalidHostName.Malformed | The specified parameter HostName is not valid. |
| 400 | Abs.Hostname.Malfo rmed | InvalidHostName.Malformed | The specified parameter HostName is not valid. |
| 400 | Abs.InvalidMaxBand widthOut.Malformed | InvalidInternetMaxBandwidthOut .Malformed | The specified parameter internetMaxBandwidthOut is not valid. |
| 400 | Abs.InvalidMaxBand widthIn.Malformed | InvalidInternetMaxBandwidthIn. Malformed | The specified parameter internetMaxBandwidthIn is not valid. |
| 400 | Abs.SnapshotNotFo und | InvalidSnapshotId.NotFound | The specified parameter SnapshotId is not exist. |
| 400 | InvalidTagKey.Malfo rmed | InvalidTagKey.Malformed | The specified Tag.n.Key is not valid. |
| 400 | InvalidTagValue.Mal formed | InvalidTagValue.Malformed | The specified Tag.n.Value is not valid. |
| 400 | INVALID TAG MISM _ _ ATCH | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. |
| 400 | INVALID TAG COUN _ _ T | InvalidTagCount | The specified tags are beyond the permitted range. |
| 400 | Abs.InvalidMinAmou nt.Malformed | InvalidMinAmount.Malformed | The specified parameter MinAmount is not valid. |
| 400 | Abs.InvalidMaxAmo unt.Malformed | InvalidMaxAmount.Malformed | The specified parameter MaxAmount is not valid. |
| 400 | Abs.InvalidAutoRele aseTime.Malformed | InvalidAutoReleaseTime.Malform ed | The specified parameter AutoReleaseTime is not valid. |
| 400 | Abs.InvalidPrivateIp Address.Malformed | InvalidPrivateIpAddress.Malform ed | The specified parameter PrivateIpAddress is not valid. |
| 400 | Abs.InvalidInnerIpAd dress.Malformed | InvalidInnerIpAddress.Malformed | The specified parameter InnerIpAddress is not valid. |
| 400 | -1015001 | OperationDenied.NoVlan | The specified parameter "VlanId" is not valid or vlan has not enough IP address. |
| 400 | -192 | OperationDenied.NoVlan | The specified parameter "VlanId" is not valid or vlan has not enough IP address. |

|  | 开发指南·API参 | 考 |  | 云服务器EC | S |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1015001 | OperationDenied.NoVlan | The specified parameter "VlanId" is not valid or vlan has not enough IP address. |
| 400 | OperationDenied.Qu otaExceed | OperationDenied.QuotaExceed | The quota of tags on resource is beyond permitted range. |
| 403 | ORDER.ARREARAGE | Account.Arrearage | Your account has been in arrears. |
| 400 | InvalidUserData.Size Exceeded | InvalidUserData.SizeExceeded | The specified parameter "UserData" exceeds the size. |
| 400 | InvalidUserData.Not Kvm | InvalidUserData.NotSupported | The specified parameter "UserData" only support the vpc and IoOptimized Instance. |
| 400 | InvalidUserData.Not Kvm | InvalidUserData.NotSupported | The specified parameter "UserData" only support the vpc and IoOptimized Instance. |
| 400 | InvalidUserData.Bas e64FormatInvalid | InvalidUserData.Base64FormatIn valid | The specified UserData is not valid. |
| 400 | Abs.InvalidDataDisk s.MalFormed | InstanceDiskNumber.LimitExcee d | The total number of specified disk in an instance exceeds. |
| 400 | INVALID DISK CATE _ _ GORY | InvalidDiskCategory.ValueNotSu pported | The specified parameter "DiskCategory" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 01570138 | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | Abs.InvalidSpotStrat egy | InvalidSpotStrategy | The specified SpotStrategy is not valid. |
| 400 | Abs.SpotStrategy.E mptyZoneID | InvalidSpotParam.EmptyZoneID | The specified zoneid is empty when SpotStrategy is set. |
| 400 | Abs.InvalidSpotPrice Limit | InvalidSpotPriceLimit | The specified SpotPriceLimitis not valid. |
| 400 | Abs.InvalidSpotDura tion | InvalidSpotDuration | The specified SpotDuration is not valid. |
| 400 | Abs.InvalidSpotAuth | InvalidSpotAuthorized | The specified Spot param is unauthorized. |
| 400 | Abs.InvalidSpotPreP ay | InvalidSpotPrepaid | The specified Spot type is not support PrePay Instance. |
| 400 | Abs.Abs.InvalidSpotI nstanceUID | InvalidSpotAliUid | The specified UID is not authorized to use SPOT instance. |
| 400 | Invalid.Bandwidth.P ublicOut | InvalidParameter.Bandwidth | %s |
| 400 | Invalid.DataDisk.Cat egory | InvalidDataDiskCategory.ValueN otSupported | %s |

|  | 云服务器ECS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.SystemDisk. Category | InvalidSystemDiskCategory.Valu eNotSupported | %s |
| 400 | Invalid.Conflict | InvalidParameter.Conflict | %s |
| 400 | Invalid.Bandwidth.P ayType | InvalidInternetChargeType.Value NotSupported | %s |
| 400 | Invalid.Instance.Typ e | InvalidInstanceType.ValueNotSu pported | %s |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 006444 | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | NOT AVAILABLE IZ _ _ _ AUZ EXISTS _ | Zone.NotOnSale | The resource in the specified zone is no longer available for sale. Please try other regions and zones. |
| 400 | Invalid.SystemDisk. Size | InvalidSystemDiskSize.ValueNot Supported | %s |
| 400 | Invalid.DataDisk.Siz e | InvalidDataDiskSize.ValueNotSu pported | %s |
| 400 | -1018002 | InvalidInstanceType.ValueNotSu pported | The specified parameter "KeyPairName" only support IoOptimized Instance. |
| 400 | KeyPairInstance.Not Kvm | InvalidInstanceType.ValueNotSu pported | The specified parameter "KeyPairName" only support IoOptimized Instance. |
| 400 | ENI NOT SUPPORT _ _ _ GENERATION 1 _ | InvalidInstanceType.ElasticNetw orkInterfaceNotSupported | The specified instance type does not support Elastic Network Interface, you can not attach Elastic Network Interface to generation I instances. |
| 400 | InvalidKMSKeyId.Not MatchParamEncrypt ed | InvalidParameter.EncryptedIlleg al | The specified parameter Encrypted must be true when kmsKeyId is not empty. |
| 400 | DISK CATEGORY IS _ _ _ NOT SUPPORT ENC _ _ RYPTED | InvalidParameter.EncryptedNotS upported | %s |
| 400 | PARAMETER CONFLI _ CT | InvalidParameter.Conflict | %s |
| 400 | DISK CATEGORY IS _ _ _ NOT SUPPORT ENC _ _ RYPTED | InvalidParameter.EncryptedNotS upported | %s |
| 400 | ECS SPOT USER PRI _ _ _ CE MUST LARGE TH _ _ _ AN PUBLIC PRICE _ _ | InvalidSpotPriceLimit.LowerThan PublicPrice | The specified parameter "spotPriceLimit" can't be lower than current public price. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALID RECYCLEBI _ N RELATION RESOU _ _ RCE | InvalidRelationResource.NotFou nd | The relation resource has been deleted. |
| 400 | INVALID SOURCE R _ _ ESOURCE STATUS _ | IncorrectRecycleBinStatus | The operation is not permitted due to resource status. |
| 400 | HPC CLUSTER ID IS _ _ _ UNNECESSARY _ | InvalidHpcClusterId.Unnecessary | The specified HpcClusterId is unnecessary. |
| 400 | VSWITCH IS EMPTY _ _ | InvalidVSwitchId.Necessary | The VSwitchId is necessary. |
| 400 | HPC CLUSTER ID IS _ _ _ EMPTY _ | InvalidHpcClusterId.Necessary | The HpcClusterId is necessary. |
| 400 | HPC CLUSTER ID IS _ _ _ NOT EXIST _ _ | InvalidHpcClusterId.NotFound | The specified HpcClusterId is not found. |
| 400 | HPC CLUSTER IS C _ _ _ REATING | InvalidHpcClusterId.Creating | The specified HpcClusterId is creating. |
| 400 | InvalidParameter.VS witchId | InvalidParameter.VSwitchId | %s |
| 400 | InvalidParams.Hostn ame | InvalidHostName.Malformed | The specified parameter "HostName" is not valid. |
| 400 | GROUP NOT IN DEF _ _ _ AULTVPC | InvalidSecurityGroup.NotInDefau ltVpc | %s |
| 400 | VPC NOT FOUND F _ _ _ ROM VSW _ | VpcNotFound | Vpc is not found according to the specified VSwitch or the vpc does not belong to you. |
| 400 | InvalidSystemDiskSi ze.ImageNotSupport Resize | InvalidSystemDiskSize.ImageNot SupportResize | The specified image does not support resize. |
| 400 | PRICE.PRICING PLAN _ RESULT NOT FOUN _ _ _ D | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorized. |
| 400 | Abs.InvalidSpotInter ruptionBehavior | InvalidSpotInterruptionBehavior | %s |
| 400 | Abs.InvalidDeploym entOnHost.ValueNot Supported | InvalidDeploymentOnHost | %s |
| 400 | Abs.InvalidSpotPrice LimitOnHost.ValueN otSupported | InvalidInstanceChargeType.NotS upport | The Dedicated host not support the specified Instance charge type. |
| 400 | Abs.InvalidSpotPrice LimitOnHost.ValueN otSupported | InvalidInstanceChargeType.NotS upport | The Dedicated host not support the specified Instance charge type. |
| 400 | CLASSIC NOT SUPP _ _ ORT | InvalidNetworkType.NotSupport ed | The classic networkType not support create ECS on dedicatedHost. |

|  | 云服务器ECS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NO AVAILABLE HOS _ _ T EXIST _ | NoAvaliableDedicatedHost | A dedicated host with sufficient available resources cannot be found. |
| 400 | -305 | InvalidDedicatedHostId.NotFoun d | The specified DedicatedHostId does not exist. |
| 400 | HOST BUSINESS ST _ _ ATUS NOT VALID _ _ | InvalidDedicatedHostStatus.Not Support | Operation denied due to dedicated host status. |
| 400 | HOST STATUS NOT _ _ _ VALID | IncorrectDedicatedHostStatus | The current status of the resource does not support this operation. |
| 400 | DEDICATED HOST P _ _ AY TYPE NOT SUPP _ _ _ ORTED THE VM PA _ _ _ Y TYPE _ | ChargeTypeViolation.PostPaidDe dicatedHost | Prepaid instance onto postpaid dedicated host is not allowed. |
| 400 | ECS ON HOST NOT _ _ _ SUPPORT _ | InvalidPeriod.ExceededDedicate dHost | Instance expired date can't exceed dedicated host expired date. |
| 400 | DEDICATED HOST T _ _ YPE IS ILLEGAL _ _ | InvalidInstanceType.ValueUnaut horized | The specified InstanceType is not authorize. |
| 400 | INVALID INSTANCE _ _ TYPE | DedicatedHostType.Unmatched | The specified DedicatedHostType doesn?t match the instance type. |
| 400 | DEDICATED HOST R _ _ ESOURCE NOT ENO _ _ UGH | NoAvaliableDedicatedHost | There's no enough resource on the specified dedicated host. |
| 400 | -305 | InvalidDedicatedHostId.NotFoun d | The specified DedicatedHostId does not exist. |
| 400 | Abs.MissingParamet er.ImageId | MissingParameter | The input parameter ImageId that is mandatory for processing this request is not supplied. |
| 400 | Abs.MissingParamet er.InstanceType | MissingParameter | The input parameter InstanceType that is mandatory for processing this request is not supplied. |
| 400 | DEDICATED HOST P _ _ AY TYPE NOT SUPP _ _ _ ORTED THE VM PA _ _ _ Y TYPE _ | ChargeTypeViolation.PostPaidDe dicatedHost | Prepaid instance onto postpaid dedicated host is not allowed. |
| 400 | InvalidParam.Netwo rkInterface | InvalidParam.NetworkInterface | %s |
| 400 | InvalidParams.Creat eEniParams | InvalidParams.CreateEniParams | %s |
| 400 | InvalidParameter.Cr editSpecification | InvalidParameter.CreditSpecifica tion | The specified CreditSpecification is not supported in this region. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALID INSTANCE _ _ TYPE | DedicatedHostType.Unmatched | The specified DedicatedHostType doesn?t match the instance type. |
| 400 | VPC INCORRECT ST _ _ ATUS | IncorrectVpcStatus | The current status of vpc does not support this operation. |
| 403 | PRODUCT.INSTANCE TYPE NOT EXIST _ _ _ | InvalidInstanceType.NotSupport ed | The specified InstanceType is not Supported. |
| 400 | IMAGE ARCHITECTU _ RE NOT MATCH INS _ _ _ TANCE TYPE _ | InvalidInstanceType.NotSupport ed | The specified instanceType is not supported by the image architecture. |
| 400 | VPC ZONE NOT SU _ _ _ PPORT CREATE _ | InvalidVpcZone.NotSupported | The specified operation is not allowed in the zone to which your VPC belongs, please try in other zones. |
| 400 | VPC DEFAULT DEFA _ _ ULTVPC STATUS ILL _ _ EAGE | IncorrectDefaultVpcStatus | The status of the default VPC is invalid. |
| 400 | Abs.InvalidAutoRene wPeriod.ValueNotSu pported | InvalidAutoRenewPeriod.ValueN otSupported | The specified autoRenewPeriod is invalid. |
| 400 | YUNMARKET BIZ IM _ _ AGE IS UNSUPPORT _ _ ED | InvalidMarketImageChargeType. NotSupport | The specified chargeType of marketImage is unsupported. |
| 403 | USERPROFILECOMPL ETE | OperationDenied | The user profile is not complete; try complete your basic info in account management page. |
| 400 | Abs.InvalidPeriodTy pe.Malformed | InvalidPeriodType.ValueNotSupp orted | The specified parameter PeriodType is invalid. |
| 400 | Abs.InvalidClientTok en.Malformed | InvalidClientToken.ValueNotSup ported | The ClientToken provided is invalid. |
| 400 | Trade Not Support _ _ _ Async Pay _ | OperationDenied | The current user does not support this operation. |
| 400 | YUNMARKET BIZ MI _ _ RROR IMAGE IS UN _ _ _ USABLE | IncorrectImageStatus | The specified image is an Alibaba Cloud Marketplace image. The sale of this image has ended. For more information, contact the image service provider. |
| 400 | ORDER.BID USER O _ _ RDER FORBIDDEN _ | OperationDenied | The current user does not support this operation. |
| 400 | Abs.InvalidInstanceT ype.Null | InvalidInstanceType.ValueNotSu pported | The specified InstanceType does not exist or beyond the permitted range. |
| 400 | DEDICATED HOST N _ _ O AVAILABLE HOST _ _ | NoAvaliableDedicatedHost | No dedicated host is available. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter.Te nancy | InvalidParam.Tenancy | The specified Tenancy is invalid. |
| 400 | InvalidParameter.Aff inity | InvalidParameter.Affinity | The specified Affinity is invalid. |
| 400 | InvalidParameter.Aff inity | InvalidParameter.Affinity | The specified Affinity is invalid. |
| 400 | InvalidParameter.Te nancy | InvalidParam.Tenancy | The specified Tenancy is invalid. |
| 400 | DEDICATED HOST N _ _ O AVAILABLE HOST _ _ FOR AUTOPLACEM _ _ ENT | NoAvaliableDedicatedHost | A dedicated host with sufficient available resources cannot be found. |
| 400 | NO AVAILABLE HOS _ _ T EXIST _ | NoAvaliableDedicatedHost | A dedicated host with sufficient available resources cannot be found. |
| 400 | INVALID CUSTOM I _ _ NSTANCE TYPE _ | InvalidCustomInstanceType.Not Supported | The specified custom instance type is invalid. |
| 400 | INSTANCE TYPE NO _ _ T SUPPORT BY DEP _ _ _ LOYMENT SET _ | InvalidInstanceType.NotSupport ed | The specified instanceType is not supported by the deployment set. |
| 400 | VPC INCORRECT ST _ _ ATUS | IncorrectVpcStatus | The current status of vpc does not support this operation. |
| 400 | InvalidKMSKeyId.Not MatchParamEncrypt ed | InvalidParameter.EncryptedIlleg al | The specified parameter Encrypted must be true when kmsKeyId is not empty. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199815 | IoOptimized.NotSupported | The specified instancetype is not support IoOptimized instance. |
| 400 | Abs.InvalidSnapshot Id.Malformed | InvalidSnapshotId.Malformed | The specified SnapshotId is not valid. |
| 400 | CR NOT EXIST _ _ | InvalidCapacityReservationId.No tFound | The specified CapacityReservationId does not exist. |
| 400 | CR RESOURCE NOT _ _ ENOUGH _ | LackResource | There's no enough resource on the specified capacity reservation. |
| 400 | Duplicate.TagKey | Duplicate.TagKey | The Tag.N.Key contain duplicate key. |
| 400 | InvalidTagKey.Malfo rmed | InvalidTagKey.Malformed | The specified Tag.n.Key is not valid. |
| 400 | InvalidTagValue.Mal formed | InvalidTagValue.Malformed | The specified Tag.n.Value is not valid. |
| 400 | InvalidSecurityGrou p.NetworkType | InvalidSecurityGroup.NetworkTy pe | %s |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 400 | InvalidSecurityGrou p.VpcMismatch | InvalidSecurityGroup.VpcMismat ch | %s |
| 400 | InvalidParameter.Se curityGroupIdRepea ted | InvalidParameter.SecurityGroupI dRepeated | %s |
| 400 | InvalidSecurityGrou pId.SingleIdAndMulti IdConflict | InvalidSecurityGroupId.SingleIdA ndMultiIdConflict | %s |
| 400 | InvalidSecurityGrou pId.MultiGroupIdNet workTypeConflict | InvalidSecurityGroupId.MultiGro upIdNetworkTypeConflict | %s |
| 400 | JoinedGroupLimitExc eed | JoinedGroupLimitExceed | %s |
| 400 | VPC SWITCH STATU _ _ S ERROR _ | IncorrectVSwitchStatus | The current status of vSwitch does not support this operation. |
| 400 | PAY.AMOUNT LIMIT _ _ EXCEEDED | InvalidAccountStatus.PayAmoun tLimitExceeded | Your account is being restricted, because you have no default payment method or you are not authorized. |
| 400 | Abs.InvalidPerforma nceLevel.ValueNotS upported | InvalidPerformanceLevel.Malfor med | The specified parameter DataDisk.n.PerformanceLevel is not valid. |
| 400 | Abs.InvalidPerforma nceLevel.ValueNotS upported | InvalidPerformanceLevel.Malfor med | The specified parameter DataDisk.n.PerformanceLevel is not valid. |
| 403 | InvalidOperation.Eni CountExceeded | InvalidOperation.EniCountExcee ded | %s |
| 400 | PREPAY DISK QUOT _ _ A EXCEEDED _ | QuotaExceeded.PrepayDataDisk Capacity | The quota of prepay data disk capacity exceeds. |
| 400 | DISK CATEGORY CO _ _ NFLICT SNAPSHOT _ _ CATEGORY | InvalidDiskCategory.ConflictSna pshotCategory | The specified disk category conflict with snapshot category. |
| 400 | ALI CROUP 2 CLOU _ _ _ D USER CANNOT B _ _ _ UY NOT INNER CO _ _ _ MMODITY | AccountForbidden.ProductCreati onLimited | The commodity must be officially operated by Aliyun and in pay-as-you-go billing method. |
| 400 | UnexpectedImageFa mily.ImageIdProvide d | UnexpectedImageFamily.ImageI dSupplied | The input parameter ImageFamily must be null when image id is set. |
| 400 | InvalidEncrypted.No tMatchEncryptAlgori thm | InvalidEncrypted.NotMatchEncry ptAlgorithm | The specified parameter Encrypted must be true when EncryptAlgorithm is not empty. |
| 400 | InvalidEncrypted.No tMatchKmsKeyId | InvalidEncrypted.NotMatchKmsK eyId | The specified parameter Encrypted must be true when KmsKeyId is not empty. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidEncrypted.No tMatchSnapshot | InvalidEncrypted.NotMatchSnap shot | The specified parameter Encrypted is different from the Encrypted of the snapshot. |
| 400 | InvalidEncryptAlgori thm.NotMatchSnaps hot | InvalidEncryptAlgorithm.NotMat chSnapshot | The specified parameter EncryptAlgorithm is different from the encrypt algorithm of the snapshot. |
| 400 | InvalidKmsKeyId.Not MatchSnapshot | InvalidKmsKeyId.NotMatchSnaps hot | The specified parameter KmsKeyId is different from the KmsKeyId of the snapshot. |
| 400 | InvalidEncryptAlgori thm | InvalidEncryptAlgorithm | The specified parameter EncryptAlgorithm is not valid. |
| 400 | InvalidHttpEndpoint. NotSupported | InvalidHttpEndpoint.NotSupport ed | The specified HttpEndpoint not supported, you can use enabled(default) or disabled. |
| 400 | InvalidHttpTokens.N otSupported | InvalidHttpTokens.NotSupported | The specified HttpTokens not supported, you can use optional(default) or required. |
| 400 | InvalidHttpPutRespo nseHopLimit.NotSup ported | InvalidHttpPutResponseHopLimit .NotSupported | The specified HttpPutResponseHopLimit not supported, more than 1 and less than 64 is reasonable. |
| 400 | VPC HAS ENABLED _ _ _ SENIOR NETWORK _ _ FEATURE | InvalidOperation.VpcHasEnabled AdvancedNetworkFeature | The specified vpc has enabled advanced network feature. |
| 400 | CR NOT SUPPORT T _ _ _ HE VM PAY TYPE _ _ _ | InvalidChargeType.CapacityRese rvationNotSupported | %s |
| 400 | IZ OR INSTANCE TY _ _ _ PE FAMILY NOT SU _ _ _ PPORT PL0 _ | InvalidPerformanceLevel.ValueN otSupported | The current ZoneId or InstanceType does not support PL0 of cloud essd. _ |
| 400 | KMS KEY ID MUST _ _ _ _ BE SYMMETRICAL _ | InvalidKMSKeyId.NotSymmetric | The specified parameter KmsKeyId must be symmetric. |
| 400 | InvalidParam.Arns | InvalidParameter.Arns | The specified Arns is not valid. |
| 400 | DDH CLUSTER NOT _ _ EXIST _ | InvalidDedicatedHostClusterId.N otFound | The specified DedicatedHostClusterId does not exist. |
| 400 | DDH CLUSTER NOT _ _ VALID _ | InvalidDedicatedHostClusterId.In Valid | The specified Dedicated Host Cluster is invalid. |
| 400 | DEPLOYMENT SET _ _ NOT FOUND _ | InvalidDeploymentSetId.NotFoun d | The parameter DeploymentSetId is invalid. |
| 400 | TRADE DISTRIBUTO _ R CHECK FAIL _ _ | InvalidOperation.UserNotSuppor ted | Reseller user do not support purchase at the moment. |
| 400 | MANAGED PRIVATE _ _ SPACE NOT EXIST _ _ | InvalidManagedPrivateSpaceId.N otFound | %s |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidSchedulerOpt ion | InvalidSchedulerOptions | The specified parameter SchedulerOptions is not valid. |
| 400 | Abs.MissingParamet er.PackageId | MissingParameter.PrivatePoolOp tionsId | The specified PrivatePoolOptions.Id should not be null. |
| 400 | Abs.NoNeed.Packag eId | Invalid.PrivatePoolOptionsId | The parameter PrivatePoolOptions.Id should be null when PrivatePoolOptions.MatchCriteria is not Target. |
| 400 | Abs.NoNeed.Packag eId | Invalid.PrivatePoolOptionsId | The parameter PrivatePoolOptions.Id should be null when PrivatePoolOptions.MatchCriteria is not Target. |
| 400 | RP DDH NOT SUPP _ _ _ ORT | DedicatedHostNotSupported | DedicatedHost is not supported for PrivatePool. |
| 400 | RP SPOT NOT SUPP _ _ _ ORT | SpotNotSupported | Spot is not supported for PrivatePool. |
| 400 | RP CLASSICAL NOT _ _ _ SUPPORT | ClassicNetworkNotSupported | Classic network is not supported for PrivatePool. |
| 400 | RP INSTANCE NOT _ _ _ ATTACHED | Invalid.InstanceId | The Instance dose not attached to a PrivatePool. |
| 400 | RP INSTANCE MATC _ _ H CRITERIA NOT M _ _ _ ATCH | Invalid.PrivatePoolOptions.Match Criteria | The PrivatePoolOptions.MatchCriteria does not match the PrivatePool. |
| 400 | RP MISSING ATTAC _ _ HMENT ID _ | MissingParameter.PrivatePoolOp tions.Id | The specified PrivatePoolOptions.Id should not be null. |
| 400 | RP CR NOT EXISTS _ _ _ | Invalid.PrivatePoolOptions.Id | The PrivatePool does not exist. |
| 400 | RP CR NOT EXISTS _ _ _ | Invalid.PrivatePoolOptions.Id | The PrivatePool does not exist. |
| 400 | RP INSTANCE TYPE _ _ _ MISS MATCH _ | Invalid.InstanceType | The InstanceType does not match the PrivatePool. |
| 400 | RP INSTANCE CHAR _ _ GE TYPE MISS MAT _ _ _ CH | Invalid.InstanceChargeType | The InstanceChargeType does not match the PrivatePool. |
| 400 | RP ZONE ID NOT M _ _ _ _ ATCH | Invalid.ZoneId | The ZoneId does not match the PrivatePool. |
| 400 | RP PACKAGE USED _ _ _ UP | Invalid.PrivatePoolOptions.NoSto ck | The PrivatePool has been used up. |
| 400 | RP INSTANCE MATC _ _ H CRITERIA NOT M _ _ _ ATCH | Invalid.PrivatePoolOptions.Match Criteria | The PrivatePoolOptions.MatchCriteria does not match the PrivatePool. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RP PLATFORM NOT _ _ _ MATCH | InvalidPlatform.ValueNotSupport ed | The Platform does not match the PrivatePool. |
| 400 | RP INSTANCE OPER _ _ ATE TOO LATE _ _ | Invalid.PrivatePoolOptions.status | The Instance should be created within 48 hours once the PrivatePool is started. |
| 400 | RP PACKAGE STATU _ _ S NOT VALID _ _ | Invalid.PrivatePoolOptions.status | The PrivatePool status is not valid. |
| 400 | RP INSTANCE OPER _ _ ATE TOO LATE _ _ | Invalid.PrivatePoolOptions.status | The Instance should be created within 48 hours once the PrivatePool is started. |
| 400 | RP PACKAGE INSTA _ _ NCE NOT CONSISTE _ _ NT | InvalidAliUid | The PrivatePool does not belong to the user of the Instance. |
| 400 | RP INSTANCE NOT _ _ _ ATTACHED | Invalid.InstanceId | The Instance dose not attached to a PrivatePool. |
| 400 | INVALID ISP BAND _ _ WIDTH OUT _ | InvalidBandwidthOut.LessThanZ ero | The bandwidth must be larger than 0 when specifying isp. |
| 400 | HibernationConfigur ed.InstanceType.Not Support | HibernationConfigured.InstanceT ypeNotSupport | The specified instance type is not support. |
| 400 | HibernationConfigur ed.Image.NotEncryp ted | HibernationConfigured.ImageNo tEncrypted | The hibernation configured instance only support encrypted image. |
| 400 | HibernationConfigur ed.MemorySize.Too Big | HibernationConfigured.MemoryS izeTooBig | The hibernation configured instance memory size is too big. |
| 400 | InvalidSystemDiskSi ze.LessThanMemSiz e | InvalidSystemDiskSize.LessThan MemSize | The specified parameter SystemDisk.Size is less than the memory size. |
| 400 | CLOUD BOX IZ NOT _ _ _ SUPPORT THIS OP _ _ _ ERATION | InvalidCloudBoxZone.Operation NotSupported | The cloud box zone does not support creating prepaid or encrypted resources. |
| 400 | DISK CATEGORY NO _ _ T SUPPORT PROVISI _ _ ONED IOPS _ | ProvisionedIopsForDiskCategory Unsupported | The specified disk category does not support provisioned iops. |
| 400 | PROVISIONED IOPS _ _ BEYOND PERMITTE _ D RANGE _ | InvalidProvisionedIops.LimitExce ed | The provisioned iops exceeds the limit. |
| 400 | DISK CATEGORY NO _ _ T SUPPORT BURSTI _ _ NG ENABLED _ | BurstingEnabledForDiskCategory Unsupported | The specified disk category does not support bursting enabled. |
| 400 | MULTI ATTACH DIS _ _ K NOT ALLOW TO _ _ _ _ USE BURST ATTRIB _ _ UTE | BurstingEnabledForMultiAttachD iskUnsupported | The multi attach disk does not support bursting enabled. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | PROVISIONED IOPS _ _ BEYOND PERMITTE _ D RANGE _ | InvalidProvisionedIops.LimitExce ed | The provisioned iops exceeds the limit. |
| 400 | PROVISIONED IOPS _ _ REQUIRED FOR THI _ _ S DISK CATEGORY _ _ | ProvisionedIopsForDiskCategory Required | The provisioned iops is required for this disk category. |
| 400 | INSTANCE TYPE NO _ _ T SUPPORT SNAPSH _ _ OT ENCRYPT _ | NotSupportSnapshotEncrypted.I nstanceType | The specified instance type does not support creating encrypted disks with native snapshot encrypt. |
| 400 | REGIONID NOT SUP _ _ PORT SNAPSHOT E _ _ NCRYPT | NotSupportSnapshotEncrypted.R egionId | The specified region does not support creating encrypted disks with native snapshot encrypt. |
| 400 | IZNO NOT SUPPORT _ _ SNAPSHOT ENCRY _ _ PT | NotSupportSnapshotEncrypted.Z oneId | The specified zone does not support creating encrypted disks with native snapshot encrypt. |
| 400 | NOT SUPPORT SHA _ _ RE SNAPSHOT ENC _ _ RYPT | NotSupportSnapshotEncrypted.S hareImage | Shared snapshot creating encrypted disks with native snapshot encrypt is not supported. |
| 400 | IMAGE CATEGORY _ _ NOT SUPPORT SNA _ _ PSHOT ENCRYPT _ | NotSupportSnapshotEncrypted.I mageOwnerAlias | The specified image category does not support creating encrypted disks with native snapshot encrypt. |
| 403 | DISK CATEGORY NO _ _ T SUPPORT SNAPSH _ _ OT ENCRYPT _ | NotSupportSnapshotEncrypted. DiskCategory | The specified disk category does not support creating encrypted system disks or creating encrypted data disks from snapshots. Check the DiskCategory or Encrypted parameter, or check your account for default encryption settings. |
| 400 | SNAPSHOT ENCRYP _ T ALGORITHM CON _ _ FLICT | NotSupport.SnapshotEncryptedA lgorithmConflict | Changing encrypt algorithm with encrypted snapshot is not supported. |
| 400 | NoPermission.Syste mTag | NoPermission.SystemTag | The operator is not permission for the system tag. |
| 400 | NumberExceed.Tags | NumberExceed.Tags | The Tags parameter's number is exceed , Valid : 20. |
| 400 | IZS SUPPORT CREA _ _ TE WITH SHARE EN _ _ _ CRYPTED IMAGE _ | InvalidZoneId.NotSupportShareE ncryptedImage | Creating instances by shared encrypted images is not supported in this zone. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199819 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | CMKUnauthorized | InvalidParameter.KMSKeyId.CMK Unauthorized | This operation for kmsKeyId is forbidden by KMS. If you need further assistance, you can contact the KMS Technical Support. |
| 400 | InvalidParameter.Cl oudboxNotSupporte d | InvalidParameter.CloudboxNotS upported | %s |
| 400 | IZS NOT SUPPORT _ _ _ CREATE WITH SHAR _ _ E ENCRYPTED IMAG _ _ E | InvalidZoneId.NotSupportCreate WithShareEncryptedImage | You cannot use shared encrypted images to create instances in this zone. |
| 400 | InvalidParameter.Ne tworkCardIndexInval id | InvalidParameter.NetworkCardIn dexInvalid | Invalid network card index, please check your instance type. |
| 400 | InvalidOperation.Us erNotSupportNetwor kCard | InvalidOperation.UserNotSuppor tNetworkCard | User not support network card. |
| 400 | INSTANCE TYPE NO _ _ T SUPPORT CONFID _ _ ENTIAL COMPUTING _ MODE _ | InvalidInstanceType.NotSupport ed | The specified instanceType does not support confidential computing mode: %s. |
| 400 | Invalid.SysDisk.Cate gory | InvalidSystemDiskCategory.Valu eNotSupported | %s |
| 400 | ECS SEIZE INSTANC _ _ E | InvalidAccount.NotSupportSpot | According to business rules, this account cannot purchase ECS Spot instances. |
| 400 | CONTAIN FORBIDDE _ N LABEL ERROR _ _ | AccountForbidden.AssociatedWit hResellerPartner | Your account is associated with your reseller partner. Your account or your reseller partner's account has been forbidden to create orders, please contact your reseller partner. |
| 400 | INSTANCE MUST IN _ _ DEPLOYMENT SET _ _ _ IZ | InvalidDestinationZone.Deploym entSetMismatch | Error happened, %s. |
| 400 | InvalidPermission.Q ueryPriceRequired | NoPermission.Price | The operation requires price permission. Please either apply for permission from your main account, or set the parameter AutoPay as true. |
| 400 | InvalidAutoPay.Post PaidUnsupported | InvalidAutoPay.PostPaidUnsuppo rted | The specified parameter AutoPay must be set as true for postpaid instance. |
| 400 | NOT SUPPORT SHA _ _ RE ENCRYPTED IMA _ _ GE CREATE DISK W _ _ _ ITHOUT ENCRYPTIO _ N | InvalidParam.EncryptedMismatc h | Creating encrypted disks with shared encrypted image requires replacing encryption keys. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter.De dicatedRegionNotSu pported | InvalidParameter.DedicatedRegi onNotSupported | The specified action is rejected because the specified ECS instance in the dedicated region does not support public IP. |
| 400 | InvalidParameter.Cp uOptionsTopologyTy pe | InvalidParameter.CpuOptionsTo pologyType | The specified parameter CpuOptions.TopologyType: %s is not valid. |
| 400 | INSTANCE TYPE NO _ _ T SUPPORT CPU TO _ _ _ POLOGY | InvalidInstanceType.NotSupport CpuOptionsTopologyType | The specified instance type does not support CpuOptions.TopologyType: %s. |
| 400 | InvalidOperation.Re gionOrUserNotSupp ortEniQueueSize | InvalidEniQueueSize.RegionOrUs erNotSupported | The specified parameter RxQueueSize or TxQueueSize is not supported in this region, or this account is not in the whitelist of using eni QueueSize. |
| 400 | InvalidParameter.In validEniQueueSize | InvalidParameter.EniQueueSize | The specified parameter TxQueueSize and RxQueueSize are not equal or exceed limit. |
| 400 | KMS SERVICE NOT _ _ _ ENABLED | InvalidParameter.KmsNotEnable d | Failed to perform this operation because KMS is not activated. |
| 400 | KMS.Not.Enabled | InvalidParameter.Encrypted.Kms NotEnable | Failed to perform this operation because KMS is not activated. |
| 400 | NOT SUPPORT SHA _ _ RE ENCRYPTED IMA _ _ GE CREATE DISK W _ _ _ ITHOUT ENCRYPTIO _ N | InvalidParam.EncryptedMismatc h | Creating encrypted disks with shared encrypted image requires replacing encryption keys. |
| 400 | InvalidPrivateIpAddr ess.Duplicated | InvalidPrivateIpAddress.Duplicat ed | The specified private IP address "%s" is duplicated. |
| 400 | InvalidAdditionalInfo PvdConfig.SizeExce eded | InvalidAdditionalInfoPvdConfig.Si zeExceeded | The specified parameter AdditionalInfo.PvdConfig exceeds the size. |
| 400 | InvalidPrivateIpAddr ess.Duplicated | InvalidPrivateIpAddress.Duplicat ed | The specified private IP address "%s" is duplicated. |
| 400 | SNAPSHOT ENCRYP _ T CONFLICT _ | InvalidParameter.Encrypted | Creating non-encrypted disks with encrypted snapshots is not supported. |
| 400 | INSTANCE TYPE NO _ _ T SUPPORT MODIFY _ _ HIGH DENSITY MO _ _ _ DE | InvalidInstanceType.NotSupport HighDensityMode | The specified instance type does not support the use of the high density mode. |
| 400 | QuotaExceeded.Inte rnetBandwidth | QuotaExceeded.InternetBandwid th | %s. |
| 400 | InvalidParameter.Ac celeratorOptions | InvalidParameter.CpuOptionsAcc elerators | The specified parameter CpuOptionsAccelerators is not valid. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INSTANCE TYPE NO _ _ T SUPPORT ACCELE _ _ RATOR OPTIONS _ | InvalidInstanceType.NotSupport CpuOptionsAccelerators | The specified instance type does not support attach accelerator. |
| 400 | Forbid.Create.TestA ccount | OperationDenied.TestAccountRe tricted | Test-account for testing has been prohibited from creating instance in this region. Please contact 400181. |
| 400 | DISK SIZE TOO SM _ _ _ ALL TO ENABLE BU _ _ _ RST | InvalidBurstingEnabled.DiskSize TooSmall | The disk size must be greater than 3 GiB to enable burst. |
| 401 | NoPermission | InvalidRamRole.NotEcsRole | The specified ram role is not authorized for ecs, please check your role policy. |
| 403 | PAY.COUPON AMOU _ NT NOT ENOUGH _ _ | OperationDenied.CashCouponsI nsufficientOrExpired | Cash coupon balance is insufficient or has expired, please retry. |
| 403 | InvalidParameter.Pri vateIpAddressRepea ted | InvalidParameter.PrivateIpAddre ssRepeated | %s |
| 403 | InvalidOperation.Hig hPerformanceEniPer InstanceLimitExceed ed | InvalidOperation.HighPerforman ceEniPerInstanceLimitExceeded | %s |
| 403 | EniNumExceededWi thLaunchEcs | InvalidParameter.EniNumExceed edWithLaunchEcs | %s |
| 403 | InvalidParameter.Pri vateIpAddressRepea ted | InvalidParameter.PrivateIpAddre ssRepeated | %s |
| 403 | InvalidOperation.Ins tanceTypeNotSuppo rtHighPerformanceT rafficMode | InvalidOperation.InstanceTypeN otSupportHighPerformanceTraffi cMode | %s |
| 403 | InvalidParameter.Qu euePairNumberMust Empty | InvalidParameter.QueuePairNum berMustEmpty | %s |
| 403 | InvalidParameter.En iTrafficMode | InvalidParameter.EniTrafficMode | %s |
| 403 | InvalidParameter.In validQueuePairNum ber | InvalidParameter.InvalidQueueP airNumber | The parameter of QueuePairNumber is invalid. |
| 403 | InvalidParam.IpCoun t | InvalidParam.IpCount | The parameter of ip count is invalid. |
| 403 | InvalidParameter.En iType | InvalidParameter.EniType | %s |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidOperation.Hig hPerformanceTraffic ModeIsNotAllowed | InvalidOperation.HighPerforman ceTrafficModeIsNotAllowed | %s |
| 403 | InvalidParameter.Ne tworkInterface | InvalidParameter.NetworkInterfa ce | %s |
| 403 | InvalidParameter.Co mbination | InvalidParameter.Combination | %s |
| 403 | InvalidHostname.Sin gleAndMultiConflict | InvalidHostname.SingleAndMulti Conflict | %s |
| 403 | InvalidHostname.Siz eInvalid | InvalidHostname.SizeInvalid | %s |
| 403 | Abs.InvalidParams.I nstanceNameExcee d | InvalidParams.InstanceNameExc eed | The uniqueSuffix takes three naming places, please shorten your InstanceName. |
| 403 | Abs.InvalidParams.H ostnameExceed | InvalidParams.HostnameExceed | The uniqueSuffix takes three naming places, please shorten your Hostname. |
| 403 | YUNMARKET BIZ MI _ _ RROR USER NO SU _ _ _ BSCRIPTION | ImageNotSubscribed | The specified image has not be subscribed. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179231 | InvalidSystemDiskCategory.Valu eUnauthorized | The disk category is not authorized. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179231 | InvalidSystemDiskCategory.Valu eUnauthorized | The disk category is not authorized. |
| 403 | SNAPSHOT CREATE _ NOT FINISHED _ _ | InvalidSnapshotId.NotReady | The specified snapshot has not completed yet. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179249 | InstanceDiskCategoryLimitExcee d | The total size of specified disk category in an instance exceeds. |
| 403 | DISK MOUNT POINT _ _ DUPLICATE _ | InvalidDevice.InUse | The specified device has been occupied. |
| 403 | YUNMARKET BIZ MI _ _ RROR SALE OFF _ _ | ImageRemovedInMarket | The specified market image is not available, Or the specified user defined image includes product code because it is based on an image subscribed from marketplace, and that image in marketplace includeing exact the same product code has been removed. |
| 403 | NOT AVAILABLE ZO _ _ NE SUPPORT CATE _ _ GORIES EXISTS _ | CategoryNotSupported | The specified cluster does not offer the specified disk category. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ECS BIZ DISK QUO _ _ _ TA USER _ | QuotaExceed.PortableCloudDisk | The quota of portable cloud disk exceeds. |
| 403 | PARAMETER GROUP _ ECS QUOTA FULL _ _ _ | SecurityGroupInstanceLimitExce ed | Exceeding the allowed amount of instances of a security group. |
| 403 | -3135 | NodeControllerUnavailable | The Node Controller is temporarily unavailable. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 006444 | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | NOT AVAILABLE ZO _ _ NE SUPPORT SYSTE _ _ M CATEGORY EXIST _ _ S | CategoryNotSupported | The specified Zone or cluster does not offer the specified disk category. |
| 403 | PARAMETER SNAPS _ HOT CHECK DATA _ _ | InvalidSnapshotId.NotDataDiskS napshot | The specified snapshot is system disk snapshot. |
| 403 | NOT AVAILABLE ZO _ _ NE SUPPORT CATE _ _ GORIES EXISTS _ | CategoryNotSupported | The specified cluster does not offer the specified disk category. |
| 403 | USER NOT ALLOW _ _ _ BUY COMMODITY _ | Forbbiden | User not authorized to operate on the specified resource. |
| 403 | IMAGE CATEGORY _ _ NOT SUPPORT _ | DeleteWithInstance.Conflict | The specified image is from the image market, you cannot set DeleteWithInstance attribute to false. |
| 403 | DISK CATEGORY PO _ _ RTABLE DELETE NO _ _ TMATCH | DeleteWithInstance.Conflict | The specified disk is not a portable disk and cannot be set to DeleteWithInstance attribute. |
| 403 | EXCEED DISK NUM _ _ _ FOR ONE ECS _ _ | InstanceDiskNumLimitExceed | The number of specified disk in an instance exceeds. |
| 403 | IMAGE MUST SUPP _ _ ORT IOOPTIMIZED _ | IoOptimized.NotSupported | The specified image is not support IoOptimized Instance. |
| 403 | InvalidDiskSize.TooS mall | InvalidDiskSize.TooSmall | Specified disk size is too small when choosing PL0 of cloud essd. _ |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179235 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179240 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199830 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199826 | InvalidDiskCategory.Mismatch | The specified disk categories combination is not supported. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199813 | IoOptimized.NotSupported | Vpc is not support IoOptimized instance. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179448 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199821 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199819 | InvalidDiskCategory.NotSupport ed | The specified disk category is not support the specified instance type. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179252 | InstanceDiskCategoryLimitExcee d | The total size of specified disk category in an instance exceeds. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199839 | InstanceDiskCategoryLimitExcee d | The total size of specified disk category in an instance exceeds. |
| 403 | ECS IMAGE PRODU _ _ CT QUOTA USER _ _ | QuotaExceed.BuyImage | The specified image is from the image market?You have not bought it or your quota has been exceeded. |
| 403 | InvalidResourceId.N otSupported | InvalidResourceId.NotSupported | The specified ResourceId does not support tagging. |
| 403 | Abs.OperationDenie d | OperationDenied | The specified RegionId does not support the creation of the network type ECS instance. |
| 404 | ECS BIZ IMAGE NO _ _ _ T FOUND _ | OperationDenied.ImageNotValid | The specified Image is disabled or is deleted. |
| 403 | SNAPSHOT DISK IN _ _ _ BLACK LIST _ | OperationDenied.SnapshotNotV alid | The specified snapshot is not allowed to create disk. |
| 403 | ECS SNAPSHOTID I _ _ NVALID | OperationDenied.SnapshotNotAll owed | The specified snapshot is not allowed to create disk. |
| 403 | IZ NOT IN SALE _ _ _ | OperationDenied.ZoneNotAllowe d | The creation of Instance to the specified Zone is not allowed. |
| 403 | NOT AVAILABLE IZ _ _ _ SUPPORT CATEGORI _ ES EXISTS _ | OperationDenied.ZoneSystemCa tegoryNotMatch | The specified Zone or cluster does not offer the specified disk category or the speicified zone and cluster do not match. |
| 403 | NOT AVAILABLE IZ _ _ _ SUPPORT CATEGORI _ ES EXISTS _ | OperationDenied.ZoneSystemCa tegoryNotMatch | The specified Zone or cluster does not offer the specified disk category or the speicified zone and cluster do not match. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ECS NO BUY NOW _ _ _ | OperationDenied.ResourceContr ol | The specified region is in resource control, please try later. |
| 403 | -60017 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00179244 | OperationDenied.SnapshotPara msNotValid | The capacity of snapshot exceeds the size limit of the specified disk category or the specified category is not authorizied. |
| 403 | -605 | OperationDenied.DiskTypeNotSu pport | The type of the disk does not support the operation. |
| 403 | ECS BIZ IMAGE IS _ _ _ _ DELETED | OperationDenied.ImageNotValid | The specified Image is disabled or is deleted. |
| 403 | ECS SNAPSHOTID I _ _ NVALID | OperationDenied.SnapshotNotAll owed | The specified snapshot is not allowed to create disk. |
| 403 | ECS BIZ CHECK NO _ _ _ T HAS ENOUGH ST _ _ _ OCK | OperationDenied.NoStock | The resource is out of usage. |
| 403 | InvalidUserData.NotI nWhiteList | InvalidUserData.Forbidden | User not authorized to input the parameter "UserData", please apply for permission "UserData". |
| 403 | NOT AVAILABLE IZ _ _ _ BIZ EXISTS _ | Zone.NotOpen | The specified zone is not granted to you to buy resources yet. |
| 403 | NOT AVAILABLE IZ _ _ _ AUZ EXISTS _ | Zone.NotOnSale | The resource in the specified zone is no longer available for sale. Please try other regions and zones. |
| 404 | -150 | InvalidClusterId.NotFound | The ClusterId provided does not exist in our records. |
| 403 | INVALID RESOURCE _ TYPE NOT FOUND _ _ _ | InvalidResourceType.NotSupport ed | %s |
| 403 | ECS NOT HAS ENO _ _ _ UGH STOCK _ | OperationDenied.NoStock | The resource is out of stock in the specified zone. Please try other types, or choose other regions and zones. |
| 403 | NOT AVAILABLE IZ _ _ _ FLAVOR STOCK _ | OperationDenied.NoStock | The resource is out of stock in the specified zone. Please try other types, or choose other regions and zones. |
| 403 | INSTANCE TYPE NO _ _ T EXIST _ | InvalidInstanceType.ValueNotSu pported | The specified InstanceType beyond the permitted range. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | INSTANCE TYPE NO _ _ ZONE SUPPORT _ _ | InvalidInstanceType.ZoneNotSup ported | The specified zone does not support this instancetype. |
| 403 | PARAMETER GROUP _ ECS QUOTA FULL _ _ _ | SecurityGroupInstanceLimitExce ed | Exceeding the allowed amount of instances of a security group. |
| 403 | Offline.Instance.Typ e | InstanceType.Offline | %s |
| 403 | DependencyViolatio n.WindowsInstance | DependencyViolation.WindowsIn stance | The instance creating is window, cannot use ssh key pair to login. |
| 403 | INVALID NETWORK _ _ TYPE | InvalidNetworkType.MismatchRa mRole | A RAM role can?t be used for classic instance. |
| 403 | InvalidUser.PassRole Forbidden | InvalidUser.PassRoleForbidden | The RAM user does not have the privilege to pass a RAM role. |
| 403 | Abs.InvalidTrustedS ystemMode.ValueNo tSupported | InvalidParam.TrustedSystemMod e | The specified TrustedSystemMode is invalid. |
| 403 | Abs.InvalidConfident ialComputingMode.V alueNotSupported | InvalidParam.ConfidentialCompu tingMode | The specified ConfidentialComputingMode is invalid. |
| 403 | INSTANCE TYPE NO _ _ T SUPPORT TRUSTE _ _ D SYSTEM _ | InvalidInstanceType.NotSupport ed | The specified instance type does not support trusted system. |
| 403 | Abs.InvalidSecurityO ptionsForVtpmAndE nclave.ValueNotSup ported | InvalidSecurityOptions.NotSuppo rted | SecurityOptions for vTPM and Enclave can not both be set. |
| 403 | IMAGE NOT SUPPO _ _ RT ENCLAVE INSTA _ _ NCE | InvalidImage.NotSupported | The specified image does not support Enclave instance. |
| 403 | INSTANCE TYPE NO _ _ T SUPPORT ENCLAV _ _ E | InvalidInstanceType.NotSupport ed | The specified instance type does not support Enclave. |
| 403 | IMAGE NOT SUPPO _ _ RT VSGX INSTANCE _ _ | InvalidImage.NotSupported | The specified image does not support vSGX instance. |
| 403 | IMAGE NOT SUPPO _ _ RT ENCLAVE INSTA _ _ NCE | InvalidImage.NotSupported | The specified image does not support Enclave instance. |
| 403 | RISK.RISK REJECT _ | Forbidden.RiskControl | This operation is forbidden by Aliyun RiskControl system. |
| 403 | ORDER.INST HAS U _ _ NPAID ORDER _ | InvalidInstance.UnPaidOrder | The specified Instance has unpaid order. |
| 403 | ORDER.ARREARAGE | Account.Arrearage | Your account has been in arrears. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ORDER.NO REAL N _ _ AME AUTHENTICATI _ ON | RealNameAuthenticationError | Your account has not passed the real-name authentication yet. |
| 403 | PRODUCT.INSTANCE TYPE NOT EXIST _ _ _ | InvalidInstanceType.NotSupport ed | The specified InstanceType is not Supported. |
| 403 | PAY.ACCOUNT BOO _ K NOT EXIST _ _ | InvalidPayMethod | The specified pay method is not valid. |
| 403 | PAY.ACCOUNT BOO _ K NOT EXIST _ _ | InvalidPayMethod | The specified pay method is not valid. |
| 403 | INSUFFICIENT BALA _ NCE | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |
| 403 | PAY.CREDIT BOOK I _ _ NSUFFICENT BALAN _ CE | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |
| 403 | PAY.OWNING FEE _ | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |
| 403 | PAY.INSUFFICIENT B _ ALANCE | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |
| 403 | INSUFFICIENT BALA _ NCE | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |
| 403 | ImageNotSupportIns tanceType | ImageNotSupportInstanceType | The specified image does not support the specified InstanceType. |
| 403 | DryRun.InvalidAmou nt | DryRun.InvalidAmount | %s |
| 403 | NetworkNotSupport CreateEcs | OperationDenied.InvalidNetwork Type | %s |
| 403 | CLASSIC NOT SUPP _ _ ORT | InvalidSpotInterruptionBehavior. ClassicNetworkNotSupport | The specified SpotInterruptionBehavior does not support Classic network Instance. |
| 403 | VM IS LOCAL NOT _ _ _ _ ALLOWED ARCHIVE _ | InvalidSpotInterruptionBehavior. LocalDiskNotSupport | The specified SpotInterruptionBehavior does not support local disk instance. |
| 403 | IMAGE NOT SUPPO _ _ RTED | OperationDenied.ImageNotValid | %s |
| 403 | DATA DISK QUOTA _ _ _ FULL | QuotaExceed.PostPaidDisk | Living postPaid disks quota exceeded. |
| 403 | VALIDATION FORBI _ DDEN | InvalidParameter.NotMatch | %s |
| 403 | VPC DEFAULT VSWI _ _ TCH NOT ALLOWID _ _ _ IN VPC _ | InvalidVSwitch.DefaultVSwitchN otSupport | The specified zone in vpc can't support create default vSwitch. |

|  | 开发指南·API参 | 考 |  | 云服务器EC | S |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ImageBIDNotPublish edToSpecifiedRegio n | OperationDenied.ImageNotValid | The specified image is not published in the region. |
| 403 | ImageNotPublishedT oSpecifiedRegion | OperationDenied.ImageNotValid | The specified image is not published in the region. |
| 403 | ImageNotAuthorized ToSpecifiedBid | OperationDenied.ImageNotValid | The specified image is not authorized. |
| 403 | ProductImageNotFo undInMarketplace | OperationDenied.ImageNotValid | The specified image is not found in marketplace. |
| 403 | DISK TYPE NOT SU _ _ _ PPORT | OperationDenied.LocalDiskUnsu pported | The configuration change is not allowed when the specified instance has local disks mounted. |
| 403 | INCONSISTENT SEC _ URITY GROUP AND _ _ _ VSWITCH | OperationDenied.InconsistentNe twork | The specified security group and vswitch are not in the same vpc. |
| 403 | VPC DEFAULT VSWI _ _ TCH NOT ALLOWED _ _ IN VPC _ _ | OperationDenied | If the network segment of the vswitch is the same as that of its VPC. Therefore, the VPC cannot create other vswitchs across the region. |
| 403 | VPC DEFAULT VSWI _ _ TCH EXIST _ | DefaultVswitch.Existed | The default vswitch for VPC already exists. |
| 403 | -60017 | OperationDenied.NoStock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. |
| 403 | PAY.INVALID INSTA _ NCE STATUS _ | IncorrectInstanceStatus | The current status of the resource does not support this operation. |
| 403 | vm with ephemeral _ _ disk _ | CategoryViolation | The specified instance does not support this operation because of its disk category. |
| 403 | IZ NOT MATCHED _ _ | ResourcesNotInSameZone | The specified instance and dedicated host are not in the same zone. |
| 403 | PARAMETER SYSTE _ M DISK SIZE ILLEG _ _ _ AL | InvalidDisk.SystemDiskSize | The specified SystemDiskSize beyond the permitted range. |
| 403 | 12034 | InsufficientBalance | Your account does not have enough balance. |
| 403 | InvalidOperation.Net workInterface | InvalidOperation.NetworkInterfa ce | %s |
| 403 | MaxEniIpv6IpsCount Exceeded | MaxEniIpv6IpsCountExceeded | %s |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidIp.IpRepeated | InvalidIp.IpRepeated | %s |
| 403 | InvalidIp.IpAssigned | InvalidIp.IpAssigned | %s |
| 403 | InvalidIp.Address | InvalidIp.Address | %s |
| 403 | InvalidOperation.Eni CountExceeded | InvalidOperation.EniCountExcee ded | %s |
| 403 | InvalidOperation.ipv 4CountExceeded | InvalidOperation.Ipv4CountExce eded | %s |
| 403 | InvalidOperation.ipv 6CountExceeded | InvalidOperation.Ipv6CountExce eded | %s |
| 403 | InvalidOperation.ipv 6NotSupport | InvalidOperation.Ipv6NotSupport | %s |
| 403 | InvalidOperation.ipv 4NotSupport | InvalidOperation.Ipv4NotSupport | %s |
| 403 | InvalidParam.Secon daryIp | InvalidParam.SecondaryIp | %s |
| 403 | InvalidVSwitch.Ipv6 NotTurnOn | InvalidVSwitch.Ipv6NotTurnOn | %s |
| 403 | InvalidParam.ipAssi gn | InvalidParam.IpAssign | %s |
| 403 | InvalidParam.Amoun t | InvalidParam.Amount | %s |
| 403 | Abs.InvalidCpuOptio nsCore.ValueNotSup ported | InvalidParam.CpuOptionsCore | %s |
| 403 | Abs.InvalidCpuOptio nsNuma.ValueNotSu pported | InvalidParam.CpuOptionsNuma | %s |
| 403 | InvalidVSwitchId.IpI nvalid | InvalidVSwitchId.IpInvalid | %s |
| 403 | Forbidden.RegionId | Forbidden.RegionId | %s |
| 403 | DEPLOYMENT SET I _ _ NSTANCE QUOTA F _ _ ULL | QuotaExceed.DeploymentSetIns tanceQuotaFull | The instance quota in one deployment set exceeded. |
| 403 | Abs.InvalidInstance ChargeType.WithDel etionProtection | InvalidChargeType.ValueNotSup ported | Deletion protection is only valid for postPaid instance, not for prePaid or spot instance. |
| 403 | InvalidRegionId.Not Support | InvalidRegion.NotSupport | The specified region does not support byok. |
| 403 | InvalidUserId.NotInA rnsWhiteList | UserNotInTheWhiteList | The user is not in Arns white list. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | CMKNotEnabled | InvalidParameter.KMSKeyId.CMK NotEnabled | The CMK needs to be enabled. |
| 403 | KMSUnauthorized | InvalidParameter.KMSKeyId.KMS Unauthorized | ECS service have no right to access your KMS. |
| 403 | RR307 | SecurityRisk.3DVerification | We have detected a security risk with your default credit or debit card. Please proceed with verification via the link in your email. |
| 403 | USERPROFILECOMPL ETE | OperationDenied | The user profile is not complete; try complete your basic info in account management page. |
| 403 | ORDER.MAYI SYNC _ _ ORDER ERROR _ | Mayi.InternalError | The request processing has failed due to some unknown error. |
| 403 | Invalid.Network.Typ e | InvalidNetworkType | The network type is not support in this region. |
| 403 | ORDER.ACCOUNT S _ TATUS ILLEGAL _ | InvalidAccountStatus | Your account status is invalid, please contact customer service. |
| 403 | InvalidVSwitchId.IpN otEnough | QuotaExceeded.PrivateIpAddres s | %s |
| 403 | Abs.InvalidPerforma nceLevel.ValueMust Lower | OperationDenied.PerformanceLe velNotMatch | The specified DataDisk.n.PerformanceLevel and DataDisk.n.Size do not match. |
| 403 | Abs.InvalidPerforma nceLevel.ValueMust Lower | OperationDenied.PerformanceLe velNotMatch | The specified DataDisk.n.PerformanceLevel and DataDisk.n.Size do not match. |
| 403 | InvalidStorageSetNa me.Malformed | InvalidStorageSetName.Malform ed | Specified parameter StorageSetName is not valid. |
| 403 | InvalidDescription.M alformed | InvalidDescription.Malformed | Specified parameter Description is not valid. |
| 403 | InvalidMaxPartitionN umber.Malformed | InvalidMaxPartitionNumber.Malf ormed | Specified parameter MaxPartitionNumber is not valid. |
| 403 | InvalidParameter.St orageSetPartitionNu mber | InvalidParameter.StorageSetPart itionNumber | Specified parameter StorageSetPartitionNumber is not valid. |
| 403 | InvalidParameter.St orageSetId | InvalidParameter.StorageSetId | Specified parameter StorageSetId is not valid. |
| 403 | InvalidParameter.St orageSetZoneId | InvalidParameter.StorageSetZon eId | Specified parameter StorageSetZoneId is not valid. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | INSTANCE NOT SUP _ _ PORT MULTI GROUP _ _ TYPE _ | EnterpriseGroupLimited.MutliGro upType | The specified instance can't join multi SecurityGroup types. |
| 403 | INSTANCE NOT SUP _ _ PORT ENTERPRISE _ _ GROUP | EnterpriseGroupLimited.Instance Type | The specified instance type doesn't support Enterprise SecurityGroup. |
| 403 | QuotaExceed.Tags | QuotaExceed.Tags | %s |
| 403 | REGION NOT SUPPO _ _ RT SPOT DURATION _ _ INSTANCE _ | OperationDenied.RegionIdNotSu pported | The specified region does not support spot duration instance. |
| 403 | FLAVOR NOT SUPP _ _ ORT SPOT DURATIO _ _ N INSTANCE _ | OperationDenied.FlavorNotSupp orted | Flavor not support spot duration instance. |
| 403 | TIMESTAMP NOT SU _ _ PPORT SPOT DURA _ _ TION INSTANCE _ | OperationDenied.TimestampNot Supported | Timestamp not support spot duration instance. |
| 403 | Forbid.EcsCreate | OperationDenied.PaygNotAvaila ble | Pay-as-you-go instance is not available now. |
| 403 | Forbid.VmCreate | OperationDenied.PrepayNotAvail able | Prepay instance is not available now. |
| 403 | Abs.BidCreateResou rceForbid | OperationDenied.BidOwnResour ce | Bid user can not own resource. |
| 403 | CloudSSD.NotSuppo rted | OperationDenied.CloudSSDNotS upported | The specified available zone does not offer the cloud ssd _ disk, use cloud essd instead. _ |
| 403 | ELASTIC QUOTA EX _ _ CEEDED | QuotaExceed.ElasticQuota | The request failed due to elastic quota check, details as follows: %s. |
| 403 | ECS INSTANCE TYP _ _ E QUOTA EXCEEDE _ _ D | QuotaExceed.ElasticQuota | The number of the specified ECS instances has exceeded the quota of the specified instance type.Please sign-on to Alibaba Cloud Console, and submit a quota increase application. |
| 403 | ECS VCPU QUOTA _ _ _ EXCEEDED | QuotaExceed.ElasticQuota | The number of vCPUs assigned to the ECS instances has exceeded the quota in the zone.Please sign-on to Alibaba Cloud Console, and submit a quota increase application. |
| 403 | ECS INSTANCE TYP _ _ E OR VCPU QUOTA _ _ _ EXCEEDED _ | QuotaExceed.ElasticQuota | The number of the specified ECS instances has exceeded the quota of the specified instance type, or the number of vCPUs assigned to the ECS instances has exceeded the quota in the zone.Please go to submit a quota increase application. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | DISK CAPACITY QU _ _ OTA FULL _ | QuotaExceeded.PostpaidDataDis kCapacity | The quota of postpaid data disk capacity exceeds. |
| 403 | InvalidImageFamily. MissingAvailableIma ge | InvalidImageFamily.MissingAvail ableImage | There is no available image related to the specified image family. |
| 403 | InvalidRegionId.Not SupportEncryptAlgo rithm | InvalidRegionId.NotSupportEncr yptAlgorithm | The current region does not support creating encrypted disks with EncryptAlgorithm. |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | InvalidOperation.ResourceMana gedByCloudProduct | %s |
| 403 | InvalidDiskSize.TooS mall | InvalidDiskSize.TooSmall | Specified disk size is too small when choosing PL0 of cloud essd. _ |
| 403 | InvalidUserId.NotInA rnsWhiteList | UserNotInTheWhiteList | The user is not in Arns white list. |
| 403 | InvalidManagedPriv ateSpaceId.Dedicate dHostIdConflict | InvalidManagedPrivateSpaceId.D edicatedHostIdConflict | ManagedPrivateSpaceId and DedicatedHostId cannot be specified at the same time. |
| 403 | InvalidManagedPriv ateSpaceId.Tenancy Conflict | InvalidManagedPrivateSpaceId.T enancyConflict | ManagedPrivateSpaceId and Tenancy cannot be specified at the same time. |
| 403 | InvalidParameter.In validEniQueueNumb er | InvalidParameter.InvalidEniQueu eNumber | %s |
| 403 | InvalidOperation.Ma xEniQueueNumberE xceeded | InvalidOperation.MaxEniQueueN umberExceeded | %s |
| 403 | InvalidOperation.Exc eedInstanceTypeQu eueNumber | InvalidOperation.ExceedInstance TypeQueueNumber | %s |
| 403 | Abs.InvalidIspType.V alueNotSupported | InvalidIspType.ValueNotSupport ed | %s |
| 403 | Abs.UnsupportedIsp ChargeType | UnsupportedIspChargeType | %s |
| 403 | Abs.UnsupportedIsp ClassicNetwork | UnsupportedIspClassicNetwork | %s |
| 403 | Abs.InvalidIspBandw idthOut | InvalidIspBandwidthOut | %s |
| 403 | Abs.UnsupportedIsp NetworkChargeType | UnsupportedIspNetworkChargeT ype | %s |
| 403 | Abs.InvalidIspUID | InvalidIspUID | %s |
| 403 | Abs.UnsupportedIsp Region | UnsupportedIspRegion | %s |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 403 | IMAGE CATEGORY _ _ NOT SUPPORT _ | DeleteWithInstance.Conflict | The specified image is from the image market, you cannot set DeleteWithInstance attribute to false. |
| 403 | PARAMETER GROUP _ TYPE MUST BE EN _ _ _ _ TERPRISE | Forbidden.OnlySupportEnterpris eGroup | %s |
| 403 | HibernationConfigur ed.Instance.Operati onForbidden | HibernationConfigured.Instance OperationForbidden | The operation is not permitted due to limit of the hibernation configured instance. |
| 403 | DISK NUMBER EXCE _ _ EDED | InstanceDiskLimitExceeded | The amount of the disk on instance reach its limits. |
| 403 | INSTANCE TYPE NO _ _ T SUPPORT DISK C _ _ _ ATEGORY | InvalidInstanceType.NotSupport DiskCategory | The instanceType of the specified instance does not support this disk category. |
| 403 | CONFIDENTIAL COM _ PUTING MODE IN IN _ _ _ VITE ONLY TESTING _ _ | InvalidOperation.ConfidentialCo mputingModeInInviteOnlyTestin g | The specified confidential computing mode is in invite only testing: %s. |
| 403 | InvalidOperation.Inv alidNetworkInterfac eId | InvalidOperation.InvalidNetworkI nterfaceId | %s |
| 403 | InvalidOperation.Re gionNotSupportNet workInterfaceId | InvalidOperation.RegionNotSupp ortNetworkInterfaceId | The specific region does not support network interface id. |
| 403 | InvalidEniId.NotFoun d | InvalidEniId.NotFound | %s |
| 403 | DISK CATEGORY NO _ _ T SUPPORT SNAPSH _ _ OT ENCRYPT _ | NotSupportSnapshotEncrypted. DiskCategory | The specified disk category does not support creating encrypted system disks or creating encrypted data disks from snapshots. Check the DiskCategory or Encrypted parameter, or check your account for default encryption settings. |
| 403 | InvalidEncrypted.No tMatchDiskDefaultE ncryption | InvalidEncrypted.DefaultEncrypti onUnsupported | The specified parameter Encrypted must be true when default encryption is enabled. |
| 403 | InvalidOperation.Pu blicIpAddressNoStoc k | InvalidOperation.PublicIpAddress NoStock | The public IP address for the specified Region or ChargeType of the instance is out of stock. Please try another Region or ChargeType. |
| 403 | ELASTIC QUOTA RE _ _ CORD NOT FOUND _ _ | QuotaExceed.ElasticQuota | The request failed due to elastic quota check, details as follows: %s. |
| 403 | ELASTIC QUOTA EX _ _ CEEDED | QuotaExceed.ElasticQuota | The request failed due to elastic quota check, details as follows: %s. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 403 | AclLimitExceed | AclLimitExceed | %s |
| 403 | IMAGE NOT AVAILA _ _ BLE | OperationDenied.ImageNotValid | The specified image is not available, please check the status of the image. |
| 403 | CREATE ENCRYPTE _ D KEY FAIL _ _ | InvalidParameter.DataEncrypted KeyCreateFailed | Create kms data encrypted key fail. If you need further assistance, you can contact the KMS Technical Support. |
| 403 | INVALID CPU OPTIO _ _ NS HT _ | InvalidParameter.CpuOptionsThr eadsPerCore | The specified parameter CpuOptions.ThreadsPerCore is not valid. |
| 403 | INVALID CPU OPTIO _ _ NS CORE _ | InvalidParameter.CpuOptionsCor e | The specified parameter CpuOptions.Core is not valid. |
| 403 | INSTANCE TYPE NO _ _ T SUPPORT MODIFY _ _ HT _ | InvalidInstanceType.CpuOptions ThreadsPerCoreUnsupported | The current instance type does not support setting or modifying the CpuOptions.ThreadsPerCore parameter. |
| 403 | INVALID CPU OPTIO _ _ NS NUMA _ | InvalidParameter.CpuOptionsNu ma | The specified parameter CpuOptions.Numa is not valid. |
| 404 | InvalidDedicatedBlo ckStorageClusterId. NotExist | InvalidStorageClusterId.NotExist | The specified StorageClusterId does not exist in current region. |
| 404 | -140 | InvalidRegionId.NotFound | The RegionId provided does not exist in our records. |
| 404 | NOT AVAILABLE IZ _ _ _ SPECIFY EXISTS _ | InvalidZoneId.NotFound | The specified zoneId does not exist. |
| 404 | Abs.InvalidSecurityG roupId | InvalidSecurityGroupId | The specified SecurityGroupId is invalid or does not exist. |
| 404 | -560 | InvalidSecurityGroupId.NotFoun d | The SecurityGroupId provided does not exist in our records. |
| 404 | ECS SYSTEM SNAPS _ _ HOT QUERY ERROR _ _ | InvalidDataDiskSnapshotId.NotF ound | The specified parameter "DataDisk.n.SnapshotId" is not valid. |
| 404 | -910 | InvalidDataDiskSnapshotId.NotF ound | The specified parameter "DataDisk.n.SnapshotId" is not valid. |
| 404 | -150 | InvalidClusterId.NotFound | The ClusterId provided does not exist in our records. |
| 404 | ECS BIZ IZ INVALID _ _ _ | InvalidZoneId.NotFound | The ZoneId provided does not exist in our records. |
| 404 | ECS SYSTEM IZ QU _ _ _ ERY ERROR _ | InvalidZoneId.NotFound | The ZoneId provided does not exist in our records. |
| 404 | IZ INVALID _ | InvalidZoneId.NotFound | The ZoneId provided does not exist in our records. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 404 | ECS BIZ SNAPSHOT _ _ INVALID _ | InvalidDataDiskSnapshotId.NotF ound | The specified parameter "DataDisk.n.SnapshotId" is not valid. |
| 404 | ECS SYSTEM SNAPS _ _ HOT QUERY ERROR _ _ | InvalidDataDiskSnapshotId.NotF ound | The specified parameter "DataDisk.n.SnapshotId" is not valid. |
| 404 | VSW NOT EXIST _ _ | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 404 | USER NOT ALLOW _ _ _ BUY COMMODITY _ | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 404 | VPC VSWITCHID NO _ _ T EXISTS _ | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 404 | InvalidVSwitchId.Not Found | InvalidVSwitchId.NotFound | %s |
| 404 | VSW NOT EXIST _ _ | InvalidVSwitchId.NotFound | Specified virtual switch does not exist. |
| 404 | Abs.ImageNotFound | InvalidImageId.NotFound | The specified ImageId does not exist. |
| 404 | Abs.ImageNotFound | InvalidImageId.NotFound | The specified ImageId does not exist. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL 1 _ _ _ 00199815 | IoOptimized.NotSupported | The specified instancetype is not support IoOptimized instance. |
| 404 | Abs.InvalidInstance ChargeType.ValueN otSupported | InvalidInstanceChargeType.NotF ound | The InstanceChargeType does not exist in our records. |
| 404 | DependencyViolatio n.IoOptimized | DependencyViolation.IoOptimize d | The specified instancetype must be IoOptimized instance. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL N _ _ _ OCARD | PaymentMethodNotFound | No payment method has been registered on the account. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL N _ _ _ OCARD | PaymentMethodNotFound | No payment method has been registered on the account. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL N _ _ _ OCARD | PaymentMethodNotFound | No payment method has been registered on the account. |
| 404 | -101 | HOSTNAME ILLEGAL _ | The specified parameter HostName is not valid. |
| 404 | SYSTEM DISK SIZE _ _ _ MUST LARGE THAN _ _ IMAGE _ | InvalidSystemDiskSize.LessThan ImageSize | The specified parameter SystemDisk.Size is less than the image size. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | SYSTEM DISK SIZE _ _ _ MUST LARGE THAN _ _ IMAGE _ | InvalidSystemDiskSize.LessThan ImageSize | The specified parameter SystemDisk.Size is less than the image size. |
| 404 | InvalidSystemDiskSi ze.LessThanMinSize | InvalidSystemDiskSize.LessThan MinSize | The specified parameter SystemDisk.Size is less than the min size. |
| 404 | InvalidSystemDiskSi ze.MoreThanMaxSiz e | InvalidSystemDiskSize.MoreTha nMaxSize | The specified parameter SystemDisk.Size is more than the max size. |
| 404 | ECS BIZ IMAGE NO _ _ _ T FOUND _ | OperationDenied.ImageNotValid | The specified Image is disabled or is deleted. |
| 404 | ECS CREATE ONE L _ _ _ IMIT BY SYNC _ _ | OperationDenied.CreatingConflic t | Another Instance has been creating. |
| 404 | NOT AVAILABLE IZ _ _ _ SPECIFY EXISTS _ | InvalidZoneId.NotFound | The specified zoneId does not exist. |
| 404 | InvalidKeyPairName. NotFound | InvalidKeyPairName.NotFound | The specified parameter KeyPairName does not exist in our records. |
| 404 | InvalidResourceGro up | InvalidResourceGroup.NotFound | The ResourceGroup provided does not exist in our records. |
| 404 | InvalidRamRole.Not Found | InvalidRamRole.NotFound | The specified parameter "RAMRoleName" does not exist. |
| 404 | InvalidLaunchTempl ate.NotFound | InvalidLaunchTemplate.NotFoun d | %s |
| 404 | InvalidLaunchTempl ateVersion.NotFoun d | InvalidLaunchTemplateVersion.N otFound | %s |
| 404 | VSWITCH NOT EXIS _ _ T | InvalidVSwitchId.NotExist | %s |
| 404 | ImageNotFound | InvalidMarketImage.NotFound | The specified marketplace image does not exist, please change the imageId and try again. |
| 404 | -1023003 | DeploymentSet.NotFound | The specified deployment set does not exist. |
| 404 | -1023003 | DeploymentSet.NotFound | The specified deployment set does not exist. |
| 404 | InvalidParameter.De ploymentSetGroupN o | InvalidParameter.DeploymentSe tGroupNo | Parameter DeploymentSetGroupNo is invalid. |
| 404 | KMSKeyIdNotFound | InvalidParameter.KMSKeyId.NotF ound | The specified KMSKeyId does not exist. |
| 404 | InvalidSecurityGrou pId.NotFound | InvalidSecurityGroupId.NotFoun d | %s |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 404 | Abs.InvalidPortable. ValueNotSupported | InvalidDiskIds.NotPortable | The specified DiskId is not portable. |
| 404 | Abs.SnapshotPolicy NotFound | InvalidAutoSnapshotPolicyId.Not Found | Specified parameter AutoSnapshotPolicyId not found. |
| 429 | Throttle.Resource | Throttling.Resource | The request throttle by resource operation. |
| 500 | PRICE.HSF TIMEOUT _ ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | LX CREATE ORDER _ _ _ FAILED | InternalError | The request processing has failed due to some unknown error. |
| 500 | Constraint.Forbidde n | InternalError | The request processing has failed due to some unknown error. |
| 500 | Abs.InnerServiceFail ed | InternalError | The request processing has failed due to some unknown error. |
| 500 | KMS.Service.Unavail able | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | LxCheckService.Not Pass | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | CreditAndWhitelistC heck.NotPass | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | SYSTEM.SYSTEM ER _ ROR | InternalError | The request processing has failed due to some unknown error. |
| 500 | SYSTEM.SALE VALID _ ATE UNEXPECTED E _ _ RROR | InternalError | The request processing has failed due to some unknown error. |
| 500 | PRICE.PRICING HSF _ _ TIMEOUT ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | -1023102 | InternalError | The request processing has failed due to some unknown error. |
| 500 | PRICE.WAN HUA TO _ _ NG SYS _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | Trade Complete Art _ _ icle ERROR _ | InternalError | The request processing has failed due to some unknown error. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | INSERT ECS DEVICE _ _ FAILED _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | SDK.ServerUnreach able | InternalError | The request processing has failed due to some unknown error. |
| 500 | Trade Sync Create _ _ _ Sub ERROR _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | SYSTEM.SALE VALID _ ATE NO SPECIFIC C _ _ _ ODE FAILED _ | InternalError | The request processing has failed due to some unknown error. |
| 500 | RAMSerivceUnavaila bleTemporary | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | SYSTEM.UNKNOWN _ ERROR | InternalError | The request processing has failed due to some unknown error. |
| 500 | ORDER.DEDUCE AC _ TIVITY INVENTORY _ _ ERROR | InternalError | The request processing has failed due to some unknown error. |
| 500 | PRICE.HSF TIMEOUT _ ERROR _ | InternalError | The request processing has failed due to some unknown error. |

##### StartInstance

调用StartInstance启动一台ECS实例，接口调用成功后实例进入启动中状态。

**接口说明**

调用该接口时，您需要注意：

| 为已停止（ | Stopped |  |
|---|---|---|
| OperationLocks |  | 中 |

例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartInstance | 系统规定参数。取值：StartInstance |
| InstanceId | String | 是 | i- bp67acfmxazb4p **** | 指定启动的实例ID。 |

云服务器ECS

| InitLocalDisk | Boolean | 否 | true | 适用于实例规格族d1或者i2等包含本地盘的实例。当d1或者i2的本地盘出现故障时，可通过此参数指定启动实例时，是否将实例恢复到最初的健康状态。取值范围： true：将实例恢复到最初的健康状态，实例原有本地盘中的数据将会丢失。 false（默认）：不做任何处理，维持现状。 |
|---|---|---|---|---|
| DryRun | Boolean | 否 | true | 是否只预检查此次请求。取值范围： true：仅检查此次请求，不会启动实例。 检查项包括AccessKey是否有效、RAM用户的授权情况和是否填写了必需参数。如果检查不通过，则返回对应错误。如果检查通过，会返回错误码 DryRunOperation。 false（默认）：发送正常请求，请求通过检查后，返回2XX HTTP状态码并直接启动实例。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&InstanceId=i-bp67acfmxazb4p**** &InitLocalDisk=true
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

云服务器ECS

| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
|---|---|---|---|
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 403 | InsufficientBalance | Your account does not have enough balance. | 账户余额不足，请先充值再操作。 |
| 500 | InstanceNotReady | The specified instance is not ready for use | 暂时无法连接指定的实例，请稍后再试。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | DiskError | IncorrectDiskStatus. | 指定的磁盘状态不合法。 |
| 403 | InstanceExpired | The postPaid instance has been expired.Please ensure your account have enough balance. | 按量付费的实例已过期。请确保您的帐户有足够的余额。 |
| 403 | InstanceExpired | The prePaid instance has been expired. | 包年包月实例已到期。 |
| 403 | InstanceNotReady | The specified instance is not ready for use. | 该资源目前的状态不支持此操作，请您等待一段时间再进行操作，并确认实例目前状态与操作是否冲突。 |
| 403 | DiskInArrears | The specified operation is denied as your disk has expired. | 磁盘欠费过期。 |
| 403 | OperationDenied.No Stock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. | 库存不足。 |
| 403 | OperationDenied.Sp otPriceLowerThanPu blicPrice | The spot instance price is lower than public price. | 抢占式实例的竞价价格不能低于公开的价格。 |
| 403 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### StopInstance

调用StopInstance停止一台运行中（Running）的ECS实例。成功调用接口后，实例从停止中（Stopping）变成已停止（Stopped）状态。

**接口说明**

云服务器ECS 被安全控制的ECS实例的OperationLocks参数包含"LockReason": "security"时，不能停止实例。 停止本地SSD型实例规格族： 成功调用接口后，本地盘上的数据会被清空，您需要通过应用层的数据冗余保证数据可用性。 ECS自动忽略其他实例规格族的 `ConfirmStop` 请求参数。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StopInstance | 系统规定参数。取值：StopInstance |
| InstanceId | String | 是 | i- bp67acfmxazb4p h*** | 指定的实例ID。 |
| ForceStop | Boolean | 否 | false | 停止实例时的是否强制关机策略。取值范围： true：强制关机。 false（默认）：正常关机流程。 |
| DryRun | Boolean | 否 | true | 是否只预检此次请求。取值范围： true：发送检查请求，不会停止实例。检查项包括是否填写了必需参数、请求格式、业务限制和ECS库存。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认）：发送正常请求，通过检查后直接停止实例。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1C488B66-B819- 4D14-8711- C4EAAA13AC01 | 请求ID。 |

**示例**

请求示例

```
&InstanceId=i-bp67acfmxazb4ph*** &ConfirmStop=true &ForceStop=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>1C488B66-B819-4D14-8711-C4EAAA13AC01</RequestId>
```

云服务器ECS `JSON` 格式

```json
{
    "RequestId": "1C488B66-B819-4D14-8711-C4EAAA13AC01"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 403 | DiskError | IncorrectDiskStatus | 指定的磁盘状态不合法。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | InstanceType.Param eterMismatch | The input parameter ConfirmStop must be true when an instance have localstorage. | 当实例使用本地存储时，输入参数 ConfirmStop必须为Ture。 |
| 403 | InstanceExpiredOrIn Arrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). | 包年包月实例已过期，请您续费后再进行操作。 |
| 403 | InvalidInstanceId.No tSupport | Classic network Instance does not support this operation. | 经典网络类型的实例不支持此操作。 |
| 403 | InvalidInstanceId.No tSupport | Pre pay instance does not support this operation. | 包年包月实例不支持该操作。 |
| 403 | InvalidInstanceId.No tSupport | Local disk instance does not support this operation. | 本地盘实例不支持该操作。 |
| 403 | InvalidInstanceId.No tSupport | Spot instance does not support this operation. | 抢占式实例不支持该操作。 |
| 403 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### RebootInstance

云服务器ECS 当一台ECS实例处于运行中（Running）状态时，调用RebootInstance可以重启这台实例。

**接口说明**

| 为运行中（ Running ） 进入启动中（ Starting | Running |  |  | ） |
|---|---|---|---|---|
|  |  | Starting |  |  |
| ForceStop |  |  | ），强制重 |  |

盘的数据。 被安全控制的ECS实例的OperationLocks参数包含"LockReason": "security"时，不能重启实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RebootInstance | 系统规定参数。取值：RebootInstance |
| InstanceId | String | 是 | i- bp67acfmxazb4p h*** | 指定实例的ID。 |
| ForceStop | Boolean | 否 | false | 重启ECS实例前，是否强制关机。取值范围： true：强制关机。相当于典型的断电操作，所有未写入存储设备的缓存数据会丢失。 false（默认）：正常关机。 |
| DryRun | Boolean | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会重启实例。检查项包括是否填写了必需参数、请求格式、业务限制和ECS库存。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认）：发送正常请求，通过检查后直接重启实例。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&InstanceId=i-bp67acfmxazb4ph*** &ForceStop=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <RequestId>F2E2C40D-AB09-45A1-B5C5-EB9F5C4E4E4A</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "F2E2C40D-AB09-45A1-B5C5-EB9F5C4E4E4A"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 403 | DiskError | IncorrectDiskStatus. | 指定的磁盘状态不合法。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | InstanceExpiredOrIn Arrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). | 包年包月实例已过期，请您续费后再进行操作。 |
| 403 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### DeleteInstance

**接口说明**

释放后，实例所使用的物理资源都被回收，相关数据全部丢失且不可恢复。 挂载在实例上的云盘：

| 置了 | DeleteWithInstance=true |
|---|---|
| DeleteAutoSnapshot=false |  |
| DeleteAutoSnapshot=true |  |

云服务器ECS 仍旧保留云盘的手动快照。 被安全控制的ECS实例的OperationLocks参数包含"LockReason": "security"时，即使云盘的 `DeleteWithInstance` 的属性为 `false` ，系统会忽略这个属性而释放云盘。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteInstance | 系统规定参数，取值：DeleteInstance。 |
| InstanceId | String | 是 | i- bp1g6zv0ce8ogh u7k*** | 实例ID。 |
| Force | Boolean | 否 | false | 是否强制释放运行中（ Running ）的实例。 true：强制释放运行中（ Running ） 的实例。强制释放相当于断电，实例内存以及存储中的临时数据都会被擦除，无法恢复。 false（默认值）：正常释放实例，此时实例必须处于已停止（ Stopped ）状态。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&InstanceId=i-bp1g6zv0ce8oghu7k**** &Force=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>928E2273-5715-46B9-A730-238DC996A533</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "928E2273-5715-46B9-A730-238DC996A533"
}
```

云服务器ECS

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 403 | ChargeTypeViolatio n | The operation is not permitted due to charge type of the instance. | 付费方式不支持该操作，请您检查实例的付费类型是否与该操作冲突。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 400 | DependencyViolatio n.SLBConfiguring | Specified operation is denied as your instance is using by another product. | 实例被SLB引用，且SLB正在配置。 |
| 400 | DependencyViolatio n.RouteEntry | Specified instance is used by route entry. | 当前专有网络VPC还存在未删除的自定义路由规则，删除失败。 |
| 400 | InvalidParameter | The input parameter InstanceId is invalid. | 指定的InstanceId不合法，请您检查 InstanceId是否正确，且存在。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | IncorrectInstanceSta tus.Initializing | The specified instance status does not support this operation. | 实例正在初始化中，暂时无法释放请稍后重试。 |
| 403 | IncorrectInstanceSta tus | The specified instance is still attached by volumes. | 指定的实例上存在数据卷。 |
| 403 | InvalidOperation.Del etionProtection | %s | 该操作无效，请先取消该实例的释放保护。 |
| 403 | InvalidOperation.Eni Linked | %s | 实例的当前弹性网卡关联了其他弹性网卡，导致操作无效。需要解除关联后才能从实例解绑。 |

##### AttachInstanceRamRole

调用AttachInstanceRamRole为一台或多台ECS实例授予实例RAM角色。如果实例已有RAM角色，则报错提示您不能附加新的角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AttachInstanceRa mRole | 系统规定参数，取值： AttachInstanceRamRole。 |

云服务器ECS

| InstanceIds | String | 是 | [“i- bp14ss25xca5ex 1u****”, “i- bp154z5o1qjalfse ****”, “i- bp10ws62o04ubh vi****”…] | 实例ID。取值可以由多个实例ID组成一个 JSON数组，最多支持100个ID，ID之间用半角逗号（,）隔开。 |
|---|---|---|---|---|
| RamRoleName | String | 是 | RamRoleTest | 实例RAM角色名称。您可以使用 RAM API ListRoles查询您已创建的实例RAM角色。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AttachInstance RamRoleResult s | Array of AttachInstance RamRoleResult |  | 由实例RAM角色类型 （AttachInstanceRamRoleResult）组成的信息集。 |
| AttachInstance RamRoleResult |  |  |  |
| Code | String | 200 | 判断是否成功授予实例RAM角色。返回值为200表示成功授予，返回其他值表示授予失败，失败原因参见错误码。 |
| InstanceId | String | i- bp10ws62o04ubhvi* *** | 实例ID。 |
| Message | String | success | 判断是否成功授予实例RAM角色。返回值为 Success表示成功授予，返回其他值表示授予失败，失败原因参见错误码。 |
| Success | Boolean | true | 是否成功授予实例RAM角色。 true：授予实例RAM角色成功。 false：授予实例RAM角色失败。 |
| FailCount | Integer | 0 | 授予实例RAM角色的失败个数。 |
| RamRoleName | String | RamRoleTest | 实例RAM角色的名称。 |
| RequestId | String | D9553E4C-6C3A- 4D66-AE79- 9835AF705639 | 请求ID。 |
| TotalCount | Integer | 1 | 授予的实例RAM角色总个数。 |

**示例**

云服务器ECS 请求示例

```
https://ecs.example.com/?Action=AttachInstanceRamRole &InstanceIds=["i-bp10ws62o04ubhvi****"] &RamRoleName=RamRoleTest &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>E6352369-5C2B-41CD-AB50-471550C8F674</RequestId>
                   <InstanceId>i-bp10ws62o04ubhvi****</InstanceId>
                   <Code>200</Code>
                   <Message>success</Message>
      <TotalCount>1</TotalCount>
      <FailCount>0</FailCount>
      <RamRoleName>RamRoleTest</RamRoleName>
```

`JSON` 格式

```json
{
    "RequestId": "D9553E4C-6C3A-4D66-AE79-9835AF705639",
            {
                "Message": "success",
                "InstanceId": "i-bp10ws62o04ubhvi****",
                "Code": "200"
            }
```

]

```json
    },
    "TotalCount": 1,
    "FailCount": 0,
    "RamRoleName": "RamRoleTest"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInstanceIds.M alformed | The specified instanceIds are not valid. | 指定的多个InstanceId不合法。 |
| 404 | InvalidInstanceId.No tFound | The specified instanceId does not exist | 指定的实例不存在，请您检查实例ID 是否正确。 |

云服务器ECS

| 403 | InvalidNetworkType. MismatchRamRole | Ram role cannot be applied to instances of Classic network type. | 实例RAM角色不能被用于经典网络类型的实例，RAM角色只能使用在VPC 类型的实例上。 |
|---|---|---|---|
| 403 | InvalidUser.PassRole Forbidden | The RAM user does not have the privilege to pass a RAM role. | 该RAM用户无权传递RAM角色。 |
| 404 | InvalidRamRole.Not Found | The specified RAMRoleName does not exist. | 指定的RamRoleName不存在。 |
| 404 | InvalidRamRole.Not EcsRole | The specified ram role is not authorized for ecs, please check your role policy. | 指定的RAM角色无权使用ECS，请检查您的角色策略。 |

##### DetachInstanceRamRole

调用DetachInstanceRamRole回收一台或多台ECS实例的实例RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DetachInstanceR amRole | 系统规定参数。取值： DetachInstanceRamRole |
| InstanceIds | String | 是 | ["i- bp67acfmxazb4p ****", "i- bp67acfmxazb4p ****", "i- bp67acfmxazb4p ****"…] | 指定收回的实例ID。取值可以由多个实例ID 组成一个JSON数组，最多支持100个ID，ID 之间用半角逗号（,）隔开。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| RamRoleName | String | 否 | RamRoleTest | 收回赋予了某一实例RAM角色的所有ECS实例。您可以使用RAM API ListRoles查询您已创建的实例RAM角色。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DetachInstance RamRoleResult s | Array of DetachInstance RamRoleResult |  | 由实例RAM角色类型 （DetachInstanceRamRoleResult）组成的信息集。 |
| DetachInstance RamRoleResult |  |  |  |
| Code | String | 200 | 判断是否成功收回实例RAM角色。返回值为200表示成功收回，返回其他值表示收回失败，失败原因参见错误码。 |

云服务器ECS

| InstanceId | String | i- bp67acfmxazb4p*** * | 准备收回实例RAM角色的ECS实例。 |
|---|---|---|---|
| InstanceRamRo leSets | Array of InstanceRamRo leSet |  | 实例的RAM角色集合。 |
| InstanceRamRo leSet |  |  |  |
| InstanceId | String | i- bp67acfmxazb4p*** * | 实例ID。 |
| RamRoleName | String | RamRoleTest | 收回实例RAM角色的名称。 |
| Message | String | Success | 判断是否成功收回实例RAM角色。返回值为 Success表示成功收回，返回其他值表示收回失败，失败原因参见错误码。 |
| Success | Boolean | true | 是否成功回收了指定的实例角色。 |
| FailCount | Integer | 0 | 收回失败的实例RAM角色的个数。 |
| RamRoleName | String | RamRoleTest | 收回实例RAM角色的名称。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 1 | 收回的实例RAM角色的总个数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DetachInstanceRamRole &InstanceIds=["i-bp67acfmxazb4p****"] &RegionId=cn-qingdao-env17-d01 &RamRoleName=RamRoleTest
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <TotalCount>1</TotalCount>
                  <Message>success</Message>
                  <InstanceId>i-bp16qng6jnvt6g7t****</InstanceId>
                  <Code>200</Code>
                  <InstanceRamRoleSets>
                        <InstanceId>i-bp16qng6jnvt6g7t****</InstanceId>
                        <RamRoleName>RamRoleTest</RamRoleName>
                  </InstanceRamRoleSets>
      <RequestId>14D5B163-CE6C-4489-B979-DBE5D0495A63</RequestId>
      <RamRoleName></RamRoleName>
      <FailCount>0</FailCount>
```

`JSON` 格式

```json
{
 "TotalCount": 1,
   {
    "Message": "success",
    "InstanceId": "i-bp16qng6jnvt6g7t****",
    "Code": "200",
    "InstanceRamRoleSets": {
     "InstanceId": "i-bp16qng6jnvt6g7t****",
     "RamRoleName": "RamRoleTest"
    }
   }
```

]

```json
 },
 "RequestId": "14D5B163-CE6C-4489-B979-DBE5D0495A63",
 "RamRoleName": "",
 "FailCount": 0
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInstanceIds.M alformed | The specified instanceIds are not valid. | 指定的多个InstanceId不合法。 |
| 403 | InvalidNetworkType. MismatchRamRole | Ram role cannot be applied to instances of Classic network type. | 实例RAM角色不能被用于经典网络类型的实例，RAM角色只能使用在VPC 类型的实例上。 |
| 403 | InvalidUser.PassRole Forbidden | The RAM user does not have the privilege to pass a RAM role. | 该RAM用户无权传递RAM角色。 |

云服务器ECS

##### DescribeInstanceStatus

**接口说明**

该接口同时可用于获取实例列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInstance Status | 系统规定参数。取值： DescribeInstanceStatus |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| InstanceId.N | RepeatLi st | 否 | i- bp1j4i2jdf3owlhe **** | 一个或者多个ECS实例ID。N的取值范围： 1~100，多个取值使用重复列表的形式。 |
| ZoneId | String | 否 | cn-qingdao- env17- amtest11001-a | 实例所属可用区。 |
| ClusterId | String | 否 | cls- bp67acfmxazb4p **** | 实例所属的集群ID。 |
| PageNumber | Integer | 否 | 1 | 实例状态列表的页码。 起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。取值范围： 1~50 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceStatus es | Array of InstanceStatus |  | 实例状态集类型（InstanceStatus）。 |
| InstanceStatus |  |  |  |
| InstanceId | String | i- bp1j4i2jdf3owlhe*** * | 实例ID。 |
| Status | String | Running | 实例状态。 |

云服务器ECS

| PageNumber | Integer | 1 | 实例列表的页码。 |
|---|---|---|---|
| PageSize | Integer | 1 | 输入时设置的每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 58 | 实例总个数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeInstanceStatus &RegionId=cn-qingdao-env17-d01 &PageSize=1 &PageNumber=1 &InstanceId.1=i-bp1j4i2jdf3owlhe****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <PageNumber>1</PageNumber>
      <InstanceStatuses>
            <InstanceStatus>
                  <Status>Running</Status>
                  <InstanceId>i-bp1j4i2jdf3owlhe****</InstanceId>
            </InstanceStatus>
      </InstanceStatuses>
      <TotalCount>58</TotalCount>
      <PageSize>1</PageSize>
      <RequestId>746C3444-9A24-4D7D-B8A8-DCBF7AC8BD66</RequestId>
```

`JSON` 格式

```json
{
 "PageNumber": 1,
 "InstanceStatuses": {
  "InstanceStatus": [
   {
    "Status": "Running",
    "InstanceId": "i-bp1j4i2jdf3owlhe****"
   }
```

]

```json
 },
 "TotalCount": 58,
 "PageSize": 1,
 "RequestId": "746C3444-9A24-4D7D-B8A8-DCBF7AC8BD66"
}
```

云服务器ECS

##### DescribeInstances

**接口说明**

请求参数的作用类似于一个过滤器，过滤器为逻辑与（AND）关系。如果某一参数为空，则过滤器不起作用。 但是参数InstanceIds如果是一个空JSON数组，则视为该过滤器有效，且返回空。 如果您使用的是RAM用户账号或者RAM角色，当用户或者角色缺乏接口权限时，将会返回空列表。您可以在请求中加入 `DryRun` 参数，判断是否因权限问题导致的空列表现象。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInstance s | 系统规定参数。取值：DescribeInstances |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| VpcId | String | 否 | v- bp67acfmxazb4p **** | 专有网络VPC ID。 |
| VSwitchId | String | 否 | vsw- bp67acfmxazb4p **** | 交换机ID。 |
| ZoneId | String | 否 | cn-qingdao- env17- amtest11001-a | 可用区ID。 |
| InstanceNetworkT ype | String | 否 | vpc | 实例网络类型。取值范围： classic：经典网络 vpc：专有网络VPC |
| SecurityGroupId | String | 否 | sg- bp67acfmxazb4p **** | 实例所属的安全组。 |
| InstanceIds | String | 否 | ["i- bp67acfmxazb4p ****", "i- bp67acfmxazb4p ****", … "i- bp67acfmxazb4p ****"] | 实例ID。取值可以由多个实例ID组成一个 JSON数组，最多支持100个ID，ID之间用半角逗号（,）隔开。 |
| PageNumber | Integer | 否 | 1 | 实例状态列表的页码。 起始值：1。 默认值：1。 |

云服务器ECS

| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。 最大值：100。 默认值：10。 |
|---|---|---|---|---|
| InnerIpAddresses | String | 否 | ["10.1.1.1", "10.1.2.1", … "10.1.10.1"] | 经典网络类型实例的内网IP列表。当 InstanceNetworkType=classic时生效， 取值可以由多个IP组成一个JSON数组，最多支持100个IP，IP之间用半角逗号（,）隔开。 |
| PrivateIpAddress es | String | 否 | ["172.16.1.1", "172.16.2.1", … "172.16.10.1"] | VPC网络类型实例的私有IP。当 InstanceNetworkType=vpc时生效，取值可以由多个IP组成一个JSON数组，最多支持 100个IP，IP之间用半角逗号（,）隔开。 |
| PublicIpAddresse s | String | 否 | ["42.1.1.**", "42.1.2.**", … "42.1.10.**"] | 说明该参数暂未支持。 |
| EipAddresses | String | 否 | ["42.1.1.**", "42.1.2.**", … "42.1.10.**"] | 实例的弹性公网IP列表。当 InstanceNetworkType=vpc时该参数生效，取值可以由多个IP组成一个JSON数组， 最多支持100个IP，IP之间用半角逗号（,） 隔开。 |
| InstanceName | String | 否 | test- InstanceName | 实例名称，支持使用通配符*进行模糊搜索。 |
| ImageId | String | 否 | m- bp67acfmxazb4p **** | 镜像ID。 |
| Status | String | 否 | Running | 实例状态。取值范围： Running：运行中 Starting：启动中 Stopping：停止中 Stopped：已停止 |
| LockReason | String | 否 | security | 资源被锁定的原因。 |
| IoOptimized | Boolean | 否 | true | 是否是I/O优化型实例。 |
| Tag.N.Key | String | 否 | TestKey | 实例的标签键。N的取值范围：1~20。 |
| Tag.N.Value | String | 否 | TestValue | 实例的标签值。N的取值范围：1~20。 |
| InstanceType | String | 否 | ecs.g5.large | 实例的规格。 |
| InstanceTypeFam ily | String | 否 | ecs.g5 | 实例的规格族。 |

云服务器ECS

| KeyPairName | String | 否 | test- KeyPairName | 实例使用的SSH密钥对名称。 |
|---|---|---|---|---|
| ResourceGroupId | String | 否 | rg- bp67acfmxazb4p **** | 实例所在的企业资源组ID。 |
| HpcClusterId | String | 否 | hpc- bp67acfmxazb4p **** | 实例所在的HPC集群ID。 |
| RdmaIpAddresses | String | 否 | 10.10.10.102 | HPC实例的Rdma网络IP。 |
| DryRun | Boolean | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会查询资源状况。检查项包括AccessKey是否有效、 RAM用户的授权情况和是否填写了必需参数。如果检查不通过，则返回对应错误。 如果检查通过，会返回错误码 DryRunOperation。 false（默认值）：发送正常请求，通过检查后返回2XX HTTP状态码并直接查询资源状况。 |
| AdditionalAttribut es.N | RepeatLi st | 否 | META OPTIONS _ | 其他属性值。N的取值范围：1~20。 |
| HttpEndpoint | String | 否 | enabled | 是否启用实例元数据的访问通道。取值范围： enabled：启用。 enabled：启用。 默认值：enabled。 |
| HttpTokens | String | 否 | optional | 访问实例元数据时是否强制使用加固模式 （IMDSv2）。取值范围： 不强制使用。 强制使用。设置该取值后，普通模式无法访问实例元数据。 默认值：optional。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Instances | Array of Instance |  | 由Instances组成的数组格式，返回实例的信息。 |
| Instance |  |  |  |
| AutoReleaseTi me | String | test | 说明该参数暂未支持。 |

云服务器ECS

| ClusterId | String | c- bp67acfmxazb4p*** * | 实例所在的集群ID。 说明该参数即将被弃用，为提高兼容性，请尽量使用其他参数。 |
|---|---|---|---|
| Cpu | Integer | 8 | vCPU数。 |
| CpuOptions | Struct |  | CPU配置详情。 |
| CoreCount | Integer | 2 | 物理CPU核心数。 |
| Numa | String | 2 | 分配的线程数。可能值：2。 |
| ThreadsPerCor e | Integer | 4 | CPU线程数。 |
| CreationTime | String | 2017-12-10T04:04Z | 实例创建时间。 |
| CreditSpecificat ion | String | Standard | 修改突发性能实例的运行模式。可能值： Standard：标准模式。 Unlimited：无性能约束模式。 |
| DedicatedHost Attribute | Struct |  | 由专有宿主机ID（DedicatedHostId）和名称 （DedicatedHostName）组成的宿主机属性数组。 |
| DedicatedHost ClusterId | String | dc- bp67acfmxazb4h*** * | 专有宿主机集群ID。 |
| DedicatedHostI d | String | dh- bp67acfmxazb4p*** * | 专有宿主机ID。 |
| DedicatedHost Name | String | test- DedicatedHostName | 专有宿主机名称。 |
| DedicatedInsta nceAttribute | Struct |  | 专有宿主机实例的属性。 |
| Affinity | String | default | 说明该参数暂未支持。 |
| Tenancy | String | default | 实例的宿主机类型是否为专有宿主机。可能值： default：实例的宿主机类型不是专有宿主机。 host：实例的宿主机类型为专有宿主机。 |

云服务器ECS

| DeletionProtect ion | Boolean | false | 说明该参数暂未支持。 |
|---|---|---|---|
| DeploymentSet GroupNo | Integer | 1 | ECS实例绑定部署集分散部署时，实例在部署集中的分组位置。 |
| DeploymentSet Id | String | ds- bp67acfmxazb4p*** * | 部署集ID。 |
| Description | String | This is a description example. | 实例描述。 |
| DeviceAvailabl e | Boolean | true | 实例是否可以挂载数据盘。 |
| EcsCapacityRes ervationAttr | Struct |  | 云服务器ECS的容量预留相关参数。 |
| CapacityReserv ationId | String | cr- bp67acfmxazb4p*** * | 容量预留ID。 |
| CapacityReserv ationPreference | String | cr- bp67acfmxazb4p*** * | 容量预留偏好。 |
| EipAddress | Struct |  | 弹性公网IP绑定信息。 |
| AllocationId | String | i- bp67acfmxazb4p*** * | 弹性公网IP绑定的实例ID。 |
| Bandwidth | Integer | 5 | 弹性公网IP的公网带宽限速，单位为Mbit/s。 |
| InternetCharge Type | String | test | 说明该参数暂未支持。 |
| IpAddress | String | 42.112.17.** | 弹性公网IP。 |
| IsSupportUnass ociate | Boolean | true | 是否可以解绑弹性公网IP。 |
| ExpiredTime | String | 2017-12-10T04:04Z | 说明该参数暂未支持。 |
| GPUAmount | Integer | 4 | 实例规格附带的GPU数量。 |
| GPUSpec | String | NVIDIA V100 | 实例规格附带的GPU类型。 |
| HostName | String | test-HostName | 实例主机名。 |

云服务器ECS

| HpcClusterId | String | hpc- bp67acfmxazb4p*** * | 实例所属的HPC集群ID。 |
|---|---|---|---|
| ImageId | String | m- bp67acfmxazb4p*** * | 实例运行的镜像ID。 |
| InnerIpAddress | List | 10.170.**.*** | 实例的内网IP地址。 |
| InstanceCharge Type | String | test | 说明该参数暂未支持。 |
| InstanceId | String | i- bp67acfmxazb4p*** * | 实例ID。 |
| InstanceName | String | test-InstanceName | 实例名称。 |
| InstanceNetwor kType | String | vpc | 实例网络类型。可能值： classic。 vpc。 |
| InstanceType | String | ecs.g5.large | 实例规格。 |
| InstanceTypeFa mily | String | ecs.g5 | 实例规格族。 |
| InternetCharge Type | String | test | 说明该参数暂未支持。 |
| InternetMaxBa ndwidthIn | Integer | 50 | 网络入带宽最大值，单位为Mbit/s。 |
| InternetMaxBa ndwidthOut | Integer | 5 | 网络出带宽最大值，单位为Mbit/s。 |
| IoOptimized | Boolean | true | 是否为I/O优化型实例。 |
| KeyPairName | String | test-KeyPairName | 密钥对名称。 |
| LocalStorageA mount | Integer | 2 | 实例挂载的本地存储数量。 |
| LocalStorageCa pacity | Long | 1000 | 实例挂载的本地存储容量。 |
| Memory | Integer | 1024 | 内存大小，单位MiB。 |
| MetadataOptio ns | Struct |  | 元数据选项集合。 |

云服务器ECS

| HttpEndpoint | String | enabled | 是否启用实例元数据的访问通道。可能值： enabled：启用 disabled：禁用 |
|---|---|---|---|
| HttpPutRespon seHopLimit | Integer | 0 | 说明该参数暂未支持。 |
| HttpTokens | String | optional | 访问实例元数据时是否强制使用加固模式 （IMDSv2）。可能值： optional：不强制使用 required：强制使用 |
| NetworkInterfa ces | Array of NetworkInterfa ce |  | 实例包含的弹性网卡集合。 |
| NetworkInterfa ce |  |  |  |
| MacAddress | String | 00:16:3e:32:b4:** | 弹性网卡的MAC地址。 |
| NetworkInterfa ceId | String | eni- 2zeh9atclduxvf1z*** * | 弹性网卡的ID。 |
| PrimaryIpAddre ss | String | 172.17.**.*** | 弹性网卡主私有IP地址。 |
| OSName | String | CentOS 7.4 64 位 | 实例的操作系统名称。 |
| OSNameEn | String | CentOS 7.4 64 bit | 实例操作系统的英文名称。 |
| OSType | String | linux | 实例的操作系统类型，分为Windows Server和 Linux两种。可能值： windows。 linux。 |
| OperationLocks | Array of LockReason |  | 实例的锁定原因。 |
| LockReason |  |  |  |
| LockMsg | String | The specified instance is locked due to financial reason. | 实例被锁定的描述信息。 |
| LockReason | String | test | 说明该参数暂未支持。 |
| PublicIpAddress | List | 121.40.61.*** | 说明该参数暂未支持。 |

云服务器ECS

| RdmaIpAddress | List | 10.10.10.102 | HPC实例的Rdma网络IP。 |
|---|---|---|---|
| Recyclable | Boolean | false | 实例是否可以回收。 |
| RegionId | String | cn-qingdao-env17- d01 | 实例所属地域ID。 |
| ResourceGroup Id | String | rg- bp67acfmxazb4p*** * | 实例所属的企业资源组ID。 |
| SaleCycle | String | month | 说明该参数暂未支持。 |
| SecurityGroupI ds | List | sg- bp67acfmxazb4p*** * | 实例所属安全组集合。 |
| SerialNumber | String | 51d1353b-22bf- 4567-a176- 8b3e12e4**** | 实例序列号。 |
| SpotPriceLimit | Float | 0.00 | 说明该参数暂未支持。 |
| SpotStrategy | String | test | 说明该参数暂未支持。 |
| StartTime | String | test | 说明该参数暂未支持。 |
| Status | String | Running | 实例状态。 |
| StoppedMode | String | test | 说明该参数暂未支持。 |
| Tags | Array of Tag |  | 实例的标签集合。 |
| Tag |  |  |  |
| TagKey | String | TestKey | 实例的标签键。 |
| TagValue | String | TestValue | 实例的标签值。 |
| VlanId | String | 10 | 实例的VLAN ID。 说明该参数即将被弃用，为提高兼容性，请尽量使用其他参数。 |
| VpcAttributes | Struct |  | 专有网络VPC属性。 |

云服务器ECS

| NatIpAddress | String | 172.17.**.*** | 云产品的IP，用于VPC云产品之间的网络互通。 |
|---|---|---|---|
| PrivateIpAddres s | List | 172.17.**.*** | 私有IP地址。 |
| VSwitchId | String | vsw- 2zeh0r1pabwtg6wcs **** | 虚拟交换机ID。 |
| VpcId | String | vpc- 2zeuphj08tt7q3brd* *** | 专有网络VPC ID。 |
| ZoneId | String | cn-qingdao-env17- amtest11001-a | 实例所属可用区。 |
| PageNumber | Integer | 1 | 实例列表的页码。 |
| PageSize | Integer | 1 | 输入时设置的每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 58 | 查询到的实例总数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeInstances &RegionId=cn-qingdao-env17-d01 &PageSize=1 PageNumber=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <PageNumber>1</PageNumber>
      <TotalCount>58</TotalCount>
      <PageSize>1</PageSize>
      <RequestId>97935DF1-0289-4AA2-9DD1-72377838B16B</RequestId>
      <Instances>
            <Instance>
                  <ImageId>centos_7_06_64_20G_alibase_20190711.vhd</ImageId>
                  <VlanId></VlanId>
                  <EipAddress>
                        <IpAddress></IpAddress>
                        <AllocationId></AllocationId>
                  </EipAddress>
                  <ZoneId>cn-qingdao-env17-amtest11001-a</ZoneId>
                  <IoOptimized>true</IoOptimized>
                  <SerialNumber>51d1353b-22bf-4567-a176-8b3e12e43***</SerialNumber>
```

云服务器ECS /

```xml
                  <Cpu>2</Cpu>
                  <Memory>8192</Memory>
                  <DeviceAvailable>true</DeviceAvailable>
                  <SecurityGroupIds>
                        <SecurityGroupId>sg-bp17zljqpohu6j2i****</SecurityGroupId>
                  </SecurityGroupIds>
                  <SaleCycle></SaleCycle>
                  <AutoReleaseTime></AutoReleaseTime>
                  <ResourceGroupId></ResourceGroupId>
                  <OSType>linux</OSType>
                  <OSName>CentOS  7.6 64位</OSName>
                  <InstanceNetworkType>classic</InstanceNetworkType>
                  <HostName>iZbp1j4i2jdf3owlheb****</HostName>
                  <CreationTime>2019-11-11T08:35Z</CreationTime>
                  <Tags>
                        <Tag>
                              <TagValue>asg-bp1d8uuut40f4qc4****</TagValue>
                              <TagKey>acs:autoscaling:scalingGroupId</TagKey>
                        </Tag>
                        <Tag>
                              <TagValue>ESS</TagValue>
                              <TagKey>ESS</TagKey>
                        </Tag>
                  </Tags>
                  <EcsCapacityReservationAttr>
                        <CapacityReservationPreference>none</CapacityReservationPreference>
                        <CapacityReservationId></CapacityReservationId>
                  </EcsCapacityReservationAttr>
                  <RegionId>cn-qingdao-env17-d01</RegionId>
                  <DeletionProtection>false</DeletionProtection>
                  <OperationLocks>
            </OperationLocks>
                  <ExpiredTime>2099-12-31T15:59Z</ExpiredTime>
                  <CpuOptions>
                        <Numa></Numa>
                        <ThreadsPerCore>2</ThreadsPerCore>
                        <CoreCount>1</CoreCount>
                  </CpuOptions>
                  <InnerIpAddress>
                        <IpAddress>10.80.61.42</IpAddress>
                  </InnerIpAddress>
                  <InstanceTypeFamily>ecs.mn4</InstanceTypeFamily>
                  <InstanceId>i-bp1j4i2jdf3owlhe****</InstanceId>
                  <InternetMaxBandwidthIn>50</InternetMaxBandwidthIn>
                  <CreditSpecification></CreditSpecification>
                  <InternetChargeType>PayByTraffic</InternetChargeType>
                  <SpotStrategy>NoSpot</SpotStrategy>
                  <StoppedMode>Not-applicable</StoppedMode>
                  <InternetMaxBandwidthOut>1</InternetMaxBandwidthOut>
                  <VpcAttributes>
                        <NatIpAddress></NatIpAddress>
                        <PrivateIpAddress>
                </PrivateIpAddress>
                        <VSwitchId></VSwitchId>
                        <VpcId></VpcId>
                  </VpcAttributes>
<SpotPriceLimit>0</SpotPriceLimit>
```

云服务器ECS

```xml
                  <SpotPriceLimit>0</SpotPriceLimit>
                  <StartTime>2019-11-11T08:35Z</StartTime>
                  <InstanceName>ECS-asg-MyFirstScalingGroup</InstanceName>
                  <Description>ECS</Description>
                  <OSNameEn>CentOS  7.6 64 bit</OSNameEn>
                  <PublicIpAddress>
                        <IpAddress>121.40.77.XXX</IpAddress>
                  </PublicIpAddress>
                  <InstanceType>ecs.mn4.large</InstanceType>
                  <Status>Running</Status>
                  <MetadataOptions>
                        <HttpTokens></HttpTokens>
                        <HttpEndpoint></HttpEndpoint>
                  </MetadataOptions>
                  <Recyclable>false</Recyclable>
                  <ClusterId></ClusterId>
                  <GPUSpec></GPUSpec>
                  <InstanceChargeType>PostPaid</InstanceChargeType>
                  <GPUAmount>0</GPUAmount>
                  <DedicatedHostAttribute>
                        <DedicatedHostId></DedicatedHostId>
                        <DedicatedHostName></DedicatedHostName>
                  </DedicatedHostAttribute>
                  <DedicatedInstanceAttribute>
                        <Affinity></Affinity>
                        <Tenancy></Tenancy>
                  </DedicatedInstanceAttribute>
                  <DeploymentSetId></DeploymentSetId>
            </Instance>
      </Instances>
```

`JSON` 格式

```json
{
 "PageNumber": 1,
 "TotalCount": 58,
 "PageSize": 1,
 "RequestId": "97935DF1-0289-4AA2-9DD1-72377838B16B",
 "Instances": {
  "Instance": [
   {
    "ImageId": "centos_7_06_64_20G_alibase_20190711.vhd",
    "VlanId": "",
    "EipAddress": {
     "IpAddress": "",
     "AllocationId": "",
    },
    "ZoneId": "cn-qingdao-env17-amtest11001-a",
    "IoOptimized": true,
    "SerialNumber": "51d1353b-22bf-4567-a176-8b3e12e43***",
    "Cpu": 2,
    "Memory": 8192,
    "DeviceAvailable": true,
    "SecurityGroupIds": {
     "SecurityGroupId": [
"sg-bp17zljqpohu6j2i****"
```

云服务器ECS

```
      sgbp17zljqpohu6j2i
```

]

```json
    },
    "SaleCycle": "",
    "AutoReleaseTime": "",
    "ResourceGroupId": "",
    "OSType": "linux",
    "OSName": "CentOS  7.6 64位",
    "InstanceNetworkType": "classic",
    "HostName": "iZbp1j4i2jdf3owlheb****",
    "CreationTime": "2019-11-11T08:35Z",
    "Tags": {
     "Tag": [
      {
       "TagValue": "asg-bp1d8uuut40f4qc4****",
       "TagKey": "acs:autoscaling:scalingGroupId"
      },
      {
       "TagValue": "ESS",
       "TagKey": "ESS"
      }
```

]

```json
    },
    "EcsCapacityReservationAttr": {
     "CapacityReservationPreference": "none",
     "CapacityReservationId": ""
    },
    "RegionId": "cn-qingdao-env17-d01",
    "DeletionProtection": false,
    "OperationLocks": {
     "LockReason": []
    },
    "ExpiredTime": "2099-12-31T15:59Z",
    "CpuOptions": {
     "Numa": "",
     "ThreadsPerCore": 2,
     "CoreCount": 1
    },
    "InnerIpAddress": {
     "IpAddress": [
      "10.80.61.42"
```

]

```json
    },
    "InstanceTypeFamily": "ecs.mn4",
    "InstanceId": "i-bp1j4i2jdf3owlhe****",
    "InternetMaxBandwidthIn": 50,
    "CreditSpecification": "",
    "InternetChargeType": "PayByTraffic",
    "SpotStrategy": "NoSpot",
    "StoppedMode": "Not-applicable",
    "InternetMaxBandwidthOut": 1,
    "VpcAttributes": {
     "NatIpAddress": "",
     "PrivateIpAddress": {
      "IpAddress": []
     },
     "VSwitchId": "",
```

云服务器ECS

```json
     "VpcId": ""
    },
    "SpotPriceLimit": 0,
    "StartTime": "2019-11-11T08:35Z",
    "InstanceName": "ECS-asg-MyFirstScalingGroup",
    "Description": "ECS",
    "OSNameEn": "CentOS  7.6 64 bit",
    "PublicIpAddress": {
     "IpAddress": [
      "121.40.77.XXX"
```

]

```json
    },
    "InstanceType": "ecs.mn4.large",
    "Status": "Running",
                "MetadataOptions": {
     "HttpTokens": "",
     "HttpEndpoint": ""
    },
    "Recyclable": false,
    "ClusterId": "",
    "GPUSpec": "",
    "InstanceChargeType": "PostPaid",
    "GPUAmount": 0,
    "DedicatedHostAttribute": {
     "DedicatedHostId": "",
     "DedicatedHostName": ""
    },
    "DedicatedInstanceAttribute": {
     "Affinity": "",
     "Tenancy": ""
    },
    "DeploymentSetId": ""
   }
```

]

```
 }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceChar geType.NotFound | The InstanceChargeType does not exist in our records | 指定的实例计费方式不存在。 |
| 404 | InvalidInternetCharg eType.ValueNotSup ported | The specified InternetChargeType is not valid | 指定的网络计费方式不合法。 |
| 404 | InvalidLockReason.N otFound | The specified LockReason is not found | 指定的锁定类型不存在。 |
| 404 | InvalidFilterKey.NotF ound |  | 指定的起始时间或到期时间参数错误。 |
| 404 | InvalidNetworkType. NotFound | The specified InstanceNetworkType is not found | 指定的带宽类型不存在。 |

云服务器ECS

| 404 | InvalidStatus.NotFou nd | The specified Status is not found | 指定的资源状态不存在。 |
|---|---|---|---|
| 400 | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. | 指定的Tag.N.Key和Tag.N.Value不匹配。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
| 400 | InvalidHpcClusterId. NotFound | The specified HpcClusterId is not found. | 指定的参数HpcClusterId不存在。 |
| 400 | InvalidHpcClusterId. Creating | The specified HpcClusterId is creating. | 指定的HPC集群正在创建中。 |

##### StartInstances

调用StartInstances启动一台或多台处于已停止（Stopped）状态的ECS实例，接口调用成功后实例进入启动中 （Starting）状态。

**接口说明**

调用该接口时，您需要注意： ECS实例状态必须为**已停止**（ `Stopped` ）。 查询ECS实例信息时，如果返回数据中包含 `{"OperationLocks": {"LockReason" : "security"}}` ，则禁止一切操作。 支持批量操作，可以通过参数 `BatchOptimization` 设置批量操作模式。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartInstances | 系统规定参数。取值：StartInstances。 |
| InstanceId.N | RepeatLi st | 是 | i- bp67acfmxazb4p **** | 实例ID。N的取值范围：1~100。 |
| RegionId | String | 是 | cn-qingdao-**** | 实例所在的地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| DryRun | Boolean | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会启动实例。检查项包括是否填写了必需参数、请求格式、实例状态。如果检查不通过，则返回对应错误。如果检查通过，则返回 DRYRUN.SUCCESS 。 说明如果参数 BatchOptimization 被设置为 SuccessFirst ，对应的 DryRun=true 的预检结果只会返回 DRYRUN.SUCCESS 。 false：发送正常请求，通过检查后直接启动实例。 默认值：false。 |
|---|---|---|---|---|
| BatchOptimizatio n | String | 否 | SuccessFirst | 设置批量操作模式。取值范围： AllTogether：该模式下，如果实例全部启动成功，则返回成功信息；如果任意一个实例校验不通过，则所有实例启动失败，并返回失败信息。 SuccessFirst：该模式下，分别启动每个实例，返回结果包含每个实例的操作结果信息。 默认值：AllTogether。 |

| BatchOptimization |  |
|---|---|
| SuccessFirst |  |
| DryRun=true |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceRespon ses | Array of InstanceRespon se |  | 由InstanceResposne组成的数组格式，返回每个实例操作的前后状态及操作结果。 |
| InstanceRespon se |  |  |  |
| Code | String | 200 | 实例操作结果错误码。返回值200为成功，更多请参见下文错误码列表。 |
| CurrentStatus | String | Starting | 实例当前状态。 |
| InstanceId | String | i- bp67acfmxazb4p*** * | 实例ID。 |
| Message | String | success | 实例操作返回错误信息。返回值success为成功， 更多请参见下文错误码列表。 |
| PreviousStatus | String | Stopped | 操作前实例的状态。 |

云服务器ECS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
&InstanceId.1=i-bp67acfmxazb4p**** &InstanceId.2=i-bp67acfmxazb4p**** &InstanceId.3=i-TestID &RegionId=cn-qingdao-**** $BatchOptimization=SuccessFirst
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId> <InstanceResponses>
    <InstanceResponse>
        <Message>success</Message>
        <InstanceId>i-bp67acfmxazb4p****</InstanceId>
        <PreviousStatus>Stopped</PreviousStatus>
        <CurrentStatus>Starting</CurrentStatus>
        <Code>200</Code>
    </InstanceResponse>
    <InstanceResponse>
        <Message>success</Message>
        <InstanceId>i-bp67acfmxazb4p****</InstanceId>
        <PreviousStatus>Stopped</PreviousStatus>
        <CurrentStatus>Starting</CurrentStatus>
        <Code>200</Code>
    </InstanceResponse>
    <InstanceResponse>
        <Message>The specified InstanceId does not exist.</Message>
        <InstanceId>i-TestID</InstanceId>
        <PreviousStatus/>
        <CurrentStatus/>
        <Code>InvalidInstanceId.NotFound</Code>
    </InstanceResponse>
</InstanceResponses>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
    "InstanceResponses": {
        "InstanceResponse": [
            {
                "Message": "success",
                "InstanceId": "i-bp67acfmxazb4p****",
                "PreviousStatus": "Stopped",
                "CurrentStatus": "Starting",
                "Code": "200"
            },
            {
                "Message": "success",
                "InstanceId": "i-bp67acfmxazb4p****",
                "PreviousStatus": "Stopped",
                "CurrentStatus": "Starting",
                "Code": "200"
            },
            {
                "Message": "The specified InstanceId does not exist.",
                "InstanceId": "i-TestID",
                "PreviousStatus": "",
                "CurrentStatus": "",
                "Code": "InvalidInstanceId.NotFound"
            }
```

]

```
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter.K MSKeyId.CMKNotEn abled | The CMK needs to be enabled. | 加密云盘设置了 KMSKeyId 后，CMK必须处于启用状态。您可以调用密钥管理服务的 DescribeKey 接口查询指定CMK的相关信息。 |
| 400 | DRYRUN.SUCCESS | This request is a dryrun request with successful result. | 您设置了预检此次请求，并且检查通过。 |
| 404 | InvalidInstanceId.No tFound | %s | 指定的实例不存在，请确认参数 InstanceId 是否正确。 |
| 404 | InvalidInstanceIds.N otFound | The specified InstanceIds does not exist. | 指定的 InstanceId 不存在。请检查 InstanceId 参数值是否正确。您可以调用 DescribeInstances 查询指定实例的状态。 |
| 403 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 403 | InvalidInstance.NotF oundSystemDisk | %s | 指定的实例ID未挂载系统盘，无法启动，具体信息请参见错误信息%s占位符的实际返回结果。请先调用 AttachDisk为指定的实例挂载系统盘。 |

云服务器ECS

| 403 | OperationDenied.No Stock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. | 库存不足。 |
|---|---|---|---|
| 403 | OperationDenied.Sp otPriceLowerThanPu blicPrice | The spot instance price is lower than public price. | 抢占式实例的竞价价格不能低于公开的价格。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | InsufficientBalance | Your account does not have enough balance. | 账户余额不足，请先充值再操作。 |
| 403 | InstanceNotReady | The specified instance is not ready for use. | 该资源目前的状态不支持此操作，请您等待一段时间再进行操作，并确认实例目前状态与操作是否冲突。 |

##### RebootInstances

调用RebootInstances重启一台或多台处于运行中（Running）状态的ECS实例。接口调用成功后，ECS实例先进入停止中（Stopping）状态，最终进入运行中（Running）状态。

**接口说明**

| 必须为运行中（ Running ）。 可以通过参数 BatchOptimization |  | Running | ）。 |
|---|---|---|---|
|  | BatchOptimization |  |  |
| ForceReboot |  | ），强制重启等同于 |  |

块存储的数据。 查询ECS实例信息时，如果返回数据中包含 `{"OperationLocks": {"LockReason" : "security"}}` ，则禁止一切操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RebootInstances | 系统规定参数。取值：RebootInstances。 |
| InstanceId.N | RepeatLi st | 是 | i- bp67acfmxazb4p **** | 实例ID。N的取值范围：1~100。 |
| RegionId | String | 是 | cn-qingdao-**** | 实例所属的地域ID。您可以调用 DescribeRegions查询地域ID。 |

云服务器ECS

| DryRun | Boolean | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会重启实例。检查项包括是否填写了必需参数、请求格式、实例状态。如果检查不通过，则返回对应错误。如果检查通过，则返回 DRYRUN.SUCCESS 。 说明如果参数 BatchOptimization 被设置为 SuccessFirst ，对应的 DryRun=true 的预检结果只会返回 DRYRUN.SUCCESS 。 false：发送正常请求，通过检查后直接重启实例。 默认值：false。 |
|---|---|---|---|---|
| ForceReboot | Boolean | 否 | false | 是否强制重启。取值范围： true：强制重启。相当于典型的断电操作，所有未写入存储设备的缓存数据会丢失。 false：正常重启。 默认值：false。 |
| BatchOptimizatio n | String | 否 | SuccessFirst | 设置批量操作模式。取值范围： AllTogether：该模式下，如果实例全部重启成功，则返回成功信息；如果任意一个实例校验不通过，则所有实例重启失败，并返回失败信息。 SuccessFirst：该模式下，分别重启每个实例，返回结果包含每个实例的操作结果信息。 默认值：AllTogether。 |

| BatchOptimization |  |
|---|---|
| SuccessFirst |  |
| DryRun=true |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceRespon ses | Array of InstanceRespon se |  | 由InstanceResposne组成的数组格式，返回每个实例操作的前后状态及操作结果。 |
| InstanceRespon se |  |  |  |
| Code | String | 200 | 实例操作结果错误码。返回值200为成功，更多请参见下文错误码列表。 |
| CurrentStatus | String | Stopping | 实例当前状态。 |
| InstanceId | String | i- bp67acfmxazb4p*** * | 实例ID。 |

云服务器ECS

| Message | String | success | 实例操作返回错误信息。返回值Success为成功， 更多请参见下文错误码列表。 |
|---|---|---|---|
| PreviousStatus | String | Running | 实例操作前状态。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=RebootInstances &InstanceId.1=i-bp67acfmxazb4p**** &InstanceId.2=i-bp1g6zv0ce8oghu7**** &InstanceId.3=i-TestID &RegionId=cn-qingdao-**** &ForceReboot=false $BatchOptimization=SuccessFirst
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
        <InstanceResponses>
                <InstanceResponse>
                        <Message>success</Message>
                        <InstanceId>i-bp67acfmxazb4p****</InstanceId>
                        <PreviousStatus>Running</PreviousStatus>
                        <CurrentStatus>Stopping</CurrentStatus>
                        <Code>200</Code>
                </InstanceResponse>
                <InstanceResponse>
                        <Message>success</Message>
                        <InstanceId>i-bp1g6zv0ce8oghu7****</InstanceId>
                        <PreviousStatus>Running</PreviousStatus>
                        <CurrentStatus>Stopping</CurrentStatus>
                        <Code>200</Code>
                </InstanceResponse>
                <InstanceResponse>
                        <Message>The specified InstanceId does not exist.</Message>
                        <InstanceId>i-TestID</InstanceId>
                        <PreviousStatus></PreviousStatus>
                        <CurrentStatus></CurrentStatus>
                        <Code>InvalidInstanceId.NotFound</Code>
                </InstanceResponse>
        </InstanceResponses>
```

`JSON` 格式云服务器ECS

```json
{
        "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
        "InstanceResponses": {
            "InstanceResponse": [
                {
                    "Message": "success",
                    "InstanceId": "i-bp67acfmxazb4p****",
                    "PreviousStatus": "Running",
                    "CurrentStatus": "Stopping",
                    "Code": 200
                },
                {
                    "Message": "success",
                    "InstanceId": "i-bp67acfmxazb4p****",
                    "PreviousStatus": "Running",
                    "CurrentStatus": "Stopping",
                    "Code": 200
                },
                {
                    "Message": "The specified InstanceId does not exist.",
                    "InstanceId": "i-TestID",
                    "PreviousStatus": "",
                    "CurrentStatus": "",
                    "Code": "InvalidInstanceId.NotFound"
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
| 400 | InvalidParameter.K MSKeyId.CMKNotEn abled | The CMK needs to be enabled. | 加密云盘设置了 KMSKeyId 后，CMK必须处于启用状态。您可以调用密钥管理服务的 DescribeKey 接口查询指定CMK的相关信息。 |
| 400 | DRYRUN.SUCCESS | This request is a dryrun request with successful result. | 您设置了预检此次请求，并且检查通过。 |
| 404 | InvalidInstanceId.No tFound | %s | 指定的实例不存在，请确认参数 InstanceId 是否正确。 |
| 404 | InvalidInstanceIds.N otFound | The specified InstanceIds does not exist. | 指定的 InstanceId 不存在。请检查 InstanceId 参数值是否正确。您可以调用 DescribeInstances 查询指定实例的状态。 |
| 403 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |

云服务器ECS

| 403 | InvalidInstance.NotF oundSystemDisk | %s | 指定的实例ID未挂载系统盘，无法启动，具体信息请参见错误信息%s占位符的实际返回结果。请先调用 AttachDisk为指定的实例挂载系统盘。 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | InsufficientBalance | Your account does not have enough balance. | 账户余额不足，请先充值再操作。 |
| 403 | InstanceNotReady | The specified instance is not ready for use. | 该资源目前的状态不支持此操作，请您等待一段时间再进行操作，并确认实例目前状态与操作是否冲突。 |

##### DeleteInstances

**接口说明**

释放后，实例所使用的物理资源都被回收，相关数据全部丢失且不可恢复。 挂载在实例上的云盘： 如果设置了 `DeleteWithInstance=true` ，云盘会被同时释放。 如果为 `DeleteAutoSnapshot=false` ，保留自动快照。 如果为 `DeleteAutoSnapshot=true` ，同时释放自动快照。 仍旧保留云盘的手动快照。

| 例被安全控制并且 | OperationLocks |  |  | 中标 |
|---|---|---|---|---|
| DeleteWithInstance |  | 的属性为 | false |  |

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteInstances | 系统规定参数。对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值： DeleteInstances。 |
| InstanceId.N | RepeatLi st | 是 | i- bp1g6zv0ce8ogh u7k*** | 实例ID。N的取值范围：1~100。 |
| RegionId | String | 是 | cn-qingdao-**** | 实例所属的地域ID。您可以调用 DescribeRegions查询地域ID。 |

云服务器ECS

| DryRun | Boolean | 否 | false | 是否只预检此次请求。 true：发送检查请求，不会查询资源状况。检查项包括AccessKey是否有效、 RAM用户的授权情况和是否填写了必需参数。如果检查不通过，则返回对应错误。 如果检查通过，会返回错误码 DRYRUN.SUCCESS。 false（默认值）：发送正常请求，通过检查后返回2XX HTTP状态码并直接查询资源状况。 |
|---|---|---|---|---|
| Force | Boolean | 否 | false | 是否强制释放运行中（ Running ）的 ECS实例。 true：强制释放运行中（ Running ） 的实例。强制释放相当于断电，实例内存以及存储中的临时数据都会被擦除，无法恢复。 false（默认值）：正常释放实例，此时实例必须处于已停止（ Stopped ）状态。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见《云服务器ECS开发指南》中的如何保证幂等性章节。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 7B7813C6-57BF- 41XX-B12B- F172F65***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DeleteInstances &InstanceId.1=i-bp1g6zv0ce8oghu7k*** &RegionId=cn-qingdao-****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <RequestId>7B7813C6-57BF-41XX-B12B-F172F65*****</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "7B7813C6-57BF-41XX-B12B-F172F65*****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceIds.N otFound | The specified InstanceIds does not exist. | 指定的 InstanceId 不存在。请检查 InstanceId 参数值是否正确。您可以调用 DescribeInstances 查询指定实例的状态。 |
| 403 | InvalidOperation.Del etionProtection | %s | 该操作无效，请先取消该实例的释放保护。 |
| 404 | InvalidInstanceId.No tFound | %s | 指定的实例不存在，请确认参数 InstanceId 是否正确。 |
| 400 | DRYRUN.SUCCESS | This request is a dryrun request with successful result. | 您设置了预检此次请求，并且检查通过。 |
| 403 | InvalidOperation.Eni Linked | %s | 实例的当前弹性网卡关联了其他弹性网卡，导致操作无效。需要解除关联后才能从实例解绑。 |
| 403 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 500 | InternalError | %s | 内部错误。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 400 | DependencyViolatio n.SLBConfiguring | Specified operation is denied as your instance is using by another product. | 实例被 SLB 引用，且 SLB 正在配置。 |
| 400 | DependencyViolatio n.RouteEntry | Specified instance is used by route entry. | 当前专有网络 VPC 还存在未删除的自定义路由规则，删除失败。 |

##### DescribeUserData

**接口说明**

返回的实例自定义数据将以Base64编码的方式显示。 如果实例不存在自定义数据，则返回空值。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云服务器ECS

| Action | String | 是 | DescribeUserDat a | 系统规定参数。取值：DescribeUserdata |
|---|---|---|---|---|
| InstanceId | String | 是 | i- bp1a0cmfrfi71qlh **** | 要查询的实例ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceId | String | i- bp1a0cmfrfi71qlh*** * | 实例ID。 |
| RegionId | String | cn-qingdao-env17- d01 | 地域ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| UserData | String | ZWNobyBoZWxsbyB lY3Mh | 实例的自定义数据。 |

**示例**

请求示例

```
https://ecs.example.com/?Action= DescribeUserdata &RegionId=cn-qingdao-env17-d01 &InstanceId=i-bp1a0cmfrfi71qlh****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
      <UserData>ZWNobyBoZWxsbyBlY3Mh</UserData>
      <InstanceId>i-bp1a0cmfrfi71qlh****</InstanceId>
      <RegionId>cn-qingdao-env17-d01</RegionId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    " UserData ": "ZWNobyBoZWxsbyBlY3Mh",
    " InstanceId ": "i-bp1a0cmfrfi71qlh****",
    " RegionId": "cn-qingdao-env17-d01"
}
```

云服务器ECS

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |

##### DescribeInstanceRamRole

调用DescribeInstanceRamRole查询一台或者多台ECS实例上的已赋予的实例RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInstance RamRole | 接口名称。取值： DescribeInstanceRamRole |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例RAM角色所在的地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| PageNumber | Integer | 否 | 1 | 查询接口返回资源信息列表的页码。 起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页展示响应信息时设置的每页行数，单位：行。 最大值：50。 默认值：10。 |
| InstanceIds | String | 否 | ["i- bp67acfmxazb4p ****", "i- bp67acfmxazb4p ****", "bp67acfmxazb4 p****"…] | 指定查询的实例ID的集合。最多支持一次查询100台实例。 InstanceIds 与 RamRoleName 参数必须至少填写一个。 |
| RamRoleName | String | 否 | EcsServiceRole- EcsDocGuideTest | 查询赋予了某一实例RAM角色的所有ECS实例。您可以使用RAM API ListRoles查询您已创建的实例RAM角色。 InstanceIds 与 RamRoleName 参数必须至少填写一个。 |

| cfmxazb4 |  |
|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceRamRo leSets | Array of InstanceRamRo leSet |  | 由实例RAM角色类型InstanceRamRoleSet组成的信息集。 |

云服务器ECS

| InstanceRamRo leSet |  |  |  |
|---|---|---|---|
| InstanceId | String | i- bp67acfmxazb4p*** * | 实例ID。 |
| RamRoleName | String | EcsServiceRole- EcsDocGuideTest | 实例RAM角色名称列表。 |
| RegionId | String | cn-qingdao-env17- d01 | 实例RAM角色所在的地域。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 1 | 返回的RAM角色数量。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeInstanceRamRole &RegionId=cn-qingdao-env17-d01 &InstanceIds=["i-bp67acfmxazb4p****"] &PageNumber=1 &PageSize=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>8F4CAE3F-7892-4662-83A5-2C2FFD639553</RequestId>
      <InstanceRamRoleSets>
            <InstanceRamRoleSet>
                  <InstanceId>i-bp67acfmxazb4p****</InstanceId>
                  <RamRoleName>EcsServiceRole-EcsDocGuideTest</RamRoleName>
            </InstanceRamRoleSet>
      </InstanceRamRoleSets>
      <TotalCount>1</TotalCount>
      <PageNumber>1</PageNumber>
      <PageSize>1</PageSize>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "8F4CAE3F-7892-4662-83A5-2C2FFD639553",
    "InstanceRamRoleSets": {
        "InstanceRamRoleSet": [
            {
                "InstanceId": "i-bp67acfmxazb4p****",
                "RamRoleName": "EcsServiceRole-EcsDocGuideTest"
            }
```

]

```json
    },
    "TotalCount": 1,
    "PageNumber": 1,
    "PageSize": 1
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInstanceIds.M alformed | The specified instanceIds are not valid. | 指定的多个InstanceId不合法。 |
| 404 | InvalidInstanceId.No tFound | The specified instanceId does not exist | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | InvalidNetworkType. MismatchRamRole | Ram role cannot be applied to instances of Classic network type. | 实例RAM角色不能被用于经典网络类型的实例，RAM角色只能使用在VPC 类型的实例上。 |
| 403 | InvalidParameter.All Empty | %s | 您没有输入任何参数，请输入必要的参数。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### DescribeInstanceTypeFamilies

调用DescribeInstanceTypeFamilies查询云服务器ECS提供的实例规格族列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInstance TypeFamilies | 接口名称。取值： DescribeInstanceTypeFamilies |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| Generation | String | 否 | ecs-3 | 实例规格族的系列信息。取值范围： ecs-1：系列I实例规格族，上线时间较早，性价比高。 ecs-2：系列II实例规格族，第二次软硬件升级，实例性能增强。 ecs-3：系列III实例规格族，实例性能优良，能承载不同业务需求。 ecs-4：系列IV实例规格族，具有强大的场景适应性，能承载海量热门业务需求， 延迟更低。 ecs-5：系列V实例规格族，包含常见的企业级实例规格（g6、c6、r6等）和弹性裸金属服务器实例规格等，响应更快，性能更优越。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceTypeFa milies | Array of InstanceTypeFa mily |  | 由实例规格族InstanceTypeFamily组成的集合。 |
| InstanceTypeFa mily |  |  |  |
| Generation | String | ecs-5 | 实例规格族所属代数。 |
| InstanceTypeFa milyId | String | ecs.g6 | 实例规格族ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeInstanceTypeFamilies &RegionId=cn-qingdao-env17-d01 &Generation=ecs-5
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <InstanceTypeFamilies>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.g6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.ebmg6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.ebmg6e</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.g6e</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.c6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.r6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.t6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.hfc6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.hfg6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.hfr6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.ebmc6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
            <InstanceTypeFamily>
                  <InstanceTypeFamilyId>ecs.ebmr6</InstanceTypeFamilyId>
                  <Generation>ecs-5</Generation>
            </InstanceTypeFamily>
      </InstanceTypeFamilies>
      <RequestId>A66D039A-EC35-4130-B0D1-E9873C0742D2</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
 "InstanceTypeFamilies": {
  "InstanceTypeFamily": [
   {
    "InstanceTypeFamilyId": "ecs.g6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.ebmg6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.ebmg6e",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.g6e",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.c6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.r6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.t6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.hfc6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.hfg6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.hfr6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.ebmc6",
    "Generation": "ecs-5"
   },
   {
    "InstanceTypeFamilyId": "ecs.ebmr6",
    "Generation": "ecs-5"
   }
```

]

```json
 },
 "RequestId": "A66D039A-EC35-4130-B0D1-E9873C0742D2"
}
```

云服务器ECS

##### DescribeInstanceAttribute

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInstance Attribute | 系统规定参数。取值： DescribeInstanceAttribute。 |
| InstanceId | String | 是 | i- uf6f5trc95ug8t33 **** | 指定实例的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ClusterId | String | cls- bp67acfmxazb4p*** * | 实例所在的集群ID。 说明该参数即将被弃用，为提高兼容性，请尽量使用其他参数。 |
| Cpu | Integer | 8 | vCPU处理器核心数量。 |
| CreationTime | String | 2021-12-10T04:04Z | 实例创建时间。以ISO 8601为标准，并使用 UTC+0时间，格式为yyyy-MM-ddTHH:mmZ。 |
| CreditSpecificat ion | String | Standard | 修改突发性能实例的运行模式。可能值： Standard：标准模式。 Unlimited：无性能约束模式。 |
| DedicatedHost Attribute | Struct |  | 由专有宿主机集群 ID（DedicatedHostClusterId）、专有宿主机 ID（DedicatedHostId）和名称 （DedicatedHostName）组成的宿主机属性数组。 |
| DedicatedHostI d | String | dh- 2ze7qrzz6lvbfhr0*** * | 专有宿主机ID。 |
| DedicatedHost Name | String | ecs-autoui-create- ddh-temp | 专有宿主机的名称。 |
| Description | String | testDescription | ECS实例描述。 |
| EipAddress | Struct |  | 弹性公网IP绑定信息。 |

云服务器ECS

| AllocationId | String | eip- wz9uilio26dfscamm **** | 弹性公网IP的ID。 |
|---|---|---|---|
| Bandwidth | Integer | 8 | 弹性公网IP的公网带宽限速，单位为Mbit/s。 |
| InternetCharge Type | String | PayByTraffic | 该参数未开放使用。 |
| IpAddress | String | 30.21.**.** | 弹性公网IP。 |
| ExpiredTime | String | 2021-12-10T04:04Z | 过期时间。以ISO 8601为标准，并使用UTC+0时间，格式为yyyy-MM-ddTHH:mmZ。 |
| HostName | String | testHostName | 实例主机名。 |
| ImageId | String | m- bp1h46wfpjsjastc*** * | 实例运行的镜像ID。 |
| InnerIpAddress | List | 192.168.**.** | 该参数未开放使用。 |
| InstanceCharge Type | String | PrePaid | 该参数未开放使用。 |
| InstanceId | String | i- uf6f5trc95ug8t33*** * | 实例ID。 |
| InstanceName | String | testInstanceName | 实例名称。 |
| InstanceNetwor kType | String | vpc | 实例网络类型。支持设置为 vpc ，表示专有网络 VPC。 |
| InstanceType | String | ecs.s6-k | 实例的规格。 |
| InternetCharge Type | String | PayByTraffic | 该参数未开放使用。 |
| InternetMaxBa ndwidthIn | Integer | 50 | 公网入带宽最大值，单位为Mbit/s。 |
| InternetMaxBa ndwidthOut | Integer | 5 | 公网出带宽最大值，单位为Mbit/s。 |
| IoOptimized | String | true | 是否为I/O优化型实例。 |
| Memory | Integer | 16384 | 内存大小，单位为MiB。 |

云服务器ECS

| OperationLocks | Array of LockReason |  | 锁定类型。可能值为 security ，表示因安全原因被锁定。 |
|---|---|---|---|
| LockReason |  |  |  |
| LockReason | String | security | 锁定类型。可能值为 security ，表示因安全原因被锁定。 |
| PublicIpAddress | List | 121.40.**.** | 实例公网IP地址。 |
| RegionId | String | cn-hangzhou | 实例所属地域ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| SecurityGroupI ds | List | sg- bp1fg655nh68xyz9i **** | 实例所属安全组集合。 |
| SerialNumber | String | 51d1353b-22bf- 4567-a176- 8b3e12e4**** | 实例序列号。 |
| Status | String | Running | 实例状态。取值范围： Pending：创建中。 Running：运行中。 Starting：启动中。 Stopping：停止中。 Stopped：已停止。 |
| StoppedMode | String | KeepCharging | 该参数未开放使用。 |
| VlanId | String | 10 | 实例的VLAN ID。 说明该参数即将被弃用，为提高兼容性，请尽量使用其他参数。 |
| VpcAttributes | Struct |  | 专有网络VPC属性。 |
| NatIpAddress | String | 172.17.**.** | 云产品的IP，用于VPC云产品之间的网络互通。 |
| PrivateIpAddres s | List | 192.168.**.** | 私有IP地址。 |
| VSwitchId | String | vsw- uf6ixacqz8osrwnqb* *** | 虚拟交换机ID。 |

云服务器ECS

| VpcId | String | vpc- wz9e4e9pmbcnj6ki6 **** | 专有网络VPC ID。 |
|---|---|---|---|
| ZoneId | String | cn-hangzhou-g | 实例所属可用区。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribeInstanceAttribute &InstanceId=i-uf6f5trc95ug8t33****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
<Description>testDescription</Description> <Memory>16384</Memory> <Cpu>8</Cpu> <InstanceNetworkType>vpc</InstanceNetworkType> <PublicIpAddress>121.40.**.**</PublicIpAddress> <InnerIpAddress>192.168.**.**</InnerIpAddress> <ExpiredTime>2021-12-10T04:04Z</ExpiredTime> <ImageId>m-bp1h46wfpjsjastc****</ImageId> <EipAddress>
    <Bandwidth>8</Bandwidth>
    <AllocationId>eip-wz9uilio26dfscamm****</AllocationId>
    <IpAddress>30.21.**.**</IpAddress>
</EipAddress> <InstanceType>ecs.s6-k</InstanceType> <VlanId>10</VlanId> <HostName>testHostName</HostName> <Status>Running</Status> <IoOptimized>true</IoOptimized> <ZoneId>cn-hangzhou-g</ZoneId> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId> <InstanceId>i-uf6f5trc95ug8t33****</InstanceId> <DedicatedHostAttribute>
    <DedicatedHostId>dh-2ze7qrzz6lvbfhr0****</DedicatedHostId>
    <DedicatedHostName>ecs-autoui-create-ddh-temp</DedicatedHostName>
</DedicatedHostAttribute> <SecurityGroupIds>sg-bp1fg655nh68xyz9i****</SecurityGroupIds> <VpcAttributes>
    <VpcId>vpc-wz9e4e9pmbcnj6ki6****</VpcId>
    <VSwitchId>vsw-uf6ixacqz8osrwnqb****</VSwitchId>
    <NatIpAddress>172.17.**.**</NatIpAddress>
    <PrivateIpAddress>192.168.**.**</PrivateIpAddress>
</VpcAttributes> <OperationLocks>
    <LockReason>security</LockReason>
</OperationLocks> <InstanceName>testInstanceName</InstanceName> <InternetMaxBandwidthOut>5</InternetMaxBandwidthOut> <SerialNumber>51d1353b-22bf-4567-a176-8b3e12e4****</SerialNumber> <InternetMaxBandwidthIn>50</InternetMaxBandwidthIn> <CreationTime>2021-12-10T04:04Z</CreationTime> <RegionId>cn-hangzhou</RegionId> <CreditSpecification>Standard</CreditSpecification>
```

`JSON` 格式云服务器ECS

```json
{
    "Description": "testDescription",
    "Memory": 16384,
    "Cpu": 8,
    "InstanceNetworkType": "vpc",
    "PublicIpAddress": "121.40.**.**",
    "InnerIpAddress": "192.168.**.**",
    "ExpiredTime": "2021-12-10T04:04Z",
    "ImageId": "m-bp1h46wfpjsjastc****",
    "EipAddress": {
        "Bandwidth": 8,
        "AllocationId": "eip-wz9uilio26dfscamm****",
        "IpAddress": "30.21.**.**"
    },
    "InstanceType": "ecs.s6-k",
    "VlanId": 10,
    "HostName": "testHostName",
    "Status": "Running",
    "IoOptimized": true,
    "ZoneId": "cn-hangzhou-g",
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "InstanceId": "i-uf6f5trc95ug8t33****",
    "DedicatedHostAttribute": {
        "DedicatedHostId": "dh-2ze7qrzz6lvbfhr0****",
        "DedicatedHostName": "ecs-autoui-create-ddh-temp"
    },
    "SecurityGroupIds": "sg-bp1fg655nh68xyz9i****",
    "VpcAttributes": {
        "VpcId": "vpc-wz9e4e9pmbcnj6ki6****",
        "VSwitchId": "vsw-uf6ixacqz8osrwnqb****",
        "NatIpAddress": "172.17.**.**",
        "PrivateIpAddress": "192.168.**.**"
    },
    "OperationLocks": {
        "LockReason": "security"
    },
    "InstanceName": "testInstanceName",
    "InternetMaxBandwidthOut": 5,
    "SerialNumber": "51d1353b-22bf-4567-a176-8b3e12e4****",
    "InternetMaxBandwidthIn": 50,
    "CreationTime": "2021-12-10T04:04Z",
    "RegionId": "cn-hangzhou",
    "CreditSpecification": "Standard"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

云服务器ECS

##### ModifyInstanceAttribute

调用ModifyInstanceAttribute修改一台ECS实例的部分信息，包括实例密码、名称、描述、主机名、所属安全组和自定义数据等。 接口说明查询ECS实例信息时，如果返回数据中包含 `{"OperationLocks": {"LockReason" : "security"}}` ，则禁止一切操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ModifyInstanceAttribute | 系统规定参数。取值： ModifyInstanceAttribute。 |
| InstanceId | String | Query | 是 | i-bp67acfmxazb4ph*** | 实例ID。 |
| Password | String | Query | 否 | EcsV**** | 实例的密码。支持长度为 8~30个字符，必须同时包含大小写英文字母、数字和特殊符号中的三类字符。特殊符号可以是： ()`~!@#$%^&*- +=\|{} _ []:;'<>,.?/ 其中，Windows实例不能以斜线号（/）为密码首字符。 使用该参数时请注意： 实例不能处于启动中 （Starting）状态。 重启实例后生效。您可以在ECS控制台重启或者调用 RebootInstance 重启， 在操作系统内部重启不能生效。 说明如果传入 Password 参数， 建议您使用HTTPS协议发送请求，避免密码泄露。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| HostName | String | Query | 否 | LocalHost | 操作系统的主机名。使用该参数时请注意： 修改主机名时，实例不能处于创建中 （ Pending ） 或启动中 （ Starting ）的状态，否则可能出现主机名以及 /etc/hosts 配置失效等情况。您可以调用 DescribeInstances 查询实例当前的状态信息。 您可以在 ECS控制台重启或者调用 RebootInstance 重启， 在操作系统内部重启不能生效。 不同操作系统主机名存在以下限制： Windows Server系统： 长度为2~15个字符，允许使用大小写字母、数字或连字符（-）。不能以连字符（-）开头或结尾，不能连续使用连字符（-），也不能仅使用数字。 其他类型实例（Linux 等）：长度为2~64个字符，允许使用点号（.）分隔字符成多段，每段允许使用大小写字母、数字或连字符（-），但不能连续使用点号（.）或连字符 （-）。不能以点号（.）或连字符（-）开头或结尾。 |  |  |
| InstanceNa me | String | Query | 否 | EcsInstance | 实例名称。长度为2~128个字符，支持Unicode中letter 分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号（:）、下划线 （ ）、半角句号（.）或者短 _ 划线（-）。 |  |  |
| Descriptio n | String | Query | 否 | InstanceAttribute | 实例描述。长度为2~256个英文或中文字符，不能以 http:// 或 https:/ / 开头。 默认值：无。 |  |  |
|  |  |  |  |  |  | https:/ |  |

|  |  |  | 创建 |  |
|---|---|---|---|---|
|  | 中 |  |  |  |
|  |  |  | （ |  |
|  | 或 |  |  |  |
|  | 中 |  |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserData | String | Query | 否 | ZWNobyBoZWxsbyBlY3M h | 实例自定义数据，建议 Base64 编码后传入。使用该参数时请注意： 实例必须满足自定义数据使用限制。更多信息，请参见生成实例自定义数据。 重启实例后，实例上将展示新的自定义数据，但不会运行数据。 说明编码前， 原始数据不能超过 32 KB。建议不要明文传入敏感信息，例如密码和私钥等。如果必须传入敏感信息，建议您加密后再以 Base64 编码传入，在实例内部以同样的方式解密。 |
| DeletionPr otection | Boole an | Query | 否 | false | 实例释放保护属性，指定是否支持通过控制台或 API（ DeleteInstance ）释放实例。 说明该属性只能限制手动释放操作， 对系统释放操作不生效。 |
| NetworkInt erfaceQue ueNumber | Intege r | Query | 否 | 8 | 主网卡队列数。使用该参数时请注意： 实例必须为已停止 （Stopped）状态。 不能超过实例规格允许的单块网卡最大队列数，实例的所有网卡累加队列数不能超过实例规格允许的队列数总配额。实例规格的单块网卡最大队列数和总配额可以通过 DescribeInstanceTypes 查询。 当取值为-1时，将重置主网卡队列数为对应实例规格的默认值。实例规格的弹性网卡默认队列数可以通过 DescribeInstanceTypes 查询。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CpuOption s.Topology Type | String | Query | 否 | DiscreteCoreToHTMappin g | 实例的 Cpu 拓扑类型。取值范围： ContinuousCoreToHTM apping：实例的Cpu 拓扑中，实例的同一个Core的 HT是连续的。 DiscreteCoreToHTMapp ing：实例的同一个Core 的HT是离散的。 默认值：无。 使用该参数时请注意： 实例必须为已停止 （Stopped）状态。 仅以下Intel独享型的规格族支持修改CPU拓扑结构： ecs.g6s-k10、ecs.g6s- k25、ecs.g6m-k10、 ecs.g6m-k25 ecs.g7s-k10、ecs.g7s- k25、ecs.g7m-k10、 ecs.g7m-k25、ecs.g7x- k10、ecs.g7x-k25 |
| OSNameEn | String | Query | 否 | Debian 11.1 64 bit | 操作系统的英文显示名称。 |
| SecurityGr oupIds | Repea tList | Query | 否 | sg- bp15ed6xe1yxeycg7**** | 实例重新加入的安全组 ID 数组。使用该参数时请注意： 数组内的安全组ID不能重复，数组长度与实例能够加入安全组配额有关。更多信息，请参见使用限制。 实例会离开当前的安全组，如需保留设置，您需要在数组中添加当前的安全组ID。 支持切换安全组类型，但设置的安全组列表中不能同时包含普通安全组和企业安全组。 安全组必须和实例属于同一个VPC。 说明修改安全组后很快会生效于对应的实例，但可能有较小的延迟。 |

**返回数据**

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyInstanceAttribute &InstanceId=i-bp67acfmxazb4ph*** &DeletionProtection=false &Description=InstanceAttribute &HostName=LocalHost &InstanceName=EcsInstance &Password=EcsV*
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

`XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidInstance Name.Malformed | InvalidInstanceName.Malformed | The specified parameter "InstanceName" is not valid. |
| 400 | Abs.InvalidDescripti on.Malformed | InvalidDescription.Malformed | The specified parameter "Description" is not valid. |
| 400 | NICKNAME ILLEGAL _ | InvalidInstanceName.Malformed | The specified parameter "InstanceName" is not valid. |
| 400 | DESCRIPTION ILLEG _ AL | InvalidDescription.Malformed | The specified parameter "Description" is not valid. |
| 400 | InvalidRemoteConn ectionOptionsPassw ord.ValueNotSuppor ted | InvalidRemoteConnectionOption s.Password | The remote connection password is invalid. |
| 400 | InvalidRemoteConn ectionOptionsType.V alueNotSupported | InvalidRemoteConnectionOption s.Type | The remote connection type is invalid. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidInstanceT ype.ValueNotSuppor ted | InstanceType.ValueNotSupporte d | The instance type not supported. |
| 400 | Abs.InvalidOSType. Malformed | OSType.ValueNotSupported | The OS type is not supported. |
| 400 | -217 | InvalidHostPassword.Malformed | The specified parameter "Password" is not valid. |
| 400 | -251 | InvalidHostName.Malformed | The specified parameter "HostName" is not valid. |
| 400 | HOSTNAME ILLEGAL _ | InvalidHostName.Malformed | The specified parameter "HostName" is not valid. |
| 400 | -7180 | InvalidHostPassword.Malformed | The specified parameter "Password" is not valid. |
| 400 | PASSWORD ILLEGAL _ | InvalidPassword.Malformed | The specified parameter "Password" is not valid. |
| 400 | InvalidUserData.Size Exceeded | InvalidUserData.SizeExceeded | The specified parameter "UserData" exceeds the size. |
| 400 | InvalidUserData.Not Vpc | InvalidUserData.NotSupported | TThe specified parameter "UserData" only support the vpc and IoOptimized Instance. |
| 400 | InvalidUserData.Not Kvm | InvalidUserData.NotSupported | The specified parameter "UserData" only support the vpc and IoOptimized Instance. |
| 400 | ImageNotSupportCl oudInit | ImageNotSupportCloudInit | The specified image does not support cloud-init. |
| 400 | ChargeTypeViolatio n | ChargeTypeViolation | Pay-As-You-Go instances do not support this operation. |
| 400 | FORBIDDEN RECYCL _ EBIN | InvalidParameter.RecycleBin | You do not have permission to set recyclable properties. |
| 400 | InvalidParameter.Cr editSpecification | InvalidParameter.CreditSpecifica tion | The specified CreditSpecification is not supported in this region. |
| 400 | -1033008 | InvalidInstanceStatus.CreditSpec Restricted | The current status of the resource does not support this operation. |
| 400 | INVALID INSTANCE _ _ STATUS FOR MODIF _ _ Y CREDIT SPEC _ _ | InvalidInstanceStatus.NotRunnin g | The current status of the resource is invalid, you can only do this operation when instance is running. |
| 400 | Abs.InvalidPassword .Malformed | InvalidPassword.Malformed | The specified parameter "Password" is not valid. |
| 400 | CLASSIC NOT SUPP _ _ ORT | InvalidNetworkType.NotSupport ed | The classic networkType does not support to modify security group |

|  | 云服务器ECS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | EnterpriseSecurityG roupEniLimitExceed | InvalidOperation.EniCountExcee ded | =The maximum number of eni in a enterprise security group is exceeded. |
| 400 | JoinedGroupLimitExc eed | JoinedGroupLimitExceed | %s |
| 400 | -1000005 | InvalidParameter | The specified parameter is not valid. |
| 400 | InvalidOperation.Inv alidEcsState | InvalidOperation.InvalidEcsState | %s |
| 400 | NOT SUPPORT JUMB _ _ O FRAME _ | InvalidParam.NotSupportJumboF rame | Not support jumbo frame. |
| 400 | -15026 | InvalidOperation.InstanceStatus NotSupport | The instance status is not support modify mtu config. |
| 400 | INSTANCE STATUS _ _ NOT SUPPORT MOD _ _ IFY CPU TOPOLOGY _ _ | InvalidOperation.InstanceStatus Unsupported | The specified instance status does not support modification of cpu topology type. |
| 400 | InvalidParameter.Cp uOptionsTopologyTy pe | InvalidParameter.CpuOptionsTo pologyType | The specified parameter CpuOptions.TopologyType: %s is not valid. |
| 400 | INSTANCE TYPE NO _ _ T SUPPORT CPU TO _ _ _ POLOGY | InvalidInstanceType.NotSupport CpuOptionsTopologyType | The specified instance type does not support CpuOptions.TopologyType: %s. |
| 400 | InvalidAdditionalInfo PvdConfig.SizeExce eded | InvalidAdditionalInfoPvdConfig.Si zeExceeded | The specified parameter AdditionalInfo.PvdConfig exceeds the size. |
| 403 | -215 | IncorrectInstanceStatus | The current status of the resource does not support this operation. |
| 403 | 21001 | InstanceLockedForSecurity | The specified operation is denied as your instance is locked for security reasons. |
| 403 | -503 | OperationDenied | The instance amount in the specified SecurityGroup reach its limit. |
| 403 | -15029 | OperationDenied | The current status of the resource does not support this operation. |
| 403 | InvalidUserData.NotI nWhiteList | InvalidUserData.Forbidden | User not authorized to input the parameter "UserData"please apply for permission "UserData" |
| 403 | IncorrectInstanceSta tus | IncorrectInstanceStatus | The current status of the resource does not support this operation. |
| 403 | InvalidUserData.Bas e64FormatInvalid | InvalidUserData.Base64FormatIn valid | The specified UserData is not valid |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Abs.InvalidInstance ChargeType.WithDel etionProtection | InvalidChargeType.ValueNotSup ported | Deletion protection is only valid for postPaid instance, not for prePaid or spot instance. |
| 403 | 401 | InvalidUser.Unauthorized | The user is not authorized |
| 403 | INSTANCE NOT SUP _ _ PORT MULTI GROUP _ _ TYPE _ | EnterpriseGroupLimited.MutliGro upType | The specified instance can not join multi SecurityGroup types. |
| 403 | SecurityGroupInstan ceLimitExceed | SecurityGroupInstanceLimitExce ed | %s |
| 403 | -506 | InstanceNotInSecurityGroup | The instance not in the group. |
| 403 | RECONFIG GROUP _ _ NOT SUPPORT REGI _ _ ON | InvalidOperation.InvalidRegion | %s |
| 403 | -300 | OperationDenied | The specified Image is disabled or is deleted. |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | InvalidOperation.ResourceMana gedByCloudProduct | %s |
| 403 | InvalidParameter.In validEniQueueNumb er | InvalidParameter.InvalidEniQueu eNumber | %s |
| 403 | InvalidOperation.Ma xEniQueueNumberE xceeded | InvalidOperation.MaxEniQueueN umberExceeded | %s |
| 403 | InvalidOperation.Exc eedInstanceTypeQu eueNumber | InvalidOperation.ExceedInstance TypeQueueNumber | %s |
| 403 | InvalidOperation.Ins tanceTypeNotSuppo rtHighPerformanceT rafficMode | InvalidOperation.InstanceTypeN otSupportHighPerformanceTraffi cMode | %s |
| 403 | InvalidParameter.In validQueuePairNum ber | InvalidParameter.InvalidQueueP airNumber | %s |
| 403 | InvalidOperation.Ma xEniQueuePairNumb erExceed | InvalidOperation.MaxEniQueueP airNumberExceed | %s |
| 403 | InvalidOperation.Eni QueuePairNumberO verflow | InvalidOperation.EniQueuePairN umberOverflow | %s |
| 404 | -205 | InvalidInstanceId.NotFound | The specified InstanceId does not exist. |
| 404 | -560 | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | -1000009 | InvalidInstanceId.NotFound | The specified InstanceId does not exist. |
| 404 | -1033005 | Credit.NotFound | The specified credit information does not exist. |
| 404 | INSTANCE NO EXIS _ _ T | InvalidInstanceId.NotFound | The specified InstanceId does not exist. |
| 404 | -1033013 | InvalidInstanceStatus.NeedResta rt | The current status of the resource is invalid, you can only do this operation after instance is restarted. |
| 404 | InvalidParameter.Se curityGroupIdRepea ted | InvalidParameter.SecurityGroupI dRepeated | The specified security group ids has repeated. |
| 404 | GROUP NOT EXIST _ _ | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |
| 404 | NOT USE TO CLASS _ _ _ IC GROUP _ | InvalidSecurityGroupType.NotSu pportClassic | The specified SecurityGroupIds have classic group type. |
| 404 | GROUP BELONG TO _ _ DIFFERENT VPC _ _ | InvalidSecurityGroupVpc.NotBel ongToOneVpc | The specified SecurityGroupIds are belong to different vpc. |
| 404 | InvalidSecurityGrou pId.NotFound | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |
| 404 | -106 | InvalidInstanceId.NotFound | The specified InstanceId does not exist. |
| 500 | -1 | InternalError | The request processing has failed due to some unknown error. |
| 500 | -1000000 | InternalError | The request processing has failed due to some unknown error. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |
| 500 | InternalError | InternalError | The request processing has failed due to some unknown error, exception or failure. |

##### ModifyInstanceVpcAttribute

调用ModifyInstanceVpcAttribute修改一台专有网络VPC类型ECS实例的专有网络VPC、私网IP地址或虚拟交换机。

**接口说明**

调用该接口时，ECS实例的状态必须是**已停止**（ `Stopped` ）。 当您使用该接口修改实例的私网IP地址或虚拟交换机时，请注意： 新建的ECS实例必须经过重启才能调用该接口。 云服务器ECS 成功修改一次后，ECS实例必须经过重启才能继续调用该接口。 当您使用该接口修改实例的专有网络VPC时，请注意： 实例： 不支持已关联负载均衡实例的ECS实例。 实例的状态不能为已锁定、等待释放中。 实例不能在其它云服务中被使用。例如，实例不能在迁移中、不能已在更换VPC流程中或实例内部署的数据库不能被DTS服务管理等。 网络： 不支持绑定辅助网卡的实例。 不支持已分配IPv6地址的实例。 不支持主网卡有多IP的实例。 传入的虚拟交换机必须属于目标VPC。 修改前后虚拟交换机可用区必须一致。 如果指定主网卡私网IP，则IP必须在虚拟交换机地址段内且可用。如果不指定则随机分配，且目标虚拟交换机的可用IP数充足。 目标VPC的所有者账号（资源所有者），不能将该目标VPC共享给其他账号（资源使用者）使用。 安全组（SecurityGroupId.N）： 安全组的配额与实例能够加入安全组的限制有关。请确保有足够的配额。 安全组所属的VPC必须与目标VPC一致。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyInstanceVp cAttribute | 接口名称。对于您自行拼凑HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值： ModifyInstanceVpcAttribute。 |
| InstanceId | String | 是 | i- bp1iudwa5b1tqa* ***** | 实例ID。 |
| VSwitchId | String | 是 | vsw- bp1s5fnvk4gn3tw ****** | 虚拟交换机ID。 传入的ID为实例的当前虚拟交换机时，表明实例不变更虚拟交换机。 传入的ID为一台新的虚拟交换机时，并且参数 VpcId 为空时，新旧虚拟交换机必须属于同一个可用区、同一个专有网络 VPC。 当参数VpcId不为空时，该参数传入的虚拟交换机ID必须属于 VpcId ，并且和原虚拟交换机属于同一个可用区。 |

云服务器ECS

| PrivateIpAddress | String | 否 | 172.17.**.*** | 新的私网IP地址。 说明 PrivateIpAddress 依赖于 VSwitchId ，指定的IP地址必须在虚拟交换机子网网段中。 默认值：从虚拟交换机子网网段中随机分配。 |
|---|---|---|---|---|
| VpcId | String | 否 | vpc- bp1vwnn14rqpyic zj**** | 目标VPC ID。 |
| SecurityGroupId. N | RepeatLi st | 否 | sg- o6w9l8bc8dgmk w87**** | 实例修改VPC后加入的安全组ID。当且仅当传入VpcId参数时，需要同时传入该参数。 指定实例修改后加入的安全组列表，可以是一个或者多个。参数中N的取值范围与实例能够加入安全组的限制有关。 专有网络类型ECS实例的安全组必须属于 VpcId 所在的VPC。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyInstanceVpcAttribute &InstanceId=i-bp1iudwa5b1tqa****** &VSwitchId=vsw-bp1s5fnvk4gn3tw****** &PrivateIpAddress=172.17.**.*** &VpcId=vpc-bp1vwnn14rqpyiczj**** &SecurityGroupId.N=sg-o6w9l8bc8dgmkw87****
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

云服务器ECS

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 400 | InvalidPrivateIpAddr ess.Malformed | Specified private IP address is malformed. | 指定的私有IP不合法。 |
| 400 | InvalidPrivateIpAddr ess.Duplicated | Specified private IP address is duplicated. | 指定的私网IP已经被使用，请您更换 IP再重试。 |
| 400 | IncorrectVSwitchSta tus | The current status of virtual switch does not support this operation. | 指定的虚拟交换机处于pending状态，无法删除。 |
| 404 | InvalidVSwitchId.Not Found | Specified virtual switch does not exist. | 指定的虚拟交换机ID不存在。 |
| 400 | IncorrectInstanceSta tus | The current status of instance does not support this operation. | 目前实例状态不支持此类操作。 |
| 400 | OperationDenied | Specified operation is denied as your instance is not in VPC. | 该实例不是VPC实例。 |
| 400 | InvalidVSwitchId.Mis match | Specified instance and virtual switch are not in the same zone. | 指定的实例和指定的虚拟交换机不属于同一个可用区。 |
| 400 | InvalidPrivateIpAddr ess.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. | 指定的私网IP不在指定虚拟交换机的网段中。 |
| 404 | InvalidVSwitchId.Not Found | Specified virtual switch is not found in current VPC. | 当前VPC中不存在指定的虚拟交换机。 |
| 400 | InvalidPrivateIp.Cha nging | Previous action is not finished yet. | 实例修改私网IP未完成，不能再进行在修改。 |
| 404 | NoSuchResource | The specified resource is not found. | 指定的资源不存在。 |
| 400 | InvalidPrivateIpAddr ess.Duplicated | error new ip is the same with old ip | 新的IP地址必须不同于旧的IP地址。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | OperationDenied | %s | 拒绝操作。 |
| 404 | InvalidVSwitch.NotB elongToVpc | %s | 指定的VSwitchId不属于指定的 VPC。请检查参数值是否正确。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组ID不存在。 |
| 404 | InvalidSecurityGrou pType.NotSupportCl assic | The specified SecurityGroupIds have classic group type. | 指定的安全组的网络类型为经典网络。请检查SecurityGroupIds参数值是否正确。 |

云服务器ECS

| 404 | InvalidSecurityGrou pVpc.NotBelongToO neVpc | The specified SecurityGroupIds are belong to different vpc. | 指定的安全组ID属于不同的VPC。请检查SecurityGroupIds参数值是否正确。您可以调用 DescribeSecurityGroups查询指定安全组所属的VPC。 |
|---|---|---|---|
| 404 | EnterpriseGroupLimi ted.MutliGroupType | The specified instance can not join multi SecurityGroup types. | 指定的实例不能同时加入普通安全组和企业安全组。您可以调用 DescribeSecurityGroups查询指定安全组的类型。 |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | %s | 云产品托管的安全组不支持修改操作。 |

##### ModifyInstanceVncPasswd

调用ModifyInstanceVncPasswd修改一台ECS实例的Web管理终端密码。

**接口说明**

密码长度必须是六位字符，只支持大小写英文字母和阿拉伯数字。 修改密码后： I/O优化的实例，立刻生效，无需重启实例。 非I/O优化的实例，需要在控制台重启实例或者调用API （RebootInstance）才能生效。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyInstanceVn cPasswd | 系统规定参数。取值： ModifyInstanceVncPasswd |
| InstanceId | String | 是 | i- bp67acfmxazb4p h*** | ECS实例ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | ECS实例所在的地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| VncPassword | String | 是 | 123456 | 新的ECS实例管理终端连接密码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例云服务器ECS

```
https://ecs.example.com/?Action=ModifyInstanceVncPasswd &RegionId=cn-qingdao-env17-d01 &InstanceId=i-bp67acfmxazb4ph*** &VncPassword=123456
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>FDB6C963-9CE8-4B7F-BCA3-845F6BD29AFC</RequestId>
```

`JSON` 格式

```json
{
      "RequestId": "FDB6C963-9CE8-4B7F-BCA3-845F6BD29AFC"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域ID不存在。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 400 | IncorrectVncPasswo rd.Malformed | The specified parameter VncPassword is not valid. | 指定的VNC密码不合法。 |
| 404 | NoSuchResource | The specified resource is not found. | 指定的资源不存在。 |

##### ModifyInstanceMetadataOptions

调用ModifyInstanceMetadataOptions修改一台实例的元数据信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyInstanceM etadataOptions | 系统规定参数。取值： ModifyInstanceMetadataOptions。 |

云服务器ECS

| HttpEndpoint | String | 是 | enabled | 是否启用实例元数据的访问通道。取值范围： enabled：启用。 disabled：禁用。 默认值：enabled。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao-**** | 实例所在地域的ID。您可以调用 DescribeRegions查询地域ID。 |
| InstanceId | String | 否 | i- bp67acfmxaz**** | 指定的实例ID。 |
| HttpTokens | String | 否 | required | 访问实例元数据时是否强制使用加固模式 （IMDSv2）。取值范围： optional：不强制使用。 required：强制使用。设置该取值后，普通模式无法访问实例元数据。 默认值：optional。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=ModifyInstanceMetadataOptions &HttpEndpoint=enabled &RegionId=cn-qingdao-**** &HttpEndpoint=enabled &HttpTokens=required
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

云服务器ECS

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidHttpEndpoint. NotSupported | The specified HttpEndpoint not supported, you can use enabled(default) or disabled. | 指定的参数 HttpEndpoint 值非法， 请使用enabled（默认）或者 disabled。 |
| 400 | InvalidHttpTokens.N otSupported | The specified HttpTokens not supported, you can use optional(default) or required. | 指定的参数 HttpTokens 值非法，请使用optional（默认）或者 required。 |
| 400 | InvalidHttpPutRespo nseHopLimit.NotSup ported | The specified HttpPutResponseHopLimit not supported, more than 1 and less than 64 is reasonable. | 指定的参数 HttpPutResponseHopLimit 值非法，取值范围必须大于等于1且小于等于64。 |

##### DescribeInstanceTypes

调用DescribeInstanceTypes查询云服务器ECS提供的实例规格资源。 接口说明 DescribeInstanceTypes仅查询实例规格的配置和性能信息。如果您需要查询指定地域或可用区的资源列表，

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 否 | cn-qingdaoenv17-d01 | 实例所属的地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| Action | String | Query | 是 | DescribeInstanceTypes | 系统规定参数。取值： DescribeInstanceTypes |
| InstanceTy peFamily | String | Query | 否 | ecs.g6 | 实例规格所属的规格族。取值请参见 DescribeInstanceTypeFa milies。 更多详情，请参见 《云服务器ECS实例规格族& 实例规格简介》中实例规格章节。 |
| InstanceTy pes | Repea tList | Query | 否 | ecs.g6.large | 指定查询的实例规格。当该参数不传值时，默认查询所有实例规格的信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| InstanceTypes | Array | \ | 实例规格族集合。 |
| - EniTotalQuantit y | Integer | 0 | 说明该参数暂未支持。 |
| - LocalStorageCa tegory | String | local ssd pro _ _ | 本地盘类型。可能值： local hdd pro：实例规格 _ _ 族d1搭载的SATA HDD本地盘。 local ssd pro： _ _ 实例规格族i2和gn5等搭载的NVMe SSD本地盘。 |
| - PrimaryEniQue ueNumber | Integer | 4 | 主网卡默认队列数。 |
| -MemorySize | Float | 8.0 | 内存大小，单位GiB。 |
| - LocalStorageCa pacity | Long | 2048 | 实例挂载的本地盘的单盘容量，单位：GiB。 |
| - InstanceFamily Level | String | EnterpriseLevel | 实例规格族级别。可能值： EntryLevel：入门级。 EnterpriseLevel：企业级。 CreditEntryLevel： 积分入门级。 |
| -InstancePpsRx | Long | 300000 | 内网入方向网络收发包能力，单位：Pps。 |
| - EniIpv6Address Quantity | Integer | 1 | 单块弹性网卡的IPv6地址上限。 |
| - MaximumQueu eNumberPerEni | Integer | 4 | 单块弹性网卡最大队列数。包括主网卡及辅助网卡支持的队列数。 |
| - InstanceTypeId | String | ecs.g5.large | 实例规格ID。 |
| - InstanceBandwi dthRx | Integer | 1024000 | 内网入方向带宽限制，单位：kbit/s。 |
| - SecondaryEniQ ueueNumber | Integer | 4 | 辅助弹性网卡默认队列数。 |
| -GPUSpec | String | NVIDIA V100 | GPU类型。 |
| - InstanceBandwi dthTx | Integer | 1024000 | 内网出方向带宽限制，单位：kbit/s。 |
| - QueuePairNum ber | Integer | 22 | 单块弹性RDMA网卡（ERI）的QP（QueuePair） 队列数上限。 |

|  | 开发指南·API参考 |  |  | 云服务器EC | S |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -EriQuantity | Integer | 0 | 弹性RDMA网卡（ERI）数量。 |
| -GPUAmount | Integer | 2 | GPU数量。 |
| - TotalEniQueue Quantity | Integer | 128 | 实例规格允许修改的队列数配额。 说明主网卡队列数不累计在内。 |
| -NvmeSupport | String | unsupported | 实例规格所挂载的云盘是否支持NVMe。可能值： required：支持。表示云盘以NVMe的方式挂载。 unsupported：不支持。表示云盘不以NVMe的方式挂载。 |
| -DiskQuantity | Integer | 17 | 支持挂载的云盘数量上限。 |
| -InitialCredit | Integer | 120 | 突发性能实例t5的初始vCPU积分值。 |
| - LocalStorageA mount | Integer | 1 | 实例挂载的本地盘的数量。 |
| -BaselineCredit | Integer | 4 | 突发性能实例t5的基准vCPU计算性能（所有vCPU 之和）。 |
| -InstancePpsTx | Long | 300000 | 内网出方向网络收发包能力，单位：Pps。 |
| - EniPrivateIpAdd ressQuantity | Integer | 6 | 单块弹性网卡的私有IP地址上限。 |
| -CpuCoreCount | Integer | 8 | vCPU数量。 |
| - InstanceTypeFa mily | String | ecs.g5 | 实例规格族。 |
| -EniQuantity | Integer | 2 | 支持挂载的弹性网卡上限。 |
| - EniTrunkSuppor ted | Boolean | true | 说明该参数暂未支持。 |
| RequestId | String | 00827261-20B7- 4562-83F2- 4DF3987XXXXX | 请求ID。 |
| NextToken | String | e71d8a535bd9**** | 本次调用返回的查询凭证（Token）。 |

**示例**

云服务器ECS 请求示例

```
https://ecs.example.com/?Action=DescribeInstanceTypes &InstanceTypeFamily=ecs.g6
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "NextToken": "e71d8a535bd9****",
    "RequestId": "00827261-20B7-4562-83F2-4DF3987XXXXX",
    "InstanceTypes": {
        "InstancePpsTx": 300000,
        "NvmeSupport": "unsupported",
        "PrimaryEniQueueNumber": 4,
        "TotalEniQueueQuantity": 128,
        "LocalStorageCapacity": 2048,
        "InstanceTypeFamily": "ecs.g5",
        "InstancePpsRx": 300000,
        "EriQuantity": 0,
        "InstanceBandwidthRx": 1024000,
        "InstanceBandwidthTx": 1024000,
        "LocalStorageAmount": 1,
        "SecondaryEniQueueNumber": 4,
        "LocalStorageCategory": "local_ssd_pro",
        "GPUSpec": "NVIDIA V100",
        "InstanceTypeId": "ecs.g5.large",
        "MemorySize": 8,
        "MaximumQueueNumberPerEni": 4,
        "EniIpv6AddressQuantity": 1,
        "CpuCoreCount": 8,
        "InitialCredit": 120,
        "EniQuantity": 2,
        "GPUAmount": 2,
        "DiskQuantity": 17,
        "QueuePairNumber": 22,
        "BaselineCredit": 4,
        "InstanceFamilyLevel": "EnterpriseLevel",
        "EniPrivateIpAddressQuantity": 6
    }
}
```

`XML` 格式云服务器ECS

```xml
<NextToken>e71d8a535bd9****</NextToken> <RequestId>00827261-20B7-4562-83F2-4DF3987XXXXX</RequestId> <InstanceTypes>
    <InstancePpsTx>300000</InstancePpsTx>
    <NvmeSupport>unsupported</NvmeSupport>
    <PrimaryEniQueueNumber>4</PrimaryEniQueueNumber>
    <TotalEniQueueQuantity>128</TotalEniQueueQuantity>
    <LocalStorageCapacity>2048</LocalStorageCapacity>
    <InstanceTypeFamily>ecs.g5</InstanceTypeFamily>
    <InstancePpsRx>300000</InstancePpsRx>
    <EriQuantity>0</EriQuantity>
    <InstanceBandwidthRx>1024000</InstanceBandwidthRx>
    <InstanceBandwidthTx>1024000</InstanceBandwidthTx>
    <LocalStorageAmount>1</LocalStorageAmount>
    <SecondaryEniQueueNumber>4</SecondaryEniQueueNumber>
    <LocalStorageCategory>local_ssd_pro</LocalStorageCategory>
    <GPUSpec>NVIDIA V100</GPUSpec>
    <InstanceTypeId>ecs.g5.large</InstanceTypeId>
    <MemorySize>8</MemorySize>
    <MaximumQueueNumberPerEni>4</MaximumQueueNumberPerEni>
    <EniIpv6AddressQuantity>1</EniIpv6AddressQuantity>
    <CpuCoreCount>8</CpuCoreCount>
    <InitialCredit>120</InitialCredit>
    <EniQuantity>2</EniQuantity>
    <GPUAmount>2</GPUAmount>
    <DiskQuantity>17</DiskQuantity>
    <QueuePairNumber>22</QueuePairNumber>
    <BaselineCredit>4</BaselineCredit>
    <InstanceFamilyLevel>EnterpriseLevel</InstanceFamilyLevel>
    <EniPrivateIpAddressQuantity>6</EniPrivateIpAddressQuantity>
</InstanceTypes>
```

##### SoftDeleteInstances

**接口说明**

软删除是一种新的删除ECS资源的方式。区别于DeleteInstance，软删除ECS实例后，该ECS实例会进入回收站并处于冷冻期（由Hours指定）。冷冻期内，实例的CPU、内存等计算资源被释放，弹性公网IP被解绑，存储资源保留；冷冻期过后，ECS所有资源（包含存储资源）会被彻底销毁，不可恢复。 软删除实例时，您需要注意： 软删除不支持带有本地盘的规格族的ECS实例。 ECS实例状态必须为**已停止**（Stopped）或**运行中**（Running）。 软删除实例后，该实例处于冷冻期，仅支持恢复和删除操作，不支持解除、添加与其它产品的关联（如挂载云盘、卸载云盘）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云服务器ECS

| Action | String | 是 | SoftDeleteInstanc es | 系统规定参数。取值： SoftDeleteInstances。 |
|---|---|---|---|---|
| InstanceId.N | RepeatLi st | 是 | i- bp1g6zv0ce8ogh u7k*** | 待软删除的实例ID。您可以调用 DescribeInstances查看实例ID。 N指软删除的实例数，N的取值范围： 1~100。 |
| RegionId | String | 是 | cn-qingdao-****- d01 | 实例所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| Hours | Integer | 否 | 72 | 冷冻时间，单位：小时，取值范围： 1~720。 默认值：72 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见云服务器ECS开发指南中的如何保证幂等性章节。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=SoftDeleteInstances &InstanceId.1=i-bp1g6zv0ce8oghu7k*** &RegionId=cn-qingdao-****-d01 &Hours=72
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>
     473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E
</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |

##### RestoreSoftDeletedInstances

调用RestoreSoftDeletedInstances恢复一个或多个被软删除的ECS实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceRegi onId | String | Host | 否 | - | 鉴权相关的系统参数，不填。 |
| Action | String | Query | 是 | RestoreSoftDeletedInstan ces | 系统规定参数。取值： RestoreSoftDeletedInstan ces。 |
| OwnerId | Long | Query | 否 | - | 鉴权相关的系统参数，不填。 |
| ResourceO wnerAccou nt | String | Query | 否 | - | 鉴权相关的系统参数，不填。 |
| ResourceO wnerId | Long | Query | 否 | - | 鉴权相关的系统参数，不填。 |
| InstanceId | Repea tList | Query | 是 | i-bp67acfmxazb4p**** | 指定的实例ID。您可以调用 DescribeInstances 查询实例ID。 |
| OwnerAcco unt | String | Query | 否 | - | 鉴权相关的系统参数，不填。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AttemptSt artVm | Boole an | Query | 否 | true | 恢复后是否尝试启动ECS实例。取值范围： true：启动 false：不启动默认值：true |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多详情，请参见云服务器 ECS开发指南中的如何保证幂等性章节。 |
| RegionId | String | Query | 是 | cn-qingdao-****-d01 | 实例所属的地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RestoreSoftDeletedInstances &InstanceId=i-bp67acfmxazb4p**** &RegionId=cn-qingdao-****-d01
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

`XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

**错误码**

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | MULTI ECS BUSINES _ _ S STATUS ILLEGAL _ _ | IncorrectInstanceStatus | %s |
| 403 | LOCAL TASK SUBMI _ _ T PART FAILED _ _ | OperateFail.PartOfInstances | %s |
| 403 | LOCAL TASK SUBMI _ _ T ALL FAILED _ _ | OperateFail.AllInstances | %s |
| 403 | InvalidParameter.IN VALID INSTANCE ID _ _ S TOO MANY _ _ | InvalidParameter.TooManyInstan ceIds | Instance ids cannot be more than 100. |
| 404 | INSTANCE NO EXIS _ _ T | InvalidInstanceId.NotFound | The specified InstanceId does not exist. |

#### 专有宿主机

##### AllocateDedicatedHosts

调用AllocateDedicatedHosts创建一台或多台专有宿主机。专有宿主机是单租户独享的物理机资源，您可以在

**接口说明**

创建专有宿主机前，您可以调用DescribeAvailableResource查看指定地域或者可用区内的资源供给情况。 创建成功后，您可以将返回的专有宿主机ID列表作为请求参数，调用DescribeDedicatedHosts查询新建专有宿主机状态。 提交创建专有宿主机的请求后，指定的参数值不合规或者库存不足时会报错。具体的报错原因，请参见错误码。 创建专有宿主机后，您可以调用ModifyInstanceDeployment将ECS实例从共享宿主机迁移到专有宿主机，

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | AllocateDedicate dHosts | 系统规定参数，取值： AllocateDedicatedHosts。 |
| DedicatedHostT ype | String | 是 | ddh.c5 | 专有宿主机的规格。您可以调用 DescribeDedicatedHostTypes接口获得最新的专有宿主机规格表。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 专有宿主机所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| Tag.N.Key | String | 否 | Environment | 专有宿主机的标签键。N的取值范围：1~20 一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以aliyun或者acs:开头，不能包含http://或者https://。 |
|---|---|---|---|---|
| Tag.N.Value | String | 否 | Production | 专有宿主机的标签值。N的取值范围：1~20 一旦传入该值，可以为空字符串。最多支持 128个字符，不能以acs:开头，不能包含 http://或者https://。 |
| ResourceGroupI d | String | 否 | rg- bp67acfmxazb4p h*** | 专有宿主机要加入的资源组ID。 |
| ZoneId | String | 否 | cn-qingdao- env17- amtest11001-a | 专有宿主机所属的可用区编号。 默认值：空，表示由系统选择。 |
| DedicatedHost Name | String | 否 | myDDH | 专有宿主机的名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以http://和https://开头。可以包含数字、 半角冒号（:）、下划线（ ）或者连字符 _ （-）。 |
| ActionOnMainte nance | String | 否 | Migrate | 当专有宿主机发生故障或者在线修复时，为其所宿实例设置迁移方案。取值范围： Migrate：迁移实例到其他物理机并重新启动实例。 当专有宿主机上挂载云盘存储时，默认值：Migrate。 Stop：在当前专有宿主机上停止实例，确认无法修复专有宿主机后，迁移实例到其他物理机并重新启动实例。 当专有宿主机上挂载本地盘存储时，默认值：Stop。 |
| NetworkAttribu tes.SlbUdpTime out | Integer | 否 | 60 | 负载均衡连接的UDP会话超时时间，单位： 秒。取值范围：15~310 |
| NetworkAttribu tes.UdpTimeout | Integer | 否 | 60 | 为专有宿主机上运行的云服务设置用户访问的UDP会话超时时间，单位：秒。取值范围：15~310 |
| Description | String | 否 | This-is-my-DDH | 专有宿主机的描述。长度为2~256个英文或中文字符，不能以http://和https://开头。 |

云服务器ECS

| AutoPlacement | String | 否 | off | 专有宿主机是否加入自动部署资源池。当您在专有宿主机上创建实例，却不指定DedicatedHostId时，阿里云将自动从加入资源池的专有宿主机中，为您选取适合的宿主机部署实例。取值范围： on：加入自动部署资源池。 off：不加入自动部署资源池。 默认值：on。 说明若您不希望专有宿主机加入自动部署资源池，请将该参数设置为 off。 |
|---|---|---|---|---|
| Quantity | Integer | 否 | 1 | 本次创建的专有宿主机的数量。取值范围： 1~100。 默认值：1。 |
| AutoReleaseTi me | String | 否 | 2019-08- 21T12:30:24Z | 专有宿主机自动释放时间。需按照ISO8601 标准表示，并使用UTC+0时间，格式为 yyyy-MM-ddTHH:mm:ssZ。 说明最短设置为当前时间之后半小时。 最长不能超过当前时间之后三年。 若参数值中的秒（ss）不是 00，则自动取为00。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见《云服务器ECS开发指南》中的如何保证幂等性章节。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DedicatedHostI dSets | List | "DedicatedHostIdSe ts": {"DedicatedHostId": ["dh- bp67acfmxazb4ph** *", "dh- bp67acfmxazb4pi** *"]} | 专有宿主机ID（DedicatedHostId）组成的列表。 |
| RequestId | String | E2A664A6-2933- 4C64-88AE- 5033D003EADF | 请求ID。 |

云服务器ECS

**示例**

请求示例

```
https://ecs.example.com/?Action=AllocateDedicatedHosts &RegionId=cn-qingdao-env17-d01 &DedicatedHostType=ddh.sn1ne &Quantity=2 &ClientToken=123e4567-e89b-12d3-a456-426655440000
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>E2A664A6-2933-4C64-88AE-5033D003EADF</RequestId>
    <DedicatedHostIdSets>
        <DedicatedHostId>dh-bp67acfmxazb4ph***</DedicatedHostId>
        <DedicatedHostId>dh-bp67acfmxazb4pi***</DedicatedHostId>
    </DedicatedHostIdSets>
```

`JSON` 格式

```json
{
    "RequestId":"E2A664A6-2933-4C64-88AE-5033D003EADF",
    "DedicatedHostIdSets":{
        "DedicatedHostId":[
            "dh-bp67acfmxazb4ph***",
            "dh-bp67acfmxazb4pi***"
```

]

```
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInstanceType. ValueUnauthorized | The specified InstanceType is not authorized. | 指定的实例规格未授权使用。 |
| 400 | InvalidDescription.M alformed | The specified parameter "Description" is not valid. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
| 403 | OperationDenied | The creation of Host to the specified Zone is not allowed. | 无法在指定可用区创建专用宿主机。 |
| 403 | OperationDenied.No Stock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. | 库存不足。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

云服务器ECS

| 403 | OperationDenied | Sales of this resource are temporarily suspended in the specified region; please try again later. | 指定的地域暂时关闭了此资源的售卖，请稍后重试。 |
|---|---|---|---|
| 400 | InvalidParameter.Co nflict | The specified region and cluster do not match. | 指定的地域与指定的集群不匹配。 |
| 403 | NodeControllerUnav ailable | The Node Controller is temporarily unavailable. | 节点控制器暂不可用。 |
| 404 | OperationDenied | Another Host has been creating | 另一个宿主机正在创建。 |
| 403 | OperationDenied | The resource is out of usage. | 该实例不在运行状态，请您启动实例或检查操作是否合理。 |
| 404 | PaymentMethodNot Found | No payment method has been registered on the account. | 账户尚未注册支付方式。 |
| 404 | InvalidDedicatedHos tName.Malformed | The specified parameter DedicatedHostName is not valid. | 指定的参数“DedicatedHostName”无效。 |
| 403 | InvalidParameter.Re sourceOwnerAccoun t | ResourceOwnerAccount is Invalid. | 指定的 ResourceOwnerAccount 不合法。 |
| 403 | InvalidUserData.For bidden | User not authorized to input the parameter "UserData", please apply for permission "UserData" | 您没有操作“UserData”的权限，或者权限不足，请先申请权限。 |
| 403 | Zone.NotOpen | The specified zone is not granted to you to buy resources yet. | 用户未被授权购买指定的可用区的资源。 |
| 403 | Zone.NotOnSale | The specified zone is not available for purchase. | 指定可用区已经售罄，请您更换实例规格或者更换地域创建。 |
| 403 | InvalidDedicatedHos tType.ValueNotSupp orted | The specified DedicatedHostType does not exist or beyond the permitted range. | 指定的宿主机规格不存在。 |
| 403 | InvalidDedicatedHos tType.ZoneNotSupp orted | The specified zone does not support this dedicatedHostType. | 指定可用区不支持指定宿主机规格。 |
| 400 | InvalidAutoRenewPe riod.ValueNotSuppor ted | The specified autoRenewPeriod is not valid. | 指定的参数 AutoReleaseTime 不合法。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键不合法。 |
| 400 | InvalidDedicatedHos tType.ValueNotSupp orted | %s | 指定的专有宿主机类型无效。 |
| 400 | RegionUnauthorized | %s | 该地域未被授权。 |
| 500 | InternalError | %s | 内部错误。 |
| 400 | Zone.NotOnSale | %s | 该可用区暂时关闭了售卖。 |

云服务器ECS

| 400 | OperationDenied | The specified DedicatedHostType or Zone is not available or not authorized. | 指定宿主机规格、可用区不可用或者没有操作的权限。 |
|---|---|---|---|
| 400 | InvalidPeriodUnit.Val ueNotSupported | The specified parameter PeriodUnit is not valid. | 参数“PeriodUnit”无效。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值不合法。 |
| 403 | InvalidParameter.No tMatch | %s | 您输入的参数无效，请检查参数之间是否冲突。 |
| 403 | Account.Arrearage | Your account has been in arrears. | 账户余额不足，请先充值再操作。 |
| 400 | QuotaExceed.Afterp ayDedicatedHost | The maximum number of Pay- As-You-Go DedicatedHosts is exceeded: %s | 按量付费的宿主机库存不足，请减少创建数量。 |
| 400 | InvalidChargeType.V alueNotSupported | ChargeType is not valid | 付费类型无效。 |
| 400 | InvalidParameter.Sl bUdpTimeout | The specified value is invalid. | 指定的参数“SlbUdpTimeout”无效。 |
| 400 | InvalidParameter.Ud pTimeout | The specified value is invalid. | 指定的参数“UdpTimeout”无效。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |

##### ModifyDedicatedHostAttribute

调用ModifyDedicatedHostAttribute修改一台专有宿主机的部分信息，包括专有宿主机的名称、描述和服务不可用属性等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDedicated HostAttribute | 系统规定参数。取值： ModifyDedicatedHostAttribute。 |
| DedicatedHostId | String | 是 | dh- bp165p6xk2tlw6 1e**** | 专有宿主机ID。 |
| RegionId | String | 是 | cn-qingdao-**** | 专有宿主机所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| DedicatedHostNa me | String | 否 | myDDH | 专有宿主机名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 或者 https:// 开头。可以包含数字、半角冒号（:）、下划线（ ） _ 或者短划线（-）。 |

云服务器ECS

| Description | String | 否 | this-is-my-ddh | 专有宿主机的描述。长度为2~256个英文或中文字符，不能以 http:// 或者 https:// 开头。 |
|---|---|---|---|---|
| ActionOnMainten ance | String | 否 | Migrate | 当专有宿主机发生故障或者在线修复时，为其所宿实例设置迁移方案。取值范围： Migrate：迁移实例到其他物理机并重新启动实例。 Stop：在当前专有宿主机上停止实例，确认无法修复专有宿主机后，迁移实例到其他物理机并重新启动实例。 当专有宿主机上挂载的是云盘时，默认值： Migrate。 当专有宿主机上挂载的是本地盘时，默认值：Stop。 |
| NetworkAttribute s.SlbUdpTimeout | Integer | 否 | 60 | 负载均衡连接的UDP会话超时时间，单位： 秒。取值范围：15~310。 |
| NetworkAttribute s.UdpTimeout | Integer | 否 | 60 | 为专有宿主机上运行的云服务设置用户访问的UDP会话超时时间，单位：秒。取值范围：15~310。 |
| AutoPlacement | String | 否 | on | 设置专有宿主机是否加入自动部署资源池。 当您在专有宿主机上创建实例，却不指定DedicatedHostId时，阿里云自动从资源池中选取专有宿主机放置实例。取值范围： on：加入自动部署资源池。 off：不加入自动部署资源池。 |
| DedicatedHostClu sterId | String | 否 | dc- bp165p6xk2tlw6 1e**** | 专有宿主机集群ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 2A4EA075-CB5B- 41B7-B0EB- 70D339F***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=ModifyDedicatedHostAttribute &DedicatedHostId=dh-bp165p6xk2tlw61e**** &RegionId=cn-qingdao-****
```

`&<`公共请求参数> 正常返回示例云服务器ECS `XML` 格式

```xml
    <RequestId>2A4EA075-CB5B-41B7-B0EB-70D339F*****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"2A4EA075-CB5B-41B7-B0EB-70D339F*****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDedicatedHos tName.Malformed | The specified parameter DedicatedHostName is not valid. | 指定的参数DedicatedHostName无效。 |
| 400 | InvalidDescription.M alformed | The specified parameter Description is not valid. | 指定的资源描述格式不合法。长度为 2-256 个字符，不能以 http:// 和 https:// 开头。 |
| 400 | InvalidParameter.Sl bUdpTimeout | The specified value is invalid. | 指定的参数 SlbUdpTimeout 无效。 |
| 400 | InvalidParameter.Ud pTimeout | The specified value is invalid. | 指定的参数 UdpTimeout 无效。 |
| 403 | InvalidUser.Unautho rized | The user is not authorized | 您当前使用的账号无权限。 |
| 404 | InvalidDedicatedHos tId.NotFound | The specified DedicatedHostId does not exist. | 指定的专有宿主机不存在。 |

##### ModifyInstanceDeployment

调用ModifyInstanceDeployment修改ECS实例的部署集，或迁移ECS实例至专有宿主机。支持在迁移ECS实例的同时变更实例规格。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ModifyInstanceDeployme nt | 系统规定参数。取值： ModifyInstanceDeployme nt |
| RegionId | String | Query | 是 | cn-qingdao-env17-d01 | 实例所在的地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | String | Query | 是 | i-bp67acfmxazb4ph*** | 实例ID。 |
| Dedicated HostId | String | Query | 否 | dh-bp67acfmxazb4ph*** | 专有宿主机ID。调用 DescribeDedicatedHosts 查看可以使用的专有宿主机。 修改ECS实例宿主机（即将 ECS实例从共享宿主机迁移至专有宿主机，或在不同专有宿主机间迁移ECS实例）时： 若将实例迁移至指定专有宿主机上，必须设置该参数。 若将实例迁移至系统自动为您选择的专有宿主机上，必须将该参数设置为空，并将参数Tenancy设置为host。 |
| Deployme ntSetId | String | Query | 否 | ds-bp67acfmxazb4ph*** | 部署集ID。 将ECS实例加入一个部署集， 或调整ECS实例的部署集时， 该参数为必填参数。 修改专有宿主机实例相关参数（Tenancy、 Affinity和 DedicatedHostId） 时，不可同时修改部署集。 |
| Deployme ntSetGrou pNo | Intege r | Query | 否 | 3 | 当 ECS 实例要加入或调整的部署集策略为部署集组高可用策略（AvailabilityGroup） 时，可以通过该参数指定实例在部署集中的分组号。取值范围：1~7。 如果您为 ECS 实例调整部署集，且部署集策略为部署集组高可用策略 （AvailablilityGroup ），当不指定该参数时，系统会自动在各组之间均衡分配 ECS 实例。如果您为 ECS 实例指定的仍是当前实例所属的部署集，系统也会重新在各组之间均衡分配 ECS 实例。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Force | Boole an | Query | 否 | false | 是否强制更换实例宿主机。取值范围： true：允许。允许重启运行中（Running）、已停止（Stopped）状态的 ECS实例。 已停止状态的实例不包括开启停机不收费功能的按量付费ECS实例。 false（默认）：不允许。 只在当前宿主机上加入部署集。这可能导致更换部署集失败。 |
| Affinity | String | Query | 否 | host | 实例是否与专有宿主机关联。 取值范围： host：关联。已开启停机不收费功能的实例停机后再次启动时，仍部署在原专有宿主机上。 default：不关联。已开启停机不收费功能的实例停机后再次启动时，若原专有宿主机资源不足，可迁移至自动部署资源池中的其它专有宿主机上。 实例从共享宿主机迁移至专有宿主机时，默认值： default。 |
| Tenancy | String | Query | 否 | host | 实例是否在专有宿主机上部署。取值范围：host（实例在专有宿主机上部署）。 |
| MigrationT ype | String | Query | 否 | live | 是否先停止实例，再迁移到目标专有宿主机。取值范围： reboot（默认）：先停止实例再迁移。 live：不停止实例，直接迁移。此时，您必须指定参数DedicatedHostId。该取值不支持在迁移ECS实例的同时变更实例规格。 默认值：reboot。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceTy pe | String | Query | 否 | ecs.c6.large | ECS实例要变更的目标实例规格。调用 DescribeInstanceTypes接口可获取最新实例规格列表。 修改ECS实例宿主机时，可同时变更ECS实例规格。目标实例规格必须与指定专有宿主机的规格相匹配。 变更实例规格时，必须指定专有宿主机ID，即设置参数DedicatedHostId的值。 使用自动部署功能迁移ECS 实例时，不能变更实例规格。 |
| Dedicated HostCluste rId | String | Query | 否 | dc-bp67acfmxazb4ph**** | 专有宿主机集群 ID。 |
| RemoveFr omDeploy mentSet | Boole an | Query | 否 | false | 是否将所选实例移出所选部署集。取值范围： true：是。 false：否。 默认值：false。 当该参数为true 时，必须指定具有所属关系的 InstanceId 和 DeploymentSetId。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE73368 | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyInstanceDeployment &InstanceId=i-bp67acfmxazb4ph**** &RegionId=cn-qingdao-env17-d01 &DedicatedHostId=dh-bp67acfmxazb4ph**** &Tenancy=host &MigrationType=live
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式云服务器ECS

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE73368"
}
```

`XML` 格式

```xml
      <RequestId>04F0F334-1335-436C-A1D7-6C044FE73368</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDedicatedHos tId.NotFound | The specified DedicatedHostId does not exist. | 指定的专有宿主机不存在。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 400 | OperationDenied.Un stoppedInstance | Operation denied due to unstopped instance. | 当前操作无效，请确认实例是否已停止。 |
| 400 | InvalidDedicatedHos tStatus.NotSupport | Operation denied due to dedicated host status. | 专有宿主机当前的状态不支持此操作。 |
| 400 | InvalidPeriod.Excee dedDedicatedHost | Instance expired date can't exceed dedicated host expired date. | 实例过期日期不能超过专有宿主机的过期日期。 |
| 404 | InvalidInstanceNetw orkType.NotSupport | The specified Instance network type not support. | 当前实例的网络类型不支持此操作。 |
| 404 | InvalidInstanceType. NotSupport | The Dedicated host not support the specified instance type. | 当前宿主机不支持指定的实例规格。 |
| 400 | OperationDenied.Lo calDiskInstance | Operation denied due to instance has local disk | 由于实例具有本地磁盘，此操作被拒绝。 |
| 403 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 400 | InvalidParam.Tenan cy | The specified Tenancy is invalid. | 您指定的参数“Tenancy”无效。 |
| 403 | OperationDenied.No Stock | The resource is out of usage. | 该实例不在运行状态，请您启动实例或检查操作是否合理。 |
| 400 | ChargeTypeViolatio n.PostPaidDedicated Host | Prepaid instance onto postpaid dedicated host is not allowed | 包年包月的实例无法添加到按量付费的专有宿主机上。 |
| 400 | InvalidInstanceType. ValueNotSupported | The specified InstanceType does not exist or beyond the permitted range. | 您指定的实例规格不存在，或者您没有权限操作此规格的实例。 |

云服务器ECS

##### DescribeDedicatedHostTypes

调用DescribeDedicatedHostTypes查询指定地域下支持的专有宿主机规格详细参数，或者查询专有宿主机支持的ECS实例规格族。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeDedicate dHostTypes | 系统规定参数，取值： DescribeDedicatedHostTypes。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 专有宿主机所在地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| DedicatedHostT ype | String | 否 | ddh.sn1ne | 专有宿主机规格。 |
| SupportedInsta nceTypeFamily | String | 否 | ecs.sn1ne | 专有宿主机规格支持的ECS实例规格族。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DedicatedHost Types | Array |  | 返回专有宿主机规格的信息。 |
| DedicatedHost Type |  |  |  |
| Cores | Integer | 2 | 单个物理CPU的核数。 |
| DedicatedHost Type | String | ddh.sn1ne | 专有宿主机规格类型。如果您需要使用更多专有宿主机规格，可以提交工单联系阿里云。 |
| GPUSpec | String | gpu | GPU型号。 |
| LocalStorageA mount | Integer | 0 | 专有宿主机上的本地盘数量。 |
| LocalStorageCa pacity | Long | 0 | 一块本地盘容量，单位：GiB。 |
| LocalStorageCa tegory | String | local | 本地盘类型。 |
| MemorySize | Float | 112.0 | 内存容量，单位：GiB。 |
| PhysicalGpus | Integer | 2 | 物理GPU数量。 |

云服务器ECS

| Sockets | Integer |  |  | 2 | 物理处理器（CPU）数量。 |  |  |
|---|---|---|---|---|---|---|---|
| SupportedInsta nceTypeFamilie s | List |  |  | ecs.sn1ne | 专有宿主机规格支持的ECS实例的规格族。可能值： "SupportedInstanceTypeFamily": [ecs.sn1ne] |  |  |
|  |  |  |  |  |  | "SupportedInstanceTypeFamily": |  |
|  |  |  |  |  | [ecs.sn1ne] |  |  |
| SupportedInsta nceTypesList | List |  |  | ecs.sn1ne | 专有宿主机规格支持的ECS实例规格族。可能值： "SupportedInstanceTypesList": [ecs.sn1ne] |  |  |
|  |  |  |  |  |  | "SupportedInstanceTypesList": |  |
|  |  |  |  |  | [ecs.sn1ne] |  |  |
| TotalVcpus | Integer |  |  | 56 | 虚拟CPU总核数。 |  |  |
| TotalVgpus | Integer |  |  | 10 | 虚拟GPU总核数。 |  |  |
| RequestId | String |  |  | 5FE5FF06-3A33- 4658-8495- 6445FC54E327 | 请求ID。 |  |  |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeDedicatedHostTypes &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
    <DedicatedHostTypes>
        <DedicatedHostType>
            <LocalStorageAmount>0</LocalStorageAmount>
            <Sockets>2</Sockets>
            <DedicatedHostType>ddh.sn1ne</DedicatedHostType>
            <LocalStorageCapacity>0</LocalStorageCapacity>
            <SupportedInstanceTypeFamilies>
                <SupportedInstanceTypeFamily>ecs.sn1ne</SupportedInstanceTypeFamily>
            </SupportedInstanceTypeFamilies>
            <MemorySize>112.0</MemorySize>
            <Cores>32</Cores>
            <TotalVcpus>56</TotalVcpus>
            <LocalStorageCategory></LocalStorageCategory>
        </DedicatedHostType>
        <DedicatedHostType>
            <LocalStorageAmount>0</LocalStorageAmount>
            <Sockets>2</Sockets>
            <DedicatedHostType>ddh.sn2ne</DedicatedHostType>
            <LocalStorageCapacity>0</LocalStorageCapacity>
            <SupportedInstanceTypeFamilies>
                <SupportedInstanceTypeFamily>ecs.sn2ne</SupportedInstanceTypeFamily>
            </SupportedInstanceTypeFamilies>
            <MemorySize>224.0</MemorySize>
            <Cores>32</Cores>
            <TotalVcpus>56</TotalVcpus>
            <LocalStorageCategory></LocalStorageCategory>
        </DedicatedHostType>
    </DedicatedHostTypes>
    <RequestId>5FE5FF06-3A33-4658-8495-6445FC54E327</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
    "DedicatedHostTypes":{
        "DedicatedHostType":[
            {
                "LocalStorageAmount":0,
                "Sockets":2,
                "DedicatedHostType":"ddh.sn1ne",
                "LocalStorageCapacity":0,
                "SupportedInstanceTypeFamilies":{
                    "SupportedInstanceTypeFamily":[
                        "ecs.sn1ne"
```

]

```json
                },
                "MemorySize":112,
                "Cores":32,
                "TotalVcpus":56,
                "LocalStorageCategory":""
            },
            {
                "LocalStorageAmount":0,
                "Sockets":2,
                "DedicatedHostType":"dh.c60m83.n1",
                "LocalStorageCapacity":0,
                "SupportedInstanceTypeFamilies":{
                    "SupportedInstanceTypeFamily":[
                        "ecs.n1"
```

]

```json
                },
                "MemorySize":84,
                "Cores":32,
                "TotalVcpus":40,
                "LocalStorageCategory":""
            }
```

]

```json
    },
    "RequestId":"9A0FE8A2-720C-45AE-B2D9-813060FCBBF5"
}
```

##### DescribeDedicatedHosts

调用DescribeDedicatedHosts查询一台或多台专有宿主机的详细信息，包括专有宿主机的物理性能指标、机器码、使用状态和已创建的ECS实例列表等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeDedicate dHosts | 系统规定参数，取值： DescribeDedicatedHosts。 |

云服务器ECS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 专有宿主机所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
|---|---|---|---|---|
| ZoneId | String | 否 | cn-qingdao- env17- amtest11001-a | 可用区ID。 |
| DedicatedHostI ds | String | 否 | ["dh- bp165p6xk2tlw6 1e****", "dh- bp165p6xk2tlw6 1e****", … "dh- bp165p6xk2tlw6 1e****"] | 专有宿主机ID列表。单次最多支持100个ID ，ID之间用半角逗号（,）隔开。 |
| DedicatedHost Name | String | 否 | test- DedicatedHostNa me | 专有宿主机的名称。 |
| Status | String | 否 | Available | 专有宿主机的使用状态。取值范围： Available（默认）：可用状态。 Under-Assessment：故障潜伏期，专有宿主机可能会出故障。 Permanent-Failure：永久性故障，专有宿主机不可用。 |
| DedicatedHostT ype | String | 否 | ddh.g5 | 专有宿主机的规格类型。 |
| PageNumber | Integer | 否 | 1 | 响应信息的页码数。 默认值：1 |
| PageSize | Integer | 否 | 10 | 响应信息的每页行数。最大值：100。 默认值：10 |
| Tag.N.Key | String | 否 | TestKey | 专有宿主机的标签键。N的取值范围： 1~20。一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以aliyun和 acs:开头，不能包含http://或 https://。 |
| Tag.N.Value | String | 否 | TestValue | 专有宿主机的标签值。N的取值范围： 1~20。一旦传入该值，可以为空字符串。最多支持128个字符，不能以aliyun和acs:开头，不能包含http://或者https://。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DedicatedHosts | Array |  | 专有宿主机的详细信息集合。 |

云服务器ECS

| DedicatedHost |  |  |  |
|---|---|---|---|
| ActionOnMainte nance | String | Migrate | 当专有宿主机发生故障或者在线修复时，为其所宿实例设置迁移方案。取值范围： Migrate：迁移实例到其他物理机并重新启动实例。 默认值：Migrate（当专有宿主机上挂载云盘存储时） Stop：在当前专有宿主机上停止实例，确认无法修复专有宿主机后，迁移实例到其他物理机并重新启动实例。 默认值：Stop（当专有宿主机上挂载本地盘存储时） |
| AutoPlacement | String | on | 专有宿主机是否加入自动部署资源池。取值范围： on：加入自动部署资源池。 off：不加入自动部署资源池。 |
| AutoReleaseTi me | String | 2017-01- 01T12:00:00Z | 自动释放时间。按照ISO8601标准表示，并需要使用UTC+0时间，格式为 yyyy-MM- ddTHH:mmZ 。 |
| Capacity | Struct |  | 专有宿主机性能指标集合。 |
| AvailableLocalS torage | Integer | 65 | 剩余的本地盘容量。单位：GiB。 |
| AvailableMemo ry | Float | 25 | 剩余的内存容量，单位：GiB。 |
| AvailableVcpus | Integer | 5 | 剩余的vCPU核数。 |
| AvailableVgpus | Integer | 2 | 可用虚拟GPU数量。 |
| LocalStorageCa tegory | String | i2 | 本地盘类型。 |
| TotalLocalStora ge | Integer | 512 | 本地盘总容量，单位：GiB。 |
| TotalMemory | Float | 1024 | 内存总容量，单位：GiB。 |
| TotalVcpus | Integer | 56 | vCPU总核数。 |
| TotalVgpus | Integer | 10 | 总虚拟GPU数量。 |
| ChargeType | String | test | 说明该参数暂未支持。 |

| Z | ddTHH:mmZ |
|---|---|

云服务器ECS

| Cores | Integer | 3 | 单个CPU的核数。 |
|---|---|---|---|
| CreationTime | String | 2018-01- 01T12:00:00Z | 专有宿主机的创建时间。按照ISO8601标准表示， 并需要使用UTC+0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |
| DedicatedHostI d | String | dh- bp165p6xk2tlw61e* *** | 专有宿主机ID。 |
| DedicatedHost Name | String | myDDH | 专有宿主机的名称。 |
| DedicatedHost Type | String | ddh.g5 | 专有宿主机的规格类型。 |
| Description | String | This is a description example. | 专有宿主机的描述信息。 |
| ExpiredTime | String | test | 说明该参数暂未支持。 |
| GPUSpec | String | gpu | GPU型号。 |
| Instances | Array |  | 专有宿主机上创建的ECS实例。 |
| Instance |  |  |  |
| InstanceId | String | i- bp1a0cmfrfi71qlh3f k3 | 专有宿主机上创建的ECS实例ID。 |
| InstanceType | String | ecs.g5 | 专有宿主机上创建的ECS实例类型。 |
| MachineId | String | 2099-09-08T16:00Z | 专有宿主机机器码。 |
| NetworkAttribut es | Struct |  | 专有宿主机的网络属性值。 |
| SlbUdpTimeout | Integer | 60 | SLB UDP超时时间。 |
| UdpTimeout | Integer | 60 | UDP超时时间。 |
| OperationLocks | Array |  | 专有宿主机资源被锁定原因。 |
| OperationLock |  |  |  |
| LockReason | String | financial | 资源锁定原因。 |

云服务器ECS

| PhysicalGpus | Integer | 10 | 物理GPU数量。 |
|---|---|---|---|
| RegionId | String | cn-qingdao-env17- d01 | 专有宿主机所在地域ID。 |
| ResourceGroup Id | String | rg-**** | 专有宿主机所在资源组ID。 |
| SaleCycle | String | test | 说明该参数暂未支持。 |
| Sockets | Integer | 5 | 物理处理器（CPU）数量。 |
| Status | String | Available | 专有宿主机的使用状态。取值范围：Available \| Under-Assessment \| Permanent-Failure |
| SupportedCust omInstanceTyp eFamilies | List | ecs.ddh6s.custom | 专有宿主机支持的自定义实例规格族。 |
| SupportedInsta nceTypeFamilie s | List | ecs.g5 | 专有宿主机支持的ECS实例规格族。 |
| SupportedInsta nceTypesList | List | ecs.g5 | 专有宿主机支持的ECS实例规格族。 |
| Tags | Array |  | 专有宿主机的标签。 |
| Tag |  |  |  |
| TagKey | String | TestKey | 专有宿主机的标签键。 |
| TagValue | String | TestValue | 专有宿主机的标签值。 |
| ZoneId | String | cn-qingdao-env17- amtest11001-a | 可用区ID。 |
| PageNumber | Integer | 5 | 专有宿主机列表的页码。 |
| PageSize | Integer | 1 | 输入时设置的每页行数。 |
| RequestId | String | C9E9EA51-6B74- 409E-BA40- 107126A200D4 | 请求ID。 |
| TotalCount | Integer | 3 | 专有宿主机总数。 |

**示例**

请求示例云服务器ECS

```
https://ecs.example.com/?Action=DescribeDedicatedHosts &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <PageNumber>1</PageNumber>
      <DedicatedHosts>
            <DedicatedHost>
                  <DedicatedHostId>dh-bp165p6xk2tlw61e****</DedicatedHostId>
                  <Description></Description>
                  <ResourceGroupId></ResourceGroupId>
                  <SupportInstanceTypeFamilies>
                        <SupportInstanceTypeFamily>ecs.se1ne</SupportInstanceTypeFamily>
                  </SupportInstanceTypeFamilies>
                  <Instances>
            </Instances>
                  <Cores>32</Cores>
                  <ZoneId>cn-qingdao-env17-amtest11001-a</ZoneId>
                  <CreationTime>2018-08-13T07:59Z</CreationTime>
                  <Sockets>2</Sockets>
                  <Status>Available</Status>
                  <DedicatedHostType>ddh.se1ne</DedicatedHostType>
                  <RegionId>cn-qingdao-env17-d01</RegionId>
                  <DedicatedHostName>test-DedicatedHostName</DedicatedHostName>
                  <Capacity>
                        <AvailableVcpus>56</AvailableVcpus>
                        <TotalMemory>448</TotalMemory>
                        <TotalVcpus>56</TotalVcpus>
                        <AvailableLocalStorage>0</AvailableLocalStorage>
                        <TotalLocalStorage>0</TotalLocalStorage>
                        <LocalStorageCategory></LocalStorageCategory>
                        <AvailableMemory>448</AvailableMemory>
                  </Capacity>
                  <OperationLocks>
            </OperationLocks>
                  <MachineId> 73aa79494f26e****</MachineId>
            </DedicatedHost>
      </DedicatedHosts>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>9D5CC4F5-921A-4E02-B971-0DAF703407BE</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
    "PageNumber": 1,
    "DedicatedHosts": {
        "DedicatedHost": [
            {
                "DedicatedHostId": "dh-bp165p6xk2tlw61e****",
                "Description": "",
                "ResourceGroupId": "",
                "SupportInstanceTypeFamilies": {
                    "SupportInstanceTypeFamily": [
                        "ecs.se1ne"
```

]

```json
                },
                "Instances": {
                    "Instance": []
                },
                "Cores": 32,
                "ZoneId": "cn-qingdao-env17-amtest11001-a",
                "CreationTime": "2018-08-13T07:59Z",
                "Sockets": 2,
                "Status": "Available",
                "DedicatedHostType": "ddh.se1ne",
                "RegionId": "cn-qingdao-env17-d01",
                "DedicatedHostName": "test-DedicatedHostName",
                "AutoReleaseTime": "",
                "Capacity": {
                    "AvailableVcpus": 56,
                    "TotalMemory": 448,
                    "TotalVcpus": 56,
                    "AvailableLocalStorage": 0,
                    "TotalLocalStorage": 0,
                    "LocalStorageCategory": "",
                    "AvailableMemory": 448
                },
                "OperationLocks": {
                    "OperationLock": []
                },
                "MachineId": " 73aa79494f26e****",
            }
```

]

```json
    },
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "9D5CC4F5-921A-4E02-B971-0DAF703407BE"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidStatus.ValueN otSupported | The pecified dedicated host status is not supported. | 当前宿主机状态不支持此操作。 |
| 400 | MissingParamter.Re gionId | The regionId should not be null. | 参数 RegionId 不得为空。 |

云服务器ECS

| 403 | InvalidDedicatedHos tIds.Malformed | The amount of specified dedicatedHostIds exceeds the limit. | 参数“DedicatedHostIds”中的数据最多设置 100 个。 |
|---|---|---|---|
| 400 | InvalidParameter.De dicatedHostIds | The specified parameter dedicatedHostIds is not valid. | 指定的参数“DedicatedHostIds”无效。 |
| 400 | InvalidRegion.NotFo und | The specified parameter RegionId is not valid. | RegionId参数不合法 |
| 400 | InvalidZone.NotFoun d | The specified parameter ZoneId is not valid. | 指定的 ZoneId 不合法。 |
| 404 | InvalidLockReason.N otFound | The specified LockReason is not found | 指定的锁定类型不存在。 |

##### ReleaseDedicatedHost

**接口说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | ReleaseDedicate dHost | 系统规定参数。取值： ReleaseDedicatedHost |
| DedicatedHostI d | String | 是 | dh- xxxxxxxxxxxxxxx xx | 专有宿主机ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 专有宿主机所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A1B15AC8-E6F6- 49A4-8985- 8C07104B9199 | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=ReleaseDedicatedHost &DedicatedHostId=dh-xxxxxxxxxxxxxxxxx &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例云服务器ECS `XML` 格式

```xml
    <RequestId>A1B15AC8-E6F6-49A4-8985-8C07104B9199</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"A1B15AC8-E6F6-49A4-8985-8C07104B9199"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InstanceExist | Instance exists on the dedicated host. | 释放宿主机前，请先移除宿主机上的所有实例。 |
| 400 | ChargeTypeViolatio n | The operation is not permitted due to charge type of the dedicated host. | 专有宿主机的付费方式不支持该操作，请您检查专有宿主机的付费类型是否与该操作冲突。 |
| 400 | IncorrectHostStatus. Initializing | The specified dedicatedHost status is not support this operation | 当前宿主机状态不支持当前操作。 |
| 404 | InvalidDedicatedHos tId.NotFound | The specified DedicatedHostId does not exist. | 指定的专有宿主机不存在。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### CreateDedicatedHostCluster

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | CreateDedicated HostCluster | 系统规定参数。取值： CreateDedicatedHostCluster |
| RegionId | String | 是 | cn-qingdao- env8e-d01 | 专有宿主机集群所在的地域ID。您可以调用 DescribeRegions查看最新的地域列表。 |

云服务器ECS

| DryRun | Boolean | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会查询资源状况。检查项包括AccessKey是否有效、 RAM用户的授权情况和是否填写了必需参数。如果检查不通过，则返回对应错误。 如果检查通过，会返回错误码 DryRunOperation 。 false：发送正常请求，通过检查后返回 2XX HTTP状态码并直接查询资源状况。 默认值：false |
|---|---|---|---|---|
| Tag.N.Key | String | 否 | TestKey | 专有宿主机集群的标签键。N的取值范围： 1~20。一旦传入该值，则不允许为空字符串。最多支持64个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 或 https:// 。 |
| Tag.N.Value | String | 否 | TestValue | 专有宿主机集群的标签值。N的取值范围： 1~20。一旦传入该值，则不允许为空字符串。最多支持64个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 或 https:// 。 |
| ResourceGroupId | String | 否 | rg- bp67acfmxazb4p **** | 专有宿主机集群要加入的资源组ID。 |
| ZoneId | String | 否 | cn-qingdao- env8e-nu20001-a | 专有宿主机集群所在的可用区ID。您可以调用DescribeZones查看可用区。 |
| DedicatedHostClu sterName | String | 否 | myDDHCluster | 专有宿主机集群的名称。长度为2~128个英文或中文字符，必须以大小字母或中文开头，可包含数字、英文句号（.）、下划线 （ ）或短划线（-）。不能包 _ 含 http:// 和 https:// 。 默认值：空 |
| Description | String | 否 | This-is-my- DDHCluster | 专有宿主机集群的描述。长度为2~256个字符。不能以 http:// 和 https:// 开头。 默认值：空 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DedicatedHost ClusterId | String | dc- bp12wlf6bw0vz9v2* *** | 专有宿主机集群ID。 |
| RequestId | String | E2A664A6-2933- 4C64-88AE- 5033D003EADF | 请求ID。 |

云服务器ECS

**示例**

请求示例

```
https://ecs.example.com/?Action=CreateDedicatedHostCluster &RegionId=cn-qingdao-env8e-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <RequestId>214A2187-B06F-4E49-A081-4D053466A8C7</RequestId>
        <DedicatedHostClusterId>dc-bp12wlf6bw0vz9v2****</DedicatedHostClusterId>
```

`JSON` 格式

```json
{
 "RequestId": "214A2187-B06F-4E49-A081-4D053466A8C7",
 "DedicatedHostClusterId": "dc-bp12wlf6bw0vz9v2****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidResourceGro up.NotFound | The ResourceGroup provided does not exist in our records. | 资源组并不在记录中。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |

##### DescribeDedicatedHostClusters

调用DescribeDedicatedHostClusters查询一个或多个专有宿主机集群的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeDedicate dHostClusters | 系统规定参数。取值： DescribeDedicatedHostClusters |
| RegionId | String | 是 | cn-qingdao- env8e-d01 | 专有宿主机集群所在的地域ID。您可以调用 DescribeRegions查看最新的地域列表。 |

云服务器ECS

| Tag.N.Key | String | 否 |  | TestKey | 专有宿主机集群的标签键。N的取值范围： 1~20。一旦传入该值，则不允许为空字符串。最多支持64个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 使用一个标签过滤资源，查询到该标签下的资源数量不能超过1000个；使用多个标签过滤资源，查询到同时绑定了多个标签的资源数量不能超过1000个。如果资源数量超过 1000个，请使用ListTagResources接口进行查询。 |  |
|---|---|---|---|---|---|---|
| Tag.N.Value | String | 否 |  | TestValue | 专有宿主机集群的标签值。N的取值范围： 1~20。一旦传入该值，则不允许为空字符串。最多支持64个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |  |
| ResourceGroupId | String | 否 |  | rg- bp67acfmxazb4p **** | 专有宿主机集群要加入的资源组ID。使用该参数过滤资源时，资源数量不能超过1000 个。 |  |
| ZoneId | String | 否 |  | cn-qingdao- env8e-nu20001-a | 专有宿主机集群所在的可用区ID。您可以调用DescribeZones查看可用区。 |  |
| DedicatedHostClu sterIds | String | 否 |  | ["dc- bp12wlf6am0vz9 v2****", "dc- | 专有宿主机集群ID列表。取值可以由多个专有宿主机集群ID组成一个JSON数组，格式为 ["dc-xxxxxxxxx", "dc- yyyyyyyyy", … "dc-zzzzzzzzz"] 。 支持最多100个ID，用半角逗号字符隔开。 |  |
|  |  |  |  |  |  | ["dc-xxxxxxxxx", "dc- |
|  |  |  |  | bp12wlf6am0vz9 | yyyyyyyyy", … "dc-zzzzzzzzz"] |  |
|  |  |  |  | v3****"] |  |  |
| DedicatedHostClu sterName | String | 否 |  | myDDHCluster | 专有宿主机集群名称。 |  |
| PageNumber | Integer | 否 |  | 1 | 专有宿主机集群状态列表的页码。 起始值：1 默认值：1 |  |
| PageSize | Integer | 否 |  | 5 | 分页查询时设置的每页行数。 最大值：100 默认值：10 |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DedicatedHost Clusters | Array of DedicatedHost Cluster |  | 由一个或多个专有宿主机集群状态组成的数组。 |

云服务器ECS

| DedicatedHost Cluster |  |  |  |
|---|---|---|---|
| DedicatedHost ClusterCapacity | Struct |  | 专有宿主机集群容量。 |
| AvailableMemo ry | Integer | 4 | 当前可用内存大小。单位：GiB |
| AvailableVcpus | Integer | 2 | 当前可用vCPU数。 |
| LocalStorageCa pacities | Array of LocalStorageCa pacity |  | 本地存储容量。 |
| LocalStorageCa pacity |  |  |  |
| AvailableDisk | Integer | 20 | 当前可用本地盘大小。单位：GiB |
| DataDiskCateg ory | String | cloud | 数据盘类型。可能值： cloud：普通云盘 cloud efficiency：高效云盘 _ cloud ssd：SSD云盘 _ |
| TotalDisk | Integer | 40 | 本地盘总大小。单位：GiB |
| TotalMemory | Integer | 8 | 总内存大小。单位：GiB |
| TotalVcpus | Integer | 4 | 总vCPU数。 |
| DedicatedHost ClusterId | String | dc- bp12wlf6am0vz9v2* *** | 专有宿主机集群ID。 |
| DedicatedHost ClusterName | String | myDDHCluster | 专有宿主机集群名称。 |
| DedicatedHostI ds | List | ["dh- bp181e5064b5sotr* ***","dh- bp18064b5sotrr9c** **"] | 由DedicatedHostId组成的集合，返回专有宿主机集群下的专有宿主机ID列表。 |
| Description | String | This-is-my- DDHCluster | 专有宿主机集群描述。 |
| RegionId | String | cn-qingdao-env8e- d01 | 专有宿主机集群所在的地域ID。 |
| ResourceGroup Id | String | rg- bp67acfmxazb4p*** * | 专有宿主机集群的资源组ID。 |

云服务器ECS

| Tags | Array of Tag |  | 专有宿主机集群的标签。 |
|---|---|---|---|
| Tag |  |  |  |
| TagKey | String | TestKey | 专有宿主机集群的标签键。 |
| TagValue | String | TestValue | 专有宿主机集群的标签值。 |
| ZoneId | String | cn-qingdao-env8e- nu20001-a | 专有宿主机集群所在的可用区ID。 |
| PageNumber | Integer | 1 | 专有宿主机集群状态列表的页码。 |
| PageSize | Integer | 5 | 输入时设置的每页行数。 |
| RequestId | String | 214A2187-B06F- 4E49-A081- 4D053466A8C7 | 请求ID。 |
| TotalCount | Integer | 2 | 专有宿主机总个数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeDedicatedHostClusters &RegionId=cn-qingdao-env8e-d01 &ZoneId=cn-qingdao-env8e-nu20001-a &DedicatedHostClusterName=myDDHCluster &PageNumber=1 &PageSize=5
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
        <DedicatedHostClusters>
                <DedicatedHostCluster>
                        <Description>This-is-my-DDHCluster</Description>
                        <ZoneId>cn-qingdao-env8e-nu20001-a</ZoneId>
                        <DedicatedHostClusterName>myDDHCluster</DedicatedHostClusterName>
                        <ResourceGroupId>rg-bp67acfmxazb4p****</ResourceGroupId>
                        <DedicatedHostClusterCapacity>
                                <TotalMemory>0</TotalMemory>
                                <AvailableMemory>0</AvailableMemory>
                                <AvailableVcpus>0</AvailableVcpus>
                                <TotalVcpus>0</TotalVcpus>
                                <LocalStorageCapacities>
                </LocalStorageCapacities>
                        </DedicatedHostClusterCapacity>
                        <RegionId>cn-qingdao-env8e-d01</RegionId>
                        <DedicatedHostIds>
            </DedicatedHostIds>
                        <DedicatedHostClusterId>dc-bp1i7d8p4ku9jgob****
</DedicatedHostClusterId>
                </DedicatedHostCluster>
        </DedicatedHostClusters>
        <TotalCount>1</TotalCount>
        <RequestId>502C9C44-B851-44F4-8805-3EC15E726745</RequestId>
        <PageSize>10</PageSize>
        <PageNumber>1</PageNumber>
```

`JSON` 格式云服务器ECS

```json
{
 "DedicatedHostClusters": {
  "DedicatedHostCluster": [
   {
    "Description": "This-is-my-DDHCluster",
    "ZoneId": "cn-qingdao-env8e-nu20001-a",
    "DedicatedHostClusterName": "myDDHCluster",
    "ResourceGroupId": "rg-bp67acfmxazb4p****",
    "DedicatedHostClusterCapacity": {
     "TotalMemory": 0,
     "AvailableMemory": 0,
     "AvailableVcpus": 0,
     "TotalVcpus": 0,
     "LocalStorageCapacities": {
      "LocalStorageCapacity": []
     }
    },
    "RegionId": "cn-qingdao-env8e-d01",
    "DedicatedHostIds": {
     "DedicatedHostId": []
    },
    "DedicatedHostClusterId": "dc-bp1i7d8p4ku9jgob****"
   }
```

]

```json
 },
 "TotalCount": 1,
 "RequestId": "502C9C44-B851-44F4-8805-3EC15E726745",
 "PageSize": 10,
 "PageNumber": 1
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParamter.Re gionId | The regionId should not be null. | 参数RegionId不得为空。 |
| 400 | InvalidRegion.NotFo und | The specified parameter RegionId is not valid. | RegionId参数不合法。 |
| 400 | InvalidZone.NotFoun d | The specified parameter ZoneId is not valid. | 指定的ZoneId不合法。 |

##### ModifyDedicatedHostClusterAttribute

调用ModifyDedicatedHostClusterAttribute修改一台专有宿主机集群的部分信息，包括专有宿主机集群的名称、描述信息、属性等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | ModifyDedicated HostClusterAttrib ute | 系统规定参数。取值： ModifyDedicatedHostClusterAttribute |

云服务器ECS

| DedicatedHostClu sterId | String | 是 | dc- bp12wlf6am0vz9 v2**** | 专有宿主机集群ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao- env8e-d01 | 专有宿主机集群所在的地域ID。您可以调用 DescribeRegions查看最新的地域列表。 |
| DedicatedHostClu sterName | String | 否 | newClusterName | 专有宿主机集群的名称。长度为2~128个英文或中文字符，必须以大小字母或中文开头，可包含数字、英文句号（.）、下划线 （ ）或短划线（-）。不能包 _ 含 http:// 和 https:// 。 |
| Description | String | 否 | newClusterDescri ption | 专有宿主机集群的描述。长度为2~256个字符。不能以 http:// 和 https:// 开头。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 11B55F58-D3A4- 4A9B-9596- 342420D02FF8 | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyDedicatedHostClusterAttribute &RegionId=cn-qingdao-env8e-d01 &DedicatedHostClusterId=dc-bp12wlf6am0vz9v2**** &DedicatedHostClusterName=newClusterName
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDedicatedHostClusterAttributeResponse>
        <RequestId>11B55F58-D3A4-4A9B-9596-342420D02FF8</RequestId>
</ModifyDedicatedHostClusterAttributeResponse>
```

`JSON` 格式

```json
{
 "RequestId": "11B55F58-D3A4-4A9B-9596-342420D02FF8"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云服务器ECS

| 400 | InvalidDescription.M alformed | The specified parameter Description is not valid. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
|---|---|---|---|
| 403 | InvalidUser.Unautho rized | The user is not authorized | 您当前使用的账号无权限。 |

##### DeleteDedicatedHostCluster

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DeleteDedicated HostCluster | 系统规定参数。取值： DeleteDedicatedHostCluster |
| DedicatedHostClu sterId | String | 是 | dc- bp12wlf6am0vz9 v2**** | 专有宿主机集群ID。 |
| RegionId | String | 是 | cn-qingdao- env8e-d01 | 专有宿主机集群所在的地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 11B55F58-D3A4- 4A9B-9596- 342420D02FF8 | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DeleteDedicatedHostCluster &DedicatedHostClusterId=dc-bp12wlf6am0vz9v2**** &RegionId=cn-qingdao-env8e-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <RequestId>11B55F58-D3A4-4A9B-9596-342420D02FF8</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "11B55F58-D3A4-4A9B-9596-342420D02FF8"
}
```

云服务器ECS

#### 部署集

##### CreateDeploymentSet

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | CreateDeployme ntSet | 系统规定参数，取值： CreateDeploymentSet。 |
| RegionId | String | 是 | cn-qingdao-**** | 部署集所属地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| OnUnableToRed eployFailedInst ance | String | 否 | CancelMembershi pAndStart | 部署集内实例宕机迁移后，缺乏可供打散的实例库存的紧急处理方案。取值范围： CancelMembershipAndStart（默认）：将实例移出部署集，宕机迁移后即刻启动实例。 KeepStopped：保持异常状态等待补货充足后再启动实例。 |
| Description | String | 否 | This is a description example. | 部署集描述信息。长度为2~256个英文或中文字符，不能以http://和https://开头。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见《云服务器ECS开发指南》中的如何保证幂等性章节。 |
| DeploymentSet Name | String | 否 | FinanceDeploym ent | 部署集名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http://和https://开头。可以包含数字、半角冒号（:）、下划线（ ）或者连字符（-）。 _ |
| Domain | String | 否 | null | 部署域。取值范围： Default Switch 默认值：Default。 |

云服务器ECS

| Granularity | String | 否 | null | 部署粒度。取值范围： Host：宿主机，代表最小调度粒度为一个物理服务器。 Rack：代表最小调度粒度为一个机架。 Switch：代表最小调度粒度为一个网络交换机。 默认值：Host。如果部署域是Switch，部署粒度不能选择Switch。 |
|---|---|---|---|---|
| Strategy | String | 否 | null | 部署策略。取值范围： LooseDispersion：尽量分散。 LooseAggregation：尽量聚合。 StrictAggregation：严格聚合。 StrictDispersion：严格分散。 默认值：LooseDispersion。如果部署粒度为Switch，可以支持4种部署策略。如果部署粒度为Rack或者Host，只可以选择尽量分散或者严格分散。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DeploymentSet Id | String | ds- bp1frxuzdg87zh4pz q*** | 部署集ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=CreateDeploymentSet &RegionId=cn-qingdao-**** &DeploymentSetName=FinanceDeployment
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>04F0F334-1335-436C-A1D7-6C044FE73368</RequestId>
   <DeploymentSetId>ds-bp1frxuzdg87zh4pzq***</DeploymentSetId>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368",
    "DeploymentSetId": "ds-bp1frxuzdg87zh4pzq***"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | The input parameter RegionId that is mandatory for processing this request is not supplied. | 参数RegionId不得为空。 |
| 400 | InvalidDeploymentS etName.Malformed | Specified deployment set name is not valid. | 指定的参数DeploymentSetName 不合法。 |
| 400 | InvalidDescription.M alformed | The specified parameter Description is not valid. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
| 400 | InvalidDeploymentS etId.NotFound | The specified DeploymentSetId does not exist. | 指定的参数DeploymentSetId不存在，请您检查DeploymentSetId是否正确。 |
| 400 | MissingParameter | The input parameter DeploymentSetId that is mandatory for processing this request is not supplied. | 未提供必需的 DeploymentSetId。 |
| 400 | InvalidParameter.Do main | The specified parameter Domain is not valid. | 指定的 Domain 参数不合法。 |
| 400 | InvalidParameter.Str ategy | The specified parameter Strategy is not valid | 指定的 Strategy 不合法。 |
| 400 | InvalidParameter.gr anularity | The specified parameter Granularity is not valid. | 指定的 Granularity 参数不合法。 |
| 400 | DependencyViolatio n.domain.granularit y | The DeploymentSet domain and granularity is violation. | 部署集域与数据粒度冲突。 |
| 400 | DependencyViolatio n.strategy.granularit y | The DeploymentSet strategy and granularity is violation. | 部署集策略与数据粒度冲突。 |
| 400 | DEPLOYMENTSET.Q UOTA FULL _ | The deploymentSet quota is full | 部署集配额已满，请您减少部署集数量。 |

##### ModifyDeploymentSetAttribute

调用ModifyDeploymentSetAttribute修改一个部署集的名称和描述信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDeployme ntSetAttribute | 系统规定参数。取值： ModifyDeploymentSetAttribute |

云服务器ECS

| DeploymentSetId | String | 是 | ds- bp1frxuzdg87zh4 p**** | 部署集ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao- env17-d01 | 部署集所属地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| Description | String | 否 | TestDescription | 新的部署集描述信息。长度为2~256个英文或中文字符，不能以http://和https://开头。 |
| DeploymentSetN ame | String | 否 | DeploymentSetT estName | 新的部署集名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以http://和https://开头。可以包含数字、半角冒号（:）、下划线（ ）或者连字符 _ （-）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyDeploymentSetAttribute &RegionId=cn-qingdao-env17-d01 &DeploymentSetId=ds-bp1frxuzdg87zh4p**** &DeploymentSetName=DeploymentSetTestName
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>04F0F334-1335-436C-A1D7-6C044FE73368</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云服务器ECS

| 400 | MissingParameter | The input parameter RegionId that is mandatory for processing this request is not supplied. | 参数RegionId不得为空。 |
|---|---|---|---|
| 400 | InvalidDeploymentS etName.Malformed | Specified deployment set name is not valid. | 指定的参数DeploymentSetName 不合法。 |
| 400 | InvalidDescription.M alformed | The specified parameter Description is not valid. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
| 400 | InvalidDeploymentS etId.NotFound | The specified DeploymentSetId does not exist. | 指定的参数DeploymentSetId不存在，请您检查DeploymentSetId是否正确。 |
| 403 | QuotaExceed.Deplo ymentSetInstanceQ uotaFull | instance quota in one deployment set exceeded. | 当前部署集内的实例数量已满额。 |

##### DescribeDeploymentSets

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeDeploym entSets | 系统规定参数，取值： DescribeDeploymentSets。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 部署集所属地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| PageNumber | Integer | 否 | 1 | 部署集列表的页码。 起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。 最大值：50。 默认值：10。 |
| DeploymentSet Ids | String | 否 | ["ds- bp67acfmxazb4p h***", "ds- bp67acfmxazb4pi ***", … "ds- bp67acfmxazb4pj ***"] | 部署集ID列表。取值可以由多个部署集ID组成一个JSON数组，最多支持100个ID，ID之间用半角逗号（,）隔开。 |
| DeploymentSet Name | String | 否 | FinanceDeploym en**** | 部署集名称。 |

云服务器ECS

| Strategy | String | 否 | Availability | 部署策略。取值范围： LooseDispersion：尽量分散。 LooseAggregation：尽量聚合。 StrictAggregation：严格聚合。 StrictDispersion：严格分散。 默认值：LooseDispersion。如果部署粒度为Switch，可以支持4种部署策略。如果部署粒度为Rack或者Host，只可以选择尽量分散或者严格分散。 |
|---|---|---|---|---|
| NetworkType | String | 否 | null | 部署集内实例的网络类型。 说明为提高兼容性，请尽量使用其他参数。 |
| Granularity | String | 否 | null | 部署粒度。取值范围： Host：宿主机，代表最小调度粒度为一个物理服务器。 Rack：代表最小调度粒度为一个机架。 Switch：代表最小调度粒度为一个网络交换机。 默认值：Host。 |
| Domain | String | 否 | null | 部署域。取值范围： Default Switch 默认值：Default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DeploymentSet s | Array |  | 由DeploymentSet组成的数组格式，返回部署集详细信息。 |
| DeploymentSet |  |  |  |
| CreationTime | String | 2017-12- 05T22:40:00Z | 部署集的创建时间。 |
| DeploymentSet Description | String | FinanceDeptLooseDi spersion | 部署集的描述信息。 |
| DeploymentSet Id | String | ds- deploymentse**** | 部署集ID。 |
| DeploymentSet Name | String | FinanceDept | 部署集名称。 |
| DeploymentStr ategy | String | Availability | 部署策略。 |

云服务器ECS

| Domain | String | Default | 部署域。 |
|---|---|---|---|
| Granularity | String | Host | 部署粒度。 |
| InstanceAmoun t | Integer | 1 | 部署集内的实例数量。 |
| InstanceIds | List | ["i-instanc****"] | 部署集内的实例ID列表。 |
| Strategy | String | StrictDispersion | 部署策略。 |
| PageNumber | Integer | 1 | 部署集列表的页数。 |
| PageSize | Integer | 10 | 设置的每页行数。 |
| RegionId | String | cn-qingdao-env17- d01 | 部署集所处的地域 ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求 ID。 |
| TotalCount | Integer | 1 | 查询到的部署集总数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeDeploymentSets &RegionId=cn-qingdao-env17-d01 &PageSize=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <DeploymentSets>
            <DeploymentSet>
                  <CreationTime>Tue Jul 23 17:24:33 CST 2019</CreationTime>
                  <Granularity>switch</Granularity>
                  <DeploymentSetDescription>autogen deploymentset, do not
delete</DeploymentSetDescription>
                  <Domain>default</Domain>
                  <InstanceIds>
                        <InstanceId>i-bp67acfmxazb4ph***</InstanceId>
                        <InstanceId>i-bp67acfmxazb4pi***</InstanceId>
                        <InstanceId>i-bp67acfmxazb4pj***</InstanceId>
                  </InstanceIds>
                  <InstanceAmount>0</InstanceAmount>
                  <Strategy>LooseAggregation</Strategy>
                  <DeploymentSetName>FinanceDeploymen****</DeploymentSetName>
                  <DeploymentStrategy>Availability</DeploymentStrategy>
                  <DeploymentSetId>ds-bp120c8htdzx3869****</DeploymentSetId>
            </DeploymentSet>
      </DeploymentSets>
      <PageNumber>1</PageNumber>
      <TotalCount>5</TotalCount>
      <PageSize>1</PageSize>
      <RegionId>cn-qingdao-env17-d01</RegionId>
      <RequestId>FB5EF912-FD87-4CF7-91D9-9204974A63F3</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
 "DeploymentSets": {
  "DeploymentSet": [
   {
    "CreationTime": "2017-12-05T22:40:00Z",
    "Granularity": "Switch",
    "DeploymentSetDescription": "autogen deploymentset, do not delete",
    "Domain": "Default",
    "InstanceIds": {
     "InstanceId": [
                        "i-bp67acfmxazb4ph***",
                        "i-bp67acfmxazb4pi***",
                        "i-bp67acfmxazb4pj***"]
    },
    "InstanceAmount": 0,
    "Strategy": "LooseAggregation",
    "DeploymentSetName": "FinanceDeploymen****",
    "DeploymentStrategy": "Availability",
    "DeploymentSetId": "ds-bp120c8htdzx3869****"
   }
```

]

```json
 },
 "PageNumber": 1,
 "TotalCount": 5,
 "PageSize": 1,
 "RegionId": "cn-qingdao-env17-d01",
 "RequestId": "FB5EF912-FD87-4CF7-91D9-9204974A63F3"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidDeploymentS etIds.TooManyInput | The parameter DeploymentSets size should less than 100. | 指定的 DeploymentSets 数量大于 100。 |

##### DeleteDeploymentSet

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDeployme ntSet | 系统规定参数，取值： DeleteDeploymentSet。 |
| DeploymentSetId | String | 是 | ds- deploymentsetid 1 | 部署集ID。如果部署集中仍有实例存在，则无法删除。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 部署集所属地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DeleteDeploymentSet &RegionId=cn-qingdao-env17-d01 &DeploymentSetId=ds-bp1frxuzdg87zh4pz***
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>04F0F334-1335-436C-A1D7-6C044FE73368</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | The input parameter "DeploymentSetId" that is mandatory for processing this request is not supplied. | 参数DeploymentSetId不得为空。 |
| 403 | DependencyViolatio n.NotEmpty | There are still instance(s) in the specified DeploymentSetId. | 指定的部署集ID内仍有实例。 |
| 403 | DependencyViolatio n.ReferByHPC | The specified deployment set is still referred by an HPC cluster. | 指定的部署集与其它HPC集群有关联。 |

**6.1.6.5.**

##### DescribeDeploymentSetSupportedInstanceTypeFamily

调用DescribeDeploymentSetSupportedInstanceTypeFamily查询支持部署集的实例规格族。

**接口说明**

更多实例规格族的详情，请参见《云服务器ECS实例规格族&实例规格简介》。

**请求参数**

云服务器ECS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDeploym entSetSupportedI nstanceTypeFami ly | 系统规定参数。取值： DescribeDeploymentSetSupportedInsta nceTypeFamily。 |
| RegionId | String | 是 | cn-hangzhou-**** | 部署集所属地域ID。您可以调用 DescribeRegions查询地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceTypeFa milies | String | ecs.s6-k,ecs.sn1 | 支持部署集的实例规格族。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B7DB- A3DC7DE***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribeDeploymentSetSupportedInstanceTypeFamily &RegionId=cn-hangzhou-****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDeploymentSetSupportedInstanceTypeFamilyResponse>
        <RequestId>473469C7-AA6F-4DC5-B7DB-A3DC7DE*****</RequestId>
        <InstanceTypeFamilies>ecs.s6-k,ecs.sn1</InstanceTypeFamilies>
</DescribeDeploymentSetSupportedInstanceTypeFamilyResponse>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B7DB-A3DC7DE*****",
    "InstanceTypeFamilies": "ecs.s6-k,ecs.sn1"
}
```

#### 存储集

##### CreateStorageSet

**接口说明**

存储集可以将云盘或共享块存储分散处理。存储集可以设置分区数量，分区数越大，表示云盘或共享块存储的物理位置越分散。 云服务器ECS 关于存储集的更多信息，请参见云服务定义存储用户指南中的创建存储集章节。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateStorageSet | 系统规定参数。取值： CreateStorageSet。 |
| RegionId | String | 是 | cn-qingdao-****- d01 | 存储集所属地域。您可以调用 DescribeRegions查询支持的地域列表。 |
| ZoneId | String | 是 | cn-qingdao-****- d01-a | 存储集所属可用区。您可以调用 DescribeZones查询支持的可用区列表。 |
| StorageSetName | String | 否 | storageSetTest | 存储集名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 和 https:// 开头。可以包含数字、半角冒号（:）、下划线（ ）或 _ 者短划线（-）。 |
| MaxPartitionNum ber | Integer | 否 | 10 | 存储集最大分区，StorageSet支持的最大分区号。取值范围：大于等于2。 默认值：2。 |
| Description | String | 否 | storageSetTest | 存储集描述信息。长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见云服务器ECS开发指南中的如何保证幂等性章节。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| StorageSetId | String | ss- bp67acfmxazb4ph** * | 存储集ID。 |

**示例**

请求示例云服务器ECS

```
http(s)://ecs.example.com/?Action=CreateStorageSet &RegionId=cn-qingdao-****-d01 &ZoneId=cn-qingdao-****-d01-a &StorageSetName=testStorageSetName &MaxPartitionNumber=10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
  <StorageSetId>ss-bp67acfmxazb4ph***</StorageSetId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "StorageSetId": "ss-bp67acfmxazb4ph***"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidClientToken.V alueNotSupported | clienttoken is not valid. | 指定的ClientToken不合法。 |
| 403 | InvalidUser.NotSupp orted | %s | 您的用户暂时不支持此操作。 |
| 403 | InvalidRegionId.NotF ound | %s | 提供的地域ID不存在。 |
| 403 | InvalidParameter | %s | 无效的参数。 |

##### DescribeStorageSets

调用DescribeStorageSets查询一个或多个存储集信息，包括所属地域、所属可用区、创建时间和最大分区数等信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeStorageS ets | 系统规定参数。取值： DescribeStorageSets。 |
| RegionId | String | 是 | cn-qingdao-****- d01 | 存储集所属地域。您可以调用 DescribeRegions查询支持的地域列表。 |

云服务器ECS

| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过 64个字符。更多详情，请参见云服务定义存储用户指南中的创建存储集章节。 |
|---|---|---|---|---|
| StorageSetIds | String | 否 | ["ss- bp1d6tsvznfghy7 y****", "ss- bp1ippxbaql9zet 7****", … "ss- bp1ib7bcz07l**** "] | 存储集ID列表。取值可以由多个存储集ID组成一个JSON数组，最多支持100个ID，ID之间用半角逗号（,）隔开。 |
| ZoneId | String | 否 | cn-qingdao-****- d01-a | 云盘或共享块存储所属可用区。 |
| StorageSetName | String | 否 | storageSetTest | 存储集名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 和 https:// 开头。可以包含数字、半角冒号（:）、下划线（ ）或 _ 者短划线（-）。 |
| PageNumber | Integer | 否 | 1 | 存储集列表的页码。 起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。 最大值：100。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 存储集列表的页码。 |
| PageSize | Integer | 10 | 单页返回的条目数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| StorageSets | Array of StorageSet |  | 由StorageSet组成的数组格式，返回存储集详细信息。 |
| StorageSet |  |  |  |
| CreationTime | String | 2022-03- 31T00:00:00Z | 存储集创建时间。 |

云服务器ECS

| Description | String | testDescription | 存储集描述信息。 |
|---|---|---|---|
| RegionId | String | cn-qingdao-****-d01 | 存储集所属地域ID。 |
| StorageSetId | String | ss- bp67acfmxazb4ph** ** | 存储集ID。 |
| StorageSetNam e | String | testStorageSetNam e | 存储集名称。 |
| StorageSetParti tionNumber | Integer | 3 | 存储集支持的最大分区数。 |
| ZoneId | String | cn-qingdao-****- d01-a | 云盘或共享块存储所属可用区。 |
| TotalCount | Integer | 20 | 存储集总数。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribeStorageSets &RegionId=cn-qingdao-****-d01 &PageSize=1 &PageNumber=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <TotalCount>20</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
  <PageNumber>1</PageNumber>
  <StorageSets>
        <Description>testDescription</Description>
        <ZoneId>cn-qingdao-****-d01-a</ZoneId>
        <CreationTime>2022-03-31T00:00:00Z</CreationTime>
        <StorageSetPartitionNumber>3</StorageSetPartitionNumber>
        <RegionId>cn-qingdao-****-d01</RegionId>
        <StorageSetId>ss-bp67acfmxazb4ph****</StorageSetId>
        <StorageSetName>testStorageSetName</StorageSetName>
  </StorageSets>
```

`JSON` 格式云服务器ECS

```json
{
    "TotalCount": 20,
    "PageSize": 10,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "PageNumber": 1,
    "StorageSets": {
        "Description": "testDescription",
        "ZoneId": "cn-qingdao-****-d01-a",
        "CreationTime": "2022-03-31T00:00:00Z",
        "StorageSetPartitionNumber": 3,
        "RegionId": "cn-qingdao-****-d01",
        "StorageSetId": "ss-bp67acfmxazb4ph****",
        "StorageSetName": "testStorageSetName"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidClientToken.V alueNotSupported | clienttoken is not valid. | 指定的ClientToken不合法。 |
| 403 | InvalidUser.NotSupp orted | %s | 您的用户暂时不支持此操作。 |
| 403 | InvalidRegionId.NotF ound | %s | 提供的地域ID不存在。 |
| 403 | InvalidParameter | %s | 无效的参数。 |

##### DescribeStorageSetDetails

调用DescribeStorageSetDetails查询一个存储集内云盘或共享块存储的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeStorageS etDetails | 系统规定参数。取值： DescribeStorageSetDetails。 |
| RegionId | String | 是 | cn-qingdao-****- d01 | 存储集所属地域。您可以调用 DescribeRegions查询支持的地域列表。 |
| StorageSetId | String | 是 | ss- bp67acfmxazb4p h**** | 存储集ID。您可以调用 DescribeStorageSets查询存储集ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过 64个字符。更多详情，请参见云服务定义存储用户指南中的创建存储集章节。 |

云服务器ECS

| StorageSetPartiti onNumber | Integer | 否 | 10 | 存储集内的最大分区数。 |
|---|---|---|---|---|
| DiskIds | String | 否 | ["d- bp1d6tsvznfghy7 y****", "d- bp1ippxbaql9zet 7****", … "d- bp1ib7bcz07l**** "] | 云盘或共享块存储ID列表。取值可以由多块云盘或共享块存储ID组成一个JSON数组，最多支持100个ID，ID之间用半角逗号（,）隔开。 |
| PageNumber | Integer | 否 | 1 | 存储集列表的页码。 起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。 最大值：100。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Disks | Array of Disk |  | 由Disk组成的数组格式，返回存储集内云盘或共享块存储的详细信息。 |
| Disk |  |  |  |
| Category | String | cloud ssd _ | 云盘或共享块存储种类。 |
| CreationTime | String | 2022-03- 31T00:00:00Z | 云盘或共享块存储创建时间。 |
| DiskId | String | d- bp67acfmxazb4p*** * | 云盘或共享块存储ID。 |
| DiskName | String | testDiskName | 云盘或共享块存储名称。 |
| RegionId | String | cn-qingdao-****-d01 | 云盘或共享块存储所属地域。 |
| StorageSetId | String | ss- bp67acfmxazb4ph** ** | 存储集ID。 |
| StorageSetParti tionNumber | Integer | 10 | 存储集分区数。 |
| ZoneId | String | cn-qingdao-****- d01-a | 云盘或共享块存储所属可用区。 |
| PageNumber | Integer | 1 | 存储集列表的页数。 |

云服务器ECS

| PageSize | Integer | 1 | 单页返回的条数。 |
|---|---|---|---|
| RequestId | String | 49765E79-0D5D- 4451-B3AE- 580A2083**** | 请求ID。 |
| TotalCount | Integer | 1 | 存储集总数。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribeStorageSetDetails &RegionId=cn-qingdao-****-d01 &StorageSetId=ss-bp67acfmxazb4ph****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <TotalCount>1</TotalCount>
  <PageSize>1</PageSize>
  <RequestId>49765E79-0D5D-4451-B3AE-580A2083****</RequestId>
  <PageNumber>1</PageNumber>
  <Disks>
        <Category>cloud_ssd</Category>
        <ZoneId>cn-qingdao-****-d01-a</ZoneId>
        <CreationTime>2022-03-31T00:00:00Z</CreationTime>
        <StorageSetPartitionNumber>10</StorageSetPartitionNumber>
        <RegionId>cn-qingdao-****-d01</RegionId>
        <StorageSetId>ss-bp67acfmxazb4ph****</StorageSetId>
        <DiskName>testDiskName</DiskName>
        <DiskId>d-bp67acfmxazb4p****</DiskId>
  </Disks>
```

`JSON` 格式云服务器ECS

```json
{
    "TotalCount": 1,
    "PageSize": 1,
    "RequestId": "49765E79-0D5D-4451-B3AE-580A2083****",
    "PageNumber": 1,
    "Disks": {
        "Category": "cloud_ssd",
        "ZoneId": "cn-qingdao-****-d01-a",
        "CreationTime": "2022-03-31T00:00:00Z",
        "StorageSetPartitionNumber": 10,
        "RegionId": "cn-qingdao-****-d01",
        "StorageSetId": "ss-bp67acfmxazb4ph****",
        "DiskName": "testDiskName",
        "DiskId": "d-bp67acfmxazb4p****"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidClientToken.V alueNotSupported | clienttoken is not valid. | 指定的ClientToken不合法。 |
| 403 | InvalidUser.NotSupp orted | %s | 您的用户暂时不支持此操作。 |
| 403 | InvalidRegionId.NotF ound | %s | 提供的地域ID不存在。 |
| 403 | InvalidParameter | %s | 无效的参数。 |

##### ModifyStorageSetAttribute

调用ModifyStorageSetAttribute修改一个存储集的名称或描述信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyStorageSet Attribute | 系统规定参数。取值： ModifyStorageSetAttribute。 |
| RegionId | String | 是 | cn-qingdao-****- d01 | 存储集所属地域。您可以调用 DescribeRegions查询支持的地域列表。 |
| StorageSetId | String | 是 | ss- bp67acfmxazb4p h**** | 存储集ID。您可以调用 DescribeStorageSets查询要修改的存储集 ID。 |
| Description | String | 否 | testStorageSetDe scription | 存储集描述信息。长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。 |

云服务器ECS

| StorageSetName | String | 否 | testStorageSetNa me | 存储集名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 或 https:// 开头。可以包含数字、半角冒号（:）、下划线（ ）或 _ 者短划线（-）。 |
|---|---|---|---|---|
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见云服务器ECS开发指南中的如何保证幂等性章节。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=ModifyStorageSetAttribute &RegionId=cn-qingdao-****-d01 &StorageSetId=ss-bp67acfmxazb4ph**** &StorageSetName=testStorageSetName &Description=testStorageSetDescription
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId>
```

`JSON` 格式

```json
{
  "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidClientToken.V alueNotSupported | clienttoken is not valid. | 指定的ClientToken不合法。 |
| 403 | InvalidUser.NotSupp orted | %s | 您的用户暂时不支持此操作。 |

云服务器ECS

| 403 | InvalidRegionId.NotF ound | %s | 提供的地域ID不存在。 |
|---|---|---|---|
| 403 | InvalidParameter | %s | 无效的参数。 |

##### DeleteStorageSet

调用DeleteStorageSet删除一个空的存储集。待删除的存储集必须为空，不能包含云盘或者共享块存储。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteStorageSet | 系统规定参数。取值： DeleteStorageSet。 |
| RegionId | String | 是 | cn-qingdao-****- d01 | 存储集所属地域。您可以调用 DescribeRegions查询支持的地域列表。 |
| StorageSetId | String | 是 | ss- bp67acfmxazb4p h*** | 存储集ID。您可以调用 DescribeStorageSets查询要删除的存储集 ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见云服务器ECS开发指南中的如何保证幂等性章节。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DeleteStorageSet &RegionId=cn-qingdao-****-d01 &StorageSetId=ss-bp67acfmxazb4ph***
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId>
```

云服务器ECS `JSON` 格式

```json
{
  "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidClientToken.V alueNotSupported | clienttoken is not valid. | 指定的ClientToken不合法。 |
| 403 | InvalidUser.NotSupp orted | %s | 您的用户暂时不支持此操作。 |
| 403 | InvalidRegionId.NotF ound | %s | 提供的地域ID不存在。 |
| 403 | InvalidParameter | %s | 无效的参数。 |

#### 云盘

##### CreateDisk

接口说明创建云盘时，默认在删除云盘时删除其自动快照，即 `DeleteAutoSnapshot` 取值为 `true` ，可以通

| ModifyDiskAttribute |  | 修 |
|---|---|---|
| 须指定一项请求参数 Size SnapshotId 使用快照创建 | Size |  |
| SnapshotId |  |  |

创建云盘时支持开启多重挂载特性（ `MultiAttach` ）。建议您先了解该特性及使用限制，更多信息，请参见专有云文档中心《云服务器ECS用户指南》文档中的**云盘** > **支持****NVMe****协议和多重挂载功能** 章节。 支持创建高性能云盘、普通性能云盘、高效云盘和SSD盘。 默认不支持创建共享SSD盘和共享高效云盘。如需创建，请提交工单。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | CreateDisk | 系统规定参数。取值： CreateDisk。 |
| RegionId | String | Query | 是 | cn-qingdao-env***-d** | 所属的地域ID。您可以调用 DescribeRegions 查看地域列表。 |
| ZoneId | String | Query | 否 | cn-qingdao-env***- test001-a | 可用区ID。 |

| 云服务器ECS |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| SnapshotId | String | Query | 否 | s-bp67acfmxazb4p**** | 创建云盘使用的快照。 SnapshotId 参数和 Size 参数存在以下限制： 如果 SnapshotId 参数对应的快照容量大于设置的 Size 参数值，实际创建的云盘大小为指定快照的大小。 如果 SnapshotId 参数对应的快照容量小于设置的 Size 参数值，实际创建的云盘大小为指定的 Size 参数值。 |
| DiskName | String | Query | 否 | test-DiskName | 云盘名称。长度为2~128个字符，支持Unicode中letter 分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号（:）、下划线 （ ）、半角句号（.）或者短 _ 划线（-）。 |

|  | SnapshotId |
|---|---|
| Size |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Size | Intege r | Query | 否 | 2000 | 容量大小，以GiB为单位。指定该参数后，其取值必须≥指定快照ID的容量大小。取值范围： cloud efficiency： _ 20~32768。 san efficiency： _ 20~32768。 cloud ssd： _ 20~32768。 san ssd：20~32768。 _ cloud pperf： _ 20~32768。 cloud sperf： _ 20~32768。 如果您指定了 SnapshotId 参数， SnapshotId 参数和 Size 参数存在以下限制： 如果 SnapshotId 参数对应的快照容量大于设置的 Size 参数值，实际创建的云盘大小为指定快照的大小。 如果 SnapshotId 参数对应的快照容量小于设置的 Size 参数值，实际创建的云盘大小为指定的 Size 参数值。 当数据盘的类型选择为高效云盘（cloud efficiency）或者 _ SSD盘（cloud ssd）时，如 _ 果填写的容量超过2 TB，注意按照以下EBS集群的机器数量与推荐的云盘最大建议值 （机器数量：云盘最大值）进行填写。 6台：2 TB 12台：4 TB 15台：5 TB 24台：8 TB 云盘最大建议值的计算公式为：云盘最大大小S = N/3， 其中N为相应EBS集群的机器数量，结果向下取整。例如： 如果EBS集群的机器数量为6 台，则建议创建的云盘容量不超过2 TB。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DiskCateg ory | String | Query | 否 | cloud ssd _ | 数据盘的云盘种类。取值范围： cloud efficiency：高效 _ 云盘。 cloud ssd：SSD云盘。 _ cloud pperf：高性能云 _ 盘。 cloud sperf：普通性能云 _ 盘。 san ssd：共享SSD盘。 _ san efficiency：共享高 _ 效云盘。 默认值：cloud efficiency。 _ 默认不支持创建共享SSD盘和共享高效云盘。如需创建，请提交工单。 |  |  |
| Descriptio n | String | Query | 否 | This is a description example. | 云盘描述。长度为2~256个英文或中文字符，不能以 http:// 或 https:/ / 开头。 默认值：空。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| Encrypted | Boole an | Query | 否 | false | 是否加密云盘。取值范围： true：是。 false：否。 默认值：false。 |  |  |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多信息，请参见专有云文档中心《云服务器ECS开发指南》文档中的如何保证幂等性章节。 |  |  |
| KMSKeyId | String | Query | 否 | 0e478b7a-4262-4802- b8cb-00d3fb40826X | 云盘使用的KMS密钥ID。 |  |  |
| StorageSet Id | String | Query | 否 | ss-bp67acfmxazb4p**** | 存储集ID。您可以调用 DescribeStorageSets 查询存储集ID。 |  |  |
| EncryptAlg orithm | String | Query | 否 | aes-256 | 选择加密算法。取值范围： aes-256：使用AES 256 算法。 sm4-128：使用SM4国密算法。 |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| StorageSet PartitionNu mber | Intege r | Query | 否 | 3 | 存储集对应分区号，在指定了 StorageSetId 时，该参数为必填。 |  |  |
| MultiAttac h | String | Query | 否 | Disabled | 是否开启多重挂载特性。取值范围： Disabled: 不开启。 Enabled : 开启。目前仅高性能云盘支持设置为 Enabled。 默认值：Disabled。 您可以在创建云盘后调用 AttachDisk 进行挂载，但需要注意开启多重挂载功能的云盘只能作为数据盘进行挂载。 |  |  |
| Tag | Repea tList | Query | 否 |  | 云盘的标签信息列表。 |  |  |
| -key | String |  | 否 | null | 云盘的标签键。 为提高代码兼容性，请使用 Tag.N.Key 参数。 |  |  |
| -Key | String |  | 否 | TestKey | 云盘的标签键。参数格式为 Tag.N.Key ，N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 或 https:/ / 。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| -Value | String |  | 否 | TestValue | 云盘的标签值。参数格式为 Tag.N.Value ，N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128个字符，不能包含 http:// 或 https:/ / 。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| -value | String |  | 否 | null | 云盘的标签值。 为提高代码兼容性，请使用 Tag.N.Value 参数。 |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

**返回数据**

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DiskId | String | d- bp131n0q38u3a4zi1 **** | 云盘ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env***-d** &ZoneId=cn-qingdao-env***-test001-a &SnapshotId=s-bp67acfmxazb4p**** &DiskName=test-DiskName &Size=2000 &DiskCategory=cloud_ssd &Description=This is a description example. &Encrypted=false &ClientToken=123e4567-e89b-12d3-a456-426655440000 &Tag.1.Key=TestKey &Tag.1.Value=TestValue
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "DiskId": "d-bp131n0q38u3a4zi1****"
}
```

`XML` 格式

```xml
        <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
        <DiskId>d-bp131n0q38u3a4zi1****</DiskId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidSize.ValueNot Supported | The specified parameter Size is not valid. | 指定的 Size 不合法。 |
| 400 | InvalidDiskName.Ma lformed | The specified disk name is wrongly formed. | 磁盘名称格式不正确。长度为2-128 个字符，以英文字母或中文开头，可包含数字，点号（.），下划线（ ） _ 或连字符（-）。 不能以http://和 https://开头。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDescription.M alformed | The specified description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256 个字符，不能以 http:// 和 https:// 开头。 |
| 400 | InvalidDiskCategory. NotSupported | The specified disk category is not support. | 不支持的磁盘种类。 |
| 400 | Account.Arrearage | Your account has an outstanding payment. | 您的账号存在未支付的款项。 |
| 400 | InvalidDataDiskCate gory.ValueNotSuppo rted | %s | 指定的数据磁盘类型无效。%s为变量，将根据调用API的实际情况动态返回错误信息。 |
| 400 | InvalidParameter.Co nflict | %s | 您输入的参数无效，请检查参数之间是否冲突。%s为变量，将根据调用 API的实际情况动态返回错误信息。 |
| 400 | RegionUnauthorized | %s | 该地域未被授权。%s为变量，将根据调用API的实际情况动态返回错误信息。 |
| 400 | Zone.NotOnSale | %s | 该可用区暂时关闭了售卖。%s为变量，将根据调用API的实际情况动态返回错误信息。 |
| 400 | InvalidDataDiskSize. ValueNotSupported | %s | 指定的数据盘容量无效。%s为变量， 将根据调用API的实际情况动态返回错误信息。 |
| 400 | OperationDenied | The specified Zone is not available or not authorized. | 指定的可用区不可用或未授权。 |
| 400 | InvalidDiskSize.NotS upported | The specified parameter size is not valid. | 指定的磁盘容量无效。 |
| 400 | InvalidDiskSizeOrCa tegory | The specified disk category or size is invalid. | 指定的磁盘类别或大小无效。 |
| 400 | InvalidParameter.En cryptedIllegal | %s | 您输入的参数无效，请确认您的加密是否合法。%s为变量，将根据调用 API 的实际情况动态返回错误信息。 |
| 400 | InvalidParameter.En cryptedNotSupporte d | %s | 您输入的参数无效，暂时不支持您的加密操作。%s为变量，将根据调用 API的实际情况动态返回错误信息。 |
| 400 | EncryptedOption.Co nflict | %s | 参数不支持（加密盘）。%s为变量， 将根据调用API的实际情况动态返回错误信息。 |
| 400 | InvalidParameter.En cryptedIllegal | The specified parameter Encrypted must be true when kmsKeyId is not empty. | 设置参数 KMSKeyId 后，您必须开启加密属性。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 400 | InvalidPerformanceL evel.Malformed | The specified parameter PerformanceLevel is not valid. | 指定的参数 PerformanceLevel 无效。 |
| 400 | InvalidInstance.NotF oundSystemDisk | The specified instance has no system disk. | 指定的实例没有挂载系统盘。请确保指定的实例已挂载了系统盘。您可以调用 DescribeInstances 查询指定实例的信息。 |
| 403 | InvalidDataDiskCate gory.NotSupported | Specified disk category is not supported. | 不支持指定的磁盘种类。 |
| 403 | InstanceDiskCategor yLimitExceed | The total size of specified disk category in an instance exceeds. | 磁盘种类总容量超过实例限制。 |
| 403 | InvalidSnapshot.Not Ready | The specified snapshot creation is not completed yet. | 指定快照未创建。 |
| 403 | InvalidSnapshot.Too Old | This operation is forbidden because the specified snapshot is created before 2013-07-15. | 指定磁盘的源快照创建于2013年7月 15日（含）之前，不能重新初始化。 |
| 403 | InvalidSnapshot.Too Large | The capacity of snapshot exceeds 2000GB. | 快照容量超过 2000 GB。 |
| 403 | OperationDenied | The specified snapshot is not allowed to create disk. | 指定快照不支持创建磁盘。 |
| 403 | QuotaExceed.Portab leCloudDisk | The quota of portable cloud disk exceeds. | 可卸载磁盘数量已达上限。 |
| 403 | InvalidDiskCategory. ValueUnauthorized | The disk category is not authorized. | 该磁盘种类未经授权。 |
| 403 | InvalidSnapshotId.N otReady | The specified snapshot has not completed yet. | 指定的快照未完成。 |
| 403 | InvalidSnapshotId.N otDataDiskSnapshot | The specified snapshot is system disk snapshot. | 指定的快照为系统磁盘快照。 |
| 403 | InvalidDiskSize.TooS mall | Specified disk size is less than the size of snapshot. | 指定的磁盘容量小于快照容量。 |
| 403 | OperationDenied | The type of the disk does not support the operation. | 此磁盘种类不支持指定的操作。 |
| 403 | InvalidDataDiskCate gory.NotSupported | %s | 指定的数据磁盘类型无效。%s为变量，将根据调用API的实际情况动态返回错误信息。 |
| 403 | InvalidAccountStatu s.NotEnoughBalance | Your account does not have enough balance. | 账号余额不足，请您先充值再进行该操作。 |
| 403 | InvalidAccountStatu s.SnapshotServiceU navailable | Snapshot service has not been opened yet. | 快照服务未开通，操作无法执行。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidPayMethod | The specified pay method is not valid. | 没有可用的付费方式。 |
| 403 | InvalidDiskCategory. NotSupported | The specified disk category is not supported. | 指定的云盘类型不支持当前操作。 |
| 403 | InvalidDiskSize.NotS upported | The specified disk size is not supported. | 暂不支持您设置的磁盘容量。 |
| 403 | UserNotInTheWhiteL ist | The user is not in disk white list. | 您不在磁盘白名单中，请加入白名单后重试。 |
| 403 | QuotaExceed.PostPa idDisk | Living postPaid disks quota exceeded. | 按量付费磁盘数量已超出允许数量。 |
| 403 | InvalidRegion.NotSu pport | The specified region does not support byok. | 该地域不支持BYOK。 |
| 403 | UserNotInTheWhiteL ist | The user is not in byok white list. | 您不在byok白名单中，请加入白名单后重试。 |
| 403 | InvalidParameter.K MSKeyId.CMKNotEn abled | The CMK needs to be enabled. | 加密云盘设置了 KMSKeyId 后，CMK必须处于启用状态。您可以调用密钥管理服务的 DescribeKey 接口查询指定CMK的相关信息。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS 服务无权访问您的 KMS。 |
| 403 | SecurityRisk.3DVerif ication | We have detected a security risk with your default credit or debit card. Please proceed with verification via the link in your email. | 我们检测到您的默认信用卡或借记卡存在安全风险。请通过电子邮件中的链接进行验证。 |
| 403 | InvalidStatus.Upgra ding | The instance is upgrading; please try again later. | 实例正在升级，请稍后重试。 |
| 403 | QuotaExceed.Tags | %s | 标签数超过可以配置的最大数量。%s 为变量，将根据调用API的实际情况动态返回错误信息。 |
| 403 | OperationDenied.Sn apshotNotAllowed | The specified snapshot is not allowed to create disk. | 指定的快照不支持创建磁盘。 |
| 403 | LastTokenProcessin g | The last token request is processing. | 正在处理上一条令牌请求，请您稍后再试。 |
| 403 | InvalidParameter.Mu ltiAttach | The specified param MultiAttach is not valid. | MultiAttach 参数的取值有误。 |
| 403 | InvalidParameter.Mu ltiAttachAndInstanc eIdConflict | The parameter MultiAttach and InstanceId are conflict. | 不支持同时设置 MultiAttach 参数和 InstanceId 参数。 |
| 403 | InvalidParameter.Di skCategoryAndMulti AttachConflict | The specified disk category does not support multi attach set. | 共享块存储不支持设置 MultiAttach 参数。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidParameter.Di skCategoryAndMulti AttachNotMatch | The specified disk category does not support multi attach enabled. | 要创建的云盘类型不支持开启多重挂载。 |
| 403 | OperationDenied.Zo neNotSupportMultiA ttachDisk | The specified zone does support multi attach disk. | 指定的可用区不支持创建开启多重挂载特性的云盘。 |
| 403 | InvalidAccountStatu s.CouponAmountNot Enough | Your coupon balance is insufficient or has expired. | 代金券余额不足或已过期。 |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 404 | InvalidZoneId.NotFo und | The specified zone does not exist. | 指定的可用区 ID 不存在。 |
| 404 | InvalidSnapshotId.N otFound | The specified SnapshotId does not exist. | 指定的快照不存在，请您检查快照是否正确。 |
| 404 | InvalidResourceGro up.NotFound | The ResourceGroup provided does not exist in our records. | 资源组并不在记录中。 |
| 404 | InvalidParameter.K MSKeyId.NotFound | The specified KMSKeyId does not exist. | 指定的参数 KMSKeyId 不存在。 |
| 404 | InvalidInstanceId.No tFound | The InstanceId provided does not exist in our records. | 指定的实例不存在，请您检查实例 ID 是否正确。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### DescribeDisks

调用DescribeDisks查询一块或多块您已经创建的块存储（包括云盘以及本地盘）。

**接口说明**

请求参数 `RegionId` 、 `ZoneId` 、 `DiskIds` 和 `InstanceId` 等都是过滤器的概念，参数间是逻辑与 （AND）关系。

| 求参数 | DiskIds |  |
|---|---|---|
| DiskIds |  | 如果是 |

开启多重挂载特性的云盘可以挂载到多个实例上，您可以根据返回结果的Attachment列表查看云盘涉及的所有挂载信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云服务器ECS

| Action | String | 是 | DescribeDisks | 系统规定参数，取值：DescribeDisks。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao-**** | 块存储所属的地域ID。您可以调用 DescribeRegions查询地域ID。 |
| ZoneId | String | 否 | cn-qingdao-****- a | 可用区ID。您可以调用DescribeZones查询可用区ID。 |
| DiskIds | String | 否 | ["d- bp67acfmxazb4p ****", "d- bp67acfmxazb4p ****", … "d- bp67acfmxazb4p ****"] | 云盘或本地盘ID。一个带有格式的JSON数组，最多支持100个ID，用半角逗号（,）隔开。 |
| InstanceId | String | 否 | i- bp67acfmxazb4p **** | 云盘或本地盘挂载的实例ID。 |
| DiskType | String | 否 | all | 要查询的云盘或本地盘类型。取值范围： all：同时查询系统盘与数据盘。 system：只查询系统盘。 data：只查询数据盘。 默认值：all。 |
| Category | String | 否 | all | 数据盘的云盘种类。取值范围： cloud efficiency：高效云盘。 _ san efficiency：共享高效云盘。 _ cloud ssd：SSD云盘。 _ san ssd：共享SSD盘。 _ cloud pperf：高性能云盘。 _ cloud sperf：普通性能云盘。 _ 默认值：cloud efficiency。 _ |
| Status | String | 否 | All | 云盘状态。取值范围： In use：使用中。 _ Available：待挂载。 Attaching：挂载中。 Detaching：卸载中。 Creating：创建中。 ReIniting：初始化中。 All：所有状态。 默认值：All。 |
| SnapshotId | String | 否 | s- bp67acfmxazb4p **** | 创建云盘时使用的快照ID。 |

云服务器ECS

| Portable | Boolean | 否 | false | 云盘或本地盘是否支持卸载。取值范围： true：支持。可以独立存在，且可以在可用区内自由挂载和卸载。 false：不支持。不可以独立存在，且不可以在可用区内自由挂载和卸载。 |
|---|---|---|---|---|
| DeleteWithInstan ce | Boolean | 否 | false | 云盘是否设置了随实例释放。取值范围： true：云盘随实例一起释放。 false：云盘保留不释放。 默认值：false。 |
| DeleteAutoSnaps hot | Boolean | 否 | false | 释放云盘时，是否会同时释放自动快照。取值范围： true：是。 false：否。 默认值：false。 |
| PageNumber | Integer | 否 | 1 | 云盘或本地盘状态列表的页码。 起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。 最大值：100。 默认值：10。 |
| NextToken | String | 否 | AAAAAdDWBF2** ** | 查询凭证（Token），取值为上一次API调用返回的 NextToken 参数值。 |
| MaxResults | Integer | 否 | 50 | 返回的最大数。取值范围：1~500。 默认值：10。 |
| DiskName | String | 否 | test-DiskName | 云盘或本地盘名称。 |
| AutoSnapshotPoli cyId | String | 否 | sp- m5e2w2jutw8bv3 1a**** | 根据自动快照策略ID查询云盘。 |

云服务器ECS

| EnableAutoSnaps hot | Boolean | 否 | false | 云盘是否启用自动快照策略功能。 true：启用。 false：未启用。 说明创建后的云盘默认启用自动快照策略功能，您只需要为云盘绑定自动快照策略即可正常使用。 |  |
|---|---|---|---|---|---|
| EnableAutomated SnapshotPolicy | Boolean | 否 | false | 是否查询开启了自动快照策略的云盘。 true：已设置。 false：未设置。 默认值：false。 |  |
| Filter.1.Key | String | 否 | CreationStartTim e | 查询资源时的筛选键，取值必须为 CreationStartTime 。同时设置 Filter.1.Key 和 Filter.1.Valu e 可以查询在指定时间点后创建的资源信息。 |  |
| Filter.2.Key | String | 否 | CreationEndTime | 查询资源时的筛选键，取值必须为 CreationEndTime 。同时设置 Filter.2.Key 和 Filter.2.Valu e 可以查询在指定时间点前创建的资源信息。 |  |
| Filter.1.Value | String | 否 | 2017-12- 05T22:40:00Z | 查询资源时的筛选值。指定该参数时必须同时指定 Filter.1.Key 参数，格式为： yyyy-MM-ddTHH:mmZ ，采用UTC +0时区。 |  |
| Filter.2.Value | String | 否 | 2017-12- 06T22:40:00Z | 查询资源时的筛选值。指定该参数时必须同时指定 Filter.2.Key 参数，格式为： yyyy-MM-ddTHH:mmZ ，采用UTC +0时区。 |  |
| EnableShared | Boolean | 否 | false | 是否是共享块存储。取值范围： true：是。 false：否。 默认值：false。 |  |
| Encrypted | Boolean | 否 | false | 是否只筛选出加密云盘。取值范围： true：是。 false：否。 默认值：false。 |  |

|  |  | CreationStartTime |  |
|---|---|---|---|
|  |  | Filter.1.Key |  |
|  | e |  |  |

|  |  | CreationEndTime |  |
|---|---|---|---|
|  |  | Filter.2.Key |  |
|  | e |  |  |

云服务器ECS

| DryRun | Boolean | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会查询资源状况。检查项包括AccessKey是否有效、 RAM用户的授权情况和是否填写了必需参数。如果检查不通过，则返回对应错误。 如果检查通过，会返回错误码 DryRunOperation 。 false：发送正常请求，通过检查后返回 2XX HTTP状态码并直接查询资源状况。 默认值：false。 |
|---|---|---|---|---|
| KMSKeyId | String | 否 | 0e478b7a-4262- 4802-b8cb- 00d3fb408*** | 云盘使用的KMS密钥ID。 |
| MultiAttach | String | 否 | Disabled | 是否开启了多重挂载特性。取值范围： Disabled：未开启。 Enabled：已开启。 LegacyShared：用于查询共享块存储。 |
| Tag.N.key | String | 否 | hide | 云盘或本地盘的标签键。 说明为提高代码兼容性，请尽量使用Tag.N.Key参数。 |
| Tag.N.Key | String | 否 | TestKey | 云盘或本地盘的标签键。N的取值范围： 1~20。 使用一个标签过滤资源，查询到该标签下的资源数量不能超过1000个；使用多个标签过滤资源，查询到同时绑定了多个标签的资源数量不能超过1000个。如果资源数量超过 1000个，请使用ListTagResources接口进行查询。 |
| Tag.N.Value | String | 否 | TestValue | 云盘或本地盘的标签值。N的取值范围： 1~20。 |
| Tag.N.value | String | 否 | hide | 云盘或本地盘的标签值。 说明为提高代码兼容性，请尽量使用Tag.N.Key参数。 |
| AdditionalAttribut es.N | RepeatLi st | 否 | null | 其他属性值。 说明该参数即将停止使用，为提高代码兼容性，建议您尽量不要使用该参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云服务器ECS

| Disks | Array of Disk |  | 云盘或本地盘信息组成的集合。 |  |  |
|---|---|---|---|---|---|
| Disk |  |  |  |  |  |
| AttachedTime | String | 2018-01- 01T01:04:22Z | 挂载时间。按照ISO 8601标准表示，使用UTC+0 时间。格式为：yyyy-MM-ddThh:mmZ。 该参数值仅在 Status 参数值为 Available 时才有意义。 |  |  |
| Attachments | Array of Attachment |  | 云盘所涉及的挂载信息。由 Attachment 对象组成的列表，查询共享块存储时不返回该列表。 |  |  |
| Attachment |  |  |  |  |  |
| AttachedTime | String | 2022-04- 10T06:08:56Z | 该云盘最后一次挂载的时间。按照ISO 8601标准表示，使用UTC+0时间。格式为： yyyy-MM- ddThh:mmZ 。 |  |  |
|  |  |  |  | yyyy-MM- |  |
| Device | String | /dev/xvda | 云盘或本地盘挂载的实例的设备名，例如 /dev/xvdb 。该参数仅在 Status 参数值为 In use 时才有值，其他状态时为空。 _ |  |  |
| InstanceId | String | i- bp67acfmxazb4q*** * | 云盘或本地盘挂载的实例ID。 |  |  |
| AutoSnapshotP olicyId | String | sp- bp67acfmxazb4p*** * | 云盘采用的自动快照策略ID。 |  |  |
| BdfId | String | test | 说明该参数暂未支持。 |  |  |
| Category | String | cloud ssd _ | 云盘或本地盘种类。可能值： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD盘。 _ cloud essd：ESSD云盘。 _ cloud pperf：高性能云盘。 _ cloud sperf：普通性能云盘。 _ |  |  |
| CreationTime | String | 2018-01- 01T01:01:22Z | 创建时间。 |  |  |
| DeleteAutoSna pshot | Boolean | false | 是否同时删除自动快照。可能值： true：删除云盘上的快照。 false：保留云盘上的快照。 通过CreateSnapshot或者在控制台创建的快照， 不受这个参数的影响，会始终保留。 |  |  |

|  | Status |
|---|---|
| Available |  |

| Z | ddThh:mmZ |
|---|---|

云服务器ECS

| DeleteWithInst ance | Boolean | true | 是否随实例释放。可能值： true：释放实例时，这块云盘随实例一起释放。 false：释放实例时，这块云盘保留不释放。 |
|---|---|---|---|
| Description | String | This is a description example. | 云盘或本地盘描述。 |
| DetachedTime | String | 2018-01- 08T01:01:22Z | 卸载时间。 该参数值仅在 Status 参数值为 Available 时才有意义。 |
| Device | String | /dev/xvdb | 云盘或本地盘挂载的实例的设备名，例如/dev/xvdb。 该参数仅在 Status 参数值为 In use 时才 _ 有值，其他状态时为空。 说明该参数即将停止使用，为提高代码兼容性，建议您尽量不要使用该参数。 |
| DiskChargeTyp e | String | PostPaid | 说明该参数暂未支持。 |
| DiskId | String | d- bp18um4r4f2fve24* *** | 云盘或本地盘ID。 |
| DiskName | String | test-DiskName | 云盘或本地盘名称。 |
| EnableAutoSna pshot | Boolean | false | 云盘是否启用自动快照策略功能。可能值： true：启用。 false：未启用。 说明创建后的云盘默认启用自动快照策略功能，您只需要为云盘绑定自动快照策略即可正常使用。 |
| EnableAutomat edSnapshotPoli cy | Boolean | false | 云盘是否设置了自动快照策略。 true：已设置。 false：未设置。 默认值：false。 |
| Encrypted | Boolean | false | 是否只筛选出加密云盘。 true：是。 false：否。 默认值：false。 |
| ExpiredTime | String | 2018-01- 10T01:01:22Z | 说明该参数暂未支持。 |

|  | Status |
|---|---|
| Available |  |

| 开发指南·API参考 |  |  | 云服务器EC |
|---|---|---|---|

| IOPS | Integer | 4000 | 每秒读写（I/O）操作的次数上限，单位：次/s。 |
|---|---|---|---|
| IOPSRead | Integer | 2000 | 每秒读操作的次数上限，单位：次/s。 |
| IOPSWrite | Integer | 2000 | 每秒写操作的次数上限，单位：次/s。 |
| ImageId | String | m- bp13aqm171qynt3* *** | 创建ECS实例时使用的镜像ID，只有通过镜像创建的云盘才有值，否则为空。这个值在云盘的生命周期内始终不变。 |
| InstanceId | String | i- bp1j4i2jdf3owlhe*** * | 云盘或本地盘挂载的实例ID。 该参数值仅在 Status 参数值为 In use 时 _ 才有值，其他状态时为空。 |
| KMSKeyId | String | 0e478b7a-4262- 4802-b8cb- 00d3fb40**** | 云盘使用的KMS密钥ID。 |
| MountInstance Num | Integer | 1 | 共享存储挂载的实例数量。 |
| MountInstances | Array of MountInstance |  | 挂载到实例上的信息集合。 |
| MountInstance |  |  |  |
| AttachedTime | String | 2017-12- 05T2340:00Z | 挂载时间。按照ISO 8601标准表示，使用UTC +0 时间，格式为 yyyy-MM-ddTHH:mm:ssZ 。 |
| Device | String | /dev/xvda | 云盘或本地盘的挂载点。 |
| InstanceId | String | i- bp1j4i2jdf3owlhe*** * | 云盘或本地盘挂载的实例ID。 |
| MultiAttach | String | Disabled | 云盘是否开启了多重挂载特性。 |
| OperationLocks | Array of OperationLock |  | 云盘或本地盘锁定原因类型。 |
| OperationLock |  |  |  |
| LockReason | String | security | 云盘或本地盘被安全锁定的原因。 |
| PerformanceLe vel | String | null | 说明该参数暂未支持。 |

云服务器ECS

| Portable | Boolean | false | 云盘是否可卸载。可能值： true：支持。可以独立存在，且可以在可用区内自由挂载和卸载。 false：不支持。不可以独立存在，且不可以在可用区内自由挂载和卸载。 |
|---|---|---|---|
| ProductCode | String | test | 说明该参数暂未支持。 |
| RegionId | String | cn-qingdao-**** | 云盘或本地盘所属的地域ID。 |
| ResourceGroup Id | String | rg- bp67acfmxazb4p*** * | 说明该参数暂未支持。 |
| SerialNumber | String | bp18um4r4f2fve2** ** | 云盘或本地盘的序列号。 |
| Size | Integer | 2000 | 云盘或本地盘大小，单位：GiB。 |
| SourceSnapsho tId | String | s- bp67acfmxazb4p*** * | 创建云盘使用的快照ID。 如果创建云盘时，没有指定快照，则该参数值为空。该参数值在云盘的生命周期内始终不变。 |
| Status | String | Available | 云盘状态。可能值： In use：使用中。 _ Available：待挂载。 Attaching：挂载中。 Detaching：卸载中。 Creating：创建中。 ReIniting：初始化中。 |
| StorageClusterI d | String | hide | 说明该参数暂未支持。 |
| StorageSetId | String | ss-i- bp1j4i2jdf3owlhe*** * | 存储集ID。 |
| StorageSetParti tionNumber | Integer | 11 | 存储集分区数。 |
| Tags | Array of Tag |  | 云盘或本地盘的标签集合。 |
| Tag |  |  |  |
| TagKey | String | TestKey | 标签键。 |
| TagValue | String | TestValue | 标签值。 |

云服务器ECS

| Type | String | data | 云盘或本地盘类型。可能值： system：系统盘。 data：数据盘。 |
|---|---|---|---|
| ZoneId | String | cn-qingdao-****-a | 云盘或本地盘所属的可用区ID。 |
| NextToken | String | AAAAAdDWBF2**** | 本次调用返回的查询凭证值。 |
| PageNumber | Integer | 1 | 云盘或本地盘列表的页码。 |
| PageSize | Integer | 1 | 输入时设置的每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| TotalCount | Integer | 76 | 查询结果总条数。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-**** &PageNumber=1 &PageSize=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>76</TotalCount> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId> <PageSize>1</PageSize> <NextToken>AAAAAdDWBF2****</NextToken> <PageNumber>1</PageNumber> <Disks>
    <DetachedTime>2018-01-08T01:01:22Z</DetachedTime>
    <Category>cloud_ssd</Category>
    <KMSKeyId>0e478b7a-4262-4802-b8cb-00d3fb40****</KMSKeyId>
    <Description>This is a description example.</Description>
    <Size>2000</Size>
    <Encrypted>false</Encrypted>
    <DeleteAutoSnapshot>false</DeleteAutoSnapshot>
    <StorageSetPartitionNumber>11</StorageSetPartitionNumber>
    <IOPS>4000</IOPS>
    <MultiAttach>Disabled</MultiAttach>
    <ImageId>m-bp13aqm171qynt3****</ImageId>
    <StorageSetId>ss-i-bp1j4i2jdf3owlhe****</StorageSetId>
    <Status>Available</Status>
    <AttachedTime>2018-01-01T01:04:22Z</AttachedTime>
<IOPSRead>2000</IOPSRead>
```

云服务器ECS

```xml
    <IOPSRead>2000</IOPSRead>
    <IOPSWrite>2000</IOPSWrite>
    <ZoneId>cn-qingdao-****-a</ZoneId>
    <InstanceId>i-bp1j4i2jdf3owlhe****</InstanceId>
    <SourceSnapshotId>s-bp67acfmxazb4p****</SourceSnapshotId>
    <Device>/dev/xvdb</Device>
    <EnableAutomatedSnapshotPolicy>false</EnableAutomatedSnapshotPolicy>
    <DeleteWithInstance>true</DeleteWithInstance>
    <EnableAutoSnapshot>false</EnableAutoSnapshot>
    <AutoSnapshotPolicyId>sp-bp67acfmxazb4p****</AutoSnapshotPolicyId>
    <DiskName>test-DiskName</DiskName>
    <Portable>false</Portable>
    <Type>data</Type>
    <MountInstanceNum>1</MountInstanceNum>
    <SerialNumber>bp18um4r4f2fve2****</SerialNumber>
    <CreationTime>2018-01-01T01:01:22Z</CreationTime>
    <RegionId>cn-qingdao-****</RegionId>
    <DiskId>d-bp18um4r4f2fve24****</DiskId>
    <MountInstances>
        <AttachedTime>2017-12-05T2340:00Z</AttachedTime>
        <InstanceId>i-bp1j4i2jdf3owlhe****</InstanceId>
        <Device>/dev/xvda</Device>
    </MountInstances>
    <Attachments>
        <AttachedTime>2022-04-10T06:08:56Z</AttachedTime>
        <InstanceId>i-bp67acfmxazb4q****</InstanceId>
        <Device>/dev/xvda</Device>
    </Attachments>
    <OperationLocks>
        <LockReason>security</LockReason>
    </OperationLocks>
    <Tags>
        <TagKey>TestKey</TagKey>
        <TagValue>TestValue</TagValue>
    </Tags>
</Disks>
```

`JSON` 格式

```json
{
    "TotalCount": 76,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "PageSize": 1,
    "NextToken": "AAAAAdDWBF2****",
    "PageNumber": 1,
    "Disks": {
        "DetachedTime": "2018-01-08T01:01:22Z",
        "Category": "cloud_ssd",
        "KMSKeyId": "0e478b7a-4262-4802-b8cb-00d3fb40****",
        "Description": "This is a description example.",
        "Size": 2000,
        "Encrypted": false,
        "DeleteAutoSnapshot": false,
        "StorageSetPartitionNumber": 11,
        "IOPS": 4000,
        "MultiAttach": "Disabled",
"ImageId":"m-bp13aqm171qynt3****",
```

云服务器ECS

```
        ImageId: mbp13aqm171qynt3
```

,

```json
        "StorageSetId": "ss-i-bp1j4i2jdf3owlhe****",
        "Status": "Available",
        "AttachedTime": "2018-01-01T01:04:22Z",
        "IOPSRead": 2000,
        "IOPSWrite": 2000,
        "ZoneId": "cn-qingdao-****-a",
        "InstanceId": "i-bp1j4i2jdf3owlhe****",
        "SourceSnapshotId": "s-bp67acfmxazb4p****",
        "Device": "/dev/xvdb",
        "EnableAutomatedSnapshotPolicy": false,
        "DeleteWithInstance": true,
        "EnableAutoSnapshot": false,
        "AutoSnapshotPolicyId": "sp-bp67acfmxazb4p****",
        "DiskName": "test-DiskName",
        "Portable": false,
        "Type": "data",
        "MountInstanceNum": 1,
        "SerialNumber": "bp18um4r4f2fve2****",
        "CreationTime": "2018-01-01T01:01:22Z",
        "RegionId": "cn-qingdao-****",
        "DiskId": "d-bp18um4r4f2fve24****",
        "MountInstances": {
            "AttachedTime": "2017-12-05T2340:00Z",
            "InstanceId": "i-bp1j4i2jdf3owlhe****",
            "Device": "/dev/xvda"
        },
        "Attachments": {
            "AttachedTime": "2022-04-10T06:08:56Z",
            "InstanceId": "i-bp67acfmxazb4q****",
            "Device": "/dev/xvda"
        },
        "OperationLocks": {
            "LockReason": "security"
        },
        "Tags": {
            "TagKey": "TestKey",
            "TagValue": "TestValue"
        }
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDiskType.Val ueNotSupported | The specified disk type is not supported. | 指定的磁盘属性不支持。 |
| 400 | InvalidCategory.Val ueNotSupported | The specified disk category is not supported. | 不支持指定的磁盘种类。 |
| 400 | InvalidStatus.ValueN otSupported | The specified disk status is not supported. | 指定的磁盘状态不支持此类操作。 |
| 400 | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. | 指定的Tag.N.Key和Tag.N.Value不匹配。 |

云服务器ECS

| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
|---|---|---|---|
| 400 | InvalidRegion.NotFo und | The specified parameter RegionId is not valid. | RegionId参数不合法。 |
| 400 | InvalidZoneId.NotFo und | The zoneId provided does not exist in our records. | 指定的可用区ID不存在。 |
| 400 | MissingParamter.Re gionId | The regionId should not be null. | 参数RegionId不得为空。 |
| 400 | InvalidParameter.Di skIds | The specified parameter diskIds is not valid. | 指定的参数diskIds无效。 |
| 400 | IncompleteParamter | Some fields can not be null in this request. | 请求中缺失参数。 |
| 400 | InvalidParamter | Some parameters are invalid in this request. | 请求中包含非法参数。 |
| 400 | InvalidSnapshot.Not Found | The specified parameter SnapshotId is not valid. | 指定的SnapshotId不合法。 |
| 403 | InvalidDiskIds.Malfor med | The amount of specified disk Ids exceeds the limit. | 指定的磁盘ID格式不正确。 |
| 403 | UserNotInTheWhiteL ist | The user is not in volume white list. | 用户不在共享块存储白名单中，请您提交工单申请白名单。 |
| 403 | InvalidParameter.Mu ltiAttachAndEnableS haredNotMatch | The parameter MultiAttach and EnableShared are not match. | 设置的 MultiAttach 参数和 EnableShared 参数的值不兼容。 |
| 403 | InvalidParameter.Mu ltiAttach | The specified param MultiAttach is not valid. | MultiAttach 参数的取值有误。 |
| 404 | InvalidDiskChargeTy pe.NotFound | The DiskChargeType does not exist in our records | 指定的磁盘计费方式不存在。 |
| 404 | InvalidLockReason.N otFound | The specified LockReason is not found | 指定的锁定类型不存在。 |
| 404 | InvalidDiskIds.Value NotSupported | The specified parameter "DiskIds" is not supported. | 指定的磁盘ID无效。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### AttachDisk

调用AttachDisk为一台ECS实例挂载一块数据盘，或者挂载一块系统盘。实例和云盘必须在同一个可用区。

**接口说明**

调用该接口时，您需要注意： 云盘的状态必须为**待挂载**（ `Available` ）。 挂载数据盘时： 目标ECS实例必须处于**运行中**（ `Running` ）或者**已停止**（ `Stopped` ）状态。 云服务器ECS 挂载系统盘时： 目标ECS实例必须是卸载系统盘时的源实例。 目标ECS实例必须处于**已停止**（ `Stopped` ）状态。 您必须设置实例登录凭证。 查询ECS实例信息时，如果返回数据中包含 `{"OperationLocks": {"LockReason" : "security"}}` ，则禁止一切操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AttachDisk | 系统规定参数。取值：AttachDisk |
| DiskId | String | 是 | d- bp198f7xn673w2 rw**** | 待挂载的云盘ID。云盘（ DiskId ）和实例（ InstanceId ）必须在同一个可用区。 说明支持挂载数据盘和系统盘，相关约束条件请参见上文接口说明章节。 |
| InstanceId | String | 是 | i- bp1ahcvgu9z55p k7**** | 目标ECS实例的ID。 |
| Device | String | 否 | testName | 云盘设备名称。 说明该参数即将被弃用，为提高兼容性，建议您尽量使用其他参数。 |
| DeleteWithInstan ce | Boolean | 否 | false | 释放实例时，该云盘是否随实例一起释放。 true：释放。 false：不释放。 默认值：false。 说明将 DeleteWithInstance 置为 false 后，一旦ECS实例被安全控制，即 OperationLocks 中标记了 "LockReason" : "security" ，释放ECS实例时会忽略云盘的该属性，被同时释放。 |
| Bootable | Boolean | 否 | false | 是否作为系统盘挂载。 默认值：false。 说明设置为 Bootable=true 时，目标ECS 实例必须处于无系统盘状态。 |

| DeleteWithInstance |  |
|---|---|
| false |  |

|  |  |  | "LockReason" : |
|---|---|---|---|
|  |  | "security" |  |

云服务器ECS

| Password | String | 否 | EcsV587! | 挂载系统盘时，设置实例的用户名密码，仅对administrator和root用户名生效，其他用户名不生效。长度为8至30个字符，必须同时包含大小写英文字母、数字和特殊符号中的三类字符。特殊符号可以是： ()`~!@#$%^&*- +=\|{}[]:;'<>,.?/ _ 其中，Windows实例不能以斜线号（/）为密码首字符。 说明如果传入 Password 参数，建议您使用 HTTPS协议发送请求，避免密码泄露。 |
|---|---|---|---|---|
| KeyPairName | String | 否 | test- KeyPairName | 挂载系统盘时，为Linux系统ECS实例绑定的 SSH密钥对的名称。 Windows Server系统：不支持SSH密钥对。即使填写了该参数，只执行 Password 的配置。 Linux系统：密码登录方式会被初始化成禁止。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&DiskId=d-bp198f7xn673w2rw**** &InstanceId=i-bp1ahcvgu9z55pk7**** &DeleteWithInstance=false
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

云服务器ECS

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 404 | InvalidDiskId.NotFou nd | The specified disk does not exist. | 指定的磁盘不存在。请您检查磁盘ID 是否正确。 |
| 400 | InvalidDevice.Malfor med | The specified device is not valid. | 指定的磁盘设备名不存在。 |
| 403 | InstanceDiskLimitEx ceeded | The amount of the disk on instance in question reach its limits. | 指定实例已经达到可挂载磁盘的最大值。 |
| 403 | InvalidDevice.InUse | The specified device has been occupied. | 指定的设备已经挂载了磁盘。 |
| 403 | IncorrectDiskStatus | The operation is not supported in this status. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 403 | DiskNotPortable | The specified disk is not a portable disk. | 指定的磁盘不是可卸载的磁盘，Portable为false的磁盘无法卸载。 |
| 403 | InstanceLockedForS ecurity | The instance is locked due to security. | 您的资源被安全锁定，拒绝操作。 |
| 403 | ResourcesNotInSam eZone | The specified instance and disk are not in the same zone. | 指定的实例和磁盘不在同一可用区。 |
| 403 | InstanceExpiredOrIn Arrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). | 包年包月实例已过期，请您续费后再进行操作。 |
| 403 | DiskInArrears | The specified operation is denied as your disk owing fee. | 指定的磁盘已欠费。 |
| 400 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | DiskError | IncorrectDiskStatus. | 指定的磁盘状态不合法。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 400 | InvalidParameter | The input parameter is mandatory for processing this request is empty. | 参数不能为空。 |
| 403 | DiskId.ValueNotSup ported | The specified parameter diskid is not supported. | 指定的块存储类型不支持此操作。 |
| 403 | DiskId.StatusNotSup ported | The specified disk status is not supported. | 当前磁盘的状态不支持此操作。 |
| 404 | InvalidDisk.InUse | The specified disk has been occupied. | 指定的磁盘已占用。 |

云服务器ECS

| 404 | DiskAttachedNumbe rExceeded | The attaching times of the specified disk exceeded. | 指定的云盘所挂载的实例数量已达上限。 |
|---|---|---|---|
| 403 | UserNotInTheWhiteL ist | The user is not in disk white list. | 您不在磁盘白名单中，请加入白名单后重试。 |
| 400 | InvalidRegionId.MalF ormed | The specified RegionId is not valid | 指定的RegionId不合法。 |
| 400 | InvalidOperation.Ins tanceTypeNotSuppo rt | The instance type of the specified instance does not support hot attach disk. | 磁盘挂载的实例不支持磁盘热插拔操作。 |
| 400 | DiskCategory.Opera tionNotSupported | The operation is not supported to the specified disk due to its disk category | 由于磁盘种类限制，指定的磁盘不支持该操作。 |
| 400 | InvalidOperation.Ins tanceTypeNotSuppo rt | The specified disk which has kms key should only attach to ioOptimized instance. | 指定的实例无效，只有I/O优化类型的实例支持设置KMS Key。 |
| 403 | InvalidParameter.K MSKeyId.CMKNotEn abled | The CMK needs to be enabled. | 加密云盘设置了KMSKeyId后，CMK 必须处于启用状态。您可以调用密钥管理服务的DescribeKey接口查询指定CMK的相关信息。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 400 | InvalidParameter.All Empty | %s | 您没有输入任何参数，请输入必要的参数。 |
| 403 | InvalidInstanceType. NotSupportDiskCate gory | The instanceType of the specified instance does not support this disk category. | 指定的实例规格（InstanceType） 不支持当前实例的云盘类别。请尝试更换其它实例规格。关于实例规格支持的云盘类型，请参见实例规格族文档。 |

##### DetachDisk

接口说明调用该接口时，请注意：

| 状态为使用中 （ In Use )。 _ 必须处于运行中 （ Running 必须处于已停止 （ Stopped OperationLocks 中不能标记 |  |
|---|---|
| OperationLocks | 中不能标记 |

（ `Stopped` ）状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DetachDisk | 系统规定参数。 取值：DetachDisk。 |
| InstanceId | String | Query | 是 | i-bp67acfmxazb4p**** | 待卸载的ECS实例ID。 |
| DiskId | String | Query | 是 | d-bp67acfmxazb4p**** | 待卸载的云盘ID。 |
| DeleteWith Instance | Boole an | Query | 否 | false | 卸载系统盘时，设置自动释放属性。表示释放ECS实例时， 是否同时释放该系统盘。默认值：true。 true：释放。 false：不释放。云盘会被保留下来。 如果卸载的是数据盘，默认值为false。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
&InstanceId=i-bp67acfmxazb4p**** &DiskId=d-bp67acfmxazb4p****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

`XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

**错误码**

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 404 | InvalidDiskId.NotFou nd | The specified disk does not exist. | 指定的磁盘不存在。请您检查磁盘 ID 是否正确。 |
| 403 | IncorrectDiskStatus | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 403 | DiskNotPortable | The specified disk is not a portable disk. | 指定的磁盘不是可卸载的磁盘，Portable为false的磁盘无法卸载。 |
| 403 | InstanceLockedForS ecurity | The instance is locked due to security. | 您的资源被安全锁定，拒绝操作。 |
| 403 | DependencyViolatio n | The specified disk has not been attached on the specified instance. | 资源有其它依赖无法执行操作，请先将依赖取消关联。如：指定磁盘没有挂载在指定的实例上；指定安全组内有实例时无法删除安全组等。 |
| 403 | DiskTypeViolation | The specified disk is a system disk and cannot support the operation. | 指定的云盘是系统盘，不能卸载。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 400 | InvalidParameter | The input parameter is mandatory for processing this request is empty. | 参数不能为空。 |
| 403 | UserNotInTheWhiteL ist | The user is not in disk white list. | 您不在磁盘白名单中，请加入白名单后重试。 |
| 400 | InvalidRegionId.MalF ormed | The specified RegionId is not valid | 指定的 RegionId 不合法。 |
| 404 | InvalidDisk.AlreadyD etached | The specified disk has been detached. | 指定的磁盘已分离。 |
| 400 | InvalidOperation.Ins tanceTypeNotSuppo rt | The instance type of the specified instance does not support hot detach disk. | 磁盘挂载的实例不支持磁盘热插拔操作。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### ModifyDiskAttribute

调用ModifyDiskAttribute修改一个块存储的名称、描述、是否随实例释放等属性。

**接口说明**

云服务器ECS 当您调用该接口时设置了不随实例释放（DeleteWithInstance=false）属性，一旦磁盘挂载的ECS实例被安全锁定且OperationLocks中标记了 `"LockReason" : "security"` 的锁定状态，释放实例时会忽略磁盘的 DeleteWithInstance属性而被同时释放。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | ModifyDiskAttribu te | 系统规定参数。取值： ModifyDiskAttribute |
| DiskId | String | 否 | d- bp198f7xn673w2 rw**** | 待修改明细的磁盘ID。 说明 DiskId 和 DiskIds.N 两个参数不能同时被调用，请您根据需求任选其一传值。 |
| DiskIds.N | RepeatLi st | 否 | d- bp198f7xn673w2 rw**** | 待修改明细的多个磁盘ID。N的取值范围： 0~100。 说明 DiskId 和 DiskIds.N 两个参数不能同时被调用，请您根据需求任选其一传值。 |
| DiskName | String | 否 | test-DiskName | 磁盘名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http://和https://开头。可以包含数字、半角冒号（:）、下划线（ ）或者连字符（-）。 _ |
| Description | String | 否 | This is a description example. | 磁盘描述。 长度为2~256个英文或中文字符，不能以http://和https://开头。 |
| DeleteWithInst ance | Boolean | 否 | false | 磁盘是否随实例释放。默认值：无，无表示不改变当前的值。 在下列两种情况下，将参数 DeleteWithInstance设置成false时会报错。 磁盘的种类（category）为本地盘 （ephemeral）时。 磁盘的种类（category）为普通云盘 （cloud），且不可以卸载 （Portable=false）时。 |
| DeleteAutoSna pshot | Boolean | 否 | false | 删除磁盘时，是否同时删除其自动快照。默认值：无，无表示不改变当前的值。 |
| EnableAutoSna pshot | Boolean | 否 | true | 如果您已经创建了自动快照策略，是否应用于该磁盘。默认值：无，无表示不改变当前的值。 |

云服务器ECS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyDiskAttribute &DiskId=d-bp198f7xn673w2rw**** &DiskName=test-DiskName
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
| 404 | InvalidDiskId.NotFou nd | The specified disk does not exist. | 指定的磁盘不存在。请您检查磁盘 ID 是否正确。 |
| 400 | InvalidDiskName.Ma lformed | The specified disk name is wrongly formed. | 磁盘名称格式不正确。长度为2-128 个字符，以英文字母或中文开头，可包含数字，点号（.），下划线（ ） _ 或连字符（-）。 不能以http://和 https://开头。 |
| 404 | InvalidDescription.M alformed | The specified description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以 http:// 和 https:// 开头。 |
| 400 | NoAttributeToModify | No attribute to be modified in this request. | 没有任何属性被修改。 |
| 403 | QuotaExceed.Snaps hot | The snapshot quota exceeds. | 快照额度超过限制，若要存储新快照，在不影响业务的情况下，请您删除已有的老快照。 |
| 403 | DiskNotPortable | The specified disk is not a portable disk. | 指定的磁盘不是可卸载的磁盘，Portable为false的磁盘无法卸载。 |

云服务器ECS

| 403 | IncorrectDiskStatus | The operation is not supported in this status. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
|---|---|---|---|
| 400 | IncompleteParamter | Some fields can not be null in this request. | 请求中缺失参数。 |
| 403 | UserNotInTheWhiteL ist | The user is not in disk white list. | 您不在磁盘白名单中，请加入白名单后重试。 |
| 400 | InvalidRegionId.MalF ormed | The specified RegionId is not valid | 指定的 RegionId 不合法。 |
| 404 | InvalidInstanceId.No tFound | Specified attached instance does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |

##### ModifyDiskSpec

**接口说明**

调用该接口完成以下操作时，您需要注意： 变更一块云盘类型的注意事项，请参见《云服务器ECS用户指南》的变更云盘类型章节。 调用接口后，新的云盘类型立即生效。 开启多重挂载特性的云盘不支持云盘变配。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDiskSpec | 系统规定参数。取值：ModifyDiskSpec。 |
| DiskId | String | 是 | d- bp131n0q38u3a4 zi***** | 云盘的ID。 |
| DiskCategory | String | 否 | cloud ssd _ | 变配一块云盘，即修改一块云盘的类型。取值范围： cloud ssd：SSD云盘。 _ cloud efficiency：高效云盘。 _ cloud pperf：高性能云盘。 _ cloud sperf：普通性能云盘。 _ 默认值：空，表示不变配云盘。 |
| DryRun | Boolean | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求。检查项包括是否填写了必需参数、请求格式、业务限制和 ECS库存。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认）：发送正常请求，通过检查后返回2XX HTTP状态码并且直接变配云盘。 |

云服务器ECS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| OrderId | String | 20413515388**** | 说明该参数未开放使用。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |
| TaskId | String | t- bp67acfmxazb4p*** * | 变配云盘的任务ID。 |

**示例**

请求示例

```
&DiskId=d-bp131n0q38u3a4zi***** &DiskCategory=cloud_ssd
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

`JSON` 格式

```json
{
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidPerformanceL evel.Malformed | The specified parameter PerformanceLevel is not valid. | 指定的参数 PerformanceLevel 无效。 |
| 403 | DiskInArrears | The specified operation is denied as your disk owing fee. | 指定的磁盘已欠费。 |
| 403 | InstanceExpiredOrIn Arrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). | 包年包月实例已过期，请您续费后再进行操作。 |
| 403 | IncorrectDiskStatus | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |

云服务器ECS

| 403 | DiskCreatingSnapsh ot | The operation is denied due to a snapshot of the specified disk is not completed yet. | 指定的磁盘正在创建快照。 |
|---|---|---|---|
| 403 | OperationDenied | The type of the disk does not support the operation. | 此磁盘种类不支持指定的操作。 |
| 403 | OperationDenied.Pe rformanceLevelNot Match | The specified PerformanceLevel and disk size do not match. | 指定的性能等级与磁盘大小不匹配。 |
| 403 | InvalidInstanceType. NotSupportDiskCate gory | The instanceType of the specified instance does not support this disk category. | 指定的实例规格（InstanceType） 不支持当前实例的云盘类别。请尝试更换其它实例规格。关于实例规格支持的云盘类型，请参见实例规格族文档。 |
| 403 | OperationDenied.No Stock | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. | 库存不足。 |
| 403 | InvalidOperation.Mul tiAttachDisk | Multi attach disk does not support this operation. | 开启多重挂载特性的云盘不支持该操作。 |
| 404 | InvalidDiskId.NotFou nd | The specified disk does not exist. | 指定的磁盘不存在。请您检查磁盘 ID 是否正确。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |

##### ReInitDisk

**接口说明**

调用该接口时，您需要注意： 云盘的状态必须为**使用中**（In_use），云盘挂载的ECS实例的状态必须为**已停止**（Stopped）。 实例首次启动前，不能重新初始化挂载在其上的云盘。 对于系统盘，初始化到镜像的最初状态。若创建云盘的源镜像被删除，则无法初始化。 对于直接创建的数据盘，初始化到空盘状态。 对于通过快照创建的数据盘，初始化到快照状态。若源快照已被删除，则无法初始化并返回错误。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ReInitDisk | 系统规定参数。取值：ReInitDisk |
| DiskId | String | 是 | d- bp67acfmxazb4p **** | 指定的云盘ID。 |

云服务器ECS

| Password | String | 否 | EcsV587! | 重新初始化系统盘时，是否重置ECS实例的用户名密码。长度为8~30个字符，必须同时包含大小写英文字母、数字和特殊符号中的三类字符。特殊符号可以是： ()`~!@#$%^&*- +=\|{}[]:;'<>,.?/ _ 其中，Windows实例不能以正斜线（/）为密码首字符。 说明如果传入 Password 参数，建议您使用 HTTPS协议发送请求，避免密码泄露。 |
|---|---|---|---|---|
| KeyPairName | String | 否 | test- KeyPairName | 密钥对名称。 说明该参数仅适用于Linux实例。重新初始化系统盘时，您可以为 ECS实例绑定一个SSH密钥对，作为登录凭证。使用了SSH密钥对后，用户名密码的登录凭证方式将被禁用。 |
| AutoStartInstance | Boolean | 否 | true | 重新初始化云盘后，是否自动启动实例。 默认值：false。 |
| SecurityEnhance mentStrategy | String | 否 | Active | 当指定的云盘为系统盘时，重新初始化云盘后是否使用云安全中心服务。取值范围： Active：使用。该值仅支持公共镜像。 Deactive：不使用。该值支持所有镜像。 默认值：Deactive。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
&DiskId=d-bp67acfmxazb4p**** &KeyPairName=test-KeyPairName &SecurityEnhancementStrategy=Active
```

`&<`公共请求参数> 正常返回示例云服务器ECS `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDiskId.NotFou nd | The specified disk does not exist. | 指定的磁盘不存在。请您检查磁盘ID 是否正确。 |
| 403 | IncorrectDiskStatus | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The instance is locked due to security. | 您的资源被安全锁定，拒绝操作。 |
| 403 | InvalidSnapshot.Too Old | The disk is created from a snapshotId made before 2013- 07-15, it cannot be re-initiated the specified disk any more since the detached first time. | 创建于2013年7月15日之前的快照不支持此操作。 |
| 403 | OperationDenied | The snapshot which is used to create the specified disk has been deleted. | 用来创建指定磁盘的快照不存在。 |
| 403 | InstanceExpiredOrIn Arrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). | 包年包月实例已过期，请您续费后再进行操作。 |
| 403 | DiskCreatingSnapsh ot | The operation is denied due to a snapshot of the specified disk is not completed yet. | 指定的磁盘正在创建快照。 |
| 403 | InvalidSourceSnaps hot | The snapshot which is used to create the specified disk has been deleted. | 用于创建指定磁盘的快照已被删除。 |
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像ID是否正确。 |
| 403 | SharedImageDelete d | The specified image by others shared is deleted. | 指定的共享镜像已删除。 |
| 400 | InvalidPassword.Mal formed | The specified parameter "Password" is not valid. | 指定的Password参数不合法。 |

云服务器ECS

| 400 | DiskCategory.Opera tionNotSupported | The operation is not supported to the specified disk due to its disk category | 由于磁盘种类限制，指定的磁盘不支持该操作。 |
|---|---|---|---|
| 400 | InvalidKeyPairName. NotFound | The specified KeyPairName does not exist. | 指定的KeyPairName不存在。 |
| 400 | DependencyViolatio n.IoOptimize | The specified parameter InstanceId is not valid. | 指定的实例IO优化配置不合法。 |
| 403 | UserNotInTheWhiteL ist | The user is not in volume white list. | 用户不在共享块存储白名单中，请您提交工单申请白名单。 |
| 400 | InvalidRegionId.MalF ormed | The specified RegionId is not valid | 指定的RegionId不合法。 |
| 404 | InvalidDiskId.Operat ionNotSupported | The operation is not supported due to image not exist. | 指定的镜像不存在。 |
| 403 | InvalidParameter.K MSKeyId.CMKNotEn abled | The CMK needs to be enabled. | 加密云盘设置了KMSKeyId后，CMK 必须处于启用状态。您可以调用密钥管理服务的DescribeKey接口查询指定CMK的相关信息。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### ReplaceSystemDisk

调用ReplaceSystemDisk更换一台ECS实例的系统盘或者操作系统。系统盘的云盘ID会发生变化，原云盘会被释放。

**接口说明**

更换系统盘时，您需要注意： 不支持更换系统盘的云盘类型。 实例的状态必须为已停止（Stopped）状态。 被安全控制的ECS实例的OperationLocks参数包含"LockReason": "security"时，不能重启实例。 您可以通过参数SystemDisk.Size重新指定系统盘的容量大小。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ReplaceSystemDisk | 系统规定参数。取值： ReplaceSystemDisk |
| InstanceId | String | Query | 是 | i-bp67acfmxazb4p**** | 指定实例的ID。 |

| 开发指南·API参 | 考 |  |  |  | 云服务器EC |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ImageId | String | Query | 否 | m-bp67acfmxazb4p**** | 重置系统时使用的镜像ID。 |
| SystemDis k.Size | Intege r | Query | 否 | 80 | 新的系统盘容量，单位为 GiB。取值范围：Max{20, 参数ImageId对应的镜像大小}~2048。 默认值：Max{40, 参数 ImageId对应的镜像大小}。 |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 详情请参见《云服务器ECS开发指南》中的如何保证幂等性 。 |
| UseAdditio nalService | Boole an | Query | 否 | true | 是否使用阿里云提供的虚拟机系统配置（Windows： NTP、KMS；Linux：NTP、 YUM）。 说明挂载系统盘时（即设备名为/dev/xvda）有效。 |
| Password | String | Query | 否 | EcsV587! | 是否重置ECS实例的用户名密码。长度为8至30个字符，必须同时包含大小写英文字母、 数字和特殊符号中的三类字符。特殊符号可以是： ()`~!@#$%^&*- +=\|{} _ []:;'<>,.?/ 其中，Windows实例不能以斜线号（/）为密码首字符。 默认值：保持不变。 说明如果传入Password参数，建议您使用HTTPS协议发送请求，避免密码泄露。 |
| PasswordIn herit | Boole an | Query | 否 | false | 是否使用镜像预设的密码。 默认值：false。 说明使用该参数时，Password参数必须为空。同时您需要确保使用的镜像已经设置了密码。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| KeyPairNa me | String | Query | 否 | test-KeyPairName | 密钥对名称。 说明该参数仅对Linux系统 ECS实例生效。您可以为ECS 实例绑定一个SSH密钥对，作为登录凭证。使用了SSH密钥对后，用户名密码的登录凭证方式将被禁用。 |
| Platform | String | Query | 否 | CentOS | 操作系统发行版。取值范围： CentOS Ubuntu |
| Architectur e | String | Query | 否 | i386 | 系统架构。取值范围： i386 x86 64 _ |
| SecurityEn hancement Strategy | String | Query | 否 | Active | 更换系统盘后，是否使用云安全中心服务。取值范围： Active：使用。该值仅支持公共镜像。 Deactive：不使用。该值支持所有镜像。 默认值：Deactive。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DiskId | String | d- bp67acfmxazb4p*** * | 新系统盘的云盘ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ReplaceSystemDisk &InstanceId=i-bp67acfmxazb4p**** &ImageId=m-bp67acfmxazb4p**** &SystemDisk.Size=80 &ClientToken=123e4567-e89b-12d3-a456-426655440000 &PasswordInherit=false &KeyPairName=test-KeyPairName &SecurityEnhancementStrategy=Active
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式云服务器ECS

```json
{
    "RequestId": "337568C5-64F3-4B76-8CDD-D3D8C57B5B8C",
    "DiskId": "d-bp67acfmxazb4p****"
}
```

`XML` 格式

```xml
      <DiskId>d-bp67acfmxazb4p****</DiskId>
      <RequestId>F3CD6886-D8D0-4FEE-B93E-1B73239673DE</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 400 | InvalidSystemDiskSi ze.ValueNotSupport ed | The specified parameter SystemDisk.Size is invalid. | 指定的SystemDisk.Size不合法。 |
| 404 | InvalidInstanceId.No tFound | The specified instance does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | InvalidSystemDiskSt atus.IsTransfering | The current status of the resource does not support this operation, system disk is transfering. | 当前资源的状态不支持此操作，请再系统盘停止传输数据后重试。 |
| 403 | IncorrectDiskStatus | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像ID是否正确。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The instance is locked due to security. | 您的资源被安全锁定，拒绝操作。 |
| 403 | ImageNotSubscribe d | The specified image has not be subscribed. | 指定的镜像未在镜像市场订阅。 |
| 403 | ImageRemovedInMa rket | The specified market image is not available, Or the specified user defined image includes product code because it is based on an image subscribed from marketplace, and that image in marketplace includeing exact the same product code has been removed. | 指定的市场镜像不可用，或者指定的用户定义镜像包含产品代码，因为它基于从市场订购的镜像，并且市场中包含完全相同的产品代码的镜像已被删除。 |
| 500 | OperationDenied | Internal Error. | 内部错误。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter.Co nflict | The specified image does not support the specified instance type. | 指定的镜像不能用于指定的实例规格。 |
| 404 | InvalidSystemDiskSi ze.MoreThanMaxSiz e | The specified SystemDisk.Size parameter exceeds the maximum size. | 指定的系统盘大小超出最大容量。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | InstanceExpiredOrIn Arrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). | 包年包月实例已过期，请您续费后再进行操作。 |
| 403 | ChargeTypeViolatio n | The operation is not permitted due to charge type of the instance. | 付费方式不支持该操作，请您检查实例的付费类型是否与该操作冲突。 |
| 403 | DiskCreatingSnapsh ot | The operation is denied due to a snapshot of the specified disk is not completed yet. | 指定的磁盘正在创建快照。 |
| 403 | IoOptimized.NotSup ported | The specified image is not support IoOptimized Instance. | 指定的镜像不支持I/O优化型实例。 |
| 403 | ImageNotSupportIns tanceType | The specified image don not support the InstanceType instance. | 指定的镜像不支持此类实例规格。 |
| 403 | QuotaExceed.BuyIm age | The specified image is from the image market,You have not bought it or your quota has been exceeded. | 您暂时不能使用指定的市场镜像。 |
| 404 | InvalidSystemDiskSi ze.LessThanImageSi ze | The specified parameter SystemDisk.Size is less than the image size. | 指定的参数SystemDisk.Size小于镜像文件大小数值。 |
| 404 | InvalidSystemDiskSi ze.LessThanMinSize | The specified parameter SystemDisk.Size is less than the min size. | 指定的系统盘小于最低容量。 |
| 404 | NoSuchResource | The specified resource is not found. | 指定的资源不存在。 |
| 400 | InvalidSystemDiskSi ze.ImageNotSupport Resize | The specified image does not support resize. | 指定的镜像不支持扩容。 |
| 400 | InvalidSystemDiskSi ze | The specified parameter SystemDisk.Size is invalid. | 指定的SystemDisk.Size不合法。 |
| 403 | INST HAS UNPAID _ _ _ ORDER | The instance has unpaid order. | 该实例有未完成的账单。 |
| 400 | InvalidSystemDiskSi ze.ValueNotSupport ed | The specified parameter SystemDisk.Size is invalid | 指定的参数SystemDisk.Size不合法。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidPassword.Mal formed | The specified parameter "Password" is not valid. | 指定的Password参数不合法。 |
| 400 | InvalidPasswordPara m.Mismatch | The input password should be null when passwdInherit is true. | 启用PasswdInherit后，用户名密码应该设置为空。 |
| 400 | OperationDenied | The specified image contains the snapshot of the data disk,does not support this operation. | 包含了数据盘快照的镜像，不支持此操作。 |
| 400 | InvalidDiskCategory. ValueNotSupported | The specified parameter "DiskCategory" is not valid. | 指定的SystemDisk.Category参数有误。 |
| 403 | OperationDenied.Ins tanceCreating | The specified instance is creating. | 指定的实例已存在。 |
| 400 | InvalidParameter.Co nflict | %s | 您输入的参数无效，请检查参数之间是否冲突。 |
| 400 | InvalidSystemDiskSi ze.ValueNotSupport ed | %s | 当前操作不支持设置的系统盘大小。 |
| 400 | OperationDenied | %s | 拒绝操作。 |
| 400 | InvalidKeyPairName. NotFound | The specified KeyPairName does not exist. | 指定的KeyPairName不存在。 |
| 400 | DependencyViolatio n.IoOptimize | The specified parameter InstanceId is not valid. | 指定的实例IO优化配置不合法。 |
| 403 | InvalidParameter.No tMatch | %s | 您输入的参数无效，请检查参数之间是否冲突。 |
| 400 | MissingParameter.Ar chitecture | Architecture should not be null. | 参数Architecture不能为空。 |
| 400 | InvalidArchitecture. Malformed | Architecture is not valid. | 您输入的参数Architecture无效，请查看该参数格式是否正确。 |
| 400 | MissingParameter.Pl atform | Platform should not be null. | 参数Platform不能为空。 |
| 400 | InvalidPlatform.Malf ormed | Platform is not valid. | 指定的平台无效。 |
| 400 | InvalidParameter.All Empty | %s | 您没有输入任何参数，请输入必要的参数。 |
| 400 | InvalidDiskId.NotFou nd | The specified disk do not exist. | 指定的磁盘不存在。 |
| 400 | InvalidDatadisk.Disk StatusViolation | The operation is not permitted due to status of the Datadisk. | 当前数据盘的状态不支持此操作。 |
| 400 | InvalidDatadisk.Disk CategoryViolation | The operation is not permitted due to category of the Datadisk. | 该数据盘的类型不支持该操作。 |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ResourcesNotInSam eZone | The specified instance and disk are not in the same zone. | 指定的实例和磁盘不在同一可用区。 |
| 400 | InvalidSystemDiskSi ze.ValueNotSupport ed | The specified SystemDiskSize is not valid. | 指定的SystemDisk.Size不合法。 |
| 400 | MissingParameter | The input parameter "ImageId" that is mandatory for processing this request is not supplied. | 参数ImageId不得为空。 |
| 403 | ImageNotSupportIns tanceType | The specified instanceType is not supported by instance with marketplace image. | 指定的市场镜像不支持该实例规格。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | OperationDenied.Im ageNotValid | %s | 当前镜像不支持此操作。 |

##### ResizeDisk

**接口说明**

扩容前，请务必查询云盘采用的分区格式。如果是MBR格式，不支持扩容到2TiB以上，否则会造成数据丢失。对于MBR分区扩容，建议您重新创建并挂载一块数据盘，采用GPT分区格式后，再将已有数据拷贝至新的数据盘上。更多详情，请参见 《云服务器ECS用户指南》中的磁盘扩容。 支持扩容的云盘类型包括普通云盘（cloud）、高效云盘（cloud_efficiency）和SSD云盘（cloud_ssd）。 当云盘正在创建快照时，不允许扩容。 云盘挂载的实例的状态必须为运行中（Running）或者已停止（Stopped）。 扩容时，不会修改云盘分区和文件系统，您需要在扩容后自行分配存储空间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ResizeDisk | 系统规定参数。对于您自行拼凑HTTP/HTTPS URL发起的 API请求，Action为必选参数。取值：ResizeDisk |
| DiskId | String | Query | 是 | d-bp67acfmxazb4p**** | 云盘ID。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Type | String | Query | 否 | offline | 扩容云盘的方式。取值范围： offline（默认）：离线扩容。扩容后，您必须在控制台重启实例或者调用API RebootInstance使操作生效。 online：在线扩容，无需重启实例即可完成扩容。 云盘类型支持高效云盘和 SSD云盘。 |
| NewSize | Intege r | Query | 是 | 1900 | 希望扩容到的云盘容量大小。 单位为GiB。取值范围： 高效云盘 （cloud efficiency）： _ 20~32768 SSD云盘（cloud ssd）： _ 20~32768 普通云盘（cloud）： 5~2000 指定的新云盘容量必须比原云盘容量大。 当数据盘的类型选择为高效云盘（cloud efficiency）或者 _ SSD盘（cloud ssd）时，如 _ 果填写的容量超过2 TB，注意按照以下EBS集群的机器数量与推荐的云盘最大建议值 （机器数量：云盘最大值）进行填写。 6台：2 TB 12台：4 TB 15台：5 TB 24台：8 TB 云盘最大建议值的计算公式为：云盘最大大小S = N/3， 其中N为相应EBS集群的机器数量，结果向下取整。例如： 如果EBS集群的机器数量为6 台，则建议创建的云盘容量不超过2 TB。 |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 详情请参见《云服务器ECS开发指南》中的如何保证幂等性。 |

**返回数据**

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F3CD6886-D8D0- 4FEE-B93E- 1B73239673DE | 请求ID。 |

**示例**

请求示例

```
&DiskId=d-bp67acfmxazb4p**** &NewSize=1900 &ClientToken=123e4567-e89b-12d3-a456-426655440000
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "RequestId": "F3CD6886-D8D0-4FEE-B93E-1B73239673DE"
}
```

`XML` 格式

```xml
      <RequestId>F3CD6886-D8D0-4FEE-B93E-1B73239673DE</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidDataDiskSize. ValueNotSupported | The specified DataDisk.n.Size beyond the permitted range, or the capacity of snapshot exceeds the size limit of the specified disk category. | 指定的DataDisk.n.Size超出允许范围，或者快照的容量超过指定磁盘类别的大小限制。 |
| 404 | InvalidDiskId.NotFou nd | The specified disk does not exist. | 指定的磁盘不存在。请您检查磁盘ID 是否正确。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | OperationDenied | The type of the disk does not support the operation. | 此磁盘种类不支持指定的操作。 |
| 403 | OperationDenied | The status of the disk or the instance that the disk is attaching with does not support the operation. | 此磁盘或实例状态无法执行指定的操作。 |
| 403 | InvalidDiskSize.TooS mall | Specified new disk size is less than the original disk size. | 指定的新磁盘小于原始磁盘。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidDiskSize.TooL arge | Specified new disk size is beyond the permitted range. | 指定的新磁盘大小超过限制。 |
| 403 | InstanceExpiredOrIn Arrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). | 包年包月实例已过期，请您续费后再进行操作。 |
| 403 | DiskError | IncorrectDiskStatus | 指定的磁盘状态不合法。 |
| 403 | DiskInArrears | The specified operation is denied as your disk owing fee. | 指定的磁盘已欠费。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | DiskCreatingSnapsh ot | The operation is denied due to a snapshot of the specified disk is not completed yet. | 指定的磁盘正在创建快照。 |
| 400 | InvalidDataDiskCate gory.ValueNotSuppo rted | %s | 指定的数据磁盘类型无效。 |
| 400 | InvalidParameter.Co nflict | %s | 您输入的参数无效，请检查参数之间是否冲突。 |
| 400 | InvalidDataDiskSize. ValueNotSupported | %s | 指定的数据盘容量无效。 |
| 400 | InvalidSystemDiskSi ze.ValueNotSupport ed | %s | 当前操作不支持设置的系统盘大小。 |
| 403 | InvalidDiskSize | Specified new disk size is less than or equal the original disk size. | 指定的新磁盘大小必须大于原始磁盘大小。 |
| 400 | IncompleteParamter | Some fields can not be null in this request. | 请求中缺失参数。 |
| 403 | Operation.Conflict | The operation may conflicts with others. | 该操作与其他操作冲突。 |
| 403 | InstanceLockedForS ecurity | The instance is locked due to security. | 您的资源被安全锁定，拒绝操作。 |
| 403 | IncorrectDiskStatus | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 403 | UserNotInTheWhiteL ist | The user is not in disk white list. | 您不在磁盘白名单中，请加入白名单后重试。 |
| 400 | InvalidRegionId.MalF ormed | The specified RegionId is not valid | 指定的RegionId不合法。 |

|  | 云服务器ECS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidDiskCategory. NotSupported | The specified disk category is not supported. | 指定的云盘类型不支持当前操作。 |
| 400 | InvalidParam.Type | The specified type is not supported. | 指定的参数Type无效。 |
| 403 | InvalidRegion.NotSu pport | The specified region does not support resize online. | 该地域不支持在线扩容。 |
| 403 | InvalidDiskCategory. NotSupported | The specified disk category does not support resize online. | 指定的磁盘类型不支持在线扩容。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support resize online. | 当前资源的状态不支持此操作。 |
| 403 | InvalidInstanceStatu s.NotRunning | The status of instance to which the disk attachs must be running when resizing online. | 在线调整磁盘大小时，磁盘连接到的实例的状态必须正在运行。 |
| 403 | IncorrectDiskStatus | The current status of the resource does not support resize online | 当前资源的状态不支持在线扩容。 |
| 400 | LastOrderProcessing | The previous order is still processing, please try again later. | 订单正在处理中，稍后重试。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | SecurityRisk.3DVerif ication | We have detected a security risk with your default credit or debit card. Please proceed with verification via the link in your email. | 我们检测到您的默认信用卡或借记卡存在安全风险。请通过电子邮件中的链接进行验证。 |
| 400 | InvalidSystemDiskSi ze.ImageNotSupport Resize | The specified image does not support resize. | 指定的镜像不支持扩容。 |

##### DeleteDisk

**接口说明**

调用该接口时，您需要注意： 您的磁盘手动快照会被保留。 您可以通过ModifyDiskAttribute设置是否保留或者同时释放自动快照。建议您及时删除不必要的快照，以保持足够的快照额度完成周期性的自动快照策略。 释放磁盘时，云盘的状态必须为待挂载（Available）。 如果指定ID的磁盘不存在，请求将被忽略。 云服务器ECS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDisk | 系统规定参数。取值：DeleteDisk |
| DiskId | String | 是 | d- bp198f7xn673w2 rw**** | 需要释放的云盘设备ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
&DiskId=d-bp198f7xn673w2rw****
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
| 403 | IncorrectDiskStatus | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | DiskNotPortable | The specified disk is not a portable disk. | 指定的磁盘不是可卸载的磁盘，Portable为false的磁盘无法卸载。 |

云服务器ECS

| 403 | DiskTypeViolation | The specified disk is a system disk and cannot support the operation. | 指定的云盘是系统盘，不能卸载。 |
|---|---|---|---|
| 403 | DiskCreatingSnapsh ot | The operation is denied due to a snapshot of the specified disk is not completed yet. | 指定的磁盘正在创建快照。 |
| 403 | IncorrectDiskStatus. Initializing | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 404 | InvalidDiskId.NotFou nd | The specified disk does not exist. | 指定的磁盘不存在。请您检查磁盘ID 是否正确。 |
| 403 | DiskStillAttached | The disk is still attached to the disk. | 磁盘仍然挂载在实例上。 |
| 403 | UserNotInTheWhiteL ist | The user is not in disk white list. | 您不在磁盘白名单中，请加入白名单后重试。 |
| 400 | InvalidRegionId.MalF ormed | The specified parameter RegionId is not valid. | 指定的RegionId不合法。 |
| 403 | InvalidDiskStatus.De leteProtection | The specified disk is under delete protection, can not be deleted. | 指定的云盘处于删除保护状态。可能原因：该云盘作为系统盘从源实例上卸载，被卸载的系统盘会作为数据盘保留下来。源实例未释放前，被卸载的系统盘无法被主动释放。 |

##### ResetDisks

通过实例快照回滚一个或多个云盘。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ResetDisks | 系统规定参数。取值： ResetDisks |
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 地域ID。您可以调用 DescribeRegions查询地域 ID。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DryRun | Boole an | Query | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会查询资源状况。检查项包括AccessKey是否有效、RAM用户的授权情况和是否填写了必需参数。 如果检查不通过，则返回对应错误。如果检查通过，会返回错误码 DryRunOperation 。 false：发送正常请求，通过检查后返回2XX HTTP状态码并直接查询资源状况。 默认值：false。 |
| Disk | Repea tList | Query | 是 | / | 云盘列表。 |
| - SnapshotId | String |  | 否 | s-bp67acfmxazb4p**** | 指定云盘对应的快照ID。 |
| -DiskId | String |  | 否 | d-bp67acfmxazb4p**** | 指定待回滚的云盘ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| OperationProgr essSet | Array | {"progress": "75%", "status": "in progress", "step": "data processing"} | 回滚一个或多个云盘时的操作状态信息合集。 |
| - RelatedItemSet | Array | / | 资源信息类型。 |
| --Name | String | testName | 文件名称。 |
| --Value | String | ecs.g5.large | 标签值。 |
| -ErrorMsg | String | testErrorMsg | 错误信息。回滚成功时返回空值。 |
| -ErrorCode | String | 400 | 错误代码。 |
| - OperationStatu s | String | Success | 操作是否成功。 成功返回Success，失败返回 ErrorCode和ErrorMsg信息。 |

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-**** &Disk=/
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****",
 "OperationProgressSet":[
  {
   "OperationStatus":"Success",
   "ErrorMsg":"testErrorMsg",
   "ErrorCode":"400",
   "RelatedItemSet":[
    {
     "Value":"ecs.g5.large",
     "Name":"testName"
    }
```

]

```
  }
```

]

```
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DISK CATEGORY OP _ _ ERATION NOT SUPP _ _ ORTED | DiskCategory.OperationNotSupp orted | The operation is not supported to the specified disk due to its disk category |
| 400 | Abs.InvalidRegionId. MalFormed | InvalidRegionId.MalFormed | The specified RegionId is not valid |
| 400 | DRYRUN SUCCESS _ | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 403 | DISK STATUS ERRO _ _ R | IncorrectDiskStatus | The current disk status does not support this operation. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | -215 | IncorrectInstanceStatus | The current status of the resource does not support this operation. |
| 403 | 21001 | InstanceLockedForSecurity | The instance is locked due to security. |
| 403 | DISK SNAPSHOT NO _ _ T MATCH _ | InvalidParameter.Mismatch | The specified snapshot is not created from the specified disk. |
| 403 | ENCRYPTED ATTRIB _ UTE NOT MATCH _ _ | InvalidParameter.Mismatch | Non-encrypted disk can not be reset by encrypted snapshot. |
| 403 | SNAPSHOT AT BEF _ _ ORE ASSIGN DATE _ _ _ AND DETACH _ | InvalidSnapshot.TooOld | The snapshotId is created before 2013-07-15, it cannot be restored since the first time the disk detached. |
| 403 | DISK ECS EXPIRED _ _ _ ERROR | InstanceExpiredOrInArrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). |
| 403 | SNAPSHOT IN BLAC _ _ K LIST _ | OperationDenied | The specified snapshot dees not support ResetDisk. |
| 403 | SNAPSHOT CREATE _ NOT FINISHED _ _ | InvalidSnapshotId.NotReady | The specified snapshot has not completed yet. |
| 403 | -4003 | IncorrectDiskStatus | The current disk status does not support this operation. |
| 403 | -912 | IncorrectDiskStatus | The current disk status does not support this operation. |
| 403 | ACCOUNT OVERDUE _ | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |
| 403 | SNAPSHOT SERVICE _ UNAVAILABLE _ | InvalidAccountStatus.SnapshotS erviceUnavailable | Snapshot service has not been opened yet. |
| 403 | ECS IN PENDING _ _ | IncorrectInstanceStatus | The current status of the resource does not support this operation. |
| 403 | DISK ECS BIZ STAT _ _ _ US ERROR _ | IncorrectInstanceStatus | The current status of the resource does not support this operation. |
| 403 | ECS TASK CONFLIC _ _ T | Operation.Conflict | The operation may conflicts with others. |
| 403 | VOLUME STATUS E _ _ RROR | IncorrectDiskStatus | The current disk status does not support this operation. |
| 403 | VOLUME BIZ STATU _ _ S ERROR _ | IncorrectDiskStatus | The current disk status does not support this operation. |
| 403 | 401 | UserNotInTheWhiteList | The user is not in disk white list. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | CMKUnauthorized | InvalidParameter.KMSKeyId.CMK Unauthorized | The CMK needs to be added ECS tag |
| 403 | CMKNotEnabled | InvalidParameter.KMSKeyId.CMK NotEnabled | The CMK needs to be enabled. |
| 403 | KMSUnauthorized | InvalidParameter.KMSKeyId.KMS Unauthorized | ECS service have no right to access your KMS. |
| 403 | DISK HAS UNFINISH _ _ ED SNAPSHOT _ | IncorrectDiskStatus.HasUnfinish edSnapshot | The current disk has unfinished snapshot. |
| 403 | InvalidRegionId.Not Support | InvalidRegion.NotSupport | The specified region does not support resetting disks. |
| 403 | USER NOT IN WHIT _ _ _ E LIST _ | UserNotInTheWhiteList | The user is not in the white list of resetting disks. |
| 403 | VOLUME NOT SUPP _ _ ORT | InvalidDisk.ShareVolume | %s |
| 403 | MULTI ATTACH DIS _ _ K NOT SUPPORT _ _ | InvalidOperation.MultiAttachDisk | Multi attach disk does not support this operation. |
| 404 | -905 | InvalidDiskId.NotFound | The specified disk does not exist. |
| 404 | RAM.DiskNotFound | Disk.NotFound | The specified disk does not exist. |
| 404 | -106 | InvalidSnapshotId.NotFound | The specified SnapshotId does not exist. |
| 404 | ECS NOT FOUND _ _ | InvalidInstanceId.NotFound | The specified InstanceId does not exist. |
| 404 | STORAGE NOT FOU _ _ ND | InvalidDiskId.NotFound | The specified disk does not exist. |
| 404 | RAM.VolumeNotFou nd | InvalidDiskId.NotFound | The specified disk does not exist. |
| 404 | DISK NOT FOUND _ _ | InvalidDiskId.NotFound | The specified disk does not exist. |
| 404 | -140 | InvalidRegionId.NotFound | The RegionId provided does not exist in our records. |
| 404 | SNAPSHOT NOT EXI _ _ ST | InvalidSnapshot.NotFound | The SnapshotId provided does not exist in our records. |
| 500 | -1000021 | InternalError | The request processing has failed due to some unknown error. |
| 500 | -3010 | InternalError | The request processing has failed due to some unknown error. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -90 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | RAMSerivceUnavaila bleTemporary | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -1000016 | InternalError | The request processing has failed due to some unknown error, exception or failure. |

#### 快照

##### CreateSnapshot

**接口说明**

以下场景中，您无法为指定的云盘创建快照： 云盘保留的手动快照数达到了256份。 上份快照还未完成创建。 云盘挂载的实例从未启动过。

| Stopped |  | ）或者运行中（ | Running | ）状态。 |
|---|---|---|---|---|
| 数据中包含 | {"OperationLocks": {"LockReason" : "security"}} |  |  |  |

止一切操作。 创建快照时，您需要注意： 新建一台云服务器ECS或者更换系统盘大约一小时后才可以创建快照，新增一块数据盘可创建快照的时间取决于云盘数据的大小。 如果云盘已挂载到ECS实例上，创建快照期间请勿变更实例状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateSnapshot | 系统规定参数。取值：CreateSnapshot。 |
| DiskId | String | 是 | d- bp1s5fnvk4gn2tw s0**** | 云盘ID。您可以调用DescribeDisks查询云盘ID。 |
| SnapshotName | String | 否 | test-Snapshot**** | 快照的显示名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 或 https:// 开头。可以包含数字、半角冒号（:）、下划线（ ）或 _ 者短划线（-）。 为防止和自动快照的名称冲突，不能以auto 开头。 |

云服务器ECS

| Description | String | 否 | This is a description example. | 快照的描述。长度为2~256个英文或中文字符，不能以 http:// 或 https:// 开头。 默认值：空。 |
|---|---|---|---|---|
| RetentionDays | Integer | 否 | 30 | 设置快照的保留时间，单位为天。超过保留时间后快照会被自动释放，取值范围： 1~65535。 默认值：空，表示快照不会被自动释放。 |
| Category | String | 否 | Standard | 快照类型。取值范围： Standard：普通快照 Flash：本地快照说明该参数即将被弃用，为提高兼容性，建议您尽量使用参数 InstantAccess 。该参数和参数 InstantAccess 不能同时传值。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见《云服务器ECS开发指南》中的如何保证幂等性。 |
| Tag.N.value | String | 否 | null | 快照的标签值。 说明为提高兼容性，建议您尽量使用Tag.N.Value参数。 |
| Tag.N.key | String | 否 | null | 快照的标签键。 说明为提高兼容性，建议您尽量使用Tag.N.Key参数。 |
| Tag.N.Key | String | 否 | TestKey | 快照的标签键。N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Tag.N.Value | String | 否 | TestValue | 快照的标签值。N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128 个字符，不能以acs:开头，不能包含 http:// 或者 https:// 。 |

云服务器ECS

| InstantAccess | Boolean | 否 | false | 是否开启快照极速可用功能。取值范围： true：开启。仅高性能云盘和普通性能云盘支持开启该功能。 说明启用快照极速可用功能后，即使快照还没有创建完成，您也可以使用快照回滚云盘或者跨可用区创建云盘。无论多大的高性能云盘或普通性能云盘，均能够快速确保该快照可用。 false：关闭。即创建普通快照。 默认值：false 说明该参数和参数 Category 不能同时传值。更多信息，请参见接口说明。 |
|---|---|---|---|---|
| InstantAccessRet entionDays | Integer | 否 | 1 | 设置快照极速可用功能的保留时间，保留时间到期后快照将自动释放。该参数在 InstantAccess=true 时生效。单位：天。取值范围：1~65535。 默认与参数 RetentionDays 的值一致。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| SnapshotId | String | s- bp17441ohwka0yuh **** | 快照ID。 |

**示例**

请求示例

```
&DiskId=d-bp1s5fnvk4gn2tws0**** &SnapshotName=test-SnapshotName &Description=This is a description example. &ClientToken=123e4567-e89b-12d3-a456-42665544**** &Tag.1.Key=TestKey &Tag.1.Value=TestValue
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
          <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
          <SnapshotId>s-bp17441ohwka0yuh****</SnapshotId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "SnapshotId": "s-bp17441ohwka0yuh****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDiskId.NotFou nd | The specified DiskId does not exist. | 指定的磁盘不存在。请您检查磁盘ID 是否正确。 |
| 400 | InvalidSnapshotNam e.Malformed | The specified SnapshotName is wrongly formed. | 快照名称格式不合法。 |
| 404 | InvalidDescription.M alformed | The specified description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
| 400 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | IncorrectDiskStatus. CreatingSnapshot | A previous snapshot creation is in process. | 当前磁盘有创建中的快照，请您等待创建完成再试。 |
| 403 | InstanceLockedForS ecurity | The disk attached instance is locked due to security. | 磁盘挂载的实例因安全原因被锁定。 |
| 403 | IncorrectDiskStatus. NeverAttached | The specified disk has never been attached to any instance. | 可卸载的云磁盘创建后未被挂载，内容没有变化。 |
| 403 | QuotaExceed.Snaps hot | The snapshot quota exceeds. | 快照额度超过限制，若要存储新快照，在不影响业务的情况下，请您删除已有的老快照。 |
| 403 | IncorrectDiskStatus. NeverUsed | The specified disk has never been used after creating. | 磁盘创建后未被使用，内容没有变化。 |
| 403 | CreateSnapshot.Fail ed | The process of creating snapshot is failed. | 创建快照失败。 |
| 403 | DiskInArrears | The specified operation is denied as your disk has expired. | 磁盘欠费过期。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | DiskId.ValueNotSup ported | The specified parameter diskid is not supported. | 指定的块存储类型不支持此操作。 |

云服务器ECS

| 400 | DiskCategory.Opera tionNotSupported | The operation is not supported to the specified disk due to its disk category | 由于磁盘种类限制，指定的磁盘不支持该操作。 |
|---|---|---|---|
| 403 | IncorrectDiskStatus | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 403 | InvalidAccountStatu s.NotEnoughBalance | Your account does not have enough balance. | 账号余额不足，请您先充值再进行该操作。 |
| 403 | InvalidAccountStatu s.SnapshotServiceU navailable | Snapshot service has not been opened yet. | 快照服务未开通，操作无法执行。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | IncorrectVolumeStat us | The current volume status does not support this operation. | 共享块存储状态不支持当前操作。 |
| 404 | InvalidVolumeId.Not Found | The specified volume does not exist. | 指定的共享块存储不存在，请您检查共享块存储是否正确。 |
| 403 | IdempotentParamet erMismatch | The specified clientToken is used. | 指定的客户令牌已经被使用。 |
| 403 | IncorrectDiskType.N otSupport | The specified device type is not supported. | 指定磁盘存储类型不支持此操作。 |
| 403 | IncorrectDiskStatus. Transferring | The specified device is transferring, you can retry after the process is finished. | 指定磁盘正在迁移中，请在迁移完毕后重试。 |
| 403 | InvalidParameter.K MSKeyId.CMKNotEn abled | The CMK needs to be enabled. | 加密云盘设置了KMSKeyId后，CMK 必须处于启用状态。您可以调用密钥管理服务的DescribeKey接口查询指定CMK的相关信息。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 403 | IdempotentProcessi ng | The previous idempotent request(s) is still processing. | 先前的幂等请求仍在处理中，请稍后重试。 |
| 400 | InvalidRetentionDay s.Malformed | The specified RetentionDays is not valid. | 指定的保留天数无效。请检查 RetentionDays参数值是否正确。 |
| 403 | QuotaExceed.Tags | %s | 标签数超过可以配置的最大数量。%s 为变量，将根据调用API的实际情况动态返回错误信息。 |

云服务器ECS

| 403 | InvalidSnapshotCate gory.Malformed | The specified Category is not valid. | 指定的快照类型无效。请检查 Category参数值是否正确。 |
|---|---|---|---|

##### DescribeSnapshots

调用DescribeSnapshots查询一台ECS实例或一块云盘所有的快照列表。 接口说明 `InstanceId` 、 `DiskId` 和 `SnapshotIds` 不是必需的请求参数，但是可以构建过滤器逻辑，参数之间为逻辑与（And）关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| Action | String | Query | 是 | DescribeSnapshots |  | 系统规定参数，取值： DescribeSnapshots。 |  |  |
| InstanceId | String | Query | 否 | i-bp67acfmxazb4p**** |  | 指定的实例ID。您可以调用 DescribeInstances 查询实例ID。 |  |  |
| DiskId | String | Query | 否 | d-bp67acfmxazb4p**** |  | 指定的云盘ID。您可以调用 DescribeSnapshots 查询云盘ID。 |  |  |
| SnapshotLi nkId | String | Query | 否 | sp-bp67acfmxazb4p**** |  | 快照链ID。您可以调用 DescribeSnapshotLin ks 查询云盘快照链ID。 |  |  |
|  |  |  |  |  |  |  | DescribeSnapshotLin |  |
|  |  |  |  |  |  | ks |  |  |
| RegionId | String | Query | 是 | cn-qingdao-env***-d** |  | 云盘所属于的地域ID。您可以调用 DescribeRegions 查询地域ID。 |  |  |
| SnapshotId s | String | Query | 否 | ["s- bp67acfmxazb4ph****", "s- bp67acfmxazb4pk****", … "s- bp67acfmxazb4pj****"] |  | 快照标识编码。取值可以由多个快照ID组成一个JSON数组，最多支持100个ID，ID之间用半角逗号（,）隔开。 |  |  |
| PageNumb er | Intege r | Query | 否 | 1 |  | 快照列表的页码。 起始值：1。 默认值：1。 |  |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| PageSize | Intege r | Query | 否 | 10 | 分页查询时设置的每页行数。 最大值：100。 默认值：10。 |  |  |
| NextToken | String | Query | 否 | caeba0bbb2be03f84eb48 b699f0a**** | 查询起始标志。由上一次的请求结果中获取。 |  |  |
| MaxResult s | Intege r | Query | 否 | 10 | 分页查询时每页行数。 最大值：100。 默认值：10。 |  |  |
| SnapshotN ame | String | Query | 否 | test-SnapshotName | 快照名称。 |  |  |
| Status | String | Query | 否 | all | 快照状态。取值范围： progressing：正在创建的快照。 accomplished：创建成功的快照。 failed：创建失败的快照。 all：所有快照状态。 默认值：all。 |  |  |
| SnapshotT ype | String | Query | 否 | all | 快照类型。取值范围： auto：自动快照。 user：手动创建的快照。 all：所有快照类型。 默认值：all。 |  |  |
| Filter.1.Key | String | Query | 否 | CreationStartTime | 查询资源时的筛选键，取值必须为 CreationStartTime 。同时设置 Filter.1.Key 和 Fi lter.1.Value 可以查询在指定时间点后创建的资源信息。 |  |  |
|  |  |  |  |  |  | Fi |  |

|  |  | Filter.1.Key |
|---|---|---|
|  | lter.1.Value |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| Filter.2.Key | String | Query | 否 | CreationEndTime | 查询资源时的筛选键，取值必须为 CreationEndTime 。 同时设置 Filter.2.Key 和 Fi lter.2.Value 可以查询在指定时间点前创建的资源信息。 |  |  |
|  |  |  |  |  |  | Fi |  |
| Filter.1.Val ue | String | Query | 否 | 2022-04-10T17:00Z | 查询资源时的筛选值。指定该参数时必须同时指定 Filter.1.Key 参数， 格式为： yyyy-MM- ddTHH:mmZ ，采用UTC +0时区。 |  |  |
| Filter.2.Val ue | String | Query | 否 | 2022-04-10T22:00Z | 查询资源时的筛选值。指定该参数时必须同时指定 Filter.2.Key 参数， 格式为： yyyy-MM- ddTHH:mmZ ，采用UTC +0时区。 |  |  |
| Usage | String | Query | 否 | none | 快照是否被用作创建镜像或云盘。取值范围： image：使用快照创建了自定义镜像。 disk：使用快照创建了云盘。 image disk：使用快照创 _ 建了数据盘和自定义镜像。 none：暂未使用。 |  |  |
| SourceDisk Type | String | Query | 否 | Data | 快照源云盘的云盘类型。取值范围： System：系统盘。 Data：数据盘。 |  |  |
| Encrypted | Boole an | Query | 否 | false | 是否过滤加密快照。取值范围： true：是。 false：否。 默认值：false。 |  |  |

|  |  | Filter.2.Key |
|---|---|---|
|  | lter.2.Value |  |

|  | ddTHH:mmZ |  |
|---|---|---|

|  | ddTHH:mmZ |  |
|---|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DryRun | Boole an | Query | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会查询资源状况。检查项包括AccessKey是否有效、RAM用户的授权情况和是否填写了必需参数。 如果检查不通过，则返回对应错误。如果检查通过，会返回错误码 DryRunOperation 。 false：发送正常请求，通过检查后返回2XX HTTP状态码并直接查询资源状况。 默认值：false。 |  |  |
| KMSKeyId | String | Query | 否 | 0e478b7a-4262-4802- b8cb-00d3fb40**** | 数据盘对应的KMS密钥ID。 |  |  |
| Category | String | Query | 否 | Standard | 快照类型。取值范围： Standard：普通快照。 Flash：本地快照。 该参数即将被弃用，为提高兼容性，建议您尽量使用其他参数。 |  |  |
| Tag | Repea tList | Query | 否 | / | 标签列表。 |  |  |
| -key | String |  | 否 | null | 快照的标签键。 为提高兼容性，建议您尽量使用 Tag.N.Key 参数。 |  |  |
| -Key | String |  | 否 | TestKey | 快照的标签键。参数格式为 Tag.N.Key ，N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 或 https:/ / 。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| -Value | String |  | 否 | TestValue | 快照的标签值。参数格式为 Tag.N.Value ，N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128个字符，不能包含 http:// 或 https:/ / 。 |  |  |
|  |  |  |  |  |  | https:/ |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -value | String |  | 否 | null | 快照的标签值。 为提高兼容性，建议您尽量使用 Tag.N.Value 参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Snapshots | Array | / | 快照详情集合。 |
| -Tags | Array | / | 标签。 |
| --TagValue | String | TestValue | 快照的标签值。 |
| --TagKey | String | TestKey | 快照的标签键。 |
| -Status | String | accomplished | 快照状态。可能值： progressing：正在创建的快照。 accomplished：创建成功的快照。 failed：创建失败的快照。 |
| -CreationTime | String | 2022-04- 13T13:00:52Z | 创建时间。按照ISO 8601标准表示，并使用UTC +0时间，格式为 yyyy-MM-ddTHH:mm:ssZ 。 |
| -Progress | String | 100 | 快照创建进度，单位为百分比。 |
| -InstantAccess | Boolean | false | 是否开启了快照极速可用功能。可能值： true：开启。仅高性能云盘和普通性能云盘支持开启该功能。 false：关闭。即快照为未开启快照极速可用功能的普通快照。 |
| -Available | Boolean | false | 快照是否可用于创建云盘、回滚云盘、共享快照。 可能值： true：可用。 false：不可用。 |
| -RemainTime | Integer | 38 | 正在创建的快照剩余完成时间，单位：秒。 |
| - SourceDiskSize | String | 2000 | 源云盘容量，单位：GiB。 |
| -RetentionDays | Integer | 30 | 自动快照保留天数。 |

|  | 开发指南·API参考 |  |  | 云服务器EC | S |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| - SourceDiskTyp e | String | Data | 源云盘属性。可能值： System。 Data。 |  |  |
| - SourceStorage Type | String | disk | 原云盘类型。 该参数即将被弃用，为提高兼容性，建议您尽量使用其他参数。 |  |  |
| -Usage | String | none | 快照是否被用作创建镜像或云盘。可能值： image：使用快照创建了自定义镜像。 disk：使用快照创建了云盘。 image disk：使用快照创建了数据盘和自定义 _ 镜像。 none：暂未使用。 |  |  |
| - LastModifiedTi me | String | test | 快照的最后变更时间。按照ISO 8601标准表示，并使用UTC +0时间，格式为 yyyy-MM- ddTHH:mm:ssZ 。 |  |  |
|  |  |  |  | yyyy-MM- |  |
| -Encrypted | Boolean | false | 该快照是否加密。 |  |  |
| -SnapshotType | String | all | 快照类型。可能值： auto：自动快照。 user：手动创建的快照。 all：所有快照类型。 |  |  |
| -SourceDiskId | String | d- bp67acfmxazb4p*** * | 源云盘ID。如果快照的源云盘已经被释放，该字段仍旧保留。 |  |  |
| - SnapshotName | String | test-SnapshotName | 快照显示名称。如果创建时指定了快照显示名称， 则返回。 |  |  |
| - InstantAccessR etentionDays | Integer | 30 | 设置快照极速可用功能的保留时间，保留时间到期后自动关闭快照极速可用功能。 默认与参数 RetentionDays 的值一致。 |  |  |
| -Description | String | FinanceDept | 描述信息。 |  |  |
| -SnapshotId | String | s- bp67acfmxazb4p*** * | 快照ID。 |  |  |
| -RegionId | String | cn-qingdao-env***- d** | 快照所属的地域 ID。 |  |  |

|  | ddTHH:mm:ssZ |
|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ResourceGroup Id | String | rg-123****** | 资源组 ID。 |
| -Category | String | standard | 快照类型。可能值： standard：普通快照。 flash：本地快照。 该参数即将被弃用，为提高兼容性，建议您尽量使用参数 InstantAccess 。 |
| -KMSKeyId | String | 0e478b7a-4262- 4802-b8cb- 00d3fb40**** | 数据盘对应的KMS密钥ID。 |
| -SnapshotSN | String | 64472-116742336- 61976**** | 快照序列号。 |
| - SourceSnapsho tId | String | s- bp67acfmxazb4p*** * | 源快照。 |
| - SourceRegionId | String | cn-********-d01 | 源快照地域。 |
| - SnapshotLinkId | String | sl- bp1grgphbcc9brb5* *** | 快照关联的快照链 ID。 |
| NextToken | String | caeba0bbb2be03f84 eb48b699f0a**** | 下一个查询起始标志。 |
| PageSize | Integer | 10 | 输入时设置的每页行数。 |
| PageNumber | Integer | 1 | 快照列表的页码。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| TotalCount | Integer | 36 | 快照总个数。 |

**示例**

请求示例云服务器ECS

```
https://ecs.example.com/?Action=DescribeSnapshots &RegionId=cn-qingdao-env***-d** &InstanceId=i-bp67acfmxazb4p**** &DiskId=d-bp67acfmxazb4p**** &SnapshotIds=["s-bp67acfmxazb4p****", "s-bp67acfmxazb5p****", … "s-bp67acfmxazb6p****"] &PageNumber=1 &PageSize=10 &SnapshotName=testSnapshotName &Status=all &SnapshotType=all &Usage=none &SourceDiskType=Data &Tag.1.Key=TestKey &Tag.1.Value=TestValue &Encrypted=false &DryRun=false
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "TotalCount": 36,
    "NextToken": "caeba0bbb2be03f84eb48b699f0a****",
    "PageSize": 10,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "PageNumber": 1,
    "Snapshots": {
        "Status": "accomplished",
        "InstantAccess": false,
        "Usage": "none",
        "Progress": 100,
        "Category": "standard",
        "KMSKeyId": "0e478b7a-4262-4802-b8cb-00d3fb40****",
        "Description": "FinanceDept",
        "ProductCode": "jxsc000***",
        "Encrypted": false,
        "RetentionDays": 30,
        "InstantAccessRetentionDays": 30,
        "SnapshotName": "test-SnapshotName",
        "SourceDiskId": "d-bp67acfmxazb4p****",
        "SnapshotSN": "64472-116742336-61976****",
        "SnapshotId": "s-bp67acfmxazb4p****",
        "SourceDiskSize": 2000,
        "LastModifiedTime": "test",
        "CreationTime": "2022-04-13T13:00:52Z",
        "SnapshotType": "all",
        "RemainTime": 38,
        "SourceDiskType": "Data",
        "Tags": {
            "TagKey": "TestKey",
            "TagValue": "TestValue"
        }
    }
}
```

云服务器ECS `XML` 格式

```xml
  <TotalCount>36</TotalCount>
  <NextToken>caeba0bbb2be03f84eb48b699f0a****</NextToken>
  <PageSize>10</PageSize>
  <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
  <PageNumber>1</PageNumber>
  <Snapshots>
        <Status>accomplished</Status>
        <InstantAccess>false</InstantAccess>
        <Usage>none</Usage>
        <Progress>100</Progress>
        <Category>standard</Category>
        <KMSKeyId>0e478b7a-4262-4802-b8cb-00d3fb40****</KMSKeyId>
        <Description>FinanceDept</Description>
        <ProductCode>jxsc000***</ProductCode>
        <Encrypted>false</Encrypted>
        <RetentionDays>30</RetentionDays>
        <InstantAccessRetentionDays>30</InstantAccessRetentionDays>
        <SnapshotName>test-SnapshotName</SnapshotName>
        <SourceDiskId>d-bp67acfmxazb4p****</SourceDiskId>
        <SnapshotSN>64472-116742336-61976**** </SnapshotSN>
        <SnapshotId>s-bp67acfmxazb4p****</SnapshotId>
        <SourceDiskSize>2000</SourceDiskSize>
        <LastModifiedTime>test</LastModifiedTime>
        <CreationTime>2022-04-13T13:00:52Z</CreationTime>
        <SnapshotType>all</SnapshotType>
        <RemainTime>38</RemainTime>
        <SourceDiskType>Data</SourceDiskType>
        <Tags>
              <TagKey>TestKey</TagKey>
              <TagValue>TestValue</TagValue>
        </Tags>
  </Snapshots>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTag.Mismatch | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. |
| 400 | InvalidTagCount | InvalidTagCount | The specified tags are beyond the permitted range. |
| 403 | INSTANCE IDS SIZE _ _ EXCEED LIMIT _ _ | InvalidSnapshotIds.Malformed | The amount of specified specified snapshot Ids exceeds the limit. |
| 403 | Abs.InvalidSnapshot Ids.Malformed | InvalidSnapshotIds.Malformed | The amount of specified specified snapshot Ids exceeds the limit. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Abs.InvalidSnapshot Category.Malformed | InvalidSnapshotCategory.Malfor med | The specified Category is not valid. |
| 404 | Abs.InvalidFilterkey. MalFormed | InvalidFilterKey.NotFound | The specified FilterKey is not found. |
| 404 | Abs.InvalidFilterValu e.MalFormed | InvalidFilterValue | The specified FilterValue exceeds the limit. |
| 404 | Abs.InvalidUsage.Va lueNotSupported | InvalidUsage | The specifed Usage is not valid. |
| 404 | Abs.InvalidDiskType. ValueNotSupported | InvalidSourceDiskType | The specifed SourceDiskType is not valid. |
| 404 | Abs.InvalidStatus.Va lueNotSupported | InvalidStatus.NotFound | The specified Status is not found. |
| 404 | Abs.InvalidSnapshot Type.ValueNotSupp orted | InvalidSnapshotType.NotFound | The specfied SnapshotType is not found. |
| 404 | SNAPSHOT LINK NO _ _ T EXISTS _ | InvalidSnapshotLinkId.NotFound | The specified snapshot link is not found. |
| 500 | -40 | InternalError | The request processing has failed due to some unknown error. |

##### DeleteSnapshot

调用DeleteSnapshot删除指定的快照。如果需要取消正在创建的快照，也可以调用该接口删除快照，即取消创建快照任务。

**接口说明**

调用该接口时，您需要注意： 如果指定的快照ID不存在，请求将被忽略。 如果快照已经被用于创建自定义镜像，则快照不能被删除。您需要先删除已创建的自定义镜像如果快照已经被用于创建云盘，且未设置 `Force` 参数或 `Force=false` 时，不能直接删除快照。如果您确定要删除快照，请设置 `Force=true` 进行强制删除，快照被强制删除后对应的云盘将不能执行重新初始化。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteSnapshot | 系统规定参数。取值：DeleteSnapshot。 |
| SnapshotId | String | 是 | s- bp1btgnlb4licd41 **** | 快照ID。您可以调用DescribeSnapshots查询快照ID。 |

云服务器ECS

| Force | Boolean | 否 | false | 是否强制删除已经被用于创建云盘的快照。 取值范围： true：强制删除。强制删除后该磁盘无法重新初始化。 false：不强制删除。 默认值：false。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。无论调用接口成功与否，都会返回请求 ID。 |

**示例**

请求示例

```
&SnapshotId=s-bp1btgnlb4licd41****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7B****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7B****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | SnapshotCreatedIm age | The snapshot has been used to create user defined image(s). | 如果快照已经被用于创建自定义镜像，将不能执行删除操作。您需要先删除已创建的自定义镜像 （DeleteImage），才能继续删除快照。 |
| 403 | SnapshotCreatedDis k | The snapshot has been used to create disk(s). | 指定的快照已经用于创建云盘，当未设置Force参数或Force参数值为 false时，不能直接删除快照。如果您确定要删除快照，请设置Force参数值为true进行强制删除，快照被强制删除后对应的云盘将不能执行重新初始化。 |

云服务器ECS

| 400 | MissingParameter | The input parameter SnapshotId that is mandatory for processing this request is not supplied. | 参数SnapshotId不得为空。 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 404 | InvalidSnapshotId.N otFound | The specified snapshot is not found | 指定的快照不存在。 |
| 403 | Operation.Conflict | The operation may conflicts with others, please retry later. | 您当前的操作可能与其他人的操作产生了冲突，请稍后重试。 |

##### CopySnapshot

**接口说明**

调用该接口时，您需要注意： 复制后的新快照不能回滚源快照对应的云盘。 不支持复制已加密的快照。 不支持复制本地快照。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | CopySnapshot | 系统必选参数。取值：CopySnapshot。 |
| SnapshotId | String | 是 | s- bp67acfmxazb4p **** | 源快照ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 源快照所在的地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| DestinationRegi onId | String | 是 | cn-beijing-env17- d01 | 新快照的目标地域ID。 |
| DestinationSna pshotName | String | 是 | test- DestinationSnaps hotName | 新快照的名称。长度为2~128个英文或中文字符，必须以大小字母或中文开头，不能以 http://和https:// 开头。可以包含数字、半角冒号（:）、下划线（ ）或者连字符 _ （-）。 默认值：空。 |
| DestinationSna pshotDescriptio n | String | 是 | This is a description example. | 新快照的描述信息。长度为2~256个英文或中文字符，不能以http://和https://开头。 默认值：空。 |

云服务器ECS

| RetentionDays | Integer | 否 | 60 | 新快照的保留时长，单位为天，超过保留时长后快照会被自动释放。取值范围： 1~65536。 默认值：空，表示快照不会被自动释放。 |
|---|---|---|---|---|
| Tag.N.Key | String | 否 | TestKey | 新快照的标签键。一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun和acs:开头，不能包含http://或者 https://。 |
| Tag.N.Value | String | 否 | TestValue | 新快照的标签值。一旦传入该值，允许为空字符串。最多支持128个字符，不能以 aliyun和acs:开头，不能包含http://或者 https://。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | C8B26B44-0189- 443E-9816- D951F59623A9 | 请求ID。 |
| SnapshotId | String | s- bp17441ohwka0yui* *** | 新快照的ID。 |

**示例**

请求示例

```
&DestinationRegionId=cn-beijing-env17-d01 &RegionId=cn-qingdao-env17-d01 &SnapshotId=s-bp67acfmxazb4p****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
            <RequestId>C8B26B44-0189-443E-9816-D951F59623A9</RequestId>
            <SnapshotId>s-bp17441ohwka0yuhi****</SnapshotId>
```

`JSON` 格式

```json
{
        "RequestId": "C8B26B44-0189-443E-9816-D951F59623A9",
        "SnapshotId": "s-bp17441ohwka0yuhi****"
}
```

**错误码**

云服务器ECS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidSnapshotId.N otFound | The specified snapshot is not exists. | 指定的源快照不存在。 |
| 403 | InvalidUser.NotInWh iteList | The user is not in the white list of copying snapshot. | 您暂未授权执行该操作。 |
| 403 | InvalidAccountStatu s.NotEnoughBalance | Your account does not have enough balance. | 账号余额不足，请您先充值再进行该操作。 |
| 403 | InvalidAccountStatu s.SnapshotServiceU navailable | Snapshot service has not been opened yet. | 快照服务未开通，操作无法执行。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键不合法。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值不合法。 |
| 400 | InvalidRegionId.MalF ormed | The specified RegionId is not valid | 指定的 RegionId 不合法。 |

##### DescribeSnapshotLinks

调用DescribeSnapshotLinks查询云盘快照链。快照链是一块云盘所有快照组成的关系链，一块云盘对应一条快照链。 接口说明调用该接口时，您需要注意：

| InstanceId |  | 等 |
|---|---|---|
| 用。当 | DiskIds |  |

滤器有效，但是返回结果为空。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceRegi onId | String | Host | 否 |  | 该参数暂未支持。 |
| Action | String | Query | 是 | DescribeSnapshotLinks | 系统规定参数。取值：DescribeSnapshotL inks 。 |
| OwnerId | Long | Query | 否 |  | 该参数暂未支持。 |
| ResourceO wnerAccou nt | String | Query | 否 |  | 该参数暂未支持。 |

| 云服务器ECS |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerId | Long | Query | 否 |  | 该参数暂未支持。 |
| OwnerAcco unt | String | Query | 否 |  | 该参数暂未支持。 |
| RegionId | String | Query | 是 | cn-qingdao-**** | 云盘所属地域ID。您可以调用 DescribeRegions 查看最新的阿里云地域列表。 |
| InstanceId | String | Query | 否 | i-bp1ahcvgu9z55pk7**** | 实例ID。 |
| DiskIds | String | Query | 否 | ["d- bp198f7xn673w2rw****", "d- bp12te2l9m0170wc****", … "d- bp1btgnlb4lgdzoi****"] | 云盘ID。一次最多指定100个云盘ID。 DiskIds 参数取值格式为JSON数组，ID之间用半角逗号（,）隔开。 |
| SnapshotLi nkIds | String | Query | 否 | ["sl- bp14r3b4xczuenhr****", "sl- bp1eftye2796vi2a****", … "sl- bp1aixnfbjo290a8****"] | 快照链ID。一次最多指定100 个快照 ID。 SnapshotLinkIds 参数取值格式为JSON数组，ID之间用半角逗号（,） 隔开。 |
| PageNumb er | Intege r | Query | 否 | 1 | 云盘状态列表的页码。起始值：1。 默认值：1 。 |
| PageSize | Intege r | Query | 否 | 50 | 分页查询时设置的每页行数。 取值范围：1~100。 默认值：10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SnapshotLinks | Array |  | 快照链信息组成的集合。 |
| -InstantAccess | Boolean |  | 该参数暂未支持。 |
| -TotalSize | Long | 2097152 | 快照链中所有快照的大小，单位为Byte。 |
| - SourceDiskNam e | String | test- SourceDiskName | 源云盘的名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - SourceDiskSize | Integer | 40 | 源云盘容量，单位为GiB。 |
| - SourceDiskTyp e | String | cloud ssd _ | 源云盘的类型。可能值： cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ cloud pperf：高性能云盘。 _ cloud sperf：普通性能云盘。 _ san ssd：共享SSD盘。 _ san efficiency：共享高效云盘。 _ 默认不支持创建共享SSD盘和共享高效云盘。 |
| -InstanceId | String | i- bp1ahcvgu9z55pk7* *** | 实例ID。 |
| - SnapshotLinkId | String | sl- bp14r3b4xczuenhr* *** | 快照链ID。 |
| -TotalCount | Integer | 1 | 快照总个数。 |
| -RegionId | String | cn-qingdao-**** | 快照链源云盘所属地域ID。 |
| -SourceDiskId | String | d- bp198f7xn673w2rw **** | 源云盘ID，如果快照的源云盘已经被删除，该字段仍旧保留。 |
| -InstanceName | String | test-InstanceName | 实例名称。 |
| -Category | String | test | 该参数暂未支持。 |
| PageSize | Integer | 50 | 输入时设置的每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |
| PageNumber | Integer | 1 | 快照链列表的页码。 |
| TotalCount | Integer | 9 | 快照链总个数。 |

**示例**

请求示例云服务器ECS

```
http(s)://ecs.example.com/?Action=DescribeSnapshotLinks &RegionId=cn-qingdao-**** &InstanceId=i-bp1ahcvgu9z55pk7**** &DiskIds=["d-bp198f7xn673w2rw****", "d-bp12te2l9m0170wc****", … "d-bp1btgnlb4lgdzoi****"] &SnapshotLinkIds=["sl-bp14r3b4xczuenhr****", "sl-bp1eftye2796vi2a****", … "slbp1aixnfbjo290a8****"] &PageNumber=1 &PageSize=10
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
    "SnapshotLinks": {
        "SnapshotLink": [
            {
                "SourceDiskSize": 20,
                "TotalSize": 2097152,
                "SourceDiskType": "data",
                "RegionId": "cn-qingdao-****",
                "SnapshotLinkId": "sl-bp14r3b4xczuenhr****",
                "SourceDiskId": "d-bp198f7xn673w2rw****",
                "TotalCount": 1
            },
            {
                "SourceDiskSize": 40,
                "TotalSize": 2097152,
                "SourceDiskType": "data",
                "RegionId": "cn-qingdao-****",
                "SnapshotLinkId": "sl-bp14r3b4xczuenhr****",
                "SourceDiskId": "d-bp198f7xn673w2rw****",
                "TotalCount": 1
            }
```

]

```json
    },
    "PageNumber": 1,
    "PageSize": 2,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
    "TotalCount": 9
}
```

`XML` 格式云服务器ECS

```xml
      <SnapshotLinks>
            <SnapshotLink>
                  <SourceDiskSize>20</SourceDiskSize>
                  <TotalSize>2097152</TotalSize>
                  <SourceDiskType>data</SourceDiskType>
                  <RegionId>cn-qingdao-****</RegionId>
                  <SnapshotLinkId>sl-bp14r3b4xczuenhr****</SnapshotLinkId>
                  <SourceDiskId>d-bp198f7xn673w2rw****</SourceDiskId>
                  <TotalCount>1</TotalCount>
            </SnapshotLink>
            <SnapshotLink>
                  <SourceDiskSize>40</SourceDiskSize>
                  <TotalSize>2097152</TotalSize>
                  <SourceDiskType>data</SourceDiskType>
                  <RegionId>cn-qingdao-****</RegionId>
                  <SnapshotLinkId>sl-bp14r3b4xczuenhr****</SnapshotLinkId>
                  <SourceDiskId>d-bp198f7xn673w2rw****</SourceDiskId>
                  <TotalCount>1</TotalCount>
            </SnapshotLink>
      </SnapshotLinks>
      <PageNumber>1</PageNumber>
      <PageSize>2</PageSize>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
      <TotalCount>9</TotalCount>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ECS NOT EXIST _ _ | InvalidInstanceId.NotFound | The specified instanceId is not exists. |
| 400 | PARAMETER REGIO _ N ID INVALID _ _ | InvalidRegionId | The specified regionId is invalid. |
| 400 | PARAMETER SNAPS _ HOT LINK INVALID _ _ | InvalidSnapshotLinkIds | The specified snapshotLinkIds is invalid. |
| 400 | PARAMETER DISK I _ _ DS INVALID _ | InvalidDiskIds | The specified diskIds is invalid. |
| 500 | -40 | InternalError | The request processing has failed due to some unknown error. |

##### DescribeSnapshotsUsage

调用DescribeSnapshotsUsage查询您在一个地域下的快照数量以及快照容量。 如果您想知道当前地域下每块磁盘的快照使用情况，推荐使用DescribeSnapshotLinks查询快照链。

**请求参数**

云服务器ECS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeSnapsho tsUsage | 系统规定参数。取值： DescribeSnapshotsUsage |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 快照所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| SnapshotCount | Integer | 5 | 当前地域下的快照总数。 |
| SnapshotSize | Long | 122 | 当前地域下已产生的快照容量，单位Byte。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeSnapshotsUsage &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <SnapshotCount>5</SnapshotCount>
   <SnapshotSize>122</SnapshotSize>
      <RequestId>ED5CF6DD-71CA-462C-9C94-A61A78A01479</RequestId>
```

`JSON` 格式

```json
{
 "SnapshotCount": "5",
 "SnapshotSize": "122",
 "RequestId": "ACD9BBB0-A9D1-46D7-9630-B7A69889E110"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidParam.Region Id | The specified region is not exist. | 指定的地域不存在，请检查该参数是否正确。 |

云服务器ECS

##### CreateAutoSnapshotPolicy

**接口说明**

创建的自动快照策略可以应用到任一云盘（ApplyAutoSnapshotPolicy），成功创建的自动快照策略可以后续调用该接口时，您需要注意： 一个阿里云账户在一个地域最多能创建100条自动快照策略。 如果云盘数据较多，单次创建自动快照的时长超过两个时间点间隔，则自动跳过下一时间点。示例：您设置了 09:00、10:00、11:00和12:00为自动快照时间点。由于云盘数据较多，09:00开始创建快照，10:20完成创建快照，实际耗时80分钟。系统会跳过时间点10:00，等到11:00继续为您创建自动快照。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | CreateAutoSnaps hotPolicy | 系统规定参数。取值： CreateAutoSnapshotPolicy |
| regionId | String | 是 | cn-qingdao- env17-d01 | 自动快照策略所属的地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| repeatWeekday s | String | 是 | ["1","2"] | 自动快照的重复日期，单位为天，周期为星期。取值范围：1~7，如1表示周一。 当一星期内需要创建多次自动快照时，可以传入多个时间点： 最多传入7个时间点。 多个时间点用一个格式类似 ["1","2"..."7"] 的JSON数组表示，时间点之间用半角逗号（,）隔开。 |
| retentionDays | Integer | 是 | 30 | 自动快照的保留时间，单位为天。取值范围： -1：永久保存。 1~65535：指定保存天数。 默认值：-1。 |
| timePoints | String | 是 | ["0", "1", … "23"] | 自动快照的创建时间点，单位为小时。取值范围：0~23，代表00:00至23:00共24个时间点，如1表示01:00。 当一天内需要创建多次自动快照时，可以传入多个时间点，最多传入24个时间点。 |

云服务器ECS

| autoSnapshotP olicyName | String | 否 | test- autoSnapshotPoli cyName | 自动快照策略的名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头， 不能以http://和https://开头。可以包含数字、半角冒号（:）、下划线（ ）或者连字 _ 符（-）。 默认值：空。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AutoSnapshotP olicyId | String | sp- bp12m37ccmxvbmi 5**** | 自动快照策略ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=CreateAutoSnapshotPolicy &regionId=cn-qingdao-env17-d01 &repeatWeekdays=["1"] &retentionDays=30 &timePoints=["0", "19"] &autoSnapshotPolicyName=test-autoSnapshotPolicyName
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>F3CD6886-D8D0-4FEE-B93E-1B73239673DE</RequestId>
      <AutoSnapshotPolicyId>sp-bp12m37ccmxvbmi5****</AutoSnapshotPolicyId>
```

`JSON` 格式

```json
{
    "RequestId": "F3CD6886-D8D0-4FEE-B93E-1B73239673DE",
    "AutoSnapshotPolicyId": "sp-bp12m37ccmxvbmi5****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ParameterInvalid | The specified RegionId parameter is invalid. | 指定的地域 ID 无效，请您检查该地域是否正确。 |

云服务器ECS

| 403 | ParameterInvalid | The specified RepeatWeekDays parameter is invalid. | 指定的日期无效，请您检查该日期是否正确。 |
|---|---|---|---|
| 403 | ParameterInvalid | The specified TimePoints parameter is invalid. | 指定的时间点不合法，请您查看该时间点是否填写正确。 |
| 403 | ParameterInvalid | The specified RetentionDays parameter is invalid. | 指定的保持天数不合法。 |
| 403 | AutoSnapshotPolicy. QuotaExceed | The maximum number of automatic snapshot policy has been reached. | 自动快照策略数超出最大值。 |
| 400 | DiskCategory.Opera tionNotSupported | The type of the specified disk does not support creating a snapshot. | 当前磁盘类型不支持此操作 |
| 403 | InvalidAccountStatu s.NotEnoughBalance | Your account does not have enough balance. | 账号余额不足，请您先充值再进行该操作。 |
| 403 | InvalidAccountStatu s.SnapshotServiceU navailable | Snapshot service has not been opened yet. | 快照服务未开通，操作无法执行。 |

##### DeleteAutoSnapshotPolicy

删除一条自动快照策略。如果目标自动快照策略已经被应用到磁盘上，删除自动快照策略后，这些磁盘不再执行该策略。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DeleteAutoSnaps hotPolicy | 系统规定参数。取值： DeleteAutoSnapshotPolicy |
| autoSnapshotP olicyId | String | 是 | sp- bp12m37ccmxvb mi5**** | 自动快照策略的ID。您可以调用 DescribeAutoSnapshotPolicyEx查看您可用的自动快照策略。 |
| regionId | String | 是 | cn-qingdao- env17-d01 | 自动快照所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。无论调用接口成功与否，都会返回请求 ID。 |

**示例**

请求示例云服务器ECS

```
https://ecs.example.com/?Action=DeleteAutoSnapshotPolicy &autoSnapshotPolicyId=sp-bp12m37ccmxvbmi5**** &regionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>F3CD6886-D8D0-4FEE-B93E-1B73239673DE</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"F3CD6886-D8D0-4FEE-B93E-1B73239673DE"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | ParameterInvalid | The specified automatic snapshot policy does not exist. | 指定的自动快照策略不存在，请您检查自动快照策略是否正确。 |
| 404 | ParameterInvalid | The specified automatic snapshot policy does not exist in the region. | 指定的自动快照策略不存在，请您检查自动快照策略是否正确。 |

##### ModifyAutoSnapshotPolicyEx

调用ModifyAutoSnapshotPolicyEx修改一条自动快照策略。修改自动快照策略后，之前已应用该策略的云盘随即执行修改后的自动快照策略。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | ModifyAutoSnaps hotPolicyEx | 系统规定参数。取值： ModifyAutoSnapshotPolicyEx |
| autoSnapshotP olicyId | String | 是 | sp- bp12m37ccmxvb mi5**** | 目标自动快照策略 ID。您可以调用 DescribeAutoSnapshotPolicyEx查看您可用的自动快照策略。 |
| regionId | String | 是 | cn-qingdao- env17-d01 | 自动快照策略所在的地域 ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| autoSnapshotP olicyName | String | 否 | test- autoSnapshotPoli cyName | 自动快照策略的名称。如果参数为空则代表不修改。 |
|---|---|---|---|---|
| timePoints | String | 否 | ["0", "1"] | 自动快照的创建时间点，单位为小时。取值范围：0~23，代表 00:00 至 23:00 共 24 个时间点，如 1 表示 01:00。当一天内需要创建多次自动快照时，可以传入多个时间点： 最多传入 24 个时间点。 多个时间点用一个格式类似 "0", "1", … "23" 的 JSON 数组表示，时间点之间用半角逗号（,）隔开。 |
| repeatWeekday s | String | 否 | ["1", "7"] | 自动快照的重复日期，单位为天，周期为星期。取值范围：1~7，如 1 表示周一。当一星期内需要创建多次自动快照时，可以传入多个时间点： 最多传入 7 个时间点。 多个时间点用一个格式类似 "1", "2", … "7" 的 JSON 数组表示，时间点之间用半角逗号（,）隔开。 |
| retentionDays | Integer | 否 | 30 | 自动快照的保留时间，单位为天。取值范围： -1（默认）：永久保存。 1~65536：指定保存天数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyAutoSnapshotPolicyEx &autoSnapshotPolicyId=sp-bp12m37ccmxvbmi5**** &regionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyAutoSnapshotPolicyResponse>
      <RequestId>F3CD6886-D8D0-4FEE-B93E-1B73239673DE</RequestId>
</ModifyAutoSnapshotPolicyResponse>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId":"F3CD6886-D8D0-4FEE-B93E-1B73239673DE"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | ParameterInvalid | The specified automatic snapshot policy does not exist. | 指定的自动快照策略不存在，请您检查自动快照策略是否正确。 |
| 404 | ParameterInvalid | The specified automatic snapshot policy does not exist in the region. | 指定的自动快照策略不存在，请您检查自动快照策略是否正确。 |
| 403 | ParameterInvalid | The specified RegionId parameter is invalid. | 指定的地域 ID 无效，请您检查该地域是否正确。 |
| 403 | ParameterInvalid | The specified RepeatWeekDays parameter is invalid. | 指定的日期无效，请您检查该日期是否正确。 |
| 403 | ParameterInvalid | The specified TimePoints parameter is invalid. | 指定的时间点不合法，请您查看该时间点是否填写正确。 |
| 403 | ParameterInvalid | The specified AutoSnapshotPolicyId is invalid. | 指定的自动快照规则 ID 不合法。 |
| 403 | ParameterInvalid | The specified RetentionDays parameter is invalid. | 指定的保持天数不合法。 |

##### ModifySnapshotAttribute

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySnapshotA ttribute | 系统规定参数。取值： ModifySnapshotAttribute。 |
| SnapshotId | String | 是 | s- bp199lyny9bb47 pa**** | 快照ID。您可以调用DescribeSnapshots查询快照ID。 |
| SnapshotName | String | 否 | testSnapshotNam e | 快照的显示名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 或 https:// 开头。可以包含数字、半角冒号（:）、下划线（ ）或 _ 者短划线（-）。 为防止和自动快照的名称冲突，不能以auto 开头。 |
| Description | String | 否 | testDescription | 快照的描述。长度为2~256个英文或中文字符，不能以 http:// 或 https:// 开头。 |

云服务器ECS

| DisableInstantAcc ess | Boolean | 否 | false | 是否关闭快照极速可用功能。取值范围： true：关闭快照极速可用。 false：不关闭快照极速可用。 默认值：false。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifySnapshotAttribute &SnapshotId=s-bp199lyny9bb47pa**** &SnapshotName=testSnapshotName &Description=testDescription &DisableInstantAccess=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
            <RequestId>C8B26B44-0189-443E-9816-D951F596****</RequestId>
```

`JSON` 格式

```json
{
 "RequestId":"C8B26B44-0189-443E-9816-D951F596****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDescription.M alformed | The specified description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
| 400 | InvalidSnapshotNam e.Malformed | The specified SnapshotName is wrongly formed. | 快照名称格式不合法。 |
| 400 | NoAttributeToModify | No attribute to be modified in this request. | 没有任何属性被修改。 |
| 404 | InvalidSnapshotId.N otFound | The specified SnapshotId does not exist. | 指定的快照不存在，请您检查快照是否正确。 |

云服务器ECS

##### DescribeAutoSnapshotPolicyEX

调用DescribeAutoSnapshotPolicyEX查询您已创建的自动快照策略。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeAutoSna pshotPolicyEx | 系统规定参数。取值： DescribeAutoSnapshotPolicyEx |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 要查询的自动快照策略所在的地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| AutoSnapshotP olicyId | String | 否 | sp- bp67acfmxazb4p **** | 自动快照策略ID。 |
| PageNumber | Integer | 否 | 1 | 自动快照策略返回结果分多页展示。 起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 1 | 分页展示返回的自动快照策略时的每页行数。 最大值：100。 默认值：10。 |
| Tag.N.Key | String | 否 | TestKey | 快照的标签键。N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 128个字符，不能以aliyun和acs:开头，不能包含http://或者https://。 |
| Tag.N.Value | String | 否 | TestValue | 快照的标签值。N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128 个字符，不能以acs:开头，不能包含http:// 或者https://。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AutoSnapshotP olicies | Array |  | 自动快照策略详情AutoSnapshotPolicy组成的集合。 |
| AutoSnapshotP olicy |  |  |  |
| AutoSnapshotP olicyId | String | sp- bp67acfmxazb4p*** * | 自动快照策略ID。 |

云服务器ECS

| AutoSnapshotP olicyName | String | test- AutoSnapshotPolicy Name | 自动快照策略的名称。 |  |  |
|---|---|---|---|---|---|
| CopiedSnapsho tsRetentionDay s | Integer | 0 | 说明该参数暂未支持。 |  |  |
| CreationTime | String | 2014-04- 21T12:08:52Z | 创建时间。按照ISO8601标准表示，并需要使用 UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。 |  |  |
| DiskNums | Integer | 1 | 启用该策略的云盘数量。 |  |  |
| EnableCrossRe gionCopy | Boolean | false | 说明该参数暂未支持。 |  |  |
| RegionId | String | cn-qingdao-env17- d01 | 自动快照策略所属的地域ID。 |  |  |
| RepeatWeekda ys | String | ["6"] | 指定自动快照的重复日期。选定周一到周日中需要创建快照的日期，参数为1~7的数字，如1表示周一。允许选择多个日期。 |  |  |
| RetentionDays | Integer | 30 | 指定自动快照的保留时间，单位为天。可能值： -1：永久保存 1~65536：指定保存天数 |  |  |
| Status | String | Normal | 自动快照策略状态。可能值： Normal Expire |  |  |
| Tags | Array |  | 快照的标签键值集合。 |  |  |
| Tag |  |  |  |  |  |
| TagKey | String | TestKey | 快照标签键。 |  |  |
| TagValue | String | TestValue | 快照标签值。 |  |  |
| TargetCopyReg ions | String | test | 说明该参数暂未支持。 |  |  |
| TimePoints | String | ["4", "19"] | 指定自动快照的创建时间点。 最小单位为小时，从00:00~23:00共24个时间点可选，参数为0~23的数字，如：1代表在01:00时间点。可以选定多个时间点。 传递参数为一个带有格式的Json Array： "0", "1", ... "23" ，最多24个时间点，用半角逗号字符（,）隔开。 |  |  |
|  |  |  |  | "0", |  |

|  | "1", ... "23" |
|---|---|

云服务器ECS

| VolumeNums | Integer | 2 | 启用该策略的拓展卷数量。 |
|---|---|---|---|
| PageNumber | Integer | 1 | 自动快照策略列表的页码。 |
| PageSize | Integer | 1 | 分页展示返回的自动快照策略时的每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 2 | 自动快照策略的总个数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeAutoSnapshotPolicyEx &RegionId=cn-qingdao-env17-d01 &AutoSnapshotPolicyId=sp-bp67acfmxazb4p**** &PageNumber=1 &PageSize=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
<DescribeAutoSnapshotPolicyResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>2</TotalCount>
      <AutoSnapshotPolicies>
            <AutoSnapshotPolicy>
                  <CreationTime>2019-01-22 11:38:08</CreationTime>
                  <Status>Normal</Status>
                  <DiskNums>1</DiskNums>
                  <AutoSnapshotPolicyName>test-
AutoSnapshotPolicyName</AutoSnapshotPolicyName>
                  <RegionId>cn-qingdao-env17-d01</RegionId>
                  <VolumeNums>2</VolumeNums>
                  <RetentionDays>30</RetentionDays>
                  <TimePoints>["0"]</TimePoints>
                  <AutoSnapshotPolicyId>sp-bp67acfmxazb4p****</AutoSnapshotPolicyId>
                  <RepeatWeekdays>["7"]</RepeatWeekdays>
                  <Tags>
                        <Tag>
                              <TagKey>Test</TagKey>
                              <TagValue>Test</TagValue>
                        </Tag>
                  </Tags>
            </AutoSnapshotPolicy>
      </AutoSnapshotPolicies>
      <PageSize>1</PageSize>
      <RequestId>CC323EDF-BBB7-420F-BCD1-D9B9D2E9D424</RequestId>
</DescribeAutoSnapshotPolicyResponse>
```

`JSON` 格式云服务器ECS

```json
{
 "PageNumber": 1,
 "TotalCount": 2,
 "AutoSnapshotPolicies": {
  "AutoSnapshotPolicy": [
   {
    "CreationTime": "2019-01-22 11:38:08",
    "Status": "Normal",
    "DiskNums": 1,
    "AutoSnapshotPolicyName": "test-AutoSnapshotPolicyName",
    "RegionId": "cn-qingdao-env17-d01",
    "VolumeNums": 2,
    "RetentionDays": 30,
    "TimePoints": "[\"0\"]",
    "AutoSnapshotPolicyId": "sp-bp67acfmxazb4p****",
    "RepeatWeekdays": "[\"7\"]",
                "Tags": {
     "Tag": [
      {
       "TagKey": "Test",
       "TagValue": "Test"
      }
```

]

```
    }
   }
```

]

```json
 },
 "PageSize": 1,
 "RequestId": "CC323EDF-BBB7-420F-BCD1-D9B9D2E9D424"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 400 | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. | 指定的Tag.n.Key和Tag.n.Value不匹配。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |

##### ApplyAutoSnapshotPolicy

调用ApplyAutoSnapshotPolicy为一块或者多块云盘应用自动快照策略。目标云盘已经应用了自动快照策略时，调用ApplyAutoSnapshotPolicy可以更换云盘当前应用的自动快照策略。

**接口说明**

一块云盘只能应用一条自动快照策略。 一条自动快照策略能应用到多块云盘。

**请求参数**

云服务器ECS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ApplyAutoSnapsh otPolicy | 系统规定参数。取值： ApplyAutoSnapshotPolicy |
| regionId | String | 是 | cn-qingdao-****- d01 | 自动快照策略和云盘所在的地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| autoSnapshotPoli cyId | String | 是 | sp- bp12m37ccmxvb mi5**** | 目标自动快照策略ID。 |
| diskIds | String | 是 | ["d- bp198f7xn673w2 rw****", "d- bp12te2l9m0170 wc****", "d- bp1btgnlb4lgdzoi ****"] | 一块或多块云盘的ID。取值是JSON数组格式，云盘ID之间用半角逗号（,）隔开。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ApplyAutoSnapshotPolicy &autoSnapshotPolicyId=sp-bp12m37ccmxvbmi5**** &diskIds=["d-bp198f7xn673w2rw****", "d-bp12te2l9m0170wc****", "d-bp1btgnlb4lgdzoi****"] &regionId=cn-qingdao-****-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云服务器ECS

| 404 | ParameterInvalid | The specified automatic snapshot policy does not exist. | 指定的自动快照策略不存在，请您检查自动快照策略是否正确。 |
|---|---|---|---|
| 404 | ParameterInvalid | The specified automatic snapshot policy does not exist in the region. | 指定的自动快照策略不存在，请您检查自动快照策略是否正确。 |
| 404 | InvalidDiskId.NotFou nd | The specified disk does not exist in the region. | 当前地域不存在指定的磁盘。 |
| 403 | ParameterInvalid | The specified RegionId parameter is invalid. | 指定的地域ID无效，请您检查该地域是否正确。 |
| 403 | ParameterInvalid | The specified AutoSnapshotPolicyId parameter is invalid. | 指定的参数自动快照ID不合法。 |
| 403 | ParameterInvalid | The specified DiskIds are invalid. | 指定的磁盘ID不合法，请您检查磁盘 ID是否存在。 |
| 400 | DiskCategory.Opera tionNotSupported | The type of the specified disk does not support creating a snapshot. | 当前磁盘类型不支持此操作。 |
| 400 | PartofDiskCategory. OperationNotSuppor ted | The types of some disks in the disk list do not support creating snapshots. | 部分指定的磁盘不支持此操作。 |
| 403 | InvalidAccountStatu s.NotEnoughBalance | Your account does not have enough balance. | 账号余额不足，请您先充值再进行该操作。 |
| 403 | InvalidAccountStatu s.SnapshotServiceU navailable | Snapshot service has not been opened yet. | 快照服务未开通，操作无法执行。 |

##### CancelAutoSnapshotPolicy

调用CancelAutoSnapshotPolicy取消一块或者多块云盘的自动快照策略。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CancelAutoSnaps hotPolicy | 系统规定参数，取值： CancelAutoSnapshotPolicy。 |
| diskIds | String | 是 | ["d- bp198f7xn673w2 rw****", "d- bp12te2l9m0170 wc****", "d- bp1btgnlb4lgdzoi ****"] | 目标云盘ID。当您需要取消多块云盘的自动快照策略时，多块云盘ID用一个格式类似 "d-xxxxxxxxx", "d-yyyyyyyyy", … "d- zzzzzzzzz" 的JSON数组表示，云盘ID之间用半角逗号（,）隔开。 |
| regionId | String | 是 | cn-qingdao- env17-d01 | 自动快照策略和云盘所在的地域 ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

云服务器ECS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。无论调用接口成功与否，都会返回请求 ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=CancelAutoSnapshotPolicy &diskIds=["d-bp198f7xn673w2rw****", "d-bp12te2l9m0170wc****", "d-bp1btgnlb4lgdzoi****"] &regionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>F3CD6886-D8D0-4FEE-B93E-1B73239673DE</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"F3CD6886-D8D0-4FEE-B93E-1B73239673DE"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ParameterInvalid | The specified RegionId parameter is invalid. | 指定的地域ID无效，请您检查该地域是否正确。 |
| 403 | ParameterInvalid | The specified DiskIds are invalid. | 指定的磁盘ID不合法，请您检查磁盘 ID是否存在。 |
| 404 | InvalidDiskId.NotFou nd | The specified DiskIds are not found. | 指定的参数DiskIds不存在。 |

##### CreateSnapshotGroup

调用CreateSnapshotGroup为指定ECS实例中的云盘创建快照一致性组。快照一致性组包含一个或多个云盘对应的快照。

**接口说明**

创建快照一致性组时，请注意：

| 于运行中（ | Running |
|---|---|
| Running | ）的状态， |

止（ `Stopped` ）。 如果云盘处于**待挂载**（ `Available` ）的状态，则需要保证云盘有过挂载到ECS实例的历史操作。从未挂载过ECS实例的云盘不支持创建快照。 云服务器ECS 目前快照一致性组只支持高性能云盘和普通性能云盘。 单个快照一致性组最多包括16块云盘（包括系统盘和数据盘），且总容量不超过32 TiB。 您自行创建的快照会一直保留，请定期删除不再需要的快照，避免快照数量超过配额限制。 开启多重挂载特性的云盘不支持创建快照一致性组。如果实例挂载了开启多重挂载特性的云盘，您需要设置 `ExcludeDiskId.N` 参数排除该云盘。 关于快照一致性组的功能信息，请参见云服务器ECS用户指南中的创建快照一致性组章节。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateSnapshotG roup | 系统规定参数。取值： CreateSnapshotGroup。 |
| InstanceId | String | 是 | i- q1a01ac6ae3gcb 11**** | 实例ID。 |
| RegionId | String | 是 | cn-qingdao-**** | 实例所属的地域ID。您可以调用 DescribeRegions查看地域列表。 具体操作，请参见云服务器ECS开发指南中的DescribeRegions章节。 |
| ExcludeDiskId.N | RepeatLi st | 否 | d- q1a0113yyonhqb gu**** | 实例中不需要创建快照的云盘ID。指定云盘 ID后，创建的快照一致性组将不包含该云盘对应的快照。N的取值范围为1~16。 默认值：空，表示为实例中的所有云盘创建快照。 |
| InstantAccess | Boolean | 否 | false | 是否开启快照极速可用。取值范围： true：开启。 false：关闭。 默认值为false。 |
| InstantAccessRet entionDays | Integer | 否 | 1 | 设置快照极速可用的使用时间。单位：天， 取值范围：1~65535。 仅当 InstantAccess=true 时，该参数生效。到期后自动关闭快照极速可用功能。 默认值：空，表示和快照释放时间一致。 |
| Name | String | 否 | testName | 快照一致性组名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 或 https:// 开头，可以包含数字、半角句号（.）、下划线（ ）、 _ 短划线（-）或者半角冒号（:）。 |
| Description | String | 否 | This is description. | 快照一致性组描述。长度为2～256个字符， 不能以 http:// 或 https:// 开头。 |

**返回数据**

云服务器ECS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | ssg- j6ciyh3k52qp7ovm* *** | 快照一致性组ID。 |
| SnapshotGroup Id | String | 01ABBD93-1ABB- 4D92-B496- 1A3D20EC**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=CreateSnapshotGroup &InstanceId=i-q1a01ac6ae3gcb11**** &RegionId=cn-qingdao-****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <RequestId>ssg-j6ciyh3k52qp7ovm**** </RequestId>
  <SnapshotGroupId>01ABBD93-1ABB-4D92-B496-1A3D20EC****</SnapshotGroupId>
```

`JSON` 格式

```json
{
    "RequestId": "ssg-j6ciyh3k52qp7ovm****",
    "SnapshotGroupId": "01ABBD93-1ABB-4D92-B496-1A3D20EC****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDiskId.NotFou nd | The specified DiskId does not exist. | 指定的磁盘不存在。请您检查磁盘ID 是否正确。 |
| 400 | InvalidSnapshotNam e.Malformed | The specified SnapshotName is wrongly formed. | 快照名称格式不合法。 |
| 404 | InvalidDescription.M alformed | The specified description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
| 400 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | IncorrectDiskStatus. CreatingSnapshot | A previous snapshot creation is in process. | 当前磁盘有创建中的快照，请您等待创建完成再试。 |
| 403 | InstanceLockedForS ecurity | The disk attached instance is locked due to security. | 磁盘挂载的实例因安全原因被锁定。 |

云服务器ECS

| 403 | IncorrectDiskStatus. NeverAttached | The specified disk has never been attached to any instance. | 可卸载的云磁盘创建后未被挂载，内容没有变化。 |
|---|---|---|---|
| 403 | QuotaExceed.Snaps hot | The snapshot quota exceeds. | 快照额度超过限制，若要存储新快照，在不影响业务的情况下，请您删除已有的老快照。 |
| 403 | IncorrectDiskStatus. NeverUsed | The specified disk has never been used after creating. | 磁盘创建后未被使用，内容没有变化。 |
| 403 | CreateSnapshot.Fail ed | The process of creating snapshot is failed. | 创建快照失败。 |
| 403 | DiskInArrears | The specified operation is denied as your disk has expired. | 磁盘欠费过期。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | DiskId.ValueNotSup ported | The specified parameter diskid is not supported. | 指定的块存储类型不支持此操作。 |
| 400 | DiskCategory.Opera tionNotSupported | The operation is not supported to the specified disk due to its disk category | 由于磁盘种类限制，指定的磁盘不支持该操作。 |
| 403 | IncorrectDiskStatus | The current disk status does not support this operation. | 当前的磁盘不支持此操作，请您确认磁盘处于正常使用状态，是否欠费。 |
| 403 | InvalidAccountStatu s.NotEnoughBalance | Your account does not have enough balance. | 账号余额不足，请您先充值再进行该操作。 |
| 403 | InvalidAccountStatu s.SnapshotServiceU navailable | Snapshot service has not been opened yet. | 快照服务未开通，操作无法执行。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | IncorrectVolumeStat us | The current volume status does not support this operation. | 共享块存储状态不支持当前操作。 |
| 404 | InvalidVolumeId.Not Found | The specified volume does not exist. | 指定的共享块存储不存在，请您检查共享块存储是否正确。 |
| 403 | IdempotentParamet erMismatch | The specified clientToken is used. | 指定的客户令牌已经被使用。 |
| 403 | IncorrectDiskType.N otSupport | The specified device type is not supported. | 指定磁盘存储类型不支持此操作。 |
| 403 | IncorrectDiskStatus. Transferring | The specified device is transferring, you can retry after the process is finished. | 指定磁盘正在迁移中，请在迁移完毕后重试。 |
| 403 | InvalidParameter.K MSKeyId.CMKNotEn abled | The CMK needs to be enabled. | 加密云盘设置了KMSKeyId后，CMK 必须处于启用状态。您可以调用密钥管理服务的DescribeKey接口查询指定CMK的相关信息。 |
| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |

云服务器ECS

| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
|---|---|---|---|
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 403 | IdempotentProcessi ng | The previous idempotent request(s) is still processing. | 先前的幂等请求仍在处理中，请稍后重试。 |
| 400 | InvalidRetentionDay s.Malformed | The specified RetentionDays is not valid. | 指定的保留天数无效。请检查 RetentionDays参数值是否正确。 |
| 403 | QuotaExceed.Tags | %s | 标签数超过可以配置的最大数量。%s 为变量，将根据调用API的实际情况动态返回错误信息。 |
| 403 | InvalidSnapshotCate gory.Malformed | The specified Category is not valid. | 指定的快照类型无效。请检查 Category参数值是否正确。 |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域ID不存在。 |
| 400 | InvalidParameter.Na me | The specified Name is invalid. | 指定的Name参数无效。 |
| 403 | NumberExceed.Too ManyDisks | The number of all disks in the request exceeds. | 请求中云盘的数量超过限制。 |

##### DescribeSnapshotGroups

调用DescribeSnapshotGroups查询一个或多个快照一致性组的信息。

**接口说明**

`InstanceId` 、 `SnapshotGroupId.N` 和 `Status.N` 不是必需的请求参数，但是可以构建过滤器逻辑，参数之间为逻辑与（And）关系。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSnapsho tGroups | 系统规定参数。取值： DescribeSnapshotGroups。 |
| RegionId | String | 是 | cn-qingdao-**** | 实例所属的地域ID。您可以调用 DescribeRegions查看地域列表。 具体操作，请参见云服务器ECS开发指南中的DescribeRegions章节。 |
| InstanceId | String | 否 | i- q1a01ac6ae3gcb 11**** | 实例ID。您可以调用DescribeInstances查询实例ID。 |

云服务器ECS

| SnapshotGroupId. N | RepeatLi st | 否 | ssg- j6ciyh3k52qp7ov m**** | 指定的快照一致性组ID。N的取值范围为 1~10。 |
|---|---|---|---|---|
| Status.N | RepeatLi st | 否 | accomplished | 快照一致性组的状态。N的取值范围： 1~3。取值如下： progressing：创建中。 accomplished：创建成功。 failed：创建失败。 |
| Name | String | 否 | testName | 快照一致性组的名称。 |
| AdditionalAttribut es.N | RepeatLi st | 否 | META OPTIONS _ | 其他属性值。N的取值范围为1~20。取值范围： META OPTIONS：实例元数据。 _ DDH CLUSTER：专有宿主机集群。 _ NETWORK PRIMARY ENI IP：主网卡 _ _ _ 辅助IP。 |
| NextToken | String | 否 | caeba0bbb2be03 f84eb48b699f0a4 883 | 查询凭证（Token），取值为上一次API调用返回的NextToken参数值。 |
| MaxResults | Integer | 否 | 10 | 分页查询时每页行数。 最大值为100。 默认值为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f84 eb48b699f0a4883 | 下一个查询起始标志。 说明该返回值为空时，表示无更多返回的数据信息 |
| RequestId | String | 3F9A4CC4-362F- 469A-B9EF- B3204EF8AA3A | 请求ID。 |
| SnapshotGroup s | Array of SnapshotGroup |  | 快照一致性组的信息组成的数组。 |
| SnapshotGroup |  |  |  |
| CreationTime | String | 2021-03- 23T10:58:48Z | 快照一致性组创建时间。 |
| Description | String | This is description. | 快照一致性组描述。 |

云服务器ECS

| InstanceId | String | i- q1a01ac6ae3gcb11 **** | 快照一致性组所属的实例ID。 该参数仅当快照一致性组内的所有云盘快照属于同一实例时有返回值。 |
|---|---|---|---|
| Name | String | testName | 快照一致性组的名称。 |
| ProgressStatus | String | null | 说明该参数暂未开放使用。 |
| SnapshotGroup Id | String | ssg- j6ciyh3k52qp7ovm* *** | 快照一致性组ID。 |
| Snapshots | Array of Snapshot |  | 快照一致性组中包含的快照信息组成的数组。 |
| Snapshot |  |  |  |
| InstantAccess | Boolean | true | 是否开启了快照极速可用功能。可能值： true：开启。仅高性能云盘和普通性能云盘支持开启该功能。 false：关闭。即快照为未开启快照极速可用功能的普通快照。 |
| InstantAccessR etentionDays | Integer | 1 | 快照极速可用功能的保留时间，保留时间到期后快照将自动释放。 |
| Progress | String | 100% | 快照创建进度，单位为百分比。 |
| SnapshotId | String | s- j6cbzmrlbf09w72q** ** | 快照ID。 |
| SourceDiskId | String | d- j6c3ogynmvpi6wy7* *** | 源云盘ID。如果快照的源云盘已经被释放，该字段仍旧保留。 |
| SourceDiskTyp e | String | system | 源云盘类型。可能值： system：系统盘 data：数据盘 |
| Status | String | accomplished | 快照一致性组的状态。可能值： progressing：创建中。 accomplished：创建成功。 failed：创建失败。 |

**示例**

请求示例云服务器ECS

```
http(s)://ecs.example.com/?Action=DescribeSnapshotGroups &RegionId=cn-qingdao-**** &SnapshotGroupId.1=ssg-j6ciyh3k52qp7ovm****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <NextToken>caeba0bbb2be03f84eb48b699f0a4883</NextToken>
  <RequestId>3F9A4CC4-362F-469A-B9EF-B3204EF8AA3A </RequestId>
  <SnapshotGroups>
        <Status>accomplished</Status>
        <ProgressStatus>null</ProgressStatus>
        <Description>This is description. </Description>
        <InstanceId>i-q1a01ac6ae3gcb11****</InstanceId>
        <CreationTime>2021-03-23T10:58:48Z </CreationTime>
        <SnapshotGroupId>ssg-j6ciyh3k52qp7ovm**** </SnapshotGroupId>
        <Name>testName </Name>
        <Snapshots>
              <InstantAccess>true</InstantAccess>
              <SnapshotId>s-j6cbzmrlbf09w72q**** </SnapshotId>
              <Progress>100% </Progress>
              <SourceDiskType>system</SourceDiskType>
              <InstantAccessRetentionDays>1</InstantAccessRetentionDays>
              <SourceDiskId>d-j6c3ogynmvpi6wy7**** </SourceDiskId>
        </Snapshots>
  </SnapshotGroups>
```

`JSON` 格式

```json
{
    "NextToken": "caeba0bbb2be03f84eb48b699f0a4883",
    "RequestId": "3F9A4CC4-362F-469A-B9EF-B3204EF8AA3A",
    "SnapshotGroups": {
        "Status": "accomplished",
        "ProgressStatus": "null",
        "Description": "This is description.",
        "InstanceId": "i-q1a01ac6ae3gcb11****",
        "CreationTime": "2021-03-23T10:58:48Z",
        "SnapshotGroupId": "ssg-j6ciyh3k52qp7ovm****",
        "Name": "testName",
        "Snapshots": {
            "InstantAccess": true,
            "SnapshotId": "s-j6cbzmrlbf09w72q****",
            "Progress": "100%",
            "SourceDiskType": "system",
            "InstantAccessRetentionDays": 1,
            "SourceDiskId": "d-j6c3ogynmvpi6wy7****"
        }
    }
}
```

云服务器ECS

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidStatus.ValueN otSupported | %s | 该资源当前的状态不支持此操作。 |

##### DeleteSnapshotGroup

**接口说明**

如果快照一致性组中的云盘快照已经用于创建自定义镜像，则实例快照删除时相关的云盘快照不会被删除。您如果需要删除相关的云盘快照，请先删除已创建的自定义镜像（DeleteImage），再删除相关的云盘快照

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteSnapshotG roup | 系统规定参数。取值： DeleteSnapshotGroup。 |
| RegionId | String | 是 | cn-qingdao-**** | 快照一致性组所属的地域ID。您可以调用 DescribeRegions查看地域列表。 |
| SnapshotGroupId | String | 是 | ssg- j6ciyh3k52qp7ov m**** | 快照一致性组ID。您可以调用 DescribeSnapshotGroups查询快照一致性组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| OperationProgr essSet | Array of OperationProgr ess |  | 删除实例快照时操作状态信息合集。 |
| OperationProgr ess |  |  |  |
| ErrorCode | String | 400 | 错误码。删除成功时返回空值。 |
| ErrorMsg | String | testErrorMsg | 错误信息。删除成功时返回空值。 |
| OperationStatu s | String | Success | 操作是否成功。成功返回Success，失败返回 ErrorCode和ErrorMsg信息。 |
| RelatedItemSet | Array of RelatedItem |  | 资源信息。 |
| RelatedItem |  |  |  |

云服务器ECS

| Name | String | SnapshotId | 资源名称。 |
|---|---|---|---|
| Value | String | s- j6c9lpuyxo2uxxnx** ** | 资源ID。 |
| RequestId | String | 6EDE885A-FDC1- 4FAE-BC44- 6EACAEA6**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DeleteSnapshotGroup &RegionId=cn-qingdao-**** &SnapshotGroupId=ssg-j6ciyh3k52qp7ovm****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <RequestId>6EDE885A-FDC1-4FAE-BC44-6EACAEA6****</RequestId>
  <OperationProgressSet>
        <OperationStatus>Success</OperationStatus>
        <ErrorMsg>testErrorMsg</ErrorMsg>
        <ErrorCode>400 </ErrorCode>
        <RelatedItemSet>
              <Value></Value>
              <Name></Name>
        </RelatedItemSet>
  </OperationProgressSet>
```

`JSON` 格式

```json
{
    "RequestId": "6EDE885A-FDC1-4FAE-BC44-6EACAEA6****",
    "OperationProgressSet": {
        "OperationStatus": "Success",
        "ErrorMsg": "testErrorMsg",
        "ErrorCode": 400,
        "RelatedItemSet": {
            "Value": "",
            "Name": ""
        }
    }
}
```

##### ModifySnapshotGroup

云服务器ECS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySnapshotG roup | 系统规定参数。取值： ModifySnapshotGroup。 |
| RegionId | String | 是 | cn-qingdao-**** | 实例快照所属的地域ID。您可以调用 DescribeRegions查看地域列表。 具体操作，请参见云服务器ECS开发指南中的DescribeRegions章节。 |
| SnapshotGroupId | String | 是 | ssg- j6ciyh3k52qp7ov m**** | 快照一致性组ID。您可以调用 DescribeSnapshotGroups查询快照一致性组ID。 |
| Name | String | 否 | testName02 | 修改后的实例快照名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 和 https:// 开头，可以包含数字、半角句号（.）、下划线 （ ）、短划线（-）或者半角冒号（:）。 _ |
| Description | String | 否 | This is new description | 修改后的快照一致性组描述。长度为2~256 个英文或中文字符，不能以http://和https:// 开头。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A00B5E55-76B7- 42C8-8A80- AF10E980**** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=ModifySnapshotGroup &RegionId=cn-qingdao-**** &SnapshotGroupId=ssg-j6ciyh3k52qp7ovm****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <RequestId>A00B5E55-76B7-42C8-8A80-AF10E980****</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "A00B5E55-76B7-42C8-8A80-AF10E980****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter.Na me | The specified Name is invalid. | 指定的Name参数无效。 |

#### 镜像

##### CreateImage

调用CreateImage创建一份自定义镜像。您可以使用创建的自定义镜像创建ECS实例（RunInstances），或者接口说明调用该接口时，您需要注意： 等待镜像状态变为可用（ `Available` ）后才能使用镜像资源。 查询ECS实例信息时，如果返回数据中包含 `{"OperationLocks": {"LockReason" : "security"}}` ，则禁止一切操作。 以下描述了三种通过该接口创建自定义镜像的方法。请求参数的优先级为： `InstanceId` > `DiskDeviceMapping` > `SnapshotId` ，若您的请求中同时含有两个及以上参数，默认以优先级更高的参数为准创建镜像。 ：使用一台实例做模板，只需要指定实例ID（ `InstanceId` ）。该台实例的状态必须为运行中

**方法一**

（ `Running` ）或者已停止（ `Stopped` ）。接口调用成功后，该台实例的每块云盘均会新增一份快照。由于运行中的实例存在缓存数据未落盘的情况，可能导致创建的自定义镜像数据与实例数据不完全一致。因此阿

**方法二**

：针对某一台实例的系统盘创建自定义镜像，只需要指定实例系统盘的一份历史快照 ID（ `SnapshotId` ）。 ：将多份快照组合成一个镜像模板，需要建立几块云盘的数据关联（ `DiskDeviceMapping` ）。

**方法三**

使用**方法三** 创建自定义镜像时，请注意： 只能指定一个系统盘快照，系统盘的设备名必须为/dev/xvda。 可以指定多个数据盘快照，数据盘设备名默认由系统有序分配，从/dev/xvdb依次排序到/dev/xvdz，不能重复。 可以不指定 `SnapshotId` ，不指定时会创建一个指定大小的没有任何数据的空数据盘。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceRegi onId | String | Host | 否 | - | 鉴权相关的系统参数，不填。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| Action | String | Query | 是 | CreateImage | 系统规定参数。取值： CreateImage |  |  |
| OwnerId | Long | Query | 否 | - | 鉴权相关的系统参数，不填。 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 | - | 鉴权相关的系统参数，不填。 |  |  |
| ResourceO wnerId | Long | Query | 否 | - | 鉴权相关的系统参数，不填。 |  |  |
| RegionId | String | Query | 是 | cn-qingdao-env***-d** | 镜像所在的地域ID。您可以调用 DescribeRegions 查看最新的阿里云地域列表。 |  |  |
| SnapshotId | String | Query | 否 | s-bp17441ohwkdca0**** | 根据指定的快照创建自定义镜像。 |  |  |
| InstanceId | String | Query | 否 | i-bp1g6zv0ce8oghu7**** | 实例ID。 |  |  |
| ImageNam e | String | Query | 否 | TestCentOS | 镜像名称。长度为2~128个字符，支持Unicode中letter 分类下的字符（其中包括英文、中文和数字等）。可以包含半角冒号（:）、下划线 （ ）、半角句号（.）或者短 _ 划线（-）。 默认值：空。 |  |  |
| ImageFami ly | String | Query | 否 | daily-update | 镜像族系名称。长度为 2~128个字符。必须以大小字母或中文开头，不能以 aliyun或acs:开头，不能包含 http:// 或者 https:// 。可以包含数字、半角句号（.）、半角冒号（:）、下划线（ ）或者 _ 短划线（-）。 |  |  |
| ImageVersi on | String | Query | 否 | 2017011017 | 镜像版本。 |  |  |
| Descriptio n | String | Query | 否 | ImageTestDescription | 镜像的描述信息。长度为 2~256个英文或中文字符， 不能以 http:// 或 https:/ / 开头。 默认值：空。 |  |  |
|  |  |  |  |  |  | https:/ |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Platform | String | Query | 否 | CentOS | 指定数据盘快照做镜像的系统盘后，需要通过Platform确定系统盘的操作系统发行版。 取值范围： CentOS Ubuntu SUSE OpenSUSE RedHat Kylin UOS Anolis Debian CoreOS Aliyun Linux Windows Server 2012 Windows Server 2016 Windows Server 2019 Windows Server 2022 Customized Linux Others Linux 默认值：Others Linux。 |
| BootMode | String | Query | 否 | BIOS | 修改镜像的启动模式。取值范围： BIOS：BIOS启动模式。 UEFI：UEFI启动模式。 您需要了解指定的镜像支持的启动模式，当通过该参数修改启动模式后，必须与镜像本身支持的启动模式匹配，实例才能正常启动。 |
| Architectur e | String | Query | 否 | x86 64 _ | 指定数据盘快照做镜像的系统盘后，需要通过 Architecture 确定系统盘的系统架构。取值范围： i386。 x86 64。 _ arm64。 默认值：x86 64。 _ |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 |  | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多详情，请参见专有云文档中心《云服务器ECS开发指南》中的如何保证幂等性章节。 |  |  |
| OwnerAcco unt | String | Query | 否 | - |  | 鉴权相关的系统参数，不填。 |  |  |
| ResourceG roupId | String | Query | 否 | rg-bp67acfmxazb4p**** |  | 自定义镜像所在的资源组 ID。如果不设置该参数值，创建的镜像属于默认资源组。 |  |  |
| DetectionS trategy | String | Query | 否 | Standard |  | 镜像检测策略，不配置此参数时不触发检测。仅支持标准 （Standard）检测模式。 |  |  |
| DiskDevice Mapping | Repea tList | Query | 否 | / |  | 创建的自定义镜像信息列表。 |  |  |
| - SnapshotId | String |  | 否 | s-bp17441ohwkdca0**** |  | 根据指定的快照创建自定义镜像。参数格式为 DiskDeviceMapping.N .SnapshotId 。 |  |  |
|  |  |  |  |  |  |  | DiskDeviceMapping.N |  |
|  |  |  |  |  |  | .SnapshotId |  |  |
| -Size | Intege r |  | 否 | 2000 |  | DiskDeviceMapping.N云盘的大小，单位为 GiB，参数格式为 DiskDeviceMapping.N .Size 。 DiskDeviceMapping.N.Siz e的取值和默认值与 DiskDeviceMapping.N .SnapshotId 参数有关： 如果没有指定 SnapshotId ， Si ze 取值以及默认值为： 普通云盘：5~2000 GiB，默认为5。 其他云盘：20~32768 GiB，默认为20。 如果指定了 SnapshotId ， Si ze 取值必须大于等于 SnapshotId 的大小，默认为 SnapshotId 的大小。 |  |  |
|  |  |  |  |  |  |  | DiskDeviceMapping.N |  |
|  |  |  |  |  |  | .SnapshotId |  |  |

|  |  | DiskDeviceMapping.N |  |
|---|---|---|---|
|  | .Size |  |  |

|  | SnapshotId |
|---|---|
| ze |  |

| Si |  |
|---|---|

|  | SnapshotId |
|---|---|
| ze |  |

| Si |  |
|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| -Device | String |  | 否 | /dev/vdb |  | 指定DiskDeviceMapping.N 在自定义镜像中的设备名称， 参数格式为 DiskDeviceMapping.N .Device 。取值范围： 其他云盘（例如SSD云盘、高效云盘和ESSD云盘）：/dev/vda~/dev/vd z。 普通云盘：/dev/xvda~/dev/xv dz。 |  |  |
| -DiskType | String |  | 否 | system |  | 指定 DiskDeviceMapping.N 在新镜像中的云盘类型，参数格式为 DiskDeviceMapping.N .DiskType 。您可以通过该参数使用数据盘快照做为镜像的系统盘，如果不指定，默认为快照对应的云盘类型。取值范围： system：系统盘 data：数据盘 |  |  |
|  |  |  |  |  |  |  | DiskDeviceMapping.N |  |
|  |  |  |  |  | m | .DiskType |  |  |
| Tag | Repea tList | Query | 否 | / |  | 标签列表。 |  |  |
| -key | String |  | 否 | null |  | 镜像的标签键。 为提高兼容性，建议您尽量使用 Tag.N.Key 参数。 |  |  |
| -Key | String |  | 否 | KeyTest |  | 镜像的标签键，参数格式为 Tag.N.Key ，N的取值范围为 1~20。 一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 或 https:/ / 。 |  |  |
| -Value | String |  | 否 | ValueTest |  | 镜像的标签值，参数格式为 Tag.N.Value ，N的取值范围为 1~20。 一旦传入该值，允许为空字符串。最多支持128个字符，不能包含 http:// 或 https:/ / 。 |  |  |

|  |  | DiskDeviceMapping.N |  |
|---|---|---|---|
|  | .Device |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -value | String |  | 否 | null | 镜像的标签值。 为提高兼容性，建议您尽量使用 Tag.N.Value 参数。 |
| Features | Struct | Query | 否 | null | 暂不支持该参数。 |
| - ImdsSuppo rt | String |  | 否 | null | 暂不支持该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ImageId | String | m- bp146shijn7hujku** ** | 镜像ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env***-d** &SnapshotId=s-bp17441ohwkdca0**** &ImageName=TestCentOS
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
    "ImageId": "m-bp146shijn7hujku****"
}
```

`XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
      <ImageId>m-bp146shijn7hujku****</ImageId>
```

**错误码**

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NAME ILLEGAL _ | InvalidImageName.Malformed | The specified Image name is wrongly formed. |
| 400 | -121 | InvalidImageName.Duplicated | The specified Image name has already bean used. |
| 400 | DESCRIPTION ILLEG _ AL | InvalidDescription.Malformed | The specified description is wrongly formed. |
| 400 | Abs.InvalidImageNa me.Malformed | InvalidImageName.Malformed | The specified Image name is wrongly formed. |
| 400 | Abs.InvalidDescripti on.Malformed | InvalidDescription.Malformed | The specified description is wrongly formed. |
| 400 | PARAMETER IMAGE _ _ VERSION ILLEGAL _ | InvalidImageVersion.Malformed | The specified ImageVersion is wrongly formed. |
| 400 | -215 | IncorrectInstanceStatus | The current status of the instance does not support this operation. |
| 400 | -15026 | IncorrectInstanceStatus | The current status of the instance does not support this operation. |
| 400 | 21001 | InstanceLockedForSecurity | The specified operation is denied as your instance is locked for security reasons. |
| 400 | Abs.InvalidDevice.M alformed | InvalidDevice.Malformed | The specified parameter DiskDeviceMapping.n.Device is not valid. |
| 400 | Abs.MissingParamet er.CreateImage | MissingParameter | The input parameter SnapshotId or InstanceId or DiskDeviceMapping that is mandatory for processing this request is not supplied. |
| 400 | PARAMETER MISS F _ _ OR CREATE IMAGE _ _ | MissingParameter | The input parameter SnapshotId or InstanceId or DiskDeviceMapping that is mandatory for processing this request is not supplied. |
| 400 | Abs.InvalidDiskSize. ValueNotSupported | InvalidSize.ValueNotSupported | The specified parameter DiskDeviceMapping.n.Size beyond the permitted range. |
| 400 | Abs.InvalidDevice.In Use | InvalidDevice.InUse | The specified parameter DiskDeviceMapping.n.Device has been occupied. |
| 400 | Abs.InvalidSystemS napshot.Missing | OperationDenied | The specified parameter DiskDeviceMapping.n.SnapshotI d does not contain system disk snapshot. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidSystemS napshot.Redundant | OperationDenied | The specified parameter DiskDeviceMapping.n.SnapshotI d contains two or more system disk snapshots. |
| 400 | Abs.InvalidInstanceT ype.ValueNotSuppor ted | InvalidDiskCategory.CreateImag e | The specified diskCategory is not allowed to create image. |
| 400 | Abs.InvalidArchitect ure.Malformed | InvalidArchitecture.Malformed | The specified Architecture is wrongly formed. |
| 400 | Abs.InvalidPlatform. Malformed | InvalidPlatform.Malformed | The specified Platform is wrongly formed. |
| 400 | Abs.NotSupportEncr yptedSystemDisk | OperationDenied | Not support creating system image from an encrypted snapshot/disk. |
| 400 | InvalidParameter.All Empty | InvalidParameter.AllEmpty | %s |
| 400 | InvalidParameter.Di skType | InvalidParameter.DiskType | The specified disk type which has kms key can't convert to system disk. |
| 400 | Duplicate.TagKey | Duplicate.TagKey | The Tag.N.Key contain duplicate key. |
| 400 | InvalidTagKey.Malfo rmed | InvalidTagKey.Malformed | The specified Tag.n.Key is not valid. |
| 400 | InvalidTagValue.Mal formed | InvalidTagValue.Malformed | The specified Tag.n.Value is not valid. |
| 400 | SYSTEM DISK NOT _ _ _ EXIST | InvalidInstance.NotFoundSystem Disk | The specified instance does not have system disk. |
| 400 | Abs.InvalidImageFa mily.Malformed | InvalidImageFamily.Malformed | The format of the specified image family is invalid. |
| 400 | IMAGE FAMILY IMA _ _ GES QUOTA FULL _ _ | ImageQuotaExceed.ImageFamil y | The specified image family exceeds the maximum number of images for one image family. |
| 400 | IMAGE FAMILY QUO _ _ TA FULL _ | ImageFamilyQuotaExceed | The number of image families exceeds the limit in the region. |
| 400 | Abs.InvalidDiskType. ValueNotSupported | InvalidDiskType.ValueNotSuppor ted | The specified disk type is not supported. |
| 400 | -187 | IdempotenceParamNotMatch | Request uses a client token in a previous request but is not identical to that request. |
| 400 | SHARED SNAPSHOT _ NOT SUPPORT CRE _ _ _ ATE IMAGE _ | OperationDenied | Shared snapshots do not support creating images. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ENCRYPTED SHARE _ _ SNAPSHOT NOT SU _ _ PPORT IMAGE CREA _ _ TION | OperationDenied | Shared snapshots do not support creating images. |
| 400 | Abs.InvalidBootMod e.ArmImageNotSup ported | InvalidBootMode.NotSupport | The specified parameter BootMode is not supported for current image architecture. |
| 400 | InvalidParameter.Fe aturesImdsSupport | InvalidParameter.FeaturesImdsS upport | The specified parameter Features.ImdsSupport is not supported. |
| 400 | TO IMAGE EXIST _ _ | InvalidImageName.Duplicated | The specified Image name has already bean used. |
| 400 | DISK CATEGORY OP _ _ ERATION NOT SUPP _ _ ORTED | InvalidOperation.DiskCategoryU nsupported | The current category of the disk does not support this operation. |
| 403 | PARAMETER SNAPS _ HOT check DISK ST _ _ _ ATUS | IncorrectDiskStatus.NeverAttach ed | The specified disk has never been attached to instance. |
| 403 | SNAPSHOT CREATE _ NOT FINISHED _ _ | InvalidSnapshotId.NotReady | The current status of the DiskDeviceMapping.n.SnapshotI d or SnapshotId does not support this operation. |
| 403 | -912 | InvalidSnapshotId.NotReady | The current status of the DiskDeviceMapping.n.SnapshotI d or SnapshotId does not support this operation. |
| 403 | SNAPSHOT AT BEF _ _ ORE ASSIGN DATE _ _ | InvalidSnapshot.TooOld | This operation is denied because the specified snapshot by DiskDeviceMapping.n.SnapshotI d or SnapshotId is created before 2013-07-15. |
| 403 | SNAPSHOT DISK IN _ _ _ BLACK LIST _ | OperationDenied | The specified snapshot is not allowed to create image. |
| 403 | SNAPSHOT IN BLAC _ _ K LIST _ | OperationDenied | The specified snapshot is not allowed to create image. |
| 403 | QUOTA FULL _ | QuotaExceed.Image | The Image Quota exceeds. |
| 403 | PARAMETER SNAPS _ HOT CHECK SYSTE _ _ M | OperationDenied | The specified snapshot is not from system disk. |
| 403 | 12133 | InvalidParamter.Conflict | The specified same token is trying to make requests with different parameters. |
| 403 | ACCOUNT OVERDUE _ | InvalidAccountStatus.NotEnough Balance | Your account does not have enough balance. |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | SNAPSHOT SERVICE _ UNAVAILABLE _ | InvalidAccountStatus.SnapshotS erviceUnavailable | Snapshot service has not been opened yet. |
| 403 | USER NOT IN WHIT _ _ _ E LIST _ | UserNotInTheWhiteList | The user is not in the white list of create image by data disk snapshot. |
| 403 | -1016028 | IncorrectDiskStatus.Invalid | Device status is invalid, please restart instance and try again. |
| 403 | SNAPSHOT NOT SU _ _ PPORT IMAGE CREA _ _ TION | OperationDenied.InvalidSnapsho tCategory | %s |
| 403 | -120 | QuotaExceed.Snapshot | The snapshot quota exceeds. |
| 403 | -1017068 | IncorrectDiskStatus.Transferring | The specified device is transferring, you can retry after the process is finished. |
| 403 | DISK STATUS ERRO _ _ R | IncorrectDiskStatus | The current disk status does not support this operation. |
| 403 | PARAMETER MISS S _ _ YSTEM SNAPSHOT _ | InvalidSystemSnapshot.Missing | %s |
| 403 | -1016030 | IncorrectDiskStatus.CreatingSna pshot | A previous snapshot creation is in process. |
| 403 | CMKUnauthorized | InvalidParameter.KMSKeyId.CMK Unauthorized | The CMK needs to be added ECS tag. |
| 403 | CMKNotEnabled | InvalidParameter.KMSKeyId.CMK NotEnabled | The CMK needs to be enabled. |
| 403 | KMSUnauthorized | InvalidParameter.KMSKeyId.KMS Unauthorized | ECS service have no right to access your KMS. |
| 403 | QuotaExceed.Tags | QuotaExceed.Tags | %s |
| 403 | SNAPSHOT NOT SU _ _ PPORT IMAGE CREA _ _ TION | InvalidSnapshotCategory.NotSup portImageCreation | The specified snapshot category does not support create image. |
| 403 | SNAPSHOT SERVICE _ UNAVAILABLE _ | InvalidAccountStatus.SnapshotS erviceUnavailable | Snapshot service has not been opened yet. |
| 403 | TOO MANY UNFINIS _ _ HED SNAPSHOT _ | TooManySnapshot.Unfinished | There are too many snapshots being created, please wait for them to be created done. |
| 403 | HibernationConfigur ed.Instance.Operati onForbidden | HibernationConfigured.Instance OperationForbidden | The operation is not permitted due to limit of the hibernation configured instance. |
| 403 | -10002 | SnapshotNotReady | The specified snapshot is not ready. |
| 403 | DISK NOT CREATED _ _ | IncorrectInstanceStatus.NeedRe start | The instance needs to be restarted after adding a disk in a shutdown status. |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 403 | CONCURRENT SNAP _ SHOT QUOTA EXCE _ _ EDED | QuotaExceed.ConcurrentSnapsh otQuota | The number of snapshots being created for the disk %s has exceeded the concurrent quota (%s). Please wait for the previous snapshots to complete before trying again. |
| 404 | PARAMETER SNAPS _ HOT | InvalidSnapshotId.NotFound | The specified SnapshotId does not exist. |
| 404 | -910 | InvalidSnapshotId.NotFound | The specified SnapshotId does not exist. |
| 404 | Abs.SnapshotNotFo und | InvalidSnapshotId.NotFound | The specified SnapshotId does not exist. |
| 404 | INSTANCE NO EXIS _ _ T | InvalidInstanceId.NotFound | The specified InstanceId does not exist. |
| 404 | -205 | InvalidInstanceId.NotFound | The specified InstanceId does not exist. |
| 404 | InvalidResourceGro up | InvalidResourceGroup.NotFound | The ResourceGroup provided does not exist in our records. |
| 500 | -30003 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -95 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -1000021 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -30004 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -1000016 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -2092 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -60 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -4099 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -4016 | InternalError | The process of creating snapshot has failed due to some unknown error. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -4015 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -10000611 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -28317 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -19 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -2029 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -10000510 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -2008004 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | -1017001 | InternalError | The process of creating snapshot has failed due to some unknown error. |
| 500 | RAMSerivceUnavaila bleTemporary | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -305 | InternalError | The process of creating snapshot has failed due to some unknown error. |

##### DescribeImages

**接口说明**

您可以查询的镜像资源包括您的自定义镜像、阿里云提供的公共镜像以及其他阿里云用户主动共享给您的共享镜像。 支持分页查询，查询结果包括可使用的镜像资源的总数和当前页的镜像资源。每页的数量默认为10条。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeImages | 系统规定参数，取值：DescribeImages。 |

云服务器ECS

| RegionId | String | 是 | cn-qingdao-**** | 镜像所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
|---|---|---|---|---|
| Status | String | 否 | Available | 查询某种状态下的镜像。取值范围： Creating：镜像正在创建中。 Waiting：多任务排队中。 Available（默认）：您可以使用的镜像。 UnAvailable：您不能使用的镜像。 CreateFailed：创建失败的镜像。 支持同时取多个值，值之间以半角逗号（,） 隔开。 |
| ImageId | String | 否 | m- bp1g7004ksh0oe uc3*** | 镜像ID。 |
| SnapshotId | String | 否 | s- bp17ot2q7x72gg twr*** | 根据某一快照ID创建的自定义镜像。 |
| ImageName | String | 否 | Test | 镜像名称。 |
| ImageOwnerAlias | String | 否 | self | 镜像来源。取值范围： system：阿里云提供的公共镜像。 self：您创建的自定义镜像。 others：其他用户共享给您的镜像。 默认值：空，空表示返回取值为system、 self以及others的结果。 |
| InstanceType | String | 否 | ecs.g5.large | 指定实例类型可以使用的镜像。 |
| IsSupportIoOptimi zed | Boolean | 否 | true | 镜像是否可以运行在I/O优化实例上。 |
| IsSupportCloudini t | Boolean | 否 | true | 镜像是否支持Cloud Init。 |
| OSType | String | 否 | linux | 镜像的操作系统类型。取值范围： windows。 linux。 |
| Architecture | String | 否 | i386 | 镜像的体系架构。取值范围： i386。 x86 64。 _ arm64。 |
| PageNumber | Integer | 否 | 1 | 镜像资源列表的页码。起始值：1。 默认值：1。 |

云服务器ECS

| PageSize | Integer | 否 | 1 | 分页查询时设置的每页行数。最大值： 100。 默认值：10。 |
|---|---|---|---|---|
| Usage | String | 否 | instance | 镜像是否已经运行在ECS实例中。取值范围： instance：镜像处于运行状态，有ECS实例使用。 none：镜像处于闲置状态，暂无ECS实例使用。 |
| DryRun | Boolean | 否 | false | 是否只预检此次请求。 true：发送检查请求，不会查询资源状况。检查项包括AccessKey是否有效、 RAM用户的授权情况和是否填写了必需参数。如果检查不通过，则返回对应错误。 如果检查通过，会返回错误码 DryRunOperation。 false：发送正常请求，通过检查后返回 2XX HTTP状态码并直接查询资源状况。 默认值：false。 |
| ActionType | String | 否 | CreateEcs | 镜像需要被使用到的场景。取值范围： CreateEcs（默认）：创建实例。 ChangeOS：更换系统盘/更换操作系统。 |
| Tag.N.key | String | 否 | null | 镜像的标签键。 说明该参数即将被弃用，为提高兼容性，建议您尽量使用Tag.N.Key 参数。 |
| Tag.N.Key | String | 否 | Test | 镜像的标签键。N的取值范围：1~20。 |
| Tag.N.Value | String | 否 | Test | 镜像的标签值。N的取值范围：1~20。 |
| Tag.N.value | String | 否 | null | 镜像的标签值。 说明该参数即将被弃用，为提高兼容性，建议您尽量使用 Tag.N.Value参数。 |
| Filter.N.Key | String | 否 | CreationStartTim e | 指定过滤类型的Key。 |
| Filter.N.Value | String | 否 | 2017-12- 05T22:40:00Z | 指定过滤类型的Value。 |

**返回数据**

云服务器ECS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Images | Array of Image |  | 镜像信息Images组成的集合。 |
| Image |  |  |  |
| Architecture | String | x86 64 _ | 镜像系统架构类型。可能值： i386。 x86 64。 _ arm64。 |
| BootMode | String | BIOS | 修改镜像的启动模式。取值范围： BIOS：BIOS启动模式。 UEFI：UEFI启动模式。 说明您需要了解指定的镜像支持的启动模式，当通过该参数修改启动模式后，必须与镜像本身支持的启动模式匹配，实例才能正常启动。 |
| CreationTime | String | 2018-01- 10T01:01:10Z | 镜像的创建时间。 |
| Description | String | Archive log for Oracle | 描述信息。 |
| DetectionOptio ns | Struct |  | 镜像检测相关结果。 |
| Items | Array of Item |  | 镜像检测项列表。 |
| Item |  |  |  |
| Name | String | Nvme | 镜像检测项名称。 |
| RiskCode | String | NVMe.NotInstallded | 检测项可能存在的缺陷。 |
| RiskLevel | String | High | 导入的自定义镜像检测项是否存在风险，如果存在风险返回此字段，不存在风险则不返回。 风险等级可能值： High：严重，影响实例能否启动成功，强烈建议修复。 Medium：重要，影响实例启动性能或者实例配置等，建议优化。 |
| Value | String | Supported | 镜像检测项结果。 |

云服务器ECS

| Status | String | Processing | 镜像检测任务状态。可能值： Processing：检测中。 Finished：检测完成。 |
|---|---|---|---|
| DiskDeviceMap pings | Array of DiskDeviceMap ping |  | 镜像下包含云盘和快照的映射关系。 |
| DiskDeviceMap ping |  |  |  |
| Device | String | /dev/xvdb | 云盘的设备信息，例如/dev/xvdb。 说明该参数即将停止使用，为提高代码的兼容性，建议您尽量不要使用该参数。 |
| Format | String | qcow2 | 镜像格式。 |
| ImportOSSBuck et | String | testEcsImport | 导入镜像的OSS的bucket。 |
| ImportOSSObje ct | String | imageImport | 导入镜像文件的所属OSS的object。 |
| Progress | String | 32% | 对于复制中的镜像，返回复制任务的进度。 |
| RemainTime | Integer | 213 | 对于复制中的镜像，返回复制任务的剩余时间，单位为秒。 |
| Size | String | 80 | 云盘的大小。 |
| SnapshotId | String | s- bp17ot2q7x72ggtwr *** | 快照ID。 |
| Type | String | custom | 镜像的类型。 |
| Features | Struct |  | 镜像特性相关属性。 |
| NvmeSupport | String | supported | 镜像是否支持NVMe。可能值： supported：支持。表示以该镜像创建的实例支持NVMe协议。 unsupported：不支持。表示以该镜像创建的实例不支持NVMe协议。 |
| ImageFamily | String | as-hangzhou-game- 01 | 说明该参数未开放使用。 |
| ImageId | String | m- bp1g7004ksh0oeuc 3*** | 镜像ID。 |

云服务器ECS

| ImageName | String | Test | 镜像的名称。 |
|---|---|---|---|
| ImageOwnerAli as | String | self | 说明该参数未开放使用。 |
| ImageOwnerId | Long | 1234567890 | 说明该参数未开放使用。 |
| ImageVersion | String | 2 | 镜像版本。 |
| IsCopied | Boolean | false | 是否是拷贝的镜像。 |
| IsPublic | Boolean | false | 说明该参数未开放使用。 |
| IsSelfShared | String | true | 是否共享过该自定义镜像给其他用户。 |
| IsSubscribed | Boolean | false | 说明该参数未开放使用。 |
| IsSupportCloudi nit | Boolean | true | 是否支持Cloud Init。 |
| IsSupportIoOpti mized | Boolean | true | 是否可以在I/O优化实例上运行。 |
| LoginAsNonRoo tSupported | Boolean | false | 当前镜像是否支持非root用户登录。可能值： true：支持。 false：不支持。 |
| OSName | String | Aliyun Linux 2.1903 | 操作系统的中文显示名称。 |
| OSNameEn | String | Aliyun Linux 2.1903 | 操作系统的英文显示名称。 |
| OSType | String | Linux | 操作系统类型。可能值： windows。 linux。 |
| Platform | String | Aliyun Linux | 操作系统平台。 |
| ProductCode | String | jxsc000204 | 说明该参数未开放使用。 |
| Progress | String | 100 | 镜像完成的进度，单位为百分比。 |

云服务器ECS

| ResourceGroup Id | String | rg- bp67acfmxazb4ph** * | 说明该参数未开放使用。 |
|---|---|---|---|
| Size | Integer | 80 | 镜像大小，单位GiB。 |
| Status | String | Available | 镜像的状态。可能值： UnAvailable：不可用。 Available：可用。 Creating：创建中。 CreateFailed：创建失败。 |
| SupplierName | String | TestName | 说明该参数未开放使用。 |
| Tags | Array of Tag |  | 镜像的标签对信息。 |
| Tag |  |  |  |
| TagKey | String | Test | 镜像的标签键。 |
| TagValue | String | Test | 镜像的标签值。 |
| Usage | String | none | 有引用关系的资源类型。可能值： instance：创建了一台或多台ECS实例。 none：未创建过ECS实例。 |
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 1 | 当前分页包含多少条目。 |
| RegionId | String | cn-qingdao-**** | 镜像所属地域ID。 |
| RequestId | String | 66189103-EDB2- 43E2-BB60- BFF2B62***** | 请求ID。 |
| TotalCount | Integer | 24 | 镜像总数。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-****
```

`&<`公共请求参数> 云服务器ECS 正常返回示例 `XML` 格式

```xml
      <PageNumber>1</PageNumber>
      <TotalCount>61</TotalCount>
      <PageSize>1</PageSize>
      <RegionId>cn-qingdao-env17-d01</RegionId>
      <RequestId>66189103-EDB2-43E2-BB60-BFF2B62*****</RequestId>
      <Images>
            <Image>
                  <ImageId>m-bp1g7004ksh0oeuc3***</ImageId>
                  <Description>Archive log for Oracle</Description>
                  <OSNameEn>Windows Server  2016 Data Center Edition 64bit Chinese
Edition</OSNameEn>
                  <ResourceGroupId></ResourceGroupId>
                  <OSType>windows</OSType>
                  <Architecture>x86_64</Architecture>
```

`<OSName>Windows Server 2016` 数据中心版 `64`位中文版`</OSName>`

```xml
                  <DiskDeviceMappings>
                        <DiskDeviceMapping>
                              <ImportOSSObject></ImportOSSObject>
                              <Format></Format>
                              <Device>/dev/xvda</Device>
                              <Type>system</Type>
                              <SnapshotId>s-bp17ot2q7x72ggtwr***</SnapshotId>
                              <ImportOSSBucket></ImportOSSBucket>
                              <Progress></Progress>
                              <Size>60</Size>
                        </DiskDeviceMapping>
                  </DiskDeviceMappings>
                  <ImageOwnerAlias>self</ImageOwnerAlias>
                  <Progress>100%</Progress>
                  <IsSupportCloudinit>true</IsSupportCloudinit>
                  <Usage>none</Usage>
                  <CreationTime>2019-11-15T06:07:05Z</CreationTime>
                  <ImageVersion></ImageVersion>
                  <Tags>
                        <Tag>
                              <TagValue>Oracle</TagValue>
                              <TagKey>DTS</TagKey>
                        </Tag>
                  </Tags>
                  <Status>Available</Status>
                  <ImageName>Oracle_DTS</ImageName>
                  <IsSupportIoOptimized>true</IsSupportIoOptimized>
                  <IsSelfShared>False</IsSelfShared>
                  <IsCopied>false</IsCopied>
                  <IsSubscribed>false</IsSubscribed>
                  <Platform>Windows Server 2016</Platform>
                  <Size>60</Size>
            </Image>
      </Images>
```

云服务器ECS `JSON` 格式

```json
{
 "PageNumber": 1,
 "TotalCount": 61,
 "PageSize": 1,
 "RegionId": "cn-qingdao-env17-d01",
 "RequestId": "66189103-EDB2-43E2-BB60-BFF2B62*****",
 "Images": {
  "Image": [
   {
    "ImageId": "m-bp1g7004ksh0oeuc3***",
    "Description": "Archive log for Oracle",
    "OSNameEn": "Windows Server  2016 Data Center Edition 64bit Chinese Edition",
    "ResourceGroupId": "",
    "OSType": "windows",
    "Architecture": "x86_64",
```

`"OSName": "Windows Server 2016` 数据中心版 `64`位中文版`",`

```json
    "DiskDeviceMappings": {
     "DiskDeviceMapping": [
      {
       "ImportOSSObject": "",
       "Format": "",
       "Device": "/dev/xvda",
       "Type": "system",
       "SnapshotId": "s-bp17ot2q7x72ggtwr***",
       "ImportOSSBucket": "",
       "Progress": "",
       "Size": "60"
      }
```

]

```json
    },
    "ImageOwnerAlias": "self",
    "Progress": "100%",
    "IsSupportCloudinit": true,
    "Usage": "none",
    "CreationTime": "2019-11-15T06:07:05Z",
    "ImageVersion": "",
    "Tags": {
     "Tag": [
      {
       "TagValue": "Oracle",
       "TagKey": "DTS"
      }
```

]

```json
    },
    "Status": "Available",
    "ImageName": "Oracle_DTS",
    "IsSupportIoOptimized": true,
    "IsSelfShared": "False",
    "IsCopied": false,
    "IsSubscribed": false,
    "Platform": "Windows Server 2016",
    "Size": 60
   }
```

]

```
 }
```

云服务器ECS

```
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidImageOwner Alias.ValueNotSupp orted | The specified ImageOwnerAlias value is not supported. | 无效的镜像所有者别名，请您检查该参数是否正确。 |
| 400 | InvalidParamter | Invalid Parameter | 指定的参数不合法。 |
| 400 | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. | 指定的 Tag.N.Key 和 Tag.N.Value 不匹配。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
| 400 | InvalidInstanceType. ValueNotSupported | The specified InstanceType does not exist or beyond the permitted range. | 您指定的实例规格不存在，或者您没有权限操作此规格的实例。 |
| 404 | InvalidUsage | The specifed Usage is not valid | 指定有引用关系的资源类型 （image、disk、image disk、 _ none）不合法。 |
| 404 | InvalidOSType | The specifed OSType is not valid | 不支持指定的操作系统。 |
| 404 | InvalidArchitecture | The specifed Architecture is not valid | 指定的架构不存在。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### ModifyImageAttribute

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyImageAttri bute | 系统规定参数。取值： ModifyImageAttribute。 |
| ImageId | String | 是 | m-imageid1 | 自定义镜像的ID。 |
| RegionId | String | 是 | cn-qingdao-***** | 自定义镜像所在的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| ImageName | String | 否 | Test | 自定义镜像的名称。能包含2~128个字符。 必须以大小字母或中文开头，可包含数字、 半角冒号（:）、下划线（ ）或者短划线 _ （-）。不能以http://和https://开头。 默认值：空，表示保持原有名称不变。 |
|---|---|---|---|---|
| BootMode | String | 否 | BIOS | 配置镜像的启动模式。取值范围： BIOS：BIOS启动模式。 UEFI：UEFI启动模式。 默认值：BIOS。如果 Architecture=arm64 ，则该参数默认值为UEFI，且只能设置为UEFI。 说明您需要了解指定的镜像支持的启动模式，当通过该参数修改启动模式后，必须与镜像本身支持的启动模式匹配，实例才能正常启动。 |
| Description | String | 否 | testDescription | 自定义镜像的描述信息。能包含2~256个字符。不能以http://和https://开头。 默认值：空，表示保持原有描述信息不变。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyImageAttribute &ImageId=m-imageid1 &RegionId=cn-qingdao-**** &ImageName=Test &BootMode=BIOS &Description=testDescription
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidImageName. Malformed | The specified Image name is wrongly formed. | 镜像名称格式错误。长度为2~128个字符。必须以大小字母或中文开头， 不能以aliyun和acs:开头，不能包含 http://或者https://。可以包含数字、半角句号（.）、半角冒号 （:）、下划线（ ）或者短划线 _ （-）。 |
| 400 | InvalidImageName. Duplicated | The specified Image name has already bean used. | 镜像名称已经重复。 |
| 400 | InvalidDescription.M alformed | The specified description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256 个字符，不能以 http:// 和 https:// 开头。 |
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像 ID 是否正确。 |

##### DeleteImage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DeleteImage | 系统规定参数。取值：DeleteImage |
| ImageId | String | 是 | m- bp67acfmxazb4p h*** | 镜像ID。如果指定的自定义镜像不存在，则请求将被忽略。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 自定义镜像所在的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| Force | Boolean | 否 | false | 是否执行强制删除。取值范围： true：强制删除自定义镜像，忽略当前镜像是否被其他实例使用。 false：正常删除自定义镜像，删除前检查当前镜像是否被其他实例使用。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云服务器ECS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
&ImageId=m-bp67acfmxazb4ph*** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ImageUsingByInstan ce | The specified image has been used to create instances. | 指定的镜像已被用于创建实例，无法删除。 |
| 403 | ImageUseShared | The specified image has been shared to others. | 指定的镜像已经分享给其它用户。 |
| 403 | OperationDenied.Im ageCopying | The Image is coping. | 正在复制镜像，请您稍后再试。 |
| 403 | ImageIsCreating | The specified image is being created. | 正在生成指定的镜像中。 |
| 403 | ImageIsImporting | The specified Image is importing. | 指定镜像正在导入，无法执行操作。 |
| 403 | ImageIsExporting | The specified Image is exporting. Please cancel task first. | 该镜像正在导出，请先取消任务。 |
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像id是否正确。 |

##### CopyImage

调用CopyImage复制一个地域下的自定义镜像到其他地域。复制镜像可以实现跨地域部署ECS实例、跨地域复制ECS实例等目的。 云服务器ECS

**接口说明**

您可以在其他地域使用复制后的镜像创建ECS实例（RunInstances），或者更换实例的系统盘调用该接口时，您需要注意： 自定义镜像的状态必须为可用（ `Available` ）。 源自定义镜像必须为您账号下的镜像，不能跨账号复制。 复制镜像时，您无法使用DeleteImage删除目标镜像，但是您可以使用CancelCopyImage取消复制任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CopyImage | 系统规定参数。取值：CopyImage |
| ImageId | String | 是 | m- bp1h46wfpjsjastc **** | 源自定义镜像的ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 源自定义镜像的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| DestinationRegio nId | String | 否 | cn-shanghai- env17-d02 | 复制到目标地域的ID。 |
| DestinationImage Name | String | 否 | YourImageName | 复制后的镜像的名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头， 不能以http://和https:// 开头。可以包含数字、半角冒号（:）、下划线（ ）或者短划 _ 线（-）。 默认值：空。 |
| DestinationDescri ption | String | 否 | This is a description example. | 复制后的镜像的描述信息。长度为2~256个英文或中文字符，不能以http://和https://开头。 默认值：空。 |
| Encrypted | Boolean | 否 | false | 是否加密复制后的镜像。 默认值：false。 |
| KMSKeyId | String | 否 | e522b26d-abf6- 4e0d-b5da- 04b7******3c | 加密镜像使用的密钥ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ImageId | String | m- bp1h46wfpjsjastd*** * | 复制后的镜像的ID。 |

云服务器ECS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
&ImageId=m-bp1h46wfpjsjastc**** &RegionId=cn-qingdao-env17-d01 &DestinationRegionId=cn-shanghai-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>C8B26B44-0189-443E-9816-D951F59623A9</RequestId>
      <ImageId>m-bp1h46wfpjsjastd****</ImageId>
```

`JSON` 格式

```json
{
    "RequestId": "C8B26B44-0189-443E-9816-D951F59623A9",
    "ImageId": "m-bp1h46wfpjsjastd****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 401 | InvalidAliUid.IsNull | The aliUid must not be null | 参数aliUid不得为空。 |
| 400 | InvalidImageName. Malformed | The specified Image name is wrongly formed. | 镜像名称不合法。长度为2~128个字符，以英文字母或中文开头，可包含数字，点号（.），下划线（ ）或连 _ 字符（-）。 不能以http://和https:// 开头。 |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | 用户未被授权操作指定的资源。 |
| 400 | InvalidImageName. Malformed | The specified destination Image name is wrongly formed. | 镜像名称不合法。限制条件请参见 DestinationImageName参数说明。 |
| 400 | InvalidDescription.M alformed | The specified destination description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
| 400 | InvalidDescription.M alformed | The specified description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以http://和 https://开头。 |
| 400 | SourceRegion.NotFo und | The source region not found | 指定的源镜像的地域不存在。 |

云服务器ECS

| 400 | DestinationRegion.N otFound | The destination region not found | 指定的目标地域不存在。 |
|---|---|---|---|
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像ID是否正确。 |
| 400 | IncorrectImageStatu s | The image not available. | 指定的镜像不可用。 |
| 400 | InvalidSnapshotId.N otFound | The specified SnapshotId does not exist. | 指定的快照不存在，请您检查快照是否正确。 |
| 400 | InvalidImageName. Duplicated | The destination image is exist. | 指定的镜像名已存在。 |
| 403 | QuotaExceed.Image | The Image Quota exceeds. | 自定义镜像额度已用完。 |
| 403 | QuotaExceed.Snaps hot | The snapshot quota exceeds. | 快照额度超过限制，若要存储新快照，在不影响业务的情况下，请您删除已有的老快照。 |
| 403 | OperationDenied.Im ageCopying | The Image are coping. | 正在复制镜像，请您稍后再试。 |
| 403 | RegionNotSupportC opy | The region not support copy. | 指定的目标镜像地域或者源镜像所在地域暂时不支持镜像复制。 |
| 403 | InvalidSnapshot.Too Old | This operation is denied because the specified snapshot is created before 2013-07-15. | 该操作被拒绝。因为指定的快照创建于2013-07-15之前。 |
| 403 | OperationDenied | The specified snapshot is not allowed to create image. | 指定快照不允许创建镜像。 |
| 403 | IncorrectDestination Region | The destination region is not equal the target region. | 复制镜像的源地域不能等于目标地域。 |
| 403 | SizeExceed.Image | The image exceeds the maximum size. Please open a ticket to add the account to the white list. | 镜像的大小已超过可操作的最大值， 请联系客服添加白名单。 |
| 403 | OperationDeined.En cryptedSnapshot | The image contains encrypted snapshots, which do not support copying. | 指定的镜像含有加密快照，不支持复制这种镜像。 |
| 403 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | OperationDenied.Sa meRegionOnly | The image shared from others can not be copied to another region directly. | 其他人分享的镜像不能复制到另一个地域。 |
| 403 | OperationDenied.No tPublished | The operation is denied because corresponding marketplace image is not published in destination region. | 由于目标地域不支持该类型镜像，导致操作被拒绝。 |
| 404 | InvalidParameter.K MSKeyId.NotFound | The specified KMSKeyId does not exist. | 指定的参数KMSKeyId不存在。 |

云服务器ECS

| 403 | InvalidParameter.K MSKeyId.KMSUnauth orized | ECS service have no right to access your KMS. | ECS服务无权访问您的KMS。 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | InvalidRegion.NotSu pport | The specified region does not support byok. | 该地域不支持BYOK。 |
| 403 | UserNotInTheWhiteL ist | The user is not in byok white list. | 您不在byok白名单中，请加入白名单后重试。 |
| 400 | InvalidParameter.En cryptedIllegal | The specified parameter Encrypted must be true when kmsKeyId is not empty. | 设置参数KMSKeyId后，您必须开启加密属性。 |

##### CancelCopyImage

调用CancelCopyImage取消正在进行中的复制镜像（CopyImage）任务。

**接口说明**

调用该接口时，您需要注意： 取消复制镜像后，目标地域中新建的镜像会被自动删除，源镜像保持不变。 若复制镜像已完成，则操作失败并返回错误提示。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | CancelCopyImag e | 系统规定参数。取值：CancelCopyImage |
| ImageId | String | 是 | m-imageid1 | 正在被复制的镜像ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 目标镜像所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=CancelCopyImage &ImageId=m-imageid1 &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 云服务器ECS 正常返回示例 `XML` 格式

```xml
      <RequestId>C8B26B44-0189-443E-9816-D951F59623A9</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "C8B26B44-0189-443E-9816-D951F59623A9"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像id是否正确。 |
| 400 | ImageCreatedNotFr omCopy | The specified image is not the target image of a copy action. | 这个镜像不是来源于拷贝的镜像，只能取消来自于拷贝的镜像。 |
| 400 | IncorrectImageStatu s | The image is copied finished. | 复制镜像已完成。 |
| 400 | InvalidDescription.M alformed | The specified description is wrongly formed. | 指定的资源描述格式不合法。长度为 2-256个字符，不能以 http:// 和 https:// 开头。 |
| 400 | IncorrectImageStatu s | The specified snapshot is not coping. | 指定的快照不在复制中。 |
| 400 | IncorrectImageStatu s | The specified image is not coping. | 指定的镜像不在复制中。 |
| 400 | IncorrectImageStatu s | The image has completed copy. | 镜像已完成复制。 |
| 400 | IncorrectImageStatu s | The Image copy has been failed. | 复制镜像失败。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 400 | CancelNotSupported | The specified image coping can not be cancelled. | 无法取消复制镜像。 |

##### ModifyImageSharePermission

调用ModifyImageSharePermission管理镜像共享权限。您可以将自己的自定义镜像共享给其他阿里云用户， 该用户可以使用共享的自定义镜像创建 ECS 实例（RunInstances）或者更换实例的系统盘

**接口说明**

云服务器ECS 调用该接口时，您需要注意： 您只能共享自己的自定义镜像给其他阿里云用户。 每份自定义镜像一次最多共享给 10 个阿里云账号。所以，参数 AddAccount.n 或者参数 RemoveAccount.n 单次最多可以传入 10 个阿里云账号，超过 10 个账号系统会忽略该参数。 每份自定义镜像最多可以共享给 50 个阿里云账号。 使用共享镜像创建 ECS 实例（RunInstances)后，一旦自定义镜像拥有者解除了镜像共享关系，或者删除了自定义镜像（DeleteImage），该实例将无法初始化系统盘（ReInitDisk）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyImageShar ePermission | 系统规定参数。取值： ModifyImageSharePermission |
| ImageId | String | 是 | m-imageid1 | 被共享的自定义镜像 ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 自定义镜像所属的地域 ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| AddAccount.N | RepeatLi st | 否 | 155780923*** | 授权共享镜像的阿里云账号 ID。n 的取值范围：1~10，超过 10 系统会忽略该参数。 |
| RemoveAccount. N | RepeatLi st | 否 | 155780923*** | 删除镜像共享的阿里云账号 ID。n 的取值范围：1~10，超过 10 系统会忽略该参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求 ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyImageSharePermission &ImageId=m-imageid1 &RegionId=cn-qingdao-env17-d01 &AddAccount.1=155780923***
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>C8B26B44-0189-443E-9816-D951F59623A9</RequestId>
```

云服务器ECS `JSON` 格式

```json
{
    "RequestId": "C8B26B44-0189-443E-9816-D951F59623A9"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | The input parameter "RegionId" that is mandatory for processing this request is not supplied. | RegionId不得为空。 |
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像ID是否正确。 |
| 404 | InvalidAccount.NotF ound | The specified parameter "AddAccount.n" or "RemoveAccount.n" does not exist. | 参数AddAccount.N或者 RemoveAccount.N不存在。 |
| 404 | InvalidAccount.Forb biden | The specified Account does not yourself. | 不能把镜像共享给自己。 |
| 403 | QuotaExceed.ShareI mage | The shared Image Quota exceeds. | 已经超过自定义镜像共享配额限制。 |
| 403 | QuotaExceed.ShareI mageUser | The shared Image user Quota exceeds. | 已经超过单个镜像共享给用户数量的配额限制。 |
| 400 | InvalidGroup.Malfor med | The specified Group is wrongly formed. | 指定的组不存在。 |
| 403 | InvalidImageId.BidM ismatch | Cannot share image with other bid user. | 镜像无法跨运营商共享。 |
| 403 | OperationDeined.En cryptedSnapshot | The image contains encrypted snapshots, which do not support share. | 指定的镜像含有加密快照，不支持共享这种镜像。 |

##### DescribeImageSharePermission

调用DescribeImageSharePermission查询一份自定义镜像已经共享的所有用户。返回结果支持分页显示，每页的信息条目默认为10条。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeImageSh arePermission | 系统规定参数，取值： DescribeImageSharePermission。 |
| ImageId | String | 是 | m-282dz**** | 自定义镜像ID。 |

云服务器ECS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 自定义镜像所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 查询结果显示的页码。起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 10 | 查询结果显示的每页的信息条目数。最大值：100。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Accounts | Array |  | 阿里云注册用户。 |
| Account |  |  |  |
| AliyunId | String | 123456**** | 阿里云账号ID。 |
| ImageId | String | m-282dz**** | 自定义镜像ID。 |
| PageNumber | Integer | 1 | 查询结果显示的页码。 |
| PageSize | Integer | 10 | 每页的信息条目数。 |
| RegionId | String | cn-qingdao-env17- d01 | 镜像所属地域ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| ShareGroups | Array |  | 共享组。 |
| ShareGroup |  |  |  |
| Group | String | all | 共享分组。 |
| TotalCount | Integer | 1 | 记录总数。 |

**示例**

请求示例云服务器ECS

```
https://ecs.example.com/?Action=DescribeImageSharePermission &ImageId=m-282dz**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <ImageId>m-282dz****</ImageId>
      <PageNumber>1</PageNumber>
      <PageSize>10</PageSize>
      <RegionId>cn-qingdao-env17-d01</RegionId>
      <TotalCount>1</TotalCount>
      <RequestId>441CF898-42FF-47CF-9348-3C3BFF557278</RequestId>
      <ShareGroups>
            <ShareGroup>
                  <Group>all</Group>
            </ShareGroup>
      </ShareGroups>
      <Accounts>
            <Account>
                  <AliyunId>123456****</AliyunId>
            </Account>
      </Accounts>
```

`JSON` 格式

```json
{
    "ShareGroups": {
        "ShareGroup": [
            {
                "Group": "all"
            }
```

]

```json
    },
    "Accounts": {
        "Account": [
            {
                "AliyunId": "123456****"
            }
```

]

```json
    },
    "ImageId": "m-282dz****",
    "PageNumber": 1,
    "PageSize": 10,
    "RegionId": "cn-qingdao-env17-d01",
    "TotalCount": 1,
    "RequestId": "9AD96F49-0BE5-4868-A66A-224352549CEC"
}
```

**错误码**

云服务器ECS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | The input parameter "RegionId "that is mandatory for processing this request is not supplied. | 参数“RegionId”不能为空。 |
| 400 | MissingParameter | The input parameter "ImageId "that is mandatory for processing this request is not supplied. | 参数“ImageId”不能为空。 |
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像id是否正确。 |

##### ImportImage

调用ImportImage导入一份您的本地镜像文件到云服务器ECS，作为自定义镜像出现在相应地域中。您可以使用导入的镜像创建ECS实例（RunInstances），或者更换实例的系统盘（ReplaceSystemDisk）。

**接口说明**

调用该接口时，您需要注意： 您必须提前上传镜像文件到对象存储OSS。

| NoSetRoletoECSServiceAcount |  | ，部分步骤策 |
|---|---|---|
| 创建角色 | AliyunECSImageImportDefaultRole |  |

```json
{
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "ecs.example.com"
```

]

```
      }
    }
```

`],`

```json
  "Version": "1"
}
```

ii. 在该角色下，添加系统策略 `AliyunECSImageImportRolePolicy` 。或者您也可以创建自定义策略，权限必须包含： 云服务器ECS

```json
{
  "Version": "1",
  "Statement": [
    {
      "Action": [
       "oss:GetObject",
        "oss:GetBucketLocation",
        "oss:GetBucketInfo"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
    }
```

]

```
}
```

不能删除正在导入的镜像。 支持取消导入镜像任务（CancelTask）。导入镜像任务取消后，导入的镜像将被删除。 导入镜像的地域必须跟镜像文件上传的OSS Bucket的地域相同。 参数 `DiskDeviceMapping.N` 中N的取值范围为1~17。N为1时表示系统盘，N为2~17时表示数据盘。 如果您待导入的自定义镜像对应的系统架构为arm64时，您需要设置其RTC时钟使用UTC时间标准。

**请求参数**

| 名称 | 类型 | 是否必选 |  | 示例值 | 描述 |  |
|---|---|---|---|---|---|---|
| Action | String | 是 |  | ImportImage | 系统规定参数，取值：ImportImage。 |  |
| RegionId | String | 是 |  | cn-qingdao-**** | 源自定义镜像的地域ID。 您可以调用DescribeRegions查看最新的阿里云地域列表。 |  |
| DiskDeviceMappi ng.N.Format | String | 否 |  | qcow2 | 镜像格式。取值范围： RAW。 VHD。 qcow2。 默认值：无，表示阿里云自动检测镜像格式，以检测格式为准。 |  |
| DiskDeviceMappi ng.N.OSSBucket | String | 否 |  | ecsimageos | 镜像文件所在的OSS Bucket。 说明首次导入镜像到该OSS Bucket前，请参见接口说明章节添加 RAM授权策略，否则会报错 NoSetRoletoECSServiceAcount 。 |  |
| DiskDeviceMappi ng.N.OSSObject | String | 否 |  | CentOS 5.4 32.ra _ _ w | 镜像文件所在的OSS Object的文件名称 （key）。 |  |

| NoSetRoletoECSServiceAcount |  |
|---|---|

云服务器ECS

| DiskDeviceMappi ng.N.DiskImSize | Integer | 否 | 80 | 自定义镜像大小。 说明该参数即将被弃用，为提高兼容性，请尽量使用 DiskDeviceMapping.N.DiskImageSi ze参数。 |
|---|---|---|---|---|
| DiskDeviceMappi ng.N.DiskImageSi ze | Integer | 否 | 80 | 镜像大小。必须确保系统盘空间≥文件系统空间。取值范围： N=1时，即系统盘：5~500 GiB。 N=2~17时，即数据盘：5~1000 GiB。 导入镜像时，系统自动检测镜像大小，以检测结果为准。 |
| DiskDeviceMappi ng.N.Device | String | 否 | null | 指定DiskDeviceMapping.N.Device在自定义镜像中的设备名。 说明该参数即将停止使用，为提高代码兼容性，建议您尽量不要使用该参数。 |
| ImageName | String | 否 | ImageTestName | 镜像名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http://和https://开头。可以包含数字、半角冒号（:）、下划线（ ）或者短划线（-）。 _ 默认值：空。 |
| Description | String | 否 | TestDescription | 镜像的描述信息。长度为2~256个英文或中文字符，不能以http://和https://开头。 默认值：空。 |
| Architecture | String | 否 | x86 64 _ | 系统架构。取值范围： i386。 arm64。 x86 64。 _ 默认值：x86 64。 _ |
| OSType | String | 否 | linux | 操作系统平台类型。取值范围： windows。 linux。 默认值：linux。 |

云服务器ECS

| Platform | String | 否 | Aliyun | 系统平台。取值范围： CentOS。 Ubuntu。 SUSE。 OpenSUSE。 Debian。 CoreOS。 Aliyun。 Windows Server 2003。 Windows Server 2008。 Windows Server 2012。 Windows Server 2016。 Windows Server 2019。 Windows Server 2022。 Others Linux。 默认值：Others Linux。 |
|---|---|---|---|---|
| BootMode | String | 否 | BIOS | 配置镜像的启动模式。取值范围： BIOS：BIOS启动模式。 UEFI：UEFI启动模式。 默认值：BIOS。如果 Architecture=arm64 ，则该参数默认值为UEFI，且只能设置为UEFI。 说明您需要了解指定的镜像支持的启动模式，当通过该参数修改启动模式后，必须与镜像本身支持的启动模式匹配，实例才能正常启动。 |
| RoleName | String | 否 | AliyunECSImageI mportDefaultRole | 导入镜像时，使用的RAM角色名称。 |
| LicenseType | String | 否 | Auto | 导入镜像后，激活操作系统采用的许可证类型。取值范围： Auto（默认）：由阿里云检测源操作系统并分配许可证。自动模式下，系统优先搜索您设置的 Platform 是否有阿里云官方渠道的许可证并分配给导入的镜像， 如果缺乏该类许可，会切换成 BYOL（Bring Your Own License）方式。 Aliyun：根据您设置的 Platform 采用阿里云官方渠道的许可证。 BYOL：源操作系统自带的许可证。采用 BYOL时，您必须确保您的许可证密钥支持在阿里云使用。 |
| Tag.N.Key | String | 否 | TestKey | 镜像的标签键。N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 128个字符，不能以aliyun和acs:开头，不能包含http://或者https://。 |

云服务器ECS

| Tag.N.Value | String | 否 | TestValue | 镜像的标签值。N的取值范围：1~20。一旦传入该值，允许为空字符串。最多支持128 个字符，不能以acs:开头，不能包含http:// 或者https://。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ImageId | String | m- bp67acfmxazb4p*** * | 镜像ID。 |
| RegionId | String | cn-qingdao-env17- d01 | 地域ID。 |
| RequestId | String | C8B26B44-0189- 443E-9816- D951F59**** | 请求ID。 |
| TaskId | String | t- bp67acfmxazb4p*** * | 导入镜像任务ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-**** &DiskDeviceMapping.1.Format=qcow2 &DiskDeviceMapping.1.OSSBucket=ecsimageos &DiskDeviceMapping.1.OSSObject=CentOS_5.4_32.raw &DiskDeviceMapping.1.DiskImageSize=80 &ImageName=Test &Description=Test &Architecture=x86_64 &OSType=linux &Platform=Aliyun &LicenseType=Aliyun
```

正常返回示例 `XML` 格式

```xml
      <RequestId>C8B26B44-0189-443E-9816-D951F59*****</RequestId>
      <ImageId>m-bp67acfmxazb4p****</ImageId>
      <RegionId>cn-qingdao-env17-d01</RegionId>
      <TaskId>t-bp67acfmxazb4p****</TaskId>
```

`JSON` 格式云服务器ECS

```json
{
        "RequestId": "C8B26B44-0189-443E-9816-D951F59*****",
        "ImageId": "m-bp67acfmxazb4p****",
        "RegionId": "cn-qingdao-env17-d01",
        "TaskId": "t-bp67acfmxazb4p****"
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidImageName. Malformed | The specified Image name is wrongly formed. | 镜像名称格式错误。长度为2~128个字符。必须以大小字母或中文开头， 不能以aliyun和acs:开头，不能包含 http://或者https://。可以包含数字、半角句号（.）、半角冒号 （:）、下划线（ ）或者短划线 _ （-）。 |
| 400 | InvalidOSSObject.M alformed | The specified OSS object is wrongly formed. | 指定的 OSS Object 不合法。 |
| 400 | InvalidDescription.M alformed | The specified Image description is wrongly formed. | 镜像描述格式错误。 |
| 400 | InvalidArchitecture. Malformed | The specified Architecture is wrongly formed. | 参数 Architecture 格式错误。 |
| 400 | InvalidPlatform.Malf ormed | The specified Platform is wrongly formed. | 指定的镜像操作系统发行版不合法。 |
| 400 | InvalidOSType.Malfo rmed | The specified OSType is wrongly formed. | 格式不对。 |
| 400 | InvalidImageName. Duplicated | The destination image is exist. | 指定的镜像名已存在。 |
| 400 | InvalidImageSize | %s | 镜像大小不符合要求。 |
| 400 | InvalidDataDiskSize | The specified DiskDeviceMapping.N.DiskImSiz e should be in the specified range. | 指定的 DiskDeviceMapping.N.DiskImSiz e 超出取值范围。 |
| 400 | InvalidImageFormat. Malformed | The specified Image Format is wrongly formed. | 指定的镜像格式错误。 |
| 400 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 400 | InvalidRegion.NotSu pport | The specified region does not support image import or export. | 指定的地域暂时不支持此操作。 |
| 403 | ImageIsImporting | The specified Image is importing. | 指定镜像正在导入，无法执行操作。 |
| 403 | QuotaExceed.Image | The Image Quota exceeds. | 自定义镜像额度已用完。 |

云服务器ECS

| 403 | ImportImageFailed | Importing image is failed, Please contact the administrator. | 导入镜像失败，请联系系统管理员排查。 |
|---|---|---|---|
| 403 | UserNotInTheWhiteL ist | The user is not in the white list of importing image. | 用户未被授权导入镜像。 |
| 403 | NoSetRoletoECSSer viceAcount | ECS service account Have no right to access your OSS.please attach a role of access your oss to ECS service account. | ECS 官网服务账号没有权限访问您指定的 OSS 的 bucket 和 Object。 |
| 400 | InvalidOSSBucket.N otFound | The specified OSS bucket does not exist in this region. | 指定的 bucket 不存在。 |
| 403 | MissingParameter.Di skDeviceMapping | The specified parameter DiskDeviceMapping is not supplied. | 参数 DiskDeviceMapping 不能为空。 |
| 400 | InvalidOSSObject.No tFound | The specified OSS object does not exist in this region. | 指定的 OSS object 不存在。 |
| 400 | InvalidOSSObject.No tFound | The specified OSS object cannot be retrieved. | 指定的 OSS 对象无法检索。 |
| 403 | InvalidOSS.NotAuth orized | The specified OSS bucket or object is not allowed to access | 您没有权限访问指定的OSS的bucket 和Object。 |
| 400 | InvalidOSSBucket.N otMatched | The specified OSS bucket is incorrect, %s. | 指定的 OSS Bucket 有误，具体信息请参见错误信息的实际返回结果。 |
| 400 | InvalidLicenseType. NotSupported | The specified LicenseType is not supported | 指定的许可证类型不支持。 |
| 400 | InvalidLicenseType. BYOLOnly | Only BYOL LicenseType is supported for the current platform provided | 当前提供的平台仅支持BYOL类型的许可证。 |

##### ExportImage

调用ExportImage导出一份自定义镜像到与该自定义镜像同一地域的OSS Bucket里。

**接口说明**

支持导出镜像中包括数据盘快照的信息的自定义镜像，其中数据盘数不能超过4块，单块数据盘容量最大不能超过500 GiB。 导出镜像前，您必须通过RAM授权云服务器ECS官方服务账号写入OSS的权限：
1. 创建角色： `AliyunECSImageExportDefaultRole` （其他任何角色名称无效），为该角色设置以下角色策
略： 云服务器ECS

```json
         {
           "Statement": [
             {
               "Action": "sts:AssumeRole",
               "Effect": "Allow",
               "Principal": {
                 "Service": [
                   "ecs.aliyuncs.com"
```

]

```
               }
             }
```

`],`

```json
           "Version": "1"
         }
```

| 角色 | AliyunECSImageExportDefaultRole |  |
|---|---|---|
| AliyunECSImageExportRolePolicy |  | ，该策 |

```json
         {
           "Version": "1",
           "Statement": [
             {
               "Action": [
                 "oss:GetObject",
                 "oss:PutObject",
                 "oss:DeleteObject",
                 "oss:GetBucketLocation",
                 "oss:GetBucketInfo",
                 "oss:AbortMultipartUpload",
                 "oss:ListMultipartUploads",
                 "oss:ListParts"
```

`],`

```json
               "Resource": "*",
               "Effect": "Allow"
             }
```

]

```
         }
```

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ExportImage | 系统规定参数。取值：ExportImage |
| ImageId | String | 是 | m- bp67acfmxazb4p **** | 自定义镜像ID。 |
| OSSBucket | String | 是 | testexportImage | 保存导出镜像的OSS bucket。 |

云服务器ECS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 自定义镜像的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
|---|---|---|---|---|
| OSSPrefix | String | 否 | EcsExport | 您的OSS Object的前缀。可以由数字或者字母组成，字符长度为1~30。 |
| ImageFormat | String | 否 | raw | 镜像文件的导出格式。取值范围： raw vhd qcow2 vmdk vdi 默认值：raw。 |
| RoleName | String | 否 | EcsServiceRole- EcsDocGuideTest | 导出镜像时使用的RAM角色名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RegionId | String | cn-qingdao-env17- d01 | 地域ID。 |
| RequestId | String | C8B26B44-0189- 443E-9816- D951F59623A9 | 请求ID。 |
| TaskId | String | tsk- bp67acfmxazb4p*** * | 导出镜像任务ID。 |

**示例**

请求示例

```
&ImageId=m-bp67acfmxazb4p**** &RegionId=cn-qingdao-env17-d01 &OSSPrefix=EcsExport &ImageFormat=raw
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>C8B26B44-0189-443E-9816-D951F59623A9</RequestId>
      <TaskId>tsk-bp67acfmxazb4p****</TaskId>
      <RegionId>cn-qingdao-env17-d01</RegionId>
```

云服务器ECS `JSON` 格式

```json
{
    "RequestId": "C8B26B44-0189-443E-9816-D951F59623A9",
    "TaskId": "tsk-bp67acfmxazb4p****",
    "RegionId": "cn-qingdao-env17-d01"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | An input parameter "RegionId" that is mandatory for processing the request is not supplied. | 参数RegionId不得为空。 |
| 400 | MissingParameter | An input parameter "ImageId" that is mandatory for processing the request is not supplied. | 参数ImageId不得为空。 |
| 400 | MissingParameter | An input parameter "OSSBucket" that is mandatory for processing the request is not supplied. | 参数OSSBucket不得为空。 |
| 400 | InvalidImageName. Malformed | The specified Image name is wrongly formed. | 镜像名称不合法。长度为2~128个字符，以英文字母或中文开头，可包含数字，点号（.），下划线（ ）或连 _ 字符（-）。 不能以http://和https:// 开头。 |
| 400 | InvalidOSSPrefix.Mal formed | The specified OSSPrefix format is wrongly formed. | 参数OssPrefix格式错误。 |
| 400 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域ID不存在。 |
| 400 | InvalidRegion.NotSu pport | The specified region does not support image import or export. | 指定的地域暂时不支持此操作。 |
| 404 | InvalidImageId.NotF ound | The specified ImageId does not exist. | 指定的镜像在该用户账号下不存在， 请您检查镜像ID是否正确。 |
| 400 | IncorrectImageStatu s | The specified Image is not available. | 指定的源镜像状态不正确。 |
| 403 | ImageNotSupported | The specified image from the image market, do not support export image. | 指定的镜像来自镜像市场，此镜像不能导出。 |
| 400 | InvalidImageFormat. Malformed | The specified Image Format is wrongly formed. | 指定的镜像格式错误。 |
| 403 | ImageIsExporting | The specified Image is exporting. | 正在导出指定的镜像中。 |
| 403 | ExportImageFailed | Exporting image is failed, Please contact the administrator. | 导出镜像失败，请联系系统管理员。 |
| 403 | UserNotInTheWhiteL ist | The user is not in the white list of exporting image. | 该用户不在导出镜像白名单中。 |

云服务器ECS

| 403 | NoSetRoletoECSSer viceAcount | ECS service account Have no right to access your OSS.please attach a role of access your oss to ECS service account. | ECS官网服务账号没有权限访问您指定的OSS的bucket和Object。 |
|---|---|---|---|
| 400 | InvalidOSSBucket.N otFound | The specified OSS bucket does not exist in this region. | 指定的bucket不存在。 |
| 400 | OperationDenied | The specified image contains the snapshot of the data disk,does not support this operation. | 包含了数据盘快照的镜像，不支持此操作。 |
| 400 | InvalidImage.DiskA mountOrSize | %s | 无效的镜像，导出的镜像限制数据盘数不能超过4块，单块数据盘容量最大不能超过500GiB。 |
| 400 | ImageNotSupported | The specified Image contains encrypted snapshots, do not support export. | 指定的镜像包含了加密快照，不支持导出。 |
| 400 | ImageNotSupported | Image from image market does not support exporting. | 不支持导出镜像市场里的镜像。 |
| 403 | ConcurrentQuotaEx ceed.ExportImage | %s | 当前处理中的任务，已达到并发最大额度，请耐心等待一段时间再创建任务。 |
| 403 | WeeklyQuotaExceed .ExportImage | %s | 本周提交任务已经超出配额，请耐心等候再次分配可用额度。 |

##### DescribeImageSupportInstanceTypes

调用DescribeImageSupportInstanceTypes查询指定镜像支持的实例规格。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeImageSu pportInstanceTyp es | 系统规定参数。取值： DescribeImageSupportInstanceTypes |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ImageId | String | 否 | m- o6w3gy99qf89rk ga**** | 镜像ID。 |
| ActionType | String | 否 | CreateEcs | 实例规格需要使用到的场景。取值范围： CreateEcs（默认）：创建实例 Upgrade：升级实例规格 Downgrade：降级实例规格 |

云服务器ECS

| Filter.N.Key | String | 否 | imageId | 指定过滤条件Key，当前只支持过滤镜像 ID，取值范围： imageId：过滤条件为镜像ID filter：过滤条件为镜像ID |
|---|---|---|---|---|
| Filter.N.Value | String | 否 | m- o6w3gy99qf89rk ga**** | 指定过滤条件Value。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ImageId | String | m- o6w3gy99qf89rkga* *** | 查询的镜像ID。 |
| InstanceTypes | Array |  | 由InstanceTypeItemType组成的实例规格集合。 |
| InstanceType |  |  |  |
| CpuCoreCount | Integer | 1 | 实例规格的vCPU内核数目。 |
| InstanceTypeFa mily | String | ecs.t1 | 实例规格族。 |
| InstanceTypeId | String | ecs.t1.xsmall | 镜像支持的实例规格ID。 |
| MemorySize | Float | 1024 | 实例规格的内存大小，单位GiB。 |
| RegionId | String | cn-qingdao-env17- d01 | 镜像所属地域ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeImageSupportInstanceTypes &RegionId=cn-qingdao-env17-d01 &ImageId=m-o6w3gy99qf89rkga****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
<DescribeImageSupportInstanceTypesResponse>
      <RequestId>CF661E2D-4AFE-4BCD-959A-A65E14416B44</RequestId>
      <RegionId>cn-qingdao-env17-d01</RegionId>
      <ImageId>ubuntu_16_0402_64_20G_alibase_20180409.vhd</ImageId>
      <InstanceTypes>
            <InstanceType>
                  <InstanceTypeId>ecs.t1.xsmall</InstanceTypeId>
                  <CpuCoreCount>1</CpuCoreCount>
                  <MemorySize>0.5</MemorySize>
                  <InstanceTypeFamily>ecs.t1</InstanceTypeFamily>
            </InstanceType>
            <InstanceType>
                  <InstanceTypeId>ecs.t1.small</InstanceTypeId>
                  <CpuCoreCount>1</CpuCoreCount>
                  <MemorySize>1</MemorySize>
                  <InstanceTypeFamily>ecs.t1</InstanceTypeFamily>
            </InstanceType>
      </InstanceTypes>
</DescribeImageSupportInstanceTypesResponse>
```

`JSON` 格式

```json
{
    "RequestId": "CF661E2D-4AFE-4BCD-959A-A65E14416B44",
    "RegionId": "cn-qingdao-env17-d01",
    "ImageId": "ubuntu_16_0402_64_20G_alibase_20180409.vhd",
    "InstanceTypes": {
        "InstanceType": [{
            "InstanceTypeId": "ecs.t1.xsmall",
            "CpuCoreCount": 1,
            "MemorySize": 0.5,
            "InstanceTypeFamily": "ecs.t1"
        },
        {
            "InstanceTypeId": "ecs.t1.small",
            "CpuCoreCount": 1,
            "MemorySize": 1,
            "InstanceTypeFamily": "ecs.t1"
        }]
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParamter | Invalid Parameter | 指定的参数不合法。 |
| 404 | InvalidUsage | The specifed Usage is not valid | 指定有引用关系的资源类型 （image、disk、image disk、 _ none）不合法。 |
| 400 | InvalidInstanceType. ValueNotSupported | The specified InstanceType does not exist or beyond the permitted range. | 您指定的实例规格不存在，或者您没有权限操作此规格的实例。 |

云服务器ECS

#### 网络

##### ModifyInstanceNetworkSpec

调用ModifyInstanceNetworkSpec修改ECS实例的带宽配置。当实例现有网络规格不满足要求时，可以通过修改实例的带宽配置提高网络性能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyInstanceNe tworkSpec | 系统规定参数，取值： ModifyInstanceNetworkSpec。 |
| InstanceId | String | 是 | i- bp67acfmxazb4p h*** | 需要修改网络配置的实例ID。 |
| InternetMaxBand widthOut | Integer | 否 | 10 | 网络出带宽最大值，单位： Mbit/s（Megabit per second）。取值范围：0~100。 |
| InternetMaxBand widthIn | Integer | 否 | 10 | 设置网络入带宽最大值，单位： Mbit/s（Megabit per second）。取值范围： 当网络出带宽小于等于10Mbit/s时： 1~10，默认为10。 当网络出带宽大于10Mbit/s时： 1~ InternetMaxBandwidthOut 的取值，默认为 InternetMaxBandwidthOut 的取值。 |
| AllocatePublicIp | Boolean | 否 | false | 说明该参数暂未支持。 |
| StartTime | String | 否 | 2017-12- 05T22:40Z | 临时带宽升级开始时间。按照ISO8601标准表示，并使用UTC+0时间，格式为yyyy- MM-ddThh:mmZ。精确到分钟（mm）。 |
| EndTime | String | 否 | 2017-12-06T22Z | 临时带宽升级结束时间。按照ISO8601标准表示，并使用UTC+0时间，格式为yyyy- MM-ddThhZ。精确到小时（hh）。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见《云服务器ECS开发指南》中的如何保证幂等性章节。 |

**返回数据**

云服务器ECS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| OrderId | String | 0 | 说明该参数暂未支持。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyInstanceNetworkSpec &InstanceId=i-bp67acfmxazb4ph**** &InternetMaxBandwidthOut=10 &ClientToken=123e4567-e89b-12d3-a456-426655440000
```

正常返回示例 `XML` 格式

```xml
        <RequestId>04F0F334-1335-436C-A1D7-6C044FE73368</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368",
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 400 | InvalidInternetMaxB andwidthIn.ValueNo tSupported | The specified InternetMaxBandwidthIn is beyond the permitted range. | 指定的公网入方向最大带宽超出允许值。 |
| 400 | InvalidInternetMaxB andwidthOut.ValueN otSupported | The specified InternetMaxBandwidthOut is beyond the permitted range. | 指定的公网出方向最大带宽超出允许值。 |
| 403 | IncorrectInstanceSta tus | The current status of the instance does not support this operation. | 当前实例状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 403 | InstanceExpiredOrIn Arrears | The specified operation is denied as your prepay instance is expired (prepay mode) or in arrears (afterpay mode). | 包年包月实例已过期，请您续费后再进行操作。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
|---|---|---|---|
| 403 | ChargeTypeViolatio n | The operation is not permitted due to billing method of the instance. | 实例的计费方式不支持该操作。 |
| 403 | OperationDenied | The operation is denied due to the instance is PrePaid. | 包年包月的实例不支持此操作。 |
| 400 | OperationDenied | Specified instance is in VPC. | 指定实例存在于VPC。 |
| 400 | InvalidParameter.Ba ndwidth | %s | 指定的带宽无效，请检查参数是否正确。 |
| 400 | InvalidParameter.Co nflict | %s | 您输入的参数无效，请检查参数之间是否冲突。 |
| 400 | InvalidStartTime.Val ueNotSupported | %s | 结束时间不能早于开始时间。 |
| 400 | Account.Arrearage | Your account has an outstanding payment. | 您的账号存在未支付的款项。 |
| 400 | InvalidInternetCharg eType.ValueNotSup ported | The specified InternetChargeType is invalid. | 指定的参数InternetChargeType无效。 |
| 400 | DecreasedBandwidt hNotAllowed | %s | 降低带宽操作无效。 |
| 400 | BandwidthUpgradeD enied.EipBoundInsta nce | The specified VPC instance has bound EIP, temporary bandwidth upgrade is denied. | 该实例已经绑定EIP，不能进行临时升级。 |
| 400 | InvalidClientToken.V alueNotSupported | The ClientToken provided is invalid. | 指定的ClientToken不合法。 |
| 403 | InvalidAccountStatu s.NotEnoughBalance | Your account does not have enough balance. | 账号余额不足，请您先充值再进行该操作。 |
| 403 | InvalidInstance.UnP aidOrder | The specified Instance has unpaid order. | 指定的实例有未支付的订单，请您先支付再进行操作。 |
| 400 | Throttling | Request was denied due to request throttling, please try again after 5 minutes. | 您当前的请求被流控，请5分钟后重试。 |
| 400 | InvalidAction | Specified action is not valid. | 该操作无效。 |
| 400 | IpAllocationError | Allocate public ip failed. | 公网IP地址分配失败。 |
| 400 | InvalidParam.Allocat ePublicIp | The specified param AllocatePublicIp is invalid. | 指定的AllocatePublicIp无效。 |
| 400 | InstanceDowngrade. QuotaExceed | Quota of instance downgrade is exceed. | 您的实例降配已超额度，无法进行此操作。 |

云服务器ECS

| 400 | InvalidBandwidth.Va lueNotSupported | Instance upgrade bandwidth of temporary not allow less then existed. | 临时宽带升级带宽不能低于已有带宽。 |
|---|---|---|---|
| 403 | InvalidInstance.Insta nceNotSupported | The special vpc instance with eip not need bandwidth. | VPC类型实例绑定EIP后不需要指定公网带宽。 |
| 400 | InvalidInstanceStatu s | The specified instance status does not support this action. | 实例的当前状态不支持该操作。 |
| 403 | InvalidInstanceStatu s | The current status of the instance does not support this operation. | 当前实例的状态不支持此操作。 |
| 400 | InvalidInstance.UnP aidOrder | Unpaid order exists in your account, please complete or cancel the payment in the expense center. | 您的账号里有未支付的订单，请处理后重试。 |
| 400 | OperationDenied | After downgrade, you cannot upgrade or downgrade your instances again in the remaining time of the current billing cycle. | 降配后，您将无法在当前结算周期的剩余时间内再次升级或降级实例配置。 |
| 400 | InvalidInternetCharg eType.ValueNotSup ported | %s | 暂不支持指定的网络计费方式，请确认相关参数是否正确。 |
| 400 | LastOrderProcessing | The previous order is still processing, please try again later. | 订单正在处理中，稍后重试。 |
| 400 | OperationDenied | The current user does not support this operation. | 您使用的账号暂不支持此操作。 |
| 403 | NAT PUBLIC IP BIN _ _ _ DING FAILED _ | Binding nat public ip failed | 公网IP绑定网关失败。 |
| 403 | InvalidInstance.EipN otSupport | The specified instance with eip is not supported, please unassociate eip first. | 已绑定EIP的实例不支持该操作，请先解绑此EIP。 |
| 403 | InvalidNetworkType. ValueNotSupported | The specified parameter NetworkType is not valid. | 指定的网络类型不合法。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |

##### AttachClassicLinkVpc

调用AttachClassicLinkVpc将一台经典网络类型实例连接到专有网络VPC中，使经典网络类型实例可以和VPC 中的云资源私网互通。

**接口说明**

调用该接口时，您需要注意： 连接经典网络类型实例前，实例必须处于**运行中**（Running）或者**已停止**（Stopped）状态。 云服务器ECS 经典网络类型实例和VPC必须在同一个阿里云地域。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AttachClassicLink Vpc | 系统规定参数，取值： AttachClassicLinkVpc。 |
| InstanceId | String | 是 | i-test | 经典网络类型实例ID。您可以调用 DescribeInstances查看您可用的实例。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| VpcId | String | 是 | vpc-test | 开启ClassicLink的VPC ID。您可以调用 DescribeVpcs查看您可用的VPC。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=AttachClassicLinkVpc &RegionId=cn-qingdao-env17-d01 &InstanceId=i-test &VpcId=vpc-test
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

云服务器ECS

| 403 | InvalidInstanceId.No tFound | The InstanceId provided does not exist in our records. | 指定的实例不存在，请您检查实例ID 是否正确。 |
|---|---|---|---|
| 403 | InvalidRegionId.Malf ormed | The specified parameter ? RegionId? is not valid. | 指定的 RegionId 不合法。 |
| 403 | InvalidVpcId.Malfor med | The specified parameter ?VpcId? is not valid. | 指定的 VpcId 不合法。 |
| 403 | InvalidInstanceId.Ma lFormed | The specified instance is not a classic network instance. | 指定的实例不是经典网络实例。 |
| 403 | OperationDenied | The instance does not allow link to vpc. | 该实例已链接到其他VPC。 |
| 403 | InvalidParameter.In validInstanceIdAndV pcId | The parameter InstanceId and VpcId are not allowed to be empty at the same time. | 至少指定一个InstanceId或VpcId。 |
| 403 | OperationDenied | The specified vpc is disabled attach classic link. | 指定的VPC网络禁止创建classicLink 链接。 |
| 403 | InvalidInstanceId.No tFound | The specified instance does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | InvalidStatus.Instan ceStatus | The specified instance status is not support this operation ,expect status is running or shutted. | 指定的实例状态不支持此操作，期望的操作状态是Running或者 Stopped。 |
| 403 | InvalidStatus.Instan ceStatus | The specified instance status is not support this operation, expect status is running or shutted. | 指定的实例状态不支持此操作，期望的操作状态是Running或者 Stopped。 |
| 403 | InvalidInstanceId.No tBelong | The specified instance is not belong to you. | 指定的实例不在您账号下。 |
| 403 | QuotaExceeded | The link quota exceeded in this vpc. | 已达到指定的VPC网络创建链接的配额。 |
| 403 | InvalidStatus.Instan ceLocked | The specified instance is locked,please wait more. | 指定的实例被锁定，请等待解锁后再操作。 |
| 403 | InvalidInstanceId.Li mitedRegion | The specified instance does not support this operation due to the limitation of its region. | 指定的实例受区域的限制，不支持此操作。 |
| 403 | Forbidden.SubUser | User not authorized to operate on the specified resource. | 您当前的子账号没有操作此资源的权限。 |

##### ModifyInstanceSpec

调用ModifyInstanceSpec调整一台ECS实例的实例规格和网络带宽大小。

**接口描述**

调用该接口时，您需要注意： 实例状态必须为运行中（Running）或者已停止（Stopped）时才能调节网络带宽大小。 升级或者降低实例规格前，您可以通过DescribeResourcesModification查询当前实例支持变配的实例规格。 实例状态必须为已停止（Stopped）时才能变更实例规格。 云服务器ECS 单次只能升级单项配置，即单次只能修改实例规格，或者只能调整网络带宽大小。 单台实例每成功操作一次，5分钟内不能继续操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ModifyInstanceSpec | 接口名称。对于您自行拼凑 HTTP/HTTPS URL发起的API 请求，Action为必选参数。取值：ModifyInstanceSpec。 |
| InstanceId | String | Query | 是 | i-bp67acfmxazb4ph*** | 指定的实例ID。 |
| InstanceTy pe | String | Query | 否 | ecs.g5.large | 实例的目标规格。可以调用 DescribeInstanceTypes接口获得最新的规格表。 |
| InternetMa xBandwidt hOut | Intege r | Query | 否 | 10 | 网络出带宽最大值，单位为 Mbit/s（Megabit per second）。取值范围： 0~100。 |
| InternetMa xBandwidt hIn | Intege r | Query | 否 | 10 | 网络入带宽最大值，单位为 Mbit/s（Megabit per second）。取值范围： 当网络出带宽小于等于 10Mbit/s时：1~10，默认为10。 当网络出带宽大于 10Mbit/s时： 1~InternetMaxBandwid thOut的取值，默认为 InternetMaxBandwidth Out的取值。 |
| Temporary .StartTime | String | Query | 否 | 2017-12-05T22:40:00Z | 临时提升带宽的起始时间点。 按照ISO 8601标准表示，并使用UTC +0时间，格式为 yyyy-MM- ddTHH:mm:ssZ。 |
| Temporary .EndTime | String | Query | 否 | 2017-12-05T22:40:00Z | 临时提升带宽的截止时间点。 按照ISO 8601标准表示，并使用UTC +0时间，格式为 yyyy-MM- ddTHH:mm:ssZ。 |
| Temporary .InternetM axBandwid thOut | Intege r | Query | 否 | 50 | 临时网络出带宽的最大值。取值范围：1~100。 说明为提高兼容性，请尽量使用其他参数。 |

|  | 开发指南·API参 | 考 |  |  |  | 云服务器EC | S |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Async | Boole an | Query | 否 | false | 是否提交异步请求。 默认值：false。 |
| AllowMigra teAcrossZo ne | Boole an | Query | 否 | false | 是否支持跨集群升级实例规格。 默认值：false。 当参数 AllowMigrateAcrossZone 取值为true时，一旦您根据返回信息升级了云服务器，请留意以下注意事项： 经典网络类型实例： 对于已停售的实例规格，非I/O优化实例变配到I/O优化实例时，实例私网IP地址、磁盘设备名和软件授权码会发生变化。对于Linux实例， 普通云盘（cloud）会被识别为xvda或者xvdb 等，高效云盘 （cloud efficiency） _ 和SSD云盘 （cloud ssd）会被识 _ 别为vda或者vdb等。 对于正常售卖的实例规格族，实例的私网IP地址会发生变化。 专有网络VPC类型实例： 对于已停售的实例规格， 非I/O优化实例变配到I/O优化实例时，云服务器磁盘设备名和软件授权码会发生变化。 Linux实例的普通云盘 （cloud）会被识别为 xvda或者xvdb等，高效云盘（cloud efficiency） _ 和SSD云盘（cloud ssd） _ 会被识别为vda或者vdb 等。 |
| SystemDis k.Category | String | Query | 否 | cloud ssd _ | 更换系统盘类型。该参数只有在从已停售的实例规格升级到正常售卖的实例规格族，并将非I/O优化实例规格升级为I/O 优化实例规格时有效。取值范围： cloud efficiency：高效 _ 云盘。 cloud ssd：SSD云盘。 _ |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClientToke n | String | Query | 否 | 0c593ea1-3bea-11e9- b96b-88e9fe6***** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多详情，请参见《云服务器 ECS开发指南》中的如何保证幂等性章节。 |
| ModifyMod e | String | Query | 否 | Online | 修改方式，可选值： Online Offline |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyInstanceSpec &InstanceId=i-bp67acfmxazb4ph***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

`XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInternetCharg eType.ValueNotSup ported | The specified InternetChargeType is not valid. | 暂不支持指定的网络付费类型的实例，请确认相关参数是否正确。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInstanceType. ValueUnauthorized | The specified InstanceType does not exist or beyond the permitted range. | 您指定的实例规格不存在，或者您没有权限操作此规格的实例。 |
| 400 | InvalidInstanceType. ValueUnauthorized | The specified InstanceType is not authorized. | 指定的实例规格未授权使用。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 400 | InvalidInstanceType. ValueNotSupported | The specified InstanceType does not exist or beyond the permitted range. | 您指定的实例规格不存在，或者您没有权限操作此规格的实例。 |
| 400 | InvalidParameter | The specified parameter "InternetMaxBandwidthOut" is not valid. | 指定的InternetMaxBandwidthOut 参数不合法。 |
| 400 | InvalidParameter.Mi smatch | Too many parameters in one request. | 请求中包含的参数过多。 |
| 403 | CategoryViolation | The specified instance does not support this operation because of its disk category. | 挂载有本地磁盘的实例不支持升降配。 |
| 403 | InvalidStatus.ValueN otSupported | The current status of the resource does not support this operation. | 当前资源的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | InvalidAccountStatu s.NotEnoughBalance | Your account does not have enough balance. | 账号余额不足，请您先充值再进行该操作。 |
| 403 | ChargeTypeViolatio n | The operation is not permitted due to charge type of the instance. | 付费方式不支持该操作，请您检查实例的付费类型是否与该操作冲突。 |
| 403 | OperationDenied | The specified instance is out of usage. | 指定的实例库存不足。 |
| 400 | BandwidthUpgradeD enied.EipBoundInsta nce | The specified VPC instance has bound EIP, temporary bandwidth upgrade is denied. | 该实例已经绑定EIP，不能进行临时升级。 |
| 404 | MissingTemporary.S tartTime | Temporary.StartTime is not specified. | 未指定临时升级开始时间。 |
| 404 | MissingTemporary.E ndTime | Temporary.EndTime is not specified. | 未指定临时升级结束时间。 |
| 400 | InvalidTemporary.St artTime | The specifed Temporary.StartTime is not valid. | 指定的临时升级开始时间无效。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTemporary.En dTime | The specifed Temporary.EndTime is not valid. | 指定的临时升级结束时间无效。 |
| 403 | LastTokenProcessin g | The last token request is processing. | 正在处理上一条令牌请求，请您稍后再试。 |
| 400 | Downgrade.NotSupp orted | Downgrade operation is not supported. | 不支持降配。 |
| 403 | InstanceSpecModific ation.NotEffective | The specified instance has been reserved for making a spec modification and not taken effective in the current contract period. | 指定的实例因规格调整被保留，在当前合同期内无法生效。 |
| 400 | DependencyViolatio n.InstanceType | The current InstanceType cannot be changed to the specified InstanceType. | 当前实例的规格不能变更到指定的规格。 |
| 403 | InvalidInstanceType. ValueNotSupported | The specified zone does not offer the specified instancetype. | 指定的区域不提供此类型的实例。 |
| 403 | ImageNotSupportIns tanceType | The specified image do not support the InstanceType instance. | 指定的镜像不支持此类实例规格。 |
| 400 | Account.Arrearage | Your account has an outstanding payment. | 您的账号存在未支付的款项。 |
| 400 | InvalidParameter.Ba ndwidth | The specified parameter Bandwidth is not valid. | 指定的Bandwidth不合法。 |
| 400 | InvalidParameter.Co nflict | The specified image does not support the specified instance type. | 指定的镜像不能用于指定的实例规格。 |
| 400 | InvalidParameter.All owMigrateAcrossZo ne | The specified parameter CanMigrateAcrossZone is not valid. | 指定的参数 CanMigrateAcrossZone无效。 |
| 400 | InvalidParam.Syste mDiskCategory | The specified param SystemDisk.Category is not valid. | 指定的系统盘类型参数无效。 |
| 400 | Throttling | Request was denied due to request throttling, please try again after 5 minutes. | 您当前的请求被流控，请5分钟后重试。 |
| 400 | InvalidInstanceStatu s.NotStopped | The specified Instance status is not stopped. | 指定实例的状态不是已停止。 |
| 403 | InstanceType.Offline | The specified InstanceType has been offline | 您指定的实例规格已下线，请选择其它规格的实例。 |
| 400 | InvalidAction | Specified action is not valid. | 该操作无效。 |
| 400 | IdempotenceParam NotMatch | There is a idempotence signature mismatch between this and last request. | 该请求与上一个请求的ClientToken 参数一致，但其它请求参数不一致。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidClientToken.V alueNotSupported | The ClientToken provided is invalid. | 指定的ClientToken不合法。 |
| 400 | Price.PricePlanResul tNotFound | The internetMaxBandwidthIn or internetMaxBandwidthOut provided is invalid. | 提供的internetMaxBandwidthIn或 internetMaxBandwidthOut无效。 |
| 403 | InvalidParameter.No tMatch | %s | 您输入的参数无效，请检查参数之间是否冲突。 |
| 403 | InvalidInstance.EipN otSupport | The specified instance with eip is not supported, please unassociate eip first. | 已绑定EIP的实例不支持该操作，请先解绑此EIP。 |
| 400 | InvalidAction.NotSu pport | The ecs on dedicatedHost not support modify instanceType. | 专用宿主机上的实例不支持变更实例规格。 |
| 400 | InvalidMarketImage Status.NotSupporte d | The status of specified market image does not support this operation. | 指定的市场镜像的状态不支持该操作。 |
| 403 | OperationDenied.No Stock | The resource is out of usage. | 该实例不在运行状态，请您启动实例或检查操作是否合理。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | OperationDenied.Un paidOrder | The specified instance has unpaid order. | 指定的实例ID已存在未支付订单，您可以登录ECS管理控制台支付。 |
| 403 | OperationDenied | %s | 拒绝操作。 |
| 403 | InvalidOperation.Ipv 4CountExceeded | %s | IPv4数量达到上限，导致该操作无效。 |
| 403 | InvalidOperation.Ipv 6CountExceeded | %s | IPv6数量达到上限，导致该操作无效。 |
| 403 | InvalidOperation.Ipv 6NotSupport | %s | IPv6不支持当前操作。 |
| 403 | InvalidOperation.Ins tanceWithEipNotSup port | The special instance with eip not support operate, please unassociate eip first. | 已绑定EIP的实例不支持该操作，请优先解绑EIP。 |
| 403 | SecurityRisk.3DVerif ication | We have detected a security risk with your default credit or debit card. Please proceed with verification via the link in your email. | 我们检测到您的默认信用卡或借记卡存在安全风险。请通过电子邮件中的链接进行验证。 |
| 404 | InvalidInstanceChar geType.NotFound | The InstanceChargeType does not exist in our records | 指定的实例计费方式不存在。 |
| 403 | InvalidInstance.NotF oundSystemDisk | The specified instance has no system disk. | 指定的实例没有挂载系统盘。请确保指定的实例已挂载了系统盘。您可以调用DescribeInstances查询指定实例的信息。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidInstanceType. NotSupportDiskCate gory | The instanceType of the specified instance does not support this disk category. | 指定的实例规格（InstanceType） 不支持当前实例的云盘类别。请尝试更换其它实例规格。关于实例规格支持的云盘类型，请参见实例规格族文档。 |
| 403 | QuotaExceed.Elastic Quota | No additional quota is available for the specified ECS instance type. | 您在当前地域选择的实例规格所要创建的台数超出系统限额，您可以选择其他地域、实例规格或减少台数重新购买，也可以前往ECS管理控制台或配额中心申请提高限额。 |
| 403 | QuotaExceed.Elastic Quota | The number of the specified ECS instances has exceeded the quota of the specified instance type. | 您在当前地域选择的实例规格所要创建的台数超出系统限额，您可以选择其他地域、实例规格或减少台数重新购买，也可以前往ECS管理控制台或配额中心申请提高限额。 |
| 403 | QuotaExceed.Elastic Quota | The number of vCPUs assigned to the ECS instances has exceeded the quota in the zone. | 您的全实例规格vCPU配额超出系统限额，您可以前往ECS管理控制台或配额中心申请提高限额。 |
| 403 | QuotaExceed.Elastic Quota | The number of the specified ECS instances has exceeded the quota of the specified instance type, or the number of vCPUs assigned to the ECS instances has exceeded the quota in the zone. | 您在当前地域选择的实例规格所要创建的台数超出系统限额，或者全实例规格vCPU配额超出系统限额，您可以前往ECS管理控制台或配额中心申请提高限额。 |
| 400 | InvalidOperation.Vp cHasEnabledAdvanc edNetworkFeature | The specified vpc has enabled advanced network feature. | 该VPC开启了高阶特性，不能创建低规格的ECS。 |
| 403 | InvalidOperation.Ins tanceTypeNotSuppo rtEniTrunking | %s | 不支持本次操作。具体信息请参见错误信息%s占位符的实际返回值。 |
| 403 | InvalidOperation.Ma xEniQueueNumberE xceeded | %s | 弹性网卡队列数超过上限，具体信息请参见错误信息%s占位符的实际返回结果。 |
| 403 | InvalidOperation.Exc eedInstanceTypeQu eueNumber | %s | 弹性网卡队列总数超过上限，具体信息请参见错误信息%s占位符的实际返回结果。 |
| 403 | InvalidParameter.In validEniQueueNumb er | %s | 弹性网卡队列数有误，具体信息请参见错误信息%s占位符的实际返回结果。 |
| 400 | Invalid.PrivatePoolO ptions.MatchCriteria | Target mode does not support this operation. | Target模式不支持本次操作。 |

##### DescribeClassicLinkInstances

调用DescribeClassicLinkInstances查询一台或多台与专有网络 VPC 建立了连接的经典网络类型实例。

**接口说明**

调用该接口时，您需要注意： 云服务器ECS 该接口仅支持经典网络类型实例。 单次最多只能查询100台经典网络类型实例。 参数VpcId和InstanceId不能同时为空。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeClassicLi nkInstances | 系统规定参数，取值： DescribeClassicLinkInstances。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| VpcId | String | 否 | vpc-tes**** | VPC ID。目标VPC必须已开启ClassicLink 功能。 |
| InstanceId | String | 否 | i-tes**** | 实例ID。最多指定100台实例ID，并使用半角逗号（,）隔开。 |
| PageNumber | String | 否 | 1 | 当前页码。起始值：1。 默认值：1 。 |
| PageSize | String | 否 | 10 | 分页查询时设置的每页行数。取值范围： 1~100。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Links | Array |  | 返回经典网络类型实例和VPC连接信息。 |
| Link |  |  |  |
| InstanceId | String | i-tes**** | 实例ID。 |
| VpcId | String | vpc-tes**** | VPC ID。 |
| PageNumber | Integer | 1 | 连接列表的页码。 |
| PageSize | Integer | 10 | 输入时设置的每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

云服务器ECS

| TotalCount | Integer | 2 | 连接总数。 |
|---|---|---|---|

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeClassicLinkInstances &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-tes**** &InstanceId=i-tes****, i-tes****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>B154D309-F3E1-4AB7-BA94-FEFCA8B89001</RequestId>
      <TotalCount>2</TotalCount>
      <PageNumber>1</PageNumber>
      <PageSize>10</PageSize>
      <Links>
            <Link>
                  <InstanceId>i-tes****</InstanceId>
                  <VpcId>vpc-test</VpcId>
            </Link>
            <Link>
                  <InstanceId>i-tes****</InstanceId>
                  <VpcId>vpc-tes****</VpcId>
            </Link>
      </Links>
```

`JSON` 格式

```json
{
    "PageNumber":1,
    "Links":{
        "Link":[{
            "InstanceId":"i-tes****",
            "VpcId":"vpc-tes****"
            },
           {
           "InstanceId": "i-tes****",
           "VpcId": "vpc-tes****"
           }]
    },
    "TotalCount":2,
    "PageSize":10,
    "RequestId":"B154D309-F3E1-4AB7-BA94-FEFCA8B89001"
}
```

**错误码**

云服务器ECS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidInstanceId.No tFound | The InstanceId provided does not exist in our records. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | InvalidParameter.To ManyInstanceIds | No more than 100 InstanceIds can be specified. | 最多只能指定 100 个 InstanceId。 |
| 403 | InvalidParameter.In validInstanceIdAndV pcId | The parameter InstanceId and VpcId are not allowed to be empty at the same time. | 至少指定一个 InstanceId 或 VpcId。 |
| 403 | InvalidInstanceId.No tBelong | The specified instance is not belong to you. | 指定的实例不在您账号下。 |
| 403 | InvalidVpc.NotBelon g | The specified vpc is not belong to you. | 指定的VPC是不在您的账号下。 |

##### DetachClassicLinkVpc

调用DetachClassicLinkVpc取消一台经典网络类型ECS实例与专有网络VPC的连接（ClassicLink）。取消 ClassicLink后，经典网络类型实例无法与VPC互通。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DetachClassicLin kVpc | 系统规定参数。取值： DetachClassicLinkVpc |
| InstanceId | String | 是 | i- bp67acfmxazb4p **** | 经典网络类型实例ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| VpcId | String | 是 | vpc- bp67acfmxazb4p **** | 实例连接的VPC ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例云服务器ECS

```
https://ecs.example.com/?Action=DetachClassicLinkVpc &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-bp67acfmxazb4p**** &InstanceId=i-bp67acfmxazb4p****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>C0003E8B-B930-4F59-ADC0-0E209A9012A8</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "C0003E8B-B930-4F59-ADC0-0E209A9012A8"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidInstanceId.No tFound | The InstanceId provided does not exist in our records. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | InvalidInstanceId.Ma lFormed | The specified instance is not a classic network instance. | 指定的实例不是经典网络实例。 |
| 403 | OperationDenied | The instances are not allowed to detach from the linked vpc. | 不允许将此实例与已连接的 VPC 分离。 |
| 403 | InvalidParameter.In validInstanceIdAndV pcId | The parameter InstanceId and VpcId are not allowed to be empty at the same time. | 至少指定一个 InstanceId 或 VpcId。 |
| 403 | InvalidInstanceId.No tFound | The specified instance does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 403 | InvalidStatus.Instan ceStatus | The specified instance status is not support this operation ,expect status is running or shutted. | 指定的实例状态不支持此操作，期望的操作状态是“running”或者“shutted”。 |
| 403 | InvalidInstanceId.No tBelong | The specified instance is not belong to you. | 指定的实例不在您账号下。 |
| 403 | Forbidden.SubUser | User not authorized to operate on the specified resource. | 您当前的子账号没有操作此资源的权限。 |
| 403 | InvalidStatus.Instan ceStatus | The specified instance status does not support this operation, expected status is Running or Stopped. | 指定的实例状态不支持此操作，期望的操作状态是“Running”或者“Stopped”。 |

#### 安全组

云服务器ECS

##### CreateSecurityGroup

调用API CreateSecurityGroup新建一个安全组。新建的安全组，默认只允许安全组内的实例互相访问，安全组外的一切通信请求会被拒绝。若您想允许其他安全组实例的通信请求，或者来自互联网的访问请求，需要授权安接口说明创建专有网络VPC类型的安全组时，您必须指定参数 `VpcId` 。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| Action | String | Query | 是 | CreateSecurityGroup | 系统规定参数。取值： CreateSecurityGro up 。 |  |  |
|  |  |  |  |  |  | CreateSecurityGro |  |
| RegionId | String | Query | 是 | cn-qingdao-**** | 安全组所属地域ID。您可以调用 DescribeRegions 查看最新的阿里云地域列表。 |  |  |
| Descriptio n | String | Query | 否 | SecurityGroupTestDescrip tion | 安全组描述信息。长度为 2~256个英文或中文字符， 不能以 http:// 或 https:/ / 开头。 默认值：空。 |  |  |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken 只支持ASCII字符，且不能超过64 个字符。更多详情，请参见 《云服务器ECS开发指南》中的如何保证幂等性章节。 |  |  |
| SecurityGr oupName | String | Query | 否 | SecurityGroupTestName | 安全组名称。长度为2~128 个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 或 https:/ / 开头。可以包含数字、半角冒号（:）、下划线（ ）或 _ 者短划线（-）。 默认值：空。 |  |  |
| VpcId | String | Query | 否 | vpc- bp1opxu1zkhn00gzv**** | 安全组所属VPC ID。 |  |  |

|  | up |
|---|---|

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

|  |  | http:// |
|---|---|---|
| ame | / |  |

| https:/ |  |
|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| SecurityGr oupType | String | Query | 否 | enterprise | 安全组类型，分为普通安全组与企业安全组。取值范围： normal：普通安全组。 enterprise：企业安全组。 |  |  |
| ResourceG roupId | String | Query | 否 | rg-bp67acfmxazb4p**** | 安全组所在的企业资源组ID。 |  |  |
| Tag | Repea tList | Query | 否 |  |  |  |  |
| -key | String |  | 否 |  | 安全组的标签键。 为提高兼容性，建议您尽量使用 Tag.N.Key 参数。 |  |  |
| -Key | String |  | 否 |  | 安全组的标签键。格式为 Tag.N.Key ，其中N的取值范围：1~20。 一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 或 https:/ / 。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| -Value | String |  | 否 |  | 安全组的标签值。格式为 Tag.N.Value ，其中N 的取值范围：1~20。 一旦传入该值，允许为空字符串。最多支持128个字符，不能以 acs: 开头，不能包含 http:// 或 https:/ / 。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| -value | String |  | 否 |  | 安全组的标签值。 为提高兼容性，建议您尽量使用 Tag.N.Value 参数。 |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

**返回数据**

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SecurityGroupI d | String | sg- bp1fg655nh68xyz9* *** | 安全组ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=CreateSecurityGroup &RegionId=cn-qingdao-**** &Description=SecurityGroupTestDescription &VpcId=vpc-bp1opxu1zkhn00gzv****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
 "SecurityGroupId":"sg-bp1fg655nh68xyz9****"
}
```

`XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId> <SecurityGroupId>sg-bp1fg655nh68xyz9****</SecurityGroupId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidDescripti on.Malformed | InvalidDescription.Malformed | The specified parameter "Description" is not valid. |
| 400 | PARAMETER GROUP _ DESC IS ILLEGAL _ _ _ | InvalidDescription.Malformed | The specified parameter "Description" is not valid. |
| 400 | NAME ILEGAL _ | InvalidSecurityGroupName.Malfo rmed | Specified security group name is not valid. |
| 400 | Abs.InvalidSecurityG roupName.MalForm ed | InvalidSecurityGroupName.Malfo rmed | Specified security group name is not valid. |
| 400 | DESCRIPTION ILLEG _ AL | InvalidSecurityGroupDiscription. Malformed | Specified security group description is not valid. |
| 400 | VPC INCORRECT ST _ _ ATUS | IncorrectVpcStatus | Current VPC status does not support this operation. |

|  | 云服务器ECS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTagKey.Malfo rmed | InvalidTagKey.Malformed | Specified tag key is not valid. |
| 400 | InvalidTagValue.Mal formed | InvalidTagValue.Malformed | Specified tag value is not valid. |
| 400 | Duplicate.TagKey | Duplicate.TagKey | The Tag.N.Key contain duplicate key. |
| 400 | InvalidTagKey.Malfo rmed | InvalidTagKey.Malformed | The specified Tag.n.Key is not valid. |
| 400 | InvalidTagValue.Mal formed | InvalidTagValue.Malformed | The specified Tag.n.Value is not valid. |
| 400 | InvalidParams.Grou pType | InvalidParams.GroupType | The specified security group type is not valid. |
| 400 | ENTERPRISE SECURI _ TY GROUP MUST B _ _ _ E VPC TYPE _ _ | InvalidParams.VpcIdGroupType | Only VPC instance supports enterprise level security group. |
| 400 | InvalidUserId.NotIn WhiteList | InvalidUserId.NotInWhiteList | The userId isn't in enterprise level security group white list. |
| 400 | ENTERPRISE SECURI _ TY GROUP NOT OP _ _ _ EN FOR REGION _ _ | InvalidRegion.NotInWhiteList | The Enterprise SecurityGroup isn't open to this region yet. |
| 500 | 401 | InternalError | The request processing has failed due to some unknown error. |
| 500 | -1201015 | InternalError | The request processing has failed due to some unknown error. |
| 500 | VPC TASK CONFLIC _ _ T | InternalError | The request processing has failed due to some unknown error. |
| 500 | -90 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -96 | InternalError | The request processing has failed due to some unknown error. |
| 403 | QUOTA FULL _ | QuotaExceed.SecurityGroup | The maximum number of security groups is reached. |
| 403 | -1201010 | InvalidVpcId.NotFound | vpc id must not empty when only support vpc vm. |
| 403 | VPC DEFAULT DEFA _ _ ULTVPC STATUS ILL _ _ EAGE | IncorrectVpcStatus | Current VPC status does not support this operation. |
| 403 | TOKEN PROCESSIN _ G | IdempotentProcessing | The previous idempotent request(s) is still processing. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 403 | QuotaExceed.Tags | QuotaExceed.Tags | %s |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | InvalidOperation.ResourceMana gedByCloudProduct | %s |
| 404 | -140 | InvalidRegionId.NotFound | The RegionId provided does not exist in our records. |
| 404 | VPC NOT EXIST _ _ | InvalidVpcId.NotFound | Specified VPC does not exist. |
| 404 | -1013022 | InvalidVpcId.NotFound | Specified VPC does not exist. |
| 404 | InvalidResourceGro up | InvalidResourceGroup.NotFound | The ResourceGroup provided does not exist in our records. |

##### AuthorizeSecurityGroup

调用AuthorizeSecurityGroup增加一条入方向安全组规则。指定安全组入方向的访问权限，允许或者拒绝其他设备发送入方向流量到安全组里的实例。

**接口说明**

安全组的API文档中，流量的发起端为源端（Source），数据传输的接收端为目的端（Dest）。 调用该接口时，您需要了解： 出方向和入方向安全组规则总和不能超过1,000条。 安全组规则优先级（Priority）可选范围为1~100。数字越小，代表优先级越高。 优先级相同的安全组规则，以拒绝访问（drop）的规则优先。 源端设备可以是指定的IP地址范围（SourceCidrIp），也可以是其他安全组（SourceGroupId）中的ECS实例。 如果匹配的安全组规则已存在，此次AuthorizeSecurityGroup调用成功，但不会增加规则数。 以下任意一组参数可以确定一条安全组规则，只指定一个参数无法确定一条安全组规则。 设置指定IP地址段的访问权限。此时，经典网络类型安全组的网卡类型（NicType）可设置公网 （internet）和内网（intranet）。VPC类型安全组的网卡类型（NicType）只可设置内网（intranet）。 如以下请求示例：IpProtocol、PortRange、（可选）SourcePortRange、NicType、Policy和 SourceCidrIp。

```
https://ecs.example.com/?Action=AuthorizeSecurityGroup &SecurityGroupId=sg-F876FF7** &SourceCidrIp=10.0.0.0/8 &IpProtocol=tcp &PortRange=22/22 &NicType=intranet &Policy=accept
```

`&<`公共请求参数> 云服务器ECS 设置其他安全组的访问权限。此时，网卡类型（NicType）只能为内网（intranet）。经典网络类型安全组之间互访时，可以设置同一地域中其他安全组对您的安全组的访问权限。这个安全组可以是您的也可以是其他阿里云账户（SourceGroupOwnerAccount）的。VPC类型安全组之间互访时，可以设置同一VPC内其他安全组访问该安全组的访问权限。如以下请求示例：IpProtocol、PortRange、（可选）SourcePortRange、NicType、Policy、SourceGroupOwnerAccount和SourceGroupId。

```
https://ecs.example.com/?Action=AuthorizeSecurityGroup &SecurityGroupId=sg-F876FF7** &SourceGroupId=sg-1651FBB** &SourceGroupOwnerAccount=t***@aliyun.com &IpProtocol=tcp &PortRange=22/22 &NicType=intranet &Policy=drop
```

`&<`公共请求参数>

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | AuthorizeSecurityGroup | 系统规定参数。取值： AuthorizeSecurityGroup。 |
| RegionId | String | Query | 是 | cn-qingdao-env17-d01 | 安全组所属地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多详情，请参见《云服务器 ECS开发指南》中的如何保证幂等性章节。 |
| SecurityGr oupId | String | Query | 是 | sg-bp67acfmxazb4ph*** | 目的端安全组ID。 |
| Policy | String | Query | 否 | accept | 设置访问权限。取值范围： accept（默认）：接受访问。 drop：拒绝访问，不返回拒绝信息，表现为发起端请求超时或者无法建立连接的类似信息。 |
| Priority | String | Query | 否 | 1 | 安全组规则优先级，数字越小，代表优先级越高。取值范围：1~100。 默认值：1。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| IpProtocol | String | Query | 否 | all | 传输层协议。取值大小写敏感。取值范围： tcp。 udp。 icmp。 gre。 all：支持所有协议。 说明此处icmp协议仅支持IPv4地址。 |
| SourceCidr Ip | String | Query | 否 | 10.0.0.0/8 | 源端IPv4 CIDR地址段。支持 CIDR格式和IPv4格式的IP地址范围。 默认值：无。 |
| Ipv6Source CidrIp | String | Query | 否 | 2001:250:6000::*** | 源端IPv6 CIDR地址段。支持 CIDR格式和IPv6格式的IP地址范围。 说明仅支持VPC类型ECS实例的IPv6地址。 默认值：无。 |
| SourceGro upId | String | Query | 否 | sg-bp67acfmxazb4pj*** | 需要设置访问权限的源端安全组ID。至少设置一项 SourceGroupId或者 SourceCidrIp参数。 如果指定了SourceGroupId没有指定参数SourceCidrIp，则参数NicType取值只能为 intranet。 如果同时指定了 SourceGroupId和 SourceCidrIp，则默认以 SourceCidrIp为准。 |
| PortRange | String | Query | 否 | 22/22 | 目的端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为1~65535。使用斜线 （/）隔开起始端口和终止端口。正确示范：1/200；错误示范：200/1。 ICMP协议：- 1/-1。 GRE协议：-1/-1。 IpProtocol取值为all：-1/- 1。 |
| DestCidrIp | String | Query | 否 | 10.0.0.0/8 | 目的端IPv4 CIDR地址段。支持CIDR格式和IPv4格式的IP 地址范围。 默认值：无。 |
| Ipv6DestCi drIp | String | Query | 否 | 2001:250:6000::*** | 目的端IPv6 CIDR地址段。支持CIDR格式和IPv6格式的IP 地址范围。 说明仅支持VPC 类型ECS实例的IPv6地址。 默认值：无。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourcePort Range | String | Query | 否 | 22/22 | 源端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为 1~65535。使用斜线（/）隔开起始端口和终止端口。正确示范：1/200；错误示范： 200/1。 ICMP协议：-1/-1。 GRE协议：-1/-1。 IpProtocol取值为all：-1/- 1。 |
| SourceGro upOwnerA ccount | String | Query | 否 | t***@aliyun.com | 跨账户设置安全组规则时，源端安全组所属的阿里云账户。 如果 SourceGroupOwnerAccou nt及SourceGroupOwnerId 均未设置，则认为是设置您其他安全组的访问权限。 如果已经设置参数 SourceCidrIp，则参数 SourceGroupOwnerAccou nt无效。 |
| SourceGro upOwnerId | Long | Query | 否 | 155780923770 | 跨账户设置安全组规则时，源端安全组所属的阿里云账户 ID。 如果 SourceGroupOwnerId及 SourceGroupOwnerAccou nt均未设置，则认为是设置您其他安全组的访问权限。 如果您已经设置参数 SourceCidrIp，则参数 SourceGroupOwnerId无效。 |
| NicType | String | Query | 否 | intranet | 经典网络类型安全组规则的网卡类型。取值范围： internet：公网网卡。 intranet：内网网卡。 专有网络VPC类型安全组规则无需设置网卡类型，默认为 intranet，只能为intranet。 设置安全组之间互相访问时， 即指定了DestGroupId且没有指定DestCidrIp，只能为 intranet。 默认值： internet。 |
| Descriptio n | String | Query | 否 | 手动授权SSH 22端口- RuleDemo | 安全组规则的描述信息。长度为1~512个字符。 |

**返回数据**

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=AuthorizeSecurityGroup &SecurityGroupId=sg-bp67acfmxazb4ph*** &SourceCidrIp=10.0.0.0/8 &IpProtocol=tcp &PortRange=22/22 &NicType=intranet &Policy=accept
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****"
}
```

`XML` 格式

```xml
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7*****</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationDenied | The specified IpProtocol does not exist or IpProtocol and PortRange do not match. | 指定的 IP 协议不存在，或与端口范围不匹配。 |
| 400 | InvalidIpProtocol.Mal formed | The specified parameter PortRange is not valid. | IP 协议参数格式不正确，PortRange 参数不正确。 |
| 400 | InvalidSourceCidrIp. Malformed | The specified parameter SourceCidrIp is not valid. | 源 IP 地址范围参数格式不正确。 |
| 400 | InvalidPolicy.Malfor med | The specified parameter Policy is not valid. | 指定的参数无效，请您检查该参数是否正确。 |
| 400 | InvalidNicType.Valu eNotSupported | The specified NicType does not exist. | 指定的网络类型不存在，请您检查网络类型是否正确。 |
| 400 | InvalidNicType.Mism atch | Specified nic type conflicts with the authorization record. | 指定的 NIC 类型与规则信息冲突。 |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidSourceGroupI d.Mismatch | Specified security group and source group are not in the same VPC. | 指定的安全组和源安全组不在一个 VPC 内。 |
| 400 | InvalidSourceGroup. NotFound | Specified source security group does not exist. | 指定的安全组入方向规则不存在，或相关参数缺失。 |
| 400 | InvalidPriority.Malfor med | The parameter Priority is invalid. | 指定的参数 Priority 无效。 |
| 400 | InvalidSecurityGrou p.InvalidNetworkTyp e | The specified security group network type is not support this operation, please check the security group network types. For VPC security groups, ClassicLink must be enabled. | 指定的安全组网络类型不支持此操作，请检查安全组网络类型。对于 VPC 安全组，必须启用 ClassicLink。 |
| 400 | InvalidSecurityGrou pId.Malformed | The specified parameter SecurityGroupId is not valid. | 指定的参数 SecurityGroupId 无效。 |
| 400 | InvalidParamter.Con flict | The specified SourceCidrIp should be different from the DestCidrIp. | 参数 SourceCidrIp 和 DestCidrIp 不能相同。 |
| 400 | InvalidSourcePortRa nge.Malformed | The specified parameter SourcePortRange is not valid. | 指定的参数 SourcePortRange 无效。 |
| 400 | InvalidParam.Source Ip | %s | 指定的参数 SourceIp 无效。 |
| 400 | InvalidParam.DestIp | %s | 指定的参数 DestIp 无效。 |
| 400 | InvalidParam.Ipv6De stCidrIp | %s | 您输入的参数无效。 |
| 400 | InvalidParam.Ipv6So urceCidrIp | %s | 您输入的参数无效。 |
| 400 | InvalidParam.Ipv4Pr otocolConflictWithIp v6Address | %s | 您输入的参数无效，请检查 IPv4 协议下是否填写了 IPv6 地址。 |
| 400 | InvalidParam.Ipv6Pr otocolConflictWithIp v4Address | %s | 您输入的参数无效，请检查IPv6协议下是否填写了 IPv4 地址。 |
| 400 | ILLEGAL IPV6 CIDR _ _ | %s | 指定的IPv6地址无效。 |
| 400 | InvalidDestCidrIp.Ma lformed | The specified parameter DestCidrIp is not valid. | 指定的 DestCidrIp 无效，请您检查该参数是否正确。 |
| 400 | InvalidParameter.Co nflict | IPv6 and IPv4 addresses cannot exist at the same time. | IPv6地址和IPv4地址不能同时指定。 |
| 400 | InvalidParam.PrefixL istAddressFamilyMis match | The address family of the specified prefix list does not match the specified CidrIp. | 指定前缀列表的地址族，与指定的 CidrIP的地址族不匹配。 |
| 400 | NotSupported.Classi cNetworkPrefixList | The prefix list is not supported when the network type of security group is classic. | 安全组的网络类型为经典网络，不支持前缀列表。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 400 | InvalidParam.Source CidrIp | The specified param SourceCidrIp is not valid. | 参数SourceCidrIp不合法。 |
| 400 | InvalidParam.DestCi drIp | The specified param DestCidrIp is not valid. | 您指定的参数DestCidrIp不合法。 |
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 400 | InvalidParam.Permis sions | The specified parameter Permissions cannot coexist with other parameters. | 指定的参数Permissions不能与其他参数同时存在。 |
| 400 | InvalidParam.Duplic atePermissions | There are duplicate permissions in the specified parameter Permissions. | 指定的参数Permissions中存在重复的规则。 |
| 403 | InvalidSourceGroupI d.Mismatch | NicType is required or NicType expects intranet. | 需要提供 NicType，NicType 仅在内网中使用。 |
| 403 | AuthorizationLimitEx ceed | The limit of authorization records in the security group reaches. | 安全组授权规则数达到上限，请您检查授权规则是否合理。 |
| 403 | InvalidParamter.Con flict | The specified SecurityGroupId should be different from the SourceGroupId. | 授权与被授权安全组必须不同。 |
| 403 | InvalidNetworkType. Mismatch | The specified SecurityGroup network type should be same with SourceGroup network type (vpc or classic). | 指定的 SecurityGroup 的网络类型必须与 SouceGroup 的网络类型一致。 |
| 403 | InvalidNetworkType. Conflict | The specified SecurityGroup network type should be same with SourceGroup network type (vpc or classic). | 指定的 SecurityGroup 的网络类型必须与 SouceGroup 的网络类型一致。 |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | %s | 云产品托管的安全组不支持修改操作。 |
| 403 | LimitExceed.PrefixLi stAssociationResour ce | The number of resources associated with the prefix list exceeds the limit. | 与前缀列表关联的资源数量超出限制。 |
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组 ID 是否正确。 |
| 404 | InvalidSourceGroupI d.NotFound | The SourceGroupId provided does not exist in our records. | 指定的入方向安全组不存在。 |
| 404 | InvalidPrefixListId.N otFound | The specified prefix list was not found. | 前缀列表不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

云服务器ECS

##### AuthorizeSecurityGroupEgress

调用AuthorizeSecurityGroupEgress增加一条安全组出方向规则。指定安全组出方向的访问权限，允许或者拒绝安全组里的实例发送出方向流量到其他设备。

**接口说明**

安全组的API文档中，流量的发起端为源端（Source），数据传输的接收端为目的端（Dest）。 调用该接口时，您需要了解： 出方向和入方向安全组规则总和不能超过1,000条。 安全组规则分为接受访问（accept）和拒绝访问（drop）两类。 安全组规则优先级（Priority）可选范围为1~100。数字越小，代表优先级越高。 优先级相同的安全组规则，优先以拒绝访问（drop）的规则为准。 目的端设备可以是指定的IP地址范围（DestCidrIp），也可以是其他安全组（DestGroupId）中的ECS实例。 如果匹配的安全组规则已存在，此次AuthorizeSecurityGroupEgress调用成功，但不会增加规则数。 以下任意一组参数可以确定一条安全组规则，只指定一个参数无法确定一条安全组规则。 设置指定IP地址段的访问权限。如以下请求示例：IpProtocol、PortRange、（可选）SourcePortRange、NicType、Policy和DestCidrIp。

```
https://ecs.example.com/?Action=AuthorizeSecurityGroupEgress &SecurityGroupId=sg-bp67acfmxazb4ph*** &IpProtocol=icmp &DestCidrIp=10.0.0.0/8 &PortRange=-1/-1 &NicType=intranet &Policy=Allow &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 设置其他安全组的访问权限。如以下请求示例：IpProtocol、PortRange、（可选）SourcePortRange、 NicType、Policy、DestGroupOwnerAccount和DestGroupId。

```
https://ecs.example.com/?Action=AuthorizeSecurityGroupEgress &SecurityGroupId=sg-bp67acfmxazb4ph*** &DestGroupId=sg-bp67acfmxazb4pi*** &DestGroupOwnerAccount=T***@aliyun.com &IpProtocol=tcp &PortRange=22/22 &NicType=intranet &Policy=Drop &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数>

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | AuthorizeSecurityGroupE gress | 系统规定参数。取值： AuthorizeSecurityGroupE gress。 |

| 开发指南·API参 | 考 |  |  |  | 云服务器EC |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 源端安全组所属地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多详情，请参见《云服务器 ECS开发指南》中的如何保证幂等性章节。 |
| SecurityGr oupId | String | Query | 是 | sg-bp67acfmxazb4ph*** | 源端安全组ID。 |
| Policy | String | Query | 否 | accept | 设置访问权限。取值范围： accept：接受访问。 drop： 拒绝访问，不返回拒绝信息。 默认值：accept。 |
| Priority | String | Query | 否 | 1 | 安全组规则优先级。取值范围：1~100。 默认值：1。 |
| IpProtocol | String | Query | 否 | all | 传输层协议。取值大小写敏感。取值范围： icmp。 gre。 tcp。 udp。 all：支持所有协议。 |
| DestCidrIp | String | Query | 否 | 10.0.0.0/8 | 目的端IP地址范围。支持 CIDR格式和IPv4格式的IP地址范围。 默认值：无。 |
| Ipv6DestCi drIp | String | Query | 否 | 2001:db8:1233:1a00::*** | 目的端IPv6 CIDR地址段。支持CIDR格式和IPv6格式的IP 地址范围。 默认值：无。 说明仅支持VPC类型的IP地址。 |
| DestGroupI d | String | Query | 否 | sg-bp67acfmxazb4pi*** | 需要设置访问权限的目的端安全组ID。 至少设置一项 DestGroupId或者 DestCidrIp参数。 如果指定了DestGroupId没有指定参数DestCidrIp，则参数 NicType取值只能为 intranet。 如果同时指定了 DestGroupId和 DestCidrIp，则默认以 DestCidrIp为准。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PortRange | String | Query | 否 | 80/80 | 目的端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为1~65535。使用正斜线 （/）隔开起始端口和终止端口。例如：1/200。 ICMP协议：-1/-1。 GRE协议：-1/- 1。 all：-1/-1。 |
| SourceCidr Ip | String | Query | 否 | 10.0.0.0/8 | 源端IP地址范围。支持CIDR 格式和IPv4格式的IP地址范围。 默认值：无。 |
| Ipv6Source CidrIp | String | Query | 否 | 2001:db8:1234:1a00::*** | 源端IPv6 CIDR地址段。支持 CIDR格式和IPv6格式的IP地址范围。 默认值：无。 说明仅支持VPC类型的IP地址。 |
| SourcePort Range | String | Query | 否 | 80/80 | 源端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：1~65535。 使用正斜线（/）隔开起始端口和终止端口。例如： 1/200。 ICMP协议：-1/-1。 GRE协议：-1/-1。 all：-1/- 1。 |
| DestGroup OwnerAcco unt | String | Query | 否 | T***@aliyun.com | 跨账户设置安全组规则时，目的端安全组所属的阿里云账户。 如果 DestGroupOwnerAccount 及DestGroupOwnerId均未设置，则认为是设置您其他安全组的访问权限。 如果已经设置参数DestCidrIp，则参数 DestGroupOwnerAccount 无效。 |
| DestGroup OwnerId | Long | Query | 否 | 12345678910 | 跨账户设置安全组规则时，目的端安全组所属的阿里云账户 ID。 如果 DestGroupOwnerId及 DestGroupOwnerAccount 均未设置，则认为是设置您其他安全组的访问权限。 如果您已经设置参数 DestCidrIp，则参数 DestGroupOwnerId无效。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NicType | String | Query | 否 | intranet | 经典网络类型安全组规则的网卡类型。取值范围： internet：公网网卡 intranet：内网网卡专有网络VPC类型安全组规则无需设置网卡类型，默认为 intranet，只能为intranet。 设置安全组之间互相访问时， 即指定了DestGroupId且没有指定DestCidrIp，只能为 intranet。 默认值： internet。 |
| Descriptio n | String | Query | 否 | 手动授权SSH 22端口- RuleDemo | 安全组规则的描述信息。长度为1~512个字符。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=AuthorizeSecurityGroupEgress &IpProtocol=tcp &PortRange=80/80 &RegionId=cn-qingdao-env17-**** &SecurityGroupId=sg-bp67acfmxazb4ph***
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7*****"
}
```

`XML` 格式

```xml
<RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7*****</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationDenied | The specified IpProtocol does not exist or IpProtocol and PortRange do not match. | 指定的 IP 协议不存在，或与端口范围不匹配。 |
| 400 | InvalidNicType.Valu eNotSupported | The specified NicType does not exist. | 指定的网络类型不存在，请您检查网络类型是否正确。 |
| 400 | InvalidNicType.Mism atch | Specified nic type conflicts with the authorization record. | 指定的 NIC 类型与规则信息冲突。 |
| 400 | InvalidDestGroupId. Mismatch | Specified security group and destination group are not in the same VPC. | 指定的安全组和目标组不在同一个 VPC 下。 |
| 400 | InvalidDestGroup.No tFound | Specified destination security group does not exist. | 指定的出方向安全组不存在。 |
| 400 | InvalidPriority.Malfor med | The parameter Priority is invalid. | 指定的参数 Priority 无效。 |
| 400 | InvalidDestCidrIp.Ma lformed | The specified parameter DestCidrIp is not valid. | 指定的 DestCidrIp 无效，请您检查该参数是否正确。 |
| 400 | InvalidDestCidrIp.Ma lformed | The parameter DestCidrIp is not valid. | 指定的参数 DestCidrIp 无效。 |
| 400 | InvalidSecurityGrou p.InvalidNetworkTyp e | The specified security group network type is not support this operation, please check the security group network types. For VPC security groups, ClassicLink must be enabled. | 指定的安全组网络类型不支持此操作，请检查安全组网络类型。对于 VPC 安全组，必须启用 ClassicLink。 |
| 400 | InvalidSecurityGrou pId.Malformed | The specified parameter SecurityGroupId is not valid. | 指定的参数 SecurityGroupId 无效。 |
| 400 | InvalidParamter.Con flict | The specified SourceCidrIp should be different from the DestCidrIp. | 参数 SourceCidrIp 和 DestCidrIp 不能相同。 |
| 400 | InvalidSourcePortRa nge.Malformed | The specified parameter SourcePortRange is not valid. | 指定的参数 SourcePortRange 无效。 |
| 400 | InvalidParam.Source Ip | %s | 指定的参数 SourceIp 无效。 |
| 400 | InvalidParam.DestIp | %s | 指定的参数 DestIp 无效。 |
| 400 | InvalidParam.Ipv6De stCidrIp | %s | 您输入的参数无效。 |
| 400 | InvalidParam.Ipv6So urceCidrIp | %s | 您输入的参数无效。 |
| 400 | InvalidParam.Ipv4Pr otocolConflictWithIp v6Address | %s | 您输入的参数无效，请检查 IPv4 协议下是否填写了 IPv6 地址。 |
| 400 | InvalidParam.Ipv6Pr otocolConflictWithIp v4Address | %s | 您输入的参数无效，请检查IPv6协议下是否填写了 IPv4 地址。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 400 | ILLEGAL IPV6 CIDR _ _ | %s | 指定的IPv6地址无效。 |
| 400 | InvalidParameter.Co nflict | IPv6 and IPv4 addresses cannot exist at the same time. | IPv6地址和IPv4地址不能同时指定。 |
| 400 | InvalidParam.PrefixL istAddressFamilyMis match | The address family of the specified prefix list does not match the specified CidrIp. | 指定前缀列表的地址族，与指定的 CidrIP的地址族不匹配。 |
| 400 | NotSupported.Classi cNetworkPrefixList | The prefix list is not supported when the network type of security group is classic. | 安全组的网络类型为经典网络，不支持前缀列表。 |
| 400 | InvalidParam.DestCi drIp | The specified parameter DestCidrIp is invalid. | 指定的参数“DestCidrIp”无效。 |
| 400 | InvalidParam.Source CidrIp | The specified param SourceCidrIp is not valid. | 参数SourceCidrIp不合法。 |
| 400 | InvalidParam.Permis sions | The specified parameter Permissions cannot coexist with other parameters. | 指定的参数Permissions不能与其他参数同时存在。 |
| 400 | InvalidParam.Duplic atePermissions | There are duplicate permissions in the specified parameter Permissions. | 指定的参数Permissions中存在重复的规则。 |
| 403 | InvalidDestGroupId. Mismatch | NicType is required or NicType expects intranet. | 请指定 NicType，或使用内网模式。 |
| 403 | AuthorizationLimitEx ceed | The limit of authorization records in the security group reaches. | 安全组授权规则数达到上限，请您检查授权规则是否合理。 |
| 403 | InvalidParamter.Con flict | The specified SecurityGroupId should be different from the SourceGroupId. | 授权与被授权安全组必须不同。 |
| 403 | InvalidNetworkType. Conflict | The specified SecurityGroup network type should be same with SourceGroup network type (vpc or classic). | 指定的 SecurityGroup 的网络类型必须与 SouceGroup 的网络类型一致。 |
| 403 | InvalidSecurityGrou p.IsSame | The authorized SecurityGroupId should be different from the DestGroupId. | 已授权的 SecurityGroupId 不能与 DestGroupId 相同。 |
| 403 | InvalidNetworkType. Conflict | The parameter SecurityGroup network type should be same with SourceGroup network type (vpc or classic). | 安全组网络类型必须和源安全组网络类型一致。 |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | %s | 云产品托管的安全组不支持修改操作。 |
| 403 | LimitExceed.PrefixLi stAssociationResour ce | The number of resources associated with the prefix list exceeds the limit. | 与前缀列表关联的资源数量超出限制。 |

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组 ID 是否正确。 |
| 404 | InvalidDestGroupId. NotFound | The DestGroupId provided does not exist in our records. | 指定的出方向安全组不存在。 |
| 404 | InvalidPrefixListId.N otFound | The specified prefix list was not found. | 前缀列表不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### JoinSecurityGroup

**接口说明**

调用该接口时，您需要注意： 加入安全组之前，实例必须处于已停止（`Stopped`）或者运行中（`Running`）状态。 一台实例最多可以加入10个安全组。 每个安全组最多能管理1000台实例。 您的安全组和实例必须属于同一个阿里云地域。 您的安全组和实例的网络类型必须相同。如果网络类型为专有网络VPC，则安全组和实例必须属于同一个 VPC。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | JoinSecurityGroup | 系统规定参数。取值： JoinSecurityGroup |
| SecurityGr oupId | String | Query | 是 | sg-bp67acfmxazb4ph*** | 安全组ID。您可以调用 DescribeSecurityGroups查看您可用的安全组。 |
| InstanceId | String | Query | 否 | i-bp67acfmxazb4ph*** | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&SecurityGroupId=sg-bp67acfmxazb4ph***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

`XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组ID是否正确。 |
| 400 | InstanceSecurityGro upLimitExceeded | Exceeding the allowed amount of security groups that an instance can be in. | 加入安全组失败，该实例加入的安全组数量已达到上限。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 403 | SecurityGroupInstan ceLimitExceeded | The maximum number of instances in a security group is exceeded. | 该安全组内已有的实例数量已达到最大限制。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInstanceId.Mi smatch | Specified instance and security group are not in the same VPC. | 指定的实例和安全组不属于同一个虚拟专有网络。（包含另外两种特殊情况：1.实例不属于VPC类型，安全组属于VPC类型；2.实例属于VPC类型，安全组不属于VPC类型。） |
| 403 | InvalidInstanceId.Alr eadyExists | The specified instance already exists in the specified security group. | 指定的实例已经在指定的安全组中。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | SecurityGroupInstan ceLimitExceeded | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | AclLimitExceed | %s | AccessPoint已超出限额值。 |
| 403 | InstanceSecurityGro upLimitExceeded | %s | 实例绑定的安全组数量达到最大限制。 |
| 400 | InvalidInstanceId.Ma lformed | The specified parameter "InstanceId" is not valid. | 指定的参数InstanceId格式有误。 |

##### LeaveSecurityGroup

**接口说明**

调用该接口时，您需要注意： 移出安全组之前，实例必须处于**已停止**（Stopped）或者**运行中**（Running）状态。 一台实例必须至少加入一个安全组，当该实例只加入了一个安全组时，则LeaveSecurityGroup请求会失败。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | LeaveSecurityGro up | 系统规定参数。取值： LeaveSecurityGroup |
| InstanceId | String | 是 | i- bp67acfmxazb4p h*** | 实例ID。 |
| SecurityGroupId | String | 是 | sg- bp67acfmxazb4p h*** | 安全组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云服务器ECS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
https://ecs.example.com/?Action=LeaveSecurityGroup &InstanceId=i-bp67acfmxazb4ph*** &SecurityGroupId=sg-bp67acfmxazb4ph***
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
| 404 | InvalidInstanceId.No tFound | The specified InstanceId does not exist. | 指定的实例不存在，请您检查实例ID 是否正确。 |
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组ID是否正确。 |
| 403 | InstanceLastSecurit yGroup | The specified security group is the last security group for the instance. | 指定的安全组是实例的最后一个安全组。 |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | 该资源目前的状态不支持此操作。 |
| 403 | InstanceLockedForS ecurity | The specified operation is denied as your instance is locked for security reasons. | 实例被安全锁定，指定的操作无法完成。 |
| 403 | InstanceNotInSecuri tyGroup | The instance not in the group. | 指定的实例不在安全组内。 |
| 504 | RequestTimeout | The request encounters an upstream server timeout. | 上游服务器超时，请求被拒绝。 |
| 400 | InvalidInstanceId.Ma lformed | The specified parameter "InstanceId" is not valid. | 指定的参数InstanceId格式有误。 |

云服务器ECS

##### DeleteSecurityGroup

**接口说明**

删除安全组之前，请确保安全组内不存在实例，并且没有其他安全组与该安全组有授权行为 （DescribeSecurityGroupReferences），否则DeleteSecurityGroup请求失败。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteSecurityGr oup | 系统规定参数。取值： DeleteSecurityGroup |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| SecurityGroupId | String | 是 | sg- bp1fg655nh68xy z9i*** | 安全组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DeleteSecurityGroup &RegionId=cn-qingdao-env17-d01 &SecurityGroupId=sg-bp1fg655nh68xyz9i***
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
}
```

**错误码**

云服务器ECS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | DependencyViolatio n | There is still instance(s) in the specified security group. | 安全组中还有未释放的实例，请您先释放实例再进行该操作。 |
| 403 | DependencyViolatio n | The specified security group has been authorized in another one. | 指定的安全组已在另一个组中授权， 不允许重复授权。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### DescribeSecurityGroupAttribute

调用DescribeSecurityGroupAttribute查询一个安全组的安全组规则。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSecurity GroupAttribute | 系统规定参数，取值： DescribeSecurityGroupAttribute。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 安全组所属地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| SecurityGroupId | String | 是 | sg- bp1gxw6bznjjvhu 3g*** | 安全组ID。 |
| NicType | String | 否 | intranet | 安全组规则的网卡类型。 经典网络类型安全组的取值范围： internet（默认）：公网 intranet：内网说明单次调用只能查询一种网卡类型的安全组规则，查询全部类型请分两次调用。 专有网络类型安全组的取值范围： intranet（默认）：内网说明如果传入internet或空值，则会默认转化为intranet。 |
| Direction | String | 否 | all | 安全组规则授权方向。取值范围： egress：安全组出方向 ingress：安全组入方向 all：不区分方向默认值：all。 |

云服务器ECS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Description | String | FinanceDept | 安全组描述信息。 |
| InnerAccessPoli cy | String | Accept | 安全组内网络连通策略。可能值： Accept：内网互通 Drop：内网隔离 |
| Permissions | Array of Permission |  | 安全组权限规则集合。 |
| Permission |  |  |  |
| CreateTime | String | 2018-12- 12T07:28:38Z | 创建时间，UTC时间。 |
| Description | String | FinanceDept | 安全组描述信息。 |
| DestCidrIp | String | 0.0.0.0/0 | 目标IP地址段，用于出方向授权。 |
| DestGroupId | String | sg-securitygroupid1 | 目标安全组，用于出方向授权。 |
| DestGroupNam e | String | SecurityGuard | 目的端安全组名称。 |
| DestGroupOwn erAccount | String | SecurityGuard | 目标安全组所属阿里云账户ID。 |
| Direction | String | ingress | 授权方向。 |
| IpProtocol | String | TCP | IP协议。 |
| Ipv6DestCidrIp | String | 2001:db8:1233:1a0 0::*** | 目的IPv6地址段。 |
| Ipv6SourceCidrI p | String | 2001:db8:1234:1a0 0::*** | 源IPv6地址段。 |
| NicType | String | intranet | 网络类型。 |
| Policy | String | Accept | 授权策略。 |
| PortRange | String | 80/80 | 端口范围。 |
| Priority | String | 1 | 规则优先级。 |

云服务器ECS

| SourceCidrIp | String | 0.0.0.0/0 | 源IP地址段，用于入方向授权。 |
|---|---|---|---|
| SourceGroupId | String | sg-securitygroupid2 | 源安全组，用于入方向授权。 |
| SourceGroupNa me | String | FinanceDeptSource G**** | 源端安全组名称。 |
| SourceGroupO wnerAccount | String | FinanceGroupO**** | 源安全组所属阿里云账户ID。 |
| SourcePortRan ge | String | 80/80 | 源端端口范围。 |
| RegionId | String | cn-qingdao-env17- d01 | 地域ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| SecurityGroupI d | String | sg- bp1gxw6bznjjvhu3g *** | 目标安全组ID。 |
| SecurityGroupN ame | String | FinanceSecurityG*** * | 目标安全组名称。 |
| VpcId | String | vpc- bp1opxu1zkhn00gz v2*** | VPC ID。如果返回VPC ID，表示该安全组网络类型为VPC。否则，表示是经典网络类型安全组。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeSecurityGroupAttribute &SecurityGroupId=sg-bp1gxw6bznjjvhu3g*** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <SecurityGroupId>sg-bp1gxw6bznjjvhu3g***</SecurityGroupId>
   <InnerAccessPolicy>Accept</InnerAccessPolicy>
   <SecurityGroupName>FinanceSecurityG****</SecurityGroupName>
   <Description>FinanceDept</Description>
   <RegionId>cn-qingdao-env17-d01</RegionId>
   <RequestId>A72322C1-47C0-491E-8088-8B17E4EA859F</RequestId>
   <Permissions>
      <Permission>
         <SourceCidrIp>10.0.0.0/8</SourceCidrIp>
         <Description></Description>
         <DestCidrIp></DestCidrIp>
         <NicType>intranet</NicType>
         <DestGroupName></DestGroupName>
```

云服务器ECS

```xml
         <PortRange>22/22</PortRange>
         <DestGroupId></DestGroupId>
         <Ipv6DestCidrIp></Ipv6DestCidrIp>
         <Direction>ingress</Direction>
         <Priority>1</Priority>
         <IpProtocol>TCP</IpProtocol>
         <SourcePortRange></SourcePortRange>
         <SourceGroupOwnerAccount></SourceGroupOwnerAccount>
         <Policy>Accept</Policy>
         <CreateTime>2018-12-12T07:28:38Z</CreateTime>
         <SourceGroupId></SourceGroupId>
         <DestGroupOwnerAccount></DestGroupOwnerAccount>
         <Ipv6SourceCidrIp></Ipv6SourceCidrIp>
         <SourceGroupName></SourceGroupName>
      </Permission>
      <Permission>
         <SourceCidrIp>0.0.0.0/0</SourceCidrIp>
         <Description></Description>
         <DestCidrIp></DestCidrIp>
         <NicType>intranet</NicType>
         <DestGroupName></DestGroupName>
         <PortRange>443/443</PortRange>
         <DestGroupId></DestGroupId>
         <Ipv6DestCidrIp></Ipv6DestCidrIp>
         <Direction>ingress</Direction>
         <Priority>1</Priority>
         <IpProtocol>TCP</IpProtocol>
         <SourcePortRange></SourcePortRange>
         <SourceGroupOwnerAccount></SourceGroupOwnerAccount>
         <Policy>Accept</Policy>
         <CreateTime>2018-12-12T07:28:38Z</CreateTime>
         <SourceGroupId></SourceGroupId>
         <DestGroupOwnerAccount></DestGroupOwnerAccount>
         <Ipv6SourceCidrIp></Ipv6SourceCidrIp>
         <SourceGroupName></SourceGroupName>
      </Permission>
      <Permission>
         <SourceCidrIp>10.0.0.0/8</SourceCidrIp>
         <Description></Description>
         <DestCidrIp></DestCidrIp>
         <NicType>intranet</NicType>
         <DestGroupName></DestGroupName>
         <PortRange>80/80</PortRange>
         <DestGroupId></DestGroupId>
         <Ipv6DestCidrIp></Ipv6DestCidrIp>
         <Direction>ingress</Direction>
         <Priority>1</Priority>
         <IpProtocol>TCP</IpProtocol>
         <SourcePortRange></SourcePortRange>
         <SourceGroupOwnerAccount></SourceGroupOwnerAccount>
         <Policy>Accept</Policy>
         <CreateTime>2018-12-12T07:28:38Z</CreateTime>
         <SourceGroupId></SourceGroupId>
         <DestGroupOwnerAccount></DestGroupOwnerAccount>
         <Ipv6SourceCidrIp></Ipv6SourceCidrIp>
         <SourceGroupName></SourceGroupName>
</Permission>
```

云服务器ECS

```xml
      </Permission>
      <Permission>
         <SourceCidrIp>10.0.0.0/8</SourceCidrIp>
         <Description></Description>
         <DestCidrIp></DestCidrIp>
         <NicType>intranet</NicType>
         <DestGroupName></DestGroupName>
         <PortRange>-1/-1</PortRange>
         <DestGroupId></DestGroupId>
         <Ipv6DestCidrIp></Ipv6DestCidrIp>
         <Direction>ingress</Direction>
         <Priority>1</Priority>
         <IpProtocol>ICMP</IpProtocol>
         <SourcePortRange>-1/-1</SourcePortRange>
         <SourceGroupOwnerAccount></SourceGroupOwnerAccount>
         <Policy>Accept</Policy>
         <CreateTime>2018-12-12T07:28:38Z</CreateTime>
         <SourceGroupId></SourceGroupId>
         <DestGroupOwnerAccount></DestGroupOwnerAccount>
         <Ipv6SourceCidrIp></Ipv6SourceCidrIp>
         <SourceGroupName></SourceGroupName>
      </Permission>
   </Permissions>
   <VpcId>vpc-bp1opxu1zkhn00gzv2***</VpcId>
```

`JSON` 格式

```json
{
    "SecurityGroupId": "sg-bp1gxw6bznjjvhu3g***",
    "InnerAccessPolicy": "Accept",
    "SecurityGroupName": "FinanceSecurityG****",
    "Description": "FinanceDept",
    "RegionId": "cn-qingdao-env17-d01",
    "RequestId": "A72322C1-47C0-491E-8088-8B17E4EA859F",
    "Permissions": {
        "Permission": [
            {
                "SourceCidrIp": "10.0.0.0/8",
                "Description": "",
                "DestCidrIp": "",
                "NicType": "intranet",
                "DestGroupName": "",
                "PortRange": "22/22",
                "DestGroupId": "",
                "Ipv6DestCidrIp": "",
                "Direction": "ingress",
                "Priority": 1,
                "IpProtocol": "TCP",
                "SourcePortRange": "",
                "SourceGroupOwnerAccount": "",
                "Policy": "Accept",
                "CreateTime": "2018-12-12T07:28:38Z",
                "SourceGroupId": "",
                "DestGroupOwnerAccount": "",
                "Ipv6SourceCidrIp": "",
"SourceGroupName":""
```

云服务器ECS

```json
SouceGoupae:
            },
            {
                "SourceCidrIp": "0.0.0.0/0",
                "Description": "",
                "DestCidrIp": "",
                "NicType": "intranet",
                "DestGroupName": "",
                "PortRange": "443/443",
                "DestGroupId": "",
                "Ipv6DestCidrIp": "",
                "Direction": "ingress",
                "Priority": 1,
                "IpProtocol": "TCP",
                "SourcePortRange": "",
                "SourceGroupOwnerAccount": "",
                "Policy": "Accept",
                "CreateTime": "2018-12-12T07:28:38Z",
                "SourceGroupId": "",
                "DestGroupOwnerAccount": "",
                "Ipv6SourceCidrIp": "",
                "SourceGroupName": ""
            },
            {
                "SourceCidrIp": "0.0.0.0/0",
                "Description": "",
                "DestCidrIp": "",
                "NicType": "intranet",
                "DestGroupName": "",
                "PortRange": "80/80",
                "DestGroupId": "",
                "Ipv6DestCidrIp": "",
                "Direction": "ingress",
                "Priority": 1,
                "IpProtocol": "TCP",
                "SourcePortRange": "",
                "SourceGroupOwnerAccount": "",
                "Policy": "Accept",
                "CreateTime": "2018-12-12T07:28:38Z",
                "SourceGroupId": "",
                "DestGroupOwnerAccount": "",
                "Ipv6SourceCidrIp": "",
                "SourceGroupName": ""
            },
            {
                "SourceCidrIp": "10.0.0.0/8",
                "Description": "",
                "DestCidrIp": "",
                "NicType": "intranet",
                "DestGroupName": "",
                "PortRange": "-1/-1",
                "DestGroupId": "",
                "Ipv6DestCidrIp": "",
                "Direction": "ingress",
                "Priority": 1,
                "IpProtocol": "ICMP",
                "SourcePortRange": "-1/-1",
```

`"S` G O A `t"` `""` 云服务器ECS

```json
                "SourceGroupOwnerAccount": "",
                "Policy": "Accept",
                "CreateTime": "2018-12-12T07:28:38Z",
                "SourceGroupId": "",
                "DestGroupOwnerAccount": "",
                "Ipv6SourceCidrIp": "",
                "SourceGroupName": ""
            }
```

]

```json
    },
    "VpcId": "vpc-bp1opxu1zkhn00gzv2***"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域ID不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组ID是否正确。 |
| 400 | InvalidNicType.Valu eNotSupported | The specified NicType does not exist. | 指定的网络类型不存在，请您检查网络类型是否正确。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 400 | InvalidParamter | Invalid Parameter | 指定的参数不合法。 |
| 400 | InvalidSecurityGrou pId.Malformed | The specified parameter "SecurityGroupId" is not valid. | 指定的参数SecurityGroupId无效。 |

##### DescribeSecurityGroups

**接口说明**

安全组的基本信息包括安全组ID和安全组描述等。返回参数列表按照安全组ID降序排列。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSecurity Groups | 系统规定参数。取值： DescribeSecurityGroups |
| RegionId | String | 是 | cn-qingdao- XXXXX-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| VpcId | String | 否 | vpc- bp67acfmxazb4p **** | 安全组所在的专有网络ID。 |

云服务器ECS

| PageNumber | Integer | 否 | 1 | 安全组列表的页码。 起始值：1。 默认值：1。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。 最大值：50。 默认值：10。 |
| SecurityGroupIds | String | 否 | ["sg- bp67acfmxazb4p ****", "sg- bp67acfmxazb4p ****", "sg- bp67acfmxazb4p ****",....] | 安全组ID列表。一次最多支持100个安全组 ID，ID之间用半角逗号（,）隔开，格式为 JSON数组。 |
| Tag.N.value | String | 否 | null | 安全组的标签值。 说明为提高兼容性，建议您尽量使用Tag.N.Value参数。 |
| Tag.N.key | String | 否 | null | 安全组的标签键。 说明为提高兼容性，建议您尽量使用Tag.N.Key参数。 |
| Tag.N.Key | String | 否 | TestKey | 安全组的标签键。N的取值范围：1~20。 |
| Tag.N.Value | String | 否 | TestValue | 安全组的标签值。N的取值范围：1~20。 |
| NetworkType | String | 否 | vpc | 安全组的网络类型。取值范围： vpc classic |
| SecurityGroupId | String | 否 | sg- bp67acfmxazb4p **** | 安全组ID。 |
| SecurityGroupNa me | String | 否 | SGTestName | 安全组名称。 |

云服务器ECS

| DryRun | Boolean | 否 | false | 是否只预检此次请求。取值范围： true：发送检查请求，不会查询资源状况。检查项包括AccessKey是否有效、 RAM用户的授权情况和是否填写了必需参数。如果检查不通过，则返回对应错误。 如果检查通过，会返回错误码 DryRunOperation。 false：发送正常请求，通过检查后返回 2XX HTTP状态码并直接查询资源状况。 默认值：false。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 1 | 每页行数。 |
| RegionId | String | cn-qingdao-XXXXX- d01 | 安全组所属地域ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |
| SecurityGroups | Array of SecurityGroup |  | 安全组信息集合。 |
| SecurityGroup |  |  |  |
| AvailableInstan ceAmount | Integer | 880 | 该参数未开放使用。 |
| CreationTime | String | 2017-12- 05T22:40:00Z | 创建时间。按照时间格式ISO 8601标准表示，并需要使用UTC时间。格式为：yyyy-MM- ddThh:mmZ。 |
| Description | String | TestDescription | 描述信息。 |
| EcsCount | Integer | 120 | 该参数未开放使用。 |
| ResourceGroup Id | String | rg- bp67acfmxazb4p*** * |  |
| SecurityGroupI d | String | sg- bp67acfmxazb4p*** * | 安全组ID。 |
| SecurityGroupN ame | String | SGTestName | 安全组名称。 |

云服务器ECS

| SecurityGroupT ype | String | normal | 安全组类型。可能值： normal：普通安全组。 enterprise：企业安全组。 |
|---|---|---|---|
| ServiceID | Long | 111111111 | 该参数未开放使用。 |
| ServiceManage d | Boolean | false | 该参数未开放使用。 |
| Tags | Array of Tag |  | 安全组的标签。 |
| Tag |  |  |  |
| TagKey | String | TestKey | 安全组的标签键。 |
| TagValue | String | TestValue | 安全组的标签值。 |
| VpcId | String | vpc- bp67acfmxazb4p*** * | 安全组所属的专有网络。 |
| TotalCount | Integer | 49 | 安全组的总数。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribeSecurityGroups &RegionId=cn-qingdao-XXXXX-d01 &VpcId=vpc-bp67acfmxazb4p**** &PageSize=10 &PageNumber=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
<SecurityGroups>
    <EcsCount>120</EcsCount>
    <Description>TestDescription</Description>
    <VpcId>vpc-bp67acfmxazb4p****</VpcId>
    <SecurityGroupName>SGTestName</SecurityGroupName>
    <SecurityGroupId>sg-bp67acfmxazb4p****</SecurityGroupId>
    <SecurityGroupType>normal</SecurityGroupType>
    <CreationTime>2017-12-05T22:40:00Z</CreationTime>
    <Tags>
        <TagKey>TestKey</TagKey>
        <TagValue>TestValue</TagValue>
    </Tags>
</SecurityGroups> <TotalCount>49</TotalCount> <PageSize>1</PageSize> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId> <PageNumber>1</PageNumber> <RegionId>cn-qingdao-XXXXX-d01</RegionId>
```

`JSON` 格式

```json
{
    "SecurityGroups": {
        "EcsCount": 120,
        "Description": "TestDescription",
        "VpcId": "vpc-bp67acfmxazb4p****",
        "SecurityGroupName": "SGTestName",
        "SecurityGroupId": "sg-bp67acfmxazb4p****",
        "SecurityGroupType": "normal",
        "CreationTime": "2017-12-05T22:40:00Z",
        "Tags": {
            "TagKey": "TestKey",
            "TagValue": "TestValue"
        }
    },
    "TotalCount": 49,
    "PageSize": 1,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
    "PageNumber": 1,
    "RegionId": "cn-qingdao-XXXXX-d01"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### DescribeSecurityGroupReferences

调用DescribeSecurityGroupReferences查询一个安全组和其他哪些安全组有安全组级别的授权行为。 云服务器ECS

**接口说明**

调用该接口时，您需要注意： 授权行为包括入方向授权和出方向授权。 该接口单次最多返回100条记录。 当您无法删除某一安全组（DeleteSecurityGroup）时，可以调用该接口查看指定的安全组是否已被其他安全组授权。如果指定的安全组已被授权，您需要在删除该安全组之前解除授权行为。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSecurity GroupReferences | 系统规定参数。取值： DescribeSecurityGroupReferences |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 安全组所属地域。 |
| SecurityGroupId. N | RepeatLi st | 是 | sg- bp1euoep32o6kv rw**** | 要查询的第N个SecurityGroupId，N的取值范围为1~10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| SecurityGroupR eferences | Array of SecurityGroupR eference |  | 所有用户指定的安全组被授权的完整信息。 |
| SecurityGroupR eference |  |  |  |
| ReferencingSec urityGroups | Array of ReferencingSec urityGroup |  | 正在授权给这个安全组的其他安全组信息。 |
| ReferencingSec urityGroup |  |  |  |
| AliUid | String | 1557809237** | 这个安全组所属用户ID。 |
| SecurityGroupI d | String | sg- bp1euoep32o6kvrw **** | 安全组ID。 |
| SecurityGroupI d | String | sg- bp67acfmxazb4pj** ** | 对应用户要查询的一个安全组。 |

**示例**

请求示例云服务器ECS

```
https://ecs.example.com/?Action=DescribeSecurityGroupReferences &RegionId=cn-qingdao-env17-d01 &SecurityGroupId.1=sg-bp1euoep32o6kvrw****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSecurityGroupReferencesResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
      <SecurityGroupReferences>
          <SecurityGroupReference>
              <SecurityGroupId>sg-bp1euoep32o6kvrw****</SecurityGroupId>
              <ReferencingSecurityGroups>
                  <ReferencingSecurityGroup>
                      <SecurityGroupId>sg-bp67acfmxazb4pi****</SecurityGroupId>
                      <AliUid>155780923770</AliUid>
                  </ReferencingSecurityGroup>
                  <ReferencingSecurityGroup>
                      <SecurityGroupId>sg-bp67acfmxazb4pj****</SecurityGroupId>
                      <AliUid>155780923770</AliUid>
                  </ReferencingSecurityGroup>
              </ReferencingSecurityGroups>
          </SecurityGroupReference>
      </SecurityGroupReferences>
</DescribeSecurityGroupReferencesResponse>
```

`JSON` 格式

```json
{
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984",
    "SecurityGroupReferences": [
        {
            "SecurityGroupId": "sg-bp1euoep32o6kvrw****",
            "SecurityReferencingGroups": [
                {
                    "AliUid": "1557809237**",
                    "SecurityGroupId": "sg-bp67acfmxazb4pi****"
                },
                {
                    "AliUid": "1557809237**",
                    "SecurityGroupId": "sg-bp67acfmxazb4pj****"
                }
```

]

```
        }
```

]

```
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云服务器ECS

| 400 | InvalidSecurityGrou pId.Malformed | The specified parameter SecurityGroupId is essential and size should less than 10 | 参数SecurityGroupId不能为空，且要查询的个数不能大于10个。 |
|---|---|---|---|
| 404 | InvalidSecurityGrou pId.NotFound | The SecurityGroupId provided does not exist in our records. | 指定的安全组在该用户账号下不存在，请您检查安全组ID是否正确。 |

##### RevokeSecurityGroup

调用RevokeSecurityGroup删除一条安全组入方向规则，撤销安全组入方向的权限设置。

**接口说明**

安全组的API文档中，流量的发起端为源端（Source），数据传输的接收端为目的端（Dest）。 以下任意一组参数可以匹配一条安全组入方向规则，只指定一个参数无法确定一条安全组规则。 撤销指定IP地址段的权限设置：IpProtocol、PortRange、（可选）SourcePortRange、NicType、 Policy、DestCidrIp和（可选）SourceCidrIp。 撤销其他安全组的权限设置：IpProtocol、PortRange、（可选）SourcePortRange、NicType、 Policy、（可选）DestCidrIp、DestGroupOwnerAccount和DestGroupId。 如果匹配的安全组规则不存在，此次RevokeSecurityGroup调用成功，但不会删除任何规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | RevokeSecurityGroup | 系统规定参数。取值： RevokeSecurityGroup。 |
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 目的端安全组所属地域ID。您可以调用DescribeRegions 查看最新的阿里云地域列表。 |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多详情，请参见《云服务器 ECS开发指南》中的如何保证幂等性章节。 |
| SecurityGr oupId | String | Query | 是 | sg-bp67acfmxazb4p**** | 目的端安全组ID。 |
| Policy | String | Query | 否 | accept | 访问权限。取值范围： accept：接受访问。 drop：拒绝访问，不发回拒绝信息。 默认值：accept。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Priority | String | Query | 否 | 1 | 安全组规则优先级。取值范围：1~100。 默认值：1。 |
| IpProtocol | String | Query | 否 | all | 传输层协议。参数值大小写敏感。取值范围： icmp。 icmpv6。 gre tcp。 udp。 all：支持所有协议。 |
| SourceCidr Ip | String | Query | 否 | 10.0.0.0/8 | 源端IP地址范围。支持CIDR 格式和IPv4格式的IP地址范围。 默认值：0.0.0.0/0。 |
| Ipv6Source CidrIp | String | Query | 否 | 2001:db8:1234:1a00::*** | 源端IPv6 CIDR地址段。 支持CIDR格式和IPv6格式的IP地址范围。 仅支持VPC类型的IP地址。 默认值：无。 |
| SourceGro upId | String | Query | 否 | sg-bp67acfmxazb4p**** | 需要撤销访问权限的源端安全组ID。 必须设置SourceGroupId 或者SourceCidrIp参数。 如果指定了 SourceGroupId没有指定参数SourceCidrIp，则参数NicType取值只能为 intranet。 如果同时指定了 SourceGroupId和 SourceCidrIp，则默认以 SourceCidrIp为准。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourcePref ixListId | String | Query | 否 | pl-x1j1k5ykzqlixdcy**** | 需要撤销访问权限的源端前缀列表 ID。 注意事项： 安全组的网络类型为经典网络时，不支持设置前缀列表。关于安全组以及前缀列表使用限制的更多信息，请参见安全组使用限制。 当您指定了 SourceCidrIp、 Ipv6SourceCidrIp或 SourceGroupId参数中的一个时，将忽略该参数。 |
| PortRange | String | Query | 否 | 1/200 | 目的端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为1~65535。使用正斜线 （/）隔开起始端口和终止端口。例如：1/200。 ICMP协议：-1/-1。 GRE协议：-1/-1。 ALL：-1/-1。 |
| DestCidrIp | String | Query | 否 | 10.0.0.0/8 | 目的端IP地址范围。支持 CIDR格式和IPv4格式的IP地址范围。 默认值：0.0.0.0/0。 |
| Ipv6DestCi drIp | String | Query | 否 | 2001:db8:1233:1a00::*** | 目的端IPv6 CIDR地址段。支持CIDR格式和IPv6格式的IP 地址范围。 说明仅支持VPC 类型的IP地址。 默认值：无。 |
| SourcePort Range | String | Query | 否 | 80/80 | 源端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为1~65535。使用正斜线 （/）隔开起始端口和终止端口。例如：1/200。 ICMP协议：-1/-1。 GRE协议：-1/-1。 ALL：-1/-1。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceGro upOwnerA ccount | String | Query | 否 | T***@aliyun.com | 跨账户删除安全组规则时，源端安全组所属的阿里云账户。 如果 SourceGroupOwnerAcc ount及 SourceGroupOwnerId均未设置，则认为是撤销您其他安全组的访问权限。 如果已经设置参数 SourceCidrIp，则参数 SourceGroupOwnerAcc ount无效。 |
| SourceGro upOwnerId | Long | Query | 否 | 12345678910 | 跨账户删除安全组规则时，源端安全组所属的阿里云账户 ID。 如果 SourceGroupOwnerId及 SourceGroupOwnerAcc ount均未设置，则认为是撤销您其他安全组的访问权限。 如果您已经设置参数 SourceCidrIp，则参数 SourceGroupOwnerId无效。 |
| NicType | String | Query | 否 | intranet | 经典网络类型安全组规则的网卡类型。取值范围： internet：公网网卡 intranet：内网网卡专有网络VPC类型安全组规则无需设置网卡类型，默认为intranet， 只能为intranet。 设置安全组之间互相访问时，即指定了 DestGroupId且没有指定DestCidrIp，只能为 intranet。 默认值：internet。 |
| Descriptio n | String | Query | 否 | TestDescription | 安全组规则描述。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Permission s | Array | Query | 否 | [ { "Policy": "accept", "Priority": "1", "IpProtocol": "TCP", "SourceCidrIp": "10.0.0.0/8", "Ipv6SourceCidrIp": "2001:db8:1234:1a00::*** ", "SourceGroupId": "sg- bp67acfmxa123b​****​", "SourcePrefixListId": "pl- x1j1k5ykzqlixdcy​****​", "PortRange": "1/200", "DestCidrIp": "10.0.0.0/8", "Ipv6DestCidrIp": "2001:db8:1233:1a00::*** ", "SourcePortRange": "80/80", "SourceGroupOwnerAcco unt": "T***@aliyun.com", "SourceGroupOwnerId": 12345678910, "NicType": "intranet", "Description": "This is description.", "PortRangeListId": "prl- 2ze9743​****​" }, { "Policy": "reject", "Priority": "2", ... } ] | 安全组规则数组。数组长度： 0~100。 |
| SecurityGr oupRuleId | Repea tList | Query | 否 | [ "sgr- bp67acfmxa123b***", "sgr-bp67acfmxa123b***" ] | 安全组规则 ID 数组。数组长度：0~100。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=RevokeSecurityGroup &SecurityGroupId=sg-bp67acfmxazb4p**** &SourceGroupId=sg-bp67acfmxazb4p**** &SourceGroupOwnerAccount=T***@aliyun.com &IpProtocol=tcp &PortRange=80/80 &Priority=1 &RegionId=cn-qingdao-env17-****
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式云服务器ECS

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****"
}
```

`XML` 格式

```xml
       <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7*****</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidSecurityGrou pId.Malformed | The specified parameter SecurityGroupId is not valid. | 指定的参数 SecurityGroupId 无效。 |
| 400 | InvalidSourceCidrIp. Malformed | The specified parameter SourceCidrIp is not valid. | 源 IP 地址范围参数格式不正确。 |
| 400 | MissingParameter | The input parameter SourceGroupId or SourceCidrIp cannot be both blank. | 参数 SourceGroupId 和 SourceCidrIp 不能同时为空。 |
| 400 | InvalidSourceGroupI d.Mismatch | Specified security group and source group are not in the same VPC. | 指定的安全组和源安全组不在一个 VPC 内。 |
| 400 | InvalidPriority.Malfor med | The parameter Priority is invalid. | 指定的参数 Priority 无效。 |
| 400 | InvalidPriority.Value NotSupported | The parameter Priority is invalid. | 指定的参数 Priority 无效。 |
| 400 | InvalidParamter.Con flict | The specified SecurityGroupId should be different from the SourceGroupId. | 授权与被授权安全组必须不同。 |
| 400 | InvalidDestCidrIp.Ma lformed | The specified parameter DestCidrIp is not valid. | 指定的 DestCidrIp 无效，请您检查该参数是否正确。 |
| 400 | InvalidParam.Source Ip | %s | 指定的参数 SourceIp 无效。 |
| 400 | InvalidParam.DestIp | %s | 指定的参数 DestIp 无效。 |
| 400 | InvalidParam.Ipv6De stCidrIp | %s | 您输入的参数无效。 |
| 400 | InvalidParam.Ipv6So urceCidrIp | %s | 您输入的参数无效。 |
| 400 | InvalidParam.Ipv4Pr otocolConflictWithIp v6Address | %s | 您输入的参数无效，请检查 IPv4 协议下是否填写了 IPv6 地址。 |
| 400 | InvalidParam.Ipv6Pr otocolConflictWithIp v4Address | %s | 您输入的参数无效，请检查IPv6协议下是否填写了 IPv4 地址。 |

|  | 云服务器ECS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ILLEGAL IPV6 CIDR _ _ | %s | 指定的IPv6地址无效。 |
| 400 | InvalidSecurityGrou pDiscription.Malfor med | The specified security group rule description is not valid. | 指定的安全组规则描述不合法。 |
| 400 | NotSupported.Classi cNetworkPrefixList | The prefix list is not supported when the network type of security group is classic. | 安全组的网络类型为经典网络，不支持前缀列表。 |
| 400 | InvalidParam.Source CidrIp | The specified param SourceCidrIp is not valid. | 参数SourceCidrIp不合法。 |
| 400 | InvalidParam.DestCi drIp | The specified parameter DestCidrIp is invalid. | 指定的参数“DestCidrIp”无效。 |
| 400 | InvalidParam.Permis sions | The specified parameter Permissions cannot coexist with other parameters. | 指定的参数Permissions不能与其他参数同时存在。 |
| 400 | InvalidParam.Duplic atePermissions | There are duplicate permissions in the specified parameter Permissions. | 指定的参数Permissions中存在重复的规则。 |
| 403 | InvalidNicType.Mism atch | Specified nic type conflicts with the authorization record. | 指定的 NIC 类型与规则信息冲突。 |
| 403 | InvalidGroupAuthIte m.NotFound | Specified group authorized item does not exist in our records. | 指定的组授权条目不存在。 |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | %s | 云产品托管的安全组不支持修改操作。 |
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组 ID 是否正确。 |
| 404 | InvalidSourceGroupI d.NotFound | The SourceGroupId provided does not exist in our records. | 指定的入方向安全组不存在。 |
| 404 | InvalidPrefixListId.N otFound | The specified prefix list was not found. | 前缀列表不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### RevokeSecurityGroupEgress

调用RevokeSecurityGroupEgress删除一条出方向安全组规则，撤销安全组出方向的访问权限。

**接口说明**

安全组的API文档中，流量的发起端为源端（Source），数据传输的接收端为目的端（Dest）。 以下任意一组参数可以确定一条安全组规则，只指定一个参数无法确定一条安全组规则。 撤销对指定IP地址段的访问权限，如以下请求示例：IpProtocol、PortRange、（可云服务器ECS 选）SourcePortRange、NicType、Policy、DestCidrIp和（可选）SourceCidrIp。

```
https://ecs.example.com/?Action=RevokeSecurityGroupEgress &SecurityGroupId=sg-bp67acfmxazb4ph*** &IpProtocol=tcp &DestCidrIp=10.0.0.0/8 &PortRange=-22/22 &NicType=intranet &Policy=Allow
```

`&<`公共请求参数> 撤销对其他安全组的访问权限，如以下请求示例：IpProtocol、PortRange、（可选）SourcePortRange、 NicType、Policy、（可选）DestCidrIp、DestGroupOwnerAccount和DestGroupId。

```
https://ecs.example.com/?Action=RevokeSecurityGroupEgress &SecurityGroupId=sg-bp67acfmxazb4ph*** &DestGroupId=sg-bp67acfmxazb4pi*** &DestGroupOwnerAccount=t***@aliyun.com &IpProtocol=tcp &PortRange=22/22 &NicType=intranet &Policy=Drop
```

`&<`公共请求参数> 如果匹配的安全组规则不存在，此次RevokeSecurityGroupEgress调用成功，但不会删除任何规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | RevokeSecurityGroupEgre ss | 系统规定参数。取值： RevokeSecurityGroupEgre ss |
| RegionId | String | Query | 是 | cn-qingdao-env17-d01 | 源端安全组所属地域ID。您可以调用DescribeRegions查询地域ID。 |
| ClientToke n | String | Query | 否 | 473469C7-AA6F-4DC5- B3DB-A3DC0DE3C83E | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken 只支持ASCII字符，且不能超过64 个字符。更多详情，请参见 《云服务器ECS开发指南》中的如何保证幂等性章节。 |
| SecurityGr oupId | String | Query | 是 | sg-bp67acfmxazb4p**** | 源端安全组ID。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Policy | String | Query | 否 | accept | 访问权限。取值范围： accept：接受访问。 drop：拒绝访问，不返回拒绝信息，表现为发起端请求超时或者无法建立连接的类似信息。 默认值：accept。 |
| Priority | String | Query | 否 | 1 | 安全组规则优先级。数字越小，代表优先级越高。取值范围：1~100。 默认值：1。 |
| IpProtocol | String | Query | 否 | tcp | 传输层协议。不区分大小写。 取值范围： ICMP。 GRE。 TCP。 UDP。 ALL：支持所有协议。 |
| DestCidrIp | String | Query | 否 | 10.0.0.0/8 | 目的端IP地址范围。支持 CIDR格式和IPv4格式的IP地址范围。 默认值：无。 |
| Ipv6DestCi drIp | String | Query | 否 | 2001:db8:1233:1a00::*** | 目的端IPv6 CIDR地址段。 支持CIDR格式和IPv6格式的IP地址范围。 仅支持VPC类型的IP地址。 默认值：无。 |
| DestGroupI d | String | Query | 否 | sg-bp67acfmxazb4p**** | 需要撤销访问权限的目的端安全组ID。 必须设置DestGroupId或者DestCidrIp参数。 如果指定了DestGroupId 没有指定参数 DestCidrIp，则参数 NicType的取值只能为 intranet。 如果同时指定了 DestGroupId和 DestCidrIp，则默认以 DestCidrIp为准。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DestPrefix ListId | String | Query | 否 | pl-x1j1k5ykzqlixdcy**** | 需要撤销访问权限的目的端前缀列表。 注意事项： 当您指定了 DestCidrIp、 Ipv6DestCidrIp、 DestGroupId参数中的一个时，将忽略该参数。 |
| PortRange | String | Query | 否 | 22/22 | 目的端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为1~65535。使用斜线 （/）隔开起始端口和终止端口。正确示范：1/200； 错误示范：200/1。 ICMP协议：-1/-1。 GRE协议：-1/-1。 ALL：-1/-1。 |
| SourceCidr Ip | String | Query | 否 | 10.0.0.0/8 | 源端IP地址范围。支持CIDR 格式和IPv4格式的IP地址范围。 默认值：无。 |
| Ipv6Source CidrIp | String | Query | 否 | 2001:db8:1234:1a00::*** | 源端IPv6 CIDR地址段。 支持CIDR格式和IPv6格式的IP地址范围。 仅支持VPC类型的IP地址。 默认值：无。 |
| SourcePort Range | String | Query | 否 | 22/22 | 源端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为1~65535。使用正斜线 （/）隔开起始端口和终止端口。例如：1/200。 ICMP协议：-1/-1。 GRE协议：-1/-1。 ALL：-1/-1。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DestGroup OwnerAcco unt | String | Query | 否 | T***@aliyun.com | 跨账户删除安全组规则时，目的端安全组所属的阿里云账户。 如果 DestGroupOwnerAccou nt 及DestGroupOwnerId 均未设置，则认为是撤销您其他安全组的访问权限。 如果已经设置参数 DestCidrIp，则参数 DestGroupOwnerAccou nt无效。 |
| DestGroup OwnerId | Long | Query | 否 | 12345678910 | 跨账户删除安全组规则时，目的端安全组所属的阿里云账户 ID。 如果DestGroupOwnerId 及 DestGroupOwnerAccou nt均未设置，则认为是撤销您其他安全组的访问权限。 如果您已经设置参数 DestCidrIp，则参数 DestGroupOwnerId无效。 |
| NicType | String | Query | 否 | intranet | 经典网络类型安全组规则的网卡类型。取值范围： internet：公网网卡。 intranet：内网网卡。 专有网络VPC类型安全组规则无需设置网卡类型，默认为intranet， 只能为intranet。 设置安全组之间互相访问时，即指定了 DestGroupId且没有指定DestCidrIp，只能为 intranet。 默认值：internet。 |
| Descriptio n | String | Query | 否 | TestDescription | 安全组规则的描述。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Permission s | Array | Query | 否 | [ { "Policy": "accept", "Priority": "1", "IpProtocol": "TCP", "SourceCidrIp": "10.0.0.0/8", "Ipv6SourceCidrIp": "2001:db8:1234:1a00::*** ", "SourceGroupId": "sg- bp67acfmxa123b​****​", "SourcePrefixListId": "pl- x1j1k5ykzqlixdcy​****​", "PortRange": "1/200", "DestCidrIp": "10.0.0.0/8", "Ipv6DestCidrIp": "2001:db8:1233:1a00::*** ", "SourcePortRange": "80/80", "SourceGroupOwnerAcco unt": "T***@aliyun.com", "SourceGroupOwnerId": 12345678910, "NicType": "intranet", "Description": "This is description.", "PortRangeListId": "prl- 2ze9743​****​" }, { "Policy": "reject", "Priority": "2", ... } ] | 安全组规则数组。数组长度： 0~100。 |
| SecurityGr oupRuleId | Repea tList | Query | 否 | [ "sgr- bp67acfmxa123b***", "sgr-bp67acfmxa123b***" ] | 安全组规则 ID 数组。数组长度：0~100。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RevokeSecurityGroupEgress &RegionId=cn-qingdao-env17-d01 &SecurityGroupId=sg-bp67acfmxazb4p****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

云服务器ECS `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -540 | InvalidIpProtocol.ValueNotSuppo rted | The parameter IpProtocol must be specified with case insensitive TCP, UDP, ICMP, GRE or All. |
| 400 | -545 | InvalidIpProtocol.ValueNotSuppo rted | The parameter IpProtocol must be specified with case insensitive TCP, UDP, ICMP, GRE or All. |
| 400 | -555 | InvalidIpPortRange.Malformed | The specified parameter PortRange is not valid. |
| 400 | -535 | InvalidDestCidrIp.sMalformed | The specified parameter DestCidrIp is not valid. |
| 400 | -525 | MissingParameter | The input parameter DestGroupId or DestCidrIp cannot be both blank. |
| 400 | Abs.InvalidPolicy.Ma lformed | InvalidPolicy.Malformed | The specified parameter %s is not valid. |
| 400 | Abs.InvalidNicType. ValueNotSupported | InvalidNicType.ValueNotSupport ed | The specified parameter %s is not valid. |
| 400 | GROUP AUTH MISM _ _ ATCH | InvalidDestGroupId.Mismatch | Specified security group and destination group are not in the same VPC. |
| 400 | INVALID CIDR _ | InvalidDestCidrIp.Malformed | The specified parameter DestCidrIp is not valid. |
| 400 | MissingParameter.D est | MissingParameter.Dest | One of the parameters DestCidrIp, Ipv6DestCidrIp, DestGroupId or DestPrefixListId in %s must be specified. |
| 400 | InvalidParam.PortRa nge | InvalidParam.PortRange | The specified parameter %s is not valid. It should be two integers less than 65535 in ?/? format. |
| 400 | Abs.InvalidIpProtoco l.Malformed | InvalidIpProtocol.ValueNotSuppo rted | The parameter %s must be specified with case insensitive TCP, UDP, ICMP, GRE or All. |
| 400 | InvalidPriority.Malfor med | InvalidPriority.Malformed | The parameter Priority is invalid. |
| 400 | InvalidParam.Priorit y | InvalidPriority.ValueNotSupporte d | The specified parameter %s is invalid. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -536 | InvalidDestCidrIp.Malformed | The specified parameter DestCidrIp is not valid. |
| 400 | InvalidParam.Source Ip | InvalidParam.SourceIp | The Parameters SourceCidrIp and Ipv6SourceCidrIp in %s cannot be set at the same time. |
| 400 | InvalidParam.DestIp | InvalidParam.DestIp | The Parameters DestCidrIp and Ipv6DestCidrIp in %s cannot be set at the same time. |
| 400 | InvalidParam.Ipv6De stCidrIp | InvalidParam.Ipv6DestCidrIp | The specified parameter %s is not valid. |
| 400 | InvalidParam.Ipv6So urceCidrIp | InvalidParam.Ipv6SourceCidrIp | The specified parameter %s is not valid. |
| 400 | -1011017 | InvalidParam.Ipv4ProtocolConflic tWithIpv6Address | IPv6 address cannot be specified for IPv4-specific protocol. |
| 400 | -1011018 | InvalidParam.Ipv6ProtocolConflic tWithIpv4Address | IPv4 address cannot be specified for IPv6-specific protocol. |
| 400 | ILLEGAL IPV6 CIDR _ _ | InvalidParameter.Ipv6CidrIp | The specified Ipv6CidrIp is not valid. |
| 400 | ENTERPRISE GROUP _ CAN NOT AUTHORI _ _ _ ZE TO OTHER GRO _ _ _ UP | InvalidGroupAuthParameter.Ope rationDenied | The security group can not authorize to enterprise level security group. |
| 400 | Abs.InvalidGroupId. Malformed | InvalidSecurityGroupId.Malforme d | The specified parameter SecurityGroupId is not valid. |
| 400 | -550 | InvalidPortRange.Malformed | The specified parameter PortRange must set. |
| 400 | -6 | InvalidSourcePortRange.Malform ed | The specified parameter SourcePortRange is not valid. |
| 400 | -559 | InvalidSecurityGroupDiscription. Malformed | The specified security group rule description is not valid. |
| 400 | CLASSIC GROUP NO _ _ T SUPPORT PREFIX _ _ _ LIST | NotSupported.ClassicNetworkPre fixList | The prefix list is not supported when the network type of security group is classic. |
| 400 | InvalidParam.Source CidrIp | InvalidParam.SourceCidrIp | The specified parameter %s is not valid. |
| 400 | SOURCE CIDR IP M _ _ _ ALFORMED | InvalidParam.SourceCidrIp | The specified param SourceCidrIp is not valid. |
| 400 | InvalidParam.DestCi drIp | InvalidParam.DestCidrIp | The specified parameter %s is not valid. |
| 400 | DEST CIDR IP MALF _ _ _ ORMED | InvalidParam.DestCidrIp | The specified parameter DestCidrIp is invalid. |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParam.Permis sions | InvalidParam.Permissions | The specified parameter Permissions cannot coexist with other parameters. |
| 400 | InvalidParam.Securit yGroupPermissionR epeated | InvalidParam.DuplicatePermissio ns | There are duplicate permissions in the specified parameter Permissions. |
| 400 | InvalidParam.Securit yGroupRuleId | InvalidParam.SecurityGroupRuleI d | The specified parameter SecurityGroupRuleId is not valid. |
| 400 | InvalidParam.Securit yGroupRuleIdRepeat ed | InvalidParam.SecurityGroupRuleI dRepeated | The specified parameter SecurityGroupRuleId is repeated. |
| 400 | -1011007 | InvalidParam.SecurityGroupRuleI d | The specified parameter SecurityGroupRuleId is not valid. |
| 400 | ENTERPRISE GROUP _ AUTH ERROR _ _ | InvalidGroupParameter.Operatio nDenied | The attributes Policy, SourceGroupId, DestGroupId of enterprise level security groups are not allowed to be set or modified. |
| 400 | InvalidSecurityGrou pRule.RuleNotExist | InvalidSecurityGroupRule.RuleN otExist | The specified rule does not exist. |
| 401 | OPERATE GROUP N _ _ OT AUTHORIZED _ | InvalidOperation.SecurityGroupN otAuthorized | The specified security group is not authorized to operate. |
| 403 | -591 | InvalidNicType.Mismatch | Specified nic type conflicts with the authorization record. |
| 403 | -570 | InvalidGroupAuthItem.NotFound | Specified group authorized item does not exist in our records. |
| 403 | -566 | InvalidSecurityGroup.IsSame | The authorized SecurityGroupId should be different from the DestGroupId. |
| 403 | -565 | InvalidParamter.Conflict | The specified SecurityGroupId should be different from the SourceGroupId. |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | InvalidOperation.ResourceMana gedByCloudProduct | %s |
| 403 | InvalidOperation.Se curityGroupService Managed | InvalidOperation.ResourceMana gedByCloudProduct | %s |
| 403 | InvalidOperation.Se curityGroupService Managed | InvalidOperation.ResourceMana gedByCloudProduct | %s |
| 404 | -560 | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |
| 404 | -530 | InvalidDestGroupId.NotFound | The DestGroupId provided does not exist in our records. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | DEST GROUP NOT _ _ _ EXIST | InvalidDestGroupId.NotFound | The DestGroupId provided does not exist in our records. |
| 404 | InvalidSecurityGrou pId.NotFound | InvalidSecurityGroupId.NotFoun d | The specified SecurityGroupId does not exist. |
| 404 | SG ACL ID NOT EXI _ _ _ _ STS | InvalidSecurityGroupRuleId.NotF ound | The specified SecurityGroupRuleId is not exists. |
| 404 | PREFIX LIST NOT F _ _ _ OUND | InvalidPrefixListId.NotFound | The specified prefix list was not found. |

##### ModifySecurityGroupAttribute

调用ModifySecurityGroupAttribute修改一个安全组的名称或者描述。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySecurityGr oupAttribute | 系统规定参数。取值： ModifySecurityGroupAttribute |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| SecurityGroupId | String | 是 | sg- bp67acfmxazb4p **** | 安全组ID。 |
| SecurityGroupNa me | String | 否 | SecurityGroupTes tName | 安全组名称。 长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 和 https:// 开头。可以包含数字、半角冒号（:）、下划线（ ）或 _ 者短划线（-）。 默认值：空。 |
| Description | String | 否 | TestDescription | 安全组描述信息。长度为2~256个英文或中文字符，不能以 http:// 和 https:/ /开头。 默认值：空。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

云服务器ECS 请求示例

```
https://ecs.example.com/?Action=ModifySecurityGroupAttribute &SecurityGroupId=sg-bp67acfmxazb4p**** &RegionId=cn-qingdao-env17-d01 &SecurityGroupName=SecurityGroupTestName
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组ID是否正确。 |
| 400 | InvalidSecurityGrou pName.Malformed | Specified security group name is not valid. | 指定的安全组名称格式不合法。请您按照规则进行配置：默认值为空，长度为2-128个英文或中文字符，必须以大小字母或中文开头，可包含数字，英文句号（.），下划线（ ）或 _ 连字符（-），安全组名称会展示在控制台。不能以http://和https://开头。 |
| 400 | InvalidSecurityGrou pDiscription.Malfor med | Specified security group description is not valid. | 指定的安全组描述不合法。 |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | %s | 云产品托管的安全组不支持修改操作。 |

##### ModifySecurityGroupPolicy

调用ModifySecurityGroupPolicy修改普通安全组内网连通策略，企业安全组不支持修改组内内网连通策略。

**接口说明**

调用该接口时，您需要注意： 参数InnerAccessPolicy的值为Accept时，安全组内的实例之间的网络是互通的。此时，遵循Accept优先原则，即，安全组内的实例之间的网络一直保持互通，不受用户自定义安全组规则影响。 参数InnerAccessPolicy的值为Drop时，安全组内的实例之间的网络是隔离的。此时，遵循用户自定义安全组规则优先原则，即，安全组内的实例之间的网络虽然是隔离的，但您可以自定义安全组规则改变内网状态，例如，您可以通过AuthorizeSecurityGroup使安全组内的两台ECS实例网络互通。 云服务器ECS 您可以通过DescribeSecurityGroupAttribute查询当前安全组内网连通策略。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySecurityGr oupPolicy | 系统规定参数。取值： ModifySecurityGroupPolicy。 |
| InnerAccessPolicy | String | 是 | Drop | 安全组内的ECS实例之间的内网连通策略。 取值范围： Accept：互通。 Drop：隔离。 取值不区分大小写。 |
| RegionId | String | 是 | cn-qingdao- env17-**** | 安全组所属地域ID。您可以调用 DescribeRegions查看最新的地域列表。 |
| SecurityGroupId | String | 是 | sg- bp67acfmxazb4p h*** | 安全组的ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见《云服务器ECS开发指南》中的如何保证幂等性章节。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifySecurityGroupPolicy &RegionId=cn-qingdao-env17-**** &SecurityGroupId=sg-bp67acfmxazb4ph*** &InnerAccessPolicy=Drop
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7*****</RequestId>
```

云服务器ECS `JSON` 格式

```json
{
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7*****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidSecurityGrou pId.Malformed | The SecurityGroupId is invalid. Only letters, numbers and underscores are supported. Maximum length is 100 characters. | 指定的参数 SecurityGroupId 格式错误，该参数仅支持字母，数字和下划线且最大长度为 100 个字符。 |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | %s | 云产品托管的安全组不支持修改操作。 |
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组 ID 是否正确。 |

##### ModifySecurityGroupRule

调用ModifySecurityGroupRule修改指定安全组中的一条入方向安全组规则。 接口说明指定安全组规则 ID 修改安全组规则时，您需要注意以下使用限制： 安全组规则的授权对象分为IPv4 的 CIDR 地址块（或 IP 地址）、IPv6 的 CIDR 地址块（或 IP 地址）、安全组，您不能通过该接口修改已有安全组规则的授权对象类型。如原来授权对象类型为 IPv4 的 CIDR 地址块， 您可以更改为另一个 IPv4 的 CIDR 地址块（或 IP 地址），但不能修改为 IPv6 的 CIDR 地址块（或 IP 地址）或安全组。 字段不支持从非空修改为空，如果需要修改建议先增加一条新规则，再删除当前规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ModifySecurityGroupRule | 系统规定参数。取值： ModifySecurityGroupRule |
| RegionId | String | Query | 是 | cn-qingdao-env17-d01 | 目标安全组所属地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多详情，请参见《云服务器 ECS开发指南》中的如何保证幂等性章节。 |
| SecurityGr oupId | String | Query | 是 | sg-bp67acfmxazb4p**** | 安全组 ID。 |
| SecurityGr oupRuleId | String | Query | 否 | sgr-bp67acfmxa123b*** | 安全组规则 ID。 |
| Policy | String | Query | 否 | accept | 访问权限。取值范围： accept：接受访问 drop：拒绝访问，不返回拒绝信息。 默认值：accept。 |
| Priority | String | Query | 否 | 1 | 安全组规则优先级。取值范围：1~100。 默认值：1。 |
| IpProtocol | String | Query | 否 | all | 传输层协议。不区分大小写。 取值范围： ICMP ICMPv6 GRE TCP UDP ALL：支持所有协议。 |
| SourceCidr Ip | String | Query | 否 | 10.0.0.0/8 | 设置访问权限的源端 IPv4 CIDR 地址块。支持 CIDR 格式和 IPv4 格式的 IP 地址范围。 默认值：无。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ipv6Source CidrIp | String | Query | 否 | 2001:db8:1233:1a00::*** | 设置访问权限的源端IPv4 CIDR地址块。支持CIDR格式和IPv4格式的IP地址范围。 仅支持VPC类型的IP地址，且该参数与 SourceCidrIp参数不可同时设置。 默认值：无。 |
| SourceGro upId | String | Query | 否 | sg-bp67acfmxazb4p**** | 设置访问权限的源端安全组 ID。至少设置一项 SourceGroupId或者 SourceCidrIp参数。 如果指定了 SourceGroupId没有指定参数SourceCidrIp，则参数NicType取值只能为 intranet。 如果同时指定了 SourceGroupId和 SourceCidrIp，则默认以 SourceCidrIp为准。 |
| PortRange | String | Query | 否 | 80/80 | 目的端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为1~65535。使用斜线 （/）隔开起始端口和终止端口。正确示范：1/200； 错误示范：200/1 ICMP协议：-1/-1 GRE协议：-1/-1 all：-1/-1 |
| DestCidrIp | String | Query | 否 | 10.0.0.0/8 | 目的端IP地址范围。支持 CIDR格式和IPv4格式的IP地址范围。 默认值：0.0.0.0/0。 |
| Ipv6DestCi drIp | String | Query | 否 | 2001:db8:1234:1a00::*** | 目的端IPv6 CIDR地址段。支持CIDR格式和IPv6格式的IP 地址范围。 仅支持VPC类型的IP地址。 默认值：无。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourcePort Range | String | Query | 否 | 80/80 | 源端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为1~65535。使用斜线 （/）隔开起始端口和终止端口。例如：1/200。 ICMP协议：-1/-1 GRE协议：-1/-1 all：-1/-1 |
| SourceGro upOwnerA ccount | String | Query | 否 | T***@aliyun.com | 跨账户设置安全组规则时，源端安全组所属的阿里云账户。 如果 SourceGroupOwnerAcc ount及 SourceGroupOwnerID均未设置，则认为是设置您其他安全组的访问权限。 如果已经设置参数 SourceCidrIp，则参数 SourceGroupOwnerAcc ount无效。 |
| SourceGro upOwnerId | Long | Query | 否 | 12345678910 | 跨账户设置安全组规则时，源端安全组所属的阿里云账户 ID。 如果 SourceGroupOwnerId及 SourceGroupOwnerAcc ount均未设置，则认为是设置您其他安全组的访问权限。 如果您已经设置参数 SourceCidrIp，则参数 SourceGroupOwnerId无效。 |
| NicType | String | Query | 否 | intranet | 网卡类型。 根据安全组规则 ID 修改规则时，不支持修改该参数。如果需要修改， 建议先增加一条新规则，再删除当前规则。 |
| Descriptio n | String | Query | 否 | This is a new security group rule. | 安全组规则的描述信息。长度为1~512个字符。 |

**返回数据**

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifySecurityGroupRule &SecurityGroupId=sg-bp67acfmxazb4p**** &SourceGroupId=sg-bp67acfmxazb4p**** &SourceGroupOwnerAccount=T***@aliyun.com &IpProtocol=all &PortRange=80/80 &Policy=accept &Description=This is a new security group rule. &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
}
```

`XML` 格式

```xml
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidSecurityGrou pId.NotFound | The specified SecurityGroupId does not exist. | 指定的安全组在该用户账号下不存在，请您检查安全组ID是否正确。 |
| 404 | InvalidSourceGroupI d.NotFound | The SourceGroupId provided does not exist in our records. | 指定的入方向安全组不存在。 |
| 400 | OperationDenied | The specified IpProtocol does not exist or IpProtocol and PortRange do not match. | 指定的IP协议不存在，或与端口范围不匹配。 |
| 400 | InvalidIpProtocol.Mal formed | The specified parameter "PortRange" is not valid. | IP协议参数格式不正确，PortRange 参数不正确。 |
| 403 | InvalidSourceGroupI d.Mismatch | NicType is required or NicType expects intrnet. | 需要明确IP段类型参数或者网络类型必须为内网。 |
| 400 | InvalidSourceCidrIp. Malformed | The specified parameter "SourceCidrIp" is not valid. | 源IP地址范围参数格式不正确。 |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 403 | MissingParameter | The input parameter "SourceGroupId" or "SourceCidrIp" cannot be both blank. | 参数SourceGroupId和 SourceCidrIp不能同时为空。 |
| 400 | InvalidPolicy.Malfor med | The specified parameter "Policy" is not valid. | 指定的参数无效，请您检查该参数是否正确。 |
| 400 | InvalidNicType.Valu eNotSupported | The specified NicType does not exist. | 指定的网络类型不存在，请您检查网络类型是否正确。 |
| 400 | InvalidNicType.Mism atch | Specified nic type conflicts with the authorization record. | 指定的NIC类型与规则信息冲突。 |
| 403 | AuthorizationLimitEx ceed | The limit of authorization records in the security group reaches. | 安全组授权规则数达到上限，请您检查授权规则是否合理。 |
| 403 | InvalidParamter.Con flict | The specified SecurityGroupId should be different from the SourceGroupId. | 授权与被授权安全组必须不同。 |
| 400 | InvalidSourceGroupI d.Mismatch | Specified security group and source group are not in the same VPC. | 指定的安全组和源安全组不在一个 VPC内。 |
| 400 | InvalidSourceGroup. NotFound | Specified source security group does not exist. | 指定的安全组入方向规则不存在，或相关参数缺失。 |
| 400 | VPCDisabled | Can't use the SecurityGroup in VPC. | VPC 不支持安全组。 |
| 400 | InvalidPriority.Malfor med | The parameter Priority is invalid. | 指定的参数Priority无效。 |
| 400 | InvalidPriority.Value NotSupported | The parameter Priority is invalid. | 指定的参数Priority无效。 |
| 500 | InternalError | The request processing has failed due to some unknown error. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |
| 403 | InvalidNetworkType. Mismatch | The specified SecurityGroup network type should be same with SourceGroup network type (vpc or classic). | 指定的SecurityGroup的网络类型必须与SouceGroup的网络类型一致。 |
| 400 | InvalidSecurityGrou pDiscription.Malfor med | The specified security group rule description is not valid. | 指定的安全组规则描述不合法。 |
| 404 | SecurityGroupRule. NotFound | The target security group rule not exist. | 目标安全组规则不存在。 |
| 400 | MissingParameter.S ource | Either SourceCidrIp or SourceGroupId must be specified. | 参数SourceCidrIp和 SourceGroupId不能同时为空。 |

云服务器ECS

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidIpProtocol.Val ueNotSupported | The parameter IpProtocol must be specified with case insensitive TCP, UDP, ICMP, GRE or All. | 协议类型只能是TCP、UDP、ICMP、 GRE或者All。 |
| 400 | InvalidParam.Source Ip | %s | 指定的参数SourceIp无效。 |
| 400 | InvalidParam.DestIp | %s | 指定的参数DestIp无效。 |
| 400 | InvalidParam.Ipv6De stCidrIp | %s | 您输入的参数无效。 |
| 400 | InvalidParam.Ipv6So urceCidrIp | %s | 您输入的参数无效。 |
| 400 | InvalidParam.Ipv4Pr otocolConflictWithIp v6Address | %s | 您输入的参数无效，请检查IPv4协议下是否填写了IPv6地址。 |
| 400 | InvalidParam.Ipv6Pr otocolConflictWithIp v4Address | %s | 您输入的参数无效，请检查IPv6协议下是否填写了IPv4地址。 |
| 400 | ILLEGAL IPV6 CIDR _ _ | %s | 指定的IPv6地址无效。 |
| 400 | InvalidSourcePortRa nge.Malformed | The specified parameter "SourcePortRange" is not valid. | 指定的参数SourcePortRange无效。 |
| 400 | InvalidSecurityGrou pId.Malformed | The specified parameter "SecurityGroupId" is not valid. | 指定的参数SecurityGroupId无效。 |

##### ModifySecurityGroupEgressRule

调用ModifySecurityGroupEgressRule修改一条出方向安全组规则。 接口说明指定安全组规则 ID 修改安全组规则时，您需要注意以下使用限制： 安全组规则的授权对象分为IPv4 的 CIDR 地址块（或 IP 地址）、IPv6 的 CIDR 地址块（或 IP 地址）、安全组，您不能通过该接口修改已有安全组规则的授权对象类型。如原来授权对象类型为 IPv4 的 CIDR 地址块， 您可以更改为另一个 IPv4 的 CIDR 地址块（或 IP 地址），但不能修改为 IPv6 的 CIDR 地址块（或 IP 地址）或安全组。 字段不支持从非空修改为空，如果需要修改建议先增加一条新规则，再删除当前规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ModifySecurityGroupEgre ssRule | 系统规定参数。取值： ModifySecurityGroupRule |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-qingdao-****-d01 | 源端安全组所属地域 ID。您可以调用 DescribeRegions 查看最新的阿里云地域列表。 |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 更多详情，请参见《云服务器 ECS开发指南》中的如何保证幂等性章节。 |
| SecurityGr oupId | String | Query | 是 | sg-bp67acfmxazb4p**** | 安全组 ID。 |
| SecurityGr oupRuleId | String | Query | 否 | sgr-bp67acfmxazb4q**** | 安全组规则 ID。您可以通过 DescribeSecurityGroupAtt ribute 查询安全组规则 ID。 |
| Policy | String | Query | 否 | accept | 访问权限。取值范围： accept：接受访问。 drop：拒绝访问，不返回拒绝信息。 默认值：accept。 |
| Priority | String | Query | 否 | 1 | 安全组规则优先级。取值范围：1~100。 默认值：1。 |
| IpProtocol | String | Query | 否 | TCP | 传输层协议。不区分大小写。 取值范围： ICMP ICMPv6 GRE TCP UDP ALL：支持所有协议。 |
| DestCidrIp | String | Query | 否 | 10.0.0.0/8 | 目的端 IPv4 CIDR 地址块。 支持 CIDR 格式和 IPv4 格式的 IP 地址范围。 默认值：无。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ipv6DestCi drIp | String | Query | 否 | 2001:db8:1233:1a00::*** | 目的端 IPv6 CIDR 地址块。 支持 CIDR 格式和 IPv6 格式的 IP 地址范围。 说明仅支持 VPC 类型的 IP 地址，且该参数与DestCidrIp参数不可同时设置。 默认值：无。 |
| DestGroupI d | String | Query | 否 | sg-bp67acfmxa123b**** | 需要设置访问权限的目的端安全组 ID。至少设置一项 DestGroupId或者 DestCidrIp参数。 至少设置DestGroupId、 DestCidrIp、 Ipv6DestCidrIp 或 DestPrefixListId 参数中的一项。 如果指定了DestGroupId 没有指定参数 DestCidrIp，则参数 NicType 取值只能为 intranet。 如果同时指定了 DestGroupId 和 DestCidrIp，则默认以 DestCidrIp 为准。 |
| PortRange | String | Query | 否 | 80/80 | 目的端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为 1~65535。使用斜线 （/）隔开起始端口和终止端口。例如：1/200。 ICMP协议：-1/-1。 GRE协议：-1/-1。 ALL：-1/-1。 |
| SourceCidr Ip | String | Query | 否 | 10.0.0.0/8 | 源端 IPv4 CIDR 地址块。支持 CIDR 格式和 IPv4 格式的 IP 地址范围。 默认值：无。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ipv6Source CidrIp | String | Query | 否 | 2001:db8:1234:1a00::*** | 源端 IPv6 CIDR 地址块。支持 CIDR 格式和 IPv6 格式的 IP 地址范围。 说明仅支持 VPC 类型的 IP 地址，且该参数与SourceCidrIp 参数不可同时设置。 默认值：无。 |
| SourcePort Range | String | Query | 否 | 80/80 | 源端安全组开放的传输层协议相关的端口范围。取值范围： TCP/UDP协议：取值范围为 1~65535。使用斜线 （/）隔开起始端口和终止端口。例如：1/200 ICMP协议：-1/-1。 GRE协议：-1/-1。 ALL：-1/-1。 |
| DestGroup OwnerAcco unt | String | Query | 否 | E***@Alibaba.com | 跨账户设置安全组规则时，目的端安全组所属的阿里云账户。 |
| DestGroup OwnerId | Long | Query | 否 | 1234567890 | 跨账户设置安全组规则时，目的端安全组所属的阿里云账户 ID。 |
| NicType | String | Query | 否 | intranet | 网卡类型。 说明根据安全组规则 ID 修改规则时， 不支持修改该参数。如果需要修改，建议先增加一条新规则，再删除当前规则。 |
| Descriptio n | String | Query | 否 | This is a new securitygroup rule. | 安全组规则的描述信息。长度为 1~512 个字符。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

云服务器ECS

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifySecurityGroupEgressRule &SecurityGroupId=sg-bp67acfmxazb4ph*** &DestGroupId=sg-bp67acfmxazb4pi*** &SourceGroupOwnerAccount=E***@Alibaba.com &IpProtocol=tcp &PortRange=80/80 &Policy=allow &Description=Thisisanewsecuritygrouprule.
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

`XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

#### SSH密钥对

##### CreateKeyPair

调用CreateKeyPair创建一对SSH密钥对。我们会为您保管密钥的公钥部分，并返回未加密的PEM编码的 PKCS#8格式私钥。您需要自行妥善保管私钥部分。

**接口说明**

除了调用CreateKeyPair创建密钥对之外，您还可以使用第三方工具创建密钥对，然后上传（ImportKeyPair） 到某一阿里云地域，其使用方法和我们为您创建的密钥对是一致的。 您在每个地域的密钥对数最高为500对。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateKeyPair | 系统规定参数，取值：CreateKeyPair。 |
| KeyPairName | String | 是 | TestKeyPairV23 | 密钥对名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http://和https://开头。可以包含数字、半角冒号（:）、下划线（ ）或者短划线（-）。 _ |

云服务器ECS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 密钥对所在的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
|---|---|---|---|---|
| Tag.N.Key | String | 否 | TestKey | 密钥对的标签键。N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以aliyun和acs:开头， 不能包含http://或者https://。 |
| Tag.N.Value | String | 否 | TestValue | 密钥对的标签值。N的取值范围：1~20。最多支持128个字符，不能以acs:开头，不能包含http://或者https://。 |
| ResourceGroupId | String | 否 | rg- bp67acfmxazb4p h*** | SSH密钥对所在的企业资源组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| KeyPairFingerPr int | String | 89:f0:ba:62:ac:b8:a a:e1:61:5e:fd:81:69: 86:6d:6b:f0:c0:5a:** | 密钥对的指纹。根据RFC4716定义的公钥指纹格式，采用MD5信息摘要算法。更多详情，请参见RFC4716。 |
| KeyPairId | String | ssh- bp67acfmxazb4ph** * | SSH密钥对的ID。 |
| KeyPairName | String | TestKeyPairV23 | 密钥对名称。 |
| PrivateKeyBody | String | MIIEpAIBAAKCAQEAt ReyMzLIcBH78EV2zj **** | 密钥对的私钥。PEM编码的PKCS#8格式的私钥部分。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &KeyPairName=TestKeyPairV23
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
      <KeyPairName>test</KeyPairName>
      <KeyPairId>ssh-bp67acfmxazb4ph***</KeyPairId>
      <KeyPairFingerPrint>89:f0:ba:62:ac:b8:aa:e1:61:5e:fd:81:69:86:6d:6b:f0:c0:5a:**
</KeyPairFingerPrint>
      <PrivateKeyBody>MIIEpAIBAAKCAQEAtReyMzLIcBH78EV2zj****</PrivateKeyBody>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "KeyPairName": "TestKeyPairV23",
    "KeyPairId": "ssh-bp67acfmxazb4ph***",
    "KeyPairFingerPrint": "89:f0:ba:62:ac:b8:aa:e1:61:5e:fd:81:69:86:6d:6b:f0:c0:5a:**",
    "PrivateKeyBody": "MIIEpAIBAAKCAQEAtReyMzLIcBH78EV2zj****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidKeyPairName. Malformed | Specified Key Pair name is not valid. | 密钥对名称不合法。 |
| 403 | QuotaExceed.KeyPai r | The key pair quota exceeds. | 密钥对数量已达上限。 |
| 400 | KeyPair.AlreadyExist | The key pair already exist. | 密钥对已存在，请不要重复添加。 |
| 404 | InvalidResourceGro up.NotFound | The ResourceGroup provided does not exist in our records. | 资源组并不在记录中。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 403 | QuotaExceed.Tags | %s | 标签数超过可以配置的最大数量。 |

##### AttachKeyPair

**接口说明**

当您使用该接口时，需要注意： 如果ECS实例原先使用密码认证，绑定密钥对后，可能会导致密码认证方式被禁用。 如果实例处于运行中（Running）状态，重启实例（RebootInstance）后，SSH密钥对生效。 如果实例处于已停止（Stopped）状态，启动实例（StartInstance）后，SSH密钥对生效。 云服务器ECS

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | 是 | AttachKeyPair | 系统规定参数，取值： AttachKeyPair。 |
| RegionId | Strin g | Quer y | 是 | cn-qingdao-env17-d01 | SSH密钥对所在的地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| KeyPairNa me | Strin g | Quer y | 是 | KeyPairV25 | SSH密钥对名称。 |
| InstanceIds | Strin g | Quer y | 是 | ["i-xxxxxxxxx", "i- yyyyyyyyy", … "i- zzzzzzzzz"] | 绑定SSH密钥对的实例ID。取值可以由多台实例ID组成一个 JSON数组，最多支持50个 ID，ID之间用半角逗号（,）隔开。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Results | Array | / | 绑定密钥对成功或失败的结果集合。 |
| -Code | String | 200 | 传递的操作状态码，其中200表示操作成功。 |
| -Message | String | successful | 传递的操作信息，当code=200时，message为 successful。 |
| -InstanceId | String | i-instanc**** | 实例ID。 |
| -Success | String | true | 此次操作是否成功。 |
| KeyPairName | String | KeyPairV25 | 密钥对的名称。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | String | 2 | 绑定密钥对的实例总数量。 |

云服务器ECS

| FailCount | String | 0 | 绑定密钥对失败的实例数量。 |
|---|---|---|---|

**示例**

请求示例

```
&InstanceIds=["i-xxxxx****", "i-yyyyy****", … "i-zzzzz****"] &KeyPairName=KeyPairV25 &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "TotalCount": 2,
    "RequestId": "4ADF7A06-66BD-4FBF-A2ED-2364E41D8C06",
    "Results": {
        "Result": [
            {
                "Message": "successful",
                "InstanceId": "i-m5eg7be9ndloji64j***",
                "Success": true,
                "Code": "200"
            },
            {
                "Message": "successful",
                "InstanceId": "i-m5e25x2mwr0hk33dw***",
                "Success": true,
                "Code": "200"
            }
```

]

```json
    },
    "FailCount": 0
}
```

`XML` 格式云服务器ECS

```xml
   <TotalCount>2</TotalCount>
   <RequestId>4ADF7A06-66BD-4FBF-A2ED-2364E41D8C06</RequestId>
   <Results>
      <Result>
         <Message>successful</Message>
         <InstanceId>i-m5eg7be9ndloji64j***</InstanceId>
         <Success>true</Success>
         <Code>200</Code>
      </Result>
      <Result>
         <Message>successful</Message>
         <InstanceId>i-m5e25x2mwr0hk33dw***</InstanceId>
         <Success>true</Success>
         <Code>200</Code>
      </Result>
   </Results>
   <FailCount>0</FailCount>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidKeyPairName. NotFound | The specified KeyPairName does not exist in our records. | 指定的 KeyPairName 不存在。 |
| 403 | DependencyViolatio n.WindowsInstance | The instance creating is windows, cannot use ssh key pair to login | 指定的实例是 windows 操作系统， 此类实例不支持 SSH 密钥对登录。 |
| 403 | InstanceKeyPairLimi tExceeded | Exceeding the allowed amount of instance that an key pair can attach. | 单次处理的密钥对数量超出上限。 |
| 400 | InvalidInstanceIds.V alueNotSupported | The specified parameter InstanceIds is not valid. | 指定的 InstanceId 参数不合法。 |
| 400 | DependencyViolatio n.IoOptimize | The specified parameter InstanceIds is not valid. | 指定的实例 ID 不合法。 |

Ecs 2014-05-26

##### DetachKeyPair

**接口说明**

云服务器ECS 使用该接口时，请注意：

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DetachKeyPair | 系统规定参数，取值：DetachKeyPair。 |
| InstanceIds | String | 是 | ["i-xxxxx****", "i- yyyyy****", … "i- zzzzz****"] | 解绑SSH密钥对的实例ID。取值可以是由多台实例ID组成的一个JSON数组，最多支持50 个ID，ID之间用半角逗号（,）隔开。 |
| KeyPairName | String | 是 | KeyPairV26 | SSH密钥对名称。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | SSH密钥对所在的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FailCount | String | 0 | 解绑密钥对失败的实例数量。 |
| KeyPairName | String | KeyPairV26 | 密钥对的名称。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| Results | Array |  | 解绑密钥对成功或失败的结果集合。 |
| Result |  |  |  |
| Code | String | 200 | 传递的操作状态码，其中200表示操作成功。 |
| InstanceId | String | i-instanc**** | 实例ID。 |
| Message | String | successful | 传递的操作信息，当code=200时，message为 successful。 |
| Success | String | true | 此次操作是否成功。 |
| TotalCount | String | 2 | 解绑密钥对的实例总数量。 |

**示例**

云服务器ECS 请求示例

```
&RegionId=cn-qingdao-env17-d01 &InstanceIds=["i-xxx****", "i-yyy****"] &KeyPairName=test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <TotalCount>2</TotalCount>
   <RequestId>834B3E6B-2D1D-482F-81A4-810C327D4735</RequestId>
   <Results>
      <Result>
         <Message>successful</Message>
         <InstanceId>i-m5eg7be9ndloji64j***</InstanceId>
         <Success>true</Success>
         <Code>200</Code>
      </Result>
      <Result>
         <Message>successful</Message>
         <InstanceId>i-m5e25x2mwr0hk33dw***</InstanceId>
         <Success>true</Success>
         <Code>200</Code>
      </Result>
   </Results>
   <FailCount>0</FailCount>
```

`JSON` 格式

```json
{
    "TotalCount": 2,
    "RequestId": "834B3E6B-2D1D-482F-81A4-810C327D4735",
    "Results": {
        "Result": [
            {
                "Message": "successful",
                "InstanceId": "i-m5eg7be9ndloji64j***",
                "Success": true,
                "Code": "200"
            },
            {
                "Message": "successful",
                "InstanceId": "i-m5e25x2mwr0hk33dw***",
                "Success": true,
                "Code": "200"
            }
```

]

```json
    },
    "FailCount": 0
}
```

云服务器ECS

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidKeyPairName. NotFound | The specified KeyPairName does not exist in our records. | 指定的 KeyPairName 不存在。 |
| 403 | DependencyViolatio n.WindowsInstance | The instance creating is windows, cannot use ssh key pair to login | 指定的实例是 windows 操作系统， 此类实例不支持 SSH 密钥对登录。 |
| 403 | InstanceKeyPairLimi tExceeded | Exceeding the allowed amount of instance that an key pair can attach. | 单次处理的密钥对数量超出上限。 |
| 400 | InvalidInstanceIds.V alueNotSupported | The specified parameter InstanceIds is not valid. | 指定的 InstanceId 参数不合法。 |

##### DeleteKeyPairs

**接口说明**

查询实例信息时（DescribeInstances），会显示SSH密钥对名称（KeyPairName），但不再显示其他相关信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteKeyPairs | 系统规定参数，取值：DeleteKeyPairs。 |
| KeyPairNames | String | 是 | ["skp- bp67acfmxazb4p h***", "skp- bp67acfmxazb4pi ***", … "skp- bp67acfmxazb4p k***"] | SSH密钥对名称。取值可以由多个SSH密钥对名称组成一个JSON数组，最多支持100对 SSH密钥对，名称之间用半角逗号（,）隔开。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | SSH密钥对所在的地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求 ID。 |

云服务器ECS

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &KeyPairNames=["skp-bp67acfmxazb4ph***", "skp-bp67acfmxazb4pi***", … "skpbp67acfmxazb4pk***"]
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
| 400 | MissingParameter | The input parameter "KeyPairNames" that is mandatory for processing this request is not supplied. | 未提供必需的KeyPairNames。 |
| 400 | InvalidKeyPairName s.ValueNotSupporte d | The specified parameter "KeyPairNames" is not valid. | 密钥对名称不合法。 |
| 403 | InstanceKeyPairLimi tExceeded | Exceeding the allowed amount of instance which will be deleted. | 要删除的密钥对数量达到上限。 |

##### DescribeKeyPairs

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeKeyPairs | 系统规定参数，取值：DescribeKeyPairs。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 密钥对所在的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| KeyPairName | String | 否 | *Finance* | 密钥对名称。支持正则表达式模糊搜索，使用*匹配子表达式，示例： *SshKey ：查询以SshKey结尾的密钥对名称，包括SshKey。 SshKey* ：查询以SshKey开头的密钥对名称，包括SshKey。 *SshKey* ：查询名称中间有SshKey 的密钥对，包括SshKey。 SshKey ：精确匹配SshKey。 |
|---|---|---|---|---|
| KeyPairFingerP rint | String | 否 | XXXXXXXXXX | 密钥对的指纹。根据RFC4716定义的公钥指纹格式，采用MD5信息摘要算法。更多详情，请参见RFC4716。 |
| PageNumber | Integer | 否 | 1 | 密钥对列表的页码。起始值：1 默认值：1 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数。最大值：50 默认值：10 |
| Tag.N.Key | String | 否 | FinanceDeptKey | 密钥对的标签键。N的取值范围：1~20 |
| Tag.N.Value | String | 否 | FinanceDeptValu e | 密钥对的标签值。N的取值范围：1~20 |
| ResourceGroupI d | String | 否 | rg- resourcegrou**** | 密钥对所在的企业资源组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| KeyPairs | Array |  | 密钥对信息集合。 |
| KeyPair |  |  |  |
| CreationTime | String | 2019-12- 04T13:35:00Z | 密钥对的创建时间。 |
| KeyPairFingerPr int | String | xxxxxxxxxx | 密钥对的指纹。 |
| KeyPairName | String | KeyPairV27 | 密钥对的名称。 |
| ResourceGroup Id | String | rg-resourcegrou**** | 资源组ID。 |
| Tags | Array |  | 密钥对的标签。 |
| Tag |  |  |  |

云服务器ECS

| TagKey | String | FinanceDeptKey | 密钥对的标签键。 |
|---|---|---|---|
| TagValue | String | FinanceDeptValue | 密钥对的标签值。 |
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 1 | 密钥对的总数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeKeyPairs &RegionId=cn-qingdao-env17-d01 &KeyPairFingerPrint=xxxxxxxxxx &KeyPairName=test &PageNumber=1 &PageSize=20
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <PageNumber>1</PageNumber>
      <PageSize>2</PageSize>
      <TotalCount>1</TotalCount>
      <KeyPairs>
            <KeyPair>
                  <CreationTime>2018-10-10T01:00Z</CreationTime>
                  <ResourceGroupId></ResourceGroupId>
                  <KeyPairName>test</KeyPairName>
                  <KeyPairFingerPrint>xxxxxxxxxx</KeyPairFingerPrint>
            </KeyPair>
      </KeyPairs>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
 "PageNumber": 1,
 "PageSize": 2,
 "TotalCount": 1,
 "KeyPairs": {
  "KeyPair": [{
   "CreationTime": "2018-10-10T01:00Z",
   "ResourceGroupId": "",
   "KeyPairName": "test",
   "KeyPairFingerPrint": "xxxxxxxxxx"
  }]
 },
 "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

#### 弹性网卡

##### CreateNetworkInterface

**接口说明**

新创建的弹性网卡处于可用（Available）状态。 弹性网卡只支持附加到同一可用区的VPC类型实例。 一个弹性网卡只能附加到一台实例。附加到新实例之前您需要将其与当前实例分离。 弹性网卡重新附加到另一台实例时，其属性不变，网络流量也会重定向到新的实例。 创建弹性网卡时，如果您需要设置IPv6地址，则需要确保指定的交换机开通了IPv6。 一个账号在一个阿里云地域内默认最多可创建100个弹性网卡。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateNetworkInt erface | 系统规定参数，取值： CreateNetworkInterface。 |
| RegionId | String | 是 | cn-qingdao-**** | 实例所在地域的ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| VSwitchId | String | 是 | vsw- bp1s5fnvk4gn2tw s03*** | 指定VPC的交换机ID。弹性网卡的私网IP地址在交换机的IP地址段内的空闲地址中取值。 |

云服务器ECS

| Tag.N.Key | String | 否 | TestKey | 弹性网卡的标签键。N的取值范围：1~20。 一旦传入该值，则不允许为空字符串。最多支持128个字符，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 |  |  |  |
|---|---|---|---|---|---|---|---|
| Tag.N.Value | String | 否 | TestValue | 弹性网卡的标签值。N的取值范围：1~20。 一旦传入该值，可以为空字符串。最多支持 128个字符，不能以 acs: 开头，不能包含 http:// 或者 https:// 。 |  |  |  |
| PrimaryIpAddress | String | 否 | 172.17.**.*** | 弹性网卡的主私有IP地址。 指定IP必须是在所属交换机的地址段内的空闲地址，不指定则默认随机分配该交换机中的空闲地址。 |  |  |  |
| SecurityGroupId | String | 否 | sg- bp1fg655nh68xy z9i*** | 加入一个安全组。安全组和弹性网卡必须在同一个专有网络VPC中。 说明调用接口时，您必须设置 SecurityGroupId 或 Securi tyGroupIds.N 其中一个，但不支持同时设置。 |  |  |  |
|  |  |  |  |  | Securi |  |  |
| NetworkInterface Name | String | 否 | testNetworkInterf aceName | 弹性网卡名称。长度为2~128个英文或中文字符。必须以大小写字母或中文开头，不能以 http:// 或者 https:// 开头。可以包含数字、半角冒号（:）、下划线（ ） _ 或者短划线（-）。 默认值：空。 |  |  |  |
| Description | String | 否 | testDescription | 弹性网卡的描述信息。长度为2~256个英文或中文字符，不能以 http:// 或者 https:// 开头。 默认值：空。 |  |  |  |
| SecondaryPrivate IpAddressCount | Integer | 否 | 1 | 指定私有IP地址数量，让ECS为您自动创建IP 地址。 |  |  |  |

|  |  |  | SecurityGroupId |
|---|---|---|---|
|  |  | tyGroupIds.N |  |

云服务器ECS

| QueueNumber | Integer | 否 |  | 1 | 弹性网卡队列数。取值范围：1~2048。 默认值：空。 说明绑定弹性网卡时，该值必须少于实例规格支持单块网卡的最大队列数。实例规格的单块网卡最大队列数可以通过DescribeInstanceTypes接口查询 MaximumQueueNumberPerEni 字段。在绑定时会采用实例规格的弹性网卡默认队列数，实例规格的弹性网卡默认队列数可以通过 DescribeInstanceTypes接口查询 SecondaryEniQueueNumber 字段。 |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| ClientToken | String | 否 |  | 123e4567-e89b- 12d3-a456- 426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。更多详情，请参见《云服务器ECS开发指南》中的如何保证幂等性章节。 |  |  |  |  |  |
| Ipv6AddressCoun t | Integer | 否 |  | 1 | 为弹性网卡指定随机生成的IPv6地址数量。 取值范围：1~10。 说明如果您需要为弹性网卡设置IPv6地址，则必须设置 Ipv6Addresses.N 或者 Ipv6AddressCount 的其中一个，但不能同时设置这两个参数。 |  |  |  |  |  |
| SecurityGroupIds. N | RepeatLi st | 否 |  | sg- bp1fg655nh68xy z9i*** | 加入一个或多个安全组。安全组和弹性网卡必须在同一个专有网络VPC中。N的取值范围与弹性网卡能够加入安全组配额有关。 说明调用接口时，您必须设置 SecurityGroupId 或 Securi tyGroupIds.N 其中一个，但不支持同时设置。 |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Securi |  |  |
| PrivateIpAddress. N | RepeatLi st | 否 |  | 172.***.***.177 | 从弹性网卡所属交换机的CIDR地址段内的空闲地址中选择一个或多个辅助私有IP地址。N 的取值范围：1~10。 说明分配辅助私有IP地址时， 您不能同时指定参数 PrivateIpAddress.N 和参数 SecondaryPrivateIpAddressCo unt 。 |  |  |  |  |  |
|  |  |  |  |  |  | unt |  |  |  |  |

|  |  |  | SecurityGroupId |
|---|---|---|---|
|  |  | tyGroupIds.N |  |

云服务器ECS

| Ipv6Address.N | RepeatLi st | 否 | 2001:db8:1234:1 a00::**** | 为弹性网卡指定一个或多个IPv6地址。支持设置最多10个IPv6地址，即N的取值范围： 1~10。 取值示例： Ipv6Address.1=2001:db8:1234:1a00:: 说明如果您需要为弹性网卡设置IPv6地址，则必须设置 Ipv6Addresses.N 或者 Ipv6AddressCount 的其中一个，但不能同时设置这两个参数。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Description | String | testDescription | 弹性网卡的描述信息。 |
| Ipv6Sets | Array of Ipv6Set |  | 弹性网卡已分配的IPv6地址。 |
| Ipv6Set |  |  |  |
| Ipv6Address | String | 2001:db8:1234:1a0 0::**** | IPv6地址。 |
| MacAddress | String | 00:16:3e:12:**:** | 弹性网卡的MAC地址。 |
| NetworkInterfa ceId | String | eni- bp14v2sdd3v8htln** ** | 弹性网卡ID。 |
| NetworkInterfa ceName | String | my-eni-name | 弹性网卡的名称。 |
| OwnerId | String | 123456**** | 弹性网卡的所属账号ID。 |
| PrivateIpAddres s | String | 172.17.**.** | 弹性网卡的私网IP地址。 |
| PrivateIpSets | Array of PrivateIpSet |  | PrivateIpSet组成的集合。 |
| PrivateIpSet |  |  |  |
| Primary | Boolean | true | 是否是主私网IP地址。 |
| PrivateIpAddres s | String | 172.17.**.** | 实例的私网IP地址。 |

云服务器ECS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |
|---|---|---|---|
| ResourceGroup Id | String | rg- 2ze88m67qx5z**** | 该参数未开放使用。 |
| SecurityGroupI ds | List | sg- bp18kz60mefsicfg** ** | 所属的安全组集合。 |
| ServiceID | Long | 12345678910 | 该参数未开放使用。 |
| ServiceManage d | Boolean | true | 该参数未开放使用。 |
| Status | String | Available | 弹性网卡的状态。 |
| Tags | Array of Tag |  | 标签。 |
| Tag |  |  |  |
| TagKey | String | TestKey | 标签键。 |
| TagValue | String | TestValue | 标签值。 |
| Type | String | Secondary | 弹性网卡的类型。 |
| VSwitchId | String | vsw- bp16usj2p27htro3** ** | VPC的交换机ID。 |
| VpcId | String | vpc- bp1j7w3gc1cexjqd** ** | 网卡所属的专有网络VPC ID。 |
| ZoneId | String | cn-hangzhou-e | 可用区ID。 |

**示例**

请求示例云服务器ECS

```
http(s)://ecs.example.com/?Action=CreateNetworkInterface &RegionId=cn-qingdao-**** &SecurityGroupIds.1=sg-bp1fg655nh68xyz9i*** &SecurityGroupIds.2=sg-bp67acfmxazb4ph*** &VSwitchId=vsw-bp1s5fnvk4gn2tws03*** &Tag.1.Key=TestKey &Tag.1.Value=TestValue &PrimaryIpAddress=172.17.**.*** &NetworkInterfaceName=testNetworkInterfaceName &Description=testDescription &ClientToken=123e4567-e89b-12d3-a456-426655440000 &Ipv6AddressCount=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <Status>Available</Status>
      <PrivateIpAddress>172.17.**.**</PrivateIpAddress>
      <Description>testDescription</Description>
      <ZoneId>cn-hangzhou-e</ZoneId>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
      <VSwitchId>vsw-bp16usj2p27htro3****</VSwitchId>
      <NetworkInterfaceName>my-eni-name</NetworkInterfaceName>
      <NetworkInterfaceId>eni-bp14v2sdd3v8htln****</NetworkInterfaceId>
      <MacAddress>00:16:3e:12:**:**</MacAddress>
      <SecurityGroupIds>sg-bp18kz60mefsicfg****</SecurityGroupIds>
      <Type>Secondary</Type>
      <Ipv6Sets>
            <Ipv6Address>2001:db8:1234:1a00::****</Ipv6Address>
      </Ipv6Sets>
      <OwnerId>123456****</OwnerId>
      <VpcId>vpc-bp1j7w3gc1cexjqd****</VpcId>
      <Tags>
            <TagKey>TestKey</TagKey>
            <TagValue>TestValue</TagValue>
      </Tags>
      <PrivateIpSets>
            <PrivateIpAddress>172.17.**.**</PrivateIpAddress>
            <Primary>true</Primary>
      </PrivateIpSets>
```

`JSON` 格式云服务器ECS

```json
{
        "Status": "Available",
        "PrivateIpAddress": "172.17.**.**",
        "Description": "testDescription",
        "ZoneId": "cn-hangzhou-e",
        "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
        "VSwitchId": "vsw-bp16usj2p27htro3****",
        "NetworkInterfaceName": "my-eni-name",
        "NetworkInterfaceId": "eni-bp14v2sdd3v8htln****",
        "MacAddress": "00:16:3e:12:**:**",
        "SecurityGroupIds": "sg-bp18kz60mefsicfg****",
        "Type": "Secondary",
        "Ipv6Sets": {
            "Ipv6Address": "2001:db8:1234:1a00::****"
        },
        "OwnerId": "123456****",
        "VpcId": "vpc-bp1j7w3gc1cexjqd****",
        "Tags": {
            "TagKey": "TestKey",
            "TagValue": "TestValue"
        },
        "PrivateIpSets": {
            "PrivateIpAddress": "172.17.**.**",
            "Primary": true
        }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 400 | InvalidParameter | %s | 无效的参数。 |
| 400 | InvalidInstanceID.M alformed | %s | 参数 InstanceId 格式错误。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 400 | InvalidOperation.Det achPrimaryEniNotAll owed | %s | 不允许解绑实例的主网卡。 |
| 400 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |

云服务器ECS

| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
|---|---|---|---|
| 400 | JoinedGroupLimitExc eed | %s | 指定资源所能加入的安全组数量达到上限。具体信息请参见错误信息%s占位符的实际返回结果。 |
| 400 | InvalidPrivateIpAddr ess.Duplicated | Specified private IP address is duplicated. | 指定的私网 IP 已经被使用，请您更换 IP 再重试。 |
| 400 | InvalidParameter.Co nflict | %s | 您输入的参数无效，请检查参数之间是否冲突。%s为变量，将根据调用 API的实际情况动态返回错误信息。 |
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey 已经过期。 |
| 403 | Forbidden.NotSuppo rtRAM | %s | 暂不支持RAM用户执行该操作。 |
| 403 | Forbidden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 403 | MaxEniCountExceed ed | %s | 已超过可以操作的最大弹性网卡数。 |
| 403 | EniPerInstanceLimit Exceeded | %s | 实例绑定的弹性网卡数量已经达到了最大限度，不能在为实例绑定弹性网卡。 |
| 403 | InvalidOperation.Av ailabilityZoneMisma tch | %s | 该操作无效。 |
| 403 | InvalidOperation.Vp cMismatch | %s | 您的操作无效，请确认该操作中的 VPC 与其它参数是否匹配。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | InvalidSecurityGrou pId.NotVpc | %s | 参数 SecurityGroupId 无效，该安全组的网络类型不是专有网络。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 403 | InvalidVSwitchId.IpN otEnough | %s | 指定的交换机内 IP 数量不足。 |
| 403 | InvalidVSwitchId.IpI nvalid | %s | 指定的私网 IP 无效。 |
| 403 | QuotaExceed.Tags | %s | 标签数超过可以配置的最大数量。%s 为变量，将根据调用API的实际情况动态返回错误信息。 |
| 403 | InvalidIp.IpRepeated | %s | 指定的 IP 重复。 |
| 403 | MaxEniPrivateIpsCo untExceeded | %s | 指定的ENI分配的辅助私网IP数量超过限制，具体信息请参见错误信息%s 占位符的实际返回结果。 |

云服务器ECS

| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | %s | 云产品托管的安全组不支持修改操作。 |
|---|---|---|---|
| 403 | InvalidParameter.In validEniQueueNumb er | %s | 弹性网卡队列数有误，具体信息请参见错误信息%s占位符的实际返回结果。 |
| 403 | InvalidOperation.Ma xEniQueueNumberE xceeded | %s | 弹性网卡队列数超过上限，具体信息请参见错误信息%s占位符的实际返回结果。 |
| 403 | InvalidOperation.Exc eedInstanceTypeQu eueNumber | %s | 弹性网卡队列总数超过上限，具体信息请参见错误信息%s占位符的实际返回结果。 |
| 404 | InvalidEcsId.NotFou nd | %s | 指定的实例 ID 不存在。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡 ID 不存在。 |
| 404 | InvalidVSwitchId.Not Found | %s | 指定的交换机不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |
| 404 | InvalidResourceGro up.NotFound | The ResourceGroup provided does not exist in our records. | 资源组并不在记录中。 |
| 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. | 内部错误，请重试。如果多次尝试失败，请提交工单。 |

##### AttachNetworkInterface

调用AttachNetworkInterface附加一个弹性网卡（ENI）到一台专有网络VPC类型ECS实例上。

**接口说明**

调用该接口时，请注意：

| 于可用（ Available 中（ Running ）或者 Stopped ）状态。 | Available |
|---|---|
| Stopped |  |

如果实例最后一次启动时间在2018年4月1日之前（包括但不限于启动新购的实例、重启、重

**说明**

开机），您必须提前调用RebootInstance重启一直保持运行中状态的实例，否则无法附加弹性网卡。 一台实例可以同时附加多个弹性网卡。 实例与弹性网卡所在的虚拟交换机必须属于同一可用区、同一专有网络VPC。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | AttachNetworkInt erface | 系统规定参数，取值： AttachNetworkInterface。 |

云服务器ECS

| InstanceId | String | 是 | i- bp16qstyvxj9gpq w**** | 实例ID。 |
|---|---|---|---|---|
| NetworkInterfa ceId | String | 是 | eni- bp17pdijfczax1hu ji**** | 弹性网卡ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所在地域的ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=AttachNetworkInterface &RegionId=cn-qingdao-env17-d01 &InstanceId=i-bp16qstyvxj9gpqw**** &NetworkInterfaceId=eni-bp17pdijfczax1huji****
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
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey已经过期。 |
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |

云服务器ECS

| 403 | Forbidden.NotSuppo rtRAM | %s | 暂不支持 RAM 用户执行该操作。 |
|---|---|---|---|
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 403 | Forbidden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 400 | InvalidParameter | %s | 无效的参数。 |
| 400 | InvalidInstanceID.M alformed | %s | 参数“InstanceId”格式错误。 |
| 400 | InvalidOperation.Inv alidRegion | %s | 指定的参数“RegionId”无效。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 400 | InvalidOperation.Det achPrimaryEniNotAll owed | %s | 不允许解绑实例的主网卡。 |
| 404 | InvalidEcsId.NotFou nd | %s | 指定的实例 ID 不存在。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡 ID 不存在。 |
| 404 | InvalidVSwitchId.Not Found | %s | 指定的交换机不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |
| 403 | MaxEniCountExceed ed | %s | 已超过可以操作的最大弹性网卡数。 |
| 403 | EniPerInstanceLimit Exceeded | %s | 实例绑定的弹性网卡数量已经达到了最大限度，不能在为实例绑定弹性网卡。 |
| 403 | InvalidOperation.Av ailabilityZoneMisma tch | %s | 该操作无效。 |
| 403 | InvalidOperation.Vp cMismatch | %s | 您的操作无效，请确认该操作中的 VPC 与其它参数是否匹配。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | InvalidSecurityGrou pId.NotVpc | %s | 参数“SecurityGroupId”无效，该安全组的网络类型不是专有网络。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 400 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |

云服务器ECS

| 403 | InvalidInstanceId.No tFound | %s | 指定的实例不存在，请确认参数“InstanceId”是否正确。 |
|---|---|---|---|
| 400 | InvalidOperation.Inv alidGeneration | %s | 该操作无效。 |
| 400 | InvalidParams.EniId | %s | 指定的参数“EniId”无效。 |
| 403 | InvalidOperation.Ipv 4CountExceeded | %s | IPv4 数量达到上限，导致该操作无效。 |
| 403 | InvalidOperation.Eni ServiceManaged | %s | 操作无效。 |
| 403 | InvalidOperation.Ipv 6NotSupport | %s | IPv6 不支持当前操作。 |

##### AssignPrivateIpAddresses

调用AssignPrivateIpAddresses为一块弹性网卡分配一个或多个辅助私有IP地址。分配的IP地址为网卡所属交换机（VSwitch）的空闲私有IP地址，您可以通过直接设置指定的IP地址分配，或者仅设置地址数量让系统自动分配。

**接口说明**

只支持可用（Available）或者已绑定（InUse）状态下的弹性网卡。 操作主网卡时，网卡附加的实例必须处于运行中（Running）或者已停止（Stopped）状态。

**请求参数**

| 名称 | 类型 |  | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| Action | String |  | 是 | AssignPrivateIpA ddresses | 系统规定参数，取值： AssignPrivateIpAddresses。 |
| NetworkInterfaceI d | String |  | 是 | eni- bp67acfmxazb4p **** | 弹性网卡ID。 |
| RegionId | String |  | 是 | cn-qingdao- env17-d01 | 弹性网卡所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| PrivateIpAddress. N | RepeatLi st |  | 否 | 10.1.2.1 | 从弹性网卡所属交换机的空闲IP地址中选择一个或多个辅助私有IP地址。N的取值范围： 弹性网卡处于可用（ Available ）状态：1~10。 弹性网卡处于已绑定（ InUse ）状态：受到实例规格限制，更多信息，请参见云服务器ECS产品简介中的实例规格章节。 分配辅助私有IP地址时，您不能同时指定参数 PrivateIpAddress.N 和参数 SecondaryPrivateIpAddressCount 。 |

云服务器ECS

| SecondaryPrivate IpAddressCount | Integer | 否 | 1 | 指定私有IP地址数量，自动从交换机的空闲 IP地址中分配IP地址。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AssignedPrivat eIpAddressesSe t | Struct |  | 已分配辅助私有IP地址的弹性网卡集合。 |
| NetworkInterfa ceId | String | eni- bp67acfmxazb4p*** * | 弹性网卡ID。 |
| PrivateIpSet | List | [ "192.168.**.**" ] | 私网IP地址集合。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=AssignPrivateIpAddresses &NetworkInterfaceId=eni-bp67acfmxazb4p**** &RegionId=cn-qingdao-env17-d01 &PrivateIpAddress.1=10.1.2.1 &PrivateIpAddress.2=10.1.2.2
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
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey已经过期。 |

云服务器ECS

| 403 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
|---|---|---|---|
| 403 | Forbidden.NotSuppo rtRAM | %s | 暂不支持RAM用户执行该操作。 |
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 403 | Forbidden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 400 | InvalidParameter | %s | 无效的参数。 |
| 400 | InvalidInstanceID.M alformed | %s | 参数InstanceId格式错误。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 400 | InvalidOperation.Det achPrimaryEniNotAll owed | %s | 不允许解绑实例的主网卡。 |
| 404 | InvalidEcsId.NotFou nd | %s | 指定的实例ID不存在。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡ID不存在。 |
| 404 | InvalidVSwitchId.Not Found | %s | 指定的交换机不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组ID不存在。 |
| 403 | MaxEniCountExceed ed | %s | 已超过可以操作的最大弹性网卡数。 |
| 403 | EniPerInstanceLimit Exceeded | %s | 实例绑定的弹性网卡数量已经达到了最大限度，不能在为实例绑定弹性网卡。 |
| 403 | InvalidOperation.Av ailabilityZoneMisma tch | %s | 该操作无效。 |
| 403 | InvalidOperation.Vp cMismatch | %s | 您的操作无效，请确认该操作中的 VPC与其它参数是否匹配。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | InvalidSecurityGrou pId.NotVpc | %s | 参数SecurityGroupId无效，该安全组的网络类型不是专有网络。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 404 | InvalidInstanceId.No tFound | %s | 指定的实例不存在，请确认参数 InstanceId是否正确。 |

云服务器ECS

| 403 | InvalidVSwitchId.IpN otEnough | %s | 指定的交换机内IP数量不足。 |
|---|---|---|---|
| 403 | InvalidVSwitchId.IpI nvalid | %s | 指定的私网IP无效。 |
| 403 | InvalidIp.IpAssigned | %s | 指定的IP已被分配。 |
| 403 | MaxEniPrivateIpsCo untExceeded | %s | 指定的ENI分配的辅助私网IP数量超过限制，具体信息请参见错误信息%s 占位符的实际返回结果。 |
| 403 | Operation.Conflict | %s | 您当前的操作与其它正在执行的操作有冲突，请稍后重试。 |
| 400 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
| 400 | InvalidAction | %s | 操作无效。 |
| 403 | InvalidOperation.Ipv 4CountExceeded | %s | IPv4数量达到上限，导致该操作无效。 |
| 403 | InvalidOperation.Eni ServiceManaged | %s | 操作无效。 |
| 400 | InvalidPrivateIpAddr ess.Duplicated | Specified private IP address is duplicated. | 指定的私网IP已经被使用，请您更换 IP再重试。 |
| 403 | InvalidIp.IpRepeated | %s | 指定的IP重复。 |

##### UnassignPrivateIpAddresses

调用UnassignPrivateIpAddresses从一块弹性网卡删除一个或多个辅助私有IP地址。

**接口说明**

只支持**可用**（Available）或者**已绑定**（InUse）状态下的弹性网卡。 操作主网卡时，网卡附加的实例必须处于**运行中**（Running）或者**已停止**（Stopped）状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | UnassignPrivateI pAddresses | 系统规定参数。取值： UnassignPrivateIpAddresses |
| NetworkInterfa ceId | String | 是 | eni- bp67acfmxazb4p h*** | 弹性网卡ID。 |
| PrivateIpAddres s.N | RepeatLi st | 是 | 192.168.**.1 | 一个或多个需要删除的辅助私有IP地址。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 资源所属地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

云服务器ECS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=UnassignPrivateIpAddresses &NetworkInterfaceId=eni-bp67acfmxazb4ph*** &PrivateIpAddress.1=192.168.**.1 &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>04F0F334-1335-436C-A1D7-6C044FE70008</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE70008"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey已经过期。 |
| 403 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 403 | Forbidden.NotSuppo rtRAM | %s | 暂不支持 RAM 用户执行该操作。 |
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 403 | Forbidden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 400 | InvalidParameter | %s | 无效的参数。 |
| 400 | InvalidInstanceID.M alformed | %s | 参数“InstanceId”格式错误。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |

云服务器ECS

| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
|---|---|---|---|
| 400 | InvalidOperation.Det achPrimaryEniNotAll owed | %s | 不允许解绑实例的主网卡。 |
| 404 | InvalidEcsId.NotFou nd | %s | 指定的实例 ID 不存在。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡 ID 不存在。 |
| 404 | InvalidVSwitchId.Not Found | %s | 指定的交换机不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |
| 403 | MaxEniCountExceed ed | %s | 已超过可以操作的最大弹性网卡数。 |
| 403 | EniPerInstanceLimit Exceeded | %s | 实例绑定的弹性网卡数量已经达到了最大限度，不能在为实例绑定弹性网卡。 |
| 403 | InvalidOperation.Av ailabilityZoneMisma tch | %s | 该操作无效。 |
| 403 | InvalidOperation.Vp cMismatch | %s | 您的操作无效，请确认该操作中的 VPC 与其它参数是否匹配。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | InvalidSecurityGrou pId.NotVpc | %s | 参数“SecurityGroupId”无效，该安全组的网络类型不是专有网络。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 404 | InvalidInstanceId.No tFound | %s | 指定的实例不存在，请确认参数“InstanceId”是否正确。 |
| 403 | InvalidVSwitchId.IpI nvalid | %s | 指定的私网 IP 无效。 |
| 403 | InvalidIp.IpUnassign ed | %s | 指定的 IP 未被分配。 |
| 403 | Operation.Conflict | %s | 您当前的操作与其它正在执行的操作有冲突，请稍后重试。 |
| 400 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
| 400 | InvalidAction | %s | 操作无效。 |
| 403 | InvalidOperation.Eni ServiceManaged | %s | 操作无效。 |

##### DescribeNetworkInterfaces

云服务器ECS 调用DescribeNetworkInterfaces查看弹性网卡（ENI）列表。

**接口说明**

方式一：通过 `NextToken` 设置查询凭证（Token），其取值是上一次调用 `DescribeNetworkInterfaces` 返回的 `NextToken` 参数值，再通过 `MaxResults` 设置单页查询的最大条目数。 方式二：通过 `PageSize` 设置单页返回的条目数，再通过 `PageNumber` 设置页码。 以上两种方式只能任选其中之一。当弹性网卡返回的条目数较多时，推荐使用方式一。如果设置了 `NextToken` ，则请求参数 `PageSize` 和 `PageNumber` 将失效，且返回数据中的 `TotalCount` 无效。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeNetworkI nterfaces | 系统规定参数，取值： DescribeNetworkInterfaces。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 所在地域ID。您可以调用DescribeRegions 查看最新的阿里云地域列表。 |
| Tag.N.Key | String | 否 | TestKey | 弹性网卡的标签值。N的取值范围：1~20。 |
| Tag.N.Value | String | 否 | TestValue | 弹性网卡的标签键。N的取值范围：1~20。 |
| ResourceGroupI d | String | 否 | rg- bp67acfmxazb4p **** | 资源组ID。 |
| VSwitchId | String | 否 | vsw- bp16usj2p27htro 3**** | VPC的交换机ID。 |
| VpcId | String | 否 | vpc- wz9wh0fywtu5szs zb**** | 网卡所属的专有网络VPC ID。 |
| PrimaryIpAddre ss | String | 否 | 192.168.*.* | 弹性网卡主私网IP地址。 |
| PrivateIpAddres s.N | RepeatLi st | 否 | 192.168.*.* | 弹性网卡的辅助私网IP地址，N的取值范围： 1~100。 |
| SecurityGroupI d | String | 否 | sg- bp144yr32sx6nd w**** | 安全组ID。 |
| NetworkInterfa ceName | String | 否 | my-eni-name | 弹性网卡的名称。 |

云服务器ECS

| Type | String | 否 | Secondary | 弹性网卡类型。取值范围： Primary：主网卡 Secondary：辅助弹性网卡默认值：空，表示查询所有类型。 |
|---|---|---|---|---|
| InstanceId | String | 否 | i- bp1e2l6djkndyuli **** | 弹性网卡当前关联的实例ID。 |
| NetworkInterfa ceId.N | RepeatLi st | 否 | eni- bp125p95hhdhn3 ot**** | 弹性网卡ID。N的取值范围：1~100。 |
| ServiceManage d | Boolean | 否 | true | 该弹性网卡的使用者是否为云产品或虚商。 |
| Status | String | 否 | InUse | 网卡状态。取值范围： Creating：创建中 Available：未挂载 Attaching：挂载中 InUse：已挂载 Detaching：分离中 Deleting：删除中 CreateFailed：创建失败，属于异常状态默认值：空，表示查询所有状态。 |
| PageNumber | Integer | 否 | 1 | 查询结果的页码。 起始值：1。 默认值：1。 |
| PageSize | Integer | 否 | 100 | 查询结果的分页大小。 最大值：100。 默认值：10。 有关本接口查看返回数据的设置方式，请参见上文接口说明。 |
| NextToken | String | 否 | AAAAAdDWBF2** ** | 查询凭证（Token），取值为上一次API调用返回的 NextToken 参数值。 有关本接口查看返回数据的设置方式，请参见上文接口说明。 |
| MaxResults | Integer | 否 | 50 | 返回的最大数。取值范围：1~500。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云服务器ECS

| NetworkInterfa ceSets | Array |  | 弹性网卡信息组成的集合。 |
|---|---|---|---|
| NetworkInterfa ceSet |  |  |  |
| AssociatedPubli cIp | Struct |  | 弹性网卡辅助私有IP地址关联的公网IP。 |
| AllocationId | String | eip- 2ze88m67qx5z**** | 弹性公网IP的ID。 |
| PublicIpAddress | String | 116.62.*.* | 说明该参数暂未支持。 |
| Attachment | Struct |  | 弹性网卡的绑定状态。 |
| DeviceIndex | Integer | 1 |  |
| InstanceId | String | null |  |
| TrunkNetworkI nterfaceId | String | null |  |
| CreationTime | String | 2017-11- 24T06:14:22Z | 创建时间。 |
| Description | String | DescriptionTest | 描述。 |
| InstanceId | String | i- bp1e2l6djkndyuli*** * | 弹性网卡绑定的实例ID。 说明由其他阿里云服务管理和控制的弹性网卡不会返回实例ID。 |
| Ipv6Sets | Array |  | 为弹性网卡分配的IPv6地址集合。 |
| Ipv6Set |  |  |  |
| Ipv6Address | String | 2408:4321:180:170 1:94c7:bc38:3bfa:** * | 为弹性网卡指定的IPv6地址。 |
| MacAddress | String | 00:16:3e:12:e7:** | 弹性网卡的MAC地址。 |
| NetworkInterfa ceId | String | eni- bp125p95hhdhn3ot* *** | 弹性网卡ID。 |
| NetworkInterfa ceName | String | my-eni-name | 弹性网卡的名称。 |
| OwnerId | String | 123456**** | 弹性网卡的所属账号ID。 |

云服务器ECS

| PrivateIpAddres s | String | 172.17.*.* | 弹性网卡的私网IP地址。 |
|---|---|---|---|
| PrivateIpSets | Array |  | PrivateIpSet组成的集合。 |
| PrivateIpSet |  |  |  |
| AssociatedPubli cIp | Struct |  | 弹性网卡关联的公网IP。 |
| AllocationId | String | eip- 2ze88m67qx5z**** | 弹性公网IP的ID。 |
| PublicIpAddress | String | 116.62.*.* | 说明该参数暂未支持。 |
| Primary | Boolean | true | 是否是主私网IP地址。 |
| PrivateIpAddres s | String | 172.17.*.* | 实例的私网IP地址。 |
| QueueNumber | Integer | 2 | 弹性网卡的队列号。 |
| ResourceGroup Id | String | rg- 2ze88m67qx5z**** | 资源组ID。 |
| SecurityGroupI ds | List | sg- bp18kz60mefsicfg** ** | 所属的安全组集合。 |
| ServiceID | Long | 12345678910 | 弹性网卡对应的虚商ID。 |
| ServiceManage d | Boolean | true | 该弹性网卡的使用者是否为云产品或虚商。 |
| Status | String | Available | 弹性网卡的状态。 |
| Tags | Array |  | 标签。 |
| Tag |  |  |  |
| TagKey | String | TestKey | 标签键。 |
| TagValue | String | TestValue | 标签值。 |
| Type | String | Secondary | 弹性网卡的类型。 |
| VSwitchId | String | vsw- bp16usj2p27htro3** ** | VPC的交换机ID。 |

云服务器ECS

| VpcId | String | vpc- bp1j7w3gc1cexjqd** ** | 网卡所属的专有网络VPC ID。 |
|---|---|---|---|
| ZoneId | String | cn-qingdao-env17- amtest11001-a | 可用区ID。 |
| NextToken | String | AAAAAdDWBF2**** | 本次调用返回的查询凭证值。 |
| PageNumber | Integer | 1 | 返回数据列表页码。 |
| PageSize | Integer | 1 | 查询时设置的每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 70 | 返回的弹性网卡总数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeNetworkInterfaces &RegionId=cn-qingdao-env17-d01 &PrivateIpAddress.1=192.168.*.* &PrivateIpAddress.2=192.168.*.* &NextToken=AAAAAdDWBF2****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <TotalCount>1</TotalCount>
      <RequestId>5C0E2B68-EDB0-421D-B146-E58A04808242</RequestId>
      <PageSize>10</PageSize>
      <NextToken>AAAAAdDWBF2w6Olxc+cMPjUtUMpaCa3hjTbxWpikFyOaihc****/JSvFWO/sGLK3bh****
</NextToken>
      <PageNumber>1</PageNumber>
      <NetworkInterfaceSets>
            <NetworkInterfaceSet>
                  <Status>InUse</Status>
                  <PrivateIpAddress>192.168.*.*</PrivateIpAddress>
                  <ResourceGroupId>rg-aek2boynwys****</ResourceGroupId>
                  <InstanceId>i-wz91t9p4j9xsw2pn****</InstanceId>
                  <VSwitchId>vsw-wz9vqfgwgkj94ubb1****</VSwitchId>
                  <NetworkInterfaceId>eni-wz9iib303as7e5c3****</NetworkInterfaceId>
                  <MacAddress>00:16:3e:*:*:c2</MacAddress>
                  <SecurityGroupIds>
                        <SecurityGroupId>sg-wz9iib303as7e5c7****</SecurityGroupId>
                  </SecurityGroupIds>
                  <Type>Primary</Type>
                  <Ipv6Sets>
                        <Ipv6Set>
                              <Ipv6Address>2408:4321:180:1701:94c7:bc38:3bfa:***</Ipv6Address
```

>

```xml
                        </Ipv6Set>
                  </Ipv6Sets>
                  <VpcId>vpc-wz9wh0fywtu5szszb****</VpcId>
                  <OwnerId>140692647406****</OwnerId>
                  <AssociatedPublicIp></AssociatedPublicIp>
                  <CreationTime>2019-12-25T12:31:31Z</CreationTime>
                  <Tags>
                        <Tag>
                              <TagKey>owner</TagKey>
                              <TagValue>lisi</TagValue>
                        </Tag>
                  </Tags>
                  <PrivateIpSets>
                        <PrivateIpSet>
                              <PrivateIpAddress>192.168.*.*</PrivateIpAddress>
                              <AssociatedPublicIp></AssociatedPublicIp>
                              <Primary>true</Primary>
                        </PrivateIpSet>
                  </PrivateIpSets>
            </NetworkInterfaceSet>
      </NetworkInterfaceSets>
```

`JSON` 格式云服务器ECS

```json
{
 "TotalCount": 1,
 "RequestId": "5C0E2B68-EDB0-421D-B146-E58A04808242",
 "PageSize": 10,
 "NextToken": "AAAAAdDWBF2w6Olxc+cMPjUtUMpaCa3hjTbxWpikFyOaihc****/JSvFWO/sGLK3bh****",
 "PageNumber": 1,
 "NetworkInterfaceSets": {
  "NetworkInterfaceSet": [{
   "Status": "InUse",
   "PrivateIpAddress": "192.168.*.*",
   "ResourceGroupId": "rg-aek2boynwys****",
   "InstanceId": "i-wz91t9p4j9xsw2pn****",
   "VSwitchId": "vsw-wz9vqfgwgkj94ubb1****",
   "NetworkInterfaceId": "eni-wz9iib303as7e5c3****",
   "MacAddress": "00:16:3e:*:*:c2",
   "SecurityGroupIds": {
    "SecurityGroupId": [
     "sg-wz9iib303as7e5c7****"
```

]

```json
   },
   "Type": "Primary",
   "Ipv6Sets": {
    "Ipv6Set": [{
     "Ipv6Address": "2408:4321:180:1701:94c7:bc38:3bfa:***"
    }]
   },
   "VpcId": "vpc-wz9wh0fywtu5szszb****",
   "OwnerId": "140692647406****",
   "AssociatedPublicIp": {},
   "CreationTime": "2019-12-25T12:31:31Z",
   "Tags": {
    "Tag": [{
     "TagKey": "owner",
     "TagValue": "lisi"
    }]
   },
   "PrivateIpSets": {
    "PrivateIpSet": [{
     "PrivateIpAddress": "192.168.*.*",
     "AssociatedPublicIp": {},
     "Primary": true
    }]
   }
  }]
 }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey已经过期。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
|---|---|---|---|
| 403 | Forbidden.NotSuppo rtRAM | %s | 暂不支持 RAM 用户执行该操作。 |
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 403 | Forbidden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 400 | InvalidParameter | %s | 无效的参数。 |
| 400 | InvalidInstanceID.M alformed | %s | 参数“InstanceId”格式错误。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 400 | InvalidOperation.Det achPrimaryEniNotAll owed | %s | 不允许解绑实例的主网卡。 |
| 404 | InvalidEcsId.NotFou nd | %s | 指定的实例 ID 不存在。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡 ID 不存在。 |
| 404 | InvalidVSwitchId.Not Found | %s | 指定的交换机不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |
| 403 | MaxEniCountExceed ed | %s | 已超过可以操作的最大弹性网卡数。 |
| 403 | EniPerInstanceLimit Exceeded | %s | 实例绑定的弹性网卡数量已经达到了最大限度，不能在为实例绑定弹性网卡。 |
| 403 | InvalidOperation.Av ailabilityZoneMisma tch | %s | 该操作无效。 |
| 403 | InvalidOperation.Vp cMismatch | %s | 您的操作无效，请确认该操作中的 VPC 与其它参数是否匹配。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | InvalidSecurityGrou pId.NotVpc | %s | 参数“SecurityGroupId”无效，该安全组的网络类型不是专有网络。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |

云服务器ECS

| 400 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
|---|---|---|---|

##### DetachNetworkInterface

调用DetachNetworkInterface从一台ECS实例上分离一个弹性网卡（ENI）。

**接口描述**

调用该接口时，您需要注意： 不允许分离实例主网卡。 弹性网卡必须处于解绑中（Detaching）或者已绑定（InUse）状态。 实例必须处于运行中（Running）或者已停止（Stopped）状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DetachNetworkIn terface | 系统规定参数，取值： DetachNetworkInterface。 |
| InstanceId | String | 是 | i- bp67acfmxazb4p **** | 实例ID。 |
| NetworkInterfa ceId | String | 是 | eni- bp67acfmxazb4p **** | 弹性网卡ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 资源所属地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DetachNetworkInterface &InstanceId=i-bp67acfmxazb4p**** &NetworkInterfaceId=eni-bp67acfmxazb4p**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

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
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey已经过期。 |
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 403 | Forbidden.NotSuppo rtRAM | %s | 暂不支持 RAM 用户执行该操作。 |
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 403 | Forbidden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 400 | InvalidParameter | %s | 无效的参数。 |
| 400 | InvalidInstanceID.M alformed | %s | 参数“InstanceId”格式错误。 |
| 400 | InvalidOperation.Inv alidRegion | %s | 指定的参数“RegionId”无效。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 400 | InvalidOperation.Det achPrimaryEniNotAll owed | %s | 不允许解绑实例的主网卡。 |
| 404 | InvalidEcsId.NotFou nd | %s | 指定的实例 ID 不存在。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡 ID 不存在。 |
| 404 | InvalidVSwitchId.Not Found | %s | 指定的交换机不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |

云服务器ECS

| 403 | MaxEniCountExceed ed | %s | 已超过可以操作的最大弹性网卡数。 |
|---|---|---|---|
| 403 | EniPerInstanceLimit Exceeded | %s | 实例绑定的弹性网卡数量已经达到了最大限度，不能在为实例绑定弹性网卡。 |
| 403 | InvalidOperation.Av ailabilityZoneMisma tch | %s | 该操作无效。 |
| 403 | InvalidOperation.Vp cMismatch | %s | 您的操作无效，请确认该操作中的 VPC 与其它参数是否匹配。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | InvalidSecurityGrou pId.NotVpc | %s | 参数“SecurityGroupId”无效，该安全组的网络类型不是专有网络。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 400 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
| 400 | InvalidParams.EniId | %s | 指定的参数“EniId”无效。 |
| 403 | InvalidOperation.Eni ServiceManaged | %s | 操作无效。 |
| 403 | InvalidOperation.Eni Linked | %s | 由于实例绑定了弹性网卡导致此操作无效 |
| 403 | InvalidInstanceId.No tFound | %s | 指定的实例不存在，请确认参数“InstanceId”是否正确。 |

##### DeleteNetworkInterface

**接口描述**

弹性网卡必须处于可用（Available）状态。 如果弹性网卡已经附加到ECS实例，必须先从实例分离（DetachNetworkInterface），才能删除弹性网卡。 删除弹性网卡之后： 弹性网卡的主私有IP地址（PrimaryIpAddress）自动释放。 被删除的弹性网卡退出所属的所有安全组。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DeleteNetworkInt erface | 系统规定参数，取值： DeleteNetworkInterface。 |
| NetworkInterfa ceId | String | 是 | eni- bp14v2sdd3v8htl nm*** | 弹性网卡的ID。 |

云服务器ECS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 所在地域ID。您可以调用DescribeRegions 查看最新的阿里云地域列表。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | F3CD6886-D8D0- 4FEE-B93E- 1B73239673DE | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DeleteNetworkInterface &NetworkInterfaceId=eni-bp14v2sdd3v8htlnm*** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>04F0F334-1335-436C-A1D7-6C044FExxxxx</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FExxxxx"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey已经过期。 |
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 403 | Forbidden.NotSuppo rtRAM | %s | 暂不支持 RAM 用户执行该操作。 |
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 403 | Forbidden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 400 | InvalidParameter | %s | 无效的参数。 |

云服务器ECS

| 400 | InvalidInstanceID.M alformed | %s | 参数“InstanceId”格式错误。 |
|---|---|---|---|
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 400 | InvalidOperation.Det achPrimaryEniNotAll owed | %s | 不允许解绑实例的主网卡。 |
| 404 | InvalidEcsId.NotFou nd | %s | 指定的实例 ID 不存在。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡 ID 不存在。 |
| 404 | InvalidVSwitchId.Not Found | %s | 指定的交换机不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组 ID 不存在。 |
| 403 | MaxEniCountExceed ed | %s | 已超过可以操作的最大弹性网卡数。 |
| 403 | EniPerInstanceLimit Exceeded | %s | 实例绑定的弹性网卡数量已经达到了最大限度，不能在为实例绑定弹性网卡。 |
| 403 | InvalidOperation.Av ailabilityZoneMisma tch | %s | 该操作无效。 |
| 403 | InvalidOperation.Vp cMismatch | %s | 您的操作无效，请确认该操作中的 VPC 与其它参数是否匹配。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | InvalidSecurityGrou pId.NotVpc | %s | 参数“SecurityGroupId”无效，该安全组的网络类型不是专有网络。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 400 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
| 400 | InvalidParams.EniId | %s | 指定的参数“EniId”无效。 |
| 403 | InvalidOperation.Eni ServiceManaged | %s | 操作无效。 |

##### ModifyNetworkInterfaceAttribute

调用ModifyNetworkInterfaceAttribute修改一个弹性网卡（ENI）的名称、描述以及所属安全组等。

**请求参数**

云服务器ECS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyNetworkInt erfaceAttribute | 系统规定参数，取值： ModifyNetworkInterfaceAttribute。 |
| NetworkInterfaceI d | String | 是 | eni- bp67acfmxazb4p h*** | 弹性网卡ID。 您可以调用DescribeNetworkInterfaces查询弹性网卡ID。 |
| RegionId | String | 是 | cn-qingdao-****- d01 | 弹性网卡所在地域ID。 您可以调用DescribeRegions查询地域ID。 |
| SecurityGroupId. N | RepeatLi st | 否 | sg- bp67acfmxazb4p h*** | SecurityGroupId，弹性网卡会移出已有的安全组，并加入该参数指定的安全组。N的取值范围为1~5。 |
| NetworkInterface Name | String | 否 | my-eni-name | 弹性网卡的名称。长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以http://和https://开头。可以包含数字、半角冒号（:）、下划线（ ）或者连字符 _ （-）。 默认值：空。 |
| Description | String | 否 | test | 弹性网卡的描述信息。 长度为2~256个英文或中文字符，不能以http://和https://开头。 默认值：空。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=ModifyNetworkInterfaceAttribute &NetworkInterfaceId=eni-bp67acfmxazb4ph*** &RegionId=cn-qingdao-****-d01 &SecurityGroupId.1=sg-bp67acfmxazb4ph*** &NetworkInterfaceName=my-eni-name &Description=test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
        <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
```

`JSON` 格式

```json
{
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey已经过期。 |
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 403 | Forbidden.NotSuppo rtRAM | %s | 暂不支持RAM用户执行该操作。 |
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 403 | Forbidden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 400 | InvalidParameter | %s | 无效的参数。 |
| 400 | InvalidInstanceID.M alformed | %s | 参数InstanceId格式错误。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 400 | InvalidOperation.Det achPrimaryEniNotAll owed | %s | 不允许解绑实例的主网卡。 |
| 400 | InvalidParams.EniId | %s | 指定的参数EniId无效。 |
| 404 | InvalidEcsId.NotFou nd | %s | 指定的实例ID不存在。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡ID不存在。 |
| 404 | InvalidVSwitchId.Not Found | %s | 指定的交换机不存在。 |
| 404 | InvalidSecurityGrou pId.NotFound | %s | 指定的安全组ID不存在。 |

云服务器ECS

| 403 | MaxEniCountExceed ed | %s | 已超过可以操作的最大弹性网卡数。 |
|---|---|---|---|
| 403 | EniPerInstanceLimit Exceeded | %s | 实例绑定的弹性网卡数量已经达到了最大限度，不能在为实例绑定弹性网卡。 |
| 403 | InvalidOperation.Av ailabilityZoneMisma tch | %s | 该操作无效。 |
| 403 | InvalidOperation.Vp cMismatch | %s | 您的操作无效，请确认该操作中的 VPC与其它参数是否匹配。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 403 | InvalidSecurityGrou pId.NotVpc | %s | 参数SecurityGroupId无效，该安全组的网络类型不是专有网络。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 400 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
| 403 | InvalidOperation.Eni ServiceManaged | %s | 操作无效。 |
| 403 | InvalidOperation.Re sourceManagedByCl oudProduct | %s | 云产品托管的安全组不支持修改操作。 |

##### AssignIpv6Addresses

**接口说明**

您可以指定弹性网卡所属交换机下CIDR的IPv6地址，也可以指定IPv6地址数量自动创建IPv6地址。

|  | InUse |
|---|---|
| Running |  |

单个网卡能够分配的IPv6地址数量和网卡附加的实例规格有关。 如果弹性网卡处于**可用**（ `Available` ）状态，最多可以分配10个IPv6地址。 如果弹性网卡挂载到实例上，能够分配的IPv6地址数将受到实例规格限制。 成功调用该接口后，您可以从返回结果中获取已分配的IPv6地址信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssignIpv6Addres ses | 系统规定参数，取值： AssignIpv6Addresses。 |
| RegionId | String | 是 | cn-qingdao-**** | 弹性网卡所在地域的ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| NetworkInterfaceI d | String | 是 | eni- bp14v2sdd3v8ht* ***** | 弹性网卡ID。 |
|---|---|---|---|---|
| Ipv6Address.N | RepeatLi st | 否 | 2001:db8:1234:1 a00::**** | 为弹性网卡指定一个或多个IPv6地址。支持设置最多10个IPv6地址，即N的取值范围： 1~10。 取值示例： Ipv6Address.1=2001:db8:1234:1a00:: XXX 说明调用该接口时，您必须设置 Ipv6Addresses.N 参数或者 Ipv6AddressCount 参数的其中一个，但不能同时设置这两个参数。 |
| Ipv6AddressCoun t | Integer | 否 | 1 | 为弹性网卡指定随机生成的IPv6地址数量。 取值范围：1~10。 说明调用该接口时，您必须设置 Ipv6Addresses.N 参数或者 Ipv6AddressCount 参数的其中一个，但不能同时设置这两个参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Ipv6Sets | List | 2001:db8:1234:1a0 0::**** | 弹性网卡已分配的IPv6地址。 |
| NetworkInterfa ceId | String | eni- bp1iqejowblx6h8j*** * | 弹性网卡ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=AssignIpv6Addresses &RegionId=cn-qingdao-**** &NetworkInterfaceId=eni-bp14v2sdd3v8ht****** &Ipv6Address.1=2001:db8:1234:1a00::***
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <Ipv6Sets>2001:db8:1234:1a00::****</Ipv6Sets>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
      <NetworkInterfaceId>eni-bp1iqejowblx6h8j****</NetworkInterfaceId>
```

`JSON` 格式

```json
{
    "Ipv6Sets": "2001:db8:1234:1a00::****",
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
    "NetworkInterfaceId": "eni-bp1iqejowblx6h8j****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 400 | InvalidParameter | %s | 无效的参数。 |
| 400 | InvalidInstanceID.M alformed | %s | 参数 InstanceId 格式错误。 |
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 400 | InvalidParams.EniId | %s | 指定的参数 EniId 无效。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 400 | InvalidPrivateIpAddr ess.Duplicated | Specified private IP address is duplicated. | 指定的私网 IP 已经被使用，请您更换 IP 再重试。 |
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey 已经过期。 |
| 403 | Forbedden.NotSupp ortRAM | %s | 暂不支持RAM用户执行该操作。 |
| 403 | Forbbiden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 403 | MaxEniIpv6IpsCount Exceeded | %s | 该弹性网卡挂载的 IPv6 个数达到上限。 |
| 403 | InvalidIp.IpUnassign ed | %s | 指定的 IP 未被分配。 |

云服务器ECS

| 403 | InvalidIp.IpRepeated | %s | 指定的 IP 重复。 |
|---|---|---|---|
| 403 | InvalidIp.IpAssigned | %s | 指定的 IP 已被分配。 |
| 403 | InvalidIp.Address | %s | 指定的 IPv6 地址无效。 |
| 403 | InvalidOperation.Ipv 4CountExceeded | %s | IPv4 数量达到上限，导致该操作无效。 |
| 403 | InvalidOperation.Ipv 6CountExceeded | %s | IPv6 数量达到上限，导致该操作无效。 |
| 403 | InvalidOperation.Ipv 6NotSupport | %s | IPv6不支持当前操作。 |
| 403 | InvalidVSwitch.Ipv6 NotTurnOn | %s | 您当前使用的交换机没有开启 IPv6 功能，请先开启此功能后重试。 |
| 403 | InvalidVSwitchId.IpI nvalid | %s | 指定的私网 IP 无效。 |
| 403 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
| 403 | InvalidOperation.Eni ServiceManaged | %s | 操作无效。 |
| 403 | SecurityGroupInstan ceLimitExceed | %s | 该安全组内已有的实例数量已达到最大限制。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡 ID 不存在。 |

##### UnassignIpv6Addresses

若弹性网卡已被分配了IPv6地址，调用UnassignIpv6Addresses可以回收一个或多个IPv6地址。

**接口说明**

调用该接口时，您需要注意： 弹性网卡必须处于**可用**（Available）或**已挂载**（InUse）状态。 主网卡关联的ECS实例必须处于**运行中**（Running）或**已停止**（Stopped）状态。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | UnassignIpv6Add resses | 系统规定参数。取值： UnassignIpv6Addresses。 |
| Ipv6Address.N | RepeatLi st | 是 | 2001:db8:1234:1 a00::*** | 为弹性网卡指定一个或多个IPv6地址。N的取值范围仅支持1。 取值示例： Ipv6Address.1=2001:db8:1234:1a00::* 。 |
| NetworkInterfa ceId | String | 是 | eni- bp14v2sdd3v8ht* ***** | 弹性网卡ID。 |

云服务器ECS

| RegionId | String | 是 | cn-qingdao- env17-d01 | 弹性网卡所在地域的ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=UnassignIpv6Addresses &Ipv6Address.1=2001:db8:1234:1a00::*** &NetworkInterfaceId=eni-bp14v2sdd3v8ht****** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>48285314-3192-47FE-B4C8-9D51E7Fxxxxx</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "48285314-3192-47FE-B4C8-9D51E7Fxxxxx"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidUserType.Not Supported | %s | 您当前的账号不支持此操作。 |
| 403 | Abs.InvalidAccount. NotFound | %s | 您的阿里云账号不存在，或者您的 AccessKey已经过期。 |
| 403 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 403 | Forbedden.NotSupp ortRAM | %s | 暂不支持 RAM 用户执行该操作。 |
| 400 | UnsupportedParame ter | %s | 不支持参数。 |
| 403 | Forbbiden.SubUser | %s | 您的账号没有操作此资源的权限，请向主账号申请相关的权限。 |

云服务器ECS

| 400 | InvalidParameter | %s | 无效的参数。 |
|---|---|---|---|
| 400 | InvalidInstanceID.M alformed | %s | 参数“InstanceId”格式错误。 |
| 400 | InvalidOperation.Inv alidEcsState | %s | 实例当前的状态不支持此操作。 |
| 400 | InvalidOperation.Inv alidEniState | %s | 弹性网卡当前的状态不支持此操作。 |
| 404 | InvalidEniId.NotFoun d | %s | 指定的弹性网卡 ID 不存在。 |
| 403 | InvalidOperation.Inv alidEniType | %s | 当前弹性网卡的类型不支持此操作。 |
| 403 | InvalidIp.IpUnassign ed | %s | 指定的 IP 未被分配。 |
| 403 | InvalidIp.IpRepeated | %s | 指定的 IP 重复。 |
| 403 | InvalidIp.Address | %s | 指定的 IPv6 地址无效。 |
| 403 | Forbidden.RegionId | %s | 当前地域暂时没有提供该服务。 |
| 403 | InvalidOperation.Eni ServiceManaged | %s | 操作无效。 |

#### 前缀列表

##### CreatePrefixList

创建前缀列表。

**接口说明**

前缀列表是一些网络前缀（即 CIDR 地址块）的集合，您可以在配置其他资源的网络规则时引用前缀列表。 创建前缀列表时： 您必须为该前缀列表指定地址族（IPv4或 IPv6），同一前缀列表中的条目只能属于同一地址族，且地址族创建后不能修改。 您必须为该前缀列表设置最大条目容量，且创建后不能修改。 您可以为该前缀列表指定一些条目，条目由 CIDR 地址块和描述构成，条目数量不能超过您设置的最大条目容量。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | CreatePrefixList | 系统规定参数。取值： CreatePrefixList |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 地域 ID。您可以调用 DescribeRegions查询地域 ID。 |  |  |  |
| Tag | Repea tList | Query | 否 | / | 标签列表。 |  |  |  |
| -Key | String |  | 否 | TestKey | 前缀列表的标签键。N 的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 128 个字符，不能以 aliyun和acs:开头，不能包含 http:// 或者 https:// 。 |  |  |  |
| -Value | String |  | 否 | TestValue | 前缀列表的标签值。N 的取值范围：1~20。该值可以为空字符串。 最多支持 128 个字符，不能包含 http:// 或 https:// 。 |  |  |  |
| MaxEntries | Intege r | Query | 是 | 10 | 前缀列表支持的最大条目容量。取值范围：1~200。 |  |  |  |
| AddressFa mily | String | Query | 是 | IPv4 | 前缀列表的地址族。取值范围： IPv4。 IPv6。 |  |  |  |
| ClientToke n | String | Query | 否 | 123e4567-e89b-12d3- a456-42665544**** | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken 只支持 ASCII字符，且不能超过64个字符。 |  |  |  |
| PrefixListN ame | String | Query | 是 | PrefixListNameSample | 前缀列表的名称。长度为 2~128个字符，必须以大小字母或中文开头，不能以 http:// 、 https:/ / 、 com.aliyun 和 c om.alibabacloud 开头。 可以包含中文、英文、数字、 半角冒号（:）、下划线 （ ）、半角句号（.）或者短 _ 划线（-）。 |  |  |  |
|  |  |  |  |  |  | https:/ |  |  |
|  |  |  |  |  |  |  | c |  |

|  | http:// |
|---|---|
| https:// |  |

|  |  |  | http:// |  |  |
|---|---|---|---|---|---|
| ple |  | / |  |  |  |
|  |  |  |  | 、 |  |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| Descriptio n | String | Query | 否 | This is description. | 前缀列表的描述信息。长度为 2~256 个英文或中文字符， 不能以 http:// 和 https:/ / 开头。 |  |  |
|  |  |  |  |  |  | https:/ |  |
| Entry | Repea tList | Query | 否 | / | 前缀列表条目信息。 |  |  |
| - Descriptio n | String |  | 否 | Description Sample 01 | 安全组规则描述。 |  |  |
| -Cidr | String |  | 是 | 192.168.1.0/24 | 前缀列表条目的CIDR地址块信息。N的取值范围： 0~200。注意事项： 前缀列表的条目数量不能大于最大条目容量 （ MaxEntries ）。 条目中的CIDR地址块类型根据地址族决定，一个前缀列表不能同时包含IPv4 和IPv6的CIDR地址块。 多个条目中的CIDR地址块不能重复。例如，您不能设置两个 192.168.1.0/24。 支持设置单IP地址，系统会自动转换为CIDR地址块。 例如，您设置 192.168.1.100，系统会自动转换成 192.168.1.100/32。 如果使用IPv6 CIDR地址块，系统会自动转换成零压缩表示形式且字母转换为小写。例如，您设置 2001:0DB8:0000:0000: 0000:0000:0000:0000/ 32，系统会自动转换成 2001:db8::/32。 默认值：空。 |  |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PrefixListId | String | pl- x1j1k5ykzqlixdcy*** * | 前缀列表ID。 |
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

云服务器ECS 请求示例

```
http(s)://ecs.example.com/?Action=CreatePrefixList &RegionId=cn-qingdao-env17-**** &MaxEntries=10 &AddressFamily=IPv4 &PrefixListName=PrefixListNameSample
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****",
 "PrefixListId":"pl-x1j1k5ykzqlixdcy****"
}
```

`XML` 格式

```xml
<RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7*****</RequestId> <PrefixListId>pl-x1j1k5ykzqlixdcy****</PrefixListId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.MissingParamet er | MissingParameter | %s |
| 400 | InvalidParameter.Ad dressFamily | InvalidParameter.AddressFamily | The parameter AddressFamily should be IPv4 or IPv6. |
| 400 | PARAMETER ILLEGA _ L | InvalidParameter | %s |
| 400 | InvalidParameter.Pr efixListName | InvalidParameter.PrefixListName | The parameter PrefixListName is not valid. |
| 400 | Abs.InvalidDescripti on.Malformed | InvalidDescription.Malformed | The specified Description is wrongly formed. |
| 400 | Abs.InvalidClientTok en.Malformed | InvalidClientToken.ValueNotSup ported | The ClientToken provided is invalid. |
| 400 | CIDR INVALID FOR _ _ MAT | InvalidParameter.CidrMalformed | %s |
| 400 | CIDR DUPLICATED _ _ WITH | InvalidParameter.CidrDuplicated | %s |
| 400 | LimitExceed.Entry | LimitExceed.Entry | The number of entries added or removed exceeds the limit. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | LimitExceed.MaxEnt ries | LimitExceed.MaxEntries | The number of entries exceeds the MaxEntries of the specified prefix list. |
| 400 | CIDR DUPLICATED _ | InvalidParameter.CidrDuplicated | %s |
| 400 | CIDR DUPLICATED _ _ WITH | InvalidParameter.CidrDuplicated | %s |
| 404 | PREFIX LIST PER RE _ _ _ GION LIMIT EXCEED _ _ | LimitExceed.PrefixListPerRegion | The number of prefix lists in the region exceeds the limit. |
| 404 | REGION NOT EXIST _ _ S | InvalidRegionId.NotFound | The specified RegionId does not exist. |

##### DescribePrefixLists

查询一个或多个前缀列表的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| Action | String | Query | 是 | DescribePrefixLists | 系统规定参数。取值： DescribePrefixLists |  |  |
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 地域ID。您可以调用 DescribeRegions查询地域 ID。 |  |  |
| Tag | Repea tList | Query | 否 | / | 标签列表。 |  |  |
| -Key | String |  | 否 | TestKey | 前缀列表的标签键。N 的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 128 个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |  |  |
| -Value | String |  | 否 | TestKey | 前缀列表的标签值。N 的取值范围：1~20。该值可以为空字符串。 最多支持 128 个字符，不能包含 http:// 或 https:/ / 。 |  |  |
|  |  |  |  |  |  | https:/ |  |

|  | / |  |
|---|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|
| PrefixListN ame | String | Query | 否 | PrefixListNameSample | 前缀列表的名称。长度为 2~128个字符，必须以大小字母或中文开头，不能以 http:// 、 https:/ / 、 com.aliyun 和 c om.alibabacloud 开头。 可以包含中文、英文、数字、 半角冒号（:）、下划线 （ ）、半角句号（.）或者短 _ 划线（-）。 |  |  |  |
|  |  |  |  |  |  | https:/ |  |  |
|  |  |  |  |  |  |  | c |  |
| NextToken | String | Query | 否 | AAAAAdDWBF2**** | 查询凭证（Token）。取值为上一次调用该接口返回的 NextToken 参数值， 初次调用接口时无需设置该参数。 |  |  |  |
| MaxResult s | Intege r | Query | 否 | 10 | 分页查询时每页行数。取值范围：1~500。 默认值：50。 |  |  |  |
| AddressFa mily | String | Query | 否 | IPv4 | 前缀列表的地址族。取值范围： IPv4。 IPv6。 |  |  |  |
| PrefixListId | Repea tList | Query | 否 | pl-x1j1k5ykzqlixdcy**** | 前缀列表ID。 |  |  |  |

|  |  |  | http:// |  |  |
|---|---|---|---|---|---|
| ple |  | / |  |  |  |
|  |  |  |  | 、 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PrefixLists | Array | / | 前缀列表信息组成的数组。 |
| -Tags | Array | / | 标签列表。 |
| --TagValue | String | TestKey | 前缀列表的标签键。N 的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 128 个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| --TagKey | String | TestValue | 前缀列表的标签值。N 的取值范围：1~20。该值可以为空字符串。 最多支持 128 个字符，不能包含 http:// 或 https:// 。 |
| -CreationTime | String | 2022-04- 10T06:15:54Z | 实例创建时间。 |

|  | aliyun |  |
|---|---|---|
| http:// |  |  |

| 开发指南·API参考 |  |  | 云服务器EC |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - AssociationCou nt | Integer | 1 | 关联资源的数量。 |
| -MaxEntries | Integer | 10 | 前缀列表支持的最大条目容量。 |
| -Description | String | This is description. | 描述信息。 |
| -AddressFamily | String | IPv4 | 前缀列表的地址族。可能值： IPv4。 IPv6。 |
| -PrefixListName | String | PrefixListNameSam ple | 前缀列表的名称。 |
| -PrefixListId | String | pl- x1j1k5ykzqlixdcy*** * | 前缀列表ID。 |
| NextToken | String | e71d8a535bd9cc11 | 本次调用返回的查询凭证（Token）。具体使用方式请参见接口说明。 |
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribePrefixLists &RegionId=cn-qingdao-env17-****
```

&公共请求参数正常返回示例 `JSON` 格式云服务器ECS

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "NextToken":"e71d8a535bd9cc11",
 "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****",
 "PrefixLists":[
  {
   "MaxEntries":10,
```

`"Description":"`买满1年，立享官网价格`8.5`折优惠。`",`

```json
   "AssociationCount":1,
   "PrefixListId":"pl-x1j1k5ykzqlixdcy****",
   "PrefixListName":"PrefixListNameSample",
   "CreationTime":"2022-04-10T06:15:54Z",
   "AddressFamily":"IPv4"
  }
```

]

```
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | PARAMETER ILLEGA _ L | InvalidParameter | %s |
| 400 | LimitExceed.PrefixLi stId | LimitExceed.PrefixListId | The specified number of PrefixListId exceeds the limit. |
| 404 | REGION NOT EXIST _ _ S | InvalidRegionId.NotFound | The specified RegionId does not exist. |

##### ModifyPrefixList

修改指定前缀列表的名称、描述等，支持增加、修改和删除条目。

**接口说明**

指定的CIDR地址块应当为标准形式。例如，10.0.0.0/8 是正确形式的 CIDR 地址块，而 10.0.0.1/8 是错误形式。 新增或删除条目时，不能指定重复的CIDR 地址块。例如： 对于IPv4 CIDR 地址块：不能同时指定两个 CIDR 地址块均为 10.0.0.0/8 的条目；不能同时指定两个 CIDR 地址块分别为 10.0.0.1/32 和 10.0.0.1 的条目，这两个地址块重复。 对于IPv6 CIDR 地址块：不能同时指定两个条目的 CIDR 地址块分别为 2001:fd01:0:0:0:0:0:0/32 和 2001:fd01::/32，这两个地址块重复。 新增条目的 CIDR 地址块不能与删除条目的 CIDR 地址块重复。例如，在您新增 CIDR 地址块为 10.0.0.0/8 的条目时，不能在待删除的条目中包含 CIDR 地址块 10.0.0.0/8。 若您需要修改条目的描述，需要指定条目的 CIDR 地址块（AddEntry.N.Cidr）和新的描述信息 （AddEntry.N.Description）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Action | String | Query | 是 | ModifyPrefixList | 系统规定参数。取值： ModifyPrefixList |  |  |  |
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 您可以调用 DescribeRegions查询地域 ID。 |  |  |  |
| PrefixListId | String | Query | 是 | pl-x1j1k5ykzqlixdcy**** | 前缀列表ID。 |  |  |  |
| PrefixListN ame | String | Query | 否 | PrefixListNameSample | 前缀列表的名称。长度为 2~128个字符，必须以大小字母或中文开头，不能以 http:// 、 https:/ / 、 com.aliyun 和 c om.alibabacloud 开头。 可以包含中文、英文、数字、 半角冒号（:）、下划线 （ ）、半角句号（.）或者短 _ 划线（-）。 |  |  |  |
|  |  |  |  |  |  | https:/ |  |  |
|  |  |  |  |  |  |  | c |  |
| Descriptio n | String | Query | 否 | This is description. | 前缀列表的描述信息。长度为 2~256 个英文或中文字符， 不能以 http:// 和 https:/ / 开头。 |  |  |  |
| AddEntry | Repea tList | Query | 否 | / | 添加的前缀列表信息。 |  |  |  |
| - Descriptio n | String |  | 否 | Description Sample 01 | 前缀列表的描述信息。长度为 2~256 个英文或中文字符， 不能以 http:// 和 https:/ / 开头。 |  |  |  |
| -Cidr | String |  | 是 | 192.168.1.0/24 | 添加的前缀列表条目的 CIDR 地址块信息。 添加时请您注意： 前缀列表的条目数量，不能大于前缀列表支持的最大条目容量。您可以调 DescribePrefixListAttrib utes 查询指定前缀列表的最大条目容量信息。 不允许设置重复的 CIDR 地址块信息。 不允许与 RemoveEntry.N.Cidr参数值重复。 |  |  |  |

|  |  |  | http:// |  |  |
|---|---|---|---|---|---|
| ple |  | / |  |  |  |
|  |  |  |  | 、 |  |

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

|  |  | http:// |
|---|---|---|
|  | / |  |

| https:/ |  |
|---|---|

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RemoveEn try | Repea tList | Query | 否 | / | 删除的前缀列表信息。 |
| -Cidr | String |  | 是 | 192.168.1.0/24 | 删除的前缀列表条目的 CIDR 地址块信息。 删除时请您注意： 不允许设置重复的CIDR 地址块信息。 不允许与 AddEntry.N.Cidr参数值重复。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=ModifyPrefixList &RegionId=cn-qingdao-env17-**** &PrefixListId=pl-x1j1k5ykzqlixdcy****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.MissingParamet er | MissingParameter | %s |
| 400 | InvalidParameter.Pr efixListName | InvalidParameter.PrefixListName | The parameter PrefixListName is not valid. |
| 400 | Abs.InvalidDescripti on.Malformed | InvalidDescription.Malformed | The specified Description is wrongly formed. |

| 开发指南·API参 | 考 |  | 云服务器EC |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter.Ci drDuplicated | InvalidParameter.CidrDuplicated | %s |
| 400 | CIDR DUPLICATED _ | InvalidParameter.CidrDuplicated | %s |
| 400 | CIDR DUPLICATED _ _ WITH | InvalidParameter.CidrDuplicated | %s |
| 400 | CIDR INVALID FOR _ _ MAT | InvalidParameter.CidrMalformed | %s |
| 400 | -2021010114 | LimitExceed.MaxEntries | The number of entries exceeds the MaxEntries of the specified prefix list. |
| 400 | LimitExceed.Entry | LimitExceed.Entry | The number of entries added or removed exceeds the limit. |
| 400 | LimitExceed.MaxEnt ries | LimitExceed.MaxEntries | The number of entries exceeds the MaxEntries of the specified prefix list. |
| 404 | PREFIX LIST NOT F _ _ _ OUND | InvalidPrefixListId.NotFound | The specified prefix list was not found. |
| 404 | -2021010112 | InvalidPrefixListId.NotFound | The specified prefix list was not found. |
| 404 | REGION NOT EXIST _ _ S | InvalidRegionId.NotFound | The specified RegionId does not exist. |

##### DescribePrefixListAttributes

查询指定前缀列表的详细信息，包含前缀列表的名称、地址族、最大条目容量以及条目的详细信息等。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DescribePrefixListAttribut es | 系统规定参数。取值： DescribePrefixListAttribut es |
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 地域ID。您可以调用 DescribeRegions查询地域 ID。 |
| PrefixListId | String | Query | 是 | pl-x1j1k5ykzqlixdcy**** | 前缀列表ID。 |

**返回数据**

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Entries | Array | / | 前缀列表中的条目信息组成的数组。 |
| -Description | String | Description Sample 01 | 前缀列表条目的描述信息。 |
| -Cidr | String | 10.0.0.0/8 | 前缀列表条目的CIDR地址块信息。 |
| CreationTime | String | 2022-04- 10T06:15:54Z | 前缀列表的创建时间。 |
| MaxEntries | Integer | 10 | 前缀列表支持的最大条目容量。 |
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |
| Description | String | This is description. | 前缀列表的描述信息。 |
| AddressFamily | String | IPv4 | 前缀列表的地址族。可能值： IPv4。 IPv6。 |
| PrefixListName | String | PrefixListNameSam ple | 前缀列表的名称。 |
| PrefixListId | String | pl- x1j1k5ykzqlixdcy*** * | 前缀列表ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribePrefixListAttributes &RegionId=cn-qingdao-env17-**** &PrefixListId=pl-x1j1k5ykzqlixdcy****
```

&公共请求参数正常返回示例 `JSON` 格式云服务器ECS

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "MaxEntries":10,
 "Description":"This is description.",
 "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****",
 "PrefixListId":"pl-x1j1k5ykzqlixdcy****",
 "PrefixListName":"PrefixListNameSample",
 "CreationTime":"2022-04-10T06:15:54Z",
 "Entries":[
  {
   "Description":"Description Sample 01",
   "Cidr":"10.0.0.0/8"
  }
```

`],`

```json
 "AddressFamily":"IPv4"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | PREFIX LIST NOT F _ _ _ OUND | InvalidPrefixListId.NotFound | The specified prefix list was not found. |
| 404 | -2021010112 | InvalidPrefixListId.NotFound | The specified prefix list was not found. |
| 404 | REGION NOT EXIST _ _ S | InvalidRegionId.NotFound | The specified RegionId does not exist. |

##### DescribePrefixListAssociations

查询指定前缀列表已关联的资源信息，例如，资源ID和资源类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DescribePrefixListAssociat ions | 系统规定参数。取值： DescribePrefixListAssociat ions |
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 地域ID。您可以调用 DescribeRegions查询地域 ID。 |
| PrefixListId | String | Query | 是 | pl-x1j1k5ykzqlixdcy**** | 前缀列表ID。 |

| 云服务器ECS |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NextToken | String | Query | 否 | AAAAAdDWBF2**** | 查询凭证（Token）。取值为上一次调用该接口返回的 NextToken 参数值， 初次调用接口时无需设置该参数。 |
| MaxResult s | Intege r | Query | 否 | 10 | 分页查询时每页行数。取值范围：1~500。 默认值：50。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PrefixListAssoci ations | Array | / | 前缀列表已关联的资源信息组成的数组。 |
| -ResourceId | String | sg- bp11ujym6xsff6l0** ** | 资源 ID。 |
| -ResourceType | String | securitygroup | 资源类型。 |
| NextToken | String | e71d8a535bd9cc11 | 本次调用返回的查询凭证（Token）。具体使用方式请参见接口说明。 |
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribePrefixListAssociations &RegionId=cn-qingdao-env17-**** &PrefixListId=pl-x1j1k5ykzqlixdcy****
```

&公共请求参数正常返回示例 `JSON` 格式云服务器ECS

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "NextToken":"e71d8a535bd9cc11",
 "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****",
 "PrefixListAssociations":[
  {
   "ResourceId":"i-uf6i0tv2refv8wz*****",
   "ResourceType":"securitygroup"
  }
```

]

```
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | PARAMETER ILLEGA _ L | InvalidParameter | %s |
| 400 | RESOURCE TYPE N _ _ OT SUPPORT _ | NotSupported.ResourceType | The specified resource type is not supported. |
| 404 | PREFIX LIST NOT F _ _ _ OUND | InvalidPrefixListId.NotFound | The specified prefix list was not found. |
| 404 | REGION NOT EXIST _ _ S | InvalidRegionId.NotFound | The specified RegionId does not exist. |

##### DeletePrefixList

删除指定的前缀列表，同时删除前缀列表中的所有条目。

**接口说明**

前缀列表与其他资源存在关联时，不能直接删除，需要先在其他资源中解除对该前缀列表的关联，再执行删除操作。您可以调用 DescribePrefixListAssociations 查询指定前缀列表的已关联资源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DeletePrefixList | 系统规定参数。取值： DeletePrefixList |
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 地域ID。您可以调用 DescribeRegions查询地域 ID。 |
| PrefixListId | String | Query | 是 | pl-x1j1k5ykzqlixdcy**** | 前缀列表ID。 |

云服务器ECS

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7***** | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-**** &PrefixListId=pl-x1j1k5ykzqlixdcy****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7*****"
}
```

`XML` 格式

```xml
<RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7*****</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ASSOCIATED RESO _ URCES EXIST _ | NotAllowed.AssociationExist | The specified prefix list has associated resources. |
| 404 | PREFIX LIST NOT F _ _ _ OUND | InvalidPrefixListId.NotFound | The specified prefix list was not found. |
| 404 | -2021010112 | InvalidPrefixListId.NotFound | The specified prefix list was not found. |
| 404 | REGION NOT EXIST _ _ S | InvalidRegionId.NotFound | The specified RegionId does not exist. |

#### 系统事件

##### DescribeInstanceHistoryEvents

调用DescribeInstanceHistoryEvents查询指定实例的系统事件信息，默认查询已完结（系统事件状态为 Executed、Avoided、Canceled、Failed）的历史系统事件。通过指定InstanceEventCycleStatus参数，可以查询任意状态的系统事件。 云服务器ECS

**接口说明**

您最多可以查询最近30天的已完结历史系统事件。对于未完结的系统事件无查询时间限制。 通过指定 `InstanceEventCycleStatus` 参数，还可以查询处于Scheduled（等待执行事件）、 Executing（事件执行中）和Inquiring（事件问询中）状态的系统事件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInstance HistoryEvents | 系统规定参数。取值： DescribeInstanceHistoryEvents。 |
| RegionId | String | 是 | cn-qingdao-***** | 实例所在地域ID。您可以调用 DescribeRegions查询地域ID。 |
| InstanceId | String | 否 | i- uf678mass4zvr9n 1**** | 实例ID。不指定实例ID时，表示查询您指定地域下所有实例的系统事件信息。 |
| EventId.N | RepeatLi st | 否 | e- uf64yvznlao4jl2c **** | 一个或者多个系统事件ID。N的取值范围： 1~100，多个取值使用重复列表的形式。 |
| InstanceEventCyc leStatus.N | RepeatLi st | 否 | Executed | 一个或者多个系统事件的生命周期状态。N的取值范围：1~7，多个取值使用重复列表的形式。取值范围： Scheduled：等待执行事件。 Avoided：事件已避免。 Executing：事件执行中。 Executed：事件已完成执行。 Canceled：事件已取消。 Failed：事件执行失败。 Inquiring：事件问询中。 |
| EventCycleStatus | String | 否 | Executed | 系统事件的生命周期状态。 EventCycleStatus 参数只在未指定 InstanceEventCycleStatus.N 参数时有效。取值范围： Scheduled：等待执行事件。 Avoided：事件已避免。 Executing：事件执行中。 Executed：事件已完成执行。 Canceled：事件已取消。 Failed：事件执行失败。 Inquiring：事件问询中。 |

云服务器ECS

| InstanceEventTyp e.N | RepeatLi st | 否 | SystemMaintena nce.Reboot | 一个或者多个系统事件的类型。N的取值范围：1~30，多个取值使用重复列表的形式。 取值范围： SystemMaintenance.Reboot：因系统维护实例重启。 SystemMaintenance.Redeploy：因系统维护实例重新部署。 SystemFailure.Reboot：因系统错误实例重启。 SystemFailure.Redeploy：因系统错误实例重新部署。 SystemFailure.Delete：因实例创建失败实例释放。 InstanceFailure.Reboot：因实例错误实例重启。 |
|---|---|---|---|---|
| EventType | String | 否 | SystemMaintena nce.Reboot | 系统事件的类型。 EventType 参数只在未指定 InstanceEventType.N 参数时有效。取值范围： SystemMaintenance.Reboot：因系统维护实例重启。 SystemMaintenance.Redeploy：因系统维护实例重新部署。 SystemFailure.Reboot：因系统错误实例重启。 SystemFailure.Redeploy：因系统错误实例重新部署。 SystemFailure.Delete：因实例创建失败实例释放。 InstanceFailure.Reboot：因实例错误实例重启。 |
| NotBefore.Start | String | 否 | 2017-11- 30T06:32:31Z | 查询系统事件计划执行时间的开始时间。按照ISO 8601标准表示，并需要使用UTC +0 时间，格式为yyyy-MM-ddTHH:mm:ssZ。 |
| NotBefore.End | String | 否 | 2017-12- 01T06:32:31Z | 查询系统事件计划执行时间的结束时间。按照ISO 8601标准表示，并需要使用UTC +0 时间，格式为yyyy-MM-ddTHH:mm:ssZ。 |
| EventPublishTime .Start | String | 否 | 2017-11- 30T06:32:31Z | 查询系统事件发布时间的开始时间。按照ISO 8601标准表示，并需要使用UTC +0时间， 格式为yyyy-MM-ddTHH:mm:ssZ。 |
| EventPublishTime .End | String | 否 | 2017-12- 01T06:32:31Z | 查询系统事件发布时间的结束时间。按照ISO 8601标准表示，并需要使用UTC +0时间， 格式为yyyy-MM-ddTHH:mm:ssZ。 |
| ImpactLevel | String | 否 | 100 | 影响级别。 |
| PageNumber | Integer | 否 | 1 | 查询结果的页码。取值范围：正整数。 默认值：1。 |

云服务器ECS

| PageSize | Integer | 否 | 10 | 查询结果的分页大小。取值范围：1~100。 默认值：10。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceSyste mEventSet | Array of InstanceSyste mEventType |  | 实例历史系统事件数组。 |
| InstanceSyste mEventType |  |  |  |
| EventCycleStat us | Struct |  | 系统事件的生命周期状态。 |
| Code | Integer | 0 | 系统事件状态代码。 |
| Name | String | Executed | 系统事件状态名称。 |
| EventFinishTim e | String | 2017-12- 01T06:35:31Z | 系统事件结束时间。按照ISO 8601标准表示，并需要使用UTC +0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |
| EventId | String | e- uf64yvznlao4jl2c*** * | 系统事件ID。 |
| EventPublishTi me | String | 2017-11- 30T06:32:31Z | 系统事件发布时间。按照ISO 8601标准表示，并需要使用UTC +0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |
| EventType | Struct |  | 系统事件类型。 |
| Code | Integer | 34 | 系统事件类型代码。 |
| Name | String | InstanceExpiration.S top | 系统事件类型名称。 |
| ExtendedAttrib ute | Struct |  | 事件扩展属性。 |
| Device | String | /dev/vda | 本地盘设备名。 |
| DiskId | String | d- bp198jigq7l1xliw*** * | 本地盘ID。 |
| InactiveDisks | Array of InactiveDisk |  | 已释放但需要清理的非活跃云盘或本地盘信息。 |
| InactiveDisk |  |  |  |

| CreationTime | String | 2018-11- 30T06:32:31Z | 云盘或本地盘创建时间。按照ISO 8601标准表示， 并需要使用UTC +0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |
|---|---|---|---|
| DeviceCategor y | String | cloud efficiency _ | 云盘或本地盘的种类。可能值： cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ cloud pperf：高性能云盘。 _ cloud sperf：普通性能云盘。 _ san ssd：共享SSD盘。 _ san efficiency：共享高效云盘。 _ 说明默认ECS实例不支持创建共享 SSD盘和共享高效云盘。 |
| DeviceSize | String | 80 | 云盘或本地盘大小，单位GiB。 |
| DeviceType | String | data | 云盘或本地盘类型。可能值： system：系统盘 data：数据盘 |
| ReleaseTime | String | 2019-11- 30T06:32:31Z | 云盘或本地盘释放时间。按照ISO 8601标准表示， 并需要使用UTC +0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |
| ImpactLevel | String | 100 | 影响级别。 |
| InstanceId | String | i- uf678mass4zvr9n1* *** | 实例ID。 |
| NotBefore | String | 2017-12- 06T00:00:00Z | 系统事件计划执行时间。按照ISO 8601标准表示， 并需要使用UTC +0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |
| Reason | String | System maintenance is scheduled due to ***. | 系统事件的计划原因。 |
| PageNumber | Integer | 1 | 实例列表页码。 |
| PageSize | Integer | 10 | 输入时设置的每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

云服务器ECS

| TotalCount | Integer | 2 | 实例总个数。 |
|---|---|---|---|

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeInstanceHistoryEvents &RegionId=cn-qingdao-***** &InstanceId=i-uf678mass4zvr9n1**** &EventId.1=e-uf64yvznlao4jl2c**** &EventCycleStatus=Executed &InstanceEventType.1=SystemMaintenance.Reboot &NotBefore.Start=2017-11-30T06:32:31Z &NotBefore.End=2017-12-01T06:32:31Z &PageNumber=1 &PageSize=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
<InstanceSystemEventSet>
    <InstanceSystemEventType>
        <InstanceId>i-uf678mass4zvr9n1****</InstanceId>
        <EventId>e-uf64yvznlao4jl2c****</EventId>
        <EventType>
            <Code>1</Code>
            <Name>SystemMaintenance.Reboot</Name>
        </EventType>
        <EventCycleStatus>
            <Code>0</Code>
            <Name>Executed</Name>
        </EventCycleStatus>
        <EventPublishTime>2017-11-30T06:32:31Z</EventPublishTime>
        <NotBefore>2017-12-01T06:32:31Z</NotBefore>
        <EventFinishTime>2017-12-01T06:35:31Z</EventFinishTime>
    </InstanceSystemEventType>
    <InstanceSystemEventType>
        <InstanceId>i-uf678mass4zvr9n1****</InstanceId>
        <EventId>e-uf61cbvp0w8x2xfx****</EventId>
        <EventType>
            <Code>34</Code>
            <Name>InstanceExpiration.Stop</Name>
        </EventType>
        <EventCycleStatus>
            <Code>8</Code>
            <Name>Avoided</Name>
        </EventCycleStatus>
        <EventPublishTime>2017-11-29T06:32:31Z</EventPublishTime>
        <NotBefore>2017-12-06T00:00:00Z</NotBefore>
        <EventFinishTime>2017-12-05T12:35:31Z</EventFinishTime>
    </InstanceSystemEventType>
</InstanceSystemEventSet> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <TotalCount>2</TotalCount> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
    "InstanceSystemEventSet": {
        "InstanceSystemEventType": [
            {
                "InstanceId": "i-uf678mass4zvr9n1****",
                "EventId": "e-uf64yvznlao4jl2c****",
                "EventType": {
                    "Code": 1,
                    "Name": "SystemMaintenance.Reboot"
                },
                "EventCycleStatus": {
                    "Code": 0,
                    "Name": "Executed"
                },
                "EventPublishTime": "2017-11-30T06:32:31Z",
                "NotBefore": "2017-12-01T06:32:31Z",
                "EventFinishTime": "2017-12-01T06:35:31Z"
            },
            {
                "InstanceId": "i-uf678mass4zvr9n1****",
                "EventId": "e-uf61cbvp0w8x2xfx****",
                "EventType": {
                    "Code": 34,
                    "Name": "InstanceExpiration.Stop"
                },
                "EventCycleStatus": {
                    "Code": 8,
                    "Name": "Avoided"
                },
                "EventPublishTime": "2017-11-29T06:32:31Z",
                "NotBefore": "2017-12-06T00:00:00Z",
                "EventFinishTime": "2017-12-05T12:35:31Z"
            }
```

]

```json
    },
    "PageSize": 10,
    "PageNumber": 1,
    "TotalCount": 2,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 403 | InvalidParameter | %s | 无效的参数。 |
| 403 | EventIdLimitExceed ed | %s | 一次最多能指定100个模拟事件ID。 |
| 403 | InvalidParameter.Ti meEndBeforeStart | %s | 您输入的参数无效，请确认结束时间是否早于开始时间。 |

云服务器ECS

| 403 | OperationDenied.No tInWhiteList | %s | 该操作无效，请先加入白名单。 |
|---|---|---|---|

#### 地域

##### DescribeRegions

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeRegions | 系统规定参数，取值：DescribeRegions。 |
| ResourceType | String | 否 | instance | 资源类型。取值范围： instance：ECS实例 disk：磁盘默认值：instance。 |
| AcceptLanguag e | String | 否 | zh-CN | 根据汉语、英语和日语筛选返回结果。更多详情，请参见RFC7231。取值范围： zh-CN：中文 en-US：英文 ja：日文默认值：zh-CN。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Regions | Array |  | 地域信息集合。 |
| Region |  |  |  |
| LocalName | String | China (Qingdao) | 地域名称。 |
| RegionEndpoint | String | ecs.example.com | 地域对应的接入地址（Endpoint）。 |
| RegionId | String | cn-qingdao-env17- d01 | 地域ID。 |
| Status | String | available | 该参数暂未支持。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

云服务器ECS 请求示例

```
https://ecs.example.com/?Action=DescribeRegions &RegionId=cn-qingdao-env17-d01 &AcceptLanguage=en-US
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>38EC7366-F5A9-46B1-BDB1-0FDC2E296397</RequestId>
      <Regions>
            <Region>
                  <RegionId>cn-qingdao-et2-bo1</RegionId>
                  <RegionEndpoint>ecs.example.com</RegionEndpoint>
                  <LocalName>China (Qingdao)</LocalName>
            </Region>
            <Region>
                  <RegionId>cn-qingdao-nebula</RegionId>
                  <RegionEndpoint>ecs.cn-qingdao-nebula.example.com</RegionEndpoint>
                  <LocalName>cn-qingdao-nebula</LocalName>
            </Region>
      </Regions>
```

`JSON` 格式

```json
{
    "RequestId": "38EC7366-F5A9-46B1-BDB1-0FDC2E296397",
    "Regions": {
        "Region": [
            {
                "RegionId": "cn-qingdao-et2-b01",
                "RegionEndpoint": "ecs.example.com",
                "LocalName": "China (Qingdao)"
            },
            {
                "RegionId": "cn-qingdao-nebula",
                "RegionEndpoint": "ecs.cn-qingdao-nebula.example.com",
                "LocalName": "cn-qingdao-nebula"
            }
```

]

```
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Unauthorized.Empty Region | The specified account has no access authority to any region. | 当前账号未被授权访问任何地域，请您授权后再重试。 |

云服务器ECS

| 404 | InvalidAcceptLangu age.NotFound | Only Chinese (zh-CN), English (en-US), and Japanese (ja) are allowed. | 您选择的语言类型无效，现在只支持中文、英语和日语。 |
|---|---|---|---|
| 404 | InvalidResourceTyp e.NotFound | The ResourceType provided does not exist in our records. | 指定的资源类型不存在。 |

##### DescribeZones

接口说明 DescribeZones仅查询阿里云提供的可用区列表并返回少量库存信息。如果您需要查询某一可用区下的资源列

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceRegi onId | String | Host | 否 |  | 该参数暂未支持。 |
| Action | String | Query | 是 | DescribeZones | 系统规定参数。取值：DescribeZones 。 |
| OwnerId | Long | Query | 否 |  | 该参数暂未支持。 |
| ResourceO wnerAccou nt | String | Query | 否 |  | 该参数暂未支持。 |
| ResourceO wnerId | Long | Query | 否 |  | 该参数暂未支持。 |
| RegionId | String | Query | 是 | cn-qingdao-**** | 可用区所在的地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| OwnerAcco unt | String | Query | 否 |  | 该参数暂未支持。 |
| Verbose | Boole an | Query | 否 | false | 是否展示详细信息。 true：展示。 false：不展示。 默认值：true。 |
| InstanceCh argeType | String | Query | 否 |  | 该参数暂未支持。 |
| SpotStrate gy | String | Query | 否 |  | 该参数暂未支持。 |

| 开发指南·API参 | 考 |  |  |  | 云服务器EC |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AcceptLan guage | String | Query | 否 | zh-CN | 根据汉语、英语和日语筛选返回结果。更多信息，请参见RFC7231 。取值范围： zh-CN ：汉语。 en-US ：英语。 ja ：日语。 默认值：zh-CN。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Zones | Array |  | 数据中心信息Zone组成的集合。 |
| - AvailableResou rceCreation | Normal | DedicatedHost | 允许创建的资源类型。可能值： VSwitch：交换机。 IoOptimized：I/O优化实例。 Instance：实例。 DedicatedHost：专有宿主机。 Disk：云盘。 |
| - DedicatedHost Generations | Normal | ["ddh-6"] | 支持的专有宿主机代数列表。 |
| - AvailableInstan ceTypes | Normal | c5 | 当前可用区下可创建的所有规格列表。 |
| - AvailableDiskC ategories | Normal | cloud | 允许创建的云盘种类集合。可能值： cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ cloud pperf：高性能云盘。 _ cloud sperf：普通性能云盘。 _ san ssd：共享SSD盘。 _ san efficiency：共享高效云盘。 _ 默认不支持创建共享SSD盘和共享高效云盘。 |
| - AvailableDedic atedHostTypes | Normal | 计算型 | 支持的专有宿主机规格列表。 |
| - AvailableVolum eCategories | Normal | san ssd _ | 可以使用的共享存储类型。 |
| - AvailableResou rces | Array |  | 可供创建的具体资源组成的数组。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- SystemDiskCat egories | Normal | cloud ssd _ | 允许创建的系统盘类型。可能值： cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ cloud pperf：高性能云盘。 _ cloud sperf：普通性能云盘。 _ san ssd：共享SSD盘。 _ san efficiency：共享高效云盘。 _ 默认不支持创建共享SSD盘和共享高效云盘。 |
| -- InstanceGenera tions | Normal | Ⅳ | 支持的实例规格族代数。 |
| -- DataDiskCateg ories | Normal | cloud ssd _ | 允许创建的数据盘类型。可能值： cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ cloud pperf：高性能云盘。 _ cloud sperf：普通性能云盘。 _ san ssd：共享SSD盘。 _ san efficiency：共享高效云盘。 _ 默认不支持创建共享SSD盘和共享高效云盘。 |
| --InstanceTypes | Normal | ["ecs.g5.large"] | 当前可用区下可创建的所有规格列表。 |
| -- InstanceTypeFa milies | Normal | ["d1", "d1ne"] | 允许创建的实例规格族列表。 |
| --NetworkTypes | Normal | VPC | 支持的网络类型。可能值： VPC：专有网络VPC。 Classic：经典网络。 |
| --IoOptimized | Boolean | true | 是否为I/O优化实例。 |
| -ZoneId | String | cn-qingdao-****- amtest11001-a | 可用区ID。 |
| -ZoneType | String |  | 该参数暂未支持。 |
| -LocalName | String | 华东 1 可用区G | 可用区本地语言名。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |

**示例**

请求示例云服务器ECS

```
&RegionId=cn-qingdao-****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
  "Zones": {
    "Zone": [
      {
        "AvailableDiskCategories": {
          "DiskCategories": [
            "cloud"
```

]

```json
        },
        "AvailableResourceCreation": {
          "ResourceTypes": [
            "Instance",
            "Disk"
```

]

```json
        },
        "LocalName": "",
        "ZoneId": "cn-qingdao-****-amtest11001-b"
      },
      {
        "AvailableDiskCategories": {
          "DiskCategories": [
            "cloud"
```

]

```json
        },
        "AvailableResourceCreation": {
          "ResourceTypes": [
            "Instance",
            "Disk"
```

]

```json
        },
        "LocalName": "",
        "ZoneId": "cn-qingdao-****-amtest11001-a"
      }
```

]

```
  }
}
```

`XML` 格式云服务器ECS

```xml
      <Zones>
            <Zone>
                  <AvailableResourceCreation>
                        <ResourceTypes>Instance</ResourceTypes>
                        <ResourceTypes>Disk</ResourceTypes>
                  </AvailableResourceCreation>
                  <LocalName></LocalName>
                  <ZoneId>cn-qingdao-****-amtest11001-b</ZoneId>
                  <AvailableDiskCategories>
                        <DiskCategories>cloud</DiskCategories>
                  </AvailableDiskCategories>
            </Zone>
            <Zone>
                  <AvailableResourceCreation>
                        <ResourceTypes>Instance</ResourceTypes>
                        <ResourceTypes>Disk</ResourceTypes>
                  </AvailableResourceCreation>
                  <LocalName></LocalName>
                  <ZoneId>cn-qingdao-****-amtest11001-a</ZoneId>
                  <AvailableDiskCategories>
                        <DiskCategories>cloud</DiskCategories>
                  </AvailableDiskCategories>
            </Zone>
      </Zones>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidSpotStrat egy | InvalidSpotStrategy | The specified SpotStrategy is not valid. |
| 404 | REGION NOT FOUN _ _ D | InvalidRegionId.NotFound | The specified RegionId does not exist. |
| 404 | REGION NOT EXIST _ _ S | InvalidRegion.NotFound | The specified parameter RegionId is not valid. |
| 404 | Abs.InvalidInstance ChargeType.ValueN otSupported | InvalidInstanceChargeType.NotF ound | The InstanceChargeType does not exist in our records |
| 404 | InvalidAcceptLangu age.NotFound | InvalidAcceptLanguage.NotFoun d | Only Chinese (zh-CN), English (en-US), and Japanese (ja) are allowed. |

##### DescribeAvailableResource

调用DescribeAvailableResource查询某一可用区的资源列表。您可以在某一可用区创建实例 （RunInstances）或者修改实例规格（ModifyInstanceSpec）时查询该可用区的资源列表。 接口说明云服务器ECS 参数 `DestinationResource` 的取值有不同的逻辑与要求。在下列的顺序列表中，不同顺序的取值所需设置和可供选择的关联参数不同，您需要根据实际情况设置参数，不支持通过低顺序的取值筛选高顺序的资源类别。

```
取值顺序： Zone > IoOptimized > InstanceType = Network = ddh > SystemDisk > DataDisk 。
```

取值示例：

| 参数 | DestinationResource |  |  | 取值 |
|---|---|---|---|---|
| ResourceType |  | 参数值为 | disk |  |
| 参数 | DestinationResource |  |  | 取值 |

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-qingdao-env17-**** | 目标地域ID。您可以调用DescribeRegions 查看最新的阿里云地域列表。 |
| InstanceCh argeType | String | Query | 否 |  | 该参数暂未支持。 |
| SpotStrate gy | String | Query | 否 |  | 该参数暂未支持。 |
| SpotDurati on | Intege r | Query | 否 |  | 该参数暂未支持。 |
| Destinatio nResource | String | Query | 是 | InstanceType | 要查询的资源类型。取值范围： Zone：可用区。 IoOptimized：I/O优化。 InstanceType：实例规格。 SystemDisk：系统盘。 DataDisk：数据盘。 Network：网络类型。 ddh：专有宿主机。 参数 DestinationResource 的取值方式请参见本文中的接口说明 。 |
| ZoneId | String | Query | 否 | cn-qingdao-env17-*****-a | 可用区ID。 默认值：无，表示随机分配当前地域下的可用区，返回该地域（ RegionId ）下所有可用区的符合查询条件的资源。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| IoOptimize d | String | Query | 否 | optimized | 是否为I/O优化实例。取值范围： none：非I/O优化实例。 optimized：I/O优化实例。 默认值：optimized。 |
| Dedicated HostId | String | Query | 否 | dh- bp165p6xk2tlw61e**** | 专有宿主机ID。 |
| InstanceTy pe | String | Query | 否 | ecs.g5.large | 实例规格。更多信息，请参见 《云服务器ECS实例规格族& 实例规格简介》，也可以调用 DescribeInstanceTypes接口获得最新的规格表。 参数 InstanceType 的取值方式请参见本文中的接口说明 。 |
| SystemDis kCategory | String | Query | 否 | cloud ssd _ | 系统盘类型。取值范围： cloud efficiency：高效 _ 云盘。 cloud ssd：SSD云盘。 _ cloud pperf：高性能云 _ 盘。 cloud sperf：普通性能云 _ 盘。 san ssd：共享SSD盘。 _ san efficiency：共享高 _ 效云盘。 默认值：cloud efficiency。 _ 默认不支持创建共享SSD盘和共享高效云盘。 |
| DataDiskC ategory | String | Query | 否 | cloud ssd _ | 数据盘类型。取值范围： cloud efficiency：高效 _ 云盘。 cloud ssd：SSD云盘。 _ cloud pperf：高性能云 _ 盘。 cloud sperf：普通性能云 _ 盘。 san ssd：共享SSD盘。 _ san efficiency：共享高 _ 效云盘。 默认不支持创建共享SSD盘和共享高效云盘。 |

云服务器ECS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| NetworkCa tegory | String | Query | 否 | vpc |  | 网络类型。 仅支持取值为 vpc ，表示专有网络。 |  |  |
| Cores | Intege r | Query | 否 | 2 |  | 实例规格的vCPU内核数目。 取值请参见《云服务器ECS实例规格族&实例规格简介》。 当 DestinationResource 取值为 InstanceType 时， Cores 才为有效参数。 |  |  |
| Memory | Float | Query | 否 | 8.0 |  | 实例规格的内存大小，单位为 GiB。取值请参见《云服务器 ECS实例规格族&实例规格简介》。 当 DestinationResource 取值为 InstanceType 时， Memory 才为有效参数。 |  |  |
| ResourceT ype | String | Query | 否 | instance |  | 资源类型。取值范围： instance：ECS实例。 disk：云盘。 ddh：专有宿主机。 |  |  |
| Scope | String | Query | 否 |  |  | 该参数暂未支持。 |  |  |
| SourceRegi onId | String | Host | 否 |  |  | 该参数暂未支持。 |  |  |
| Action | String | Query | 是 | DescribeAvailableResourc e |  | 系统规定参数。取值： DescribeAvailable Resource 。 |  |  |
|  |  |  |  |  |  |  | DescribeAvailable |  |
|  |  |  |  |  |  | Resource |  |  |
| OwnerId | Long | Query | 否 |  |  | 该参数暂未支持。 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  | 该参数暂未支持。 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  | 该参数暂未支持。 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  | 该参数暂未支持。 |  |  |

|  |  | InstanceType |
|---|---|---|
|  | 为 |  |
|  | Cores |  |

|  |  | InstanceType |
|---|---|---|
|  | 为 |  |
|  | Memory |  |

**返回数据**

云服务器ECS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0041D94C-FB92- 4C49-B115- 259DA1C***** | 请求ID。 |
| AvailableZones | Array |  | 库存信息组成的集合。 |
| - AvailableResou rces | Array |  | 可供创建的具体资源组成的数组。 |
| -- SupportedReso urces | Array |  | 可供创建的具体资源组成的数组。 |
| ---Status | String | Available | 资源状态。可能值： Available：资源充足。 SoldOut：无资源。 |
| ---Value | String | ecs.d1ne.xlarge | 资源值。 |
| ---Max | Integer | 2 | 资源规格的最大值，该参数值为空时将不返回。 |
| ---Unit | String | null | 资源规格单位，该参数值为空时将不返回。 |
| --- StatusCategory | String | WithStock | 根据库存详细分类资源类别。可能值： WithStock：库存充足。 ClosedWithStock：库存供应保障能力低，建议选用WithStock状态的产品规格。 WithoutStock：无资源，将会补充资源，建议选用WithStock状态的产品规格。 ClosedWithoutStock：无资源，且不补充资源，请选用WithStock状态的产品规格。 |
| ---Min | Integer | 1 | 资源规格的最小值，该参数值为空时将不返回。 |
| --Type | String | InstanceType | 资源类型。可能值： Zone：可用区。 IoOptimized：I/O优化。 InstanceType：实例规格。 SystemDisk：系统盘。 DataDisk：数据盘。 Network：网络类型。 ddh：专有宿主机。 |
| -ZoneId | String | cn-qingdao-env17- ****-a | 可用区ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Status | String | Available | 可用区的状态描述。可能值： Available：资源充足。 SoldOut：无资源。 |
| - StatusCategory | String | WithStock | 根据可用区下库存情况对可用区状态进行详细描述。可能值： WithStock：库存充足。 ClosedWithStock：库存供应保障能力低，建议选用WithStock状态的产品规格。 WithoutStock：无资源，将会补充资源，建议选用WithStock状态的产品规格。 ClosedWithoutStock：无资源，且不补充资源，请选用WithStock状态的产品规格。 |
| -RegionId | String | cn-qingdao-env17- **** | 地域ID。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribeAvailableResource &RegionId=cn-qingdao-env17-**** &DestinationResource=InstanceType &IoOptimized=optimized &InstanceType=ecs.g5.large
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
    "RequestId": "0041D94C-FB92-4C49-B115-259DA1C*****",
    "AvailableZones": {
        "Status": "Available",
        "StatusCategory": "WithStock",
        "ZoneId": "cn-qingdao-env17-****-a",
        "RegionId": "cn-qingdao-env17-****",
        "AvailableResources": {
            "Type": "InstanceType",
            "SupportedResources": {
                "Status": "Available",
                "Min": 1,
                "StatusCategory": "WithStock",
                "Max": 2,
                "Value": "ecs.d1ne.xlarge",
                "Unit": "null"
            }
        }
    }
}
```

云服务器ECS `XML` 格式

```xml
    <RequestId>0041D94C-FB92-4C49-B115-259DA1C*****</RequestId>
    <AvailableZones>
            <Status>Available</Status>
            <StatusCategory>WithStock</StatusCategory>
            <ZoneId>cn-qingdao-env17-****-a</ZoneId>
            <RegionId>cn-qingdao-env17-****</RegionId>
            <AvailableResources>
                    <Type>InstanceType</Type>
                    <SupportedResources>
                            <Status>Available</Status>
                            <Min>1</Min>
                            <StatusCategory>WithStock</StatusCategory>
                            <Max>2</Max>
                            <Value>ecs.d1ne.xlarge</Value>
                            <Unit>null</Unit>
                    </SupportedResources>
            </AvailableResources>
    </AvailableZones>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidSaleStrat egy.ValueNotSuppor ted | Invalid.InstanceChargeType | The specified InstanceChargeType is not valid. |
| 400 | Abs.InvalidInstance ChargeType.ValueN otSupported | Invalid.InstanceChargeType | The specified InstanceChargeType is not valid. |
| 400 | Missing.Condition.Pa ram | Invalid.Param | The input parameter DestinationResource that is mandatory for processing this request is not supplied. |
| 400 | Abs.InvalidRegionId. MalFormed | InvalidRegionId.MalFormed | The specified parameter RegionId is not valid. |
| 403 | -305 | InvalidDedicatedHostId.NotFoun d | The specified DedicatedHostId does not exist. |
| 403 | InvalidParam.TypeA ndCpuMem.Conflict | InvalidParam.TypeAndCpuMem. Conflict | The specified 'InstanceType' and 'Cores','Memory' are not blank at the same time. |
| 403 | InvalidParam.Cores | InvalidParam.Cores | The specified parameter 'Cores' should be empty |
| 403 | InvalidParam.Memor y | InvalidParam.Memory | The specified parameter 'Memory' should be empty |
| 403 | InvalidParameter.Sc ope | InvalidParameter.Scope | The specified parameter Scope is invalid. |

|  | 开发指南·API参 | 考 |  | 云服务器EC | S |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | REGION NOT SUPPO _ _ RT SPOT DURATION _ _ INSTANCE _ | OperationDenied.RegionIdNotSu pported | region not support spot duration instance. |
| 403 | FLAVOR NOT SUPP _ _ ORT SPOT DURATIO _ _ N INSTANCE _ | OperationDenied.FlavorNotSupp orted | flavor not support spot duration instance. |
| 403 | TIMESTAMP NOT SU _ _ PPORT SPOT DURA _ _ TION INSTANCE _ | OperationDenied.TimestampNot Supported | timestamp not support spot duration instance. |
| 403 | RAM.UnacceptableP aram.ResourceOwn erId | InvalidParameter.ResourceOwne rId | The specified parameter ResourceOwnerId is not available anymore. |
| 404 | REGION NOT FOUN _ _ D | Invalid.RegionId | The specified RegionId does not exist. |
| 404 | NOT AVAILABLE RE _ _ GION EXISTS _ | Unavailable.Regions | The available regions does not exists |
| 404 | InvalidResourceTyp e.NotFound | Invalid.ResourceType | The ResourceType provided does not exist in our records. |
| 404 | Abs.InvalidDestinati onResource.ValueNo tSupported | Invalid.DestinationResource | The specified DestinationResource is not valid. |
| 404 | Abs.IoOptimized.Val ueNotSupported | Invalid.IoOptimized | The specified IoOptimized is not valid. |
| 404 | Abs.InvalidNetworkT ype.ValueNotSuppor ted | Invalid.NetworkCategory | The specified NetworkCategory is not valid. |
| 404 | Abs.InvalidSpotStrat egy | Invalid.SpotStrategy | The specified SpotStrategy is not valid. |
| 404 | Abs.IoOptimized.Val ueNotSupported | Invalid.IoOptimized | The specified IoOptimized is not valid. |
| 404 | Abs.IoOptimized.Val ueNotSupported | Invalid.IoOptimized | The specified IoOptimized is not valid. |
| 404 | Abs.InvalidNetworkT ype.ValueNotSuppor ted | Invalid.NetworkType | The specified NetworkType is not valid. |
| 404 | InvalidResourceId.N otFound | InvalidResourceId.NotFound | The specified ResourceId is not found in our records |
| 404 | -140 | InvalidRegionId.NotFound | The RegionId provided does not exist in our records. |

##### DescribeResourcesModification

调用DescribeResourcesModification查询升级和降配实例规格或者系统盘时，某一可用区的可用资源信息。 云服务器ECS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeResourc esModification | 系统规定参数。对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值： DescribeResourcesModification |
| DestinationRes ource | String | 是 | InstanceType | 目标资源类型。取值范围： InstanceType：实例规格。 SystemDisk：系统盘类型。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 目标地域ID。您可以调用DescribeRegions 查看最新的阿里云地域列表。 |
| ResourceId | String | 是 | i- bp67acfmxazb4p **** | 资源ID。例如，当待查询的资源为实例时， 可以理解为InstanceId。 |
| MigrateAcrossZ one | Boolean | 否 | true | 是否支持跨集群升级实例规格。取值范围： true：支持。 false：不支持。 默认值：false。 |
| InstanceType | String | 否 | ecs.g5.large | 实例规格。更多详情，请参见《云服务器 ECS用户指南》的实例规格，也可以调用 DescribeInstanceTypes接口获得最新的规格表。当参数DestinationResource取值为 SystemDisk时，必须同时指定 InstanceType参数。 |
| Cores | Integer | 否 | 2 | 实例规格的vCPU内核数目。取值请参见《云服务器ECS用户指南》的实例规格。当 DestinationResource=InstanceType参数有效，Cores才为有效参数。 |
| Memory | Float | 否 | 8.0 | 实例规格的内存大小，单位为GiB。取值请参见《云服务器ECS用户指南》的实例规格。 当 DestinationResource=InstanceType，M emory才为有效参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AvailableZones | Array |  | 数据中心信息AvailableZone组成的集合。 |
| AvailableZone |  |  |  |

云服务器ECS

| AvailableResou rces | Array |  | 可供创建的具体资源组成的数组。 |
|---|---|---|---|
| AvailableResou rce |  |  |  |
| SupportedReso urces | Array |  | 支持的可供创建的具体资源组成的数组。 |
| SupportedReso urce |  |  |  |
| Max | Integer | 2 | 资源规格的最大值，该参数值为空时不返回。 |
| Min | Integer | 1 | 资源规格的最小值，该参数值为空时不返回。 |
| Status | String | Available | 资源状态。可能值： Available：资源充足 SoldOut：资源告罄 |
| StatusCategory | String | WithStock | 根据库存详细分类资源类别。可能值： WithStock：库存充足 ClosedWithStock：库存接近水位低线 WithoutStock：库存告罄 |
| Unit | String | null | 资源规格单位，该参数值为空时不返回。 |
| Value | String | ecs.g5.large | 资源值。 |
| Type | String | InstanceType | 资源类型。可能值： Zone：可用区 IoOptimized：I/O优化 InstanceType：实例规格 SystemDisk：系统盘类型 DataDisk：数据盘类型 Network：网络类型 |
| RegionId | String | cn-qingdao-env17- d01 | 地域ID。 |
| Status | String | Available | 资源状态。可能值： Available：资源充足 SoldOut：资源告罄 |
| StatusCategory | String | WithStock | 根据库存详细分类资源类别。可能值： WithStock：库存充足 ClosedWithStock：库存接近水位低线 WithoutStock：库存告罄 |

云服务器ECS

| ZoneId | String | cn-qingdao-env17- amtest11001-a | 可用区ID。 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeResourcesModification &DestinationResource=InstanceType &RegionId=cn-qingdao-env17-d01 &ResourceId=i-bp67acfmxazb4p**** &MigrateAcrossZone=true &OperationType=Upgrade &InstanceType=ecs.g5.large
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
   <RequestId>994F2B60-B050-49E3-9283-44655FAC7A4X</RequestId>
   <AvailableZones>
      <AvailableZone>
         <Status>Available</Status>
         <RegionId>cn-qingdao-env17-d01</RegionId>
         <AvailableResources>
            <AvailableResource>
               <Type>InstanceType</Type>
               <SupportedResources>
                  <SupportedResource>
                     <Status>Available</Status>
                     <Value>ecs.g5.xlarge</Value>
                  </SupportedResource>
                  <SupportedResource>
                     <Status>Available</Status>
                     <Value>ecs.t5-lc1m2.large</Value>
                  </SupportedResource>
                  <SupportedResource>
                     <Status>Available</Status>
                     <Value>ecs.t5-c1m4.2xlarge</Value>
                  </SupportedResource>
                  <SupportedResource>
                     <Status>Available</Status>
                     <Value>ecs.c5.xlarge</Value>
                  </SupportedResource>
               </SupportedResources>
            </AvailableResource>
         </AvailableResources>
         <ZoneId>cn-qingdao-env17-amtest11001-a</ZoneId>
      </AvailableZone>
   </AvailableZones>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "994F2B60-B050-49E3-9283-44655FAC7A4X",
    "AvailableZones": {
        "AvailableZone": [
            {
                "Status": "Available",
                "RegionId": "cn-qingdao-env17-d01",
                "AvailableResources": {
                    "AvailableResource": [
                        {
                            "Type": "InstanceType",
                            "SupportedResources": {
                                "SupportedResource": [
                                    {
                                        "Status": "Available",
                                        "Value": "ecs.g5.xlarge"
                                    },
                                    {
                                        "Status": "Available",
                                        "Value": "ecs.t5-lc1m2.large"
                                    },
                                    {
                                        "Status": "Available",
                                        "Value": "ecs.t5-c1m4.2xlarge"
                                    },
                                    {
                                        "Status": "Available",
                                        "Value": "ecs.c5.xlarge"
                                    }
```

]

```
                            }
                        }
```

]

```json
                },
                "ZoneId": "cn-qingdao-env17-amtest11001-a"
            }
```

]

```
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | Invalid.RegionId | The specified RegionId does not exist. | 地域参数无效。 |
| 404 | Unavailable.Regions | The available regions does not exists | 地域参数无效。 |
| 400 | Invalid.OperationTy pe | The specified operationType is not valid. | 指定的参数“operationType”无效。 |
| 400 | Invalid.Param | The input parameter DestinationResource that is mandatory for processing this request is not supplied. | 目标资源类型无效。 |

云服务器ECS

| 404 | Invalid.ResourceTyp e | The ResourceType provided does not exist in our records. | 资源类型无效。 |
|---|---|---|---|
| 404 | Invalid.DestinationR esource | The specified DestinationResource is not valid. | 指定的目标资源无效。 |
| 404 | Invalid.IoOptimized | The specified IoOptimized is not valid. | 指定的参数“IoOptimized”无效。 |
| 404 | Invalid.NetworkCate gory | The specified NetworkCategory is not valid. | 指定的参数“NetworkCategory”无效。 |
| 404 | Invalid.SpotStrategy | The specified SpotStrategy is not valid. | 竞价策略参数无效。 |
| 400 | Invalid.InstanceChar geType | The specified InstanceChargeType is not valid. | 指定的参数“InstanceChargeType”无效。 |
| 404 | Invalid.ResourceId | The specified ResourceId is not valid. | 指定的参数“ResourceId”无效。 |
| 404 | Invalid.InstancePayT ype | The specified InstancePayType is not valid. | 指定的参数“InstanceChargeType”无效。 |
| 404 | OperationDenied | The specified operation is denied as this instanceType is not support. | 实例规格不支持当前操作。 |
| 403 | InvalidDedicatedHos tId.NotFound | The specified DedicatedHostId does not exist in our records. | 指定的宿主机在当前地域中不存在。 |
| 404 | InvalidInstanceId.No tFound | The specified InstanceId provided does not exist in our records. | 指定的实例不存在，请确认参数是否正确。 |
| 404 | InvalidResourceId.N otFound | The specified ResourceId is not found in our records | 指定的参数“ResourceId”无效，请确认该资源是否存在。 |
| 403 | InvalidParam.TypeA ndCpuMem.Conflict | The specified 'InstanceType' and 'Cores','Memory' are not blank at the same time. | 参数“InstanceType”、“Cores”、 “Memory”不能同时为空。 |
| 403 | InvalidParam.Cores | The specified parameter 'Cores' should be empty | 指定的参数“Cores”应该为空。 |
| 403 | InvalidParam.Memor y | The specified parameter 'Memory' should be empty | 指定的参数“Memory”应为空。 |

#### 运维与监控

##### GetInstanceConsoleOutput

调用GetInstanceConsoleOutput获取一台实例的系统命令行输出，数据以Base64编码后返回。

**接口说明**

云服务器ECS是虚拟化的云上服务，无法接入显示设备，也无法手动截屏。但是我们缓存了实例最近一次启动、重启或者关机时的系统命令行输出，您可以调用GetInstanceConsoleOutput获取。 Windows实例不支持获取系统命令行输出。

**请求参数**

云服务器ECS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | GetInstanceCons oleOutput | 系统规定参数。取值： GetInstanceConsoleOutput |
| InstanceId | String | 是 | i- bp1c1xhsrac2coi w**** | 实例ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所在地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConsoleOutput | String | V2VsY29tZSB0byBD ZW50T1MgCgpDaG Vja2luZyBmaWxlc3l zdGVtcwpDaGVja2lu ZyBhbGwgZmlsZSB zeXN0ZW1zLgpbL3 NiaW4vZnNjay5leH Q0ICgxKSAtLSAvXS Bmc2NrLmV4dDQgL WEgL2Rldi92ZGExIA ovZGV2L3ZkYTE6IG NsZWFuLCAzMjAxNi 8yNjIxNDQwIGZpbG VzLCA0NDc5NzQvM TA0ODU1MDQgYmx vY2tzCgpFbnRlcmlu ZyBub24taW50ZXJh Y3RpdmUgc3RhcnR 1cApDYWxsaW5nIH RoZSBzeXN0ZW0gY WN0aXZpdHkgZGF0 YSBjb2xsZWN0b3Ig KHNhZGMpLi4uIAoK QnJpbmdpbmcgdXA gaW50ZXJmYWNlIG V0aDA6ICAKRGV0Z XJtaW5pbmcgSVAga W5mb3JtYXRpb24g Zm9yIGV0aDAuLi4g ZG9uZS4KCmFsaXl1 bi1zZXJ2aWNlIHN0Y XJ0L3J1bm5pbmcsIH Byb2Nlc3MgMTczM wpmaW5pc2hlZAoK Q2VudE9TIHJlbGVhc 2UgNi44IChGaW5hb CkKS2VybmVsIDIuNi 4zMi02OTYuMy4yL mVsNi5pNjg2IG9uIG FuIGk2ODYKCmlaMn plZDk2ZTQ2MmF5cj BxeioqKioqIGxvZ2lu Og== | 实例的系统命令行输出，根据Base64编码后输出。 |

云服务器ECS

| InstanceId | String | i- bp1c1xhsrac2coiw** ** | 实例ID。 |
|---|---|---|---|
| LastUpdateTim e | String | 2018-03-22 10:04:57 | 实例最近一次启动、重启或者关机的时间。按照 ISO8601标准表示，并使用UTC时间，格式为 yyyy-MM-ddTHH:mm:ssZ。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http://ecs.example.com/?Action=GetInstanceConsoleOutput &InstanceId=i-bp1c1xhsrac2coiw**** &RegionId=cn-qingdao-env17-d01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>22A1933F-AD02-4560-A6A7-53CF2231D942</RequestId>
      <InstanceId>i-bp1c1xhsrac2coiw****</InstanceId>
      <LastUpdateTime>2018-03-22 10:04:57</LastUpdateTime>
<ConsoleOutput>V2VsY29tZSB0byBDZW50T1MgCgpDaGVja2luZyBmaWxlc3lzdGVtcwpDaGVja2luZyBhbGwgZmlsZSB XN0ZW1zLgpbL3NiaW4vZnNjay5leHQ0ICgxKSAtLSAvXSBmc2NrLmV4dDQgLWEgL2Rldi92ZGExIAovZGV2L3ZkYTE6IGN WFuLCAzMjAxNi8yNjIxNDQwIGZpbGVzLCA0NDc5NzQvMTA0ODU1MDQgYmxvY2tzCgpFbnRlcmluZyBub24taW50ZXJhY3R mUgc3RhcnR1cApDYWxsaW5nIHRoZSBzeXN0ZW0gYWN0aXZpdHkgZGF0YSBjb2xsZWN0b3IgKHNhZGMpLi4uIAoKQnJpbm mcgdXAgaW50ZXJmYWNlIGV0aDA6ICAKRGV0ZXJtaW5pbmcgSVAgaW5mb3JtYXRpb24gZm9yIGV0aDAuLi4gZG9uZS4KCm Xl1bi1zZXJ2aWNlIHN0YXJ0L3J1bm5pbmcsIHByb2Nlc3MgMTczMwpmaW5pc2hlZAoKQ2VudE9TIHJlbGVhc2UgNi44ICh W5hbCkKS2VybmVsIDIuNi4zMi02OTYuMy4yLmVsNi5pNjg2IG9uIGFuIGk2ODYKCmlaMnplZDk2ZTQ2MmF5cjBxeioqKi GxvZ2luOg==</ConsoleOutput>
```

`JSON` 格式

```json
{
    "RequestId": "22A1933F-AD02-4560-A6A7-53CF2231D942",
    "InstanceId": "i-bp1c1xhsrac2coiw****",
    "LastUpdateTime": "2018-03-22 10:04:57",
    "ConsoleOutput":
"V2VsY29tZSB0byBDZW50T1MgCgpDaGVja2luZyBmaWxlc3lzdGVtcwpDaGVja2luZyBhbGwgZmlsZSBzeXN0ZW1zLgpb iaW4vZnNjay5leHQ0ICgxKSAtLSAvXSBmc2NrLmV4dDQgLWEgL2Rldi92ZGExIAovZGV2L3ZkYTE6IGNsZWFuLCAzMjAxN yNjIxNDQwIGZpbGVzLCA0NDc5NzQvMTA0ODU1MDQgYmxvY2tzCgpFbnRlcmluZyBub24taW50ZXJhY3RpdmUgc3RhcnR1 DYWxsaW5nIHRoZSBzeXN0ZW0gYWN0aXZpdHkgZGF0YSBjb2xsZWN0b3IgKHNhZGMpLi4uIAoKQnJpbmdpbmcgdXAgaW50 mYWNlIGV0aDA6ICAKRGV0ZXJtaW5pbmcgSVAgaW5mb3JtYXRpb24gZm9yIGV0aDAuLi4gZG9uZS4KCmFsaXl1bi1zZXJ2 lIHN0YXJ0L3J1bm5pbmcsIHByb2Nlc3MgMTczMwpmaW5pc2hlZAoKQ2VudE9TIHJlbGVhc2UgNi44IChGaW5hbCkKS2Vyb sIDIuNi4zMi02OTYuMy4yLmVsNi5pNjg2IG9uIGFuIGk2ODYKCmlaMnplZDk2ZTQ2MmF5cjBxeioqKioqIGxvZ2luOg== }
```

云服务器ECS

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 404 | InvalidParameter | %s | 无效的参数。 |
| 405 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 405 | NotSupported | %s | 您当前的操作无效。 |
| 429 | Throttling | %s | 请求被流控。 |

##### GetInstanceScreenshot

**接口说明**

云服务器ECS返回Base64编码后的JPG图像格式的实例截屏后，您需要自行解码。您可以在排查故障时调用该接口，并请注意： 实例必须处于运行中（Running）状态。 在同一台实例中多次调用该接口时，调用的间隔时间至少10秒，否则将返回错误码 `Throttling` 。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | GetInstanceScree nshot | 系统规定参数。取值： GetInstanceScreenshot |
| InstanceId | String | 是 | i- bp1gbz20g229bv u5**** | 实例ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 实例所在地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| WakeUp | Boolean | 否 | false | 是否唤醒处于休眠状态的实例。 默认值：false |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceId | String | i- bp1gbz20g229bvu5 **** | 实例ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

云服务器ECS

| Screenshot | String | iVBORw0KGgoA...AA ABJRU5ErkJggg== | JPG图像格式的实例截屏，返回Base64编码后的图像。 |
|---|---|---|---|

**示例**

请求示例

```
http://ecs.example.com/?Action=GetInstanceScreenshot &InstanceId=i-bp1gbz20g229bvu5**** &RegionId=cn-qingdao-env17-d01 &WakeUp=false
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>22A1933F-AD02-4560-A6A7-53CF2231D942</RequestId>
      <InstanceId>i-bp1gbz20g229bvu5****</InstanceId>
      <Screenshot>iVBORw0KGgoA...AAABJRU5ErkJggg==</Screenshot>
```

`JSON` 格式

```json
{
    "RequestId": "22A1933F-AD02-4560-A6A7-53CF2231D942",
    "InstanceId": "i-bp1gbz20g229bvu5****",
    "Screenshot": "iVBORw0KGgoA...AAABJRU5ErkJggg=="
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | %s | 缺失参数，请检查参数是否完整。 |
| 404 | InvalidParameter | %s | 无效的参数。 |
| 405 | IncorrectInstanceSta tus | %s | 当前实例的状态不支持此操作。 |
| 405 | NotSupported | %s | 您当前的操作无效。 |
| 429 | Throttling | %s | 请求被流控。 |

##### DescribeSnapshotMonitorData

调用DescribeSnapshotMonitorData查询一个地域下近30天内的快照容量变化监控数据。

**接口说明**

调用该接口时，您需要注意： 每次最多返回400条监控数据，如果指定的参数 `(EndTime - StartTime)/Period` 大于400时，则返回错误。 云服务器ECS 单次最多能查询近30天内的监控信息，如果指定的参数 `StartTime` 超过30天，则返回错误。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeSnapsho tMonitorData | 系统规定参数。取值： DescribeSnapshotMonitorData |
| EndTime | String | 是 | 2019-05- 10T03:00:00Z | 获取快照容量变化数据的结束时间点。按照 ISO8601标准表示，并使用UTC +0时间， 格式为yyyy-MM-ddTHH:mm:ssZ。如果指定的秒（ss）不是 00，则自动换算为下一分钟。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| StartTime | String | 是 | 2019-05- 10T00:00:00Z | 获取快照容量变化数据的起始时间点。按照 ISO8601标准表示，并使用UTC +0时间， 格式为yyyy-MM-ddTHH:mm:ssZ。如果指定的秒（ss）不是 00，则自动换算为下一分钟。 |
| Period | Integer | 否 | 60 | 获取快照容量变化数据的间隔时间，单位为秒。取值范围： 60 600 3600 默认值：60。 |
| Category | String | 否 | Standard | 快照类型。取值范围： Standard：普通快照 Flash：本地快照默认值：Standard。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MonitorData | Array |  | 快照容量变化数据的集合。 |
| DataPoint |  |  |  |
| Size | Long | 243036848128 | 快照总容量，单位：字节（Byte）。 |
| TimeStamp | String | 2019-05- 10T04:00:00Z | 某一快照容量数值对应的时间戳。 |

云服务器ECS

| RequestId | String | 9F8163A8-F5DE- 47A2-A572- 4E062D223E09 | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
https://ecs.example.com/?&Action=DescribeSnapshotMonitorData &RegionId=cn-qingdao-env17-d01 &StartTime=2019-05-10T00:00:00Z &EndTime=2019-05-10T03:00:00Z &Period=60
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
     <MonitorData>
          <DataPoint>
               <element>
                    <Size>243036848128</Size>
                    <TimeStamp>2019-05-10T01:00:00Z</TimeStamp>
               </element>
               <element>
                    <Size>243036848128</Size>
                    <TimeStamp>2019-05-10T02:00:00Z</TimeStamp>
               </element>
               <element>
                    <Size>243036848128</Size>
                    <TimeStamp>2019-05-10T03:00:00Z</TimeStamp>
               </element>
          </DataPoint>
     </MonitorData>
     <RequestId>9F8163A8-F5DE-47A2-A572-4E062D223E09</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
 "RequestId": "9F8163A8-F5DE-47A2-A572-4E062D223E09",
 "MonitorData": {
  "DataPoint": [
   {
    "TimeStamp": "2019-05-10T01:00:00Z",
    "Size": 243036848128
   },
   {
    "TimeStamp": "2019-05-10T02:00:00Z",
    "Size": 243036848128
   },
   {
    "TimeStamp": "2019-05-10T03:00:00Z",
    "Size": 243036848128
   }
        ]}
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidStartTime.Mal formed | The specified parameter "StartTime" is not valid. | 指定的开始时间格式不合法。 |
| 400 | InvalidEndTime.Malf ormed | The specified parameter "EndTime" is not valid. | 指定的结束时间格式不合法。 |
| 400 | InvalidPeriod.ValueN otSupported | The specified parameter "Period" is not valid. | 指定的 Period 参数不合法。 |
| 400 | InvalidStartTime.Too Early | The specified parameter "StartTime" is too early. | 指定的开始时间太早。 |
| 400 | InvalidParameter.To oManyDataQueried | Too many data queried. | 监控数据节点超出范围。 |
| 400 | Throttling | Request was denied due to request throttling. | 当前的操作太过频繁，请稍后重试。 |

##### DescribeEniMonitorData

调用DescribeEniMonitorData查询一块辅助网卡在指定时间段内使用的流量信息。

**接口说明**

可查询的辅助网卡流量信息包括辅助网卡收发数据包的数量、内网出入流量、辅助网卡收发丢包的数量。当返回信息中缺少部分内容时，可能是由于系统没有获取到相应的信息。例如，当时实例处于已停止（Stopped）状态或者辅助网卡没有挂载到实例上，即处于可用（Available）状态时，无法获取到相应的信息。调用该接口时，您需要注意： 每次最多返回400条监控数据，即如果指定的参数(EndTime - StartTime)/Peroid>400，则返回错误。 单次最多能查询近30天内的监控信息，如果指定的参数StartTime超过30天，则返回错误。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云服务器ECS

| Action | String | 否 | DescribeEniMonit orData | 系统规定参数。取值： DescribeEniMonitorData |
|---|---|---|---|---|
| EndTime | String | 是 | 2018-05- 21T12:22:00Z | 获取数据的结束时间点。按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy- MM-ddTHH:mm:ssZ。如果指定的秒 （ss）不是00，则自动换算为下一分钟。 |
| InstanceId | String | 是 | i- m5e88p52tbip9r 2x**** | 辅助网卡绑定的实例ID。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| StartTime | String | 是 | 2018-05- 21T12:19:00Z | 获取数据的起始时间点。按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy- MM-ddTHH:mm:ssZ。如果指定的秒 （ss）不是00，则自动换算为下一分钟。 |
| EniId | String | 否 | eni- m5e0ajic0vbwx7l 3**** | 辅助网卡的ID。默认查询指定实例上所有已绑定的辅助网卡。 |
| Period | Integer | 否 | 60 | 获取监控数据的间隔时间，单位：秒。取值范围： 60 600 3600 默认值：60 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MonitorData | Array |  | 辅助网卡流量的监控数据EniMonitorDataType组成的集合。 |
| EniMonitorData |  |  |  |
| DropPacketRx | String | 0 | 辅助网卡接收丢弃的内网数据包，单位： packets。 |
| DropPacketTx | String | 0 | 辅助网卡发送丢弃的内网数据包，单位： packets。 |
| EniId | String | eni- m5e0ajic0vbwx7l3* *** | 辅助网卡ID。 |
| IntranetRx | String | 0 | 辅助网卡接收的内网数据流量，单位：kbits。 |

云服务器ECS

| IntranetTx | String | 0 | 辅助网卡发送的内网数据流量，单位：kbits。 |
|---|---|---|---|
| PacketRx | String | 0 | 辅助网卡接收的内网数据包，单位：packets。 |
| PacketTx | String | 0 | 辅助网卡发送的内网数据包，单位：packets。 |
| TimeStamp | String | 2018-05- 21T03:22:00Z | 查询监控信息的时间戳。按照ISO8601标准表示， 并使用UTC +0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 4 | 返回条目数量。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeEniMonitorData &EndTime=2018-05-21T12:22:00Z &InstanceId=i-m5e88p52tbip9r2x**** &RegionId=cn-qingdao-env17-d01 &StartTime=2018-05-21T12:19:00Z &EniId=eni-m5e0ajic0vbwx7l3**** &Period=60
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
   <RequestId>5A03C2BA-3BCE-4A87-8076-7DC1629</RequestId>
   <TotalCount>4</TotalCount>
   <MonitorData>
         <EniMonitorData>
               <PacketTx>0</PacketTx>
               <TimeStamp>2018-05-21T03:22:00Z</TimeStamp>
               <IntranetOut>0</IntranetOut>
               <DropPacketRx>0</DropPacketRx>
               <IntranetIn>0</IntranetIn>
               <EniId>eni-m5e0ajic0vbwx7l3****</EniId>
               <DropPacketTx>0</DropPacketTx>
               <PacketRx>0</PacketRx>
         </EniMonitorData>
         <EniMonitorData>
               <PacketTx>0</PacketTx>
               <TimeStamp>2018-05-21T03:21:00Z</TimeStamp>
               <IntranetOut>0</IntranetOut>
               <DropPacketRx>0</DropPacketRx>
               <IntranetIn>0</IntranetIn>
               <EniId>eni-m5e0ajic0vbwx7l3****</EniId>
               <DropPacketTx>0</DropPacketTx>
               <PacketRx>0</PacketRx>
         </EniMonitorData>
         <EniMonitorData>
               <PacketTx>52240</PacketTx>
               <TimeStamp>2018-05-21T03:19:00Z</TimeStamp>
               <IntranetOut>73344</IntranetOut>
               <DropPacketRx>0</DropPacketRx>
               <IntranetIn>467</IntranetIn>
               <EniId>eni-m5e0ajic0vbwx7l3****</EniId>
               <DropPacketTx>0</DropPacketTx>
               <PacketRx>6603</PacketRx>
         </EniMonitorData>
         <EniMonitorData>
               <PacketTx>34925</PacketTx>
               <TimeStamp>2018-05-21T03:20:00Z</TimeStamp>
               <IntranetOut>48871</IntranetOut>
               <DropPacketRx>0</DropPacketRx>
               <IntranetIn>350</IntranetIn>
               <EniId>eni-m5e0ajic0vbwx7l3****</EniId>
               <DropPacketTx>0</DropPacketTx>
               <PacketRx>4888</PacketRx>
         </EniMonitorData>
   </MonitorData>
```

`JSON` 格式云服务器ECS

```json
{
 "RequestId":"5A03C2BA-3BCE-4A87-8076-7DC1629",
 "MonitorData":{
     "EniMonitorData":[
         {
             "PacketTx":0,
             "TimeStamp":"2018-05-21T03:22:00Z",
             "IntranetOut":0,
             "DropPacketRx":0,
             "IntranetIn":0,
             "EniId":"eni-m5e0ajic0vbwx7l3****",
             "DropPacketTx":0,
             "PacketRx":0
         },
         {
             "PacketTx":0,
             "TimeStamp":"2018-05-21T03:21:00Z",
             "IntranetOut":0,
             "DropPacketRx":0,
             "IntranetIn":0,
             "EniId":"eni-m5e0ajic0vbwx7l3****",
             "DropPacketTx":0,
             "PacketRx":0
         },
         {
             "PacketTx":52240,
             "TimeStamp":"2018-05-21T03:19:00Z",
             "IntranetOut":73344,
             "DropPacketRx":0,
             "IntranetIn":467,
             "EniId":"eni-m5e0ajic0vbwx7l3****",
             "DropPacketTx":0,
             "PacketRx":6603
         },
         {
             "PacketTx":34925,
             "TimeStamp":"2018-05-21T03:20:00Z",
             "IntranetOut":48871,
             "DropPacketRx":0,
             "IntranetIn":350,
             "EniId":"eni-m5e0ajic0vbwx7l3****",
             "DropPacketTx":0,
             "PacketRx":4888
         }
```

]

```
 }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDiskId.NotFou nd | The DiskId provided does not exist in our records. | 指定的磁盘不存在。请您检查磁盘 ID 是否正确。 |

云服务器ECS

| 403 | InvalidStartTime.Mal formed | The specified parameter "StartTime" is not valid. | 指定的开始时间格式不合法。 |
|---|---|---|---|
| 403 | InvalidEndTime.Malf ormed | The specified parameter "EndTime" is not valid. | 指定的结束时间格式不合法。 |
| 403 | InvalidPeriod.ValueN otSupported | The specified parameter "Period" is not valid. | 指定的 Period 参数不合法。 |
| 403 | InvalidStartTime.Too Early | The specified parameter "StartTime" is too early. | 指定的开始时间太早。 |
| 403 | InvalidParameter.To oManyDataQueried | Too many data queried. | 监控数据节点超出范围。 |
| 403 | Throttling | Request was denied due to request throttling. | 当前的操作太过频繁，请稍后重试。 |
| 403 | InvalidInstanceType. NotSupportCredit | The InstanceType of the specified instance does not support credit. | 实例规格不支持突发性能实例。 |
| 403 | InvalidParameter.En dTime | The specified parameter EndTime is earlier than StartTime. | 结束时间不能早于开始时间。 |
| 4003 | InvalidParam.Malfor med | The specified parameter "EniId" and "InstanceId" are not valid | 指定的参数无效。 |

#### 云助手

##### CreateCommand

**接口说明**

您可以创建以下类型的命令： Windows实例适用的Bat脚本（RunBatScript） Windows实例适用的PowerShell脚本（RunPowerShellScript） Linux实例适用的Shell脚本（RunShellScript） 您可以通过指定参数TimeOut为命令设置在ECS实例中执行时最大的超时时间，命令执行超时后，云助手客户端会强制终止命令进程，即取消命令的PID。 对于单次执行，超时后，该命令针对指定的ECS实例的执行状态（InvokeRecordStatus）变为执行失败 （Failed）。 对于周期执行： 周期执行的超时时间对每一次执行记录均有效。 某次执行超时后，该次执行记录的状态（InvokeRecordStatus）变为执行失败（Failed）。 上次执行超时与否不影响下一次执行。 您可以通过指定参数WorkingDir为命令指定执行路径。对于Linux实例，默认在管理员root用户的home目录下，具体为 `/root` 目录。对于Windows实例，默认在云助手客户端进程所在目录，例如，C:\Windows\System32\。 您可以通过指定参数EnableParameter=true启用自定义参数功能。在设置CommandContent时可以通过 {{parameter}}的形式表示自定义参数，并在运行命令（InvokeCommand）时，传入自定义参数键值对。 例如，您在创建命令时，创建了 `echo {{name}}` 命令，在 InvokeCommand时，通过Parameters参数传云服务器ECS 入键值对 `<name, Jack>` 。则自定义参数将自动替换命令，您会得到一条新的命令，并在实例中执行 `echo` `Jack` 。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateCommand | 系统规定参数。取值：CreateCommand。 |
| CommandConten t | String | 是 | ZWNobyAxMjM= | 命令Base64编码后的内容。 该参数的值必须使用Base64编码后传输，且脚本内容的大小在Base64编码之后不能超过18 KB。 命令内容支持使用自定义参数形式，具体通过指定参数 EnableParameter=true 启用自定义参数功能： 自定义参数用 {{}} 包含的方式定义，在 {{}} 内参数名前后的空格以及换行符会被忽略。 自定义参数个数不能超过20个。 自定义参数名允许 a~z 、 A~Z 、 0~9 、 - 的组合，不支持其余字符，参数名 _ 不区分大小写。 单个参数名不能超过64字节。 |
| Name | String | 是 | testName | 命令名称。支持全字符集，长度不得超过 128个字符。 |
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查看地域ID。 |
| Type | String | 是 | RunShellScript | 命令的类型。取值范围： RunBatScript：创建一个在Windows实例中运行的Bat脚本。 RunPowerShellScript：创建一个在 Windows实例中运行的PowerShell脚本。 RunShellScript：创建一个在Linux实例中运行的Shell脚本。 |
| Description | String | 否 | testDescription | 命令描述，支持全字符集。长度不得超过 512个字符。 |
| WorkingDir | String | 否 | /root/ | 创建的命令在ECS实例中运行的目录。 默认值： Linux实例：管理员root用户的home目录下，具体为/root目录。 Windows实例：云助手客户端进程所在目录，例如 C:\Windows\System32 。 |

|  | a~z |
|---|---|
| _ |  |

云服务器ECS

| Timeout | Long | 否 | 60 | 创建的命令在ECS实例中执行时最大的超时时间，单位为秒。当因为某种原因无法运行您创建的命令时，会出现超时现象。超时后，会强制终止命令进程，即取消命令的 PID。 默认值：60。 |
|---|---|---|---|---|
| EnableParameter | Boolean | 否 | false | 创建的命令是否使用自定义参数。取值范围： true：是。 false：否。 默认值：false。 |
| ContentEncoding | String | 否 | Base64 | 命令内容（CommandContent）的编码方式。取值范围： PlainText：不编码，采用明文传输。 Base64：Base64编码。 默认值：Base64。 说明错填该取值会当作 Base64处理。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CommandId | String | c- 7d2a745b412b4601 b2d47f6a768d**** | 命令ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DEC**** | 请求ID。 |

**示例**

请求示例

```
&CommandContent=ZWNobyAxMjM= &Name=testName &RegionId=cn-qingdao-**** &Type=RunShellScript &ContentEncoding=Base64
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DEC****</RequestId>
  <CommandId>c-7d2a745b412b4601b2d47f6a768d****</CommandId>
```

云服务器ECS `JSON` 格式

```json
{
    "RequestId": "E69EF3CC-94CD-42E7-8926-F133B863****",
    "CommandId": "c-7d2a745b412b4601b2d47f6a768d****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 403 | InvalidCmdType.Not Found | The specified command type does not exist. | 指定的命令类型不存在。 |
| 403 | CmdContent.Exceed Limit | The length of the command content exceeds the upper limit. | 命令内容长度超过上限。 |
| 403 | CmdName.ExceedLi mit | The length of the command name exceeds the upper limit. | 命令名称长度超过上限。 |
| 403 | CmdDesc.ExceedLi mit | The length of the command description exceeds the upper limit. | 命令描述长度超过上限。 |
| 403 | CmdCount.ExceedQ uota | The total number of commands in the current region exceeds the quota. | 当前地域下的云助手命令数量已超出限。 |
| 403 | CmdParam.EmptyKe y | You must specify the parameter names. | 请检查您的参数是否完整，是否有参数名未填写的情况。 |
| 403 | CmdParam.InvalidPa ramName | Invalid parameter name. The name can contain only lowercase letters (a to z), uppercase letters (A to Z), numbers (0 to 9), hyphens (-), and underscores ( ). _ | 自定义参数的参数名无效，只允许 a- zA-Z0-9- 的组合。 _ |
| 403 | CmdParamName.Ex ceedLimit | The maximum length of a parameter name is exceeded. | 您的自定义参数的参数名长度超过限制。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### InvokeCommand

**接口说明**

对目标ECS实例有如下限制。选择了多台ECS实例后，若其中某台实例不满足执行条件，您需要重新调用接口。 网络类型是专有网络VPC。 状态必须为运行中（ `Running` ）。 已预先安装云助手客户端。具体操作，请参见InstallCloudAssistant。 云服务器ECS 执行类型为PowerShell的命令时，实例必须已经配置了PowerShell模块。 单次执行（ `Timed=false` ），只执行一次命令。 周期执行（ `Timed=true` ）： 根据参数 `Frequency` 指定的时间频率定时执行，上次的执行结果不对下一次执行产生任何影响。 时间设置基准为UTC +0，且该时间以实例的系统时间为准。请确保ECS实例的时间或者时区与您预期的时间一致。 命令的执行可能会因为目标实例的状态异常、网络异常或云助手客户端异常而出现无法执行的情况，无法执行时不会生成执行信息。 当您创建命令时启用了自定义参数功能，需要在执行命令时传入自定义参数（ `Parameters` ）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | InvokeCommand | 系统规定参数，取值：InvokeCommand。 |
| CommandId | String | 是 | c- e9962872063249 75b5fbe1d******* * | 命令ID。您可以通过接口 DescribeCommands查询所有可用的 CommandId。 |
| InstanceId.N | RepeatLi st | 是 | i- bp185dy2o3o6n* ***** | 需要执行命令的实例列表，最多能指定50台实例ID。N的取值范围：1~50。 |
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查看地域ID。 |

云服务器ECS

| RepeatMode | String | 否 | Once | 设置命令执行的方式。取值范围： Once：立即执行命令。 Period：定时执行命令。当该参数取值为 Period 时，必须同时指定 Timed=true 参数值以及 Frequency 参数。 NextRebootOnly：当实例下一次启动时，自动执行命令。 EveryReboot：实例每一次启动都将自动执行命令。 默认值： 当不指定 Timed=true 参数值以及 Frequency 参数时，默认值为 Once 。 当指定 Timed=true 参数值以及 Frequency 参数时，无论是否已设置了该参数值，都将按照 Period 处理。 注意事项： 当该参数取值 Period 、 NextRebootOnly 或者 EveryReboot 时，您可以调用 StopInvocation 停止待执行的命令或定时执行的命令。 当该参数取值 Period 或者 EveryReboot 时，您可以调用 DescribeInvocationResults ，然后指定 IncludeHistory=true 查看命令定时执行的历史记录。 |
|---|---|---|---|---|
| Timed | Boolean | 否 | true | 命令是否为周期执行。取值范围： true：是。 false：否。 默认值：false。 |
| Frequency | String | 否 | 0 */20 * * * * | 周期任务的执行周期，两次周期任务的时间间隔不能低于10秒。当参数 Timed 的值为 true 时， Frequency 为必选参数。 该参数取值遵循Cron表达式。具体信息，请参见《云服务器ECS用户指南》中的Cron表达式章节。 |

|  | Timed=true |
|---|---|
| Frequency |  |
| Once |  |

|  | Period |
|---|---|
| EveryReboot |  |

|  | Timed |
|---|---|
| Frequency |  |

云服务器ECS

| Parameters | Json | 否 | {"name":"Jack", "accessKey":"LTA Idyv******aRY"} | 启用自定义参数功能时，执行命令时传入的自定义参数的键值对。自定义参数的个数范围：0~10。 Map的键不允许为空字符串，最多支持64 个字符。 Map的值允许为空字符串。 自定义参数与原始命令内容在Base64编码后，综合长度不能超过18 KB。 设置的自定义参数名集合必须为创建命令时定义的参数集的子集。对于未传入的参数，您可以使用空字符串代替。 您可以取消设置该参数从而禁用自定义参数。 |
|---|---|---|---|---|
| Username | String | 否 | root | 在ECS实例中执行命令的用户名称。 说明该参数仅支持Linux系统的ECS实例，默认以root用户执行命令。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InvokeId | String | t- 7d2a745b412b4601 b2d47f6a768d3*** | 命令执行ID。 |
| RequestId | String | E69EF3CC-94CD- 42E7-8926- F133B863**** | 请求ID。 |

**示例**

请求示例

```
&CommandId=c-e996287206324975b5fbe1d******** &InstanceId.1=i-bp185dy2o3o6n****** &RegionId=cn-qingdao-**** &Timed=true &Frequency=0 */20 * * * * &Parameters={"name":"Jack", "accessKey":"LTAIdyv******aRY"}
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>E69EF3CC-94CD-42E7-8926-F133B863****</RequestId>
      <InvokeId>t-7d2a745b412b4601b2d47f6a768d3***</InvokeId>
```

`JSON` 格式云服务器ECS

```json
{
    "RequestId": "E69EF3CC-94CD-42E7-8926-F133B863****",
    "InvokeId": "t-7d2a745b412b4601b2d47f6a768d3***"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 403 | InvalidInstance.Not Match | The specified instance type does not match the command. | 指定的实例ID不支持执行指定的命令 ID。请检查实例的状态是否符合云助手命令的执行条件。 |
| 403 | MissingParam.Frequ ency | The frequency must be specified when you create a timed task. | 创建定时任务时必须指定频率。 |
| 403 | InvalidParam.Freque ncy | The specified frequency is invalid. | 指定的 Frequency 参数无效。请检查参数值是否正确。 |
| 403 | InstanceIds.ExceedL imit | The number of instance IDs exceeds the upper limit. | 目标实例数量超过上限。 |
| 403 | Invocation.ExceedQ uota | The invocation quota in the current region has been reached for today. | 在当前地域命令执行次数已到达今天的额度。 |
| 403 | ParameterCount.Exc eedLimit | The maximum number of parameters is exceeded. | 参数数量超出最大可设置数量。 |
| 403 | ParameterKey.Exce edLimit | The maximum length of a parameter name is exceeded. | 指定的参数Key长度超过可设置的最大长度。 |
| 403 | CmdContent.Exceed Limit | The maximum length of a command is exceeded. | 您的命令内容过长，请精简您的命令内容。 |
| 403 | ParameterKey.Dupli cate | Parameter names cannot be duplicated. | 参数名称不能重复，请确认后重试。 |
| 403 | Parameter.NotMatch ed | The passed-in parameters do not match the parameters defined when you created the command. | 传入的自定义参数与创建命令时定义的自定义参数不匹配。 |
| 403 | Username.ExceedLi mit | The length of the username exceeds the upper limit. | 用户名长度超过上限。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 403 | Parameter.MissingV alue | The parameter value of this command is required. | 该命令的参数值是必填的。 |
| 404 | InvalidRepeatMode. NotFound | The specified repeat mode does not exist. | 指定的命令执行方式不存在。 |
| 404 | InvalidInstance.NotF ound | The specified instance does not exist. | 指定的实例不存在。 |

云服务器ECS

| 404 | InvalidCmdId.NotFo und | The specified command ID does not exist. | 指定的 CommandId 参数有误，请检查参数值是否正确。您可以通过接口 DescribeCommands 查询所有可用的 CommandId。 |
|---|---|---|---|
| 404 | Parameter.Disabled | Parameters cannot be passed in when the command customization function is disabled. | 当您禁用命令自定义参数功能时，请不要传递自定义参数。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### RunCommand

调用RunCommand在一台或多台ECS实例中执行一段Shell、PowerShell或者Bat类型的脚本。

**接口说明**

不同于通过CreateCommand和InvokeCommand执行命令，RunCommand只需一次调用即可完成命令的创建与执行。 调用该接口时，您需要注意： 目标实例的网络类型必须是专有网络VPC。 目标实例的状态必须为运行中（ `Running` ）。 目标实例必须预先安装云助手客户端（InstallCloudAssistant）。 执行类型为PowerShell的命令时，您需要确保目标ECS Windows实例已经配置了PowerShell模块。 周期执行的时间设置基准为UTC +0，且该时间以实例的系统时间为准。ECS实例的时间或者时区必须与您预期的时间一致。 您可以通过指定参数 `TimeOut` 为命令设置在ECS实例中执行时最大的超时时间，命令执行超时后，云助手客户端会强制终止进程。 单次执行超时后，命令的执行状态（InvokeRecordStatus）变为执行失败（Failed）。 周期执行的超时时间对每一次执行记录均有效，上次执行超时不影响下一次执行。某次执行超时后，执行状态（InvokeRecordStatus）变为执行失败（Failed）。 命令可能会因为目标实例的状态异常、网络异常或云助手客户端异常而出现无法执行的情况，无法执行时不会生成执行信息。

| EnableParameter=true |  |  |
|---|---|---|
| 过 | {{parameter}} | 的形式 |

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RunCommand | 系统规定参数。取值：RunCommand。 |

云服务器ECS

| CommandConten t | String | 是 | ZWNobyAxMjM= | 命令内容。命令内容可以是明文内容或 Base64编码后的内容。您需要注意： 若保存命令，命令内容在Base64编码后的大小不能超过18 KB；若不保存命令， 命令内容在Base64编码后的大小不能超过24 KB。您可通过 KeepCommand 设置是否保留命令。 如果您的命令内容是Base64编码后的内容，则必须设置 ContentEncoding=Base64 。 指定参数 EnableParameter=true 可在命令内容中启用自定义参数功能： 用 {{}} 包含的方式定义自定义参数，在 {{}} 内参数名前后的空格以及换行符会被忽略。 自定义参数个数不能超过20个。 自定义参数名允许 a~z 、 A~Z 、 0~9 、 - 的组合，不支持其余字符，参数名 _ 不区分大小写。 单个自定义参数名不能超过64字节。 |
|---|---|---|---|---|
| InstanceId.N | RepeatLi st | 是 | i- bp185dy2o3o6ne g**** | ECS实例ID列表。N的取值范围：1~50。 若指定了多台实例后，其中某台实例不满足执行条件时，您都需要重新选择。 |
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查询地域ID。 |
| Type | String | 是 | RunShellScript | 运维脚本的语言类型。取值范围： RunBatScript：适用于Windows实例的 Bat脚本。 RunPowerShellScript：适用于 Windows实例的PowerShell脚本。 RunShellScript：适用于Linux实例Shell 脚本 。 |
| Name | String | 否 | Test | 命令名称。支持全字符集，长度不得超过 128个字符。 |
| Description | String | 否 | RunCommand- Test | 命令描述。支持全字符集，长度不得超过 512个字符。 |

|  | a~z |
|---|---|
| _ |  |

云服务器ECS

| WorkingDir | String | 否 | /home/ | 命令在ECS实例中的运行目录。 默认值： Linux系统实例默认在管理员（root用户）的home目录下，即 /root 。 Windows系统实例默认在云助手客户端进程所在目录，例如 C:\Windows\System32 。 |
|---|---|---|---|---|
| Timeout | Long | 否 | 60 | 执行命令的超时时间，单位：秒。 当因为进程原因、缺失模块、缺失云助手客户端等原因无法运行命令时，会出现超时现象。超时后，会强制终止命令进程。 默认值：60。 |
| EnableParameter | Boolean | 否 | false | 创建的命令是否使用自定义参数。取值范围： true：是。 false：否。 默认值：false。 |

云服务器ECS

| RepeatMode | String | 否 | Once | 设置命令执行的方式。取值范围： Once：立即执行命令。 Period：定时执行命令。当该参数取值为 Period 时，必须同时指定 Timed=true 参数值以及 Frequency 参数。 NextRebootOnly：当实例下一次启动时，自动执行命令。 EveryReboot：实例每一次启动都将自动执行命令。 默认值： 当不指定 Timed=true 参数值以及 Frequency 参数时，默认值为 Once 。 当指定 Timed=true 参数值以及 Frequency 参数时，无论是否已设置了该参数值，都将按照 Period 处理。 注意事项： 当该参数取值 Period 、 NextRebootOnly 或者 EveryReboot 时，您可以调用 StopInvocation 停止待执行的命令或定时执行的命令。 当该参数取值 Period 或者 EveryReboot 时，您可以调用 DescribeInvocationResults ，然后指定 IncludeHistory=true 查看命令定时执行的历史记录。 |
|---|---|---|---|---|
| Timed | Boolean | 否 | true | 是否周期执行命令。取值范围： true：根据参数 Frequency 设置的时间频率定时执行。上次的执行结果不对下一次执行产生任何影响。 false：只执行一次。 默认值为false。 |
| Frequency | String | 否 | 0 */20 * * * * | 周期执行命令的执行周期。 您需要注意： 两次周期执行的命令时间间隔不能低于10 秒，且周期命令最小执行间隔不能小于任务执行超时时间。其中任务执行超时时间请参见您在调用本API时设置的 Timeout 参数。 当参数 Timed 的值为 true 时，该参数为必选参数。 该参数取值遵循Cron表达式，更多信息， 请参见云服务器ECS用户指南中的Cron表达式章节。 |

|  | Timed=true |
|---|---|
| Frequency |  |
| Once |  |

|  | Period |
|---|---|
| EveryReboot |  |

云服务器ECS

| Parameters | Json | 否 | {"name":"Jack", "accessKey":"LTA IdyvdIqaRY****"} | 命令中包含自定义参数时，执行命令时传入的自定义参数的键值对。例如，命令内容为 echo {{name}} ，则可以通过 Parameter 参数传入键值对 {"name":"Jack"} 。自定义参数将自动替换变量值 name ，得到一条新的命令，实际执行的是 echo Jack 。 自定义参数的个数范围为0~10，且您需要注意： 键不允许为空字符串，最多支持64个字符。 值允许为空字符串。 自定义参数与原始命令内容在Base64编码后，若保存命令，命令内容在Base64 编码后的大小不能超过18 KB；若不保存命令，命令内容在Base64编码后的大小不能超过24 KB。您可通过 KeepCommand 设置是否保留命令。 设置的自定义参数名集合必须为创建命令时定义的参数集的子集。对于未传入的参数，您可以使用空字符串代替。 默认值：空，表示取消设置该参数从而禁用自定义参数。 |
|---|---|---|---|---|
| KeepCommand | Boolean | 否 | false | 执行完该命令后，是否保留下来。取值范围： true：保留。可以通过InvokeCommand 再次执行。会占用云助手命令的保有量配额。 false：不保留。执行完成后自动删除，不占用云助手命令的保有量配额。 默认值为false。 |
| ContentEncoding | String | 否 | Base64 | 命令内容（ CommandContent ）的编码方式。取值范围（不区分大小写）： PlainText：不编码，采用明文传输。 Base64：Base64编码。 默认值：PlainText，乱填或错填该取值会当作PlainText处理。 |
| Username | String | 否 | root | 在ECS实例中执行命令的用户名称。 说明该参数仅支持Linux系统的ECS实例，默认以root用户执行命令。 |

**返回数据**

云服务器ECS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CommandId | String | c- 7d2a745b412b4601 b2d47f6a768d**** | 脚本ID。 |
| InvokeId | String | t- 7d2a745b412b4601 b2d47f6a768d**** | 脚本执行ID。 |
| RequestId | String | E69EF3CC-94CD- 42E7-8926- F133B863**** | 请求ID。 |

**示例**

请求示例

```
&CommandContent='echo hello' &InstanceId.1=i-bp185dy2o3o6neg**** &InstanceId.2=i-bp541dc26ko6dd5**** &Name=Test &RegionId=cn-qingdao-**** &Type=RunShellScript &Username=root
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <RequestId>E69EF3CC-94CD-42E7-8926-F133B86387C0</RequestId>
        <CommandId>c-7d2a745b412b4601b2d47f6a768d****</CommandId>
        <InvokeId>t-7d2a745b412b4601b2d47f6a768d****</InvokeId>
```

`JSON` 格式

```json
{
    "RequestId": "E69EF3CC-94CD-42E7-8926-F133B863****",
    "CommandId": "c-7d2a745b412b4601b2d47f6a768d****",
    "InvokeId": "t-7d2a745b412b4601b2d47f6a768d****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 400 | NumberExceed.Tags | The Tags parameter number is exceed , Valid : 20 | 标签个数超过最大限制，本操作最多可以操作 20 个标签。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |

云服务器ECS

| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
|---|---|---|---|
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | MissingParameter.T agKey | You must specify Tag.N.Key. | 请指定标签键。 |
| 403 | InvalidCmdType.Not Found | The specified command type does not exist. | 指定的命令类型不存在。 |
| 403 | CmdContent.Exceed Limit | The length of the command content exceeds the upper limit. | 命令内容长度超过上限。 |
| 403 | CmdName.ExceedLi mit | The length of the command name exceeds the upper limit. | 命令名称长度超过上限。 |
| 403 | CmdDesc.ExceedLi mit | The length of the command description exceeds the upper limit. | 命令描述长度超过上限。 |
| 403 | CmdCount.ExceedQ uota | The total number of commands in the current region exceeds the quota. | 当前地域下的云助手命令数量已超出限。 |
| 403 | CmdParam.EmptyKe y | Command parameters can not be empty. | 命令中自定义参数不能为空。 |
| 403 | CmdParam.InvalidPa ramName | A command parameter name is invalid. | 命令中自定义参数名称不合法。 |
| 403 | InvalidInstance.Not Match | The specified instance type does not match the command. | 指定的实例ID不支持执行指定的命令 ID。请检查实例的状态是否符合云助手命令的执行条件。 |
| 403 | MissingParam.Frequ ency | The frequency must be specified when you create a timed task. | 创建定时任务时必须指定频率。 |
| 403 | InvalidParam.Freque ncy | The specified frequency is invalid. | 指定的 Frequency 参数无效。请检查参数值是否正确。 |
| 403 | InstanceIds.ExceedL imit | The number of instance IDs exceeds the upper limit. | 目标实例数量超过上限。 |
| 403 | Invocation.ExceedQ uota | The invocation quota in the current region has been reached for today. | 在当前地域命令执行次数已到达今天的额度。 |
| 403 | Username.ExceedLi mit | The length of the username exceeds the upper limit. | 用户名长度超过上限。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 404 | InvalidRepeatMode. NotFound | The specified repeat mode does not exist. | 指定的命令执行方式不存在。 |
| 404 | InvalidInstance.NotF ound | The specified instance does not exist. | 指定的实例不存在。 |
| 404 | InvalidCmdId.NotFo und | The specified command ID does not exist. | 指定的 CommandId 参数有误，请检查参数值是否正确。您可以通过接口 DescribeCommands 查询所有可用的 CommandId。 |

云服务器ECS

| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |
|---|---|---|---|

##### DescribeCommands

调用DescribeCommands查询您已经创建的云助手命令。只输入参数Action和RegionId，不输入其他任何请求参数，则默认查询您所有可用的命令（CommandId）。

**请求参数**

| 名称 | 类型 | 是否必选 |  | 示例值 | 描述 |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Action | String | 是 |  | DescribeComman ds | 系统规定参数，取值： DescribeCommands。 |  |  |  |
| RegionId | String | 是 |  | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查询地域ID。 |  |  |  |
| Provider | String | 否 |  | AlibabaCloud | 公共命令的提供者。参数值的具体说明如下： 当该参数不传值时，默认查询您手动创建的所有云助手命令。 当该参数取值为 AlibabaCloud 时， 查询由阿里云提供的所有公共命令。 当该参数的取值为具体的公共命令提供者时，查询该提供者提供的所有公共命令。 例如： 当 Provider=AlibabaCloud.ECS.G uestOS 时，查询 AlibabaCloud.ECS.GuestOS 提供的公共命令。 当 Provider=AlibabaCloud.ECS.G uestOSDiagnose 时，查询 AlibabaCloud.ECS.GuestOSDia gnose 提供的公共命令。 |  |  |  |
|  |  |  |  |  |  | Provider=AlibabaCloud.ECS.G |  |  |
|  |  |  |  |  | uestOS |  |  |  |
|  |  |  |  |  |  | Provider=AlibabaCloud.ECS.G |  |  |
|  |  |  |  |  | uestOSDiagnose |  |  |  |
|  |  |  |  |  |  |  | 时，查 |  |
|  |  |  |  |  | 询 |  |  |  |
|  |  |  |  |  | gnose |  |  |  |
| CommandId | String | 否 |  | c- 7d2a745b412b46 01b2d47f6a768d **** | 命令ID。 |  |  |  |
| Name | String | 否 |  | Tes**** | 命令的名称，暂不支持模糊查询。 |  |  |  |
| Description | String | 否 |  | test | 命令描述。 |  |  |  |

云服务器ECS

| Type | String | 否 | RunShellScript | 命令的类型。取值范围： RunBatScript：命令为在Windows实例中运行的Bat脚本。 RunPowerShellScript：命令为在 Windows实例中运行的PowerShell脚本。 RunShellScript：命令为在Linux实例中运行的Shell脚本。 |
|---|---|---|---|---|
| ContentEncoding | String | 否 | PlainText | 设置返回数据中 CommandContent 字段和 Output 字段的编码方式。取值范围： PlainText：返回原始脚本内容和输出信息。 Base64：返回Base64编码后的脚本内容和输出信息。 默认值：Base64。 |
| PageNumber | Long | 否 | 1 | 当前页码，起始值：1。 默认值：1。 |
| PageSize | Long | 否 | 10 | 分页查询时设置的每页行数，最大值：50。 默认值：10。 |
| Latest | Boolean | 否 | true | 若查询结果包含公共命令，是否只查询最新版本的公共命令。该参数不影响私有命令的查询。 true：只查询最新版本的公共命令。 false：查询所有版本的公共命令。 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Commands | Array of Command |  | 命令数据集类型 。 |
| Command |  |  |  |
| Category | String | “” | 公共命令的类目。 |
| CommandCont ent | String | Y2QgL3Jvb3Q= | 命令内容，以Base64编码后传输。 |
| CommandId | String | c- 7d2a745b412b4601 b2d47f6a768d3*** | 命令ID。 |
| CreationTime | String | 2018-01- 05T15:45:02Z | 命令创建时间。 |

云服务器ECS

| Description | String | test | 命令描述。 |
|---|---|---|---|
| EnableParamet er | Boolean | true | 该命令是否启用自定义参数。 |
| InvokeTimes | Integer | 1 | 使用该命令创建的任务数。 |
| Latest | Boolean | true | 公共命令是否是最新版本。如果多个命令属于同一个 Provider ，且名称与类目相同，则这些命令属于同一个命令的不同版本。您手动创建的云助手命令不会返回该值。可能值： true：是。 false：否。 |
| Name | String | Test1 | 命令名称。 |
| ParameterDefin itions | Array of ParameterDefin ition |  | 自定义参数详细信息列表。 |
| ParameterDefin ition |  |  |  |
| DefaultValue | String | https://aliyun-client- assist.oss- accelerate.aliyuncs. com/linux/aliyun as _ sist latest.rpm _ | 自定义参数的默认值。 |
| Description | String | 云助手客户端安装包路径 | 自定义参数描述。 |
| ParameterNam e | String | DownloadUrl | 自定义参数名称。 |
| PossibleValues | List | "Linux","Windows" | 枚举类型自定义参数的可选值。 |
| Required | Boolean | true | 该自定义参数是否必填。 true：是。 false：否。 默认值：false。 |
| ParameterNam es | List | ['parameter1','para meter2'] | 通过创建命令时的CommandContent解析出的自定义参数名列表，以列表（List）的形式返回。如未使用自定义参数功能，则返回空值列表。 |
| Provider | String | AlibabaCloud.ECS.G uestOS | 公共命令的提供者。 |
| Tags | Array of Tag |  | 说明该参数未开放使用。 |
| Tag |  |  |  |

云服务器ECS

| TagKey | String | owner | 说明该参数未开放使用。 |
|---|---|---|---|
| TagValue | String | zhangsan | 说明该参数未开放使用。 |
| Timeout | Long | 3600 | 超时时间。 |
| Type | String | RunShellScript | 命令类型。 |
| Version | Integer | 1 | 公共命令的版本。如果多个命令属于同一个 Provider ，且名称与类目相同，则这些命令属于同一个命令的不同版本。您手动创建的云助手命令不会返回该值。 |
| WorkingDir | String | /home/ | 执行路径。 |
| PageNumber | Long | 1 | 命令列表页码。 |
| PageSize | Long | 10 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |
| TotalCount | Long | 5 | 命令总个数。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeCommands &RegionId=cn-qingdao-**** &PageNumber=1 &PageSize=10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
  <TotalCount>5</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
  <PageNumber>1</PageNumber>
  <Commands>
        <Description>test</Description>
        <Category>“”</Category>
        <Timeout>3600</Timeout>
        <Provider>AlibabaCloud.ECS.GuestOS</Provider>
        <Name>Test1</Name>
        <WorkingDir>/home/</WorkingDir>
        <CommandContent>Y2QgL3Jvb3Q=</CommandContent>
        <Type>RunShellScript</Type>
        <Version>1</Version>
        <InvokeTimes>1</InvokeTimes>
        <CreationTime>2018-01-05T15:45:02Z</CreationTime>
        <EnableParameter>true</EnableParameter>
        <Latest>true</Latest>
        <CommandId>c-7d2a745b412b4601b2d47f6a768d3***</CommandId>
        <ParameterNames>['parameter1','parameter2']</ParameterNames>
                <ParameterDefinitions>
                  <Required>true</Required>
```

`<Description>`云助手客户端安装包路径`</Description>`

```xml
                  <DefaultValue>https://aliyun-client-assist.oss-
accelerate.aliyuncs.com/linux/aliyun_assist_latest.rpm</DefaultValue>
                  <ParameterName>DownloadUrl</ParameterName>
                  <PossibleValues>"Linux","Windows"</PossibleValues>
        </ParameterDefinitions>
  </Commands>
```

`JSON` 格式云服务器ECS

```json
{
    "TotalCount": 5,
    "PageSize": 10,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
    "PageNumber": 1,
    "Commands": {
        "Description": "test",
        "Category": "“”",
        "Timeout": 3600,
        "Provider": "AlibabaCloud.ECS.GuestOS",
        "Name": "Test1",
        "WorkingDir": "/home/",
        "CommandContent": "Y2QgL3Jvb3Q=",
        "Type": "RunShellScript",
        "Version": 1,
        "InvokeTimes": 1,
        "CreationTime": "2018-01-05T15:45:02Z",
        "EnableParameter": true,
        "Latest": true,
        "CommandId": "c-7d2a745b412b4601b2d47f6a768d3***",
        "ParameterNames": "['parameter1','parameter2']",
            "ParameterDefinitions": [
                {
                    "Required": true,
```

`"Description": "`云助手客户端安装包路径`",`

```json
                    "DefaultValue": "https://aliyun-client-assist.oss-
accelerate.aliyuncs.com/linux/aliyun_assist_latest.rpm",
                    "ParameterName": "DownloadUrl",
                    "PossibleValues": [
                        "\"Linux\",\"Windows\""
```

]

```
                }
```

]

```
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 400 | NumberExceed.Tags | The Tags parameter number is exceed , Valid : 20 | 标签个数超过最大限制，本操作最多可以操作 20 个标签。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 400 | MissingParameter.T agKey | You must specify Tag.N.Key. | 请指定标签键。 |

云服务器ECS

| 403 | InvalidParam.PageN umber | The specified parameter is invalid. | 指定的 PageNumber 参数无效。 |
|---|---|---|---|
| 403 | InvalidParam.PageSi ze | The specified parameter is invalid. | 指定的 PageSize 参数无效。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### ModifyCommand

修改一条云助手命令相关参数以及命令内容。

**接口说明**

命令执行期间也允许修改，修改命令后，后续执行会按照新的命令内容执行。 您不能修改命令的类型，例如，如果命令是Shell命令（RunShellScript），则不能修改为Bat命令 （RunBatScript）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyCommand | 系统规定参数。取值：ModifyCommand。 |
| CommandId | String | 是 | c- 4d34302d02424c 5c8e10281e3a31 5*** | 命令ID。您可以通过接口 DescribeCommands查询所有可用的 CommandId。 |
| RegionId | String | 是 | cn-qingdao-***** | 地域ID。您可以调用DescribeRegions查看地域ID。 |
| Name | String | 否 | AlibabaCommand | 命令名称。支持全字符集，长度不得超过 128个字符。 |
| Description | String | 否 | UserGuide | 命令描述。支持全字符集，长度不得超过 512个字符。 |

云服务器ECS

| CommandConten t | String | 否 | c2VydmljZSB0b2 1jYXQgc3RhcnQ= | 命令内容。命令内容可以是明文内容或 Base64编码后的内容。您需要注意： 命令内容在Base64编码后的大小不能超过16 KB。 如果您的命令内容是Base64编码后的内容，则必须设置 ContentEncoding=Base64 。 指定参数 EnableParameter=true 可在命令内容中启用自定义参数功能： 用 {{}} 包含的方式定义自定义参数，在 {{}} 内参数名前后的空格以及换行符会被忽略。 自定义参数个数不能超过20个。 自定义参数名允许 a-z 、 A- Z 、 0-9 、 - 的组合，不支持 _ 其余字符，参数名不区分大小写。 单个自定义参数名不能超过64字节。 |
|---|---|---|---|---|
| WorkingDir | String | 否 | /home/ | 执行路径。 |
| Timeout | Long | 否 | 60 | 您创建的命令在ECS实例中执行时最大的超时时间，单位：秒。当无法在配置的时间内运行并完成您创建的命令时，会出现超时现象。超时后，会强制终止命令进程，即取消命令的PID。 |

|  | a-z |
|---|---|
| - _ |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0DE9B41E-EF0D- 40A0-BB43- 37749C5B**** | 请求ID。 |

**示例**

请求示例

```
&CommandId=c-4d34302d02424c5c8e10281e3a315*** &RegionId=cn-qingdao-**** &Name=AlibabaCommand &Description=UserGuide &CommandContent=c2VydmljZSB0b21jYXQgc3RhcnQ= &WorkingDir=/home/ &Timeout=60
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```json
    "RequestId": "0DE9B41E-EF0D-40A0-BB43-37749C5B****"
```

`JSON` 格式

```json
{
    "RequestId": "0DE9B41E-EF0D-40A0-BB43-37749C5B****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 403 | CmdName.Readonly | The command name is readonly after publishing. | 命令已经发布，禁止修改。 |
| 403 | CmdName.ExceedLi mit | The length of the command name exceeds the upper limit. | 命令名称长度超过上限。 |
| 403 | CmdContent.Exceed Limit | The length of the command content exceeds the upper limit. | 命令内容长度超过上限。 |
| 403 | CmdDesc.ExceedLi mit | The length of the command description exceeds the upperlimit. | 命令描述长度超过上限。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 404 | InvalidCmdId.NotFo und | The specified command ID does not exist. | 指定的 CommandId 参数有误，请检查参数值是否正确。您可以通过接口 DescribeCommands 查询所有可用的 CommandId。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### StopInvocation

调用StopInvocation停止一台或多台ECS实例中一条正在进行中（Running）的云助手命令进程。

**接口说明**

停止单次命令进程后，已经开始执行的实例会继续执行，未开始执行的实例将不再执行。 停止周期命令进程后，已经开始执行的命令将继续执行，但后续将不会再进行下一次的执行。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StopInvocation | 系统规定参数。取值：StopInvocation。 |

云服务器ECS

| InvokeId | String | 是 | t- 7d2a745b412b46 01b2d47f6a768d 3*** | 命令进程执行ID。您可以通过接口 DescribeInvocations查询所有的 InvokeId。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查询地域ID。 |
| InstanceId.N | RepeatLi st | 否 | i- bp67acfmxazb4p h*** | 要停止执行命令的实例列表，最多能指定20 台实例ID。N的取值范围为1~50。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&InvokeId=t-7d2a745b412b4601b2d47f6a768d3*** &RegionId=cn-qingdao-****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式

```json
{
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |
| 404 | InvalidInvokeId.NotF ound | The specified invoke ID does not exist. | 指定的参数InvokeId不存在，请确认该参数是否正确。 |

云服务器ECS

##### DescribeInvocationResults

调用DescribeInvocationResults查看一条或多条云助手命令的执行结果，即在ECS实例中的实际执行结果。

**接口说明**

当您执行命令后，不代表命令一定成功运行，并且一定有预期的命令效果。您需要通过本接口查看实际的具体执行结果，以实际输出结果为准。 您可以查询最近2周的执行信息，执行信息的保留上限为10万条。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInvocatio nResults | 系统规定参数。取值： DescribeInvocationResults。 |
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查询地域ID。 |
| InvokeId | String | 否 | t- 7d2a745b412b46 01b2d47f6a768d **** | 命令执行ID。命令进程执行ID。您可以通过接口DescribeInvocations查询InvokeId。 |
| InstanceId | String | 否 | i- bp10ua7jvif75ha 8**** | 实例ID。 |
| CommandId | String | 否 | c- 4d34302d02424c 5c8e10281e3a31 **** | 命令ID。 |
| InvokeRecordStat us | String | 否 | Finished | 命令执行状态。取值范围： Running：运行中。 Finished：已完成。 Failed：失败。 Stopped：已停止。 |
| IncludeHistory | Boolean | 否 | false | 是否返回周期性任务的历史记录。取值范围： true ：表示返回周期性任务的执行结果。 当取值为true时，参数 InvokeId 的取值不能为空，且必须为周期性任务的执行ID。 false ：表示不返回。 默认值：false。 |

云服务器ECS

| ContentEncoding | String | 否 | PlainText | 设置返回数据中 Output 字段的编码方式，取值范围： PlainText：返回原始脚本内容和输出信息。 Base64：返回Base64编码后的脚本内容和输出信息。 默认值：Base64。 |
|---|---|---|---|---|
| PageNumber | Long | 否 | 1 | 当前页码。 起始值：1。 默认值：1。 |
| PageSize | Long | 否 | 10 | 分页查询时设置的每页行数。 最大值：50。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Invocation | Struct |  | 命令执行结果的集合。 |
| InvocationResul ts | Array of InvocationResul t |  | 命令执行结果集合。 |
| InvocationResul t |  |  |  |
| CommandId | String | c- 4d34302d02424c5c 8e10281e3a31**** | 命令ID。 |
| Dropped | Integer | 0 | Output 字段中文字长度超出24 KB后，截断并丢弃的文字长度。 |

云服务器ECS

| ErrorCode | String | InstanceNotExists | 命令的下发失败或执行失败原因的代码，可能值： 空：命令运行正常。 InstanceNotExists：指定的实例不存在或已释放。 InstanceReleased：执行任务期间，该实例被释放。 InstanceNotRunning：创建任务时，该实例不在运行中。 CommandNotApplicable：命令不适用于指定的实例。 AccountNotExists：指定的阿里云账号不存在。 DirectoryNotExists：指定的目录不存在。 BadCronExpression：指定的周期表达式不合法。 ClientNotRunning：云助手客户端未运行。 ClientNotResponse：云助手客户端无响应。 ClientIsUpgrading：云助手客户端正在升级中。 ClientNeedUpgrade：云助手客户端需要升级。 DeliveryTimeout：发送命令超时。 ExecutionTimeout：命令运行超时。 ExecutionException：命令运行发生异常。 ExecutionInterrupted：命令运行任务中断。 ExitCodeNonzero：命令执行结束，退出码非 0。 |
|---|---|---|---|

云服务器ECS

| ErrorInfo | String | the specified instance does not exists | 命令的下发失败或执行失败原因的详情，可能值： 空：命令运行正常。 the specified instance does not exists：指定的实例不存在或已释放。 the instance has released when create task：执行任务期间，该实例被释放。 the instance is not running when create task：创建任务时，该实例不在运行中。 the command is not applicable：命令不适用于指定的实例。 the specified account does not exists：指定的阿里云账号不存在。 the specified directory does not exists：指定的目录不存在。 the cron job expression is invalid：指定的周期表达式不合法。 the aliyun service is not running on the instance：云助手客户端未运行。 the aliyun service in the instance does not response：云助手客户端无响应。 the aliyun service in the instance is upgrading now：云助手客户端正在升级中。 the aliyun service in the instance need upgrade：云助手客户端需要升级。 the command delivery has been timeout： 发送命令超时。 the command execution has been timeout：命令运行超时。 the command execution got an exception：命令运行发生异常。 the command execution has been interrupted：命令运行任务中断。 the command execution exit code is not zero：命令执行结束，退出码非0。 |
|---|---|---|---|
| ExitCode | Long | 0 | 命令进程的退出码。 Linux实例为Shell进程的退出码。 Windows实例为Bat或者PowerShell进程的退出码。 |
| FinishedTime | String | 2018-01-05 15:45:02 | 命令进程的完成时间。如果命令进程出现超时情况，命令进程的完成时间以CreateCommand中指定的参数TimedOut为准。 |
| InstanceId | String | i-uf614fhehhzm**** | 实例ID。 |

云服务器ECS

| InvocationStatu s | String | Success | 单台实例的脚本进度状态，可能值： Pending：系统正在校验或发送命令。 Invalid：指定命令类型或参数有误。 Aborted：向实例发送命令失败。实例必须在运行中，且命令可以1分钟内发送完成。 Running：命令正在实例上运行。 Success： 立即运行的任务：命令执行完成，且退出码为 0。 周期运行的任务：上一次运行成功且退出码为 0，且指定的周期已结束。 Failed： 立即运行的任务：命令执行完成，且退出码非 0。 周期运行的任务：上一次运行成功且退出码非 0，且指定的周期将中止。 Error：命令执行时发生异常无法继续。 Timeout：命令执行超时。 Cancelled：任务已经取消，命令未曾启动。 Stopping：正在停止任务。 Terminated：命令运行时被终止。 Scheduled： 立即运行的任务：不适用，不会出现。 周期运行的任务：等待运行。 |
|---|---|---|---|
| InvokeId | String | t- 7d2a745b412b4601 b2d47f6a768d**** | 命令执行ID。 |
| InvokeRecordSt atus | String | Finished | 命令执行状态。 |
| Output | String | MTU6MzA6MDEK | 命令进程完成后的实际结果，输出内容以Base64 编码的形式传输。 |
| Repeats | Integer | 0 | 命令在该实例上执行的次数。 若执行方式为立即执行，则值为0或1。 若执行方式为周期执行，则值为执行过多少次。 |
| StartTime | String | 2022-04- 01T02:36:20Z | 开始执行的时间。 |
| StopTime | String | 2022-04- 01T09:15:47Z | 若调用了 StopInvocation ，则表示调用的时间。 |
| Tags | Array of Tag |  | 说明该参数未开放使用。 |
| Tag |  |  |  |

云服务器ECS

| TagKey | String | owner | 说明该参数未开放使用。 |
|---|---|---|---|
| TagValue | String | zhangsan | 说明该参数未开放使用。 |
| Username | String | root | 在ECS实例中执行命令的用户名称。 说明该参数仅支持Linux系统的ECS 实例，默认以root用户执行命令。 |
| PageNumber | Long | 1 | 当前页码。 |
| PageSize | Long | 1 | 分页查询时设置的每页行数。 |
| TotalCount | Long | 1 | 命令总个数。 |
| RequestId | String | 919C8FD6-0BC1- 4259-A6EA- 5B40036***** | 请求ID。 |

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeInvocationResults &RegionId=cn-qingdao-env17-d01 &InstanceId=i-bp10ua7jvif75ha8**** &PageNumber=1 &PageSize=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <RequestId>919C8FD6-0BC1-4259-A6EA-5B40036*****</RequestId>
      <Invocation>
            <PageNumber>1</PageNumber>
            <TotalCount>1</TotalCount>
            <InvocationResults>
                  <InvocationResult>
                        <InvokeRecordStatus>Running</InvokeRecordStatus>
                        <FinishedTime></FinishedTime>
                        <InstanceId>i-bp10ua7jvif75ha8****</InstanceId>
                        <Output>MTU6NDU6MDEK</Output>
                        <ExitCode>0</ExitCode>
                        <InvokeId>t-c6d11006a9374619838af10a2b09****</InvokeId>
                        <StartTime>2018-08-01T02:36:20Z</StartTime>
                        <CommandId>c-1791e8b850f44949aba6c883ad3****</CommandId>
                  </InvocationResult>
            </InvocationResults>
            <PageSize>1</PageSize>
      </Invocation>
```

`JSON` 格式

```json
{
 "RequestId": "919C8FD6-0BC1-4259-A6EA-5B40036*****",
 "Invocation": {
  "PageNumber": 1,
  "TotalCount": 1,
  "InvocationResults": {
   "InvocationResult": [
    {
     "InvokeRecordStatus": "Running",
     "FinishedTime": "",
     "InstanceId": "i-bp10ua7jvif75ha8****",
     "Output": "MTU6NDU6MDEK",
                    "ExitCode": 0,
     "InvokeId": "t-c6d11006a9374619838af10a2b09****",
     "StartTime": "2018-08-01T02:36:20Z",
     "CommandId": "c-1791e8b850f44949aba6c883ad3e****"
    }
```

]

```json
  },
  "PageSize": 1
 }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 400 | NumberExceed.Tags | The Tags parameter number is exceed , Valid : 20 | 标签个数超过最大限制，本操作最多可以操作 20 个标签。 |

云服务器ECS

| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
|---|---|---|---|
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 400 | MissingParameter.T agKey | You must specify Tag.N.Key. | 请指定标签键。 |
| 403 | InvalidParam.PageN umber | The specified parameter is invalid. | 指定的 PageNumber 参数无效。 |
| 403 | InvalidParam.PageSi ze | The specified parameter is invalid. | 指定的 PageSize 参数无效。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### DescribeInvocations

**接口说明**

当您执行命令后，不代表命令一定成功运行，并且一定有预期的命令效果。您需要通过接口返回值查看实际执行结果，以实际输出结果为准。 您可以查询最近2周的执行信息，执行信息的保留上限为10万条。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInvocatio ns | 系统规定参数。取值： DescribeInvocations。 |
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查询地域ID。 |
| InvokeId | String | 否 | t- 7d2a745b412b46 01b2d47f6a76d2 **** | 命令执行ID。 |
| CommandId | String | 否 | c- 4d34302d02424c 5c8e10281e3ad2 **** | 命令ID。您可以通过接口 DescribeCommands查询所有可用的 CommandId。 |
| CommandName | String | 否 | test- CommandName | 命令名称。 |
| CommandType | String | 否 | RunShellScript | 命令类型。 |

云服务器ECS

| Timed | Boolean | 否 | true | 查询的命令是否在将来会自动执行。取值范围： true：查询在调用 RunCommand 或 InvokeCommand 执行命令时， RepeatMod 参数取值为 Period 、 NextRebootOny 或者 EveryReboot ，且处于未被取消的未完成状态命令或者未被停止的未完成状态命令。 false：查询以下两种状态的命令： 在调用 RunCommand 或 InvokeComma nd 执行命令时， RepeatMode 参数取值为 Once 。 已被取消、被停止或者已完成执行的命令。 默认值：false。 |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | InvokeComma |  |
|  |  |  |  |  | RepeatMode |  |  |
| InvokeStatus | String | 否 | Finished | 命令执行的总执行状态。总执行状态取决于创建执行中的一台或多台实例的共同执行状态。取值范围： Running： 周期执行：未手动停止周期执行命令前，执行状态一直为进行中。 单次执行：一旦有进行中的命令进程， 总的执行状态就为进行中。 Finished： 周期执行：命令进程不可能为执行完成。 单次执行：所有实例全部完成执行。或者手动停止部分实例的命令进程，其余实例全部执行完成。 Failed： 周期执行：命令进程不可能为执行失败。 单次执行：所有实例全部执行失败。 PartialFailed： 周期执行：命令进程不可能为部分失败。 单次执行：部分实例有执行失败的命令进程，则总执行状态为部分失败。 Stopped：停止命令。 默认值：Running。 |  |  |  |
| InstanceId | String | 否 | i- bp10jvkun5h1ifzq **** | 实例ID。当您传入了该参数，将查询该实例所有的命令执行记录。 |  |  |  |

|  |  | RunCommand |
|---|---|---|
|  | nd |  |

云服务器ECS

| ContentEncoding | String | 否 | PlainText | 设置返回数据中 CommandContent 字段和 Output 字段的编码方式。取值范围： PlainText：返回原始命令内容和输出信息。 Base64：返回Base64编码后的命令内容和输出信息。 默认值：Base64。 |
|---|---|---|---|---|
| IncludeOutput | Boolean | 否 | false | 是否在结果中返回命令运行的输出信息。 true：返回。此时，您至少指定参数 InvokeId 或 InstanceId 。 false：不返回。 默认值：false。 |
| PageNumber | Long | 否 | 1 | 当前页码。 起始值：1。 默认值：1。 |
| PageSize | Long | 否 | 10 | 分页查询时设置的每页行数。 最大值：50。 默认值：10。 |
| RepeatMode | String | 否 | Once | 命令执行的方式。取值范围： Once：立即执行命令。 Period：定时执行命令。 NextRebootOnly：当实例下一次启动时，自动执行命令。 EveryReboot：实例每一次启动都将自动执行命令。 默认值为空，表示查询全部。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Invocations | Array of Invocation |  | 命令执行记录组成的数组。 |
| Invocation |  |  |  |
| CommandCont ent | String | ZWNobyAiaGVsbG8 gd29ybGQiID4vcm9 vdC90ZXN0******= = | 命令内容，以Base64编码后传输。 |
| CommandDesc ription | String | testDescription | 命令描述。 |

云服务器ECS

| CommandId | String | c- 4d34302d02424c5c 8e10281e3ad2**** | 命令ID。 |
|---|---|---|---|
| CommandNam e | String | test-CommandName | 命令名称。 |
| CommandType | String | RunShellScript | 命令类型。 |
| CreationTime | String | 2020-01- 19T09:15:46Z | 任务的创建时间。 |
| Frequency | String | 0 */20 * * * * | 周期任务的执行周期。该参数值结构以Cron表达式为准。 |

云服务器ECS

| InvocationStatu s | String | Pending | 命令执行的总执行状态，总执行状态取决于本次调用的全部实例的共同执行状态，可能值： Pending：系统正在校验或发送命令。存在至少一台实例的命令执行状态为Pending，则总执行状态为Pending。 Scheduled：周期执行的命令已发送，等待运行。存在至少一台实例的命令执行状态为 Scheduled，则总执行状态为Scheduled。 Running：命令正在实例上运行。存在至少一台实例的命令执行状态为Running，则总执行状态为Running。 Success：各个实例上的命令执行状态均为 Stopped或Success，且至少一个实例的命令执行状态是Success，则总执行状态为Success。 立即运行的任务：命令执行完成，且退出码为 0。 周期运行的任务：最近一次执行成功且退出码为0，且指定的周期已全部完成。 Failed：各个实例上的命令执行状态均为 Stopped或Failed，则总执行状态为Failed。实例上的命令执行状态一项或多项为以下状态时， 返回值均为Failed状态： 命令校验失败（Invalid） 命令发送失败（Aborted） 命令执行完成但退出码非0（Failed） 命令执行超时（Timeout） 命令执行异常（Error） Stopping：正在停止任务。存在至少一台实例的命令执行状态为Stopping，则总执行状态为 Stopping。 Stopped：任务已停止。所有实例的命令执行状态是Stopped，则总执行状态为Stopped。实例上的命令执行状态为以下状态时，返回值均为 Stopped状态： 任务已取消（Cancelled） 任务已终止（Terminated） PartialFailed：部分实例执行成功且部分实例执行失败。各个实例的命令执行状态均为 Success、Failed或Stopped，则总执行状态为 PartialFailed。 说明返回参数中的 InvokeStatus 与该参数意义相似， 但建议您查看该返回值。 |
|---|---|---|---|
| InvokeId | String | t- 7d2a745b412b4601 b2d47f6a76d2**** | 命令执行ID。 |
| InvokeInstance s | Array of InvokeInstance |  | 执行目标实例集类型。 |
| InvokeInstance |  |  |  |

云服务器ECS

| CreationTime | String | 2019-12- 20T06:15:54Z | 命令执行的开始时间。 |
|---|---|---|---|
| Dropped | Integer | 0 | Output字段中文字长度超出24 KB后，截断丢弃的文字长度。 |
| ErrorCode | String | InstanceNotExists | 命令的下发失败或执行失败原因的代码，可能值： 空：命令运行正常。 InstanceNotExists：指定的实例不存在或已释放。 InstanceReleased：执行命令期间，该实例被释放。 InstanceNotRunning：开始执行命令时，该实例不在运行中。 CommandNotApplicable：命令不适用于指定的实例。 AccountNotExists：指定的账号不存在。 DirectoryNotExists：指定的目录不存在。 BadCronExpression：指定的周期表达式不合法。 ClientNotRunning：云助手客户端未运行。 ClientNotResponse：云助手客户端无响应。 ClientIsUpgrading：云助手客户端正在升级中。 ClientNeedUpgrade：云助手客户端需要升级。 DeliveryTimeout：发送命令超时。 ExecutionTimeout：命令执行超时。 ExecutionException：命令执行发生异常。 ExecutionInterrupted：命令执行任务中断。 ExitCodeNonzero：命令执行结束，退出码非 0。 |

云服务器ECS

| ErrorInfo | String | the specified instance does not exists | 命令的下发失败或执行失败原因的详情，可能值： 空：命令运行正常。 the specified instance does not exists：指定的实例不存在或已释放。 the instance has released when create task：执行命令期间，该实例被释放。 the instance is not running when create task：开始执行命令时，该实例不在运行中。 the command is not applicable：命令不适用于指定的实例。 the specified account does not exists：指定的账号不存在。 the specified directory does not exists：指定的目录不存在。 the cron job expression is invalid：指定的周期表达式不合法。 the aliyun service is not running on the instance：云助手客户端未运行。 the aliyun service in the instance does not response：云助手客户端无响应。 the aliyun service in the instance is upgrading now：云助手客户端正在升级中。 the aliyun service in the instance need upgrade：云助手客户端需要升级。 the command delivery has been timeout： 发送命令超时。 the command execution has been timeout：命令执行超时。 the command execution got an exception：命令执行发生异常。 the command execution has been interrupted：命令执行任务中断。 the command execution exit code is not zero：命令执行结束，退出码非0。 |
|---|---|---|---|
| ExitCode | Long | 0 | 命令进程的退出代码。可能值： Linux实例为Shell进程的退出码。 Windows实例为Bat或者PowerShell进程的退出码。 |
| FinishTime | String | 2019-12- 20T06:15:56Z | 命令进程的结束时间。 |
| InstanceId | String | i- bp10jvkun5h1ifzq** ** | 实例ID。 |

云服务器ECS

| InstanceInvoke Status | String | Finished | 单台实例的脚本进程状态。可能值： Running： 周期执行：未手动停止周期执行脚本前，脚本进程一直为进行中。 单次执行：进行中。 Finished： 周期执行：不可能为执行完成。 单次执行：执行完成。 Failed： 周期执行：不可能为执行失败。 单次执行：执行失败。 Stopped：停止脚本执行。 PartialFailed： 周期执行：不可能为部分失败。 单次执行：部分实例有执行失败的脚本进程， 则总执行状态为部分失败。 |
|---|---|---|---|

云服务器ECS

| InvocationStatu s | String | Success | 脚本执行的总执行状态，总执行状态取决于本次调用的全部实例的共同执行状态，可能值： Pending：系统正在校验或发送命令。存在至少一台实例的脚本执行状态为Pending，则总执行状态为Pending。 Scheduled： 立即运行的任务：不适用，不会出现。 周期运行的任务：已发送，等待运行。存在至少一台实例的脚本执行状态为Scheduled，则总执行状态为Scheduled。 Running：命令正在实例上运行。存在至少一台实例的脚本执行状态为Running，则总执行状态为Running。 Success：各个实例上的脚本执行状态均为 Stopped或Success，且至少一个实例的脚本执行状态是Success，则总执行状态为Success。 立即运行的任务：命令执行完成，且退出码为 0。 周期运行的任务：最近一次运行成功且退出码为0，且指定的周期已全部完成。 Failed：各个实例上的脚本执行状态均为 Stopped或Failed，则总执行状态为Failed。实例上的脚本执行状态一项或多项为以下状态时， 均为Failed状态： 命令校验失败（Invalid） 命令发送失败（Aborted） 命令执行完成但退出码非0（Failed） 命令执行超时（Timeout） 命令执行异常（Error） Stopping：正在停止任务。存在至少一台实例的脚本执行状态为Stopping，则总执行状态为 Stopping。 Stopped：任务已停止。所有实例的脚本执行状态是Stopped，则总执行状态为Stopped。实例上的脚本执行状态为以下状态时，均为Stopped 状态： 任务已取消（Cancelled） 任务已终止（Terminated） PartialFailed：部分实例执行成功且部分实例执行失败。各个实例的脚本执行状态均为 Success、Failed或Stopped，则总执行状态为 PartialFailed。 |
|---|---|---|---|
| Output | String | OutPutTestmsg | 脚本进程的输出信息。 |
| Repeats | Integer | 0 | 命令在该实例上执行的次数。 若执行方式为立即执行，则值为0或1。 若执行方式为周期执行，则值为执行过多少次。 |
| StartTime | String | 2019-12- 20T06:15:55Z | 脚本进程在实例中开始执行的时间。 |

云服务器ECS

| StopTime | String | 2020-01- 19T09:15:47Z | 若调用了 StopInvocation ，表示调用的时间。 |
|---|---|---|---|
| Timed | Boolean | false | 查询的命令是否在将来会自动执行。 |
| UpdateTime | String | 2020-01- 19T09:15:47Z | 任务状态的更新时间。 |
| InvokeStatus | String | Finished | 脚本总的执行状态。 说明不推荐查看该参数返回值，推荐查看 InvocationStatus 参数返回值。 |
| Parameters | String | AccessKeyID | 命令中的自定义参数。 |
| RepeatMode | String | Once | 命令执行的方式。可能值： Once：立即执行命令。 Period：定时执行命令。 NextRebootOnly：当实例下一次启动时，自动执行命令。 EveryReboot：实例每一次启动都将自动执行命令。 |
| Tags | Array of Tag |  | 命令执行的标签信息。 |
| Tag |  |  |  |
| TagKey | String | owner | 说明该参数未开放使用。 |
| TagValue | String | zhangsan | 说明该参数未开放使用。 |
| Timed | Boolean | false | 是否为周期执行。 |
| Timeout | Long | 60 | 您创建的命令在ECS实例中执行时最大的超时时间，单位：秒。 当因为某种原因无法运行您创建的命令时，会出现超时现象。超时后，会强制终止命令进程，即取消命令的PID。 |
| Username | String | root | ECS实例中执行命令的用户名称。 说明该参数仅支持Linux系统的ECS 实例，默认以root用户执行命令。 |
| WorkingDir | String | /home/ | 命令执行路径。 |

云服务器ECS

| PageNumber | Long | 1 | 查询结果的页码。 |
|---|---|---|---|
| PageSize | Long | 10 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE***** | 请求ID。 |
| TotalCount | Long | 2 | 命令总个数。 |

**示例**

请求示例

```
http(s)://ecs.example.com/?Action=DescribeInvocations &RegionId=cn-qingdao-**** &InvokeId=t-hz0jdfwd9f**** &CommandId=c-hz0jdfwcsr**** &CommandName=CommandTestName &CommandType=RunShellScrip &Timed=true &InvokeStatus=Finished &InstanceId=i-bp1i7gg30r52z2em**** &PageNumber=1 &PageSize=10 &RepeatMode=Once
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <PageNumber>1</PageNumber>
      <Invocations>
            <Invocation>
                  <CreationTime>2020-01-19T09:15:46Z</CreationTime>
                  <Parameters>{}</Parameters>
                  <CommandContent>ZWNobyAiaGVsbG8gd29ybGQiID4vcm9vdC90ZXN0Ln****==
</CommandContent>
                  <CommandName>exec-2dbb68f9584c4aa6****.t0004</CommandName>
                  <CommandType>RunShellScript</CommandType>
                  <InvokeStatus>Finished</InvokeStatus>
                  <RepeatMode>Once</RepeatMode>
                  <InvokeId>t-7d2a745b412b4601b2d47f6a76d2****</InvokeId>
                  <Username>root</Username>
                  <WorkingDir>/home/</WorkingDir>
                  <Timeout>60</Timeout>
                  <InvokeInstances>
                        <InvokeInstance>
                              <InstanceInvokeStatus>Finished</InstanceInvokeStatus>
                              <InvocationStatus>Success</InvocationStatus>
                              <ExitCode>0</ExitCode>
                              <Dropped>0</Dropped>
                              <InstanceId>i-bp10jvkun5h1ifzq****</InstanceId>
                              <UpdateTime>2020-01-19T09:15:47Z</UpdateTime>
                              <Output></Output>
                              <Repeats>1</Repeats>
                              <ErrorInfo></ErrorInfo>
                              <CreationTime>2020-01-19T09:15:46Z</CreationTime>
                              <FinishTime>2020-01-19T09:15:47Z</FinishTime>
                              <StopTime></StopTime>
                              <StartTime>2020-01-19T09:15:47Z</StartTime>
                              <ErrorCode></ErrorCode>
                        </InvokeInstance>
                  </InvokeInstances>
                  <Timed>false</Timed>
                  <Frequency></Frequency>
                  <CommandId>c-4d34302d02424c5c8e10281e3ad2****</CommandId>
            </Invocation>
      </Invocations>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
```

`JSON` 格式云服务器ECS

```json
{
 "PageNumber": 1,
 "Invocations": {
  "Invocation": [
   {
    "CreationTime": "2020-01-19T09:15:46Z",
    "Parameters": "{}",
    "CommandContent": "ZWNobyAiaGVsbG8gd29ybGQiID4vcm9vdC90ZXN0Ln****==",
    "CommandName": "exec-2dbb68f9584c4aa6****.t0004",
    "CommandType": "RunShellScript",
    "InvokeStatus": "Finished",
                "RepeatMode": "Once",
    "InvokeId": "t-7d2a745b412b4601b2d47f6a76d2****",
    "Username": "root",
                "WorkingDir": "/home/",
                "Timeout": 60,
                "InvokeInstances": {
     "InvokeInstance": [
      {
       "InstanceInvokeStatus": "Finished",
       "InvocationStatus": "Success",
       "ExitCode": 0,
       "Dropped": 0,
       "InstanceId": "i-bp10jvkun5h1ifzq****",
       "UpdateTime": "2020-01-19T09:15:47Z",
       "Output": "",
       "Repeats": 1,
       "ErrorInfo": "",
       "CreationTime": "2020-01-19T09:15:46Z",
       "FinishTime": "2020-01-19T09:15:47Z",
       "StopTime": "",
       "StartTime": "2020-01-19T09:15:47Z",
       "ErrorCode": ""
      }
```

]

```json
    },
    "Timed": false,
    "Frequency": "",
    "CommandId": "c-4d34302d02424c5c8e10281e3ad2****"
   }
```

]

```json
 },
 "TotalCount": 1,
 "PageSize": 10,
 "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 400 | NumberExceed.Tags | The Tags parameter number is exceed , Valid : 20 | 标签个数超过最大限制，本操作最多可以操作 20 个标签。 |

| 云服务器ECS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
|---|---|---|---|
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 400 | MissingParameter.T agKey | You must specify Tag.N.Key. | 请指定标签键。 |
| 403 | InvalidParam.PageN umber | The specified parameter is invalid. | 指定的 PageNumber 参数无效。 |
| 403 | InvalidParam.PageSi ze | The specified parameter is invalid. | 指定的 PageSize 参数无效。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### DescribeCloudAssistantStatus

调用DescribeCloudAssistantStatus查询一台或者多台实例是否安装了云助手客户端。如果已安装了云助手， 还将查询云助手命令执行的总数量、正在执行的数量以及最近一次命令执行的时间。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCloudAs sistantStatus | 系统规定参数，取值： DescribeCloudAssistantStatus。 |
| RegionId | String | 是 | cn-qingdao-**** | 实例所在地域ID。您可以调用 DescribeRegions查询地域ID。 |
| OSType | String | 否 | Windows | 实例的操作系统类型。取值范围： Windows。 Linux。 |
| PageNumber | Long | 否 | 1 | 当前页码。 起始值为1。 默认值为1。 |
| PageSize | Long | 否 | 10 | 分页查询时设置的每页行数。 最大值为100。 默认值为10。 |

云服务器ECS

| InstanceId.N | RepeatLi st | 否 | i- bp1iudwa5b1tqa* ***** | 实例ID列表。单次请求最多支持50台实例，N的取值范围为1~50。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceCloudA ssistantStatusS et | Array of InstanceCloudA ssistantStatus |  | 实例云助手安装状态结果集合。 |
| InstanceCloudA ssistantStatus |  |  |  |
| ActiveTaskCou nt | Long | 1 | 正在执行的命令的数量。 |
| CloudAssistant Status | String | true | 是否已经安装了云助手。可能值： true：是。 false：否。 |
| CloudAssistant Version | String | 1.0.1.395 | 云助手客户端版本号。 |
| InstanceId | String | i- bp1iudwa5b1tqa*** *** | 实例ID。 |
| InvocationCoun t | Long | 2 | 已执行的命令的总数量。 |
| LastHeartbeatT ime | String | 2021-03- 15T09:00:00Z | 云助手最近一次心跳时间。 |
| LastInvokedTim e | String | 2022-03- 15T09:00:00Z | 最近一次命令执行的时间。 |
| OSType | String | Windows | 实例操作系统类型。可能值： Windows。 Linux。 |
| SupportSession Manager | Boolean | true | 说明该参数未开放使用。 |
| PageNumber | Long | 1 | 当前页码。 |
| PageSize | Long | 10 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| TotalCount | Long | 1 | 实例总个数。 |

云服务器ECS

**示例**

请求示例

```
https://ecs.example.com/?Action=DescribeCloudAssistantStatus &InstanceId.1=i-bp1iudwa5b1tqa****** &RegionId=cn-qingdao-****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
  <PageNumber>1</PageNumber>
  <InstanceCloudAssistantStatusSet>
        <CloudAssistantVersion>1.0.1.395</CloudAssistantVersion>
        <InstanceId>i-bp1iudwa5b1tqa******</InstanceId>
        <InvocationCount>2</InvocationCount>
        <OSType>Windows</OSType>
        <CloudAssistantStatus>true</CloudAssistantStatus>
        <LastInvokedTime>2022-03-15T09:00:00Z</LastInvokedTime>
        <ActiveTaskCount>1</ActiveTaskCount>
  </InstanceCloudAssistantStatusSet>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "PageNumber": 1,
    "InstanceCloudAssistantStatusSet": {
        "CloudAssistantVersion": "1.0.1.395",
        "InstanceId": "i-bp1iudwa5b1tqa******",
        "InvocationCount": 2,
        "OSType": "Windows",
        "CloudAssistantStatus": true,
        "LastInvokedTime": "2022-03-15T09:00:00Z",
        "ActiveTaskCount": 1
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 403 | InstanceIds.ExceedL imit | The number of instance IDs exceeds the upper limit. | 目标实例数量超过上限。 |

云服务器ECS

| 403 | InvalidParam.PageSi ze | The specified parameter is invalid. | 指定的 PageSize 参数无效。 |
|---|---|---|---|
| 403 | InvalidParam.PageN umber | The specified parameter is invalid. | 指定的 PageNumber 参数无效。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 404 | InvalidInstance.NotF ound | The specified instance does not exist. | 指定的实例不存在。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### DeleteCommand

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteCommand | 系统规定参数，取值：DeleteCommand。 |
| CommandId | String | 是 | c- 4d34302d02424c 5c8e10281e3a31 5*** | 命令ID。您可以通过接口 DescribeCommands查询所有可用的 CommandId。 |
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查询地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | E69EF3CC-94CD- 42E7-8926- F133B863**** | 请求 ID。 |

**示例**

请求示例

```
&CommandId=c-4d34302d02424c5c8e10281e3a315*** &RegionId=cn-qingdao-****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>E69EF3CC-94CD-42E7-8926-F133B863****</RequestId>
```

云服务器ECS `JSON` 格式

```json
{
    "RequestId":"E69EF3CC-94CD-42E7-8926-F133B863****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 403 | InvalidStatus.CmdIdI nUse | The specified commandId is in use by some runing Invocation. | 指定的CommandId正在执行中，请停止命令后再次调用该接口。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 404 | InvalidCmdId.NotFo und | The specified command ID does not exist. | 指定的 CommandId 参数有误，请检查参数值是否正确。您可以通过接口 DescribeCommands 查询所有可用的 CommandId。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### SendFile

**接口说明：**

目标ECS实例的状态必须为运行中（ `Running` ）。 目标ECS实例必须预先安装云助手客户端。 文件内容在进行Base64编码后，大小不能超过32 KB。 文件下发可能会因为目标ECS实例的状态异常、网络异常或云助手客户端异常而出现失败的情况。请调用

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SendFile | 系统规定参数。取值：SendFile。 |
| Content | String | 是 | #!/bin/bash echo "Current User is :" echo $(ps \| grep "$$" \| awk '{print $2}') ------- - oss://bucketNam e/objectName | 文件内容。文件内容在Base64编码后，大小不能超过32 KB。 当 ContentType 参数为 PlainText 时，该字段为明文格式的普通文本。 当 ContentType 参数为 Base64 时，该字段为Base64编码的文本。 |

云服务器ECS

| InstanceId.N | RepeatLi st | 是 | i- bp185dy2o3o6n* *** | 需要执行命令的ECS实例列表。最多能指定 50台ECS实例ID。N的取值范围为1~50。 |
|---|---|---|---|---|
| Name | String | 是 | file.txt | 文件名称。支持全字符集，长度不得超过 255个字符。 |
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查询地域ID。 |
| TargetDir | String | 是 | /home | 文件下发目标ECS实例中的目录。如不存在则会自动创建。 |
| Description | String | 否 | This is a test file. | 描述信息。支持全字符集，长度不得超过 512个字符。 |
| Timeout | Long | 否 | 60 | 下发文件的超时时间。单位：秒。 当因为进程原因、缺失模块、缺失云助手客户端等原因无法下发文件时，会出现超时现象。 当设置的超时时间小于10秒时，为确保下发成功，系统会将超时时间自动设置为10 秒。 默认值：60。 |
| ContentType | String | 否 | PlainText | 文件内容类型。 PlainText：普通文本。 Base64：Base64编码。 默认值：PlainText。 |
| FileOwner | String | 否 | root | 文件的用户。只对Linux实例生效，默认为 root。 |
| FileGroup | String | 否 | root | 文件的用户组。只对Linux实例生效，默认为 root。 |
| FileMode | String | 否 | 0644 | 文件的权限。只对Linux实例生效，设置方式与chmod命令相同。 默认值为0644，表示用户具有读写权限，用户组和其它用户具有只读权限。 |
| Overwrite | Boolean | 否 | true | 如果同名文件在目标目录已存在，是否覆盖文件。 true：覆盖。 false：不覆盖。 默认值：false。 |

**返回数据**

云服务器ECS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InvokeId | String | f- 7d2a745b412b46*** * | 命令执行ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE**** | 请求ID。 |

**示例**

请求示例

```
&Content=#!/bin/bash echo "Current User is :" echo $(ps | grep "$$" | awk '{print $2}') -------- oss://bucketName/objectName &InstanceId.1=i-bp185dy2o3o6n**** &Name=file.txt &RegionId=cn-qingdao-**** &TargetDir=/home
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
          <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE****</RequestId>
          <InvokeId>f-7d2a745b412b46****</InvokeId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE****",
    "InvokeId": "f-7d2a745b412b46****"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 403 | FileSize.ExceedLimit | The length of file content exceeds limit. | 文件内容长度超过上限。 |
| 403 | FileName.ExceedLi mit | The length of file name exceeds limit. | 文件名称长度超过上限。 |
| 403 | FileDesc.ExceedLimi t | The length of file description exceeds limit. | 文件描述长度超过上限。 |
| 403 | FileTargetDir.Invalid | The target directory of file is invalid. | 目标路径TargetDir参数无效。 |

云服务器ECS

| 403 | InstanceIds.ExceedL imit | The number of instance IDs exceeds the upper limit. | 目标实例数量超过上限。 |
|---|---|---|---|
| 403 | FileMode.Invalid | The mode of file is invalid. | 文件权限FileMode参数无效。 |
| 403 | FileContent.Decode Error | The Content can not be base64 decoded. | 文件内容Base64解码错误。 |
| 403 | FileContentType.Inv alid | The ContentType of file is invalid. | 文件内容类型ContentType参数无效。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 404 | InvalidInstance.NotF ound | The specified instances not found. | 指定的实例ID不存在。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

##### DescribeSendFileResults

**接口说明**

当您下发文件后，不代表文件一定成功下发。您需要通过接口返回值查看实际下发结果，并以实际输出结果为准。 您可以查询最近2周的下发记录，下发记录的保留上限为10万条。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSendFile Results | 系统规定参数。取值： DescribeSendFileResults。 |
| RegionId | String | 是 | cn-qingdao-**** | 地域ID。您可以调用DescribeRegions查询地域ID。 |
| InvokeId | String | 否 | f-hz0jdfwd9f**** | 执行ID。 |
| Name | String | 否 | test.txt | 文件名称。传入该参数后，将查询该名称文件的所有的下发记录。 |
| InstanceId | String | 否 | i-hz0jdfwd9f**** | 实例ID。传入该参数后，将查询该实例所有的文件下发记录。 |
| PageNumber | Long | 否 | 1 | 当前页码。 起始值为1。 默认值为1。 |

云服务器ECS

| PageSize | Long | 否 | 10 | 分页查询时设置的每页行数。 最大值为50。 默认值为10。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Invocations | Array of Invocation |  | 文件下发记录。 |
| Invocation |  |  |  |
| Content | String | #!/bin/bash echo "Current User is :" echo $(ps \| grep "$$" \| awk '{print $2}') | 文件内容。 |
| ContentType | String | PlainTex | 文件内容类型。可能值： PlainText：普通文本。 Base64：Base64编码。 |
| CreationTime | String | 2022-04- 10T06:15:54Z | 文件下发任务创建时间。 |
| Description | String | This is a test file. | 描述信息。 |
| FileGroup | String | root | 文件的用户组。 |
| FileMode | String | 777 | 文件的权限。 |
| FileOwner | String | root | 文件的用户。 |

云服务器ECS

| InvocationStatu s | String | Success | 文件的总下发状态。总状态取决于本次下发的全部实例的共同执行状态，可能值： Pending：系统正在校验或下发文件。存在至少一台实例的下发状态为Pending，则总状态为 Pending。 Running：文件创建任务正在实例上运行。存在至少一台实例的状态为Running，则总状态为 Running。 Success：各个实例上的文件下发状态均为 Success，则总执行状态为Success。 Failed：各个实例上的文件下发状态均为 Failed，则总执行状态为Failed。实例上的文件下发状态一项或多项为以下状态时，返回值均为 Failed状态： 校验失败（Invalid）。 文件发送失败（Aborted）。 文件创建失败（Failed）。 文件下发超时（Timeout）。 文件下发异常（Error）。 PartialFailed：部分实例下发成功且部分实例执行失败。存在且只存在实例下发状态为Success 与Failed时，则总执行状态为PartialFailed。 |
|---|---|---|---|
| InvokeId | String | f-hz0jdfwd9f**** | 执行ID。 |
| InvokeInstance s | Array of InvokeInstance |  | 下发文件目标实例集类型。 |
| InvokeInstance |  |  |  |
| CreationTime | String | 2022-04- 10T06:15:54Z | 文件下发任务的创建时间。 |

云服务器ECS

| ErrorCode | String | InstanceNotExists | 文件下发的失败原因代码。可能值： 空：文件下发正常。 InstanceNotExists：指定的实例不存在或已释放。 InstanceReleased：下发文件期间，该实例被释放。 InstanceNotRunning：创建下发文件任务时， 该实例不在运行中。 AccountNotExists：指定的账号不存在。 ClientNotRunning：云助手客户端未运行。 ClientNotResponse：云助手客户端无响应。 ClientIsUpgrading：云助手客户端正在升级中。 ClientNeedUpgrade：云助手客户端需要升级。 DeliveryTimeout：发送文件超时。 FileCreateFail：文件创建失败。 FileAlreadyExists：相同路径下存在同名文件。 FileContentInvalid：文件内容不合法。 FileNameInvalid：文件名不合法。 FilePathInvalid：文件路径不合法。 FileAuthorityInvalid：文件权限不合法。 |
|---|---|---|---|

云服务器ECS

| ErrorInfo | String | the instance is not running when create task | 文件下发的失败或执行失败原因详情。可能值： 空：文件下发正常。 the specified instance does not exists：指定的实例不存在或已释放。 the instance has released when create task：下发文件期间，该实例被释放。 the instance is not running when create task：创建下发文件任务时，该实例不在运行中。 the specified account does not exists：指定的账号不存在。 the aliyun service is not running on the instance：云助手客户端未运行。 the aliyun service in the instance does not response：云助手客户端无响应。 the aliyun service in the instance is upgrading now：云助手客户端正在升级中。 the aliyun service in the instance need upgrade：云助手客户端需要升级。 the command delivery has been timeout： 下发文件超时。 Unexpected error during creating：文件创建失败。 File already exists：相同路径下存在同名文件。 File content error：文件内容不合法。 File name is invalid：文件名不合法。 File path is invalid：文件路径不合法。 Owner not exists：用户不存在。 Group not exists：用户组不存在。 Mode is invalid：文件权限设置不合法。 |
|---|---|---|---|
| FinishTime | String | 2022-04- 12T06:20:00Z | 下发任务的结束时间。 |
| InstanceId | String | i-uf614fhehhz**** | 实例ID。 |
| InvocationStatu s | String | Success | 下发任务的状态。 |
| StartTime | String | 2022-04- 10T06:20:00Z | 下发任务在实例中开始执行的时间。 |
| UpdateTime | String | 2022-04-10T06:2:00 | 任务状态的更新时间。 |
| Name | String | test.txt | 文件名称。 |
| Overwrite | String | false | 是否允许覆盖。 |
| TargetDir | String | /root | 目标路径。 |

云服务器ECS

| VmCount | Integer | 1 | 下发实例的数量。 |
|---|---|---|---|
| PageNumber | Long | 1 | 查询结果的当前页码。 |
| PageSize | Long | 10 | 每页行数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3**** | 请求ID。 |
| TotalCount | Long | 2 | 命令总个数。 |

**示例**

请求示例

```
https://ecs.aliyuncs.com/?Action=DescribeSendFileResults &RegionId=cn-qingdao-**** &InvokeId=f-hz0vk9**** &Name=test.txt &InstanceId=i-bp1hsglsw**** &PageNumber=1 &PageSize=10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
  <TotalCount>2</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3****</RequestId>
  <PageNumber>1</PageNumber>
  <Invocations>
        <FileMode>777</FileMode>
        <InvocationStatus>Success</InvocationStatus>
        <Overwrite>false</Overwrite>
        <Description>This is a test file. </Description>
        <VmCount>1</VmCount>
        <ContentType>PlainTex</ContentType>
        <Content>#!/bin/bash echo "Current User is :" echo $(ps | grep "$$" | awk '{print
$2}')</Content>
        <CreationTime>2022-04-10T06:15:54Z </CreationTime>
        <FileGroup>root</FileGroup>
        <TargetDir>/root</TargetDir>
        <FileOwner>root</FileOwner>
        <InvokeId>f-hz0jdfwd9f****</InvokeId>
        <Name>test.txt</Name>
        <InvokeInstances>
              <InvocationStatus>Success</InvocationStatus>
              <FinishTime>2022-04-12T06:20:00Z</FinishTime>
              <InstanceId>i-uf614fhehhz****</InstanceId>
              <ErrorInfo>the instance is not running when create task</ErrorInfo>
              <UpdateTime>2022-04-10T06:2:00</UpdateTime>
              <StartTime>2022-04-10T06:20:00Z</StartTime>
              <CreationTime>2022-04-10T06:15:54Z</CreationTime>
              <ErrorCode>InstanceNotExists</ErrorCode>
        </InvokeInstances>
  </Invocations>
```

`JSON` 格式云服务器ECS

```json
{
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3****",
    "PageNumber": 1,
    "Invocations": {
        "FileMode": 777,
        "InvocationStatus": "Success",
        "Overwrite": false,
        "Description": "This is a test file.",
        "VmCount": 1,
        "ContentType": "PlainTex",
        "Content": "#!/bin/bash echo \"Current User is :\" echo $(ps | grep \"$$\" | awk
'{print $2}')",
        "CreationTime": "2022-04-10T06:15:54Z",
        "FileGroup": "root",
        "TargetDir": "/root",
        "FileOwner": "root",
        "InvokeId": "f-hz0jdfwd9f****",
        "Name": "test.txt",
        "InvokeInstances": {
            "InvocationStatus": "Success",
            "FinishTime": "2022-04-12T06:20:00Z",
            "InstanceId": "i-uf614fhehhz****",
            "ErrorInfo": "the instance is not running when create task",
            "UpdateTime": "2022-04-10T06:2:00",
            "StartTime": "2022-04-10T06:20:00Z",
            "CreationTime": "2022-04-10T06:15:54Z",
            "ErrorCode": "InstanceNotExists"
        }
    }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RegionId.ApiNotSup ported | The api is not supported in this region. | 指定地域下不支持调用 API。请检查 RegionId 参数取值是否正确。 |
| 403 | InvalidParam.PageN umber | The specified parameter is invalid. | 指定的 PageNumber 参数无效。 |
| 403 | InvalidParam.PageSi ze | The specified parameter is invalid. | 指定的 PageSize 参数无效。 |
| 403 | Operation.Forbidden | The operation is not permitted. | 该操作是不被允许的。 |
| 500 | InternalError.Dispat ch | An error occurred when you dispatched the request. | 发送请求时发生错误，请稍后重试。 |

#### 标签

##### AddTags

云服务器ECS 添加或者覆盖一个或者多个标签到云服务器ECS的各项资源上。您可以添加标签到实例、磁盘、快照、镜像、安全组等，便于管理资源。

**接口说明**

调用该接口时，您需要注意： 单项云服务器ECS资源最多可以添加20个标签。 标签键（ `Tag.N.Key` ）与标签值（ `Tag.N.Value` ）必须键值匹配。 如果标签键（ `Tag.N.Key` ）在指定的资源上已经存在，则使用新的标签值（ `Tag.N.Value` ）自动覆盖原标签值。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | AddTags | 系统规定参数，取值：AddTags。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 资源所在的地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ResourceType | String | 是 | instance | 资源类型。取值范围： disk instance image securitygroup snapshot 以上取值均为小写。 |
| ResourceId | String | 是 | i- bp1ecr********5g o2go | 要绑定标签的资源ID。例如，当资源类型 （ResourceType）为实例（instance） 时，资源ID可以理解为实例ID。 |
| Tag.N.value | String | 否 | FinanceTagValue | 资源的标签值。 说明为提高兼容性，建议您尽量使用Tag.N.Value参数。 |
| Tag.N.key | String | 否 | Finance | 资源的标签键。 说明为提高兼容性，建议您尽量使用Tag.N.Key参数。 |
| Tag.N.Key | String | 否 | Finance | 资源的标签键。N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 128个字符，不能以aliyun和acs:开头，不能包含 http:// 或者 https:// 。 |

云服务器ECS

| Tag.N.Value | String | 否 | FinanceTagValue | 资源的标签值。N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128 个字符，不能以aliyun和acs:开头，不能包含 http:// 或者 https:// 。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &ResourceType=instance &ResourceId=i-bp1ecr5g**** &Tag.1.Key=Finance &Tag.1.Value=FinanceTagValue
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>C46FF5A8-C5F0-4024-8262-B16B639225A0</RequestId>
```

`JSON` 格式

```json
{
  "RequestId": "C46FF5A8-C5F0-4024-8262-B16B639225A0"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 404 | InvalidResourceId.N otFound | The specified ResourceId is not found in our records. | 指定的资源不存在，请您检查该资源是否正确。 |
| 404 | InvalidResourceTyp e.NotFound | The ResourceType provided does not exist in our records. | 指定的资源类型不存在。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键不合法。 |

云服务器ECS

| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值不合法。 |
|---|---|---|---|
| 400 | OperationDenied.Qu otaExceed | The quota of tags on resource is beyond permitted range. | 资源标签已达上限。 |
| 403 | InvalidResourceId.N otSupported | The specified ResourceId does not support tagging. | 指定的资源ID不支持标记。 |
| 400 | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. | 指定的Tag.n.Key和Tag.n.Value不匹配。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 403 | QuotaExceed.Tags | %s | 标签数超过可以配置的最大数量。 |

##### RemoveTags

从实例、磁盘、快照、镜像或者安全组等解绑一个或多个标签。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | RemoveTags | 系统规定参数，取值：RemoveTags。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 资源所属地域。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ResourceId | String | 是 | s-946ntx4** | 要解绑标签的资源ID。例如，当资源类型 （ResourceType）为实例（instance） 时，资源ID可以理解为实例ID。 |
| ResourceType | String | 是 | snapshot | 资源类型。取值范围： disk instance image securitygroup snapshot 以上取值均为小写。 |
| Tag.N.value | String | 否 | FinanceTagValue | 资源的标签值。 说明为提高兼容性，建议您尽量使用Tag.N.Value参数。 |

云服务器ECS

| Tag.N.key | String | 否 | Finance | 资源的标签键。 说明为提高兼容性，建议您尽量使用Tag.N.Key参数。 |
|---|---|---|---|---|
| Tag.N.Key | String | 否 | Finance | 资源的标签键。N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 64个字符，不能以aliyun和acs:开头，不能包含 http:// 或者 https:// 。 |
| Tag.N.Value | String | 否 | FinanceTagValue | 资源的标签值。N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128 个字符，不能以aliyun和acs:开头，不能包含 http:// 或者 https:// 。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &ResourceId=s-946ntx4**** &ResourceType=snapshot &Tag.1.Key=Finance &Tag.1.Value=FinanceTagValue
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>6A2C8AB5-E15D-478C-B56A-CF3DAF060028</RequestId>
```

`JSON` 格式

```json
{
  "RequestId": "6A2C8AB5-E15D-478C-B56A-CF3DAF060028"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云服务器ECS

| 404 | InvalidResourceId.N otFound | The specified ResourceId is not found in our records. | 指定的资源不存在，请您检查该资源是否正确。 |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 404 | InvalidResourceTyp e.NotFound | The ResourceType provided does not exist in our records. | 指定的资源类型不存在。 |
| 403 | InvalidResourceId.N otSupported | The specified ResourceId does not support tagging. | 指定的资源ID不支持标记。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键不合法。 |
| 400 | InvalidResourceTyp e.NotFound | The specified ResourceType does not exist. | 资源类型无效。 |

##### DescribeTags

查询可以供您使用的标签。您可以根据资源类型、资源ID、标签键或标签值等条件查询标签，筛选条件之间为逻辑与（&&）关系，返回满足所有筛选条件的标签。

**接口说明**

如果您指定了标签键（Tag.N.Key）但没有指定标签值（Tag.N.Value），我们将查询该标签键对应的所有标签键值对。如果您指定了标签键值对，就查询精确匹配该键值对的标签。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | DescribeTags | 系统规定参数，取值：DescribeTags。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| PageSize | Integer | 否 | 50 | 分页查询时设置的每页行数。 最大值：100 默认值：50 |
| PageNumber | Integer | 否 | 1 | 标签列表的页码。 起始值：1 默认值：1 |

云服务器ECS

| ResourceType | String | 否 | snapshot | 资源类型。取值范围： disk instance image securitygroup snapshot 以上取值均为小写。 |
|---|---|---|---|---|
| ResourceId | String | 否 | s-946ntx4wr | 标签绑定的资源ID。例如，当资源类型 （ResourceType）为实例（instance） 时，资源ID可以理解为实例ID。 |
| Tag.N.value | String | 否 | Finance | 资源的标签值。 说明为提高兼容性，建议您尽量使用Tag.N.Value参数。 |
| Tag.N.key | String | 否 | Finance | 资源的标签键。 说明为提高兼容性，建议您尽量使用Tag.N.Key参数。 |
| Tag.N.Key | String | 否 | Finance | 资源的标签键。N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 64个字符，不能以aliyun和acs:开头，不能包含 http:// 或者 https:// 。 |
| Tag.N.Value | String | 否 | Finance | 资源的标签值。N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128 个字符，不能以aliyun和acs:开头，不能包含 http:// 或者 https:// 。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 标签列表的页码。 |
| PageSize | Integer | 50 | 分页查询时设置的每页行数。 |
| RequestId | String | B04B8CF3-4489- 432D-83BA- 6F128E4F2295 | 请求ID。 |
| Tags | Array |  | 满足所有筛选条件的标签。 |
| Tag |  |  |  |
| ResourceTypeC ount | Struct |  | 资源类型计数。 |

| 开发指南·API参考 |  |  | 云服务器EC |
|---|---|---|---|

| Ddh | Integer | 1 | 该标签标记了多少专有宿主机。 |
|---|---|---|---|
| Disk | Integer | 15 | 该标签标记了多少磁盘。 |
| Eni | Integer | 5 | 该标签标记了多少弹性网卡。 |
| Image | Integer | 6 | 该标签标记了多少镜像。 |
| Instance | Integer | 45 | 该标签标记了多少实例。 |
| KeyPair | Integer | 17 | 该标签标记了多少密钥对。 |
| LaunchTemplat e | Integer | 6 | 该标签标记了多少启动模板。 |
| Securitygroup | Integer | 4 | 该标签标记了多少安全组。 |
| Snapshot | Integer | 15 | 该标签标记了多少快照。 |
| Volume | Integer | 6 | 该标签标记了多少扩展卷。 |
| TagKey | String | test | 标签键。 |
| TagValue | String | api | 标签值。 |
| TotalCount | Integer | 1 | 标签总个数。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &PageSize=50 &PageNumber=1 &ResourceType=snapshot &ResourceId=s-946ntx4** &Tag.1.Key=Finance &Tag.1.Value=Finance
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云服务器ECS

```xml
      <RequestId>B04B8CF3-4489-432D-83BA-6F128E4F2295</RequestId>
      <PageNumber>1</PageNumber>
      <PageSize>50</PageSize>
      <Tags>
            <Tag>
                  <TagKey>test</TagKey>
                  <TagValue>api</TagValue>
            </Tag>
      </Tags>
      <TotalCount>1</TotalCount>
```

`JSON` 格式

```json
{
  "PageNumber": 1,
  "PageSize": 50,
  "RequestId": "B04B8CF3-4489-432D-83BA-6F128E4F2295",
  "Tags": {
    "Tag": [
      {
        "TagKey": "test",
        "TagValue": "api"
      }
```

]

```json
  },
  "TotalCount": 1
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 404 | InvalidResourceTyp e.NotFound | The ResourceType provided does not exist in our records. | 指定的资源类型不存在。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
| 400 | InvalidTagKey.Malfo rmed | The parameter Tag.n.Key is illegal. | Tag.n.Key 不合法。 |
| 400 | InvalidTagValue.Mal formed | The parameter Tag.n.Value is illegal. | Tag.n.Value 不合法。 |

##### TagResources

**接口说明**

绑定标签前，阿里云会校验资源已有标签数量。超过限制值后返回报错信息。 云服务器ECS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | TagResources | 系统规定参数。取值：TagResources |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 资源所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ResourceId.N | RepeatLi st | 是 | i- bp67acfmxazb4p h*** | 资源ID，N的取值范围为1~50。 |
| ResourceType | String | 是 | instance | 资源类型定义。取值范围： instance：ECS实例 disk：磁盘 snapshot：快照 image：镜像 securitygroup：安全组 volume：存储卷 eni：弹性网卡 ddh：专有宿主机 keypair：SSH密钥对 |
| Tag.N.Key | String | 否 | Test | 资源的标签键。N的取值范围：1~20。一旦传入该值，则不允许为空字符串。最多支持 128个字符，不能以aliyun和acs:开头，不能包含http://或者https://。 |
| Tag.N.Value | String | 否 | Test | 资源的标签值。N的取值范围：1~20。一旦传入该值，可以为空字符串。最多支持128 个字符，不能以acs:开头，不能包含http:// 或者https://。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &ResourceId.1=i-bp1j6qtvdm8w0z1o0**** &ResourceId.2=i-bp1j6qtvdm8w0z1oP**** &ResourceType=instance &Tag.1.Key=Test
```

`&<`公共请求参数> 云服务器ECS 正常返回示例 `XML` 格式

```xml
    <RequestId>C46FF5A8-C5F0-4024-8262-B16B639225A0</RequestId>
```

`JSON` 格式

```json
{
 "RequestId":"C46FF5A8-C5F0-4024-8262-B16B639225A0"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | %s | 提供的地域ID不存在。 |
| 404 | MissingParameter.T agOwnerUid | The parameter - TagOwnerUid should not be null | 参数“TagOwnerUid”不能为空。 |
| 404 | MissingParameter.T agOwnerBid | The parameter - TagOwnerBid should not be null | 参数“TagOwnerBid”不能为空。 |
| 404 | MissingParameter.R esourceType | The parameter - ResourceType should not be null | 参数“ResourceType”不能为空。 |
| 404 | MissingParameter.T ags | The parameter - Tags should not be null | 参数“Tags”不能为空。 |
| 404 | MissingParameter.R egionId | The parameter - RegionId should not be null | 参数“RegionId”不能为空。 |
| 403 | PermissionDenied.T agOwnerUid | The specified operator not have permission to set TagOwnerUid value. | 无权设置标签归属者。 |
| 403 | PermissionDenied.S cope | The specified operator not have permission to set Scope value. | 指定的操作员无权设置范围值。 |
| 400 | NumberExceed.Res ourceIds | The ResourceIds parameter's number is exceed , Valid : 50 | 参数“ResourceIds”中包含的“ResourceId”不能超过 50 个。 |
| 400 | NumberExceed.Tags | The Tags parameter's number is exceed , Valid : 20 | 标签个数超过最大限制，本操作最多可以操作 20 个标签。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 404 | InvalidResourceId.N otFound | The specified ResourceIds are not found in our records. | 指定的资源不存在，请检查参数“ResourceId”是否正确。 |
| 404 | InvalidResourceTyp e.NotFound | The ResourceType provided does not exist in our records. | 指定的资源类型不存在。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键不合法。 |

云服务器ECS

| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值不合法。 |
|---|---|---|---|
| 400 | OperationDenied.Qu otaExceed | The quota of tags on resource is beyond permitted range. | 资源标签已达上限。 |
| 403 | InvalidResourceId.N otSupported | The specified ResourceId does not support tagging. | 指定的资源ID不支持标记。 |
| 400 | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. | 指定的Tag.n.Key和Tag.n.Value不匹配。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 400 | Invalid.Scope | The specified scope is invalid. | 可见范围参数无效。 |
| 403 | NoPermission.Tag | The operator is not permission for the tag. | 您没有操作该资源标签的权限。 |
| 403 | QuotaExceed.Tags | %s | 标签数超过可以配置的最大数量。 |

##### ListTagResources

调用ListTagResources查询一个或多个ECS资源和ECS资源已经绑定的标签列表。

**接口说明**

请求中至少指定一个参数： `ResourceId.N` 、 `Tag.N` （ `Tag.N.Key` 与 `Tag.N.Value` ）或者 `TagFilter.N` ，以确定查询对象。 同时指定下列参数时，返回结果中仅包含同时满足这两个条件的ECS资源。

```
 Tag.N 和 ResourceId.N
 TagFilter.N 和 ResourceId.N
```

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTagResources | 系统规定参数，取值：ListTagResources。 |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 资源所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |

云服务器ECS

| ResourceType | String | 是 |  | instance | 资源类型。取值范围： instance：ECS实例 disk：块存储 snapshot：快照 image：镜像 securitygroup：安全组 volume：存储卷 eni：弹性网卡 ddh：专有宿主机 keypair：SSH密钥对 |  |  |  |
|---|---|---|---|---|---|---|---|---|
| TagFilter.N.TagKe y | String | 是 |  | env | 模糊查找ECS资源时使用的标签键。标签键长度的取值范围：1~128。N的取值范围： 1~5 TagFilter.N 用于模糊查找绑定了指定标签的ECS资源，由一个键和一个或多个值组成。模糊查询可能会有2秒延时，仅支持模糊过滤后资源数小于等于5000的情况。 通过标签键 （ TagFilter.N.TagKey ）模糊查找ECS资源时，标签值 （ TagFilter.N.TagValues.N ） 必须为空。例如，模糊搜索标签键为 environment 的ECS资源时， TagFilter.1.TagKey 可以设置为 env ， 而 TagFilter.1.TagValues 必须为空。 通过标签值 （ TagFilter.N.TagValues.N ） 模糊查找ECS资源时，标签键 （ TagFilter.N.TagKey ）必须设置为精确值。例如，模糊搜索标签键为 env ，标签值为 product 的 ECS资源时， TagFilter.1.TagKey 必须精确设置为 env ， TagFilter.1.TagValues .1 可以设置为 proc 。 标签键之间为交集关系，即仅同时满足您指定的所有标签键的ECS资源才会被查找到。 同一标签键下的标签值之间为并集关系， 即满足您为该标签键指定的任一标签值的 ECS资源均会被查找到。 说明 TagFilter.N 与 Tag.N 参数不能同时使用，否则会返回错误信息。 |  |  |  |
|  |  |  |  |  |  | env | TagFilter.1.TagValues |  |
|  |  |  |  |  | .1 |  |  |  |
| ResourceId.N | RepeatLi st | 否 |  | i- bp1j6qtvdm8w0z 1o0*** | ECS资源ID。N的取值范围：1~50 |  |  |  |

云服务器ECS

| Tag.N.Key | String | 否 | FinanceDeptKey | 精确查找ECS资源时使用的标签键。标签键长度的取值范围：1~128。N的取值范围： 1~20。 Tag.N 用于精确查找绑定了指定标签的 ECS资源，由一个键值对组成。 仅指定 Tag.N.Key 时，则返回关联该标签键的所有资源。 仅指定 Tag.N.Value ，则报错 InvalidParameter.TagValue 。 同时指定多个标签键值对时，仅同时满足所有标签键值对的ECS资源会被查找到。 |
|---|---|---|---|---|
| Tag.N.Value | String | 否 | FinanceDeptValu e | 精确查找ECS资源时使用的标签值。标签值长度的取值范围：1~128。N的取值范围： 1~20 |
| TagFilter.N.TagVa lues.N | RepeatLi st | 否 | product | 模糊查找ECS资源时使用的标签值。标签值长度的取值范围：1~128。N的取值范围： 1~5 |
| NextToken | String | 否 | caeba0bbb2be03 f84eb48b699f0a4 883 | 下一个查询开始Token。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f84 eb48b699f0a4883 | 下一个查询开始Token。 |
| RequestId | String | 484256DA-D816- 44D2-9D86- B6EE4D5BA78C | 请求ID。 |
| TagResources | Array of TagResource |  | 由资源及其标签组成的集合，包含了资源ID、资源类型和标签键值等信息。 |
| TagResource |  |  |  |
| ResourceId | String | i- bp1j6qtvdm8w0z1o 0*** | 资源ID。 |
| ResourceType | String | instance | 资源类型。 |
| TagKey | String | FinanceDeptKey | 标签键。 |
| TagValue | String | FinanceDeptValue | 标签值。 |

**示例**

云服务器ECS 请求示例

```
https://ecs.example.com/?Action=ListTagResources &RegionId=cn-qingdao-env17-d01 &ResourceType=instance &ResourceId.1=i-bp1j6qtvdm8w0z1o0***
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <TagResource>
         <ResourceType>instance</ResourceType>
         <TagValue>FinanceTagValue</TagValue>
         <ResourceId>i-bp1j6qtvdm8w0z1o0***</ResourceId>
         <TagKey>FinanceTagKey</TagKey>
      </TagResource>
   <RequestId>DE65F6B7-7566-4802-9007-96F2494AC5XX</RequestId>
```

`JSON` 格式

```json
{
        "TagResource": [
            {
                "ResourceType": "instance",
                "TagValue": "FinanceTagValue",
                "ResourceId": "i-bp1j6qtvdm8w0z1o0***",
                "TagKey": "FinanceTagKey"
            }
```

]

```json
    },
    "RequestId": "DE65F6B7-7566-4802-9007-96F2494AC512"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | %s | 提供的地域ID不存在。 |
| 404 | MissingParameter.T agOwnerUid | The parameter - TagOwnerUid should not be null | 参数TagOwnerUid不能为空。 |
| 404 | MissingParameter.T agOwnerBid | The parameter - TagOwnerBid should not be null | 参数TagOwnerBid不能为空。 |
| 404 | MissingParameter.R esourceType | The parameter - ResourceType should not be null | 参数ResourceType不能为空。 |

云服务器ECS

| 404 | MissingParameter.T ags | The parameter - Tags should not be null | 参数Tags不能为空。 |
|---|---|---|---|
| 404 | MissingParameter.R egionId | The parameter - RegionId should not be null | 参数RegionId不能为空。 |
| 403 | PermissionDenied.T agOwnerUid | The specified operator not have permission to set TagOwnerUid value. | 无权设置标签归属者。 |
| 403 | PermissionDenied.S cope | The specified operator not have permission to set Scope value. | 指定的操作员无权设置范围值。 |
| 400 | NumberExceed.Res ourceIds | The ResourceIds parameter's number is exceed , Valid : 50 | 参数“ResourceIds”中包含的“ResourceId”不能超过 50 个。 |
| 400 | NumberExceed.Tags | The Tags parameter's number is exceed , Valid : 20 | 标签个数超过最大限制，本操作最多可以操作 20 个标签。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 404 | InvalidResourceId.N otFound | The specified ResourceIds are not found in our records. | 指定的资源不存在，请检查参数 ResourceId是否正确。 |
| 404 | InvalidResourceTyp e.NotFound | The ResourceType provided does not exist in our records. | 指定的资源类型不存在。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键参数有误。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值参数有误。 |
| 400 | OperationDenied.Qu otaExceed | The quota of tags on resource is beyond permitted range. | 资源标签已达上限。 |
| 403 | InvalidResourceId.N otSupported | The specified ResourceId does not support tagging. | 指定的资源ID不支持标记。 |
| 400 | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. | 指定的Tag.N.Key和Tag.N.Value不匹配。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域ID不存在。 |
| 400 | Invalid.Scope | The specified scope is invalid. | 可见范围参数无效。 |
| 403 | NoPermission.Tag | The operator is not permission for the tag. | 您没有操作该资源标签的权限。 |

##### UntagResources

调用UntagResources为指定的ECS资源列表统一解绑标签。解绑后，如果该标签没有绑定其他任何资源，会被自动删除。

**请求参数**

云服务器ECS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 否 | UntagResources | 系统规定参数。取值：UntagResources |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 资源所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ResourceId.N | RepeatLi st | 是 | i- bp67acfmxazb4p h*** | 资源ID，N的取值范围为1~50。 |
| ResourceType | String | 是 | instance | 资源类型。取值范围： instance：ECS实例。 disk：磁盘。 snapshot：快照。 image：镜像。 securitygroup：安全组。 volume：存储卷。 eni：弹性网卡。 ddh：专有宿主机。 keypair：SSH密钥对。 launchtemplate：启动模板。 |
| TagKey.N | RepeatLi st | 否 | FinanceDept | 资源的标签键。N的取值范围：1~20。 |
| All | Boolean | 否 | false | 是否解绑资源上全部的标签。当请求中未设置TagKey.N时，该参数才有效。取值范围： true false 默认值：false。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | C46FF5A8-C5F0- 4024-8262- B16B639225A0 | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &ResourceType=instance &ResourceId.1=i-bp1j6qtvdm8w0z1o0*** &TagKey.1=FinanceDept
```

`&<`公共请求参数> 正常返回示例云服务器ECS `XML` 格式

```xml
    <RequestId>C46FF5A8-C5F0-4024-8262-B16B639225A0</RequestId>
```

`JSON` 格式

```json
{
 "RequestId":"C46FF5A8-C5F0-4024-8262-B16B639225A0"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | %s | 提供的地域ID不存在。 |
| 404 | MissingParameter.T agOwnerUid | The parameter - TagOwnerUid should not be null | 参数“TagOwnerUid”不能为空。 |
| 404 | MissingParameter.T agOwnerBid | The parameter - TagOwnerBid should not be null | 参数“TagOwnerBid”不能为空。 |
| 404 | MissingParameter.R esourceType | The parameter - ResourceType should not be null | 参数“ResourceType”不能为空。 |
| 404 | MissingParameter.T ags | The parameter - Tags should not be null | 参数“Tags”不能为空。 |
| 404 | MissingParameter.R egionId | The parameter - RegionId should not be null | 参数“RegionId”不能为空。 |
| 403 | PermissionDenied.T agOwnerUid | The specified operator not have permission to set TagOwnerUid value. | 无权设置标签归属者。 |
| 403 | PermissionDenied.S cope | The specified operator not have permission to set Scope value. | 指定的操作员无权设置范围值。 |
| 400 | NumberExceed.Res ourceIds | The ResourceIds parameter's number is exceed , Valid : 50 | 参数“ResourceIds”中包含的“ResourceId”不能超过 50 个。 |
| 400 | NumberExceed.Tags | The Tags parameter's number is exceed , Valid : 20 | 标签个数超过最大限制，本操作最多可以操作 20 个标签。 |
| 400 | Duplicate.TagKey | The Tag.N.Key contain duplicate key. | 标签中存在重复的键，请保持键的唯一性。 |
| 404 | InvalidResourceId.N otFound | The specified ResourceIds are not found in our records. | 指定的资源不存在，请检查参数“ResourceId”是否正确。 |
| 404 | InvalidResourceTyp e.NotFound | The ResourceType provided does not exist in our records. | 指定的资源类型不存在。 |
| 400 | InvalidTagKey.Malfo rmed | The specified Tag.n.Key is not valid. | 指定的标签键不合法。 |
| 400 | InvalidTagValue.Mal formed | The specified Tag.n.Value is not valid. | 指定的标签值不合法。 |

云服务器ECS

| 400 | OperationDenied.Qu otaExceed | The quota of tags on resource is beyond permitted range. | 资源标签已达上限。 |
|---|---|---|---|
| 403 | InvalidResourceId.N otSupported | The specified ResourceId does not support tagging. | 指定的资源ID不支持标记。 |
| 400 | InvalidTag.Mismatch | The specified Tag.n.Key and Tag.n.Value are not match. | 指定的Tag.n.Key和Tag.n.Value不匹配。 |
| 400 | InvalidTagCount | The specified tags are beyond the permitted range. | 指定的标记超出取值范围。 |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 400 | Invalid.Scope | The specified scope is invalid. | 可见范围参数无效。 |
| 403 | NoPermission.Tag | The operator is not permission for the tag. | 您没有操作该资源标签的权限。 |

#### 其他接口

##### DescribeTasks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeTasks | 系统规定参数。取值：DescribeTasks |
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。 |
| PageNumber | Integer | 否 | 1 | 查询结果的页码，起始值为1，默认值为1。 |
| PageSize | Integer | 否 | 2 | 分页查询时设置的每页记录数，最大值100 行，默认值为10。 |
| TaskIds | String | 否 | t- bp1hvgwromzv32 iq****,t- bp179lofu2pv768 w**** | 任务ID，单次最多支持指定100个，ID之间使用半角逗号（,）分隔。 |
| TaskAction | String | 否 | ImportImage | 任务操作的接口名称。取值范围： ImportImage：导入镜像。 ExportImage：导出镜像。 |

云服务器ECS

| TaskStatus | String | 否 | Finished | 任务状态。取值范围： Finished：已完成。 Processing：运行中。 Pending：等待执行。 Deleted：已取消。 Paused：暂停。 默认值：无。 |
|---|---|---|---|---|
| StartTime | String | 否 | 2015-11- 23T15:10:00Z | 按创建时间查询，创建时间区间的起始点。 按照ISO8601标准表示，并需要使用UTC +0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |
| EndTime | String | 否 | 2015-11- 23T15:16:00Z | 按创建时间查询，创建时间区间的终止点。 按照ISO8601标准表示，并需要使用UTC +0时间，格式为yyyy-MM- ddTHH:mm:ssZ。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 2 | 当前分页包含多少条目。 |
| RegionId | String | cn-qingdao-env17- d01 | 地域ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TaskSet | Array of Task |  | 任务集合。 |
| Task |  |  |  |
| CreationTime | String | 2015-11-24T12:50Z | 创建时间。 |
| FinishedTime | String | 2015-11-24T12:50Z | 结束时间。 |
| SupportCancel | String | true | 是否支持取消任务。 |
| TaskAction | String | IMPORT IMAGE _ | 任务名称。 |
| TaskId | String | t- bp1hvgwromzv32iq* *** | 任务ID。 |

云服务器ECS

| TaskStatus | String | Finished | 任务状态。 |
|---|---|---|---|
| TotalCount | Integer | 2 | 列表条目数。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &PageNumber=1 &PageSize=2 &TaskIds=t-bp1hvgwromzv32iq**** &TaskStatus=Finished &StartTime=2015-11-23T15:10:00Z &EndTime=2015-11-23T15:16:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <PageNumber>1</PageNumber>
    <TotalCount>2</TotalCount>
    <PageSize>2</PageSize>
    <RegionId>cn-qingdao-env17-d01</RegionId>
    <RequestId>E5C82807-5588-4661-9A96-350B206A7623</RequestId>
    <TaskSet>
        <Task>
            <CreationTime>2015-11-24T12:50Z</CreationTime>
            <FinishedTime>2015-11-24T12:50Z</FinishedTime>
            <SupportCancel>true</SupportCancel>
            <TaskStatus>Finished</TaskStatus>
            <TaskId>t-bp1hvgwromzv32iq****</TaskId>
        </Task>
        <Task>
            <CreationTime>2015-11-23T15:10Z</CreationTime>
            <FinishedTime>2015-11-23T15:16Z</FinishedTime>
            <SupportCancel>true</SupportCancel>
            <TaskStatus>Finished</TaskStatus>
            <TaskId>t-bp179lofu2pv768w****</TaskId>
        </Task>
    </TaskSet>
```

`JSON` 格式云服务器ECS

```json
{
    "PageNumber": 1,
    "TotalCount": 2,
    "PageSize": 2,
    "RegionId": "cn-qingdao-env17-d01",
    "TaskSet": [
        {
            "Task": [
                {
                    "CreationTime": "2015-11-24T12:50Z",
                    "FinishedTime": "2015-11-24T12:50Z",
                    "SupportCancel": true,
                    "TaskAction": "ImportImage",
                    "TaskStatus": "Finished",
                    "TaskId": "t-bp1hvgwromzv32iq****"
                },
                {
                    "CreationTime": "2015-11-23T15:10Z",
                    "FinishedTime": "2015-11-23T15:16Z",
                    "SupportCancel": true,
                    "TaskAction": "ImportImage",
                    "TaskStatus": "Finished",
                    "TaskId": "t-bp179lofu2pv768w****"
                }
```

]

```
        }
```

`],`

```json
    "RequestId": "F746C690-D9EA-4F87-AF31-8E1910FAB541"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | An input parameter "RegionId" that is mandatory for processing the request is not supplied. | 参数RegionId不得为空。 |
| 400 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域ID不存在。 |

##### CancelTask

**接口说明**

您能取消正在运行的以下任务：

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云服务器ECS

| Action | String | 是 | CancelTask | 系统规定参数，取值：CancelTask。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao- env17-d01 | 地域ID。您可以调用DescribeRegions查看最新的地域列表。 |
| TaskId | String | 是 | t-23ym6**** | 任务ID。您可以调用DescribeTasks查看任务ID列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-qingdao-env17-d01 &TaskId=t-23ym6mv****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>4BE2C7FE-C7A4-4675-A153-174E032AABFB</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "4BE2C7FE-C7A4-4675-A153-174E032AABFB"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParameter | An input parameter "RegionId" that is mandatory for processing the request is not supplied. | 参数RegionId不得为空。 |
| 400 | MissingParameter | An input parameter "TaskId" that is mandatory for processing the request is not supplied. | 参数TaskId不得为空。 |
| 400 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域ID不存在。 |

云服务器ECS

| 400 | InvalidTaskId.NotFo und | The specified "TaskId" is not found. | 指定的TaskId不存在。 |
|---|---|---|---|
| 403 | InvalidTaskId.TaskA ctionNotSupport | The specified task action not support. | 不支持指定的任务操作。 |
| 403 | InvalidTaskId.Incorr ectTaskStatus | The specified task status is not invalid. | 指定的任务状态不合法。 |
| 403 | CancelTaskFailed | The task is failed to cancel, Please contact the administrator. | 任务无法取消，请联系管理员。 |

##### DescribeTaskAttribute

您能查询以下异步任务：

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DescribeTaskAttribute | 系统规定参数，取值： DescribeTaskAttribute。 |
| RegionId | String | Query | 是 | cn-qingdao-env17-d01 | 地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| TaskId | String | Query | 是 | t-taskid | 任务ID。您可以调用 DescribeTasks查看任务 ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| OperationProgr essSet | Array | / | 返回任务包含的信息，其中包括每一个子任务的状态和相关信息。 |
| - RelatedItemSet | Array | / | 资源信息类型。 |
| --Name | String | OSSObject | 相关项名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Value | String | MYOSSPRE m- _ 23f8tcp*** t- _ 23ym6mv***.vhd | 相关项值。 |
| -ErrorMsg | String | The specified RegionId parameter is invalid. | 错误信息。 |
| -ErrorCode | String | ParameterInvalid | 错误代码。 |
| - OperationStatu s | String | Success | 操作状态。 |
| CreationTime | String | 2015-11-23T02:13Z | 任务创建时间。 |
| SupportCancel | String | true | 是否可以取消任务。取值范围： true：可以取消 false：无法取消 |
| TotalCount | Integer | 1 | 任务总数。 |
| SuccessCount | Integer | 1 | 成功任务数。 |
| RegionId | String | cn-qingdao-env17- d01 | 地域ID。 |
| TaskAction | String | ExportImage | 任务操作的接口名称。 |
| FailedCount | Integer | 0 | 失败任务数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TaskStatus | String | Finished | 任务状态。 |
| TaskProcess | String | 100% | 任务进程。 |
| FinishedTime | String | 2015-11-23T02:19Z | 任务完成时间。 |
| TaskId | String | t-taskid | 任务ID。 |

**示例**

请求示例云服务器ECS

```
https://ecs.example.com/?Action=DescribeTaskAttribute &RegionId=cn-qingdao-env17-d01 &TaskId=t-taskid
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "CreationTime": "2015-11-23T02:13Z",
    "OperationProgressSet": {
        "OperationProgress": [
            {
                "RelatedItemSet": {
                    "RelatedItem": [
                        {
                            "Name": "OSSBucket",
                            "Value": "image-temp"
                        },
                        {
                            "Name": "OSSObject",
                            "Value": "MYOSSPRE_m-23f8tcp***_t-23ym6mv***.vhd"
                        },
                        {
                            "Name": "ImageFormat",
                            "Value": "vhd"
                        }
```

]

```json
                },
                "ErrorMsg": "",
                "ErrorCode": "",
                "OperationStatus": "Success"
            }
```

]

```json
    },
    "FinishedTime": "2015-11-23T02:19Z",
    "FailedCount": 0,
    "SupportCancel": true,
    "TotalCount": 1,
    "SuccessCount": 1,
    "RequestId": "4BE2C7FE-C7A4-4675-A153-174E032AABFB",
    "RegionId": "cn-qingdao-env17-d01",
    "TaskAction": "ExportImage",
    "TaskStatus": "Finished",
    "TaskProcess": "100%",
    "TaskId": "t-23ym6mv***"
}
```

`XML` 格式云服务器ECS

```xml
    <CreationTime>2015-11-23T02:13Z</CreationTime>
    <OperationProgressSet>
        <OperationProgress>
            <RelatedItemSet>
                <RelatedItem>
                    <Name>OSSBucket</Name>
                    <Value>image-temp</Value>
                </RelatedItem>
                <RelatedItem>
                    <Name>OSSObject</Name>
                    <Value>MYOSSPRE_m-23f8tcp***_t-23ym6mv***.vhd</Value>
                </RelatedItem>
                <RelatedItem>
                    <Name>ImageFormat</Name>
                    <Value>vhd</Value>
                </RelatedItem>
            </RelatedItemSet>
            <ErrorMsg></ErrorMsg>
            <ErrorCode></ErrorCode>
            <OperationStatus>Success</OperationStatus>
        </OperationProgress>
    </OperationProgressSet>
    <FinishedTime>2015-11-23T02:19Z</FinishedTime>
    <FailedCount>0</FailedCount>
    <SupportCancel>true</SupportCancel>
    <TotalCount>1</TotalCount>
    <SuccessCount>1</SuccessCount>
    <RequestId>EF0C5969-279B-49C8-AD83-BACCC74DD38C</RequestId>
    <RegionId>cn-qingdao-env17-d01</RegionId>
    <TaskStatus>Finished</TaskStatus>
    <TaskProcess>100%</TaskProcess>
    <TaskId>t-23ym6mv***</TaskId>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.NotF ound | The specified RegionId does not exist. | 指定的地域 ID 不存在。 |
| 400 | MissingParameter | An input parameter "RegionId" that is mandatory for processing the request is not supplied. | 参数 RegionId 不得为空。 |
| 400 | MissingParameter | An input parameter "TaskId" that is mandatory for processing the request is not supplied. | 参数 TaskId 不得为空。 |
| 400 | InvalidTaskId.NotFo und | The specified "TaskId" is not found. | 指定的 TaskId 不存在。 |

云服务器ECS

#### 附录

##### 资源术语

本文档对ECS的API操作中可能涉及到的术语进行了说明。

**术语表**

本文可能涉及的术语解释如下所示：

| 术语 | 全称 | 中文 | 说明 |
|---|---|---|---|
| Instance | ECS Instance | 弹性计算服务实例，简称实例。 | 是一个通过物理服务器，采用虚拟化技术虚拟出来的计算机。 |
| Region |  | 地域 | 代表资源所在的地域，每个地域包含一组可用区。 |
| Zone | Availability Zone | 可用区 | 同一地域内，电力和网络互相独立的物理区域。同一可用区内的ECS实例网络延时更小。在同一地域内可用区与可用区之间内网互通，可用区之间能做到故障隔离。 |
| Image | Image File | 镜像文件，简称镜像 | 操作系统和应用软件都可以制作成镜像文件，用户可以选择某镜像文件来初始化云服务器实例。镜像是创建实例的必要条件。新创建实例的系统盘内容是镜像内容的完全拷贝，包括操作系统，软件配置等内容。因此，创建不同操作系统版本的实例需要选择不同的镜像文件。 |
| Disk |  | 磁盘 | 实例所使用的存储设备。 |
| Snapshot |  | 快照 | 为磁盘创建的数据还原点，包含特定时刻磁盘的数据，可以用于还原磁盘数据或创建自定义镜像。 |
| IP |  | IP 地址 | 互联网上的公网IP地址。 |
| SecurityGro up | Security Group | 安全组 | 实例相关的安全组，可以使用安全组制定安全策略，一个实例必须属于某个安全控制组，也可以属于多个安全组，组中的实例继承安全组的安全策略 |
| CIDR | Classless Inter-Domain Routing | 无类别域间路由选择 | 是互联网中一种新的寻址方式，与传统的A类、B类和C类寻址模式相比，CIDR在IP地址分配方面更为高效。 例如IP号段是10.203.96.0~10.203.127.255，转化CIDR格式就是找相同的前十九位： 10.203.0110 0000.0000 0000到10.203.0111 1111.1111 1111可以写成10.203.96.0/19 |

**限制说明**

在ECS中，对用户可拥有的实例、安全组等资源的数量均有限制。 对实例规格、实例上挂载的磁盘数量、磁盘大小、磁盘的快照数量等方面也有限制。

##### 实例状态

表 1. 状态说明

| 状态名 | 状态说明 |
|---|---|
| Pending | 任务创建中 |
| Stopped | 停止 |

云服务器ECS

| Starting | 启动中 |
|---|---|
| Running | 运行中 |
| Stopping | 停止中 |

图 1. 状态图说明

##### 公共错误码

表 1. 代码说明

| 错误代码 | Http 状态码 | 错误信息 |
|---|---|---|
| IdempotentParameterMismatch | 400 | The request is retried with updated parameters. |
| IllegalTimestamp | 400 | The input parameter "Timestamp" that is mandatory for processing this request is not supplied. |
| IncompleteSignature | 400 | The request signature does not conform to Aliyun standards. |
| InvalidAccessKeyId.NotFound | 400 | The Access Key ID provided does not exist in our records. |
| InvalidOwner | 400 | OwnerId and OwnerAccount can't be used at one API access. |
| InvalidOwnerId | 400 | The specified OwnerId is not valid. |
| InvalidOwnerAccount | 400 | The specified OwnerAccount is not valid. |
| InvalidParamater | 400 | The specified parameter "SignatureMethod" is not valid. |
| InvalidParamater | 400 | The specified parameter "SignatureVersion" is not valid. |
| InvalidParameter | 400 | The specified parameter "Action or Version" is not valid. |
| InvalidParameter | 400 | The specified parameter is not valid. |
| InvalidParameter.IsNull | 400 | The required parameter must be not null. |

云服务器ECS

| MissingParameter | 400 | The input parameter "Action" that is mandatory for processing this request is not supplied. |
|---|---|---|
| MissingParameter | 400 | The input parameter "AccessKeyId" that is mandatory for processing this request is not supplied |
| MissingParameter | 400 | An input parameter "Signature" that is mandatory for processing the request is not supplied. |
| MissingParameter | 400 | The input parameter "Timestamp" that is mandatory for processing this request is not supplied. |
| MissingParameter | 400 | The input parameter "Version" that is mandatory for processing this request is not supplied. |
| SignatureNonceUsed | 400 | The request signature nonce has been used. |
| Throttling | 400 | You have made too many requests within a short time; your request is denied due to request throttling. |
| UnsupportedParameter | 400 | The parameter is unsupported. |
| UnknownError | 400 | The request processing has failed due to some unknown error. |
| Forbidden.AccessKeyDisabled | 403 | The Access Key is disabled. |
| Forbidden.NotSupportRAM | 403 | This action does not support accessed by RAM mode. |
| Forbidden.RAM | 403 | User not authorized to operate the specified resource, or this API doesn't support RAM. |
| Forbidden.RiskControl | 403 | This operation is forbidden by Aliyun Risk Control system. |
| Forbidden.SubUser | 403 | The specified action is not available for you。 |
| Forbidden.Unauthorized | 403 | User not authorized to operate on the specified resource. |
| InvalidAccount.NotFound | 403 | The specified Account does not exist. |
| InvalidAction | 403 | Specified action is not valid. |
| InvalidIdempotenceParameter.Mismatch | 403 | The specified parameters are different from before. |
| InvalidParameter.OwnerAccount | 403 | OwnerAccount is Invalid. |
| InvalidParameter.ResourceOwnerAccoun t | 403 | ResourceOwnerAccount is Invalid. |
| LastTokenProcessing | 403 | The last token request is processing. |

云服务器ECS

| MissingParameter | 403 | The input parameter OwnerId, OwnerAccount that is mandatory for processing this request is not supplied. |
|---|---|---|
| RealNameAuthenticationError | 403 | Your account has not passed the real-name authentication yet. |
| UnsupportedHTTPMethod | 403 | This http method is not supported. |
| InvalidDiskId.NotFound | 404 | The specified DiskId does not exist. |
| InvalidImageId.NotFound | 404 | The specified ImageId does not exist. |
| InvalidInstanceId.NotFound | 404 | The specified InstanceId does not exist. |
| InvalidRegionId.NotFound | 404 | The specified RegionId does not exist. |
| InvalidSecurityGroupId.NotFound | 404 | The specified SecurityGroupId does not exist. |
| InvalidSnapshotId.NotFound | 404 | The specified SnapshotId does not exist. |
| OperationConflict | 409 | Request was denied due to conflict with a previous request. |
| InternalError | 500 | The request processing has failed due to some unknown error, exception or failure. |
| ServiceUnavailable | 500 | The request has failed due to a temporary failure of the server. |
| ServiceUnavailable.RegionMaintaining | 503 | System maintenance is in progress on the selected region, please wait a few minutes before trying again. |

##### 云盘类型

本文描述了云服务器ECS支持的云盘类型及其相关信息。

| 云盘类型 | 参数取值（DiskCategory） | 单块最大容量 |
|---|---|---|
| SSD盘 | cloud ssd _ | 32768 GB |
| 共享SSD盘 | san ssd _ | 32768 GB |
| 高效云盘 | cloud efficiency _ | 32768 GB |
| 共享高效云盘 | san efficiency _ | 32768 GB |
| 普通性能云盘 | cloud sperf _ | 32768 GB |
| 高性能云盘 | cloud pperf _ | 32768 GB |

更多云盘信息，请参见**《云服务器****ECS** **用户指南》**中的**《云盘概述》**章节。

##### 如何保证幂等性

当通过调用创建实例接口在 ECS 中创建云服务器时，如果遇到了请求超时或服务器内部错误时，客户端可能会尝试重发请求，这时客户端可以通过提供可选参数**ClientToken**避免服务器创建出比预期要多的实例，也就是通过提供**ClientToken**参数保证请求的幂等性。 云服务器ECS
**ClientToken**是一个由客户端生成的唯一的、大小写敏感、不超过64个ASCII字符的字符串。
如果用户使用同一个**ClientToken**值调用创建实例接口，则服务端会返回相同的请求结果，包含相同的**InstanceId**。因此用户在遇到错误进行重试的时候，可以通过提供相同的**ClientToken**值，来确保 ECS 只创建一个实例，并得到这个实例的**InstanceId**。 如果用户提供了一个已经使用过的**ClientToken**，但其他请求参数不同，则ECS会返回**IdempotentParameterMismatch**的错误代码。但需要注意的是，**SignatureNonce**、**Timestamp**和**Signature**参数在重试时是需要变化的，因为 ECS 使用**SignatureNonce**来防止重放攻击，使用**Timestamp**来标记每次请求时间，所以再次请求必须提供不同的**SignatureNonce**和**Timestamp**参数值，这同时也会导致**Signature**值的变化。 通常，客户端只需要在500（InternalError）或503（ServiceUnavailable）错误、或者无法得到响应结果的情况下进行重试操作。返回结果是200时，重试可以得到上次相同的结果，但不会对服务端状态带来任何影响。 而对 4xx 的返回错误，除非提示信息里明确出现“try it later”，通常重试也是不能成功的。

##### 实例被安全锁定时API的行为

被安全锁定指的是在DescribeInstanceAttribute返回的传出参数中的OperationLocks包含了LockReason: security。 和磁盘有关的行为在In_use的状态下依赖实例的OperationLocks，否则可以忽略实例的OperationLocks。 表 1. 行为接口说明

| 接口 | 行为 |
|---|---|
| AttachDisk | 报错 |
| AuthorizeSecurityGroup | 正常逻辑 |
| CreateDisk | 正常逻辑 |
| CreateImage | 正常逻辑 |
| CreateInstance | - |
| CreateSecurityGroup | 正常逻辑 |
| CreateSnapshot | 报错（只针对挂载在该实例上的磁盘，为运行中状态） |
| DeleteDisk | 正常逻辑 |
| DeleteImage | 正常逻辑 |
| DeleteInstance | 正常逻辑 |
| DeleteSecurityGroup | 正常逻辑 |
| DeleteSnapshot | 正常逻辑 |
| DescribeAutoSnapshotPolicy | 正常逻辑 |
| DescribeDisks | 正常逻辑 |
| DescribeImages | 正常逻辑 |
| DescribeInstanceAttribute | 正常逻辑 |
| DescribeInstanceStatus | 正常逻辑 |
| DescribeInstanceTypes | 正常逻辑 |

云服务器ECS

| DescribeInstanceMonitorData | 正常逻辑 |
|---|---|
| DescribeRegions | 正常逻辑 |
| DescribeSecurityGroupAttribute | 正常逻辑 |
| DescribeSecurityGroups | 正常逻辑 |
| DescribeSnapshotAttribute | 正常逻辑 |
| DescribeSnapshots | 正常逻辑 |
| DescribeZones | 正常逻辑 |
| DetachDisk | 报错 |
| JoinSecurityGroup | 报错 |
| LeaveSecurityGroup | 报错 |
| ModifyAutoSnapshotPolicy | 正常逻辑 |
| ModifyDiskAttribute | 正常逻辑 |
| ModifyInstanceAttribute | 报错 |
| RebootInstance | 报错 |
| ReInitDisk | 报错(In use)，正常逻辑（其他状态） _ |
| ReplaceSystemDisk | 正常逻辑 |
| ResetDisk | 报错 |
| RevokeSecurityGroup | 正常逻辑 |
| StartInstance | 报错 |
| StopInstance | 报错 |

##### 时间格式ISO8601

和时间的表示方法》，ECS Open API 的时间格式采用 ISO8601 格式。 云服务器ECS

## 附录

### STS概要

#### 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和 RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

**使用RAM用户扮演角色时获取STS Token**

有权限的RAM用户可以使用其访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用 STS Token访问阿里云资源。

**产品优势**

使用STS Token，减少长期访问密钥（Accesskey）泄露的风险。 STS Token具有时效性，可以自定义有效期，到期后将自动失效，无需定期轮换。 可以为STS Token绑定自定义权限策略，提供更加灵活和精细的云资源授权。

#### AssumeRole

RAM用户调用AssumeRole接口获取一个扮演RAM角色的临时身份凭证STS Token。该接口中RAM用户扮演的是可信实体为阿里云账号类型的RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssumeRole | 要执行的操作。取值：AssumeRole |
| RoleArn | String | 是 | acs:ram::1234567 89012****:role/ad minrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM角色。 |
| RoleSessionNam e | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该 API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-）和下划线（ ）。 _ |

云服务器ECS

| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource ": ["*"]}],"Version":" 1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 如果指定该权限策略，则STS Token最终的权限策略取RAM角色权限策略与该权限策略的交集。 如果不指定该权限策略，则STS Token最终的权限策略取RAM角色的权限策略。 长度为1~1024个字符。 |
|---|---|---|---|---|

##### 返回结果

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | 无 | 无 | 访问凭证。 |
| AccessKeyId | String | STS.L4aBSCSJVMuKg 5U1**** | 访问密钥ID。 |
| AccessKeySecret | String | ****************************************** | 访问密钥。 |
| SecurityToken | String | ******** | 安全令牌。 |
| Expiration | String | 2015-04- 09T11:52:19Z | 失效时间。 |
| AssumedRoleUser | 无 | 无 | 角色扮演时的临时身份。 |
| Arn | String | acs:ram::123456789 012****:role/adminro le/alice | 临时身份的ARN。 |
| AssumedRoleId | String | 34458433936495*** *:alice | 临时身份的ID。 |

**示例**

**引入Pom依赖**

操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下： 云服务器ECS

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

```
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKey
ID>", "<yourAccessKeySecret>");
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

`//` 获取到`STS`三元组云服务器ECS

```java
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + sts
Token);
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

云服务器ECS

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile;
    public static void main(String[] args) {
```

`// "<yourRegionID>"`替换为真实的`RegionID` `// "<yourStsAccesskey>", "<yourStsAccessKeySecret>"`替换为上面获取到的`STS`三元组中`stsAk`、s

```
tsSk
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccess
Key>", "<yourStsAccessKeySecret>");
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

云服务器ECS

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.RoleAr n | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.RoleS essionName | The parameter RoleSessionName is wrongly formed. | RoleSessionName格式错误，支持输入2~64个字符，请输入至少2个字符， 允许输入英文字母、数字、 半角句号（.）、 at（@）、短划线（-）和下划线（ ）。 _ |
| 400 | InvalidParameter.Durati onSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | DurationSeconds参数设置错误，过期时间最小值为900秒，最大值为MaxSessionDuratio n设置的时间。 |
| 400 | InvalidParameter.Policy Grammar | The parameter Policy has not passed grammar check. | 权限策略语法错误。 |
| 400 | InvalidParameter.Policy Size | The size of Policy must be smaller than 1024 bytes. | 权限策略长度超限，最大不超过1024字符。 |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | STS Token没有权限。 |
| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
