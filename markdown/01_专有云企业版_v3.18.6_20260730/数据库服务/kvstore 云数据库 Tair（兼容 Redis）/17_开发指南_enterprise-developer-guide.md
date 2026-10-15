---
title: "云数据库 Tair（兼容 Redis） 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 104
source_pdf: "17_开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/kvstore/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云数据库 Tair（兼容 Redis） 开发指南

云数据库 Tair（兼容Redis）开发指

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
云数据库 Tair（兼容Redis）开发指
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

本文为您介绍调用流程及可以参考的文档资料。

**流程图**

云数据库 Tair（兼容Redis）开发指

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
云数据库 Tair（兼容Redis）开发指

## 准备工作

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

### 获取AccessKey

访问身份验证中通过使用AccessKey ID和AccessKey Secret对称加密的方法来验证某个请求的发送者身份。AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。本文将为您描述如何获取通过RAM授权的AccessKey。

**前提条件**

只有运营管理员和一级组织管理员可以获取组织AccessKey。 云数据库 Tair（兼容Redis）开发指

**背景信息**

AccessKey支持两种授权模式： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。 本文仅为您介绍如何获取通过RAM授权的AccessKey，通过STS授权的AccessKey获取方式请参见获取 STS AccessKey。 推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

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
云数据库 Tair（兼容Redis）开发指
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取公共Header参数

调用API时需要提供多个Header参数。本文为您介绍如何获取这些参数。并对调用后的一些返回值做出解释。

**获取Region ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理**>**地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看**Region****名称**，即为Region ID。

**获取组织ID**

组织ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取组织ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
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
云数据库 Tair（兼容Redis）开发指
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

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择利用STS方式，调用专有云的产品API。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 使用以下代码，通过角色的 `RAM Role` 获得 `stsAK` 、 `stsSK` 和 `stsToken` 。
云数据库 Tair（兼容Redis）开发指

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
云数据库 Tair（兼容Redis）开发指

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

云数据库 Tair（兼容Redis）开发指

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
云数据库 Tair（兼容Redis）开发指
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

云数据库 Tair（兼容Redis）开发指 `//` 创建`DefaultAcsClient`实例并初始化。

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

云数据库 Tair（兼容Redis）开发指

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

`//`必填值，调用来源说明云数据库 Tair（兼容Redis）开发指 `//` 必填值，调用来源说明

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
云数据库 Tair（兼容Redis）开发指

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 示例代码如下： 云数据库 Tair（兼容Redis）开发指

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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 云数据库 Tair（兼容Redis）开发指

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

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 云数据库 Tair（兼容Redis）开发指

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

云数据库 Tair（兼容Redis）开发指

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

云数据库 Tair（兼容Redis）开发指
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
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
```

)

```
request.set_protocol_type('https') # 使用https client.do_action_with_exception(request)
```

云数据库 Tair（兼容Redis）开发指

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

) 云数据库 Tair（兼容Redis）开发指

## API参考

### API 概览

| API | 描述 |
|---|---|
| CreateInstance | 创建实例 |
| DeleteInstance | 释放实例 |
| ModifyInstanceSpec | 变更实例 |

表 2. 实例管理接口

| API | 描述 |
|---|---|
| DescribeInstanceAttribute | 查询实例详情 |
| DescribeInstances | 查询实例基础信息 |
| DescribeRegions | 查询实例可售卖地域 |
| DescribeSecurityIps | 查询允许访问实例的 IP 名单 |
| FlushInstance | 清空实例 |
| ModifyInstanceAttribute | 修改实例属性 |
| ModifyInstanceMaintainTime | 修改实例可运维时间 |
| ModifySecurityIps | 修改实例白名单 |
| ModifyInstanceNetExpireTime | 修改经典网络域名的保留时间 |
| SwitchNetwork | 修改网络类型 |

表 3. 备份恢复接口

| API | 描述 |
|---|---|
| CreateBackup | 创建备份 |
| ModifyBackupPolicy | 修改备份策略 |
| DescribeBackupPolicy | 查询备份策略 |
| DescribeBackups | 显示备份列表 |
| RestoreInstance | 基于备份集回滚实例 |

表 4. 监控管理接口

| API | 描述 |
|---|---|

云数据库 Tair（兼容Redis）开发指

| DescribeMonitorItems | 查看监控项列表 |
|---|---|
| DescribeHistoryMonitorValues | 查看历史监控 |

表 5. 参数管理接口

| API | 描述 |
|---|---|
| DescribeInstanceConfig | 查看实例参数配置 |
| ModifyInstanceConfig | 修改参数配置 |

### 请求结构

**服务地址**

Redis API 的服务接入地址为 `r-kvstore.example.com` 。

**说明**

example.com是项目自定义的访问域名，请联系管理员获取该域名。

**通信协议**

支持通过 HTTP 或 HTTPS 通道进行请求通信。为了获得更高的安全性，推荐您使用 HTTPS 通道发送请求。

**请求方法**

支持 HTTP GET 方法发送请求，这种方式下请求参数需要包含在请求的 URL 中。

**请求参数**

每个请求都需要指定要执行的操作，即 Action 参数（例如 CreateInstance），以及每个操作都需要包含的公共请求参数和指定操作所特有的请求参数。

**字符编码**

请求及返回结果都使用 UTF-8 字符集进行编码。

### 公共参数

公共请求参数是指每个接口都需要使用到的请求参数。

**公共请求参数**

表 1. 公共请求参数

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | String | 是 | 返回值的类型，支持 JSON 与 XML。默认为 XML。 |
| Version | String | 是 | API 版本号，为日期形式：YYYY-MM-DD，本版本对应为 2015-01-01。 |
| AccessKeyId | String | 是 | 阿里云颁发给用户的访问服务所用的密钥 ID。 |

云数据库 Tair（兼容Redis）开发指

| Signature | String | 是 | 签名结果串，关于签名的计算方法，请参见签名机制。 |
|---|---|---|---|
| SignatureMeth od | String | 是 | 签名方式，目前支持 HMAC-SHA1。 |
| Timestamp | String | 是 | 请求的时间戳。日期格式按照ISO8601标准表示，并需要使用 UTC 时间。格式为 YYYY-MM-DDThh:mm:ssZ 。例如，2016-01-01T12:00:00Z（为北京时间2016年1月1日 20点0分0秒）。 |
| SignatureVersi on | String | 是 | 签名算法版本，目前版本是1.0。 |
| SignatureNonc e | String | 是 | 唯一随机数，用于防止网络重放攻击。用户在不同请求时间要使用不同的随机数值。 |

```
https:// r-kvstore.example.com/ ?Format=json &Version=2015-01-01 &Signature=Pc5xxxxxxxxxxxxxxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2016-01-01T12:00:00Z
```

**公共返回参数**

用户每次发送的接口调用请求，无论成功与否，系统都会返回一个唯一识别码 RequestId 给用户。

```xml
<?xml version="1.0" encoding="utf-8"?>
```

<!—结果的根结点`-->` <接口名称`+Response>` <!—返回请求标签`-->`

```xml
<RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId>
```

<!—返回结果数据`-->` `</`接口名称`+Response>`

### 返回结果

调用 API 服务后返回数据采用统一格式。返回的 HTTP 状态码为 `2xx` 代表调用成功；返回 `4xx` 或 `5xx` 的 HTTP 状态码代表调用失败。调用成功返回的数据格式主要有 XML 和 JSON 两种， 外部系统可以在请求时传入参数来制定返回的数据格式，默认为 XML 格式。 本文档中的返回示例为了便于用户查看，做了格式化处理，实际返回结果是没有进行换

**说明**

行、缩进等处理的。

**成功结果**

XML 返回结果包括请求是否成功信息和具体的业务数据。示例如下： 云数据库 Tair（兼容Redis）开发指

```xml
<?xml version="1.0" encoding="utf-8"?>
```

<!—结果的根结点`-->` <接口名称`+Response>` <!—返回请求标签`-->`

```xml
<RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId>
```

<!—返回结果数据`-->` `</`接口名称`+Response>` JSON 示例：

```json
{ "RequestId": "4C4fdsf38-3910-447D-87AD-AC078932216",
```

`/*` 返回结果数据 `*/`

```
}
```

**错误结果**

调用接口出错后，将不会返回结果数据。调用方可根据附表错误代码表来定位错误原因。当调用出错时，HTTP 请求返回一个 `4xx` 或 `5xx` 的 HTTP 状态码。返回的消息体中是具体的错误代码及错误信息。另外还包含一个全局唯一的请求 ID:RequestId 和一个您该次请求访问的站点 ID:HostId。若在调用方找不到错误原因，可以联系专有云客服，并提供该 HostId 和 RequestId，以便我们尽快帮您解决问题。

```xml
<?xml version="1.0" encoding="UTF-8"?> <Error> <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId> <HostId> r-kvstore.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported.</Message> </Error>
```

JSON 示例：

```json
{ "RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF", "HostId": " r-kvstore.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported." }
```

### 签名机制

Redis 服务会对每个访问的请求进行身份验证，所以无论使用 HTTP 还是 HTTPS 协议提交请求，都需要在请求中包含签名（Signature）信息。Redis 服务通过使用 Access Key ID 和 Access Key Secret 进行对称加密的方法来验证请求的发送者身份。 Access Key ID 和 Access Key Secret 由阿里云官方颁发给访问者（可以通过阿里云官方网站申请和管理），其中 Access Key ID 用于标识访问者的身份；Access Key Secret 是用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密，只有阿里云和用户知道。

**签名处理**

用户在访问时，按照下面的方法对请求进行签名处理： 云数据库 Tair（兼容Redis）开发指
1. 使用请求参数构造规范化的请求字符串（Canonicalized Query String）。
i. 按照参数名称的字典顺序对请求中所有的请求参数（包括文档中描述的“公共请求参数”和指定请求接口的自定义参数，但不能包括“公共请求参数”中提到 Signature 参数本身）进行排序。 当使用 GET 方法提交请求时，这些参数就是请求 URI 中的参数部分（即 URI

**说明**

中“?”之后由“&”连接的部分）。 ii. 对每个请求参数的名称和值进行编码。 名称和值要使用 UTF-8 字符集进行 URL 编码。URL 编码的编码规则如下： 对于字符 A~Z、a~z、0~9 以及字符“-”、“_”、“.”、“~”不编码；

|  |  |  | XY |
|---|---|---|---|
| %22 |  | ； |  |
|  | %XY%ZA… |  |  |

英文空格（）要编码成 %20 ，而不是加号（+）。 一般支持 URL 编码的库（比如 Java 中的 java.net.URLEncoder）都是按

**说明**

照 `application/x-www-form-urlencoded` 的 MIME 类型的规则进行编码的。实现时可以直接使用这类方式进行编码，把编码后的字符串中加号（+）替换成 %20 、星号（*）替换成 %2A 、 %7E 替换回波浪号（~），即可得到上述规则描述的编码字符串。 iii. 对编码后的参数名称和值使用英文等号（=）进行连接。 iv. 再把英文等号连接得到的字符串按参数名称的字典顺序依次使用&符号连接，即得到规范化请求字符串。
2. 使用上一步构造的规范化字符串按照下面的规则构造用于计算签名的字符串：

```
 StringToSign=
 HTTPMethod + “&” +
 percentEncode(“/”) + ”&” +
 percentEncode(CanonicalizedQueryString)
```

其中：

| HTTPMethod 是提交请求用的 HTTP 方法，比如 percentEncode(“/”) 是按照步骤 1.b 中描述的 %2F 。 |  |
|---|---|
|  | percentEncode(“/”) |
| %2F |  |
|  | percentEncode(CanonicalizedQueryString) |

3. 按照 RFC2104 的定义，使用上面的用于签名的字符串计算签名 HMAC 值。
计算签名时使用的 Key 就是用户持有的 Access Key Secret 并加上一个“&”字符

**说明**

（ASCII:38），使用的哈希算法是 SHA1。
4. 按照 Base64 编码规则把上面的 HMAC 值编码成字符串，即得到签名值（Signature）。
5. 将得到的签名值作为 Signature 参数添加到请求参数中，即完成对请求签名的过程。
得到的签名值在作为最后的请求参数值提交给 Redis 服务器的时候，要和其他参数一

**说明**

样，按照 RFC3986 的规则进行 URL 编码。

**示例**

以 DescribeDBInstances 为例，签名前的请求 URL 如下： 云数据库 Tair（兼容Redis）开发指

```
http://r-kvstore.example.com/?Timestamp=2013-06- 01T10:33:56Z&Format=XML&AccessKeyId=testid&Action=DescribeInstances&SignatureMethod=HMAC- SHA1&RegionId=region1&SignatureNonce=NwDAxvLU6tFE0DVb&Version=2015-01- 01&SignatureVersion=1.0
```

计算得到的待签名字符串 StringToSign 为：

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeInstances&Format%3DXML&RegionId%3Dregion1&S natureMethod%3DHMAC- SHA1&SignatureNonce%3DNwDAxvLU6tFE0DVb&SignatureVersion%3D1.0&Timestamp%3D2013-06-01T10 %253A33%253A56Z&Version%3D2015-01-01
```

假如使用的 Access Key Id 是 `testid` ，Access Key Secret 是 `testsecret` ，用于计算 HMAC 的 Key 就是 `testsecret&` ，则计算得到的签名值是 `BIxxxxxxxxxxxxxxxxxxxxxx=` 。 签名后的请求 URL 为（注意增加了 Signature 参数）：

```
http://r-kvstore.example.com/?Timestamp=2013-06- 01T10%3A33%3A56Z&Format=XML&AccessKeyId=testid&Action=DescribeInstances&SignatureMethod=H
```

`C-`

```
SHA1&RegionId=region1&SignatureNonce=NwDAxvLU6tFE0DVb&SignatureVersion=1.0&Version=2015- 01-01&Signature=BIPOMlxxxxxxxxxxxxxxxxxxu8LXBeZtLQkJTw6iFvw1E%3D
```

### 如何使用RAM授权

#### 使用 RAM 实现资源授权

您通过云账号创建的实例，都是该账号拥有的资源。默认情况下，账号对自己的资源拥有完整的操作权限。 使用阿里云的 RAM（Resource Access Management）服务，您可以将云账号下的资源的访问及管理权限授予 RAM 中子用户。 如果您不需要使用 RAM，请略过此章节。

**说明**

#### RAM 中可授权的资源类型

云数据库KVStore for Redis可以在 RAM 中进行授权的资源类型仅一种：instance。 在通过 RAM 进行授权时，资源的描述方式如下：

| 资源类型 | 授权策略中的资源描述方式 |
|---|---|
| Instance | acs:kvstore:$regionid:$accountid:instance/$insta nceid acs:kvstore:$regionid:$accountid:instance/ acs:kvstore:::instance/ |

其中，所有 $regionid 应为某个 region 的 ID，或者 * ；所有 $instanceid 应为某个 instance 的 ID，或者 * ；以此类推，$account-id 是云账号的数字 ID，可以用 * 代替。

#### RAM 中可对资源进行授权的 Action

云数据库 Tair（兼容Redis）开发指 RenewInstance RenewMultiInstance TransformToPrePaid

#### API 的鉴权规则

当子用户通过 API 进行资源访问时，后台向 RAM 进行权限检查，以确保调用者拥有响应权限。 每个不同的 API 会根据涉及到的资源以及 API 的语义来确定需要检查哪些资源的权限。具体地，每个 API 的鉴权规则见下表。表 1. 鉴权规则

| Action | 鉴权规则 |
|---|---|
| CreateDBInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DeleteInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceSpec | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| RenewInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| RenewMultiInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| TransformToPrePaid | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$insta nceid |

云数据库 Tair（兼容Redis）开发指

| FlushInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
|---|---|
| DescribeInstances | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceMaintainTime | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifySecurityIps | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| SwitchNetwork | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceNetExpireTime | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| CreateBackup | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeBackups | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| RestoreInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeHistoryMonitorValues | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$insta nceid |

### 生命周期管理

#### CreateInstance

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 Tair（兼容Redis）开发指

| <公共请求参数 > | 无 | 是 | 无 |  | 参见公共请求参数。 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Action | String | 是 | CreateInstanc e |  | 操作接口名，取值： CreateInstance。 |  |  |  |  |
| InstanceName | String | 否 | apitest |  | 实例名称。 名称为2~128个字符，以大小写英文字母或中文开头，不支持空格和特殊字符 @/:=”<>{[]} 。 |  |  |  |  |
| Password | String | 否 | Pass!123456 |  | 实例密码。 字符类型，8~30个字符， 需同时包含大写字母、小写字母和数字。 说明暂时不支持 !<>()[]{},`~.- @#$%^&* 之类的特殊符号。 _ |  |  |  |  |
|  |  |  |  |  |  |  | !<>()[]{},`~.- |  |  |
|  |  |  |  |  |  | @#$%^&* _ |  |  |  |
| InstanceClass | String | 是 | redis.master.s mall.default |  | Redis实例规格，更多信息，请参见 《用户指南》中实例规格章节。 |  |  |  |  |
| RegionId | String | 是 | cn-hangzhou |  | 申请的存储实例所在区域，可调用 DescribeRegions获取可用的数据中心。 |  |  |  |  |
| ZoneId | String | 否 | cn-hangzhou-e |  | RegionId 下的可用区，可调用 DescribeRegions获取可用的可用区。 |  |  |  |  |
| Token | String | 否 | ChargeType |  | 用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一， 大小写敏感、不超过64个ASCII字符。 |  |  |  |  |
| NetworkType | String | 否 | VPC |  | 网络类型： CLASSIC：经典网络，默认为经典网络。 VPC：专有网络 |  |  |  |  |
| VpcId | String | 否 | vpc- bp1nme44gek 34slfc**** |  | VPC 网络 ID。 |  |  |  |  |

云数据库 Tair（兼容Redis）开发指

| VSwitchId | String | 否 | vsw- bp1e7clcw529l 773d**** | 虚拟交换机 ID。 说明如果传入了VpcId参数，则本参数必须传入。 |
|---|---|---|---|---|
| PrivateIp | String | 否 | 172.16.0.*** | 私有 IP 地址。 |
| SrcDBInstanceI d | String | 否 | r- bp1zxszhcgatn x**** | 基于某个实例的备份集创建实例有效， 输入产生备份集的实例 ID。 |
| BackupId | String | 否 | 111111111 | 基于某个实例的备份集创建实例有效， 输入产生备份集 ID。可调用 DescribeBackups接口获取。 |
| InstanceType | String | 否 | Redis | 实例类型，取值： Redis，Memcache。 默认为 Redis。 |
| EngineVersion | String | 否 | 5.0 | 引擎版本号（Redis经典版本）。 取值：2.8（不推荐，计划停止全面支持）、4.0（不推荐）、5.0、6.0、 7.0 。 默认值：5.0。 |
| CpuType | String | 否 | intel | CPU芯片架构。 取值：intel/hygon/kunpeng等。可以通过接口：DescribeCpuTypes 获取对应取值。 |
| ipVersionSelec tedType | String | 否 | IPv4 | IP类型，默认IPv4。取值范围： IPv4 IPv4v6 |
| securityIPv6Lis t | String | 否 | 2001:0db8:85 a3:0000:0000: 8a2e:0370:xxx x | IPv6白名单。 |
| securityIPList | String | 否 | 192.168.1.xxx | IPv4白名单。 |

**返回参数**

表 2. 返回参数云数据库 Tair（兼容Redis）开发指

| 名称 | 参数类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |
| InstanceId | String | r-bp1zxszhcgatnx**** | 实例ID（全局唯一）。 |
| InstanceName | String | apitest | 实例名称。 |

**说明**

出于历史兼容性考虑，该函数会有些返回结构在文档中并未提及（如 Config，Region 等），后续阿里云将逐步把这些字段删除，请您在调用 API 时不要依赖这些在文档中没有涉及的返回字段。

**请求示例**

```
https://r-kvstore.example.com
```

?<公共请求参数>

```
&RegionId=cn-hangzhou &Password=Pass!123456 &InstanceClass=redis.master.small.default
```

**返回示例**

XML格式：

```xml
    <InstanceId>r-n8r8c5119d2e****</InstanceId>
    <InstanceName>testdb</InstanceName>
```

JSON格式：

```json
{ "InstanceId":"r-n8r8c5119d2e****", "InstanceName":"testdb" }
```

#### DeleteInstance

调用DeleteInstance接口释放Redis实例，调用时要求实例状态为**运行中**。

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 Tair（兼容Redis）开发指

| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
|---|---|---|---|---|
| Action | String | 是 | DeleteInstance | 系统规定参数，取值： DeleteInstance。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例 ID（全局唯一）。 |

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.example.com &InstanceId=r-n8r8c5119d2e****
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>5D622714-AEDD-4609-9167-F5DDD3D190D2</RequestId>
```

JSON格式：

```json
{
    "RequestId": "5D622714-AEDD-4609-9167-F5DDD3D190D2"
}
```

#### ModifyInstanceSpec

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 Tair（兼容Redis）开发指

| Action | String | 是 | ModifyInsta nceSpec | 操作接口名，取值：ModifyInstanceSpec。 |
|---|---|---|---|---|
| InstanceId | String | 是 | r- bp1zxszhcg atnx**** | 实例 ID。 |
| InstanceClas s | String | 是 | redis.logic.s harding.drre dissdb1g.1d b.0rodb.4pr oxy.default | Tair实例的规格。 |
| PreserveBan dwidth | Boolean | 否 | false | 带宽决策逻辑。 true：使用当前实例实际带宽值。 false：使用目标规格定义的默认带宽。 |

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| OrderId | String | 20722623431**** | 订单ID。 |

**请求示例**

```
https://r-kvstore.example.com &InstanceId=r-n8r8c5119d2e**** &InstanceClass= redis.master.mid.default
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>A4828C10-AF0A-4CD7-8FBE-737C6CC1193E</RequestId>
      <OrderId>20722623431****</OrderId>
```

JSON格式： 云数据库 Tair（兼容Redis）开发指

```json
{
    "RequestId": "A4828C10-AF0A-4CD7-8FBE-737C6CC1193E",
    "OrderId": "20722623431****"
}
```

### 实例管理

#### RestartInstance

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 是 | RestartInstance | 接口名，固定值 RestartInstance。 |
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID。 |
| EffectiveTi me | Strin g | Query | 否 | Immediately | 重启时间，取值： Immediately ：默认值，立即重启。 MaintainTime ：可运维时间段重启。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | EFC9161F-15E3- 4A6E-8A99- C33331**** | 请求ID。 |
| InstanceId | String | r- bp1zxszhcgatnx*** * | 实例ID。 |
| TaskId | String | 11111**** | 任务ID。 |

**示例**

请求示例云数据库 Tair（兼容Redis）开发指

```
&Action= &InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TaskId":"11111****",
 "RequestId":"EFC9161F-15E3-4A6E-8A99-C33331****",
 "InstanceId":"r-bp1zxszhcgatnx****"
}
```

#### FlushExpireKeys

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID。 |
| EffectiveTi me | Strin g | Query | 否 | Immediately | 执行时间，取值： Immediately ：立即执行，默认值。 MaintainTime ：在可维护时间段执行。 您可以调用 ModifyInstanceMain tainTime接口修改 Redis实例的可维护时间段。 |
| Action | Strin g | Query | 是 | FlushExpireKeys | 接口名，固定值 FlushExpireKeys。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

云数据库 Tair（兼容Redis）开发指

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TaskId | String | 21986**** | 任务ID。 |
| RequestId | String | 82E30AB7-E3A4- 46AC-88A0- 3E4DCDC5**** | 请求ID。 |
| InstanceId | String | r- bp1zxszhcgatnx*** * | 实例ID。 |

**示例**

请求示例

```
&InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TaskId":"21986****",
 "RequestId":"82E30AB7-E3A4-46AC-88A0-3E4DCDC5****",
 "InstanceId":"r-bp1zxszhcgatnx****"
}
```

#### DescribeLogicInstanceTopology

调用DescribeLogicInstanceTopology接口查询Redis实例的逻辑拓扑结构。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RedisShardList | Array |  | 分片详情，包含NodeInfo等子节点信息。 |

| 云数据库 Tair（兼容南·API参考 | Redis）开发指 |  |  |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -NodeId | String | r- bp10noxlhcoim2** **-db-0#688**** | 节点ID。 |
| -Connection | String | 10000 | 连接数限制。 |
| -Bandwidth | String | 96 | 节点的带宽限制，单位为MB/s。 |
| -Capacity | String | 2048 | 节点的容量，单位为MB。 |
| -NodeType | String | db | 节点类型，返回值： proxy ：代理节点。 db ：数据节点。 |
| RequestId | String | 794120D1-E0CF- 4713-BAE4- EBAEA04506AF | 请求ID。 |
| InstanceId | String | r- bp1zxszhcgatnx*** * | 实例的ID。 |
| RedisProxyList | Array |  | 代理详情，包含代理节点信息。 |
| -NodeId | String | r- bp10noxlhcoim2** **-proxy- 3#542**** | 节点ID。 |
| -Connection | String | 320000 | 连接数限制。 |
| -Bandwidth | String | 96 | 节点的带宽限制，单位为MB/s。 |
| -Capacity | String | 5120 | 节点的容量，单位为MB。 |
| -NodeType | String | proxy | 节点类型，返回值： db ：数据节点。 normal ：管理节点，由Proxy节点（代理节点）和CS节点（配置管理节点）组成。部分实例不会返回normal，而是分别返回 proxy和cs。 |

**示例**

请求示例云数据库 Tair（兼容Redis）开发指

```
http(s)://[Endpoint]/?Action=DescribeLogicInstanceTopology &InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RedisShardList":{
  "Capacity":"2048",
  "Bandwidth":"96",
  "NodeType":"db",
  "NodeId":"r-bp10noxlhcoim2****-db-0#688****",
  "Connection":"10000"
 },
 "RequestId":"794120D1-E0CF-4713-BAE4-EBAEA04506AF",
 "InstanceId":"r-bp1zxszhcgatnx****",
 "RedisProxyList":{
  "Capacity":"5120",
  "Bandwidth":"96",
  "NodeType":"proxy",
  "NodeId":"r-bp10noxlhcoim2****-proxy-3#542****",
  "Connection":"320000"
 }
}
```

#### DescribeEngineVersion

调用DescribeEngineVersion接口查询Redis实例的大版本和小版本信息，同时可查询到小版本的发布日志信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID，可调用 DescribeInstances接口获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| MajorVersion | String | 5.0 | 实例的大版本。 |

|  | 云数据库 Tair（兼容南·API参考 | Redis）开发指 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | A52974D1-9D57- 4805-86CC- 92E6EDE8**** | 请求ID。 |
| MinorVersion | String | redis-5.0 0.5.0 _ | 实例当前的小版本。 |
| EnableUpgrad eMajorVersion | Boolean | true | 实例是否可升级大版本，返回值： true ：可升级。 false ：不可升级，通常已经是最新版本。 如需升级大版本，请调用 ModifyInstanceMajorVersion接口。 |
| IsLatestVersio n | Boolean | false | 实例的小版本是否为最新，返回值： true ：是。 false ：不是。 |
| EnableUpgrad eMinorVersion | Boolean | true | 实例是否可升级小版本，返回值： true ：可升级。 false ：已经是最新版本，不可升级。 如需升级小版本，请调用 ModifyInstanceMinorVersion接口。 |
| Engine | String | redis | 数据库类型，返回值：redis 或memcache 。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeEngineVersion &InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式云数据库 Tair（兼容Redis）开发指

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "MajorVersion":"5.0",
 "IsLatestVersion":false,
 "RequestId":"A52974D1-9D57-4805-86CC-92E6EDE8****",
 "MinorVersion":"redis-5.0_0.5.0",
 "EnableUpgradeMinorVersion":true,
 "Engine":"redis",
 "EnableUpgradeMajorVersion":true
}
```

#### DescribeInstanceAttribute

调用DescribeInstanceAttribute查询Redis实例的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | DescribeInstance Attribute | 系统规定参数，取值： DescribeInstance Attribute |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Instances | List | 无 | 由DBInstanceAttribute 组成的数组。 |

**DBInstanceAttribute 的参数构成**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceId | String | r-bp1d72gwl41z7f**** | 实例ID。 |
| InstanceName | String | apitest | 实例名称。 |
| Capacity | Long | 1024 | 申请到的存储实例容量； 单位：MB。 |
| InstanceClass | String | redis.logic.sharding.drr edissdb1g.1db.0rodb.4 proxy.default | 实例规格。 |

云数据库 Tair（兼容Redis）开发指

| Bandwidth | Long | 10 |  | 实例带宽限制；单位： Mbps。 |  |  |
|---|---|---|---|---|---|---|
| Connections | Long | 10000 |  | 实例连接数限制；单位： 个。 |  |  |
| ConnectionDomain | String | r- bp1d72gwl41z7f****.r edis.rds.aliyuncs.com |  | Redis 实例的连接域名 （仅支持内网访问）。 |  |  |
| Port | Int | 6379 |  | Redis连接端口。 |  |  |
| RegionId | String | cn-hangzhou |  | 申请的存储实例所在区域。参见Redis区域列表。 |  |  |
| ZoneId | String | cn-hangzhou-b |  | RegionId下的可用区编码。参见Redis区域列表。 |  |  |
| InstanceStatus | String | Normal |  | 实例状态： Normal：正常 Creating：创建中 Changing：修改中 Inactive：被禁用 |  |  |
| CreateTime | String | 2019-03- 06T10:42:03Z |  | 实例创建时间。采用 ISO8601 表示法，并使用 UTC 时间。格式为： YYYY-MM- DDThh:mm:ssZ 。 |  |  |
|  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  | DDThh:mm:ssZ |  |  |
| EndTime | String | 2019-04- 06T10:42:03Z |  | 预付费实例到期时间。采用ISO8601 表示法，并使用 UTC 时间。格式为： YYYY-MM- DDThh:mm:ssZ 。 |  |  |
| NetworkType | String | VPC |  | 网络类型：CLASSIC或 VPC。 |  |  |
| VpcId | String | vpc- bp1nme44gek34slfc** ** |  | VPC ID。 |  |  |
| VSwitchId | String | vsw- bp1e7clcw529l773d*** * |  | 虚拟交换机ID。 |  |  |
| MaintainStartTime | String | 18:00Z |  | 可运维开始时间。 |  |  |
| MaintainEndTime | String | 22:00Z |  | 可运维结束时间。 |  |  |
| SecurityIPList | String | 127.0.0.1 |  | IP白名单。 |  |  |
| AvailabilityValue | String | 100% |  | 当月的可用性指标。 |  |  |

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

云数据库 Tair（兼容Redis）开发指出于历史兼容性考虑，该函数会有些返回结构在文档中并未提及（如 Config、Region

**说明**

等），后续阿里云将逐步把这些字段删除，请您在调用 API 时不要依赖这些在文档中没有涉及的返回字段。

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeInstanceAttribute &InstanceId=r-bp1zxszhcgatnx****
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <Instances>
            <DBInstanceAttribute>
                  <Connections>10000</Connections>
                  <ResourceGroupId>rg-acfmyiu4ekp****</ResourceGroupId>
                  <Config>{"EvictionPolicy":"volatile-lru","hash-max-ziplist-entries":51
2,"zset-max-ziplist-entries":128,"list-max-ziplist-entries":512,"list-max-ziplist-value ":64,"zset-max-ziplist-value":64,"set-max-intset-entries":512,"hash-max-ziplist-value": 64}</Config>
                  <Port>6379</Port>
                  <HasRenewChangeOrder>false</HasRenewChangeOrder>
                  <ZoneType>singlezone</ZoneType>
                  <ConnectionDomain>r-
bp1wcw2rlw76acc5k****.redis.rds.aliyuncs.com</ConnectionDomain>
                  <MaintainEndTime>22:00Z</MaintainEndTime>
                  <Capacity>1024</Capacity>
                  <QPS>100000</QPS>
                  <PrivateIp>172.16.49.***</PrivateIp>
                  <SecurityIPList>127.0.0.1</SecurityIPList>
                  <InstanceStatus>Normal</InstanceStatus>
                  <NetworkType>VPC</NetworkType>
                  <Bandwidth>10</Bandwidth>
                  <PackageType>standard</PackageType>
                  <InstanceReleaseProtection>false</InstanceReleaseProtection>
                  <InstanceType>Redis</InstanceType>
                  <AvailabilityValue>100.0%</AvailabilityValue>
                  <Engine>Redis</Engine>
                  <MaintainStartTime>18:00Z</MaintainStartTime>
                  <Tags>
                        <Tag>
```

`<Value>`社区版`</Value>` `<Key>`类型`</Key>`

```xml
                        </Tag>
                  </Tags>
                  <ArchitectureType>standard</ArchitectureType>
                  <EngineVersion>5.0</EngineVersion>
                  <ZoneId>cn-hangzhou-f</ZoneId>
                  <InstanceId>r-bp1wcw2rlw76ac****</InstanceId>
                  <VSwitchId>vsw-bp1w9ouei2nm66qlz****</VSwitchId>
tTi 20200331T145622Z/C tTi
```

云数据库 Tair（兼容Redis）开发指

```xml
                  <CreateTime>2020-03-31T14:56:22Z</CreateTime>
<InstanceClass>redis.logic.sharding.drredissdb1g.1db.0rodb.4proxy.default</InstanceClass>
                  <AuditLogRetention>7</AuditLogRetention>
                  <IsRds>true</IsRds>
                  <ReplicationMode>master-slave</ReplicationMode>
                  <InstanceName>社区主从50</InstanceName>
                  <VpcId>vpc-bp1opxu1zkhn00gzv****</VpcId>
                  <ChargeType>PostPaid</ChargeType>
                  <VpcAuthMode>Open</VpcAuthMode>
                  <NodeType>double</NodeType>
                  <VpcCloudInstanceId>r-bp1wcw2rlw76ac****</VpcCloudInstanceId>
                  <RegionId>cn-hangzhou</RegionId>
            </DBInstanceAttribute>
      </Instances>
      <RequestId>D67A69DF-C1FC-4B01-B239-B17888CCFD2A</RequestId>
```

JSON格式：

```json
{
 "Instances": {
  "DBInstanceAttribute": [
   {
    "Connections": 10000,
    "ResourceGroupId": "rg-acfmyiu4ekp****",
    "Config": "{\"EvictionPolicy\":\"volatile-lru\",\"hash-max-ziplist-
entries\":512,\"zset-max-ziplist-entries\":128,\"list-max-ziplist-entries\":512,\"listmax-ziplist-value\":64,\"zset-max-ziplist-value\":64,\"set-max-intsetentries\":512,\"hash-max-ziplist-value\":64}",
    "Port": 6379,
    "HasRenewChangeOrder": "false",
                "ZoneType":"singlezone",
    "ConnectionDomain": "r-bp1wcw2rlw76acc5k****.redis.rds.aliyuncs.com",
    "MaintainEndTime": "22:00Z",
    "Capacity": 1024,
    "QPS": 100000,
    "PrivateIp": "172.16.49.***",
    "SecurityIPList": "127.0.0.1",
    "InstanceStatus": "Normal",
    "NetworkType": "VPC",
    "Bandwidth": 10,
    "PackageType": "standard",
    "InstanceReleaseProtection": false,
    "InstanceType": "Redis",
    "AvailabilityValue": "100.0%",
    "Engine": "Redis",
    "MaintainStartTime": "18:00Z",
    "Tags": {
     "Tag": [
      {
```

`"Value": "`社区版`",` `"Key": "`类型" 云数据库 Tair（兼容Redis）开发指

```
      }
```

]

```json
    },
    "ArchitectureType": "standard",
    "EngineVersion": "5.0",
    "ZoneId": "cn-hangzhou-f",
    "InstanceId": "r-bp1wcw2rlw76ac****",
    "VSwitchId": "vsw-bp1w9ouei2nm66qlz****",
    "CreateTime": "2020-03-31T14:56:22Z",
    "InstanceClass": "redis.logic.sharding.drredissdb1g.1db.0rodb.4proxy.default",
    "AuditLogRetention": "7",
    "IsRds": true,
    "ReplicationMode": "master-slave",
```

`"InstanceName": "`社区主从`50",`

```json
    "VpcId": "vpc-bp1opxu1zkhn00gzv****",
    "ChargeType": "PostPaid",
    "VpcAuthMode": "Open",
    "NodeType": "double",
    "VpcCloudInstanceId": "r-bp1wcw2rlw76ac****",
    "RegionId": "cn-hangzhou"
   }
```

]

```json
 },
 "RequestId": "D67A69DF-C1FC-4B01-B239-B17888CCFD2A"
}
```

#### DescribeInstances

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | DescribeIns tances | 操作接口名，取值：DescribeInstances。 |
| InstanceIds | String | 否 | r- n8r8c5119d 2e**** | 实例 ID（全局唯一）。 说明如需传入多个实例ID，使用英文逗号（,）分隔。 不传入本参数即表示查询该用户名下所有实例。 |

云数据库 Tair（兼容Redis）开发指

| InstanceSta tus | String | 否 | Normal | 按状态过滤所需返回的实例： Normal：正常 Creating：创建中 Changing：修改中 Inactive：被禁用 |
|---|---|---|---|---|
| RegionId | String | 是 | cn- hangzhou | 调用 DescribeRegions 查询 RegionId。 |
| InstanceTyp e | String | 否 | Redis | 引擎类型的过滤。 Memcache：Memcache 类型的实例 Redis：Redis 类型的实例 |
| PageNumbe r | Integer | 否 | 1 | 实例状态列表的页码，起始值为1，默认值为 1。 |
| PageSize | Integer | 否 | 10 | 分页查询时设置的每页行数，最大值50行， 默认值为10。 |
| NetworkTyp e | String | 否 | VPC | 按网络类型过滤： CLASSIC：经典网络类型 VPC：VPC 网络类型 |

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |
| Instances | List | 无 | 由 Instance 组成的数组，详见Instance参数构成。 |
| TotalCount | Integer | 1 | 实例总个数 |
| PageNumber | Integer | 1 | 实例列表的页码 |
| PageSize | Integer | 10 | 输入时设置的每页行数 |

**Instance参数构成**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceId | String | r- n8r8c5119d2e **** | 实例 ID （全局唯一） |
| InstanceName | String | testdb | 实例名称 |
| Capacity | Long | 512 | 申请到的存储实例容量； 单位：MB。 |
| InstanceClass | String | redis.master. mid.default | 实例规格信息 |

云数据库 Tair（兼容Redis）开发指

| Bandwidth | Long | 128 | 实例带宽限制；单位：Mbps。 |
|---|---|---|---|
| Connections | Long | 300 | 实例连接数限制；单位：个。 |
| ConnectionDo main | String | de5d88e34d0 0****.m.cnhzal icm10pub001. r- kvstore.examp le.com | 实例连接域名（仅支持内网访问。） |
| Port | Int | 11211 | 连接端口 |
| UserName | String | testuser | 连接用户名 |
| RegionId | String | cn-qingdao | 申请的存储实例所在区域 |
| ZoneId | String | cn-qingdao-b | RegionId 下的可用区编码 |
| InstanceStatus | String | Normal | 实例状态： Normal：正常 Creating：创建中 Changing：修改中 Inactive：被禁用 Transforming：转换中 BackupRecovering：备份恢复中 MinorVersionUpgrading：实例小版本升级中 |
| ChargeType | String | PostPaid | 付费类型：PrePaid 或 PostPaid |
| CreateTime | String | 2019-03- 06T10:42:03Z | 实例创建时间。采用ISO8601 表示法，并使用 UTC 时间。格式为： YYYY-MM-DDThh:mm:ssZ 。 |
| EndTime | String | 2019-04- 06T10:42:03Z | 预付费实例到期时间。采用ISO8601 表示法，并使用 UTC 时间。格式为： YYYY-MM- DDThh:mm:ssZ 。 |
| NetworkType | String | VPC | 网络类型：CLASSIC 或 VPC |
| VpcId | String | vpc- bp1nme44gek 34slfc**** | VPC 的 ID |
| VSwitchId | String | vsw- bp1e7clcw529l 773d**** | 虚拟交换机 ID |
| PrivateIpAddr | String | 172.16.**.*** | 私有 IP 地址 |

| 42:03Z | DDThh:mm:ssZ |
|---|---|

出于历史兼容性考虑，该函数会有些返回结构在文档中并未提及（如 Config），后续阿里

**说明**

云将逐步把这些字段删除，请您在调用 API 时不要依赖这些在文档中没有涉及的返回字段。

**请求示例**

云数据库 Tair（兼容Redis）开发指

```
https://r-kvstore.example.com
```

?<公共请求参数>

```
&PageNumber=1 &PageSize=10 &InstanceId=r-n8r8c5119d2e****
```

**返回示例**

XML格式：

```xml
    <Instances>
        <Instance>
            <Bandwidth>128</Bandwidth>
            <Capacity>512</Capacity>
            <ConnectionDomain>de5d88e34d00****.m.cnhzalicm10pub001.r-
kvstore.example.com</ConnectionDomain>
            <Connections>300</Connections>
            <ZoneId>cn-qingdao-b</ZoneId>
            <InstanceId>r-n8r8c5119d2e****</InstanceId>
            <InstanceName>testdb</InstanceName>
            <InstanceStatus>Available</InstanceStatus>
            <InstanceClass>redis.master.mid.default</InstanceClass>
            <Port>11211</Port>
            <RegionId>cn-qingdao</RegionId>
            <UserName>testuser</UserName>
            <NetworkType>CLASSSIC</NetworkType>
            <ChargeType> PostPaid</ChargeType>
        </Instance>
    </Instances>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TotalCount>1</TotalCount>
    <RequestId>969D0A1D-C91A-4837-9F70-49785DF9BDCE</RequestId>
```

JSON格式： 云数据库 Tair（兼容Redis）开发指

```json
{
    "Instances" : {
        "Instance" : [{
                "Bandwidth" : 128,
                "Capacity" : 512,
                "ConnectionDomain" : "de5d88e34d00****.m.cnhzalicm10pub001.r-kvstore.exa
mple.com",
                "Connections" : 300,
                "ZoneId" : "cn-qingdao-b",
                "InstanceId" : "r-n8r8c5119d2e****",
                "InstanceName" : "testdb",
                "InstanceStatus" : "Available",
                 "InstanceClass" : "redis.master.mid.default",
                "Port" : 11211,
                "RegionId" : "cn-qingdao",
                "UserName" : "testuser"
                "NetworkType":"CLASSSIC"
"ChargeType":" PostPaid"
            }
```

]

```json
    },
    "PageNumber" : 1,
    "PageSize" : 10,
    "TotalCount" : 1,
    "RequestId" : "969D0A1D-C91A-4837-9F70-49785DF9BDCE"
}
```

#### DescribeRegions

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | DescribeRegions | 系统规定参数，取值： DescribeRegions 。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

云数据库 Tair（兼容Redis）开发指

| RegionIds | List | 无 | RegionIds 为一个 List， 里面每个元素由两部分组成：RegionId、 ZoneIds，其中的 ZoneIds 也是一个 String，多个 ZoneId 用“,”分隔。 |
|---|---|---|---|

**请求示例**

```
https://r-kvstore.aliyuncs.com?Action=DescribeRegions
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RegionIds>
            <KVStoreRegion>
              <RegionId>cn-hangzhou</RegionId>
              <ZoneIdList>
                    <ZoneId>cn-hangzhou-h</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ10(h,i)</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ9(g,h)</ZoneId>
                    <ZoneId>cn-hangzhou-b</ZoneId>
                    <ZoneId>cn-hangzhou-d</ZoneId>
                    <ZoneId>cn-hangzhou-e</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ6(b,f)</ZoneId>
                    <ZoneId>cn-hangzhou-f</ZoneId>
                    <ZoneId>cn-hangzhou-g</ZoneId>
              </ZoneIdList>
              <RegionEndpoint>r-kvstore.aliyuncs.com</RegionEndpoint>
              <ZoneIds>cn-hangzhou-h,cn-hangzhou-MAZ10(h,i),cn-hangzhou-MAZ9(g,h),cn-
hangzhou-b,cn-hangzhou-d,cn-hangzhou-e,cn-hangzhou-MAZ6(b,f),cn-hangzhou-f,cn-hangzhoug</ZoneIds>
```

`<LocalName>`华东1（杭州）`</LocalName>`

```xml
            </KVStoreRegion>
      </RegionIds>
      <RequestId>AD425AD3-CC7B-4EE2-A5CB-2F61BA73****</RequestId>
```

JSON格式： 云数据库 Tair（兼容Redis）开发指

```json
{
 "RegionIds": {
  "KVStoreRegion": [{
    "RegionId": "cn-hangzhou",
    "ZoneIdList": {
     "ZoneId": [
      "cn-hangzhou-h",
      "cn-hangzhou-MAZ10(h,i)",
      "cn-hangzhou-MAZ9(g,h)",
      "cn-hangzhou-b",
      "cn-hangzhou-d",
      "cn-hangzhou-e",
      "cn-hangzhou-MAZ6(b,f)",
      "cn-hangzhou-f",
      "cn-hangzhou-g"
```

]

```json
    },
    "RegionEndpoint": "r-kvstore.aliyuncs.com",
    "ZoneIds": "cn-hangzhou-h,cn-hangzhou-MAZ10(h,i),cn-hangzhou-MAZ9(g,h),cn-hangzhou-
b,cn-hangzhou-d,cn-hangzhou-e,cn-hangzhou-MAZ6(b,f),cn-hangzhou-f,cn-hangzhou-g",
```

`"LocalName": "`华东1（杭州）"

```
   }
```

]

```json
 },
 "RequestId": "AD425AD3-CC7B-4EE2-A5CB-2F61BA73****"
}
```

#### DescribeSecurityIps

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | DescribeSecurityI ps | 系统规定参数，取值： DescribeSecurityI ps。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |
| WhitelistNetType | String | 否 | vpc | 白名单的网络类型。 |

云数据库 Tair（兼容Redis）开发指

| SecurityIpType | String | 否 | IPv4 | IP类型。 |
|---|---|---|---|---|
| CreateTime | String | 否 | 2023-10- 27T08:30:00Z | 创建时间。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |
| SecurityIpGroups | List | 无 | 实例的IP白名单分组列表。 |

**SecurityIpGroups 的参数**

| 名称 | 类型 | 示例值 |  |  | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| SecurityIpGroupName | String | default |  |  | IP 白名单分组的名字。 |  |  |  |  |
| SecurityIpList | String | 100.100.202.***/24,10 .10.10.*** |  |  | IP 白名单分组下的 IP 列表，最多1000个。IP 之间以逗号隔开，格式如下： 0.0.0.0/0,10.23.12 .24（IP） ，或者 10.23.12.24/24 （CI DR 模式，无类域间路由，/24表示了地址中前缀的长度，范围[1,32]）。 |  |  |  |  |
|  |  |  |  |  |  | 0.0.0.0/0,10.23.12 |  |  |  |
|  |  |  | 10.*** |  | .24（IP） |  |  |  |  |
|  |  |  |  |  |  |  | ，或者 |  |  |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeSecurityIps &InstanceId=r-bp1zxszhcgatnx****
```

`&<`公共请求参数>

**返回示例**

XML格式： 云数据库 Tair（兼容Redis）开发指

```xml
      <SecurityIpGroups>
            <SecurityIpGroup>
                  <SecurityIpList>127.0.0.1</SecurityIpList>
                  <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
                  <SecurityIpGroupName>default</SecurityIpGroupName>
            </SecurityIpGroup>
            <SecurityIpGroup>
                  <SecurityIpList>100.100.202.***/24,10.10.10.***</SecurityIpList>
                  <SecurityIpGroupAttribute>hidden</SecurityIpGroupAttribute>
                  <SecurityIpGroupName>rds_replica_group</SecurityIpGroupName>
            </SecurityIpGroup>
      </SecurityIpGroups>
      <RequestId>EFC9161F-15E3-4A6E-8A99-C09916D1****</RequestId>
```

JSON格式：

```json
{
    "SecurityIpGroups": {
        "SecurityIpGroup": [
            {
                "SecurityIpList": "127.0.0.1",
                "SecurityIpGroupAttribute": "",
                "SecurityIpGroupName": "default"
            },
            {
                "SecurityIpList": "100.100.202.***/24,10.10.10.***",
                "SecurityIpGroupAttribute": "hidden",
                "SecurityIpGroupName": "rds_replica_group"
            }
```

]

```json
    },
    "RequestId": "EFC9161F-15E3-4A6E-8A99-C09916D1****"
}
```

#### DescribeCpuTypes

查询云数据库Redis实例支持的CPU类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKey Id | Strin g | Query | 否 | LTAI4G28PhwnizaSC**** **** | 访问密钥ID。 |

云数据库 Tair（兼容Redis）开发指

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 否 | DescribeCpuTypes | 系统规定参数。取值： DescribeCpuTypes |
| SecurityT oken | Strin g | Query | 否 | ******** | STS 安全令牌。 |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| Resource OwnerAcc ount | Strin g | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| Resource OwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| OwnerAcc ount | Strin g | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| RegionId | Strin g | Domain | 否 | cn-huhehaote | 地域 ID，可调用 DescribeRegions 查询， 使用此参数指定要创建实例的地域。 |
| ZoneId | Strin g | Query | 是 | cn-hongkong-b | 可用区ID，您可以调用 DescribeZones查询。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| CpuTypes | Array | SPARC | 由Sun公司开发的RISC架构，用于其服务器和工作站产品线 |
| -CpuType | String | Itanium | CPU属性 |
| RequestId | String | 5DEA3CC9-F81D- 4387-8E97- CEA40F09**** | 请求Id。 |

**示例**

请求示例

```
&ZoneId=cn-hongkong-b
```

&公共请求参数云数据库 Tair（兼容Redis）开发指正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"5DEA3CC9-F81D-4387-8E97-CEA40F09****",
 "CpuTypes":[
  {
   "CpuType":"Itanium"
  }
```

]

```
}
```

#### DescribeZones

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Domain | 否 | cn-huhehaote | 地域ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1D42F072-72FE- 4DC4-BB8E- 64B1D298**** | 请求ID。 |
| Zones | Array |  | 可用区的集合。 |
| -RegionId | String | cn-huhehaote | 该地域的ID。 |
| -ZoneId | String | cn-huhehaote-b | 该地域下的某可用区的ID。 |
| -ZoneName | String | 呼和浩特可用区B | 该地域下的某可用区的名称。 |
| - SwitchNetwork | Boolean | true | 是否支持将Redis实例从经典网络切换为专有网络，返回值： true ：支持。 false ：不支持。 |

云数据库 Tair（兼容Redis）开发指

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -IsRds | Boolean | true | 是否属于RDS管控，Redis实例中该参数的返回值固定为true 。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1D42F072-72FE-4DC4-BB8E-64B1D298****",
 "Zones":{
```

`"ZoneName":"`呼和浩特可用区`B",`

```json
  "ZoneId":"cn-huhehaote-b",
  "SwitchNetwork":true,
  "RegionId":"cn-huhehaote",
  "IsRds":true
 }
}
```

#### FlushInstance

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | FlushInstance | 系统规定参数，取值： FlushInstance。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例 ID，全局唯一。 |

**返回参数**

表 2. 返回参数云数据库 Tair（兼容Redis）开发指

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=FlushInstance &InstanceId=r-bp1zxszhcgatnx****
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76</RequestId>
```

JSON格式：

```json
{
  "RequestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E7"
}
```

#### ModifyInstanceAttribute

修改实例的属性，包括名称或密码。

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数 > | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | ModifyInstanc eAttribute | 操作接口名，取值： ModifyInstanceAttribute。 |
| InstanceId | String | 是 | r- bp1zxszhcgat nx**** | 实例 ID，全局唯一。 |
| InstanceNam e | String | 否 | TestInstance | 修改后的实例名称。名称为2-128个字符，以大小写英文字母或中文开头，不支持字符@/:=”<>{[]}和空格。 |

云数据库 Tair（兼容Redis）开发指

| NewPassword | String | 否 | Qa12345678 | 实例密码。字符类型：8～30个字符，需同时包含大写字母、小写字母和数字。 说明对于特殊字符 ! <>()[]{},`~.- @#$%^&* _ 暂不支持。 |
|---|---|---|---|---|

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.example.com &InstanceId=r-bp1zxszhcgatnx**** &NewPassword=Qa12345678 &InstanceName=TestInstance
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
    <RequestId>E3B35BEA-9EB0-402C-88CF-C46CCCC1EE59</RequestId>
```

JSON格式：

```json
{ "RequestId" : "E3B35BEA-9EB0-402C-88CF-C46CCCC1EE59" }
```

#### ModifyInstanceMaintainTime

调用ModifyInstanceMaintainTime修改Redis实例的可维护时间段，阿里云将在您设定的可维护时间段内对Redis实例进行例行维护。

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |

云数据库 Tair（兼容Redis）开发指

| Action | String | 是 | ModifyInstanceM aintainTime | 系统规定参数，取值： ModifyInstanceM aintainTime。 |
|---|---|---|---|---|
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |
| MaintainStartTim e | String | 是 | 03:00Z | 可运维时间开始时间。 |
| MaintainEndTime | String | 是 | 04:00Z | 可运维时间结束时间。 |

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceMaintainTime &InstanceId=r-bp1zxszhcgatnx**** &MaintainStartTime=17:00Z &MaintainEndTime=18:00Z
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76</RequestId>
```

JSON格式：

```json
{
 "RequestId": "8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76"
}
```

#### ModifyInstanceNetExpireTime

若Redis实例之前执行过由经典网络向VPC网络切换，并保留了经典网络连接地址，则可调用 ModifyInstanceNetExpireTime延长经典网络连接地址的保留时间。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 Tair（兼容Redis）开发指

| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
|---|---|---|---|---|
| Action | String | 是 | ModifyInstanceN etExpireTime | 系统规定参数，取值： ModifyInstanceN etExpireTime。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例D。 |
| ConnectionString | String | 是 | r- bp1zxszhcgatnx* ***.redis.rds.aliyu ncs.com | 经典网络的访问域名。 |
| ClassicExpiredDa ys | String | 是 | 14 | 选择保留时长。取值：14、30、60或 120。 |

**返回参数**

表 1. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceNetExpireTime &ClassicExpiredDays=14 &ConnectionString=r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com &InstanceId=r-bp1zxszhcgatnx****
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>9C4AF387-1EA3-4C84-8013-3F6B973EDDF5</RequestId>
```

JSON格式：

```json
{
    "RequestId": "9C4AF387-1EA3-4C84-8013-3F6B973EDDF5",
}
```

#### ModifySecurityIps

**请求参数**

云数据库 Tair（兼容Redis）开发指

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数公共参数。 |
| Action | String | 是 | ModifySecurityIps | 系统规定参数，取值： ModifySecurityIps 。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID（全局唯一）。 |
| SecurityIps | String | 是 | 100.64.***.0/24,1 0.101.11.*** | 待修改的IP白名单列表。 |
| SecurityIpGroupN ame | String | 是 | default | 白名单分组。 |
| securityIPType | String | 否 | IPv4 | IP类型，默认 IPv4，取值范围： IPv4 IPv6 |

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=ModifySecurityIps &InstanceId=r-bp1zxszhcgatnx**** &SecurityIps=100.64.***.0/24,10.101.11.***
```

`&<`公共请求参数>

**返回示例**

XML格式： 云数据库 Tair（兼容Redis）开发指

```xml
      <RequestId>AAAF99B1-69ED-4E80-8CD5-272C09E4****</RequestId>
```

JSON格式：

```json
{
    "RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E4****"
}
```

#### SwitchNetwork

调用SwitchNetwork切换Redis实例的专有网络VPC或交换机，如果Redis实例为经典网络，则会将其切换为专有网络。

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | SwitchNetwork | 系统规定参数，取值： SwitchNetwork。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |
| TargetNetworkTy pe | String | 是 | VPC | 切换到的网络类型。 VPC：专有网络类型的实例 Classic：经典网络类型的实例当前只支持经典网络切换到 VPC 类型， 该类型需要填写 VPC。 |
| VpcId | String | 否 | vpc- bp1nme44gek34 slfc**** | 切换到的 VPC 的虚拟网络ID。 |
| VSwitchId | String | 否 | vsw- bp1e7clcw529l77 3d**** | 切换到的 VPC 的虚拟交换机 ID。如果指定了 VPC ID，则该参数也必须指定。 |
| RetainClassic | String | 否 | True | 是否保留经典网络 IP。默认是False。 True：保留 False：不保留 |

云数据库 Tair（兼容Redis）开发指

| ClassicExpiredDa ys | String | 否 | 30 | 保留经典网络 IP 的时间。单位：天。 可选值：14、30、 60、120。若选择保留经典网络地址，则该参数必选。 |
|---|---|---|---|---|

**返回参数**

表 1. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com?Action=SwitchNetwork &InstanceId=r-bp1zxszhcgatnx**** &TargetNetworkType=VPC &VpcId=vpc-bp1nme44gek34slfc**** &VSwitchId=vsw-bp1e7clcw529l773d**** &RetainClassic=True &ClassicExpiredDays=30
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <TaskId>578678678</TaskId>
      <requestId>F0997EE8-F4C2-4503-9168-85177ED78C70</requestId>
```

JSON格式：

```json
{
    "TaskId":"578678678",
    "requestId": "F0997EE8-F4C2-4503-9168-85177ED78C70"
}
```

#### SwitchInstanceHA

执行主备切换（即切换节点角色），可应用于容灾演练、多可用区场景下的应用就近连接。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 云数据库 Tair（兼容Redis）开发指

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | 否 | SwitchInstanceHA | 系统规定参数。取值： SwitchInstanceHA。 |
| InstanceId | Strin g | Quer y | 是 | r-bp1zxszhcgatnx**** | 实例ID，可调用 DescribeInstances获取。 |
| NodeId | Strin g | Quer y | 否 | 56****19,56****20 | 数据分片节点ID，您可以调用 DescribeRoleZoneInfo获取 CustinsId参数，多个数据分片节点ID之间使用英文逗号 （,）分隔，如需指定所有节点请输入 all 。 当实例为集群或读写分离架构时，本参数才可用，且必填。 |
| SwitchTyp e | Strin g | Quer y | 是 | AvailablePriority | 您需要根据业务场景对数据、 服务等方面的需求进行衡量， 然后选取切换模式。 枚举值: AvailablePriority(可用性优先，不考虑主备延迟， 立即执行主备切换，可能会丢失少量数据。) ReliabilityPriority(可靠性优先，确保主备同步无延迟时才执行主备切换，不会丢失数据。该模式在写入量较大且持续存在同步延迟的场景下，可能会造成主备切换失败。) ImmediatelyPriority(立即切换，设置改参数 SwitchMode只能是0，实例会跳过其他检测步骤立即触发HA切换，保障实例 RTO，但无法保证实例数据一致性。) |

云数据库 Tair（兼容Redis）开发指

| SwitchMod e | Integ er | Quer y | 否 | 0 | 执行时间，取值： 0：立即执行，默认值。 1：在可维护时间段执行。 您可以调用 ModifyInstanceMaint ainTime修改实例的可维护时间段。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 5D622714-AEDD- 4609-9167- F5DDD3D1**** | 请求ID。 |

**示例**

请求示例

```
&InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId": "5D622714-AEDD-4609-9167-F5DDD3D1****"
}
```

`XML` 格式

```xml
<RequestId>5D622714-AEDD-4609-9167-F5DDD3D1****</RequestId>
```

### 数据加密

#### DescribeEncryptionKey

调用DescribeEncryptionKey接口查询Redis实例的透明数据加密TDE自定义密钥的详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

云数据库 Tair（兼容Redis）开发指

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID，可调用 DescribeInstances获取。 |
| Encryptio nKey | Strin g | Query | 否 | ad463061-992d-4195- 8a94-ed63******** | 实例的自定义密钥ID，可调用 DescribeEncryptionKeyLi st接口查询。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Origin | String | Aliyun KMS _ | 密钥材料的来源，返回值Aliyun KMS ，即 _ 表示阿里云密钥管理服务KMS。 |
| Description | String | testkey | 密钥的描述信息，默认为空。 |
| RequestId | String | 9A931CE5-C926- 5E09-B0EC- 6299C4A6**** | 请求ID。 |
| EncryptionKey Status | String | Enabled | 实例的密钥状态，返回值： Enabled ：可用。 Disabled ：不可用。 |
| MaterialExpire Time | String | 2021-09- 24T18:22:03Z | 密钥的过期时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 本参数返回内容为空时，表示密钥不会过期。 |
| KeyUsage | String | ENCRYPT/DECRYPT | 实例密钥的用途，返回值 ENCRYPT/DECRYPT 即表示加密和解密。 |
| EncryptionKey | String | ad463061-992d- 4195-8a94- ed63******** | 实例的密钥ID。 |
| Creator | String | 17649847******** | 密钥创建者的云账号ID。 |
| DeleteDate | String | 2021-09- 24T18:22:03Z | 实例密钥的预计删除时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 本参数返回内容为空时，表示密钥不会被自动删除。 |

云数据库 Tair（兼容Redis）开发指

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeEncryptionKey &InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "Origin":"Aliyun_KMS",
 "Description":"testkey",
 "RequestId":"9A931CE5-C926-5E09-B0EC-6299C4A6****",
 "EncryptionKeyStatus":"Enabled",
 "MaterialExpireTime":"2021-09-24T18:22:03Z",
 "KeyUsage":"ENCRYPT/DECRYPT",
 "EncryptionKey":"ad463061-992d-4195-8a94-ed63********",
 "Creator":"17649847********",
 "DeleteDate":"2021-09-24T18:22:03Z"
}
```

#### DescribeInstanceTDEStatus

调用DescribeInstanceTDEStatus接口查询Redis实例是否开启了TDE加密功能。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID，可调用 DescribeInstances获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TDEStatus | String | Enabled | TDE加密功能是否开启，返回值： Enabled ：开启。 Disabled ：关闭。 |
| RequestId | String | 5D622714-AEDD- 4609-9167- F5DDD3D1**** | 请求ID。 |

云数据库 Tair（兼容Redis）开发指

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeInstanceTDEStatus &InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TDEStatus":"Enabled",
 "RequestId":"5D622714-AEDD-4609-9167-F5DDD3D1****"
}
```

#### CheckCloudResourceAuthorized

调用CheckCloudResourceAuthorized接口查询Redis实例是否已被授权使用KMS密钥服务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID，可调用DescribeInstances获取。 |

云数据库 Tair（兼容Redis）开发指

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RoleArn | Strin g | Query | 否 | acs:ram::123456789012 ****:role/AliyunRdsInsta nceEncryptionDefaultRol e | 指定待授权角色的全局资源描述符ARN（Alibaba Cloud Resource Name） 信息，完成该角色的授权后即可使用相关密钥管理服务，格式： acs:ram::$accoun tID:role/$roleName 。 $accountID ：云账号ID。您可以登录阿里云控制台，将鼠标悬停在右上角头像的位置，单击安全设置进行查看。 $roleName ： RAM角色名称，取值固定为：AliyunRdsIn stanceEncrypti onDefaultRol e 。 |

|  |  | acs:ram::$accoun |
|---|---|---|
|  | tID:role/$roleName |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| AuthorizationS tate | Integer | 1 | 授权状态，返回值： 0 ：未授权。 1 ：已授权。 2 ：未开通密钥管理服务，具体操作，请参见开通密钥管理服务。 |
| RequestId | String | A501A191-BD70- 5E50-98A9- C2A486A82**** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CheckCloudResourceAuthorized &InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式云数据库 Tair（兼容Redis）开发指

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "AuthorizationState":1,
 "RequestId":"A501A191-BD70-5E50-98A9-C2A486A82****"
}
```

### 账号管理

#### DescribeUserInfo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 3A40BE4E-1890- 4972-889C- FEFA376XXX | 请求Id。 |
| IsAuthenticatio n | Boolean | true | 身份认证。 |
| IsFinance | Boolean | false | 金融客户。 |
| BalanceAmoun t | Long | 0 | 余额。 |
| AlreadyHasRe sourceNum | Struct |  | 已有资源数。 |
| -EcsBought | Long | 22 | 从ECS购买。 |
| -KVSBought | Long | 29 | 从KVS购买。 |

**示例**

请求示例正常返回示例 `JSON` 格式云数据库 Tair（兼容Redis）开发指

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "BalanceAmount":0,
 "RequestId":"3A40BE4E-1890-4972-889C-FEFA376XXX",
 "IsAuthentication":true,
 "IsFinance":false,
 "AlreadyHasResourceNum":{
  "EcsBought":22,
  "KVSBought":29
 }
}
```

#### CreateAccount

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID。 |
| AccountN ame | Strin g | Query | 是 | demoaccount | 账号名，需满足以下条件： 以英文字母开头，由小写英文字母、数字或下划线 （ ）组成。 _ 长度不超过100个字符。 不能为Redis账号名保留字。 |
| AccountPr ivilege | Strin g | Query | 否 | RoleReadOnly | 账号权限，取值： RoleReadOnly ：只读权限。 RoleReadWrite ： 读写权限，默认值。 |
| AccountPa ssword | Strin g | Query | 是 | uWonno21**** | 账号的密码。长度为8~32 位，需包含大写字母、小写字母、特殊字符和数字中的至少三种，允许的特殊字符包括 !@#$%^&*() +- _ = 。 |

|  | = |
|---|---|

云数据库 Tair（兼容Redis）开发指

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccountD escription | Strin g | Query | 否 | testaccount | 账号描述。 需以中文、英文字母开头，不能以 http: // 或 https: // 开头。 可以包含中文、英文字母、数字、下划线（ ） _ 和短划线（-）。 长度为2~256个字符。 |
| AccountTy pe | Strin g | Query | 否 | Normal | 账号类型，取值固定为Normal （普通账号）。 |

|  | http: |
|---|---|
| https: |  |

|  |  | // |
|---|---|---|
|  |  | // |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | ABAF95F6-35C1- 4177-AF3A- 70969EBD**** | 请求ID。 |
| InstanceId | String | r- bp1zxszhcgatnx*** * | 实例ID。 |
| AcountName | String | demoaccount | 账号名称。 |

**示例**

请求示例

```
&InstanceId=r-bp1zxszhcgatnx**** &AccountName=demoaccount &AccountPassword=uWonno21****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"ABAF95F6-35C1-4177-AF3A-70969EBD****",
 "InstanceId":"r-bp1zxszhcgatnx****",
 "AcountName":"demoaccount"
}
```

云数据库 Tair（兼容Redis）开发指

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAccountNam e.Duplicate | InvalidAccountName.Duplicate | Specified AccountName already exists in this instance. |
| 400 | InvalidAccountNam e.Format | InvalidAccountName.Format | Specified AccountName is not valid. |
| 400 | IncorrectEngineVer sion | InvalidEngineVersion.Format | Current EngineVersion does not support operations. |
| 400 | InvalidAccountDesc ription.Format | InvalidAccountDescription.For mat | Specified AccountDescription is not valid. |
| 400 | InvalidAccountPass word.Format | InvalidAccountPassword.Forma t | Specified AccountPassword is not valid. |
| 400 | IncorrectDBInstanc eAccountMode | InvalidDBInstanceAccountMod e.Format | Current DB instance AccountMode does not support this operation. |
| 400 | InvalidAccountNam e.Forbid | InvalidAccountName.Forbid | Specified AccountName is a keyword. |
| 403 | AccountLimitExcee ded | AccountLimitExceeded | Exceeding the allowed amount of account. |

### 网络安全

#### DescribeInstanceSSL

调用DescribeInstanceSSL接口查询实例是否开启了TLS（SSL）加密认证。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SSLExpiredTim e | String | 2020-08- 05T09:05:53Z | CA证书的过期时间。 |

云数据库 Tair（兼容Redis）开发指

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 02260F96-913E- 4655-9BA5- A3651CAF**** | 请求ID。 |
| SSLEnabled | String | Enable | TLS（SSL）加密功能的状态： Enable ：已开启。 Disable ：未开启。 |
| InstanceId | String | r- bp1zxszhcgatnx*** * | 实例ID。 |
| CertCommonN ame | String | r- bp1zxszhcgatnx*** *.redis.rds.aliyuncs .com | CA证书的公共名，默认值为实例的内网连接地址。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeInstanceSSL &InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "SSLExpiredTime":"2020-08-05T09:05:53Z",
 "RequestId":"02260F96-913E-4655-9BA5-A3651CAF****",
 "SSLEnabled":"Enable",
 "InstanceId":"r-bp1zxszhcgatnx****",
 "CertCommonName":"r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com"
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectCharacter Type | IncorrectCharacterType | Current DB instance CharacterType does not support this operation. |
| 403 | IncorrectEngineVer sion | IncorrectEngineVersion | Current engine version does not support operations. |

云数据库 Tair（兼容Redis）开发指

### 连接管理

#### DescribeIntranetAttribute

调用DescribeIntranetAttribute接口查询Redis实例当前的内网带宽。如果调整过带宽，您还可以查询到带宽的过期时间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| IntranetBandw idth | Integer | 102 | 实例当前的内网带宽，单位MB/s。 |
| RequestId | String | 25D42CC3-FBA1- 4AEC-BCE2- B8DD3137**** | 请求ID。 |
| ExpireTime | String | 0 | 临时带宽的过期时间，格式为yyyy-MM- ddTHH:mm:ssZ。 如果实例未执行过临时调整带宽或临时带宽已过期，本参数返回0 。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeIntranetAttribute &InstanceId=r-bp1zxszhcgatnx****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "IntranetBandwidth":102,
 "RequestId":"25D42CC3-FBA1-4AEC-BCE2-B8DD3137****",
 "ExpireTime":"0"
}
```

云数据库 Tair（兼容Redis）开发指

#### ModifyInstanceVpcAuthMode

调用ModifyInstanceVpcAuthMode接口开启或关闭专有网络免密访问，可在保障安全性的前提下，实现更便捷的数据库连接。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp1zxszhcgatnx**** | 实例ID。 |
| VpcAuthM ode | Strin g | Query | 是 | Close | 专有网络下的认证模式，取值： Open ：通过密码认证。 Close ：关闭密码认证，即开启免密访问。 默认值为Open 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | ABAF95F6-35C1- 4177-AF3A- 70969EBD**** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyInstanceVpcAuthMode &InstanceId=r-bp1zxszhcgatnx**** &VpcAuthMode=Close
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"ABAF95F6-35C1-4177-AF3A-70969EBD****"
}
```

#### AllocateInstancePublicConnection

云数据库 Tair（兼容Redis）开发指调用AllocateInstancePublicConnection接口为Redis实例申请公网连接地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | 是 | r-bp1zxszhcgatnx**** |  |  | 实例ID。 |  |  |  |
| Connectio nStringPref ix | Strin g | Quer y | 是 | r-bp1zxszhcgatnx**** |  |  | 公网连接地址的前缀，需由小写英文字母与数字组成，以小写字母开头，长度为8~40个字符。 公网连接地址格式为： <前缀 |  |  |  |
|  |  |  |  |  |  |  |  |  | <前缀 |  |
|  |  |  |  |  |  |  |  | >.redis.rds.aliyun |  |  |
|  |  |  |  |  |  |  |  | cs.com |  |  |
| Port | Strin g | Quer y | 是 | 6379 |  |  | Redis服务端口，取值范围：1024~65535。 |  |  |  |
| IPVersionS electedTyp e | Strin g | Quer y | 否 | IPv4 |  |  | IP类型。默认IPv4，取值范围： IPv4 IPv6 |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 20C8341E-B5AD- 4B24-BD82- D73241522ABF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AllocateInstancePublicConnection &InstanceId=r-bp1zxszhcgatnx**** &ConnectionStringPrefix=r-bp1zxszhcgatnx**** &Port=6379
```

&公共请求参数正常返回示例云数据库 Tair（兼容Redis）开发指 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"20C8341E-B5AD-4B24-BD82-D73241522ABF"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingInstanceId | MissingInstanceId | InstanceId is mandatory for this action. |
| 400 | MissingConnection String | MissingConnectionString | ConnectionStringPrefix is mandatory for this action. |
| 400 | MissingPort | MissingPort | Port is mandatory for this action. |
| 400 | NetTypeExists | NetTypeExists | Specified net type already existed. |
| 400 | InvalidConnectionS tring.Format | InvalidConnectionString.Forma t | Specified connection string is not valid. |

### 备份恢复

#### CreateBackup

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | CreateBackup | 系统规定参数，取值： CreateBackup。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |

**返回参数**

云数据库 Tair（兼容Redis）开发指

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=CreateBackup &InstanceId=r-bp1zxszhcgatnx****
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>2FF6158E-3394-4A90-B634-79C49184****</RequestId>
      <BackupJobID>1162****</BackupJobID>
```

JSON格式：

```json
{
    "RequestId": "2FF6158E-3394-4A90-B634-79C49184****",
    "BackupJobID": "1162****"
}
```

#### ModifyBackupPolicy

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 |  | 描述 |  |  |
|---|---|---|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 |  | 参见公共请求参数。 |  |  |
| Action | String | 是 | ModifyBackupPoli cy |  | 系统规定参数，取值： ModifyBackupPoli cy。 |  |  |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** |  | 实例ID。 |  |  |
| PreferredBackup Time | String | 是 | 00:00Z-04:00Z |  | 备份时间，格式： HH:mmZ- HH:mm Z 。 |  |  |
|  |  |  |  |  |  | HH:mmZ- |  |
|  |  |  |  |  | HH:mm Z |  |  |

云数据库 Tair（兼容Redis）开发指

| PreferredBackupP eriod | String | 是 | Tuesday | 备份周期： Monday：周一 Tuesday：周二 Wednesday： 周三 Thursday：周四 Friday：周五 Saturday：周六 Sunday：周日 |
|---|---|---|---|---|

**返回参数**

表 1. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=ModifyBackupPolicy &InstanceId=r-bp1zxszhcgatnx**** &PreferredBackupTime=00:00Z-04:00Z &PreferredBackupPeriod=Tuesday
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
```

JSON格式：

```json
{
    "RequestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
}
```

#### DescribeBackupPolicy

调用DescribeBackupPolicy查询Redis实例的备份策略，包括备份周期、备份时间等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |

云数据库 Tair（兼容Redis）开发指

| Action | String | 是 | DescribeBackupP olicy | 系统规定参数，取值： DescribeBackupP olicy。 |
|---|---|---|---|---|
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |
| BackupRetentionPerio d | String | 7 | 备份保留天数。 |
| PreferredBackupTime | String | 05:00Z-06:00Z | 备份时间，格式： HH:mmZ- HH:mm Z。 |
| PreferredBackupPeriod | String | Monday,Tuesday,Wed nesday,Thursday,Frida y,Saturday,Sunday | 备份周期： Monday：周一 Tuesday：周二 Wednesday：周三 Thursday：周四 Friday：周五 Saturday：周六 Sunday：周日 |
| PreferredNextBackupTi me | String | 2019-03-14T05:28Z | 下次备份时间 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeBackupPolicy &InstanceId=r-bp1zxszhcgatnx****
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
<PreferredBackupPeriod>Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday</Preferre ackupPeriod>
      <RequestId>90B82DB7-FB28-4CC2-ADBF-1F8659F3****</RequestId>
      <PreferredNextBackupTime>2018-10-26T19:05Z</PreferredNextBackupTime>
      <PreferredBackupTime>19:00Z-20:00Z</PreferredBackupTime>
      <BackupRetentionPeriod>7</BackupRetentionPeriod>
```

JSON格式： 云数据库 Tair（兼容Redis）开发指

```json
{
 "PreferredBackupPeriod": "Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday",
 "RequestId": "90B82DB7-FB28-4CC2-ADBF-1F8659F3****",
 "PreferredNextBackupTime": "2018-10-26T19:05Z",
 "PreferredBackupTime": "19:00Z-20:00Z",
 "BackupRetentionPeriod": "7"
}
```

#### DescribeBackups

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | DescribeBackups | 系统规定参数，取值： DescribeBackups 。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |
| BackupId | String | 否 | 11611111 | 备份集ID。 |
| PageSize | String | 是 | 30 | 每页记录数，取值：30/50/100。 |
| PageNumber | String | 是 | 1 | 页码，大于0，且不超过 Integer 的最大值。 |
| StartTime | String | 是 | 2019-03- 11T10:00Z | 查询开始时间。 |
| EndTime | String | 是 | 2019-03- 14T18:00Z | 查询结束时间。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |
| Backups | List | 无 | 由Backup组成的数组。 |
| PageNumber | Integer | 1 | 页码。 |
| TotalCount | Integer | 5 | 备份总个数。 |
| PageSize | Integer | 30 | 每页记录数。 |

云数据库 Tair（兼容Redis）开发指

**Backup 的参数构成**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupId | String | 111111111 | 备份集ID。 |
| BackupDBNames | String | all | 备份的DB名称。 |
| BackupStatus | String | Success | 备份集状态： Success：成功 Failed：失败 |
| BackupStartTime | String | 2019-03- 14T05:28:50Z | 备份开始时间。 |
| BackupEndTime | String | 2019-03- 14T05:31:13Z | 备份结束时间。 |
| BackupType | String | FullBackup | 备份类型： FullBackup：全量备份 IncrementalBackup ：增量备份 |
| BackupMode | String | Automated | 备份模式： Automated：自动备份 Manual：手工触发备份 |
| BackupMethod | String | Physical | 备份方法： Logical：逻辑备份 Physical：物理备份 |
| BackupDownloadURL | String | https://rdsbak-hk45- v2.oss-cn- hongkong.aliyuncs.co m/******** | 备份文件的URL下载地址。 |
| BackupSize | String | 1024 | 备份集大小。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeBackups &InstanceId=r-bp1zxszhcgatnx**** &StartTime=2019-03-11T10:00Z &EndTime=2019-03-14T18:00Z
```

`&<`公共请求参数>

**返回示例**

XML格式： 云数据库 Tair（兼容Redis）开发指

```xml
      <TotalCount>1</TotalCount>
      <RequestId>721E2D39-351D-40E2-BF7C-B5075B0A****</RequestId>
      <PageSize>30</PageSize>
      <PageNumber>1</PageNumber>
      <Backups>
            <Backup>
                  <BackupMethod>Physical</BackupMethod>
                  <EngineVersion>4.0</EngineVersion>
                  <BackupIntranetDownloadURL>http://rdsbak-hz-v3.oss-cn-hangzhou-interna
l.aliyuncs.com/********</BackupIntranetDownloadURL>
                  <BackupMode>Automated</BackupMode>
                  <BackupSize>2263040</BackupSize>
                  <BackupId>775661111</BackupId>
                  <NodeInstanceId>r-bp12fdcf4dea****</NodeInstanceId>
                  <BackupDBNames>all</BackupDBNames>
                  <BackupDownloadURL>http://rdsbak-hz-v3.oss-cn-
hangzhou.aliyuncs.com/********</BackupDownloadURL>
                  <BackupEndTime>2020-10-30T17:31:26Z</BackupEndTime>
                  <BackupStartTime>2020-10-30T17:28:28Z</BackupStartTime>
                  <BackupType>FullBackup</BackupType>
                  <BackupStatus>Success</BackupStatus>
            </Backup>
      </Backups>
```

JSON格式： 云数据库 Tair（兼容Redis）开发指

```json
{
    "TotalCount": 1,
    "RequestId": "721E2D39-351D-40E2-BF7C-B5075B0A****",
    "PageSize": 30,
    "PageNumber": 1,
    "Backups": {
        "Backup": [
            {
                "BackupMethod": "Physical",
                "EngineVersion": "4.0",
                "BackupIntranetDownloadURL": "http://rdsbak-hz-v3.oss-cn-hangzhou-intern
al.aliyuncs.com/********",
                "BackupMode": "Automated",
                "BackupSize": 2263040,
                "BackupId": 775661111,
                "NodeInstanceId": "r-bp12fdcf4dea****",
                "BackupDBNames": "all",
                "BackupDownloadURL": "http://rdsbak-hz-v3.oss-cn-
hangzhou.aliyuncs.com/********",
                "BackupEndTime": "2020-10-30T17:31:26Z",
                "BackupStartTime": "2020-10-30T17:28:28Z",
                "BackupType": "FullBackup",
                "BackupStatus": "Success"
            }
```

]

```
    }
}
```

#### RestoreInstance

调用RestoreInstance将备份文件中的数据恢复到当前Redis实例中，结合数据闪回更可实现将指定的Key 恢复至某个秒级时间点。

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | RestoreInstance | 系统规定参数，取值： RestoreInstance 。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |
| BackupId | String | 是 | 78241**** | 备份结果集ID。 |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库 Tair（兼容Redis）开发指

| 南·API参考 |  |  |  |
|---|---|---|---|

| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |
|---|---|---|---|

**请求示例**

```
http(s)://r-kvstore.aliyuncs.com/?Action=RestoreInstance &InstanceId=r-bp1zxszhcgatnx**** &RestoreType=1 &RestoreTime=2021-07-06T07:25:57Z &FilterKey=key:00000007198*
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
```

JSON格式：

```json
{
    "RequestId": "8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
}
```

### 监控管理

#### DescribeMonitorItems

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必须 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | DescribeMonitorIt ems | 系统规定参数，取值： DescribeMonitorIt ems。 |

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库 Tair（兼容Redis）开发指

| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |
|---|---|---|---|
| MonitorItems | List | 无 | 每个可查看的监控参数 List。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeMonitorItems
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
 <MonitorItems>
  <MonitorItem>
   <MonitorKey>GetQ</MonitorKey>
   <Unit>Counts/s</Unit>
  </MonitorItem>
  <MonitorItem>
   <MonitorKey>Flush</MonitorKey>
   <Unit>Counts/s</Unit>
  </MonitorItem>
  <MonitorItem>
   <MonitorKey>UsedMemCache</MonitorKey>
   <Unit>Bytes</Unit>
  </MonitorItem>
  <MonitorItem>
   <MonitorKey>ReplaceQ</MonitorKey>
   <Unit>Counts/s</Unit>
  </MonitorItem>
 </MonitorItems>
 <RequestId>B906A893-58A3-4644-AC2D-A2C9B08706C1</RequestId>
```

JSON格式： 云数据库 Tair（兼容Redis）开发指

```json
{
    "MonitorItems" : {
        "MonitorItem" : [{
                "MonitorKey" : "GetQ",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "Flush",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "UsedMemCache",
                "Unit" : "Bytes"
            }, {
                "MonitorKey" : "ReplaceQ",
                "Unit" : "Counts/s"
            }
```

]

```json
    },
    "RequestId" : "B906A893-58A3-4644-AC2D-A2C9B08706C1"
}
```

#### DescribeHistoryMonitorValues

调用DescribeHistoryMonitorValues查看Redis实例的性能监控信息。

**请求参数**

| 名称 | 类型 | 是否必须 | 示例值 |  | 描述 |  |  |
|---|---|---|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 |  | 参见公共请求参数。 |  |  |
| Action | String | 是 | DescribeHistoryM onitorValues |  | 系统规定参数，取值： DescribeHistoryM onitorValues。 |  |  |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** |  | 实例ID。 |  |  |
| StartTime | String | 是 | 2018-10- 18T12:00:00Z |  | 历史监控开始时间点；采用ISO8601 表示法，并使用 UTC 时间。格式为： YYYY-MM- DDThh:mm:ssZ 。 |  |  |
|  |  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  |  | DDThh:mm:ssZ |  |  |

云数据库 Tair（兼容Redis）开发指

| EndTime | String | 是 | 2018-10- 19T12:00:00Z |  | 历史监控结束时间点；采用ISO8601 表示法，并使用 UTC 时间。格式为： YYYY-MM- DDThh:mm:ssZ 。 EndTime 必须大于等于 StartTime。 |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  | 00Z | DDThh:mm:ssZ |  |  |
| IntervalForHistor y | String | 是 | 01m |  | 取值必须是01m、 05m、15m、 60m。 监控信息采样间隔，即每隔 N 分钟取一个监控采样点。 |  |  |
| MonitorKeys | String | 否 | CpuUsage |  | 监控项Key。通过函数 DescribeMonitorIt ems查询。 |  |  |

**返回参数**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |
| MonitorHistory | String | {\"2020-11- 18T00:00:00Z\": {\"CpuUsage\":\"0.30\" },\"2020-11- 18T00:02:00Z\": {\"CpuUsage\":\"0.60\" },\"2020-11- 18T00:03:00Z\": {\"CpuUsage\":\"0.60\" }} | 以 JSON 格式返回的监控信息。返回的监控项，参见DescribeMonitorItem s。 说明为了提高数据传输效率，只有非0的监控数据才会返回，其余未显示给出的监控数据均为默认值0。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeHistoryMonitorValues &InstanceId=r-bp1zxszhcgatnx**** &StartTime=2018-10-18T12:00:00Z &EndTime=2018-10-18T12:03:00Z &IntervalForHistory=01m &MonitorKeys=CpuUsage
```

`&<`公共请求参数>

**返回示例**

XML格式： 云数据库 Tair（兼容Redis）开发指

```xml
      <MonitorHistory>{"2020-11-18T00:00:00Z":{"CpuUsage":"0.30"},"2020-11-
18T00:02:00Z":{"CpuUsage":"0.60"},"2020-11-18T00:03:00Z":{"CpuUsage":"0.60"}} </MonitorHistory>
      <RequestId>689E8093-3094-4DC2-A2A2-30D40097****</RequestId>
```

JSON格式：

```json
{
 "MonitorHistory": "{\"2020-11-18T00:00:00Z\":{\"CpuUsage\":\"0.30\"},\"2020-11-18T00:0
2:00Z\":{\"CpuUsage\":\"0.60\"},\"2020-11-18T00:03:00Z\":{\"CpuUsage\":\"0.60\"}}",
 "RequestId": "689E8093-3094-4DC2-A2A2-30D40097****"
}
```

### 参数管理

#### DescribeInstanceConfig

调用DescribeInstanceConfig查询Redis实例的参数配置信息。

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | DescribeInstance Config | 系统规定参数，取值： DescribeInstance Config。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例ID。 |

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

云数据库 Tair（兼容Redis）开发指

| Config | String | {"#no loose statistics _ _ - cmds":"SET,GET","Evic tionPolicy":"volatile- lru","hash-max-ziplist- entries":512,"slowlog- log-slower- than":"1000","notify- keyspace- events":"$","zset-max- ziplist- entries":128,"list-max- ziplist- entries":512,"list-max- ziplist-value":64,"zset- max-ziplist- value":64,"set-max- intset- entries":512,"hash- max-ziplist- value":64,"#no loose _ _ disabled- commands":"flushall"} | 实例的配置参数。参见实例配置参数表。 |
|---|---|---|---|

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeInstanceConfig &InstanceId=r-bp1zxszhcgatnx****
```

`&<`公共请求参数>

**返回示例**

XML格式：

```xml
      <RequestId>4E2C08F6-2D11-4ECD-9A4C-27EF2D3D****</RequestId>
      <Config>{"#no_loose_statistics-cmds":"SET,GET","EvictionPolicy":"volatile-lru","h
ash-max-ziplist-entries":512,"slowlog-log-slower-than":"1000","notify-keyspace-events": "$","zset-max-ziplist-entries":128,"list-max-ziplist-entries":512,"list-max-ziplist-val ue":64,"zset-max-ziplist-value":64,"set-max-intset-entries":512,"hash-max-ziplist-value ":64,"#no_loose_disabled-commands":"flushall"}</Config>
```

JSON格式：

```json
{
    "RequestId": "4E2C08F6-2D11-4ECD-9A4C-27EF2D3D****",
    "Config": "{\"#no_loose_statistics-
cmds\":\"SET,GET\",\"EvictionPolicy\":\"volatile-lru\",\"hash-max-ziplistentries\":512,\"slowlog-log-slower-than\":\"1000\",\"notify-keyspaceevents\":\"$\",\"zset-max-ziplist-entries\":128,\"list-max-ziplistentries\":512,\"list-max-ziplist-value\":64,\"zset-max-ziplist-value\":64,\"set-max-int set-entries\":512,\"hash-max-ziplist-value\":64,\"#no_loose_disabledcommands\":\"flushall\"}" }
```

云数据库 Tair（兼容Redis）开发指

#### ModifyInstanceConfig

**请求参数**

表 1. 请求参数

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| <公共请求参数> | 无 | 是 | 无 | 参见公共请求参数。 |
| Action | String | 是 | ModifyInstanceCo nfig | 系统规定参数，取值： ModifyInstanceCo nfig。 |
| InstanceId | String | 是 | r- bp1zxszhcgatnx* *** | 实例 ID |
| Config | String | 是 | {"EvictionPolicy": "volatile-lru","list- max-ziplist- entries":512,"zse t-max-ziplist- entries":128,"has h-max-ziplist- entries":512,"has h-max-ziplist- value":64,"list- max-ziplist- value":64,"set- max-intset- entries":512,"zse t-max-ziplist- value":64} | 实例的配置参数 （Json String）。 参见实例配置参数表。 |

**返回参数**

表 2. 返回参数

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| <公共返回参数> | 无 | 无 | 参见公共返回参数。 |

**请求示例**

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceConfig &InstanceId=r-bp1zxszhcgatnx**** &Config={"EvictionPolicy":"volatile-lru","list-max-ziplist-entries":512,"zset-max-zipli st-entries":128,"hash-max-ziplist-entries":512,"hash-max-ziplist-value":64,"list-max-zi plist-value":64,"set-max-intset-entries":512,"zset-max-ziplist-value":64}
```

`&<`公共请求参数>

**返回示例**

XML格式： 云数据库 Tair（兼容Redis）开发指

```xml
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
```

JSON格式：

```json
{
  "requestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
}
```

### 附表

#### 错误码表

| 错误码描述 | Code | message | httpStatusCode |
|---|---|---|---|
| 子账号调用 API 未经授权 | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| 该操作不支持 RAM 模式访问 | Forbedden.NotSupport RAM | This action does not support accessed by RAM mode. | 403 |
| 服务器端异常错误 | ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |
| 输入的实例状态不存在 | InvalidStatus.NotFoun d | The Status provided does not exist in our records. | 404 |
| 输入的参数不合法 | InvalidParameter | The specified parameter InstanceName is not valid. | 400 |
| 普通用户调用管理类 API | Forbbiden.NotAdminUs er | User not authorized to operate on the specified API as you are not the administrator. | 403 |
| 缺少参数 | MissingParameter | Specified parameter is missing. | 400 |
| 至少需要包含 InstanceName 或 NewPassword 参数两者之一 | MissingParameter | InstanceName/NewPas sword at least one is mandatory for this action. | 400 |

云数据库 Tair（兼容Redis）开发指

| 调用该接口没有指定 OwnerId | MissingParameter | The input parameter OwnerId, OwnerAccount that is mandatory for processing this request is not supplied. | 403 |
|---|---|---|---|
| 指定的参数 Token 不合法 | InvalidToken.Malforme d | The Specified parameter "Token" is not valid. | 400 |
| 指定的参数 InstanceName 不合法 | InvalidInstanceName. Malformed | The Specified parameter "InstanceName" is not valid. | 400 |
| 指定的参数 Password 不合法 | InvalidPassword.Malfor med | The Specified parameter "Password" is not valid." | 400 |
| 指定的参数 Instances 不合法 | InvalidInstances.Malfor med | The Specified parameter "Instances" is not valid. | 400 |
| 指定的参数 StartTime 不合法 | InvalidStartTime.Malfo rmed | The Specified parameter "StartTime" is not valid. | 400 |
| 指定的参数 EndTime 不合法 | InvalidEndTime.Malfor med | The Specified parameter "EndTime" is not valid. | 400 |
| 指定的参数 InstanceIds 不合法 | InvalidInstanceIds.Malf ormed | The Specified parameter "InstanceIds" is not valid. | 400 |
| 余额不足 | InsufficientBalance | Your account does not have enough balance. | 400 |
| 用户未进行实名认证 | RealNameAuthenticati onError | Your account has not passed the real-name authentication yet. | 403 |
| 购买数量超出限制 | QuotaExcee | Living afterpay instances quota exceeded. | 400 |
| 容量配置不合法 | InvalidCapacity.NotFou nd | The Capacity provided does not exist in our records. | 400 |
| 用了一个已经使用过的 ClientToken，但此次请求内容却又与上一次使用该 Token 的请求内容又不一样 | IdempotentParameter Mismatch | Request uses a client token in a previous request but is not identical to that request. | 400 |
| 指定的可用区库存不足 | QuotaNotEnough | Quota not enough in this zone. | 400 |

云数据库 Tair（兼容Redis）开发指

| 无权调用订单类接口 | Forbbiden.SubUser | The specified action is not available for you. | 403 |
|---|---|---|---|
| 阿里云风控系统拒绝了此次访问 | Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| 指定的 Region 不存在 | InvalidRegion.NotFoun d | The RegionId or ZoneId provided does not exist in our records. | 404 |
| 指定的 ZoneId 不合法 | InvalidZoneId.NotFoun d | The ZoneId provided is invalid. | 400 |
| 实例 ID 不存在 | InvalidInstanceId.NotF ound | The InstanceId provided does not exist in our records. | 404 |
| 密码不正确 | IncorrectPassword | The Password provided is not correct. | 400 |
| 服务不可用 | ServiceNotSupported | The specified service is not supported. | 400 |
| 有未生效的续费变配订单 | HasRenewChangeOrde r | This instance has a renewChange order. | 400 |
| 内部错误 | InternalError | The request processing has failed due to some unknown error. | 500 |
| 备份时间无效 | InvalidPreferredBacku pTime | Specified preferred backup time is not valid. | 400 |
| 输入备份类型不合法 | InvalidBackupType.For mat | Specified backup type is not valid. | 400 |
| 输入的备份方法不合法 | InvalidBackupMethod. Format | Specified backup method is not valid. | 400 |
| 备份任务已经存在，暂不能支持 | BackupJobExists | A backup job already exists in the specified DB instance. | 400 |
| 备份次数已经超出限制 | BackupTimesExceeded | Exceeding the daily backup times of this DB instance. | 400 |
| 必须输入一个参数 | ParameterLeastAssoci ate | Must input at least one optional parameter. | 400 |
| 输入的备份周期不合法 | InvalidBackupRetentio nPeriod.Malformed | Specified backup retention period is not valid. | 400 |

云数据库 Tair（兼容Redis）开发指

| 输入的下次备份时间不合法 | InvalidPreferredBacku pTime.Format | Specified preferred backup time is not valid. | 400 |
|---|---|---|---|
| 输入的备份周期不合法 | InvalidPreferredBacku pPeriod.Malformed | Specified backup period is not valid. | 400 |
| 当前的实例类型不支持此操作 | IncorrectDBInstanceTy pe | Current DB instance type does not support this operation | 400 |
| 输入的 key 不合法 | InvalidKey.Malformed | Specified key is not valid. | 400 |
| 签名已经被使用 | SignatureNonceUsed | Specified signature nonce was used already. | 400 |
| 已经无法分配虚拟 ip | AllocateVpcIp.NotEnou gh | Ip resource is not enough | 400 |
| 该可用区不支持创建此类型实例 | Zone.NotSupport | Specified zone does not support creating with instance class. | 400 |
| 规格代码不合法 | MissingClassCode | Capacity or InstanceClass is mandatory for this action. | 400 |
| 实例规格不支持 | InvalidDBInstanceClas s.NotFound | Specified DB instance class is not found. | 404 |
| 实例已经被锁定 | IncorrectDBInstanceLo ckMode | Current DB instance lock mode does not support this operation. | 400 |
| 备份集 Id 不存在 | InvalidBackupSetID.No tFound | Specified backup set ID does not exist. | 400 |
| 实例状态不支持此操作 | IncorrectDBInstanceSt ate | Current DB instance state does not support this operation. | 400 |
| 资源不足 | InsufficientResourceCa pacity | There is insufficient capacity available for the requested instance. | 400 |
| 输入的结束时间无效 | InvalidEndTime.Format | Specified end time is not valid. | 400 |
| 输入的保留经典 ip 的时间长度不合法 | InvalidClassicExpiredD ays.Format | The specified classicExpiredDays format is not valid. | 400 |
| 备份集状态不支持此操作 | IncorrectBackupSetSta te | Current backup set state does not support operations. | 400 |

云数据库 Tair（兼容Redis）开发指

| 白名单格式不合法 | InvalidSecurityIPList.Fo rmat | Specified security IP list format is not valid. | 400 |
|---|---|---|---|

#### 实例配置参数表

表 1. Redis 实例参数配置表

| 参数名称 | 参数含义 | 参数值 |
|---|---|---|
| maxmemory-policy | 内存超过阈值时的逐出策略，云数据库KVStore for Memcache支持 6 种数据逐出策略。 | VolatileLRU：按照 LRU 算法逐出原有数据，但仅逐出设置了过期时间的数据。 VolatileTTL: 仅逐出设置了过期时间的数据，并且是按照 TTL 由小到大的顺序进行逐出。 AllKeysLRU: 按照 LRU 算法逐出原有数据。 VolatileRandom: 随机逐出原有数据，但仅逐出设置了过期时间的数据。 AllKeysRandom: 随机逐出原有数据。 NoEviction: 不逐出任何数据， 新数据的写入会得到一个错误信息。 |
| hash-max-ziplist-entries | 当 hash 对象同时满足以下两个条件时， hash 对象使用 ziplist 编码： hash 对象保存的键值对数量小于或者等于 list-max-ziplist- entries 参数值。 hash 对象保存的所有键值对的键和值的字符串长度都小于或者等于 list-max-ziplist-value 参数值。 | 默认值：512 |
| hash-max-ziplist-value | 当 hash 对象同时满足以下两个条件时， hash 对象使用 ziplist 编码： hash 对象保存的键值对数量小于或者等于 list-max-ziplist- entries 参数值。 hash 对象保存的所有键值对的键和值的字符串长度都小于或者等于 list-max-ziplist-value 参数值。 | 默认值：64 |
| list-max-ziplist-entries | 当 list 对象同时满足以下两个条件时，list 对象使用 ziplist 编码： list 对象保存的键值对数量小于或者等于 list-max-ziplist-entries 参数值。 list 对象保存的所有键值对的键和值的字符串长度都小于或者等于 list-max-ziplist-value 参数值。 | 默认值：512 |

云数据库 Tair（兼容Redis）开发指

| list-max-ziplist-value | 当 list 对象同时满足以下两个条件时，list 对象使用 ziplist 编码： list 对象保存的键值对数量小于或者等于 list-max-ziplist-entries 参数值。 list 对象保存的所有键值对的键和值的字符串长度都小于或者等于 list-max-ziplist-value 参数值。 | 默认值：64 |  |  |
|---|---|---|---|---|
| set-max-intset-entries | 当 set 对象满足条目小于或者等于 set-max-intset-entries 参数值并且都是十进制整数时，编码为 intset。 | 默认值：512 |  |  |
| zset-max-ziplist-entries | 当 zset 对象同时满足以下两个条件时，zset 对象使用 ziplist 编码： zset 对象保存的键值对数量小于或者等于 zset-max-ziplist- entries 参数值。 zset 对象保存的所有键值对的键和值的字符串长度都小于或者等于 zset-max-ziplist-value 参数值。 | 默认值：128 |  |  |
| zset-max-ziplist-value | 当 zset 对象同时满足以下两个条件时，zset 对象使用 ziplist 编码： zset 对象保存的键值对数量小于或者等于 zset-max-ziplist- entries 参数值。 zset 对象保存的所有键值对的键和值的字符串长度都小于或者等于 zset-max-ziplist-value 参数值。 | 默认值：64 |  |  |
| notify-keyspace-events | 键空间通知使得客户端可以通过订阅频道或模式来接收那些以某种方式改动了 Redis 数据集的事件。 | K 键空间通知，所有通知以 \ keyspace\@ \ 为前缀。 __ _ _ E 键事件通知，所有通知以 keyevent@ 为前缀。 __ __ g DEL 、 EXPIRE 、 RENAME 等类型无关的通用命令的通知。 $ 字符串命令的通知。 l 列表命令的通知。 s 集合命令的通知。 h 哈希命令的通知。 z 有序集合命令的通知。 x 过期事件：每当有过期键被删除时发送。 e 驱逐（evict）事件：每当有键因为 maxmemory 政策而被删除时发送。 A 参数 g$lshzxe 的别名。 |  |  |
