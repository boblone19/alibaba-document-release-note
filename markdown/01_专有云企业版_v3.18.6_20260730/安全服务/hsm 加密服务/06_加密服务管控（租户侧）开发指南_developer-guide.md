---
title: "加密服务 加密服务管控（租户侧）开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 112
source_pdf: "06_加密服务管控（租户侧）开发指南_developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/hsm/zh/developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 加密服务 加密服务管控（租户侧）开发指南

加密服务

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
加密服务
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云AP。本文介绍如何通过POP网关调用专有云API。

**流程图**

加密服务

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
加密服务

## 准备工作

### 登录API与工具控制台

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

### 获取API信息及其EndPoint

通过POP网关调用API需要您了解产品开放API接口的相关信息，本文为您介绍获取云产品的Endpoint的两种方式。

**背景信息**

加密服务为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

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
加密服务
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
apigateway.openapi.endpoint值，即 `Endpoint` 。

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

加密服务

| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |
|---|---|

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
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击**个人信息**。 加密服务 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourAccessKeyID>：请替换为您实际的AccessKey ID。 <yourAccessKeySecret>：请替换为您实际的AccessKey Secret。 <yourRoleSessionName>：请替换为您当前实际的会话名称。 该名称为用户自定义，通常设置为调用该API的用户身份，例如：用户名。在同一个RAM角色执行的操作中，可以根据不同的 `RoleSessionName` 来区分实际操作者，以实现用户级别的访问审计。长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-）和下划线（_）。 <yourRoleArn>：请替换为您实际的RAM Role。 "sts.aliyuns.com" ：请替换为实际的STS Endpoint。 加密服务

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
加密服务

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

加密服务

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

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your-region-id>，请替换为您实际的地域ID。 <your-access-key-id>，请替换为您实际的AccessKey ID。 <your-access-key-secret>>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您当前产品实际的Endpoint。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。 加密服务

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

本文介绍如何安装及调用云盾Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用云盾的开发工具包，必须安装阿里云Java SDK核心库。SDK核心库推荐使用4.5.17及以上版本。 您在安装阿里云Java SDK核心库时，需要在pom.xml文件中添加以下依赖。关于准确的SDK版本号，请参见阿里云开发工具包（SDK）。 加密服务

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 使用CommonRequest进行调用

通过POP Java SDK访问产品域名，需要了解该产品调用方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **API****调试**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

目前仅支持通过RPC方式调用API。

**CommonRequest调用示例**

RPC调用，示例接口信息：接口（DescribeVpc）、版本（2018-06-30）。 加密服务

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

```java
        CommonRequest request = new CommonRequest();
        request.setDomain("<hsmprivateEndpoint>");// 当前产品实际的Endpoint
        request.setVersion("2018-06-30");// 接口的版本
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

加密服务

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

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your_region_id>，请替换为您实际的地域ID。 <your_access_key_id>，请替换为您实际的AccessKey ID。 <your_access_key_secret>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您实际的产品访问地址。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。 加密服务

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

本文为您介绍POP Python SDK调用云产品API的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **API****调试**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！ 加密服务

**背景信息**

目前仅支持通过RPC方式调用API。

**CommonRequest调用示例**

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<hsmprivateEndpoint>') //当前产品实际的Endpoint request.set_version('2018-06-30') //接口的版本
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
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
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
```

)

```
request.set_protocol_type('https') # 使用https client.do_action_with_exception(request)
```

**忽略证书**

加密服务

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
加密服务

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

加密服务本文为您介绍POP Go SDK调用的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **API****调试**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

目前仅支持通过RPC方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：接口（DescribeVpc）、版本（2018-06-30）。

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
    request.Domain = "<hsmprivateEndpoint>"// 当前产品实际的Endpoint
    request.Version = "2018-06-30"// 接口的版本
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

**设置代理**

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 加密服务

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

加密服务

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

加密服务

| EndpointPre | Strin g | 是 | 接口对应的域名前缀。取值： auditprivate：云盾基础组件。 yundunnextsoc-pop：云安全管理中心（SOC）。 tds：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy-share：网络流量检测与响应。 ddosprivate：DDos 清洗。 hsmprivate：加密服务。 cloudfw：云防火墙。 sddp-api：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |
|---|---|---|---|

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。 加密服务

## API参考

**5.1.**

### ModifyReleaseProtectionStatus

修改云密码机实例的保护状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Resource OwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| InstanceId | Strin g | Query | 是 | hsm-0k121E5c3**** | 密码机实例ID。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |
| OpenStat us | Integ er | Query | 是 | 0 | 实例保护开启状态。取值： 0：关闭。 1：开启。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyReleaseProtectionStatus &InstanceId=hsm-0k121E5c3**** &OpenStatus=
```

&公共请求参数正常返回示例加密服务 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1002 | ParamsInvalid | The param %s is invalid, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 500 | -2009 | VsmLockedStatusError | The vsm device %s occupied by the instance is in a locked state, please try again later |
| 400 | -4020 | InstanceExistInCluster | The instance %s is already exist in cluster, operation not allowed |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### GetHsmIds

查询由密码机SN组成的唯一标识集

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | 是 | cn-hangzhou | 地域ID。 |
| ZoneId | Strin g | Query | 是 | cn-hangzhou-b | 可用区ID。 |
| VendorCo de | Strin g | Query | 是 | jnta | 密码机实例所用设备的设备厂商编码。 说明 ：您可以调用DescribeVendors 接口获取该参数。 |
| ProductCo de | Strin g | Query | 是 | jnta.SJJ**** | 密码机实例所用设备的设备型号编码。 说明 ：如果查询单个密码机集群的详情，此参数无效。您可以调用DescribeProducts 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HsmIds | List | ["hsm- 20132564xxxxx","h sm-21531532xxx"] | 由密码机SN组成的设备唯一标识 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &VendorCode=jnta &ProductCode=jnta.SJJ****
```

&公共请求参数正常返回示例 `JSON` 格式加密服务

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "HsmIds":["hsm-20132564xxxxx","hsm-21531532xxx"],
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<HsmIds>["hsm-20132564xxxxx","hsm-21531532xxx"]</HsmIds> <RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 400 | -1002 | ParamsInvalid | The param %s is invalid, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### GetChannelStatus

查询密码机实例的状态集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |

**返回数据**

加密服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ChannelStatus List | Array | [{"Code":"1","Nam e":"未初始化"}, {"Code":"5","Name ":"运行中"}] | 密码机实例状态集。 |
| -Code | String | 1 | 密码机实例状态的code。 |
| -Name | String | 未初始化 | 密码机实例的状态名称。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "ChannelStatusList":[
  {
   "Code":"1",
```

`"Name":"`未初始化"

```
  }
```

]

```
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DescribeInstances

获取密码机实例的数据集

**请求头**

加密服务该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh：中文。 en：英文。 |
| PageSize | Integ er | Query | 否 | 15 | 分页查询时，指定每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 分页查询时，设置当前页面的页码。 |
| RegionId | Strin g | Query | 是 | cn-neimeng-*****-d01 | 密码机实例所在地域的编号。 说明 ：您可以调用DescribeRegions 接口获取该参数。 |
| HsmStatu s | Integ er | Query | 否 | 5 | 密码机实例状态。取值： 1：未初始化。 3：已释放。 4：生产失败。 5：运行中。 6：同步中。 7：重置中。 8：已停用。 说明 ：此参数仅支持单状态查询，兼容历史版本未删除。当该参数与Status参数同时有值时，此参数无效， 查询结果以Status参数为准。 |
| InstanceId | Strin g | Query | 否 | hsm-0k121E5c3**** | 密码机实例ID。 说明 ：您可以调用本接口获取该参数。 |
| VpcIp | Strin g | Query | 否 | 192.168.XX.XX | 密码机实例所注册的经典网络IP地址。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| VsmType | Strin g | Query | 否 | evsm | 密码机实例的设备类型。取值： evsm：金融数据密码机。 gvsm：通用服务器密码机。 svsm：签名验签服务器密码机。 |
| Status | Strin g | Query | 否 | 1,5 | 密码机实例状态。取值： 1：未初始化。 3：已释放。 4：生产失败。 5：运行中。 6：同步中。 7：重置中。 8：已停用。 说明 ：此参数支持多个状态的密码机实例查询。当该参数与HsmStatus参数同时有值时，HsmStatus参数无效，查询结果该参数为准。 |
| ClusterId | Strin g | Query | 否 | cluster-***** | 密码机实例所属集群的ID。 说明 ：您可以调用DescribeClusters 接口获取该参数。 |
| ZoneNo | Strin g | Query | 否 | cn-qingdao-env***- amtest***-a | 密码机实例所在可用区的编号。 说明 ：您可以调用DescribeZones 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Instances | Array |  | 密码机实例数据集。 |
| -WhiteList | Normal | ["192.168.XX.XX"," 172.16.XX.XX"] | 密码机实例的白名单IP数组。 **说明：**如果当前实例有所属集群，则白名单与集群白名单保持一致。 |
| -InstanceId | String | hsm- 0k121E5c3**** | 密码机实例ID。 |

| 加密服务 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -RegionId | String | cn-neimeng-*****- d01 | 密码机实例所在地域编号。 |
| -HsmStatus | Integer | 5 | 密码机实例状态。取值： 1：未初始化。 3：已释放。 4：生产失败。 5：运行中。 6：同步中。 7：重置中。 8：已停用。 |
| -VpcId | String | vpc- ke7kj03hq3es7luti* *** | 配置给密码机实例的VPC实例ID。 |
| -VswitchId | String | vsw- ke7j6p4za4lwtjrju* *** | 配置给密码机实例的交换机实例ID。 |
| -Ip | String | 192.168.XX.XX | 密码机实例对应的经典网络的IP地址。 |
| -Remark | String | testInstance | 密码机实例的别名。 |
| -VendorName | String | 江南天安 | 密码机实例所用设备的设备厂商名称。 |
| -VendorCode | String | jnta | 密码机实例所用设备的设备厂商编码。 |
| -ProductName | String | 江南天安云密码机 | 密码机实例所用设备的设备型号名称。 |
| -ProductCode | String | jnta.SJJ**** | 密码机实例所用设备的设备型号编码。 |
| -VsmType | String | evsm | 密码机实例的设备类型。取值： evsm：金融数据密码机。 gvsm：通用服务器密码机。 svsm：签名验签服务器密码机。 |
| -ClusterId | String | cluster-***** | 密码机实例所在集群的ID。 |
| -ClusterName | String | testCluster | 密码机实例所在集群的名称。 |

加密服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -IsMaster | Integer | 1 | 当前密码机在集群中是否是主密码机。取值： 0：不是。 1：是。 |
| -ZoneNo | String | cn-qingdao-env***- amtest***-a | 密码机实例所在的可用区编号。 |
| - ShowCreateCl uster | Boolean | true | 是否可以创建集群。取值： true：是。 false：否。 说明 ：创建集群的功能存在使用限制，只有支持集群能力的设备厂商的密码机才可以创建集群。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |
| TotalCount | Long | 5 | 集群数据集的总记录数。 |
| CurrentPage | Integer | 1 | 页查询时，设置当前页面的页码。 |
| PageSize | Integer | 15 | 分页查询时，指定每页最多显示的数据条数。 |

**示例**

请求示例

```
&RegionId=cn-neimeng-*****-d01
```

&公共请求参数正常返回示例 `JSON` 格式加密服务

```json
{
 "Instances":[{
```

`"VendorName":"`江南天安`",` `"ProductName":"`江南天安云密码机`",`

```json
  "InstanceId":"hsm-0k121E5c3****",
  "ProductCode":"jnta.SJJ****",
  "ClusterId":"cluster-*****",
  "Ip":"10.25.XX.XX",
  "WhiteList":"[\"192.168.XX.XX\",\"172.16.XX.XX\"]",
  "VswitchId":"vsw-ke7j6p4za4lwtjrju****",
  "ZoneNo":"cn-qingdao-env***-amtest***-a",
  "Remark":"testInstance",
  "ShowCreateCluster":true,
  "HsmStatus":5,
  "VpcId":"vpc-ke7kj03hq3es7luti****",
  "VsmType":"evsm",
  "IsMaster":1,
  "VendorCode":"jnta",
  "ClusterName":"testCluster",
  "RegionId":"cn-neimeng-*****-d01"
 }],
 "TotalCount":5,
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "PageSize":15,
 "CurrentPage":1
}
```

`XML` 格式加密服务

```xml
<Instances>
 <VendorName>江南天安</VendorName>
```

`<ProductName>`江南天安云密码机`</ProductName>`

```xml
 <InstanceId>hsm-0k121E5c3****</InstanceId>
 <ProductCode>jnta.SJJ****</ProductCode>
 <ClusterId>cluster-*****</ClusterId>
 <Ip>10.25.XX.XX</Ip>
 <WhiteList>[&quot;192.168.XX.XX&quot;,&quot;172.16.XX.XX&quot;]</WhiteList>
 <VswitchId>vsw-ke7j6p4za4lwtjrju****</VswitchId>
 <ZoneNo>cn-qingdao-env***-amtest***-a</ZoneNo>
 <Remark>testInstance</Remark>
 <ShowCreateCluster>true</ShowCreateCluster>
 <HsmStatus>5</HsmStatus>
 <VpcId>vpc-ke7kj03hq3es7luti****</VpcId>
 <VsmType>evsm</VsmType>
 <IsMaster>1</IsMaster>
 <VendorCode>jnta</VendorCode>
 <ClusterName>testCluster</ClusterName>
 <RegionId>cn-neimeng-*****-d01</RegionId>
</Instances> <TotalCount>5</TotalCount> <RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId> <PageSize>15</PageSize> <CurrentPage>1</CurrentPage>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DescribeInstanceStock

查询密码机实例的是否有可用库存。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| RegionId | Strin g | Query | 是 | cn-neimeng-*****-d01 | 密码机实例所在地域的编号。 说明 ：您可以调用DescribeRegions 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |
| HasStock | Boolean | true | 是否有库存。取值： true ：是。 false ：否。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeInstanceStock &RegionId=cn-neimeng-*****-d01
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "HasStock":true
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId> <HasStock>true</HasStock>
```

加密服务

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |

### DescribeZones

获取可用区数据集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| RegionId | Strin g | Query | 是 | cn-neimeng-*****-d01 | 可用区所属地域的编号。 说明 ：您可以调用DescribeRegions 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Zones | Array |  | 可用区数据集。 |
| -ZoneNo | String | cn-qingdao-env***- amtest***-a | 可用区编号。 |
| -IsMaster | Integer | 1 | 是否是主可用区。取值： 1 ：是。 0 ：否。 |

加密服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "Zones":[{
  "IsMaster":1,
  "ZoneNo":"cn-qingdao-env***-amtest***-a"
 }]
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId> <Zones>
 <IsMaster>1</IsMaster>
 <ZoneNo>cn-qingdao-env***-amtest***-a
 </ZoneNo>
</Zones>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |

### DescribeVsmTypes

获取密码机设备的设备类型数据集。 只查询有密码机库存的设备类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| ZoneNo | Strin g | Query | 否 | cn-qingdao-env***- amtest***-a | 密码机设备所在的可用区编号。 说明 ：您可以调用DescribeZones 接口获取该参数。 |
| VendorCo de | Strin g | Query | 否 | jnta | 密码机设备的设备厂商编号。 说明 ：您可以调用DescribeVendors 接口获取该参数。 |
| ProductCo de | Strin g | Query | 否 | jnta.SJJ**** | 密码机设备的设备型号编号。 说明 ：您可以调用DescribeProducts 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| VsmTypes | Array |  | 密码机设备的设备类型数据集。 |
| -Code | String | evsm | 设备类型编码。取值： evsm ：金融数据密码机。 gvsm ：通用服务器密码机。 svsm ：签名验签服务器密码机。 |
| -Stock | Integer | 3 | 当前设备类型下的密码机可用的库存数量。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例加密服务 &公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "VsmTypes":{
  "Code":"evsm",
  "Stock":3
 },
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<VsmTypes>
 <Code>evsm</Code>
 <Stock>3</Stock>
</VsmTypes> <RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### CreateCluster

创建密码机实例集群。 创建集群时所使用的密码机将被定义为该集群的主密码机。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |

| 开发指南·API参 | 考 |  |  |  | 加密服务 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| ClusterNa me | Strin g | Query | 是 | testCluster***** | 用户自定义的集群名称。 |
| IpWhiteLis t | Strin g | Query | 否 | 192.168.XX.XX,192.168. XX.XX | 集群白名单。支持配置多个值，可以使用“,”分隔。 |
| MasterInst anceId | Strin g | Query | 是 | hsm-0k121E5c3**** | 主密码机实例ID。 说明 ：您可以调用DescribeInstances 获取获取该参数。 |
| VpcId | Strin g | Query | 是 | vpc- ke7kj03hq3es7luti**** | 集群的VPC实例ID。 说明 ：您可以调用DescribeVpc 获取该参数。 |
| VSwitchId s | Strin g | Query | 是 | vsw- ke7j6p4za4lwtjrju****,vs w- hy5t6e9q9456qtypow*** * | 集群中的交换机ID集合。 说明 ：您可以调用DescribeVpc 接口获取该参数。创建多可用区的集群时，集合的第一个下标位置需设置为主密码机所在的可用区下的交换机ID，其余交换机信息须与参数ZoneNos 中设置的可用区一一对应。 |
| ZoneNos | Strin g | Query | 是 | cn-qingdao-env***- amtest***-a,cn-qingdao- env***-amtest***-b | 集群的可用区编号集合。 说明 ：您可以调用DescribeZones 接口获取该参数。创建多可用区的集群时，集合的第一个下标位置需设置为主密码机所在的可用区，其余可用区信息顺位设置即可。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

| 加密服务 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ClusterId | String | cluster-***** | 集群ID，集群唯一标识。 |

**示例**

请求示例

```
&ClusterName=testCluster***** &MasterInstanceId=hsm-0k121E5c3**** &VpcId=vpc-ke7kj03hq3es7luti**** &VSwitchIds=vsw-ke7j6p4za4lwtjrju****,vsw-hy5t6e9q9456qtypow**** &ZoneNos=cn-hangzhou-env212-a*****,cn-hangzhou-env212-b*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "ClusterId":"cluster-*****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId> <ClusterId>cluster-*****</ClusterId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 400 | -1002 | ParamsInvalid | The param %s is invalid, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 400 | -2001 | StatusInvalid | Device channel status is invalid, place check the device channel status |
| 500 | -2002 | ConfigIpError | Failed to configure VPC IP for instance, please contact the administrator to check vpc tunnel |

| 开发指南·API参 | 考 |  | 加密服务 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -2003 | WhiteListInvalid | The param whiteList is invalid, please check it again |
| 500 | -3001 | VpcServerError | Vpc server is error, operation data failed, please contact the administrator to check vpc service |
| 500 | -3002 | VpcClientError | Vpc client is error, operation data failed, please contact the administrator to check vpc client |
| 500 | -3004 | ResultError | Failed to request HSM device result. please contact the administrator to check the device status |
| 500 | -3005 | HsmCallError | Unable to connect to the HSM device, please contact the administrator to check the device status and network information |
| 500 | -3006 | SlbCallError | Slb call is error, operation data failed, please contact the administrator to check slb client |
| 400 | -3009 | SlbResultError | Slb result is error, operation data failed, please contact the administrator to check slb client |
| 400 | -4002 | ClusterNameExist | The clusterName is already exist, please replace it |
| 500 | -4003 | SetSizeNotEqual | The set size of vSwitch and zoneNo are not equal |
| 500 | -4004 | ClusterProcessNotSupport | The device model is not support cluster process |
| 500 | -4008 | VSwitchNotEqual | The vSwitch %s of instance is not equals to cluster, please check them and try again |
| 500 | -4014 | ClusterAddHsmEmpty | The set hsm instance to be extended in the cluster is empty |
| 500 | -4029 | ZoneNotExist | The zoneNo %s of instance does not exist in the cluster |
| 500 | -4030 | ZoneDuplicate | The entered parameter value of zoneNo %s is duplicate |

加密服务

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -4031 | VSwitchDuplicate | The entered parameter value of vSwitch %s is duplicate |
| 500 | -4035 | VswitchChangeError | The vswitch of master instance is not allowed to change |
| 500 | -4036 | ClusterInfoIncorrect | The number of cluster nodes in the cluster info of instance is incorrect |
| 500 | -5001 | InstanceInOperation | The current instance %S is being operated on, please try again later |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DeleteCluster

删除密码机实例集群。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| ClusterId | Strin g | Query | 是 | cluster-***** | 集群ID，集群唯一标识。 说明 ：您可以调用DescribeClusters 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

加密服务

**示例**

请求示例

```
&ClusterId=cluster-*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId": "04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 400 | -4001 | ClusterNotEmpty | The cluster is not empty, please remove other instances except master instance |
| 500 | -4025 | ClusterLocked | The cluster is locked and cannot be operated. please wait for unlocking and try again |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DescribeClusterInstances

获取密码机集群相关的密码机实例数据集。 该接口有两个用法： 获取用于创建集群的主密码机实例数据集。 获取用于集群扩缩容的子密码机实例数据集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| ClusterId | Strin g | Query | 否 | cluster-***** | 集群ID，集群唯一标识。 如果查询主密码机实例数据集，此参数无效。 如果查询子密码机实例数据集，此参数须必传。 说明 ：您可以调用DescribeClusters 接口获取该参数。 |
| Ip | Strin g | Query | 否 | 192.168.XX.XX | 子密码机实例所注册的经典网络IP地址。 如果查询主密码机实例数据集，此参数无效。 如果查询子密码机实例数据集，此参数非必传，传值时查询指定IP地址的子密码机实例。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |
| ZoneNo | Strin g | Query | 否 | cn-qingdao-env***- amtest***-a | 子密码机实例所在可用区编号。 如果查询主密码机实例数据集，此参数无效。 如果查询子密码机实例数据集，此参数非必传。不传值时默认查询当前集群中可用区下的子密码机实例数据集。 说明 ：您可以调用DescribeZones 接口获取该参数。 |
| IsMasterIn stance | Boole an | Query | 是 | false | 是否查询主密码机实例数据集。取值： true ：是。 false ：否。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 否 | hsm-0k121E5c3**** | 密码机实例ID。 如果查询主密码机实例数据集，此时查询指定的主密码机实例。 如果查询子密码机实例数据集，此时查询指定的子密码机实例。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |
| BelongTyp e | Integ er | Query | 否 | 1 | 集群扩缩容的操作类型，默认值为1。取值： 1 ：扩容。 2 ：缩容。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Instances | Array |  | 主密码机实例/子密码机实例数据集。 |
| -WhiteList | Normal | ["192.168.XX.XX"," 192.168.XX.XX"] | 密码机实例的白名单IP数组。 说明 ：如果当前实例有所属集群，则白名单与集群白名单保持一致。 |
| -InstanceId | String | hsm- 0k121E5c3**** | 密码机实例ID。 |
| -RegionId | String | cn-neimeng-*****- d01 | 密码机实例所在地域编号。 |
| -HsmStatus | Integer | 5 | 密码机实例状态。取值： 1 ：未初始化。 3 ：已释放。 4 ：生产失败。 5 ：运行中。 6 ：:同步中。 7 ：重置中。 8 ：已停用。 |
| -VpcId | String | vpc- ke7kj03hq3es7luti* *** | 密码机实例的VPC实例ID。 |
| -VswitchId | String | vsw- ke7j6p4za4lwtjrju* *** | 密码机实例的交换机ID。 |

| 加密服务 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Ip | String | 10.125.XX.XX | 密码机实例所以设备的真实IP地址。 |
| -Remark | String | testInstance | 密码机实例的别名。 |
| -VendorName | String | 江南天安 | 密码机实例所用设备的设备厂商名称。 |
| -VendorCode | String | jnta | 密码机实例所用设备的设备厂商编码。 |
| -ProductName | String | 江南天安云密码机 | 密码机实例所用设备的设备型号名称。 |
| -ProductCode | String | jnta.SJJ**** | 密码机实例所用设备的设备型号编码。 |
| -VsmType | String | evsm | 密码机实例的设备类型。取值： evsm ：金融数据密码机。 gvsm ：通用服务器密码机。 svsm ：签名验签服务器密码机。 |
| -VpcIp | String | 192.168.XX.XX | 密码机实例对应的经典网络的IP地址。 |
| -ClusterId | String | cluster-***** | 密码机实例所在集群的ID。 |
| -ClusterName | String | testCluster | 密码机实例所在集群的名称。 |
| -IsMaster | Integer | 1 | 当前密码机在集群中是否是主密码机。取值： 0 ：不是。 1 ：是。 |
| -ZoneNo | String | cn-qingdao-env***- amtest***-a | 密码机实例所在的可用区编号。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeClusterInstances &IsMasterInstance=false
```

&公共请求参数正常返回示例加密服务 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "Instances":[{
  "VpcIp":"192.168.XX.XX",
```

`"VendorName":"`江南天安`",` `"ProductName":"`江南天安云密码机`",`

```json
  "InstanceId":"hsm-0k121E5c3****",
  "ProductCode":"jnta.SJJ****",
  "ClusterId":"cluster-*****",
  "Ip":"10.125.XX.XX",
  "WhiteList":"[\"192.168.XX.XX\",\"192.168.XX.XX\"]",
  "VswitchId":"vsw-ke7j6p4za4lwtjrju****",
  "ZoneNo":"cn-qingdao-env***-amtest***-a",
  "Remark":"testInstance",
  "HsmStatus":5,
  "VpcId":"vpc-ke7kj03hq3es7luti****",
  "VsmType":"evsm",
  "IsMaster":1,
  "VendorCode":"jnta",
  "ClusterName":"testCluster",
  "RegionId":"cn-neimeng-*****-d01"
 }],
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式加密服务

```xml
<Instances>
 <VpcIp>192.168.XX.XX</VpcIp>
 <VendorName>江南天安</VendorName>
```

`<ProductName>`江南天安云密码机`</ProductName>`

```xml
 <InstanceId>hsm-0k121E5c3****</InstanceId>
 <ProductCode>jnta.SJJ****</ProductCode>
 <ClusterId>cluster-*****</ClusterId>
 <Ip>10.125.XX.XX</Ip>
 <WhiteList>[&quot;192.168.XX.XX&quot;,&quot;192.168.XX.XX&quot;]</WhiteList>
 <VswitchId>vsw-ke7j6p4za4lwtjrju****</VswitchId>
 <ZoneNo>cn-qingdao-env***-amtest***-a</ZoneNo>
 <Remark>testInstance</Remark>
 <HsmStatus>5</HsmStatus>
 <VpcId>vpc-ke7kj03hq3es7luti****
 </VpcId>
 <VsmType>evsm</VsmType>
 <IsMaster>1</IsMaster>
 <VendorCode>jnta</VendorCode>
 <ClusterName>testCluster</ClusterName>
 <RegionId>cn-neimeng-*****-d01
 </RegionId>
</Instances> <RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 500 | -4038 | CLusterWhiteListError | Unable to obtain data for built- in cluster whiteList, please contact the administrator for troubleshooting |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DescribeClusters

获取密码机集群。 该接口有两个用法： 获取单个密码机集群的详情。 获取所有密码机集群的数据集。

**请求头**

加密服务该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| PageSize | Integ er | Query | 否 | 15 | 分页查询时，指定每页最多显示的数据条数。 说明 ：如果查询单个密码机集群的详情，此参数无效。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 分页查询时，设置当前页面的页码。 **说明：**如果查询单个密码机集群的详情，此参数无效。 |
| ClusterId | Strin g | Query | 否 | cluster-***** | 集群ID，集群唯一标识。 说明 ：如果查询所有密码机集群的数据，此参数无效。您可以调用DescribeClusters 接口获取该参数。 |
| VendorCo de | Strin g | Query | 否 | jnta | 密码机实例所用设备的设备厂商编码。 说明 ：如果查询单个密码机集群的详情，此参数无效。您可以调用DescribeVendors 接口获取该参数。 |
| ProductCo de | Strin g | Query | 否 | jnta.SJJ**** | 密码机实例所用设备的设备型号编码。 说明 ：如果查询单个密码机集群的详情，此参数无效。您可以调用DescribeProducts 接口获取该参数。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterNa me | Strin g | Query | 否 | testCluster | 集群名称。 说明 ：如果查询单个密码机集群的详情，此参数无效。您可以调用DescribeClusters 接口获取该参数。 |
| VsmType | Strin g | Query | 否 | evsm | 集群中主密码机实例的设备类型，也可标识为整个集群的密码机实例的设备类型。 取值： evsm ：金融数据密码机。 gvsm ：通用服务器密码机。 svsm ：签名验签服务器密码机。 说明 ：如果查询单个密码机集群的详情，此参数无效。 |
| ClusterSta tus | Strin g | Query | 否 | 2 | 密码机集群状态。取值： 0 ：未初始化。 1 ：初始化中。 2 ：已启用。 3 ：同步中。 4 ：已删除。 5 ：异常。 说明 ：如果查询单个密码机集群的详情，此参数无效。 |
| IsAllResult | Boole an | Query | 否 | true | 是否获取全部集群。取值： true ：是。 false ：否。 说明 ：取值为是时，获取的是所有集群数据；取值为否时，获取的是按照分页指定的每页数量的集群数据集。如果查询单个密码机集群的详情，此参数无效。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HsmClusters | Array |  | 集群数据集。 |

|  | 开发指南·API参考 |  |  | 加密服务 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - HsmClusterIte ms | Array |  | 集群中子项数据集，每个子项即为密码机实例。 |
| --Id | Long | 1 | 集群中子项的主键ID。 |
| --ClusterId | String | cluster-***** | 密码机实例所在集群的ID。 |
| --InstanceId | String | hsm- 0k121E5c3**** | 密码机实例ID。 |
| --Status | Integer | 5 | 密码机实例状态。取值： **1：**未初始化。 **3：**已释放。 **4：**生产失败。 **5：**运行中。 **6：**同步中。 **7：**重置中。 **8：**已停用。 |
| --IsMaster | Integer | 0 | 当前密码机是否是集群的主密码机。 |
| --ZoneNo | String | cn-qingdao-env***- amtest***-a | 密码机实例所在的可用区编号。 |
| --Ip | String | 192.168.XX.XX | 密码机实例所注册的经典网络IP地址。 |
| --VsmType | String | evsm | 密码机实例的设备类型。取值： **evsm：**金融数据密码机。 **gvsm：**通用服务器密码机。 **svsm：**签名验签服务器密码机。 |
| -ClusterZones | Array |  | 集群下属的可用区与交换机的数据集。每个交换机只属于一个可用区。 |
| --VSwitchId | String | vsw- ke7j6p4za4lwtjrju* *** | 交换机ID。 |
| --ZoneNo | String | cn-qingdao-env***- amtest***-a | 可用区编号。 |
| -ClusterId | String | cluster-***** | 集群ID，集群唯一标识。 |
| -AliUid | Long | 123456789 | 用户标识。 |

| 加密服务 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -VsmType | String | evsm | 集群中主密码机实例的设备类型，此处标识为整个集群的密码机实例的设备类型。取值： evsm ：金融数据密码机。 gvsm ：通用服务器密码机。 svsm ：签名验签服务器密码机。 |
| -ClusterName | String | testCluster | 用户自定义的集群名称。 |
| -ClusterStatus | String | 2 | 集群状态。取值： 0 ：未初始化。 1 ：初始化中。 2 ：已启用。 3 ：同步中。 4 ：已删除。 5 ：异常。 |
| -IpWhiteList | String | 192.168.XX.XX,172 .16.XX.XX. | 集群的白名单IP。 |
| -VpcId | String | vpc- ke7kj03hq3es7luti* *** | 集群的VPC实例ID。 说明 ：每个集群只有一个VPC实例。 |
| -ClusterSize | String | 3 | 集群大小，即集群下属密码机实例的数量。 |
| -ClusterMaster | String | hsm- 0k121E5c3**** | 集群中主密码机实例ID。 |
| -GmtCreate | Long | 1682045208971 | 集群的创建时间。 |
| -MasterIp | String | 192.168.XX.XX | 集群中主密码机实例所注册的经典网络IP地址。 |
| - AbnormalType | String | 3 | 集群异常类型。取值： 3 ：密码机数据不一致。 4 ：所有密码机不可访问。 5 ：密码机数量不一致。 说明 ：只有集群状态异常时，此参数有值，否则为空值。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |
| TotalCount | Long | 3 | 集群数据集的总记录数。 |

| 开发指南·API参考 |  |  | 加密服务 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| CurrentPage | Integer | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Integer | 15 | 分页查询时，指定每页最多显示的数据条数。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式加密服务

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":3,
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "PageSize":15,
 "CurrentPage":1,
 "HsmClusters":[{
  "-ClusterZones":[{
   "VSwitchId":"vsw-ke7j6p4za4lwtjrju****",
   "ZoneNo":"cn-qingdao-env***-amtest***-a"
  }],
  "ClusterId":"cluster-*****",
  "ClusterSize":"3",
  "IpWhiteList":"192.168.XX.XX,172.16.XX.XX.",
  "ClusterMaster":"hsm-0k121E5c3****",
  "AbnormalType":"3",
  "MasterIp":"192.168.XX.XX",
  "GmtCreate":1682045208971,
  "VpcId":"vpc-ke7kj03hq3es7luti****",
  "-HsmClusterItems":[{
   "Status":5,
   "ClusterId":"cluster-*****",
   "InstanceId":"hsm-0k121E5c3****",
   "Ip":"192.168.XX.XX",
   "VsmType":"evsm",
   "IsMaster":0,
   "Id":1,
   "ZoneNo":"cn-qingdao-env***-amtest***-a"
  }],
  "VsmType":"evsm",
  "ClusterName":"testCluster",
  "ClusterStatus":"2",
  "AliUid":123456789
 }]
}
```

`XML` 格式加密服务

```xml
<TotalCount>3</TotalCount> <RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId> <PageSize>15</PageSize> <CurrentPage>1</CurrentPage> <HsmClusters>
 <-ClusterZones>
  <VSwitchId>vsw-ke7j6p4za4lwtjrju****</VSwitchId>
  <ZoneNo>cn-qingdao-env***-amtest***-a
  </ZoneNo>
 </-ClusterZones>
 <ClusterId>cluster-*****
 </ClusterId>
 <ClusterSize>3</ClusterSize>
 <IpWhiteList>192.168.XX.XX,172.16.XX.XX.</IpWhiteList>
 <ClusterMaster>hsm-0k121E5c3****
 </ClusterMaster>
 <AbnormalType>3</AbnormalType>
 <MasterIp>192.168.XX.XX</MasterIp>
 <GmtCreate>1682045208971</GmtCreate>
 <VpcId>vpc-ke7kj03hq3es7luti****
 </VpcId>
 <-HsmClusterItems>
  <Status>5</Status>
  <ClusterId>cluster-*****
  </ClusterId>
  <InstanceId>hsm-0k121E5c3****
  </InstanceId>
  <Ip>192.168.XX.XX</Ip>
  <VsmType>evsm</VsmType>
  <IsMaster>0</IsMaster>
  <Id>1</Id>
  <ZoneNo>cn-qingdao-env***-amtest***-a
  </ZoneNo>
 </-HsmClusterItems>
 <VsmType>evsm</VsmType>
 <ClusterName>testCluster</ClusterName>
 <ClusterStatus>2</ClusterStatus>
 <AliUid>123456789</AliUid>
</HsmClusters>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

加密服务

### ModifyCluster

编辑集群信息。 只支持对集群下的以下内容进行变更： 集群名称。 非主可用区的可用区编号和交换机实例。 集群白名单。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| ClusterId | Strin g | Query | 是 | cluster-***** | 集群ID，集群唯一标识。 说明 ：您可以调用DescribeClusters 接口获取该参数。 |
| IpWhiteLis t | Strin g | Query | 否 | 192.168.XX.XX,172.18.X X.XX | 集群白名单。支持配置多个值，可以使用“,”分隔。 |
| ClusterNa me | Strin g | Query | 是 | testCluster | 用户自定义的集群名称。 |
| Zones | Strin g | Query | 否 | cn-qingdao-env***- amtest***-a,cn-qingdao- env***-amtest***-b | 待变更的可用区编号集合 （不包含主可用区的）。 说明 ：您可以调用DescribeZones 接口获取该参数。创建多可用区的集群时，集合的第一个下标位置需设置为主密码机所在的可用区，其余可用区信息顺位设置即可。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| VSwitchId s | Strin g | Query | 否 | vsw- ke7j6p4za4lwtjrju****,vs w- hy5t6e9q9456qtypow*** * | 待变更的交换机ID集合（不包含主可用区的）。 说明 ：您可以调用DescribeVpc 接口获取该参数。创建多可用区的集群时，集合的第一个下标位置需设置为主密码机所在的可用区下的交换机ID，其余交换机信息须与参数Zones 中设置的可用区一一对应。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&ClusterId=cluster-***** &ClusterName=testCluster
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |

| 加密服务 |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |
| 400 | -1002 | ParamsInvalid | The param %s is invalid, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 400 | -2003 | WhiteListInvalid | The param whiteList is invalid, please check it again |
| 400 | -4002 | ClusterNameExist | The clusterName is already exist, please replace it |
| 500 | -4013 | ClusterZoneExceed | The cluster supports up to two zones |
| 500 | -4032 | MasterZoneExist | The same value zoneNo %s as master instance exists in parameter zones |
| 500 | -4033 | MasterVSwitchExist | The same value vSwitchId %s as master instance exists in parameter vSwitchIds |
| 500 | -4034 | ResourceOccupied | There are usable instances occupying zoneNo and vSwitchId in the cluster |
| 500 | -4037 | ClusterInOperation | The current cluster %s is being operated on, please try again later |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### QuickInit

快速初始化密码机实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | 是 | cluster-***** | 集群ID，集群唯一标识。 说明 ：您可以调用DescribeClusters 接口获取该参数。 |
| Name | Strin g | Query | 是 | tass | 密码机默认的用户名称。 |
| Password | Strin g | Query | 是 | df5et42/dd5 | 用户自定义的密码。 说明 ：改密码将替换修改密码机的原始密码，修改后须使用新的密码方可登录密码机，请妥善保管。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&ClusterId=cluster-***** &Name=tass &Password=df5et42/dd5
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId>
```

**错误码**

加密服务

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 500 | -3004 | ResultError | Failed to request HSM device result. please contact the administrator to check the device status |
| 500 | -3005 | HsmCallError | Unable to connect to the HSM device, please contact the administrator to check the device status and network information |
| 500 | -4004 | ClusterProcessNotSupport | The device model is not support cluster process |
| 500 | -4015 | ProductNotSupportQuickInit | QuickInit is not supported by device model %s of master instance in the cluster |
| 500 | -4016 | QuickInitModifyPwdError | Failed to modify login password when quickly initializing hsm device |
| 500 | -4017 | QuickInitSystemError | Failed to quickly initialize hsm device, please check the hsm device |
| 500 | -4025 | ClusterLocked | The cluster is locked and cannot be operated. please wait for unlocking and try again |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### CreateInstance

开通密码机实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| ProductCo de | Strin g | Query | 是 | jnta.SJJ**** | 密码机实例所用设备的设备型号编号。 说明 ：您可以调用DescribeProducts 接口获取该参数。 |
| RegionId | Strin g | Query | 是 | cn-neimeng-*****-d01 | 密码机实例所在的地域编号。 说明 ：您可以调用DescribeRegions 接口获取该参数。 |
| VendorCo de | Strin g | Query | 是 | jnta | 密码机实例所用设备的设备厂商编号。 说明 ：您可以调用DescribeVendors 接口获取该参数。 |
| VsmType | Strin g | Query | 否 | evsm | 指定开通密码机实例的设备类型，默认值为evsm。取值： evsm ：金融数据密码机。 gvsm ：通用服务器密码机。 svsm ：签名验签服务器密码机。 |
| VsmNum | Integ er | Query | 否 | 2 | 开通密码机实例的数量。 |
| CreateDiff | Boole an | Query | 否 | false | 是否在不同物理加密机开通实例，默认值为true。取值： true ：是。 false ：否。 |
| ZoneNo | Strin g | Query | 否 | cn-qingdao-env***- amtest***-a | 密码机所在的可用区编号。 说明 ：您可以调用DescribeZones 接口获取该参数。 |

加密服务

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| InstanceIds | List | hsm- 0k121E5c3****,hs m-8h6546R2f3**** | 开通密码机实例的ID集合。 说明 ：开通多个时返回实例ID集合，开通一个时此值为空。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |
| InstanceId | String | hsm- 0k121E5c3**** | 开通密码机实例的ID。 说明 ：开通一个时返回实例ID，开通多个时此值为空。 |

**示例**

请求示例

```
&ProductCode=jnta.SJJ**** &RegionId=cn-neimeng-*****-d01 &VendorCode=jnta
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "InstanceId":"hsm-0k121E5c3****",
 "InstanceIds":["hsm-0k121E5c3****,hsm-8h6546R2f3****"]
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId> <InstanceId>hsm-0k121E5c3****</InstanceId> <InstanceIds>hsm-0k121E5c3****,hsm-8h6546R2f3****</InstanceIds>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |

| 开发指南·API参 | 考 |  | 加密服务 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1002 | ParamsInvalid | The param %s is invalid, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 400 | -1004 | ResourceExist | Resource %s is already exist, please check it again |
| 500 | -2005 | UnderStock | Hsm instance resource is not enough，please contact the administrator to add hsm instance resources |
| 500 | -2006 | ConfigToken | Config hsm instance token failed, please contact the administrator to check the device status |
| 500 | -3004 | ResultError | Failed to request HSM device result. please contact the administrator to check the device status |
| 500 | -3005 | HsmCallError | Unable to connect to the HSM device, please contact the administrator to check the device status and network information |
| 500 | -3006 | SlbCallError | Unable to connect to slb service, please contact the administrator to check the SLB service status |
| 500 | -3007 | CloseError | Close hsm connection failed, please contact the administrator to check the device status |
| 400 | -3009 | SlbResultError | Slb result is error, operation data failed, please contact the administrator to check slb client |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DescribeProducts

获取密码机的设备型号数据集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| VendorCo de | Strin g | Query | 是 | jnta | 密码机实例所用设备的设备厂商编码。 说明 ：您可以调用DescribeVendors 接口获取该参数。 |
| RegionId | Strin g | Query | 否 | cn-neimeng-*****-d01 | 密码机实例所在地域的编号。 说明 ：您可以调用DescribeRegions 接口获取该参。如果此参数有值，则查询当前地域下有密码机库存的设备型号数据集。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Products | Array | [{"Code":"jnta.SJJ** **","Name":"江南天安云密码机"}] | 密码机的设备型号数据集。 |
| -Code | String | jnta.SJJ**** | 密码机设备的设备型号编码。 |
| -Name | String | 江南天安云密码机 | 密码机设备的设备型号名称。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&VendorCode=jnta
```

&公共请求参数正常返回示例 `JSON` 格式加密服务

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "Products":[{
  "Code":"jnta.SJJ****",
```

`"Name":"`江南天安云密码机"

```json
 }],
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<Products>
 <Code>jnta.SJJ****</Code>
```

`<Name>`江南天安云密码机`</Name>`

```xml
</Products> <RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |

### ReleaseInstance

释放密码机实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |

| 加密服务 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| InstanceId | Strin g | Query | 是 | hsm-0k121E5c3**** | 密码机实例ID。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&InstanceId=hsm-0k121E5c3****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 400 | -1002 | ParamsInvalid | The param %s is invalid, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |

| 开发指南·API参 | 考 |  | 加密服务 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -3001 | VpcServerError | Vpc server is error, operation data failed, please contact the administrator to check vpc service |
| 500 | -3002 | VpcClientError | Vpc client is error, operation data failed, please contact the administrator to check vpc client |
| 500 | -3006 | SlbCallError | Slb call is error, operation data failed, please contact the administrator to check slb client |
| 400 | -3009 | SlbResultError | Slb result is error, operation data failed, please contact the administrator to check slb client |
| 500 | -4020 | InstanceExistInCluster | Hsm instance is already in cluster %s, please remove it from cluster first and try again |
| 500 | -5003 | InstanceInReleaseProtection | Hsm instance has already open release protection, please contact the administrator to close and try again |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DescribeRegions

获取地域数据集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |

**返回数据**

加密服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Regions | Array |  | 地域数据集。 |
| -RegionName | String | cn-neimeng-*****- d01 | 地域名称。 |
| -RegionId | String | cn-neimeng-*****- d01 | 地域编号。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "Regions":[{
  "RegionName":"cn-neimeng-*****-d01",
  "RegionId":"cn-neimeng-*****-d01"
 }]
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId> <Regions>
 <RegionName>cn-neimeng-*****-d01
 </RegionName>
 <RegionId>cn-neimeng-*****-d01
 </RegionId>
</Regions>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

加密服务

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DescribeVendors

获取设备厂商数据集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| PageSize | Integ er | Query | 否 | 15 | 分页查询时，指定每页最多显示的数据条数。 |
| CurrentPa ge | Integ er | Query | 否 | 1 | 分页查询时，设置当前页面的页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Vendors | Array | [{"Code":"jnta","Na me":"江南天安"}] | 设备厂商数据集。 |
| -Code | String | jnta | 设备厂商编码。 |
| -Name | String | 江南天安 | 设备厂商名称。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例加密服务 &公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "Vendors":[{
  "Code":"jnta",
```

`"Name":"`江南天安"

```
 }]
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId> <Vendors>
 <Code>jnta</Code>
```

`<Name>`江南天安`</Name>`

```
</Vendors>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |
| 500 | -1005 | GetVendorsError | System error, get init vendor data failed. please contact the administrator for troubleshooting |

### DescribeVpc

获取VPC实例数据集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |

| 开发指南·API参 | 考 |  |  |  | 加密服务 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| RegionId | Strin g | Query | 是 | cn-neimeng-*****-d01 | VPC实例所在的地域编号。 说明 ：您可以调用DescribeRegions 接口获取该参数。 |
| ZoneNo | Strin g | Query | 否 | cn-qingdao-env***- amtest***-a | VPC实例下的交换机所在的可用区编号。 说明 ：您可以调用DescribeZones 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| VpcInstances | Array |  | VPC实例数据集。 |
| -VSwitches | Array |  | VPC实例下的交换机数据集。 |
| --InstanceId | String | vsw- ke7j6p4za4lwtjrju* *** | 交换机实例ID。 |
| --ZoneNo | String | cn-qingdao-env***- amtest***-a | 交换机所在可用区编号。 |
| --CidrBlock | String | 172.18.XX.XX0/26 | 交换机实例的网段。 |
| -InstanceId | String | vpc- ke7kj03hq3es7luti* *** | VPC实例ID。 |
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&RegionId=cn-neimeng-*****-d01
```

&公共请求参数加密服务正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "VpcInstances":[{
  "-VSwitches":[{
   "InstanceId":"vsw-ke7j6p4za4lwtjrju****",
   "CidrBlock":"172.18.XX.XX0/26",
   "ZoneNo":"cn-qingdao-env***-amtest***-a"
  }],
  "InstanceId":"vpc-ke7kj03hq3es7luti****"
 }]
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId> <VpcInstances>
 <-VSwitches>
  <InstanceId>vsw-ke7j6p4za4lwtjrju****
  </InstanceId>
  <CidrBlock>172.18.XX.XX0/26</CidrBlock>
  <ZoneNo>cn-qingdao-env***-amtest***-a
  </ZoneNo>
 </-VSwitches>
 <InstanceId>vpc-ke7kj03hq3es7luti****
 </InstanceId>
</VpcInstances>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -3001 | VpcServerError | Vpc server is error, operation data failed, please contact the administrator to check vpc service |
| 500 | -3002 | VpcClientError | Vpc client is error, operation data failed, please contact the administrator to check vpc client |
| 500 | -3003 | VpcEndpointError | Vpc endpoint is error, please contact the administrator for troubleshooting |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

加密服务

### ModifyInstance

编辑密码机实例。 可变更内容仅包含密码机实例的别名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| InstanceId | Strin g | Query | 是 | hsm-0k121E5c3**** | 密码机实例ID。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |
| Remark | Strin g | Query | 是 | testInstance | 密码机实例别名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&InstanceId=hsm-0k121E5c3**** &Remark=testInstance
```

&公共请求参数正常返回示例 `JSON` 格式加密服务

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 500 | -5001 | InstanceInOperation | The current instance %S is being operated on, please try again later |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### AddHsmToCluster

向集群中扩容密码机实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | 是 | cluster-***** | 集群ID，集群的唯一标识。 说明 ：您可以调用DescribeClusters 接口获取该参数。 |
| HsmInsta nceIds | Strin g | Query | 是 | hsm- 0k121E5c3****,hsm- sr132G5b9**** | 待扩容的密码机实例ID。支持同时扩容多个实例，多值时可使用“,”分隔。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&ClusterId=cluster-***** &HsmInstanceIds=hsm-0k121E5c3****,hsm-sr132G5b9****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |

| 加密服务 |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 400 | -2001 | StatusInvalid | The status of instance to be expanded is not uninitialized, you are not allowed to join the cluster |
| 500 | -2002 | ConfigIpError | Failed to automatically configure ip for instance, please check if vSwitch is correct |
| 500 | -3004 | ResultError | Failed to request HSM device result. please contact the administrator to check the device status |
| 500 | -3005 | HsmCallError | Unable to connect to the HSM device, please contact the administrator to check the device status and network information |
| 500 | -4005 | ClusterAddHsmError | The empty cluster can only add a master instance for the first time, please select again |
| 400 | -4006 | ClusterStatusInvalid | The status of cluster is not enabled, it's not support to expand |
| 500 | -4007 | MasterNodeStatusInvalid | The status of cluster master node device is not active, please activate the device first |
| 500 | -4008 | VSwitchNotEqual | The vSwitch %s of instance is not equals to cluster, please check them and try again |
| 500 | -4009 | ClusterNodeNotEqualDb | The number of cluster nodes in hsm device is not equals to that in the database |
| 500 | -4010 | NumOfHsmInstanceExceed | The number of hsm instance in cluster is exceed |
| 500 | -4011 | VsmClusterInfoError | Failed to obtain cluster device information, the result of device %s is null |
| 500 | -4012 | InstanceZoneExceed | The cluster already uses an instance with two zones. you cannot add another %s |
| 500 | -4013 | ClusterZoneExceed | The cluster supports up to two zones |

| 开发指南·API参 | 考 |  | 加密服务 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -4014 | ClusterAddHsmEmpty | The set hsm instance to be extended in the cluster is empty |
| 400 | -4020 | InstanceExistInCluster | The instance is already exist in cluster %s, please select again |
| 500 | -4021 | RegionNotEqual | The region %s of instance is not equals to cluster, please check them and try again |
| 500 | -4022 | VendorNotEqual | The device vendor %s of instance in the cluster is inconsistent, please check them and try again |
| 500 | -4023 | ProductNotEqual | The device model %s of instance in the cluster is inconsistent, please check them and try again |
| 500 | -4024 | DeviceTypeNotEqual | The device type %s of instance in the cluster is inconsistent, please check them and try again |
| 500 | -4025 | ClusterLocked | The cluster is locked and cannot be operated. please wait for unlocking and try again |
| 500 | -4027 | VpcNotEqual | The vpc %s of instance is not equals to cluster, please check them and try again |
| 500 | -4028 | InitializedAlready | The instance %s is initialized and cannot join the cluster |
| 500 | -4029 | ZoneNotExist | The zoneNo %s of instance does not exist in the cluster |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### DescribeQuickInitInfo

获取密码机的初始化信息。 初始化信息包括：集群信息和密码机的默认用户名称。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| ClusterId | Strin g | Query | 是 | cluster-***** | 集群ID，集群唯一标识。 说明 ：您可以调用DescribeClusters 接口获取该参数。 |
| InstanceId | Strin g | Query | 是 | hsm-0k121E5c3**** | 密码机实例ID。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |
| ClusterId | String | cluster-***** | 集群ID，集群唯一标识。 |
| ClusterName | String | testCluster | 用户自定义的集群名称。 |
| AdminName | String | tass | 密码机默认的用户名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeQuickInitInfo &ClusterId=cluster-***** &InstanceId=hsm-0k121E5c3****
```

&公共请求参数正常返回示例 `JSON` 格式加密服务

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****",
 "ClusterId":"cluster-*****",
 "AdminName":"tass",
 "ClusterName":"testCluster"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId> <ClusterId>cluster-*****</ClusterId> <AdminName>tass</AdminName> <ClusterName>testCluster</ClusterName>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -4026 | ClusterNotFound | The current cluster does not exist or has been deleted |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### RemoveHsmFromCluster

集群缩容。 从集群中移除密码机实例，减少集群容量。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | 是 | cluster-***** | 集群ID，集群唯一标识。 说明 ：您可以调用DescribeClusters 接口获取该参数。 |
| HsmInsta nceIds | Strin g | Query | 是 | hsm- 0k121E5c3****,hsm- 5g256r6v8**** | 待缩容的密码机实例。支持缩容多台密码机实例，多值时使用“,”分隔。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveHsmFromCluster &ClusterId=cluster-***** &HsmInstanceIds=hsm-0k121E5c3****,hsm-5g256r6v8****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7**** </RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

加密服务

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 500 | -3004 | ResultError | Failed to request HSM device result. please contact the administrator to check the device status |
| 500 | -3005 | HsmCallError | Unable to connect to the HSM device, please contact the administrator to check the device status and network information |
| 400 | -4006 | ClusterStatusInvalid | The status of cluster is not enabled, it's not support to expand |
| 500 | -4009 | ClusterNodeNotEqualDb | The number of cluster nodes in hsm device is not equals to that in the database |
| 500 | -4011 | VsmClusterInfoError | Failed to obtain cluster device information, the result of device %s is null |
| 500 | -4018 | RemoveMasterNotAllowed | It is not allowed to remove master instance %s in the cluster |
| 500 | -4019 | ClusterNodeNotFound | The cluster node in the database is not found in hsm device |
| 500 | -4025 | ClusterLocked | The cluster is locked and cannot be operated. please wait for unlocking and try again |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### ConfigNetwork

对VSM实例进行网络配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

加密服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Resource OwnerId | Long | Query | 否 |  |  |
| InstanceId | Strin g | Query | 是 | hsm-0k121E5c3**** | 密码机实例ID。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |
| VSwitchId | Strin g | Query | 是 | vsw- ke7j6p4za4lwtjrju**** | 交换机ID。 说明 ：您可以调用DescribeVpc 接口获取该参数。 |
| Ip | Strin g | Query | 否 | 192.168.XX.XX | 密码机实例对应的经典网络的IP。不传该参数时，系统将根据VPC和VSWITCH自动分配一个可用IP。 |
| VpcId | Strin g | Query | 是 | vpc- ke7kj03hq3es7luti**** | VPC实例ID。 说明 ：您可以调用DescribeVpc 接口获取该参数。 |
| WhiteList | Strin g | Query | 否 | 192.168.XX.XX,192.168. XX.XX | 可访问密码机实例的白名单 IP。支持配置多个值，可以使用“,”分隔。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&InstanceId=hsm-0k121E5c3**** &VSwitchId=vsw-ke7j6p4za4lwtjrju**** &VpcId=vpc-ke7kj03hq3es7luti****
```

&公共请求参数正常返回示例加密服务 `JSON` 格式

```json
{
 "RequestId": "04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 400 | -1002 | ParamsInvalid | The param %s is invalid, please check it again |
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 400 | -2001 | StatusInvalid | Device channel status is invalid, place check the device channel status |
| 500 | -2002 | ConfigIpError | Failed to configure VPC IP for instance, please contact the administrator to check vpc tunnel |
| 500 | -2008 | VsmStatusInvalid | Hsm instance access exception, please contact the administrator to check the status of device |
| 500 | -3001 | VpcServerError | Vpc server is error, operation data failed, please contact the administrator to check vpc service |
| 500 | -3002 | VpcClientError | Vpc client is error, operation data failed, please contact the administrator to check vpc client |
| 500 | -3003 | VpcEndpointError | Vpc endpoint is error, please contact the administrator for troubleshooting |
| 500 | -3005 | HsmCallError | Unable to connect to the HSM device, please contact the administrator to check the device status and network information |

加密服务

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -3006 | SlbCallError | Slb call is error, operation data failed, please contact the administrator to check slb client |
| 400 | -3008 | VpcIpInUsed | The specified IPAddress is already used by other resource, please change it and try again |
| 400 | -3009 | SlbResultError | Slb result is error, operation data failed, please contact the administrator to check slb client |
| 500 | -4020 | InstanceExistInCluster | Hsm instance is already in cluster %s, modifying vpc is not allowed here |
| 500 | -5001 | InstanceInOperation | The current instance %S is being operated on, please try again later |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

### ConfigWhiteList

配置密码机实例的白名单IP。 通过此接口仅配置密码机实例的白名单信息。v3.18.0版本开始，配置白名单的功能已合并至密码机网络配置的功能中（ConfigVpc接口）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | 否 | 192.168.XX.XX | 来源IP。 |
| Lang | Strin g | Query | 否 | zh | 指定请求和接受消息的语言类型。取值： zh ：中文。 en ：英文。 |
| InstanceId | Strin g | Query | 是 | hsm-0k121E5c3**** | 密码机实例ID。 说明 ：您可以调用DescribeInstances 接口获取该参数。 |

| 开发指南·API参 | 考 |  |  |  | 加密服务 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

| WhiteList | Strin g | Query | 是 | 192.168.XX.XX,192.168. XX.XX | 可访问密码机实例的白名单 IP。支持配置多个值，可以使用“,”分隔。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 04F0F334-1335- 436C-A1D7- 6C044FE7**** | 本次接口调用的请求ID。 |

**示例**

请求示例

```
&InstanceId=hsm-0k121E5c3**** &WhiteList=192.168.XX.XX,192.168.XX.XX
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"04F0F334-1335-436C-A1D7-6C044FE7****"
}
```

`XML` 格式

```xml
<RequestId>04F0F334-1335-436C-A1D7-6C044FE7****</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | ParamsEmpty | The param %s is empty, please check it again |
| 400 | -1002 | ParamsInvalid | The param %s is invalid, please check it again |

| 加密服务 |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | -1003 | ResourceNotExist | Resource %s is not exist, please check it again |
| 400 | -2001 | StatusInvalid | Device channel status is invalid, place check the device channel status |
| 400 | -2003 | WhiteListInvalid | The param whiteList is invalid, please check it again |
| 400 | -2004 | WhiteListOversize | The param whiteList's length is oversize, please shorten it and try again |
| 400 | -4020 | InstanceExistInCluster | The instance is already exist in cluster %s, modifying whiteList is not allowed here |
| 500 | -5001 | InstanceInOperation | The current instance %S is being operated on, please try again later |
| 500 | -1 | SystemError | System is error, please contact the administrator for troubleshooting |

加密服务

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

加密服务

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

加密服务

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

表 4. 安骑士错误代码加密服务

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

加密服务

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

加密服务

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

加密服务

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

| 加密服务 |  | 开发指南·错误代码表 |
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

加密服务

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

加密服务

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

加密服务

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

加密服务

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

加密服务

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

加密服务

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

加密服务

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

加密服务

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

加密服务

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

加密服务

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

加密服务

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

加密服务

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
