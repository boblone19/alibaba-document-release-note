---
title: "云安全中心（态势感知） 云安全管理中心开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 262
source_pdf: "36_云安全管理中心开发指南_developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sas/zh/developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云安全中心（态势感知） 云安全管理中心开发指南

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
2. 根据专有云的版本单击**飞天企业版**、**敏捷版****&XStack**或**一体机**页签。
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

### 登录开发者门户控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器

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

### 查看API信息

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本，在通过SDK调用API接口时需要填写上述信息。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏单击
图标，进入**帮助与开放平台**。
3. 在顶部菜单栏**产品文档**的下拉列表中，选择**API****调试**。
4. 在左侧导航栏中选择目标云产品。在下方API列表中可浏览当前API版本中的所有API接口名称。若当前云
产品存在多个API版本，可在**版本**下拉列表中，选择目标API版本。

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
|---|---|
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

### 获取Endpoint

本文介绍如何获取云盾各产品的Endpoint。

**背景信息**

通过POP网关调用API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。您也

**操作步骤**

1. 登录飞天基础运维平台。
2. 在顶部菜单栏，选择**产品运维** > **飞天基础运维平台**。
3. 在左侧导航栏，单击**产品集群运维**。
4. 在**产品** | **集群**搜索框输入sas-securityoperationscentercluster，单击**集群详情**。
5. 在**服务列表**页签，单击服务名称。
6. 在**组件列表**页点击 **yundun-soc**组件，单击**注册变量**，搜索yundunsoc.pop.endpoint，对应的值即
为业务域的Endpoint。
7. 云产品的Endpoint构成格式为：

```
${EndpointPre}.${global:region}.${global:internet-domain}
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

**说明**

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式 （CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
阿里云产品的API有RPC和RESTful两种风格，不同风格的API的CommonRequest的调用方法也不同。 通常API参数中包含Action参数的是RPC风格，包含PathPattern参数的是RESTful风格。一般情况下，每个产品内，所有API的调用风格是统一的。每个API仅支持特定的一种风格调用，传入错误的标识，可能会调用到其他API，或收到 `ApiNotFound` 的错误信息。 发起一次CommonRequest请求，您需要获取以下几个参数的值。关于以下参数的更多说明，请参见API公共参数。 接入点（endpoint）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 接口信息：要调用的接口名称。 当调用的API为RPC风格（大部分阿里云产品API为RPC风格，如Sas）时，需要获取Action参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 当调用的API为RESTful风格（如容器服务）时，需要获取PathPattern参数，使用 `request.PathPattern = "<PathPattern>"` 的方式来指定RESTful路径。

**示例：调用RPC风格的API**

以下代码展示了如何使用CommonRequest的方式调用云盾的接口：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // 您的地域ID
            "<YOUR-ACCESS-KEY-ID>",      // 您的AccessKey ID
            "<YOUR-ACCESS-KEY-SECRET>"); // 您的AccessKey Secret
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```java
        CommonRequest request = new CommonRequest();
        request.setDomain("<YOUR-ENDPOINT>");// 当前产品实际的Endpoint
        request.setVersion("<API-version>");// 接口的版本
        request.setAction("<YOUR-ACTION>");// 接口的名称
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

##### 使用CommonRequest进行调用

**说明**

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式 （CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
阿里云产品的API有RPC和RESTful两种风格，不同风格的API的CommonRequest的调用方法也不同。 通常API参数中包含Action参数的是RPC风格，包含PathPattern参数的是RESTful风格。一般情况下，每个产品内，所有API的调用风格是统一的。每个API仅支持特定的一种风格调用，传入错误的标识，可能会调用到其他API，或收到 `ApiNotFound` 的错误信息。 发起一次CommonRequest请求，您需要获取以下几个参数的值。关于以下参数的更多说明，请参见API公共参数。 接入点（endpoint）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 接口信息：要调用的接口名称。 当调用的API为RPC风格（大部分阿里云产品API为RPC风格，如Sas）时，需要获取Action参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 当调用的API为RESTful风格（如容器服务）时，需要获取PathPattern参数，使用 `request.PathPattern = "<PathPattern>"` 的方式来指定RESTful路径。

**示例：调用RPC风格的API**

以下代码展示了如何使用CommonRequest的方式调用接口：

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<YOUR-ENDPOINT>') //当前产品实际的Endpoint request.set_version('<API-version>') //接口的版本 request.set_action_name('<YOUR-ACTION>')//接口的名称
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

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

**说明**

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式 （CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
阿里云产品的API有RPC和RESTful两种风格，不同风格的API的CommonRequest的调用方法也不同。 通常API参数中包含Action参数的是RPC风格，包含PathPattern参数的是RESTful风格。一般情况下，每个产品内，所有API的调用风格是统一的。每个API仅支持特定的一种风格调用，传入错误的标识，可能会调用到其他API，或收到 `ApiNotFound` 的错误信息。 发起一次CommonRequest请求，您需要获取以下几个参数的值。关于以下参数的更多说明，请参见API公共参数。 接入点（endpoint）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 接口信息：要调用的接口名称。 当调用的API为RPC风格（大部分阿里云产品API为RPC风格，如Sas）时，需要获取Action参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 当调用的API为RESTful风格（如容器服务）时，需要获取PathPattern参数，使用 `request.PathPattern = "<PathPattern>"` 的方式来指定RESTful路径。

**示例：使用RPC风格的API**

以下代码展示了如何使用CommonRequest的方式调用接口：

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("cn-hangzhou", "{your_access_key_id}", "{
your_access_key_secret}")
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Domain = "<YOUR-ENDPOINT>"// 当前产品实际的Endpoint
    request.Version = "<API-version>"// 接口的版本
    request.ApiName = "<YOUR-ACTION>"// 接口的名称
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

数

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

数

| Product | Strin g | 是 | 接口对应的产品名称。取值： Auditprivate：云盾基础组件。 yundunnextsoc：云安全管理中心（SOC）。 Sas：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy：网络流量检测与响应。 Ddosprivate：DDos 清洗。 hsm-private：加密服务。 Cloudfw：云防火墙。 Sddp：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |
|---|---|---|---|
| EndpointPre | Strin g | 是 | 接口对应的域名前缀。取值： auditprivate：云盾基础组件。 yundunnextsoc-pop：云安全管理中心（SOC）。 tds：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy-share：网络流量检测与响应。 ddosprivate：DDos 清洗。 hsmprivate：加密服务。 cloudfw：云防火墙。 sddp-api：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

## 云安全管理中心（SOC）

### 调用方式

#### 请求结构

**请求结构说明**

其中： `endpoint` ，表示调用的云服务接入点，云安全管理中心（SoC）的接入点为 `yundunnewsoc-pop.`

```
[RegionId].example.com 。
```

**说明**

`Action` ，表示要执行的操作，即接口名。 例如， `Action=GetEcsProtectCount` 表示通过GetEcsProtectCount接口查询ECS保护状态的在线数及异常离线数。

#### 签名机制

云盾服务会对每个访问的请求进行身份验证，所以无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。

**API签名**

为保证API的安全调用，在调用API时阿里云会对每个API请求通过签名（Signature）进行身份验证。当您手动发起API请求时，需要按照RFC 2104的定义，使用AccessSecret对编码、排序后的整个请求串计算 HMAC值作为签名。 本章节以如下原始访问参数为例，说明API签名制作的流程：

| 参数 | 内容 |
|---|---|
| 接入点 | http://yundunnewsoc-pop.[RegionId].example.com/? |
| API自定义参数 | Action=GetEcsProtectCount |
| 公共参数（不包含Signature） | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2019-07-23 &SignatureVersion=1.0 |

| Access Key Secret | <yourAccessKeySecret> |
|---|---|

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
| Version | String | 是 | API版本号，为日期形式：YYYY-MM-DD。 取值：2019-07-23 |

| AccessKeyId | String | 是 | 阿里云颁发给用户的访问服务所用的密钥 ID。 |
|---|---|---|---|
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

### 安全监控

#### DescribeAttacks

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 是 | DescribeAttacks | 系统规定参数。取值： DescribeAttacks。 |
| DataScop e | Integ er | Query | 否 | 1 | 区分平台侧或用户侧，取值： 0：表示平台侧。 1：表示用户侧。 |
| PageSize | Integ er | Query | 否 | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| PageNo | Integ er | Query | 否 | 1 | 分页查询时，设置当前页面的页码。 |
| SourceFro m | Integ er | Query | 否 | 41 | 攻击防护的数据来源。取值： 40：Web应用防火墙。 41：云防火墙。 42：DDoS防护 （aliguard）。 44：流量安全监控 （IDS）。 46：态势感知（暴力破解防护）。 |
| UserId | Long | Query | 否 | 2956140888888888 | 组织ID。 |

|  |  |  |  | 云安全 | 管理中心开发指南·云安全管理中心（SOC） |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AttackTyp e | Strin g | Query | 否 | 暴力破解 | 攻击类型。取值：暴力破解 、非 Web 攻击 、SQL 注入等。 |
| ProcessSt ate | Integ er | Query | 否 | 1 | 处理状态。取值： 2：已告警。 1：已防御。 3：清洗中。 4：清洗结束。 |
| StartTime | Long | Query | 否 | 1641398400000 | 攻击开始时间的最小值，单位为毫秒。 |
| EndTime | Long | Query | 否 | 1643644800000 | 攻击开始时间的最大值，单位为毫秒。 |
| Keyword | Strin g | Query | 否 | 192.168.XX.XX | 攻击名称或资产名称，资产 IP。 |
| Asset | Strin g | Query | 否 | ae3ef6ef-8888-4aee- 8bac-19879e68**** | 资产ID。 |
| Lang | Strin g | Query | 否 | zh CN _ | 请求和接收消息的语言类型。取值： zh CN：简体中文。 _ zh TW：繁体中文。 _ en US：英文。 _ |
| AssetType | Strin g | Query | 否 | ECS | 受影响资产类型。 如：ECS ，SLB ，OS S ，EIP ，RDS 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | 本次调用请求的ID。 |
| Data | Struct |  | 数据集合。 |
| -Items | Array |  | 数据列表。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --AttackerIp | String | 10.0.X.X | 攻击者IP。 |
| --AttackType | Integer | 1 | 攻击类型。 |
| --AttackId | Integer | 10154212 | 攻击ID。 |
| --ProcessState | Integer | 1 | 处理状态。取值： 2：已告警。 1：已防御。 3：清洗中。 4：清洗结束。 |
| --AttackTrait | String | 1 | 此参数已废弃。 |
| --SourceFrom | String |  | 攻击防护的数据来源。取值： 40：Web应用防火墙。 41：云防火墙。 42：DDoS防护（aliguard）。 44：流量安全监控（IDS）。 46：态势感知（暴力破解防护）。 |
| --UserId | Long | 295614088888888 8 | 组织ID。 |
| --UserName | String | 组织A | 组织名称。 |
| --RaisedTime | Long | 1641548505000 | 攻击时间。 |
| --AssetType | Integer | 1 | 受影响资产类型。 |
| --AttackName | String | zz 78**** _ | 攻击名称。 |
| --Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | 被攻击资产ID。 |
| -- SourceFromIp | String | 10.0.X.X | 数据来源IP。 |
| --TargetIp | String | 10.0.X.X | 攻击目标IP。 |
| --AssetName | String | SSH暴力**** | 被攻击资产名称。 |

|  |  |  | 云安全管理中心开发指南·云安全管理中心（SOC） |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- AssetPublicIps | String | 192.168.XX.XX | 受影响资产公网IP。 |
| -- AssetPrivateIp s | String | 192.168.XX.XX | 受影响资产私网IP。 |
| -Total | Integer | 20 | 符合条件的记录总数。 |
| -PageNo | Integer | 1 | 分页查询时，设置当前页面的页码。 |
| -PageSize | Integer | 10 | 分页查询时，指定每页最多显示的数据条数。 |

**示例**

请求示例

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeAttacks &DataScope=1 &PageSize=20 &PageNo=1
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"20","PageNo":"1","Items":[{"UserName":"组织 A","AttackTrait":"1","SourceFrom":"1","AttackType":"1","AttackerIp":"10.0.X.X","AssetName
```

`"SSH`暴力

```
****","SourceFromIp":"10.0.X.X","AssetPrivateIps":"192.168.XX.XX","ProcessState":"1","Ass
Type":"1","AttackId":"10154212","AttackName":"zz_78****","UserId":"2956140888888888","Ass PublicIps":"172.12.XX.XX","Asset":"ae3ef6ef-8888-4aee-8bac- 19879e68****","TargetIp":"10.0.X.X","RaisedTime":"1641548505000"}]}}
```

`XML` 格式

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>20</Total>
    <PageNo>1</PageNo>
    <Items>
        <UserName>组织A</UserName>
        <AttackTrait>1</AttackTrait>
        <SourceFrom>1</SourceFrom>
        <AttackType>1</AttackType>
        <AttackerIp>10.0.X.X</AttackerIp>
        <AssetName>SSH暴力****</AssetName>
        <SourceFromIp>10.0.X.X</SourceFromIp>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>1</AssetType>
        <AttackId>10154212</AttackId>
        <AttackName>zz_78****</AttackName>
        <UserId>2956140888888888</UserId>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <TargetIp>10.0.X.X</TargetIp>
        <RaisedTime>1641548505000</RaisedTime>
    </Items>
</Data>
```

#### DescribeAlarms

通过DescribeAlarms接口，指定条件查询用户侧和平台侧安全监控中安全告警列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAlarms | 系统规定参数。取值：DescribeAlarms。 |
| DataScope | Integer | 否 | 1 | 区分平台侧或租户侧，取值： 0：表示平台侧。 1：表示租户侧。 |
| PageSize | Integer | 否 | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| PageNo | Integer | 否 | 1 | 分页查询时，设置当前页面的页码。 |
| StartTime | Long | 否 | 1609430400000 | 告警开始发生时间最小值，单位为毫秒。 |

| EndTime | Long | 否 | 1645977600000 | 告警开始发生时间最大值，单位为毫秒。 |
|---|---|---|---|---|
| ProcessState | Integer | 否 | 1 | 处理状态。取值： 1：未处理。 2：已处理。 3：已忽略。 |
| RiskLevels.N | RepeatL ist | 否 | 1 | 风险等级范围。取值： 0：提醒。 1：可疑。 2：紧急，可以传多值，数组逗号分割如0，1，2。 |
| Keyword | String | 否 | 192.168.XX.XX | 搜索告警涉及的告警名称或资产名称、资产IP。 |
| SourceFrom | Integer | 否 | 20 | 数据来源标识。取值： 20：态势感知/安骑士。 |
| UserId | Long | 否 | 2956140888888 888 | 组织ID。 |
| AlarmType | String | 否 | 异常网络连接 | 告警类型，如：其他、异常网络连接、网站后门、进程异常行为、异常登录。 |
| Asset | String | 否 | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | 资产ID。 |
| Lang | String | 否 | zh CN _ | 请求和接收消息的语言类型。取值： zh CN：简体中文。 _ zh TW：繁体中文。 _ en US：英文。 _ |
| AssetType | String | 否 | ECS | 受影响资产类型。 如：ECS，SLB，OSS，EIP，RDS。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 数据集合。 |
| Items | Array of Item |  | 数据列表。 |

| AlarmId | Integer | 4008888 | 告警ID。 |
|---|---|---|---|
| AlarmName | String | 反弹** | 告警名称。 |
| AlarmType | String | 进程异常行为 | 告警类型，如：其他，异常网络连接，网站后门，进程异常行为，异常登录。 |
| AlarmUniqueIn fo | String | eeee98dd0c4cd5cc 61c016b2bdcf**** | 告警唯一键。 |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | 受影响资产ID。 |
| AssetName | String | zzzz 88**** _ | 受影响资产名称。 |
| AssetPrivateIp s | String | 192.168.XX.XX | 受影响资产私网IP。 |
| AssetPublicIps | String | 172.12.XX.XX | 受影响资产公网IP。 |
| AssetType | String | ECS | 受影响资产类型。 如：ECS，SLB，OSS，EIP，RDS。 |
| Detail | String | {"lastTime": 1641536460051,"a ssetsType": 0,"modifiedTime": "2022-01-07 14:21:00"} | 详情。 |
| LastTime | Integer | 1641537619 | 告警最近发生时间。单位为毫秒。 |
| ProcessState | Integer | 1 | 处理状态。取值： 1：未处理。 2：已处理。 3：已忽略。 |
| RaisedTime | Long | 1640931449000 | 告警首次发生时间。单位为毫秒。 |
| RiskLevel | Integer | 2 | 风险等级范围。取值： 0：提醒。 1：可疑。 2：紧急。 |

| SourceFrom | Integer | 20 | 数据来源标识。取值： 20：态势感知/安骑士。 |
|---|---|---|---|
| UserId | Integer | 295614088 | 组织ID。 |
| UserName | String | 组织A | 组织名称。 |
| PageNo | Integer | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Integer | 20 | 分页查询时，指定每页最多显示的数据条数。 |
| Total | Integer | 200 | 符合条件的记录总数。 |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeAlarms &RiskLevels=[0,1,2] &DataScope=1 &PageSize=20 &PageNo=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>20</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <AlarmId>4008888</AlarmId>
        <UserName>组织A</UserName>
```

`<AlarmType>`进程异常行为`</AlarmType>`

```xml
        <SourceFrom>20</SourceFrom>
        <AssetName>zzzz_88****</AssetName>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>ECS</AssetType>
        <AlarmName>反弹**</AlarmName>
        <UserId>295614088</UserId>
        <AlarmUniqueInfo>eeee98dd0c4cd5cc61c016b2bdcf****</AlarmUniqueInfo>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <RaisedTime>1640931449000</RaisedTime>
        <RiskLevel>2</RiskLevel>
        <Detail>{"lastTime": 1641536460051,"assetsType": 0,"modifiedTime": "2022-01-07
14:21:00"}</Detail>
        <LastTime>1641537619</LastTime>
    </Items>
</Data>
```

`JSON` 格式

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"20","Total":"200","PageNo":"1","Items": [{"AlarmId":"4008888","UserName":"组织A","AlarmType":"进程异常行为","SourceFrom":"20","AssetName":"zzzz_88****","AssetPrivateIps":"192.168.XX.XX","Proces tate":"1","AssetType":"ECS","AlarmName":"反弹
**","UserId":"295614088","AlarmUniqueInfo":"eeee98dd0c4cd5cc61c016b2bdcf****","AssetPubli
ps":"172.12.XX.XX","Asset":"ae3ef6ef-8888-4aee-8bac- 19879e68****","RaisedTime":"1640931449000","RiskLevel":"2","Detail":"{\"lastTime\": 164 1536460051,\"assetsType\": 0,\"modifiedTime\": \"2022-01-07 14:21:00\"}","LastTime":"1641537619"}]}}
```

#### DescribeVulFrangs

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulFran gs | 系统规定参数。取值：DescribeVulFrangs。 |

| RiskLevel | Integer | 否 | 1 | 漏洞等级,取值： 0：低危。 1：中危。 2：高危。 |
|---|---|---|---|---|
| ProcessState | Integer | 否 | 1 | 处理状态。取值： 1：未处理。 2：已处理。 |
| VulType | String | 否 | cve | 漏洞类型。取值：cve、sys、sca、emg等。 |
| PocFlag | Integer | 否 | 1 | 是否有POC。取值： 0：否。 1：是。 |
| PageSize | Integer | 否 | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| DataScope | Integer | 否 | 1 | 区分平台侧或用户侧。取值： 0：表示平台侧。 1：表示用户侧。 |
| UserId | Long | 否 | 2956140888888 888 | 组织ID。 |
| UsageLevel | String | 否 | LOW | 利用难度。 如：LOW，HIGH，MEDIUM，INSUF FICIENT INFO，NONE。 _ |
| StartTime | Long | 否 | 1641484800000 | 漏洞开始时间最小值，单位为毫秒。 |
| EndTime | Long | 否 | 1643644800000 | 漏洞开始时间最大值，单位为毫秒。 |
| Page | Integer | 否 | 1 | 分页查询时，设置当前页面的页码。 |
| NeedFix | String | 否 | necessity | 修复必要性。 |
| Keyword | String | 否 | 192.168.XX.XX | 漏洞名称或资产名称、资产IP。 |
| SourceFrom | Integer | 否 | 1 | 数据来源。取值： 1：安骑士主机漏洞。 |

| Asset | String | 否 | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | 漏洞涉及的资产ID。 |
|---|---|---|---|---|
| AssetType | String | 否 | ECS | 漏洞受影响资产类型。 如：ECS，SLB，OSS，EIP，RDS。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 数据集合。 |
| Items | Array of Item |  | 数据列表。 |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | 漏洞涉及的资产ID。 |
| AssetName | String | zzz 75**** _ | 漏洞影响的资产名称 |
| AssetPrivateIp s | String | 192.168.XX.XX | 受漏洞影响的资产私网IP。 |
| AssetPublicIps | String | 172.12.XX.XX | 受漏洞影响的资产公网IP。 |
| AssetType | String | ECS | 漏洞受影响资产类型。 如：ECS，SLB，OSS，EIP，RDS。 |
| Id | Long | 75489 | 数据ID。 |
| LastTime | String | 1642025151000 | 最近发现漏洞时间。单位为毫秒。 |
| NeedFix | String | necessity | 漏洞修复的必要性。 |
| ProcessState | Integer | 1 | 处理状态。取值： 1：未处理。 2：已处理。 |
| RaisedTime | Integer | 2022 | 发生时间。使用yyyy格式。 |
| RiskLevel | Integer | 1 | 漏洞等级。取值： 0：低危。 1：中危。 2：高危。 |

| SourceFrom | Integer | 1 | 数据来源。取值： 1：安骑士主机漏洞。 |
|---|---|---|---|
| SrcInnerName | String | oval:com.redhat.rh sa:def:2021**** | 漏洞名称。 |
| UsageLevel | String | LOW | 利用难度。 如：LOW，HIGH，MEDIUM，INSUFFICIE NT INFO，NONE。 _ |
| UserName | String | 组织A | 组织名称。 |
| VulName | String | RHSA-2021:1180- Mode**** | 漏洞名称。 |
| VulRelated | String | CVE-2017-100**** | 漏洞详情关联ID。 |
| VulType | String | cve | 漏洞类型。取值：cve、sys、sca、emg等。 |
| PageNo | Integer | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Integer | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| Total | Integer | 200 | 符合条件的记录总数。 |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeVulFrangs &DataScope=1 &PageSize=20 &Page=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <NeedFix>necessity</NeedFix>
        <UserName>组织A</UserName>
        <SourceFrom>1</SourceFrom>
        <VulName>RHSA-2021:1180-Mode****</VulName>
        <AssetName>zzz_75****</AssetName>
        <UsageLevel>LOW</UsageLevel>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>ECS</AssetType>
        <SrcInnerName>oval:com.redhat.rhsa:def:2021****</SrcInnerName>
        <VulRelated>CVE-2017-100****</VulRelated>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <Id>75489</Id>
        <RaisedTime>2022</RaisedTime>
        <RiskLevel>1</RiskLevel>
        <LastTime>1642025151000</LastTime>
        <VulType>cve</VulType>
    </Items>
</Data>
```

`JSON` 格式

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"200","PageNo":"1","Items": [{"NeedFix":"necessity","UserName":"组织A","SourceFrom":"1","VulName":"RHSA-2021:1180-Mo de****","AssetName":"zzz_75****","UsageLevel":"LOW","AssetPrivateIps":"192.168.XX.XX","Pr essState":"1","AssetType":"ECS","SrcInnerName":"oval:com.redhat.rhsa:def:2021****","VulRe ted":"CVE-2017-100****","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6ef-8888-4aee-8ba
```

`c-`

```
19879e68****","Id":"75489","RaisedTime":"2022","RiskLevel":"1","LastTime":"1642025151000" VulType":"cve"}]}}
```

#### DescribeHcFrangs

通过DescribeHcFrangs接口，根据指定条件查询用户侧安全监控的脆弱性风险（主机配置列表）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeHcFran gs | 系统规定参数。取值：DescribeHcFrangs。 |

| RiskLevel | Integer | 否 | 1 | 风险等级，取值如下： 0：低危。 1：中危。 2：高危。 |
|---|---|---|---|---|
| ProcessState | Integer | 否 | 1 | 处理状态。取值： 1：未处理。 2：已处理。 |
| HcType | String | 否 | 阿里云标准- Windows 2016/2019 安全基线检查 | 主机配置风险的类型。取值：阿里云标准- Windows 2016/2019 安全基线检查、阿里云标准-Apache Tomcat 安全基线检查、阿里云标准-CentOS Linux 7/8安全基线检查等。 |
| PageSize | Integer | 否 | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| StartTime | Long | 否 | 1641484800000 | 查询开始时间的最小值，单位为毫秒。 |
| EndTime | Long | 否 | 1643731200000 | 查询开始时间的最大值，单位为毫秒。 |
| Page | Integer | 否 | 1 | 分页查询时，设置当前页面的页码。 |
| Keyword | String | 否 | 192.168.XX.XX | 资产名称、资产IP。 |
| DataScope | Integer | 否 | 1 | 区分平台侧或租户侧。取值： 0：表示平台侧。 1：表示租户侧。 |
| UserId | Long | 否 | 2956140888888 888 | 组织ID。 |
| SourceFrom | Integer | 否 | 2 | 数据来源。取值： 2：主机配置核查。 |
| Asset | String | 否 | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | 资产ID。 |
| AssetType | String | 否 | ECS | 资产类型。 如：ECS，SLB，OSS，EIP，RDS。 |

| Lang | String | 否 | zh CN _ | 请求和接收消息的语言类型。取值： zh CN：简体中文。 _ zh TW：繁体中文。 _ en US：英文。 _ |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 数据集合。 |
| Items | Array of Item |  | 数据列表。 |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | 风险影响的资产ID。 |
| AssetName | String | zz 78**** _ | 风险影响的资产名称。 |
| AssetPrivateIp s | String | 192.168.XX.XX | 风险影响的资产私网IP。 |
| AssetPublicIps | String | 172.12.XX.XX | 风险影响的资产公网IP。 |
| AssetType | String | ECS | 风险影响的资产类型。 如：ECS，SLB，OSS，EIP，RDS。 |
| HcAsset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | 资产ID。 |
| HcName | String | CIS标准*** | 主机配置风险名称。 |
| HcType | String | 阿里云标准- Windows 2016/2019 安全基线检查 | 主机配置风险的类型。取值：阿里云标准- Windows 2016/2019 安全基线检查、阿里云标准-Apache Tomcat 安全基线检查、阿里云标准-CentOS Linux 7/8安全基线检查等。 |
| Id | Long | 65357 | 记录ID。 |
| LastFoundTim e | String | 1642042910000 | 最近发现风险时间。单位为毫秒。 |
| ProcessState | Integer | 2 | 风险处理状态。 取值： 1：已处理。 2：未处理。 |

| RiskLevel | Integer | 1 | 风险等级。取值如下： 0：低危。 1：中危。 2：高危。 |
|---|---|---|---|
| SourceFrom | String | 2 | 数据来源。取值： 2：主机配置核查。 |
| UserId | Long | 295614088888888 8 | 组织ID。 |
| UserName | String | 组织A | 组织名称。 |
| PageNo | Integer | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Integer | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| Total | Integer | 200 | 符合条件的记录总数。 |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeVulFrangs &DataScope=1 &PageSize=20 &Page=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <UserName>组织A</UserName>
        <SourceFrom>2</SourceFrom>
```

`<HcType>`阿里云标准`-Windows 2016/2019` 安全基线检查`</HcType>`

```xml
        <AssetName>zz_78****</AssetName>
        <HcAsset>ae3ef6ef-8888-4aee-8bac-19879e68****</HcAsset>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>2</ProcessState>
        <LastFoundTime>1642042910000</LastFoundTime>
        <AssetType>ECS</AssetType>
        <HcName>CIS标准***</HcName>
        <UserId>2956140888888888</UserId>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <Id>65357</Id>
        <RiskLevel>1</RiskLevel>
    </Items>
</Data>
```

`JSON` 格式

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"200","PageNo":"1","Items":[{"UserName":"组织
```

`A","SourceFrom":"2","HcType":"`阿里云标准`-Windows 2016/2019` 安全基线检

```
查","AssetName":"zz_78****","HcAsset":"ae3ef6ef-8888-4aee-8bac- 19879e68****","AssetPrivateIps":"192.168.XX.XX","ProcessState":"2","LastFoundTime":"16420 910000","AssetType":"ECS","HcName":"CIS标准
***","UserId":"2956140888888888","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6ef-8888
-4aee-8bac-19879e68****","Id":"65357","RiskLevel":"1"}]}}
```

### 运营大屏

#### QueryThreats

查询运营大屏威胁数据列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | QueryThreats | 系统规定参数。取值：QueryThreats。 |
| FromTime | Long | 否 | 1640944798076 | 威胁开始时间的最小值，单位为毫秒。 |

| ToTime | Long | 否 | 1641549603697 | 威胁开始时间的最大值，单位为毫秒。 |
|---|---|---|---|---|
| CurrentPage | Integer | 否 | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Integer | 否 | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| Index | String | 否 | threat | 数据index，固定为threat。 |
| UserIds | String | 否 | - 1,29561408888 8**** | 部门ID。支持平台值（固定取值为-1）、 租户组织ID。多个取值之间需用半角逗号分隔。 |
| Aliuid | Long | 否 | 1 | 此参数已废弃。 |
| Query | String | 否 | 192.168.XX.XX | 告警资产/攻击IP。 |
| ProcessStatus | String | 否 | 1 | 处置状态。取值： 1： 未处置。 2 ：已处置。 |
| ThreatLevel | String | 否 | 1 | 威胁级别。取值： 1：低。 2：中。 3：高。 |
| SrcFrom | String | 否 | 20,40 | 数据来源。可以多值，逗号分割。取值： 20：安骑士。 40：WAF。 41：云防火墙。 44：NDR。 |
| ThreatType | String | 否 | 进程异常行为 | 告警类型（攻击类型）。取值：非 Web 攻击、精准防御、web攻击、其他、进程异常行为等。 |
| ThreatName | String | 否 | 可疑编码命令 | 攻击名称。 |

| ProcessWay | String | 否 | 1 | 处置方式。取值： 0：放行。 1：拦截。 2：无动作。 3：手动处置。 4：一键封禁。 5：自动处置。 6：告警。 7：丢弃。 8：阻断。 |
|---|---|---|---|---|
| ThreatInoutside | String | 否 | 1 | 事件来源。取值： 1：内部攻击。 2：外部攻击。 |
| ThreatResult | String | 否 | 成功 | 攻击结果。如：企图，成功，失败。 |
| Lang | String | 否 | zh CN _ | 请求和接收消息的语言类型。取值： zh CN：简体中文。 _ zh TW：繁体中文。 _ en US：英文。 _ |
| Tag | String | 否 | 121 | 标签。 |
| DestinationIp | String | 否 | 192.168.XX.XX | 被攻击IP。 |
| ThreatSourceIp | String | 否 | 172.12.XX.XX | 攻击者来源（攻击者IP）。 |
| UrlHost | String | 否 | www.ecs****.co m | Web站点。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 分页查询时，设置当前页面的页码。 |
| Datas | List | {"lastTime":16415 49724000," logTi __ me":16415497242 87,"process way":" _ "} | 数组存储从Elasticsearch查出来的所有数据。 每个元素是一组数据。 |
| FromTime | Long | 1641484800000 | 威胁开始时间的最小值，单位为毫秒。 |

| HistogramInter val | Long | 0 | 直方图区间。 |
|---|---|---|---|
| PageSize | Integer | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | 本次调用请求的ID。 |
| ToTime | Long | 1641550177290 | 威胁开始时间的最大值，单位为毫秒。 |
| Total | Integer | 200 | 符合条件的总记录数。 |

**示例**

请求示例

```
&CurrentPage=1 &PageSize=10 &FromTime=1641484800000 &ToTime=1641550177290
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ToTime>1641550177290</ToTime> <PageSize>10</PageSize> <RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <HistogramInterval>0</HistogramInterval> <CurrentPage>1</CurrentPage> <Datas>{"lastTime":1641549724000,"__logTime":1641549724287,"process_way":""}</Datas> <Total>200</Total> <FromTime>1641484800000</FromTime>
```

`JSON` 格式

```json
{"ToTime":"1641550177290","PageSize":"10","RequestId":"8010791A-3154-4154-ACB2-866E56A6
****","HistogramInterval":"0","CurrentPage":"1","Datas":"
{\"lastTime\":1641549724000,\"__logTime\":1641549724287,\"process_way\":\"\"}","Total":"2 ","FromTime":"1641484800000"}
```

#### QueryThreatChartData

查询运营大屏相关图表数据。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | QueryThreatCha rtData | 系统规定参数。取值：QueryThreatChartData。 |
| FromTime | Long | 否 | 1640944798076 | 查询开始时间的最小值，单位为毫秒。 |
| ToTime | Long | 否 | 1641549603697 | 查询开始时间的最大值，单位为毫秒。 |
| CurrentPage | Integer | 否 | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Integer | 否 | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| Index | String | 否 | threat | 数据index，固定为threat。 |
| Aliuid | Long | 否 | 1 | 此参数已废弃。 |
| UserIds | String | 否 | - 1,29561408888 8**** | 部门ID。支持平台值（固定取值为-1）、 租户组织ID。多个取值之间需用半角逗号分隔。 |
| Query | String | 否 | 192.168.XX.XX | 告警资产/攻击IP。 |
| ProcessStatus | String | 否 | 1 | 处置状态。取值： 1：未处置。 2：已处置。 |
| ThreatLevel | String | 否 | 1 | 威胁级别。取值： 1：低。 2：中。 3：高。 |
| SrcFrom | String | 否 | 20,40 | 数据来源。可以多值，逗号分割。取值： 20：安骑士。 40：WAF。 41：云防火墙。 44：NDR。 |
| ThreatType | String | 否 | 进程异常行为 | 告警类型（攻击类型）。取值：非 Web 攻击、精准防御、web攻击、其他、进程异常行为等。 |

| ThreatName | String | 否 | 可疑编码命令 | 攻击名称。 |
|---|---|---|---|---|
| ProcessWay | String | 否 | 1 | 处置方式。取值： 0：放行。 1：拦截。 2：无动作。 3：手动处置。 4：一键封禁。 5：自动处置。 6：告警。 7：丢弃。 8：阻断。 |
| ThreatInoutside | String | 否 | 1 | 事件来源。取值： 1：内部攻击。 2：外部攻击。 |
| ThreatResult | String | 否 | 成功 | 攻击结果。如：企图，成功，失败。 |
| Properties | String | 否 | {"x type":"term" _ ,"y config 1":"sr _ _ c from,count"} _ | JSON。 查询图表的规则，JSON结构，格式 {"x type":"term"（横坐 _ 标）,"y config 1":"src from（纵坐 _ _ _ 标）,count（统计数量）"}。 |
| ChartType | String | 否 | pie | 图表类型。 如：histogram，bar，line，pie，ta ble，value。 |
| Lang | String | 否 | zh CN _ | 请求和接收消息的语言类型。取值： zh CN：简体中文。 _ zh TW：繁体中文。 _ en US：英文。 _ |
| Tag | String | 否 | tem | 标签。 |
| Size | String | 否 | 10 | 返回统计数据的条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| Data | List | {"20": {"src from,count":" _ 23507"}} | 数组存储从Elasticsearch查出来的所有数据。 每个元素是一组数据。 |
|---|---|---|---|
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryThreatChartData &CurrentPage=1 &PageSize=10 &FromTime=1641484800000 &ToTime=1641550177290
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>{"20":{"src_from,count":"23507"}}</Data>
```

`JSON` 格式

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data":"{\"20\": {\"src_from,count\":\"23507\"}}"}
```

### 威胁事件

#### GetSocEvents

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundunnextsoc:GetSocEvents | Read | acs:yundunnextsoc:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Lang | Strin g | Quer y | 否 | zh CN _ | 语言，取值说明如下： en US: 英文 _ zh CN: 中文 _ zh TW: 繁体 _ |
| OrgScope | Strin g | Quer y | 否 | all | 当前请求的数据范围： all：全部 platform：平台 (Aliuids 需要传-1) allOrg：所有组织 singleOrg：单组织 (一级组织传Aliuids,二级及以下传Orgids和OrgFullIds) multiOrg：多组织 (一级组织传Aliuids,二级及以下传Orgids和OrgFullIds， 多选逗号分割) |
| Aliuids | Strin g | Quer y | 否 | 123456789,987654321 | aliuids集合。 |
| OrgIds | Strin g | Quer y | 否 | 1,2 | 组织id集合。 |
| OrgFullIds | Strin g | Quer y | 否 | \|1\|3\|,\|1\|4\| | orgFullIds集合。 |
| ResourceS etIds | Strin g | Quer y | 否 | 1,2,3 | 资源集id集合。 |
| PageNo | Integ er | Quer y | 否 | 1 | 页数，起始为1。 |
| PageSize | Integ er | Quer y | 否 | 10 | 每页条数，默认10，最大 500。 |

| FromTime | Long | Quer y | 否 | 1703575552000 | 查询开始时间，该时间是指事件的判定时间。 |
|---|---|---|---|---|---|
| ToTime | Long | Quer y | 否 | 1703575552000 | 查询截止时间，该时间是指事件的判定时间。 |
| Ip | Strin g | Quer y | 否 | 127.0.0.1 | 事件来源ip或目的ip。 |
| Severitys | Strin g | Quer y | 否 | suspicious,information | 威胁级别多选，以逗号分隔。 取值说明如下: information: 信息 suspicious: 可疑 general: 一般 serious: 严重 urgent: 紧急 |
| AssetNam e | Strin g | Quer y | 否 | assetA | 资产名称。 |
| LoginAkId | Strin g | Quer y | 否 | akabc | 登录akid。 |
| Types | Strin g | Quer y | 否 | illegalAccount,riskConnec tion | 威胁类型多选,以逗号分隔。 取值说明如下: networkScanning： 网络扫描 exploitVulnerability： 漏洞利用 maliciousSoftware： 恶意软件 networkAttack： 网络攻击 riskConnection： 风险连接 abnormalBehavior： 异常行为 illegalAccount：非法提取 |
| Tag | Strin g | Quer y | 否 | tag1 | 标签。 |

| Killchains | Strin g | Quer y | 否 | delivery,target | 所属攻击阶段多选，以逗号分隔。取值说明如下: delivery： 载荷投递 exploitation： 漏洞利用 installation：后门植入 commadControl：命令控制 lateral：扫描扩散 elevate：权限提升 target： 目标打击 |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | 否 | eventname | 事件名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| Data | Struct | xxx | 返回结果（一般为json格式）。 |
| -Items | Array | json格式数据 | 列表。 |
| --SourceIps | Array | [] | 来源ip。 |
| ---Ip | String | 127.0.0.1 | ip地址。 |
| ---Port | Integer | 80 | 端口。 |
| ---Location | String | 北京 | 地址。 |
| --DestIps | Array | [] | 目的ip。 |
| ---Ip | String | 127.0.0.1 | ip地址。 |
| ---Port | Integer | 80 | 端口。 |

| ---Location | String | 北京 | 地址。 |
|---|---|---|---|
| --DocId | String | 123SDFd343 | 事件id。 |
| --Aliuid | Long | 123456789 | aliuid。 |
| --OrgId | Long | 1 | OrgId。 |
| --OrgFullId | String | \|1\|3\| | OrgFullId。 |
| --StartTime | Long | 1703575552000 | 开始时间。 |
| --EndTime | Long | 1703575552000 | 结束时间。 |
| --ThreatTime | Long | 1703575552000 | 威胁事件时间。 |
| --Killchain | String | delivery | 所属攻击阶段多选，以逗号分隔。取值说明如下: delivery： 载荷投递 exploitation： 漏洞利用 installation：后门植入 commadControl：命令控制 lateral：扫描扩散 elevate：权限提升 target： 目标打击 |
| --LogCount | Integer | 10 | 日志数量。 |
| --Status | Integer | 1 | 事件状态:。取值说明如下: 0：新发现 1：未处理 2：已忽略 3：已处理 4：处理中 5：处理失败 |
| --Content | String | 事件的备注信息ABC | 备注。 |
| --Name | String | eventname | 事件名称。 |

| --Severity | String | suspicious | 威胁级别多选，以逗号分隔。取值说明如下: information: 信息 suspicious: 可疑 general: 一般 serious: 严重 urgent: 紧急 |
|---|---|---|---|
| --SocRuleId | Long | 6001232 | 规则id。 |
| --Tag | String | tag1,tag2,tag3 | 标签。 |
| --Type | String | illegalAccount | 威胁类型多选,以逗号分隔。取值说明如下: networkScanning： 网络扫描 exploitVulnerability： 漏洞利用 maliciousSoftware： 恶意软件 networkAttack： 网络攻击 riskConnection： 风险连接 abnormalBehavior： 异常行为 illegalAccount：非法提取 |
| --RuleEsIndex | String | index1 | 规则索引。 |
| --BatchCode | String | 123443 | 文档code。 |
| --NameKey | String | soc.rule.nameKey | 名称key。 |
| -- DescriptionKe y | String | soc.rule.description Key | 威胁描述key。 |
| -- SuggestionsKe y | String | soc.rule.suggestion sKey | 处置建议key。 |
| --HasTraceInfo | Integer | 1 | 是否有溯源信息： 0：无溯源信息 1：有溯源信息 |
| --UpdateTime | Long | 1703575552000 | 更新时间。 |

| -Total | Long | 1000 | 总数。 |
|---|---|---|---|
| -PageNo | Integer | 1 | 页数。 |
| -PageSize | Integer | 10 | 每页条数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetSocEvents&RegionId=cnhangzhou&Lang=zh_CN&OrgScope=all&Aliuids=123456789,987654321&OrgIds=1,2&OrgFullIds=|1|3|,
|4|&ResourceSetIds=1,2,3&PageNo=1&PageSize=10&FromTime=1703575552000&ToTime=1703575552000
p=127.0.0.1&Severity=suspicious&Severitys=suspicious,information&AssetName=assetA&LoginAk =akabc&Type=illegalAccount&Types=illegalAccount,riskConnection&Tag=tag1&Killchain=deliver Killchains=delivery,target&Name=eventname
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Data":{
        "PageSize":10,
        "Total":1000,
        "PageNo":1,
        "Items":[
            {
                "DestIps":[
                    {
                        "Ip":"127.0.0.1",
                        "Port":80,
                        "Location":"北京"
                    }
```

`],`

```json
                "RuleEsIndex":"index1",
                "EndTime":1703575552000,
                "SourceIps":[
                    {
                        "Ip":"127.0.0.1",
                        "Port":80,
                        "Location":"北京"
                    }
```

`],`

```json
                "HasTraceInfo":1,
                "Name":"eventname",
                "DescriptionKey":"soc.rule.descriptionKey",
                "SocRuleId":6001232,
                "Aliuid":123456789,
                "LogCount":10,
                "Status":1,
                "DocId":"123SDFd343",
                "StartTime":1703575552000,
                "Severity":"suspicious",
                "NameKey":"soc.rule.nameKey",
                "OrgId":1,
                "OrgFullId":"|1|3|",
                "Type":"illegalAccount",
                "SuggestionsKey":"soc.rule.suggestionsKey",
                "ThreatTime":1703575552000,
                "BatchCode":"123443",
```

`"Content":"`事件的备注信息`ABC",`

```json
                "UpdateTime":1703575552000,
                "Killchain":"delivery",
                "Tag":"tag1,tag2,tag3"
            }
```

]

```
    }
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Data>
        <Total>1000</Total>
        <PageNo>1</PageNo>
        <PageSize>10</PageSize>
        <Items>
            <DocId>123SDFd343</DocId>
            <Aliuid>123456789</Aliuid>
            <OrgId>1</OrgId>
            <OrgFullId>|1|3|</OrgFullId>
            <StartTime>1703575552000</StartTime>
            <EndTime>1703575552000</EndTime>
            <ThreatTime>1703575552000</ThreatTime>
            <Killchain>delivery</Killchain>
            <LogCount>10</LogCount>
            <Status>1</Status>
```

`<Content>`事件的备注信息`ABC</Content>`

```xml
            <Name>eventname</Name>
            <Severity>suspicious</Severity>
            <SocRuleId>6001232</SocRuleId>
            <Tag>tag1,tag2,tag3</Tag>
            <Type>illegalAccount</Type>
            <RuleEsIndex>index1</RuleEsIndex>
            <BatchCode>123443</BatchCode>
            <NameKey>soc.rule.nameKey</NameKey>
            <DescriptionKey>soc.rule.descriptionKey</DescriptionKey>
            <SuggestionsKey>soc.rule.suggestionsKey</SuggestionsKey>
            <HasTraceInfo>1</HasTraceInfo>
            <SourceIps>
                <Ip>127.0.0.1</Ip>
                <Port>80</Port>
                <Location>北京</Location>
            </SourceIps>
            <DestIps>
                <Ip>127.0.0.1</Ip>
                <Port>80</Port>
                <Location>北京</Location>
            </DestIps>
            <UpdateTime>1703575552000</UpdateTime>
        </Items>
    </Data>
```

yundunnextsoc 2019-07-23

#### GetSocThreatInfo

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundunnextsoc:GetSocThreatIn fo | Read | acs:yundunnextsoc:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Lang | Strin g | Query | 否 | zh CN _ | 语言。 |
| OrgScope | Strin g | Query | 否 | all | 当前请求的数据范围：all： 全部， platform：平台，allOrg：所有组织， singleOrg：单组织， multiOrg：多组织。 |
| Aliuids | Strin g | Query | 否 | 123456789,987654321 | aliuids集合。 |
| OrgIds | Strin g | Query | 否 | 1,2 | 组织id集合。 |
| OrgFullIds | Strin g | Query | 否 | \|1\|3\|,\|1\|4\| | orgFullIds集合。 |
| ResourceS etIds | Strin g | Query | 否 | 1,2,3 | 资源集id集合。 |
| RuleEsInd ex | Strin g | Query | 是 | index1 | 规则索引 |
| BatchCod e | Strin g | Query | 是 | 123443 | code |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| Data | Struct | { "Domains":[ { "TipFlag":1, "Name":"aa" } ], "DestIps":[ { "AssetType":"ECS", "TipFlag":1, "Ip":"127.0.0.1", "Port":80, "IsInnerIp":false, "AssetId":"一般为 uuid", "Tags":"恶意 ip", "AssetName":"ecs0 01", "Location":"aa" } ], "Md5s":[ { "TipFlag":1, "Name":"aa" } ], "Networks":[ { "TipFlag":1, "Name":"aa" } ], "Procs":[ { "TipFlag":1, "Name":"aa" } ], "FilePaths":[ { "TipFlag":1, "Name":"aa" } ], "SourceIps":[ { "AssetType":"ECS", "TipFlag":1, "Ip":"127.0.0.1", "Port":80, "IsInnerIp":false, "AssetId":"一般为 uuid", "Tags":"恶意 ip", "AssetName":"ecs0 01", "Location":"aa" } ], "FileMd5CountTip": { "Names":"aa", "Count":10 }, "FileNames":[ { "TipFlag":1, "Name":"aa" } ], "DomainCountTip": { "Names":"aa", "Count":10 }, "MaliciousIpTip":{ "Names":"aa", "Count":10 }, "Aks":{ "Names":"aa", "Count":10 } } | 返回结果（一般为json格式）。 |
| -Tips | List | - | 提示 |

|  |  |  | 云安全管理中心开发指南·云安全管理中心（SOC） |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -SourceIps | Array | [] | 来源ip |
| --Ip | String | 127.0.0.1 | ip地址 |
| --Port | Integer | 80 | 端口 |
| --Ports | String | - | 端口 |
| --Location | String | aa | 地址 |
| --TipFlag | Integer | 1 | 是否命中情报 |
| --IsInnerIp | Boolean | 1 | 是否是内部ip |
| --Tags | String | 恶意ip | 标签 |
| --AssetId | String | 一般为uuid | 资产id |
| --AssetName | String | ecs001 | 资产名称 |
| --AssetType | String | ECS | 资产类型 |
| -DestIps | Array | [] | 目的ip |
| --Ip | String | 127.0.0.1 | ip地址 |
| --Port | Integer | 80 | 端口 |
| --Ports | String | - | 端口 |
| --Location | String | aa | 地址 |
| --TipFlag | Integer | 1 | 是否命中情报 |
| --IsInnerIp | Boolean | 1 | 是否是内部ip |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Tags | String | 恶意ip | 标签 |
| --AssetId | String | 一般为uuid | 资产id |
| --AssetName | String | ecs001 | 资产名称 |
| --AssetType | String | ECS | 资产类型 |
| -Domains | Array | [] | 域名 |
| --Name | String | aa | 参数值 |
| --TipFlag | Integer | 1 | 是否命中情报 |
| -FileNames | Array | [] | 文件名称 |
| --Name | String | aa | 参数值 |
| --TipFlag | Integer | 1 | 是否命中情报 |
| -FilePaths | Array | [] | 文件路径 |
| --Name | String | aa | 参数值 |
| --TipFlag | Integer | 1 | 是否命中情报 |
| -Md5s | Array | [] | md5 |
| --Name | String | aa | 参数值 |
| --TipFlag | Integer | 1 | 是否命中情报 |
| -Networks | Array | [] | 网络 |
| --Name | String | aa | 参数值 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --TipFlag | Integer | 1 | 是否命中情报 |
| -Procs | Array | [] | 进程信息 |
| --Name | String | aa | 参数值 |
| --TipFlag | Integer | 1 | 是否命中情报 |
| -Aks | Array | [] | AK信息 |
| --Name | String | aa | 参数值 |
| --TipFlag | Integer | 1 | 是否命中情报 |
| -MaliciousIpTip | Struct | [] | 恶意IP情报信息 |
| --Names | List | aa | 信息 |
| --Count | Integer | 10 | 数量 |
| - DomainCountT ip | Struct | [] | 恶意域名情报信息 |
| --Names | List | aa | 信息 |
| --Count | Integer | 10 | 数量 |
| - FileMd5CountT ip | Struct | [] | 恶意文件MD5情报信息 |
| --Names | List | aa | 信息 |
| --Count | Integer | 10 | 数量 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetSocThreatInfo&RegionId=cnhangzhou&Lang=zh_CN&OrgScope=all&Aliuids=123456789,987654321&OrgIds=1,2&OrgFullIds=|1|3|,
|4|&ResourceSetIds=1,2,3&RuleEsIndex=index1&BatchCode=123443
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Data":{
        "Domains":[
            {
                "TipFlag":1,
                "Name":"aa"
            }
```

`],`

```json
        "DestIps":[
            {
                "AssetType":"ECS",
                "TipFlag":1,
                "Ip":"127.0.0.1",
                "Port":80,
                "IsInnerIp":false,
                "AssetId":"一般为uuid",
                "Tags":"恶意ip",
                "AssetName":"ecs001",
                "Location":"aa"
            }
```

`],`

```json
        "Md5s":[
            {
                "TipFlag":1,
                "Name":"aa"
            }
```

`],`

```json
        "Networks":[
            {
                "TipFlag":1,
                "Name":"aa"
            }
```

`],`

```json
        "Procs":[
            {
                "TipFlag":1,
                "Name":"aa"
            }
```

`],`

```json
        "FilePaths":[
            {
                "TipFlag":1,
```

```json
                "Name":"aa"
            }
```

`],`

```json
        "SourceIps":[
            {
                "AssetType":"ECS",
                "TipFlag":1,
                "Ip":"127.0.0.1",
                "Port":80,
                "IsInnerIp":false,
                "AssetId":"一般为uuid",
                "Tags":"恶意ip",
                "AssetName":"ecs001",
                "Location":"aa"
            }
```

`],`

```json
        "FileMd5CountTip":{
            "Names":"aa",
            "Count":10
        },
        "FileNames":[
            {
                "TipFlag":1,
                "Name":"aa"
            }
```

`],`

```json
        "DomainCountTip":{
            "Names":"aa",
            "Count":10
        },
        "MaliciousIpTip":{
            "Names":"aa",
            "Count":10
        }
    }
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Data>
        <SourceIps>
            <Ip>127.0.0.1</Ip>
            <Port>80</Port>
            <Location>aa</Location>
            <TipFlag>1</TipFlag>
            <IsInnerIp>1</IsInnerIp>
            <Tags>恶意ip</Tags>
            <AssetId>一般为uuid</AssetId>
            <AssetName>ecs001</AssetName>
```

```xml
ssetaeecs00 /ssetae
            <AssetType>ECS</AssetType>
        </SourceIps>
        <DestIps>
            <Ip>127.0.0.1</Ip>
            <Port>80</Port>
            <Location>aa</Location>
            <TipFlag>1</TipFlag>
            <IsInnerIp>1</IsInnerIp>
            <Tags>恶意ip</Tags>
            <AssetId>一般为uuid</AssetId>
            <AssetName>ecs001</AssetName>
            <AssetType>ECS</AssetType>
        </DestIps>
        <Domains>
            <Name>aa</Name>
            <TipFlag>1</TipFlag>
        </Domains>
        <FileNames>
            <Name>aa</Name>
            <TipFlag>1</TipFlag>
        </FileNames>
        <FilePaths>
            <Name>aa</Name>
            <TipFlag>1</TipFlag>
        </FilePaths>
        <Md5s>
            <Name>aa</Name>
            <TipFlag>1</TipFlag>
        </Md5s>
        <Networks>
            <Name>aa</Name>
            <TipFlag>1</TipFlag>
        </Networks>
        <Procs>
            <Name>aa</Name>
            <TipFlag>1</TipFlag>
        </Procs>
        <Tips>
            <StringItem></StringItem>
        </Tips>
        <MaliciousIpTip>
            <Count>10</Count>
            <Names>
                <StringItem>aa</StringItem>
            </Names>
        </MaliciousIpTip>
        <DomainCountTip>
            <Count>10</Count>
            <Names>
                <StringItem>aa</StringItem>
            </Names>
        </DomainCountTip>
        <FileMd5CountTip>
            <Count>10</Count>
```

```xml
            <Names>
                <StringItem>aa</StringItem>
            </Names>
        </FileMd5CountTip>
    </Data>
```

## 安全审计

### DescribeOperatorType

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| Resource OwnerId | Long | Query | 否 | 34567891*** | 资源拥有者Uid。 |
| Lang | Strin g | Query | 否 | zh cn _ | 接收消息的语言类型（默认 zh：中文、en：英文）。 |
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| OperatorTypeL ist | Array | QUERY | 操作类型列表。 |
| -Id | Long | 10000 | 操作类型ID。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -ModifiedTime | Long | 1639236844747 | 更新时间。 |
| -OperatorType | Integer | 1 | 操作类型编号。 |
| -Name | String | build | 操作类型名称。 |
| -Remark | String | 新建 | 操作类型描述。 |

|  |  |  | 云安全管理中心开发指南·安全审计 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeOperatorType
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "OperatorTypeList":[
  {
   "ModifiedTime":1639236844747,
   "CreateTime":1639236844747,
   "Id":10000,
   "OperatorType":1,
   "Name":"build",
```

`"Remark":"`新建"

```
  }
```

]

```
}
```

`XML` 格式

```xml
<RequestId>7E0618A9-D5EF-4220-9471-C42B5E92****</RequestId> <OperatorTypeList>
 <ModifiedTime>1639236844747</ModifiedTime>
 <CreateTime>1639236844747</CreateTime>
 <Id>10000</Id>
 <OperatorType>1</OperatorType>
 <Name>build</Name>
 <Remark>新建</Remark>
</OperatorTypeList>
```

### CreateEventType

创建审计事件类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | CreateEventType | 系统规定参数。取值：CreateEventTyp e 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Integ er | Query | 是 | 5 | 日志类型编码。 |
| SourceId | Long | Query | 是 | 10000 | 日志源ID。 |
| Name | Strin g | Query | 是 | 高危查询 | 审计事件类型名称。 |
| Remark | Strin g | Query | 是 | 高危数据库查询操作 | 审计事件类型描述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| EventType | Struct | - | 已创建的审计事件类型。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| -SourceId | Long | 1000 | 日志源ID。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Reserved | Boolean | true | 是否系统预留事件类型。 |
| -Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | 审计事件类型名称。 |
| -Remark | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | 审计事件类型描述。 |
| -Id | Integer | 10135 | 审计事件类型ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -SourceName | String | rds-ss12222 | 日志数据源名称。 |

**示例**

请求示例

```
&LogType=5
```

`&Name=`高危查询 `&Remark=`高危数据库查询操作

```
&SourceId=10000
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "EventType":{
  "SourceId":1000,
  "CreateTime":1639236844747,
  "LogType":1,
  "SourceName":"rds-ss12222",
  "Id":10135,
  "Reserved":true,
  "Name":"EVENT_TYPE_NAME__host__account_create",
  "Remark":"EVENT_TYPE_NAME__host__account_create"
 }
}
```

### DescribeEventType

获取审计事件类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeEventType | 系统规定参数。取值：DescribeEventTyp e 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |

| 云安全管理中心 | 开发指南· | 安全审计 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceId | Long | Query | 否 | 1000 | 日志源ID。 |
| LogType | Integ er | Query | 否 | 1 | 日志类型编码。 |
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| EventTypeList | Array | - | 审计事件类型列表。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| -SourceId | Long | 1000 | 日志源ID。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Reserved | Boolean | true | 是否系统预留事件类型。 |
| -Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | 审计事件类型名称。 |
| -Remark | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | 审计事件类型描述。 |
| -Code | String | account create _ | 事件类型编码。 |
| -Id | Integer | 10135 | 审计事件类型ID。 |
| -SourceName | String | rds-ss12222 | 日志数据源名称。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |

|  |  |  | 云安全管理中心开发指南·安全审计 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 100 | 数据的总条数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1,
 "EventTypeList":[
  {
   "SourceId":1000,
   "CreateTime":1639236844747,
   "LogType":1,
   "SourceName":"rds-ss12222",
   "Id":10135,
   "Code":"account_create",
   "Reserved":true,
   "Name":"EVENT_TYPE_NAME__host__account_create",
   "Remark":"EVENT_TYPE_NAME__host__account_create"
  }
```

]

```
}
```

### DeleteEventType

删除审计事件类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DeleteEventType | 系统规定参数。取值：DeleteEventTyp e 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| Id | Integ er | Query | 是 | 10135 | 审计事件类型ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
&Id=10135
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### CreateLogFilter

创建审计日志查询过滤条件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | 是 | CreateLogFilter | 系统规定参数。取值：CreateLogFilter。 |

| SourceIp | Strin g | Quer y | 否 | 192.168.XX.XX | 访问源IP地址。 |
|---|---|---|---|---|---|
| Type | Integ er | Quer y | 是 | 1 | 过滤条件类型，包含：1：表示日志过滤 2：表示审计事件过滤。 |
| LogType | Integ er | Quer y | 是 | 1 | 日志类型编码。 |
| SourceId | Long | Quer y | 否 | 1000 | 日志源ID。 |
| Name | Strin g | Quer y | 是 | RDS-scscsc | 过滤条件名称。 |
| Defaultabl e | Bool ean | Quer y | 否 | true | 是否默认过滤条件，包含： True：表示默认条件 False：表示非默认条件。 |
| EventRiskL evel | Integ er | Quer y | 否 | 1 | 风险级别编码。 |
| EventType | Integ er | Quer y | 否 | 1 | 审计事件类型。 |
| Alertable | Bool ean | Quer y | 否 | true | 是否告警，包含：True：表示告警 False：表示不告警。 |
| Query | Strin g | Quer y | 否 | Get | 查询关键字。 |
| StartTime | Long | Quer y | 否 | 1519813584985 | 查询开始时间，以时间戳格式表述。 |
| EndTime | Long | Quer y | 否 | 1519813584985 | 查询结束时间，以时间戳格式表述。 |
| LogInitiatio r | Strin g | Quer y | 否 | EQ:Initiator | 发起者。 |
| LogTarget | Strin g | Quer y | 否 | EQ:target | 目标。 |

| LogAction | Strin g | Quer y | 否 | EQ:cmd | 操作行为。 |
|---|---|---|---|---|---|
| LogOutco me | Strin g | Quer y | 否 | EQ:result | 结果。 |
| LogReason | Strin g | Quer y | 否 | EQ:reason | 原因。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| LogFilter | Struct | - | 已创建的查询过滤条件，具体子项说明参见以下参数描述。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| -SourceId | Long | 1000 | 日志源ID。 |
| -Defaultable | Boolean | true | 是否默认过滤条件，包含：True：表示默认条件 False：表示非默认条件。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Name | String | RDS-scscsc | 过滤条件名称。 |
| -Id | Integer | 1000 | 查询过滤条件ID。 |
| -Type | Integer | 1 | 过滤条件类型，包含：1：表示日志过滤 2：表示审计事件过滤。 |
| -UserId | String | 1000 | 创建人ID。 |
| -EventType | Integer | 1 | 审计事件类型。 |

**示例**

请求示例

```
&LogType=1 &Name=RDS-scscsc &Type=1
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "LogFilter":{
  "Type":1,
  "EventType":1,
  "UserId":"1000",
  "SourceId":1000,
  "CreateTime":1639236844747,
  "LogType":1,
  "Id":1000,
  "Defaultable":true,
  "Name":"RDS-scscsc"
 }
}
```

Auditprivate 2018-01-16

### DescribeLogFilter

获取审计日志查询过滤条件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RequestId | Strin g | System | 是 | DescribeLogFilter | 系统规定参数。取值：DescribeLogFilte r 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Strin g | Query | 否 | 1 | 日志类型编码。 |
| SourceId | Long | Query | 否 | 1001 | 日志源ID。 |

| 云安全管理中心 | 开发指南· | 安全审计 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Count | Integ er | Query | 否 | 1001 | 查询返回记录数。 |
| Type | Strin g | Query | 否 | 1 | 过滤条件类型，包含：1： 表示日志过滤2：表示审计事件过滤 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| LogFilterList | Array | - | 查询过滤条件列表。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| -SourceId | Long | 1000 | 日志源ID。 |
| -Defaultable | Boolean | true | 是否默认过滤条件，包含：True：表示默认条件 False：表示非默认条件 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Name | String | RDS-scscsc | 过滤条件名称。 |
| -Id | Integer | 1000 | 查询过滤条件ID。 |
| -Type | Integer | 1 | 过滤条件类型，包含：1：表示日志过滤2：表示审计事件过滤 |
| -UserId | String | 100000 | 创建人ID。 |
| - EventRiskLeve l | Integer | 1 | 风险级别编码。 |
| -EventType | Integer | 1 | 审计事件类型。 |
| -Alertable | Boolean | true | 是否告警。 |
| -StartTime | Long | 1519813584985 | 查询开始时间，以时间戳格式表述。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -EndTime | Long | 1519813584985 | 查询结束时间，以时间戳格式表述。 |
| -Query | String | Get | 查询关键字。 |
| -LogTarget | String | EQ:target | 目标。 |
| -LogAction | String | EQ:cmd | 操作行为。 |
| -LogOutcome | String | EQ:result | 结果。 |
| -LogInitiatior | String | EQ:Initiator | 发起者。 |
| -LogReason | String | EQ:reason | 原因。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "LogFilterList":[
  {
   "EndTime":1519813584985,
   "Query":"Get",
   "EventType":1,
   "SourceId":1000,
   "CreateTime":1639236844747,
   "LogType":1,
   "StartTime":1519813584985,
   "EventRiskLevel":1,
   "LogTarget":"EQ:target",
   "Name":"RDS-scscsc",
   "Type":1,
   "LogAction":"EQ:cmd",
   "LogInitiatior":"EQ:Initiator",
   "UserId":"100000",
   "LogReason":"EQ:reason",
   "LogOutcome":"EQ:result",
   "Id":1000,
   "Alertable":true,
   "Defaultable":true
  }
```

]

```
}
```

### DeleteLogFilter

删除审计日志查询过滤条件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DeleteLogFilter | 系统规定参数。取值：DeleteLogFilter 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| Id | Integ er | Query | 是 | 1000 | 查询过滤条件ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
&Id=1000
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### CreateReceiver

创建审计事件告警接收人。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | CreateReceiver | 系统规定参数。取值：CreateReceiver 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Integ er | Query | 否 | 1 | 日志类型编码。 |
| SourceId | Long | Query | 否 | 1000 | 日志源ID。 |
| EventRisk Level | Integ er | Query | 是 | 1 | 风险级别编码。 |
| Contact | Strin g | Query | 是 | *****@aliyun.com | 告警接收人人联系方式。 |
| Name | Strin g | Query | 是 | Jack | 告警接收人姓名。 |

| 云安全管理中心 | 开发指南· | 安全审计 |  |  |  |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Type | Integ er | Query | 是 | 1 | 接收类型编码。取值：1， 表示通过邮件方式告警。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| Receiver | Struct | - | 已创建的告警接收人，具体子项说明参见以下参数描述。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| -SourceId | Long | 1000 | 日志源ID。 |
| - EventRiskLeve l | Integer | 1 | 风险级别编码。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Contact | String | *****@aliyun.com | 告警接收人人联系方式。 |
| -Name | String | Jack | 告警接收人姓名。 |
| -Id | Integer | 10001 | 告警接收人ID。 |
| -SourceName | String | rds-ss12222 | 日志数据源名称。 |
| -Type | Integer | 1 | 接收类型编码。取值：1，表示通过邮件方式告警。 |

**示例**

请求示例

```
&Contact=*****@aliyun.com &EventRiskLevel=1 &Name=Jack &Type=1
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "Receiver":{
  "Type":1,
  "SourceId":1000,
  "CreateTime":1639236844747,
  "LogType":1,
  "SourceName":"rds-ss12222",
  "Id":10001,
  "EventRiskLevel":1,
  "Contact":"*****@aliyun.com",
  "Name":"Jack"
 }
}
```

### DescribeReceiver

获取告警接收人。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeReceiver | 系统规定参数。取值：DescribeReceive r 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Strin g | Query | 否 | 1 | 日志类型编码。 |
| SourceId | Long | Query | 否 | 1000 | 日志源ID。 |
| EventRisk Level | Strin g | Query | 否 | 1 | 风险级别编码。 |
| Contact | Strin g | Query | 否 | 123@qq.com | 告警接收人人联系方式。 |
| Name | Strin g | Query | 否 | Jack | 告警接收人姓名。 |
| SourceNa me | Strin g | Query | 否 | rds-ss12222 | 日志数据源名称。 |

| 云安全管理中心 | 开发指南· | 安全审计 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ReceiverList | Array | - | 告警接收人列表。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| -SourceId | Long | 1000 | 日志源ID。 |
| - EventRiskLeve l | Integer | 1 | 风险级别编码。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Contact | String | *****@aliyun.com | 告警接收人人联系方式。 |
| -Name | String | Jack | 告警接收人姓名。 |
| -Id | Integer | 10001 | 告警接收人ID。 |
| -SourceName | String | rds-ss12222 | 日志数据源名称。 |
| -Type | Integer | 1 | 接收类型编码。取值：1，表示通过邮件方式告警。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 100 | 数据的总条数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1,
 "ReceiverList":[
  {
   "Type":1,
   "SourceId":1000,
   "CreateTime":1639236844747,
   "LogType":1,
   "SourceName":"rds-ss12222",
   "Id":10001,
   "EventRiskLevel":1,
   "Contact":"*****@aliyun.com",
   "Name":"Jack"
  }
```

]

```
}
```

### DeleteReceiver

删除审计事件告警接收人。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DeleteReceiver | 系统规定参数。取值：DeleteReceiver 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| Id | Integ er | Query | 是 | 1000 | 告警接收人ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
&Id=1000
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### CreateRule

创建审计规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | CreateRule | 系统规定参数。取值：CreateRule |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Integ er | Query | 是 | 1 | 日志类型编码。 |
| SourceId | Long | Query | 否 | 1000 | 日志源ID。 |
| Expressio n | Strin g | Query | 否 | action INCLUDE "删除实例" OR action INCLUDE "删除集群" OR action INCLUDE "删除主机" | 审计规则表达式。 |
| EventRisk Level | Integ er | Query | 是 | 1 | 风险级别编码。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Remark | Strin g | Query | 否 | remark | 备注。 |
| Alertable | Boole an | Query | 是 | true | 是否告警。 |
| EventType Id | Integ er | Query | 是 | 10001 | 审计事件类型编码。 |
| OperatorT ype | Integ er | Query | 否 |  |  |
| RuleName | Strin g | Query | 是 | 高危删除 | 审计规则名称。 |
| StartTime | Strin g | Query | 否 | 1640442436125 | 开始时间，以时间戳格式表述。 |
| EndTime | Strin g | Query | 否 | 1640442436125 | 结束时间，以时间戳格式表述。 |
| AlertActio nList | Strin g | Query | 否 | 1 | 规则告警对象，指定多个告警接收人以“,”隔开。 |
| LogInitiati or | Strin g | Query | 否 | EQ:Initiator | 发起者。 |
| LogTarget | Strin g | Query | 否 | EQ:target | 目标。 |
| LogAction | Strin g | Query | 否 | EQ:cmd | 审计对象。 |
| LogOutco me | Strin g | Query | 否 | EQ:result | 结果。 |
| LogReaso n | Strin g | Query | 否 | EQ:reason | 原因。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| Rule | Struct | - | 已创建的审计规则，具体子项说明参见以下参数描述。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -LogType | Integer | 1 | 日志类型编码。 |
| -SourceId | Long | 1000 | 日志源ID。 |
| - EventRiskLeve l | Integer | 1 | 风险级别编码。 |
| -Alertable | Boolean | true | 是否告警。 |
| -Enabled | Boolean | true | 是否启用。 |
| -EventTypeId | Integer | 10001 | 审计事件类型编码。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Reserved | Boolean | false | 是否预留。 |
| -Name | String | 高危删除 | 审计规则名称。 |
| - EventTypeNa me | String | 资源管理事件 | 事件类型名称。 |
| -Id | Integer | 1000 | 审计规则ID。 |
| -SourceName | String | rds-ss12222 | 日志数据源名称。 |
| -AlertActions | String | 1 | 规则告警对象。 |

**示例**

请求示例

```
&Alertable=true &EventRiskLevel=1 &EventTypeId=10001 &LogType=1
```

`&RuleName=`高危删除 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "Rule":{
  "SourceId":1000,
  "CreateTime":1639236844747,
  "LogType":1,
  "Enabled":true,
  "EventTypeId":10001,
  "SourceName":"rds-ss12222",
  "AlertActions":"1",
  "EventRiskLevel":1,
```

`"Name":"`高危删除`",` `"EventTypeName":"`资源管理事件`",`

```json
  "Alertable":true,
  "Id":1000,
  "Reserved":false
 }
}
```

### DescribeRule

获取审计规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeRule | 系统规定参数。取值：DescribeRule 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Integ er | Query | 否 | 1 | 日志类型编码。 |
| SourceId | Long | Query | 否 | 1000 | 日志源ID。 |
| EventType Id | Long | Query | 否 | 10001 | 审计事件类型编码。 |
| Expressio n | Strin g | Query | 否 | action INCLUDE "删除实例" OR action INCLUDE "删除集群" OR action INCLUDE "删除主机" | 审计规则表达式。 |
| EventRisk Level | Integ er | Query | 否 | 1 | 风险级别编码。 |

| 云安全管理中心 | 开发指南· | 安全审计 |  |  |  |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

| Alertable | Boole an | Query | 否 | true | 是否告警。 |
|---|---|---|---|---|---|
| Enabled | Boole an | Query | 否 | true | 是否启用。 |
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RuleList | Array | - | 审计规则列表。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| -EventTypeId | Integer | 10001 | 审计事件类型编码。 |
| -Expression | String | action INCLUDE "删除实例" OR action INCLUDE "删除集群" OR action INCLUDE "删除主机" | 审计规则表达式。 |
| - EventRiskLeve l | Integer | 1 | 风险级别编码。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Reserved | Boolean | true | 是否预留。 |
| -Name | String | 高危删除 | 审计规则名称。 |
| - EventTypeNa me | String | 资源管理事件 | 事件类型名称。 |
| -Id | Integer | 1000 | 审计规则ID。 |
| -Alertable | Boolean | true | 是否告警。 |

|  |  |  | 云安全管理中心开发指南·安全审计 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -Enabled | Boolean | true | 是否启用。 |
| -AlertActions | String | 1 | 规则告警对象。 |
| -SourceName | String | rds-ss12222 | 日志数据源名称。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 100 | 数据的总条数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RuleList":[
  {
   "CreateTime":1639236844747,
   "LogType":1,
   "EventTypeId":10001,
   "Enabled":true,
   "SourceName":"rds-ss12222",
   "AlertActions":"1",
   "EventRiskLevel":1,
```

`"Name":"`高危删除`",`

```json
   "Expression":"action INCLUDE \"删除实例\" OR action INCLUDE \"删除集群\" OR action INCL
```

UDE \"删除主机\"", `"EventTypeName":"`资源管理事件`",`

```json
   "Id":1000,
   "Alertable":true,
   "Reserved":true
  }
```

`],`

```json
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1
}
```

### EnableRule

启用审计规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | EnableRule | 系统规定参数。取值：EnableRule 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DisableRule

禁用审计规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DisableRule | 系统规定参数。取值：DisableRule 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |
| Id | Integ er | Query | 否 | 1 | 审计规则ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

`JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DeleteRule

删除审计规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DeleteRule | 系统规定参数。取值：DeleteRule 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |
| Id | Integ er | Query | 是 | 1000 | 审计规则ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
&Id=1000
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### CreateTask

创建导出任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | CreateTask | 系统规定参数。取值：CreateTask 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |
| Param | Strin g | Query | 是 | {"id":421711} | 查询参数，以JSON格式表述。 |
| Type | Integ er | Query | 是 | 1 | 导出任务类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| Task | Struct | - | 已创建的导出任务，具体子项说明参见以下参数描述。 |
| -Result | String | {"url":"https://yund un-auditlog- archive.oss- ***.aliyun.com/OPS /20211224151432 914- e902e5b4/EVENT/O PS-******.zip?} | 任务执行结果。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Param | String | {"id":421711} | 查询参数，以JSON格式表述。 |
| -Id | Integer | 1000 | 导出任务ID。 |
| -Type | Integer | 1 | 导出任务类型。 |
| -Status | Integer | 3 | 任务执行状态：1：准备中2：执行中3：任务成功4：任务失败。 |

**示例**

请求示例

```
&Param={"id":421711} &Type=1
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "Task":{
  "Status":3,
  "Type":1,
  "CreateTime":1639236844747,
  "Param":"{\"id\":421711}",
  "Id":1000,
  "Result":"{\"url\":\"https://yundun-auditlog-archive.oss-
***.aliyun.com/OPS/20211224151432914-e902e5b4/EVENT/OPS-******.zip?}"
 },
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeTask

获取导出任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeTask | 系统规定参数。取值：DescribeTask 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |
| Type | Integ er | Query | 否 | 1 | 导出任务类型。 |
| Status | Integ er | Query | 否 | 1 | 任务执行状态：1：准备中 2：执行中3：任务成功4： 任务失败。 |
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TaskList | Array | - | 导出任务列表。 |
| -Result | String | {"url":"https://yund un-auditlog- archive.oss-cn- neimeng-env30- d01- a.intra.env30.shug uang.com/OPS/202 11224151432914- e902e5b4/EVENT/O PS- 20211224151432.z ip?} | 任务执行结果。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Param | String | {"id":421711} | 查询参数，以JSON格式表述。 |
| -StartTime | Long | 1639236844747 | 开始时间，以时间戳格式表述。 |
| -Id | Integer | 1000 | 导出任务ID。 |
| -EndTime | Long | 1639236844747 | 结束时间，以时间戳格式表述。 |
| -Type | Integer | 1 | 导出任务类型。 |
| -Status | Integer | 1 | 任务执行状态：1：准备中2：执行中3：任务成功4：任务失败。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 100 | 数据的总条数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1,
 "TaskList":[
  {
   "Status":1,
   "Type":1,
   "EndTime":1639236844747,
   "CreateTime":1639236844747,
   "Param":"{\"id\":421711}",
   "StartTime":1639236844747,
   "Id":1000,
   "Result":"{\"url\":\"https://yundun-auditlog-archive.oss-cn-neimeng-env30-d01-a.intr
a.env30.shuguang.com/OPS/20211224151432914-e902e5b4/EVENT/OPS-20211224151432.zip?}"
  }
```

]

```
}
```

### DescribeSetting

获取安全审计系统设置参数信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeSetting | 系统规定参数。取值：DescribeSetting 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SettingList | Array | - | 系统参数信息列表。 |

|  |  |  |  | 云安全管理中心开发指南·安全审计 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Name | String | max day alert nu _ _ _ mber | 系统参数名称。 |
| -UpdateTime | Long | 1639236844747 | 上次更新时间。 |
| -Remark | String | 每天发送报警的最大次数 | 系统参数描述。 |
| -Id | Integer | 1 | 系统参数ID。 |
| -Type | Integer | 2 | 数据类型。 |
| -Value | String | -1 | 系统参数值。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "SettingList":[
  {
   "Type":2,
   "UpdateTime":1639236844747,
   "Value":"-1",
   "Id":1,
   "Name":"max_day_alert_number",
```

`"Remark":"`每天发送报警的最大次数"

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### ModifySetting

修改安全审计系统设置参数信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | ModifySetting | 系统规定参数。取值：ModifySetting 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |
| Name | Strin g | Query | 是 | max day alert number _ _ _ | 系统参数名称。 |
| Value | Strin g | Query | 是 | -1 | 系统参数值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeLogType

获取日志类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeLogType | 系统规定参数。取值：DescribeLogTyp e 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| LogTypeList | Array | - | 日志类型列表。 |
| -Remark | String | 平台数据库 | 日志类型名称。 |
| -Type | Integer | 1 | 日志类型编码。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "LogTypeList":[
  {
   "Type":1,
```

`"Remark":"`平台数据库"

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeLogSource

获取日志源信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeLogSource | 系统规定参数。取值：DescribeLogSourc e 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Integ er | Query | 否 | 1 | 日志类型编码。 |
| Enabled | Boole an | Query | 否 | true | 是否启用。 |
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| LogSourceList | Array | - | 日志源列表。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| -Code | String | RDS-scscsc | 日志源编码。 |
| -CreateTime | Long | 1639236844747 | 创建时间。 |
| -Name | String | RDS-scscsc | 日志源名称。 |
| -Id | Integer | 1000 | 日志源ID。 |
| -Alertable | Boolean | true | 是否告警。 |
| -Enabled | Boolean | true | 是否启用。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 1000 | 数据的总条数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "LogSourceList":[
  {
   "CreateTime":1639236844747,
   "LogType":1,
   "Enabled":true,
   "Id":1000,
   "Alertable":true,
   "Code":"RDS-scscsc",
   "Name":"RDS-scscsc"
  }
```

`],`

```json
 "TotalCount":1000,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1
}
```

### DescribeLogCountStat

获取原始日志统计信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeLogCountStat | 系统规定参数。取值：DescribeLogCount Stat 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| StartTime | Strin g | Query | 否 | 1639725751259 | 开始时间，以时间戳格式表述。 |
| LogTypeLi st | Strin g | Query | 否 | 1,2,3,4,5 | 日志类型编码，指定多个日志类型以“，”隔开。 |
| EndTime | Strin g | Query | 否 | 1639725751259 | 结束时间，以时间戳格式表述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| StatList | Array | - | 原始日志统计数据列表。 |
| -StatItemList | Array | - | 原始日志数据。 |
| --Count | Long | 1000 | 原始日志数量。 |
| --Time | Long | 1640244151259 | 统计时间，以时间戳格式表述。 |
| --Capacity | Float | 1000.0 | 空间占用量。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLogCountStat
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "StatList":[
  {
   "LogType":1,
   "StatItemList":[
    {
     "Capacity":1000.0,
     "Time":1640244151259,
     "Count":1000
    }
```

]

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeLog

获取原始日志详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeLog | 系统规定参数。取值：DescribeLog 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Integ er | Query | 否 | 1 | 日志类型编码。 |
| SourceId | Long | Query | 否 | 1001 | 日志源ID。 |
| Query | Strin g | Query | 否 | Get | 查询关键字。 |
| StartTime | Long | Query | 否 | 1639236844747 | 开始时间，以时间戳格式表述。 |
| EndTime | Long | Query | 否 | 1639236844747 | 结束时间，以时间戳格式表述。 |
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |

| 云安全管理中心 | 开发指南· | 安全审计 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HistogramList | Array | - | 原始日志数量图表信息。 |
| -Count | Integer | 1000 | 原始日志数量。 |
| -StartTime | Long | 1639236844747 | 开始时间，以时间戳格式表述。 |
| -EndTime | Long | 1639236844747 | 结束时间，以时间戳格式表述。 |
| -Completed | Boolean | true | 在该子时间区间内的原始日志结果是否完整，如果不完整则展示估算值。 |
| LogList | Array | - | 原始日志列表。 |
| -ColumnList | Array | - | 日志详情列表。 |
| --TokenList | Array | - | Token数据列表。 |
| ---Delimit | Boolean | false | Token是否限定。 |
| ---Word | String | 012 | 限定值。 |
| --Value | String | 012 | 列值。 |
| --Key | String | value | 列名称。 |
| -Source | String | 1 | 日志源名称。 |
| -LogTime | Long | 1640244151259 | 日志产生时间。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Long | 100 | 数据的总条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "LogList":[
  {
   "ColumnList":[
    {
     "Value":"012",
     "TokenList":[
      {
       "Word":"012",
       "Delimit":false
      }
```

`],`

```json
     "Key":"value"
    }
```

`],`

```json
   "LogTime":1640244151259,
   "Source":"1"
  }
```

`],`

```json
 "HistogramList":[
  {
   "EndTime":1639236844747,
   "StartTime":1639236844747,
   "Completed":true,
   "Count":1000
  }
```

`],`

```json
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1
}
```

### DescribeEventRisk

获取审计事件风险级别信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeEventRisk | 系统规定参数。取值：DescribeEventRis k 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| EventRiskList | Array | - | 事件风险级别列表。 |
| -Level | Integer | 0 | 风险级别编码。 |
| -Name | String | 全局风险 | 风险级别名称。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "EventRiskList":[
  {
   "Level":0,
```

`"Name":"`全局风险"

```
  }
```

]

```
}
```

### DescribeEventRiskStat

按风险等级获取审计事件统计信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeEventRiskStat | 系统规定参数。取值：DescribeEventRis kStat 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| StartTime | Strin g | Query | 否 | 1639725751259 | 开始时间，以时间戳格式表述。 |
| LogTypeLi st | Strin g | Query | 否 | 1,2,3 | 日志类型编码，指定多个日志类型以","隔开。 |
| EndTime | Strin g | Query | 否 | 1640244151259 | 结束时间，以时间戳格式表述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| StatList | Array | - | 统计数据列表。 |
| -StatItemList | Array | - | 统计数据。 |
| -- EventRiskLeve l | Integer | 1 | 风险级别编码。 |

|  | 云安全管理中心开发 | 指南·安全审计 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Count | Integer | 1 | 审计事件数量。 |
| --Capacity | Integer | 44 | 空间占用量。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeEventRiskStat
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "StatList":[
  {
   "LogType":1,
   "StatItemList":[
    {
     "Capacity":44,
     "Count":1,
     "EventRiskLevel":1
    }
```

]

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeEventTypeStat

按审计事件类型获取审计事件统计信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RequestId | Strin g | System | 是 | DescribeEventTypeStat | 系统规定参数。取值：DescribeEventTyp eStat 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| StartTime | Strin g | Query | 否 | 1639725751259 | 开始时间，以时间戳格式表述。 |
| LogTypeLi st | Strin g | Query | 否 | 1,2,3,4,5 | 日志类型编码，指定多个日志类型以“,”隔开。 |
| EndTime | Strin g | Query | 否 | 1640244151259 | 结束时间，以时间戳格式表述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| StatList | Array | - | 统计数据列表。 |
| -Count | Integer | 10001 | 审计事件数量。 |
| -Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | 审计事件类型名称。 |
| -Reserved | Boolean | true | 是否系统预留事件类型。 |
| -Id | Integer | 10135 | 审计事件类型ID。 |
| -Capacity | Float | 8991.659133 | 空间占用量。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeEventTypeStat
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "StatList":[
  {
   "Capacity":8991.659,
   "Count":10001,
   "Id":10135,
   "Name":"EVENT_TYPE_NAME__host__account_create",
   "Reserved":true
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeEventCountStat

获取审计事件统计信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeEventCountStat | 系统规定参数。取值：DescribeEventCou ntStat 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| StartTime | Strin g | Query | 否 | 1639725751259 | 开始时间，以时间戳格式表述。 |
| LogTypeLi st | Strin g | Query | 否 | 1,2,3 | 日志类型编码，指定多个日志类型以“，”隔开。 |
| EndTime | Strin g | Query | 否 | 1640244151259 | 结束时间，以时间戳格式表述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| StatList | Array | - | 审计事件统计数据列表，具体子项说明参见以下参数描述。 |

|  |  |  | 云安全管理中心开发指南·安全审计 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -StatItemList | Array | - | 审计事件数据，具体子项说明参见以下参数描述。 |
| --Count | Integer | 10001 | 审计事件数量。 |
| --Time | Long | 1639929600000 | 日志产生时间。 |
| --Capacity | Integer | 8991 | 空间占用量统计。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeEventCountStat
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "StatList":[
  {
   "LogType":1,
   "StatItemList":[
    {
     "Capacity":8991,
     "Time":1639929600000,
     "Count":10001
    }
```

]

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeEvent

获取审计事件详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeEvent | 系统规定参数。取值：DescribeEvent 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| lang | Strin g | Query | 否 | zh | 请求和接收消息的语言类型。（zh：中文；en：英文） |
| LogType | Integ er | Query | 否 | 1 | 日志类型编码。 |
| SourceId | Long | Query | 否 | 1000 | 日志源ID。 |
| EventRisk Level | Integ er | Query | 否 | 1 | 风险级别编码。 |
| Alertable | Boole an | Query | 否 | true | 是否告警。 |
| EventType Id | Long | Query | 否 | 10001 | 审计事件类型ID。 |
| StartTime | Long | Query | 否 | 1639236844747 | 开始时间，以时间戳格式表述。 |
| EndTime | Long | Query | 否 | 1639236844747 | 结束时间，以时间戳格式表述。 |
| Keyword | Strin g | Query | 否 | Describe | 查询关键字。 |
| RuleId | Long | Query | 否 | 1000 | 审计规则ID。 |
| LogInitiati or | Strin g | Query | 否 | EQ:Initiator | 发起者。 |
| LogTarget | Strin g | Query | 否 | EQ:Target | 目标。 |
| LogAction | Strin g | Query | 否 | EQ:cmd | 操作行为。 |
| LogOutco me | Strin g | Query | 否 | EQ:result | 结果。 |

|  |  |  |  |  | 云安 | 全管理中心开发指南·安全审计 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| LogReaso n | Strin g | Query | 否 | EQ:reason | 原因。 |
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HistogramList | Array | - | 审计事件数量图表信息。 |
| -Count | Integer | 1001 | 审计事件数量。 |
| -StartTime | Long | 1639236844747 | 开始时间，以时间戳格式表述。 |
| -EndTime | Long | 1639236844747 | 结束时间，以时间戳格式表述。 |
| -Completed | Boolean | true | 在该子时间区间内的审计事件结果是否完整，如果不完整则展示估算值。 |
| EventList | Array | - | 审计事件列表。 |
| -LogSha256 | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | 日志文件SHA256值。 |
| -SourceId | Long | 1000 | 日志源ID。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| - EventRiskLeve l | Integer | 1 | 风险级别编码。 |
| -LogContent | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | 日志内容。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -LogMd5 | String | 36c22c2020d4738 81f8b8bbf1c3eaf0 8 | 日志文件MD5值。 |
| -LogTime | Long | 1639929600000 | 日志产生时间。 |
| -EventTypeId | Integer | 1001 | 审计事件类型ID。 |
| -CreateTime | Long | 1639236844747 | 创建时间 |
| -Receivers | String | 123.qq.com | 告警接收对象。 |
| - EventTypeNa me | String | 资源管理事件 | 审计事件类型名称。 |
| -Id | Long | 1000 | 审计事件ID。 |
| -SourceName | String | rds-ss12222 | 日志数据源名称。 |
| - EventTypeRes erved | Boolean | true | 是否系统默认审计事件类型。 |
| -RuleId | Integer | 1000 | 审计规则ID。 |
| -LogInitiatior | String | EQ:Initiator | 发起者。 |
| -LogTarget | String | EQ:target | 目标。 |
| -LogAction | String | EQ:cmd | 操作行为。 |
| -LogOutcome | String | EQ:result | 结果。 |
| -LogReason | String | EQ:reason | 原因。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| TotalCount | Integer | 100 | 数据的总条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |

|  |  |  | 云安全管理中心开发指南·安全审计 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
|---|---|---|---|

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "HistogramList":[
  {
   "EndTime":1639236844747,
   "StartTime":1639236844747,
   "Completed":true,
   "Count":1001
  }
```

`],`

```json
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "EventList":[
  {
   "LogMd5":"36c22c2020d473881f8b8bbf1c3eaf08",
   "SourceId":1000,
   "LogTime":1639929600000,
   "RuleId":1000,
   "EventTypeId":1001,
   "LogAction":"EQ:cmd",
   "LogOutcome":"EQ:result",
   "EventTypeReserved":true,
   "CreateTime":1639236844747,
   "Receivers":"123.qq.com",
   "LogType":1,
   "SourceName":"rds-ss12222",
   "EventRiskLevel":1,
   "LogTarget":"EQ:target",
   "LogInitiatior":"EQ:Initiator",
   "LogSha256":"929724b41deb5adc78764976f0a397109f2602ba5c7dcced2cb26b8d37a97b5d",
   "LogContent":"929724b41deb5adc78764976f0a397109f2602ba5c7dcced2cb26b8d37a97b5d",
   "LogReason":"EQ:reason",
```

`"EventTypeName":"`资源管理事件`",`

```json
   "Id":1000
  }
```

`],`

```json
 "CurrentPage":1
}
```

### DescribeArchiveCountStat

获取日志、事件存档统计信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeArchiveCountSt at | 系统规定参数。取值：DescribeArchiveC ountStat |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| StartTime | Strin g | Query | 否 | 1639725751259 | 开始时间，以时间戳格式表述。 |
| LogTypeLi st | Strin g | Query | 否 | 1,2,3 | 日志类型编码，指定多个日志类型以“，”隔开。 |
| EndTime | Strin g | Query | 否 | 1640244151259 | 结束时间，以时间戳格式表述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| StatList | Array | - | 存档统计数据列表，具体子项说明参见以下参数描述。 |
| -StatItemList | Array | - | 存档统计数据，具体子项说明参见以下参数描述。 |
| --Count | Integer | 3 | 数量。 |
| --Time | Long | 1639929600000 | 统计时间，以时间戳格式表述。 |
| --Capacity | Float | 6.6 | 存档占用空间。 |
| -LogType | Integer | 1 | 日志类型编码。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeArchiveCountStat
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "StatList":[
  {
   "LogType":1,
   "StatItemList":[
    {
     "Capacity":6.6,
     "Time":1639929600000,
     "Count":3
    }
```

]

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DeleteTask

删除导出任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DeleteTask | 系统规定参数。取值：DeleteTask 。 |
| SourceIp | Strin g | Query | 否 | 192.168.x.x | 访问源IP地址。 |
| Id | Integ er | Query | 是 | 1000 | 导出任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |

**示例**

请求示例

```
&Id=1000
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeArchive

获取日志、事件存档详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeArchive | 系统规定参数。取值：DescribeArchive 。 |
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 访问源IP地址。 |
| LogType | Integ er | Query | 否 | 1 | 日志类型编码。 |
| StartTime | Strin g | Query | 否 | 1639725751259 | 开始时间，以时间戳格式表述。 |
| EndTime | Strin g | Query | 否 | 1640244151259 | 结束时间，以时间戳格式表述。 |
| Type | Integ er | Query | 否 | 1 | 归存档类型。 |
| PageSize | Integ er | Query | 否 | 20 | 每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 当前页的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ArchiveList | Array | - | 存档数据列表，具体子项说明参见以下参数描述。 |

| 云安全管理中心开发 | 指南·安全审计 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -LogType | Integer | 1 | 日志类型编码。 |
| -CompactAlg | Integer | 1 | 压缩算法类型。 |
| -Sha256 | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | 存档文件SHA256值。 |
| -CreateTime | Long | 1639236844747 | 创建时间 |
| -Count | Integer | 3 | 数量。 |
| -Name | String | NETWORK/202112 24153332996- 44a9fc6e/EVENT/N ETWORK- 20211224153332.z ip | 存档文件名称。 |
| -Id | Integer | 1000 | 存档ID。 |
| -Type | Integer | 1 | 归存档类型。 |
| -Md5 | String | 36c22c2020d4738 81f8b8bbf1c3eaf0 8 | 存档文件MD5值。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 本次调用请求的ID。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 100 | 数据的总条数。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "TotalCount":100,
 "ArchiveList":[
  {
   "Type":1,
   "CompactAlg":1,
   "CreateTime":1639236844747,
   "LogType":1,
   "Count":3,
   "Id":1000,
   "Sha256":"929724b41deb5adc78764976f0a397109f2602ba5c7dcced2cb26b8d37a97b5d",
   "Name":"NETWORK/20211224153332996-44a9fc6e/EVENT/NETWORK-20211224153332.zip",
   "Md5":"36c22c2020d473881f8b8bbf1c3eaf08"
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1
}
```

## 态势感知

### 资产管理

#### DescribeFieldStatistics

调用该接口检索资产实例列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeFieldSta tistics | 系统规定参数。取值：DescribeFieldStatistics。 |
| RegionId | String | 否 | cn-hangzhou | 所属地域ID。 |
| MachineTypes | String | 否 | ecs | 指定需要查询的机器类型。多个类型之间需要用英文逗号分隔。不指定资产类型， 即查询所有类型资产的统计信息。取值： 0：云服务器。 1：负载均衡。 2：NAT网关。 3：RDS数据库。 4：MongoDb数据库。 6：容器镜像。 7：容器资产类型。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| GroupedFields | Struct |  | 资产信息。 |
| AliYunInstance Count | Integer | 10 | 阿里云实例数量。 |
| ExposedInstan ceCount | Integer | 10 | 暴露实例数量。 |
| GeneralAssetC ount | Integer | 10 | 一般实例数量。 |
| GroupCount | Integer | 10 | 分组数量。 |
| IdcInstanceCo unt | Integer | 10 | 云外主机实例数量。 |

| ImportantAsse tCount | Integer | 10 | 重要实例数量。 |
|---|---|---|---|
| InstanceCount | Integer | 10 | 实例数量。 |
| InstanceSyncT askCount | Integer | 10 | 同步任务数量。 |
| NewInstanceC ount | Integer | 10 | 新实例数量。 |
| NotRunningSta tusCount | Integer | 10 | 非运行中机器数量。 |
| OfflineInstanc eCount | Integer | 10 | 离线实例数量。 |
| ProviderCount | Integer | 10 | 供应商数量。 |
| RegionCount | Integer | 10 | 区域数量。 |
| RiskInstanceC ount | Integer | 10 | 风险实例数量。 |
| TencentInstan ceCount | Integer | 10 | 腾讯主机实例数量。 |
| TestAssetCoun t | Integer | 10 | 测试实例数量。 |
| UnprotectedIn stanceCount | Integer | 10 | 不受保护实例数量。 |
| VpcCount | Integer | 10 | VPC数量。 |
| RequestId | String | 7E06****9-D5EF- 4220-9471- ***5E92719F | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeFieldStatistics
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7E06****9-D5EF-4220-9471-***5E92719F</RequestId> <GroupedFields>
    <ProviderCount>10</ProviderCount>
    <ExposedInstanceCount>10</ExposedInstanceCount>
    <GroupCount>10</GroupCount>
    <InstanceSyncTaskCount>10</InstanceSyncTaskCount>
    <TencentInstanceCount>10</TencentInstanceCount>
    <RiskInstanceCount>10</RiskInstanceCount>
    <ImportantAssetCount>10</ImportantAssetCount>
    <IdcInstanceCount>10</IdcInstanceCount>
    <GeneralAssetCount>10</GeneralAssetCount>
    <TestAssetCount>10</TestAssetCount>
    <UnprotectedInstanceCount>10</UnprotectedInstanceCount>
    <InstanceCount>10</InstanceCount>
    <OfflineInstanceCount>10</OfflineInstanceCount>
    <VpcCount>10</VpcCount>
    <AliYunInstanceCount>10</AliYunInstanceCount>
    <RegionCount>10</RegionCount>
    <NotRunningStatusCount>10</NotRunningStatusCount>
    <NewInstanceCount>10</NewInstanceCount>
</GroupedFields>
```

`JSON` 格式

```json
{
    "RequestId": "7E06****9-D5EF-4220-9471-***5E92719F",
    "GroupedFields": {
        "ProviderCount": 10,
        "ExposedInstanceCount": 10,
        "GroupCount": 10,
        "InstanceSyncTaskCount": 10,
        "TencentInstanceCount": 10,
        "RiskInstanceCount": 10,
        "ImportantAssetCount": 10,
        "IdcInstanceCount": 10,
        "GeneralAssetCount": 10,
        "TestAssetCount": 10,
        "UnprotectedInstanceCount": 10,
        "InstanceCount": 10,
        "OfflineInstanceCount": 10,
        "VpcCount": 10,
        "AliYunInstanceCount": 10,
        "RegionCount": 10,
        "NotRunningStatusCount": 10,
        "NewInstanceCount": 10
    }
}
```

#### DescribeGroupedTags

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeGroupe dTags | 系统规定参数。取值：DescribeGroupedTags。 |
| MachineTypes | String | 否 | 0 | 指定需要查询的机器类型。多个类型之间需要用英文逗号分隔。取值： 0：云服务器。 1：负载均衡。 2：NAT网关。 3：RDS数据库。 4：MongoDb数据库。 6：容器镜像。 7：容器。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 2 | 当前页显示的数据条数。 |
| GroupedFileds | Array of GroupedFiled |  | 资产标签的统计信息。 |
| Count | String | 2 | 标签对应资产数量。 |
| Name | String | test | 标签名称。 |
| TagId | Integer | 5 | 标签ID。 |
| HttpStatusCod e | Integer | 1 | 已废弃。 |
| RequestId | String | 7E0618A9-D5EF- ***-9471- C42B5E92719F | 本次调用请求的ID。 |
| Success | Boolean | true | 已废弃。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGroupedTags
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7E0618A9-D5EF-***-9471-C42B5E92719F</RequestId> <HttpStatusCode>1</HttpStatusCode> <GroupedFileds>
    <TagId>5</TagId>
    <Count>2</Count>
    <Name>test</Name>
</GroupedFileds> <Count>2</Count> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "7E0618A9-D5EF-***-9471-C42B5E92719F",
    "HttpStatusCode": 1,
    "GroupedFileds": {
        "TagId": 5,
        "Count": 2,
        "Name": "test"
    },
    "Count": 2,
    "Success": true
}
```

#### DescribeAllGroups

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAllGrou ps | 系统规定参数。取值：DescribeAllGroups。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值： zh：中文。 en：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 1 | 当前页显示数据数量。 |

| Groups | Array of Group |  | 服务器分组信息。 |
|---|---|---|---|
| GroupFlag | Integer | 1 | 分组标识。取值： 0：默认分组。 1：其他分组。 |
| GroupId | Integer | 3 | 分组ID。 |
| GroupName | String | 分组名 | 分组名称。 |
| RequestId | String | 7E0618A9-****- 4220-9471- C42B5E92719F | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7E0618A9-****-4220-9471-C42B5E92719F</RequestId> <Groups>
    <GroupName>分组名</GroupName>
    <GroupFlag>1</GroupFlag>
    <GroupId>3</GroupId>
</Groups> <Count>1</Count>
```

`JSON` 格式

```json
{
    "RequestId": "7E0618A9-****-4220-9471-C42B5E92719F",
    "Groups": {
```

`"GroupName": "`分组名`",`

```json
        "GroupFlag": 1,
        "GroupId": 3
    },
    "Count": 1
}
```

#### DescribeInstanceStatistics

查询资产的风险统计信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeInstanc eStatistics | 系统规定参数。取值：DescribeInstanceStatistics。 |
| From | String | 是 | sas | 数据请求来源。固定为sas。 |
| Uuid | String | 是 | a51cec37-ed73- 4c53-b467-*** | 资产实例的唯一标识ID列表。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Array of Data |  | 资产风险的统计信息。 |
| Account | Integer | 1 | 登录账户数量。 |
| AppNum | Integer | 0 | 应用漏洞数量。 |
| CmsNum | Integer | 2 | CMS漏洞数量。 |
| CveNum | Integer | 1 | Linux漏洞数量。 |
| EmgNum | Integer | 0 | 应急漏洞数量。 |
| ExposedCount | Integer | 1 | 已废弃。 |
| Health | Integer | 1 | 基线检查风险数量。 |
| ScaNum | Integer | 5 | SCA漏洞数量。 |
| Suspicious | Integer | 2 | 告警数量。 |

| SysNum | Integer | 1 | Windows漏洞数量。 |
|---|---|---|---|
| Trojan | Integer | 1 | 木马数量。 |
| Uuid | String | us1233****** | 资产实例的唯一标识ID。 |
| Vul | Integer | 4 | 所有漏洞数量总和。 说明总和 =CveNum+EmgNum+SysNum+CmsN um+AppNum。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeInstanceStatistics &From=sas &Uuid=a51cec37-ed73-4c53-b467-***
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId> <Data>
    <Account>1</Account>
    <Uuid>us1233******</Uuid>
    <Suspicious>2</Suspicious>
    <Health>1</Health>
    <CveNum>1</CveNum>
    <ExposedCount>1</ExposedCount>
    <ScaNum>5</ScaNum>
    <CmsNum>2</CmsNum>
    <Trojan>1</Trojan>
    <SysNum>1</SysNum>
    <EmgNum>0</EmgNum>
    <AppNum>0</AppNum>
    <Vul>4</Vul>
</Data>
```

`JSON` 格式

```json
{
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
    "Data": {
        "Account": 1,
        "Uuid": "us1233******",
        "Suspicious": 2,
        "Health": 1,
        "CveNum": 1,
        "ExposedCount": 1,
        "ScaNum": 5,
        "CmsNum": 2,
        "Trojan": 1,
        "SysNum": 1,
        "EmgNum": 0,
        "AppNum": 0,
        "Vul": 4
    }
}
```

#### DescribeCloudProductFieldStatistics

获取云产品统计信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCloudPr oductFieldStatist ics | 系统规定参数。取值：DescribeCloudProductFieldSt atistics。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| GroupedFields | Struct |  | 云产品统计信息。 |
| CategoryCount | String | [{"MachineType":1 ,"Count":11}] | 不同类型资产数量的统计信息。其中 MachineType表示资产类型，Count表示资产类型对应的资产数量。 以下为MachineType取值说明： 1：负载均衡。 2：NAT网关。 3：RDS数据库。 4：MongoDB数据库。 |
| InstanceCount | Integer | 100 | 实例数量。 |

| RiskInstanceC ount | Integer | 90 | 风险实例数量。 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCloudProductFieldStatistics
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId> <GroupedFields>
    <InstanceCount>100</InstanceCount>
    <CategoryCount>[{"MachineType":1,"Count":11}]</CategoryCount>
    <RiskInstanceCount>90</RiskInstanceCount>
</GroupedFields>
```

`JSON` 格式

```json
{
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
    "GroupedFields": {
        "InstanceCount": 100,
        "CategoryCount": "[{\"MachineType\":1,\"Count\":11}]",
        "RiskInstanceCount": 90
    }
}
```

#### DescribeCloudCenterInstances

查询资产中心页面中的资产信息，例如资产实例名称、资产实例所属区域等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCloudC enterInstances | 系统规定参数。取值：DescribeCloudCenterInstance s。 |
| RegionId | String | 否 | cn-demo-***-*** | 区域ID。 |

| Criteria | String | 否 | [{\"name\":\"risk Status\",\"value\ ":\"YES\"}, {\"name\":\"inte rnetIp\",\"value\" :\"1.2.3.4\"}] | 设置搜索资产的条件。 说明支持使用实例ID、实例名称、所属VPC ID、地域、公网IP地址等条件搜索资产。您可以调用 DescribeCriteria查询支持的搜索条件。 该参数格式为： [{\"name\":\"条件1 名称 _ \",\"value\":\"条件1 值\"}, _ {\"name\":\"条件2 名称 _ \",\"value\":\"条件2 值\"}, _ {},...] |
|---|---|---|---|---|
| MachineTypes | String | 否 | 0 | 指定需要查询的机器类型。取值： 0：云服务器。 1：负载均衡。 2：NAT网关。 3：RDS数据库。 4：MongoDb数据库。 6：容器镜像 。 7：容器。 |
| LogicalExp | String | 否 | OR | 设置多个搜索条件间生效的逻辑关系。取值： OR：表示多个条件间为或的关系。 AND：表示多个条件间为与的关系。 |
| NoPage | Boolean | 否 | true | 是否分页查询。取值： true：表示进行分页查询数据。 false：表示不进行分页查询数据。 |
| PageSize | Integer | 否 | 20 | 进行分页查询时，每页显示的数据最大条数。 |
| CurrentPage | Integer | 否 | 1 | 进行分页查询时，当前页的页码。 |

| Importance | Integer | 否 | 1 | 已废弃。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Instances | Array of Instance |  | 资产详细信息。 |
| AlarmStatus | String | NO | 是否有安全告警。取值： YES：有。 NO：无。 |
| AssetType | String | ecs | 资产类型。 |
| AutoSnapshots Level | Integer | 1 | 已废弃。 |
| ClientStatus | String | online | 实例客户端是否在线。取值： online：在线，表示资产的安全防护状态为开启 。 offline：离线，表示资产的安全防护状态为关闭 。 pause：暂停，表示资产的安全防护状态为暂停保护。 |
| ClientVersion | String | 11 11 _ | 实例客户端版本。 |
| ClusterId | String | 16392368***** | 集群ID。 |
| ClusterName | String | demo-cluster | 集群名称。 |
| CreatedTime | Long | 1609988137000 | 创建时间。使用时间戳格式，单位：毫秒。 |
| ExposedCount | Integer | 5 | 暴露风险漏洞数量。 |
| ExposedStatus | Integer | 0 | 暴露状态。取值： 0：未暴露。 1：已暴露。 |
| Flag | Integer | 1 | 已废弃。 |
| GroupId | String | 3 | 分组ID。 |

| HcStatus | String | NO | 是否有基线问题。取值： YES：有。 NO：无。 |
|---|---|---|---|
| HealthCheckC ount | Integer | 0 | 基线检查问题数。 |
| Importance | Integer | 1 | 已废弃。 |
| InstanceId | String | i-m5*** | 实例ID。 |
| InstanceName | String | yztest-l*** | 实例名称。 |
| InternetIp | String | 47.100.XX.XX | 公网IP。 |
| IntranetIp | String | 192.168.XX.XX | 内网IP。 |
| Ip | String | 192.168.XX.XX | 显示IP（有公网展示公网IP，无公网展示内网 IP）。 |
| Os | String | Linux | 操作系统。 |
| OsName | String | CentOS 7.6 64位 | 操作系统名称。 |
| PodCount | Integer | 1 | 容器组数量。 |
| ProviderAzId | Long | 1 | 已废弃。 |
| ProviderAzNa me | String | 无 | 已废弃。 |
| ProviderId | Long | 1 | 已废弃。 |
| ProviderName | String | 无 | 已废弃。 |
| ProviderRegio nId | Long | 1 | 已废弃。 |
| ProviderRegio nName | String | 无 | 已废弃。 |
| Region | String | cn-demo-***-*** | 区域。 |

| RegionId | String | cn-demo-***-*** | 区域ID。 |
|---|---|---|---|
| RegionName | String | 杭州（中国） | 区域名称。 |
| RiskCount | String | {} | 风险详情。 |
| RiskStatus | String | NO | 资产实例是否存在风险。取值： YES：存在。 NO：不存在。 |
| SafeEventCou nt | Integer | 5 | 资产实例的安全告警数量。 |
| Status | String | Running | 资产实例的开机状态。取值： Running：开机。 notRunning：关机。 |
| Tag | String | InternetIp | 资产实例所属标签名称。 |
| Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | 资产实例的唯一标识ID。 |
| VpcInstanceId | String | classic | 资产实例的所属VPC ID。 |
| VulCount | Integer | 2 | 资产实例的漏洞数量。 |
| VulStatus | String | YES | 资产实例是否有漏洞问题。取值： YES：有。 NO：无。 |
| WeakPassword Count | Integer | 2 | 弱密码检测问题数量。 |
| WeakPassword Status | String | YES | 是否有弱密码问题。取值： YES：有。 NO：无。 |
| PageInfo | Struct |  | 页面显示信息。 |
| Count | Integer | 10 | 当前页显示的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |

| PageSize | Integer | 20 | 每页显示数据条数。 |
|---|---|---|---|
| TotalCount | Integer | 50 | 数据的总条数。 |
| RequestId | String | 32A73759-4C0F- 4801-****- 901223ACEE9A | 本次调用请求的ID。 |
| Success | Boolean | true | 结果的请求状态。取值： true：请求成功。 false：请求失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCloudCenterInstances
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Instances>
    <ProviderId>1</ProviderId>
    <ProviderAzName>无</ProviderAzName>
    <CreatedTime>1609988137000</CreatedTime>
    <Os>Linux</Os>
    <VulStatus>YES</VulStatus>
    <ExposedCount>5</ExposedCount>
    <Ip>192.168.XX.XX</Ip>
    <ProviderRegionName>无</ProviderRegionName>
    <ClientVersion>11_11</ClientVersion>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <RiskCount>{}</RiskCount>
    <PodCount>1</PodCount>
    <Importance>1</Importance>
    <AutoSnapshotsLevel>1</AutoSnapshotsLevel>
    <ProviderRegionId>1</ProviderRegionId>
    <InternetIp>47.100.XX.XX</InternetIp>
```

`<RegionName>`杭州（中国）`</RegionName>`

```xml
    <ClusterName>demo-cluster</ClusterName>
    <ExposedStatus>0</ExposedStatus>
    <Status>Running</Status>
    <ClientStatus>online</ClientStatus>
    <SafeEventCount>5</SafeEventCount>
    <ClusterId>16392368*****</ClusterId>
    <InstanceId>i-m5***</InstanceId>
    <WeakPasswordCount>2</WeakPasswordCount>
    <OsName>CentOS  7.6 64位</OsName>
    <HealthCheckCount>0</HealthCheckCount>
    <ProviderAzId>1</ProviderAzId>
    <WeakPasswordStatus>YES</WeakPasswordStatus>
    <RiskStatus>NO</RiskStatus>
    <Flag>0</Flag>
    <GroupId>3</GroupId>
    <VulCount>2</VulCount>
    <InstanceName>yztest-l***</InstanceName>
    <ProviderName>无</ProviderName>
    <AssetType>ecs</AssetType>
    <Uuid>c9107c04-942f-40c1-981a-f1c1***</Uuid>
    <AlarmStatus>NO</AlarmStatus>
    <Region>cn-demo-***-***</Region>
    <VpcInstanceId>classic</VpcInstanceId>
    <RegionId>cn-demo-***-***</RegionId>
    <Tag>InternetIp</Tag>
    <HcStatus>NO</HcStatus>
</Instances> <PageInfo>
    <TotalCount>50</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>10</Count>
</PageInfo> <RequestId>32A73759-4C0F-4801-****-901223ACEE9A</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "Instances": {
        "ProviderId": 1,
        "ProviderAzName": "无",
        "CreatedTime": 1609988137000,
        "Os": "Linux",
        "VulStatus": "YES",
        "ExposedCount": 5,
        "Ip": "192.168.XX.XX",
        "ProviderRegionName": "无",
        "ClientVersion": "11_11",
        "IntranetIp": "192.168.XX.XX",
        "RiskCount": "{}",
        "PodCount": 1,
        "Importance": 1,
        "AutoSnapshotsLevel": 1,
        "ProviderRegionId": 1,
        "InternetIp": "47.100.XX.XX",
```

`"RegionName": "`杭州（中国）`",`

```json
        "ClusterName": "demo-cluster",
        "ExposedStatus": 0,
        "Status": "Running",
        "ClientStatus": "online",
        "SafeEventCount": 5,
        "ClusterId": "16392368*****",
        "InstanceId": "i-m5***",
        "WeakPasswordCount": 2,
        "OsName": "CentOS  7.6 64位",
        "HealthCheckCount": 0,
        "ProviderAzId": 1,
        "WeakPasswordStatus": "YES",
        "RiskStatus": "NO",
        "Flag": 0,
        "GroupId": 3,
        "VulCount": 2,
        "InstanceName": "yztest-l***",
        "ProviderName": "无",
        "AssetType": "ecs",
        "Uuid": "c9107c04-942f-40c1-981a-f1c1***",
        "AlarmStatus": "NO",
        "Region": "cn-demo-***-***",
        "VpcInstanceId": "classic",
        "RegionId": "cn-demo-***-***",
        "Tag": "InternetIp",
        "HcStatus": "NO"
    },
    "PageInfo": {
        "TotalCount": 50,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 10
    },
```

```json
    "RequestId": "32A73759-4C0F-4801-****-901223ACEE9A",
    "Success": true
}
```

#### DescribeSummaryInfo

调用本接口查询资产的安全评分信息，例如资产的安全分值、已防护资产数量、未防护资产数量。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSumma ryInfo | 系统规定参数。取值：DescribeSummaryInfo。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值： zh：中文。 en：英文。 |
| ResourceDirecto ryAccountId | String | 否 | 无 | 已废弃。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AegisClientOffl ineCount | Integer | 12 | 未防护资产的数量。 |
| AegisClientOnl ineCount | Integer | 127 | 已防护资产的数量。 |
| RequestId | String | D40198E1-6EA8- 482E-****- D9573D75C0CA | 本次调用请求的ID。 |
| SecurityScore | Integer | 44 | 资产的安全分值。分值说明如下： 95-100：表示资产安全状态良好。 85-94：表示资产存在安全隐患，建议尽快加固安全防护体系。 70-84：表示资产存在较多安全隐患，建议及时加固安全防护体系。 69分以下：表示资产防御黑客入侵的能力很弱，建议尽快加固安全防护体系。 |
| Success | Boolean | true | 已废弃。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSummaryInfo
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<AegisClientOnlineCount>127</AegisClientOnlineCount> <RequestId>D40198E1-6EA8-482E-****-D9573D75C0CA</RequestId> <AegisClientOfflineCount>12</AegisClientOfflineCount> <SecurityScore>44</SecurityScore> <Success>true</Success>
```

`JSON` 格式

```json
{
    "AegisClientOnlineCount": 127,
    "RequestId": "D40198E1-6EA8-482E-****-D9573D75C0CA",
    "AegisClientOfflineCount": 12,
    "SecurityScore": 44,
    "Success": true
}
```

### 安全评分

#### DescribeSecureSuggestion

查询安全分相关的安全风险的处理建议详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSecure Suggestion | 需要执行的操作。 取值：DescribeSecureSuggestion。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 取值包括： zh：中文。 en：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | F35F45B0-5D6B- ****-BE02- A62D0760E840 | 阿里云为该请求生成的唯一标识符。 |
| Suggestions | Array of Suggestion |  | 安全风险处理列表。 |
| Detail | Array of Detail |  | 安全风险处理建议的详情。 |
| Description | String | 您有4台RDS受到影响 | 安全风险处理建议的描述。 |
| SubType | String | CLOUD HC RDS _ _ | 安全风险待处理项的类型。 |
| Title | String | RDS-数据库安全策略检查未通过，存在安全风险 | 安全风险待处理项的名称。 |
| Points | Integer | 40 | 单个扣分项的扣分值。 |
| SuggestType | String | SS ALARM _ | 待处理的安全风险的类型。 取值包括： SS REINFORCE：关键功能未配置（例如： _ 防病毒功能）。 SS ALARM：待处理告警。 _ SS VUL：待修复漏洞。 _ SS HC：基线问题。 _ SS AK：AK泄露问题。 _ SS CLOUD HC：云平台配置风险。 _ _ OTHER：其他。 |
| TotalCount | Integer | 15 | 总数据条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSecureSuggestion
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Suggestions>
    <Points>40</Points>
    <SuggestType>SS_ALARM</SuggestType>
    <Detail>
        <SubType>CLOUD_HC_RDS</SubType>
```

`<Description>`您有4台`RDS`受到影响`</Description>` `<Title>RDS-`数据库安全策略检查未通过，存在安全风险`</Title>`

```xml
    </Detail>
</Suggestions> <TotalCount>15</TotalCount> <RequestId>F35F45B0-5D6B-****-BE02-A62D0760E840</RequestId>
```

`JSON` 格式

```json
{
    "Suggestions": {
        "Points": 40,
        "SuggestType": "SS_ALARM",
        "Detail": {
            "SubType": "CLOUD_HC_RDS",
```

`"Description": "`您有4台`RDS`受到影响`",` `"Title": "RDS-`数据库安全策略检查未通过，存在安全风险"

```json
        }
    },
    "TotalCount": 15,
    "RequestId": "F35F45B0-5D6B-****-BE02-A62D0760E840"
}
```

### 获取告警数据

#### DescribeAlarmEventList

获取安全告警处理页面的告警事件信息。告警事件分为告警与异常两个维度，一个告警事件包含多个异常事件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAlarmE ventList | 要执行的操作。 取值：DescribeAlarmEventList。 |
| CurrentPage | Integer | 是 | 1 | 当前页的页码。 |
| From | String | 是 | sas | 请求来源标识，固定为sas。 |
| PageSize | String | 是 | 20 | 每页最多显示的数据条数。 |

| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
|---|---|---|---|---|
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值： zh：中文。 en：英文。 |
| Dealed | String | 否 | Y | 告警事件状态。取值： N：待处理告警。 Y：已处理告警。 |
| Levels | String | 否 | serious | 告警事件的危险等级，多个严重等级用逗号分隔（严重等级递减）。取值： serious：紧急。 suspicious：可疑。 remind：提醒。 |
| Remark | String | 否 | database server _ | 告警名称/资产信息。 |
| GroupId | String | 否 | tst*** | 告警事件受影响资产的分组ID。 |
| AlarmEventNam e | String | 否 | DDoS木马 | 告警事件名称。 |
| AlarmEventType | String | 否 | 恶意进程（云查杀） | 告警事件类型。 |
| UniqueInfo | String | 否 | asdasjhdk**** | 唯一标识。 |

| OperateErrorCod eList.N | RepeatL ist | 否 | ignore. Success | 告警事件处理结果码。格式为：操作类型. 操作结果码。包括以下操作类型： Common：通用操作。 deal：处理。 ignore：忽略。 offline handled：告警已确认。 _ mark mis info：加白名单。 _ _ rm mark mis info：取消加白名 _ _ _ 单。 quara：隔离。 kill and quara：普通查杀。 _ _ kill virus：深度清理。 _ block ip：阻断。 _ manual handled：手工处理。 _ 操作结果码： Success：成功。 Failure：失败。 AgentOffline：客户端离线。 |
|---|---|---|---|---|
| ClusterId | String | 否 | dasdaS****** | 容器防护：集群ID。 |
| ContainerFieldN ame | String | 否 | containerId | 容器防护：容器查询key。 |
| ContainerFieldV alue | String | 否 | sadskdjhaskjdha sd***** | 容器防护：容器查询value。 |
| TargetType | String | 否 | containerId | 容器防护：ContainerFieldName和Contai nerFieldValue筛选目标内容。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 页面显示信息。 |
| Count | Integer | 1 | 总页码数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 1 | 总数据条数。 |

| RequestId | String | 28267723-D857- 4DD8-****- 013100000000 | 本次调用请求的ID。 |
|---|---|---|---|
| SuspEvents | Array of SuspEvents |  | 告警事件信息。 |
| AlarmEventNa me | String | 执行恶意命令 | 告警事件名称。 |
| AlarmEventNa meOriginal | String | 恶意命令执行精准防御 | 告警事件原始父名称。 |
| AlarmEventTy pe | String | 进程异常行为 | 告警事件类型。 |
| AlarmUniqueIn fo | String | 8df9******f4211fbf 756ef***** | 告警事件的唯一标识ID。 |
| AppName | String | app1 | 应用名。 |
| CanBeDealOnL ine | Boolean | true | 是否能在线处理告警事件，例如阻断隔离、加白名单、忽略等。 true：支持在线处理。 false：不支持在线处理。 |
| CanCancelFaul t | Boolean | false | 能否取消标记为误报。 true：能。 false：不能。 |
| ContainHwMod e | Boolean | false | 是否开启护网模式。 true：是。 false：否。 |
| ContainerId | String | sadjadash*** | 容器ID。 |
| ContainerImag eId | String | cri-asdaks***** | 容器镜像ID。 |
| ContainerImag eName | String | centos1 | 容器镜像名。 |
| DataSource | String | aegis *** _ | 数据来源。 |
| Dealed | Boolean | false | 告警是否已处理。 true：已处理。 false：待处理。 |

| Description | String | 黑客入侵服务器后， 为了让恶意后门程序能持久化运行，黑客常常将恶意SHELL脚本写入crontab、 systemd等计划任务。 | 告警事件的描述。 |
|---|---|---|---|
| EndTime | Long | 1543740301000 | 告警事件结束时间。使用时间戳格式，单位：毫秒。 |
| GmtModified | Long | 1569235879000 | 告警最新发生时间。使用时间戳格式，单位：毫秒。 |
| HasTraceInfo | Boolean | true | 告警是否有溯源信息。 true：有溯源。 false：无溯源。 |
| InstanceId | String | i-e*** | 受影响资产实例ID。 |
| InstanceName | String | 测试服务器 | 受影响资产实例的名称。 |
| InternetIp | String | 47.100.XX.XX | 受影响资产实例的公网IP。 |
| IntranetIp | String | 192.168.XX.XX | 受影响资产实例的私网IP。 |
| K8sClusterId | String | cb9218d50728c47 0fb7dfbc16***** | Kubernetes集群ID。 |
| K8sClusterNa me | String | cqqtesttest | Kubernetes集群名。 |
| K8sNamespac e | String | kube-system | Kubernetes命名空间。 |
| K8sNodeId | String | i-km100o6qy****** | Kubernetes节点ID。 |
| K8sNodeName | String | node1 | Kubernetes节点名。 |
| K8sPodName | String | podname1 | Kubernetes容器组名。 |
| Level | String | serious | 告警事件的危险等级。 serious：紧急。 suspicious：可疑。 remind：提醒。 |

| OperateErrorC ode | String | kill and quara.Suc _ _ cess | 告警处理结果码。 |
|---|---|---|---|
| OperateTime | Long | 1234567890123 | 操作时间。 使用时间戳格式，单位：毫秒。 |
| SaleVersion | String | 1 | 告警事件检测支持的售卖版本。 0：基础版本。 1：企业版本。 |
| SecurityEventI ds | String | 1 | 关联异常的ID。 |
| Solution | String | 请及时排查告警中提示的恶意URL，以及所下载的目录下的恶意文件，并及时清理已运行的恶意进程。 如果该指令是您自己主动执行的，您可以在控制台点击标记为误报。 | 告警事件的处理方法。 |
| Stages | String | ["attack entrance"] _ | 阶段。 |
| StartTime | Long | 1543740301000 | 告警事件的开始时间。使用时间戳格式，单位： 毫秒。 |
| SuspiciousEve ntCount | Integer | 1 | 关联的异常事件的条数。 |
| Uuid | String | 47900178-885d- 4fa4-9d77-*** | 关联实例的唯一标识。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventList &CurrentPage=1 &From=sas &PageSize=20
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PageInfo>
    <TotalCount>1</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>1</Count>
</PageInfo> <RequestId>28267723-D857-4DD8-****-013100000000</RequestId> <SuspEvents>
    <K8sNodeId>i-km100o6qy******</K8sNodeId>
```

`<Description>`黑客入侵服务器后，为了让恶意后门程序能持久化运行，黑客常常将恶意`SHELL`脚本写入`cront` `ab`、`systemd`等计划任务。`</Description>`

```xml
    <K8sNodeName>node1</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <EndTime>1543740301000</EndTime>
    <OperateErrorCode>kill_and_quara.Success</OperateErrorCode>
```

`<AlarmEventName>`执行恶意命令`</AlarmEventName>`

```xml
    <SecurityEventIds>1</SecurityEventIds>
    <GmtModified>1569235879000</GmtModified>
    <HasTraceInfo>true</HasTraceInfo>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>cb9218d50728c470fb7dfbc16*****</K8sClusterId>
    <AppName>app1</AppName>
    <K8sNamespace>kube-system</K8sNamespace>
    <InternetIp>47.100.XX.XX</InternetIp>
    <ContainerId>sadjadash***</ContainerId>
```

`<AlarmEventType>`进程异常行为`</AlarmEventType>` `<Solution>`请及时排查告警中提示的恶意`URL`，以及所下载的目录下的恶意文件，并及时清理已运行的恶意进程 。如果该指令是您自己主动执行的，您可以在控制台点击标记为误报。`</Solution>`

```xml
    <CanCancelFault>false</CanCancelFault>
```

`<AlarmEventNameOriginal>`恶意命令执行精准防御`</AlarmEventNameOriginal>`

```xml
    <InstanceId>i-e***</InstanceId>
    <Stages>["attack_entrance"]</Stages>
    <StartTime>1543740301000</StartTime>
    <K8sPodName>podname1</K8sPodName>
    <SaleVersion>1</SaleVersion>
    <Dealed>false</Dealed>
    <ContainerImageId>cri-asdaks*****</ContainerImageId>
    <DataSource>aegis_***</DataSource>
    <InstanceName>测试服务器</InstanceName>
    <OperateTime>1234567890123</OperateTime>
    <CanBeDealOnLine>true</CanBeDealOnLine>
    <K8sClusterName>cqqtesttest</K8sClusterName>
    <Uuid>47900178-885d-4fa4-9d77-***</Uuid>
    <ContainerImageName>centos1</ContainerImageName>
    <SuspiciousEventCount>1</SuspiciousEventCount>
    <AlarmUniqueInfo>8df9******f4211fbf756ef*****</AlarmUniqueInfo>
    <Level>serious</Level>
</SuspEvents>
```

`JSON` 格式

```json
{
    "PageInfo": {
        "TotalCount": 1,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 1
    },
    "RequestId": "28267723-D857-4DD8-****-013100000000",
    "SuspEvents": {
        "K8sNodeId": "i-km100o6qy******",
```

`"Description": "`黑客入侵服务器后，为了让恶意后门程序能持久化运行，黑客常常将恶意`SHELL`脚本写入`crontab`、`systemd`等计划任务。`",`

```json
        "K8sNodeName": "node1",
        "ContainHwMode": false,
        "EndTime": 1543740301000,
        "OperateErrorCode": "kill_and_quara.Success",
```

`"AlarmEventName": "`执行恶意命令`",`

```json
        "SecurityEventIds": 1,
        "GmtModified": 1569235879000,
        "HasTraceInfo": true,
        "IntranetIp": "192.168.XX.XX",
        "K8sClusterId": "cb9218d50728c470fb7dfbc16*****",
        "AppName": "app1",
        "K8sNamespace": "kube-system",
        "InternetIp": "47.100.XX.XX",
        "ContainerId": "sadjadash***",
```

`"AlarmEventType": "`进程异常行为`",` `"Solution": "`请及时排查告警中提示的恶意`URL`，以及所下载的目录下的恶意文件，并及时清理已运行的恶意进程。如果该指令是您自己主动执行的，您可以在控制台点击标记为误报。`",`

```json
        "CanCancelFault": false,
```

`"AlarmEventNameOriginal": "`恶意命令执行精准防御`",`

```json
        "InstanceId": "i-e***",
        "Stages": "[\"attack_entrance\"]",
        "StartTime": 1543740301000,
        "K8sPodName": "podname1",
        "SaleVersion": 1,
        "Dealed": false,
        "ContainerImageId": "cri-asdaks*****",
        "DataSource": "aegis_***",
```

`"InstanceName": "`测试服务器`",`

```json
        "OperateTime": 1234567890123,
        "CanBeDealOnLine": true,
        "K8sClusterName": "cqqtesttest",
        "Uuid": "47900178-885d-4fa4-9d77-***",
        "ContainerImageName": "centos1",
        "SuspiciousEventCount": 1,
        "AlarmUniqueInfo": "8df9******f4211fbf756ef*****",
        "Level": "serious"
    }
}
```

#### DescribeAlarmEventDetail

获取告警事件的详细信息。告警事件分为告警与异常两个维度，一个告警事件包含多个异常事件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAlarmE ventDetail | 要执行的操作。 取值：DescribeAlarmEventDetail。 |
| AlarmUniqueInfo | String | 是 | 8df************* *********** | 告警事件的唯一标识。 说明查询警事件的详细信息，需要提供告警事件的唯一标识信息，该标识信息可调用 DescribeAlarmEventList接口获取。 |
| From | String | 是 | sas | 请求来源标识，固定为sas。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值包括： zh：中文。 en：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 告警事件详情。 |
| AlarmEventAli asName | String | 网站后门-发现后门 （Webshell）文件 | 告警类型别名。 |
| AlarmEventDe sc | String | 黑客入侵服务器后， 为了让恶意后门程序能持久化运行，黑客常常将恶意SHELL脚本写入crontab、 systemd等计划任务。 | 告警事件描述。 |
| AlarmUniqueIn fo | String | asds************ | 告警事件的唯一标识。 |
| AppName | String | demo-name | Kubernetes应用名。 |

| CanBeDealOnL ine | Boolean | false | 是否支持在线处理告警事件，例如阻断隔离、加白名单、忽略等。取值： true：支持在线处理。 false：不支持在线处理。 |
|---|---|---|---|
| CanCancelFaul t | Boolean | false | 能否取消标记为误报。取值： true：可以取消标记为误报。 false：不能取消标记为误报。 |
| CauseDetails | Array of CauseDetail |  | 告警事件发生的原因（溯源信息）。 |
| Key | String | item | 溯源信息字段的Key。 |
| Value | Array of Value |  | 溯源信息字段值。 |
| Name | String | 排查方案 | 溯源信息字段名。 |
| Type | String | html | 溯源信息字段展示的类型，取值： html。 text。 |
| Value | String | 请根据上述信息排查您的WEB服务被利用的页面及参数是否存在漏洞，并及时修复。 | 溯源信息字段的值。 |
| ContainHwMod e | Boolean | false | 是否开启护网模式。取值： true：开启。 false：关闭。 |
| ContainerId | String | B4*****-3***-4***- B***-9F******** | 容器ID。 |
| ContainerImag eId | String | docker- pullable://registry.a cs.demo.com/acs/a liyun-demo- controller:demo | 容器镜像ID。 |
| ContainerImag eName | String | registry.acs.demo. com/acs/aliyun- demo- controller:demo | 容器镜像名。 |
| DataSource | String | demo *** _ | 数据来源。 |

| EndTime | Long | 1542366542000 | 告警事件结束时间。使用时间戳格式，单位：毫秒。 |
|---|---|---|---|
| InstanceName | String | worker-k8s-for-cs- cb9****** | 实例名称。 |
| InternetIp | String | 47.100.XX.XX | 公网IP。 |
| IntranetIp | String | 192.168.XX.XX | 内网IP。 |
| K8sClusterId | String | cb9218*********** | Kubernetes集群ID。 |
| K8sClusterNa me | String | demo******* | Kubernetes集群名。 |
| K8sNamespac e | String | kube-system | Kubernetes命名空间。 |
| K8sNodeId | String | i-km10********** | Kubernetes节点ID。 |
| K8sNodeName | String | cn-wulan-env116- d01.i- km10*********** | Kubernetes节点名。 |
| K8sPodName | String | nginx-ingress- controller-5b******- l4*** | Kubernetes容器组名。 |
| Level | String | serious | 告警事件的危险等级。取值： serious：紧急。 suspicious：可疑。 remind：提醒。 |
| Solution | String | 请及时排查告警中提示的恶意URL，以及所下载的目录下的恶意文件。并及时清理已运行的恶意进程。 如果该指令是您自己主动执行，您可以在控制台点击标记为误报，并通过工单方式反馈给我们的安全工程师。 | 告警事件的处理方法。 |
| StartTime | Long | 1542378601000 | 告警事件开始时间。使用时间戳格式，单位：毫秒。 |
| Type | String | 异常网络连接 | 告警事件类型。 |

| Uuid | String | B41******-3***- 4***-B***- 9********* | 机器UUID。 |
|---|---|---|---|
| RequestId | String | B41******-3***- 4***-B***- 9********* | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventDetail &AlarmUniqueInfo=8df914418f4211fbf756efe7a6f40cbc &From=sas
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>B41******-3***-4***-B***-9*********</RequestId> <Data>
    <K8sNodeId>i-km10**********</K8sNodeId>
    <K8sNodeName>cn-wulan-env116-d01.i-km10***********</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <EndTime>1542366542000</EndTime>
    <IntranetIp>192.168.0.100</IntranetIp>
    <K8sClusterId>cb9218***********</K8sClusterId>
    <AppName>demo-name</AppName>
    <K8sNamespace>kube-system</K8sNamespace>
    <InternetIp>123.123.123.123</InternetIp>
    <ContainerId>B4*****-3***-4***-B***-9F********</ContainerId>
```

`<AlarmEventDesc>`黑客入侵服务器后，为了让恶意后门程序能持久化运行，黑客常常将恶意`SHELL`脚本写入`cr` `ontab`、`systemd`等计划任务。`</AlarmEventDesc>` `<Solution>`请及时排查告警中提示的恶意`URL`，以及所下载的目录下的恶意文件。并及时清理已运行的恶意进程 。如果该指令是您自己主动执行，您可以在控制台点击标记为误报，并通过工单方式反馈给我们的安全工程师。`</Sol`

```xml
ution>
    <CanCancelFault>false</CanCancelFault>
    <StartTime>1542378601000</StartTime>
    <K8sPodName>nginx-ingress-controller-5b******-l4***</K8sPodName>
    <ContainerImageId>docker-pullable://registry.acs.demo.com/acs/aliyun-demo-
controller:demo</ContainerImageId>
    <DataSource>demo_***</DataSource>
    <InstanceName>worker-k8s-for-cs-cb9******</InstanceName>
    <CanBeDealOnLine>false</CanBeDealOnLine>
```

`<Type>`异常网络连接`</Type>`

```xml
    <K8sClusterName>demo*******</K8sClusterName>
    <Uuid>B41******-3***-4***-B***-9*********</Uuid>
    <ContainerImageName>registry.acs.demo.com/acs/aliyun-demo-
controller:demo</ContainerImageName>
    <AlarmUniqueInfo>asds************</AlarmUniqueInfo>
```

`<AlarmEventAliasName>`网站后门-发现后门（`Webshell`）文件`</AlarmEventAliasName>`

```xml
    <Level>serious</Level>
    <CauseDetails>
        <Key>item</Key>
        <Value>
            <Type>html</Type>
```

`<Value>`请根据上述信息排查您的`WEB`服务被利用的页面及参数是否存在漏洞，并及时修复。`</Value` > `<Name>`排查方案`</Name>`

```
        </Value>
    </CauseDetails>
</Data>
```

`JSON` 格式

```json
{
    "RequestId": "B41******-3***-4***-B***-9*********",
    "Data": {
        "K8sNodeId": "i-km10**********",
        "K8sNodeName": "cn-wulan-env116-d01.i-km10***********",
        "ContainHwMode": false,
        "EndTime": 1542366542000,
        "IntranetIp": "192.168.0.100",
        "K8sClusterId": "cb9218***********",
        "AppName": "demo-name",
        "K8sNamespace": "kube-system",
        "InternetIp": "123.123.123.123",
        "ContainerId": "B4*****-3***-4***-B***-9F********",
```

`"AlarmEventDesc": "`黑客入侵服务器后，为了让恶意后门程序能持久化运行，黑客常常将恶意`SHELL`脚本写入`crontab`、`systemd`等计划任务。`",` `"Solution": "`请及时排查告警中提示的恶意`URL`，以及所下载的目录下的恶意文件。并及时清理已运行的恶意进程。如果该指令是您自己主动执行，您可以在控制台点击标记为误报，并通过工单方式反馈给我们的安全工程师 。`",`

```json
        "CanCancelFault": false,
        "StartTime": 1542378601000,
        "K8sPodName": "nginx-ingress-controller-5b******-l4***",
        "ContainerImageId": "docker-pullable://registry.acs.demo.com/acs/aliyun-demo-co
ntroller:demo",
        "DataSource": "demo_***",
        "InstanceName": "worker-k8s-for-cs-cb9******",
        "CanBeDealOnLine": false,
```

`"Type": "`异常网络连接`",`

```json
        "K8sClusterName": "demo*******",
        "Uuid": "B41******-3***-4***-B***-9*********",
        "ContainerImageName": "registry.acs.demo.com/acs/aliyun-demo-controller:demo",
        "AlarmUniqueInfo": "asds************",
```

`"AlarmEventAliasName": "`网站后门-发现后门（`Webshell`）文件`",`

```json
        "Level": "serious",
        "CauseDetails": {
            "Key": "item",
            "Value": {
                "Type": "html",
```

`"Value": "`请根据上述信息排查您的`WEB`服务被利用的页面及参数是否存在漏洞，并及时修复。 `",` `"Name": "`排查方案"

```
            }
        }
    }
}
```

#### DescribeSuspEvents

查询异常事件信息。告警事件分为告警与异常两个维度，一个告警事件包含多个异常事件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribeSuspEv ents | 需要执行的操作。 取值：DescribeSuspEvents。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Dealed | String | 否 | N | 异常事件状态。取值包括： N：待处理。 Y：已处理。 |
| Name | String | 否 | ecs-xxx | 异常事件名称或者是主机名称，支持模糊匹配。 |
| Levels | String | 否 | serious | 异常事件的危险等级，多个危险等级用英文逗号分隔。以下危险等级严重程度依次递减： serious：紧急。 suspicious：可疑。 remind：提醒。 |
| ParentEventTyp es | String | 否 | 网站后门 | 告警事件类型。取值： 进程异常行为。 网站后门。 异常登录。 异常事件。 敏感文件篡改。 恶意进程（云查杀）。 异常网络连接。 其他。 异常账号。 应用入侵事件。 云产品威胁检测。 精准防御。 应用白名单。 持久化后门。 Web应用威胁检测。 恶意脚本。 威胁情报。 恶意网络行为。 |
| Remark | String | 否 | 测试机器 | 主机IP或者名称。 |
| Status | String | 否 | 无 | 已废弃。 |
| PageSize | String | 否 | 20 | 每页最多显示的数据条数。 |

| CurrentPage | String | 否 | 1 | 当前页的页码。 |
|---|---|---|---|---|
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值包括： zh：中文。 en：英文。 |
| AlarmUniqueInfo | String | 否 | 8df914418f4211 fbf*** | 异常事件所属告警事件的唯一标识ID。 说明如果查询单个告警事件的异常事件信息，需要提供告警事件的唯一标识ID，该ID可调用DescribeAlarmEventList接口获取。 |
| UniqueInfo | String | 否 | a0************** ******* | 唯一信息。 |
| From | String | 否 | sas | 异常事件所属数据源标识，固定为sas。 |
| Source | String | 否 | 47.100.XX.XX | 访问源IP地址。 |
| GroupId | Long | 否 | 1 | 分组ID。 |
| Uuids | String | 否 | xxxx-xx-xxxx- xxxx-xxxx | 主机资产UUID，多个UUID之间需要用英文逗号分隔。 |
| OperateErrorCod eList.N | RepeatL ist | 否 | 无 | 已废弃。 |
| ClusterId | String | 否 | 1 | 容器防护：集群ID。 |
| ContainerFieldN ame | String | 否 | appName1 | 容器防护：容器查询key。 |
| ContainerFieldV alue | String | 否 | nginx-***- controller | 容器防护：容器查询value。 |
| TargetType | String | 否 | containerId | 容器防护：ContainerFieldName条件和ContainerFieldValue条件查询目标类型。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 1 | 总页码数。 |

| CurrentPage | Integer | 1 | 当前页的页码。 |
|---|---|---|---|
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| RequestId | String | 43F670F3-AB40- 4E91-****- C57400000000 | 本次调用请求的ID。 |
| SuspEvents | Array of WarningSumm ary |  | 异常事件信息。 |
| Advanced | Boolean | false | 是否是高级版。取值： true：是。 false：否。 |
| AlarmEventNa me | String | DDoS木马 | 告警事件名称。 |
| AlarmEventNa meDisplay | String | 无 | 已废弃。 |
| AlarmEventTy pe | String | 恶意进程（云查杀） | 告警事件类型。 |
| AlarmEventTy peDisplay | String | 无 | 已废弃。 |
| AlarmUniqueIn fo | String | 8df914418f*** | 告警事件的唯一标识ID。 |
| AppName | String | demo-name | Kubernetes应用名。 |
| AutoBreaking | Boolean | false | 是否自动拦截。取值： true：是。 false：否。 |
| CanBeDealOnL ine | Boolean | true | 是否支持在线处理异常事件，例如隔离。取值包括： true：支持在线处理。 false：不支持在线处理。 |
| CanCancelFaul t | Boolean | false | 能否取消标记为误报。取值： true：可以取消标记为误报。 false：不能取消标记为误报。 |

| ContainHwMod e | Boolean | false | 是否开启护网模式。取值： true：开启 。 false：关闭。 |
|---|---|---|---|
| ContainerId | String | B4*****-3***-4***- B***-9F******** | 容器ID。 |
| ContainerImag eId | String | docker- pullable://registry.a cs.***.com/acs/aliy un-**- controller:demo | 容器镜像ID。 |
| ContainerImag eName | String | registry.acs.demo. com/acs/aliyun-**- controller:demo | 容器镜像名。 |
| DataSource | String | aegis suspicious * _ _ ** | 数据来源。 |
| Desc | String | XorDDoS木马 | 异常事件详情。 |
| Details | Array of QuaraFile |  | 文案列表。 |
| InfoType | String | download url _ | 图标展示的类型。 |
| Name | String | 告警描述 | 文案的标题。 |
| NameDisplay | String | 无 | 已废弃。 |
| Type | String | html | 文案展示的方式。取值包括： text：文本方式。 html：富文本的方式。 |
| Value | String | 描述内容 | 文案的内容。 |
| ValueDisplay | String | 无 | 已废弃。 |
| EventNotes | Array of EventNote |  | 备注列表。 |
| Note | String | 备注内容 | 备注内容。 |
| NoteId | Long | 1 | 备注内容ID。 |

| NoteTime | String | 2018-12-12 12:00:00 | 备注时间。使用yyyy-MM-dd HH:mm:ss格式。 |
|---|---|---|---|
| EventStatus | Integer | 1 | 异常事件的状态。取值包括： 1：PENDING（待处理）。 2：IGNORE（已忽略）。 4：HANDLED（已确认）。 8：FAULT（已标记误报）。 16：DEALING（处理中）。 32：DONE（处理完毕）。 64：EXPIRE（已经过期）。 |
| EventSubType | String | XorDDoS木马 | 异常事件名称。 |
| HasTraceInfo | Boolean | false | 已废弃。 |
| Id | Long | 1000 | 记录异常事件的唯一标识ID。 |
| InstanceId | String | i-km10********* | 实例ID。 |
| InstanceName | String | nginx | 关联实例的名称。 |
| InternetIp | String | 47.100.XX.XX | 关联实例的公网IP。 |
| IntranetIp | String | 192.168.XX.XX | 关联实例的私网IP。 |
| K8sClusterId | String | cb9218*********** | Kubernetes集群ID。 |
| K8sClusterNa me | String | demo******* | Kubernetes集群名。 |
| K8sNamespac e | String | kube-**** | Kubernetes命名空间。 |
| K8sNodeId | String | i-km10********** | Kubernetes节点ID。 |
| K8sNodeName | String | cn-wulan-env116- d01.i- km10*********** | Kubernetes节点名称。 |
| K8sPodName | String | nginx-ingress- controller-5b******- l4*** | Kubernetes容器组名。 |

| LastTime | String | 2018-09-26 01:51:01 | 异常事件最新发生时间。使用yyyy-MM-dd HH:mm:ss格式。 |
|---|---|---|---|
| LastTimeStam p | Long | 1639236844747 | 最后一次发生时间。使用时间戳格式，单位：毫秒。 |
| Level | String | serious | 异常事件的危险等级。取值包括： serious：紧急。 suspicious：可疑。 remind：提醒。 |
| MarkMisRules | String | ***木马文件路径 *****包含**** | 高级加白规则。 |
| Name | String | 恶意进程（云查杀）- XorDDoS木马 | 异常事件的完整名称。 |
| OccurrenceTi me | String | 2018-09-26 01:51:01 | 异常事件首次发生的时间。使用yyyy-MM-dd HH:mm:ss格式。 |
| OccurrenceTi meStamp | Long | 1639236844747 | 首次发生时间。使用时间戳格式，单位：毫秒。 |
| OperateErrorC ode | String | quara.Succes | 事件的处理结果。 |
| OperateMsg | String | success | 异常事件操作的备注信息。 |
| OperateTime | Long | 1639236844747 | 操作时间。使用时间戳格式，单位：毫秒。 |
| SaleVersion | String | 1 | 异常事件检测支持的产品售卖版本。取值包括： 0：基础版本。 1：企业版本。 |
| SecurityEventI ds | String | 无 | 已废弃。 |
| Stages | String | [] | 事件所处阶段。 |
| UniqueInfo | String | e17e*** | 异常事件的唯一标识ID。 |
| Uuid | String | bf6b30d3-eea8- 4924-9f0a-*** | 关联实例的唯一标识。 |
| TotalCount | Integer | 100 | 总数据条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSuspEvents
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>100</TotalCount> <PageSize>20</PageSize> <RequestId>43F670F3-AB40-4E91-****-C57400000000</RequestId> <CurrentPage>1</CurrentPage> <Count>1</Count> <SuspEvents>
    <K8sNodeId>i-km10**********</K8sNodeId>
    <Advanced>false</Advanced>
    <K8sNodeName>cn-wulan-env116-d01.i-km10***********</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <OperateErrorCode>quara.Succes</OperateErrorCode>
    <AlarmEventName>DDoS木马</AlarmEventName>
    <SecurityEventIds>无</SecurityEventIds>
    <EventStatus>1</EventStatus>
    <HasTraceInfo>false</HasTraceInfo>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>cb9218***********</K8sClusterId>
    <EventSubType>XorDDoS木马</EventSubType>
    <AppName>demo-name</AppName>
```

`<Name>`恶意进程（云查杀）`-XorDDoS`木马`</Name>`

```xml
    <K8sNamespace>kube-****</K8sNamespace>
    <Desc>XorDDoS木马</Desc>
    <LastTimeStamp>1639236844747</LastTimeStamp>
    <InternetIp>47.100.XX.XX</InternetIp>
    <ContainerId>B4*****-3***-4***-B***-9F********</ContainerId>
```

`<AlarmEventType>`恶意进程（云查杀）`</AlarmEventType>`

```xml
    <AlarmEventNameDisplay>无</AlarmEventNameDisplay>
    <UniqueInfo>e17e***</UniqueInfo>
    <CanCancelFault>false</CanCancelFault>
    <AlarmEventTypeDisplay>无</AlarmEventTypeDisplay>
    <InstanceId>i-km10*********</InstanceId>
    <Stages>[]</Stages>
```

`<MarkMisRules>***`木马文件路径`*****`包含`****</MarkMisRules>`

```xml
    <K8sPodName>nginx-ingress-controller-5b******-l4***</K8sPodName>
    <SaleVersion>1</SaleVersion>
    <ContainerImageId>docker-pullable://registry.acs.***.com/acs/aliyun-**-
controller:demo</ContainerImageId>
    <DataSource>aegis_suspicious_***</DataSource>
    <InstanceName>nginx</InstanceName>
    <OccurrenceTime>2018-09-26 01:51:01</OccurrenceTime>
    <OperateTime>1639236844747</OperateTime>
    <CanBeDealOnLine>true</CanBeDealOnLine>
    <OperateMsg>success</OperateMsg>
    <K8sClusterName>demo*******</K8sClusterName>
    <Uuid>bf6b30d3-eea8-4924-9f0a-***</Uuid>
<ContainerImageName>registryacsdemocom/acs/aliyun-**-
```

```xml
    <ContainerImageName>registry.acs.demo.com/acs/aliyun
controller:demo</ContainerImageName>
    <AlarmUniqueInfo>8df914418f***</AlarmUniqueInfo>
    <AutoBreaking>false</AutoBreaking>
    <OccurrenceTimeStamp>1639236844747</OccurrenceTimeStamp>
    <Level>serious</Level>
    <Id>1000</Id>
    <LastTime>2018-09-26 01:51:01</LastTime>
    <Details>
        <Type>html</Type>
```

`<Value>`描述内容`</Value>`

```xml
        <ValueDisplay>无</ValueDisplay>
        <InfoType>download_url</InfoType>
        <NameDisplay>无</NameDisplay>
```

`<Name>`告警描述`</Name>`

```xml
    </Details>
    <EventNotes>
        <NoteId>1</NoteId>
```

`<Note>`备注内容`</Note>`

```xml
        <NoteTime>2018-12-12 12:00:00</NoteTime>
    </EventNotes>
</SuspEvents>
```

`JSON` 格式

```json
{
    "TotalCount": 100,
    "PageSize": 20,
    "RequestId": "43F670F3-AB40-4E91-****-C57400000000",
    "CurrentPage": 1,
    "Count": 1,
    "SuspEvents": {
        "K8sNodeId": "i-km10**********",
        "Advanced": false,
        "K8sNodeName": "cn-wulan-env116-d01.i-km10***********",
        "ContainHwMode": false,
        "OperateErrorCode": "quara.Succes",
        "AlarmEventName": "DDoS木马",
        "SecurityEventIds": "无",
        "EventStatus": 1,
        "HasTraceInfo": false,
        "IntranetIp": "192.168.XX.XX",
        "K8sClusterId": "cb9218***********",
        "EventSubType": "XorDDoS木马",
        "AppName": "demo-name",
```

`"Name": "`恶意进程（云查杀）`-XorDDoS`木马`",`

```json
        "K8sNamespace": "kube-****",
        "Desc": "XorDDoS木马",
        "LastTimeStamp": 1639236844747,
        "InternetIp": "47.100.XX.XX",
        "ContainerId": "B4*****-3***-4***-B***-9F********",
```

`"AlarmEventType": "`恶意进程（云查杀）`",`

```json
        "AlarmEventNameDisplay": "无",
        "UniqueInfo": "e17e***",
```

`"C` `lF`

```
lt"
```

fl

```json
        "CanCancelFault": false,
        "AlarmEventTypeDisplay": "无",
        "InstanceId": "i-km10*********",
        "Stages": "[]",
```

`"MarkMisRules": "***`木马文件路径`*****`包含`****",`

```json
        "K8sPodName": "nginx-ingress-controller-5b******-l4***",
        "SaleVersion": 1,
        "ContainerImageId": "docker-pullable://registry.acs.***.com/acs/aliyun-**-contr
oller:demo",
        "DataSource": "aegis_suspicious_***",
        "InstanceName": "nginx",
        "OccurrenceTime": "2018-09-26 01:51:01",
        "OperateTime": 1639236844747,
        "CanBeDealOnLine": true,
        "OperateMsg": "success",
        "K8sClusterName": "demo*******",
        "Uuid": "bf6b30d3-eea8-4924-9f0a-***",
        "ContainerImageName": "registry.acs.demo.com/acs/aliyun-**-controller:demo",
        "AlarmUniqueInfo": "8df914418f***",
        "AutoBreaking": false,
        "OccurrenceTimeStamp": 1639236844747,
        "Level": "serious",
        "Id": 1000,
        "LastTime": "2018-09-26 01:51:01",
        "Details": {
            "Type": "html",
```

`"Value": "`描述内容`",`

```json
            "ValueDisplay": "无",
            "InfoType": "download_url",
            "NameDisplay": "无",
```

`"Name": "`告警描述"

```json
        },
        "EventNotes": {
            "NoteId": 1,
```

`"Note": "`备注内容`",`

```json
            "NoteTime": "2018-12-12 12:00:00"
        }
    }
}
```

#### DescribeSuspEventDetail

查询单个异常事件详情。告警事件分为告警与异常两个维度，一个告警事件包含多个异常事件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSuspEv entDetail | 要执行的操作。 取值：DescribeSuspEventDetail。 |

| From | String | 是 | sas | 异常事件数据的来源，固定为sas。 |
|---|---|---|---|---|
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值包括： zh：中文。 en：英文。 |
| SuspiciousEventI d | Integer | 否 | 1 | 记录异常事件的唯一标识ID。 说明查询单个异常事件信息，需要提供记录异常事件的唯一标识ID，该ID可调用 DescribeSuspEvents接口获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CanBeDealOnL ine | Boolean | true | 是否支持在线处理异常事件。取值包括： true：支持在线处理。 false：不支持在线处理。 |
| DataSource | String | aegis suspicious * _ _ ** | 异常事件的数据来源。 |
| Details | Array of QuaraFile |  | 异常事件的详情。 |
| InfoType | String | download url _ | 图标展示的类型。 |
| Name | String | 告警描述 | 文案的标题。 |
| Type | String | html | 文案展示的方式。取值包括： text：文本方式。 html：富文本的方式。 |
| Value | String | 描述内容 | 文案的内容。 |
| EventDesc | String | 该文件极有可能是黑客成功入侵网站后种植的，建议您先确认文件合法性并处理 | 异常事件描述。 |
| EventName | String | WEBSHELL | 异常事件的名称。 |

| EventStatus | String | 32 | 异常事件状态。取值包括： 1：待处理。 2：已忽略。 4：已确认。 8：已标记误报。 16：处理中。 32：处理完毕。 64：已经过期。 |
|---|---|---|---|
| EventTypeDes c | String | 网站后门-发现后门 (Webshell)文件 | 异常事件类型说明。 |
| Id | Integer | 1 | 告警事件ID。 |
| InstanceName | String | worker-k8s-for-cs- cb9****** | 实例的名称。 |
| InternetIp | String | 47.100.XX.XX | 公网IP。 |
| IntranetIp | String | 192.168.XX.XX | 内网IP。 |
| LastTime | String | 2018-10-30 11:43:46 | 最新时间。使用yyyy-MM-dd HH:mm:ss格式。 |
| Level | String | serious | 异常事件的危险等级。取值包括： serious：紧急。 suspicious：可疑。 remind：提醒。 |
| OperateErrorC ode | String | quara.Succes | 事件的处理结果。 |
| OperateMsg | String | success | 事件的处理结果的描述信息。 |
| RequestId | String | 1 | 本次调用请求的ID。 |
| SaleVersion | String | 无 | 已废弃。 |
| SasId | String | 无 | 已废弃。 |
| Uuid | String | B41******-3***- 4***-B***- 9********* | 机器UUID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSuspEventDetail &From=sas
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 `<EventDesc>`该文件极有可能是黑客成功入侵网站后种植的，建议您先确认文件合法性并处理`</EventDesc>` `<EventTypeDesc>`网站后门-发现后门`(Webshell)`文件`</EventTypeDesc>`

```xml
<RequestId>1</RequestId> <OperateErrorCode>quara.Succes</OperateErrorCode> <EventStatus>32</EventStatus> <EventName>WEBSHELL</EventName> <SaleVersion>无</SaleVersion> <IntranetIp>192.168.XX.XX</IntranetIp> <DataSource>aegis_suspicious_***</DataSource> <InstanceName>worker-k8s-for-cs-cb9******</InstanceName> <CanBeDealOnLine>true</CanBeDealOnLine> <OperateMsg>success</OperateMsg> <Uuid>B41******-3***-4***-B***-9*********</Uuid> <Details>
    <Type>html</Type>
```

`<Value>`描述内容`</Value>`

```xml
    <InfoType>download_url</InfoType>
```

`<Name>`告警描述`</Name>`

```xml
</Details> <InternetIp>47.100.XX.XX</InternetIp> <Level>serious</Level> <Id>1</Id> <LastTime> 2018-10-30 11:43:46 </LastTime> <SasId>无</SasId>
```

`JSON` 格式

```
{
```

`"EventDesc": "`该文件极有可能是黑客成功入侵网站后种植的，建议您先确认文件合法性并处理`",` `"EventTypeDesc": "`网站后门-发现后门`(Webshell)`文件`",`

```json
    "RequestId": 1,
    "OperateErrorCode": "quara.Succes",
    "EventStatus": 32,
    "EventName": "WEBSHELL",
    "SaleVersion": "无",
    "IntranetIp": "192.168.XX.XX",
    "DataSource": "aegis_suspicious_***",
    "InstanceName": "worker-k8s-for-cs-cb9******",
    "CanBeDealOnLine": true,
    "OperateMsg": "success",
    "Uuid": "B41******-3***-4***-B***-9*********",
    "Details": {
        "Type": "html",
```

`"Value": "`描述内容`",`

```json
        "InfoType": "download_url",
```

`"Name": "`告警描述"

```json
    },
    "InternetIp": "47.100.XX.XX",
    "Level": "serious",
    "Id": 1,
    "LastTime": "2018-10-30 11:43:46",
    "SasId": "无"
}
```

### 云产品配置检查

#### DescribeRiskItemType

查看所有云产品配置检测项的类型。每个检测项都对应一个类型。检查项类型包含：身份认证及权限、网络访问控制、日志审计、数据安全、监控告警和基础安全防护。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRiskIte mType | 要执行的操作。 取值：DescribeRiskItemType。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| List | Array of ItemType |  | 云产品配置检查项类型的信息。 |
| Id | Long | 1 | 云产品配置检查项的ID。 |
| Title | String | 身份认证及权限 | 检查类型标题。 |
| RequestId | String | 3B3F3A90-46A5- ***-A2D8- D68B14262F96 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRiskItemType
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>3B3F3A90-46A5-***-A2D8-D68B14262F96</RequestId> <List>
```

`<Title>`身份认证及权限`</Title>`

```xml
    <Id>1</Id>
</List>
```

`JSON` 格式

```json
{
    "RequestId": "3B3F3A90-46A5-***-A2D8-D68B14262F96",
    "List": {
```

`"Title": "`身份认证及权限`",`

```json
        "Id": 1
    }
}
```

#### StartBaselineSecurityCheck

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | StartBaselineSe curityCheck | 要执行的操作。 取值：StartBaselineSecurityCheck。 |
|---|---|---|---|---|
| Type | String | 是 | check | 检查的任务类型。取值包括： check：执行检测。 verify：执行验证。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值包括： zh：中文。 en：英文。 |
| ItemIds.N | RepeatL ist | 否 | 1 | 检查项ID。 说明执行云产品配置检查任务，需要提供检查项的ID，该ID可调用DescribeRiskItemType接口获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-***- 0995757C47E9 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=StartBaselineSecurityCheck &Type=check
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>48D2E9A9-A1B0-4295-***-0995757C47E9</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "48D2E9A9-A1B0-4295-***-0995757C47E9"
}
```

#### DescribeRiskCheckSummary

查看云产品配置检查结果汇总信息，包括检测到的风险项数量、风险率、影响资产数量、上次检测时间以及检测项各个类型的统计数据等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRiskChe ckSummary | 要执行的操作。 取值：DescribeRiskCheckSummary 。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |
| ResourceDirecto ryAccountId | String | 否 | 无 | 已废弃。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 291B49F9-1685- 4005-****- 606B6F78740F | 本次调用请求的ID。 |
| RiskCheckSum mary | Struct |  | 云产品配置检查的结果统计。 |
| AffectedAsset Count | Integer | 0 | 检查结果中风险项影响的资产数量。 |
| DisabledRiskC ount | Integer | 0 | 检查不通过的检查项数量。 |
| EnabledRiskCo unt | Integer | 3 | 检查通过的检查项数量。 |
| Groups | Array of group |  | 检查项类型的统计信息。 |

| CountByStatus | Array of statusCount |  | 检查项结果统计。 |
|---|---|---|---|
| Count | Integer | 2 | 检查到的风险项数量。 |
| Status | String | pass | 完成检查后，检查项的状态。取值： pass：检查通过，表示检查项正常。 failed：检查不通过，表示检查项存在风险。 |
| Id | Long | 1 | 检查项类别ID。 |
| RemainingTim e | Integer | 0 | 预计检查时间。 |
| Sort | Integer | 1 | 检查项类型在控制台全部类型下拉列表中的排列顺序。 |
| Status | String | finish | 检查完成的状态。取值： finish：检查已完成。 running：检查中。 waiting：检查等待中。 notStart：检查未开始。 |
| Title | String | 身份认证及权限 | 检查项类别的名称。 |
| ItemCount | Integer | 4 | 检查项的数量。 |
| PreviousCount | Integer | 0 | 上次检查到的风险项数量。 |
| PreviousTime | Long | 1545012926000 | 上次检查时间。使用时间戳格式，单位：毫秒。 |
| RiskCount | Integer | 1 | 检查到的风险项数量。 |
| RiskLevelCoun t | Array of levelCount |  | 检查项每类危险等级的数量。取值： high：高危。 medium：中危。 low：低危。 |
| Count | Integer | 1 | 数量。 |
| Key | String | medium | 检查项的危险等级。 |

| RiskRate | Float | 0.25 | 检查出的风险项数量在检查项总数中的占比。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckSummary
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>291B49F9-1685-4005-****-606B6F78740F</RequestId> <RiskCheckSummary>
    <DisabledRiskCount>0</DisabledRiskCount>
    <PreviousTime>1545012926000</PreviousTime>
    <RiskRate>0.25</RiskRate>
    <ItemCount>4</ItemCount>
    <PreviousCount>0</PreviousCount>
    <EnabledRiskCount>3</EnabledRiskCount>
    <AffectedAssetCount>0</AffectedAssetCount>
    <RiskCount>1</RiskCount>
    <Groups>
        <Status>finish</Status>
        <RemainingTime>0</RemainingTime>
        <Sort>1</Sort>
```

`<Title>`身份认证及权限`</Title>`

```xml
        <Id>1</Id>
        <CountByStatus>
            <Status>pass</Status>
            <Count>2</Count>
        </CountByStatus>
    </Groups>
    <RiskLevelCount>
        <Count>1</Count>
        <Key>medium</Key>
    </RiskLevelCount>
</RiskCheckSummary>
```

`JSON` 格式

```json
{
    "RequestId": "291B49F9-1685-4005-****-606B6F78740F",
    "RiskCheckSummary": {
        "DisabledRiskCount": 0,
        "PreviousTime": 1545012926000,
        "RiskRate": 0.25,
        "ItemCount": 4,
        "PreviousCount": 0,
        "EnabledRiskCount": 3,
        "AffectedAssetCount": 0,
        "RiskCount": 1,
        "Groups": {
            "Status": "finish",
            "RemainingTime": 0,
            "Sort": 1,
```

`"Title": "`身份认证及权限`",`

```json
            "Id": 1,
            "CountByStatus": {
                "Status": "pass",
                "Count": 2
            }
        },
        "RiskLevelCount": {
            "Count": 1,
            "Key": "medium"
        }
    }
}
```

#### DescribeRiskCheckResult

查询检查项的检测结果，可根据类别或名称进行筛选查询。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRiskChe ckResult | 系统规定参数。取值：DescribeRiskCheckResult。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值： zh：中文。 en：英文。 |
| GroupId | Long | 否 | 21000 | 检测项类别ID。 |

| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
|---|---|---|---|---|
| RiskLevel | String | 否 | high | 检查项风险等级。可选： high：高危。 medium：中危。 low：低危。 |
| Status | String | 否 | pass | 检查结果的状态。取值： pass：通过。 failed：失败。 running：运行中。 waiting：等待运行。 ignored：已忽略。 falsePositive：已标记误报。 |
| ItemIds.N | RepeatL ist | 否 | sde*** | 检查项ID。 |
| AssetType | String | 否 | RDS | 检查的云产品类型。取值： RDS：云数据库RDS。 ECS：云服务器ECS。 OSS：对象存储OSS。 MongoDB：云数据库 MongoDB。 Redis：云数据库 Redis。 |
| Name | String | 否 | 云平台-主账号双因素认证配置检查 | 检查项名称。 |
| PageSize | Integer | 否 | 10 | 每页最多显示的数据条数。 |
| QueryFlag | String | 否 | 无 | 已废弃。 |
| regionId | String | 否 | hangzhou** | 区域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 10 | 总页码数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| List | Array of RiskCheckRes ultForDisplay |  | 检查项信息。 |

| AffectedCount | Integer | 0 | 受影响资产数量。 |
|---|---|---|---|
| CheckTime | Long | 1543991525000 | 最新检测时间。使用时间戳格式，单位：毫秒。 |
| ItemId | Long | 1 | 检查项ID。 |
| RemainingTim e | Integer | 0 | 已废弃。 |
| RepairStatus | String | disabled | 配置检查项是否支持修复功能。 enabled：支持修复。 disabled：不支持修复。 |
| RiskAssertTyp e | String | ECS | 受影响的资产类型。 |
| RiskItemResou rces | Array of RiskItemResou rce |  | 检查项的详情数据。 |
| ContentResour ce | Json | { "type": "link", "value": "未开启多因素认证，存在风险\n", "url": "https://***.aliyun.c om/#/secure\n" } | 详情项的内容。 |
| ResourceNam e | String | bestPractice | 详情项标题。取值： bestPractice：检查描述。 influence：威胁影响。 suggestion：指导方案。 helpResource：帮助资源。 |
| RiskLevel | String | high | 检查项的风险等级。取值： high：高危。 medium：中危。 low：低危。 |
| Sort | Integer | 1 | 检查结果的排序序号。 |
| StartStatus | String | enabled | 检查项启用状态。取值： enabled：用户所用的产品版本支持检测该检查项。 disable：用户所用的产品版本不支持检测该检查项。 |

| Status | String | pass | 检查项检查状态。取值： pass：通过。 failed：失败。 running：运行中。 waiting：等待运行。 ignored：已忽略。 falsePositive：已标记误报。 |
|---|---|---|---|
| TaskId | Long | 7 | 检查任务的ID。 |
| Title | String | 云平台-主账号双因素认证配置检查 | 检查项标题。 |
| Type | String | 身份认证及权限 | 检查项类型。 |
| PageCount | Integer | 20 | 数据的总页数。 |
| PageSize | Integer | 10 | 分页查询时，显示的每页数据的最大条数。 |
| RequestId | String | AD271C07-4ACE- ***-AA9B- F14FD3B7717F | 本次调用请求的ID。 |
| TotalCount | Integer | 12 | 数据的总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckResult
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>12</TotalCount> <PageSize>10</PageSize> <PageCount>20</PageCount> <RequestId>AD271C07-4ACE-***-AA9B-F14FD3B7717F</RequestId> <CurrentPage>1</CurrentPage> <List>
    <RiskAssertType>ECS</RiskAssertType>
    <Status>pass</Status>
    <CheckTime>1543991525000</CheckTime>
    <StartStatus>enabled</StartStatus>
```

`<Type>`身份认证及权限`</Type>`

```xml
    <TaskId>7</TaskId>
    <RemainingTime>0</RemainingTime>
    <AffectedCount>0</AffectedCount>
    <Sort>1</Sort>
```

`<Title>`云平台-主账号双因素认证配置检查`</Title>`

```xml
    <RepairStatus>disabled</RepairStatus>
    <RiskLevel>high</RiskLevel>
    <ItemId>1</ItemId>
    <RiskItemResources>
```

`<ContentResource>{ "type": "link", "value": "`未开启多因素认证，存在风险\n", "u

```xml
rl": "https://***.aliyun.com/#/secure\n" }</ContentResource>
        <ResourceName>bestPractice</ResourceName>
    </RiskItemResources>
</List> <Count>10</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 12,
    "PageSize": 10,
    "PageCount": 20,
    "RequestId": "AD271C07-4ACE-***-AA9B-F14FD3B7717F",
    "CurrentPage": 1,
    "List": {
        "RiskAssertType": "ECS",
        "Status": "pass",
        "CheckTime": 1543991525000,
        "StartStatus": "enabled",
```

`"Type": "`身份认证及权限`",`

```json
        "TaskId": 7,
        "RemainingTime": 0,
        "AffectedCount": 0,
        "Sort": 1,
```

`"Title": "`云平台-主账号双因素认证配置检查`",`

```json
        "RepairStatus": "disabled",
        "RiskLevel": "high",
        "ItemId": 1,
        "RiskItemResources": {
            "ContentResource": "{   \"type\": \"link\",   \"value\": \"未开启多因素认证，存
在风险\\n\", \"url\": \"https://***.aliyun.com/#/secure\\n\" }",
            "ResourceName": "bestPractice"
        }
    },
    "Count": 10
}
```

#### DescribeSecurityCheckScheduleConfig

查看用户自定义设置的检测周期以及时间段。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSecurit yCheckSchedule Config | 系统规定参数。取值：DescribeSecurityCheckSched uleConfig。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-****- 0995757C47E9 | 本次调用请求的ID。 |
| RiskCheckJobC onfig | Struct |  | 周期检测任务的设置信息。 |
| DaysOfWeek | String | 1,2,3 | 检测周期。可取值周一至周日，支持设置多天。 多天之间使用英文逗号隔开。取值： 1：周一。 2：周二。 3：周三。 4：周四。 5：周五。 6：周六。 7：周日。 |
| EndTime | Integer | 12 | 检测结束时间。取值： 6：在00:00-06:00结束检测。 12：在06:00-12:00结束检测。 18：在12:00-18:00结束检测。 24：在18:00-24:00结束检测。 |
| StartTime | Integer | 6 | 检测开始时间。取值： 6：在00:00-06:00结束检测。 12：在06:00-12:00结束检测。 18：在12:00-18:00结束检测。 24：在18:00-24:00结束检测。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSecurityCheckScheduleConfig
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RiskCheckJobConfig>
    <DaysOfWeek>1,2,3</DaysOfWeek>
    <EndTime>12</EndTime>
    <StartTime>6</StartTime>
</RiskCheckJobConfig> <RequestId>48D2E9A9-A1B0-4295-****-0995757C47E9</RequestId>
```

`JSON` 格式

```json
{
    "RiskCheckJobConfig": {
        "DaysOfWeek": "1,2,3",
        "EndTime": 12,
        "StartTime": 6
    },
    "RequestId": "48D2E9A9-A1B0-4295-****-0995757C47E9"
}
```

### 漏洞管理

#### DescribeVulList

调用本接口可以根据漏洞类型查询对应漏洞信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulList | 要执行的操作。 取值：DescribeVulList。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值包括： zh：中文。 en：英文。 |
| Remark | String | 否 | 47.200.XX.XX | 查询标记，可以为资产内网IP、外网IP或资产名称。 |
| GroupId | String | 否 | 9207613 | 要查询的资产分组ID。 |
| Type | String | 否 | cve | 漏洞类型。取值包括： cve：Linux软件漏洞。 sys：Windows系统漏洞。 cms：Web-CMS漏洞。 app：应用漏洞。 emg：应急漏洞。 |
| Uuids | String | 否 | 1587bedb-fdb4- 48c4-9330- ************ | 资产实例的唯一标识ID列表，多个ID用英文逗号分隔。 |
| AliasName | String | 否 | RHSA-2019:***- Important: polkit security update | 漏洞别名。 |

| Level | String | 否 | serious | 漏洞等级，取值范围： serious：表示严重。 high：表示高危。 medium：表示中危。 low：表示低危。 |
|---|---|---|---|---|
| Necessity | String | 否 | asap,later,nntf | 漏洞修复必要性等级。多个等级用英文逗号分隔。取值包括： asap：高。 later：中。 nntf：低。 |
| Dealed | String | 否 | n | 漏洞是否处理。取值包括： y：已处理。 n：未处理。 |
| BatchName | String | 否 | 测试 | 批量名称。 |
| Resource | String | 否 | vulnerability | 批次来源 (**vulnerability**，**host**)。 |
| CreateTsStart | Long | 否 | 1512949391000 | 创建开始时间。使用时间戳格式，单位： 毫秒。 |
| CreateTsEnd | Long | 否 | 1512949392000 | 创建结束时间。使用时间戳格式，单位： 毫秒。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| ModifyTsStart | Long | 否 | 1512949391000 | 修改开始时间。使用时间戳格式，单位： 毫秒。 |
| ModifyTsEnd | Long | 否 | 1512949392000 | 修改结束时间。使用时间戳格式，单位： 毫秒。 |
| AttachTypes | String | 否 | sca | 查询应用漏洞时的附加漏洞类型。查询应用漏洞（即Type设置为app）时需要设置该参数。该参数固定取值为sca。 |
| ContainerFieldN ame | String | 否 | 无 | 已废弃。 |

| ContainerFieldV alue | String | 否 | 无 | 已废弃。 |
|---|---|---|---|---|
| TargetType | String | 否 | groupId | TargetType参数值的类型： groupId：表示资产分组ID。 uuid：表示主机资产UUID。 |
| ClusterId | String | 否 | 测试集群1 | 集群ID。 |
| MinScore | Integer | 否 | 100 | 最小分数。 |
| VpcInstanceIds | String | 否 | vpc-xxx | VPC实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | ECDE6715-6286- 40E6-A32D- 3094051FD74D | 本次调用请求的ID。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 2 | 查询结果总数。 |
| VulRecords | Array of VulRecord |  | 漏洞信息。 |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | 漏洞别名。 |
| ContainerId | String | 无 | 已废弃。 |
| ContainerImag eId | String | 无 | 已废弃。 |
| ContainerImag eName | String | 无 | 已废弃。 |
| ContainerInner Path | String | 无 | 已废弃。 |
| ContainerNam e | String | 无 | 已废弃。 |

| ExtendContent Json | Struct |  | 扩展信息。 |
|---|---|---|---|
| AbsolutePath | String | /roo/www/web | 绝对路径。 |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | 漏洞别名。 |
| Ip | String | 47.200.XX.XX | 漏洞关联资产的IP地址。优先展示公网IP，若公网IP不存在，则显示私网IP。 |
| LastTs | Long | 1554189334000 | 最后发现时间的时间戳，单位为毫秒。 |
| Necessity | Struct |  | 漏洞修复必要性。 |
| Assets factor _ | String | 1 | 资产因子。 |
| Cvss factor _ | String | 7.8 | CVSS因子。 |
| Enviroment fa _ ctor | String | 1.0 | 环境因子。 |
| Is calc _ | String | 1 | 是否计算出分数。 0：未计算。 1：已计算。 |
| Status | String | normal | 漏洞修复建议得分状态。 none：未生成分数 pending：等待计算中 miss：未计算出分数 normal：正常 |
| Time factor _ | String | 1.0 | 时间因子。 |
| Total score _ | String | 7.8 | 漏洞影响的总分。 |
| Os | String | centos | 操作系统。 |
| OsRelease | String | 7 | 操作系统描述。 |
| PrimaryId | Long | 111 | 漏洞ID。 |

| RpmEntityList | Array of RpmEntity |  | RPM包列表。 |
|---|---|---|---|
| FullVersion | String | 3.10.0-693.2.2.el7 | 完整版本号。 |
| MatchDetail | String | python-perf version less than 0:3.10.0- 693.21.1.el7 | 匹配细节。 |
| Name | String | python-perf | RPM名称。 |
| Path | String | /usr/lib64/python2. 7/site-packages | 路径。 |
| UpdateCmd | String | *** update python- perf | 修复命令。 |
| Version | String | 3.10.0 | 版本号。 |
| Status | String | 1 | 漏洞状态。 1：未修复。 2：修复失败。 3：回滚失败。 4：修复中。 5：回滚中。 6：验证中。 7：修复成功。 8：修复成功待重启。 9：回滚成功。 10：已忽略。 11：回滚成功待重启。 12：漏洞不存在。 20：已失效。 |
| Tag | String | oval | 漏洞标签。 |
| cveList | List | ["CVE-2016-8610", "CVE-2017-5335" ] | 漏洞公告列表。 |
| FirstTs | Long | 1554189334000 | 首次发现时间的时间戳，单位为毫秒。 |
| GroupId | Integer | 281801 | 资产分组ID。 |
| InstanceId | String | i-bp18t*** | 资产实例ID。 |

| InstanceName | String | 测试ECS | 资产实例名称。 |
|---|---|---|---|
| InternetIp | String | 47.200.XX.XX | 资产外网IP。 |
| IntranetIp | String | 192.168.XX.XX | 资产内网IP。 |
| K8sClusterId | String | 无 | 已废弃。 |
| K8sNamespac e | String | 无 | 已废弃。 |
| K8sNodeId | String | 无 | 已废弃。 |
| K8sNodeName | String | 无 | 已废弃。 |
| K8sPodName | String | 无 | 已废弃。 |
| LastTs | Long | 1541207563000 | 最后发现时间的时间戳，单位为毫秒。 |
| ModifyTs | Long | 1541207563000 | 修改时间的时间戳，单位为毫秒。 |
| Name | String | oval:com.redhat.rh sa:def:20170574 | 漏洞名称。 |
| Necessity | String | asap | 漏洞修复必要性等级。取值包括： asap：高。 later：中。 nntf：低。 |
| Online | Boolean | true | 资产实例是否在线。取值包括： true：在线。 false：离线。 |
| OsVersion | String | linux | 操作系统版本。 |
| PrimaryId | Long | 101162078 | 漏洞ID。 |
| Related | String | CVE-2017- 7518,CVE-2017- 12188 | 漏洞关联CVE列表，多个用英文逗号分隔。 |
| RepairTs | Long | 1541207563000 | 修复时间的时间戳，单位为毫秒。 |

| ResultCode | String | 0 | 修复返回码。 |
|---|---|---|---|
| ResultMessage | String | timeout | 修复返回消息。 |
| Status | Integer | 1 | 漏洞状态。取值包括： 1：未修复。 2：修复失败。 3：回滚失败。 4：修复中。 5：回滚中。 6：验证中。 7：修复成功。 8：修复成功待重启。 9：回滚成功。 10：已忽略。 11：回滚成功待重启。 12：漏洞不存在。 20：已失效。 |
| Tag | String | oval | 漏洞标签。 |
| Type | String | cve | 漏洞类型。取值包括： cve：Linux漏洞。 sys：Windows漏洞。 cms：WebCMS漏洞。 emg：应急漏洞。 app：应用漏洞。 |
| Uuid | String | 04c56617-23fc- 43a5-ab9b- ************ | 资产实例的唯一标识ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>2</TotalCount> <PageSize>20</PageSize> <RequestId>ECDE6715-6286-40E6-A32D-3094051FD74D</RequestId> <VulRecords>
    <K8sNodeId>无</K8sNodeId>
    <K8sNodeName>无</K8sNodeName>
```

```xml
    <OsVersion>linux</OsVersion>
    <ContainerInnerPath>无</ContainerInnerPath>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>无</K8sClusterId>
    <Name>oval:com.redhat.rhsa:def:20170574</Name>
    <K8sNamespace>无</K8sNamespace>
    <RepairTs>1541207563000</RepairTs>
    <ModifyTs>1541207563000</ModifyTs>
    <InternetIp>47.200.XX.XX</InternetIp>
    <ContainerId>无</ContainerId>
    <ContainerName>无</ContainerName>
    <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement
update</AliasName>
    <Status>1</Status>
    <InstanceId>i-bp18t***</InstanceId>
    <Necessity>asap</Necessity>
    <LastTs>1541207563000</LastTs>
    <K8sPodName>无</K8sPodName>
    <ResultMessage>timeout</ResultMessage>
    <ContainerImageId>无</ContainerImageId>
    <GroupId>281801</GroupId>
    <InstanceName>测试ECS</InstanceName>
    <FirstTs>1554189334000</FirstTs>
    <Type>cve</Type>
    <Related>CVE-2017-7518,CVE-2017-12188</Related>
    <Uuid>04c56617-23fc-43a5-ab9b-************</Uuid>
    <ContainerImageName>无</ContainerImageName>
    <Tag>oval</Tag>
    <Online>true</Online>
    <ResultCode>0</ResultCode>
    <PrimaryId>101162078</PrimaryId>
    <ExtendContentJson>
        <Status>1</Status>
        <Os>centos</Os>
        <Ip>47.200.XX.XX</Ip>
        <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement
update</AliasName>
        <LastTs>1554189334000</LastTs>
        <Tag>oval</Tag>
        <AbsolutePath>/roo/www/web</AbsolutePath>
        <OsRelease>7</OsRelease>
        <PrimaryId>111</PrimaryId>
        <RpmEntityList>
            <Path>/usr/lib64/python2.7/site-packages</Path>
            <UpdateCmd>*** update python-perf</UpdateCmd>
            <Version>3.10.0</Version>
            <FullVersion>3.10.0-693.2.2.el7</FullVersion>
            <MatchDetail>python-perf version less than 0:3.10.0-
693.21.1.el7</MatchDetail>
            <Name>python-perf</Name>
        </RpmEntityList>
        <cveList>["CVE-2016-8610", "CVE-2017-5335" ]</cveList>
        <Necessity>
            <Total_score>7.8</Total_score>
<Stt
```

>

```
l</Stt
```

>

```xml
            <Status>normal</Status>
            <Time_factor>1.0</Time_factor>
            <Cvss_factor>7.8</Cvss_factor>
            <Is_calc>1</Is_calc>
            <Enviroment_factor>1.0</Enviroment_factor>
            <Assets_factor>1</Assets_factor>
        </Necessity>
    </ExtendContentJson>
</VulRecords> <CurrentPage>1</CurrentPage>
```

`JSON` 格式

```json
{
    "TotalCount": 2,
    "PageSize": 20,
    "RequestId": "ECDE6715-6286-40E6-A32D-3094051FD74D",
    "VulRecords": {
        "K8sNodeId": "无",
        "K8sNodeName": "无",
        "OsVersion": "linux",
        "ContainerInnerPath": "无",
        "IntranetIp": "192.168.XX.XX",
        "K8sClusterId": "无",
        "Name": "oval:com.redhat.rhsa:def:20170574",
        "K8sNamespace": "无",
        "RepairTs": 1541207563000,
        "ModifyTs": 1541207563000,
        "InternetIp": "47.200.XX.XX",
        "ContainerId": "无",
        "ContainerName": "无",
        "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement update"
```

,

```json
        "Status": 1,
        "InstanceId": "i-bp18t***",
        "Necessity": "asap",
        "LastTs": 1541207563000,
        "K8sPodName": "无",
        "ResultMessage": "timeout",
        "ContainerImageId": "无",
        "GroupId": 281801,
        "InstanceName": "测试ECS",
        "FirstTs": 1554189334000,
        "Type": "cve",
        "Related": "CVE-2017-7518,CVE-2017-12188",
        "Uuid": "04c56617-23fc-43a5-ab9b-************",
        "ContainerImageName": "无",
        "Tag": "oval",
        "Online": true,
        "ResultCode": 0,
        "PrimaryId": 101162078,
        "ExtendContentJson": {
            "Status": 1,
            "Os": "centos",
```

```json
            "Ip": "47.200.XX.XX",
            "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement upd
ate",
            "LastTs": 1554189334000,
            "Tag": "oval",
            "AbsolutePath": "/roo/www/web",
            "OsRelease": 7,
            "PrimaryId": 111,
            "RpmEntityList": {
                "Path": "/usr/lib64/python2.7/site-packages",
                "UpdateCmd": "*** update python-perf",
                "Version": "3.10.0",
                "FullVersion": "3.10.0-693.2.2.el7",
                "MatchDetail": "python-perf version less than 0:3.10.0-693.21.1.el7",
                "Name": "python-perf"
            },
            "cveList": "[\"CVE-2016-8610\", \"CVE-2017-5335\" ]",
            "Necessity": {
                "Total_score": 7.8,
                "Status": "normal",
                "Time_factor": 1,
                "Cvss_factor": 7.8,
                "Is_calc": 1,
                "Enviroment_factor": 1,
                "Assets_factor": 1
            }
        }
    },
    "CurrentPage": 1
}
```

#### DescribeVulWhitelist

分页查询漏洞白名单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeVulWhit elist | 需要执行的操作。 取值：DescribeVulWhitelist。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 10 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| CurrentPage | Integer | 1 | 当前页的页码。 |
|---|---|---|---|
| PageSize | Integer | 10 | 每页最多显示的数据条数。 |
| RequestId | String | 74F97EF7-B543- 43FD-XXXX- 18456731F9C5 | 本次调用请求的ID。 |
| TotalCount | Integer | 1 | 总数据条数。 |
| VulWhitelists | Array of VulWhitelist |  | 漏洞白名单信息。 |
| AliasName | String | RHSA-xxxx | 漏洞别名。 |
| Name | String | oval:com.redh.xxx xx | 漏洞名称。 |
| Reason | String | 暂不修复 | 加白原因。 |
| Type | String | cve | 漏洞类型。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVulWhitelist
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>74F97EF7-B543-43FD-XXXX-18456731F9C5</RequestId> <VulWhitelists>
    <Type>cve</Type>
    <AliasName>RHSA-xxxx</AliasName>
```

`<Reason>`暂不修复`</Reason>`

```xml
    <Name>oval:com.redh.xxxxx</Name>
</VulWhitelists> <CurrentPage>1</CurrentPage>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "74F97EF7-B543-43FD-XXXX-18456731F9C5",
    "VulWhitelists": {
        "Type": "cve",
        "AliasName": "RHSA-xxxx",
```

`"Reason": "`暂不修复`",`

```json
        "Name": "oval:com.redh.xxxxx"
    },
    "CurrentPage": 1
}
```

#### DescribeConcernNecessity

查询关注的漏洞修复必要性信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeConcer nNecessity | 系统规定参数。取值：DescribeConcernNecessity。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值： zh：中文。 en：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConcernNeces sity | List | [ "asap", "later", "nntf"] | 漏洞修复必要性列表。取值： asap：高。 later：中。 nntf：低。 |
| RequestId | String | 9139DAF6-5CE0- 49A0-XXXX- 07243A290F70 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeConcernNecessity
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>9139DAF6-5CE0-49A0-XXXX-07243A290F70</RequestId> <ConcernNecessity>[ "asap", "later", "nntf"]</ConcernNecessity>
```

`JSON` 格式

```json
{
    "RequestId": "9139DAF6-5CE0-49A0-XXXX-07243A290F70",
    "ConcernNecessity": "[ \"asap\", \"later\", \"nntf\"]"
}
```

#### DescribeGroupedVul

分组查询漏洞信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeGroupe dVul | 系统规定参数。取值：DescribeGroupedVul。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |
| Type | String | 否 | cve | 漏洞类型。包括以下几类： cve：Linux漏洞。 sys：Windows漏洞。 cms：WebCMS漏洞。 app：应用漏洞。 emg：应急漏洞。 |
| Uuids | String | 否 | d42f938c-d962- 48a0-90f9- 05e4ea****** | 资产实例唯一标识ID列表，多个用英文逗号分隔。 |
| AliasName | String | 否 | RHSA-2019:***- Important: polkit security update | 漏洞别名。 |
| Necessity | String | 否 | asap,later,nntf | 漏洞修复必要性等级。多个等级用英文逗号分隔。可取值： asap：高。 later：中。 nntf：低。 |

| Dealed | String | 否 | n | 漏洞是否处理。取值： y：已处理。 n：未处理。 |
|---|---|---|---|---|
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 20 | 每页最多显示的数据条数。 |
| GroupId | String | 否 | weds**** | 资产分组ID。 |
| ContainerFieldN ame | String | 否 | XXX | 容器字段名称。 |
| ContainerFieldV alue | String | 否 | XXX | 容器字段值。 |
| TargetType | String | 否 | groupId | Target参数值的类型： groupId：表示资产分组ID。 uuid：表示主机资产UUID。 |
| ClusterId | String | 否 | 测试1 | 集群ID。 |
| MinScore | Integer | 否 | 100 | 最小分数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| RequestId | String | 0DFCADBA-7065- 42DA-XXXX- 6868B9C2A8CF | 本次调用请求的ID。 |
| TotalCount | Integer | 2 | 总数据条数。 |
| GroupedVulIte ms | Array of GroupedVulIte m |  | 分组漏洞信息。 |
| AliasName | String | RHSA-2019:***- Important: polkit security update | 漏洞别名。 |

| AsapCount | Integer | 0 | 修复必要性等级高的漏洞数量。 |
|---|---|---|---|
| GmtLast | Long | 1554185744000 | 漏洞最后发现时间。使用时间戳格式，单位：毫秒。 |
| HandledCount | Integer | 0 | 已处理漏洞数量。 |
| LaterCount | Integer | 0 | 修复必要性等级中等的漏洞数量。 |
| Name | String | ***glibc 安全和BUG 修复更新 | 漏洞名称。 |
| NntfCount | Integer | 59 | 修复必要性等级低的漏洞数量。 |
| Tags | String | 需要重启 | 漏洞标签。 |
| TotalFixCount | Long | 0 | 已修复漏洞的总数量。 |
| Type | String | cve | 漏洞类型。包括以下几类： cve：Linux漏洞。 sys：Windows漏洞。 cms：WebCMS漏洞。 app：应用漏洞。 emg：应急漏洞。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGroupedVul
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>2</TotalCount> <PageSize>20</PageSize> <RequestId>0DFCADBA-7065-42DA-XXXX-6868B9C2A8CF</RequestId> <CurrentPage>1</CurrentPage> <GroupedVulItems>
    <Type>cve</Type>
    <LaterCount>0</LaterCount>
    <GmtLast>1554185744000</GmtLast>
    <HandledCount>0</HandledCount>
    <AliasName>RHSA-2019:***-Important: polkit security update</AliasName>
    <AsapCount>0</AsapCount>
    <TotalFixCount>0</TotalFixCount>
    <NntfCount>59</NntfCount>
```

`<Tags>`需要重启`</Tags>` `<Name>***glibc` 安全和`BUG`修复更新`</Name>`

```
</GroupedVulItems>
```

`JSON` 格式

```json
{
    "TotalCount": 2,
    "PageSize": 20,
    "RequestId": "0DFCADBA-7065-42DA-XXXX-6868B9C2A8CF",
    "CurrentPage": 1,
    "GroupedVulItems": {
        "Type": "cve",
        "LaterCount": 0,
        "GmtLast": 1554185744000,
        "HandledCount": 0,
        "AliasName": "RHSA-2019:***-Important: polkit security update",
        "AsapCount": 0,
        "TotalFixCount": 0,
        "NntfCount": 59,
```

`"Tags": "`需要重启`",` `"Name": "***glibc` 安全和`BUG`修复更新"

```
    }
}
```

#### DescribeAutoDelConfig

获取漏洞管理设置中失效漏洞自动删除天数配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAutoDel Config | 要执行的操作。 取值：DescribeAutoDelConfig。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Days | Integer | 7 | 在自动删除漏洞前系统保存漏洞的天数。单位： 天。 |
| RequestId | String | 43186B14-5A39- 44E0-XXXX- 8B24D1EF82CC | 本次调用请求的ID。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

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

### 基线

#### DescribeCheckWarningSummary

查看基线检查的结果统计情况，例如基线检查的服务器数量、基线检查项数量、最近检查通过率等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCheckW arningSummary | 取值：DescribeCheckWarningSumm ary。 |
| SourceIp | String | 否 | 1.2.XX.XX | 访问源的IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文 en：英文 |

| TypeName | String | 否 | database | 基线检查项一级类型。 |
|---|---|---|---|---|
| Status | String | 否 | 1 | 基线检查项状态。 1：未通过 2：验证中 3：已通过 5：已失效 6：已忽略 |
| RiskStatus | Integer | 否 | 1 | 基线检查项的状态。 1：未通过 3：已通过 |
| RiskName | String | 否 | Redis安全基线检查 | 基线检查风险项名称。 |
| StrategyId | Long | 否 | 1 | 基线检查策略ID。 |
| Uuids | String | 否 | f03259d8-1e81- 4fae-bcbb- 275fb5****** | 执行基线检查策略的服务器ID。 |
| PageSize | Integer | 否 | 10 | 分页查询时，显示的每页数据的最大条数。 |
| CurrentPage | Integer | 否 | 1 | 分页查询时，显示的当前页的页码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 10 | 分页查询时，显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 分页查询时，显示的当前页的页码。 |
| PageSize | Integer | 10 | 分页查询时，显示的每页数据的最大条数。 |
| RequestId | String | 00BD7CE2-284A- 4534-BD09-*** | 本次调用请求的ID。 |
| TotalCount | Integer | 100 | 基线检查项的总数。 |
| WarningSumm arys | Array of WarningSumm ary |  | 检查项统计明细。 |

| CheckCount | Integer | 10 | 基线检查项个数。 |
|---|---|---|---|
| HighWarningC ount | Integer | 1 | 高危检查项个数。 |
| LastFoundTim e | String | 2019-01-01 12:23:00 | 最近执行基线检查的时间。 |
| Level | String | high | 基线检查风险项的危险等级。包含以下等级： high：高危 medium：中危 low：低危 |
| LowWarningCo unt | Integer | 3 | 低危检查项的个数。 |
| MediumWarni ngCount | Integer | 2 | 中危检查项的个数。 |
| RiskId | Long | 1 | 风险项ID。 |
| RiskName | String | Redis密码检查 | 基线检查风险项名称。 |
| SubTypeAlias | String | Redis检查 | 风险项二级分类。 |
| TypeAlias | String | 数据库 | 基线检查项的分类，例如：数据库、系统、弱密码检测和中间件。 |
| WarningMachi neCount | Integer | 11 | 检测出基线风险项的资产的数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningSummary &Lang=zh &TypeName=database &Status=1 &RiskStatus=1
```

`&RiskName=Redis`安全基线检查

```
&StrategyId=1 &Uuids=f03259d8-1e81-4fae-bcbb-275fb5****** &CurrentPage=1 &PageSize=20
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <TotalCount>25</TotalCount>
   <PageSize>20</PageSize>
   <RequestId>DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD</RequestId>
   <CurrentPage>1</CurrentPage>
   <Count>20</Count>
   <WarningSummarys>
      <RiskId>43</RiskId>
      <LastFoundTime>2019-04-10 00:33:00</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>3</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>8</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>系统</TypeAlias>
      <SubTypeAlias>
```

`CentOS Linux 7`安全基线检查

```xml
                              </SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>
```

`CentOS Linux 7`安全基线检查

```xml
                              </RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>47</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>7</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>系统</TypeAlias>
```

`<SubTypeAlias>CentOS Linux 7`合规基线检查-等保三级`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>CentOS Linux 7`合规基线检查-等保三级`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>48</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>6</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>系统</TypeAlias>
```

`<SubTypeAlias>CentOS Linux 7`合规基线检查-等保二级`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>CentOS Linux 7`合规基线检查-等保二级`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
RikId3/RikId
```

```xml
      <RiskId>3</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>数据库</TypeAlias>
      <SubTypeAlias>Redis安全基线检查</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>Redis`安全基线检查`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>19</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
```

`<TypeAlias>`弱密码检测`</TypeAlias>` `<SubTypeAlias>Linux`系统登录弱口令检测`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>Linux`系统登录弱口令检测`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>12</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
```

`<TypeAlias>`弱密码检测`</TypeAlias>` `<SubTypeAlias>FTP`匿名登录配置检测`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>FTP`匿名登录配置检测`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>13</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
```

`<TypeAlias>`弱密码检测`</TypeAlias>` `<SubTypeAlias>Windows`系统登录弱口令检测`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>Windows`系统登录弱口令检测`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>23</RiskId>
      <LastFoundTime>2019-04-10 14:00:17</LastFoundTime>
<MediumWarningCount>0</MediumWarningCount>
```

```xml
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>8</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>中间件</TypeAlias>
      <SubTypeAlias>Apache Tomcat 安全基线检查</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Apache Tomcat 安全基线检查</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>2</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
```

`<TypeAlias>`弱密码检测`</TypeAlias>`

```xml
      <SubTypeAlias>PostgreSQL弱密码检测</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>PostgreSql`登录弱口令检测`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>11</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
```

`<TypeAlias>`弱密码检测`</TypeAlias>`

```xml
      <SubTypeAlias>MySQL弱密码检测</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>MySQL`弱密码检测`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>20</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
```

`<TypeAlias>`弱密码检测`</TypeAlias>` `<SubTypeAlias>FTP`登录弱口令检测`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>FTP`登录弱口令检测`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>17</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
<CheckCount>1</CheckCount>
```

```xml
      CheckCount1/CheckCount
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
```

`<TypeAlias>`弱密码检测`</TypeAlias>`

```xml
      <SubTypeAlias>Microsoft SQL Server弱密码检测</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Microsoft SQL Server登录弱口令检测</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>24</RiskId>
      <LastFoundTime>2019-04-10 06:52:05</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>2</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>数据库</TypeAlias>
      <SubTypeAlias>Memcached安全基线检查</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>Memcached`安全基线检查`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>42</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>系统</TypeAlias>
      <SubTypeAlias>CentOS Linux 6安全基线检查</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6安全基线检查</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>49</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>系统</TypeAlias>
```

`<SubTypeAlias>CentOS Linux 6`合规基线检查-等保二级`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>CentOS Linux 6`合规基线检查-等保二级`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>50</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
```

```xml
      <TypeAlias>系统</TypeAlias>
```

`<SubTypeAlias>CentOS Linux 6`合规基线检查-等保三级`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>CentOS Linux 6`合规基线检查-等保三级`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>55</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>14</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>系统</TypeAlias>
```

`<SubTypeAlias>Linux Ubuntu`合规基线检查-等保二级`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>Linux Ubuntu`合规基线检查-等保二级`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>56</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>系统</TypeAlias>
```

`<SubTypeAlias>Linux Ubuntu`合规基线检查-等保三级`</SubTypeAlias>`

```xml
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>Linux Ubuntu`合规基线检查-等保三级`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>54</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>系统</TypeAlias>
      <SubTypeAlias>Linux Ubuntu 安全基线检查</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
```

`<RiskName>Linux Ubuntu` 安全基线检查`</RiskName>`

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>51</RiskId>
      <LastFoundTime>2019-02-19 12:44:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>系统</TypeAlias>
      <SubTypeAlias>Windows 2012 R2安全基线检查</SubTypeAlias>
```

```xml
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows 2012 R2安全基线检查</RiskName>
   </WarningSummarys>
```

`JSON` 格式

```json
{
 "TotalCount":25,
 "PageSize":20,
 "RequestId":"DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD",
 "CurrentPage":1,
 "Count":20,
 "WarningSummarys":[
  {
   "RiskId":43,
   "LastFoundTime":"2019-04-10 00:33:00",
   "MediumWarningCount":0,
   "WarningMachineCount":3,
   "CheckCount":16,
   "HighWarningCount":8,
   "Level":"high",
   "TypeAlias":"系统",
   "SubTypeAlias":"CentOS Linux 7安全基线检查\n                                \n
```

`",`

```json
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 7安全基线检查\n                                \n
```

"

```json
  },
  {
   "RiskId":47,
   "LastFoundTime":"2019-04-10 00:58:11",
   "MediumWarningCount":0,
   "WarningMachineCount":2,
   "CheckCount":15,
   "HighWarningCount":7,
   "Level":"medium",
   "TypeAlias":"系统",
```

`"SubTypeAlias":"CentOS Linux 7`合规基线检查-等保三级`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"CentOS Linux 7`合规基线检查-等保三级"

```json
  },
  {
   "RiskId":48,
   "LastFoundTime":"2019-04-10 00:58:11",
   "MediumWarningCount":0,
   "WarningMachineCount":2,
   "CheckCount":12,
   "HighWarningCount":6,
   "Level":"medium",
   "TypeAlias":"系统",
```

`"SubTypeAlias":"CentOS Linux 7`合规基线检查-等保二级`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"CentOS Linux 7`合规基线检查-等保二级"

```json
  },
  {
   "RiskId":3,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
```

`"TypeAlias":"`数据库`",` `"SubTypeAlias":"Redis`安全基线检查`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Redis`安全基线检查"

```json
  },
  {
   "RiskId":19,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
```

`"TypeAlias":"`弱密码检测`",` `"SubTypeAlias":"Linux`系统登录弱口令检测`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Linux`系统登录弱口令检测"

```json
  },
  {
   "RiskId":12,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
```

`"TypeAlias":"`弱密码检测`",` `"SubTypeAlias":"FTP`匿名登录配置检测`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"FTP`匿名登录配置检测"

```json
  },
  {
   "RiskId":13,
   "LastFoundTime":"2019-04-10 06:58:58",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
```

`"TypeAlias":"`弱密码检测`",` `"SubTypeAlias":"Windows`系统登录弱口令检测`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Windows`系统登录弱口令检测"

```
  },
  {
```

```json
   "RiskId":23,
   "LastFoundTime":"2019-04-10 14:00:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":8,
   "HighWarningCount":0,
   "Level":"medium",
```

`"TypeAlias":"`中间件`",` `"SubTypeAlias":"Apache Tomcat` 安全基线检查`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Apache Tomcat` 安全基线检查"

```json
  },
  {
   "RiskId":2,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
```

`"TypeAlias":"`弱密码检测`",` `"SubTypeAlias":"PostgreSQL`弱密码检测`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"PostgreSql`登录弱口令检测"

```json
  },
  {
   "RiskId":11,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
```

`"TypeAlias":"`弱密码检测`",` `"SubTypeAlias":"MySQL`弱密码检测`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"MySQL`弱密码检测"

```json
  },
  {
   "RiskId":20,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
```

`"TypeAlias":"`弱密码检测`",` `"SubTypeAlias":"FTP`登录弱口令检测`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"FTP`登录弱口令检测"

```json
  },
  {
   "RiskId":17,
   "LastFoundTime":"2019-04-10 06:58:58",
```

```json
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
```

`"TypeAlias":"`弱密码检测`",`

```json
   "SubTypeAlias":"Microsoft SQL Server弱密码检测",
   "LowWarningCount":0,
```

`"RiskName":"Microsoft SQL Server`登录弱口令检测"

```json
  },
  {
   "RiskId":24,
   "LastFoundTime":"2019-04-10 06:52:05",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":2,
   "HighWarningCount":0,
   "Level":"medium",
```

`"TypeAlias":"`数据库`",` `"SubTypeAlias":"Memcached`安全基线检查`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Memcached`安全基线检查"

```json
  },
  {
   "RiskId":42,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":16,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"系统",
```

`"SubTypeAlias":"CentOS Linux 6`安全基线检查`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"CentOS Linux 6`安全基线检查"

```json
  },
  {
   "RiskId":49,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":12,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"系统",
```

`"SubTypeAlias":"CentOS Linux 6`合规基线检查-等保二级`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"CentOS Linux 6`合规基线检查-等保二级"

```json
  },
  {
   "RiskId":50,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
"Ch
```

`kC`

```
t"15
```

```json
   "CheckCount":15,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"系统",
```

`"SubTypeAlias":"CentOS Linux 6`合规基线检查-等保三级`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"CentOS Linux 6`合规基线检查-等保三级"

```json
  },
  {
   "RiskId":55,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":14,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"系统",
```

`"SubTypeAlias":"Linux Ubuntu`合规基线检查-等保二级`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Linux Ubuntu`合规基线检查-等保二级"

```json
  },
  {
   "RiskId":56,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":15,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"系统",
```

`"SubTypeAlias":"Linux Ubuntu`合规基线检查-等保三级`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Linux Ubuntu`合规基线检查-等保三级"

```json
  },
  {
   "RiskId":54,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":16,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"系统",
```

`"SubTypeAlias":"Linux Ubuntu` 安全基线检查`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Linux Ubuntu` 安全基线检查"

```json
  },
  {
   "RiskId":51,
   "LastFoundTime":"2019-02-19 12:44:58",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":12,
   "HighWarningCount":0,
"Level":"high"
```

```json
   Level:high,
   "TypeAlias":"系统",
```

`"SubTypeAlias":"Windows 2012 R2`安全基线检查`",`

```json
   "LowWarningCount":0,
```

`"RiskName":"Windows 2012 R2`安全基线检查"

```
  }
```

]

```
}
```

#### DescribeStratety

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeStratety | 系统规定参数。 取值：DescribeStratety。 |
| SourceIp | String | 否 | 1.2.x.x | 访问源IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |
| StrategyIds | String | 否 | test1,test2,test3 | 基线检查策略ID，多个用逗号分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 16B9826C-B99F- 4F8A-8048- EA81D6D3DE8B | 结果的请求ID。 |
| Strategies | Array of Strategy |  | 基线检查策略信息。 |
| ConfigTargets | Array of ConfigTarget |  | 基线检查策略关联分组信息。 |
| Flag | String | add | 关联标识。 |
| Target | String | 1xxx | 关联分组ID。 |
| TargetType | String | groupId | 关联类型。 |

| CycleDays | Integer | 1 | 基线检查周期。 1：每隔1天。 3：每隔3天。 7：每隔7天。 30：每隔30天。 |
|---|---|---|---|
| CycleStartTim e | Integer | 6 | 基线检查开始时间，可在0:00、06:00、 12:00、18:00四个时间点开始执行基线检查。 |
| EcsCount | Integer | 5 | 该基线检查策略中执行基线检测的服务器数量。 |
| ExecStatus | Integer | 1 | 执行状态。 1：未执行 。 2：执行中。 |
| Id | Integer | 1 | 策略ID。 |
| Name | String | 测试 | 策略名称。 |
| PassRate | Integer | 80 | 上一次检测通过率。 |
| ProcessRate | Integer | 80 | 基线检查进度。 |
| RiskCount | Integer | 5 | 选择的基线检查项数量。 |
| Type | Integer | 1 | 基线检查策略的类型。 1：默认策略 。 2：用户自定义的策略。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>16B9826C-B99F-4F8A-8048-EA81D6D3DE8B</RequestId> <Strategies>
    <CycleStartTime>6</CycleStartTime>
    <EcsCount>5</EcsCount>
    <PassRate>80</PassRate>
    <ExecStatus>1</ExecStatus>
    <Type>1</Type>
    <ProcessRate>80</ProcessRate>
    <CycleDays>1</CycleDays>
    <Id>1</Id>
    <RiskCount>5</RiskCount>
    <Name>测试</Name>
    <ConfigTargets>
        <Target>1xxx</Target>
        <TargetType>groupId</TargetType>
        <Flag>add</Flag>
    </ConfigTargets>
</Strategies>
```

`JSON` 格式

```json
{
    "RequestId": "16B9826C-B99F-4F8A-8048-EA81D6D3DE8B",
    "Strategies": {
        "CycleStartTime": 6,
        "EcsCount": 5,
        "PassRate": 80,
        "ExecStatus": 1,
        "Type": 1,
        "ProcessRate": 80,
        "CycleDays": 1,
        "Id": 1,
        "RiskCount": 5,
```

`"Name": "`测试`",`

```json
        "ConfigTargets": {
            "Target": "1xxx",
            "TargetType": "groupId",
            "Flag": "add"
        }
    }
}
```

#### DescribeStrategyExecDetail

查询单个基线检测策略执行最近一次检查的结果详情，包括最近一次执行检查的时间、检测出的风险项数量及基线配置风险详情等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribeStrateg yExecDetail | 取值：DescribeStrategyExecDetail。 |
|---|---|---|---|---|
| StrategyId | Integer | 是 | 1 | 基线检测策略ID。 说明查询单个基线检测策略的检测结果，需要提供该基线策略的 ID。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源IP地址。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| EndTime | String | 2019-01-08 20:11:20 | 基线检查执行结束时间。使用yyyy-MM-dd HH:mm:ss格式。 |
| FailCount | Integer | 94 | 基线检查未通过的风险项数量。 |
| FailedEcsList | Array of FailedEcs |  | 检测出基线风险项的服务器列表。 |
| IP | String | 192.168.XX.XX | 执行基线检查的服务器实例IP地址。 |
| InstanceName | String | 测试-20180703 | 实例名。 |
| IntranetIp | String | 192.168.XX.XX | 内网IP。 |
| Reason | String | Detect timeout | 基线检查未通过的原因。 |
| InProcessCoun t | Integer | 0 | 状态为执行中的基线检查任务的个数。 |
| Percent | String | 100% | 执行进度。 |
| RequestId | String | 09322632-4668- 4AD9-****- 32757DEFBBA6 | 本次调用请求的ID。 |
| Source | String | Manual | 基线检查执行类型。取值： Schedule：周期性自动检查。 Manual：即时手动检查。 |

| StartTime | String | 2019-01-08 19:41:12 | 基线检查执行开始时间。使用yyyy-MM-dd HH:mm:ss格式。 |
|---|---|---|---|
| SuccessCount | Integer | 81 | 基线检查状态为已通过的风险项数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeStrategyExecDetail &StrategyId=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<EndTime>2019-01-08 20:11:20</EndTime> <RequestId>09322632-4668-4AD9-BD0D-32757DEFBBA6</RequestId> <Percent>100%</Percent> <FailCount>94</FailCount> <StartTime>2019-01-08 19:41:12</StartTime> <SuccessCount>81</SuccessCount> <Source>Manual</Source> <FailedEcsList>
    <InstanceName>测试-20180703</InstanceName>
    <IP>192.168.XX.XX</IP>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <Reason>Detect timeout</Reason>
</FailedEcsList> <InProcessCount>0</InProcessCount>
```

`JSON` 格式

```json
{
    "EndTime": "2019-01-08 20:11:20",
    "RequestId": "09322632-4668-4AD9-BD0D-32757DEFBBA6",
    "Percent": "100%",
    "FailCount": 94,
    "StartTime": "2019-01-08 19:41:12",
    "SuccessCount": 81,
    "Source": "Manual",
    "FailedEcsList": {
        "InstanceName": "测试-20180703",
        "IP": "192.168.XX.XX",
        "IntranetIp": "192.168.XX.XX",
        "Reason": "Detect timeout"
    },
    "InProcessCount": 0
}
```

#### DescribeCheckWarnings

调用DescribeCheckWarnings接口查询指定风险项和指定服务器下的检查项信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCheckW arnings | 取值：DescribeCheckWarnings。 |
| RiskId | Long | 是 | 1 | 风险项ID。 说明查询指定风险项和指定服务器下的检查项信息，需要提供风险项ID。 |
| Uuid | String | 是 | d42f938c-d962- 48a0-90f9- 05********** | 执行基线检查的服务器的ID。 风险项ID。 说明查询指定风险项和指定服务器下的检查项信息，需要提供执行基线检查的服务器的ID。 |
| SourceIp | String | 否 | 192.168.XX.XX | 访问源IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |
| PageSize | Integer | 否 | 20 | 分页查询时，每页显示数据最大条数。 默认值为20，代表系统默认每页显示20条数据。 |
| CurrentPage | Integer | 否 | 1 | 分页查询时，当前分页的页码。 起始值为1，表示第1个分页。默认值为 1，表示默认展示第1个分页。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CheckWarning s | Array of CheckWarning |  | 检查项信息。 |
| CheckId | Long | 1 | 检查项ID。 |

| CheckWarning Id | Long | 10 | 告警数据ID。 |
|---|---|---|---|
| Item | String | 密码到期警告 | 检查项名称。 |
| Level | String | high | 基线检查风险项的危险等级。包含以下等级： high：高。 medium：中危。 low：低危。 |
| Status | Integer | 1 | 检查项状态。 1：基线检查未通过。 2：基线修复验证中。 3：基线检查已通过。 5：基线检查状态已失效。 6：基线检查项已忽略。 |
| Type | String | 身份鉴别 | 检查项类型。 |
| Uuid | String | d42f938c-d962- 48a0-90f9- *********** | 执行基线检查的服务器的ID。 |
| Count | Integer | 10 | 当前页显示数据条数。 |
| CurrentPage | Integer | 1 | 当前分页的页码。 |
| PageSize | Integer | 20 | 每页显示数据条数。 |
| RequestId | String | 0DFCADBA-7065- 42DA-AF17- 6868B9C2A8CF | 结果的请求ID。 |
| TotalCount | Integer | 100 | 数据的总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCheckWarnings &RiskId=1 &Uuid=d42f938c-d962-48a0-90f9-05**********
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>100</TotalCount> <CheckWarnings>
    <Status>1</Status>
```

`<Item>`密码到期警告`</Item>` `<Type>`身份鉴别`</Type>`

```xml
    <Uuid>d42f938c-d962-48a0-90f9-***********</Uuid>
    <CheckId>1</CheckId>
    <CheckWarningId>10</CheckWarningId>
    <Level>high</Level>
</CheckWarnings> <PageSize>20</PageSize> <RequestId>0DFCADBA-7065-42DA-AF17-6868B9C2A8CF</RequestId> <CurrentPage>1</CurrentPage> <Count>10</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 100,
    "CheckWarnings": {
        "Status": 1,
```

`"Item": "`密码到期警告`",` `"Type": "`身份鉴别`",`

```json
        "Uuid": "d42f938c-d962-48a0-90f9-***********",
        "CheckId": 1,
        "CheckWarningId": 10,
        "Level": "high"
    },
    "PageSize": 20,
    "RequestId": "0DFCADBA-7065-42DA-AF17-6868B9C2A8CF",
    "CurrentPage": 1,
    "Count": 10
}
```

#### DescribeCheckWarningDetail

调用DescribeCheckWarningDetail接口查询指定检查项的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCheckW arningDetail | 取值：DescribeCheckWarningDetail 。 |
| CheckWarningId | Long | 是 | 1 | 检查项告警ID。 说明查询指定检查项的详细信息，需要提供检查项告警ID。 |

| SourceIp | String | 否 | 192.168.x.x | 访问源IP地址。 |
|---|---|---|---|---|
| Lang | String | 否 | zh | 请求和接收消息的语言类型。 zh：中文。 en：英文。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Advice | String | 立即修复 | 基线检查风险项的加固建议。 |
| CheckId | Long | 1 | 检查项ID。 |
| Description | String | 密码即将过期 | 基线检查风险项的补充描述内容。 |
| Item | String | 密码到期警告 | 检查项名称。 |
| Level | String | high | 检查项的风险等级。 high：高，红色高亮显示，表示风险等级高。 medium：中，橙色高亮显示，表示风险等级为中等。 low：低，灰色高亮显示，表示风险等级低。 |
| Prompt | String | 密码到期警告 | 基线检查风险项的检查提示。 |
| RequestId | String | 09969D2C-4FAD- 429E-BFBF- 9A60DEF8BF6F | 本次调用的请求ID。 |
| Type | String | 身份鉴别 | 基线检查项的类型。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningDetail &CheckWarningId=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 `<Item>`密码到期警告`</Item>` `<Type>`身份鉴别`</Type>` `<Description>`密码即将过期`</Description>`

```xml
<CheckId>1</CheckId> <RequestId>09969D2C-4FAD-429E-BFBF-9A60DEF8BF6F</RequestId>
```

`<Prompt>`密码到期警告`</Prompt>`

```xml
<Level>high</Level>
```

`<Advice>`立即修复`</Advice>` `JSON` 格式

```
{
```

`"Item": "`密码到期警告`",` `"Type": "`身份鉴别`",` `"Description": "`密码即将过期`",`

```json
    "CheckId": 1,
    "RequestId": "09969D2C-4FAD-429E-BFBF-9A60DEF8BF6F",
```

`"Prompt": "`密码到期警告`",`

```json
    "Level": "high",
```

`"Advice": "`立即修复"

```
}
```

#### DescribeWarningMachines

查询执行了基线检查的服务器的信息，包含服务器的ID、服务器名称、检测到的风险项统计数据和风险项状态等信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeWarnin gMachines | 取值：DescribeWarningMachines。 |
| RiskId | Long | 是 | 1 | 风险项ID。 说明查询执行了基线检查的服务器的信息，需要提供基线检查处的风险项ID，该ID可调用DescribeCheckWarningSum mary接口获取。 |
| SourceIp | String | 否 | 47.100.XX.XX | 访问源IP地址。 |
| Lang | String | 否 | zh | 请求和接收消息的语言类型。取值： zh：中文。 en：英文。 |

| MachineName | String | 否 | 基线测试服务器 | 执行基线检查的服务器的名称。 |
|---|---|---|---|---|
| Uuids | String | 否 | xxx-aaa-bbb-ccc | 执行基线检查的服务器ID。多个ID用英文逗号分隔。 |
| StrategyId | Long | 否 | 1 | 基线检查策略的ID。 |
| PageSize | Integer | 否 | 10 | 每页最多显示的数据条数。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Count | Integer | 10 | 总页码数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 10 | 每页最多显示的数据条数。 |
| RequestId | String | 00BD7CE2-284A- 4534-BD09- FB69836DD750 | 本次调用请求的ID。 |
| TotalCount | Integer | 100 | 总数据条数。 |
| WarningMachi nes | Array of WarningMachi ne |  | 产生告警的服务器的信息。 |
| HighWarningC ount | Integer | 10 | 高危检查项的个数。 |
| InstanceId | String | i- m5ee8b9nr3h30m hb**** | 服务器的实例ID。 |
| InstanceName | String | aaawebtest | 实例名称。 |
| InternetIp | String | 47.100.XX.XX | 服务器外网IP。 |
| IntranetIp | String | 192.168.XX.XX | 服务器内网IP。 |
| LowWarningCo unt | Integer | 3 | 低危检查项的个数。 |

| MediumWarni ngCount | Integer | 2 | 中危检查项的个数。 |
|---|---|---|---|
| PassCount | Integer | 10 | 通过检测的检查项个数。 |
| RegionId | String | cn-qingdao** | 服务器所在的地域ID。 |
| Status | Integer | 1 | 基线检查风险项修复完成后，风险项验证的状态。取值： 1：已完成。 2：验证中。 |
| Uuid | String | xxx-aaa-bbb-ccc | 执行基线检查的服务器的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeWarningMachines &RiskId=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>100</TotalCount> <PageSize>10</PageSize> <RequestId>00BD7CE2-284A-4534-BD09-FB69836DD750</RequestId> <CurrentPage>1</CurrentPage> <WarningMachines>
    <Status>1</Status>
    <InstanceName>aaawebtest</InstanceName>
    <MediumWarningCount>2</MediumWarningCount>
    <Uuid>xxx-aaa-bbb-ccc</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <InstanceId>i-m5ee8b9nr3h30mhb****</InstanceId>
    <HighWarningCount>10</HighWarningCount>
    <RegionId>cn-qingdao</RegionId>
    <PassCount>10</PassCount>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <LowWarningCount>3</LowWarningCount>
</WarningMachines> <Count>10</Count>
```

`JSON` 格式

```json
{
    "TotalCount": 100,
    "PageSize": 10,
    "RequestId": "00BD7CE2-284A-4534-BD09-FB69836DD750",
    "CurrentPage": 1,
    "WarningMachines": {
        "Status": 1,
        "InstanceName": "aaawebtest",
        "MediumWarningCount": 2,
        "Uuid": "xxx-aaa-bbb-ccc",
        "InternetIp": "47.100.XX.XX",
        "InstanceId": "i-m5ee8b9nr3h30mhb****",
        "HighWarningCount": 10,
        "RegionId": "cn-qingdao",
        "PassCount": 10,
        "IntranetIp": "192.168.XX.XX",
        "LowWarningCount": 3
    },
    "Count": 10
}
```

### 资产指纹

#### DescribePropertyCount

获取资产指纹的统计信息，即进程、端口、软件、账户和计划任务五种资产指纹的数量统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yCount | 系统规定参数。取值：DescribePropertyCount。 |
| Type | String | 否 | port | 资产指纹类型。取值： user：账户。 software：软件。 process：进程。 port：端口。 cron：计划任务。 说明类型不填表示查询所有类型资产指纹信息。 |
| UuidList | String | 否 | [c4678332- ef3**,c46***] | 资产实例的唯一标识ID列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Autorun | Integer | 123 | 启动项的数量统计。 |
| Cron | Integer | 261 | 计划任务的数量统计。 |
| Port | Integer | 163 | 监听端口的数量统计。 |
| Process | Integer | 367 | 运行进程的数量统计。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | 结果的请求ID。 |
| Sca | Integer | 125 | 中间件的数量统计。 |
| Software | Integer | 5073 | 软件资产的数量统计。 |
| User | Integer | 114 | 账户资产的数量统计。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyCount
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Sca>125</Sca> <User>114</User> <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92****</RequestId> <Port>163</Port> <Software>5073</Software> <Process>367</Process> <Autorun>123</Autorun> <Cron>261</Cron>
```

`JSON` 格式

```json
{
    "Sca": 125,
    "User": 114,
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92****",
    "Port": 163,
    "Software": 5073,
    "Process": 367,
    "Autorun": 123,
    "Cron": 261
}
```

#### DescribePropertyPortDetail

查询端口列表中一个端口的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yPortDetail | 要执行的操作。 取值：DescribePropertyPortDetail。 |
| Remark | String | 否 | 47.100.XX.XX | 服务器名称或IP。 |
| Port | String | 否 | 22 | 端口信息。 |
| ProcName | String | 否 | sshd | 进程名称。 |
| Uuid | String | 否 | 50d213b4-3a35- 427a-b8a5-*** | 资产实例的唯一标识ID。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 6 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 页面显示信息。 |
| Count | Integer | 5 | 当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |

| PageSize | Integer | 5 | 每页最多显示的数据条数。 |
|---|---|---|---|
| TotalCount | Integer | 762 | 数据的总条数。 |
| Propertys | Array of PropertyPort |  | 端口信息。 |
| BindIp | String | 47.100.XX.XX | 端口绑定的IP地址信息。 |
| Create | String | 2019-05- 13T10:39Z | 数据的最新采集时间。 |
| CreateTimesta mp | Long | 1557715141000 | 数据最新采集时间戳。格式：毫秒。 |
| InstanceId | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1fxxx | 端口关联资产的ID。 |
| InstanceName | String | test-*** | 端口关联资产的名称。 |
| InternetIp | String | 42.2.X.X | 资产对应公网IP地址。 |
| IntranetIp | String | 192.168.X.X | 资产对应私网IP地址。 |
| Ip | String | 42.2.X.X | 资产对应公网IP地址。 |
| Port | String | 22 | 端口值。 |
| ProcName | String | sshd | 端口对应的进程名称。 |
| Proto | String | tcp | 端口对应网络协议。 |
| Uuid | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1fXX | 端口关联的资产实例的唯一标识ID。 |
| pid | String | 1 | 父进程进程号。 |
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyPortDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Propertys>
    <InstanceName>test-***</InstanceName>
    <Uuid>50d213b4-3a35-427a-b8a5-04b0c7e1fXX</Uuid>
    <InternetIp>42.2.X.X</InternetIp>
    <Proto>tcp</Proto>
    <InstanceId>50d213b4-3a35-427a-b8a5-04b0c7e1fxxx</InstanceId>
    <Create>2019-05-13T10:39Z</Create>
    <ProcName>sshd</ProcName>
    <Ip>42.2.X.X</Ip>
    <Port>22</Port>
    <pid>1</pid>
    <IntranetIp>192.168.X.X</IntranetIp>
    <CreateTimestamp>1557715141000</CreateTimestamp>
    <BindIp>47.100.XX.XX</BindIp>
</Propertys> <PageInfo>
    <TotalCount>762</TotalCount>
    <PageSize>5</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>5</Count>
</PageInfo> <RequestId> FAA793EF-5B14-4CDD-B3E0-B14D4342C422</RequestId>
```

`JSON` 格式

```json
{
    "Propertys": {
        "InstanceName": "test-***",
        "Uuid": "50d213b4-3a35-427a-b8a5-04b0c7e1fXX",
        "InternetIp": "42.2.X.X",
        "Proto": "tcp",
        "InstanceId": "50d213b4-3a35-427a-b8a5-04b0c7e1fxxx",
        "Create": "2019-05-13T10:39Z",
        "ProcName": "sshd",
        "Ip": "42.2.X.X",
        "Port": 22,
        "pid": 1,
        "IntranetIp": "192.168.X.X",
        "CreateTimestamp": 1557715141000,
        "BindIp": "47.100.XX.XX"
    },
    "PageInfo": {
        "TotalCount": 762,
        "PageSize": 5,
        "CurrentPage": 1,
        "Count": 5
    },
    "RequestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
}
```

#### DescribePropertyProcDetail

获取进程列表中一个进程的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yProcDetail | 系统规定参数。取值：DescribePropertyProcDetail。 |
| Remark | String | 否 | 47.100.XX.XX | 服务器名称或IP。 |
| Name | String | 否 | 8888 | 进程名称。 |
| User | String | 否 | root | 进程的运行用户信息。 |
| Cmdline | String | 否 | ./8888 | 进程的启动参数。 |
| Uuid | String | 否 | c4678332-ef35- 4ad4-*** | 进程关联资产实例的唯一标识ID。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |

| PageSize | Integer | 否 | 5 | 每页最多显示的数据条数。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 页面显示信息。 |
| Count | Integer | 1 | 当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 5 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 1 | 数据的总条数。 |
| Propertys | Array of PropertyProc |  | 进程的信息。 |
| Cmdline | String | ./8888 | 进程对应启动参数。 |
| Create | String | 2019-05- 15T11:08Z | 数据的最新采集时间。 |
| CreateTimesta mp | Long | 1565686951000 | 数据最新采集时间戳。单位：毫秒。 |
| EuidName | String | root | 进程对应的运行权限。 |
| InstanceId | String | c4678332-ef35- 4ad4-8358-*** | 进程关联的资产ID。 |
| InstanceName | String | test-*** | 进程关联的资产名称。 |
| InternetIp | String | 40.2.x.x | 资产对应公网IP地址。 |
| IntranetIp | String | 192.168.x.x | 资产对应私网IP地址。 |
| Md5 | String | N/A | 进程对应的文件MD5信息。 |
| Name | String | 8888 | 进程名称。 |
| Path | String | /root/Oracle/Middle ware/***/8888 | 进程所在路径。 |

| Pid | String | 12826 | 运行进程的身份标识。 |
|---|---|---|---|
| Pname | String | start***.s | 进程所属父进程名称。 |
| StartTime | String | 2019-08-07 10:09:05 | 进程启动时间。格式：yyyy-MM-dd HH:mm:ss。 |
| User | String | root | 进程的运行用户。 |
| Uuid | String | c4678332-ef35- 4ad4-8358-6*** | 进程关联资产实例的唯一标识ID。 |
| RequestId | String | 64388374-A309- 4191-8606- 3346CCA364B0 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyProcDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Propertys>
    <Path>/root/Oracle/Middleware/***/8888</Path>
    <Pname>start***.s</Pname>
    <User>root</User>
    <InstanceId>c4678332-ef35-4ad4-8358-***</InstanceId>
    <StartTime>2019-08-07 10:09:05</StartTime>
    <Pid>12826</Pid>
    <EuidName>root</EuidName>
    <IntranetIp>192.168.x.x</IntranetIp>
    <Name>8888</Name>
    <InstanceName>test-***</InstanceName>
    <Uuid>c4678332-ef35-4ad4-8358-6***</Uuid>
    <InternetIp>40.2.x.x</InternetIp>
    <Create>2019-05-15T11:08Z</Create>
    <Cmdline>./8888</Cmdline>
    <CreateTimestamp>1565686951000</CreateTimestamp>
    <Md5>N/A</Md5>
</Propertys> <PageInfo>
    <TotalCount>1</TotalCount>
    <PageSize>5</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>1</Count>
</PageInfo> <RequestId>64388374-A309-4191-8606-3346CCA364B0</RequestId>
```

`JSON` 格式

```json
{
    "Propertys": {
        "Path": "/root/Oracle/Middleware/***/8888",
        "Pname": "start***.s",
        "User": "root",
        "InstanceId": "c4678332-ef35-4ad4-8358-***",
        "StartTime": "2019-08-07 10:09:05",
        "Pid": 12826,
        "EuidName": "root",
        "IntranetIp": "192.168.x.x",
        "Name": 8888,
        "InstanceName": "test-***",
        "Uuid": "c4678332-ef35-4ad4-8358-6***",
        "InternetIp": "40.2.x.x",
        "Create": "2019-05-15T11:08Z",
        "Cmdline": "./8888",
        "CreateTimestamp": 1565686951000,
        "Md5": "N/A"
    },
    "PageInfo": {
        "TotalCount": 1,
        "PageSize": 5,
        "CurrentPage": 1,
        "Count": 1
    },
    "RequestId": "64388374-A309-4191-8606-3346CCA364B0"
}
```

#### DescribePropertyPortItem

获取所有端口信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yPortItem | 要执行的操作。 取值：DescribePropertyPortItem。 |
| ForceFlush | Boolean | 否 | true | 是否强制刷新待查询数据。 |
| Port | String | 否 | 22 | 端口号。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 5 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 页面显示信息。 |
| Count | Integer | 5 | 当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 5 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 163 | 数据的总条数。 |
| PropertyItems | Array of PropertyItem |  | 端口信息。 |
| Count | Integer | 495 | 端口对应的服务器数量。 |
| Port | String | 22 | 监听端口号。 |
| Proto | String | tcp | 端口对应的网络协议。 |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyPortItem
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
        <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId>
        <PropertyItems>
       <Port>22</Port>
       <Proto>tcp</Proto>
       <Count>495</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>111</Port>
       <Proto>tcp</Proto>
       <Count>43</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>6000</Port>
       <Proto>tcp</Proto>
       <Count>2</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>53</Port>
       <Proto>tcp</Proto>
       <Count>1</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>80</Port>
       <Proto>tcp</Proto>
       <Count>38</Count>
     </PropertyItems>
        <PageInfo>
       <Count>5</Count>
       <PageSize>5</PageSize>
       <TotalCount>163</TotalCount>
       <CurrentPage>1</CurrentPage>
     </PageInfo>
```

`JSON` 格式

```json
{
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "PropertyItems": [
      {
        "Port": "22",
        "Proto": "tcp",
        "Count": 495
      },
      {
        "Port": "111",
        "Proto": "tcp",
        "Count": 43
      },
      {
        "Port": "6000",
        "Proto": "tcp",
        "Count": 2
      },
      {
        "Port": "53",
        "Proto": "tcp",
        "Count": 1
      },
      {
        "Port": "80",
        "Proto": "tcp",
        "Count": 38
      }
```

`],`

```json
  "PageInfo": {
      "Count": 5,
      "PageSize": 5,
      "TotalCount": 163,
      "CurrentPage": 1
    }
}
```

#### DescribePropertyProcItem

获取所有进程信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yProcItem | 系统规定参数。取值：DescribePropertyProcItem。 |
| ForceFlush | Boolean | 否 | true | 是否强制刷新待查询数据。 |

| Name | String | 否 | test | 进程名称。 |
|---|---|---|---|---|
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 10 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 页面显示信息。 |
| Count | Integer | 5 | 分页查询时，显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 5 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 372 | 数据的总条数。 |
| PropertyItems | Array of PropertyProcIt em |  | 进程的信息。 |
| Count | Integer | 8888 | 进程名对应的服务器数量。 |
| Name | String | .ss | 进程名称。 |
| RequestId | String | BD8AD4C6-A169- 4FA3-BA1F- ED40ED52973B | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyProcItem
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <PropertyItems>
        <Name>(sd-**)</Name>
        <Count>7</Count>
  </PropertyItems>
  <PropertyItems>
        <Name>6Cm***</Name>
        <Count>1</Count>
  </PropertyItems>
  <RequestId>BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B</RequestId>
  <PageInfo>
        <Count>2</Count>
        <TotalCount>395</TotalCount>
        <PageSize>2</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
```

`JSON` 格式

```json
{
 "PropertyItems": [
  {
   "Name": "(sd-**)",
   "Count": 7
  },
  {
   "Name": "6Cm***",
   "Count": 1
  }
```

`],`

```json
 "RequestId": "BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B",
 "PageInfo": {
  "Count": 2,
  "TotalCount": 395,
  "PageSize": 2,
  "CurrentPage": 1
 }
}
```

#### DescribePropertySoftwareDetail

获取软件列表中一个软件的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | DescribePropert ySoftwareDetail | 系统规定参数。取值：DescribePropertySoftwareDe tail。 |
|---|---|---|---|---|
| Remark | String | 否 | 47.100.XX.XX | 服务器名称或IP。 |
| Name | String | 否 | tes*** | 软件名称。 |
| Path | String | 否 | /etc/test | 软件安装路径。 |
| SoftwareVersion | String | 否 | 11 | 软件版本信息。 |
| Uuid | String | 否 | 50d213b4-3a35- 427a-b8a5-*** | 软件所属资产实例的唯一标识ID。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 5 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 页面的显示信息。 |
| Count | Integer | 2 | 显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 2 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 23 | 数据的总条数。 |
| Propertys | Array of PropertySoftw are |  | 软件的信息。 |
| Create | Long | 1565539587000 | 数据的最新采集时间。单位：毫秒。 |
| CreateTimesta mp | Long | 1565539587000 | 数据的最新采集时间戳。单位：毫秒。 |

| InstallTime | String | 2017-09-07 10:54:49 | 返回的软件安装时间。格式：yyyy-MM-dd HH:mm:ss。 |
|---|---|---|---|
| InstallTimeSta mp | Long | 1565539587000 | 软件安装时间戳。单位：毫秒。 |
| InstanceId | String | i-uf*** | 资产实例ID。 |
| InstanceName | String | test | 资产名称。 |
| InternetIp | String | 47.100.XX.XX | 资产对应公网IP地址。 |
| IntranetIp | String | 192.168.0.1 | 资产对应私网IP地址。 |
| Ip | String | 47.100.XX.XX | 显示IP。 说明有公网展示公网IP，无公网展示内网IP。 |
| Name | String | aaa base _ | 软件名称。 |
| Path | String | /etc/test | 软件资产的安装目录信息。 |
| Uuid | String | 4ef1115b-e423- 4b4b-b930-*** | 返回的软件版本信息。 |
| Version | String | 11 | 软件资产对应的版本信息。 |
| RequestId | String | 9C5AE850-7140- 4DE6-B892- 055EB0D9F28A | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Propertys>
    <InstanceName>test</InstanceName>
    <Path>/etc/test</Path>
    <Uuid>4ef1115b-e423-4b4b-b930-***</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <InstallTimeStamp>1565539587000</InstallTimeStamp>
    <InstanceId>i-uf***</InstanceId>
    <Version>11</Version>
    <InstallTime>2017-09-07 10:54:49</InstallTime>
    <Create>1565539587000</Create>
    <Ip>47.100.XX.XX</Ip>
    <IntranetIp>192.168.0.1</IntranetIp>
    <CreateTimestamp>1565539587000</CreateTimestamp>
    <Name>aaa_base</Name>
</Propertys> <PageInfo>
    <TotalCount>23</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>9C5AE850-7140-4DE6-B892-055EB0D9F28A</RequestId>
```

`JSON` 格式

```json
{
    "Propertys": {
        "InstanceName": "test",
        "Path": "/etc/test",
        "Uuid": "4ef1115b-e423-4b4b-b930-***",
        "InternetIp": "47.100.XX.XX",
        "InstallTimeStamp": 1565539587000,
        "InstanceId": "i-uf***",
        "Version": 11,
        "InstallTime": "2017-09-07 10:54:49",
        "Create": 1565539587000,
        "Ip": "47.100.XX.XX",
        "IntranetIp": "192.168.0.1",
        "CreateTimestamp": 1565539587000,
        "Name": "aaa_base"
    },
    "PageInfo": {
        "TotalCount": 23,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
    },
    "RequestId": "9C5AE850-7140-4DE6-B892-055EB0D9F28A"
}
```

#### DescribePropertySoftwareItem

获取所有软件列表信息.。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert ySoftwareItem | 要执行的操作。 取值：DescribePropertySoftwareIte m。 |
| ForceFlush | Boolean | 否 | true | 是否强制刷新待查询数据。 |
| Name | String | 否 | test | 指定待查询的软件名称。 |
| CurrentPage | Integer | 否 | 1 | 指定返回结果的当前页码。 |
| PageSize | Integer | 否 | 10 | 指定列表每页显示数据条数 。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 返回结果的页面显示信息。 |
| Count | Integer | 2 | 返回结果的当前页显示数据条数。 |
| CurrentPage | Integer | 1 | 返回结果中显示的当前页码。 |
| PageSize | Integer | 2 | 返回结果中每页显示数据条数。 |
| TotalCount | Integer | 5037 | 返回数据的总条数。 |
| PropertyItems | Array of PropertySoftw areItem |  | 返回的软件列表。 |
| Count | Integer | 23 | 返回结果中软件资产对应的服务器数量。 |
| Name | String | aaa base _ | 返回的软件资产名称。 |
| RequestId | String | 3A85CFCF-05C8- 451A-9E41- C0D5E96BA407 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareItem
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <PageInfo>
       <Count>2</Count>
       <PageSize>2</PageSize>
       <TotalCount>5037</TotalCount>
       <CurrentPage>1</CurrentPage>
   </PageInfo>
   <PropertyItems>
       <Name>a11y-profile-manager-indicator</Name>
       <Count>1</Count>
   </PropertyItems>
   <PropertyItems>
       <Name>aaa_base</Name>
       <Count>23</Count>
   </PropertyItems>
   <requestId>3A85CFCF-05C8-451A-9E41-C0D5E96BA407</requestId>
```

`JSON` 格式

```json
{
  "PageInfo": {
      "Count": 2,
      "PageSize": 2,
      "TotalCount": 5037,
      "CurrentPage": 1
    },
    "PropertyItems": [
      {
        "Name": "a11y-profile-manager-indicator",
        "Count": 1
      },
      {
        "Name": "aaa_base",
        "Count": 23
      }
```

`],`

```json
     "requestId": "3A85CFCF-05C8-451A-9E41-C0D5E96BA407"
}
```

#### DescribePropertyUserDetail

获取账号列表中一个账号的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yUserDetail | 要执行的操作。 取值：DescribePropertyUserDetail。 |
| Remark | String | 否 | 47.100.XX.XX | 服务器名称或IP。 |
| User | String | 否 | tes*** | 指定待查询的账户名称。 |
| IsRoot | String | 否 | 0 | 是否拥有ROOT权限。取值包括： 0：否。 1：是。 |
| Uuid | String | 否 | 50d213b4-*****- 427a-b8a5- 04b0c7****** | 指定待查询的资产UUID。 |
| CurrentPage | Integer | 否 | 1 | 指定返回结果的当前页码。 |
| PageSize | Integer | 否 | 2 | 指定列表每页显示数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 返回结果的页面显示信息。 |
| Count | Integer | 2 | 返回结果的当前页显示数据条数。 |
| CurrentPage | Integer | 1 | 返回结果中显示的当前页码。 |
| PageSize | Integer | 2 | 返回结果中每页显示数据条数。 |
| TotalCount | Integer | 384 | 返回数据的总条数。 |
| Propertys | Array of PropertyUser |  | 返回的账号详情列表。 |
| AccountsExpir ationDate | String | 无 | 已废弃。 |

| Create | String | 2022-01- 03T06:43Z | 返回结果中的最新采集时间。使用yyyy-MM- ddTHH:mmZ格式。 |
|---|---|---|---|
| CreateTimesta mp | Long | 1565644643000 | 返回结果中的采集时间戳。单位：毫秒。 |
| GroupNames | List | adm | 用户组。 |
| InstanceId | String | 02c4a5dc-****- 483a-9015- f972b****** | 返回结果中的资产ID。 |
| InstanceName | String | e21g06001.cloud.g 06.xxx | 返回结果中的资产名称。 |
| InternetIp | String | 47.100.XX.XX | 返回结果中资产对应公网IP地址。 |
| IntranetIp | String | 192.168.0.1 | 返回结果中资产对应私网IP地址。 |
| Ip | String | 47.100.XX.XX | 返回结果中的IP地址。 |
| IsRoot | String | 0 | 返回账号是否为ROOT权限。 0：否。 1：是。 |
| LastLoginIp | String | 47.100.XX.XX | 上次登录来源。 |
| LastLoginTime | String | 2022-01-03 06:33:33 | 上次登录时间。使用yyyy-MM-dd HH:mm:ss 格式。 |
| LastLoginTime stamp | Long | 1565644643000 | 上次登录时间戳。单位：毫秒。 |
| PasswordExpir ationDate | String | 无 | 已废弃。 |
| Status | String | 0 | 返回账号的登录状态。 取值包括： 0：不可登录。 1：可登录。 |
| User | String | adm | 账户名称。 |
| Uuid | String | 02c4a5dc-c2d2- 483a-9015- f972b4****** | 返回结果中的资产UUID。 |

| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | 本次调用请求的ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyUserDetail
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Propertys>
    <Status>0</Status>
    <IsRoot>0</IsRoot>
    <User>adm</User>
    <InstanceId>02c4a5dc-****-483a-9015-f972b******</InstanceId>
    <LastLoginIp>47.100.XX.XX</LastLoginIp>
    <Ip>47.100.XX.XX</Ip>
    <IntranetIp>192.168.0.1</IntranetIp>
    <AccountsExpirationDate>无</AccountsExpirationDate>
    <InstanceName>e21g06001.cloud.g06.xxx</InstanceName>
    <LastLoginTime>2022-01-03 06:33:33</LastLoginTime>
    <Uuid>02c4a5dc-c2d2-483a-9015-f972b4******</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <LastLoginTimestamp>1565644643000</LastLoginTimestamp>
    <Create>2022-01-03T06:43Z</Create>
    <CreateTimestamp>1565644643000</CreateTimestamp>
    <PasswordExpirationDate>无</PasswordExpirationDate>
    <GroupNames>adm</GroupNames>
</Propertys> <PageInfo>
    <TotalCount>384</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</RequestId>
```

`JSON` 格式

```json
{
    "Propertys": {
        "Status": 0,
        "IsRoot": 0,
        "User": "adm",
        "InstanceId": "02c4a5dc-****-483a-9015-f972b******",
        "LastLoginIp": "47.100.XX.XX",
        "Ip": "47.100.XX.XX",
        "IntranetIp": "192.168.0.1",
        "AccountsExpirationDate": "无",
        "InstanceName": "e21g06001.cloud.g06.xxx",
        "LastLoginTime": "2022-01-03 06:33:33",
        "Uuid": "02c4a5dc-c2d2-483a-9015-f972b4******",
        "InternetIp": "47.100.XX.XX",
        "LastLoginTimestamp": 1565644643000,
        "Create": "2022-01-03T06:43Z",
        "CreateTimestamp": 1565644643000,
        "PasswordExpirationDate": "无",
        "GroupNames": "adm"
    },
    "PageInfo": {
        "TotalCount": 384,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
    },
    "RequestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
}
```

#### DescribePropertyUserItem

获取资产的账号信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePropert yUserItem | 系统规定参数。取值：DescribePropertyUserItem。 |
| ForceFlush | Boolean | 否 | true | 是否强制刷新待查询数据。 |
| User | String | 否 | adm | 资产指纹的账号信息。 |
| CurrentPage | Integer | 否 | 1 | 当前页的页码。 |
| PageSize | Integer | 否 | 2 | 每页最多显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 页面显示信息。 |
| Count | Integer | 2 | 显示的当前页的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 2 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 114 | 总数据条数。 |
| PropertyItems | Array of PropertyUserIt em |  | 账号信息。 |
| Count | Integer | 384 | 账号对应的服务器数量。 |
| User | String | adm | 账号名称。 |
| RequestId | String | 76068BE2-F9C4- 4EDD-967B- F503B8CCXXXX | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePropertyUserItem
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PageInfo>
    <TotalCount>114</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>76068BE2-F9C4-4EDD-967B-F503B8CCXXXX</RequestId> <PropertyItems>
    <User>adm</User>
    <Count>384</Count>
</PropertyItems>
```

`JSON` 格式

```json
{
    "PageInfo": {
        "TotalCount": 114,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
    },
    "RequestId": "76068BE2-F9C4-4EDD-967B-F503B8CCXXXX",
    "PropertyItems": {
        "User": "adm",
        "Count": 384
    }
}
```

#### DescribeModuleConfig

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeModule Config | 需要执行的操作。 取值：DescribeModuleConfig |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | 结果的请求ID。 |
| Success | Boolean | true | 请求是否成功。 |
| Count | Integer | 2 | 模块设置信息个数。 |
| HttpStatusCod e | Integer | 200 | 响应码。 |
| ModuleConfigL ist | Array |  | 模块设置信息列表。 |
| ConfigName | String | timescan | 设置名称。 |
| ModuleName | String | alihids | 模板名称。 |

| Items | Array |  | 设置项列表。 |
|---|---|---|---|
| InstanceId | String | lb-xxx | 机器实例ID。 |
| InstanceName | String | ssxxxxxxxx | 机器实例名称。 |
| GroupId | Integer | 173 | 分组ID。 |
| Ip | String | 2.2.2.2 | 机器IP。 |
| Region | String | outside-of-aliyun | 地域。 |
| Uuid | String | lb-xxxx-xxxx-xxxx- xxxx | 服务器uuid。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeModuleConfig
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<code>200</code> <data>
    <Count>2</Count>
    <ModuleConfigList>
        <ConfigName>timescan</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>ssxxxxxxxx</InstanceName>
            <Uuid>lb-xxxx-xxxx-xxxx-xxxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.1.2.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
    <ModuleConfigList>
        <ConfigName>sysvulfix</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>xx</InstanceName>
            <Uuid>lb-xxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.168.5.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
</data> <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId> <success>true</success>
```

`JSON` 格式

```json
{
  "code": 200,
  "data": {
    "Count": 2,
    "ModuleConfigList": [{
        "ConfigName": "timescan",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "ssxxxxxxxx",
            "Uuid": "lb-xxxx-xxxx-xxxx-xxxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
          },
          {
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.1.2.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
          }
```

]

```json
      },
      {
        "ConfigName": "sysvulfix",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "xx",
            "Uuid": "lb-xxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
          },
          {
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.168.5.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
          }
```

]

```
      }
```

]

```json
  },
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
}
```

**错误码**

关于本接口的错误码的详细解释，请查看错误代码表。

### 资产暴露

#### DescribeExposedInstanceList

获取资产暴露列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeExpose dInstanceList | 系统规定参数。取值：DescribeExposedInstanceList 。 |
| PageSize | Integer | 否 | 20 | 分页查询时，每页最多显示的数据条数。 |
| CurrentPage | Integer | 否 | 1 | 分页查询时，当前页的页码。 |
| GroupId | Long | 否 | 9469268 | 服务器分组ID。 |
| VulStatus | Boolean | 否 | true | 指定要查询的服务器是否存在漏洞。取值： true：存在。 false：不存在。 |
| HealthStatus | Boolean | 否 | true | 可被利用基线数量。 |
| ExposureCompo nent | String | 否 | openssl | 指定要查询的暴露在互联网中的系统组件名称。 |
| ExposurePort | String | 否 | 22 | 指定要查询的暴露端口。 |
| ExposureIp | String | 否 | 116.12.XX.XX | 指定要查询的服务器公网IP。 |
| InstanceId | String | 否 | i- bp1g6wxdwps7s 9dz**** | 指定要查询的服务器实例ID。 |
| InstanceName | String | 否 | abc centos7.2 0 _ _ 05 | 指定要查询的服务器名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| ExposedInstan ces | Array of ExposedInstan ce |  | 资产暴露分析的列表信息。 |
|---|---|---|---|
| AsapVulCount | Integer | 0 | 暴露在互联网上可被黑客利用的高危漏洞数量。 |
| ExploitHealthC ount | Integer | 0 | 可被利用基线数量。 |
| ExposureCom ponent | String | openssl,openssh | 暴露在互联网上的系统组件。 |
| ExposureIp | String | 116.12.XX.XX | 暴露在互联网上的公网IP。 |
| ExposurePort | String | 22 | 暴露在互联网上的端口。 |
| ExposureType | String | INTERNET IP _ | 暴露方式。取值： INTERNET IP：ECS公网IP。 _ SLB：负载均衡SLB公网IP。 EIP：弹性公网IP。 DNAT：使用DNAT功能连接互联网的NAT网关。 |
| ExposureTypeI d | String | i-ew11313a**** | 暴露方式对应的实例ID，不同暴露方式对应不同的实例ID。 当ExposureType为INTERNET IP时：取值 _ 为空。 当ExposureType为SLB时：取值为负载均衡公网实例ID。 当ExposureType为EIP时：取值为弹性公网 IP的实例ID。 当ExposureType为DNAT时：取值为NAT网关实例ID。 |
| GroupId | Long | 9469268 | 服务器分组ID。 |
| GroupName | String | 未分组 | 服务器分组名称。 |
| InstanceId | String | i- bp1g6wxdwps7s9d z**** | 服务器实例ID。 |
| InstanceName | String | abc centos7.2 005 _ _ | 服务器名称。 |
| InternetIp | String | 116.12.XX.XX | 服务器公网IP。 |
| IntranetIp | String | 192.168.XX.XX | 服务器私网IP。 |

| LaterVulCount | Integer | 0 | 暴露在互联网上可被黑客利用的中危漏洞数量。 |
|---|---|---|---|
| NntfVulCount | Integer | 0 | 暴露在互联网上可被黑客利用的低危漏洞数量。 |
| RegionId | String | cn-hangzhou | 服务器所在区域的ID。 |
| TotalVulCount | Integer | 0 | 暴露在互联网上可被黑客利用的漏洞总数量。 |
| Uuid | String | dd803d9e-a337- 4add-9c5b- 7d503e08**** | 服务器UUID。 |
| PageInfo | Struct |  | 分页信息。 |
| Count | Integer | 2 | 当前页显示的数据条数。 |
| CurrentPage | Integer | 1 | 当前页的页码。 |
| PageSize | Integer | 20 | 每页最多显示的数据条数。 |
| TotalCount | Integer | 2 | 总数居条数。 |
| RequestId | String | 598A4A61-ABA7- 456B-8725- 7378258276D9 | 本次调用请求的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeExposedInstanceList
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PageInfo>
    <TotalCount>2</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>598A4A61-ABA7-456B-8725-7378258276D9</RequestId> <ExposedInstances>
    <GroupName>未分组</GroupName>
    <TotalVulCount>0</TotalVulCount>
    <ExposureType>INTERNET_IP</ExposureType>
    <InstanceId>i-bp1g6wxdwps7s9dz****</InstanceId>
    <ExposureComponent>openssl,openssh</ExposureComponent>
    <ExposurePort>22</ExposurePort>
    <NntfVulCount>0</NntfVulCount>
    <AsapVulCount>0</AsapVulCount>
    <ExploitHealthCount>0</ExploitHealthCount>
    <IntranetIp>192.168.XX.XX </IntranetIp>
    <GroupId>9469268</GroupId>
    <InstanceName>abc_centos7.2_005 </InstanceName>
    <Uuid>dd803d9e-a337-4add-9c5b-7d503e08****</Uuid>
    <ExposureIp>116.12.XX.XX </ExposureIp>
    <ExposureTypeId>i-ew11313a****</ExposureTypeId>
    <InternetIp>116.12.XX.XX</InternetIp>
    <LaterVulCount>0</LaterVulCount>
    <RegionId>cn-hangzhou</RegionId>
</ExposedInstances>
```

`JSON` 格式

```json
{"PageInfo": {"TotalCount":"2","PageSize":"20","CurrentPage":"1","Count":"2"},"RequestId":"598A4A61- ABA7-456B-8725-7378258276D9","ExposedInstances":[{"GroupName":"未分组","TotalVulCount":"0","ExposureType":"INTERNET_IP","InstanceId":"ibp1g6wxdwps7s9dz****","ExposureComponent":"openssl,openssh","ExposurePort":"22","NntfVulC nt":"0","AsapVulCount":"0","ExploitHealthCount":"0","IntranetIp":"192.168.XX.XX\t","Group ":"9469268","InstanceName":"abc_centos7.2_005\t","Uuid":"dd803d9e-a337-4add-9c5b-7d503e 08****","ExposureIp":"116.12.XX.XX\t","ExposureTypeId":"iew11313a****","InternetIp":"116.12.XX.XX","LaterVulCount":"0","RegionId":"cn-hangzhou"} ]}
```
