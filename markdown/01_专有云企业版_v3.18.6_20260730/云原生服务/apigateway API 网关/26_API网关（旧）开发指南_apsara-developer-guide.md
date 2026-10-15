---
title: "网关 API网关（旧）开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 174
source_pdf: "26_API网关（旧）开发指南_apsara-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/apigateway/zh/apsara-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 网关 API网关（旧）开发指南

API 网关

## 简介

欢迎使用阿里云 API 网关服务。用户可以使用本文档介绍的 API 对 API 网关服务进行相关操作。

**术语表**

| 术语 | 全称 | 中文 | 说明 |
|---|---|---|---|
| Region |  | 地域 | 用户开放API，需选择API在API网关的部署地域，建议选择与后端服务相同的Region。 |
| API |  | 应用程序编程接口 | 用户开放API，在API网关录入API，以提供接口的方式对外提供服务或者数据。 |
| Group | API Group | API分组 | 一组API。 用户开放API，首先需要创建API分组每个API分组拥有一个二级域名，两个Stage 用户需要将已经备案且解析至分组二级域名的独立域名绑定到 API分组上同分组下的API均可通过已绑定的独立域名访问 |
| SubDomai n |  | 分组二级域名 | 用户开放API，创建的每个API分组都有一个二级域名，独立域名需要解析到该二级域名上，直接访问该域名可以调用测试环境的API。 |
| CustomDo main | Custom Domain | 域名 | 用户开放API，需要绑定自己的独立域名，该域名需要CNAME解析到分组二级域名上且在阿里云备案或备案接入。且若支持HTTPS协议，还需为域名上传SSL合规证书。 |
| Stage |  | 环境 | 用户开放API，创建的每个API分组目前有两个环境，测试和线上。 用户操作API发布到某个环境后，API才能被调用。区别在于，直接访问分组二级域名调用API，默认是调用测试环境。 |
| Signature | Backen d Signatu re | 后端签名密钥 | 用于开放API的用户给API网关颁发身份验证密钥。后端签名密钥绑定到API后对绑定的API即时生效。网关接收到这些API的请求，再去请求后端服务的时候就会带上签名信息，供后端服务对API网关做身份校验。 |
| TrafficCon trol |  | 流量控制策略 （简称“流控策略”） | 用于开放API的用户对API做访问流控。流控策略与API绑定后对绑定的API即时生效。流控策略可以从Api、App、User三个维度管控 API的调用。流控策略下还可以配置特殊流控，如某App/User在调用绑定的API时，可以按照特殊的值来流控。 |
| Special | Special Traffic Control | 特殊流量控制 （简称“特殊流控”） | 是流控策略的一个配置，可以指定某App/User，针对流控策略绑定的API，按照单独的值进行流控。 |
| APP |  | 应用 | 调用其他用户开放的API时，需要创建一个APP作为调用者的身份。 请求到达网关时，会对AppKey和AppSecret进行签名校验。 |

API 网关

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
API 网关
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

本文为您介绍调用流程及可以参考的文档资料。

**流程图**

API 网关

**调用步骤**

1. 获取AccessKey。

**说明**

推荐使用个人AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
3. 获取组织ID与资源集ID。

**说明**

调用API时，通过Header参数组织ID（<x-acs-organizationid>）和资源集ID（<x-acsresourcegroupid>）指定组织和资源集，实现实例资源的隔离查询。 组织ID（<x-acs-organizationid>）不指定则默认获取当前用户所属的组织。 资源集ID（<x-acs-resourcegroupid>）不指定默认为空，如果指定资源集需要同时指定组织ID。
4. 查找API的开发文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，查找开发指南的方式请参见开发文档使用说明。
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
API 网关

## 准备工作

### 登录API与工具控制台

**前提条件**

登录ASCM控制台前，确认您已从部署人员处获取ASCM控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入ASCM控制台的访问地址，按回车键。
2. 输入正确的用户名及密码。
请向运营管理员获取登录控制台的用户名和密码。 首次登录ASCM控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为

**说明**

提高安全性，密码长度必须为 8~20 位，且至少包含以下两种类型： 英文大写或小写字母（A~Z、a~z） 阿拉伯数字（0~9） 特殊符号（感叹号（！）、at（@）、井号（#）、美元符号（$）、百分号（%）等）
3. 单击**登录**，进入ASCM控制台页面。
4. 在页面顶部的菜单栏中，选择**产品** > **其他** **> API****与工具**。

### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。
API 网关

### 获取AccessKey

访问身份验证中通过使用AccessKey ID和AccessKey Secret对称加密的方法来验证某个请求的发送者身份。AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。本文将为您描述如何获取通过RAM授权的AccessKey。

**前提条件**

只有运营管理员和一级组织管理员可以获取组织AccessKey。

**背景信息**

AccessKey支持两种授权模式： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。 本文仅为您介绍如何获取通过RAM授权的AccessKey，通过STS授权的AccessKey获取方式请参见获取 STS AccessKey。 推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

API 网关个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，将鼠标悬停在当前登录用户的头像上，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。
Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

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

### 获取公共Header参数

调用API时需要提供多个Header参数。本文为您介绍如何获取这些参数。并对调用后的一些返回值做出解释。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理**>**地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看**Region****名称**，即为Region ID。

**获取组织ID**

组织ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取组织ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
API 网关
2. 单击顶部菜单栏**产品**，选择**应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，
调用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源
集ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节ListResourceGroup。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以API网关为例， 获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>应用服务>API网关。
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

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。 API 网关

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择利用STS方式，调用专有云的产品API。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 使用以下代码，通过角色的 `RAM Role` 获得 `stsAK` 、 `stsSK` 和 `stsToken` 。
API 网关

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
```

`//` 调用来源说明

```
        asClient.setSdkSource("test");
```

`//` 传入`Arn`

```
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
```

`//` 获取到`STS`三元组

```
        String stsAK = credentials.getString("AccessKeyId");
        String stsSK = credentials.getString("AccessKeySecret");
        String stsToken = credentials.getString("SecurityToken");
} public static String AssumeRole(ASClient asClient, String roleArn) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "AssumeRole");
        reqParams.put("Product", "Sts");
        reqParams.put("Version", "2015-04-01");
        reqParams.put("regionId", regionId);
```

`//` 当前登录用户的`ak`

```
        reqParams.put("AccessKeyId", <当前用户的AccessKey ID>);
```

`//` 当前登录用户的`sk`

```
        reqParams.put("AccessKeySecret", <当前用户的AccessKey Secret>);
        reqParams.put("roleSessionName", "StsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
}
```

3. 通过STS可以调用云产品的接口，下列代码以ECS为示例。
API 网关

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("test");
```

`//` 调用云产品的`API`

```
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
} public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, Str ing stsToken) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "DescribeZones");
        reqParams.put("Product", "Ecs");
        reqParams.put("Version", "2014-05-26");
        reqParams.put("regionId", "<your-RegionID>");
        //STS AK/SK/Token三元组
        reqParams.put("AccessKeyId", <stsAK>);
        reqParams.put("AccessKeySecret", <stsSK>);
        reqParams.put("SecurityToken", <stsToken>);
        return asClient.doRequest(endpoint, headers, reqParams, HttpMethod.GET);
    }
```

API 网关

## 通过POP网关调用专有云API

### 调用前置

阿里云专有云与公共云一样，可通过POP网关的方式进行API调用。本文为您介绍调用前需要进行的准备工作。

**背景信息**

为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

**获取云产品的Endpoint**

**通过开发者门户获取**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

**通过飞天基础运维平台获取**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。 您也可以自行获取Endpoint，本文以API网关为例为您介绍获取云产品业务域Endpoint的方法。
1. 登录Apsara Uni-manager运维控制台。
API 网关
2. 顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务注册变量大盘**。
4. 在服务注册变量大盘页面，单击**高级筛选**。
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
apigateway.openapi.endpoint值，即 `Endpoint` 。

**获取公共参数**

通过POP网关调用专有云API过程中所使用的参数，如组织ID、资源集ID、RegionID和实例ID，获取方式请

### Java版

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
```

API 网关 `//` 创建`DefaultAcsClient`实例并初始化。

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
```

API 网关

```java
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

`//`必填值，调用来源说明 API 网关 `//` 必填值，调用来源说明

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

### Go版

本文为您介绍POP Go SDK调用的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。
API 网关

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 示例代码如下： API 网关

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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： API 网关

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

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： API 网关

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

API 网关

### Python版

本文为您介绍POP Python SDK调用云产品API的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

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

API 网关
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
```

)

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # 使用https client.do_action_with_exception(request)
```

API 网关

**忽略证书**

**重要**

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL/TLS证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过参数 `verify` 设置。

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
```

`verify=False #` 忽略对 `SSL` 证书的验证 )

**指定CA证书文件**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    verify='./cacert.pem'  # 证书路径
```

) API 网关

## API 概览

| API | 描述 |
|---|---|
| CreateApiGroup | 创建API分组 |
| ModifyApiGroup | 修改API分组 |
| DeleteApiGroup | 删除API分组 |
| CreateApiStageVariable | 创建环境变量 |
| DeleteApiStageVariable | 删除环境变量 |
| DescribeApiStage | 查询指定环境详情 |
| DescribeApiGroup | 查询指定API分组详情 |
| DescribeApiGroups | 查询API分组列表 |

| API | 描述 |
|---|---|
| SetDomain | 绑定自定义域名 |
| SetDomainCertificate | 给指定自定义域名上传SSL证书 |
| DescribeDomain | 查询指定自定义域名详情信息 |
| DeleteDomain | 删除指定自定义域名 |
| DeleteDomainCertificate | 删除指定域名的证书 |

| API | 描述 |
|---|---|
| CreateApi | 创建API |
| ModifyApi | 修改API |
| DeployApi | 发布指定API到指定环境 |
| SwitchApi | 切换指定API在指定环境运行中的定义 |
| AbolishApi | 将指定环境的指定API下线 |
| DeleteApi | 删除指定Api定义 |
| DescribeApi | 查询指定API定义中的详情 |
| DescribeApis | 查询定义中的API列表 |

API 网关

| DescribeApiDoc | 查询指定API在指定环境中的调用说明（运行的定义） |
|---|---|
| DescribeDeployedApi | 查询指定API在指定环境中的运行定义 |
| DescribeDeployedApis | 查询指定环境中正在运行的API列表 |
| DescribeApiHistory | 查询指定API指定历史版本的定义 |
| DescribeApiHistories | 查询指定API指定历史版本列表 |

| API | 描述 |
|---|---|
| CreatePlugin | 创建插件 |
| ModifyPlugin | 修改插件 |
| DeletePlugin | 删除插件 |
| AttachPlugin | 插件绑定API |
| DetachPlugin | 解除插件与API的绑定 |
| DescribePluginApis | 查询插件下绑定的API |
| DescribePlugins | 查询插件列表及详情 |
| DescribePluginsByApi | 查询API上绑定的插件 |

**APP相关接口**

| API | 描述 |
|---|---|
| CreateApp | 创建应用 |
| ModifyApp | 修改应用 |
| ResetAppSecret | 重置指定APP密钥 |
| DescribeAppAttributes | 查询APP列表及基本属性 |
| DescribeAppSecurity | 查询指定APP密钥信息 |
| DeleteApp | 删除应用 |

| API | 描述 |
|---|---|
| DescribeApps | 查询可授权的APP列表 |
| DescribeAuthorizedApis | 查询指定APP已授权的API列表 |
| DescribeAuthorizedApps | 查询API的应用授权列表 |

API 网关

| SetApisAuthorities | 给指定APP添加多个API的访问权限 |
|---|---|
| SetAppsAuthorities | 给多个APP添加指定API的访问权限 |
| RemoveApisAuthorities | 批量撤销指定APP对多个API的访问权限 |
| RemoveAppsAuthorities | 批量撤销多个APP对指定API的访问权限 |

## 其他接口

| API | 描述 |
|---|---|
| DescribeRegions | 查询支持的区域列表 |
| DescribeSystemParameters | 查询系统参数列表 |

API 网关

## 签名机制

API网关服务会对每个访问的请求进行身份验证，所以无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。 API网关通过使用Access Key ID和Access Key Secret进行对称加密的方法来验证请求者身份。Access Key ID和Access Key Secret由阿里云官方颁发给访问者（可以通过阿里云官方网站申请和管理），其中： Access Key ID：用于标识访问者的身份 Access Key Secret：是用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密，只有阿里云和用户知道。 用户在访问时，按照下面的方法对请求进行签名处理：
1. 使用请求参数构造规范化的请求字符串（Canonicalized Query String）
按照参数名称的字典顺序对请求中所有的请求参数（包括文档中描述的“公共请求参数”和给定了的请求接口的自定义参数，但不能包括“公共请求参数”中提到Signature参数本身）进行排序。 当使用 `GET` 方法提交请求时，这些参数就是请求URI中的参数部分（即URI中“?”之

**说明**

后由“&”连接的部分）。 对每个请求参数的名称和值进行编码。名称和值要使用UTF-8字符集进行URL编码，URL编码的编码规则是： 对于字符 A-Z、a-z、0-9以及字符“-”、“_”、“.”、“~”不编码； 对于其他字符编码成“%XY”的格式，其中XY是字符对应ASCII码的16进制表示。比如英文的双引号 （”）对应的编码就是%22； 对于扩展的UTF-8字符，编码成“%XY%ZA…”的格式； 需要说明的是英文空格（）要被编码是%20，而不是加号（+）。 一般支持URL编码的库（比如Java中的java.net.URLEncoder）都是按

**说明**

照“application/x-www-form-urlencoded”的MIME类型的规则进行编码的。实现时可以直接使用这类方式进行编码，把编码后的字符串中加号（+）替换成%20、星号（*）替换成%2A、%7E 替换回波浪号（~），即可得到上述规则描述的编码字符串。 对编码后的参数名称和值使用**英文**等号（=）进行连接。 再把英文等号连接得到的字符串按参数名称的字典顺序依次使用&符号连接，即得到规范化请求字符串。
2. 使用上一步构造的规范化字符串按照下面的规则构造用于计算签名的字符串：

```
StringToSign= HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

其中： `HTTPMethod` 是提交请求用的HTTP方法，比如 `GET` 。 percentEncode(“/”) 是按照URL编码规则对字符“/”进行编码得到的值，即“%2F”。 `percentEncode(CanonicalizedQueryString)` 是对第1步中构造的规范化请求字符串按1.b中描述的URL编码规则编码后得到的字符串。
3. 按照RFC2104的定义，使用上面的用于签名的字符串计算签名HMAC值。注意：计算签名时使用的Key
就是用户持有的 Access Key Secret 并加上一个“&”字符(ASCII:38)，使用的哈希算法是SHA1。
4. 按照Base64编码规则把上面的HMAC值编码成字符串，即得到签名值（Signature）。
5. 将得到的签名值作为Signature参数添加到请求参数中，即完成对请求签名的过程。
API 网关得到的签名值在作为最后的请求参数值提交给API网关服务器的时候，要和其他参数一

**说明**

样，按照RFC3986的规则进行URL编码）。

```
http://apigateway.[RegionId].aliyuncs.com? Format=json&AccessKeyId=testid&Action=DescribeRegions&SignatureMethod=Hmac- SHA1&SignatureNonce=d48e931b-90c9-49c7-ac86a70dd3607c88&SignatureVersion=1.0&Version=2016-07-14&Timestamp=2016-09-27T09%3A08%3A30Z
```

那么StringToSign就是：

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeRegions%26Format%3Djson%26SignatureMethod DHmac-SHA1%26SignatureNonce%3Dd48e931b-90c9-49c7-ac86a70dd3607c88%26SignatureVersion%3D1.0%26Timestamp%3D2016-09- 27T09%253A08%253A30Z%26Version%3D2016-07-14
```

假如使用的Access Key Id是 testid，Access Key Secret是testsecret，用于计算HMAC的Key就是 testsecret&，则计算得到的签名值是： DRdMb%2F1m7PeToGRBApTl3wThyOg%3D 签名后的请求URL为（注意增加了Signature参数）：

```
http://apigateway.[RegionId].aliyuncs.com? Signature=DRdMb%2F1m7PeToGRBApTl3wThyOg%3D&Format=json&AccessKeyId=testid&Action=Describe gions&SignatureMethod=Hmac-SHA1&SignatureNonce=d48e931b-90c9-49c7-ac86a70dd3607c88&SignatureVersion=1.0&Version=2016-07-14&Timestamp=2016-09-27T09%3A08%3A30Z
```

API 网关

## API 分组相关接口

### 创建API分组

**描述**

此功能面向API提供者。 系统自动给分组分配二级域名，用于测试API。 分组带有区域属性，后续创建API选择分组后就选择了区域，为减少网络延时，建议选择与后端服务相同的区域。 创建分组后，可为分组绑定已备案的自定义域名。 该接口调用的QPS限制为：单用户QPS不超过50。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 接口名称，系统规定参数，取值：CreateApiGroup。 |
| GroupN ame | Strin g | 是 | 分组名称，必须唯一，支持汉字、英文字母、数字、英文格式的下划线，必须以英文字母或汉字开头，4~50个字符。 |
| Descrip tion | Strin g | 是 | API分组描述，不超过180个字符。 |

**说明**

CreateApiGroup接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识。 |
| GroupID | String | API分组 ID，系统生成，全局唯一。 |
| GroupName | String | API分组名称。 |

API 网关

| SubDomain | String | 系统给分组绑定的二级域名，用于测试API调用。 |
|---|---|---|
| Description | String | API分组描述。 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=CreateApiGroup &GroupName=Weather &De scription=The weather informations. &<公共请求参数>
```

**返回示例**

XML格式

```xml
<CreateApiGroupResponse>
    <RequestId>FF3B7D81-66AE-47E0-BF69-157DCF187514</RequestId>
    <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
    <GroupName>Weather</GroupName>
    <SubDomain>523e8dc7bbe04613b5b1d726c2a7889d-cn-
hangzhou.alicloudapi.com</SubDomain>
    <Description>The weather informations</Description>
</CreateApiGroupResponse>
```

JSON格式

```json
{
  "RequestId": "FF3B7D81-66AE-47E0-BF69-157DCF187514",
  "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
  "GroupName": "Weather",
  "SubDomain": "523e8dc7bbe04613b5b1d726c2a7889d-cn-hangzhou.alicloudapi.com",
  "Description": "The weather informations"
 }
```

### 修改API分组

**描述**

用于修改已经存在的API分组的名称或者描述此功能面向API提供者。 该接口调用的QPS限制为：单用户QPS不超过50。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 接口名称，系统规定参数，取值：ModifyApiGroup。 |
| GroupI d | Strin g | 是 | API分组 ID，系统生成，全局唯一。 |

API 网关

| GroupN ame | Strin g | 否 | 分组名称，必须唯一，支持汉字、英文字母、数字、英文格式的下划线，必须以英文字母或汉字开头，4~50个字符，不传递表示不修改。 |
|---|---|---|---|
| Descrip tion | Strin g | 否 | 分组描述，不超过180个字符，不传递表示不修改。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |
| GroupID | String | API分组 ID，系统生成，全局唯一。 |
| GroupName | String | API分组名称 |
| SubDomain | String | 系统为API分组分配的二级域名。 |
| Description | String | API分组描述 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=ModifyApiGroup &Description=New weath er informations. &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &GroupName=NewWeather &<公共
```

请求参数>

**返回示例**

XML格式

```xml
<ModifyApiGroupResponse>
    <RequestId>4CF287C6-CE5B-477B-BE27-C48F99EADBC8</RequestId>
    <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
    <GroupName>NewWeather</GroupName>
    <SubDomain>523e8dc7bbe04613b5b1d726c2a7889d-cn-
hangzhou.alicloudapi.com</SubDomain>
    <Description>New weather informations.</Description>
</ModifyApiGroupResponse>
```

JSON格式

```json
{
    "RequestId": "4CF287C6-CE5B-477B-BE27-C48F99EADBC8",
    "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
    "GroupName": "NewWeather",
    "SubDomain":"523e8dc7bbe04613b5b1d726c2a7889d-cn-hangzhou.alicloudapi.com"
    "Description": "New weather informations."
}
```

### 删除API分组

**描述**

API 网关用于删除指定的API分组。 此功能面向API提供者。 分组下存在API时，分组不可删除，须先删除分组下的API。 删除分组后，系统分配给此分组的二级域名自动生效。 删除不存在的分组时，会返回删除成功。 该接口调用的QPS限制为：单用户QPS不超过50。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：DeleteApiGroup。 |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一。 |

**说明**

DeleteApiGroup接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DeleteApiGroup &GroupId=523e8dc7bbe04613b5b1d726c2a7889d
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DeleteApiGroupResponse>
    <RequestId>E8515BA6-81CD-4191-A7CF-C4FCDD3C0D99</RequestId>
</DeleteApiGroupResponse>
```

JSON格式 API 网关

```json
{
    "RequestId": "E8515BA6-81CD-4191-A7CF-C4FCDD3C0D99"
}
```

### 创建环境变量

**描述**

在某运行环境下增加变量。 此功能面向API提供者。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：CreateApiStageVariable。 |
| GroupId | String | 是 | API分组 ID |
| StageId | String | 是 | 环境 ID |
| VariableName | String | 是 | 变量名，区分大小写。 |
| VariableValue | String | 否 | 变量值 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=CreateApiStageVariable &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &StageId=6EF60BEC-0242-43AF-BB20-270359FB54A7 &VariableName=serverName &VariableValue=api.domain.com
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<CreateApiStageVariableResponse>
    <RequestId>03442A3D-3B7D-434C-8A95-A5FEB999B529</RequestId>
</CreateApiStageVariableResponse>
```

JSON格式 API 网关

```json
{
    "RequestId": "03442A3D-3B7D-434C-8A95-A5FEB999B529"
  }
```

### 删除环境的指定变量

**描述**

删除指定环境的指定变量。 此功能面向API提供者。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值： DeleteApiStageVariable。 |
| GroupId | String | 是 | API分组 ID |
| StageId | String | 是 | 环境 ID |
| VariableName | String | 是 | 变量名，区分大小写。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DeleteApiStageVariable &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &StageId=6EF60BEC-0242-43AF-BB20-270359FB54A7 &VariableName=serverName
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DeleteApiStageVariableResponse>
    <RequestId>03442A3D-3B7D-434C-8A95-A5FEB969B529</RequestId>
</DeleteApiStageVariableResponse>
```

JSON格式

```json
{
    "RequestId": "03442A3D-3B7D-434C-8A95-A5FEB969B529"
  }
```

API 网关

### 查询API分组详情

**描述**

用于查询API分组的详情信息，包含分组系统自动生成的二级域名、自定义域名及SSL证书信息。 此功能面向API提供者用于查询指定分组全部详情信息

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：DescribeApiGroup。 |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |
| GroupID | String | API分组 ID，系统生成，全局唯一。 |
| GroupName | String | API分组名称 |
| SubDomain | String | 系统为分组分配的二级域名 |
| Description | String | API分组描述 |
| CreatedTime | String | 创建时间，格林威治时间。 |
| ModifiedTime | String | 最后修改时间，格林威治时间。 |
| RegionId | String | 分组所在区域 |
| Status | String | 分组状态 NORMAL：正常 DELETE：删除 |
| BillingStatus | String | 计费状态 NORMAL：正常 LOCKED：欠费锁定 |
| IllegalStatus | String | 违法锁定 NORMAL：正常 LOCKED：违法锁定 |
| TrafficLimit | Integer | 分组最高QPS限制，默认500，可申请提高。 |
| CustomDomains | CustomDomain | 自定义域名信息 |
| StageItems | StageInfo | 运行环境信息 |

API 网关

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeApiGroup &GroupId=523e8dc7bbe04613b5b1d726c2a7889d
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DescribeApiGroupResponse>
    <RequestId>03442A3D-3B7D-434C-8A95-A5FEB989B519</RequestId>
    <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
    <GroupName>NewWeather</GroupName>
    <SubDomain>927d50c0f2e54b359919923d908bb015-cn-
hangzhou.alicloudapi.com</SubDomain>
    <Description>New weather informations.</Description>
    <CreatedTime>2016-08-01T06:53:02Z</CreatedTime>
    <ModifiedTime>2016-08-01T06:54:32Z</ModifiedTime>
    <Status>NORMAL</Status>
    <BillingStatus>NORMAL</BillingStatus>
    <IllegalStatus>NORMAL</IllegalStatus>
    <TrafficLimit>500</TrafficLimit>
            <DomainName>api.demo.com</DomainName>
            <CertificateId>6EF60BEC-0242-43AF-BB20-270359FB54A7</CertificateId>
            <CertificateName>myCertificate</CertificateName>
            <DomainNameResolution>RESOLVED</DomainNameResolution>
            <DomainStatus>BINDING</DomainStatus>
    <StageItems>
            <StageId>123e8dc7bbe01613b5b1d726c2a7887e</StageId>
            <StageName>RELEASE</StageName>
            <Description>MYRELEASE</Description>
            <StageId>123e8dc7bbe01613b5b1d726c2a7888e</StageId>
            <StageName>TEST</StageName>
            <Description>MYTEST</Description>
    </StageItems>
</DescribeApiGroupResponse>
```

JSON格式 API 网关

```json
{
    "RequestId": "03442A3D-3B7D-434C-8A95-A5FEB989B519",
    "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
    "GroupName": "NewWeather",
    "SubDomain": "927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com",
    "Description": "New weather informations.",
    "CreatedTime": "2016-08-01T06:53:02Z",
    "ModifiedTime": "2016-08-01T06:54:32Z",
    "RegionId": "cn-hangzhou",
    "Status": "NORMAL",
    "BillingStatus": "NORMAL",
    "IllegalStatus": "NORMAL",
    "TrafficLimit": "500",
        "DomainName": "api.demo.com",
        "CertificateId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "CertificateName": "myCertificate",
        "DomainNameResolution": "RESOLVED",
        "DomainStatus": "BINDING"
      }
    },
    "StageItems": {
        {
          "StageId": "123e8dc7bbe01613b5b1d726c2a7887e",
          "StageName": "RELEASE",
          "Description": "MYRELEASE"
        },
        {
          "StageId": "123e8dc7bbe01613b5b1d726c2a7888e",
          "StageName": "TEST",
          "Description": "MYTEST"
        }
```

]

```
    }
}
```

### 查询API分组列表

**描述**

用于查询当前存在的API分组列表及基本信息。 此功能面向API提供者。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：DescribeApiGroups。 |

API 网关

| GroupId | String | 否 | API分组 ID，系统生成，全局唯一。 |
|---|---|---|---|
| GroupName | String | 否 | API组名称中，可指定的关键字。 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1。 |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值50，默认值为10。 |

**说明**

DescribeApiGroups接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |
| TotalCount | Integer | 返回结果的总条数 |
| PageNumber | Integer | 返回指定的页码 |
| PageSize | Integer | 返回指定的每页条数 |
| ApiGroupAttributes | ApiGroupAttribute | 返回分组集合 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeApiGroups
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<DescribeApiGroupsResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
                <GroupId>be6d2abcc0dd4f749fc2d2edd6567164</GroupId>
                <GroupName>Traffic</GroupName>
                <SubDomain>be6d2abcc0dd4f749fc2d2edd6567164-cn-
hangzhou.alicloudapi.com</SubDomain>
                <Description>TrafficInformations.</Description>
                  <CreatedTime>2016-08-01T08:45:15Z</CreatedTime>
                  <ModifiedTime>2016-08-01T08:45:15Z</ModifiedTime>
                  <TrafficLimit>500</TrafficLimit>
                  <BillingStatus>NORMAL</BillingStatus>
                  <IllegalStatus>NORMAL</IllegalStatus>
                <GroupId>927d50c0f2e54b359919923d908bb015</GroupId>
                <GroupName>NewWeather</GroupName>
                  <SubDomain>927d50c0f2e54b359919923d908bb015-cn-
hangzhou.alicloudapi.com</SubDomain>
                  <Description>NewWeatherInformations.</Description>
                  <CreatedTime>2016-08-01T06:54:32Z</CreatedTime>
                  <ModifiedTime>2016-08-01T06:54:32Z</ModifiedTime>
                  <TrafficLimit>500</TrafficLimit>
                  <BillingStatus>NORMAL</BillingStatus>
                  <IllegalStatus>NORMAL</IllegalStatus>
</DescribeApiGroupsResponse>
```

JSON格式 API 网关

```json
 {
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
    "TotalCount": "2",
    "PageSize": "10",
    "PageNumber": "1",
        {
          "GroupId": "be6d2abcc0dd4f749fc2d2edd6567164",
          "GroupName": "Traffic",
          "SubDomain": "be6d2abcc0dd4f749fc2d2edd6567164-cn-
hangzhou.alicloudapi.com",
          "Description": "TrafficInformations.",
          "CreatedTime": "2016-08-01T08:45:15Z",
          "ModifiedTime": "2016-08-01T08:45:15Z",
          "RegionId": "cn-hangzhou",
          "TrafficLimit": "500",
          "BillingStatus": "NORMAL",
          "IllegalStatus": "NORMAL"
        },
        {
          "GroupId": "927d50c0f2e54b359919923d908bb015",
          "GroupName": "NewWeather",
          "SubDomain": "927d50c0f2e54b359919923d908bb015-cn-
hangzhou.alicloudapi.com",
          "Description": "NewWeatherInformations.",
          "CreatedTime": "2016-08-01T06:54:32Z",
          "ModifiedTime": "2016-08-01T06:54:32Z",
          "RegionId": "cn-hangzhou",
          "TrafficLimit": "500",
          "BillingStatus": "NORMAL",
          "IllegalStatus": "NORMAL"
        }
```

]

```
    }
}
```

### 查询环境详情

**描述**

用于查看API分组中某个运行环境的的详情信息： 此功能面向API提供者。 用于查询指定运行环境详情信息。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：DescribeApiStage。 |
| GroupId | String | 是 | API分组 ID |

API 网关

| StageId | String | 是 | 环境 ID |
|---|---|---|---|

**返回参数**

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |
| GroupID | String | API分组 ID |
| StageID | String | 环境 ID |
| StageName | String | 环境名称 |
| Description | String | 环境描述 |
| CreatedTime | String | 创建时间，格林威治时间。 |
| ModifiedTime | String | 最后修改时间，格林威治时间。 |
| Variables | VariableItem | 变量信息 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeApiStage &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &StageId=6EF60BEC-0242-43AF-BB20-270359FB54A7
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<DescribeApiStageResponse>
    <RequestId>03442A3D-3B7D-434C-8A95-A5FEB989B529</RequestId>
    <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
    <StageID>123e8dc7bbe01613b5b1d726c2a7887e</StageID>
    <StageName>RELEASE</StageName>
    <Description>myRELEASE</Description>
    <CreatedTime>2016-08-01T06:53:02Z</CreatedTime>
    <ModifiedTime>2016-08-01T06:54:32Z</ModifiedTime>
    <Status>NORMAL</Status>
    <BillingStatus>NORMAL</BillingStatus>
    <IllegalStatus>NORMAL</IllegalStatus>
    <TrafficLimit>500</TrafficLimit>
    <Variables>
        <VariableItem>
            <VariableName>serverName</VariableName>
            <VariableValue>api.domain.com</VariableValue>
        </VariableItem>
        <VariableItem>
            <VariableName>version</VariableName>
            <VariableValue>v1.0</VariableValue>
        </VariableItem>
    </Variables>
</DescribeApiStageResponse>
```

JSON格式

```json
{
    "RequestId": "03442A3D-3B7D-434C-8A95-A5FEB989B529",
    "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
    "StageID": "123e8dc7bbe01613b5b1d726c2a7887e",
    "StageName": "RELEASE",
    "Description": "myRELEASE",
    "CreatedTime": "2016-08-01T06:53:02Z",
    "ModifiedTime": "2016-08-01T06:54:32Z",
    "Status": "NORMAL",
    "BillingStatus": "NORMAL",
    "IllegalStatus": "NORMAL",
    "TrafficLimit": "500",
    "Variables": {
      "VariableItem": [
        {
          "VariableName": "serverName",
          "VariableValue": "api.domain.com"
        },
        {
          "VariableName": "version",
          "VariableValue": "v1.0"
        }
```

]

```
    }
  }
```

API 网关

### 创建模型

在API分组的模型管理中创建模型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ModelNam e | Strin g | Quer y | 是 | Test | 模型的名称，组内不许重复。 |
| GroupId | Strin g | Quer y | 是 | 30e792398d6c4569b04c 0e53a3494381 | 模型所属的分组编号。 |
| Schema | Strin g | Quer y | 是 | {"type":"object","properti es":{"id": {"format":"int64","maxim um":100,"exclusiveMaxim um":true,"type":"integer" },"name": {"maxLength":10,"type":" string"}}} | 模型的JSON Schema定义。 |
| Descriptio n | Strin g | Quer y | 否 | Model Description | 模型定义的描述。 |
| Action | Strin g | Quer y | 否 | CreateModel | 接口名称，取值： CreateModel。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Description | String | Model Description | 本次创建模型的描述。 |
| ModelName | String | Test | 本次创建模型的名称。 |
| CreatedTime | String | 2019-01- 29T09:33:01Z | 本次创建模型的创建时间。 |
| ModifiedTime | String | 2019-01- 29T09:33:01Z | 本次创建模型的最后修改时间。 |

API 网关

| RequestId | String | 4173F95B-360C- 460C-9F6C- 4A960B904411 | 请求ID。 |
|---|---|---|---|
| Schema | String | {\"type\":\"object\", \"properties\": {\"id\": {\"format\":\"int64\ ",\"maximum\":100 ,\"exclusiveMaximu m\":true,\"type\":\"i nteger\"},\"name\": {\"maxLength\":10, \"type\":\"string\"} }} | 本次创建模型的模型定义。 |
| RegionId | String | cn-qingdao | 本次创建模型的所属区域。 |
| ModelId | String | 766c0b9538a04bdf 974953b5576783b a | 本次创建模型的ID。 |
| ModelRef | String | https://apigateway. aliyun.com/models/ 30e792398d6c456 9b04c0e53a34943 81/766c0b9538a04 bdf974953b55767 83ba | 本次创建模型的URI。 |
| GroupId | String | 30e792398d6c456 9b04c0e53a34943 81 | 本次创建模型所属的分组编号。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateModel &ModelName=Test &GroupId=30e792398d6c4569b04c0e53a3494381 &Schema={"type":"object","properties":{"id": {"format":"int64","maximum":100,"exclusiveMaximum":true,"type":"integer"},"name":{"maxL ength":10,"type":"string"}}}
```

&公共请求参数正常返回示例 API 网关 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "Description":"Model Description",
 "ModelName":"Test",
 "CreatedTime":"2019-01-29T09:33:01Z",
 "ModifiedTime":"2019-01-29T09:33:01Z",
 "RequestId":"4173F95B-360C-460C-9F6C-4A960B904411",
 "Schema":"{\\\"type\\\":\\\"object\\\",\\\"properties\\\":{\\\"id\\\":
{\\\"format\\\":\\\"int64\\\",\\\"maximum\\\":100,\\\"exclusiveMaximum\\\":true,\\\"type\ ":\\\"integer\\\"},\\\"name\\\":{\\\"maxLength\\\":10,\\\"type\\\":\\\"string\\\"}}}",
 "RegionId":"cn-qingdao",
 "ModelId":"766c0b9538a04bdf974953b5576783ba",
"ModelRef":"https://apigateway.aliyun.com/models/30e792398d6c4569b04c0e53a3494381/766c0b9 8a04bdf974953b5576783ba",
 "GroupId":"30e792398d6c4569b04c0e53a3494381"
}
```

### 删除已有模型

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ModelNam e | Strin g | Quer y | 是 | Test | 模型的名称。 |
| GroupId | Strin g | Quer y | 是 | 30e792398d6c4569b04c 0e53a3494381 | 模型所属的分组编号。 |
| Action | Strin g | Quer y | 否 | DeleteModel | 接口名称，取值： DeleteModel。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

API 网关

| RequestId | String | 4173F95B-360C- 460C-9F6C- 4A960B904411 | 请求ID。 |
|---|---|---|---|

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"4173F95B-360C-460C-9F6C-4A960B904411"
}
```

API 网关

## 域名相关接口

### 绑定自定义域名

**描述**

此功能面向API提供者。 独立域名要CNAME解析到该分组的二级域名上，或者添加A记录到二级域名所在的IP上，后操作绑定。 若您需要将其他分组的独立域名变更到当前分组，需要先变更解析，才能成功绑定。 若为https协议，则需要同时绑定SSL证书，要求同时传递 CertificateName、CertificateBody、 PrivateKey三个请求参数。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：SetDomain。 |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一。 |
| DomainName | String | 是 | 自定义域名。 |
| CertificateName | String | 否 | SSL证书名称。 |
| CertificateBody | String | 否 | 证书内容。 |
| PrivateKey | String | 否 | 证书私钥。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |
| GroupID | String | API分组 ID，系统生成，全局唯一。 |
| DomainName | String | 自定义域名 |
| SubDomain | String | 系统给分组绑定的二级域名，用于测试API调用。 |
| DomainBindingStatus | String | 自定义域名绑定状态。BINDING：正常 |

**示例**

**请求示例**

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=SetDomain &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com
```

`&<`公共请求参数>

**返回示例**

API 网关 XML格式

```xml
<SetDomainResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
    <GroupId>927d50c0f2e54b359919923d908bb015</GroupId>
    <DomainName>api.demo.com</DomainName>
    <SubDomain>927d50c0f2e54b359919923d908bb015-cn-
hangzhou.alicloudapi.com</SubDomain>
    <DomainBindingStatus>BINDING</DomainBindingStatus>
</SetDomainResponse>
```

JSON格式

```json
{
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "GroupId": "927d50c0f2e54b359919923d908bb015",
    "DomainName": "api.abcdef.com",
    "SubDomain": "927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com",
    "DomainBindingStatus": "BINDING"
}
```

### 上传SSL证书

**描述**

此功能面向API提供者 SSL证书必须与域名匹配绑定SSL证书后，可提供基于HTTPS的API服务

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值： SetDomainCertificate |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一 |
| DomainName | String | 是 | 自定义域名 |
| CertificateName | String | 是 | SSL证书名称 |
| CertificateBody | String | 是 | 证书内容 |
| CertificatePrivateKey | String | 是 | 证书私钥 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

API 网关

**请求示例**

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=SetDomainCertificate &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com &CertificateName＝test_cert &CertificateBody＝-----BEGIN CERTIFICATE----- MIICaTCCAdICCQDLDvXtNkCrHjANBgkqhkiG9w0BAQUFADB5MQswCQYDVQQGEwJD TjELMAkGA1UECBMCWkoxCzAJBgNVBAcTAkhaMQ0wCwYDVQQKEwR0ZXN0MQ0wCwYD VQQLEwR0ZXN0MRQwEgYDVQQDEwthcGkuaWxhZC5jbjEcMBoGCSqGSIb3DQEJARYN dGVzdEB0ZXN0LmNvbTAeFw0xNjAzMzEwMzMxMTBaFw0yNjAzMjkwMzMxMTBaMHkx CzAJBgNVBAYTAkNOMQswCQYDVQQIEwJaSjELMAkGA1UEBxMCSFoxDTALBgNVBAoT BHRlc3QxDTALBgNVBAsTBHRlc3QxFDASBgNVBAMTC2FwaS5pbGFkLmNuMRwwGgYJ KoZIhvcNAQkBFg10ZXN0QHRlc3QuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB iQKBgQDFfPttxLedyMF+tk/9VIGIIQ90LEx6JwfuKX38aO8zlN3+KxU7kMXBLYN7 kB7yZDsHBo87wlxXXPg7FO+3HjEcWAy8FgBFNfrnLLjXEK23Lrkn/3AdVulQ+eEi oVfOokQ1PO7GYFZSo8UFvBzol2An/f2Sd/bey713/rIUVgUd7wIDAQABMA0GCSqG SIb3DQEBBQUAA4GBAAqj2TQ8jzbmN5IDM8fMOARKLQQK8qTgkrHMAMEq7PJwNRtK A05enhbgZKJVkYhYk5nccWb3XZuklm6KX/ImWM1zfxi9EjvdD6Xkvxd9RpdZwlod zu6LnGpfi0YFiIBY301sFp0ACPudUvE1tVckrqM/ONPNhHWEnkAT9DF84hEN -----END CERTIFICATE----- &CertificatePrivateKey＝-----BEGIN RSA PRIVATE KEY----- MIICXAIBAAKBgQDFfPttxLedyMF+tk/9VIGIIQ90LEx6JwfuKX38aO8zlN3+KxU7 kMXBLYN7kB7yZDsHBo87wlxXXPg7FO+3HjEcWAy8FgBFNfrnLLjXEK23Lrkn/3Ad VulQ+eEioVfOokQ1PO7GYFZSo8UFvBzol2An/f2Sd/bey713/rIUVgUd7wIDAQAB AoGAeBxKgvlYv5Mg8+MIBUhHO7b3wi1LGiPw882yfTiI+vM4jORBFqg3TgVTaWw/ FicVq3E23h6YsN2vb6eNH+8x6DtGGZFiaWqIubWGEFenct8GPnlNY6JnxDdLMoGT K0P0r4qMZD5gSRs4sGR/wcGdbCGvSaFrzEConLmsaSlgLTkCQQD5KVwvchG/pai0 o13LJ9F4TVSegt8roH6QO0SuEb4GiKqUlY+Q1+PIBMHS1VciBJGyAWreLJkZnfKK g80cDL6VAkEAyuiPBt4u9dc68qet9vgVAYBI95vyCvg2u+MdVJKFYKaqNEDXbeyV qsrlsJ46LCAsQiLpzdEyrOioGiW3yNo9cwJBAKkn0EMR0UToJcIFSy8aaFahQXqf 5P1MZ8BpzHXU68qpzA02AJLYTvdDa4dEeXRJ39QWrEQLySEgH0K0unJ5oIUCQDtp Ln+vTIa091CXYit+5f+jhTni0lL97GDFFhBuOllbU1irZ6iK7iOs9uXo3lWPMgZH XLfjuffAw3+sbYyEwhsCQEtkrLCYEi5PQ4Z2RjonIBWWgXs+hDkd6qe5QM4Asr5t SDX2p8U+SnvvzJ3HuLM2ZB3D8duKJHCrKwOjX7nlXHo= -----END RSA PRIVATE KEY-----
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<SetDomainCertificateResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
</SetDomainCertificateResponse>
```

JSON格式

```json
{
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
}
```

### 查询域名详情

API 网关

**描述**

用于查询您绑定的自定义域名详情信息，包含系统自动分配的二级域名、自定义域名和SSL证书信息。 此功能面向API提供者。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：DescribeDomain。 |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一。 |
| DomainName | String | 是 | 自定义域名 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |
| GroupID | String | API分组 ID，系统生成，全局唯一。 |
| DomainName | String | 自定义域名 |
| SubDomain | String | 系统为分组分配的二级域名 |
| CertificateId | String | SSL证书ID，系统自动生成唯一编号。 |
| CertificateName | String | SSL证书名称 |
| CertificateBody | String | 证书内容 |
| CertificatePrivateKey | String | 证书私钥 |
| DomainBindingStatus | String | 自定义域名绑定状态，取值： BINDING：正常 BOUND：未生效 |
| DomainCNAMEStatus | String | 域名解析情况，取值： RESOLVED：已解析 UNRESOLVED：未解析 |

**示例**

**请求示例**

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=DescribeDomain &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<DescribeDomainResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
    <GroupId>927d50c0f2e54b359919923d908bb015</GroupId>
    <SubDomain>927d50c0f2e54b359919923d908bb015-cn-
hangzhou.alicloudapi.com</SubDomain>
    <DomainName>api.demo.com</DomainName>
    <CertificateId>6EF60BEC-0242-43AF-BB20-270359FB54A7</CertificateId>
    <CertificateName>myCertificate</CertificateName>
    <CertificateBody>..</CertificateBody>
    <CertificatePrivateKey>..</CertificatePrivateKey>
    <DomainBindingStatus>BINDING</DomainBindingStatus>
    <DomainCNAMEStatus>RESOLVED</DomainCNAMEStatus>
</DescribeDomainResponse>
```

JSON格式

```json
{
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "GroupId": "927d50c0f2e54b359919923d908bb015",
    "SubDomain": "927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com",
    "DomainName": "api.demo.com",
    "CertificateId":"6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "CertificateName": "myCertificate",
    "CertificateBody":"..",
    "CertificatePrivateKey":"..",
    "DDomainBindingStatus": "BINDING",
    "DomainCNAMEStatus": "RESOLVED"
  }
```

### 删除域名

**描述**

用于解除绑定在分组的自定义域名此功能面向API提供者。 删除不存在的域名，会返回成功。 删除域名将会影响API的访问，删除前请确认影响，谨慎操作。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：DeleteDomain |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一 |
| DomainName | String | 是 | 自定义域名 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

API 网关

**示例**

**请求示例**

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=DeleteDomain &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DeleteDomainResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
</DeleteDomainResponse>
```

JSON格式

```json
{
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
}
```

### 删除域名证书

**描述**

用于删除指定域名的SSL证书此功能面向API提供者删除不存在的SSL证书，会返回成功。 指定的分组不存在，会报错：InvalidGroupId.NotFound。 删除SSL证书后，将不能支持HTTPS访问，请谨慎操作。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值： DeleteDomainCertificate |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一 |
| DomainName | String | 是 | 自定义域名 |
| CertificateId | String | 是 | SSL证书ID，系统自动生成的SSL证书的唯一标识 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

**请求示例**

API 网关

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=DeleteDomainCertificate &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com &CertificateId=6EF60BEC-0242-43AF-BB20-270359FB54A7
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DeleteDomainCertificateResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
</DeleteDomainCertificateResponse>
```

JSON格式

```json
{
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
}
```

API 网关

## API 管理相关接口

### 创建API

**描述**

新建一个API。 此接口面向开放API的用户。 同一个分组内API不允许重名。 同一个分组内Path不允许重复。 分组内只允许定义200个API。 该接口调用的QPS限制为：单用户QPS不超过50。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 操作接口名，系统规定参数，取值：CreateApi |
| GroupId | Strin g | 是 | 指定的分组编号 |
| ApiName | Strin g | 是 | 设置API的名称，组内不允许重复。支持汉字、英文、数字和下划线， 且只能以英文和汉字开头，4~50个字符。 |
| Visibility | Strin g | 是 | API是否公开，可以取值： PUBLIC：公开，如选择此类型，该API的线上环境定义，会在所有用户的控制台“发现API”页面可见。 PRIVATE：不公开，如选择此类型，当该组API在云市场上架时，私有类型的API不会上架 |
| Description | Strin g | 是 | API描述信息，最多180个字符 |

API 网关

| AuthType | Strin g | 是 | API安全认证类型，目前可以取值： APP：只允许已授权的APP调用 ANONYMOUS：允许匿名调用，设置为允许匿名调用需要注意： 任何能够获取该API服务信息的人，都将能够调用该API。网关不会对调用者做身份认证，也无法设置按用户的流量控制，若开放该API请设置好按API的流量控制。 “ANONYMOUS”API不建议上架云市场，网关无法对调用者区分计量，也无法限制调用次数，若所在分组要上架云市场，建议将该API转移至其他分组，或将类型设置为“私有”，或选择“阿里云 APP”认证方式。 APPOPENID：支持第三方账号认证OpenID Connect，而且只允许已授权的APP调用；当设置此项时，参数OpenIdConnectConfig为必传。 |
|---|---|---|---|
| OpenIdConne ctConfig | Strin g | 是 | 第三方账号认证OpenID Connect相关配置项，详情见OpenIdConnectConfig |
| RequestConfi g | Strin g | 是 | Consumer向网关发送API请求的相关配置项，详情见RequestConfig |
| ServiceConfi g | Strin g | 是 | 网关向后端服务发送API请求的相关配置项，详情见ServiceConfig |
| RequestPara meters | Strin g | 是 | Consumer向网关发送API请求的参数描述，详情见RequestParameter |
| ServicePara meters | Strin g | 是 | 网关向后端服务发送API请求的参数描述，详情见ServiceParameter |
| ServicePara metersMap | Strin g | 是 | Consumer向网关发送请求的参数和网关向后端服务发送的请求的参数的映射关系，详情见ServiceParameterMap |
| ResultType | Strin g | 是 | 后端服务返回应答的格式，目前可以设置为：JSON、TEXT、 BINARY、XML、HTML |
| ResultSampl e | Strin g | 是 | 后端服务返回应答的示例 |
| FailResultSa mple | Strin g | 否 | 后端服务失败返回应答的示例 |
| ErrorCodeSa mples | Strin g | 否 | 后端服务返回的错误码示例，详情见ErrorCodeSample |

API 网关

**说明**

CreateApi接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次创建API的请求Id |
| ApiId | String | 本次创建API的Id |

**示例**

**请求示例**

API 网关

```json
https://ecs.aliyuncs.com/?Action=CreateApi &GroupId=08ae4aa0f95e4321849ee57f4e0b3077 &ApiName=ApiName &Visibility=PUBLIC &Description=Api description &AuthType=APP {"RequestProtocol":"HTTP","RequestHttpMethod":"GET","RequestPath":"/v3/getUserTest/[userI ","BodyFormat":"FORM","PostBodyDescription":""} {"ServiceProtocol":"HTTP","ServiceHttpMethod":"GET","ServiceAddress":"http://www.customer main.com","ServiceTimeout":"1000","ServicePath":"/v3/getUserTest/[userId]"} [{"ParameterType":"Number","Required":"OPTIONAL","isHide":false,"ApiParameterName":"age", efaultValue":"20","DemoValue":"20","Description":"年龄","MinValue":18,"MaxValue":100,"Location":"Head"}, {"ParameterType":"String","Required":"OPTIONAL","isHide":false,"ApiParameterName":"sex"," faultValue":"boy","DemoValue":"boy","Description":"性别","EnumValue":"boy,girl","Location":"Query"}, {"ParameterType":"Number","Required":"REQUIRED","isHide":false,"ApiParameterName":"userId "MaxLength":10,"MinValue":10000000,"MaxValue":100000000,"Location":"Path"}, {"ApiParameterName":"CaClientIp","ParameterLocation": {"name":"Head","orderNumber":0},"Location":"Head","ParameterType":"String","Required":"RE IRED","Description":"客户端IP"},{"ApiParameterName":"constance","ParameterLocation":{"na me":"Head","orderNumber":0},"Location":"Head","ParameterType":"String","Required":"REQUIR ","DefaultValue":"constance","Description":"constance"}] [{"ServiceParameterName":"age","Location":"Head","Type":"Number","ParameterCatalog":"REQU T"}, {"ServiceParameterName":"sex","Location":"Query","Type":"String","ParameterCatalog":"REQU T"}, {"ServiceParameterName":"userId","Location":"Path","Type":"Number","ParameterCatalog":"RE EST"}, {"ServiceParameterName":"clientIp","Location":"Head","Type":"String","ParameterCatalog":" STEM"}, {"ServiceParameterName":"constance","Location":"Head","Type":"String","ParameterCatalog": ONSTANT"}] &ServiceParametersMap=[{"ServiceParameterName":"age","RequestParameterName":"age"},{"Se rviceParameterName":"sex","RequestParameterName":"sex"}, {"ServiceParameterName":"userId","RequestParameterName":"userId"}, {"ServiceParameterName":"clientIp","RequestParameterName":"CaClientIp"}, {"ServiceParameterName":"constance","RequestParameterName":"constance"}] &ResultType=HTML &ResultSample=200
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<CreateApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
    <ApiId>8afff6c8c4c6447abb035812e4d66b65</ApiId>
</CreateApiResponse>
```

JSON格式

```json
{
    "RequestId":"6C87A26A-6A18-4B8E-8099-705278381A2C",
    "ApiId":"8afff6c8c4c6447abb035812e4d66b65"
}
```

### 修改API

**描述**

此接口面向开放API的用户修改RequestPath时需要注意，同一个分组内Path不允许重复。 该接口调用的QPS限制为：单用户QPS不超过50。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：ModifyApi |
| GroupId | String | 是 | 指定的分组编号 |
| ApiId | String | 是 | API的Id标识 |
| ApiName | String | 是 | API的名称，组内不允许重复。支持汉字、英文、数字和下划线，且只能以英文和汉字开头，4~50个字符 |
| Visibility | String | 是 | API是否公开，目前可以取值： PUBLIC：公开，如选择此类型，该API的线上环境，会在所有用户的控制台“发现API”页面展示 PRIVATE：不公开，如选择此类型，当该组API在云市场上架时，私有类型的API不会上架 |
| Description | String | 是 | API描述信息，最多180个字符 |

API 网关

| AuthType | String | 是 | API安全认证类型，目前可以取值： APP：只允许已授权的APP调用 ANONYMOUS：允许匿名调用，设置为允许匿名调用需要注意： 任何能够获取该API服务信息的人，都将能够调用该API。网关不会对调用者做身份认证，也无法设置按用户的流量控制，若开放该API请设置好按API的流量控制。 “ANONYMOUS”API不建议上架云市场，网关无法对调用者区分计量， 也无法限制调用次数，若所在分组要上架云市场，建议将该API转移至其他分组，或将类型设置为“私有”，或选择“阿里云APP”认证方式。 APPOPENID：支持第三方账号认证OpenID Connect，而且只允许已授权的APP调用；当设置此项时，参数OpenIdConnectConfig为必传。 |
|---|---|---|---|
| OpenIdConne ctConfig | String | 是 | 第三方账号认证OpenID Connect相关配置项，详情见 ApiAttributesType.md#OpenIdConnectConfig |
| RequestConfi g | String | 是 | Consumer向网关发送API请求的相关配置项，详情见 ApiAttributesType.md#RequestConfig |
| ServiceConfi g | String | 是 | 网关向后端服务发送API请求的相关配置项，详情见 ApiAttributesType.md#ServiceConfig |
| RequestPara meters | String | 是 | Consumer向网关发送API请求的参数描述，详情见 ApiAttributesType.md#RequestParameters |
| ServicePara meters | String | 是 | 网关向后端服务发送API请求的参数描述，详情见 ApiAttributesType.md#ServiceParameters |
| ServicePara metersMap | String | 是 | Consumer向网关发送请求的参数和网关向后端服务发送的请求的参数的映射关系，详情见ApiAttributesType.md#ServiceParametersMap |
| ResultType | String | 是 | 后端服务返回应答的格式，目前可以设置为：JSON、TEXT、BINARY、 XML、HTML |
| ResultSampl e | String | 是 | 后端服务返回应答的示例 |
| FailResultSa mple | String | 否 | 后端服务失败返回应答的示例 |
| ErrorCodeSa mples | String | 否 | 后端服务返回的错误码示例，详情见 ApiAttributesType.md#ErrorCodeSamples |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次创建API的请求Id |

**示例**

**请求示例**

API 网关

```json
https://ecs.aliyuncs.com/?Action=ModifyApi &GroupId=08ae4aa0f95e4321849ee57f4e0b3077 &ApiName=ApiName &ApiId=8afff6c8c4c6447abb035812e4d66b65 &Visibility=PUBLIC &Description=Api description &AuthType=APP {"RequestProtocol":"HTTP","RequestHttpMethod":"GET","RequestPath":"/v3/getUserTest/[userI ","BodyFormat":"FORM","PostBodyDescription":""} {"ServiceProtocol":"HTTP","ServiceHttpMethod":"GET","ServiceAddress":"http://www.customer main.com","ServiceTimeout":"1000","ServicePath":"/v3/getUserTest/[userId]"} &RequestParameters=[{"ParameterLocation": {"name":"Head","orderNumber":1},"ParameterType":"Number","Required":"OPTIONAL","isHide":f se,"ApiParameterName":"age","DefaultValue":"20","DemoValue":"20","Description":“年龄”,"M inValue":18,"MaxValue":100,"Location":"Head"},{"ParameterLocation": {"name":"Query","orderNumber":2},"ParameterType":"String","Required":"OPTIONAL","isHide": lse,"ApiParameterName":"sex","DefaultValue":"boy","DemoValue":"boy","Description":“性别” ,"EnumValue":"boy,girl","Location":"Query"},{"ParameterLocation":{"name":"Parameter Pat h","orderNumber":3},"ParameterType":"Number","Required":"REQUIRED","isHide":false,"ApiPar eterName":"userId","MaxLength":10,"MinValue":10000000,"MaxValue":100000000,"Location":"Pa "},{"ApiParameterName":"CaClientIp","ParameterLocation": {"name":"Head","orderNumber":0},"Location":"Head","ParameterType":"String","Required":"RE IRED","Description":“客户端IP”},{"ApiParameterName":"constance","ParameterLocation":{"na me":"Head","orderNumber":0},"Location":"Head","ParameterType":"String","Required":"REQUIR ","DefaultValue":"constance","Description":"constance"}] [{"ServiceParameterName":"age","Location":"Head","Type":"Number","ParameterCatalog":"REQU T"}, {"ServiceParameterName":"sex","Location":"Query","Type":"String","ParameterCatalog":"REQU T"}, {"ServiceParameterName":"userId","Location":"Path","Type":"Number","ParameterCatalog":"RE EST"}, {"ServiceParameterName":"clientIp","Location":"Head","Type":"String","ParameterCatalog":" STEM"}, {"ServiceParameterName":"constance","Location":"Head","Type":"String","ParameterCatalog": ONSTANT"}] &ServiceParametersMap=[{"ServiceParameterName":"age","RequestParameterName":"age"},{"Se rviceParameterName":"sex","RequestParameterName":"sex"}, {"ServiceParameterName":"userId","RequestParameterName":"userId"}, {"ServiceParameterName":"clientIp","RequestParameterName":"CaClientIp"}, {"ServiceParameterName":"constance","RequestParameterName":"constance"}] &ResultType=HTML &ResultSample=200
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<ModifyApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</ModifyApiResponse>
```

JSON格式

```json
{
    "RequestId":"6C87A26A-6A18-4B8E-8099-705278381A2C"
}
```

### 发布API

**描述**

此功能面向开放API的用户，定义的API只有发布到运行环境，才能被调用 API发布到集群里需要一定的时间，最长5秒后生效该接口调用的QPS限制为：单用户QPS不超过50

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DeployApi |
| GroupId | String | 是 | 分组编号 |
| ApiId | String | 是 | API编号 |
| StageName | String | 是 | 运行环境名称，取值： RELEASE: 线上 TEST: 测试 |
| Description | String | 是 | 本次发布备注说明 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DeployApi &GroupId=63be9002440b4778a61122f14c2b2bbb &ApiId=d6f679aeb3be4b91b3688e887ca1fe16 &StageName=release &Description=for_test1
```

`&<`公共请求参数>

**返回示例**

格式 API 网关 XML格式

```xml
<DeployApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</DeployApiResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015"
}
```

### 快速切换API版本

**描述**

用指定历史版本切换掉指定环境中正在运行中的API定义，即用历史定义替换运行中定义。 此功能面向开放API的用户历史版本号可通过DescribeHistoryApis接口获取发布超过1次的API才可以切换切换针对的是运行中API，切换操作不可逆且迅速生效，需谨慎；切换有一定的延迟性，最长不超过5s。 切换本质上也是一次发布操作，需要说明切换的原因。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：SwitchApi |
| GroupId | String | 是 | 分组编号 |
| ApiId | String | 是 | API编号 |
| StageName | String | 是 | 运行环境名称，取值： RELEASE: 线上 TEST: 测试 |
| HistoryVersion | String | 是 | 指定要切换到的历史版本号 |
| Description | String | 是 | 切换备注 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

API 网关

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=SwitchApi &GroupId=63be9002440b4778a61122f14c2b2bbb &ApiId=d6f679aeb3be4b91b3688e887ca1fe16 &StageName=release &HistoryVersion=20160705104552292 &Description=for_demo
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<SwitchApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ001</RequestId>
</SwitchApiResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ001"
}
```

### 下线API

**描述**

下线指定运行环境的指定API 将指定环境中运行的指定API从运行环境里摘除，需要一定的时间，最长不超过5s。 API下线后将不能被调用（指定环境）

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：AbolishApi |
| GroupId | String | 是 | 指定分组编号 |
| ApiId | String | 是 | 指定API编号 |
| StageName | String | 是 | 运行环境名称，取值： RELEASE: 线上 TEST: 测试 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

API 网关

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=AbolishApi &GroupId=63be9002440b4778a61122f14c2b2bbb &ApiId=d6f679aeb3be4b91b3688e887ca1fe16 &StageName=RELEASE
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<AbolishApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ016</RequestId>
</AbolishApiResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ016"
}
```

### 删除API定义

**描述**

删除指定的API定义此功能面向开放API的用户，此操作不可逆 API在运行环境中运行，则不允许删除，需要先调用AbolishApi操作下线该接口调用的QPS限制为：单用户QPS不超过50

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DeleteApi |
| GroupId | String | 是 | 分组编号 |
| ApiId | String | 是 | API编号 |

**说明**

DeleteApi接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

**返回参数**

API 网关

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DeleteApi &GroupId=63be9002440b4778a61122f14c2b2bbb &ApiId=d6f679aeb3be4b91b3688e887ca1fe16
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DeleteApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ017</RequestId>
</DeleteApiResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ017"
}
```

### 查询API定义

**描述**

此接口面向开放API的用户用于查询指定API的定义

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeApi |
| GroupId | String | 是 | API所在的分组编号 |
| ApiId | String | 是 | API的Id标识 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次创建API的请求Id |
| RegionId | String | API所处的Region的Id |

API 网关

| ApiId | String | API的Id标识 |
|---|---|---|
| ApiName | String | API的名称，组内不允许重复 |
| GroupId | String | API所在的分组编号 |
| GroupName | String | API所在的分组名称 |
| Visibility | String | API是否公开，目前可以取值： PUBLIC：公开，如选择此类型，该API的线上环境，会在所有用户的控制台“发现API”页面展示 PRIVATE：不公开，如选择此类型，当该组API在云市场上架时，私有类型的API不会上架 |
| AuthType | String | API安全认证类型，目前可以取值： APP：只允许已授权的APP调用 ANONYMOUS：允许匿名调用，设置为允许匿名调用需要注意： 任何能够获取该API服务信息的人，都将能够调用该API。网关不会对调用者做身份认证，也无法设置按用户的流量控制，若开放该API请设置好按API的流量控制。 “ANONYMOUS”API不建议上架云市场，网关无法对调用者区分计量，也无法限制调用次数，若所在分组要上架云市场，建议将该API 转移至其他分组，或将类型设置为“私有”，或选择“阿里云APP”认证方式。 APPOPENID：支持第三方账号认证OpenID Connect，而且只允许已授权的APP调用；当设置此项时，参数OpenIdConnectConfig为必传。 |
| ResultType | String | 后端服务返回应答的格式，目前可以设置为：JSON、TEXT、BINARY、 XML、HTML |
| ResultSample | String | 后端服务返回应答的示例 |
| FailResultSam ple | String | 后端服务失败返回应答的示例 |
| CreateTime | String | API创建的时间 |
| ModifyTime | String | API最后一次修改的时间 |
| Description | String | API描述信息 |
| ErrorCodeSa mples | ErrorCodeSampl e | 后端服务返回的错误码示例，详情见 ApiAttributesType.md#ErrorCodeSamples |
| SystemParam eters | SystemParamet er | 网关发送给后端服务的系统参数，详情见 ApiAttributesType.md#SystemParameters |
| ConstantPara meters | ConstantParame ter | 网关发送给后端服务的常量参数，详情见 ApiAttributesType.md#ConstantParameters |
| RequestPara metersObject | RequestParame ter | Consumer向网关发送API请求的参数描述，详情见 ApiAttributesType.md#RequestParameters |
| ServiceParam etersObject | ServiceParamet er | 网关向后端服务发送API请求的参数描述，详情见 ApiAttributesType.md#ServiceParameters |

API 网关

| ParametersMa pObject | ServiceParamet erMap | Consumer向网关发送请求的参数和网关向后端服务发送的请求的参数的映射关系，详情见ApiAttributesType.md#ServiceParametersMap |
|---|---|---|
| DeployedInfos | DeployedInfo | API发布状态，详情见ApiAttributesType.md#DeployedInfos |
| RequestConfi g | RequestConfig | Consumer向网关发送API请求的相关配置项，详情见 ApiAttributesType.md#RequestConfig |
| ServiceConfig | ServiceConfig | 网关向后端服务发送API请求的相关配置项，详情见 ApiAttributesType.md#ServiceConfig |
| OpenIdConne ctConfig | OpenIdConnect Config | 第三方账号认证OpenID Connect相关配置项，详情见 ApiAttributesType.md#OpenIdConnectConfig |

**示例**

**请求示例**

```
https://ecs.aliyuncs.com/?Action=DescribeApi &GroupId=08ae4aa0f95e4321849ee57f4e0b3077 &ApiId=8afff6c8c4c6447abb035812e4d66b65
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DescribeApiResponse>
    <RequestId>D0FF585F-7966-40CF-BC60-75DB070B23D5</RequestId>
    <Description>Api description</Description>
    <ApiName>ApiName</ApiName>
    <CreatedTime>2016-07-28T09:50:43Z</CreatedTime>
    <GroupName>ApiTest</GroupName>
    <ModifiedTime>2016-07-28T13:13:12Z</ModifiedTime>
        <ServiceParam>
            <ServiceParameterName>age</ServiceParameterName>
            <Type>Number</Type>
            <Location>head</Location>
        </ServiceParam>
        <ServiceParam>
            <ServiceParameterName>sex</ServiceParameterName>
            <Type>String</Type>
            <Location>query</Location>
        </ServiceParam>
        <ServiceParam>
            <ServiceParameterName>userId</ServiceParameterName>
            <Type>Number</Type>
            <Location>path</Location>
        </ServiceParam>
        <ServiceParam>
            <ServiceParameterName>clientIp</ServiceParameterName>
            <Type>String</Type>
            <Location>head</Location>
        </ServiceParam>
```

API 网关

```xml
        <ServiceParam>
            <ServiceParameterName>constance</ServiceParameterName>
            <Type>String</Type>
            <Location>head</Location>
        </ServiceParam>
            <ServiceParameterName>constance</ServiceParameterName>
            <Description>constance</Description>
            <Location>HEAD</Location>
            <ConstantValue>constance</ConstantValue>
    <GroupId>08ae4aa0f95e4321849ee57f4e0b3077</GroupId>
            <ServiceParameterName>clientIp</ServiceParameterName>
            <Description>客户端IP</Description>
            <DemoValue>192.168.1.1</DemoValue>
            <Location>HEAD</Location>
            <ParameterName>CaClientIp</ParameterName>
        <RequestParam>
            <Required>OPTIONAL</Required>
            <MinValue>18</MinValue>
            <Description>年龄</Description>
            <DemoValue>20</DemoValue>
            <ParameterType>NUMBER</ParameterType>
            <ApiParameterName>age</ApiParameterName>
            <DocShow>PUBLIC</DocShow>
            <DefaultValue>20</DefaultValue>
            <Location>HEAD</Location>
            <MaxValue>100</MaxValue>
            <DocOrder>0</DocOrder>
        </RequestParam>
        <RequestParam>
            <Required>OPTIONAL</Required>
            <Description>性别</Description>
            <DemoValue>boy</DemoValue>
            <ParameterType>STRING</ParameterType>
            <ApiParameterName>sex</ApiParameterName>
            <DocShow>PUBLIC</DocShow>
            <DefaultValue>boy</DefaultValue>
            <Location>QUERY</Location>
            <EnumValue>boy,girl</EnumValue>
            <DocOrder>0</DocOrder>
        </RequestParam>
        <RequestParam>
            <Required>REQUIRED</Required>
            <MinValue>10000000</MinValue>
            <ParameterType>NUMBER</ParameterType>
```

API 网关

```xml
            <ApiParameterName>userId</ApiParameterName>
            <DocShow>PUBLIC</DocShow>
            <Location>PATH</Location>
            <MaxValue>100000000</MaxValue>
            <DocOrder>0</DocOrder>
        </RequestParam>
            <DeployedStatus>NONDEPLOYED</DeployedStatus>
            <StageName>TEST</StageName>
            <DeployedStatus>NONDEPLOYED</DeployedStatus>
            <StageName>RELEASE</StageName>
        <ServiceProtocol>HTTP</ServiceProtocol>
        <ServiceTimeout>1000</ServiceTimeout>
        <ServiceAddress>http://www.customerdomain.com</ServiceAddress>
        <ServicePath>/v3/getUserTest/[userId]</ServicePath>
        <ServiceHttpMethod>GET</ServiceHttpMethod>
        <Mock>FALSE</Mock>
    <RequestId>D0FF585F-7966-40CF-BC60-75DB070B23D5</RequestId>
        <RequestHttpMethod>GET</RequestHttpMethod>
        <RequestProtocol>HTTP</RequestProtocol>
        <RequestPath>/v3/getUserTest/[userId]</RequestPath>
    <Visibility>PUBLIC</Visibility>
    <ParametersMapObject>
            <ServiceParameterName>sex</ServiceParameterName>
            <RequestParameterName>sex</RequestParameterName>
            <ServiceParameterName>age</ServiceParameterName>
            <RequestParameterName>age</RequestParameterName>
            <ServiceParameterName>userId</ServiceParameterName>
            <RequestParameterName>userId</RequestParameterName>
    </ParametersMapObject>
            <Code>400</Code>
            <Message>Missing the parameter UserId</Message>
```

`<Description>`请求缺少参数 `UserId</Description>`

```xml
<AiId>8fff6846447bb0358124d66b65</AiId>
```

API 网关

```xml
    <ApiId>8afff6c8c4c6447abb035812e4d66b65</ApiId>
    <AuthType>APP</AuthType>
    <ResultType>HTML</ResultType>
    <ResultSample>200</ResultSample>
    <FailResultSample>400</FailResultSample>
    <OpenIdConnectConfig>
        <publicKey>EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92</publicKey>
        <openIdApiType>IDTOKEN</openIdApiType>
        <publicKeyId>88483727556929326703309904351185815489</publicKeyId>
    </OpenIdConnectConfig>
</DescribeApiResponse>
```

JSON格式

```json
{
    "RequestId":D0FF585F-7966-40CF-BC60-75DB070B23D5,
    "RegionId":cn-qingdao,
    "Description": "billingTest001",
    "ApiName": "billingTest001",
    "CreatedTime": "2016-07-01T09:18:20Z",
    "GroupName": "billingTest",
    "ModifiedTime": "2016-07-21T03:52:12Z",
        "ServiceParam": [
            {
                "ServiceParameterName": "headerParam",
                "Type": "String",
                "Location": "head"
            },
            {
                "ServiceParameterName": "queryparam",
                "Type": "String",
                "Location": "query"
            },
            {
                "ServiceParameterName": "NumberParam",
                "Type": "Number",
                "Location": "query"
            },
            {
                "ServiceParameterName": "type",
                "Type": "String",
                "Location": "path"
            },
            {
                "ServiceParameterName": "clientIp",
                "Type": "String",
                "Location": "head"
            },
            {
                "ServiceParameterName": "constantParam",
                "Type": "String",
                "Location": "query"
            }
```

] API 网关

```json
    },
            {
                "ServiceParameterName": "constantParam",
                "Description": "constant",
                "Location": "QUERY",
                "ConstantValue": "constant"
            }
```

]

```json
    },
    "GroupId": "4a3f3050b9c5469bb685bdd29e571be1",
            {
                "ServiceParameterName": "clientIp",
                "Description": "客户端IP",
                "DemoValue": "192.168.1.1",
                "Location": "HEAD",
                "ParameterName": "CaClientIp"
            }
```

]

```json
    },
        "RequestParam": [
            {
                "Required": "OPTIONAL",
                "Description": "head param",
                "DemoValue": "headparm",
                "ParameterType": "STRING",
                "ApiParameterName": "headerParam",
                "DocShow": "PUBLIC",
                "DefaultValue": "",
                "Location": "HEAD",
                "EnumValue": "head",
                "DocOrder": 0
            },
            {
                "Required": "REQUIRED",
                "ParameterType": "STRING",
                "ApiParameterName": "queryparam",
                "DocShow": "PUBLIC",
                "DefaultValue": "",
                "Location": "QUERY",
                "DocOrder": 0
            },
            {
                "Required": "OPTIONAL",
                "MinValue": 1,
                "Description": "number param",
                "DemoValue": "10",
                "ParameterType": "NUMBER",
                "ApiParameterName": "NumberParam",
                "DocShow": "PUBLIC",
```

API 网关

```json
                "DefaultValue": "10",
                "Location": "QUERY",
                "MaxValue": 100,
                "DocOrder": 0
            },
            {
                "Required": "REQUIRED",
                "ParameterType": "STRING",
                "ApiParameterName": "type",
                "DocShow": "PUBLIC",
                "Location": "PATH",
                "DocOrder": 0
            }
```

]

```json
    },
            {
                "DeployedStatus": "NONDEPLOYED",
                "StageName": "TEST"
            },
            {
                "DeployedStatus": "DEPLOYED",
                "StageName": "RELEASE",
                "EffectiveVersion": "20160721115223375"
            }
```

]

```json
    },
        "ServiceProtocol": "HTTP",
        "ServiceTimeout": 10000,
        "ServiceAddress": "http://120.55.69.157:8080",
        "ServicePath": "/web/cloudapi/[type]",
        "ServiceHttpMethod": "POST",
        "Mock": "CLOSED"
    },
    "RequestId": "415F037A-94C2-4100-B17A-F3C514CA1391",
    "RegionId": "cn-qingdao",
        "RequestHttpMethod": "POST",
        "RequestProtocol": "HTTP",
        "PostBodyDescription": "fwefwef",
        "BodyFormat": "STREAM",
        "RequestPath": "/api/billing/test/[type]"
    },
    "Visibility": "PUBLIC",
    "ParametersMapObject": {
            {
                "ServiceParameterName": "headerParam",
            },
            {
                "ServiceParameterName": "queryparam",
```

`"R` `tP` t N " " " API 网关

```json
            },
            {
                "ServiceParameterName": "NumberParam",
            },
            {
                "ServiceParameterName": "type",
            }
```

]

```json
    },
            {
                "Code": "400",
                "Message": "Missing the parameter UserId",
```

`"Description": "`请求缺少参数 `UserId"`

```
            }
```

]

```json
    },
    "ApiId": "e77fd9257b1d436a806fe23c649300a0",
    "AuthType": "APP",
    "ResultType": "JSON",
    "ResultSample": "fwef",
    "FailResultSample": "400",
    "OpenIdConnectConfig": {
        "publicKey": "EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92",
        "openIdApiType": "IDTOKEN",
        "publicKeyId": "88483727556929326703309904351185815489"
    }
}
```

### 查询API服务文档

**描述**

查询指定API的服务说明文档。 此功能面向调用API的用户，指定的API必须是发布到运行环境，且Visibility=PUBLIC的API或者被授权的Visibility=PRIVATE的API 若您是调用API的用户，该接口返回您指定的API的服务信息及参数定义等详情信息。 若您是开放API的用户，那么调用该接口可以查看当前指定API在指定环境中运行的定义，可能与您现在修改中的API定义不同，是真正在环境中生效的定义。 若您是开放API的用户，由于该接口面向API调用者鉴权，所以您需要确认该API为PUBLIC类型或者您的相关APP已被授权。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeApiDoc |
| GroupId | String | 是 | 指定的分组编号 |

API 网关

| ApiId | String | 是 | 指定的API编号 |
|---|---|---|---|
| StageName | String | 否 | 环境名称，可选值： RELEASE: 线上 TEST: 测试若不传入，则默认为release。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| RegionId | String | 所在的region |
| GroupId | String | API分组编号 |
| GroupName | String | API分组名称 |
| StageName | String | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |
| ApiId | String | API编号 |
| ApiName | String | API名称 |
| Description | String | API描述 |
| Visibility | String | 可见性，取值为：PUBLIC、PRIVATE，分别表示公开、私有 |
| AuthType | String | 安全认证方式，取值为：APP、ANONYMOUS，分别表示阿里云APP、 匿名 |
| ResultType | String | 返回类型 |
| ResultSample | String | 返回示例 |
| FailResultSample | String | 后端服务失败返回应答的示例 |
| ErrorCodeSampl es | ErrorCodeSampl e | 后端服务返回的错误码示例，详情见 ApiAttributesType.md#ErrorCodeSamples |
| RequestConfig | RequestConfig | 由 RequestConfig 组成的格式，返回API前端定义信息 |
| RequestParamet ers | RequestParame ter | 由 RequestParameter 组成的数组格式，返回API中前端入参信息项 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApiDoc &GroupId=0009db9c828549768a200320714b8930 &ApiId=3b81fd160f5645e097cc8855d75a1cf6
```

`&<`公共请求参数> API 网关

**返回示例**

XML格式

```xml
<DescribeApiDocResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ014</RequestId>
    <GroupId>0009db9c828549768a200320714b8930</GroupId>
    <GroupName>myGroup2</GroupName>
    <StageName>RELEASE</StageName>
    <ApiId>3b81fd160f5645e097cc8855d75a1cf6</ApiId>
    <ApiName>creatobject</ApiName>
    <Description>对象创建</Description>
    <Visibility>public</Visibility>
    <AuthType>APP</AuthType>
    <ResultType>application/json</ResultType>
    <ResultSample></ResultSample>
    <FailResultSample></FailResultSample>
            <Code>400</Code>
            <Message>Missing the parameter UserId</Message>
```

`<Description>`请求缺少参数 `UserId</Description>`

```xml
        <RequestProtocol>HTTP</RequestProtocol>
        <RequestHttpMethod>GET</RequestHttpMethod>
        <RequestPath>/mypath/creatobject</RequestPath>
        <BodyFormat>FORM</BodyFormat>
        <PostBodyDescription>对象</PostBodyDescription>
            <ApiParameterName>RequestKey1</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
            <Required>REQUIRED</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>demo1</DemoValue>
            <MaxValue></MaxValue>
            <MinValue></MinValue>
            <MaxLength>100</MaxLength>
            <MinLength>3</MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>1</DocOrder>
            <Description>Desc1</Description>
            <ApiParameterName>RequestKey2</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
```

API 网关

```xml
            <Required>OPTIONAL</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>12</DemoValue>
            <MaxValue>120</MaxValue>
            <MinValue>100</MinValue>
            <MaxLength></MaxLength>
            <MinLength></MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>2</DocOrder>
            <Description>Desc2</Description>
</DescribeApiDocResponse>
```

JSON格式

```json
{
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ014",
    "RegionId": "cn-qingdao",
    "GroupId": "0009db9c828549768a200320714b8930",
    "GroupName": "myGroup2",
    "StageName": "RELEASE",
    "ApiId": "3b81fd160f5645e097cc8855d75a1cf6",
    "ApiName": "creatobject",
```

`"Description": "`对象创建`",`

```json
    "Visibility": "public",
    "AuthType": "APP",
    "ResultType": "application/json",
    "ResultSample": "200",
    "FailResultSample": "400",
            {
                "Code": "400",
                "Message": "Missing the parameter UserId",
```

`"Description": "`请求缺少参数 `UserId"`

```
            }
```

]

```json
    },
      "RequestProtocol": "HTTP",
      "RequestHttpMethod": "GET",
      "RequestPath": "/mypath/creatobject",
      "BodyFormat": "FORM",
      "PostBodyDescription": "对象"
    },
        {
          "ApiParameterName": "RequestKey1",
          "Location": "QUERY",
"ParameterType":"String",
```

API 网关

```json
          ParameterType: String,
          "Required": "REQUIRED",
          "DemoValue": "demo1",
          "MaxLength": "100",
          "MinLength": "3",
          "DocShow": "PUBLIC",
          "DocOrder": "1",
          "Description": "Desc1"
        },
        {
          "ApiParameterName": "RequestKey2",
          "Location": "QUERY",
          "ParameterType": "Number",
          "Required": "OPTIONAL",
          "DemoValue": "12",
          "MaxValue": "120",
          "MinValue": "100",
          "DocShow": "PUBLIC",
          "DocOrder": "2",
          "Description": "Desc2"
        }
```

]

```
    }
  }
```

### 查询定义中的API列表

**描述**

此功能面向开放API的用户接口返回所有定义中的API列表，以及概况信息请注意是返回所有编辑中的API定义信息，跟环境无关，也可能跟环境中正在运行的定义不同，是最新的编辑结果

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeApis |
| GroupId | String | 否 | 指定的分组编号 |
| ApiId | String | 否 | 指定的API编号 |
| ApiName | String | 否 | API名称（模糊匹配） |

API 网关

| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |
|---|---|---|---|
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |

**说明**

DescribeApis接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| TotalCount | Integer | 返回结果的总条数 |
| PageNumber | Integer | 返回指定的页码 |
| PageSize | Integer | 返回指定的每页条数 |
| ApiSummarys | ApiSummary | 由 ApiSummary 组成的数组格式，返回API的定义信息 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApis &ApiName=weather &pageSize=15 &pageNumber=3
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<DescribeApisResponse>
            <GroupId>63be9002440b4778a61122f14c2b2bbb</GroupId>
            <GroupName>myGroup3</GroupName>
            <ApiId>c076144d7878437b8f82fb85890ce6a0</ApiId>
```

`<ApiName>`获取对象列表`</ApiName>`

```xml
            <Visibility>public</Visibility>
```

`<Description>`分页显示对象列表`</Description>`

```xml
            <CreatedTime>2016-06-20T18:18:25Z</CreatedTime>
            <ModifiedTime>2016-07-23T08:28:48Z</ModifiedTime>
            <GroupId>1084f9034c744137901057206b39d2b6</GroupId>
            <GroupName>myGroup2</GroupName>
            <ApiId>5af418828f0344a3b588c0cc1331a3bc</ApiId>
```

`<ApiName>`创建对象`</ApiName>`

```xml
            <Visibility>public</Visibility>
```

`<Description>`创建对象接口`</Description>`

```xml
            <CreatedTime>2016-05-20T18:18:25Z</CreatedTime>
            <ModifiedTime>2016-07-23T08:28:48Z</ModifiedTime>
    <PageNumber>3</PageNumber>
    <PageSize>15</PageSize>
    <TotalCount>32</TotalCount>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ002</RequestId>
</DescribeApisResponse>
```

JSON格式 API 网关

```json
{
        {
          "RegionId": "cn-qingdao",
          "GroupId": "63be9002440b4778a61122f14c2b2bbb",
          "GroupName": "myGroup3",
          "ApiId": "c076144d7878437b8f82fb85890ce6a0",
```

`"ApiName": "`获取对象列表`",`

```json
          "Visibility": "public",
```

`"Description": "`分页显示对象列表`",`

```json
          "CreatedTime": "2016-06-20T18:18:25Z",
          "ModifiedTime": "2016-07-23T08:28:48Z"
        },
        {
          "RegionId": "cn-qingdao",
          "GroupId": "1084f9034c744137901057206b39d2b6",
          "GroupName": "myGroup2",
          "ApiId": "5af418828f0344a3b588c0cc1331a3bc",
```

`"ApiName": "`创建对象`",`

```json
          "Visibility": "public",
```

`"Description": "`创建对象接口`",`

```json
          "CreatedTime": "2016-05-20T18:18:25Z",
          "ModifiedTime": "2016-07-23T08:28:48Z"
        }
```

]

```json
    },
    "PageNumber": "3",
    "PageSize": "15",
    "TotalCount": "32",
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ002"
  }
```

### 查询历史版本详情

**描述**

查询指定API的某一次历史发布版本的定义详情，即某一次历史发布时发布的API定义。 此功能面向开放API的用户网关会记录下每个API每一次发布的时间、定义等等，您可以通过其他的接口获取版本号来指定查询某一次发布的定义详情

**请求参数**

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeApiHistory |
| GroupId | String | 是 | 指定的分组编号 |
| ApiId | String | 是 | 指定的API编号 |

API 网关

| StageName | String | 是 | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |
|---|---|---|---|
| HistoryVersio n | String | 是 | 指定的版本号（从DescribeHistoryApis接口可以获取到版本号） |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| RegionId | String | 所在的region |
| GroupId | String | API分组编号 |
| GroupName | String | API分组名称 |
| StageName | String | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |
| ApiId | String | API编号 |
| ApiName | String | API名称 |
| Description | String | API描述 |
| HistoryVersio n | String | API定义的版本号 |
| Status | String | 对应版本的API是否生效，取值为：ENABLE、DISABLE，分别表示有效、无效 |
| Visibility | String | 可见性，取值为：PUBLIC、PRIVATE，分别表示公开、私有 |
| AuthType | String | 安全认证方式，取值为：APP、ANONYMOUS、APPOPENID，分别表示阿里云APP、匿名、第三方账号认证OpenID Connect |
| ResultType | String | 返回类型 |
| ResultSample | String | 返回示例 |
| FailResultSam ple | String | 后端服务失败返回应答的示例 |
| DeployedTime | String | 发布时间（格林威治时间） |
| ErrorCodeSa mples | ErrorCodeSa mple | 后端服务返回的错误码示例，详情见 ApiAttributesType.md#ErrorCodeSamples |
| RequestConfi g | RequestConfi g | 由 RequestConfig 组成的格式，返回API前端定义信息 |
| ServiceConfig | ServiceConfi g | 由 ServiceConfig 组成的格式，返回API调用后端服务信息 |

API 网关

| SystemParam eters | SystemPara meter | 由 SystemParameter 组成的数组格式，返回API中调用后端服务时系统入参信息项 |
|---|---|---|
| ConstantPara meters | ConstantPara meter | 由 ConstantParameter 组成的数组格式，返回API中调用后端服务时常量入参信息项 |
| RequestPara meters | RequestPara meter | 由 RequestParameter 组成的数组格式，返回API中前端入参信息项 |
| ServiceParam eters | ServicePara meter | 由 ServiceParameter 组成的数组格式，返回API中调用后端服务时常量入参信息项 |
| ServiceParam etersMap | ServicePara meterMap | 由 ServiceParameterMap 组成的数组格式，返回API中前后端参数映射关系 |
| OpenIdConne ctConfig | OpenIdConne ctConfig | 第三方账号认证OpenID Connect相关配置项，详情见 ApiAttributesType.md#OpenIdConnectConfig |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApiHistory &GroupId=0009db9c828549768a200320714b8930 &ApiId=3b81fd160f5645e097cc8855d75a1cf6 &StageName=RELEASE &HistoryVersion=20160314220059844
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DescribeApiHistoryResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
    <GroupId>0009db9c828549768a200320714b8930</GroupId>
    <GroupName>myGroup2</GroupName>
    <StageName>RELEASE</StageName>
    <ApiId>3b81fd160f5645e097cc8855d75a1cf6</ApiId>
    <ApiName>creatobject</ApiName>
    <Description>对象创建</Description>
    <HistoryVersion>20160314220059844</HistoryVersion>
    <Status>DISABLE</Status>
    <Visibility>public</Visibility>
    <AuthType>APP</AuthType>
    <ResultType>application/json</ResultType>
    <ResultSample></ResultSample>
    <FailResultSample></FailResultSample>
    <DeployedTime>2016-07-23T08:28:48Z</DeployedTime>
        <RequestProtocol>HTTP</RequestProtocol>
        <RequestHttpMethod>GET</RequestHttpMethod>
        <RequestPath>/mypath/creatobject</RequestPath>
        <BodyFormat>FORM</BodyFormat>
        <PostBodyDescription>对象</PostBodyDescription>
```

API 网关

```xml
        <ServiceProtocol>HTTP/HTTPS</ServiceProtocol>
        <ServiceAddress>http://api.a.com:8080</ServiceAddress>
        <ServiceHttpMethod>GET</ServiceHttpMethod>
        <ServicePath>/object/add</ServicePath>
        <ServiceTimeout>2000</ServiceTimeout>
            <ParameterName>CaRequestId</ParameterName>
            <ServiceParameterName>RequestId</ServiceParameterName>
            <Location>HEAD</Location>
            <DemoValue>0A964636-F7A3-4F1A-92D7-135584A6397F</DemoValue>
            <Description>请求编号</Description>
            <ParameterName>CaAppId</ParameterName>
            <ServiceParameterName>AppId</ServiceParameterName>
            <Location>QUERY</Location>
            <DemoValue>0A964636-F7A3-4F1A-92D7-135584A6398F</DemoValue>
```

`<Description>`请求者应用编号`</Description>`

```xml
            <ServiceParameterName>ConstantKey1</ServiceParameterName>
            <ConstantValue>helloworld</ConstantValue>
            <Location>QUERY</Location>
            <Description>Desc</Description>
            <ApiParameterName>RequestKey1</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
            <Required>REQUIRED</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>demo1</DemoValue>
            <MaxValue></MaxValue>
            <MinValue></MinValue>
            <MaxLength>100</MaxLength>
            <MinLength>3</MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>1</DocOrder>
            <Description>Desc1</Description>
            <ApiParameterName>RequestKey2</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
```

API 网关 `yp` / `yp`

```xml
            <Required>OPTIONAL</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>12</DemoValue>
            <MaxValue>120</MaxValue>
            <MinValue>100</MinValue>
            <MaxLength></MaxLength>
            <MinLength></MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>2</DocOrder>
            <Description>Desc2</Description>
            <Code>400</Code>
            <Message>Missing the parameter UserId</Message>
```

`<Description>`请求缺少参数 `UserId</Description>`

```xml
            <ServiceParameterName>ServiceKey1</ServiceParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
            <ServiceParameterName>ServiceKey2</ServiceParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
            <ServiceParameterName>RequestKey1</ServiceParameterName>
            <RequestParameterName>ServiceKey1</RequestParameterName>
            <ServiceParameterName>RequestKey2</ServiceParameterName>
            <RequestParameterName>ServiceKey2</RequestParameterName>
    <OpenIdConnectConfig>
        <publicKey>EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92</publicKey>
        <openIdApiType>IDTOKEN</openIdApiType>
        <publicKeyId>88483727556929326703309904351185815489</publicKeyId>
    </OpenIdConnectConfig>
</DescribeApiHistoryResponse>
```

JSON格式

```
{
```

`"R`

```
tId" "CEF72CEB54B64AE8B225F876FF7BZ004"
```

API 网关

```json
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ004",
    "RegionId": "cn-qingdao",
    "GroupId": "0009db9c828549768a200320714b8930",
    "GroupName": "myGroup2",
    "StageName": "RELEASE",
    "ApiId": "3b81fd160f5645e097cc8855d75a1cf6",
    "ApiName": "creatobject",
```

`"Description": "`对象创建`",`

```json
    "HistoryVersion": "20160314220059844",
    "Status": "DISABLE",
    "Visibility": "public",
    "AuthType": "APP",
    "ResultType": "application/json",
    "ResultSample": "200",
    "FailResultSample": "400",
    "DeployedTime": "2016-07-23T08:28:48Z",
      "RequestProtocol": "HTTP",
      "RequestHttpMethod": "GET",
      "RequestPath": "/mypath/creatobject",
      "BodyFormat": "FORM",
      "PostBodyDescription": "对象"
    },
      "ServiceProtocol": "HTTP/HTTPS",
      "ServiceAddress": "http://api.a.com:8080",
      "ServiceHttpMethod": "GET",
      "ServicePath": "/object/add",
      "ServiceTimeout": "2000"
    },
        {
          "ParameterName": "CaRequestId",
          "ServiceParameterName": "RequestId",
          "Location": "HEAD",
          "DemoValue": "0A964636-F7A3-4F1A-92D7-135584A6397F",
```

`"Description": "`请求编号"

```json
        },
        {
          "ParameterName": "CaAppId",
          "ServiceParameterName": "AppId",
          "Location": "QUERY",
          "DemoValue": "0A964636-F7A3-4F1A-92D7-135584A6398F",
```

`"Description": "`请求者应用编号"

```
        }
```

]

```json
    },
        "ServiceParameterName": "ConstantKey1",
        "ConstantValue": "helloworld",
        "Location": "QUERY",
        "Description": "Desc"
}
```

API 网关

```json
      }
    },
        {
          "ApiParameterName": "RequestKey1",
          "Location": "QUERY",
          "ParameterType": "String",
          "Required": "REQUIRED",
          "DemoValue": "demo1",
          "MaxLength": "100",
          "MinLength": "3",
          "DocShow": "PUBLIC",
          "DocOrder": "1",
          "Description": "Desc1"
        },
        {
          "ApiParameterName": "RequestKey2",
          "Location": "QUERY",
          "ParameterType": "Number",
          "Required": "OPTIONAL",
          "DemoValue": "12",
          "MaxValue": "120",
          "MinValue": "100",
          "DocShow": "PUBLIC",
          "DocOrder": "2",
          "Description": "Desc2"
        }
```

]

```json
    },
            {
                "Code": "400",
                "Message": "Missing the parameter UserId",
```

`"Description": "`请求缺少参数 `UserId"`

```
            }
```

]

```json
    },
        {
          "ServiceParameterName": "ServiceKey1",
          "Location": "QUERY",
          "ParameterType": "String"
        },
        {
          "ServiceParameterName": "ServiceKey2",
          "Location": "QUERY",
          "ParameterType": "Number"
        }
```

]

```
    },
```

API 网关 `Se`

```json
ceaaete ap:[
        {
          "ServiceParameterName": "RequestKey1",
        },
        {
          "ServiceParameterName": "RequestKey2",
        }
```

]

```json
    },
    "OpenIdConnectConfig": {
        "publicKey": "EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92",
        "openIdApiType": "IDTOKEN",
        "publicKeyId": "88483727556929326703309904351185815489"
    }
}
```

### 查询API历史版本列表

**描述**

查询指定API历次历史发布的版本列表此功能面向开放API的用户，有过发布的API才有历史版本记录调用该接口能获取API历史版本号数据，用于其他接口的调用

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeApiHistories |
| GroupId | String | 是 | 指定的分组编号 |
| ApiId | String | 否 | 指定的API编号 |
| ApiName | String | 否 | API名称（模糊匹配） |
| StageName | String | 否 | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| TotalCount | Integer | 返回结果的总条数 |

API 网关

| PageNumber | Integer | 返回指定的页码 |
|---|---|---|
| PageSize | Integer | 返回指定的每页条数 |
| ApiHisItems | ApiHisItem | 由 ApiHisItem 组成的数组格式，返回API的信息 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApiHistories &ApiName=weather &pageSize=15 &pageNumber=3
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DescribeApiHistoriesResponse>
            <GroupId>63be9002440b4778a61122f14c2b2bbb</GroupId>
            <GroupName>myGroup3</GroupName>
            <ApiId>c076144d7878437b8f82fb85890ce6a0</ApiId>
```

`<ApiName>`获取对象列表`</ApiName>`

```xml
            <StageName>release</StageName>
            <HistoryVersion>20160705104552292</HistoryVersion>
            <Status>DISABLE</Status>
```

`<Description>`分页显示对象列表`</Description>`

```xml
            <DeployedTime>2016-07-23T08:28:48Z</DeployedTime>
            <GroupId>1084f9034c744137901057206b39d2b6</GroupId>
            <GroupName>myGroup2</GroupName>
            <ApiId>5af418828f0344a3b588c0cc1331a3bc</ApiId>
```

`<ApiName>`创建对象`</ApiName>`

```xml
            <StageName>release</StageName>
            <HistoryVersion>20160705104552393</HistoryVersion>
            <Status>DISABLE</Status>
```

`<Description>`创建对象接口`</Description>`

```xml
            <DeployedTime>2016-07-20T08:28:48Z</DeployedTime>
    <PageNumber>3</PageNumber>
    <PageSize>15</PageSize>
    <TotalCount>32</TotalCount>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ003</RequestId>
</DescribeApiHistoriesResponse>
```

JSON格式 API 网关

```json
{
              {
                "RegionId": "cn-qingdao",
                "GroupId": "63be9002440b4778a61122f14c2b2bbb",
                "GroupName": "myGroup3",
                "ApiId": "c076144d7878437b8f82fb85890ce6a0",
```

`"ApiName": "`获取对象列表`",`

```json
                "StageName": "release",
                "HistoryVersion": "20160705104552292",
                "Status": "DISABLE",
```

`"Description": "`分页显示对象列表`",`

```json
                "DeployedTime": "2016-07-23T08:28:48Z"
              },
              {
                "RegionId": "cn-qingdao",
                "GroupId": "1084f9034c744137901057206b39d2b6",
                "GroupName": "myGroup2",
                "ApiId": "5af418828f0344a3b588c0cc1331a3bc",
```

`"ApiName": "`创建对象`",`

```json
                "StageName": "release",
                "HistoryVersion": "20160705104552393",
                "Status": "DISABLE",
```

`"Description": "`创建对象接口`",`

```json
                "DeployedTime": "2016-07-20T08:28:48Z"
              }
```

]

```json
      },
    "PageNumber": 3,
      "PageSize": 15,
      "TotalCount": 32,
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ003"
}
```

### 查询已发布API的运行定义

**描述**

查询指定API在指定环境中正在运行的定义，是真正在指定环境中生效的定义，可能跟正在编辑中的定义不同。 此功能面向开放API的用户用于查询某指定API已经发布到某指定环境的定义，即环境中正在运行的定义，这一版定义可能和正在修改中的定义不同。只有将修改后定义重新发布到某环境，才会覆盖该API在该环境的运行中定义。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeDeployedApi |
| GroupId | String | 是 | 指定的分组编号 |

API 网关

| ApiId | String | 是 | 指定的API编号 |
|---|---|---|---|
| StageName | String | 是 | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| RegionId | String | 所在的region |
| GroupId | String | API分组编号 |
| GroupName | String | API分组名称 |
| StageName | String | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |
| ApiId | String | API编号 |
| ApiName | String | API名称 |
| Description | String | API描述 |
| Visibility | String | 可见性，取值为：PUBLIC、PRIVATE，分别表示公开、私有 |
| AuthType | String | 安全认证方式，取值为：APP、ANONYMOUS、APPOPENID， 分别表示阿里云APP、匿名、第三方账号认证OpenID Connect |
| ResultType | String | 返回类型 |
| ResultSample | String | 返回示例 |
| FailResultSample | String | 后端服务失败返回应答的示例 |
| DeployedTime | String | 发布时间（格林威治时间） |
| ErrorCodeSamples | ErrorCodeSample | 后端服务返回的错误码示例，详情见 ApiAttributesType.md#ErrorCodeSamples |
| RequestConfig | RequestConfig | 由 RequestConfig 组成的格式，返回API前端定义信息 |
| ServiceConfig | ServiceConfig | 由 ServiceConfig 组成的格式，返回API调用后端服务信息 |
| SystemParameters | SystemParameter | 由 SystemParameter 组成的数组格式，返回API中调用后端服务时系统入参信息项 |
| ConstantParameter s | ConstantParamete r | 由 ConstantParameter 组成的数组格式，返回API中调用后端服务时常量入参信息项 |
| RequestParameter s | RequestParameter | 由 RequestParameter 组成的数组格式，返回API中前端入参信息项 |

API 网关

| ServiceParameters | ServiceParameter | 由 ServiceParameter 组成的数组格式，返回API中调用后端服务时常量入参信息项 |
|---|---|---|
| ServiceParameters Map | ServiceParameter Map | 由 ServiceParameterMap 组成的数组格式，返回API中前后端参数映射关系 |
| OpenIdConnectCon fig | OpenIdConnectCo nfig | 第三方账号认证OpenID Connect相关配置项，详情见 ApiAttributesType.md#OpenIdConnectConfig |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeDeployedApi &GroupId=0009db9c828549768a200320714b8930 &ApiId=3b81fd160f5645e097cc8855d75a1cf6 &StageName=RELEASE
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DescribeDeployedApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
    <GroupId>0009db9c828549768a200320714b8930</GroupId>
    <GroupName>myGroup2</GroupName>
    <StageName>RELEASE</StageName>
    <ApiId>3b81fd160f5645e097cc8855d75a1cf6</ApiId>
    <ApiName>creatobject</ApiName>
    <Description>对象创建</Description>
    <Visibility>public</Visibility>
    <AuthType>APP</AuthType>
    <ResultType>application/json</ResultType>
    <ResultSample></ResultSample>
    <FailResultSample></FailResultSample>
    <DeployedTime>2016-07-23T08:28:48Z</DeployedTime>
        <RequestProtocol>HTTP</RequestProtocol>
        <RequestHttpMethod>GET</RequestHttpMethod>
        <RequestPath>/mypath/creatobject</RequestPath>
        <BodyFormat>FORM</BodyFormat>
        <PostBodyDescription>对象</PostBodyDescription>
        <ServiceProtocol>HTTP/HTTPS</ServiceProtocol>
        <ServiceAddress>http://api.a.com:8080</ServiceAddress>
        <ServiceHttpMethod>GET</ServiceHttpMethod>
        <ServicePath>/object/add</ServicePath>
        <ServiceTimeout>2000</ServiceTimeout>
        <Mock>FALSE</Mock>
<ParameterName>CaReqestId</ParameterName>
```

API 网关

```xml
            <ParameterName>CaRequestId</ParameterName>
            <ServiceParameterName>RequestId</ServiceParameterName>
            <Location>HEAD</Location>
            <DemoValue>0A964636-F7A3-4F1A-92D7-135584A6397F</DemoValue>
            <Description>请求编号</Description>
            <ParameterName>CaAppId</ParameterName>
            <ServiceParameterName>AppId</ServiceParameterName>
            <Location>QUERY</Location>
            <DemoValue>0A964636-F7A3-4F1A-92D7-135584A6398F</DemoValue>
```

`<Description>`请求者应用编号`</Description>`

```xml
            <ServiceParameterName>ConstantKey1</ServiceParameterName>
            <ConstantValue>helloworld</ConstantValue>
            <Location>QUERY</Location>
            <Description>Desc</Description>
            <ApiParameterName>RequestKey1</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
            <Required>REQUIRED</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>demo1</DemoValue>
            <MaxValue></MaxValue>
            <MinValue></MinValue>
            <MaxLength>100</MaxLength>
            <MinLength>3</MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>1</DocOrder>
            <Description>Desc1</Description>
            <ApiParameterName>RequestKey2</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
            <Required>OPTIONAL</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>12</DemoValue>
            <MaxValue>120</MaxValue>
            <MinValue>100</MinValue>
            <MaxLength></MaxLength>
            <MinLength></MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
<EnumValue></EnumValue>
```

API 网关

```xml
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>2</DocOrder>
            <Description>Desc2</Description>
            <ServiceParameterName>ServiceKey1</ServiceParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
            <ServiceParameterName>ServiceKey2</ServiceParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
            <ServiceParameterName>RequestKey1</ServiceParameterName>
            <RequestParameterName>ServiceKey1</RequestParameterName>
            <ServiceParameterName>RequestKey2</ServiceParameterName>
            <RequestParameterName>ServiceKey2</RequestParameterName>
            <Code>400</Code>
            <Message>Missing the parameter UserId</Message>
```

`<Description>`请求缺少参数 `UserId</Description>`

```xml
    <OpenIdConnectConfig>
        <publicKey>EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92</publicKey>
        <openIdApiType>IDTOKEN</openIdApiType>
        <publicKeyId>88483727556929326703309904351185815489</publicKeyId>
    </OpenIdConnectConfig>
</DescribeDeployedApiResponse>
```

JSON格式

```json
{
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ004",
    "RegionId": "cn-qingdao",
    "GroupId": "0009db9c828549768a200320714b8930",
    "GroupName": "myGroup2",
    "StageName": "RELEASE",
    "ApiId": "3b81fd160f5645e097cc8855d75a1cf6",
    "ApiName": "creatobject",
```

`"Description": "`对象创建`",`

```json
    "Visibility": "public",
    "AuthType": "APP",
```

API 网关

```json
    "ResultType": "application/json",
    "DeployedTime": "2016-07-23T08:28:48Z",
      "RequestProtocol": "HTTP",
      "RequestHttpMethod": "GET",
      "RequestPath": "/mypath/creatobject",
      "BodyFormat": "FORM",
      "PostBodyDescription": "对象"
    },
      "ServiceProtocol": "HTTP/HTTPS",
      "ServiceAddress": "http://api.a.com:8080",
      "ServiceHttpMethod": "GET",
      "ServicePath": "/object/add",
      "ServiceTimeout": "2000",
      "Mock": "FALSE"
    },
        {
          "ParameterName": "CaRequestId",
          "ServiceParameterName": "RequestId",
          "Location": "HEAD",
          "DemoValue": "0A964636-F7A3-4F1A-92D7-135584A6397F",
```

`"Description": "`请求编号"

```json
        },
        {
          "ParameterName": "CaAppId",
          "ServiceParameterName": "AppId",
          "Location": "QUERY",
          "DemoValue": "0A964636-F7A3-4F1A-92D7-135584A6398F",
```

`"Description": "`请求者应用编号"

```
        }
```

]

```json
    },
        "ServiceParameterName": "ConstantKey1",
        "ConstantValue": "helloworld",
        "Location": "QUERY",
        "Description": "Desc"
      }
    },
        {
          "ApiParameterName": "RequestKey1",
          "Location": "QUERY",
          "ParameterType": "String",
          "Required": "REQUIRED",
          "DemoValue": "demo1",
          "MaxLength": "100",
          "MinLength": "3",
          "DocShow": "PUBLIC",
```

`"D` Od "

```
"1"
```

API 网关

```json
          "DocOrder": "1",
          "Description": "Desc1"
        },
        {
          "ApiParameterName": "RequestKey2",
          "Location": "QUERY",
          "ParameterType": "Number",
          "Required": "OPTIONAL",
          "DemoValue": "12",
          "MaxValue": "120",
          "MinValue": "100",
          "DocShow": "PUBLIC",
          "DocOrder": "2",
          "Description": "Desc2"
        }
```

]

```json
    },
        {
          "ServiceParameterName": "ServiceKey1",
          "Location": "QUERY",
          "ParameterType": "String"
        },
        {
          "ServiceParameterName": "ServiceKey2",
          "Location": "QUERY",
          "ParameterType": "Number"
        }
```

]

```json
    },
        {
          "ServiceParameterName": "RequestKey1",
        },
        {
          "ServiceParameterName": "RequestKey2",
        }
```

]

```json
    },
            {
                "Code": "400",
                "Message": "Missing the parameter UserId",
```

`"Description": "`请求缺少参数 `UserId"`

```
            }
```

]

```json
    },
    "OpenIdConnectConfig": {
        "publicKey": "EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92",
"openIdApiType":"IDTOKEN"
```

API 网关

```json
        openIdApiType: IDTOKEN,
        "publicKeyId": "88483727556929326703309904351185815489"
    }
}
```

### 查询已发布API列表

**描述**

查询已经发布到某指定环境中的API列表，即查询指定环境中正在运行的API列表。 此功能面向开放API的用户。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeDeployedApis |
| GroupId | String | 否 | 指定的分组编号 |
| StageName | String | 是 | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |
| ApiId | String | 否 | 指定的API编号 |
| ApiName | String | 否 | API名称（模糊匹配） |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| TotalCount | Integer | 返回结果的总条数 |
| PageNumber | Integer | 返回指定的页码 |
| PageSize | Integer | 返回指定的每页条数 |
| DeployedApis | DeployedApiItem | 由 DeployedApiItem 组成的数组格式，返回API的信息 |

**示例**

**请求示例**

API 网关

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeDeployedApis &ApiName=weather &pageSize=15 &pageNumber=3
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DescribeDeployedApisResponse>
    <DeployedApis>
            <GroupId>63be9002440b4778a61122f14c2b2bbb</GroupId>
            <GroupName>myGroup3</GroupName>
            <ApiId>c076144d7878437b8f82fb85890ce6a0</ApiId>
```

`<ApiName>`获取对象列表`</ApiName>`

```xml
            <StageName>release</StageName>
            <Visibility>public</Visibility>
```

`<Description>`分页显示对象列表`</Description>`

```xml
            <DeployedTime>2016-07-23T08:28:48Z</DeployedTime>
            <GroupId>1084f9034c744137901057206b39d2b6</GroupId>
            <GroupName>myGroup2</GroupName>
            <ApiId>5af418828f0344a3b588c0cc1331a3bc</ApiId>
```

`<ApiName>`创建对象`</ApiName>`

```xml
            <StageName>release</StageName>
            <Visibility>public</Visibility>
```

`<Description>`创建对象接口`</Description>`

```xml
            <DeployedTime>2016-07-20T08:28:48Z</DeployedTime>
    </DeployedApis>
    <PageNumber>3</PageNumber>
    <PageSize>15</PageSize>
    <TotalCount>32</TotalCount>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ002</RequestId>
</DescribeDeployedApisResponse>
```

JSON格式 API 网关

```json
{
    "DeployedApis": {
              {
                "RegionId": "cn-qingdao",
                "GroupId": "63be9002440b4778a61122f14c2b2bbb",
                "GroupName": "myGroup3",
                "ApiId": "c076144d7878437b8f82fb85890ce6a0",
```

`"ApiName": "`获取对象列表`",`

```json
                "StageName": "release",
                "Visibility": "public",
```

`"Description": "`分页显示对象列表`",`

```json
                "DeployedTime": "2016-07-23T08:28:48Z"
              },
              {
                "RegionId": "cn-qingdao",
                "GroupId": "1084f9034c744137901057206b39d2b6",
                "GroupName": "myGroup2",
                "ApiId": "5af418828f0344a3b588c0cc1331a3bc",
```

`"ApiName": "`创建对象`",`

```json
                "StageName": "release",
                "Visibility": "public",
```

`"Description": "`创建对象接口`",`

```json
                "DeployedTime": "2016-07-20T08:28:48Z"
              }
```

]

```json
      },
    "PageNumber": 3,
      "PageSize": 15,
      "TotalCount": 32,
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ002"
}
```

### 通过 Swagger 创建 API

通过导入符合阿里云 Swagger 规范的文本内容创建 API。阿里云目前支持基于Swagger 2.0的扩展，只支持json/yaml格式的Swagger配置文件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Overwrite | Bool ean | Quer y | 是 | true | 是否覆盖现有API。 覆盖检测条件为：API的 HTTP请求类型+后端请求路径相同。 |

API 网关

| GlobalCon dition | Json | Quer y | 否 | {} | 全局条件。 |
|---|---|---|---|---|---|
| DataForma t | Strin g | Quer y | 是 | yaml | Swagger文本格式： json yaml |
| Data | Strin g | Body | 是 | "A Swagger API definition in YAML" | Swagger文本内容。 |
| GroupId | Strin g | Quer y | 是 | 0009db9c828549768a20 0320714b**** | Swagger将被导入的分组编号。 |
| DryRun | Bool ean | Quer y | 否 | true | 预检验。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 647CEF05-404C- 4125-B3D7- 44792EB77392 | 本次请求ID。 |
| Failed | Array | { "Path":"/http/get/m apping", "ErrorMsg":"api already exists : apiUid ===> 8e274ec61cf6468e 83b683719568**** ", "HttpMethod":"post " } | 本次所有通过swagger导入失败的API信息。 |
| -Path | String | /http/get/mapping | 创建API时配置的请求路径。 |
| -HttpMethod | String | post | 创建API时配置的http方法。 |
| -ErrorMsg | String | api already exists : apiUid ===> 8e274ec61cf6468e 83b683719568**** | 创建API时返回的错误信息。 |

API 网关

| ModelFailed | Array | { "ModelName":"Reg ion", "ErrorMsg":"error msg", "GroupId":"36d4bcf aec1946e1870d90 b2d751****" } | 本次所有通过 swagger 导入失败的 Model 信息。 |
|---|---|---|---|
| -GroupId | String | 36d4bcfaec1946e1 870d90b2d751**** | API 分组 ID。 |
| -ModelName | String | Region | 模型名称。 |
| -ErrorMsg | String | error msg | 错误信息。 |
| Success | Array | { "ApiImportSwagger Success": [ { "Path": "/http/get/mapping ", "HttpMethod": "get", "ApiOperation": "CREATE", "ApiUid": "8e274ec61cf6468 e83b683719568*** *" } ] } | 本次所有通过swagger导入成功的API信息。 |
| -Path | String | /http/get/mapping | 创建API时配置的请求路径。 |
| -HttpMethod | String | get | 创建API时配置的http方法。 |
| -ApiUid | String | 8e274ec61cf6468e 83b683719568**** | 导入成功的API的UID。 |

API 网关

| -ApiOperation | String | CREATE | 该API是创建（CREATE）或修改（MODIFY）。 |
|---|---|---|---|
| ModelSuccess | Array | { "ModelUid": "d4bcfaec1946e18 70d", "ModelName": "NewInstance", "GroupId": "b2d552ed90ca43 5b86f7bf8d4541** **", "ModelOperation": "" } | 本次所有通过 swagger 导入成功的 Model 信息。 |
| -ModelUid | String | d4bcfaec1946e187 0d | 模型uid。 |
| - ModelOperatio n | String | {} | 模型操作。 |
| -GroupId | String | b2d552ed90ca435 b86f7bf8d4541**** | api分组id。 |
| -ModelName | String | NewInstance | 模型名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ImportSwagger &Overwrite=true &DataFormat=yaml &Data="A Swagger API definition in YAML" &GroupId=0009db9c828549768a200320714b****
```

&公共请求参数正常返回示例 `JSON` 格式 API 网关

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"647CEF05-404C-4125-B3D7-44792EB77392",
 "Failed":{
  "Path":"/http/get/mapping",
  "ErrorMsg":"api already exists : apiUid ===> 8e274ec61cf6468e83b683719568****",
  "HttpMethod":"post"
 },
 "ModelFailed":{
  "ModelName":"Region",
  "ErrorMsg":"error msg",
  "GroupId":"36d4bcfaec1946e1870d90b2d751****"
 },
 "Success":{
  "Path":"/http/get/mapping",
  "ApiUid":"8e274ec61cf6468e83b683719568****",
  "ApiOperation":"CREATE",
  "HttpMethod":"get"
 },
 "ModelSuccess":{
  "ModelUid":"d4bcfaec1946e1870d",
  "ModelOperation":null,
  "ModelName":"NewInstance",
  "GroupId":"b2d552ed90ca435b86f7bf8d4541****"
 }
}
```

API 网关

## 插件相关接口

### 创建插件

API网关将流控管理，IP访问控制，等功能统一到插件体系中，未来还会增加更多功能的插件，如CORS(跨域资源访问)，Caching等。您可以通过该接口创建各种类型的插件。

**插件使用规则**

一个API只能绑定一个相同类型的插件。 插件策略和API分别是独立管理的，将插件绑定到API的指定环境后，插件策略才会对已绑定的API起作用。 插件的绑定、解绑、更新会实时生效，不需要重新发布API，对于风险比较高的API，请先在测试API上测试通过。 API的下线操作不影响插件的绑定关系，再次发布后仍然会带有下线前绑定的插件。 如果插件上有已发布或者发布过但未删除的API，则插件无法执行删除操作。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：CreatePlugin |
| PluginName | String | 是 | 插件名称，支持大小写英文字母、中文、数字和下划线，长度4~50, 且不能以下划线开头。 |
| PluginType | String | 是 | 插件类型, 可选值： ipControl : IP访问控制 trafficControl : 流量控制 backendSignature : 后端签名 jwtAuth : JWT(OpenId Connect) cors : CORS跨域资源访问 caching : 缓存 routing: 后端路由 errorMapping：错误码映射 accessControl：访问控制 |
| PluginData | String | 是 | 插件定义语句，支持json、yaml，参考PluginData模板 |
| Description | String | 否 | 描述，限200字以内 |

API 网关

**说明**

CreatePlugin接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**PluginData模板**

可以选择json或者yaml格式的来配置您的插件，两种格式的schema相同，可以搜索yaml to json转换工具来进行配置格式的转换，yaml格式的模板如下流控插件

```
--unit: SECOND # 控制区间, 取值: SECOND, MINUTE, HOUR, DAY
```

`apiDefault: 1000 #` 允许的总流量值 `userDefault: 30 # (`可选)每个用户的默认流量最大值`, 0`表示不进行限制, 不能大于总流量值 `appDefault: 30 # (`可选)每个`APP`允许的流量最大值`, 0`表示不进行限制, 不能大于总流量值
    - `- type: "APP" #` 针对不同应用`(AK)`进行的流控

```
    policies:
```

    - `- key: 10123123 # AppId, AppId`的取值请在`API`网关控制台`->`应用管理`->`应用详情处查看
`value: 10 #` 特殊流控值, 不能大于总流量值

```
      - key: 10123123  # AppId
```

`value: 10 #` 特殊流控值, 不能大于总流量值 IP访问控制插件

```
---
```

`type: ALLOW #` 控制模式，支持白名单模式`'ALLOW'`和黑名单模式`'REFUSE'`

```
items:
  - blocks:          # IP地址段
```

    - `- 78.11.12.2 #` 使用`IP`地址方式配置
    - `- 61.3.9.0/24 #` 使用`CIDR`方式配置
`appId: 219810 # (`可选) 如果配置了`appId`则该条目仅对该`AppId`生效

```
  - blocks:          # IP地址段
```

    - `- 79.11.12.2 #` 使用`IP`地址方式配置
后端签名插件

```
--type: APIGW_BACKEND key: SampleKey secret: SampleSecret
```

JWT鉴权 API 网关

```
---
```

`parameter: X-Token #` 从指定的参数中获取`JWT,` 对应`API`的参数 `parameterLocation: header # API`为映射模式时可选`, API`为透传模式下必填, 用于指定`JWT`的读取位置, 仅支持`query`,`header` `claimParameters: # claims`参数转换, 网关会将`jwt claims`映射为后端参数
    - `- claimName: aud # claim`名称,支持公共和私有
`parameterName: X-Aud #` 映射后参数名称

```
  location: header         # 映射后参数位置, 支持`query,header,path,formData`
```

    - `- claimName: userId # claim`名称,支持公共和私有
`parameterName: userId #` 映射后参数名称 `location: query #` 映射后的参数位置, 支持`query,header,path,formData` `preventJtiReplay: false #` 是否开启针对`jti`的防重放检查, 默认`: false`
#

```bash
# `Json Web Key`的`Public Key`
jwk:
  kty: RSA
  e: AQAB
  use: sig
```

`kid: O8fpdhrViq2zaaaBEWZITz #` 在只配置一个`JWK`时`,kid`是可选的,但如果中`JWT`包含了`kid,`网关会校验`kid`的一致性

```
  alg: RS256
  n: qSVxcknOm0uCq5vGsOmaorPDzHUubBmZZ4UXj-9do7w9X1uKFXAnqfto4TepSNuYU2bA_-tzSLAGBsR-
BqvT6w9SjxakeiyQpVmexxnDw5WZwpWenUAcYrfSPEoNU-0hAQwFYgqZwJQMN8ptxkd0170PFauwACOx4Hfr- 9FPGy8NCoIO4MfLXzJ3mJ7xqgIZp3NIOGXz- GIAbCf13ii7kSStpYqN3L_zzpvXUAos1FJ9IPXRV84tIZpFVh2lmRh0h8ImKvI42dwlD_hOIzayL1Xno2R0T-d5AwTSdnep7g-Fwu8-sj4cCRWq3bd61Zs2QOJ8iustH0vSRMYdP5oYQ
```

跨域资源访问（CORS)

```
--allowOrigins: "api.foo.com" # 允许的ORIGIN, 用逗号分隔, 默认"
```

`*"`

```
allowMethods: "GET,POST,PUT,DELETE,HEAD,OPTIONS,PATCH" # 允许的方法 allowHeaders: "Authorization,Accept,Accept-Ranges,Cache-Control,Range,Date,Content-Ty pe,Content-Length,Content-MD5,User-Agent,X-Ca-Signature,X-Ca-Signature-Headers,X-Ca-S ignature-Method,X-Ca-Key,X-Ca-Timestamp,X-Ca-Nonce,X-Ca-Stage,X-Ca-Request-Mode,x-cadeviceid" exposeHeaders: "Content-MD5,Server,Date,Latency,X-Ca-Request-Id,X-Ca-Error-Code,X-Ca- Error-Message" maxAge: 172800 allowCredentials: true # 是否允许Cookie
```

缓存 API 网关

```
---
```

`varyByApp: false #` 是否按照访问方的`AppId`来区分缓存内容, 默认为`false` `varyByParameters: #` 按照不同的参数取值来区分缓存内容
    - `- userId #` 参数名称，如果后端参数映射为不同的名称，这里请填写映射后的参数名称
`varyByHeaders: #` 是否按照不同的请求`Header`值来区分缓存内容
    - Accept # `Accept`表示按照不同的`Accept`头来区分缓存
`clientCacheControl: #` 允许客户端通过`Cache-Control`头来影响缓存策略, 默认`off` `mode: "app" # off:` 拒绝所有端`, all:` 允许所有端`, apps:` 允许`appId`取值在`apps`列表中的端 `apps: #` 如果`mode`配置为`app`, 则允许`AppId`在以下列表中的取值
    - `- 1992323 #` 消费者`AppId,` 注意不是`AppKey`
    - `- 1239922 #` 消费者`AppId,` 注意不是`AppKey`
`cacheableHeaders: #` 允许缓存的后端`Headers,` 默认只缓存`Content-Type`和`Content-Length`
    - `- X-Customer-Token #` 允许缓存的`Header`名称
后端路由

```
--routes:
```

# 针对太老的客户端, 返回不再支持的应答`, ClientVersion`是`API`中的自定义参数

```
- name: MockForOldClient
  condition: "$ClientVersion < '2.0.5'"
  backend:
    type: "MOCK"
    statusCode: 400
    mockBody: "This version is not supported!!!"
```

# 蓝绿发布场景: 将5%的请求路由给蓝绿发布后端

```
- name: BlueGreenPercent05
  condition: "Random() < 0.05"
  backend:
    type: "HTTP"
    address: "https://beta-version.api.foo.com"
  constant-parameters:
  - name: x-route-blue-green
    location: header
    value: "route-blue-green"
```

错误码映射 API 网关

```
---
```

# 参与映射的字段

```
parameters:
  statusCode: "StatusCode"
  resultCode: "BodyJsonField:$.result_code"
  resultId: "BodyJsonField:$.req_msg_id"
```

# 映射条件

```
errorCondition: "$statusCode = 200 and $resultCode <> 'OK'"
```

# 错误码字段

```
errorCode: "resultCode"
```

# 映射项

```
mappings:
  - code: "ROLE_NOT_EXISTS"
    statusCode: 404
    errorMessage: "Role Not Exists, RequestId=${resultId}"
  - code: "INVALID_PARAMETER"
    statusCode: 400
    errorMessage: "Invalid Parameter, RequestId=${resultId}"
```

# 默认映射

```
defaultMapping:
  statusCode: 500
  errorMessage: "Unknown Error, ${resultCode}, RequestId=${ResultId}"
```

访问控制 API 网关

```
---
```

#
# 在这个例子中假设我们的`API`请求`Path`为`/{userId}/...`,
# API使用`JWT`认证，`JWT`中有`userId`和`userType`两个`claim`
# 我们这个插件的校验条件为
# - 当`userType=admin`时，允许所有的路径，
# - 当`userType=user`时，仅允许`/{userId}`路径一致的请求

```
parameters:
  userId: "Token:userId"
  userType: "Token:userType"
  pathUserId: "path:userId"
```

#
# 关于`Rules`的处理规则，依次演算条件，按照返回值为`true`或者`false`，处理`ifTrue`的逻辑或`ifFals
e`的结果
# `ALLOW`会直接判断为成功，而`DENY`则会直接返回错误代码给客户端，
# 如果没有触发`ALLOW`或`DENY`逻辑，则执行下一条

```xml
rules:
  - name: admin
    condition: "$userType = 'admin'"
    ifTrue: "ALLOW"
  - name: user
    condition: "$userId = $pathUserId"
    ifFalse: "DENY"
    statusCode: 403
    errorMessage: "Path not match ${userId} vs /${pathUserId}"
    responseHeaders:
      Content-Type: application/xml
    responseBody: |
      <Reason>Path not match ${userId} vs /${pathUserId}</Reason>
```

断路器

```
---
```

`timeoutThreshold: 15 #` 超时出现的阈值 `windowInSeconds: 30 #` 判断超时次数的时间窗口 `openTimeoutSeconds: 15 #` 断路器打开的超时时间 `downgradeBackend: #` 降级后的后端配置

```xml
  type: mock
  statusCode: 302
  body: |
    <result>
      <errorCode>I's a teapot</errorCode>
    </result>
```

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| PluginId | String | 插件唯一ID |

API 网关

**示例**

**请求示例**

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=CreatePlugin &PluginName=NewCors &PluginType=cors &PluginData="Plugin definition" &Description="createPlugin"
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<CreatePluginResponse>
   <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
   <PluginId>285bb759342649a1b70c2093a772e087</PluginId>
</CreatePluginResponse>
```

JSON格式

```json
{
    "RequestId":"EF924FE4-2EDD-4CD3-89EC-34E4708574E7",
    "PluginId" :"1f3bde29b43d4d53989248327ff737f2"
 }
```

### 修改插件

**描述**

修改用户自定义的插件配置此功能面向开放API的用户修改将对插件下绑定的API即时生效插件不允许重名

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Str ing | 是 | 操作接口名，系统规定参数，取值：ModifyPlugin |

API 网关

| PluginId | Str ing | 是 | 插件ID |
|---|---|---|---|
| PluginName | Str ing | 否 | 插件名称，支持大小写英文字母、中文、数字和下划线，长度4~50，且不能以下划线开头。 |
| PluginData | Str ing | 否 | 插件定义语句，格式参考CreatePlugin中的PluginData模板 |
| Description | Str ing | 否 | 描述信息 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=ModifyPlugin &PluginId=a96926e82f994915a8da40a119374537 &PluginName=modifyCors &PluginData="Plugin definition" &Description="modify plugin first"
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<ModifyPluginResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
</ModifyPluginResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ004",
}
```

### 删除插件

**描述**

API 网关删除指定的用户自定义插件，以及该策略包含的特殊流控策略此功能面向开放API的用户若该插件已经绑定了API，则需要先解除绑定才能操作删除，否则会报错

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DeletePlugin |
| PluginId | String | 是 | 插件ID |

**说明**

DeletePlugin接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DeletePlugin &PluginId=9a3f1a5279434f2ba74ccd91c295af9f
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DeletePluginResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
</DeletePluginResponse>
```

JSON格式 API 网关

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ004",
}
```

### 插件绑定API

**描述**

绑定插件到API上此接口面向开放API的用户绑定操作只能选择发布状态的API 绑定以后及时生效修改插件后及时生效

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：AttachPlugin |
| PluginId | String | 是 | 要绑定的插件ID。 |
| ApiIds | String | 是 | 指定要操作的API编号 |
| StageName | String | 是 | 指定要操作API的环境。 RELEASE:线上 PRE:预发 TEST:测试 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

```
http://apigateway.cn-qingdao.aliyuncs.com/Action=AttachPlugin &PluginId=9a3f1a5279434f2ba74ccd91c295af9f &ApiId=8afff6c8c4c6447abb035812e4d66b65 &StageName=RELEASE
```

**返回示例**

XML格式 API 网关

```xml
<AttachPluginResponse>
   <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</AttachPluginResponse>
```

JSON格式

```json
{
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ004"
}
```

### 解除插件与API绑定

**描述**

解除API与插件的绑定关系此功能面向开放API的用户用于解除API与插件的绑定关系，解绑及时生效

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DetachPlugin |
| PluginId | String | 是 | 指定要操作的插件ID。 |
| ApiIds | String | 是 | 指定要解绑的API。 |
| StageName | String | 是 | 指定要操作API的环境。 RELEASE：线上 PRE: 预发 TEST：测试 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

API 网关

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=DetachPlugin &PluginId=9a3f1a5279434f2ba74ccd91c295af9f &ApiId=8afff6c8c4c6447abb035812e4d66b65 &StageName=RELEASE
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DetachPluginResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
</DetachPluginResponse>
```

JSON格式

```json
{
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ004"
}
```

### 查询插件下绑定的API

**描述**

查询指定插件下已绑定的API信息此功能面向开放API的用户用于查询指定插件下已经绑定的API列表信息分页返回绑定关系列表中返回的API在对应的环境中可能已经下线

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribePluginApis |
| PluginId | String | 是 | 指定查询要用的插件ID。 |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |

**返回参数**

API 网关

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| TotalCount | Integer | 返回结果的总条数 |
| PageSize | Integer | 返回指定的每页条数 |
| PageNumber | Integer | 返回指定的页码 |
| ApiSummarys | ApiPluginSummary | 由ApiPluginSummary组成的数组格式，返回API的信息项 |

**示例**

**请求示例**

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribePluginApis &PluginId=a96926e82f994915a8da40a119374537
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<DescribePluginApisResponse>
   <RequestId>46373DC4-19F1-4DC8-8C31-1107289BB5E0</RequestId>
   <TotalCount>20</TotalCount>
   <PageSize>10</PageSize>
   <PageNumber>1</PageNumber>
          <ApiId>9a3f1a5279434f2ba74ccd91c295af9f</ApiId>
          <ApiName>firstAPI</ApiName>
          <StageName>RELEASE</StageName>
          <GroupId>46c79e78dfab4521a5f737faa805c4e1</GroupId>
          <GroupName>firstGroup</GroupName>
          <Description>描述</Description>
</DescribePluginApisResponse>
```

JSON格式 API 网关

```json
{
   "RequestId": "2DF14872-77CE-43A4-AB47-C4F128E5AA31",
   "TotalCount": "1",
   "PageNumber": "1",
   "PageSize": "10",
            "ApiId":"9a3f1a5279434f2ba74ccd91c295af9f",
            "ApiName":"firstAPI",
            "RegionId":"cn-qingdao",
            "StageName":"RELEASE",
            "GroupId":"46c79e78dfab4521a5f737faa805c4e1",
            "GroupName": "firstGroup"，
            "Description":"描述"
        }]
    },
}
```

### 查询插件列表及详情

**描述**

查询一组符合条件的API网关插件详情支持分页支持按照插件业务类型查询支持按照插件ID查询支持按照插件名称查询

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

API 网关

| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribePlugins |
|---|---|---|---|
| PluginId | String | 否 | 插件ID |
| PluginName | String | 否 | 插件名称 |
| PluginType | String | 否 | 插件类型, 可选值： ipControl : IP访问控制 trafficControl : 流量控制 backendSignature : 后端签名 |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |

**说明**

DescribePlugins接口调用时，您需要在调用代码的Header参数中设置x-acs-regionid、x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的地域、 资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| TotalCount | Integer | 返回结果的总条数 |
| PageNumber | Integer | 返回指定的页码 |
| PageSize | Integer | 返回指定的每页条数 |
| Plugins | PluginAttrubite | 由PluginAttribute 组成的数组格式，返回插件信息 |

**示例**

请求示例 API 网关

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribePlugins &PluginId=a96926e82f994915a8da40a119374537 &PluginName=testPlugin &PluginType=ipControl
```

`&<`公共请求参数> 返回示例 XML格式

```xml
<DescribePluginsResponse>
   <RequestId>46373DC4-19F1-4DC8-8C31-1107289BB5E0</RequestId>
   <TotalCount>20</TotalCount>
   <PageSize>10</PageSize>
   <PageNumber>1</PageNumber>
   <Plugins>
          <PluginId>9a3f1a5279434f2ba74ccd91c295af9f</PluginId>
          <PluginName>firstPlugin</PluginName>
          <PluginType>trafficControl</PluginType>
          <PluginData>{"unit":"MINUTE","apiDefault":20}</PluginData>
          <Description>流控</Description>
          <CreatedTime>2019-01-11T09:29:58Z</CreatedTime>
          <ModifiedTime>2019-01-11T09:29:58Z</ModifiedTime>
   </Plugins>
</DescribePluginsResponse>
```

JSON格式

```json
{
   "RequestId": "46373DC4-19F1-4DC8-8C31-1107289BB5E0",
   "TotalCount": "1",
   "PageNumber": "1",
   "PageSize": "10",
   "Plugins": {
            "PluginId":"9a3f1a5279434f2ba74ccd91c295af9f",
            "PluginName":"firstPlugin",
            "RegionId":"cn-qingdao",
            "PluginType":"trafficControl",
            "PluginData":"{\"unit\":\"MINUTE\",\"apiDefault\":20}",
            "Description": "流控"，
            "CreatedTime":"2019-01-11T09:29:58Z",
            "ModifiedTime":"2019-01-11T09:29:58Z"
        }]
    }
}
```

API 网关

### 查询API上绑定的插件

**描述**

查询指定API已绑定的插件，该API必须已发布到该环境。 此功能面向开放API的用户用于查询指定环境上指定API已绑定的插件列表

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribePluginsByApi |
| GroupId | String | 是 | 指定要查询的API所属分组。 |
| ApiId | String | 是 | 指定要查询的ApiId。 |
| StageName | String | 是 | 指定要查询的环境。 RELEASE： 线上 PRE：预发 TEST：测试 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| TotalCount | Integer | 返回结果的总条数 |
| PageNumber | Integer | 返回指定的页码 |
| PageSize | Integer | 返回指定的每页条数 |
| Plugins | PluginAttribute | 由PluginAttribute 组成的数组格式，返回插件的信息项 |

**示例**

**请求示例**

```
http://apigateway.example.com/?Action=DescribePluginsByApi
 &ApiId=93f4ead4080c4b2da70b7f81f50ae459
 &GroupId=3c7a38392e764718ad7673e7b7f535d4
 &StageName=RELEASE
```

`&<`公共请求参数>

**返回示例**

API 网关 XML格式

```xml
<DescribePluginsByApiResponse>
   <RequestId>46373DC4-19F1-4DC8-8C31-1107289BB5E0</RequestId>
   <TotalCount>20</TotalCount>
   <PageSize>10</PageSize>
   <PageNumber>1</PageNumber>
   <Plugins>
          <PluginId>9a3f1a5279434f2ba74ccd91c295af9f</PluginId>
          <PluginName>firstPlugin</PluginName>
          <PluginType>trafficControl</PluginType>
          <PluginData>{"unit":"MINUTE","apiDefault":20}</PluginData>
          <Description>流控</Description>
          <CreatedTime>2019-01-11T09:29:58Z</CreatedTime>
          <ModifiedTime>2019-01-11T09:29:58Z</ModifiedTime>
   </Plugins>
</DescribePluginsByApiResponse>
```

JSON格式 API 网关

```json
{
   "RequestId": "46373DC4-19F1-4DC8-8C31-1107289BB5E0",
   "TotalCount": "1",
   "PageNumber": "1",
   "PageSize": "10",
   "Plugins": {
            "PluginId":"9a3f1a5279434f2ba74ccd91c295af9f",
            "PluginName":"firstPlugin",
            "RegionId":"cn-qingdao",
            "PluginType":"trafficControl",
            "PluginData":"{\"unit\":\"MINUTE\",\"apiDefault\":20}",
            "Description": "流控"，
            "CreatedTime":"2019-01-11T09:29:58Z",
            "ModifiedTime":"2019-01-11T09:29:58Z"
        }]
    }
}
```

API 网关

## 应用管理相关接口

### 创建应用

**描述**

创建APP，APP是您调用第三方API时的身份，要调用第三方API必须创建APP。 此功能面向调用API的用户。 每个APP有一对Key和Value密钥对，该密钥在调用API时用于身份验证。 APP调用API需要建立授权关系，即授予APP调用某API的权限。 一个APP下只能有一对密钥，若密钥泄露可以重置。 该接口调用的QPS限制为：单用户QPS不超过50

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 操作接口名，系统规定参数，取值：CreateApp |
| AppName | Strin g | 是 | APP的名称，全局唯一，命名时最好加上特定标识，避免重名。支持汉字、英文字母、数字、英文格式的下划线，且必须以字母或汉字开始，4~15个字符 |
| Descriptio n | Strin g | 否 | APP描述信息，长度不超过180个字符 |

**说明**

CreateApp接口调用时，您需要在调用代码的Header参数中设置x-acs-organizationid、x-acsresourcegroupid、x-acs-instanceid等参数，用于指定资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| AppId | Long | APP的唯一编号 |

**示例**

请求示例 API 网关

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=CreateApp &AppName=CreateAppTest &Description=test
```

`&<`公共请求参数> 返回示例 XML格式

```xml
<CreateAppResponse>
    <AppId>20112314518278</AppId>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</CreateAppResponse>
```

JSON格式

```json
{
    "AppId":20112314518278,
    "RequestId":"BA20890E-75C7-41BC-9C8B-73276B58F550"
}
```

### 修改应用

**描述**

修改指定APP的基本信息此功能面向调用API的用户可修改AppName或者Description，若两个属性都为空，则不做修改，直接返回成功该接口调用的QPS限制为：单用户QPS不超过50

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：ModifyApp |
| AppId | Long | 是 | APP的唯一标识 |
| AppName | String | 否 | APP的名称，全局唯一，命名时最好加上特定标识，避免重名。支持汉字、英文字母、数字、英文格式的下划线，且必须以字母或汉字开始，4~15个字符若不修改，可不传该参数 |
| Description | String | 否 | APP描述信息，长度不超过180个字符若不修改，可不传该参数 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

API 网关

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=ModifyApp &AppId=20112314518278 &Description=modidyTest
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<ModifyAppResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</ModifyAppResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015"
}
```

### 重置APP密钥

**描述**

重置指定APP密钥此功能面向调用API的用户重置后密码是自动生成的，不能自己设置该接口不直接返回密码，需要通过查询密码的接口获取

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：ResetAppSecret |
| AppKey | String | 是 | APP的Key，用于调用API时使用 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=ResetAppSecret &AppKey=60030986
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<ResetAppSecretResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</ResetAppSecretResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015"
}
```

### 查询APP列表

**描述**

此功能面向调用API的用户 AppId选择性传入

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeAppAttributes |
| AppId | Long | 否 | APP的编号 |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |

**说明**

DescribeAppAttributes接口调用时，您需要在调用代码的Header参数中设置x-acsorganizationid、x-acs-resourcegroupid、x-acs-instanceid等参数，用于指定资源所属的组织、 资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| TotalCount | Integer | 返回结果的总条数 |

API 网关

| PageNumber | Integer | 返回指定的页码 |
|---|---|---|
| PageSize | Integer | 返回指定的每页条数 |
| Apps | AppAttribute | 由 AppAttribute 组成的数组格式，返回APP的信息 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeAppAttributes &AppId=20112314518278 &pageSize=10 &pageNumber=1
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
      <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Apps>
            <AppId>20112314518278</AppId>
            <AppName>CreateApptest</AppName>
            <Description>APP test</Description>
            <CreatedTime>2016-07-31T04:10:19Z</CreatedTime>
            <ModifiedTime>2016-07-31T04:10:19Z</ModifiedTime>
    </Apps>
```

JSON格式 API 网关

```json
{
    "TotalCount":1,
    "PageSize":10,
    "PageNumber":1,
    "RequestId":"8883AC74-259D-4C0B-99FC-0B7F9A588B2F",
    "Apps":
    {
        "AppAttribute":
```

[

```json
            {
                "AppId":20112314518278,
                "AppName":"CreateApptest",
                "Description":"APP test",
                "CreatedTime":"2016-07-31T04:10:19Z",
                "ModifiedTime":"2016-07-31T04:10:19Z"
            }
```

]

```
    }
}
```

### 查询APP密钥

**描述**

查询指定APP的密钥信息，该密钥在调用API时要用作身份认证。 此功能面向调用API的用户。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeAppSecurity |
| AppId | Long | 是 | APP的编号 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| AppKey | String | APP的key |
| AppSecret | String | APP的密码 |
| CreatedTime | String | 密钥创建时间（格林威治时间），与APP创建时间相同 |
| ModifiedTime | String | 密钥修改时间（格林威治时间） |

**示例**

**请求示例**

API 网关

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeAppSecurity &AppId=20112314518278
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DescribeAppSecurityResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
    <AppKey>60030986</AppKey>
    <AppSecret>c1ae97aaa7e45f21d10824bc44678fee</AppSecret>
    <CreatedTime>2016-07-31T04:10:19Z</CreatedTime>
    <ModifiedTime>2016-07-31T04:10:19Z</ModifiedTime>
</DescribeAppSecurityResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015",
    "AppKey":"60030986",
    "AppSecret":"c1ae97aaa7e45f21d10824bc44678fee",
    "CreatedTime":"2016-07-31T04:10:19Z",
    "ModifiedTime":"2016-07-31T04:10:19Z"
}
```

### 删除应用

**描述**

删除指定APP 此功能面向调用API的用户注意删除之后不可恢复，与API的授权关系也不可恢复该接口调用的QPS限制为：单用户QPS不超过50

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DeleteApp |
| AppId | Long | 是 | APP唯一编号 |

**说明**

DeleteApp接口调用时，您需要在调用代码的Header参数中设置x-acs-organizationid、x-acsresourcegroupid、x-acs-instanceid等参数，用于指定资源所属的组织、资源所属的资源集以及资源实例ID（如果存在的话），否则调用会指向根组织和根资源集。 API 网关

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DeleteApp &AppId=20112314518278
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<DeleteAppResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</DeleteAppResponse>
```

JSON格式

```json
{
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015"
}
```

API 网关

## 授权相关接口

### 查询待授权的APP

查询可授权的APP列表（DescribeApps）。

**描述**

查询可授权的APP列表，为API开放者在操作授权时提取APP信息此功能面向开放API的用户 API开放者可通过AppId或者阿里云登录账号查询APP信息，进而操作授权

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeApps |
| AppId | Long | 否 | APP的唯一标识 |
| AppOwner | String | 否 | APP拥有者的阿里云账号ID |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| TotalCount | Integer | 返回结果的总条数 |
| PageNumber | Integer | 返回指定的页码 |
| PageSize | Integer | 返回指定的每页条数 |
| Apps | AppItem | 由 AppItem 组成的数组格式，返回APP的信息 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApps &AppId=20112314518278 &pageSize=10 &pageNumber=1
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
<DescribeAppsResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
      <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Apps>
            <AppId>20112314518278</AppId>
            <AppName>CreateApptest</AppName>
            <Description>APP test</Description>
    </Apps>
</DescribeAppsResponse>
```

JSON格式

```json
{
    "TotalCount":1,
    "PageSize":10,
    "PageNumber":1,
    "RequestId":"8883AC74-259D-4C0B-99FC-0B7F9A588B2F",
    "Apps":
    {
        "AppItem":
```

[

```json
            {
                "AppId":20112314518278,
                "AppName":"CreateApptest",
                "Description":"APP test"                    }
```

]

```
    }
}
```

### 查询已授权APP的API

**描述**

用于查询指定APP已授权于的API列表，即指定APP可以调用的API列表此功能面向API使用者 APP可以调用查询结果返回的所有API

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：DescribeAuthorizedApis |
| AppId | Long | 是 | APP编号，系统生成，全局唯一 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |

API 网关

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |
| TotalCount | Integer | 返回结果的总条数 |
| PageSize | Integer | 返回指定的每页条数 |
| PageNumber | Integer | 返回指定的页码 |
| AuthorizedApis | AuthorizedApi | 已授权的API集合 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeAuthorizedApis &AppId＝2386789
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
    <PageNumber>1</PageNumber>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
            <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
            <GroupName>Weather</GroupName>
            <StageName>RELEASE</StageName>
            <Operator>PROVIDER</Operator>
            <ApiId>baacc592e63a4cb6a41920d9d3f91f38</ApiId>
            <ApiName>AreaWeather</ApiName>
            <AuthorizationSource>CONSOLE</AuthorizationSource>
```

`<Description>`根据地区名称查询天气情况`</Description>`

```xml
            <AuthorizedTime>2016-07-21T06:17:20Z</AuthorizedTime>
            <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
            <GroupName>Weather</GroupName>
            <StageName>RELEASE</StageName>
            <Operator>CONSUMER</Operator>
            <ApiId>baacc592e63a4cb6a41920d9d3f89g76</ApiId>
            <ApiName>Area</ApiName>
            <AuthorizationSource>API</AuthorizationSource>
            <Description>查询区域</Description>
            <AuthorizedTime>2016-07-21T06:17:20Z</AuthorizedTime>
```

JSON格式 API 网关

```json
{ "PageNumber": "1", "TotalCount": "2", "PageSize": "10", "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
    {
      "RegionId": "cn-hangzhou",
      "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
      "GroupName": "Weather",
      "StageName": "RELEASE",
      "Operator": "Provider",
      "ApiId": "baacc592e63a4cb6a41920d9d3f91f38",
      "ApiName": "AreaWeather",
      "AuthorizationSource": "CONSOLE",
```

`"Description": "`根据地区名称查询天气情况`",`

```json
      "AuthorizedTime": "2016-07-21T06:17:20Z"
    },
    {
      "RegionId": "cn-hangzhou",
      "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
      "GroupName": "Weather",
      "StageName": "RELEASE",
      "Operator": "CONSUMER",
      "ApiId": "baacc592e63a4cb6a41920d9d3f89g76",
      "ApiName": "Area",
      "AuthorizationSource": "API",
```

`"Description": "`查询区域`",`

```json
      "AuthorizedTime": "2016-07-21T06:17:20Z"
    }
```

]

```
} }
```

### 查询API授权记录

**描述**

用于查询当前可访问API的应用(APP)列表此功能面向API提供者查询当前可访问指定API的应用应用(APP)列表查询结果返回的所有应用（APP）均可访问指定的API

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：DescribeAuthorizedApps |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一 |

API 网关

| ApiId | String | 是 | API编号，系统生成，全局唯一 |
|---|---|---|---|
| StageName | String | 否 | 环境名称，取值为： RELEASE: 线上 TEST: 测试 |
| PageNumber | Integer | 否 | 指定要查询的页码，默认是1，起始是1 |
| PageSize | Integer | 否 | 指定分页查询时每页行数，最大值100，默认值为10 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |
| TotalCount | Integer | 返回结果的总条数 |
| PageNumber | Integer | 返回指定的页码 |
| PageSize | Integer | 返回指定的每页条数 |
| AuthorizedApps | AuthorizedApp | 返回分组集合 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeAuthorizedApps &GroupId＝523e8dc7bbe04613b5b1d726c2a7889d &ApiId＝baacc592e63a4cb6a41920d9d3f91f38
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
    <TotalCount>2</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
            <StageName>RELEASE</StageName>
            <AppId>2386789</AppId>
            <AppName>天气APP</AppName>
            <Operator>PROVIDER</Operator>
            <AuthorizationSource>CONSOLE</AuthorizationSource>
```

`<Description>`根据地区名称查询天气情况`</Description>`

```xml
            <AuthorizedTime>2016-07-21T06:17:20Z</AuthorizedTime>
            <StageName>TEST</StageName>
            <AppId>2386789</AppId>
            <AppName>天气APP</AppName>
            <Operator>CONSUMER</Operator>
            <AuthorizationSource>API</AuthorizationSource>
```

`<Description>`根据地区名称查询天气情况`</Description>`

```xml
            <AuthorizedTime>2016-07-21T06:17:20Z</AuthorizedTime>
```

JSON格式 API 网关

```json
{ "TotalCount": "2", "PageNumber": "1", "PageSize": "10", "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
    {
      "StageName": "RELEASE",
      "AppId": 2386789,
      "AppName": "天气APP",
      "Operator": "PROVIDER",
      "AuthorizationSource": "CONSOLE",
```

`"Description": "`根据地区名称查询天气情况`",`

```json
      "AuthorizedTime": "2016-07-21T06:17:20Z"
    },
    {
      "StageName": "TEST",
      "AppId": 2386789,
      "AppName": "天气APP",
      "Operator": "CONSUMER",
      "AuthorizationSource": "API",
```

`"Description": "`根据地区名称查询天气情况`",`

```json
      "AuthorizedTime": "2016-07-21T06:17:20Z"
    }
```

]

```
} }
```

### 将多个API授权给APP

**描述**

用于给指定APP添加多个API的访问权限此功能面向API提供者和API使用者 API提供者可以授权自己的API给任意应用（APP）调用 API使用者可以将已创建的API授权给自己的应用（APP）

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：SetApisAuthorities |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一 |
| StageName | String | 是 | 环境名称，取值为： RELEASE: 线上 TEST: 测试 |
| AppId | Long | 是 | 应用编号，系统生成，全局唯一 |

API 网关

| ApiIds | String | 否 | 指定要操作的API编号，支持输入多个，“,”分隔，最多支持 100个 |
|---|---|---|---|
| Description | String | 否 | 授权说明 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=SetApisAuthorities &GroupId＝523e8dc7bbe04613b5b1d726c2a7889d &StageName＝RELEASE &AppId＝2386789 &ApiIds＝baacc592e63a4cb6a41920d9d3f91f38,jkscc489e63a4cb6a41920d9d3f92d78
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<SetApisAuthoritiesResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
</SetApisAuthoritiesResponse>
```

JSON格式

```json
{
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
 }
```

### 将API授权给多个APP

**描述**

用于给多个APP添加指定API的访问权限，多个APP一个API 此功能面向API调用者和API使用者 API提供者可以授权自己的API给任意应用（APP）调用 API使用者可以将已购买的API授权给自己的应用（APP）

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：SetAppsAuthorities |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一 |

API 网关

| StageName | String | 是 | 环境名称，取值为： RELEASE: 线上 TEST: 测试 |
|---|---|---|---|
| ApiId | String | 是 | API编号，系统生成，全局唯一 |
| AppIds | String | 是 | 指定要操作的APP编号，支持输入多个，“,”分隔，最多支持 100个 |
| Description | String | 否 | 授权说明 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=SetAppsAuthorities &GroupId＝523e8dc7bbe04613b5b1d726c2a7889d &StageName＝RELEASE &ApiId＝baacc592e63a4cb6a41920d9d3f91f38 &AppIds＝2386789,3389798
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<SetAppsAuthoritiesResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
</SetAppsAuthoritiesResponse>
```

JSON格式

```json
{
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
 }
```

### 解除多个API与某APP的授权

**描述**

用于撤销指定应用（APP）对多个API的访问权限此功能面向API提供者和API使用者撤销前请查看添加授权记录的授权者，API所有者只能撤销Provicder的授权，API使用者只能撤销 Consumer的授权

**请求参数**

API 网关

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：RemoveApisAuthorities |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一 |
| StageName | String | 是 | 环境名称，取值为： RELEASE: 线上 TEST: 测试 |
| ApiIds | String | 是 | 指定要操作的API编号，支持输入多个，“,”分隔，最多支持 100个 |
| AppId | Long | 是 | 应用（APP）编号，系统生成，全局唯一 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=RemoveApisAuthorities &GroupId＝523e8dc7bbe04613b5b1d726c2a7889d &StageName＝RELEASE &ApiId＝baacc592e63a4cb6a41920d9d3f91f38,jkscc489e63a4cb6a41920d9d3f92d78 &AppId＝2386789
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<RemoveApisAuthoritiesResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
</RemoveApisAuthoritiesResponse>
```

JSON格式

```json
{
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
 }
```

### 解除API与多个APP的授权

**描述**

用于撤销多个APP对指定API的访问权限，多个APP一个API 此功能面向API提供者和API使用者撤销前请查看添加授权记录的授权者，API所有者只能撤销Provicder的授权，API使用者只能撤销 Consumer的授权 API 网关

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 接口名称，系统规定参数，取值：RemoveAppsAuthorities |
| GroupId | String | 是 | API分组 ID，系统生成，全局唯一 |
| StageName | String | 是 | 环境名称，取值为 RELEASE TEST |
| ApiId | String | 是 | API编号，系统生成，全局唯一 |
| AppIds | String | 是 | 指定要操作的APP编号，支持输入多个，“,”分隔，最多支持 100个 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求唯一标识 |

**示例**

**请求示例**

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=RemoveAppsAuthorities &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &StageName＝RELEASE &ApiId＝baacc592e63a4cb6a41920d9d3f91f38 &AppIds＝2386789,3286798
```

`&<`公共请求参数>

**返回示例**

XML格式

```xml
<RemoveAppsAuthoritiesResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
</RemoveAppsAuthoritiesResponse>
```

JSON格式

```json
 {
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
 }
```

API 网关

## 其他接口

### 查询支持的区域

**描述**

此功能面向开放API和调用API的用户。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeRegions |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| Regions | Region | 由 Region 组成的数组格式，返回区域信息 |

**示例**

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeRegions
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
    <RequestId>36BBBAD4-1CFB-489F-841A-8CA52EEA787E</RequestId>
            <EndPoint>apigateway.cn-qingdao.aliyuncs.com</EndPoint>
            <LocalName>华北 1 (青岛)</LocalName>
            <EndPoint>apigateway.cn-hangzhou.aliyuncs.com</EndPoint>
            <LocalName>华东 1 (杭州)</LocalName>
            <EndPoint>apigateway.cn-beijing.aliyuncs.com</EndPoint>
            <LocalName>华北 2 (北京)</LocalName>
            <EndPoint>apigateway.cn-shenzhen.aliyuncs.com</EndPoint>
            <LocalName>华南 1 (深圳)</LocalName>
```

JSON格式 API 网关

```json
{
    "RequestId": "36BBBAD4-1CFB-489F-841A-8CA52EEA787E",
            {
                "RegionId": "cn-qingdao",
                "EndPoint": "apigateway.cn-qingdao.aliyuncs.com",
```

`"LocalName": "`华北 `1 (`青岛`)"`

```json
            },
            {
                "RegionId": "cn-hangzhou",
                "EndPoint": "apigateway.cn-hangzhou.aliyuncs.com",
```

`"LocalName": "`华东 `1 (`杭州`)"`

```json
            },
            {
                "RegionId": "cn-beijing",
                "EndPoint": "apigateway.cn-beijing.aliyuncs.com",
```

`"LocalName": "`华北 `2 (`北京`)"`

```json
            },
            {
                "RegionId": "cn-shenzhen",
                "EndPoint": "apigateway.cn-shenzhen.aliyuncs.com",
```

`"LocalName": "`华南 `1 (`深圳`)"`

```
            }
```

]

```
    }
}
```

### 查询可配置的系统参数

**描述**

查询系统参数列表此功能面向开放API的用户此接口返回定义API时可选择接收的系统参数列表

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 操作接口名，系统规定参数，取值：DescribeSystemParameters |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 本次请求编号 |
| SystemParams | SystemParamItem | 由 SystemParam 组成的数组格式，返回系统参数信息 |

**示例**

API 网关

**请求示例**

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeSystemParameters
```

`&<`公共请求参数>

**返回示例**

XML格式 API 网关

```xml
    <RequestId>0CCDF65E-6050-412D-AD68-FA3D9196836C</RequestId>
            <Description>客户端IP</Description>
            <DemoValue>192.168.1.1</DemoValue>
            <ParamName>CaClientIp</ParamName>
            <ParamType>string</ParamType>
            <Description>请求域名</Description>
            <DemoValue>api.aliyun.com</DemoValue>
            <ParamName>CaDomain</ParamName>
            <ParamType>string</ParamType>
```

`<Description>`请求时间（格林威治时间）`</Description>`

```xml
            <DemoValue>2016-01-30T03:53:16Z</DemoValue>
            <ParamName>CaRequestHandleTime</ParamName>
            <ParamType>string</ParamType>
            <Description>ConsumerAppId</Description>
            <DemoValue>123456</DemoValue>
            <ParamName>CaAppId</ParamName>
            <ParamType>string</ParamType>
            <Description>RequestId</Description>
            <DemoValue>7157EBD9-4684-4827-B3B0-9B32D186819B</DemoValue>
            <ParamName>CaRequestId</ParamName>
            <ParamType>string</ParamType>
            <Description>Http Schema</Description>
            <DemoValue>https</DemoValue>
            <ParamName>CaHttpSchema</ParamName>
            <ParamType>string</ParamType>
            <Description>代理</Description>
            <DemoValue>AliCloudApiGateway</DemoValue>
            <ParamName>CaProxy</ParamName>
            <ParamType>string</ParamType>
```

JSON格式 API 网关

```json
{
    "RequestId": "0CCDF65E-6050-412D-AD68-FA3D9196836C",
            {
                "Description": "客户端IP",
                "DemoValue": "192.168.1.1",
                "ParamName": "CaClientIp",
                "ParamType": "string"
            },
            {
```

`"Description": "`请求域名`",`

```json
                "DemoValue": "api.aliyun.com",
                "ParamName": "CaDomain",
                "ParamType": "string"
            },
            {
```

`"Description": "`请求时间（格林威治时间）`",`

```json
                "DemoValue": "2016-01-30T03:53:16Z",
                "ParamName": "CaRequestHandleTime",
                "ParamType": "string"
            },
            {
                "Description": "ConsumerAppId",
                "DemoValue": "123456",
                "ParamName": "CaAppId",
                "ParamType": "string"
            },
            {
                "Description": "RequestId",
                "DemoValue": "7157EBD9-4684-4827-B3B0-9B32D186819B",
                "ParamName": "CaRequestId",
                "ParamType": "string"
            },
            {
                "Description": "Http Schema",
                "DemoValue": "https",
                "ParamName": "CaHttpSchema",
                "ParamType": "string"
            },
            {
                "Description": "代理",
                "DemoValue": "AliCloudApiGateway",
                "ParamName": "CaProxy",
                "ParamType": "string"
            }
```

]

```
    }
}
```

API 网关

## 数据类型

### ApiGroupAttribute

**描述**

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| GroupId | String | API分组 ID，系统生成，全局唯一 |
| GroupName | String | API组名称 |
| SubDomain | String | API组对应的二级域名，自定义域名cname所用 |
| Description | String | 分组描述 |
| CreatedTime | String | 创建时间，格林威治时间 |
| ModifiedTime | String | 最后修改时间，格林威治时间 |
| RegionId | String | 分组所在区域 |
| TrafficLimit | Integer | 分组最高QPS限制，默认500，可申请提高 |
| BillingStatus | String | 计费状态，取值： NORMAL：正常 LOCKED：欠费锁定 |
| IllegalStatus | String | 违法锁定，取值： NORMAL：正常 LOCKED：违法锁定 |

### ApiHisItem

**描述**

列举API信息项的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|

API 网关

| RegionId | String | 所在的region |
|---|---|---|
| GroupId | String | API分组编号 |
| GroupName | String | API分组名称 |
| StageName | String | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |
| ApiId | String | API编号 |
| ApiName | String | API名称 |
| Description | String | API描述 |
| HistoryVersion | String | API定义的历史版本 |
| Status | String | 对应版本的API是否生效，取值为：ONLINE、OFFLINE，分别表示有效、无效 |
| DeployedTime | String | 发布时间（格林威治时间） |

### ApiInfo

**描述**

列举API信息项的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| RegionId | String | 所在的region |
| GroupId | String | API分组编号 |
| GroupName | String | API分组名称 |
| StageName | String | 环境名称，枚举为： RELEASE: 线上 TEST: 测试 |
| ApiId | String | API编号 |
| ApiName | String | API名称 |
| Description | String | API描述 |

API 网关

| Visibility | String | 可见性，枚举为： PUBLIC: 公开 PRIVATE: 私有 |
|---|---|---|
| BoundTime | String | 绑定时间 |

### ApiPluginSummary

**描述**

绑定到插件的API概要信息项

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| RegionId | String | 所在的region |
| GroupId | String | API分组编号 |
| GroupName | String | API分组名称 |
| ApiId | String | API编号 |
| ApiName | String | API名称 |
| Description | String | API描述 |
| StageName | String | Stage名称 |

### ApiSummary

**描述**

API概要信息项

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| RegionId | String | 所在的region |
| GroupId | String | API分组编号 |
| GroupName | String | API分组名称 |
| ApiId | String | API编号 |

API 网关

| ApiName | String | API名称 |
|---|---|---|
| Description | String | API描述 |
| Visibility | String | 可见性，可选值： PUBLIC: 公开 PRIVATE: 私有 |
| CreatedTime | String | 创建时间（格林威治时间） |
| ModifiedTime | String | 修改时间（格林威治时间） |

### AppAttribute

**描述**

列举APP的信息

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| AppId | Long | APP编号 |
| AppName | String | APP名称 |
| Description | String | APP描述信息 |
| CreatedTime | String | 创建时间（格林威治时间） |
| ModifiedTime | String | 修改时间（格林威治时间） |

### AppItem

**描述**

列举APP的信息

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| AppId | Long | APP编号 |
| AppName | String | APP名称 |
| Description | String | APP描述信息 |

API 网关

### AuthorizedApi

**描述**

应用和API的对应关系

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| RegionId | String | API所在区域 |
| GroupId | String | API分组 ID，系统生成，全局唯一 |
| GroupName | String | API分组名称 |
| StageName | String | API环境，取值： RELEASE：线上 TEST:测试 |
| Operator | String | 授权的人，取值： PROVIDER：API所有者 CONSUMER：API调用着 |
| ApiId | String | 系统自动生成API唯一标识符 |
| ApiName | String | API名称 |
| AuthorizationSource | String | 授权来源，取值： CONSOLE：控制台 API：API |
| Description | String | 授权说明 |
| AuthorizedTime | String | 授权时间，格林威治时间 |

### AuthorizedApp

**描述**

API的应用授权信息

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|

API 网关

| StageName | String | 环境名称，取值： RELEASE TEST |
|---|---|---|
| AppId | Long | 编号，系统生成，全局唯一 |
| AppName | String | 应用名称 |
| Operator | String | 授权的人，取值： PROVIDER：API所有者 CONSUMER：API调用者 |
| AuthorizationSource | String | 授权来源，取值： CONSOLE：控制台 API：API |
| Description | String | 授权说明 |
| AuthorizedTime | String | 授权时间，格林威治时间 |

### ConstantParameter

**描述**

常量入参信息项的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| ServiceParameterName | String | 后端参数名称 |
| ConstantValue | String | 参数值 |
| Location | String | 参数位置，取值为：BODY、HEAD、QUERY、 PATH |
| Description | String | 参数描述 |

### CustomDomain

**描述**

域名信息

**节点名**

**子节点**

API 网关

| 名称 | 类型 | 描述 |
|---|---|---|
| DomainName | String | 域名名称 |
| CertificateId | String | SSL证书ID，系统自动生成唯一编号 |
| CertificateName | String | SSL证书名称 |
| DomainCNAMEStatus | String | 域名解析情况，取值： RESOLVED：已解析 UNRESOLVED：未解析 |
| DomainBindingStatus | String | 自定义域名绑定状态，取值： BINDING：正常 BOUND：未生效 |

### DeployedApiItem

**描述**

列举API信息项的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| RegionId | String | 所在的region |
| GroupId | String | API分组编号 |
| GroupName | String | API分组名称 |
| StageName | String | 环境名称，可选值： RELEASE: 线上 TEST: 测试 |
| ApiId | String | API编号 |
| ApiName | String | API名称 |
| Description | String | API描述 |
| Visibility | String | 可见性，可选值： PUBLIC: 公开 PRIVATE: 私有 |
| DeployedTime | String | 发布时间（格林威治时间） |

API 网关

### DeployedInfo

**描述**

API发布信息项的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| StageName | String | 环境名称，取值为：RELEASE、TEST |
| EffectiveVersion | String | 有效的版本 |
| DeployedStatus | String | 部署状态，取值为：DEPLOYED、NONDEPLOYED，分别表示已部署、未部署 |

### DomainItem

**描述**

API的调用域名信息

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| DomainName | String | API的调用域名 |

### ErrorCodeSample

**描述**

错误码示例的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| Code | String | 错误码 |
| Message | String | 错误信息 |

API 网关

| Description | String | 描述 |
|---|---|---|

### MonitorItem

**描述**

监控信息项

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| ItemTime | String | 对应时间，按照ISO8601标准表示，并需要使用UTC时间。格式为： YYYY-MM-DDThh:mm:ssZ |
| ItemValue | String | 对应值 |

### PluginAttribute

**描述**

插件详情

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| PluginId | String | 插件Id |
| PluginType | String | 插件类型 |
| PluginName | String | 插件名称 |
| PluginData | String | 插件定义语句 |
| RegionId | String | 插件所在region |
| Description | String | 插件描述 |
| CreatedTime | String | 创建时间，格林威治时间 |
| ModifiedTime | String | 修改时间，格林威治时间 |

### Region

**描述**

API 网关区域信息的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| RegionId | String | 区域Id |
| LocalName | String | 区域名称 |
| EndPoint | String | 域名，例如：gateway.cn-hangzhou.aliyuncs.com |

### RequestConfig

**描述**

前端信息项

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestProtoc ol | String | API 支持的协议类型，可以多选，多选情况下以英文逗号隔开， 如：”HTTP,HTTPS”，取值为：HTTP、HTTPS |
| RequestHttpM ethod | String | HTTP Method，取值为：GET、POST、DELETE、PUT、HEADER、 TRACE、PATCH、CONNECT、OPTIONS |
| RequestPath | String | API path，比如API的完全地址为 http://api.a.com：8080/object/add? key1=value1&key2=value2，path是指/object/add这一部分 |
| BodyFormat | String | POST/PUT请求时，表示数据已何种方式传递给服务器，取值为：FORM、 STREAM，分别表示表单形式(k-v对应)、字节流形式 |
| PostBodyDescr iption | String | Body描述 |

### RequestParameter

**描述**

前端入参信息项的类型

**节点名**

**子节点**

API 网关

| 名称 | 类型 | 描述 |
|---|---|---|
| ApiParameterName | String | 参数名 |
| Location | String | 参数位置，取值为：BODY、HEAD、QUERY、PATH |
| ParameterType | String | 参数类型，取值为：String、Int、Long、Float、Double、 Boolean，分别表示字符、整型、长整型、单精度浮点型、双精度浮点型、布尔 |
| Required | String | 是否必填，取值为：REQUIRED、OPTIONAL，分别表示必填、 不必填 |
| DefaultValue | String | 默认值 |
| DemoValue | String | 示例 |
| MaxValue | Long | 当ParameterType=Int、Long、Float、Double，参数的最大值限定 |
| MinValue | Long | 当ParameterType=Int、Long、Float、Double，参数的最小值限定 |
| MaxLength | Long | 当ParameterType=String，参数的最大长度限定 |
| MinLength | Long | 当ParameterType=String，参数的最小长度限定 |
| RegularExpression | String | 当ParameterType=String，参数验证（正则表达式） |
| JsonScheme | String | 当ParameterType=String，JSON验证（Json Scheme） |
| EnumValue | String | 当ParameterType=Int、Long、Float、Double或String，允许输入的散列值，不同的值用英文的逗号分隔，形如：1,2,3,4,9 或A,B,C,E,F |
| DocShow | String | 文档可见，取值为：PUBLIC、PRIVATE |
| DocOrder | Integer | 文档中顺序 |
| Description | String | 参数描述 |

### ServiceConfig

**描述**

后端服务调用信息项

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|

API 网关

| ServiceProto col | String | 后端服务协议类型，目前只支持HTTP/HTTPS |
|---|---|---|
| ServiceAddre ss | String | 调用后端服务地址，比如后端服务完全地址为 http://api.a.com:8080/object/add? key1=value1&key2=value2，ServiceAddress是指 http://api.a.com:8080这一部分 |
| ServicePath | String | 调用后端服务path，比如后端服务完全地址为 http://api.a.com:8080/object/add? key1=value1&key2=value2，ServicePath是指/object/add这一部分 |
| ServiceHttpM ethod | String | 调用后端服务HTTP协议时的Method，取值为：GET、POST、DELETE、 PUT、HEADER、TRACE、PATCH、CONNECT、OPTIONS |
| ServiceTimeo ut | String | 后端服务超时时间，单位：毫秒 |
| Mock | String | 是否采取Mock模式，目前可以取值：TRUE：启用Mock模式FALSE：不启用 Mock模式 |
| MockResult | String | 如果启用Mock模式，返回的结果 |
| ContentType Catagory | String | 调用后端服务HTTP服务时，ContentType头的取值策略： DEFAULT：使用 API网关默认的值 CUSTOM：自定义 CLIENT：使用客户端上行的 ContentType的头 |
| ContentType Value | String | 调用后端服务HTTP服务，ContentTypeCatagory的值为DEFAULT或者 CUSTOM时，ContentType头的取值 |
| ServiceVpcE nable | Boolean | 是否启用VPC通道，目前可以取值： TRUE：启用VPC通道 FALSE：不启用 VPC |
| VpcId | String | 当VPC通道时，后端服务所在VPC ID |

### ServiceParameter

**描述**

后端服务调用入参信息项的类型

**节点名**

**子节点**

API 网关

| 名称 | 类型 | 描述 |
|---|---|---|
| ServiceParameterName | String | 后端参数名称 |
| Location | String | 参数位置，取值为：BODY、HEAD、QUERY、PATH |
| ParameterType | String | 后端参数类型，取值为：STRING、NUMBER、 BOOLEAN，分别表示字符、数值、布尔 |

### ServiceParameterMap

**描述**

后端服务调用入参和前端入参映射

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| ServicePara meterName | String | 后端参数名称 |
| RequestPara meterName | String | 对应前端入参名称。 这个值必须存在于RequestParametersObject中，匹配于 RequestParam.ApiParameterName |

### Special

**描述**

特殊流控策略数据项的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| SpecialKey | String | 根据 SpecialType 对应的AppId或者是用户账号 |
| TrafficValue | Integer | 流控值 |

### SpecialPolicy

**描述**

特殊流控策略信息项的类型 API 网关

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| SpecialType | String | 特殊流控类型，可选值： APP: 应用 USER: 用户 |
| Specials | Special | 由 Special 组成的数组格式，返回特殊流控策略数据项信息 |

### StageInfo

**描述**

运行环境信息

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| StageId | String | 运行环境编号 |
| StageName | String | 运行环境名称 |
| Description | String | 运行环境描述 |

### SystemParameter

**描述**

系统入参信息项的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| ParameterName | String | 系统参数名，取值为：CaClientIp、CaDomain、 CaRequestHandleTime、CaAppId、CaRequestId、CaHttpSchema、 CaProxy |
| ServiceParamete rName | String | 对应后端参数名称 |
| Location | String | 参数位置，取值为：BODY、HEAD、QUERY、PATH |

API 网关

| DemoValue | String | 示例 |
|---|---|---|
| Description | String | 参数描述 |

### SystemParamItem

**描述**

系统参数信息的类型

**节点名**

**子节点**

| 名称 | 类型 | 描述 |
|---|---|---|
| ParamName | String | 参数名称 |
| ParamType | String | 参数类型 |
| DemoValue | String | 示例 |
| Description | String | 参数描述 |

API 网关

## 错误码参考

当您调用API网关开放的管控OpenAPI时，如CreateAPI、ModifyAPI、DeleteAPI等，您可能遇到以下错误码。

**服务端错误码**

HttpCode为5xx，表示服务不可用。此时建议重试。

| 错误代码 | 描述 | Http 状态码 | 语义 | 解决方案 |
|---|---|---|---|---|
| ServiceUnavailabl e | The request has failed due to a temporary failure of the server. | 503 | 服务不可用，有时是API返回超时导致 | 建议重试。 |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 | 内部错误 | 请提工单咨询 |

**客户端错误码**

HttpCode为4xx，表示业务错误。一般为参数错误、权限限制、业务逻辑错误等问题，此时需要仔细查看错误码，并针对性解决问题。

| 错误代码 | 描述 | Http 状态码 | 语义 | 解决方案 |
|---|---|---|---|---|
| Repeated%s | The specified %s is repeated. | 400 | 某参数重复（%s 是占位符，实际调用会给出明确的参数名或提示。） | 建议按照提示修改重复的参数后重试。 |
| RepeatedCommit | Resubmit request. | 400 | 请求重复 | 请不要频繁提交请求。 |
| Missing%s | The %s is mandatory for this action. | 400 | 缺少参数 %s | 根据具体返回补充缺少的参数，重试请求。 |
| MissingAppIdOrA ppOwner | AppId or AppOwner must have a valid value. | 400 | 缺少参数 AppId 或者 AppOwner | 参数 AppId 和 AppOwner 不能同时为空。 |
| Invalid%s | The specified parameter %s value is not valid. | 400 | 参数无效 | 根据返回提示的具体参数，查看相关参数约束，修改后重试。 |
| NotFound%s | Cannot find resource according to your specified %s. | 400 | 找不到资源 | 根据指定的参数%s 找不到资源，建议检查%s是否正确。 |
| InvalidFormat%s | The specified parameter %s value is not well formatted. | 400 | 参数格式错误 | 建议根据实际返回提示，查看%s的格式要求，修改后重试。 |

| PI 网关 |  |  | 开发 | 指南（旧）·错误码参考 |
|---|---|---|---|---|

| Duplicate%s | The specified parameter %s value is duplicate. | 400 | 参数重复 | 某请求参数不允许重复，建议检查修正后重试。 |
|---|---|---|---|---|
| DependencyViola tion%s | The specified %s has %s definitions. | 400 | 参数依赖错误 | 指定参数被依赖， 不能随意删除，请先解除依赖。 |
| Forbidden%s | Not allowed to operate on the specified %s. | 403 | 无权操作/操作禁止 | 您无权执行该操作。 |
| NoPermission | User is not authorized to operate on the specified resource. | 403 | 无权操作 | RAM 鉴权不通过。 |
| ExceedLimit%s | The specified %s count exceeds the limit. | 400 | 超出个数限制 | 一般指用户账户下创建的 API、API 分组或者APP超出个数限制。 |
| UserNotFound | The specified user can not be found. | 404 | 指定用户找不到 | 根据输入的用户信息找不到该用户。 |
| Invalid%s.Length Limit | The parameter %s length exceeds the limit. | 400 | 长度超限 | 参数%s超出长度限制，建议修正后重试。 |
| InvalidApiDefault | The ApiDefault value exceeds limit. | 400 | 流控 API 默认值超过限制值 | 该值数值不能超过1 亿 |
| InvalidAppDefault | The AppDefault value must smaller than the UserDefault and ApiDefault. | 400 | AppDefault 的值不符合规则 | 该值需要小于 API 流控值和用户流控值。 |
| InvalidUserDefaul t | The UserDefault value must bigger than the AppDefault and smaller than the ApiDefault. | 400 | UserDefault 的值不符合规则 | 该值需要小于 API 流控值并大于 APP 流控值。 |
| InvalidParamMap ping | Parameters must be fully mapped. | 400 | 参数映射无效 | 创建 API 时，前后端参数映射需要是全映射。即每个入参都需要配置后端参数名称。 |

API 网关

| EqualSignature | The new signature is the same as the old. | 400 | 新密钥与旧的相等 | 修改后端签名密钥时，新设置的 Key 和 Secret 不能跟原来的一样。 |
|---|---|---|---|---|
| CertificateNotMat ch | The domain does not match the one in the certificate. | 400 | 证书不匹配 | 指定域名与证书内域名不匹配。 |
| CertificateKeyNot Match | The certificate private key does not match the public key. | 400 | 证书密钥不匹配 | 证书的公钥和私钥不匹配。 |

**客户端公用错误码**

HttpCode为4xx，调用全阿里云产品的OpenAPI均可能遇到，表示业务错误。一般为请求格式错误、请求方式错误、必填参数丢失、参数格式错误、签名错误、流控限制等问题。此时需查看具体错误码，针对性解决问题。

| 报错场景 | 错误码 | 错误提示 | 状态码 | 建议 |
|---|---|---|---|---|
| API 找不到。 | InvalidApi.NotFou nd | Specified api is not found,please check your url and method. | 404 | 请检查指定的 action 接口名称是否正确，注意大小写区分。 |
| 缺少必填参数。 | Missing{Paramet erName} | {ParameterName } is mandatory for this action. | 400 | 指定参数为必填参数，请传入。 |
| AccessKeyId 找不到 | InvalidAccessKey Id.NotFound | Specified access key is not found. | 404 | 请检查调用时是否传入正确的 AccessKeyId。 |
| AccessKeyId 被禁用。 | InvalidAccessKey Id.Inactive | Specified access key is disabled. | 400 | 检查 AK 是否可用。 |
| 时间戳格式不对( Date 和 Timestamp)。 | InvalidTimeStam p.Format | Specified time stamp or date value is not well formatted. | 400 | 检查时间戳。 |
| 用户时间和服务器时间超过15分钟。 | InvalidTimeStam p.Expired | Specified time stamp or date value is expired. | 400 | 检查时间戳。 |
| SignatureNonce 重复 | SignatureNonceU sed | Specified signature nonce was used already. | 400 | 确认客户端调用时 SignatureNonce 是否重复 |
| 返回值格式不正确。 | InvalidParameter. Format | Specified parameter format is not valid. | 400 | 仅支持 XML/JSON。 |

API 网关

| 参数值校验不通过。 | Invalid{Paramete rName} | Specified parameter {ParameterName } is not valid. | 400 | 请检查指定参数的值。 |
|---|---|---|---|---|
| Http 请求方法不支持。 | UnsupportedHTT PMethod | Specified signature is not matched with our calculation. | 400 | 请检查请求 Method。 |
| 签名方法不支持。 | InvalidSignature Method | Specified signature method is not valid. | 400 | 默认可以不填写该值。 |
| 签名不通过 | SignatureDoesNo tMatch | Specified signature is not matched with our calculation. | 400 | 签名不通过。 |
| 用户调用频率超限。 | Throttling.User | Request was denied due to user flow control. | 400 | 请稍后访问，降低访问频率。 |
| API 访问频率超限。 | Throttling.API | Request was denied due to api flow control. | 400 | 请稍后访问，降低访问频率。 |
| 缺少 AccessKeyId。 | MissingSecurityT oken | SecurityToken is mandatory for this action. | 400 | 请检查是否传入有效AccessKeyId。 |
