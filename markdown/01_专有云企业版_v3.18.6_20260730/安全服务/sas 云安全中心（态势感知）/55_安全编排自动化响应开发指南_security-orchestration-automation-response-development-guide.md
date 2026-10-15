---
title: "云安全中心（态势感知） 安全编排自动化响应开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 76
source_pdf: "55_安全编排自动化响应开发指南_security-orchestration-automation-response-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sas/zh/security-orchestration-automation-response-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云安全中心（态势感知） 安全编排自动化响应开发指南

门

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
门
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍如何通过POP网关调用专有云API。

**流程图**

**调用步骤**

1. 获取AccessKey。
门获取调用时所需要的AccessKey参数，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganiza tionList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResour ceGroup章节。

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织 ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参见开发文档使用说明。
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
作

## 准备工作

### 登录开发者门户控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器

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

### 查看API信息

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本，在通过 SDK调用API接口时需要填写上述信息。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。 作

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏单击
图标，进入**帮助与开放平台**。
3. 在顶部菜单栏**产品文档**的下拉列表中，选择**API****调试**。
4. 在左侧导航栏中选择目标云产品。在下方API列表中可浏览当前API版本中的所有API接口名称。若当前云产品
存在多个API版本，可在**版本**下拉列表中，选择目标API版本。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。 其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参见获取STS AccessKey。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

作

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
作

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourAccessKeyID>：请替换为您实际的AccessKey ID。 <yourAccessKeySecret>：请替换为您实际的AccessKey Secret。 <yourRoleSessionName>：请替换为您当前实际的会话名称。 该名称为用户自定义，通常设置为调用该API的用户身份，例如：用户名。在同一个RAM角色执行的操作中，可以根据不同的 `RoleSessionName` 来区分实际操作者，以实现用户级别的访问审计。长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-）和下划线（_）。 <yourRoleArn>：请替换为您实际的RAM Role。 "sts.aliyuns.com" ：请替换为实际的STS Endpoint。 作

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
作

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

本文介绍如何获取云盾各产品的Endpoint。 作

**背景信息**

通过POP网关调用API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。您也可以

**操作步骤**

1. 登录飞天基础运维平台。
2. 在顶部菜单栏，选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在左侧导航栏，单击**产品集群运维**。
4. 在**产品** | **集群**搜索框输入sas-securityorchautoresponsecluster，点击**集群详情**。
5. 在集群详情切换到资源详情页，搜索soar-pop-biz-endpoint，对应的Json值中domain对应的内容即为业务
域的Endpoint。
6. 云产品的业务域的Endpoint构成格式为：

```
soar-biz.${global:region}.${global:internet-domain}
```

例

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

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your-region-id>，请替换为您实际的地域ID。 <your-access-key-id>，请替换为您实际的AccessKey ID。 <your-access-key-secret>>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您当前产品实际的Endpoint。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。 例

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

例

##### 使用CommonRequest进行调用

**说明**

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
阿里云产品的API有RPC和RESTful两种风格，不同风格的API的CommonRequest的调用方法也不同。 通常API参数中包含Action参数的是RPC风格，包含PathPattern参数的是RESTful风格。一般情况下，每个产品内，所有API的调用风格是统一的。每个API仅支持特定的一种风格调用，传入错误的标识，可能会调用到其他 API，或收到 `ApiNotFound` 的错误信息。 发起一次CommonRequest请求，您需要获取以下几个参数的值。关于以下参数的更多说明，请参见API公共参数。 接入点（endpoint）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 接口信息：要调用的接口名称。 当调用的API为RPC风格（大部分阿里云产品API为RPC风格，如Sas）时，需要获取Action参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 当调用的API为RESTful风格（如容器服务）时，需要获取PathPattern参数，使用 `request.PathPattern` `= "<PathPattern>"` 的方式来指定RESTful路径。

**示例：调用RPC风格的API**

以下代码展示了如何使用CommonRequest的方式调用云盾的接口： 例

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

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体信息，请参如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库： 例

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

本文档介绍如何安装及调用Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。 例使用产品的开发工具包，都必须安装阿里云Python SDK核心库。

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

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
阿里云产品的API有RPC和RESTful两种风格，不同风格的API的CommonRequest的调用方法也不同。 通常API参数中包含Action参数的是RPC风格，包含PathPattern参数的是RESTful风格。一般情况下，每个产品内，所有API的调用风格是统一的。每个API仅支持特定的一种风格调用，传入错误的标识，可能会调用到其他 API，或收到 `ApiNotFound` 的错误信息。 发起一次CommonRequest请求，您需要获取以下几个参数的值。关于以下参数的更多说明，请参见API公共参数。 接入点（endpoint）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 接口信息：要调用的接口名称。 当调用的API为RPC风格（大部分阿里云产品API为RPC风格，如Sas）时，需要获取Action参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 当调用的API为RESTful风格（如容器服务）时，需要获取PathPattern参数，使用 `request.PathPattern` `= "<PathPattern>"` 的方式来指定RESTful路径。

**示例：调用RPC风格的API**

以下代码展示了如何使用CommonRequest的方式调用接口： 例

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

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体信息，请参见获取AccessKey，并在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。

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

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <your_region_id>，请替换为您实际的地域ID。 <your_access_key_id>，请替换为您实际的AccessKey ID。 <your_access_key_secret>，请替换为您实际的AccessKey Secret。 <your-endpoint>，请替换为您实际的产品访问地址。 <API-version>，请替换成接口的版本。 <your-action>，请替换成接口的名称。 例

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

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
阿里云产品的API有RPC和RESTful两种风格，不同风格的API的CommonRequest的调用方法也不同。 例通常API参数中包含Action参数的是RPC风格，包含PathPattern参数的是RESTful风格。一般情况下，每个产品内，所有API的调用风格是统一的。每个API仅支持特定的一种风格调用，传入错误的标识，可能会调用到其他 API，或收到 `ApiNotFound` 的错误信息。 发起一次CommonRequest请求，您需要获取以下几个参数的值。关于以下参数的更多说明，请参见API公共参数。 接入点（endpoint）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 接口信息：要调用的接口名称。 当调用的API为RPC风格（大部分阿里云产品API为RPC风格，如Sas）时，需要获取Action参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 当调用的API为RESTful风格（如容器服务）时，需要获取PathPattern参数，使用 `request.PathPattern` `= "<PathPattern>"` 的方式来指定RESTful路径。

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
    client, err := sdk.NewClientWithAccessKey("cn-hangzhou", "{your_access_key_id}", "{your
_access_key_secret}")
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

共参数

## API公共参数

**公共请求参数**

公共请求参数是每个接口调用都需要提供的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | Strin g | 否 | 返回值的类型，仅支持JSON。 |
| Version | Strin g | 是 | API版本号，以日期形式YYYY-MM-DD输入，取值： 2018-01-16：Auditprivate。 2019-07-23：yundunnextsoc。 2018-12-03：Sas。 2016-11-11：aegis。 2021-10-11：yundun-css。 2019-08-05：secspy。 2018-01-16：Ddosprivate。 2018-06-30：hsm-private。 2017-12-07：Cloudfw。 2019-01-03：Sddp。 2020-07-01：semawaf。 2018-12-03：soar。 |
| AccessKeyId | Strin g | 是 | 访问服务使用的密钥ID。 |
| AccessKeySec ret | Strin g | 是 | 访问服务使用的密钥值。 |
| RegionId | Strin g | 是 | 服务所使用的地域ID。 |

共参数

| Product | Strin g | 是 | 接口对应的产品名称。取值： Auditprivate：云盾基础组件。 yundunnextsoc：云安全管理中心（SOC）。 Sas：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy：网络流量检测与响应。 Ddosprivate：DDos 清洗。 hsm-private：加密服务。 Cloudfw：云防火墙。 Sddp：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |
|---|---|---|---|
| EndpointPre | Strin g | 是 | 接口对应的域名前缀。取值： auditprivate：云盾基础组件。 yundunnextsoc-pop：云安全管理中心（SOC）。 tds：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy-share：网络流量检测与响应。 ddosprivate：DDos 清洗。 hsmprivate：加密服务。 cloudfw：云防火墙。 sddp-api：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码RequestId。

## 剧本

### TriggerPlaybook

调用剧本接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlaybookU uid | String | Query | 否 | bdeaa8bc-a003-4a9a- b37c-249d64a41ba2 | 剧本唯一键ID。 |
| PlaybookN ame | String | Query | 否 | 测试剧本 | 剧本名称。 |
| InputPara m | String | Query | 是 | {"name":"test","ip":"10.1 23.xx.xx"} | 流程调用的触发参数，参数为用户自定义的剧本输入参数。 |
| TriggerTyp e | String | Query | 否 | manual | 触发类型: one： 手工触发。 mul： 定时触发。 strema： 流式触发。 |
| TaskTenan tId | String | Query | 否 | -999999 | 触发剧本增加剧本租户信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0E402C78-34DC- 4B2B-BB15- 73BB914172C1 | 本次调用请求的ID。 |
| RequestUuid | String | a5a60946-3ad4- 4e0d-92db- 500da9619793 | 本次流程执行的唯一ID，可以用来停止流程或者查询结果。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"0E402C78-34DC-4B2B-BB15-73BB914172C1",
 "RequestUuid":"a5a60946-3ad4-4e0d-92db-500da9619793"
}
```

`XML` 格式

```xml
<RequestId>0E402C78-34DC-4B2B-BB15-73BB914172C1 </RequestId> <RequestUuid>a5a60946-3ad4-4e0d-92db-500da9619793 </RequestUuid>
```

### TriggerPlaybookAndWait

调用TriggerPlaybookAndWait接口触发剧本并设置时间等待执行结果。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- soar:TriggerPlaybookAndWait | Write | acs:yundun-soar:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | String | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| PlaybookU uid | String | Query | 否 | 195afca5-****-****-****- a126a173e271 | 剧本唯一标识。 |
| PlaybookN ame | String | Query | 否 | 测试剧本名称。 | 剧本名称。 |
| InputPara m | String | Query | 是 | {"ip":"11.**.**.12"} | 剧本输入信息。 |
| TaskTenan tId | String | Query | 否 | -1 | 任务租户ID。 |
| MaxWaitSe conds | Integ er | Query | 是 |  | 最大等待时间，单位秒。 |
| PageNumb er | Integ er | Query | 是 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1， 表示从第1页开始显示。 |
| PageSize | Integ er | Query | 是 | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20， 表示每页显示20条资产信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SaoExecuteDet ailInfoList | Array |  |  |
| -Content | String | {"tenantId":"2**2"," eventUuid":"cb8fe2 ee-****-****-****- b51a16f42677","ali Uid":"1504*****314" ,"taskId":"6"} | 内容。 |
| -NodeName | String | returnAll | 节点名称。 |
| -ActionUuid | String | 1706237708172 | 节点的唯一标识。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| RequestUuid | String | 53240ac2-****-****- ****-7348c400c0ca | 请求的唯一标识。 |
| PlaybookUuid | String | 195afca5-****-****- a126a173e271 | 剧本的唯一标识。 |
| ResultStatus | String | success | 剧本执行状态： inprogress：处理中。 success：成功。 failed：失败。 |
| ErrorMsg | String |  | 错误信息，状态为错误的时候返回。 |
| PageSize | Integer | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20，表示每页显示20条资产信息。 |
| PageNumber | Integer | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1，表示从第1页开始显示。 |
| TotalCount | Integer | 50 | 查询到的数据的总数量。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TriggerPlaybookAndWait&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&PlaybookUuid=195afca5-****-****-****a126a173e271&PlaybookName=测试剧本名称。&InputParam={"ip":"11.**.**.12"}&TaskTenantId=- 1&MaxWaitSeconds=&PageNumber=1&PageSize=100
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "RequestUuid":"53240ac2-****-****-****-7348c400c0ca",
    "PlaybookUuid":"195afca5-****-****-a126a173e271",
    "ResultStatus":"success",
    "ErrorMsg":"",
    "PageSize":100,
    "PageNumber":1,
    "TotalCount":50,
    "SaoExecuteDetailInfoList":[
        {
            "ActionUuid":"1706237708172",
            "NodeName":"returnAll",
            "Content":"{\"tenantId\":\"2**2\",\"eventUuid\":\"cb8fe2ee-****-****-****-
b51a16f42677\",\"aliUid\":\"1504*****314\",\"taskId\":\"6\"}"
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
    <RequestUuid>53240ac2-****-****-****-7348c400c0ca</RequestUuid>
    <PlaybookUuid>195afca5-****-****-a126a173e271</PlaybookUuid>
    <ResultStatus>success</ResultStatus>
    <ErrorMsg></ErrorMsg>
    <PageSize>100</PageSize>
    <PageNumber>1</PageNumber>
    <TotalCount>50</TotalCount>
    <SaoExecuteDetailInfoList>
        <Content>{"tenantId":"2**2","eventUuid":"cb8fe2ee-****-****-****-
b51a16f42677","aliUid":"1504*****314","taskId":"6"}</Content>
        <NodeName>returnAll</NodeName>
        <ActionUuid>1706237708172</ActionUuid>
    </SaoExecuteDetailInfoList>
```

### GetPlaybookTriggerResult

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- soar:GetPlaybookTriggerResult | Read | acs:yundun-soar:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | String | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| RequestUu id | String | Query | 是 | 99a947a5-***-****-****- 02288dd9b920 | 请求的唯一标识。 |
| NodeName | String | Query | 否 | msg notify _ | 节点名称。 |
| PageNumb er | Integ er | Query | 是 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1， 表示从第1页开始显示。 |
| PageSize | Integ er | Query | 是 | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20， 表示每页显示20条资产信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SaoExecuteDet ailInfoList | Array |  |  |
| -Content | String | {"tenantId":"2**2"," eventUuid":"cb8fe2 ee-****-****-****- b51a16f42677","ali Uid":"1504*****314" ,"taskId":"6"} | 内容。 |
| -NodeName | String | returnAll | 节点名称。 |
| -ActionUuid | String | 1706237708172 | 节点的唯一标识。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

|  |  |  | 安全编排自动化响应开发指南·剧本 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestUuid | String | 99a947a5-***-****- ****-02288dd9b920 | 请求的唯一标识。 |
| PlaybookUuid | String |  | 剧本的唯一编码。 |
| ResultStatus | String | success | 剧本执行状态： inprogress：处理中。 success：成功。 failed：失败。 |
| ErrorMsg | String |  | 错误信息，状态为错误的时候返回。 |
| PageSize | Integer | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20，表示每页显示20条资产信息。 |
| PageNumber | Integer | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1，表示从第1页开始显示。 |
| TotalCount | Integer | 50 | 查询到的数据的总数量。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetPlaybookTriggerResult&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&RequestUuid=99a947a5-***-****-****- 02288dd9b920&NodeName=msg_notify&PageNumber=1&PageSize=100
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "RequestUuid":"99a947a5-***-****-****-02288dd9b920",
    "PlaybookUuid":"",
    "ResultStatus":"success",
    "ErrorMsg":"",
    "PageSize":100,
    "PageNumber":1,
    "TotalCount":50,
    "SaoExecuteDetailInfoList":[
        {
            "ActionUuid":"1706237708172",
            "NodeName":"returnAll",
            "Content":"{\"tenantId\":\"2**2\",\"eventUuid\":\"cb8fe2ee-****-****-****-
b51a16f42677\",\"aliUid\":\"1504*****314\",\"taskId\":\"6\"}"
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
    <RequestUuid>99a947a5-***-****-****-02288dd9b920</RequestUuid>
    <PlaybookUuid></PlaybookUuid>
    <ResultStatus>success</ResultStatus>
    <ErrorMsg></ErrorMsg>
    <PageSize>100</PageSize>
    <PageNumber>1</PageNumber>
    <TotalCount>50</TotalCount>
    <SaoExecuteDetailInfoList>
        <Content>{"tenantId":"2**2","eventUuid":"cb8fe2ee-****-****-****-
b51a16f42677","aliUid":"1504*****314","taskId":"6"}</Content>
        <NodeName>returnAll</NodeName>
        <ActionUuid>1706237708172</ActionUuid>
    </SaoExecuteDetailInfoList>
```

### DescribeSoarTriggerResult

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- soar:DescribeSoarTriggerResult | Read | acs:yundun-soar:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | String | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| RequestUu id | String | Query | 是 | 99a947a5-***-****-****- 02288dd9b920 | 请求的唯一标识。 |
| NodeName | String | Query | 否 | msg notify _ | 节点名称。 |
| PageNumb er | Integ er | Query | 是 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1， 表示从第1页开始显示。 |
| PageSize | Integ er | Query | 是 | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20， 表示每页显示20条资产信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Contents | Array |  |  |
| -Content | String | {"tenantId":"2**2"," eventUuid":"cb8fe2 ee-****-****-****- b51a16f42677","ali Uid":"1504*****314" ,"taskId":"6"} | 内容。 |
| -NodeName | String | returnAll | 节点名称。 |
| -ActionUuid | String | 1706237708172 | 节点的唯一标识。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| PageSize | Integer | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20，表示每页显示20条资产信息。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageNumber | Integer | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1，表示从第1页开始显示。 |
| TotalCount | Integer | 50 | 查询到的数据的总数量。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=DescribeSoarTriggerResult&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&RequestUuid=99a947a5-***-****-****- 02288dd9b920&NodeName=msg_notify&PageNumber=1&PageSize=100
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "PageSize":100,
    "PageNumber":1,
    "TotalCount":50,
    "Contents":[
        {
            "ActionUuid":"1706237708172",
            "NodeName":"returnAll",
            "Content":"{\"tenantId\":\"2**2\",\"eventUuid\":\"cb8fe2ee-****-****-****-
b51a16f42677\",\"aliUid\":\"1504*****314\",\"taskId\":\"6\"}"
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
    <PageSize>100</PageSize>
    <PageNumber>1</PageNumber>
    <TotalCount>50</TotalCount>
    <Contents>
        <Content>{"tenantId":"2**2","eventUuid":"cb8fe2ee-****-****-****-
b51a16f42677","aliUid":"1504*****314","taskId":"6"}</Content>
        <NodeName>returnAll</NodeName>
        <ActionUuid>1706237708172</ActionUuid>
    </Contents>
```

**5.5.**

### DescribeSoarRecordActionOutputList

调用DescribeSoarRecordActionOutputList接口查询剧本动作的完整输出信息。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- soar:DescribeSoarRecordActionO utputList | Read | acs:yundun-soar:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | String | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| ActionUuid | String | Query | 是 | ffd16ad0-****-****-***- e9f0229a64bc-4 | 流程动作的唯一标识。 |
| SearchValu e | String | Query | 是 | test | 查询的关键字。 |
| PageNumb er | Integ er | Query | 是 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1， 表示从第1页开始显示。 |
| PageSize | Integ er | Query | 是 | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20， 表示每页显示20条资产信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| PageSize | Integer | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20，表示每页显示20条资产信息。 |

| 安全编排自动化响应 | 开发指南·剧本 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageNumber | Integer | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1，表示从第1页开始显示。 |
| TotalCount | Integer | 50 | 查询到的数据的总数量。 |
| ActionOutputs | String | [{"address": {"country":"巴西","city":""},"ip":"1 77.**.***.4"}, {"address": {"country":"中国","city":""},"ip":"1 10.**.***.66"}] | 节点的完整输出结果。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=DescribeSoarRecordActionOutputList&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&ActionUuid=ffd16ad0-****-****-***-e9f0229a64bc- 4&SearchValue=test&PageNumber=1&PageSize=100
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "PageSize":100,
    "PageNumber":1,
    "TotalCount":50,
    "ActionOutputs":"[{\"address\":{\"country\":\"巴西
\",\"city\":\"\"},\"ip\":\"177.**.***.4\"},{\"address\":{\"country\":\"中国\",\"city\":\"\"} ,\"ip\":\"110.**.***.66\"}]" }
```

`XML` 格式

```json
HTTP/1.1 200 OK Content-Type:application/xml <DescribeSoarRecordActionOutputListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <PageSize>100</PageSize>
    <PageNumber>1</PageNumber>
    <TotalCount>50</TotalCount>
    <ActionOutputs>[{"address":{"country":"巴西","city":""},"ip":"177.**.***.4"},{"address":
{"country":"中国","city":""},"ip":"110.**.***.66"}]</ActionOutputs> </DescribeSoarRecordActionOutputListResponse>
```

### ExportPlaybookActionData

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- soar:ExportPlaybookActionData | Write | acs:yundun-soar:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | String | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| ActionUuid | String | Query | 是 | 4dab66ad-**-****-****- 3cf0***d1f2-23 | 动作节点ID。 |
| SearchValu e | String | Query | 是 | 测试节点信息 | 搜索条件。 |
| StartTime | String | Query | 是 | 2024-01-01 00:00:00 | 开始时间。 |
| TaskName | String | Query | 是 | IP封禁任务 | 任务名称。 |
| SrcIp | String | Query | 是 | 10.**.**.123 | 服务器IP，通过 DescribeSoarRecordInfo查询剧本日志记录信息接口获取此IP信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| TaskId | String | export 4752259f- _ ***-***-*****- 223bad071807 | 任务ID。 |
| ExportUrl | String | https**//***.com | 导出数据的下载链接。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=ExportPlaybookActionData&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&ActionUuid=4dab66ad-**-****-****-3cf0***d1f2- 23&SearchValue=测试节点信息&StartTime=2024-01-01 00:00:00&TaskName=IP封禁任务 &SrcIp=10.**.**.123
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TaskId":"export_4752259f-***-***-*****-223bad071807",
    "ExportUrl":"https**//***.com"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TaskId>export_4752259f-***-***-*****-223bad071807</TaskId>
    <ExportUrl>https**//***.com</ExportUrl>
```

行日志

## 剧本执行日志

### DescribeSoarRecords

查询剧本历史执行记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | 是 | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Integ er | Query | 是 | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| QueryCond ition | String | Query | 否 | {\"type\":\"complex\",\"co ndition\":\" {\\\"condition\\\":\\\"AND\\ \",\\\"rules\\\": [{\\\"field\\\":\\\"taskName \\\",\\\"match\\\":\\\"is\\\",\\ \"type\\\":\\\"string\\\",\\\"v alue\\\": [\\\"test rtap\\\"]}]}\"} _ | 复杂的查询条件： field： 表示要匹配的字段。 value： 表示要匹配的值。 type： 表示匹配的类型，如下： match： 表示等于。 contains： 表示包含。 complex： 表示可嵌套的子查询，子查询遵循上述规则。 |
| TaskUuid | String | Query | 否 | 73b14357-e011-4993- a769-bfb779ab3638 | 本次流程执行的唯一 ID，TriggerPlaybook 中的返回的TriggerUuid 。如果TriggerUuid 在，则不使用QueryCondition 中的条件。 |
| PlaybookN ame | String | Query | 否 | 测试剧本 | 剧本名称。 |
| TriggerUse r | String | Query | 否 | user | 触发剧本的用户名称。 |

行日志

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TaskStatus | String | Query | 否 | success | 剧本运行状态: success： 成功。 failed： 失败 inprogress： 正在运行。 |
| PlaybookU uid | String | Query | 否 | 77dd60ec-a788-4cc9- a930-bedcfca4ce5f | 剧本运行的唯一ID。 |
| TaskflowM d5 | String | Query | 否 | 58638e2be58a4185f5106 298fb3e5157 | 流程的配置文件的Md5信息。 |
| TaskType | String | Query | 否 | general | 任务类型。 |
| StartMillis | String | Query | 否 | 1695107717298 | 查询开始时间节点。 |
| EndMillis | String | Query | 否 | 1695194117298 | 查询结束时间节点。 |
| RequestUu id | String | Query | 否 | bdeaa8bc-a003-4a9a- b37c-249d64a41ba2 | 本次流程执行的唯一ID。 |
| TriggerTyp e | String | Query | 否 | stream | 触发类型： stream： 流式。 manual： 人工。 schedule： 定时调度。 trace： 作战室。 |
| EventId | String | Query | 否 | 1 | 事件ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SoarExecuteRe cords | Array | [] | 执行结果详情。 |
| -Id | Long | 1 | 查询记录的ID。 |
| -RequestUuid | String | a5a60946-3ad4- 4e0d-92db- 500da9619793 | 本次流程执行的唯一ID。 |
| -PlaybookName | String | 测试 | 剧本名称。 |
| -TriggerType | String | manual | 触发的类型。 |

|  |  |  |  | 安全编排自动化响应开发指南·剧本执行日志 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -TriggerUser | String | 12385**452 | 该次剧本执行的触发人，为调用用户登录账号的 ID。 |
| -TenantId | String | -999999 | 租户信息。 |
| -TaskTenantId | String | -1 | 触发任务的租户信息。 |
| -ResultStatus | String | success | 剧本执行状态。 |
| -TaskStatus | String | TaskStatus | 任务状态。 |
| -TaskflowMd5 | String | 58638e2be58a4185 f5106298fb3e5157 | 流程的配置文件的Md5信息。 |
| -PlaybookUuid | String | bdeaa8bc-a003- 4a9a-b37c- 249d64a41ba2 | 剧本唯一键ID。 |
| -EndTime | Long | 1695179134000 | 任务执行结束时间。 |
| -StartTime | Long | 1695179131000 | 任务执行开始时间。 |
| -FlowTag | Integer | 1 | 执行的任务是否为正式发布的剧本 0：否 1：是 |
| RequestId | String | 1C982EAB-D314- 4583-B108- 62F20DE02CD5 | 本次流程执行的唯一ID。 |
| PageSize | Integer | 1 | 分页信息，页码。 |
| PageNumber | Integer | 10 | 分页信息，每页返回的数据量。 |
| TotalCount | Integer | 50 | 数据总数据量。 |

**示例**

`JSON` 格式行日志

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":50,
 "RequestId":"1C982EAB-D314-4583-B108-62F20DE02CD5",
 "PageSize":1,
 "PageNumber":10,
 "SoarExecuteRecords":{
  "TriggerType":"manual",
  "EndTime":1695179134000,
  "ResultStatus":"success",
  "TaskTenantId":"-1",
  "StartTime":1695179131000,
  "PlaybookName":"测试",
  "TaskStatus":"TaskStatus",
  "TriggerUser":"\t12385**452\t",
  "PlaybookUuid":"bdeaa8bc-a003-4a9a-b37c-249d64a41ba2",
  "TenantId":"-999999",
  "Id":1,
  "RequestUuid":"a5a60946-3ad4-4e0d-92db-500da9619793\t",
  "TaskflowMd5":"58638e2be58a4185f5106298fb3e5157",
  "FlowTag":1
 }
}
```

`XML` 格式

```xml
<TotalCount>50</TotalCount> <RequestId>1C982EAB-D314-4583-B108-62F20DE02CD5</RequestId> <PageSize>1</PageSize> <PageNumber>10</PageNumber> <SoarExecuteRecords>
 <TriggerType>manual</TriggerType>
 <EndTime>1695179134000</EndTime>
 <ResultStatus>success</ResultStatus>
 <TaskTenantId>-1</TaskTenantId>
 <StartTime>1695179131000</StartTime>
 <PlaybookName>测试</PlaybookName>
 <TaskStatus>TaskStatus</TaskStatus>
 <TriggerUser>
12385**452 </TriggerUser>
  <PlaybookUuid>bdeaa8bc-a003-4a9a-b37c-249d64a41ba2</PlaybookUuid>
  <TenantId>-999999</TenantId>
  <Id>1</Id>
  <RequestUuid>a5a60946-3ad4-4e0d-92db-500da9619793
  </RequestUuid>
  <TaskflowMd5>58638e2be58a4185f5106298fb3e5157</TaskflowMd5>
  <FlowTag>1</FlowTag>
 </SoarExecuteRecords>
```

### DescribeSoarRecordInfo

调用DescribeSoarRecordInfo接口查询剧本的执行日志的详情信息。 行日志

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- soar:DescribeSoarRecordInfo | Read | acs:yundun-soar:*: {#accountId}:* |

**流量控制**

单用户调用频率：20QPS。 API调用频率：200QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | String | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| RequestUu id | String | Query | 是 | 5076e93f-****-****-****- d1b4fd3e4336 | 流程执行记录的唯一标识。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| TriggerType | String | debug | 触发剧本的执行类型： debug：调试模式。 stream：流式触发。 manual：人工触发。 schedule： 定时调度。 trace：作战室触发。 |
| TriggerDataId | String | 5076e93f-****-****- ****-d1b4fd3e4336 | 触发数据ID。 |
| Sao | String | 测试剧本 | 剧本的名称。 |
| TaskName | String | 测试剧本 | 任务名称（与剧本名称一致）。 |
| EndTime | Long | 1706077659725 | 流程运行结束时间。 |
| StartTime | Long | 1706077659685 | 流程运行开始时间。 |
| EventId | String | 5076e93f-****-****- ****-d1b4fd3e4336 | 事件ID。 |

| 安全编排自动化响应行日志 | 开发指南·剧本执 |  |  |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| Status | String | success | 剧本的运行状态： success：成功。 failed：失败。 inprogress：正在运行。 |
| TaskUuid | String | 1f32aa0b-****-****- af7c-eccdc5c219e2 | 流程的唯一编码。 |
| TriggerUser | String | alibaba | 触发流程的用户。 |
| RequestUuid | String | 5076e93f-****-****- ****-d1b4fd3e4336 | 流程执行记录的唯一标识。 |
| ErrorMsg | String | server error | 流程执行后的报错信息。 |
| DataSourceNa me | String | 测试数据源。 | 数据源名称。 |
| RouterPath | String | {"actorPath":"/user/ sysActorMgr/eventM atchRouter/$e/1238 88 saoDebug 1706 _ _ ****6851.01","port": ***,"ip":"10.**.**.72" } | 剧本的路由路径。 |
| SrcIp | String | 10.**.**.72 | 剧本运行的服务器IP。 |
| ResultLevel | String | DEBUG | 剧本的执行类型： debug：调试模式。 stream：流式触发。 manual：人工触发。 schedule：定时调度。 trace：作战室触发。 |
| ResultDetailInfo | String | [] | 任务执行详情。 |
| TaskTenantId | String | -1 | 该次剧本执行的触发人，为调用用户登录账号的 ID。 |
| TaskType | String | general | 流程操作类型，固定填写为general。 |
| PlaybookUuid | String | bbb82d1f-****-****- 8927-28c13c8fc3bc | 剧本的唯一标识ID。 |
| TaskFlowMd5 | String | 4e2847a0*********2 73e9952cef | 流程的MD5值。 |

|  |  |  | 安全编排自动化响应开发指南·剧本执 |
|---|---|---|---|

行日志

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| EventStr | String | { "banTime":"48h", "organization":"all", "banType":"all", "IsVpcWebsite":"fals e" } | 流程的输入信息。 |
| TenantId | String | -1 | 执行流程的租户ID。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=DescribeSoarRecordInfo&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&RequestUuid=5076e93f-****-****-****-d1b4fd3e4336
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TriggerType":"debug",
    "TriggerDataId":"5076e93f-****-****-****-d1b4fd3e4336",
```

`"Sao":"`测试剧本`",` `"TaskName":"`测试剧本`",`

```json
    "EndTime":1706077659725,
    "StartTime":1706077659685,
    "EventId":"5076e93f-****-****-****-d1b4fd3e4336",
    "Status":"success",
    "TaskUuid":"1f32aa0b-****-****-af7c-eccdc5c219e2",
    "TriggerUser":"alibaba",
    "RequestUuid":"5076e93f-****-****-****-d1b4fd3e4336",
    "ErrorMsg":"server error",
```

`"DataSourceName":"`测试数据源。`",`

```json
    "RouterPath":"
{\"actorPath\":\"/user/sysActorMgr/eventMatchRouter/$e/123888_saoDebug_1706****6851.01\",\"po \":***,\"ip\":\"10.**.**.72\"}",
    "SrcIp":"10.**.**.72",
    "ResultLevel":"DEBUG",
    "ResultMessage":"",
    "ResultDetailInfo":"[]",
    "TaskTenantId":"-1",
    "TaskType":"general",
    "PlaybookUuid":"bbb82d1f-****-****-8927-28c13c8fc3bc",
    "TaskFlowMd5":"4e2847a0*********273e9952cef",
    "EventStr":"{                            \"banTime\":\"48h\",
"organization\":\"all\", \"banType\":\"all\", \"IsVpcWebsite\":\"false\" }",
    "TenantId":"-1"
}
```

行日志 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TriggerType>debug</TriggerType>
    <TriggerDataId>5076e93f-****-****-****-d1b4fd3e4336</TriggerDataId>
```

`<Sao>`测试剧本`</Sao>` `<TaskName>`测试剧本`</TaskName>`

```xml
    <EndTime>1706077659725</EndTime>
    <StartTime>1706077659685</StartTime>
    <EventId>5076e93f-****-****-****-d1b4fd3e4336</EventId>
    <Status>success</Status>
    <TaskUuid>1f32aa0b-****-****-af7c-eccdc5c219e2</TaskUuid>
    <TriggerUser>alibaba</TriggerUser>
    <RequestUuid>5076e93f-****-****-****-d1b4fd3e4336</RequestUuid>
    <ErrorMsg>server error</ErrorMsg>
```

`<DataSourceName>`测试数据源。`</DataSourceName>`

```json
    <RouterPath>
{"actorPath":"/user/sysActorMgr/eventMatchRouter/$e/123888_saoDebug_1706****6851.01","port":* ,"ip":"10.**.**.72"}</RouterPath>
    <SrcIp>10.**.**.72</SrcIp>
    <ResultLevel>DEBUG</ResultLevel>
    <ResultMessage></ResultMessage>
    <ResultDetailInfo>[]</ResultDetailInfo>
    <TaskTenantId>-1</TaskTenantId>
    <TaskType>general</TaskType>
    <PlaybookUuid>bbb82d1f-****-****-8927-28c13c8fc3bc</PlaybookUuid>
    <TaskFlowMd5>4e2847a0*********273e9952cef</TaskFlowMd5>
    <EventStr>{ "banTime":"48h", "organization":"all", "banType":"all",
"IsVpcWebsite":"false" }</EventStr>
    <TenantId>-1</TenantId>
```

表

## 任务列表

### DescribeManualTaskInfo

查询执行结果信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Long | Query | 否 | 1 | 任务ID(任务ID和TaskUUID 必填一个)。 |
| NodeName | String | Query | 否 | test | 节点名称。 |
| TaskUuid | String | Query | 否 | 13123233 | 任务UUID(任务ID和 TaskUUID必填一个)。 |
| NeedDataI nfo | Boole an | Query | 是 | true | 是否返回数据详情： true ：是。 false ：否。 |
| PageNumb er | Integ er | Query | 是 | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Integ er | Query | 是 | 10 | 分页查询时，指定每页最多显示的数据条数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ManualTaskRec ords | Array |  | 任务详情。 |
| - AssignedUserId | String | test | 用户ID。 |
| - AssignedUserG roup | String | test | 用户组。 |
| -GmtCreate | Long | 1641803299000 | 创建时间。 |
| -GmtModified | Long | 1641803299000 | 更新时间。 |

| 安全编排自动化响应 | 开发指南·任务列 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Id | Long | 1231 | 节点ID。 |
| -PlaybookId | Long | 123 | 剧本ID。 |
| -PlaybookName | String | 测试剧本 | 剧本名称。 |
| -NodeName | String | test | 节点名。 |
| -Status | Integer | 0 | 任务状态，不传查所有： -1 ：无需处理。 0 ：未处理。 1 ：已经处理。 2 ：超时未处理。 |
| -TaskUuid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | 任务ID。 |
| -ActionUuid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | 动作UUID。 |
| -ActualDealerId | String | 1 | 处理ID。 |
| - ActualDealedTi me | Long | 1641803299000 | 处理时间。 |
| -PageConfigId | Long | 1 | 页面配置ID。 |
| - DisplayActionU uid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | 展示UUID。 |
| -AkkaActorInfo | String | test | 动作节点信息。 |
| -DeadlineTime | Long | 1641803299000 | 延迟时间。 |
| -TenantId | String | -1 | 租户ID。 |
| -Content | String | 数据信息 | 内容信息。 |
| -Url | String |  | URL地址。 |
| -TaskType | Integer |  | 任务类型。 |

|  |  |  | 安全编排自动化响应开发指南·任务列表 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DataUrl | String | http://xxxxxx | 数据链接地址。 |
| -DataInfo | String | {"k":"value"} | 数据信息。 |
| -DownloadUrl | String | http://xxxxxx | 数据下载地址。 |
| -NeedDataInfo | Boolean | true | 是否需要展示节点信息。 |
| -PlaybookType | String |  | 剧本类型。 |
| -TaskTenantId | String | -2 | 执行任务的租户ID。 |
| RequestId | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | 本次调用请求的ID。 |
| PageNumber | Long | 1 | 分页查询时，设置当前页面的页码。 |
| PageSize | Long | 10 | 分页查询时，指定每页最多显示的数据条数。 |
| TotalCount | Long | 100 | 总数量。 |

**示例**

`JSON` 格式表

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":100,
 "RequestId":"AF2B656D-C2C1-4E47-85FD-1596C83C6B86",
 "PageSize":10,
 "ManualTaskRecords":{
  "ActualDealedTime":1641803299000,
  "ActionUuid":"AF2B656D-C2C1-4E47-85FD-1596C83C6B86\t",
  "AssignedUserId":"test",
  "NodeName":"test",
  "NeedDataInfo":true,
  "GmtModified":1641803299000,
  "AkkaActorInfo":"test",
```

`"PlaybookName":"`测试剧本`",`

```json
  "Url":"",
  "TaskType":"",
  "ActualDealerId":"1",
  "DownloadUrl":"http://xxxxxx\t",
  "Status":0,
  "DataInfo":"{\"k\":\"value\"}\t",
  "AssignedUserGroup":"test",
  "TaskUuid":"AF2B656D-C2C1-4E47-85FD-1596C83C6B86\t",
  "TaskTenantId":"-2",
  "PageConfigId":1,
  "GmtCreate":1641803299000,
  "TenantId":"-1",
  "DeadlineTime":1641803299000,
```

`"Content":"`数据信息\t",

```json
  "DataUrl":"http://xxxxxx\t",
  "PlaybookId":123,
  "Id":1231,
  "DisplayActionUuid":"AF2B656D-C2C1-4E47-85FD-1596C83C6B86\t",
  "PlaybookType":""
 },
 "PageNumber":1
}
```

`XML` 格式表

```xml
<TotalCount>100</TotalCount> <RequestId>AF2B656D-C2C1-4E47-85FD-1596C83C6B86</RequestId> <PageSize>10</PageSize> <ManualTaskRecords>
 <ActualDealedTime>1641803299000</ActualDealedTime>
 <ActionUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86
 </ActionUuid>
 <AssignedUserId>test</AssignedUserId>
 <NodeName>test</NodeName>
 <NeedDataInfo>true</NeedDataInfo>
 <GmtModified>1641803299000</GmtModified>
 <AkkaActorInfo>test</AkkaActorInfo>
 <PlaybookName>测试剧本</PlaybookName>
 <Url  />
 <TaskType  />
 <ActualDealerId>1</ActualDealerId>
 <DownloadUrl>http://xxxxxx
 </DownloadUrl>
 <Status>0</Status>
 <DataInfo>{&quot;k&quot;:&quot;value&quot;}
 </DataInfo>
 <AssignedUserGroup>test</AssignedUserGroup>
 <TaskUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86
 </TaskUuid>
 <TaskTenantId>-2</TaskTenantId>
 <PageConfigId>1</PageConfigId>
 <GmtCreate>1641803299000</GmtCreate>
 <TenantId>-1</TenantId>
 <DeadlineTime>1641803299000</DeadlineTime>
```

`<Content>`数据信息

```xml
 </Content>
 <DataUrl>http://xxxxxx
 </DataUrl>
 <PlaybookId>123</PlaybookId>
 <Id>1231</Id>
 <DisplayActionUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86
 </DisplayActionUuid>
 <PlaybookType  />
</ManualTaskRecords> <PageNumber>1</PageNumber>
```

### DescribeManualTaskRecords

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- soar:DescribeManualTaskRecords | Read | acs:yundun-soar:*: {#accountId}:* |

**流量控制**

单用户调用频率：20QPS。 表 API调用频率：200QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SourceIp | String | Query | 否 | 219.133.XX.XX | 访问源IP地址。 |
| PlaybookN ame | String | Query | 否 | Sys Beaver waf applicati _ _ _ on ban v64 _ _ | 剧本名称。 |
| PageNumb er | Integ er | Query | 是 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1， 表示从第1页开始显示。 |
| PageSize | Integ er | Query | 是 | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20， 表示每页显示20条资产信息。 |
| NodeName | String | Query | 否 | MsgNotify | 节点名称。 |
| Status | String | Query | 否 | 0 | 任务状态： 0：未处理。 1：已处理。 2：超时未处理。 -1：无需处理。 |
| Content | String | Query | 否 | key | 内容。 |
| StartTime | Long | Query | 否 | 1706004856000 | 开始时间。 |
| EndTime | Long | Query | 否 | 1706004856000 | 结束时间。 |
| TaskType | Integ er | Query | 否 | 0 | 任务类型： 0：需人工处理 （默认值）。 1：钉钉消息。 3：任务通知。 |
| TaskTenan tId | String | Query | 否 | -1 | 任务所属的租户ID。 |
| PlaybookU uid | String | Query | 否 | 8de26e06-****-****-****- 08f8e1598b49 | 剧本的唯一标识。 |

**返回数据**

表

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ManualTaskRec ords | Array |  |  |
| - AssignedUserId | String | 1 | 当前任务处理人的用户ID。 |
| - AssignedUserG roup | String | user | 当前任务处理人组的信息。 |
| -GmtCreate | Long | 1705572167000 | 创建时间。 |
| -GmtModified | Long | 1705572167001 | 修改时间。 |
| -Id | Long | 1 | 任务编码。 |
| -PlaybookId | Long | 50 | 剧本编码。 |
| -PlaybookName | String | Sys Beaver waf ap _ _ _ plication ban v64 _ _ | 剧本名称。 |
| -NodeName | String | MsgNotify | 节点名称。 |
| -Status | Integer | 0 | 任务状态： 0：未处理。 1：已处理。 2：超时未处理。 -1：无需处理。 |
| -TaskUuid | String | bcc5818f-****-****- ****-09f14a1ccc7e | 任务ID。 |
| -ActionUuid | String | 3896adf2-****-****- ****-63546a067a78 | 节点请求的唯一标识。 |
| -ActualDealerId | String | 1 | 任务实际处理人。 |
| - ActualDealedTi me | Long | 1706078939000 | 实际被处理的时间。 |
| -PageConfigId | Long | 2 | 展示模版ID。 |
| - DisplayActionU uid | String | displayUuid | 展示节点请求的唯一标识。 |
| -AkkaActorInfo | String | selfActorInfo | 人工节点所在的AKKA集群中的actor信息。 |

| 安全编排自动化响应表 | 开发指南·任务列 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DeadlineTime | Long | 1706078939000 | 处理时间。 |
| -TenantId | String | -1 | 租户ID。 |
| -Content | String | 一键封禁操作完成，摘要如下，具体参见详情链接.. | 任务内容。 |
| -Url | String | http*://**.com | 任务关联的URL。 |
| -TaskType | Integer | 0 | 任务类型： 0：需人工处理 （默认值）。 1：钉钉消息。 3：任务通知。 |
| -DataUrl | String | http*://**.com | 数据URL。 |
| -ErrorMsg | String |  | 错误信息。 |
| -PlaybookType | String | general | 剧本类型，固定填写为general。 |
| -TaskTenantId | String | -2 | 执行任务的租户ID。 |
| -PlaybookUuid | String | a7535142-****-****- ****-97b3eae7d34b | 剧本的唯一标识。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| PageNumber | Long | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1，表示从第1页开始显示。 |
| PageSize | Long | 100 | 设置分页查询时，每页显示的资产的数量。默认值为20，表示每页显示20条资产信息。 |
| TotalCount | Long | 50 | 查询到的数据的总数量。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=DescribeManualTaskRecords&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&PlaybookName=Sys_Beaver_waf_application_ban_v64&PageNumber=1& geSize=100&NodeName=MsgNotify&Status=0&Content=key&StartTime=1706004856000&EndTime=1706004856 0&TaskType=0&TaskTenantId=-1&PlaybookUuid=8de26e06-****-****-****-08f8e1598b49
```

表正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "PageNumber":1,
    "PageSize":100,
    "TotalCount":50,
    "ManualTaskRecords":[
        {
            "ActualDealedTime":1706078939000,
            "ActionUuid":"3896adf2-****-****-****-63546a067a78",
            "AssignedUserId":"1",
            "NodeName":"MsgNotify",
            "GmtModified":1705572167001,
            "AkkaActorInfo":"selfActorInfo",
            "PlaybookName":"Sys_Beaver_waf_application_ban_v64",
            "Url":"http*://**.com",
            "TaskType":"",
            "ActualDealerId":"1",
            "Status":0,
            "AssignedUserGroup":"user",
            "TaskUuid":"bcc5818f-****-****-****-09f14a1ccc7e",
            "ErrorMsg":"",
            "TaskTenantId":"-2",
            "PlaybookUuid":"a7535142-****-****-****-97b3eae7d34b",
            "PageConfigId":2,
            "GmtCreate":1705572167000,
            "TenantId":"-1",
            "DeadlineTime":1706078939000,
```

`"Content":"`一键封禁操作完成，摘要如下，具体参见详情链接`..",`

```json
            "DataUrl":"http*://**.com",
            "PlaybookId":50,
            "Id":1,
            "DisplayActionUuid":"displayUuid",
            "PlaybookType":"general"
        }
```

]

```
}
```

`XML` 格式表

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <PageNumber>1</PageNumber>
    <PageSize>100</PageSize>
    <TotalCount>50</TotalCount>
    <ManualTaskRecords>
        <AssignedUserId>1</AssignedUserId>
        <AssignedUserGroup>user</AssignedUserGroup>
        <GmtCreate>1705572167000</GmtCreate>
        <GmtModified>1705572167001</GmtModified>
        <Id>1</Id>
        <PlaybookId>50</PlaybookId>
        <PlaybookName>Sys_Beaver_waf_application_ban_v64</PlaybookName>
        <NodeName>MsgNotify</NodeName>
        <Status>0</Status>
        <TaskUuid>bcc5818f-****-****-****-09f14a1ccc7e</TaskUuid>
        <ActionUuid>3896adf2-****-****-****-63546a067a78</ActionUuid>
        <ActualDealerId>1</ActualDealerId>
        <ActualDealedTime>1706078939000</ActualDealedTime>
        <PageConfigId>2</PageConfigId>
        <DisplayActionUuid>displayUuid</DisplayActionUuid>
        <AkkaActorInfo>selfActorInfo</AkkaActorInfo>
        <DeadlineTime>1706078939000</DeadlineTime>
        <TenantId>-1</TenantId>
```

`<Content>`一键封禁操作完成，摘要如下，具体参见详情链接`..</Content>`

```xml
        <Url>http*://**.com</Url>
        <TaskType></TaskType>
        <DataUrl>http*://**.com</DataUrl>
        <ErrorMsg></ErrorMsg>
        <PlaybookType>general</PlaybookType>
        <TaskTenantId>-2</TaskTenantId>
        <PlaybookUuid>a7535142-****-****-****-97b3eae7d34b</PlaybookUuid>
    </ManualTaskRecords>
```

码表

## 错误代码表

本文介绍云盾API返回的错误代码信息。 表 1. 云盾通用错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.all.10001 | 权限不够 | 请检查账户权限。 |
| yd.error.all.10002 | 系统错误，请稍后重试 | 请稍后重试。 |
| yd.error.all.10003 | 参数错误 | 请检查请求参数后重试。 |
| yd.error.all.other | 系统异常 | 请稍后重试。 |
| yd.error.all.ConsoleSystemError _ 1001 | 未知异常 | 请稍后重试。 |
| yd.error.all.ConsoleSystemError _ 1007 | api已下线 | 请联系阿里云技术支持人员。 |
| yd.error.all.ConsoleSystemError _ 1008 | postOnly校验失败 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError _ 1009 | csrfToken为空 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError _ 1010 | csrfToken校验失败 | 请检查公共请求参数后重试。 |
| yd.error.all.ConsoleSystemError _ 1011 | regionId为空 | 请检查RegionId请求参数。 |
| yd.error.all.ConsoleSystemError _ 1012 | regionId格式错误 | 请检查RegionId请求参数。 |
| yd.error.all.ConsoleSystemError _ 1013 | 参数为空 | 请检查请求参数后重试。 |
| yd.error.all.ConsoleSystemError _ 1014 | 参数格式错误 | 请检查请求参数后重试。 |
| yd.error.all.ConsoleNeedLogin | 未登录 | 请检查账户权限。 |
| yd.error.all.InvalidApi | 接口异常 | 请稍后重试。 |
| yd.error.all.InvalidParameter | 参数异常 | 请检查请求参数后重试。 |
| yd.error.all.InvalidResult | 返回值异常 | 请稍后重试。 |
| yd.error.all.PropertyConvertFaile d | 转换异常 | 请稍后重试。 |
| yd.error.all.NoPermission | 无权限 | 请检查账户权限。 |
| yd.error.all.ServerError | 服务器异常 | 请稍后重试或联系阿里云技术支持人员。 |
| yd.error.all.UnkownError | 未知异常 | 请稍后重试或联系阿里云技术支持人员。 |

码表表 2. 态势感知错误代码

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
| yd.error.ddos.UNKNOWN EXCEPT _ ION | 未知异常 | 请联系阿里云技术支持人员。 |
| yd.error.ddos.REQUEST TIMEOUT _ | 请求超时 | 请稍后重试。 |
| yd.error.ddos.SERVER FAILED _ | 操作失败 | 请联系阿里云技术支持人员。 |
| yd.error.ddos.NOT AUTHORIZED _ | 没有权限 | 请检查账户权限。 |
| yd.error.ddos.PARAMETER INVALI _ D | 参数无效或缺少 | 请求参数有误，请检查后重试。 |
| yd.error.ddos.IP SEGMENT INVAL _ _ ID | IP段不合法，请检查后重新输入 | 请检查请求参数中的IP网段。 |
| yd.error.ddos.IP SEGMENT REPE _ _ AT | 同一网段不能配置不同区域，请检查后重新输入 | 请检查请求参数中的IP网段。 |

码表

| yd.error.ddos.IP SEGMENT ALRE _ _ ADY | 网段已存在，请重新输入 | 请检查请求参数中的IP网段。 |
|---|---|---|
| yd.error.ddos.IP SEGMENT MASK _ _ LENGTH ERR _ _ | 掩码长度需小于或等于24字符 | 请检查请求参数中的IP网段的掩码。 |
| yd.error.ddos.QUERY REGION LIS _ _ T ERR _ | 读取区域列表失败 | 请稍后重试。 |
| yd.error.ddos.IP SEGMENT OPER _ _ ATION ERR _ | 处理网段操作失败 | 请稍后重试。 |
| yd.error.ddos.QUERY IP SEGMEN _ _ T ERR _ | 读取网段信息失败 | 请稍后重试。 |
| yd.error.ddos.MODIFY IP SEGME _ _ NT ERR _ | 修改网段信息失败 | 请稍后重试。 |
| yd.error.ddos.IP SEGMENT TYPE _ _ _ ERR | 请检查是否设置网段类型（外网网段或内网网段） | 请检查网段类型后重试。 |
| yd.error.ddos.CANCEL FLOW CLE _ _ AN ERR _ | 取消清洗失败，请确认与beaver的网络连接是否正常 | 请检查与流量安全监控模块的网络连接后重试。 |
| yd.error.ddos.QUERY FLOW ANA _ _ LYSIS ERR _ | 获取流量分析结果失败，请确认与 beaver的网络连接是否正常 | 请检查与流量安全监控模块的网络连接后重试。 |
| yd.error.ddos.QUERY BEAVER UR _ _ L ERR _ | 获取beaver Url失败 | 请检查与流量安全监控模块的网络连接后重试。 |
| yd.error.ddos.SET VALVE INVALI _ _ D | 阈值校验失败，请确认各阈值后重新输入 | 请检查阈值参数后重试。 |
| yd.error.ddos.VALVE DEFAULT A _ _ LREADY | 无效的请求，不允许再次添加default 阈值 | 无法再次添加默认阈值，只能修改。 |
| yd.error.ddos.NOT BELONG BEA _ _ VER IP SEGMENT _ _ | 请检查输入网段是否属于Beaver内网网段 | 请检查网段是否属于流量监控内网网段。 |
| yd.error.ddos.VALVE DELETE ER _ _ R | default或128.0.XX.XX/XX，阈值不允许删除 | 默认阈值或128.0.XX.XX/XX网段的阈值无法删除 |
| yd.error.ddos.QUERY CODE ERR _ _ | 读取字典异常 | 请稍后重试。 |
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

码表

| yd.error.audit.Alert.IdNotExist | 接收人不存在 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.Receiver.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.IdNotExist | 接收人不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.LogTypeE mpty | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.LogTypeP atternWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.LogSourc eidNotExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.NameEm pty | 【名称】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.NameLen gthWrong | 【名称】不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.ContactE mpty | 【联系方式】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.ContactLe ngthWrong | 【联系方式】不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.Receiver.ContactN otEmail | 【联系方式】必须为邮件格式 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotExist | 字典值【%s】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotBoolean | 字典值非Boolean类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotInteger | 字典值非Integer类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotLong | 字典值非Long类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotFloat | 字典值非Float类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotDouble | 字典值非Double类型 | 请检查请求参数后重试。 |
| yd.error.audit.Dict.NotString | 字典值非String类型 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.IdEmpt y | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.IdNotEx ist | 事件类型不存在 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.LogTyp eEmpty | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.LogTyp ePatternWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.LogSour ceIdNotExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.Reserve dEmpty | 【是否预留】不能为空 | 请检查请求参数后重试。 |

码表

| yd.error.audit.EventType.NameE mpty | 【名称】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.EventType.NameLe ngthWrong | 【名称】不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.EventType.Remark LengthWrong | 【备注】不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.IdNotExist | 规则不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.LogTypeEmpt y | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.LogTypePatte rnWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.LogSourceIdN otExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.NameEmpty | 【名称】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.NameLength Wrong | 【名称】长度不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.ExpressionEm pty | 【表达式】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.ExpressionLe ngthWrong | 【表达式】长度不成超过500字符 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.ExpressionPat ternWrong | 【表达式】正则表达式格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.EventTypeEm pty | 【事件类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.EventTypeNot Exist | 【事件类型】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.RiskLevelEmp ty | 【风险级别】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.ReserverEmpt y | 【是否预留】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.EnableEmpty | 【是否启用】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.AlerttAbleEmp ty | 【是否告警】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.AlerttActionE mpty | 【告警动作】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.AlerttAcitonPa tternWrong | 【告警动作】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.Rule.RemarkLengt hWrong | 【备注】不能超过20000字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |

码表

| yd.error.audit.LogConfig.EnableE mpty | 【是否启用】不能为空 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.LogConfig.AlerttAbl eEmpty | 【是否告警】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.TypeEm pty | 【类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.TypePatt ernWrong | 【类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogStor ePeriodEmpty | 【日志存储周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogArchi vePeriodEmpty | 【日志归档周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogArchi vePeriodLengthWrong | 【日志归档周期】不能超过1095天 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogArchi veIntervalEmpty | 【日志归档间隔】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.LogArchi veIntervalPatternWrong | 【日志归档间隔】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventSt orePeriodEmpty | 【事件存储周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventSt orePeriodLengthWrong | 【事件存储周期】不能超过1095天 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventAr chivePeriodEmpty | 【事件归档周期】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventAr chivePeriodLengthWrong | 【事件归档周期】不能超过1095天 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventAr chiveIntervalEmpty | 【事件归档间隔】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogConfig.EventAr chiveIntervalPatternWrong | 【事件归档间隔】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.IdNotExist | 【id】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.TypeEmpt y | 【类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.TypePatte rnWrong | 【类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.UserIdEm pty | 【用户】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.UserIdLen gthWrong | 【用户】长度不成超过500字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogFilter.LogType. emtpy | 【日志类型】不能为空 | 请检查请求参数后重试。 |

码表

| yd.error.audit.LogFilter.LogTypeP atternWrong | 【日志类型】格式错误 | 请检查请求参数后重试。 |
|---|---|---|
| yd.error.audit.LogFilter.LogSourc eIdNotExist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.IdEmpty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.LogTyp eEmpty | 【日志类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeEm pty | 【编码】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeLe ngthWrong | 【编码】长度不能超过50字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodePat ternWrong | 【编码】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeNo tExist | 【编码】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.CodeExi st | 【编码】已存在 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.NameE mpty | 【名称】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.NameLe ngthWrong | 【名称】长度不能超过200字符 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.EnableE mpty | 【是否启用】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.AlerttAb leEmpty | 【是否告警】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.TypePat ternWrong | 【类型】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.LogSource.Remark LengthWrong | 【备注】长度不能超过20000字符 | 请检查请求参数后重试。 |
| yd.error.audit.log.LogSourceIdNot Exist | 【日志源】不存在 | 请检查请求参数后重试。 |
| yd.error.audit.ProcessTask.IdEmp ty | 【id】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.ProcessTask.TypeE mpty | 【任务类型】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.ProcessTask.Param Empty | 【执行参数】不能为空 | 请检查请求参数后重试。 |
| yd.error.audit.ProcessTask.Param PatternWrong | 【执行参数】格式错误 | 请检查请求参数后重试。 |
| yd.error.audit.System.Error | 系统内部错误 | 请联系阿里云技术支持人员。 |
| yd.error.audit.System.NotFind | 资源未找到 | 请稍后重试。 |

码表

| yd.error.audit.System.AuthError | 权限认证失败 | 请检查账户权限。 |
|---|---|---|

表 6. 同步中心错误代码

| 错误代码 | 错误信息 | 说明 |
|---|---|---|
| yd.error.scs.100 | 请求参数错误 | 请求参数有误，请检查后重试。 |
| yd.error.scs.101 | 未授权 | 请检查账户权限。 |
| yd.error.scs.102 | 无需更新 | 指定业务规则库无需更新。 |
| yd.error.scs.500 | 内部异常 | 请联系阿里云技术支持人员。 |
| yd.error.ddos.UPGRADE SWITCH _ _ ERR | 升级通道开关失败 | 请稍后重试。 |
| yd.error.ddos.AUTO UPGRADE S _ _ WITCH | 自动升级通道操作失败 | 请稍后重试。 |

表 7. 云防火墙错误码

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

码表

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

码表

| yd.error.code.-360148 | 相同网段不能重复配置，请重新选择网段 |
|---|---|
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

码表

| yd.error.code.-360179 | 调用接口失败 |
|---|---|
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

码表

| yd.error.code.-360210 | cen ID错误 |
|---|---|
| yd.error.code.-360211 | 参数错误，请重试 |
| yd.error.code.-360212 | 云企业网VPC数量限制，无法开启VPC边界防火墙 |
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

码表

| yd.error.code.-360322 | 更新IDC专线失败 |
|---|---|
| yd.error.code.-360323 | 更新IDC路由信息失败 |
| yd.error.code.-360400 | 未知错误 |
| yd.error.code.-360401 | 没有可用的Vlan |
| yd.error.code.-360402 | 调用VPC接口失败 |
| yd.error.code.-360403 | 创建虚墙失败 |
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

码表

| yd.error.code.-193103 | 解析INT失败 |
|---|---|
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

码表

| yd.error.code.-200106 | 地址簿IP地址错误，请检查输入 |
|---|---|
| yd.error.code.-200107 | 地址簿已存在 |
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

码表

| yd.error.code.-200302 | 后台错误 |
|---|---|
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
| yd.error.code.-230104 | 参数失败 |
| yd.error.code.-230105 | 策略模板已存在 |

码表

| yd.error.code.-230106 | 策略模板不存在 |
|---|---|
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
| yd.error.code.-230151 | 策略组超出限制 |
| yd.error.code.-230152 | 策略组不允许修改 |
| yd.error.code.-230153 | 策略组前置 |
| yd.error.code.-230154 | 规则ID不合法 |

码表

| yd.error.code.-230200 | 后台错误 |
|---|---|
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
| ErrorParametersDstIP.-210921 | invalid para dst ip（无效的目的IP参数） | dstIP参数无效，需要传入有效的 dstIP。 |
| ErrorParametersPort.-210208 | invalid port, must 0~65535（无效的端口，端口范围0~65535） | 无效的端口参数，端口范围 0~65535。 |
| ErrorParametersLiveTime.- 210922 | invalid para live time（无效的 liveTime参数） | liveTime参数无效，需要传入有效的 liveTime。 |
| ErrorDBInsert.-210122 | internal error: sql insert（内部错误:sql insert发生错误） | 内部错误：sql insert发生错误。 |
| ErrorInnerUuid.-210606 | internal error: uuid list is 0（内部错误：UUID列表为空） | 内部错误：UUID列表为空。 |
| ErrorDBSelect.-210124 | internal error: sql select（内部错误:sql select发生错误） | 内部错误:sql select发生错误。 |
| ErrorParasAddressCidrFeild.- 210915 | paras addressCidrList filed （重置 addressCidrList规则失败） | 重置addressCidrList规则失败。 |
| ErrorPortAddressGroup.-210303 | get port in address group failed（在群组中获取prot失败） | 在群组中获取prot失败。 |
| ErrorPortAddressGroup.-210303 | get port in address group failed（在群组中获取prot失败） | 在群组中获取prot失败。 |
| ErrorSourceAddressGroup.- 210304 | get source address in address group failed（在群组中获取源地址失败） | 在群组中获取源地址失败。 |

码表

| ErrorSourceAddressRange.- 210306 | source address range error, must be like \"192.168.XX.XX/192.168.XX.XX\ "（源地址范围错误，举例： \"192.168.XX.XX/192.168.XX.XX\ "） | 源地址范围错误，举例： \"192.168.XX.XX/192.168.XX.XX\ "。 |
|---|---|---|
| ErrorDestAddressGroup.-210305 | get dest address in address group failed（在群组中获取目的地址失败） | 在群组中获取目的地址失败。 |
| ErrorNoBeaverRules.-210226 | no beaver rules for online（没有对应的beaver rules） | 没有对应的beaver rules。 |
| ErrorDBUpdate.-210121 | internal error: sql update（内部错误：sql update发生错误） | 内部错误：sql update发生错误。 |
| ErrorDBDelete.-210123 | internal error: sql delete（内部错误：sql delete发生错误） | 内部错误：sql delete发生错误。 |
| ErrorMarshalJSON.-210125 | internal error: marshal json（内部错误：marshal json发生错误） | 内部错误：marshal json发生错误。 |
